---
id: alasql
type: knowledge
owner: OA_Triage
---
# alasql
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "alasql",
	"description": "Use SQL to select and filter javascript data - including relational joins and search in nested objects (JSON). Export to and import from Excel and CSV",
	"version": "4.17.1",
	"author": "Andrey Gershun <agershun@gmail.com>",
	"contributors": [
		"Mathias Wulff <m@rawu.dk>"
	],
	"main": "dist/alasql.fs.js",
	"browser": "dist/alasql.min.js",
	"exports": {
		".": {
			"types": "./types/alasql.d.ts",
			"node": "./dist/alasql.fs.js",
			"browser": "./dist/alasql.min.js",
			"default": "./dist/alasql.fs.js"
		},
		"./precompile": "./dist/precompile/index.js"
	},
	"directories": {
		"test": "test"
	},
	"typings": "types/alasql.d.ts",
	"scripts": {
		"test": "sh build.sh && yarn test-only",
		"test-ci": "(yarn test-format-all || 1) && yarn test-only && yarn install-g && alasql 'select 1 as Succes'",
		"test-only": "node node_modules/mocha/bin/mocha.js ./test --reporter dot --bail",
		"#test-only": "(command -v bun && bun node_modules/.bin/mocha ./test --reporter dot) || npx bun node_modules/.bin/mocha ./test --reporter dot",
		"test-browser": "node test/browserTestRunner.js 7387",
		"test-cover": "# istanbul cover  -x 'lib/zt/zt.js' --dir test/coverage _mocha",
		"build": "yarn format && yarn build-only",
		"build-only": "sh build.sh",
		"install-g": "yarn build && npm uninstall alasql -g && npm install -g .",
		"release": "yarn version",
		"jison": "jison ./src/alasqlparser.jison -o ./src/alasqlparser.js",
		"fmt": "yarn pretty-commit --write",
		"format": "yarn pretty-since-dev --write",
		"format-all": "yarn pretty-all --write",
		"test-format": "yarn pretty-since-dev --list-different || (echo 'Please correct file formatting using `yarn format` and try again.' && exit 1)",
		"test-format-all": "prettier --list-different '{.,src,test}/*.{js,ts,json}' || (echo 'Please correct file formatting using `yarn format-all` and try again.' && exit 1)",
		"pretty-since-dev": "{ git diff --name-only --diff-filter=d origin/develop ; git diff --name-only --diff-filter=d --staged origin/develop ; } | sort | uniq | grep -vE '^dist/|^test/coverage|^lib/|.min.js$' | grep -E '\\.(scss|css|js|ts|vue|json)$' | xargs npx prettier",
		"pretty-commit": "{ git diff --name-only  --diff-filter=d ; git diff --name-only  --diff-filter=d --staged ; } | sort | uniq | grep -vE '^dist/|^test/coverage|^lib/|.min.js$' | grep -E '\\.(scss|css|js|ts|vue|json)$' | xargs npx prettier",
		"pretty-all": "git ls-tree --full-tree --name-only -r HEAD | grep -vE '^dist/|^test/coverage|^lib/|.min.js$' | grep -E '\\.(scss|css|js|ts|vue|json)$' | xargs npx prettier",
		"push": "git push --force-with-lease && git push --no-verify --tags #",
		"repush": "yarn rebase && yarn push",
		"amend": "git reset --soft HEAD~1 && sleep 1 && git add --all && git commit --file .git/COMMIT_EDITMSG # This works with husky hooks",
		"commit": "cmdmix 'git add --all && git commit -am \"%1\"'",
		"add": "git add --all",
		"goto": "git fetch && git checkout",
		"todo": "git ls-tree --full-tree --name-only -r head | xargs grep -inEro '\\Wtodo[ :].*' #",
		"fresh": "cmdmix 'yarn goto '%1' && yarn pull-hard'",
		"pre-pr": "cmdmix 'yarn fresh '%1' && yarn repush'",
		"prepare": "husky",
		"preversion": "yarn && yarn test && npm login",
		"postversion": "npm publish && git push && git push --tags && echo \"Successfully released version $npm_package_version\""
	},
	"dependencies": {
		"cross-fetch": "4.1.0",
		"yargs": "16"
	},
	"optionalDependencies": {
		"react-native-fs": "^2.20.0"
	},
	"devDependencies": {
		"blueimp-md5": "2.19.0",
		"cmdmix": "2.2.2",
		"dom-storage": "2.1.0",
		"esbuild": "0.27.4",
		"git-branch-is": "4.0.0",
		"husky": "9.1.7",
		"jison": "^0.4.18",
		"mocha": "11.7.5",
		"mocha.parallel": "0.15.6",
		"open": "11.0.0",
		"prettier": "3.8.1",
		"react-native-fetch-blob": "^0.10.8",
		"rexreplace": "7.1.14",
		"strftime": "0.10.3",
		"tabletop": "^1.6.2",
		"uglify-js": "3.19.3"
	},
	"resolutions": {
		"got": "14",
		"axios": "^1.13.2",
		"json5": "2",
		"underscore": "1",
		"glob-parent": "6",
		"decode-uri-component": "0.4",
		"semver": "7",
		"follow-redirects": "^1.15.11",
		"js-yaml": "4",
		"glob": "^13.0.0",
		"rimraf": "^6.1.2"
	},
	"overrides": {
		"axios": "^1.13.2",
		"follow-redirects": "^1.15.11",
		"glob": "^13.0.0",
		"rimraf": "^6.1.2"
	},
	"engines": {
		"node": ">=15"
	},
	"repository": {
		"type": "git",
		"url": "http://github.com/alasql/alasql.git"
	},
	"bugs": {
		"url": "https://github.com/alasql/alasql/issues"
	},
	"bin": {
		"alasql": "./bin/alasql-cli.js"
	},
	"homepage": "https://github.com/alasql/alasql",
	"keywords": [
		"SQL",
		"javascript",
		"database",
		"Excel",
		"XLSX",
		"XLS",
		"CSV"
	],
	"license": "MIT",
	"prettier": {
		"useTabs": true,
		"printWidth": 100,
		"singleQuote": true,
		"arrowParens": "avoid",
		"trailingComma": "es5",
		"bracketSpacing": false
	}
}

