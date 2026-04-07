---
id: domutils
type: knowledge
owner: OA_Triage
---
# domutils
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "type": "module",
    "name": "domutils",
    "version": "4.0.2",
    "description": "Utilities for working with htmlparser2's dom",
    "author": "Felix Boehm <me@feedic.com>",
    "funding": {
        "type": "github",
        "url": "https://github.com/fb55/domutils?sponsor=1"
    },
    "license": "BSD-2-Clause",
    "sideEffects": false,
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
        "!**/*.spec.ts",
        "!**/__fixtures__/**"
    ],
    "scripts": {
        "build": "tsc",
        "build:docs": "typedoc src",
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
        "url": "git://github.com/fb55/domutils.git"
    },
    "keywords": [
        "dom",
        "htmlparser2"
    ],
    "dependencies": {
        "dom-serializer": "^3.0.0",
        "domelementtype": "^3.0.0",
        "domhandler": "^6.0.0"
    },
    "devDependencies": {
        "@biomejs/biome": "^2.4.8",
        "@eslint/compat": "^2.0.3",
        "@feedic/eslint-config": "^0.3.1",
        "@types/node": "^25.5.0",
        "eslint": "^10.0.3",
        "eslint-config-biome": "^2.1.3",
        "htmlparser2": "~11.0.0",
        "typedoc": "^0.28.17",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.57.1",
        "vitest": "^4.0.18"
    },
    "engines": {
        "node": ">=20.19.0"
    }
}

