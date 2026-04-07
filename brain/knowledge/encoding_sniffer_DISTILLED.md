---
id: encoding-sniffer
type: knowledge
owner: OA_Triage
---
# encoding-sniffer
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "encoding-sniffer",
    "version": "1.0.2",
    "description": "Implementation of the HTML encoding sniffer algo, with stream support",
    "bugs": {
        "url": "https://github.com/fb55/encoding-sniffer/issues"
    },
    "repository": {
        "type": "git",
        "url": "git://github.com/fb55/encoding-sniffer.git"
    },
    "funding": {
        "type": "github",
        "url": "https://github.com/fb55/encoding-sniffer?sponsor=1"
    },
    "license": "MIT",
    "author": "Felix Boehm <me@feedic.com>",
    "sideEffects": false,
    "type": "module",
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "default": "./dist/index.js"
        },
        "./sniffer": {
            "types": "./dist/sniffer.d.ts",
            "default": "./dist/sniffer.js"
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
        "build": "tsc",
        "build:docs": "typedoc --hideGenerator src/index.ts",
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
        "@exodus/bytes": "^1.15.0"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.10",
        "@feedic/eslint-config": "^0.3.1",
        "@types/node": "^25.5.2",
        "eslint": "^10.1.0",
        "eslint-config-biome": "^2.1.3",
        "globals": "^17.4.0",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.58.0",
        "vitest": "^4.1.2"
    },
    "engines": {
        "node": ">=20.19.0"
    }
}

```

### File: README.md
```md
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
            "!package-lock.json",
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

### File: eslint.config.js
```js
import { commonTypeScriptRules } from "@feedic/eslint-config/typescript";
import tseslint from "typescript-eslint";
import eslintConfigBiome from "eslint-config-biome";
import globals from "globals";
import feedicFlatConfig from "@feedic/eslint-config";
import { defineConfig } from "eslint/config";

export default defineConfig(
    {
        ignores: [
            "node_modules/",
            "coverage/",
            "dist/",
            "docs/",
            "jsr.json",
        ],
    },
    ...feedicFlatConfig,
    {
        languageOptions: {
            globals: globals.node,
            ecmaVersion: 2022,
            sourceType: "module",
        },
        settings: {
            node: {
                version: ">=20.19.0",
            },
        },
        rules: {
            "unicorn/text-encoding-identifier-case": "off",
        },
    },
    {
        files: ["**/*.ts"],
        extends: [...tseslint.configs.recommended],
        languageOptions: {
            parser: tseslint.parser,
            parserOptions: {
                sourceType: "module",
                project: "./tsconfig.eslint.json",
            },
        },
        rules: {
            ...commonTypeScriptRules,
            "@typescript-eslint/explicit-function-return-type": "error",
            "@typescript-eslint/no-unnecessary-condition": "error",
        },
    },
    eslintConfigBiome,
);

```

### File: package-lock.json
```json
{
    "name": "encoding-sniffer",
    "version": "1.0.2",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "encoding-sniffer",
            "version": "1.0.2",
            "license": "MIT",
            "dependencies": {
                "@exodus/bytes": "^1.15.0"
            },
            "devDependencies": {
                "@biomejs/biome": "^2.4.10",
                "@feedic/eslint-config": "^0.3.1",
                "@types/node": "^25.5.2",
                "eslint": "^10.1.0",
                "eslint-config-biome": "^2.1.3",
                "globals": "^17.4.0",
                "typescript": "^5.9.3",
                "typescript-eslint": "^8.58.0",
                "vitest": "^4.1.2"
            },
            "engines": {
                "node": ">=20.19.0"
            },
            "funding": {
                "type": "github",
                "url": "https://github.com/fb55/encoding-sniffer?sponsor=1"
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
                "eslint": {
                    "optional": true
                }
            }
        },
        "node_modules/@eslint/object-schema": {
            "version": "3.0.3",
            "resolved": "https://registry.npmjs.org/@eslint/object-schema/-/object-schema-3.0.3.tgz",
            "integrity": "sha512-iM869Pugn9Nsxbh/YHRqYiqd23AmIbxJOcpUMOuWCVNdoQJ5ZtwL6h3t0bcZzJUlC3Dq9jCFCESBZnX0GTv7iQ==",
            "dev": true,
            "license": "Apache-2.0",
            "engines": {
                "node": "^20.19.0 || ^22.13.0 || >=24"
            }
        },
        "node_modules/@eslint/plugin-kit": {
            "version": "0.6.1",
            "resolved": "https://registry.npmjs.org/@eslint/plugin-kit/-/plugin-kit-0.6.1.tgz",
       
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
        "rootDir": "src",
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
        "noUnusedParameters": true
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

### File: src\charset-with-underscore.spec.ts
```ts
import { describe, expect, it } from "vitest";
import { ResultType, Sniffer } from "./sniffer.js";

