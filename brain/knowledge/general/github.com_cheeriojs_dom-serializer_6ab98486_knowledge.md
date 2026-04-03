---
id: github.com-cheeriojs-dom-serializer-6ab98486-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:38.766677
---

# KNOWLEDGE EXTRACT: github.com_cheeriojs_dom-serializer_6ab98486
> **Extracted on:** 2026-04-01 14:39:12
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524030/github.com_cheeriojs_dom-serializer_6ab98486

---

## File: `.gitignore`
```
node_modules/
coverage/
dist/
jsr.json
```

## File: `LICENSE`
```
Copyright © 2022 The Cheerio contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
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
| ------------------------------------------------------------- | ------------------------------------------------------- |
| [htmlparser2](https://github.com/fb55/htmlparser2)            | Fast & forgiving HTML/XML parser                        |
| [domhandler](https://github.com/fb55/domhandler)              | Handler for htmlparser2 that turns documents into a DOM |
| [domutils](https://github.com/fb55/domutils)                  | Utilities for working with domhandler's DOM             |
| [css-select](https://github.com/fb55/css-select)              | CSS selector engine, compatible with domhandler's DOM   |
| [cheerio](https://github.com/cheeriojs/cheerio)               | The jQuery API for domhandler's DOM                     |
| [dom-serializer](https://github.com/cheeriojs/dom-serializer) | Serializer for domhandler's DOM                         |

---

LICENSE: MIT
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

Only the last published version is supported.

## Reporting a Vulnerability

To report a security vulnerability,
please use the [Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.
```

