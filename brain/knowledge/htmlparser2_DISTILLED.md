---
id: htmlparser2
type: knowledge
owner: OA_Triage
---
# htmlparser2
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "htmlparser2",
    "version": "12.0.0",
    "description": "Fast & forgiving HTML/XML parser",
    "keywords": [
        "html",
        "parser",
        "streams",
        "xml",
        "dom",
        "rss",
        "feed",
        "atom"
    ],
    "repository": {
        "type": "git",
        "url": "git://github.com/fb55/htmlparser2.git"
    },
    "funding": [
        "https://github.com/fb55/htmlparser2?sponsor=1",
        {
            "type": "github",
            "url": "https://github.com/sponsors/fb55"
        }
    ],
    "license": "MIT",
    "author": "Felix Boehm <me@feedic.com>",
    "sideEffects": false,
    "type": "module",
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "default": "./dist/index.js"
        },
        "./WebWritableStream": {
            "types": "./dist/WebWritableStream.d.ts",
            "default": "./dist/WebWritableStream.js"
        },
        "./WritableStream": {
            "types": "./dist/WritableStream.d.ts",
            "default": "./dist/WritableStream.js"
        }
    },
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "files": [
        "dist",
        "src",
        "!**/*.spec.ts",
        "!src/**/__tests__/**",
        "!src/**/__fixtures__/**",
        "!src/**/__snapshots__/**"
    ],
    "scripts": {
        "build": "tsc",
        "format": "npm run format:es && npm run format:biome",
        "format:biome": "biome check --write .",
        "format:es": "npm run lint:es -- --fix",
        "lint": "npm run lint:es && npm run lint:ts && npm run lint:biome",
        "lint:biome": "biome check .",
        "lint:es": "eslint .",
        "lint:ts": "tsc --noEmit -p tsconfig.eslint.json",
        "prepublishOnly": "npm run build",
        "test": "npm run test:vi && npm run lint",
        "test:vi": "vitest run"
    },
    "dependencies": {
        "domelementtype": "^3.0.0",
        "domhandler": "^6.0.0",
        "domutils": "^4.0.2",
        "entities": "^8.0.0"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.8",
        "@feedic/eslint-config": "^0.3.1",
        "@types/node": "^25.5.0",
        "eslint": "^10.0.3",
        "eslint-config-biome": "^2.1.3",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.57.1",
        "vitest": "^4.1.0"
    },
    "engines": {
        "node": ">=20.19.0"
    }
}

```

### File: README.md
```md
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
         * You can rely on this event only firing when you have received an
         * equivalent opening tag before. Closing tags without corresponding
         * opening tags will be ignored.
         */
        if (tagname === "script") {
            console.log("That's it?!");
        }
    },
});
parser.write(
    "Xyz <script type='text/javascript'>const foo = '<<bar>>';</script>",
);
parser.end();
```

Output (with multiple text events combined):

```
--> Xyz
JS! Hooray!
--> const foo = '<<bar>>';
That's it?!
```

### Parser events

All callbacks are optional. The handler object you pass to `Parser` may implement any subset of these:

| Event                                        | Description                                                                                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `onopentag(name, attribs, isImplied)`        | Opening tag. `attribs` is an object mapping attribute names to values. `isImplied` is `true` when the tag was opened implicitly (HTML mode only). |
| `onopentagname(name)`                        | Emitted for the tag name as soon as it is available (before attributes are parsed).                                                              |
| `onattribute(name, value, quote)`            | Attribute. `quote` is `"` / `'` / `null` (unquoted) / `undefined` (no value, e.g. `disabled`).                                                  |
| `onclosetag(name, isImplied)`                | Closing tag. `isImplied` is `true` when the tag was closed implicitly (HTML mode only).                                                          |
| `ontext(data)`                               | Text content. May fire multiple times for a single text node.                                                                                    |
| `oncomment(data)`                            | Comment (content between `<!--` and `-->`).                                                                                                      |
| `oncdatastart()`                             | Opening of a CDATA section (`<![CDATA[`).                                                                                                        |
| `oncdataend()`                               | End of a CDATA section (`]]>`).                                                                                                                  |
| `onprocessinginstruction(name, data)`        | Processing instruction (e.g. `<?xml ...?>`).                                                                                                     |
| `oncommentend()`                             | Fires after a comment has ended.                                                                                                                 |
| `onparserinit(parser)`                       | Fires when the parser is initialized or reset.                                                                                                   |
| `onreset()`                                  | Fires when `parser.reset()` is called.                                                                                                           |
| `onend()`                                    | Fires when parsing is complete.                                                                                                                  |
| `onerror(error)`                             | Fires on error.                                                                                                                                  |

### Parser options

| Option                   | Type      | Default    | Description                                                                                                                                              |
| ------------------------ | --------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `xmlMode`                | `boolean` | `false`    | Treat the document as XML. This affects entity decoding, self-closing tags, CDATA handling, and more. Set this to `true` for XML, RSS, Atom and RDF feeds. |
| `decodeEntities`         | `boolean` | `true`     | Decode HTML entities (e.g. `&amp;` -> `&`).                                                                                                              |
| `lowerCaseTags`          | `boolean` | `!xmlMode` | Lowercase tag names.                                                                                                                                     |
| `lowerCaseAttributeNames`| `boolean` | `!xmlMode` | Lowercase attribute names.                                                                                                                               |
| `recognizeSelfClosing`   | `boolean` | `xmlMode`  | Recognize self-closing tags (e.g. `<br/>`). Always enabled in `xmlMode`.                                                                                 |
| `recognizeCDATA`         | `boolean` | `xmlMode`  | Recognize CDATA sections as text. Always enabled in `xmlMode`.                                                                                           |

