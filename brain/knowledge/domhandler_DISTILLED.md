---
id: domhandler
type: knowledge
owner: OA_Triage
---
# domhandler
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "type": "module",
    "name": "domhandler",
    "version": "6.0.1",
    "description": "Handler for htmlparser2 that turns pages into a dom",
    "author": "Felix Boehm <me@feedic.com>",
    "funding": {
        "type": "github",
        "url": "https://github.com/fb55/domhandler?sponsor=1"
    },
    "license": "BSD-2-Clause",
    "main": "dist/index.js",
    "types": "dist/index.d.ts",
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "default": "./dist/index.js"
        }
    },
    "sideEffects": false,
    "files": [
        "dist",
        "src",
        "!**/*.spec.ts"
    ],
    "scripts": {
        "build": "tsc",
        "build:docs": "typedoc --hideGenerator --plugin typedoc-plugin-missing-exports src/index.ts",
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
    "repository": {
        "type": "git",
        "url": "git://github.com/fb55/domhandler.git"
    },
    "keywords": [
        "dom",
        "htmlparser2"
    ],
    "engines": {
        "node": ">=20.19.0"
    },
    "dependencies": {
        "domelementtype": "^3.0.0"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.10",
        "@eslint/compat": "^2.0.3",
        "@feedic/eslint-config": "^0.3.1",
        "@types/node": "^25.5.2",
        "eslint": "^10.1.0",
        "eslint-config-biome": "^2.1.3",
        "htmlparser2": "^10.1.0",
        "typedoc": "^0.28.18",
        "typedoc-plugin-missing-exports": "^4.1.2",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.58.0",
        "vitest": "^4.1.2"
    }
}

```

### File: readme.md
```md
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