```

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

### File: FETCHED_alasql_033725\package.json
```json
{
	"name": "alasql",
	"description": "Use SQL to select and filter javascript data - including relational joins and search in nested objects (JSON). Export to and import from Excel and CSV",
	"version": "4.17.1",
	"author": "Andrey Gershun <agershun@gmail.com>",
	"contributors": [
		"Mathias Wulff <m@rawu.dk>"
	],
	"main": "dist/alasql.fs.js",
	"browser": "dist/alasql.min.js",
	"exports": {
		".": {
			"types": "./types/alasql.d.ts",
			"node": "./dist/alasql.fs.js",
			"browser": "./dist/alasql.min.js",
			"default": "./dist/alasql.fs.js"
		},
		"./precompile": "./dist/precompile/index.js"
	},
	"directories": {
		"test": "test"
	},
	"typings": "types/alasql.d.ts",
	"scripts": {
		"test": "sh build.sh && yarn test-only",
		"test-ci": "(yarn test-format-all || 1) && yarn test-only && yarn install-g && alasql 'select 1 as Succes'",
		"test-only": "node node_modules/mocha/bin/mocha.js ./test --reporter dot --bail",
		"#test-only": "(command -v bun && bun node_modules/.bin/mocha ./test --reporter dot) || npx bun node_modules/.bin/mocha ./test --reporter dot",
		"test-browser": "node test/browserTestRunner.js 7387",
		"test-cover": "# istanbul cover  -x 'lib/zt/zt.js' --dir test/coverage _mocha",
		"build": "yarn format && yarn build-only",
		"build-only": "sh build.sh",
		"install-g": "yarn build && npm uninstall alasql -g && npm install -g .",
		"release": "yarn version",
		"jison": "jison ./src/alasqlparser.jison -o ./src/alasqlparser.js",
		"fmt": "yarn pretty-commit --write",
		"format": "yarn pretty-since-dev --write",
		"format-all": "yarn pretty-all --write",
		"test-format": "yarn pretty-since-dev --list-different || (echo 'Please correct file formatting using `yarn format` and try again.' && exit 1)",
		"test-format-all": "prettier --list-different '{.,src,test}/*.{js,ts,json}' || (echo 'Please correct file formatting using `yarn format-all` and try again.' && exit 1)",
		"pretty-since-dev": "{ git diff --name-only --diff-filter=d origin/develop ; git diff --name-only --diff-filter=d --staged origin/develop ; } | sort | uniq | grep -vE '^dist/|^test/coverage|^lib/|.min.js$' | grep -E '\\.(scss|css|js|ts|vue|json)$' | xargs npx prettier",
		"pretty-commit": "{ git diff --name-only  --diff-filter=d ; git diff --name-only  --diff-filter=d --staged ; } | sort | uniq | grep -vE '^dist/|^test/coverage|^lib/|.min.js$' | grep -E '\\.(scss|css|js|ts|vue|json)$' | xargs npx prettier",
		"pretty-all": "git ls-tree --full-tree --name-only -r HEAD | grep -vE '^dist/|^test/coverage|^lib/|.min.js$' | grep -E '\\.(scss|css|js|ts|vue|json)$' | xargs npx prettier",
		"push": "git push --force-with-lease && git push --no-verify --tags #",
		"repush": "yarn rebase && yarn push",
		"amend": "git reset --soft HEAD~1 && sleep 1 && git add --all && git commit --file .git/COMMIT_EDITMSG # This works with husky hooks",
		"commit": "cmdmix 'git add --all && git commit -am \"%1\"'",
		"add": "git add --all",
		"goto": "git fetch && git checkout",
		"todo": "git ls-tree --full-tree --name-only -r head | xargs grep -inEro '\\Wtodo[ :].*' #",
		"fresh": "cmdmix 'yarn goto '%1' && yarn pull-hard'",
		"pre-pr": "cmdmix 'yarn fresh '%1' && yarn repush'",
		"prepare": "husky",
		"preversion": "yarn && yarn test && npm login",
		"postversion": "npm publish && git push && git push --tags && echo \"Successfully released version $npm_package_version\""
	},
	"dependencies": {
		"cross-fetch": "4.1.0",
		"yargs": "16"
	},
	"optionalDependencies": {
		"react-native-fs": "^2.20.0"
	},
	"devDependencies": {
		"blueimp-md5": "2.19.0",
		"cmdmix": "2.2.2",
		"dom-storage": "2.1.0",
		"esbuild": "0.27.4",
		"git-branch-is": "4.0.0",
		"husky": "9.1.7",
		"jison": "^0.4.18",
		"mocha": "11.7.5",
		"mocha.parallel": "0.15.6",
		"open": "11.0.0",
		"prettier": "3.8.1",
		"react-native-fetch-blob": "^0.10.8",
		"rexreplace": "7.1.14",
		"strftime": "0.10.3",
		"tabletop": "^1.6.2",
		"uglify-js": "3.19.3"
	},
	"resolutions": {
		"got": "14",
		"axios": "^1.13.2",
		"json5": "2",
		"underscore": "1",
		"glob-parent": "6",
		"decode-uri-component": "0.4",
		"semver": "7",
		"follow-redirects": "^1.15.11",
		"js-yaml": "4",
		"glob": "^13.0.0",
		"rimraf": "^6.1.2"
	},
	"overrides": {
		"axios": "^1.13.2",
		"follow-redirects": "^1.15.11",
		"glob": "^13.0.0",
		"rimraf": "^6.1.2"
	},
	"engines": {
		"node": ">=15"
	},
	"repository": {
		"type": "git",
		"url": "http://github.com/alasql/alasql.git"
	},
	"bugs": {
		"url": "https://github.com/alasql/alasql/issues"
	},
	"bin": {
		"alasql": "./bin/alasql-cli.js"
	},
	"homepage": "https://github.com/alasql/alasql",
	"keywords": [
		"SQL",
		"javascript",
		"database",
		"Excel",
		"XLSX",
		"XLS",
		"CSV"
	],
	"license": "MIT",
	"prettier": {
		"useTabs": true,
		"printWidth": 100,
		"singleQuote": true,
		"arrowParens": "avoid",
		"trailingComma": "es5",
		"bracketSpacing": false
	}
}

