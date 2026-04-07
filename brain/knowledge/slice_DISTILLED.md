---
id: slice
type: knowledge
owner: OA_Triage
---
# slice
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
import tokenizeAnsi from './tokenize-ansi.js';

function applySgrFragments(activeStyles, fragments) {
	for (const fragment of fragments) {
		switch (fragment.type) {
			case 'reset': {
				activeStyles.clear();
				break;
			}

			case 'end': {
				activeStyles.delete(fragment.endCode);
				break;
			}

			case 'start': {
				activeStyles.delete(fragment.endCode);
				activeStyles.set(fragment.endCode, fragment.code);
				break;
			}

			default: {
				break;
			}
		}
	}

	return activeStyles;
}

function undoAnsiCodes(activeStyles) {
	return [...activeStyles.keys()].reverse().join('');
}

function closeHyperlink(hyperlinkToken) {
	return `${hyperlinkToken.closePrefix}${hyperlinkToken.terminator}`;
}

function shouldIncludeSgrAfterEnd(token, activeStyles) {
	let hasStartFragment = false;
	let hasClosingEffect = false;

	for (const fragment of token.fragments) {
		if (fragment.type === 'start') {
			hasStartFragment = true;
			continue;
		}

		if (fragment.type === 'reset' && activeStyles.size > 0) {
			hasClosingEffect = true;
			continue;
		}

		if (fragment.type === 'end' && activeStyles.has(fragment.endCode)) {
			hasClosingEffect = true;
		}
	}

	return hasClosingEffect && !hasStartFragment;
}

function applySgrToken({token, isPastEnd, activeStyles, returnValue, include, activeHyperlink, position}) {
	if (isPastEnd && !shouldIncludeSgrAfterEnd(token, activeStyles)) {
		return {
			activeStyles,
			activeHyperlink,
			position,
			returnValue,
			include,
		};
	}

	activeStyles = applySgrFragments(activeStyles, token.fragments);
	if (include) {
		returnValue += token.code;
	}

	return {
		activeStyles,
		activeHyperlink,
		position,
		returnValue,
		include,
	};
}

function applyHyperlinkToken({token, isPastEnd, activeStyles, activeHyperlink, position, returnValue, include}) {
	if (
		isPastEnd
		&& (
			token.action !== 'close'
			|| !activeHyperlink
		)
	) {
		return {
			activeStyles,
			activeHyperlink,
			position,
			returnValue,
			include,
		};
	}

	if (token.action === 'open') {
		activeHyperlink = token;
	} else if (token.action === 'close') {
		activeHyperlink = undefined;
	}

	if (include) {
		returnValue += token.code;
	}

	return {
		activeStyles,
		activeHyperlink,
		position,
		returnValue,
		include,
	};
}

function applyControlToken({token, isPastEnd, activeStyles, activeHyperlink, position, returnValue, include}) {
	if (!isPastEnd && include) {
		returnValue += token.code;
	}

	return {
		activeStyles,
		activeHyperlink,
		position,
		returnValue,
		include,
	};
}

function applyCharacterToken({token, start, activeStyles, activeHyperlink, position, returnValue, include}) {
	if (
		!include
		&& position >= start
		&& !token.isGraphemeContinuation
	) {
		include = true;
		returnValue = [...activeStyles.values()].join('');
		if (activeHyperlink) {
			returnValue += activeHyperlink.code;
		}
	}

	if (include) {
		returnValue += token.value;
	}

	position += token.visibleWidth;
	return {
		activeStyles,
		activeHyperlink,
		position,
		returnValue,
		include,
	};
}

const tokenHandlers = {
	sgr: applySgrToken,
	hyperlink: applyHyperlinkToken,
	control: applyControlToken,
	character: applyCharacterToken,
};

function applyToken(parameters) {
	const tokenHandler = tokenHandlers[parameters.token.type];
	if (!tokenHandler) {
		const {
			activeStyles,
			activeHyperlink,
			position,
			returnValue,
			include,
		} = parameters;

		return {
			activeStyles,
			activeHyperlink,
			position,
			returnValue,
			include,
		};
	}

	return tokenHandler(parameters);
}

function createHasContinuationAheadMap(tokens) {
	const hasContinuationAhead = Array.from({length: tokens.length}, () => false);
	let nextCharacterIsContinuation = false;

	for (let tokenIndex = tokens.length - 1; tokenIndex >= 0; tokenIndex--) {
		const token = tokens[tokenIndex];
		hasContinuationAhead[tokenIndex] = nextCharacterIsContinuation;
		if (token.type === 'character') {
			nextCharacterIsContinuation = Boolean(token.isGraphemeContinuation);
		}
	}

	return hasContinuationAhead;
}

export default function sliceAnsi(string, start, end) {
	const tokens = tokenizeAnsi(string, {endCharacter: end});
	const hasContinuationAhead = createHasContinuationAheadMap(tokens);
	let activeStyles = new Map();
	let activeHyperlink;
	let position = 0;
	let returnValue = '';
	let include = false;

	for (const [tokenIndex, token] of tokens.entries()) {
		let isPastEnd = end !== undefined && position >= end;
		if (
			isPastEnd
			&& token.type !== 'character'
			&& hasContinuationAhead[tokenIndex]
		) {
			isPastEnd = false;
		}

		if (
			isPastEnd
			&& token.type === 'character'
			&& !token.isGraphemeContinuation
		) {
			break;
		}

		({activeStyles, activeHyperlink, position, returnValue, include} = applyToken({
			token,
			isPastEnd,
			start,
			activeStyles,
			activeHyperlink,
			position,
			returnValue,
			include,
		}));
	}

	if (!include) {
		return '';
	}

	if (activeHyperlink) {
		returnValue += closeHyperlink(activeHyperlink);
	}

	// Disable active codes at the end
	returnValue += undoAnsiCodes(activeStyles);

	return returnValue;
}

