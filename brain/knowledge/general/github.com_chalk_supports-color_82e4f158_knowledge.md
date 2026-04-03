---
id: github.com-chalk-supports-color-82e4f158-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:37.056488
---

# KNOWLEDGE EXTRACT: github.com_chalk_supports-color_82e4f158
> **Extracted on:** 2026-04-01 11:38:49
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521421/github.com_chalk_supports-color_82e4f158

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

## File: `browser.d.ts`
```typescript
export {default} from './index.js';
```

## File: `browser.js`
```javascript
/* eslint-env browser */
/* eslint-disable n/no-unsupported-features/node-builtins */

const level = (() => {
	if (!('navigator' in globalThis)) {
		return 0;
	}

	if (globalThis.navigator.userAgentData) {
		const brand = navigator.userAgentData.brands.find(({brand}) => brand === 'Chromium');
		if (brand?.version > 93) {
			return 3;
		}
	}

	if (/\b(Chrome|Chromium)\//.test(globalThis.navigator.userAgent)) {
		return 1;
	}

	return 0;
})();

const colorSupport = level !== 0 && {
	level,
	hasBasic: true,
	has256: level >= 2,
	has16m: level >= 3,
};

const supportsColor = {
	stdout: colorSupport,
	stderr: colorSupport,
};

export default supportsColor;
```

## File: `index.d.ts`
```typescript
import type {WriteStream} from 'node:tty';

export type Options = {
	/**
	Whether `process.argv` should be sniffed for `--color` and `--no-color` flags.

	@default true
	*/
	readonly sniffFlags?: boolean;
};

/**
Levels:
- `0` - All colors disabled.
- `1` - Basic 16 colors support.
- `2` - ANSI 256 colors support.
- `3` - Truecolor 16 million colors support.
*/
export type ColorSupportLevel = 0 | 1 | 2 | 3;

/**
Detect whether the terminal supports color.
*/
export type ColorSupport = {
	/**
	The color level.
	*/
	level: ColorSupportLevel;

	/**
	Whether basic 16 colors are supported.
	*/
	hasBasic: boolean;

	/**
	Whether ANSI 256 colors are supported.
	*/
	has256: boolean;

	/**
	Whether Truecolor 16 million colors are supported.
	*/
	has16m: boolean;
};

export type ColorInfo = ColorSupport | false;

export function createSupportsColor(stream?: WriteStream, options?: Options): ColorInfo;

declare const supportsColor: {
	stdout: ColorInfo;
	stderr: ColorInfo;
};

export default supportsColor;
```

