---
id: textql
type: knowledge
owner: OA_Triage
---
# textql
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: Readme.md
```md
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

### File: snapcraft.yaml
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

### File: TODO.txt
```txt
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
/github.com/dinedal/textql/storage/sqlite_test.go

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
Line 34
... [TRUNCATED]
```

### File: outputs\csv.go
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

### File: outputs\output.go
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

### File: outputs\pretty_csv.go
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

### File: storage\sqlite.go
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

### File: storage\sqlite_regexp.go
```go
package storage

import "regexp"

func regExp(re, s string) (bool, error) {
	return regexp.MatchString(re, s)
}

```

### File: storage\sqlite_test.go
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

### File: storage\storage.go
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

