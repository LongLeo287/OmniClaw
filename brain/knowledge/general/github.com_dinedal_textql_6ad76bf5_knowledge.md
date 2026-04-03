---
id: github.com-dinedal-textql-6ad76bf5-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:44.973654
---

# KNOWLEDGE EXTRACT: github.com_dinedal_textql_6ad76bf5
> **Extracted on:** 2026-04-01 10:29:09
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520904/github.com_dinedal_textql_6ad76bf5

---

## File: `.SRCINFO`
```
pkgbase = textql-git
	pkgdesc = Execute SQL against structured text like CSV or TSV
	pkgver = 2.0.3
	pkgrel = 1
	url = https://github.com/dinedal/textql
	arch = x86_64
	arch = i686
	license = MIT
	makedepends = git
	depends = go
	options = !strip
	options = !emptydirs

pkgname = textql-git

```

## File: `.gitignore`
```
vendor/
glide
build/
```

## File: `.travis.yml`
```yaml
os: linux
arch:
 - amd64
 - ppc64le
language: go
sudo: false

go:
  - '1.13.x'

install: make
```

## File: `Dockerfile`
```
FROM golang:1.10

# install sqlite3 for option "-console"
RUN apt-get update && apt-get install -y sqlite3

WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

WORKDIR /tmp

ENTRYPOINT ["textql"]
```

## File: `Dockerfile.alpine`
```
FROM golang:1.10-alpine3.7 AS build

# "build-base" for gcc
RUN apk update && apk add git && apk add build-base
WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

FROM alpine:3.7
RUN apk add --update-cache sqlite
COPY --from=build /go/bin/textql /usr/bin
WORKDIR /tmp
ENTRYPOINT ["textql"]

```

## File: `LICENSE`
```
MIT License
-----------

Copyright (c) 2014, Paul Bergeron

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

## File: `Makefile`
```
.PHONY: all test clean man godep fast release install

all: textql

textql: test
	go build -ldflags "-X main.VERSION=`cat VERSION` -s" -o ./build/textql ./textql/main.go

fast:
	go build -i -ldflags "-X main.VERSION=`cat VERSION`-dev -s" -o ./build/textql ./textql/main.go

test:
	go test ./...

clean:
	rm -fr ./build

release: textql
	git tag -a `cat VERSION`
	git push origin `cat VERSION`

install: test
	go install -ldflags "-X main.VERSION=`cat VERSION` -s" ./textql/main.go

man:
	ronn man/textql.1.ronn
```

## File: `PKGBUILD`
```
# Maintainer: Aniket-Pradhan aniket17133@iiitd.ac.in
# Owner/Cofntributer: Paul Bergeron https://github.com/dinedal

pkgname=textql-git
pkgver=2.0.3
pkgrel=1
pkgdesc="Execute SQL against structured text like CSV or TSV"
arch=('x86_64' 'i686')
url="https://github.com/dinedal/textql"
license=('MIT')
depends=('go')
makedepends=('git')
options=('!strip' '!emptydirs')
_gourl=github.com/dinedal/textql

build() {
  GOPATH="$srcdir" go get -v -u ${_gourl}/...
}

check() {
  echo $GOPATH
  echo $srcdir
  GOPATH="$GOPATH:$srcdir" go test -v ${_gourl}/...
}

package() {
  mkdir -p "$pkgdir/usr/bin"
  install -p -m755 "$srcdir/bin/"* "$pkgdir/usr/bin"

  mkdir -p "$pkgdir/$GOPATH"
  cp -Rv --preserve=timestamps "$srcdir/"{src,pkg} "$pkgdir/$GOPATH"

  for f in LICENSE COPYING LICENSE.* COPYING.*; do
    if [ -e "$srcdir/src/$_gourl/$f" ]; then
      install -Dm644 "$srcdir/src/$_gourl/$f" \
        "$pkgdir/usr/share/licenses/$pkgname/$f"
    fi
  done
}

# vim:set ts=2 sw=2 et:
```

## File: `Readme.md`
```markdown
# TextQL