## File: `index.js`
```javascript
import process from 'node:process';
import os from 'node:os';
import tty from 'node:tty';

// From: https://github.com/sindresorhus/has-flag/blob/main/index.js
/// function hasFlag(flag, argv = globalThis.Deno?.args ?? process.argv) {
function hasFlag(flag, argv = globalThis.Deno ? globalThis.Deno.args : process.argv) {
	const prefix = flag.startsWith('-') ? '' : (flag.length === 1 ? '-' : '--');
	const position = argv.indexOf(prefix + flag);
	const terminatorPosition = argv.indexOf('--');
	return position !== -1 && (terminatorPosition === -1 || position < terminatorPosition);
}

const {env} = process;

let flagForceColor;
if (
	hasFlag('no-color')
	|| hasFlag('no-colors')
	|| hasFlag('color=false')
	|| hasFlag('color=never')
) {
	flagForceColor = 0;
} else if (
	hasFlag('color')
	|| hasFlag('colors')
	|| hasFlag('color=true')
	|| hasFlag('color=always')
) {
	flagForceColor = 1;
}

function envForceColor() {
	if (!('FORCE_COLOR' in env)) {
		return;
	}

	if (env.FORCE_COLOR === 'true') {
		return 1;
	}

	if (env.FORCE_COLOR === 'false') {
		return 0;
	}

	if (env.FORCE_COLOR.length === 0) {
		return 1;
	}

	const level = Math.min(Number.parseInt(env.FORCE_COLOR, 10), 3);

	if (![0, 1, 2, 3].includes(level)) {
		return;
	}

	return level;
}

function translateLevel(level) {
	if (level === 0) {
		return false;
	}

	return {
		level,
		hasBasic: true,
		has256: level >= 2,
		has16m: level >= 3,
	};
}

function _supportsColor(haveStream, {streamIsTTY, sniffFlags = true} = {}) {
	const noFlagForceColor = envForceColor();
	if (noFlagForceColor !== undefined) {
		flagForceColor = noFlagForceColor;
	}

	const forceColor = sniffFlags ? flagForceColor : noFlagForceColor;

	if (forceColor === 0) {
		return 0;
	}

	if (sniffFlags) {
		if (hasFlag('color=16m')
			|| hasFlag('color=full')
			|| hasFlag('color=truecolor')) {
			return 3;
		}

		if (hasFlag('color=256')) {
			return 2;
		}
	}

	// Check for Azure DevOps pipelines.
	// Has to be above the `!streamIsTTY` check.
	if ('TF_BUILD' in env && 'AGENT_NAME' in env) {
		return 1;
	}

	if (haveStream && !streamIsTTY && forceColor === undefined) {
		return 0;
	}

	const min = forceColor || 0;

	if (env.TERM === 'dumb') {
		return min;
	}

	if (process.platform === 'win32') {
		// Windows 10 build 10586 is the first Windows release that supports 256 colors.
		// Windows 10 build 14931 is the first release that supports 16m/TrueColor.
		const osRelease = os.release().split('.');
		if (
			Number(osRelease[0]) >= 10
			&& Number(osRelease[2]) >= 10_586
		) {
			return Number(osRelease[2]) >= 14_931 ? 3 : 2;
		}

		return 1;
	}

	if ('CI' in env) {
		if (['GITHUB_ACTIONS', 'GITEA_ACTIONS', 'CIRCLECI'].some(key => key in env)) {
			return 3;
		}

		if (['TRAVIS', 'APPVEYOR', 'GITLAB_CI', 'BUILDKITE', 'DRONE'].some(sign => sign in env) || env.CI_NAME === 'codeship') {
			return 1;
		}

		return min;
	}

	if ('TEAMCITY_VERSION' in env) {
		return /^(9\.(0*[1-9]\d*)\.|\d{2,}\.)/.test(env.TEAMCITY_VERSION) ? 1 : 0;
	}

	if (env.COLORTERM === 'truecolor') {
		return 3;
	}

	if (env.TERM === 'xterm-kitty') {
		return 3;
	}

	if (env.TERM === 'xterm-ghostty') {
		return 3;
	}

	if (env.TERM === 'wezterm') {
		return 3;
	}

	if ('TERM_PROGRAM' in env) {
		const version = Number.parseInt((env.TERM_PROGRAM_VERSION || '').split('.')[0], 10);

		switch (env.TERM_PROGRAM) {
			case 'iTerm.app': {
				return version >= 3 ? 3 : 2;
			}

			case 'Apple_Terminal': {
				return 2;
			}
			// No default
		}
	}

	if (/-256(color)?$/i.test(env.TERM)) {
		return 2;
	}

	if (/^screen|^xterm|^vt100|^vt220|^rxvt|color|ansi|cygwin|linux/i.test(env.TERM)) {
		return 1;
	}

	if ('COLORTERM' in env) {
		return 1;
	}

	return min;
}

export function createSupportsColor(stream, options = {}) {
	const level = _supportsColor(stream, {
		streamIsTTY: stream && stream.isTTY,
		...options,
	});

	return translateLevel(level);
}

const supportsColor = {
	stdout: createSupportsColor({isTTY: tty.isatty(1)}),
	stderr: createSupportsColor({isTTY: tty.isatty(2)}),
};

export default supportsColor;
```

