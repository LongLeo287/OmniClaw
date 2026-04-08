---
id: repo-fetched-alasql-112909
type: knowledge
owner: OA
registered_at: 2026-04-05T03:06:56.583986
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_alasql_112909

## Assimilation Report
Auto-cloned repository: FETCHED_alasql_112909

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
- _AlaSQL is an unfunded open source project installed 650k+ times each month. [Please donate your time](https://github.com/AlaSQL/alasql/issues?q=is%3Aopen+label%3A%22Help+wanted%22+sort%3Aupdated-desc). We appreciate any and all contributions we can get._

- _Have a question? [Ask The AlaSQL Bot](https://chatgpt.com/g/g-XcBL24WTe-alasql-bot) or post on [Stack Overflow](http://stackoverflow.com/questions/ask?tags=AlaSQL)._

[![CI-test](https://github.com/alasql/alasql/workflows/CI%20build%20&%20test/badge.svg)](https://github.com/alasql/alasql/actions)
[![NPM downloads](http://img.shields.io/npm/dm/alasql.svg?style=flat&label=npm%20downloads)](https://npm-stat.com/charts.html?package=alasql)
[![OPEN open source software](https://img.shields.io/badge/Open--OSS-%E2%9C%94-brightgreen.svg)](http://open-oss.com)
[![Release](https://img.shields.io/github/release/alasql/alasql.svg?label=npm&a)](https://www.npmjs.com/package/alasql)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/AlaSQL/alasql.svg)](http://isitmaintained.com/project/AlaSQL/alasql 'Average time to resolve an issue')
[![Coverage](https://img.shields.io/codecov/c/github/alasql/alasql/develop.svg)](https://rawgit.com/alasql/alasql/develop/test/coverage/lcov-report/dist/alasql.fs.js.html)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/AlaSQL/alasql/badge)](https://securityscorecards.dev/viewer/?uri=github.com/AlaSQL/alasql)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/328/badge)](https://bestpractices.coreinfrastructure.org/projects/328)
[![](https://data.jsdelivr.com/v1/package/npm/alasql/badge?style=rounded)](https://www.jsdelivr.com/package/npm/alasql)
[![Stars](https://img.shields.io/github/stars/alasql/alasql.svg?label=Github%20%E2%98%85&a)](https://github.com/alasql/alasql)

# AlaSQL

<h2 align="center"><a href="http://alasql.org"><img src="https://cloud.githubusercontent.com/assets/1063454/19309516/94f8007e-9085-11e6-810f-62fd60b42185.png" alt="AlaSQL logo" styl="max-width:80%"/></a>
</h2>

AlaSQL - _( [à la](http://en.wiktionary.org/wiki/%C3%A0_la) [SQL](http://en.wikipedia.org/wiki/SQL) ) [ælæ ɛskju:ɛl]_ - is an open source SQL database for JavaScript with a strong focus on query speed and data source flexibility for both relational data and schemaless data. It works in the web browser, Node.js, and mobile apps.

This library is perfect for:

- Fast in-memory SQL data processing for BI and ERP applications on fat clients
- Easy ETL and options for persistence by data import / manipulation / export of several formats
- All major browsers, Node.js, and mobile applications

We focus on [speed](https://github.com/alasql/alasql/wiki/Speed) by taking advantage of the dynamic nature of JavaScript when building up queries. Real-world solutions demand flexibility regarding where data comes from and where it is to be stored. We focus on flexibility by making sure you can [import/export](https://github.com/alasql/alasql/wiki/Import-export) and query directly on data stored in Excel (both `.xls` and `.xlsx`), CSV, JSON, TAB, IndexedDB, LocalStorage, and SQLite files.

The library adds the comfort of a full database engine to your JavaScript app. No, really - it's working towards a full database engine complying with [most of the SQL-99 language](https://github.com/alasql/alasql/wiki/Supported-SQL-statements), spiced up with additional syntax for NoSQL (schema-less) data and graph networks.

#### Traditional SQL Table

```js
/* create SQL Table and add data */
alasql('CREATE TABLE cities (city string, pop number)');

alasql("INSERT INTO cities VALUES ('Paris',2249975),('Berlin',3517424),('Madrid',3041579)");

/* execute query */
var res = alasql('SELECT * FROM cities WHERE pop < 3500000 ORDER BY pop DESC');

// res = [ { "city": "Madrid", "pop": 3041579 }, { "city": "Paris", "pop": 2249975 } ]
```

[Live Demo](https://jsfiddle.net/jqk80ard/)

#### Array of Objects

```js
var data = [
	{a: 1, b: 10},
	{a: 2, b: 20},
	{a: 1, b: 30},
];

var res = alasql('SELECT a, SUM(b) AS b FROM ? GROUP BY a', [data]);

// res = [ { "a": 1, "b": 40},{ "a": 2, "b": 20 } ]
```

[Live Demo](https://jsfiddle.net/8brvex4f/)

#### Spreadsheet

```js
// file is read asynchronously (Promise returned when SQL given as array)
alasql([
	'SELECT * FROM XLS("./data/mydata") WHERE lastname LIKE "A%" and city = "London" GROUP BY name ',
])
	.then(function (res) {
		console.log(res); // output depends on mydata.xls
	})
	.catch(function (err) {
		console.log('Does the file exist? There was an error:', err);
	});
```

#### Bulk Data Load

```js
alasql('CREATE TABLE example1 (a INT, b INT)');

// alasql's data store for a table can be assigned directly
alasql.tables.example1.data = [
	{a: 2, b: 6},
	{a: 3, b: 4},
];

// ... or manipulated with normal SQL
alasql('INSERT INTO example1 VALUES (1,5)');

var res = alasql('SELECT * FROM example1 ORDER BY b DESC');

console.log(res); // [{a:2,b:6},{a:1,b:5},{a:3,b:4}]
```

**If you are familiar with SQL, it should be no surprise that proper use of indexes on your tables is essential for good performance.**

#### Options

AlaSQL has several [configuration options](https://github.com/AlaSQL/alasql/wiki/AlaSQL-Options) which change the behavior. It can be set via SQL statements or via the options object before using `alasql`.

If you're using `NOW()` in queries often, setting `alasql.options.dateAsString` to `false` speed things up. It will just return a JS Date object instead of a string representation of a date.

## Installation

```bash
yarn add alasql                # yarn

npm install alasql             # npm

npm install -g alasql          # global install of command line tool
```

For the browsers: include [alasql.min.js](https://cdn.jsdelivr.net/npm/alasql)

```html
<script src="https://cdn.jsdelivr.net/npm/alasql@4"></script>
```

## Getting started

See the ["Getting started" section of the wiki](https://github.com/alasql/alasql/wiki/Getting%20started)

More advanced topics are covered in other wiki sections like ["Data manipulation"](https://github.com/alasql/alasql/wiki/Data-manipulation) and in questions on [Stack Overflow](http://stackoverflow.com/questions/tagged/alasql)

Other links:

- Documentation: [Github wiki](https://github.com/alasql/alasql/wiki)

- Library CDN: [jsDelivr.com](http://www.jsdelivr.com/#!alasql)

- Feedback: [Open an issue](https://github.com/alasql/alasql/issues/new)

- Try online: <a href="http://alasql.org/console?CREATE TABLE cities (city string, population number);INSERT INTO cities VALUES ('Rome',2863223), ('Paris',2249975),('Berlin',3517424), ('Madrid',3041579);SELECT * FROM cities WHERE population < 3500000 ORDER BY population DESC">Playground</a>

- Website: [alasql.org](http://AlaSQL.org)

## Please note

**All contributions are extremely welcome and greatly appreciated(!)** -
The project has never received any funding and is based on unpaid voluntary work: [We really (really) love pull requests](https://github.com/alasql/alasql/blob/develop/CONTRIBUTING.md)

The AlaSQL project depends on your contribution of code and <s>may</s> have [bugs](https://github.com/alasql/alasql/labels/%21%20Bug). So please, submit any bugs and suggestions [as an issue](https://github.com/alasql/alasql/issues/new).

Please check out the [limitations of the library](https://github.com/alasql/alasql#limitations).

## Performance

AlaSQL is designed for speed and includes some of the classic SQL engine optimizations:

- Queries are cached as compiled functions
- Joined tables are pre-indexed
- `WHERE` expressions are pre-filtered for joins

See more [performance-related info on the wiki](https://github.com/alasql/alasql/wiki/Speed)

## Features you might like

### Traditional SQL

Use "good old" SQL on your data with multiple levels of: `JOIN`, `VIEW`, `GROUP BY`, `UNION`, `PRIMARY KEY`, `ANY`, `ALL`, `IN`, `ROLLUP()`, `CUBE()`, `GROUPING SETS()`, `CROSS APPLY`, `OUTER APPLY`, `WITH SELECT`, and subqueries. [The wiki lists supported SQL statements and keywords](https://github.com/alasql/alasql/wiki/SQL%20keywords).

### User-Defined Functions in your SQL

You can use all benefits of SQL and JavaScript together by defining your own custom functions. Just add new functions to the alasql.fn object:

```js
alasql.fn.myfn = function (a, b) {
	return a * b + 1;
};
var res = alasql('SELECT myfn(a,b) FROM one');
```

You can also define your own aggregator functions (like your own `SUM(...)`). See more [in the wiki](https://github.com/alasql/alasql/wiki/User-Defined-Functions)

### Compiled statements and functions

```js
var ins = alasql.compile('INSERT INTO one VALUES (?,?)');
ins(1, 10);
ins(2, 20);
```

See more [in the wiki](https://github.com/alasql/alasql/wiki/Compile)

### SELECT against your JavaScript data

Group your JavaScript array of objects by field and count number of records in each group:

```js
var data = [
	{a: 1, b: 1, c: 1},
	{a: 1, b: 2, c: 1},
	{a: 1, b: 3, c: 1},
	{a: 2, b: 1, c: 1},
];
var res = alasql('SELECT a, COUNT(*) AS b FROM ? GROUP BY a', [data]);
```

See more ideas for creative data manipulation [in the wiki](https://github.com/alasql/alasql/wiki/Getting-started)

### JavaScript Sugar

AlaSQL extends "good old" SQL to make it closer to JavaScript. The "sugar" includes:

- Write Json objects - `{a:'1',b:@['1','2','3']}`

- Access object properties - `obj->property->subproperty`
- Access object and arrays elements - `obj->(a*1)`
- Access JavaScript functions - `obj->valueOf()`
- Format query output with `SELECT VALUE, ROW, COLUMN, MATRIX`
- Output nested objects with `INTO OBJECT()` - converts arrow notation columns back to nested structure
- ES5 multiline SQL with `var SQL = function(){/*SELECT 'MY MULTILINE SQL'*/}` and pass instead of SQL string (will not work if you compress your code)

#### Extracting Nested Properties with INTO OBJECT()

When selecting nested properties using arrow notation (`->`), results are normally flattened with the arrow path as the key. Use `INTO OBJECT()` to restore the nested structure:

```js
var data = [{name: 'Oslo', info: {country: 'Norway', population: 700000}}];

// Standard output (flattened)
alasql('SELECT name, info->country FROM ?', [data]);
// [{ "name": "Oslo", "info->country": "Norway" }]

// With INTO OBJECT() (nested)
alasql('SELECT name, info->country INTO OBJECT() FROM ?', [data]);
// [{ "name": "Oslo", "info": { "country": "Norway" } }]
```

### Read and write Excel and raw data files

You can import from and export to CSV, TAB, TXT, and JSON files. File extensions can be omitted. Calls to files will always be asynchronous so multi-file queries should be chained:

```js
var tabFile = 'mydata.tab';

alasql
	.promise([
		"SELECT * FROM txt('MyFile.log') WHERE [0] LIKE 'M%'", // parameter-less query
		['SELECT * FROM tab(?) ORDER BY [1]', [tabFile]], // [query, array of params]
		"SELECT [3] AS city,[4] AS population FROM csv('./data/cities')",
		"SELECT * FROM json('../config/myJsonfile')",
	])
	.then(function (results) {
		console.log(results);
	})
	.catch(console.error);
```

### Read SQLite database files

AlaSQL can read (but not write) SQLite data files using [SQL.js](https://github.com/sql-js/sql.js) library:

```html
<script src="alasql.js"></script>
<script src="sql.js"></script>
<script>
	alasql([
		'ATTACH SQLITE DATABASE Chinook("Chinook_Sqlite.sqlite")',
		'USE Chinook',
		'SELECT * FROM Genre',
	]).then(function (res) {
		console.log('Genres:', res.pop());
	});
</script>
```

`sql.js` calls will always be asynchronous.

### AlaSQL works in the console - CLI

The node module ships with an `alasql` command-line tool:

```bash
$ npm install -g alasql ## install the module globally

$ alasql -h ## shows usage information

$ alasql "SET @data = @[{a:'1',b:?},{a:'2',b:?}]; SELECT a, b FROM @data;" 10 20
[ 1, [ { a: 1, b: 10 }, { a: 2, b: 20 } ] ]

$ alasql "VALUE OF SELECT COUNT(*) AS abc FROM TXT('README.md') WHERE LENGTH([0]) > ?" 140
// Number of lines with more than 140 characters in README.md
```

[More examples are included in the wiki](https://github.com/alasql/alasql/wiki/AlaSQL-CLI)

## Features you might love

### AlaSQL ♥ D3.js

AlaSQL plays nice with d3.js and gives you a convenient way to integrate a specific subset of your data with the visual powers of D3. See more about [D3.js and AlaSQL in the wiki](https://github.com/alasql/alasql/wiki/d3.js)

### AlaSQL ♥ Excel

AlaSQL can export data to both [Excel 2003 (.xls)](https://github.com/alasql/alasql/wiki/XLS) and [Excel 2007 (.xlsx)](https://github.com/alasql/alasql/wiki/XLSX) formats with coloring of cells and other Excel formatting functions.

### AlaSQL ♥ Meteor

Meteor is amazing. You can query directly on your Meteor collections with SQL - simple and easy. See more about [Meteor and AlaSQL in the wiki](https://github.com/alasql/alasql/wiki/Meteor)

### AlaSQL ♥ Angular.js

Angular is great. In addition to normal data manipulation, AlaSQL works like a charm for exporting your present scope to Excel. See more about [Angular and AlaSQL in the wiki](https://github.com/alasql/alasql/wiki/Angular.js)

### AlaSQL ♥ Google Maps

Pinpointing data on a map should be easy. AlaSQL is great to prepare source data for Google Maps from, for example, Excel or CSV, making it one unit of work for fetching and identifying what's relevant. See more about [Google Maps and AlaSQL in the wiki](https://github.com/alasql/alasql/wiki/Google-maps)

### AlaSQL ♥ Google Spreadsheets

AlaSQL can query data directly from a Google spreadsheet. A good "partnership" for easy editing and powerful data manipulation. See more about [Google Spreadsheets and AlaSQL in the wiki](https://github.com/alasql/alasql/wiki/Google-Spreadsheets)

### Miss a feature?

Take charge and [add your idea](http://feathub.com/alasql/alasql/features/new) or [vote for your favorite feature](http://feathub.com/alasql/alasql) to be implemented:

[![Feature Requests](http://feathub.com/alasql/alasql?format=svg)](http://feathub.com/alasql/alasql)

## Limitations

Please be aware that AlaSQL has [bugs](https://github.com/alasql/alasql/labels/Bug). Beside having some bugs, there are a number of limitations:

0. AlaSQL has a (long) list of keywords that must be escaped if used for column names. When selecting a field named `key` please write ``SELECT `key` FROM ...`` instead. This is also the case for words like `` `value` ``, `` `read` ``, `` `count` ``, `` `by` ``, `` `top` ``, `` `path` ``, `` `deleted` ``, `` `work` `` and `` `offset` ``. Please consult the [full list of keywords](https://github.com/alasql/alasql/wiki/AlaSQL-Keywords).

1. It is OK to `SELECT` 1000000 records or to `JOIN` two tables with 10000 records in each (You can use streaming functions to work with longer datasources - see [test/test143.js](test/test143.js)) but be aware that the workload is multiplied so `SELECT`ing from more than 8 tables with just 100 rows in each will show b
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# Changelog

Please see https://github.com/AlaSQL/alasql/releases for more info...

## 0.7.1 (2021-03-05)

- Bump: Update lodash dependency


## 0.7.0 (2021-03-03)

- Fix: Code injection vulnerability processing literals
- Fix: Return empty results in group by when input is empty #927



### 0.6.5 (11.11.2020)

- Fix: Do not include null in COUNT or AVG fixes #1251


### 0.6.4 (24.09.2020)

- Add: String and Number objects supported as values
- Add: `JOIN USING` now supports String and Number objects 
- Fix: File naming when exporting to Exel


### 0.6.2 (31.05.2020)


- Add: Use NOT BETWEEN without parenthesis. 



### 0.6.1 (20.05.2020)

- Add: Use BETWEEN without parenthesis. 
- Fix: Let ADD COLUMN use the given dbtypeid



## 0.6.0 (02.05.2020)

- Add: NULLS FIRST/LAST clause in ORDER BY (#1187)
- Add: Support table/row names starting with numbers



### 0.5.9 (26.04.2020)

- Add: Composite foreign keys implementation (#1179) 
- Fix: Insert's toString() (#1177)
- Fix: DROP Filestorage Database with database name (#1184)

### 0.5.8 (27.03.2020)

- Fix: usage of CURRENT_TIMESTAMP (Fix #1174)

### 0.5.6 "Bafq" (22.03.2020)

- Add: GroupBy within nested array data set/params (#1167)
- Fix: Use unknown DB name

### 0.5.5 "Bam" (29.01.2020)

- Fix: Typescript typing

### 0.5.4 "Qom" (19.01.2020)

- Fix: QUART/MEDIAN/MIN/MAX on number/date/string


### 0.5.3 "Chabahar" (02.01.2020)

- Better: Support csv data from buffer
- Better: Error message for foreign key constraint fail #1009
- Fix: ORDER BY supports parameters #1100
- Fix: Filestorage DELETE FROM #624
- Fix: Drop trigger #1113


## 0.5.1 "Qazvin" (16.09.2019)

- Add: Chain OUTER JOIN's #1105
- Better: Typescript typings
- Better: Updated dependencies
- Fix: Join on CSV files directly
- Fix: OUTER JOIN bug #1101
- Fix: Pivot function cast for SUM and AVG 


### 0.4.11 "Lawdar" (05.10.2018)

* Add: Specified XLSX sheet without knowing the name


### 0.4.10 "Maoshk" (04.10.2018)


* Add: xlsxml files with multiple sheets


### 0.4.9 "Alsalfiah" (05.08.2018)

* Better: Error message grammar
* Better: Support for Meteor code standards
* Fix: dbprecision for select query
* Fix: Handle promise error when reading one line csv files
* Fix: AUTO_INCREMENT when using local storage

### 0.4.8 "Nafhan" (14.07.2018)

* Fix: Error when installing caused by missing cli file in npm


### 0.4.7 "Tarim" (14.07.2018)

* Better: Always find global object 


### 0.4.6 "Rahbah" (14.06.2018)

* Better: `Use strict` mode for javascript 


### 0.4.5 "Marib" (24.01.2018)

* Fix: Aggregate functions applied to empty sets (#964)
* Fix: missing ORDER BY direction when calling toString on AST (#970)
* Fix: Converting the syntax tree back to SQL with multple joins (#972)

### 0.4.4 "Alsowm" (03.12.2017)

* Better: Better usage via unpkg.com
* Better: Better usage via jsdelivr.com


### 0.4.3 "Hajjah" (05.09.2017)

* Update: Removed implicit "any" in definition file
* Fix: Tabletop reads in empty cells as numeric 0 instead of empty string 
* Fix: DISTINCT on emtpy table produced error


### 0.4.2 "Baraqish" (17.08.2017)

* Added: SQL function LTRIM
* Added: SQL function RTRIM
* Better: Remove implicit any in type script definitioni
* Better: Out-of-the-box Webpack and Browserify compatibility without hacks
* Fix: Use created database id on foreign key check as default database

 
### 0.4.1 "Sayhut" (23.07.2017)

* Better: Performace on `distinct` selects 
* Better: Hashing for cashed SQLs 
* Fix: Case insensetive selects from EXCEL
* Fix: Select from empty EXCEL


##0.4.0 "Sanaa" (09.05.2017)
* **Breaking:** OFFSET will now skip the first N rows in a result set before starting to return any rows (before it would skip N-1)
* Add: Quartile aggregators (QUART, QUART2, QUART3)
* Add: Typescript definitoin now supports extensions
* Fix: Aggregate MEDIAN now working with ROLLUP
* Fix: Aggregate STDEV now working with ROLLUP
* Fix: SHOW COLUMNS works with the promise interface 
* Fix: SHOW INDEX works with the promise interface 

### 0.3.9 "Turua" (23.03.2017)
* Add: React native support
* Fix: CSV error when quote set to empty
* Fix: autoExt bug when not set for CSV on read

### 0.3.8 "Wanaka" (15.03.2017)

* Added: Lazy promise notation
* Added: Create user defined function via SQL statement
* Added: Create user defined aggretator via SQL statement 
* Added: Auto extension for filenames on read + write
* Fix: `.xlsx` can now be imported via browser "upload"
* Update: `xls.js` package not needed any more. Only `xlsx` package is needed. 

### 0.3.7 "Niau" (20.02.2017)

* Added: Last `S` in `VALUES` can be omitted when insterting (For the lazy ones)
* Added: The `VALUES` keyword is optional when insterting (For the very lazy ones)
* Fix: Multiple worksheet Excel with custom headers 


### 0.3.6 "Hipu" (24.01.2017)

* Addded: Support for "use strict" 
* Fix: Select.toString() had bugs
* Update: Better and faster deep compare of objects


### 0.3.5 "Maiao" (22.12.2016)
* Added: Import data through AngularJS controllers
* Added: Support for running in VM for nodeJS
* Fix: Typescript definition
* Fix: False negatives for deepequal'ing of extended primitives
* Fix: Double quotation marks in CSV output


### 0.3.4 "Fitii" (09.11.2016)
* Added: trigger `AFTER DELETE`
* Fix: `TRUNCATE TABLE` now works for local storage DB
* Fix: `JOIN` a sub select
* Removed: The `HELP` command (to save space) 


### 0.3.3 "Makemo" (13.10.2016)
* Add: support for VALUE inside checks
* Add: Conflate null and undefined
* Add: Load CSV data from a string
* Add: Warn when server side uses browser build of lib
* Update: typescript definition for native import 
* Update: filesaver.js updated to 1.3.2


### 0.3.2 "Maumu" (05.09.2016)
* Added: Postgres arrays like array[] and text[]
* Added: Allow non-reserved keywords as identifiers
* Fix: Empty tsv/csv files will no longer raise an error
* Fix: alasql.d.ts format
* Fix: Better way to find out if indexedDB is present
* Fix: `null = null` is (now) null, baby.
* Update: Column names first for RECORDSETS


### 0.3.1 "Taravao" (01.08.2016)
* Allow unknown functions to be defined on alasql.fn afterwards
* Easy access to AUTOINCREMENT values
* MEDIAN will ignore null values 
* STDEV will ignore null values


## Version 0.3.0 "Papeete" (25.07.2016)
* Breaking change: CSVs with header will now default have BOM added (for better utf8 support) 
* Added: Constraint names will now be exported in error message
* Added: Web worker now supports .promise notation
* Added: Postgres-specific aliases and fixes
* Added: Make converting to an unknown type result in a noop rather than an error
* Added: Support column types consisting of more than 2 words


### 0.2.7 "Corinth" (30.05.2016)
* Added: Now supports Node 6.0 
* Added: Let .promise return all responses (not just last) 
* Change: Headers set as default true for INTO and FROM statements
* Fix: Back on track (for good) with supporting Meteor 
* Fix: Default tentative string to numbers conversion when reading data from google spreadsheets 
* Update: No need for empty params when async
* Update: Better hashing for cashing


### 0.2.6 "Frikes" (22.04.2016)
* Added: Progress callback
* Change: CLI defaults to pretty print (with option for compressed output as original)
* Fix: Declaring all variables
* Fix: Read XLSX files
* Fix: Selecting a view from localstorage 
* Fix: CREATE VIEW for localStorage engine 
* Fix: Better use for RequireJS
* Update: CLI output is guaranteed to be valid JSON 
* Update: Better error message for missing table or column
* Update: Typescript defenition for .promise
* Update: Empty params not needed for async calls


### 0.2.5 "Polychrono" (23.03.2016)
* Added: Promise chain of queries
* Fix: Remove leading whitespace from fields when importing csv files
* Fix: Set default option for XLSXML
* Fix: Use callbacks consistently 


### 0.2.4 "Exogi" (04.03.2016)
* Added: Central enviroment detection
* Added: SELECT * FROM ? GROUP BY a works as FIRST(*)
* Added: Better detection for browserify, phonegap and cordova
* Fix: CONCAT without space
* Fix: IE11: Reading Excel File
* Fix: Date handeling (in)dependent from locale


### 0.2.3 "Spetses" (01.02.2016)
* Changed: New fast way to calculate aggregators (some parameters changed)
* Added: User defined aggregators
* Fixed: Remove empty Last line in TXT and XLSX
* Changed: {headers:true} now is default option
* Fixed: option.joinstar flag for SELECT * FROM a,b
* Added: EXP() function, ^ now is XOR, ~ binary NOT
* Added: REPLACE() string function (see issue #560)
* Added: NEWID(), UUID() and GEN_RANDOM_UUID() functions for GUID
* Added: DEFAULT for column can be a function (e.g. DEFAULT NEWID())


### 0.2.2 "Mitilini" (15.01.2016)
* Fix: SELECT can use functions from GROUP BY list
* Fix: Bug in NUMERIC type conversion
* Added: functions CEIL/CEILING and FLOOR
* Added: CONCAT to the list of standard functions
* Fix: Bug with primary key after DELETE all
* Fix: Added String() to UPPER() and LOWER() functions 
* Added: PIVOT and UNPIVOT functionality
* Added: REPLACE INTO command (see issue #467)
* Added: ON UPDATE - column constraint
* Fix: COLLATE and UNIQUE KEY words for CREATE TABLE (see issue #452)
* Fix: Added params to SEARCH WHERE function
* Added: TRIGGERs
* Fix: Bug with MATRIX modifier
* Fix: Bug with undefined content variable with IN operation (issue #501)
* Fix: Bug with wrong realizaion of REPLACE INTO (issue #505)
* Added: >>,<<,&,| - binary operations
* Added: || - string concatenation (issue #514)
* Added: GLOB operator
* Fix: >> for binary operation and graphs collisions
* Added: SELECT * FROM INSERTED (for T-SQL like triggers)
* Fix: Added DEFAULT clause to INSERT SELECT statement
* Added: expression NOT NULL operator (issue #507)
* Added and Fix: REINDEX and fixed CREATE INDEX (issues #509, #470)
* Fixed: browser tests, IndexedDB tests, DROP TABLE callback for external engines
* Added: DATETIME2 type for compatibility with T-SQL
* Added: DATEADD() and DATEDIFF() functions in T-SQL style
* Added: CONCAT_WS() function
* Added: OF() selector for SEARCH statement

### 0.2.1 "Rodos" (28.09.2015)
* Added: AlaSQL CLI: Support for --version flag
* Added: AlaSQL CLI: support for CLI exit code 
* Added: AlaSQL CLI: Missing file now won't throw exception (but log error text) nor if its a folder
* Added: Support for using _ as a single wildcard in LIKE queries
* Added: Support for FETCH NEXT syntax in queries (MSSQL/T-SQL)
* Added: SUBSTR() alias for MID() function (for SQLite compatibility)
* Added: LIKE ESCAPE functionality
* Added: REGEXP operator (like MySQL) and REGEXP_LIKE() function (like in Oracle)
* Added: INSERT OR REPLACE VALUE, INSERT OR REPLACE SELECT
* Added: Read Blob as parameter for from-functions like XLS()
* Fix: .CSV files made Excel 2013 compliant 
* Fix: misbehavour related to 'NOT' and '=' predecession
* Fix: alasql running from cordova on iOS


## Version 0.2.0 "Athens" (13.07.2015)
The purpose of this release were hard work on:
* Documentation
* Resolving bugs
* Refactoring code
 
Minor verison updated to sync lib, Meteor and npm version

### 0.1.11 "San Remo" (03.06.2015)
* Code partially refactored with help of bitHound 
* New directory 'partners' added
* Added file for codecomplexity.com

### 0.1.10 "Genova" (31.05.2015 - 02.06.2015)
* CALL procedure() statement
* bitHound advices
* bower.json file updated

### 0.1.9 "Torino" (29.05.2015 - 31.05.2015)
* SERIAL data type added
* Changed package.json
* Sample application AlaSQL Codex (alasql.org/codex)
* Changed type conversion procedure for INTEGER, JSON and other types
* TypeScript definition file: alasql.d.ts

### 0.1.8 "Pisa" (22.05.2015 - 28.05.2015)
* SELECT FROM syntax
* Export to multiple sheets workbook
* SQL-99 features list
* Changed README.md
* PEOPLE.md moved to wiki
* VALUE OF SELECT operator
* bitHound file

### 0.1.7 "Parma" (17.05.2015 - 22.05.2015)
* Fixed BETWEEN AND and AND parsing priority bug (KPI1:95%)
* Fixed SUM() with NULL(undefined) values
* SLT tests run
* select1.test passed 100%
* Set jsdoc environment
* Added 'var y' and functions for NULL and undefined conversions
* Fixed AVG() aggregator for NULL elements
* New gulp commands: 'gulp doc' and 'gulp console'
* Some jsDoc documentation tag added
* Expression statement ( = 2*2 )

### 0.1.6 "Palermo" (13.05.2015 - 17.05.2015)
* SET NOCOUNT OFF (for CREATE and INSERT)
* ROWNUM() and ROW_NUMBER() functions
* Promised version of alasql() - alasql.async() (based on es6-promises)
* SELECT * FROM Json
* SEARCH COMMA selector
* Fixed bug with ORDER BY 1,2,3
* Added subqueries for INSERT/DELETE/UPDATE
* First 'official' ECHO plugin released (REQUIRE ECHO)
* New catalogs added for future plugins
* Meteor package 'agershun:alasql'
* Changed readFile and readBinaryFile to read data from Meteor server
* Added alasql.path
* Test program improved

### 0.1.5 "San Marino" (12.05.2015 - 12.05.2015)
* Added Meteor package (agershun:alasql) - still does not work - skeleton
* Northwind test database - test for speed and SQL
* Added w3 database (Northwind analogue)
* Fixed FOREIGN KEY problem

### 0.1.4 "Napoli" (09.05.2015 - 11.05.2015)
* Convert Meteor/Mongo collections on the fly 
* Added METEOR() from-function
* Fixed $[0] -> $0 for parameters
* utils/2ch.js - utility for minification of AlaSQL (calculate size of economy)
* d3 graph path samples
* alasql.options.autovertex flag - create vertices if not found
* EQ() selector
* LIKE selector
* RETURNS selector - return record with columns like in SELECT
* ALL() and ANY() selectors
* Added CREATE TABLE column UNIQUE constraint on INSERT/DELETE/UPDATE
* Added OBJECT_ID() function (like in T-SQL)
* Added parts and optional for specific database compatibility
* Changed REFERENCES syntax
* dbo always as default database (for some compatibility with T-SQL)
* NOT NULL check on INSERT/UPDATE
* CHECK constraint (for whole table)
* CURRENT_TIMESTAMP function
* UNIQUE constraint (whole table)
* VARCHAR(MAX)
* CHECK constraint for columns
* FOREIGN KEYS for columns and tables

### 0.1.3 "Vaticano" (08.05.2015 - 09.05.2015)
* Check for null values for SEARCH
* ORDER BY for SEARCH operator
* Brackets for SEARCH selectors (WITH() selector)
* SEARCH DISTINCT, UNION ALL, UNION selectors
* Added simple PATH() selector

### 0.1.2 "Firenze" (06.05.2015 - 07.05.2015)
* Simple compilation of SEARCH operator
* SUM(),COUNT(),MIN(),MAX(),FIRST(),LAST() search aggregators
* The # operator, CREATE VERTEX #
* SEARCH # - start with object
* SERCH smth # - test for object
* SEARCH VALUE - leave only one first object in the result
* Bug in browser version (no global object)
* Changed Bower
* CREATE GRAPH
* Minor changes in SEARCH over XML syntax
* New tests added

### 0.1.1 "Milano" (03.05.2015 - 04.05.2015)
* XLSXML() into- function with colors
* $$hashKey - remove Angular's key
* CREATE VERTEX, CREATE EDGE
* SEARCH objects
* SEARCH graph
* "name" as name for graph vertices and edges
* Added INSTANCEOF selector
* Added C
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# How to Contribute to AlaSQL

Thank you very much for your interest! AlaSQL has a lot of thing to be improved, and your help is very appreciated! 

For you to submit a pull request: 

- Make sure you have git, Node and yarn installed (`npm install -g yarn`)
- Fork the repo here on Github (button top right)
- Clone your forked repo and install dependencies `git clone https://github.com/MYUSERNAME/alasql/ --depth 1 && cd alasql && yarn` 
- Make sure you work with the develop branch `git checkout develop`
- Make sure you got dependencies installed `yarn`
- Run tests to verify all is good `yarn test`
- Implement a test that reflects the issue.
  - Add a new test file for the issue: Copy `test/test000.js` and replace `000` with a new number. Preferably the number of the issue you are solving.
- Run `yarn test` to verify only the new test fails
- Implement your contributions in `src/`
- Run `yarn test` and verify all tests are OK
- Format the souce with `yarn format`
- Commit changes to git and push to your forked repo
- Click "Create Pull-request" when looking at your forked repo on Github

Please note that 
- `yarn test` will compile from `src/` and overwrite `dist/` before running tests
- If you would like to change the alasql.org website please make a PR to https://github.com/alasql/alasql-org
- To help debug a problem you can see some advice on https://github.com/AlaSQL/alasql/issues/1415#issuecomment-1293335079
 

```

### File: RELEASES.md
```md
# Releases Plan

## Target
The target for AlaSQLdevelopment is a small compact library with size less than 200kb with support of:
a) significant subset of SQL-92 to use the same SQL code on the client and server
b) complex queries on the JavaScript arrays (including search and JSON traversing) 
c) support some simple ETL operations (import-export from CSV and XLS formats)   
d) database backend support (IndexedDB in the first)

Plus some other features, like graphs and others in plug-ins.

## Alasql Development Prioritites
1. Bugs, Speed, Memory Leaks, Better Code, JsDoc, Errors handling, Library Size, Compatibility (Browsers, Mobiles, SQLs)
2. Documentation, alasql.org website, Social Media, Alasql promotion, Article, Coockbook, Tutorial
3. IF problem, UNION bug, merge algorithms, utilities, Prettify, Console, Alacon
4. Transactions
5. PIVOT, UNPIVOT, GROUP BY TOTAL, DETAIL, GROUP BY HIERARCHY
6. WebSQL and pass-thru databases, better support of with IndexedDB and NeDB, WebWorkers
7. SYNC, optimiztic blocking
8. Linq, NoSQL, and MongoDB functions
9. Streams, cursors,while, Console

## Next Releases:

### AlaSQL 0.3
There are some features in the short list for the June-July 2015:
e) extend transactions support
f) add simple triggers or INSERT OR REPLACE operator
g) improve database backend functionality (IndexedDB, localStorage, fileStorage) - especially for mobile applications (Cordova, Meteor).

The target of this phase is to pass SQLLOGIC test. 


### AlaSQL 0.4
h) split alasql.js into core and additional modules to reduce the size of the library
i) add OrientDB support to search over graphs
j) work with memory leaks

### AlaSQL 0.5
k) improve parser to reduce its size, make it faster (especally for INSERT operator), split grammar files by modules



```

### File: SECURITY.md
```md
Hi

Lovely to hear you found a problem. Lets solve it together. 

If you dont feel like writing an issue about it you are welcome to contact Mathias and/or Andrew

- [Mathias Wulff](mailto:hi@mwulff.com)
- [Andrey Gershun](mailto:agershun@gmail.com)


```

### File: TESTLOG.md
```md
# Testlog for AlaSQL

List of final results from [different test runs](https://github.com/alasql/alasql/tree/develop/test/!testlog/) to keep track on progres.  


## SQLlogic

The Sqllogictest was developed by [the SQLite team](https://www.sqlite.org/sqllogictest/doc/trunk/about.wiki) 
to verify that SQL database engine computes correct results by comparing the results to identical queries from other SQL database engines. The full test consists of roughly 6 million SQL statements.

### Node 
* `alasql@0.3.2`
* Total tested: 5,941,494
* Failed tests: 638,370
* Skipped tests: 53,316
* Final score: 88 % was OK

See full result [here](https://github.com/alasql/alasql/tree/develop/test/!testlog/SQLlogic.md)

### Chakra
It has not yet been possible to run the SQLlogic tests on the Chrakra engine. 


## Regression test
The [regression tests for AlaSQL](https://github.com/alasql/alasql/tree/develop/test/) consists of more than 1000 test casescovering [![Coverage]( https://img.shields.io/codecov/c/github/agershun/alasql/develop.svg)](https://rawgit.com/agershun/alasql/develop/test/coverage/lcov-report/dist/alasql.fs.js.html) of the functionality in the library. The regression test is ran everytime the library is compiled from `src/` to `dist/` and must always be 100% OK on Node before releaseing a new version. 

By executing `npm test` the regression test will run via Node. By executing `npm run test:browser` it will run in a browser. 




### Chrome 52
- `alasql@0.3.2-develop-1413`
- Failures: 47
- Passes 1080

See full result [here](https://github.com/alasql/alasql/tree/develop/test/!testlog/Chrome.md)

_It needs more investigations, but as Chrome uses the same V8 engine as Node the errors are likely caused by how some of the tests loads or stores test data. The amount of Chrome errors will be therefor (probably) also be represented in other browsers._ 

### Safari 9
- `alasql@0.3.2-develop-1413`
- Failures: 63
- Passes 1064

See full result [here](https://github.com/alasql/alasql/tree/develop/test/!testlog/Safari.md)


### Firefox 47
- `alasql@0.3.2-develop-1413`
- Failures: 58
- Passes 1069

See full result [here](https://github.com/alasql/alasql/tree/develop/test/!testlog/Firefox.md)

### Edge
- `alasql@0.2.3-develop-1206`
- Failures: 81
- Passes 1034

### Opera 38
- `alasql@0.3.2-develop-1413`
- Failures: 46
- Passes 1081


### Chakra v6.0.0-pre5
- `alasql@0.2.3-develop-1216`
-  1364 passing (2m)
-  66 pending
-  22 failing

See full result [here](https://github.com/alasql/alasql/tree/develop/test/!testlog/Chakra.md)


### Node
- `alasql@0.3.2-develop-1413`
- 1385 passing (2m)
-  83 pending
  


If 100% of the regression test is OK for [the lats commit](https://travis-ci.org/agershun/alasql/builds) this will be green: 

[![Build status](https://api.travis-ci.org/agershun/alasql.svg)](https://travis-ci.org/agershun/alasql?123)

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for alasql
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\CONTRIBUTING.md
```md
# Contributing to making AlaSQL better


Got questions? [Tag a Stack Overflow question](http://stackoverflow.com/questions/ask?tags=AlaSQL) with `alasql`.


Inputs to improvement? [Open an issue](https://github.com/alasql/alasql/issues/new). 


**All contributions are much welcome and greatly appreciated(!)** 

- Make sure you have git, Node and yarn installed (`npm install -g yarn`)
- Fork the repo here on Github (button top right)
- Clone your forked repo and install dependencies `git clone https://github.com/MYUSERNAME/alasql/ --depth 1 && cd alasql && yarn` 
- Make sure you work with the develop branch `git checkout develop`
- Run tests to verify all is good `yarn test`
- Implement a test that reflects the issue.
  - Add a new test file for the issue: Copy `test/test000.js` and replace `000` with a new number. Preferably the number of the issue you are solving.
- Run `yarn test` to verify only the new test fails
- Implement your contributions in `src/`
- Run `yarn test` and verify all tests are OK
- Format the souce with `yarn format`
- Commit changes to git and push to your forked repo
- Click "Create Pull-request" when looking at your forked repo on Github

Please note that 
- `npm test` will compile from `src/` and overwrite `dist/` before running all tests
- If you would like to change the alasql.org website please make a PR to https://github.com/alasql/alasql-org
- To help debug a problem you can see some advice on https://github.com/AlaSQL/alasql/issues/1415#issuecomment-1293335079

```

### File: .github\copilot-instructions.md
```md
# GitHub Copilot Instructions for AlaSQL

## About This Project

AlaSQL is an open source SQL database for JavaScript with a focus on query speed and data source flexibility for both relational data and schemaless data. It works in web browsers, Node.js, and mobile apps.

## When Implementing Features

1. **Understand the issue thoroughly** - Read related test cases and existing code
2. **Write a test first** - Copy test/test000.js into a new file called `test/test###.js` where where `###` is the id of the issue we are trying to solve.
3. **Verify test fails** - Run `yarn test` to confirm the test catches the issue
4. **Implement the fix** - Modify appropriate file(s) in `src/`
  - If you modify the grammar in `src/alasqlgrammar.jison`, run `yarn jison && yarn test` to regenerate the parser and verify
5. **Reconsider elegance** - Make sure to assess the solution and reconsider if this can be more elegant or efficient
6. **Format code** - Run `yarn format` before committing


## Commands

```bash
# Install dependencies
yarn

# Generate grammar (if needed)
yarn jison

# Run tests
yarn test

# Format code
yarn format
```


## Files to Avoid Modifying
- `dist/` - Generated files, will be overwritten on build
- `src/alasqlparser.js` - Generated from Jison grammar (modify the `.jison` file instead)
- `.min.js` files - Generated during build


## Plesae note 

- Alasql is meant to return `undefined` instead of `null` (unline regular SQL engines)

## Resources

- [AlaSQL Documentation](https://github.com/alasql/alasql/wiki)
- [Issue Tracker](https://github.com/AlaSQL/alasql/issues)

```

### File: .github\ISSUE_TEMPLATE.md
```md

AlaSQL is based on unpaid voluntary work. Thank you for taking the time to make it better.


Got ChatGPT?
============

- Try the AlaSQL Bot for answering questions and helping you out with your programming. It has all the documentation and heaps of examples.

- https://chat.openai.com/g/g-XcBL24WTe-alasql-bot


Something is not working as expected?
====================================

- Describe the problem.

- Provide data and code that replicates the problem.

- We suggest spawning a jsfiddle from https://jsfiddle.net/b5ajLveq/

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md

Thank you for the time you are putting into AlaSQL!



```

### File: docs\PRECOMPILE.md
```md

### Transform SQL to JavaScript code

If you want to fiddle with speed you can pre-generate the JS code that will be running your query. 

The returned function has the signature `function(params, cb)` and is designed to be called with `alasql` as context.

```js
import alasql from 'alasql';
import {compileToJS} from 'alasql/precompile';

const jsCode = compileToJS('SELECT * FROM ? WHERE pop > 1000000', 'my_db');

const selectPop = new Function('return ' + jsCode)().bind(alasql);

// Now you can call it like a regular alasql function, but without the SQL
let data = [{city: 'Copenhagen', pop: 1300000}, {city: 'Aarhus', pop: 300000}];
let res = selectPop([data]);
// res will be [{city: 'Copenhagen', pop: 1300000}]
```

This example is not useful in it self, as it is all done during exeuction time (you could just as well have used alasql.compile() directly). However, if you precompile the function at build time, it can be a significant performance boost as the execution don't have to parse the SQL. There is an example of how to do this with Bun in [examples/precompileJS](https://github.com/AlaSQL/alasql/tree/develop/examples/precompileJS)


---------


# AlaSQL Precompile Module

This module provides SQL compilation functionality that allows you to pre-compile SQL queries into JavaScript code, skipping SQL parsing on execution.

The functionality is experimental - so proceed with caution and expect changes.

## Installation

```javascript
import { compileToJS } from 'alasql/precompile';
```

## Functions

### `compileToJS(sql, databaseid?)` - Precompile

Compiles a SQL statement to JavaScript source code that expects an AlaSQL engine as `this`. This is useful for performance optimization as it eliminates SQL parsing overhead at runtime.

**Parameters:**
- `sql` (string): SQL statement to compile
- `databaseid` (string, optional): Database identifier

**Returns:** Generated JavaScript source code string

## Usage Example

```javascript
import { compileToJS } from 'alasql/precompile';

const sql = 'SELECT name, age FROM users WHERE age > ?';
const jsCode = compileToJS(sql);

// Create a function from the compiled code
const queryFn = new Function('return ' + jsCode)().bind(alasql);

// Execute the function (requires AlaSQL)
const result = queryFn([users, 18]);
```

## Build-time Compilation

You can use this function with build tools like Bun, Vite, or Webpack to compile SQL queries at build time:

```javascript
// Using Bun macro for precompile
import { compileToJS } from './my-queries.js' with { type: 'macro' };

const queryFn = new Function('return ' + compileToJS('SELECT * FROM users'))().bind(alasql);
```

## Benefits

- **Performance**: Eliminate SQL parsing overhead at runtime
- **Flexibility**: Still has access to full AlaSQL functionality
- **Debugging**: Can still use AlaSQL debugging tools
- **Works with database tables**: Supports both parameterized queries and database tables

```

