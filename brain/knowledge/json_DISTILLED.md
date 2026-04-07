---
id: json
type: knowledge
owner: OA_Triage
---
# json
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "json-schema-to-zod",
  "version": "2.8.1",
  "description": "Converts JSON schema objects or files into Zod schemas",
  "types": "./dist/types/index.d.ts",
  "bin": "./dist/cjs/cli.js",
  "main": "./dist/cjs/index.js",
  "module": "./dist/esm/index.js",
  "exports": {
    "import": {
      "types": "./dist/types/index.d.ts",
      "default": "./dist/esm/index.js"
    },
    "require": {
      "types": "./dist/types/index.d.ts",
      "default": "./dist/cjs/index.js"
    }
  },
  "scripts": {
    "build:types": "tsc -p tsconfig.types.json",
    "build:cjs": "tsc -p tsconfig.cjs.json && node postcjs.js",
    "build:esm": "tsc -p tsconfig.esm.json && node postesm.js",
    "build": "npm i && npm run gen && npm test && rimraf ./dist && npm run build:types && npm run build:cjs && npm run build:esm",
    "dry": "npm run build && npm pub --dry-run",
    "dev": "tsx watch test/index.ts",
    "gen": "tsx ./createIndex.ts",
    "test": "tsx test/index.ts"
  },
  "c8": {
    "exclude": [
      "dist",
      "createIndex.ts",
      "jest.config.js",
      "postcjs.js",
      "postesm.js",
      "test"
    ]
  },
  "keywords": ["zod", "json", "schema", "converter", "cli"],
  "author": "Stefan Terdell",
  "contributors": [
    "Chen (https://github.com/werifu)",
    "Nuno Carduso (https://github.com/ncardoso-barracuda)",
    "Lars Strojny (https://github.com/lstrojny)",
    "Navtoj Chahal (https://github.com/navtoj)",
    "Ben McCann (https://github.com/benmccann)",
    "Dmitry Zakharov (https://github.com/DZakh)",
    "Michel Turpin (https://github.com/grimly)",
    "David Barratt (https://github.com/davidbarratt)",
    "pevisscher (https://github.com/pevisscher)",
    "Aidin Abedi (https://github.com/aidinabedi)",
    "Brett Zamir (https://github.com/brettz9)",
    "vForgeOne (https://github.com/vforgeone)",
    "Adrian Ordonez (https://github.com/adrianord)",
    "Jonas Reucher (https://github.com/Mantls)",
    "Nicolas Forstner (https://github.com/nlsfnr)",
    "Jordyn https://github.com/ColourfulMelon"
  ],
  "license": "ISC",
  "repository": {
    "type": "git",
    "url": "https://github.com/StefanTerdell/json-schema-to-zod"
  },
  "devDependencies": {
    "@types/json-schema": "^7.0.15",
    "@types/node": "^20.9.0",
    "fast-diff": "^1.3.0",
    "rimraf": "^5.0.5",
    "tsx": "^4.1.1",
    "typescript": "^5.2.2",
    "zod": "^4.1.3"
  }
}

```

### File: README.md
```md
# Json-Schema-to-Zod

