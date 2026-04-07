---
id: cheerio
type: knowledge
owner: OA_Triage
---
# cheerio
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: Readme.md
```md
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
[`outerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/outerHTML)
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
[browser-based DOM nodes](https://developer.mozilla.org/en-US/docs/Web/API/Node).
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

### File: biome.json
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

### File: CONTRIBUTING.md
```md
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

### File: eslint.config.js
```js
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

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

Only the latest release will receive security updates.

## Reporting a Vulnerability

To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security). Tidelift will
coordinate the fix and disclosure.

```

### File: src_DISTILLED.md
```md
---
id: src
type: distilled_knowledge
---
# src

## SWALLOW ENGINE DISTILLATION

### File: cheerio.spec.ts
```ts
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

      /
... [TRUNCATED]
```

### File: tsconfig.json
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

### File: tsconfig.typedoc.json
```json
{
  "extends": "./tsconfig.json",
  "exclude": ["*.config.ts", "*.spec.ts", "scripts/*", "website/*"]
}

```

### File: vitest.config.ts
```ts
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

### File: .github\issue_template.md
```md
<!-- Thanks for your interest in cheerio!

Please note that issues should be primarily used for tracking bugs and feature requests.
If you have a more general question, please consider consulting StackOverflow first:
https://stackoverflow.com/questions/tagged/cheerio

If you think you uncovered a bug, please try to provide a minimal example that triggers the behavior.
Please note that we will not investigate issues that perform HTTP requests, as the source might already have changed.
-->

```

### File: src\cheerio.spec.ts
```ts
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
        const
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