## File: `biome.json`
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
    "indentStyle": "space"
  },
  "javascript": {
    "formatter": {}
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "complexity": {
        "noUselessStringConcat": "error",
        "noUselessUndefined": "error",
        "useSimplifiedLogicExpression": "error",
        "useWhile": "error"
      },
      "performance": {
        "useTopLevelRegex": "error"
      },
      "suspicious": {
        "noConstantBinaryExpressions": "error",
        "useAwait": "error"
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
        "useFilenamingConvention": "error",
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

## File: `eslint.config.mjs`
```
import { includeIgnoreFile } from '@eslint/compat';
import feedicFlatConfig from '@feedic/eslint-config';
import { commonTypeScriptRules } from '@feedic/eslint-config/typescript';
import tseslint from 'typescript-eslint';
import { defineConfig } from 'eslint/config';
import { fileURLToPath } from 'node:url';
import eslintConfigBiome from 'eslint-config-biome';

const gitignorePath = fileURLToPath(new URL('.gitignore', import.meta.url));

export default defineConfig([
  includeIgnoreFile(gitignorePath),
  {
    linterOptions: {
      reportUnusedDisableDirectives: 'error',
    },
  },
  {
    ignores: ['eslint.config.{js,cjs,mjs}'],
  },
  ...feedicFlatConfig,
  {
    files: [
        "**/*.ts"
    ],
    extends: [...tseslint.configs.recommended],
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: {
          "sourceType": "module",
          "project": "./tsconfig.eslint.json"
      },
    },
    rules: {
      ...commonTypeScriptRules,
    },
  },
  eslintConfigBiome
]);
```

## File: `package.json`
```json
{
    "type": "module",
    "name": "dom-serializer",
    "version": "3.0.0",
    "description": "render domhandler DOM nodes to a string",
    "author": "Felix Boehm <me@feedic.com>",
    "sideEffects": false,
    "keywords": [
        "html",
        "xml",
        "render"
    ],
    "repository": {
        "type": "git",
        "url": "git://github.com/cheeriojs/dom-serializer.git"
    },
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "default": "./dist/index.js"
        }
    },
    "files": [
        "dist",
        "src",
        "!**/*.spec.ts"
    ],
    "dependencies": {
        "domelementtype": "^3.0.0",
        "domhandler": "^6.0.0",
        "entities": "^8.0.0"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.6",
        "@eslint/compat": "^2.0.3",
        "@feedic/eslint-config": "^0.3.1",
        "@types/node": "^25.5.0",
        "cheerio": "^1.2.0",
        "eslint": "^10.0.3",
        "eslint-config-biome": "^2.1.3",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.57.1",
        "vitest": "^4.0.18"
    },
    "engines": {
        "node": ">=20.19.0"
    },
    "scripts": {
        "build": "tsc",
        "format": "npm run format:es && npm run format:biome",
        "format:biome": "biome check --write .",
        "format:es": "npm run lint:es -- --fix",
        "lint": "npm run lint:es && npm run lint:ts && npm run lint:biome",
        "lint:biome": "biome check .",
        "lint:es": "eslint .",
        "lint:ts": "tsc --noEmit -p tsconfig.eslint.json",
        "prepare": "npm run build",
        "test": "npm run test:vi && npm run lint",
        "test:vi": "vitest run"
    },
    "funding": {
        "type": "github",
        "url": "https://github.com/cheeriojs/dom-serializer?sponsor=1"
    },
    "license": "MIT"
}
```

## File: `tsconfig.eslint.json`
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

## File: `tsconfig.json`
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
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,

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

## File: `src/foreign-names.ts`
```typescript
/**
 * Mixed-case SVG and MathML element names recognized in foreign content.
 */
export const elementNames = new Map<string, string>(
  [
    "altGlyph",
    "altGlyphDef",
    "altGlyphItem",
    "animateColor",
    "animateMotion",
    "animateTransform",
    "clipPath",
    "feBlend",
    "feColorMatrix",
    "feComponentTransfer",
    "feComposite",
    "feConvolveMatrix",
    "feDiffuseLighting",
    "feDisplacementMap",
    "feDistantLight",
    "feDropShadow",
    "feFlood",
    "feFuncA",
    "feFuncB",
    "feFuncG",
    "feFuncR",
    "feGaussianBlur",
    "feImage",
    "feMerge",
    "feMergeNode",
    "feMorphology",
    "feOffset",
    "fePointLight",
    "feSpecularLighting",
    "feSpotLight",
    "feTile",
    "feTurbulence",
    "foreignObject",
    "glyphRef",
    "linearGradient",
    "radialGradient",
    "textPath",
  ].map((value) => [value.toLowerCase(), value]),
);
/**
 * Mixed-case SVG and MathML attribute names recognized in foreign content.
 */
export const attributeNames = new Map<string, string>(
  [
    "definitionURL",
    "attributeName",
    "attributeType",
    "baseFrequency",
    "baseProfile",
    "calcMode",
    "clipPathUnits",
    "diffuseConstant",
    "edgeMode",
    "filterUnits",
    "glyphRef",
    "gradientTransform",
    "gradientUnits",
    "kernelMatrix",
    "kernelUnitLength",
    "keyPoints",
    "keySplines",
    "keyTimes",
    "lengthAdjust",
    "limitingConeAngle",
    "markerHeight",
    "markerUnits",
    "markerWidth",
    "maskContentUnits",
    "maskUnits",
    "numOctaves",
    "pathLength",
    "patternContentUnits",
    "patternTransform",
    "patternUnits",
    "pointsAtX",
    "pointsAtY",
    "pointsAtZ",
    "preserveAlpha",
    "preserveAspectRatio",
    "primitiveUnits",
    "refX",
    "refY",
    "repeatCount",
    "repeatDur",
    "requiredExtensions",
    "requiredFeatures",
    "specularConstant",
    "specularExponent",
    "spreadMethod",
    "startOffset",
    "stdDeviation",
    "stitchTiles",
    "surfaceScale",
    "systemLanguage",
    "tableValues",
    "targetX",
    "targetY",
    "textLength",
    "viewBox",
    "viewTarget",
    "xChannelSelector",
    "yChannelSelector",
    "zoomAndPan",
  ].map((value) => [value.toLowerCase(), value]),
);
```

## File: `src/index.spec.ts`
```typescript
import { type CheerioOptions, load } from "cheerio";
import { describe, expect, it } from "vitest";
import render from "./index.js";

interface LoadingOptions extends CheerioOptions {
  _useHtmlParser2?: boolean;
  decodeEntities?: boolean;
  encodeEntities?: "utf8";
  selfClosingTags?: boolean;
  emptyAttrs?: boolean;
}

function html(
  preset: LoadingOptions,
  markup: string,
  options: LoadingOptions = {},
) {
  const options_ = { ...preset, ...options };
  const $ = load(markup, options_, true);
  return render($._root, options_);
}

function xml(markup: string, options: LoadingOptions = {}) {
  const options_ = { ...options, xmlMode: true };
  const $ = load(markup, options_, true);
  return render($._root, options_);
}

describe("render DOM parsed with htmlparser2", () => {
  // Only test applicable to the default setup
  describe("(html)", () => {
    const htmlFunction = html.bind(null, { _useHtmlParser2: true });
    /*
     * It doesn't really make sense for {decodeEntities: false}
     * since currently it will convert <hr class='blah'> into <hr class="blah"> anyway.
     */
    it("should handle double quotes within single quoted attributes properly", () => {
      const markup = "<hr class='an \"edge\" case' />";
      expect(htmlFunction(markup)).toStrictEqual(
        '<hr class="an &quot;edge&quot; case">',
      );
    });

    it("should escape entities to utf8 if requested", () => {
      const markup = '<a href="a < b &quot; & c">& " &lt; &gt;</a>';
      expect(
        html({ _useHtmlParser2: true, encodeEntities: "utf8" }, markup),
      ).toStrictEqual('<a href="a < b &quot; &amp; c">&amp; " &lt; &gt;</a>');
    });

    it("should stringify non-string attribute values before escaping", () => {
      const $ = load("<div></div>", { _useHtmlParser2: true } as CheerioOptions, true);
      const div = $("div")[0];

      (div.attribs as Record<string, unknown>).width = 42;

      expect(render($._root, { _useHtmlParser2: true } as LoadingOptions)).toStrictEqual(
        '<div width="42"></div>',
      );
    });
  });

  // Run html with default options
  describe(
    "(html, {})",
    testBody.bind(null, html.bind(null, { _useHtmlParser2: true })),
  );

  // Run html with turned off decodeEntities
  describe(
    "(html, {decodeEntities: false})",
    testBody.bind(
      null,
      html.bind(null, { _useHtmlParser2: true, decodeEntities: false }),
    ),
  );

  describe("(xml)", () => {
    it("should render CDATA correctly", () => {
      const markup =
        "<a> <b> <![CDATA[ asdf&asdf ]]> <c/> <![CDATA[ asdf&asdf ]]> </b> </a>";
      expect(xml(markup)).toStrictEqual(markup);
    });

    it('should append ="" to attributes with no value', () => {
      const markup = "<div dropdown-toggle>";
      expect(xml(markup)).toStrictEqual('<div dropdown-toggle=""/>');
    });

    it('should append ="" to boolean attributes with no value', () => {
      const markup = "<input disabled>";
      expect(xml(markup)).toStrictEqual('<input disabled=""/>');
    });

    it("should preserve XML prefixes on attributes", () => {
      const markup =
        '<div xmlns:ex="http://example.com/ns"><p ex:ample="attribute">text</p></div>';
      expect(xml(markup)).toStrictEqual(markup);
    });

    it("should preserve mixed-case XML elements and attributes", () => {
      const markup = '<svg viewBox="0 0 8 8"><radialGradient/></svg>';
      expect(xml(markup)).toStrictEqual(markup);
    });

    it("should encode entities in otherwise special tags", () => {
      expect(xml('<script>"<br/>"</script>')).toStrictEqual(
        "<script>&quot;<br/>&quot;</script>",
      );
    });

    it("should not encode entities if disabled", () => {
      const markup = '<script>"<br/>"</script>';
      expect(xml(markup, { decodeEntities: false })).toStrictEqual(markup);
    });

    it("should stringify non-string SVG attribute values before escaping", () => {
      const $ = load("<svg><rect/></svg>", { xmlMode: true }, true);
      const rect = $("rect")[0];

      (rect.attribs as Record<string, unknown>).width = 42;
      (rect.attribs as Record<string, unknown>).height = 24;

      expect(render($._root, { xmlMode: true })).toStrictEqual(
        '<svg><rect width="42" height="24"/></svg>',
      );
    });
  });
});

describe("(xml, {selfClosingTags: false})", () => {
  it("should render childless nodes with an explicit closing tag", () => {
    const markup = "<foo /><bar></bar>";
    expect(xml(markup, { selfClosingTags: false })).toStrictEqual(
      "<foo></foo><bar></bar>",
    );
  });
});

describe("(html, {selfClosingTags: true})", () => {
  it("should render <br /> tags correctly", () => {
    const markup = "<br />";
    expect(
      html(
        {
          _useHtmlParser2: true,
          decodeEntities: false,
          selfClosingTags: true,
        },
        markup,
      ),
    ).toStrictEqual(markup);
  });
});

describe("(html, {selfClosingTags: false})", () => {
  it("should render childless SVG nodes with an explicit closing tag", () => {
    const markup =
      '<svg><circle x="12" y="12"></circle><path d="123M"></path><polygon points="60,20 100,40 100,80 60,100 20,80 20,40"></polygon></svg>';
    expect(
      html(
        {
          _useHtmlParser2: true,
          decodeEntities: false,
          selfClosingTags: false,
        },
        markup,
      ),
    ).toStrictEqual(markup);
  });
});

function testBody(html: (input: string, options?: LoadingOptions) => string) {
  it("should render <br /> tags without a slash", () => {
    const markup = "<br />";
    expect(html(markup)).toStrictEqual("<br>");
  });

  it("should retain encoded HTML content within attributes", () => {
    const markup = '<hr class="cheerio &amp; node = happy parsing" />';
    expect(html(markup)).toStrictEqual(
      '<hr class="cheerio &amp; node = happy parsing">',
    );
  });

  it('should shorten the "checked" attribute when it contains the value "checked"', () => {
    const markup = "<input checked/>";
    expect(html(markup)).toStrictEqual("<input checked>");
  });

  it("should render empty attributes if asked for", () => {
    const markup = "<input checked/>";
    expect(html(markup, { emptyAttrs: true })).toStrictEqual(
      '<input checked="">',
    );
  });

  it('should not shorten the "name" attribute when it contains the value "name"', () => {
    const markup = '<input name="name"/>';
    expect(html(markup)).toStrictEqual('<input name="name">');
  });

  it('should not append ="" to attributes with no value', () => {
    const markup = "<div dropdown-toggle>";
    expect(html(markup)).toStrictEqual("<div dropdown-toggle></div>");
  });

  it("should render comments correctly", () => {
    const markup = "<!-- comment -->";
    expect(html(markup)).toStrictEqual("<!-- comment -->");
  });

  it("should render whitespace by default", () => {
    const markup =
      '<a href="./haha.html">hi</a> <a href="./blah.html">blah</a>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should preserve multiple hyphens in data attributes", () => {
    const markup = '<div data-foo-bar-baz="value"></div>';
    expect(html(markup)).toStrictEqual('<div data-foo-bar-baz="value"></div>');
  });

  it("should not encode characters in script tag", () => {
    const markup = '<script>alert("hello world")</script>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should not encode tags in script tag", () => {
    const markup = '<script>"<br>"</script>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should not encode json data", () => {
    const markup =
      '<script>var json = {"simple_value": "value", "value_with_tokens": "&quot;here & \'there\'&quot;"};</script>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should render childless SVG nodes with a closing slash in HTML mode", () => {
    const markup =
      '<svg><circle x="12" y="12"/><path d="123M"/><polygon points="60,20 100,40 100,80 60,100 20,80 20,40"/></svg>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should render childless MathML nodes with a closing slash in HTML mode", () => {
    const markup = "<math><infinity/></math>";
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should allow SVG elements to have children", () => {
    const markup =
      '<svg><circle cx="12" r="12"><title>dot</title></circle></svg>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should not include extra whitespace in SVG self-closed elements", () => {
    const markup = '<svg><image href="x.png"/>     </svg>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should fix-up bad nesting in SVG in HTML mode", () => {
    const markup = '<svg><g><image href="x.png"></svg>';
    expect(html(markup)).toStrictEqual(
      '<svg><g><image href="x.png"/></g></svg>',
    );
  });

  it("should preserve XML prefixed attributes on inline SVG nodes in HTML mode", () => {
    const markup =
      '<svg><text id="t" xml:lang="fr">Bonjour</text><use xlink:href="#t"/></svg>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should handle mixed-case SVG content in HTML mode", () => {
    const markup = '<svg viewBox="0 0 8 8"><radialGradient/></svg>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should render HTML content in SVG foreignObject in HTML mode", () => {
    const markup =
      '<svg><foreignObject requiredFeatures=""><img src="test.png" viewbox>text<svg viewBox="0 0 8 8"><circle r="3"/></svg></foreignObject></svg>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should render iframe nodes with a closing tag in HTML mode", () => {
    const markup = '<iframe src="test"></iframe>';
    expect(html(markup)).toStrictEqual(markup);
  });

  it("should encode double quotes in attribute", () => {
    const markup = `<img src="/" alt='title" onerror="alert(1)" label="x'>`;
    expect(html(markup)).toStrictEqual(
      '<img src="/" alt="title&quot; onerror=&quot;alert(1)&quot; label=&quot;x">',
    );
  });
}
```

## File: `src/index.ts`
```typescript
/*
 * Module dependencies
 */
import * as ElementType from "domelementtype";
import type {
  AnyNode,
  CDATA,
  Comment,
  Element,
  ProcessingInstruction,
  Text,
} from "domhandler";
import { encodeXML, escapeAttribute, escapeText } from "entities";

/**
 * Mixed-case SVG and MathML tags & attributes
 * recognized by the HTML parser.
 * @see https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inforeign
 */
import { attributeNames, elementNames } from "./foreign-names.js";

/**
 * Options for DOM serialization.
 */
export interface DomSerializerOptions {
  /**
   * Print an empty attribute's value.
   * @default xmlMode
   * @example With <code>emptyAttrs: false</code>: <code>&lt;input checked&gt;</code>
   * @example With <code>emptyAttrs: true</code>: <code>&lt;input checked=""&gt;</code>
   */
  emptyAttrs?: boolean;
  /**
   * Print self-closing tags for tags without contents. If `xmlMode` is set, this will apply to all tags.
   * Otherwise, only tags that are defined as self-closing in the HTML specification will be printed as such.
   * @default xmlMode
   * @example With <code>selfClosingTags: false</code>: <code>&lt;foo&gt;&lt;/foo&gt;&lt;br&gt;&lt;/br&gt;</code>
   * @example With <code>xmlMode: true</code> and <code>selfClosingTags: true</code>: <code>&lt;foo/&gt;&lt;br/&gt;</code>
   * @example With <code>xmlMode: false</code> and <code>selfClosingTags: true</code>: <code>&lt;foo&gt;&lt;/foo&gt;&lt;br /&gt;</code>
   */
  selfClosingTags?: boolean;
  /**
   * Treat the input as an XML document; enables the `emptyAttrs` and `selfClosingTags` options.
   *
   * If the value is `"foreign"`, it will try to correct mixed-case attribute names.
   * @default false
   */
  xmlMode?: boolean | "foreign";
  /**
   * Encode characters that are either reserved in HTML or XML.
   *
   * If `xmlMode` is `true` or the value not `'utf8'`, characters outside of the ASCII range will be encoded as well.
   * @default `decodeEntities`
   */
  encodeEntities?: boolean | "utf8";
  /**
   * Option inherited from parsing; will be used as the default value for `encodeEntities`.
   * @default true
   */
  decodeEntities?: boolean;
}

const unencodedElements = new Set([
  "style",
  "script",
  "xmp",
  "iframe",
  "noembed",
  "noframes",
  "plaintext",
  "noscript",
]);

function replaceQuotes(value: string): string {
  return value.replace(/"/g, "&quot;");
}

/**
 * Format attributes
 * @param attributes Attribute map to serialize.
 * @param options Options that control this operation.
 */
function formatAttributes(
  attributes: Record<string, unknown> | undefined,
  options: DomSerializerOptions,
) {
  if (!attributes) return;

  const encode =
    (options.encodeEntities ?? options.decodeEntities) === false
      ? replaceQuotes
      : !!options.xmlMode || options.encodeEntities !== "utf8"
        ? encodeXML
        : escapeAttribute;

  return Object.keys(attributes)
    .map((key) => {
      const value = attributes[key];
      const normalizedValue = value == null ? "" : String(value);

      if (options.xmlMode === "foreign") {
        /* Fix up mixed-case attribute names */
        key = attributeNames.get(key) ?? key;
      }

      if (!(options.emptyAttrs || options.xmlMode) && normalizedValue === "") {
        return key;
      }

      return `${key}="${encode(normalizedValue)}"`;
    })
    .join(" ");
}

/**
 * Self-enclosing tags
 */
const singleTag = new Set([
  "area",
  "base",
  "basefont",
  "br",
  "col",
  "command",
  "embed",
  "frame",
  "hr",
  "img",
  "input",
  "isindex",
  "keygen",
  "link",
  "meta",
  "param",
  "source",
  "track",
  "wbr",
]);

/**
 * Renders a DOM node or an array of DOM nodes to a string.
 *
 * Can be thought of as the equivalent of the `outerHTML` of the passed node(s).
 * @param node Node to be rendered.
 * @param options Changes serialization behavior
 */
export function render(
  node: AnyNode | ArrayLike<AnyNode>,
  options: DomSerializerOptions = {},
): string {
  const nodes = "length" in node ? node : [node];

  let output = "";
  let index = 0;
  while (index < nodes.length) {
    output += renderNode(nodes[index], options);
    index++;
  }

  return output;
}

export default render;

function renderNode(node: AnyNode, options: DomSerializerOptions): string {
  switch (node.type) {
    case ElementType.Root: {
      return render(node.children, options);
    }
    // @ts-expect-error We don't use `Doctype` yet
    case ElementType.Doctype:
    case ElementType.Directive: {
      return renderDirective(node);
    }
    case ElementType.Comment: {
      return renderComment(node);
    }
    case ElementType.CDATA: {
      return renderCdata(node);
    }
    case ElementType.Script:
    case ElementType.Style:
    case ElementType.Tag: {
      return renderTag(node, options);
    }
    case ElementType.Text: {
      return renderText(node, options);
    }
  }
}

const foreignModeIntegrationPoints = new Set([
  "mi",
  "mo",
  "mn",
  "ms",
  "mtext",
  "annotation-xml",
  "foreignObject",
  "desc",
  "title",
]);

const foreignElements = new Set(["svg", "math"]);

function renderTag(element: Element, options: DomSerializerOptions) {
  // Handle SVG / MathML in HTML
  if (options.xmlMode === "foreign") {
    /* Fix up mixed-case element names */
    element.name = elementNames.get(element.name) ?? element.name;
    /* Exit foreign mode at integration points */
    if (
      element.parent &&
      foreignModeIntegrationPoints.has((element.parent as Element).name)
    ) {
      options = { ...options, xmlMode: false };
    }
  }
  if (!options.xmlMode && foreignElements.has(element.name)) {
    options = { ...options, xmlMode: "foreign" };
  }

  let tag = `<${element.name}`;
  const attribs = formatAttributes(element.attribs, options);

  if (attribs) {
    tag += ` ${attribs}`;
  }

  if (
    element.children.length === 0 &&
    (options.xmlMode
      ? // In XML mode or foreign mode, and user hasn't explicitly turned off self-closing tags
        options.selfClosingTags !== false
      : // User explicitly asked for self-closing tags, even in HTML mode
        options.selfClosingTags && singleTag.has(element.name))
  ) {
    if (!options.xmlMode) tag += " ";
    tag += "/>";
  } else {
    tag += ">";
    if (element.children.length > 0) {
      tag += render(element.children, options);
    }

    if (!!options.xmlMode || !singleTag.has(element.name)) {
      tag += `</${element.name}>`;
    }
  }

  return tag;
}

function renderDirective(element: ProcessingInstruction) {
  return `<${element.data}>`;
}

function renderText(element: Text, options: DomSerializerOptions) {
  let data = element.data || "";

  // If entities weren't decoded, no need to encode them back
  if (
    (options.encodeEntities ?? options.decodeEntities) !== false &&
    !(
      !options.xmlMode &&
      element.parent &&
      unencodedElements.has((element.parent as Element).name)
    )
  ) {
    data =
      !!options.xmlMode || options.encodeEntities !== "utf8"
        ? encodeXML(data)
        : escapeText(data);
  }

  return data;
}

function renderCdata(element: CDATA) {
  return `<![CDATA[${(element.children[0] as Text).data}]]>`;
}

function renderComment(element: Comment) {
  return `<!--${element.data}-->`;
}
```

