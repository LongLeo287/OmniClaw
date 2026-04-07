---
id: strip
type: knowledge
owner: OA_Triage
---
# strip
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
import ansiRegex from 'ansi-regex';

const regex = ansiRegex();

export default function stripAnsi(string) {
	if (typeof string !== 'string') {
		throw new TypeError(`Expected a \`string\`, got \`${typeof string}\``);
	}

	// Fast path: ANSI codes require ESC (7-bit) or CSI (8-bit) introducer
	if (!string.includes('\u001B') && !string.includes('\u009B')) {
		return string;
	}

	// Even though the regex is global, we don't need to reset the `.lastIndex`
	// because unlike `.exec()` and `.test()`, `.replace()` does it automatically
	// and doing it manually has a performance penalty.
	return string.replace(regex, '');
}

```

### File: package.json
```json
{
	"name": "strip-ansi",
	"version": "7.2.0",
	"description": "Strip ANSI escape codes from a string",
	"license": "MIT",
	"repository": "chalk/strip-ansi",
	"funding": "https://github.com/chalk/strip-ansi?sponsor=1",
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
		"node": ">=12"
	},
	"scripts": {
		"test": "xo && ava && tsd"
	},
	"files": [
		"index.js",
		"index.d.ts"
	],
	"keywords": [
		"strip",
		"trim",
		"remove",
		"ansi",
		"styles",
		"color",
		"colour",
		"colors",
		"terminal",
		"console",
		"string",
		"tty",
		"escape",
		"formatting",
		"rgb",
		"256",
		"shell",
		"xterm",
		"log",
		"logging",
		"command-line",
		"text"
	],
	"dependencies": {
		"ansi-regex": "^6.2.2"
	},
	"devDependencies": {
		"ava": "^6.4.1",
		"tsd": "^0.33.0",
		"xo": "^1.2.3"
	}
}

```

### File: readme.md
```md
# strip-ansi

> Strip [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) from a string

> [!NOTE]
> Node.js has this built-in now with [`stripVTControlCharacters`](https://nodejs.org/api/util.html#utilstripvtcontrolcharactersstr). The benefit of this package is consistent behavior across Node.js versions and faster improvements. The Node.js version is actually based on this package.

## Install

```sh
npm install strip-ansi
```

## Usage

```js
import stripAnsi from 'strip-ansi';

stripAnsi('\u001B[4mUnicorn\u001B[0m');
//=> 'Unicorn'

stripAnsi('\u001B]8;;https://github.com\u0007Click\u001B]8;;\u0007');
//=> 'Click'
```

## Related

- [strip-ansi-cli](https://github.com/chalk/strip-ansi-cli) - CLI for this module
- [strip-ansi-stream](https://github.com/chalk/strip-ansi-stream) - Streaming version of this module
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)

```

### File: index.d.ts
```ts
/**
Strip [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) from a string.

@example
```
import stripAnsi from 'strip-ansi';

stripAnsi('\u001B[4mUnicorn\u001B[0m');
//=> 'Unicorn'

stripAnsi('\u001B]8;;https://github.com\u0007Click\u001B]8;;\u0007');
//=> 'Click'
```
*/
export default function stripAnsi(string: string): string;

```

### File: index.test-d.ts
```ts
import {expectType} from 'tsd';
import stripAnsi from './index.js';

expectType<string>(stripAnsi('\u001B[4mcake\u001B[0m'));

```

### File: test.js
```js
import test from 'ava';
import stripAnsi from './index.js';

test('strip color from string', t => {
	t.is(stripAnsi('\u001B[0m\u001B[4m\u001B[42m\u001B[31mfoo\u001B[39m\u001B[49m\u001B[24mfoo\u001B[0m'), 'foofoo');
});

test('strip color from ls command', t => {
	t.is(stripAnsi('\u001B[00;38;5;244m\u001B[m\u001B[00;38;5;33mfoo\u001B[0m'), 'foo');
});

test('strip reset;setfg;setbg;italics;strike;underline sequence from string', t => {
	t.is(stripAnsi('\u001B[0;33;49;3;9;4mbar\u001B[0m'), 'bar');
});

test('strip link from terminal link', t => {
	t.is(stripAnsi('\u001B]8;;https://github.com\u0007click\u001B]8;;\u0007'), 'click');
});

test('strip OSC sequence with BEL terminator', t => {
	const input = '\u001B[2J\u001B[m\u001B[HABC\r\n\u001B]0;C:\\WINDOWS\\system32\\cmd.exe\u0007\u001B[?25h';
	const output = stripAnsi(input);
	t.is(output, 'ABC\r\n');
});

test('strip color from string using 8-bit CSI introducer', t => {
	t.is(stripAnsi('\u009B31mfoo\u009B39m'), 'foo');
});

test('return string as-is if no ANSI codes', t => {
	t.is(stripAnsi('foo bar'), 'foo bar');
});

test('return empty string as-is', t => {
	t.is(stripAnsi(''), '');
});

```

### File: .github\security.md
```md
# Security Policy

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security). Tidelift will coordinate the fix and disclosure.

```

