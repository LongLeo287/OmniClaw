---
id: github.com-privatenumber-resolve-pkg-maps-d898ffbd
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:15.470815
---

# KNOWLEDGE EXTRACT: github.com_privatenumber_resolve-pkg-maps_d898ffbd
> **Extracted on:** 2026-04-01 10:33:22
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520961/github.com_privatenumber_resolve-pkg-maps_d898ffbd

---

## File: `.editorconfig`
```
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.yml]
indent_style = space
indent_size = 2
```

## File: `.gitattributes`
```
* text=auto eol=lf
```

## File: `.gitignore`
```
# macOS
.DS_Store

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Dependency directories
node_modules/

# Output of 'npm pack'
*.tgz

# dotenv environment variables file
.env
.env.test

# VSCode
.vscode

# Distribution
dist

# Cache
.eslintcache
```

## File: `.nvmrc`
```
v16.15.1
```

## File: `LICENSE`
```
MIT License

Copyright (c) Hiroki Osame <hiroki.osame@gmail.com>

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

## File: `README.md`
```markdown
# resolve-pkg-maps

Utils to resolve `package.json` subpath & conditional [`exports`](https://nodejs.org/api/packages.html#exports)/[`imports`](https://nodejs.org/api/packages.html#imports) in resolvers.

Implements the [ESM resolution algorithm](https://nodejs.org/api/esm.html#resolver-algorithm-specification). Tested [against Node.js](/tests/) for accuracy.

<sub>Support this project by ⭐️ starring and sharing it. [Follow me](https://github.com/privatenumber) to see what other cool projects I'm working on! ❤️</sub>

## Usage

### Resolving `exports`

_utils/package.json_
```json5
{
    // ...
    "exports": {
        "./reverse": {
            "require": "./file.cjs",
            "default": "./file.mjs"
        }
    },
    // ...
}
```

```ts
import { resolveExports } from 'resolve-pkg-maps'

const [packageName, packageSubpath] = parseRequest('utils/reverse')

const resolvedPaths: string[] = resolveExports(
    getPackageJson(packageName).exports,
    packageSubpath,
    ['import', ...otherConditions]
)
// => ['./file.mjs']
```

### Resolving `imports`

_package.json_
```json5
{
    // ...
    "imports": {
        "#supports-color": {
            "node": "./index.js",
            "default": "./browser.js"
        }
    },
    // ...
}
```

```ts
import { resolveImports } from 'resolve-pkg-maps'

const resolvedPaths: string[] = resolveImports(
    getPackageJson('.').imports,
    '#supports-color',
    ['node', ...otherConditions]
)
// => ['./index.js']
```

## API

### resolveExports(exports, request, conditions)

Returns: `string[]`

Resolves the `request` based on `exports` and `conditions`. Returns an array of paths (e.g. in case a fallback array is matched).

#### exports

Type:
```ts
type Exports = PathOrMap | readonly PathOrMap[]

type PathOrMap = string | PathConditionsMap

type PathConditionsMap = {
    [condition: string]: PathConditions | null
}
```

The [`exports` property](https://nodejs.org/api/packages.html#exports) value in `package.json`.

#### request

Type: `string`

The package subpath to resolve. Assumes a normalized path is passed in (eg. [repeating slashes `//`](https://github.com/nodejs/node/issues/44316)).

It _should not_ start with `/` or `./`.

Example: if the full import path is `some-package/subpath/file`, the request is `subpath/file`.


#### conditions

Type: `readonly string[]`

An array of conditions to use when resolving the request. For reference, Node.js's default conditions are [`['node', 'import']`](https://nodejs.org/api/esm.html#:~:text=defaultConditions%20is%20the%20conditional%20environment%20name%20array%2C%20%5B%22node%22%2C%20%22import%22%5D.).

The order of this array does not matter; the order of condition keys in the export map is what matters instead.

Not all conditions in the array need to be met to resolve the request. It just needs enough to resolve to a path.

---

### resolveImports(imports, request, conditions)

Returns: `string[]`

Resolves the `request` based on `imports` and `conditions`. Returns an array of paths (e.g. in case a fallback array is matched).

#### imports

Type:
```ts
type Imports = {
    [condition: string]: PathOrMap | readonly PathOrMap[] | null
}

type PathOrMap = string | Imports
```

The [`imports` property](https://nodejs.org/api/packages.html#imports) value in `package.json`.


#### request

Type: `string`

The request resolve. Assumes a normalized path is passed in (eg. [repeating slashes `//`](https://github.com/nodejs/node/issues/44316)).

> **Note:** In Node.js, imports resolutions are limited to requests prefixed with `#`. However, this package does not enforce that requirement in case you want to add custom support for non-prefixed entries.

#### conditions

Type: `readonly string[]`

An array of conditions to use when resolving the request. For reference, Node.js's default conditions are [`['node', 'import']`](https://nodejs.org/api/esm.html#:~:text=defaultConditions%20is%20the%20conditional%20environment%20name%20array%2C%20%5B%22node%22%2C%20%22import%22%5D.).

The order of this array does not matter; the order of condition keys in the import map is what matters instead.

Not all conditions in the array need to be met to resolve the request. It just needs enough to resolve to a path.

---

### Errors

#### `ERR_PACKAGE_PATH_NOT_EXPORTED`
 - If the request is not exported by the export map

#### `ERR_PACKAGE_IMPORT_NOT_DEFINED`
  - If the request is not defined by the import map

#### `ERR_INVALID_PACKAGE_CONFIG`

  - If an object contains properties that are both paths and conditions (e.g. start with and without `.`)
  - If an object contains numeric properties 
  
#### `ERR_INVALID_PACKAGE_TARGET`
  - If a resolved exports path is not a valid path (e.g. not relative or has protocol)
  - If a resolved path includes `..` or `node_modules`
  - If a resolved path is a type that cannot be parsed

## FAQ

### Why do the APIs return an array of paths?

`exports`/`imports` supports passing in a [fallback array](https://github.com/jkrems/proposal-pkg-exports/#:~:text=Whenever%20there%20is,to%20new%20cases.) to provide fallback paths if the previous one is invalid:

```json5
{
    "exports": {
        "./feature": [
            "./file.js",
            "./fallback.js"
        ]
    }
}
```

Node.js's implementation [picks the first valid path (without attempting to resolve it)](https://github.com/nodejs/node/issues/44282#issuecomment-1220151715) and throws an error if it can't be resolved. Node.js's fallback array is designed for [forward compatibility with features](https://github.com/jkrems/proposal-pkg-exports/#:~:text=providing%20forwards%20compatiblitiy%20for%20new%20features) (e.g. protocols) that can be immediately/inexpensively validated:

```json5
{
    "exports": {
        "./core-polyfill": ["std:core-module", "./core-polyfill.js"]
    }
}
```

However, [Webpack](https://webpack.js.org/guides/package-exports/#alternatives) and [TypeScript](https://github.com/microsoft/TypeScript/blob/71e852922888337ef51a0e48416034a94a6c34d9/src/compiler/moduleSpecifiers.ts#L695) have deviated from this behavior and attempts to resolve the next path if a path cannot be resolved.

By returning an array of matched paths instead of just the first one, the user can decide which behavior to adopt.

### How is it different from [`resolve.exports`](https://github.com/lukeed/resolve.exports)?

`resolve.exports` only resolves `exports`, whereas this package resolves both `exports` & `imports`. This comparison will only cover resolving `exports`.

- Despite it's name, `resolve.exports` handles more than just `exports`. It takes in the entire `package.json` object to handle resolving `.` and [self-references](https://nodejs.org/api/packages.html#self-referencing-a-package-using-its-name). This package only accepts `exports`/`imports` maps from `package.json` and is scoped to only resolving what's defined in the maps.

- `resolve.exports` accepts the full request (e.g. `foo/bar`), whereas this package only accepts the requested subpath (e.g. `bar`).

- `resolve.exports` only returns the first result in a fallback array. This package returns an array of results for the user to decide how to handle it.

- `resolve.exports` supports [subpath folder mapping](https://nodejs.org/docs/latest-v16.x/api/packages.html#subpath-folder-mappings) (deprecated in Node.js v16 & removed in v17) but seems to [have a bug](https://github.com/lukeed/resolve.exports/issues/7). This package does not support subpath folder mapping because Node.js has removed it in favor of using subpath patterns.

- Neither resolvers rely on a file-system

This package also addresses many of the bugs in `resolve.exports`, demonstrated in [this test](/tests/exports/compare-resolve.exports.ts).
```

## File: `package.json`
```json
{
	"name": "resolve-pkg-maps",
	"version": "0.0.0-semantic-release",
	"description": "Resolve package.json exports & imports maps",
	"keywords": [
		"node.js",
		"package.json",
		"exports",
		"imports"
	],
	"license": "MIT",
	"repository": "privatenumber/resolve-pkg-maps",
	"funding": "https://github.com/privatenumber/resolve-pkg-maps?sponsor=1",
	"author": {
		"name": "Hiroki Osame",
		"email": "hiroki.osame@gmail.com"
	},
	"type": "module",
	"files": [
		"dist"
	],
	"main": "./dist/index.cjs",
	"module": "./dist/index.mjs",
	"types": "./dist/index.d.cts",
	"exports": {
		"require": {
			"types": "./dist/index.d.cts",
			"default": "./dist/index.cjs"
		},
		"import": {
			"types": "./dist/index.d.mts",
			"default": "./dist/index.mjs"
		}
	},
	"imports": {
		"#resolve-pkg-maps": {
			"types": "./src/index.ts",
			"development": "./src/index.ts",
			"default": "./dist/index.mjs"
		}
	},
	"scripts": {
		"build": "pkgroll --target=node12.19 --minify",
		"lint": "eslint --cache .",
		"type-check": "tsc --noEmit",
		"test": "pnpm build && tsx tests",
		"dev": "tsx watch --conditions=development tests",
		"prepack": "pnpm build && clean-pkg-json"
	},
	"devDependencies": {
		"@pvtnbr/eslint-config": "^0.33.0",
		"@types/node": "^18.11.11",
		"clean-pkg-json": "^1.2.0",
		"eslint": "^8.29.0",
		"execa": "^6.1.0",
		"fs-fixture": "^1.2.0",
		"manten": "^0.6.0",
		"pkgroll": "^1.8.0",
		"resolve.exports": "^1.1.0",
		"tsx": "^3.12.1",
		"typescript": "^4.9.4"
	},
	"eslintConfig": {
		"extends": "@pvtnbr",
		"rules": {
			"unicorn/no-array-reduce": "off",
			"no-prototype-builtins": "off"
		}
	}
}
```

## File: `tsconfig.json`
```json
{
	"compilerOptions": {
		"module": "Node16",
		"isolatedModules": true,
		"esModuleInterop": true,
		"strict": true,
	}
}
```

## File: `src/exports.ts`
```typescript
import { isObject } from './utils/is-object.js';
import { createError } from './utils/create-error.js';
import { resolveConditions, Type } from './utils/resolve-conditions.js';
import { findMatchingPath } from './utils/find-matching-map-entry.js';
import {
	ERR_INVALID_PACKAGE_CONFIG,
	ERR_INVALID_PACKAGE_TARGET,
	ERR_PACKAGE_PATH_NOT_EXPORTED,
} from './utils/errors.js';
import type { PathConditions, PathConditionsMap } from './types.js';

const isConditionalObject = (
	exportsMap: PathConditionsMap,
) => Object.keys(exportsMap).reduce<boolean | undefined>(
	(firstKey, key) => {
		const isKeyConditionalSugar = key === '' || key[0] !== '.';

		if (
			firstKey === undefined
			|| firstKey === isKeyConditionalSugar
		) {
			return isKeyConditionalSugar;
		}

		throw createError(
			ERR_INVALID_PACKAGE_CONFIG,
			'"exports" cannot contain some keys starting with "." and some not',
		);
	},
	undefined,
);

const hasProtocolPattern = /^\w+:/;

// Based on https://github.com/nodejs/node/blob/v18.8.0/lib/internal/modules/esm/resolve.js#L549
export const resolveExports = (
	exports: PathConditions,
	request: string,
	conditions: readonly string[],
): string[] => {
	if (!exports) {
		throw new Error('"exports" is required');
	}

	request = request === '' ? '.' : `./${request}`;

	// https://github.com/nodejs/node/blob/v18.7.0/lib/internal/modules/esm/resolve.js#L651-L652
	if (
		typeof exports === 'string'
		|| Array.isArray(exports)
		|| (isObject(exports) && isConditionalObject(exports))
	) {
		exports = { '.': exports };
	}

	const [pathMatch, starMatch] = findMatchingPath(exports, request);

	const resolved = resolveConditions(
		Type.Export,
		exports[pathMatch as string],
		request,
		conditions,
		starMatch,
	);

	if (resolved.length === 0) {
		throw createError(
			ERR_PACKAGE_PATH_NOT_EXPORTED,
			request === '.'
				? 'No "exports" main defined'
				: `Package subpath '${request}' is not defined by "exports"`,
		);
	}

	for (const resolvedPath of resolved) {
		if (
			!resolvedPath.startsWith('./')
			&& !hasProtocolPattern.test(resolvedPath)
		) {
			throw createError(
				ERR_INVALID_PACKAGE_TARGET,
				`Invalid "exports" target "${resolvedPath}" defined in the package config`,
			);
		}
	}

	return resolved;
};
```

## File: `src/imports.ts`
```typescript
import { resolveConditions, Type } from './utils/resolve-conditions.js';
import { findMatchingPath } from './utils/find-matching-map-entry.js';
import { createError } from './utils/create-error.js';
import { ERR_PACKAGE_IMPORT_NOT_DEFINED } from './utils/errors.js';
import type { PathConditionsMap } from './types.js';

// Based on https://github.com/nodejs/node/blob/v18.8.0/lib/internal/modules/esm/resolve.js#L642
export const resolveImports = (
	imports: PathConditionsMap,
	request: string,
	conditions: readonly string[],
): string[] => {
	if (!imports) {
		throw new Error('"imports" is required');
	}

	const [pathMatch, starMatch] = findMatchingPath(imports, request);

	const resolved = resolveConditions(
		Type.Import,
		imports[pathMatch as string],
		request,
		conditions,
		starMatch,
	);

	if (resolved.length === 0) {
		throw createError(
			ERR_PACKAGE_IMPORT_NOT_DEFINED,
			`Package import specifier "${request}" is not defined in package`,
		);
	}

	return resolved;
};
```

## File: `src/index.ts`
```typescript
export * from './exports.js';
export * from './imports.js';
export * from './types.js';
```

## File: `src/types.ts`
```typescript
export type PathConditionsMap = {
	[condition: string]: PathConditions | null;
};

type PathOrMap = string | PathConditionsMap;

export type PathConditions = PathOrMap | readonly PathOrMap[];
```

## File: `src/@types/array.d.ts`
```typescript
interface ArrayConstructor {
	isArray(array: unknown): array is unknown[] | readonly unknown[];
}
```

## File: `src/utils/create-error.ts`
```typescript
export const createError = (
	code: string,
	message: string,
): Error & { code: string } => Object.assign(
	new Error(`[${code}]: ${message}`),
	{ code },
);
```

## File: `src/utils/errors.ts`
```typescript
export const ERR_INVALID_PACKAGE_CONFIG = 'ERR_INVALID_PACKAGE_CONFIG';
export const ERR_INVALID_PACKAGE_TARGET = 'ERR_INVALID_PACKAGE_TARGET';
export const ERR_PACKAGE_PATH_NOT_EXPORTED = 'ERR_PACKAGE_PATH_NOT_EXPORTED';
export const ERR_PACKAGE_IMPORT_NOT_DEFINED = 'ERR_PACKAGE_IMPORT_NOT_DEFINED';
```

## File: `src/utils/find-matching-map-entry.ts`
```typescript
import type { PathConditions } from '../types.js';

const STAR = '*';

const hasHigherSpecificity = (
	keyA: string,
	keyB: string,
) => {
	const starIndexA = keyA.indexOf(STAR);
	const starIndexB = keyB.indexOf(STAR);

	return (
		starIndexA === starIndexB
			? keyB.length > keyA.length
			: starIndexB > starIndexA
	);
};

export function findMatchingPath(
	pathConditions: PathConditions,
	request: string,
) {
	if (
		!request.includes(STAR)
		&& pathConditions.hasOwnProperty(request)
	) {
		return [request];
	}

	let pathMatch: string | undefined;
	let starMatch: string | undefined;
	for (const exportPath of Object.keys(pathConditions)) {
		if (exportPath.includes(STAR)) {
			const [prefix, suffix, remaining] = exportPath.split(STAR);

			if (
				remaining === undefined
				&& request.startsWith(prefix)
				&& request.endsWith(suffix)
			) {
				const currentStarMatch = request.slice(
					prefix.length,
					-suffix.length || undefined,
				);

				if (
					currentStarMatch
					&& (
						!pathMatch
						|| hasHigherSpecificity(pathMatch, exportPath)
					)
				) {
					pathMatch = exportPath;
					starMatch = currentStarMatch;
				}
			}
		}
	}

	return [pathMatch, starMatch];
}
```

## File: `src/utils/is-object.ts`
```typescript
export const isObject = (
	object: any,
): object is object => (
	object !== null
	&& typeof object === 'object'
);
```

## File: `src/utils/resolve-conditions.ts`
```typescript
import type { PathConditions } from '../types.js';
import { isObject } from './is-object.js';
import { createError } from './create-error.js';
import { ERR_INVALID_PACKAGE_CONFIG, ERR_INVALID_PACKAGE_TARGET } from './errors.js';

const isInteger = /^\d+$/;

// eslint-disable-next-line regexp/no-unused-capturing-group
const disallowedPathSegments = /^(\.{1,2}|node_modules)$/i;

const pathSeparator = /\/|\\/;

export enum Type {
	Export = 'exports',
	Import = 'imports',
}

export const resolveConditions = (
	type: Type,
	pathConditions: PathConditions | null,
	request: string,
	conditions: readonly string[],
	asterisk?: string,
): string[] => {
	/**
	 * Handle null or undefined
	 * Null is an acceptable value in export maps.
	 * undefined can will be passed in if there is no path match
	 * in exports or imports.
	 */
	// eslint-disable-next-line no-eq-null
	if (pathConditions == null) {
		return [];
	}

	if (typeof pathConditions === 'string') {
		const [firstSegment, ...pathSegments] = pathConditions.split(pathSeparator);

		if (
			firstSegment === '..'
			|| pathSegments.some(
				segment => disallowedPathSegments.test(segment),
			)
		) {
			throw createError(
				ERR_INVALID_PACKAGE_TARGET,
				`Invalid "${type}" target "${pathConditions}" defined in the package config`,
			);
		}

		return [
			asterisk
				? pathConditions.replace(/\*/g, asterisk)
				: pathConditions,
		];
	}

	if (Array.isArray(pathConditions)) {
		return pathConditions
			.flatMap(
				pathCondition => resolveConditions(
					type,
					pathCondition,
					request,
					conditions,
					asterisk,
				),
			);
	}

	if (isObject(pathConditions)) {
		for (const condition of Object.keys(pathConditions)) {
			if (isInteger.test(condition)) {
				throw createError(
					ERR_INVALID_PACKAGE_CONFIG,
					'Cannot contain numeric property keys',
				);
			}

			if (
				condition === 'default'
				|| conditions.includes(condition)
			) {
				return resolveConditions(
					type,
					pathConditions[condition],
					request,
					conditions,
					asterisk,
				);
			}
		}
		return [];
	}

	throw createError(
		ERR_INVALID_PACKAGE_TARGET,
		`Invalid "${type}" target "${pathConditions}"`,
	);
};
```

## File: `tests/index.ts`
```typescript
import { describe } from 'manten';

describe('resolve-pkg-maps', ({ runTestSuite }) => {
	runTestSuite(import('./exports/index.js'));
	runTestSuite(import('./imports/index.js'));
});
```

## File: `tests/exports/basic.ts`
```typescript
import { testSuite } from 'manten';
import { resolveExportsWithNode } from '../utils/resolve-with-node.js';

export default testSuite(({ describe }) => {
	describe('basic', ({ test, describe }) => {
		describe('main entry point', ({ test }) => {
			test(
				'export string',
				() => resolveExportsWithNode({
					exports: './entry.js',

					assertions: [{
						request: '',
						conditions: [],
						output: ['./entry.js'],
					}],
				}),
			);

			test(
				'export map',
				() => resolveExportsWithNode({
					exports: { '.': './entry.js' },
					assertions: [
						{
							request: '',
							conditions: [],
							output: ['./entry.js'],
						},
						{
							request: '.',
							conditions: [],
							error: '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./.\' is not defined by "exports"',
						},
					],
				}),
			);
		});

		test(
			'multiple entries',
			() => resolveExportsWithNode({
				exports: {
					'./a': './lib/a.js',
					'./.invisible': './.invisible.js',
				},

				assertions: [
					// Non relative path
					{
						request: 'a',
						conditions: [],
						output: ['./lib/a.js'],
					},

					{
						request: 'a',
						conditions: [],
						output: ['./lib/a.js'],
					},

					// Invisible file
					{
						request: '.invisible',
						conditions: [],
						output: ['./.invisible.js'],
					},
				],
			}),
		);
	});
});
```

## File: `tests/exports/compare-resolve.exports.ts`
```typescript
import { testSuite, expect } from 'manten';
// @ts-expect-error broken types
import { resolve as lukeedResolve } from 'resolve.exports';
import { nodeResolveExports } from '../utils/node-resolve.js';
import { resolveExports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('compare with resolve.exports', ({ test }) => {
		// https://github.com/lukeed/resolve.exports/issues/19
		test(
			'request starting with .',
			async () => {
				const packageJson = {
					exports: {
						'./.hidden': './file.js',
					},
				};
				const request = '.hidden';
				const conditions = ['worker', 'node'];

				// lukeed/resolve.exports: Fails
				expect(() => {
					lukeedResolve(packageJson, request, { conditions });
				}).toThrow('Missing ".hidden" export in "undefined" package');

				// resolve-pkg-maps: Passes
				expect(
					resolveExports(packageJson.exports, request, conditions),
				).toStrictEqual(['./file.js']);

				// Node.js: Expected behavior
				expect(
					await nodeResolveExports(
						packageJson.exports,
						request,
						conditions,
					),
				).toBe('./file.js');
			},
		);

		// https://github.com/lukeed/resolve.exports/issues/16
		test(
			'null target exclusion',
			async () => {
				const packageJson = {
					exports: {
						'./*': './*',
						'./file.js': null,
					},
				};
				const request = 'file.js';
				const conditions = ['worker', 'node'];

				// lukeed/resolve.exports: Fails - should be blocked
				expect(
					lukeedResolve(packageJson, request, { conditions }),
				).toBe('./file.js');

				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./file.js\' is not defined by "exports"';

				// resolve-pkg-maps: Passes
				expect(
					() => resolveExports(packageJson.exports, request, conditions),
				).toThrow(error);

				// Node.js: Expected behavior
				await expect(
					nodeResolveExports(
						packageJson.exports,
						request,
						conditions,
						{ '/file.js': '' },
					),
				).rejects.toThrow(error);
			},
		);

		// https://github.com/lukeed/resolve.exports/issues/17
		test(
			'fallback array',
			async () => {
				const packageJson = {
					exports: {
						'./file': ['http://a.com', './file.js'],
					},
				};
				const request = 'file';
				const conditions = ['worker', 'node'];

				// lukeed/resolve.exports: Fails - should leave fallback to user to handle
				expect(
					lukeedResolve(packageJson, request, { conditions }),
				).toBe('http://a.com');

				// resolve-pkg-maps: Passes - Leaves fallback up to user to handle
				expect(
					resolveExports(packageJson.exports, request, conditions),
				).toStrictEqual(['http://a.com', './file.js']);

				// Node.js: Expected behavior
				expect(
					await nodeResolveExports(
						packageJson.exports,
						request,
						conditions,
					),
				).toBe('./file.js');
			},
		);

		// https://github.com/lukeed/resolve.exports/issues/22
		test(
			'star with suffix',
			async () => {
				const packageJson = {
					exports: {
						'./*.js': './*.js',
					},
				};
				const request = 'file.js';
				const conditions = ['worker', 'node'];

				// lukeed/resolve.exports: Fails - should resolve
				expect(() => {
					lukeedResolve(packageJson, request, { conditions });
				}).toThrow('Missing "./file.js" export in "undefined" package');

				// resolve-pkg-maps: Passes - Leaves fallback up to user to handle
				expect(
					resolveExports(packageJson.exports, request, conditions),
				).toStrictEqual(['./file.js']);

				// Node.js: Expected behavior
				expect(
					await nodeResolveExports(
						packageJson.exports,
						request,
						conditions,
						{ '/file.js': '' },
					),
				).toBe('./file.js');
			},
		);

		// https://github.com/lukeed/resolve.exports/issues/9
		test(
			'multiple stars',
			async () => {
				const packageJson = {
					exports: {
						'./*.js': './*/*.js',
					},
				};
				const request = 'file.js';
				const conditions = ['worker', 'node'];

				// lukeed/resolve.exports: Fails - should resolve
				expect(() => {
					lukeedResolve(packageJson, request, { conditions });
				}).toThrow('Missing "./file.js" export in "undefined" package');

				// resolve-pkg-maps: Passes - Leaves fallback up to user to handle
				expect(
					resolveExports(packageJson.exports, request, conditions),
				).toStrictEqual(['./file/file.js']);

				// Node.js: Expected behavior
				expect(
					await nodeResolveExports(
						packageJson.exports,
						request,
						conditions,
						{ '/file/file.js': '' },
					),
				).toBe('./file/file.js');
			},
		);

		// https://github.com/lukeed/resolve.exports/issues/7
		test(
			'should apply suffix to star / order of exports should not matter',
			async () => {
				const packageJson = {
					exports: {
						'./': './',
						'./*': './*.js',
					},
				};
				const request = 'file';
				const conditions = ['worker', 'node'];

				// lukeed/resolve.exports: Fails - should have .js appended
				expect(
					lukeedResolve(packageJson, request, { conditions }),
				).toBe('./file');

				// resolve-pkg-maps: Passes
				expect(
					resolveExports(packageJson.exports, request, conditions),
				).toStrictEqual(['./file.js']);

				// Node.js: Expected behavior
				expect(
					await nodeResolveExports(
						packageJson.exports,
						request,
						conditions,
						{ '/file.js': '' },
					),
				).toBe('./file.js');
			},
		);
	});
});
```

## File: `tests/exports/conditions.ts`
```typescript
import { testSuite, expect } from 'manten';
import { nodeResolveExports } from '../utils/node-resolve.js';
import { resolveExportsWithNode } from '../utils/resolve-with-node.js';
import { resolveExports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('conditions', ({ test }) => {
		describe(
			'single entry - only conditions',
			({ test }) => {
				const exports = {
					'condition-a': './lib/a.js',
					'condition-b': './lib/b.js',
				};

				const request = '';

				test('no match', async () => {
					const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: No "exports" main defined';

					expect(
						() => resolveExports(exports, request, []),
					).toThrow(error);

					await expect(
						nodeResolveExports(exports, request, []),
					).rejects.toThrow(error);
				});

				test('match', async () => {
					const validCondition = ['condition-b'];

					expect(
						resolveExports(exports, request, validCondition),
					).toStrictEqual(['./lib/b.js']);

					expect(
						await nodeResolveExports(exports, request, validCondition),
					).toBe('./lib/b.js');
				});

				test('no match on non-existent condition', async () => {
					const invalidCondition = ['nonexistent-condition'];
					const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: No "exports" main defined';

					expect(
						() => resolveExports(exports, request, invalidCondition),
					).toThrow(error);

					await expect(
						nodeResolveExports(exports, request, invalidCondition),
					).rejects.toThrow(error);
				});
			},
		);

		test(
			'single-entry - with path',
			() => resolveExportsWithNode({
				exports: {
					'.': {
						'condition-a': './lib/a.js',
						'condition-b': './lib/b.js',
					},
				},

				assertions: [{
					request: '',
					conditions: ['condition-b'],
					output: ['./lib/b.js'],
				}],
			}),
		);

		test(
			'use default when no conditions',
			() => resolveExportsWithNode({
				exports: {
					'.': {
						'condition-a': './lib/a.js',
						default: './lib/index.js',
					},
				},

				assertions: [
					{
						request: '',
						conditions: [],
						output: ['./lib/index.js'],
					},
					{
						request: '',
						conditions: ['non-existent-condition'],
						output: ['./lib/index.js'],
					},
				],
			}),
		);

		test(
			'nested conditions',
			() => resolveExportsWithNode({
				exports: {
					node: {
						import: './node.import.js',
						require: './node.require.js',
					},
					browser: {
						import: './browser.import.js',
						require: './browser.require.js',
					},
				},

				assertions: [
					{
						request: '',
						conditions: ['require', 'node'],
						output: ['./node.require.js'],
					},
					{
						request: '',
						conditions: ['node', 'import'],
						output: ['./node.import.js'],
					},
					{
						request: '',
						conditions: ['import', 'browser'],
						output: ['./browser.import.js'],
					},
					{
						request: '',
						conditions: ['require', 'browser'],
						output: ['./browser.require.js'],
					},
					{
						request: '',
						conditions: ['node', 'require', 'random-condition-doesnt-matter'],
						output: ['./node.require.js'],
					},

					// Errors
					{
						request: '',
						conditions: [],
						error: 'No "exports" main defined',
					},
					{
						request: '',
						conditions: ['node'], // incomplete conditions
						error: 'No "exports" main defined',
					},
				],
			}),
		);
	});
});
```

## File: `tests/exports/error-cases.ts`
```typescript
import { testSuite, expect } from 'manten';
import { nodeResolveExports } from '../utils/node-resolve.js';
import { resolveExports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('error cases', ({ describe }) => {
		describe('invalid exports', ({ test }) => {
			test(
				'mixing conditional with paths',
				async () => {
					const exports = {
						'.': './index.js',
						condition: './index.js',
					};
					const expectedError = '"exports" cannot contain some keys starting with';

					expect(() => resolveExports(exports, '', [])).toThrow(expectedError);
					await expect(nodeResolveExports(exports, '', [])).rejects.toThrow(expectedError);
				},
			);

			test(
				'numeric value',
				async () => {
					const exports = { '.': 1 };

					// @ts-expect-error number type
					expect(() => resolveExports(exports, '', [])).toThrow('Invalid "exports" target "1"');

					// @ts-expect-error invalid exports
					await expect(nodeResolveExports(exports, '', [])).rejects.toThrow('Invalid "exports" main target "1"');
				},
			);

			test(
				'boolean value',
				async () => {
					const exports = { '.': true };

					// @ts-expect-error number type
					expect(() => resolveExports(exports, '', [])).toThrow('[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "true"');

					// @ts-expect-error invalid exports
					await expect(nodeResolveExports(exports, '', [])).rejects.toThrow('[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" main target "true"');
				},
			);

			test(
				'numeric keys',
				async () => {
					const exports = { 0: './index.js' };
					const error = 'annot contain numeric property keys';

					expect(() => resolveExports(exports, '', [])).toThrow(error);
					await expect(nodeResolveExports(exports, '', [])).rejects.toThrow(error);
				},
			);

			test(
				'path doesnt start with ./',
				async () => {
					const target = 'entry';
					const exports = { './entry': target };
					const error = `[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "${target}"`;

					expect(() => resolveExports(exports, 'entry', [])).toThrow(error);
					await expect(nodeResolveExports(exports, 'entry', [])).rejects.toThrow(error);
				},
			);

			test(
				'./ in middle of path',
				async () => {
					const target = './lib/./entry.js';
					const exports = { './entry': target };
					const error = `[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "${target}"`;

					expect(() => resolveExports(exports, 'entry', [])).toThrow(error);
					await expect(nodeResolveExports(exports, 'entry', [])).rejects.toThrow(error);
				},
			);

			test(
				'starts with ..',
				async () => {
					const target = '../entry';
					const exports = { './entry': target };
					const error = `[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "${target}"`;

					expect(() => resolveExports(exports, 'entry', [])).toThrow(error);
					await expect(nodeResolveExports(exports, 'entry', [])).rejects.toThrow(error);
				},
			);

			test(
				'../ in middle of path',
				async () => {
					const target = './lib/../entry.js';
					const exports = { './entry': target };
					const error = `[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "${target}"`;

					expect(() => resolveExports(exports, 'entry', [])).toThrow(error);
					await expect(nodeResolveExports(exports, 'entry', [])).rejects.toThrow(error);
				},
			);

			test(
				'node_modules in path',
				async () => {
					const target = './lib/node_modules/entry.js';
					const exports = { './entry': target };
					const error = `[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "${target}"`;

					expect(() => resolveExports(exports, 'entry', [])).toThrow(error);
					await expect(nodeResolveExports(exports, 'entry', [])).rejects.toThrow(error);
				},
			);

			test(
				'case insensitive node_modules in path',
				async () => {
					const target = './lib/NODE_MODULES/entry.js';
					const exports = { './entry': target };
					const error = `[ERR_INVALID_PACKAGE_TARGET]: Invalid "exports" target "${target}"`;

					expect(() => resolveExports(exports, 'entry', [])).toThrow(error);
					await expect(nodeResolveExports(exports, 'entry', [])).rejects.toThrow(error);
				},
			);
		});

		describe('throws on null exports', ({ test }) => {
			test(
				'falls back to package.json#main',
				async () => {
					const exports = null;
					const request = '';

					expect(
						// @ts-expect-error invalid exports
						() => resolveExports(exports, request, []),
					).toThrow('"exports" is required');

					// Node.js resolves to main
					expect(
						await nodeResolveExports(
							'manually created below',
							request,
							[],
							{
								'entry.js': '',
								'package.json': JSON.stringify({
									main: './entry.js',
									exports: null,
								}),
							},
						),
					).toBe('./entry.js');
				},
			);

			test(
				'resolves subpath',
				async () => {
					const exports = null;
					const request = 'non-existent-export.js';

					expect(
						// @ts-expect-error invalid exports
						() => resolveExports(exports, request, []),
					).toThrow('"exports" is required');

					expect(
						await nodeResolveExports(
							// @ts-expect-error invalid exports
							exports,
							request,
							[],
							{ 'non-existent-export.js': '' },
						),
					).toBe('./non-existent-export.js');
				},
			);
		});

		describe('missing export', ({ test }) => {
			test(
				'non-existent export',
				async () => {
					const exports = './entry.js';
					const request = 'non-existent-export';
					const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./non-existent-export\' is not defined by "exports"';

					expect(
						() => resolveExports(exports, request, []),
					).toThrow(error);

					await expect(
						nodeResolveExports(exports, request, []),
					).rejects.toThrow(error);
				},
			);

			test(
				'null path',
				async () => {
					const exports = { './entry.js': null };
					const request = 'entry.js';
					const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./entry.js\' is not defined by "exports"';

					expect(
						() => resolveExports(exports, request, []),
					).toThrow(error);

					await expect(
						nodeResolveExports(
							exports,
							request,
							[],
							{ 'entry.js': '' },
						),
					).rejects.toThrow(error);
				},
			);
		});
	});
});
```

## File: `tests/exports/fallback-array.ts`
```typescript
import { testSuite, expect } from 'manten';
import { resolveExportsWithNode } from '../utils/resolve-with-node.js';
import { resolveExports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('fallback array', ({ test }) => {
		test(
			'skips false condition',
			() => resolveExportsWithNode({
				exports: [
					{
						'condition-a': './a.js',
					},
					'./b.js',
					'std:core-module',
				],

				assertions: [
					{
						request: '',
						conditions: [],
						output: ['./b.js', 'std:core-module'],
					},
				],
			}),
		);

		test(
			'returns array of matched fallback paths',
			() => {
				const exports = [
					'./a.js',
					{
						'condition-b': './b.js',
					},
					'./c.js',
					{
						'condition-d': './d.js',
						default: ['./e.js', './f.js'],
					},
				] as const;
				const resolved = resolveExports(exports, '', []);

				expect(resolved).toStrictEqual([
					'./a.js',
					'./c.js',
					'./e.js',
					'./f.js',
				]);
			},
		);

		test(
			'stars replaced',
			() => {
				const exports = {
					'./*': [
						{ condition: './dir-a/*.js' },
						'./dir-b/*.js',
						{ default: './dir-c/*.js' },
						{
							default: {
								default: [
									'./dir-d/*',
									'./dir-e/*/*.js',
								],
							},
						},
					],
				} as const;
				const resolved = resolveExports(exports, 'file', []);

				expect(resolved).toStrictEqual([
					'./dir-b/file.js',
					'./dir-c/file.js',
					'./dir-d/file',
					'./dir-e/file/file.js',
				]);
			},
		);
	});
});
```

## File: `tests/exports/index.ts`
```typescript
import { testSuite } from 'manten';

export default testSuite(({ describe }) => {
	describe('exports', ({ runTestSuite }) => {
		runTestSuite(import('./error-cases.js'));
		runTestSuite(import('./basic.js'));
		runTestSuite(import('./star.js'));
		runTestSuite(import('./conditions.js'));
		runTestSuite(import('./fallback-array.js'));
		runTestSuite(import('./compare-resolve.exports.js'));
	});
});
```

## File: `tests/exports/star.ts`
```typescript
import { testSuite, expect } from 'manten';
import { nodeResolveExports } from '../utils/node-resolve.js';
import { resolveExportsWithNode } from '../utils/resolve-with-node.js';
import { resolveExports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('star', ({ test }) => {
		test(
			'static match',
			() => resolveExportsWithNode({
				exports: {
					'./*': './file.js',
				},

				assertions: [{
					request: 'any-entry',
					conditions: [],
					output: ['./file.js'],
				}],
			}),
		);

		test(
			'dynamic match - prefix',
			() => resolveExportsWithNode({
				exports: {
					'./prefix/*': './lib/*.js',
				},

				files: {
					'lib/a.js': '',
				},

				assertions: [{
					request: 'prefix/a',
					conditions: [],
					output: ['./lib/a.js'],
				}],
			}),
		);

		test(
			'dynamic match - prefix & suffix',
			() => resolveExportsWithNode({
				exports: {
					'./prefix/*.suffix': './lib/*.mjs',
				},

				files: {
					lib: {
						'a.mjs': '',
						'b.mjs': '',
						'directory/a/b/c.mjs': '',
						'.mjs': '',
					},
				},

				assertions: [
					{
						request: 'prefix/a.suffix',
						conditions: [],
						output: ['./lib/a.mjs'],
					},
					{
						request: 'prefix/b.suffix',
						conditions: [],
						output: ['./lib/b.mjs'],
					},
					{
						request: 'prefix/directory/a/b/c.suffix',
						conditions: [],
						output: ['./lib/directory/a/b/c.mjs'],
					},
				],
			}),
		);

		test(
			'error: shouldnt resolve value-less star',
			async () => {
				const exports = {
					'./prefix/*.suffix': './lib/*.mjs',
				};
				const request = './prefix/.suffix';
				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'././prefix/.suffix\' is not defined by "exports"';

				expect(
					() => resolveExports(exports, request, []),
				).toThrow(error);

				await expect(
					nodeResolveExports(exports, request, []),
				).rejects.toThrow(error);
			},
		);

		test(
			'multiple stars',
			() => resolveExportsWithNode({
				exports: {
					'./*.ext': './*/src/*.mjs',
				},

				files: {
					'match/src/match.mjs': '',
				},

				assertions: [{
					request: 'match.ext',
					conditions: [],
					output: ['./match/src/match.mjs'],
				}],
			}),
		);

		test(
			'star treated literally if only in path',
			() => resolveExportsWithNode({
				exports: {
					'./file': './lib/*.js',
				},

				files: {
					'lib/*.js': '',
				},

				assertions: [{
					request: 'file',
					conditions: [],
					output: ['./lib/*.js'],
				}],
			}),
		);

		test(
			'export ignored if multiple stars',
			async () => {
				const exports = {
					'./*/*': './file.js',
				};

				const requestInvalid = './dir/file.js';
				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'././dir/file.js\' is not defined by "exports"';

				expect(
					() => resolveExports(exports, requestInvalid, []),
				).toThrow(error);

				await expect(
					nodeResolveExports(
						exports,
						requestInvalid,
						[],
						{ 'file.js': '' },
					),
				).rejects.toThrow(error);
			},
		);

		test(
			'export ignored if multiple stars',
			async () => {
				const exports = {
					'./**': './file.js',
				};

				const requestInvalid = 'file.js';
				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./file.js\' is not defined by "exports"';

				expect(
					() => resolveExports(exports, requestInvalid, []),
				).toThrow(error);

				await expect(
					nodeResolveExports(
						exports,
						requestInvalid,
						[],
						{ 'file.js': '' },
					),
				).rejects.toThrow(error);
			},
		);

		test(
			'path order - null blocks entry',
			async () => {
				const exports = {
					'./*': './*',
					'./internal/*': null,
				};

				const requestValid = 'file.js';
				expect(resolveExports(exports, requestValid, [])).toStrictEqual(['./file.js']);
				await expect(
					await nodeResolveExports(
						exports,
						requestValid,
						[],
						{ 'file.js': '' },
					),
				).toBe('./file.js');

				const requestInvalid = 'internal/file.js';
				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./internal/file.js\' is not defined by "exports"';

				expect(
					() => resolveExports(exports, requestInvalid, []),
				).toThrow(error);

				await expect(
					nodeResolveExports(
						exports,
						requestInvalid,
						[],
						{ 'internal/file.js': '' },
					),
				).rejects.toThrow(error);
			},
		);

		test(
			'path order - null blocks entry - same star position (compares entire length)',
			async () => {
				const exports = {
					'./*': './*',
					'./*.js': null,
				};

				const requestValid = 'file.mjs';
				expect(resolveExports(exports, requestValid, [])).toStrictEqual(['./file.mjs']);
				await expect(
					await nodeResolveExports(
						exports,
						requestValid,
						[],
						{ 'file.mjs': '' },
					),
				).toBe('./file.mjs');

				const requestInvalid = 'file.js';
				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./file.js\' is not defined by "exports"';

				expect(
					() => resolveExports(exports, requestInvalid, []),
				).toThrow(error);

				await expect(
					nodeResolveExports(
						exports,
						requestInvalid,
						[],
						{ 'file.js': '' },
					),
				).rejects.toThrow(error);
			},
		);

		test(
			'path order - same prefix & length',
			async () => {
				const exports = {
					'./*.cjs': './*.cjs',
					'./*.mjs': null,
				};

				const requestValid = 'file.cjs';
				expect(resolveExports(exports, requestValid, [])).toStrictEqual(['./file.cjs']);
				await expect(
					await nodeResolveExports(
						exports,
						requestValid,
						[],
						{ 'file.cjs': '' },
					),
				).toBe('./file.cjs');

				const requestInvalid = 'file.mjs';
				const error = '[ERR_PACKAGE_PATH_NOT_EXPORTED]: Package subpath \'./file.mjs\' is not defined by "exports"';

				expect(
					() => resolveExports(exports, requestInvalid, []),
				).toThrow(error);

				await expect(
					nodeResolveExports(
						exports,
						requestInvalid,
						[],
						{ 'file.mjs': '' },
					),
				).rejects.toThrow(error);
			},
		);
	});
});
```

## File: `tests/imports/error-cases.ts`
```typescript
import { testSuite, expect } from 'manten';
import { nodeResolveImports } from '../utils/node-resolve.js';
import { resolveImports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('error cases', ({ test }) => {
		test(
			'missing target',
			async () => {
				const request = '#entry';
				const dependencyName = 1;
				const imports = {};
				const files = {
					[`node_modules/${dependencyName}`]: {
						'package.json': '{}',
						'index.js': '',
					},
				};

				expect(
					() => resolveImports(imports, request, []),
				).toThrow(
					'Package import specifier "#entry" is not defined in package',
				);
				await expect(
					nodeResolveImports(imports, request, [], files),
				).rejects.toThrow(
					'[ERR_PACKAGE_IMPORT_NOT_DEFINED]: Package import specifier "#entry" is not defined',
				);
			},
		);

		test(
			'numeric value',
			async () => {
				const request = '#entry';
				const dependencyName = 1;
				const imports = { [request]: dependencyName };
				const files = {
					[`node_modules/${dependencyName}`]: {
						'package.json': '{}',
						'index.js': '',
					},
				};

				// @ts-expect-error number type
				expect(() => resolveImports(imports, request, [])).toThrow('Invalid "imports" target "1"');

				// @ts-expect-error number type
				await expect(nodeResolveImports(imports, request, [], files)).rejects.toThrow('Invalid "imports" target "1"');
			},
		);

		test(
			'boolean value',
			async () => {
				const request = '#entry';
				const dependencyName = true;
				const imports = { [request]: dependencyName };
				const files = {
					[`node_modules/${dependencyName}`]: {
						'package.json': '{}',
						'index.js': '',
					},
				};

				// @ts-expect-error number type
				expect(() => resolveImports(imports, request, [])).toThrow('Invalid "imports" target "true"');

				// @ts-expect-error number type
				await expect(nodeResolveImports(imports, request, [], files)).rejects.toThrow('Invalid "imports" target "true"');
			},
		);

		test(
			'starts with ..',
			async () => {
				const request = '#entry';
				const target = '../file.js';
				const imports = { [request]: target };

				expect(() => resolveImports(imports, request, [])).toThrow(`Invalid "imports" target "${target}"`);
				await expect(nodeResolveImports(imports, request, [])).rejects.toThrow(`Invalid "imports" target "${target}"`);
			},
		);

		test(
			'.. in path',
			async () => {
				const request = '#entry';
				const target = './directory/../file.js';
				const imports = { [request]: target };

				expect(() => resolveImports(imports, request, [])).toThrow(`Invalid "imports" target "${target}"`);
				await expect(nodeResolveImports(imports, request, [])).rejects.toThrow(`Invalid "imports" target "${target}"`);
			},
		);

		test(
			'node_modules in path',
			async () => {
				const request = '#entry';
				const dependencyName = 'dependency';
				const target = `./node_modules/${dependencyName}/file.js`;
				const imports = { [request]: target };
				const files = {
					[`node_modules/${dependencyName}`]: {
						'package.json': '{}',
						'file.js': '',
					},
				};

				expect(() => resolveImports(imports, request, [])).toThrow(`Invalid "imports" target "${target}"`);
				await expect(nodeResolveImports(imports, request, [], files)).rejects.toThrow(`Invalid "imports" target "${target}"`);
			},
		);
	});
});
```

## File: `tests/imports/index.ts`
```typescript
import { testSuite, expect } from 'manten';
import { nodeResolveImports } from '../utils/node-resolve.js';
import { resolveImports } from '#resolve-pkg-maps';

export default testSuite(({ describe }) => {
	describe('imports', ({ test, runTestSuite }) => {
		runTestSuite(import('./error-cases.js'));

		test(
			'resolves',
			async () => {
				const request = '#a';
				const imports = { [request]: './file.js' };
				const nodeResolved = await nodeResolveImports(imports, request, []);
				const resolved = resolveImports(imports, request, []);

				await expect(nodeResolved).toBe('./file.js');
				await expect(resolved[0]).toBe(nodeResolved);
			},
		);

		test(
			'resolves node_modules dependency (not allowed in exports)',
			async () => {
				const request = '#entry';
				const imports = { [request]: 'dependency' };
				const nodeResolved = await nodeResolveImports(imports, request, [], {
					'node_modules/dependency': {
						'package.json': '{}',
						'index.js': '',
					},
				});
				const resolved = resolveImports(imports, request, []);

				await expect(nodeResolved).toBe('./node_modules/dependency/index.js');
				await expect(resolved[0]).toBe('dependency');
			},
		);

		test(
			'conditions',
			async () => {
				const request = '#entry';
				const imports = {
					[request]: {
						'condition-a': './condition-a.js',
						'condition-b': './condition-b.js',
						default: './default.js',
					},
				};

				const conditions = [
					[[], './default.js'],
					[['condition-a'], './condition-a.js'],
					[['condition-a', 'condition-b'], './condition-a.js'],
				] as const;

				for (const [condition, expected] of conditions) {
					const nodeResolved = await nodeResolveImports(imports, request, condition);
					const resolved = resolveImports(imports, request, condition);

					await expect(nodeResolved).toBe(expected);
					await expect(resolved[0]).toBe(nodeResolved);
				}
			},
		);

		test(
			'star',
			async () => {
				const request = '#entry/file';
				const imports = {
					'#entry/*': {
						dev: './src/*.js',
						test: './tests/*/*.spec.js',
						default: './dist/*.js',
					},
				};

				const conditions = [
					[[], './dist/file.js'],
					[['dev'], './src/file.js'],
					[['test'], './tests/file/file.spec.js'],
				] as const;

				const files = {
					'src/file.js': '',
					'tests/file/file.spec.js': '',
					'dist/file.js': '',
				} as const;

				for (const [condition, expected] of conditions) {
					const nodeResolved = await nodeResolveImports(imports, request, condition, files);
					const resolved = resolveImports(imports, request, condition);

					await expect(nodeResolved).toBe(expected);
					await expect(resolved[0]).toBe(nodeResolved);
				}
			},
		);

		describe('star order', ({ test }) => {
			const imports = {
				'#entry/*': './*.js',
				'#entry/*.js': null,
			};
			const files = { 'file.js': '' };

			test('resolves', async () => {
				const request = '#entry/file';
				const nodeResolved = await nodeResolveImports(imports, request, [], files);
				const [resolved] = resolveImports(imports, request, []);

				await expect(nodeResolved).toBe('./file.js');
				await expect(resolved).toBe(nodeResolved);
			});

			test('blocks request', async () => {
				const request = '#entry/file.js';
				const error = '[ERR_PACKAGE_IMPORT_NOT_DEFINED]: Package import specifier "#entry/file.js" is not defined in package';

				expect(
					() => resolveImports(imports, request, []),
				).toThrow(error);

				await expect(
					nodeResolveImports(imports, request, [], files),
				).rejects.toThrow(error);
			});
		});
	});
});
```

## File: `tests/utils/node-resolve.ts`
```typescript
import path from 'path';
import { fileURLToPath } from 'node:url';
import { execaNode } from 'execa';
import { createFixture, type FileTree } from 'fs-fixture';
import type { PathConditions, PathConditionsMap } from '#resolve-pkg-maps';

const loaderPath = path.resolve('./tests/utils/resolve-logger.mjs');

const packagePath = 'node_modules/package/';

const loaderWarning = 'to show where the warning was created)';

export async function nodeResolve(
	files: FileTree,
	request: string,
	conditions: readonly string[],
) {
	const fixture = await createFixture({
		...files,
		'resolve.mjs': `import '${request}'`,
	});

	const nodeProcess = await execaNode(
		'./resolve.mjs',
		[],
		{
			nodeOptions: [
				'--loader',
				loaderPath,
				...conditions.map(condition => `--conditions=${condition}`),
			],
			cwd: fixture.path,
			reject: false,
		},
	);

	await fixture.rm();

	const stderr = nodeProcess.stderr.slice(
		nodeProcess.stderr.indexOf(loaderWarning) + loaderWarning.length,
	);

	if (stderr) {
		throw new Error(stderr);
	}

	if (nodeProcess.stdout) {
		return fileURLToPath(nodeProcess.stdout).replace(
			path.join(fixture.path),
			'.',
		);
	}
}

function normalizeExports(
	exports: PathConditions,
): PathConditionsMap {
	if (
		!exports
		|| typeof exports === 'string'
		|| Array.isArray(exports)
		|| (
			exports
			&& typeof exports === 'object'

			// If condition object
			&& Object.keys(exports).every(key => key === '' || key[0] !== '.')
		)
	) {
		return { '.': exports };
	}

	return exports;
}

const getMapPaths = (
	exports: PathConditions | null,
): string[] => {
	if (!exports) {
		return [];
	}

	if (typeof exports === 'string') {
		return exports.includes('*') ? [] : [exports];
	}

	return (
		Array.isArray(exports)
			? exports
			: Object.values(exports)
	).flatMap(getMapPaths);
};

export async function nodeResolveExports(
	exports: PathConditions,
	request: string,
	conditions: readonly string[],
	files?: FileTree,
) {
	if (!files) {
		// Generate files from export map
		files = Object.fromEntries(
			getMapPaths(
				normalizeExports(exports),
			)
				.filter(filePath => filePath !== './non-existent.js')
				.map(filePath => [filePath, '']),
		);
	}

	const resolved = await nodeResolve(
		{
			[packagePath]: {
				'package.json': JSON.stringify({ exports }),
				...files,
			},
		},
		`package${request ? `/${request}` : ''}`,
		conditions,
	);

	if (resolved) {
		return resolved.replace(packagePath, '');
	}
}

export async function nodeResolveImports(
	imports: PathConditionsMap,
	request: string,
	conditions: readonly string[],
	files?: FileTree,
) {
	if (!files) {
		// Generate files from import map
		files = Object.fromEntries(
			getMapPaths(imports).map(filePath => [filePath, '']),
		);
	}

	return await nodeResolve(
		{
			'package.json': JSON.stringify({ imports }),
			...files,
		},
		request,
		conditions,
	);
}
```

## File: `tests/utils/resolve-logger.mjs`
```
let firstCall = true;

export async function resolve(
	specifier,
	context,
	nextResolve,
) {
	// Remove default conditions
	context.conditions = context.conditions.slice(3);

	const resolved = await nextResolve(specifier, context, nextResolve);

	if (firstCall) {
		firstCall = false;
	} else {
		console.log(resolved.url);
	}

	return resolved;
}
```

## File: `tests/utils/resolve-with-node.ts`
```typescript
import { expect } from 'manten';
import { type FileTree } from 'fs-fixture';
import { nodeResolveExports } from './node-resolve.js';
import { resolveExports, type PathConditions } from '#resolve-pkg-maps';

type AssertionBase = {
	request: string;
	conditions: string[];
	debug?: boolean;
	disableNodeCheck?: boolean;
};

export async function resolveExportsWithNode({
	exports,
	files,
	assertions,
}: {
	exports: PathConditions;

	files?: FileTree;

	assertions: ((AssertionBase & { output: string[] }) | (AssertionBase & { error: string }))[];
}) {
	for (const assertion of assertions) {
		const { request, conditions, debug } = assertion;
		const error = 'error' in assertion ? assertion.error : undefined;
		const output = 'output' in assertion ? assertion.output : undefined;

		let resolved: string[];

		try {
			resolved = resolveExports(exports, request, conditions);
		} catch (resolvedError) {
			if (error) {
				expect((resolvedError as any).message).toMatch(error);
				continue;
			}

			throw resolvedError;
		}

		if (error) {
			throw new Error(`Expected to throw error matching ${error}`);
		}

		expect(resolved).toStrictEqual(output);

		let resolvedNode: string | undefined;
		try {
			resolvedNode = await nodeResolveExports(
				exports,
				request,
				conditions,
				files,
			);
		} catch (nodeError) {
			if (error) {
				expect((nodeError as any).message).toMatch(error);
				continue;
			}

			throw nodeError;
		}

		if (debug) {
			console.log({
				request,
				conditions,
				resolved,
				resolvedNode,
			});
		}

		if (error) {
			throw new Error(
				`Expected Node.js to throw error matching ${error}`,
			);
		}

		expect(resolvedNode).toBe(resolved[0]);
	}
}
```

