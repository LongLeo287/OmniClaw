---
id: micromatch-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.790153
---

# KNOWLEDGE EXTRACT: micromatch
> **Extracted on:** 2026-03-30 17:42:48
> **Source:** micromatch

---

## File: `anymatch.md`
```markdown
# 📦 micromatch/anymatch [🔖 PENDING/APPROVE]
🔗 https://github.com/micromatch/anymatch


## Meta
- **Stars:** ⭐ 402 | **Forks:** 🍴 43
- **Language:** JavaScript | **License:** ISC
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
:bangbang: Matches strings against configurable strings, globs, regular expressions, and/or functions

## README (trích đầu)
```
anymatch [![Build Status](https://travis-ci.org/micromatch/anymatch.svg?branch=master)](https://travis-ci.org/micromatch/anymatch) [![Coverage Status](https://img.shields.io/coveralls/micromatch/anymatch.svg?branch=master)](https://coveralls.io/r/micromatch/anymatch?branch=master)
======
Javascript module to match a string against a regular expression, glob, string,
or function that takes the string as an argument and returns a truthy or falsy
value. The matcher can also be an array of any or all of these. Useful for
allowing a very flexible user-defined config to define things like file paths.

__Note: This module has Bash-parity, please be aware that Windows-style backslashes are not supported as separators. See https://github.com/micromatch/micromatch#backslashes for more information.__


Usage
-----
```sh
npm install anymatch
```

#### anymatch(matchers, testString, [returnIndex], [options])
* __matchers__: (_Array|String|RegExp|Function_)
String to be directly matched, string with glob patterns, regular expression
test, function that takes the testString as an argument and returns a truthy
value if it should be matched, or an array of any number and mix of these types.
* __testString__: (_String|Array_) The string to test against the matchers. If
passed as an array, the first element of the array will be used as the
`testString` for non-function matchers, while the entire array will be applied
as the arguments for function matchers.
* __options__: (_Object_ [optional]_) Any of the [picomatch](https://github.com/micromatch/picomatch#options) options.
    * __returnIndex__: (_Boolean [optional]_) If true, return the array index of
the first matcher that that testString matched, or -1 if no match, instead of a
boolean result.

```js
const anymatch = require('anymatch');

const matchers = [ 'path/to/file.js', 'path/anyjs/**/*.js', /foo.js$/, string => string.includes('bar') && string.length > 10 ] ;

anymatch(matchers, 'path/to/file.js'); // true
anymatch(matchers, 'path/anyjs/baz.js'); // true
anymatch(matchers, 'path/to/foo.js'); // true
anymatch(matchers, 'path/to/bar.js'); // true
anymatch(matchers, 'bar.js'); // false

// returnIndex = true
anymatch(matchers, 'foo.js', {returnIndex: true}); // 2
anymatch(matchers, 'path/anyjs/foo.js', {returnIndex: true}); // 1

// any picomatc

// using globs to match directories and their children
anymatch('node_modules', 'node_modules'); // true
anymatch('node_modules', 'node_modules/somelib/index.js'); // false
anymatch('node_modules/**', 'node_modules/somelib/index.js'); // true
anymatch('node_modules/**', '/absolute/path/to/node_modules/somelib/index.js'); // false
anymatch('**/node_modules/**', '/absolute/path/to/node_modules/somelib/index.js'); // true

const matcher = anymatch(matchers);
['foo.js', 'bar.js'].filter(matcher);  // [ 'foo.js' ]
anymatch master* ❯

```

#### anymatch(matchers)
You can also pass in only your matcher(s) to get a curried function that has
already been bound to the provide
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `picomatch.md`
```markdown
# 📦 micromatch/picomatch [🔖 PENDING/APPROVE]
🔗 https://github.com/micromatch/picomatch
🌐 https://github.com/micromatch

## Meta
- **Stars:** ⭐ 1228 | **Forks:** 🍴 81
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Blazing fast and accurate glob matcher written JavaScript, with no dependencies and full support for standard and extended Bash glob features, including braces, extglobs, POSIX brackets, and regular expressions. Used by GraphQL, Jest, Astro, Snowpack, Storybook, bulma, Serverless, fdir, Netlify, AWS Amplify, Revogrid, rollup, routify, open-wc, imba, ava, docusaurus, fast-glob, globby, chokidar, anymatch, cloudflare/miniflare, pts, and more than 5 million projects! Please follow picomatch's author: https://github.com/jonschlinkert

## README (trích đầu)
```
<h1 align="center">Picomatch</h1>

<p align="center">
<a href="https://npmjs.org/package/picomatch">
<img src="https://img.shields.io/npm/v/picomatch.svg" alt="version">
</a>
<a href="https://github.com/micromatch/picomatch/actions/workflows/test.yml">
<img src="https://github.com/micromatch/picomatch/actions/workflows/test.yml/badge.svg?branch=master" alt="test status">
</a>
<a href="https://coveralls.io/github/micromatch/picomatch">
<img src="https://img.shields.io/coveralls/github/micromatch/picomatch/master.svg" alt="coverage status">
</a>
<a href="https://npmjs.org/package/picomatch">
<img src="https://img.shields.io/npm/dw/picomatch" alt="downloads">
</a>
</p>

<br>
<br>

<p align="center">
<strong>Blazing fast and accurate glob matcher written in JavaScript.</strong></br>
<em>No dependencies and full support for standard and extended Bash glob features, including braces, extglobs, POSIX brackets, and regular expressions.</em>
</p>

<br>
<br>

## Why picomatch?

* **Lightweight** - No dependencies
* **Minimal** - Tiny API surface. Main export is a function that takes a glob pattern and returns a matcher function.
* **Fast** - Loads in about 2ms (that's several times faster than a [single frame of a HD movie](http://www.endmemo.com/sconvert/framespersecondframespermillisecond.php) at 60fps)
* **Performant** - Use the returned matcher function to speed up repeat matching (like when watching files)
* **Accurate matching** - Using wildcards (`*` and `?`), globstars (`**`) for nested directories, [advanced globbing](#advanced-globbing) with extglobs, braces, and POSIX brackets, and support for escaping special characters with `\` or quotes.
* **Well tested** - Thousands of unit tests

See the [library comparison](#library-comparisons) to other libraries.

<br>
<br>

## Table of Contents

<details><summary> Click to expand </summary>

- [Install](#install)
- [Usage](#usage)
- [API](#api)
  * [picomatch](#picomatch)
  * [.test](#test)
  * [.matchBase](#matchbase)
  * [.isMatch](#ismatch)
  * [.parse](#parse)
  * [.scan](#scan)
  * [.compileRe](#compilere)
  * [.makeRe](#makere)
  * [.toRegex](#toregex)
- [Options](#options)
  * [Picomatch options](#picomatch-options)
  * [Scan Options](#scan-options)
  * [Options Examples](#options-examples)
- [Globbing features](#globbing-features)
  * [Basic globbing](#basic-globbing)
  * [Advanced globbing](#advanced-globbing)
  * [Braces](#braces)
  * [Matching special characters as literals](#matching-special-characters-as-literals)
- [Library Comparisons](#library-comparisons)
- [Benchmarks](#benchmarks)
- [Philosophies](#philosophies)
- [About](#about)
  * [Author](#author)
  * [License](#license)

_(TOC generated by [verb](https://github.com/verbose/verb) using [markdown-toc](https://github.com/jonschlinkert/markdown-toc))_

</details>

<br>
<br>

## Install

Install with [npm](https://www.npmjs.com/):

```sh
npm install --save picomatch
```

<br>

## Usage

The main export is a function that takes a glob 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