[![Build Status](https://travis-ci.org/dinedal/textql.svg)](https://travis-ci.org/dinedal/textql) [![Go Report Card](http://goreportcard.com/badge/dinedal/textql)](http://goreportcard.com/report/dinedal/textql)

Allows you to easily execute SQL against structured text like CSV or TSV.

Example session:

![textql_usage_session](https://raw.github.com/dinedal/textql/master/textql_usage.gif)

## Major changes!

In the time since the initial release of textql, I've made some improvements as well as made the project much more modular. There've also been additional performance tweaks and added functionality, but this comes at the cost of breaking the original command-line flags and changing the install command.

### Changes since v1

Additions:

- Numeric values are automatically recognized in more cases.
- Date / Time / DateTime values are automatically recognized in reasonable formats. See [Time Strings](https://www.sqlite.org/lang_datefunc.html) for a list for accepted formats, and how to convert from other formats.
- Added join support! Multiple files / directories can be loaded by listing them at the end of the command.
- Directories are read by reading each file inside, and this is non-recursive.
- You can list as many files / directories as you like.
- Added flag '-output-file' to save output directly to a file.
- Added flag '-output-dlm' to modify the output delimiter.
- Added "short SQL" syntax.
  - For the case of a single table, the `FROM [table]` can be dropped from the query.
  - For simple selects, the `SELECT` keyword can be dropped from the query.
  - This means the v1 command `textql -sql "select * from tbl" -source some_file.csv` can be shortened to `textql -sql "*" some_file.csv`

Changes:

- The flag '-outputHeader' was renamed to '-output-header'.

Removals:

- Dropped the ability to override table names. This makes less sense after the automatic tablename generation based on filename, joins, and shorter SQL syntax changes.
- Removed '-source', any files / paths at the end of the command are used, as well as piped-in data.

Bug fixes:

- Writing to a directory no longer fails silently.

## Key differences between textql and sqlite importing

- sqlite import will not accept stdin, breaking unix pipes. textql will happily do so.
- textql supports quote-escaped delimiters, sqlite does not.
- textql leverages the sqlite in-memory database feature as much as possible and only touches disk if asked.

## Is it any good?

[Yes](https://news.ycombinator.com/item?id=3067434)

## Requirements

- Go 1.4 or later

## Install

**Latest release on Homebrew (OS X)**

```bash
brew install textql
```

**Build from source**

```bash
go get -u github.com/dinedal/textql/...
```

## Docker

First build the image.

```bash
docker build -t textql .
```

Now use that image mounting your current directory into the container.

```bash
docker run --rm -it -v $(pwd):/tmp textql [rest_of_command]
```

### Alias

You can add the following alias to your system to provide quick access to TextQL:

```bash
alias textql='docker run --rm -it -v $(pwd):/tmp textql '
```

## AUR

**Using an AUR-Helper**

```bash
yaourt textql-git
```

**Building from PKGBUILD**
First clone the repository.
```bash
makepkg -cs
```
Then install the package using pacman or your favorite Package Manager


## Usage

```bash
  textql [-console] [-save-to path path] [-output-file path] [-output-dlm delimter] [-output-header] [-pretty] [-quiet] [-header] [-dlm delimter] [-sql sql_statements] [path ...]

  -console
        After all statements are run, open SQLite3 REPL with this data
  -dlm string
        Input delimiter character between fields -dlm=tab for tab, -dlm=0x## to specify a character code in hex (default ",")
  -header
        Treat input files as having the first row as a header row
  -output-dlm string
        Output delimiter character between fields -output-dlm=tab for tab, -dlm=0x## to specify a character code in hex (default ",")
  -output-file file
        Filename to write output to, if empty no output is written (default "stdout")
  -output-header
        Display column names in output
  -quiet
        Suppress logging
  -pretty
        Pretty print output
  -save-to file
        SQLite3 db is left on disk at this file
  -sql string
        SQL Statement(s) to run on the data
  -version
        Print version and exit
```

## I want stdev, average, other functions

Just follow the install directions at [go-sqlite3-extension-functions](https://github.com/dinedal/go-sqlite3-extension-functions) and textql will automatically load this library.

Full function list:

- Math: acos, asin, atan, atn2, atan2, acosh, asinh, atanh, difference, degrees, radians, cos, sin, tan, cot, cosh, sinh, tanh, coth, exp, log, log10, power, sign, sqrt, square, ceil, floor, pi.
- String: replicate, charindex, leftstr, rightstr, ltrim, rtrim, trim, replace, reverse, proper, padl, padr, padc, strfilter.
- Aggregate: stdev, variance, mode, median, lower_quartile, upper_quartile

## License

New MIT License - Copyright (c) 2015, 2016 Paul Bergeron [http://pauldbergeron.com/](http://pauldbergeron.com/)

See LICENSE for details
```

## File: `TODO.txt`
```
Install is really complex with vitess dep. Find a way to fix it?

~ go get -u github.com/dinedal/textql/...
# github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_int.go:7: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_custom.go:7
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_map.go:7: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_int.go:7
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_mixed.go:11: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_map.go:7
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_private.go:7: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_mixed.go:11
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_ptr.go:7: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_private.go:7
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_simple.go:9: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_ptr.go:7
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_slice.go:7: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_simple.go:9
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_tag.go:7: MyType redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/input_slice.go:7
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/output_int.go:29: (*MyType).UnmarshalBson redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/output_custom.go:42
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/output_map.go:18: (*MyType).MarshalBson redeclared in this block
    previous declaration at go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/output_custom.go:19
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/data/test/bson_test/output_map.go:18: too many errors
# pkg-config --cflags gomysql
Package gomysql was not found in the pkg-config search path.
Perhaps you should add the directory containing `gomysql.pc'
to the PKG_CONFIG_PATH environment variable
No package 'gomysql' found
pkg-config: exit status 1
# launchpad.net/gozk/zookeeper
go/src/launchpad.net/gozk/zookeeper/zk.go:15:10: fatal error: 'zookeeper.h' file not found
#include <zookeeper.h>
         ^
1 error generated.
# github.com/youtube/vitess/go/stats/influxdbbackend
go/src/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:40: undefined: client.ClientConfig
go/src/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:60: undefined: client.Series
go/src/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:62: undefined: client.Series
go/src/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:73: backend.client.WriteSeries undefined (type *client.Client has no field or method WriteSeries)
# github.com/youtube/vitess/go/terminal
go/src/github.com/youtube/vitess/go/terminal/tty.go:16: undefined: syscall.TCGETS
# pkg-config --cflags gomysql
Package gomysql was not found in the pkg-config search path.
Perhaps you should add the directory containing `gomysql.pc'
to the PKG_CONFIG_PATH environment variable
No package 'gomysql' found
pkg-config: exit status 1
# github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/stats/influxdbbackend
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:40: undefined: client.ClientConfig
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:60: undefined: client.Series
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:62: undefined: client.Series
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/stats/influxdbbackend/influxdb_backend.go:73: backend.client.WriteSeries undefined (type *client.Client has no field or method WriteSeries)
# github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/terminal
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/go/terminal/tty.go:16: undefined: syscall.TCGETS
# github.com/dinedal/textql/vendor/github.com/youtube/vitess/third_party/go/launchpad.net/gozk/zookeeper
go/src/github.com/dinedal/textql/vendor/github.com/youtube/vitess/third_party/go/launchpad.net/gozk/zookeeper/zk.go:15:10: fatal error: 'zookeeper.h' file not found
#include <zookeeper.h>
         ^
1 error generated.



Fix all the below:


Gofmt formats Go programs. We run gofmt -s on your code, where -s is for the "simplify" command

/github.com/dinedal/textql/outputs/csv.go
/github.com/dinedal/textql/vault/sqlite_test.go

Gocyclo calculates cyclomatic complexities of functions in Go source code. The cyclomatic complexity of a function is calculated according to the following rules: 1 is the base complexity of a function +1 for each 'if', 'for', 'case', '&&' or '||'

/github.com/dinedal/textql/cmd/textql.go
Line 106: 24 main main repos/src/github.com/dinedal/textql/cmd/textql.go:106:1
/github.com/dinedal/textql/sqlparser/parsed_query.go
Line 53: 18 sqlparser EncodeValue repos/src/github.com/dinedal/textql/sqlparser/parsed_query.go:53:1
/github.com/dinedal/textql/sqlparser/sql.go
/github.com/dinedal/textql/sqlparser/token.go
Line 141: 31 sqlparser (*Tokenizer).Scan repos/src/github.com/dinedal/textql/sqlparser/token.go:141:1
Line 297: 16 sqlparser (*Tokenizer).scanNumber repos/src/github.com/dinedal/textql/sqlparser/token.go:297:1
/github.com/dinedal/textql/sqlparser/tracked_buffer.go
Line 40: 18 sqlparser (*TrackedBuffer).Myprintf repos/src/github.com/dinedal/textql/sqlparser/tracked_buffer.go:40:1
gofmt
89%
golint
10%
Golint is a linter for Go source code.

/github.com/dinedal/textql/cmd/textql.go
Line 18: exported type CommandLineOptions should have comment or be unexported
Line 32: exported var VERSION should have comment or be unexported
Line 34: exported function NewCommandLineOptions should have comment or be unexported
Line 52: exported method CommandLineOptions.GetCommands should have comment or be unexported
Line 52: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 56: exported method CommandLineOptions.GetSourceFiles should have comment or be unexported
Line 56: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 60: exported method CommandLineOptions.GetDelimiter should have comment or be unexported
Line 60: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 64: exported method CommandLineOptions.GetHeader should have comment or be unexported
Line 64: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 68: exported method CommandLineOptions.GetOutputHeader should have comment or be unexported
Line 68: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 72: exported method CommandLineOptions.GetOutputDelimiter should have comment or be unexported
Line 72: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 76: exported method CommandLineOptions.GetOutputFile should have comment or be unexported
Line 76: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 80: exported method CommandLineOptions.GetSaveTo should have comment or be unexported
Line 80: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 84: exported method CommandLineOptions.GetConsole should have comment or be unexported
Line 84: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 88: exported method CommandLineOptions.GetVersion should have comment or be unexported
Line 88: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 92: exported method CommandLineOptions.GetQuiet should have comment or be unexported
Line 92: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 96: exported method CommandLineOptions.Usage should have comment or be unexported
Line 96: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 133: can probably use "var inputSources []string" instead
/github.com/dinedal/textql/inputs/csv.go
Line 21: exported type CSVInputOptions should have comment or be unexported
Line 27: exported function NewCSVInput should have comment or be unexported
Line 27: exported func NewCSVInput returns unexported type *inputs.csvInput, which can be annoying to use
Line 49: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 53: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 57: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 84: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 106: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
/github.com/dinedal/textql/inputs/input.go
Line 3: exported type Input should have comment or be unexported
/github.com/dinedal/textql/outputs/csv.go
Line 18: exported type CSVOutputOptions should have comment or be unexported
Line 24: exported function NewCSVOutput should have comment or be unexported
Line 24: exported func NewCSVOutput returns unexported type *outputs.csvOutput, which can be annoying to use
Line 35: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 53: should omit 2nd value from range; this loop is equivalent to `for i := range ...`
/github.com/dinedal/textql/outputs/output.go
Line 5: exported type Output should have comment or be unexported
/github.com/dinedal/textql/sqlparser/analyzer.go
Line 50: comment on exported function HasINClause should be of the form "HasINClause ..."
/github.com/dinedal/textql/sqlparser/ast.go
Line 56: exported method Union.IStatement should have comment or be unexported
Line 57: exported method Select.IStatement should have comment or be unexported
Line 58: exported method Insert.IStatement should have comment or be unexported
Line 59: exported method Update.IStatement should have comment or be unexported
Line 60: exported method Delete.IStatement should have comment or be unexported
Line 61: exported method Set.IStatement should have comment or be unexported
Line 62: exported method DDL.IStatement should have comment or be unexported
Line 63: exported method Other.IStatement should have comment or be unexported
Line 73: exported method Select.ISelectStatement should have comment or be unexported
Line 74: exported method Union.ISelectStatement should have comment or be unexported
Line 92: don't use ALL_CAPS in Go names; use CamelCase
Line 97: don't use ALL_CAPS in Go names; use CamelCase
Line 98: don't use ALL_CAPS in Go names; use CamelCase
Line 101: exported method Select.Format should have comment or be unexported
Line 117: don't use ALL_CAPS in Go names; use CamelCase
Line 118: don't use ALL_CAPS in Go names; use CamelCase
Line 119: don't use ALL_CAPS in Go names; use CamelCase
Line 120: don't use ALL_CAPS in Go names; use CamelCase
Line 121: don't use ALL_CAPS in Go names; use CamelCase
Line 124: exported method Union.Format should have comment or be unexported
Line 137: exported method Insert.Format should have comment or be unexported
Line 149: exported method Select.IInsertRows should have comment or be unexported
Line 150: exported method Union.IInsertRows should have comment or be unexported
Line 151: exported method Values.IInsertRows should have comment or be unexported
Line 163: exported method Update.Format should have comment or be unexported
Line 178: exported method Delete.Format should have comment or be unexported
Line 190: exported method Set.Format should have comment or be unexported
Line 204: don't use ALL_CAPS in Go names; use CamelCase
Line 204: exported const AST_CREATE should have comment (or a comment on this block) or be unexported
Line 205: don't use ALL_CAPS in Go names; use CamelCase
Line 206: don't use ALL_CAPS in Go names; use CamelCase
Line 207: don't use ALL_CAPS in Go names; use CamelCase
Line 210: exported method DDL.Format should have comment or be unexported
Line 226: exported method Other.Format should have comment or be unexported
Line 233: exported method Comments.Format should have comment or be unexported
Line 242: exported method SelectExprs.Format should have comment or be unexported
Line 256: exported method StarExpr.ISelectExpr should have comment or be unexported
Line 257: exported method NonStarExpr.ISelectExpr should have comment or be unexported
Line 264: exported method StarExpr.Format should have comment or be unexported
Line 277: exported method NonStarExpr.Format should have comment or be unexported
Line 290: exported method Columns.Format should have comment or be unexported
Line 300: exported method TableExprs.Format should have comment or be unexported
Line 314: exported method AliasedTableExpr.ITableExpr should have comment or be unexported
Line 315: exported method ParenTableExpr.ITableExpr should have comment or be unexported
Line 316: exported method JoinTableExpr.ITableExpr should have comment or be unexported
Line 326: exported method AliasedTableExpr.Format should have comment or be unexported
Line 343: exported method TableName.ISimpleTableExpr should have comment or be unexported
Line 344: exported method Subquery.ISimpleTableExpr should have comment or be unexported
Line 351: exported method TableName.Format should have comment or be unexported
Line 364: exported method ParenTableExpr.Format should have comment or be unexported
Line 378: don't use ALL_CAPS in Go names; use CamelCase
Line 379: don't use ALL_CAPS in Go names; use CamelCase
Line 380: don't use ALL_CAPS in Go names; use CamelCase
Line 381: don't use ALL_CAPS in Go names; use CamelCase
Line 382: don't use ALL_CAPS in Go names; use CamelCase
Line 383: don't use ALL_CAPS in Go names; use CamelCase
Line 386: exported method JoinTableExpr.Format should have comment or be unexported
Line 400: don't use ALL_CAPS in Go names; use CamelCase
Line 400: exported const AST_USE should have comment (or a comment on this block) or be unexported
Line 401: don't use ALL_CAPS in Go names; use CamelCase
Line 402: don't use ALL_CAPS in Go names; use CamelCase
Line 405: exported method IndexHints.Format should have comment or be unexported
Line 423: don't use ALL_CAPS in Go names; use CamelCase
Line 424: don't use ALL_CAPS in Go names; use CamelCase
Line 436: exported method Where.Format should have comment or be unexported
Line 451: don't use ALL_CAPS in Go names; use CamelCase
Line 463: exported method From.Format should have comment or be unexported
Line 476: exported method AndExpr.IExpr should have comment or be unexported
Line 477: exported method OrExpr.IExpr should have comment or be unexported
Line 478: exported method NotExpr.IExpr should have comment or be unexported
Line 479: exported method ParenBoolExpr.IExpr should have comment or be unexported
Line 480: exported method ComparisonExpr.IExpr should have comment or be unexported
Line 481: exported method RangeCond.IExpr should have comment or be unexported
Line 482: exported method NullCheck.IExpr should have comment or be unexported
Line 483: exported method ExistsExpr.IExpr should have comment or be unexported
Line 484: exported method KeyrangeExpr.IExpr should have comment or be unexported
Line 485: exported method StrVal.IExpr should have comment or be unexported
Line 486: exported method NumVal.IExpr should have comment or be unexported
Line 487: exported method ValArg.IExpr should have comment or be unexported
Line 488: exported method NullVal.IExpr should have comment or be unexported
Line 489: exported method ColName.IExpr should have comment or be unexported
Line 490: exported method ValTuple.IExpr should have comment or be unexported
Line 491: exported method Subquery.IExpr should have comment or be unexported
Line 492: exported method ListArg.IExpr should have comment or be unexported
Line 493: exported method BinaryExpr.IExpr should have comment or be unexported
Line 494: exported method UnaryExpr.IExpr should have comment or be unexported
Line 495: exported method FuncExpr.IExpr should have comment or be unexported
Line 496: exported method CaseExpr.IExpr should have comment or be unexported
Line 504: exported method AndExpr.IBoolExpr should have comment or be unexported
Line 505: exported method OrExpr.IBoolExpr should have comment or be unexported
Line 506: exported method NotExpr.IBoolExpr should have comment or be unexported
Line 507: exported method ParenBoolExpr.IBoolExpr should have comment or be unexported
Line 508: exported method ComparisonExpr.IBoolExpr should have comment or be unexported
Line 509: exported method RangeCond.IBoolExpr should have comment or be unexported
Line 510: exported method NullCheck.IBoolExpr should have comment or be unexported
Line 511: exported method ExistsExpr.IBoolExpr should have comment or be unexported
Line 512: exported method KeyrangeExpr.IBoolExpr should have comment or be unexported
Line 519: exported method AndExpr.Format should have comment or be unexported
Line 528: exported method OrExpr.Format should have comment or be unexported
Line 537: exported method NotExpr.Format should have comment or be unexported
Line 546: exported method ParenBoolExpr.Format should have comment or be unexported
Line 558: don't use ALL_CAPS in Go names; use CamelCase
Line 559: don't use ALL_CAPS in Go names; use CamelCase
Line 560: don't use ALL_CAPS in Go names; use CamelCase
Line 561: don't use ALL_CAPS in Go names; use CamelCase
Line 562: don't use ALL_CAPS in Go names; use CamelCase
Line 563: don't use ALL_CAPS in Go names; use CamelCase
Line 564: don't use ALL_CAPS in Go names; use CamelCase
Line 565: don't use ALL_CAPS in Go names; use CamelCase
Line 566: don't use ALL_CAPS in Go names; use CamelCase
Line 567: don't use ALL_CAPS in Go names; use CamelCase
Line 568: don't use ALL_CAPS in Go names; use CamelCase
Line 571: exported method ComparisonExpr.Format should have comment or be unexported
Line 584: don't use ALL_CAPS in Go names; use CamelCase
Line 585: don't use ALL_CAPS in Go names; use CamelCase
Line 588: exported method RangeCond.Format should have comment or be unexported
Line 600: don't use ALL_CAPS in Go names; use CamelCase
Line 601: don't use ALL_CAPS in Go names; use CamelCase
Line 604: exported method NullCheck.Format should have comment or be unexported
Line 613: exported method ExistsExpr.Format should have comment or be unexported
Line 622: exported method KeyrangeExpr.Format should have comment or be unexported
Line 632: exported method StrVal.IValExpr should have comment or be unexported
Line 633: exported method NumVal.IValExpr should have comment or be unexported
Line 634: exported method ValArg.IValExpr should have comment or be unexported
Line 635: exported method NullVal.IValExpr should have comment or be unexported
Line 636: exported method ColName.IValExpr should have comment or be unexported
Line 637: exported method ValTuple.IValExpr should have comment or be unexported
Line 638: exported method Subquery.IValExpr should have comment or be unexported
Line 639: exported method ListArg.IValExpr should have comment or be unexported
Line 640: exported method BinaryExpr.IValExpr should have comment or be unexported
Line 641: exported method UnaryExpr.IValExpr should have comment or be unexported
Line 642: exported method FuncExpr.IValExpr should have comment or be unexported
Line 643: exported method CaseExpr.IValExpr should have comment or be unexported
Line 648: exported method StrVal.Format should have comment or be unexported
Line 656: exported method NumVal.Format should have comment or be unexported
Line 663: exported method ValArg.Format should have comment or be unexported
Line 670: exported method NullVal.Format should have comment or be unexported
Line 679: exported method ColName.Format should have comment or be unexported
Line 702: exported method ValTuple.IColTuple should have comment or be unexported
Line 703: exported method Subquery.IColTuple should have comment or be unexported
Line 704: exported method ListArg.IColTuple should have comment or be unexported
Line 709: exported method ValTuple.Format should have comment or be unexported
Line 717: exported method ValExprs.Format should have comment or be unexported
Line 730: exported method Subquery.Format should have comment or be unexported
Line 737: exported method ListArg.Format should have comment or be unexported
Line 749: don't use ALL_CAPS in Go names; use CamelCase
Line 750: don't use ALL_CAPS in Go names; use CamelCase
Line 751: don't use ALL_CAPS in Go names; use CamelCase
Line 752: don't use ALL_CAPS in Go names; use CamelCase
Line 753: don't use ALL_CAPS in Go names; use CamelCase
Line 754: don't use ALL_CAPS in Go names; use CamelCase
Line 755: don't use ALL_CAPS in Go names; use CamelCase
Line 756: don't use ALL_CAPS in Go names; use CamelCase
Line 759: exported method BinaryExpr.Format should have comment or be unexported
Line 771: don't use ALL_CAPS in Go names; use CamelCase
Line 772: don't use ALL_CAPS in Go names; use CamelCase
Line 773: don't use ALL_CAPS in Go names; use CamelCase
Line 776: exported method UnaryExpr.Format should have comment or be unexported
Line 787: exported method FuncExpr.Format should have comment or be unexported
Line 815: exported method FuncExpr.IsAggregate should have comment or be unexported
Line 826: exported method CaseExpr.Format should have comment or be unexported
Line 846: exported method When.Format should have comment or be unexported
Line 853: exported method GroupBy.Format should have comment or be unexported
Line 864: exported method OrderBy.Format should have comment or be unexported
Line 880: don't use ALL_CAPS in Go names; use CamelCase
Line 881: don't use ALL_CAPS in Go names; use CamelCase
Line 884: exported method Order.Format should have comment or be unexported
Line 893: exported method Limit.Format should have comment or be unexported
Line 950: exported method Values.Format should have comment or be unexported
Line 964: exported method ValTuple.IRowTuple should have comment or be unexported
Line 965: exported method Subquery.IRowTuple should have comment or be unexported
Line 970: exported method UpdateExprs.Format should have comment or be unexported
Line 984: exported method UpdateExpr.Format should have comment or be unexported
Line 991: exported method OnDup.Format should have comment or be unexported
/github.com/dinedal/textql/sqlparser/parsed_query.go
Line 20: exported type ParsedQuery should have comment or be unexported
Line 25: exported type EncoderFunc should have comment or be unexported
Line 27: exported method ParsedQuery.GenerateQuery should have comment or be unexported
Line 49: exported method ParsedQuery.MarshalJSON should have comment or be unexported
Line 53: exported function EncodeValue should have comment or be unexported
Line 102: exported type TupleEqualityList should have comment or be unexported
Line 107: exported method TupleEqualityList.Encode should have comment or be unexported
Line 156: exported function FetchBindVar should have comment or be unexported
/github.com/dinedal/textql/sqlparser/sql.go
/github.com/dinedal/textql/sqlparser/token.go
Line 15: exported const EOFCHAR should have comment or be unexported
Line 172: if block ends with a return statement, so drop this else and outdent its block
Line 190: if block ends with a return statement, so drop this else and outdent its block
Line 214: if block ends with a return statement, so drop this else and outdent its block
Line 221: if block ends with a return statement, so drop this else and outdent its block
Line 249: var keywordId should be keywordID
Line 417: exported method Tokenizer.ConsumeNext should have comment or be unexported
/github.com/dinedal/textql/sqlparser/tracked_buffer.go
Line 25: exported function NewTrackedBuffer should have comment or be unexported
Line 101: exported method TrackedBuffer.ParsedQuery should have comment or be unexported
Line 105: exported method TrackedBuffer.HasBindVars should have comment or be unexported
/github.com/dinedal/textql/vault/sqlite.go
Line 20: struct field connId should be connID
Line 24: exported type SQLite3Options should have comment or be unexported
Line 27: should omit type []*sqlite3.SQLiteConn from declaration of var sqlite3conn; it will be inferred from the right-hand side
Line 28: should omit type *regexp.Regexp from declaration of var allWhiteSpace; it will be inferred from the right-hand side
Line 29: should omit type *regexp.Regexp from declaration of var tableNameCheckRegEx; it will be inferred from the right-hand side
Line 42: exported function NewSQLite3Storage should have comment or be unexported
Line 42: exported func NewSQLite3Storage returns unexported type *storage.sqlite3Storage, which can be annoying to use
Line 52: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 69: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 97: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 135: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 160: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 165: can probably use "var vals []interface{}" instead
Line 184: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 199: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
Line 207: var backupConnId should be backupConnID
Line 234: receiver name should be a reflection of its identity; don't use generic names such as "me", "this", or "self"
/github.com/dinedal/textql/vault/sqlite_test.go
Line 188: should omit 2nd value from range; this loop is equivalent to `for i := range ...`
/github.com/dinedal/textql/vault/storage.go
Line 9: exported type Storage should have comment or be unexported
/github.com/dinedal/textql/test_util/test_util.go
Line 1: don't use an underscore in package name
Line 8: exported function OpenFileFromString should have comment or be unexported
/github.com/dinedal/textql/util/file_helpers.go
Line 12: exported function IsPathDir should have comment or be unexported
Line 30: exported function OpenFileOrStdDev should have comment or be unexported
Line 65: exported function CleanPath should have comment or be unexported
Line 94: exported function RewindFile should have comment or be unexported
Line 102: exported function IsThereDataOnStdin should have comment or be unexported
Line 111: if block ends with a return statement, so drop this else and outdent its block
Line 116: exported function AllFilesInDirectory should have comment or be unexported
Line 119: can probably use "var result []string" instead
/github.com/dinedal/textql/util/seperator_helpers.go
Line 10: exported function DetermineSeparator should have comment or be unexported
```

## File: `VERSION`
```
2.0.3
```

## File: `go.mod`
```
module github.com/dinedal/textql

go 1.13

require (
	github.com/mattn/go-runewidth v0.0.2 // indirect
	github.com/mattn/go-sqlite3 v2.0.3+incompatible
	github.com/olekukonko/tablewriter v0.0.0-20180506121414-d4647c9c7a84
)
```

## File: `go.sum`
```
github.com/BurntSushi/toml v0.3.1 h1:WXkYYl6Yr3qBf1K79EBnL4mak0OimBfB0XUf9Vl28OQ=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/BurntSushi/xgb v0.0.0-20160522181843-27f122750802/go.mod h1:IVnqGOEym/WlBOVXweHU+Q+/VP0lqqI8lqeDx9IjBqo=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/edsrzf/mmap-go v0.0.0-20170320065105-0bce6a688712 h1:aaQcKT9WumO6JEJcRyTqFVq4XUZiUcKR2/GI31TOcz8=
github.com/edsrzf/mmap-go v0.0.0-20170320065105-0bce6a688712/go.mod h1:YO35OhQPt3KJa3ryjFM5Bs14WD66h8eGKpfaBNrHW5M=
github.com/google/renameio v0.1.0/go.mod h1:KWCgfxg9yswjAJkECMjeO8J8rahYeXnNhOm40UhjYkI=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/mattn/go-runewidth v0.0.2 h1:UnlwIPBGaTZfPQ6T1IGzPI0EkYAQmT9fAEJ/poFC63o=
github.com/mattn/go-runewidth v0.0.2/go.mod h1:LwmH8dsx7+W8Uxz3IHJYH5QSwggIsqBzpuz5H//U1FU=
github.com/mattn/go-sqlite3 v1.9.0 h1:pDRiWfl+++eC2FEFRy6jXmQlvp4Yh3z1MJKg4UeYM/4=
github.com/mattn/go-sqlite3 v1.9.0/go.mod h1:FPy6KqzDD04eiIsT53CuJW3U88zkxoIYsOqkbpncsNc=
github.com/mattn/go-sqlite3 v2.0.3+incompatible h1:gXHsfypPkaMZrKbD5209QV9jbUTJKjyR5WD3HYQSd+U=
github.com/mattn/go-sqlite3 v2.0.3+incompatible/go.mod h1:FPy6KqzDD04eiIsT53CuJW3U88zkxoIYsOqkbpncsNc=
github.com/olekukonko/tablewriter v0.0.0-20180506121414-d4647c9c7a84 h1:fiKJgB4JDUd43CApkmCeTSQlWjtTtABrU2qsgbuP0BI=
github.com/olekukonko/tablewriter v0.0.0-20180506121414-d4647c9c7a84/go.mod h1:vsDQFd/mU46D+Z4whnwzcISnGGzXWMclvtLoiIKAKIo=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/remyoudompheng/bigfft v0.0.0-20170806203942-52369c62f446 h1:/NRJ5vAYoqz+7sG51ubIDHXeWO8DlTSrToPu6q11ziA=
github.com/remyoudompheng/bigfft v0.0.0-20170806203942-52369c62f446/go.mod h1:uYEyJGbgTkfkS4+E/PavXkNJcbFIpEtjt2B0KDQ5+9M=
github.com/rogpeppe/go-internal v1.3.0/go.mod h1:M8bDsm7K2OlrFYOpmOWEs/qY81heoFRclV5y23lUDJ4=
github.com/sergi/go-diff v1.0.0 h1:Kpca3qRNrduNnOQeazBd0ysaKrUJiIuISHxogkT9RPQ=
github.com/sergi/go-diff v1.0.0/go.mod h1:0CfEIISq7TuYL3j771MWULgwwjU+GofnZX9QAmXWZgo=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
gitlab.com/cznic/ebnf2y v1.0.0/go.mod h1:jx14dqOldV2pRvSi8HASTB/k5fkIv2TwjYAp5py0MTs=
gitlab.com/cznic/golex v1.0.0/go.mod h1:vkWdDgqbbThjRHoOLU7yNPgMxaubAkwnvF/4zeG8cvU=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190510104115-cbcb75029529/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/exp v0.0.0-20190411193353-0480eff6dd7c/go.mod h1:ZjyILWgesfNpC6sMxTJOJm9Kp84zZh5NQWvqDGG3Qr8=
golang.org/x/image v0.0.0-20190227222117-0694c2d4d067/go.mod h1:kZ7UVZpmo3dzQBMxlp+ypCbDeSB+sBbTgSJuh5dn5js=
golang.org/x/mobile v0.0.0-20190312151609-d3739f865fa6/go.mod h1:z+o9i4GpDbdi3rU15maQ/Ox0txvL9dWGYEHz965HBQE=
golang.org/x/mod v0.0.0-20190513183733-4bf6d317e70e/go.mod h1:mXi4GBBbnImb6dmsKGUJ2LatrhH/nqhxcFungHvyanc=
golang.org/x/mod v0.1.1-0.20191105210325-c90efee705ee h1:WG0RUwxtNT4qqaXX3DPA8zHFNm/D9xaBpxzHt1WcA/E=
golang.org/x/mod v0.1.1-0.20191105210325-c90efee705ee/go.mod h1:QqPTAvyqsEbceGzBzNggFXnrqF1CaUcvgkdR5Ot7KZg=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/sync v0.0.0-20190423024810-112230192c58 h1:8gQV6CLnAEikrhgkHFbMAEhagSSnXWGV915qUMm9mrU=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190312061237-fead79001313/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/tools v0.0.0-20190312151545-0bb0c0a6e846/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190621195816-6e04913cbbac/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20200130224948-02f1738cbe39 h1:5ERHXLQfA0b8cHOwaOfWaaGekrA4+Ka/N74zilLnsIk=
golang.org/x/tools v0.0.0-20200130224948-02f1738cbe39/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/tools v0.0.0-20200131211209-ecb101ed6550 h1:3Kc3/T5DQ/majKzDmb+0NzmbXFhKLaeDTp3KqVPV5Eo=
golang.org/x/tools/gopls v0.3.0 h1:l9KKK1/n6CIbfgaUvHBWAvCfOxcl1N+KSOK79OlPIao=
golang.org/x/tools/gopls v0.3.0/go.mod h1:vvBkm7WBjHNudDeK7Sg7HeR+sKt6yp5TD/4NQaTZzRs=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898 h1:/atklqdjdhuosWIl6AIbOeHJjicWYPqR9bpxqxYG2pA=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/errgo.v2 v2.1.0/go.mod h1:hNsd1EY+bozCKY1Ytp96fpM3vjJbqLJn88ws8XvfDNI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
honnef.co/go/tools v0.0.1-2019.2.3 h1:3JgtbtFHMiCmsznwGVTUWbgGov+pVqnlf1dEJTNAXeM=
honnef.co/go/tools v0.0.1-2019.2.3/go.mod h1:a3bituU0lyd329TUQxRnasdCoJDkEUEAqEt0JzvZhAg=
modernc.org/b v1.0.0 h1:vpvqeyp17ddcQWF29Czawql4lDdABCDRbXRAS4+aF2o=
modernc.org/b v1.0.0/go.mod h1:uZWcZfRj1BpYzfN9JTerzlNUnnPsV9O2ZA8JsRcubNg=
modernc.org/db v1.0.0 h1:2c6NdCfaLnshSvY7OU09cyAY0gYXUZj4lmg5ItHyucg=
modernc.org/db v1.0.0/go.mod h1:kYD/cO29L/29RM0hXYl4i3+Q5VojL31kTUVpVJDw0s8=
modernc.org/ebnfutil v1.0.0/go.mod h1:+2n/OnQXoild9pzrPa/2wmVtR+ufWjB/0fYkc0BV9sc=
modernc.org/file v1.0.0 h1:9/PdvjVxd5+LcWUQIfapAWRGOkDLK90rloa8s/au06A=
modernc.org/file v1.0.0/go.mod h1:uqEokAEn1u6e+J45e54dsEA/pw4o7zLrA2GwyntZzjw=
modernc.org/fileutil v1.0.0 h1:Z1AFLZwl6BO8A5NldQg/xTSjGLetp+1Ubvl4alfGx8w=
modernc.org/fileutil v1.0.0/go.mod h1:JHsWpkrk/CnVV1H/eGlFf85BEpfkrp56ro8nojIq9Q8=
modernc.org/golex v1.0.0 h1:wWpDlbK8ejRfSyi0frMyhilD3JBvtcx2AdGDnU+JtsE=
modernc.org/golex v1.0.0/go.mod h1:b/QX9oBD/LhixY6NDh+IdGv17hgB+51fET1i2kPSmvk=
modernc.org/internal v1.0.0 h1:XMDsFDcBDsibbBnHB2xzljZ+B1yrOVLEFkKL2u15Glw=
modernc.org/internal v1.0.0/go.mod h1:VUD/+JAkhCpvkUitlEOnhpVxCgsBI90oTzSCRcqQVSM=
modernc.org/lex v1.0.0/go.mod h1:G6rxMTy3cH2iA0iXL/HRRv4Znu8MK4higxph/lE7ypk=
modernc.org/lexer v1.0.0/go.mod h1:F/Dld0YKYdZCLQ7bD0USbWL4YKCyTDRDHiDTOs0q0vk=
modernc.org/lldb v1.0.0 h1:6vjDJxQEfhlOLwl4bhpwIz00uyFK4EmSYcbwqwbynsc=
modernc.org/lldb v1.0.0/go.mod h1:jcRvJGWfCGodDZz8BPwiKMJxGJngQ/5DrRapkQnLob8=
modernc.org/mathutil v1.0.0 h1:93vKjrJopTPrtTNpZ8XIovER7iCIH1QU7wNbOQXC60I=
modernc.org/mathutil v1.0.0/go.mod h1:wU0vUrJsVWBZ4P6e7xtFJEhFSNsfRLJ8H458uRjg03k=
modernc.org/ql v1.0.1 h1:pwGOhUbl75KRiGEUUotORpnBlI0whDEb/koIqZOGI7k=
modernc.org/ql v1.0.1/go.mod h1:Fj1ylcVyzcu/fgWZTrvBO9j/aEUg/ixLFnGtmzh7quI=
modernc.org/sortutil v1.0.0 h1:SUTM1sCR0Ldpv7dbB/KCPC2zHHsZ1KrSkhmGmmV22CQ=
modernc.org/sortutil v1.0.0/go.mod h1:1QO0q8IlIlmjBIwm6t/7sof874+xCfZouyqZMLIAtxM=
modernc.org/strutil v1.0.0 h1:XVFtQwFVwc02Wk+0L/Z/zDDXO81r5Lhe6iMKmGX3KhE=
modernc.org/strutil v1.0.0/go.mod h1:lstksw84oURvj9y3tn8lGvRxyRC1S2+g5uuIzNfIOBs=
modernc.org/zappy v1.0.0 h1:dPVaP+3ueIUv4guk8PuZ2wiUGcJ1WUVvIheeSSTD0yk=
modernc.org/zappy v1.0.0/go.mod h1:hHe+oGahLVII/aTTyWK/b53VDHMAGCBYYeZ9sn83HC4=
mvdan.cc/xurls/v2 v2.1.0 h1:KaMb5GLhlcSX+e+qhbRJODnUUBvlw01jt4yrjFIHAuA=
mvdan.cc/xurls/v2 v2.1.0/go.mod h1:5GrSd9rOnKOpZaji1OZLYL/yeAAtGDlo/cFe+8K5n8E=
```

## File: `snapcraft.yaml`
```yaml
name: textql
version: '1.0'
summary: Execute SQL against structured text like CSV or TSV 
description: |
  Execute SQL against structured text like CSV or TSV.
grade: stable
confinement: strict
base: core18
parts:
  textql:
    plugin: go
    source: https://github.com/dinedal/textql.git
    go-importpath: github.com/dinedal/textql
    build-packages:
      - build-essential
apps:
  textql:
    command: bin/textql
    plugs:
      - home
```

## File: `inputs/csv.go`
```go
package inputs

import (
	"encoding/csv"
	"io"
	"log"
	"os"
	"path/filepath"
	"strconv"
)

// CSVInput represents a record producing input from a CSV formatted file or pipe.
type CSVInput struct {
	options         *CSVInputOptions
	reader          *csv.Reader
	firstRow        []string
	header          []string
	minOutputLength int
	name            string
}

// CSVInputOptions options are passed to the underlying encoding/csv reader.
type CSVInputOptions struct {
	// HasHeader when true, will treat the first row as a header row.
	HasHeader bool
	// Separator is the rune that fields are delimited by.
	Separator rune
	// ReadFrom is where the data will be read from.
	ReadFrom io.Reader
}

// NewCSVInput sets up a new CSVInput, the first row is read when this is run.
// If there is a problem with reading the first row, the error is returned.
// Otherwise, the returned csvInput can be reliably consumed with ReadRecord()
// until ReadRecord() returns nil.
func NewCSVInput(opts *CSVInputOptions) (*CSVInput, error) {
	csvInput := &CSVInput{
		options: opts,
		reader:  csv.NewReader(opts.ReadFrom),
	}
	csvInput.firstRow = nil

	csvInput.reader.FieldsPerRecord = -1
	csvInput.reader.Comma = csvInput.options.Separator
	csvInput.reader.LazyQuotes = true

	headerErr := csvInput.readHeader()

	if headerErr != nil {
		return nil, headerErr
	}

	if asFile, ok := csvInput.options.ReadFrom.(*os.File); ok {
		csvInput.name = filepath.Base(asFile.Name())
	} else {
		csvInput.name = "pipe"
	}

	return csvInput, nil
}

// Name returns the name of the CSV being read.
// By default, either the base filename or 'pipe' if it is a unix pipe
func (csvInput *CSVInput) Name() string {
	return csvInput.name
}

// SetName overrides the name of the CSV
func (csvInput *CSVInput) SetName(name string) {
	csvInput.name = name
}

// ReadRecord reads a single record from the CSV. Always returns successfully.
// If the record is empty, an empty []string is returned.
// Record expand to match the current row size, adding blank fields as needed.
// Records never return less then the number of fields in the first row.
// Returns nil on EOF
// In the event of a parse error due to an invalid record, it is logged, and
// an empty []string is returned with the number of fields in the first row,
// as if the record were empty.
//
// In general, this is a very tolerant of problems CSV reader.
func (csvInput *CSVInput) ReadRecord() []string {
	var row []string
	var fileErr error

	if csvInput.firstRow != nil {
		row = csvInput.firstRow
		csvInput.firstRow = nil
		return row
	}

	row, fileErr = csvInput.reader.Read()
	emptysToAppend := csvInput.minOutputLength - len(row)
	if fileErr == io.EOF {
		return nil
	} else if parseErr, ok := fileErr.(*csv.ParseError); ok {
		log.Println(parseErr)
		emptysToAppend = csvInput.minOutputLength
	}

	if emptysToAppend > 0 {
		for counter := 0; counter < emptysToAppend; counter++ {
			row = append(row, "")
		}
	}

	return row
}

func (csvInput *CSVInput) readHeader() error {
	var readErr error

	csvInput.firstRow, readErr = csvInput.reader.Read()

	if readErr != nil {
		log.Fatalln(readErr)
		return readErr
	}

	csvInput.minOutputLength = len(csvInput.firstRow)

	if csvInput.options.HasHeader {
		csvInput.header = csvInput.firstRow
		csvInput.firstRow = nil
	} else {
		csvInput.header = make([]string, csvInput.minOutputLength)
		for i := 0; i < len(csvInput.firstRow); i++ {
			csvInput.header[i] = "c" + strconv.Itoa(i)
		}
	}

	return nil
}

// Header returns the header of the csvInput. Either the first row if a header
// set in the options, or c#, where # is the column number, starting with 0.
func (csvInput *CSVInput) Header() []string {
	return csvInput.header
}
```

## File: `inputs/csv_test.go`
```go
package inputs

import (
	"os"
	"strings"

	"reflect"
	"testing"

	"github.com/dinedal/textql/test_util"
)

var (
	simple = `a,b,c
1,2,3
4,5,6`

	bad = `a,b,c
1,2,
4,5,6
7,8


9,,10
11,12,13,14
"foo,bar","boo,\"far",","
'foo,bar','"','"'
"test
",multi-line
`
)

func TestCSVInputFakesHeader(t *testing.T) {
	fp := test_util.OpenFileFromString(simple)
	defer fp.Close()
	defer os.Remove(fp.Name())

	opts := &CSVInputOptions{
		HasHeader: false,
		Separator: ',',
		ReadFrom:  fp,
	}

	input, _ := NewCSVInput(opts)
	expected := []string{"c0", "c1", "c2"}

	if !reflect.DeepEqual(input.Header(), expected) {
		t.Errorf("Header() = %v, want %v", input.Header(), expected)
	}
}

func TestCSVInputReadsHeader(t *testing.T) {
	fp := test_util.OpenFileFromString(simple)
	defer fp.Close()
	defer os.Remove(fp.Name())

	opts := &CSVInputOptions{
		HasHeader: true,
		Separator: ',',
		ReadFrom:  fp,
	}

	input, _ := NewCSVInput(opts)
	expected := []string{"a", "b", "c"}

	if !reflect.DeepEqual(input.Header(), expected) {
		t.Errorf("Header() = %v, want %v", input.Header(), expected)
	}
}

func TestCSVInputReadsSimple(t *testing.T) {
	fp := test_util.OpenFileFromString(simple)
	defer fp.Close()
	defer os.Remove(fp.Name())

	opts := &CSVInputOptions{
		HasHeader: true,
		Separator: ',',
		ReadFrom:  fp,
	}

	input, _ := NewCSVInput(opts)
	expected := make([][]string, len(strings.Split(simple, "\n"))-1)
	expected[0] = []string{"1", "2", "3"}
	expected[1] = []string{"4", "5", "6"}

	for counter := 0; counter < len(expected); counter++ {
		row := input.ReadRecord()
		if !reflect.DeepEqual(row, expected[counter]) {
			t.Errorf("ReadRecord() = %v, want %v", row, expected[counter])
		}
	}
}

func TestCSVInputReadsBad(t *testing.T) {
	fp := test_util.OpenFileFromString(bad)
	defer fp.Close()
	defer os.Remove(fp.Name())

	opts := &CSVInputOptions{
		HasHeader: true,
		Separator: ',',
		ReadFrom:  fp,
	}

	input, _ := NewCSVInput(opts)
	expected := make([][]string, len(strings.Split(bad, "\n"))-1)
	expected[0] = []string{"1", "2", ""}
	expected[1] = []string{"4", "5", "6"}
	expected[2] = []string{"7", "8", ""}
	expected[3] = []string{"9", "", "10"}
	expected[4] = []string{"11", "12", "13", "14"}
	expected[5] = []string{"foo,bar", `boo,\"far`, ","}
	expected[6] = []string{`'foo`, `bar'`, `'"'`, `'"'`}
	expected[7] = []string{"test\n", "multi-line", ""}

	for counter := 0; counter < len(expected); counter++ {
		row := input.ReadRecord()
		if !reflect.DeepEqual(row, expected[counter]) {
			t.Errorf("ReadRecord() = %v, want %v", row, expected[counter])
		}
	}
}

func TestCSVInputHasAName(t *testing.T) {
	fp := test_util.OpenFileFromString(simple)
	defer fp.Close()
	defer os.Remove(fp.Name())

	opts := &CSVInputOptions{
		HasHeader: true,
		Separator: ',',
		ReadFrom:  fp,
	}

	input, _ := NewCSVInput(opts)
	expected := fp.Name()

	if !reflect.DeepEqual(input.Name(), expected) {
		t.Errorf("Name() = %v, want %v", input.Name(), expected)
	}
}
```

## File: `inputs/input.go`
```go
package inputs

// Input is how TextQL reads from data sources.
// To be an input, an implementor must return tabular data.
// How data is manipulated into the tabular structure is left to the implementor.
// Inputs are expected to return in a row by row fashion.
type Input interface {
	// ReadRecord should return nil on the end of data, or a single record.
	// Recoverable errors should represent themselves as empty sets.
	// Unrecoverable errors should return nil.
	ReadRecord() []string
	// Header should return metadata naming the columns in the table.
	Header() []string
	// Name should return a reasonable name for the data set, prehaps the file name.
	Name() string
	// SetName allows users of the dataset to supply their own name if needed.
	SetName(string)
}
```

## File: `man/textql.1`
```
.\" generated with Ronn/v0.7.3
.\" http://github.com/rtomayko/ronn/tree/0.7.3
.
.TH "TEXTQL" "1" "December 2015" "" ""
.
.SH "NAME"
\fBtextql\fR \- execute queries on structured text
.
.SH "SYNOPSIS"
\fBtextql\fR [\fI\-save\-to path\fR] [\fI\-output\-file path\fR] [\fI\-output\-dlm delimter\fR] [\fI\-output\-header\fR] [\fI\-header\fR] [\fI\-dlm delimter\fR] [\fI\-source path\fR] [\fI\-sql sql_statements\fR] [\fI\-quiet\fR] [\fIpath\fR\.\.\.]
.
.br
\fBtextql\fR \fI\-console\fR \fIpath\fR\.\.\.
.
.br
.
.SH "DESCRIPTION"
\fBtextql\fR executes given statements in SQL on structured texts and returns the result\. SQL statements accepted by \fBtextql\fR are ANSI SQL compatible, and are executed against the data in the order provided\. No transformations are applied to the text files but are instead applied to a temporary view of the data\. Statements that insert data or modify the existing data will only have their effects visible in the output\.
.
.P
The argument list of the end is expected to be a list of paths which may or may not be specific files\. Each path is traversed for files that are then loaded as part of the database that \fBtextql\fR creates internally, and files are loaded without traversal\. Paths provided are not recursed\.
.
.P
Each statement is then executed against \fBtextql\fR\'s internal database and the result, if any, is printed\. \fBINSERT\fR, \fBUPDATE\fR, \fBDELETE\fR or other side effecting statements do not effect the text files given as input, but instead modify the database internal to \fBtextql\fR\. Their result may be viewed via the output, presisting the database as is with \fB\-save\-to\fR or in a SQLite REPL with \fB\-\-console\fR
.
.P
With no arguements, \fBtextql\fR will print a brief overview of it\'s usage\.
.
.SH "FILES"
Structured text accepted by textql is any text file in a tabular format where each row of the table is on a single line, and each column is a section of the line delimited by a single character which is consistent throughout the file\. A common structured text format is CSV (RFC4180)\.
.
.SH "OPTIONS"
.
.TP
\fB\-console\fR
After all statements are run, open SQLite3 REPL with this data
.
.TP
\fB\-dlm string\fR
Input delimiter character between fields \-dlm=tab for tab, \-dlm=0x## to specify a character code in hex (default ",")
.
.TP
\fB\-header\fR
Treat input files as having the first row as a header row
.
.TP
\fB\-output\-dlm string\fR
Output delimiter character between fields \-output\-dlm=tab for tab, \-dlm=0x## to specify a character code in hex (default ",")
.
.TP
\fB\-output\-file file\fR
Filename to write output to, if empty no output is written (default "stdout")
.
.TP
\fB\-output\-header\fR
Display column names in output
.
.TP
\fB\-quiet\fR
Surpress logging
.
.TP
\fB\-pretty\fR
Pretty print output
.
.TP
\fB\-save\-to file\fR
SQLite3 db is left on disk at this file
.
.TP
\fB\-sql string\fR
SQL Statement(s) to run on the data
.
.TP
\fB\-version\fR
Print version and exit
.
.SH "COPYRIGHT"
textql is Copyright (C) 2015, 2016 Paul Bergeron \fIhttp://pauldbergeron\.com/\fR
```

## File: `man/textql.1.html`
```html
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv='content-type' value='text/html;charset=utf8'>
  <meta name='generator' value='Ronn/v0.7.3 (http://github.com/rtomayko/ronn/tree/0.7.3)'>
  <title>textql(1) - execute queries on structured text</title>
  <style type='text/css' media='all'>
  /* style: man */
  body#manpage {margin:0}
  .mp {max-width:100ex;padding:0 9ex 1ex 4ex}
  .mp p,.mp pre,.mp ul,.mp ol,.mp dl {margin:0 0 20px 0}
  .mp h2 {margin:10px 0 0 0}
  .mp > p,.mp > pre,.mp > ul,.mp > ol,.mp > dl {margin-left:8ex}
  .mp h3 {margin:0 0 0 4ex}
  .mp dt {margin:0;clear:left}
  .mp dt.flush {float:left;width:8ex}
  .mp dd {margin:0 0 0 9ex}
  .mp h1,.mp h2,.mp h3,.mp h4 {clear:left}
  .mp pre {margin-bottom:20px}
  .mp pre+h2,.mp pre+h3 {margin-top:22px}
  .mp h2+pre,.mp h3+pre {margin-top:5px}
  .mp img {display:block;margin:auto}
  .mp h1.man-title {display:none}
  .mp,.mp code,.mp pre,.mp tt,.mp kbd,.mp samp,.mp h3,.mp h4 {font-family:monospace;font-size:14px;line-height:1.42857142857143}
  .mp h2 {font-size:16px;line-height:1.25}
  .mp h1 {font-size:20px;line-height:2}
  .mp {text-align:justify;background:#fff}
  .mp,.mp code,.mp pre,.mp pre code,.mp tt,.mp kbd,.mp samp {color:#131211}
  .mp h1,.mp h2,.mp h3,.mp h4 {color:#030201}
  .mp u {text-decoration:underline}
  .mp code,.mp strong,.mp b {font-weight:bold;color:#131211}
  .mp em,.mp var {font-style:italic;color:#232221;text-decoration:none}
  .mp a,.mp a:link,.mp a:hover,.mp a code,.mp a pre,.mp a tt,.mp a kbd,.mp a samp {color:#0000ff}
  .mp b.man-ref {font-weight:normal;color:#434241}
  .mp pre {padding:0 4ex}
  .mp pre code {font-weight:normal;color:#434241}
  .mp h2+pre,h3+pre {padding-left:0}
  ol.man-decor,ol.man-decor li {margin:3px 0 10px 0;padding:0;float:left;width:33%;list-style-type:none;text-transform:uppercase;color:#999;letter-spacing:1px}
  ol.man-decor {width:100%}
  ol.man-decor li.tl {text-align:left}
  ol.man-decor li.tc {text-align:center;letter-spacing:4px}
  ol.man-decor li.tr {text-align:right;float:right}
  </style>
</head>
<!--
  The following styles are deprecated and will be removed at some point:
  div#man, div#man ol.man, div#man ol.head, div#man ol.man.

  The .man-page, .man-decor, .man-head, .man-foot, .man-title, and
  .man-navigation should be used instead.
-->
<body id='manpage'>
  <div class='mp' id='man'>

  <div class='man-navigation' style='display:none'>
    <a href="#NAME">NAME</a>
    <a href="#SYNOPSIS">SYNOPSIS</a>
    <a href="#DESCRIPTION">DESCRIPTION</a>
    <a href="#FILES">FILES</a>
    <a href="#OPTIONS">OPTIONS</a>
    <a href="#COPYRIGHT">COPYRIGHT</a>
  </div>

  <ol class='man-decor man-head man head'>
    <li class='tl'>textql(1)</li>
    <li class='tc'></li>
    <li class='tr'>textql(1)</li>
  </ol>

  <h2 id="NAME">NAME</h2>
<p class="man-name">
  <code>textql</code> - <span class="man-whatis">execute queries on structured text</span>
</p>

<h2 id="SYNOPSIS">SYNOPSIS</h2>

<p><code>textql</code> [<var>-save-to path</var>] [<var>-output-file path</var>] [<var>-output-dlm delimter</var>] [<var>-output-header</var>] [<var>-header</var>] [<var>-dlm delimter</var>] [<var>-source path</var>] [<var>-sql sql_statements</var>] [<var>-quiet</var>] [<var>path</var>...]<br />
<code>textql</code> <var>-console</var> <var>path</var>...<br /></p>

<h2 id="DESCRIPTION">DESCRIPTION</h2>

<p><strong>textql</strong> executes given statements in SQL on structured texts and returns the result.
SQL statements accepted by <code>textql</code> are ANSI SQL compatible, and are executed against
the data in the order provided. No transformations are applied to the text files
but are instead applied to a temporary view of the data. Statements that insert data
or modify the existing data will only have their effects visible in the output.</p>

<p>The argument list of the end is expected to be a list of paths which may or may not
be specific files. Each path is traversed for files that are then loaded as part of
the database that <code>textql</code> creates internally, and files are loaded without traversal.
Paths provided are not recursed.</p>

<p>Each statement is then executed against <code>textql</code>'s internal database and the result, if
any, is printed. <strong>INSERT</strong>, <strong>UPDATE</strong>, <strong>DELETE</strong> or other side effecting statements
do not effect the text files given as input, but instead modify the database
internal to <code>textql</code>. Their result may be viewed via the output, presisting the
database as is with <code>-save-to</code> or in a SQLite REPL with <code>--console</code></p>

<p>With no arguements, <code>textql</code> will print a brief overview of it's usage.</p>

<h2 id="FILES">FILES</h2>

<p>Structured text accepted by textql is any text file in a tabular format
where each row of the table is on a single line, and each column is a section of the
line delimited by a single character which is consistent throughout the file. A
common structured text format is CSV (RFC4180).</p>

<h2 id="OPTIONS">OPTIONS</h2>

<dl>
<dt><code>-console</code></dt><dd>After all statements are run, open SQLite3 REPL with this data</dd>
<dt><code>-dlm string</code></dt><dd>Input delimiter character between fields -dlm=tab for tab, -dlm=0x## to specify a character code in hex (default ",")</dd>
<dt class="flush"><code>-header</code></dt><dd>Treat input files as having the first row as a header row</dd>
<dt><code>-output-dlm string</code></dt><dd>Output delimiter character between fields -output-dlm=tab for tab, -dlm=0x## to specify a character code in hex (default ",")</dd>
<dt><code>-output-file file</code></dt><dd>Filename to write output to, if empty no output is written (default "stdout")</dd>
<dt><code>-output-header</code></dt><dd>Display column names in output</dd>
<dt class="flush"><code>-quiet</code></dt><dd>Surpress logging</dd>
<dt class="flush"><code>-pretty</code></dt><dd>Pretty print output</dd>
<dt><code>-save-to file</code></dt><dd>SQLite3 db is left on disk at this file</dd>
<dt><code>-sql string</code></dt><dd>SQL Statement(s) to run on the data</dd>
<dt><code>-version</code></dt><dd>Print version and exit</dd>
</dl>


<h2 id="COPYRIGHT">COPYRIGHT</h2>

<p>textql is Copyright (C) 2015, 2016 Paul Bergeron
<a href="http://pauldbergeron.com/" data-bare-link="true">http://pauldbergeron.com/</a></p>


  <ol class='man-decor man-foot man foot'>
    <li class='tl'></li>
    <li class='tc'>December 2015</li>
    <li class='tr'>textql(1)</li>
  </ol>

  </div>
</body>
</html>
```

## File: `man/textql.1.ronn`
```
textql(1) -- execute queries on structured text
===============================================

## SYNOPSIS

`textql` [<-save-to path>] [<-output-file path>] [<-output-dlm delimter>] [<-output-header>] [<-header>] [<-dlm delimter>] [<-source path>] [<-sql sql_statements>] [<-quiet>] [<path>...]<br>
`textql` <-console> <path>...<br>

## DESCRIPTION

**textql** executes given statements in SQL on structured texts and returns the result.
SQL statements accepted by `textql` are ANSI SQL compatible, and are executed against
the data in the order provided. No transformations are applied to the text files
but are instead applied to a temporary view of the data. Statements that insert data
or modify the existing data will only have their effects visible in the output.

The argument list of the end is expected to be a list of paths which may or may not
be specific files. Each path is traversed for files that are then loaded as part of
the database that `textql` creates internally, and files are loaded without traversal.
Paths provided are not recursed.

Each statement is then executed against `textql`'s internal database and the result, if
any, is printed. **INSERT**, **UPDATE**, **DELETE** or other side effecting statements
do not effect the text files given as input, but instead modify the database
internal to `textql`. Their result may be viewed via the output, presisting the
database as is with `-save-to` or in a SQLite REPL with `--console`

With no arguements, `textql` will print a brief overview of it's usage.

## FILES

Structured text accepted by textql is any text file in a tabular format
where each row of the table is on a single line, and each column is a section of the
line delimited by a single character which is consistent throughout the file. A
common structured text format is CSV (RFC4180).

## OPTIONS

  * `-console`:
    After all statements are run, open SQLite3 REPL with this data
  * `-dlm string`:
    Input delimiter character between fields -dlm=tab for tab, -dlm=0x## to specify a character code in hex (default ",")
  * `-header`:
    Treat input files as having the first row as a header row
  * `-output-dlm string`:
    Output delimiter character between fields -output-dlm=tab for tab, -dlm=0x## to specify a character code in hex (default ",")
  * `-output-file file`:
    Filename to write output to, if empty no output is written (default "stdout")
  * `-output-header`:
    Display column names in output
  * `-quiet`:
    Surpress logging
  * `-pretty`:
    Pretty print output
  * `-save-to file`:
    SQLite3 db is left on disk at this file
  * `-sql string`:
    SQL Statement(s) to run on the data
  * `-version`:
    Print version and exit


## COPYRIGHT

textql is Copyright (C) 2015, 2016 Paul Bergeron
<http://pauldbergeron.com/>
```

## File: `outputs/csv.go`
```go
package outputs

import (
	"database/sql"
	"encoding/csv"
	"io"
	"log"
)

// CSVOutput represents a TextQL output that transforms sql.Rows into CSV formatted
// string data using encoding/csv
type CSVOutput struct {
	options         *CSVOutputOptions
	writer          *csv.Writer
	firstRow        []string
	header          []string
	minOutputLength int
}

// CSVOutputOptions define options that are passed to encoding/csv for formatting
// the output in specific ways.
type CSVOutputOptions struct {
	// WriteHeader determines if a header row based on the column names should be written.
	WriteHeader bool
	// Separator is the rune used to delimit fields.
	Separator rune
	// WriteTo is where the formatted data will be written to.
	WriteTo io.Writer
}

// NewCSVOutput returns a new CSVOutput configured per the options provided.
func NewCSVOutput(opts *CSVOutputOptions) *CSVOutput {
	csvOutput := &CSVOutput{
		options: opts,
		writer:  csv.NewWriter(opts.WriteTo),
	}

	csvOutput.writer.Comma = csvOutput.options.Separator

	return csvOutput
}

// Show writes the sql.Rows given to the destination in CSV format.
func (csvOutput *CSVOutput) Show(rows *sql.Rows) {
	cols, colsErr := rows.Columns()

	if colsErr != nil {
		log.Fatalln(colsErr)
	}

	if csvOutput.options.WriteHeader && len(cols) > 0 {
		if err := csvOutput.writer.Write(cols); err != nil {
			log.Fatalln(err)
		}
	}

	rawResult := make([][]byte, len(cols))
	result := make([]string, len(cols))

	dest := make([]interface{}, len(cols))

	for i := range cols {
		dest[i] = &rawResult[i]
	}

	for rows.Next() {
		rows.Scan(dest...)

		for i, raw := range rawResult {
			result[i] = string(raw)
		}

		writeErr := csvOutput.writer.Write(result)

		if writeErr != nil {
			log.Fatalln(writeErr)
		}
	}

	csvOutput.writer.Flush()
	rows.Close()
}
```

## File: `outputs/output.go`
```go
package outputs

import "database/sql"

// Output implementors should accept sql.Rows and transform them
// however they need to in order to represent them in their specific format.
type Output interface {
	// Show should display/write the sql.Rows to the implmentor's destination and format.
	Show(*sql.Rows)
}
```

## File: `outputs/pretty_csv.go`
```go
package outputs

import (
	"database/sql"
	"io"
	"log"

	"github.com/olekukonko/tablewriter"
)

// PrettyCSVOutput represents a TextQL output that transforms sql.Rows into pretty tables
type PrettyCSVOutput struct {
	options         *PrettyCSVOutputOptions
	writer          *tablewriter.Table
	firstRow        []string
	header          []string
	minOutputLength int
}

// PrettyCSVOutputOptions define options that are passed to tablewriter for formatting
// the output in specific ways.
type PrettyCSVOutputOptions struct {
	// WriteHeader determines if a header row based on the column names should be written.
	WriteHeader bool
	// WriteTo is where the formatted data will be written to.
	WriteTo io.Writer
}

// NewPrettyCSVOutput returns a new PrettyCSVOutput configured per the options provided.
func NewPrettyCSVOutput(opts *PrettyCSVOutputOptions) *PrettyCSVOutput {
	prettyCsvOutput := &PrettyCSVOutput{
		options: opts,
		writer:  tablewriter.NewWriter(opts.WriteTo),
	}

	return prettyCsvOutput
}

// Show writes the sql.Rows given to the destination in tablewriter basic format.
func (prettyCsvOutput *PrettyCSVOutput) Show(rows *sql.Rows) {
	cols, colsErr := rows.Columns()

	if colsErr != nil {
		log.Fatalln(colsErr)
	}

	if prettyCsvOutput.options.WriteHeader {
		prettyCsvOutput.writer.SetHeader(cols)
		prettyCsvOutput.writer.SetHeaderLine(true)
		prettyCsvOutput.writer.SetAutoFormatHeaders(false)
	}

	rawResult := make([][]byte, len(cols))
	result := make([]string, len(cols))

	dest := make([]interface{}, len(cols))

	for i := range cols {
		dest[i] = &rawResult[i]
	}

	for rows.Next() {
		rows.Scan(dest...)

		for i, raw := range rawResult {
			result[i] = string(raw)
		}

		prettyCsvOutput.writer.Append(result)
	}

	if len(cols) > 0 {
		prettyCsvOutput.writer.Render()
	}
	rows.Close()
}
```

## File: `sqlparser/Makefile`
```

MAKEFLAGS = -s

sql.go: sql.y
	go tool yacc -o sql.go sql.y
	gofmt -w sql.go

clean:
	rm -f y.output sql.go
```

## File: `sqlparser/analyzer.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package sqlparser

// analyzer.go contains utility analysis functions.

import (
	"fmt"

	"github.com/dinedal/textql/sqlparser/sqltypes"
)

// GetTableName returns the table name from the SimpleTableExpr
// only if it's a simple expression. Otherwise, it returns "".
func GetTableName(node SimpleTableExpr) string {
	if n, ok := node.(*TableName); ok && n.Qualifier == nil {
		return string(n.Name)
	}
	// sub-select or '.' expression
	return ""
}

// GetColName returns the column name, only if
// it's a simple expression. Otherwise, it returns "".
func GetColName(node Expr) string {
	if n, ok := node.(*ColName); ok {
		return string(n.Name)
	}
	return ""
}

// IsColName returns true if the ValExpr is a *ColName.
func IsColName(node ValExpr) bool {
	_, ok := node.(*ColName)
	return ok
}

// IsValue returns true if the ValExpr is a string, number or value arg.
// NULL is not considered to be a value.
func IsValue(node ValExpr) bool {
	switch node.(type) {
	case StrVal, NumVal, ValArg:
		return true
	}
	return false
}

// HasINCaluse returns true if any of the conditions has an IN clause.
func HasINClause(conditions []BoolExpr) bool {
	for _, node := range conditions {
		if c, ok := node.(*ComparisonExpr); ok && c.Operator == AST_IN {
			return true
		}
	}
	return false
}

// IsSimpleTuple returns true if the ValExpr is a ValTuple that
// contains simple values or if it's a list arg.
func IsSimpleTuple(node ValExpr) bool {
	switch vals := node.(type) {
	case ValTuple:
		for _, n := range vals {
			if !IsValue(n) {
				return false
			}
		}
		return true
	case ListArg:
		return true
	}
	// It's a subquery
	return false
}

// AsInterface converts the ValExpr to an interface. It converts
// ValTuple to []interface{}, ValArg to string, StrVal to sqltypes.String,
// NumVal to sqltypes.Numeric, NullVal to nil.
// Otherwise, it returns an error.
func AsInterface(node ValExpr) (interface{}, error) {
	switch node := node.(type) {
	case ValTuple:
		vals := make([]interface{}, 0, len(node))
		for _, val := range node {
			v, err := AsInterface(val)
			if err != nil {
				return nil, err
			}
			vals = append(vals, v)
		}
		return vals, nil
	case ValArg:
		return string(node), nil
	case ListArg:
		return string(node), nil
	case StrVal:
		return sqltypes.MakeString(node), nil
	case NumVal:
		n, err := sqltypes.BuildNumeric(string(node))
		if err != nil {
			return nil, fmt.Errorf("type mismatch: %s", err)
		}
		return n, nil
	case *NullVal:
		return nil, nil
	}
	return nil, fmt.Errorf("unexpected node %v", node)
}

// StringIn is a convenience function that returns
// true if str matches any of the values.
func StringIn(str string, values ...string) bool {
	for _, val := range values {
		if str == val {
			return true
		}
	}
	return false
}
```

## File: `sqlparser/ast.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package sqlparser

import (
	"errors"
	"fmt"
	"strconv"

	"github.com/dinedal/textql/sqlparser/sqltypes"
)

// Instructions for creating new types: If a type
// needs to satisfy an interface, declare that function
// along with that interface. This will help users
// identify the list of types to which they can assert
// those interfaces.
// If the member of a type has a string with a predefined
// list of values, declare those values as const following
// the type.
// For interfaces that define dummy functions to consolidate
// a set of types, define the function as ITypeName.
// This will help avoid name collisions.

// Parse parses the sql and returns a Statement, which
// is the AST representation of the query.
func Parse(sql string) (Statement, error) {
	tokenizer := NewStringTokenizer(sql)
	if yyParse(tokenizer) != 0 {
		return nil, errors.New(tokenizer.LastError)
	}
	return tokenizer.ParseTree, nil
}

// SQLNode defines the interface for all nodes
// generated by the parser.
type SQLNode interface {
	Format(buf *TrackedBuffer)
}

// String returns a string representation of an SQLNode.
func String(node SQLNode) string {
	buf := NewTrackedBuffer(nil)
	buf.Myprintf("%v", node)
	return buf.String()
}

// Statement represents a statement.
type Statement interface {
	IStatement()
	SQLNode
}

func (*Union) IStatement()  {}
func (*Select) IStatement() {}
func (*Insert) IStatement() {}
func (*Update) IStatement() {}
func (*Delete) IStatement() {}
func (*Set) IStatement()    {}
func (*DDL) IStatement()    {}
func (*Other) IStatement()  {}

// SelectStatement any SELECT statement.
type SelectStatement interface {
	ISelectStatement()
	IStatement()
	IInsertRows()
	SQLNode
}

func (*Select) ISelectStatement() {}
func (*Union) ISelectStatement()  {}

// Select represents a SELECT statement.
type Select struct {
	Comments    Comments
	Distinct    string
	SelectExprs SelectExprs
	From        *From
	Where       *Where
	GroupBy     GroupBy
	Having      *Where
	OrderBy     OrderBy
	Limit       *Limit
	Lock        string
}

// Select.Distinct
const (
	AST_DISTINCT = "distinct "
)

// Select.Lock
const (
	AST_FOR_UPDATE = " for update"
	AST_SHARE_MODE = " lock in share mode"
)

func (node *Select) Format(buf *TrackedBuffer) {
	buf.Myprintf("select %v%s%v from %v%v%v%v%v%v%s",
		node.Comments, node.Distinct, node.SelectExprs,
		node.From, node.Where,
		node.GroupBy, node.Having, node.OrderBy,
		node.Limit, node.Lock)
}

// Union represents a UNION statement.
type Union struct {
	Type        string
	Left, Right SelectStatement
}

// Union.Type
const (
	AST_UNION     = "union"
	AST_UNION_ALL = "union all"
	AST_SET_MINUS = "minus"
	AST_EXCEPT    = "except"
	AST_INTERSECT = "intersect"
)

func (node *Union) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v %s %v", node.Left, node.Type, node.Right)
}

// Insert represents an INSERT statement.
type Insert struct {
	Comments Comments
	Table    *TableName
	Columns  Columns
	Rows     InsertRows
	OnDup    OnDup
}

func (node *Insert) Format(buf *TrackedBuffer) {
	buf.Myprintf("insert %vinto %v%v %v%v",
		node.Comments,
		node.Table, node.Columns, node.Rows, node.OnDup)
}

// InsertRows represents the rows for an INSERT statement.
type InsertRows interface {
	IInsertRows()
	SQLNode
}

func (*Select) IInsertRows() {}
func (*Union) IInsertRows()  {}
func (Values) IInsertRows()  {}

// Update represents an UPDATE statement.
type Update struct {
	Comments Comments
	Table    *TableName
	Exprs    UpdateExprs
	Where    *Where
	OrderBy  OrderBy
	Limit    *Limit
}

func (node *Update) Format(buf *TrackedBuffer) {
	buf.Myprintf("update %v%v set %v%v%v%v",
		node.Comments, node.Table,
		node.Exprs, node.Where, node.OrderBy, node.Limit)
}

// Delete represents a DELETE statement.
type Delete struct {
	Comments Comments
	Table    *TableName
	Where    *Where
	OrderBy  OrderBy
	Limit    *Limit
}

func (node *Delete) Format(buf *TrackedBuffer) {
	buf.Myprintf("delete %vfrom %v%v%v%v",
		node.Comments,
		node.Table, node.Where, node.OrderBy, node.Limit)
}

// Set represents a SET statement.
type Set struct {
	Comments Comments
	Exprs    UpdateExprs
}

func (node *Set) Format(buf *TrackedBuffer) {
	buf.Myprintf("set %v%v", node.Comments, node.Exprs)
}

// DDL represents a CREATE, ALTER, DROP or RENAME statement.
// Table is set for AST_ALTER, AST_DROP, AST_RENAME.
// NewName is set for AST_ALTER, AST_CREATE, AST_RENAME.
type DDL struct {
	Action  string
	Table   []byte
	NewName []byte
}

const (
	AST_CREATE = "create"
	AST_ALTER  = "alter"
	AST_DROP   = "drop"
	AST_RENAME = "rename"
)

func (node *DDL) Format(buf *TrackedBuffer) {
	switch node.Action {
	case AST_CREATE:
		buf.Myprintf("%s table %s", node.Action, node.NewName)
	case AST_RENAME:
		buf.Myprintf("%s table %s %s", node.Action, node.Table, node.NewName)
	default:
		buf.Myprintf("%s table %s", node.Action, node.Table)
	}
}

// Other represents a SHOW, DESCRIBE, or EXPLAIN statement.
// It should be used only as an indicator. It does not contain
// the full AST for the statement.
type Other struct{}

func (node *Other) Format(buf *TrackedBuffer) {
	buf.WriteString("other")
}

// Comments represents a list of comments.
type Comments [][]byte

func (node Comments) Format(buf *TrackedBuffer) {
	for _, c := range node {
		buf.Myprintf("%s ", c)
	}
}

// SelectExprs represents SELECT expressions.
type SelectExprs []SelectExpr

func (node SelectExprs) Format(buf *TrackedBuffer) {
	var prefix string
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// SelectExpr represents a SELECT expression.
type SelectExpr interface {
	ISelectExpr()
	SQLNode
}

func (*StarExpr) ISelectExpr()    {}
func (*NonStarExpr) ISelectExpr() {}

// StarExpr defines a '*' or 'table.*' expression.
type StarExpr struct {
	TableName []byte
}

func (node *StarExpr) Format(buf *TrackedBuffer) {
	if node.TableName != nil {
		buf.Myprintf("%s.", node.TableName)
	}
	buf.Myprintf("*")
}

// NonStarExpr defines a non-'*' select expr.
type NonStarExpr struct {
	Expr Expr
	As   []byte
}

func (node *NonStarExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v", node.Expr)
	if node.As != nil {
		buf.Myprintf(" as %s", node.As)
	}
}

// Columns represents an insert column list.
// The syntax for Columns is a subset of SelectExprs.
// So, it's castable to a SelectExprs and can be analyzed
// as such.
type Columns []SelectExpr

func (node Columns) Format(buf *TrackedBuffer) {
	if node == nil {
		return
	}
	buf.Myprintf("(%v)", SelectExprs(node))
}

// TableExprs represents a list of table expressions.
type TableExprs []TableExpr

func (node TableExprs) Format(buf *TrackedBuffer) {
	var prefix string
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// TableExpr represents a table expression.
type TableExpr interface {
	ITableExpr()
	SQLNode
}

func (*AliasedTableExpr) ITableExpr() {}
func (*ParenTableExpr) ITableExpr()   {}
func (*JoinTableExpr) ITableExpr()    {}

// AliasedTableExpr represents a table expression
// coupled with an optional alias or index hint.
type AliasedTableExpr struct {
	Expr  SimpleTableExpr
	As    []byte
	Hints *IndexHints
}

func (node *AliasedTableExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v", node.Expr)
	if node.As != nil {
		buf.Myprintf(" as %s", node.As)
	}
	if node.Hints != nil {
		// Hint node provides the space padding.
		buf.Myprintf("%v", node.Hints)
	}
}

// SimpleTableExpr represents a simple table expression.
type SimpleTableExpr interface {
	ISimpleTableExpr()
	SQLNode
}

func (*TableName) ISimpleTableExpr() {}
func (*Subquery) ISimpleTableExpr()  {}

// TableName represents a table  name.
type TableName struct {
	Name, Qualifier []byte
}

func (node *TableName) Format(buf *TrackedBuffer) {
	if node.Qualifier != nil {
		escape(buf, node.Qualifier)
		buf.Myprintf(".")
	}
	escape(buf, node.Name)
}

// ParenTableExpr represents a parenthesized TableExpr.
type ParenTableExpr struct {
	Expr TableExpr
}

func (node *ParenTableExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("(%v)", node.Expr)
}

// JoinTableExpr represents a TableExpr that's a JOIN operation.
type JoinTableExpr struct {
	LeftExpr  TableExpr
	Join      string
	RightExpr TableExpr
	On        BoolExpr
}

// JoinTableExpr.Join
const (
	AST_JOIN          = "join"
	AST_STRAIGHT_JOIN = "straight_join"
	AST_LEFT_JOIN     = "left join"
	AST_RIGHT_JOIN    = "right join"
	AST_CROSS_JOIN    = "cross join"
	AST_NATURAL_JOIN  = "natural join"
)

func (node *JoinTableExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v %s %v", node.LeftExpr, node.Join, node.RightExpr)
	if node.On != nil {
		buf.Myprintf(" on %v", node.On)
	}
}

// IndexHints represents a list of index hints.
type IndexHints struct {
	Type    string
	Indexes [][]byte
}

const (
	AST_USE    = "use"
	AST_IGNORE = "ignore"
	AST_FORCE  = "force"
)

func (node *IndexHints) Format(buf *TrackedBuffer) {
	buf.Myprintf(" %s index ", node.Type)
	prefix := "("
	for _, n := range node.Indexes {
		buf.Myprintf("%s%s", prefix, n)
		prefix = ", "
	}
	buf.Myprintf(")")
}

// Where represents a WHERE or HAVING clause.
type Where struct {
	Type string
	Expr BoolExpr
}

// Where.Type
const (
	AST_WHERE  = "where"
	AST_HAVING = "having"
)

// NewWhere creates a WHERE or HAVING clause out
// of a BoolExpr. If the expression is nil, it returns nil.
func NewWhere(typ string, expr BoolExpr) *Where {
	if expr == nil {
		return nil
	}
	return &Where{Type: typ, Expr: expr}
}

func (node *Where) Format(buf *TrackedBuffer) {
	if node == nil || node.Expr == nil {
		return
	}
	buf.Myprintf(" %s %v", node.Type, node.Expr)
}

// From represents a FROM clause
type From struct {
	Type string
	Expr TableExprs
}

// From.Type
const (
	AST_FROM = "from"
)

// NewFrom creates a FROM clause
// of a table list expression. If the expression is nil, it returns nil.
func NewFrom(typ string, expr TableExprs) *From {
	if expr == nil {
		return nil
	}
	return &From{Type: typ, Expr: expr}
}

func (node *From) Format(buf *TrackedBuffer) {
	if node == nil || node.Expr == nil {
		return
	}
	buf.Myprintf("%v", node.Expr)
}

// Expr represents an expression.
type Expr interface {
	IExpr()
	SQLNode
}

func (*AndExpr) IExpr()        {}
func (*OrExpr) IExpr()         {}
func (*NotExpr) IExpr()        {}
func (*ParenBoolExpr) IExpr()  {}
func (*ComparisonExpr) IExpr() {}
func (*RangeCond) IExpr()      {}
func (*NullCheck) IExpr()      {}
func (*ExistsExpr) IExpr()     {}
func (*KeyrangeExpr) IExpr()   {}
func (StrVal) IExpr()          {}
func (NumVal) IExpr()          {}
func (ValArg) IExpr()          {}
func (*NullVal) IExpr()        {}
func (*ColName) IExpr()        {}
func (ValTuple) IExpr()        {}
func (*Subquery) IExpr()       {}
func (ListArg) IExpr()         {}
func (*BinaryExpr) IExpr()     {}
func (*UnaryExpr) IExpr()      {}
func (*FuncExpr) IExpr()       {}
func (*CaseExpr) IExpr()       {}

// BoolExpr represents a boolean expression.
type BoolExpr interface {
	IBoolExpr()
	Expr
}

func (*AndExpr) IBoolExpr()        {}
func (*OrExpr) IBoolExpr()         {}
func (*NotExpr) IBoolExpr()        {}
func (*ParenBoolExpr) IBoolExpr()  {}
func (*ComparisonExpr) IBoolExpr() {}
func (*RangeCond) IBoolExpr()      {}
func (*NullCheck) IBoolExpr()      {}
func (*ExistsExpr) IBoolExpr()     {}
func (*KeyrangeExpr) IBoolExpr()   {}

// AndExpr represents an AND expression.
type AndExpr struct {
	Left, Right BoolExpr
}

func (node *AndExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v and %v", node.Left, node.Right)
}

// OrExpr represents an OR expression.
type OrExpr struct {
	Left, Right BoolExpr
}

func (node *OrExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v or %v", node.Left, node.Right)
}

// NotExpr represents a NOT expression.
type NotExpr struct {
	Expr BoolExpr
}

func (node *NotExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("not %v", node.Expr)
}

// ParenBoolExpr represents a parenthesized boolean expression.
type ParenBoolExpr struct {
	Expr BoolExpr
}

func (node *ParenBoolExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("(%v)", node.Expr)
}

// ComparisonExpr represents a two-value comparison expression.
type ComparisonExpr struct {
	Operator    string
	Left, Right ValExpr
}

// ComparisonExpr.Operator
const (
	AST_EQ       = "="
	AST_LT       = "<"
	AST_GT       = ">"
	AST_LE       = "<="
	AST_GE       = ">="
	AST_NE       = "!="
	AST_NSE      = "<=>"
	AST_IN       = "in"
	AST_NOT_IN   = "not in"
	AST_LIKE     = "like"
	AST_NOT_LIKE = "not like"
)

func (node *ComparisonExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v %s %v", node.Left, node.Operator, node.Right)
}

// RangeCond represents a BETWEEN or a NOT BETWEEN expression.
type RangeCond struct {
	Operator string
	Left     ValExpr
	From, To ValExpr
}

// RangeCond.Operator
const (
	AST_BETWEEN     = "between"
	AST_NOT_BETWEEN = "not between"
)

func (node *RangeCond) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v %s %v and %v", node.Left, node.Operator, node.From, node.To)
}

// NullCheck represents an IS NULL or an IS NOT NULL expression.
type NullCheck struct {
	Operator string
	Expr     ValExpr
}

// NullCheck.Operator
const (
	AST_IS_NULL     = "is null"
	AST_IS_NOT_NULL = "is not null"
)

func (node *NullCheck) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v %s", node.Expr, node.Operator)
}

// ExistsExpr represents an EXISTS expression.
type ExistsExpr struct {
	Subquery *Subquery
}

func (node *ExistsExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("exists %v", node.Subquery)
}

// KeyrangeExpr represents a KEYRANGE expression.
type KeyrangeExpr struct {
	Start, End ValExpr
}

func (node *KeyrangeExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("keyrange(%v, %v)", node.Start, node.End)
}

// ValExpr represents a value expression.
type ValExpr interface {
	IValExpr()
	Expr
}

func (StrVal) IValExpr()      {}
func (NumVal) IValExpr()      {}
func (ValArg) IValExpr()      {}
func (*NullVal) IValExpr()    {}
func (*ColName) IValExpr()    {}
func (ValTuple) IValExpr()    {}
func (*Subquery) IValExpr()   {}
func (ListArg) IValExpr()     {}
func (*BinaryExpr) IValExpr() {}
func (*UnaryExpr) IValExpr()  {}
func (*FuncExpr) IValExpr()   {}
func (*CaseExpr) IValExpr()   {}

// StrVal represents a string value.
type StrVal []byte

func (node StrVal) Format(buf *TrackedBuffer) {
	s := sqltypes.MakeString([]byte(node))
	s.EncodeSql(buf)
}

// NumVal represents a number.
type NumVal []byte

func (node NumVal) Format(buf *TrackedBuffer) {
	buf.Myprintf("%s", []byte(node))
}

// ValArg represents a named bind var argument.
type ValArg []byte

func (node ValArg) Format(buf *TrackedBuffer) {
	buf.WriteArg(string(node))
}

// NullVal represents a NULL value.
type NullVal struct{}

func (node *NullVal) Format(buf *TrackedBuffer) {
	buf.Myprintf("null")
}

// ColName represents a column name.
type ColName struct {
	Name, Qualifier []byte
}

func (node *ColName) Format(buf *TrackedBuffer) {
	if node.Qualifier != nil {
		escape(buf, node.Qualifier)
		buf.Myprintf(".")
	}
	escape(buf, node.Name)
}

func escape(buf *TrackedBuffer, name []byte) {
	if _, ok := keywords[string(name)]; ok {
		buf.Myprintf("`%s`", name)
	} else {
		buf.Myprintf("%s", name)
	}
}

// ColTuple represents a list of column values.
// It can be ValTuple, Subquery, ListArg.
type ColTuple interface {
	IColTuple()
	ValExpr
}

func (ValTuple) IColTuple()  {}
func (*Subquery) IColTuple() {}
func (ListArg) IColTuple()   {}

// ValTuple represents a tuple of actual values.
type ValTuple ValExprs

func (node ValTuple) Format(buf *TrackedBuffer) {
	buf.Myprintf("(%v)", ValExprs(node))
}

// ValExprs represents a list of value expressions.
// It's not a valid expression because it's not parenthesized.
type ValExprs []ValExpr

func (node ValExprs) Format(buf *TrackedBuffer) {
	var prefix string
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// Subquery represents a subquery.
type Subquery struct {
	Select SelectStatement
}

func (node *Subquery) Format(buf *TrackedBuffer) {
	buf.Myprintf("(%v)", node.Select)
}

// ListArg represents a named list argument.
type ListArg []byte

func (node ListArg) Format(buf *TrackedBuffer) {
	buf.WriteArg(string(node))
}

// BinaryExpr represents a binary value expression.
type BinaryExpr struct {
	Operator    byte
	Left, Right Expr
}

// BinaryExpr.Operator
const (
	AST_BITAND = '&'
	AST_BITOR  = '|'
	AST_BITXOR = '^'
	AST_PLUS   = '+'
	AST_MINUS  = '-'
	AST_MULT   = '*'
	AST_DIV    = '/'
	AST_MOD    = '%'
)

func (node *BinaryExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v%c%v", node.Left, node.Operator, node.Right)
}

// UnaryExpr represents a unary value expression.
type UnaryExpr struct {
	Operator byte
	Expr     Expr
}

// UnaryExpr.Operator
const (
	AST_UPLUS  = '+'
	AST_UMINUS = '-'
	AST_TILDA  = '~'
)

func (node *UnaryExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%c%v", node.Operator, node.Expr)
}

// FuncExpr represents a function call.
type FuncExpr struct {
	Name     []byte
	Distinct bool
	Exprs    SelectExprs
}

func (node *FuncExpr) Format(buf *TrackedBuffer) {
	var distinct string
	if node.Distinct {
		distinct = "distinct "
	}
	buf.Myprintf("%s(%s%v)", node.Name, distinct, node.Exprs)
}

// Aggregates is a map of all aggregate functions.
var Aggregates = map[string]bool{
	"avg":          true,
	"bit_and":      true,
	"bit_or":       true,
	"bit_xor":      true,
	"count":        true,
	"group_concat": true,
	"max":          true,
	"min":          true,
	"std":          true,
	"stddev_pop":   true,
	"stddev_samp":  true,
	"stddev":       true,
	"sum":          true,
	"var_pop":      true,
	"var_samp":     true,
	"variance":     true,
}

func (node *FuncExpr) IsAggregate() bool {
	return Aggregates[string(node.Name)]
}

// CaseExpr represents a CASE expression.
type CaseExpr struct {
	Expr  ValExpr
	Whens []*When
	Else  ValExpr
}

func (node *CaseExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("case ")
	if node.Expr != nil {
		buf.Myprintf("%v ", node.Expr)
	}
	for _, when := range node.Whens {
		buf.Myprintf("%v ", when)
	}
	if node.Else != nil {
		buf.Myprintf("else %v ", node.Else)
	}
	buf.Myprintf("end")
}

// When represents a WHEN sub-expression.
type When struct {
	Cond BoolExpr
	Val  ValExpr
}

func (node *When) Format(buf *TrackedBuffer) {
	buf.Myprintf("when %v then %v", node.Cond, node.Val)
}

// GroupBy represents a GROUP BY clause.
type GroupBy []ValExpr

func (node GroupBy) Format(buf *TrackedBuffer) {
	prefix := " group by "
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// OrderBy represents an ORDER By clause.
type OrderBy []*Order

func (node OrderBy) Format(buf *TrackedBuffer) {
	prefix := " order by "
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// Order represents an ordering expression.
type Order struct {
	Expr      ValExpr
	Direction string
}

// Order.Direction
const (
	AST_ASC  = "asc"
	AST_DESC = "desc"
)

func (node *Order) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v %s", node.Expr, node.Direction)
}

// Limit represents a LIMIT clause.
type Limit struct {
	Offset, Rowcount ValExpr
}

func (node *Limit) Format(buf *TrackedBuffer) {
	if node == nil {
		return
	}
	buf.Myprintf(" limit ")
	if node.Offset != nil {
		buf.Myprintf("%v, ", node.Offset)
	}
	buf.Myprintf("%v", node.Rowcount)
}

// Limits returns the values of the LIMIT clause as interfaces.
// The returned values can be nil for absent field, string for
// bind variable names, or int64 for an actual number.
// Otherwise, it's an error.
func (node *Limit) Limits() (offset, rowcount interface{}, err error) {
	if node == nil {
		return nil, nil, nil
	}
	switch v := node.Offset.(type) {
	case NumVal:
		o, err := strconv.ParseInt(string(v), 0, 64)
		if err != nil {
			return nil, nil, err
		}
		if o < 0 {
			return nil, nil, fmt.Errorf("negative offset: %d", o)
		}
		offset = o
	case ValArg:
		offset = string(v)
	case nil:
		// pass
	default:
		return nil, nil, fmt.Errorf("unexpected node for offset: %+v", v)
	}
	switch v := node.Rowcount.(type) {
	case NumVal:
		rc, err := strconv.ParseInt(string(v), 0, 64)
		if err != nil {
			return nil, nil, err
		}
		if rc < 0 {
			return nil, nil, fmt.Errorf("negative limit: %d", rc)
		}
		rowcount = rc
	case ValArg:
		rowcount = string(v)
	default:
		return nil, nil, fmt.Errorf("unexpected node for rowcount: %+v", v)
	}
	return offset, rowcount, nil
}

// Values represents a VALUES clause.
type Values []RowTuple

func (node Values) Format(buf *TrackedBuffer) {
	prefix := "values "
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// RowTuple represents a row of values. It can be ValTuple, Subquery.
type RowTuple interface {
	IRowTuple()
	ValExpr
}

func (ValTuple) IRowTuple()  {}
func (*Subquery) IRowTuple() {}

// UpdateExprs represents a list of update expressions.
type UpdateExprs []*UpdateExpr

func (node UpdateExprs) Format(buf *TrackedBuffer) {
	var prefix string
	for _, n := range node {
		buf.Myprintf("%s%v", prefix, n)
		prefix = ", "
	}
}

// UpdateExpr represents an update expression.
type UpdateExpr struct {
	Name *ColName
	Expr ValExpr
}

func (node *UpdateExpr) Format(buf *TrackedBuffer) {
	buf.Myprintf("%v = %v", node.Name, node.Expr)
}

// OnDup represents an ON DUPLICATE KEY clause.
type OnDup UpdateExprs

func (node OnDup) Format(buf *TrackedBuffer) {
	if node == nil {
		return
	}
	buf.Myprintf(" on duplicate key update %v", UpdateExprs(node))
}
```

## File: `sqlparser/fuzz.go`
```go
package sqlparser

func Fuzz(data []byte) int {
	_, err := Parse(string(data))
	if err != nil {
		return 0
	}
	return 1
}
```

## File: `sqlparser/parsed_query.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package sqlparser

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"

	"github.com/dinedal/textql/sqlparser/sqltypes"
)

type bindLocation struct {
	offset, length int
}

type ParsedQuery struct {
	Query         string
	bindLocations []bindLocation
}

type EncoderFunc func(value interface{}) ([]byte, error)

func (pq *ParsedQuery) GenerateQuery(bindVariables map[string]interface{}) ([]byte, error) {
	if len(pq.bindLocations) == 0 {
		return []byte(pq.Query), nil
	}
	buf := bytes.NewBuffer(make([]byte, 0, len(pq.Query)))
	current := 0
	for _, loc := range pq.bindLocations {
		buf.WriteString(pq.Query[current:loc.offset])
		name := pq.Query[loc.offset : loc.offset+loc.length]
		supplied, _, err := FetchBindVar(name, bindVariables)
		if err != nil {
			return nil, err
		}
		if err := EncodeValue(buf, supplied); err != nil {
			return nil, err
		}
		current = loc.offset + loc.length
	}
	buf.WriteString(pq.Query[current:])
	return buf.Bytes(), nil
}

func (pq *ParsedQuery) MarshalJSON() ([]byte, error) {
	return json.Marshal(pq.Query)
}

func EncodeValue(buf *bytes.Buffer, value interface{}) error {
	switch bindVal := value.(type) {
	case nil:
		buf.WriteString("null")
	case []sqltypes.Value:
		for i := 0; i < len(bindVal); i++ {
			if i != 0 {
				buf.WriteString(", ")
			}
			if err := EncodeValue(buf, bindVal[i]); err != nil {
				return err
			}
		}
	case [][]sqltypes.Value:
		for i := 0; i < len(bindVal); i++ {
			if i != 0 {
				buf.WriteString(", ")
			}
			buf.WriteByte('(')
			if err := EncodeValue(buf, bindVal[i]); err != nil {
				return err
			}
			buf.WriteByte(')')
		}
	case []interface{}:
		buf.WriteByte('(')
		for i, v := range bindVal {
			if i != 0 {
				buf.WriteString(", ")
			}
			if err := EncodeValue(buf, v); err != nil {
				return err
			}
		}
		buf.WriteByte(')')
	case TupleEqualityList:
		if err := bindVal.Encode(buf); err != nil {
			return err
		}
	default:
		v, err := sqltypes.BuildValue(bindVal)
		if err != nil {
			return err
		}
		v.EncodeSql(buf)
	}
	return nil
}

type TupleEqualityList struct {
	Columns []string
	Rows    [][]sqltypes.Value
}

func (tpl *TupleEqualityList) Encode(buf *bytes.Buffer) error {
	if len(tpl.Rows) == 0 {
		return errors.New("cannot encode with 0 rows")
	}
	if len(tpl.Columns) == 1 {
		return tpl.encodeAsIN(buf)
	}
	return tpl.encodeAsEquality(buf)
}

func (tpl *TupleEqualityList) encodeAsIN(buf *bytes.Buffer) error {
	buf.WriteString(tpl.Columns[0])
	buf.WriteString(" in (")
	for i, r := range tpl.Rows {
		if len(r) != 1 {
			return errors.New("values don't match column count")
		}
		if i != 0 {
			buf.WriteString(", ")
		}
		if err := EncodeValue(buf, r); err != nil {
			return err
		}
	}
	buf.WriteByte(')')
	return nil
}

func (tpl *TupleEqualityList) encodeAsEquality(buf *bytes.Buffer) error {
	for i, r := range tpl.Rows {
		if i != 0 {
			buf.WriteString(" or ")
		}
		buf.WriteString("(")
		for j, c := range tpl.Columns {
			if j != 0 {
				buf.WriteString(" and ")
			}
			buf.WriteString(c)
			buf.WriteString(" = ")
			if err := EncodeValue(buf, r[j]); err != nil {
				return err
			}
		}
		buf.WriteByte(')')
	}
	return nil
}

func FetchBindVar(name string, bindVariables map[string]interface{}) (val interface{}, isList bool, err error) {
	name = name[1:]
	if name[0] == ':' {
		name = name[1:]
		isList = true
	}
	supplied, ok := bindVariables[name]
	if !ok {
		return nil, false, fmt.Errorf("missing bind var %s", name)
	}
	list, gotList := supplied.([]interface{})
	if isList {
		if !gotList {
			return nil, false, fmt.Errorf("unexpected list arg type %T for key %s", supplied, name)
		}
		if len(list) == 0 {
			return nil, false, fmt.Errorf("empty list supplied for %s", name)
		}
		return list, true, nil
	}
	if gotList {
		return nil, false, fmt.Errorf("unexpected arg type %T for key %s", supplied, name)
	}
	return supplied, false, nil
}
```

## File: `sqlparser/sql.go`
```go
//line sql.y:6
package sqlparser

import __yyfmt__ "fmt"

//line sql.y:6
import "bytes"

func SetParseTree(yylex interface{}, stmt Statement) {
	yylex.(*Tokenizer).ParseTree = stmt
}

func SetAllowComments(yylex interface{}, allow bool) {
	yylex.(*Tokenizer).AllowComments = allow
}

func ForceEOF(yylex interface{}) {
	yylex.(*Tokenizer).ForceEOF = true
}

var (
	SHARE        = []byte("share")
	MODE         = []byte("mode")
	IF_BYTES     = []byte("if")
	VALUES_BYTES = []byte("values")
)

//line sql.y:31
type yySymType struct {
	yys         int
	empty       struct{}
	statement   Statement
	selStmt     SelectStatement
	byt         byte
	bytes       []byte
	bytes2      [][]byte
	str         string
	selectExprs SelectExprs
	selectExpr  SelectExpr
	columns     Columns
	colName     *ColName
	tableExprs  TableExprs
	tableExpr   TableExpr
	smTableExpr SimpleTableExpr
	tableName   *TableName
	indexHints  *IndexHints
	expr        Expr
	boolExpr    BoolExpr
	valExpr     ValExpr
	colTuple    ColTuple
	valExprs    ValExprs
	values      Values
	rowTuple    RowTuple
	subquery    *Subquery
	caseExpr    *CaseExpr
	whens       []*When
	when        *When
	orderBy     OrderBy
	order       *Order
	limit       *Limit
	insRows     InsertRows
	updateExprs UpdateExprs
	updateExpr  *UpdateExpr
}

const LEX_ERROR = 57346
const SELECT = 57347
const INSERT = 57348
const UPDATE = 57349
const DELETE = 57350
const FROM = 57351
const WHERE = 57352
const GROUP = 57353
const HAVING = 57354
const ORDER = 57355
const BY = 57356
const LIMIT = 57357
const FOR = 57358
const ALL = 57359
const DISTINCT = 57360
const AS = 57361
const EXISTS = 57362
const IN = 57363
const IS = 57364
const LIKE = 57365
const BETWEEN = 57366
const NULL = 57367
const ASC = 57368
const DESC = 57369
const VALUES = 57370
const INTO = 57371
const DUPLICATE = 57372
const KEY = 57373
const DEFAULT = 57374
const SET = 57375
const LOCK = 57376
const KEYRANGE = 57377
const ID = 57378
const STRING = 57379
const NUMBER = 57380
const VALUE_ARG = 57381
const LIST_ARG = 57382
const COMMENT = 57383
const LE = 57384
const GE = 57385
const NE = 57386
const NULL_SAFE_EQUAL = 57387
const UNION = 57388
const MINUS = 57389
const EXCEPT = 57390
const INTERSECT = 57391
const JOIN = 57392
const STRAIGHT_JOIN = 57393
const LEFT = 57394
const RIGHT = 57395
const INNER = 57396
const OUTER = 57397
const CROSS = 57398
const NATURAL = 57399
const USE = 57400
const FORCE = 57401
const ON = 57402
const OR = 57403
const AND = 57404
const NOT = 57405
const UNARY = 57406
const CASE = 57407
const WHEN = 57408
const THEN = 57409
const ELSE = 57410
const END = 57411
const CREATE = 57412
const ALTER = 57413
const DROP = 57414
const RENAME = 57415
const ANALYZE = 57416
const TABLE = 57417
const INDEX = 57418
const VIEW = 57419
const TO = 57420
const IGNORE = 57421
const IF = 57422
const UNIQUE = 57423
const USING = 57424
const SHOW = 57425
const DESCRIBE = 57426
const EXPLAIN = 57427

var yyToknames = []string{
	"LEX_ERROR",
	"SELECT",
	"INSERT",
	"UPDATE",
	"DELETE",
	"FROM",
	"WHERE",
	"GROUP",
	"HAVING",
	"ORDER",
	"BY",
	"LIMIT",
	"FOR",
	"ALL",
	"DISTINCT",
	"AS",
	"EXISTS",
	"IN",
	"IS",
	"LIKE",
	"BETWEEN",
	"NULL",
	"ASC",
	"DESC",
	"VALUES",
	"INTO",
	"DUPLICATE",
	"KEY",
	"DEFAULT",
	"SET",
	"LOCK",
	"KEYRANGE",
	"ID",
	"STRING",
	"NUMBER",
	"VALUE_ARG",
	"LIST_ARG",
	"COMMENT",
	"LE",
	"GE",
	"NE",
	"NULL_SAFE_EQUAL",
	"'('",
	"'='",
	"'<'",
	"'>'",
	"'~'",
	"UNION",
	"MINUS",
	"EXCEPT",
	"INTERSECT",
	"','",
	"JOIN",
	"STRAIGHT_JOIN",
	"LEFT",
	"RIGHT",
	"INNER",
	"OUTER",
	"CROSS",
	"NATURAL",
	"USE",
	"FORCE",
	"ON",
	"OR",
	"AND",
	"NOT",
	"'&'",
	"'|'",
	"'^'",
	"'+'",
	"'-'",
	"'*'",
	"'/'",
	"'%'",
	"'.'",
	"UNARY",
	"CASE",
	"WHEN",
	"THEN",
	"ELSE",
	"END",
	"CREATE",
	"ALTER",
	"DROP",
	"RENAME",
	"ANALYZE",
	"TABLE",
	"INDEX",
	"VIEW",
	"TO",
	"IGNORE",
	"IF",
	"UNIQUE",
	"USING",
	"SHOW",
	"DESCRIBE",
	"EXPLAIN",
}
var yyStatenames = []string{}

const yyEofCode = 1
const yyErrCode = 2
const yyMaxDepth = 200

//line yacctab:1
var yyExca = []int{
	-1, 1,
	1, -1,
	-2, 0,
}

const yyNprod = 207
const yyPrivate = 57344

var yyTokenNames []string
var yyStates []string

const yyLast = 678

var yyAct = []int{

	51, 122, 141, 363, 359, 342, 49, 48, 83, 314,
	366, 280, 126, 334, 225, 159, 142, 42, 43, 125,
	3, 163, 205, 174, 332, 60, 47, 90, 138, 381,
	381, 37, 31, 32, 33, 34, 84, 85, 99, 98,
	268, 94, 15, 17, 18, 19, 153, 146, 127, 381,
	86, 340, 128, 91, 196, 29, 320, 91, 91, 219,
	71, 196, 73, 121, 124, 76, 74, 77, 136, 330,
	20, 144, 194, 38, 148, 383, 382, 150, 143, 329,
	132, 154, 195, 328, 147, 230, 231, 232, 233, 234,
	43, 235, 236, 43, 149, 380, 168, 339, 170, 302,
	299, 82, 173, 251, 249, 181, 182, 197, 185, 186,
	187, 188, 189, 190, 191, 192, 171, 172, 167, 304,
	157, 78, 21, 22, 24, 23, 25, 176, 293, 295,
	297, 198, 43, 43, 206, 26, 27, 28, 79, 80,
	81, 206, 183, 255, 241, 99, 98, 152, 215, 109,
	110, 111, 112, 113, 214, 209, 223, 216, 294, 218,
	306, 203, 200, 202, 193, 161, 207, 97, 96, 210,
	274, 111, 112, 113, 99, 98, 98, 198, 227, 211,
	335, 244, 245, 327, 325, 224, 184, 240, 242, 272,
	335, 167, 316, 275, 170, 222, 287, 326, 248, 291,
	285, 288, 243, 43, 176, 286, 290, 169, 160, 144,
	289, 260, 144, 211, 264, 373, 143, 354, 196, 143,
	252, 228, 265, 212, 256, 92, 262, 254, 263, 155,
	129, 352, 278, 250, 258, 230, 231, 232, 233, 234,
	279, 235, 236, 271, 273, 270, 166, 259, 301, 351,
	283, 284, 15, 211, 167, 167, 165, 305, 350, 144,
	144, 310, 31, 32, 33, 34, 143, 312, 177, 317,
	134, 91, 133, 131, 175, 130, 313, 309, 318, 303,
	158, 239, 96, 166, 198, 123, 346, 345, 298, 95,
	322, 59, 296, 165, 321, 324, 277, 276, 238, 323,
	261, 220, 331, 56, 57, 58, 96, 217, 333, 213,
	139, 156, 151, 16, 364, 337, 208, 370, 353, 15,
	137, 247, 379, 341, 338, 266, 29, 178, 348, 179,
	180, 221, 365, 347, 87, 343, 344, 282, 315, 281,
	226, 144, 308, 349, 160, 357, 360, 356, 355, 88,
	140, 367, 367, 367, 361, 384, 378, 362, 15, 36,
	267, 371, 368, 369, 72, 319, 269, 75, 377, 145,
	311, 257, 374, 358, 385, 360, 375, 376, 386, 35,
	388, 387, 389, 253, 201, 144, 54, 390, 135, 391,
	204, 59, 143, 53, 65, 50, 52, 67, 68, 69,
	70, 55, 41, 56, 57, 58, 336, 307, 100, 44,
	292, 164, 46, 229, 162, 40, 63, 237, 93, 30,
	106, 107, 108, 109, 110, 111, 112, 113, 89, 14,
	13, 12, 11, 10, 9, 45, 8, 7, 6, 61,
	62, 39, 5, 4, 2, 1, 66, 54, 0, 0,
	0, 0, 59, 0, 0, 65, 0, 0, 0, 0,
	0, 64, 55, 41, 56, 57, 58, 199, 0, 372,
	0, 0, 0, 46, 0, 0, 0, 63, 0, 0,
	0, 0, 0, 15, 106, 107, 108, 109, 110, 111,
	112, 113, 0, 0, 0, 0, 45, 0, 54, 0,
	61, 62, 39, 59, 0, 0, 65, 66, 0, 0,
	0, 0, 0, 55, 123, 56, 57, 58, 54, 0,
	0, 0, 64, 59, 46, 0, 65, 0, 63, 0,
	0, 0, 0, 55, 123, 56, 57, 58, 0, 0,
	0, 0, 0, 15, 46, 0, 0, 45, 63, 0,
	0, 61, 62, 0, 0, 0, 0, 0, 66, 0,
	0, 0, 0, 59, 0, 0, 65, 45, 0, 0,
	0, 61, 62, 64, 123, 56, 57, 58, 66, 0,
	0, 0, 0, 59, 129, 0, 65, 0, 63, 0,
	0, 0, 0, 64, 123, 56, 57, 58, 0, 0,
	0, 0, 0, 0, 129, 0, 0, 0, 63, 0,
	0, 61, 62, 101, 105, 103, 104, 300, 66, 106,
	107, 108, 109, 110, 111, 112, 113, 0, 0, 0,
	0, 61, 62, 64, 117, 118, 119, 120, 66, 114,
	115, 116, 246, 0, 106, 107, 108, 109, 110, 111,
	112, 113, 0, 64, 0, 0, 0, 0, 0, 0,
	0, 102, 106, 107, 108, 109, 110, 111, 112, 113,
	106, 107, 108, 109, 110, 111, 112, 113,
}
var yyPact = []int{

	37, -1000, -1000, 211, -1000, -1000, -1000, -1000, -1000, -1000,
	-1000, -1000, -1000, -1000, -1000, -1000, 427, -1000, -1000, -1000,
	-1000, -30, -27, 31, 48, 11, -1000, -1000, -1000, -1000,
	353, 317, -1000, -1000, -1000, 308, -1000, 216, -1000, -1000,
	270, 89, 107, 592, -1000, 498, 478, -1000, -1000, -1000,
	558, 229, 227, -1000, 226, 224, -1000, -1000, -1000, -1000,
	-1000, -1000, -1000, -1000, -1000, -1000, 558, 291, 274, 341,
	249, -48, -7, 246, -1000, 4, 246, -1000, 276, -49,
	246, -49, 275, -1000, -1000, -1000, -1000, -1000, 427, 239,
	334, 427, 210, -1000, -1000, 246, -1000, 132, 498, 498,
	558, 228, 306, 558, 558, 117, 558, 558, 558, 558,
	558, 558, 558, 558, -1000, -1000, -1000, -1000, -1000, -1000,
	-1000, -1000, 592, 86, -29, -19, 6, 592, -1000, 538,
	366, 427, -1000, 353, 266, 53, 600, 274, 283, 77,
	274, 158, -1000, 176, -1000, 273, 85, 246, -1000, 271,
	-1000, -34, 265, 311, 129, 246, -1000, 216, -1000, 329,
	498, -1000, 166, 179, 262, 247, 66, -1000, -1000, -1000,
	-1000, -1000, 108, 600, -1000, 538, -1000, -1000, 228, 558,
	558, 600, 574, -1000, 296, 76, 76, 76, 96, 96,
	-1000, -1000, -1000, 246, -1000, -1000, 558, -1000, 600, -1000,
	3, 427, 2, 165, 60, -1000, 498, 201, 249, 264,
	334, 249, 558, -1000, 305, -57, -1000, 157, -1000, 261,
	-1000, -1000, 260, -1000, 334, 327, 323, 107, 210, 210,
	-1000, -1000, 144, 140, 154, 150, 143, 64, -1000, 256,
	29, 252, -1, -1000, 600, 549, 558, -1000, 600, -1000,
	-2, -1000, 266, 35, -1000, 558, 78, 314, 249, 249,
	198, -1000, 325, -1000, 600, -1000, -1000, 126, 246, -1000,
	-37, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, 329,
	325, 498, 558, 179, 118, -1000, 141, -1000, 127, -1000,
	-1000, -1000, -1000, -8, -12, -22, -1000, -1000, -1000, -1000,
	558, 600, -1000, -77, -1000, 600, 558, 114, 184, 211,
	124, -4, -1000, 325, 320, 322, 251, -1000, -1000, 250,
	-1000, 327, 320, 107, 163, 498, -1000, -1000, 212, 203,
	185, 600, -1000, 600, -1000, 288, 162, -1000, -1000, -1000,
	249, 320, -1000, 558, 558, -1000, -1000, 325, 298, 107,
	246, 246, 246, 286, 184, -1000, -1000, 414, 160, -1000,
	350, -1000, 320, -1000, 349, 301, -6, -1000, -25, -26,
	348, -1000, 558, 558, -1000, -1000, -1000, 298, -1000, 246,
	-1000, 246, -1000, -1000, 249, 600, -1000, -1000, 246, -1000,
	158, -1000,
}
var yyPgo = []int{

	0, 445, 444, 19, 443, 442, 438, 437, 436, 434,
	433, 432, 431, 430, 429, 379, 428, 419, 313, 31,
	73, 418, 417, 415, 414, 21, 27, 413, 411, 28,
	410, 10, 15, 17, 409, 408, 407, 26, 1, 23,
	12, 406, 6, 396, 25, 395, 7, 393, 390, 22,
	388, 383, 14, 11, 9, 373, 4, 372, 5, 3,
	371, 370, 13, 2, 16, 147, 369, 367, 366, 365,
	364, 360, 0, 8, 359,
}
var yyR1 = []int{

	0, 1, 2, 2, 2, 2, 2, 2, 2, 2,
	2, 2, 2, 2, 4, 3, 3, 5, 5, 6,
	7, 8, 9, 9, 9, 10, 10, 10, 11, 12,
	12, 12, 13, 14, 14, 14, 74, 15, 16, 16,
	17, 17, 17, 17, 17, 18, 18, 19, 19, 20,
	20, 20, 23, 23, 21, 21, 21, 24, 24, 25,
	25, 25, 25, 22, 22, 22, 27, 27, 27, 27,
	27, 27, 27, 27, 27, 28, 28, 28, 29, 29,
	30, 30, 30, 30, 31, 31, 26, 26, 32, 32,
	33, 33, 33, 33, 33, 34, 34, 34, 34, 34,
	34, 34, 34, 34, 34, 34, 35, 35, 35, 35,
	35, 35, 35, 39, 39, 39, 44, 40, 40, 38,
	38, 38, 38, 38, 38, 38, 38, 38, 38, 38,
	38, 38, 38, 38, 38, 38, 43, 43, 45, 45,
	45, 47, 50, 50, 48, 48, 49, 51, 51, 46,
	46, 37, 37, 37, 37, 52, 52, 53, 53, 54,
	54, 55, 55, 56, 57, 57, 57, 58, 58, 58,
	59, 59, 59, 60, 60, 61, 61, 62, 62, 36,
	36, 41, 41, 42, 42, 63, 63, 64, 65, 65,
	66, 66, 67, 67, 68, 68, 68, 68, 68, 69,
	69, 70, 70, 71, 71, 72, 73,
}
var yyR2 = []int{

	0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 9, 11, 3, 7, 7, 8,
	7, 3, 5, 8, 4, 6, 7, 4, 5, 4,
	5, 5, 3, 2, 2, 2, 0, 2, 0, 2,
	1, 2, 1, 1, 1, 0, 1, 1, 3, 1,
	2, 3, 1, 1, 0, 1, 2, 1, 3, 3,
	3, 3, 5, 0, 1, 2, 1, 1, 2, 3,
	2, 3, 2, 2, 2, 1, 3, 1, 1, 3,
	0, 5, 5, 5, 1, 3, 0, 2, 0, 2,
	1, 3, 3, 2, 3, 3, 3, 4, 3, 4,
	5, 6, 3, 4, 2, 6, 1, 1, 1, 1,
	1, 1, 1, 3, 1, 1, 3, 1, 3, 1,
	1, 1, 3, 3, 3, 3, 3, 3, 3, 3,
	2, 3, 4, 5, 4, 1, 1, 1, 1, 1,
	1, 5, 0, 1, 1, 2, 4, 0, 2, 1,
	3, 1, 1, 1, 1, 0, 3, 0, 2, 0,
	3, 1, 3, 2, 0, 1, 1, 0, 2, 4,
	0, 2, 4, 0, 3, 1, 3, 0, 5, 2,
	1, 1, 3, 3, 1, 1, 3, 3, 0, 2,
	0, 3, 0, 1, 1, 1, 1, 1, 1, 0,
	1, 0, 1, 0, 2, 1, 0,
}
var yyChk = []int{

	-1000, -1, -2, -3, -4, -5, -6, -7, -8, -9,
	-10, -11, -12, -13, -14, 5, -18, 6, 7, 8,
	33, 85, 86, 88, 87, 89, 98, 99, 100, 18,
	-17, 51, 52, 53, 54, -15, -74, -19, -20, 75,
	-23, 36, -33, -38, -34, 69, 46, -37, -46, -42,
	-45, -72, -43, -47, 20, 35, 37, 38, 39, 25,
	-44, 73, 74, 50, 95, 28, 80, -15, -15, -15,
	-15, 90, -70, 92, 96, -67, 92, 94, 90, 90,
	91, 92, 90, -73, -73, -73, -3, 17, -18, -16,
	-26, 55, 9, -21, -72, 19, 36, 78, 68, 67,
	-35, 21, 69, 23, 24, 22, 70, 71, 72, 73,
	74, 75, 76, 77, 47, 48, 49, 42, 43, 44,
	45, -33, -38, 36, -33, -3, -40, -38, -38, 46,
	46, 46, -44, 46, 46, -50, -38, 29, -29, 36,
	9, -63, -64, -46, -72, -66, 95, 91, -72, 90,
	-72, 36, -65, 95, -72, -65, 36, -19, 41, -32,
	10, -20, -24, -25, -28, 46, 36, -44, -72, 75,
	-72, -33, -33, -38, -39, 46, -44, 40, 21, 23,
	24, -38, -38, 25, 69, -38, -38, -38, -38, -38,
	-38, -38, -38, 78, 101, 101, 55, 101, -38, 101,
	-19, 18, -19, -37, -48, -49, 81, -29, 33, 78,
	-29, 55, 47, 36, 69, -72, -73, 36, -73, 93,
	36, 20, 66, -72, -26, -52, 11, -33, 55, -27,
	56, 57, 58, 59, 60, 62, 63, -22, 36, 19,
	-25, 78, -40, -39, -38, -38, 68, 25, -38, 101,
	-19, 101, 55, -51, -49, 83, -33, -60, 33, 46,
	-63, 36, -32, -64, -38, -73, 20, -71, 97, -68,
	88, 86, 32, 87, 13, 36, 36, 36, -73, -32,
	-53, 12, 14, -25, -25, 56, 61, 56, 61, 56,
	56, 56, -30, 64, 94, 65, 36, 101, 36, 101,
	68, -38, 101, -37, 84, -38, 82, -36, 28, -3,
	-63, -61, -46, -32, -54, 13, 66, -72, -73, -69,
	93, -52, -54, -33, -40, 66, 56, 56, 91, 91,
	91, -38, 101, -38, -62, 66, -41, -42, -62, 101,
	55, -54, -58, 15, 14, 36, 36, -53, -58, -33,
	46, 46, 46, 30, 55, -46, -58, -38, -55, -56,
	-38, -73, -54, -59, 16, 34, -31, -72, -31, -31,
	31, -42, 55, 55, -57, 26, 27, -58, 7, 21,
	101, 55, 101, 101, 7, -38, -56, -59, -72, -72,
	-63, -72,
}
var yyDef = []int{

	45, -2, 1, 2, 3, 4, 5, 6, 7, 8,
	9, 10, 11, 12, 13, 36, 0, 36, 36, 36,
	36, 201, 192, 0, 0, 0, 206, 206, 206, 46,
	0, 40, 42, 43, 44, 45, 38, 86, 47, 49,
	54, 205, 52, 53, 90, 0, 0, 119, 120, 121,
	0, 149, 0, 135, 0, 0, 151, 152, 153, 154,
	184, 138, 139, 140, 136, 137, 142, 0, 0, 0,
	0, 190, 0, 0, 202, 0, 0, 193, 0, 188,
	0, 188, 0, 33, 34, 35, 16, 41, 0, 37,
	88, 0, 0, 50, 55, 0, 205, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 106, 107, 108, 109, 110, 111,
	112, 93, 0, 205, 0, 0, 0, 117, 130, 0,
	0, 0, 104, 0, 0, 0, 143, 0, 0, 78,
	0, 21, 185, 0, 149, 0, 0, 0, 206, 0,
	206, 0, 0, 0, 0, 0, 32, 86, 39, 155,
	0, 48, 87, 57, 63, 0, 75, 77, 56, 51,
	150, 91, 92, 95, 96, 0, 114, 115, 0, 0,
	0, 98, 0, 102, 0, 122, 123, 124, 125, 126,
	127, 128, 129, 0, 94, 116, 0, 183, 117, 131,
	0, 0, 0, 0, 147, 144, 0, 173, 0, 0,
	88, 0, 0, 206, 0, 203, 24, 0, 27, 0,
	29, 189, 0, 206, 88, 157, 0, 89, 0, 0,
	66, 67, 0, 0, 0, 0, 0, 80, 64, 0,
	0, 0, 0, 97, 99, 0, 0, 103, 118, 132,
	0, 134, 0, 0, 145, 0, 0, 0, 0, 0,
	88, 79, 159, 186, 187, 22, 191, 0, 0, 206,
	199, 194, 195, 196, 197, 198, 28, 30, 31, 155,
	159, 0, 0, 58, 61, 68, 0, 70, 0, 72,
	73, 74, 59, 0, 0, 0, 65, 60, 76, 113,
	0, 100, 133, 0, 141, 148, 0, 177, 0, 180,
	177, 0, 175, 159, 167, 0, 0, 204, 25, 0,
	200, 157, 167, 158, 156, 0, 69, 71, 0, 0,
	0, 101, 105, 146, 17, 0, 179, 181, 18, 174,
	0, 167, 20, 0, 0, 206, 26, 159, 170, 62,
	0, 0, 0, 0, 0, 176, 19, 168, 160, 161,
	164, 23, 167, 14, 0, 0, 0, 84, 0, 0,
	0, 182, 0, 0, 163, 165, 166, 170, 171, 0,
	81, 0, 82, 83, 0, 169, 162, 15, 0, 85,
	178, 172,
}
var yyTok1 = []int{

	1, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 77, 70, 3,
	46, 101, 75, 73, 55, 74, 78, 76, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	48, 47, 49, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 72, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
	3, 3, 3, 3, 71, 3, 50,
}
var yyTok2 = []int{

	2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
	12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
	22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
	32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
	42, 43, 44, 45, 51, 52, 53, 54, 56, 57,
	58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
	68, 69, 79, 80, 81, 82, 83, 84, 85, 86,
	87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
	97, 98, 99, 100,
}
var yyTok3 = []int{
	0,
}

//line yaccpar:1

/*	parser for yacc output	*/

var yyDebug = 0

type yyLexer interface {
	Lex(lval *yySymType) int
	Error(s string)
}

const yyFlag = -1000

func yyTokname(c int) string {
	// 4 is TOKSTART above
	if c >= 4 && c-4 < len(yyToknames) {
		if yyToknames[c-4] != "" {
			return yyToknames[c-4]
		}
	}
	return __yyfmt__.Sprintf("tok-%v", c)
}

func yyStatname(s int) string {
	if s >= 0 && s < len(yyStatenames) {
		if yyStatenames[s] != "" {
			return yyStatenames[s]
		}
	}
	return __yyfmt__.Sprintf("state-%v", s)
}

func yylex1(lex yyLexer, lval *yySymType) int {
	c := 0
	char := lex.Lex(lval)
	if char <= 0 {
		c = yyTok1[0]
		goto out
	}
	if char < len(yyTok1) {
		c = yyTok1[char]
		goto out
	}
	if char >= yyPrivate {
		if char < yyPrivate+len(yyTok2) {
			c = yyTok2[char-yyPrivate]
			goto out
		}
	}
	for i := 0; i < len(yyTok3); i += 2 {
		c = yyTok3[i+0]
		if c == char {
			c = yyTok3[i+1]
			goto out
		}
	}

out:
	if c == 0 {
		c = yyTok2[1] /* unknown char */
	}
	if yyDebug >= 3 {
		__yyfmt__.Printf("lex %s(%d)\n", yyTokname(c), uint(char))
	}
	return c
}

func yyParse(yylex yyLexer) int {
	var yyn int
	var yylval yySymType
	var yyVAL yySymType
	yyS := make([]yySymType, yyMaxDepth)

	Nerrs := 0   /* number of errors */
	Errflag := 0 /* error recovery flag */
	yystate := 0
	yychar := -1
	yyp := -1
	goto yystack

ret0:
	return 0

ret1:
	return 1

yystack:
	/* put a state and value onto the stack */
	if yyDebug >= 4 {
		__yyfmt__.Printf("char %v in %v\n", yyTokname(yychar), yyStatname(yystate))
	}

	yyp++
	if yyp >= len(yyS) {
		nyys := make([]yySymType, len(yyS)*2)
		copy(nyys, yyS)
		yyS = nyys
	}
	yyS[yyp] = yyVAL
	yyS[yyp].yys = yystate

yynewstate:
	yyn = yyPact[yystate]
	if yyn <= yyFlag {
		goto yydefault /* simple state */
	}
	if yychar < 0 {
		yychar = yylex1(yylex, &yylval)
	}
	yyn += yychar
	if yyn < 0 || yyn >= yyLast {
		goto yydefault
	}
	yyn = yyAct[yyn]
	if yyChk[yyn] == yychar { /* valid shift */
		yychar = -1
		yyVAL = yylval
		yystate = yyn
		if Errflag > 0 {
			Errflag--
		}
		goto yystack
	}

yydefault:
	/* default state action */
	yyn = yyDef[yystate]
	if yyn == -2 {
		if yychar < 0 {
			yychar = yylex1(yylex, &yylval)
		}

		/* look through exception table */
		xi := 0
		for {
			if yyExca[xi+0] == -1 && yyExca[xi+1] == yystate {
				break
			}
			xi += 2
		}
		for xi += 2; ; xi += 2 {
			yyn = yyExca[xi+0]
			if yyn < 0 || yyn == yychar {
				break
			}
		}
		yyn = yyExca[xi+1]
		if yyn < 0 {
			goto ret0
		}
	}
	if yyn == 0 {
		/* error ... attempt to resume parsing */
		switch Errflag {
		case 0: /* brand new error */
			yylex.Error("syntax error")
			Nerrs++
			if yyDebug >= 1 {
				__yyfmt__.Printf("%s", yyStatname(yystate))
				__yyfmt__.Printf(" saw %s\n", yyTokname(yychar))
			}
			fallthrough

		case 1, 2: /* incompletely recovered error ... try again */
			Errflag = 3

			/* find a state where "error" is a legal shift action */
			for yyp >= 0 {
				yyn = yyPact[yyS[yyp].yys] + yyErrCode
				if yyn >= 0 && yyn < yyLast {
					yystate = yyAct[yyn] /* simulate a shift of "error" */
					if yyChk[yystate] == yyErrCode {
						goto yystack
					}
				}

				/* the current p has no shift on "error", pop stack */
				if yyDebug >= 2 {
					__yyfmt__.Printf("error recovery pops state %d\n", yyS[yyp].yys)
				}
				yyp--
			}
			/* there is no state on the stack with an error shift ... abort */
			goto ret1

		case 3: /* no shift yet; clobber input char */
			if yyDebug >= 2 {
				__yyfmt__.Printf("error recovery discards %s\n", yyTokname(yychar))
			}
			if yychar == yyEofCode {
				goto ret1
			}
			yychar = -1
			goto yynewstate /* try again in the same state */
		}
	}

	/* reduction by production yyn */
	if yyDebug >= 2 {
		__yyfmt__.Printf("reduce %v in:\n\t%v\n", yyn, yyStatname(yystate))
	}

	yynt := yyn
	yypt := yyp
	_ = yypt // guard against "declared and not used"

	yyp -= yyR2[yyn]
	yyVAL = yyS[yyp+1]

	/* consult goto table to find next state */
	yyn = yyR1[yyn]
	yyg := yyPgo[yyn]
	yyj := yyg + yyS[yyp].yys + 1

	if yyj >= yyLast {
		yystate = yyAct[yyg]
	} else {
		yystate = yyAct[yyj]
		if yyChk[yystate] != -yyn {
			yystate = yyAct[yyg]
		}
	}
	// dummy call; replaced with literal code
	switch yynt {

	case 1:
		//line sql.y:154
		{
			SetParseTree(yylex, yyS[yypt-0].statement)
		}
	case 2:
		//line sql.y:160
		{
			yyVAL.statement = yyS[yypt-0].selStmt
		}
	case 3:
		//line sql.y:164
		{
			yyVAL.statement = yyS[yypt-0].selStmt
		}
	case 4:
		yyVAL.statement = yyS[yypt-0].statement
	case 5:
		yyVAL.statement = yyS[yypt-0].statement
	case 6:
		yyVAL.statement = yyS[yypt-0].statement
	case 7:
		yyVAL.statement = yyS[yypt-0].statement
	case 8:
		yyVAL.statement = yyS[yypt-0].statement
	case 9:
		yyVAL.statement = yyS[yypt-0].statement
	case 10:
		yyVAL.statement = yyS[yypt-0].statement
	case 11:
		yyVAL.statement = yyS[yypt-0].statement
	case 12:
		yyVAL.statement = yyS[yypt-0].statement
	case 13:
		yyVAL.statement = yyS[yypt-0].statement
	case 14:
		//line sql.y:180
		{
			yyVAL.selStmt = &Select{Comments: nil, Distinct: yyS[yypt-8].str, SelectExprs: yyS[yypt-7].selectExprs, From: NewFrom(AST_FROM, yyS[yypt-6].tableExprs), Where: NewWhere(AST_WHERE, yyS[yypt-5].boolExpr), GroupBy: GroupBy(yyS[yypt-4].valExprs), Having: NewWhere(AST_HAVING, yyS[yypt-3].boolExpr), OrderBy: yyS[yypt-2].orderBy, Limit: yyS[yypt-1].limit, Lock: yyS[yypt-0].str}
		}
	case 15:
		//line sql.y:186
		{
			yyVAL.selStmt = &Select{Comments: Comments(yyS[yypt-9].bytes2), Distinct: yyS[yypt-8].str, SelectExprs: yyS[yypt-7].selectExprs, From: NewFrom(AST_FROM, yyS[yypt-6].tableExprs), Where: NewWhere(AST_WHERE, yyS[yypt-5].boolExpr), GroupBy: GroupBy(yyS[yypt-4].valExprs), Having: NewWhere(AST_HAVING, yyS[yypt-3].boolExpr), OrderBy: yyS[yypt-2].orderBy, Limit: yyS[yypt-1].limit, Lock: yyS[yypt-0].str}
		}
	case 16:
		//line sql.y:190
		{
			yyVAL.selStmt = &Union{Type: yyS[yypt-1].str, Left: yyS[yypt-2].selStmt, Right: yyS[yypt-0].selStmt}
		}
	case 17:
		//line sql.y:196
		{
			yyVAL.statement = &Insert{Comments: Comments(yyS[yypt-5].bytes2), Table: yyS[yypt-3].tableName, Columns: yyS[yypt-2].columns, Rows: yyS[yypt-1].insRows, OnDup: OnDup(yyS[yypt-0].updateExprs)}
		}
	case 18:
		//line sql.y:200
		{
			cols := make(Columns, 0, len(yyS[yypt-1].updateExprs))
			vals := make(ValTuple, 0, len(yyS[yypt-1].updateExprs))
			for _, col := range yyS[yypt-1].updateExprs {
				cols = append(cols, &NonStarExpr{Expr: col.Name})
				vals = append(vals, col.Expr)
			}
			yyVAL.statement = &Insert{Comments: Comments(yyS[yypt-5].bytes2), Table: yyS[yypt-3].tableName, Columns: cols, Rows: Values{vals}, OnDup: OnDup(yyS[yypt-0].updateExprs)}
		}
	case 19:
		//line sql.y:212
		{
			yyVAL.statement = &Update{Comments: Comments(yyS[yypt-6].bytes2), Table: yyS[yypt-5].tableName, Exprs: yyS[yypt-3].updateExprs, Where: NewWhere(AST_WHERE, yyS[yypt-2].boolExpr), OrderBy: yyS[yypt-1].orderBy, Limit: yyS[yypt-0].limit}
		}
	case 20:
		//line sql.y:218
		{
			yyVAL.statement = &Delete{Comments: Comments(yyS[yypt-5].bytes2), Table: yyS[yypt-3].tableName, Where: NewWhere(AST_WHERE, yyS[yypt-2].boolExpr), OrderBy: yyS[yypt-1].orderBy, Limit: yyS[yypt-0].limit}
		}
	case 21:
		//line sql.y:224
		{
			yyVAL.statement = &Set{Comments: Comments(yyS[yypt-1].bytes2), Exprs: yyS[yypt-0].updateExprs}
		}
	case 22:
		//line sql.y:230
		{
			yyVAL.statement = &DDL{Action: AST_CREATE, NewName: yyS[yypt-1].bytes}
		}
	case 23:
		//line sql.y:234
		{
			// Change this to an alter statement
			yyVAL.statement = &DDL{Action: AST_ALTER, Table: yyS[yypt-1].bytes, NewName: yyS[yypt-1].bytes}
		}
	case 24:
		//line sql.y:239
		{
			yyVAL.statement = &DDL{Action: AST_CREATE, NewName: yyS[yypt-1].bytes}
		}
	case 25:
		//line sql.y:245
		{
			yyVAL.statement = &DDL{Action: AST_ALTER, Table: yyS[yypt-2].bytes, NewName: yyS[yypt-2].bytes}
		}
	case 26:
		//line sql.y:249
		{
			// Change this to a rename statement
			yyVAL.statement = &DDL{Action: AST_RENAME, Table: yyS[yypt-3].bytes, NewName: yyS[yypt-0].bytes}
		}
	case 27:
		//line sql.y:254
		{
			yyVAL.statement = &DDL{Action: AST_ALTER, Table: yyS[yypt-1].bytes, NewName: yyS[yypt-1].bytes}
		}
	case 28:
		//line sql.y:260
		{
			yyVAL.statement = &DDL{Action: AST_RENAME, Table: yyS[yypt-2].bytes, NewName: yyS[yypt-0].bytes}
		}
	case 29:
		//line sql.y:266
		{
			yyVAL.statement = &DDL{Action: AST_DROP, Table: yyS[yypt-0].bytes}
		}
	case 30:
		//line sql.y:270
		{
			// Change this to an alter statement
			yyVAL.statement = &DDL{Action: AST_ALTER, Table: yyS[yypt-0].bytes, NewName: yyS[yypt-0].bytes}
		}
	case 31:
		//line sql.y:275
		{
			yyVAL.statement = &DDL{Action: AST_DROP, Table: yyS[yypt-1].bytes}
		}
	case 32:
		//line sql.y:281
		{
			yyVAL.statement = &DDL{Action: AST_ALTER, Table: yyS[yypt-0].bytes, NewName: yyS[yypt-0].bytes}
		}
	case 33:
		//line sql.y:287
		{
			yyVAL.statement = &Other{}
		}
	case 34:
		//line sql.y:291
		{
			yyVAL.statement = &Other{}
		}
	case 35:
		//line sql.y:295
		{
			yyVAL.statement = &Other{}
		}
	case 36:
		//line sql.y:300
		{
			SetAllowComments(yylex, true)
		}
	case 37:
		//line sql.y:304
		{
			yyVAL.bytes2 = yyS[yypt-0].bytes2
			SetAllowComments(yylex, false)
		}
	case 38:
		//line sql.y:310
		{
			yyVAL.bytes2 = nil
		}
	case 39:
		//line sql.y:314
		{
			yyVAL.bytes2 = append(yyS[yypt-1].bytes2, yyS[yypt-0].bytes)
		}
	case 40:
		//line sql.y:320
		{
			yyVAL.str = AST_UNION
		}
	case 41:
		//line sql.y:324
		{
			yyVAL.str = AST_UNION_ALL
		}
	case 42:
		//line sql.y:328
		{
			yyVAL.str = AST_SET_MINUS
		}
	case 43:
		//line sql.y:332
		{
			yyVAL.str = AST_EXCEPT
		}
	case 44:
		//line sql.y:336
		{
			yyVAL.str = AST_INTERSECT
		}
	case 45:
		//line sql.y:341
		{
			yyVAL.str = ""
		}
	case 46:
		//line sql.y:345
		{
			yyVAL.str = AST_DISTINCT
		}
	case 47:
		//line sql.y:351
		{
			yyVAL.selectExprs = SelectExprs{yyS[yypt-0].selectExpr}
		}
	case 48:
		//line sql.y:355
		{
			yyVAL.selectExprs = append(yyVAL.selectExprs, yyS[yypt-0].selectExpr)
		}
	case 49:
		//line sql.y:361
		{
			yyVAL.selectExpr = &StarExpr{}
		}
	case 50:
		//line sql.y:365
		{
			yyVAL.selectExpr = &NonStarExpr{Expr: yyS[yypt-1].expr, As: yyS[yypt-0].bytes}
		}
	case 51:
		//line sql.y:369
		{
			yyVAL.selectExpr = &StarExpr{TableName: yyS[yypt-2].bytes}
		}
	case 52:
		//line sql.y:375
		{
			yyVAL.expr = yyS[yypt-0].boolExpr
		}
	case 53:
		//line sql.y:379
		{
			yyVAL.expr = yyS[yypt-0].valExpr
		}
	case 54:
		//line sql.y:384
		{
			yyVAL.bytes = nil
		}
	case 55:
		//line sql.y:388
		{
			yyVAL.bytes = yyS[yypt-0].bytes
		}
	case 56:
		//line sql.y:392
		{
			yyVAL.bytes = yyS[yypt-0].bytes
		}
	case 57:
		//line sql.y:398
		{
			yyVAL.tableExprs = TableExprs{yyS[yypt-0].tableExpr}
		}
	case 58:
		//line sql.y:402
		{
			yyVAL.tableExprs = append(yyVAL.tableExprs, yyS[yypt-0].tableExpr)
		}
	case 59:
		//line sql.y:408
		{
			yyVAL.tableExpr = &AliasedTableExpr{Expr: yyS[yypt-2].smTableExpr, As: yyS[yypt-1].bytes, Hints: yyS[yypt-0].indexHints}
		}
	case 60:
		//line sql.y:412
		{
			yyVAL.tableExpr = &ParenTableExpr{Expr: yyS[yypt-1].tableExpr}
		}
	case 61:
		//line sql.y:416
		{
			yyVAL.tableExpr = &JoinTableExpr{LeftExpr: yyS[yypt-2].tableExpr, Join: yyS[yypt-1].str, RightExpr: yyS[yypt-0].tableExpr}
		}
	case 62:
		//line sql.y:420
		{
			yyVAL.tableExpr = &JoinTableExpr{LeftExpr: yyS[yypt-4].tableExpr, Join: yyS[yypt-3].str, RightExpr: yyS[yypt-2].tableExpr, On: yyS[yypt-0].boolExpr}
		}
	case 63:
		//line sql.y:425
		{
			yyVAL.bytes = nil
		}
	case 64:
		//line sql.y:429
		{
			yyVAL.bytes = yyS[yypt-0].bytes
		}
	case 65:
		//line sql.y:433
		{
			yyVAL.bytes = yyS[yypt-0].bytes
		}
	case 66:
		//line sql.y:439
		{
			yyVAL.str = AST_JOIN
		}
	case 67:
		//line sql.y:443
		{
			yyVAL.str = AST_STRAIGHT_JOIN
		}
	case 68:
		//line sql.y:447
		{
			yyVAL.str = AST_LEFT_JOIN
		}
	case 69:
		//line sql.y:451
		{
			yyVAL.str = AST_LEFT_JOIN
		}
	case 70:
		//line sql.y:455
		{
			yyVAL.str = AST_RIGHT_JOIN
		}
	case 71:
		//line sql.y:459
		{
			yyVAL.str = AST_RIGHT_JOIN
		}
	case 72:
		//line sql.y:463
		{
			yyVAL.str = AST_JOIN
		}
	case 73:
		//line sql.y:467
		{
			yyVAL.str = AST_CROSS_JOIN
		}
	case 74:
		//line sql.y:471
		{
			yyVAL.str = AST_NATURAL_JOIN
		}
	case 75:
		//line sql.y:477
		{
			yyVAL.smTableExpr = &TableName{Name: yyS[yypt-0].bytes}
		}
	case 76:
		//line sql.y:481
		{
			yyVAL.smTableExpr = &TableName{Qualifier: yyS[yypt-2].bytes, Name: yyS[yypt-0].bytes}
		}
	case 77:
		//line sql.y:485
		{
			yyVAL.smTableExpr = yyS[yypt-0].subquery
		}
	case 78:
		//line sql.y:491
		{
			yyVAL.tableName = &TableName{Name: yyS[yypt-0].bytes}
		}
	case 79:
		//line sql.y:495
		{
			yyVAL.tableName = &TableName{Qualifier: yyS[yypt-2].bytes, Name: yyS[yypt-0].bytes}
		}
	case 80:
		//line sql.y:500
		{
			yyVAL.indexHints = nil
		}
	case 81:
		//line sql.y:504
		{
			yyVAL.indexHints = &IndexHints{Type: AST_USE, Indexes: yyS[yypt-1].bytes2}
		}
	case 82:
		//line sql.y:508
		{
			yyVAL.indexHints = &IndexHints{Type: AST_IGNORE, Indexes: yyS[yypt-1].bytes2}
		}
	case 83:
		//line sql.y:512
		{
			yyVAL.indexHints = &IndexHints{Type: AST_FORCE, Indexes: yyS[yypt-1].bytes2}
		}
	case 84:
		//line sql.y:518
		{
			yyVAL.bytes2 = [][]byte{yyS[yypt-0].bytes}
		}
	case 85:
		//line sql.y:522
		{
			yyVAL.bytes2 = append(yyS[yypt-2].bytes2, yyS[yypt-0].bytes)
		}
	case 86:
		//line sql.y:527
		{
			yyVAL.tableExprs = nil
		}
	case 87:
		//line sql.y:531
		{
			yyVAL.tableExprs = yyS[yypt-0].tableExprs
		}
	case 88:
		//line sql.y:537
		{
			yyVAL.boolExpr = nil
		}
	case 89:
		//line sql.y:541
		{
			yyVAL.boolExpr = yyS[yypt-0].boolExpr
		}
	case 90:
		yyVAL.boolExpr = yyS[yypt-0].boolExpr
	case 91:
		//line sql.y:548
		{
			yyVAL.boolExpr = &AndExpr{Left: yyS[yypt-2].boolExpr, Right: yyS[yypt-0].boolExpr}
		}
	case 92:
		//line sql.y:552
		{
			yyVAL.boolExpr = &OrExpr{Left: yyS[yypt-2].boolExpr, Right: yyS[yypt-0].boolExpr}
		}
	case 93:
		//line sql.y:556
		{
			yyVAL.boolExpr = &NotExpr{Expr: yyS[yypt-0].boolExpr}
		}
	case 94:
		//line sql.y:560
		{
			yyVAL.boolExpr = &ParenBoolExpr{Expr: yyS[yypt-1].boolExpr}
		}
	case 95:
		//line sql.y:566
		{
			yyVAL.boolExpr = &ComparisonExpr{Left: yyS[yypt-2].valExpr, Operator: yyS[yypt-1].str, Right: yyS[yypt-0].valExpr}
		}
	case 96:
		//line sql.y:570
		{
			yyVAL.boolExpr = &ComparisonExpr{Left: yyS[yypt-2].valExpr, Operator: AST_IN, Right: yyS[yypt-0].colTuple}
		}
	case 97:
		//line sql.y:574
		{
			yyVAL.boolExpr = &ComparisonExpr{Left: yyS[yypt-3].valExpr, Operator: AST_NOT_IN, Right: yyS[yypt-0].colTuple}
		}
	case 98:
		//line sql.y:578
		{
			yyVAL.boolExpr = &ComparisonExpr{Left: yyS[yypt-2].valExpr, Operator: AST_LIKE, Right: yyS[yypt-0].valExpr}
		}
	case 99:
		//line sql.y:582
		{
			yyVAL.boolExpr = &ComparisonExpr{Left: yyS[yypt-3].valExpr, Operator: AST_NOT_LIKE, Right: yyS[yypt-0].valExpr}
		}
	case 100:
		//line sql.y:586
		{
			yyVAL.boolExpr = &RangeCond{Left: yyS[yypt-4].valExpr, Operator: AST_BETWEEN, From: yyS[yypt-2].valExpr, To: yyS[yypt-0].valExpr}
		}
	case 101:
		//line sql.y:590
		{
			yyVAL.boolExpr = &RangeCond{Left: yyS[yypt-5].valExpr, Operator: AST_NOT_BETWEEN, From: yyS[yypt-2].valExpr, To: yyS[yypt-0].valExpr}
		}
	case 102:
		//line sql.y:594
		{
			yyVAL.boolExpr = &NullCheck{Operator: AST_IS_NULL, Expr: yyS[yypt-2].valExpr}
		}
	case 103:
		//line sql.y:598
		{
			yyVAL.boolExpr = &NullCheck{Operator: AST_IS_NOT_NULL, Expr: yyS[yypt-3].valExpr}
		}
	case 104:
		//line sql.y:602
		{
			yyVAL.boolExpr = &ExistsExpr{Subquery: yyS[yypt-0].subquery}
		}
	case 105:
		//line sql.y:606
		{
			yyVAL.boolExpr = &KeyrangeExpr{Start: yyS[yypt-3].valExpr, End: yyS[yypt-1].valExpr}
		}
	case 106:
		//line sql.y:612
		{
			yyVAL.str = AST_EQ
		}
	case 107:
		//line sql.y:616
		{
			yyVAL.str = AST_LT
		}
	case 108:
		//line sql.y:620
		{
			yyVAL.str = AST_GT
		}
	case 109:
		//line sql.y:624
		{
			yyVAL.str = AST_LE
		}
	case 110:
		//line sql.y:628
		{
			yyVAL.str = AST_GE
		}
	case 111:
		//line sql.y:632
		{
			yyVAL.str = AST_NE
		}
	case 112:
		//line sql.y:636
		{
			yyVAL.str = AST_NSE
		}
	case 113:
		//line sql.y:642
		{
			yyVAL.colTuple = ValTuple(yyS[yypt-1].valExprs)
		}
	case 114:
		//line sql.y:646
		{
			yyVAL.colTuple = yyS[yypt-0].subquery
		}
	case 115:
		//line sql.y:650
		{
			yyVAL.colTuple = ListArg(yyS[yypt-0].bytes)
		}
	case 116:
		//line sql.y:656
		{
			yyVAL.subquery = &Subquery{yyS[yypt-1].selStmt}
		}
	case 117:
		//line sql.y:662
		{
			yyVAL.valExprs = ValExprs{yyS[yypt-0].valExpr}
		}
	case 118:
		//line sql.y:666
		{
			yyVAL.valExprs = append(yyS[yypt-2].valExprs, yyS[yypt-0].valExpr)
		}
	case 119:
		//line sql.y:672
		{
			yyVAL.valExpr = yyS[yypt-0].valExpr
		}
	case 120:
		//line sql.y:676
		{
			yyVAL.valExpr = yyS[yypt-0].colName
		}
	case 121:
		//line sql.y:680
		{
			yyVAL.valExpr = yyS[yypt-0].rowTuple
		}
	case 122:
		//line sql.y:684
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_BITAND, Right: yyS[yypt-0].valExpr}
		}
	case 123:
		//line sql.y:688
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_BITOR, Right: yyS[yypt-0].valExpr}
		}
	case 124:
		//line sql.y:692
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_BITXOR, Right: yyS[yypt-0].valExpr}
		}
	case 125:
		//line sql.y:696
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_PLUS, Right: yyS[yypt-0].valExpr}
		}
	case 126:
		//line sql.y:700
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_MINUS, Right: yyS[yypt-0].valExpr}
		}
	case 127:
		//line sql.y:704
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_MULT, Right: yyS[yypt-0].valExpr}
		}
	case 128:
		//line sql.y:708
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_DIV, Right: yyS[yypt-0].valExpr}
		}
	case 129:
		//line sql.y:712
		{
			yyVAL.valExpr = &BinaryExpr{Left: yyS[yypt-2].valExpr, Operator: AST_MOD, Right: yyS[yypt-0].valExpr}
		}
	case 130:
		//line sql.y:716
		{
			if num, ok := yyS[yypt-0].valExpr.(NumVal); ok {
				switch yyS[yypt-1].byt {
				case '-':
					yyVAL.valExpr = append(NumVal("-"), num...)
				case '+':
					yyVAL.valExpr = num
				default:
					yyVAL.valExpr = &UnaryExpr{Operator: yyS[yypt-1].byt, Expr: yyS[yypt-0].valExpr}
				}
			} else {
				yyVAL.valExpr = &UnaryExpr{Operator: yyS[yypt-1].byt, Expr: yyS[yypt-0].valExpr}
			}
		}
	case 131:
		//line sql.y:731
		{
			yyVAL.valExpr = &FuncExpr{Name: yyS[yypt-2].bytes}
		}
	case 132:
		//line sql.y:735
		{
			yyVAL.valExpr = &FuncExpr{Name: yyS[yypt-3].bytes, Exprs: yyS[yypt-1].selectExprs}
		}
	case 133:
		//line sql.y:739
		{
			yyVAL.valExpr = &FuncExpr{Name: yyS[yypt-4].bytes, Distinct: true, Exprs: yyS[yypt-1].selectExprs}
		}
	case 134:
		//line sql.y:743
		{
			yyVAL.valExpr = &FuncExpr{Name: yyS[yypt-3].bytes, Exprs: yyS[yypt-1].selectExprs}
		}
	case 135:
		//line sql.y:747
		{
			yyVAL.valExpr = yyS[yypt-0].caseExpr
		}
	case 136:
		//line sql.y:753
		{
			yyVAL.bytes = IF_BYTES
		}
	case 137:
		//line sql.y:757
		{
			yyVAL.bytes = VALUES_BYTES
		}
	case 138:
		//line sql.y:763
		{
			yyVAL.byt = AST_UPLUS
		}
	case 139:
		//line sql.y:767
		{
			yyVAL.byt = AST_UMINUS
		}
	case 140:
		//line sql.y:771
		{
			yyVAL.byt = AST_TILDA
		}
	case 141:
		//line sql.y:777
		{
			yyVAL.caseExpr = &CaseExpr{Expr: yyS[yypt-3].valExpr, Whens: yyS[yypt-2].whens, Else: yyS[yypt-1].valExpr}
		}
	case 142:
		//line sql.y:782
		{
			yyVAL.valExpr = nil
		}
	case 143:
		//line sql.y:786
		{
			yyVAL.valExpr = yyS[yypt-0].valExpr
		}
	case 144:
		//line sql.y:792
		{
			yyVAL.whens = []*When{yyS[yypt-0].when}
		}
	case 145:
		//line sql.y:796
		{
			yyVAL.whens = append(yyS[yypt-1].whens, yyS[yypt-0].when)
		}
	case 146:
		//line sql.y:802
		{
			yyVAL.when = &When{Cond: yyS[yypt-2].boolExpr, Val: yyS[yypt-0].valExpr}
		}
	case 147:
		//line sql.y:807
		{
			yyVAL.valExpr = nil
		}
	case 148:
		//line sql.y:811
		{
			yyVAL.valExpr = yyS[yypt-0].valExpr
		}
	case 149:
		//line sql.y:817
		{
			yyVAL.colName = &ColName{Name: yyS[yypt-0].bytes}
		}
	case 150:
		//line sql.y:821
		{
			yyVAL.colName = &ColName{Qualifier: yyS[yypt-2].bytes, Name: yyS[yypt-0].bytes}
		}
	case 151:
		//line sql.y:827
		{
			yyVAL.valExpr = StrVal(yyS[yypt-0].bytes)
		}
	case 152:
		//line sql.y:831
		{
			yyVAL.valExpr = NumVal(yyS[yypt-0].bytes)
		}
	case 153:
		//line sql.y:835
		{
			yyVAL.valExpr = ValArg(yyS[yypt-0].bytes)
		}
	case 154:
		//line sql.y:839
		{
			yyVAL.valExpr = &NullVal{}
		}
	case 155:
		//line sql.y:844
		{
			yyVAL.valExprs = nil
		}
	case 156:
		//line sql.y:848
		{
			yyVAL.valExprs = yyS[yypt-0].valExprs
		}
	case 157:
		//line sql.y:853
		{
			yyVAL.boolExpr = nil
		}
	case 158:
		//line sql.y:857
		{
			yyVAL.boolExpr = yyS[yypt-0].boolExpr
		}
	case 159:
		//line sql.y:862
		{
			yyVAL.orderBy = nil
		}
	case 160:
		//line sql.y:866
		{
			yyVAL.orderBy = yyS[yypt-0].orderBy
		}
	case 161:
		//line sql.y:872
		{
			yyVAL.orderBy = OrderBy{yyS[yypt-0].order}
		}
	case 162:
		//line sql.y:876
		{
			yyVAL.orderBy = append(yyS[yypt-2].orderBy, yyS[yypt-0].order)
		}
	case 163:
		//line sql.y:882
		{
			yyVAL.order = &Order{Expr: yyS[yypt-1].valExpr, Direction: yyS[yypt-0].str}
		}
	case 164:
		//line sql.y:887
		{
			yyVAL.str = AST_ASC
		}
	case 165:
		//line sql.y:891
		{
			yyVAL.str = AST_ASC
		}
	case 166:
		//line sql.y:895
		{
			yyVAL.str = AST_DESC
		}
	case 167:
		//line sql.y:900
		{
			yyVAL.limit = nil
		}
	case 168:
		//line sql.y:904
		{
			yyVAL.limit = &Limit{Rowcount: yyS[yypt-0].valExpr}
		}
	case 169:
		//line sql.y:908
		{
			yyVAL.limit = &Limit{Offset: yyS[yypt-2].valExpr, Rowcount: yyS[yypt-0].valExpr}
		}
	case 170:
		//line sql.y:913
		{
			yyVAL.str = ""
		}
	case 171:
		//line sql.y:917
		{
			yyVAL.str = AST_FOR_UPDATE
		}
	case 172:
		//line sql.y:921
		{
			if !bytes.Equal(yyS[yypt-1].bytes, SHARE) {
				yylex.Error("expecting share")
				return 1
			}
			if !bytes.Equal(yyS[yypt-0].bytes, MODE) {
				yylex.Error("expecting mode")
				return 1
			}
			yyVAL.str = AST_SHARE_MODE
		}
	case 173:
		//line sql.y:934
		{
			yyVAL.columns = nil
		}
	case 174:
		//line sql.y:938
		{
			yyVAL.columns = yyS[yypt-1].columns
		}
	case 175:
		//line sql.y:944
		{
			yyVAL.columns = Columns{&NonStarExpr{Expr: yyS[yypt-0].colName}}
		}
	case 176:
		//line sql.y:948
		{
			yyVAL.columns = append(yyVAL.columns, &NonStarExpr{Expr: yyS[yypt-0].colName})
		}
	case 177:
		//line sql.y:953
		{
			yyVAL.updateExprs = nil
		}
	case 178:
		//line sql.y:957
		{
			yyVAL.updateExprs = yyS[yypt-0].updateExprs
		}
	case 179:
		//line sql.y:963
		{
			yyVAL.insRows = yyS[yypt-0].values
		}
	case 180:
		//line sql.y:967
		{
			yyVAL.insRows = yyS[yypt-0].selStmt
		}
	case 181:
		//line sql.y:973
		{
			yyVAL.values = Values{yyS[yypt-0].rowTuple}
		}
	case 182:
		//line sql.y:977
		{
			yyVAL.values = append(yyS[yypt-2].values, yyS[yypt-0].rowTuple)
		}
	case 183:
		//line sql.y:983
		{
			yyVAL.rowTuple = ValTuple(yyS[yypt-1].valExprs)
		}
	case 184:
		//line sql.y:987
		{
			yyVAL.rowTuple = yyS[yypt-0].subquery
		}
	case 185:
		//line sql.y:993
		{
			yyVAL.updateExprs = UpdateExprs{yyS[yypt-0].updateExpr}
		}
	case 186:
		//line sql.y:997
		{
			yyVAL.updateExprs = append(yyS[yypt-2].updateExprs, yyS[yypt-0].updateExpr)
		}
	case 187:
		//line sql.y:1003
		{
			yyVAL.updateExpr = &UpdateExpr{Name: yyS[yypt-2].colName, Expr: yyS[yypt-0].valExpr}
		}
	case 188:
		//line sql.y:1008
		{
			yyVAL.empty = struct{}{}
		}
	case 189:
		//line sql.y:1010
		{
			yyVAL.empty = struct{}{}
		}
	case 190:
		//line sql.y:1013
		{
			yyVAL.empty = struct{}{}
		}
	case 191:
		//line sql.y:1015
		{
			yyVAL.empty = struct{}{}
		}
	case 192:
		//line sql.y:1018
		{
			yyVAL.empty = struct{}{}
		}
	case 193:
		//line sql.y:1020
		{
			yyVAL.empty = struct{}{}
		}
	case 194:
		//line sql.y:1024
		{
			yyVAL.empty = struct{}{}
		}
	case 195:
		//line sql.y:1026
		{
			yyVAL.empty = struct{}{}
		}
	case 196:
		//line sql.y:1028
		{
			yyVAL.empty = struct{}{}
		}
	case 197:
		//line sql.y:1030
		{
			yyVAL.empty = struct{}{}
		}
	case 198:
		//line sql.y:1032
		{
			yyVAL.empty = struct{}{}
		}
	case 199:
		//line sql.y:1035
		{
			yyVAL.empty = struct{}{}
		}
	case 200:
		//line sql.y:1037
		{
			yyVAL.empty = struct{}{}
		}
	case 201:
		//line sql.y:1040
		{
			yyVAL.empty = struct{}{}
		}
	case 202:
		//line sql.y:1042
		{
			yyVAL.empty = struct{}{}
		}
	case 203:
		//line sql.y:1045
		{
			yyVAL.empty = struct{}{}
		}
	case 204:
		//line sql.y:1047
		{
			yyVAL.empty = struct{}{}
		}
	case 205:
		//line sql.y:1051
		{
			yyVAL.bytes = yyS[yypt-0].bytes
		}
	case 206:
		//line sql.y:1056
		{
			ForceEOF(yylex)
		}
	}
	goto yystack /* stack new state and value */
}
```

## File: `sqlparser/sql.y`
```
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

%{
package sqlparser

import "bytes"

func SetParseTree(yylex interface{}, stmt Statement) {
  yylex.(*Tokenizer).ParseTree = stmt
}

func SetAllowComments(yylex interface{}, allow bool) {
  yylex.(*Tokenizer).AllowComments = allow
}

func ForceEOF(yylex interface{}) {
  yylex.(*Tokenizer).ForceEOF = true
}

var (
  SHARE =        []byte("share")
  MODE  =        []byte("mode")
  IF_BYTES =     []byte("if")
  VALUES_BYTES = []byte("values")
)

%}

%union {
  empty       struct{}
  statement   Statement
  selStmt     SelectStatement
  byt         byte
  bytes       []byte
  bytes2      [][]byte
  str         string
  selectExprs SelectExprs
  selectExpr  SelectExpr
  columns     Columns
  colName     *ColName
  tableExprs  TableExprs
  tableExpr   TableExpr
  smTableExpr SimpleTableExpr
  tableName   *TableName
  indexHints  *IndexHints
  expr        Expr
  boolExpr    BoolExpr
  valExpr     ValExpr
  colTuple    ColTuple
  valExprs    ValExprs
  values      Values
  rowTuple    RowTuple
  subquery    *Subquery
  caseExpr    *CaseExpr
  whens       []*When
  when        *When
  orderBy     OrderBy
  order       *Order
  limit       *Limit
  insRows     InsertRows
  updateExprs UpdateExprs
  updateExpr  *UpdateExpr
}

%token LEX_ERROR
%token <empty> SELECT INSERT UPDATE DELETE FROM WHERE GROUP HAVING ORDER BY LIMIT FOR
%token <empty> ALL DISTINCT AS EXISTS IN IS LIKE BETWEEN NULL ASC DESC VALUES INTO DUPLICATE KEY DEFAULT SET LOCK KEYRANGE
%token <bytes> ID STRING NUMBER VALUE_ARG LIST_ARG COMMENT
%token <empty> LE GE NE NULL_SAFE_EQUAL
%token <empty> '(' '=' '<' '>' '~'

%left <empty> UNION MINUS EXCEPT INTERSECT
%left <empty> ','
%left <empty> JOIN STRAIGHT_JOIN LEFT RIGHT INNER OUTER CROSS NATURAL USE FORCE
%left <empty> ON
%left <empty> OR
%left <empty> AND
%right <empty> NOT
%left <empty> '&' '|' '^'
%left <empty> '+' '-'
%left <empty> '*' '/' '%'
%nonassoc <empty> '.'
%left <empty> UNARY
%right <empty> CASE, WHEN, THEN, ELSE
%left <empty> END

// DDL Tokens
%token <empty> CREATE ALTER DROP RENAME ANALYZE
%token <empty> TABLE INDEX VIEW TO IGNORE IF UNIQUE USING
%token <empty> SHOW DESCRIBE EXPLAIN

%start any_command

%type <statement> command
%type <selStmt> select_statement
%type <selStmt> missing_select_statement
%type <statement> insert_statement update_statement delete_statement set_statement
%type <statement> create_statement alter_statement rename_statement drop_statement
%type <statement> analyze_statement other_statement
%type <bytes2> comment_opt comment_list
%type <str> union_op
%type <str> distinct_opt
%type <selectExprs> select_expression_list
%type <selectExpr> select_expression
%type <bytes> as_lower_opt as_opt
%type <expr> expression
%type <tableExprs> table_expression_list
%type <tableExpr> table_expression
%type <tableExprs> from_expression_list_opt
%type <str> join_type
%type <smTableExpr> simple_table_expression
%type <tableName> dml_table_expression
%type <indexHints> index_hint_list
%type <bytes2> index_list
%type <boolExpr> where_expression_opt
%type <boolExpr> boolean_expression condition
%type <str> compare
%type <insRows> row_list
%type <valExpr> value value_expression
%type <colTuple> col_tuple
%type <valExprs> value_expression_list
%type <values> tuple_list
%type <rowTuple> row_tuple
%type <bytes> keyword_as_func
%type <subquery> subquery
%type <byt> unary_operator
%type <colName> column_name
%type <caseExpr> case_expression
%type <whens> when_expression_list
%type <when> when_expression
%type <valExpr> value_expression_opt else_expression_opt
%type <valExprs> group_by_opt
%type <boolExpr> having_opt
%type <orderBy> order_by_opt order_list
%type <order> order
%type <str> asc_desc_opt
%type <limit> limit_opt
%type <str> lock_opt
%type <columns> column_list_opt column_list
%type <updateExprs> on_dup_opt
%type <updateExprs> update_list
%type <updateExpr> update_expression
%type <empty> exists_opt not_exists_opt ignore_opt non_rename_operation to_opt constraint_opt using_opt
%type <bytes> sql_id
%type <empty> force_eof


%%

any_command:
  command
  {
    SetParseTree(yylex, $1)
  }

command:
  select_statement
  {
    $$ = $1
  }
| missing_select_statement
  {
    $$ = $1
  }
| insert_statement
| update_statement
| delete_statement
| set_statement
| create_statement
| alter_statement
| rename_statement
| drop_statement
| analyze_statement
| other_statement

missing_select_statement:
  distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt
  {
    $$ = &Select{Comments: nil, Distinct: $1, SelectExprs: $2, From: NewFrom(AST_FROM, $3), Where: NewWhere(AST_WHERE, $4), GroupBy: GroupBy($5), Having: NewWhere(AST_HAVING, $6), OrderBy: $7, Limit: $8, Lock: $9}
  }

select_statement:
  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt
  {
    $$ = &Select{Comments: Comments($2), Distinct: $3, SelectExprs: $4, From: NewFrom(AST_FROM, $5), Where: NewWhere(AST_WHERE, $6), GroupBy: GroupBy($7), Having: NewWhere(AST_HAVING, $8), OrderBy: $9, Limit: $10, Lock: $11}
  }
| select_statement union_op select_statement %prec UNION
  {
    $$ = &Union{Type: $2, Left: $1, Right: $3}
  }

insert_statement:
  INSERT comment_opt INTO dml_table_expression column_list_opt row_list on_dup_opt
  {
    $$ = &Insert{Comments: Comments($2), Table: $4, Columns: $5, Rows: $6, OnDup: OnDup($7)}
  }
| INSERT comment_opt INTO dml_table_expression SET update_list on_dup_opt
  {
    cols := make(Columns, 0, len($6))
    vals := make(ValTuple, 0, len($6))
    for _, col := range $6 {
      cols = append(cols, &NonStarExpr{Expr: col.Name})
      vals = append(vals, col.Expr)
    }
    $$ = &Insert{Comments: Comments($2), Table: $4, Columns: cols, Rows: Values{vals}, OnDup: OnDup($7)}
  }

update_statement:
  UPDATE comment_opt dml_table_expression SET update_list where_expression_opt order_by_opt limit_opt
  {
    $$ = &Update{Comments: Comments($2), Table: $3, Exprs: $5, Where: NewWhere(AST_WHERE, $6), OrderBy: $7, Limit: $8}
  }

delete_statement:
  DELETE comment_opt FROM dml_table_expression where_expression_opt order_by_opt limit_opt
  {
    $$ = &Delete{Comments: Comments($2), Table: $4, Where: NewWhere(AST_WHERE, $5), OrderBy: $6, Limit: $7}
  }

set_statement:
  SET comment_opt update_list
  {
    $$ = &Set{Comments: Comments($2), Exprs: $3}
  }

create_statement:
  CREATE TABLE not_exists_opt ID force_eof
  {
    $$ = &DDL{Action: AST_CREATE, NewName: $4}
  }
| CREATE constraint_opt INDEX sql_id using_opt ON ID force_eof
  {
    // Change this to an alter statement
    $$ = &DDL{Action: AST_ALTER, Table: $7, NewName: $7}
  }
| CREATE VIEW sql_id force_eof
  {
    $$ = &DDL{Action: AST_CREATE, NewName: $3}
  }

alter_statement:
  ALTER ignore_opt TABLE ID non_rename_operation force_eof
  {
    $$ = &DDL{Action: AST_ALTER, Table: $4, NewName: $4}
  }
| ALTER ignore_opt TABLE ID RENAME to_opt ID
  {
    // Change this to a rename statement
    $$ = &DDL{Action: AST_RENAME, Table: $4, NewName: $7}
  }
| ALTER VIEW sql_id force_eof
  {
    $$ = &DDL{Action: AST_ALTER, Table: $3, NewName: $3}
  }

rename_statement:
  RENAME TABLE ID TO ID
  {
    $$ = &DDL{Action: AST_RENAME, Table: $3, NewName: $5}
  }

drop_statement:
  DROP TABLE exists_opt ID
  {
    $$ = &DDL{Action: AST_DROP, Table: $4}
  }
| DROP INDEX sql_id ON ID
  {
    // Change this to an alter statement
    $$ = &DDL{Action: AST_ALTER, Table: $5, NewName: $5}
  }
| DROP VIEW exists_opt sql_id force_eof
  {
    $$ = &DDL{Action: AST_DROP, Table: $4}
  }

analyze_statement:
  ANALYZE TABLE ID
  {
    $$ = &DDL{Action: AST_ALTER, Table: $3, NewName: $3}
  }

other_statement:
  SHOW force_eof
  {
    $$ = &Other{}
  }
| DESCRIBE force_eof
  {
    $$ = &Other{}
  }
| EXPLAIN force_eof
  {
    $$ = &Other{}
  }

comment_opt:
  {
    SetAllowComments(yylex, true)
  }
  comment_list
  {
    $$ = $2
    SetAllowComments(yylex, false)
  }

comment_list:
  {
    $$ = nil
  }
| comment_list COMMENT
  {
    $$ = append($1, $2)
  }

union_op:
  UNION
  {
    $$ = AST_UNION
  }
| UNION ALL
  {
    $$ = AST_UNION_ALL
  }
| MINUS
  {
    $$ = AST_SET_MINUS
  }
| EXCEPT
  {
    $$ = AST_EXCEPT
  }
| INTERSECT
  {
    $$ = AST_INTERSECT
  }

distinct_opt:
  {
    $$ = ""
  }
| DISTINCT
  {
    $$ = AST_DISTINCT
  }

select_expression_list:
  select_expression
  {
    $$ = SelectExprs{$1}
  }
| select_expression_list ',' select_expression
  {
    $$ = append($$, $3)
  }

select_expression:
  '*'
  {
    $$ = &StarExpr{}
  }
| expression as_lower_opt
  {
    $$ = &NonStarExpr{Expr: $1, As: $2}
  }
| ID '.' '*'
  {
    $$ = &StarExpr{TableName: $1}
  }

expression:
  boolean_expression
  {
    $$ = $1
  }
| value_expression
  {
    $$ = $1
  }

as_lower_opt:
  {
    $$ = nil
  }
| sql_id
  {
    $$ = $1
  }
| AS sql_id
  {
    $$ = $2
  }

table_expression_list:
  table_expression
  {
    $$ = TableExprs{$1}
  }
| table_expression_list ',' table_expression
  {
    $$ = append($$, $3)
  }

table_expression:
  simple_table_expression as_opt index_hint_list
  {
    $$ = &AliasedTableExpr{Expr:$1, As: $2, Hints: $3}
  }
| '(' table_expression ')'
  {
    $$ = &ParenTableExpr{Expr: $2}
  }
| table_expression join_type table_expression %prec JOIN
  {
    $$ = &JoinTableExpr{LeftExpr: $1, Join: $2, RightExpr: $3}
  }
| table_expression join_type table_expression ON boolean_expression %prec JOIN
  {
    $$ = &JoinTableExpr{LeftExpr: $1, Join: $2, RightExpr: $3, On: $5}
  }

as_opt:
  {
    $$ = nil
  }
| ID
  {
    $$ = $1
  }
| AS ID
  {
    $$ = $2
  }

join_type:
  JOIN
  {
    $$ = AST_JOIN
  }
| STRAIGHT_JOIN
  {
    $$ = AST_STRAIGHT_JOIN
  }
| LEFT JOIN
  {
    $$ = AST_LEFT_JOIN
  }
| LEFT OUTER JOIN
  {
    $$ = AST_LEFT_JOIN
  }
| RIGHT JOIN
  {
    $$ = AST_RIGHT_JOIN
  }
| RIGHT OUTER JOIN
  {
    $$ = AST_RIGHT_JOIN
  }
| INNER JOIN
  {
    $$ = AST_JOIN
  }
| CROSS JOIN
  {
    $$ = AST_CROSS_JOIN
  }
| NATURAL JOIN
  {
    $$ = AST_NATURAL_JOIN
  }

simple_table_expression:
ID
  {
    $$ = &TableName{Name: $1}
  }
| ID '.' ID
  {
    $$ = &TableName{Qualifier: $1, Name: $3}
  }
| subquery
  {
    $$ = $1
  }

dml_table_expression:
ID
  {
    $$ = &TableName{Name: $1}
  }
| ID '.' ID
  {
    $$ = &TableName{Qualifier: $1, Name: $3}
  }

index_hint_list:
  {
    $$ = nil
  }
| USE INDEX '(' index_list ')'
  {
    $$ = &IndexHints{Type: AST_USE, Indexes: $4}
  }
| IGNORE INDEX '(' index_list ')'
  {
    $$ = &IndexHints{Type: AST_IGNORE, Indexes: $4}
  }
| FORCE INDEX '(' index_list ')'
  {
    $$ = &IndexHints{Type: AST_FORCE, Indexes: $4}
  }

index_list:
  sql_id
  {
    $$ = [][]byte{$1}
  }
| index_list ',' sql_id
  {
    $$ = append($1, $3)
  }

from_expression_list_opt:
  {
    $$ = nil
  }
| FROM table_expression_list
  {
    $$ = $2
  }


where_expression_opt:
  {
    $$ = nil
  }
| WHERE boolean_expression
  {
    $$ = $2
  }

boolean_expression:
  condition
| boolean_expression AND boolean_expression
  {
    $$ = &AndExpr{Left: $1, Right: $3}
  }
| boolean_expression OR boolean_expression
  {
    $$ = &OrExpr{Left: $1, Right: $3}
  }
| NOT boolean_expression
  {
    $$ = &NotExpr{Expr: $2}
  }
| '(' boolean_expression ')'
  {
    $$ = &ParenBoolExpr{Expr: $2}
  }

condition:
  value_expression compare value_expression
  {
    $$ = &ComparisonExpr{Left: $1, Operator: $2, Right: $3}
  }
| value_expression IN col_tuple
  {
    $$ = &ComparisonExpr{Left: $1, Operator: AST_IN, Right: $3}
  }
| value_expression NOT IN col_tuple
  {
    $$ = &ComparisonExpr{Left: $1, Operator: AST_NOT_IN, Right: $4}
  }
| value_expression LIKE value_expression
  {
    $$ = &ComparisonExpr{Left: $1, Operator: AST_LIKE, Right: $3}
  }
| value_expression NOT LIKE value_expression
  {
    $$ = &ComparisonExpr{Left: $1, Operator: AST_NOT_LIKE, Right: $4}
  }
| value_expression BETWEEN value_expression AND value_expression
  {
    $$ = &RangeCond{Left: $1, Operator: AST_BETWEEN, From: $3, To: $5}
  }
| value_expression NOT BETWEEN value_expression AND value_expression
  {
    $$ = &RangeCond{Left: $1, Operator: AST_NOT_BETWEEN, From: $4, To: $6}
  }
| value_expression IS NULL
  {
    $$ = &NullCheck{Operator: AST_IS_NULL, Expr: $1}
  }
| value_expression IS NOT NULL
  {
    $$ = &NullCheck{Operator: AST_IS_NOT_NULL, Expr: $1}
  }
| EXISTS subquery
  {
    $$ = &ExistsExpr{Subquery: $2}
  }
| KEYRANGE '(' value ',' value ')'
  {
    $$ = &KeyrangeExpr{Start: $3, End: $5}
  }

compare:
  '='
  {
    $$ = AST_EQ
  }
| '<'
  {
    $$ = AST_LT
  }
| '>'
  {
    $$ = AST_GT
  }
| LE
  {
    $$ = AST_LE
  }
| GE
  {
    $$ = AST_GE
  }
| NE
  {
    $$ = AST_NE
  }
| NULL_SAFE_EQUAL
  {
    $$ = AST_NSE
  }

col_tuple:
  '(' value_expression_list ')'
  {
    $$ = ValTuple($2)
  }
| subquery
  {
    $$ = $1
  }
| LIST_ARG
  {
    $$ = ListArg($1)
  }

subquery:
  '(' select_statement ')'
  {
    $$ = &Subquery{$2}
  }

value_expression_list:
  value_expression
  {
    $$ = ValExprs{$1}
  }
| value_expression_list ',' value_expression
  {
    $$ = append($1, $3)
  }

value_expression:
  value
  {
    $$ = $1
  }
| column_name
  {
    $$ = $1
  }
| row_tuple
  {
    $$ = $1
  }
| value_expression '&' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_BITAND, Right: $3}
  }
| value_expression '|' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_BITOR, Right: $3}
  }