```

### File: package.json
```json
{
	"name": "slice-ansi",
	"version": "8.0.0",
	"description": "Slice a string with ANSI escape codes",
	"license": "MIT",
	"repository": "chalk/slice-ansi",
	"funding": "https://github.com/chalk/slice-ansi?sponsor=1",
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
		"test": "xo && ava && tsc --lib esnext index.d.ts"
	},
	"files": [
		"index.js",
		"tokenize-ansi.js",
		"index.d.ts"
	],
	"keywords": [
		"slice",
		"string",
		"ansi",
		"styles",
		"color",
		"colour",
		"colors",
		"terminal",
		"console",
		"cli",
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
		"ansi-styles": "^6.2.3",
		"is-fullwidth-code-point": "^5.1.0"
	},
	"devDependencies": {
		"ava": "^6.4.1",
		"chalk": "^5.6.2",
		"random-item": "^4.0.1",
		"strip-ansi": "^7.1.2",
		"xo": "^1.2.3"
	}
}

```

### File: readme.md
```md
# slice-ansi [![XO: Linted](https://img.shields.io/badge/xo-linted-blue.svg)](https://github.com/xojs/xo)

> Slice a string with [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles)

## Install

```sh
npm install slice-ansi
```

## Usage

```js
import chalk from 'chalk';
import sliceAnsi from 'slice-ansi';

const string = 'The quick brown ' + chalk.red('fox jumped over ') +
	'the lazy ' + chalk.green('dog and then ran away with the unicorn.');

console.log(sliceAnsi(string, 20, 30));
```

## API

### sliceAnsi(string, startSlice, endSlice?)

#### string

Type: `string`

