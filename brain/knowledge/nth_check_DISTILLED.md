---
id: nth-check
type: knowledge
owner: OA_Triage
---
# nth-check
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "type": "module",
    "name": "nth-check",
    "version": "3.0.1",
    "description": "Parses and compiles CSS nth-checks to highly optimized functions.",
    "author": "Felix Boehm <me@feedic.com>",
    "license": "BSD-2-Clause",
    "sideEffects": false,
    "funding": {
        "type": "github",
        "url": "https://github.com/fb55/nth-check?sponsor=1"
    },
    "main": "dist/index.js",
    "types": "dist/index.d.ts",
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
    "repository": {
        "type": "git",
        "url": "https://github.com/fb55/nth-check"
    },
    "keywords": [
        "nth-child",
        "nth",
        "css"
    ],
    "bugs": {
        "url": "https://github.com/fb55/nth-check/issues"
    },
    "homepage": "https://github.com/fb55/nth-check",
    "engines": {
        "node": ">=20.19.0"
    },
    "dependencies": {
        "boolbase": "^2.0.0"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.10",
        "@eslint/compat": "^2.0.3",
        "@feedic/eslint-config": "^0.3.1",
        "@types/node": "^25.5.2",
        "eslint": "^10.1.0",
        "eslint-config-biome": "^2.1.3",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.58.0",
        "vitest": "^4.1.2"
    }
}

```

### File: README.md
```md
# nth-check [![Build Status](https://travis-ci.org/fb55/nth-check.svg)](https://travis-ci.org/fb55/nth-check)

Parses and compiles CSS nth-checks to highly optimized functions.

### About

This module can be used to parse & compile nth-checks, as they are found in CSS 3's `nth-child()` and `nth-last-of-type()`. It can be used to check if a given index matches a given nth-rule, or to generate a sequence of indices matching a given nth-rule.