| value_expression '^' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_BITXOR, Right: $3}
  }
| value_expression '+' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_PLUS, Right: $3}
  }
| value_expression '-' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_MINUS, Right: $3}
  }
| value_expression '*' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_MULT, Right: $3}
  }
| value_expression '/' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_DIV, Right: $3}
  }
| value_expression '%' value_expression
  {
    $$ = &BinaryExpr{Left: $1, Operator: AST_MOD, Right: $3}
  }
| unary_operator value_expression %prec UNARY
  {
    if num, ok := $2.(NumVal); ok {
      switch $1 {
      case '-':
        $$ = append(NumVal("-"), num...)
      case '+':
        $$ = num
      default:
        $$ = &UnaryExpr{Operator: $1, Expr: $2}
      }
    } else {
      $$ = &UnaryExpr{Operator: $1, Expr: $2}
    }
  }
| sql_id '(' ')'
  {
    $$ = &FuncExpr{Name: $1}
  }
| sql_id '(' select_expression_list ')'
  {
    $$ = &FuncExpr{Name: $1, Exprs: $3}
  }
| sql_id '(' DISTINCT select_expression_list ')'
  {
    $$ = &FuncExpr{Name: $1, Distinct: true, Exprs: $4}
  }
| keyword_as_func '(' select_expression_list ')'
  {
    $$ = &FuncExpr{Name: $1, Exprs: $3}
  }