String with ANSI escape codes. Like one styled by [`chalk`](https://github.com/chalk/chalk).

#### startSlice

Type: `number`

Zero-based visible-column index at which to start the slice. Grapheme clusters (for example, emoji sequences and combining marks) are kept intact.

#### endSlice

Type: `number`

Zero-based visible-column index at which to end the slice.

## Related

- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes
- [cli-truncate](https://github.com/sindresorhus/cli-truncate) - Truncate a string to a specific width in the terminal
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)

```

### File: index.d.ts
```ts
/**
Slice a string with [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles)

@param string - A string with ANSI escape codes. Like one styled by [`chalk`](https://github.com/chalk/chalk).
@param startSlice - Zero-based visible-column index at which to start the slice. Grapheme clusters are kept intact.
@param endSlice - Zero-based visible-column index at which to end the slice.

@example
```
import chalk from 'chalk';
import sliceAnsi from 'slice-ansi';

const string = 'The quick brown ' + chalk.red('fox jumped over ') +
	'the lazy ' + chalk.green('dog and then ran away with the unicorn.');

console.log(sliceAnsi(string, 20, 30));
```
*/
export default function sliceAnsi(string: string, startSlice: number, endSlice?: number): string;

```

### File: test.js
```js
import test from 'ava';
import chalk from 'chalk';
import stripAnsi from 'strip-ansi';
import randomItem from 'random-item';
import sliceAnsi from './index.js';

chalk.level = 1;

const fixture = chalk.red('the ') + chalk.green('quick ') + chalk.blue('brown ') + chalk.cyan('fox ') + chalk.yellow('jumped ');
const stripped = stripAnsi(fixture);
const ESCAPE = '\u001B';
const ANSI_BELL = '\u0007';
const ANSI_STRING_TERMINATOR = `${ESCAPE}\\`;
const C1_OSC = '\u009D';
const C1_STRING_TERMINATOR = '\u009C';

function generate(string) {
	const random1 = randomItem(['rock', 'paper', 'scissors']);
	const random2 = randomItem(['blue', 'green', 'yellow', 'red']);
	return `${string}:${chalk[random2](random1)} `;
}

function createHyperlink(text, url, terminator = ANSI_BELL, closeTerminator = terminator) {
	return `${ESCAPE}]8;;${url}${terminator}${text}${ESCAPE}]8;;${closeTerminator}`;
}

function stripOscHyperlinks(string) {
	const hyperlinkPrefixes = [`${ESCAPE}]8;`, `${C1_OSC}8;`];
	let output = '';
	let index = 0;

	while (index < string.length) {
		const hyperlinkPrefix = hyperlinkPrefixes.find(prefix => string.startsWith(prefix, index));
		if (!hyperlinkPrefix) {
			output += string[index];
			index++;
			continue;
		}

		const uriStart = string.indexOf(';', index + hyperlinkPrefix.length);
		if (uriStart === -1) {
			break;
		}

		let sequenceIndex = uriStart + 1;
		while (sequenceIndex < string.length) {
			if (string[sequenceIndex] === ANSI_BELL) {
				index = sequenceIndex + 1;
				break;
			}

			if (
				string[sequenceIndex] === ESCAPE
				&& string[sequenceIndex + 1] === '\\'
			) {
				index = sequenceIndex + 2;
				break;
			}

			if (string[sequenceIndex] === C1_STRING_TERMINATOR) {
				index = sequenceIndex + 1;
				break;
			}

			sequenceIndex++;
		}

		if (sequenceIndex >= string.length) {
			break;
		}
	}

	return output;
}

function stripForVisibleComparison(string) {
	return stripAnsi(stripOscHyperlinks(string));
}

function assertVisibleSliceMatchesNative(t, input, start, end) {
	const nativeSlice = stripForVisibleComparison(input).slice(start, end);
	const ansiSlice = stripForVisibleComparison(sliceAnsi(input, start, end));
	t.is(ansiSlice, nativeSlice);
}

function styleScalarAtIndex(string, scalarIndex, style) {
	let output = '';
	let index = 0;

	for (const scalar of string) {
		output += index === scalarIndex ? style(scalar) : scalar;
		index++;
	}

	return output;
}

function hyperlinkScalarAtIndex(string, scalarIndex, url) {
	let output = '';
	let index = 0;

	for (const scalar of string) {
		output += index === scalarIndex ? createHyperlink(scalar, url) : scalar;
		index++;
	}

	return output;
}

function assertSlicesMatchPlainReference(t, plain, styled, maximumIndex = 6) {
	for (let start = 0; start <= maximumIndex; start++) {
		for (let end = start; end <= maximumIndex; end++) {
			const expected = stripForVisibleComparison(sliceAnsi(plain, start, end));
			const actual = stripForVisibleComparison(sliceAnsi(styled, start, end));
			t.is(actual, expected);
		}
	}
}

function createRandomInteger(maximum) {
	return Math.floor(Math.random() * maximum);
}

function createRandomVisibleText() {
	const parts = ['a', 'b', 'c', ' ', 'ß'];
	const length = createRandomInteger(6) + 1;
	let returnValue = '';

	for (let index = 0; index < length; index++) {
		returnValue += randomItem(parts);
	}

	return returnValue;
}

function createRandomHyperlinkText() {
	const url = `https://example.com/${createRandomInteger(1000)}`;
	const terminator = randomItem([ANSI_BELL, ANSI_STRING_TERMINATOR]);
	return createHyperlink(createRandomVisibleText(), url, terminator);
}

function createRandomStyledText() {
	const text = createRandomVisibleText();
	const style = randomItem([
		chalk.red,
		chalk.green,
		chalk.blue,
		chalk.bold,
		chalk.underline,
		chalk.bgYellow.black,
	]);

	return style(text);
}

function createRandomValidAnsiText() {
	const segmentCount = createRandomInteger(8) + 1;
	let output = '';

	for (let segmentIndex = 0; segmentIndex < segmentCount; segmentIndex++) {
		const type = randomItem(['plain', 'styled', 'hyperlink']);

		if (type === 'plain') {
			output += createRandomVisibleText();
		} else if (type === 'styled') {
			output += createRandomStyledText();
		} else {
			output += createRandomHyperlinkText();
		}
	}

	return output;
}

test('main', t => {
	// The slice should behave exactly as a regular JS slice behaves
	for (let index = 0; index < 20; index++) {
		for (let index2 = 19; index2 > index; index2--) {
			const nativeSlice = stripped.slice(index, index2);
			const ansiSlice = sliceAnsi(fixture, index, index2);
			t.is(nativeSlice, stripAnsi(ansiSlice));
		}
	}

	const a = JSON.stringify('\u001B[31mthe \u001B[39m\u001B[32mquick \u001B[39m');
	const b = JSON.stringify('\u001B[34mbrown \u001B[39m\u001B[36mfox \u001B[39m');
	const c = JSON.stringify('\u001B[31m \u001B[39m\u001B[32mquick \u001B[39m\u001B[34mbrown \u001B[39m\u001B[36mfox \u001B[39m');

	t.is(JSON.stringify(sliceAnsi(fixture, 0, 10)), a);
	t.is(JSON.stringify(sliceAnsi(fixture, 10, 20)), b);
	t.is(JSON.stringify(sliceAnsi(fixture, 3, 20)), c);

	const string = generate(1) + generate(2) + generate(3) + generate(4) + generate(5) + generate(6) + generate(7) + generate(8) + generate(9) + generate(10) + generate(11) + generate(12) + generate(13) + generate(14) + generate(15) + generate(1) + generate(2) + generate(3) + generate(4) + generate(5) + generate(6) + generate(7) + generate(8) + generate(9) + generate(10) + generate(11) + generate(12) + generate(13) + generate(14) + generate(15);
	const native = stripAnsi(string).slice(0, 55);
	const ansi = stripAnsi(sliceAnsi(string, 0, 55));
	t.is(native, ansi);
});

test('supports fullwidth characters', t => {
	t.is(sliceAnsi('안녕하세', 0, 4), '안녕');
});

test('supports unicode surrogate pairs', t => {
	t.is(sliceAnsi('a\uD83C\uDE00BC', 0, 2), 'a\uD83C\uDE00');
});

test('does not split grapheme clusters with combining marks', t => {
	const input = 'Ae\u0301B';
	t.is(sliceAnsi(input, 1, 2), 'e\u0301');
	t.is(sliceAnsi(input, 2, 3), 'B');
});

test('does not split ZWJ emoji grapheme clusters', t => {
	const input = 'A👨‍👩‍👧‍👦B';
	t.is(sliceAnsi(input, 1, 3), '👨‍👩‍👧‍👦');
	t.is(sliceAnsi(input, 3, 4), 'B');
});

test('treats CRLF as a single grapheme cluster', t => {
	const input = 'A\r\nB';
	t.is(sliceAnsi(input, 1, 2), '\r\n');
	t.is(sliceAnsi(input, 2, 3), 'B');
});

test('does not split styled grapheme clusters with combining marks', t => {
	const input = '\u001B[31me\u0301\u001B[39m';
	t.is(sliceAnsi(input, 0, 1), input);
	t.is(sliceAnsi(input, 1, 2), '');
});

test('does not split grapheme clusters when styles appear inside combining sequence', t => {
	const input = '\u001B[31me\u001B[39m\u0301B';
	t.is(stripForVisibleComparison(sliceAnsi(input, 0, 1)), 'e\u0301');
	t.is(stripForVisibleComparison(sliceAnsi(input, 1, 2)), 'B');
});

test('does not split Hangul Jamo grapheme clusters when styles appear inside sequence', t => {
	const input = '\u001B[31mᄀ\u001B[39mᅡB';
	t.is(stripForVisibleComparison(sliceAnsi(input, 0, 2)), '가');
	t.is(stripForVisibleComparison(sliceAnsi(input, 2, 3)), 'B');
});

test('keeps style opens inside grapheme continuation past end boundary', t => {
	const input = `e${chalk.red('\u0301')}B`;
	t.is(sliceAnsi(input, 0, 1), `e${chalk.red('\u0301')}`);
});

test('keeps hyperlink opens inside grapheme continuation past end boundary', t => {
	const open = `${ESCAPE}]8;;https://example.com${ANSI_BELL}`;
	const close = `${ESCAPE}]8;;${ANSI_BELL}`;
	const input = `e${open}\u0301${close}B`;
	t.is(sliceAnsi(input, 0, 1), `e${open}\u0301${close}`);
});

test('doesn\'t add unnecessary escape codes', t => {
	t.is(sliceAnsi('\u001B[31municorn\u001B[39m', 0, 3), '\u001B[31muni\u001B[39m');
});

test('can slice a normal character before a colored character', t => {
	t.is(sliceAnsi('a\u001B[31mb\u001B[39m', 0, 1), 'a');
});

test('can slice a normal character after a colored character', t => {
	t.is(sliceAnsi('\u001B[31ma\u001B[39mb', 1, 2), 'b');
});

// See https://github.com/chalk/slice-ansi/issues/22
test('can slice a string styled with both background and foreground', t => {
	// Test string: `chalk.bgGreen.black('test');`
	t.is(sliceAnsi('\u001B[42m\u001B[30mtest\u001B[39m\u001B[49m', 0, 1), '\u001B[42m\u001B[30mt\u001B[39m\u001B[49m');
});

test('can slice a string styled with modifier', t => {
	// Test string: `chalk.underline('test');`
	t.is(sliceAnsi('\u001B[4mtest\u001B[24m', 0, 1), '\u001B[4mt\u001B[24m');
});

test('can slice a string with unknown ANSI color', t => {
	t.is(sliceAnsi('\u001B[20mTEST\u001B[49m', 0, 4), '\u001B[20mTEST\u001B[0m');
	t.is(sliceAnsi('\u001B[1001mTEST\u001B[49m', 0, 3), '\u001B[1001mTES\u001B[0m');
	t.is(sliceAnsi('\u001B[1001mTEST\u001B[49m', 0, 2), '\u001B[1001mTE\u001B[0m');
});

test('weird null issue', t => {
	const s = '\u001B[1mautotune.flipCoin("easy as") ? 🎂 : 🍰 \u001B[33m★\u001B[39m\u001B[22m';
	const result = sliceAnsi(s, 38);
	t.false(result.includes('null'));
});

test('supports true color escape sequences', t => {
	t.is(sliceAnsi('\u001B[1m\u001B[48;2;255;255;255m\u001B[38;2;255;0;0municorn\u001B[39m\u001B[49m\u001B[22m', 0, 3), '\u001B[1m\u001B[48;2;255;255;255m\u001B[38;2;255;0;0muni\u001B[39m\u001B[49m\u001B[22m');
});

test('supports colon-delimited truecolor SGR syntax', t => {
	t.is(sliceAnsi('\u001B[38:2:255:0:0mred\u001B[39m', 0, 1), '\u001B[38:2:255:0:0mr\u001B[39m');
});

// See https://github.com/chalk/slice-ansi/issues/24
test('doesn\'t add extra escapes', t => {
	const output = `${chalk.black.bgYellow(' RUNS ')}  ${chalk.green('test')}`;
	t.is(sliceAnsi(output, 0, 7), `${chalk.black.bgYellow(' RUNS ')} `);
	t.is(sliceAnsi(output, 0, 8), `${chalk.black.bgYellow(' RUNS ')}  `);
	t.is(JSON.stringify(sliceAnsi('\u001B[31m' + output, 0, 4)), JSON.stringify(chalk.black.bgYellow(' RUN')));
});

// See https://github.com/chalk/slice-ansi/issues/26
test('does not lose fullwidth characters', t => {
	t.is(sliceAnsi('古古test', 0), '古古test');
});

test('does not split regional-indicator flag graphemes', t => {
	const input = 'A🇮🇱B';
	t.is(sliceAnsi(input, 1, 2), '🇮🇱');
	t.is(sliceAnsi(input, 2, 3), '');
});

test('does not split styled regional-indicator flag graphemes', t => {
	const input = '\u001B[31m🇮🇱\u001B[39m';
	t.is(sliceAnsi(input, 0, 1), input);
	t.is(sliceAnsi(input, 1, 2), '');
});

test('counts emoji-style graphemes as fullwidth', t => {
	t.is(sliceAnsi('A☺️B', 1, 3), '☺️');
	t.is(sliceAnsi('A1️⃣B', 1, 3), '1️⃣');
	t.is(sliceAnsi('A🇦B', 1, 3), '🇦');
});

test('does not treat text-presentation pictographs as fullwidth', t => {
	t.is(sliceAnsi('A☺B', 2, 3), 'B');
	t.is(sliceAnsi('A☂B', 2, 3), 'B');
});

test('can create empty slices', t => {
	t.is(sliceAnsi('test', 0, 0), '');
});

test('slice links (issue #31)', t => {
	const link = createHyperlink('Google', 'https://google.com');
	t.is(sliceAnsi(link, 0, 6), link);
});

test('supports OSC 8 hyperlinks with ST terminator', t => {
	const link = createHyperlink('Google', 'https://google.com', ANSI_STRING_TERMINATOR);
	t.is(sliceAnsi(link, 0, 6), link);
});

test('supports OSC 8 hyperlinks with mixed close terminator', t => {
	const link = createHyperlink('Google', 'https://google.com', ANSI_STRING_TERMINATOR, ANSI_BELL);
	t.is(sliceAnsi(link, 0, 6), link);
});

test('supports OSC 8 hyperlinks with parameters', t => {
	const link = `${ESCAPE}]8;id=abc;https://google.com${ANSI_BELL}Google${ESCAPE}]8;;${ANSI_BELL}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 1, 4), `${ESCAPE}]8;id=abc;https://google.com${ANSI_BELL}oog${ESCAPE}]8;;${ANSI_BELL}`);
});