## File: `index.test-d.ts`
```typescript
import {stdout, stderr} from 'node:process';
import {expectType} from 'tsd';
import supportsColor, {createSupportsColor, type Options, type ColorInfo} from './index.js';

const options: Options = {};

expectType<ColorInfo>(supportsColor.stdout);
expectType<ColorInfo>(supportsColor.stderr);

expectType<ColorInfo>(createSupportsColor(stdout));
expectType<ColorInfo>(createSupportsColor(stderr));
expectType<ColorInfo>(createSupportsColor(undefined));

expectType<ColorInfo>(createSupportsColor(stdout, options));
```

## File: `license`
```
MIT License

Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (https://sindresorhus.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `package.json`
```json
{
	"name": "supports-color",
	"version": "10.2.2",
	"description": "Detect whether a terminal supports color",
	"license": "MIT",
	"repository": "chalk/supports-color",
	"funding": "https://github.com/chalk/supports-color?sponsor=1",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": {
		"types": "./index.d.ts",
		"node": "./index.js",
		"default": "./browser.js"
	},
	"sideEffects": false,
	"engines": {
		"node": ">=18"
	},
	"scripts": {
		"test": "xo && ava && tsd"
	},
	"files": [
		"index.js",
		"index.d.ts",
		"browser.js",
		"browser.d.ts"
	],
	"keywords": [
		"color",
		"colour",
		"colors",
		"terminal",
		"console",
		"cli",
		"ansi",
		"styles",
		"tty",
		"rgb",
		"256",
		"shell",
		"xterm",
		"command-line",
		"support",
		"supports",
		"capability",
		"detect",
		"truecolor",
		"16m"
	],
	"devDependencies": {
		"@types/node": "^22.10.2",
		"ava": "^6.2.0",
		"tsd": "^0.31.2",
		"xo": "^0.60.0"
	},
	"ava": {
		"serial": true,
		"workerThreads": false
	}
}
```

## File: `readme.md`
```markdown
# supports-color

> Detect whether a terminal supports color

## Install

```sh
npm install supports-color
```

## Usage

```js
import supportsColor from 'supports-color';

if (supportsColor.stdout) {
	console.log('Terminal stdout supports color');
}

if (supportsColor.stdout.has256) {
	console.log('Terminal stdout supports 256 colors');
}

if (supportsColor.stderr.has16m) {
	console.log('Terminal stderr supports 16 million colors (truecolor)');
}
```

## API

Returns an `object` with a `stdout` and `stderr` property for testing either streams. Each property is an `Object`, or `false` if color is not supported.

The `stdout`/`stderr` objects specifies a level of support for color through a `.level` property and a corresponding flag:

- `.level = 1` and `.hasBasic = true`: Basic color support (16 colors)
- `.level = 2` and `.has256 = true`: 256 color support
- `.level = 3` and `.has16m = true`: Truecolor support (16 million colors)

### Custom instance

The package also exposes the named export `createSupportColor` function that takes an arbitrary write stream (for example, `process.stdout`) and an optional options object to (re-)evaluate color support for an arbitrary stream.

```js
import {createSupportsColor} from 'supports-color';

const stdoutSupportsColor = createSupportsColor(process.stdout);

if (stdoutSupportsColor) {
	console.log('Terminal stdout supports color');
}

// `stdoutSupportsColor` is the same as `supportsColor.stdout`
```

The options object supports a single boolean property `sniffFlags`. By default it is `true`, which instructs the detection to sniff `process.argv` for the multitude of `--color` flags (see _Info_ below). If `false`, then `process.argv` is not considered when determining color support.

## Info

It obeys the `--color` and `--no-color` CLI flags.

For situations where using `--color` is not possible, use the environment variable `FORCE_COLOR=1` (level 1), `FORCE_COLOR=2` (level 2), or `FORCE_COLOR=3` (level 3) to forcefully enable color, or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.

Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.

## Related