| case_expression
  {
    $$ = $1
  }

keyword_as_func:
  IF
  {
    $$ = IF_BYTES
  }
| VALUES
  {
    $$ = VALUES_BYTES
  }

unary_operator:
  '+'
  {
    $$ = AST_UPLUS
  }
| '-'
  {
    $$ = AST_UMINUS
  }
| '~'
  {
    $$ = AST_TILDA
  }

case_expression:
  CASE value_expression_opt when_expression_list else_expression_opt END
  {
    $$ = &CaseExpr{Expr: $2, Whens: $3, Else: $4}
  }

value_expression_opt:
  {
    $$ = nil
  }
| value_expression
  {
    $$ = $1
  }

when_expression_list:
  when_expression
  {
    $$ = []*When{$1}
  }
| when_expression_list when_expression
  {
    $$ = append($1, $2)
  }

when_expression:
  WHEN boolean_expression THEN value_expression
  {
    $$ = &When{Cond: $2, Val: $4}
  }

else_expression_opt:
  {
    $$ = nil
  }
| ELSE value_expression
  {
    $$ = $2
  }

column_name:
  sql_id
  {
    $$ = &ColName{Name: $1}
  }
| ID '.' sql_id
  {
    $$ = &ColName{Qualifier: $1, Name: $3}
  }