### Usage with streams

While the `Parser` interface closely resembles Node.js streams, it's not a 100% match.
Use the `WritableStream` interface to process a streaming input:

```js
import { WritableStream } from "htmlparser2/WritableStream";

const parserStream = new WritableStream({
    ontext(text) {
        console.log("Streaming:", text);
    },
});

const htmlStream = fs.createReadStream("./my-file.html");
htmlStream.pipe(parserStream).on("finish", () => console.log("done"));
```

## Getting a DOM

The `parseDocument` helper parses a string and returns a DOM tree (a [`Document`](https://github.com/fb55/domhandler) node).

```js
import * as htmlparser2 from "htmlparser2";

const dom = htmlparser2.parseDocument(
    `<ul id="fruits">
        <li class="apple">Apple</li>
        <li class="orange">Orange</li>
    </ul>`,
);
```

`parseDocument` accepts an optional second argument with both parser and [DOM handler options](https://github.com/fb55/domhandler):

```js
const dom = htmlparser2.parseDocument(data, {
    // Parser options
    xmlMode: true,

    // domhandler options
    withStartIndices: true, // Add `startIndex` to each node
    withEndIndices: true,   // Add `endIndex` to each node
});
```

### Searching the DOM

The [`DomUtils`](https://github.com/fb55/domutils) module (re-exported on the main `htmlparser2` export) provides helpers for finding nodes:

```js
import * as htmlparser2 from "htmlparser2";

const dom = htmlparser2.parseDocument(`<div><p id="greeting">Hello</p></div>`);

// Find elements by ID, tag name, or class
const greeting = htmlparser2.DomUtils.getElementById("greeting", dom);
const paragraphs = htmlparser2.DomUtils.getElementsByTagName("p", dom);

// Find elements with custom test functions
const all = htmlparser2.DomUtils.findAll(
    (el) => el.attribs?.class === "active",
    dom,
);

// Get text content
htmlparser2.DomUtils.textContent(greeting); // "Hello"
```

For CSS selector queries, use [`css-select`](https://github.com/fb55/css-select):

```js
import { selectAll, selectOne } from "css-select";

const results = selectAll("ul#fruits > li", dom);
const first = selectOne("li.apple", dom);
```

Or, if you'd prefer a jQuery-like API, use [`cheerio`](https://github.com/cheeriojs/cheerio).

### Modifying and serializing the DOM

Use `DomUtils` to modify the tree, and [`dom-serializer`](https://github.com/cheeriojs/dom-serializer) (also available as `DomUtils.getOuterHTML`) to serialize it back to HTML:

```js
import * as htmlparser2 from "htmlparser2";

const dom = htmlparser2.parseDocument(
    `<ul><li>Apple</li><li>Orange</li></ul>`,
);

// Remove the first <li>
const items = htmlparser2.DomUtils.getElementsByTagName("li", dom);
htmlparser2.DomUtils.removeElement(items[0]);

// Serialize back to HTML
const html = htmlparser2.DomUtils.getOuterHTML(dom);
// "<ul><li>Orange</li></ul>"
```

Other manipulation helpers include `appendChild`, `prependChild`, `append`, `prepend`, and `replaceElement` -- see the [`domutils` docs](https://github.com/fb55/domutils) for the full API.

## Parsing feeds

`htmlparser2` makes it easy to parse RSS, RDF and Atom feeds, by providing a `parseFeed` method:

```javascript
const feed = htmlparser2.parseFeed(content);
```

This returns an object with `type`, `title`, `link`, `description`, `updated`, `author`, and `items` (an array of feed entries), or `null` if the document isn't a recognized feed format.

The `xmlMode` option is enabled by default for `parseFeed`. If you pass custom options, make sure to include `xmlMode: true`.

## Performance

After having some artificial benchmarks for some time, **@AndreasMadsen** published his [`htmlparser-benchmark`](https://github.com/AndreasMadsen/htmlparser-benchmark), which benchmarks HTML parses based on real-world websites.

At the time of writing, the latest versions of all supported parsers show the following performance characteristics on GitHub Actions (sourced from [here](https://github.com/AndreasMadsen/htmlparser-benchmark/blob/e78cd8fc6c2adac08deedd4f274c33537451186b/stats.txt)):

```
htmlparser2        : 2.17215 ms/file ± 3.81587
node-html-parser   : 2.35983 ms/file ± 1.54487
html5parser        : 2.43468 ms/file ± 2.81501
neutron-html5parser: 2.61356 ms/file ± 1.70324
htmlparser2-dom    : 3.09034 ms/file ± 4.77033
html-dom-parser    : 3.56804 ms/file ± 5.15621
libxmljs           : 4.07490 ms/file ± 2.99869
htmljs-parser      : 6.15812 ms/file ± 7.52497
parse5             : 9.70406 ms/file ± 6.74872
htmlparser         : 15.0596 ms/file ± 89.0826
html-parser        : 28.6282 ms/file ± 22.6652
saxes              : 45.7921 ms/file ± 128.691
html5              : 120.844 ms/file ± 153.944
```

## Security contact information

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

```

### File: biome.json
```json
{
    "$schema": "https://biomejs.dev/schemas/2.4.7/schema.json",
    "vcs": {
        "enabled": true,
        "clientKind": "git",
        "useIgnoreFile": true
    },
    "files": {
        "ignoreUnknown": true,
        "includes": ["**/*.{ts,md,json,yml}", "!**/.*"]
    },
    "formatter": {
        "enabled": true,
        "indentStyle": "space",
        "indentWidth": 4
    },
    "javascript": {
        "formatter": {}
    },
    "linter": {
        "enabled": true,
        "rules": {
            "recommended": true,
            "suspicious": {
                "noConstEnum": "off",
                "noConstantBinaryExpressions": "error",
                "useAwait": "error"
            },
            "complexity": {
                "noUselessStringConcat": "error",
                "noUselessUndefined": "error",
                "useSimplifiedLogicExpression": "error",
                "useWhile": "error"
            },
            "performance": {
                "useTopLevelRegex": "error"
            },
            "style": {
                "noInferrableTypes": "error",
                "noNegationElse": "error",
                "noUnusedTemplateLiteral": "error",
                "noUselessElse": "error",
                "noYodaExpression": "error",
                "useAsConstAssertion": "error",
                "useCollapsedElseIf": "error",
                "useCollapsedIf": "error",
                "useConsistentArrayType": "error",
                "useConsistentArrowReturn": "error",
                "useConsistentMemberAccessibility": "error",
                "useConsistentObjectDefinitions": "error",
                "useConsistentTypeDefinitions": "error",
                "useDefaultParameterLast": "error",
                "useExplicitLengthCheck": "error",
                "useNumberNamespace": "error",
                "useNumericSeparators": "error",
                "useObjectSpread": "error",
                "useShorthandAssign": "error",
                "useUnifiedTypeSignatures": "error"
            }
        }
    },
    "assist": {
        "enabled": true,
        "actions": {
            "source": {
                "organizeImports": "on"
            }
        }
    },
    "overrides": [
        {
            "includes": ["**/*.{test,spec}.ts", "test/**/*.ts"],
            "javascript": {
                "globals": [
                    "jest",
                    "describe",
                    "it",
                    "beforeEach",
                    "afterEach",
                    "expect",
                    "vi"
                ]
            }
        },
        {
            "includes": ["**/*.ts", "**/*.cts", "**/*.mts", "**/*.tsx"],
            "linter": {
                "rules": {
                    "complexity": {
                        "useLiteralKeys": "off"
                    }
                }
            }
        }
    ]
}

```

### File: package-lock.json
```json
{
    "name": "htmlparser2",
    "version": "12.0.0",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "htmlparser2",
            "version": "12.0.0",
            "funding": [
                "https://github.com/fb55/htmlparser2?sponsor=1",
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/fb55"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "domelementtype": "^3.0.0",
                "domhandler": "^6.0.0",
                "domutils": "^4.0.2",
                "entities": "^8.0.0"
            },
            "devDependencies": {
                "@biomejs/biome": "^2.4.8",
                "@feedic/eslint-config": "^0.3.1",
                "@types/node": "^25.5.0",
                "eslint": "^10.0.3",
                "eslint-config-biome": "^2.1.3",
                "typescript": "^5.9.3",
                "typescript-eslint": "^8.57.1",
                "vitest": "^4.1.0"
            },
            "engines": {
                "node": ">=20.19.0"
            }
        },
        "node_modules/@altano/repository-tools": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/@altano/repository-tools/-/repository-tools-2.0.1.tgz",
            "integrity": "sha512-YE/52CkFtb+YtHPgbWPai7oo5N9AKnMuP5LM+i2AG7G1H2jdYBCO1iDnkDE3dZ3C1MIgckaF+d5PNRulgt0bdw==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/@babel/helper-validator-identifier": {
            "version": "7.28.5",
            "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
            "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@biomejs/biome": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/biome/-/biome-2.4.8.tgz",
            "integrity": "sha512-ponn0oKOky1oRXBV+rlSaUlixUxf1aZvWC19Z41zBfUOUesthrQqL3OtiAlSB1EjFjyWpn98Q64DHelhA6jNlA==",
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "bin": {
                "biome": "bin/biome"
            },
            "engines": {
                "node": ">=14.21.3"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/biome"
            },
            "optionalDependencies": {
                "@biomejs/cli-darwin-arm64": "2.4.8",
                "@biomejs/cli-darwin-x64": "2.4.8",
                "@biomejs/cli-linux-arm64": "2.4.8",
                "@biomejs/cli-linux-arm64-musl": "2.4.8",
                "@biomejs/cli-linux-x64": "2.4.8",
                "@biomejs/cli-linux-x64-musl": "2.4.8",
                "@biomejs/cli-win32-arm64": "2.4.8",
                "@biomejs/cli-win32-x64": "2.4.8"
            }
        },
        "node_modules/@biomejs/cli-darwin-arm64": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-darwin-arm64/-/cli-darwin-arm64-2.4.8.tgz",
            "integrity": "sha512-ARx0tECE8I7S2C2yjnWYLNbBdDoPdq3oyNLhMglmuctThwUsuzFWRKrHmIGwIRWKz0Mat9DuzLEDp52hGnrxGQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-darwin-x64": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-darwin-x64/-/cli-darwin-x64-2.4.8.tgz",
            "integrity": "sha512-Jg9/PsB9vDCJlANE8uhG7qDhb5w0Ix69D7XIIc8IfZPUoiPrbLm33k2Ig3NOJ/7nb3UbesFz3D1aDKm9DvzjhQ==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-linux-arm64": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-arm64/-/cli-linux-arm64-2.4.8.tgz",
            "integrity": "sha512-5CdrsJct76XG2hpKFwXnEtlT1p+4g4yV+XvvwBpzKsTNLO9c6iLlAxwcae2BJ7ekPGWjNGw9j09T5KGPKKxQig==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-linux-arm64-musl": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-arm64-musl/-/cli-linux-arm64-musl-2.4.8.tgz",
            "integrity": "sha512-Zo9OhBQDJ3IBGPlqHiTISloo5H0+FBIpemqIJdW/0edJ+gEcLR+MZeZozcUyz3o1nXkVA7++DdRKQT0599j9jA==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-linux-x64": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-x64/-/cli-linux-x64-2.4.8.tgz",
            "integrity": "sha512-PdKXspVEaMCQLjtZCn6vfSck/li4KX9KGwSDbZdgIqlrizJ2MnMcE3TvHa2tVfXNmbjMikzcfJpuPWH695yJrw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-linux-x64-musl": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-x64-musl/-/cli-linux-x64-musl-2.4.8.tgz",
            "integrity": "sha512-Gi8quv8MEuDdKaPFtS2XjEnMqODPsRg6POT6KhoP+VrkNb+T2ywunVB+TvOU0LX1jAZzfBr+3V1mIbBhzAMKvw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-win32-arm64": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-win32-arm64/-/cli-win32-arm64-2.4.8.tgz",
            "integrity": "sha512-LoFatS0tnHv6KkCVpIy3qZCih+MxUMvdYiPWLHRri7mhi2vyOOs8OrbZBcLTUEWCS+ktO72nZMy4F96oMhkOHQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@biomejs/cli-win32-x64": {
            "version": "2.4.8",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-win32-x64/-/cli-win32-x64-2.4.8.tgz",
            "integrity": "sha512-vAn7iXDoUbqFXqVocuq1sMYAd33p8+mmurqJkWl6CtIhobd/O6moe4rY5AJvzbunn/qZCdiDVcveqtkFh1e7Hg==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT OR Apache-2.0",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">=14.21.3"
            }
        },
        "node_modules/@emnapi/core": {
            "version": "1.9.0",
            "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.9.0.tgz",
            "integrity": "sha512-0DQ98G9ZQZOxfUcQn1waV2yS8aWdZ6kJMbYCJB3oUBecjWYO1fqJ+a1DRfPF3O5JEkwqwP1A9QEN/9mYm2Yd0w==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "@emnapi/wasi-threads": "1.2.0",
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@emnapi/runtime": {
            "version": "1.9.0",
            "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.9.0.tgz",
            "integrity": "sha512-QN75eB0IH2ywSpRpNddCRfQIhmJYBCJ1x5Lb3IscKAL8bMnVAKnRg8dCoXbHzVLLH7P38N2Z3mtulB7W0J0FKw==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@emnapi/wasi-threads": {
            "version": "1.2.0",
            "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.2.0.tgz",
            "integrity": "sha512-N10dEJNSsUx41Z6pZsXU8FjPjpBEplgH24sfkmITrBED1/U2Esum9F3lfLrMjKHHjmi557zQn7kR9R+XWXu5Rg==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@es-joy/jsdoccomment": {
            "version": "0.84.0",
            "resolved": "https://registry.npmjs.org/@es-joy/jsdoccomment/-/jsdoccomment-0.84.0.tgz",
            "integrity": "sha512-0xew1CxOam0gV5OMjh2KjFQZsKL2bByX1+q4j3E73MpYIdyUxcZb/xQct9ccUb+ve5KGUYbCUxyPnYB7RbuP+w==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@types/estree": "^1.0.8",
                "@typescript-eslint/types": "^8.54.0",
                "comment-parser": "1.4.5",
                "esquery": "^1.7.0",
                "jsdoc-type-pratt-parser": "~7.1.1"
            },
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@es-joy/resolve.exports": {
            "version": "1.2.0",
            "resolved": "https://registry.npmjs.org/@es-joy/resolve.exports/-/resolve.exports-1.2.0.tgz",
            "integrity": "sha512-Q9hjxWI5xBM+qW2enxfe8wDKdFWMfd0Z29k5ZJnuBqD/CasY5Zryj09aCA6owbGATWz+39p5uIdaHXpopOcG8g==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=10"
            }
        },
        "node_modules/@eslint-community/eslint-utils": {
            "version": "4.9.1",
            "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.9.1.tgz",
            "integrity": "sha512-phrYmNiYppR7znFEdqgfWHXR6NCkZEK7hwWDHZUjit/2/U0r6XvkDl0SYnoM51Hq7FhCGdLDT6zxCCOY1hexsQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "eslint-visitor-keys": "^3.4.3"
            },
            "engines": {
                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
            },
            "funding": {
                "url": "https://opencollective.com/eslint"
            },
            "peerDependencies": {
                "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
            }
        },
        "node_modules/@eslint-community/eslint-utils/node_modules/eslint-visitor-keys": {
            "version": "3.4.3",
            "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz",
            "integrity": "sha512-wpc+LXeiyiisxPlEkUzU6svyS1frIO3Mgxj1fdy7Pm8Ygzguax2N3Fa/D/ag1WqbOprdI+uY6wMUl8/a2G+iag==",
            "dev": true,
            "license": "Apache-2.0",
            "engines": {
                "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
            },
            "funding": {
                "url": "https://opencollective.com/eslint"
            }
        },
        "node_modules/@eslint-community/regexpp": {
            "version": "4.12.2",
            "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
            "integrity": "sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
            }
        },
        "node_modules/@eslint/config-array": {
            "version": "0.23.3",
            "resolved": "https://registry.npmjs.org/@eslint/config-array/-/config-array-0.23.3.tgz",
            "integrity": "sha512-j+eEWmB6YYLwcNOdlwQ6L2OsptI/LO6lNBuLIqe5R7RetD658HLoF+Mn7LzYmAWWNNzdC6cqP+L6r8ujeYXWLw==",
            "dev": true,
            "license": "Apache-2.0",
            "dependencies": {
                "@eslint/object-schema": "^3.0.3",
                "debug": "^4.3.1",
                "minimatch": "^10.2.4"
            },
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@eslint/config-helpers": {
            "version": "0.5.3",
            "resolved": "https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.5.3.tgz",
            "integrity": "sha512-lzGN0onllOZCGroKJmRwY6QcEHxbjBw1gwB8SgRSqK8YbbtEXMvKynsXc3553ckIEBxsbMBU7oOZXKIPGZNeZw==",
            "dev": true,
            "license": "Apache-2.0",
            "dependencies": {
                "@eslint/core": "^1.1.1"
            },
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@eslint/core": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/@eslint/core/-/core-1.1.1.tgz",
            "integrity": "sha512-QUPblTtE51/7/Zhfv8BDwO0qkkzQL7P/aWWbqcf4xWLEYn1oKjdO0gglQBB4GAsu7u6wjijbCmzsUTy6mnk6oQ==",
            "dev": true,
            "license": "Apache-2.0",
            "dependencies": {
                "@types/json-schema": "^7.0.15"
            },
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@eslint/js": {
            "version": "10.0.1",
            "resolved": "https://registry.npmjs.org/@eslint/js/-/js-10.0.1.tgz",
            "integrity": "sha512-zeR9k5pd4gxjZ0abRoIaxdc7I3nDktoXZk2qOv9gCNWx3mVwEn32VRhyLaRsDiJjTs0xq/T8mfPtyuXu7GWBcA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            },
            "funding": {
                "url": "https://eslint.org/donate"
            },
            "peerDependencies": {
                "eslint": "^10.0.0"
            },
            "peerDependenciesMeta": {
     
... [TRUNCATED]
```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

Only the current version is supported. Please make sure to update to the latest release.

## Reporting a Vulnerability

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.

```

### File: tsconfig.eslint.json
```json
{
    "extends": "./tsconfig.json",
    "compilerOptions": {
        "rootDir": ".",
        "noEmit": true
    },
    "include": ["src"],
    "exclude": []
}

```

### File: tsconfig.json
```json
{
    "compilerOptions": {
        /* Basic Options */
        "target": "es2022",
        "module": "nodenext",
        "moduleResolution": "nodenext",
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,
        "outDir": "dist",

        /* Strict Type-Checking Options */
        "strict": true,

        /* Additional Checks */
        "exactOptionalPropertyTypes": true,
        "forceConsistentCasingInFileNames": true,
        "isolatedModules": true,
        "isolatedDeclarations": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitOverride": true,
        "noImplicitReturns": true,
        "noPropertyAccessFromIndexSignature": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,

        /* Module Resolution Options */
        "resolveJsonModule": true
    },
    "include": ["src"],
    "exclude": [
        "**/*.spec.ts",
        "**/__fixtures__/*",
        "**/__tests__/*",
        "**/__snapshots__/*"
    ]
}

```

### File: src\FeedHandler.spec.ts
```ts
import fs from "node:fs/promises";
import { describe, expect, it } from "vitest";
import { parseFeed } from "./index.js";

const documents = new URL("__fixtures__/Documents/", import.meta.url);

describe("parseFeed", () => {
    it("(rssFeed)", async () =>
        expect(
            parseFeed(
                await fs.readFile(
                    new URL("RSS_Example.xml", documents),
                    "utf8",
                ),
            ),
        ).toMatchSnapshot());

    it("(atomFeed)", async () =>
        expect(
            parseFeed(
                await fs.readFile(
                    new URL("Atom_Example.xml", documents),
                    "utf8",
                ),
            ),
        ).toMatchSnapshot());

    it("(rdfFeed)", async () =>
        expect(
            parseFeed(
                await fs.readFile(
                    new URL("RDF_Example.xml", documents),
                    "utf8",
                ),
            ),
        ).toMatchSnapshot());
});

```

### File: src\index.spec.ts
```ts
import { Element } from "domhandler";
import { describe, expect, it } from "vitest";
import {
    createDocumentStream,
    DefaultHandler,
    DomHandler,
    type Parser,
    parseDocument,
} from "./index.js";

// Add an `attributes` prop to the Element for now, to make it possible for Jest to render DOM nodes.
Object.defineProperty(Element.prototype, "attributes", {
    get() {
        return Object.keys(this.attribs).map((name) => ({
            name,
            value: this.attribs[name],
        }));
    },
    configurable: true,
    enumerable: false,
});

describe("Index", () => {
    it("parseDocument", () => {
        const dom = parseDocument("<a foo><b><c><?foo>Yay!");
        expect(dom).toMatchSnapshot();
    });

    it("parseDocument in foreign content", () => {
        const dom = parseDocument("<svg><![CDATA[a<b]]></svg>");
        expect(dom).toMatchSnapshot();
    });

    it("createDocumentStream", () => {
        let documentStream!: Parser;

        const documentPromise = new Promise((resolve, reject) => {
            documentStream = createDocumentStream((error, dom) =>
                error ? reject(error) : resolve(dom),
            );
        });

        for (const c of "&amp;This is text<!-- and comments --><tags>") {
            documentStream.write(c);
        }

        documentStream.end();

        return expect(documentPromise).resolves.toMatchSnapshot();
    });

    describe("API", () => {
        it("should export the appropriate APIs", () => {
            expect(DomHandler).toEqual(DefaultHandler);
        });
    });
});

```

### File: src\index.ts
```ts
import { Parser, type ParserOptions } from "./Parser.js";

export type { Handler, ParserOptions } from "./Parser.js";
export { Parser } from "./Parser.js";

import {
    type Document,
    DomHandler,
    type DomHandlerOptions,
    type Element,
} from "domhandler";

export {
    DomHandler,
    // Old name for DomHandler
    DomHandler as DefaultHandler,
    type DomHandlerOptions,
} from "domhandler";

/**
 * Combined parser and handler options.
 */
export type Options = ParserOptions & DomHandlerOptions;

// Helper methods

/**
 * Parses the data, returns the resulting document.
 * @param data The data that should be parsed.
 * @param options Optional options for the parser and DOM handler.
 */
export function parseDocument(data: string, options?: Options): Document {
    const handler = new DomHandler(undefined, options);
    new Parser(handler, options).end(data);
    return handler.root;
}

/**
 * Creates a parser instance, with an attached DOM handler.
 * @param callback A callback that will be called once parsing has been completed, with the resulting document.
 * @param options Optional options for the parser and DOM handler.
 * @param elementCallback An optional callback that will be called every time a tag has been completed inside of the DOM.
 */
export function createDocumentStream(
    callback: (error: Error | null, document: Document) => void,
    options?: Options,
    elementCallback?: (element: Element) => void,
): Parser {
    const handler: DomHandler = new DomHandler(
        (error: Error | null) => callback(error, handler.root),
        options,
        elementCallback,
    );
    return new Parser(handler, options);
}

/*
 * All of the following exports exist for backwards-compatibility.
 * They should probably be removed eventually.
 */
export * as ElementType from "domelementtype";
export {
    type Callbacks as TokenizerCallbacks,
    default as Tokenizer,
    QuoteType,
} from "./Tokenizer.js";

import { type Feed, getFeed } from "domutils";

export { type Feed, getFeed } from "domutils";

const parseFeedDefaultOptions = { xmlMode: true };

/**
 * Parse a feed.
 * @param feed The feed that should be parsed, as a string.
 * @param options Optionally, options for parsing. When using this, you should set `xmlMode` to `true`.
 */
export function parseFeed(
    feed: string,
    options: Options = parseFeedDefaultOptions,
): Feed | null {
    return getFeed(parseDocument(feed, options).children);
}

export * as DomUtils from "domutils";

```

### File: src\Parser.events.spec.ts
```ts
import { describe, expect, it, vi } from "vitest";
import * as helper from "./__fixtures__/testHelper.js";
import { Parser, type ParserOptions } from "./Parser.js";

/**
 * Write to the parser twice, once a bytes, once as a single blob. Then check
 * that we received the expected events.
 * @internal
 * @param input Data to write.
 * @param options Parser options.
 * @returns Promise that resolves if the test passes.
 */
function runTest(input: string, options?: ParserOptions) {
    let firstResult: unknown[] | undefined;

    return new Promise<void>((resolve, reject) => {
        const handler = helper.getEventCollector((error, actual) => {
            if (error) {
                return reject(error);
            }

            if (firstResult) {
                expect(actual).toEqual(firstResult);
                resolve();
            } else {
                firstResult = actual;
                expect(actual).toMatchSnapshot();
            }
        });

        const parser = new Parser(handler, options);
        // First, try to run the test via chunks
        for (let index = 0; index < input.length; index++) {
            parser.write(input.charAt(index));
        }
        parser.end();
        // Then, parse everything
        parser.parseComplete(input);
    });
}

describe("Events", () => {
    it("simple", () => runTest("<h1 class=test>adsf</h1>"));

    it("Template script tags", () =>
        runTest(
            '<p><script type="text/template"><h1>Heading1</h1></script></p>',
        ));

    it("Lowercase tags", () =>
        runTest("<H1 class=test>adsf</H1>", { lowerCaseTags: true }));

    it("CDATA", () =>
        runTest("<tag><![CDATA[ asdf ><asdf></adsf><> fo]]></tag><![CD>", {
            xmlMode: true,
        }));

    it("CDATA (inside special)", () =>
        runTest(
            "<script>/*<![CDATA[*/ asdf ><asdf></adsf><> fo/*]]>*/</script>",
        ));

    it("leading lt", () => runTest(">a>"));

    it("end slash: void element ending with />", () =>
        runTest("<hr / ><p>Hold the line."));

    it("end slash: void element ending with >", () =>
        runTest("<hr   ><p>Hold the line."));

    it("end slash: void element ending with >, xmlMode=true", () =>
        runTest("<hr   ><p>Hold the line.", { xmlMode: true }));

    it("end slash: non-void element ending with />", () =>
        runTest("<xx / ><p>Hold the line."));

    it("end slash: non-void element ending with />, xmlMode=true", () =>
        runTest("<xx / ><p>Hold the line.", { xmlMode: true }));

    it("end slash: non-void element ending with />, recognizeSelfClosing=true", () =>
        runTest("<xx / ><p>Hold the line.", { recognizeSelfClosing: true }));

    it("end slash: special tag ending with />, recognizeSelfClosing=true", () =>
        runTest("<script/><b>x</b>", { recognizeSelfClosing: true }));

    it("end slash: plaintext tag ending with />, recognizeSelfClosing=true", () =>
        runTest("<plaintext/><b>x</b>", { recognizeSelfClosing: true }));

    it("end slash: as part of attrib value of void element", () =>
        runTest("<img src=gif.com/123/><p>Hold the line."));

    it("end slash: as part of attrib value of non-void element", () =>
        runTest("<a href=http://test.com/>Foo</a><p>Hold the line."));

    it("Implicit close tags", () =>
        runTest(
            "<ol><li class=test><div><table style=width:100%><tr><th>TH<td colspan=2><h3>Heading</h3><tr><td><div>Div</div><td><div>Div2</div></table></div><li><div><h3>Heading 2</h3></div></li></ol><p>Para<h4>Heading 4</h4><p><ul><li>Hi<li>bye</ul>",
        ));

    it("attributes (no white space, no value, no quotes)", () =>
        runTest(
            '<button class="test0"title="test1" disabled value=test2>adsf</button>',
        ));

    it("crazy attribute", () => runTest("<p < = '' FAIL>stuff</p><a"));

    it("Scripts creating other scripts", () =>
        runTest("<p><script>var str = '<script></'+'script>';</script></p>"));

    it("Long comment ending", () =>
        runTest("<meta id='before'><!-- text ---><meta id='after'>"));

    it("Long CDATA ending", () =>
        runTest("<before /><tag><![CDATA[ text ]]]></tag><after />", {
            xmlMode: true,
        }));

    it("Implicit open p and br tags", () =>
        runTest("<div>Hallo</p>World</br></ignore></div></p></br>"));

    it("lt followed by whitespace", () => runTest("a < b"));

    it("double attribute", () => runTest("<h1 class=test class=boo></h1>"));

    it("numeric entities", () =>
        runTest("&#x61;&#x62&#99;&#100&#x66g&#x;&#x68"));

    it("legacy entities", () => runTest("&AMPel&iacutee&ampeer;s&lter&sum"));

    it("named entities", () =>
        runTest("&amp;el&lt;er&CounterClockwiseContourIntegral;foo&bar"));

    it("xml entities", () =>
        runTest("&amp;&gt;&amp&lt;&uuml;&#x61;&#x62&#99;&#100&#101", {
            xmlMode: true,
        }));

    it("entity in attribute", () =>
        runTest(
            "<a href='http://example.com/p&#x61;#x61ge?param=value&param2&param3=&lt;val&; & &'>",
        ));

    it("double brackets", () =>
        runTest("<<princess-purpose>>testing</princess-purpose>"));

    it("legacy entities fail", () => runTest("M&M"));

    it("Special special tags", () =>
        runTest(
            "<tItLe><b>foo</b><title></TiTlE><sitle><b></b></sitle><ttyle><b></b></ttyle><sCriPT></scripter</soo</sCript><STyLE></styler</STylE><sCiPt><stylee><scriptee><soo>",
        ));

    it("Empty tag name", () => runTest("< ></ >"));

    it("Not quite closed", () => runTest("<foo /bar></foo bar>"));

    it("Entities in attributes", () =>
        runTest("<foo bar=&amp; baz=\"&amp;\" boo='&amp;' noo=>"));

    it("CDATA in HTML", () => runTest("<![CDATA[ foo ]]>"));

    it("Comment edge-cases", () => runTest("<!-foo><!-- --- --><!--foo"));

    it("CDATA edge-cases", () =>
        runTest("<![CDATA><![CDATA[[]]sdaf]]><![CDATA[foo", {
            recognizeCDATA: true,
        }));

    it("Comment false ending", () => runTest("<!-- a-b-> -->"));

    it("Short bang comment", () => runTest("<!--!>"));

    it("Abruptly closed comment", () => runTest("<!--->text"));

    it("Empty EOF comment", () => runTest("<!--"));

    it("HTML bogus comments", () => runTest("<?foo><!foo>"));

    it("Short HTML bogus comments", () => runTest("<!><!->"));

    it("Bogus comment after </ and whitespace", () => runTest("<div></ div>"));

    it("Empty closing tag", () => runTest("</>"));

    it("Empty closing tag, xmlMode=true", () =>
        runTest("</>", { xmlMode: true }));

    it("Doctype without whitespace", () => runTest("<!DOCTYPEhtml>"));

    it("Foreign CDATA in SVG", () => runTest("<svg><![CDATA[a<b]]></svg>"));

    it("Foreign CDATA in MathML", () =>
        runTest("<math><![CDATA[a<b]]></math>"));

    it("SVG title is not HTML special", () =>
        runTest("<svg><title>&amp;<b>x</b></title></svg>"));

    it("SVG tag case adjustment", () =>
        runTest("<svg><foreignObject><b>x</b></foreignObject></svg>"));

    it("SVG integration point closing with unclosed child", () =>
        runTest("<svg><foreignObject><div>x</foreignObject></svg>after"));

    it("Content after SVG integration point", () =>
        runTest("<svg><foreignObject><b>x</b></foreignObject><rect/></svg>"));

    it("Stray </svg> does not break foreign context", () =>
        runTest("</svg><script><b>not a tag</b></script>"));

    it("Implicit close of nested foreign elements", () =>
        runTest("<svg><math><mi>text</svg><script><b>x</b></script>"));

    it("Self-closing foreign element with recognizeSelfClosing", () =>
        runTest("<svg/><script><b>x</b></script>", {
            recognizeSelfClosing: true,
        }));

    it("HTML image alias", () => runTest("<image></image>"));

    it("SVG image is not aliased", () => runTest("<svg><image></image></svg>"));

    it("EOF bogus comments", () => runTest("<!-"));

    it("EOF empty bogus comment", () => runTest("<!"));

    it("EOF partial doctype", () => runTest("<!DOC"));

    it("EOF complete doctype", () => runTest("<!DOCTYPE"));

    it("EOF incomplete doctype", () => runTest("<!DOCTYPE h"));

    it("EOF processing instruction", () => runTest("<?"));

    it("Partial CDATA match with >", () => runTest("<![CD>"));

    it("Unclosed CDATA at EOF", () => runTest("<![CDATA[foo"));

    it("Empty unclosed CDATA at EOF", () => runTest("<![CDATA["));

    it("Partial CDATA at EOF", () => runTest("<![C"));

    it("Scripts ending with <", () => runTest("<script><</script>"));

    it("Special end tags ending with /> in script", () =>
        runTest("<script>safe</script/><img>"));

    it("Special end tags ending with /> in style", () =>
        runTest("<style>safe</style/><img>"));

    it("Special end tags ending with /> in title", () =>
        runTest("<title>safe</title/><img>"));

    it("Special end tags ending with /> in textarea", () =>
        runTest("<textarea>safe</textarea/><img>"));

    it("CDATA more edge-cases", () =>
        runTest("<![CDATA[foo]bar]>baz]]>", { recognizeCDATA: true }));

    it("tag names are not ASCII alpha", () => runTest("<12>text</12>"));

    it("open-implies-close case of (non-br) void close tag in non-XML mode", () =>
        runTest("<select><input></select>", { lowerCaseAttributeNames: true }));

    it("entity in attribute (#276)", () =>
        runTest(
            '<img src="?&image_uri=1&&image;=2&image=3"/>?&image_uri=1&&image;=2&image=3',
        ));

    it("entity in title (#592)", () => runTest("<title>the &quot;title&quot"));

    it("entity in textarea", () => runTest("<textarea>&amp;</textarea>"));

    it("entity in title - decodeEntities=false (#592)", () =>
        runTest("<title>the &quot;title&quot;", { decodeEntities: false }));

    it("plaintext", () => runTest("<plaintext><b>hi</b>"));

    it("</title> in <script> (#745)", () =>
        runTest("<script>'</title>'</script>"));

    it("XML tags", () => runTest("<:foo><_bar>", { xmlMode: true }));

    it("Trailing legacy entity", () => runTest("&timesbar;&timesbar"));

    it("Trailing numeric entity", () => runTest("&#53&#53"));

    it("Multi-byte entity", () => runTest("&NotGreaterFullEqual;"));

    it("Start & end indices from domhandler", () =>
        runTest(
            "<!DOCTYPE html> <html> <title>The Title</title> <body class='foo'>Hello world <p></p></body> <!-- the comment --> </html> ",
        ));

    it("Self-closing indices (#941)", () =>
        runTest("<xml><a/><b/></xml>", { xmlMode: true }));

    it("Entity after <", () => runTest("<&amp;"));

    it("Attribute in XML (see #1350)", () =>
        runTest(
            '<Page\n    title="Hello world"\n    actionBarVisible="false"/>',
            { xmlMode: true },
        ));
});

describe("Helper", () => {
    it("should handle errors", () => {
        const eventCallback = vi.fn();
        const parser = new Parser(helper.getEventCollector(eventCallback));

        parser.end();
        parser.write("foo");

        expect(eventCallback).toHaveBeenCalledTimes(2);
        expect(eventCallback).toHaveBeenNthCalledWith(1, null, []);
        expect(eventCallback).toHaveBeenLastCalledWith(
            new Error(".write() after done!"),
        );
    });
});

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