`nth-check` focusses on speed, providing optimized functions for different kinds of nth-child formulas, while still following the [spec](http://www.w3.org/TR/css3-selectors/#nth-child-pseudo).

### API

```js
import nthCheck, { parse, compile } from "nth-check";
```

##### `nthCheck(formula)`

Parses and compiles a formula to a highly optimized function. Combination of `parse` and `compile`.

If the formula doesn't match any elements, it returns [`boolbase`](https://github.com/fb55/boolbase)'s `falseFunc`. Otherwise, a function accepting an _index_ is returned, which returns whether or not the passed _index_ matches the formula.

**Note**: The nth-rule starts counting at `1`, the returned function at `0`.

**Example:**

```js
const check = nthCheck("2n+3");

check(0); // `false`
check(1); // `false`
check(2); // `true`
check(3); // `false`
check(4); // `true`
check(5); // `false`
check(6); // `true`
```

##### `parse(formula)`

Parses the expression, throws an `Error` if it fails. Otherwise, returns an array containing the integer step size and the integer offset of the nth rule.

**Example:**

```js
parse("2n+3"); // [2, 3]
```

##### `compile([a, b])`

Takes an array with two elements (as returned by `.parse`) and returns a highly optimized function.

**Example:**

```js
const check = compile([2, 3]);

check(0); // `false`
check(1); // `false`
check(2); // `true`
check(3); // `false`
check(4); // `true`
check(5); // `false`
check(6); // `true`
```

##### `generate([a, b])`

Returns a function that produces a monotonously increasing sequence of indices.

If the sequence has an end, the returned function will return `null` after the last index in the sequence.

**Example:** An always increasing sequence

```js
const gen = nthCheck.generate([2, 3]);

gen(); // `1`
gen(); // `3`
gen(); // `5`
gen(); // `8`
gen(); // `11`
```

**Example:** With an end value

```js
const gen = nthCheck.generate([-2, 5]);

gen(); // 0
gen(); // 2
gen(); // 4
gen(); // null
```

##### `sequence(formula)`

Parses and compiles a formula to a generator that produces a sequence of indices. Combination of `parse` and `generate`.

**Example:** An always increasing sequence

```js
const gen = nthCheck.sequence("2n+3");

gen(); // `1`
gen(); // `3`
gen(); // `5`
gen(); // `8`
gen(); // `11`
```

**Example:** With an end value

```js
const gen = nthCheck.sequence("-2n+5");

gen(); // 0
gen(); // 2
gen(); // 4
gen(); // null
```

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
        "includes": [
            "**/*.{ts,md,json,yml}",
            "!node_modules",
            "!coverage",
            "!lib",
            "!**/.*"
        ]
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
    "name": "nth-check",
    "version": "3.0.1",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "nth-check",
            "version": "3.0.1",
            "license": "BSD-2-Clause",
            "dependencies": {
                "boolbase": "^2.0.0"
            },
            "devDependencies": {
                "@biomejs/biome": "^2.4.10",
                "@eslint/compat": "^2.0.3",
                "@feedic/eslint-config": "^0.3.1",
                "@types/node": "^25.5.2",
                "eslint": "^10.1.0",
                "eslint-config-biome": "^2.1.3",
                "typescript": "^5.9.3",
                "typescript-eslint": "^8.58.0",
                "vitest": "^4.1.2"
            },
            "engines": {
                "node": ">=20.19.0"
            },
            "funding": {
                "type": "github",
                "url": "https://github.com/fb55/nth-check?sponsor=1"
            }
        },
        "node_modules/@aashutoshrathi/word-wrap": {
            "version": "1.2.6",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
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
        "node_modules/@eslint-community/regexpp": {
            "version": "4.12.2",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
            }
        },
        "node_modules/@eslint/compat": {
            "version": "2.0.3",
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
                "eslint": {
                    "optional": true
                }
            }
        },
        "node_modules/@eslint/object-schema": {
            "version": "3.0.3",
            "dev": true,
            "license": "Apache-2.0",
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@eslint/plugin-kit": {
            "version": "0.6.1",
            "dev": true,
            "license": "Apache-2.0",
            "dependencies": {
                "@eslint/core": "^1.1.1",
                "levn": "^0.4.1"
            },
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@feedic/eslint-config": {
            "version": "0.3.1",
            "resolved": "https://registry.npmjs.org/@feedic/eslint-config/-/eslint-config-0.3.1.tgz",
            "integrity": "sha512-CBDfjWp629dQs4IaZVsQdeMVN2lPyKSVaitxnr/Vb5wz7lXwGX0h9h4Rn9nQ4O5OdgK4KIxftlD+4AnDdZfNpw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@eslint/js": "^10.0.1",
                "eslint-plugin-jsdoc": "^62.8.0",
                "eslint-plugin-n": "^17.24.0",
                "eslint-plugin-package-json": "^0.90.1",
                "eslint-plugin-unicorn"
... [TRUNCATED]
```

### File: tsconfig.eslint.json
```json
{
    "extends": "./tsconfig.json",
    "compilerOptions": {
        "rootDir": ".",
        "noEmit": true,
        "isolatedDeclarations": false
    },
    "include": ["src", "test"],
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

        "forceConsistentCasingInFileNames": true,
        "isolatedModules": true,
        "isolatedDeclarations": true,
        "noFallthroughCasesInSwitch": true,
        "noImplicitOverride": true,
        "noImplicitReturns": true,
        "noPropertyAccessFromIndexSignature": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,

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

### File: src\compile.spec.ts
```ts
import { describe, expect, it } from "vitest";
import { valid } from "./__fixtures__/rules.js";
import nthCheck, { compile, generate, sequence } from "./index.js";

const valueArray = Array.from({ length: 2e3 }, (_, index) => index);

/**
 * Iterate through all possible values. This is adapted from qwery,
 * and uses a more intuitive way to process all elements.
 * @param rule A tuple [a, b] representing an nth-rule, as returned by `parse`.
 * @param rule."0" The `a` value from the tuple.
 * @param rule."1" The `b` value from the tuple.
 */
function slowNth([a, b]: [number, number]): number[] {
    if (a === 0 && b > 0) return [b - 1];

    return valueArray.filter((value) => {
        for (
            let index = b;
            a > 0 ? index <= valueArray.length : index >= 1;
            index += a
        ) {
            if (value === valueArray[index - 1]) return true;
        }
        return false;
    });
}

describe("parse", () => {
    it("compile & run all valid", () => {
        for (const [, parsed] of valid) {
            const filtered = valueArray.filter(compile(parsed));
            const iterated = slowNth(parsed);

            expect(filtered).toStrictEqual(iterated);
        }
    });

    it("parse, compile & run all valid", () => {
        for (const [rule, parsed] of valid) {
            const filtered = valueArray.filter(nthCheck(rule));
            const iterated = slowNth(parsed);

            expect([filtered, rule]).toStrictEqual([iterated, rule]);
        }
    });
});

describe("generate", () => {
    it("should return a function", () => {
        expect(generate([1, 2])).toBeInstanceOf(Function);
    });

    it("should only return valid values", () => {
        for (const [, parsed] of valid) {
            const gen = generate(parsed);
            const check = compile(parsed);
            let value = gen();

            for (let index = 0; index < 1e3; index++) {
                // Should pass the check iff `i` is the next value.
                expect(value === index).toBe(check(index));

                if (value === index) {
                    value = gen();
                }
            }
        }
    });

    it("should produce an increasing sequence", () => {
        const gen = generate([2, 2]);

        expect(gen()).toBe(1);
        expect(gen()).toBe(3);
        expect(gen()).toBe(5);
        expect(gen()).toBe(7);
        expect(gen()).toBe(9);
    });

    it("should produce an increasing sequence for a negative `n`", () => {
        const gen = generate([-1, 2]);

        expect(gen()).toBe(0);
        expect(gen()).toBe(1);
        expect(gen()).toBe(null);
    });

    it("should not produce any values for `-n`", () => {
        const gen = generate([-1, 0]);

        expect(gen()).toBe(null);
    });

    it("should parse selectors with `sequence`", () => {
        const gen = sequence("-2n+5");

        expect(gen()).toBe(0);
        expect(gen()).toBe(2);
        expect(gen()).toBe(4);
        expect(gen()).toBe(null);
    });
});

```

### File: src\compile.ts
```ts
import * as boolbase from "boolbase";

/**
 * Returns a function that checks if an elements index matches the given rule
 * highly optimized to return the fastest solution.
 * @param parsed A tuple [a, b], as returned by `parse`.
 * @returns A highly optimized function that returns whether an index matches the nth-check.
 * @example
 *
 * ```js
 * const check = nthCheck.compile([2, 3]);
 *
 * check(0); // `false`
 * check(1); // `false`
 * check(2); // `true`
 * check(3); // `false`
 * check(4); // `true`
 * check(5); // `false`
 * check(6); // `true`
 * ```
 */
export function compile(
    parsed: [a: number, b: number],
): (index: number) => boolean {
    const a = parsed[0];
    // Subtract 1 from `b`, to convert from one- to zero-indexed.
    const b = parsed[1] - 1;

    /*
     * When `b <= 0`, `a * n` won't be lead to any matches for `a < 0`.
     * Besides, the specification states that no elements are
     * matched when `a` and `b` are 0.
     *
     * `b < 0` here as we subtracted 1 from `b` above.
     */
    if (b < 0 && a <= 0) return boolbase.falseFunc;

    // When `a` is in the range -1..1, it matches any element (so only `b` is checked).
    if (a === -1) return (index) => index <= b;
    if (a === 0) return (index) => index === b;
    // When `b <= 0` and `a === 1`, they match any element.
    if (a === 1) return b < 0 ? boolbase.trueFunc : (index) => index >= b;

    /*
     * Otherwise, modulo can be used to check if there is a match.
     *
     * Modulo doesn't care about the sign, so let's use `a`s absolute value.
     */
    const absA = Math.abs(a);
    // Get `b mod a`, + a if this is negative.
    const bModulo = ((b % absA) + absA) % absA;

    return a > 1
        ? (index) => index >= b && index % absA === bModulo
        : (index) => index <= b && index % absA === bModulo;
}

/**
 * Returns a function that produces a monotonously increasing sequence of indices.
 *
 * If the sequence has an end, the returned function will return `null` after
 * the last index in the sequence.
 * @param parsed A tuple [a, b], as returned by `parse`.
 * @returns A function that produces a sequence of indices.
 * @example <caption>Always increasing (2n+3)</caption>
 *
 * ```js
 * const gen = nthCheck.generate([2, 3])
 *
 * gen() // `1`
 * gen() // `3`
 * gen() // `5`
 * gen() // `8`
 * gen() // `11`
 * ```
 * @example <caption>With end value (-2n+10)</caption>
 *
 * ```js
 *
 * const gen = nthCheck.generate([-2, 5]);
 *
 * gen() // 0
 * gen() // 2
 * gen() // 4
 * gen() // null
 * ```
 */
export function generate(parsed: [a: number, b: number]): () => number | null {
    const a = parsed[0];
    // Subtract 1 from `b`, to convert from one- to zero-indexed.
    let b = parsed[1] - 1;

    let n = 0;

    // Make sure to always return an increasing sequence
    if (a < 0) {
        const aPos = -a;
        // Get `b mod a`
        const minValue = ((b % aPos) + aPos) % aPos;
        return () => {
            const value = minValue + aPos * n++;

            return value > b ? null : value;
        };
    }

    if (a === 0)
        return b < 0
            ? // There are no result — always return `null`
              () => null
            : // Return `b` exactly once
              () => (n++ === 0 ? b : null);

    if (b < 0) {
        b += a * Math.ceil(-b / a);
    }

    return () => a * n++ + b;
}

```

### File: src\index.ts
```ts
import { compile, generate } from "./compile.js";
import { parse } from "./parse.js";

/**
 * Parses and compiles a formula to a highly optimized function.
 * Combination of {@link parse} and {@link compile}.
 *
 * If the formula doesn't match any elements,
 * it returns [`boolbase`](https://github.com/fb55/boolbase)'s `falseFunc`.
 * Otherwise, a function accepting an _index_ is returned, which returns
 * whether or not the passed _index_ matches the formula.
 *
 * Note: The nth-rule starts counting at `1`, the returned function at `0`.
 * @param formula The formula to compile.
 * @example
 * const check = nthCheck("2n+3");
 *
 * check(0); // `false`
 * check(1); // `false`
 * check(2); // `true`
 * check(3); // `false`
 * check(4); // `true`
 * check(5); // `false`
 * check(6); // `true`
 */
export default function nthCheck(formula: string): (index: number) => boolean {
    return compile(parse(formula));
}

/**
 * Parses and compiles a formula to a generator that produces a sequence of indices.
 * Combination of {@link parse} and {@link generate}.
 * @param formula The formula to compile.
 * @returns A function that produces a sequence of indices.
 * @example <caption>Always increasing</caption>
 *
 * ```js
 * const gen = nthCheck.sequence('2n+3')
 *
 * gen() // `1`
 * gen() // `3`
 * gen() // `5`
 * gen() // `8`
 * gen() // `11`
 * ```
 * @example <caption>With end value</caption>
 *
 * ```js
 *
 * const gen = nthCheck.sequence('-2n+5');
 *
 * gen() // 0
 * gen() // 2
 * gen() // 4
 * gen() // null
 * ```
 */
export function sequence(formula: string): () => number | null {
    return generate(parse(formula));
}

export { compile, generate } from "./compile.js";
export { parse } from "./parse.js";

```

### File: src\parse.spec.ts
```ts
import { describe, expect, it } from "vitest";
import { invalid, valid } from "./__fixtures__/rules.js";
import { parse } from "./parse.js";

describe("parse", () => {
    it("parse invalid", () => {
        for (const formula of invalid) {
            expect(() => parse(formula)).toThrowError(Error);
        }
    });

    it("parse valid", () => {
        for (const [formula, result] of valid) {
            expect(parse(formula)).toStrictEqual(result);
        }
    });
});

```

### File: src\parse.ts
```ts
// Following http://www.w3.org/TR/css3-selectors/#nth-child-pseudo

// Whitespace as per https://www.w3.org/TR/selectors-3/#lex is " \t\r\n\f"
const whitespace = new Set([9, 10, 12, 13, 32]);
const ZERO = "0".charCodeAt(0);
const NINE = "9".charCodeAt(0);

/**
 * Parses an expression.
 * @param formula CSS nth-formula to parse.
 * @throws {Error} An `Error` if parsing fails.
 * @returns An array containing the integer step size and the integer offset of the nth rule.
 * @example nthCheck.parse("2n+3"); // returns [2, 3]
 */
export function parse(formula: string): [a: number, b: number] {
    formula = formula.trim().toLowerCase();

    switch (formula) {
        case "even": {
            return [2, 0];
        }
        case "odd": {
            return [2, 1];
        }
    }

    // Parse [ ['-'|'+']? INTEGER? {N} [ S* ['-'|'+'] S* INTEGER ]?

    let index = 0;

    let a = 0;
    let sign = readSign();
    let number = readNumber();

    if (index < formula.length && formula.charAt(index) === "n") {
        index++;
        a = sign * (number ?? 1);

        skipWhitespace();

        if (index < formula.length) {
            sign = readSign();
            skipWhitespace();
            number = readNumber();
        } else {
            sign = number = 0;
        }
    }

    // Throw if there is anything else
    if (number === null || index < formula.length) {
        throw new Error(`n-th rule couldn't be parsed ('${formula}')`);
    }

    return [a, sign * number];

    function readSign() {
        switch (formula.charAt(index)) {
            case "-": {
                index++;
                return -1;
            }
            case "+": {
                index++;
                break;
            }
        }

        return 1;
    }

    function readNumber() {
        const start = index;
        let value = 0;

        while (
            index < formula.length &&
            formula.charCodeAt(index) >= ZERO &&
            formula.charCodeAt(index) <= NINE
        ) {
            value = value * 10 + (formula.charCodeAt(index) - ZERO);
            index++;
        }

        // Return `null` if we didn't read anything.
        return index === start ? null : value;
    }

    function skipWhitespace() {
        while (
            index < formula.length &&
            whitespace.has(formula.charCodeAt(index))
        ) {
            index++;
        }
    }
}

