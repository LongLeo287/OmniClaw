---
id: entities
type: knowledge
owner: OA_Triage
---
# entities
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "entities",
    "version": "8.0.0",
    "description": "Encode & decode XML and HTML entities with ease & speed",
    "keywords": [
        "html entities",
        "entity decoder",
        "entity encoding",
        "html decoding",
        "html encoding",
        "xml decoding",
        "xml encoding"
    ],
    "repository": {
        "type": "git",
        "url": "https://github.com/fb55/entities.git"
    },
    "funding": "https://github.com/fb55/entities?sponsor=1",
    "license": "BSD-2-Clause",
    "author": "Felix Boehm <me@feedic.com>",
    "sideEffects": false,
    "type": "module",
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "default": "./dist/index.js"
        },
        "./decode": {
            "types": "./dist/decode.d.ts",
            "default": "./dist/decode.js"
        },
        "./escape": {
            "types": "./dist/escape.d.ts",
            "default": "./dist/escape.js"
        }
    },
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "files": [
        "dist",
        "src",
        "!**/*.spec.ts"
    ],
    "scripts": {
        "benchmark": "node --import=tsx scripts/benchmark.ts",
        "build": "tsc",
        "build:docs": "typedoc --hideGenerator src/index.ts",
        "build:encode-trie": "node --import=tsx scripts/write-encode-map.ts",
        "build:trie": "node --import=tsx scripts/write-decode-map.ts",
        "format": "npm run format:es && npm run format:biome",
        "format:biome": "biome check --fix .",
        "format:es": "npm run lint:es -- --fix",
        "lint": "npm run lint:es && npm run lint:ts && npm run lint:biome",
        "lint:biome": "biome check .",
        "lint:es": "eslint .",
        "lint:ts": "tsc --noEmit -p tsconfig.eslint.json",
        "prepublishOnly": "npm run build",
        "test": "npm run test:vi && npm run lint",
        "test:vi": "vitest run"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.8",
        "@eslint/compat": "^2.0.3",
        "@feedic/eslint-config": "^0.3.1",
        "@types/he": "^1.2.3",
        "@types/node": "^25.5.0",
        "eslint": "^10.1.0",
        "eslint-config-biome": "^2.1.3",
        "globals": "^17.4.0",
        "he": "^1.2.0",
        "html-entities": "^2.6.0",
        "parse-entities": "^4.0.2",
        "tinybench": "^6.0.0",
        "tsx": "^4.21.0",
        "typedoc": "^0.28.17",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.57.1",
        "vitest": "^4.0.17"
    },
    "engines": {
        "node": ">=20.19.0"
    }
}

```

### File: readme.md
```md
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

If your target supports UTF-8, the `escapeUTF8` method is going to be your best
choice. Otherwise, use either `encodeHTML` or `encodeXML` based on whether
you're dealing with an HTML or an XML document.

You can have a look at the options for the `encode` and `decode` methods to see
everything you can configure.

> When should I use strict decoding?

When strict decoding, entities not terminated with a semicolon will be ignored.
This is helpful for decoding entities in legacy environments.

> Why should I use `entities` instead of alternative modules?

As of September 2025, `entities` is faster than other modules. Still, this is
not a differentiated space and other modules can catch up.

**More importantly**, you might already have `entities` in your dependency graph
(as a dependency of eg. `cheerio`, or `htmlparser2`), and including it directly
might not even increase your bundle size. The same is true for other entity
libraries, so have a look through your `node_modules` directory!

> Does `entities` support tree shaking?

Yes! Note that for best results, you should not use the `encode` and `decode`
functions, as they wrap around a number of other functions, all of which will
remain in the bundle. Instead, use the functions that you need directly.

---

## Acknowledgements

This library wouldn't be possible without the work of these individuals. Thanks
to

