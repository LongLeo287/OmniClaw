---
id: fb55-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:23.873373
---

# KNOWLEDGE EXTRACT: fb55
> **Extracted on:** 2026-03-30 17:36:59
> **Source:** fb55

---

## File: `domhandler.md`
```markdown
# 📦 fb55/domhandler [🔖 PENDING/APPROVE]
🔗 https://github.com/fb55/domhandler
🌐 https://domhandler.js.org

## Meta
- **Stars:** ⭐ 364 | **Forks:** 🍴 67
- **Language:** TypeScript | **License:** BSD-2-Clause
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Handler for htmlparser2, to get a DOM

## README (trích đầu)
```
# domhandler [![Node.js CI](https://github.com/fb55/domhandler/actions/workflows/nodejs-test.yml/badge.svg)](https://github.com/fb55/domhandler/actions/workflows/nodejs-test.yml)

The DOM handler creates a tree containing all nodes of a page.
The tree can be manipulated using the [domutils](https://github.com/fb55/domutils)
or [cheerio](https://github.com/cheeriojs/cheerio) libraries and
rendered using [dom-serializer](https://github.com/cheeriojs/dom-serializer) .

## Usage

```javascript
const handler = new DomHandler([ <func> callback(err, dom), ] [ <obj> options ]);
// const parser = new Parser(handler[, options]);
```

Available options are described below.

## Example

```javascript
const { Parser } = require("htmlparser2");
const { DomHandler } = require("domhandler");
const rawHtml =
    "Xyz <script language= javascript>var foo = '<<bar>>';</script><!--<!-- Waah! -- -->";
const handler = new DomHandler((error, dom) => {
    if (error) {
        // Handle error
    } else {
        // Parsing completed, do something
        console.log(dom);
    }
});
const parser = new Parser(handler);
parser.write(rawHtml);
parser.end();
```

Output:

```javascript
[
    {
        data: "Xyz ",
        type: "text",
    },
    {
        type: "script",
        name: "script",
        attribs: {
            language: "javascript",
        },
        children: [
            {
                data: "var foo = '<bar>';<",
                type: "text",
            },
        ],
    },
    {
        data: "<!-- Waah! -- ",
        type: "comment",
    },
];
```

## Option: `withStartIndices`

Add a `startIndex` property to nodes.
When the parser is used in a non-streaming fashion, `startIndex` is an integer
indicating the position of the start of the node in the document.
The default value is `false`.

## Option: `withEndIndices`

Add an `endIndex` property to nodes.
When the parser is used in a non-streaming fashion, `endIndex` is an integer
indicating the position of the end of the node in the document.
The default value is `false`.

---

License: BSD-2-Clause

## Security contact information

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `domutils.md`
```markdown
# 📦 fb55/domutils [🔖 PENDING/APPROVE]
🔗 https://github.com/fb55/domutils
🌐 https://domutils.js.org

## Meta
- **Stars:** ⭐ 223 | **Forks:** 🍴 62
- **Language:** TypeScript | **License:** BSD-2-Clause
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Utilities for working with htmlparser2's DOM

## README (trích đầu)
```
# domutils [![Node.js CI](https://github.com/fb55/domutils/actions/workflows/nodejs-test.yml/badge.svg)](https://github.com/fb55/domutils/actions/workflows/nodejs-test.yml)

Utilities for working with [htmlparser2](https://github.com/fb55/htmlparser2)'s DOM.

All functions are exported as a single module. Look [through the docs](https://domutils.js.org/modules.html) to see what is available.

## Ecosystem

| Name                                                          | Description                                             |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| [htmlparser2](https://github.com/fb55/htmlparser2)            | Fast & forgiving HTML/XML parser                        |
| [domhandler](https://github.com/fb55/domhandler)              | Handler for htmlparser2 that turns documents into a DOM |
| [domutils](https://github.com/fb55/domutils)                  | Utilities for working with domhandler's DOM             |
| [css-select](https://github.com/fb55/css-select)              | CSS selector engine, compatible with domhandler's DOM   |
| [cheerio](https://github.com/cheeriojs/cheerio)               | The jQuery API for domhandler's DOM                     |
| [dom-serializer](https://github.com/cheeriojs/dom-serializer) | Serializer for domhandler's DOM                         |

---

License: BSD-2-Clause

## Security contact information

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `encoding-sniffer.md`
```markdown
# 📦 fb55/encoding-sniffer [🔖 PENDING/APPROVE]
🔗 https://github.com/fb55/encoding-sniffer


## Meta
- **Stars:** ⭐ 6 | **Forks:** 🍴 3
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
HTML encoding sniffer, with stream support

## README (trích đầu)
```
# encoding-sniffer [![Node.js CI](https://github.com/fb55/encoding-sniffer/actions/workflows/nodejs-test.yml/badge.svg)](https://github.com/fb55/encoding-sniffer/actions/workflows/nodejs-test.yml)

An implementation of the HTML Standard's
[encoding sniffing algorithm](https://html.spec.whatwg.org/multipage/syntax.html#encoding-sniffing-algorithm),
with stream support.

This module wraps around [`@exodus/bytes`](https://github.com/ExodusOSS/bytes)
to make decoding buffers and streams incredibly easy.

## Features

- Support for streams
- Support for XML encoding types, including UTF-16 prefixes and
  `<?xml encoding="...">`
- Allows decoding streams and buffers with a single function call

## Installation

```bash
npm install encoding-sniffer
```

## Usage

```js
import { DecodeStream, getEncoding, decodeBuffer } from "encoding-sniffer";

/**
 * All functions accept an optional options object.
 *
 * Available options are (with default values):
 */
const options = {
    /**
     * The maximum number of bytes to sniff. Defaults to `1024`.
     */
    maxBytes: 1024,
    /**
     * The encoding specified by the user. If set, this will only be overridden
     * by a Byte Order Mark (BOM).
     */
    userEncoding: undefined,
    /**
     * The encoding specified by the transport layer. If set, this will only be
     * overridden by a Byte Order Mark (BOM) or the user encoding.
     */
    transportLayerEncodingLabel: undefined,
    /**
     * The default encoding to use, if no encoding can be detected.
     *
     * Defaults to `"windows-1252"`.
     */
    defaultEncoding: "windows-1252",
};

// Use the `DecodeStream` transform stream to automatically decode
// the contents of a stream as they are read
const decodeStream = new DecodeStream(options);

// Or, use the `getEncoding` function to detect the encoding of a buffer
const encoding = getEncoding(buffer, options);

// Use the `decodeBuffer` function to decode the contents of a buffer
const decodedBuffer = decodeBuffer(buffer, options);
```

## Security contact information

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file
for more information.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `entities.md`
```markdown
# 📦 fb55/entities [🔖 PENDING/APPROVE]
🔗 https://github.com/fb55/entities


## Meta
- **Stars:** ⭐ 378 | **Forks:** 🍴 73
- **Language:** TypeScript | **License:** BSD-2-Clause
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
encode & decode HTML & XML entities with ease & speed

## README (trích đầu)
```
# entities [![NPM version](https://img.shields.io/npm/v/entities.svg)](https://npmjs.org/package/entities) [![Downloads](https://img.shields.io/npm/dm/entities.svg)](https://npmjs.org/package/entities) [![Node.js CI](https://github.com/fb55/entities/actions/workflows/nodejs-test.yml/badge.svg)](https://github.com/fb55/entities/actions/workflows/nodejs-test.yml)

Encode & decode HTML & XML entities with ease & speed.

## Features

- 😇 Tried and true: `entities` is used by many popular libraries; eg.
  [`htmlparser2`](https://github.com/fb55/htmlparser2), the official
  [AWS SDK](https://github.com/aws/aws-sdk-js-v3) and
  [`commonmark`](https://github.com/commonmark/commonmark.js) use it to process
  HTML entities.
- ⚡️ Fast: `entities` is the fastest library for decoding HTML entities (as of
  September 2025); see [performance](#performance).
- 🎛 Configurable: Get an output tailored for your needs. You are fine with
  UTF8? That'll save you some bytes. Prefer to only have ASCII characters? We
  can do that as well!

## How to…

### …install `entities`

    npm install entities

### …use `entities`

```javascript
import * as entities from "entities";

// Encoding
entities.escapeUTF8("&#38; ü"); // "&amp;#38; ü"
entities.encodeXML("&#38; ü"); // "&amp;#38; &#xfc;"
entities.encodeHTML("&#38; ü"); // "&amp;&num;38&semi; &uuml;"

// Decoding
entities.decodeXML("asdf &amp; &#xFF; &#xFC; &apos;"); // "asdf & ÿ ü '"
entities.decodeHTML("asdf &amp; &yuml; &uuml; &apos;"); // "asdf & ÿ ü '"
```

## Performance

Benchmarked in September 2025 with Node v24.6.0 on Apple M2 using `tinybench`.
Higher ops/s is better; `avg (μs)` is the mean time per operation.
See `scripts/benchmark.ts` to reproduce.

### Decoding

| Library        | Version | ops/s     | avg (μs) | ±%   | slower |
| -------------- | ------- | --------- | -------- | ---- | ------ |
| entities       | 7.0.0   | 5,838,416 | 175.57   | 0.06 | —      |
| html-entities  | 2.6.0   | 2,919,637 | 347.77   | 0.33 | 50.0%  |
| he             | 1.2.0   | 2,318,438 | 446.48   | 0.70 | 60.3%  |
| parse-entities | 4.0.2   |   852,855 | 1,199.51 | 0.36 | 85.4%  |

### Encoding

| Library        | Version | ops/s     | avg (μs) | ±%   | slower |
| -------------- | ------- | --------- | -------- | ---- | ------ |
| entities       | 7.0.0   | 2,770,115 | 368.09   | 0.11 | —      |
| html-entities  | 2.6.0   | 1,491,963 | 679.96   | 0.58 | 46.2%  |
| he             | 1.2.0   |   481,278 | 2,118.25 | 0.61 | 82.6%  |

### Escaping

| Library        | Version | ops/s     | avg (μs) | ±%   | slower |
| -------------- | ------- | --------- | -------- | ---- | ------ |
| entities       | 7.0.0   | 4,616,468 | 223.84   | 0.17 | —      |
| he             | 1.2.0   | 3,659,301 | 280.76   | 0.58 | 20.7%  |
| html-entities  | 2.6.0   | 3,555,301 | 296.63   | 0.84 | 23.0%  |

Note: Micro-benchmarks may vary across machines and Node versions.

---

## FAQ

> What methods should I actually use to encode my documents?

If your t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `htmlparser2.md`
```markdown
# 📦 fb55/htmlparser2 [🔖 PENDING/APPROVE]
🔗 https://github.com/fb55/htmlparser2
🌐 https://feedic.com/htmlparser2

## Meta
- **Stars:** ⭐ 4812 | **Forks:** 🍴 397
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The fast & forgiving HTML and XML parser

## README (trích đầu)
```
# htmlparser2

[![NPM version](https://img.shields.io/npm/v/htmlparser2.svg)](https://npmjs.org/package/htmlparser2)
[![Downloads](https://img.shields.io/npm/dm/htmlparser2.svg)](https://npmjs.org/package/htmlparser2)
[![Node.js CI](https://github.com/fb55/htmlparser2/actions/workflows/nodejs-test.yml/badge.svg)](https://github.com/fb55/htmlparser2/actions/workflows/nodejs-test.yml)
[![Coverage](https://img.shields.io/coveralls/fb55/htmlparser2.svg)](https://coveralls.io/r/fb55/htmlparser2)

The fast & forgiving HTML/XML parser.

_htmlparser2 is [the fastest HTML parser](#performance), and takes some shortcuts to get there. If you need strict HTML spec compliance, have a look at [parse5](https://github.com/inikulin/parse5)._

## Installation

    npm install htmlparser2

A live demo of `htmlparser2` is available [on AST Explorer](https://astexplorer.net/#/2AmVrGuGVJ).

## Ecosystem

| Name                                                          | Description                                             |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| [htmlparser2](https://github.com/fb55/htmlparser2)            | Fast & forgiving HTML/XML parser                        |
| [domhandler](https://github.com/fb55/domhandler)              | Handler for htmlparser2 that turns documents into a DOM |
| [domutils](https://github.com/fb55/domutils)                  | Utilities for working with domhandler's DOM             |
| [css-select](https://github.com/fb55/css-select)              | CSS selector engine, compatible with domhandler's DOM   |
| [cheerio](https://github.com/cheeriojs/cheerio)               | The jQuery API for domhandler's DOM                     |
| [dom-serializer](https://github.com/cheeriojs/dom-serializer) | Serializer for domhandler's DOM                         |

## Usage

`htmlparser2` itself provides a callback interface that allows consumption of documents with minimal allocations.
For a more ergonomic experience, read [Getting a DOM](#getting-a-dom) below.

```js
import * as htmlparser2 from "htmlparser2";

const parser = new htmlparser2.Parser({
    onopentag(name, attributes) {
        /*
         * This fires when a new tag is opened.
         *
         * If you don't need an aggregated `attributes` object,
         * have a look at the `onopentagname` and `onattribute` events.
         */
        if (name === "script" && attributes.type === "text/javascript") {
            console.log("JS! Hooray!");
        }
    },
    ontext(text) {
        /*
         * Fires whenever a section of text was processed.
         *
         * Note that this can fire at any point within text and you might
         * have to stitch together multiple pieces.
         */
        console.log("-->", text);
    },
    onclosetag(tagname) {
        /*
         * Fires when a tag is closed.
         *
         * You can rely on this event only firing when you have recei
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

