---
id: github.com-sindresorhus-configstore-e285fa68-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.333456
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_configstore_e285fa68
> **Extracted on:** 2026-04-01 07:37:25
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519093/github.com_sindresorhus_configstore_e285fa68

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
	Store the config at `$CONFIG/package-name/config.json` instead of the default `$CONFIG/configstore/package-name.json`.

	This is not recommended as you might end up conflicting with other tools, rendering the "without having to think" idea moot.

	@default false
	*/
	readonly globalConfigPath?: boolean;

	/**
	Set the path of the config file. Overrides the `id` and `globalConfigPath` options.

	**Please don't use this option unless absolutely necessary and you know what you're doing.**
	*/
	readonly configPath?: string;

	/**
	Clear the config file if it contains invalid JSON. If set to `false`, a `SyntaxError` will be thrown instead of clearing the file. This allows you to recover corrupted config files manually.

	@default true
	*/
	readonly clearInvalidConfig?: boolean;
};

/**
Easily load and persist config without having to think about where and how.

The config is stored in a JSON file located in `$XDG_CONFIG_HOME` or `~/.config`.
Example: `~/.config/configstore/some-id.json`
*/
export default class Configstore {
	/**
	Get the path to the config file. Can be used to show the user where the config file is located or even better open it for them.
	*/
	readonly path: string;

	/**
	Get the item count.
	*/
	readonly size: number;

	/**
	Get all the config as an object or replace the current config with an object.
	*/
	all: Record<string, unknown>;

	/**
	@param id - Identifier for your config. Usually your package name.
	@param defaults - Default config.
	*/
	constructor(id: string, defaults?: Record<string, unknown>, options?: Options);

	/**
	Set an item.

	@param key - You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.
	@param value - Must be JSON serializable.
	*/
	set(key: string, value: unknown): void;

	/**
	Set multiple items at once.

	@param object - A hashmap of items to set at once.
	*/
	set(object: Record<string, unknown>): void;

	/**
	Get an item.

	@param key - You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.
	*/
	get<T = unknown>(key: string): T | undefined;

	/**
	Check if an item exists.

	@param key - You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.
	*/
	has(key: string): boolean;

	/**
	Delete an item.

	@param key - You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.
	*/
	delete(key: string): void;

	/**
	Delete all items.
	*/
	clear(): void;
}
```

## File: `index.js`
```javascript
import path from 'node:path';
import os from 'node:os';
import fs from 'graceful-fs';
import {xdgConfig} from 'xdg-basedir';
import {writeFileSync} from 'atomically';
import {
	getProperty,
	setProperty,
	hasProperty,
	deleteProperty,
} from 'dot-prop';
import isSafeFilename from 'is-safe-filename';

function getConfigDirectory(id, globalConfigPath) {
	if (!isSafeFilename(id)) {
		throw new Error(`\`id\` must be a safe filename: ${JSON.stringify(id)}`);
	}

	const pathPrefix = globalConfigPath
		? path.join(id, 'config.json')
		: path.join('configstore', `${id}.json`);

	const configDirectory = xdgConfig ?? fs.mkdtempSync(fs.realpathSync(os.tmpdir()) + path.sep);

	return path.join(configDirectory, pathPrefix);
}

const permissionError = 'You don\'t have access to this file.';
const mkdirOptions = {mode: 0o0700, recursive: true};
const writeFileOptions = {mode: 0o0600};

function handlePermissionError(error) {
	if (error.code === 'EACCES') {
		error.message = `${error.message}\n${permissionError}\n`;
	}

	throw error;
}

export default class Configstore {
	constructor(id, defaults, options = {}) {
		this._path = options.configPath ?? getConfigDirectory(id, options.globalConfigPath);
		this._clearInvalidConfig = options.clearInvalidConfig ?? true;

		if (defaults) {
			this.all = {
				...defaults,
				...this.all,
			};
		}
	}