[![NPM Version](https://img.shields.io/npm/v/json-schema-to-zod.svg)](https://npmjs.org/package/json-schema-to-zod)
[![NPM Downloads](https://img.shields.io/npm/dw/json-schema-to-zod.svg)](https://npmjs.org/package/json-schema-to-zod)

# Notice of deprecation

As of March 2026, this project will no longer be actively maintained.

_Thank you to all the contributors and sponsors throughout the years! So long, and thanks for all the fish._

## Summary

A runtime package and CLI tool to convert JSON schema (draft 4+) objects or files into Zod schemas in the form of JavaScript code.

Before v2 it used [`prettier`](https://www.npmjs.com/package/prettier) for formatting and [`json-refs`](https://www.npmjs.com/package/json-refs) to resolve schemas. To replicate the previous behaviour, please use their respective CLI tools.

Since v2 the CLI supports piped JSON.

_Looking for the exact opposite? Check out [zod-to-json-schema](https://npmjs.org/package/zod-to-json-schema)_

## Usage

### Online

[Just paste your JSON schemas here!](https://stefanterdell.github.io/json-schema-to-zod-react/)

### CLI

#### Simplest example

```console
npm i -g json-schema-to-zod
```

```console
json-schema-to-zod -i mySchema.json -o mySchema.ts
```

#### Example with `$refs` resolved and output formatted

```console
npm i -g json-schema-to-zod json-refs prettier
```

```console
json-refs resolve mySchema.json | json-schema-to-zod | prettier --parser typescript > mySchema.ts
```

#### Options

| Flag           | Shorthand | Function                                                                                       |
| -------------- | --------- | ---------------------------------------------------------------------------------------------- |
| `--input`      | `-i`      | JSON or a source file path. Required if no data is piped.                                      |
| `--output`     | `-o`      | A file path to write to. If not supplied stdout will be used.                                  |
| `--name`       | `-n`      | The name of the schema in the output                                                           |
| `--depth`      | `-d`      | Maximum depth of recursion in schema before falling back to `z.any()`. Defaults to 0.          |
| `--module`     | `-m`      | Module syntax; `esm`, `cjs` or none. Defaults to `esm` in the CLI and `none` programmaticly.   |
| `--type`       | `-t`      | Export a named type along with the schema. Requires `name` to be set and `module` to be `esm`. |
| `--noImport`   | `-ni`     | Removes the `import { z } from 'zod';` or equivalent from the output.                          |
| `--withJsdocs` | `-wj`     | Generate jsdocs off of the description property.                                               |
| `--zodVersion` | `-zv`     | Target Zod version: `3` or `4`. Defaults to `4`.                                               |

### Zod Version Targeting

This package supports generating code compatible with both Zod v3 and v4. By default, Zod v4 syntax is generated.

**Key differences between versions:**

- **`z.record()`**: Zod v4 requires an explicit key type: `z.record(z.string(), valueSchema)` vs `z.record(valueSchema)` in v3
- **Error paths**: Zod v4 uses simplified error paths in `superRefine` callbacks

**CLI:**

```console
# Generate Zod v4 compatible code (default)
json-schema-to-zod -i schema.json -o output.ts

# Generate Zod v3 compatible code
json-schema-to-zod -i schema.json -o output.ts --zodVersion 3
```

**Programmatic:**

```typescript
// Zod v4 (default)
jsonSchemaToZod(schema, { zodVersion: 4 });

// Zod v3
jsonSchemaToZod(schema, { zodVersion: 3 });
```

### Programmatic

#### Simple example

```typescript
import { jsonSchemaToZod } from "json-schema-to-zod";

const myObject = {
  type: "object",
  properties: {
    hello: {
      type: "string",
    },
  },
};

const module = jsonSchemaToZod(myObject, { module: "esm" });

// `type` can be either a string or - outside of the CLI - a boolean. If its `true`, the name of the type will be the name of the schema with a capitalized first letter.
const moduleWithType = jsonSchemaToZod(myObject, {
  name: "mySchema",
  module: "esm",
  type: true,
});

const cjs = jsonSchemaToZod(myObject, { module: "cjs", name: "mySchema" });

const justTheSchema = jsonSchemaToZod(myObject);
```

##### `module`

```typescript
import { z } from "zod";

export default z.object({ hello: z.string().optional() });
```

##### `moduleWithType`

```typescript
import { z } from "zod";

export const mySchema = z.object({ hello: z.string().optional() });
export type MySchema = z.infer<typeof mySchema>;
```

##### `cjs`

```typescript
const { z } = require("zod");

module.exports = { mySchema: z.object({ hello: z.string().optional() }) };
```

##### `justTheSchema`

```typescript
z.object({ hello: z.string().optional() });
```

#### Example with `$refs` resolved and output formatted

```typescript
import { z } from "zod";
import { resolveRefs } from "json-refs";
import { format } from "prettier";
import jsonSchemaToZod from "json-schema-to-zod";

async function example(jsonSchema: Record<string, unknown>): Promise<string> {
  const { resolved } = await resolveRefs(jsonSchema);
  const code = jsonSchemaToZod(resolved);
  const formatted = await format(code, { parser: "typescript" });

  return formatted;
}
```

#### Overriding a parser

You can pass a function to the `parserOverride` option, which represents a function that receives the current schema node and the reference object, and should return a string when it wants to replace a default output. If the default output should be used for the node just return void.

#### Schema factoring

Factored schemas (like object schemas with "oneOf" etc.) is only partially supported. Here be dragons.

#### Use at Runtime

The output of this package is not meant to be used at runtime. JSON Schema and Zod does not overlap 100% and the scope of the parsers are purposefully limited in order to help the author avoid a permanent state of chaotic insanity. As this may cause some details of the original schema to be lost in translation, it is instead recommended to use tools such as [Ajv](https://ajv.js.org/) to validate your runtime values directly against the original JSON Schema.

That said, it's possible in most cases to use `eval`. Here's an example that you shouldn't use:

```typescript
const zodSchema = eval(jsonSchemaToZod({ type: "string" }, { module: "cjs" }));

zodSchema.safeParse("Please just use Ajv instead");
```

```

### File: .prettierrc.json
```json
{
  "semi": true
}

```

### File: CONTRIBUTING.md
```md
# Contributing

Hey, thanks for wanting to contribute.

Before you open a PR, make sure to open an issue and discuss the problem you want to solve. I will not consider PRs without issues.

I use [gitmoji](https://gitmoji.dev/) for my commit messages because I think it's fun. I encourage you to do the same, but won't enforce it.

I check PRs and issues very rarely so please be patient.

```

### File: createIndex.ts
```ts
import { readdirSync, writeFileSync, statSync } from "fs";

const ignore = ["src/index.ts", "src/cli.ts", "src/utils/cliTools.ts"];

function checkSrcDir(path: string): string[] {
  const lines: string[] = [];

  for (const item of readdirSync(path)) {
    const itemPath = path + "/" + item;

    if (ignore.includes(itemPath)) {
      continue;
    }

    if (statSync(itemPath).isDirectory()) {
      lines.push(...checkSrcDir(itemPath));
    } else if (item.endsWith(".ts")) {
      lines.push('export * from "./' + itemPath.slice(4, -2) + 'js"');
    }
  }

  return lines;
}

const lines = checkSrcDir("src");

lines.push(
  'import { jsonSchemaToZod } from "./jsonSchemaToZod.js"',
  "export default jsonSchemaToZod",
);

writeFileSync("./src/index.ts", lines.join("\n"));

```

### File: jest.config.js
```js
module.exports = {
  preset: "ts-jest",
  testEnvironment: "node",
};

```

### File: package-lock.json
```json
{
  "name": "json-schema-to-zod",
  "version": "2.8.1",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "json-schema-to-zod",
      "version": "2.8.1",
      "license": "ISC",
      "bin": {
        "json-schema-to-zod": "dist/cjs/cli.js"
      },
      "devDependencies": {
        "@types/json-schema": "^7.0.15",
        "@types/node": "^20.9.0",
        "fast-diff": "^1.3.0",
        "rimraf": "^5.0.5",
        "tsx": "^4.1.1",
        "typescript": "^5.2.2",
        "zod": "^4.1.3"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.25.12.tgz",
      "integrity": "sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.25.12.tgz",
      "integrity": "sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.25.12.tgz",
      "integrity": "sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.25.12.tgz",
      "integrity": "sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.25.12.tgz",
      "integrity": "sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.25.12.tgz",
      "integrity": "sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.25.12.tgz",
      "integrity": "sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg==",
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
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.25.12.tgz",
      "integrity": "sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ==",
      "cpu": [
        "x64"
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
    "node_modules/@esbuild/linux-arm": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.25.12.tgz",
      "integrity": "sha512-lPDGyC1JPDou8kGcywY0YILzWlhhnRjdof3UlcoqYmS9El818LLfJJc3PXXgZHrHCAKs/Z2SeZtDJr5MrkxtOw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.25.12.tgz",
      "integrity": "sha512-8bwX7a8FghIgrupcxb4aUmYDLp8pX06rGh5HqDT7bB+8Rdells6mHvrFHHW2JAOPZUbnjUpKTLg6ECyzvas2AQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.25.12.tgz",
      "integrity": "sha512-0y9KrdVnbMM2/vG8KfU0byhUN+EFCny9+8g202gYqSSVMonbsCfLjUO+rCci7pM0WBEtz+oK/PIwHkzxkyharA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.25.12.tgz",
      "integrity": "sha512-h///Lr5a9rib/v1GGqXVGzjL4TMvVTv+s1DPoxQdz7l/AYv6LDSxdIwzxkrPW438oUXiDtwM10o9PmwS/6Z0Ng==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.25.12.tgz",
      "integrity": "sha512-iyRrM1Pzy9GFMDLsXn1iHUm18nhKnNMWscjmp4+hpafcZjrr2WbT//d20xaGljXDBYHqRcl8HnxbX6uaA/eGVw==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.25.12.tgz",
      "integrity": "sha512-9meM/lRXxMi5PSUqEXRCtVjEZBGwB7P/D4yT8UG/mwIdze2aV4Vo6U5gD3+RsoHXKkHCfSxZKzmDssVlRj1QQA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.25.12.tgz",
      "integrity": "sha512-Zr7KR4hgKUpWAwb1f3o5ygT04MzqVrGEGXGLnj15YQDJErYu/BGg+wmFlIDOdJp0PmB0lLvxFIOXZgFRrdjR0w==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.25.12.tgz",
      "integrity": "sha512-MsKncOcgTNvdtiISc/jZs/Zf8d0cl/t3gYWX8J9ubBnVOwlk65UIEEvgBORTiljloIWnBzLs4qhzPkJcitIzIg==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.25.12.tgz",
      "integrity": "sha512-uqZMTLr/zR/ed4jIGnwSLkaHmPjOjJvnm6TVVitAa08SLS9Z0VM8wIRx7gWbJB5/J54YuIMInDquWyYvQLZkgw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.25.12.tgz",
      "integrity": "sha512-xXwcTq4GhRM7J9A8Gv5boanHhRa/Q9KLVmcyXHCTaM4wKfIpWkdXiMog/KsnxzJ0A1+nD+zoecuzqPmCRyBGjg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.25.12.tgz",
      "integrity": "sha512-Ld5pTlzPy3YwGec4OuHh1aCVCRvOXdH8DgRjfDy/oumVovmuSzWfnSJg+VtakB9Cm0gxNO9BzWkj6mtO1FMXkQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.25.12.tgz",
      "integrity": "sha512-fF96T6KsBo/pkQI950FARU9apGNTSlZGsv1jZBAlcLL1MLjLNIWPBkj5NlSz8aAzYKg+eNqknrUJ24QBybeR5A==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.25.12.tgz",
      "integrity": "sha512-MZyXUkZHjQxUvzK7rN8DJ3SRmrVrke8ZyRusHlP+kuwqTcfWLyqMOE3sScPPyeIXN/mDJIfGXvcMqCgYKekoQw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openharmony-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.25.12.tgz",
      "integrity": "sha512-rm0YWsqUSRrjncSXGA7Zv78Nbnw4XL6/dzr20cyrQf7ZmRcsovpcRBdhD43Nuk3y7XIoW2OxMVvwuRvk9XdASg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.25.12.tgz",
      "integrity": "sha512-3wGSCDyuTHQUzt0nV7bocDy72r2lI33QL3gkDNGkod22EsYl04sMf0qLb8luNKTOmgF/eDEDP5BFNwoBKH441w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.25.12.tgz",
      "integrity": "sha512-rMmLrur64A7+DKlnSuwqUdRKyd3UE7oPJZmnljqEptesKM8wx9J8gx5u0+9Pq0fQQW8vqeKebwNXdfOyP+8Bsg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.25.12.tgz",
      "integrity": "sha512-HkqnmmBoCbCwxUKKNPBixiWDGCpQGVsrQfJoVGYLPT41XWF8lHuE5N6WhVia2n4o5QK5M4tYr21827fNhi4byQ==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.25.12.tgz",
      "integrity": "sha512-alJC0uCZpTFrSL0CCDjcgleBXPnCrEAhTBILpeAp7M/OFgoqtAetfBzX0xM00MUsVVPpVjlPuMbREqnZCXaTnA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@isaacs/cliui": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/@isaacs/cliui/-/cliui-8.0.2.tgz",
      "integrity": "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==",
      "dev": true,
      "dependencies": {
        "string-width": "^5.1.2",
        "string-width-cjs": "npm:string-width@^4.2.0",
        "strip-ansi": "^7.0.1",
        "strip-ansi-cjs": "npm:strip-ansi@^6.0.1",
        "wrap-ansi": "^8.1.0",
        "wrap-ansi-cjs": "npm:wrap-ansi@^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@isaacs/cliui/node_modules/ansi-regex": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.0.1.tgz",
      "integrity": "sha512-n5M855fKb2SsfMIiFFoVrABHJC8QtHwVx+mHWP3QcEqBHYienj5dHSgjbxtC0WEZXYt4wcD6zrQElDPhFuZgfA==",
      "dev": true,
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/@isaacs/cliui/node_modules/emoji-regex": {
      "version": "9.2.2",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-9.2.2.tgz",
      "integrity": "sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==",
      "dev": true
    },
    "node_modules/@isaacs/cliui/node_modules/string-width": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-5.1.2.tgz",
      "integrity": "sha512-HnLOCR3vjcY8beoNLtcjZ5/nxn2afmME6lhrDrebokqMap+XbeW8n9TXpPDOqdGK5qcI3oT0GKTW6wC7EMiVqA==",
      "dev": true,
      "dependencies": {
        "eastasianwidth": "^0.2.0",
        "em
... [TRUNCATED]
```

### File: postcjs.js
```js
require("fs").writeFileSync("./dist/cjs/package.json", '{"type":"commonjs"}', "utf-8")

```

### File: postesm.js
```js
require("fs").writeFileSync("./dist/esm/package.json", '{"type":"module"}', "utf-8")

```

### File: tsconfig.cjs.json
```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "commonjs",
    "outDir": "dist/cjs",
    "strict": true,
    "skipLibCheck": true,
    "esModuleInterop": true
  },
  "include": ["src"]
}

```

### File: tsconfig.esm.json
```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "es2020",
    "outDir": "dist/esm",
    "strict": true,
    "skipLibCheck": true,
    "esModuleInterop": true
  },
  "include": ["src"]
}

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "strict": true,
    "noEmit": true,
    "skipLibCheck": true,
    "esModuleInterop": true
  },
  "include": ["src"]
}

```

### File: tsconfig.types.json
```json
{
  "compilerOptions": {
    "declaration": true,
    "emitDeclarationOnly": true,
    "outDir": "dist/types",
    "strict": true,
    "skipLibCheck": true,
    "esModuleInterop": true
  },
  "include": ["src"]
}

```

### File: src\cli.ts
```ts
#!/usr/bin/env node
import { jsonSchemaToZod } from "./jsonSchemaToZod.js";
import { writeFileSync, mkdirSync } from "fs";
import { dirname } from "path";
import { parseArgs, parseOrReadJSON, readPipe } from "./utils/cliTools.js";
import { JsonSchema, ZodVersion } from "./Types.js";

const params = {
  input: {
    shorthand: "i",
    value: "string",
    required:
      process.stdin.isTTY &&
      "input is required when no JSON or file path is piped",
    description: "JSON or a source file path. Required if no data is piped.",
  },
  output: {
    shorthand: "o",
    value: "string",
    description:
      "A file path to write to. If not supplied stdout will be used.",
  },
  name: {
    shorthand: "n",
    value: "string",
    description: "The name of the schema in the output.",
  },
  depth: {
    shorthand: "d",
    value: "number",
    description:
      "Maximum depth of recursion before falling back to z.any(). Defaults to 0.",
  },
  module: {
    shorthand: "m",
    value: ["esm", "cjs", "none"],
    description: "Module syntax; 'esm', 'cjs' or 'none'. Defaults to 'esm'.",
  },
  type: {
    shorthand: "t",
    value: "string",
    description: "The name of the (optional) inferred type export."
  },
  noImport: {
    shorthand: "ni",
    description: "Removes the `import { z } from 'zod';` or equivalent from the output."
  },
  withJsdocs: {
    shorthand: "wj",
    description: "Generate jsdocs off of the description property.",
  },
  zodVersion: {
    shorthand: "zv",
    value: "number",
    description: "Target Zod version: 3 or 4. Defaults to 4.",
  },
} as const;

async function main() {
  const args = parseArgs(params, process.argv, true);
  const input = args.input || (await readPipe());
  const jsonSchema = parseOrReadJSON(input);
  const zodVersion = (args.zodVersion === 3 ? 3 : 4) as ZodVersion;
  const zodSchema = jsonSchemaToZod(jsonSchema as JsonSchema, {
    name: args.name,
    depth: args.depth,
    module: args.module || "esm",
    noImport: args.noImport,
    type: args.type,
    withJsdocs: args.withJsdocs,
    zodVersion,
  });

  if (args.output) {
    mkdirSync(dirname(args.output), { recursive: true });
    writeFileSync(args.output, zodSchema);
  } else {
    console.log(zodSchema);
  }
}

void main();

```

### File: src\index.ts
```ts
export * from "./Types.js"
export * from "./jsonSchemaToZod.js"
export * from "./parsers/parseAllOf.js"
export * from "./parsers/parseAnyOf.js"
export * from "./parsers/parseArray.js"
export * from "./parsers/parseBoolean.js"
export * from "./parsers/parseConst.js"
export * from "./parsers/parseDefault.js"
export * from "./parsers/parseEnum.js"
export * from "./parsers/parseIfThenElse.js"
export * from "./parsers/parseMultipleType.js"
export * from "./parsers/parseNot.js"
export * from "./parsers/parseNull.js"
export * from "./parsers/parseNullable.js"
export * from "./parsers/parseNumber.js"
export * from "./parsers/parseObject.js"
export * from "./parsers/parseOneOf.js"
export * from "./parsers/parseSchema.js"
export * from "./parsers/parseSimpleDiscriminatedOneOf.js"
export * from "./parsers/parseString.js"
export * from "./utils/half.js"
export * from "./utils/jsdocs.js"
export * from "./utils/omit.js"
export * from "./utils/withMessage.js"
import { jsonSchemaToZod } from "./jsonSchemaToZod.js"
export default jsonSchemaToZod
```

### File: src\jsonSchemaToZod.ts
```ts
import { Options, JsonSchema } from "./Types.js";
import { parseSchema } from "./parsers/parseSchema.js";
import { expandJsdocs } from "./utils/jsdocs.js";

export const jsonSchemaToZod = (
  schema: JsonSchema,
  { module, name, type, noImport, zodVersion = 4, ...rest }: Options = {},
): string => {
  if (type && (!name || module !== "esm")) {
    throw new Error(
      "Option `type` requires `name` to be set and `module` to be `esm`",
    );
  }

  let result = parseSchema(schema, {
    module,
    name,
    path: [],
    seen: new Map(),
    zodVersion,
    ...rest,
  });

  const jsdocs = rest.withJsdocs && typeof schema !== "boolean" && schema.description
    ? expandJsdocs(schema.description)
    : "";

  if (module === "cjs") {
    result = `${jsdocs}module.exports = ${name ? `{ ${JSON.stringify(name)}: ${result} }` : result}
`;

    if (!noImport) {
      result = `${jsdocs}const { z } = require("zod")

${result}`;
    }
  } else if (module === "esm") {
    result = `${jsdocs}export ${name ? `const ${name} =` : `default`} ${result}
`;

    if (!noImport) {
      result = `import { z } from "zod"

${result}`;
    }
  } else if (name) {
    result = `${jsdocs}const ${name} = ${result}`;
  }

  if (type && name) {
    let typeName =
      typeof type === "string"
        ? type
        : `${name[0].toUpperCase()}${name.substring(1)}`;

    result += `export type ${typeName} = z.infer<typeof ${name}>
`;
  }

  return result;
};

```

### File: src\Types.ts
```ts
export type Serializable =
  | { [key: string]: Serializable }
  | Serializable[]
  | string
  | number
  | boolean
  | null;

export type JsonSchema = JsonSchemaObject | boolean;
export type JsonSchemaObject = {
  // left permissive by design
  type?: string | string[];

  // object
  properties?: { [key: string]: JsonSchema };
  additionalProperties?: JsonSchema;
  unevaluatedProperties?: JsonSchema;
  patternProperties?: { [key: string]: JsonSchema };
  minProperties?: number;
  maxProperties?: number;
  required?: string[] | boolean;
  propertyNames?: JsonSchema;

  // array
  items?: JsonSchema | JsonSchema[];
  additionalItems?: JsonSchema;
  minItems?: number;
  maxItems?: number;
  uniqueItems?: boolean;

  // string
  minLength?: number;
  maxLength?: number;
  pattern?: string;
  format?: string;

  // number
  minimum?: number;
  maximum?: number;
  exclusiveMinimum?: number | boolean;
  exclusiveMaximum?: number | boolean;
  multipleOf?: number;

  // unions
  anyOf?: JsonSchema[];
  allOf?: JsonSchema[];
  oneOf?: JsonSchema[];

  if?: JsonSchema;
  then?: JsonSchema;
  else?: JsonSchema;

  // shared
  const?: Serializable;
  enum?: Serializable[];

  errorMessage?: { [key: string]: string | undefined };
} & { [key: string]: any };

export type ParserSelector = (schema: JsonSchemaObject, refs: Refs) => string;
export type ParserOverride = (
  schema: JsonSchemaObject,
  refs: Refs,
) => string | void;

export type ZodVersion = 3 | 4;

export type Options = {
  name?: string;
  module?: "cjs" | "esm" | "none";
  withoutDefaults?: boolean;
  withoutDescribes?: boolean;
  withJsdocs?: boolean;
  parserOverride?: ParserOverride;
  depth?: number;
  type?: boolean | string;
  noImport?: boolean;
  zodVersion?: ZodVersion;
};

export type Refs = Options & {
  path: (string | number)[];
  seen: Map<object | boolean, { n: number; r: string | undefined }>;
};

export type SimpleDiscriminatedOneOfSchema<D extends string = string> = JsonSchemaObject & {
  oneOf: (JsonSchemaObject & {
    type: "object";
    properties: {
      [K in D]: JsonSchemaObject & { type: "string" };
    } & {
      [key: string]: JsonSchemaObject
    };
  })[];
  discriminator: {
    propertyName: D;
  };
}

```

### File: test\all.json
```json
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "properties": {
    "allOf": {
      "allOf": [
        {
          "type": "boolean"
        },
        {
          "type": "number"
        },
        {
          "type": "string"
        }
      ]
    },
    "anyOf": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "number"
        },
        {
          "type": "string"
        }
      ]
    },
    "oneOf": {
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "type": "number"
        },
        {
          "type": "string"
        }
      ]
    },
    "array": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 2,
      "maxItems": 3
    },
    "tuple": {
      "type": "array",
      "items": [
        {
          "type": "boolean"
        },
        {
          "type": "number"
        },
        {
          "type": "string"
        }
      ],
      "minItems": 2,
      "maxItems": 3
    },
    "const": {
      "const": "xbox"
    },
    "enum": {
      "enum": ["ps4", "ps5"]
    },
    "ifThenElse": {
      "if": {
        "type": "string"
      },
      "then": {
        "const": "x"
      },
      "else": {
        "enum": [1, 2, 3]
      }
    },
    "null": {
      "type": "null"
    },
    "multiple": {
      "type": ["array", "boolean"]
    },
    "objAdditionalTrue": {
      "type": "object",
      "properties": {
        "x": {
          "type": "string"
        }
      },
      "additionalProperties": true
    },
    "objAdditionalFalse": {
      "type": "object",
      "properties": {
        "x": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "objAdditionalNumber": {
      "type": "object",
      "properties": {
        "x": {
          "type": "string"
        }
      },
      "additionalProperties": {
        "type": "number"
      }
    },
    "objAdditionalOnly": {
      "type": "object",
      "additionalProperties": {
        "type": "number"
      }
    },
    "patternProps": {
      "type": "object",
      "patternProperties": {
        "^x": {
          "type": "string"
        },
        "^y": {
          "type": "number"
        }
      },
      "properties": {
        "z": {
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  }
}

```

### File: test\cli.ts
```ts
import { spawnSync } from 'node:child_process';
import { suite } from "./suite";

suite("cli", (test) => {
  test("runs cli (help)", (assert) => {
    const { stdout } = spawnSync('tsx', ['src/cli.ts', '-h'], {
      encoding: 'utf8'
    });
    assert(stdout.includes('--input'));
  });

  test("runs cli (input only)", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '-i', 'test/all.json'
    ], {
      encoding: 'utf8'
    });
    assert(!stderr);
  });

  test("runs cli (noImport)", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '-i', 'test/all.json',
      '--noImport'
    ], {
      encoding: 'utf8'
    });
    assert(!stderr);
  });

  test("runs cli (stdin only)", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts'
    ], {
      input: '{"type": "any"}',
      encoding: 'utf8'
    });
    assert(!stderr);
  });

  test("runs cli (output)", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '--output', 'test/output/output.js',
      '-i', 'test/all.json'
    ], {
      encoding: 'utf8'
    });
    assert(!stderr);
  });

  test("runs cli (output with depth)", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '--output', 'test/output/output.js',
      '-i', 'test/all.json',
      '-d', '2'
    ], {
      encoding: 'utf8'
    });
    assert(!stderr);
  });

  test("cli should err with with missing input", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '--output', 'test/output/output.js'
    ], {
      encoding: 'utf8'
    });
    assert(stderr.includes('Unexpected end of JSON input'));
  });

  test("cli should err with with bad depth", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '--output', 'test/output/output.js',
      '-i', 'test/all.json',
      '-d', 'abc'
    ], {
      encoding: 'utf8'
    });
    assert(stderr.includes('Value of argument depth must be a valid number'));
  });

  test("cli should err with with missing depth", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '--output', 'test/output/output.js',
      '-i', 'test/all.json',
      '-d'
    ], {
      encoding: 'utf8'
    });
    assert(stderr.includes('Expected a value for argument depth'));
  });

  test("cli should err with bad array value", (assert) => {
    const { stderr } = spawnSync('tsx', [
      'src/cli.ts',
      '--output', 'test/output/output.js',
      '-i', 'test/all.json',
      '-m', 'notAModule'
    ], {
      encoding: 'utf8'
    });
    assert(stderr.includes('Value of argument module must be one of esm,cjs,none'));
  });
});