```

### File: FETCHED_alasql_033725\README.md
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

### File: modules\xlsx\README.md
```md
# [SheetJS](https://sheetjs.com)

The SheetJS Community Edition offers battle-tested open-source solutions for
extracting useful data from almost any complex spreadsheet and generating new
spreadsheets that will work with legacy and modern software alike.

[SheetJS Pro](https://sheetjs.com/pro) offers solutions beyond data processing:
Edit complex templates with ease; let out your inner Picasso with styling; make
custom sheets with images/graphs/PivotTables; evaluate formula expressions and
port calculations to web apps; automate common spreadsheet tasks, and much more!

[![Analytics](https://ga-beacon.appspot.com/UA-36810333-1/SheetJS/sheetjs?pixel)](https://github.com/SheetJS/sheetjs)

[![Build Status](https://saucelabs.com/browser-matrix/sheetjs.svg)](https://saucelabs.com/u/sheetjs)

## Documentation

- [API and Usage Documentation](https://docs.sheetjs.com)

- [Downloadable Scripts and Modules](https://cdn.sheetjs.com)

## Related Projects

- <https://oss.sheetjs.com/notes/>: File Format Notes

- [`ssf`](packages/ssf): Format data using ECMA-376 spreadsheet format codes

- [`xlsx-cli`](packages/xlsx-cli/): NodeJS command-line tool for processing files

- [`test_files`](https://github.com/SheetJS/test_files): Sample spreadsheets

- [`cfb`](https://github.com/SheetJS/js-cfb): Container (OLE/ZIP) format library

- [`codepage`](https://github.com/SheetJS/js-codepage): Legacy text encodings

## License

Please consult the attached LICENSE file for details.  All rights not explicitly
granted by the Apache 2.0 License are reserved by the Original Author.


```

### File: src\console\README.md
```md
# Console functions

* ECHO
* PRINT 
```

### File: src\db2\README.md
```md
# DB2 syntax + connector
```

### File: src\debug\README.md
```md
# Debugging functions

ASSERT
```

### File: src\echo\README.md
```md
# Echo Plugin

This is a simple test plugin to support only one command:
```js
    alasql('REQUIRE ECHO');
    var res = alasql('ECHO 123');
```
returns 123
```

### File: src\filestorage\README.md
```md
# Native AlaSQL database backend

```

### File: src\filesystem\README.md
```md
# HTML5 FileSystem backend
```

### File: src\graph\README.md
```md
# AlaSQL Graph functions

* CREATE GRAPH
* Graph SEARCH functions (searchers and selectors)
* Path finding function

```

### File: src\help\README.md
```md
# AlaSQL internal help system

* HELP keyword
```

### File: src\html\README.md
```md
# HTML import-export + connector functions
```

### File: src\indexeddb\README.md
```md
# AlaSQL IndexedDB backend
```

### File: src\linq\README.md
```md
# ALaSQL Fulent interface

```

### File: src\localstorage\README.md
```md
# LocalStorage and SessionStorage database backend
```

### File: src\lovefield\README.md
```md
# AlaSQL Lovefield SQL interface
```

### File: src\md\README.md
```md
﻿# MD (Markdonw) plug-in

This is an example of simple AlaSQL plugin.

```sql
    REQUIRE MD;
    SELECT * INTO MD('RESULTS.md',{headers:true}) FROM one;
```
```

### File: src\mongodb\README.md
```md
# MongoDB AlaSQL interface
```

### File: src\mysql\README.md
```md
# MySQL syntax and pass-thru driver
```

### File: src\neo4j\README.md
```md
# Neo4j syntax + pass-thru connector
```

### File: src\oracle\README.md
```md
# Oracle syntax + pass-thru connector

```

### File: src\orientdb\README.md
```md
# AlaSQL OrientDB plugin

Supported commands:
```
OSELECT 
CREATE CLASS
CREATE VERTEX
CREATE EDGE
```
```

### File: src\postgres\README.md
```md
# Postgres syntax + connector
```

### File: src\pouchdb\README.md
```md
Support PouchDB backend
```

### File: src\precompile\index.js
```js
/**
	AlaSQL Precompile Module
	Provides compileToJS function for generating pre-compiled SQL queries
*/

// Import alasql from the built file
import alasql from '../../dist/alasql.fs.js';

/**
	 Compile SQL statement to JavaScript source code string.
	 Returns pre-compiled function source that skips SQL parsing.
	 The returned function must be bound to alasql context.
	 @param {string} sql SQL statement
	 @param {string} databaseid Database identifier
	 @return {string} Generated JavaScript source code
	*/
export function compileToJS(sql, databaseid) {
	const compiledFn = alasql.compile(sql, databaseid);
	const query = compiledFn.query;

	// Extract compiled functions
	const selectfnStr = query.selectfn ? query.selectfn.toString() : 'null';
	const wherefnStr = query.wherefn ? query.wherefn.toString() : 'null';
	const orderfnStr = query.orderfn ? query.orderfn.toString() : 'null';

	// Extract source information for data fetching
	const sources = query.sources || [];
	const firstSource = sources[0] || {};
	const alias = firstSource.alias ? JSON.stringify(firstSource.alias) : '"default"';
	const tableid = firstSource.tableid ? JSON.stringify(firstSource.tableid) : 'null';
	const srcDatabaseid = firstSource.databaseid
		? JSON.stringify(firstSource.databaseid)
		: JSON.stringify(databaseid || 'alasql');

	// Build wrapper
	const wrapper = `(function(params, cb, scope) {
		const alasql = this;
		const selectfn = ${selectfnStr};
		const wherefn = ${wherefnStr};
		const orderfn = ${orderfnStr};
		const removeKeys = ${JSON.stringify(query.removeKeys || [])};
		const distinct = ${JSON.stringify(query.distinct)};
		const limit = ${JSON.stringify(query.limit)};
		const offset = ${JSON.stringify(query.offset)};
		const alias = ${alias};
		
		// Get data from source (either params or database table)
		let data;
		if (${tableid}) {
			// Query from database table
			const db = alasql.databases[${srcDatabaseid}];
			data = db.tables[${tableid}].data;
		} else if (params && params[0]) {
			// Query from parameter
			data = params[0];
		} else {
			data = [];
		}
		
		// Execute query
		let result = [];
		for (let i = 0; i < data.length; i++) {
			const p = {};
			p[alias] = data[i];
			if (!wherefn || wherefn(p, params, alasql)) {
				const row = selectfn ? selectfn(p, params, alasql) : data[i];
				result.push(row);
			}
		}
		
		// Apply ORDER BY (before removing keys)
		if (orderfn) {
			result.sort(orderfn);
		}
		
		// Remove temporary keys
		if (removeKeys && removeKeys.length > 0) {
			result.forEach(row => {
				removeKeys.forEach(key => delete row[key]);
			});
		}
		
		// Apply DISTINCT
		if (distinct) {
			const seen = new Set();
			result = result.filter(row => {
				const key = JSON.stringify(row);
				if (seen.has(key)) return false;
				seen.add(key);
				return true;
			});
		}
		
		// Apply OFFSET and LIMIT
		if (offset) {
			result = result.slice(offset);
		}
		if (limit) {
			result = result.slice(0, limit);
		}
		
		if (cb) cb(result);
		return result;
	})`;

	return wrapper;
}

```

### File: src\precompile\README.md
```md
# AlaSQL Precompile Module

The precompile module provides the `compileToJS` function to compile SQL queries into JavaScript code that skips SQL parsing on repeated executions.

## Installation

```bash
npm install alasql
```

## Usage

Import the precompile module separately to keep it out of your main bundle:

```javascript
const alasql = require('alasql');
const { compileToJS } = require('alasql/precompile');
```

Or with ES modules:

```javascript
import alasql from 'alasql';
import { compileToJS } from 'alasql/precompile';
```

## API

### `compileToJS(sql, databaseid)`

Compiles an SQL statement into JavaScript source code that skips SQL parsing.

**Parameters:**
- `sql` (string): The SQL statement to compile
- `databaseid` (string, optional): Database identifier

**Returns:** String containing the generated JavaScript function

**Example:**

```javascript
const { compileToJS } = require('alasql/precompile');

// Compile the SQL once
const sql = 'SELECT product, price FROM ? WHERE price > ?';
const jsCode = compileToJS(sql);

// Create the compiled function
const compiledFn = new Function('return ' + jsCode)().bind(alasql);

// Execute many times - NO SQL parsing!
const data = [{product: 'Book', price: 5}, {product: 'Pen', price: 1}];
const result1 = compiledFn([data, 2]);
const result2 = compiledFn([data, 3]);
```


## Use Cases

### 1. Performance-Critical Code

When you need to execute the same SQL query thousands of times:

```javascript
const { compileToJS } = require('alasql/precompile');

// Compile once
const jsCode = compileToJS('SELECT * FROM ? WHERE active = true');
const compiledFn = new Function('return ' + jsCode)().bind(alasql);

// Execute many times (no parsing overhead!)
for (let i = 0; i < 10000; i++) {
  const result = compiledFn([users]);
  // process result...
}
```

### 2. Build-Time Optimization

Generate optimized query functions at build time:

```javascript
const { compileToJS } = require('alasql/precompile');
const fs = require('fs');

const sql = 'SELECT product, price*100 AS cents FROM products WHERE price > 2';
const jsCode = compileToJS(sql);

// Save to file
fs.writeFileSync('queries/getProducts.js', `
  const alasql = require('alasql');
  module.exports = ${jsCode}.bind(alasql);
`);
```

### 3. Reduced Bundle Size

Keep precompile functionality separate from your main bundle:

```javascript
// In your build tool, only import precompile during build
import { compileToJS } from 'alasql/precompile';

// Main app only needs alasql, not precompile
import alasql from 'alasql';
```

## Differences from `alasql.compile()`

| Feature | `alasql.compile()` | `compileToJS()` |
|---------|-------------------|-----------------|
| Returns | Function | String (source code) |
| Portable | No | Yes (requires alasql) |
| SQL parsing | Once | Once |
| Database tables | ✓ | ✓ |
| Parameterized queries | ✓ | ✓ |

## Notes

- The generated code from `compileToJS()` must be bound to an `alasql` instance
- SQL is parsed once during compilation; execution skips the parsing step
- Both database tables and parameterized queries are supported

```

### File: src\pretty\README.md
```md
# Prettyfier functions

alasql.pretty(sql)
```

### File: src\prolog\README.md
```md
# Prolog queries

:-
?-

```

### File: src\sprintf\README.md
```md
# Sprintf and other string formatting functions
```

### File: src\sqlite\README.md
```md
# SQLite syntax + pass-thru connector
```

### File: src\sqljs\README.md
```md
# SQL.js connector

```

### File: src\tabletop\README.md
```md
# Google Spreadsheet connector (with Tableto library)
```

### File: src\tsql\README.md
```md
# T-SQL syntax + SQL Server connector
```

### File: src\websql\README.md
```md
# WebSQL connector
```

### File: src\xls\README.md
```md
# Excel import-export operations
```

### File: src\xml\README.md
```md
# XML parsing and search functions
```

### File: FETCHED_alasql_033725\modules\xlsx\README.md
```md
# [SheetJS](https://sheetjs.com)

The SheetJS Community Edition offers battle-tested open-source solutions for
extracting useful data from almost any complex spreadsheet and generating new
spreadsheets that will work with legacy and modern software alike.

[SheetJS Pro](https://sheetjs.com/pro) offers solutions beyond data processing:
Edit complex templates with ease; let out your inner Picasso with styling; make
custom sheets with images/graphs/PivotTables; evaluate formula expressions and
port calculations to web apps; automate common spreadsheet tasks, and much more!

[![Analytics](https://ga-beacon.appspot.com/UA-36810333-1/SheetJS/sheetjs?pixel)](https://github.com/SheetJS/sheetjs)

[![Build Status](https://saucelabs.com/browser-matrix/sheetjs.svg)](https://saucelabs.com/u/sheetjs)

## Documentation

- [API and Usage Documentation](https://docs.sheetjs.com)

- [Downloadable Scripts and Modules](https://cdn.sheetjs.com)

## Related Projects

- <https://oss.sheetjs.com/notes/>: File Format Notes

- [`ssf`](packages/ssf): Format data using ECMA-376 spreadsheet format codes

- [`xlsx-cli`](packages/xlsx-cli/): NodeJS command-line tool for processing files

- [`test_files`](https://github.com/SheetJS/test_files): Sample spreadsheets

- [`cfb`](https://github.com/SheetJS/js-cfb): Container (OLE/ZIP) format library

- [`codepage`](https://github.com/SheetJS/js-codepage): Legacy text encodings

## License

Please consult the attached LICENSE file for details.  All rights not explicitly
granted by the Apache 2.0 License are reserved by the Original Author.


```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