const XML_ENCODING = "<?xml encoding='Shift_JIS'>";
const META_CONTENT =
    "<meta http-equiv='content-type' content=charset=Shift_JIS>";

const META_CHARSET = "<meta charset=Shift_JIS>";

describe("Sniffer", () => {
    it("should recognize XML ", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(XML_ENCODING));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.XML_ENCODING);
    });

    it("should recognize HTML meta tag charset, lower", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CHARSET));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag charset, upper", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CHARSET.toUpperCase()));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag charset, quoted", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from("<Meta Charset  =  ' Shift_JIS '>"));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, lower", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CONTENT));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, upper", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CONTENT.toUpperCase()));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, byte-by-byte", () => {
        const sniffer = new Sniffer();
        for (const c of META_CONTENT) sniffer.write(Buffer.from(c));
        expect(sniffer.encoding).toBe("Shift_JIS");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });
});

```

### File: src\html-encoding-sniffer.spec.ts
```ts
/**
 * This file, and the __fixtures__ directory, were adapted from the
 * html-encoding-sniffer module, copyright © Domenic Denicola.
 *
 * See __fixtures__/LICENSE.txt for full license terms.
 */

import assert from "node:assert";
import fs from "node:fs";
import path from "node:path";
import { describe, it } from "vitest";
import { getEncoding as htmlEncodingSniffer } from "./index.js";

function read(relative: string): Uint8Array {
    // Test that the module works with Uint8Arrays, not just Buffers:
    const buffer = fs.readFileSync(
        path.resolve(__dirname, "__fixtures__", relative),
    );
    return new Uint8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);
}

describe("A file with a UTF-8 BOM", () => {
    const buffer = read("utf-8-bom.html");

    it("should sniff as UTF-8, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "UTF-8");
    });

    it("should sniff as UTF-8, given overriding options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1252",
            defaultEncoding: "UTF-16LE",
        });

        assert.strictEqual(sniffedEncoding, "UTF-8");
    });
});

describe("A file with a UTF-16LE BOM", () => {
    const buffer = read("utf-16le-bom.html");

    it("should sniff as UTF-16LE, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "UTF-16LE");
    });

    it("should sniff as UTF-16LE, given overriding options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1252",
            defaultEncoding: "UTF-8",
        });

        assert.strictEqual(sniffedEncoding, "UTF-16LE");
    });
});

describe("A file with a UTF-16BE BOM", () => {
    const buffer = read("utf-16be-bom.html");

    it("should sniff as UTF-16BE, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "UTF-16BE");
    });

    it("should sniff as UTF-16BE, given overriding options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1252",
            defaultEncoding: "UTF-8",
        });

        assert.strictEqual(sniffedEncoding, "UTF-16BE");
    });
});

describe("A file with no BOM and no <meta charset>", () => {
    const buffer = read("no-bom-no-charset.html");

    it("should sniff as windows-1252, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "windows-1252");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the default encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "ISO-8859-16");
    });
});

describe("A file with no BOM and a <meta charset>", () => {
    const buffer = read("no-bom-charset-koi8.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "KOI8-R");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "KOI8-R");
    });
});

describe("A file with no BOM and a <meta http-equiv>", () => {
    const buffer = read("no-bom-charset-http-equiv-tis-620.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "windows-874");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-874");
    });
});