value:
  STRING
  {
    $$ = StrVal($1)
  }
| NUMBER
  {
    $$ = NumVal($1)
  }
| VALUE_ARG
  {
    $$ = ValArg($1)
  }
| NULL
  {
    $$ = &NullVal{}
  }

group_by_opt:
  {
    $$ = nil
  }
| GROUP BY value_expression_list
  {
    $$ = $3
  }

having_opt:
  {
    $$ = nil
  }
| HAVING boolean_expression
  {
    $$ = $2
  }

order_by_opt:
  {
    $$ = nil
  }
| ORDER BY order_list
  {
    $$ = $3
  }

order_list:
  order
  {
    $$ = OrderBy{$1}
  }
| order_list ',' order
  {
    $$ = append($1, $3)
  }

order:
  value_expression asc_desc_opt
  {
    $$ = &Order{Expr: $1, Direction: $2}
  }

asc_desc_opt:
  {
    $$ = AST_ASC
  }
| ASC
  {
    $$ = AST_ASC
  }
| DESC
  {
    $$ = AST_DESC
  }

limit_opt:
  {
    $$ = nil
  }
| LIMIT value_expression
  {
    $$ = &Limit{Rowcount: $2}
  }
| LIMIT value_expression ',' value_expression
  {
    $$ = &Limit{Offset: $2, Rowcount: $4}
  }

lock_opt:
  {
    $$ = ""
  }
| FOR UPDATE
  {
    $$ = AST_FOR_UPDATE
  }
| LOCK IN sql_id sql_id
  {
    if !bytes.Equal($3, SHARE) {
      yylex.Error("expecting share")
      return 1
    }
    if !bytes.Equal($4, MODE) {
      yylex.Error("expecting mode")
      return 1
    }
    $$ = AST_SHARE_MODE
  }

column_list_opt:
  {
    $$ = nil
  }
| '(' column_list ')'
  {
    $$ = $2
  }

column_list:
  column_name
  {
    $$ = Columns{&NonStarExpr{Expr: $1}}
  }
| column_list ',' column_name
  {
    $$ = append($$, &NonStarExpr{Expr: $3})
  }

on_dup_opt:
  {
    $$ = nil
  }
| ON DUPLICATE KEY UPDATE update_list
  {
    $$ = $5
  }

row_list:
  VALUES tuple_list
  {
    $$ = $2
  }
| select_statement
  {
    $$ = $1
  }

tuple_list:
  row_tuple
  {
    $$ = Values{$1}
  }
| tuple_list ',' row_tuple
  {
    $$ = append($1, $3)
  }

row_tuple:
  '(' value_expression_list ')'
  {
    $$ = ValTuple($2)
  }
| subquery
  {
    $$ = $1
  }

update_list:
  update_expression
  {
    $$ = UpdateExprs{$1}
  }
| update_list ',' update_expression
  {
    $$ = append($1, $3)
  }

update_expression:
  column_name '=' value_expression
  {
    $$ = &UpdateExpr{Name: $1, Expr: $3} 
  }

exists_opt:
  { $$ = struct{}{} }
| IF EXISTS
  { $$ = struct{}{} }

not_exists_opt:
  { $$ = struct{}{} }
| IF NOT EXISTS
  { $$ = struct{}{} }

ignore_opt:
  { $$ = struct{}{} }
| IGNORE
  { $$ = struct{}{} }

non_rename_operation:
  ALTER
  { $$ = struct{}{} }
| DEFAULT
  { $$ = struct{}{} }
| DROP
  { $$ = struct{}{} }
| ORDER
  { $$ = struct{}{} }
| ID
  { $$ = struct{}{} }

to_opt:
  { $$ = struct{}{} }
| TO
  { $$ = struct{}{} }

constraint_opt:
  { $$ = struct{}{} }
| UNIQUE
  { $$ = struct{}{} }

using_opt:
  { $$ = struct{}{} }
| USING sql_id
  { $$ = struct{}{} }

sql_id:
  ID
  {
    $$ = $1
  }

force_eof:
{
  ForceEOF(yylex)
}
```

## File: `sqlparser/sql_mod.go`
```go
package sqlparser

// Magicify runs the SQL passed in, and a table name, throught a customized
// TextQL SQL Parser. This provides the following functionality:
//  - Queries that do not start with SELECT are implictly mapped to SELECT statements
//  - Queries that are missing a FROM, have the FROM inserted with tableName
func Magicify(sql string, tableName string) string {
	if tableName == "" {
		return sql
	}

	statement, err := Parse(sql)

	if err != nil {
		return sql
	}

	switch statement := statement.(type) {
	case *Select:
		replaceFromInSelect(statement, tableName)
		return generateQuery(statement)
	default:
		return sql
	}
}

func replaceFromInSelect(statement *Select, tableName string) {
	if statement.From == nil {
		tableName := &TableName{[]byte("[" + tableName + "]"), nil}
		aliasedTableExpr := AliasedTableExpr{tableName, nil, nil}
		tableExprs := TableExprs{&aliasedTableExpr}
		statement.From = &From{Type: AST_FROM, Expr: tableExprs}
	} else {
		for _, expr := range statement.From.Expr {
			switch expr := expr.(type) {
			case *AliasedTableExpr:
				switch subQuery := expr.Expr.(type) {
				case *Subquery:
					switch selectSubQuery := subQuery.Select.(type) {
					case *Select:
						replaceFromInSelect(selectSubQuery, tableName)
					default:
						return
					}
				default:
					return
				}
			default:
				return
			}
		}
	}
}

func generateQuery(statement Statement) string {
	buf := NewTrackedBuffer(nil)
	statement.Format(buf)
	return buf.String()
}
```

## File: `sqlparser/token.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package sqlparser

import (
	"bytes"
	"fmt"
	"strings"

	"github.com/dinedal/textql/sqlparser/sqltypes"
)

const EOFCHAR = 0x100

// Tokenizer is the struct used to generate SQL
// tokens for the parser.
type Tokenizer struct {
	InStream      *strings.Reader
	AllowComments bool
	ForceEOF      bool
	lastChar      uint16
	Position      int
	errorToken    []byte
	LastError     string
	posVarIndex   int
	ParseTree     Statement
}

// NewStringTokenizer creates a new Tokenizer for the
// sql string.
func NewStringTokenizer(sql string) *Tokenizer {
	return &Tokenizer{InStream: strings.NewReader(sql)}
}

var keywords = map[string]int{
	"all":           ALL,
	"alter":         ALTER,
	"analyze":       ANALYZE,
	"and":           AND,
	"as":            AS,
	"asc":           ASC,
	"between":       BETWEEN,
	"by":            BY,
	"case":          CASE,
	"create":        CREATE,
	"cross":         CROSS,
	"default":       DEFAULT,
	"delete":        DELETE,
	"desc":          DESC,
	"describe":      DESCRIBE,
	"distinct":      DISTINCT,
	"drop":          DROP,
	"duplicate":     DUPLICATE,
	"else":          ELSE,
	"end":           END,
	"except":        EXCEPT,
	"exists":        EXISTS,
	"explain":       EXPLAIN,
	"for":           FOR,
	"force":         FORCE,
	"from":          FROM,
	"group":         GROUP,
	"having":        HAVING,
	"if":            IF,
	"ignore":        IGNORE,
	"in":            IN,
	"index":         INDEX,
	"inner":         INNER,
	"insert":        INSERT,
	"intersect":     INTERSECT,
	"into":          INTO,
	"is":            IS,
	"join":          JOIN,
	"key":           KEY,
	"keyrange":      KEYRANGE,
	"left":          LEFT,
	"like":          LIKE,
	"limit":         LIMIT,
	"lock":          LOCK,
	"minus":         MINUS,
	"natural":       NATURAL,
	"not":           NOT,
	"null":          NULL,
	"on":            ON,
	"or":            OR,
	"order":         ORDER,
	"outer":         OUTER,
	"rename":        RENAME,
	"right":         RIGHT,
	"select":        SELECT,
	"set":           SET,
	"show":          SHOW,
	"straight_join": STRAIGHT_JOIN,
	"table":         TABLE,
	"then":          THEN,
	"to":            TO,
	"union":         UNION,
	"unique":        UNIQUE,
	"update":        UPDATE,
	"use":           USE,
	"using":         USING,
	"values":        VALUES,
	"view":          VIEW,
	"when":          WHEN,
	"where":         WHERE,
}

// Lex returns the next token form the Tokenizer.
// This function is used by go yacc.
func (tkn *Tokenizer) Lex(lval *yySymType) int {
	typ, val := tkn.Scan()
	for typ == COMMENT {
		if tkn.AllowComments {
			break
		}
		typ, val = tkn.Scan()
	}
	switch typ {
	case ID, STRING, NUMBER, VALUE_ARG, LIST_ARG, COMMENT:
		lval.bytes = val
	}
	tkn.errorToken = val
	return typ
}

// Error is called by go yacc if there's a parsing error.
func (tkn *Tokenizer) Error(err string) {
	buf := bytes.NewBuffer(make([]byte, 0, 32))
	if tkn.errorToken != nil {
		fmt.Fprintf(buf, "%s at position %v near %s", err, tkn.Position, tkn.errorToken)
	} else {
		fmt.Fprintf(buf, "%s at position %v", err, tkn.Position)
	}
	tkn.LastError = buf.String()
}

// Scan scans the tokenizer for the next token and returns
// the token type and an optional value.
func (tkn *Tokenizer) Scan() (int, []byte) {
	if tkn.ForceEOF {
		return 0, nil
	}

	if tkn.lastChar == 0 {
		tkn.next()
	}
	tkn.skipBlank()
	switch ch := tkn.lastChar; {
	case isLetter(ch):
		return tkn.scanIdentifier()
	case isDigit(ch):
		return tkn.scanNumber(false)
	case ch == ':':
		return tkn.scanBindVar()
	default:
		tkn.next()
		switch ch {
		case EOFCHAR:
			return 0, nil
		case '=', ',', ';', '(', ')', '+', '*', '%', '&', '|', '^', '~':
			return int(ch), nil
		case '?':
			tkn.posVarIndex++
			buf := new(bytes.Buffer)
			fmt.Fprintf(buf, ":v%d", tkn.posVarIndex)
			return VALUE_ARG, buf.Bytes()
		case '.':
			if isDigit(tkn.lastChar) {
				return tkn.scanNumber(true)
			} else {
				return int(ch), nil
			}
		case '/':
			switch tkn.lastChar {
			case '/':
				tkn.next()
				return tkn.scanCommentType1("//")
			case '*':
				tkn.next()
				return tkn.scanCommentType2()
			default:
				return int(ch), nil
			}
		case '-':
			if tkn.lastChar == '-' {
				tkn.next()
				return tkn.scanCommentType1("--")
			} else {
				return int(ch), nil
			}
		case '<':
			switch tkn.lastChar {
			case '>':
				tkn.next()
				return NE, nil
			case '=':
				tkn.next()
				switch tkn.lastChar {
				case '>':
					tkn.next()
					return NULL_SAFE_EQUAL, nil
				default:
					return LE, nil
				}
			default:
				return int(ch), nil
			}
		case '>':
			if tkn.lastChar == '=' {
				tkn.next()
				return GE, nil
			} else {
				return int(ch), nil
			}
		case '!':
			if tkn.lastChar == '=' {
				tkn.next()
				return NE, nil
			} else {
				return LEX_ERROR, []byte("!")
			}
		case '\'', '"':
			return tkn.scanString(ch, STRING)
		case '`':
			return tkn.scanLiteralIdentifier()
		default:
			return LEX_ERROR, []byte{byte(ch)}
		}
	}
}

func (tkn *Tokenizer) skipBlank() {
	ch := tkn.lastChar
	for ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t' {
		tkn.next()
		ch = tkn.lastChar
	}
}

func (tkn *Tokenizer) scanIdentifier() (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	buffer.WriteByte(byte(tkn.lastChar))
	for tkn.next(); isLetter(tkn.lastChar) || isDigit(tkn.lastChar); tkn.next() {
		buffer.WriteByte(byte(tkn.lastChar))
	}
	lowered := bytes.ToLower(buffer.Bytes())
	if keywordId, found := keywords[string(lowered)]; found {
		return keywordId, lowered
	}
	return ID, buffer.Bytes()
}

func (tkn *Tokenizer) scanLiteralIdentifier() (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	buffer.WriteByte(byte(tkn.lastChar))
	if !isLetter(tkn.lastChar) {
		return LEX_ERROR, buffer.Bytes()
	}
	for tkn.next(); isLetter(tkn.lastChar) || isDigit(tkn.lastChar); tkn.next() {
		buffer.WriteByte(byte(tkn.lastChar))
	}
	if tkn.lastChar != '`' {
		return LEX_ERROR, buffer.Bytes()
	}
	tkn.next()
	return ID, buffer.Bytes()
}

func (tkn *Tokenizer) scanBindVar() (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	buffer.WriteByte(byte(tkn.lastChar))
	token := VALUE_ARG
	tkn.next()
	if tkn.lastChar == ':' {
		token = LIST_ARG
		buffer.WriteByte(byte(tkn.lastChar))
		tkn.next()
	}
	if !isLetter(tkn.lastChar) {
		return LEX_ERROR, buffer.Bytes()
	}
	for isLetter(tkn.lastChar) || isDigit(tkn.lastChar) || tkn.lastChar == '.' {
		buffer.WriteByte(byte(tkn.lastChar))
		tkn.next()
	}
	return token, buffer.Bytes()
}

func (tkn *Tokenizer) scanMantissa(base int, buffer *bytes.Buffer) {
	for digitVal(tkn.lastChar) < base {
		tkn.ConsumeNext(buffer)
	}
}