	get all() {
		try {
			return JSON.parse(fs.readFileSync(this._path, 'utf8'));
		} catch (error) {
			// File doesn't exist yet
			if (error.code === 'ENOENT') {
				return {};
			}

			// Handle invalid JSON
			if (error.name === 'SyntaxError') {
				if (this._clearInvalidConfig) {
					writeFileSync(this._path, '', writeFileOptions);
					return {};
				}

				throw error;
			}

			handlePermissionError(error); // This always throws
			/* c8 ignore next */
			return {}; // Unreachable, but satisfies linter
		}
	}

	set all(value) {
		try {
			// Make sure the folder exists as it could have been deleted in the meantime
			fs.mkdirSync(path.dirname(this._path), mkdirOptions);

			writeFileSync(this._path, JSON.stringify(value, undefined, '\t'), writeFileOptions);
		} catch (error) {
			handlePermissionError(error); // This always throws
		}
	}

	get size() {
		return Object.keys(this.all).length;
	}

	get(key) {
		return getProperty(this.all, key);
	}

	set(key, value) {
		const config = this.all;

		if (typeof key === 'object' && arguments.length === 1) {
			for (const k of Object.keys(key)) {
				setProperty(config, k, key[k]);
			}
		} else {
			setProperty(config, key, value);
		}

		this.all = config;
	}

	has(key) {
		return hasProperty(this.all, key);
	}

	delete(key) {
		const config = this.all;
		deleteProperty(config, key);
		this.all = config;
	}

	clear() {
		this.all = {};
	}

	get path() {
		return this._path;
	}
}
```

## File: `license`
```
BSD 2-Clause License

Copyright (c) Google
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## File: `package.json`
```json
{
	"name": "configstore",
	"version": "8.0.0",
	"description": "Easily load and save config without having to think about where and how",
	"license": "BSD-2-Clause",
	"repository": "sindresorhus/configstore",
	"funding": "https://github.com/sponsors/sindresorhus",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": "./index.js",
	"types": "./index.d.ts",
	"sideEffects": false,
	"engines": {
		"node": ">=20"
	},
	"scripts": {
		"test": "xo && ava"
	},
	"files": [
		"index.js",
		"index.d.ts"
	],
	"keywords": [
		"config",
		"store",
		"storage",
		"configuration",
		"settings",
		"preferences",
		"json",
		"data",
		"persist",
		"persistent",
		"save"
	],
	"dependencies": {
		"atomically": "^2.1.0",
		"dot-prop": "^10.1.0",
		"graceful-fs": "^4.2.11",
		"is-safe-filename": "^0.1.0",
		"xdg-basedir": "^5.1.0"
	},
	"devDependencies": {
		"ava": "^6.4.1",
		"xo": "^1.2.3"
	},
	"ava": {
		"serial": true
	}
}
```

## File: `readme.md`
```markdown
# configstore

> Easily load and persist config without having to think about where and how

The config is stored in a JSON file located in `$XDG_CONFIG_HOME` or `~/.config`.\
Example: `~/.config/configstore/some-id.json`

*If you need this for Electron, check out [`electron-store`](https://github.com/sindresorhus/electron-store) instead.*\
*And check out [`conf`](https://github.com/sindresorhus/conf) for a more modern version of `configstore`.*

## Install

```sh
npm install configstore
```

## Usage

```js
import fs from 'node:fs';
import Configstore from 'configstore';

const packageJson = JSON.parse(fs.readFileSync('./package.json', 'utf8'));

// Create a Configstore instance.
const config = new Configstore(packageJson.name, {foo: 'bar'});

console.log(config.get('foo'));
//=> 'bar'

config.set('awesome', true);
console.log(config.get('awesome'));
//=> true

// Use dot-notation to access nested properties.
config.set('bar.baz', true);
console.log(config.get('bar'));
//=> {baz: true}

// Handle missing keys with nullish coalescing.
console.log(config.get('nonexistent') ?? 'default value');
//=> 'default value'