- [supports-color-cli](https://github.com/chalk/supports-color-cli) - CLI for this module
- [supports-hyperlinks](https://github.com/chalk/supports-hyperlinks) - Detect whether a terminal supports hyperlinks
- [supports-terminal-graphics](https://github.com/sindresorhus/supports-terminal-graphics) - Detect which terminal graphics protocols are supported
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right
- [is-unicode-supported](https://github.com/sindresorhus/is-unicode-supported) - Detect whether the terminal supports Unicode
- [is-interactive](https://github.com/sindresorhus/is-interactive) - Check if stdout or stderr is interactive

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)
```

## File: `test.js`
```javascript
import {randomInt} from 'node:crypto';
import process from 'node:process';
import os from 'node:os';
import tty from 'node:tty';
import test from 'ava';

const currentNodeVersion = process.versions.node;

const importFresh = async moduleName => import(`${moduleName}?${randomInt(100_000_000)}`);

const importMain = async () => {
	const {default: main} = await importFresh('./index.js');
	return main;
};

test.beforeEach(() => {
	Object.defineProperty(process, 'platform', {
		value: 'linux',
	});

	Object.defineProperty(process.versions, 'node', {
		value: currentNodeVersion,
	});

	process.stdout.isTTY = true;
	process.argv = [];
	process.env = {};
	tty.isatty = () => true;
});

test('return true if `FORCE_COLOR` is in env', async t => {
	process.stdout.isTTY = false;
	process.env.FORCE_COLOR = 'true';
	const result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 1);
});

test('return true if `FORCE_COLOR` is in env, but honor 256', async t => {
	process.argv = ['--color=256'];
	process.env.FORCE_COLOR = 'true';
	const result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 2);
});

test('return true if `FORCE_COLOR` is in env, but honor 256 #2', async t => {
	process.argv = ['--color=256'];
	process.env.FORCE_COLOR = '1';
	const result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 2);
});

test('return false if `FORCE_COLOR` is in env and is 0', async t => {
	process.env.FORCE_COLOR = '0';
	const result = await importMain();
	t.false(result.stdout);
});

test('do not cache `FORCE_COLOR`', async t => {
	process.env.FORCE_COLOR = '0';
	const {default: result, createSupportsColor} = await importFresh('./index.js');
	t.false(result.stdout);
	process.env.FORCE_COLOR = '1';
	const updatedStdOut = createSupportsColor({isTTY: tty.isatty(1)});
	t.truthy(updatedStdOut);
});

test('return false if not TTY', async t => {
	process.stdout.isTTY = false;
	const result = await importMain();
	t.false(result.stdout);
});

test('return false if --no-color flag is used', async t => {
	process.env = {TERM: 'xterm-256color'};
	process.argv = ['--no-color'];
	const result = await importMain();
	t.false(result.stdout);
});

test('return false if --no-colors flag is used', async t => {
	process.env = {TERM: 'xterm-256color'};
	process.argv = ['--no-colors'];
	const result = await importMain();
	t.false(result.stdout);
});

test('return true if --color flag is used', async t => {
	process.argv = ['--color'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return true if --colors flag is used', async t => {
	process.argv = ['--colors'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return true if `COLORTERM` is in env', async t => {
	process.env.COLORTERM = true;
	const result = await importMain();
	t.truthy(result.stdout);
});

test('support `--color=true` flag', async t => {
	process.argv = ['--color=true'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('support `--color=always` flag', async t => {
	process.argv = ['--color=always'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('support `--color=false` flag', async t => {
	process.env = {TERM: 'xterm-256color'};
	process.argv = ['--color=false'];
	const result = await importMain();
	t.false(result.stdout);
});

test('support `--color=256` flag', async t => {
	process.argv = ['--color=256'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('level should be 2 if `--color=256` flag is used', async t => {
	process.argv = ['--color=256'];
	const result = await importMain();
	t.is(result.stdout.level, 2);
	t.true(result.stdout.has256);
});

test('support `--color=16m` flag', async t => {
	process.argv = ['--color=16m'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('support `--color=full` flag', async t => {
	process.argv = ['--color=full'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('support `--color=truecolor` flag', async t => {
	process.argv = ['--color=truecolor'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('level should be 3 if `--color=16m` flag is used', async t => {
	process.argv = ['--color=16m'];
	const result = await importMain();
	t.is(result.stdout.level, 3);
	t.true(result.stdout.has256);
	t.true(result.stdout.has16m);
});

test('ignore post-terminator flags', async t => {
	process.argv = ['--color', '--', '--no-color'];
	const result = await importMain();
	t.truthy(result.stdout);
});

test('allow tests of the properties on false', async t => {
	process.env = {TERM: 'xterm-256color'};
	process.argv = ['--no-color'];
	const result = await importMain();
	t.is(result.stdout.hasBasic, undefined);
	t.is(result.stdout.has256, undefined);
	t.is(result.stdout.has16m, undefined);
	t.false(result.stdout.level > 0);
});

test('return false if `CI` is in env', async t => {
	process.env.CI = 'AppVeyor';
	const result = await importMain();
	t.false(result.stdout);
});

test('return true if `TRAVIS` is in env', async t => {
	process.env = {CI: 'Travis', TRAVIS: '1'};
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return level 3 if `CIRCLECI` is in env', async t => {
	process.env = {CI: true, CIRCLECI: true};
	const result = await importMain();
	t.is(result.stdout.level, 3);
});

test('return true if `APPVEYOR` is in env', async t => {
	process.env = {CI: true, APPVEYOR: true};
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return true if `GITLAB_CI` is in env', async t => {
	process.env = {CI: true, GITLAB_CI: true};
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return true if `BUILDKITE` is in env', async t => {
	process.env = {CI: true, BUILDKITE: true};
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return true if `DRONE` is in env', async t => {
	process.env = {CI: true, DRONE: true};
	const result = await importMain();
	t.truthy(result.stdout);
});

test('return level 3 if `GITEA_ACTIONS` is in env', async t => {
	process.env = {CI: true, GITEA_ACTIONS: true};
	const result = await importMain();
	t.is(result.stdout.level, 3);
});

test('return true if Codeship is in env', async t => {
	process.env = {CI: true, CI_NAME: 'codeship'};
	const result = await importMain();
	t.truthy(result);
});

test('return false if `TEAMCITY_VERSION` is in env and is < 9.1', async t => {
	process.env.TEAMCITY_VERSION = '9.0.5 (build 32523)';
	const result = await importMain();
	t.false(result.stdout);
});

test('return level 1 if `TEAMCITY_VERSION` is in env and is >= 9.1', async t => {
	process.env.TEAMCITY_VERSION = '9.1.0 (build 32523)';
	const result = await importMain();
	t.is(result.stdout.level, 1);
});

test('support rxvt', async t => {
	process.env = {TERM: 'rxvt'};
	const result = await importMain();
	t.is(result.stdout.level, 1);
});

test('prefer level 2/xterm over COLORTERM', async t => {
	process.env = {COLORTERM: '1', TERM: 'xterm-256color'};
	const result = await importMain();
	t.is(result.stdout.level, 2);
});

test('support screen-256color', async t => {
	process.env = {TERM: 'screen-256color'};
	const result = await importMain();
	t.is(result.stdout.level, 2);
});

test('support putty-256color', async t => {
	process.env = {TERM: 'putty-256color'};
	const result = await importMain();
	t.is(result.stdout.level, 2);
});

test('level should be 3 when using iTerm 3.0', async t => {
	Object.defineProperty(process, 'platform', {
		value: 'darwin',
	});
	process.env = {
		TERM_PROGRAM: 'iTerm.app',
		TERM_PROGRAM_VERSION: '3.0.10',
	};
	const result = await importMain();
	t.is(result.stdout.level, 3);
});

test('level should be 2 when using iTerm 2.9', async t => {
	Object.defineProperty(process, 'platform', {
		value: 'darwin',
	});
	process.env = {
		TERM_PROGRAM: 'iTerm.app',
		TERM_PROGRAM_VERSION: '2.9.3',
	};
	const result = await importMain();
	t.is(result.stdout.level, 2);
});

test('return level 1 if on Windows earlier than 10 build 10586', async t => {
	Object.defineProperty(process, 'platform', {
		value: 'win32',
	});
	Object.defineProperty(process.versions, 'node', {
		value: '8.0.0',
	});
	os.release = () => '10.0.10240';
	const result = await importMain();
	t.is(result.stdout.level, 1);
});

test('return level 2 if on Windows 10 build 10586 or later', async t => {
	Object.defineProperty(process, 'platform', {
		value: 'win32',
	});
	Object.defineProperty(process.versions, 'node', {
		value: '8.0.0',
	});
	os.release = () => '10.0.10586';
	const result = await importMain();
	t.is(result.stdout.level, 2);
});

test('return level 3 if on Windows 10 build 14931 or later', async t => {
	Object.defineProperty(process, 'platform', {
		value: 'win32',
	});
	Object.defineProperty(process.versions, 'node', {
		value: '8.0.0',
	});
	os.release = () => '10.0.14931';
	const result = await importMain();
	t.is(result.stdout.level, 3);
});

test('return level 2 when FORCE_COLOR is set when not TTY in xterm256', async t => {
	process.stdout.isTTY = false;
	process.env.FORCE_COLOR = 'true';
	process.env.TERM = 'xterm-256color';
	const result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 2);
});

test('supports setting a color level using FORCE_COLOR', async t => {
	let result;
	process.env.FORCE_COLOR = '1';
	result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 1);

	process.env.FORCE_COLOR = '2';
	result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 2);

	process.env.FORCE_COLOR = '3';
	result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 3);

	process.env.FORCE_COLOR = '0';
	result = await importMain();
	t.false(result.stdout);
});

test('FORCE_COLOR maxes out at a value of 3', async t => {
	process.env.FORCE_COLOR = '4';
	const result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 3);
});

test('FORCE_COLOR works when set via command line (all values are strings)', async t => {
	let result;
	process.env.FORCE_COLOR = 'true';
	result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 1);

	process.stdout.isTTY = false;
	process.env.FORCE_COLOR = 'true';
	process.env.TERM = 'xterm-256color';
	result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 2);

	process.env.FORCE_COLOR = 'false';
	result = await importMain();
	t.false(result.stdout);
});

test('return false when `TERM` is set to dumb', async t => {
	process.env.TERM = 'dumb';
	const result = await importMain();
	t.false(result.stdout);
});

test('return false when `TERM` is set to dumb when `TERM_PROGRAM` is set', async t => {
	process.env.TERM = 'dumb';
	process.env.TERM_PROGRAM = 'Apple_Terminal';
	const result = await importMain();
	t.false(result.stdout);
});

test('return false when `TERM` is set to dumb when run on Windows', async t => {
	Object.defineProperty(process, 'platform', {
		value: 'win32',
	});
	Object.defineProperty(process.versions, 'node', {
		value: '10.13.0',
	});
	os.release = () => '10.0.14931';
	process.env.TERM = 'dumb';
	const result = await importMain();
	t.false(result.stdout);
});

test('return level 1 when `TERM` is set to dumb when `FORCE_COLOR` is set', async t => {
	process.env.FORCE_COLOR = '1';
	process.env.TERM = 'dumb';
	const result = await importMain();
	t.truthy(result.stdout);
	t.is(result.stdout.level, 1);
});

test('ignore flags when sniffFlags=false', async t => {
	process.argv = ['--color=256'];
	process.env.TERM = 'dumb';
	const {default: result, createSupportsColor} = await importFresh('./index.js');

	t.truthy(result.stdout);
	t.is(result.stdout.level, 2);

	const sniffResult = createSupportsColor(process.stdout, {sniffFlags: true});
	t.truthy(sniffResult);
	t.is(sniffResult.level, 2);

	const nosniffResult = createSupportsColor(process.stdout, {sniffFlags: false});
	t.falsy(nosniffResult);
});
```