describe("A file with no BOM and a <meta http-equiv> with no quotes", () => {
    const buffer = read("no-bom-charset-http-equiv-no-quotes.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "ISO-8859-5");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "ISO-8859-5");
    });
});

describe("A file with no BOM and a ><meta charset>", () => {
    const buffer = read("no-bom-charset-bracket.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "UTF-8");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "UTF-8");
    });
});

describe("A file with no BOM and a <meta charset> preceeded by a short comment <!-->", () => {
    const buffer = read("no-bom-charset-short-comment.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "ISO-8859-2");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "ISO-8859-2");
    });
});

describe("A file with no BOM and a <meta http-equiv> ending with a trailing space", () => {
    const buffer = read("no-bom-charset-http-equiv-trailing-space.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "ISO-8859-2");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "ISO-8859-2");
    });
});

describe("A file with no BOM and a <meta http-equiv> with 'charsetcharset'", () => {
    const buffer = read("no-bom-charset-http-equiv-second-charset.html");

    it("should sniff as the charset value, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "ISO-8859-2");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the charset value, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "ISO-8859-2");
    });
});

describe("A file with no BOM and a <meta http-equiv=refresh> with another http-equiv", () => {
    const buffer = read("no-bom-charset-http-equiv-refresh.html");

    it("should sniff as windows-1252, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "windows-1252");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as the default encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "ISO-8859-16");
    });
});

for (const utf16Encoding of ["utf-16be", "utf-16", "utf-16le"]) {
    describe(`A file with a BOM and a <meta charset> of ${utf16Encoding}`, () => {
        const buffer = read(`no-bom-charset-${utf16Encoding}.html`);

        it("should sniff as UTF-8, given no options", () => {
            const sniffedEncoding = htmlEncodingSniffer(buffer);

            assert.strictEqual(sniffedEncoding, "UTF-8");
        });

        it("should sniff as the transport layer encoding, given that", () => {
            const sniffedEncoding = htmlEncodingSniffer(buffer, {
                transportLayerEncodingLabel: "windows-1251",
                defaultEncoding: "ISO-8859-16",
            });

            assert.strictEqual(sniffedEncoding, "windows-1251");
        });

        it("should sniff as UTF-8, given only a default encoding", () => {
            const sniffedEncoding = htmlEncodingSniffer(buffer, {
                defaultEncoding: "ISO-8859-16",
            });

            assert.strictEqual(sniffedEncoding, "UTF-8");
        });
    });
}

describe("A file with a BOM and a <meta charset> of x-user-defined", () => {
    const buffer = read("no-bom-charset-x-user-defined.html");

    it("should sniff as windows-1252, given no options", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer);

        assert.strictEqual(sniffedEncoding, "windows-1252");
    });

    it("should sniff as the transport layer encoding, given that", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            transportLayerEncodingLabel: "windows-1251",
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1251");
    });

    it("should sniff as windows-1252, given only a default encoding", () => {
        const sniffedEncoding = htmlEncodingSniffer(buffer, {
            defaultEncoding: "ISO-8859-16",
        });

        assert.strictEqual(sniffedEncoding, "windows-1252");
    });
});

```

### File: src\index.spec.ts
```ts
import { createReadStream, promises as fs, readdirSync } from "node:fs";
import path from "node:path";
import { setTimeout } from "node:timers/promises";
import { describe, expect, it } from "vitest";
import { DecodeStream } from "./index.js";

function getStream(stream: NodeJS.ReadableStream): Promise<string> {
    // TODO[engines.node@>=18]: Use `reduce`
    return new Promise((resolve, reject) => {
        let data = "";
        stream.on("data", (chunk) => {
            expect(typeof chunk).toBe("string");
            data += chunk;
        });
        stream.on("end", () => resolve(data));
        stream.on("error", reject);
        stream.resume();
    });
}