- [@mathiasbynens](https://github.com/mathiasbynens) for his explanations about
  character encodings, and his library `he`, which was one of the inspirations
  for `entities`
- [@inikulin](https://github.com/inikulin) for his work on optimized tries for
  decoding HTML entities for the `parse5` project
- [@mdevils](https://github.com/mdevils) for taking on the challenge of
  producing a quick entity library with his `html-entities` library. `entities`
  would be quite a bit slower if there wasn't any competition. Right now
  `entities` is on top, but we'll see how long that lasts!

---

License: BSD-2-Clause

## Security contact information

To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security). Tidelift will
coordinate the fix and disclosure.

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
    "formatter": {
        "enabled": true,
        "indentStyle": "space",
        "indentWidth": 4,
        "lineWidth": 80
    },
    "linter": {
        "enabled": true,
        "rules": {
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
                "noShadowRestrictedNames": "off",
                "noAssignInExpressions": "off",
                "noConstEnum": "off",
                "useAwait": "error"
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
            "recommended": true
        }
    },
    "assist": {
        "actions": {
            "source": {
                "organizeImports": "on"
            }
        },
        "enabled": true
    },
    "files": {
        "includes": ["**", "!maps/*.json", "!maps", "!**/.*"],
        "ignoreUnknown": true
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
    "name": "entities",
    "version": "8.0.0",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "entities",
            "version": "8.0.0",
            "license": "BSD-2-Clause",
            "devDependencies": {
                "@biomejs/biome": "^2.4.8",
                "@eslint/compat": "^2.0.3",
                "@feedic/eslint-config": "^0.3.1",
                "@types/he": "^1.2.3",
                "@types/node": "^25.5.0",
                "eslint": "^10.1.0",
                "eslint-config-biome": "^2.1.3",
                "globals": "^17.4.0",
                "he": "^1.2.0",
                "html-entities": "^2.6.0",
                "parse-entities": "^4.0.2",
                "tinybench": "^6.0.0",
                "tsx": "^4.21.0",
                "typedoc": "^0.28.17",
                "typescript": "^5.9.3",
                "typescript-eslint": "^8.57.1",
                "vitest": "^4.0.17"
            },
            "engines": {
                "node": ">=20.19.0"
            },
            "funding": {
                "url": "https://github.com/fb55/entities?sponsor=1"
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
        "node_modules/@esbuild/aix-ppc64": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.2.tgz",
            "integrity": "sha512-GZMB+a0mOMZs4MpDbj8RJp4cw+w1WV5NYD6xzgvzUJ5Ek2jerwfO2eADyI6ExDSUED+1X8aMbegahsJi+8mgpw==",
            "cpu": [
                "ppc64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "aix"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/android-arm": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.2.tgz",
            "integrity": "sha512-DVNI8jlPa7Ujbr1yjU2PfUSRtAUZPG9I1RwW4F4xFB1Imiu2on0ADiI/c3td+KmDtVKNbi+nffGDQMfcIMkwIA==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/android-arm64": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.2.tgz",
            "integrity": "sha512-pvz8ZZ7ot/RBphf8fv60ljmaoydPU12VuXHImtAs0XhLLw+EXBi2BLe3OYSBslR4rryHvweW5gmkKFwTiFy6KA==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/android-x64": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.2.tgz",
            "integrity": "sha512-z8Ank4Byh4TJJOh4wpz8g2vDy75zFL0TlZlkUkEwYXuPSgX8yzep596n6mT7905kA9uHZsf/o2OJZubl2l3M7A==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/darwin-arm64": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.2.tgz",
            "integrity": "sha512-davCD2Zc80nzDVRwXTcQP/28fiJbcOwvdolL0sOiOsbwBa72kegmVU0Wrh1MYrbuCL98Omp5dVhQFWRKR2ZAlg==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/darwin-x64": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.2.tgz",
            "integrity": "sha512-ZxtijOmlQCBWGwbVmwOF/UCzuGIbUkqB1faQRf5akQmxRJ1ujusWsb3CVfk/9iZKr2L5SMU5wPBi1UWbvL+VQA==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/freebsd-arm64": {
            "version": "0.27.2",
            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.2.tgz",
            "integrity": "sha512-lS/9CN+rgqQ9czogxlMcBMGd+l8Q3Nj1MFQwBZJyoEKI50XGxwuzznYdwcav6lpOGv5BqaZXqvBSiB/kJ5op+g==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "freebsd"
            ],
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@esbuild/freebsd-x64": {
            "version": "0.27.2",
            "resolved": "https://regi
... [TRUNCATED]
```

### File: tsconfig.eslint.json
```json
{
    "extends": "./tsconfig.json",
    "compilerOptions": {
        "rootDir": ".",
        "noEmit": true
    },
    "include": ["src", "scripts"],
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
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,
        "rootDir": "src",
        "outDir": "dist",

        /* Strict Type-Checking Options */
        "strict": true,

        /* Additional Checks */
        "exactOptionalPropertyTypes": true,
        "forceConsistentCasingInFileNames": true,
        "isolatedDeclarations": true,
        "isolatedModules": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitOverride": true,
        "noImplicitReturns": true,
        "noPropertyAccessFromIndexSignature": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,

        /* Module Resolution Options */
        "resolveJsonModule": true,
        "skipLibCheck": true
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

### File: scripts\benchmark.ts
```ts
import he from "he";
import * as htmlEntities from "html-entities";
import { parseEntities } from "parse-entities";
import { Bench } from "tinybench";
import * as entities from "../src/index.js";

const htmlEntitiesHtml5EncodeOptions: htmlEntities.EncodeOptions = {
    level: "html5",
    mode: "nonAsciiPrintable",
};

const heEscapeOptions = { useNamedReferences: true };

const encoders: [string, (stringToEncode: string) => string][] = [
    ["entities", (stringToEncode) => entities.encodeHTML(stringToEncode)],
    ["he", (stringToEncode) => he.encode(stringToEncode, heEscapeOptions)],
    [
        "html-entities",
        (stringToEncode) =>
            htmlEntities.encode(stringToEncode, htmlEntitiesHtml5EncodeOptions),
    ],
];

const htmlEntitiesHtml5DecodeOptions: htmlEntities.DecodeOptions = {
    level: "html5",
    scope: "body",
};

const decoders: [string, (stringToDecode: string) => string][] = [
    ["entities", (stringToDecode) => entities.decodeHTML(stringToDecode)],
    ["he", (stringToDecode) => he.decode(stringToDecode)],
    ["parse-entities", (stringToDecode) => parseEntities(stringToDecode)],
    [
        "html-entities",
        (stringToDecode) =>
            htmlEntities.decode(stringToDecode, htmlEntitiesHtml5DecodeOptions),
    ],
];

const htmlEntitiesXmlEncodeOptions: htmlEntities.EncodeOptions = {
    level: "xml",
    mode: "specialChars",
};

const escapers: [string, (escapee: string) => string][] = [
    ["entities", (escapee) => entities.escapeUTF8(escapee)],
    ["he", (escapee) => he.escape(escapee)],
    // Html-entities cannot escape, so we use its simplest mode.
    [
        "html-entities",
        (escapee) => htmlEntities.encode(escapee, htmlEntitiesXmlEncodeOptions),
    ],
];

const textToDecode = `This is a simple text &uuml;ber &#x${"?"
    .charCodeAt(0)
    .toString(16)}; something.`;

const textToEncode = `über & unter's sprießende <boo> ❤️👊😉`;

console.log(
    "Escaping results",
    escapers.map(([name, escape]) => [name, escape(textToEncode)]),
);

console.log(
    "Encoding results",
    encoders.map(([name, encode]) => [name, encode(textToEncode)]),
);

console.log(
    "Decoding results",
    decoders.map(([name, decode]) => [name, decode(textToDecode)]),
);

function printResults(title: string, bench: Bench) {
    console.log(`\n=== ${title} ===`);
    console.table(bench.table());
}

async function runCategory(
    title: string,
    input: string,
    tasks: [string, (s: string) => string][],
) {
    const bench = new Bench({ warmupTime: 1e3, time: 1e4 });
    for (const [name, run] of tasks) {
        bench.add(name, () => run(input));
    }
    await bench.run();
    printResults(title, bench);
}

await runCategory("Escaping", textToEncode, escapers);
await runCategory("Encoding", textToEncode, encoders);
await runCategory("Decoding", textToDecode, decoders);

```

### File: scripts\write-decode-map.ts
```ts
import * as fs from "node:fs";
import entityMap from "../maps/entities.json" with { type: "json" };
import legacyMap from "../maps/legacy.json" with { type: "json" };
import xmlMap from "../maps/xml.json" with { type: "json" };
import { encodeTrie } from "./trie/encode-trie.js";
import { getTrie } from "./trie/trie.js";

function encodeUint16ArrayToBase64LittleEndian(data: Uint16Array): string {
    const buffer = Buffer.from(data.buffer, data.byteOffset, data.byteLength);
    return buffer.toString("base64");
}

function generateFile(name: string, data: Uint16Array): string {
    const b64 = encodeUint16ArrayToBase64LittleEndian(data);
    return `// Generated using scripts/write-decode-map.ts

import { decodeBase64 } from "../internal/decode-shared.js";
/** Packed ${name.toUpperCase()} decode trie data. */
export const ${name}DecodeTree: Uint16Array = /* #__PURE__ */ decodeBase64(
    ${JSON.stringify(b64)},
);`;
}

function convertMapToBinaryTrie(
    name: "html" | "xml",
    map: Record<string, string>,
    legacy: Record<string, string>,
) {
    const encoded = new Uint16Array(encodeTrie(getTrie(map, legacy), 2));
    const code = `${generateFile(name, encoded)}\n`;
    fs.writeFileSync(
        new URL(`../src/generated/decode-data-${name}.ts`, import.meta.url),
        code,
    );
}

convertMapToBinaryTrie("xml", xmlMap, {});
convertMapToBinaryTrie("html", entityMap, legacyMap);

console.log("Done!");

```

### File: scripts\write-encode-map.ts
```ts
import { writeFileSync } from "node:fs";
import htmlMap from "../maps/entities.json" with { type: "json" };

interface TrieNode {
    /** The value, if the node has a value. */
    value?: string | undefined;
    /** A map with the next nodes, if there are any. */
    next?: Map<number, TrieNode> | undefined;
}

const htmlTrie = getTrie(htmlMap);
const serialized = serializeTrieToString(htmlTrie);

writeFileSync(
    new URL("../src/generated/encode-html.ts", import.meta.url),
    `// Generated using scripts/write-encode-map.ts
// This file contains a compact, single-string serialization of the HTML encode trie.
// Format per entry (sequence in ascending code point order using diff encoding):
//   <diffBase36>[&name;][{<children>}]  -- diff omitted when 0.
// "&name;" gives the entity value for the node. A following { starts a nested sub-map.
// Diffs use the same scheme as before: diff = currentKey - previousKey - 1, first entry stores key.

import {
    type EncodeTrieNode,
    parseEncodeTrie,
    } from "../internal/encode-shared.js";

/** Compact serialized HTML encode trie (intended to stay small & JS engine friendly) */
export const htmlTrie: Map<number, EncodeTrieNode> =
    /* #__PURE__ */ parseEncodeTrie(
        ${JSON.stringify(serialized)},
    );
`,
);

console.log("Done!");

function getTrie(map: Record<string, string>): Map<number, TrieNode> {
    const trie = new Map<number, TrieNode>();

    for (const entity of Object.keys(map)) {
        const decoded = map[entity];
        // Resolve the key
        let lastMap = trie;
        for (let index = 0; index < decoded.length - 1; index++) {
            const char = decoded.charCodeAt(index);
            const next = lastMap.get(char) ?? {};
            lastMap.set(char, next);
            lastMap = next.next ??= new Map();
        }
        const value = lastMap.get(decoded.charCodeAt(decoded.length - 1)) ?? {};
        value.value ??= entity;
        lastMap.set(decoded.charCodeAt(decoded.length - 1), value);
    }

    return trie;
}

function serializeTrieToString(trie: Map<number, TrieNode>): string {
    // @ts-expect-error `toSorted` requires a lib bump.
    const entries = [...trie.entries()].toSorted((a, b) => a[0] - b[0]);
    let out = "";
    let lastKey = -1;
    for (const [key, node] of entries) {
        if (lastKey === -1) {
            out += key.toString(36);
        } else {
            const diff = key - lastKey - 1;
            if (diff !== 0) out += diff.toString(36);
        }
        if (node.value) out += `&${node.value};`;
        if (node.next) {
            out += `{${serializeTrieToString(node.next)}}`;
        } else if (!node.value) {
            throw new Error("Invalid node: neither value nor next");
        }
        lastKey = key;
    }
    return out;
}

```

### File: src\decode-codepoint.ts
```ts
// Adapted from https://github.com/mathiasbynens/he/blob/36afe179392226cf1b6ccdb16ebbb7a5a844d93a/src/he.js#L106-L134

const decodeMap = new Map([
    [0, 65_533],
    // C1 Unicode control character reference replacements
    [128, 8364],
    [130, 8218],
    [131, 402],
    [132, 8222],
    [133, 8230],
    [134, 8224],
    [135, 8225],
    [136, 710],
    [137, 8240],
    [138, 352],
    [139, 8249],
    [140, 338],
    [142, 381],
    [145, 8216],
    [146, 8217],
    [147, 8220],
    [148, 8221],
    [149, 8226],
    [150, 8211],
    [151, 8212],
    [152, 732],
    [153, 8482],
    [154, 353],
    [155, 8250],
    [156, 339],
    [158, 382],
    [159, 376],
]);

/**
 * Replace the given code point with a replacement character if it is a
 * surrogate or is outside the valid range. Otherwise return the code
 * point unchanged.
 * @param codePoint Unicode code point to convert.
 */
export function replaceCodePoint(codePoint: number): number {
    if (
        (codePoint >= 0xd8_00 && codePoint <= 0xdf_ff) ||
        codePoint > 0x10_ff_ff
    ) {
        return 0xff_fd;
    }

    return decodeMap.get(codePoint) ?? codePoint;
}

```

### File: src\decode-stream.spec.ts
```ts
import { describe, expect, it, vi } from "vitest";
import { DecodingMode, EntityDecoder } from "./decode.js";
import { htmlDecodeTree } from "./generated/decode-data-html.js";
import { xmlDecodeTree } from "./generated/decode-data-xml.js";

describe("EntityDecoder Streaming", () => {
    it("should decode long entities split across chunks (char-by-char)", () => {
        const callback = vi.fn();
        const decoder = new EntityDecoder(htmlDecodeTree, callback);

        const entity = "&CounterClockwiseContourIntegral;";
        const codepoint = 8755; // ∳

        decoder.startEntity(DecodingMode.Strict);

        // Feed char by char starting after '&'
        let result: number;
        for (let index = 1; index < entity.length; index++) {
            const char = entity[index];
            result = decoder.write(char, 0);

            if (index < entity.length - 1) {
                expect(result).toBe(-1);
            } else {
                expect(result).toBe(entity.length);
            }
        }

        expect(callback).toHaveBeenCalledWith(codepoint, entity.length);
    });

    it("should decode distinct chunks", () => {
        const callback = vi.fn();
        const decoder = new EntityDecoder(htmlDecodeTree, callback);

        const part1 = "&CounterClockwise";
        const part2 = "ContourIntegral;";

        decoder.startEntity(DecodingMode.Strict);

        expect(decoder.write(part1.substring(1), 0)).toBe(-1);
        expect(decoder.write(part2, 0)).toBe(33);

        expect(callback).toHaveBeenCalledWith(8755, 33);
    });

    it("should decode xml entities (single chunk)", () => {
        const callback = vi.fn();
        const decoder = new EntityDecoder(xmlDecodeTree, callback);

        const data = "&amp;&gt;&amp&lt;&copy;&#x61;&#x62&#99;&#100&#101";

        for (let index = 0; index < data.length; index++) {
            if (data.charAt(index) !== "&") {
                continue;
            }

            decoder.startEntity(DecodingMode.Strict);
            const offset = decoder.write(data, index + 1);

            if (offset === -1) {
                break;
            }

            if (offset > 0) {
                index += offset - 1; // -1 because of the for loop increment
            }
        }

        decoder.end();

        expect(callback).toHaveBeenNthCalledWith(1, 38, 5); // &amp;
        expect(callback).toHaveBeenNthCalledWith(2, 62, 4); // &gt;
        // NOT &amp
        expect(callback).toHaveBeenNthCalledWith(3, 60, 4); // &lt;
        // NOT &copy;
        expect(callback).toHaveBeenNthCalledWith(4, 97, 6); // &#x61;
        // NOT &#x62
        expect(callback).toHaveBeenNthCalledWith(5, 99, 5); // &#99;
        /*
         * NOT &#100
         * NOT &#101
         */

        expect(callback).toHaveBeenCalledTimes(5);
    });

    it("should decode xml entities (char-by-char)", () => {
        const callback = vi.fn();
        const decoder = new EntityDecoder(xmlDecodeTree, callback);

        const data = "&amp;&gt;&amp&lt;&copy;&#x61;&#x62&#99;&#100&#101";

        let inEntity = false;
        for (let index = 0; index < data.length; index++) {
            const char = data[index];

            if (!inEntity) {
                if (char === "&") {
                    decoder.startEntity(DecodingMode.Strict);
                    inEntity = true;
                }
                continue;
            }

            const offset = decoder.write(char, 0);

            if (offset === -1) {
                if (char === "&") {
                    inEntity = false;
                    index -= 1; // Reprocess '&' as a new entity start.
                }
                continue;
            }

            inEntity = false;

            if (offset === 0) {
                index -= 1; // Reprocess current char outside the failed entity.
            }
        }

        decoder.end();

        expect(callback).toHaveBeenNthCalledWith(1, 38, 5); // &amp;
        expect(callback).toHaveBeenNthCalledWith(2, 62, 4); // &gt;
        // NOT &amp
        expect(callback).toHaveBeenNthCalledWith(3, 60, 4); // &lt;
        // NOT &copy;
        expect(callback).toHaveBeenNthCalledWith(4, 97, 6); // &#x61;
        // NOT &#x62
        expect(callback).toHaveBeenNthCalledWith(5, 99, 5); // &#99;
        /*
         * NOT &#100
         * NOT &#101
         */

        expect(callback).toHaveBeenCalledTimes(5);
    });
});

```

### File: src\decode.spec.ts
```ts
import { beforeEach, describe, expect, it, vi } from "vitest";
import * as entities from "./decode.js";

describe("Decode test", () => {
    const testcases = [
        { input: "&amp;amp;", output: "&amp;" },
        { input: "&amp;#38;", output: "&#38;" },
        { input: "&amp;#x26;", output: "&#x26;" },
        { input: "&amp;#X26;", output: "&#X26;" },
        { input: "&#38;#38;", output: "&#38;" },
        { input: "&#x26;#38;", output: "&#38;" },
        { input: "&#X26;#38;", output: "&#38;" },
        { input: "&#x3a;", output: ":" },
        { input: "&#x3A;", output: ":" },
        { input: "&#X3a;", output: ":" },
        { input: "&#X3A;", output: ":" },
        { input: "&#", output: "&#" },
        { input: "&>", output: "&>" },
        { input: "id=770&#anchor", output: "id=770&#anchor" },
    ];

    it.each(testcases)("should XML decode $input", ({ input, output }) =>
        expect(entities.decodeXML(input)).toBe(output));
    it.each(testcases)("should HTML decode $input", ({ input, output }) =>
        expect(entities.decodeHTML(input)).toBe(output));

    it("should HTML decode partial legacy entity", () => {
        expect(entities.decodeHTMLStrict("&timesbar")).toBe("&timesbar");
        expect(entities.decodeHTML("&timesbar")).toBe("×bar");
    });

    it("should HTML decode legacy entities according to spec", () =>
        expect(entities.decodeHTML("?&image_uri=1&ℑ=2&image=3")).toBe(
            "?&image_uri=1&ℑ=2&image=3",
        ));

    it("should back out of legacy entities", () =>
        expect(entities.decodeHTML("&ampa")).toBe("&a"));

    it("should not parse numeric entities in strict mode", () =>
        expect(entities.decodeHTMLStrict("&#55")).toBe("&#55"));

    it("should parse &nbsp followed by < (#852)", () =>
        expect(entities.decodeHTML("&nbsp<")).toBe("\u00A0<"));

    it("should decode trailing legacy entities", () => {
        expect(entities.decodeHTML("&timesbar;&timesbar")).toBe("⨱×bar");
    });

    it("should decode multi-byte entities", () => {
        expect(entities.decodeHTML("&NotGreaterFullEqual;")).toBe("≧̸");
    });

    it("should not decode legacy entities followed by text in attribute mode", () => {
        expect(
            entities.decodeHTML("&not", entities.DecodingMode.Attribute),
        ).toBe("¬");

        expect(
            entities.decodeHTML("&noti", entities.DecodingMode.Attribute),
        ).toBe("&noti");

        expect(
            entities.decodeHTML("&not=", entities.DecodingMode.Attribute),
        ).toBe("&not=");

        expect(entities.decodeHTMLAttribute("&notp")).toBe("&notp");
        expect(entities.decodeHTMLAttribute("&notP")).toBe("&notP");
        expect(entities.decodeHTMLAttribute("&not3")).toBe("&not3");
    });
});

describe("EntityDecoder", () => {
    let callback: ReturnType<typeof vi.fn<(cp: number, consumed: number) => void>>;
    let decoder: entities.EntityDecoder;

    beforeEach(() => {
        callback = vi.fn<(cp: number, consumed: number) => void>();
        decoder = new entities.EntityDecoder(entities.htmlDecodeTree, callback);
    });

    it("should decode decimal entities", () => {
        expect(decoder.write("&#5", 1)).toBe(-1);
        expect(decoder.write("8;", 0)).toBe(5);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(":".charCodeAt(0), 5);
    });

    it("should decode hex entities", () => {
        expect(decoder.write("&#x3a;", 1)).toBe(6);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(":".charCodeAt(0), 6);
    });

    it("should decode named entities", () => {
        expect(decoder.write("&amp;", 1)).toBe(5);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith("&".charCodeAt(0), 5);
    });

    it("should decode legacy entities", () => {
        decoder.startEntity(entities.DecodingMode.Legacy);

        expect(decoder.write("&amp", 1)).toBe(-1);

        expect(callback).toHaveBeenCalledTimes(0);

        expect(decoder.end()).toBe(4);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith("&".charCodeAt(0), 4);
    });

    it("should decode named entity written character by character", () => {
        for (const c of "amp") {
            expect(decoder.write(c, 0)).toBe(-1);
        }
        expect(decoder.write(";", 0)).toBe(5);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith("&".charCodeAt(0), 5);
    });

    it("should decode numeric entity written character by character", () => {
        for (const c of "#x3a") {
            expect(decoder.write(c, 0)).toBe(-1);
        }
        expect(decoder.write(";", 0)).toBe(6);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(":".charCodeAt(0), 6);
    });

    it("should decode hex entities across several chunks", () => {
        for (const chunk of ["#x", "cf", "ff", "d"]) {
            expect(decoder.write(chunk, 0)).toBe(-1);
        }

        expect(decoder.write(";", 0)).toBe(9);
        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(0xc_ff_fd, 9);
    });

    it("should not fail if nothing is written", () => {
        expect(decoder.end()).toBe(0);
        expect(callback).toHaveBeenCalledTimes(0);
    });

    /*
     * Focused tests exercising early exit paths inside a compact run in the real trie.
     * Discovered prefix: "zi" followed by compact run "grarr"; mismatching inside this run should
     * return 0 with no emission (result still 0).
     */
    describe("compact run mismatches", () => {
        it.each([
            ["first run character mismatch", "ziXgrar"],
            ["mismatch after one correct run char", "zigXarr"],
            ["mismatch after two correct run chars", "zigrXrr"],
        ])("%s returns 0", (_name, input) => {
            const callback = vi.fn<(cp: number, consumed: number) => void>();
            const d = new entities.EntityDecoder(
                entities.htmlDecodeTree,
                callback,
            );
            d.startEntity(entities.DecodingMode.Strict);
            expect(d.write(input, 0)).toBe(0);
            expect(callback).not.toHaveBeenCalled();
        });
    });

    describe("errors", () => {
        const errorHandlers = {
            missingSemicolonAfterCharacterReference: vi.fn(),
            absenceOfDigitsInNumericCharacterReference: vi.fn(),
            validateNumericCharacterReference: vi.fn(),
        };

        beforeEach(() => {
            errorHandlers.missingSemicolonAfterCharacterReference.mockClear();
            errorHandlers.absenceOfDigitsInNumericCharacterReference.mockClear();
            errorHandlers.validateNumericCharacterReference.mockClear();
            callback = vi.fn<(cp: number, consumed: number) => void>();
            decoder = new entities.EntityDecoder(
                entities.htmlDecodeTree,
                callback,
                errorHandlers,
            );
            decoder.startEntity(entities.DecodingMode.Legacy);
        });

        it("should produce an error for a named entity without a semicolon", () => {
            expect(decoder.write("&amp;", 1)).toBe(5);
            expect(callback).toHaveBeenCalledTimes(1);
            expect(callback).toHaveBeenCalledWith("&".charCodeAt(0), 5);
            expect(
                errorHandlers.missingSemicolonAfterCharacterReference,
            ).toHaveBeenCalledTimes(0);

            decoder.startEntity(entities.DecodingMode.Legacy);
            expect(decoder.write("&amp", 1)).toBe(-1);
            expect(decoder.end()).toBe(4);

            expect(callback).toHaveBeenCalledTimes(2);
            expect(callback).toHaveBeenLastCalledWith("&".charCodeAt(0), 4);
            expect(
                errorHandlers.missingSemicolonAfterCharacterReference,
            ).toHaveBeenCalledTimes(1);
        });

        it("should produce an error for a numeric entity without a semicolon", () => {
            expect(decoder.write("&#x3a", 1)).toBe(-1);
            expect(decoder.end()).toBe(5);

            expect(callback).toHaveBeenCalledTimes(1);
            expect(callback).toHaveBeenCalledWith(0x3a, 5);
            expect(
                errorHandlers.missingSemicolonAfterCharacterReference,
            ).toHaveBeenCalledTimes(1);
            expect(
                errorHandlers.absenceOfDigitsInNumericCharacterReference,
            ).toHaveBeenCalledTimes(0);
            expect(
                errorHandlers.validateNumericCharacterReference,
            ).toHaveBeenCalledTimes(1);
            expect(
                errorHandlers.validateNumericCharacterReference,
            ).toHaveBeenCalledWith(0x3a);
        });

        it("should produce an error for numeric entities without digits", () => {
            expect(decoder.write("&#", 1)).toBe(-1);
            expect(decoder.end()).toBe(0);

            expect(callback).toHaveBeenCalledTimes(0);
            expect(
                errorHandlers.missingSemicolonAfterCharacterReference,
            ).toHaveBeenCalledTimes(0);
            expect(
                errorHandlers.absenceOfDigitsInNumericCharacterReference,
            ).toHaveBeenCalledTimes(1);
            expect(
                errorHandlers.absenceOfDigitsInNumericCharacterReference,
            ).toHaveBeenCalledWith(2);
            expect(
                errorHandlers.validateNumericCharacterReference,
            ).toHaveBeenCalledTimes(0);
        });

        it("should produce an error for hex entities without digits", () => {
            expect(decoder.write("&#x", 1)).toBe(-1);
            expect(decoder.end()).toBe(0);

            expect(callback).toHaveBeenCalledTimes(0);
            expect(
                errorHandlers.missingSemicolonAfterCharacterReference,
            ).toHaveBeenCalledTimes(0);
            expect(
                errorHandlers.absenceOfDigitsInNumericCharacterReference,
            ).toHaveBeenCalledTimes(1);
            expect(
                errorHandlers.validateNumericCharacterReference,
            ).toHaveBeenCalledTimes(0);
        });
    });
});

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
