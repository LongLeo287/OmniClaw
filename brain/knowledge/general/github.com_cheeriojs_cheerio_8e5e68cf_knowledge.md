---
id: github.com-cheeriojs-cheerio-8e5e68cf-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:38.735986
---

# KNOWLEDGE EXTRACT: github.com_cheeriojs_cheerio_8e5e68cf
> **Extracted on:** 2026-04-01 15:31:05
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524559/github.com_cheeriojs_cheerio_8e5e68cf

---

## File: `.gitattributes`
```
# Enforce Unix newlines
* text=auto eol=lf

benchmark/documents/* binary
benchmark/jquery*.js binary
```

## File: `.gitignore`
```
node_modules
npm-debug.log
.DS_Store
.docusaurus
.cache-loader
/coverage
/.tshy
/.tshy-build
/dist

# Website build artifacts
website/.astro/
website/dist/
website/src/content/brain/knowledge/docs_legacy/api
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Cheerio

Thanks for your interest in contributing to the project! Here's a rundown of how
we'd like to work with you:

1.  File an issue on GitHub describing the contribution you'd like to make. This
    will help us to get you started on the right foot.
2.  Fork the project, and make your changes in a new branch based off of the
    `main` branch:
    1.  Follow the project's code style (see below)
    2.  Add enough unit tests to "prove" that your patch is correct
    3.  Update the project documentation as needed (see below)
    4.  Describe your approach with as much detail as necessary in the git
        commit message
3.  Open a pull request, and reference the initial issue in the pull request
    message.

# Documentation

Any API change should be reflected in the project's README.md file. Reuse
[jQuery's documentation](https://api.jquery.com) wherever possible, but take
care to note aspects that make Cheerio distinct.

# Code Style

Please make sure commit hooks are run, which will enforce the code style.

When implementing private functionality that isn't part of the jQuery API,
please opt for:

- _Static methods_: If the functionality does not require a reference to a
  Cheerio instance, simply define a named function within the module it is
  needed.
- _Instance methods_: If the functionality requires a reference to a Cheerio
  instance, informally define the method as "private" using the following
  conventions:
  - Define the method as a function on the Cheerio prototype
  - Prefix the method name with an underscore (`_`) character
  - Include `@api private` in the code comment the documents the method
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2022 The Cheerio contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `Readme.md`
```markdown
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

```js
$('.apple', '#fruits').text();
//=> Apple

$('ul .pear').attr('class');
//=> pear

$('li[class=orange]').html();
//=> Orange
```

### Rendering

When you're ready to render the document, you can call the `html` method on the
"root" selection:

```js
$.root().html();
//=>  <html>
//      <head></head>
//      <body>
//        <ul id="fruits">
//          <li class="apple">Apple</li>
//          <li class="orange">Orange</li>
//          <li class="pear">Pear</li>
//        </ul>
//      </body>
//    </html>
```

If you want to render the
[`outerHTML`](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/API/Element/outerHTML)
of a selection, you can use the `outerHTML` prop:

```js
$('.pear').prop('outerHTML');
//=> <li class="pear">Pear</li>
```

You may also render the text content of a Cheerio object using the `text`
method:

```js
const $ = cheerio.load('This is <em>content</em>.');
$('body').text();
//=> This is content.
```

### The "DOM Node" object

Cheerio collections are made up of objects that bear some resemblance to
[browser-based DOM nodes](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/API/Node).
You can expect them to define the following properties:

- `tagName`
- `parentNode`
- `previousSibling`
- `nextSibling`
- `nodeValue`
- `firstChild`
- `childNodes`
- `lastChild`

## Screencasts

[https://vimeo.com/31950192](https://vimeo.com/31950192)

> This video tutorial is a follow-up to Nettut's "How to Scrape Web Pages with
> Node.js and jQuery", using cheerio instead of JSDOM + jQuery. This video shows
> how easy it is to use cheerio and how much faster cheerio is than JSDOM +
> jQuery.

## Cheerio in the real world

Are you using cheerio in production? Add it to the
[wiki](https://github.com/cheeriojs/cheerio/wiki/Cheerio-in-Production)!

## Sponsors

Does your company use Cheerio in production? Please consider
[sponsoring this project](https://github.com/cheeriojs/cheerio?sponsor=1)! Your
help will allow maintainers to dedicate more time and resources to its
development and support.

**Headlining Sponsors**

<!-- BEGIN SPONSORS: headliner -->

<a href="https://github.com/" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%3A%2F%2Fgithub.com%2Fgithub.png?ixlib=js-3.8.0&w=128&h=128&fit=fillmax&fill=solid&s=a1e87ca289de84eb32ea85432cf8ad11" title="Github" alt="Github"></img>
          </a>
<a href="https://www.airbnb.com/" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%3A%2F%2Fgithub.com%2Fairbnb.png?ixlib=js-3.8.0&w=128&h=128&fit=fillmax&fill=solid&s=384cad45e10faea516202ad10801f895" title="AirBnB" alt="AirBnB"></img>
          </a>
<a href="https://hasdata.com" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%3A%2F%2Fhasdata.com%2Ffavicon.svg?ixlib=js-3.8.0&w=128&h=128&fit=fillmax&fill=solid&s=21933842d61dec74a961fc57754e58cb" title="HasData" alt="HasData"></img>
          </a>
<a href="https://context.dev/" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%3A%2F%2Fgithub.com%2Fcontext-dot-dev.png?ixlib=js-3.8.0&w=128&h=128&fit=fillmax&fill=solid&s=938601d3e2c0435ccb6ca004c19111d4" title="context.dev" alt="context.dev"></img>
          </a>

<!-- END SPONSORS -->

**Other Sponsors**

<!-- BEGIN SPONSORS: sponsor -->

<a href="https://onlinecasinosspelen.com" target="_blank" rel="noopener noreferrer">
            <img height="64px" width="64px" src="https://humble.imgix.net/https%3A%2F%2Fimages.opencollective.com%2Fonlinecasinosspelen%2F99ac6a2%2Flogo.png?ixlib=js-3.8.0&w=64&h=64&fit=fillmax&fill=solid&s=8ec1ec058845b823858f22205485be02" title="OnlineCasinosSpelen" alt="OnlineCasinosSpelen"></img>
          </a>
<a href="https://Nieuwe-Casinos.net" target="_blank" rel="noopener noreferrer">
            <img height="64px" width="64px" src="https://humble.imgix.net/https%3A%2F%2Fimages.opencollective.com%2Fnieuwecasinos%2Fc67d423%2Flogo.png?ixlib=js-3.8.0&w=64&h=64&fit=fillmax&fill=solid&s=ed55d86b80b1aa8cf89b033020521945" title="Nieuwe-Casinos.net" alt="Nieuwe-Casinos.net"></img>
          </a>

<!-- END SPONSORS -->

## Backers

[Become a backer](https://github.com/cheeriojs/cheerio?sponsor=1) to show your
support for Cheerio and help us maintain and improve this open source project.

<!-- BEGIN SPONSORS: backer -->

<a href="https://kafidoff.com" target="_blank" rel="noopener noreferrer">
            <img height="64px" width="64px" src="https://humble.imgix.net/https%3A%2F%2Fimages.opencollective.com%2Fkafidoff-vasy%2Fd7ff85c%2Favatar.png?ixlib=js-3.8.0&w=64&h=64&fit=fillmax&fill=solid&s=a41c66c2f9b1d3a7a241e425e7aa2d09" title="Vasy Kafidoff" alt="Vasy Kafidoff"></img>
          </a>

<!-- END SPONSORS -->

## License

MIT
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

Only the latest release will receive security updates.

## Reporting a Vulnerability

To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security). Tidelift will
coordinate the fix and disclosure.
```

## File: `biome.json`
```json
{
  "$schema": "https://biomejs.dev/schemas/2.4.6/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "ignoreUnknown": true
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single"
    }
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "complexity": {
        "useLiteralKeys": "off",
        "noArguments": "off",
        "noCommaOperator": "off",
        "noUselessStringConcat": "error",
        "noUselessUndefined": "error",
        "useSimplifiedLogicExpression": "error",
        "useWhile": "error"
      },
      "style": {
        "noNonNullAssertion": "off",
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
        "useFilenamingConvention": "error",
        "useNumberNamespace": "error",
        "useNumericSeparators": "error",
        "useObjectSpread": "error",
        "useShorthandAssign": "error",
        "useUnifiedTypeSignatures": "error"
      },
      "suspicious": {
        "noAssignInExpressions": "off",
        "noConfusingVoidType": "off",
        "noConstEnum": "off",
        "noExplicitAny": "off",
        "noImplicitAnyLet": "off",
        "noShadowRestrictedNames": "off",
        "noUnsafeDeclarationMerging": "off",
        "noConstantBinaryExpressions": "error",
        "useAwait": "error"
      },
      "performance": {
        "useTopLevelRegex": "error"
      }
    }
  },
  "css": {
    "parser": {
      "tailwindDirectives": true
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
      "includes": ["**/*.astro"],
      "linter": {
        "rules": {
          "correctness": {
            "noUnusedImports": "off",
            "noUnusedVariables": "off"
          },
          "style": {
            "useFilenamingConvention": "off"
          },
          "performance": {
            "useTopLevelRegex": "off"
          }
        }
      }
    }
  ]
}
```

## File: `eslint.config.js`
```javascript
import { fileURLToPath } from 'node:url'; // Added for .gitignore path
import { includeIgnoreFile } from '@eslint/compat'; // Added for .gitignore
import feedicFlatConfig from '@feedic/eslint-config';
import { commonTypeScriptRules } from '@feedic/eslint-config/typescript';
import eslintPluginVitest from '@vitest/eslint-plugin';
import { defineConfig } from 'eslint/config';
import eslintConfigBiome from 'eslint-config-biome';
import globals from 'globals';
import tseslint from 'typescript-eslint';

const gitignorePath = fileURLToPath(new URL('.gitignore', import.meta.url));

export default defineConfig(
  includeIgnoreFile(gitignorePath), // Handle .gitignore patterns

  // Global linter options
  {
    linterOptions: {
      reportUnusedDisableDirectives: 'error',
    },
  },

  // Base configurations for all relevant files
  ...feedicFlatConfig,

  {
    rules: {
      'jsdoc/tag-lines': [2, 'any', { startLines: 1 }],
      'jsdoc/require-param-type': 0,
      'jsdoc/require-returns-type': 0,
      'jsdoc/no-types': 2,
      'jsdoc/require-returns-check': 0,
      'jsdoc/check-tag-names': [
        2,
        {
          definedTags: ['private'],
        },
      ],
    },
  },

  // Global custom rules and language options
  {
    languageOptions: {
      globals: globals.node,
      parserOptions: {
        projectService: {
          allowDefaultProject: ['*.js'],
          defaultProject: 'tsconfig.json',
        },
        tsconfigRootDir: import.meta.dirname, // eslint-disable-line n/no-unsupported-features/node-builtins
      },
    },
    rules: {
      'n/file-extension-in-import': [2, 'always'],
      'no-lonely-if': 2,
      'no-proto': 2,
      'no-else-return': [2, { allowElseIf: false }],
      'no-unused-expressions': 2,
      'no-useless-call': 2,
      'no-constant-binary-expression': 2,
      'no-void': 2,
      'unicorn/no-array-callback-reference': 0,
      'unicorn/no-array-reduce': 0,
      'unicorn/no-for-loop': 0,
      'unicorn/no-useless-undefined': 0,
      'unicorn/prefer-array-find': 0,
      'unicorn/prevent-abbreviations': 0,
    },
  },

  // TypeScript specific configurations
  {
    // Custom overrides and settings for TypeScript files
    files: ['**/*.{c,m,}ts', '**/*.tsx'], // Ensure this block specifically targets TS files
    extends: [
      ...tseslint.configs.recommendedTypeChecked,
      ...tseslint.configs.stylisticTypeChecked,
    ],
    languageOptions: {
      parser: tseslint.parser,
    },
    rules: {
      ...commonTypeScriptRules,
      // Enabling this in cheerio currently triggers broad churn across src + website.
      '@typescript-eslint/no-unnecessary-condition': 0,
    },
  },

  // Vitest specific configuration (for *.spec.ts files)
  {
    files: ['**/*.spec.ts'],
    plugins: { vitest: eslintPluginVitest },
    languageOptions: {
      globals: globals.vitest, // Add Vitest globals
    },
    rules: {
      // Assuming "recommended" is the flat config equivalent for "legacy-recommended"
      ...eslintPluginVitest.configs.recommended.rules,
      'n/no-unpublished-import': 0, // Allow importing devDependencies
    },
  },

  // Website specific configuration
  {
    files: ['website/**/*.{m,}ts{x,}'],
    languageOptions: {
      parserOptions: {
        projectService: {
          allowDefaultProject: ['*.mjs'],
        },
        tsconfigRootDir: `${import.meta.dirname}/website`, // eslint-disable-line n/no-unsupported-features/node-builtins
      },
    },
  },

  // Prettier - must be the last configuration to override styling rules
  eslintConfigBiome,
);
```

## File: `package.json`
```json
{
  "name": "cheerio",
  "version": "1.2.0",
  "description": "The fast, flexible & elegant library for parsing and manipulating HTML and XML.",
  "keywords": [
    "htmlparser",
    "jquery",
    "selector",
    "scraper",
    "parser",
    "dom",
    "xml",
    "html"
  ],
  "homepage": "https://cheerio.js.org/",
  "bugs": {
    "url": "https://github.com/cheeriojs/cheerio/issues"
  },
  "repository": {
    "type": "git",
    "url": "git://github.com/cheeriojs/cheerio.git"
  },
  "funding": "https://github.com/cheeriojs/cheerio?sponsor=1",
  "license": "MIT",
  "author": "Matt Mueller <mattmuelle@gmail.com>",
  "sideEffects": false,
  "maintainers": [
    "Felix Boehm <me@feedic.com>"
  ],
  "type": "module",
  "exports": {
    ".": {
      "browser": {
        "types": "./dist/browser/index.d.ts",
        "default": "./dist/browser/index.js"
      },
      "import": {
        "types": "./dist/esm/index.d.ts",
        "default": "./dist/esm/index.js"
      },
      "require": {
        "types": "./dist/commonjs/index.d.ts",
        "default": "./dist/commonjs/index.js"
      }
    },
    "./package.json": "./package.json",
    "./slim": {
      "browser": {
        "types": "./dist/browser/slim.d.ts",
        "default": "./dist/browser/slim.js"
      },
      "import": {
        "types": "./dist/esm/slim.d.ts",
        "default": "./dist/esm/slim.js"
      },
      "require": {
        "types": "./dist/commonjs/slim.d.ts",
        "default": "./dist/commonjs/slim.js"
      }
    },
    "./utils": {
      "browser": {
        "types": "./dist/browser/utils.d.ts",
        "default": "./dist/browser/utils.js"
      },
      "import": {
        "types": "./dist/esm/utils.d.ts",
        "default": "./dist/esm/utils.js"
      },
      "require": {
        "types": "./dist/commonjs/utils.d.ts",
        "default": "./dist/commonjs/utils.js"
      }
    }
  },
  "main": "./dist/commonjs/index.js",
  "module": "./dist/esm/index.js",
  "browser": "./dist/browser/index.js",
  "types": "./dist/commonjs/index.d.ts",
  "files": [
    "dist",
    "src",
    "!**/*.spec.{t,j}s",
    "!**/__tests__/*",
    "!**/__fixtures__/*"
  ],
  "scripts": {
    "benchmark": "node --import=tsx benchmark/benchmark.ts",
    "build": "tshy",
    "format": "npm run format:es && npm run format:biome",
    "format:biome": "biome check --write .",
    "format:es": "npm run lint:es -- --fix",
    "lint": "npm run lint:es && npm run lint:ts && npm run lint:biome",
    "lint:biome": "biome check .",
    "lint:es": "eslint .",
    "lint:ts": "tsc --noEmit",
    "prepare": "husky",
    "prepublishOnly": "npm run build",
    "test": "npm run lint && npm run test:vi",
    "test:vi": "vitest run",
    "update-sponsors": "tsx scripts/fetch-sponsors.mts"
  },
  "lint-staged": {
    "*.js": [
      "biome check --write",
      "eslint --fix"
    ],
    "*.{json,md,ts}": [
      "biome check --write"
    ]
  },
  "dependencies": {
    "cheerio-select": "^2.1.0",
    "dom-serializer": "^2.0.0",
    "domhandler": "^5.0.3",
    "domutils": "^3.2.2",
    "encoding-sniffer": "^0.2.1",
    "htmlparser2": "^10.1.0",
    "parse5": "^7.3.0",
    "parse5-htmlparser2-tree-adapter": "^7.1.0",
    "parse5-parser-stream": "^7.1.2",
    "undici": "^7.24.4",
    "whatwg-mimetype": "^4.0.0"
  },
  "devDependencies": {
    "@biomejs/biome": "^2.4.4",
    "@eslint/compat": "^2.0.3",
    "@feedic/eslint-config": "^0.3.1",
    "@imgix/js-core": "^3.8.0",
    "@octokit/graphql": "^9.0.3",
    "@types/jsdom": "^28.0.0",
    "@types/node": "^25.5.0",
    "@types/whatwg-mimetype": "^3.0.2",
    "@vitest/coverage-v8": "^4.1.0",
    "@vitest/eslint-plugin": "^1.6.12",
    "eslint": "^10.0.3",
    "eslint-config-biome": "^2.1.3",
    "globals": "^17.4.0",
    "husky": "^9.1.7",
    "jquery": "^4.0.0",
    "jsdom": "^29.0.0",
    "lint-staged": "^16.4.0",
    "prettier-plugin-jsdoc": "^1.8.0",
    "tinybench": "^6.0.0",
    "tshy": "^3.3.2",
    "tsx": "^4.21.0",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.57.1",
    "vitest": "^4.0.18"
  },
  "engines": {
    "node": ">=20.18.1"
  },
  "tshy": {
    "esmDialects": [
      "browser"
    ],
    "exports": {
      ".": "./src/index.ts",
      "./slim": "./src/slim.ts",
      "./utils": "./src/utils.ts",
      "./package.json": "./package.json"
    },
    "exclude": [
      "**/*.spec.ts",
      "**/__fixtures__/*",
      "**/__tests__/*"
    ]
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    /* Basic Options */
    "target": "es2019",
    "module": "node16",
    "moduleResolution": "node16",
    "lib": ["ES2022"],
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "lib",

    /* Strict Type-Checking Options */
    "strict": true,

    /* Additional Checks */
    "isolatedDeclarations": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,
    "noFallthroughCasesInSwitch": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noPropertyAccessFromIndexSignature": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  },
  "exclude": ["website/"] /* The website has its own tsconfig. */
}
```

## File: `tsconfig.typedoc.json`
```json
{
  "extends": "./tsconfig.json",
  "exclude": ["*.config.ts", "*.spec.ts", "scripts/*", "website/*"]
}
```

## File: `vitest.config.ts`
```typescript
import { defineConfig, type ViteUserConfig } from 'vitest/config';

const config: ViteUserConfig = defineConfig({
  test: {
    coverage: {
      exclude: [
        'benchmark/**',
        'scripts/**',
        'website/**',
        'dist/**',
        '*.config.ts',
      ],
    },
    typecheck: {
      enabled: true,
      include: ['src/api/extract.spec.ts'],
    },
  },
});

export default config;
```

## File: `benchmark/benchmark.ts`
```typescript
import fs from 'node:fs/promises';
import { Script } from 'node:vm';
import type { Element } from 'domhandler';
import { JSDOM } from 'jsdom';
import { Bench } from 'tinybench';
import type { Cheerio } from '../src/cheerio.js';
import type { CheerioAPI } from '../src/load.js';
import { load } from '../src/load-parse.js';

const documentDir = new URL('documents/', import.meta.url);
const jQuerySrc = await fs.readFile(
  new URL('../node_modules/jquery/dist/jquery.slim.js', import.meta.url),
  'utf8',
);
const jQueryScript = new Script(jQuerySrc);
const filterIndex = process.argv.indexOf('--filter') + 1;
const benchmarkFilter = filterIndex > 0 ? process.argv[filterIndex] : '';

const cheerioOnly = process.argv.includes('--cheerio-only');

type SuiteOptions<T> = T extends void
  ? {
      test(this: void, $: CheerioAPI): void;
      setup?: (this: void, $: CheerioAPI) => T;
    }
  : {
      test(this: void, $: CheerioAPI, data: T): void;
      setup(this: void, $: CheerioAPI): T;
    };

async function benchmark<T = void>(
  name: string,
  fileName: string,
  options: SuiteOptions<T>,
): Promise<void> {
  if (!name.includes(benchmarkFilter)) {
    return;
  }
  const markup = await fs.readFile(new URL(fileName, documentDir), 'utf8');

  console.log(`Test: ${name} (file: ${fileName})`);

  const bench = new Bench();
  const { test, setup } = options;

  // Add Cheerio test
  const $ = load(markup);
  const setupData = setup?.($) as T;

  bench.add('cheerio', () => {
    test($, setupData);
  });

  // Add JSDOM test
  if (!cheerioOnly) {
    const dom = new JSDOM(markup, { runScripts: 'outside-only' });

    jQueryScript.runInContext(dom.getInternalVMContext());

    const setupData = setup?.(dom.window['$'] as CheerioAPI) as T;

    bench.add('jsdom', () => test(dom.window['$'] as CheerioAPI, setupData));
  }

  await bench.run();

  console.table(bench.table());
}

await benchmark('Select all', 'jquery.html', {
  test: ($) => $('*').length,
});
await benchmark('Select some', 'jquery.html', {
  test: ($) => $('li').length,
});

/*
 * Manipulation Tests
 */
const DIVS_MARKUP = '<div>'.repeat(50);
await benchmark<Cheerio<Element>>('manipulation - append', 'jquery.html', {
  setup: ($) => $('body'),
  test: (_, $body) => $body.append(DIVS_MARKUP),
});

// JSDOM used to run out of memory on these tests
await benchmark<Cheerio<Element>>(
  'manipulation - prepend - highmem',
  'jquery.html',
  {
    setup: ($) => $('body'),
    test: (_, $body) => $body.prepend(DIVS_MARKUP),
  },
);
await benchmark<Cheerio<Element>>(
  'manipulation - after - highmem',
  'jquery.html',
  {
    setup: ($) => $('body'),
    test: (_, $body) => $body.after(DIVS_MARKUP),
  },
);
await benchmark<Cheerio<Element>>(
  'manipulation - before - highmem',
  'jquery.html',
  {
    setup: ($) => $('body'),
    test: (_, $body) => $body.before(DIVS_MARKUP),
  },
);

await benchmark<Cheerio<Element>>('manipulation - remove', 'jquery.html', {
  setup: ($) => $('body'),
  test($, $lis) {
    const child = $('<div>');
    $lis.append(child);
    child.remove();
  },
});

await benchmark('manipulation - replaceWith', 'jquery.html', {
  setup($) {
    $('body').append('<div id="foo">');
  },
  test($) {
    $('#foo').replaceWith('<div id="foo">');
  },
});

await benchmark<Cheerio<Element>>('manipulation - empty', 'jquery.html', {
  setup: ($) => $('li'),
  test(_, $lis) {
    $lis.empty();
  },
});
await benchmark<Cheerio<Element>>('manipulation - html', 'jquery.html', {
  setup: ($) => $('li'),
  test(_, $lis) {
    $lis.html();
    $lis.html('foo');
  },
});
await benchmark<Cheerio<Element>>('manipulation - html render', 'jquery.html', {
  setup: ($) => $('body'),
  test(_, $lis) {
    $lis.html();
  },
});

const HTML_INDEPENDENT_MARKUP =
  '<div class="foo"><div id="bar">bat<hr>baz</div> </div>'.repeat(6);
await benchmark('manipulation - html independent', 'jquery.html', {
  test: ($) => $(HTML_INDEPENDENT_MARKUP).html(),
});
await benchmark<Cheerio<Element>>('manipulation - text', 'jquery.html', {
  setup: ($) => $('li'),
  test(_, $lis) {
    $lis.text();
    $lis.text('foo');
  },
});

/*
 * Traversing Tests
 */
await benchmark<Cheerio<Element>>('traversing - Find', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.find('li').length,
});
await benchmark<Cheerio<Element>>('traversing - Parent', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.parent('div').length,
});
await benchmark<Cheerio<Element>>('traversing - Parents', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.parents('div').length,
});
await benchmark<Cheerio<Element>>('traversing - Closest', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.closest('div').length,
});
await benchmark<Cheerio<Element>>('traversing - next', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.next().length,
});
await benchmark<Cheerio<Element>>('traversing - nextAll', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.nextAll('li').length,
});
await benchmark<Cheerio<Element>>('traversing - nextUntil', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.nextUntil('li').length,
});
await benchmark<Cheerio<Element>>('traversing - prev', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.prev().length,
});
await benchmark<Cheerio<Element>>('traversing - prevAll', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.prevAll('li').length,
});
await benchmark<Cheerio<Element>>('traversing - prevUntil', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.prevUntil('li').length,
});
await benchmark<Cheerio<Element>>('traversing - siblings', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.siblings('li').length,
});
await benchmark<Cheerio<Element>>('traversing - Children', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.children('a').length,
});
await benchmark<Cheerio<Element>>('traversing - Filter', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.filter('li').length,
});
await benchmark<Cheerio<Element>>('traversing - First', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.first().first().length,
});
await benchmark<Cheerio<Element>>('traversing - Last', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.last().last().length,
});
await benchmark<Cheerio<Element>>('traversing - Eq', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.eq(0).eq(0).length,
});

/*
 * Attributes Tests
 */
await benchmark<Cheerio<Element>>('attributes - Attributes', 'jquery.html', {
  setup: ($) => $('li'),
  test(_, $lis) {
    $lis.attr('foo', 'bar');
    $lis.attr('foo');
    $lis.removeAttr('foo');
  },
});
await benchmark<Cheerio<Element>>(
  'attributes - Single Attribute',
  'jquery.html',
  {
    setup: ($) => $('body'),
    test(_, $lis) {
      $lis.attr('foo', 'bar');
      $lis.attr('foo');
      $lis.removeAttr('foo');
    },
  },
);
await benchmark<Cheerio<Element>>('attributes - Data', 'jquery.html', {
  setup: ($) => $('li'),
  test(_, $lis) {
    $lis.data('foo', 'bar');
    $lis.data('foo');
  },
});
await benchmark<Cheerio<Element>>('attributes - Val', 'jquery.html', {
  setup: ($) => $('select,input,textarea,option'),
  test($, $lis) {
    $lis.each(function () {
      $(this).val();
      $(this).val('foo');
    });
  },
});

await benchmark<Cheerio<Element>>('attributes - Has class', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.hasClass('foo'),
});
await benchmark<Cheerio<Element>>('attributes - Toggle class', 'jquery.html', {
  setup: ($) => $('li'),
  test: (_, $lis) => $lis.toggleClass('foo'),
});
await benchmark<Cheerio<Element>>(
  'attributes - Add Remove class',
  'jquery.html',
  {
    setup: ($) => $('li'),
    test(_, $lis) {
      $lis.addClass('foo');
      $lis.removeClass('foo');
    },
  },
);
```

## File: `benchmark/documents/jquery.html`
```html
<html
  class="js multiplebgs boxshadow cssgradients wf-klavikaweb-i7-active wf-klavikaweb-n7-active wf-sourcecodepro-n4-active wf-sourcecodepro-n7-active wf-active"
  lang="en-US"
>
  <head data-live-domain="api.jquery.com">
    <script type="text/javascript" async="" src="null"></script>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <title>jQuery() | jQuery API Documentation</title>

    <meta name="author" content="jQuery Foundation - jquery.org" />
    <meta
      name="description"
      content="jQuery: The Write Less, Do More, JavaScript Library"
    />

    <meta name="viewport" content="width=device-width" />

    <link
      rel="shortcut icon"
      href="http://api.jquery.com/jquery-wp-content/themes/api.jquery.com/i/favicon.ico"
      src="null"
    />

    <link
      rel="stylesheet"
      href="http://api.jquery.com/jquery-wp-content/themes/jquery/css/base.css?v=1"
      src="null"
    />
    <link
      rel="stylesheet"
      href="http://api.jquery.com/jquery-wp-content/themes/api.jquery.com/style.css"
      src="null"
    />
    <link rel="pingback" href="http://api.jquery.com/xmlrpc.php" src="null" />
    <!--[if lt IE 7
      ]><link rel="stylesheet" href="css/font-awesome-ie7.min.css"
    /><![endif]-->

    <script type="text/javascript" async="" src="null"></script>
    <script src="null"></script>

    <script src="null"></script>
    <script>
      window.jQuery ||
        document.write(
          unescape(
            '%3Cscript src="http://api.jquery.com/jquery-wp-content/themes/jquery/js/jquery-1.9.1.min.js"%3E%3C/script%3E'
          )
        );
    </script>
    <script src="null"></script>

    <script src="null"></script>
    <script src="null"></script>

    <script src="null"></script>
    <style type="text/css">
      .tk-source-code-pro {
        font-family: 'source-code-pro', sans-serif;
      }
      .tk-klavika-web {
        font-family: 'klavika-web', sans-serif;
      }
    </style>
    <link
      rel="stylesheet"
      href="http://use.typekit.net/c/d4d852/klavika-web:i7:n7,source-code-pro:n4:n7.PYh:F:2,PYg:F:2,Y1M:F:2,Y1P:F:2/d?3bb2a6e53c9684ffdc9a98f2135b2a6250f2340d8ca0853b7df9676f5fa610fe069f9d29c9b5e67ae7b6312a16ff95d3a73356eed53502d6630d88cb0fe9789e0ac2d9a6c14ac282069f97be80efceecd4f5e0e58b889e8649ff22efc0c4063e9f9f87c7a8920dcab32add3496e6b09e6a94141aaaeb81a4bb1d4a09b8a14ac46d7d0dff3bf6532c044b0313c5ed1d7226c76cac5039645b4082ff59a8953c4e06ef9a344cf9265e8de3ed48ac2f34b281583cbaf6f2f580f7709eba9ea284dc14f4722ed0e264d7faa135466fbba043f093297f0efc92bfcb7b3eb8761407436be31d8029117f1a72aa7b8b6319c956c739e1c25b7a993a45"
      src="null"
    />
    <script>
      try {
        Typekit.load();
      } catch (_e) {}
    </script>

    <link
      rel="alternate"
      type="application/rss+xml"
      title="jQuery API Documentation » Feed"
      href="http://api.jquery.com/feed/"
      src="null"
    />
    <link
      rel="alternate"
      type="application/rss+xml"
      title="jQuery API Documentation » Comments Feed"
      href="http://api.jquery.com/comments/feed/"
      src="null"
    />
    <link
      rel="alternate"
      type="application/rss+xml"
      title="jQuery API Documentation » jQuery() Comments Feed"
      href="http://api.jquery.com/jQuery/feed/"
      src="null"
    />
    <script type="text/javascript" src="null"></script>
    <link
      rel="EditURI"
      type="application/rsd+xml"
      title="RSD"
      href="http://api.jquery.com/xmlrpc.php?rsd"
      src="null"
    />
    <link
      rel="wlwmanifest"
      type="application/wlwmanifest+xml"
      href="http://api.jquery.com/wp-includes/wlwmanifest.xml"
      src="null"
    />
    <link
      rel="prev"
      title="jQuery.holdReady()"
      href="http://api.jquery.com/jQuery.holdReady/"
      src="null"
    />
    <link
      rel="next"
      title="jQuery.inArray()"
      href="http://api.jquery.com/jQuery.inArray/"
      src="null"
    />
    <meta name="generator" content="WordPress 3.7" />
    <link rel="canonical" href="http://api.jquery.com/jQuery/" src="null" />
    <link rel="shortlink" href="http://api.jquery.com/?p=339" src="null" />
  </head>
  <body
    class="api jquery single single-post postid-339 single-format-standard single-author singular"
  >
    <!--[if lt IE 7]>
      <p class="chromeframe">
        You are using an outdated browser.
        <a href="http://browsehappy.com/">Upgrade your browser today</a>
        or
        <a href="http://www.google.com/chromeframe/?redirect=true"
          >install Google Chrome Frame</a
        >
        to better experience this site.
      </p>
    <![endif]-->

    <header>
      <section id="global-nav">
        <nav>
          <div class="constrain">
            <ul class="projects">
              <li class="project jquery">
                <a href="http://jquery.com/" title="jQuery" src="null"
                  >jQuery</a
                >
              </li>
              <li class="project jquery-ui">
                <a href="http://jqueryui.com/" title="jQuery UI" src="null"
                  >jQuery UI</a
                >
              </li>
              <li class="project jquery-mobile">
                <a
                  href="http://jquerymobile.com/"
                  title="jQuery Mobile"
                  src="null"
                  >jQuery Mobile</a
                >
              </li>
              <li class="project sizzlejs">
                <a href="http://sizzlejs.com/" title="Sizzle" src="null"
                  >Sizzle</a
                >
              </li>
              <li class="project qunitjs">
                <a href="http://qunitjs.com/" title="QUnit" src="null">QUnit</a>
              </li>
            </ul>
            <ul class="links l_tinynav1">
              <li>
                <a href="http://plugins.jquery.com/" src="null">Plugins</a>
              </li>
              <li class="dropdown">
                <a href="http://contribute.jquery.org/" src="null"
                  >Contribute</a
                >
                <ul>
                  <li>
                    <a href="http://contribute.jquery.org/cla/" src="null"
                      >CLA</a
                    >
                  </li>
                  <li>
                    <a
                      href="http://contribute.jquery.org/style-guide/"
                      src="null"
                      >Style Guides</a
                    >
                  </li>
                  <li>
                    <a href="http://contribute.jquery.org/triage/" src="null"
                      >Bug Triage</a
                    >
                  </li>
                  <li>
                    <a href="http://contribute.jquery.org/code/" src="null"
                      >Code</a
                    >
                  </li>
                  <li>
                    <a
                      href="http://contribute.jquery.org/documentation/"
                      src="null"
                      >Documentation</a
                    >
                  </li>
                  <li>
                    <a href="http://contribute.jquery.org/web-sites/" src="null"
                      >Web Sites</a
                    >
                  </li>
                </ul>
              </li>
              <li class="dropdown">
                <a href="http://events.jquery.org/" src="null">Events</a>
                <ul class="wide">
                  <li>
                    <a
                      href="http://www.deque.com/deque-partners-jquery-create-accessibility-summit"
                      src="null"
                      >Oct 10-11 | jQuery Accessibility Summit</a
                    >
                  </li>
                  <li>
                    <a href="http://jquery.itmozg.ru/" src="null"
                      >Oct 15 | jQuery Russia</a
                    >
                  </li>
                  <li>
                    <a
                      href="http://modernweb.com/training/jquery-oct-2013.php"
                      src="null"
                      >Oct 15-17 | jQuery Virtual Training</a
                    >
                  </li>
                  <li>
                    <a href="http://2013.cssdevconf.com/" src="null"
                      >Oct 21-22 | CSS Dev Conf</a
                    >
                  </li>
                  <li>
                    <a href="http://javascriptsummit.com/" src="null"
                      >Nov 19-21 | JavaScript Summit</a
                    >
                  </li>
                  <li>
                    <a
                      href="http://events.jquery.org/2014/san-diego/"
                      src="null"
                      >Feb 12-13 | jQuery San Diego</a
                    >
                  </li>
                  <li>
                    <a href="http://www.gentics.com/jquery-europe" src="null"
                      >Feb 28-Mar 1 | jQuery Europe</a
                    >
                  </li>
                  <li>
                    <a href="http://jqueryuk.com" src="null"
                      >May 16 | jQuery UK</a
                    >
                  </li>
                </ul>
              </li>
              <li class="dropdown">
                <a href="https://jquery.org/support/" src="null">Support</a>
                <ul>
                  <li>
                    <a href="http://learn.jquery.com/" src="null"
                      >Learning Center</a
                    >
                  </li>
                  <li>
                    <a href="http://try.jquery.com/" src="null">Try jQuery</a>
                  </li>
                  <li>
                    <a href="http://irc.jquery.org/" src="null">IRC/Chat</a>
                  </li>
                  <li>
                    <a href="http://forum.jquery.com/" src="null">Forums</a>
                  </li>
                  <li>
                    <a
                      href="http://stackoverflow.com/tags/jquery/info"
                      src="null"
                      >Stack Overflow</a
                    >
                  </li>
                  <li>
                    <a href="https://jquery.org/support/" src="null"
                      >Commercial Support</a
                    >
                  </li>
                </ul>
              </li>
              <li class="dropdown">
                <a href="https://jquery.org/" src="null">jQuery Foundation</a>
                <ul>
                  <li>
                    <a href="https://jquery.org/join/" src="null">Join</a>
                  </li>
                  <li>
                    <a href="https://jquery.org/members/" src="null">Members</a>
                  </li>
                  <li>
                    <a href="https://jquery.org/team/" src="null">Team</a>
                  </li>
                  <li>
                    <a href="http://brand.jquery.org/" src="null"
                      >Brand Guide</a
                    >
                  </li>
                  <li>
                    <a href="https://jquery.org/donate/" src="null">Donate</a>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </nav>
      </section>
    </header>

    <div id="container">
      <div id="logo-events" class="constrain clearfix">
        <h2 class="logo">
          <a
            href="http://jquery.com/"
            title="jQuery API Documentation"
            src="null"
            >jQuery API Documentation</a
          >
        </h2>

        <aside>
          <div id="broadcast">
            <a
              href="http://engine.adzerk.net/r?e=eyJhdiI6MjIyMzYsImF0IjoxMzE0LCJjbSI6NjM3NjcsImNoIjo4MzY4LCJjciI6MTc4ODcxLCJkaSI6ImZhNDViODgwMzBhOTQxYzNhZmMyZTg0MmIwYzFiZDI1IiwiZG0iOjEsImZjIjoyMjgyOTgsImZsIjoxMTM1MjksImt3IjoidW5kZWZpbmVkIiwibnciOjU0NDksInJmIjoiaHR0cDovL2FwaS5qcXVlcnkuY29tLz9zPWpxdWVyeSIsInJ2IjowLCJwciI6MjE5MzcsInN0Ijo1MzgyOSwidHMiOjEzODU4Mzk5ODgyOTIsInVyIjoiaHR0cDovL2V2ZW50cy5qcXVlcnkub3JnLzIwMTQvc2FuLWRpZWdvLyJ9&amp;s=pUb8fXw8Ar8bGvQszZJHXjkx8Gk"
              rel="nofollow"
              target="_blank"
              title="jQuery San Diego"
              src="null"
              ><img
                src="null"
                title="jQuery San Diego"
                alt="jQuery San Diego"
                border="0"
                width="400"
                height="100" /></a
            ><img height="0px" width="0px" border="0" src="null" alt="" />
          </div>
        </aside>
      </div>

      <nav id="main" class="constrain clearfix">
        <div class="menu-top-container">
          <ul id="menu-top" class="menu l_tinynav2">
            <li class="menu-item">
              <a href="http://jquery.com/download/" src="null">Download</a>
            </li>
            <li class="menu-item current">
              <a href="http://api.jquery.com/" src="null">API Documentation</a>
            </li>
            <li class="menu-item">
              <a href="http://blog.jquery.com/" src="null">Blog</a>
            </li>
            <li class="menu-item">
              <a href="http://plugins.jquery.com/" src="null">Plugins</a>
            </li>
            <li class="menu-item">
              <a href="http://jquery.com/browser-support/" src="null"
                >Browser Support</a
              >
            </li>
          </ul>
          <select id="tinynav2" class="tinynav tinynav2"
            ><option>Navigate...</option
            ><option value="http://jquery.com/download/">Download</option
            ><option value="http://api.jquery.com/">API Documentation</option
            ><option value="http://blog.jquery.com/">Blog</option
            ><option value="http://plugins.jquery.com/">Plugins</option
            ><option value="http://jquery.com/browser-support/"
              >Browser Support</option
            ></select
          >
        </div>

        <form method="get" class="searchform" action="http://api.jquery.com/">
          <button type="submit" class="icon-search">
            <span class="visuallyhidden">search</span>
          </button>
          <label>
            <span class="visuallyhidden">Search jQuery API Documentation</span>
            <input type="text" name="s" value="" placeholder="Search" />
          </label>
          <label>
            <span class="visuallyhidden">Search jQuery API Documentation</span>
            <input type="radio" name="rad" value="" placeholder="Search" />
          </label>
          <label>
            <span class="visuallyhidden">Search jQuery API Documentation</span>
            <input type="radio" name="rad" value="foo" placeholder="Search" />
          </label>
        </form>
      </nav>

      <div id="content-wrapper" class="clearfix row">
        <div class="content-right twelve columns">
          <div id="content">
            <article
              id="post-339"
              class="post-339 post type-post status-publish format-standard hentry category-core category-10 category-14"
            >
              <header class="entry-header">
                <h1 class="entry-title">jQuery()</h1>
                <hr />
                <div class="entry-meta">
                  Categories:
                  <span class="category"
                    ><a
                      href="http://api.jquery.com/category/core/"
                      title="View all posts in Core"
                      src="null"
                      >Core</a
                    ></span
                  >
                </div>
                <!-- .entry-meta -->
              </header>
              <!-- .entry-header -->

              <div class="entry-content">
                Return a collection of matched elements either found in the DOM
                based on passed argument(s) or created by passing an HTML
                string.
                <div class="toc">
                  <h4><span>Contents:</span></h4>
                  <ul class="toc-list">
                    <li>
                      <a href="#jQuery1" src="null"
                        >jQuery( selector [, context ] )</a
                      >
                      <ul>
                        <li>
                          <a href="#jQuery-selector-context" src="null"
                            >jQuery( selector [, context ] )</a
                          >
                        </li>
                        <li>
                          <a href="#jQuery-element" src="null"
                            >jQuery( element )</a
                          >
                        </li>
                        <li>
                          <a href="#jQuery-elementArray" src="null"
                            >jQuery( elementArray )</a
                          >
                        </li>
                        <li>
                          <a href="#jQuery-object" src="null"
                            >jQuery( object )</a
                          >
                        </li>
                        <li>
                          <a href="#jQuery-jQuery-object" src="null"
                            >jQuery( jQuery object )</a
                          >
                        </li>
                        <li>
                          <a href="#jQuery" src="null">jQuery()</a>
                        </li>
                      </ul>
                    </li>
                    <li>
                      <a href="#jQuery2" src="null"
                        >jQuery( html [, ownerDocument ] )</a
                      >
                      <ul>
                        <li>
                          <a href="#jQuery-html-ownerDocument" src="null"
                            >jQuery( html [, ownerDocument ] )</a
                          >
                        </li>
                        <li>
                          <a href="#jQuery-html-attributes" src="null"
                            >jQuery( html, attributes )</a
                          >
                        </li>
                      </ul>
                    </li>
                    <li>
                      <a href="#jQuery3" src="null">jQuery( callback )</a>
                      <ul>
                        <li>
                          <a href="#jQuery-callback" src="null"
                            >jQuery( callback )</a
                          >
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
                <article id="jQuery1" class="entry method">
                  <h2 class="section-title">
                    <span class="name">jQuery( selector [, context ] )</span
                    ><span class="returns"
                      >Returns:
                      <a href="http://api.jquery.com/Types/#jQuery" src="null"
                        >jQuery</a
                      ></span
                    >
                  </h2>
                  <div class="entry-wrapper">
                    <p class="desc">
                      <strong>Description: </strong>Accepts a string containing
                      a CSS selector which is then used to match a set of
                      elements.
                    </p>
                    <ul class="signatures">
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-selector-context"
                            href="#jQuery-selector-context"
                            src="null"
                            ><span class="icon-link"></span>jQuery( selector [,
                            context ] )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>selector</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#Selector"
                                src="null"
                                >Selector</a
                              >
                            </div>
                            <div>
                              A string containing a selector expression
                            </div>
                          </li>
                          <li>
                            <div>
                              <strong>context</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#Element"
                                src="null"
                                >Element</a
                              >
                              or
                              <a
                                href="http://api.jquery.com/Types/#jQuery"
                                src="null"
                                >jQuery</a
                              >
                            </div>
                            <div>
                              A DOM Element, Document, or jQuery to use as
                              context
                            </div>
                          </li>
                        </ul>
                      </li>
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-element"
                            href="#jQuery-element"
                            src="null"
                            ><span class="icon-link"></span>jQuery( element )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>element</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#Element"
                                src="null"
                                >Element</a
                              >
                            </div>
                            <div>
                              A DOM element to wrap in a jQuery object.
                            </div>
                          </li>
                        </ul>
                      </li>
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-elementArray"
                            href="#jQuery-elementArray"
                            src="null"
                            ><span class="icon-link"></span>jQuery( elementArray
                            )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>elementArray</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#Array"
                                src="null"
                                >Array</a
                              >
                            </div>
                            <div>
                              An array containing a set of DOM elements to wrap
                              in a jQuery object.
                            </div>
                          </li>
                        </ul>
                      </li>
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-object"
                            href="#jQuery-object"
                            src="null"
                            ><span class="icon-link"></span>jQuery( object )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>object</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#PlainObject"
                                src="null"
                                >PlainObject</a
                              >
                            </div>
                            <div>
                              A plain object to wrap in a jQuery object.
                            </div>
                          </li>
                        </ul>
                      </li>
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-jQuery-object"
                            href="#jQuery-jQuery-object"
                            src="null"
                            ><span class="icon-link"></span>jQuery( jQuery
                            object )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>jQuery object</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#PlainObject"
                                src="null"
                                >PlainObject</a
                              >
                            </div>
                            <div>
                              An existing jQuery object to clone.
                            </div>
                          </li>
                        </ul>
                      </li>
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.4/" src="null"
                              >1.4</a
                            ></span
                          ><a id="jQuery" href="#jQuery" src="null"
                            ><span class="icon-link"></span>jQuery()</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div class="null-signature">
                              This signature does not accept any arguments.
                            </div>
                          </li>
                        </ul>
                      </li>
                    </ul>
                    <div class="longdesc" id="entry-longdesc">
                      <p>
                        In the first formulation listed above,
                        <code>jQuery()</code> — which can also be written as
                        <code>$()</code> — searches through the DOM for any
                        elements that match the provided selector and creates a
                        new jQuery object that references these elements:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"div.foo"</span> );</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        If no elements match the provided selector, the new
                        jQuery object is "empty"; that is, it contains no
                        elements and has
                        <code><a href="/length/" src="null">.length</a></code>
                        property of 0.
                      </p>
                      <h4 id="selector-context">
                        Selector Context
                      </h4>
                      <p>
                        By default, selectors perform their searches within the
                        DOM starting at the document root. However, an alternate
                        context can be given for the search by using the
                        optional second parameter to the
                        <code>$()</code> function. For example, to do a search
                        within an event handler, the search can be restricted
                        like so:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>

                                <div class="line n3">
                                  3
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"div.foo"</span> ).click(<span class="keyword">function</span>() {</code></div></div><div class="container"><div class="line"><code>  $( <span class="string">"span"</span>, <span class="keyword">this</span> ).addClass( <span class="string">"bar"</span> );</code></div></div><div class="container"><div class="line"><code>});</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        When the search for the span selector is restricted to
                        the context of <code>this</code>, only spans within the
                        clicked element will get the additional class.
                      </p>
                      <p>
                        Internally, selector context is implemented with the
                        <code>.find()</code> method, so
                        <code>$( "span", this )</code>
                        is equivalent to
                        <code>$( this ).find( "span" )</code>.
                      </p>

                      <h4 id="using-dom-elements">
                        Using DOM elements
                      </h4>
                      <p>
                        The second and third formulations of this function
                        create a jQuery object using one or more DOM elements
                        that were already selected in some other way.
                      </p>
                      <p>
                        <strong>Note:</strong> These formulations are meant to
                        consume only DOM elements; feeding mixed data to the
                        elementArray form is particularly discouraged.
                      </p>
                      <p>
                        A common use of this facility is to call jQuery methods
                        on an element that has been passed to a callback
                        function through the keyword <code>this</code>:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>

                                <div class="line n3">
                                  3
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"div.foo"</span> ).click(<span class="keyword">function</span>() {</code></div></div><div class="container"><div class="line"><code>  $( <span class="keyword">this</span> ).slideUp();</code></div></div><div class="container"><div class="line"><code>});</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        This example causes elements to be hidden with a sliding
                        animation when clicked. Because the handler receives the
                        clicked item in the
                        <code>this</code> keyword as a bare DOM element, the
                        element must be passed to the <code>$()</code> function
                        before applying jQuery methods to it.
                      </p>
                      <p>
                        XML data returned from an Ajax call can be passed to the
                        <code>$()</code> function so individual elements of the
                        XML structure can be retrieved using
                        <code>.find()</code> and other DOM traversal methods.
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>

                                <div class="line n3">
                                  3
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$.post( <span class="string">"url.xml"</span>, <span class="keyword">function</span>( data ) {</code></div></div><div class="container"><div class="line"><code>  <span class="keyword">var</span> $child = $( data ).find( <span class="string">"child"</span> );</code></div></div><div class="container"><div class="line"><code>});</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <h4 id="cloning-jquery-objects">
                        Cloning jQuery Objects
                      </h4>
                      <p>
                        When a jQuery object is passed to the
                        <code>$()</code> function, a clone of the object is
                        created. This new jQuery object references the same DOM
                        elements as the initial one.
                      </p>

                      <h4 id="returning-empty-set">
                        Returning an Empty Set
                      </h4>
                      <p>
                        As of jQuery 1.4, calling the
                        <code>jQuery()</code> method with
                        <em>no arguments</em> returns an empty jQuery set (with
                        a
                        <code><a href="/length/" src="null">.length</a></code>
                        property of 0). In previous versions of jQuery, this
                        would return a set containing the document node.
                      </p>
                      <h4 id="working-with-plain-objects">
                        Working With Plain Objects
                      </h4>
                      <p>
                        At present, the only operations supported on plain
                        JavaScript objects wrapped in jQuery are:
                        <code>.data()</code
                        >,<code>.prop()</code>,<code>.on()</code>,
                        <code>.off()</code>, <code>.trigger()</code> and
                        <code>.triggerHandler()</code>. The use of
                        <code>.data()</code> (or any method requiring
                        <code>.data()</code>) on a plain object will result in a
                        new property on the object called jQuery{randomNumber}
                        (eg. jQuery123456789).
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>

                                <div class="line n3">
                                  3
                                </div>

                                <div class="line n4">
                                  4
                                </div>

                                <div class="line n5">
                                  5
                                </div>

                                <div class="line n6">
                                  6
                                </div>

                                <div class="line n7">
                                  7
                                </div>

                                <div class="line n8">
                                  8
                                </div>

                                <div class="line n9">
                                  9
                                </div>

                                <div class="line n10">
                                  10
                                </div>

                                <div class="line n11">
                                  11
                                </div>

                                <div class="line n12">
                                  12
                                </div>

                                <div class="line n13">
                                  13
                                </div>

                                <div class="line n14">
                                  14
                                </div>

                                <div class="line n15">
                                  15
                                </div>

                                <div class="line n16">
                                  16
                                </div>

                                <div class="line n17">
                                  17
                                </div>

                                <div class="line n18">
                                  18
                                </div>

                                <div class="line n19">
                                  19
                                </div>

                                <div class="line n20">
                                  20
                                </div>

                                <div class="line n21">
                                  21
                                </div>

                                <div class="line n22">
                                  22
                                </div>

                                <div class="line n23">
                                  23
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code><span class="comment">// Define a plain object</span></code></div></div><div class="container"><div class="line"><code><span class="keyword">var</span> foo = { foo: <span class="string">"bar"</span>, hello: <span class="string">"world"</span> };</code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="comment">// Pass it to the jQuery function</span></code></div></div><div class="container"><div class="line"><code><span class="keyword">var</span> $foo = $( foo );</code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="comment">// Test accessing property values</span></code></div></div><div class="container"><div class="line"><code><span class="keyword">var</span> test1 = $foo.prop( <span class="string">"foo"</span> ); <span class="comment">// bar</span></code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="comment">// Test setting property values</span></code></div></div><div class="container"><div class="line"><code>$foo.prop( <span class="string">"foo"</span>, <span class="string">"foobar"</span> );</code></div></div><div class="container"><div class="line"><code><span class="keyword">var</span> test2 = $foo.prop( <span class="string">"foo"</span> ); <span class="comment">// foobar</span></code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="comment">// Test using .data() as summarized above</span></code></div></div><div class="container"><div class="line"><code>$foo.data( <span class="string">"keyName"</span>, <span class="string">"someValue"</span> );</code></div></div><div class="container"><div class="line"><code>console.log( $foo ); <span class="comment">// will now contain a jQuery{randomNumber} property</span></code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="comment">// Test binding an event name and triggering</span></code></div></div><div class="container"><div class="line"><code>$foo.on( <span class="string">"eventName"</span>, <span class="function"><span class="keyword">function</span> <span class="params">()</span> {</span></code></div></div><div class="container"><div class="line"><code>  console.log( <span class="string">"eventName was called"</span> );</code></div></div><div class="container"><div class="line"><code>});</code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code>$foo.trigger( <span class="string">"eventName"</span> ); <span class="comment">// Logs "eventName was called"</span></code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        Should
                        <code>.trigger( "eventName" )</code>
                        be used, it will search for an "eventName" property on
                        the object and attempt to execute it after any attached
                        jQuery handlers are executed. It does not check whether
                        the property is a function or not. To avoid this
                        behavior,
                        <code>.triggerHandler( "eventName" )</code>
                        should be used instead.
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$foo.triggerHandler( <span class="string">"eventName"</span> ); <span class="comment">// Also logs "eventName was called"</span></code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                    <section class="entry-examples" id="entry-examples">
                      <header><h2>Examples:</h2></header>
                      <div class="entry-example" id="example-0">
                        <h4>
                          Example:
                          <span class="desc"
                            >Find all p elements that are children of a div
                            element and apply a border to them.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter xml">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>

                                  <div class="line n2">
                                    2
                                  </div>

                                  <div class="line n3">
                                    3
                                  </div>

                                  <div class="line n4">
                                    4
                                  </div>

                                  <div class="line n5">
                                    5
                                  </div>

                                  <div class="line n6">
                                    6
                                  </div>

                                  <div class="line n7">
                                    7
                                  </div>

                                  <div class="line n8">
                                    8
                                  </div>

                                  <div class="line n9">
                                    9
                                  </div>

                                  <div class="line n10">
                                    10
                                  </div>

                                  <div class="line n11">
                                    11
                                  </div>

                                  <div class="line n12">
                                    12
                                  </div>

                                  <div class="line n13">
                                    13
                                  </div>

                                  <div class="line n14">
                                    14
                                  </div>

                                  <div class="line n15">
                                    15
                                  </div>

                                  <div class="line n16">
                                    16
                                  </div>

                                  <div class="line n17">
                                    17
                                  </div>

                                  <div class="line n18">
                                    18
                                  </div>

                                  <div class="line n19">
                                    19
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code><span class="doctype">&lt;!doctype html&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">html</span> <span class="attribute">lang</span>=<span class="value">"en"</span>&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">head</span>&gt;</span></code></div></div><div class="container"><div class="line"><code>  <span class="tag">&lt;<span class="title">meta</span> <span class="attribute">charset</span>=<span class="value">"utf-8"</span>&gt;</span></code></div></div><div class="container"><div class="line"><code>  <span class="tag">&lt;<span class="title">title</span>&gt;</span>jQuery demo<span class="tag">&lt;/<span class="title">title</span>&gt;</span></code></div></div><div class="container"><div class="line"><code>  <span class="tag">&lt;<span class="title">script</span> <span class="attribute">src</span>=<span class="value">"http://code.jquery.com/jquery-1.9.1.js"</span>&gt;</span><span class="javascript"></span><span class="tag">&lt;/<span class="title">script</span>&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;/<span class="title">head</span>&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">body</span>&gt;</span></code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">p</span>&gt;</span>one<span class="tag">&lt;/<span class="title">p</span>&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">div</span>&gt;</span><span class="tag">&lt;<span class="title">p</span>&gt;</span>two<span class="tag">&lt;/<span class="title">p</span>&gt;</span><span class="tag">&lt;/<span class="title">div</span>&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">p</span>&gt;</span>three<span class="tag">&lt;/<span class="title">p</span>&gt;</span></code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;<span class="title">script</span>&gt;</span><span class="javascript"></span></code></div></div><div class="container"><div class="line"><code>$( <span class="string">"div &gt; p"</span> ).css( <span class="string">"border"</span>, <span class="string">"1px solid gray"</span> );</code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;/<span class="title">script</span>&gt;</span></code></div></div><div class="container"><div class="line"><code> </code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;/<span class="title">body</span>&gt;</span></code></div></div><div class="container"><div class="line"><code><span class="tag">&lt;/<span class="title">html</span>&gt;</span></code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>

                        <h4>Demo:</h4>
                        <div class="demo code-demo">
                          <iframe width="100%" height="250" title="Demo"></iframe>
                        </div>
                      </div>
                      <div class="entry-example" id="example-1">
                        <h4>
                          Example:
                          <span class="desc"
                            >Find all inputs of type radio within the first form
                            in the document.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$( <span class="string">"input:radio"</span>, document.forms[ <span class="number">0</span> ] );</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div class="entry-example" id="example-2">
                        <h4>
                          Example:
                          <span class="desc"
                            >Find all div elements within an XML document from
                            an Ajax response.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$( <span class="string">"div"</span>, xml.responseXML );</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div class="entry-example" id="example-3">
                        <h4>
                          Example:
                          <span class="desc"
                            >Set the background color of the page to
                            black.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$( document.body ).css( <span class="string">"background"</span>, <span class="string">"black"</span> );</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div class="entry-example" id="example-4">
                        <h4>
                          Example:
                          <span class="desc"
                            >Hide all the input elements within a form.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$( myForm.elements ).hide();</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </section>
                  </div>
                </article>
                <article id="jQuery2" class="entry method">
                  <h2 class="section-title">
                    <span class="name">jQuery( html [, ownerDocument ] )</span
                    ><span class="returns"
                      >Returns:
                      <a href="http://api.jquery.com/Types/#jQuery" src="null"
                        >jQuery</a
                      ></span
                    >
                  </h2>
                  <div class="entry-wrapper">
                    <p class="desc">
                      <strong>Description: </strong>Creates DOM elements on the
                      fly from the provided string of raw HTML.
                    </p>
                    <ul class="signatures">
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-html-ownerDocument"
                            href="#jQuery-html-ownerDocument"
                            src="null"
                            ><span class="icon-link"></span>jQuery( html [,
                            ownerDocument ] )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>html</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#htmlString"
                                src="null"
                                >htmlString</a
                              >
                            </div>
                            <div>
                              A string of HTML to create on the fly. Note that
                              this parses HTML,
                              <strong>not</strong>
                              XML.
                            </div>
                          </li>
                          <li>
                            <div>
                              <strong>ownerDocument</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#document"
                                src="null"
                                >document</a
                              >
                            </div>
                            <div>
                              A document in which the new elements will be
                              created.
                            </div>
                          </li>
                        </ul>
                      </li>
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.4/" src="null"
                              >1.4</a
                            ></span
                          ><a
                            id="jQuery-html-attributes"
                            href="#jQuery-html-attributes"
                            src="null"
                            ><span class="icon-link"></span>jQuery( html,
                            attributes )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>html</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#htmlString"
                                src="null"
                                >htmlString</a
                              >
                            </div>
                            <div>
                              A string defining a single, standalone, HTML
                              element (e.g. &lt;div/&gt; or
                              &lt;div&gt;&lt;/div&gt;).
                            </div>
                          </li>
                          <li>
                            <div>
                              <strong>attributes</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#PlainObject"
                                src="null"
                                >PlainObject</a
                              >
                            </div>
                            <div>
                              An object of attributes, events, and methods to
                              call on the newly-created element.
                            </div>
                          </li>
                        </ul>
                      </li>
                    </ul>
                    <div class="longdesc" id="entry-longdesc-1">
                      <h4 id="creating-new-elements">
                        Creating New Elements
                      </h4>
                      <p>
                        If a string is passed as the parameter to
                        <code>$()</code>, jQuery examines the string to see if
                        it looks like HTML (i.e., it starts with
                        <code>&lt;tag ... &gt;</code>). If not, the string is
                        interpreted as a selector expression, as explained
                        above. But if the string appears to be an HTML snippet,
                        jQuery attempts to create new DOM elements as described
                        by the HTML. Then a jQuery object is created and
                        returned that refers to these elements. You can perform
                        any of the usual jQuery methods on this object:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;p id='test'&gt;My &lt;em&gt;new&lt;/em&gt; text&lt;/p&gt;"</span> ).appendTo( <span class="string">"body"</span> );</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        For explicit parsing of a string to HTML, use the
                        <a href="/jQuery.parseHTML/" src="null"
                          >$.parseHTML()</a
                        >
                        method.
                      </p>
                      <p>
                        By default, elements are created with an
                        <code>ownerDocument</code>
                        matching the document into which the jQuery library was
                        loaded. Elements being injected into a different
                        document should be created using that document, e.g.,
                        <code
                          >$("&lt;p&gt;hello iframe&lt;/p&gt;",
                          $("#myiframe").prop("contentWindow").document)</code
                        >.
                      </p>
                      <p>
                        If the HTML is more complex than a single tag without
                        attributes, as it is in the above example, the actual
                        creation of the elements is handled by the browser's
                        <code>innerHTML</code>
                        mechanism. In most cases, jQuery creates a new
                        &lt;div&gt; element and sets the innerHTML property of
                        the element to the HTML snippet that was passed in. When
                        the parameter has a single tag (with optional closing
                        tag or quick-closing) —
                        <code>$( "&lt;img&nbsp;/&gt;" )</code>
                        or
                        <code>$( "&lt;img&gt;" )</code>,
                        <code>$( "&lt;a&gt;&lt;/a&gt;" )</code>
                        or
                        <code>$( "&lt;a&gt;" )</code> — jQuery creates the
                        element using the native JavaScript
                        <code>createElement()</code>
                        function.
                      </p>
                      <p>
                        When passing in complex HTML, some browsers may not
                        generate a DOM that exactly replicates the HTML source
                        provided. As mentioned, jQuery uses the browser"s
                        <code>.innerHTML</code> property to parse the passed
                        HTML and insert it into the current document. During
                        this process, some browsers filter out certain elements
                        such as <code>&lt;html&gt;</code>,
                        <code>&lt;title&gt;</code>, or
                        <code>&lt;head&gt;</code>
                        elements. As a result, the elements inserted may not be
                        representative of the original string passed.
                      </p>
                      <p>
                        Filtering isn't, however, limited to these tags. For
                        example, Internet Explorer prior to version 8 will also
                        convert all <code>href</code> properties on links to
                        absolute URLs, and Internet Explorer prior to version 9
                        will not correctly handle HTML5 elements without the
                        addition of a separate
                        <a href="http://code.google.com/p/html5shiv/" src="null"
                          >compatibility layer</a
                        >.
                      </p>
                      <p>
                        To ensure cross-platform compatibility, the snippet must
                        be well-formed. Tags that can contain other elements
                        should be paired with a closing tag:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;a href='http://jquery.com'&gt;&lt;/a&gt;"</span> );</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        Tags that cannot contain elements may be quick-closed or
                        not:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;img&gt;"</span> );</code></div></div><div class="container"><div class="line"><code>$( <span class="string">"&lt;input&gt;"</span> );</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        When passing HTML to
                        <code>jQuery()</code>, please also note that text nodes
                        are not treated as DOM elements. With the exception of a
                        few methods (such as <code>.content()</code>), they are
                        generally otherwise ignored or removed. E.g:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code><span class="keyword">var</span> el = $( <span class="string">"1&lt;br&gt;2&lt;br&gt;3"</span> ); <span class="comment">// returns [&lt;br&gt;, "2", &lt;br&gt;]</span></code></div></div><div class="container"><div class="line"><code>el = $( <span class="string">"1&lt;br&gt;2&lt;br&gt;3 &gt;"</span> ); <span class="comment">// returns [&lt;br&gt;, "2", &lt;br&gt;, "3 &amp;gt;"]</span></code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>This behavior is expected.</p>
                      <p>
                        As of jQuery 1.4, the second argument to
                        <code>jQuery()</code> can accept a plain object
                        consisting of a superset of the properties that can be
                        passed to the
                        <a href="/attr/" src="null">.attr()</a>
                        method.
                      </p>
                      <p>
                        <strong>Important:</strong> If the second argument is
                        passed, the HTML string in the first argument must
                        represent a a simple element with no attributes.
                        <strong>As of jQuery 1.4</strong>, any
                        <a href="/category/events/" src="null">event type</a>
                        can be passed in, and the following jQuery methods can
                        be called:
                        <a href="/val/" src="null">val</a>,
                        <a href="/css/" src="null">css</a>,
                        <a href="/html/" src="null">html</a>,
                        <a href="/text/" src="null">text</a>,
                        <a href="/data/" src="null">data</a>,
                        <a href="/width/" src="null">width</a>,
                        <a href="/height/" src="null">height</a>, or
                        <a href="/offset/" src="null">offset</a>.
                      </p>
                      <p>
                        <strong>As of jQuery 1.8</strong>, any jQuery instance
                        method (a method of <code>jQuery.fn</code>) can be used
                        as a property of the object passed to the second
                        parameter:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>

                                <div class="line n3">
                                  3
                                </div>

                                <div class="line n4">
                                  4
                                </div>

                                <div class="line n5">
                                  5
                                </div>

                                <div class="line n6">
                                  6
                                </div>

                                <div class="line n7">
                                  7
                                </div>

                                <div class="line n8">
                                  8
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;div&gt;&lt;/div&gt;"</span>, {</code></div></div><div class="container"><div class="line"><code>  <span class="string">"class"</span>: <span class="string">"my-div"</span>,</code></div></div><div class="container"><div class="line"><code>  on: {</code></div></div><div class="container"><div class="line"><code>    touchstart: <span class="keyword">function</span>( event ) {</code></div></div><div class="container"><div class="line"><code>      <span class="comment">// Do something</span></code></div></div><div class="container"><div class="line"><code>    }</code></div></div><div class="container"><div class="line"><code>  }</code></div></div><div class="container"><div class="line"><code>}).appendTo( <span class="string">"body"</span> );</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <p>
                        The name
                        <code>"class"</code> must be quoted in the object since
                        it is a JavaScript reserved word, and
                        <code>"className"</code> cannot be used since it refers
                        to the DOM property, not the attribute.
                      </p>
                      <p>
                        While the second argument is convenient, its flexibility
                        can lead to unintended consequences (e.g.
                        <code>$( "&lt;input&gt;", {size: "4"} )</code>
                        calling the
                        <code>.size()</code> method instead of setting the size
                        attribute). The previous code block could thus be
                        written instead as:
                      </p>
                      <div class="syntaxhighlighter javascript nogutter">
                        <table>
                          <tbody>
                            <tr>
                              <td class="gutter">
                                <div class="line n1">
                                  1
                                </div>

                                <div class="line n2">
                                  2
                                </div>

                                <div class="line n3">
                                  3
                                </div>

                                <div class="line n4">
                                  4
                                </div>

                                <div class="line n5">
                                  5
                                </div>

                                <div class="line n6">
                                  6
                                </div>

                                <div class="line n7">
                                  7
                                </div>

                                <div class="line n8">
                                  8
                                </div>
                              </td>
                              <td class="code">
                                <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;div&gt;&lt;/div&gt;"</span> )</code></div></div><div class="container"><div class="line"><code>  .addClass( <span class="string">"my-div"</span> )</code></div></div><div class="container"><div class="line"><code>  .on({</code></div></div><div class="container"><div class="line"><code>    touchstart: <span class="keyword">function</span>( event ) {</code></div></div><div class="container"><div class="line"><code>      <span class="comment">// Do something</span></code></div></div><div class="container"><div class="line"><code>    }</code></div></div><div class="container"><div class="line"><code>  })</code></div></div><div class="container"><div class="line"><code>    .appendTo( <span class="string">"body"</span> );</code></div></div></pre>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                    <section class="entry-examples" id="entry-examples-1">
                      <header><h2>Examples:</h2></header>
                      <div class="entry-example" id="example-1-0">
                        <h4>
                          Example:
                          <span class="desc"
                            >Create a div element (and all of its contents)
                            dynamically and append it to the body element.
                            Internally, an element is created and its innerHTML
                            property set to the given markup.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;div&gt;&lt;p&gt;Hello&lt;/p&gt;&lt;/div&gt;"</span> ).appendTo( <span class="string">"body"</span> )</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div class="entry-example" id="example-1-1">
                        <h4>
                          Example:
                          <span class="desc">Create some DOM elements.</span>
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>

                                  <div class="line n2">
                                    2
                                  </div>

                                  <div class="line n3">
                                    3
                                  </div>

                                  <div class="line n4">
                                    4
                                  </div>

                                  <div class="line n5">
                                    5
                                  </div>

                                  <div class="line n6">
                                    6
                                  </div>

                                  <div class="line n7">
                                    7
                                  </div>

                                  <div class="line n8">
                                    8
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$( <span class="string">"&lt;div/&gt;"</span>, {</code></div></div><div class="container"><div class="line"><code>  <span class="string">"class"</span>: <span class="string">"test"</span>,</code></div></div><div class="container"><div class="line"><code>  text: <span class="string">"Click me!"</span>,</code></div></div><div class="container"><div class="line"><code>  click: <span class="keyword">function</span>() {</code></div></div><div class="container"><div class="line"><code>    $( <span class="keyword">this</span> ).toggleClass( <span class="string">"test"</span> );</code></div></div><div class="container"><div class="line"><code>  }</code></div></div><div class="container"><div class="line"><code>})</code></div></div><div class="container"><div class="line"><code>  .appendTo( <span class="string">"body"</span> );</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </section>
                  </div>
                </article>
                <article id="jQuery3" class="entry method">
                  <h2 class="section-title">
                    <span class="name">jQuery( callback )</span
                    ><span class="returns"
                      >Returns:
                      <a href="http://api.jquery.com/Types/#jQuery" src="null"
                        >jQuery</a
                      ></span
                    >
                  </h2>
                  <div class="entry-wrapper">
                    <p class="desc">
                      <strong>Description: </strong>Binds a function to be
                      executed when the DOM has finished loading.
                    </p>
                    <ul class="signatures">
                      <li class="signature">
                        <h4 class="name">
                          <span class="version-details"
                            >version added:
                            <a href="/category/version/1.0/" src="null"
                              >1.0</a
                            ></span
                          ><a
                            id="jQuery-callback"
                            href="#jQuery-callback"
                            src="null"
                            ><span class="icon-link"></span>jQuery( callback
                            )</a
                          >
                        </h4>
                        <ul>
                          <li>
                            <div>
                              <strong>callback</strong>
                            </div>
                            <div>
                              Type:
                              <a
                                href="http://api.jquery.com/Types/#Function"
                                src="null"
                                >Function</a
                              >()
                            </div>
                            <div>
                              The function to execute when the DOM is ready.
                            </div>
                          </li>
                        </ul>
                      </li>
                    </ul>
                    <div class="longdesc" id="entry-longdesc-2">
                      <p>
                        This function behaves just like
                        <code>$( document ).ready()</code>, in that it should be
                        used to wrap other <code>$()</code> operations on your
                        page that depend on the DOM being ready. While this
                        function is, technically, chainable, there really isn"t
                        much use for chaining against it.
                      </p>
                    </div>
                    <section class="entry-examples" id="entry-examples-2">
                      <header><h2>Examples:</h2></header>
                      <div class="entry-example" id="example-2-0">
                        <h4>
                          Example:
                          <span class="desc"
                            >Execute the function when the DOM is ready to be
                            used.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>

                                  <div class="line n2">
                                    2
                                  </div>

                                  <div class="line n3">
                                    3
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>$(<span class="keyword">function</span>() {</code></div></div><div class="container"><div class="line"><code>  <span class="comment">// Document is ready</span></code></div></div><div class="container"><div class="line"><code>});</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <div class="entry-example" id="example-2-1">
                        <h4>
                          Example:
                          <span class="desc"
                            >Use both the shortcut for $(document).ready() and
                            the argument to write failsafe jQuery code using the
                            $ alias, without relying on the global alias.</span
                          >
                        </h4>
                        <div class="syntaxhighlighter javascript">
                          <table>
                            <tbody>
                              <tr>
                                <td class="gutter">
                                  <div class="line n1">
                                    1
                                  </div>

                                  <div class="line n2">
                                    2
                                  </div>

                                  <div class="line n3">
                                    3
                                  </div>
                                </td>
                                <td class="code">
                                  <pre><div class="container"><div class="line"><code>jQuery(<span class="keyword">function</span>( $ ) {</code></div></div><div class="container"><div class="line"><code>  <span class="comment">// Your code using failsafe $ alias here...</span></code></div></div><div class="container"><div class="line"><code>});</code></div></div></pre>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </section>
                  </div>
                </article>
              </div>
              <!-- .entry-content -->
            </article>
            <!-- #post-339 -->
          </div>

          <div id="sidebar" class="widget-area" role="complementary">
            <aside id="categories" class="widget">
              <ul>
                <li class="cat-item cat-item-1">
                  <a
                    href="http://api.jquery.com/category/ajax/"
                    title="View all posts filed under Ajax"
                    src="null"
                    >Ajax</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-2">
                      <a
                        href="http://api.jquery.com/category/ajax/global-ajax-event-handlers/"
                        title="View all posts filed under Global Ajax Event Handlers"
                        src="null"
                        >Global Ajax Event Handlers</a
                      >
                    </li>
                    <li class="cat-item cat-item-3">
                      <a
                        href="http://api.jquery.com/category/ajax/helper-functions/"
                        title="View all posts filed under Helper Functions"
                        src="null"
                        >Helper Functions</a
                      >
                    </li>
                    <li class="cat-item cat-item-4">
                      <a
                        href="http://api.jquery.com/category/ajax/low-level-interface/"
                        title="View all posts filed under Low-Level Interface"
                        src="null"
                        >Low-Level Interface</a
                      >
                    </li>
                    <li class="cat-item cat-item-5">
                      <a
                        href="http://api.jquery.com/category/ajax/shorthand-methods/"
                        title="View all posts filed under Shorthand Methods"
                        src="null"
                        >Shorthand Methods</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-6">
                  <a
                    href="http://api.jquery.com/category/attributes/"
                    title="View all posts filed under Attributes"
                    src="null"
                    >Attributes</a
                  >
                </li>
                <li class="cat-item cat-item-7">
                  <a
                    href="http://api.jquery.com/category/callbacks-object/"
                    title="View all posts filed under Callbacks Object"
                    src="null"
                    >Callbacks Object</a
                  >
                </li>
                <li class="cat-item cat-item-8 current-cat">
                  <a
                    href="http://api.jquery.com/category/core/"
                    title="View all posts filed under Core"
                    src="null"
                    >Core</a
                  >
                </li>
                <li class="cat-item cat-item-9">
                  <a
                    href="http://api.jquery.com/category/css/"
                    title="View all posts filed under CSS"
                    src="null"
                    >CSS</a
                  >
                </li>
                <li class="cat-item cat-item-10">
                  <a
                    href="http://api.jquery.com/category/data/"
                    title="View all posts filed under Data"
                    src="null"
                    >Data</a
                  >
                </li>
                <li class="cat-item cat-item-11">
                  <a
                    href="http://api.jquery.com/category/deferred-object/"
                    title="View all posts filed under Deferred Object"
                    src="null"
                    >Deferred Object</a
                  >
                </li>
                <li class="cat-item cat-item-87">
                  <a
                    href="http://api.jquery.com/category/deprecated/"
                    title="View all posts filed under Deprecated"
                    src="null"
                    >Deprecated</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-93">
                      <a
                        href="http://api.jquery.com/category/deprecated/deprecated-1.10/"
                        title="View all posts filed under Deprecated 1.10"
                        src="null"
                        >Deprecated 1.10</a
                      >
                    </li>
                    <li class="cat-item cat-item-90">
                      <a
                        href="http://api.jquery.com/category/deprecated/deprecated-1.3/"
                        title="View all posts filed under Deprecated 1.3"
                        src="null"
                        >Deprecated 1.3</a
                      >
                    </li>
                    <li class="cat-item cat-item-88">
                      <a
                        href="http://api.jquery.com/category/deprecated/deprecated-1.7/"
                        title="View all posts filed under Deprecated 1.7"
                        src="null"
                        >Deprecated 1.7</a
                      >
                    </li>
                    <li class="cat-item cat-item-89">
                      <a
                        href="http://api.jquery.com/category/deprecated/deprecated-1.8/"
                        title="View all posts filed under Deprecated 1.8"
                        src="null"
                        >Deprecated 1.8</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-12">
                  <a
                    href="http://api.jquery.com/category/dimensions/"
                    title="View all posts filed under Dimensions"
                    src="null"
                    >Dimensions</a
                  >
                </li>
                <li class="cat-item cat-item-13">
                  <a
                    href="http://api.jquery.com/category/effects/"
                    title="View all posts filed under Effects"
                    src="null"
                    >Effects</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-14">
                      <a
                        href="http://api.jquery.com/category/effects/basics/"
                        title="View all posts filed under Basics"
                        src="null"
                        >Basics</a
                      >
                    </li>
                    <li class="cat-item cat-item-15">
                      <a
                        href="http://api.jquery.com/category/effects/custom-effects/"
                        title="View all posts filed under Custom"
                        src="null"
                        >Custom</a
                      >
                    </li>
                    <li class="cat-item cat-item-16">
                      <a
                        href="http://api.jquery.com/category/effects/fading/"
                        title="View all posts filed under Fading"
                        src="null"
                        >Fading</a
                      >
                    </li>
                    <li class="cat-item cat-item-17">
                      <a
                        href="http://api.jquery.com/category/effects/sliding/"
                        title="View all posts filed under Sliding"
                        src="null"
                        >Sliding</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-18">
                  <a
                    href="http://api.jquery.com/category/events/"
                    title="View all posts filed under Events"
                    src="null"
                    >Events</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-19">
                      <a
                        href="http://api.jquery.com/category/events/browser-events/"
                        title="View all posts filed under Browser Events"
                        src="null"
                        >Browser Events</a
                      >
                    </li>
                    <li class="cat-item cat-item-20">
                      <a
                        href="http://api.jquery.com/category/events/document-loading/"
                        title="View all posts filed under Document Loading"
                        src="null"
                        >Document Loading</a
                      >
                    </li>
                    <li class="cat-item cat-item-21">
                      <a
                        href="http://api.jquery.com/category/events/event-handler-attachment/"
                        title="View all posts filed under Event Handler Attachment"
                        src="null"
                        >Event Handler Attachment</a
                      >
                    </li>
                    <li class="cat-item cat-item-22">
                      <a
                        href="http://api.jquery.com/category/events/event-object/"
                        title="View all posts filed under Event Object"
                        src="null"
                        >Event Object</a
                      >
                    </li>
                    <li class="cat-item cat-item-23">
                      <a
                        href="http://api.jquery.com/category/events/form-events/"
                        title="View all posts filed under Form Events"
                        src="null"
                        >Form Events</a
                      >
                    </li>
                    <li class="cat-item cat-item-24">
                      <a
                        href="http://api.jquery.com/category/events/keyboard-events/"
                        title="View all posts filed under Keyboard Events"
                        src="null"
                        >Keyboard Events</a
                      >
                    </li>
                    <li class="cat-item cat-item-25">
                      <a
                        href="http://api.jquery.com/category/events/mouse-events/"
                        title="View all posts filed under Mouse Events"
                        src="null"
                        >Mouse Events</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-26">
                  <a
                    href="http://api.jquery.com/category/forms/"
                    title="View all posts filed under Forms"
                    src="null"
                    >Forms</a
                  >
                </li>
                <li class="cat-item cat-item-27">
                  <a
                    href="http://api.jquery.com/category/internals/"
                    title="View all posts filed under Internals"
                    src="null"
                    >Internals</a
                  >
                </li>
                <li class="cat-item cat-item-28">
                  <a
                    href="http://api.jquery.com/category/manipulation/"
                    title="View all posts filed under Manipulation"
                    src="null"
                    >Manipulation</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-29">
                      <a
                        href="http://api.jquery.com/category/manipulation/class-attribute/"
                        title="View all posts filed under Class Attribute"
                        src="null"
                        >Class Attribute</a
                      >
                    </li>
                    <li class="cat-item cat-item-30">
                      <a
                        href="http://api.jquery.com/category/manipulation/copying/"
                        title="View all posts filed under Copying"
                        src="null"
                        >Copying</a
                      >
                    </li>
                    <li class="cat-item cat-item-32">
                      <a
                        href="http://api.jquery.com/category/manipulation/dom-insertion-around/"
                        title="View all posts filed under DOM Insertion, Around"
                        src="null"
                        >DOM Insertion, Around</a
                      >
                    </li>
                    <li class="cat-item cat-item-33">
                      <a
                        href="http://api.jquery.com/category/manipulation/dom-insertion-inside/"
                        title="View all posts filed under DOM Insertion, Inside"
                        src="null"
                        >DOM Insertion, Inside</a
                      >
                    </li>
                    <li class="cat-item cat-item-34">
                      <a
                        href="http://api.jquery.com/category/manipulation/dom-insertion-outside/"
                        title="View all posts filed under DOM Insertion, Outside"
                        src="null"
                        >DOM Insertion, Outside</a
                      >
                    </li>
                    <li class="cat-item cat-item-35">
                      <a
                        href="http://api.jquery.com/category/manipulation/dom-removal/"
                        title="View all posts filed under DOM Removal"
                        src="null"
                        >DOM Removal</a
                      >
                    </li>
                    <li class="cat-item cat-item-36">
                      <a
                        href="http://api.jquery.com/category/manipulation/dom-replacement/"
                        title="View all posts filed under DOM Replacement"
                        src="null"
                        >DOM Replacement</a
                      >
                    </li>
                    <li class="cat-item cat-item-37">
                      <a
                        href="http://api.jquery.com/category/manipulation/general-attributes/"
                        title="View all posts filed under General Attributes"
                        src="null"
                        >General Attributes</a
                      >
                    </li>
                    <li class="cat-item cat-item-38">
                      <a
                        href="http://api.jquery.com/category/manipulation/style-properties/"
                        title="View all posts filed under Style Properties"
                        src="null"
                        >Style Properties</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-39">
                  <a
                    href="http://api.jquery.com/category/miscellaneous/"
                    title="View all posts filed under Miscellaneous"
                    src="null"
                    >Miscellaneous</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-40">
                      <a
                        href="http://api.jquery.com/category/miscellaneous/collection-manipulation/"
                        title="View all posts filed under Collection Manipulation"
                        src="null"
                        >Collection Manipulation</a
                      >
                    </li>
                    <li class="cat-item cat-item-41">
                      <a
                        href="http://api.jquery.com/category/miscellaneous/data-vault/"
                        title="View all posts filed under Data Storage"
                        src="null"
                        >Data Storage</a
                      >
                    </li>
                    <li class="cat-item cat-item-42">
                      <a
                        href="http://api.jquery.com/category/miscellaneous/dom-element-methods/"
                        title="View all posts filed under DOM Element Methods"
                        src="null"
                        >DOM Element Methods</a
                      >
                    </li>
                    <li class="cat-item cat-item-43">
                      <a
                        href="http://api.jquery.com/category/miscellaneous/setup-methods/"
                        title="View all posts filed under Setup Methods"
                        src="null"
                        >Setup Methods</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-44">
                  <a
                    href="http://api.jquery.com/category/offset/"
                    title="View all posts filed under Offset"
                    src="null"
                    >Offset</a
                  >
                </li>
                <li class="cat-item cat-item-45">
                  <a
                    href="http://api.jquery.com/category/properties/"
                    title="View all posts filed under Properties"
                    src="null"
                    >Properties</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-46">
                      <a
                        href="http://api.jquery.com/category/properties/jquery-object-instance-properties/"
                        title="View all posts filed under Properties of jQuery Object Instances"
                        src="null"
                        >Properties of jQuery Object Instances</a
                      >
                    </li>
                    <li class="cat-item cat-item-47">
                      <a
                        href="http://api.jquery.com/category/properties/global-jquery-object-properties/"
                        title="View all posts filed under Properties of the Global jQuery Object"
                        src="null"
                        >Properties of the Global jQuery Object</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-92">
                  <a
                    href="http://api.jquery.com/category/removed/"
                    title="View all posts filed under Removed"
                    src="null"
                    >Removed</a
                  >
                </li>
                <li class="cat-item cat-item-48">
                  <a
                    href="http://api.jquery.com/category/selectors/"
                    title="View all posts filed under Selectors"
                    src="null"
                    >Selectors</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-49">
                      <a
                        href="http://api.jquery.com/category/selectors/attribute-selectors/"
                        title="View all posts filed under Attribute"
                        src="null"
                        >Attribute</a
                      >
                    </li>
                    <li class="cat-item cat-item-50">
                      <a
                        href="http://api.jquery.com/category/selectors/basic-css-selectors/"
                        title="View all posts filed under Basic"
                        src="null"
                        >Basic</a
                      >
                    </li>
                    <li class="cat-item cat-item-51">
                      <a
                        href="http://api.jquery.com/category/selectors/basic-filter-selectors/"
                        title="View all posts filed under Basic Filter"
                        src="null"
                        >Basic Filter</a
                      >
                    </li>
                    <li class="cat-item cat-item-52">
                      <a
                        href="http://api.jquery.com/category/selectors/child-filter-selectors/"
                        title="View all posts filed under Child Filter"
                        src="null"
                        >Child Filter</a
                      >
                    </li>
                    <li class="cat-item cat-item-53">
                      <a
                        href="http://api.jquery.com/category/selectors/content-filter-selector/"
                        title="View all posts filed under Content Filter"
                        src="null"
                        >Content Filter</a
                      >
                    </li>
                    <li class="cat-item cat-item-54">
                      <a
                        href="http://api.jquery.com/category/selectors/form-selectors/"
                        title="View all posts filed under Form"
                        src="null"
                        >Form</a
                      >
                    </li>
                    <li class="cat-item cat-item-55">
                      <a
                        href="http://api.jquery.com/category/selectors/hierarchy-selectors/"
                        title="View all posts filed under Hierarchy"
                        src="null"
                        >Hierarchy</a
                      >
                    </li>
                    <li class="cat-item cat-item-56">
                      <a
                        href="http://api.jquery.com/category/selectors/jquery-selector-extensions/"
                        title="View all posts filed under jQuery Extensions"
                        src="null"
                        >jQuery Extensions</a
                      >
                    </li>
                    <li class="cat-item cat-item-57">
                      <a
                        href="http://api.jquery.com/category/selectors/visibility-filter-selectors/"
                        title="View all posts filed under Visibility Filter"
                        src="null"
                        >Visibility Filter</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-58">
                  <a
                    href="http://api.jquery.com/category/traversing/"
                    title="View all posts filed under Traversing"
                    src="null"
                    >Traversing</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-59">
                      <a
                        href="http://api.jquery.com/category/traversing/filtering/"
                        title="View all posts filed under Filtering"
                        src="null"
                        >Filtering</a
                      >
                    </li>
                    <li class="cat-item cat-item-60">
                      <a
                        href="http://api.jquery.com/category/traversing/miscellaneous-traversal/"
                        title="View all posts filed under Miscellaneous Traversing"
                        src="null"
                        >Miscellaneous Traversing</a
                      >
                    </li>
                    <li class="cat-item cat-item-61">
                      <a
                        href="http://api.jquery.com/category/traversing/tree-traversal/"
                        title="View all posts filed under Tree Traversal"
                        src="null"
                        >Tree Traversal</a
                      >
                    </li>
                  </ul>
                </li>
                <li class="cat-item cat-item-63">
                  <a
                    href="http://api.jquery.com/category/utilities/"
                    title="View all posts filed under Utilities"
                    src="null"
                    >Utilities</a
                  >
                </li>
                <li class="cat-item cat-item-64">
                  <a
                    href="http://api.jquery.com/category/version/"
                    title="View all posts filed under Version"
                    src="null"
                    >Version</a
                  >
                  <ul class="children">
                    <li class="cat-item cat-item-65">
                      <a
                        href="http://api.jquery.com/category/version/1.0/"
                        title="View all posts filed under Version 1.0"
                        src="null"
                        >Version 1.0</a
                      >
                    </li>
                    <li class="cat-item cat-item-66">
                      <a
                        href="http://api.jquery.com/category/version/1.0.4/"
                        title="View all posts filed under Version 1.0.4"
                        src="null"
                        >Version 1.0.4</a
                      >
                    </li>
                    <li class="cat-item cat-item-67">
                      <a
                        href="http://api.jquery.com/category/version/1.1/"
                        title="View all posts filed under Version 1.1"
                        src="null"
                        >Version 1.1</a
                      >
                    </li>
                    <li class="cat-item cat-item-68">
                      <a
                        href="http://api.jquery.com/category/version/1.1.2/"
                        title="View all posts filed under Version 1.1.2"
                        src="null"
                        >Version 1.1.2</a
                      >
                    </li>
                    <li class="cat-item cat-item-69">
                      <a
                        href="http://api.jquery.com/category/version/1.1.3/"
                        title="View all posts filed under Version 1.1.3"
                        src="null"
                        >Version 1.1.3</a
                      >
                    </li>
                    <li class="cat-item cat-item-70">
                      <a
                        href="http://api.jquery.com/category/version/1.1.4/"
                        title="View all posts filed under Version 1.1.4"
                        src="null"
                        >Version 1.1.4</a
                      >
                    </li>
                    <li class="cat-item cat-item-71">
                      <a
                        href="http://api.jquery.com/category/version/1.2/"
                        title="View all posts filed under Version 1.2"
                        src="null"
                        >Version 1.2</a
                      >
                    </li>
                    <li class="cat-item cat-item-72">
                      <a
                        href="http://api.jquery.com/category/version/1.2.3/"
                        title="View all posts filed under Version 1.2.3"
                        src="null"
                        >Version 1.2.3</a
                      >
                    </li>
                    <li class="cat-item cat-item-73">
                      <a
                        href="http://api.jquery.com/category/version/1.2.6/"
                        title="View all posts filed under Version 1.2.6"
                        src="null"
                        >Version 1.2.6</a
                      >
                    </li>
                    <li class="cat-item cat-item-74">
                      <a
                        href="http://api.jquery.com/category/version/1.3/"
                        title="View all posts filed under Version 1.3"
                        src="null"
                        >Version 1.3</a
                      >
                    </li>
                    <li class="cat-item cat-item-75">
                      <a
                        href="http://api.jquery.com/category/version/1.4/"
                        title="View all posts filed under Version 1.4"
                        src="null"
                        >Version 1.4</a
                      >
                    </li>
                    <li class="cat-item cat-item-76">
                      <a
                        href="http://api.jquery.com/category/version/1.4.1/"
                        title="View all posts filed under Version 1.4.1"
                        src="null"
                        >Version 1.4.1</a
                      >
                    </li>
                    <li class="cat-item cat-item-77">
                      <a
                        href="http://api.jquery.com/category/version/1.4.2/"
                        title="View all posts filed under Version 1.4.2"
                        src="null"
                        >Version 1.4.2</a
                      >
                    </li>
                    <li class="cat-item cat-item-78">
                      <a
                        href="http://api.jquery.com/category/version/1.4.3/"
                        title="View all posts filed under Version 1.4.3"
                        src="null"
                        >Version 1.4.3</a
                      >
                    </li>
                    <li class="cat-item cat-item-79">
                      <a
                        href="http://api.jquery.com/category/version/1.4.4/"
                        title="View all posts filed under Version 1.4.4"
                        src="null"
                        >Version 1.4.4</a
                      >
                    </li>
                    <li class="cat-item cat-item-80">
                      <a
                        href="http://api.jquery.com/category/version/1.5/"
                        title="View all posts filed under Version 1.5"
                        src="null"
                        >Version 1.5</a
                      >
                    </li>
                    <li class="cat-item cat-item-81">
                      <a
                        href="http://api.jquery.com/category/version/1.5.1/"
                        title="View all posts filed under Version 1.5.1"
                        src="null"
                        >Version 1.5.1</a
                      >
                    </li>
                    <li class="cat-item cat-item-82">
                      <a
                        href="http://api.jquery.com/category/version/1.6/"
                        title="View all posts filed under Version 1.6"
                        src="null"
                        >Version 1.6</a
                      >
                    </li>
                    <li class="cat-item cat-item-83">
                      <a
                        href="http://api.jquery.com/category/version/1.7/"
                        title="View all posts filed under Version 1.7"
                        src="null"
                        >Version 1.7</a
                      >
                    </li>
                    <li class="cat-item cat-item-84">
                      <a
                        href="http://api.jquery.com/category/version/1.8/"
                        title="View all posts filed under Version 1.8"
                        src="null"
                        >Version 1.8</a
                      >
                    </li>
                    <li class="cat-item cat-item-86">
                      <a
                        href="http://api.jquery.com/category/version/1.9/"
                        title="View all posts filed under Version 1.9"
                        src="null"
                        >Version 1.9</a
                      >
                    </li>
                  </ul>
                </li>
              </ul>
            </aside>
          </div>
        </div>
      </div>
    </div>

    <footer class="clearfix simple">
      <div class="constrain">
        <div class="row">
          <div class="eight columns">
            <h3><span>Quick Access</span></h3>
            <div class="cdn">
              <strong>CDN</strong>
              <input
                value="//code.jquery.com/jquery-1.10.2.min.js"
                readonly=""
              />
            </div>
            <div class="download">
              <strong
                ><a href="http://jquery.com/download/" src="null"
                  >Download jQuery 1.10.2 →</a
                ></strong
              >
            </div>
            <div class="tinynav-container">
              <h3><span>More jQuery Sites</span></h3>
              <select id="tinynav1" class="tinynav tinynav1"
                ><option>Browse...</option
                ><option value="http://plugins.jquery.com/">Plugins</option
                ><option value="http://contribute.jquery.org/"
                  >Contribute</option
                ><option value="http://contribute.jquery.org/cla/">- CLA</option
                ><option value="http://contribute.jquery.org/style-guide/"
                  >- Style Guides</option
                ><option value="http://contribute.jquery.org/triage/"
                  >- Bug Triage</option
                ><option value="http://contribute.jquery.org/code/"
                  >- Code</option
                ><option value="http://contribute.jquery.org/documentation/"
                  >- Documentation</option
                ><option value="http://contribute.jquery.org/web-sites/"
                  >- Web Sites</option
                ><option value="http://events.jquery.org/">Events</option
                ><option
                  value="http://www.deque.com/deque-partners-jquery-create-accessibility-summit"
                  >- Oct 10-11 | jQuery Accessibility Summit</option
                ><option value="http://jquery.itmozg.ru/"
                  >- Oct 15 | jQuery Russia</option
                ><option
                  value="http://modernweb.com/training/jquery-oct-2013.php"
                  >- Oct 15-17 | jQuery Virtual Training</option
                ><option value="http://2013.cssdevconf.com/"
                  >- Oct 21-22 | CSS Dev Conf</option
                ><option value="http://javascriptsummit.com/"
                  >- Nov 19-21 | JavaScript Summit</option
                ><option value="http://events.jquery.org/2014/san-diego/"
                  >- Feb 12-13 | jQuery San Diego</option
                ><option value="http://www.gentics.com/jquery-europe"
                  >- Feb 28-Mar 1 | jQuery Europe</option
                ><option value="http://jqueryuk.com"
                  >- May 16 | jQuery UK</option
                ><option value="https://jquery.org/support/">Support</option
                ><option value="http://learn.jquery.com/"
                  >- Learning Center</option
                ><option value="http://try.jquery.com/">- Try jQuery</option
                ><option value="http://irc.jquery.org/">- IRC/Chat</option
                ><option value="http://forum.jquery.com/">- Forums</option
                ><option value="http://stackoverflow.com/tags/jquery/info"
                  >- Stack Overflow</option
                ><option value="https://jquery.org/support/"
                  >- Commercial Support</option
                ><option value="https://jquery.org/">jQuery Foundation</option
                ><option value="https://jquery.org/join/">- Join</option
                ><option value="https://jquery.org/members/">- Members</option
                ><option value="https://jquery.org/team/">- Team</option
                ><option value="http://brand.jquery.org/">- Brand Guide</option
                ><option value="https://jquery.org/donate/"
                  >- Donate</option
                ></select
              >
            </div>
            <ul class="footer-icon-links">
              <li>
                <a
                  class="icon-github"
                  href="http://github.com/jquery/jquery"
                  src="null"
                  >GitHub <small>jQuery <br />Source</small></a
                >
              </li>
              <li>
                <a class="icon-group" href="http://forum.jquery.com" src="null"
                  >Forum <small>Community <br />Support</small></a
                >
              </li>
              <li>
                <a
                  class="icon-warning-sign"
                  href="http://bugs.jquery.com"
                  src="null"
                  >Bugs <small>Issue <br />Tracker</small></a
                >
              </li>
            </ul>
          </div>

          <div class="four columns">
            <h3><span>Books</span></h3>
            <ul class="books">
              <li>
                <a
                  href="http://www.packtpub.com/learning-jquery-with-simple-javascript-techniques-fourth-edition/book"
                  src="null"
                >
                  <span class="bottom"
                    ><img
                      src="null"
                      alt="Learning jQuery 4th Edition by Karl Swedberg and Jonathan Chaffer"
                      width="92"
                      height="114"
                  /></span>
                  <strong>Learning jQuery Fourth Edition</strong><br />
                  <cite>Karl Swedberg and Jonathan Chaffer</cite>
                </a>
              </li>
              <li>
                <a
                  href="http://www.manning.com/affiliate/idevaffiliate.php?id=648_176"
                  src="null"
                >
                  <span
                    ><img
                      src="null"
                      alt="jQuery in Action by Bear Bibeault and Yehuda Katz"
                      width="92"
                      height="114"
                  /></span>
                  <strong>jQuery in Action</strong><br />
                  <cite>Bear Bibeault and Yehuda Katz</cite>
                </a>
              </li>
              <li>
                <a
                  href="http://www.syncfusion.com/resources/techportal/ebooks/jquery?utm_medium=BizDev-jQuery.org0513"
                  src="null"
                >
                  <span
                    ><img
                      src="null"
                      alt="jQuery Succinctly by Cody Lindley"
                      width="92"
                      height="114"
                  /></span>
                  <strong>jQuery Succinctly</strong><br />
                  <cite>Cody Lindley</cite>
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div id="legal">
          <ul class="footer-site-links">
            <li>
              <a class="icon-pencil" href="http://learn.jquery.com/" src="null"
                >Learning Center</a
              >
            </li>
            <li>
              <a class="icon-group" href="http://forum.jquery.com/" src="null"
                >Forum</a
              >
            </li>
            <li>
              <a class="icon-wrench" href="http://api.jquery.com/" src="null"
                >API</a
              >
            </li>
            <li>
              <a
                class="icon-twitter"
                href="http://twitter.com/jquery"
                src="null"
                >Twitter</a
              >
            </li>
            <li>
              <a class="icon-comments" href="http://irc.jquery.org/" src="null"
                >IRC</a
              >
            </li>
          </ul>
          <p class="copyright">
            Copyright 2013
            <a href="https://jquery.org/team/" src="null"
              >The jQuery Foundation</a
            >.<br />
            <span class="sponsor-line"
              ><a
                href="http://mediatemple.net"
                rel="noindex,nofollow"
                class="mt-link"
                src="null"
                >Web hosting by Media Temple</a
              >
              |
              <a
                href="http://www.maxcdn.com"
                rel="noindex,nofollow"
                class="mc-link"
                src="null"
                >CDN by MaxCDN</a
              >
              |
              <a href="http://wordpress.org/" class="wp-link" src="null"
                >Powered by WordPress</a
              >
              | Thanks:
              <a href="https://jquery.org/members/" src="null">Members</a>,
              <a href="https://jquery.org/sponsors/" src="null"
                >Sponsors</a
              ></span
            >
          </p>
        </div>
      </div>
    </footer>

    <script>
      // biome-ignore lint/correctness/noInvalidUseBeforeDeclaration: Vendor script
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-1076265-1']);
      _gaq.push(['_setDomainName', 'api.jquery.com']);
      _gaq.push(['_setAllowLinker', true]);
      _gaq.push(['_trackPageview']);

      (() => {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src =
          `${document.location.protocol === 'https:' 
            ? 'https://ssl'
            : 'http://www'}.google-analytics.com/ga.js`;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
      })();
    </script>

    <div id="cboxOverlay" style="display: none;"></div>
    <div id="colorbox" class="" style="display: none;">
      <div id="cboxWrapper">
        <div>
          <div id="cboxTopLeft" style="float: left;"></div>
          <div id="cboxTopCenter" style="float: left;"></div>
          <div id="cboxTopRight" style="float: left;"></div>
        </div>
        <div style="clear: left;">
          <div id="cboxMiddleLeft" style="float: left;"></div>
          <div id="cboxContent" style="float: left;">
            <div
              id="cboxLoadedContent"
              style="width: 0px; height: 0px; overflow: hidden; float: left;"
            ></div>
            <div id="cboxTitle" style="float: left;"></div>
            <div id="cboxCurrent" style="float: left;"></div>
            <div id="cboxNext" style="float: left;"></div>
            <div id="cboxPrevious" style="float: left;"></div>
            <div id="cboxSlideshow" style="float: left;"></div>
            <div id="cboxClose" style="float: left;"></div>
          </div>
          <div id="cboxMiddleRight" style="float: left;"></div>
        </div>
        <div style="clear: left;">
          <div id="cboxBottomLeft" style="float: left;"></div>
          <div id="cboxBottomCenter" style="float: left;"></div>
          <div id="cboxBottomRight" style="float: left;"></div>
        </div>
      </div>
      <div
        style="
          position: absolute;
          width: 9999px;
          visibility: hidden;
          display: none;
        "
      ></div>
    </div>
  </body>
</html>
```

## File: `scripts/fetch-sponsors.mts`
```
/**
 * @file Script To fetch sponsor data from Open Collective and GitHub.
 *
 *   Adapted from
 *   https://github.com/eslint/website/blob/230e73457dcdc2353ad7934e876a5a222a17b1d7/_tools/fetch-sponsors.js.
 */
/* eslint-disable @typescript-eslint/no-unsafe-assignment,
                  @typescript-eslint/no-unsafe-return,
                  @typescript-eslint/no-unsafe-call,
                  @typescript-eslint/no-unsafe-argument,
                  @typescript-eslint/no-unsafe-member-access,
                  @typescript-eslint/prefer-nullish-coalescing */
import * as fs from 'node:fs/promises';
import ImgixClient from '@imgix/js-core';
import { graphql as githubGraphQL } from '@octokit/graphql';
import { request } from 'undici';

type Tier = 'headliner' | 'sponsor' | 'professional' | 'backer';

interface Sponsor {
  createdAt: string;
  name: string;
  image: string;
  url: string;
  type: 'ORGANIZATION' | 'INDIVIDUAL' | 'FUND';
  monthlyDonation: number;
  totalDonations: number;
  source: 'github' | 'opencollective' | 'manual';
  tier: Tier | null;
}

const tierSponsors: Record<Tier, Sponsor[]> = {
  headliner: [
    // Some sponsors are manually added here.
    {
      createdAt: '2022-06-24',
      name: 'Github',
      image: 'https://github.com/github.png',
      url: 'https://github.com/',
      type: 'ORGANIZATION',
      monthlyDonation: 0,
      totalDonations: 0,
      source: 'manual',
      tier: 'headliner',
    },
    {
      createdAt: '2018-05-02',
      name: 'AirBnB',
      image: 'https://github.com/airbnb.png',
      url: 'https://www.airbnb.com/',
      type: 'ORGANIZATION',
      monthlyDonation: 0,
      totalDonations: 0,
      source: 'manual',
      tier: 'headliner',
    },
    {
      createdAt: '2026-01-21',
      name: 'HasData',
      image: 'https://hasdata.com/favicon.svg',
      url: 'https://hasdata.com',
      type: 'ORGANIZATION',
      monthlyDonation: 0,
      totalDonations: 0,
      source: 'manual',
      tier: 'headliner',
    },
    {
      createdAt: '2026-01-28',
      name: 'context.dev',
      image: 'https://github.com/context-dot-dev.png',
      url: 'https://context.dev/',
      type: 'ORGANIZATION',
      monthlyDonation: 0,
      totalDonations: 0,
      source: 'manual',
      tier: 'headliner',
    },
  ],
  sponsor: [],
  professional: [],
  backer: [],
};

const { CHEERIO_SPONSORS_GITHUB_TOKEN, IMGIX_TOKEN } = process.env;

if (!CHEERIO_SPONSORS_GITHUB_TOKEN) {
  throw new Error('Missing CHEERIO_SPONSORS_GITHUB_TOKEN.');
}

// @ts-expect-error - Types don't have a constructor
const imgix = new ImgixClient({
  domain: 'humble.imgix.net',
  secureURLToken: IMGIX_TOKEN,
});

/**
 * Returns the tier ID for a given donation amount.
 *
 * @param monthlyDonation - The monthly donation in dollars.
 * @returns The ID of the tier the donation belongs to.
 */
function getTierSlug(monthlyDonation: number): Tier | null {
  if (monthlyDonation >= 250) {
    return 'headliner';
  }

  if (monthlyDonation >= 100) {
    return 'sponsor';
  }

  if (monthlyDonation >= 25) {
    return 'professional';
  }

  if (monthlyDonation >= 5) {
    return 'backer';
  }

  return null;
}

/**
 * Fetch order data from Open Collective using the GraphQL API.
 *
 * @returns An array of sponsors.
 */
async function fetchOpenCollectiveSponsors(): Promise<Sponsor[]> {
  const endpoint = 'https://api.opencollective.com/graphql/v2';

  const query = `{
        account(slug: "cheerio") {
          orders(status: ACTIVE, filter: INCOMING) {
            nodes {
              createdAt
              fromAccount {
                name
                website
                imageUrl
                type
              }
              amount {
                value
              }
              tier {
                slug
              }
              frequency
              totalDonations {
                value
              }
            }
          }
        }
      }`;

  const { body } = await request(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query }),
  });

  const payload: any = await body.json();

  return payload.data.account.orders.nodes.map((order: any): Sponsor => {
    const donation = order.amount.value * 100;
    const monthlyDonation =
      order.frequency === 'YEARLY' ? Math.round(donation / 12) : donation;

    return {
      createdAt: order.createdAt,
      name: order.fromAccount.name,
      url: order.fromAccount.website,
      image: order.fromAccount.imageUrl,
      type: order.fromAccount.type,
      monthlyDonation,
      totalDonations: order.totalDonations.value * 100,
      source: 'opencollective',
      tier: getTierSlug(monthlyDonation / 100),
    };
  });
}

function getMonthsActive(date: string): number {
  const now = new Date();
  const then = new Date(date);
  const months = (now.getFullYear() - then.getFullYear()) * 12;
  return months - then.getMonth() + now.getMonth() + 1;
}

/**
 * Fetches GitHub Sponsors data using the GraphQL API.
 *
 * @returns An array of sponsors.
 */
async function fetchGitHubSponsors(): Promise<Sponsor[]> {
  const { organization } = await githubGraphQL<any>(
    `{
      organization(login: "cheeriojs") {
        sponsorshipsAsMaintainer(first: 100) {
          nodes {
            sponsor: sponsorEntity {
              ... on User {
                name
                login
                avatarUrl
                url
                websiteUrl
                isViewer
              }
              ... on Organization {
                name
                login
                avatarUrl
                url
                websiteUrl
                viewerCanAdminister
              }
            }
            tier {
              monthlyPriceInDollars
            }
            createdAt
          }
        }
      }
    }
    `,
    {
      headers: {
        authorization: `token ${CHEERIO_SPONSORS_GITHUB_TOKEN}`,
      },
    },
  );

  // Return an array in the same format as Open Collective
  return organization.sponsorshipsAsMaintainer.nodes.map(
    ({ sponsor, tier, createdAt }: any): Sponsor => ({
      createdAt,
      name: sponsor.name,
      image: `${sponsor.avatarUrl}&s=128`,
      url: sponsor.websiteUrl || sponsor.url,
      type:
        // Workaround to get the type — fetch a field that only exists on users.
        sponsor.isViewer === undefined ? 'ORGANIZATION' : 'INDIVIDUAL',
      monthlyDonation: (tier?.monthlyPriceInDollars ?? 0) * 100,
      totalDonations:
        getMonthsActive(createdAt) * tier?.monthlyPriceInDollars * 100,
      source: 'github',
      tier: getTierSlug(tier?.monthlyPriceInDollars ?? 0),
    }),
  );
}

async function fetchSponsors(): Promise<Sponsor[]> {
  const results = await Promise.all([
    fetchOpenCollectiveSponsors(),
    fetchGitHubSponsors(),
  ]);

  return results.flat();
}

/*
 * Remove sponsors from lower tiers that have individual accounts,
 * but are clearly orgs.
 */
const MISLABELED_ORGS =
  /[ck]as[iy]+no|bet$|poker|gambling|coffee|tuxedo|(?:ph|f)oto/i;

const README_PATH = new URL('../Readme.md', import.meta.url);
const JSON_PATH = new URL('../website/sponsors.json', import.meta.url);

const SECTION_START_BEGINNING = '<!-- BEGIN SPONSORS:';
const SECTION_START_END = '-->';
const SECTION_END = '<!-- END SPONSORS -->';

const professionalToBackerOverrides = new Map([
  ['Vasy Kafidoff', 'https://kafidoff.com'],
]);

const sponsors = await fetchSponsors();

console.log('Received sponsors:', sponsors);

// Remove sponsors that are already in the pre-populated headliners
for (let i = 0; i < sponsors.length; i++) {
  if (
    tierSponsors.headliner.some((sponsor) => sponsor.url === sponsors[i].url)
  ) {
    sponsors.splice(i, 1);
    i--;
  }
}

sponsors.sort((a, b) => Date.parse(a.createdAt) - Date.parse(b.createdAt));

// Process into a useful format
for (const sponsor of sponsors) {
  if (
    !sponsor.tier || // Always skip if sponsor has no tier (e.g., donation < $5)
    // OR if it's a 'professional' or 'backer' tier AND meets specific filtering criteria
    ((sponsor.tier === 'professional' || sponsor.tier === 'backer') &&
      (sponsor.type === 'ORGANIZATION' ||
        MISLABELED_ORGS.test(sponsor.name) ||
        MISLABELED_ORGS.test(sponsor.url)))
  ) {
    continue;
  }

  if (
    (sponsor.tier === 'professional' || sponsor.tier === 'backer') &&
    professionalToBackerOverrides.has(sponsor.name)
  ) {
    sponsor.url = professionalToBackerOverrides.get(sponsor.name)!;
  }

  tierSponsors[sponsor.tier].push(sponsor);
}

for (const tier of Object.values(tierSponsors)) {
  // Sort order based on total donations
  tier.sort((a: Sponsor, b: Sponsor) => b.totalDonations - a.totalDonations);

  // Set all donations to 0 before writing to JSON
  for (const sponsor of tier) {
    sponsor.monthlyDonation = 0;
    sponsor.totalDonations = 0;
  }
}

// Write sponsors.json
await fs.writeFile(JSON_PATH, JSON.stringify(tierSponsors, null, 2), 'utf8');

// Prepend professionals to backers for now
tierSponsors.backer.unshift(...tierSponsors.professional);

let readme = await fs.readFile(README_PATH, 'utf8');

const TIER_IMAGE_SIZES: Record<Tier, number> = {
  headliner: 128,
  sponsor: 64,
  professional: 64,
  backer: 48,
};

for (let sectionStartIndex = 0; ; ) {
  sectionStartIndex = readme.indexOf(
    SECTION_START_BEGINNING,
    sectionStartIndex,
  );

  if (sectionStartIndex < 0) break;

  sectionStartIndex += SECTION_START_BEGINNING.length;

  const sectionStartEndIndex = readme.indexOf(
    SECTION_START_END,
    sectionStartIndex,
  );
  const sectionName = readme
    .slice(sectionStartIndex, sectionStartEndIndex)
    .trim() as Tier;

  const sectionContentStart = sectionStartEndIndex + SECTION_START_END.length;

  const sectionEndIndex = readme.indexOf(SECTION_END, sectionContentStart);

  readme = `${readme.slice(0, sectionContentStart)}\n\n${tierSponsors[
    sectionName
  ]
    .map((s: Sponsor) => {
      const size = TIER_IMAGE_SIZES[s.tier ?? sectionName];
      // Display each sponsor's image in the README.
      return `<a href="${s.url}" target="_blank" rel="noopener noreferrer">
            <img height="${size}px" width="${size}px" src="${imgix.buildURL(
              s.image,
              {
                w: size,
                h: size,
                fit: 'fillmax',
                fill: 'solid',
              },
            )}" title="${s.name}" alt="${s.name}"></img>
          </a>`;
    })
    .join('\n')}\n\n${readme.slice(sectionEndIndex)}`;
}

await fs.writeFile(README_PATH, readme, {
  encoding: 'utf8',
});
```

## File: `src/cheerio.spec.ts`
```typescript
import type { AnyNode, Element } from 'domhandler';
import { parseDOM } from 'htmlparser2';
import { describe, expect, it } from 'vitest';
import { cheerio, food, fruits, noscript } from './__fixtures__/fixtures.js';
import type { Cheerio } from './index.js';

declare module './index.js' {
  interface Cheerio<T> {
    myPlugin(...args: unknown[]): {
      context: Cheerio<T>;
      args: unknown[];
    };
    foo(this: void): void;
  }
}

function testAppleSelect($apple: ArrayLike<Element>) {
  expect($apple).toHaveLength(1);
  const apple = $apple[0];
  expect(apple.parentNode).toHaveProperty('tagName', 'ul');
  expect(apple.prev).toBe(null);
  expect((apple.next as Element).attribs).toHaveProperty('class', 'orange');
  expect(apple.childNodes).toHaveLength(1);
  expect(apple.childNodes[0]).toHaveProperty('data', 'Apple');
}

describe('cheerio', () => {
  it('cheerio(null) should be empty', () => {
    expect(cheerio(null as never)).toHaveLength(0);
  });

  it('cheerio(undefined) should be empty', () => {
    expect(cheerio(undefined)).toHaveLength(0);
  });

  it("cheerio('') should be empty", () => {
    expect(cheerio('')).toHaveLength(0);
  });

  it('cheerio(selector) with no context or root should be empty', () => {
    expect(cheerio('.h2')).toHaveLength(0);
    expect(cheerio('#fruits')).toHaveLength(0);
  });

  it('cheerio(node) : should override previously-loaded nodes', () => {
    const $ = cheerio.load('<div><span></span></div>');
    const spanNode = $('span')[0];
    const $span = $(spanNode);
    expect($span[0]).toBe(spanNode);
  });

  it('should be able to create html without a root or context', () => {
    const $h2 = cheerio('<h2>');
    expect($h2).not.toHaveLength(0);
    expect($h2).toHaveLength(1);
    expect($h2[0]).toHaveProperty('tagName', 'h2');
  });

  it('should be able to create complicated html', () => {
    const $script = cheerio(
      '<script src="script.js" type="text/javascript"></script>',
    ) as Cheerio<Element>;
    expect($script).not.toHaveLength(0);
    expect($script).toHaveLength(1);
    expect($script[0].attribs).toHaveProperty('src', 'script.js');
    expect($script[0].attribs).toHaveProperty('type', 'text/javascript');
    expect($script[0].childNodes).toHaveLength(0);
  });

  // eslint-disable-next-line vitest/expect-expect
  it('should be able to select .apple with only a context', () => {
    const $apple = cheerio('.apple', fruits);
    testAppleSelect($apple);
  });

  // eslint-disable-next-line vitest/expect-expect
  it('should be able to select .apple with a node as context', () => {
    const $apple = cheerio('.apple', cheerio(fruits)[0]);
    testAppleSelect($apple);
  });

  // eslint-disable-next-line vitest/expect-expect
  it('should be able to select .apple with only a root', () => {
    const $apple = cheerio('.apple', null, fruits);
    testAppleSelect($apple);
  });

  it('should be able to select an id', () => {
    const $fruits = cheerio('#fruits', null, fruits);
    expect($fruits).toHaveLength(1);
    expect($fruits[0].attribs).toHaveProperty('id', 'fruits');
  });

  it('should be able to select a tag', () => {
    const $ul = cheerio('ul', fruits);
    expect($ul).toHaveLength(1);
    expect($ul[0].tagName).toBe('ul');
  });

  it('should accept a node reference as a context', () => {
    const $elems = cheerio('<div><span></span></div>');
    expect(cheerio('span', $elems[0])).toHaveLength(1);
  });

  it('should accept an array of node references as a context', () => {
    const $elems = cheerio('<div><span></span></div>');
    expect(cheerio('span', $elems.toArray())).toHaveLength(1);
  });

  it('should select only elements inside given context (Issue #193)', () => {
    const $ = cheerio.load(food);
    const $fruits = $('#fruits');
    const fruitElements = $('li', $fruits);

    expect(fruitElements).toHaveLength(3);
  });

  it('should be able to select multiple tags', () => {
    const $fruits = cheerio('li', null, fruits);
    expect($fruits).toHaveLength(3);
    const classes = ['apple', 'orange', 'pear'];
    $fruits.each((idx, $fruit) => {
      expect($fruit.attribs).toHaveProperty('class', classes[idx]);
    });
  });

  // eslint-disable-next-line vitest/expect-expect
  it('should be able to do: cheerio("#fruits .apple")', () => {
    const $apple = cheerio('#fruits .apple', fruits);
    testAppleSelect($apple);
  });

  // eslint-disable-next-line vitest/expect-expect
  it('should be able to do: cheerio("li.apple")', () => {
    const $apple = cheerio('li.apple', fruits);
    testAppleSelect($apple);
  });

  // eslint-disable-next-line vitest/expect-expect
  it('should be able to select by attributes', () => {
    const $apple = cheerio('li[class=apple]', fruits);
    testAppleSelect($apple);
  });

  it('should be able to select multiple classes: cheerio(".btn.primary")', () => {
    const $a = cheerio(
      '.btn.primary',
      '<p><a class="btn primary" href="#">Save</a></p>',
    );
    expect($a).toHaveLength(1);
    expect($a[0].childNodes[0]).toHaveProperty('data', 'Save');
  });

  it('should not create a top-level node', () => {
    const $elem = cheerio('* div', '<div>');
    expect($elem).toHaveLength(0);
  });

  it('should be able to select multiple elements: cheerio(".apple, #fruits")', () => {
    const $elems = cheerio('.apple, #fruits', fruits);
    expect($elems).toHaveLength(2);

    const $apple = $elems
      .toArray()
      .filter((elem) => elem.attribs['class'] === 'apple');
    const $fruit = $elems
      .toArray()
      .find((elem) => elem.attribs['id'] === 'fruits');
    testAppleSelect($apple);
    expect($fruit?.attribs).toHaveProperty('id', 'fruits');
  });

  it('should select first element cheerio(:first)', () => {
    const $elem = cheerio('li:first', fruits);
    expect($elem.attr('class')).toBe('apple');

    const $filtered = cheerio('li', fruits).filter(':even');
    expect($filtered).toHaveLength(2);
  });

  it('should be able to select immediate children: cheerio("#fruits > .pear")', () => {
    const $food = cheerio(food);
    cheerio('.pear', $food).append('<li class="pear">Another Pear!</li>');
    expect(cheerio('#fruits .pear', $food)).toHaveLength(2);
    const $elem = cheerio('#fruits > .pear', $food);
    expect($elem).toHaveLength(1);
    expect($elem.attr('class')).toBe('pear');
  });

  it('should be able to select immediate children: cheerio(".apple + .pear")', () => {
    expect(cheerio('.apple + li', fruits)).toHaveLength(1);
    expect(cheerio('.apple + .pear', fruits)).toHaveLength(0);
    const $elem = cheerio('.apple + .orange', fruits);
    expect($elem).toHaveLength(1);
    expect($elem.attr('class')).toBe('orange');
  });

  it('should be able to select immediate children: cheerio(".apple ~ .pear")', () => {
    expect(cheerio('.apple ~ li', fruits)).toHaveLength(2);
    expect(cheerio('.apple ~ .pear', fruits).attr('class')).toBe('pear');
  });

  it('should handle wildcards on attributes: cheerio("li[class*=r]")', () => {
    const $elem = cheerio('li[class*=r]', fruits);
    expect($elem).toHaveLength(2);
    expect($elem.eq(0).attr('class')).toBe('orange');
    expect($elem.eq(1).attr('class')).toBe('pear');
  });

  it('should handle beginning of attr selectors: cheerio("li[class^=o]")', () => {
    const $elem = cheerio('li[class^=o]', fruits);
    expect($elem).toHaveLength(1);
    expect($elem.eq(0).attr('class')).toBe('orange');
  });

  it('should handle beginning of attr selectors: cheerio("li[class$=e]")', () => {
    const $elem = cheerio('li[class$=e]', fruits);
    expect($elem).toHaveLength(2);
    expect($elem.eq(0).attr('class')).toBe('apple');
    expect($elem.eq(1).attr('class')).toBe('orange');
  });

  it('(extended Array) should not interfere with prototype methods (issue #119)', () => {
    const extended: AnyNode[] = [];
    // @ts-expect-error - Ignore for testing
    extended.find =
      // @ts-expect-error - Ignore for testing
      extended.children =
      // @ts-expect-error - Ignore for testing
      extended.each =
        () => {
          /* Ignore */
        };
    const $empty = cheerio(extended);

    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    expect($empty.find).toBe(cheerio.prototype.find);
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    expect($empty.children).toBe(cheerio.prototype.children);
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    expect($empty.each).toBe(cheerio.prototype.each);
  });

  it('cheerio.html(null) should return a "" string', () => {
    expect(cheerio.html(null as never)).toBe('');
  });

  it('should set html(number) as a string', () => {
    const $elem = cheerio('<div>');
    $elem.html(123 as never);
    expect(typeof $elem.text()).toBe('string');
  });

  it('should set text(number) as a string', () => {
    const $elem = cheerio('<div>');
    $elem.text(123 as never);
    expect(typeof $elem.text()).toBe('string');
  });

  describe('.load', () => {
    it('should generate selections as proper instances', () => {
      const $ = cheerio.load(fruits);

      expect($('.apple')).toBeInstanceOf($);
    });

    // Issue #1092
    it('should handle a character `)` in `:contains` selector', () => {
      const result =
        cheerio.load('<p>)aaa</p>')(String.raw`:contains('\)aaa')`);
      expect(result).toHaveLength(3);
      expect(result.first().prop('tagName')).toBe('HTML');
      expect(result.eq(1).prop('tagName')).toBe('BODY');
      expect(result.last().prop('tagName')).toBe('P');
    });

    it('should be able to filter down using the context', () => {
      const $ = cheerio.load(fruits);
      const apple = $('.apple', 'ul');
      const lis = $('li', 'ul');

      expect(apple).toHaveLength(1);
      expect(lis).toHaveLength(3);
    });

    it('should preserve root content', () => {
      const $ = cheerio.load(fruits);
      // Root should not be overwritten
      const el = $('<div></div>');
      expect(Object.is(el, el._root)).toBe(false);
      // Query has to have results
      expect($('li', 'ul')).toHaveLength(3);
    });

    it('should allow loading a pre-parsed DOM', () => {
      const dom = parseDOM(food);
      const $ = cheerio.load(dom);

      expect($('ul')).toHaveLength(3);
    });

    it('should allow loading a single element', () => {
      const el = parseDOM(food)[0];
      const $ = cheerio.load(el);

      expect($('ul')).toHaveLength(3);
    });

    it('should render xml in html() when options.xml = true', () => {
      const str = '<MixedCaseTag UPPERCASEATTRIBUTE=""></MixedCaseTag>';
      const expected = '<MixedCaseTag UPPERCASEATTRIBUTE=""/>';
      const $ = cheerio.load(str, { xml: true });

      expect($('MixedCaseTag').get(0)).toHaveProperty(
        'tagName',
        'MixedCaseTag',
      );
      expect($.html()).toBe(expected);
    });

    it('should render xml in html() when options.xml = true passed to html()', () => {
      const str = '<MixedCaseTag UPPERCASEATTRIBUTE=""></MixedCaseTag>';
      // Since parsing done without xml flag, all tags converted to lowercase
      const expectedXml =
        '<html><head/><body><mixedcasetag uppercaseattribute=""/></body></html>';
      const expectedNoXml =
        '<html><head></head><body><mixedcasetag uppercaseattribute=""></mixedcasetag></body></html>';
      const $ = cheerio.load(str);

      expect($('MixedCaseTag').get(0)).toHaveProperty(
        'tagName',
        'mixedcasetag',
      );
      expect($.html()).toBe(expectedNoXml);
      expect($.html({ xml: true })).toBe(expectedXml);
    });

    it('should respect options on the element level', () => {
      const str =
        '<!doctype html><html><head><title>Some test</title></head><body><footer><p>Copyright &copy; 2003-2014</p></footer></body></html>';
      const expectedHtml = '<p>Copyright &copy; 2003-2014</p>';
      const expectedXml = '<p>Copyright © 2003-2014</p>';
      const domNotEncoded = cheerio.load(str, {
        xml: { decodeEntities: false },
      });
      const domEncoded = cheerio.load(str);

      expect(domNotEncoded('footer').html()).toBe(expectedHtml);
      expect(domEncoded('footer').html()).toBe(expectedXml);
    });

    it('should use htmlparser2 if xml option is used', () => {
      const str = '<div></div>';
      const dom = cheerio.load(str, null, false);
      expect(dom.html()).toBe(str);
    });

    it('should return a fully-qualified Function', () => {
      const $ = cheerio.load('<div>');

      expect($).toBeInstanceOf(Function);
    });

    describe('prototype extensions', () => {
      it('should honor extensions defined on `prototype` property', () => {
        const $ = cheerio.load('<div>');

        ($.prototype as Cheerio<AnyNode>).myPlugin = function (
          ...args: unknown[]
        ) {
          return {
            context: this,
            args,
          };
        };

        const $div = $('div');

        expect(typeof $div.myPlugin).toBe('function');
        expect($div.myPlugin().context).toBe($div);
        expect($div.myPlugin(1, 2, 3).args).toStrictEqual([1, 2, 3]);
      });

      it('should honor extensions defined on `fn` property', () => {
        const $ = cheerio.load('<div>');
        $.fn.myPlugin = function (...args: unknown[]) {
          return {
            context: this,
            args,
          };
        };

        const $div = $('div');

        expect(typeof $div.myPlugin).toBe('function');
        expect($div.myPlugin().context).toBe($div);
        expect($div.myPlugin(1, 2, 3).args).toStrictEqual([1, 2, 3]);
      });

      it('should isolate extensions between loaded functions', () => {
        const $a = cheerio.load('<div>');
        const $b = cheerio.load('<div>');

        ($a.prototype as Cheerio<AnyNode>).foo = () => {
          /* Ignore */
        };

        expect($b('div').foo).toBeUndefined();
      });
    });
  });

  describe('parse5 options', () => {
    // Should parse noscript tags only with false option value
    it('{scriptingEnabled: ???}', () => {
      // [default] `scriptingEnabled: true` - tag contains one text element
      const withScripts = cheerio.load(noscript)('noscript');
      expect(withScripts).toHaveLength(1);
      expect(withScripts[0].children).toHaveLength(1);
      expect(withScripts[0].children[0].type).toBe('text');

      // `scriptingEnabled: false` - content of noscript will parsed
      const noScripts = cheerio.load(noscript, { scriptingEnabled: false })(
        'noscript',
      );
      expect(noScripts).toHaveLength(1);
      expect(noScripts[0].children).toHaveLength(2);
      expect(noScripts[0].children[0].type).toBe('comment');
      expect(noScripts[0].children[1].type).toBe('tag');
      expect(noScripts[0].children[1]).toHaveProperty('name', 'a');

      // `scriptingEnabled: ???` - should acts as true
      for (const val of [undefined, null, 0, '']) {
        const options = { scriptingEnabled: val as never };
        const result = cheerio.load(noscript, options)('noscript');
        expect(result).toHaveLength(1);
        expect(result[0].children).toHaveLength(1);
        expect(result[0].children[0].type).toBe('text');
      }
    });

    // Should contain location data only with truthful option value
    it('{sourceCodeLocationInfo: ???}', () => {
      // Location data should not be present
      for (const val of [undefined, null, 0, false, '']) {
        const options = { sourceCodeLocationInfo: val as never };
        const result = cheerio.load(noscript, options)('noscript');
        expect(result).toHaveLength(1);
        expect(result[0]).not.toHaveProperty('sourceCodeLocation');
      }

      // Location data should be present
      for (const val of [true, 1, 'test']) {
        const options = { sourceCodeLocationInfo: val as never };
        const result = cheerio.load(noscript, options)('noscript');
        expect(result).toHaveLength(1);
        expect(result[0]).toHaveProperty('sourceCodeLocation');
        expect(typeof result[0].sourceCodeLocation).toBe('object');
      }
    });
  });
});
```

## File: `src/cheerio.ts`
```typescript
import type { AnyNode, Document, ParentNode } from 'domhandler';
import * as Attributes from './api/attributes.js';
import * as Css from './api/css.js';
import * as Extract from './api/extract.js';
import * as Forms from './api/forms.js';
import * as Manipulation from './api/manipulation.js';
import * as Traversing from './api/traversing.js';
import type { InternalOptions } from './options.js';
import type { BasicAcceptedElems } from './types.js';

type MethodsType = typeof Attributes &
  typeof Traversing &
  typeof Manipulation &
  typeof Css &
  typeof Forms &
  typeof Extract;

/**
 * The cheerio class is the central class of the library. It wraps a set of
 * elements and provides an API for traversing, modifying, and interacting with
 * the set.
 *
 * Loading a document will return the Cheerio class bound to the root element of
 * the document. The class will be instantiated when querying the document (when
 * calling `$('selector')`).
 *
 * @example This is the HTML markup we will be using in all of the API examples:
 *
 * ```html
 * <ul id="fruits">
 *   <li class="apple">Apple</li>
 *   <li class="orange">Orange</li>
 *   <li class="pear">Pear</li>
 * </ul>
 * ```
 */
export abstract class Cheerio<T> implements ArrayLike<T> {
  length = 0;
  [index: number]: T;

  options: InternalOptions;
  /**
   * The root of the document. Can be set by using the `root` argument of the
   * constructor.
   *
   * @private
   */
  _root: Cheerio<Document> | null;

  /**
   * Instance of cheerio. Methods are specified in the modules. Usage of this
   * constructor is not recommended. Please use `$.load` instead.
   *
   * @private
   * @param elements - The new selection.
   * @param root - Sets the root node.
   * @param options - Options for the instance.
   */
  constructor(
    elements: ArrayLike<T> | undefined,
    root: Cheerio<Document> | null,
    options: InternalOptions,
  ) {
    this.options = options;
    this._root = root;

    if (elements) {
      for (let idx = 0; idx < elements.length; idx++) {
        this[idx] = elements[idx];
      }
      this.length = elements.length;
    }
  }

  prevObject: Cheerio<any> | undefined;
  /**
   * Make a cheerio object.
   *
   * @private
   * @param dom - The contents of the new object.
   * @param context - The context of the new object.
   * @returns The new cheerio object.
   */
  abstract _make<T>(
    dom: ArrayLike<T> | T | string,
    context?: BasicAcceptedElems<AnyNode>,
  ): Cheerio<T>;

  /**
   * Parses some content.
   *
   * @private
   * @param content - Content to parse.
   * @param options - Options for parsing.
   * @param isDocument - Allows parser to be switched to fragment mode.
   * @returns A document containing the `content`.
   */
  abstract _parse(
    content: string | Document | AnyNode | AnyNode[] | Buffer,
    options: InternalOptions,
    isDocument: boolean,
    context: ParentNode | null,
  ): Document;

  /**
   * Render an element or a set of elements.
   *
   * @private
   * @param dom - DOM to render.
   * @returns The rendered DOM.
   */
  abstract _render(dom: AnyNode | ArrayLike<AnyNode>): string;
}

/** Public Cheerio collection interface exposed by the module. */
export interface Cheerio<T> extends MethodsType, Iterable<T> {
  cheerio: '[cheerio object]';

  splice: typeof Array.prototype.splice;
}

/** Set a signature of the object. */
Cheerio.prototype.cheerio = '[cheerio object]';

/*
 * Make cheerio an array-like object
 */
Cheerio.prototype.splice = Array.prototype.splice;

// Support for (const element of $(...)) iteration:
Cheerio.prototype[Symbol.iterator] = Array.prototype[Symbol.iterator];

// Plug in the API
Object.assign(
  Cheerio.prototype,
  Attributes,
  Traversing,
  Manipulation,
  Css,
  Forms,
  Extract,
);
```

## File: `src/index-browser.mts`
```
export * from './load-parse.js';
export type {
  AnyNode,
  Cheerio,
  CheerioAPI,
  CheerioOptions,
  Document,
  Element,
  HTMLParser2Options,
  ParentNode,
} from './slim.js';
export { contains, merge } from './static.js';
export type * from './types.js';
```

## File: `src/index.spec.ts`
```typescript
import { createServer, type RequestListener, type Server } from 'node:http';
import { Writable } from 'node:stream';
import { afterEach, describe, expect, it } from 'vitest';
import * as cheerio from './index.js';

function noop() {
  // Ignore
}

// Returns a promise and a resolve function
function getPromise() {
  let cb!: (error: Error | null | undefined, $: cheerio.CheerioAPI) => void;
  const promise = new Promise<cheerio.CheerioAPI>((resolve, reject) => {
    cb = (error, $) => (error ? reject(error) : resolve($));
  });

  return { promise, cb };
}

const TEST_HTML = '<h1>Hello World</h1><a href="link">Example</a>';
const TEST_HTML_UTF16 = Buffer.from(TEST_HTML, 'utf16le');
const TEST_HTML_UTF16_BOM = Buffer.from([
  // UTF16-LE BOM
  0xff,
  0xfe,
  ...TEST_HTML_UTF16,
]);

describe('loadBuffer', () => {
  it('should parse UTF-8 HTML', () => {
    const $ = cheerio.loadBuffer(Buffer.from(TEST_HTML));

    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
  });

  it('should parse UTF-16 HTML', () => {
    const $ = cheerio.loadBuffer(TEST_HTML_UTF16_BOM);

    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
  });
});

describe('stringStream', () => {
  it('should use parse5 by default', async () => {
    const { promise, cb } = getPromise();
    const stream = cheerio.stringStream({}, cb);

    expect(stream).toBeInstanceOf(Writable);

    stream.end(TEST_HTML);

    const $ = await promise;

    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
  });

  it('should error from parse5 on buffer', () => {
    const stream = cheerio.stringStream({}, noop);
    expect(stream).toBeInstanceOf(Writable);

    expect(() => stream.write(Buffer.from(TEST_HTML))).toThrow(
      'Parser can work only with string streams.',
    );
  });

  it('should use htmlparser2 for XML', async () => {
    const { promise, cb } = getPromise();
    const stream = cheerio.stringStream({ xmlMode: true }, cb);

    expect(stream).toBeInstanceOf(Writable);

    stream.end(TEST_HTML);

    const $ = await promise;

    expect($.html()).toBe(TEST_HTML);
  });
});

describe('decodeStream', () => {
  it('should use parse5 by default', async () => {
    const { promise, cb } = getPromise();
    const stream = cheerio.decodeStream({}, cb);

    expect(stream).toBeInstanceOf(Writable);

    stream.end(TEST_HTML_UTF16_BOM);

    const $ = await promise;

    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
    expect($('a').prop('href')).toBe('link');
  });

  it('should use htmlparser2 for XML', async () => {
    const { promise, cb } = getPromise();
    const stream = cheerio.decodeStream({ xmlMode: true }, cb);

    expect(stream).toBeInstanceOf(Writable);

    stream.end(TEST_HTML_UTF16_BOM);

    const $ = await promise;

    expect($.html()).toBe(TEST_HTML);
  });
});

describe('fromURL', () => {
  let server: Server | undefined;

  function createTestServer(
    contentType: string,
    body: string | Buffer,
    handler: RequestListener = (_req, res) => {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(body);
    },
  ): Promise<number> {
    return new Promise((resolve, reject) => {
      server = createServer(handler);

      server.listen(0, () => {
        const address = server?.address();

        if (typeof address === 'string' || address == null) {
          reject(new Error('Failed to get port'));
        } else {
          resolve(address.port);
        }
      });
    });
  }

  afterEach(
    async () =>
      new Promise<void>((resolve, reject) => {
        if (server) {
          server.close((err) => (err ? reject(err) : resolve()));
          server = undefined;
        } else {
          resolve();
        }
      }),
  );

  it('should fetch UTF-8 HTML', async () => {
    const port = await createTestServer('text/html', TEST_HTML);
    const $ = await cheerio.fromURL(`http://localhost:${port}`);

    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
  });

  it('should fetch UTF-16 HTML', async () => {
    const port = await createTestServer(
      'text/html; charset=utf-16le',
      TEST_HTML_UTF16,
    );
    const $ = await cheerio.fromURL(`http://localhost:${port}`);

    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
  });

  it('should parse XML based on Content-Type', async () => {
    const port = await createTestServer('text/xml', TEST_HTML);
    const $ = await cheerio.fromURL(`http://localhost:${port}`);

    expect($.html()).toBe(TEST_HTML);
  });

  it('should throw on non-HTML/XML Content-Type', async () => {
    const port = await createTestServer('text/plain', TEST_HTML);
    await expect(cheerio.fromURL(`http://localhost:${port}`)).rejects.toThrow(
      'The content-type "text/plain" is neither HTML nor XML.',
    );
  });

  it('should throw on non-2xx responses', async () => {
    const port = await createTestServer('text/html', TEST_HTML, (_, res) => {
      res.writeHead(500);
      res.end();
    });

    await expect(cheerio.fromURL(`http://localhost:${port}`)).rejects.toThrow(
      'Response Error',
    );
  });

  it('should follow redirects', async () => {
    let firstRequestUrl: string | undefined;
    let secondRequestUrl: string | undefined;
    const port = await createTestServer('text/html', TEST_HTML, (req, res) => {
      if (firstRequestUrl === undefined) {
        firstRequestUrl = req.url;
        res.writeHead(302, { Location: `http://localhost:${port}/final/path` });
        res.end();
      } else {
        secondRequestUrl = req.url;
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(TEST_HTML);
      }
    });

    const $ = await cheerio.fromURL(`http://localhost:${port}/first`);
    expect(firstRequestUrl).toBe('/first');
    expect(secondRequestUrl).toBe('/final/path');
    expect($.html()).toBe(
      `<html><head></head><body>${TEST_HTML}</body></html>`,
    );
    expect($('a').prop('href')).toBe(`http://localhost:${port}/final/link`);
  });
});
```

## File: `src/index.ts`
```typescript
/**
 * @file Batteries-included version of Cheerio. This module includes several
 *   convenience methods for loading documents from various sources.
 */

export * from './load-parse.js';
export type {
  AnyNode,
  Cheerio,
  CheerioAPI,
  CheerioOptions,
  Document,
  Element,
  HTMLParser2Options,
  ParentNode,
} from './slim.js';
export { contains, merge } from './static.js';
export type * from './types.js';

import { finished, Writable } from 'node:stream';
import {
  DecodeStream,
  decodeBuffer,
  type SnifferOptions,
} from 'encoding-sniffer';
import * as htmlparser2 from 'htmlparser2';
import { adapter as htmlparser2Adapter } from 'parse5-htmlparser2-tree-adapter';
import { ParserStream as Parse5Stream } from 'parse5-parser-stream';
import * as undici from 'undici';
import MIMEType from 'whatwg-mimetype';
import type { CheerioAPI } from './load.js';
import { load } from './load-parse.js';
import {
  type CheerioOptions,
  flattenOptions,
  type InternalOptions,
} from './options.js';

/**
 * Sniffs the encoding of a buffer, then creates a querying function bound to a
 * document created from the buffer.
 *
 * @category Loading
 * @example
 *
 * ```js
 * import * as cheerio from 'cheerio';
 *
 * const buffer = fs.readFileSync('index.html');
 * const $ = cheerio.loadBuffer(buffer);
 * ```
 *
 * @param buffer - The buffer to sniff the encoding of.
 * @param options - The options to pass to Cheerio.
 * @returns The loaded document.
 */
export function loadBuffer(
  buffer: Buffer,
  options: DecodeStreamOptions = {},
): CheerioAPI {
  const opts = flattenOptions(options);
  const str = decodeBuffer(buffer, {
    defaultEncoding: opts?.xmlMode ? 'utf8' : 'windows-1252',
    ...options.encoding,
  });

  return load(str, opts);
}

function _stringStream(
  options: InternalOptions | undefined,
  cb: (err: Error | null | undefined, $: CheerioAPI) => void,
): Writable {
  if (options?._useHtmlParser2) {
    const parser = htmlparser2.createDocumentStream(
      (err, document) => cb(err, load(document, options)),
      options,
    );

    return new Writable({
      decodeStrings: false,
      write(chunk, _encoding, callback) {
        if (typeof chunk !== 'string') {
          throw new TypeError('Expected a string');
        }

        parser.write(chunk);
        callback();
      },
      final(callback) {
        parser.end();
        callback();
      },
    });
  }

  options ??= {};
  options.treeAdapter ??= htmlparser2Adapter;

  if (options.scriptingEnabled !== false) {
    options.scriptingEnabled = true;
  }

  const stream = new Parse5Stream(options);

  finished(stream, (err) => cb(err, load(stream.document, options)));

  return stream;
}

/**
 * Creates a stream that parses a sequence of strings into a document.
 *
 * The stream is a `Writable` stream that accepts strings. When the stream is
 * finished, the callback is called with the loaded document.
 *
 * @category Loading
 * @example
 *
 * ```js
 * import * as cheerio from 'cheerio';
 * import * as fs from 'fs';
 *
 * const writeStream = cheerio.stringStream({}, (err, $) => {
 *   if (err) {
 *     // Handle error
 *   }
 *
 *   console.log($('h1').text());
 *   // Output: Hello, world!
 * });
 *
 * fs.createReadStream('my-document.html', { encoding: 'utf8' }).pipe(
 *   writeStream,
 * );
 * ```
 *
 * @param options - The options to pass to Cheerio.
 * @param cb - The callback to call when the stream is finished.
 * @returns The writable stream.
 */
export function stringStream(
  options: CheerioOptions,
  cb: (err: Error | null | undefined, $: CheerioAPI) => void,
): Writable {
  return _stringStream(flattenOptions(options), cb);
}

/** Options used by {@link decodeStream} for decoding incoming buffers. */
export interface DecodeStreamOptions extends CheerioOptions {
  encoding?: SnifferOptions;
}

/**
 * Parses a stream of buffers into a document.
 *
 * The stream is a `Writable` stream that accepts buffers. When the stream is
 * finished, the callback is called with the loaded document.
 *
 * @category Loading
 * @param options - The options to pass to Cheerio.
 * @param cb - The callback to call when the stream is finished.
 * @returns The writable stream.
 */
export function decodeStream(
  options: DecodeStreamOptions,
  cb: (err: Error | null | undefined, $: CheerioAPI) => void,
): Writable {
  const { encoding = {}, ...cheerioOptions } = options;
  const opts = flattenOptions(cheerioOptions);

  // Set the default encoding to UTF-8 for XML mode
  encoding.defaultEncoding ??= opts?.xmlMode ? 'utf8' : 'windows-1252';

  const decodeStream = new DecodeStream(encoding);
  const loadStream = _stringStream(opts, cb);

  decodeStream.pipe(loadStream);

  return decodeStream;
}

type UndiciStreamOptions = Omit<
  undici.Dispatcher.RequestOptions<unknown>,
  'path'
>;

/** Options accepted by {@link fromURL}. */
export interface CheerioRequestOptions extends DecodeStreamOptions {
  /** The options passed to `undici`'s `stream` method. */
  requestOptions?: UndiciStreamOptions;
}

const defaultRequestOptions: UndiciStreamOptions = {
  method: 'GET',
  // Set an Accept header
  headers: {
    accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  },
};

/**
 * `fromURL` loads a document from a URL.
 *
 * By default, redirects are allowed and non-2xx responses are rejected.
 *
 * @category Loading
 * @example
 *
 * ```js
 * import * as cheerio from 'cheerio';
 *
 * const $ = await cheerio.fromURL('https://example.com');
 * ```
 *
 * @param url - The URL to load the document from.
 * @param options - The options to pass to Cheerio.
 * @returns The loaded document.
 */
export async function fromURL(
  url: string | URL,
  options: CheerioRequestOptions = {},
): Promise<CheerioAPI> {
  const {
    requestOptions = defaultRequestOptions,
    encoding = {},
    ...cheerioOptions
  } = options;
  let undiciStream: Promise<undici.Dispatcher.StreamData<unknown>> | undefined;

  // Add headers if none were supplied.
  const urlObject = typeof url === 'string' ? new URL(url) : url;
  const streamOptions = {
    headers: defaultRequestOptions.headers,
    path: urlObject.pathname + urlObject.search,
    ...requestOptions,
  };

  const promise = new Promise<CheerioAPI>((resolve, reject) => {
    undiciStream = new undici.Client(urlObject.origin)
      .compose(undici.interceptors.redirect({ maxRedirections: 5 }))
      .stream(streamOptions, (res) => {
        if (res.statusCode < 200 || res.statusCode >= 300) {
          throw new undici.errors.ResponseError(
            'Response Error',
            res.statusCode,
            {
              headers: res.headers,
            },
          );
        }

        const contentTypeHeader = res.headers['content-type'] ?? 'text/html';
        const mimeType = new MIMEType(
          Array.isArray(contentTypeHeader)
            ? contentTypeHeader[0]
            : contentTypeHeader,
        );

        if (!(mimeType.isHTML() || mimeType.isXML())) {
          throw new RangeError(
            `The content-type "${mimeType.essence}" is neither HTML nor XML.`,
          );
        }

        // Forward the charset from the header to the decodeStream.
        encoding.transportLayerEncodingLabel =
          mimeType.parameters.get('charset');

        /*
         * If we allow redirects, we will have entries in the history.
         * The last entry will be the final URL.
         */
        const history = (
          res.context as
            | {
                history?: URL[];
              }
            | undefined
        )?.history;
        // Set the `baseURI` to the final URL.
        const baseURI = history?.at(-1) ?? urlObject;

        const opts: DecodeStreamOptions = {
          encoding,
          // Set XML mode based on the MIME type.
          xmlMode: mimeType.isXML(),
          baseURI,
          ...cheerioOptions,
        };

        return decodeStream(opts, (err, $) => (err ? reject(err) : resolve($)));
      });
  });

  // Let's make sure the request is completed before returning the promise.
  await undiciStream;

  return promise;
}
```

## File: `src/load-parse.ts`
```typescript
import renderWithHtmlparser2 from 'dom-serializer';
import type { AnyNode } from 'domhandler';
import { parseDocument as parseWithHtmlparser2 } from 'htmlparser2';
import { type CheerioAPI, getLoad } from './load.js';
import type { CheerioOptions } from './options.js';
import { getParse } from './parse.js';
import { parseWithParse5, renderWithParse5 } from './parsers/parse5-adapter.js';

const parse = getParse((content, options, isDocument, context) =>
  options._useHtmlParser2
    ? parseWithHtmlparser2(content, options)
    : parseWithParse5(content, options, isDocument, context),
);

// Duplicate docs due to https://github.com/TypeStrong/typedoc/issues/1616
/**
 * Create a querying function, bound to a document created from the provided
 * markup.
 *
 * Note that similar to web browser contexts, this operation may introduce
 * `<html>`, `<head>`, and `<body>` elements; set `isDocument` to `false` to
 * switch to fragment mode and disable this.
 *
 * @category Loading
 * @param content - Markup to be loaded.
 * @param options - Options for the created instance.
 * @param isDocument - Allows parser to be switched to fragment mode.
 * @returns The loaded document.
 * @see {@link https://cheerio.js.org/brain/knowledge/docs_legacy/basics/loading#load} for additional usage information.
 */
export const load: (
  content: string | AnyNode | AnyNode[] | Buffer,
  options?: CheerioOptions | null,
  isDocument?: boolean,
) => CheerioAPI = getLoad(parse, (dom, options) =>
  options._useHtmlParser2
    ? renderWithHtmlparser2(dom, options)
    : renderWithParse5(dom),
);
```

## File: `src/load.spec.ts`
```typescript
import { describe, expect, it } from 'vitest';
import { load } from './index.js';

describe('.load', () => {
  it('(html) : should retain original root after creating a new node', () => {
    const $ = load('<body><ul id="fruits"></ul></body>');
    expect($('body')).toHaveLength(1);
    $('<script>');
    expect($('body')).toHaveLength(1);
  });

  it('(html) : should handle lowercase tag options', () => {
    const $ = load('<BODY><ul id="fruits"></ul></BODY>', {
      xml: { lowerCaseTags: true },
    });
    expect($.html()).toBe('<body><ul id="fruits"/></body>');
  });

  it('(html) : should handle xml tag option', () => {
    const $ = load('<body><script><foo></script></body>', {
      xml: true,
    });
    expect($('script')[0].children[0].type).toBe('tag');
  });

  it('(buffer) : should accept a buffer', () => {
    const html = '<html><head></head><body>foo</body></html>';
    const $html = load(Buffer.from(html));
    expect($html.html()).toBe(html);
  });
});
```

## File: `src/load.ts`
```typescript
import type { AnyNode, Document, Element, ParentNode } from 'domhandler';
import { ElementType } from 'htmlparser2';
import { Cheerio } from './cheerio.js';
import {
  type CheerioOptions,
  flattenOptions,
  type InternalOptions,
} from './options.js';
import * as staticMethods from './static.js';
import type { BasicAcceptedElems, SelectorType } from './types.js';
import { isCheerio, isHtml } from './utils.js';

export type { AnyNode, Document, Element, ParentNode } from 'domhandler';

type StaticType = typeof staticMethods;

/**
 * A querying function, bound to a document created from the provided markup.
 *
 * Also provides several helper methods for dealing with the document as a
 * whole.
 */
export interface CheerioAPI extends StaticType {
  /**
   * This selector method is the starting point for traversing and manipulating
   * the document. Like jQuery, it's the primary method for selecting elements
   * in the document.
   *
   * `selector` searches within the `context` scope, which searches within the
   * `root` scope.
   *
   * @example
   *
   * ```js
   * $('ul .pear').attr('class');
   * //=> pear
   *
   * $('li[class=orange]').html();
   * //=> Orange
   *
   * $('.apple', '#fruits').text();
   * //=> Apple
   * ```
   *
   * Optionally, you can also load HTML by passing the string as the selector:
   *
   * ```js
   * $('<ul id="fruits">...</ul>');
   * ```
   *
   * Or the context:
   *
   * ```js
   * $('ul', '<ul id="fruits">...</ul>');
   * ```
   *
   * Or as the root:
   *
   * ```js
   * $('li', 'ul', '<ul id="fruits">...</ul>');
   * ```
   *
   * @param selector - Either a selector to look for within the document, or the
   *   contents of a new Cheerio instance.
   * @param context - Either a selector to look for within the root, or the
   *   contents of the document to query.
   * @param root - Optional HTML document string.
   */
  <T extends AnyNode, S extends string>(
    selector?: S | BasicAcceptedElems<T>,
    context?: BasicAcceptedElems<AnyNode> | null,
    root?: BasicAcceptedElems<Document>,
    options?: CheerioOptions,
  ): Cheerio<S extends SelectorType ? Element : T>;

  /**
   * The root the document was originally loaded with.
   *
   * @private
   */
  _root: Document;

  /**
   * The options the document was originally loaded with.
   *
   * @private
   */
  _options: InternalOptions;

  /** Mimic jQuery's prototype alias for plugin authors. */
  fn: typeof Cheerio.prototype;

  /**
   * The `.load` static method defined on the "loaded" Cheerio factory function
   * is deprecated. Users are encouraged to instead use the `load` function
   * exported by the Cheerio module.
   *
   * @deprecated Use the `load` function exported by the Cheerio module.
   * @category Deprecated
   * @example
   *
   * ```js
   * const $ = cheerio.load('<h1>Hello, <span>world</span>.</h1>');
   * ```
   */
  load: ReturnType<typeof getLoad>;
}

/**
 * Create a loader factory from parser and renderer implementations.
 *
 * @param parse - Parser used to convert input into a document.
 * @param render - Renderer used to serialize nodes back to markup.
 */
export function getLoad(
  parse: Cheerio<AnyNode>['_parse'],
  render: (
    dom: AnyNode | ArrayLike<AnyNode>,
    options: InternalOptions,
  ) => string,
) {
  /**
   * Create a querying function, bound to a document created from the provided
   * markup.
   *
   * Note that similar to web browser contexts, this operation may introduce
   * `<html>`, `<head>`, and `<body>` elements; set `isDocument` to `false` to
   * switch to fragment mode and disable this.
   *
   * @param content - Markup to be loaded.
   * @param options - Options for the created instance.
   * @param isDocument - Allows parser to be switched to fragment mode.
   * @returns The loaded document.
   * @see {@link https://cheerio.js.org/brain/knowledge/docs_legacy/basics/loading#load} for additional usage information.
   */
  return function load(
    content: string | AnyNode | AnyNode[] | Buffer,
    options?: CheerioOptions | null,
    isDocument = true,
  ): CheerioAPI {
    if ((content as string | null) == null) {
      throw new Error('cheerio.load() expects a string');
    }

    const internalOpts = flattenOptions(options);
    const initialRoot = parse(content, internalOpts, isDocument, null);

    /**
     * Create an extended class here, so that extensions only live on one
     * instance.
     */
    class LoadedCheerio<T> extends Cheerio<T> {
      _make<T>(
        selector?: ArrayLike<T> | T | string,
        context?: BasicAcceptedElems<AnyNode> | null,
      ): Cheerio<T> {
        const cheerio = initialize(selector, context);
        cheerio.prevObject = this;

        return cheerio;
      }

      _parse(
        content: string | Document | AnyNode | AnyNode[] | Buffer,
        options: InternalOptions,
        isDocument: boolean,
        context: ParentNode | null,
      ) {
        return parse(content, options, isDocument, context);
      }

      _render(dom: AnyNode | ArrayLike<AnyNode>): string {
        return render(dom, this.options);
      }
    }

    function initialize<T = AnyNode, S extends string = string>(
      selector?: ArrayLike<T> | T | S,
      context?: BasicAcceptedElems<AnyNode> | null,
      root: BasicAcceptedElems<Document> = initialRoot,
      opts?: CheerioOptions,
    ): Cheerio<S extends SelectorType ? Element : T> {
      type Result = S extends SelectorType ? Element : T;

      // $($)
      if (selector && isCheerio<Result>(selector)) return selector;

      const options = flattenOptions(opts, internalOpts);
      const r =
        typeof root === 'string'
          ? [parse(root, options, false, null)]
          : 'length' in root
            ? root
            : [root];
      const rootInstance = isCheerio<Document>(r)
        ? r
        : new LoadedCheerio<Document>(r, null, options);
      // Add a cyclic reference, so that calling methods on `_root` never fails.
      rootInstance._root = rootInstance;

      // $(), $(null), $(undefined), $(false)
      if (!selector) {
        return new LoadedCheerio<Result>(undefined, rootInstance, options);
      }

      const elements: AnyNode[] | undefined =
        typeof selector === 'string' && isHtml(selector)
          ? // $(<html>)
            parse(selector, options, false, null).children
          : isNode(selector)
            ? // $(dom)
              [selector]
            : Array.isArray(selector)
              ? // $([dom])
                selector
              : undefined;

      const instance = new LoadedCheerio(elements, rootInstance, options);

      if (elements) {
        return instance as Cheerio<Result>;
      }

      if (typeof selector !== 'string') {
        throw new TypeError('Unexpected type of selector');
      }

      // We know that our selector is a string now.
      let search = selector;

      const searchContext: Cheerio<AnyNode> | undefined = context
        ? // If we don't have a context, maybe we have a root, from loading
          typeof context === 'string'
          ? isHtml(context)
            ? // $('li', '<ul>...</ul>')
              new LoadedCheerio<Document>(
                [parse(context, options, false, null)],
                rootInstance,
                options,
              )
            : // $('li', 'ul')
              ((search = `${context} ${search}` as S), rootInstance)
          : isCheerio<AnyNode>(context)
            ? // $('li', $)
              context
            : // $('li', node), $('li', [nodes])
              new LoadedCheerio<AnyNode>(
                Array.isArray(context) ? context : [context],
                rootInstance,
                options,
              )
        : rootInstance;

      // If we still don't have a context, return
      if (!searchContext) return instance as Cheerio<Result>;

      /*
       * #id, .class, tag
       */
      return searchContext.find(search) as Cheerio<Result>;
    }

    // Add in static methods & properties
    Object.assign(initialize, staticMethods, {
      load,
      // `_root` and `_options` are used in static methods.
      _root: initialRoot,
      _options: internalOpts,
      // Add `fn` for plugins
      fn: LoadedCheerio.prototype,
      // Add the prototype here to maintain `instanceof` behavior.
      prototype: LoadedCheerio.prototype,
    });

    return initialize as CheerioAPI;
  };
}

function isNode(obj: unknown): obj is AnyNode {
  return (
    // @ts-expect-error: TS doesn't know about the `name` property.
    !!obj.name ||
    // @ts-expect-error: TS doesn't know about the `type` property.
    obj.type === ElementType.Root ||
    // @ts-expect-error: TS doesn't know about the `type` property.
    obj.type === ElementType.Text ||
    // @ts-expect-error: TS doesn't know about the `type` property.
    obj.type === ElementType.Comment
  );
}
```

## File: `src/options.ts`
```typescript
import type { Options as SelectOptions } from 'cheerio-select';
import type { DomSerializerOptions } from 'dom-serializer';
import type { DomHandlerOptions } from 'domhandler';
import type { ParserOptions as HTMLParser2ParserOptions } from 'htmlparser2';
import type { ParserOptions as Parse5ParserOptions } from 'parse5';
import type { Htmlparser2TreeAdapterMap } from 'parse5-htmlparser2-tree-adapter';

/**
 * Options accepted by htmlparser2, the default parser for XML.
 *
 * @see https://github.com/fb55/htmlparser2/wiki/Parser-options
 */
export interface HTMLParser2Options
  extends DomHandlerOptions,
    DomSerializerOptions,
    HTMLParser2ParserOptions {
  /** Treat the input as an XML document. */
  xmlMode?: boolean;
}

/**
 * Options accepted by Cheerio.
 *
 * Please note that parser-specific options are _only recognized_ if the
 * relevant parser is used.
 */
export interface CheerioOptions
  extends Parse5ParserOptions<Htmlparser2TreeAdapterMap> {
  /**
   * Recommended way of configuring htmlparser2 when wanting to parse XML.
   *
   * This will switch Cheerio to use htmlparser2.
   *
   * @default false
   */
  xml?: HTMLParser2Options | boolean;

  /**
   * Enable xml mode, which will switch Cheerio to use htmlparser2.
   *
   * @deprecated Please use the `xml` option instead.
   * @default false
   */
  xmlMode?: boolean;

  /** The base URI for the document. Used to resolve the `href` and `src` props. */
  baseURI?: string | URL;

  /**
   * Is the document in quirks mode?
   *
   * This will lead to `.className` and `#id` being case-insensitive.
   *
   * @default false
   */
  quirksMode?: SelectOptions['quirksMode'];
  /**
   * Extension point for pseudo-classes.
   *
   * Maps from names to either strings of functions.
   *
   * - A string value is a selector that the element must match to be selected.
   * - A function is called with the element as its first argument, and optional
   *   parameters second. If it returns true, the element is selected.
   *
   * @example
   *
   * ```js
   * const $ = cheerio.load(
   *   '<div class="foo"></div><div data-bar="boo"></div>',
   *   {
   *     pseudos: {
   *       // `:foo` is an alias for `div.foo`
   *       foo: 'div.foo',
   *       // `:bar(val)` is equivalent to `[data-bar=val s]`
   *       bar: (el, val) => el.attribs['data-bar'] === val,
   *     },
   *   },
   * );
   *
   * $(':foo').length; // 1
   * $('div:bar(boo)').length; // 1
   * $('div:bar(baz)').length; // 0
   * ```
   */
  pseudos?: SelectOptions['pseudos'];
}

/** Internal options for Cheerio. */
export interface InternalOptions
  extends HTMLParser2Options,
    Omit<CheerioOptions, 'xml'> {
  /**
   * Whether to use htmlparser2.
   *
   * This is set to true if `xml` is set to true.
   */
  _useHtmlParser2?: boolean;
}

const defaultOpts: InternalOptions = {
  _useHtmlParser2: false,
};

/**
 * Flatten the options for Cheerio.
 *
 * This will set `_useHtmlParser2` to true if `xml` is set to true.
 *
 * @param options - The options to flatten.
 * @param baseOptions - The base options to use.
 * @returns The flattened options.
 */
export function flattenOptions(
  options?: CheerioOptions | null,
  baseOptions?: InternalOptions,
): InternalOptions {
  if (!options) {
    return baseOptions ?? defaultOpts;
  }

  const opts: InternalOptions = {
    _useHtmlParser2: !!options.xmlMode,
    ...baseOptions,
    ...options,
  };

  if (options.xml) {
    opts._useHtmlParser2 = true;
    opts.xmlMode = true;

    if (options.xml !== true) {
      Object.assign(opts, options.xml);
    }
  } else if (options.xmlMode) {
    opts._useHtmlParser2 = true;
  }

  return opts;
}
```

## File: `src/parse.spec.ts`
```typescript
import type { Document, Element } from 'domhandler';
import { parseDocument as parseWithHtmlparser2 } from 'htmlparser2';
import { describe, expect, it } from 'vitest';
import { getParse } from './parse.js';
import { parseWithParse5 } from './parsers/parse5-adapter.js';

const defaultOpts = { _useHtmlParser2: false };

const parse = getParse((content, options, isDocument, context) =>
  options._useHtmlParser2
    ? parseWithHtmlparser2(content, options)
    : parseWithParse5(content, options, isDocument, context),
);

// Tags
const basic = '<html></html>';
const siblings = '<h2></h2><p></p>';

// Single Tags
const single = '<br/>';
const singleWrong = '<br>';

// Children
const children = '<html><br/></html>';
const li = '<li class="durian">Durian</li>';

// Attributes
const attributes = '<img src="hello.png" alt="man waving">';
const noValueAttribute = '<textarea disabled></textarea>';

// Comments
const comment = '<!-- sexy -->';
const conditional =
  '<!--[if IE 8]><html class="no-js ie8" lang="en"><![endif]-->';

// Text
const text = 'lorem ipsum';

// Script
const script = '<script type="text/javascript">alert("hi world!");</script>';
const scriptEmpty = '<script></script>';

// Style
const style = '<style type="text/css"> h2 { color:blue; } </style>';
const styleEmpty = '<style></style>';

// Directives
const directive = '<!doctype html>';

function rootTest(root: Document) {
  expect(root).toHaveProperty('type', 'root');

  expect(root.nextSibling).toBe(null);
  expect(root.previousSibling).toBe(null);
  expect(root.parentNode).toBe(null);

  const child = root.childNodes[0];
  expect(child.parentNode).toBe(root);
}

describe('parse', () => {
  describe('evaluate', () => {
    it(`should parse basic empty tags: ${basic}`, () => {
      const [tag] = parse(basic, defaultOpts, true, null).children as Element[];
      expect(tag.type).toBe('tag');
      expect(tag.tagName).toBe('html');
      expect(tag.childNodes).toHaveLength(2);
    });

    it(`should handle sibling tags: ${siblings}`, () => {
      const dom = parse(siblings, defaultOpts, false, null)
        .children as Element[];
      const [h2, p] = dom;

      expect(dom).toHaveLength(2);
      expect(h2.tagName).toBe('h2');
      expect(p.tagName).toBe('p');
    });

    it(`should handle single tags: ${single}`, () => {
      const [tag] = parse(single, defaultOpts, false, null)
        .children as Element[];
      expect(tag.type).toBe('tag');
      expect(tag.tagName).toBe('br');
      expect(tag.childNodes).toHaveLength(0);
    });

    it(`should handle malformatted single tags: ${singleWrong}`, () => {
      const [tag] = parse(singleWrong, defaultOpts, false, null)
        .children as Element[];
      expect(tag.type).toBe('tag');
      expect(tag.tagName).toBe('br');
      expect(tag.childNodes).toHaveLength(0);
    });

    it(`should handle tags with children: ${children}`, () => {
      const [tag] = parse(children, defaultOpts, true, null)
        .children as Element[];
      expect(tag.type).toBe('tag');
      expect(tag.tagName).toBe('html');
      expect(tag.childNodes).toBeTruthy();
      expect(tag.childNodes[1]).toHaveProperty('tagName', 'body');
      expect((tag.childNodes[1] as Element).childNodes).toHaveLength(1);
    });

    it(`should handle tags with children: ${li}`, () => {
      const [tag] = parse(li, defaultOpts, false, null).children as Element[];
      expect(tag.childNodes).toHaveLength(1);
      expect(tag.childNodes[0]).toHaveProperty('data', 'Durian');
    });

    it(`should handle tags with attributes: ${attributes}`, () => {
      const attrs = parse(attributes, defaultOpts, false, null)
        .children[0] as Element;
      expect(attrs.attribs).toBeTruthy();
      expect(attrs.attribs).toHaveProperty('src', 'hello.png');
      expect(attrs.attribs).toHaveProperty('alt', 'man waving');
    });

    it(`should handle value-less attributes: ${noValueAttribute}`, () => {
      const attrs = parse(noValueAttribute, defaultOpts, false, null)
        .children[0] as Element;
      expect(attrs.attribs).toBeTruthy();
      expect(attrs.attribs).toHaveProperty('disabled', '');
    });

    it(`should handle comments: ${comment}`, () => {
      const elem = parse(comment, defaultOpts, false, null).children[0];
      expect(elem.type).toBe('comment');
      expect(elem).toHaveProperty('data', ' sexy ');
    });

    it(`should handle conditional comments: ${conditional}`, () => {
      const elem = parse(conditional, defaultOpts, false, null).children[0];
      expect(elem.type).toBe('comment');
      expect(elem).toHaveProperty(
        'data',
        conditional.replace('<!--', '').replace('-->', ''),
      );
    });

    it(`should handle text: ${text}`, () => {
      const text_ = parse(text, defaultOpts, false, null).children[0];
      expect(text_.type).toBe('text');
      expect(text_).toHaveProperty('data', 'lorem ipsum');
    });

    it(`should handle script tags: ${script}`, () => {
      const script_ = parse(script, defaultOpts, false, null)
        .children[0] as Element;
      expect(script_.type).toBe('script');
      expect(script_.tagName).toBe('script');
      expect(script_.attribs).toHaveProperty('type', 'text/javascript');
      expect(script_.childNodes).toHaveLength(1);
      expect(script_.childNodes[0].type).toBe('text');
      expect(script_.childNodes[0]).toHaveProperty(
        'data',
        'alert("hi world!");',
      );
    });

    it(`should handle style tags: ${style}`, () => {
      const style_ = parse(style, defaultOpts, false, null)
        .children[0] as Element;
      expect(style_.type).toBe('style');
      expect(style_.tagName).toBe('style');
      expect(style_.attribs).toHaveProperty('type', 'text/css');
      expect(style_.childNodes).toHaveLength(1);
      expect(style_.childNodes[0].type).toBe('text');
      expect(style_.childNodes[0]).toHaveProperty(
        'data',
        ' h2 { color:blue; } ',
      );
    });

    it(`should handle directives: ${directive}`, () => {
      const elem = parse(directive, defaultOpts, true, null).children[0];
      expect(elem.type).toBe('directive');
      expect(elem).toHaveProperty('data', '!DOCTYPE html');
      expect(elem).toHaveProperty('name', '!doctype');
    });
  });

  describe('.parse', () => {
    // Root test utility

    it(`should add root to: ${basic}`, () => {
      const root = parse(basic, defaultOpts, true, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(1);
      expect(root.childNodes[0]).toHaveProperty('tagName', 'html');
    });

    it(`should add root to: ${siblings}`, () => {
      const root = parse(siblings, defaultOpts, false, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(2);
      expect(root.childNodes[0]).toHaveProperty('tagName', 'h2');
      expect(root.childNodes[1]).toHaveProperty('tagName', 'p');
      expect(root.childNodes[1].parent).toBe(root);
    });

    it(`should add root to: ${comment}`, () => {
      const root = parse(comment, defaultOpts, false, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(1);
      expect(root.childNodes[0].type).toBe('comment');
    });

    it(`should add root to: ${text}`, () => {
      const root = parse(text, defaultOpts, false, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(1);
      expect(root.childNodes[0].type).toBe('text');
    });

    it(`should add root to: ${scriptEmpty}`, () => {
      const root = parse(scriptEmpty, defaultOpts, false, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(1);
      expect(root.childNodes[0].type).toBe('script');
    });

    it(`should add root to: ${styleEmpty}`, () => {
      const root = parse(styleEmpty, defaultOpts, false, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(1);
      expect(root.childNodes[0].type).toBe('style');
    });

    it(`should add root to: ${directive}`, () => {
      const root = parse(directive, defaultOpts, true, null);
      rootTest(root);
      expect(root.childNodes).toHaveLength(2);
      expect(root.childNodes[0].type).toBe('directive');
    });

    it('should simply return root', () => {
      const oldroot = parse(basic, defaultOpts, true, null);
      const root = parse(oldroot, defaultOpts, true, null);
      expect(root).toBe(oldroot);
      rootTest(root);
      expect(root.childNodes).toHaveLength(1);
      expect(root.childNodes[0]).toHaveProperty('tagName', 'html');
    });

    it('should expose the DOM level 1 API', () => {
      const root = parse(
        '<div><a></a><span></span><p></p></div>',
        defaultOpts,
        false,
        null,
      ).childNodes[0] as Element;
      const childNodes = root.childNodes as Element[];

      expect(childNodes).toHaveLength(3);

      expect(root.tagName).toBe('div');
      expect(root.firstChild).toBe(childNodes[0]);
      expect(root.lastChild).toBe(childNodes[2]);

      expect(childNodes[0].tagName).toBe('a');
      expect(childNodes[0].previousSibling).toBe(null);
      expect(childNodes[0].nextSibling).toBe(childNodes[1]);
      expect(childNodes[0].parentNode).toBe(root);
      expect(childNodes[0].childNodes).toHaveLength(0);
      expect(childNodes[0].firstChild).toBe(null);
      expect(childNodes[0].lastChild).toBe(null);

      expect(childNodes[1].tagName).toBe('span');
      expect(childNodes[1].previousSibling).toBe(childNodes[0]);
      expect(childNodes[1].nextSibling).toBe(childNodes[2]);
      expect(childNodes[1].parentNode).toBe(root);
      expect(childNodes[1].childNodes).toHaveLength(0);
      expect(childNodes[1].firstChild).toBe(null);
      expect(childNodes[1].lastChild).toBe(null);

      expect(childNodes[2].tagName).toBe('p');
      expect(childNodes[2].previousSibling).toBe(childNodes[1]);
      expect(childNodes[2].nextSibling).toBe(null);
      expect(childNodes[2].parentNode).toBe(root);
      expect(childNodes[2].childNodes).toHaveLength(0);
      expect(childNodes[2].firstChild).toBe(null);
      expect(childNodes[2].lastChild).toBe(null);
    });

    it('Should parse less than or equal sign sign', () => {
      const root = parse('<i>A</i><=<i>B</i>', defaultOpts, false, null);
      const { childNodes } = root;

      expect(childNodes[0]).toHaveProperty('tagName', 'i');
      expect((childNodes[0] as Element).childNodes[0]).toHaveProperty(
        'data',
        'A',
      );
      expect(childNodes[1]).toHaveProperty('data', '<=');
      expect(childNodes[2]).toHaveProperty('tagName', 'i');
      expect((childNodes[2] as Element).childNodes[0]).toHaveProperty(
        'data',
        'B',
      );
    });

    it('Should ignore unclosed CDATA', () => {
      const root = parse(
        '<a></a><script>foo //<![CDATA[ bar</script><b></b>',
        defaultOpts,
        false,
        null,
      );
      const childNodes = root.childNodes as Element[];

      expect(childNodes[0].tagName).toBe('a');
      expect(childNodes[1].tagName).toBe('script');
      expect(childNodes[1].childNodes[0]).toHaveProperty(
        'data',
        'foo //<![CDATA[ bar',
      );
      expect(childNodes[2].tagName).toBe('b');
    });

    it('Should add <head> to documents', () => {
      const root = parse('<html></html>', defaultOpts, true, null);
      const childNodes = root.childNodes as Element[];

      expect(childNodes[0].tagName).toBe('html');
      expect(childNodes[0].childNodes[0]).toHaveProperty('tagName', 'head');
    });

    it('Should implicitly create <tr> around <td>', () => {
      const root = parse(
        '<table><td>bar</td></tr></table>',
        defaultOpts,
        false,
        null,
      );

      const table = root.childNodes[0] as Element;
      expect(table.tagName).toBe('table');
      expect(table.childNodes.length).toBe(1);
      const tbody = table.childNodes[0] as Element;
      expect(table.childNodes[0]).toHaveProperty('tagName', 'tbody');
      const tr = tbody.childNodes[0] as Element;
      expect(tr).toHaveProperty('tagName', 'tr');
      const td = tr.childNodes[0] as Element;
      expect(td).toHaveProperty('tagName', 'td');
      expect(td.childNodes[0]).toHaveProperty('data', 'bar');
    });

    it('Should parse custom tag <line>', () => {
      const root = parse('<line>test</line>', defaultOpts, false, null);
      const childNodes = root.childNodes as Element[];

      expect(childNodes.length).toBe(1);
      expect(childNodes[0].tagName).toBe('line');
      expect(childNodes[0].childNodes[0]).toHaveProperty('data', 'test');
    });

    it('Should properly parse misnested table tags', () => {
      const root = parse(
        '<tr><td>i1</td></tr><tr><td>i2</td></td></tr><tr><td>i3</td></td></tr>',
        defaultOpts,
        false,
        null,
      );
      const childNodes = root.childNodes as Element[];

      expect(childNodes.length).toBe(3);

      for (let i = 0; i < childNodes.length; i++) {
        const child = childNodes[i];
        expect(child.tagName).toBe('tr');
        expect(child.childNodes[0]).toHaveProperty('tagName', 'td');
        expect((child.childNodes[0] as Element).childNodes[0]).toHaveProperty(
          'data',
          `i${i + 1}`,
        );
      }
    });

    it('Should correctly parse data url attributes', () => {
      const html =
        '<div style=\'font-family:"butcherman-caps"; src:url(data:font/opentype;base64,AAEA...);\'></div>';
      const expectedAttr =
        'font-family:"butcherman-caps"; src:url(data:font/opentype;base64,AAEA...);';
      const root = parse(html, defaultOpts, false, null);
      const childNodes = root.childNodes as Element[];

      expect(childNodes[0].attribs).toHaveProperty('style', expectedAttr);
    });

    it('Should treat <xmp> tag content as text', () => {
      const root = parse('<xmp><h2></xmp>', defaultOpts, false, null);
      const childNodes = root.childNodes as Element[];

      expect(childNodes[0].childNodes[0]).toHaveProperty('data', '<h2>');
    });

    it('Should correctly parse malformed numbered entities', () => {
      const root = parse('<p>z&#</p>', defaultOpts, false, null);
      const childNodes = root.childNodes as Element[];

      expect(childNodes[0].childNodes[0]).toHaveProperty('data', 'z&#');
    });

    it('Should correctly parse mismatched headings', () => {
      const root = parse('<h2>Test</h3><div></div>', defaultOpts, false, null);
      const { childNodes } = root;

      expect(childNodes.length).toBe(2);
      expect(childNodes[0]).toHaveProperty('tagName', 'h2');
      expect(childNodes[1]).toHaveProperty('tagName', 'div');
    });

    it('Should correctly parse tricky <pre> content', () => {
      const root = parse(
        '<pre>\nA <- factor(A, levels = c("c","a","b"))\n</pre>',
        defaultOpts,
        false,
        null,
      );
      const childNodes = root.childNodes as Element[];

      expect(childNodes.length).toBe(1);
      expect(childNodes[0].tagName).toBe('pre');
      expect(childNodes[0].childNodes[0]).toHaveProperty(
        'data',
        'A <- factor(A, levels = c("c","a","b"))\n',
      );
    });

    it('should pass the options for including the location info to parse5', () => {
      const root = parse(
        '<p>Hello</p>',
        { ...defaultOpts, sourceCodeLocationInfo: true },
        false,
        null,
      );
      const location = root.children[0].sourceCodeLocation;

      expect(typeof location).toBe('object');
      expect(location?.endOffset).toBe(12);
    });
  });
});
```

## File: `src/parse.ts`
```typescript
import {
  type AnyNode,
  isDocument as checkIsDocument,
  Document,
  type ParentNode,
} from 'domhandler';
import { removeElement } from 'domutils';
import type { InternalOptions } from './options.js';

/**
 * Get the parse function with options.
 *
 * @param parser - The parser function.
 * @returns The parse function with options.
 */
export function getParse(
  parser: (
    content: string,
    options: InternalOptions,
    isDocument: boolean,
    context: ParentNode | null,
  ) => Document,
) {
  /**
   * Parse a HTML string or a node.
   *
   * @param content - The HTML string or node.
   * @param options - The parser options.
   * @param isDocument - If `content` is a document.
   * @param context - The context node in the DOM tree.
   * @returns The parsed document node.
   */
  return function parse(
    content: string | Document | AnyNode | AnyNode[] | Buffer,
    options: InternalOptions,
    isDocument: boolean,
    context: ParentNode | null,
  ): Document {
    if (typeof Buffer !== 'undefined' && Buffer.isBuffer(content)) {
      content = content.toString();
    }

    if (typeof content === 'string') {
      return parser(content, options, isDocument, context);
    }

    const doc = content as AnyNode | AnyNode[] | Document;

    if (!Array.isArray(doc) && checkIsDocument(doc)) {
      // If `doc` is already a root, just return it
      return doc;
    }

    // Add content to new root element
    const root = new Document([]);

    // Update the DOM using the root
    update(doc, root);

    return root;
  };
}

/**
 * Update the dom structure, for one changed layer.
 *
 * @param newChilds - The new children.
 * @param parent - The new parent.
 * @returns The parent node.
 */
export function update(
  newChilds: AnyNode[] | AnyNode,
  parent: ParentNode | null,
): ParentNode | null {
  // Normalize
  const arr = Array.isArray(newChilds) ? newChilds : [newChilds];

  // Update parent
  if (parent) {
    parent.children = arr;
  } else {
    parent = null;
  }

  // Update neighbors
  for (let i = 0; i < arr.length; i++) {
    const node = arr[i];

    // Cleanly remove existing nodes from their previous structures.
    if (node.parent && node.parent.children !== arr) {
      removeElement(node);
    }

    if (parent) {
      node.prev = arr[i - 1] || null;
      node.next = arr[i + 1] || null;
    } else {
      node.prev = node.next = null;
    }

    node.parent = parent;
  }

  return parent;
}
```

## File: `src/slim.ts`
```typescript
/**
 * @file Alternative entry point for Cheerio that always uses htmlparser2. This
 *   way, parse5 won't be loaded, saving some memory.
 */

import render from 'dom-serializer';
import type { AnyNode } from 'domhandler';
import { parseDocument } from 'htmlparser2';
import { type CheerioAPI, getLoad } from './load.js';
import type { CheerioOptions } from './options.js';
import { getParse } from './parse.js';

export type { Cheerio } from './cheerio.js';
export type {
  AnyNode,
  CheerioAPI,
  Document,
  Element,
  ParentNode,
} from './load.js';
export type { CheerioOptions, HTMLParser2Options } from './options.js';
export { contains, merge } from './static.js';
export type * from './types.js';

/**
 * Create a querying function, bound to a document created from the provided
 * markup.
 *
 * @param content - Markup to be loaded.
 * @param options - Options for the created instance.
 * @param isDocument - Always `false` here, as we are always using
 *   `htmlparser2`.
 * @returns The loaded document.
 * @see {@link https://cheerio.js.org#loading} for additional usage information.
 */
export const load: (
  content: string | AnyNode | AnyNode[] | Buffer,
  options?: CheerioOptions | null,
  isDocument?: boolean,
) => CheerioAPI = getLoad(getParse(parseDocument), render);
```

## File: `src/static.spec.ts`
```typescript
import { beforeEach, describe, expect, it } from 'vitest';
import { cheerio, eleven, food } from './__fixtures__/fixtures.js';
import type { CheerioAPI } from './index.js';

describe('cheerio', () => {
  describe('.html', () => {
    it('() : should return innerHTML; $.html(obj) should return outerHTML', () => {
      const $div = cheerio(
        'div',
        '<div><span>foo</span><span>bar</span></div>',
      );
      const span = $div.children()[1];
      expect(cheerio(span).html()).toBe('bar');
      expect(cheerio.html(span)).toBe('<span>bar</span>');
    });

    it('(<obj>) : should accept an object, an array, or a cheerio object', () => {
      const $span = cheerio('<span>foo</span>');
      expect(cheerio.html($span[0])).toBe('<span>foo</span>');
      expect(cheerio.html($span)).toBe('<span>foo</span>');
    });

    it('(<value>) : should be able to set to an empty string', () => {
      const $elem = cheerio('<span>foo</span>').html('');
      expect(cheerio.html($elem)).toBe('<span></span>');
    });

    it('(<root>) : does not render the root element', () => {
      const $ = cheerio.load('');
      expect(cheerio.html($.root())).toBe(
        '<html><head></head><body></body></html>',
      );
    });

    it('(<elem>, <root>, <elem>) : does not render the root element', () => {
      const $ = cheerio.load('<div>a div</div><span>a span</span>');
      const $collection = $('div').add($.root()).add('span');
      const expected =
        '<html><head></head><body><div>a div</div><span>a span</span></body></html><div>a div</div><span>a span</span>';
      expect(cheerio.html($collection)).toBe(expected);
    });

    it('() : does not crash with `null` as `this` value', () => {
      const { html } = cheerio;
      expect(html.call(null as never)).toBe('');
      expect(html.call(null as never, '#nothing')).toBe('');
    });
  });

  describe('.text', () => {
    it('(cheerio object) : should return the text contents of the specified elements', () => {
      const $ = cheerio.load('<a>This is <em>content</em>.</a>');
      expect(cheerio.text($('a'))).toBe('This is content.');
    });

    it('(cheerio object) : should omit comment nodes', () => {
      const $ = cheerio.load(
        '<a>This is <!-- a comment --> not a comment.</a>',
      );
      expect(cheerio.text($('a'))).toBe('This is  not a comment.');
    });

    it('(cheerio object) : should include text contents of children recursively', () => {
      const $ = cheerio.load(
        '<a>This is <div>a child with <span>another child and <!-- a comment --> not a comment</span> followed by <em>one last child</em> and some final</div> text.</a>',
      );
      expect(cheerio.text($('a'))).toBe(
        'This is a child with another child and  not a comment followed by one last child and some final text.',
      );
    });

    it('() : should return the rendered text content of the root', () => {
      const $ = cheerio.load(
        '<a>This is <div>a child with <span>another child and <!-- a comment --> not a comment</span> followed by <em>one last child</em> and some final</div> text.</a>',
      );
      expect(cheerio.text($.root())).toBe(
        'This is a child with another child and  not a comment followed by one last child and some final text.',
      );
    });

    it('(cheerio object) : should not omit script tags', () => {
      const $ = cheerio.load('<script>console.log("test")</script>');
      expect(cheerio.text($.root())).toBe('console.log("test")');
    });

    it('(cheerio object) : should omit style tags', () => {
      const $ = cheerio.load(
        '<style type="text/css">.cf-hidden { display: none; }</style>',
      );
      expect($.text()).toBe('.cf-hidden { display: none; }');
    });

    it('() : does not crash with `null` as `this` value', () => {
      const { text } = cheerio;
      expect(text.call(null as never)).toBe('');
    });
  });

  describe('.parseHTML', () => {
    const $ = cheerio.load('');

    it('() : returns null', () => {
      expect($.parseHTML()).toBe(null);
    });

    it('(null) : returns null', () => {
      expect($.parseHTML(null)).toBe(null);
    });

    it('("") : returns null', () => {
      expect($.parseHTML('')).toBe(null);
    });

    it('(largeHtmlString) : parses large HTML strings', () => {
      const html = '<div></div>'.repeat(10);
      const nodes = $.parseHTML(html);

      expect(nodes.length).toBe(10);
      expect(nodes).toBeInstanceOf(Array);
    });

    it('("<script>") : ignores scripts by default', () => {
      const html = '<script>undefined()</script>';
      expect($.parseHTML(html)).toHaveLength(0);
    });

    it('("<script>", true) : preserves scripts when requested', () => {
      const html = '<script>undefined()</script>';
      expect($.parseHTML(html, true)[0]).toHaveProperty('tagName', 'script');
    });

    it('("scriptAndNonScript) : preserves non-script nodes', () => {
      const html = '<script>undefined()</script><div></div>';
      expect($.parseHTML(html)[0]).toHaveProperty('tagName', 'div');
    });

    it('(scriptAndNonScript, true) : Preserves script position', () => {
      const html = '<script>undefined()</script><div></div>';
      expect($.parseHTML(html, true)[0]).toHaveProperty('tagName', 'script');
    });

    it('(text) : returns a text node', () => {
      expect($.parseHTML('text')[0].type).toBe('text');
    });

    it('(<tab>>text) : preserves leading whitespace', () => {
      expect($.parseHTML('\t<div></div>')[0]).toHaveProperty('data', '\t');
    });

    it('( text) : Leading spaces are treated as text nodes', () => {
      expect($.parseHTML(' <div/> ')[0].type).toBe('text');
    });

    it('(html) : should preserve content', () => {
      const html = '<div>test div</div>';
      expect(cheerio($.parseHTML(html)[0]).html()).toBe('test div');
    });

    it('(malformedHtml) : should not break', () => {
      expect($.parseHTML('<span><span>')).toHaveLength(1);
    });

    it('(garbageInput) : should not cause an error', () => {
      expect(
        $.parseHTML('<#if><tr><p>This is a test.</p></tr><#/if>'),
      ).toBeTruthy();
    });

    it('(text) : should return an array that is not effected by DOM manipulation methods', () => {
      const $div = cheerio.load('<div>');
      const elems = $div.parseHTML('<b></b><i></i>');

      $div('div').append(elems);

      expect(elems).toHaveLength(2);
    });

    it('(html, context) : should ignore context argument', () => {
      const $div = cheerio.load('<div>');
      const elems = $div.parseHTML('<script>foo</script><a>', { foo: 123 });

      $div('div').append(elems);

      expect(elems).toHaveLength(1);
    });

    it('(html, context, keepScripts) : should ignore context argument', () => {
      const $div = cheerio.load('<div>');
      const elems = $div.parseHTML(
        '<script>foo</script><a>',
        { foo: 123 },
        true,
      );

      $div('div').append(elems);

      expect(elems).toHaveLength(2);
    });
  });

  describe('.merge', () => {
    const $ = cheerio.load('');

    it('should be a function', () => {
      expect(typeof $.merge).toBe('function');
    });

    it('(arraylike, arraylike) : should modify the first array, but not the second', () => {
      const arr1 = [1, 2, 3];
      const arr2 = [4, 5, 6];

      const ret = $.merge(arr1, arr2);
      expect(typeof ret).toBe('object');
      expect(Array.isArray(ret)).toBe(true);
      expect(ret).toBe(arr1);
      expect(arr1).toHaveLength(6);
      expect(arr2).toHaveLength(3);
    });

    it('(arraylike, arraylike) : should handle objects that arent arrays, but are arraylike', () => {
      const arr1: ArrayLike<string> = {
        length: 3,
        0: 'a',
        1: 'b',
        2: 'c',
      };
      const arr2 = {
        length: 3,
        0: 'd',
        1: 'e',
        2: 'f',
      };

      $.merge(arr1, arr2);
      expect(arr1).toHaveLength(6);
      expect(arr1[3]).toBe('d');
      expect(arr1[4]).toBe('e');
      expect(arr1[5]).toBe('f');
      expect(arr2).toHaveLength(3);
    });

    it('(?, ?) : should gracefully reject invalid inputs', () => {
      expect($.merge([4], 3 as never)).toBeFalsy();
      expect($.merge({} as never, {} as never)).toBeFalsy();
      expect($.merge([], {} as never)).toBeFalsy();
      expect($.merge({} as never, [])).toBeFalsy();
      const fakeArray1 = { length: 3, 0: 'a', 1: 'b', 3: 'd' };
      expect($.merge(fakeArray1, [])).toBeFalsy();
      expect($.merge([], fakeArray1)).toBeFalsy();
      expect($.merge({ length: '7' } as never, [])).toBeFalsy();
      expect($.merge({ length: -1 }, [])).toBeFalsy();
    });

    it('(?, ?) : should no-op on invalid inputs', () => {
      const fakeArray1 = { length: 3, 0: 'a', 1: 'b', 3: 'd' };
      $.merge(fakeArray1, []);
      expect(fakeArray1).toHaveLength(3);
      expect(fakeArray1[0]).toBe('a');
      expect(fakeArray1[1]).toBe('b');
      expect(fakeArray1[3]).toBe('d');
      $.merge([], fakeArray1);
      expect(fakeArray1).toHaveLength(3);
      expect(fakeArray1[0]).toBe('a');
      expect(fakeArray1[1]).toBe('b');
      expect(fakeArray1[3]).toBe('d');
    });
  });

  describe('.contains', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = cheerio.load(food);
    });

    it('(container, contained) : should correctly detect the provided element', () => {
      const $food = $('#food');
      const $fruits = $('#fruits');
      const $apple = $('.apple');

      expect($.contains($food[0], $fruits[0])).toBe(true);
      expect($.contains($food[0], $apple[0])).toBe(true);
    });

    it('(container, other) : should not detect elements that are not contained', () => {
      const $fruits = $('#fruits');
      const $vegetables = $('#vegetables');
      const $apple = $('.apple');

      expect($.contains($vegetables[0], $apple[0])).toBe(false);
      expect($.contains($fruits[0], $vegetables[0])).toBe(false);
      expect($.contains($vegetables[0], $fruits[0])).toBe(false);
      expect($.contains($fruits[0], $fruits[0])).toBe(false);
      expect($.contains($vegetables[0], $vegetables[0])).toBe(false);
    });
  });

  describe('.root', () => {
    it('() : should return a cheerio-wrapped root object', () => {
      const $ = cheerio.load('<html><head></head><body>foo</body></html>');
      $.root().append('<div id="test"></div>');
      expect($.html()).toBe(
        '<html><head></head><body>foo</body></html><div id="test"></div>',
      );
    });
  });

  describe('.extract', () => {
    it('() : should extract values for selectors', () => {
      const $ = cheerio.load(eleven);

      expect(
        $.extract({
          red: [{ selector: '.red', value: 'outerHTML' }],
        }),
      ).toStrictEqual({
        red: [
          '<li class="red">Four</li>',
          '<li class="red">Five</li>',
          '<li class="red sel">Nine</li>',
        ],
      });
    });
  });
});
```

## File: `src/static.ts`
```typescript
import type { AnyNode, Document } from 'domhandler';
import { textContent } from 'domutils';
import type { ExtractedMap, ExtractMap } from './api/extract.js';
import type { Cheerio } from './cheerio.js';
import type { CheerioAPI } from './load.js';
import {
  type CheerioOptions,
  flattenOptions,
  type InternalOptions,
} from './options.js';
import type { BasicAcceptedElems } from './types.js';

/**
 * Helper function to render a DOM.
 *
 * @param that - Cheerio instance to render.
 * @param dom - The DOM to render. Defaults to `that`'s root.
 * @param options - Options for rendering.
 * @returns The rendered document.
 */
function render(
  that: CheerioAPI,
  dom: BasicAcceptedElems<AnyNode> | undefined,
  options: InternalOptions,
): string {
  if (!that) return '';

  return that(dom ?? that._root.children, null, undefined, options).toString();
}

/**
 * Checks if a passed object is an options object.
 *
 * @param dom - Object to check if it is an options object.
 * @param options - Options object.
 * @returns Whether the object is an options object.
 */
function isOptions(
  dom?: BasicAcceptedElems<AnyNode> | CheerioOptions | null,
  options?: CheerioOptions,
): dom is CheerioOptions {
  return (
    !options &&
    typeof dom === 'object' &&
    dom != null &&
    !('length' in dom) &&
    !('type' in dom)
  );
}

/**
 * Renders the document.
 *
 * @category Static
 * @param options - Options for the renderer.
 * @returns The rendered document.
 */
export function html(this: CheerioAPI, options?: CheerioOptions): string;
/**
 * Renders the document.
 *
 * @category Static
 * @param dom - Element to render.
 * @param options - Options for the renderer.
 * @returns The rendered document.
 */
export function html(
  this: CheerioAPI,
  dom?: BasicAcceptedElems<AnyNode>,
  options?: CheerioOptions,
): string;
export function html(
  this: CheerioAPI,
  dom?: BasicAcceptedElems<AnyNode> | CheerioOptions,
  options?: CheerioOptions,
): string {
  /*
   * Be flexible about parameters, sometimes we call html(),
   * with options as only parameter
   * check dom argument for dom element specific properties
   * assume there is no 'length' or 'type' properties in the options object
   */
  const toRender = isOptions(dom) ? ((options = dom), undefined) : dom;

  /*
   * Sometimes `$.html()` is used without preloading html,
   * so fallback non-existing options to the default ones.
   */
  const opts = {
    ...this?._options,
    ...flattenOptions(options),
  };

  return render(this, toRender, opts);
}

/**
 * Render the document as XML.
 *
 * @category Static
 * @param dom - Element to render.
 * @returns THe rendered document.
 */
export function xml(
  this: CheerioAPI,
  dom?: BasicAcceptedElems<AnyNode>,
): string {
  const options = { ...this._options, xmlMode: true };

  return render(this, dom, options);
}

/**
 * Render the document as text.
 *
 * This returns the `textContent` of the passed elements. The result will
 * include the contents of `<script>` and `<style>` elements. To avoid this, use
 * `.prop('innerText')` instead.
 *
 * @category Static
 * @param elements - Elements to render.
 * @returns The rendered document.
 */
export function text(
  this: CheerioAPI | void,
  elements?: ArrayLike<AnyNode>,
): string {
  const elems = elements ?? (this ? this.root() : []);

  let ret = '';

  for (let i = 0; i < elems.length; i++) {
    ret += textContent(elems[i]);
  }

  return ret;
}

/**
 * Parses a string into an array of DOM nodes. The `context` argument has no
 * meaning for Cheerio, but it is maintained for API compatibility with jQuery.
 *
 * @category Static
 * @param data - Markup that will be parsed.
 * @param context - Will be ignored. If it is a boolean it will be used as the
 *   value of `keepScripts`.
 * @param keepScripts - If false all scripts will be removed.
 * @returns The parsed DOM.
 * @alias Cheerio.parseHTML
 * @see {@link https://api.jquery.com/jQuery.parseHTML/}
 */
export function parseHTML(
  this: CheerioAPI,
  data: string,
  context?: unknown,
  keepScripts?: boolean,
): AnyNode[];
export function parseHTML(this: CheerioAPI, data?: '' | null): null;
export function parseHTML(
  this: CheerioAPI,
  data?: string | null,
  context?: unknown,
  keepScripts = typeof context === 'boolean' ? context : false,
): AnyNode[] | null {
  if (!data || typeof data !== 'string') {
    return null;
  }

  if (typeof context === 'boolean') {
    keepScripts = context;
  }

  const parsed = this.load(data, this._options, false);
  if (!keepScripts) {
    parsed('script').remove();
  }

  /*
   * The `children` array is used by Cheerio internally to group elements that
   * share the same parents. When nodes created through `parseHTML` are
   * inserted into previously-existing DOM structures, they will be removed
   * from the `children` array. The results of `parseHTML` should remain
   * constant across these operations, so a shallow copy should be returned.
   */
  return [...parsed.root()[0].children];
}

/**
 * Sometimes you need to work with the top-level root element. To query it, you
 * can use `$.root()`.
 *
 * @category Static
 * @example
 *
 * ```js
 * $.root().append('<ul id="vegetables"></ul>').html();
 * //=> <ul id="fruits">...</ul><ul id="vegetables"></ul>
 * ```
 *
 * @returns Cheerio instance wrapping the root node.
 * @alias Cheerio.root
 */
export function root(this: CheerioAPI): Cheerio<Document> {
  return this(this._root);
}

/**
 * Checks to see if the `contained` DOM element is a descendant of the
 * `container` DOM element.
 *
 * @category Static
 * @param container - Potential parent node.
 * @param contained - Potential child node.
 * @returns Indicates if the nodes contain one another.
 * @alias Cheerio.contains
 * @see {@link https://api.jquery.com/jQuery.contains/}
 */
export function contains(container: AnyNode, contained: AnyNode): boolean {
  // According to the jQuery API, an element does not "contain" itself
  if (contained === container) {
    return false;
  }

  /*
   * Step up the descendants, stopping when the root element is reached
   * (signaled by `.parent` returning a reference to the same object)
   */
  let next: AnyNode | null = contained;
  while (next && next !== next.parent) {
    next = next.parent;
    if (next === container) {
      return true;
    }
  }

  return false;
}

/**
 * Extract multiple values from a document, and store them in an object.
 *
 * @category Static
 * @param map - An object containing key-value pairs. The keys are the names of
 *   the properties to be created on the object, and the values are the
 *   selectors to be used to extract the values.
 * @returns An object containing the extracted values.
 */
export function extract<M extends ExtractMap>(
  this: CheerioAPI,
  map: M,
): ExtractedMap<M> {
  return this.root().extract(map);
}

type Writable<T> = { -readonly [P in keyof T]: T[P] };

/**
 * $.merge().
 *
 * @category Static
 * @param arr1 - First array.
 * @param arr2 - Second array.
 * @returns `arr1`, with elements of `arr2` inserted.
 * @alias Cheerio.merge
 * @see {@link https://api.jquery.com/jQuery.merge/}
 */
export function merge<T>(
  arr1: Writable<ArrayLike<T>>,
  arr2: ArrayLike<T>,
): ArrayLike<T> | undefined {
  if (!(isArrayLike(arr1) && isArrayLike(arr2))) {
    return;
  }
  let newLength = arr1.length;
  const len = +arr2.length;

  for (let i = 0; i < len; i++) {
    arr1[newLength++] = arr2[i];
  }
  arr1.length = newLength;
  return arr1;
}

/**
 * Checks if an object is array-like.
 *
 * @category Static
 * @param item - Item to check.
 * @returns Indicates if the item is array-like.
 */
function isArrayLike(item: unknown): item is ArrayLike<unknown> {
  if (Array.isArray(item)) {
    return true;
  }

  if (
    typeof item !== 'object' ||
    item === null ||
    !('length' in item) ||
    typeof item.length !== 'number' ||
    item.length < 0
  ) {
    return false;
  }

  for (let i = 0; i < item.length; i++) {
    if (!(i in item)) {
      return false;
    }
  }
  return true;
}
```

## File: `src/types.ts`
```typescript
/** @file Types used in signatures of Cheerio methods. */

type LowercaseLetters =
  | 'a'
  | 'b'
  | 'c'
  | 'd'
  | 'e'
  | 'f'
  | 'g'
  | 'h'
  | 'i'
  | 'j'
  | 'k'
  | 'l'
  | 'm'
  | 'n'
  | 'o'
  | 'p'
  | 'q'
  | 'r'
  | 's'
  | 't'
  | 'u'
  | 'v'
  | 'w'
  | 'x'
  | 'y'
  | 'z';

type AlphaNumeric =
  | LowercaseLetters
  | Uppercase<LowercaseLetters>
  | `${number}`;

type SelectorSpecial = '.' | '#' | ':' | '|' | '>' | '+' | '~' | '[';
/**
 * Type for identifying selectors. Allows us to "upgrade" queries using
 * selectors to return `Element`s.
 */
export type SelectorType =
  | `${SelectorSpecial}${AlphaNumeric}${string}`
  | `${AlphaNumeric}${string}`;

import type { AnyNode } from 'domhandler';
import type { Cheerio } from './cheerio.js';

/** Elements that can be passed to manipulation methods. */
export type BasicAcceptedElems<T extends AnyNode> = ArrayLike<T> | T | string;
/** Elements that can be passed to manipulation methods, including functions. */
export type AcceptedElems<T extends AnyNode> =
  | BasicAcceptedElems<T>
  | ((this: T, i: number, el: T) => BasicAcceptedElems<T>);

/** Function signature, for traversal methods. */
export type FilterFunction<T> = (this: T, i: number, el: T) => boolean;
/** Supported filter types, for traversal methods. */
export type AcceptedFilters<T> = string | FilterFunction<T> | T | Cheerio<T>;
```

## File: `src/utils.spec.ts`
```typescript
import { describe, expect, it } from 'vitest';
import * as utils from './utils.js';

describe('util functions', () => {
  it('camelCase function test', () => {
    expect(utils.camelCase('cheerio.js')).toBe('cheerioJs');
    expect(utils.camelCase('camel-case-')).toBe('camelCase');
    expect(utils.camelCase('__directory__')).toBe('_directory_');
    expect(utils.camelCase('_one-two.three')).toBe('OneTwoThree');
  });

  it('cssCase function test', () => {
    expect(utils.cssCase('camelCase')).toBe('camel-case');
    expect(utils.cssCase('jQuery')).toBe('j-query');
    expect(utils.cssCase('neverSayNever')).toBe('never-say-never');
    expect(utils.cssCase('CSSCase')).toBe('-c-s-s-case');
  });

  it('isHtml function test', () => {
    expect(utils.isHtml('<html>')).toBe(true);
    expect(utils.isHtml('\n<html>\n')).toBe(true);
    expect(utils.isHtml('#main')).toBe(false);
    expect(utils.isHtml('\n<p>foo<p>bar\n')).toBe(true);
    expect(utils.isHtml('dog<p>fox<p>cat')).toBe(true);
    expect(utils.isHtml('<p>fox<p>cat')).toBe(true);
    expect(utils.isHtml('\n<p>fox<p>cat\n')).toBe(true);
    expect(utils.isHtml('#<p>fox<p>cat#')).toBe(true);
    expect(utils.isHtml('<!-- comment -->')).toBe(true);
    expect(utils.isHtml('<!doctype html>')).toBe(true);
    expect(utils.isHtml('<123>')).toBe(false);
  });
});
```

## File: `src/utils.ts`
```typescript
import type { AnyNode } from 'domhandler';
import type { Cheerio } from './cheerio.js';

/**
 * Checks if an object is a Cheerio instance.
 *
 * @category Utils
 * @param maybeCheerio - The object to check.
 * @returns Whether the object is a Cheerio instance.
 */
export function isCheerio<T>(
  maybeCheerio: unknown,
): maybeCheerio is Cheerio<T> {
  return (maybeCheerio as Cheerio<T>).cheerio != null;
}

/**
 * Convert a string to camel case notation.
 *
 * @private
 * @category Utils
 * @param str - The string to be converted.
 * @returns String in camel case notation.
 */
export function camelCase(str: string): string {
  return str.replace(/[._-](\w|$)/g, (_, x) => (x as string).toUpperCase());
}

/**
 * Convert a string from camel case to "CSS case", where word boundaries are
 * described by hyphens ("-") and all characters are lower-case.
 *
 * @private
 * @category Utils
 * @param str - The string to be converted.
 * @returns String in "CSS case".
 */
export function cssCase(str: string): string {
  return str.replace(/[A-Z]/g, '-$&').toLowerCase();
}

/**
 * Iterate over each DOM element without creating intermediary Cheerio
 * instances.
 *
 * This is indented for use internally to avoid otherwise unnecessary memory
 * pressure introduced by _make.
 *
 * @category Utils
 * @param array - The array to iterate over.
 * @param fn - Function to call.
 * @returns The original instance.
 */
export function domEach<
  T extends AnyNode,
  Arr extends ArrayLike<T> = Cheerio<T>,
>(array: Arr, fn: (elem: T, index: number) => void): Arr {
  const len = array.length;
  for (let i = 0; i < len; i++) fn(array[i], i);
  return array;
}

const enum CharacterCode {
  LowerA = 97,
  LowerZ = 122,
  UpperA = 65,
  UpperZ = 90,
  Exclamation = 33,
}

/**
 * Check if string is HTML.
 *
 * Tests for a `<` within a string, immediate followed by a letter and
 * eventually followed by a `>`.
 *
 * @private
 * @category Utils
 * @param str - The string to check.
 * @returns Indicates if `str` is HTML.
 */
export function isHtml(str: string): boolean {
  if (typeof str !== 'string') {
    return false;
  }

  const tagStart = str.indexOf('<');

  if (tagStart === -1 || tagStart > str.length - 3) return false;

  const tagChar = str.charCodeAt(tagStart + 1) as CharacterCode;

  return (
    ((tagChar >= CharacterCode.LowerA && tagChar <= CharacterCode.LowerZ) ||
      (tagChar >= CharacterCode.UpperA && tagChar <= CharacterCode.UpperZ) ||
      tagChar === CharacterCode.Exclamation) &&
    str.includes('>', tagStart + 2)
  );
}
```

## File: `src/__fixtures__/fixtures.ts`
```typescript
import type { CheerioAPI } from '../load.js';
import { load } from '../load-parse.js';

/** A Cheerio instance with no content. */
export const cheerio: CheerioAPI = load([]);

export const fruits: string = [
  '<ul id="fruits">',
  '<li class="apple">Apple</li>',
  '<li class="orange">Orange</li>',
  '<li class="pear">Pear</li>',
  '</ul>',
].join('');

export const vegetables: string = [
  '<ul id="vegetables">',
  '<li class="carrot">Carrot</li>',
  '<li class="sweetcorn">Sweetcorn</li>',
  '</ul>',
].join('');

export const divcontainers: string = [
  '<div class="container">',
  '<div class="inner">First</div>',
  '<div class="inner">Second</div>',
  '</div>',
  '<div class="container">',
  '<div class="inner">Third</div>',
  '<div class="inner">Fourth</div>',
  '</div>',
  '<div id="new"><div>',
  '<div>\n\n<p><em><b></b></em></p>\n\n</div>',
  '</div>',
].join('');

export const chocolates: string = [
  '<ul id="chocolates">',
  '<li class="linth" data-highlight="Lindor" data-origin="swiss">Linth</li>',
  '<li class="frey" data-taste="sweet" data-best-collection="Mahony">Frey</li>',
  '<li class="cailler">Cailler</li>',
  '</ul>',
].join('');

export const drinks: string = [
  '<ul id="drinks">',
  '<li class="beer">Beer</li>',
  '<li class="juice">Juice</li>',
  '<li class="milk">Milk</li>',
  '<li class="water">Water</li>',
  '<li class="cider">Cider</li>',
  '</ul>',
].join('');

export const food: string = [
  '<ul id="food">',
  fruits,
  vegetables,
  '</ul>',
].join('');

export const eleven = `
<html>
  <body>
    <ul>
      <li>One</li>
      <li>Two</li>
      <li class="blue sel">Three</li>
      <li class="red">Four</li>
    </ul>

    <ul>
      <li class="red">Five</li>
      <li>Six</li>
      <li class="blue">Seven</li>
    </ul>

    <ul>
      <li>Eight</li>
      <li class="red sel">Nine</li>
      <li>Ten</li>
      <li class="sel">Eleven</li>
    </ul>
  </body>
</html>
`;

export const unwrapspans: string = [
  '<div id=unwrap style="display: none;">',
  '<div id=unwrap1><span class=unwrap>a</span><span class=unwrap>b</span></div>',
  '<div id=unwrap2><span class=unwrap>c</span><span class=unwrap>d</span></div>',
  '<div id=unwrap3><b><span class="unwrap unwrap3">e</span></b><b><span class="unwrap unwrap3">f</span></b></div>',
  '</div>',
].join('');

export const inputs: string = [
  '<button id="btn-value" value="button">Button</button>',
  '<button id="btn-valueless">Button</button>',
  '<select id="one"><option value="option_not_selected">Option not selected</option><option value="option_selected" selected>Option selected</option></select>',
  '<select id="one-valueless"><option>Option not selected</option><option selected>Option selected</option></select>',
  '<select id="one-html-entity"><option>Option not selected</option><option selected>Option &lt;selected&gt;</option></select>',
  '<select id="one-nested"><option>Option not selected</option><option selected>Option <span>selected</span></option></select>',
  '<input type="text" value="input_text" />',
  '<input type="checkbox" name="checkbox_off" value="off" /><input type="checkbox" name="checkbox_on" value="on" checked />',
  '<input type="checkbox" name="checkbox_valueless" />',
  '<input type="radio" value="off" name="radio" /><input type="radio" name="radio" value="on" checked />',
  '<input type="radio" value="off" name="radio[brackets]" /><input type="radio" name="radio[brackets]" value="on" checked />',
  '<input type="radio" name="radio_valueless" />',
  '<select id="multi" multiple><option value="1">1</option><option value="2" selected>2</option><option value="3" selected>3</option><option value="4">4</option></select>',
  '<select id="multi-valueless" multiple><option>1</option><option selected>2</option><option selected>3</option><option>4</option></select>',
].join('');

export const text: string = [
  '<p>Apples, <b>oranges</b> and pears.</p>',
  '<p>Carrots and <!-- sweetcorn --></p>',
].join('');

export const forms: string = [
  '<form id="simple"><input type="text" name="fruit" value="Apple" /></form>',
  '<form id="nested"><div><input type="text" name="fruit" value="Apple" /></div><input type="text" name="vegetable" value="Carrot" /></form>',
  '<form id="disabled"><input type="text" name="fruit" value="Apple" disabled /></form>',
  '<form id="submit"><input type="text" name="fruit" value="Apple" /><input type="submit" name="submit" value="Submit" /></form>',
  '<form id="select"><select name="fruit"><option value="Apple">Apple</option><option value="Orange" selected>Orange</option></select></form>',
  '<form id="unnamed"><input type="text" name="fruit" value="Apple" /><input type="text" value="Carrot" /></form>',
  '<form id="multiple"><select name="fruit" multiple><option value="Apple" selected>Apple</option><option value="Orange" selected>Orange</option><option value="Carrot">Carrot</option></select></form>',
  '<form id="textarea"><textarea name="fruits">Apple\nOrange</textarea></form>',
  '<form id="spaces"><input type="text" name="fruit" value="Blood orange" /></form>',
].join('');

export const noscript: string = [
  '</body>',
  '<noscript>',
  '<!-- anchor linking to external file -->',
  '<a href="https://github.com/cheeriojs/cheerio">External Link</a>',
  '</noscript>',
  '<p>Rocks!</p>',
  '</body>',
].join('');

export const script: string = [
  '<div>',
  '<a>A</a>',
  '<script>',
  '  var foo = "bar";',
  '</script>',
  '<b>B</b>',
  '</div>',
].join('');

export const mixedText = '<a>1</a>TEXT<b>2</b>';
```

## File: `src/__tests__/deprecated.spec.ts`
```typescript
/**
 * This file includes tests for deprecated APIs. The methods are expected to be
 * removed in the next major release of Cheerio, but their stability should be
 * maintained until that time.
 */
import { beforeEach, describe, expect, it } from 'vitest';
import { cheerio, food, fruits } from '../__fixtures__/fixtures.js';

describe('deprecated APIs', () => {
  describe('cheerio module', () => {
    describe('.parseHTML', () => {
      it('(html) : should preserve content', () => {
        const html = '<div>test div</div>';
        expect(cheerio(cheerio.parseHTML(html)[0]).html()).toBe('test div');
      });
    });

    describe('.merge', () => {
      it('should be a function', () => {
        expect(typeof cheerio.merge).toBe('function');
      });

      // #1674 - merge, wont accept Cheerio object
      it('should be a able merge array and cheerio object', () => {
        const ret = cheerio.merge<unknown>(cheerio(), ['elem1', 'elem2']);
        expect(typeof ret).toBe('object');
        expect(ret).toHaveLength(2);
      });

      it('(arraylike, arraylike) : should modify the first array, but not the second', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [4, 5, 6];
        const ret = cheerio.merge(arr1, arr2);

        expect(typeof ret).toBe('object');
        expect(Array.isArray(ret)).toBe(true);
        expect(ret).toBe(arr1);
        expect(arr1).toHaveLength(6);
        expect(arr2).toHaveLength(3);
      });

      it('(arraylike, arraylike) : should handle objects that arent arrays, but are arraylike', () => {
        const arr1: ArrayLike<string> = {
          length: 3,
          0: 'a',
          1: 'b',
          2: 'c',
        };
        const arr2 = {
          length: 3,
          0: 'd',
          1: 'e',
          2: 'f',
        };

        cheerio.merge(arr1, arr2);
        expect(arr1).toHaveLength(6);
        expect(arr1[3]).toBe('d');
        expect(arr1[4]).toBe('e');
        expect(arr1[5]).toBe('f');
        expect(arr2).toHaveLength(3);
      });

      it('(?, ?) : should gracefully reject invalid inputs', () => {
        expect(cheerio.merge([4], 3 as never)).toBeUndefined();
        expect(cheerio.merge({} as never, {} as never)).toBeUndefined();
        expect(cheerio.merge([], {} as never)).toBeUndefined();
        expect(cheerio.merge({} as never, [])).toBeUndefined();

        const fakeArray = { length: 3, 0: 'a', 1: 'b', 3: 'd' };
        expect(cheerio.merge(fakeArray, [])).toBeUndefined();
        expect(cheerio.merge([], fakeArray)).toBeUndefined();

        expect(cheerio.merge({ length: '7' } as never, [])).toBeUndefined();
        expect(cheerio.merge({ length: -1 }, [])).toBeUndefined();
      });

      it('(?, ?) : should no-op on invalid inputs', () => {
        const fakeArray1 = { length: 3, 0: 'a', 1: 'b', 3: 'd' };
        cheerio.merge(fakeArray1, []);
        expect(fakeArray1).toHaveLength(3);
        expect(fakeArray1[0]).toBe('a');
        expect(fakeArray1[1]).toBe('b');
        expect(fakeArray1[3]).toBe('d');
        cheerio.merge([], fakeArray1);
        expect(fakeArray1).toHaveLength(3);
        expect(fakeArray1[0]).toBe('a');
        expect(fakeArray1[1]).toBe('b');
        expect(fakeArray1[3]).toBe('d');
      });
    });

    describe('.contains', () => {
      let $: typeof cheerio;

      beforeEach(() => {
        $ = cheerio.load(food);
      });

      it('(container, contained) : should correctly detect the provided element', () => {
        const $food = $('#food');
        const $fruits = $('#fruits');
        const $apple = $('.apple');

        expect(cheerio.contains($food[0], $fruits[0])).toBe(true);
        expect(cheerio.contains($food[0], $apple[0])).toBe(true);
      });

      it('(container, other) : should not detect elements that are not contained', () => {
        const $fruits = $('#fruits');
        const $vegetables = $('#vegetables');
        const $apple = $('.apple');

        expect(cheerio.contains($vegetables[0], $apple[0])).toBe(false);
        expect(cheerio.contains($fruits[0], $vegetables[0])).toBe(false);
        expect(cheerio.contains($vegetables[0], $fruits[0])).toBe(false);
        expect(cheerio.contains($fruits[0], $fruits[0])).toBe(false);
        expect(cheerio.contains($vegetables[0], $vegetables[0])).toBe(false);
      });
    });

    describe('.root', () => {
      it('returns an empty selection', () => {
        const $empty = cheerio.root();
        expect($empty).toHaveLength(1);
        expect($empty[0].children).toHaveLength(0);
      });
    });
  });

  describe('Cheerio function', () => {
    it('.load', () => {
      const $1 = cheerio.load(fruits);
      const $2 = $1.load('<div><p>Some <a>text</a>.</p></div>');

      expect($2('a')).toHaveLength(1);
    });

    /**
     * The `.html` static method defined on the "loaded" Cheerio factory
     * function is deprecated.
     *
     * In order to promote consistency with the jQuery library, users are
     * encouraged to instead use the instance method of the same name.
     *
     * @example
     *
     * ```js
     * const $ = cheerio.load('<h1>Hello, <span>world</span>.</h1>');
     *
     * $('h1').html();
     * //=> 'Hello, <span>world</span>.'
     * ```
     *
     * @example <caption>To render the markup of an entire document, invoke the
     * `html` function exported by the Cheerio module with a "root"
     * selection.</caption>
     *
     * ```js
     * cheerio.html($.root());
     * //=> '<html><head></head><body><h1>Hello, <span>world</span>.</h1></body></html>'
     * ```
     */
    describe('.html - deprecated API', () => {
      it('() : of empty cheerio object should return null', () => {
        /*
         * Note: the direct invocation of the Cheerio constructor function is
         * also deprecated.
         */
        const $ = cheerio();
        expect($.html()).toBe(null);
      });

      it('(selector) : should return the outerHTML of the selected element', () => {
        const $ = cheerio.load(fruits);
        expect($.html('.pear')).toBe('<li class="pear">Pear</li>');
      });
    });

    /**
     * The `.xml` static method defined on the "loaded" Cheerio factory function
     * is deprecated. Users are encouraged to instead use the `xml` function
     * exported by the Cheerio module.
     *
     * @example
     *
     * ```js
     * cheerio.xml($.root());
     * ```
     */
    describe('.xml  - deprecated API', () => {
      it('() :  renders XML', () => {
        const $ = cheerio.load('<foo></foo>', { xmlMode: true });
        expect($.xml()).toBe('<foo/>');
      });
    });

    /**
     * The `.text` static method defined on the "loaded" Cheerio factory
     * function is deprecated.
     *
     * In order to promote consistency with the jQuery library, users are
     * encouraged to instead use the instance method of the same name.
     *
     * @example
     *
     * ```js
     * const $ = cheerio.load('<h1>Hello, <span>world</span>.</h1>');
     * $('h1').text();
     * //=> 'Hello, world.'
     * ```
     *
     * @example <caption>To render the text content of an entire document,
     * invoke the `text` function exported by the Cheerio module with a "root"
     * selection. </caption>
     *
     * ```js
     * cheerio.text($.root());
     * //=> 'Hello, world.'
     * ```
     */
    describe('.text  - deprecated API', () => {
      it('(cheerio object) : should return the text contents of the specified elements', () => {
        const $ = cheerio.load('<a>This is <em>content</em>.</a>');
        expect($.text($('a'))).toBe('This is content.');
      });

      it('(cheerio object) : should omit comment nodes', () => {
        const $ = cheerio.load(
          '<a>This is <!-- a comment --> not a comment.</a>',
        );
        expect($.text($('a'))).toBe('This is  not a comment.');
      });

      it('(cheerio object) : should include text contents of children recursively', () => {
        const $ = cheerio.load(
          '<a>This is <div>a child with <span>another child and <!-- a comment --> not a comment</span> followed by <em>one last child</em> and some final</div> text.</a>',
        );
        expect($.text($('a'))).toBe(
          'This is a child with another child and  not a comment followed by one last child and some final text.',
        );
      });

      it('() : should return the rendered text content of the root', () => {
        const $ = cheerio.load(
          '<a>This is <div>a child with <span>another child and <!-- a comment --> not a comment</span> followed by <em>one last child</em> and some final</div> text.</a>',
        );
        expect($.text()).toBe(
          'This is a child with another child and  not a comment followed by one last child and some final text.',
        );
      });

      it('(cheerio object) : should not omit script tags', () => {
        const $ = cheerio.load('<script>console.log("test")</script>');
        expect($.text()).toBe('console.log("test")');
      });

      it('(cheerio object) : should omit style tags', () => {
        const $ = cheerio.load(
          '<style type="text/css">.cf-hidden { display: none; }</style>',
        );
        expect($.text()).toBe('.cf-hidden { display: none; }');
      });
    });
  });
});
```

## File: `src/__tests__/xml.spec.ts`
```typescript
import { describe, expect, it } from 'vitest';
import { load } from '../index.js';
import type { CheerioOptions } from '../options.js';

function xml(str: string, options?: CheerioOptions) {
  options = { xml: true, ...options };
  const $ = load(str, options);
  return $.xml();
}

function dom(str: string, options?: CheerioOptions) {
  const $ = load('', options);
  return $(str).html();
}

describe('render', () => {
  describe('(xml)', () => {
    it('should render <media:thumbnail /> tags correctly', () => {
      const str =
        '<media:thumbnail url="http://www.foo.com/keyframe.jpg" width="75" height="50" time="12:05:01.123" />';
      expect(xml(str)).toBe(
        '<media:thumbnail url="http://www.foo.com/keyframe.jpg" width="75" height="50" time="12:05:01.123"/>',
      );
    });

    it('should render <link /> tags (RSS) correctly', () => {
      const str = '<link>http://www.github.com/</link>';
      expect(xml(str)).toBe('<link>http://www.github.com/</link>');
    });

    it('should escape entities', () => {
      const str = '<tag attr="foo &amp; bar"/>';
      expect(xml(str)).toBe(str);
    });

    it('should render HTML as XML', () => {
      const $ = load('<foo></foo>', null, false);
      expect($.xml()).toBe('<foo/>');
    });
  });

  describe('(dom)', () => {
    it('should not keep camelCase for new nodes', () => {
      const str = '<g><someElem someAttribute="something">hello</someElem></g>';
      expect(dom(str, { xml: false })).toBe(
        '<someelem someattribute="something">hello</someelem>',
      );
    });

    it('should keep camelCase for new nodes', () => {
      const str = '<g><someElem someAttribute="something">hello</someElem></g>';
      expect(dom(str, { xml: true })).toBe(
        '<someElem someAttribute="something">hello</someElem>',
      );
    });

    it('should maintain the parsing options of distinct contexts independently', () => {
      const str = '<g><someElem someAttribute="something">hello</someElem></g>';
      const $ = load('', { xml: false });

      expect($(str).html()).toBe(
        '<someelem someattribute="something">hello</someelem>',
      );
    });
  });
});
```

## File: `src/api/attributes.spec.ts`
```typescript
import type { Element } from 'domhandler';
import { beforeEach, describe, expect, it } from 'vitest';
import {
  cheerio,
  chocolates,
  food,
  fruits,
  inputs,
  mixedText,
  script,
  vegetables,
} from '../__fixtures__/fixtures.js';
import { type Cheerio, type CheerioAPI, load } from '../index.js';

function withClass(attr: string) {
  return cheerio(`<div class="${attr}"></div>`);
}

describe('$(...)', () => {
  describe('.attr', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(fruits);
    });

    it('() : should get all the attributes', () => {
      const attrs = $('ul').attr();
      expect(attrs).toHaveProperty('id', 'fruits');
    });

    it('(invalid key) : invalid attr should get undefined', () => {
      const attr = $('.apple').attr('lol');
      expect(attr).toBeUndefined();
    });

    it('(valid key) : valid attr should get value', () => {
      const cls = $('.apple').attr('class');
      expect(cls).toBe('apple');
    });

    it('(valid key) : valid attr should get name when boolean', () => {
      const attr = $('<input name=email autofocus>').attr('autofocus');
      expect(attr).toBe('autofocus');
    });

    it('(key, value) : should set one attr', () => {
      const $pear = $('.pear').attr('id', 'pear');
      expect($('#pear')).toHaveLength(1);
      expect($pear).toBeInstanceOf($);
    });

    it('(key, value) : should set multiple attr', () => {
      const $el = cheerio('<div></div> <div></div>').attr(
        'class',
        'pear',
      ) as Cheerio<Element>;

      expect($el[0].attribs).toHaveProperty('class', 'pear');
      expect($el[1].attribs).toBeUndefined();
      expect($el[2].attribs).toHaveProperty('class', 'pear');
    });

    it('(key, value) : should return an empty object for an empty object', () => {
      const $src = $().attr('key', 'value');
      expect($src.length).toBe(0);
      expect($src[0]).toBeUndefined();
    });

    it('(map) : object map should set multiple attributes', () => {
      $('.apple').attr({
        id: 'apple',
        style: 'color:red;',
        'data-url': 'http://apple.com',
      });
      const attrs = $('.apple').attr();
      expect(attrs).toHaveProperty('id', 'apple');
      expect(attrs).toHaveProperty('style', 'color:red;');
      expect(attrs).toHaveProperty('data-url', 'http://apple.com');
    });

    it('(map, val) : should throw with wrong combination of arguments', () => {
      expect(() =>
        $('.apple').attr(
          {
            id: 'apple',
            style: 'color:red;',
            'data-url': 'http://apple.com',
          } as never,
          () => '',
        ),
      ).toThrow('Bad combination of arguments.');
    });

    it('(key, function) : should call the function and update the attribute with the return value', () => {
      const $fruits = $('#fruits');
      $fruits.attr('id', (index, value) => {
        expect(index).toBe(0);
        expect(value).toBe('fruits');
        return 'ninja';
      });
      const attrs = $fruits.attr();
      expect(attrs).toHaveProperty('id', 'ninja');
    });

    it('(key, function) : should ignore text nodes', () => {
      const $text = $(mixedText);
      $text.attr('class', () => 'ninja');
      const className = $text.attr('class');
      expect(className).toBe('ninja');
    });

    it('(key, value) : should correctly encode then decode unsafe values', () => {
      const $apple = $('.apple');
      $apple.attr(
        'href',
        'http://github.com/"><script>alert("XSS!")</script><br',
      );
      expect($apple.attr('href')).toBe(
        'http://github.com/"><script>alert("XSS!")</script><br',
      );

      $apple.attr(
        'href',
        'http://github.com/"><script>alert("XSS!")</script><br',
      );
      expect($apple.html()).not.toContain('<script>alert("XSS!")</script>');
    });

    it('(key, value) : should coerce values to a string', () => {
      const $apple = $('.apple');
      $apple.attr('data-test', 1 as never);
      expect($apple[0].attribs['data-test']).toBe('1');
      expect($apple.attr('data-test')).toBe('1');
    });

    it('(key, value) : handle removed boolean attributes', () => {
      const $apple = $('.apple');
      $apple.attr('autofocus', 'autofocus');
      expect($apple.attr('autofocus')).toBe('autofocus');
      $apple.removeAttr('autofocus');
      expect($apple.attr('autofocus')).toBeUndefined();
    });

    it('(key, value) : should remove non-boolean attributes with names or values similar to boolean ones', () => {
      const $apple = $('.apple');
      $apple.attr('data-autofocus', 'autofocus');
      expect($apple.attr('data-autofocus')).toBe('autofocus');
      $apple.removeAttr('data-autofocus');
      expect($apple.attr('data-autofocus')).toBeUndefined();
    });

    it('(key, value) : should remove attributes when called with null value', () => {
      const $pear = $('.pear').attr('autofocus', 'autofocus');
      expect($pear.attr('autofocus')).toBe('autofocus');
      $pear.attr('autofocus', null);
      expect($pear.attr('autofocus')).toBeUndefined();
    });

    it('(map) : should remove attributes with null values', () => {
      const $pear = $('.pear').attr({
        autofocus: 'autofocus',
        style: 'color:red',
      });
      expect($pear.attr('autofocus')).toBe('autofocus');
      expect($pear.attr('style')).toBe('color:red');
      $pear.attr({ autofocus: null, style: 'color:blue' });
      expect($pear.attr('autofocus')).toBeUndefined();
      expect($pear.attr('style')).toBe('color:blue');
    });

    it('(chaining) setting value and calling attr returns result', () => {
      const pearAttr = $('.pear').attr('foo', 'bar').attr('foo');
      expect(pearAttr).toBe('bar');
    });

    it('(chaining) setting attr to null returns a $', () => {
      const $pear = $('.pear').attr('foo', null);
      expect($pear).toBeInstanceOf($);
    });

    it('(chaining) setting attr to undefined returns a $', () => {
      const $pear = $('.pear').attr('foo', undefined);
      expect($('.pear')).toHaveLength(1);
      expect($('.pear').attr('foo')).toBeUndefined();
      expect($pear).toBeInstanceOf($);
    });

    it("(bool) shouldn't treat boolean attributes differently in XML mode", () => {
      const $xml = $.load('<input checked=checked disabled=yes />', {
        xml: true,
      })('input');

      expect($xml.attr('checked')).toBe('checked');
      expect($xml.attr('disabled')).toBe('yes');
    });
  });

  describe('.prop', () => {
    let $: CheerioAPI;
    let checkbox: Cheerio<Element>;

    beforeEach(() => {
      $ = load(inputs);
      checkbox = $('input[name=checkbox_on]');
    });

    it('(valid key) : valid prop should get value', () => {
      expect(checkbox.prop('checked')).toBe(true);
      checkbox.css('display', 'none');
      expect(checkbox.prop('style')).toHaveProperty('display', 'none');
      expect(checkbox.prop('style')).toHaveLength(1);
      expect(checkbox.prop('style')).toContain('display');
      expect(checkbox.prop('tagName')).toBe('INPUT');
      expect(checkbox.prop('nodeName')).toBe('INPUT');
    });

    it('(valid key) : should return on empty collection', () => {
      expect($(undefined).prop('checked')).toBeUndefined();
      expect($(undefined).prop('style')).toBeUndefined();
      expect($(undefined).prop('tagName')).toBeUndefined();
      expect($(undefined).prop('nodeName')).toBeUndefined();
    });

    it('(invalid key) : invalid prop should get undefined', () => {
      expect(checkbox.prop('lol')).toBeUndefined();
      expect(checkbox.prop(4 as never)).toBeUndefined();
      expect(checkbox.prop(true as never)).toBeUndefined();
    });

    it('(key, value) : should set prop', () => {
      expect(checkbox.prop('checked')).toBe(true);
      checkbox.prop('checked', false);
      expect(checkbox.prop('checked')).toBe(false);
      checkbox.prop('checked', true);
      expect(checkbox.prop('checked')).toBe(true);
    });

    it('(key, value) : should update attribute', () => {
      expect(checkbox.prop('checked')).toBe(true);
      expect(checkbox.attr('checked')).toBe('checked');
      checkbox.prop('checked', false);
      expect(checkbox.prop('checked')).toBe(false);
      expect(checkbox.attr('checked')).toBeUndefined();
      checkbox.prop('checked', true);
      expect(checkbox.prop('checked')).toBe(true);
      expect(checkbox.attr('checked')).toBe('checked');
    });

    it('(key, value) : should update namespace', () => {
      const imgs = $('<img>\n\n<img>\n\n<img>');
      const nsHtml = 'http://www.w3.org/1999/xhtml';
      imgs.prop('src', '#').prop('namespace', nsHtml);
      expect(imgs.prop('namespace')).toBe(nsHtml);
      imgs.prop('attribs', null);
      expect(imgs.prop('src')).toBeUndefined();
      expect(imgs.prop('data-foo')).toBeUndefined();
    });

    it('(key, value) : should ignore empty collection', () => {
      expect($(undefined).prop('checked')).toBeUndefined();
      $(undefined).prop('checked', true);
      expect($(undefined).prop('checked')).toBeUndefined();
    });

    it('(map) : object map should set multiple props', () => {
      checkbox.prop({
        id: 'check',
        checked: false,
      });
      expect(checkbox.prop('id')).toBe('check');
      expect(checkbox.prop('checked')).toBe(false);
    });

    it('(map, val) : should throw with wrong combination of arguments', () => {
      expect(() =>
        $('.apple').prop(
          {
            id: 'check',
            checked: false,
          } as never,
          () => '',
        ),
      ).toThrow('Bad combination of arguments.');
    });

    it('(key, function) : should call the function and update the prop with the return value', () => {
      checkbox.prop('checked', (index, value) => {
        expect(index).toBe(0);
        expect(value).toBe(true);
        return false;
      });
      expect(checkbox.prop('checked')).toBe(false);
    });

    it('(key, value) : should support chaining after setting props', () => {
      expect(checkbox.prop('checked', false)).toBe(checkbox);
    });

    it('(invalid element/tag) : prop should return undefined', () => {
      expect($(undefined).prop('prop')).toBeUndefined();
      expect($(null as never).prop('prop')).toBeUndefined();
    });

    it('("href") : should resolve links with `baseURI`', () => {
      const $ = load(
        `
          <a id="1" href="http://example.org">example1</a>
          <a id="2" href="//example.org">example2</a>
          <a id="3" href="/example.org">example3</a>
          <a id="4" href="example.org">example4</a>
        `,
        { baseURI: 'http://example.com/page/1' },
      );

      expect($('#1').prop('href')).toBe('http://example.org/');
      expect($('#2').prop('href')).toBe('http://example.org/');
      expect($('#3').prop('href')).toBe('http://example.com/example.org');
      expect($('#4').prop('href')).toBe('http://example.com/page/example.org');

      expect($(undefined).prop('href')).toBeUndefined();
    });

    it('("href") : should skip values without an href', () => {
      const $ = load('<a id="1">example1</a>');
      expect($('#1').prop('href')).toBeUndefined();
    });

    it('("src") : should resolve links with `baseURI`', () => {
      const $ = load(
        `
          <img id="1" src="http://example.org/image.png">
          <iframe id="2" src="//example.org/page.html"></iframe>
          <audio id="3" src="/example.org/song.mp3"></audio>
          <source id="4" src="example.org/image.png">
        `,
        { baseURI: 'http://example.com/page/1' },
      );

      expect($('#1').prop('src')).toBe('http://example.org/image.png');
      expect($('#2').prop('src')).toBe('http://example.org/page.html');
      expect($('#3').prop('src')).toBe(
        'http://example.com/example.org/song.mp3',
      );
      expect($('#4').prop('src')).toBe(
        'http://example.com/page/example.org/image.png',
      );

      expect($(undefined).prop('src')).toBeUndefined();
    });

    it('("outerHTML") : should render properly', () => {
      const outerHtml = '<div><a></a></div>';
      const $a = $(outerHtml);

      expect($a.prop('outerHTML')).toBe(outerHtml);

      expect($(undefined).prop('outerHTML')).toBeUndefined();
    });

    it('("outerHTML") : should support root nodes', () => {
      const $ = load('<div></div>');
      expect($.root().prop('outerHTML')).toBe(
        '<html><head></head><body><div></div></body></html>',
      );
    });

    it('("innerHTML") : should render properly', () => {
      const $a = $('<div><a></a></div>');

      expect($a.prop('innerHTML')).toBe('<a></a>');

      expect($(undefined).prop('innerHTML')).toBeUndefined();
    });

    it('("textContent") : should render properly', () => {
      expect($('select').children().prop('textContent')).toBe(
        'Option not selected',
      );

      expect($(script).prop('textContent')).toBe('A  var foo = "bar";B');

      expect($(undefined).prop('textContent')).toBeUndefined();
    });

    it('("textContent") : should include style and script tags', () => {
      const $ = load(
        '<body>Welcome <div>Hello, testing text function,<script>console.log("hello")</script></div><style type="text/css">.cf-hidden { display: none; }</style>End of message</body>',
      );
      expect($('body').prop('textContent')).toBe(
        'Welcome Hello, testing text function,console.log("hello").cf-hidden { display: none; }End of message',
      );
      expect($('style').prop('textContent')).toBe(
        '.cf-hidden { display: none; }',
      );
      expect($('script').prop('textContent')).toBe('console.log("hello")');
    });

    it('("innerText") : should render properly', () => {
      expect($('select').children().prop('innerText')).toBe(
        'Option not selected',
      );

      expect($(script).prop('innerText')).toBe('AB');

      expect($(undefined).prop('innerText')).toBeUndefined();
    });

    it('("innerText") : should omit style and script tags', () => {
      const $ = load(
        '<body>Welcome <div>Hello, testing text function,<script>console.log("hello")</script></div><style type="text/css">.cf-hidden { display: none; }</style>End of message</body>',
      );
      expect($('body').prop('innerText')).toBe(
        'Welcome Hello, testing text function,End of message',
      );
      expect($('style').prop('innerText')).toBe('');
      expect($('script').prop('innerText')).toBe('');
    });

    it('(inherited properties) : prop should support inherited properties', () => {
      expect($('select').prop('childNodes')).toBe($('select')[0].childNodes);
    });

    it('(key) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      expect($text($body[1]).prop('tagName')).toBeUndefined();

      $body.prop('test-name', () => 'tester');
      expect($text('body').html()).toBe(
        '<a test-name="tester">1</a>TEXT<b test-name="tester">2</b>',
      );
    });

    it("(bool) shouldn't treat boolean attributes differently in XML mode", () => {
      const $xml = $.load('<input checked=checked disabled=yes />', {
        xml: true,
      })('input');

      expect($xml.prop('checked')).toBe('checked');
      expect($xml.prop('disabled')).toBe('yes');
    });
  });

  describe('.data', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(chocolates);
    });

    it('() : should get all data attributes initially declared in the markup', () => {
      const data = $('.linth').data();
      expect(data).toStrictEqual({
        highlight: 'Lindor',
        origin: 'swiss',
      });
    });

    it('() : should get all data set via `data`', () => {
      const $el = cheerio('<div>');
      $el.data('a', 1);
      $el.data('b', 2);

      expect($el.data()).toStrictEqual({
        a: 1,
        b: 2,
      });
    });

    it('() : should get all data attributes initially declared in the markup merged with all data additionally set via `data`', () => {
      const $el = cheerio('<div data-a="a" data-b="b">');
      $el.data('b', 'b-modified');
      $el.data('c', 'c');

      expect($el.data()).toStrictEqual({
        a: 'a',
        b: 'b-modified',
        c: 'c',
      });
    });

    it('() : no data attribute should return an empty object', () => {
      const data = $('.cailler').data();
      expect(Object.keys(data)).toHaveLength(0);
      expect($('.free').data()).toBeUndefined();
    });

    it('(invalid key) : invalid data attribute should return `undefined`', () => {
      const data = $('.frey').data('lol');
      expect(data).toBeUndefined();
    });

    it('(valid key) : valid data attribute should get value', () => {
      const highlight = $('.linth').data('highlight');
      const origin = $('.linth').data('origin');

      expect(highlight).toBe('Lindor');
      expect(origin).toBe('swiss');
    });

    it('(key) : should translate camel-cased key values to hyphen-separated versions', () => {
      const $el = cheerio(
        '<div data--three-word-attribute="a" data-foo-Bar_BAZ-="b">',
      );

      expect($el.data('ThreeWordAttribute')).toBe('a');
      expect($el.data('fooBar_baz-')).toBe('b');
    });

    it('(key) : should retrieve object values', () => {
      const data = {};
      const $el = cheerio('<div>');

      $el.data('test', data);

      expect($el.data('test')).toBe(data);
    });

    it('(key) : should parse JSON data derived from the markup', () => {
      const $el = cheerio('<div data-json="[1, 2, 3]">');

      expect($el.data('json')).toStrictEqual([1, 2, 3]);
    });

    it('(key) : should not parse JSON data set via the `data` API', () => {
      const $el = cheerio('<div>');
      $el.data('json', '[1, 2, 3]');

      expect($el.data('json')).toBe('[1, 2, 3]');
    });

    // See https://api.jquery.com/data/ and https://bugs.jquery.com/ticket/14523
    it('(key) : should ignore the markup value after the first access', () => {
      const $el = cheerio('<div data-test="a">');

      expect($el.data('test')).toBe('a');

      $el.attr('data-test', 'b');

      expect($el.data('test')).toBe('a');
    });

    it('(key) : should recover from malformed JSON', () => {
      const $el = cheerio('<div data-custom="{{templatevar}}">');

      expect($el.data('custom')).toBe('{{templatevar}}');
    });

    it('("") : should accept the empty string as a name', () => {
      const $el = cheerio('<div data-="a">');

      expect($el.data('')).toBe('a');
    });

    it('(hyphen key) : data addribute with hyphen should be camelized ;-)', () => {
      const data = $('.frey').data();
      expect(data).toStrictEqual({
        taste: 'sweet',
        bestCollection: 'Mahony',
      });
    });

    it('(key, value) : should set data attribute', () => {
      // Adding as object.
      const a = $('.frey').data({
        balls: 'giandor',
      });
      // Adding as string.
      const b = $('.linth').data('snack', 'chocoletti');

      expect(() => {
        a.data(4 as never, 'throw');
      }).not.toThrow();
      expect(a.data('balls')).toStrictEqual('giandor');
      expect(b.data('snack')).toStrictEqual('chocoletti');
    });

    it('(key, value) : should set data for all elements in the selection', () => {
      $('li').data('foo', 'bar');

      expect($('li').eq(0).data('foo')).toStrictEqual('bar');
      expect($('li').eq(1).data('foo')).toStrictEqual('bar');
      expect($('li').eq(2).data('foo')).toStrictEqual('bar');
    });

    it('(map) : object map should set multiple data attributes', () => {
      const { data } = $('.linth').data({
        id: 'Cailler',
        flop: 'Pippilotti Rist',
        top: 'Frigor',
        url: 'http://www.cailler.ch/',
      })[0] as never;

      expect(data).toHaveProperty('id', 'Cailler');
      expect(data).toHaveProperty('flop', 'Pippilotti Rist');
      expect(data).toHaveProperty('top', 'Frigor');
      expect(data).toHaveProperty('url', 'http://www.cailler.ch/');
    });

    describe('(attr) : data-* attribute type coercion :', () => {
      it('boolean', () => {
        const $el = cheerio('<div data-bool="true">');
        expect($el.data('bool')).toBe(true);
      });

      it('number', () => {
        const $el = cheerio('<div data-number="23">');
        expect($el.data('number')).toBe(23);
      });

      it('number (scientific notation is not coerced)', () => {
        const $el = cheerio('<div data-sci="1E10">');
        expect($el.data('sci')).toBe('1E10');
      });

      it('null', () => {
        const $el = cheerio('<div data-null="null">');
        expect($el.data('null')).toBe(null);
      });

      it('object', () => {
        const $el = cheerio('<div data-obj=\'{ "a": 45 }\'>');
        expect($el.data('obj')).toStrictEqual({ a: 45 });
      });

      it('array', () => {
        const $el = cheerio('<div data-array="[1, 2, 3]">');
        expect($el.data('array')).toStrictEqual([1, 2, 3]);
      });
    });

    it('(key, value) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.data('snack', 'chocoletti');

      expect($text('b').data('snack')).toBe('chocoletti');
    });
  });

  describe('.val', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(inputs);
    });

    it('(): on div should get undefined', () => {
      expect($('<div>').val()).toBeUndefined();
    });

    it('(): on button should get value', () => {
      const val = $('#btn-value').val();
      expect(val).toBe('button');
    });
    it('(): on button with no value should get undefined', () => {
      const val = $('#btn-valueless').val();
      expect(val).toBeUndefined();
    });
    it('(): on select should get value', () => {
      const val = $('select#one').val();
      expect(val).toBe('option_selected');
    });
    it('(): on select with no value should get text', () => {
      const val = $('select#one-valueless').val();
      expect(val).toBe('Option selected');
    });
    it('(): on select with no value should get converted HTML', () => {
      const val = $('select#one-html-entity').val();
      expect(val).toBe('Option <selected>');
    });
    it('(): on select with no value should get text content', () => {
      const val = $('select#one-nested').val();
      expect(val).toBe('Option selected');
    });
    it('(): on option should get value', () => {
      const val = $('select#one option').eq(0).val();
      expect(val).toBe('option_not_selected');
    });
    it('(): on text input should get value', () => {
      const val = $('input[type="text"]').val();
      expect(val).toBe('input_text');
    });
    it('(): on checked checkbox should get value', () => {
      const val = $('input[name="checkbox_on"]').val();
      expect(val).toBe('on');
    });
    it('(): on unchecked checkbox should get value', () => {
      const val = $('input[name="checkbox_off"]').val();
      expect(val).toBe('off');
    });
    it('(): on valueless checkbox should get value', () => {
      const val = $('input[name="checkbox_valueless"]').val();
      expect(val).toBe('on');
    });
    it('(): on radio should get value', () => {
      const val = $('input[type="radio"]').val();
      expect(val).toBe('off');
    });
    it('(): on valueless radio should get value', () => {
      const val = $('input[name="radio_valueless"]').val();
      expect(val).toBe('on');
    });
    it('(): on multiple select should get an array of values', () => {
      const val = $('select#multi').val();
      expect(val).toStrictEqual(['2', '3']);
    });
    it('(): on multiple select with no value attribute should get an array of text content', () => {
      const val = $('select#multi-valueless').val();
      expect(val).toStrictEqual(['2', '3']);
    });
    it('(): with no selector matches should return nothing', () => {
      const val = $('.nasty').val();
      expect(val).toBeUndefined();
    });
    it('(invalid value): should only handle arrays when it has the attribute multiple', () => {
      const val = $('select#one').val([]);
      expect(val).not.toBeUndefined();
    });
    it('(value): on empty set should get `this`', () => {
      const $empty = $([]);
      expect($empty.val('test')).toBe($empty);
    });
    it('(value): on input text should set value', () => {
      const element = $('input[type="text"]').val('test');
      expect(element.val()).toBe('test');
    });
    it('(value): on select should set value', () => {
      const element = $('select#one').val('option_not_selected');
      expect(element.val()).toBe('option_not_selected');
    });
    it('(value): on option should set value', () => {
      const element = $('select#one option').eq(0).val('option_changed');
      expect(element.val()).toBe('option_changed');
    });
    it('(value): on radio should set value', () => {
      const element = $('input[name="radio"]').val('off');
      expect(element.val()).toBe('off');
    });
    it('(value): on radio with special characters should set value', () => {
      const element = $('input[name="radio[brackets]"]').val('off');
      expect(element.val()).toBe('off');
    });
    it('(values): on multiple select should set multiple values', () => {
      const element = $('select#multi').val(['1', '3', '4']);
      expect(element.val()).toHaveLength(3);
    });
  });

  describe('.removeAttr', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(fruits);
    });

    it('(key) : should remove a single attr', () => {
      const $fruits = $('#fruits');
      expect($fruits.attr('id')).not.toBeUndefined();
      $fruits.removeAttr('id');
      expect($fruits.attr('id')).toBeUndefined();
    });

    it('(key key) : should remove multiple attrs', () => {
      const $apple = $('.apple');
      $apple.attr('id', 'favorite');
      $apple.attr('size', 'small');

      expect($apple.attr('id')).toBe('favorite');
      expect($apple.attr('class')).toBe('apple');
      expect($apple.attr('size')).toBe('small');
      $apple.removeAttr('id class');
      expect($apple.attr('id')).toBeUndefined();
      expect($apple.attr('class')).toBeUndefined();
      expect($apple.attr('size')).toBe('small');
    });

    it('(key) : should return cheerio object', () => {
      const obj = $('ul').removeAttr('id');
      expect(obj).toBeInstanceOf($);
    });

    it('(key) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.addClass(() => 'test');

      expect($text('body').html()).toBe(
        '<a class="test">1</a>TEXT<b class="test">2</b>',
      );

      $body.removeAttr('class');

      expect($text('body').html()).toBe(mixedText);
    });
  });

  describe('.hasClass', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(fruits);
    });

    it('(valid class) : should return true', () => {
      const cls = $('.apple').hasClass('apple');
      expect(cls).toBe(true);

      expect(withClass('foo').hasClass('foo')).toBe(true);
      expect(withClass('foo bar').hasClass('foo')).toBe(true);
      expect(withClass('bar foo').hasClass('foo')).toBe(true);
      expect(withClass('bar foo bar').hasClass('foo')).toBe(true);
    });

    it('(invalid class) : should return false', () => {
      const cls = $('#fruits').hasClass('fruits');
      expect(cls).toBe(false);
      expect(withClass('foo-bar').hasClass('foo')).toBe(false);
      expect(withClass('foo-bar').hasClass('foo')).toBe(false);
      expect(withClass('foo-bar').hasClass('foo-ba')).toBe(false);
    });

    it('should check multiple classes', () => {
      // Add a class
      $('.apple').addClass('red');
      expect($('.apple').hasClass('apple')).toBe(true);
      expect($('.apple').hasClass('red')).toBe(true);

      // Remove one and test again
      $('.apple').removeClass('apple');
      expect($('li').eq(0).hasClass('apple')).toBe(false);
    });

    it('(empty string argument) : should return false', () => {
      expect(withClass('foo').hasClass('')).toBe(false);
      expect(withClass('foo bar').hasClass('')).toBe(false);
      expect(withClass('foo bar').removeClass('foo').hasClass('')).toBe(false);
    });
  });

  describe('.addClass', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(fruits);
    });

    it('(first class) : should add the class to the element', () => {
      const $fruits = $('#fruits');
      $fruits.addClass('fruits');
      const cls = $fruits.hasClass('fruits');
      expect(cls).toBe(true);
    });

    it('(single class) : should add the class to the element', () => {
      $('.apple').addClass('fruit');
      const cls = $('.apple').hasClass('fruit');
      expect(cls).toBe(true);
    });

    it('(class): adds classes to many selected items', () => {
      $('li').addClass('fruit');
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.orange').hasClass('fruit')).toBe(true);
      expect($('.pear').hasClass('fruit')).toBe(true);

      // Mixed with text nodes
      const $red = $('<html>\n<ul id=one>\n</ul>\t</html>').addClass('red');
      expect($red).toHaveLength(3);
      expect($red[0].type).toBe('text');
      expect($red[1].type).toBe('tag');
      expect($red[2].type).toBe('text');
      expect($red.hasClass('red')).toBe(true);
    });

    it('(class class class) : should add multiple classes to the element', () => {
      $('.apple').addClass('fruit red tasty');
      expect($('.apple').hasClass('apple')).toBe(true);
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.apple').hasClass('red')).toBe(true);
      expect($('.apple').hasClass('tasty')).toBe(true);
    });

    it('(fn) : should add classes returned from the function', () => {
      const $fruits = $('#fruits').children().add($('#fruits'));
      const args: [i: number, className: string][] = [];
      const thisVals: Element[] = [];
      const toAdd = ['main', 'apple red', '', undefined];

      $fruits.addClass(function (...myArgs) {
        args.push(myArgs);
        thisVals.push(this);
        return toAdd[myArgs[0]];
      });

      expect(args).toStrictEqual([
        [0, ''],
        [1, 'apple'],
        [2, 'orange'],
        [3, 'pear'],
      ]);
      expect(thisVals).toStrictEqual([
        $fruits[0],
        $fruits[1],
        $fruits[2],
        $fruits[3],
      ]);
      expect($fruits.eq(0).hasClass('main')).toBe(true);
      expect($fruits.eq(0).hasClass('apple')).toBe(false);
      expect($fruits.eq(1).hasClass('apple')).toBe(true);
      expect($fruits.eq(1).hasClass('red')).toBe(true);
      expect($fruits.eq(2).hasClass('orange')).toBe(true);
      expect($fruits.eq(3).hasClass('pear')).toBe(true);
    });
  });

  describe('.removeClass', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(fruits);
    });

    it('() : should remove all the classes', () => {
      $('.pear').addClass('fruit');
      $('.pear').removeClass();
      expect($('.pear').attr('class')).toBeUndefined();
    });

    it('("") : should not modify class list', () => {
      const $fruits = $('#fruits');
      $fruits.children().removeClass('');
      expect($('.apple')).toHaveLength(1);
    });

    it('(invalid class) : should not remove anything', () => {
      $('.pear').removeClass('fruit');
      expect($('.pear').hasClass('pear')).toBe(true);
    });

    it('(no class attribute) : should not throw an exception', () => {
      const $vegetables = cheerio(vegetables);

      expect(() => {
        $('li', $vegetables).removeClass('vegetable');
      }).not.toThrow();
    });

    it('(single class) : should remove a single class from the element', () => {
      $('.pear').addClass('fruit');
      expect($('.pear').hasClass('fruit')).toBe(true);
      $('.pear').removeClass('fruit');
      expect($('.pear').hasClass('fruit')).toBe(false);
      expect($('.pear').hasClass('pear')).toBe(true);

      // Remove one class from set
      const $li = $('li').removeClass('orange');
      expect($li.eq(0).attr('class')).toBe('apple');
      expect($li.eq(1).attr('class')).toBe('');
      expect($li.eq(2).attr('class')).toBe('pear');

      // Mixed with text nodes
      const $red = $('<html>\n<ul class=one>\n</ul>\t</html>').removeClass(
        'one',
      );
      expect($red).toHaveLength(3);
      expect($red[0].type).toBe('text');
      expect($red[1].type).toBe('tag');
      expect($red[2].type).toBe('text');
      expect($red.eq(1).attr('class')).toBe('');
      expect($red.eq(1).prop('tagName')).toBe('UL');
    });

    it('(single class) : should remove a single class from multiple classes on the element', () => {
      $('.pear').addClass('fruit green tasty');
      expect($('.pear').hasClass('fruit')).toBe(true);
      expect($('.pear').hasClass('green')).toBe(true);
      expect($('.pear').hasClass('tasty')).toBe(true);

      $('.pear').removeClass('green');
      expect($('.pear').hasClass('fruit')).toBe(true);
      expect($('.pear').hasClass('green')).toBe(false);
      expect($('.pear').hasClass('tasty')).toBe(true);
    });

    it('(class class class) : should remove multiple classes from the element', () => {
      $('.apple').addClass('fruit red tasty');
      expect($('.apple').hasClass('apple')).toBe(true);
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.apple').hasClass('red')).toBe(true);
      expect($('.apple').hasClass('tasty')).toBe(true);

      $('.apple').removeClass('apple red tasty');
      expect($('.fruit').hasClass('apple')).toBe(false);
      expect($('.fruit').hasClass('red')).toBe(false);
      expect($('.fruit').hasClass('tasty')).toBe(false);
      expect($('.fruit').hasClass('fruit')).toBe(true);
    });

    it('(class) : should remove all occurrences of a class name', () => {
      const $div = cheerio('<div class="x x y x z"></div>');
      expect($div.removeClass('x').hasClass('x')).toBe(false);
    });

    it('(fn) : should remove classes returned from the function', () => {
      const $fruits = $('#fruits').children();
      const args: [number, string][] = [];
      const thisVals: Element[] = [];
      const toAdd = ['apple red', '', undefined];

      $fruits.removeClass(function (...myArgs) {
        args.push(myArgs);
        thisVals.push(this);
        return toAdd[myArgs[0]];
      });

      expect(args).toStrictEqual([
        [0, 'apple'],
        [1, 'orange'],
        [2, 'pear'],
      ]);
      expect(thisVals).toStrictEqual([$fruits[0], $fruits[1], $fruits[2]]);
      expect($fruits.eq(0).hasClass('apple')).toBe(false);
      expect($fruits.eq(0).hasClass('red')).toBe(false);
      expect($fruits.eq(1).hasClass('orange')).toBe(true);
      expect($fruits.eq(2).hasClass('pear')).toBe(true);
    });

    it('(fn) : should no op elements without attributes', () => {
      const $inputs = $(inputs);
      const val = $inputs.removeClass(() => 'tasty');
      expect(val).toHaveLength(17);
    });

    it('(fn) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.addClass(() => 'test');

      expect($text('body').html()).toBe(
        '<a class="test">1</a>TEXT<b class="test">2</b>',
      );

      $body.removeClass(() => 'test');

      expect($text('body').html()).toBe(
        '<a class="">1</a>TEXT<b class="">2</b>',
      );
    });
  });

  describe('.toggleClass', () => {
    let $: CheerioAPI;

    beforeEach(() => {
      $ = load(fruits);
    });

    it('(class class) : should toggle multiple classes from the element', () => {
      $('.apple').addClass('fruit');
      expect($('.apple').hasClass('apple')).toBe(true);
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.apple').hasClass('red')).toBe(false);

      $('.apple').toggleClass('apple red');
      expect($('.fruit').hasClass('apple')).toBe(false);
      expect($('.fruit').hasClass('red')).toBe(true);
      expect($('.fruit').hasClass('fruit')).toBe(true);

      // Mixed with text nodes
      const $red = $('<html>\n<ul class=one>\n</ul>\t</html>').toggleClass(
        'red',
      );
      expect($red).toHaveLength(3);
      expect($red.hasClass('red')).toBe(true);
      expect($red.hasClass('one')).toBe(true);
      $red.toggleClass('one');
      expect($red.hasClass('red')).toBe(true);
      expect($red.hasClass('one')).toBe(false);
    });

    it('(class class, true) : should add multiple classes to the element', () => {
      $('.apple').addClass('fruit');
      expect($('.apple').hasClass('apple')).toBe(true);
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.apple').hasClass('red')).toBe(false);

      $('.apple').toggleClass('apple red', true);
      expect($('.fruit').hasClass('apple')).toBe(true);
      expect($('.fruit').hasClass('red')).toBe(true);
      expect($('.fruit').hasClass('fruit')).toBe(true);
    });

    it('(class true) : should add only one instance of class', () => {
      $('.apple').toggleClass('tasty', true);
      $('.apple').toggleClass('tasty', true);
      expect($('.apple').attr('class')).toMatch(/tasty/g);
    });

    it('(class class, false) : should remove multiple classes from the element', () => {
      $('.apple').addClass('fruit');
      expect($('.apple').hasClass('apple')).toBe(true);
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.apple').hasClass('red')).toBe(false);

      $('.apple').toggleClass('apple red', false);
      expect($('.fruit').hasClass('apple')).toBe(false);
      expect($('.fruit').hasClass('red')).toBe(false);
      expect($('.fruit').hasClass('fruit')).toBe(true);
    });

    it('(fn) : should toggle classes returned from the function', () => {
      const $ = load(food);

      $('.apple').addClass('fruit');
      $('.carrot').addClass('vegetable');
      expect($('.apple').hasClass('fruit')).toBe(true);
      expect($('.apple').hasClass('vegetable')).toBe(false);
      expect($('.orange').hasClass('fruit')).toBe(false);
      expect($('.orange').hasClass('vegetable')).toBe(false);
      expect($('.carrot').hasClass('fruit')).toBe(false);
      expect($('.carrot').hasClass('vegetable')).toBe(true);
      expect($('.sweetcorn').hasClass('fruit')).toBe(false);
      expect($('.sweetcorn').hasClass('vegetable')).toBe(false);

      $('li').toggleClass(function () {
        return $(this).parent().is('#fruits') ? 'fruit' : 'vegetable';
      });
      expect($('.apple').hasClass('fruit')).toBe(false);
      expect($('.apple').hasClass('vegetable')).toBe(false);
      expect($('.orange').hasClass('fruit')).toBe(true);
      expect($('.orange').hasClass('vegetable')).toBe(false);
      expect($('.carrot').hasClass('fruit')).toBe(false);
      expect($('.carrot').hasClass('vegetable')).toBe(false);
      expect($('.sweetcorn').hasClass('fruit')).toBe(false);
      expect($('.sweetcorn').hasClass('vegetable')).toBe(true);
    });

    it('(fn) : should work with no initial class attribute', () => {
      const $inputs = load(inputs);
      $inputs('input, select').toggleClass(function () {
        return $inputs(this).get(0)!.tagName === 'select'
          ? 'selectable'
          : 'inputable';
      });
      expect($inputs('.selectable')).toHaveLength(6);
      expect($inputs('.inputable')).toHaveLength(9);
    });

    it('(fn) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.toggleClass(() => 'test');

      expect($text('body').html()).toBe(
        '<a class="test">1</a>TEXT<b class="test">2</b>',
      );

      $body.toggleClass(() => 'test');

      expect($text('body').html()).toBe(
        '<a class="">1</a>TEXT<b class="">2</b>',
      );
    });

    it('(invalid) : should be a no-op for invalid inputs', () => {
      const original = $('.apple');
      const testAgainst = original.attr('class');
      expect(original.toggleClass().attr('class')).toStrictEqual(testAgainst);

      for (const value of [undefined, true, false, null, 0, 1, {}]) {
        expect(
          original.toggleClass(value as never).attr('class'),
        ).toStrictEqual(testAgainst);
      }
    });
  });
});
```

## File: `src/api/attributes.ts`
```typescript
/**
 * Methods for getting and modifying attributes.
 *
 * @module cheerio/attributes
 */

import { type AnyNode, type Element, isTag } from 'domhandler';
import { innerText, textContent } from 'domutils';
import { ElementType } from 'htmlparser2';
import type { Cheerio } from '../cheerio.js';
import { text } from '../static.js';
import { camelCase, cssCase, domEach } from '../utils.js';

const rspace = /\s+/;
const dataAttrPrefix = 'data-';

// Attributes that are booleans
const rboolean =
  /^(?:autofocus|autoplay|async|checked|controls|defer|disabled|hidden|loop|multiple|open|readonly|required|scoped|selected)$/i;
// Matches strings that look like JSON objects or arrays
const rbrace = /^{[\s\S]*}$|^\[[\s\S]*]$/;

/**
 * Gets a node's attribute. For boolean attributes, it will return the value's
 * name should it be set.
 *
 * Also supports getting the `value` of several form elements.
 *
 * @category Attributes
 * @param elem - Element to get the attribute of.
 * @param name - Name of the attribute.
 * @param xmlMode - Disable handling of special HTML attributes.
 * @returns The attribute's value.
 */
function getAttr(
  elem: AnyNode,
  name: undefined,
  xmlMode?: boolean,
): Record<string, string> | undefined;
function getAttr(
  elem: AnyNode,
  name: string,
  xmlMode?: boolean,
): string | undefined;
function getAttr(
  elem: AnyNode,
  name: string | undefined,
  xmlMode?: boolean,
): Record<string, string> | string | undefined;
function getAttr(
  elem: AnyNode,
  name: string | undefined,
  xmlMode?: boolean,
): Record<string, string> | string | undefined {
  if (!(elem && isTag(elem))) return;

  elem.attribs ??= {};

  // Return the entire attribs object if no attribute specified
  if (!name) {
    return elem.attribs;
  }

  if (Object.hasOwn(elem.attribs, name)) {
    // Get the (decoded) attribute
    return !xmlMode && rboolean.test(name) ? name : elem.attribs[name];
  }

  // Mimic the DOM and return text content as value for `option's`
  if (elem.name === 'option' && name === 'value') {
    return text(elem.children);
  }

  // Mimic DOM with default value for radios/checkboxes
  if (
    elem.name === 'input' &&
    (elem.attribs['type'] === 'radio' || elem.attribs['type'] === 'checkbox') &&
    name === 'value'
  ) {
    return 'on';
  }

  return;
}

/**
 * Sets the value of an attribute. The attribute will be deleted if the value is
 * `null`.
 *
 * @private
 * @param el - The element to set the attribute on.
 * @param name - The attribute's name.
 * @param value - The attribute's value.
 */
function setAttr(el: Element, name: string, value: string | null) {
  if (value === null) {
    removeAttribute(el, name);
  } else {
    el.attribs[name] = `${value}`;
  }
}

/**
 * Method for getting attributes. Gets the attribute value for only the first
 * element in the matched set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('ul').attr('id');
 * //=> fruits
 * ```
 *
 * @param name - Name of the attribute.
 * @returns The attribute's value.
 * @see {@link https://api.jquery.com/attr/}
 */
export function attr<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
): string | undefined;
/**
 * Method for getting all attributes and their values of the first element in
 * the matched set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('ul').attr();
 * //=> { id: 'fruits' }
 * ```
 *
 * @returns The attribute's values.
 * @see {@link https://api.jquery.com/attr/}
 */
export function attr<T extends AnyNode>(
  this: Cheerio<T>,
): Record<string, string> | undefined;
/**
 * Method for setting attributes. Sets the attribute value for all elements in
 * the matched set. If you set an attribute's value to `null`, you remove that
 * attribute. You may also pass a `map` and `function`.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.apple').attr('id', 'favorite').prop('outerHTML');
 * //=> <li class="apple" id="favorite">Apple</li>
 * ```
 *
 * @param name - Name of the attribute.
 * @param value - The new value of the attribute.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/attr/}
 */
export function attr<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
  value?:
    | string
    | null
    | ((this: Element, i: number, attrib: string) => string | null),
): Cheerio<T>;
/**
 * Method for setting multiple attributes at once. Sets the attribute value for
 * all elements in the matched set. If you set an attribute's value to `null`,
 * you remove that attribute.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.apple').attr({ id: 'favorite' }).prop('outerHTML');
 * //=> <li class="apple" id="favorite">Apple</li>
 * ```
 *
 * @param values - Map of attribute names and values.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/attr/}
 */
export function attr<T extends AnyNode>(
  this: Cheerio<T>,
  values: Record<string, string | null>,
): Cheerio<T>;
export function attr<T extends AnyNode>(
  this: Cheerio<T>,
  name?: string | Record<string, string | null>,
  value?:
    | string
    | null
    | ((this: Element, i: number, attrib: string) => string | null),
): string | Cheerio<T> | undefined | Record<string, string> {
  // Set the value (with attr map support)
  if (typeof name === 'object' || value !== undefined) {
    if (typeof value === 'function') {
      if (typeof name !== 'string') {
        throw new TypeError('Bad combination of arguments.');
      }
      return domEach(this, (el, i) => {
        if (isTag(el)) setAttr(el, name, value.call(el, i, el.attribs[name]));
      });
    }
    return domEach(this, (el) => {
      if (!isTag(el)) return;

      if (typeof name === 'object') {
        for (const objName of Object.keys(name)) {
          const objValue = name[objName];
          setAttr(el, objName, objValue);
        }
      } else {
        if (typeof name !== 'string') {
          throw new TypeError('Bad combination of arguments.');
        }
        setAttr(el, name, value ?? null);
      }
    });
  }

  return arguments.length > 1
    ? this
    : getAttr(this[0], name, this.options.xmlMode);
}

/**
 * Gets a node's prop.
 *
 * @private
 * @category Attributes
 * @param el - Element to get the prop of.
 * @param name - Name of the prop.
 * @param xmlMode - Disable handling of special HTML attributes.
 * @returns The prop's value.
 */
function getProp(
  el: Element,
  name: string,
  xmlMode?: boolean,
): string | undefined | boolean | Element[keyof Element] {
  return name in el
    ? // @ts-expect-error TS doesn't like us accessing the value directly here.
      (el[name] as string | undefined)
    : !xmlMode && rboolean.test(name)
      ? getAttr(el, name, false) !== undefined
      : getAttr(el, name, xmlMode);
}

/**
 * Sets the value of a prop.
 *
 * @private
 * @param el - The element to set the prop on.
 * @param name - The prop's name.
 * @param value - The prop's value.
 * @param xmlMode - Disable handling of special HTML attributes.
 */
function setProp(el: Element, name: string, value: unknown, xmlMode?: boolean) {
  if (name in el) {
    // @ts-expect-error Overriding value
    el[name] = value;
  } else {
    setAttr(
      el,
      name,
      !xmlMode && rboolean.test(name)
        ? value
          ? ''
          : null
        : `${value as string}`,
    );
  }
}

interface StyleProp {
  length: number;
  [key: string]: string | number;
  [index: number]: string;
}
/**
 * Get a string representation of the element.
 *
 * @param name Name of the property.
 */
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  name: 'innerHTML' | 'outerHTML' | 'innerText' | 'textContent',
): string | null;
/**
 * Get a parsed CSS style object.
 *
 * @param name - Name of the property.
 * @returns The style object, or `undefined` if the element has no `style`
 *   attribute.
 */
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  name: 'style',
): StyleProp | undefined;

/**
 * Method for getting and setting properties. Gets the property value for only
 * the first element in the matched set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('input[type="checkbox"]').prop('checked');
 * //=> false
 *
 * $('input[type="checkbox"]').prop('checked', true).val();
 * //=> ok
 * ```
 *
 * @param name - Name of the property.
 * @returns If `value` is specified the instance itself, otherwise the prop's
 *   value.
 * @see {@link https://api.jquery.com/prop/}
 */
// biome-ignore lint/style/useUnifiedTypeSignatures: Separate overloads needed for accurate docs
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  name: 'tagName' | 'nodeName',
): string | undefined;
/**
 * Resolve `href` or `src` of supported elements. Requires the `baseURI` option
 * to be set, and a global `URL` object to be part of the environment.
 *
 * @example With `baseURI` set to `'https://example.com'`:
 *
 * ```js
 * $('<img src="image.png">').prop('src');
 * //=> 'https://example.com/image.png'
 * ```
 *
 * @param name - Name of the property.
 * @returns The resolved URL, or `undefined` if the element is not supported.
 */
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  name: 'href' | 'src',
): string | undefined;
/**
 * Get a property of an element.
 *
 * @param name - Name of the property.
 * @returns The property's value.
 */
export function prop<T extends AnyNode, K extends keyof Element>(
  this: Cheerio<T>,
  name: K,
): Element[K];
/**
 * Set a property of an element.
 *
 * @param name - Name of the property.
 * @param value - Value to set the property to.
 * @returns The instance itself.
 */
export function prop<T extends AnyNode, K extends keyof Element>(
  this: Cheerio<T>,
  name: K,
  value:
    | Element[K]
    | ((this: Element, i: number, prop: K) => Element[keyof Element]),
): Cheerio<T>;
/**
 * Set multiple properties of an element.
 *
 * @example
 *
 * ```js
 * $('input[type="checkbox"]').prop({
 *   checked: true,
 *   disabled: false,
 * });
 * ```
 *
 * @param map - Object of properties to set.
 * @returns The instance itself.
 */
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  map: Record<string, string | Element[keyof Element] | boolean>,
): Cheerio<T>;
/**
 * Set a property of an element.
 *
 * @param name - Name of the property.
 * @param value - Value to set the property to.
 * @returns The instance itself.
 */
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
  value:
    | string
    | boolean
    | null
    | ((this: Element, i: number, prop: string) => string | boolean),
): Cheerio<T>;
/**
 * Get a property of an element.
 *
 * @param name - The property's name.
 * @returns The property's value.
 */
export function prop<T extends AnyNode>(this: Cheerio<T>, name: string): string;
export function prop<T extends AnyNode>(
  this: Cheerio<T>,
  name: string | Record<string, string | Element[keyof Element] | boolean>,
  value?: unknown,
):
  | Cheerio<T>
  | string
  | boolean
  | undefined
  | null
  | Element[keyof Element]
  | StyleProp {
  if (typeof name === 'string' && value === undefined) {
    const el = this[0];

    if (!el) return;

    switch (name) {
      case 'style': {
        const property = this.css() as StyleProp;
        const keys = Object.keys(property);
        for (let i = 0; i < keys.length; i++) {
          property[i] = keys[i];
        }

        property.length = keys.length;

        return property;
      }
      case 'tagName':
      case 'nodeName': {
        if (!isTag(el)) return;
        return el.name.toUpperCase();
      }

      case 'href':
      case 'src': {
        if (!isTag(el)) return;
        const prop = el.attribs?.[name];

        if (
          typeof URL !== 'undefined' &&
          ((name === 'href' && (el.tagName === 'a' || el.tagName === 'link')) ||
            (name === 'src' &&
              (el.tagName === 'img' ||
                el.tagName === 'iframe' ||
                el.tagName === 'audio' ||
                el.tagName === 'video' ||
                el.tagName === 'source'))) &&
          prop !== undefined &&
          this.options.baseURI
        ) {
          return new URL(prop, this.options.baseURI).href;
        }

        return prop;
      }

      case 'innerText': {
        return innerText(el);
      }

      case 'textContent': {
        return textContent(el);
      }

      case 'outerHTML': {
        if (el.type === ElementType.Root) return this.html();
        return this.clone().wrap('<container />').parent().html();
      }

      case 'innerHTML': {
        return this.html();
      }

      default: {
        if (!isTag(el)) return;
        return getProp(el, name, this.options.xmlMode);
      }
    }
  }

  if (typeof name === 'object' || value !== undefined) {
    if (typeof value === 'function') {
      if (typeof name === 'object') {
        throw new TypeError('Bad combination of arguments.');
      }
      return domEach(this, (el, i) => {
        if (isTag(el)) {
          setProp(
            el,
            name,
            value.call(el, i, getProp(el, name, this.options.xmlMode)),
            this.options.xmlMode,
          );
        }
      });
    }

    return domEach(this, (el) => {
      if (!isTag(el)) return;

      if (typeof name === 'object') {
        for (const key of Object.keys(name)) {
          const val = name[key];
          setProp(el, key, val, this.options.xmlMode);
        }
      } else {
        setProp(el, name, value, this.options.xmlMode);
      }
    });
  }

  return;
}

/**
 * An element with a data attribute.
 *
 * @private
 */
interface DataElement extends Element {
  /** The data attribute. */
  data?: Record<string, unknown>;
}

/**
 * Sets the value of a data attribute.
 *
 * @private
 * @param elem - The element to set the data attribute on.
 * @param name - The data attribute's name.
 * @param value - The data attribute's value.
 */
function setData(
  elem: DataElement,
  name: string | Record<string, unknown>,
  value?: unknown,
) {
  elem.data ??= {};

  if (typeof name === 'object') Object.assign(elem.data, name);
  else if (typeof name === 'string' && value !== undefined) {
    elem.data[name] = value;
  }
}

/**
 * Read _all_ HTML5 `data-*` attributes from the equivalent HTML5 `data-*`
 * attribute, and cache the value in the node's internal data store.
 *
 * @private
 * @category Attributes
 * @param el - Element to get the data attribute of.
 * @returns A map with all of the data attributes.
 */
function readAllData(el: DataElement): unknown {
  const data = (el.data ??= {});

  for (const domName of Object.keys(el.attribs)) {
    if (!domName.startsWith(dataAttrPrefix)) {
      continue;
    }

    const jsName = camelCase(domName.slice(dataAttrPrefix.length));

    if (!Object.hasOwn(data, jsName)) {
      data[jsName] = parseDataValue(el.attribs[domName]);
    }
  }

  return data;
}

/**
 * Read the specified attribute from the equivalent HTML5 `data-*` attribute,
 * and (if present) cache the value in the node's internal data store.
 *
 * @category Attributes
 * @param el - Element to get the data attribute of.
 * @param name - Name of the data attribute.
 * @returns The data attribute's value.
 */
function readData(el: DataElement, name: string): unknown {
  const domName = dataAttrPrefix + cssCase(name);
  const data = (el.data ??= {});

  if (Object.hasOwn(data, name)) {
    return data[name];
  }

  if (Object.hasOwn(el.attribs, domName)) {
    data[name] = parseDataValue(el.attribs[domName]);
    return data[name];
  }

  return;
}

/**
 * Coerce string data-* attributes to their corresponding JavaScript primitives.
 *
 * @category Attributes
 * @param value - The value to parse.
 * @returns The parsed value.
 */
function parseDataValue(value: string): unknown {
  if (value === 'null') return null;
  if (value === 'true') return true;
  if (value === 'false') return false;
  const num = Number(value);
  if (value === String(num)) return num;
  if (rbrace.test(value)) {
    try {
      return JSON.parse(value);
    } catch {
      /* Ignore */
    }
  }
  return value;
}

/**
 * Method for getting data attributes, for only the first element in the matched
 * set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('<div data-apple-color="red"></div>').data('apple-color');
 * //=> 'red'
 * ```
 *
 * @param name - Name of the data attribute.
 * @returns The data attribute's value, or `undefined` if the attribute does not
 *   exist.
 * @see {@link https://api.jquery.com/data/}
 */
export function data<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
): unknown;
/**
 * Method for getting all of an element's data attributes, for only the first
 * element in the matched set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('<div data-apple-color="red"></div>').data();
 * //=> { appleColor: 'red' }
 * ```
 *
 * @returns A map with all of the data attributes.
 * @see {@link https://api.jquery.com/data/}
 */
export function data<T extends AnyNode>(
  this: Cheerio<T>,
): Record<string, unknown>;
/**
 * Method for setting data attributes, for only the first element in the matched
 * set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * const apple = $('.apple').data('kind', 'mac');
 *
 * apple.data('kind');
 * //=> 'mac'
 * ```
 *
 * @param name - Name of the data attribute.
 * @param value - The new value.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/data/}
 */
export function data<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
  value: unknown,
): Cheerio<T>;
/**
 * Method for setting multiple data attributes at once, for only the first
 * element in the matched set.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * const apple = $('.apple').data({ kind: 'mac' });
 *
 * apple.data('kind');
 * //=> 'mac'
 * ```
 *
 * @param values - Map of names to values.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/data/}
 */
export function data<T extends AnyNode>(
  this: Cheerio<T>,
  values: Record<string, unknown>,
): Cheerio<T>;
export function data<T extends AnyNode>(
  this: Cheerio<T>,
  name?: string | Record<string, unknown>,
  value?: unknown,
): unknown {
  const elem = this[0];

  if (!(elem && isTag(elem))) return;

  const dataEl: DataElement = elem;
  dataEl.data ??= {};

  // Return the entire data object if no data specified
  if (name == null) {
    return readAllData(dataEl);
  }

  // Set the value (with attr map support)
  if (typeof name === 'object' || value !== undefined) {
    domEach(this, (el) => {
      if (isTag(el)) {
        if (typeof name === 'object') setData(el, name);
        else setData(el, name, value);
      }
    });
    return this;
  }

  return readData(dataEl, name);
}

/**
 * Method for getting the value of input, select, and textarea. Note: Support
 * for `map`, and `function` has not been added yet.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('input[type="text"]').val();
 * //=> input_text
 * ```
 *
 * @returns The value.
 * @see {@link https://api.jquery.com/val/}
 */
export function val<T extends AnyNode>(
  this: Cheerio<T>,
): string | undefined | string[];
/**
 * Method for setting the value of input, select, and textarea. Note: Support
 * for `map`, and `function` has not been added yet.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('input[type="text"]').val('test').prop('outerHTML');
 * //=> <input type="text" value="test"/>
 * ```
 *
 * @param value - The new value.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/val/}
 */
export function val<T extends AnyNode>(
  this: Cheerio<T>,
  value: string | string[],
): Cheerio<T>;
export function val<T extends AnyNode>(
  this: Cheerio<T>,
  value?: string | string[],
): string | string[] | Cheerio<T> | undefined {
  const querying = arguments.length === 0;
  const element = this[0];

  if (!(element && isTag(element))) return querying ? undefined : this;

  switch (element.name) {
    case 'textarea': {
      return this.text(value as string);
    }
    case 'select': {
      const option = this.find('option:selected');
      if (!querying) {
        if (this.attr('multiple') == null && typeof value === 'object') {
          return this;
        }

        this.find('option').removeAttr('selected');

        const values = typeof value === 'object' ? value : [value];
        for (const val of values) {
          this.find(`option[value="${val}"]`).attr('selected', '');
        }

        return this;
      }

      return this.attr('multiple')
        ? option.toArray().map((el) => text(el.children))
        : option.attr('value');
    }
    case 'button':
    case 'input':
    case 'option': {
      return querying
        ? this.attr('value')
        : this.attr('value', value as string);
    }
  }

  return;
}

/**
 * Remove an attribute.
 *
 * @param elem - Node to remove attribute from.
 * @param name - Name of the attribute to remove.
 */
function removeAttribute(elem: Element, name: string) {
  if (!(elem.attribs && Object.hasOwn(elem.attribs, name))) return;

  delete elem.attribs[name];
}

/**
 * Splits a space-separated list of names to individual names.
 *
 * @category Attributes
 * @param names - Names to split.
 * @returns - Split names.
 */
function splitNames(names?: string): string[] {
  return names ? names.trim().split(rspace) : [];
}

/**
 * Method for removing attributes by `name`.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.pear').removeAttr('class').prop('outerHTML');
 * //=> <li>Pear</li>
 *
 * $('.apple').attr('id', 'favorite');
 * $('.apple').removeAttr('id class').prop('outerHTML');
 * //=> <li>Apple</li>
 * ```
 *
 * @param name - Name of the attribute.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/removeAttr/}
 */
export function removeAttr<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
): Cheerio<T> {
  const attrNames = splitNames(name);

  for (const attrName of attrNames) {
    domEach(this, (elem) => {
      if (isTag(elem)) removeAttribute(elem, attrName);
    });
  }

  return this;
}

/**
 * Check to see if _any_ of the matched elements have the given `className`.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.pear').hasClass('pear');
 * //=> true
 *
 * $('apple').hasClass('fruit');
 * //=> false
 *
 * $('li').hasClass('pear');
 * //=> true
 * ```
 *
 * @param className - Name of the class.
 * @returns Indicates if an element has the given `className`.
 * @see {@link https://api.jquery.com/hasClass/}
 */
export function hasClass<T extends AnyNode>(
  this: Cheerio<T>,
  className: string,
): boolean {
  return this.toArray().some((elem) => {
    const clazz = isTag(elem) && elem.attribs['class'];

    if (clazz && className.length > 0) {
      for (
        let idx = clazz.indexOf(className);
        idx > -1;
        idx = clazz.indexOf(className, idx + 1)
      ) {
        const end = idx + className.length;

        if (
          (idx === 0 || rspace.test(clazz[idx - 1])) &&
          (end === clazz.length || rspace.test(clazz[end]))
        ) {
          return true;
        }
      }
    }

    return false;
  });
}

/**
 * Adds class(es) to all of the matched elements. Also accepts a `function`.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.pear').addClass('fruit').prop('outerHTML');
 * //=> <li class="pear fruit">Pear</li>
 *
 * $('.apple').addClass('fruit red').prop('outerHTML');
 * //=> <li class="apple fruit red">Apple</li>
 * ```
 *
 * @param value - Name of new class.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/addClass/}
 */
export function addClass<T extends AnyNode, R extends ArrayLike<T>>(
  this: R,
  value?:
    | string
    | ((this: Element, i: number, className: string) => string | undefined),
): R {
  // Support functions
  if (typeof value === 'function') {
    return domEach(this, (el, i) => {
      if (isTag(el)) {
        const className = el.attribs['class'] || '';
        addClass.call([el], value.call(el, i, className));
      }
    });
  }

  // Return if no value or not a string or function
  if (!value || typeof value !== 'string') return this;

  const classNames = value.split(rspace);
  const numElements = this.length;

  for (let i = 0; i < numElements; i++) {
    const el = this[i];
    // If selected element isn't a tag, move on
    if (!isTag(el)) continue;

    // If we don't already have classes — always set xmlMode to false here, as it doesn't matter for classes
    const className = getAttr(el, 'class', false);

    if (className) {
      let setClass = ` ${className} `;

      // Check if class already exists
      for (const cn of classNames) {
        const appendClass = `${cn} `;
        if (!setClass.includes(` ${appendClass}`)) setClass += appendClass;
      }

      setAttr(el, 'class', setClass.trim());
    } else {
      setAttr(el, 'class', classNames.join(' ').trim());
    }
  }

  return this;
}

/**
 * Removes one or more space-separated classes from the selected elements. If no
 * `className` is defined, all classes will be removed. Also accepts a
 * `function`.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.pear').removeClass('pear').prop('outerHTML');
 * //=> <li class="">Pear</li>
 *
 * $('.apple').addClass('red').removeClass().prop('outerHTML');
 * //=> <li class="">Apple</li>
 * ```
 *
 * @param name - Name of the class. If not specified, removes all elements.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/removeClass/}
 */
export function removeClass<T extends AnyNode, R extends ArrayLike<T>>(
  this: R,
  name?:
    | string
    | ((this: Element, i: number, className: string) => string | undefined),
): R {
  // Handle if value is a function
  if (typeof name === 'function') {
    return domEach(this, (el, i) => {
      if (isTag(el)) {
        removeClass.call([el], name.call(el, i, el.attribs['class'] || ''));
      }
    });
  }

  const classes = splitNames(name);
  const numClasses = classes.length;
  const removeAll = arguments.length === 0;

  return domEach(this, (el) => {
    if (!isTag(el)) return;

    if (removeAll) {
      // Short circuit the remove all case as this is the nice one
      el.attribs['class'] = '';
    } else {
      const elClasses = splitNames(el.attribs['class']);
      let changed = false;

      for (let j = 0; j < numClasses; j++) {
        const index = elClasses.indexOf(classes[j]);

        if (index !== -1) {
          elClasses.splice(index, 1);
          changed = true;

          /*
           * We have to do another pass to ensure that there are not duplicate
           * classes listed
           */
          j--;
        }
      }
      if (changed) {
        el.attribs['class'] = elClasses.join(' ');
      }
    }
  });
}

/**
 * Add or remove class(es) from the matched elements, depending on either the
 * class's presence or the value of the switch argument. Also accepts a
 * `function`.
 *
 * @category Attributes
 * @example
 *
 * ```js
 * $('.apple.green').toggleClass('fruit green red').prop('outerHTML');
 * //=> <li class="apple fruit red">Apple</li>
 *
 * $('.apple.green').toggleClass('fruit green red', true).prop('outerHTML');
 * //=> <li class="apple green fruit red">Apple</li>
 * ```
 *
 * @param value - Name of the class. Can also be a function.
 * @param stateVal - If specified the state of the class.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/toggleClass/}
 */
export function toggleClass<T extends AnyNode, R extends ArrayLike<T>>(
  this: R,
  value?:
    | string
    | ((
        this: Element,
        i: number,
        className: string,
        stateVal?: boolean,
      ) => string),
  stateVal?: boolean,
): R {
  // Support functions
  if (typeof value === 'function') {
    return domEach(this, (el, i) => {
      if (isTag(el)) {
        toggleClass.call(
          [el],
          value.call(el, i, el.attribs['class'] || '', stateVal),
          stateVal,
        );
      }
    });
  }

  // Return if no value or not a string or function
  if (!value || typeof value !== 'string') return this;

  const classNames = value.split(rspace);
  const numClasses = classNames.length;
  const state = typeof stateVal === 'boolean' ? (stateVal ? 1 : -1) : 0;
  const numElements = this.length;

  for (let i = 0; i < numElements; i++) {
    const el = this[i];
    // If selected element isn't a tag, move on
    if (!isTag(el)) continue;

    const elementClasses = splitNames(el.attribs['class']);

    // Check if class already exists
    for (let j = 0; j < numClasses; j++) {
      // Check if the class name is currently defined
      const index = elementClasses.indexOf(classNames[j]);

      // Add if stateValue === true or we are toggling and there is no value
      if (state >= 0 && index === -1) {
        elementClasses.push(classNames[j]);
      } else if (state <= 0 && index !== -1) {
        // Otherwise remove but only if the item exists
        elementClasses.splice(index, 1);
      }
    }

    el.attribs['class'] = elementClasses.join(' ');
  }

  return this;
}
```

## File: `src/api/css.spec.ts`
```typescript
import type { Element } from 'domhandler';
import { beforeEach, describe, expect, it } from 'vitest';
import { cheerio, mixedText } from '../__fixtures__/fixtures.js';
import { type Cheerio, load } from '../index.js';

describe('$(...)', () => {
  describe('.css', () => {
    it('(prop): should return a css property value', () => {
      const el = cheerio('<li style="hai: there">');
      expect(el.css('hai')).toBe('there');
    });

    it('([prop1, prop2]): should return the specified property values as an object', () => {
      const el = cheerio(
        '<li style="margin: 1px; padding: 2px; color: blue;">',
      );
      expect(el.css(['margin', 'color'])).toStrictEqual({
        margin: '1px',
        color: 'blue',
      });
    });

    it('(prop, val): should set a css property', () => {
      const el = cheerio('<li style="margin: 0;"></li><li></li>');
      el.css('color', 'red');
      expect(el.attr('style')).toBe('margin: 0; color: red;');
      expect(el.eq(1).attr('style')).toBe('color: red;');
    });

    it('(prop, val) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.css('test', 'value');

      expect($text('body').html()).toBe(
        '<a style="test: value;">1</a>TEXT<b style="test: value;">2</b>',
      );
    });

    it('(prop, ""): should unset a css property', () => {
      const el = cheerio('<li style="padding: 1px; margin: 0;">');
      el.css('padding', '');
      expect(el.attr('style')).toBe('margin: 0;');
    });

    it('(any, val): should ignore unsupported prop types', () => {
      const el = cheerio('<li style="padding: 1px;">');
      el.css(123 as never, 'test');
      expect(el.attr('style')).toBe('padding: 1px;');
    });

    it('(prop): should not mangle embedded urls', () => {
      const el = cheerio(
        '<li style="background-image:url(http://example.com/img.png);">',
      );
      expect(el.css('background-image')).toBe(
        'url(http://example.com/img.png)',
      );
    });

    it('(prop): should ignore blank properties', () => {
      const el = cheerio('<li style=":#ccc;color:#aaa;">');
      expect(el.css()).toStrictEqual({ color: '#aaa' });
    });

    it('(prop): should ignore blank values', () => {
      const el = cheerio('<li style="color:;position:absolute;">');
      expect(el.css()).toStrictEqual({ position: 'absolute' });
    });

    it('(prop): should return undefined for unmatched elements', () => {
      const $ = load('<li style="color:;position:absolute;">');
      expect($('ul').css('background-image')).toBeUndefined();
    });

    it('(prop): should return undefined for unmatched styles', () => {
      const el = cheerio('<li style="color:;position:absolute;">');
      expect(el.css('margin')).toBeUndefined();
    });

    describe('(prop, function):', () => {
      let $el: Cheerio<Element>;
      beforeEach(() => {
        const $ = load(
          '<div style="margin: 0px;"></div><div style="margin: 1px;"></div><div style="margin: 2px;">',
        );
        $el = $('div');
      });

      it('should iterate over the selection', () => {
        let count = 0;
        $el.css('margin', function (idx, value) {
          expect(idx).toBe(count);
          expect(value).toBe(`${count}px`);
          expect(this).toBe($el[count]);
          count++;
          return;
        });
        expect(count).toBe(3);
      });

      it('should set each attribute independently', () => {
        const values = ['4px', '', undefined];
        $el.css('margin', (idx) => values[idx]);
        expect($el.eq(0).attr('style')).toBe('margin: 4px;');
        expect($el.eq(1).attr('style')).toBe('');
        expect($el.eq(2).attr('style')).toBe('margin: 2px;');
      });
    });

    it('(obj): should set each key and val', () => {
      const el = cheerio('<li style="padding: 0;"></li><li></li>');
      el.css({ foo: 0 } as never);
      expect(el.eq(0).attr('style')).toBe('padding: 0; foo: 0;');
      expect(el.eq(1).attr('style')).toBe('foo: 0;');
    });

    describe('parser', () => {
      it('should allow any whitespace between declarations', () => {
        const el = cheerio('<li style="one \t:\n 0;\n two \f\r:\v 1">');
        expect(el.css(['one', 'two', 'five'])).toStrictEqual({
          one: '0',
          two: '1',
        });
      });

      it('should add malformed values to previous field (#1134)', () => {
        const el = cheerio(
          '<button style="background-image: url(data:image/png;base64,iVBORw0KGgo)"></button>',
        );
        expect(el.css('background-image')).toStrictEqual(
          'url(data:image/png;base64,iVBORw0KGgo)',
        );
      });
    });
  });
});
```

## File: `src/api/css.ts`
```typescript
import { type AnyNode, type Element, isTag } from 'domhandler';
import type { Cheerio } from '../cheerio.js';
import { domEach } from '../utils.js';

/**
 * Get the value of a style property for the first element in the set of matched
 * elements.
 *
 * @category CSS
 * @param names - Optionally the names of the properties of interest.
 * @returns A map of all of the style properties.
 * @see {@link https://api.jquery.com/css/}
 */
export function css<T extends AnyNode>(
  this: Cheerio<T>,
  names?: string[],
): Record<string, string> | undefined;
/**
 * Get the value of a style property for the first element in the set of matched
 * elements.
 *
 * @category CSS
 * @param name - The name of the property.
 * @returns The property value for the given name.
 * @see {@link https://api.jquery.com/css/}
 */
export function css<T extends AnyNode>(
  this: Cheerio<T>,
  name: string,
): string | undefined;
/**
 * Set one CSS property for every matched element.
 *
 * @category CSS
 * @param prop - The name of the property.
 * @param val - The new value.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/css/}
 */
export function css<T extends AnyNode>(
  this: Cheerio<T>,
  prop: string,
  val: string | ((this: Element, i: number, style: string) => string | void),
): Cheerio<T>;
/**
 * Set multiple CSS properties for every matched element.
 *
 * @category CSS
 * @param map - A map of property names and values.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/css/}
 */
export function css<T extends AnyNode>(
  this: Cheerio<T>,
  map: Record<string, string>,
): Cheerio<T>;
/**
 * Set multiple CSS properties for every matched element.
 *
 * @category CSS
 * @param prop - The names of the properties.
 * @param val - The new values.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/css/}
 */
export function css<T extends AnyNode>(
  this: Cheerio<T>,
  prop?: string | string[] | Record<string, string>,
  val?: string | ((this: Element, i: number, style: string) => string | void),
): Cheerio<T> | Record<string, string> | string | undefined {
  if (
    (prop != null && val != null) ||
    // When `prop` is a "plain" object
    (typeof prop === 'object' && !Array.isArray(prop))
  ) {
    return domEach(this, (el, i) => {
      if (isTag(el)) {
        // `prop` can't be an array here anymore.
        setCss(el, prop as string, val, i);
      }
    });
  }

  if (this.length === 0) {
    return;
  }

  return getCss(this[0], prop as string);
}

/**
 * Set styles of all elements.
 *
 * @private
 * @param el - Element to set style of.
 * @param prop - Name of property.
 * @param value - Value to set property to.
 * @param idx - Optional index within the selection.
 */
function setCss(
  el: Element,
  prop: string | Record<string, string>,
  value:
    | string
    | ((this: Element, i: number, style: string) => string | void)
    | undefined,
  idx: number,
) {
  if (typeof prop === 'string') {
    const styles = getCss(el);

    const val =
      typeof value === 'function' ? value.call(el, idx, styles[prop]) : value;

    if (val === '') {
      delete styles[prop];
    } else if (val != null) {
      styles[prop] = val;
    }

    el.attribs['style'] = stringify(styles);
  } else if (typeof prop === 'object') {
    const keys = Object.keys(prop);
    for (let i = 0; i < keys.length; i++) {
      const k = keys[i];
      setCss(el, k, prop[k], i);
    }
  }
}

/**
 * Get the parsed styles of the first element.
 *
 * @private
 * @category CSS
 * @param el - Element to get styles from.
 * @param props - Optionally the names of the properties of interest.
 * @returns The parsed styles.
 */
function getCss(el: AnyNode, props?: string[]): Record<string, string>;
/**
 * Get a property from the parsed styles of the first element.
 *
 * @private
 * @category CSS
 * @param el - Element to get styles from.
 * @param prop - Name of the prop.
 * @returns The value of the property.
 */
function getCss(el: AnyNode, prop: string): string | undefined;
function getCss(
  el: AnyNode,
  prop?: string | string[],
): Record<string, string> | string | undefined {
  if (!(el && isTag(el))) return;

  const styles = parse(el.attribs['style']);
  if (typeof prop === 'string') {
    return styles[prop];
  }
  if (Array.isArray(prop)) {
    const newStyles: Record<string, string> = {};
    for (const item of prop) {
      if (styles[item] != null) {
        newStyles[item] = styles[item];
      }
    }
    return newStyles;
  }
  return styles;
}

/**
 * Stringify `obj` to styles.
 *
 * @private
 * @category CSS
 * @param obj - Object to stringify.
 * @returns The serialized styles.
 */
function stringify(obj: Record<string, string>): string {
  return Object.keys(obj).reduce(
    (str, prop) => `${str}${str ? ' ' : ''}${prop}: ${obj[prop]};`,
    '',
  );
}

/**
 * Parse `styles`.
 *
 * @private
 * @category CSS
 * @param styles - Styles to be parsed.
 * @returns The parsed styles.
 */
function parse(styles: string): Record<string, string> {
  styles = (styles || '').trim();

  if (!styles) return {};

  const obj: Record<string, string> = {};

  let key: string | undefined;

  for (const str of styles.split(';')) {
    const n = str.indexOf(':');
    // If there is no :, or if it is the first/last character, add to the previous item's value
    if (n < 1 || n === str.length - 1) {
      const trimmed = str.trimEnd();
      if (trimmed.length > 0 && key !== undefined) {
        obj[key] += `;${trimmed}`;
      }
    } else {
      key = str.slice(0, n).trim();
      obj[key] = str.slice(n + 1).trim();
    }
  }

  return obj;
}
```

## File: `src/api/extract.spec.ts`
```typescript
import { describe, expect, expectTypeOf, it } from 'vitest';
import * as fixtures from '../__fixtures__/fixtures.js';
import { load } from '../load-parse.js';

interface RedSelObject {
  red: string | undefined;
  sel: string | undefined;
}

interface RedSelMultipleObject {
  red: string[];
  sel: string[];
}

describe('$.extract', () => {
  it('should return an empty object when no selectors are provided', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf($root.extract({})).toEqualTypeOf<Record<never, never>>();
    const emptyExtract = $root.extract({});
    expect(emptyExtract).toStrictEqual({});
  });

  it('should return undefined for selectors that do not match any elements', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf($root.extract({ foo: 'bar' })).toEqualTypeOf<{
      foo: string | undefined;
    }>();
    const simpleExtract = $root.extract({ foo: 'bar' });
    expect(simpleExtract).toStrictEqual({ foo: undefined });
  });

  it('should extract values for existing selectors', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf($root.extract({ red: '.red' })).toEqualTypeOf<{
      red: string | undefined;
    }>();
    expect($root.extract({ red: '.red' })).toStrictEqual({ red: 'Four' });

    expectTypeOf(
      $root.extract({ red: '.red', sel: '.sel' }),
    ).toEqualTypeOf<RedSelObject>();
    expect($root.extract({ red: '.red', sel: '.sel' })).toStrictEqual({
      red: 'Four',
      sel: 'Three',
    });
  });

  it('should extract values using descriptor objects', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: { selector: '.red' },
        sel: { selector: '.sel' },
      }),
    ).toEqualTypeOf<RedSelObject>();
    expect(
      $root.extract({
        red: { selector: '.red' },
        sel: { selector: '.sel' },
      }),
    ).toStrictEqual({ red: 'Four', sel: 'Three' });
  });

  it('should extract multiple values for selectors', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: ['.red'],
        sel: ['.sel'],
      }),
    ).toEqualTypeOf<{ red: string[]; sel: string[] }>();
    const multipleExtract = $root.extract({
      red: ['.red'],
      sel: ['.sel'],
    });
    expectTypeOf(multipleExtract).toEqualTypeOf<RedSelMultipleObject>();
    expect(multipleExtract).toStrictEqual({
      red: ['Four', 'Five', 'Nine'],
      sel: ['Three', 'Nine', 'Eleven'],
    });
  });

  it('should extract custom properties specified by the user', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: { selector: '.red', value: 'outerHTML' },
        sel: { selector: '.sel', value: 'tagName' },
      }),
    ).toEqualTypeOf<RedSelObject>();
    expect(
      $root.extract({
        red: { selector: '.red', value: 'outerHTML' },
        sel: { selector: '.sel', value: 'tagName' },
      }),
    ).toStrictEqual({ red: '<li class="red">Four</li>', sel: 'LI' });
  });

  it('should extract multiple custom properties for selectors', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: [{ selector: '.red', value: 'outerHTML' }],
      }),
    ).toEqualTypeOf<{ red: string[] }>();
    expect(
      $root.extract({
        red: [{ selector: '.red', value: 'outerHTML' }],
      }),
    ).toStrictEqual({
      red: [
        '<li class="red">Four</li>',
        '<li class="red">Five</li>',
        '<li class="red sel">Nine</li>',
      ],
    });
  });

  it('should extract values using custom extraction functions', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: {
          selector: '.red',
          value: (el, key) => `${key}=${$(el).text()}`,
        },
      }),
    ).toEqualTypeOf<{ red: string | undefined }>();
    expect(
      $root.extract({
        red: {
          selector: '.red',
          value: (el, key) => `${key}=${$(el).text()}`,
        },
      }),
    ).toStrictEqual({ red: 'red=Four' });
  });

  it('should correctly type check custom extraction functions returning non-string values', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: {
          selector: '.red',
          value: (el) => $(el).text().length,
        },
      }),
    ).toEqualTypeOf<{ red: number | undefined }>();
    expect(
      $root.extract({
        red: {
          selector: '.red',
          value: (el) => $(el).text().length,
        },
      }),
    ).toStrictEqual({ red: 4 });
  });

  it('should extract multiple values using custom extraction functions', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        red: [
          {
            selector: '.red',
            value: (el, key) => `${key}=${$(el).text()}`,
          },
        ],
      }),
    ).toEqualTypeOf<{ red: string[] }>();
    expect(
      $root.extract({
        red: [
          {
            selector: '.red',
            value: (el, key) => `${key}=${$(el).text()}`,
          },
        ],
      }),
    ).toStrictEqual({ red: ['red=Four', 'red=Five', 'red=Nine'] });
  });

  it('should extract nested objects based on selectors', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        section: {
          selector: 'ul:nth(1)',
          value: {
            red: '.red',
            sel: '.blue',
          },
        },
      }),
    ).toEqualTypeOf<{
      section: { red: string | undefined; sel: string | undefined } | undefined;
    }>();
    const subExtractObject = $root.extract({
      section: {
        selector: 'ul:nth(1)',
        value: {
          red: '.red',
          sel: '.blue',
        },
      },
    });
    expectTypeOf(subExtractObject).toEqualTypeOf<{
      section: RedSelObject | undefined;
    }>();
    expect(subExtractObject).toStrictEqual({
      section: {
        red: 'Five',
        sel: 'Seven',
      },
    });
  });

  it('should correctly type check nested objects returning non-string values', () => {
    const $ = load(fixtures.eleven);
    const $root = $.root();

    expectTypeOf(
      $root.extract({
        section: {
          selector: 'ul:nth(1)',
          value: {
            red: {
              selector: '.red',
              value: (el) => $(el).text().length,
            },
          },
        },
      }),
    ).toEqualTypeOf<{
      section: { red: number | undefined } | undefined;
    }>();
    expect(
      $root.extract({
        section: {
          selector: 'ul:nth(1)',
          value: {
            red: {
              selector: '.red',
              value: (el) => $(el).text().length,
            },
          },
        },
      }),
    ).toStrictEqual({
      section: {
        red: 4,
      },
    });
  });

  it('should handle missing href properties without errors (#4239)', () => {
    const $ = load(fixtures.eleven);
    expect<{ links: string[] }>(
      $.extract({ links: [{ selector: 'li', value: 'href' }] }),
    ).toStrictEqual({ links: [] });
  });
});
```

## File: `src/api/extract.ts`
```typescript
import type { AnyNode, Element } from 'domhandler';
import type { Cheerio } from '../cheerio.js';
import type { prop } from './attributes.js';

type ExtractDescriptorFn = (
  el: Element,
  key: string,
  // TODO: This could be typed with ExtractedMap
  obj: Record<string, unknown>,
) => unknown;

interface ExtractDescriptor {
  selector: string;
  value?: string | ExtractDescriptorFn | ExtractMap;
}

type ExtractValue = string | ExtractDescriptor | [string | ExtractDescriptor];

/** Descriptor map used by {@link extract}. */
export type ExtractMap = Record<string, ExtractValue>;

type ExtractedValue<V extends ExtractValue> = V extends [
  string | ExtractDescriptor,
]
  ? NonNullable<ExtractedValue<V[0]>>[]
  : V extends string
    ? string | undefined
    : V extends ExtractDescriptor
      ? V['value'] extends infer U
        ? U extends ExtractMap
          ? ExtractedMap<U> | undefined
          : U extends ExtractDescriptorFn
            ? ReturnType<U> | undefined
            : ReturnType<typeof prop> | undefined
        : never
      : never;

/** Result type computed from an {@link ExtractMap}. */
export type ExtractedMap<M extends ExtractMap> = {
  [key in keyof M]: ExtractedValue<M[key]>;
};

function getExtractDescr(
  descr: string | ExtractDescriptor,
): Required<ExtractDescriptor> {
  if (typeof descr === 'string') {
    return { selector: descr, value: 'textContent' };
  }

  return {
    selector: descr.selector,
    value: descr.value ?? 'textContent',
  };
}

/**
 * Extract multiple values from a document, and store them in an object.
 *
 * @param map - An object containing key-value pairs. The keys are the names of
 *   the properties to be created on the object, and the values are the
 *   selectors to be used to extract the values.
 * @returns An object containing the extracted values.
 */
export function extract<M extends ExtractMap, T extends AnyNode>(
  this: Cheerio<T>,
  map: M,
): ExtractedMap<M> {
  const ret: Record<string, unknown> = {};

  for (const key in map) {
    const descr = map[key];
    const isArray = Array.isArray(descr);

    const { selector, value } = getExtractDescr(isArray ? descr[0] : descr);

    const fn: ExtractDescriptorFn =
      typeof value === 'function'
        ? value
        : typeof value === 'string'
          ? (el: Element) => this._make(el).prop(value)
          : (el: Element) => this._make(el).extract(value);

    if (isArray) {
      ret[key] = this._findBySelector(selector, Number.POSITIVE_INFINITY)
        .map((_, el) => fn(el, key, ret))
        .get();
    } else {
      const $ = this._findBySelector(selector, 1);
      ret[key] = $.length > 0 ? fn($[0], key, ret) : undefined;
    }
  }

  return ret as ExtractedMap<M>;
}
```

## File: `src/api/forms.spec.ts`
```typescript
import { beforeEach, describe, expect, it } from 'vitest';
import { cheerio, forms } from '../__fixtures__/fixtures.js';
import type { CheerioAPI } from '../index.js';

describe('$(...)', () => {
  let $: CheerioAPI;

  beforeEach(() => {
    $ = cheerio.load(forms);
  });

  describe('.serializeArray', () => {
    it('() : should get form controls', () => {
      expect($('form#simple').serializeArray()).toStrictEqual([
        {
          name: 'fruit',
          value: 'Apple',
        },
      ]);
    });

    it('() : should get nested form controls', () => {
      expect($('form#nested').serializeArray()).toHaveLength(2);
      const data = $('form#nested').serializeArray();
      data.sort((a, b) => (a.value > b.value ? 1 : -1));
      expect(data).toStrictEqual([
        {
          name: 'fruit',
          value: 'Apple',
        },
        {
          name: 'vegetable',
          value: 'Carrot',
        },
      ]);
    });

    it('() : should not get disabled form controls', () => {
      expect($('form#disabled').serializeArray()).toStrictEqual([]);
    });

    it('() : should not get form controls with the wrong type', () => {
      expect($('form#submit').serializeArray()).toStrictEqual([
        {
          name: 'fruit',
          value: 'Apple',
        },
      ]);
    });

    it('() : should get selected options', () => {
      expect($('form#select').serializeArray()).toStrictEqual([
        {
          name: 'fruit',
          value: 'Orange',
        },
      ]);
    });

    it('() : should not get unnamed form controls', () => {
      expect($('form#unnamed').serializeArray()).toStrictEqual([
        {
          name: 'fruit',
          value: 'Apple',
        },
      ]);
    });

    it('() : should get multiple selected options', () => {
      expect($('form#multiple').serializeArray()).toHaveLength(2);
      const data = $('form#multiple').serializeArray();
      data.sort((a, b) => (a.value > b.value ? 1 : -1));
      expect(data).toStrictEqual([
        {
          name: 'fruit',
          value: 'Apple',
        },
        {
          name: 'fruit',
          value: 'Orange',
        },
      ]);
    });

    it('() : should get individually selected elements', () => {
      const data = $('form#nested input').serializeArray();
      data.sort((a, b) => (a.value > b.value ? 1 : -1));
      expect(data).toStrictEqual([
        {
          name: 'fruit',
          value: 'Apple',
        },
        {
          name: 'vegetable',
          value: 'Carrot',
        },
      ]);
    });

    it('() : should standardize line breaks', () => {
      expect($('form#textarea').serializeArray()).toStrictEqual([
        {
          name: 'fruits',
          value: 'Apple\r\nOrange',
        },
      ]);
    });

    it("() : shouldn't serialize the empty string", () => {
      expect($('<input value=pineapple>').serializeArray()).toStrictEqual([]);
      expect(
        $('<input name="" value=pineapple>').serializeArray(),
      ).toStrictEqual([]);
      expect(
        $('<input name="fruit" value=pineapple>').serializeArray(),
      ).toStrictEqual([
        {
          name: 'fruit',
          value: 'pineapple',
        },
      ]);
    });

    it('() : should serialize inputs without value attributes', () => {
      expect($('<input name="fruit">').serializeArray()).toStrictEqual([
        {
          name: 'fruit',
          value: '',
        },
      ]);
    });
  });

  describe('.serialize', () => {
    it('() : should get form controls', () => {
      expect($('form#simple').serialize()).toBe('fruit=Apple');
    });

    it('() : should get nested form controls', () => {
      expect($('form#nested').serialize()).toBe('fruit=Apple&vegetable=Carrot');
    });

    it('() : should not get disabled form controls', () => {
      expect($('form#disabled').serialize()).toBe('');
    });

    it('() : should get multiple selected options', () => {
      expect($('form#multiple').serialize()).toBe('fruit=Apple&fruit=Orange');
    });

    it("() : should encode spaces as +'s", () => {
      expect($('form#spaces').serialize()).toBe('fruit=Blood+orange');
    });
  });
});
```

## File: `src/api/forms.ts`
```typescript
import { type AnyNode, isTag } from 'domhandler';
import type { Cheerio } from '../cheerio.js';

/*
 * https://github.com/jquery/jquery/blob/2.1.3/src/manipulation/var/rcheckableType.js
 * https://github.com/jquery/jquery/blob/2.1.3/src/serialize.js
 */
const submittableSelector = 'input,select,textarea,keygen';
const r20 = /%20/g;
const rCRLF = /\r?\n/g;

/**
 * Encode a set of form elements as a string for submission.
 *
 * @category Forms
 * @example
 *
 * ```js
 * $('<form><input name="foo" value="bar" /></form>').serialize();
 * //=> 'foo=bar'
 * ```
 *
 * @returns The serialized form.
 * @see {@link https://api.jquery.com/serialize/}
 */
export function serialize<T extends AnyNode>(this: Cheerio<T>): string {
  // Convert form elements into name/value objects
  const arr = this.serializeArray();

  // Serialize each element into a key/value string
  const retArr = arr.map(
    (data) =>
      `${encodeURIComponent(data.name)}=${encodeURIComponent(data.value)}`,
  );

  // Return the resulting serialization
  return retArr.join('&').replace(r20, '+');
}

/**
 * Encode a set of form elements as an array of names and values.
 *
 * @category Forms
 * @example
 *
 * ```js
 * $('<form><input name="foo" value="bar" /></form>').serializeArray();
 * //=> [ { name: 'foo', value: 'bar' } ]
 * ```
 *
 * @returns The serialized form.
 * @see {@link https://api.jquery.com/serializeArray/}
 */
export function serializeArray<T extends AnyNode>(
  this: Cheerio<T>,
): {
  name: string;
  value: string;
}[] {
  // Resolve all form elements from either forms or collections of form elements
  return this.map((_, elem) => {
    const $elem = this._make(elem);
    if (isTag(elem) && elem.name === 'form') {
      return $elem.find(submittableSelector).toArray();
    }
    return $elem.filter(submittableSelector).toArray();
  })
    .filter(
      // Verify elements have a name (`attr.name`) and are not disabled (`:enabled`)
      '[name!=""]:enabled' +
        // And cannot be clicked (`[type=submit]`) or are used in `x-www-form-urlencoded` (`[type=file]`)
        ':not(:submit, :button, :image, :reset, :file)' +
        // And are either checked/don't have a checkable state
        ':matches([checked], :not(:checkbox, :radio))',
      // Convert each of the elements to its value(s)
    )
    .map<
      AnyNode,
      {
        name: string;
        value: string;
      }
    >((_, elem) => {
      const $elem = this._make(elem);
      const name = $elem.attr('name');
      if (!name) return [];
      // If there is no value set (e.g. `undefined`, `null`), then default value to empty
      const value = $elem.val() ?? '';

      // If we have an array of values (e.g. `<select multiple>`), return an array of key/value pairs
      if (Array.isArray(value)) {
        return value.map((val) =>
          /*
           * We trim replace any line endings (e.g. `\r` or `\r\n` with `\r\n`) to guarantee consistency across platforms
           * These can occur inside of `<textarea>'s`
           */
          ({ name, value: val.replace(rCRLF, '\r\n') }),
        );
      }
      // Otherwise (e.g. `<input type="text">`, return only one key/value pair
      return { name, value: value.replace(rCRLF, '\r\n') };
    })
    .toArray();
}
```

## File: `src/api/manipulation.spec.ts`
```typescript
import type { AnyNode, Element } from 'domhandler';
import { beforeEach, describe, expect, it } from 'vitest';
import {
  divcontainers,
  fruits,
  mixedText,
  unwrapspans,
} from '../__fixtures__/fixtures.js';
import { type Cheerio, type CheerioAPI, load } from '../index.js';

describe('$(...)', () => {
  let $: CheerioAPI;
  let $fruits: Cheerio<Element>;

  beforeEach(() => {
    $ = load(fruits);
    $fruits = $('#fruits');
  });

  describe('.wrap', () => {
    it('(Cheerio object) : should insert the element and add selected element(s) as its child', () => {
      const $redFruits = $('<div class="red-fruits"></div>');
      $('.apple').wrap($redFruits);

      expect($fruits.children().eq(0).hasClass('red-fruits')).toBe(true);
      expect($('.red-fruits').children().eq(0).hasClass('apple')).toBe(true);
      expect($fruits.children().eq(1).hasClass('orange')).toBe(true);
      expect($redFruits.children()).toHaveLength(1);
    });

    it('(element) : should wrap the base element correctly', () => {
      $('ul').wrap('<a></a>');
      expect($('body').children()[0].tagName).toBe('a');
    });

    it('(document) : should ignore document node', () => {
      $.root().wrap('<a></a>');
      expect($.root()[0]).toHaveProperty('type', 'root');
    });

    it('(element) : should insert the element and add selected element(s) as its child', () => {
      const $redFruits = $('<div class="red-fruits"></div>');
      $('.apple').wrap($redFruits[0]);

      expect($fruits.children()[0]).toBe($redFruits[0]);
      expect($redFruits.children()).toHaveLength(1);
      expect($redFruits.children()[0]).toBe($('.apple')[0]);
      expect($fruits.children()[1]).toBe($('.orange')[0]);
    });

    it('(html) : should insert the markup and add selected element(s) as its child', () => {
      $('.apple').wrap('<div class="red-fruits"> </div>');
      expect($fruits.children().eq(0).hasClass('red-fruits')).toBe(true);
      expect($('.red-fruits').children().eq(0).hasClass('apple')).toBe(true);
      expect($fruits.children().eq(1).hasClass('orange')).toBe(true);
      expect($('.red-fruits').children()).toHaveLength(1);
    });

    it('(html) : discards extraneous markup', () => {
      $('.apple').wrap('<div></div><p></p>');
      expect($('div')).toHaveLength(1);
      expect($('p')).toHaveLength(0);
    });

    it('(html) : wraps with nested elements', () => {
      const $orangeFruits = $(
        '<div class="orange-fruits"><div class="and-stuff"></div></div>',
      );
      $('.orange').wrap($orangeFruits);

      expect($fruits.children().eq(1).hasClass('orange-fruits')).toBe(true);
      expect($('.orange-fruits').children().eq(0).hasClass('and-stuff')).toBe(
        true,
      );
      expect($fruits.children().eq(2).hasClass('pear')).toBe(true);
      expect($('.orange-fruits').children()).toHaveLength(1);
    });

    it('(html) : should only worry about the first tag children', () => {
      const delicious = '<span> This guy is delicious: <b></b></span>';
      $('.apple').wrap(delicious);
      expect($('b>.apple')).toHaveLength(1);
    });

    it('(selector) : wraps the content with a copy of the first matched element', () => {
      $('.apple').wrap('.orange, .pear');

      const $oranges = $('.orange');
      expect($('.pear')).toHaveLength(1);
      expect($oranges).toHaveLength(2);
      expect($oranges.eq(0).parent()[0]).toBe($fruits[0]);
      expect($oranges.eq(0).children()).toHaveLength(1);
      expect($oranges.eq(0).children()[0]).toBe($('.apple')[0]);
      expect($('.apple').parent()[0]).toBe($oranges[0]);
      expect($oranges.eq(1).children()).toHaveLength(0);
    });

    it('(fn) : should invoke the provided function with the correct arguments and context', () => {
      const $children = $fruits.children();
      const args: [number, AnyNode][] = [];
      const thisValues: AnyNode[] = [];

      $children.wrap(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return '';
      });

      expect(args).toStrictEqual([
        [0, $children[0]],
        [1, $children[1]],
        [2, $children[2]],
      ]);
      expect(thisValues).toStrictEqual([
        $children[0],
        $children[1],
        $children[2],
      ]);
    });

    it('(fn) : should use the returned HTML to wrap each element', () => {
      const $children = $fruits.children();
      const tagNames = ['div', 'span', 'p'];

      $children.wrap(() => `<${tagNames.shift()}>`);

      expect($fruits.find('div')).toHaveLength(1);
      expect($fruits.find('div')[0]).toBe($fruits.children()[0]);
      expect($fruits.find('.apple')).toHaveLength(1);
      expect($fruits.find('.apple').parent()[0]).toBe($fruits.find('div')[0]);

      expect($fruits.find('span')).toHaveLength(1);
      expect($fruits.find('span')[0]).toBe($fruits.children()[1]);
      expect($fruits.find('.orange')).toHaveLength(1);
      expect($fruits.find('.orange').parent()[0]).toBe($fruits.find('span')[0]);

      expect($fruits.find('p')).toHaveLength(1);
      expect($fruits.find('p')[0]).toBe($fruits.children()[2]);
      expect($fruits.find('.pear')).toHaveLength(1);
      expect($fruits.find('.pear').parent()[0]).toBe($fruits.find('p')[0]);
    });

    it('(fn) : should use the returned Cheerio object to wrap each element', () => {
      const $children = $fruits.children();
      const tagNames = ['span', 'p', 'div'];

      $children.wrap(() => $(`<${tagNames.shift()}>`));

      expect($fruits.find('span')).toHaveLength(1);
      expect($fruits.find('span')[0]).toBe($fruits.children()[0]);
      expect($fruits.find('.apple')).toHaveLength(1);
      expect($fruits.find('.apple').parent()[0]).toBe($fruits.find('span')[0]);

      expect($fruits.find('p')).toHaveLength(1);
      expect($fruits.find('p')[0]).toBe($fruits.children()[1]);
      expect($fruits.find('.orange')).toHaveLength(1);
      expect($fruits.find('.orange').parent()[0]).toBe($fruits.find('p')[0]);

      expect($fruits.find('div')).toHaveLength(1);
      expect($fruits.find('div')[0]).toBe($fruits.children()[2]);
      expect($fruits.find('.pear')).toHaveLength(1);
      expect($fruits.find('.pear').parent()[0]).toBe($fruits.find('div')[0]);
    });

    it('($(...)) : for each element it should add a wrapper element and add the selected element as its child', () => {
      const $fruitDecorator = $('<div class="fruit-decorator"></div>');
      $('li').wrap($fruitDecorator);
      expect($fruits.children().eq(0).hasClass('fruit-decorator')).toBe(true);
      expect($fruits.children().eq(0).children().eq(0).hasClass('apple')).toBe(
        true,
      );
      expect($fruits.children().eq(1).hasClass('fruit-decorator')).toBe(true);
      expect($fruits.children().eq(1).children().eq(0).hasClass('orange')).toBe(
        true,
      );
      expect($fruits.children().eq(2).hasClass('fruit-decorator')).toBe(true);
      expect($fruits.children().eq(2).children().eq(0).hasClass('pear')).toBe(
        true,
      );
    });
  });

  describe('.wrapInner', () => {
    it('(Cheerio object) : should insert the element and add selected element(s) as its parent', () => {
      const $container = $('<div class="container"></div>') as Cheerio<Element>;
      $fruits.wrapInner($container);

      expect($fruits.children()[0]).toBe($container[0]);
      expect($container[0].parent).toBe($fruits[0]);
      expect($container[0].children[0]).toBe($('.apple')[0]);
      expect($container[0].children[1]).toBe($('.orange')[0]);
      expect($('.apple')[0].parent).toBe($container[0]);
      expect($fruits.children()).toHaveLength(1);
      expect($container.children()).toHaveLength(3);
    });

    it('(element) : should insert the element and add selected element(s) as its parent', () => {
      const $container = $('<div class="container"></div>') as Cheerio<Element>;
      $fruits.wrapInner($container[0]);

      expect($fruits.children()[0]).toBe($container[0]);
      expect($container[0].parent).toBe($fruits[0]);
      expect($container[0].children[0]).toBe($('.apple')[0]);
      expect($container[0].children[1]).toBe($('.orange')[0]);
      expect($('.apple')[0].parent).toBe($container[0]);
      expect($fruits.children()).toHaveLength(1);
      expect($container.children()).toHaveLength(3);
    });

    it('(html) : should ignore text nodes', () => {
      const $test = load(mixedText);
      $test($test('body')[0].children).wrapInner('<test>');

      expect($test('body').html()).toBe(
        '<a><test>1</test></a>TEXT<b><test>2</test></b>',
      );
    });

    it('(html) : should insert the element and add selected element(s) as its parent', () => {
      $fruits.wrapInner('<div class="container"></div>');

      expect($fruits.children()[0]).toBe($('.container')[0]);
      expect($('.container')[0].parent).toBe($fruits[0]);
      expect($('.container')[0].children[0]).toBe($('.apple')[0]);
      expect($('.container')[0].children[1]).toBe($('.orange')[0]);
      expect($('.apple')[0].parent).toBe($('.container')[0]);
      expect($fruits.children()).toHaveLength(1);
      expect($('.container').children()).toHaveLength(3);
    });

    it("(selector) : should wrap the html of the element with the selector's first match", () => {
      $('.apple').wrapInner('.orange, .pear');
      const $oranges = $('.orange');
      expect($('.pear')).toHaveLength(1);
      expect($oranges).toHaveLength(2);
      expect($oranges.eq(0).parent()[0]).toBe($('.apple')[0]);
      expect($oranges.eq(0).text()).toBe('Apple');
      expect($('.apple').eq(0).children()[0]).toBe($oranges[0]);
      expect($oranges.eq(1).parent()[0]).toBe($fruits[0]);
      expect($oranges.eq(1).text()).toBe('Orange');
    });

    it('(fn) : should invoke the provided function with the correct arguments and context', () => {
      const $children = $fruits.children();
      const args: [number, AnyNode][] = [];
      const thisValues: AnyNode[] = [];

      $children.wrapInner(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return this;
      });

      expect(args).toStrictEqual([
        [0, $children[0]],
        [1, $children[1]],
        [2, $children[2]],
      ]);
      expect(thisValues).toStrictEqual([
        $children[0],
        $children[1],
        $children[2],
      ]);
    });

    it("(fn) : should use the returned HTML to wrap each element's contents", () => {
      const $children = $fruits.children();
      const tagNames = ['div', 'span', 'p'];

      $children.wrapInner(() => `<${tagNames.shift()}>`);

      expect($fruits.find('div')).toHaveLength(1);
      expect($fruits.find('div')[0]).toBe($('.apple').children()[0]);
      expect($fruits.find('.apple')).toHaveLength(1);

      expect($fruits.find('span')).toHaveLength(1);
      expect($fruits.find('span')[0]).toBe($('.orange').children()[0]);
      expect($fruits.find('.orange')).toHaveLength(1);

      expect($fruits.find('p')).toHaveLength(1);
      expect($fruits.find('p')[0]).toBe($('.pear').children()[0]);
      expect($fruits.find('.pear')).toHaveLength(1);
    });

    it("(fn) : should use the returned Cheerio object to wrap each element's contents", () => {
      const $children = $fruits.children();
      const tags = [$('<div></div>'), $('<span></span>'), $('<p></p>')];

      $children.wrapInner(() => tags.shift()!);

      expect($fruits.find('div')).toHaveLength(1);
      expect($fruits.find('div')[0]).toBe($('.apple').children()[0]);
      expect($fruits.find('.apple')).toHaveLength(1);

      expect($fruits.find('span')).toHaveLength(1);
      expect($fruits.find('span')[0]).toBe($('.orange').children()[0]);
      expect($fruits.find('.orange')).toHaveLength(1);

      expect($fruits.find('p')).toHaveLength(1);
      expect($fruits.find('p')[0]).toBe($('.pear').children()[0]);
      expect($fruits.find('.pear')).toHaveLength(1);
    });

    it('($(...)) : for each element it should add a wrapper element and add the selected element as its child', () => {
      const $fruitDecorator = $('<div class="fruit-decorator"></div>');
      const $children = $fruits.children();
      $('li').wrapInner($fruitDecorator);

      expect($('.fruit-decorator')).toHaveLength(3);
      expect($children.eq(0).children().eq(0).hasClass('fruit-decorator')).toBe(
        true,
      );
      expect($children.eq(0).hasClass('apple')).toBe(true);
      expect($children.eq(1).children().eq(0).hasClass('fruit-decorator')).toBe(
        true,
      );
      expect($children.eq(1).hasClass('orange')).toBe(true);
      expect($children.eq(2).children().eq(0).hasClass('fruit-decorator')).toBe(
        true,
      );
      expect($children.eq(2).hasClass('pear')).toBe(true);
    });

    it('(html) : wraps with nested elements', () => {
      const $badOrangeJoke = $(
        '<div class="orange-you-glad"><div class="i-didnt-say-apple"></div></div>',
      );
      $('.orange').wrapInner($badOrangeJoke);

      expect($('.orange').children().eq(0).hasClass('orange-you-glad')).toBe(
        true,
      );
      expect(
        $('.orange-you-glad').children().eq(0).hasClass('i-didnt-say-apple'),
      ).toBe(true);
      expect($fruits.children().eq(2).hasClass('pear')).toBe(true);
      expect($('.orange-you-glad').children()).toHaveLength(1);
    });

    it('(html) : should only worry about the first tag children', () => {
      const delicious = '<span> This guy is delicious: <b></b></span>';
      $('.apple').wrapInner(delicious);
      expect($('.apple>span>b')).toHaveLength(1);
      expect($('.apple>span>b').text()).toBe('Apple');
    });
  });

  describe('.unwrap', () => {
    let $elem: CheerioAPI;

    beforeEach(() => {
      $elem = load(unwrapspans);
    });

    it('() : should be unwrap span elements', () => {
      const abcd = $elem('#unwrap1 > span, #unwrap2 > span').get();
      const abcdef = $elem('#unwrap span').get();

      // Make #unwrap1 and #unwrap2 go away
      expect(
        $elem('#unwrap1 span').add('#unwrap2 span:first-child').unwrap(),
      ).toHaveLength(3);

      /*
       * .toEqual
       *  all four spans should still exist
       */
      expect($elem('#unwrap > span').get()).toEqual(abcd);

      // Make all b elements in #unwrap3 go away
      expect($elem('#unwrap3 span').unwrap().get()).toEqual(
        $elem('#unwrap3 > span').get(),
      );

      // Make #unwrap3 go away
      expect($elem('#unwrap3 span').unwrap().get()).toEqual(
        $elem('#unwrap > span.unwrap3').get(),
      );

      // #unwrap only contains 6 child spans
      expect($elem('#unwrap').children().get()).toEqual(abcdef);

      // Make the 6 spans become children of body
      expect($elem('#unwrap > span').unwrap().get()).toEqual(
        $elem('body > span.unwrap').get(),
      );

      // Can't unwrap children of body
      expect($elem('body > span.unwrap').unwrap().get()).toEqual(
        $elem('body > span.unwrap').get(),
      );

      // Can't unwrap children of body
      expect($elem('body > span.unwrap').unwrap().get()).toEqual(abcdef);

      // Can't unwrap children of body
      expect($elem('body > span.unwrap').get()).toEqual(abcdef);
    });

    it('(selector) : should only unwrap element parent what specified', () => {
      const abcd = $elem('#unwrap1 > span, #unwrap2 > span').get();

      // Shouldn't unwrap, no match
      $elem('#unwrap1 span').unwrap('#unwrap2');
      expect($elem('#unwrap1')).toHaveLength(1);

      // Shouldn't unwrap, no match
      $elem('#unwrap1 span').unwrap('span');
      expect($elem('#unwrap1')).toHaveLength(1);

      // Unwraps
      $elem('#unwrap1 span').unwrap('#unwrap1');
      expect($elem('#unwrap1')).toHaveLength(0);

      // Should not unwrap - unmatched unwrap
      $elem('#unwrap2 span').unwrap('quote');
      expect($elem('#unwrap > span')).toHaveLength(2);

      // Check return values - matched unwrap
      $elem('#unwrap2 span').unwrap('#unwrap2');
      expect($elem('#unwrap > span').get()).toEqual(abcd);
    });
  });

  describe('.wrapAll', () => {
    let doc: CheerioAPI;
    let $inner: Cheerio<Element>;

    beforeEach(() => {
      doc = load(divcontainers);
      $inner = doc('.inner');
    });

    it('(Cheerio object) : should insert the element and wrap elements with it', () => {
      $inner.wrapAll(doc('#new'));
      const $container = doc('.container');
      const $wrap = doc('b');

      expect($container).toHaveLength(2);
      expect($container[0].children).toHaveLength(1);
      expect($container[1].children).toHaveLength(0);
      expect($container[0].children[0]).toBe(doc('#new')[0]);

      expect($inner).toHaveLength(4);
      expect($wrap[0].children).toHaveLength(4);
      expect($inner[0].parent).toBe($wrap[0]);
      expect($inner[1].parent).toBe($wrap[0]);
      expect($inner[2].parent).toBe($wrap[0]);
      expect($inner[3].parent).toBe($wrap[0]);
    });

    it('(html) : should wrap elements with it', () => {
      $inner.wrapAll('<div class="wrap"></div>');
      const $container = doc('.container');
      const $wrap = doc('.wrap');

      expect($inner).toHaveLength(4);
      expect($container).toHaveLength(2);
      expect($wrap).toHaveLength(1);
      expect($wrap[0].children).toHaveLength(4);
      expect($container[0].children).toHaveLength(1);
      expect($container[1].children).toHaveLength(0);
      expect($inner[0].parent).toBe($wrap[0]);
      expect($inner[1].parent).toBe($wrap[0]);
      expect($inner[2].parent).toBe($wrap[0]);
      expect($inner[3].parent).toBe($wrap[0]);
      expect($wrap[0].parent).toBe($container[0]);
      expect($container[0].children[0]).toBe($wrap[0]);
    });

    it('(html) : should wrap single element with it', () => {
      const parent = doc('<p>').wrapAll('<div></div>').parent();
      expect(parent).toHaveLength(1);
      expect(parent.is('div')).toBe(true);
    });

    it('(selector) : should find element from dom, wrap elements with it', () => {
      $inner.wrapAll('#new');
      const $container = doc('.container');
      const $wrap = doc('b');
      const $new = doc('#new');

      expect($inner).toHaveLength(4);
      expect($container).toHaveLength(2);
      expect($container[0].children).toHaveLength(1);
      expect($container[1].children).toHaveLength(0);
      expect($wrap[0].children).toHaveLength(4);
      expect($inner[0].parent).toBe($wrap[0]);
      expect($inner[1].parent).toBe($wrap[0]);
      expect($inner[2].parent).toBe($wrap[0]);
      expect($inner[3].parent).toBe($wrap[0]);
      expect($new[0].parent).toBe($container[0]);
      expect($container[0].children[0]).toBe($new[0]);
    });

    it('(function) : check execution', () => {
      const $container = doc('.container');
      const p = $container[0].parent;

      const result = $container.wrapAll(
        () => "<div class='red'><div class='tmp'></div></div>",
      );

      expect(result.parent()).toHaveLength(1);
      expect($container.eq(0).parent().parent().is('.red')).toBe(true);
      expect($container.eq(1).parent().parent().is('.red')).toBe(true);
      expect($container.eq(0).parent().parent().parent().is(p)).toBe(true);
    });

    it('(function) : check execution characteristics', () => {
      const $new = doc('#new');
      let i = 0;

      doc('no-result').wrapAll(() => {
        i++;
        return '';
      });
      expect(i).toBeFalsy();

      $new.wrapAll(function (index) {
        expect(this).toBe($new[0]);
        expect(index).toBe(0);
        return this;
      });
    });

    it('(nodes) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.wrapAll($text('body')[0].children.slice(1));

      expect($text('body').html()).toBe('TEXT<b>2<a>1</a>TEXT<b>2</b></b>');
    });
  });

  describe('.append', () => {
    it('() : should do nothing', () => {
      expect($('#fruits').append()[0].tagName).toBe('ul');
    });

    it('(null) :  should do nothing', () => {
      $fruits.append(null as never);
      expect($fruits.children()).toHaveLength(3);
    });

    it('(html) : should add element as last child', () => {
      $fruits.append('<li class="plum">Plum</li>');
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
    });

    it('(html) : should not fail on text nodes', () => {
      expect($(mixedText).append(' UP').html()).toBe('1 UP');
    });

    it('($(...)) : should add element as last child', () => {
      const $plum = $('<li class="plum">Plum</li>');
      $fruits.append($plum);
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
    });

    it('(Node) : should add element as last child', () => {
      const plum = $('<li class="plum">Plum</li>')[0];
      $fruits.append(plum);
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
    });

    it('(existing Node) : should remove node from previous location', () => {
      const apple = $fruits.children()[0];

      expect($fruits.children()).toHaveLength(3);
      $fruits.append(apple);
      const $children = $fruits.children();

      expect($children).toHaveLength(3);
      expect($children[0]).not.toBe(apple);
      expect($children[2]).toBe(apple);
    });

    it('(existing Node) : should remove existing node from previous location', () => {
      const apple = $fruits.children()[0];
      const $dest = $('<div></div>');

      expect($fruits.children()).toHaveLength(3);
      $dest.append(apple);
      const $children = $fruits.children();

      expect($children).toHaveLength(2);
      expect($children[0]).not.toBe(apple);

      expect($dest.children()).toHaveLength(1);
      expect($dest.children()[0]).toBe(apple);
    });

    it('(existing Node) : should update original direct siblings', () => {
      $('.pear').append($('.orange'));
      expect($('.apple').next()[0]).toBe($('.pear')[0]);
      expect($('.pear').prev()[0]).toBe($('.apple')[0]);
    });

    it('(existing Node) : should clone all but the last occurrence', () => {
      const $originalApple = $('.apple');

      $('.orange, .pear').append($originalApple);

      const $apples = $('.apple');
      expect($apples).toHaveLength(2);
      expect($apples.eq(0).parent()[0]).toBe($('.orange')[0]);
      expect($apples.eq(1).parent()[0]).toBe($('.pear')[0]);
      expect($apples[1]).toBe($originalApple[0]);
    });

    it('(elem) : should NOP if removed', () => {
      const $apple = $('.apple');

      $apple.remove();
      $fruits.append($apple);
      expect($fruits.children().eq(2).hasClass('apple')).toBe(true);
    });

    it('($(...), html) : should add multiple elements as last children', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const grape = '<li class="grape">Grape</li>';
      $fruits.append($plum, grape);
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(4).hasClass('grape')).toBe(true);
    });

    it('(Array) : should append all elements in the array', () => {
      const more = $(
        '<li class="plum">Plum</li><li class="grape">Grape</li>',
      ).get();
      $fruits.append(more);
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(4).hasClass('grape')).toBe(true);
    });

    it('(fn) : should invoke the callback with the correct arguments and context', () => {
      const $fruits = $('#fruits').children();
      const args: [number, string][] = [];
      const thisValues: AnyNode[] = [];

      $fruits.append(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return this;
      });

      expect(args).toStrictEqual([
        [0, 'Apple'],
        [1, 'Orange'],
        [2, 'Pear'],
      ]);
      expect(thisValues).toStrictEqual([$fruits[0], $fruits[1], $fruits[2]]);
    });

    it('(fn) : should add returned string as last child', () => {
      const $fruits = $('#fruits').children();

      $fruits.append(() => '<div class="first">');

      const $apple = $fruits.eq(0);
      const $orange = $fruits.eq(1);
      const $pear = $fruits.eq(2);

      expect($apple.find('.first')[0]).toBe($apple.contents()[1]);
      expect($orange.find('.first')[0]).toBe($orange.contents()[1]);
      expect($pear.find('.first')[0]).toBe($pear.contents()[1]);
    });

    it('(fn) : should add returned Cheerio object as last child', () => {
      const $fruits = $('#fruits').children();

      $fruits.append(() => $('<div class="second">'));

      const $apple = $fruits.eq(0);
      const $orange = $fruits.eq(1);
      const $pear = $fruits.eq(2);

      expect($apple.find('.second')[0]).toBe($apple.contents()[1]);
      expect($orange.find('.second')[0]).toBe($orange.contents()[1]);
      expect($pear.find('.second')[0]).toBe($pear.contents()[1]);
    });

    it('(fn) : should add returned Node as last child', () => {
      const $fruits = $('#fruits').children();

      $fruits.append(() => $('<div class="third">')[0]);

      const $apple = $fruits.eq(0);
      const $orange = $fruits.eq(1);
      const $pear = $fruits.eq(2);

      expect($apple.find('.third')[0]).toBe($apple.contents()[1]);
      expect($orange.find('.third')[0]).toBe($orange.contents()[1]);
      expect($pear.find('.third')[0]).toBe($pear.contents()[1]);
    });

    it('should maintain correct object state (Issue: #10)', () => {
      const $obj = $('<div></div>')
        .append('<div><div></div></div>')
        .children()
        .children()
        .parent();
      expect($obj).toBeTruthy();
    });

    it('($(...)) : should remove from root element', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const { parent } = $plum[0];
      expect(parent).toBeTruthy();

      $fruits.append($plum);
      expect($plum[0].parent?.type).not.toBe('root');
      expect(parent?.childNodes).not.toContain($plum[0]);
    });
  });

  describe('.prepend', () => {
    it('() : should do nothing', () => {
      expect($('#fruits').prepend()[0].tagName).toBe('ul');
    });

    it('(html) : should add element as first child', () => {
      $fruits.prepend('<li class="plum">Plum</li>');
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
    });

    it('($(...)) : should add element as first child', () => {
      const $plum = $('<li class="plum">Plum</li>');
      $fruits.prepend($plum);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
    });

    it('($(...)) : should add style element as first child', () => {
      const $style = $('<style>.foo {}</style>');
      $fruits.prepend($style);
      const styleTag = $fruits.children().get(0);
      expect(styleTag?.tagName).toBe('style');
      expect(styleTag?.children[0]).toHaveProperty('data', '.foo {}');
    });

    it('($(...)) : should add script element as first child', () => {
      const $script = $('<script>var foo;</script>');
      $fruits.prepend($script);
      const scriptTag = $fruits.children().get(0);
      expect(scriptTag?.tagName).toBe('script');
      expect(scriptTag?.children[0]).toHaveProperty('data', 'var foo;');
    });

    it('(Node) : should add node as first child', () => {
      const plum = $('<li class="plum">Plum</li>')[0];
      $fruits.prepend(plum);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
    });

    it('(existing Node) : should remove existing nodes from previous locations', () => {
      const pear = $fruits.children()[2];

      expect($fruits.children()).toHaveLength(3);
      $fruits.prepend(pear);
      const $children = $fruits.children();

      expect($children).toHaveLength(3);
      expect($children[2]).not.toBe(pear);
      expect($children[0]).toBe(pear);
    });

    it('(existing Node) : should update original direct siblings', () => {
      $('.pear').prepend($('.orange'));
      expect($('.apple').next()[0]).toBe($('.pear')[0]);
      expect($('.pear').prev()[0]).toBe($('.apple')[0]);
    });

    it('(existing Node) : should clone all but the last occurrence', () => {
      const $originalApple = $('.apple');

      $('.orange, .pear').prepend($originalApple);

      const $apples = $('.apple');
      expect($apples).toHaveLength(2);
      expect($apples.eq(0).parent()[0]).toBe($('.orange')[0]);
      expect($apples.eq(1).parent()[0]).toBe($('.pear')[0]);
      expect($apples[1]).toBe($originalApple[0]);
    });

    it('(elem) : should handle if removed', () => {
      const $apple = $('.apple');

      $apple.remove();
      $fruits.prepend($apple);
      expect($fruits.children().eq(0).hasClass('apple')).toBe(true);
    });

    it('(Array) : should add all elements in the array as initial children', () => {
      const more = $(
        '<li class="plum">Plum</li><li class="grape">Grape</li>',
      ).get();
      $fruits.prepend(more);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(1).hasClass('grape')).toBe(true);
    });

    it('(html, $(...), html) : should add multiple elements as first children', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const grape = '<li class="grape">Grape</li>';
      $fruits.prepend($plum, grape);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(1).hasClass('grape')).toBe(true);
    });

    it('(fn) : should invoke the callback with the correct arguments and context', () => {
      const args: [number, string][] = [];
      const thisValues: AnyNode[] = [];
      const $fruits = $('#fruits').children();

      $fruits.prepend(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return this;
      });

      expect(args).toStrictEqual([
        [0, 'Apple'],
        [1, 'Orange'],
        [2, 'Pear'],
      ]);
      expect(thisValues).toStrictEqual([$fruits[0], $fruits[1], $fruits[2]]);
    });

    it('(fn) : should add returned string as first child', () => {
      const $fruits = $('#fruits').children();

      $fruits.prepend(() => '<div class="first">');

      const $apple = $fruits.eq(0);
      const $orange = $fruits.eq(1);
      const $pear = $fruits.eq(2);

      expect($apple.find('.first')[0]).toBe($apple.contents()[0]);
      expect($orange.find('.first')[0]).toBe($orange.contents()[0]);
      expect($pear.find('.first')[0]).toBe($pear.contents()[0]);
    });

    it('(fn) : should add returned Cheerio object as first child', () => {
      const $fruits = $('#fruits').children();

      $fruits.prepend(() => $('<div class="second">'));

      const $apple = $fruits.eq(0);
      const $orange = $fruits.eq(1);
      const $pear = $fruits.eq(2);

      expect($apple.find('.second')[0]).toBe($apple.contents()[0]);
      expect($orange.find('.second')[0]).toBe($orange.contents()[0]);
      expect($pear.find('.second')[0]).toBe($pear.contents()[0]);
    });

    it('(fn) : should add returned Node as first child', () => {
      const $fruits = $('#fruits').children();

      $fruits.prepend(() => $('<div class="third">')[0]);

      const $apple = $fruits.eq(0);
      const $orange = $fruits.eq(1);
      const $pear = $fruits.eq(2);

      expect($apple.find('.third')[0]).toBe($apple.contents()[0]);
      expect($orange.find('.third')[0]).toBe($orange.contents()[0]);
      expect($pear.find('.third')[0]).toBe($pear.contents()[0]);
    });

    it('($(...)) : should remove from root element', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const root = $plum[0].parent;
      expect(root?.type).toBe('root');

      $fruits.prepend($plum);
      expect($plum[0].parent?.type).not.toBe('root');
      expect(root?.childNodes).not.toContain($plum[0]);
    });
  });

  describe('.appendTo', () => {
    it('(html) : should add element as last child', () => {
      const $plum = $('<li class="plum">Plum</li>').appendTo(fruits);
      expect($plum.parent().children().eq(3).hasClass('plum')).toBe(true);
    });

    it('($(...)) : should add element as last child', () => {
      $('<li class="plum">Plum</li>').appendTo($fruits);
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
    });

    it('(Node) : should add element as last child', () => {
      $('<li class="plum">Plum</li>').appendTo($fruits[0]);
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
    });

    it('(selector) : should add element as last child', () => {
      $('<li class="plum">Plum</li>').appendTo('#fruits');
      expect($fruits.children().eq(3).hasClass('plum')).toBe(true);
    });

    it('(Array) : should add element as last child of all elements in the array', () => {
      const $multiple = $('<ul><li>Apple</li></ul><ul><li>Orange</li></ul>');
      $('<li class="plum">Plum</li>').appendTo($multiple.get());
      expect($multiple.first().children().eq(1).hasClass('plum')).toBe(true);
      expect($multiple.last().children().eq(1).hasClass('plum')).toBe(true);
    });
  });

  describe('.prependTo', () => {
    it('(html) : should add element as first child', () => {
      const $plum = $('<li class="plum">Plum</li>').prependTo(fruits);
      expect($plum.parent().children().eq(0).hasClass('plum')).toBe(true);
    });

    it('($(...)) : should add element as first child', () => {
      $('<li class="plum">Plum</li>').prependTo($fruits);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
    });

    it('(Node) : should add node as first child', () => {
      $('<li class="plum">Plum</li>').prependTo($fruits[0]);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
    });

    it('(selector) : should add element as first child', () => {
      $('<li class="plum">Plum</li>').prependTo('#fruits');
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
    });

    it('(Array) : should add element as first child of all elements in the array', () => {
      const $multiple = $('<ul><li>Apple</li></ul><ul><li>Orange</li></ul>');
      $('<li class="plum">Plum</li>').prependTo($multiple.get());
      expect($multiple.first().children().eq(0).hasClass('plum')).toBe(true);
      expect($multiple.last().children().eq(0).hasClass('plum')).toBe(true);
    });
  });

  describe('.after', () => {
    it('() : should do nothing', () => {
      expect($fruits.after()[0].tagName).toBe('ul');
    });

    it('(html) : should add element as next sibling', () => {
      const grape = '<li class="grape">Grape</li>';
      $('.apple').after(grape);
      expect($('.apple').next().hasClass('grape')).toBe(true);
    });

    it('(Array) : should add all elements in the array as next sibling', () => {
      const more = $(
        '<li class="plum">Plum</li><li class="grape">Grape</li>',
      ).get();
      $('.apple').after(more);
      expect($fruits.children().eq(1).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(2).hasClass('grape')).toBe(true);
    });

    it('($(...)) : should add element as next sibling', () => {
      const $plum = $('<li class="plum">Plum</li>');
      $('.apple').after($plum);
      expect($('.apple').next().hasClass('plum')).toBe(true);
    });

    it('(Node) : should add element as next sibling', () => {
      const plum = $('<li class="plum">Plum</li>')[0];
      $('.apple').after(plum);
      expect($('.apple').next().hasClass('plum')).toBe(true);
    });

    it('(existing Node) : should remove existing nodes from previous locations', () => {
      const pear = $fruits.children()[2];

      $('.apple').after(pear);

      const $children = $fruits.children();
      expect($children).toHaveLength(3);
      expect($children[1]).toBe(pear);
    });

    it('(existing Node) : should update original direct siblings', () => {
      $('.pear').after($('.orange'));
      expect($('.apple').next()[0]).toBe($('.pear')[0]);
      expect($('.pear').prev()[0]).toBe($('.apple')[0]);
    });

    it('(existing Node) : should clone all but the last occurrence', () => {
      const $originalApple = $('.apple');
      $('.orange, .pear').after($originalApple);

      expect($('.apple')).toHaveLength(2);
      expect($('.apple').eq(0).prev()[0]).toBe($('.orange')[0]);
      expect($('.apple').eq(0).next()[0]).toBe($('.pear')[0]);
      expect($('.apple').eq(1).prev()[0]).toBe($('.pear')[0]);
      expect($('.apple').eq(1).next()).toHaveLength(0);
      expect($('.apple')[0]).not.toStrictEqual($originalApple[0]);
      expect($('.apple')[1]).toStrictEqual($originalApple[0]);
    });

    it('(elem) : should handle if removed', () => {
      const $apple = $('.apple');
      const $plum = $('<li class="plum">Plum</li>');

      $apple.remove();
      $apple.after($plum);
      expect($plum.prev()).toHaveLength(0);
    });

    it('($(...), html) : should add multiple elements as next siblings', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const grape = '<li class="grape">Grape</li>';
      $('.apple').after($plum, grape);
      expect($('.apple').next().hasClass('plum')).toBe(true);
      expect($('.plum').next().hasClass('grape')).toBe(true);
    });

    it('(fn) : should invoke the callback with the correct arguments and context', () => {
      const args: [number, string][] = [];
      const thisValues: AnyNode[] = [];
      const $fruits = $('#fruits').children();

      $fruits.after(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return this;
      });

      expect(args).toStrictEqual([
        [0, 'Apple'],
        [1, 'Orange'],
        [2, 'Pear'],
      ]);
      expect(thisValues).toStrictEqual([$fruits[0], $fruits[1], $fruits[2]]);
    });

    it('(fn) : should add returned string as next sibling', () => {
      const $fruits = $('#fruits').children();

      $fruits.after(() => '<li class="first">');

      expect($('.first')[0]).toBe($('#fruits').contents()[1]);
      expect($('.first')[1]).toBe($('#fruits').contents()[3]);
      expect($('.first')[2]).toBe($('#fruits').contents()[5]);
    });

    it('(fn) : should add returned Cheerio object as next sibling', () => {
      const $fruits = $('#fruits').children();

      $fruits.after(() => $('<li class="second">'));

      expect($('.second')[0]).toBe($('#fruits').contents()[1]);
      expect($('.second')[1]).toBe($('#fruits').contents()[3]);
      expect($('.second')[2]).toBe($('#fruits').contents()[5]);
    });

    it('(fn) : should add returned element as next sibling', () => {
      const $fruits = $('#fruits').children();

      $fruits.after(() => $('<li class="third">')[0]);

      expect($('.third')[0]).toBe($('#fruits').contents()[1]);
      expect($('.third')[1]).toBe($('#fruits').contents()[3]);
      expect($('.third')[2]).toBe($('#fruits').contents()[5]);
    });

    it('(fn) : should support text nodes', () => {
      const $text = load(mixedText);

      $text($text('body')[0].children).after(
        (_, content) => `<c>${content}added</c>`,
      );

      expect($text('body').html()).toBe(
        '<a>1</a><c>1added</c>TEXT<b>2</b><c>2added</c>',
      );
    });

    it('($(...)) : should remove from root element', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const root = $plum[0].parent;
      expect(root?.type).toBe('root');

      $fruits.after($plum);
      expect($plum[0].parent?.type).not.toBe('root');
      expect(root?.childNodes).not.toContain($plum[0]);
    });
  });

  describe('.insertAfter', () => {
    it('(selector) : should create element and add as next sibling', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertAfter('.apple');
      expect($('.apple').next().hasClass('grape')).toBe(true);
    });

    it('(selector) : should create element and add as next sibling of multiple elements', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertAfter('.apple, .pear');
      expect($('.apple').next().hasClass('grape')).toBe(true);
      expect($('.pear').next().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should create element and add as next sibling', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertAfter($('.apple'));
      expect($('.apple').next().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should create element and add as next sibling of multiple elements', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertAfter($('.apple, .pear'));
      expect($('.apple').next().hasClass('grape')).toBe(true);
      expect($('.pear').next().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should create all elements in the array and add as next siblings', () => {
      const more = $('<li class="plum">Plum</li><li class="grape">Grape</li>');
      more.insertAfter($('.apple'));
      expect($fruits.children().eq(0).hasClass('apple')).toBe(true);
      expect($fruits.children().eq(1).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(2).hasClass('grape')).toBe(true);
    });

    it('(existing Node) : should remove existing nodes from previous locations', () => {
      $('.orange').insertAfter('.pear');
      expect($fruits.children().eq(1).hasClass('orange')).toBe(false);
      expect($fruits.children().length).toBe(3);
      expect($('.orange').length).toBe(1);
    });

    it('(existing Node) : should update original direct siblings', () => {
      $('.orange').insertAfter('.pear');
      expect($('.apple').next().hasClass('pear')).toBe(true);
      expect($('.pear').prev().hasClass('apple')).toBe(true);
      expect($('.pear').next().hasClass('orange')).toBe(true);
      expect($('.orange').next()).toHaveLength(0);
    });

    it('(existing Node) : should update original direct siblings of multiple elements', () => {
      $('.apple').insertAfter('.orange, .pear');
      expect($('.orange').prev()).toHaveLength(0);
      expect($('.orange').next().hasClass('apple')).toBe(true);
      expect($('.pear').next().hasClass('apple')).toBe(true);
      expect($('.pear').prev().hasClass('apple')).toBe(true);
      expect($fruits.children().length).toBe(4);
      const apples = $('.apple');
      expect(apples.length).toBe(2);
      expect(apples.eq(0).prev().hasClass('orange')).toBe(true);
      expect(apples.eq(1).prev().hasClass('pear')).toBe(true);
    });

    it('(elem) : should handle if removed', () => {
      const $apple = $('.apple');
      const $plum = $('<li class="plum">Plum</li>');
      $apple.remove();
      $plum.insertAfter($apple);
      expect($plum.prev()).toHaveLength(0);
    });

    it('(single) should return the new element for chaining', () => {
      const $grape = $('<li class="grape">Grape</li>').insertAfter('.apple');
      expect($grape.cheerio).toBeTruthy();
      expect($grape.each).toBeTruthy();
      expect($grape.length).toBe(1);
      expect($grape.hasClass('grape')).toBe(true);
    });

    it('(single) should return the new elements for chaining', () => {
      const $purple = $(
        '<li class="grape">Grape</li><li class="plum">Plum</li>',
      ).insertAfter('.apple');
      expect($purple.cheerio).toBeTruthy();
      expect($purple.each).toBeTruthy();
      expect($purple.length).toBe(2);
      expect($purple.eq(0).hasClass('grape')).toBe(true);
      expect($purple.eq(1).hasClass('plum')).toBe(true);
    });

    it('(multiple) should return the new elements for chaining', () => {
      const $purple = $(
        '<li class="grape">Grape</li><li class="plum">Plum</li>',
      ).insertAfter('.apple, .pear');
      expect($purple.cheerio).toBeTruthy();
      expect($purple.each).toBeTruthy();
      expect($purple.length).toBe(4);
      expect($purple.eq(0).hasClass('grape')).toBe(true);
      expect($purple.eq(1).hasClass('plum')).toBe(true);
      expect($purple.eq(2).hasClass('grape')).toBe(true);
      expect($purple.eq(3).hasClass('plum')).toBe(true);
    });

    it('(single) should return the existing element for chaining', () => {
      const $pear = $('.pear').insertAfter('.apple');
      expect($pear.cheerio).toBeTruthy();
      expect($pear.each).toBeTruthy();
      expect($pear.length).toBe(1);
      expect($pear.hasClass('pear')).toBe(true);
    });

    it('(single) should return the existing elements for chaining', () => {
      const $things = $('.orange, .apple').insertAfter('.pear');
      expect($things.cheerio).toBeTruthy();
      expect($things.each).toBeTruthy();
      expect($things.length).toBe(2);
      expect($things.eq(0).hasClass('apple')).toBe(true);
      expect($things.eq(1).hasClass('orange')).toBe(true);
    });

    it('(multiple) should return the existing elements for chaining', () => {
      $('<li class="grape">Grape</li>').insertAfter('.apple');
      const $things = $('.orange, .apple').insertAfter('.pear, .grape');
      expect($things.cheerio).toBeTruthy();
      expect($things.each).toBeTruthy();
      expect($things.length).toBe(4);
      expect($things.eq(0).hasClass('apple')).toBe(true);
      expect($things.eq(1).hasClass('orange')).toBe(true);
      expect($things.eq(2).hasClass('apple')).toBe(true);
      expect($things.eq(3).hasClass('orange')).toBe(true);
    });
  });

  describe('.before', () => {
    it('() : should do nothing', () => {
      expect($('#fruits').before()[0].tagName).toBe('ul');
    });

    it('(html) : should add element as previous sibling', () => {
      const grape = '<li class="grape">Grape</li>';
      $('.apple').before(grape);
      expect($('.apple').prev().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should add element as previous sibling', () => {
      const $plum = $('<li class="plum">Plum</li>');
      $('.apple').before($plum);
      expect($('.apple').prev().hasClass('plum')).toBe(true);
    });

    it('(Node) : should add element as previous sibling', () => {
      const plum = $('<li class="plum">Plum</li>')[0];
      $('.apple').before(plum);
      expect($('.apple').prev().hasClass('plum')).toBe(true);
    });

    it('(existing Node) : should remove existing nodes from previous locations', () => {
      const pear = $fruits.children()[2];

      $('.apple').before(pear);

      const $children = $fruits.children();
      expect($children).toHaveLength(3);
      expect($children[0]).toBe(pear);
    });

    it('(existing Node) : should update original direct siblings', () => {
      $('.apple').before($('.orange'));
      expect($('.apple').next()[0]).toBe($('.pear')[0]);
      expect($('.pear').prev()[0]).toBe($('.apple')[0]);
    });

    it('(existing Node) : should clone all but the last occurrence', () => {
      const $originalPear = $('.pear');
      $('.apple, .orange').before($originalPear);

      expect($('.pear')).toHaveLength(2);
      expect($('.pear').eq(0).prev()).toHaveLength(0);
      expect($('.pear').eq(0).next()[0]).toBe($('.apple')[0]);
      expect($('.pear').eq(1).prev()[0]).toBe($('.apple')[0]);
      expect($('.pear').eq(1).next()[0]).toBe($('.orange')[0]);
      expect($('.pear')[0]).not.toStrictEqual($originalPear[0]);
      expect($('.pear')[1]).toStrictEqual($originalPear[0]);
    });

    it('(elem) : should handle if removed', () => {
      const $apple = $('.apple');
      const $plum = $('<li class="plum">Plum</li>');

      $apple.remove();
      $apple.before($plum);
      expect($plum.next()).toHaveLength(0);
    });

    it('(Array) : should add all elements in the array as previous sibling', () => {
      const more = $(
        '<li class="plum">Plum</li><li class="grape">Grape</li>',
      ).get();
      $('.apple').before(more);
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(1).hasClass('grape')).toBe(true);
    });

    it('($(...), html) : should add multiple elements as previous siblings', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const grape = '<li class="grape">Grape</li>';
      $('.apple').before($plum, grape);
      expect($('.apple').prev().hasClass('grape')).toBe(true);
      expect($('.grape').prev().hasClass('plum')).toBe(true);
    });

    it('(fn) : should invoke the callback with the correct arguments and context', () => {
      const args: [number, string][] = [];
      const thisValues: AnyNode[] = [];
      const $fruits = $('#fruits').children();

      $fruits.before(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return this;
      });

      expect(args).toStrictEqual([
        [0, 'Apple'],
        [1, 'Orange'],
        [2, 'Pear'],
      ]);
      expect(thisValues).toStrictEqual([$fruits[0], $fruits[1], $fruits[2]]);
    });

    it('(fn) : should add returned string as previous sibling', () => {
      const $fruits = $('#fruits').children();

      $fruits.before(() => '<li class="first">');

      expect($('.first')[0]).toBe($('#fruits').contents()[0]);
      expect($('.first')[1]).toBe($('#fruits').contents()[2]);
      expect($('.first')[2]).toBe($('#fruits').contents()[4]);
    });

    it('(fn) : should add returned Cheerio object as previous sibling', () => {
      const $fruits = $('#fruits').children();

      $fruits.before(() => $('<li class="second">'));

      expect($('.second')[0]).toBe($('#fruits').contents()[0]);
      expect($('.second')[1]).toBe($('#fruits').contents()[2]);
      expect($('.second')[2]).toBe($('#fruits').contents()[4]);
    });

    it('(fn) : should add returned Node as previous sibling', () => {
      const $fruits = $('#fruits').children();

      $fruits.before(() => $('<li class="third">')[0]);

      expect($('.third')[0]).toBe($('#fruits').contents()[0]);
      expect($('.third')[1]).toBe($('#fruits').contents()[2]);
      expect($('.third')[2]).toBe($('#fruits').contents()[4]);
    });

    it('(fn) : should support text nodes', () => {
      const $text = load(mixedText);

      $text($text('body')[0].children).before(
        (_, content) => `<c>${content}added</c>`,
      );

      expect($text('body').html()).toBe(
        '<c>1added</c><a>1</a>TEXT<c>2added</c><b>2</b>',
      );
    });

    it('($(...)) : should remove from root element', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const root = $plum[0].parent;
      expect(root?.type).toBe('root');

      $fruits.before($plum);
      expect($plum[0].parent?.type).not.toBe('root');
      expect(root?.childNodes).not.toContain($plum[0]);
    });
  });

  describe('.insertBefore', () => {
    it('(selector) : should create element and add as prev sibling', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertBefore('.apple');
      expect($('.apple').prev().hasClass('grape')).toBe(true);
    });

    it('(selector) : should create element and add as prev sibling of multiple elements', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertBefore('.apple, .pear');
      expect($('.apple').prev().hasClass('grape')).toBe(true);
      expect($('.pear').prev().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should create element and add as prev sibling', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertBefore($('.apple'));
      expect($('.apple').prev().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should create element and add as next sibling of multiple elements', () => {
      const grape = $('<li class="grape">Grape</li>');
      grape.insertBefore($('.apple, .pear'));
      expect($('.apple').prev().hasClass('grape')).toBe(true);
      expect($('.pear').prev().hasClass('grape')).toBe(true);
    });

    it('($(...)) : should create all elements in the array and add as prev siblings', () => {
      const more = $('<li class="plum">Plum</li><li class="grape">Grape</li>');
      more.insertBefore($('.apple'));
      expect($fruits.children().eq(0).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(1).hasClass('grape')).toBe(true);
      expect($fruits.children().eq(2).hasClass('apple')).toBe(true);
    });

    it('(existing Node) : should remove existing nodes from previous locations', () => {
      $('.pear').insertBefore('.apple');
      expect($fruits.children().eq(2).hasClass('pear')).toBe(false);
      expect($fruits.children().length).toBe(3);
      expect($('.pear').length).toBe(1);
    });

    it('(existing Node) : should update original direct siblings', () => {
      $('.pear').insertBefore('.apple');
      expect($('.apple').prev().hasClass('pear')).toBe(true);
      expect($('.apple').next().hasClass('orange')).toBe(true);
      expect($('.pear').next().hasClass('apple')).toBe(true);
      expect($('.pear').prev()).toHaveLength(0);
    });

    it('(existing Node) : should update original direct siblings of multiple elements', () => {
      $('.pear').insertBefore('.apple, .orange');
      expect($('.apple').prev().hasClass('pear')).toBe(true);
      expect($('.apple').next().hasClass('pear')).toBe(true);
      expect($('.orange').prev().hasClass('pear')).toBe(true);
      expect($('.orange').next()).toHaveLength(0);
      expect($fruits.children().length).toBe(4);
      const pears = $('.pear');
      expect(pears.length).toBe(2);
      expect(pears.eq(0).next().hasClass('apple')).toBe(true);
      expect(pears.eq(1).next().hasClass('orange')).toBe(true);
    });

    it('(elem) : should handle if removed', () => {
      const $apple = $('.apple');
      const $plum = $('<li class="plum">Plum</li>');

      $apple.remove();
      $plum.insertBefore($apple);
      expect($plum.next()).toHaveLength(0);
    });

    it('(single) should return the new element for chaining', () => {
      const $grape = $('<li class="grape">Grape</li>').insertBefore('.apple');
      expect($grape.cheerio).toBeTruthy();
      expect($grape.each).toBeTruthy();
      expect($grape.length).toBe(1);
      expect($grape.hasClass('grape')).toBe(true);
    });

    it('(single) should return the new elements for chaining', () => {
      const $purple = $(
        '<li class="grape">Grape</li><li class="plum">Plum</li>',
      ).insertBefore('.apple');
      expect($purple.cheerio).toBeTruthy();
      expect($purple.each).toBeTruthy();
      expect($purple.length).toBe(2);
      expect($purple.eq(0).hasClass('grape')).toBe(true);
      expect($purple.eq(1).hasClass('plum')).toBe(true);
    });

    it('(multiple) should return the new elements for chaining', () => {
      const $purple = $(
        '<li class="grape">Grape</li><li class="plum">Plum</li>',
      ).insertBefore('.apple, .pear');
      expect($purple.cheerio).toBeTruthy();
      expect($purple.each).toBeTruthy();
      expect($purple.length).toBe(4);
      expect($purple.eq(0).hasClass('grape')).toBe(true);
      expect($purple.eq(1).hasClass('plum')).toBe(true);
      expect($purple.eq(2).hasClass('grape')).toBe(true);
      expect($purple.eq(3).hasClass('plum')).toBe(true);
    });

    it('(single) should return the existing element for chaining', () => {
      const $orange = $('.orange').insertBefore('.apple');
      expect($orange.cheerio).toBeTruthy();
      expect($orange.each).toBeTruthy();
      expect($orange.length).toBe(1);
      expect($orange.hasClass('orange')).toBe(true);
    });

    it('(single) should return the existing elements for chaining', () => {
      const $things = $('.orange, .pear').insertBefore('.apple');
      expect($things.cheerio).toBeTruthy();
      expect($things.each).toBeTruthy();
      expect($things.length).toBe(2);
      expect($things.eq(0).hasClass('orange')).toBe(true);
      expect($things.eq(1).hasClass('pear')).toBe(true);
    });

    it('(multiple) should return the existing elements for chaining', () => {
      $('<li class="grape">Grape</li>').insertBefore('.apple');
      const $things = $('.orange, .apple').insertBefore('.pear, .grape');
      expect($things.cheerio).toBeTruthy();
      expect($things.each).toBeTruthy();
      expect($things.length).toBe(4);
      expect($things.eq(0).hasClass('apple')).toBe(true);
      expect($things.eq(1).hasClass('orange')).toBe(true);
      expect($things.eq(2).hasClass('apple')).toBe(true);
      expect($things.eq(3).hasClass('orange')).toBe(true);
    });
  });

  describe('.remove', () => {
    it('() : should remove selected elements', () => {
      $('.apple').remove();
      expect($fruits.find('.apple')).toHaveLength(0);
    });

    it('() : should be reentrant', () => {
      const $apple = $('.apple');
      $apple.remove();
      $apple.remove();
      expect($fruits.find('.apple')).toHaveLength(0);
    });

    it('(selector) : should remove matching selected elements', () => {
      $('li').remove('.apple');
      expect($fruits.find('.apple')).toHaveLength(0);
    });

    it('($(...)) : should remove from root element', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const root = $plum[0].parent;
      expect(root?.type).toBe('root');

      $plum.remove();
      expect($plum[0].parent).toBe(null);
      expect(root?.childNodes).not.toContain($plum[0]);
    });
  });

  describe('.replaceWith', () => {
    it('(elem) : should replace one <li> tag with another', () => {
      const $plum = $('<li class="plum">Plum</li>');
      $('.orange').replaceWith($plum);
      expect($('.apple').next().hasClass('plum')).toBe(true);
      expect($('.apple').next().html()).toBe('Plum');
      expect($('.pear').prev().hasClass('plum')).toBe(true);
      expect($('.pear').prev().html()).toBe('Plum');
    });

    it('(Array) : should replace one <li> tag with the elements in the array', () => {
      const more = $(
        '<li class="plum">Plum</li><li class="grape">Grape</li>',
      ).get();
      $('.orange').replaceWith(more);

      expect($fruits.children().eq(1).hasClass('plum')).toBe(true);
      expect($fruits.children().eq(2).hasClass('grape')).toBe(true);
      expect($('.apple').next().hasClass('plum')).toBe(true);
      expect($('.pear').prev().hasClass('grape')).toBe(true);
      expect($fruits.children()).toHaveLength(4);
    });

    it('(Node) : should replace the selected element with given node', () => {
      const $src = $('<h2>hi <span>there</span></h2>');
      const $new = $('<ul></ul>');
      const $replaced = $src.find('span').replaceWith($new[0]);
      expect($new[0].parentNode).toBe($src[0]);
      expect($replaced[0].parentNode).toBe(null);
      expect($.html($src)).toBe('<h2>hi <ul></ul></h2>');
    });

    it('(existing element) : should remove element from its previous location', () => {
      $('.pear').replaceWith($('.apple'));
      expect($fruits.children()).toHaveLength(2);
      expect($fruits.children()[0]).toBe($('.orange')[0]);
      expect($fruits.children()[1]).toBe($('.apple')[0]);
    });

    it('(elem) : should NOP if removed', () => {
      const $pear = $('.pear');
      const $plum = $('<li class="plum">Plum</li>');

      $pear.remove();
      $pear.replaceWith($plum);
      expect($('.orange').next().hasClass('plum')).toBe(false);
    });

    it('(elem) : should replace the single selected element with given element', () => {
      const $src = $('<h2>hi <span>there</span></h2>');
      const $new = $('<div>here</div>');
      const $replaced = $src.find('span').replaceWith($new);
      expect($new[0].parentNode).toBe($src[0]);
      expect($replaced[0].parentNode).toBe(null);
      expect($.html($src)).toBe('<h2>hi <div>here</div></h2>');
    });

    it('(self) : should be replaced after replacing it with itself', () => {
      const $a = load('<a>foo</a>', null, false);
      const replacement = '<a>bar</a>';
      $a('a').replaceWith((_, el: AnyNode) => el);
      $a('a').replaceWith(replacement);
      expect($a.html()).toBe(replacement);
    });

    it('(str) : should accept strings', () => {
      const $src = $('<h2>hi <span>there</span></h2>');
      const newStr = '<div>here</div>';
      const $replaced = $src.find('span').replaceWith(newStr);
      expect($replaced[0].parentNode).toBe(null);
      expect($.html($src)).toBe('<h2>hi <div>here</div></h2>');
    });

    it('(str) : should replace all selected elements', () => {
      const $src = $('<b>a<br>b<br>c<br>d</b>');
      const $replaced = $src.find('br').replaceWith(' ');
      expect($replaced[0].parentNode).toBe(null);
      expect($.html($src)).toBe('<b>a b c d</b>');
    });

    it('(fn) : should invoke the callback with the correct argument and context', () => {
      const origChildren = $fruits.children().get();
      const args: [number, AnyNode][] = [];
      const thisValues: AnyNode[] = [];

      $fruits.children().replaceWith(function (...myArgs) {
        args.push(myArgs);
        thisValues.push(this);
        return '<li class="first">';
      });

      expect(args).toStrictEqual([
        [0, origChildren[0]],
        [1, origChildren[1]],
        [2, origChildren[2]],
      ]);
      expect(thisValues).toStrictEqual([
        origChildren[0],
        origChildren[1],
        origChildren[2],
      ]);
    });

    it('(fn) : should replace the selected element with the returned string', () => {
      $fruits.children().replaceWith(() => '<li class="first">');

      expect($fruits.find('.first')).toHaveLength(3);
    });

    it('(fn) : should replace the selected element with the returned Cheerio object', () => {
      $fruits.children().replaceWith(() => $('<li class="second">'));

      expect($fruits.find('.second')).toHaveLength(3);
    });

    it('(fn) : should replace the selected element with the returned node', () => {
      $fruits.children().replaceWith(() => $('<li class="third">')[0]);

      expect($fruits.find('.third')).toHaveLength(3);
    });

    it('($(...)) : should remove from root element', () => {
      const $plum = $('<li class="plum">Plum</li>');
      const root = $plum[0].parent;
      expect(root?.type).toBe('root');

      $fruits.children().replaceWith($plum);
      expect($plum[0].parent?.type).not.toBe('root');
      expect(root?.childNodes).not.toContain($plum[0]);
    });
  });

  describe('.empty', () => {
    it('() : should remove all children from selected elements', () => {
      expect($fruits.children()).toHaveLength(3);

      $fruits.empty();
      expect($fruits.children()).toHaveLength(0);
    });

    it('() : should allow element reinsertion', () => {
      const $children = $fruits.children();

      $fruits.empty();
      expect($fruits.children()).toHaveLength(0);
      expect($children).toHaveLength(3);

      $fruits.append($('<div></div><div></div>'));
      const $remove = $fruits.children().eq(0);

      $remove.replaceWith($children);
      expect($fruits.children()).toHaveLength(4);
    });

    it("() : should destroy children's references to the parent", () => {
      const $children = $fruits.children();

      $fruits.empty();

      expect($children.eq(0).parent()).toHaveLength(0);
      expect($children.eq(0).next()).toHaveLength(0);
      expect($children.eq(0).prev()).toHaveLength(0);
      expect($children.eq(1).parent()).toHaveLength(0);
      expect($children.eq(1).next()).toHaveLength(0);
      expect($children.eq(1).prev()).toHaveLength(0);
      expect($children.eq(2).parent()).toHaveLength(0);
      expect($children.eq(2).next()).toHaveLength(0);
      expect($children.eq(2).prev()).toHaveLength(0);
    });

    it('() : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.empty();

      expect($text('body').html()).toBe('<a></a>TEXT<b></b>');
    });

    it('() : should skip comment nodes', () => {
      const $comment = load('<a>1</a><!--Comment-->TEXT<b>2</b>');
      const $body = $comment($comment('body')[0].children);

      $body.empty();

      expect($comment('body').html()).toBe('<a></a><!--Comment-->TEXT<b></b>');
    });
  });

  describe('.html', () => {
    it('() : should get the innerHTML for an element', () => {
      expect($fruits.html()).toBe(
        [
          '<li class="apple">Apple</li>',
          '<li class="orange">Orange</li>',
          '<li class="pear">Pear</li>',
        ].join(''),
      );
    });

    it('() : should get innerHTML even if its just text', () => {
      expect($('.pear', '<li class="pear">Pear</li>').html()).toBe('Pear');
    });

    it('() : should return empty string if nothing inside', () => {
      expect($('li', '<li></li>').html()).toBe('');
    });

    it('(html) : should set the html for its children', () => {
      $fruits.html('<li class="durian">Durian</li>');
      const html = $fruits.html();
      expect(html).toBe('<li class="durian">Durian</li>');
    });

    it('(html) : should add new elements for each element in selection', () => {
      const $fruits = $('li');
      $fruits.html('<li class="durian">Durian</li>');
      let tested = 0;
      $fruits.each(function () {
        expect($(this).children().parent().get(0)).toBe(this);
        tested++;
      });
      expect(tested).toBe(3);
    });

    it('(html) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.html('test');

      expect($text('body').html()).toBe('<a>test</a>TEXT<b>test</b>');
    });

    it('(elem) : should set the html for its children with element', () => {
      $fruits.html($('<li class="durian">Durian</li>'));
      const html = $fruits.html();
      expect(html).toBe('<li class="durian">Durian</li>');
    });

    it('(elem) : should move the passed element (#940)', () => {
      $('.apple').html($('.orange'));
      expect($fruits.html()).toBe(
        '<li class="apple"><li class="orange">Orange</li></li><li class="pear">Pear</li>',
      );
    });

    it('() : should allow element reinsertion', () => {
      const $children = $fruits.children();

      $fruits.html('<div></div><div></div>');
      expect($fruits.children()).toHaveLength(2);

      const $remove = $fruits.children().eq(0);

      $remove.replaceWith($children);
      expect($fruits.children()).toHaveLength(4);
    });

    it('(script value) : should add content as text', () => {
      const $data = '<a><b>';
      const $script = $('<script>').html($data) as Cheerio<Element>;

      expect($script).toHaveLength(1);
      expect($script[0].type).toBe('script');
      expect($script[0]).toHaveProperty('name', 'script');

      expect($script[0].children).toHaveLength(1);
      expect($script[0].children[0].type).toBe('text');
      expect($script[0].children[0]).toHaveProperty('data', $data);
    });
  });

  describe('.toString', () => {
    it('() : should get the outerHTML for an element', () => {
      expect($fruits.toString()).toBe(fruits);
    });

    it('() : should return an html string for a set of elements', () => {
      expect($fruits.find('li').toString()).toBe(
        '<li class="apple">Apple</li><li class="orange">Orange</li><li class="pear">Pear</li>',
      );
    });

    it('() : should be called implicitly', () => {
      const string = [$('<foo>'), $('<bar>'), $('<baz>')].join('');
      expect(string).toBe('<foo></foo><bar></bar><baz></baz>');
    });

    it('() : should pass options', () => {
      const dom = load('&', { xml: { decodeEntities: false } });
      expect(dom.root().toString()).toBe('&');
    });
  });

  describe('.text', () => {
    it('() : gets the text for a single element', () => {
      expect($('.apple').text()).toBe('Apple');
    });

    it('() : combines all text from children text nodes', () => {
      expect($('#fruits').text()).toBe('AppleOrangePear');
    });

    it('(text) : sets the text for the child node', () => {
      $('.apple').text('Granny Smith Apple');
      expect($('.apple')[0].childNodes[0]).toHaveProperty(
        'data',
        'Granny Smith Apple',
      );
    });

    it('(text) : inserts separate nodes for all children', () => {
      $('li').text('Fruits');
      let tested = 0;
      $('li').each(function () {
        expect(this.childNodes[0].parentNode).toBe(this);
        tested++;
      });
      expect(tested).toBe(3);
    });

    it('(text) : should create a Node with the DOM level 1 API', () => {
      const $apple = $('.apple');

      $apple.text('anything');
      const textNode = $apple[0].childNodes[0];

      expect(textNode.parentNode).toBe($apple[0]);
      expect(textNode.nodeType).toBe(3);
      expect(textNode).toHaveProperty('data', 'anything');
    });

    it('(html) : should skip text nodes', () => {
      const $text = load(mixedText);
      const $body = $text($text('body')[0].children);

      $body.text('test');

      expect($text('body').html()).toBe('<a>test</a>TEXT<b>test</b>');
    });

    it('should allow functions as arguments', () => {
      $('.apple').text((idx, content) => {
        expect(idx).toBe(0);
        expect(content).toBe('Apple');
        return 'whatever mate';
      });
      expect($('.apple')[0].childNodes[0]).toHaveProperty(
        'data',
        'whatever mate',
      );
    });

    it('should allow functions as arguments for multiple elements', () => {
      $('li').text((idx) => `text${idx}`);
      $('li').each(function (this, idx) {
        expect(this.childNodes[0]).toHaveProperty('data', `text${idx}`);
      });
    });

    it('should decode special chars', () => {
      const text = $('<p>M&amp;M</p>').text();
      expect(text).toBe('M&M');
    });

    it('should work with special chars added as strings', () => {
      const text = $('<p>M&M</p>').text();
      expect(text).toBe('M&M');
    });

    it('should turn passed values to strings', () => {
      $('.apple').text(1 as never);
      expect($('.apple')[0].childNodes[0]).toHaveProperty('data', '1');
    });

    it('( undefined ) : should act as an accessor', () => {
      const $div = $('<div>test</div>');
      expect(typeof $div.text(undefined as never)).toBe('string');
      expect($div.text()).toBe('test');
    });

    it('( "" ) : should convert to string', () => {
      const $div = $('<div>test</div>');
      expect($div.text('').text()).toBe('');
    });

    it('( null ) : should convert to string', () => {
      expect(
        $('<div>')
          .text(null as never)
          .text(),
      ).toBe('null');
    });

    it('( 0 ) : should convert to string', () => {
      expect(
        $('<div>')
          .text(0 as never)
          .text(),
      ).toBe('0');
    });

    it('(str) should encode then decode unsafe characters', () => {
      const $apple = $('.apple');

      $apple.text('blah <script>alert("XSS!")</script> blah');
      expect($apple[0].childNodes[0]).toHaveProperty(
        'data',
        'blah <script>alert("XSS!")</script> blah',
      );
      expect($apple.text()).toBe('blah <script>alert("XSS!")</script> blah');

      $apple.text('blah <script>alert("XSS!")</script> blah');
      expect($apple.html()).not.toContain('<script>alert("XSS!")</script>');
    });
  });

  describe('.clone', () => {
    it('() : should return a copy', () => {
      const $src = $(
        '<div><span>foo</span><span>bar</span><span>baz</span></div>',
      ).children();
      const $elem = $src.clone();
      expect($elem.length).toBe(3);
      expect($elem.parent()).toHaveLength(0);
      expect($elem.text()).toBe($src.text());
      $src.text('rofl');
      expect($elem.text()).not.toBe($src.text());
    });

    it('() : should return a copy of document', () => {
      const $src = load('<html><body><div>foo</div>bar</body></html>')
        .root()
        .children();
      const $elem = $src.clone();
      expect($elem.length).toBe(1);
      expect($elem.parent()).toHaveLength(0);
      expect($elem.text()).toBe($src.text());
      $src.text('rofl');
      expect($elem.text()).not.toBe($src.text());
    });

    it('() : should preserve parsing options', () => {
      const $ = load('<div>π</div>', { xml: { decodeEntities: false } });
      const $div = $('div');

      expect($div.text()).toBe($div.clone().text());
    });
  });
});
```

## File: `src/api/manipulation.ts`
```typescript
/**
 * Methods for modifying the DOM structure.
 *
 * @module cheerio/manipulation
 */

import {
  type AnyNode,
  cloneNode,
  Document,
  type Element,
  hasChildren,
  isTag,
  type ParentNode,
  Text,
} from 'domhandler';
import { removeElement } from 'domutils';
import { ElementType } from 'htmlparser2';
import type { Cheerio } from '../cheerio.js';
import { update as updateDOM } from '../parse.js';
import { text as staticText } from '../static.js';
import type { AcceptedElems, BasicAcceptedElems } from '../types.js';
import { domEach, isCheerio, isHtml } from '../utils.js';

/**
 * Create an array of nodes, recursing into arrays and parsing strings if
 * necessary.
 *
 * @private
 * @category Manipulation
 * @param elem - Elements to make an array of.
 * @param clone - Optionally clone nodes.
 * @returns The array of nodes.
 */
export function _makeDomArray<T extends AnyNode>(
  this: Cheerio<T>,
  elem?: BasicAcceptedElems<AnyNode> | BasicAcceptedElems<AnyNode>[],
  clone?: boolean,
): AnyNode[] {
  if (elem == null) {
    return [];
  }

  if (typeof elem === 'string') {
    return [...this._parse(elem, this.options, false, null).children];
  }

  if ('length' in elem) {
    if (elem.length === 1) {
      return this._makeDomArray(elem[0], clone);
    }

    const result: AnyNode[] = [];

    for (let i = 0; i < elem.length; i++) {
      const el = elem[i];

      if (typeof el === 'object') {
        if (el == null) {
          continue;
        }

        if (!('length' in el)) {
          result.push(clone ? cloneNode(el, true) : el);
          continue;
        }
      }

      result.push(...this._makeDomArray(el, clone));
    }

    return result;
  }

  return [clone ? cloneNode(elem, true) : elem];
}

function _insert(
  concatenator: (
    dom: AnyNode[],
    children: AnyNode[],
    parent: ParentNode,
  ) => void,
) {
  return function <T extends AnyNode>(
    this: Cheerio<T>,
    ...elems:
      | [
          (
            this: AnyNode,
            i: number,
            html: string,
          ) => BasicAcceptedElems<AnyNode>,
        ]
      | BasicAcceptedElems<AnyNode>[]
  ) {
    const lastIdx = this.length - 1;

    return domEach(this, (el, i) => {
      if (!hasChildren(el)) return;

      const domSrc =
        typeof elems[0] === 'function'
          ? elems[0].call(el, i, this._render(el.children))
          : (elems as BasicAcceptedElems<AnyNode>[]);

      const dom = this._makeDomArray(domSrc, i < lastIdx);
      concatenator(dom, el.children, el);
    });
  };
}

/**
 * Modify an array in-place, removing some number of elements and adding new
 * elements directly following them.
 *
 * @private
 * @category Manipulation
 * @param array - Target array to splice.
 * @param spliceIdx - Index at which to begin changing the array.
 * @param spliceCount - Number of elements to remove from the array.
 * @param newElems - Elements to insert into the array.
 * @param parent - The parent of the node.
 * @returns The spliced array.
 */
function uniqueSplice(
  array: AnyNode[],
  spliceIdx: number,
  spliceCount: number,
  newElems: AnyNode[],
  parent: ParentNode,
): AnyNode[] {
  const spliceArgs: Parameters<AnyNode[]['splice']> = [
    spliceIdx,
    spliceCount,
    ...newElems,
  ];
  const prev = spliceIdx === 0 ? null : array[spliceIdx - 1];
  const next =
    spliceIdx + spliceCount >= array.length
      ? null
      : array[spliceIdx + spliceCount];

  /*
   * Before splicing in new elements, ensure they do not already appear in the
   * current array.
   */
  for (let idx = 0; idx < newElems.length; ++idx) {
    const node = newElems[idx];
    const oldParent = node.parent;

    if (oldParent) {
      const oldSiblings: AnyNode[] = oldParent.children;
      const prevIdx = oldSiblings.indexOf(node);

      if (prevIdx !== -1) {
        oldParent.children.splice(prevIdx, 1);
        if (parent === oldParent && spliceIdx > prevIdx) {
          spliceArgs[0]--;
        }
      }
    }

    node.parent = parent;

    if (node.prev) {
      node.prev.next = node.next ?? null;
    }

    if (node.next) {
      node.next.prev = node.prev ?? null;
    }

    node.prev = idx === 0 ? prev : newElems[idx - 1];
    node.next = idx === newElems.length - 1 ? next : newElems[idx + 1];
  }

  if (prev) {
    prev.next = newElems[0];
  }
  if (next) {
    next.prev = newElems[newElems.length - 1];
  }
  return array.splice(...spliceArgs);
}

/**
 * Insert every element in the set of matched elements to the end of the target.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('<li class="plum">Plum</li>').appendTo('#fruits');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //      <li class="plum">Plum</li>
 * //    </ul>
 * ```
 *
 * @param target - Element to append elements to.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/appendTo/}
 */
export function appendTo<T extends AnyNode>(
  this: Cheerio<T>,
  target: BasicAcceptedElems<AnyNode>,
): Cheerio<T> {
  const appendTarget = isCheerio<T>(target) ? target : this._make(target);

  appendTarget.append(this);

  return this;
}

/**
 * Insert every element in the set of matched elements to the beginning of the
 * target.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('<li class="plum">Plum</li>').prependTo('#fruits');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="plum">Plum</li>
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //    </ul>
 * ```
 *
 * @param target - Element to prepend elements to.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/prependTo/}
 */
export function prependTo<T extends AnyNode>(
  this: Cheerio<T>,
  target: BasicAcceptedElems<AnyNode>,
): Cheerio<T> {
  const prependTarget = isCheerio<T>(target) ? target : this._make(target);

  prependTarget.prepend(this);

  return this;
}

/**
 * Inserts content as the _last_ child of each of the selected elements.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('ul').append('<li class="plum">Plum</li>');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //      <li class="plum">Plum</li>
 * //    </ul>
 * ```
 *
 * @see {@link https://api.jquery.com/append/}
 */
export const append: <T extends AnyNode>(
  this: Cheerio<T>,
  ...elems:
    | [(this: AnyNode, i: number, html: string) => BasicAcceptedElems<AnyNode>]
    | BasicAcceptedElems<AnyNode>[]
) => Cheerio<T> = _insert((dom, children, parent) => {
  uniqueSplice(children, children.length, 0, dom, parent);
});

/**
 * Inserts content as the _first_ child of each of the selected elements.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('ul').prepend('<li class="plum">Plum</li>');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="plum">Plum</li>
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //    </ul>
 * ```
 *
 * @see {@link https://api.jquery.com/prepend/}
 */
export const prepend: <T extends AnyNode>(
  this: Cheerio<T>,
  ...elems:
    | [(this: AnyNode, i: number, html: string) => BasicAcceptedElems<AnyNode>]
    | BasicAcceptedElems<AnyNode>[]
) => Cheerio<T> = _insert((dom, children, parent) => {
  uniqueSplice(children, 0, 0, dom, parent);
});

function _wrap(
  insert: (
    el: AnyNode,
    elInsertLocation: ParentNode,
    wrapperDom: ParentNode[],
  ) => void,
) {
  return function <T extends AnyNode>(
    this: Cheerio<T>,
    wrapper: AcceptedElems<AnyNode>,
  ) {
    const lastIdx = this.length - 1;
    const lastParent = this.parents().last();

    for (let i = 0; i < this.length; i++) {
      const el = this[i];

      const wrap =
        typeof wrapper === 'function'
          ? wrapper.call(el, i, el)
          : typeof wrapper === 'string' && !isHtml(wrapper)
            ? lastParent.find(wrapper).clone()
            : wrapper;

      const [wrapperDom] = this._makeDomArray(wrap, i < lastIdx);

      if (!(wrapperDom && hasChildren(wrapperDom))) continue;

      let elInsertLocation = wrapperDom;

      /*
       * Find the deepest child. Only consider the first tag child of each node
       * (ignore text); stop if no children are found.
       */
      let j = 0;

      while (j < elInsertLocation.children.length) {
        const child = elInsertLocation.children[j];
        if (isTag(child)) {
          elInsertLocation = child;
          j = 0;
        } else {
          j++;
        }
      }

      insert(el, elInsertLocation, [wrapperDom]);
    }

    return this;
  };
}

/**
 * The .wrap() function can take any string or object that could be passed to
 * the $() factory function to specify a DOM structure. This structure may be
 * nested several levels deep, but should contain only one inmost element. A
 * copy of this structure will be wrapped around each of the elements in the set
 * of matched elements. This method returns the original set of elements for
 * chaining purposes.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * const redFruit = $('<div class="red-fruit"></div>');
 * $('.apple').wrap(redFruit);
 *
 * //=> <ul id="fruits">
 * //     <div class="red-fruit">
 * //      <li class="apple">Apple</li>
 * //     </div>
 * //     <li class="orange">Orange</li>
 * //     <li class="plum">Plum</li>
 * //   </ul>
 *
 * const healthy = $('<div class="healthy"></div>');
 * $('li').wrap(healthy);
 *
 * //=> <ul id="fruits">
 * //     <div class="healthy">
 * //       <li class="apple">Apple</li>
 * //     </div>
 * //     <div class="healthy">
 * //       <li class="orange">Orange</li>
 * //     </div>
 * //     <div class="healthy">
 * //        <li class="plum">Plum</li>
 * //     </div>
 * //   </ul>
 * ```
 *
 * @param wrapper - The DOM structure to wrap around each element in the
 *   selection.
 * @see {@link https://api.jquery.com/wrap/}
 */
export const wrap: <T extends AnyNode>(
  this: Cheerio<T>,
  wrapper: AcceptedElems<AnyNode>,
) => Cheerio<T> = _wrap((el, elInsertLocation, wrapperDom) => {
  const { parent } = el;

  if (!parent) return;

  const siblings: AnyNode[] = parent.children;
  const index = siblings.indexOf(el);

  updateDOM([el], elInsertLocation);
  /*
   * The previous operation removed the current element from the `siblings`
   * array, so the `dom` array can be inserted without removing any
   * additional elements.
   */
  uniqueSplice(siblings, index, 0, wrapperDom, parent);
});

/**
 * The .wrapInner() function can take any string or object that could be passed
 * to the $() factory function to specify a DOM structure. This structure may be
 * nested several levels deep, but should contain only one inmost element. The
 * structure will be wrapped around the content of each of the elements in the
 * set of matched elements.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * const redFruit = $('<div class="red-fruit"></div>');
 * $('.apple').wrapInner(redFruit);
 *
 * //=> <ul id="fruits">
 * //     <li class="apple">
 * //       <div class="red-fruit">Apple</div>
 * //     </li>
 * //     <li class="orange">Orange</li>
 * //     <li class="pear">Pear</li>
 * //   </ul>
 *
 * const healthy = $('<div class="healthy"></div>');
 * $('li').wrapInner(healthy);
 *
 * //=> <ul id="fruits">
 * //     <li class="apple">
 * //       <div class="healthy">Apple</div>
 * //     </li>
 * //     <li class="orange">
 * //       <div class="healthy">Orange</div>
 * //     </li>
 * //     <li class="pear">
 * //       <div class="healthy">Pear</div>
 * //     </li>
 * //   </ul>
 * ```
 *
 * @param wrapper - The DOM structure to wrap around the content of each element
 *   in the selection.
 * @returns The instance itself, for chaining.
 * @see {@link https://api.jquery.com/wrapInner/}
 */
export const wrapInner: <T extends AnyNode>(
  this: Cheerio<T>,
  wrapper: AcceptedElems<AnyNode>,
) => Cheerio<T> = _wrap((el, elInsertLocation, wrapperDom) => {
  if (!hasChildren(el)) return;
  updateDOM(el.children, elInsertLocation);
  updateDOM(wrapperDom, el);
});

/**
 * The .unwrap() function, removes the parents of the set of matched elements
 * from the DOM, leaving the matched elements in their place.
 *
 * @category Manipulation
 * @example <caption>without selector</caption>
 *
 * ```js
 * const $ = cheerio.load(
 *   '<div id=test>\n  <div><p>Hello</p></div>\n  <div><p>World</p></div>\n</div>',
 * );
 * $('#test p').unwrap();
 *
 * //=> <div id=test>
 * //     <p>Hello</p>
 * //     <p>World</p>
 * //   </div>
 * ```
 *
 * @example <caption>with selector</caption>
 *
 * ```js
 * const $ = cheerio.load(
 *   '<div id=test>\n  <p>Hello</p>\n  <b><p>World</p></b>\n</div>',
 * );
 * $('#test p').unwrap('b');
 *
 * //=> <div id=test>
 * //     <p>Hello</p>
 * //     <p>World</p>
 * //   </div>
 * ```
 *
 * @param selector - A selector to check the parent element against. If an
 *   element's parent does not match the selector, the element won't be
 *   unwrapped.
 * @returns The instance itself, for chaining.
 * @see {@link https://api.jquery.com/unwrap/}
 */
export function unwrap<T extends AnyNode>(
  this: Cheerio<T>,
  selector?: string,
): Cheerio<T> {
  this.parent(selector)
    .not('body')
    .each((_, el) => {
      this._make(el).replaceWith(el.children);
    });
  return this;
}

/**
 * The .wrapAll() function can take any string or object that could be passed to
 * the $() function to specify a DOM structure. This structure may be nested
 * several levels deep, but should contain only one inmost element. The
 * structure will be wrapped around all of the elements in the set of matched
 * elements, as a single group.
 *
 * @category Manipulation
 * @example <caption>With markup passed to `wrapAll`</caption>
 *
 * ```js
 * const $ = cheerio.load(
 *   '<div class="container"><div class="inner">First</div><div class="inner">Second</div></div>',
 * );
 * $('.inner').wrapAll("<div class='new'></div>");
 *
 * //=> <div class="container">
 * //     <div class='new'>
 * //       <div class="inner">First</div>
 * //       <div class="inner">Second</div>
 * //     </div>
 * //   </div>
 * ```
 *
 * @example <caption>With an existing cheerio instance</caption>
 *
 * ```js
 * const $ = cheerio.load(
 *   '<span>Span 1</span><strong>Strong</strong><span>Span 2</span>',
 * );
 * const wrap = $('<div><p><em><b></b></em></p></div>');
 * $('span').wrapAll(wrap);
 *
 * //=> <div>
 * //     <p>
 * //       <em>
 * //         <b>
 * //           <span>Span 1</span>
 * //           <span>Span 2</span>
 * //         </b>
 * //       </em>
 * //     </p>
 * //   </div>
 * //   <strong>Strong</strong>
 * ```
 *
 * @param wrapper - The DOM structure to wrap around all matched elements in the
 *   selection.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/wrapAll/}
 */
export function wrapAll<T extends AnyNode>(
  this: Cheerio<T>,
  wrapper: AcceptedElems<T>,
): Cheerio<T> {
  const el = this[0];
  if (el) {
    const wrap: Cheerio<AnyNode> = this._make(
      typeof wrapper === 'function' ? wrapper.call(el, 0, el) : wrapper,
    ).insertBefore(el);

    // If html is given as wrapper, wrap may contain text elements
    let elInsertLocation: Element | undefined;

    for (let i = 0; i < wrap.length; i++) {
      if (wrap[i].type === ElementType.Tag) {
        elInsertLocation = wrap[i] as Element;
      }
    }

    let j = 0;

    /*
     * Find the deepest child. Only consider the first tag child of each node
     * (ignore text); stop if no children are found.
     */
    while (elInsertLocation && j < elInsertLocation.children.length) {
      const child = elInsertLocation.children[j];
      if (child.type === ElementType.Tag) {
        elInsertLocation = child;
        j = 0;
      } else {
        j++;
      }
    }

    if (elInsertLocation) this._make(elInsertLocation).append(this);
  }
  return this;
}

/**
 * Insert content next to each element in the set of matched elements.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.apple').after('<li class="plum">Plum</li>');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="apple">Apple</li>
 * //      <li class="plum">Plum</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //    </ul>
 * ```
 *
 * @param elems - HTML string, DOM element, array of DOM elements or Cheerio to
 *   insert after each element in the set of matched elements.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/after/}
 */
export function after<T extends AnyNode>(
  this: Cheerio<T>,
  ...elems:
    | [(this: AnyNode, i: number, html: string) => BasicAcceptedElems<AnyNode>]
    | BasicAcceptedElems<AnyNode>[]
): Cheerio<T> {
  const lastIdx = this.length - 1;

  return domEach(this, (el, i) => {
    if (!(hasChildren(el) && el.parent)) {
      return;
    }

    const siblings: AnyNode[] = el.parent.children;
    const index = siblings.indexOf(el);

    // If not found, move on
    /* istanbul ignore next */
    if (index === -1) return;

    const domSrc =
      typeof elems[0] === 'function'
        ? elems[0].call(el, i, this._render(el.children))
        : (elems as BasicAcceptedElems<AnyNode>[]);

    const dom = this._makeDomArray(domSrc, i < lastIdx);

    // Add element after `this` element
    uniqueSplice(siblings, index + 1, 0, dom, el.parent);
  });
}

/**
 * Insert every element in the set of matched elements after the target.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('<li class="plum">Plum</li>').insertAfter('.apple');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="apple">Apple</li>
 * //      <li class="plum">Plum</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //    </ul>
 * ```
 *
 * @param target - Element to insert elements after.
 * @returns The set of newly inserted elements.
 * @see {@link https://api.jquery.com/insertAfter/}
 */
export function insertAfter<T extends AnyNode>(
  this: Cheerio<T>,
  target: BasicAcceptedElems<AnyNode>,
): Cheerio<T> {
  if (typeof target === 'string') {
    target = this._make<AnyNode>(target);
  }

  this.remove();

  const clones: T[] = [];

  for (const el of this._makeDomArray(target)) {
    const clonedSelf = this.clone().toArray();
    const { parent } = el;
    if (!parent) {
      continue;
    }

    const siblings: AnyNode[] = parent.children;
    const index = siblings.indexOf(el);

    // If not found, move on
    /* istanbul ignore next */
    if (index === -1) continue;

    // Add cloned `this` element(s) after target element
    uniqueSplice(siblings, index + 1, 0, clonedSelf, parent);
    clones.push(...clonedSelf);
  }

  return this._make(clones);
}

/**
 * Insert content previous to each element in the set of matched elements.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.apple').before('<li class="plum">Plum</li>');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="plum">Plum</li>
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //    </ul>
 * ```
 *
 * @param elems - HTML string, DOM element, array of DOM elements or Cheerio to
 *   insert before each element in the set of matched elements.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/before/}
 */
export function before<T extends AnyNode>(
  this: Cheerio<T>,
  ...elems:
    | [(this: AnyNode, i: number, html: string) => BasicAcceptedElems<AnyNode>]
    | BasicAcceptedElems<AnyNode>[]
): Cheerio<T> {
  const lastIdx = this.length - 1;

  return domEach(this, (el, i) => {
    if (!(hasChildren(el) && el.parent)) {
      return;
    }

    const siblings: AnyNode[] = el.parent.children;
    const index = siblings.indexOf(el);

    // If not found, move on
    /* istanbul ignore next */
    if (index === -1) return;

    const domSrc =
      typeof elems[0] === 'function'
        ? elems[0].call(el, i, this._render(el.children))
        : (elems as BasicAcceptedElems<AnyNode>[]);

    const dom = this._makeDomArray(domSrc, i < lastIdx);

    // Add element before `el` element
    uniqueSplice(siblings, index, 0, dom, el.parent);
  });
}

/**
 * Insert every element in the set of matched elements before the target.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('<li class="plum">Plum</li>').insertBefore('.apple');
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="plum">Plum</li>
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //      <li class="pear">Pear</li>
 * //    </ul>
 * ```
 *
 * @param target - Element to insert elements before.
 * @returns The set of newly inserted elements.
 * @see {@link https://api.jquery.com/insertBefore/}
 */
export function insertBefore<T extends AnyNode>(
  this: Cheerio<T>,
  target: BasicAcceptedElems<AnyNode>,
): Cheerio<T> {
  const targetArr = this._make<AnyNode>(target);

  this.remove();

  const clones: T[] = [];

  domEach(targetArr, (el) => {
    const clonedSelf = this.clone().toArray();
    const { parent } = el;
    if (!parent) {
      return;
    }

    const siblings: AnyNode[] = parent.children;
    const index = siblings.indexOf(el);

    // If not found, move on
    /* istanbul ignore next */
    if (index === -1) return;

    // Add cloned `this` element(s) after target element
    uniqueSplice(siblings, index, 0, clonedSelf, parent);
    clones.push(...clonedSelf);
  });

  return this._make(clones);
}

/**
 * Removes the set of matched elements from the DOM and all their children.
 * `selector` filters the set of matched elements to be removed.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.pear').remove();
 * $.html();
 * //=>  <ul id="fruits">
 * //      <li class="apple">Apple</li>
 * //      <li class="orange">Orange</li>
 * //    </ul>
 * ```
 *
 * @param selector - Optional selector for elements to remove.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/remove/}
 */
export function remove<T extends AnyNode>(
  this: Cheerio<T>,
  selector?: string,
): Cheerio<T> {
  // Filter if we have selector
  const elems = selector ? this.filter(selector) : this;

  domEach(elems, (el) => {
    removeElement(el);
    el.prev = el.next = el.parent = null;
  });

  return this;
}

/**
 * Replaces matched elements with `content`.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * const plum = $('<li class="plum">Plum</li>');
 * $('.pear').replaceWith(plum);
 * $.html();
 * //=> <ul id="fruits">
 * //     <li class="apple">Apple</li>
 * //     <li class="orange">Orange</li>
 * //     <li class="plum">Plum</li>
 * //   </ul>
 * ```
 *
 * @param content - Replacement for matched elements.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/replaceWith/}
 */
export function replaceWith<T extends AnyNode>(
  this: Cheerio<T>,
  content: AcceptedElems<AnyNode>,
): Cheerio<T> {
  return domEach(this, (el, i) => {
    const { parent } = el;
    if (!parent) {
      return;
    }

    const siblings: AnyNode[] = parent.children;
    const cont =
      typeof content === 'function' ? content.call(el, i, el) : content;
    const dom = this._makeDomArray(cont);

    /*
     * In the case that `dom` contains nodes that already exist in other
     * structures, ensure those nodes are properly removed.
     */
    updateDOM(dom, null);

    const index = siblings.indexOf(el);

    // Completely remove old element
    uniqueSplice(siblings, index, 1, dom, parent);

    if (!dom.includes(el)) {
      el.parent = el.prev = el.next = null;
    }
  });
}

/**
 * Removes all children from each item in the selection. Text nodes and comment
 * nodes are left as is.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('ul').empty();
 * $.html();
 * //=>  <ul id="fruits"></ul>
 * ```
 *
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/empty/}
 */
export function empty<T extends AnyNode>(this: Cheerio<T>): Cheerio<T> {
  return domEach(this, (el) => {
    if (!hasChildren(el)) return;
    for (const child of el.children) {
      child.next = child.prev = child.parent = null;
    }

    el.children.length = 0;
  });
}

/**
 * Gets an HTML content string from the first selected element.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.orange').html();
 * //=> Orange
 *
 * $('#fruits').html('<li class="mango">Mango</li>').html();
 * //=> <li class="mango">Mango</li>
 * ```
 *
 * @returns The HTML content string.
 * @see {@link https://api.jquery.com/html/}
 */
export function html<T extends AnyNode>(this: Cheerio<T>): string | null;
/**
 * Replaces each selected element's content with the specified content.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.orange').html('<li class="mango">Mango</li>').html();
 * //=> <li class="mango">Mango</li>
 * ```
 *
 * @param str - The content to replace selection's contents with.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/html/}
 */
export function html<T extends AnyNode>(
  this: Cheerio<T>,
  str: string | Cheerio<T>,
): Cheerio<T>;
export function html<T extends AnyNode>(
  this: Cheerio<T>,
  str?: string | Cheerio<AnyNode>,
): Cheerio<T> | string | null {
  if (str === undefined) {
    const el = this[0];
    if (!(el && hasChildren(el))) return null;
    return this._render(el.children);
  }

  return domEach(this, (el) => {
    if (!hasChildren(el)) return;
    for (const child of el.children) {
      child.next = child.prev = child.parent = null;
    }

    const content = isCheerio(str)
      ? str.toArray()
      : this._parse(`${str}`, this.options, false, el).children;

    updateDOM(content, el);
  });
}

/**
 * Turns the collection to a string. Alias for `.html()`.
 *
 * @category Manipulation
 * @returns The rendered document.
 */
export function toString<T extends AnyNode>(this: Cheerio<T>): string {
  return this._render(this);
}

/**
 * Get the combined text contents of each element in the set of matched
 * elements, including their descendants.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.orange').text();
 * //=> Orange
 *
 * $('ul').text();
 * //=>  Apple
 * //    Orange
 * //    Pear
 * ```
 *
 * @returns The text contents of the collection.
 * @see {@link https://api.jquery.com/text/}
 */
export function text<T extends AnyNode>(this: Cheerio<T>): string;
/**
 * Set the content of each element in the set of matched elements to the
 * specified text.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * $('.orange').text('Orange');
 * //=> <div class="orange">Orange</div>
 * ```
 *
 * @param str - The text to set as the content of each matched element.
 * @returns The instance itself.
 * @see {@link https://api.jquery.com/text/}
 */
export function text<T extends AnyNode>(
  this: Cheerio<T>,
  str: string | ((this: AnyNode, i: number, text: string) => string),
): Cheerio<T>;
export function text<T extends AnyNode>(
  this: Cheerio<T>,
  str?: string | ((this: AnyNode, i: number, text: string) => string),
): Cheerio<T> | string {
  // If `str` is undefined, act as a "getter"
  if (str === undefined) {
    return staticText(this);
  }
  if (typeof str === 'function') {
    // Function support
    return domEach(this, (el, i) =>
      this._make(el).text(str.call(el, i, staticText([el]))),
    );
  }

  // Append text node to each selected elements
  return domEach(this, (el) => {
    if (!hasChildren(el)) return;
    for (const child of el.children) {
      child.next = child.prev = child.parent = null;
    }

    const textNode = new Text(`${str}`);

    updateDOM(textNode, el);
  });
}

/**
 * Clone the cheerio object.
 *
 * @category Manipulation
 * @example
 *
 * ```js
 * const moreFruit = $('#fruits').clone();
 * ```
 *
 * @returns The cloned object.
 * @see {@link https://api.jquery.com/clone/}
 */
export function clone<T extends AnyNode>(this: Cheerio<T>): Cheerio<T> {
  const clone = Array.prototype.map.call(
    this.get(),
    (el) => cloneNode(el, true) as T,
  ) as T[];

  // Add a root node around the cloned nodes
  const root = new Document(clone);
  for (const node of clone) {
    node.parent = root;
  }

  return this._make(clone);
}
```

## File: `src/api/traversing.spec.ts`
```typescript
import { type AnyNode, type Element, isText, type Text } from 'domhandler';
import { beforeEach, describe, expect, it } from 'vitest';
import {
  cheerio,
  drinks,
  eleven,
  food,
  forms,
  fruits,
  mixedText,
  text,
  vegetables,
} from '../__fixtures__/fixtures.js';
import { Cheerio } from '../cheerio.js';
import { type CheerioAPI, load } from '../index.js';

function getText(el: Cheerio<Element>) {
  if (el.length === 0) return;
  const [firstChild] = el[0].childNodes;
  return isText(firstChild) ? firstChild.data : undefined;
}

describe('$(...)', () => {
  let $: CheerioAPI;

  beforeEach(() => {
    $ = load(fruits);
  });

  describe('.load', () => {
    it('should throw a TypeError if given invalid input', () => {
      expect(() => {
        // @ts-expect-error Testing invalid input
        load();
      }).toThrow('cheerio.load() expects a string');
    });
  });

  describe('.find', () => {
    it('() : should find nothing', () => {
      expect($('ul').find()).toHaveLength(0);
    });

    it('(single) : should find one descendant', () => {
      expect($('#fruits').find('.apple')[0].attribs).toHaveProperty(
        'class',
        'apple',
      );
    });

    // #1679 - text tags not filtered
    it('(single) : should filter out text nodes', () => {
      const $root = $(`<html>\n${fruits.replace(/></g, '>\n<')}\n</html>`);
      expect($root.find('.apple')[0].attribs).toHaveProperty('class', 'apple');
    });

    it('(many) : should find all matching descendant', () => {
      expect($('#fruits').find('li')).toHaveLength(3);
    });

    it('(many) : should merge all selected elems with matching descendants', () => {
      expect($('#fruits, #food', food).find('.apple')).toHaveLength(1);
    });

    it('(invalid single) : should return empty if cant find', () => {
      expect($('ul').find('blah')).toHaveLength(0);
    });

    it('(invalid single) : should query descendants only', () => {
      expect($('#fruits').find('ul')).toHaveLength(0);
    });

    it('should return empty if search already empty result', () => {
      expect($('#not-fruits').find('li')).toHaveLength(0);
    });

    it('should lowercase selectors', () => {
      expect($('#fruits').find('LI')).toHaveLength(3);
    });

    it('should query immediate descendant only', () => {
      const q = load('<foo><bar><bar></bar><bar></bar></bar></foo>');
      expect(q('foo').find('> bar')).toHaveLength(1);
    });

    it('should find siblings', () => {
      const q = load('<p class=a><p class=b></p>');
      expect(q('.a').find('+.b')).toHaveLength(1);
      expect(q('.a').find('~.b')).toHaveLength(1);
      expect(q('.a').find('+.a')).toHaveLength(0);
      expect(q('.a').find('~.a')).toHaveLength(0);
    });

    it('should find self', () => {
      const q = load('<p class=a></p>');
      expect(q('.a').find(':scope')).toHaveLength(1);
    });

    it('should query case-sensitively when in xml mode', () => {
      const q = load('<caseSenSitive allTheWay>', { xml: true });
      expect(q('caseSenSitive')).toHaveLength(1);
      expect(q('[allTheWay]')).toHaveLength(1);
      expect(q('casesensitive')).toHaveLength(0);
      expect(q('[alltheway]')).toHaveLength(0);
    });

    it('should throw an Error if given an invalid selector', () => {
      expect(() => {
        $('#fruits').find(':bah');
      }).toThrow('Unknown pseudo-class :bah');
    });

    it('should respect the `lowerCaseTags` option (#3495)', () => {
      const q = load(
        `<parentTag class="myClass">
          <firstTag> <child> blah </child> </firstTag>
          <secondTag> <child> blah </child> </secondTag>
        </parentTag> `,
        {
          xml: {
            xmlMode: true,
            decodeEntities: false,
            lowerCaseTags: true,
            lowerCaseAttributeNames: false,
            recognizeSelfClosing: true,
          },
        },
      );
      expect(q('.myClass').find('firstTag > child')).toHaveLength(1);
    });

    describe('(cheerio object) :', () => {
      it('returns only those nodes contained within the current selection', () => {
        const q = load(food);
        const $selection = q('#fruits').find(q('li'));

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe(q('.apple')[0]);
        expect($selection[1]).toBe(q('.orange')[0]);
        expect($selection[2]).toBe(q('.pear')[0]);
      });
      it('returns only those nodes contained within any element in the current selection', () => {
        const q = load(food);
        const $selection = q('.apple, #vegetables').find(q('li'));

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe(q('.carrot')[0]);
        expect($selection[1]).toBe(q('.sweetcorn')[0]);
      });
    });

    describe('(node) :', () => {
      it('returns node when contained within the current selection', () => {
        const q = load(food);
        const $selection = q('#fruits').find(q('.apple')[0]);

        expect($selection).toHaveLength(1);
        expect($selection[0]).toBe(q('.apple')[0]);
      });
      it('returns node when contained within any element the current selection', () => {
        const q = load(food);
        const $selection = q('#fruits, #vegetables').find(q('.carrot')[0]);

        expect($selection).toHaveLength(1);
        expect($selection[0]).toBe(q('.carrot')[0]);
      });
      it('does not return node that is not contained within the current selection', () => {
        const q = load(food);
        const $selection = q('#fruits').find(q('.carrot')[0]);

        expect($selection).toHaveLength(0);
      });
    });
  });

  describe('.children', () => {
    it('() : should get all children', () => {
      expect($('ul').children()).toHaveLength(3);
    });

    it('() : should skip text nodes', () => {
      expect($(mixedText).children()).toHaveLength(0);
    });

    it('() : should return children of all matched elements', () => {
      expect($('ul ul', food).children()).toHaveLength(5);
    });

    it('(selector) : should return children matching selector', () => {
      const { attribs } = $('ul').children('.orange')[0];
      expect(attribs).toHaveProperty('class', 'orange');
    });

    it('(invalid selector) : should return empty', () => {
      expect($('ul').children('.lulz')).toHaveLength(0);
    });

    it('should only match immediate children, not ancestors', () => {
      expect($(food).children('li')).toHaveLength(0);
    });
  });

  describe('.contents', () => {
    beforeEach(() => {
      $ = load(text);
    });

    it('() : should get all contents', () => {
      expect($('p').contents()).toHaveLength(5);
    });

    it('() : should skip text nodes', () => {
      expect($(mixedText).contents()).toHaveLength(2);
    });

    it('() : should include text nodes', () => {
      expect($('p').contents().first()[0].type).toBe('text');
    });

    it('() : should include comment nodes', () => {
      expect($('p').contents().last()[0].type).toBe('comment');
    });
  });

  describe('.next', () => {
    it('() : should return next element', () => {
      const { attribs } = $('.orange').next()[0];
      expect(attribs).toHaveProperty('class', 'pear');
    });

    it('() : should skip text nodes', () => {
      expect($(mixedText).next()[0]).toHaveProperty('name', 'b');
    });

    it('(no next) : should return empty for last child', () => {
      expect($('.pear').next()).toHaveLength(0);
    });

    it('(next on empty object) : should return empty', () => {
      expect($('.banana').next()).toHaveLength(0);
    });

    it('() : should operate over all elements in the selection', () => {
      expect($('.apple, .orange', food).next()).toHaveLength(2);
    });

    it('() : should return elements in order', () => {
      const result = load(eleven)('.red').next();
      expect(result).toHaveLength(2);
      expect(result.eq(0).text()).toBe('Six');
      expect(result.eq(1).text()).toBe('Ten');
    });

    it('should reject elements that violate the filter', () => {
      expect($('.apple').next('.non-existent')).toHaveLength(0);
    });

    it('should accept elements that satisfy the filter', () => {
      expect($('.apple').next('.orange')).toHaveLength(1);
    });

    describe('(selector) :', () => {
      it('should reject elements that violate the filter', () => {
        expect($('.apple').next('.non-existent')).toHaveLength(0);
      });

      it('should accept elements that satisfy the filter', () => {
        expect($('.apple').next('.orange')).toHaveLength(1);
      });
    });
  });

  describe('.nextAll', () => {
    it('() : should return all following siblings', () => {
      const elems = $('.apple').nextAll();
      expect(elems).toHaveLength(2);
      expect(elems[0].attribs).toHaveProperty('class', 'orange');
      expect(elems[1].attribs).toHaveProperty('class', 'pear');
    });

    it('(no next) : should return empty for last child', () => {
      expect($('.pear').nextAll()).toHaveLength(0);
    });

    it('(nextAll on empty object) : should return empty', () => {
      expect($('.banana').nextAll()).toHaveLength(0);
    });

    it('() : should operate over all elements in the selection', () => {
      expect($('.apple, .carrot', food).nextAll()).toHaveLength(3);
    });

    it('() : should not contain duplicate elements', () => {
      const elems = $('.apple, .orange', food);
      expect(elems.nextAll()).toHaveLength(2);
    });

    it('() : should not contain text elements', () => {
      const elems = $('.apple', fruits.replace(/></g, '>\n<'));
      expect(elems.nextAll()).toHaveLength(2);
    });

    describe('(selector) :', () => {
      it('should filter according to the provided selector', () => {
        expect($('.apple').nextAll('.pear')).toHaveLength(1);
      });

      it("should not consider siblings' contents when filtering", () => {
        expect($('#fruits', food).nextAll('li')).toHaveLength(0);
      });
    });
  });

  describe('.nextUntil', () => {
    it('() : should return all following siblings if no selector specified', () => {
      const elems = $('.apple', food).nextUntil();
      expect(elems).toHaveLength(2);
      expect(elems[0].attribs).toHaveProperty('class', 'orange');
      expect(elems[1].attribs).toHaveProperty('class', 'pear');
    });

    it('() : should filter out non-element nodes', () => {
      const elems = $('<div><div></div><!-- comment -->text<div></div></div>');
      const div = elems.children().eq(0);
      expect(div.nextUntil()).toHaveLength(1);
    });

    it('() : should operate over all elements in the selection', () => {
      const elems = $('.apple, .carrot', food);
      expect(elems.nextUntil()).toHaveLength(3);
    });

    it('() : should not contain duplicate elements', () => {
      const elems = $('.apple, .orange', food);
      expect(elems.nextUntil()).toHaveLength(2);
    });

    it('(selector) : should return all following siblings until selector', () => {
      const elems = $('.apple', food).nextUntil('.pear');
      expect(elems).toHaveLength(1);
      expect(elems[0].attribs).toHaveProperty('class', 'orange');
    });

    it('(selector) : should support selector matching multiple elements', () => {
      const elems = $('#disabled', forms).nextUntil('option, #unnamed');
      expect(elems).toHaveLength(2);
      expect(elems[0].attribs).toHaveProperty('id', 'submit');
      expect(elems[1].attribs).toHaveProperty('id', 'select');
    });

    it('(selector not sibling) : should return all following siblings', () => {
      const elems = $('.apple').nextUntil('#vegetables');
      expect(elems).toHaveLength(2);
    });

    it('(selector, filterString) : should return all following siblings until selector, filtered by filter', () => {
      const elems = $('.beer', drinks).nextUntil('.water', '.milk');
      expect(elems).toHaveLength(1);
      expect(elems[0].attribs).toHaveProperty('class', 'milk');
    });

    it('(null, filterString) : should return all following siblings until selector, filtered by filter', () => {
      const elems = $('<ul><li></li><li><p></p></li></ul>');
      const empty = elems.find('li').eq(0).nextUntil(null, 'p');
      expect(empty).toHaveLength(0);
    });

    it('() : should return an empty object for last child', () => {
      expect($('.pear').nextUntil()).toHaveLength(0);
    });

    it('() : should return an empty object when called on an empty object', () => {
      expect($('.banana').nextUntil()).toHaveLength(0);
    });

    it('(node) : should return all following siblings until the node', () => {
      const $fruits = $('#fruits').children();
      const elems = $fruits.eq(0).nextUntil($fruits[2]);
      expect(elems).toHaveLength(1);
    });

    it('(cheerio object) : should return all following siblings until any member of the cheerio object', () => {
      const $drinks = $(drinks).children();
      const $until = $([$drinks[4], $drinks[3]]);
      const elems = $drinks.eq(0).nextUntil($until);
      expect(elems).toHaveLength(2);
    });
  });

  describe('.prev', () => {
    it('() : should return previous element', () => {
      const { attribs } = $('.orange').prev()[0];
      expect(attribs).toHaveProperty('class', 'apple');
    });

    it('() : should skip text nodes', () => {
      expect($($(mixedText)[2]).prev()[0]).toHaveProperty('name', 'a');
    });

    it('(no prev) : should return empty for first child', () => {
      expect($('.apple').prev()).toHaveLength(0);
    });

    it('(prev on empty object) : should return empty', () => {
      expect($('.banana').prev()).toHaveLength(0);
    });

    it('() : should operate over all elements in the selection', () => {
      expect($('.orange, .pear', food).prev()).toHaveLength(2);
    });

    it('() : should maintain elements order', () => {
      const sel = load(eleven)('.sel');
      expect(sel).toHaveLength(3);
      expect(sel.eq(0).text()).toBe('Three');
      expect(sel.eq(1).text()).toBe('Nine');
      expect(sel.eq(2).text()).toBe('Eleven');

      // Swap last elements
      const el = sel[2];
      sel[2] = sel[1];
      sel[1] = el;

      const result = sel.prev();
      expect(result).toHaveLength(3);
      expect(result.eq(0).text()).toBe('Two');
      expect(result.eq(1).text()).toBe('Ten');
      expect(result.eq(2).text()).toBe('Eight');
    });

    describe('(selector) :', () => {
      it('should reject elements that violate the filter', () => {
        expect($('.orange').prev('.non-existent')).toHaveLength(0);
      });

      it('should accept elements that satisfy the filter', () => {
        expect($('.orange').prev('.apple')).toHaveLength(1);
      });

      it('(selector) : should reject elements that violate the filter', () => {
        expect($('.orange').prev('.non-existent')).toHaveLength(0);
      });

      it('(selector) : should accept elements that satisfy the filter', () => {
        expect($('.orange').prev('.apple')).toHaveLength(1);
      });
    });
  });

  describe('.prevAll', () => {
    it('() : should return all preceding siblings', () => {
      const elems = $('.pear').prevAll();
      expect(elems).toHaveLength(2);
      expect(elems[0].attribs).toHaveProperty('class', 'orange');
      expect(elems[1].attribs).toHaveProperty('class', 'apple');
    });

    it('() : should not contain text elements', () => {
      const elems = $('.pear', fruits.replace(/></g, '>\n<'));
      expect(elems.prevAll()).toHaveLength(2);
    });

    it('(no prev) : should return empty for first child', () => {
      expect($('.apple').prevAll()).toHaveLength(0);
    });

    it('(prevAll on empty object) : should return empty', () => {
      expect($('.banana').prevAll()).toHaveLength(0);
    });

    it('() : should operate over all elements in the selection', () => {
      expect($('.orange, .sweetcorn', food).prevAll()).toHaveLength(2);
    });

    it('() : should not contain duplicate elements', () => {
      const elems = $('.orange, .pear', food);
      expect(elems.prevAll()).toHaveLength(2);
    });

    describe('(selector) :', () => {
      it('should filter returned elements', () => {
        const elems = $('.pear').prevAll('.apple');
        expect(elems).toHaveLength(1);
      });

      it("should not consider siblings's descendents", () => {
        const elems = $('#vegetables', food).prevAll('li');
        expect(elems).toHaveLength(0);
      });
    });
  });

  describe('.prevUntil', () => {
    it('() : should return all preceding siblings if no selector specified', () => {
      const elems = $('.pear').prevUntil();
      expect(elems).toHaveLength(2);
      expect(elems[0].attribs).toHaveProperty('class', 'orange');
      expect(elems[1].attribs).toHaveProperty('class', 'apple');
    });

    it('() : should filter out non-element nodes', () => {
      const elems = $(
        '<div class="1"><div class="2"></div><!-- comment -->text<div class="3"></div></div>',
      );
      const div = elems.children().last();
      expect(div.prevUntil()).toHaveLength(1);
    });

    it('() : should operate over all elements in the selection', () => {
      const elems = $('.pear, .sweetcorn', food);
      expect(elems.prevUntil()).toHaveLength(3);
    });

    it('() : should not contain duplicate elements', () => {
      const elems = $('.orange, .pear', food);
      expect(elems.prevUntil()).toHaveLength(2);
    });

    it('(selector) : should return all preceding siblings until selector', () => {
      const elems = $('.pear').prevUntil('.apple');
      expect(elems).toHaveLength(1);
      expect(elems[0].attribs).toHaveProperty('class', 'orange');
    });

    it('(selector) : should support selector matching multiple elements', () => {
      const elems = $('#unnamed', forms).prevUntil('option, #disabled');
      expect(elems).toHaveLength(2);
      expect(elems[0].attribs).toHaveProperty('id', 'select');
      expect(elems[1].attribs).toHaveProperty('id', 'submit');
    });

    it('(selector not sibling) : should return all preceding siblings', () => {
      const elems = $('.sweetcorn', food).prevUntil('#fruits');
      expect(elems).toHaveLength(1);
      expect(elems[0].attribs).toHaveProperty('class', 'carrot');
    });

    it('(selector, filterString) : should return all preceding siblings until selector, filtered by filter', () => {
      const elems = $('.cider', drinks).prevUntil('.juice', '.water');
      expect(elems).toHaveLength(1);
      expect(elems[0].attribs).toHaveProperty('class', 'water');
    });

    it('(selector, filterString) : should return all preceding siblings until selector', () => {
      const elems = $('<ul><li><p></p></li><li></li></ul>');
      const empty = elems.find('li').eq(1).prevUntil(null, 'p');
      expect(empty).toHaveLength(0);
    });

    it('() : should return an empty object for first child', () => {
      expect($('.apple').prevUntil()).toHaveLength(0);
    });

    it('() : should return an empty object when called on an empty object', () => {
      expect($('.banana').prevUntil()).toHaveLength(0);
    });

    it('(node) : should return all previous siblings until the node', () => {
      const $fruits = $('#fruits').children();
      const elems = $fruits.eq(2).prevUntil($fruits[0]);
      expect(elems).toHaveLength(1);
    });

    it('(cheerio object) : should return all previous siblings until any member of the cheerio object', () => {
      const $drinks = $(drinks).children();
      const $until = $([$drinks[0], $drinks[1]]);
      const elems = $drinks.eq(4).prevUntil($until);
      expect(elems).toHaveLength(2);
    });
  });

  describe('.siblings', () => {
    it('() : should get all the siblings', () => {
      expect($('.orange').siblings()).toHaveLength(2);
      expect($('#fruits').siblings()).toHaveLength(0);
      expect($('.apple, .carrot', food).siblings()).toHaveLength(3);
    });

    it('(selector) : should get all siblings that match the selector', () => {
      expect($('.orange').siblings('.apple')).toHaveLength(1);
      expect($('.orange').siblings('.peach')).toHaveLength(0);
    });

    it('(selector) : should throw an Error if given an invalid selector', () => {
      expect(() => {
        $('.orange').siblings(':bah');
      }).toThrow('Unknown pseudo-class :bah');
    });

    it('(selector) : does not consider the contents of siblings when filtering (GH-374)', () => {
      expect($('#fruits', food).siblings('li')).toHaveLength(0);
    });

    it('() : when two elements are siblings to each other they have to be included', () => {
      const result = load(eleven)('.sel').siblings();
      expect(result).toHaveLength(7);
      expect(result.eq(0).text()).toBe('One');
      expect(result.eq(1).text()).toBe('Two');
      expect(result.eq(2).text()).toBe('Four');
      expect(result.eq(3).text()).toBe('Eight');
      expect(result.eq(4).text()).toBe('Nine');
      expect(result.eq(5).text()).toBe('Ten');
      expect(result.eq(6).text()).toBe('Eleven');
    });

    it('(selector) : when two elements are siblings to each other they have to be included', () => {
      const result = load(eleven)('.sel').siblings('.red');
      expect(result).toHaveLength(2);
      expect(result.eq(0).text()).toBe('Four');
      expect(result.eq(1).text()).toBe('Nine');
    });

    it('(cheerio) : test filtering with cheerio object', () => {
      const doc = load(eleven);
      const result = doc('.sel').siblings(doc(':not([class])'));
      expect(result).toHaveLength(4);
      expect(result.eq(0).text()).toBe('One');
      expect(result.eq(1).text()).toBe('Two');
      expect(result.eq(2).text()).toBe('Eight');
      expect(result.eq(3).text()).toBe('Ten');
    });
  });

  describe('.parents', () => {
    beforeEach(() => {
      $ = load(food);
    });

    it('() : should get all of the parents in logical order', () => {
      const orange = $('.orange').parents();
      expect(orange).toHaveLength(4);
      expect(orange[0].attribs).toHaveProperty('id', 'fruits');
      expect(orange[1].attribs).toHaveProperty('id', 'food');
      expect(orange[2].tagName).toBe('body');
      expect(orange[3].tagName).toBe('html');
      const fruits = $('#fruits').parents();
      expect(fruits).toHaveLength(3);
      expect(fruits[0].attribs).toHaveProperty('id', 'food');
      expect(fruits[1].tagName).toBe('body');
      expect(fruits[2].tagName).toBe('html');
    });

    it('(selector) : should get all of the parents that match the selector in logical order', () => {
      const fruits = $('.orange').parents('#fruits');
      expect(fruits).toHaveLength(1);
      expect(fruits[0].attribs).toHaveProperty('id', 'fruits');
      const uls = $('.orange').parents('ul');
      expect(uls).toHaveLength(2);
      expect(uls[0].attribs).toHaveProperty('id', 'fruits');
      expect(uls[1].attribs).toHaveProperty('id', 'food');
    });

    it('() : should not break if the selector does not have any results', () => {
      const result = $('.saladbar').parents();
      expect(result).toHaveLength(0);
    });

    it('() : should return an empty set for top-level elements', () => {
      const result = $('html').parents();
      expect(result).toHaveLength(0);
    });

    it('() : should return the parents of every element in the *reversed* collection, omitting duplicates', () => {
      const $parents = $('li').parents();

      expect($parents).toHaveLength(5);
      expect($parents[0]).toBe($('#vegetables')[0]);
      expect($parents[1]).toBe($('#fruits')[0]);
      expect($parents[2]).toBe($('#food')[0]);
      expect($parents[3]).toBe($('body')[0]);
      expect($parents[4]).toBe($('html')[0]);
    });
  });

  describe('.parentsUntil', () => {
    beforeEach(() => {
      $ = load(food);
    });

    it('() : should get all of the parents in logical order', () => {
      const result = $('.orange').parentsUntil();
      expect(result).toHaveLength(4);
      expect(result[0].attribs).toHaveProperty('id', 'fruits');
      expect(result[1].attribs).toHaveProperty('id', 'food');
      expect(result[2].tagName).toBe('body');
      expect(result[3].tagName).toBe('html');
    });

    it('() : should get all of the parents in reversed order, omitting duplicates', () => {
      const result = $('.apple, .sweetcorn').parentsUntil();
      expect(result).toHaveLength(5);
      expect(result[0]).toBe($('#vegetables')[0]);
      expect(result[1]).toBe($('#fruits')[0]);
      expect(result[2]).toBe($('#food')[0]);
      expect(result[3]).toBe($('body')[0]);
      expect(result[4]).toBe($('html')[0]);
    });

    it('(selector) : should get all of the parents until selector', () => {
      const food = $('.orange').parentsUntil('#food');
      expect(food).toHaveLength(1);
      expect(food[0].attribs).toHaveProperty('id', 'fruits');
      const fruits = $('.orange').parentsUntil('#fruits');
      expect(fruits).toHaveLength(0);
    });

    it('(selector) : Less simple parentsUntil check with selector', () => {
      const result = $('#fruits').parentsUntil('html, body');
      expect(result.eq(0).attr('id')).toBe('food');
    });

    it('(selector not parent) : should return all parents', () => {
      const result = $('.orange').parentsUntil('.apple');
      expect(result).toHaveLength(4);
      expect(result[0].attribs).toHaveProperty('id', 'fruits');
      expect(result[1].attribs).toHaveProperty('id', 'food');
      expect(result[2].tagName).toBe('body');
      expect(result[3].tagName).toBe('html');
    });

    it('(selector, filter) : should get all of the parents that match the filter', () => {
      const result = $('.apple, .sweetcorn').parentsUntil(
        '.saladbar',
        '#vegetables',
      );
      expect(result).toHaveLength(1);
      expect(result[0].attribs).toHaveProperty('id', 'vegetables');
    });

    it('(selector, filter) : Multiple-filtered parentsUntil check', () => {
      const result = $('.orange').parentsUntil('html', 'ul,body');
      expect(result).toHaveLength(3);
      expect(result.eq(0).attr('id')).toBe('fruits');
      expect(result.eq(1).attr('id')).toBe('food');
      expect(result.eq(2).prop('tagName')).toBe('BODY');
    });

    it('() : should return empty object when called on an empty object', () => {
      const result = $('.saladbar').parentsUntil();
      expect(result).toHaveLength(0);
    });

    it('() : should return an empty set for top-level elements', () => {
      const result = $('html').parentsUntil();
      expect(result).toHaveLength(0);
    });

    it('(cheerio object) : should return all parents until any member of the cheerio object', () => {
      const $fruits = $('#fruits');
      const $until = $('#food');
      const result = $fruits.children().eq(1).parentsUntil($until);
      expect(result).toHaveLength(1);
      expect(result[0].attribs).toHaveProperty('id', 'fruits');
    });

    it('(cheerio object) : should return all parents until body element', () => {
      const body = $('body')[0];
      const result = $('.carrot').parentsUntil(body);
      expect(result).toHaveLength(2);
      expect(result.eq(0).is('ul#vegetables')).toBe(true);
    });
  });

  describe('.parent', () => {
    it('() : should return the parent of each matched element', () => {
      let result = $('.orange').parent();
      expect(result).toHaveLength(1);
      expect(result[0].attribs).toHaveProperty('id', 'fruits');
      result = $('li', food).parent();
      expect(result).toHaveLength(2);
      expect(result[0].attribs).toHaveProperty('id', 'fruits');
      expect(result[1].attribs).toHaveProperty('id', 'vegetables');
    });

    it('(undefined) : should not throw an exception', () => {
      expect(() => {
        $('li').parent(undefined);
      }).not.toThrow();
    });

    it('() : should return an empty object for top-level elements', () => {
      const result = $('html').parent();
      expect(result).toHaveLength(0);
    });

    it('() : should not contain duplicate elements', () => {
      const result = $('li').parent();
      expect(result).toHaveLength(1);
    });

    it('(selector) : should filter the matched parent elements by the selector', () => {
      const parents = $('.orange').parent();
      expect(parents).toHaveLength(1);
      expect(parents[0].attribs).toHaveProperty('id', 'fruits');
      const fruits = $('li', food).parent('#fruits');
      expect(fruits).toHaveLength(1);
      expect(fruits[0].attribs).toHaveProperty('id', 'fruits');
    });
  });

  describe('.closest', () => {
    it('() : should return an empty array', () => {
      const result = $('.orange').closest();
      expect(result).toHaveLength(0);
      expect(result).toBeInstanceOf(Cheerio);
    });

    it('(selector) : should find the closest element that matches the selector, searching through its ancestors and itself', () => {
      expect($('.orange').closest('.apple')).toHaveLength(0);
      expect(
        ($('.orange', food).closest('#food')[0] as Element).attribs,
      ).toHaveProperty('id', 'food');
      expect(
        ($('.orange', food).closest('ul')[0] as Element).attribs,
      ).toHaveProperty('id', 'fruits');
      expect(
        ($('.orange', food).closest('li')[0] as Element).attribs,
      ).toHaveProperty('class', 'orange');
    });

    it('(selector) : should find the closest element of each item, removing duplicates', () => {
      const result = $('li', food).closest('ul');
      expect(result).toHaveLength(2);
    });

    it('() : should not break if the selector does not have any results', () => {
      const result = $('.saladbar', food).closest('ul');
      expect(result).toHaveLength(0);
    });

    it('(selector) : should find closest element for text nodes', () => {
      const textNode = $('.apple', food).contents().first();
      const result = textNode.closest('#food') as Cheerio<Element>;
      expect(result[0].attribs).toHaveProperty('id', 'food');
    });
  });

  describe('.each', () => {
    it('( (i, elem) -> ) : should loop selected returning fn with (i, elem)', () => {
      const items: Element[] = [];
      const classes = ['apple', 'orange', 'pear'];
      $('li').each(function (idx, elem) {
        items[idx] = elem;
        expect(this.attribs).toHaveProperty('class', classes[idx]);
      });
      expect(items[0].attribs).toHaveProperty('class', 'apple');
      expect(items[1].attribs).toHaveProperty('class', 'orange');
      expect(items[2].attribs).toHaveProperty('class', 'pear');
    });

    it('( (i, elem) -> ) : should break iteration when the iterator function returns false', () => {
      let iterationCount = 0;
      $('li').each((idx) => {
        iterationCount++;
        return idx < 1;
      });

      expect(iterationCount).toBe(2);
    });
  });

  if (typeof Symbol !== 'undefined') {
    describe('[Symbol.iterator]', () => {
      it('should yield each element', () => {
        // The equivalent of: for (const element of $('li')) ...
        const $li = $('li');
        const iterator = $li[Symbol.iterator]() as Iterator<Element, Element>;
        expect(iterator.next().value.attribs).toHaveProperty('class', 'apple');
        expect(iterator.next().value.attribs).toHaveProperty('class', 'orange');
        expect(iterator.next().value.attribs).toHaveProperty('class', 'pear');
        expect(iterator.next().done).toBe(true);
      });
    });
  }

  describe('.map', () => {
    it('(fn) : should be invoked with the correct arguments and context', () => {
      const $fruits = $('li');
      const args: [number, AnyNode][] = [];
      const thisVals: AnyNode[] = [];

      $fruits.map(function (...myArgs) {
        args.push(myArgs);
        thisVals.push(this);
        return null;
      });

      expect(args).toStrictEqual([
        [0, $fruits[0]],
        [1, $fruits[1]],
        [2, $fruits[2]],
      ]);
      expect(thisVals).toStrictEqual([$fruits[0], $fruits[1], $fruits[2]]);
    });

    it('(fn) : should return an Cheerio object wrapping the returned items', () => {
      const $fruits = $('li');
      const $mapped = $fruits.map((i) => $fruits[2 - i]);

      expect($mapped).toHaveLength(3);
      expect($mapped[0]).toBe($fruits[2]);
      expect($mapped[1]).toBe($fruits[1]);
      expect($mapped[2]).toBe($fruits[0]);
    });

    it('(fn) : should ignore `null` and `undefined` returned by iterator', () => {
      const $fruits = $('li');
      const retVals = [null, undefined, $fruits[1]];

      const $mapped = $fruits.map((i) => retVals[i]);

      expect($mapped).toHaveLength(1);
      expect($mapped[0]).toBe($fruits[1]);
    });

    it('(fn) : should perform a shallow merge on arrays returned by iterator', () => {
      const $fruits = $('li');

      const $mapped = $fruits.map(() => [1, [3, 4]]);

      expect($mapped.get()).toStrictEqual([1, [3, 4], 1, [3, 4], 1, [3, 4]]);
    });

    it('(fn) : should tolerate `null` and `undefined` when flattening arrays returned by iterator', () => {
      const $fruits = $('li');

      const $mapped = $fruits.map(() => [null, undefined]);

      expect($mapped.get()).toStrictEqual([
        null,
        undefined,
        null,
        undefined,
        null,
        undefined,
      ]);
    });
  });

  describe('.filter', () => {
    it('(selector) : should reduce the set of matched elements to those that match the selector', () => {
      const pear = $('li').filter('.pear').text();
      expect(pear).toBe('Pear');
    });

    it('(selector) : should not consider nested elements', () => {
      const lis = $('#fruits').filter('li');
      expect(lis).toHaveLength(0);
    });

    it('(selection) : should reduce the set of matched elements to those that are contained in the provided selection', () => {
      const $fruits = $('li');
      const $pear = $fruits.filter('.pear, .apple');
      expect($fruits.filter($pear)).toHaveLength(2);
    });

    it('(element) : should reduce the set of matched elements to those that specified directly', () => {
      const $fruits = $('li');
      const pear = $fruits.filter('.pear')[0];
      expect($fruits.filter(pear)).toHaveLength(1);
    });

    it("(fn) : should reduce the set of matched elements to those that pass the function's test", () => {
      const orange = $('li')
        .filter(function (i, el) {
          expect(this).toBe(el);
          expect(el.tagName).toBe('li');
          expect(typeof i).toBe('number');
          return $(this).attr('class') === 'orange';
        })
        .text();

      expect(orange).toBe('Orange');
    });

    it('should also iterate over text nodes (#1867)', () => {
      const text = $('<a>a</a>b<c></c>').filter((_, el): el is Text =>
        isText(el),
      );

      expect(text[0].data).toBe('b');
    });
  });

  describe('.not', () => {
    it('(selector) : should reduce the set of matched elements to those that do not match the selector', () => {
      const $fruits = $('li');

      const $notPear = $fruits.not('.pear');

      expect($notPear).toHaveLength(2);
      expect($notPear[0]).toBe($fruits[0]);
      expect($notPear[1]).toBe($fruits[1]);
    });

    it('(selector) : should not consider nested elements', () => {
      const lis = $('#fruits').not('li');
      expect(lis).toHaveLength(1);
    });

    it('(selection) : should reduce the set of matched elements to those that are not contained in the provided selection', () => {
      const $fruits = $('li');
      const $orange = $('.orange');

      const $notOrange = $fruits.not($orange);

      expect($notOrange).toHaveLength(2);
      expect($notOrange[0]).toBe($fruits[0]);
      expect($notOrange[1]).toBe($fruits[2]);
    });

    it('(element) : should reduce the set of matched elements to those that specified directly', () => {
      const $fruits = $('li');
      const apple = $('.apple')[0];

      const $notApple = $fruits.not(apple);

      expect($notApple).toHaveLength(2);
      expect($notApple[0]).toBe($fruits[1]);
      expect($notApple[1]).toBe($fruits[2]);
    });

    it("(fn) : should reduce the set of matched elements to those that do not pass the function's test", () => {
      const $fruits = $('li');

      const $notOrange = $fruits.not(function (i, el) {
        expect(this).toBe(el);
        expect(el).toHaveProperty('name', 'li');
        expect(typeof i).toBe('number');
        return $(this).attr('class') === 'orange';
      });

      expect($notOrange).toHaveLength(2);
      expect($notOrange[0]).toBe($fruits[0]);
      expect($notOrange[1]).toBe($fruits[2]);
    });
  });

  describe('.has', () => {
    beforeEach(() => {
      $ = load(food);
    });

    it('(selector) : should reduce the set of matched elements to those with descendants that match the selector', () => {
      const $fruits = $('#fruits,#vegetables').has('.pear');
      expect($fruits).toHaveLength(1);
      expect($fruits[0]).toBe($('#fruits')[0]);
    });

    it('(selector) : should only consider nested elements', () => {
      const $empty = $('#fruits').has('#fruits');
      expect($empty).toHaveLength(0);
    });

    it('(element) : should reduce the set of matched elements to those that are ancestors of the provided element', () => {
      const $fruits = $('#fruits,#vegetables').has($('.pear')[0]);
      expect($fruits).toHaveLength(1);
      expect($fruits[0]).toBe($('#fruits')[0]);
    });

    it('(element) : should only consider nested elements', () => {
      const $fruits = $('#fruits');
      const fruitsEl = $fruits[0];
      const $empty = $fruits.has(fruitsEl);

      expect($empty).toHaveLength(0);
    });
  });

  describe('.first', () => {
    it('() : should return the first item', () => {
      const $src = $(
        '<span>foo</span><span>bar</span><span>baz</span>',
      ) as Cheerio<Element>;
      const $elem = $src.first();
      expect($elem.length).toBe(1);
      expect($elem[0].childNodes[0]).toHaveProperty('data', 'foo');
    });

    it('() : should return an empty object for an empty object', () => {
      const $src = $();
      const $first = $src.first();
      expect($first.length).toBe(0);
      expect($first[0]).toBeUndefined();
    });
  });

  describe('.last', () => {
    it('() : should return the last element', () => {
      const $src = $(
        '<span>foo</span><span>bar</span><span>baz</span>',
      ) as Cheerio<Element>;
      const $elem = $src.last();
      expect($elem.length).toBe(1);
      expect($elem[0].childNodes[0]).toHaveProperty('data', 'baz');
    });

    it('() : should return an empty object for an empty object', () => {
      const $src = $();
      const $last = $src.last();
      expect($last.length).toBe(0);
      expect($last[0]).toBeUndefined();
    });
  });

  describe('.first & .last', () => {
    it('() : should return equivalent collections if only one element', () => {
      const $src = $('<span>bar</span>') as Cheerio<Element>;
      const $first = $src.first();
      const $last = $src.last();
      expect($first.length).toBe(1);
      expect($first[0].childNodes[0]).toHaveProperty('data', 'bar');
      expect($last.length).toBe(1);
      expect($last[0].childNodes[0]).toHaveProperty('data', 'bar');
      expect($first[0]).toBe($last[0]);
    });
  });

  describe('.eq', () => {
    it('(i) : should return the element at the specified index', () => {
      expect(getText($('li').eq(0))).toBe('Apple');
      expect(getText($('li').eq(1))).toBe('Orange');
      expect(getText($('li').eq(2))).toBe('Pear');
      expect(getText($('li').eq(3))).toBeUndefined();
      expect(getText($('li').eq(-1))).toBe('Pear');
    });
  });

  describe('.get', () => {
    it('(i) : should return the element at the specified index', () => {
      const children = $('#fruits').children();
      expect(children.get(0)).toBe(children[0]);
      expect(children.get(1)).toBe(children[1]);
      expect(children.get(2)).toBe(children[2]);
    });

    it('(-1) : should return the element indexed from the end of the collection', () => {
      const children = $('#fruits').children();
      expect(children.get(-1)).toBe(children[2]);
      expect(children.get(-2)).toBe(children[1]);
      expect(children.get(-3)).toBe(children[0]);
    });

    it('() : should return an array containing all of the collection', () => {
      const children = $('#fruits').children();
      const all = children.get();
      expect(Array.isArray(all)).toBe(true);
      expect(all).toStrictEqual([children[0], children[1], children[2]]);
    });
  });

  describe('.index', () => {
    describe('() :', () => {
      it('returns the index of a child amongst its siblings', () => {
        expect($('.orange').index()).toBe(1);
      });
      it('returns -1 when the selection has no parent', () => {
        expect($('<div/>').index()).toBe(-1);
      });
    });

    describe('(selector) :', () => {
      it('returns the index of the first element in the set matched by `selector`', () => {
        expect($('.apple').index('#fruits, li')).toBe(1);
      });
      it('returns -1 when the item is not present in the set matched by `selector`', () => {
        expect($('.apple').index('#fuits')).toBe(-1);
      });
      it('returns -1 when the first element in the set has no parent', () => {
        expect($('<div/>').index('*')).toBe(-1);
      });
    });

    describe('(node) :', () => {
      it('returns the index of the given node within the current selection', () => {
        const $lis = $('li');
        expect($lis.index($lis.get(1))).toBe(1);
      });
      it('returns the index of the given node within the current selection when the current selection has no parent', () => {
        const $apple = $('.apple').remove();

        expect($apple.index($apple.get(0))).toBe(0);
      });
      it('returns -1 when the given node is not present in the current selection', () => {
        expect($('li').index($('#fruits').get(0))).toBe(-1);
      });
      it('returns -1 when the current selection is empty', () => {
        expect($('.not-fruit').index($('#fruits').get(0))).toBe(-1);
      });
    });

    describe('(selection) :', () => {
      it('returns the index of the first node in the provided selection within the current selection', () => {
        const $lis = $('li');
        expect($lis.index($('.orange, .pear'))).toBe(1);
      });
      it('returns -1 when the given node is not present in the current selection', () => {
        expect($('li').index($('#fruits'))).toBe(-1);
      });
      it('returns -1 when the current selection is empty', () => {
        expect($('.not-fruit').index($('#fruits'))).toBe(-1);
      });
    });
  });

  describe('.slice', () => {
    it('(start) : should return all elements after the given index', () => {
      const sliced = $('li').slice(1);
      expect(sliced).toHaveLength(2);
      expect(getText(sliced.eq(0))).toBe('Orange');
      expect(getText(sliced.eq(1))).toBe('Pear');
    });

    it('(start, end) : should return all elements matching the given range', () => {
      const sliced = $('li').slice(1, 2);
      expect(sliced).toHaveLength(1);
      expect(getText(sliced.eq(0))).toBe('Orange');
    });

    it('(-start) : should return element matching the offset from the end', () => {
      const sliced = $('li').slice(-1);
      expect(sliced).toHaveLength(1);
      expect(getText(sliced.eq(0))).toBe('Pear');
    });
  });

  describe('.end() :', () => {
    let $fruits: Cheerio<Element>;

    beforeEach(() => {
      $fruits = $('#fruits').children();
    });

    it('returns an empty object at the end of the chain', () => {
      expect($fruits.end().end().end()).toBeTruthy();
      expect($fruits.end().end().end()).toHaveLength(0);
    });
    it('find', () => {
      expect($fruits.find('.apple').end()).toBe($fruits);
    });
    it('filter', () => {
      expect($fruits.filter('.apple').end()).toBe($fruits);
    });
    it('map', () => {
      expect(
        $fruits
          .map(function () {
            return this;
          })
          .end(),
      ).toBe($fruits);
    });
    it('contents', () => {
      expect($fruits.contents().end()).toBe($fruits);
    });
    it('eq', () => {
      expect($fruits.eq(1).end()).toBe($fruits);
    });
    it('first', () => {
      expect($fruits.first().end()).toBe($fruits);
    });
    it('last', () => {
      expect($fruits.last().end()).toBe($fruits);
    });
    it('slice', () => {
      expect($fruits.slice(1).end()).toBe($fruits);
    });
    it('children', () => {
      expect($fruits.children().end()).toBe($fruits);
    });
    it('parent', () => {
      expect($fruits.parent().end()).toBe($fruits);
    });
    it('parents', () => {
      expect($fruits.parents().end()).toBe($fruits);
    });
    it('closest', () => {
      expect($fruits.closest('ul').end()).toBe($fruits);
    });
    it('siblings', () => {
      expect($fruits.siblings().end()).toBe($fruits);
    });
    it('next', () => {
      expect($fruits.next().end()).toBe($fruits);
    });
    it('nextAll', () => {
      expect($fruits.nextAll().end()).toBe($fruits);
    });
    it('prev', () => {
      expect($fruits.prev().end()).toBe($fruits);
    });
    it('prevAll', () => {
      expect($fruits.prevAll().end()).toBe($fruits);
    });
    it('clone', () => {
      expect($fruits.clone().end()).toBe($fruits);
    });
  });

  describe('.add()', () => {
    let $fruits: Cheerio<AnyNode>;
    let $apple: Cheerio<Element>;
    let $orange: Cheerio<Element>;
    let $pear: Cheerio<Element>;

    beforeEach(() => {
      $ = load(food);
      $fruits = $('#fruits');
      $apple = $('.apple');
      $orange = $('.orange');
      $pear = $('.pear');
    });

    describe('(selector) matched element :', () => {
      it('occurs before current selection', () => {
        const $selection = $orange.add('.apple');

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('is identical to the current selection', () => {
        const $selection = $orange.add('.orange');

        expect($selection).toHaveLength(1);
        expect($selection[0]).toBe($orange[0]);
      });
      it('occurs after current selection', () => {
        const $selection = $orange.add('.pear');

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($orange[0]);
        expect($selection[1]).toBe($pear[0]);
      });
      it('contains the current selection', () => {
        const $selection = $orange.add('#fruits');

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('is a child of the current selection', () => {
        const $selection = $fruits.add('.orange');

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('is root object preserved', () => {
        const $selection = $('<div></div>').add('#fruits');

        expect($selection).toHaveLength(2);
        expect($selection.eq(0).is('div')).toBe(true);
        expect($selection.eq(1).is($fruits.eq(0))).toBe(true);
      });
    });
    describe('(selector) matched elements :', () => {
      it('occur before the current selection', () => {
        const $selection = $pear.add('.apple, .orange');

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('include the current selection', () => {
        const $selection = $pear.add('#fruits li');

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('occur after the current selection', () => {
        const $selection = $apple.add('.orange, .pear');

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('occur within the current selection', () => {
        const $selection = $fruits.add('#fruits li');

        expect($selection).toHaveLength(4);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($apple[0]);
        expect($selection[2]).toBe($orange[0]);
        expect($selection[3]).toBe($pear[0]);
      });
    });
    describe('(selector, context) :', () => {
      it(', context)', () => {
        const $selection = $fruits.add('li', '#vegetables');
        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($('.carrot')[0]);
        expect($selection[2]).toBe($('.sweetcorn')[0]);
      });
    });

    describe('(element) honors document order when element occurs :', () => {
      it('before the current selection', () => {
        const $selection = $orange.add($apple[0]);

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('after the current selection', () => {
        const $selection = $orange.add($pear[0]);

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($orange[0]);
        expect($selection[1]).toBe($pear[0]);
      });
      it('within the current selection', () => {
        const $selection = $fruits.add($orange[0]);

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('as an ancestor of the current selection', () => {
        const $selection = $orange.add($fruits[0]);

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('does not insert an element already contained within the current selection', () => {
        const $selection = $apple.add($apple[0]);

        expect($selection).toHaveLength(1);
        expect($selection[0]).toBe($apple[0]);
      });
    });
    describe('([elements]) : elements', () => {
      it('occur before the current selection', () => {
        const $selection = $pear.add($('.apple, .orange').get());

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('include the current selection', () => {
        const $selection = $pear.add($('#fruits li').get());

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('occur after the current selection', () => {
        const $selection = $apple.add($('.orange, .pear').get());

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('occur within the current selection', () => {
        const $selection = $fruits.add($('#fruits li').get());

        expect($selection).toHaveLength(4);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($apple[0]);
        expect($selection[2]).toBe($orange[0]);
        expect($selection[3]).toBe($pear[0]);
      });
    });

    /**
     * Element order is undefined in this case, so it should not be asserted
     * here.
     *
     * If the collection consists of elements from different documents or ones
     * not in any document, the sort order is undefined.
     *
     * @see {@link https://api.jquery.com/add/}
     */
    it('(html) : correctly parses and adds the new elements', () => {
      const $selection = $apple.add('<li class="banana">banana</li>');

      expect($selection).toHaveLength(2);
      expect($selection.is('.apple')).toBe(true);
      expect($selection.is('.banana')).toBe(true);
    });

    describe('(selection) element in selection :', () => {
      it('occurs before current selection', () => {
        const $selection = $orange.add($('.apple'));

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('is identical to the current selection', () => {
        const $selection = $orange.add($('.orange'));

        expect($selection).toHaveLength(1);
        expect($selection[0]).toBe($orange[0]);
      });
      it('occurs after current selection', () => {
        const $selection = $orange.add($('.pear'));

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($orange[0]);
        expect($selection[1]).toBe($pear[0]);
      });
      it('contains the current selection', () => {
        const $selection = $orange.add($('#fruits'));

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($orange[0]);
      });
      it('is a child of the current selection', () => {
        const $selection = $fruits.add($('.orange'));

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($orange[0]);
      });
    });
    describe('(selection) elements in the selection :', () => {
      it('occur before the current selection', () => {
        const $selection = $pear.add($('.apple, .orange'));

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('include the current selection', () => {
        const $selection = $pear.add($('#fruits li'));

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('occur after the current selection', () => {
        const $selection = $apple.add($('.orange, .pear'));

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($apple[0]);
        expect($selection[1]).toBe($orange[0]);
        expect($selection[2]).toBe($pear[0]);
      });
      it('occur within the current selection', () => {
        const $selection = $fruits.add($('#fruits li'));

        expect($selection).toHaveLength(4);
        expect($selection[0]).toBe($fruits[0]);
        expect($selection[1]).toBe($apple[0]);
        expect($selection[2]).toBe($orange[0]);
        expect($selection[3]).toBe($pear[0]);
      });
    });

    describe('(selection) :', () => {
      it('modifying nested selections should not impact the parent [#834]', () => {
        const apple_pear = $apple.add($pear);

        // Applies red to apple and pear
        apple_pear.addClass('red');

        expect($apple.hasClass('red')).toBe(true); // This is true
        expect($pear.hasClass('red')).toBe(true); // This is true

        // Applies green to pear... AND should not affect apple
        $pear.addClass('green');
        expect($pear.hasClass('green')).toBe(true); // Currently this is true
        expect($apple.hasClass('green')).toBe(false); // And this should be false!
      });
    });
  });

  describe('.addBack', () => {
    describe('() :', () => {
      it('includes siblings and self', () => {
        const $selection = $('.orange').siblings().addBack();

        expect($selection).toHaveLength(3);
        expect($selection[0]).toBe($('.apple')[0]);
        expect($selection[1]).toBe($('.orange')[0]);
        expect($selection[2]).toBe($('.pear')[0]);
      });
      it('includes children and self', () => {
        const $selection = $('#fruits').children().addBack();

        expect($selection).toHaveLength(4);
        expect($selection[0]).toBe($('#fruits')[0]);
        expect($selection[1]).toBe($('.apple')[0]);
        expect($selection[2]).toBe($('.orange')[0]);
        expect($selection[3]).toBe($('.pear')[0]);
      });
      it('includes parent and self', () => {
        const $selection = $('.apple').parent().addBack();

        expect($selection).toHaveLength(2);
        expect($selection[0]).toBe($('#fruits')[0]);
        expect($selection[1]).toBe($('.apple')[0]);
      });
      it('includes parents and self', () => {
        const q = load(food);
        const $selection = q('.apple').parents().addBack();

        expect($selection).toHaveLength(5);
        expect($selection[0]).toBe(q('html')[0]);
        expect($selection[1]).toBe(q('body')[0]);
        expect($selection[2]).toBe(q('#food')[0]);
        expect($selection[3]).toBe(q('#fruits')[0]);
        expect($selection[4]).toBe(q('.apple')[0]);
      });
    });
    it('(filter) : filters the previous selection', () => {
      const $selection = $('li').eq(1).addBack('.apple');

      expect($selection).toHaveLength(2);
      expect($selection[0]).toBe($('.apple')[0]);
      expect($selection[1]).toBe($('.orange')[0]);
    });
    it('() : fails gracefully when no args are passed', () => {
      const $div = cheerio('<div>');
      expect($div.addBack()).toBe($div);
    });
  });

  describe('.is', () => {
    it('() : should return false', () => {
      expect($('li.apple').is()).toBe(false);
    });

    it('(true selector) : should return true', () => {
      expect(cheerio('#vegetables', vegetables).is('ul')).toBe(true);
    });

    it('(false selector) : should return false', () => {
      expect(cheerio('#vegetables', vegetables).is('div')).toBe(false);
    });

    it('(true selection) : should return true', () => {
      const $vegetables = cheerio('li', vegetables);
      expect($vegetables.is($vegetables.eq(1))).toBe(true);
    });

    it('(false selection) : should return false', () => {
      const $vegetableList = cheerio(vegetables);
      const $vegetables = $vegetableList.find('li');
      expect($vegetables.is($vegetableList)).toBe(false);
    });

    it('(true element) : should return true', () => {
      const $vegetables = cheerio('li', vegetables);
      expect($vegetables.is($vegetables[0])).toBe(true);
    });

    it('(false element) : should return false', () => {
      const $vegetableList = cheerio(vegetables);
      const $vegetables = $vegetableList.find('li');
      expect($vegetables.is($vegetableList[0])).toBe(false);
    });

    it('(true predicate) : should return true', () => {
      const result = $('li').is(function () {
        return this.tagName === 'li' && $(this).hasClass('pear');
      });
      expect(result).toBe(true);
    });

    it('(false predicate) : should return false', () => {
      const result = $('li')
        .last()
        .is(function () {
          return this.tagName === 'ul';
        });
      expect(result).toBe(false);
    });
  });
});
```

## File: `src/api/traversing.ts`
```typescript
/**
 * Methods for traversing the DOM structure.
 *
 * @module cheerio/traversing
 */

import * as select from 'cheerio-select';
import {
  type AnyNode,
  type Document,
  type Element,
  hasChildren,
  isDocument,
  isTag,
} from 'domhandler';
import {
  getChildren,
  getSiblings,
  nextElementSibling,
  prevElementSibling,
  uniqueSort,
} from 'domutils';
import type { Cheerio } from '../cheerio.js';
import { contains } from '../static.js';
import type { AcceptedFilters, FilterFunction } from '../types.js';
import { domEach, isCheerio } from '../utils.js';

const reContextSelector = /^\s*(?:[+~]|:scope\b)/;

/**
 * Get the descendants of each element in the current set of matched elements,
 * filtered by a selector, jQuery object, or element.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('#fruits').find('li').length;
 * //=> 3
 * $('#fruits').find($('.apple')).length;
 * //=> 1
 * ```
 *
 * @param selectorOrHaystack - Element to look for.
 * @returns The found elements.
 * @see {@link https://api.jquery.com/find/}
 */
export function find<T extends AnyNode>(
  this: Cheerio<T>,
  selectorOrHaystack?: string | Cheerio<Element> | Element,
): Cheerio<Element> {
  if (!selectorOrHaystack) {
    return this._make([]);
  }

  if (typeof selectorOrHaystack !== 'string') {
    const haystack = isCheerio(selectorOrHaystack)
      ? selectorOrHaystack.toArray()
      : [selectorOrHaystack];

    const context = this.toArray();

    return this._make(
      haystack.filter((elem) => context.some((node) => contains(node, elem))),
    );
  }

  return this._findBySelector(selectorOrHaystack, Number.POSITIVE_INFINITY);
}

/**
 * Find elements by a specific selector.
 *
 * @private
 * @category Traversing
 * @param selector - Selector to filter by.
 * @param limit - Maximum number of elements to match.
 * @returns The found elements.
 */
export function _findBySelector<T extends AnyNode>(
  this: Cheerio<T>,
  selector: string,
  limit: number,
): Cheerio<Element> {
  const context = this.toArray();

  const elems = reContextSelector.test(selector)
    ? context
    : this.children().toArray();

  const options = {
    context,
    root: this._root?.[0],

    // Pass options that are recognized by `cheerio-select`
    xmlMode: this.options.xmlMode,
    lowerCaseTags: this.options.lowerCaseTags,
    lowerCaseAttributeNames: this.options.lowerCaseAttributeNames,
    pseudos: this.options.pseudos,
    quirksMode: this.options.quirksMode,
  };

  return this._make(select.select(selector, elems, options, limit));
}

/**
 * Creates a matcher, using a particular mapping function. Matchers provide a
 * function that finds elements using a generating function, supporting
 * filtering.
 *
 * @private
 * @param matchMap - Mapping function.
 * @returns - Function for wrapping generating functions.
 */
function _getMatcher<P>(
  matchMap: (fn: (elem: AnyNode) => P, elems: Cheerio<AnyNode>) => Element[],
) {
  return (
    fn: (elem: AnyNode) => P,
    ...postFns: ((elems: Element[]) => Element[])[]
  ) =>
    function <T extends AnyNode>(
      this: Cheerio<T>,
      selector?: AcceptedFilters<Element>,
    ): Cheerio<Element> {
      let matched: Element[] = matchMap(fn, this);

      if (selector) {
        matched = filterArray(
          matched,
          selector,
          this.options.xmlMode,
          this._root?.[0],
        );
      }

      return this._make(
        // Post processing is only necessary if there is more than one element.
        this.length > 1 && matched.length > 1
          ? postFns.reduce((elems, fn) => fn(elems), matched)
          : matched,
      );
    };
}

/** Matcher that adds multiple elements for each entry in the input. */
const _matcher = _getMatcher((fn: (elem: AnyNode) => Element[], elems) =>
  elems.toArray().flatMap((elem) => fn(elem)),
);

/** Matcher that adds at most one element for each entry in the input. */
const _singleMatcher = _getMatcher(
  (fn: (elem: AnyNode) => Element | null, elems) => {
    const ret: Element[] = [];

    for (let i = 0; i < elems.length; i++) {
      const value = fn(elems[i]);
      if (value !== null) {
        ret.push(value);
      }
    }
    return ret;
  },
);

/**
 * Matcher that supports traversing until a condition is met.
 *
 * @param nextElem - Function that returns the next element.
 * @param postFns - Post processing functions.
 * @returns A function usable for `*Until` methods.
 */
function _matchUntil(
  nextElem: (elem: AnyNode) => Element | null,
  ...postFns: ((elems: Element[]) => Element[])[]
) {
  // We use a variable here that is used from within the matcher.
  let matches: ((el: Element, i: number) => boolean) | null = null;

  const innerMatcher = _getMatcher(
    (nextElem: (elem: AnyNode) => Element | null, elems) => {
      const matched: Element[] = [];

      domEach(elems, (elem) => {
        for (let next; (next = nextElem(elem)); elem = next) {
          // FIXME: `matched` might contain duplicates here and the index is too large.
          if (matches?.(next, matched.length)) break;
          matched.push(next);
        }
      });

      return matched;
    },
  )(nextElem, ...postFns);

  return function <T extends AnyNode>(
    this: Cheerio<T>,
    selector?: AcceptedFilters<Element> | null,
    filterSelector?: AcceptedFilters<Element>,
  ): Cheerio<Element> {
    // Override `matches` variable with the new target.
    matches =
      typeof selector === 'string'
        ? (elem: Element) => select.is(elem, selector, this.options)
        : selector
          ? getFilterFn(selector)
          : null;

    const ret = innerMatcher.call(this, filterSelector);

    // Set `matches` to `null`, so we don't waste memory.
    matches = null;

    return ret;
  };
}

function _removeDuplicates<T extends AnyNode>(elems: T[]): T[] {
  return elems.length > 1 ? [...new Set<T>(elems)] : elems;
}

/**
 * Get the parent of each element in the current set of matched elements,
 * optionally filtered by a selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.pear').parent().attr('id');
 * //=> fruits
 * ```
 *
 * @param selector - If specified filter for parent.
 * @returns The parents.
 * @see {@link https://api.jquery.com/parent/}
 */
export const parent: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _singleMatcher(
  ({ parent }) => (parent && !isDocument(parent) ? (parent as Element) : null),
  _removeDuplicates,
);

/**
 * Get a set of parents filtered by `selector` of each element in the current
 * set of match elements.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.orange').parents().length;
 * //=> 2
 * $('.orange').parents('#fruits').length;
 * //=> 1
 * ```
 *
 * @param selector - If specified filter for parents.
 * @returns The parents.
 * @see {@link https://api.jquery.com/parents/}
 */
export const parents: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matcher(
  (elem) => {
    const matched: Element[] = [];
    while (elem.parent && !isDocument(elem.parent)) {
      matched.push(elem.parent as Element);
      elem = elem.parent;
    }
    return matched;
  },
  uniqueSort,
  // eslint-disable-next-line unicorn/no-array-reverse
  (elems) => elems.reverse(),
);

/**
 * Get the ancestors of each element in the current set of matched elements, up
 * to but not including the element matched by the selector, DOM node, or
 * cheerio object.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.orange').parentsUntil('#food').length;
 * //=> 1
 * ```
 *
 * @param selector - Selector for element to stop at.
 * @param filterSelector - Optional filter for parents.
 * @returns The parents.
 * @see {@link https://api.jquery.com/parentsUntil/}
 */
export const parentsUntil: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element> | null,
  filterSelector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matchUntil(
  ({ parent }) => (parent && !isDocument(parent) ? (parent as Element) : null),
  uniqueSort,
  // eslint-disable-next-line unicorn/no-array-reverse
  (elems) => elems.reverse(),
);

/**
 * For each element in the set, get the first element that matches the selector
 * by testing the element itself and traversing up through its ancestors in the
 * DOM tree.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.orange').closest();
 * //=> []
 *
 * $('.orange').closest('.apple');
 * // => []
 *
 * $('.orange').closest('li');
 * //=> [<li class="orange">Orange</li>]
 *
 * $('.orange').closest('#fruits');
 * //=> [<ul id="fruits"> ... </ul>]
 * ```
 *
 * @param selector - Selector for the element to find.
 * @returns The closest nodes.
 * @see {@link https://api.jquery.com/closest/}
 */
export function closest<T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
): Cheerio<AnyNode> {
  const set: AnyNode[] = [];

  if (!selector) {
    return this._make(set);
  }

  const selectOpts = {
    xmlMode: this.options.xmlMode,
    root: this._root?.[0],
  };

  const selectFn =
    typeof selector === 'string'
      ? (elem: Element) => select.is(elem, selector, selectOpts)
      : getFilterFn(selector);

  domEach(this, (elem: AnyNode | null) => {
    if (elem && !isDocument(elem) && !isTag(elem)) {
      elem = elem.parent;
    }
    while (elem && isTag(elem)) {
      if (selectFn(elem, 0)) {
        // Do not add duplicate elements to the set
        if (!set.includes(elem)) {
          set.push(elem);
        }
        break;
      }
      elem = elem.parent;
    }
  });

  return this._make(set);
}

/**
 * Gets the next sibling of each selected element, optionally filtered by a
 * selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.apple').next().hasClass('orange');
 * //=> true
 * ```
 *
 * @param selector - If specified filter for sibling.
 * @returns The next nodes.
 * @see {@link https://api.jquery.com/next/}
 */
export const next: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _singleMatcher((elem) => nextElementSibling(elem));

/**
 * Gets all the following siblings of the each selected element, optionally
 * filtered by a selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.apple').nextAll();
 * //=> [<li class="orange">Orange</li>, <li class="pear">Pear</li>]
 * $('.apple').nextAll('.orange');
 * //=> [<li class="orange">Orange</li>]
 * ```
 *
 * @param selector - If specified filter for siblings.
 * @returns The next nodes.
 * @see {@link https://api.jquery.com/nextAll/}
 */
export const nextAll: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matcher((elem) => {
  const matched = [];
  while (elem.next) {
    elem = elem.next;
    if (isTag(elem)) matched.push(elem);
  }
  return matched;
}, _removeDuplicates);

/**
 * Gets all the following siblings up to but not including the element matched
 * by the selector, optionally filtered by another selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.apple').nextUntil('.pear');
 * //=> [<li class="orange">Orange</li>]
 * ```
 *
 * @param selector - Selector for element to stop at.
 * @param filterSelector - If specified filter for siblings.
 * @returns The next nodes.
 * @see {@link https://api.jquery.com/nextUntil/}
 */
export const nextUntil: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element> | null,
  filterSelector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matchUntil(
  (el) => nextElementSibling(el),
  _removeDuplicates,
);

/**
 * Gets the previous sibling of each selected element optionally filtered by a
 * selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.orange').prev().hasClass('apple');
 * //=> true
 * ```
 *
 * @param selector - If specified filter for siblings.
 * @returns The previous nodes.
 * @see {@link https://api.jquery.com/prev/}
 */
export const prev: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _singleMatcher((elem) => prevElementSibling(elem));

/**
 * Gets all the preceding siblings of each selected element, optionally filtered
 * by a selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.pear').prevAll();
 * //=> [<li class="orange">Orange</li>, <li class="apple">Apple</li>]
 *
 * $('.pear').prevAll('.orange');
 * //=> [<li class="orange">Orange</li>]
 * ```
 *
 * @param selector - If specified filter for siblings.
 * @returns The previous nodes.
 * @see {@link https://api.jquery.com/prevAll/}
 */
export const prevAll: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matcher((elem) => {
  const matched = [];
  while (elem.prev) {
    elem = elem.prev;
    if (isTag(elem)) matched.push(elem);
  }
  return matched;
}, _removeDuplicates);

/**
 * Gets all the preceding siblings up to but not including the element matched
 * by the selector, optionally filtered by another selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.pear').prevUntil('.apple');
 * //=> [<li class="orange">Orange</li>]
 * ```
 *
 * @param selector - Selector for element to stop at.
 * @param filterSelector - If specified filter for siblings.
 * @returns The previous nodes.
 * @see {@link https://api.jquery.com/prevUntil/}
 */
export const prevUntil: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element> | null,
  filterSelector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matchUntil(
  (el) => prevElementSibling(el),
  _removeDuplicates,
);

/**
 * Get the siblings of each element (excluding the element) in the set of
 * matched elements, optionally filtered by a selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.pear').siblings().length;
 * //=> 2
 *
 * $('.pear').siblings('.orange').length;
 * //=> 1
 * ```
 *
 * @param selector - If specified filter for siblings.
 * @returns The siblings.
 * @see {@link https://api.jquery.com/siblings/}
 */
export const siblings: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matcher(
  (elem) =>
    getSiblings(elem).filter((el): el is Element => isTag(el) && el !== elem),
  uniqueSort,
);

/**
 * Gets the element children of each element in the set of matched elements.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('#fruits').children().length;
 * //=> 3
 *
 * $('#fruits').children('.pear').text();
 * //=> Pear
 * ```
 *
 * @param selector - If specified filter for children.
 * @returns The children.
 * @see {@link https://api.jquery.com/children/}
 */
export const children: <T extends AnyNode>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<Element>,
) => Cheerio<Element> = _matcher(
  (elem) => getChildren(elem).filter(isTag),
  _removeDuplicates,
);

/**
 * Gets the children of each element in the set of matched elements, including
 * text and comment nodes.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('#fruits').contents().length;
 * //=> 3
 * ```
 *
 * @returns The children.
 * @see {@link https://api.jquery.com/contents/}
 */
export function contents<T extends AnyNode>(
  this: Cheerio<T>,
): Cheerio<AnyNode> {
  const elems = this.toArray().flatMap((elem) =>
    hasChildren(elem) ? elem.children : [],
  );
  return this._make(elems);
}

/**
 * Iterates over a cheerio object, executing a function for each matched
 * element. When the callback is fired, the function is fired in the context of
 * the DOM element, so `this` refers to the current element, which is equivalent
 * to the function parameter `element`. To break out of the `each` loop early,
 * return with `false`.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * const fruits = [];
 *
 * $('li').each(function (i, elem) {
 *   fruits[i] = $(this).text();
 * });
 *
 * fruits.join(', ');
 * //=> Apple, Orange, Pear
 * ```
 *
 * @param fn - Function to execute.
 * @returns The instance itself, useful for chaining.
 * @see {@link https://api.jquery.com/each/}
 */
export function each<T>(
  this: Cheerio<T>,
  fn: (this: T, i: number, el: T) => void | boolean,
): Cheerio<T> {
  let i = 0;
  const len = this.length;
  while (i < len && fn.call(this[i], i, this[i]) !== false) ++i;
  return this;
}

/**
 * Pass each element in the current matched set through a function, producing a
 * new Cheerio object containing the return values. The function can return an
 * individual data item or an array of data items to be inserted into the
 * resulting set. If an array is returned, the elements inside the array are
 * inserted into the set. If the function returns null or undefined, no element
 * will be inserted.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li')
 *   .map(function (i, el) {
 *     // this === el
 *     return $(this).text();
 *   })
 *   .toArray()
 *   .join(' ');
 * //=> "apple orange pear"
 * ```
 *
 * @param fn - Function to execute.
 * @returns The mapped elements, wrapped in a Cheerio collection.
 * @see {@link https://api.jquery.com/map/}
 */
export function map<T, M>(
  this: Cheerio<T>,
  fn: (this: T, i: number, el: T) => M[] | M | null | undefined,
): Cheerio<M> {
  let elems: M[] = [];
  for (let i = 0; i < this.length; i++) {
    const el = this[i];
    const val = fn.call(el, i, el);
    if (val != null) {
      // eslint-disable-next-line unicorn/prefer-spread
      elems = elems.concat(val);
    }
  }
  return this._make(elems);
}

/**
 * Creates a function to test if a filter is matched.
 *
 * @param match - A filter.
 * @returns A function that determines if a filter has been matched.
 */
function getFilterFn<T>(
  match: FilterFunction<T> | Cheerio<T> | T,
): (el: T, i: number) => boolean {
  if (typeof match === 'function') {
    return (el, i) => (match as FilterFunction<T>).call(el, i, el);
  }
  if (isCheerio<T>(match)) {
    return (el) => Array.prototype.includes.call(match, el);
  }
  return (el) => match === el;
}

/**
 * Iterates over a cheerio object, reducing the set of selector elements to
 * those that match the selector or pass the function's test.
 *
 * This is the definition for using type guards; have a look below for other
 * ways to invoke this method. The function is executed in the context of the
 * selected element, so `this` refers to the current element.
 *
 * @category Traversing
 * @example <caption>Function</caption>
 *
 * ```js
 * $('li')
 *   .filter(function (i, el) {
 *     // this === el
 *     return $(this).attr('class') === 'orange';
 *   })
 *   .attr('class'); //=> orange
 * ```
 *
 * @param match - Value to look for, following the rules above.
 * @returns The filtered collection.
 * @see {@link https://api.jquery.com/filter/}
 */
export function filter<T, S extends T>(
  this: Cheerio<T>,
  match: (this: T, index: number, value: T) => value is S,
): Cheerio<S>;
/**
 * Iterates over a cheerio object, reducing the set of selector elements to
 * those that match the selector or pass the function's test.
 *
 * - When a Cheerio selection is specified, return only the elements contained in
 *   that selection.
 * - When an element is specified, return only that element (if it is contained in
 *   the original selection).
 * - If using the function method, the function is executed in the context of the
 *   selected element, so `this` refers to the current element.
 *
 * @category Traversing
 * @example <caption>Selector</caption>
 *
 * ```js
 * $('li').filter('.orange').attr('class');
 * //=> orange
 * ```
 *
 * @example <caption>Function</caption>
 *
 * ```js
 * $('li')
 *   .filter(function (i, el) {
 *     // this === el
 *     return $(this).attr('class') === 'orange';
 *   })
 *   .attr('class'); //=> orange
 * ```
 *
 * @param match - Value to look for, following the rules above. See
 *   {@link AcceptedFilters}.
 * @returns The filtered collection.
 * @see {@link https://api.jquery.com/filter/}
 */
export function filter<T, S extends AcceptedFilters<T>>(
  this: Cheerio<T>,
  match: S,
): Cheerio<S extends string ? Element : T>;
export function filter<T>(
  this: Cheerio<T>,
  match: AcceptedFilters<T>,
): Cheerio<unknown> {
  return this._make<unknown>(
    filterArray(this.toArray(), match, this.options.xmlMode, this._root?.[0]),
  );
}

/**
 * Filter an array of nodes with either a selector or predicate.
 *
 * @param nodes - The nodes to filter.
 * @param match - Selector or predicate used to keep nodes.
 * @param xmlMode - Whether selector matching should use XML mode.
 * @param root - Optional document root used for selector matching.
 */
export function filterArray<T>(
  nodes: T[],
  match: AcceptedFilters<T>,
  xmlMode?: boolean,
  root?: Document,
): Element[] | T[] {
  return typeof match === 'string'
    ? select.filter(match, nodes as unknown as AnyNode[], { xmlMode, root })
    : nodes.filter(getFilterFn<T>(match));
}

/**
 * Checks the current list of elements and returns `true` if _any_ of the
 * elements match the selector. If using an element or Cheerio selection,
 * returns `true` if _any_ of the elements match. If using a predicate function,
 * the function is executed in the context of the selected element, so `this`
 * refers to the current element.
 *
 * @category Traversing
 * @param selector - Selector for the selection.
 * @returns Whether or not the selector matches an element of the instance.
 * @see {@link https://api.jquery.com/is/}
 */
export function is<T>(
  this: Cheerio<T>,
  selector?: AcceptedFilters<T>,
): boolean {
  const nodes = this.toArray();
  return typeof selector === 'string'
    ? select.some(
        (nodes as unknown as AnyNode[]).filter(isTag),
        selector,
        this.options,
      )
    : selector
      ? nodes.some(getFilterFn<T>(selector))
      : false;
}

/**
 * Remove elements from the set of matched elements. Given a Cheerio object that
 * represents a set of DOM elements, the `.not()` method constructs a new
 * Cheerio object from a subset of the matching elements. The supplied selector
 * is tested against each element; the elements that don't match the selector
 * will be included in the result.
 *
 * The `.not()` method can take a function as its argument in the same way that
 * `.filter()` does. Elements for which the function returns `true` are excluded
 * from the filtered set; all other elements are included.
 *
 * @category Traversing
 * @example <caption>Selector</caption>
 *
 * ```js
 * $('li').not('.apple').length;
 * //=> 2
 * ```
 *
 * @example <caption>Function</caption>
 *
 * ```js
 * $('li').not(function (i, el) {
 *   // this === el
 *   return $(this).attr('class') === 'orange';
 * }).length; //=> 2
 * ```
 *
 * @param match - Value to look for, following the rules above.
 * @returns The filtered collection.
 * @see {@link https://api.jquery.com/not/}
 */
export function not<T extends AnyNode>(
  this: Cheerio<T>,
  match: AcceptedFilters<T>,
): Cheerio<T> {
  let nodes = this.toArray();

  if (typeof match === 'string') {
    const matches = new Set<AnyNode>(select.filter(match, nodes, this.options));
    nodes = nodes.filter((el) => !matches.has(el));
  } else {
    const filterFn = getFilterFn(match);
    nodes = nodes.filter((el, i) => !filterFn(el, i));
  }

  return this._make(nodes);
}

/**
 * Filters the set of matched elements to only those which have the given DOM
 * element as a descendant or which have a descendant that matches the given
 * selector. Equivalent to `.filter(':has(selector)')`.
 *
 * @category Traversing
 * @example <caption>Selector</caption>
 *
 * ```js
 * $('ul').has('.pear').attr('id');
 * //=> fruits
 * ```
 *
 * @example <caption>Element</caption>
 *
 * ```js
 * $('ul').has($('.pear')[0]).attr('id');
 * //=> fruits
 * ```
 *
 * @param selectorOrHaystack - Element to look for.
 * @returns The filtered collection.
 * @see {@link https://api.jquery.com/has/}
 */
export function has(
  this: Cheerio<AnyNode | Element>,
  selectorOrHaystack: string | Cheerio<Element> | Element,
): Cheerio<AnyNode | Element> {
  return this.filter(
    typeof selectorOrHaystack === 'string'
      ? // Using the `:has` selector here short-circuits searches.
        `:has(${selectorOrHaystack})`
      : (_, el) => this._make(el).find(selectorOrHaystack).length > 0,
  );
}

/**
 * Will select the first element of a cheerio object.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('#fruits').children().first().text();
 * //=> Apple
 * ```
 *
 * @returns The first element.
 * @see {@link https://api.jquery.com/first/}
 */
export function first<T extends AnyNode>(this: Cheerio<T>): Cheerio<T> {
  return this.length > 1 ? this._make(this[0]) : this;
}

/**
 * Will select the last element of a cheerio object.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('#fruits').children().last().text();
 * //=> Pear
 * ```
 *
 * @returns The last element.
 * @see {@link https://api.jquery.com/last/}
 */
export function last<T>(this: Cheerio<T>): Cheerio<T> {
  return this.length > 0 ? this._make(this[this.length - 1]) : this;
}

/**
 * Reduce the set of matched elements to the one at the specified index. Use
 * `.eq(-i)` to count backwards from the last selected element.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li').eq(0).text();
 * //=> Apple
 *
 * $('li').eq(-1).text();
 * //=> Pear
 * ```
 *
 * @param i - Index of the element to select.
 * @returns The element at the `i`th position.
 * @see {@link https://api.jquery.com/eq/}
 */
export function eq<T>(this: Cheerio<T>, i: number): Cheerio<T> {
  i = +i;

  // Use the first identity optimization if possible
  if (i === 0 && this.length <= 1) return this;

  if (i < 0) i = this.length + i;
  return this._make(this[i] ?? []);
}

/**
 * Retrieve one of the elements matched by the Cheerio object, at the `i`th
 * position.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li').get(0).tagName;
 * //=> li
 * ```
 *
 * @param i - Element to retrieve.
 * @returns The element at the `i`th position.
 * @see {@link https://api.jquery.com/get/}
 */
export function get<T>(this: Cheerio<T>, i: number): T | undefined;
/**
 * Retrieve all elements matched by the Cheerio object, as an array.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li').get().length;
 * //=> 3
 * ```
 *
 * @returns All elements matched by the Cheerio object.
 * @see {@link https://api.jquery.com/get/}
 */
export function get<T>(this: Cheerio<T>): T[];
export function get<T>(this: Cheerio<T>, i?: number): T | T[] {
  if (i == null) {
    return this.toArray();
  }
  return this[i < 0 ? this.length + i : i];
}

/**
 * Retrieve all the DOM elements contained in the jQuery set as an array.
 *
 * @example
 *
 * ```js
 * $('li').toArray();
 * //=> [ {...}, {...}, {...} ]
 * ```
 *
 * @returns The contained items.
 */
export function toArray<T>(this: Cheerio<T>): T[] {
  return (Array.prototype as T[]).slice.call(this);
}

/**
 * Search for a given element from among the matched elements.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.pear').index();
 * //=> 2 $('.orange').index('li');
 * //=> 1
 * $('.apple').index($('#fruit, li'));
 * //=> 1
 * ```
 *
 * @param selectorOrNeedle - Element to look for.
 * @returns The index of the element.
 * @see {@link https://api.jquery.com/index/}
 */
export function index<T extends AnyNode>(
  this: Cheerio<T>,
  selectorOrNeedle?: string | Cheerio<AnyNode> | AnyNode,
): number {
  let $haystack: Cheerio<AnyNode>;
  let needle: AnyNode;

  if (selectorOrNeedle == null) {
    $haystack = this.parent().children();
    needle = this[0];
  } else if (typeof selectorOrNeedle === 'string') {
    $haystack = this._make<AnyNode>(selectorOrNeedle);
    needle = this[0];
  } else {
    // eslint-disable-next-line unicorn/no-this-assignment
    $haystack = this;
    needle = isCheerio(selectorOrNeedle)
      ? selectorOrNeedle[0]
      : selectorOrNeedle;
  }

  return Array.prototype.indexOf.call($haystack, needle);
}

/**
 * Gets the elements matching the specified range (0-based position).
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li').slice(1).eq(0).text();
 * //=> 'Orange'
 *
 * $('li').slice(1, 2).length;
 * //=> 1
 * ```
 *
 * @param start - A position at which the elements begin to be selected. If
 *   negative, it indicates an offset from the end of the set.
 * @param end - A position at which the elements stop being selected. If
 *   negative, it indicates an offset from the end of the set. If omitted, the
 *   range continues until the end of the set.
 * @returns The elements matching the specified range.
 * @see {@link https://api.jquery.com/slice/}
 */
export function slice<T>(
  this: Cheerio<T>,
  start?: number,
  end?: number,
): Cheerio<T> {
  return this._make<T>(Array.prototype.slice.call(this, start, end));
}

/**
 * End the most recent filtering operation in the current chain and return the
 * set of matched elements to its previous state.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li').eq(0).end().length;
 * //=> 3
 * ```
 *
 * @returns The previous state of the set of matched elements.
 * @see {@link https://api.jquery.com/end/}
 */
export function end<T>(this: Cheerio<T>): Cheerio<AnyNode> {
  return (this.prevObject as Cheerio<AnyNode> | null) ?? this._make([]);
}

/**
 * Add elements to the set of matched elements.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('.apple').add('.orange').length;
 * //=> 2
 * ```
 *
 * @param other - Elements to add.
 * @param context - Optionally the context of the new selection.
 * @returns The combined set.
 * @see {@link https://api.jquery.com/add/}
 */
export function add<S extends AnyNode, T extends AnyNode>(
  this: Cheerio<T>,
  other: string | Cheerio<S> | S | S[],
  context?: Cheerio<S> | string,
): Cheerio<S | T> {
  const selection = this._make(other, context);
  const contents = uniqueSort([...this.get(), ...selection.get()]);
  return this._make(contents);
}

/**
 * Add the previous set of elements on the stack to the current set, optionally
 * filtered by a selector.
 *
 * @category Traversing
 * @example
 *
 * ```js
 * $('li').eq(0).addBack('.orange').length;
 * //=> 2
 * ```
 *
 * @param selector - Selector for the elements to add.
 * @returns The combined set.
 * @see {@link https://api.jquery.com/addBack/}
 */
export function addBack<T extends AnyNode>(
  this: Cheerio<T>,
  selector?: string,
): Cheerio<AnyNode> {
  return this.prevObject
    ? this.add<AnyNode, T>(
        selector ? this.prevObject.filter(selector) : this.prevObject,
      )
    : this;
}
```

## File: `src/parsers/parse5-adapter.ts`
```typescript
import {
  type AnyNode,
  type Document,
  isDocument,
  type ParentNode,
} from 'domhandler';
import { parse as parseDocument, parseFragment, serializeOuter } from 'parse5';
import { adapter as htmlparser2Adapter } from 'parse5-htmlparser2-tree-adapter';
import type { InternalOptions } from '../options.js';

/**
 * Parse the content with `parse5` in the context of the given `ParentNode`.
 *
 * @param content - The content to parse.
 * @param options - A set of options to use to parse.
 * @param isDocument - Whether to parse the content as a full HTML document.
 * @param context - The context in which to parse the content.
 * @returns The parsed content.
 */
export function parseWithParse5(
  content: string,
  options: InternalOptions,
  isDocument: boolean,
  context: ParentNode | null,
): Document {
  options.treeAdapter ??= htmlparser2Adapter;

  if (options.scriptingEnabled !== false) {
    options.scriptingEnabled = true;
  }

  return isDocument
    ? parseDocument(content, options)
    : parseFragment(context, content, options);
}

const renderOpts = { treeAdapter: htmlparser2Adapter };

/**
 * Renders the given DOM tree with `parse5` and returns the result as a string.
 *
 * @param dom - The DOM tree to render.
 * @returns The rendered document.
 */
export function renderWithParse5(dom: AnyNode | ArrayLike<AnyNode>): string {
  /*
   * `dom-serializer` passes over the special "root" node and renders the
   * node's children in its place. To mimic this behavior with `parse5`, an
   * equivalent operation must be applied to the input array.
   */
  const nodes = 'length' in dom ? dom : [dom];
  for (let index = 0; index < nodes.length; index += 1) {
    const node = nodes[index];
    if (isDocument(node)) {
      Array.prototype.splice.call(nodes, index, 1, ...node.children);
    }
  }

  let result = '';
  for (let index = 0; index < nodes.length; index += 1) {
    const node = nodes[index];
    result += serializeOuter(node, renderOpts);
  }

  return result;
}
```

## File: `website/README.md`
```markdown
# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern
static website generator.

### Installation

```
$ yarn
```

### Local Development

```
$ yarn start
```

This command starts a local development server and opens up a browser window.
Most changes are reflected live without having to restart the server.

### Build

```
$ yarn build
```

This command generates static content into the `build` directory and can be
served using any static contents hosting service.
```

## File: `website/astro.config.mjs`
```
import mdx from '@astrojs/mdx';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';
import remarkDirective from 'remark-directive';
import { rehypeExternalLinks } from './src/plugins/rehype-external-links.ts';
import { remarkAdmonitions } from './src/plugins/remark-admonitions.ts';
import { remarkFixTypedocLinks } from './src/plugins/remark-fix-typedoc-links.ts';
import { remarkLiveCode } from './src/plugins/remark-live-code.ts';

export default defineConfig({
  site: 'https://cheerio.js.org',
  integrations: [mdx(), react(), sitemap()],
  image: {
    remotePatterns: [
      { protocol: 'https', hostname: 'github.com' },
      { protocol: 'https', hostname: '*.github.com' },
      { protocol: 'https', hostname: 'images.opencollective.com' },
      { protocol: 'https', hostname: 'hasdata.com' },
    ],
  },
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    remarkPlugins: [
      remarkDirective,
      remarkAdmonitions,
      remarkFixTypedocLinks,
      remarkLiveCode,
    ],
    rehypePlugins: [rehypeExternalLinks],
  },
});
```

## File: `website/package.json`
```json
{
  "name": "@cheerio/website",
  "description": "Documentation website for cheerio",
  "type": "module",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "astro": "astro",
    "build": "npm run build:api && astro build",
    "build:api": "typedoc",
    "dev": "astro dev",
    "preview": "astro preview",
    "start": "astro dev"
  },
  "dependencies": {
    "@astrojs/mdx": "^4.3.0",
    "@astrojs/react": "^5.0.1",
    "@astrojs/rss": "^4.0.17",
    "@astrojs/sitemap": "^3.7.1",
    "@codesandbox/sandpack-react": "^2.19.0",
    "@docsearch/css": "^4.6.0",
    "@docsearch/js": "^4.6.0",
    "@lucide/astro": "^1.6.0",
    "@tailwindcss/vite": "^4.2.2",
    "astro": "^5.17.2",
    "hastscript": "^9.0.1",
    "marked": "^17.0.5",
    "react": "^19.1.0",
    "react-dom": "^19.2.4",
    "remark-directive": "^4.0.0",
    "tailwindcss": "^4.2.2",
    "unist-util-visit": "^5.1.0"
  },
  "devDependencies": {
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.1.0",
    "typedoc": "^0.28.18",
    "typedoc-plugin-markdown": "^4.11.0",
    "typedoc-plugin-mdn-links": "^5.1.1",
    "typescript": "^5.9.3"
  },
  "engines": {
    "node": ">=20.18.1"
  }
}
```

## File: `website/sponsors.json`
```json
{
  "headliner": [
    {
      "createdAt": "2022-06-24",
      "name": "Github",
      "image": "https://github.com/github.png",
      "url": "https://github.com/",
      "type": "ORGANIZATION",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "manual",
      "tier": "headliner"
    },
    {
      "createdAt": "2018-05-02",
      "name": "AirBnB",
      "image": "https://github.com/airbnb.png",
      "url": "https://www.airbnb.com/",
      "type": "ORGANIZATION",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "manual",
      "tier": "headliner"
    },
    {
      "createdAt": "2026-01-21",
      "name": "HasData",
      "image": "https://hasdata.com/favicon.svg",
      "url": "https://hasdata.com",
      "type": "ORGANIZATION",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "manual",
      "tier": "headliner"
    },
    {
      "createdAt": "2026-01-28",
      "name": "context.dev",
      "image": "https://github.com/context-dot-dev.png",
      "url": "https://context.dev/",
      "type": "ORGANIZATION",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "manual",
      "tier": "headliner"
    }
  ],
  "sponsor": [
    {
      "createdAt": "2023-12-05T16:44:08.370Z",
      "name": "OnlineCasinosSpelen",
      "url": "https://onlinecasinosspelen.com",
      "image": "https://images.opencollective.com/onlinecasinosspelen/99ac6a2/logo.png",
      "type": "ORGANIZATION",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "opencollective",
      "tier": "sponsor"
    },
    {
      "createdAt": "2023-12-07T14:07:39.203Z",
      "name": "Nieuwe-Casinos.net",
      "url": "https://Nieuwe-Casinos.net",
      "image": "https://images.opencollective.com/nieuwecasinos/c67d423/logo.png",
      "type": "ORGANIZATION",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "opencollective",
      "tier": "sponsor"
    }
  ],
  "professional": [
    {
      "createdAt": "2022-01-26T15:21:25.562Z",
      "name": "Vasy Kafidoff",
      "url": "https://kafidoff.com",
      "image": "https://images.opencollective.com/kafidoff-vasy/d7ff85c/avatar.png",
      "type": "INDIVIDUAL",
      "monthlyDonation": 0,
      "totalDonations": 0,
      "source": "opencollective",
      "tier": "professional"
    }
  ],
  "backer": []
}
```

## File: `website/tsconfig.json`
```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },
    "jsx": "react-jsx",
    "jsxImportSource": "react",
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true
  },
  "include": ["src", ".astro", "*.json", "*.mjs"]
}
```

## File: `website/typedoc.json`
```json
{
  "$schema": "https://typedoc.org/schema.json",
  "entryPoints": ["../src/index.ts"],
  "tsconfig": "../tsconfig.typedoc.json",
  "readme": "none",
  "excludePrivate": true,
  "excludeExternals": true,
  "plugin": ["typedoc-plugin-markdown", "typedoc-plugin-mdn-links"],
  "out": "src/content/brain/knowledge/docs_legacy/api",
  "entryFileName": "index",
  "router": "kind",
  "publicPath": "/brain/knowledge/docs_legacy/api/",
  "fileExtension": ".md",
  "hidePageHeader": true,
  "hideBreadcrumbs": true,
  "useCodeBlocks": true,
  "expandObjects": true,
  "parametersFormat": "table",
  "enumMembersFormat": "table",
  "typeDeclarationFormat": "table",
  "indexFormat": "table",
  "sanitizeComments": true,
  "externalSymbolLinkMappings": {
    "domhandler": {
      "Document": "https://domhandler.js.org/classes/Document.html",
      "Element": "https://domhandler.js.org/classes/Element.html",
      "Node": "https://domhandler.js.org/classes/Node.html",
      "ChildNode": "https://domhandler.js.org/types/ChildNode.html",
      "ParentNode": "https://domhandler.js.org/types/ParentNode.html",
      "AnyNode": "https://domhandler.js.org/types/AnyNode.html"
    },
    "parse5": {
      "TreeAdapterTypeMap": "https://parse5.js.org/interfaces/parse5.TreeAdapterTypeMap.html",
      "TreeAdapter": "https://parse5.js.org/interfaces/parse5.TreeAdapter.html"
    }
  }
}
```

## File: `website/src/env.d.ts`
```typescript
/* eslint-disable @typescript-eslint/triple-slash-reference */
/* eslint-disable spaced-comment */
/* eslint-disable multiline-comment-style */
/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />
```

## File: `website/src/components/Features.astro`
```
---
import { CodeXml, Globe, Zap } from '@lucide/astro';

const features = [
  {
    title: 'Proven syntax',
    description:
      'Cheerio implements a subset of core jQuery. Cheerio removes all the DOM inconsistencies and browser cruft from the jQuery library, revealing its truly gorgeous API.',
    accent: 'from-rose-500/10 to-pink-500/10',
    border: 'hover:border-rose-500/30',
    iconColor: 'text-rose-500',
    Icon: CodeXml,
  },
  {
    title: 'Blazingly fast',
    description:
      'Cheerio works with a very simple, consistent DOM model. As a result parsing, manipulating, and rendering are incredibly efficient.',
    accent: 'from-amber-500/10 to-yellow-500/10',
    border: 'hover:border-amber-500/30',
    iconColor: 'text-amber-500',
    Icon: Zap,
  },
  {
    title: 'Incredibly flexible',
    description:
      'Cheerio can parse nearly any HTML or XML document. Cheerio works in both browser and server environments.',
    accent: 'from-blue-500/10 to-cyan-500/10',
    border: 'hover:border-blue-500/30',
    iconColor: 'text-blue-500',
    Icon: Globe,
  },
];
---

<section class="relative bg-white py-24 dark:bg-slate-900">
  <!-- Subtle top divider -->
  <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-slate-200 to-transparent dark:via-slate-800"></div>

  <div class="mx-auto max-w-6xl px-6">
    <div class="animate-fade-up mb-16 text-center">
      <p class="mb-3 text-sm font-semibold uppercase tracking-widest text-primary">Why Cheerio?</p>
      <h2 class="font-display text-4xl text-slate-900 md:text-5xl dark:text-white">
        Built for developers who ship
      </h2>
    </div>

    <div class="grid grid-cols-1 gap-8 md:grid-cols-3">
      {
        features.map((feature, i) => (
          <div
            class:list={[
              'animate-fade-up group relative rounded-2xl border border-slate-200 bg-gradient-to-br p-8 transition-all duration-300 dark:border-slate-800',
              feature.accent,
              feature.border,
              `animation-delay-${(i + 1) * 200}`,
            ]}
          >
            <div class:list={['mb-6 inline-flex rounded-xl bg-white p-3 shadow-sm dark:bg-slate-800', feature.iconColor]}>
              <feature.Icon class="h-8 w-8" stroke-width={1.5} />
            </div>
            <h3 class="mb-3 text-xl font-semibold text-slate-900 dark:text-white">
              {feature.title}
            </h3>
            <p class="leading-relaxed text-slate-600 dark:text-slate-400">
              {feature.description}
            </p>
          </div>
        ))
      }
    </div>
  </div>
</section>
```

## File: `website/src/components/Footer.astro`
```
---
import { Image } from 'astro:assets';
import logo from '@/assets/orange-c.svg';

const footerLinks = {
  Docs: [
    { label: 'Learn', href: '/brain/knowledge/docs_legacy/intro' },
    { label: 'API', href: '/brain/knowledge/docs_legacy/api' },
  ],
  Community: [
    {
      label: 'Stack Overflow',
      href: 'https://stackoverflow.com/questions/tagged/cheerio',
    },
    { label: 'GitHub', href: 'https://github.com/cheeriojs/cheerio' },
  ],
  More: [{ label: 'Blog', href: '/blog' }],
};

const currentYear = new Date().getFullYear();
---

<footer class="border-t border-slate-200 bg-slate-950 py-16 text-slate-400 dark:border-slate-800">
  <div class="mx-auto max-w-7xl px-6">
    <div class="grid grid-cols-2 gap-8 md:grid-cols-4">
      <!-- Brand column -->
      <div class="col-span-2 mb-4 md:col-span-1 md:mb-0">
        <a href="/" class="mb-4 flex items-center gap-2.5">
          <Image src={logo} alt="Cheerio" class="h-7 w-7" loading="lazy" />
          <span class="text-lg font-semibold text-white">Cheerio</span>
        </a>
        <p class="mt-3 max-w-xs text-sm leading-relaxed text-slate-500">
          The fast, flexible & elegant library for parsing and manipulating HTML and XML.
        </p>
      </div>

      {
        Object.entries(footerLinks).map(([title, links]) => (
          <div>
            <h3 class="mb-4 text-xs font-semibold uppercase tracking-widest text-slate-500">
              {title}
            </h3>
            <ul class="space-y-3">
              {links.map((link) => (
                <li>
                  <a
                    href={link.href}
                    class="text-sm transition-colors hover:text-primary-light"
                    target={link.href.startsWith('http') ? '_blank' : undefined}
                    rel={
                      link.href.startsWith('http')
                        ? 'noopener noreferrer'
                        : undefined
                    }
                  >
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))
      }
    </div>

    <div class="mt-12 flex flex-col items-center justify-between gap-4 border-t border-slate-800/60 pt-8 md:flex-row">
      <div class="text-xs text-slate-600">
        Copyright &copy; {currentYear} The Cheerio contributors
      </div>
      <div class="flex items-center gap-4">
        <a
          href="https://github.com/cheeriojs/cheerio"
          target="_blank"
          rel="noopener noreferrer"
          class="text-slate-600 transition-colors hover:text-slate-400"
          aria-label="GitHub"
        >
          <svg viewBox="0 0 24 24" class="h-5 w-5" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
        </a>
      </div>
    </div>
  </div>
</footer>
```

## File: `website/src/components/Hero.astro`
```
---

const title = 'cheerio';
const tagline =
  'The fast, flexible & elegant library for parsing and manipulating HTML and XML.';

// Fetch GitHub stars and npm downloads at build time
function formatCount(n: number): string {
  if (n >= 1_000_000)
    return `${(n / 1_000_000).toFixed(1).replace(/\.0$/, '')}M`;
  if (n >= 1000) return `${(n / 1000).toFixed(1).replace(/\.0$/, '')}k`;
  return n.toString();
}

let stars = '';
let downloads = '';

try {
  const [ghRes, npmRes] = await Promise.all([
    fetch('https://api.github.com/repos/cheeriojs/cheerio', {
      headers: {
        Accept: 'application/vnd.github.v3+json',
        'User-Agent': 'cheerio-website',
      },
    }),
    fetch('https://api.npmjs.org/downloads/point/last-month/cheerio'),
  ]);

  if (ghRes.ok) {
    const gh = await ghRes.json();
    stars = formatCount(gh.stargazers_count);
  }
  if (npmRes.ok) {
    const npm = await npmRes.json();
    downloads = formatCount(npm.downloads);
  }
} catch {
  // Silently fail — badges just won't render
}
---

<header class="relative overflow-hidden bg-slate-950 py-24 md:py-32 lg:py-40">
  <!-- Background gradient layers -->
  <div class="absolute inset-0 bg-gradient-to-br from-amber-950/40 via-slate-950 to-slate-900"></div>
  <div class="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_-20%,rgba(232,140,31,0.2),transparent)]"></div>
  <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-primary/40 to-transparent"></div>

  <!-- Grain overlay -->
  <div class="grain absolute inset-0 overflow-hidden opacity-50"></div>

  <!-- Floating decorative elements -->
  <div class="absolute left-[10%] top-[15%] h-64 w-64 rounded-full bg-primary/5 blur-3xl animate-float"></div>
  <div class="absolute right-[15%] bottom-[20%] h-48 w-48 rounded-full bg-primary/8 blur-3xl animate-float animation-delay-300"></div>

  <div class="relative z-10 mx-auto max-w-7xl px-6">
    <div class="grid items-center gap-12 lg:grid-cols-2 lg:gap-16">
      <!-- Left column: Text content -->
      <div class="text-center lg:text-left">
        <div class="animate-fade-up mb-6 flex flex-wrap items-center justify-center gap-3 lg:justify-start">
          {stars && (
            <a
              href="https://github.com/cheeriojs/cheerio/stargazers"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center gap-1.5 rounded-full border border-slate-700/60 bg-slate-800/60 px-3 py-1.5 text-sm text-slate-300 transition-colors hover:border-slate-600 hover:text-white"
            >
              <svg viewBox="0 0 24 24" class="h-4 w-4" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
              <span class="font-medium text-primary-light">{stars} stars</span>
            </a>
          )}
          {downloads && (
            <a
              href="https://www.npmjs.com/package/cheerio"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center gap-1.5 rounded-full border border-slate-700/60 bg-slate-800/60 px-3 py-1.5 text-sm text-slate-300 transition-colors hover:border-slate-600 hover:text-white"
            >
              <svg viewBox="0 0 256 256" class="h-4 w-4" fill="currentColor">
                <path d="M0 256V0h256v256z"/>
                <path d="M48 48h160v160h-32V80h-32v128H48z" fill="var(--color-slate-800, #1e293b)"/>
              </svg>
              <span class="font-medium text-primary-light">{downloads} downloads/month</span>
            </a>
          )}
        </div>

        <h1 class="animate-fade-up animation-delay-100 mb-6 font-display text-6xl tracking-tight text-white md:text-7xl lg:text-8xl">
          {title}
        </h1>

        <p class="animate-fade-up animation-delay-200 mb-10 max-w-xl text-lg leading-relaxed text-slate-400 md:text-xl lg:mx-0 mx-auto">
          {tagline}
        </p>

        <div class="animate-fade-up animation-delay-300 flex flex-col items-center gap-4 sm:flex-row lg:justify-start justify-center">
          <a
            href="/brain/knowledge/docs_legacy/intro"
            class="group relative inline-flex items-center gap-2 rounded-xl bg-primary px-8 py-3.5 font-semibold text-white transition-all duration-300 hover:bg-primary-dark hover:shadow-lg hover:shadow-primary/25"
          >
            Get Started
            <svg class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
            </svg>
          </a>
          <a
            href="https://github.com/cheeriojs/cheerio"
            target="_blank"
            rel="noopener noreferrer"
            class="inline-flex items-center gap-2 rounded-xl border border-slate-700 px-8 py-3.5 font-semibold text-slate-300 transition-all duration-300 hover:border-slate-500 hover:text-white hover:bg-slate-800/50"
          >
            <svg viewBox="0 0 24 24" class="h-5 w-5" fill="currentColor">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            View on GitHub
          </a>
        </div>

        <!-- Install snippet -->
        <div class="animate-fade-up animation-delay-400 mt-8 flex items-center justify-center lg:justify-start">
          <code class="flex items-center gap-3 rounded-lg border border-slate-800 bg-slate-900/80 px-5 py-2.5 font-mono text-sm text-slate-400">
            <span class="select-none text-primary/60">$</span>
            <span>npm install cheerio</span>
            <button
              id="copy-install"
              class="ml-2 text-slate-600 transition-colors hover:text-slate-300"
              aria-label="Copy to clipboard"
            >
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.666 3.888A2.25 2.25 0 0013.5 2.25h-3c-1.03 0-1.9.693-2.166 1.638m7.332 0c.055.194.084.4.084.612v0a.75.75 0 01-.75.75H9.75a.75.75 0 01-.75-.75v0c0-.212.03-.418.084-.612m7.332 0c.646.049 1.288.11 1.927.184 1.1.128 1.907 1.077 1.907 2.185V19.5a2.25 2.25 0 01-2.25 2.25H6.75A2.25 2.25 0 014.5 19.5V6.257c0-1.108.806-2.057 1.907-2.185a48.208 48.208 0 011.927-.184" />
              </svg>
            </button>
          </code>
        </div>
      </div>

      <!-- Right column: Code preview -->
      <div class="animate-slide-in-right animation-delay-400 hidden lg:block">
        <div class="relative">
          <!-- Glow behind the code block -->
          <div class="absolute -inset-4 rounded-2xl bg-gradient-to-br from-primary/10 via-transparent to-primary/5 blur-xl"></div>

          <div class="relative rounded-2xl border border-slate-800 bg-slate-900/90 shadow-2xl shadow-black/40 backdrop-blur-sm">
            <!-- Window chrome -->
            <div class="flex items-center gap-2 border-b border-slate-800 px-4 py-3">
              <div class="h-3 w-3 rounded-full bg-slate-700"></div>
              <div class="h-3 w-3 rounded-full bg-slate-700"></div>
              <div class="h-3 w-3 rounded-full bg-slate-700"></div>
              <span class="ml-3 text-xs text-slate-600 font-mono">example.js</span>
            </div>
            <!-- Code content -->
            <pre class="overflow-x-auto p-6 text-sm leading-relaxed"><code class="font-mono"><span class="text-purple-400">import</span> <span class="text-slate-300">*</span> <span class="text-purple-400">as</span> <span class="text-amber-300">cheerio</span> <span class="text-purple-400">from</span> <span class="text-green-400">'cheerio'</span><span class="text-slate-500">;</span>

<span class="text-purple-400">const</span> <span class="text-amber-300">$</span> <span class="text-slate-500">=</span> <span class="text-slate-300">cheerio.</span><span class="text-blue-400">load</span><span class="text-slate-500">(</span><span class="text-green-400">'&lt;h2 class="title"&gt;Hello world&lt;/h2&gt;'</span><span class="text-slate-500">);</span>

<span class="text-amber-300">$</span><span class="text-slate-500">(</span><span class="text-green-400">'h2.title'</span><span class="text-slate-500">).</span><span class="text-blue-400">text</span><span class="text-slate-500">(</span><span class="text-green-400">'Hello there!'</span><span class="text-slate-500">);</span>
<span class="text-amber-300">$</span><span class="text-slate-500">(</span><span class="text-green-400">'h2'</span><span class="text-slate-500">).</span><span class="text-blue-400">addClass</span><span class="text-slate-500">(</span><span class="text-green-400">'welcome'</span><span class="text-slate-500">);</span>

<span class="text-amber-300">$</span><span class="text-slate-500">.</span><span class="text-blue-400">html</span><span class="text-slate-500">();</span>
<span class="text-slate-600">{"//=> <html><head></head><body>"}</span>
<span class="text-slate-600">{"//=>   <h2 class=\"title welcome\">Hello there!</h2>"}</span>
<span class="text-slate-600">{"//=> </body></html>"}</span></code></pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>

<script>
  function initCopyInstall() {
    const copyButton = document.getElementById('copy-install');
    if (!copyButton) return;

    copyButton.onclick = () => {
      navigator.clipboard.writeText('npm install cheerio');
      const svg = copyButton.querySelector('svg');
      if (svg) {
        const originalPath = svg.innerHTML;
        svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />';
        setTimeout(() => { svg.innerHTML = originalPath; }, 2000);
      }
    };
  }

  initCopyInstall();
  if (!(window as any).__cheerio_copy_install_swap) {
    (window as any).__cheerio_copy_install_swap = true;
    document.addEventListener('astro:after-swap', initCopyInstall);
  }
</script>
```

## File: `website/src/components/LiveEditor.astro`
```
---
/**
 * Astro component that wraps LiveCode for use in markdown.
 * Usage in markdown: <LiveEditor>...</LiveEditor>
 */
import { LiveCode } from './live-code';
---

<div class="live-editor-wrapper">
  <LiveCode client:load code={await Astro.slots.render('default')} />
</div>
```

## File: `website/src/components/Navbar.astro`
```
---
import { Image } from 'astro:assets';
import logo from '@/assets/orange-c.svg';

const navItems = [
  {
    label: 'Learn',
    href: '/brain/knowledge/docs_legacy/intro',
    match: (p: string) => p.startsWith('/brain/knowledge/docs_legacy/') && !p.startsWith('/brain/knowledge/docs_legacy/api'),
  },
  {
    label: 'API',
    href: '/brain/knowledge/docs_legacy/api',
    match: (p: string) => p.startsWith('/brain/knowledge/docs_legacy/api'),
  },
  { label: 'Blog', href: '/blog', match: (p: string) => p.startsWith('/blog') },
];

const currentPath = Astro.url.pathname;
---

<nav class="sticky top-0 z-50 border-b border-slate-200/80 bg-white/80 backdrop-blur-xl dark:border-slate-800/80 dark:bg-slate-900/80">
  <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-3.5">
    <div class="flex items-center gap-10">
      <a href="/" class="group flex items-center gap-2.5">
        <Image src={logo} alt="Cheerio Logo" class="h-8 w-8 transition-transform duration-300 group-hover:rotate-[-8deg]" />
        <span class="text-lg font-semibold tracking-tight text-slate-900 dark:text-white">Cheerio</span>
      </a>

      <div class="hidden items-center gap-1 md:flex">
        {
          navItems.map((item) => (
            <a
              href={item.href}
              class:list={[
                'rounded-lg px-3.5 py-2 text-sm font-medium transition-colors',
                item.match(currentPath)
                  ? 'bg-primary/10 text-primary'
                  : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white',
              ]}
            >
              {item.label}
            </a>
          ))
        }
      </div>
    </div>

    <div class="flex items-center gap-3">
      <!-- DocSearch container -->
      <div id="docsearch"></div>

      <a
        href="https://github.com/cheeriojs/cheerio"
        target="_blank"
        rel="noopener noreferrer"
        class="rounded-lg p-2 text-slate-500 transition-colors hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white"
        aria-label="GitHub"
      >
        <svg viewBox="0 0 24 24" class="h-5 w-5" fill="currentColor">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
      </a>

      <!-- Mobile menu button -->
      <button
        type="button"
        class="inline-flex items-center justify-center rounded-lg p-2 text-slate-500 hover:bg-slate-100 hover:text-slate-900 md:hidden dark:text-slate-400 dark:hover:bg-slate-800"
        aria-label="Open menu"
        id="mobile-menu-button"
      >
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" />
        </svg>
      </button>
    </div>
  </div>

  <!-- Mobile menu -->
  <div id="mobile-menu" class="hidden border-t border-slate-200 bg-white md:hidden dark:border-slate-800 dark:bg-slate-900">
    <div class="space-y-1 px-4 pb-4 pt-2">
      {
        navItems.map((item) => (
          <a
            href={item.href}
            class:list={[
              'block rounded-lg px-3 py-2.5 text-sm font-medium',
              item.match(currentPath)
                ? 'bg-primary/10 text-primary'
                : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white',
            ]}
          >
            {item.label}
          </a>
        ))
      }
    </div>
  </div>
</nav>

<script>
  // Mobile menu toggle — re-bind after each View Transition navigation.
  // Use a global guard to ensure the swap listener is registered only once,
  // avoiding duplicate handlers when the script re-executes on navigations.
  function initMobileMenu() {
    const menuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuButton && mobileMenu) {
      // Clone and replace to remove any previously attached listeners
      const freshButton = menuButton.cloneNode(true) as HTMLElement;
      menuButton.replaceWith(freshButton);
      freshButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
      });
    }
  }

  initMobileMenu();
  if (!(window as any).__cheerio_mobile_menu_swap) {
    (window as any).__cheerio_mobile_menu_swap = true;
    document.addEventListener('astro:after-swap', initMobileMenu);
  }
</script>

<script>
  // Initialize DocSearch — re-run after each View Transition navigation.
  // Use a global guard to ensure the swap listener is registered only once.
  import docsearch from '@docsearch/js';
  import '@docsearch/css';

  function initDocSearch() {
    const container = document.getElementById('docsearch');
    if (container) {
      // Clear any previous instance
      container.innerHTML = '';
      docsearch({
        appId: 'NRR2XU4QSP',
        apiKey: '9d30ee79d65ccc63b95e693124e05405',
        indexName: 'crawler_cheerio',
        container: '#docsearch',
      });
    }
  }

  initDocSearch();
  if (!(window as any).__cheerio_docsearch_swap) {
    (window as any).__cheerio_docsearch_swap = true;
    document.addEventListener('astro:after-swap', initDocSearch);
  }
</script>
```

## File: `website/src/components/Sidebar.astro`
```
---
import { getCollection } from 'astro:content';

interface SidebarItem {
  label: string;
  href: string;
}

interface SidebarSection {
  title: string;
  items: SidebarItem[];
}

interface ApiGroup {
  title: string;
  items: SidebarItem[];
}

interface Props {
  currentPath: string;
}

const { currentPath } = Astro.props;

const sidebar: SidebarSection[] = [
  {
    title: 'Getting Started',
    items: [{ label: 'Introduction', href: '/brain/knowledge/docs_legacy/intro' }],
  },
  {
    title: 'Basics',
    items: [
      { label: 'Loading Documents', href: '/brain/knowledge/docs_legacy/basics/loading' },
      { label: 'Selecting Elements', href: '/brain/knowledge/docs_legacy/basics/selecting' },
      { label: 'Traversing the DOM', href: '/brain/knowledge/docs_legacy/basics/traversing' },
      { label: 'Manipulating Elements', href: '/brain/knowledge/docs_legacy/basics/manipulation' },
    ],
  },
  {
    title: 'Advanced',
    items: [
      {
        label: 'Configuring Cheerio',
        href: '/brain/knowledge/docs_legacy/advanced/configuring-cheerio',
      },
      { label: 'Extending Cheerio', href: '/brain/knowledge/docs_legacy/advanced/extending-cheerio' },
      { label: 'Extracting Data', href: '/brain/knowledge/docs_legacy/advanced/extract' },
    ],
  },
];

// Dynamically build API sub-pages from the content collection
const allDocs = await getCollection('docs');
const apiDocs = allDocs.filter(
  (doc) =>
    doc.id.startsWith('api/') &&
    doc.id !== 'api/index.md' &&
    doc.id !== 'api/index',
);

// Group by kind (directory name)
const kindLabels: Record<string, string> = {
  classes: 'Classes',
  interfaces: 'Interfaces',
  functions: 'Functions',
  types: 'Types',
  variables: 'Variables',
};
const kindOrder = ['classes', 'variables', 'functions', 'interfaces', 'types'];

const apiGroups: ApiGroup[] = [];
const groupedByKind = new Map<string, SidebarItem[]>();

for (const doc of apiDocs) {
  // id looks like "api/classes/Cheerio.md" or "api/functions/contains"
  const parts = doc.id
    .replace(/^api\//, '')
    .replace(/\.mdx?$/, '')
    .split('/');
  if (parts.length !== 2) continue;
  const [kind, name] = parts;
  if (!groupedByKind.has(kind)) groupedByKind.set(kind, []);
  groupedByKind.get(kind)!.push({
    label: name,
    href: `/brain/knowledge/docs_legacy/api/${kind}/${name}`,
  });
}

// Sort items within each group alphabetically
for (const items of groupedByKind.values()) {
  items.sort((a, b) => a.label.localeCompare(b.label));
}

// Build ordered groups
for (const kind of kindOrder) {
  const items = groupedByKind.get(kind);
  if (items && items.length > 0) {
    apiGroups.push({ title: kindLabels[kind] || kind, items });
  }
}

const isApiPage = currentPath.startsWith('/brain/knowledge/docs_legacy/api');
const normalizedPath = currentPath.replace(/\/$/, '');

export { sidebar };
export type { SidebarItem, SidebarSection };
---

{/* ── Desktop sidebar ── */}
<aside
  class="hidden w-64 shrink-0 border-r border-slate-200 dark:border-slate-700 lg:block"
>
  <nav class="sticky top-14 h-[calc(100vh-3.5rem)] overflow-y-auto px-6 py-8">
    {
      sidebar.map((section) => (
        <div class="mb-8">
          <h3 class="mb-3 text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
            {section.title}
          </h3>
          <ul class="space-y-1">
            {section.items.map((item) => (
              <li>
                <a
                  href={item.href}
                  class:list={[
                    'block rounded-lg px-3 py-2 text-sm transition-all duration-150',
                    normalizedPath === item.href
                      ? 'bg-primary/10 font-semibold text-primary border-l-2 border-primary'
                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-slate-100',
                  ]}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      ))
    }

    {/* Reference / API section */}
    <div class="mb-8">
      <h3 class="mb-3 text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
        Reference
      </h3>
      <ul class="space-y-1">
        <li>
          <a
            href="/brain/knowledge/docs_legacy/api"
            class:list={[
              'block rounded-lg px-3 py-2 text-sm transition-all duration-150',
              normalizedPath === '/brain/knowledge/docs_legacy/api'
                ? 'bg-primary/10 font-semibold text-primary border-l-2 border-primary'
                : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-slate-100',
            ]}
          >
            API Documentation
          </a>
        </li>
      </ul>
      {apiGroups.map((group) => (
        <details class="group/api mt-2" open={isApiPage}>
          <summary class="flex cursor-pointer items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-semibold uppercase tracking-wider text-slate-400 hover:text-slate-600 dark:text-slate-500 dark:hover:text-slate-300">
            <svg class="h-3 w-3 shrink-0 transition-transform group-open/api:rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
            </svg>
            {group.title}
          </summary>
          <ul class="mt-1 space-y-0.5 pl-2">
            {group.items.map((item) => (
              <li>
                <a
                  href={item.href}
                  class:list={[
                    'block rounded-lg px-3 py-1.5 text-sm transition-all duration-150',
                    normalizedPath === item.href
                      ? 'bg-primary/10 font-semibold text-primary border-l-2 border-primary'
                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-slate-100',
                  ]}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </details>
      ))}
    </div>
  </nav>
</aside>

{/* ── Mobile sidebar drawer ── */}
<div
  id="sidebar-overlay"
  class="fixed inset-0 z-40 hidden bg-black/50 backdrop-blur-sm lg:hidden"
>
</div>
<aside
  id="sidebar-drawer"
  class="fixed left-0 top-0 z-50 hidden h-full w-72 -translate-x-full transform bg-white shadow-2xl transition-transform duration-300 ease-in-out lg:hidden dark:bg-slate-900"
>
  <div class="flex items-center justify-between border-b border-slate-200 px-6 py-4 dark:border-slate-700">
    <span class="text-sm font-semibold uppercase tracking-wider text-slate-400 dark:text-slate-500">Documentation</span>
    <button
      type="button"
      id="sidebar-close"
      class="rounded-lg p-1.5 text-slate-400 hover:bg-slate-100 hover:text-slate-600 dark:hover:bg-slate-800 dark:hover:text-slate-300"
      aria-label="Close sidebar"
    >
      <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>
  </div>
  <nav class="overflow-y-auto px-6 py-6" style="max-height: calc(100% - 57px);">
    {
      sidebar.map((section) => (
        <div class="mb-8">
          <h3 class="mb-3 text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
            {section.title}
          </h3>
          <ul class="space-y-1">
            {section.items.map((item) => (
              <li>
                <a
                  href={item.href}
                  class:list={[
                    'block rounded-lg px-3 py-2 text-sm transition-all duration-150',
                    normalizedPath === item.href
                      ? 'bg-primary/10 font-semibold text-primary border-l-2 border-primary'
                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-slate-100',
                  ]}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      ))
    }

    {/* Reference / API section */}
    <div class="mb-8">
      <h3 class="mb-3 text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
        Reference
      </h3>
      <ul class="space-y-1">
        <li>
          <a
            href="/brain/knowledge/docs_legacy/api"
            class:list={[
              'block rounded-lg px-3 py-2 text-sm transition-all duration-150',
              normalizedPath === '/brain/knowledge/docs_legacy/api'
                ? 'bg-primary/10 font-semibold text-primary border-l-2 border-primary'
                : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-slate-100',
            ]}
          >
            API Documentation
          </a>
        </li>
      </ul>
      {apiGroups.map((group) => (
        <details class="group/api mt-2" open={isApiPage}>
          <summary class="flex cursor-pointer items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-semibold uppercase tracking-wider text-slate-400 hover:text-slate-600 dark:text-slate-500 dark:hover:text-slate-300">
            <svg class="h-3 w-3 shrink-0 transition-transform group-open/api:rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
            </svg>
            {group.title}
          </summary>
          <ul class="mt-1 space-y-0.5 pl-2">
            {group.items.map((item) => (
              <li>
                <a
                  href={item.href}
                  class:list={[
                    'block rounded-lg px-3 py-1.5 text-sm transition-all duration-150',
                    normalizedPath === item.href
                      ? 'bg-primary/10 font-semibold text-primary border-l-2 border-primary'
                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-slate-100',
                  ]}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </details>
      ))}
    </div>
  </nav>
</aside>

<script>
  // Sidebar drawer — re-bind after each View Transition navigation.
  // Use a global guard to ensure the swap listener is registered only once.
  // Use .onclick assignment instead of addEventListener to de-dupe handlers.
  function initSidebarDrawer() {
    const overlay = document.getElementById('sidebar-overlay');
    const drawer = document.getElementById('sidebar-drawer');
    const closeBtn = document.getElementById('sidebar-close');
    const openBtn = document.getElementById('sidebar-open');

    function openDrawer() {
      if (!overlay || !drawer) return;
      overlay.classList.remove('hidden');
      drawer.classList.remove('hidden');
      // Force reflow before adding transform
      drawer.offsetHeight;
      drawer.classList.remove('-translate-x-full');
      drawer.classList.add('translate-x-0');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      if (!overlay || !drawer) return;
      drawer.classList.remove('translate-x-0');
      drawer.classList.add('-translate-x-full');
      document.body.style.overflow = '';
      // Wait for transition to finish before hiding
      setTimeout(() => {
        overlay.classList.add('hidden');
        drawer.classList.add('hidden');
      }, 300);
    }

    // Use .onclick to replace (not accumulate) handlers on each init
    if (openBtn) openBtn.onclick = openDrawer;
    if (closeBtn) closeBtn.onclick = closeDrawer;
    if (overlay) overlay.onclick = closeDrawer;
  }

  initSidebarDrawer();
  if (!(window as any).__cheerio_sidebar_swap) {
    (window as any).__cheerio_sidebar_swap = true;
    document.addEventListener('astro:after-swap', initSidebarDrawer);
  }
</script>
```

## File: `website/src/components/Sponsors.astro`
```
---
import { Image } from 'astro:assets';
import { Heart } from '@lucide/astro';
import sponsorsData from '../../sponsors.json';

interface Sponsor {
  name: string;
  image: string;
  url: string;
}

const headliners = sponsorsData.headliner as Sponsor[];
---

<section class="relative overflow-hidden bg-slate-50 py-20 dark:bg-slate-800/50">
  <!-- Decorative background -->
  <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(232,140,31,0.05),transparent_70%)]"></div>

  <div class="relative mx-auto max-w-5xl px-6">
    <div class="animate-fade-up mb-12 text-center">
      <p class="mb-3 text-sm font-semibold uppercase tracking-widest text-primary">Trusted by the best</p>
      <h2 class="font-display text-4xl text-slate-900 dark:text-white">
        Supported and Backed by
      </h2>
    </div>

    <div class="animate-fade-up animation-delay-200 flex flex-wrap items-center justify-center gap-6">
      {
        headliners.map((sponsor) => (
          <a
            href={sponsor.url}
            target="_blank"
            rel="noopener noreferrer"
            class="group flex items-center gap-3 rounded-xl border border-slate-200 bg-white px-6 py-4 transition-all duration-300 hover:border-primary/30 hover:shadow-lg hover:shadow-primary/5 dark:border-slate-700 dark:bg-slate-800 dark:hover:border-primary/40"
          >
            {sponsor.image.endsWith('.svg') ? (
              <img
                src={sponsor.image}
                alt={`${sponsor.name} logo`}
                class="h-10 w-10 rounded-lg"
                loading="lazy"
              />
            ) : (
              <Image
                src={sponsor.image}
                alt={`${sponsor.name} logo`}
                width={40}
                height={40}
                class="h-10 w-10 rounded-lg"
                loading="lazy"
              />
            )}
            <span class="font-medium text-slate-700 transition-colors group-hover:text-slate-900 dark:text-slate-300 dark:group-hover:text-white">
              {sponsor.name}
            </span>
          </a>
        ))
      }
    </div>

    <div class="animate-fade-up animation-delay-400 mt-10 text-center">
      <a
        href="https://github.com/sponsors/cheeriojs"
        target="_blank"
        rel="noopener noreferrer"
        class="inline-flex items-center gap-2 rounded-full border border-primary/30 bg-primary/5 px-6 py-2.5 text-sm font-medium text-primary transition-all duration-300 hover:bg-primary/10 hover:border-primary/50 dark:text-primary-light"
      >
        <Heart class="h-5 w-5" fill="currentColor" stroke-width={0} />
        Become a sponsor
      </a>
    </div>
  </div>
</section>
```

## File: `website/src/components/TableOfContents.astro`
```
---
interface Props {
  headings: Array<{
    depth: number;
    slug: string;
    text: string;
  }>;
}

const { headings } = Astro.props;

// Filter to only h2 and h3 headings
const toc = headings.filter((h) => h.depth >= 2 && h.depth <= 3);
---

{toc.length > 0 && (
  <nav class="hidden xl:block w-56 shrink-0 pl-6 pt-4">
    <div class="sticky top-20">
      <h4 class="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-400 dark:text-slate-500">
        On this page
      </h4>
      <ul class="space-y-2 text-xs">
        {toc.map((heading) => (
          <li>
            <a
              href={`#${heading.slug}`}
              class:list={[
                'block text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-200 transition-colors leading-snug',
                heading.depth === 2 ? 'font-medium text-slate-600 dark:text-slate-300' : 'pl-3 text-slate-500',
              ]}
            >
              {heading.text}
            </a>
          </li>
        ))}
      </ul>
    </div>
  </nav>
)}
```

## File: `website/src/components/Testimonials.astro`
```
---
import { Image } from 'astro:assets';

interface Tweet {
  id: string;
  name: string;
  user: string;
  github: string;
  tweet: string;
  tagline: string;
  url?: string;
}

const tweets: Tweet[] = [
  {
    id: '628016191928446977',
    name: 'Axel Rauschmayer',
    user: 'rauschma',
    github: 'rauschma',
    tweet:
      "For transforming HTML via Node.js scripts, @mattmueller's cheerio works really well.",
    tagline: "Author of 'Exploring JavaScript', educator at 2ality.com",
  },
  {
    id: '1616150822932385792',
    name: 'Valeri Karpov',
    user: 'code_barbarian',
    github: 'vkarpov15',
    tweet:
      'Cheerio is a weird npm module: most devs have never heard of it, but I rarely build an app without it. So much utility for quick and easy HTML transformations.',
    tagline: 'Creator of Mongoose ODM',
  },
  {
    id: '1186972238190403587',
    name: 'Matthew Phillips',
    user: 'matthewcp',
    github: 'matthewp',
    tweet:
      'Cheerio is (still) such a useful tool for manipulating HTML. Shout to @MattMueller for saving me an untold amount of time over the years.',
    tagline: 'Co-Creator of Astro',
  },
  {
    id: '1403139379757977602',
    name: 'Mike Pennisi',
    user: 'JugglinMike',
    github: 'jugglinmike',
    tweet:
      "Thank you @fb55 for tirelessly pushing Cheerio to version 1.0. That library helps so many developers expand their horizons beyond the browser, and you've been making it possible for a decade!",
    tagline: 'Open source developer at Bocoup',
  },
  {
    id: '264033999272439809',
    name: 'Thomas Steiner',
    user: 'tomayac',
    github: 'tomayac',
    tweet:
      "npm install cheerio. That's the #jQuery DOM API for #nodeJS essentially. Thanks, @MattMueller",
    tagline: 'Developer Relations Engineer at Google Chrome',
    url: 'https://tomayac.com/tweets/264033999272439809/',
  },
  {
    id: '1545481085865320449',
    name: 'Thomas Boutell',
    user: 'boutell',
    github: 'boutell',
    tweet:
      'If you\'re great at jQuery, you\'re going to be really popular on server-side projects that need web scraping or HTML transformation. "npm install cheerio" ahoy!',
    tagline: 'Co-creator of the PNG format, CEO of ApostropheCMS',
  },
];

// Split tweets into 3 columns for masonry-like layout
const columns: Tweet[][] = [[], [], []];
tweets.forEach((tweet, i) => {
  columns[i % 3].push(tweet);
});
---

<section class="relative bg-white py-24 dark:bg-slate-900">
  <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-slate-200 to-transparent dark:via-slate-800"></div>

  <div class="mx-auto max-w-6xl px-6">
    <div class="animate-fade-up mb-16 text-center">
      <p class="mb-3 text-sm font-semibold uppercase tracking-widest text-primary">Community</p>
      <h2 class="font-display text-4xl text-slate-900 md:text-5xl dark:text-white">
        What developers are saying
      </h2>
    </div>

    <!-- Masonry-like 3-column layout -->
    <div class="hidden gap-6 md:grid md:grid-cols-3">
      {
        columns.map((column, colIndex) => (
          <div class="flex flex-col gap-6">
            {column.map((tweet, i) => (
              <a
                href={tweet.url ?? `https://twitter.com/${tweet.user}/status/${tweet.id}`}
                target="_blank"
                rel="noopener noreferrer"
                class="animate-fade-up group block rounded-2xl border border-slate-200 bg-slate-50/50 p-6 transition-all duration-300 hover:border-primary/20 hover:shadow-lg hover:shadow-primary/5 dark:border-slate-800 dark:bg-slate-800/50 dark:hover:border-primary/30"
                style={`animation-delay: ${(colIndex * 100) + (i * 200)}ms`}
              >
                <div class="mb-4 flex items-start gap-3">
                  <Image
                    src={`https://github.com/${tweet.github}.png?s=88`}
                    alt={`${tweet.name}'s avatar`}
                    width={44}
                    height={44}
                    class="mt-0.5 h-11 w-11 shrink-0 rounded-full ring-2 ring-slate-100 dark:ring-slate-700"
                    loading="lazy"
                  />
                  <div class="min-w-0 flex-1">
                    <div class="font-semibold text-slate-900 dark:text-white">
                      {tweet.name}
                    </div>
                    <div class="text-sm text-slate-500 dark:text-slate-400">
                      {tweet.tagline}
                    </div>
                  </div>
                </div>
                <p class="leading-relaxed text-slate-700 dark:text-slate-300">
                  {tweet.tweet}
                </p>
              </a>
            ))}
          </div>
        ))
      }
    </div>

    <!-- Mobile: single column -->
    <div class="flex flex-col gap-6 md:hidden">
      {
        tweets.map((tweet, i) => (
          <a
            href={tweet.url ?? `https://twitter.com/${tweet.user}/status/${tweet.id}`}
            target="_blank"
            rel="noopener noreferrer"
            class="animate-fade-up group block rounded-2xl border border-slate-200 bg-slate-50/50 p-6 transition-all duration-300 hover:border-primary/20 hover:shadow-lg dark:border-slate-800 dark:bg-slate-800/50"
            style={`animation-delay: ${i * 100}ms`}
          >
            <div class="mb-4 flex items-start gap-3">
              <Image
                src={`https://github.com/${tweet.github}.png?s=88`}
                alt={`${tweet.name}'s avatar`}
                width={44}
                height={44}
                class="mt-0.5 h-11 w-11 shrink-0 rounded-full ring-2 ring-slate-100 dark:ring-slate-700"
                loading="lazy"
              />
              <div class="min-w-0 flex-1">
                <div class="font-semibold text-slate-900 dark:text-white">
                  {tweet.name}
                </div>
                <div class="text-sm text-slate-500 dark:text-slate-400">
                  {tweet.tagline}
                </div>
              </div>
            </div>
            <p class="leading-relaxed text-slate-700 dark:text-slate-300">
              {tweet.tweet}
            </p>
          </a>
        ))
      }
    </div>
  </div>
</section>
```

## File: `website/src/components/live-code.tsx`
```tsx
import {
  SandpackCodeEditor,
  SandpackConsole,
  SandpackProvider,
  useSandpack,
} from '@codesandbox/sandpack-react';
import { useCallback } from 'react';

interface LiveCodeProps {
  code: string;
}

function ResetButton() {
  const { sandpack } = useSandpack();

  const handleReset = useCallback(() => sandpack.resetAllFiles(), [sandpack]);

  return (
    <button
      type="button"
      onClick={handleReset}
      className="px-2 py-1 text-xs font-medium text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-slate-700 rounded transition-colors"
      title="Reset code and re-run"
    >
      Reset
    </button>
  );
}

function RunButton() {
  const { sandpack } = useSandpack();

  const handleRun = () => {
    const { code } = sandpack.files['/index.js'];
    sandpack.updateFile('/index.js', code, true);
  };

  return (
    <button
      type="button"
      onClick={handleRun}
      className="px-2 py-1 text-xs font-medium text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-200 dark:hover:bg-slate-700 rounded transition-colors"
      title="Run code"
    >
      Run
    </button>
  );
}

function Toolbar() {
  return (
    <div className="flex items-center justify-between px-3 py-2 bg-slate-100 dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700">
      <span className="text-xs font-medium text-slate-600 dark:text-slate-400 uppercase tracking-wide">
        Live Editor
      </span>
      <div className="flex items-center gap-2">
        <RunButton />
        <ResetButton />
      </div>
    </div>
  );
}

export function LiveCode({ code }: LiveCodeProps) {
  // Wrap user code to run immediately and output via console.log
  const wrappedCode = `import * as cheerio from 'cheerio';

${code}
`;

  return (
    <div className="my-4 overflow-hidden rounded-lg border border-slate-200 dark:border-slate-700 not-prose">
      <SandpackProvider
        template="vanilla"
        theme="auto"
        files={{
          '/index.js': wrappedCode,
        }}
        customSetup={{
          dependencies: {
            cheerio: 'latest',
          },
        }}
      >
        <Toolbar />
        <SandpackCodeEditor showLineNumbers style={{ height: '200px' }} />
        <SandpackConsole
          style={{ height: '150px' }}
          standalone
          showHeader
          showResetConsoleButton
        />
      </SandpackProvider>
    </div>
  );
}
```

## File: `website/src/content/config.ts`
```typescript
import { defineCollection, z } from 'astro:content';

const docs = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string().optional(),
    description: z.string().optional(),
    sidebar_position: z.number().optional(),
    sidebar_label: z.string().optional(),
  }),
});

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    slug: z.string().optional(),
    authors: z.union([z.string(), z.array(z.string())]).optional(),
    tags: z.array(z.string()).optional(),
    date: z.date().optional(),
  }),
});

export const collections = { docs, blog };
```

## File: `website/src/content/blog/2023-02-13-new-website.md`
```markdown
---
slug: new-website
title: New Website, Who Dis?
authors: fb55
tags: [website, intro]
---

Cheerio has a new website, and it's looking pretty good! This has been in the
works for a while, and we're excited to finally share it with you. Let's walk
through all that's new.

:::note

Cheerio's website is still a work-in-progress, and covers Cheerio's next release
that isn't available yet.
[We would love your help in making this website better!](https://github.com/cheeriojs/cheerio/discussions/3002)

:::

<!--truncate-->

## Guides

The Cheerio website now features a set of guides, helping you get started with
the project. Even if you've used the project for a while, you might still learn
something new!

Most of these guides were written with the help of
[ChatGPT](https://chat.openai.com/), which made it possible to generate
high-quality content in a reasonable amount of time. While contents have been
checked for accuracy, we are happy to accept pull requests to improve the
guides.

Get started with the [intro guide](/brain/knowledge/docs_legacy/intro).

## API Docs

API docs, the old focus of the website, have been moved to a subdirectory. They
are available at [brain/knowledge/docs_legacy/api](/brain/knowledge/docs_legacy/api).

## Blog

We're also starting a blog, where we'll share updates about the project. Feel
free to subscribe [to the RSS feed](/blog/rss.xml)!
```

## File: `website/src/content/blog/2024-08-07-version-1.md`
```markdown
---
slug: cheerio-1.0
title: Cheerio 1.0 Released, Batteries Included 🔋
authors: fb55
tags: [release, announcement]
---

Cheerio 1.0 is out! After 12 release candidates and just a short seven years
after the initial 1.0 release candidate, it is finally time to call Cheerio 1.0
complete. The theme for this release is "batteries included", with common use
cases now supported out of the box.

So grab a pair of double-As, and read below for what's new, what's changed, and
how to upgrade!

<!--truncate-->

## New Website and Documentation

Since the last release, we've published a new website and documentation for
Cheerio. The new site features detailed guides and API documentation to get the
most from Cheerio. Check it out at [cheerio.js.org](https://cheerio.js.org/).

## A new way to load documents

Loading documents into Cheerio has been revamped. Cheerio now supports multiple
loading methods, each tailored to different use cases:

- `load`: The classic method for parsing HTML or XML strings.
- `loadBuffer`: Works with binary data, automatically detecting the document
  encoding.
- `stringStream` and `decodeStream`: Parse HTML directly from streams.
- `fromURL`: Fetch and parse HTML from a URL in one go.

Dive deeper into these methods in the [Loading Documents](/brain/knowledge/docs_legacy/basics/loading)
tutorial.

## Simplified Data Extraction

The new `extract` method allows you to extract data from an HTML document and
store it in an object. To fetch the latest release of Cheerio from GitHub and
extract the release date and the release notes from the release page is now as
simple as:

```ts
import * as cheerio from 'cheerio';

const $ = await cheerio.fromURL(
  'https://github.com/cheeriojs/cheerio/releases',
);
const data = $.extract({
  releases: [
    {
      // First, we select individual release sections.
      selector: 'section',
      // Then, we extract the release date, name, and notes from each section.
      value: {
        // Selectors are executed within the context of the selected element.
        name: 'h2',
        date: {
          selector: 'relative-time',
          // The actual release date is stored in the `datetime` attribute.
          value: 'datetime',
        },
        notes: {
          selector: '.markdown-body',
          // We are looking for the HTML content of the element.
          value: 'innerHTML',
        },
      },
    },
  ],
});
```

Read more about all of the available options in the
[Extracting Data](/brain/knowledge/docs_legacy/advanced/extract) guide.

## Breaking Changes and Upgrade Guide

Cheerio 1.0 introduces several breaking changes, most notably:

- The minimum NodeJS version is now 18.17 or higher.
- Import paths were simplified. For example, use `cheerio/slim` instead of
  `cheerio/lib/slim`.
- The deprecated default Cheerio instance and static methods were removed.

  Before, it was possible to write code like this:

  ```ts
  import cheerio, { html } from 'cheerio';

  html(cheerio('<test></test>')); // ~ '<test></test>' -- NO LONGER WORKS
  ```

  Make sure to always load documents first:

  ```ts
  import * as cheerio from 'cheerio';

  cheerio.load('<test></test>').html();
  ```

- htmlparser2 options now reside exclusively under the `xml` key:

  ```ts
  const $ = cheerio.load('<html>', {
    xml: {
      withStartIndices: true,
    },
  });
  ```

- Node types previously re-exported by Cheerio must now be imported directly
  from [`domhandler`](https://github.com/fb55/domhandler).

For a comprehensive list of changes, please consult
[the changelog](https://github.com/cheeriojs/cheerio/releases).

## Upgrading to Cheerio 1.0

To upgrade to Cheerio 1.0, just run:

```bash npm2yarn
npm install cheerio@latest
```

## Get Involved

Explore the new features and let us know what you think! Encounter an issue?
Report it on our
[GitHub issue tracker](https://github.com/cheeriojs/cheerio/issues). Have an
idea for an improvement? Pull requests welcome :)

## Thank You

Thanks to [@jugglinmike](https://github.com/jugglinmike) for kick-starting
Cheerio 1.0, and to all the contributors who have helped shape this release. We
couldn't have done it without you.

Thanks to our
[sponsors and backers](https://github.com/cheeriojs/cheerio?sponsor) for
supporting Cheerio's development. If you use Cheerio at work, consider asking
your company to support us!

And finally, thank you for using Cheerio 🙇🙇‍♀️
```

## File: `website/src/content/brain/knowledge/docs_legacy/intro.md`
```markdown
---
sidebar_position: 1
sidebar_label: Introduction
---

# Welcome to Cheerio!

Let's get a quick overview of **Cheerio in less than 5 minutes**.

## Getting Started

Let's install Cheerio and its dependencies.

### Setting up Node.js

To install Cheerio, you will need to have Node.js installed on your system.

- Download the latest version of [Node.js](https://nodejs.org/en/download/):
  - When installing Node.js, you are recommended to check all checkboxes related
    to dependencies.

### Installing Cheerio

Once you have set up Node.js, you can use the following command to install
Cheerio:

```bash npm2yarn
npm install cheerio
```

### Importing Cheerio

Once Cheerio is installed, you can import it into your JavaScript code using the
`import` statement:

```js
import * as cheerio from 'cheerio';
```

If you are on an older environment (or prefer using CommonJS), you can use the
`require` function:

```js
const cheerio = require('cheerio');
```

## Using Cheerio

After importing Cheerio, you can start using it to manipulate and scrape web
page data.

### Loading a Document

The easiest way of loading HTML is to use the `load` function:

```js
const $ = cheerio.load('<h2 class="title">Hello world</h2>');
```

This will load the HTML string into Cheerio and return a `Cheerio` object. You
can then use this object to traverse the DOM and manipulate the data.

Learn more about [loading documents](/brain/knowledge/docs_legacy/basics/loading).

:::note

**Cheerio is not a web browser.** Cheerio parses markup and provides an API for
traversing/manipulating the resulting data structure. It does not interpret the
result as a web browser does. Specifically, it does _not_ produce a visual
rendering, apply CSS, load external resources, or execute JavaScript which is
common for a SPA (single page application). This makes Cheerio **much, much
faster than other solutions**. If your use case requires any of this
functionality, you should consider browser automation software like
[Puppeteer](https://github.com/puppeteer/puppeteer) and
[Playwright](https://github.com/microsoft/playwright) or DOM emulation projects
like [JSDom](https://github.com/jsdom/jsdom).

:::

### Selecting Elements

Once you have loaded a document, you can use the returned function to select
elements from the document.

Here, we will select the `h2` element with the class `title`, and then get the
text from it:

```js
$('h2.title').text(); // "Hello world"
```

Learn more about [selecting elements](/brain/knowledge/docs_legacy/basics/selecting).

### Traversing the DOM

The `$` function returns a `Cheerio` object, which is similar to an array of DOM
elements. It is possible to use this object as a starting point to further
traverse the DOM. For example, you can use the `find` function to select
elements within the selected elements:

```js
$('h2.title').find('.subtitle').text();
```

There are many other functions that can be used to traverse the DOM. Learn more
about [traversing the DOM](/brain/knowledge/docs_legacy/basics/traversing).

### Manipulating Elements

Once you have selected an element, you can use the `Cheerio` object to
manipulate the element.

Here, we will select the `h2` element with the class `title`, and then change
the text inside it. We also add a new `h3` element to the document:

```js
$('h2.title').text('Hello there!');

$('h2').after('<h3>How are you?</h3>');
```

Learn more about [manipulating elements](/brain/knowledge/docs_legacy/basics/manipulation).
```

## File: `website/src/content/brain/knowledge/docs_legacy/advanced/configuring-cheerio.md`
```markdown
---
sidebar_position: 2
description: Configure Cheerio to work with different documents.
---

# Configuring Cheerio

In this guide, we'll cover how to configure Cheerio to work with different types
of documents, and how to use and configure the different parsers that ship with
the library.

## Parsing HTML with parse5

By default, Cheerio uses the [`parse5`](https://parse5.js.org/) parser for HTML
documents. `parse5` is an excellent project that rigorously conforms to the HTML
standard. However, if you need to modify parsing options for HTML input, you may
pass an extra object to `.load()`:

```js
const cheerio = require('cheerio');
const $ = cheerio.load('<noscript><h1>Nested Tag!</h1></noscript>', {
  scriptingEnabled: false,
});
```

For example, if you want the contents of `<noscript>` tags to be parsed as HTML,
you can set the `scriptingEnabled` option to false.

For a full list of options and their effects, have a look at
[the API documentation](/brain/knowledge/docs_legacy/api/interfaces/CheerioOptions).

### Fragment Mode

By default, `parse5` treats documents it receives as full HTML documents and
will structure content in an `<html>` document element with nested `<head>` and
`<body>` tags.

```js
const $ = cheerio.load('<li>Apple</li><li>Banana</li>');

$.html(); // => '<html><head></head><body><li>Apple</li><li>Banana</li></body></html>'
```

`parse5` also supports a "fragment mode" that allows you to parse HTML
fragments, rather than complete documents. To use this mode, pass a boolean
indicating whether you are parsing a full document to the `.load()` method:

```js
// Note that we are passing `false`, as we are not parsing a full document.
const $ = cheerio.load('<li>Apple</li><li>Banana</li>', {}, false);

$.html(); // => '<li>Apple</li><li>Banana</li>'
```

This will parse the HTML fragment as a standalone document, rather than treating
it as a part of a larger document.

## Parsing XML with htmlparser2

By default, Cheerio uses `htmlparser2` for XML documents. `htmlparser2` is a
fast and memory-efficient parser that can handle both HTML and XML. To parse
XML, pass the `xml` option to `.load()`:

```js
const $ = cheerio.load('<ul id="fruits">...</ul>', {
  xml: true,
});
```

If you need to customize the parsing options for XML input, you may pass an
object as the `xml` option to `.load()`, with the options you want to change:

```js
const $ = cheerio.load('<ul id="fruits">...</ul>', {
  xml: {
    withStartIndices: true,
  },
});
```

When `xml` is set, the default options are:

```js
{
    xmlMode: true, // Enable htmlparser2's XML mode.
    decodeEntities: true, // Decode HTML entities.
    withStartIndices: false, // Add a `startIndex` property to nodes.
    withEndIndices: false, // Add an `endIndex` property to nodes.
}
```

The options in the xml object are taken directly from htmlparser2, therefore any
options that can be used in htmlparser2 are valid in cheerio as well.

For a full list of options and their effects, see
[the API documentation](/brain/knowledge/docs_legacy/api/interfaces/HTMLParser2Options).

### Using `htmlparser2` for HTML

Some users may wish to parse markup with the `htmlparser2` library, and traverse
and manipulate the resulting structure with Cheerio. This may be the case for
those upgrading from pre-1.0 releases of Cheerio (which relied on
`htmlparser2`), for those dealing with invalid markup (because `htmlparser2` is
more forgiving[^1]), or for those operating in performance-critical situations
(because `htmlparser2` is often faster and the resulting DOM consumes less
memory).

[^1]:
    Note that "more forgiving" means `htmlparser2` has error-correcting
    mechanisms that aren't always a match for the standards observed by web
    browsers. This behavior may be useful when parsing non-HTML content.

To support these cases, you can simply disable `xmlMode` inside of the `xml`
option:

```js
const $ = cheerio.load('<ul id="fruits">...</ul>', {
  xml: {
    // Disable `xmlMode` to parse HTML with htmlparser2.
    xmlMode: false,
  },
});
```

`.load()` also accepts a `htmlparser2`-compatible data structure as its first
argument. Users may install `htmlparser2`, use it to parse input, and pass the
result to `.load()`:

```js
import * as htmlparser2 from 'htmlparser2';
const dom = htmlparser2.parseDocument(document, options);

const $ = cheerio.load(dom);
```

The caveat of this method is that this will still use `parse5`'s serializer, so
the resulting output will be HTML, not XML, and not respect any of the supplied
options. Disabling `xmlMode`, as shown above, is therefore the recommended
approach.

:::tip

You can also use Cheerio's _slim_ export, which always uses `htmlparser2`. This
avoids loading `parse5`, which saves some bytes eg. in browser environments:

```js
import * as cheerio from 'cheerio/slim';
```

:::

## Conclusion

In this guide, we explored how to configure Cheerio for parsing HTML and XML
documents using `parse5` and `htmlparser2` respectively. We also discussed how
to modify parsing options and use `htmlparser2` directly.
```

## File: `website/src/content/brain/knowledge/docs_legacy/advanced/extending-cheerio.md`
```markdown
---
sidebar_position: 999
description: Create custom pseudo-classes and plugins.
---

# Extending Cheerio

Cheerio already provides many ways of working with documents, but sometimes you
may want to add custom functionality. This guide will cover two approaches:
adding custom CSS pseudo elements and writing plugins for Cheerio.

## Adding Custom CSS Pseudo-Classes

The `pseudos` option is the extension point for adding pseudo-classes. It is a
map from names to either strings of functions.

- A string value is a selector that the element must match to be selected.
- A function is called with the element as its first argument, and optional
  parameters as the second. If it returns true, the element is selected.

Here is an example of using the pseudos option:

```js
const $ = cheerio.load('<div class="foo"></div><div data-bar="boo"></div>', {
  pseudos: {
    // `:foo` is an alias for `div.foo`
    foo: 'div.foo',
    // `:bar(val)` is equivalent to `[data-bar=val s]`
    bar: (el, val) => el.attribs['data-bar'] === val,
  },
});

$(':foo').length; // 1
$('div:bar(boo)').length; // 1
$('div:bar(baz)').length; // 0
```

## Writing Plugins for Cheerio

Once you have loaded a document, you may extend the prototype or the equivalent
`fn` property with custom plugin methods. Here is an example:

```js
const $ = cheerio.load('<html><body>Hello, <b>world</b>!</body></html>');
$.prototype.logHtml = function () {
  console.log(this.html());
};

$('body').logHtml(); // logs "Hello, <b>world</b>!" to the console
```

If you're using TypeScript, you should add a type definition for your new
method:

```ts
declare module 'cheerio' {
  interface Cheerio<T> {
    logHtml(this: Cheerio<T>): void;
  }
}
```
```

## File: `website/src/content/brain/knowledge/docs_legacy/advanced/extract.md`
```markdown
---
sidebar_label: The `extract` method
sidebar_position: 1
description: Extract multiple values at once.
---

# Extracting Data with the `extract` Method

The `extract` method allows you to extract data from an HTML document and store
it in an object. The method takes a `map` object as a parameter, where the keys
are the names of the properties to be created on the object, and the values are
the selectors or descriptors to be used to extract the values.

To use the `extract` method, you first need to import the library and load an
HTML document. For example:

```js
import * as cheerio from 'cheerio';

const $ = cheerio.load(`
  <ul>
    <li>One</li>
    <li>Two</li>
    <li class="blue sel">Three</li>
    <li class="red">Four</li>
  </ul>
`);
```

Once you have loaded the document, you can use the `extract` method on the
loaded object to extract data from the document.

Here are some examples of how to use the `extract` method:

```js
// Extract the text content of the first .red element
const data = $.extract({
  red: '.red',
});
```

This will return an object with a `red` property, whose value is the text
content of the first `.red` element.

To extract the text content of all `.red` elements, you can wrap the selector in
an array:

```js
// Extract the text content of all .red elements
const data = $.extract({
  red: ['.red'],
});
```

This will return an object with a `red` property, whose value is an array of the
text content of all `.red` elements.

To be more specific about what you'd like to extract, you can pass an object
with a `selector` and a `value` property. For example, to extract the text
content of the first `.red` element and the `href` attribute of the first `a`
element:

```js
const data = $.extract({
  red: '.red',
  links: {
    selector: 'a',
    value: 'href',
  },
});
```

The `value` property can be used to specify the name of the property to extract
from the selected elements. In this case, we are extracting the `href` attribute
from the `<a>` elements. This uses Cheerio's
[`prop` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#prop) under the hood.

`value` defaults to `textContent`, which extracts the text content of the
element.

As an attribute with special logic inside the `prop` method, `href`s will be
resolved relative to the document's URL. The document's URL will be set
automatically when using `fromURL` to load the document. Otherwise, use the
`baseURI` option to specify the documents URL.

There are many props available here; have a look at the
[`prop` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#prop) for details. For example, to
extract the `outerHTML` of all `.red` elements:

```js
const data = $.extract({
  red: [
    {
      selector: '.red',
      value: 'outerHTML',
    },
  ],
});
```

You can also extract data from multiple nested elements by specifying an object
as the `value`. For example, to extract the text content of all `.red` elements
and the first `.blue` element in the first `<ul>` element, and the text content
of all `.sel` elements in the second `<ul>` element:

```js
const data = $.extract({
  ul1: {
    selector: 'ul:first',
    value: {
      red: ['.red'],
      blue: '.blue',
    },
  },
  ul2: {
    selector: 'ul:eq(2)',
    value: {
      sel: ['.sel'],
    },
  },
});
```

This will return an object with `ul1` and `ul2` properties. The `ul1` property
will be an object with a `red` property, whose value is an array of the text
content of all `.red` elements in the first ul element, and a `blue` property.
The `ul2` property will be an object with a `sel` property, whose value is an
array of the text content of all `.sel` elements in the second `<ul>` element.

Finally, you can pass a function as the `value` property. The function will be
called with each of the selected elements, and the `key` of the property:

```js
const data = $.extract({
  links: [
    {
      selector: 'a',
      value: (el, key) => {
        const href = $(el).attr('href');
        return `${key}=${href}`;
      },
    },
  ],
});
```

This will extract the `href` attribute of all `<a>` elements and return a string
in the form `links=href_value` for each element, where `href_value` is the value
of the `href` attribute. The returned object will have a `links` property whose
value is an array of these strings.

## Putting it all together

Let's fetch the latest release of Cheerio from GitHub and extract the release
date and the release notes from the release page:

```js
import * as cheerio from 'cheerio';

const $ = await cheerio.fromURL(
  'https://github.com/cheeriojs/cheerio/releases',
);

const data = $.extract({
  releases: [
    {
      // First, we select individual release sections.
      selector: 'section',
      // Then, we extract the release date, name, and notes from each section.
      value: {
        // Selectors are executed within the context of the selected element.
        name: 'h2',
        date: {
          selector: 'relative-time',
          // The actual release date is stored in the `datetime` attribute.
          value: 'datetime',
        },
        notes: {
          selector: '.markdown-body',
          // We are looking for the HTML content of the element.
          value: 'innerHTML',
        },
      },
    },
  ],
});
```
```

## File: `website/src/content/brain/knowledge/docs_legacy/basics/loading.md`
```markdown
---
sidebar_position: 2
description: A walkthrough of different loading methods.
---

# Loading Documents

In this guide, we'll take a look at how to load documents with Cheerio and when
to use the different loading methods.

:::tip

If you're familiar with jQuery, then this step will be new to you. jQuery
operates on the one, baked-in DOM. With Cheerio, we need to pass in the HTML
document.

:::

:::danger[Availability of methods]

The `loadBuffer`, `stringStream`, `decodeStream`, and `fromURL` methods are not
available in the browser environment. Instead, use the `load` method to parse
HTML strings.

:::

## `load`

The load method is the most basic way to parse an HTML or XML document with
Cheerio. It takes a string containing the document as its argument and returns a
Cheerio object that you can use to traverse and manipulate the document.

Here's an example of how to use the load method:

```js
import * as cheerio from 'cheerio';

const $ = cheerio.load('<h1>Hello, world!</h1>');

console.log($('h1').text());
// Output: Hello, world!
```

:::tip

Similar to web browser contexts, `load` will introduce `<html>`, `<head>`, and
`<body>` elements if they are not already present. You can set `load`'s third
argument to `false` to disable this.

```js
const $ = cheerio.load('<ul id="fruits">...</ul>', null, false);

$.html();
//=> '<ul id="fruits">...</ul>'
```

:::

Learn more about the `load` method in the
[API documentation](/brain/knowledge/docs_legacy/api/variables/load).

## `loadBuffer`

The `loadBuffer` method is similar to the `load` method, but it takes a buffer
containing the document as its argument instead of a string. Cheerio will run
the HTML encoding sniffing algorithm to determine the encoding of the document.
This is useful when you have the document in binary form, such as when you're
reading it from a file or receiving it over a network connection.

Here's an example of how to use the `loadBuffer` method:

```js
import * as cheerio from 'cheerio';
import * as fs from 'fs';

const buffer = fs.readFileSync('document.html');

const $ = cheerio.loadBuffer(buffer);

console.log($('title').text());
// Output: Hello, world!
```

Learn more about the `loadBuffer` method in the
[API documentation](/brain/knowledge/docs_legacy/api/functions/loadBuffer).

## `stringStream`

When loading an HTML document from a stream and the encoding is known, you can
use the `stringStream` method to parse it into a Cheerio object.

```js
import * as cheerio from 'cheerio';
import * as fs from 'fs';

const writeStream = cheerio.stringStream({}, (err, $) => {
  if (err) {
    // Handle error
  }

  console.log($('title').text());
  // Output: Hello, world!
});

fs.createReadStream('document.html', { encoding: 'utf8' }).pipe(writeStream);
```

Learn more about the `stringStream` method in the
[API documentation](/brain/knowledge/docs_legacy/api/functions/stringStream).

## `decodeStream`

When loading an HTML document from a stream and the encoding is not known, you
can use the `decodeStream` method to parse it into a Cheerio object. This method
runs the HTML encoding sniffing algorithm to determine the encoding of the
document.

Here's an example of how to use the `decodeStream` method:

```js
import * as cheerio from 'cheerio';
import * as fs from 'fs';

const writeStream = cheerio.decodeStream({}, (err, $) => {
  if (err) {
    // Handle error
  }

  console.log($('title').text());
  // Output: Hello, world!
});

fs.createReadStream('document.html').pipe(writeStream);
```

Learn more about the `decodeStream` method in the
[API documentation](/brain/knowledge/docs_legacy/api/functions/decodeStream).

## `fromURL`

The `fromURL` method allows you to load a document from a URL. This method is
asynchronous, so you need to use `await` (or a `then` block) to access the
resulting Cheerio object.

```js
import * as cheerio from 'cheerio';

const $ = await cheerio.fromURL('https://example.com');
```

Learn more about the `fromURL` method in the
[API documentation](/brain/knowledge/docs_legacy/api/functions/fromURL).

## Conclusion

Cheerio provides several methods for loading HTML documents and parsing them
into a DOM structure. These methods are useful for different scenarios,
depending on the type and source of the HTML data. Users are encouraged to read
through each of these methods and pick the one that best suits their needs.

<!-- Based on ChatGPT with the prompt: Write a guide in Markdown for loading documents with Cheerio, explaining when to use `load`, `loadBuffer`, `stringStream`, `decodeStream`, and `fromURL`. Methods that deal with binary data run the HTML encoding sniffing algorithm and are recommended when the encoding is not known. The guide should be ready to be published on Cheerio's website. Use modern JavaScript with imports in the examples. -->
```

## File: `website/src/content/brain/knowledge/docs_legacy/basics/manipulation.md`
```markdown
---
sidebar_position: 5
description: Methods to manipulate elements within a document.
---

# Manipulating the DOM

Now that you have learned the basics of using Cheerio and have gained some
experience with loading and traversing documents, it's time to dive deeper into
manipulating elements. Whether you want to modify element attributes and
properties, add and remove classes, modify text and HTML content, or insert and
remove elements, Cheerio provides a range of methods to help you do so.

In this guide, we will focus specifically on manipulating elements within a
document using Cheerio. We will cover methods for modifying element attributes
and properties, adding and removing classes, modifying text and HTML content,
inserting and removing elements, and handling errors and debugging. By the end
of this guide, you will have a good understanding of how to use these methods to
manipulate elements within a document using Cheerio.

## Modifying Element Attributes and Properties

To modify the attributes and properties of a single element, you can use the
[`attr()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#attr) and
[`prop()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#prop) methods, respectively. Both methods
take a key and a value as arguments, and allow you to get and set the attribute
or property. When setting, they apply to all elements in the selection; when
getting, they return a single value corresponding to the first element in the
selection.

```js
// Set the 'src' attribute of an image element
$('img').attr('src', 'https://example.com/image.jpg');

// Set the 'checked' property of a checkbox element
$('input[type="checkbox"]').prop('checked', true);

// Get the 'href' attribute of a link element
const href = $('a').attr('href');

// Get the 'disabled' property of a button element
const isDisabled = $('button').prop('disabled');
```

`prop()` is not limited to simple values like strings and booleans. You can also
use it to get complex properties like the `style` object, or to resolve `href`
or `src` URLs of supported elements. You can also use it to get the `tagName`,
`innerHTML`, `outerHTML`, `textContent`, and `innerText` properties of a single
element.

```js
// Get the `style` object of an element
const style = $('div').prop('style');

// Get the resolved `src` URL of an image element
$('img').prop('src');

// Get the outerHTML of an element
const outerHTML = $('div').prop('outerHTML');

// Get the innerText of an element
const innerText = $('div').prop('innerText');
```

## Adding and Removing Classes

To add or remove classes from an element, you can use the
[`addClass()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#addclass),
[`removeClass()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#removeclass), and
[`toggleClass()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#toggleclass) methods. All three
methods take a class name or a space-separated list of class names as an
argument. They modify all elements in the selection.

```js
// Add a class to an element
$('div').addClass('new-class');

// Add multiple classes to an element
$('div').addClass('new-class another-class');

// Remove a class from an element
$('div').removeClass('old-class');

// Remove multiple classes from an element
$('div').removeClass('old-class another-class');

// Toggle a class on an element (add if it doesn't exist, remove if it does)
$('div').toggleClass('active');
```

## Modifying the Text Content of an Element

To query or modify the text content of an element, you can use the
[`text()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#text) method. Given a string as an
argument, it sets the text content of every element in the selection to the
given string. Without arguments, it returns the text content of every element
(including its descendants) in the selection, concatenated together.

```js
// Set the text content of an element
$('h1').text('Hello, World!');

// Get the text content of an element
const text = $('p').text();
```

:::tip[Note]

`text()` returns the `textContent` of all passed elements. The result will
include the contents of `<script>` and `<style>` elements. To avoid this, use
`.prop('innerText')` instead.

:::

## Modifying the HTML Content of an Element

To query or modify the HTML content of an element, you can use the
[`html()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#html) method. Given an HTML string as an
argument, it sets the inner HTML of every element in the selection to the given
string. Without arguments, it returns the inner HTML of the _first_ element in
the selection.

```js
// Set the inner HTML of an element
$('div').html('<p>Hello, World!</p>');

// Get the inner HTML of an element
const html = $('div').html();
```

## Inserting New Elements

To insert new elements into a document, you can use the
[`append()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#append),
[`prepend()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#prepend),
[`before()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#before), and
[`after()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#after) methods. These modify every element
in the selection.

```js
// Append an element to the end of a parent element
$('ul').append('<li>Item</li>');

// Prepend an element to the beginning of a parent element
$('ul').prepend('<li>Item</li>');

// Insert an element before a target element
$('li').before('<li>Item</li>');

// Insert an element after a target element
$('li').after('<li>Item</li>');
```

The [`insertAfter()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#insertafter) and
[`insertBefore()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#insertbefore) methods allow you to
insert an element before or after a target element, respectively. Both methods
take a string or a Cheerio object as an argument and insert the given element
before or after the target element.

```js
const $ = require('cheerio');

// Insert an element after a target element
$('<p>Inserted element</p>').insertAfter('h1');

// Insert an element before a target element
$('<p>Inserted element</p>').insertBefore('h1');
```

The [`prependTo()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#prependto) and
[`appendTo()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#appendto) methods allow you to prepend
or append an element to a parent element, respectively. Both methods take a
string or a Cheerio object as an argument and insert the element at the
beginning or end of the given parent element.

```js
const $ = require('cheerio');

// Prepend an element to a parent element
$('<p>Inserted element</p>').prependTo('div');

// Append an element to a parent element
$('<p>Inserted element</p>').appendTo('div');
```

## Wrapping and Unwrapping Elements

Sometimes you may want to wrap an element in another element, or remove the
element's parent element while keeping its children. To do this, you can use the
`wrap()`, `wrapInner()`, and `unwrap()` methods.

The [`wrap()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#wrap) method takes a string or a
Cheerio object as an argument and wraps the element in the given element.

```js
// Wrap an element in a div
$('p').wrap('<div></div>');
```

The [`wrapInner()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#wrapinner) method works similar to
wrap(), but instead of wrapping the element itself, it wraps the element's inner
HTML in the given element.

```js
// Wrap the inner HTML of an element in a div
$('div').wrapInner('<div></div>');
```

The [`unwrap()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#unwrap) method removes the element's
parent element, while keeping the element and its children.

```js
// Unwrap an element
$('p').unwrap();
```

## Replacing Elements

To replace an element with another element, you can use the
[`replaceWith()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#replacewith) method. It takes a
string or a Cheerio object as an argument and replaces each element in the
selection with the given element.

```js
// Replace an element with another element
$('li').replaceWith('<li>Item</li>');
```

Note that the `replaceWith()` method removes the element from the document and
replaces it with the given element or HTML string. If you want to keep the
element and modify its contents, you can use the `html()` or `text()` methods
instead.

## Removing Elements

To remove an element from a document, you can use the
[`remove()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#remove) method. It removes each element
in the selection, and all of their children, from the document.

```js
// Remove an element from the document
$('li').remove();
```

Alternatively, you can remove the children of an element from the document,
without removing the element itself, using the
[`empty()`](/brain/knowledge/docs_legacy/api/classes/Cheerio#empty) method. It removes the children
(but not text nodes or comments) of each element in the selection from the
document.

```js
// Remove an element's children from the document
$('li').empty();
```

## Conclusion

We learned how to manipulate elements within a document using Cheerio. We can
modify element attributes and properties, add and remove classes, modify text
and HTML content, insert and remove elements, and handle errors and debug our
code. With these tools, you can easily manipulate a document to suit your needs.
```

## File: `website/src/content/brain/knowledge/docs_legacy/basics/selecting.md`
```markdown
---
sidebar_position: 3
description: An introduction to CSS selectors.
---

# Selecting Elements

Cheerio allows users to select elements from an HTML document using
[CSS selectors](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Glossary/CSS_Selector).
This allows you to select elements based on criteria such as their tag name,
class name, and attribute values. This guide provides an overview of how to use
CSS selectors to retrieve elements.

To select elements with Cheerio, you first need to import the library and load a
document. For example:

```js
import * as cheerio from 'cheerio';

// Load the document using any of the methods described in the "Loading Documents" section.
const $ = cheerio.load('<html>...</html>');
```

Once you have loaded the document, you can use the `$` function to select
elements. The `$` function works just like the `$` function in jQuery, and
allows you to select elements based on their tag name, class name, and attribute
values.

Here are some examples of how to use the `$` function to select elements:

- To select all the `<p>` elements in the document:

```js
const $p = $('p');
```

:::tip

The convention in Cheerio is to prefix the variable name with a $ to indicate
that it contains a Cheerio object. This is not required, but it is a good
practice to follow.

:::

- To select elements with a specific class name:

```js
const $selected = $('.selected');
```

- To select elements with a specific attribute value:

```js
const $selected = $('[data-selected=true]');
```

:::tip[XML Namespaces]

You can select with XML Namespaces but
[due to the CSS specification](https://www.w3.org/TR/2011/REC-css3-selectors-20110929/#attribute-selectors),
the colon (`:`) needs to be escaped for the selector to be valid.

```js
$('[xml\\:id="main"');
```

:::

- Selectors can be combined to select elements that match multiple criteria. For
  example, to select all `<p>` elements with the class `selected`:

```js
const $selected = $('p.selected');
```

- Further, you can use spaces (` `) to select elements that are descendants of
  other elements. For example, to select all `<p>` elements that are descendants
  of `<div>` elements:

```js
const $p = $('div p');
```

- You can also use the `>` character to select elements that are direct
  descendants of other elements. For example, to select all `<p>` elements that
  are direct descendants of `<div>` elements:

```js
const $p = $('div > p');
```

Please have a look at the documentation of Cheerio's underlying CSS selector
library, `css-select`, for
[a list of all supported selectors](https://github.com/fb55/css-select/blob/master/README.md#supported-selectors).
For example, to select `<p>` elements containing the word "hello":

```js
const $p = $('p:contains("hello")');
```

Cheerio also supports several jQuery-specific extensions that allow you to
select elements based on their position in the document. For example, to select
the first `<p>` element in the document:

```js
const $p = $('p:first');
```

Have a look at
[cheerio-select](https://github.com/cheeriojs/cheerio-select/blob/master/README.md),
the library that implements these extensions, to see what is available.

For further information, please also have a look at jQuery's guide on
[selecting elements](https://learn.jquery.com/using-jquery-core/selecting-elements/),
as well as
[MDN](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Glossary/CSS_Selector).

Finally, to add custom CSS pseudo-classes, have a look at the
[Extending Cheerio guide](/brain/knowledge/docs_legacy/advanced/extending-cheerio#adding-custom-css-pseudo-classes).
```

## File: `website/src/content/brain/knowledge/docs_legacy/basics/traversing.mdx`
```
---
sidebar_position: 4
description: Traverse the DOM tree and filter elements.
---

import { LiveCode } from '@/components/live-code';

# Traversing the DOM

Traversing a document with Cheerio allows you to select and manipulate specific
elements within the document. Whether you want to move up and down the DOM tree,
move sideways within the tree, or filter elements based on certain criteria,
Cheerio provides a range of methods to help you do so.

In this guide, we will go through the various methods available in Cheerio for
traversing and filtering elements. We will cover methods for moving down the DOM
tree, moving up the DOM tree, moving sideways within the tree, and filtering
elements. By the end of this guide, you will have a good understanding of how to
use these methods to select and manipulate elements within a document using
Cheerio.

:::tip

This guide is intended to give you an overview of the various methods available
in Cheerio for traversing and filtering elements. For a more detailed reference
of these methods, see the [API documentation](/brain/knowledge/docs_legacy/api/classes/Cheerio).

:::

## Moving Down the DOM Tree

Cheerio provides several methods for moving down the DOM tree and selecting
elements that are children or descendants of the current selection.

### `find`

The [`find` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#find) allows you to locate
specific elements within a selection. It takes a CSS selector as an argument and
returns a new selection containing all elements that match the selector within
the current selection.

Here's an example of using `find` to select all `<li>` elements within a `<ul>`
element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>`,
);

const listItems = $('ul').find('li');
console.log(`List item count: ${listItems.length}`);
```

### `children`

The [`children` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#children) allows you to select
the direct children of an element. It returns a new selection containing all
direct children of the current selection.

Here's an example of using `children` to select all `<li>` elements within a
`<ul>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>`,
);

const listItems = $('ul').children('li');
console.log(`List item count: ${listItems.length}`);
```

### `contents`

The [`contents` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#contents) allows you to select
all children of an element, including text and comment nodes. It returns a new
selection containing all children of the current selection.

Here's an example of using `contents` to select all children of a `<div>`
element:

```js live
const $ = cheerio.load(
  `<div>
    Text <p>Paragraph</p>
  </div>`,
);

const contents = $('div').contents();
console.log(`Contents count: ${contents.length}`);
```

## Moving Up the DOM Tree

Cheerio provides several methods for moving up the DOM tree and selecting
elements that are ancestors of the current selection.

### `parent`

The [`parent` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#parent) allows you to select the
parent element of a selection. It returns a new selection containing the parent
element of each element in the current selection.

Here's an example of using `parent` to select the parent `<ul>` element of a
`<li>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
  </ul>`,
);

const list = $('li').parent();
console.log(list.prop('tagName'));
```

### `parents` and `parentsUntil`

The [`parents` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#parents) allows you to select
all ancestor elements of a selection, up to the root element. It returns a new
selection containing all ancestor elements of the current selection.

The [`parentsUntil` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#parentsuntil) is similar
to `parents`, but allows you to specify an ancestor element as a stop point. It
returns a new selection containing all ancestor elements of the current
selection up to (but not including) the specified ancestor.

Here's an example of using `parents` and `parentsUntil` to select ancestor
elements of a `<li>` element:

```js live
const $ = cheerio.load(
  `<div>
    <ul>
      <li>Item 1</li>
    </ul>
  </div>`,
);

const ancestors = $('li').parents();
const ancestorsUntil = $('li').parentsUntil('div');

console.log(`Ancestor count (includes body and html): ${ancestors.length}`);
console.log(`Ancestor count (until div): ${ancestorsUntil.length}`);
```

### `closest`

The [`closest` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#closest) allows you to select
the closest ancestor matching a given selector. It returns a new selection
containing the closest ancestor element that matches the selector. If no
matching ancestor is found, the method returns an empty selection.

Here's an example of using `closest` to select the closest ancestor `<ul>`
element of a `<li>` element:

```js live
const $ = cheerio.load(
  `<div>
    <ul>
      <li>Item 1</li>
    </ul>
  </div>`,
);

const list = $('li').closest('ul');
console.log(list.prop('tagName'));
```

## Moving Sideways Within the DOM Tree

Cheerio provides several methods for moving sideways within the DOM tree and
selecting elements that are siblings of the current selection.

### `next` and `prev`

The [`next` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#next) allows you to select the
next sibling element of a selection. It returns a new selection containing the
next sibling element (if there is one). If the given selection contains multiple
elements, `next` includes the next sibling for each one.

The [`prev` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#prev) is similar to `next`, but
allows you to select the previous sibling element. It returns a new selection
containing the previous sibling element for each element in the given selection.

Here's an example of using `next` and `prev` to select sibling elements of a
`<li>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>`,
);

const nextItem = $('li:first').next();
const prevItem = $('li:eq(1)').prev();

console.log(`Next: ${nextItem.text()}`);
console.log(`Prev: ${prevItem.text()}`);
```

## `nextAll`, `prevAll`, and `siblings`

The [`nextAll` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#nextall) allows you to select
all siblings after the current element. It returns a new selection containing
all sibling elements after each element in the current selection.

The [`prevAll` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#prevall) is similar to nextAll,
but allows you to select all siblings before the current element. It returns a
new selection containing all sibling elements before each element in the current
selection.

The [`siblings` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#siblings) allows you to select
all siblings of a selection. It returns a new selection containing all sibling
elements of each element in the current selection.

Here's an example of using `nextAll`, `prevAll`, and `siblings` to select
sibling elements of a `<li>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>[1]</li>
    <li>[2]</li>
    <li>[3]</li>
  </ul>`,
);

const nextAll = $('li:first').nextAll();
const prevAll = $('li:last').prevAll();
const siblings = $('li:eq(1)').siblings();

console.log(`Next All: ${nextAll.text()}`);
console.log(`Prev All: ${prevAll.text()}`);
console.log(`Siblings: ${siblings.text()}`);
```

### `nextUntil` and `prevUntil`

The [`nextUntil` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#nextuntil) allows you to
select all siblings after the current element up to a specified sibling. It
takes a selector or a sibling element as an argument and returns a new selection
containing all sibling elements after the current element up to (but not
including) the specified element.

The [`prevUntil` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#prevuntil) is similar to
`nextUntil`, but allows you to select all siblings before the current element up
to a specified sibling. It takes a selector or a sibling element as an argument
and returns a new selection containing all sibling elements before the current
element up to (but not including) the specified element.

Here's an example of using `nextUntil` and `prevUntil` to select sibling
elements of a `<li>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>`,
);

const nextUntil = $('li:first').nextUntil('li:last-child');
const prevUntil = $('li:last').prevUntil('li:first-child');

console.log(`Next: ${nextUntil.text()}`);
console.log(`Prev: ${prevUntil.text()}`);
```

## Filtering elements

Cheerio provides several methods for filtering elements within a selection.

:::tip

Most of these filters also exist as selectors. For example, the `first` method
is available as the `:first` selector. Users are encouraged to use the selector
syntax when possible, as it is more performant.

:::

### `eq`

The [`eq` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#eq) allows you to select an element
at a specified index within a selection. It takes an index as an argument and
returns a new selection containing the element at the specified index.

Here's an example of using `eq` to select the second `<li>` element within a
`<ul>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>`,
);

const secondItem = $('li').eq(1);
console.log(secondItem.text());
```

### `filter` and `not`

The [`filter` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#filter) allows you to select
elements that match a given selector. It takes a selector as an argument and
returns a new selection containing only those elements that match the selector.

The [`not` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#not) is similar to `filter`, but
allows you to select elements that do not match a given selector. It takes a
selector as an argument and returns a new selection containing only those
elements that do not match the selector.

Here's an example of using `filter` and `not` to select `<li>` elements within a
`<ul>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li class="item">Item 1</li>
    <li>Item 2</li>
  </ul>`,
);

const matchingItems = $('li').filter('.item');
const nonMatchingItems = $('li').not('.item');

console.log(`Matching: ${matchingItems.text()}`);
console.log(`Non-matching: ${nonMatchingItems.text()}`);
```

### `has`

The [`has` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#has) allows you to select elements
that contain an element matching a given selector. It takes a selector as an
argument and returns a new selection containing only those elements that contain
an element matching the selector.

Here's an example of using `has` to select `<li>` elements within a `<ul>`
element that contain a `<strong>` element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>
      <strong>Item 2</strong>
    </li>
  </ul>`,
);

const matchingItems = $('li').has('strong');
console.log(matchingItems.length);
```

### `first` and `last`

The [`first` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#first) allows you to select the
first element in a selection. It returns a new selection containing the first
element.

The [`last` method](/brain/knowledge/docs_legacy/api/classes/Cheerio#last) is similar to `first`, but
allows you to select the last element in a selection. It returns a new selection
containing the last element.

Here's an example of using `first` and `last` to select elements within a `<ul>`
element:

```js live
const $ = cheerio.load(
  `<ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>`,
);

const firstItem = $('li').first();
const lastItem = $('li').last();

console.log(`First: ${firstItem.text()}`);
console.log(`Last: ${lastItem.text()}`);
```

## Conclusion

Cheerio provides a range of methods for traversing and filtering elements within
a document. These methods allow you to move up and down the DOM tree, move
sideways within the tree, and filter elements based on various criteria. By
using these methods, you can easily select and manipulate elements within a
document using Cheerio.
```

## File: `website/src/layouts/BaseLayout.astro`
```
---
import '@/styles/global.css';
import { ViewTransitions } from 'astro:transitions';
import Footer from '@/components/Footer.astro';
import Navbar from '@/components/Navbar.astro';

interface Props {
  title: string;
  description?: string;
}

const {
  title,
  description = 'The fast, flexible & elegant library for parsing and manipulating HTML and XML.',
} = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <meta
      name="keywords"
      content="htmlparser, jquery, selector, scraper, parser, dom, xml, html, nodejs"
    />
    <link rel="icon" type="image/x-icon" href="/img/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
    <title>{title} | Cheerio</title>
    <ViewTransitions />
    <script is:inline async src="https://www.googletagmanager.com/gtag/js?id=G-PZHRH775FB"></script>
    <script is:inline>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag('js', new Date());
      gtag('config', 'G-PZHRH775FB');
    </script>
  </head>
  <body
    class="flex min-h-screen flex-col bg-white text-slate-900 dark:bg-slate-900 dark:text-slate-100"
  >
    <Navbar />
    <main class="flex-1">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

## File: `website/src/layouts/BlogLayout.astro`
```
---
import BaseLayout from '@/layouts/BaseLayout.astro';

interface Props {
  title: string;
  description?: string;
  date?: Date;
  author?: string;
}

const {
  title,
  description = 'The fast, flexible & elegant library for parsing and manipulating HTML and XML.',
  date,
  author,
} = Astro.props;

const formattedDate = date
  ? date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    })
  : null;
---

<BaseLayout title={title} description={description}>
  <article class="mx-auto max-w-3xl px-6 py-12">
    {/* Editorial header */}
    <header class="mb-10 border-b border-slate-200 pb-8 dark:border-slate-700/50">
      <a
        href="/blog"
        class="mb-4 inline-flex items-center gap-1.5 text-sm font-medium text-slate-400 transition-colors hover:text-primary dark:text-slate-500 dark:hover:text-primary"
      >
        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
        </svg>
        Back to Blog
      </a>
      <h1 class="font-display text-3xl text-slate-900 lg:text-4xl dark:text-white">{title}</h1>
      {
        (formattedDate || author) && (
          <div class="mt-4 flex items-center gap-3 text-sm text-slate-500 dark:text-slate-400">
            {formattedDate && (
              <time class="font-medium">{formattedDate}</time>
            )}
            {formattedDate && author && (
              <span class="text-slate-300 dark:text-slate-600">&middot;</span>
            )}
            {author && <span>by {author}</span>}
          </div>
        )
      }
    </header>
    <div class="prose">
      <slot />
    </div>
  </article>
</BaseLayout>
```

## File: `website/src/layouts/DocsLayout.astro`
```
---
import '@/styles/global.css';
import { ViewTransitions } from 'astro:transitions';
import Footer from '@/components/Footer.astro';
import Navbar from '@/components/Navbar.astro';
import Sidebar from '@/components/Sidebar.astro';
import TableOfContents from '@/components/TableOfContents.astro';

interface Props {
  title: string;
  description?: string;
  sourceFile?: string;
  wide?: boolean;
  headings?: Array<{
    depth: number;
    slug: string;
    text: string;
  }>;
}

const {
  title,
  description = 'The fast, flexible & elegant library for parsing and manipulating HTML and XML.',
  sourceFile,
  wide = false,
  headings = [],
} = Astro.props;

const editUrl = sourceFile
  ? `https://github.com/cheeriojs/cheerio/edit/main/website/src/content/brain/knowledge/docs_legacy/${sourceFile}`
  : null;

const currentPath = Astro.url.pathname;

// Flat ordered list of all doc pages for prev/next navigation
const allPages = [
  { label: 'Introduction', href: '/brain/knowledge/docs_legacy/intro' },
  { label: 'Loading Documents', href: '/brain/knowledge/docs_legacy/basics/loading' },
  { label: 'Selecting Elements', href: '/brain/knowledge/docs_legacy/basics/selecting' },
  { label: 'Traversing the DOM', href: '/brain/knowledge/docs_legacy/basics/traversing' },
  { label: 'Manipulating Elements', href: '/brain/knowledge/docs_legacy/basics/manipulation' },
  { label: 'Configuring Cheerio', href: '/brain/knowledge/docs_legacy/advanced/configuring-cheerio' },
  { label: 'Extending Cheerio', href: '/brain/knowledge/docs_legacy/advanced/extending-cheerio' },
  { label: 'Extracting Data', href: '/brain/knowledge/docs_legacy/advanced/extract' },
  { label: 'API Documentation', href: '/brain/knowledge/docs_legacy/api' },
];

const currentIndex = allPages.findIndex(
  (p) => p.href === currentPath.replace(/\/$/, ''),
);
const prevPage = currentIndex > 0 ? allPages[currentIndex - 1] : null;
const nextPage =
  currentIndex >= 0 && currentIndex < allPages.length - 1
    ? allPages[currentIndex + 1]
    : null;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <meta
      name="keywords"
      content="htmlparser, jquery, selector, scraper, parser, dom, xml, html, nodejs"
    />
    <link rel="icon" type="image/x-icon" href="/img/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
    <title>{title} | Cheerio</title>
    <ViewTransitions />
  </head>
  <body
    class="flex min-h-screen flex-col bg-white text-slate-900 dark:bg-slate-900 dark:text-slate-100"
  >
    <Navbar />
    <div class="mx-auto flex w-full max-w-screen-2xl flex-1">
      <Sidebar currentPath={currentPath} />
      <main class="flex-1 min-w-0 px-6 py-10 lg:px-10">
        {/* Mobile sidebar trigger */}
        <button
          type="button"
          id="sidebar-open"
          class="mb-6 inline-flex items-center gap-2 rounded-lg border border-slate-200 px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 lg:hidden dark:border-slate-700 dark:text-slate-400 dark:hover:bg-slate-800"
          aria-label="Open navigation"
        >
          <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
          Menu
        </button>

        {/* Editorial header */}
        <header class="mb-8 border-b border-slate-200 pb-6 dark:border-slate-700/50">
          <h1 class="font-display text-3xl text-slate-900 lg:text-4xl dark:text-white">{title}</h1>
        </header>

        <article class:list={['prose docs-content', { 'prose-wide': wide }]}>
          <slot />
        </article>

        {/* Edit on GitHub */}
        {editUrl && (
          <div class="mt-10 pt-5">
            <a
              href={editUrl}
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center gap-1.5 text-sm text-slate-400 transition-colors hover:text-primary dark:text-slate-500 dark:hover:text-primary"
            >
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
              </svg>
              Edit this page on GitHub
            </a>
          </div>
        )}

        {/* Prev/Next navigation */}
        {(prevPage || nextPage) && (
          <nav class="mt-12 flex items-stretch gap-4 border-t border-slate-200 pt-6 dark:border-slate-700/50" aria-label="Page navigation">
            {prevPage ? (
              <a
                href={prevPage.href}
                class="group flex flex-1 flex-col items-start rounded-xl border border-slate-200 px-5 py-4 transition-all hover:border-primary/40 hover:shadow-sm dark:border-slate-700 dark:hover:border-primary/40"
              >
                <span class="mb-1 text-xs font-medium uppercase tracking-wider text-slate-400 dark:text-slate-500">Previous</span>
                <span class="flex items-center gap-1.5 text-sm font-semibold text-slate-700 transition-colors group-hover:text-primary dark:text-slate-200 dark:group-hover:text-primary">
                  <svg class="h-3.5 w-3.5 transition-transform group-hover:-translate-x-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                  </svg>
                  {prevPage.label}
                </span>
              </a>
            ) : <div class="flex-1" />}
            {nextPage ? (
              <a
                href={nextPage.href}
                class="group flex flex-1 flex-col items-end rounded-xl border border-slate-200 px-5 py-4 transition-all hover:border-primary/40 hover:shadow-sm dark:border-slate-700 dark:hover:border-primary/40"
              >
                <span class="mb-1 text-xs font-medium uppercase tracking-wider text-slate-400 dark:text-slate-500">Next</span>
                <span class="flex items-center gap-1.5 text-sm font-semibold text-slate-700 transition-colors group-hover:text-primary dark:text-slate-200 dark:group-hover:text-primary">
                  {nextPage.label}
                  <svg class="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                  </svg>
                </span>
              </a>
            ) : <div class="flex-1" />}
          </nav>
        )}
      </main>
      <TableOfContents headings={headings} />
    </div>
    <Footer />
  </body>
</html>
```

## File: `website/src/pages/index.astro`
```
---
import Features from '@/components/Features.astro';
import Hero from '@/components/Hero.astro';
import Sponsors from '@/components/Sponsors.astro';
import Testimonials from '@/components/Testimonials.astro';
import BaseLayout from '@/layouts/BaseLayout.astro';
---

<BaseLayout title="The industry standard for working with HTML in JavaScript">
  <Hero />
  <Features />
  <Sponsors />
  <Testimonials />

  <!-- Final CTA Section -->
  <section class="relative overflow-hidden bg-slate-950 py-24">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(232,140,31,0.12),transparent_70%)]"></div>
    <div class="grain absolute inset-0 overflow-hidden opacity-40"></div>
    <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-primary/30 to-transparent"></div>

    <div class="relative z-10 mx-auto max-w-3xl px-6 text-center">
      <h2 class="animate-fade-up font-display text-4xl text-white md:text-5xl">
        Ready to get started?
      </h2>
      <p class="animate-fade-up animation-delay-100 mt-6 text-lg leading-relaxed text-slate-400">
        Join thousands of developers who use Cheerio to parse, manipulate, and render HTML with ease.
      </p>
      <div class="animate-fade-up animation-delay-200 mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
        <a
          href="/brain/knowledge/docs_legacy/intro"
          class="group inline-flex items-center gap-2 rounded-xl bg-primary px-8 py-3.5 font-semibold text-white transition-all duration-300 hover:bg-primary-dark hover:shadow-lg hover:shadow-primary/25"
        >
          Read the docs
          <svg class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
          </svg>
        </a>
        <a
          href="https://github.com/cheeriojs/cheerio"
          target="_blank"
          rel="noopener noreferrer"
          class="inline-flex items-center gap-2 rounded-xl border border-slate-700 px-8 py-3.5 font-semibold text-slate-300 transition-all duration-300 hover:border-slate-500 hover:text-white hover:bg-slate-800/50"
        >
          Star on GitHub
        </a>
      </div>
    </div>
  </section>
</BaseLayout>
```

## File: `website/src/pages/blog/[slug].astro`
```
---
import { getCollection, render } from 'astro:content';
import BlogLayout from '@/layouts/BlogLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map((post) => ({
    params: { slug: post.id.replace('.md', '').replace('.mdx', '') },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);

// Extract date from filename (e.g., "2024-08-07-version-1.md")
const dateParts = post.id.split('-').slice(0, 3);
const date = new Date(dateParts.join('-'));

// Get author name (simplified - in a real app you'd look this up)
const authorMap: Record<string, string> = {
  fb55: 'Felix Boehm',
};
const authorName = post.data.authors
  ? Array.isArray(post.data.authors)
    ? post.data.authors.map((a: string) => authorMap[a] || a).join(', ')
    : authorMap[post.data.authors] || post.data.authors
  : undefined;
---

<BlogLayout title={post.data.title} date={date} author={authorName}>
  <Content />
</BlogLayout>
```

## File: `website/src/pages/blog/index.astro`
```
---
import { getCollection } from 'astro:content';
import BaseLayout from '@/layouts/BaseLayout.astro';

const posts = await getCollection('blog');

// Sort posts by date (newest first)
const sortedPosts = posts.sort((a, b) => {
  const dateA = new Date(a.id.split('-').slice(0, 3).join('-'));
  const dateB = new Date(b.id.split('-').slice(0, 3).join('-'));
  return dateB.getTime() - dateA.getTime();
});

function getPostDate(id: string): string {
  const datePart = id.split('-').slice(0, 3).join('-');
  return new Date(datePart).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

function getPostSlug(id: string): string {
  return id.replace('.md', '').replace('.mdx', '');
}

// Extract excerpt from raw markdown content (content before <!--truncate-->)
function getExcerpt(rawContent: string): string | null {
  const truncateIndex = rawContent.indexOf('<!--truncate-->');
  if (truncateIndex === -1) return null;

  let excerpt = rawContent.slice(0, truncateIndex).trim();

  // Remove frontmatter
  const frontmatterEnd = excerpt.indexOf('---', 3);
  if (excerpt.startsWith('---') && frontmatterEnd !== -1) {
    excerpt = excerpt.slice(frontmatterEnd + 3).trim();
  }

  // Remove the first heading (usually the title, which duplicates frontmatter title)
  excerpt = excerpt.replace(/^#\s+.+\n+/, '').trim();

  // Remove admonition blocks (:::note, :::tip, etc.)
  excerpt = excerpt.replace(/^:::\w+(\[.*?\])?\n[\s\S]*?^:::\n*/gm, '').trim();

  // Strip markdown formatting to plain text
  excerpt = excerpt
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, '') // ![alt](url) → remove
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // [text](url) → text
    .replace(/(\*\*|__)(.*?)\1/g, '$2') // **bold** → bold
    .replace(/(\*|_)(.*?)\1/g, '$2') // *italic* → italic
    .replace(/`([^`]+)`/g, '$1') // `code` → code
    .replace(/^#{1,6}\s+/gm, '') // headings → text
    .replace(/^[-*+]\s+/gm, '') // list items
    .replace(/^\d+\.\s+/gm, '') // ordered list items
    .replace(/\n{2,}/g, ' ') // collapse newlines
    .replace(/\n/g, ' ') // remaining newlines
    .trim();

  return excerpt || null;
}

// Pre-render excerpts for each post
const postsWithExcerpts = sortedPosts.map((post) => {
  const excerpt = getExcerpt(post.body || '');
  return { post, excerpt };
});
---

<BaseLayout title="Blog">
  {/* Hero header */}
  <section class="relative overflow-hidden border-b border-slate-200 bg-gradient-to-b from-amber-50/60 to-white dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
    <div class="mx-auto max-w-4xl px-6 py-16 text-center">
      <h1 class="font-display text-4xl text-slate-900 lg:text-5xl dark:text-white">Blog</h1>
      <p class="mt-4 text-lg text-slate-500 dark:text-slate-400">
        Updates and announcements from the Cheerio team.
      </p>
      <a
        href="/blog/rss.xml"
        class="mt-6 inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 shadow-sm transition-all hover:border-primary/40 hover:text-primary dark:border-slate-700 dark:bg-slate-800 dark:text-slate-400 dark:hover:border-primary/40 dark:hover:text-primary"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
          <path d="M3.75 3a.75.75 0 0 0-.75.75v.5c0 .414.336.75.75.75H4c6.075 0 11 4.925 11 11v.25c0 .414.336.75.75.75h.5a.75.75 0 0 0 .75-.75V16C17 8.82 11.18 3 4 3h-.25Z" />
          <path d="M3 8.75A.75.75 0 0 1 3.75 8H4a8 8 0 0 1 8 8v.25a.75.75 0 0 1-.75.75h-.5a.75.75 0 0 1-.75-.75V16a6 6 0 0 0-6-6h-.25A.75.75 0 0 1 3 9.25v-.5ZM7 15a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z" />
        </svg>
        Subscribe via RSS
      </a>
    </div>
  </section>

  {/* Posts grid */}
  <div class="mx-auto max-w-4xl px-6 py-12">
    <div class="space-y-8">
      {
        postsWithExcerpts.map(({ post, excerpt }) => (
          <article class="group rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-200 hover:border-primary/30 hover:shadow-lg dark:border-slate-700/80 dark:bg-slate-800/50 dark:hover:border-primary/30">
            <div class="mb-3 flex items-center gap-3 text-sm text-slate-500 dark:text-slate-400">
              <time class="font-medium">{getPostDate(post.id)}</time>
              {post.data.tags && (
                <div class="flex gap-2">
                  {post.data.tags.map((tag: string) => (
                    <span class="rounded-full bg-primary/10 px-2.5 py-0.5 text-xs font-medium text-primary">
                      {tag}
                    </span>
                  ))}
                </div>
              )}
            </div>
            <h2 class="mb-2 font-heading text-xl font-semibold lg:text-2xl">
              <a
                href={`/blog/${getPostSlug(post.id)}`}
                class="text-slate-900 transition-colors hover:text-primary dark:text-white dark:hover:text-primary"
              >
                {post.data.title}
              </a>
            </h2>
            {excerpt && (
              <p class="mb-4 line-clamp-3 text-slate-600 dark:text-slate-400">{excerpt}</p>
            )}
            <a
              href={`/blog/${getPostSlug(post.id)}`}
              class="inline-flex items-center gap-1 text-sm font-medium text-primary transition-colors hover:text-primary-dark"
            >
              Read more
              <svg class="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
              </svg>
            </a>
          </article>
        ))
      }
    </div>
  </div>
</BaseLayout>
```

## File: `website/src/pages/blog/rss.xml.ts`
```typescript
import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { marked } from 'marked';

export async function GET(context: APIContext) {
  const posts = await getCollection('blog');

  // Sort posts by date (newest first)
  const sortedPosts = posts.toSorted((a, b) => {
    const dateA = new Date(a.id.split('-').slice(0, 3).join('-'));
    const dateB = new Date(b.id.split('-').slice(0, 3).join('-'));
    return dateB.getTime() - dateA.getTime();
  });

  if (!context.site) {
    throw new Error('Site URL is required for RSS feed generation');
  }

  return rss({
    title: 'Cheerio Blog',
    description: 'Updates and announcements from the Cheerio team.',
    site: context.site,
    items: sortedPosts.map((post) => {
      const datePart = post.id.split('-').slice(0, 3).join('-');
      const slug = post.id.replace('.md', '').replace('.mdx', '');

      // Render markdown body to HTML
      const content = post.body ? marked.parse(post.body) : '';

      return {
        title: post.data.title,
        pubDate: new Date(datePart),
        link: `/blog/${slug}/`,
        content: content as string,
      };
    }),
  });
}
```

## File: `website/src/pages/brain/knowledge/docs_legacy/[slug].astro`
```
---
import { getCollection, render } from 'astro:content';
import DocsLayout from '@/layouts/DocsLayout.astro';

export async function getStaticPaths() {
  const docs = await getCollection('docs');
  return docs
    .filter((doc) => !doc.id.includes('/'))
    .map((doc) => ({
      params: { slug: doc.id.replace(/\.mdx?$/, '') },
      props: { doc },
    }));
}

const { doc } = Astro.props;
const { Content, headings } = await render(doc);
const h1 = headings.find((h) => h.depth === 1);
const title = doc.data.title || h1?.text || doc.data.sidebar_label || doc.id;
---

<DocsLayout title={title} description={doc.data.description} headings={headings} sourceFile={doc.id}>
  <Content />
</DocsLayout>
```

## File: `website/src/pages/brain/knowledge/docs_legacy/advanced/[slug].astro`
```
---
import { getCollection, render } from 'astro:content';
import DocsLayout from '@/layouts/DocsLayout.astro';

export async function getStaticPaths() {
  const docs = await getCollection('docs');
  return docs
    .filter((doc) => doc.id.startsWith('advanced/'))
    .map((doc) => ({
      params: { slug: doc.id.replace('advanced/', '').replace(/\.mdx?$/, '') },
      props: { doc },
    }));
}

const { doc } = Astro.props;
const { Content, headings } = await render(doc);
const h1 = headings.find((h) => h.depth === 1);
const title = doc.data.title || h1?.text || doc.data.sidebar_label || doc.id;
---

<DocsLayout title={title} description={doc.data.description} headings={headings} sourceFile={doc.id}>
  <Content />
</DocsLayout>
```

## File: `website/src/pages/brain/knowledge/docs_legacy/api/[...slug].astro`
```
---
import { getCollection, render } from 'astro:content';
import DocsLayout from '@/layouts/DocsLayout.astro';

export async function getStaticPaths() {
  const docs = await getCollection('docs');
  return docs
    .filter((doc) => doc.id.startsWith('api/'))
    .map((doc) => {
      // Remove 'api/' prefix and file extension
      const rawSlug = doc.id.replace('api/', '').replace(/\.mdx?$/, '');
      return {
        // Use undefined slug for index page (catch-all [...slug] root)
        params: { slug: rawSlug === 'index' ? undefined : rawSlug },
        props: { doc },
      };
    });
}

const { doc } = Astro.props;
const { Content, headings } = await render(doc);
const h1 = headings.find((h) => h.depth === 1);
const title =
  doc.data.title || h1?.text || doc.data.sidebar_label || 'API Documentation';
---

<DocsLayout title={title} description={doc.data.description} headings={headings} sourceFile={doc.id} wide>
  <Content />
</DocsLayout>
```

## File: `website/src/pages/brain/knowledge/docs_legacy/basics/[slug].astro`
```
---
import { getCollection, render } from 'astro:content';
import DocsLayout from '@/layouts/DocsLayout.astro';

export async function getStaticPaths() {
  const docs = await getCollection('docs');
  return docs
    .filter((doc) => doc.id.startsWith('basics/'))
    .map((doc) => ({
      params: { slug: doc.id.replace('basics/', '').replace(/\.mdx?$/, '') },
      props: { doc },
    }));
}

const { doc } = Astro.props;
const { Content, headings } = await render(doc);
const h1 = headings.find((h) => h.depth === 1);
const title = doc.data.title || h1?.text || doc.data.sidebar_label || doc.id;
---

<DocsLayout title={title} description={doc.data.description} headings={headings} sourceFile={doc.id}>
  <Content />
</DocsLayout>
```

## File: `website/src/plugins/rehype-external-links.ts`
```typescript
import type { Element, Root } from 'hast';
import { visit } from 'unist-util-visit';

function visitExternalLink(node: Element): void {
  if (
    node.tagName === 'a' &&
    node.properties?.href &&
    typeof node.properties.href === 'string'
  ) {
    const { href } = node.properties;
    // Check if it's an external link (starts with http:// or https://)
    if (href.startsWith('http://') || href.startsWith('https://')) {
      node.properties.target = '_blank';
      node.properties.rel = 'noopener noreferrer';
    }
  }
}

function transformer(tree: Root): void {
  visit(tree, 'element', visitExternalLink);
}

/**
 * Rehype plugin to make external links open in a new tab. Adds target="_blank"
 * and rel="noopener noreferrer" to external links.
 *
 * @returns A transformer function.
 */
export function rehypeExternalLinks() {
  return transformer;
}
```

## File: `website/src/plugins/remark-admonitions.ts`
```typescript
import type { Root } from 'mdast';
import { visit } from 'unist-util-visit';

interface DirectiveData {
  hName?: string;
  hProperties?: Record<string, string>;
  directiveLabel?: boolean;
}

interface DirectiveNode {
  type: string;
  name: string;
  data?: DirectiveData;
  children: DirectiveChild[];
}

interface DirectiveChild {
  type: string;
  value?: string;
  data?: DirectiveData;
  children?: DirectiveChild[];
}

const ADMONITION_TYPES = ['note', 'tip', 'warning', 'danger', 'info'] as const;

function visitAdmonition(node: unknown): void {
  const directive = node as DirectiveNode;
  if (directive.type === 'containerDirective') {
    if (
      !ADMONITION_TYPES.includes(
        directive.name as (typeof ADMONITION_TYPES)[number],
      )
    ) {
      return;
    }

    directive.data ??= {};
    const { data } = directive;

    /*
     * Get title from the directive label or use default
     * e.g., :::tip Title Here or just :::tip
     */
    let title =
      directive.name.charAt(0).toUpperCase() + directive.name.slice(1);

    // Check if there's a custom title in the first text
    const firstChild = directive.children[0];
    if (firstChild?.data?.directiveLabel) {
      title = firstChild.children?.[0]?.value ?? title;
      // Remove the label paragraph from children
      directive.children.shift();
    }

    data.hName = 'div';
    data.hProperties = {
      class: `admonition admonition-${directive.name}`,
      'data-type': directive.name,
    };

    // Prepend a title element
    directive.children.unshift({
      type: 'paragraph',
      data: {
        hName: 'p',
        hProperties: { class: 'admonition-title' },
      },
      children: [{ type: 'text', value: title }],
    });
  }
}

function transformer(tree: Root): void {
  visit(tree, visitAdmonition);
}

/**
 * Remark plugin to transform Docusaurus-style admonitions (:::note, :::tip,
 * etc.) into custom HTML elements that can be styled with Tailwind.
 *
 * @returns A transformer function.
 */
export function remarkAdmonitions() {
  return transformer;
}
```

## File: `website/src/plugins/remark-fix-typedoc-links.ts`
```typescript
import type { Link, Root } from 'mdast';
import { visit } from 'unist-util-visit';

const markdownExtensionRe = /\.md$/;

function visitTypedocLink(node: Link): void {
  if (typeof node.url === 'string' && node.url.startsWith('/brain/knowledge/docs_legacy/api/')) {
    // Remove .md extension from API doc links
    node.url = node.url.replace(markdownExtensionRe, '');
  }
}

function transformer(tree: Root): void {
  visit(tree, 'link', visitTypedocLink);
}

/**
 * Remark plugin to fix typedoc-generated links. Removes .md extension from
 * internal API doc links.
 *
 * @returns A transformer function.
 */
export function remarkFixTypedocLinks() {
  return transformer;
}
```

## File: `website/src/plugins/remark-live-code.ts`
```typescript
import type { Code, Parent, Root } from 'mdast';
import { visit } from 'unist-util-visit';

interface MdxJsxAttribute {
  type: 'mdxJsxAttribute';
  name: string;
  value: string | null;
}

interface MdxJsxFlowElement {
  type: 'mdxJsxFlowElement';
  name: string;
  attributes: MdxJsxAttribute[];
  children: unknown[];
}

function visitLiveCode(
  node: Code,
  index: number | undefined,
  parent: Parent | undefined,
): void {
  // Check if the code block has 'live' in its meta
  if (node.meta?.includes('live') && index !== undefined && parent) {
    // Transform the code node into an MDX JSX element
    const code = node.value;

    /*
     * Create an mdxJsxFlowElement node for the LiveCode component
     * with client:visible for lazy hydration
     */
    const jsxNode: MdxJsxFlowElement = {
      type: 'mdxJsxFlowElement',
      name: 'LiveCode',
      attributes: [
        {
          type: 'mdxJsxAttribute',
          name: 'code',
          value: code,
        },
        {
          type: 'mdxJsxAttribute',
          name: 'client:visible',
          value: null,
        },
      ],
      children: [],
    };

    // Replace the code node with the JSX node
    parent.children.splice(index, 1, jsxNode as unknown as Code);
  }
}

function transformer(tree: Root): void {
  visit(tree, 'code', visitLiveCode);
}

/**
 * Remark plugin to transform code blocks with 'live' meta into LiveCode
 * components.
 *
 * Usage in markdown:
 *
 * ```js
 * const $ = cheerio.load('<h1>Hello</h1>');
 * return <>{$('h1').text()}</>;
 * ```
 *
 * @returns A transformer function.
 */
export function remarkLiveCode() {
  return transformer;
}
```

## File: `website/src/styles/global.css`
```css
@import "tailwindcss";

@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  src: url("/fonts/inter.woff") format("woff");
  unicode-range:
    U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC,
    U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF,
    U+FFFD;
}

@font-face {
  font-family: "Rubik";
  font-style: normal;
  font-weight: 400;
  src: url("/fonts/rubik.woff") format("woff");
  unicode-range:
    U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC,
    U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF,
    U+FFFD;
}

@theme {
  --color-primary: #e88c1f;
  --color-primary-dark: #d07418;
  --color-primary-light: #f0a040;
  --color-primary-lightest: #f5c376;
  --color-amber-50: #fffbeb;
  --color-amber-100: #fef3c7;
  --color-amber-900: #78350f;
  --color-amber-950: #451a03;

  --font-sans:
    "Rubik", system-ui, -apple-system, "Segoe UI", Roboto, Ubuntu, Cantarell,
    "Noto Sans", sans-serif;
  --font-heading: "Inter", var(--font-sans);
  --font-display: "DM Serif Display", Georgia, "Times New Roman", serif;
  --font-mono:
    "JetBrains Mono", "Fira Code", "Cascadia Code", Consolas, monospace;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-sans);
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: var(--font-heading);
  font-weight: 600;
}

/* ─── Landing page animations ─── */

@keyframes fade-up {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slide-in-right {
  from {
    opacity: 0;
    transform: translateX(32px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-8px);
  }
}

@keyframes pulse-glow {
  0%,
  100% {
    box-shadow: 0 0 20px rgba(232, 140, 31, 0.15);
  }
  50% {
    box-shadow: 0 0 40px rgba(232, 140, 31, 0.3);
  }
}

@keyframes grain {
  0%,
  100% {
    transform: translate(0, 0);
  }
  10% {
    transform: translate(-5%, -10%);
  }
  30% {
    transform: translate(3%, -15%);
  }
  50% {
    transform: translate(12%, 9%);
  }
  70% {
    transform: translate(9%, 4%);
  }
  90% {
    transform: translate(-1%, 7%);
  }
}

.animate-fade-up {
  animation: fade-up 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.animate-fade-in {
  animation: fade-in 0.6s ease both;
}

.animate-slide-in-right {
  animation: slide-in-right 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animation-delay-100 {
  animation-delay: 100ms;
}
.animation-delay-200 {
  animation-delay: 200ms;
}
.animation-delay-300 {
  animation-delay: 300ms;
}
.animation-delay-400 {
  animation-delay: 400ms;
}
.animation-delay-500 {
  animation-delay: 500ms;
}
.animation-delay-600 {
  animation-delay: 600ms;
}
.animation-delay-700 {
  animation-delay: 700ms;
}
.animation-delay-800 {
  animation-delay: 800ms;
}

/* Grain texture overlay */
.grain::before {
  content: "";
  position: absolute;
  inset: -50%;
  width: 200%;
  height: 200%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  background-size: 128px 128px;
  pointer-events: none;
  animation: grain 8s steps(10) infinite;
  z-index: 1;
}

/* ─── Prose styles for documentation ─── */
.prose {
  max-width: 65ch;
}

/* API docs need more room for tables */
.prose-wide {
  max-width: 90ch;
}

/* Hide the first h1 in docs content since the editorial header already shows it */
.docs-content > h1:first-child {
  display: none;
}

.prose h1,
.prose h2,
.prose h3,
.prose h4 {
  font-family: var(--font-heading);
  font-weight: 600;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}

.prose h1 {
  font-size: 2.25rem;
}

.prose h2 {
  font-size: 1.75rem;
}

.prose h3 {
  font-size: 1.375rem;
}

.prose p {
  margin-top: 1em;
  margin-bottom: 1em;
}

.prose a {
  color: var(--color-primary);
  text-decoration: underline;
}

.prose a:hover {
  color: var(--color-primary-dark);
}

.prose code {
  background-color: #f1f5f9;
  padding: 0.125rem 0.25rem;
  border-radius: 0.25rem;
  font-size: 0.875em;
}

.prose pre {
  background-color: #1e293b;
  color: #e2e8f0;
  padding: 1rem;
  border-radius: 0.5rem;
  overflow-x: auto;
  margin: 1rem 0;
}

.prose pre code {
  background-color: transparent;
  padding: 0;
  font-size: 0.875rem;
}

.prose ul,
.prose ol {
  margin-top: 1em;
  margin-bottom: 1em;
  padding-left: 1.5em;
}

.prose ul {
  list-style-type: disc;
}

.prose ol {
  list-style-type: decimal;
}

.prose li {
  margin-top: 0.25em;
  margin-bottom: 0.25em;
}

.prose blockquote {
  border-left: 4px solid var(--color-primary);
  padding-left: 1rem;
  margin: 1rem 0;
  color: #64748b;
  font-style: italic;
}

/* Table styles */
.prose table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.875rem;
  line-height: 1.5;
  overflow: hidden;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
}

.prose thead {
  background-color: #f8fafc;
  border-bottom: 2px solid #e2e8f0;
}

.prose th {
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #64748b;
  text-align: left;
  padding: 0.75rem 1rem;
}

.prose td {
  padding: 0.75rem 1rem;
  border-top: 1px solid #f1f5f9;
  vertical-align: top;
  color: #475569;
}

.prose tbody tr:hover {
  background-color: #f8fafc;
}

.prose td:first-child {
  font-weight: 500;
  white-space: nowrap;
}

/* Table link styling */
.prose td a {
  text-decoration: none;
  font-weight: 500;
}

.prose td a:hover {
  text-decoration: underline;
}

/* Inline code within tables — smaller */
.prose td code,
.prose th code {
  font-size: 0.8125rem;
  padding: 0.1rem 0.3rem;
}

/* Admonition styles */
.admonition {
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1.5rem 0;
}

.admonition-title {
  font-weight: 600;
  /* biome-ignore lint/complexity/noImportantStyles: Override Starlight defaults */
  margin: 0 0 0.5rem 0 !important;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
}

.admonition-note {
  background-color: #eff6ff;
  border-left: 4px solid #3b82f6;
}

.admonition-note .admonition-title {
  color: #1d4ed8;
}

.admonition-tip {
  background-color: #f0fdf4;
  border-left: 4px solid #22c55e;
}

.admonition-tip .admonition-title {
  color: #15803d;
}

.admonition-info {
  background-color: #f0f9ff;
  border-left: 4px solid #0ea5e9;
}

.admonition-info .admonition-title {
  color: #0369a1;
}

.admonition-warning {
  background-color: #fefce8;
  border-left: 4px solid #eab308;
}

.admonition-warning .admonition-title {
  color: #a16207;
}

.admonition-danger {
  background-color: #fef2f2;
  border-left: 4px solid #ef4444;
}

.admonition-danger .admonition-title {
  color: #b91c1c;
}

.admonition p:last-child {
  margin-bottom: 0;
}

.admonition code {
  background-color: rgba(0, 0, 0, 0.1);
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-primary: #f4a02f;
    --color-primary-dark: #f39313;
    --color-primary-light: #f5ad4b;
  }

  .prose code {
    background-color: #334155;
    color: #e2e8f0;
  }

  .prose table {
    border-color: #334155;
  }

  .prose thead {
    background-color: #1e293b;
    border-bottom-color: #334155;
  }

  .prose th {
    color: #94a3b8;
  }

  .prose td {
    border-top-color: #1e293b;
    color: #cbd5e1;
  }

  .prose tbody tr:hover {
    background-color: #1e293b;
  }

  .admonition-note {
    background-color: #1e3a5f;
  }

  .admonition-note .admonition-title {
    color: #60a5fa;
  }

  .admonition-tip {
    background-color: #14532d;
  }

  .admonition-tip .admonition-title {
    color: #4ade80;
  }

  .admonition-info {
    background-color: #0c4a6e;
  }

  .admonition-info .admonition-title {
    color: #38bdf8;
  }

  .admonition-warning {
    background-color: #422006;
  }

  .admonition-warning .admonition-title {
    color: #fbbf24;
  }

  .admonition-danger {
    background-color: #450a0a;
  }

  .admonition-danger .admonition-title {
    color: #f87171;
  }

  .admonition code {
    background-color: rgba(255, 255, 255, 0.1);
  }
}
```