test('supports OSC 8 hyperlinks with parameters and ST terminator', t => {
	const link = `${ESCAPE}]8;id=abc;https://google.com${ANSI_STRING_TERMINATOR}Google${ESCAPE}]8;;${ANSI_STRING_TERMINATOR}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 2), `${ESCAPE}]8;id=abc;https://google.com${ANSI_STRING_TERMINATOR}ogle${ESCAPE}]8;;${ANSI_STRING_TERMINATOR}`);
});

test('supports ESC OSC 8 hyperlinks with C1 ST terminator', t => {
	const link = `${ESCAPE}]8;;https://google.com${C1_STRING_TERMINATOR}Google${ESCAPE}]8;;${C1_STRING_TERMINATOR}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 1, 4), `${ESCAPE}]8;;https://google.com${C1_STRING_TERMINATOR}oog${ESCAPE}]8;;${C1_STRING_TERMINATOR}`);
});

test('supports C1 OSC 8 hyperlinks with BEL terminator', t => {
	const link = `${C1_OSC}8;;https://google.com${ANSI_BELL}Google${C1_OSC}8;;${ANSI_BELL}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 1, 4), `${C1_OSC}8;;https://google.com${ANSI_BELL}oog${C1_OSC}8;;${ANSI_BELL}`);
});