```

### File: readme.md
```md
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
    "name": "domutils",
    "version": "4.0.2",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "domutils",
            "version": "4.0.2",
            "license": "BSD-2-Clause",
            "dependencies": {
                "dom-serializer": "^3.0.0",
                "domelementtype": "^3.0.0",
                "domhandler": "^6.0.0"
            },
            "devDependencies": {
                "@biomejs/biome": "^2.4.8",
                "@eslint/compat": "^2.0.3",
                "@feedic/eslint-config": "^0.3.1",
                "@types/node": "^25.5.0",
                "eslint": "^10.0.3",
                "eslint-config-biome": "^2.1.3",
                "htmlparser2": "~11.0.0",
                "typedoc": "^0.28.17",
                "typescript": "^5.9.3",
                "typescript-eslint": "^8.57.1",
                "vitest": "^4.0.18"
            },
            "engines": {
                "node": ">=20.19.0"
            },
            "funding": {
                "type": "github",
                "url": "https://github.com/fb55/domutils?sponsor=1"
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
            "version": "1.8.1",
            "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.8.1.tgz",
            "integrity": "sha512-AvT9QFpxK0Zd8J0jopedNm+w/2fIzvtPKPjqyw9jwvBaReTTqPBk9Hixaz7KbjimP+QNz605/XnjFcDAL2pqBg==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "@emnapi/wasi-threads": "1.1.0",
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@emnapi/runtime": {
            "version": "1.8.1",
            "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.8.1.tgz",
            "integrity": "sha512-mehfKSMWjjNol8659Z8KxEMrdSJDDot5SXMq00dM8BN4o+CLNXQ0xH2V7EchNHV4RmbZLmmPdEaXZc5H2FXmDg==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@emnapi/wasi-threads": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.1.0.tgz",
            "integrity": "sha512-WI0DdZ8xFSbgMjR1sFsKABJ/C5OnRrjT06JXbZKexJGrDuPTzZdDYfFlsgcCXCyf+suG5QU2e/y1Wo2V/OapLQ==",
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
            "version": "0.5.2",
            "resolved": "https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.5.2.tgz",
            "integrity": "sha512-a5MxrdDXEvqnIq+LisyCX6tQMPF/dSJpCfBgBauY+pNZ28yCtSsTvyTYrMhaI+LK26bVyCJfJkT0u8KIj2i1dQ==",
            "dev": true,
            "license": "Apache-2.0",
            "dependencies": {
                "@eslint/core": "^1.1.0"
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

... [TRUNCATED]
```

### File: tsconfig.eslint.json
```json
{
    "extends": "./tsconfig.json",
    "compilerOptions": {
        "rootDir": ".",
        "noEmit": true,
        "skipLibCheck": true,
        "isolatedDeclarations": false
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
        "target": "ES2022",
        "module": "nodenext",
        "moduleResolution": "nodenext",
        "lib": ["ES2022"],
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

### File: typedoc.json
```json
{
    "$schema": "https://typedoc.org/schema.json",
    "hideGenerator": true,
    "exclude": ["**/*+(index|.spec).ts"],
    "excludeExternals": true,
    "categorizeByGroup": false,
    "sort": ["enum-value-ascending", "alphabetical"],
    "navigation": {
        "includeCategories": true
    }
}

```

### File: src\feeds.spec.ts
```ts
// Runs tests for feeds

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { parseDocument } from "htmlparser2";
import { describe, expect, test } from "vitest";
import { getFeed } from "./feeds.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const documents = path.join(__dirname, "__fixtures__", "Documents");

describe("getFeed", () => {
    for (const name of fs.readdirSync(documents)) {
        test(name, async () => {
            const file = await fs.promises.readFile(
                path.join(documents, name),
                "utf8",
            );
            const document = parseDocument(file, { xmlMode: true });
            const feed = getFeed(document.children);

            expect(feed).toMatchSnapshot();
        });
    }
});

```

### File: src\feeds.ts
```ts
import type { AnyNode, Element } from "domhandler";
import { getElementsByTagName } from "./legacy.js";
import { textContent } from "./stringify.js";

/**
 * The medium of a media item.
 *
 * @category Feeds
 */
export type FeedItemMediaMedium =
    | "image"
    | "audio"
    | "video"
    | "document"
    | "executable";

/**
 * The type of a media item.
 *
 * @category Feeds
 */
export type FeedItemMediaExpression = "sample" | "full" | "nonstop";

/**
 * A media item of a feed entry.
 *
 * @category Feeds
 */
export interface FeedItemMedia {
    medium: FeedItemMediaMedium | undefined;
    isDefault: boolean;
    url?: string;
    fileSize?: number;
    type?: string;
    expression?: FeedItemMediaExpression;
    bitrate?: number;
    framerate?: number;
    samplingrate?: number;
    channels?: number;
    duration?: number;
    height?: number;
    width?: number;
    lang?: string;
}

/**
 * An entry of a feed.
 *
 * @category Feeds
 */
export interface FeedItem {
    id?: string;
    title?: string;
    link?: string;
    description?: string;
    pubDate?: Date;
    media: FeedItemMedia[];
}

/**
 * The root of a feed.
 *
 * @category Feeds
 */
export interface Feed {
    type: string;
    id?: string;
    title?: string;
    link?: string;
    description?: string;
    updated?: Date;
    author?: string;
    items: FeedItem[];
}

/**
 * Get the feed object from the root of a DOM tree.
 *
 * @category Feeds
 * @param document The DOM to extract the feed from.
 * @returns The feed.
 */
export function getFeed(document: AnyNode[]): Feed | null {
    const feedRoot = getOneElement(isValidFeed, document);

    return feedRoot
        ? feedRoot.name === "feed"
            ? getAtomFeed(feedRoot)
            : getRssFeed(feedRoot)
        : null;
}

/**
 * Parse an Atom feed.
 *
 * @param feedRoot The root of the feed.
 * @returns The parsed feed.
 */
function getAtomFeed(feedRoot: Element) {
    const childs = feedRoot.children;

    const feed: Feed = {
        type: "atom",
        items: getElementsByTagName("entry", childs).map((item) => {
            const { children } = item;
            const entry: FeedItem = { media: getMediaElements(children) };

            addConditionally(entry, "id", "id", children);
            addConditionally(entry, "title", "title", children);

            const href = getOneElement("link", children)?.attribs["href"];
            if (href) {
                entry.link = href;
            }

            const description =
                fetch("summary", children) || fetch("content", children);
            if (description) {
                entry.description = description;
            }

            const pubDate = fetch("updated", children);
            if (pubDate) {
                entry.pubDate = new Date(pubDate);
            }

            return entry;
        }),
    };

    addConditionally(feed, "id", "id", childs);
    addConditionally(feed, "title", "title", childs);
    const href = getOneElement("link", childs)?.attribs["href"];
    if (href) {
        feed.link = href;
    }
    addConditionally(feed, "description", "subtitle", childs);

    const updated = fetch("updated", childs);
    if (updated) {
        feed.updated = new Date(updated);
    }

    addConditionally(feed, "author", "email", childs, true);

    return feed;
}

/**
 * Parse a RSS feed.
 *
 * @param feedRoot The root of the feed.
 * @returns The parsed feed.
 */
function getRssFeed(feedRoot: Element) {
    const childs = getOneElement("channel", feedRoot.children)?.children ?? [];

    const feed: Feed = {
        type: feedRoot.name.substr(0, 3),
        id: "",
        items: getElementsByTagName("item", feedRoot.children).map(
            (item: Element) => {
                const { children } = item;
                const entry: FeedItem = { media: getMediaElements(children) };
                addConditionally(entry, "id", "guid", children);
                addConditionally(entry, "title", "title", children);
                addConditionally(entry, "link", "link", children);
                addConditionally(entry, "description", "description", children);
                const pubDate =
                    fetch("pubDate", children) || fetch("dc:date", children);
                if (pubDate) entry.pubDate = new Date(pubDate);

                return entry;
            },
        ),
    };

    addConditionally(feed, "title", "title", childs);
    addConditionally(feed, "link", "link", childs);
    addConditionally(feed, "description", "description", childs);

    const updated = fetch("lastBuildDate", childs);
    if (updated) {
        feed.updated = new Date(updated);
    }

    addConditionally(feed, "author", "managingEditor", childs, true);

    return feed;
}

const MEDIA_KEYS_STRING = ["url", "type", "lang"] as const;
const MEDIA_KEYS_INT = [
    "fileSize",
    "bitrate",
    "framerate",
    "samplingrate",
    "channels",
    "duration",
    "height",
    "width",
] as const;

/**
 * Get all media elements of a feed item.
 *
 * @param where Nodes to search in.
 * @returns Media elements.
 */
function getMediaElements(where: AnyNode[]): FeedItemMedia[] {
    return getElementsByTagName("media:content", where).map((element) => {
        const { attribs } = element;

        const media: FeedItemMedia = {
            medium: attribs["medium"] as unknown as
                | FeedItemMediaMedium
                | undefined,
            isDefault: !!attribs["isDefault"],
        };

        for (const attrib of MEDIA_KEYS_STRING) {
            if (attribs[attrib]) {
                media[attrib] = attribs[attrib];
            }
        }

        for (const attrib of MEDIA_KEYS_INT) {
            if (attribs[attrib]) {
                media[attrib] = Number.parseInt(attribs[attrib], 10);
            }
        }

        if (attribs["expression"]) {
            media.expression = attribs[
                "expression"
            ] as unknown as FeedItemMediaExpression;
        }

        return media;
    });
}

/**
 * Get one element by tag name.
 *
 * @param tagName Tag name to look for
 * @param node Node to search in
 * @returns The element or null
 */
function getOneElement(
    tagName: string | ((name: string) => boolean),
    node: AnyNode[],
): Element | null {
    return getElementsByTagName(tagName, node, true, 1)[0];
}

/**
 * Get the text content of an element with a certain tag name.
 *
 * @param tagName Tag name to look for.
 * @param where Node to search in.
 * @param recurse Whether to recurse into child nodes.
 * @returns The text content of the element.
 */
function fetch(
    tagName: string,
    where: AnyNode | AnyNode[],
    recurse = false,
): string {
    return textContent(getElementsByTagName(tagName, where, recurse, 1)).trim();
}

/**
 * Adds a property to an object if it has a value.
 *
 * @param object Object to be extended.
 * @param property Property name.
 * @param tagName Tag name that contains the conditionally added property.
 * @param where Element to search for the property.
 * @param recurse Whether to recurse into child nodes.
 */
function addConditionally<T>(
    object: T,
    property: keyof T,
    tagName: string,
    where: AnyNode[],
    recurse = false,
) {
    const value = fetch(tagName, where, recurse);
    if (value) object[property] = value as unknown as T[keyof T];
}

/**
 * Checks if an element is a feed root node.
 *
 * @param value The name of the element to check.
 * @returns Whether an element is a feed root node.
 */
function isValidFeed(value: string) {
    return value === "rss" || value === "feed" || value === "rdf:RDF";
}

```

### File: src\helpers.spec.ts
```ts
import type { Document, Element } from "domhandler";
import { parseDocument } from "htmlparser2";
import { beforeEach, describe, expect, it } from "vitest";
import {
    compareDocumentPosition,
    removeSubsets,
    uniqueSort,
} from "./helpers.js";

describe("helpers", () => {
    describe("removeSubsets", () => {
        const dom = parseDocument("<div><p><span></span></p><p></p></div>")
            .children[0] as Element;

        it("removes identical trees", () =>
            expect(removeSubsets([dom, dom])).toHaveLength(1));

        it("Removes subsets found first", () => {
            const firstChild = dom.children[0] as Element;
            const matches = removeSubsets([dom, firstChild.children[0]]);
            expect(matches).toHaveLength(1);
        });

        it("Removes subsets found last", () =>
            expect(removeSubsets([dom.children[0], dom])).toHaveLength(1));

        it("Does not remove unique trees", () =>
            expect(
                removeSubsets([dom.children[0], dom.children[1]]),
            ).toHaveLength(2));
    });

    describe("compareDocumentPosition", () => {
        const markup = "<div><p><span></span></p><a></a></div>";
        const dom = parseDocument(markup).children[0] as Element;
        const p = dom.children[0] as Element;
        const span = p.children[0];
        const a = dom.children[1];

        it("reports when the first node occurs before the second indirectly", () =>
            expect(compareDocumentPosition(span, a)).toBe(2));

        it("reports when the first node contains the second", () =>
            expect(compareDocumentPosition(p, span)).toBe(10));

        it("reports when the first node occurs after the second indirectly", () =>
            expect(compareDocumentPosition(a, span)).toBe(4));

        it("reports when the first node is contained by the second", () =>
            expect(compareDocumentPosition(span, p)).toBe(20));

        it("reports when the nodes belong to separate documents", () => {
            const otherDom = parseDocument(markup).children[0] as Element;
            const other = (otherDom.children[0] as Element).children[0];

            expect(compareDocumentPosition(span, other)).toBe(1);
        });

        it("reports when the nodes are identical", () =>
            expect(compareDocumentPosition(span, span)).toBe(0));

        it("does not end up in infinite loop (#109)", () => {
            const dom = parseDocument("<div><span>1</span><span>2</span></div>")
                .children[0] as Element;

            expect(
                compareDocumentPosition(
                    dom.children[0],
                    (dom.children[0] as Element).children[0],
                ),
            ).toBe(10);
        });
    });

    describe("uniqueSort", () => {
        let root: Document;
        let dom: Element;
        let p: Element;
        let span: Element;
        let a: Element;

        beforeEach(() => {
            root = parseDocument("<div><p><span></span></p><a></a></div>");
            [dom] = root.children as Element[];
            [p, a] = dom.children as Element[];
            [span] = p.children as Element[];
        });

        it("leaves unique elements untouched", () =>
            expect(uniqueSort([p, a])).toStrictEqual([p, a]));

        it("removes duplicate elements", () =>
            expect(uniqueSort([p, a, p])).toStrictEqual([p, a]));

        it("sorts nodes in document order", () =>
            expect(uniqueSort([a, dom, span, p])).toStrictEqual([
                dom,
                p,
                span,
                a,
            ]));
        it("puts the document node in the right spot", () =>
            expect(uniqueSort([a, dom, span, root, p])).toStrictEqual([
                root,
                dom,
                p,
                span,
                a,
            ]));
    });
});

```

### File: src\helpers.ts
```ts
import { type AnyNode, hasChildren, type ParentNode } from "domhandler";

/**
 * Given an array of nodes, remove any member that is contained by another
 * member.
 *
 * @category Helpers
 * @param nodes Nodes to filter.
 * @returns Remaining nodes that aren't contained by other nodes.
 */
export function removeSubsets(nodes: AnyNode[]): AnyNode[] {
    let index = nodes.length;

    /*
     * Check if each node (or one of its ancestors) is already contained in the
     * array.
     */
    while (--index >= 0) {
        const node = nodes[index];

        /*
         * Remove the node if it is not unique.
         * We are going through the array from the end, so we only
         * have to check nodes that preceed the node under consideration in the array.
         */
        if (index > 0 && nodes.lastIndexOf(node, index - 1) >= 0) {
            nodes.splice(index, 1);
            continue;
        }

        for (let ancestor = node.parent; ancestor; ancestor = ancestor.parent) {
            if (nodes.includes(ancestor)) {
                nodes.splice(index, 1);
                break;
            }
        }
    }

    return nodes;
}
/**
 * @category Helpers
 * @see {@link http://dom.spec.whatwg.org/#dom-node-comparedocumentposition}
 */
export const enum DocumentPosition {
    DISCONNECTED = 1,
    PRECEDING = 2,
    FOLLOWING = 4,
    CONTAINS = 8,
    CONTAINED_BY = 16,
}

/**
 * Compare the position of one node against another node in any other document,
 * returning a bitmask with the values from {@link DocumentPosition}.
 *
 * Document order:
 * > There is an ordering, document order, defined on all the nodes in the
 * > document corresponding to the order in which the first character of the
 * > XML representation of each node occurs in the XML representation of the
 * > document after expansion of general entities. Thus, the document element
 * > node will be the first node. Element nodes occur before their children.
 * > Thus, document order orders element nodes in order of the occurrence of
 * > their start-tag in the XML (after expansion of entities). The attribute
 * > nodes of an element occur after the element and before its children. The
 * > relative order of attribute nodes is implementation-dependent.
 *
 * Source:
 * http://www.w3.org/TR/DOM-Level-3-Core/glossary.html#dt-document-order
 *
 * @category Helpers
 * @param nodeA The first node to use in the comparison
 * @param nodeB The second node to use in the comparison
 * @returns A bitmask describing the input nodes' relative position.
 *
 * See http://dom.spec.whatwg.org/#dom-node-comparedocumentposition for
 * a description of these values.
 */
export function compareDocumentPosition(
    nodeA: AnyNode,
    nodeB: AnyNode,
): number {
    const aParents: ParentNode[] = [];
    const bParents: ParentNode[] = [];

    if (nodeA === nodeB) {
        return 0;
    }

    let current = hasChildren(nodeA) ? nodeA : nodeA.parent;
    while (current) {
        aParents.unshift(current);
        current = current.parent;
    }
    current = hasChildren(nodeB) ? nodeB : nodeB.parent;
    while (current) {
        bParents.unshift(current);
        current = current.parent;
    }

    const maxIndex = Math.min(aParents.length, bParents.length);
    let index = 0;
    while (index < maxIndex && aParents[index] === bParents[index]) {
        index++;
    }

    if (index === 0) {
        return DocumentPosition.DISCONNECTED;
    }

    const sharedParent = aParents[index - 1];
    const siblings: AnyNode[] = sharedParent.children;
    const aSibling = aParents[index];
    const bSibling = bParents[index];

    if (siblings.indexOf(aSibling) > siblings.indexOf(bSibling)) {
        if (sharedParent === nodeB) {
            return DocumentPosition.FOLLOWING | DocumentPosition.CONTAINED_BY;
        }
        return DocumentPosition.FOLLOWING;
    }
    if (sharedParent === nodeA) {
        return DocumentPosition.PRECEDING | DocumentPosition.CONTAINS;
    }
    return DocumentPosition.PRECEDING;
}

/**
 * Sort an array of nodes based on their relative position in the document,
 * removing any duplicate nodes. If the array contains nodes that do not belong
 * to the same document, sort order is unspecified.
 *
 * @category Helpers
 * @param nodes Array of DOM nodes.
 * @returns Collection of unique nodes, sorted in document order.
 */
export function uniqueSort<T extends AnyNode>(nodes: T[]): T[] {
    nodes = nodes.filter(
        (node, index, array) => !array.includes(node, index + 1),
    );

    nodes.sort((a, b) => {
        const relative = compareDocumentPosition(a, b);
        if (relative & DocumentPosition.PRECEDING) {
            return -1;
        }
        if (relative & DocumentPosition.FOLLOWING) {
            return 1;
        }
        return 0;
    });

    return nodes;
}

```

### File: src\index.ts
```ts
export * from "./feeds.js";
export * from "./helpers.js";
export * from "./legacy.js";
export * from "./manipulation.js";
export * from "./querying.js";
export * from "./stringify.js";
export * from "./traversal.js";

```

### File: src\legacy.spec.ts
```ts
import { ElementType } from "domelementtype";
import type { AnyNode, Element } from "domhandler";
import { beforeAll, describe, expect, it } from "vitest";
import fixture from "./__fixtures__/fixture.js";
import {
    getElementById,
    getElements,
    getElementsByClassName,
    getElementsByTagName,
    getElementsByTagType,
} from "./legacy.js";

describe("legacy", () => {
    // Set up expected structures
    const expected = {
        idAsdf: fixture[1] as Element,
        tag2: [] as AnyNode[],
        typeScript: [] as AnyNode[],
    };

    beforeAll(() => {
        for (let index = 0; index < 20; ++index) {
            const node = fixture[index * 2 + 1] as Element;
            expected.tag2.push(node.children[5]);
            expected.typeScript.push(node.children[1]);
        }
    });
    describe("getElements", () => {
        it("returns the node with the specified ID", () =>
            expect(getElements({ id: "asdf" }, fixture, true, 1)).toEqual([
                expected.idAsdf,
            ]));
        it("returns empty array for unknown IDs", () =>
            expect(getElements({ id: "asdfs" }, fixture, true)).toHaveLength(
                0,
            ));
        it("returns the node for a ID function", () =>
            expect(
                getElements({ id: (id) => id === "asdf" }, fixture, true, 1),
            ).toEqual([expected.idAsdf]));
        it("returns the nodes with the specified tag name", () =>
            expect(getElements({ tag_name: "tag2" }, fixture, true)).toEqual(
                expected.tag2,
            ));
        it("returns empty array for unknown tag names", () =>
            expect(
                getElements({ tag_name: "asdfs" }, fixture, true),
            ).toHaveLength(0));
        it("returns all elements for wildcard tag names", () =>
            expect(getElements({ tag_name: "*" }, fixture, true)).toHaveLength(
                60,
            ));
        it("returns the nodes with the specified tag name function", () =>
            expect(
                getElements(
                    { tag_name: (name) => name === "tag2" },
                    fixture,
                    true,
                ),
            ).toEqual(expected.tag2));
        it("returns the nodes with the specified tag type", () =>
            expect(getElements({ tag_type: "script" }, fixture, true)).toEqual(
                expected.typeScript,
            ));
        it("returns empty array for unknown tag types", () =>
            expect(
                getElements({ tag_type: "video" }, fixture, true),
            ).toHaveLength(0));
        it("returns the nodes with the specified tag type function", () =>
            expect(
                getElements(
                    { tag_type: (type) => type === "script" },
                    fixture,
                    true,
                ),
            ).toEqual(expected.typeScript));
        it("returns elements for contains", () =>
            expect(
                getElements({ tag_contains: "text" }, fixture, true),
            ).toHaveLength(20));
        it("returns elements for contains function", () =>
            expect(
                getElements(
                    { tag_contains: (text) => text === "text" },
                    fixture,
                    true,
                ),
            ).toHaveLength(20));
    });

    describe("getElementById", () => {
        it("returns the specified node", () =>
            expect(getElementById("asdf", fixture, true)).toBe(
                expected.idAsdf,
            ));
        it("returns `null` for unknown IDs", () =>
            expect(getElementById("asdfs", fixture, true)).toBeNull());
    });

    describe("getElementsByClassName", () => {
        it("returns the specified nodes", () =>
            expect(
                getElementsByClassName("class1", fixture, true),
            ).toHaveLength(20));
        it("returns empty array for unknown class names", () =>
            expect(
                getElementsByClassName("class23", fixture, true),
            ).toHaveLength(0));
    });

    describe("getElementsByTagName", () => {
        it("returns the specified nodes", () =>
            expect(getElementsByTagName("tag2", fixture, true)).toEqual(
                expected.tag2,
            ));
        it("returns empty array for unknown tag names", () =>
            expect(getElementsByTagName("tag23", fixture, true)).toHaveLength(
                0,
            ));
    });

    describe("getElementsByTagType", () => {
        it("returns the specified nodes", () =>
            expect(
                getElementsByTagType(ElementType.Script, fixture, true),
            ).toEqual(expected.typeScript));
        it("returns empty array for unknown tag types", () =>
            expect(
                getElementsByTagType("video" as never, fixture, true),
            ).toHaveLength(0));
    });
});

```

### File: src\legacy.ts
```ts
import type { ElementType } from "domelementtype";
import { type AnyNode, type Element, isTag, isText } from "domhandler";
import { filter, findOne } from "./querying.js";

type TestType = (element: AnyNode) => boolean;

/**
 * An object with keys to check elements against. If a key is `tag_name`,
 * `tag_type` or `tag_contains`, it will check the value against that specific
 * value. Otherwise, it will check an attribute with the key's name.
 *
 * @category Legacy Query Functions
 */
// eslint-disable-next-line unicorn/prevent-abbreviations -- Keep the exported API name for backwards compatibility.
export interface TestElementOpts {
    tag_name?: string | ((name: string) => boolean);
    tag_type?: string | ((name: string) => boolean);
    tag_contains?: string | ((data?: string) => boolean);
    [attributeName: string]:
        | undefined
        | string
        | ((attributeValue: string) => boolean);
}

/**
 * A map of functions to check nodes against.
 */
const Checks: Record<
    string,
    (value: string | undefined | ((inputString: string) => boolean)) => TestType
> = {
    tag_name(name) {
        if (typeof name === "function") {
            return (element: AnyNode) => isTag(element) && name(element.name);
        }
        if (name === "*") {
            return isTag;
        }
        return (element: AnyNode) => isTag(element) && element.name === name;
    },
    tag_type(type) {
        if (typeof type === "function") {
            return (element: AnyNode) => type(element.type);
        }
        return (element: AnyNode) => element.type === type;
    },
    tag_contains(data) {
        if (typeof data === "function") {
            return (element: AnyNode) => isText(element) && data(element.data);
        }
        return (element: AnyNode) => isText(element) && element.data === data;
    },
};

/**
 * Returns a function to check whether a node has an attribute with a particular
 * value.
 *
 * @param attrib Attribute to check.
 * @param value Attribute value to look for.
 * @returns A function to check whether the a node has an attribute with a
 *   particular value.
 */
function getAttribCheck(
    attrib: string,
    value: undefined | string | ((value: string) => boolean),
): TestType {
    if (typeof value === "function") {
        return (element: AnyNode) =>
            isTag(element) && value(element.attribs[attrib]);
    }
    return (element: AnyNode) =>
        isTag(element) && element.attribs[attrib] === value;
}

/**
 * Returns a function that returns `true` if either of the input functions
 * returns `true` for a node.
 *
 * @param a First function to combine.
 * @param b Second function to combine.
 * @returns A function taking a node and returning `true` if either of the input
 *   functions returns `true` for the node.
 */
function combineFuncs(a: TestType, b: TestType): TestType {
    return (element: AnyNode) => a(element) || b(element);
}

/**
 * Returns a function that executes all checks in `options` and returns `true`
 * if any of them match a node.
 *
 * @param options An object describing nodes to look for.
 * @returns A function that executes all checks in `options` and returns `true`
 *   if any of them match a node.
 */
function compileTest(options: TestElementOpts): TestType | null {
    const funcs = Object.keys(options).map((key) => {
        const value = options[key];
        return Object.hasOwn(Checks, key)
            ? Checks[key](value)
            : getAttribCheck(key, value);
    });

    return funcs.length === 0 ? null : funcs.reduce(combineFuncs);
}

/**
 * Checks whether a node matches the description in `options`.
 *
 * @category Legacy Query Functions
 * @param options An object describing nodes to look for.
 * @param node The element to test.
 * @returns Whether the element matches the description in `options`.
 */
export function testElement(options: TestElementOpts, node: AnyNode): boolean {
    const test = compileTest(options);
    return test ? test(node) : true;
}

/**
 * Returns all nodes that match `options`.
 *
 * @category Legacy Query Functions
 * @param options An object describing nodes to look for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes that match `options`.
 */
export function getElements(
    options: TestElementOpts,
    nodes: AnyNode | AnyNode[],
    recurse: boolean,
    limit: number = Number.POSITIVE_INFINITY,
): AnyNode[] {
    const test = compileTest(options);
    return test ? filter(test, nodes, recurse, limit) : [];
}

/**
 * Returns the node with the supplied ID.
 *
 * @category Legacy Query Functions
 * @param id The unique ID attribute value to look for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @returns The node with the supplied ID.
 */
export function getElementById(
    id: string | ((id: string) => boolean),
    nodes: AnyNode | AnyNode[],
    recurse = true,
): Element | null {
    if (!Array.isArray(nodes)) nodes = [nodes];
    return findOne(getAttribCheck("id", id), nodes, recurse);
}

/**
 * Returns all nodes with the supplied `tagName`.
 *
 * @category Legacy Query Functions
 * @param tagName Tag name to search for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes with the supplied `tagName`.
 */
export function getElementsByTagName(
    tagName: string | ((name: string) => boolean),
    nodes: AnyNode | AnyNode[],
    recurse = true,
    limit: number = Number.POSITIVE_INFINITY,
): Element[] {
    return filter(
        Checks["tag_name"](tagName),
        nodes,
        recurse,
        limit,
    ) as Element[];
}

/**
 * Returns all nodes with the supplied `className`.
 *
 * @category Legacy Query Functions
 * @param className Class name to search for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes with the supplied `className`.
 */
export function getElementsByClassName(
    className: string | ((name: string) => boolean),
    nodes: AnyNode | AnyNode[],
    recurse = true,
    limit: number = Number.POSITIVE_INFINITY,
): Element[] {
    return filter(
        getAttribCheck("class", className),
        nodes,
        recurse,
        limit,
    ) as Element[];
}

/**
 * Returns all nodes with the supplied `type`.
 *
 * @category Legacy Query Functions
 * @param type Element type to look for.
 * @param nodes Nodes to search through.
 * @param recurse Also consider child nodes.
 * @param limit Maximum number of nodes to return.
 * @returns All nodes with the supplied `type`.
 */
export function getElementsByTagType(
    type: ElementType | ((type: ElementType) => boolean),
    nodes: AnyNode | AnyNode[],
    recurse = true,
    limit: number = Number.POSITIVE_INFINITY,
): AnyNode[] {
    return filter(Checks["tag_type"](type as string), nodes, recurse, limit);
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