describe("DecodeStream", () => {
    it("should decode a UTF-8 string", async () => {
        const stream = new DecodeStream();
        stream.end(Buffer.from("Hello, world!"));
        expect(await getStream(stream)).toBe("Hello, world!");
    });

    describe("Fixtures", () => {
        for (const file of readdirSync(path.join(__dirname, "__fixtures__"))) {
            if (!file.endsWith(".html")) continue;

            it(`should decode ${file}`, async () => {
                const stream = new DecodeStream();
                createReadStream(
                    path.join(__dirname, "__fixtures__", file),
                ).pipe(stream);
                expect(await getStream(stream)).toMatchSnapshot();
            });
        }
    });

    it("should decode a file one byte at a time", async () => {
        const file = await fs.readFile(
            path.join(__dirname, "__fixtures__", "utf-16be-bom.html"),
        );
        const stream = new DecodeStream();
        const collector = getStream(stream);
        for (let index = 0; index < file.length; index++) {
            // Wait for a bit to allow the stream to process the data.
            await setTimeout(0);
            stream.write(file.slice(index, index + 1));
        }
        stream.end();
        expect(await collector).toMatchSnapshot();
    });
});

```

### File: src\index.ts
```ts
import { Transform, type TransformCallback } from "node:stream";

import { TextDecoder } from "@exodus/bytes/encoding.js";
import type { SnifferOptions } from "./sniffer.js";
import { getEncoding, Sniffer } from "./sniffer.js";

/**
 * Sniff the encoding of a buffer, then decode it.
 * @param buffer Buffer to be decoded
 * @param options Options for the sniffer
 * @returns The decoded buffer
 */
export function decodeBuffer(
    buffer: Buffer,
    options: SnifferOptions = {},
): string {
    const encoding = getEncoding(buffer, options);
    const decoder = new TextDecoder(encoding);
    return decoder.decode(buffer);
}

/**
 * Decodes a stream of buffers into a stream of strings.
 *
 * Reads the first 1024 bytes and passes them to the sniffer. Once an encoding
 * has been determined, it decodes all buffered data and outputs the results.
 */
export class DecodeStream extends Transform {
    private readonly sniffer: Sniffer;
    private readonly buffers: Uint8Array[] = [];
    /** The TextDecoder instance. If set, we have determined the encoding. */
    private decoder: TextDecoder | null = null;
    private readonly maxBytes: number;
    private readBytes = 0;

    constructor(options?: SnifferOptions) {
        super({ decodeStrings: false, encoding: "utf-8" });
        this.sniffer = new Sniffer(options);
        this.maxBytes = options?.maxBytes ?? 1024;
    }

    override _transform(
        chunk: Uint8Array,
        _encoding: string,
        callback: TransformCallback,
    ): void {
        if (this.readBytes < this.maxBytes) {
            this.sniffer.write(chunk);
            this.readBytes += chunk.length;

            if (this.readBytes < this.maxBytes) {
                this.buffers.push(chunk);
                callback();
                return;
            }
        }

        const decoder = this.getDecoder();
        const decoded = decoder.decode(chunk, { stream: true });
        if (decoded) {
            this.push(decoded, "utf-8");
        }
        callback();
    }

    private getDecoder(): TextDecoder {
        if (this.decoder) {
            return this.decoder;
        }

        this.decoder = new TextDecoder(this.sniffer.encoding);

        // Process all buffered chunks
        for (const buffer of this.buffers) {
            const decoded = this.decoder.decode(buffer, { stream: true });
            if (decoded) {
                this.push(decoded, "utf-8");
            }
        }
        this.buffers.length = 0;

        return this.decoder;
    }

    override _flush(callback: TransformCallback): void {
        const decoder = this.getDecoder();
        // Flush any remaining bytes
        const decoded = decoder.decode();
        if (decoded) {
            this.push(decoded, "utf-8");
        }
        callback();
    }
}

export { getEncoding, type SnifferOptions } from "./sniffer.js";

```

### File: src\sniffer.spec.ts
```ts
import { describe, expect, it } from "vitest";
import { ResultType, Sniffer, STRINGS } from "./sniffer.js";

const XML_ENCODING = "<?xml encoding='utf-16'>";
const META_CONTENT =
    "<meta http-equiv='content-type' content=charset=iso-8859-2>";

const META_CHARSET = "<meta charset=iso-8859-2>";

