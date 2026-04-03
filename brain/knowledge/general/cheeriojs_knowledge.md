---
id: cheeriojs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:01.041962
---

# KNOWLEDGE EXTRACT: cheeriojs
> **Extracted on:** 2026-03-30 17:31:17
> **Source:** cheeriojs

---

## File: `cheerio.md`
```markdown
# 📦 cheeriojs/cheerio [🔖 PENDING/APPROVE]
🔗 https://github.com/cheeriojs/cheerio
🌐 https://cheerio.js.org

## Meta
- **Stars:** ⭐ 30234 | **Forks:** 🍴 1689
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The fast, flexible, and elegant library for parsing and manipulating HTML and XML.

## README (trích đầu)
```
<h1 align="center">cheerio</h1>

<h5 align="center">The fast, flexible, and elegant library for parsing and manipulating HTML and XML.</h5>

<div align="center">
  <a href="https://github.com/cheeriojs/cheerio/actions/workflows/ci.yml">
    <img src="https://github.com/cheeriojs/cheerio/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  </a>
  <a href="https://coveralls.io/github/cheeriojs/cheerio">
    <img src="https://img.shields.io/coveralls/github/cheeriojs/cheerio/main" alt="Coverage">
  </a>
  <a href="#backers">
    <img src="https://img.shields.io/opencollective/backers/cheerio" alt="OpenCollective backers">
  </a>
  <a href="#sponsors">
    <img src="https://img.shields.io/opencollective/sponsors/cheerio" alt="OpenCollective sponsors">
  </a>
</div>

<br>

[中文文档 (Chinese Readme)](https://github.com/cheeriojs/cheerio/wiki/Chinese-README)

```js
import * as cheerio from 'cheerio';
const $ = cheerio.load('<h2 class="title">Hello world</h2>');

$('h2.title').text('Hello there!');
$('h2').addClass('welcome');

$.html();
//=> <html><head></head><body><h2 class="title welcome">Hello there!</h2></body></html>
```

## Installation

Install Cheerio using a package manager like npm, yarn, or bun.

```bash
npm install cheerio
# or
bun add cheerio
```

## Features

**&#10084; Proven syntax:** Cheerio implements a subset of core jQuery. Cheerio
removes all the DOM inconsistencies and browser cruft from the jQuery library,
revealing its truly gorgeous API.

**&#991; Blazingly fast:** Cheerio works with a very simple, consistent DOM
model. As a result parsing, manipulating, and rendering are incredibly
efficient.

**&#10049; Incredibly flexible:** Cheerio wraps around
[parse5](https://github.com/inikulin/parse5) for parsing HTML and can optionally
use the forgiving [htmlparser2](https://github.com/fb55/htmlparser2/). Cheerio
can parse nearly any HTML or XML document. Cheerio works in both browser and
server environments.

## API

### Loading

First you need to load in the HTML. This step in jQuery is implicit, since
jQuery operates on the one, baked-in DOM. With Cheerio, we need to pass in the
HTML document.

```js
// ESM or TypeScript:
import * as cheerio from 'cheerio';

// In other environments:
const cheerio = require('cheerio');

const $ = cheerio.load('<ul id="fruits">...</ul>');

$.html();
//=> <html><head></head><body><ul id="fruits">...</ul></body></html>
```

### Selectors

Once you've loaded the HTML, you can use jQuery-style selectors to find elements
within the document.

#### \$( selector, [context], [root] )

`selector` searches within the `context` scope which searches within the `root`
scope. `selector` and `context` can be a string expression, DOM Element, array
of DOM elements, or cheerio object. `root`, if provided, is typically the HTML
document string.

This selector method is the starting point for traversing and manipulating the
document. Like in jQuery, it's the primary method for selecting elements in the
document.

```
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `dom-serializer.md`
```markdown
# 📦 cheeriojs/dom-serializer [🔖 PENDING/APPROVE]
🔗 https://github.com/cheeriojs/dom-serializer


## Meta
- **Stars:** ⭐ 142 | **Forks:** 🍴 72
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
render dom nodes

## README (trích đầu)
```
# dom-serializer [![Node.js CI](https://github.com/cheeriojs/dom-serializer/actions/workflows/nodejs-test.yml/badge.svg)](https://github.com/cheeriojs/dom-serializer/actions/workflows/nodejs-test.yml)

Renders a [domhandler](https://github.com/fb55/domhandler) DOM node or an array of domhandler DOM nodes to a string.

```js
import render from "dom-serializer";

// OR

const render = require("dom-serializer").default;
```

# API

## `render`

▸ **render**(`node`: Node \| Node[], `options?`: [_Options_](#Options)): _string_

Renders a DOM node or an array of DOM nodes to a string.

Can be thought of as the equivalent of the `outerHTML` of the passed node(s).

#### Parameters:

| Name      | Type                               | Default value | Description                    |
| :-------- | :--------------------------------- | :------------ | :----------------------------- |
| `node`    | Node \| Node[]                     | -             | Node to be rendered.           |
| `options` | [_DomSerializerOptions_](#Options) | {}            | Changes serialization behavior |

**Returns:** _string_

## Options

### `encodeEntities`

• `Optional` **decodeEntities**: _boolean | "utf8"_

Encode characters that are either reserved in HTML or XML.

If `xmlMode` is `true` or the value not `'utf8'`, characters outside of the ASCII range will be encoded as well.

**`default`** `decodeEntities`

---

### `decodeEntities`

• `Optional` **decodeEntities**: _boolean_

Option inherited from parsing; will be used as the default value for `encodeEntities`.

**`default`** true

---

### `emptyAttrs`

• `Optional` **emptyAttrs**: _boolean_

Print an empty attribute's value.

**`default`** xmlMode

**`example`** With <code>emptyAttrs: false</code>: <code>&lt;input checked&gt;</code>

**`example`** With <code>emptyAttrs: true</code>: <code>&lt;input checked=""&gt;</code>

---

### `selfClosingTags`

• `Optional` **selfClosingTags**: _boolean_

Print self-closing tags for tags without contents. If `xmlMode` is set, this
will apply to all tags. Otherwise, only tags that are defined as self-closing
in the HTML specification will be printed as such.

**`default`** xmlMode

**`example`** With <code>selfClosingTags: false</code>: <code>&lt;foo&gt;&lt;/foo&gt;&lt;br&gt;&lt;/br&gt;</code>

**`example`** With <code>xmlMode: true</code> and <code>selfClosingTags: true</code>: <code>&lt;foo/&gt;&lt;br/&gt;</code>

**`example`** With <code>xmlMode: false</code> and <code>selfClosingTags: true</code>: <code>&lt;foo&gt;&lt;/foo&gt;&lt;br /&gt;</code>

---

### `xmlMode`

• `Optional` **xmlMode**: _boolean_ \| _"foreign"_

Treat the input as an XML document; enables the `emptyAttrs` and `selfClosingTags` options.

If the value is `"foreign"`, it will try to correct mixed-case attribute names.

**`default`** false

---

## Ecosystem

| Name                                                          | Description                                             |
| --------------------------------
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