config.delete('awesome');
console.log(config.get('awesome'));
//=> undefined
```

## API

### Configstore(id, defaults?, options?)

Returns a new instance.

#### id

Type: `string`

Identifier for your config. Usually your package name.

#### defaults

Type: `object`

Default config.

#### options

Type: `object`

##### globalConfigPath

Type: `boolean`\
Default: `false`

Store the config at `$CONFIG/package-name/config.json` instead of the default `$CONFIG/configstore/package-name.json`. This is not recommended as you might end up conflicting with other tools, rendering the "without having to think" idea moot.

##### configPath

Type: `string`\
Default: Automatic

**Please don't use this option unless absolutely necessary and you know what you're doing.**

Set the path of the config file. Overrides the `id` and `globalConfigPath` options.

##### clearInvalidConfig

Type: `boolean`\
Default: `true`

Clear the config file if it contains invalid JSON. If set to `false`, a `SyntaxError` will be thrown instead of clearing the file. This allows you to recover corrupted config files manually.

### Instance

You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.

### .set(key, value)

Set an item.

You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.

### .set(object)

Set multiple items at once.

### .get(key)

Get an item.

You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.

> [!TIP]
> Use the [nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) (`??`) to provide default values:
> ```js
> const value = config.get('key') ?? 'default value';
> ```

### .has(key)

Check if an item exists.

You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.

### .delete(key)

Delete an item.

You can use [dot-notation](https://github.com/sindresorhus/dot-prop) in a `key` to access nested properties.

### .clear()

Delete all items.

### .size

Get the item count.

### .path

Get the path to the config file. Can be used to show the user where the config file is located or even better open it for them.

### .all

Get all the config as an object or replace the current config with an object.

```js
console.log(config.all);
//=> {foo: 'bar', hello: 'world'}

config.all = {
	hello: 'world'
};
```
```