describe("Sniffer", () => {
    it("should recognize XML ", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(XML_ENCODING));
        expect(sniffer.encoding).toBe("UTF-8");
        expect(sniffer.resultType).toBe(ResultType.XML_ENCODING);
    });

    it("should recognize HTML meta tag charset, lower", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CHARSET));
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag charset, upper", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CHARSET.toUpperCase()));
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag charset, quoted", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from("<Meta Charset  =  ' ISO-8859-2 '>"));
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, lower", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CONTENT));
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, upper", () => {
        const sniffer = new Sniffer();
        sniffer.write(Buffer.from(META_CONTENT.toUpperCase()));
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, byte-by-byte", () => {
        const sniffer = new Sniffer();
        for (const c of META_CONTENT) sniffer.write(Buffer.from(c));
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should not recognize HTML meta tag http-equiv, if not within 1024 bytes", () => {
        const sniffer = new Sniffer();
        sniffer.write(
            Buffer.from("a".repeat(1010) + META_CONTENT.toUpperCase()),
        );
        expect(sniffer.encoding).toBe("windows-1252");
        expect(sniffer.resultType).toBe(ResultType.DEFAULT);
    });

    it("should recognize HTML meta tag http-equiv, with additional content", () => {
        const sniffer = new Sniffer();
        sniffer.write(
            Buffer.from(`${XML_ENCODING}<foo></foo> <bar baz><! ><!-- 
            foo --><mEtA foo=bar boo="hoo" content ="charsetsomethingcchArset  
            =\t'  windows-1254';other" http-EQUIV = contenT-tYpe>${META_CONTENT}`),
        );
        expect(sniffer.encoding).toBe("windows-1254");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, quoted attrib unquoted value", () => {
        const sniffer = new Sniffer();
        sniffer.write(
            Buffer.from(
                "<!---><meta http-equiv='content-type' content='CHARSET=x-user-defined'>",
            ),
        );
        expect(sniffer.encoding).toBe("windows-1252");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should recognize HTML meta tag http-equiv, unquoted attrib quoted value", () => {
        const sniffer = new Sniffer();
        sniffer.write(
            Buffer.from(
                "<!--><meta http-equiv='content-type' content=CHARSET='UTF-16BE'>",
            ),
        );
        expect(sniffer.encoding).toBe("UTF-8");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should ignore duplicate meta content attributes", () => {
        const sniffer = new Sniffer();
        sniffer.write(
            Buffer.from(
                "<meta content=CHARSET='iso-8859-2' content=charset=UTF-16LE http-equiv='content-type'>",
            ),
        );
        expect(sniffer.encoding).toBe("ISO-8859-2");
        expect(sniffer.resultType).toBe(ResultType.META_TAG);
    });

    it("should support XML UTF-16LE prefixes", () => {
        const sniffer = new Sniffer();
        sniffer.write(STRINGS.UTF16LE_XML_PREFIX);
        expect(sniffer.encoding).toBe("UTF-16LE");
        expect(sniffer.resultType).toBe(ResultType.XML_PREFIX);
    });

    it("should support XML UTF-16BE prefixes", () => {
        const sniffer = new Sniffer();
        sniffer.write(STRINGS.UTF16BE_XML_PREFIX);
        expect(sniffer.encoding).toBe("UTF-16BE");
        expect(sniffer.resultType).toBe(ResultType.XML_PREFIX);
    });

    it("should support UTF-8 BOMs", () => {
        const sniffer = new Sniffer();
        sniffer.write(STRINGS.UTF8_BOM);
        expect(sniffer.encoding).toBe("UTF-8");
        expect(sniffer.resultType).toBe(ResultType.BOM);
    });

    it("should support UTF-16LE BOMs", () => {
        const sniffer = new Sniffer();
        sniffer.write(STRINGS.UTF16LE_BOM);
        expect(sniffer.encoding).toBe("UTF-16LE");
        expect(sniffer.resultType).toBe(ResultType.BOM);
    });

    it("should support UTF-16BE BOMs", () => {
        const sniffer = new Sniffer();
        sniffer.write(STRINGS.UTF16BE_BOM);
        expect(sniffer.encoding).toBe("UTF-16BE");
        expect(sniffer.resultType).toBe(ResultType.BOM);
    });
});

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
