---
id: github.com-chalk-ansi-regex-615973ec-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:36.972823
---

# KNOWLEDGE EXTRACT: github.com_chalk_ansi-regex_615973ec
> **Extracted on:** 2026-04-01 15:23:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524489/github.com_chalk_ansi-regex_615973ec

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
	Match only the first ANSI escape.

	@default false
	*/
	readonly onlyFirst: boolean;
};

/**
Regular expression for matching ANSI escape codes.

@example
```
import ansiRegex from 'ansi-regex';

ansiRegex().test('\u001B[4mcake\u001B[0m');
//=> true

ansiRegex().test('cake');
//=> false

'\u001B[4mcake\u001B[0m'.match(ansiRegex());
//=> ['\u001B[4m', '\u001B[0m']

'\u001B[4mcake\u001B[0m'.match(ansiRegex({onlyFirst: true}));
//=> ['\u001B[4m']

'\u001B]8;;https://github.com\u0007click\u001B]8;;\u0007'.match(ansiRegex());
//=> ['\u001B]8;;https://github.com\u0007', '\u001B]8;;\u0007']
```
*/
export default function ansiRegex(options?: Options): RegExp;
```

## File: `index.js`
```javascript
export default function ansiRegex({onlyFirst = false} = {}) {
	// Valid string terminator sequences are BEL, ESC\, and 0x9c
	const ST = '(?:\\u0007|\\u001B\\u005C|\\u009C)';

	// OSC sequences only: ESC ] ... ST (non-greedy until the first ST)
	const osc = `(?:\\u001B\\][\\s\\S]*?${ST})`;

	// CSI and related: ESC/C1, optional intermediates, optional params (supports ; and :) then final byte
	const csi = '[\\u001B\\u009B][[\\]()#;?]*(?:\\d{1,4}(?:[;:]\\d{0,4})*)?[\\dA-PR-TZcf-nq-uy=><~]';

	const pattern = `${osc}|${csi}`;

	return new RegExp(pattern, onlyFirst ? undefined : 'g');
}
```

## File: `index.test-d.ts`
```typescript
import {expectType} from 'tsd';
import ansiRegex from './index.js';

expectType<RegExp>(ansiRegex());
expectType<RegExp>(ansiRegex({onlyFirst: true}));
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
	"name": "ansi-regex",
	"version": "6.2.2",
	"description": "Regular expression for matching ANSI escape codes",
	"license": "MIT",
	"repository": "chalk/ansi-regex",
	"funding": "https://github.com/chalk/ansi-regex?sponsor=1",
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
		"test": "xo && ava && tsd",
		"view-supported": "node fixtures/view-codes.js"
	},
	"files": [
		"index.js",
		"index.d.ts"
	],
	"keywords": [
		"ansi",
		"styles",
		"color",
		"colour",
		"colors",
		"terminal",
		"console",
		"cli",
		"string",
		"tty",
		"escape",
		"formatting",
		"rgb",
		"256",
		"shell",
		"xterm",
		"command-line",
		"text",
		"regex",
		"regexp",
		"re",
		"match",
		"test",
		"find",
		"pattern"
	],
	"devDependencies": {
		"ansi-escapes": "^5.0.0",
		"ava": "^3.15.0",
		"tsd": "^0.21.0",
		"xo": "^0.54.2"
	}
}
```

## File: `readme.md`
```markdown
# ansi-regex

> Regular expression for matching [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code)

## Install

```sh
npm install ansi-regex
```

## Usage

```js
import ansiRegex from 'ansi-regex';

ansiRegex().test('\u001B[4mcake\u001B[0m');
//=> true

ansiRegex().test('cake');
//=> false

'\u001B[4mcake\u001B[0m'.match(ansiRegex());
//=> ['\u001B[4m', '\u001B[0m']

'\u001B[4mcake\u001B[0m'.match(ansiRegex({onlyFirst: true}));
//=> ['\u001B[4m']

'\u001B]8;;https://github.com\u0007click\u001B]8;;\u0007'.match(ansiRegex());
//=> ['\u001B]8;;https://github.com\u0007', '\u001B]8;;\u0007']
```

