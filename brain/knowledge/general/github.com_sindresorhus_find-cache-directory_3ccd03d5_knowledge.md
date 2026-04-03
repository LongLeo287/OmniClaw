---
id: github.com-sindresorhus-find-cache-directory-3ccd0
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.702343
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_find-cache-directory_3ccd03d5
> **Extracted on:** 2026-04-01 17:09:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525544/github.com_sindresorhus_find-cache-directory_3ccd03d5

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
node_modules
yarn.lock
```

## File: `.npmrc`
```
package-lock=false
```

## File: `index.d.ts`
```typescript
export type Options = {
	/**
	Should be the same as your project name in `package.json`.
	*/
	readonly name: string;

	/**
	An array of files that will be searched for a common parent directory. This common parent directory will be used in lieu of the `cwd` option below.
	*/
	readonly files?: string[];

	/**
	The directory to start searching for a `package.json` from.

	@default process.cwd()
	*/
	readonly cwd?: string;

	/**
	Create the directory synchronously before returning.

	@default false
	*/
	readonly create?: boolean;
};

/**
Finds the cache directory using the given options.

The algorithm checks for the `CACHE_DIR` environmental variable and uses it if it is not set to `true`, `false`, `1` or `0`. If one is not found, it tries to find a `package.json` file, searching every parent directory of the `cwd` specified (or implied from other options). It returns a `string` containing the absolute path to the cache directory, or `undefined` if `package.json` was never found or if the `node_modules` directory is unwritable.

@example
```
import findCacheDirectory from 'find-cache-directory';

findCacheDirectory({name: 'unicorns'});
//=> '/user/path/node-modules/.cache/unicorns'
```
*/
export default function findCacheDirectory(options: Options): string | undefined;
```

## File: `index.js`
```javascript
import process from 'node:process';
import path from 'node:path';
import fs from 'node:fs';
import commonPathPrefix from 'common-path-prefix';
import {packageDirectorySync} from 'pkg-dir';

const {env, cwd} = process;

const isWritable = path => {
	try {
		fs.accessSync(path, fs.constants.W_OK);
		return true;
	} catch {
		return false;
	}
};

function useDirectory(directory, options) {
	if (options.create) {
		fs.mkdirSync(directory, {recursive: true});
	}

	return directory;
}

function getNodeModuleDirectory(directory) {
	const nodeModules = path.join(directory, 'node_modules');

	if (
		!isWritable(nodeModules)
			&& (fs.existsSync(nodeModules) || !isWritable(path.join(directory)))
	) {
		return;
	}

	return nodeModules;
}

export default function findCacheDirectory(options = {}) {
	if (env.CACHE_DIR && !['true', 'false', '1', '0'].includes(env.CACHE_DIR)) {
		return useDirectory(path.join(env.CACHE_DIR, options.name), options);
	}

	let {cwd: directory = cwd(), files} = options;

	if (files) {
		if (!Array.isArray(files)) {
			throw new TypeError(`Expected \`files\` option to be an array, got \`${typeof files}\`.`);
		}

		directory = commonPathPrefix(files.map(file => path.resolve(directory, file)));
	}

	directory = packageDirectorySync({cwd: directory});

	if (!directory) {
		return;
	}

	const nodeModules = getNodeModuleDirectory(directory);
	if (!nodeModules) {
		return;
	}

	return useDirectory(path.join(directory, 'node_modules', '.cache', options.name), options);
}
```

## File: `index.test-d.ts`
```typescript
import {expectType} from 'tsd';
import findCacheDirectory from './index.js';

const name = 'find-cache-directory';