```

### File: test\eval.test.ts
```ts
import { jsonSchemaToZod } from "../src/jsonSchemaToZod.js";
import ts from "typescript";
import { suite } from "./suite";

suite("eval", (test) => {
  test("is usable I guess", (assert) => {
    const zodSchema = eval(
      jsonSchemaToZod({ type: "string" }, { module: "cjs" }),
    );

    assert(zodSchema.safeParse("Please just use Ajv instead"), {
      success: true,
      data: "Please just use Ajv instead",
    });
  });

  test("oneOf accepts input when exactly one schema passes", (assert) => {
    const generated = jsonSchemaToZod(
      {
        oneOf: [
          {
            type: "object",
            properties: {
              a: { type: "string" },
            },
            required: ["a"],
          },
          {
            type: "object",
            properties: {
              b: { type: "number" },
              c: { type: "boolean" },
            },
            required: ["b", "c"],
          },
        ],
      },
      { module: "cjs" },
    );
    const zodSchema = eval(
      ts.transpileModule(generated, {
        compilerOptions: {
          module: ts.ModuleKind.CommonJS,
          target: ts.ScriptTarget.ES2020,
        },
      }).outputText,
    );

    assert(zodSchema.safeParse({ a: "ok" }), {
      success: true,
      data: { a: "ok" },
    });
  });
});