## File: `test.js`
```javascript
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import test from 'ava';
import Configstore from './index.js';

const configstorePath = new Configstore('configstore-test').path;

const cleanUpFile = () => {
	if (fs.existsSync(configstorePath)) {
		fs.unlinkSync(configstorePath);
	}
};

test.beforeEach(t => {
	cleanUpFile();
	t.context.config = new Configstore('configstore-test');
});

test('.set() and .get()', t => {
	const {config} = t.context;
	config.set('foo', 'bar');
	config.set('baz.boo', true);
	t.is(config.get('foo'), 'bar');
	t.is(config.get('baz.boo'), true);
});

test('.set() with object and .get()', t => {
	const {config} = t.context;
	config.set({
		foo1: 'bar1',
		foo2: 'bar2',
		baz: {
			boo: 'foo',
			foo: {
				bar: 'baz',
			},
		},
	});
	t.is(config.get('foo1'), 'bar1');
	t.is(config.get('foo2'), 'bar2');
	t.deepEqual(config.get('baz'), {
		boo: 'foo',
		foo: {
			bar: 'baz',
		},
	});
	t.is(config.get('baz.boo'), 'foo');
	t.deepEqual(config.get('baz.foo'), {bar: 'baz'});
	t.is(config.get('baz.foo.bar'), 'baz');
});

test('.set() handles undefined values correctly', t => {
	const {config} = t.context;
	// Undefined values are stripped during JSON serialization, so they don't persist
	config.set('undefinedValue', undefined);
	t.is(config.get('undefinedValue'), undefined);
	t.false(config.has('undefinedValue')); // JSON.stringify strips undefined values

	// Null values persist correctly
	config.set('nullValue', null);
	t.is(config.get('nullValue'), null);
	t.true(config.has('nullValue'));
});

test('.has()', t => {
	const {config} = t.context;
	config.set('foo', '🦄');
	config.set('baz.boo', '🦄');
	t.true(config.has('foo'));
	t.true(config.has('baz.boo'));
	t.false(config.has('missing'));
});

test('.delete()', t => {
	const {config} = t.context;
	config.set('foo', 'bar');
	config.set('baz.boo', true);
	config.set('baz.foo.bar', 'baz');
	config.delete('foo');
	t.is(config.get('foo'), undefined);
	config.delete('baz.boo');
	t.is(config.get('baz.boo'), undefined);
	config.delete('baz.foo');
	t.is(config.get('baz.foo'), undefined);
	config.set('foo.bar.baz', {awesome: 'icecream'});
	config.set('foo.bar.zoo', {awesome: 'redpanda'});
	config.delete('foo.bar.baz');
	t.is(config.get('foo.bar.zoo.awesome'), 'redpanda');
});

test('.clear()', t => {
	const {config} = t.context;
	config.set('foo', 'bar');
	config.set('foo1', 'bar1');
	config.set('baz.boo', true);
	config.clear();
	t.is(config.size, 0);
});

test('.all', t => {
	const {config} = t.context;
	config.set('foo', 'bar');
	config.set('baz.boo', true);
	t.is(config.all.foo, 'bar');
	t.deepEqual(config.all.baz, {boo: true});
});

test('.size', t => {
	const {config} = t.context;
	config.set('foo', 'bar');
	t.is(config.size, 1);
});

test('.path', t => {
	const {config} = t.context;
	config.set('foo', 'bar');
	t.true(fs.existsSync(config.path));
});

test('use default value', t => {
	const config = new Configstore('configstore-test', {foo: 'bar'});
	t.is(config.get('foo'), 'bar');
});

test('support `globalConfigPath` option', t => {
	const config = new Configstore('configstore-test', {}, {globalConfigPath: true});
	t.regex(config.path, /configstore-test(\/|\\)config.json$/);
});

test('support `configPath` option', t => {
	const customPath = path.join(os.tmpdir(), 'configstore-custom-path', 'foo.json');
	const config = new Configstore('ignored-namespace', {}, {
		globalConfigPath: true,
		configPath: customPath,
	});
	t.regex(config.path, /configstore-custom-path(\/|\\)foo.json$/);
});

test('ensure `.all` is always an object', t => {
	cleanUpFile();

	t.notThrows(() => {
		t.context.config.get('foo');
	});
});

test('the store is NOT created until write', t => {
	cleanUpFile();
	const config = new Configstore('configstore-test');
	t.false(fs.existsSync(config.path));
	config.set('foo', 'bar');
	t.true(fs.existsSync(config.path));
});

test('ensure necessary sub-directories are created', t => {
	const customPath = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'configstore-recursive-')), 'foo', 'bar', 'baz.json');
	const config = new Configstore('ignored-namespace', undefined, {
		globalConfigPath: true,
		configPath: customPath,
	});
	t.false(fs.existsSync(config.path));
	config.set('foo', 'bar');
	t.true(fs.existsSync(config.path));
});

test('clearInvalidConfig: true (default) clears corrupted JSON', t => {
	const {config} = t.context;

	// Set some data then corrupt the file
	config.set('test', 'data');
	fs.writeFileSync(config.path, '{"corrupted": json}', 'utf8');

	// Should clear the file and return empty object (default behavior)
	const configWithCorruptedFile = new Configstore('configstore-test');
	t.deepEqual(configWithCorruptedFile.all, {});

	// File should be cleared
	const clearedContent = fs.readFileSync(config.path, 'utf8');
	t.is(clearedContent, '');
});

test('clearInvalidConfig: false preserves corrupted JSON and throws', t => {
	// Create config, set data, then corrupt the file
	const config = new Configstore('configstore-test-preserve');
	config.set('test', 'data');

	const corruptedContent = '{"corrupted": json}';
	fs.writeFileSync(config.path, corruptedContent, 'utf8');

	// Should throw SyntaxError and preserve file
	const configWithCorruptedFile = new Configstore('configstore-test-preserve', undefined, {clearInvalidConfig: false});
	t.throws(() => configWithCorruptedFile.all, {name: 'SyntaxError'});

	// File should be preserved
	const preservedContent = fs.readFileSync(config.path, 'utf8');
	t.is(preservedContent, corruptedContent);
});

test('validate id', t => {
	const fixtures = [
		'',
		'.',
		'..',
		'../escape',
		'foo/../bar',
		'foo/bar',
		String.raw`foo\bar`,
		'foo\0bar',
	];

	for (const id of fixtures) {
		t.throws(() => new Configstore(id), {message: /`id` must be a safe filename/});
	}
});
```