expectType<string | undefined>(findCacheDirectory({name}));
expectType<string | undefined>(findCacheDirectory({name, files: ['/bar']}));
expectType<string | undefined>(findCacheDirectory({name, cwd: '/fooz'}));
expectType<string | undefined>(findCacheDirectory({name, create: true}));
```

## File: `license`
```
MIT License

Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (https://sindresorhus.com)
Copyright (c) James Talmage <james@talmage.io> (https://github.com/jamestalmage)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `package.json`
```json
{
	"name": "find-cache-directory",
	"version": "6.0.0",
	"description": "Finds the common standard cache directory",
	"license": "MIT",
	"repository": "sindresorhus/find-cache-directory",
	"funding": "https://github.com/sponsors/sindresorhus",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": {
		"types": "./index.d.ts",
		"default": "./index.js"
	},
	"sideEffects": false,
	"engines": {
		"node": ">=20"
	},
	"scripts": {
		"test": "xo && ava && tsd"
	},
	"files": [
		"index.js",
		"index.d.ts"
	],
	"keywords": [
		"cache",
		"directory",
		"caching",
		"find",
		"search"
	],
	"dependencies": {
		"common-path-prefix": "^3.0.0",
		"pkg-dir": "^8.0.0"
	},
	"devDependencies": {
		"ava": "^6.2.0",
		"del": "^8.0.0",
		"tempy": "^3.1.0",
		"tsd": "^0.31.2",
		"xo": "^0.60.0"
	},
	"ava": {
		"workerThreads": false
	},
	"xo": {
		"rules": {
			"n/no-unsupported-features/node-builtins": "off"
		}
	}
}
```

## File: `readme.md`
```markdown
# find-cache-directory

> Finds the common standard cache directory

The [`nyc`](https://github.com/istanbuljs/nyc) and [`AVA`](https://avajs.dev) projects decided to standardize on a common directory structure for storing cache information:

```sh
# nyc
./node_modules/.cache/nyc

# ava
./node_modules/.cache/ava

# your-module
./node_modules/.cache/your-module
```

This module makes it easy to correctly locate the cache directory according to this shared spec. If this pattern becomes ubiquitous, clearing the cache for multiple dependencies becomes easy and consistent:

```
rm -rf ./node_modules/.cache
```

## Install

```sh
npm install find-cache-directory
```

## Usage

```js
import findCacheDirectory from 'find-cache-directory';

findCacheDirectory({name: 'unicorns'});
//=> '/user/path/node-modules/.cache/unicorns'
```

## API

### findCacheDirectory(options?)

Finds the cache directory using the given options.

The algorithm checks for the `CACHE_DIR` environmental variable and uses it if it is not set to `true`, `false`, `1` or `0`. If one is not found, it tries to find a `package.json` file, searching every parent directory of the `cwd` specified (or implied from other options). It returns a `string` containing the absolute path to the cache directory, or `undefined` if `package.json` was never found or if the `node_modules` directory is unwritable.

#### options

Type: `object`

##### name

*Required*\
Type: `string`

Should be the same as your project name in `package.json`.

##### files

Type: `string[]`

An array of files that will be searched for a common parent directory. This common parent directory will be used in lieu of the `cwd` option below.

##### cwd

Type: `string`\
Default `process.cwd()`

The directory to start searching for a `package.json` from.

##### create

Type: `boolean`\
Default `false`

Create the directory synchronously before returning.

## Tips

- To test modules using this package, set the `CACHE_DIR` environment variable to temporarily override the directory that is resolved.

## Adopters

- [`ava`](https://avajs.dev)
- [`nyc`](https://github.com/istanbuljs/nyc)
- [`storybook`](https://github.com/storybookjs/storybook)
- [`babel-loader`](https://github.com/babel/babel-loader)
- [`eslint-loader`](https://github.com/MoOx/eslint-loader)
- [More…](https://www.npmjs.com/browse/depended/find-cache-dir)

## Related

- [env-paths](https://github.com/sindresorhus/env-paths) - Get paths for storing things like data, config, cache, etc
```

## File: `test.js`
```javascript
import process from 'node:process';
import fs from 'node:fs';
import path from 'node:path';
import test from 'ava';
import {deleteSync} from 'del';
import {temporaryDirectory} from 'tempy';
import findCacheDirectory from './index.js';

const {dirname} = import.meta;

test('finds from a list of files', t => {
	process.chdir(path.join(dirname, '..'));
	const files = ['foo/bar', 'baz/quz'].map(file => path.join(dirname, file));
	t.is(findCacheDirectory({files, name: 'blah'}), path.join(dirname, 'node_modules', '.cache', 'blah'));
});

test('finds from process.cwd', t => {
	process.chdir(path.join(dirname));
	t.is(findCacheDirectory({name: 'foo'}), path.join(dirname, 'node_modules', '.cache', 'foo'));
});

test('finds from options.cwd', t => {
	process.chdir(path.join(dirname, '..'));
	t.is(findCacheDirectory({cwd: dirname, name: 'bar'}), path.join(dirname, 'node_modules', '.cache', 'bar'));
});

test('creates directory', t => {
	const directory = path.join(dirname, 'node_modules', '.cache', 'created');
	deleteSync(directory);
	findCacheDirectory({create: true, name: 'created', cwd: dirname});
	t.true(fs.existsSync(directory));
});

test('returns undefined if it can\'t find package.json', t => {
	process.chdir(path.join(dirname, '..'));
	t.is(findCacheDirectory({name: 'foo'}), undefined);
});

test('supports CACHE_DIR environment variable', t => {
	const newCacheDirectory = temporaryDirectory();
	const finalDirectory = path.join(newCacheDirectory, 'some-package');
	process.env.CACHE_DIR = newCacheDirectory;

	t.is(findCacheDirectory({name: 'some-package'}), finalDirectory);

	findCacheDirectory({name: 'some-package', create: true});
	t.true(fs.existsSync(finalDirectory));

	delete process.env.CACHE_DIR;
});

test('ignores `false` for CACHE_DIR environment variable', t => {
	process.env.CACHE_DIR = 'false';

	t.not(findCacheDirectory(), path.resolve(dirname, 'false', 'find-cache-directory'));
});
```