func (tkn *Tokenizer) scanNumber(seenDecimalPoint bool) (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	if seenDecimalPoint {
		buffer.WriteByte('.')
		tkn.scanMantissa(10, buffer)
		goto exponent
	}

	if tkn.lastChar == '0' {
		// int or float
		tkn.ConsumeNext(buffer)
		if tkn.lastChar == 'x' || tkn.lastChar == 'X' {
			// hexadecimal int
			tkn.ConsumeNext(buffer)
			tkn.scanMantissa(16, buffer)
		} else {
			// octal int or float
			seenDecimalDigit := false
			tkn.scanMantissa(8, buffer)
			if tkn.lastChar == '8' || tkn.lastChar == '9' {
				// illegal octal int or float
				seenDecimalDigit = true
				tkn.scanMantissa(10, buffer)
			}
			if tkn.lastChar == '.' || tkn.lastChar == 'e' || tkn.lastChar == 'E' {
				goto fraction
			}
			// octal int
			if seenDecimalDigit {
				return LEX_ERROR, buffer.Bytes()
			}
		}
		goto exit
	}

	// decimal int or float
	tkn.scanMantissa(10, buffer)

fraction:
	if tkn.lastChar == '.' {
		tkn.ConsumeNext(buffer)
		tkn.scanMantissa(10, buffer)
	}

exponent:
	if tkn.lastChar == 'e' || tkn.lastChar == 'E' {
		tkn.ConsumeNext(buffer)
		if tkn.lastChar == '+' || tkn.lastChar == '-' {
			tkn.ConsumeNext(buffer)
		}
		tkn.scanMantissa(10, buffer)
	}

exit:
	return NUMBER, buffer.Bytes()
}

func (tkn *Tokenizer) scanString(delim uint16, typ int) (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	for {
		ch := tkn.lastChar
		tkn.next()
		if ch == delim {
			if tkn.lastChar == delim {
				tkn.next()
			} else {
				break
			}
		} else if ch == '\\' {
			if tkn.lastChar == EOFCHAR {
				return LEX_ERROR, buffer.Bytes()
			}
			if decodedChar := sqltypes.SqlDecodeMap[byte(tkn.lastChar)]; decodedChar == sqltypes.DONTESCAPE {
				ch = tkn.lastChar
			} else {
				ch = uint16(decodedChar)
			}
			tkn.next()
		}
		if ch == EOFCHAR {
			return LEX_ERROR, buffer.Bytes()
		}
		buffer.WriteByte(byte(ch))
	}
	return typ, buffer.Bytes()
}

func (tkn *Tokenizer) scanCommentType1(prefix string) (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	buffer.WriteString(prefix)
	for tkn.lastChar != EOFCHAR {
		if tkn.lastChar == '\n' {
			tkn.ConsumeNext(buffer)
			break
		}
		tkn.ConsumeNext(buffer)
	}
	return COMMENT, buffer.Bytes()
}

func (tkn *Tokenizer) scanCommentType2() (int, []byte) {
	buffer := bytes.NewBuffer(make([]byte, 0, 8))
	buffer.WriteString("/*")
	for {
		if tkn.lastChar == '*' {
			tkn.ConsumeNext(buffer)
			if tkn.lastChar == '/' {
				tkn.ConsumeNext(buffer)
				break
			}
			continue
		}
		if tkn.lastChar == EOFCHAR {
			return LEX_ERROR, buffer.Bytes()
		}
		tkn.ConsumeNext(buffer)
	}
	return COMMENT, buffer.Bytes()
}

func (tkn *Tokenizer) ConsumeNext(buffer *bytes.Buffer) {
	if tkn.lastChar == EOFCHAR {
		// This should never happen.
		panic("unexpected EOF")
	}
	buffer.WriteByte(byte(tkn.lastChar))
	tkn.next()
}

func (tkn *Tokenizer) next() {
	if ch, err := tkn.InStream.ReadByte(); err != nil {
		// Only EOF is possible.
		tkn.lastChar = EOFCHAR
	} else {
		tkn.lastChar = uint16(ch)
	}
	tkn.Position++
}

func isLetter(ch uint16) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_' || ch == '@'
}

func digitVal(ch uint16) int {
	switch {
	case '0' <= ch && ch <= '9':
		return int(ch) - '0'
	case 'a' <= ch && ch <= 'f':
		return int(ch) - 'a' + 10
	case 'A' <= ch && ch <= 'F':
		return int(ch) - 'A' + 10
	}
	return 16 // larger than any legal digit val
}

func isDigit(ch uint16) bool {
	return '0' <= ch && ch <= '9'
}
```

## File: `sqlparser/tracked_buffer.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package sqlparser

import (
	"bytes"
	"fmt"
)

// TrackedBuffer is used to rebuild a query from the ast.
// bindLocations keeps track of locations in the buffer that
// use bind variables for efficient future substitutions.
// nodeFormatter is the formatting function the buffer will
// use to format a node. By default(nil), it's FormatNode.
// But you can supply a different formatting function if you
// want to generate a query that's different from the default.
type TrackedBuffer struct {
	*bytes.Buffer
	bindLocations []bindLocation
	nodeFormatter func(buf *TrackedBuffer, node SQLNode)
}

func NewTrackedBuffer(nodeFormatter func(buf *TrackedBuffer, node SQLNode)) *TrackedBuffer {
	buf := &TrackedBuffer{
		Buffer:        bytes.NewBuffer(make([]byte, 0, 128)),
		bindLocations: make([]bindLocation, 0, 4),
		nodeFormatter: nodeFormatter,
	}
	return buf
}

// Myprintf mimics fmt.Fprintf(buf, ...), but limited to Node(%v),
// Node.Value(%s) and string(%s). It also allows a %a for a value argument, in
// which case it adds tracking info for future substitutions.
//
// The name must be something other than the usual Printf() to avoid "go vet"
// warnings due to our custom format specifiers.
func (buf *TrackedBuffer) Myprintf(format string, values ...interface{}) {
	end := len(format)
	fieldnum := 0
	for i := 0; i < end; {
		lasti := i
		for i < end && format[i] != '%' {
			i++
		}
		if i > lasti {
			buf.WriteString(format[lasti:i])
		}
		if i >= end {
			break
		}
		i++ // '%'
		switch format[i] {
		case 'c':
			switch v := values[fieldnum].(type) {
			case byte:
				buf.WriteByte(v)
			case rune:
				buf.WriteRune(v)
			default:
				panic(fmt.Sprintf("unexpected type %T", v))
			}
		case 's':
			switch v := values[fieldnum].(type) {
			case []byte:
				buf.Write(v)
			case string:
				buf.WriteString(v)
			default:
				panic(fmt.Sprintf("unexpected type %T", v))
			}
		case 'v':
			node := values[fieldnum].(SQLNode)
			if buf.nodeFormatter == nil {
				node.Format(buf)
			} else {
				buf.nodeFormatter(buf, node)
			}
		case 'a':
			buf.WriteArg(values[fieldnum].(string))
		default:
			panic("unexpected")
		}
		fieldnum++
		i++
	}
}

// WriteArg writes a value argument into the buffer. arg should not contain
// the ':' prefix. It also adds tracking info for future substitutions.
func (buf *TrackedBuffer) WriteArg(arg string) {
	buf.bindLocations = append(buf.bindLocations, bindLocation{
		offset: buf.Len(),
		length: len(arg),
	})
	buf.WriteString(arg)
}

func (buf *TrackedBuffer) ParsedQuery() *ParsedQuery {
	return &ParsedQuery{Query: buf.String(), bindLocations: buf.bindLocations}
}

func (buf *TrackedBuffer) HasBindVars() bool {
	return len(buf.bindLocations) != 0
}
```

## File: `sqlparser/y.output`
```

state 0
	$accept: .any_command $end 
	distinct_opt: .    (45)

	SELECT  shift 15
	INSERT  shift 17
	UPDATE  shift 18
	DELETE  shift 19
	DISTINCT  shift 29
	SET  shift 20
	CREATE  shift 21
	ALTER  shift 22
	DROP  shift 24
	RENAME  shift 23
	ANALYZE  shift 25
	SHOW  shift 26
	DESCRIBE  shift 27
	EXPLAIN  shift 28
	.  reduce 45 (src line 340)

	any_command  goto 1
	command  goto 2
	select_statement  goto 3
	missing_select_statement  goto 4
	insert_statement  goto 5
	update_statement  goto 6
	delete_statement  goto 7
	set_statement  goto 8
	create_statement  goto 9
	alter_statement  goto 10
	rename_statement  goto 11
	drop_statement  goto 12
	analyze_statement  goto 13
	other_statement  goto 14
	distinct_opt  goto 16

state 1
	$accept:  any_command.$end 

	$end  accept
	.  error


state 2
	any_command:  command.    (1)

	.  reduce 1 (src line 152)


state 3
	command:  select_statement.    (2)
	select_statement:  select_statement.union_op select_statement 

	UNION  shift 31
	MINUS  shift 32
	EXCEPT  shift 33
	INTERSECT  shift 34
	.  reduce 2 (src line 158)

	union_op  goto 30

state 4
	command:  missing_select_statement.    (3)

	.  reduce 3 (src line 163)


state 5
	command:  insert_statement.    (4)

	.  reduce 4 (src line 167)


state 6
	command:  update_statement.    (5)

	.  reduce 5 (src line 168)


state 7
	command:  delete_statement.    (6)

	.  reduce 6 (src line 169)


state 8
	command:  set_statement.    (7)

	.  reduce 7 (src line 170)


state 9
	command:  create_statement.    (8)

	.  reduce 8 (src line 171)


state 10
	command:  alter_statement.    (9)

	.  reduce 9 (src line 172)


state 11
	command:  rename_statement.    (10)

	.  reduce 10 (src line 173)


state 12
	command:  drop_statement.    (11)

	.  reduce 11 (src line 174)


state 13
	command:  analyze_statement.    (12)

	.  reduce 12 (src line 175)


state 14
	command:  other_statement.    (13)

	.  reduce 13 (src line 176)


state 15
	select_statement:  SELECT.comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 
	$$36: .    (36)

	.  reduce 36 (src line 299)

	comment_opt  goto 35
	$$36  goto 36

state 16
	missing_select_statement:  distinct_opt.select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 41
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	'*'  shift 39
	CASE  shift 66
	IF  shift 64
	.  error

	select_expression_list  goto 37
	select_expression  goto 38
	expression  goto 40
	boolean_expression  goto 42
	condition  goto 44
	value  goto 47
	value_expression  goto 43
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 17
	insert_statement:  INSERT.comment_opt INTO dml_table_expression column_list_opt row_list on_dup_opt 
	insert_statement:  INSERT.comment_opt INTO dml_table_expression SET update_list on_dup_opt 
	$$36: .    (36)

	.  reduce 36 (src line 299)

	comment_opt  goto 67
	$$36  goto 36

state 18
	update_statement:  UPDATE.comment_opt dml_table_expression SET update_list where_expression_opt order_by_opt limit_opt 
	$$36: .    (36)

	.  reduce 36 (src line 299)

	comment_opt  goto 68
	$$36  goto 36

state 19
	delete_statement:  DELETE.comment_opt FROM dml_table_expression where_expression_opt order_by_opt limit_opt 
	$$36: .    (36)

	.  reduce 36 (src line 299)

	comment_opt  goto 69
	$$36  goto 36

state 20
	set_statement:  SET.comment_opt update_list 
	$$36: .    (36)

	.  reduce 36 (src line 299)

	comment_opt  goto 70
	$$36  goto 36

state 21
	create_statement:  CREATE.TABLE not_exists_opt ID force_eof 
	create_statement:  CREATE.constraint_opt INDEX sql_id using_opt ON ID force_eof 
	create_statement:  CREATE.VIEW sql_id force_eof 
	constraint_opt: .    (201)

	TABLE  shift 71
	VIEW  shift 73
	UNIQUE  shift 74
	.  reduce 201 (src line 1039)

	constraint_opt  goto 72

state 22
	alter_statement:  ALTER.ignore_opt TABLE ID non_rename_operation force_eof 
	alter_statement:  ALTER.ignore_opt TABLE ID RENAME to_opt ID 
	alter_statement:  ALTER.VIEW sql_id force_eof 
	ignore_opt: .    (192)

	VIEW  shift 76
	IGNORE  shift 77
	.  reduce 192 (src line 1017)

	ignore_opt  goto 75

state 23
	rename_statement:  RENAME.TABLE ID TO ID 

	TABLE  shift 78
	.  error


state 24
	drop_statement:  DROP.TABLE exists_opt ID 
	drop_statement:  DROP.INDEX sql_id ON ID 
	drop_statement:  DROP.VIEW exists_opt sql_id force_eof 

	TABLE  shift 79
	INDEX  shift 80
	VIEW  shift 81
	.  error


state 25
	analyze_statement:  ANALYZE.TABLE ID 

	TABLE  shift 82
	.  error


state 26
	other_statement:  SHOW.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 83

state 27
	other_statement:  DESCRIBE.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 84

state 28
	other_statement:  EXPLAIN.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 85

state 29
	distinct_opt:  DISTINCT.    (46)

	.  reduce 46 (src line 344)


state 30
	select_statement:  select_statement union_op.select_statement 

	SELECT  shift 15
	.  error

	select_statement  goto 86

state 31
	union_op:  UNION.    (40)
	union_op:  UNION.ALL 

	ALL  shift 87
	.  reduce 40 (src line 318)


state 32
	union_op:  MINUS.    (42)

	.  reduce 42 (src line 327)


state 33
	union_op:  EXCEPT.    (43)

	.  reduce 43 (src line 331)


state 34
	union_op:  INTERSECT.    (44)

	.  reduce 44 (src line 335)


state 35
	select_statement:  SELECT comment_opt.distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 
	distinct_opt: .    (45)

	DISTINCT  shift 29
	.  reduce 45 (src line 340)

	distinct_opt  goto 88

state 36
	comment_opt:  $$36.comment_list 
	comment_list: .    (38)

	.  reduce 38 (src line 309)

	comment_list  goto 89

state 37
	missing_select_statement:  distinct_opt select_expression_list.from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 
	select_expression_list:  select_expression_list.',' select_expression 
	from_expression_list_opt: .    (86)

	FROM  shift 92
	','  shift 91
	.  reduce 86 (src line 526)

	from_expression_list_opt  goto 90

state 38
	select_expression_list:  select_expression.    (47)

	.  reduce 47 (src line 349)


state 39
	select_expression:  '*'.    (49)

	.  reduce 49 (src line 359)


state 40
	select_expression:  expression.as_lower_opt 
	as_lower_opt: .    (54)

	AS  shift 95
	ID  shift 96
	.  reduce 54 (src line 383)

	as_lower_opt  goto 93
	sql_id  goto 94

state 41
	select_expression:  ID.'.' '*' 
	column_name:  ID.'.' sql_id 
	sql_id:  ID.    (205)

	'.'  shift 97
	.  reduce 205 (src line 1049)


state 42
	expression:  boolean_expression.    (52)
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 

	OR  shift 99
	AND  shift 98
	.  reduce 52 (src line 373)


state 43
	expression:  value_expression.    (53)
	condition:  value_expression.compare value_expression 
	condition:  value_expression.IN col_tuple 
	condition:  value_expression.NOT IN col_tuple 
	condition:  value_expression.LIKE value_expression 
	condition:  value_expression.NOT LIKE value_expression 
	condition:  value_expression.BETWEEN value_expression AND value_expression 
	condition:  value_expression.NOT BETWEEN value_expression AND value_expression 
	condition:  value_expression.IS NULL 
	condition:  value_expression.IS NOT NULL 
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	IN  shift 101
	IS  shift 105
	LIKE  shift 103
	BETWEEN  shift 104
	LE  shift 117
	GE  shift 118
	NE  shift 119
	NULL_SAFE_EQUAL  shift 120
	'='  shift 114
	'<'  shift 115
	'>'  shift 116
	NOT  shift 102
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 53 (src line 378)

	compare  goto 100

state 44
	boolean_expression:  condition.    (90)

	.  reduce 90 (src line 545)


state 45
	boolean_expression:  NOT.boolean_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 121
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 46
	boolean_expression:  '('.boolean_expression ')' 
	subquery:  '('.select_statement ')' 
	row_tuple:  '('.value_expression_list ')' 

	SELECT  shift 15
	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	select_statement  goto 125
	boolean_expression  goto 124
	condition  goto 44
	value  goto 47
	value_expression  goto 127
	value_expression_list  goto 126
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 47
	value_expression:  value.    (119)

	.  reduce 119 (src line 670)


state 48
	value_expression:  column_name.    (120)

	.  reduce 120 (src line 675)


state 49
	value_expression:  row_tuple.    (121)

	.  reduce 121 (src line 679)


state 50
	value_expression:  unary_operator.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 128
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 51
	value_expression:  sql_id.'(' ')' 
	value_expression:  sql_id.'(' select_expression_list ')' 
	value_expression:  sql_id.'(' DISTINCT select_expression_list ')' 
	column_name:  sql_id.    (149)

	'('  shift 130
	.  reduce 149 (src line 815)


state 52
	value_expression:  keyword_as_func.'(' select_expression_list ')' 

	'('  shift 131
	.  error


state 53
	value_expression:  case_expression.    (135)

	.  reduce 135 (src line 746)


state 54
	condition:  EXISTS.subquery 

	'('  shift 133
	.  error

	subquery  goto 132

state 55
	condition:  KEYRANGE.'(' value ',' value ')' 

	'('  shift 134
	.  error


state 56
	value:  STRING.    (151)

	.  reduce 151 (src line 825)


state 57
	value:  NUMBER.    (152)

	.  reduce 152 (src line 830)


state 58
	value:  VALUE_ARG.    (153)

	.  reduce 153 (src line 834)


state 59
	value:  NULL.    (154)

	.  reduce 154 (src line 838)


state 60
	row_tuple:  subquery.    (184)

	.  reduce 184 (src line 986)


state 61
	unary_operator:  '+'.    (138)

	.  reduce 138 (src line 761)


state 62
	unary_operator:  '-'.    (139)

	.  reduce 139 (src line 766)


state 63
	unary_operator:  '~'.    (140)

	.  reduce 140 (src line 770)


state 64
	keyword_as_func:  IF.    (136)

	.  reduce 136 (src line 751)


state 65
	keyword_as_func:  VALUES.    (137)

	.  reduce 137 (src line 756)


state 66
	case_expression:  CASE.value_expression_opt when_expression_list else_expression_opt END 
	value_expression_opt: .    (142)

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  reduce 142 (src line 781)

	value  goto 47
	value_expression  goto 136
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	value_expression_opt  goto 135
	sql_id  goto 51

state 67
	insert_statement:  INSERT comment_opt.INTO dml_table_expression column_list_opt row_list on_dup_opt 
	insert_statement:  INSERT comment_opt.INTO dml_table_expression SET update_list on_dup_opt 

	INTO  shift 137
	.  error


state 68
	update_statement:  UPDATE comment_opt.dml_table_expression SET update_list where_expression_opt order_by_opt limit_opt 

	ID  shift 139
	.  error

	dml_table_expression  goto 138

state 69
	delete_statement:  DELETE comment_opt.FROM dml_table_expression where_expression_opt order_by_opt limit_opt 

	FROM  shift 140
	.  error


state 70
	set_statement:  SET comment_opt.update_list 

	ID  shift 123
	.  error

	column_name  goto 143
	update_list  goto 141
	update_expression  goto 142
	sql_id  goto 144

state 71
	create_statement:  CREATE TABLE.not_exists_opt ID force_eof 
	not_exists_opt: .    (190)

	IF  shift 146
	.  reduce 190 (src line 1012)

	not_exists_opt  goto 145

state 72
	create_statement:  CREATE constraint_opt.INDEX sql_id using_opt ON ID force_eof 

	INDEX  shift 147
	.  error


state 73
	create_statement:  CREATE VIEW.sql_id force_eof 

	ID  shift 96
	.  error

	sql_id  goto 148

state 74
	constraint_opt:  UNIQUE.    (202)

	.  reduce 202 (src line 1041)


state 75
	alter_statement:  ALTER ignore_opt.TABLE ID non_rename_operation force_eof 
	alter_statement:  ALTER ignore_opt.TABLE ID RENAME to_opt ID 

	TABLE  shift 149
	.  error


state 76
	alter_statement:  ALTER VIEW.sql_id force_eof 

	ID  shift 96
	.  error

	sql_id  goto 150

state 77
	ignore_opt:  IGNORE.    (193)

	.  reduce 193 (src line 1019)


state 78
	rename_statement:  RENAME TABLE.ID TO ID 

	ID  shift 151
	.  error


state 79
	drop_statement:  DROP TABLE.exists_opt ID 
	exists_opt: .    (188)

	IF  shift 153
	.  reduce 188 (src line 1007)

	exists_opt  goto 152

state 80
	drop_statement:  DROP INDEX.sql_id ON ID 

	ID  shift 96
	.  error

	sql_id  goto 154

state 81
	drop_statement:  DROP VIEW.exists_opt sql_id force_eof 
	exists_opt: .    (188)

	IF  shift 153
	.  reduce 188 (src line 1007)

	exists_opt  goto 155

state 82
	analyze_statement:  ANALYZE TABLE.ID 

	ID  shift 156
	.  error


state 83
	other_statement:  SHOW force_eof.    (33)

	.  reduce 33 (src line 285)


state 84
	other_statement:  DESCRIBE force_eof.    (34)

	.  reduce 34 (src line 290)


state 85
	other_statement:  EXPLAIN force_eof.    (35)

	.  reduce 35 (src line 294)


state 86
	select_statement:  select_statement.union_op select_statement 
	select_statement:  select_statement union_op select_statement.    (16)

	.  reduce 16 (src line 189)

	union_op  goto 30

state 87
	union_op:  UNION ALL.    (41)

	.  reduce 41 (src line 323)


state 88
	select_statement:  SELECT comment_opt distinct_opt.select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 41
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	'*'  shift 39
	CASE  shift 66
	IF  shift 64
	.  error

	select_expression_list  goto 157
	select_expression  goto 38
	expression  goto 40
	boolean_expression  goto 42
	condition  goto 44
	value  goto 47
	value_expression  goto 43
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 89
	comment_opt:  $$36 comment_list.    (37)
	comment_list:  comment_list.COMMENT 

	COMMENT  shift 158
	.  reduce 37 (src line 303)


state 90
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt.where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 
	where_expression_opt: .    (88)

	WHERE  shift 160
	.  reduce 88 (src line 536)

	where_expression_opt  goto 159

state 91
	select_expression_list:  select_expression_list ','.select_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 41
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	'*'  shift 39
	CASE  shift 66
	IF  shift 64
	.  error

	select_expression  goto 161
	expression  goto 40
	boolean_expression  goto 42
	condition  goto 44
	value  goto 47
	value_expression  goto 43
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 92
	from_expression_list_opt:  FROM.table_expression_list 

	ID  shift 166
	'('  shift 165
	.  error

	table_expression_list  goto 162
	table_expression  goto 163
	simple_table_expression  goto 164
	subquery  goto 167

state 93
	select_expression:  expression as_lower_opt.    (50)

	.  reduce 50 (src line 364)


state 94
	as_lower_opt:  sql_id.    (55)

	.  reduce 55 (src line 387)


state 95
	as_lower_opt:  AS.sql_id 

	ID  shift 96
	.  error

	sql_id  goto 168

state 96
	sql_id:  ID.    (205)

	.  reduce 205 (src line 1049)


state 97
	select_expression:  ID '.'.'*' 
	column_name:  ID '.'.sql_id 

	ID  shift 96
	'*'  shift 169
	.  error

	sql_id  goto 170

state 98
	boolean_expression:  boolean_expression AND.boolean_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 171
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 99
	boolean_expression:  boolean_expression OR.boolean_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 172
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 100
	condition:  value_expression compare.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 173
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 101
	condition:  value_expression IN.col_tuple 

	LIST_ARG  shift 177
	'('  shift 175
	.  error

	col_tuple  goto 174
	subquery  goto 176

state 102
	condition:  value_expression NOT.IN col_tuple 
	condition:  value_expression NOT.LIKE value_expression 
	condition:  value_expression NOT.BETWEEN value_expression AND value_expression 

	IN  shift 178
	LIKE  shift 179
	BETWEEN  shift 180
	.  error


state 103
	condition:  value_expression LIKE.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 181
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 104
	condition:  value_expression BETWEEN.value_expression AND value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 182
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 105
	condition:  value_expression IS.NULL 
	condition:  value_expression IS.NOT NULL 

	NULL  shift 183
	NOT  shift 184
	.  error


state 106
	value_expression:  value_expression '&'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 185
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 107
	value_expression:  value_expression '|'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 186
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 108
	value_expression:  value_expression '^'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 187
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 109
	value_expression:  value_expression '+'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 188
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 110
	value_expression:  value_expression '-'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 189
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 111
	value_expression:  value_expression '*'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 190
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 112
	value_expression:  value_expression '/'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 191
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 113
	value_expression:  value_expression '%'.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 192
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 114
	compare:  '='.    (106)

	.  reduce 106 (src line 610)


state 115
	compare:  '<'.    (107)

	.  reduce 107 (src line 615)


state 116
	compare:  '>'.    (108)

	.  reduce 108 (src line 619)


state 117
	compare:  LE.    (109)

	.  reduce 109 (src line 623)


state 118
	compare:  GE.    (110)

	.  reduce 110 (src line 627)


state 119
	compare:  NE.    (111)

	.  reduce 111 (src line 631)


state 120
	compare:  NULL_SAFE_EQUAL.    (112)

	.  reduce 112 (src line 635)


state 121
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 
	boolean_expression:  NOT boolean_expression.    (93)

	.  reduce 93 (src line 555)


state 122
	condition:  value_expression.compare value_expression 
	condition:  value_expression.IN col_tuple 
	condition:  value_expression.NOT IN col_tuple 
	condition:  value_expression.LIKE value_expression 
	condition:  value_expression.NOT LIKE value_expression 
	condition:  value_expression.BETWEEN value_expression AND value_expression 
	condition:  value_expression.NOT BETWEEN value_expression AND value_expression 
	condition:  value_expression.IS NULL 
	condition:  value_expression.IS NOT NULL 
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	IN  shift 101
	IS  shift 105
	LIKE  shift 103
	BETWEEN  shift 104
	LE  shift 117
	GE  shift 118
	NE  shift 119
	NULL_SAFE_EQUAL  shift 120
	'='  shift 114
	'<'  shift 115
	'>'  shift 116
	NOT  shift 102
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  error

	compare  goto 100

state 123
	column_name:  ID.'.' sql_id 
	sql_id:  ID.    (205)

	'.'  shift 193
	.  reduce 205 (src line 1049)


state 124
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 
	boolean_expression:  '(' boolean_expression.')' 

	OR  shift 99
	AND  shift 98
	')'  shift 194
	.  error


state 125
	select_statement:  select_statement.union_op select_statement 
	subquery:  '(' select_statement.')' 

	UNION  shift 31
	MINUS  shift 32
	EXCEPT  shift 33
	INTERSECT  shift 34
	')'  shift 195
	.  error

	union_op  goto 30

state 126
	value_expression_list:  value_expression_list.',' value_expression 
	row_tuple:  '(' value_expression_list.')' 

	','  shift 196
	')'  shift 197
	.  error


state 127
	condition:  value_expression.compare value_expression 
	condition:  value_expression.IN col_tuple 
	condition:  value_expression.NOT IN col_tuple 
	condition:  value_expression.LIKE value_expression 
	condition:  value_expression.NOT LIKE value_expression 
	condition:  value_expression.BETWEEN value_expression AND value_expression 
	condition:  value_expression.NOT BETWEEN value_expression AND value_expression 
	condition:  value_expression.IS NULL 
	condition:  value_expression.IS NOT NULL 
	value_expression_list:  value_expression.    (117)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	IN  shift 101
	IS  shift 105
	LIKE  shift 103
	BETWEEN  shift 104
	LE  shift 117
	GE  shift 118
	NE  shift 119
	NULL_SAFE_EQUAL  shift 120
	'='  shift 114
	'<'  shift 115
	'>'  shift 116
	NOT  shift 102
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 117 (src line 660)

	compare  goto 100

state 128
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	value_expression:  unary_operator value_expression.    (130)

	.  reduce 130 (src line 715)


state 129
	subquery:  '('.select_statement ')' 
	row_tuple:  '('.value_expression_list ')' 

	SELECT  shift 15
	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	select_statement  goto 125
	value  goto 47
	value_expression  goto 198
	value_expression_list  goto 126
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 130
	value_expression:  sql_id '('.')' 
	value_expression:  sql_id '('.select_expression_list ')' 
	value_expression:  sql_id '('.DISTINCT select_expression_list ')' 

	DISTINCT  shift 201
	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 41
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	'*'  shift 39
	CASE  shift 66
	IF  shift 64
	')'  shift 199
	.  error

	select_expression_list  goto 200
	select_expression  goto 38
	expression  goto 40
	boolean_expression  goto 42
	condition  goto 44
	value  goto 47
	value_expression  goto 43
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 131
	value_expression:  keyword_as_func '('.select_expression_list ')' 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 41
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	'*'  shift 39
	CASE  shift 66
	IF  shift 64
	.  error

	select_expression_list  goto 202
	select_expression  goto 38
	expression  goto 40
	boolean_expression  goto 42
	condition  goto 44
	value  goto 47
	value_expression  goto 43
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 132
	condition:  EXISTS subquery.    (104)

	.  reduce 104 (src line 601)


state 133
	subquery:  '('.select_statement ')' 

	SELECT  shift 15
	.  error

	select_statement  goto 125

state 134
	condition:  KEYRANGE '('.value ',' value ')' 

	NULL  shift 59
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	.  error

	value  goto 203

state 135
	case_expression:  CASE value_expression_opt.when_expression_list else_expression_opt END 

	WHEN  shift 206
	.  error

	when_expression_list  goto 204
	when_expression  goto 205

state 136
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	value_expression_opt:  value_expression.    (143)

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 143 (src line 785)


state 137
	insert_statement:  INSERT comment_opt INTO.dml_table_expression column_list_opt row_list on_dup_opt 
	insert_statement:  INSERT comment_opt INTO.dml_table_expression SET update_list on_dup_opt 

	ID  shift 139
	.  error

	dml_table_expression  goto 207

state 138
	update_statement:  UPDATE comment_opt dml_table_expression.SET update_list where_expression_opt order_by_opt limit_opt 

	SET  shift 208
	.  error


state 139
	dml_table_expression:  ID.    (78)
	dml_table_expression:  ID.'.' ID 

	'.'  shift 209
	.  reduce 78 (src line 489)


state 140
	delete_statement:  DELETE comment_opt FROM.dml_table_expression where_expression_opt order_by_opt limit_opt 

	ID  shift 139
	.  error

	dml_table_expression  goto 210

state 141
	set_statement:  SET comment_opt update_list.    (21)
	update_list:  update_list.',' update_expression 

	','  shift 211
	.  reduce 21 (src line 222)


state 142
	update_list:  update_expression.    (185)

	.  reduce 185 (src line 991)


state 143
	update_expression:  column_name.'=' value_expression 

	'='  shift 212
	.  error


state 144
	column_name:  sql_id.    (149)

	.  reduce 149 (src line 815)


state 145
	create_statement:  CREATE TABLE not_exists_opt.ID force_eof 

	ID  shift 213
	.  error


state 146
	not_exists_opt:  IF.NOT EXISTS 

	NOT  shift 214
	.  error


state 147
	create_statement:  CREATE constraint_opt INDEX.sql_id using_opt ON ID force_eof 

	ID  shift 96
	.  error

	sql_id  goto 215

state 148
	create_statement:  CREATE VIEW sql_id.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 216

state 149
	alter_statement:  ALTER ignore_opt TABLE.ID non_rename_operation force_eof 
	alter_statement:  ALTER ignore_opt TABLE.ID RENAME to_opt ID 

	ID  shift 217
	.  error


state 150
	alter_statement:  ALTER VIEW sql_id.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 218

state 151
	rename_statement:  RENAME TABLE ID.TO ID 

	TO  shift 219
	.  error


state 152
	drop_statement:  DROP TABLE exists_opt.ID 

	ID  shift 220
	.  error


state 153
	exists_opt:  IF.EXISTS 

	EXISTS  shift 221
	.  error


state 154
	drop_statement:  DROP INDEX sql_id.ON ID 

	ON  shift 222
	.  error


state 155
	drop_statement:  DROP VIEW exists_opt.sql_id force_eof 

	ID  shift 96
	.  error

	sql_id  goto 223

state 156
	analyze_statement:  ANALYZE TABLE ID.    (32)

	.  reduce 32 (src line 279)


state 157
	select_statement:  SELECT comment_opt distinct_opt select_expression_list.from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 
	select_expression_list:  select_expression_list.',' select_expression 
	from_expression_list_opt: .    (86)

	FROM  shift 92
	','  shift 91
	.  reduce 86 (src line 526)

	from_expression_list_opt  goto 224

state 158
	comment_list:  comment_list COMMENT.    (39)

	.  reduce 39 (src line 313)


state 159
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt where_expression_opt.group_by_opt having_opt order_by_opt limit_opt lock_opt 
	group_by_opt: .    (155)

	GROUP  shift 226
	.  reduce 155 (src line 843)

	group_by_opt  goto 225

state 160
	where_expression_opt:  WHERE.boolean_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 227
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 161
	select_expression_list:  select_expression_list ',' select_expression.    (48)

	.  reduce 48 (src line 354)


state 162
	table_expression_list:  table_expression_list.',' table_expression 
	from_expression_list_opt:  FROM table_expression_list.    (87)

	','  shift 228
	.  reduce 87 (src line 530)


state 163
	table_expression_list:  table_expression.    (57)
	table_expression:  table_expression.join_type table_expression 
	table_expression:  table_expression.join_type table_expression ON boolean_expression 

	JOIN  shift 230
	STRAIGHT_JOIN  shift 231
	LEFT  shift 232
	RIGHT  shift 233
	INNER  shift 234
	CROSS  shift 235
	NATURAL  shift 236
	.  reduce 57 (src line 396)

	join_type  goto 229

state 164
	table_expression:  simple_table_expression.as_opt index_hint_list 
	as_opt: .    (63)

	AS  shift 239
	ID  shift 238
	.  reduce 63 (src line 424)

	as_opt  goto 237

state 165
	table_expression:  '('.table_expression ')' 
	subquery:  '('.select_statement ')' 

	SELECT  shift 15
	ID  shift 166
	'('  shift 165
	.  error

	select_statement  goto 125
	table_expression  goto 240
	simple_table_expression  goto 164
	subquery  goto 167

state 166
	simple_table_expression:  ID.    (75)
	simple_table_expression:  ID.'.' ID 

	'.'  shift 241
	.  reduce 75 (src line 475)


state 167
	simple_table_expression:  subquery.    (77)

	.  reduce 77 (src line 484)


state 168
	as_lower_opt:  AS sql_id.    (56)

	.  reduce 56 (src line 391)


state 169
	select_expression:  ID '.' '*'.    (51)

	.  reduce 51 (src line 368)


state 170
	column_name:  ID '.' sql_id.    (150)

	.  reduce 150 (src line 820)


state 171
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression AND boolean_expression.    (91)
	boolean_expression:  boolean_expression.OR boolean_expression 

	.  reduce 91 (src line 547)


state 172
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 
	boolean_expression:  boolean_expression OR boolean_expression.    (92)

	AND  shift 98
	.  reduce 92 (src line 551)


state 173
	condition:  value_expression compare value_expression.    (95)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 95 (src line 564)


state 174
	condition:  value_expression IN col_tuple.    (96)

	.  reduce 96 (src line 569)


state 175
	col_tuple:  '('.value_expression_list ')' 
	subquery:  '('.select_statement ')' 

	SELECT  shift 15
	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	select_statement  goto 125
	value  goto 47
	value_expression  goto 198
	value_expression_list  goto 242
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 176
	col_tuple:  subquery.    (114)

	.  reduce 114 (src line 645)


state 177
	col_tuple:  LIST_ARG.    (115)

	.  reduce 115 (src line 649)


state 178
	condition:  value_expression NOT IN.col_tuple 

	LIST_ARG  shift 177
	'('  shift 175
	.  error

	col_tuple  goto 243
	subquery  goto 176

state 179
	condition:  value_expression NOT LIKE.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 244
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 180
	condition:  value_expression NOT BETWEEN.value_expression AND value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 245
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 181
	condition:  value_expression LIKE value_expression.    (98)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 98 (src line 577)


state 182
	condition:  value_expression BETWEEN value_expression.AND value_expression 
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	AND  shift 246
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  error


state 183
	condition:  value_expression IS NULL.    (102)

	.  reduce 102 (src line 593)


state 184
	condition:  value_expression IS NOT.NULL 

	NULL  shift 247
	.  error


state 185
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression '&' value_expression.    (122)
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 122 (src line 683)


state 186
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression '|' value_expression.    (123)
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 123 (src line 687)


state 187
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression '^' value_expression.    (124)
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 124 (src line 691)


state 188
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression '+' value_expression.    (125)
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 125 (src line 695)


state 189
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression '-' value_expression.    (126)
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 126 (src line 699)


state 190
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression '*' value_expression.    (127)
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	.  reduce 127 (src line 703)


state 191
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression '/' value_expression.    (128)
	value_expression:  value_expression.'%' value_expression 

	.  reduce 128 (src line 707)


state 192
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	value_expression:  value_expression '%' value_expression.    (129)

	.  reduce 129 (src line 711)


state 193
	column_name:  ID '.'.sql_id 

	ID  shift 96
	.  error

	sql_id  goto 170

state 194
	boolean_expression:  '(' boolean_expression ')'.    (94)

	.  reduce 94 (src line 559)


state 195
	subquery:  '(' select_statement ')'.    (116)

	.  reduce 116 (src line 654)


state 196
	value_expression_list:  value_expression_list ','.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 248
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 197
	row_tuple:  '(' value_expression_list ')'.    (183)

	.  reduce 183 (src line 981)


state 198
	value_expression_list:  value_expression.    (117)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 117 (src line 660)


state 199
	value_expression:  sql_id '(' ')'.    (131)

	.  reduce 131 (src line 730)


state 200
	select_expression_list:  select_expression_list.',' select_expression 
	value_expression:  sql_id '(' select_expression_list.')' 

	','  shift 91
	')'  shift 249
	.  error


state 201
	value_expression:  sql_id '(' DISTINCT.select_expression_list ')' 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 41
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	'*'  shift 39
	CASE  shift 66
	IF  shift 64
	.  error

	select_expression_list  goto 250
	select_expression  goto 38
	expression  goto 40
	boolean_expression  goto 42
	condition  goto 44
	value  goto 47
	value_expression  goto 43
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 202
	select_expression_list:  select_expression_list.',' select_expression 
	value_expression:  keyword_as_func '(' select_expression_list.')' 

	','  shift 91
	')'  shift 251
	.  error


state 203
	condition:  KEYRANGE '(' value.',' value ')' 

	','  shift 252
	.  error


state 204
	case_expression:  CASE value_expression_opt when_expression_list.else_expression_opt END 
	when_expression_list:  when_expression_list.when_expression 
	else_expression_opt: .    (147)

	WHEN  shift 206
	ELSE  shift 255
	.  reduce 147 (src line 806)

	when_expression  goto 254
	else_expression_opt  goto 253

state 205
	when_expression_list:  when_expression.    (144)

	.  reduce 144 (src line 790)


