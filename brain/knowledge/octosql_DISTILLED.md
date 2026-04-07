---
id: octosql
type: knowledge
owner: OA_Triage
---
# octosql
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<img src="https://raw.githubusercontent.com/cube2222/octosql/main/images/logo.png" width="168">OctoSQL
=======

OctoSQL is predominantly a CLI tool which lets you query a plethora of databases and file formats using SQL through a unified interface, even do JOINs between them. (Ever needed to join a JSON file with a PostgreSQL table? OctoSQL can help you with that.)

At the same time it's an easily extensible full-blown dataflow engine, and you can use it to add a SQL interface to your own applications.

[![GitHub](https://shields.io/github/actions/workflow/status/cube2222/octosql/test.yml?branch=main)](https://github.com/cube2222/octosql/actions/workflows/test.yml?query=branch%3Amain)
[![Go Report Card](https://goreportcard.com/badge/github.com/cube2222/octosql)](https://goreportcard.com/report/github.com/cube2222/octosql)
[![GoDoc](https://godoc.org/github.com/cube2222/octosql?status.svg)](https://godoc.org/github.com/cube2222/octosql)
[![License](https://shields.io/github/license/cube2222/octosql)](LICENSE)
[![Latest Version](https://shields.io/github/v/release/cube2222/octosql?display_name=tag&sort=semver)](https://github.com/cube2222/octosql/releases)
[![Gitter](https://badges.gitter.im/octosql/general.svg)](https://gitter.im/octosql/general?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

![Demo](images/octosql-demo.gif)

## Usage

```bash
octosql "SELECT * FROM ./myfile.json"
octosql "SELECT * FROM ./myfile.json" --describe  # Show the schema of the file.
octosql "SELECT invoices.id, address, amount
         FROM invoices.csv JOIN db.customers ON invoices.customer_id = customers.id
         ORDER BY amount DESC"
octosql "SELECT customer_id, SUM(amount)
         FROM invoices.csv
         GROUP BY customer_id"
```

OctoSQL supports a [bunch of file formats](#File-Access) out of the box, but you can additionally install plugins to add support for other databases.
```bash
octosql "SELECT * FROM plugins.available_plugins"
octosql plugin install postgres
echo "databases:
  - name: mydb
    type: postgres
    config:
      host: localhost
      port: 5443
      database: mydb
      user: postgres
      password: postgres" > octosql.yml
octosql "SELECT * FROM mydb.users" --describe
octosql "SELECT * FROM mydb.users"
```

You can specify the output format using the `--output` flag. Available values for it are `live_table`, `batch_table`, `csv` and `stream_native`.

The documentation about available aggregates and functions is contained within OctoSQL itself. It's in the `aggregates`, `aggregate_signatures`, `functions` and `function_signatures` tables in the `docs` database.
```bash
octosql "SELECT * FROM docs.functions fs"
+------------------+----------------------------------------+
|     fs.name      |             fs.description             |
+------------------+----------------------------------------+
| 'abs'            | 'Returns absolute value                |
|                  | of argument.'                          |
| 'ceil'           | 'Returns ceiling of                    |
|                  | argument.'                             |
| ...              | ...                                    |
+------------------+----------------------------------------+
```

## Installation

### Homebrew

You can install OctoSQL using Homebrew on MacOS or Linux:
```bash
brew install cube2222/octosql/octosql
```
After running it for the first time on MacOS you'll have to go into Preferences -> Security and Privacy -> Allow OctoSQL, as with any app that's not notarized.

### Pre-Compiled binary

You can also download the binary for your operating system directly from the [Releases page](https://github.com/cube2222/octosql/releases).

### Nix Package

The package can be installed in the local nix-profile.

```shell
nix-env -iA nixpkgs.octosql
```

For adhoc or testing purposes a shell with the package can be spawned.

```shell
nix-shell -p octosql
```

For NixOS users it is highly recommended to install the package by adding it to the list of `systemPackages`.

```nix
environment.systemPackages = with pkgs; [
  octosql
  # ...
];
```

### Building from source

With Go in version >= 1.18 the application can be built from source.
This can be achieved by cloning the repository and running `go install` from the project directory.

```shell
git clone https://github.com/cube2222/octosql
cd octosql
go install
```

## File Access

Support for multiple file types is included by default in OctoSQL:
- JSON (in JSONLines format, one object per line)
- CSV
- TSV
- Parquet
- Lines (reading a file line by line)

If your file has a matching extension, you can use its path directly as a table:
```
~> octosql "SELECT * FROM my/file/path.json"
```
or, if the extension is not right, you can use this alternative notation, where the extension is used in place of the database name:
```
~> octosql "SELECT * FROM `json.my/file/path.whatever`"
```

You can also specify additional options using the following notation: `myfile.ext?key=value&key2=value2`

The following options are available:
- CSV
  - header: true/false (default: true) - Whether the file has a header row.
- JSON
  - tail: true/false (default: false) - Whether to keep waiting for new content after reaching the end of the file.
- Lines
  - tail: true/false (default: false) - Whether to keep waiting for new content after reaching the end of the file.

### Reading from Standard Input
You can also pipe data in through stdin, and OctoSQL will expose it as the `stdin.<file_type>` table. For example:
```
~> echo '{"hello": "world"}' | octosql "SELECT * FROM stdin.json"
+---------+
|  hello  |
+---------+
| 'world' |
+---------+
~> seq 100 | octosql "SELECT SUM(int(text)) FROM stdin.lines"
+------+
| sum  |
+------+
| 5050 |
+------+
```

## Plugins

To use databases which are not included in the core of OctoSQL - like PostgreSQL or MySQL - you need to install a plugin. Installing plugins is very easy. The following command installs the latest version of the PostgreSQL plugin:
```bash
octosql plugin install postgres
```
Plugins are grouped into repositories, and potentially have many versions available. The above uses the default **core** repository and tries to install the latest version. So if 0.42.0 was the latest version, the above would be equivalent to:
```bash
octosql plugin install core/postgres@0.42.0
```

Browsing available and installed plugins is possible through OctoSQL itself, behind a SQL interface. The available tables are: `plugins.repositories`, `plugins.available_plugins`, `plugins.available_versions`, `plugins.installed_plugins`, `plugins.installed_versions`.

```bash
~> octosql "SELECT name, description FROM plugins.available_plugins LIMIT 2"
+------------------------+-------------------------------+
| available_plugins.name | available_plugins.description |
+------------------------+-------------------------------+
| 'postgres'             | 'Adds support for             |
|                        | querying PostgreSQL           |
|                        | databases.'                   |
| 'random_data'          | 'Generates random data        |
|                        | for testing.'                 |
+------------------------+-------------------------------+
~> octosql "SELECT plugin_name, version FROM plugins.available_versions WHERE plugin_name='random_data'"
+--------------------------------+----------------------------+
| available_versions.plugin_name | available_versions.version |
+--------------------------------+----------------------------+
| 'random_data'                  | '0.1.0'                    |
| 'random_data'                  | '0.1.1'                    |
| 'random_data'                  | '0.2.0'                    |
+--------------------------------+----------------------------+
```

Some plugins, like the `random_data` plugin, can be used without any additional configuration:
```bash
~> octosql plugin install random_data
Downloading core/random_data@0.2.0...
~> octosql "SELECT * FROM random_data.users" --describe
+---------------------------------+--------------------------+------------+
|              name               |           type           | time_field |
+---------------------------------+--------------------------+------------+
| 'users.avatar'                  | 'String'                 | false      |
| 'users.credit_card'             | '{cc_number: String}'    | false      |
| 'users.date_of_birth'           | 'String'                 | false      |
| 'users.email'                   | 'String'                 | false      |
| 'users.first_name'              | 'String'                 | false      |
| 'users.last_name'               | 'String'                 | false      |
| ...                             | ...                      | ...        |
+---------------------------------+--------------------------+------------+
~> octosql "SELECT first_name, last_name, date_of_birth FROM random_data.users LIMIT 3"
+------------------+-----------------+---------------------+
| users.first_name | users.last_name | users.date_of_birth |
+------------------+-----------------+---------------------+
| 'Alethea'        | 'Kuvalis'       | '1997-01-07'        |
| 'Ambrose'        | 'Spencer'       | '1979-04-18'        |
| 'Antione'        | 'Hodkiewicz'    | '1980-03-04'        |
+------------------+-----------------+---------------------+
```

Others, like the `postgres` plugin, require additional configuration. The configuration file is located at `~/.octosql/octosql.yml`. You can find the available configuration settings for a plugin in its own documentation.
```bash
~> octosql plugin install postgres
Downloading core/postgres@0.1.0...
echo "databases:
  - name: mydb
    type: postgres
    config:
      host: localhost
      port: 5432
      database: postgres
      user: postgres
      password: mypassword" > ~/.octosql/octosql.yml
~> octosql "SELECT * FROM mydb.customers" --describe
+--------------------------+-----------------+------------+
|           name           |      type       | time_field |
+--------------------------+-----------------+------------+
| 'customers.email'        | 'String'        | false      |
| 'customers.first_name'   | 'String'        | false      |
| 'customers.id'           | 'Int'           | false      |
| 'customers.last_name'    | 'String'        | false      |
| 'customers.phone_number' | 'String | NULL' | false      |
+--------------------------+-----------------+------------+
~> octosql "SELECT COUNT(*) FROM mydb.customers"
+-------+
| count |
+-------+
|   183 |
+-------+
```

In order to create your own plugins, see examples of existing plugins:
- [MySQL](https://github.com/cube2222/octosql-plugin-mysql)
- [PostgreSQL](https://github.com/cube2222/octosql-plugin-postgres)
- [Random Data](https://github.com/cube2222/octosql-plugin-random_data)

To test plugins while developing locally, put the plugin binary into `~/.octosql/plugins/core/octosql-plugin-<plugin name>/0.1.0/octosql-plugin-<plugin name>`. That's the location where OctoSQL will be looking for it.

## Troubleshooting
OctoSQL writes logs to `~/.octosql/logs.txt`, which is the place to look for any errors or issues during execution. Only logs of the most recent execution are kept.

## Advanced Features

### The Type System

OctoSQL is statically typed. That means that queries are verified, typechecked, and optimized based on the schemas of the tables and types of any values used in the query.

Most of the type system is straight-forward and intuitive, similar to what you'd find in other SQL dialects, even though the types have names which are closer to common programming languages, not SQL databases - in OctoSQL you'll find `String`'s, not `varchar`'s.

However, OctoSQL also supports **union types**, which means that a value might be one of multiple types. For example, you might have a dataset where a column is usually a Float, but occasionally also a String with the Float inside. Thus, the type of the column would be `Float | String`.

Moreover, `NULL` is its own type, which means that a nullable `Int` column would be represented as `Int | NULL` in OctoSQL.

There's a few helper features to handle this union types in OctoSQL.

First, whenever a type, i.e. `String | Int`, is used in a place where a subtype, i.e. `Int`, is expected, OctoSQL will add a dynamic runtime check which will fail execution only if a `String` value actually ever reaches that place.

Second, you can use type assertions to get a value only if it's of a certain type and otherwise evaluate to `NULL`. The syntax for that is `value::type`. So for example we might have a column `age` of type `String | Int` and would like to get its value only if it's an Int. We can write `age::Int` to express that.

Third, there's a bunch of conversion functions which can help you turn types into other types. For example, the `int` function is able to turn values of many types, including strings, to integers. You could use it like this: `int(age_string)`.

Fourth, and final, there's the `COALESCE` operator which accepts an arbitrary number of arguments and returns the first non-null one. It works very well with what's described in the previous two paragraphs. This way, if you have an `age` column of type `String | Int` and would like to clean it up, you can write `COALESCE(age::int, int(age::string), 0)`. This would return the value of `age` as-is if it's an `Int`, try to parse it if it's a `String`, and just evaluate to `0` if that fails.

Additionally, you can work with objects and lists using the following syntax:
- List access: `list[index]`
- Object field access: `object->field`

### Explaining Query Plans

You can use the `--explain` flag to get a visual explanation of the query plan. Setting it to 1 gives you a query plan but without type and schema information, setting it to 2 includes those too. For the visualization to work you need to have the graphviz dot command installed.

For example, running:
```bash
octosql "SELECT email, COUNT(*) as invoice_count
         FROM invoices.csv JOIN mydb.customers ON invoices.customer_id = customers.id
         WHERE first_name <= 'D'
         GROUP BY email
         ORDER BY invoice_count DESC" --explain 1
```
will produce the following output:
![Explain](images/octosql-explain.png)

Here we can see that the `first_name <= 'D'` predicate has been pushed down to the `mydb.customers` table query.

### Dataflow

OctoSQL is a dataflow engine. In practice that means it can execute a query and then update it based on changes in the inputs. The way this works in practice is by using retractions, each record sent internally has a `retraction` flag dictating whether it's an `undo` or not.

This also means that OctoSQL can work very well with endless streams of data, or display partial results before calculating the full query.

In order to handle that well, OctoSQL contains the concept of record event times and watermarks. Each Record can hav
... [TRUNCATED]
```

### File: main.go
```go
package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"

	"github.com/cube2222/octosql/cmd"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	signals := make(chan os.Signal, 1)
	signal.Notify(signals, os.Interrupt)
	go func() {
		<-signals
		cancel()
		<-signals
		fmt.Println("Force stopped without cleanup.")
		os.Exit(1)
	}()

	cmd.Execute(ctx)
}

```

### File: plugin_repository.json
```json
{
  "name": "Core OctoSQL Plugin Repository",
  "description": "The official place to publish and look for open-source OctoSQL plugins.",
  "slug": "core",
  "plugins": [
    {
      "name": "mysql",
      "description": "Adds support for querying MySQL databases.",
      "website": "https://github.com/cube2222/octosql-plugin-mysql",
      "contact_email": "jakub.wit.martin+octosql@gmail.com",
      "license": "Mozilla Public License Version 2.0",
      "readme_url": "https://raw.githubusercontent.com/cube2222/octosql-plugin-mysql/main/README.md",
      "manifest_url": "https://raw.githubusercontent.com/cube2222/octosql-plugin-mysql/main/octosql_manifest.json"
    },
    {
      "name": "postgres",
      "description": "Adds support for querying PostgreSQL databases.",
      "website": "https://github.com/cube2222/octosql-plugin-postgres",
      "contact_email": "jakub.wit.martin+octosql@gmail.com",
      "license": "Mozilla Public License Version 2.0",
      "readme_url": "https://raw.githubusercontent.com/cube2222/octosql-plugin-postgres/main/README.md",
      "manifest_url": "https://raw.githubusercontent.com/cube2222/octosql-plugin-postgres/main/octosql_manifest.json"
    },
    {
      "name": "random_data",
      "description": "Generates random data for testing.",
      "website": "https://github.com/cube2222/octosql-plugin-random_data",
      "contact_email": "jakub.wit.martin+octosql@gmail.com",
      "license": "Mozilla Public License Version 2.0",
      "readme_url": "https://raw.githubusercontent.com/cube2222/octosql-plugin-random_data/main/README.md",
      "manifest_url": "https://raw.githubusercontent.com/cube2222/octosql-plugin-random_data/main/octosql_manifest.json"
    }
  ]
}

```

### File: aggregates\array.go
```go
package aggregates

import (
	"fmt"

	"github.com/google/btree"

	"github.com/cube2222/octosql/execution"
	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var ArrayOverloads = []physical.AggregateDescriptor{
	{
		TypeFn: func(t octosql.Type) (octosql.Type, bool) {
			return octosql.Type{TypeID: octosql.TypeIDList, List: struct{ Element *octosql.Type }{Element: &t}}, true
		},
		Prototype: NewArrayPrototype(),
	},
}

// TODO: Elements should be sorted as they come, not sorted by value in a BTree.
type Array struct {
	items *btree.BTree
}

func NewArrayPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &Array{
			items: btree.New(execution.BTreeDefaultDegree),
		}
	}
}

type arrayKey struct {
	value octosql.Value
	count int
}

func (key *arrayKey) Less(than btree.Item) bool {
	thanTyped, ok := than.(*arrayKey)
	if !ok {
		panic(fmt.Sprintf("invalid key comparison: %T", than))
	}

	return key.value.Compare(thanTyped.value) == -1
}

func (c *Array) Add(retraction bool, value octosql.Value) bool {
	item := c.items.Get(&arrayKey{value: value})
	var itemTyped *arrayKey

	if item == nil {
		itemTyped = &arrayKey{value: value, count: 0}
		c.items.ReplaceOrInsert(itemTyped)
	} else {
		var ok bool
		itemTyped, ok = item.(*arrayKey)
		if !ok {
			panic(fmt.Sprintf("invalid received item: %v", item))
		}
	}
	if !retraction {
		itemTyped.count++
	} else {
		itemTyped.count--
	}
	if itemTyped.count == 0 {
		c.items.Delete(itemTyped)
	}
	return c.items.Len() == 0
}

func (c *Array) Trigger() octosql.Value {
	out := make([]octosql.Value, 0, c.items.Len())
	c.items.Ascend(func(item btree.Item) bool {
		itemTyped, ok := item.(*arrayKey)
		if !ok {
			panic(fmt.Sprintf("invalid received item: %v", item))
		}
		for i := 0; i < itemTyped.count; i++ {
			out = append(out, itemTyped.value)
		}
		return true
	})

	return octosql.NewList(out)
}

```

### File: aggregates\average.go
```go
package aggregates

import (
	"time"

	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var AverageOverloads = []physical.AggregateDescriptor{
	{
		ArgumentType: octosql.Int,
		OutputType:   octosql.Int,
		Prototype:    NewAverageIntPrototype(),
	},
	{
		ArgumentType: octosql.Float,
		OutputType:   octosql.Float,
		Prototype:    NewAverageFloatPrototype(),
	},
	{
		ArgumentType: octosql.Duration,
		OutputType:   octosql.Duration,
		Prototype:    NewAverageDurationPrototype(),
	},
}

type AverageInt struct {
	sum   SumInt
	count Count
}

func NewAverageIntPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &AverageInt{
			sum:   SumInt{},
			count: Count{},
		}
	}
}

func (c *AverageInt) Add(retraction bool, value octosql.Value) bool {
	c.sum.Add(retraction, value)
	return c.count.Add(retraction, value)
}

func (c *AverageInt) Trigger() octosql.Value {
	return octosql.NewInt(c.sum.Trigger().Int / c.count.Trigger().Int)
}

type AverageFloat struct {
	sum   SumFloat
	count Count
}

func NewAverageFloatPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &AverageFloat{
			sum:   SumFloat{},
			count: Count{},
		}
	}
}

func (c *AverageFloat) Add(retraction bool, value octosql.Value) bool {
	c.sum.Add(retraction, value)
	return c.count.Add(retraction, value)
}

func (c *AverageFloat) Trigger() octosql.Value {
	return octosql.NewFloat(c.sum.Trigger().Float / float64(c.count.Trigger().Int))
}

type AverageDuration struct {
	sum   SumDuration
	count Count
}

func NewAverageDurationPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &AverageDuration{
			sum:   SumDuration{},
			count: Count{},
		}
	}
}

func (c *AverageDuration) Add(retraction bool, value octosql.Value) bool {
	c.sum.Add(retraction, value)
	return c.count.Add(retraction, value)
}

func (c *AverageDuration) Trigger() octosql.Value {
	return octosql.NewDuration(c.sum.Trigger().Duration / time.Duration(c.count.Trigger().Int))
}

```

### File: aggregates\count.go
```go
package aggregates

import (
	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var CountOverloads = []physical.AggregateDescriptor{
	{
		ArgumentType: octosql.Any,
		OutputType:   octosql.Int,
		Prototype:    NewCountPrototype(),
	},
}

type Count struct {
	count int64
}

func NewCountPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &Count{
			count: 0,
		}
	}
}

func (c *Count) Add(retraction bool, value octosql.Value) bool {
	if !retraction {
		c.count++
	} else {
		c.count--
	}
	return c.count == 0
}

func (c *Count) Trigger() octosql.Value {
	return octosql.NewInt(c.count)
}

```

### File: aggregates\distinct.go
```go
package aggregates

import (
	"github.com/zyedidia/generic/hashmap"

	"github.com/cube2222/octosql/execution"
	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

func DistinctAggregateOverloads(overloads []physical.AggregateDescriptor) []physical.AggregateDescriptor {
	out := make([]physical.AggregateDescriptor, len(overloads))
	for i := range overloads {
		out[i] = physical.AggregateDescriptor{
			ArgumentType: overloads[i].ArgumentType,
			OutputType:   overloads[i].OutputType,
			TypeFn:       overloads[i].TypeFn,
			Prototype:    NewDistinctPrototype(overloads[i].Prototype),
		}
	}
	return out
}

type Distinct struct {
	items   *hashmap.Map[octosql.Value, *distinctKey]
	wrapped nodes.Aggregate
}

func NewDistinctPrototype(wrapped func() nodes.Aggregate) func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &Distinct{
			items: hashmap.New[octosql.Value, *distinctKey](
				execution.BTreeDefaultDegree,
				func(a, b octosql.Value) bool {
					return a.Compare(b) == 0
				}, func(v octosql.Value) uint64 {
					return v.Hash()
				}),
			wrapped: wrapped(),
		}
	}
}

type distinctKey struct {
	count int
}

func (c *Distinct) Add(retraction bool, value octosql.Value) bool {
	item, ok := c.items.Get(value)
	if !ok {
		item = &distinctKey{count: 0}
		c.items.Put(value, item)
	}
	if !retraction {
		item.count++
	} else {
		item.count--
	}
	if item.count == 1 && !retraction {
		c.wrapped.Add(false, value)
	} else if item.count == 0 {
		c.items.Remove(value)
		c.wrapped.Add(true, value)
	}
	return c.items.Size() == 0
}

func (c *Distinct) Trigger() octosql.Value {
	return c.wrapped.Trigger()
}

```

### File: aggregates\max.go
```go
package aggregates

import (
	"fmt"

	"github.com/google/btree"

	"github.com/cube2222/octosql/execution"
	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var MaxOverloads = []physical.AggregateDescriptor{
	{
		ArgumentType: octosql.Int,
		OutputType:   octosql.Int,
		Prototype:    NewMaxPrototype(),
	},
	{
		ArgumentType: octosql.Float,
		OutputType:   octosql.Float,
		Prototype:    NewMaxPrototype(),
	},
	{
		ArgumentType: octosql.Duration,
		OutputType:   octosql.Duration,
		Prototype:    NewMaxPrototype(),
	},
	{
		ArgumentType: octosql.Time,
		OutputType:   octosql.Time,
		Prototype:    NewMaxPrototype(),
	},
}

type Max struct {
	items *btree.BTree
}

func NewMaxPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &Max{
			items: btree.New(execution.BTreeDefaultDegree),
		}
	}
}

type maxKey struct {
	value octosql.Value
	count int
}

func (key *maxKey) Less(than btree.Item) bool {
	thanTyped, ok := than.(*maxKey)
	if !ok {
		panic(fmt.Sprintf("invalid key comparison: %T", than))
	}

	return key.value.Compare(thanTyped.value) == -1
}

func (c *Max) Add(retraction bool, value octosql.Value) bool {
	item := c.items.Get(&maxKey{value: value})
	var itemTyped *maxKey

	if item == nil {
		itemTyped = &maxKey{value: value, count: 0}
		c.items.ReplaceOrInsert(itemTyped)
	} else {
		var ok bool
		itemTyped, ok = item.(*maxKey)
		if !ok {
			panic(fmt.Sprintf("invalid received item: %v", item))
		}
	}
	if !retraction {
		itemTyped.count++
	} else {
		itemTyped.count--
	}
	if itemTyped.count == 0 {
		c.items.Delete(itemTyped)
	}
	return c.items.Len() == 0
}

func (c *Max) Trigger() octosql.Value {
	return c.items.Max().(*maxKey).value
}

```

### File: aggregates\min.go
```go
package aggregates

import (
	"fmt"

	"github.com/google/btree"

	"github.com/cube2222/octosql/execution"
	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var MinOverloads = []physical.AggregateDescriptor{
	{
		ArgumentType: octosql.Int,
		OutputType:   octosql.Int,
		Prototype:    NewMinPrototype(),
	},
	{
		ArgumentType: octosql.Float,
		OutputType:   octosql.Float,
		Prototype:    NewMinPrototype(),
	},
	{
		ArgumentType: octosql.Duration,
		OutputType:   octosql.Duration,
		Prototype:    NewMinPrototype(),
	},
}

type Min struct {
	items *btree.BTree
}

func NewMinPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &Min{
			items: btree.New(execution.BTreeDefaultDegree),
		}
	}
}

type minKey struct {
	value octosql.Value
	count int
}

func (key *minKey) Less(than btree.Item) bool {
	thanTyped, ok := than.(*minKey)
	if !ok {
		panic(fmt.Sprintf("invalid key comparison: %T", than))
	}

	return key.value.Compare(thanTyped.value) == -1
}

func (c *Min) Add(retraction bool, value octosql.Value) bool {
	item := c.items.Get(&minKey{value: value})
	var itemTyped *minKey

	if item == nil {
		itemTyped = &minKey{value: value, count: 0}
		c.items.ReplaceOrInsert(itemTyped)
	} else {
		var ok bool
		itemTyped, ok = item.(*minKey)
		if !ok {
			panic(fmt.Sprintf("invalid received item: %v", item))
		}
	}
	if !retraction {
		itemTyped.count++
	} else {
		itemTyped.count--
	}
	if itemTyped.count == 0 {
		c.items.Delete(itemTyped)
	}
	return c.items.Len() == 0
}

func (c *Min) Trigger() octosql.Value {
	return c.items.Min().(*minKey).value
}

```

### File: aggregates\sum.go
```go
package aggregates

import (
	"time"

	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var SumOverloads = []physical.AggregateDescriptor{
	{
		ArgumentType: octosql.Int,
		OutputType:   octosql.Int,
		Prototype:    NewSumIntPrototype(),
	},
	{
		ArgumentType: octosql.Float,
		OutputType:   octosql.Float,
		Prototype:    NewSumFloatPrototype(),
	},
	{
		ArgumentType: octosql.Duration,
		OutputType:   octosql.Duration,
		Prototype:    NewSumDurationPrototype(),
	},
}

type SumInt struct {
	sum int64
}

func NewSumIntPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &SumInt{
			sum: 0,
		}
	}
}

func (c *SumInt) Add(retraction bool, value octosql.Value) bool {
	if !retraction {
		c.sum += value.Int
	} else {
		c.sum -= value.Int
	}
	return c.sum == 0
}

func (c *SumInt) Trigger() octosql.Value {
	return octosql.NewInt(c.sum)
}

type SumFloat struct {
	sum float64
}

func NewSumFloatPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &SumFloat{
			sum: 0,
		}
	}
}

func (c *SumFloat) Add(retraction bool, value octosql.Value) bool {
	if !retraction {
		c.sum += value.Float
	} else {
		c.sum -= value.Float
	}
	return c.sum == 0
}

func (c *SumFloat) Trigger() octosql.Value {
	return octosql.NewFloat(c.sum)
}

type SumDuration struct {
	sum time.Duration
}

func NewSumDurationPrototype() func() nodes.Aggregate {
	return func() nodes.Aggregate {
		return &SumDuration{
			sum: 0,
		}
	}
}

func (c *SumDuration) Add(retraction bool, value octosql.Value) bool {
	if !retraction {
		c.sum += value.Duration
	} else {
		c.sum -= value.Duration
	}
	return c.sum == 0
}

func (c *SumDuration) Trigger() octosql.Value {
	return octosql.NewDuration(c.sum)
}

```

### File: aggregates\table.go
```go
package aggregates

import (
	"github.com/cube2222/octosql/physical"
)

var Aggregates = map[string]physical.AggregateDetails{
	"array_agg": {
		Description: "Creates an array of all items in the group.",
		Descriptors: ArrayOverloads,
	},
	"array_agg_distinct": {
		Description: "Creates an array of distinct items in the group.",
		Descriptors: DistinctAggregateOverloads(ArrayOverloads),
	},
	"count": {
		Description: "Counts all items in the group.",
		Descriptors: CountOverloads,
	},
	"count_distinct": {
		Description: "Counts distinct items in the group.",
		Descriptors: DistinctAggregateOverloads(CountOverloads),
	},
	"sum": {
		Description: "Sums all items in the group.",
		Descriptors: SumOverloads,
	},
	"sum_distinct": {
		Description: "Sums distinct items in the group.",
		Descriptors: DistinctAggregateOverloads(SumOverloads),
	},
	"avg": {
		Description: "Averages all items in the group.",
		Descriptors: AverageOverloads,
	},
	"avg_distinct": {
		Description: "Averages distinct items in the group.",
		Descriptors: DistinctAggregateOverloads(AverageOverloads),
	},
	"max": {
		Description: "Returns maximum item in the group.",
		Descriptors: MaxOverloads,
	},
	"min": {
		Description: "Returns minimum item in the group.",
		Descriptors: MinOverloads,
	},
}

```

### File: benchmarks\benchmarks.sh
```sh
curl https://s3.amazonaws.com/nyc-tlc/csv_backup/yellow_tripdata_2021-04.csv -o taxi.csv

echo "CREATE EXTERNAL TABLE taxi
STORED AS CSV
WITH HEADER ROW
LOCATION './taxi.csv';

SELECT passenger_count, COUNT(*), AVG(total_amount) FROM taxi GROUP BY passenger_count;" > datafusion_commands.txt

wc -l taxi.csv && wc -l taxi.csv && wc -l taxi.csv && wc -l taxi.csv # Get the cache warm.

hyperfine --min-runs 10 -w 2 --export-markdown benchmarks.md \
'OCTOSQL_NO_TELEMETRY=1 octosql "SELECT passenger_count, COUNT(*), AVG(total_amount) FROM taxi.csv GROUP BY passenger_count"' \
"q -d ',' -H \"SELECT passenger_count, COUNT(*), AVG(total_amount) FROM taxi.csv GROUP BY passenger_count\"" \
"q -d ',' -H -C readwrite \"SELECT passenger_count, COUNT(*), AVG(total_amount) FROM taxi.csv GROUP BY passenger_count\"" \
'textql -header -sql "SELECT passenger_count, COUNT(*), AVG(total_amount) FROM taxi GROUP BY passenger_count" taxi.csv' \
'datafusion-cli -f datafusion_commands.txt' \
'dsq taxi.csv "SELECT passenger_count, COUNT(*), AVG(total_amount) FROM {} GROUP BY passenger_count"' \
'dsq --cache taxi.csv "SELECT passenger_count, COUNT(*), AVG(total_amount) FROM {} GROUP BY passenger_count"' \
'spyql "SELECT passenger_count, count_agg(*), avg_agg(total_amount) FROM csv GROUP BY passenger_count" < taxi.csv'


```

### File: cmd\describe.go
```go
package cmd

import (
	"fmt"
	"time"

	. "github.com/cube2222/octosql/execution"
	"github.com/cube2222/octosql/octosql"
	"github.com/cube2222/octosql/physical"
)

var DescribeNodeSchema = physical.NewSchema(
	[]physical.SchemaField{
		{
			Name: "name",
			Type: octosql.String,
		},
		{
			Name: "type",
			Type: octosql.String,
		},
		{
			Name: "time_field",
			Type: octosql.Boolean,
		},
	},
	-1,
)

type DescribeNode struct {
	Schema physical.Schema
}

func (d *DescribeNode) Run(ctx ExecutionContext, produce ProduceFn, metaSend MetaSendFn) error {
	for i, field := range d.Schema.Fields {
		if err := produce(
			ProduceFromExecutionContext(ctx),
			NewRecord([]octosql.Value{
				octosql.NewString(field.Name),
				octosql.NewString(field.Type.String()),
				octosql.NewBoolean(i == d.Schema.TimeField),
			}, false, time.Time{}),
		); err != nil {
			return fmt.Errorf("couldn't produce record: %w", err)
		}
	}
	return nil
}

```

### File: cmd\plugin.go
```go
package cmd

import (
	"github.com/spf13/cobra"
)

// pluginCmd represents the plugin command
var pluginCmd = &cobra.Command{
	Use:   "plugin",
	Short: "",
	Long:  ``,
}

func init() {
	rootCmd.AddCommand(pluginCmd)
}

```

### File: cmd\plugin_install.go
```go
package cmd

import (
	"fmt"

	"github.com/Masterminds/semver"
	"github.com/spf13/cobra"

	"github.com/cube2222/octosql/config"
	"github.com/cube2222/octosql/plugins/manager"
	"github.com/cube2222/octosql/plugins/repository"
)

// pluginInstallCmd represents the plugin install command
var pluginInstallCmd = &cobra.Command{
	Use:   "install",
	Short: "",
	Long:  ``,
	RunE: func(cmd *cobra.Command, args []string) error {
		ctx := cmd.Context()
		repositories, err := repository.GetRepositories(ctx)
		if err != nil {
			return fmt.Errorf("couldn't get repositories: %w", err)
		}
		pluginManager := &manager.PluginManager{
			Repositories: repositories,
		}

		if len(args) > 0 {
			for _, arg := range args {
				if err := pluginManager.Install(ctx, arg, nil); err != nil {
					return err
				}
			}
			return nil
		}

		cfg, err := config.Read()
		if err != nil {
			return fmt.Errorf("couldn't read config: %w", err)
		}

	dbLoop:
		for i := range cfg.Databases {
			installedPlugins, err := pluginManager.ListInstalledPlugins()
			if err != nil {
				return fmt.Errorf("couldn't list installed plugins: %w", err)
			}

			if cfg.Databases[i].Version == nil {
				constraint, _ := semver.NewConstraint("*")
				cfg.Databases[i].Version = config.NewYamlUnmarshallableVersionConstraint(constraint)
			}
			for _, plugin := range installedPlugins {
				if plugin.Reference != cfg.Databases[i].Type {
					continue
				}
				for _, version := range plugin.Versions {
					if cfg.Databases[i].Version.Raw().Check(version.Number) {
						continue dbLoop
					}
				}
			}
			if err := pluginManager.Install(ctx, cfg.Databases[i].Type.String(), cfg.Databases[i].Version.Raw()); err != nil {
				return err
			}
		}

		return nil
	},
}

func init() {
	pluginCmd.AddCommand(pluginInstallCmd)
}

```

### File: cmd\plugin_repository.go
```go
package cmd

import (
	"github.com/spf13/cobra"
)

// pluginRepositoryCmd represents the plugin command
var pluginRepositoryCmd = &cobra.Command{
	Use:   "repository",
	Short: "",
	Long:  ``,
}

func init() {
	pluginCmd.AddCommand(pluginRepositoryCmd)
}

```

### File: cmd\plugin_repository_add.go
```go
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"

	"github.com/cube2222/octosql/plugins/repository"
)

// pluginRepositoryAddCmd represents the plugin install command
var pluginRepositoryAddCmd = &cobra.Command{
	Use:   "add",
	Short: "",
	Long:  ``,
	RunE: func(cmd *cobra.Command, args []string) error {
		ctx := cmd.Context()
		for _, arg := range args {
			if err := repository.AddRepository(ctx, arg); err != nil {
				return fmt.Errorf("couldn't add repository '%s': %s", arg, err)
			}
		}

		return nil
	},
}

func init() {
	pluginRepositoryCmd.AddCommand(pluginRepositoryAddCmd)
}

```

### File: cmd\root.go
```go
package cmd

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"
	"os/exec"
	"runtime/debug"
	"runtime/trace"
	"strings"
	"sync"

	"github.com/Masterminds/semver"
	"github.com/pkg/profile"
	"github.com/skratchdot/open-golang/open"
	"github.com/spf13/cobra"
	"gopkg.in/yaml.v3"

	"github.com/cube2222/octosql/aggregates"
	"github.com/cube2222/octosql/config"
	"github.com/cube2222/octosql/datasources/csv"
	"github.com/cube2222/octosql/datasources/docs"
	"github.com/cube2222/octosql/datasources/json"
	"github.com/cube2222/octosql/datasources/lines"
	"github.com/cube2222/octosql/datasources/parquet"
	"github.com/cube2222/octosql/datasources/plugins"
	"github.com/cube2222/octosql/execution"
	"github.com/cube2222/octosql/execution/nodes"
	"github.com/cube2222/octosql/functions"
	"github.com/cube2222/octosql/helpers/graph"
	"github.com/cube2222/octosql/logical"
	"github.com/cube2222/octosql/logs"
	"github.com/cube2222/octosql/optimizer"
	"github.com/cube2222/octosql/outputs/batch"
	"github.com/cube2222/octosql/outputs/eager"
	"github.com/cube2222/octosql/outputs/formats"
	"github.com/cube2222/octosql/outputs/stream"
	"github.com/cube2222/octosql/parser"
	"github.com/cube2222/octosql/parser/sqlparser"
	"github.com/cube2222/octosql/physical"
	"github.com/cube2222/octosql/plugins/executor"
	"github.com/cube2222/octosql/plugins/manager"
	"github.com/cube2222/octosql/plugins/repository"
	"github.com/cube2222/octosql/table_valued_functions"
	"github.com/cube2222/octosql/telemetry"
)

var VERSION = "dev"

var emptyYamlNode = func() yaml.Node {
	var out yaml.Node
	if err := yaml.Unmarshal([]byte("{}"), &out); err != nil {
		log.Fatalf("[BUG] Couldn't create empty yaml node: %s", err)
	}
	return out
}()

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "octosql <query>",
	Args:  cobra.ExactArgs(1),
	Short: "",
	Long:  ``,
	Example: `octosql "SELECT * FROM myfile.json"
octosql "SELECT * FROM mydir/myfile.csv"
octosql "SELECT * FROM plugins.plugins"`,
	SilenceErrors: true,
	Version:       VERSION,
	RunE: func(cmd *cobra.Command, args []string) error {
		switch prof {
		case "cpu":
			defer profile.Start(profile.CPUProfile, profile.ProfilePath(".")).Stop()
		case "memory":
			defer profile.Start(profile.MemProfile, profile.MemProfileRate(4096*8), profile.ProfilePath(".")).Stop()
		case "trace":
			defer profile.Start(profile.TraceProfile, profile.ProfilePath(".")).Stop()
		}
		ctx := cmd.Context()
		cfg, err := config.Read()
		if err != nil {
			return fmt.Errorf("couldn't read config: %w", err)
		}
		ctx = config.ContextWithConfig(ctx, cfg)

		debug.SetGCPercent(1000)

		logs.InitializeFileLogger()
		defer logs.CloseLogger()

		pluginManager := &manager.PluginManager{}

		pluginExecutor := executor.PluginExecutor{
			Manager: pluginManager,
		}
		defer func() {
			if err := pluginExecutor.Close(); err != nil {
				log.Printf("couldn't close plugin executor: %s", err)
			}
		}()

		installedPlugins, err := pluginManager.ListInstalledPlugins()
		if err != nil {
			return fmt.Errorf("couldn't list installed plugins: %w", err)
		}

		resolvedVersions := map[string]*semver.Version{}

		// Fill in plugin versions.
	dbLoop:
		for i := range cfg.Databases {
			if cfg.Databases[i].Version == nil {
				constraint, _ := semver.NewConstraint("*")
				cfg.Databases[i].Version = config.NewYamlUnmarshallableVersionConstraint(constraint)
			}
			for _, plugin := range installedPlugins {
				if plugin.Reference != cfg.Databases[i].Type {
					continue
				}
				for _, version := range plugin.Versions {
					if cfg.Databases[i].Version.Raw().Check(version.Number) {
						resolvedVersions[cfg.Databases[i].Name] = version.Number
						continue dbLoop
					}
				}
				break
			}
			return fmt.Errorf("database '%s' plugin '%s' used in configuration is not installed with the required version - run `octosql plugin install` to install all missing plugins", cfg.Databases[i].Name, cfg.Databases[i].Type.String())
		}

		databases := make(map[string]func() (physical.Database, error))
		for _, dbConfig := range cfg.Databases {
			once := sync.Once{}
			curDbConfig := dbConfig
			var db physical.Database
			var err error

			databases[curDbConfig.Name] = func() (physical.Database, error) {
				once.Do(func() {
					db, err = pluginExecutor.RunPlugin(ctx, curDbConfig.Type, curDbConfig.Name, resolvedVersions[curDbConfig.Name], curDbConfig.Config)
				})
				if err != nil {
					return nil, fmt.Errorf("couldn't run %s plugin %s: %w", curDbConfig.Type.String(), curDbConfig.Name, err)
				}
				return db, nil
			}
		}
		{
			once := sync.Once{}
			var repositories []repository.Repository
			var err error
			databases["plugins"] = func() (physical.Database, error) {
				once.Do(func() {
					repositories, err = repository.GetRepositories(ctx)
				})
				if err != nil {
					return nil, fmt.Errorf("couldn't get repositories: %w", err)
				}
				return plugins.Creator(ctx, pluginManager, repositories)
			}
		}
		databases["docs"] = func() (physical.Database, error) {
			return docs.Creator(ctx)
		}

		for _, metadata := range installedPlugins {
			if _, ok := databases[metadata.Reference.Name]; ok {
				continue
			}
			curMetadata := metadata

			once := sync.Once{}
			var db physical.Database
			var err error

			databases[curMetadata.Reference.Name] = func() (physical.Database, error) {
				once.Do(func() {
					db, err = pluginExecutor.RunPlugin(ctx, curMetadata.Reference, curMetadata.Reference.Name, curMetadata.Versions[0].Number, emptyYamlNode)
				})
				if err != nil {
					return nil, fmt.Errorf("couldn't run default plugin %s database: %w", curMetadata.Reference, err)
				}
				return db, nil
			}
		}

		fileExtensionHandlers, err := pluginManager.GetFileExtensionHandlers()
		if err != nil {
			return fmt.Errorf("couldn't get file extension handlers: %w", err)
		}
		fileHandlers := map[string]func(ctx context.Context, name string, options map[string]string) (physical.DatasourceImplementation, physical.Schema, error){
			"csv":     csv.Creator(','),
			"json":    json.Creator,
			"lines":   lines.Creator,
			"parquet": parquet.Creator,
			"tsv":     csv.Creator('\t'),
		}
		for ext, pluginName := range fileExtensionHandlers {
			fileHandlers[ext] = func(ctx context.Context, name string, options map[string]string) (physical.DatasourceImplementation, physical.Schema, error) {
				db, err := databases[pluginName]()
				if err != nil {
					return nil, physical.Schema{}, fmt.Errorf("couldn't get plugin %s database for plugin extensions %s: %w", pluginName, ext, err)
				}
				return db.GetTable(ctx, name, options)
			}
		}
		for name := range fileHandlers {
			curHandler := fileHandlers[name]
			if _, ok := databases[name]; !ok {
				databases[name] = func() (physical.Database, error) {
					return &fileTypeDatabaseCreator{
						creator: curHandler,
					}, nil
				}
			}
		}

		env := physical.Environment{
			Aggregates: aggregates.Aggregates,
			Functions:  functions.FunctionMap(),
			Datasources: &physical.DatasourceRepository{
				Databases:    databases,
				FileHandlers: fileHandlers,
			},
			PhysicalConfig:  nil,
			VariableContext: nil,
		}
		statement, err := sqlparser.Parse(args[0])
		if err != nil {
			return fmt.Errorf("couldn't parse query: %w", err)
		}
		selectStmt, ok := statement.(sqlparser.SelectStatement)
		if !ok {
			return fmt.Errorf("only SELECT statements are supported")
		}
		logicalPlan, outputOptions, err := parser.ParseNode(selectStmt)
		if err != nil {
			return fmt.Errorf("couldn't parse query: %w", err)
		}
		tableValuedFunctions := map[string]logical.TableValuedFunctionDescription{
			"max_diff_watermark": table_valued_functions.MaxDiffWatermark,
			"tumble":             table_valued_functions.Tumble,
			"range":              table_valued_functions.Range,
			"poll":               table_valued_functions.Poll,
		}
		uniqueNameGenerator := map[string]int{}
		physicalPlan, mapping, err := typecheckNode(
			ctx,
			logicalPlan,
			env,
			logical.Environment{
				CommonTableExpressions: map[string]logical.CommonTableExpression{},
				TableValuedFunctions:   tableValuedFunctions,
				UniqueNameGenerator:    uniqueNameGenerator,
			},
		)
		if err != nil {
			return err
		}
		reverseMapping := logical.ReverseMapping(mapping)

		physicalOrderByExpressions := make([]physical.Expression, len(outputOptions.OrderByExpressions))
		for i := range outputOptions.OrderByExpressions {
			physicalExpr, err := typecheckExpr(ctx, outputOptions.OrderByExpressions[i], env.WithRecordSchema(physicalPlan.Schema), logical.Environment{
				CommonTableExpressions: map[string]logical.CommonTableExpression{},
				TableValuedFunctions:   tableValuedFunctions,
				UniqueVariableNames: &logical.VariableMapping{
					Mapping: mapping,
				},
				UniqueNameGenerator: uniqueNameGenerator,
			})
			if err != nil {
				return fmt.Errorf("couldn't typecheck order by expression with index %d: %w", i, err)
			}
			physicalOrderByExpressions[i] = physicalExpr
		}
		var physicalLimitExpression *physical.Expression
		if outputOptions.Limit != nil {
			physicalExpr, err := typecheckExpr(ctx, *outputOptions.Limit, env.WithRecordSchema(physicalPlan.Schema), logical.Environment{
				CommonTableExpressions: map[string]logical.CommonTableExpression{},
				TableValuedFunctions:   tableValuedFunctions,
				UniqueVariableNames: &logical.VariableMapping{
					Mapping: mapping,
				},
				UniqueNameGenerator: uniqueNameGenerator,
			})
			if err != nil {
				return fmt.Errorf("couldn't typecheck limit expression with index: %w", err)
			}
			physicalLimitExpression = &physicalExpr
		}

		queryTelemetry := telemetry.GetQueryTelemetryData(physicalPlan, installedPlugins)

		var executionPlan execution.Node
		var orderByExpressions []execution.Expression
		var limitExpression *execution.Expression
		var outSchema physical.Schema
		if describe {
			telemetry.SendTelemetry(ctx, VERSION, "describe", queryTelemetry)

			for i := range physicalPlan.Schema.Fields {
				physicalPlan.Schema.Fields[i].Name = reverseMapping[physicalPlan.Schema.Fields[i].Name]
			}
			executionPlan = &DescribeNode{
				Schema: physical.Schema{
					Fields:        formats.WithoutQualifiers(physicalPlan.Schema.Fields),
					TimeField:     physicalPlan.Schema.TimeField,
					NoRetractions: physicalPlan.Schema.NoRetractions,
				},
			}
			outSchema = DescribeNodeSchema
		} else {
			telemetry.SendTelemetry(ctx, VERSION, "query", queryTelemetry)

			if optimize {
				physicalPlan = optimizer.Optimize(physicalPlan)
			}

			if explain >= 1 {
				file, err := os.CreateTemp(os.TempDir(), "octosql-explain-*.png")
				if err != nil {
					return fmt.Errorf("couldn't create temporary file: %w", err)
				}
				cmd := exec.Command("dot", "-Tpng")
				cmd.Stdin = strings.NewReader(graph.Show(physical.ExplainNode(physicalPlan, explain >= 2)).String())
				cmd.Stdout = file
				cmd.Stderr = os.Stderr
				if err := cmd.Run(); err != nil {
					return fmt.Errorf("couldn't render graph: %w", err)
				}
				if err := file.Close(); err != nil {
					return fmt.Errorf("couldn't close temporary file: %w", err)
				}
				if err := open.Start(file.Name()); err != nil {
					return fmt.Errorf("couldn't open graph: %w", err)
				}
				return nil
			}

			executionPlan, err = physicalPlan.Materialize(
				ctx,
				env,
			)
			if err != nil {
				return fmt.Errorf("couldn't materialize physical plan: %w", err)
			}

			orderByExpressions = make([]execution.Expression, len(physicalOrderByExpressions))
			for i, physicalExpr := range physicalOrderByExpressions {
				execExpr, err := physicalExpr.Materialize(ctx, env.WithRecordSchema(physicalPlan.Schema))
				if err != nil {
					return fmt.Errorf("couldn't materialize output order by expression with index %d: %v", i, err)
				}
				orderByExpressions[i] = execExpr
			}
			if physicalLimitExpression != nil {
				execExpr, err := physicalLimitExpression.Materialize(ctx, env.WithRecordSchema(physicalPlan.Schema))
				if err != nil {
					return fmt.Errorf("couldn't materialize output limit expression with index: %w", err)
				}
				limitExpression = &execExpr
			}

			outFields := make([]physical.SchemaField, len(physicalPlan.Schema.Fields))
			copy(outFields, physicalPlan.Schema.Fields)
			outSchema = physical.Schema{
				Fields:    outFields,
				TimeField: physicalPlan.Schema.TimeField,
			}
			for i := range outFields {
				outFields[i].Name = reverseMapping[outFields[i].Name]
			}
		}

		var sink interface {
			Run(execCtx execution.ExecutionContext) error
		}

		execCtx := execution.ExecutionContext{
			Context:         ctx,
			VariableContext: nil,
		}

		switch output {
		case "live_table", "batch_table":
			var limit *int64
			if limitExpression != nil {
				val, err := (*limitExpression).Evaluate(execCtx)
				if err != nil {
					return fmt.Errorf("couldn't evaluate limit expression: %w", err)
				}
				if val.Int < 0 {
					return fmt.Errorf("limit must be positive, got %d", val.Int)
				}
				limit = &val.Int

				if len(orderByExpressions) == 0 && physicalPlan.Schema.NoRetractions {
					// We want short-circuiting.
					executionPlan = nodes.NewLimit(executionPlan, *limitExpression)
				}
			}

			sink = batch.NewOutputPrinter(
				executionPlan,
				orderByExpressions,
				logical.DirectionsToMultipliers(outputOptions.OrderByDirections),
				limit,
				physicalPlan.Schema.NoRetractions,
				outSchema,
				func(writer io.Writer) batch.Format {
					return formats.NewTableFormatter(writer)
				},
				output == "live_table",
			)
		case "csv", "json":
			if len(orderByExpressions) > 0 || (limitExpression != nil && !physicalPlan.Schema.NoRetractions) {
				executionPlan = nodes.NewOrderSensitiveTransform(executionPlan, orderByExpressions, logical.DirectionsToMultipliers(outputOptions.OrderByDirections), limitExpression, physicalPlan.Schema.NoRetractions)
			} else if limitExpression != nil {
				executionPlan = nodes.NewLimit(executionPlan, *limitExpression)
			}

			var formatter func(writer io.Writer) eager.Format
			switch output {
			case "csv":
				formatter = func(writer io.Writer) eager.Format {
					return formats.NewCSVFormatter(writer)
				}
			case "json":
				formatter = func(writer io.Writer) eager.Format {
					return formats.NewJSONFormatter(writer)
				}
			}

			sink = eager.NewOutputPrinter(
				executionPlan,
				outSchema,
				formatter,
			)

		case "stream_native":
			if len(orderByExpressions) > 0 || (limitExpression != nil && !physicalPlan.Schema.NoRetractions) {
				executionPlan = nodes.NewOrderSensitiveTransform(executionPlan, orderByExpressions, logical.DirectionsToMultipliers(outputOptions.OrderByDirections), limitExpression, physicalPlan.Schema.NoRetractions)
			} else if limitExpression != nil {
				executionPlan = nodes.NewLimit(executionPlan, *limitExpression)
			}

			sink = stream.NewOutputPrinter(
				executionPlan,
				stream.NewNativeFormat(outSchema),
			)
		default:
			return fmt.Errorf("inv
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