### File: package-lock.json
```json
{
    "name": "domhandler",
    "version": "6.0.1",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "domhandler",
            "version": "6.0.1",
            "license": "BSD-2-Clause",
            "dependencies": {
                "domelementtype": "^3.0.0"
            },
            "devDependencies": {
                "@biomejs/biome": "^2.4.10",
                "@eslint/compat": "^2.0.3",
                "@feedic/eslint-config": "^0.3.1",
                "@types/node": "^25.5.2",
                "eslint": "^10.1.0",
                "eslint-config-biome": "^2.1.3",
                "htmlparser2": "^10.1.0",
                "typedoc": "^0.28.18",
                "typedoc-plugin-missing-exports": "^4.1.2",
                "typescript": "^5.9.3",
                "typescript-eslint": "^8.58.0",
                "vitest": "^4.1.2"
            },
            "engines": {
                "node": ">=20.19.0"
            },
            "funding": {
                "type": "github",
                "url": "https://github.com/fb55/domhandler?sponsor=1"
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/biome/-/biome-2.4.10.tgz",
            "integrity": "sha512-xxA3AphFQ1geij4JTHXv4EeSTda1IFn22ye9LdyVPoJU19fNVl0uzfEuhsfQ4Yue/0FaLs2/ccVi4UDiE7R30w==",
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
                "@biomejs/cli-darwin-arm64": "2.4.10",
                "@biomejs/cli-darwin-x64": "2.4.10",
                "@biomejs/cli-linux-arm64": "2.4.10",
                "@biomejs/cli-linux-arm64-musl": "2.4.10",
                "@biomejs/cli-linux-x64": "2.4.10",
                "@biomejs/cli-linux-x64-musl": "2.4.10",
                "@biomejs/cli-win32-arm64": "2.4.10",
                "@biomejs/cli-win32-x64": "2.4.10"
            }
        },
        "node_modules/@biomejs/cli-darwin-arm64": {
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-darwin-arm64/-/cli-darwin-arm64-2.4.10.tgz",
            "integrity": "sha512-vuzzI1cWqDVzOMIkYyHbKqp+AkQq4K7k+UCXWpkYcY/HDn1UxdsbsfgtVpa40shem8Kax4TLDLlx8kMAecgqiw==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-darwin-x64/-/cli-darwin-x64-2.4.10.tgz",
            "integrity": "sha512-14fzASRo+BPotwp7nWULy2W5xeUyFnTaq1V13Etrrxkrih+ez/2QfgFm5Ehtf5vSjtgx/IJycMMpn5kPd5ZNaA==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-arm64/-/cli-linux-arm64-2.4.10.tgz",
            "integrity": "sha512-7MH1CMW5uuxQ/s7FLST63qF8B3Hgu2HRdZ7tA1X1+mk+St4JOuIrqdhIBnnyqeyWJNI+Bww7Es5QZ0wIc1Cmkw==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-arm64-musl/-/cli-linux-arm64-musl-2.4.10.tgz",
            "integrity": "sha512-WrJY6UuiSD/Dh+nwK2qOTu8kdMDlLV3dLMmychIghHPAysWFq1/DGC1pVZx8POE3ZkzKR3PUUnVrtZfMfaJjyQ==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-x64/-/cli-linux-x64-2.4.10.tgz",
            "integrity": "sha512-tZLvEEi2u9Xu1zAqRjTcpIDGVtldigVvzug2fTuPG0ME/g8/mXpRPcNgLB22bGn6FvLJpHHnqLnwliOu8xjYrg==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-linux-x64-musl/-/cli-linux-x64-musl-2.4.10.tgz",
            "integrity": "sha512-kDTi3pI6PBN6CiczsWYOyP2zk0IJI08EWEQyDMQWW221rPaaEz6FvjLhnU07KMzLv8q3qSuoB93ua6inSQ55Tw==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-win32-arm64/-/cli-win32-arm64-2.4.10.tgz",
            "integrity": "sha512-umwQU6qPzH+ISTf/eHyJ/QoQnJs3V9Vpjz2OjZXe9MVBZ7prgGafMy7yYeRGnlmDAn87AKTF3Q6weLoMGpeqdQ==",
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
            "version": "2.4.10",
            "resolved": "https://registry.npmjs.org/@biomejs/cli-win32-x64/-/cli-win32-x64-2.4.10.tgz",
            "integrity": "sha512-aW/JU5GuyH4uxMrNYpoC2kjaHlyJGLgIa3XkhPEZI0uKhZhJZU8BuEyJmvgzSPQNGozBwWjC972RaNdcJ9KyJg==",
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
            "version": "1.9.1",
            "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.9.1.tgz",
            "integrity": "sha512-mukuNALVsoix/w1BJwFzwXBN/dHeejQtuVzcDsfOEsdpCumXb/E9j8w11h5S54tT1xhifGfbbSm/ICrObRb3KA==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "@emnapi/wasi-threads": "1.2.0",
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@emnapi/runtime": {
            "version": "1.9.1",
            "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.9.1.tgz",
            "integrity": "sha512-VYi5+ZVLhpgK4hQ0TAjiQiZ6ol0oe4mBx7mVv7IflsiEp0OWoVsp/+f9Vc1hOhE0TtkORVrI1GvzyreqpgWtkA==",
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
        "node_modules/@eslint/compat": {
            "version": "2.0.3",
            "resolved": "https://registry.npmjs.org/@eslint/compat/-/compat-2.0.3.tgz",
            "integrity": "sha512-SjIJhGigp8hmd1YGIBwh7Ovri7Kisl42GYFjrOyHhtfYGGoLW6teYi/5p8W50KSsawUPpuLOSmsq1bD0NGQLBw==",
            "dev": true,
            "license": "Apache-2.0",
            "dependencies": {
                "@eslint/core": "^1.1.1"
            },
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            },
            "peerDependencies": {
                "eslint": "^8.40 || 9 || 10"
            },
            "peerDependenciesMeta": {
                "eslint": {
                    "optional": true
                }
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
                "@types/json-schema": "^
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
    "include": ["src"],
    "exclude": []
}

```