state 206
	when_expression:  WHEN.boolean_expression THEN value_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 256
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 207
	insert_statement:  INSERT comment_opt INTO dml_table_expression.column_list_opt row_list on_dup_opt 
	insert_statement:  INSERT comment_opt INTO dml_table_expression.SET update_list on_dup_opt 
	column_list_opt: .    (173)

	SET  shift 258
	'('  shift 259
	.  reduce 173 (src line 933)

	column_list_opt  goto 257

state 208
	update_statement:  UPDATE comment_opt dml_table_expression SET.update_list where_expression_opt order_by_opt limit_opt 

	ID  shift 123
	.  error

	column_name  goto 143
	update_list  goto 260
	update_expression  goto 142
	sql_id  goto 144

state 209
	dml_table_expression:  ID '.'.ID 

	ID  shift 261
	.  error


state 210
	delete_statement:  DELETE comment_opt FROM dml_table_expression.where_expression_opt order_by_opt limit_opt 
	where_expression_opt: .    (88)

	WHERE  shift 160
	.  reduce 88 (src line 536)

	where_expression_opt  goto 262

state 211
	update_list:  update_list ','.update_expression 

	ID  shift 123
	.  error

	column_name  goto 143
	update_expression  goto 263
	sql_id  goto 144

state 212
	update_expression:  column_name '='.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 264
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 213
	create_statement:  CREATE TABLE not_exists_opt ID.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 265

state 214
	not_exists_opt:  IF NOT.EXISTS 

	EXISTS  shift 266
	.  error


state 215
	create_statement:  CREATE constraint_opt INDEX sql_id.using_opt ON ID force_eof 
	using_opt: .    (203)

	USING  shift 268
	.  reduce 203 (src line 1044)

	using_opt  goto 267

state 216
	create_statement:  CREATE VIEW sql_id force_eof.    (24)

	.  reduce 24 (src line 238)


state 217
	alter_statement:  ALTER ignore_opt TABLE ID.non_rename_operation force_eof 
	alter_statement:  ALTER ignore_opt TABLE ID.RENAME to_opt ID 

	ORDER  shift 274
	DEFAULT  shift 272
	ID  shift 275
	ALTER  shift 271
	DROP  shift 273
	RENAME  shift 270
	.  error

	non_rename_operation  goto 269

state 218
	alter_statement:  ALTER VIEW sql_id force_eof.    (27)

	.  reduce 27 (src line 253)


state 219
	rename_statement:  RENAME TABLE ID TO.ID 

	ID  shift 276
	.  error


state 220
	drop_statement:  DROP TABLE exists_opt ID.    (29)

	.  reduce 29 (src line 264)


state 221
	exists_opt:  IF EXISTS.    (189)

	.  reduce 189 (src line 1009)


state 222
	drop_statement:  DROP INDEX sql_id ON.ID 

	ID  shift 277
	.  error


state 223
	drop_statement:  DROP VIEW exists_opt sql_id.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 278

state 224
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt.where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt 
	where_expression_opt: .    (88)

	WHERE  shift 160
	.  reduce 88 (src line 536)

	where_expression_opt  goto 279

state 225
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt.having_opt order_by_opt limit_opt lock_opt 
	having_opt: .    (157)

	HAVING  shift 281
	.  reduce 157 (src line 852)

	having_opt  goto 280

state 226
	group_by_opt:  GROUP.BY value_expression_list 

	BY  shift 282
	.  error


state 227
	where_expression_opt:  WHERE boolean_expression.    (89)
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 

	OR  shift 99
	AND  shift 98
	.  reduce 89 (src line 540)


state 228
	table_expression_list:  table_expression_list ','.table_expression 

	ID  shift 166
	'('  shift 165
	.  error

	table_expression  goto 283
	simple_table_expression  goto 164
	subquery  goto 167

state 229
	table_expression:  table_expression join_type.table_expression 
	table_expression:  table_expression join_type.table_expression ON boolean_expression 

	ID  shift 166
	'('  shift 165
	.  error

	table_expression  goto 284
	simple_table_expression  goto 164
	subquery  goto 167

state 230
	join_type:  JOIN.    (66)

	.  reduce 66 (src line 437)


state 231
	join_type:  STRAIGHT_JOIN.    (67)

	.  reduce 67 (src line 442)


state 232
	join_type:  LEFT.JOIN 
	join_type:  LEFT.OUTER JOIN 

	JOIN  shift 285
	OUTER  shift 286
	.  error


state 233
	join_type:  RIGHT.JOIN 
	join_type:  RIGHT.OUTER JOIN 

	JOIN  shift 287
	OUTER  shift 288
	.  error


state 234
	join_type:  INNER.JOIN 

	JOIN  shift 289
	.  error


state 235
	join_type:  CROSS.JOIN 

	JOIN  shift 290
	.  error


state 236
	join_type:  NATURAL.JOIN 

	JOIN  shift 291
	.  error


state 237
	table_expression:  simple_table_expression as_opt.index_hint_list 
	index_hint_list: .    (80)

	USE  shift 293
	FORCE  shift 295
	IGNORE  shift 294
	.  reduce 80 (src line 499)

	index_hint_list  goto 292

state 238
	as_opt:  ID.    (64)

	.  reduce 64 (src line 428)


state 239
	as_opt:  AS.ID 

	ID  shift 296
	.  error


state 240
	table_expression:  '(' table_expression.')' 
	table_expression:  table_expression.join_type table_expression 
	table_expression:  table_expression.join_type table_expression ON boolean_expression 

	JOIN  shift 230
	STRAIGHT_JOIN  shift 231
	LEFT  shift 232
	RIGHT  shift 233
	INNER  shift 234
	CROSS  shift 235
	NATURAL  shift 236
	')'  shift 297
	.  error

	join_type  goto 229

state 241
	simple_table_expression:  ID '.'.ID 

	ID  shift 298
	.  error


state 242
	col_tuple:  '(' value_expression_list.')' 
	value_expression_list:  value_expression_list.',' value_expression 

	','  shift 196
	')'  shift 299
	.  error


state 243
	condition:  value_expression NOT IN col_tuple.    (97)

	.  reduce 97 (src line 573)


state 244
	condition:  value_expression NOT LIKE value_expression.    (99)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 99 (src line 581)


state 245
	condition:  value_expression NOT BETWEEN value_expression.AND value_expression 
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	AND  shift 300
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  error


state 246
	condition:  value_expression BETWEEN value_expression AND.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 301
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 247
	condition:  value_expression IS NOT NULL.    (103)

	.  reduce 103 (src line 597)


state 248
	value_expression_list:  value_expression_list ',' value_expression.    (118)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 118 (src line 665)


state 249
	value_expression:  sql_id '(' select_expression_list ')'.    (132)

	.  reduce 132 (src line 734)


state 250
	select_expression_list:  select_expression_list.',' select_expression 
	value_expression:  sql_id '(' DISTINCT select_expression_list.')' 

	','  shift 91
	')'  shift 302
	.  error


state 251
	value_expression:  keyword_as_func '(' select_expression_list ')'.    (134)

	.  reduce 134 (src line 742)


state 252
	condition:  KEYRANGE '(' value ','.value ')' 

	NULL  shift 59
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	.  error

	value  goto 303

state 253
	case_expression:  CASE value_expression_opt when_expression_list else_expression_opt.END 

	END  shift 304
	.  error


state 254
	when_expression_list:  when_expression_list when_expression.    (145)

	.  reduce 145 (src line 795)


state 255
	else_expression_opt:  ELSE.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 305
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 256
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 
	when_expression:  WHEN boolean_expression.THEN value_expression 

	OR  shift 99
	AND  shift 98
	THEN  shift 306
	.  error


state 257
	insert_statement:  INSERT comment_opt INTO dml_table_expression column_list_opt.row_list on_dup_opt 

	SELECT  shift 15
	VALUES  shift 308
	.  error

	select_statement  goto 309
	row_list  goto 307

state 258
	insert_statement:  INSERT comment_opt INTO dml_table_expression SET.update_list on_dup_opt 

	ID  shift 123
	.  error

	column_name  goto 143
	update_list  goto 310
	update_expression  goto 142
	sql_id  goto 144

state 259
	column_list_opt:  '('.column_list ')' 

	ID  shift 123
	.  error

	column_name  goto 312
	column_list  goto 311
	sql_id  goto 144

state 260
	update_statement:  UPDATE comment_opt dml_table_expression SET update_list.where_expression_opt order_by_opt limit_opt 
	update_list:  update_list.',' update_expression 
	where_expression_opt: .    (88)

	WHERE  shift 160
	','  shift 211
	.  reduce 88 (src line 536)

	where_expression_opt  goto 313

state 261
	dml_table_expression:  ID '.' ID.    (79)

	.  reduce 79 (src line 494)


state 262
	delete_statement:  DELETE comment_opt FROM dml_table_expression where_expression_opt.order_by_opt limit_opt 
	order_by_opt: .    (159)

	ORDER  shift 315
	.  reduce 159 (src line 861)

	order_by_opt  goto 314

state 263
	update_list:  update_list ',' update_expression.    (186)

	.  reduce 186 (src line 996)


state 264
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	update_expression:  column_name '=' value_expression.    (187)

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 187 (src line 1001)


state 265
	create_statement:  CREATE TABLE not_exists_opt ID force_eof.    (22)

	.  reduce 22 (src line 228)


state 266
	not_exists_opt:  IF NOT EXISTS.    (191)

	.  reduce 191 (src line 1014)


state 267
	create_statement:  CREATE constraint_opt INDEX sql_id using_opt.ON ID force_eof 

	ON  shift 316
	.  error


state 268
	using_opt:  USING.sql_id 

	ID  shift 96
	.  error

	sql_id  goto 317

state 269
	alter_statement:  ALTER ignore_opt TABLE ID non_rename_operation.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 318

state 270
	alter_statement:  ALTER ignore_opt TABLE ID RENAME.to_opt ID 
	to_opt: .    (199)

	TO  shift 320
	.  reduce 199 (src line 1034)

	to_opt  goto 319

state 271
	non_rename_operation:  ALTER.    (194)

	.  reduce 194 (src line 1022)


state 272
	non_rename_operation:  DEFAULT.    (195)

	.  reduce 195 (src line 1025)


state 273
	non_rename_operation:  DROP.    (196)

	.  reduce 196 (src line 1027)


state 274
	non_rename_operation:  ORDER.    (197)

	.  reduce 197 (src line 1029)


state 275
	non_rename_operation:  ID.    (198)

	.  reduce 198 (src line 1031)


state 276
	rename_statement:  RENAME TABLE ID TO ID.    (28)

	.  reduce 28 (src line 258)


state 277
	drop_statement:  DROP INDEX sql_id ON ID.    (30)

	.  reduce 30 (src line 269)


state 278
	drop_statement:  DROP VIEW exists_opt sql_id force_eof.    (31)

	.  reduce 31 (src line 274)


state 279
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt.group_by_opt having_opt order_by_opt limit_opt lock_opt 
	group_by_opt: .    (155)

	GROUP  shift 226
	.  reduce 155 (src line 843)

	group_by_opt  goto 321

state 280
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt.order_by_opt limit_opt lock_opt 
	order_by_opt: .    (159)

	ORDER  shift 315
	.  reduce 159 (src line 861)

	order_by_opt  goto 322

state 281
	having_opt:  HAVING.boolean_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 323
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 282
	group_by_opt:  GROUP BY.value_expression_list 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 198
	value_expression_list  goto 324
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 283
	table_expression_list:  table_expression_list ',' table_expression.    (58)
	table_expression:  table_expression.join_type table_expression 
	table_expression:  table_expression.join_type table_expression ON boolean_expression 

	JOIN  shift 230
	STRAIGHT_JOIN  shift 231
	LEFT  shift 232
	RIGHT  shift 233
	INNER  shift 234
	CROSS  shift 235
	NATURAL  shift 236
	.  reduce 58 (src line 401)

	join_type  goto 229

state 284
	table_expression:  table_expression.join_type table_expression 
	table_expression:  table_expression join_type table_expression.    (61)
	table_expression:  table_expression.join_type table_expression ON boolean_expression 
	table_expression:  table_expression join_type table_expression.ON boolean_expression 

	ON  shift 325
	.  reduce 61 (src line 415)

	join_type  goto 229

state 285
	join_type:  LEFT JOIN.    (68)

	.  reduce 68 (src line 446)


state 286
	join_type:  LEFT OUTER.JOIN 

	JOIN  shift 326
	.  error


state 287
	join_type:  RIGHT JOIN.    (70)

	.  reduce 70 (src line 454)


state 288
	join_type:  RIGHT OUTER.JOIN 

	JOIN  shift 327
	.  error


state 289
	join_type:  INNER JOIN.    (72)

	.  reduce 72 (src line 462)


state 290
	join_type:  CROSS JOIN.    (73)

	.  reduce 73 (src line 466)


state 291
	join_type:  NATURAL JOIN.    (74)

	.  reduce 74 (src line 470)


state 292
	table_expression:  simple_table_expression as_opt index_hint_list.    (59)

	.  reduce 59 (src line 406)


state 293
	index_hint_list:  USE.INDEX '(' index_list ')' 

	INDEX  shift 328
	.  error


state 294
	index_hint_list:  IGNORE.INDEX '(' index_list ')' 

	INDEX  shift 329
	.  error


state 295
	index_hint_list:  FORCE.INDEX '(' index_list ')' 

	INDEX  shift 330
	.  error


state 296
	as_opt:  AS ID.    (65)

	.  reduce 65 (src line 432)


state 297
	table_expression:  '(' table_expression ')'.    (60)

	.  reduce 60 (src line 411)


state 298
	simple_table_expression:  ID '.' ID.    (76)

	.  reduce 76 (src line 480)


state 299
	col_tuple:  '(' value_expression_list ')'.    (113)

	.  reduce 113 (src line 640)


state 300
	condition:  value_expression NOT BETWEEN value_expression AND.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 331
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 301
	condition:  value_expression BETWEEN value_expression AND value_expression.    (100)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 100 (src line 585)


state 302
	value_expression:  sql_id '(' DISTINCT select_expression_list ')'.    (133)

	.  reduce 133 (src line 738)


state 303
	condition:  KEYRANGE '(' value ',' value.')' 

	')'  shift 332
	.  error


state 304
	case_expression:  CASE value_expression_opt when_expression_list else_expression_opt END.    (141)

	.  reduce 141 (src line 775)


state 305
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	else_expression_opt:  ELSE value_expression.    (148)

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 148 (src line 810)


state 306
	when_expression:  WHEN boolean_expression THEN.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 333
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 307
	insert_statement:  INSERT comment_opt INTO dml_table_expression column_list_opt row_list.on_dup_opt 
	on_dup_opt: .    (177)

	ON  shift 335
	.  reduce 177 (src line 952)

	on_dup_opt  goto 334

state 308
	row_list:  VALUES.tuple_list 

	'('  shift 129
	.  error

	tuple_list  goto 336
	row_tuple  goto 337
	subquery  goto 60

state 309
	select_statement:  select_statement.union_op select_statement 
	row_list:  select_statement.    (180)

	UNION  shift 31
	MINUS  shift 32
	EXCEPT  shift 33
	INTERSECT  shift 34
	.  reduce 180 (src line 966)

	union_op  goto 30

state 310
	insert_statement:  INSERT comment_opt INTO dml_table_expression SET update_list.on_dup_opt 
	update_list:  update_list.',' update_expression 
	on_dup_opt: .    (177)

	','  shift 211
	ON  shift 335
	.  reduce 177 (src line 952)

	on_dup_opt  goto 338

state 311
	column_list_opt:  '(' column_list.')' 
	column_list:  column_list.',' column_name 

	','  shift 340
	')'  shift 339
	.  error


state 312
	column_list:  column_name.    (175)

	.  reduce 175 (src line 942)


state 313
	update_statement:  UPDATE comment_opt dml_table_expression SET update_list where_expression_opt.order_by_opt limit_opt 
	order_by_opt: .    (159)

	ORDER  shift 315
	.  reduce 159 (src line 861)

	order_by_opt  goto 341

state 314
	delete_statement:  DELETE comment_opt FROM dml_table_expression where_expression_opt order_by_opt.limit_opt 
	limit_opt: .    (167)

	LIMIT  shift 343
	.  reduce 167 (src line 899)

	limit_opt  goto 342

state 315
	order_by_opt:  ORDER.BY order_list 

	BY  shift 344
	.  error


state 316
	create_statement:  CREATE constraint_opt INDEX sql_id using_opt ON.ID force_eof 

	ID  shift 345
	.  error


state 317
	using_opt:  USING sql_id.    (204)

	.  reduce 204 (src line 1046)


state 318
	alter_statement:  ALTER ignore_opt TABLE ID non_rename_operation force_eof.    (25)

	.  reduce 25 (src line 243)


state 319
	alter_statement:  ALTER ignore_opt TABLE ID RENAME to_opt.ID 

	ID  shift 346
	.  error


state 320
	to_opt:  TO.    (200)

	.  reduce 200 (src line 1036)


state 321
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt.having_opt order_by_opt limit_opt lock_opt 
	having_opt: .    (157)

	HAVING  shift 281
	.  reduce 157 (src line 852)

	having_opt  goto 347

state 322
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt.limit_opt lock_opt 
	limit_opt: .    (167)

	LIMIT  shift 343
	.  reduce 167 (src line 899)

	limit_opt  goto 348

state 323
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 
	having_opt:  HAVING boolean_expression.    (158)

	OR  shift 99
	AND  shift 98
	.  reduce 158 (src line 856)


state 324
	value_expression_list:  value_expression_list.',' value_expression 
	group_by_opt:  GROUP BY value_expression_list.    (156)

	','  shift 196
	.  reduce 156 (src line 847)


state 325
	table_expression:  table_expression join_type table_expression ON.boolean_expression 

	EXISTS  shift 54
	NULL  shift 59
	VALUES  shift 65
	KEYRANGE  shift 55
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 46
	'~'  shift 63
	NOT  shift 45
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	boolean_expression  goto 349
	condition  goto 44
	value  goto 47
	value_expression  goto 122
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 326
	join_type:  LEFT OUTER JOIN.    (69)

	.  reduce 69 (src line 450)


state 327
	join_type:  RIGHT OUTER JOIN.    (71)

	.  reduce 71 (src line 458)


state 328
	index_hint_list:  USE INDEX.'(' index_list ')' 

	'('  shift 350
	.  error


state 329
	index_hint_list:  IGNORE INDEX.'(' index_list ')' 

	'('  shift 351
	.  error


state 330
	index_hint_list:  FORCE INDEX.'(' index_list ')' 

	'('  shift 352
	.  error


state 331
	condition:  value_expression NOT BETWEEN value_expression AND value_expression.    (101)
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 101 (src line 589)


state 332
	condition:  KEYRANGE '(' value ',' value ')'.    (105)

	.  reduce 105 (src line 605)


state 333
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	when_expression:  WHEN boolean_expression THEN value_expression.    (146)

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 146 (src line 800)


state 334
	insert_statement:  INSERT comment_opt INTO dml_table_expression column_list_opt row_list on_dup_opt.    (17)

	.  reduce 17 (src line 194)


state 335
	on_dup_opt:  ON.DUPLICATE KEY UPDATE update_list 

	DUPLICATE  shift 353
	.  error


state 336
	row_list:  VALUES tuple_list.    (179)
	tuple_list:  tuple_list.',' row_tuple 

	','  shift 354
	.  reduce 179 (src line 961)


state 337
	tuple_list:  row_tuple.    (181)

	.  reduce 181 (src line 971)


state 338
	insert_statement:  INSERT comment_opt INTO dml_table_expression SET update_list on_dup_opt.    (18)

	.  reduce 18 (src line 199)


state 339
	column_list_opt:  '(' column_list ')'.    (174)

	.  reduce 174 (src line 937)


state 340
	column_list:  column_list ','.column_name 

	ID  shift 123
	.  error

	column_name  goto 355
	sql_id  goto 144

state 341
	update_statement:  UPDATE comment_opt dml_table_expression SET update_list where_expression_opt order_by_opt.limit_opt 
	limit_opt: .    (167)

	LIMIT  shift 343
	.  reduce 167 (src line 899)

	limit_opt  goto 356

state 342
	delete_statement:  DELETE comment_opt FROM dml_table_expression where_expression_opt order_by_opt limit_opt.    (20)

	.  reduce 20 (src line 216)


state 343
	limit_opt:  LIMIT.value_expression 
	limit_opt:  LIMIT.value_expression ',' value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 357
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 344
	order_by_opt:  ORDER BY.order_list 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 360
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	order_list  goto 358
	order  goto 359
	sql_id  goto 51

state 345
	create_statement:  CREATE constraint_opt INDEX sql_id using_opt ON ID.force_eof 
	force_eof: .    (206)

	.  reduce 206 (src line 1055)

	force_eof  goto 361

state 346
	alter_statement:  ALTER ignore_opt TABLE ID RENAME to_opt ID.    (26)

	.  reduce 26 (src line 248)


state 347
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt.order_by_opt limit_opt lock_opt 
	order_by_opt: .    (159)

	ORDER  shift 315
	.  reduce 159 (src line 861)

	order_by_opt  goto 362

state 348
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt.lock_opt 
	lock_opt: .    (170)

	FOR  shift 364
	LOCK  shift 365
	.  reduce 170 (src line 912)

	lock_opt  goto 363

state 349
	table_expression:  table_expression join_type table_expression ON boolean_expression.    (62)
	boolean_expression:  boolean_expression.AND boolean_expression 
	boolean_expression:  boolean_expression.OR boolean_expression 

	OR  shift 99
	AND  shift 98
	.  reduce 62 (src line 419)


state 350
	index_hint_list:  USE INDEX '('.index_list ')' 

	ID  shift 96
	.  error

	index_list  goto 366
	sql_id  goto 367

state 351
	index_hint_list:  IGNORE INDEX '('.index_list ')' 

	ID  shift 96
	.  error

	index_list  goto 368
	sql_id  goto 367

state 352
	index_hint_list:  FORCE INDEX '('.index_list ')' 

	ID  shift 96
	.  error

	index_list  goto 369
	sql_id  goto 367

state 353
	on_dup_opt:  ON DUPLICATE.KEY UPDATE update_list 

	KEY  shift 370
	.  error


state 354
	tuple_list:  tuple_list ','.row_tuple 

	'('  shift 129
	.  error

	row_tuple  goto 371
	subquery  goto 60

state 355
	column_list:  column_list ',' column_name.    (176)

	.  reduce 176 (src line 947)


state 356
	update_statement:  UPDATE comment_opt dml_table_expression SET update_list where_expression_opt order_by_opt limit_opt.    (19)

	.  reduce 19 (src line 210)


state 357
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	limit_opt:  LIMIT value_expression.    (168)
	limit_opt:  LIMIT value_expression.',' value_expression 

	','  shift 372
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 168 (src line 903)


state 358
	order_by_opt:  ORDER BY order_list.    (160)
	order_list:  order_list.',' order 

	','  shift 373
	.  reduce 160 (src line 865)


state 359
	order_list:  order.    (161)

	.  reduce 161 (src line 870)


state 360
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	order:  value_expression.asc_desc_opt 
	asc_desc_opt: .    (164)

	ASC  shift 375
	DESC  shift 376
	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 164 (src line 886)

	asc_desc_opt  goto 374

state 361
	create_statement:  CREATE constraint_opt INDEX sql_id using_opt ON ID force_eof.    (23)

	.  reduce 23 (src line 233)


state 362
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt.limit_opt lock_opt 
	limit_opt: .    (167)

	LIMIT  shift 343
	.  reduce 167 (src line 899)

	limit_opt  goto 377

state 363
	missing_select_statement:  distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt.    (14)

	.  reduce 14 (src line 178)


state 364
	lock_opt:  FOR.UPDATE 

	UPDATE  shift 378
	.  error


state 365
	lock_opt:  LOCK.IN sql_id sql_id 

	IN  shift 379
	.  error


state 366
	index_hint_list:  USE INDEX '(' index_list.')' 
	index_list:  index_list.',' sql_id 

	','  shift 381
	')'  shift 380
	.  error


state 367
	index_list:  sql_id.    (84)

	.  reduce 84 (src line 516)


state 368
	index_hint_list:  IGNORE INDEX '(' index_list.')' 
	index_list:  index_list.',' sql_id 

	','  shift 381
	')'  shift 382
	.  error


state 369
	index_hint_list:  FORCE INDEX '(' index_list.')' 
	index_list:  index_list.',' sql_id 

	','  shift 381
	')'  shift 383
	.  error


state 370
	on_dup_opt:  ON DUPLICATE KEY.UPDATE update_list 

	UPDATE  shift 384
	.  error


state 371
	tuple_list:  tuple_list ',' row_tuple.    (182)

	.  reduce 182 (src line 976)


state 372
	limit_opt:  LIMIT value_expression ','.value_expression 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 385
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	sql_id  goto 51

state 373
	order_list:  order_list ','.order 

	NULL  shift 59
	VALUES  shift 65
	ID  shift 123
	STRING  shift 56
	NUMBER  shift 57
	VALUE_ARG  shift 58
	'('  shift 129
	'~'  shift 63
	'+'  shift 61
	'-'  shift 62
	CASE  shift 66
	IF  shift 64
	.  error

	value  goto 47
	value_expression  goto 360
	row_tuple  goto 49
	keyword_as_func  goto 52
	subquery  goto 60
	unary_operator  goto 50
	column_name  goto 48
	case_expression  goto 53
	order  goto 386
	sql_id  goto 51

state 374
	order:  value_expression asc_desc_opt.    (163)

	.  reduce 163 (src line 880)


state 375
	asc_desc_opt:  ASC.    (165)

	.  reduce 165 (src line 890)


state 376
	asc_desc_opt:  DESC.    (166)

	.  reduce 166 (src line 894)


state 377
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt.lock_opt 
	lock_opt: .    (170)

	FOR  shift 364
	LOCK  shift 365
	.  reduce 170 (src line 912)

	lock_opt  goto 387

state 378
	lock_opt:  FOR UPDATE.    (171)

	.  reduce 171 (src line 916)


state 379
	lock_opt:  LOCK IN.sql_id sql_id 

	ID  shift 96
	.  error

	sql_id  goto 388

state 380
	index_hint_list:  USE INDEX '(' index_list ')'.    (81)

	.  reduce 81 (src line 503)


state 381
	index_list:  index_list ','.sql_id 

	ID  shift 96
	.  error

	sql_id  goto 389

state 382
	index_hint_list:  IGNORE INDEX '(' index_list ')'.    (82)

	.  reduce 82 (src line 507)


state 383
	index_hint_list:  FORCE INDEX '(' index_list ')'.    (83)

	.  reduce 83 (src line 511)


state 384
	on_dup_opt:  ON DUPLICATE KEY UPDATE.update_list 

	ID  shift 123
	.  error

	column_name  goto 143
	update_list  goto 390
	update_expression  goto 142
	sql_id  goto 144

state 385
	value_expression:  value_expression.'&' value_expression 
	value_expression:  value_expression.'|' value_expression 
	value_expression:  value_expression.'^' value_expression 
	value_expression:  value_expression.'+' value_expression 
	value_expression:  value_expression.'-' value_expression 
	value_expression:  value_expression.'*' value_expression 
	value_expression:  value_expression.'/' value_expression 
	value_expression:  value_expression.'%' value_expression 
	limit_opt:  LIMIT value_expression ',' value_expression.    (169)

	'&'  shift 106
	'|'  shift 107
	'^'  shift 108
	'+'  shift 109
	'-'  shift 110
	'*'  shift 111
	'/'  shift 112
	'%'  shift 113
	.  reduce 169 (src line 907)


state 386
	order_list:  order_list ',' order.    (162)

	.  reduce 162 (src line 875)


state 387
	select_statement:  SELECT comment_opt distinct_opt select_expression_list from_expression_list_opt where_expression_opt group_by_opt having_opt order_by_opt limit_opt lock_opt.    (15)

	.  reduce 15 (src line 184)


state 388
	lock_opt:  LOCK IN sql_id.sql_id 

	ID  shift 96
	.  error

	sql_id  goto 391

state 389
	index_list:  index_list ',' sql_id.    (85)

	.  reduce 85 (src line 521)


state 390
	on_dup_opt:  ON DUPLICATE KEY UPDATE update_list.    (178)
	update_list:  update_list.',' update_expression 

	','  shift 211
	.  reduce 178 (src line 956)


state 391
	lock_opt:  LOCK IN sql_id sql_id.    (172)

	.  reduce 172 (src line 920)


101 terminals, 75 nonterminals
207 grammar rules, 392/2000 states
0 shift/reduce, 0 reduce/reduce conflicts reported
124 working sets used
memory: parser 742/30000
405 extra closures
1040 shift entries, 1 exceptions
210 goto entries
386 entries saved by goto default
Optimizer space used: output 678/30000
678 table entries, 102 zero
maximum spread: 101, maximum offset: 388
```

## File: `sqlparser/sqltypes/sqltypes.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package sqltypes implements interfaces and types that represent SQL values.
package sqltypes

import (
	"encoding/base64"
	"encoding/gob"
	"encoding/json"
	"fmt"
	"reflect"
	"strconv"
	"time"
	"unsafe"
)

var (
	NULL       = Value{}
	DONTESCAPE = byte(255)
	nullstr    = []byte("null")
)

// BinWriter interface is used for encoding values.
// Types like bytes.Buffer conform to this interface.
// We expect the writer objects to be in-memory buffers.
// So, we don't expect the write operations to fail.
type BinWriter interface {
	Write([]byte) (int, error)
	WriteByte(byte) error
}

// Value can store any SQL value. NULL is stored as nil.
type Value struct {
	Inner InnerValue
}

// Numeric represents non-fractional SQL number.
type Numeric []byte

// Fractional represents fractional types like float and decimal
// It's functionally equivalent to Numeric other than how it's constructed
type Fractional []byte

// String represents any SQL type that needs to be represented using quotes.
type String []byte

// MakeNumeric makes a Numeric from a []byte without validation.
func MakeNumeric(b []byte) Value {
	return Value{Numeric(b)}
}

// MakeFractional makes a Fractional value from a []byte without validation.
func MakeFractional(b []byte) Value {
	return Value{Fractional(b)}
}

// MakeString makes a String value from a []byte.
func MakeString(b []byte) Value {
	return Value{String(b)}
}

// Raw returns the raw bytes. All types are currently implemented as []byte.
func (v Value) Raw() []byte {
	if v.Inner == nil {
		return nil
	}
	return v.Inner.raw()
}

// String returns the raw value as a string
func (v Value) String() string {
	if v.Inner == nil {
		return ""
	}
	return toString(v.Inner.raw())
}

// String force casts a []byte to a string.
// USE AT YOUR OWN RISK
func toString(b []byte) (s string) {
	if len(b) == 0 {
		return ""
	}
	pbytes := (*reflect.SliceHeader)(unsafe.Pointer(&b))
	pstring := (*reflect.StringHeader)(unsafe.Pointer(&s))
	pstring.Data = pbytes.Data
	pstring.Len = pbytes.Len
	return
}

// ParseInt64 will parse a Numeric value into an int64
func (v Value) ParseInt64() (val int64, err error) {
	if v.Inner == nil {
		return 0, fmt.Errorf("value is null")
	}
	n, ok := v.Inner.(Numeric)
	if !ok {
		return 0, fmt.Errorf("value is not Numeric")
	}
	return strconv.ParseInt(string(n.raw()), 10, 64)
}

// ParseUint64 will parse a Numeric value into a uint64
func (v Value) ParseUint64() (val uint64, err error) {
	if v.Inner == nil {
		return 0, fmt.Errorf("value is null")
	}
	n, ok := v.Inner.(Numeric)
	if !ok {
		return 0, fmt.Errorf("value is not Numeric")
	}
	return strconv.ParseUint(string(n.raw()), 10, 64)
}

// ParseFloat64 will parse a Fractional value into an float64
func (v Value) ParseFloat64() (val float64, err error) {
	if v.Inner == nil {
		return 0, fmt.Errorf("value is null")
	}
	n, ok := v.Inner.(Fractional)
	if !ok {
		return 0, fmt.Errorf("value is not Fractional")
	}
	return strconv.ParseFloat(string(n.raw()), 64)
}

// EncodeSql encodes the value into an SQL statement. Can be binary.
func (v Value) EncodeSql(b BinWriter) {
	if v.Inner == nil {
		if _, err := b.Write(nullstr); err != nil {
			panic(err)
		}
	} else {
		v.Inner.encodeSql(b)
	}
}

// EncodeAscii encodes the value using 7-bit clean ascii bytes.
func (v Value) EncodeAscii(b BinWriter) {
	if v.Inner == nil {
		if _, err := b.Write(nullstr); err != nil {
			panic(err)
		}
	} else {
		v.Inner.encodeAscii(b)
	}
}

func (v Value) IsNull() bool {
	return v.Inner == nil
}

func (v Value) IsNumeric() (ok bool) {
	if v.Inner != nil {
		_, ok = v.Inner.(Numeric)
	}
	return ok
}

func (v Value) IsFractional() (ok bool) {
	if v.Inner != nil {
		_, ok = v.Inner.(Fractional)
	}
	return ok
}

func (v Value) IsString() (ok bool) {
	if v.Inner != nil {
		_, ok = v.Inner.(String)
	}
	return ok
}

// MarshalJSON should only be used for testing.
// It's not a complete implementation.
func (v Value) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.Inner)
}

// UnmarshalJSON should only be used for testing.
// It's not a complete implementation.
func (v *Value) UnmarshalJSON(b []byte) error {
	if len(b) == 0 {
		return fmt.Errorf("error unmarshaling empty bytes")
	}
	var val interface{}
	var err error
	switch b[0] {
	case '-':
		var ival int64
		err = json.Unmarshal(b, &ival)
		val = ival
	case '"':
		var bval []byte
		err = json.Unmarshal(b, &bval)
		val = bval
	case 'n': // null
		err = json.Unmarshal(b, &val)
	default:
		var uval uint64
		err = json.Unmarshal(b, &uval)
		val = uval
	}
	if err != nil {
		return err
	}
	*v, err = BuildValue(val)
	return err
}

// InnerValue defines methods that need to be supported by all non-null value types.
type InnerValue interface {
	raw() []byte
	encodeSql(BinWriter)
	encodeAscii(BinWriter)
}

func BuildValue(goval interface{}) (v Value, err error) {
	switch bindVal := goval.(type) {
	case nil:
		// no op
	case int:
		v = Value{Numeric(strconv.AppendInt(nil, int64(bindVal), 10))}
	case int32:
		v = Value{Numeric(strconv.AppendInt(nil, int64(bindVal), 10))}
	case int64:
		v = Value{Numeric(strconv.AppendInt(nil, int64(bindVal), 10))}
	case uint:
		v = Value{Numeric(strconv.AppendUint(nil, uint64(bindVal), 10))}
	case uint32:
		v = Value{Numeric(strconv.AppendUint(nil, uint64(bindVal), 10))}
	case uint64:
		v = Value{Numeric(strconv.AppendUint(nil, uint64(bindVal), 10))}
	case float64:
		v = Value{Fractional(strconv.AppendFloat(nil, bindVal, 'f', -1, 64))}
	case string:
		v = Value{String([]byte(bindVal))}
	case []byte:
		v = Value{String(bindVal)}
	case time.Time:
		v = Value{String([]byte(bindVal.Format("2006-01-02 15:04:05")))}
	case Numeric, Fractional, String:
		v = Value{bindVal.(InnerValue)}
	case Value:
		v = bindVal
	default:
		return Value{}, fmt.Errorf("unsupported bind variable type %T: %v", goval, goval)
	}
	return v, nil
}

// BuildNumeric builds a Numeric type that represents any whole number.
// It normalizes the representation to ensure 1:1 mapping between the
// number and its representation.
func BuildNumeric(val string) (n Value, err error) {
	if val[0] == '-' || val[0] == '+' {
		signed, err := strconv.ParseInt(val, 0, 64)
		if err != nil {
			return Value{}, err
		}
		n = Value{Numeric(strconv.AppendInt(nil, signed, 10))}
	} else {
		unsigned, err := strconv.ParseUint(val, 0, 64)
		if err != nil {
			return Value{}, err
		}
		n = Value{Numeric(strconv.AppendUint(nil, unsigned, 10))}
	}
	return n, nil
}

func (n Numeric) raw() []byte {
	return []byte(n)
}

func (n Numeric) encodeSql(b BinWriter) {
	if _, err := b.Write(n.raw()); err != nil {
		panic(err)
	}
}

func (n Numeric) encodeAscii(b BinWriter) {
	if _, err := b.Write(n.raw()); err != nil {
		panic(err)
	}
}

func (n Numeric) MarshalJSON() ([]byte, error) {
	return n.raw(), nil
}

func (f Fractional) raw() []byte {
	return []byte(f)
}

func (f Fractional) encodeSql(b BinWriter) {
	if _, err := b.Write(f.raw()); err != nil {
		panic(err)
	}
}

func (f Fractional) encodeAscii(b BinWriter) {
	if _, err := b.Write(f.raw()); err != nil {
		panic(err)
	}
}

func (s String) MarshalJSON() ([]byte, error) {
	return json.Marshal(string(s.raw()))
}

func (s String) raw() []byte {
	return []byte(s)
}

func (s String) encodeSql(b BinWriter) {
	writebyte(b, '\'')
	for _, ch := range s.raw() {
		if encodedChar := SqlEncodeMap[ch]; encodedChar == DONTESCAPE {
			writebyte(b, ch)
		} else {
			writebyte(b, '\\')
			writebyte(b, encodedChar)
		}
	}
	writebyte(b, '\'')
}

func (s String) encodeAscii(b BinWriter) {
	writebyte(b, '\'')
	encoder := base64.NewEncoder(base64.StdEncoding, b)
	encoder.Write(s.raw())
	encoder.Close()
	writebyte(b, '\'')
}

func writebyte(b BinWriter, c byte) {
	if err := b.WriteByte(c); err != nil {
		panic(err)
	}
}

// SqlEncodeMap specifies how to escape binary data with '\'.
// Complies to http://dev.mysql.com/doc/refman/5.1/en/string-syntax.html
var SqlEncodeMap [256]byte

// SqlDecodeMap is the reverse of SqlEncodeMap
var SqlDecodeMap [256]byte

var encodeRef = map[byte]byte{
	'\x00': '0',
	'\'':   '\'',
	'"':    '"',
	'\b':   'b',
	'\n':   'n',
	'\r':   'r',
	'\t':   't',
	26:     'Z', // ctl-Z
	'\\':   '\\',
}

func init() {
	for i := range SqlEncodeMap {
		SqlEncodeMap[i] = DONTESCAPE
		SqlDecodeMap[i] = DONTESCAPE
	}
	for i := range SqlEncodeMap {
		if to, ok := encodeRef[byte(i)]; ok {
			SqlEncodeMap[byte(i)] = to
			SqlDecodeMap[to] = byte(i)
		}
	}
	gob.Register(Numeric(nil))
	gob.Register(Fractional(nil))
	gob.Register(String(nil))
}
```

## File: `sqlparser/sqltypes/type_test.go`
```go
// Copyright 2012, Google Inc. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package sqltypes