test('supports C1 OSC 8 hyperlinks with C1 ST terminator', t => {
	const link = `${C1_OSC}8;;https://google.com${C1_STRING_TERMINATOR}Google${C1_OSC}8;;${C1_STRING_TERMINATOR}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 2), `${C1_OSC}8;;https://google.com${C1_STRING_TERMINATOR}ogle${C1_OSC}8;;${C1_STRING_TERMINATOR}`);
});

test('supports C1 OSC 8 hyperlinks with parameters and ESC ST terminator', t => {
	const link = `${C1_OSC}8;id=abc;https://google.com${ANSI_STRING_TERMINATOR}Google${C1_OSC}8;;${ANSI_STRING_TERMINATOR}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 1, 4), `${C1_OSC}8;id=abc;https://google.com${ANSI_STRING_TERMINATOR}oog${C1_OSC}8;;${ANSI_STRING_TERMINATOR}`);
});

test('can slice each visible character from hyperlink', t => {
	const url = 'https://google.com';
	const text = 'Google';
	const link = createHyperlink(text, url);

	for (let index = 0; index < text.length; index++) {
		t.is(sliceAnsi(link, index, index + 1), createHyperlink(text.slice(index, index + 1), url));
	}
});

test('can slice partial hyperlink text', t => {
	const url = 'https://google.com';
	const link = createHyperlink('Google', url);
	t.is(sliceAnsi(link, 1, 4), createHyperlink('oog', url));
});

test('can create an empty slice inside hyperlink text', t => {
	const link = createHyperlink('Google', 'https://google.com');
	t.is(sliceAnsi(link, 2, 2), '');
});

test('keeps outer styles when slicing after hyperlink text', t => {
	const input = chalk.red(`${createHyperlink('AB', 'https://example.com')}C`);
	t.is(sliceAnsi(input, 2, 3), chalk.red('C'));
});

test('supports hyperlinks that close with non-empty parameters', t => {
	const link = `${ESCAPE}]8;id=abc;https://google.com${ANSI_BELL}Google${ESCAPE}]8;id=abc;${ANSI_BELL}`;
	t.is(sliceAnsi(link, 0, 6), link);
	t.is(sliceAnsi(link, 0, 4), `${ESCAPE}]8;id=abc;https://google.com${ANSI_BELL}Goog${ESCAPE}]8;;${ANSI_BELL}`);
});

test('supports hyperlink slices with unicode surrogate pairs', t => {
	const url = 'https://example.com';
	const link = createHyperlink('a🙂b', url);
	t.is(sliceAnsi(link, 1, 3), createHyperlink('🙂', url));
});