```

### File: test\index.ts
```ts
import "./jsonSchemaToZod.test.js";
import "./cli.js";
import "./eval.test.js";
import "./parsers/parseAnyOf.test.js";
import "./parsers/parseAllOf.test.js";
import "./parsers/parseArray.test.js";
import "./parsers/parseConst.test.js";
import "./parsers/parseEnum.test.js";
import "./parsers/parseNot.test.js";
import "./parsers/parseNullable.test.js"
import "./parsers/parseNumber.test.js";
import "./parsers/parseObject.test.js";
import "./parsers/parseSimpleDiscriminatedOneOf.test.js";
import "./parsers/parseOneOf.test.js";
import "./parsers/parseSchema.test.js";
import "./parsers/parseMultipleType.test.js";
import "./parsers/parseString.test.js";
import "./utils/cliTools.test.js";
import "./utils/omit.test.js";
import "./utils/half.test.js";

```

### File: test\jsonSchemaToZod.test.ts
```ts
import {
  JSONSchema4,
  JSONSchema6Definition,
  JSONSchema7Definition,
} from "json-schema";
import jsonSchemaToZod from "../src";
import { suite } from "./suite";

suite("jsonSchemaToZod", (test) => {
  test("should accept json schema 7 and 4", (assert) => {
    const schema = { type: "string" } as unknown;

    assert(jsonSchemaToZod(schema as JSONSchema4));
    assert(jsonSchemaToZod(schema as JSONSchema6Definition));
    assert(jsonSchemaToZod(schema as JSONSchema7Definition));
  });

  test("should produce a string of JS code creating a Zod schema from a simple JSON schema", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.string()
`,
    );
  });

  test("should be possible to skip the import line", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
        },
        { module: "esm", noImport: true },
      ),
      `export default z.string()
`,
    );
  });

  test("should be possible to add types", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
        },
        { name: "mySchema", module: "esm", type: true },
      ),
      `import { z } from "zod"

export const mySchema = z.string()
export type MySchema = z.infer<typeof mySchema>
`,
    );
  });

  test("should be possible to add types with a custom name template", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
        },
        { name: "mySchema", module: "esm", type: "MyType" },
      ),
      `import { z } from "zod"

export const mySchema = z.string()
export type MyType = z.infer<typeof mySchema>
`,
    );
  });

  test("should throw when given module cjs and type", (assert) => {
    let didThrow = false;

    try {
      jsonSchemaToZod(
        { type: "string" },
        { name: "hello", module: "cjs", type: true },
      );
    } catch {
      didThrow = true;
    }

    assert(didThrow);
  });

  test("should throw when given type but no name", (assert) => {
    let didThrow = false;

    try {
      jsonSchemaToZod({ type: "string" }, { module: "esm", type: true });
    } catch {
      didThrow = true;
    }

    assert(didThrow);
  });

  test("should include defaults", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
          default: "foo",
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.string().default("foo")
`,
    );
  });

  test("should include falsy defaults", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
          default: "",
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.string().default("")
`,
    );
  });

  test("should include falsy defaults", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
          const: "",
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.literal("")
`,
    );
  });

  test("can exclude defaults", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
          default: "foo",
        },
        { module: "esm", withoutDefaults: true },
      ),
      `import { z } from "zod"

export default z.string()
`,
    );
  });

  test("should include describes", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
          description: "foo",
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.string().describe("foo")
`,
    );
  });

  test("can exclude describes", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "string",
          description: "foo",
        },
        { module: "esm", withoutDescribes: true },
      ),
      `import { z } from "zod"

export default z.string()
`,
    );
  });

  test("can include jsdocs", (assert) => {
    assert(
      jsonSchemaToZod({
        type: "object",
        description: "Description for schema",
        properties: {
          prop: {
            type: "string",
            description: "Description for prop"
          },
          obj: {
            type: "object",
            description: "Description for object that is multiline\nMore content\n\nAnd whitespace",
            properties: {
              nestedProp: {
                type: "string",
                description: "Description for nestedProp"
              },
              nestedProp2: {
                type: "string",
                description: "Description for nestedProp2"
              },
            },
          }
        }
      }, { module: "esm", withJsdocs: true }),
      `import { z } from "zod"

/**Description for schema*/
export default z.object({ 
/**Description for prop*/
"prop": z.string().describe("Description for prop").optional(), 
/**
* Description for object that is multiline
* More content
* 
* And whitespace
*/
"obj": z.object({ 
/**Description for nestedProp*/
"nestedProp": z.string().describe("Description for nestedProp").optional(), 
/**Description for nestedProp2*/
"nestedProp2": z.string().describe("Description for nestedProp2").optional() }).describe("Description for object that is multiline\\nMore content\\n\\nAnd whitespace").optional() }).describe("Description for schema")
`);
  });

  test("will remove optionality if default is present", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "object",
          properties: {
            prop: {
              type: "string",
              default: "def",
            },
          },
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.object({ "prop": z.string().default("def") })
`,
    );
  });

  test("will handle falsy defaults", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "boolean",
          default: false,
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.boolean().default(false)
`,
    );
  });

  test("will ignore undefined as default", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          type: "null",
          default: undefined,
        },
        { module: "esm" },
      ),
      `import { z } from "zod"

export default z.null()
`,
    );
  });

  test("should be possible to define a custom parser", (assert) => {
    assert(
      jsonSchemaToZod(
        {
          allOf: [
            { type: "string" },
            { type: "number" },
            { type: "boolean", description: "foo" },
          ],
        },
        {
          // module: false,
          parserOverride: (schema, refs) => {
            if (
              refs.path.length === 2 &&
              refs.path[0] === "allOf" &&
              refs.path[1] === 2 &&
              schema.type === "boolean" &&
              schema.description === "foo"
            ) {
              return "myCustomZodSchema";
            }
          },
        },
      ),

      `z.intersection(z.string(), z.intersection(z.number(), myCustomZodSchema))`,
    );
  });

  test("can output with cjs and a name", (assert) => {
    assert(jsonSchemaToZod({
      type: "string"
    }, { module: "cjs", name: "someName" }), `const { z } = require("zod")

module.exports = { "someName": z.string() }
`);
  });

  test("can output with cjs and no name", (assert) => {
    assert(jsonSchemaToZod({
      type: "string"
    }, { module: "cjs" }), `const { z } = require("zod")

module.exports = z.string()
`);
  });

  test("can output with name only", (assert) => {
    assert(jsonSchemaToZod({
      type: "string"
    }, { name: "someName" }), "const someName = z.string()");
  });

  test("can exclude name", (assert) => {
    assert(jsonSchemaToZod(true), "z.any()");
  });
});

```

### File: test\suite.ts
```ts
import util from "util";
import diff from "fast-diff";

const RED = "\x1b[31m";
const GREEN = "\x1b[32m";
const RESET = "\x1b[39m";

type TestContext = (assert: (result: any, expected?: any) => void) => void;
type TestFunction = (name: string, context: TestContext) => void;
type SuiteContext = (test: TestFunction) => void;
type Error = { expected: any; got: any };
type ErrorMap = { [key: string]: Error | ErrorMap };

export function suite(suiteName: string, suiteContext: SuiteContext): void {
  let tests = 0;
  let passedTests = 0;

  const test: TestFunction = (testName, testContext) => {
    tests++;

    let assertions = 0;
    let passedAssertions = 0;
    try {
      testContext((...args) => {
        assertions++;

        const error =
          args.length === 2
            ? assert(args[0], args[1], [])
            : args[0]
            ? undefined
            : { expected: "truthy", got: args[0] };

        if (!error) {
          passedAssertions++;
        } else {
          let errorString =
            typeof error.got === "string" && typeof error.expected === "string"
              ? "\n" + colorDiff(error.got, error.expected)
              : util.inspect(error, { depth: null });

          if (!errorString.endsWith("\n")) {
            errorString += "\n";
          }

          console.error(
            `❌ '${suiteName}', '${testName}', assertion ${assertions} failed:`,
            errorString,
          );
        }
      });

      if (assertions === 0) {
        console.log(`⚠ '${suiteName}', '${testName}': No assertions found`);
      }

      if (assertions === passedAssertions) {
        passedTests++;
      }
    } catch (e) {
      console.error(
        `❌ '${suiteName}', '${testName}': Error thrown after ${assertions} ${
          assertions === 1 ? "assertion" : "assertions"
        }. Error:`,
        e,
      );
    }
  };

  suiteContext(test);
  if (tests === 0) {
    console.log(`⚠ '${suiteName}': No tests found`);
  } else if (tests === passedTests) {
    console.log(
      `✔ '${suiteName}': ${tests} ${tests === 1 ? "test" : "tests"} passed`,
    );
  } else {
    console.error(
      `❌ '${suiteName}': ${passedTests}/${tests} ${
        passedTests === 1 ? "test" : "tests"
      } passed`,
    );
    process.exitCode = 1;
  }
}

function assert(
  a: unknown,
  b: unknown,
  path: (string | number)[],
): Error | ErrorMap | undefined {
  if (a === b) {
    return undefined;
  }

  if (typeof a === "object") {
    if (typeof b !== "object") {
      return { expected: typeof a, got: typeof b };
    }

    if (a === null) {
      return { expected: null, got: b };
    }

    if (b === null) {
      return { expected: a, got: null };
    }

    if (Array.isArray(a)) {
      if (!Array.isArray(b)) {
        return { expected: "array", got: b };
      }
    } else if (Array.isArray(b)) {
      return { expected: a, got: "array" };
    }

    const keysA = Object.keys(a).sort();
    const keysB = Object.keys(b).sort();

    if (keysA.join() !== keysB.join()) {
      return { got: keysA, expected: keysB };
    }

    let foundError = false;

    const errorMap = [...keysA, ...keysB].reduce((errorMap: ErrorMap, key) => {
      if (key in errorMap) {
        return errorMap;
      }

      const error = assert(a[key], b[key], [...path, key]);

      if (error) {
        foundError = true;

        errorMap[key] = error;
      }

      return errorMap;
    }, {});

    if (foundError) {
      return errorMap;
    } else {
      return undefined;
    }
  }

  if (
    typeof a === "function" &&
    typeof b === "function" &&
    a.toString() === b.toString()
  ) {
    return undefined;
  }

  if (typeof a !== typeof b) {
    return { got: typeof a, expected: typeof b };
  }

  return { got: a, expected: b };
}

export function colorDiff(got: string, exp: string) {
  return diff(got, exp).reduce(
    (acc, [type, value]) =>
      acc + (type === -1 ? GREEN : type === 1 ? RED : RESET) + value,
    "",
  );
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