import (
	"bytes"
	"testing"
	"time"
)

func TestNull(t *testing.T) {
	n := Value{}
	if !n.IsNull() {
		t.Errorf("value is not null")
	}
	if n.String() != "" {
		t.Errorf("Expecting '', got %s", n.String())
	}
	b := bytes.NewBuffer(nil)
	n.EncodeSql(b)
	if b.String() != "null" {
		t.Errorf("Expecting null, got %s", b.String())
	}
	n.EncodeAscii(b)
	if b.String() != "nullnull" {
		t.Errorf("Expecting nullnull, got %s", b.String())
	}
	js, err := n.MarshalJSON()
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if string(js) != "null" {
		t.Errorf("Expecting null, received %s", js)
	}
}

func TestNumeric(t *testing.T) {
	n := Value{Numeric([]byte("1234"))}
	b := bytes.NewBuffer(nil)
	n.EncodeSql(b)
	if b.String() != "1234" {
		t.Errorf("Expecting 1234, got %s", b.String())
	}
	n.EncodeAscii(b)
	if b.String() != "12341234" {
		t.Errorf("Expecting 12341234, got %s", b.String())
	}
	js, err := n.MarshalJSON()
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if string(js) != "1234" {
		t.Errorf("Expecting 1234, received %s", js)
	}
}

func TestTime(t *testing.T) {
	date := time.Date(1999, 1, 2, 3, 4, 5, 0, time.UTC)
	v, _ := BuildValue(date)
	if !v.IsString() || v.String() != "1999-01-02 03:04:05" {
		t.Errorf("Expecting 1999-01-02 03:04:05, got %s", v.String())
	}

	b := &bytes.Buffer{}
	v.EncodeSql(b)
	if b.String() != "'1999-01-02 03:04:05'" {
		t.Errorf("Expecting '1999-01-02 03:04:05', got %s", b.String())
	}
}

const (
	INVALIDNEG = "-9223372036854775809"
	MINNEG     = "-9223372036854775808"
	MAXPOS     = "18446744073709551615"
	INVALIDPOS = "18446744073709551616"
	NEGFLOAT   = "1.234"
	POSFLOAT   = "-1.234"
)

func TestBuildNumeric(t *testing.T) {
	var n Value
	var err error
	n, err = BuildNumeric(MINNEG)
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if n.String() != MINNEG {
		t.Errorf("Expecting %v, received %s", MINNEG, n.Raw())
	}
	n, err = BuildNumeric(MAXPOS)
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if n.String() != MAXPOS {
		t.Errorf("Expecting %v, received %s", MAXPOS, n.Raw())
	}
	n, err = BuildNumeric("0xA")
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if n.String() != "10" {
		t.Errorf("Expecting %v, received %s", 10, n.Raw())
	}
	n, err = BuildNumeric("012")
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if string(n.Raw()) != "10" {
		t.Errorf("Expecting %v, received %s", 10, n.Raw())
	}
	if n, err = BuildNumeric(INVALIDNEG); err == nil {
		t.Errorf("Expecting error")
	}
	if n, err = BuildNumeric(INVALIDPOS); err == nil {
		t.Errorf("Expecting error")
	}
	if n, err = BuildNumeric(NEGFLOAT); err == nil {
		t.Errorf("Expecting error")
	}
	if n, err = BuildNumeric(POSFLOAT); err == nil {
		t.Errorf("Expecting error")
	}
}

const (
	HARDSQL     = "\x00'\"\b\n\r\t\x1A\\"
	HARDESCAPED = "'\\0\\'\\\"\\b\\n\\r\\t\\Z\\\\'"
	HARDASCII   = "'ACciCAoNCRpc'"
)

func TestString(t *testing.T) {
	s := Value{String([]byte(HARDSQL))}
	b := bytes.NewBuffer(nil)
	s.EncodeSql(b)
	if b.String() != HARDESCAPED {
		t.Errorf("Expecting %s, received %s", HARDESCAPED, b.String())
	}
	b = bytes.NewBuffer(nil)
	s.EncodeAscii(b)
	if b.String() != HARDASCII {
		t.Errorf("Expecting %s, received %#v", HARDASCII, b.String())
	}
	s = Value{String([]byte("ab\x01cd"))}
	js, err := s.MarshalJSON()
	if err != nil {
		t.Errorf("Unexpected error: %s", err)
	}
	if got, want := string(js), "\"ab\\u0001cd\""; got != want {
		t.Errorf("%#v.MarshalJSON() = %#v, want %#v", s, got, want)
	}
}

func TestBuildValue(t *testing.T) {
	v, err := BuildValue(nil)
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNull() {
		t.Errorf("Expecting null")
	}
	n64, err := v.ParseUint64()
	if err == nil || err.Error() != "value is null" {
		t.Errorf("%v", err)
	}
	v, err = BuildValue(int(-1))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNumeric() || v.String() != "-1" {
		t.Errorf("Expecting -1, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(int32(-1))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNumeric() || v.String() != "-1" {
		t.Errorf("Expecting -1, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(int64(-1))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNumeric() || v.String() != "-1" {
		t.Errorf("Expecting -1, received %T: %s", v.Inner, v.String())
	}
	n64, err = v.ParseUint64()
	if err == nil {
		t.Errorf("-1 shouldn't convert into uint64")
	}
	i64, err := v.ParseInt64()
	if i64 != -1 {
		t.Errorf("want -1, got %d", i64)
	}
	if err != nil {
		t.Errorf("%v", err)
	}
	v, err = BuildValue(uint(1))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNumeric() || v.String() != "1" {
		t.Errorf("Expecting 1, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(uint32(1))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNumeric() || v.String() != "1" {
		t.Errorf("Expecting 1, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(uint64(1))
	if err != nil {
		t.Errorf("%v", err)
	}
	n64, err = v.ParseUint64()
	if err != nil {
		t.Errorf("%v", err)
	}
	if n64 != 1 {
		t.Errorf("Expecting 1, got %v", n64)
	}
	if !v.IsNumeric() || v.String() != "1" {
		t.Errorf("Expecting 1, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(1.23)
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsFractional() || v.String() != "1.23" {
		t.Errorf("Expecting 1.23, received %T: %s", v.Inner, v.String())
	}
	n64, err = v.ParseUint64()
	if err == nil {
		t.Errorf("1.23 shouldn't convert into uint64")
	}
	v, err = BuildValue("abcd")
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsString() || v.String() != "abcd" {
		t.Errorf("Expecting abcd, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue([]byte("abcd"))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsString() || v.String() != "abcd" {
		t.Errorf("Expecting abcd, received %T: %s", v.Inner, v.String())
	}
	n64, err = v.ParseUint64()
	if err == nil || err.Error() != "value is not Numeric" {
		t.Errorf("%v", err)
	}
	v, err = BuildValue(time.Date(2012, time.February, 24, 23, 19, 43, 10, time.UTC))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsString() || v.String() != "2012-02-24 23:19:43" {
		t.Errorf("Expecting 2012-02-24 23:19:43, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(Numeric([]byte("123")))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsNumeric() || v.String() != "123" {
		t.Errorf("Expecting 123, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(Fractional([]byte("12.3")))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsFractional() || v.String() != "12.3" {
		t.Errorf("Expecting 12.3, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(String([]byte("abc")))
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsString() || v.String() != "abc" {
		t.Errorf("Expecting abc, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(float32(1.23))
	if err == nil {
		t.Errorf("Did not receive error")
	}
	v1 := Value{String([]byte("ab"))}
	v, err = BuildValue(v1)
	if err != nil {
		t.Errorf("%v", err)
	}
	if !v.IsString() || v.String() != "ab" {
		t.Errorf("Expecting ab, received %T: %s", v.Inner, v.String())
	}
	v, err = BuildValue(float32(1.23))
	if err == nil {
		t.Errorf("Did not receive error")
	}
}

// Ensure DONTESCAPE is not escaped
func TestEncode(t *testing.T) {
	if SqlEncodeMap[DONTESCAPE] != DONTESCAPE {
		t.Errorf("Encode fail: %v", SqlEncodeMap[DONTESCAPE])
	}
	if SqlDecodeMap[DONTESCAPE] != DONTESCAPE {
		t.Errorf("Decode fail: %v", SqlDecodeMap[DONTESCAPE])
	}
}
```

## File: `vault/sqlite.go`
```go
package storage

import (
	"bytes"
	"database/sql"
	"path"
	"strings"

	"log"
	"regexp"

	"github.com/dinedal/textql/inputs"
	"github.com/dinedal/textql/sqlparser"

	sqlite3 "github.com/mattn/go-sqlite3"
)

// SQLite3Storage represents a TextQL compatible SQL backend based on in-memory SQLite3
type SQLite3Storage struct {
	options        *SQLite3Options
	db             *sql.DB
	connID         int
	firstTableName string
}

// SQLite3Options are options passed into SQLite3 connection as needed.
type SQLite3Options struct{}

var (
	sqlite3conn          = []*sqlite3.SQLiteConn{}
	allWhiteSpace        = regexp.MustCompile("^\\s+$")
	tableNameCheckRegEx  = regexp.MustCompile(`.*\[.*\].*`)
	columnNameCheckRegEx = regexp.MustCompile(`.*\[.*\].*`)
)

type entrypoint struct {
	lib  string
	proc string
}

var libNames = []entrypoint{
	{"libgo-sqlite3-extension-functions.so", "sqlite3_extension_init"},
	{"libgo-sqlite3-extension-functions.dylib", "sqlite3_extension_init"},
	{"libgo-sqlite3-extension-functions.dll", "sqlite3_extension_init"},
}

func init() {
	sql.Register("sqlite3_textql",
		&sqlite3.SQLiteDriver{
			ConnectHook: func(conn *sqlite3.SQLiteConn) error {
				for _, v := range libNames {
					conn.LoadExtension(v.lib, v.proc)
				}
				sqlite3conn = append(sqlite3conn, conn)
				return conn.RegisterFunc("regexp", regExp, true)
			},
		})
}

// NewSQLite3StorageWithDefaults returns a SQLite3Storage with the default options.
func NewSQLite3StorageWithDefaults() *SQLite3Storage {
	return NewSQLite3Storage(&SQLite3Options{})
}

// NewSQLite3Storage returns a SQLite3Storage with the SQLite3Options provided applied.
func NewSQLite3Storage(opts *SQLite3Options) *SQLite3Storage {
	sqlite3Storage := &SQLite3Storage{
		options:        opts,
		firstTableName: "",
	}

	sqlite3Storage.open()
	return sqlite3Storage
}

func (sqlite3Storage *SQLite3Storage) open() {
	db, err := sql.Open("sqlite3_textql", ":memory:")

	if err != nil {
		log.Fatalln(err)
	}

	err = db.Ping()

	if err != nil {
		log.Fatalln(err)
	}

	sqlite3Storage.connID = len(sqlite3conn) - 1
	sqlite3Storage.db = db
}

// LoadInput reads the entire Input provided into a table named after the Input name.
// The name is cooreced into a valid SQLite3 table name prior to use.
func (sqlite3Storage *SQLite3Storage) LoadInput(input inputs.Input) {
	tableName := strings.Replace(input.Name(), path.Ext(input.Name()), "", -1)
	sqlite3Storage.createTable(tableName, input.Header(), false)

	tx, txErr := sqlite3Storage.db.Begin()

	if txErr != nil {
		log.Fatalln(txErr)
	}

	stmt := sqlite3Storage.createLoadStmt(tableName, len(input.Header()), tx)

	row := input.ReadRecord()
	for {
		if row == nil {
			break
		}
		sqlite3Storage.loadRow(tableName, len(input.Header()), row, tx, stmt, true)
		row = input.ReadRecord()
	}
	stmt.Close()
	tx.Commit()

	if sqlite3Storage.firstTableName == "" {
		sqlite3Storage.firstTableName = tableName
	}
}

func (sqlite3Storage *SQLite3Storage) createTable(tableName string, columnNames []string, verbose bool) error {
	var buffer bytes.Buffer

	if tableNameCheckRegEx.FindString(tableName) != "" {
		log.Fatalln("Invalid table name", tableName)
	}

	buffer.WriteString("CREATE TABLE IF NOT EXISTS [" + (tableName) + "] (")

	for i, col := range columnNames {
		if columnNameCheckRegEx.FindString(col) != "" {
			log.Fatalln("Invalid table name", col)
		}

		buffer.WriteString("[" + col + "] NUMERIC")

		if i != len(columnNames)-1 {
			buffer.WriteString(", ")
		}
	}

	buffer.WriteString(");")

	_, err := sqlite3Storage.db.Exec(buffer.String())

	if err != nil {
		log.Fatalln(err)
	}

	if verbose {
		log.Println(buffer.String())
	}

	return err
}

func (sqlite3Storage *SQLite3Storage) createLoadStmt(tableName string, colCount int, db *sql.Tx) *sql.Stmt {
	if colCount == 0 {
		log.Fatalln("Nothing to build insert with!")
	}
	var buffer bytes.Buffer

	buffer.WriteString("INSERT INTO [" + (tableName) + "] VALUES (")
	// Don't write the comma for the last column
	for i := 1; i <= colCount; i++ {
		buffer.WriteString("nullif(?,'')")
		if i != colCount {
			buffer.WriteString(", ")
		}
	}

	buffer.WriteString(");")

	stmt, err := db.Prepare(buffer.String())

	if err != nil {
		log.Fatalln(err)
	}
	return stmt
}

func (sqlite3Storage *SQLite3Storage) loadRow(tableName string, colCount int, values []string, db *sql.Tx, stmt *sql.Stmt, verbose bool) error {
	if len(values) == 0 || colCount == 0 {
		return nil
	}

	var vals []interface{}

	for i := 0; i < colCount; i++ {
		if allWhiteSpace.MatchString(values[i]) {
			vals = append(vals, "")
		} else {
			vals = append(vals, values[i])
		}
	}

	_, err := stmt.Exec(vals...)

	if err != nil && verbose {
		log.Printf("Bad row: %v\n", err)
	}

	return err
}

// ExecuteSQLString maps the sqlQuery provided from short hand TextQL to SQL, then
// applies the query to the sqlite3 in memory database, and lastly returns the sql.Rows
// that resulted from the executing query.
func (sqlite3Storage *SQLite3Storage) ExecuteSQLString(sqlQuery string) (*sql.Rows, error) {
	var result *sql.Rows
	var err error

	if strings.Trim(sqlQuery, " ") != "" {
		implictFromSQL := sqlparser.Magicify(sqlQuery, sqlite3Storage.firstTableName)
		result, err = sqlite3Storage.db.Query(implictFromSQL)
		if err != nil {
			return nil, err
		}
	}

	return result, nil
}

// Exec maps the sqlQuery provided from short hand TextQL to SQL, then
// applies the query to the sqlite3 in memory database, and lastly returns the sql.Result
// that resulted from the executing query.
func (sqlite3Storage *SQLite3Storage) Exec(sqlQuery string) (sql.Result, error) {
	var result sql.Result
	var err error

	if strings.Trim(sqlQuery, " ") != "" {
		implictFromSQL := sqlparser.Magicify(sqlQuery, sqlite3Storage.firstTableName)
		result, err = sqlite3Storage.db.Exec(implictFromSQL)
		if err != nil {
			return nil, err
		}
	}

	return result, nil
}

// SaveTo saves the current in memory database to the path provided as a string.
func (sqlite3Storage *SQLite3Storage) SaveTo(path string) error {
	backupDb, openErr := sql.Open("sqlite3_textql", path)
	if openErr != nil {
		return openErr
	}

	backupPingErr := backupDb.Ping()
	if backupPingErr != nil {
		return backupPingErr
	}
	backupConnID := len(sqlite3conn) - 1

	backup, backupStartErr := sqlite3conn[backupConnID].Backup("main", sqlite3conn[sqlite3Storage.connID], "main")
	if backupStartErr != nil {
		return backupStartErr
	}

	_, backupPerformError := backup.Step(-1)
	if backupPerformError != nil {
		return backupPerformError
	}

	backupFinishError := backup.Finish()
	if backupFinishError != nil {
		return backupFinishError
	}

	backupCloseError := backupDb.Close()
	if backupCloseError != nil {
		return backupCloseError
	}

	return nil
}

// Close will close the current database
func (sqlite3Storage *SQLite3Storage) Close() {
	sqlite3Storage.db.Close()
}
```

## File: `vault/sqlite_regexp.go`
```go
package storage

import "regexp"

func regExp(re, s string) (bool, error) {
	return regexp.MatchString(re, s)
}
```

## File: `vault/sqlite_test.go`
```go
package storage

import (
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"testing"

	"github.com/dinedal/textql/inputs"
	"github.com/dinedal/textql/test_util"
)

var (
	storageOpts = &SQLite3Options{}
	simpleCSV   = `a,b,c
1,2,3
4,5,6`
	whitespaceValuesCSV = `a,b,c
  , ,
1,2,3
4,5,6`
)

func NewTestCSVInput() (input inputs.Input, fp *os.File) {
	fp = test_util.OpenFileFromString(simpleCSV)

	opts := &inputs.CSVInputOptions{
		HasHeader: true,
		Separator: ',',
		ReadFrom:  fp,
	}

	newInput, _ := inputs.NewCSVInput(opts)
	return newInput, fp
}

func TestSQLiteStorageLoadInput(t *testing.T) {
	storage := NewSQLite3Storage(storageOpts)
	input, fp := NewTestCSVInput()
	defer fp.Close()
	defer os.Remove(fp.Name())
	defer storage.Close()

	storage.LoadInput(input)
}

func TestSQLiteStorageSaveTo(t *testing.T) {
	var (
		cmdOut   []byte
		err      error
		tempFile *os.File
	)

	storage := NewSQLite3Storage(storageOpts)
	input, fp := NewTestCSVInput()
	defer fp.Close()
	defer os.Remove(fp.Name())
	defer storage.Close()

	storage.LoadInput(input)

	tempFile, err = ioutil.TempFile(os.TempDir(), "textql_test")

	if err != nil {
		t.Fatalf(err.Error())
	}

	defer os.Remove(tempFile.Name())
	tempFile.Close()
	storage.SaveTo(tempFile.Name())
	storage.Close()

	args := []string{tempFile.Name(), "pragma integrity_check;"}

	cmd := exec.Command("sqlite3", args...)
	cmd.Stderr = os.Stderr
	cmd.Stdin = os.Stdin

	if cmdOut, err = cmd.Output(); err != nil {
		fmt.Println(string(cmdOut))
		fmt.Println(args)
		t.Fatalf(err.Error())
	}
	cmdOutStr := string(cmdOut)

	if cmdOutStr != "ok\n" {
		fmt.Println(cmdOutStr)
		t.Fatalf("SaveTo integrity check failed!")
	}
}

func TestSQLiteStorageExecuteSQLStringNormalSQL(t *testing.T) {
	storage := NewSQLite3Storage(storageOpts)
	input, fp := NewTestCSVInput()
	defer fp.Close()
	defer os.Remove(fp.Name())
	defer storage.Close()

	storage.LoadInput(input)

	sqlString := "select count(*) from " + storage.firstTableName

	rows, rowsErr := storage.ExecuteSQLString(sqlString)

	if rowsErr != nil {
		t.Fatalf(rowsErr.Error())
	}

	cols, colsErr := rows.Columns()

	if colsErr != nil {
		t.Fatalf(colsErr.Error())
	}

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	var dest int

	for rows.Next() {
		rows.Scan(&dest)
		if dest != 2 {
			t.Fatalf("Expected 2 rows counted, got (%v)", dest)
		}
	}
}

func TestSQLiteStorageExecuteSQLStringMissingSelect(t *testing.T) {
	storage := NewSQLite3Storage(storageOpts)
	input, fp := NewTestCSVInput()
	defer fp.Close()
	defer os.Remove(fp.Name())
	defer storage.Close()

	storage.LoadInput(input)

	sqlString := "count(*) from " + storage.firstTableName

	rows, rowsErr := storage.ExecuteSQLString(sqlString)

	if rowsErr != nil {
		t.Fatalf(rowsErr.Error())
	}

	cols, colsErr := rows.Columns()

	if colsErr != nil {
		t.Fatalf(colsErr.Error())
	}

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	var dest int

	for rows.Next() {
		rows.Scan(&dest)
		if dest != 2 {
			t.Fatalf("Expected 2 rows counted, got (%v)", dest)
		}
	}
}

func LoadTestDataAndExecuteQuery(t *testing.T, testData string, sqlString string) (map[int]map[string]interface{}, []string) {
	storage := NewSQLite3Storage(storageOpts)
	fp := test_util.OpenFileFromString(testData)

	opts := &inputs.CSVInputOptions{
		HasHeader: true,
		Separator: ',',
		ReadFrom:  fp,
	}

	input, _ := inputs.NewCSVInput(opts)
	defer fp.Close()
	defer os.Remove(fp.Name())
	defer storage.Close()

	storage.LoadInput(input)

	rows, rowsErr := storage.ExecuteSQLString(sqlString)

	if rowsErr != nil {
		t.Fatalf(rowsErr.Error())
	}

	cols, colsErr := rows.Columns()

	if colsErr != nil {
		t.Fatalf(colsErr.Error())
	}

	rowNumber := 0
	result := make(map[int]map[string]interface{})
	rawResult := make([]interface{}, len(cols))
	dest := make([]interface{}, len(cols))

	for i := range cols {
		dest[i] = &rawResult[i]
	}

	for rows.Next() {
		scanErr := rows.Scan(dest...)

		if scanErr != nil {
			t.Fatalf(scanErr.Error())
		}

		result[rowNumber] = make(map[string]interface{})
		for i, raw := range rawResult {
			result[rowNumber][cols[i]] = raw
		}
		rowNumber++
	}

	return result, cols
}

func TestSQLiteStorageExecuteSQLStringMissingFromOuterQuery(t *testing.T) {
	data, cols := LoadTestDataAndExecuteQuery(t, simpleCSV, "count(*)")

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	intVal := data[0]["count(*)"].(int64)
	if intVal != 2 {
		t.Fatalf("Expected 2 rows counted, got (%v)", intVal)
	}
}

func TestSQLiteStorageExecuteSQLStringMissingFromSubQuery(t *testing.T) {
	data, cols := LoadTestDataAndExecuteQuery(t, simpleCSV, "count(*) from (select *)")

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	intVal := data[0]["count(*)"].(int64)
	if intVal != 2 {
		t.Fatalf("Expected 2 rows counted, got (%v)", intVal)
	}
}

func TestWhitespaceLoadsAsNull(t *testing.T) {
	data, cols := LoadTestDataAndExecuteQuery(t, whitespaceValuesCSV, "max(a)")

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	intVal := data[0]["max(a)"].(int64)
	if intVal != 4 {
		t.Fatalf("Expected 4 max value, got (%v)", intVal)
	}

	data, cols = LoadTestDataAndExecuteQuery(t, whitespaceValuesCSV, "typeof(a)")

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	strval := data[0]["typeof(a)"].(string)
	if strval != "null" {
		t.Fatalf("Expected null value, got (%v)", strval)
	}

	strval = data[1]["typeof(a)"].(string)
	if strval != "integer" {
		t.Fatalf("Expected integer value, got (%v)", strval)
	}

	strval = data[2]["typeof(a)"].(string)
	if strval != "integer" {
		t.Fatalf("Expected integer value, got (%v)", strval)
	}

	data, cols = LoadTestDataAndExecuteQuery(t, whitespaceValuesCSV, "max(b)")

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	intVal = data[0]["max(b)"].(int64)
	if intVal != 5 {
		t.Fatalf("Expected 5 max value, got (%v)", intVal)
	}

	data, cols = LoadTestDataAndExecuteQuery(t, whitespaceValuesCSV, "typeof(b)")

	if len(cols) != 1 {
		t.Fatalf("Expected 1 column, got (%v)", len(cols))
	}

	strval = data[0]["typeof(b)"].(string)
	if strval != "null" {
		t.Fatalf("Expected null value, got (%v)", strval)
	}

	strval = data[1]["typeof(b)"].(string)
	if strval != "integer" {
		t.Fatalf("Expected integer value, got (%v)", strval)
	}

	strval = data[2]["typeof(b)"].(string)
	if strval != "integer" {
		t.Fatalf("Expected integer value, got (%v)", strval)
	}
}

func TestSQLiteStorageExec(t *testing.T) {
	storage := NewSQLite3Storage(storageOpts)
	input, fp := NewTestCSVInput()
	defer fp.Close()
	defer os.Remove(fp.Name())
	defer storage.Close()

	storage.LoadInput(input)

	sqlString := "insert into " + storage.firstTableName + " values (7,8,9)"

	result, resultErr := storage.Exec(sqlString)

	if resultErr != nil {
		t.Fatalf(resultErr.Error())
	}

	rowsAffected, rowsErr := result.RowsAffected()

	if rowsErr != nil {
		t.Fatalf(rowsErr.Error())
	}

	if rowsAffected != 1 {
		t.Fatalf("Expected 1 row affected, got (%v)", rowsAffected)
	}
}
```

## File: `vault/storage.go`
```go
package storage

import (
	"database/sql"

	"github.com/dinedal/textql/inputs"
)

// Storage implentors are expected to be SQL capable engines.
// A Storage should support loading data from a TextQL input,
// executing any number of SQL statements and returning their resultant
// sql.Rows, as well as supporting clean closing and "backing up" of
// data to a specific path
type Storage interface {
	// LoadInput should make all the data in the input accessible to queries.
	LoadInput(*inputs.Input)
	// SaveTo should write the entire database of the SQL backend to the path given as a string.
	// Failure in any way should return an error, and nil if the operation was successful.
	SaveTo(string) error
	// ExecuteSQLString should first convert from TextQL shorthand SQL to normal SQL,
	// apply the query or transformation given to the SQL backend and return either nil
	// or the sql.Rows that were returned from the query.
	ExecuteSQLString(string) (*sql.Rows, error)
	// Close should cleanly close the database backend, cleaning up data on disk if required.
	Close()
}
```

## File: `test_util/test_util.go`
```go
package test_util

import (
	"io/ioutil"
	"os"
)

func OpenFileFromString(contents string) *os.File {
	f, _ := ioutil.TempFile("./", "csv")
	f.WriteString(contents)
	f.Seek(0, 0)
	return f
}
```

## File: `textql/main.go`
```go
package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"strings"

	"github.com/dinedal/textql/inputs"
	"github.com/dinedal/textql/outputs"
	"github.com/dinedal/textql/storage"
	"github.com/dinedal/textql/util"
)

type commandLineOptions struct {
	Statements      *string
	StatementsFile  *string
	SourceFile      *string
	Delimiter       *string
	Header          *bool
	OutputHeader    *bool
	OutputDelimiter *string
	OutputFile      *string
	SaveTo          *string
	Console         *bool
	Version         *bool
	Quiet           *bool
	Pretty          *bool
}

// Must be set at build via -ldflags "-X main.VERSION=`cat VERSION`"
var VERSION string

func newCommandLineOptions() *commandLineOptions {
	cmdLineOpts := commandLineOptions{}
	cmdLineOpts.Statements = flag.String("sql", "", "SQL Statement(s) to run on the data")
	cmdLineOpts.StatementsFile = flag.String("sqlfile", "", "SQL filepath to run on the data")
	cmdLineOpts.Delimiter = flag.String("dlm", ",", "Input delimiter character between fields -dlm=tab for tab, -dlm=0x## to specify a character code in hex")
	cmdLineOpts.Header = flag.Bool("header", false, "Treat input files as having the first row as a header row")
	cmdLineOpts.OutputHeader = flag.Bool("output-header", false, "Display column names in output")
	cmdLineOpts.OutputDelimiter = flag.String("output-dlm", ",", "Output delimiter character between fields -output-dlm=tab for tab, -dlm=0x## to specify a character code in hex")
	cmdLineOpts.OutputFile = flag.String("output-file", "stdout", "Filename to write output to, if empty no output is written")
	cmdLineOpts.SaveTo = flag.String("save-to", "", "SQLite3 db is left on disk at this file")
	cmdLineOpts.Console = flag.Bool("console", false, "After all statements are run, open SQLite3 REPL with this data")
	cmdLineOpts.Version = flag.Bool("version", false, "Print version and exit")
	cmdLineOpts.Quiet = flag.Bool("quiet", false, "Surpress logging")
	cmdLineOpts.Pretty = flag.Bool("pretty", false, "Output pretty formatting")
	flag.Usage = cmdLineOpts.Usage
	flag.Parse()

	return &cmdLineOpts
}

func (clo *commandLineOptions) GetStatements() (string, *error) {
	if clo.Statements == nil && clo.StatementsFile == nil {
		err := fmt.Errorf("No SQL statements provided")
		return "", &err
	}
	if clo.Statements != nil && *clo.Statements != "" {
		return *clo.Statements, nil
	}
	filepath := *clo.StatementsFile
	dat, err := os.ReadFile(filepath)
	if err != nil {
		return "", &err
	}
	return string(dat), nil
}

func (clo *commandLineOptions) GetSourceFiles() []string {
	return flag.Args()
}

func (clo *commandLineOptions) GetDelimiter() string {
	return *clo.Delimiter
}

func (clo *commandLineOptions) GetHeader() bool {
	return *clo.Header
}

func (clo *commandLineOptions) GetOutputHeader() bool {
	return *clo.OutputHeader
}

func (clo *commandLineOptions) GetOutputDelimiter() string {
	return *clo.OutputDelimiter
}

func (clo *commandLineOptions) GetOutputFile() string {
	return *clo.OutputFile
}

func (clo *commandLineOptions) GetSaveTo() string {
	return util.CleanPath(*clo.SaveTo)
}

func (clo *commandLineOptions) GetConsole() bool {
	return *clo.Console
}

func (clo *commandLineOptions) GetVersion() bool {
	return *clo.Version
}

func (clo *commandLineOptions) GetQuiet() bool {
	return *clo.Quiet
}

func (clo *commandLineOptions) GetPretty() bool {
	return *clo.Pretty
}

func (clo *commandLineOptions) Usage() {
	if !clo.GetQuiet() {
		fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "\n")
		fmt.Fprintf(os.Stderr, "  %s [-console] [-save-to path path] [-output-file path] [-output-dlm delimter] [-output-header] [-pretty] [-quiet] [-header] [-dlm delimter] [-sql sql_statements] [path ...] \n", os.Args[0])
		fmt.Fprintf(os.Stderr, "\n")
		flag.PrintDefaults()
	}
}

func handleSemiColon(sqlStrings *[]string) []string {
	var stack []string
	var current string
	index := 0
	current = (*sqlStrings)[index]
	for {
		if current == "" {
			current = (*sqlStrings)[index]
		}
		count := strings.Count(current, "'")
		if count%2 == 1 {
			current = current + ";" + (*sqlStrings)[index+1]
		} else {
			stack = append(stack, current)
			current = ""
		}
		index++
		if index == len((*sqlStrings)) {
			break
		}
	}
	return stack
}

func main() {
	cmdLineOpts := newCommandLineOptions()
	var outputer outputs.Output

	if cmdLineOpts.GetVersion() {
		fmt.Println(VERSION)
		os.Exit(0)
	}

	if len(cmdLineOpts.GetSourceFiles()) == 0 && !util.IsThereDataOnStdin() {
		cmdLineOpts.Usage()
	}

	if cmdLineOpts.GetQuiet() {
		log.SetOutput(ioutil.Discard)
	}

	if cmdLineOpts.GetConsole() {
		if util.IsThereDataOnStdin() {
			log.Fatalln("Can not open console with pipe input, read a file instead")
		}
		_, sqlite3ConsolePathErr := exec.LookPath("sqlite3")
		if sqlite3ConsolePathErr != nil {
			log.Fatalln("Console requested but unable to locate `sqlite3` program on $PATH")
		}
	}

	var inputSources []string

	if util.IsThereDataOnStdin() {
		inputSources = append(inputSources, "stdin")
	}

	for _, taggedName := range cmdLineOpts.GetSourceFiles() {
		// support <tablename>:<filename> syntax
		var names = strings.SplitN(taggedName, ":", 2)
		var sourceFile = names[len(names)-1]

		if util.IsPathDir(sourceFile) {
			for _, file := range util.AllFilesInDirectory(sourceFile) {
				inputSources = append(inputSources, file)
			}
		} else {
			inputSources = append(inputSources, taggedName)
		}
	}

	storage := storage.NewSQLite3StorageWithDefaults()

	for _, taggedName := range inputSources {
		// support <tablename>:<filename> syntax
		var names = strings.SplitN(taggedName, ":", 2)
		var file = names[len(names)-1]

		fp := util.OpenFileOrStdDev(file, false)

		inputOpts := &inputs.CSVInputOptions{
			HasHeader: cmdLineOpts.GetHeader(),
			Separator: util.DetermineSeparator(cmdLineOpts.GetDelimiter()),
			ReadFrom:  fp,
		}

		input, inputErr := inputs.NewCSVInput(inputOpts)

		if inputErr != nil {
			log.Printf("Unable to load %v\n", file)
		}

		if len(names) > 1 {
			input.SetName(names[0])
		}
		storage.LoadInput(input)
	}

	stat, err := cmdLineOpts.GetStatements()
	if err != nil {
		log.Fatalln(err)
	}
	if (strings.Count(stat, "'") % 2) == 1 {
		log.Fatalln("String contains odd number of \"'(Single Quotes)\"")
	}

	sqlStrings := strings.Split(stat, ";")

	sqlStrings = handleSemiColon(&sqlStrings)

	if cmdLineOpts.GetOutputFile() != "" {
		if cmdLineOpts.GetPretty() {
			displayOpts := &outputs.PrettyCSVOutputOptions{
				WriteHeader: cmdLineOpts.GetOutputHeader(),
				WriteTo:     util.OpenFileOrStdDev(cmdLineOpts.GetOutputFile(), true),
			}

			outputer = outputs.NewPrettyCSVOutput(displayOpts)
		} else {
			displayOpts := &outputs.CSVOutputOptions{
				WriteHeader: cmdLineOpts.GetOutputHeader(),
				Separator:   util.DetermineSeparator(cmdLineOpts.GetOutputDelimiter()),
				WriteTo:     util.OpenFileOrStdDev(cmdLineOpts.GetOutputFile(), true),
			}

			outputer = outputs.NewCSVOutput(displayOpts)
		}
	}

	for _, sqlQuery := range sqlStrings {
		queryResults, queryErr := storage.ExecuteSQLString(sqlQuery)

		if queryErr != nil {
			log.Fatalln(queryErr)
		}

		if queryResults != nil && cmdLineOpts.GetOutputFile() != "" {
			outputer.Show(queryResults)
		}
	}

	if cmdLineOpts.GetSaveTo() != "" {
		storage.SaveTo(cmdLineOpts.GetSaveTo())
	}

	if cmdLineOpts.GetConsole() {
		var args []string

		if cmdLineOpts.GetOutputHeader() {
			args = []string{"-header"}
		} else {
			args = []string{}
		}

		if cmdLineOpts.GetSaveTo() != "" {
			args = append(args, cmdLineOpts.GetSaveTo())
		} else {
			tempFile, err := ioutil.TempFile(os.TempDir(), "textql")
			if err != nil {
				log.Fatalln(err)
			}
			defer os.Remove(tempFile.Name())
			tempFile.Close()
			saveErr := storage.SaveTo(tempFile.Name())

			if saveErr != nil {
				log.Fatalln(saveErr)
			}

			args = append(args, tempFile.Name())
		}

		cmd := exec.Command("sqlite3", args...)

		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmdErr := cmd.Run()

		if cmd.Process != nil {
			cmd.Process.Release()
		}

		if cmdErr != nil {
			log.Fatalln(cmdErr)
		}
	} else {
		storage.Close()
	}
}
```

## File: `util/file_helpers.go`
```go
package util

import (
	"io/ioutil"
	"log"
	"os"
	"os/user"
	"path/filepath"
	"strings"
)

func IsPathDir(path string) bool {
	fp, err := os.Open(CleanPath(path))

	if err != nil {
		log.Fatalln(err)
	}

	defer fp.Close()

	stat, statErr := fp.Stat()

	if statErr != nil {
		log.Fatalln(statErr)
	}

	return stat.IsDir()
}

func OpenFileOrStdDev(path string, write bool) *os.File {
	var fp *os.File
	var err error

	if path == "stdin" {
		fp = os.Stdin
		err = nil
	} else if path == "stdout" {
		fp = os.Stdout
		err = nil
	} else {
		if write {
			fp, err = os.Create(CleanPath(path))
		} else {
			fp, err = os.Open(CleanPath(path))
		}
	}

	if err != nil {
		log.Fatalln(err)
	}

	stat, statErr := fp.Stat()

	if statErr != nil {
		log.Fatalln(err)
	}

	if stat.IsDir() {
		log.Fatalf("%s: is a directory\n", path)
	}

	return fp
}

func CleanPath(path string) string {
	result := ""

	if path == "" {
		return ""
	}

	usr, err := user.Current()
	if err != nil {
		log.Fatalln(err)
	}

	if len(path) > 1 && path[:2] == "~/" {
		dir := usr.HomeDir + "/"
		result = strings.Replace(path, "~/", dir, 1)
	} else {
		result = path
	}

	absResult, absErr := filepath.Abs(result)
	if absErr != nil {
		log.Fatalln(absErr)
	}

	cleanResult := filepath.Clean(absResult)

	return cleanResult
}

func RewindFile(fileHandle *os.File) {
	_, rewindErr := fileHandle.Seek(0, 0)

	if rewindErr != nil {
		log.Fatalln("Unable to rewind file")
	}
}

func IsThereDataOnStdin() bool {
	stat, statErr := os.Stdin.Stat()

	if statErr != nil {
		log.Fatalln(statErr)
	}

	if (stat.Mode() & os.ModeCharDevice) == 0 {
		return true
	} else {
		return false
	}
}

func AllFilesInDirectory(path string) []string {
	cleanPath := CleanPath(path)
	directoryEntries, err := ioutil.ReadDir(cleanPath)
	result := make([]string, 0)

	if err != nil {
		log.Fatalln(err)
	}

	for _, entry := range directoryEntries {
		if !entry.IsDir() {
			result = append(result, filepath.Join(cleanPath, entry.Name()))
		}
	}

	return result
}
```

## File: `util/seperator_helpers.go`
```go
package util

import (
	"encoding/hex"
	"log"
	"strings"
	"unicode/utf8"
)

func DetermineSeparator(delimiter string) rune {
	var separator rune

	if delimiter == "tab" {
		separator = '\t'
	} else if strings.Index(delimiter, "0x") == 0 {
		dlm, hexErr := hex.DecodeString(delimiter[2:])

		if hexErr != nil {
			log.Fatalln(hexErr)
		}

		separator, _ = utf8.DecodeRuneInString(string(dlm))
	} else {
		separator, _ = utf8.DecodeRuneInString(delimiter)
	}
	return separator
}
```

