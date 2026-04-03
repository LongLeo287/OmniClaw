---
id: sindresorhus-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.830847
---

# KNOWLEDGE EXTRACT: sindresorhus
> **Extracted on:** 2026-03-30 17:53:21
> **Source:** sindresorhus

---

## File: `awesome.md`
```markdown
# 📦 sindresorhus/awesome [🔖 PENDING]
🔗 https://github.com/sindresorhus/awesome


## Meta
- **Stars:** ⭐ 449101 | **Forks:** 🍴 33767
- **Language:** N/A | **License:** CC0-1.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
😎 Awesome lists about all kinds of interesting topics

## README (trích đầu)
```
<div align="center">
	<img width="500" height="350" src="media/logo.svg" alt="Awesome">
	<br>
	<br>
	<br>
	<br>
	<div>
		<sub>Check out my macOS app</sub>
		<br>
		<h2>
			<a href="https://sindresorhus.com/supercharge">Supercharge</a>
			<br>
			<sup>Elevate your Mac experience</sup>
		</h2>
	</div>
	<br>
	<br>
	<br>
	<br>
	<hr>
	<p>
		<sup>
			<a href="https://github.com/sponsors/sindresorhus">My open source work is supported by the community</a>
		</sup>
	</p>
	<p>
		<sup>Special thanks to:</sup>
		<br>
		<br>
		<br>
		<a href="https://nitric.io/?utm_campaign=github_repo&utm_medium=referral&utm_content=sindresorhus&utm_source=github">
			<div>
				<img width="230" src="https://sindresorhus.com/assets/thanks/nitric-logo.svg" alt="nitric logo">
			</div>
			<b>Effortless backends with infrastructure from code</b>
			<div>
				<sup>An open-source framework that supports any programming language, cloud provider, or deployment automation tool.</sup>
			</div>
		</a>
		<br>
		<br>
		<br>
		<h3>
			<a href="https://ref.wisprflow.ai/VjA6dYR">Wispr Flow</a>
		</h3>
		<a href="https://ref.wisprflow.ai/VjA6dYR">
			<div>
				<img width="150" src="https://sindresorhus.com/assets/thanks/flow-logo.svg" alt="Wispr Flow logo">
			</div>
			<b>Talk to code, stay in the Flow.</b>
			<div>
				<sup>Flow is built for devs who live in their tools. Speak and give more context, get better results.</sup>
			</div>
		</a>
		<br>
		<br>
		<br>
		<a href="https://depot.dev?utm_source=github&utm_medium=sindresorhus">
			<div>
				<picture>
					<source width="180" media="(prefers-color-scheme: dark)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-dark.svg">
					<source width="180" media="(prefers-color-scheme: light)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-light.svg">
					<img width="180" src="https://sindresorhus.com/assets/thanks/depot-logo-light.svg" alt="Depot logo">
				</picture>
			</div>
			<b>Fast remote container builds and GitHub Actions runners.</b>
		</a>
		<br>
		<br>
		<br>
	</p>
	<hr>
	<br>
	<br>
	<br>
	<br>
</div>
<p align="center">
	<a href="awesome.md">What is an awesome list?</a>&nbsp;&nbsp;&nbsp;
	<a href="contributing.md">Contribution guide</a>&nbsp;&nbsp;&nbsp;
	<a href="create-list.md">Creating a list</a>&nbsp;&nbsp;&nbsp;
	<a href="https://twitter.com/awesome__re">Twitter</a>&nbsp;&nbsp;&nbsp;
</p>
<br>
<br>
<p align="center">
	Just type <a href="https://awesome.re"><code>awesome.re</code></a> to go here. Check out my <a href="https://sindresorhus.com/apps">apps</a> and follow me on <a href="https://twitter.com/sindresorhus">Twitter</a>.
</p>
<br>
<br>
<br>

## Contents