## API

### ansiRegex(options?)

Returns a regex for matching ANSI escape codes.

#### options

Type: `object`

##### onlyFirst

Type: `boolean`\
Default: `false` *(Matches any ANSI escape codes in a string)*

Match only the first ANSI escape.

## Important

If you run the regex against untrusted user input in a server context, you should [give it a timeout](https://github.com/sindresorhus/super-regex).

**I do not consider [ReDoS](https://blog.yossarian.net/2022/12/28/ReDoS-vulnerabilities-and-misaligned-incentives) a valid vulnerability for this package.**

## FAQ

### Why do you test for codes not in the ECMA 48 standard?

Some of the codes we run as a test are codes that we acquired finding various lists of non-standard or manufacturer specific codes. We test for both standard and non-standard codes, as most of them follow the same or similar format and can be safely matched in strings without the risk of removing actual string content. There are a few non-standard control codes that do not follow the traditional format (i.e. they end in numbers) thus forcing us to exclude them from the test because we cannot reliably match them.

On the historical side, those ECMA standards were established in the early 90's whereas the VT100, for example, was designed in the mid/late 70's. At that point in time, control codes were still pretty ungoverned and engineers used them for a multitude of things, namely to activate hardware ports that may have been proprietary. Somewhere else you see a similar 'anarchy' of codes is in the x86 architecture for processors; there are a ton of "interrupts" that can mean different things on certain brands of processors, most of which have been phased out.

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)
```

## File: `test.js`
```javascript
import test from 'ava';
import ansiEscapes from 'ansi-escapes';
import * as ansiCodes from './fixtures/ansi-codes.js';
import ansiRegex from './index.js';

const consumptionCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890-=[]{};\':"./>?,<\\|';

// Testing against codes found at: http://ascii-table.com/ansi-escape-sequences-vt-100.php
test('match ansi code in a string', t => {
	t.regex('foo\u001B[4mcake\u001B[0m', ansiRegex());
	t.regex('\u001B[4mcake\u001B[0m', ansiRegex());
	t.regex('foo\u001B[4mcake\u001B[0m', ansiRegex());
	t.regex('\u001B[0m\u001B[4m\u001B[42m\u001B[31mfoo\u001B[39m\u001B[49m\u001B[24mfoo\u001B[0m', ansiRegex());
	t.regex('foo\u001B[mfoo', ansiRegex());
});

test('match ansi code from ls command', t => {
	t.regex('\u001B[00;38;5;244m\u001B[m\u001B[00;38;5;33mfoo\u001B[0m', ansiRegex());
});

test('match reset;setfg;setbg;italics;strike;underline sequence in a string', t => {
	t.regex('\u001B[0;33;49;3;9;4mbar\u001B[0m', ansiRegex());
	t.is('foo\u001B[0;33;49;3;9;4mbar'.match(ansiRegex())[0], '\u001B[0;33;49;3;9;4m');
});

test('match clear tabs sequence in a string', t => {
	t.regex('foo\u001B[0gbar', ansiRegex());
	t.is('foo\u001B[0gbar'.match(ansiRegex())[0], '\u001B[0g');
});

test('match clear line from cursor right in a string', t => {
	t.regex('foo\u001B[Kbar', ansiRegex());
	t.is('foo\u001B[Kbar'.match(ansiRegex())[0], '\u001B[K');
});

test('match clear screen in a string', t => {
	t.regex('foo\u001B[2Jbar', ansiRegex());
	t.is('foo\u001B[2Jbar'.match(ansiRegex())[0], '\u001B[2J');
});

test('match only first', t => {
	t.is('foo\u001B[4mcake\u001B[0m'.match(ansiRegex({onlyFirst: true})).length, 1);
});

test('match terminal link', t => {
	for (const ST of ['\u0007', '\u001B\u005C', '\u009C']) {
		t.regex(`\u001B]8;k=v;https://example-a.com/?a_b=1&c=2#tit%20le${ST}click\u001B]8;;${ST}`, ansiRegex());
		t.regex(`\u001B]8;;mailto:no-replay@mail.com${ST}mail\u001B]8;;${ST}`, ansiRegex());
		t.deepEqual(`\u001B]8;k=v;https://example-a.com/?a_b=1&c=2#tit%20le${ST}click\u001B]8;;${ST}`.match(ansiRegex()), [
			`\u001B]8;k=v;https://example-a.com/?a_b=1&c=2#tit%20le${ST}`,
			`\u001B]8;;${ST}`,
		]);
		t.deepEqual(`\u001B]8;;mailto:no-reply@mail.com${ST}mail-me\u001B]8;;${ST}`.match(ansiRegex()), [
			`\u001B]8;;mailto:no-reply@mail.com${ST}`,
			`\u001B]8;;${ST}`,
		]);
	}
});

test('match terminal link with plus in URL', t => {
	for (const ST of ['\u0007', '\u001B\u005C', '\u009C']) {
		const seqOpen = `\u001B]8;;https://www.example.com/?q=hello+world${ST}`;
		const seqClose = `\u001B]8;;${ST}`;
		const value = `${seqOpen}hello${seqClose}`;
		t.deepEqual(value.match(ansiRegex()), [seqOpen, seqClose]);
		t.is(value.replace(ansiRegex(), ''), 'hello');
	}
});

test('match "change icon name and window title" in string', t => {
	t.is('\u001B]0;sg@tota:~/git/\u0007\u001B[01;32m[sg@tota\u001B[01;37m misc-tests\u001B[01;32m]$'.match(ansiRegex())[0], '\u001B]0;sg@tota:~/git/\u0007');
});

test('match colon-separated sequence arguments', t => {
	t.regex('\u001B[38:2:68:68:68:48:2:0:0:0m', ansiRegex());
	t.is('\u001B[38:2:68:68:68:48:2:0:0:0m'.match(ansiRegex())[0], '\u001B[38:2:68:68:68:48:2:0:0:0m');
});

test('match colon-separated underline variants', t => {
	for (const code of ['\u001B[4:0m', '\u001B[4:1m', '\u001B[4:2m', '\u001B[4:3m', '\u001B[4:4m', '\u001B[4:5m']) {
		t.regex(code, ansiRegex());
		t.is(code.match(ansiRegex())[0], code);
	}
});

test('match colon-separated indexed color (38:5)', t => {
	const code = '\u001B[38:5:123m';
	t.regex(code, ansiRegex());
	t.is(code.match(ansiRegex())[0], code);
});

test('match colon-separated indexed background color (48:5)', t => {
	const code = '\u001B[48:5:200m';
	t.regex(code, ansiRegex());
	t.is(code.match(ansiRegex())[0], code);
});

test('match colon-separated underline color palette index (58:5)', t => {
	const code = '\u001B[58:5:200m';
	t.regex(code, ansiRegex());
	t.is(code.match(ansiRegex())[0], code);
});

test('match colon-separated RGB colors (38:2::R:G:B and 48:2::R:G:B)', t => {
	for (const code of ['\u001B[38:2::12:34:56m', '\u001B[48:2::200:201:202m']) {
		t.regex(code, ansiRegex());
		t.is(code.match(ansiRegex())[0], code);
	}
});

test('match colon-separated underline color RGB (58:2::R:G:B)', t => {
	const code = '\u001B[58:2::255:0:0m';
	t.regex(code, ansiRegex());
	t.is(code.match(ansiRegex())[0], code);
});

test('match colon-separated RGBA foreground/background (38:6, 48:6)', t => {
	for (const code of ['\u001B[38:6::255:0:0:128m', '\u001B[48:6::0:0:0:64m']) {
		t.regex(code, ansiRegex());
		t.is(code.match(ansiRegex())[0], code);
	}
});

test('colon-separated sequences should not overconsume', t => {
	const samples = [
		'\u001B[4:5mX',
		'\u001B[38:5:123mX',
		'\u001B[58:2::255:0:0mX',
		'\u001B[38:2::12:34:56mX',
		'\u001B[48:2::200:201:202mX',
	];

	for (const inputString of samples) {
		const match = inputString.match(ansiRegex())[0];
		t.truthy(match);
		t.is(inputString.replace(ansiRegex(), ''), 'X');
	}
});

test('does not match bracketed text without ESC', t => {
	const samples = [
		'[38:2:68:68:68m',
		'[4:5m',
		'some [0m text',
		'plain [58:2::255:0:0m words',
	];
	for (const inputString of samples) {
		t.is(inputString.match(ansiRegex()), null);
	}
});

test('does not match incomplete CSI', t => {
	const inputString = '\u001B[';
	t.is(inputString.match(ansiRegex()), null);
});

test('does not match ESC followed by unsupported final', t => {
	const inputString = 'pre\u001B`post';
	t.is(inputString.match(ansiRegex()), null);
});

// Testing against extended codes (excluding codes ending in 0-9)
for (const [codeSetKey, codeSetValue] of Object.entries(ansiCodes)) {
	for (const [code, codeInfo] of codeSetValue) {
		const shouldSkip = /\d$/.test(code);
		const skipText = shouldSkip ? '[SKIP] ' : '';
		const ecode = `\u001B${code}`;

		test(`${codeSetKey} - ${skipText}${code} → ${codeInfo[0]}`, t => {
			if (shouldSkip) {
				t.pass();
				return;
			}

			const string = `hel${ecode}lo`;
			t.regex(string, ansiRegex());
			t.is(string.match(ansiRegex())[0], ecode);
			t.is(string.replace(ansiRegex(), ''), 'hello');
		});

		test(`${codeSetKey} - ${skipText}${code} should not overconsume`, t => {
			if (shouldSkip) {
				t.pass();
				return;
			}

			for (const character of consumptionCharacters) {
				const string = ecode + character;
				t.regex(string, ansiRegex());
				t.is(string.match(ansiRegex())[0], ecode);
				t.is(string.replace(ansiRegex(), ''), character);
			}
		});
	}
}

const escapeCodeFunctionArguments = [1, 2];
const escapeCodeIgnoresList = new Set(['beep', 'image', 'iTerm']);
const escapeCodeResultMap = new Map([['link', escapeCodeFunctionArguments[0]]]);

for (const [key, escapeCode] of Object.entries(ansiEscapes)) {
	if (escapeCodeIgnoresList.has(key)) {
		continue;
	}

	const escapeCodeValue = typeof escapeCode === 'function'
		? escapeCode(...escapeCodeFunctionArguments)
		: escapeCode;

	test(`ansi-escapes ${key}`, t => {
		for (const character of consumptionCharacters) {
			const string = escapeCodeValue + character;
			const result = (escapeCodeResultMap.get(key) || '') + character;

			t.is(string.replace(ansiRegex(), ''), result);
		}
	});
}
```

## File: `fixtures/ansi-codes.js`
```javascript
// From http://www.umich.edu/~archive/apple2/misc/programmers/vt100.codes.txt
export const vt52Codes = new Map([
	['A', ['Cursor up']],
	['B', ['Cursor down']],
	['C', ['Cursor right']],
	['D', ['Cursor left']],
	['H', ['Cursor to home']],
	['I', ['Reverse line feed']],
	['J', ['Erase to end of screen']],
	['K', ['Erase to end of line']],
	['S', ['Scroll up']],
	['T', ['Scroll down']],
	['Z', ['Identify']],
	['=', ['Enter alternate keypad mode']],
	['>', ['Exit alternate keypad mode']],
	['1', ['Graphics processor on']],
	['2', ['Graphics processor off']],
	['<', ['Enter ANSI mode']],
	['s', ['Cursor save']],
	['u', ['Cursor restore']],
]);

// From https://espterm.github.io/brain/knowledge/docs_legacy/VT100%20escape%20codes.html
export const ansiCompatible = new Map([
	['[176A', ['Cursor up Pn lines']],
	['[176B', ['Cursor down Pn lines']],
	['[176C', ['Cursor forward Pn characters (right)']],
	['[176D', ['Cursor backward Pn characters (left)']],
	['[176;176H', ['Direct cursor addressing, where Pl is line#, Pc is column#']],
	['[176;176f', ['Direct cursor addressing, where Pl is line#, Pc is column#']],

	['7', ['Save cursor and attributes']],
	['8', ['Restore cursor and attributes']],

	['#3', ['Change this line to double-height top half']],
	['#4', ['Change this line to double-height bottom half']],
	['#5', ['Change this line to single-width single-height']],
	['#6', ['Change this line to double-width single-height']],

	['[176;176;176;176;176;176;176m', ['Text Styles']],
	['[176;176;176;176;176;176;176q', ['Programmable LEDs']],

	['[K', ['Erase from cursor to end of line']],
	['[0K', ['Same']],
	['[1K', ['Erase from beginning of line to cursor']],
	['[2K', ['Erase line containing cursor']],
	['[J', ['Erase from cursor to end of screen']],
	['[0J', ['Same']],
	['[2J', ['Erase entire screen']],
	['[P', ['Delete character']],
	['[0P', ['Delete character (0P)']],
	['[2P', ['Delete 2 characters']],

	['(A', ['United Kingdom (UK) (Character Set G0)']],
	[')A', ['United Kingdom (UK) (Character Set G1)']],
	['(B', ['United States (USASCII) (Character Set G0)']],
	[')B', ['United States (USASCII) (Character Set G1)']],
	['(0', ['Special graphics/line drawing set (Character Set G0)']],
	[')0', ['Special graphics/line drawing set (Character Set G1)']],
	['(1', ['Alternative character ROM (Character Set G0)']],
	[')1', ['Alternative character ROM (Character Set G1)']],
	['(2', ['Alternative graphic ROM (Character Set G0)']],
	[')2', ['Alternative graphic ROM (Character Set G1)']],

	['H', ['Set tab at current column']],
	['[g', ['Clear tab at current column']],
	['[0g', ['Same']],
	['[3g', ['Clear all tabs']],

	['[6n', ['Cursor position report']],
	['[176;176R', ['(response; Pl=line#; Pc=column#)']],
	['[5n', ['Status report']],
	['[c', ['(response; terminal Ok)']],
	['[0c', ['(response; teminal not Ok)']],
	['[?1;176c', ['response; where Ps is option present:']],

	['c', ['Causes power-up reset routine to be executed']],
	['#8', ['Fill screen with "E"']],
	['[2;176y', ['Invoke Test(s), where Ps is a decimal computed by adding the numbers of the desired tests to be executed']],
]);

// From http://ascii-table.com/ansi-escape-sequences-vt-100.php
export const commonCodes = new Map([
	['[176A', ['Move cursor up n lines', 'CUU']],
	['[176B', ['Move cursor down n lines', 'CUD']],
	['[176C', ['Move cursor right n lines', 'CUF']],
	['[176D', ['Move cursor left n lines', 'CUB']],
	['[176;176H', ['Move cursor to screen location v,h', 'CUP']],
	['[176;176f', ['Move cursor to screen location v,h', 'CUP']],
	['[176;176r', ['Set top and bottom lines of a window', 'DECSTBM']],
	['[176;176R', ['Response: cursor is at v,h', 'CPR']],

	['[?1;1760c', ['Response: terminal type code n', 'DA']],

	['[20h', ['Set new line mode', 'LMN']],
	['[?1h', ['Set cursor key to application', 'DECCKM']],
	['[?3h', ['Set number of columns to 132', 'DECCOLM']],
	['[?4h', ['Set smooth scrolling', 'DECSCLM']],
	['[?5h', ['Set reverse video on screen', 'DECSCNM']],
	['[?6h', ['Set origin to relative', 'DECOM']],
	['[?7h', ['Set auto-wrap mode', 'DECAWM']],
	['[?8h', ['Set auto-repeat mode', 'DECARM']],
	['[?9h', ['Set interlacing mode', 'DECINLM']],
	['[20l', ['Set line feed mode', 'LMN']],
	['[?1l', ['Set cursor key to cursor', 'DECCKM']],
	['[?2l', ['Set VT52 (versus ANSI)', 'DECANM']],
	['[?3l', ['Set number of columns to 80', 'DECCOLM']],
	['[?4l', ['Set jump scrolling', 'DECSCLM']],
	['[?5l', ['Set normal video on screen', 'DECSCNM']],
	['[?6l', ['Set origin to absolute', 'DECOM']],
	['[?7l', ['Reset auto-wrap mode', 'DECAWM']],
	['[?8l', ['Reset auto-repeat mode', 'DECARM']],
	['[?9l', ['Reset interlacing mode', 'DECINLM']],

	['N', ['Set single shift 2', 'SS2']],
	['O', ['Set single shift 3', 'SS3']],

	['[m', ['Turn off character attributes', 'SGR0']],
	['[0m', ['Turn off character attributes', 'SGR0']],
	['[1m', ['Turn bold mode on', 'SGR1']],
	['[2m', ['Turn low intensity mode on', 'SGR2']],
	['[4m', ['Turn underline mode on', 'SGR4']],
	['[5m', ['Turn blinking mode on', 'SGR5']],
	['[7m', ['Turn reverse video on', 'SGR7']],
	['[8m', ['Turn invisible text mode on', 'SGR8']],

	['[9m', ['strikethrough on', '--']],
	['[22m', ['bold off (see below)', '--']],
	['[23m', ['italics off', '--']],
	['[24m', ['underline off', '--']],
	['[27m', ['inverse off', '--']],
	['[29m', ['strikethrough off', '--']],
	['[30m', ['set foreground color to black', '--']],
	['[31m', ['set foreground color to red', '--']],
	['[32m', ['set foreground color to green', '--']],
	['[33m', ['set foreground color to yellow', '--']],
	['[34m', ['set foreground color to blue', '--']],
	['[35m', ['set foreground color to magenta (purple)', '--']],
	['[36m', ['set foreground color to cyan', '--']],
	['[37m', ['set foreground color to white', '--']],
	['[39m', ['set foreground color to default (white)', '--']],
	['[40m', ['set background color to black', '--']],
	['[41m', ['set background color to red', '--']],
	['[42m', ['set background color to green', '--']],
	['[43m', ['set background color to yellow', '--']],
	['[44m', ['set background color to blue', '--']],
	['[45m', ['set background color to magenta (purple)', '--']],
	['[46m', ['set background color to cyan', '--']],
	['[47m', ['set background color to white', '--']],
	['[49m', ['set background color to default (black)', '--']],

	['[H', ['Move cursor to upper left corner', 'cursorhome']],
	['[;H', ['Move cursor to upper left corner', 'cursorhome']],
	['[f', ['Move cursor to upper left corner', 'hvhome']],
	['[;f', ['Move cursor to upper left corner', 'hvhome']],
	['M', ['Move/scroll window down one line', 'RI']],
	['E', ['Move to next line', 'NEL']],

	['H', ['Set a tab at the current column', 'HTS']],
	['[g', ['Clear a tab at the current column', 'TBC']],
	['[0g', ['Clear a tab at the current column', 'TBC']],
	['[3g', ['Clear all tabs', 'TBC']],

	['[K', ['Clear line from cursor right', 'EL0']],
	['[0K', ['Clear line from cursor right', 'EL0']],
	['[1K', ['Clear line from cursor left', 'EL1']],
	['[2K', ['Clear entire line', 'EL2']],
	['[J', ['Clear screen from cursor down', 'ED0']],
	['[0J', ['Clear screen from cursor down', 'ED0']],
	['[1J', ['Clear screen from cursor up', 'ED1']],
	['[2J', ['Clear entire screen', 'ED2']],

	['[c', ['Identify what terminal type', 'DA']],
	['[0c', ['Identify what terminal type (another)', 'DA']],
	['c', ['Reset terminal to initial state', 'RIS']],
	['[2;1y', ['Confidence power up test', 'DECTST']],
	['[2;2y', ['Confidence loopback test', 'DECTST']],
	['[2;9y', ['Repeat power up test', 'DECTST']],
	['[2;10y', ['Repeat loopback test', 'DECTST']],
	['[0q', ['Turn off all four leds', 'DECLL0']],
	['[1q', ['Turn on LED #1', 'DECLL1']],
	['[2q', ['Turn on LED #2', 'DECLL2']],
	['[3q', ['Turn on LED #3', 'DECLL3']],
	['[4q', ['Turn on LED #4', 'DECLL4']],
]);

// From http://ascii-table.com/ansi-escape-sequences-vt-100.php
export const otherCode = new Map([
	['7', ['Save cursor position and attributes', 'DECSC']],
	['8', ['Restore cursor position and attributes', 'DECSC']],

	['=', ['Set alternate keypad mode', 'DECKPAM']],
	['>', ['Set numeric keypad mode', 'DECKPNM']],

	['(A', ['Set United Kingdom G0 character set', 'setukg0']],
	[')A', ['Set United Kingdom G1 character set', 'setukg1']],
	['(B', ['Set United States G0 character set', 'setusg0']],
	[')B', ['Set United States G1 character set', 'setusg1']],
	['(0', ['Set G0 special chars. & line set', 'setspecg0']],
	[')0', ['Set G1 special chars. & line set', 'setspecg1']],
	['(1', ['Set G0 alternate character ROM', 'setaltg0']],
	[')1', ['Set G1 alternate character ROM', 'setaltg1']],
	['(2', ['Set G0 alt char ROM and spec. graphics', 'setaltspecg0']],
	[')2', ['Set G1 alt char ROM and spec. graphics', 'setaltspecg1']],

	['#3', ['Double-height letters, top half', 'DECDHL']],
	['#4', ['Double-height letters, bottom half', 'DECDHL']],
	['#5', ['Single width, single height letters', 'DECSWL']],
	['#6', ['Double width, single height letters', 'DECDWL']],
	['#8', ['Screen alignment display', 'DECALN']],

	['5n', ['Device status report', 'DSR']],
	['0n', ['Response: terminal is OK', 'DSR']],
	['3n', ['Response: terminal is not OK', 'DSR']],
	['6n', ['Get cursor position', 'DSR']],
]);

// `urxvt` escapes
export const urxvt = new Map([
	['[5~', ['URxvt.keysym.Prior']],
	['[6~', ['URxvt.keysym.Next']],
	['[7~', ['URxvt.keysym.Home']],
	['[8~', ['URxvt.keysym.End']],
	['[A', ['URxvt.keysym.Up']],
	['[B', ['URxvt.keysym.Down']],
	['[C', ['URxvt.keysym.Right']],
	['[D', ['URxvt.keysym.Left']],
	['[3;5;5t', ['URxvt.keysym.C-M-q']],
	['[3;5;606t', ['URxvt.keysym.C-M-y']],
	['[3;1605;5t', ['URxvt.keysym.C-M-e']],
	['[3;1605;606t', ['URxvt.keysym.C-M-c']],
	[']710;9x15bold\u0007', ['URxvt.keysym.font']],
]);
```

## File: `fixtures/view-codes.js`
```javascript
import process from 'node:process';
import ansiRegex from '../index.js';
import ansiCodes from './ansi-codes.js';

const allCodes = {};
const supported = [];
const unsupported = [];

function addCodesToTest(codes) {
	for (const [key, value] of Object.entries(codes)) {
		allCodes[key] = value;
	}
}

function identifySupportedCodes() {
	let codeSupport = {};

	for (const [code, value] of Object.keys(allCodes)) {
		codeSupport = {
			code,
			matches: `\u001B${code}`.match(ansiRegex()),
			description: value[0],
		};

		if (codeSupport.matches !== null && codeSupport.matches[0] === `\u001B${code}`) {
			supported.push(codeSupport);
		} else {
			unsupported.push(codeSupport);
		}
	}
}

function displaySupport() {
	process.stdout.write('\u001B[32m');

	console.log('SUPPORTED');
	for (const element of supported) {
		console.log(element);
	}

	process.stdout.write('\u001B[31m');
	console.log('UNSUPPORTED');

	for (const element of unsupported) {
		console.log(element);
	}

	process.stdout.write('\u001B[0m');
}

addCodesToTest(ansiCodes.vt52Codes);
addCodesToTest(ansiCodes.ansiCompatible);
addCodesToTest(ansiCodes.commonCodes);
addCodesToTest(ansiCodes.otherCodes);

identifySupportedCodes();
displaySupport();
```