### File: tsconfig.json
```json
{
    "compilerOptions": {
        "target": "es2022",
        "module": "nodenext",
        "moduleResolution": "nodenext",
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,
        "outDir": "dist",

        "strict": true,

        "isolatedDeclarations": true,
        "isolatedModules": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,
        "noImplicitReturns": true,
        "noFallthroughCasesInSwitch": true,

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

### File: src\index.spec.ts
```ts
import { readdirSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { Parser, type ParserOptions } from "htmlparser2";
import { describe, expect, test } from "vitest";
import Handler, { type DomHandlerOptions, type Node } from "./index.js";

const basePath = resolve(fileURLToPath(import.meta.url), "..", "__fixtures__");

describe("DomHandler", () => {
    for (const { name, html, options = {}, expected } of readdirSync(basePath)
        .filter((name) => name.endsWith(".json"))
        .map((name) => resolve(basePath, name))
        .map((path) => JSON.parse(readFileSync(path, "utf8")))) {
        test(name, () => {
            const result = parse(html, options);

            compare(result, expected);
        });
    }
});

function parse(
    data: string,
    options: DomHandlerOptions & ParserOptions,
): Node[] {
    const results: Node[][] = [];

    const handler = new Handler((error: Error | null, actual: Node[]) => {
        expect(error).toBeNull();
        results.push(actual);
    }, options);

    const parser = new Parser(handler, options);

    // First, try to run the fixture via chunks
    for (let index = 0; index < data.length; index++) {
        parser.write(data.charAt(index));
    }

    parser.end();

    // Then parse everything
    parser.parseComplete(data);

    // Ensure streaming doesn't change anything.
    expect(results[0]).toEqual(results[1]);

    return results[0];
}

function compare(actual: unknown, expected: unknown) {
    if (
        typeof expected !== "object" ||
        expected === null ||
        typeof actual !== "object" ||
        actual === null
    ) {
        expect(actual).toBe(expected);
    } else {
        for (const property in expected) {
            expect(property in actual).toBeTruthy();
            compare(actual[property as never], expected[property as never]);
        }
    }
}

```

### File: src\index.ts
```ts
import { ElementType } from "domelementtype";
import {
    CDATA,
    type ChildNode,
    Comment,
    type DataNode,
    Document,
    Element,
    type ParentNode,
    ProcessingInstruction,
    Text,
} from "./node.js";

export * from "./node.js";

/**
 * Configuration options for `DomHandler`.
 */
export interface DomHandlerOptions {
    /**
     * Add a `startIndex` property to nodes.
     * When the parser is used in a non-streaming fashion, `startIndex` is an integer
     * indicating the position of the start of the node in the document.
     * @default false
     */
    withStartIndices?: boolean;

    /**
     * Add an `endIndex` property to nodes.
     * When the parser is used in a non-streaming fashion, `endIndex` is an integer
     * indicating the position of the end of the node in the document.
     * @default false
     */
    withEndIndices?: boolean;

    /**
     * Treat the markup as XML.
     * @default false
     */
    xmlMode?: boolean;
}

// Default options
const defaultOptions: DomHandlerOptions = {
    withStartIndices: false,
    withEndIndices: false,
    xmlMode: false,
};

interface ParserInterface {
    startIndex: number | null;
    endIndex: number | null;
}

type Callback = (error: Error | null, dom: ChildNode[]) => void;
type ElementCallback = (element: Element) => void;

/**
 * Event-based handler that builds a DOM tree from parser callbacks.
 */
export class DomHandler {
    /** The elements of the DOM */
    dom: ChildNode[] = [];

    /** The root element for the DOM */
    root: Document = new Document(this.dom);

    /** Called once parsing has completed. */
    private readonly callback: Callback | null;

    /** Settings for the handler. */
    private readonly options: DomHandlerOptions;

    /** Callback whenever a tag is closed. */
    private readonly elementCB: ElementCallback | null;

    /** Indicated whether parsing has been completed. */
    private done = false;

    /** Stack of open tags. */
    protected tagStack: ParentNode[] = [this.root];

    /** A data node that is still being written to. */
    protected lastNode: DataNode | null = null;

    /** Reference to the parser instance. Used for location information. */
    private parser: ParserInterface | null = null;

    /**
     * @param callback Called once parsing has completed.
     * @param options Settings for the handler.
     * @param elementCB Callback whenever a tag is closed.
     */
    constructor(
        callback?: Callback | null,
        options?: DomHandlerOptions | null,
        elementCB?: ElementCallback,
    ) {
        // Make it possible to skip arguments, for backwards-compatibility
        if (typeof options === "function") {
            elementCB = options;
            options = defaultOptions;
        }
        if (typeof callback === "object") {
            options = callback;
            callback = undefined;
        }

        this.callback = callback ?? null;
        this.options = options ?? defaultOptions;
        this.elementCB = elementCB ?? null;
    }

    onparserinit(parser: ParserInterface): void {
        this.parser = parser;
    }

    // Resets the handler back to starting state
    onreset(): void {
        this.dom = [];
        this.root = new Document(this.dom);
        this.done = false;
        this.tagStack = [this.root];
        this.lastNode = null;
        this.parser = null;
    }

    // Signals the handler that parsing is done
    onend(): void {
        if (this.done) return;
        this.done = true;
        this.parser = null;
        this.handleCallback(null);
    }

    onerror(error: Error): void {
        this.handleCallback(error);
    }

    onclosetag(): void {
        this.lastNode = null;

        const element = this.tagStack.pop() as Element;

        if (this.options.withEndIndices && this.parser) {
            element.endIndex = this.parser.endIndex;
        }

        if (this.elementCB) this.elementCB(element);
    }

    onopentag(name: string, attribs: { [key: string]: string }): void {
        const type = this.options.xmlMode ? ElementType.Tag : undefined;
        const element = new Element(name, attribs, undefined, type);
        this.addNode(element);
        this.tagStack.push(element);
    }

    ontext(data: string): void {
        const { lastNode } = this;

        if (lastNode && lastNode.type === ElementType.Text) {
            lastNode.data += data;
            if (this.options.withEndIndices && this.parser) {
                lastNode.endIndex = this.parser.endIndex;
            }
        } else {
            const node = new Text(data);
            this.addNode(node);
            this.lastNode = node;
        }
    }

    oncomment(data: string): void {
        if (this.lastNode && this.lastNode.type === ElementType.Comment) {
            this.lastNode.data += data;
            return;
        }

        const node = new Comment(data);
        this.addNode(node);
        this.lastNode = node;
    }

    oncommentend(): void {
        this.lastNode = null;
    }

    oncdatastart(): void {
        const text = new Text("");
        const node = new CDATA([text]);

        this.addNode(node);

        text.parent = node;
        this.lastNode = text;
    }

    oncdataend(): void {
        this.lastNode = null;
    }

    onprocessinginstruction(name: string, data: string): void {
        const node = new ProcessingInstruction(name, data);
        this.addNode(node);
    }

    protected handleCallback(error: Error | null): void {
        if (typeof this.callback === "function") {
            this.callback(error, this.dom);
        } else if (error) {
            throw error;
        }
    }

    protected addNode(node: ChildNode): void {
        const parent = this.tagStack[this.tagStack.length - 1];
        const previousSibling = parent.children[parent.children.length - 1] as
            | ChildNode
            | undefined;

        if (this.options.withStartIndices && this.parser) {
            node.startIndex = this.parser.startIndex;
        }

        if (this.options.withEndIndices && this.parser) {
            node.endIndex = this.parser.endIndex;
        }

        parent.children.push(node);

        if (previousSibling) {
            node.prev = previousSibling;
            previousSibling.next = node;
        }

        node.parent = parent;
        this.lastNode = null;
    }
}

export default DomHandler;

```

### File: src\node.spec.ts
```ts
import { ElementType } from "domelementtype";
import { Parser, type ParserOptions } from "htmlparser2";
import { describe, expect, it } from "vitest";
import Handler, {
    type DomHandlerOptions,
    type NodeWithChildren,
} from "./index.js";
import * as node from "./node.js";

describe("Nodes", () => {
    it("should serialize to a Jest snapshot", () => {
        const result = parse(
            "<html><!-- A Comment --><title>The Title</title><body>Hello world<input disabled type=text></body></html>",
        );
        expect(result).toMatchInlineSnapshot(`
            Document {
              "children": [
                <html>
                  <!-- A Comment -->
                  <title>
                    The Title
                  </title>
                  <body>
                    Hello world
                    <input
                      disabled=""
                      type="text"
                    />
                  </body>
                </html>,
              ],
              "endIndex": null,
              "next": null,
              "parent": null,
              "prev": null,
              "startIndex": null,
              "type": "root",
            }
        `);
    });

    it("should be cloneable", () => {
        const result = parse(
            `<html><!-- A Comment -->
                <!doctype html>
                <title>The Title</title>
                <body>Hello world<input disabled type=text></body>
                <script><![CDATA[secret script]]></script>
            </html>`,
        );
        expect(result.cloneNode(true)).toStrictEqual(result);
    });

    it("should not clone recursively if not asked to", () => {
        const result = parse("<div foo=bar><div><div>");
        expect(result.cloneNode(true)).toEqual(result);
        expect(result.cloneNode(false)).not.toEqual(result);
        expect(result.cloneNode()).toHaveProperty("children", []);
    });

    it("should clone startIndex and endIndex", () => {
        const result = parse("<div foo=bar><div><div>", {
            withStartIndices: true,
            withEndIndices: true,
        }).children[0];
        const clone = result.cloneNode(true);
        expect(clone.startIndex).toBe(0);
        expect(clone.endIndex).toBe(23);
    });

    it("should throw an error when cloning unsupported types", () => {
        class Doctype extends node.Node {
            type = ElementType.Doctype;
            nodeType = Number.NaN;
        }
        const element = new Doctype();
        expect(() => element.cloneNode()).toThrow(
            "Not implemented yet: doctype",
        );
    });

    it("should detect tag types", () => {
        const result = parse("<div foo=bar><div><div>").children[0];

        expect(node.isTag(result)).toBe(true);
        expect(node.hasChildren(result)).toBe(true);

        expect(node.isCDATA(result)).toBe(false);
        expect(node.isText(result)).toBe(false);
        expect(node.isComment(result)).toBe(false);
        expect(node.isDirective(result)).toBe(false);
        expect(node.isDocument(result)).toBe(false);
    });

    it("should support using tagged types", () => {
        // We want to make sure TS is happy about the tagged types.
        const parent: node.ParentNode = new node.Document([]);

        function setQuirks(element: node.ParentNode): void {
            if (element.type === ElementType.Root) {
                element["x-mode"] = "no-quirks";
            }
        }

        setQuirks(parent);

        expect(parent).toHaveProperty("x-mode", "no-quirks");
    });
});

type Options = DomHandlerOptions & ParserOptions;
function parse(data: string, options: Options = {}): NodeWithChildren {
    const handler = new Handler((error) => {
        if (error) throw error;
    }, options);

    const parser = new Parser(handler, options);

    parser.end(data);

    return handler.root;
}

```

### File: src\node.ts
```ts
import { ElementType, isTag as isTagRaw } from "domelementtype";

interface SourceCodeLocation {
    /** One-based line index of the first character. */
    startLine: number;
    /** One-based column index of the first character. */
    startCol: number;
    /** Zero-based first character index. */
    startOffset: number;
    /** One-based line index of the last character. */
    endLine: number;
    /** One-based column index of the last character. Points directly *after* the last character. */
    endCol: number;
    /** Zero-based last character index. Points directly *after* the last character. */
    endOffset: number;
}

interface TagSourceCodeLocation extends SourceCodeLocation {
    startTag?: SourceCodeLocation;
    endTag?: SourceCodeLocation;
}

/**
 * A node that can have children.
 */
export type ParentNode = Document | Element | CDATA;

/**
 * A node that can have a parent.
 */
export type ChildNode =
    | Text
    | Comment
    | ProcessingInstruction
    | Element
    | CDATA
    // `Document` is also used for document fragments, and can be a child node.
    | Document;

/**
 * Any node in the DOM tree.
 */
export type AnyNode = ParentNode | ChildNode;

/**
 * This object will be used as the prototype for Nodes when creating a
 * DOM-Level-1-compliant structure.
 */
export abstract class Node {
    /** The type of the node. */
    abstract readonly type: ElementType;

    /** Parent of the node */
    parent: ParentNode | null = null;

    /** Previous sibling */
    prev: ChildNode | null = null;

    /** Next sibling */
    next: ChildNode | null = null;

    /** The start index of the node. Requires `withStartIndices` on the handler to be `true. */
    startIndex: number | null = null;

    /** The end index of the node. Requires `withEndIndices` on the handler to be `true. */
    endIndex: number | null = null;

    /**
     * `parse5` source code location info.
     *
     * Available if parsing with parse5 and location info is enabled.
     */
    declare sourceCodeLocation?: SourceCodeLocation | null;

    // Read-only aliases

    /**
     * [DOM spec](https://dom.spec.whatwg.org/#dom-node-nodetype)-compatible
     * node {@link type}.
     */
    abstract readonly nodeType: number;

    // Read-write aliases for properties

    /**
     * Same as {@link parent}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get parentNode(): ParentNode | null {
        return this.parent;
    }

    set parentNode(parent: ParentNode | null) {
        this.parent = parent;
    }

    /**
     * Same as {@link prev}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get previousSibling(): ChildNode | null {
        return this.prev;
    }

    set previousSibling(previous: ChildNode | null) {
        this.prev = previous;
    }

    /**
     * Same as {@link next}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get nextSibling(): ChildNode | null {
        return this.next;
    }

    set nextSibling(next: ChildNode | null) {
        this.next = next;
    }

    /**
     * Clone this node, and optionally its children.
     * @param recursive Clone child nodes as well.
     * @returns A clone of the node.
     */
    cloneNode<T extends Node>(this: T, recursive = false): T {
        return cloneNode(this, recursive);
    }
}

/**
 * A node that contains some data.
 */
export abstract class DataNode extends Node {
    data: string;

    /**
     * @param data The content of the data node
     */
    constructor(data: string) {
        super();
        this.data = data;
    }

    /**
     * Same as {@link data}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get nodeValue(): string {
        return this.data;
    }

    set nodeValue(data: string) {
        this.data = data;
    }
}

/**
 * Text within the document.
 */
export class Text extends DataNode {
    type: ElementType.Text = ElementType.Text;

    get nodeType(): 3 {
        return 3;
    }
}

/**
 * Comments within the document.
 */
export class Comment extends DataNode {
    type: ElementType.Comment = ElementType.Comment;

    get nodeType(): 8 {
        return 8;
    }
}

/**
 * Processing instructions, including doc types.
 */
export class ProcessingInstruction extends DataNode {
    type: ElementType.Directive = ElementType.Directive;
    name: string;

    constructor(name: string, data: string) {
        super(data);
        this.name = name;
    }

    override get nodeType(): 1 {
        return 1;
    }

    /** If this is a doctype, the document type name (parse5 only). */
    "x-name"?: string;
    /** If this is a doctype, the document type public identifier (parse5 only). */
    "x-publicId"?: string;
    /** If this is a doctype, the document type system identifier (parse5 only). */
    "x-systemId"?: string;
}

/**
 * A node that can have children.
 */
export abstract class NodeWithChildren extends Node {
    children: ChildNode[];

    /**
     * @param children Children of the node. Only certain node types can have children.
     */
    constructor(children: ChildNode[]) {
        super();
        this.children = children;
    }

    // Aliases
    /** First child of the node. */
    get firstChild(): ChildNode | null {
        return this.children[0] ?? null;
    }

    /** Last child of the node. */
    get lastChild(): ChildNode | null {
        return this.children.length > 0
            ? this.children[this.children.length - 1]
            : null;
    }

    /**
     * Same as {@link children}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get childNodes(): ChildNode[] {
        return this.children;
    }

    set childNodes(children: ChildNode[]) {
        this.children = children;
    }
}

/**
 * CDATA nodes.
 */
export class CDATA extends NodeWithChildren {
    type: ElementType.CDATA = ElementType.CDATA;

    get nodeType(): 4 {
        return 4;
    }
}

/**
 * The root node of the document.
 */
export class Document extends NodeWithChildren {
    type: ElementType.Root = ElementType.Root;

    get nodeType(): 9 {
        return 9;
    }

    /** [Document mode](https://dom.spec.whatwg.org/#concept-document-limited-quirks) (parse5 only). */
    declare "x-mode"?: "no-quirks" | "quirks" | "limited-quirks";
}

/**
 * The description of an individual attribute.
 */
interface Attribute {
    name: string;
    value: string;
    namespace?: string;
    prefix?: string;
}

/**
 * An element within the DOM.
 */
export class Element extends NodeWithChildren {
    name: string;
    attribs: { [name: string]: string };
    type: ElementType.Tag | ElementType.Script | ElementType.Style;

    /**
     * @param name Name of the tag, eg. `div`, `span`.
     * @param attribs Object mapping attribute names to attribute values.
     * @param children Children of the node.
     * @param type Node type used for the new node instance.
     */
    constructor(
        name: string,
        attribs: { [name: string]: string },
        children: ChildNode[] = [],
        type:
            | ElementType.Tag
            | ElementType.Script
            | ElementType.Style = name === "script"
            ? ElementType.Script
            : name === "style"
              ? ElementType.Style
              : ElementType.Tag,
    ) {
        super(children);
        this.name = name;
        this.attribs = attribs;
        this.type = type;
    }

    get nodeType(): 1 {
        return 1;
    }

    /**
     * `parse5` source code location info, with start & end tags.
     *
     * Available if parsing with parse5 and location info is enabled.
     */
    declare sourceCodeLocation?: TagSourceCodeLocation | null;

    // DOM Level 1 aliases

    /**
     * Same as {@link name}.
     * [DOM spec](https://dom.spec.whatwg.org)-compatible alias.
     */
    get tagName(): string {
        return this.name;
    }

    set tagName(name: string) {
        this.name = name;
    }

    get attributes(): Attribute[] {
        return Object.keys(this.attribs).map((name) => ({
            name,
            value: this.attribs[name],
            namespace: this["x-attribsNamespace"]?.[name],
            prefix: this["x-attribsPrefix"]?.[name],
        }));
    }

    /** Element namespace (parse5 only). */
    namespace?: string;
    /** Element attribute namespaces (parse5 only). */
    "x-attribsNamespace"?: Record<string, string>;
    /** Element attribute namespace-related prefixes (parse5 only). */
    "x-attribsPrefix"?: Record<string, string>;
}

/**
 * Checks if `node` is an element node.
 * @param node Node to check.
 * @returns `true` if the node is an element node.
 */
export function isTag(node: Node): node is Element {
    return isTagRaw(node);
}

/**
 * Checks if `node` is a CDATA node.
 * @param node Node to check.
 * @returns `true` if the node is a CDATA node.
 */
export function isCDATA(node: Node): node is CDATA {
    return node.type === ElementType.CDATA;
}

/**
 * Checks if `node` is a text node.
 * @param node Node to check.
 * @returns `true` if the node is a text node.
 */
export function isText(node: Node): node is Text {
    return node.type === ElementType.Text;
}

/**
 * Checks if `node` is a comment node.
 * @param node Node to check.
 * @returns `true` if the node is a comment node.
 */
export function isComment(node: Node): node is Comment {
    return node.type === ElementType.Comment;
}

/**
 * Checks if `node` is a directive node.
 * @param node Node to check.
 * @returns `true` if the node is a directive node.
 */
export function isDirective(node: Node): node is ProcessingInstruction {
    return node.type === ElementType.Directive;
}

/**
 * Checks if `node` is a document node.
 * @param node Node to check.
 * @returns `true` if the node is a document node.
 */
export function isDocument(node: Node): node is Document {
    return node.type === ElementType.Root;
}

/**
 * Checks if `node` has children.
 * @param node Node to check.
 * @returns `true` if the node has children.
 */
export function hasChildren(node: Node): node is ParentNode {
    return Object.hasOwn(node, "children");
}

/**
 * Clone a node, and optionally its children.
 * @param node Node to clone.
 * @param recursive Clone child nodes as well.
 * @returns A clone of the node.
 */
export function cloneNode<T extends Node>(node: T, recursive = false): T {
    let result: Node;

    if (isText(node)) {
        result = new Text(node.data);
    } else if (isComment(node)) {
        result = new Comment(node.data);
    } else if (isTag(node)) {
        const children = recursive ? cloneChildren(node.children) : [];
        const clone = new Element(node.name, { ...node.attribs }, children);
        for (const child of children) {
            child.parent = clone;
        }

        if (node.namespace != null) {
            clone.namespace = node.namespace;
        }
        if (node["x-attribsNamespace"]) {
            clone["x-attribsNamespace"] = { ...node["x-attribsNamespace"] };
        }
        if (node["x-attribsPrefix"]) {
            clone["x-attribsPrefix"] = { ...node["x-attribsPrefix"] };
        }

        result = clone;
    } else if (isCDATA(node)) {
        const children = recursive ? cloneChildren(node.children) : [];
        const clone = new CDATA(children);
        for (const child of children) {
            child.parent = clone;
        }
        result = clone;
    } else if (isDocument(node)) {
        const children = recursive ? cloneChildren(node.children) : [];
        const clone = new Document(children);
        for (const child of children) {
            child.parent = clone;
        }

        if (node["x-mode"]) {
            clone["x-mode"] = node["x-mode"];
        }

        result = clone;
    } else if (isDirective(node)) {
        const instruction = new ProcessingInstruction(node.name, node.data);

        if (node["x-name"] != null) {
            instruction["x-name"] = node["x-name"];
            instruction["x-publicId"] = node["x-publicId"];
            instruction["x-systemId"] = node["x-systemId"];
        }

        result = instruction;
    } else {
        throw new Error(`Not implemented yet: ${node.type}`);
    }

    result.startIndex = node.startIndex;
    result.endIndex = node.endIndex;

    if (node.sourceCodeLocation != null) {
        result.sourceCodeLocation = node.sourceCodeLocation;
    }

    return result as T;
}

/**
 * Clone a list of child nodes.
 * @param childs The child nodes to clone.
 * @returns A list of cloned child nodes.
 */
function cloneChildren(childs: ChildNode[]): ChildNode[] {
    const children = childs.map((child) => cloneNode(child, true));

    for (let index = 1; index < children.length; index++) {
        children[index].prev = children[index - 1];
        children[index - 1].next = children[index];
    }

    return children;
}

```