- [Platforms](#platforms)
- [Programming Languages](#programming-languages)
- [Front-End Development](#front-end-development)
- [Back-End Development](#back-end-development)
- [Computer Science](#computer-science)
- [Big Data](#big-data)
- [Theory](#theory)
- [Books](#books)
- [Editors](#editors)
- [Gaming](#gaming)
- [Development Environment](#deve
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `configstore.md`
```markdown
# 📦 sindresorhus/configstore [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/configstore


## Meta
- **Stars:** ⭐ 888 | **Forks:** 🍴 56
- **Language:** JavaScript | **License:** BSD-2-Clause
- **Last updated:** 2026-03-16
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Easily load and persist config without having to think about where and how

## README (trích đầu)
```
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

You can use [dot-n
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `emittery.md`
```markdown
# 📦 sindresorhus/emittery [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/emittery


## Meta
- **Stars:** ⭐ 2042 | **Forks:** 🍴 83
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Simple and modern async event emitter

## README (trích đầu)
```
# <img src="media/header.png" width="1000">

> Simple and modern async event emitter

<!-- [![Coverage Status](https://codecov.io/gh/sindresorhus/emittery/branch/main/graph/badge.svg)](https://codecov.io/gh/sindresorhus/emittery) -->
[![](https://badgen.net/bundlephobia/minzip/emittery)](https://bundlephobia.com/result?p=emittery)

It works in Node.js and the browser (using a bundler).

**Highlights**

- Async-first — listeners are deferred to the next microtask, keeping your code non-blocking
- TypeScript support with strongly typed events
- Async iteration and `for await...of` support
- [Lifecycle hooks](#initeventname-initfn) (`init`/`deinit`) for lazy resource setup and teardown
- [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) support for cancellation
- [`Symbol.dispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose) / [`Symbol.asyncDispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose) support for automatic cleanup
- [Meta events](#custom-subscribable-events) for observing listener changes
- [Debug mode](#debugging) with customizable logging
- Zero dependencies

Emitting events asynchronously is important for production code where you want the least amount of synchronous operations. Since JavaScript is single-threaded, no other code can run while doing synchronous operations. For Node.js, that means it will block other requests, defeating the strength of the platform, which is scalability through async. In the browser, a synchronous operation could potentially cause lags and block user interaction.

## Install

```sh
npm install emittery
```

## Usage

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on('🦄', ({data}) => {
	console.log(data);
});

const myUnicorn = Symbol('🦄');

emitter.on(myUnicorn, ({data}) => {
	console.log(`Unicorns love ${data}`);
});

emitter.emit('🦄', '🌈'); // Will trigger printing '🌈'
emitter.emit(myUnicorn, '🦋');  // Will trigger printing 'Unicorns love 🦋'
```

## API

### eventName

Emittery accepts strings, symbols, and numbers as event names.

Symbol event names are preferred given that they can be used to avoid name collisions when your classes are extended, especially for internal events.

### isDebugEnabled

Toggle debug mode for all instances.

Default: `true` if the `DEBUG` environment variable is set to `emittery` or `*`, otherwise `false`.

Example:

```js
import Emittery from 'emittery';

Emittery.isDebugEnabled = true;

const emitter1 = new Emittery({debug: {name: 'myEmitter1'}});
const emitter2 = new Emittery({debug: {name: 'myEmitter2'}});

emitter1.on('test', () => {
	// …
});

emitter2.on('otherTest', () => {
	// …
});

emitter1.emit('test');
//=> [16:43:20.417][emittery:subscribe][myEmitter1] Event Name: test
//	data: undefined

emitter2.emit('otherTest');
//=> [16:43:20.417][emittery:subscribe][myEmitter2] Event Name: otherTest
//	
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `execa.md`
```markdown
# 📦 sindresorhus/execa [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/execa


## Meta
- **Stars:** ⭐ 7474 | **Forks:** 🍴 247
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Process execution for humans

## README (trích đầu)
```
<picture>
	<source media="(prefers-color-scheme: dark)" srcset="media/logo_dark.svg">
	<img alt="execa logo" src="media/logo.svg" width="400">
</picture>
<br>

[![Coverage Status](https://codecov.io/gh/sindresorhus/execa/branch/main/graph/badge.svg)](https://codecov.io/gh/sindresorhus/execa)

> Process execution for humans

<br>

---

<div align="center">
	<p>
		<p>
			<sup>
				<a href="https://github.com/sponsors/sindresorhus">Sindre's open source work is supported by the community</a>
			</sup>
		</p>
		<sup>Special thanks to:</sup>
		<br>
		<br>
		<br>
		<a href="https://coderabbit.ai?utm_source=sindre&utm_medium=execa">
			<img width="300" src="https://sindresorhus.com/assets/thanks/coderabbit-logo.png" alt="CodeRabbit logo">
		</a>
		<br>
		<br>
		<br>
		<a href="https://kruu.com">
			<picture>
				<source srcset="https://sindresorhus.com/assets/thanks/kruu-logo-dark.svg?y" media="(prefers-color-scheme: dark)" width="260">
				<source srcset="https://sindresorhus.com/assets/thanks/kruu-logo-light.svg?y" media="(prefers-color-scheme: light)" width="260">
				<img src="https://sindresorhus.com/assets/thanks/kruu-logo-light.svg?y" width="260"alt="KRUU logo">
			</picture>
		</a>
		<br>
		<br>
		<br>
		<a href="https://depot.dev?utm_source=github&utm_medium=sindresorhus">
			<div>
				<picture>
					<source width="180" media="(prefers-color-scheme: dark)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-dark.svg">
					<source width="180" media="(prefers-color-scheme: light)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-light.svg">
					<img width="180" src="https://sindresorhus.com/assets/thanks/depot-logo-light.svg" alt="Depot logo">
				</picture>
			</div>
			<b>Fast remote container builds and GitHub Actions runners.</b>
		</a>
		<br>
		<br>
		<br>
	</p>
</div>

---

<br>

Execa runs commands in your script, application or library. Unlike shells, it is [optimized](docs/bash.md) for programmatic usage. Built on top of the [`child_process`](https://nodejs.org/api/child_process.html) core module.

## Features

- [Simple syntax](#simple-syntax): promises and [template strings](docs/execution.md#template-string-syntax), like [`zx`](docs/bash.md).
- [Script](#script) interface.
- [No escaping](docs/escaping.md) nor quoting needed. No risk of shell injection.
- Execute [locally installed binaries](#local-binaries) without `npx`.
- Improved [Windows support](docs/windows.md): [shebangs](docs/windows.md#shebang), [`PATHEXT`](https://ss64.com/nt/path.html#pathext), [graceful termination](#graceful-termination), [and more](https://github.com/moxystudio/node-cross-spawn?tab=readme-ov-file#why).
- [Detailed errors](#detailed-error), [verbose mode](#verbose-mode) and [custom logging](#custom-logging), for [debugging](docs/debugging.md).
- [Pipe multiple subprocesses](#pipe-multiple-subprocesses) better than in shells: retrieve [intermediate results](docs/pipe.md#result), use multiple [sources](docs/pipe.md#multiple-sources-1-destin
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `file-type.md`
```markdown
# 📦 sindresorhus/file-type [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/file-type


## Meta
- **Stars:** ⭐ 4252 | **Forks:** 🍴 395
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Detect the file type of a file, stream, or data

## README (trích đầu)
```
<h1 align="center" title="file-type">
	<img src="media/logo.jpg" alt="file-type logo">
</h1>

> Detect the file type of a file, stream, or data

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

This package is for detecting binary-based file formats, not text-based formats like `.txt`, `.csv`, `.svg`, etc.

We accept contributions for commonly used modern file formats, not historical or obscure ones. Open an issue first for discussion.

## Install

```sh
npm install file-type
```

**This package is an ESM package. Your project needs to be ESM too. [Read more](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c). For TypeScript + CommonJS, see [`load-esm`](https://github.com/Borewit/load-esm).** If you use it with Webpack, you need the latest Webpack version and ensure you configure it correctly for ESM.

> [!IMPORTANT]
> File type detection is based on binary signatures (magic numbers) and is a best-effort hint. It does not guarantee the file is actually of that type or that the file is valid/not malformed.
>
> Robustness against malformed input is best-effort. When processing untrusted files on a server, enforce a reasonable file size limit and use a worker thread with a timeout (e.g., [`make-asynchronous`](https://github.com/sindresorhus/make-asynchronous)). These are not considered security issues in this package.

## Usage

### Node.js

Determine file type from a file:

```js
import {fileTypeFromFile} from 'file-type';

console.log(await fileTypeFromFile('Unicorn.png'));
//=> {ext: 'png', mime: 'image/png'}
```

Determine file type from a Uint8Array/ArrayBuffer, which may be a portion of the beginning of a file:

```js
import {fileTypeFromBuffer} from 'file-type';
import {readChunk} from 'read-chunk';

const buffer = await readChunk('Unicorn.png', {length: 4100});

console.log(await fileTypeFromBuffer(buffer));
//=> {ext: 'png', mime: 'image/png'}
```

Determine file type from a stream:

```js
import {fileTypeFromStream} from 'file-type';

const url = 'https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg';

const response = await fetch(url);
const fileType = await fileTypeFromStream(response.body);

console.log(fileType);
//=> {ext: 'jpg', mime: 'image/jpeg'}
```

## API

### fileTypeFromBuffer(buffer, options)

Detect the file type of a `Uint8Array` or `ArrayBuffer`.

The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of the buffer.

If file access is available, it is recommended to use `fileTypeFromFile()` instead.

Returns a `Promise` for an object with the detected file type:

- `ext` - One of the [supported file types](#supported-file-types)
- `mime` - The [MIME type](https://en.wikipedia.org/wiki/Internet_media_type)

Or `undefined` when there is no match.

#### buffer

Type: `Uint8Array | ArrayBuffer`

A buffer representing
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `find-cache-directory.md`
```markdown
# 📦 sindresorhus/find-cache-directory [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/find-cache-directory


## Meta
- **Stars:** ⭐ 162 | **Forks:** 🍴 24
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-10
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Finds the common standard cache directory

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `got.md`
```markdown
# 📦 sindresorhus/got [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/got


## Meta
- **Stars:** ⭐ 14882 | **Forks:** 🍴 981
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🌐 Human-friendly and powerful HTTP request library for Node.js

## README (trích đầu)
```
<div align="center">
	<br>
	<br>
	<img width="360" src="media/logo.svg" alt="Got">
	<br>
	<br>
	<br>
	<br>
	<hr>
	<p>
		<p>
			<sup>
				Sindre's open source work is supported by the community.<br>Special thanks to:
			</sup>
		</p>
		<br>
		<br>
		<a href="https://www.fame.fi#gh-light-mode-only">
			<img src="https://sindresorhus.com/assets/thanks/fame-logo-light.svg" width="200" alt="Fame Helsinki">
		</a>
		<a href="https://www.fame.fi#gh-dark-mode-only">
			<img src="https://sindresorhus.com/assets/thanks/fame-logo-dark.svg" width="200" alt="Fame Helsinki">
		</a>
		<br>
		<br>
		<br>
		<br>
		<a href="https://depot.dev?utm_source=github&utm_medium=sindresorhus">
			<div>
				<picture>
					<source width="180" media="(prefers-color-scheme: dark)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-dark.svg">
					<source width="180" media="(prefers-color-scheme: light)" srcset="https://sindresorhus.com/assets/thanks/depot-logo-light.svg">
					<img width="180" src="https://sindresorhus.com/assets/thanks/depot-logo-light.svg" alt="Depot logo">
				</picture>
			</div>
			<b>Fast remote container builds and GitHub Actions runners.</b>
		</a>
		<br>
		<br>
		<br>
	</p>
	<hr>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
</div>

> Human-friendly and powerful HTTP request library for Node.js

<!-- [![Coverage Status](https://codecov.io/gh/sindresorhus/got/branch/main/graph/badge.svg)](https://codecov.io/gh/sindresorhus/got/branch/main) -->
[![Downloads](https://img.shields.io/npm/dm/got.svg)](https://npmjs.com/got)
[![Install size](https://packagephobia.com/badge?p=got)](https://packagephobia.com/result?p=got)

[See how Got compares to other HTTP libraries](#comparison)

---

**You probably want [Ky](https://github.com/sindresorhus/ky) instead, by the same people. It's smaller, works in the browser too, and is more stable since it's built on [`Fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). Or [fetch-extras](https://github.com/sindresorhus/fetch-extras) for simple needs.**

---

**Support questions should be asked [here](https://github.com/sindresorhus/got/discussions).**

## Install

```sh
npm install got
```

**Warning:** This package is native [ESM](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) and no longer provides a CommonJS export. If your project uses CommonJS, you will have to [convert to ESM](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c). Please don't open issues for questions regarding CommonJS / ESM.

**Got v11 is no longer maintained and we will not accept any backport requests.**

## Take a peek

**A [quick start](documentation/quick-start.md) guide is available.**

### JSON mode

Got has a dedicated option for handling JSON payload.\
Furthermore, the promise exposes a `.json<T>()` function that returns `Promise<T>`.

```js
import got from 'got';

const {data} = await got.post('https://httpbin.org/anything', {
	json: {
		hello: 'world'
	}
}).json();

console.log
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `is.md`
```markdown
# 📦 sindresorhus/is [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/is


## Meta
- **Stars:** ⭐ 1766 | **Forks:** 🍴 122
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Type check values

## README (trích đầu)
```
# is

> Type check values

For example, `is.string('🦄') //=> true`

<img src="header.gif" width="182" align="right">

## Highlights

- Written in TypeScript
- [Extensive use of type guards](#type-guards)
- [Supports type assertions](#type-assertions)
- [Aware of generic type parameters](#generic-type-parameters) (use with caution)
- Actively maintained
- ![Millions of downloads per week](https://img.shields.io/npm/dw/@sindresorhus/is)

## Install

```sh
npm install @sindresorhus/is
```

## Usage

```js
import is from '@sindresorhus/is';

is('🦄');
//=> 'string'

is(new Map());
//=> 'Map'

is.number(6);
//=> true
```

[Assertions](#type-assertions) perform the same type checks, but throw an error if the type does not match.

```js
import {assert} from '@sindresorhus/is';

assert.string(2);
//=> Error: Expected value which is `string`, received value of type `number`.
```

Assertions (except `assertAll` and `assertAny`) also support an optional custom error message.

```js
import {assert} from '@sindresorhus/is';

assert.nonEmptyString(process.env.API_URL, 'The API_URL environment variable is required.');
//=> Error: The API_URL environment variable is required.
```

And with TypeScript:

```ts
import {assert} from '@sindresorhus/is';

assert.string(foo);
// `foo` is now typed as a `string`.
```

### Named exports

Named exports allow tooling to perform tree-shaking, potentially reducing bundle size by including only code from the methods that are used.

Every method listed below is available as a named export. Each method is prefixed by either `is` or `assert` depending on usage.

For example:

```js
import {assertNull, isUndefined} from '@sindresorhus/is';
```

## API

### is(value)

Returns the type of `value`.

Primitives are lowercase and object types are camelcase.

Example:

- `'undefined'`
- `'null'`
- `'string'`
- `'symbol'`
- `'Array'`
- `'Function'`
- `'Object'`

This method is also exported as `detect`. You can import it like this:

```js
import {detect} from '@sindresorhus/is';
```

Note: It will throw an error if you try to feed it object-wrapped primitives, as that's a bad practice. For example `new String('foo')`.

### is.{method}

All the below methods accept a value and return a boolean for whether the value is of the desired type.

#### Primitives

##### .undefined(value)
##### .null(value)

##### .string(value)
##### .number(value)

Note: `is.number(NaN)` returns `false`. This intentionally deviates from `typeof` behavior to increase user-friendliness of `is` type checks.

##### .boolean(value)
##### .symbol(value)
##### .bigint(value)

#### Built-in types

##### .array(value, assertion?)

Returns true if `value` is an array and all of its items match the assertion (if provided).

```js
is.array(value); // Validate `value` is an array.
is.array(value, is.number); // Validate `value` is an array and all of its items are numbers.
```

##### .function(value)

##### .buffer(value)

> [!NOTE]
> [Prefer using `Uint8Array` instead of `B
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `ora.md`
```markdown
# 📦 sindresorhus/ora [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/ora


## Meta
- **Stars:** ⭐ 9647 | **Forks:** 🍴 285
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Elegant terminal spinner

## README (trích đầu)
```
# ora

> Elegant terminal spinner

<p align="center">
	<br>
	<img src="screenshot.svg" width="500">
	<br>
</p>

## Install

```sh
npm install ora
```

*Check out [`yocto-spinner`](https://github.com/sindresorhus/yocto-spinner) for a smaller alternative.*

## Usage

```js
import ora from 'ora';

const spinner = ora('Loading unicorns').start();

setTimeout(() => {
	spinner.color = 'yellow';
	spinner.text = 'Loading rainbows';
}, 1000);
```

## API

### ora(text)
### ora(options)

If a string is provided, it is treated as a shortcut for [`options.text`](#text).

#### options

Type: `object`

##### text

Type: `string`

The text to display next to the spinner.

##### prefixText

Type: `string | () => string`

Text or a function that returns text to display before the spinner. No prefix text will be displayed if set to an empty string.

##### suffixText

Type: `string | () => string`

Text or a function that returns text to display after the spinner text. No suffix text will be displayed if set to an empty string.

##### spinner

Type: `string | object`\
Default: `'dots'` <img src="screenshot-spinner.gif" width="14">

The name of one of the [provided spinners](#spinners). See `example.js` in this repo if you want to test out different spinners. On Windows (except for Windows Terminal), it will always use the `line` spinner as the Windows command-line doesn't have proper Unicode support.

Or an object like:

```js
{
	frames: ['-', '+', '-'],
	interval: 80 // Optional
}
```

##### color

Type: `string | boolean`\
Default: `'cyan'`\
Values: `'black' | 'red' | 'green' | 'yellow' | 'blue' | 'magenta' | 'cyan' | 'white' | 'gray' | boolean`

The color of the spinner. Set to `false` to disable coloring.

##### hideCursor

Type: `boolean`\
Default: `true`

Set to `false` to stop Ora from hiding the cursor.

##### indent

Type: `number`\
Default: `0`

Indent the spinner with the given number of spaces.

##### interval

Type: `number`\
Default: Provided by the spinner or `100`

Interval between each frame.

Spinners provide their own recommended interval, so you don't really need to specify this.

##### stream

Type: `stream.Writable`\
Default: `process.stderr`

Stream to write the output.

You could for example set this to `process.stdout` instead.

##### isEnabled

Type: `boolean`

Force enable/disable the spinner. If not specified, the spinner will be enabled if the `stream` is being run inside a TTY context (not spawned or piped) and/or not in a CI environment.

Note that `{isEnabled: false}` doesn't mean it won't output anything. It just means it won't output the spinner, colors, and other ansi escape codes. It will still log text.

##### isSilent

Type: `boolean`\
Default: `false`

Disable the spinner and all log text. All output is suppressed and `isEnabled` will be considered `false`.

##### discardStdin

Type: `boolean`\
Default: `true`

Discard stdin input (except Ctrl+C) while running if it's TTY. This prevents the spinner from twitching on input, out
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `update-notifier.md`
```markdown
# 📦 sindresorhus/update-notifier [🔖 PENDING/APPROVE]
🔗 https://github.com/sindresorhus/update-notifier


## Meta
- **Stars:** ⭐ 1794 | **Forks:** 🍴 130
- **Language:** JavaScript | **License:** BSD-2-Clause
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Update notifications for your CLI app

## README (trích đầu)
```
# update-notifier

> Update notifications for your CLI app

![](screenshot.png)

Inform users of updates for your package in a non-intrusive way.

#### Contents

- [Install](#install)
- [Usage](#usage)
- [How](#how)
- [API](#api)
- [About](#about)
- [Users](#users)

## Install

```sh
npm install update-notifier
```

## Usage

### Basic

```js
import updateNotifier from 'update-notifier';
import packageJson from './package.json' assert {type: 'json'};

updateNotifier({pkg: packageJson}).notify();
```

### Advanced

```js
import updateNotifier from 'update-notifier';
import packageJson from './package.json' assert {type: 'json'};

// Checks for available update and returns an instance
const notifier = updateNotifier({pkg: packageJson});

// Notify using the built-in convenience method
notifier.notify();

// `notifier.update` contains some useful info about the update
console.log(notifier.update);
/*
{
	latest: '1.0.1',
	current: '1.0.0',
	type: 'patch', // Possible values: latest, major, minor, patch, prerelease, build
	name: 'pageres'
}
*/
```

### Options and custom message

```js
const notifier = updateNotifier({
	pkg,
	updateCheckInterval: 1000 * 60 * 60 * 24 * 7 // 1 week
});

if (notifier.update) {
	console.log(`Update available: ${notifier.update.latest}`);
}
```

## How it works

Whenever you initiate the update notifier and it's not within the interval threshold, it will asynchronously check with npm in the background for available updates, then persist the result. The next time the notifier is initiated, the result will be loaded into the `.update` property. This prevents any impact on your package startup performance.
The update check is done in an unref'ed [child process](https://nodejs.org/api/child_process.html#child_process_child_process_spawn_command_args_options). This means that if you call `process.exit`, the check will still be performed in its own process.

The first time the user runs your app, it will check for an update, and even if an update is available, it will wait the specified `updateCheckInterval` before notifying the user. This is done to not be annoying to the user, but might surprise you as an implementer if you're testing whether it works. Check out [`example.js`](example.js) to quickly test out `update-notifier` and see how you can test that it works in your app.

## API

### notifier = updateNotifier(options)

Checks if there is an available update. Accepts options defined below. Returns an instance with an `.update` property if there is an available update, otherwise `undefined`.

### options

Type: `object`

#### pkg

Type: `object`

##### name

*Required*\
Type: `string`

##### version

*Required*\
Type: `string`

#### updateCheckInterval

Type: `number`\
Default: `1000 * 60 * 60 * 24` *(1 day)*

How often to check for updates.

#### shouldNotifyInNpmScript

Type: `boolean`\
Default: `false`

Allows notification to be shown when running as an npm script.

#### distTag

Type: `string`\
Default: `'latest'`

Whi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