```

### File: src\__fixtures__\rules.ts
```ts
export const valid: [string, [number, number]][] = [
    ["1", [0, 1]],
    ["2", [0, 2]],
    ["3", [0, 3]],
    ["5", [0, 5]],
    [" 1 ", [0, 1]],
    [" 5 ", [0, 5]],
    ["+2n + 1", [2, 1]],
    ["-1", [0, -1]],
    ["-1n + 3", [-1, 3]],
    ["-1n+3", [-1, 3]],
    ["-n+2", [-1, 2]],
    ["-n+3", [-1, 3]],
    ["0n+3", [0, 3]],
    ["1n", [1, 0]],
    ["1n+0", [1, 0]],
    ["2n", [2, 0]],
    ["2n + 1", [2, 1]],
    ["2n+1", [2, 1]],
    ["3n", [3, 0]],
    ["3n+0", [3, 0]],
    ["3n+1", [3, 1]],
    ["3n+2", [3, 2]],
    ["3n+3", [3, 3]],
    ["3n-1", [3, -1]],
    ["3n-2", [3, -2]],
    ["3n-3", [3, -3]],
    ["even", [2, 0]],
    ["n", [1, 0]],
    ["n+2", [1, 2]],
    ["odd", [2, 1]],

    // Surprisingly, neither sizzle, qwery or nwmatcher cover these cases
    ["-4n+13", [-4, 13]],
    ["-2n + 12", [-2, 12]],
    ["-n", [-1, 0]],
];

export const invalid = [
    "-",
    "- 1n",
    "-1 n",
    "2+0",
    "2n+-0",
    "an+b",
    "asdf",
    "b",
    "expr",
    "odd|even|x",
];

```