test('preserves grapheme clusters when slicing hyperlink text', t => {
	const url = 'https://example.com';
	const link = createHyperlink('A👨‍👩‍👧‍👦B', url);
	t.is(sliceAnsi(link, 1, 3), createHyperlink('👨‍👩‍👧
... [TRUNCATED]
```

### File: tokenize-ansi.js
```js
import ansiStyles from 'ansi-styles';
import isFullwidthCodePoint from 'is-fullwidth-code-point';

const ESCAPE_CODE_POINT = 27;
const C1_DCS_CODE_POINT = 144;
const C1_SOS_CODE_POINT = 152;
const C1_CSI_CODE_POINT = 155;
const C1_ST_CODE_POINT = 156;
const C1_OSC_CODE_POINT = 157;
const C1_PM_CODE_POINT = 158;
const C1_APC_CODE_POINT = 159;
const ESCAPES = new Set([
	ESCAPE_CODE_POINT,
	C1_DCS_CODE_POINT,
	C1_SOS_CODE_POINT,
	C1_CSI_CODE_POINT,
	C1_ST_CODE_POINT,
	C1_OSC_CODE_POINT,
	C1_PM_CODE_POINT,
	C1_APC_CODE_POINT,
]);

const ESCAPE = '\u001B';
const ANSI_BELL = '\u0007';
const ANSI_CSI = '[';
const ANSI_OSC = ']';
const ANSI_DCS = 'P';
const ANSI_SOS = 'X';
const ANSI_PM = '^';
const ANSI_APC = '_';
const ANSI_SGR_TERMINATOR = 'm';
const ANSI_OSC_TERMINATOR = '\\';
const ANSI_STRING_TERMINATOR = `${ESCAPE}${ANSI_OSC_TERMINATOR}`;
const C1_OSC = '\u009D';
const C1_STRING_TERMINATOR = '\u009C';
const ANSI_HYPERLINK_ESC_PREFIX = `${ESCAPE}${ANSI_OSC}8;`;
const ANSI_HYPERLINK_C1_PREFIX = `${C1_OSC}8;`;
const ANSI_HYPERLINK_ESC_CLOSE = `${ANSI_HYPERLINK_ESC_PREFIX};`;
const ANSI_HYPERLINK_C1_CLOSE = `${ANSI_HYPERLINK_C1_PREFIX};`;

const CODE_POINT_0 = '0'.codePointAt(0);
const CODE_POINT_9 = '9'.codePointAt(0);
const CODE_POINT_SEMICOLON = ';'.codePointAt(0);
const CODE_POINT_COLON = ':'.codePointAt(0);
// ECMA-48 CSI format: parameter bytes 0x30-0x3F, intermediates 0x20-0x2F, final 0x40-0x7E.
const CODE_POINT_CSI_PARAMETER_START = '0'.codePointAt(0);
const CODE_POINT_CSI_PARAMETER_END = '?'.codePointAt(0);
const CODE_POINT_CSI_INTERMEDIATE_START = ' '.codePointAt(0);
const CODE_POINT_CSI_INTERMEDIATE_END = '/'.codePointAt(0);
const CODE_POINT_CSI_FINAL_START = '@'.codePointAt(0);
const CODE_POINT_CSI_FINAL_END = '~'.codePointAt(0);
const REGIONAL_INDICATOR_SYMBOL_LETTER_A = 127_462;
const REGIONAL_INDICATOR_SYMBOL_LETTER_Z = 127_487;
const SGR_RESET_CODE = 0;
const SGR_EXTENDED_FOREGROUND_CODE = 38;
const SGR_DEFAULT_FOREGROUND_CODE = 39;
const SGR_EXTENDED_BACKGROUND_CODE = 48;
const SGR_DEFAULT_BACKGROUND_CODE = 49;
const SGR_COLOR_TYPE_ANSI_256 = 5;
const SGR_COLOR_TYPE_TRUECOLOR = 2;
const SGR_ANSI_256_FRAGMENT_LENGTH = 3;
const SGR_TRUECOLOR_FRAGMENT_LENGTH = 5;
const SGR_ANSI_256_LAST_PARAMETER_OFFSET = 2;
const SGR_TRUECOLOR_LAST_PARAMETER_OFFSET = 4;
const VARIATION_SELECTOR_16_CODE_POINT = 65_039;
const COMBINING_ENCLOSING_KEYCAP_CODE_POINT = 8419;
const EMOJI_PRESENTATION_GRAPHEME_REGEX = /\p{Emoji_Presentation}/u;
const GRAPHEME_SEGMENTER = new Intl.Segmenter(undefined, {granularity: 'grapheme'});

const endCodeNumbers = new Set();
for (const [, end] of ansiStyles.codes) {
	endCodeNumbers.add(end);
}

function isSgrParameterCharacter(codePoint) {
	return (
		(codePoint >= CODE_POINT_0 && codePoint <= CODE_POINT_9)
		|| codePoint === CODE_POINT_SEMICOLON
		|| codePoint === CODE_POINT_COLON
	);
}

function isCsiParameterCharacter(codePoint) {
	return codePoint >= CODE_POINT_CSI_PARAMETER_START && codePoint <= CODE_POINT_CSI_PARAMETER_END;
}

function isCsiIntermediateCharacter(codePoint) {
	return codePoint >= CODE_POINT_CSI_INTERMEDIATE_START && codePoint <= CODE_POINT_CSI_INTERMEDIATE_END;
}

function isCsiFinalCharacter(codePoint) {
	return codePoint >= CODE_POINT_CSI_FINAL_START && codePoint <= CODE_POINT_CSI_FINAL_END;
}

function isRegionalIndicatorCodePoint(codePoint) {
	return codePoint >= REGIONAL_INDICATOR_SYMBOL_LETTER_A && codePoint <= REGIONAL_INDICATOR_SYMBOL_LETTER_Z;
}

function createControlParseResult(code, endIndex) {
	return {
		token: {
			type: 'control',
			code,
		},
		endIndex,
	};
}

function isEmojiStyleGrapheme(grapheme) {
	if (EMOJI_PRESENTATION_GRAPHEME_REGEX.test(grapheme)) {
		return true;
	}

	for (const character of grapheme) {
		const codePoint = character.codePointAt(0);
		if (
			codePoint === VARIATION_SELECTOR_16_CODE_POINT
			|| codePoint === COMBINING_ENCLOSING_KEYCAP_CODE_POINT
		) {
			return true;
		}
	}

	return false;
}

function getGraphemeWidth(grapheme) {
	let regionalIndicatorCount = 0;
	for (const character of grapheme) {
		const codePoint = character.codePointAt(0);
		if (isFullwidthCodePoint(codePoint)) {
			return 2;
		}

		if (isRegionalIndicatorCodePoint(codePoint)) {
			regionalIndicatorCount++;
		}
	}

	if (regionalIndicatorCount >= 1) {
		return 2;
	}

	if (isEmojiStyleGrapheme(grapheme)) {
		return 2;
	}

	return 1;
}

function getSgrPrefix(code) {
	if (code.startsWith('\u009B')) {
		return '\u009B';
	}

	return `${ESCAPE}${ANSI_CSI}`;
}

function createSgrCode(prefix, values) {
	return `${prefix}${values.join(';')}${ANSI_SGR_TERMINATOR}`;
}

function getSgrFragments(code) {
	const fragments = [];
	const sgrPrefix = getSgrPrefix(code);
	let parameterString;

	if (code.startsWith(`${ESCAPE}${ANSI_CSI}`)) {
		parameterString = code.slice(2, -1);
	} else if (code.startsWith('\u009B')) {
		parameterString = code.slice(1, -1);
	} else {
		return fragments;
	}

	const rawCodes = parameterString.length === 0 ? [String(SGR_RESET_CODE)] : parameterString.split(';');
	let index = 0;
	while (index < rawCodes.length) {
		const codeNumber = Number.parseInt(rawCodes[index], 10);
		if (Number.isNaN(codeNumber)) {
			index++;
			continue;
		}

		if (codeNumber === SGR_RESET_CODE) {
			fragments.push({type: 'reset'});
			index++;
			continue;
		}

		if (codeNumber === SGR_EXTENDED_FOREGROUND_CODE || codeNumber === SGR_EXTENDED_BACKGROUND_CODE) {
			const colorType = Number.parseInt(rawCodes[index + 1], 10);
			if (colorType === SGR_COLOR_TYPE_ANSI_256 && index + SGR_ANSI_256_LAST_PARAMETER_OFFSET < rawCodes.length) {
				const openCode = createSgrCode(sgrPrefix, rawCodes.slice(index, index + SGR_ANSI_256_FRAGMENT_LENGTH));
				fragments.push({
					type: 'start',
					code: openCode,
					endCode: ansiStyles.color.ansi(codeNumber === SGR_EXTENDED_FOREGROUND_CODE ? SGR_DEFAULT_FOREGROUND_CODE : SGR_DEFAULT_BACKGROUND_CODE),
				});
				index += SGR_ANSI_256_FRAGMENT_LENGTH;
				continue;
			}

			if (colorType === SGR_COLOR_TYPE_TRUECOLOR && index + SGR_TRUECOLOR_LAST_PARAMETER_OFFSET < rawCodes.length) {
				const openCode = createSgrCode(sgrPrefix, rawCodes.slice(index, index + SGR_TRUECOLOR_FRAGMENT_LENGTH));
				fragments.push({
					type: 'start',
					code: openCode,
					endCode: ansiStyles.color.ansi(codeNumber === SGR_EXTENDED_FOREGROUND_CODE ? SGR_DEFAULT_FOREGROUND_CODE : SGR_DEFAULT_BACKGROUND_CODE),
				});
				index += SGR_TRUECOLOR_FRAGMENT_LENGTH;
				continue;
			}

			const openCode = createSgrCode(sgrPrefix, [rawCodes[index]]);
			fragments.push({
				type: 'start',
				code: openCode,
				endCode: ansiStyles.color.ansi(codeNumber === SGR_EXTENDED_FOREGROUND_CODE ? SGR_DEFAULT_FOREGROUND_CODE : SGR_DEFAULT_BACKGROUND_CODE),
			});
			index++;
			continue;
		}

		if (endCodeNumbers.has(codeNumber)) {
			fragments.push({
				type: 'end',
				endCode: ansiStyles.color.ansi(codeNumber),
			});
			index++;
			continue;
		}

		const mappedEndCode = ansiStyles.codes.get(codeNumber);
		if (mappedEndCode !== undefined) {
			const openCode = createSgrCode(sgrPrefix, [rawCodes[index]]);
			fragments.push({
				type: 'start',
				code: openCode,
				endCode: ansiStyles.color.ansi(mappedEndCode),
			});
			index++;
			continue;
		}

		const openCode = createSgrCode(sgrPrefix, [rawCodes[index]]);
		fragments.push({
			type: 'start',
			code: openCode,
			endCode: ansiStyles.reset.open,
		});
		index++;
	}

	if (fragments.length === 0) {
		fragments.push({type: 'reset'});
	}

	return fragments;
}

function parseCsiCode(string, index) {
	const escapeCodePoint = string.codePointAt(index);
	let sequenceStartIndex;

	if (escapeCodePoint === ESCAPE_CODE_POINT) {
		if (string[index + 1] !== ANSI_CSI) {
			return;
		}

		sequenceStartIndex = index + 2;
	} else if (escapeCodePoint === C1_CSI_CODE_POINT) {
		sequenceStartIndex = index + 1;
	} else {
		return;
	}

	let hasCanonicalSgrParameters = true;
	for (let sequenceIndex = sequenceStartIndex; sequenceIndex < string.length; sequenceIndex++) {
		const codePoint = string.codePointAt(sequenceIndex);

		if (isCsiFinalCharacter(codePoint)) {
			const code = string.slice(index, sequenceIndex + 1);
			if (string[sequenceIndex] !== ANSI_SGR_TERMINATOR || !hasCanonicalSgrParameters) {
				return createControlParseResult(code, sequenceIndex + 1);
			}

			return {
				token: {
					type: 'sgr',
					code,
					fragments: getSgrFragments(code),
				},
				endIndex: sequenceIndex + 1,
			};
		}

		if (isCsiParameterCharacter(codePoint)) {
			if (!isSgrParameterCharacter(codePoint)) {
				hasCanonicalSgrParameters = false;
			}

			continue;
		}

		if (isCsiIntermediateCharacter(codePoint)) {
			hasCanonicalSgrParameters = false;
			continue;
		}

		const endIndex = sequenceIndex;
		return createControlParseResult(string.slice(index, endIndex), endIndex);
	}

	return createControlParseResult(string.slice(index), string.length);
}

function parseHyperlinkCode(string, index) {
	let hyperlinkPrefix;
	let hyperlinkClose;
	const codePoint = string.codePointAt(index);

	if (
		codePoint === ESCAPE_CODE_POINT
		&& string.startsWith(ANSI_HYPERLINK_ESC_PREFIX, index)
	) {
		hyperlinkPrefix = ANSI_HYPERLINK_ESC_PREFIX;
		hyperlinkClose = ANSI_HYPERLINK_ESC_CLOSE;
	} else if (
		codePoint === C1_OSC_CODE_POINT
		&& string.startsWith(ANSI_HYPERLINK_C1_PREFIX, index)
	) {
		hyperlinkPrefix = ANSI_HYPERLINK_C1_PREFIX;
		hyperlinkClose = ANSI_HYPERLINK_C1_CLOSE;
	} else {
		return;
	}

	const uriStart = string.indexOf(';', index + hyperlinkPrefix.length);
	if (uriStart === -1) {
		return createControlParseResult(string.slice(index), string.length);
	}

	for (let sequenceIndex = uriStart + 1; sequenceIndex < string.length; sequenceIndex++) {
		const character = string[sequenceIndex];

		if (character === ANSI_BELL) {
			const code = string.slice(index, sequenceIndex + 1);
			const action = sequenceIndex === uriStart + 1 ? 'close' : 'open';
			return {
				token: {
					type: 'hyperlink',
					code,
					action,
					closePrefix: hyperlinkClose,
					terminator: ANSI_BELL,
				},
				endIndex: sequenceIndex + 1,
			};
		}

		if (
			character === ESCAPE
			&& string[sequenceIndex + 1] === ANSI_OSC_TERMINATOR
		) {
			const code = string.slice(index, sequenceIndex + 2);
			const action = sequenceIndex === uriStart + 1 ? 'close' : 'open';
			return {
				token: {
					type: 'hyperlink',
					code,
					action,
					closePrefix: hyperlinkClose,
					terminator: ANSI_STRING_TERMINATOR,
				},
				endIndex: sequenceIndex + 2,
			};
		}

		if (character === C1_STRING_TERMINATOR) {
			const code = string.slice(index, sequenceIndex + 1);
			const action = sequenceIndex === uriStart + 1 ? 'close' : 'open';
			return {
				token: {
					type: 'hyperlink',
					code,
					action,
					closePrefix: hyperlinkClose,
					terminator: C1_STRING_TERMINATOR,
				},
				endIndex: sequenceIndex + 1,
			};
		}
	}

	return createControlParseResult(string.slice(index), string.length);
}

function parseControlStringCode(string, index) {
	const codePoint = string.codePointAt(index);
	let sequenceStartIndex;
	let supportsBellTerminator = false;

	switch (codePoint) {
		case ESCAPE_CODE_POINT: {
			const command = string[index + 1];
			switch (command) {
				case ANSI_OSC: {
					// OSC accepts ST (ECMA-48) and BEL (xterm compatibility extension).
					sequenceStartIndex = index + 2;
					supportsBellTerminator = true;
					break;
				}

				case ANSI_DCS:
				case ANSI_SOS:
				case ANSI_PM:
				case ANSI_APC: {
					sequenceStartIndex = index + 2;
					break;
				}

				case ANSI_OSC_TERMINATOR: {
					return createControlParseResult(ANSI_STRING_TERMINATOR, index + 2);
				}

				default: {
					return;
				}
			}

			break;
		}

		case C1_OSC_CODE_POINT: {
			sequenceStartIndex = index + 1;
			supportsBellTerminator = true;
			break;
		}

		case C1_DCS_CODE_POINT:
		case C1_SOS_CODE_POINT:
		case C1_PM_CODE_POINT:
		case C1_APC_CODE_POINT: {
			sequenceStartIndex = index + 1;
			break;
		}

		case C1_ST_CODE_POINT: {
			return createControlParseResult(C1_STRING_TERMINATOR, index + 1);
		}

		default: {
			return;
		}
	}

	for (let sequenceIndex = sequenceStartIndex; sequenceIndex < string.length; sequenceIndex++) {
		if (supportsBellTerminator && string[sequenceIndex] === ANSI_BELL) {
			return createControlParseResult(string.slice(index, sequenceIndex + 1), sequenceIndex + 1);
		}

		if (
			string[sequenceIndex] === ESCAPE
			&& string[sequenceIndex + 1] === ANSI_OSC_TERMINATOR
		) {
			return createControlParseResult(string.slice(index, sequenceIndex + 2), sequenceIndex + 2);
		}

		if (string[sequenceIndex] === C1_STRING_TERMINATOR) {
			return createControlParseResult(string.slice(index, sequenceIndex + 1), sequenceIndex + 1);
		}
	}

	return createControlParseResult(string.slice(index), string.length);
}

function parseAnsiCode(string, index) {
	const codePoint = string.codePointAt(index);
	if (codePoint === ESCAPE_CODE_POINT || codePoint === C1_OSC_CODE_POINT) {
		const hyperlinkCode = parseHyperlinkCode(string, index);
		if (hyperlinkCode) {
			return hyperlinkCode;
		}
	}

	const controlStringCode = parseControlStringCode(string, index);
	if (controlStringCode) {
		return controlStringCode;
	}

	return parseCsiCode(string, index);
}

function appendTrailingAnsiTokens(string, index, tokens) {
	while (index < string.length) {
		const nextCodePoint = string.codePointAt(index);
		if (!ESCAPES.has(nextCodePoint)) {
			break;
		}

		const escapeCode = parseAnsiCode(string, index);
		if (!escapeCode) {
			break;
		}

		tokens.push(escapeCode.token);
		index = escapeCode.endIndex;
	}

	return index;
}

function parseCharacterTokenWithRawSegmentation(string, index, graphemeSegments) {
	const segment = graphemeSegments.containing(index);
	if (!segment || segment.index !== index) {
		return;
	}

	return {
		token: {
			type: 'character',
			// Intentionally preserve UAX29 behavior (GB3): CRLF is one grapheme cluster.
			value: segment.segment,
			visibleWidth: getGraphemeWidth(segment.segment),
			isGraphemeContinuation: false,
		},
		endIndex: index + segment.segment.length,
	};
}

function collectVisibleCharacters(string) {
	const visibleCharacters = [];
	let index = 0;

	while (index < string.length) {
		const codePoint = string.codePointAt(index);
		if (ESCAPES.has(codePoint)) {
			const code = parseAnsiCode(string, index);
			if (code) {
				index = code.endIndex;
				continue;
			}
		}

		const value = String.fromCodePoint(codePoint);
		visibleCharacters.push({
			value,
			visibleWidth: 1,
			isGraphemeContinuation: false,
		});
		index += value.length;
	}

	return visibleCharacters;
}

function applyGraphemeMetadata(visibleCharacters) {
	if (visibleCharacters.length === 0) {
		return;
	}

	const visibleString = visibleCharacters.map(({value}) => value).join('');
	const scalarOffsets = [];
	let scalarOffset = 0;

	for (const visibleCharacter of visibleCharacters) {
		scalarOffsets.push(scalarOffset);
		scalarOffset += visibleCharacter.value.length;
	}

	le
... [TRUNCATED]
```

### File: .github\security.md
```md
# Security Policy

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security). Tidelift will coordinate the fix and disclosure.

```

