---
id: wrap-ansi
type: knowledge
owner: OA_Triage
---
# wrap-ansi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
import stringWidth from 'string-width';
import stripAnsi from 'strip-ansi';
import ansiStyles from 'ansi-styles';

const ANSI_ESCAPE = '\u001B';
const ANSI_ESCAPE_CSI = '\u009B';
const ESCAPES = new Set([
	ANSI_ESCAPE,
	ANSI_ESCAPE_CSI,
]);

const ANSI_ESCAPE_BELL = '\u0007';
const ANSI_CSI = '[';
const ANSI_OSC = ']';
const ANSI_SGR_TERMINATOR = 'm';
const ANSI_SGR_RESET = 0;
const ANSI_SGR_RESET_FOREGROUND = 39;
const ANSI_SGR_RESET_BACKGROUND = 49;
const ANSI_SGR_RESET_UNDERLINE_COLOR = 59;
const ANSI_SGR_FOREGROUND_EXTENDED = 38;
const ANSI_SGR_BACKGROUND_EXTENDED = 48;
const ANSI_SGR_UNDERLINE_COLOR_EXTENDED = 58;
const ANSI_SGR_COLOR_MODE_256 = 5;
const ANSI_SGR_COLOR_MODE_RGB = 2;
const ANSI_ESCAPE_LINK = `${ANSI_OSC}8;;`;
const ANSI_ESCAPE_REGEX = new RegExp(`^\\u001B(?:\\${ANSI_CSI}(?<sgr>[0-9;]*)${ANSI_SGR_TERMINATOR}|${ANSI_ESCAPE_LINK}(?<uri>[^\\u0007\\u001B]*)(?:\\u0007|\\u001B\\\\))`);
const ANSI_ESCAPE_CSI_REGEX = new RegExp(`^\\u009B(?<sgr>[0-9;]*)${ANSI_SGR_TERMINATOR}`);
const ANSI_SGR_MODIFIER_CLOSE_CODES = new Set(ansiStyles.codes.values());
ANSI_SGR_MODIFIER_CLOSE_CODES.delete(ANSI_SGR_RESET);

const segmenter = new Intl.Segmenter();
const getGraphemes = string => Array.from(segmenter.segment(string), ({segment}) => segment);
const TAB_SIZE = 8;

const wrapAnsiCode = code => `${ANSI_ESCAPE}${ANSI_CSI}${code}${ANSI_SGR_TERMINATOR}`;
const wrapAnsiHyperlink = url => `${ANSI_ESCAPE}${ANSI_ESCAPE_LINK}${url}${ANSI_ESCAPE_BELL}`;

const getSgrTokens = sgrParameters => {
	const codes = sgrParameters.split(';').map(sgrParameter => sgrParameter === '' ? ANSI_SGR_RESET : Number.parseInt(sgrParameter, 10));
	const sgrTokens = [];

	for (let index = 0; index < codes.length; index++) {
		const code = codes[index];

		if (!Number.isFinite(code)) {
			continue;
		}

		if (
			(
				code === ANSI_SGR_FOREGROUND_EXTENDED
				|| code === ANSI_SGR_BACKGROUND_EXTENDED
				|| code === ANSI_SGR_UNDERLINE_COLOR_EXTENDED
			)
		) {
			if (index + 1 >= codes.length) {
				break;
			}

			const mode = codes[index + 1];

			if (mode === ANSI_SGR_COLOR_MODE_256 && Number.isFinite(codes[index + 2])) {
				sgrTokens.push([code, mode, codes[index + 2]]);
				index += 2;
				continue;
			}

			const red = codes[index + 2];
			const green = codes[index + 3];
			const blue = codes[index + 4];
			if (
				mode === ANSI_SGR_COLOR_MODE_RGB
				&& Number.isFinite(red)
				&& Number.isFinite(green)
				&& Number.isFinite(blue)
			) {
				sgrTokens.push([code, mode, red, green, blue]);
				index += 4;
				continue;
			}

			break;
		}

		sgrTokens.push([code]);
	}

	return sgrTokens;
};

const removeActiveStyle = (activeStyles, family) => {
	const activeStyleIndex = activeStyles.findIndex(activeStyle => activeStyle.family === family);

	if (activeStyleIndex !== -1) {
		activeStyles.splice(activeStyleIndex, 1);
	}
};

const upsertActiveStyle = (activeStyles, nextActiveStyle) => {
	removeActiveStyle(activeStyles, nextActiveStyle.family);
	activeStyles.push(nextActiveStyle);
};

const removeModifierStylesByClose = (activeStyles, closeCode) => {
	for (let index = activeStyles.length - 1; index >= 0; index--) {
		const activeStyle = activeStyles[index];
		if (activeStyle.family.startsWith('modifier-') && activeStyle.close === closeCode) {
			activeStyles.splice(index, 1);
		}
	}
};

const getColorStyle = (code, sgrToken) => {
	if ((code >= 30 && code <= 37) || (code >= 90 && code <= 97) || (code === ANSI_SGR_FOREGROUND_EXTENDED && sgrToken.length > 1)) {
		return {
			family: 'foreground',
			open: sgrToken.join(';'),
			close: ANSI_SGR_RESET_FOREGROUND,
		};
	}

	if ((code >= 40 && code <= 47) || (code >= 100 && code <= 107) || (code === ANSI_SGR_BACKGROUND_EXTENDED && sgrToken.length > 1)) {
		return {
			family: 'background',
			open: sgrToken.join(';'),
			close: ANSI_SGR_RESET_BACKGROUND,
		};
	}

	if (code === ANSI_SGR_UNDERLINE_COLOR_EXTENDED && sgrToken.length > 1) {
		return {
			family: 'underlineColor',
			open: sgrToken.join(';'),
			close: ANSI_SGR_RESET_UNDERLINE_COLOR,
		};
	}
};

const applySgrResetCode = (code, activeStyles) => {
	if (code === ANSI_SGR_RESET) {
		activeStyles.length = 0;
		return true;
	}

	if (code === ANSI_SGR_RESET_FOREGROUND) {
		removeActiveStyle(activeStyles, 'foreground');
		return true;
	}

	if (code === ANSI_SGR_RESET_BACKGROUND) {
		removeActiveStyle(activeStyles, 'background');
		return true;
	}

	if (code === ANSI_SGR_RESET_UNDERLINE_COLOR) {
		removeActiveStyle(activeStyles, 'underlineColor');
		return true;
	}

	if (ANSI_SGR_MODIFIER_CLOSE_CODES.has(code)) {
		removeModifierStylesByClose(activeStyles, code);
		return true;
	}

	return false;
};

const applySgrToken = (sgrToken, activeStyles) => {
	const [code] = sgrToken;

	if (applySgrResetCode(code, activeStyles)) {
		return;
	}

	const colorStyle = getColorStyle(code, sgrToken);
	if (colorStyle) {
		upsertActiveStyle(activeStyles, colorStyle);
		return;
	}

	const close = ansiStyles.codes.get(code);
	if (close !== undefined && close !== ANSI_SGR_RESET) {
		upsertActiveStyle(activeStyles, {
			family: `modifier-${code}`,
			open: sgrToken.join(';'),
			close,
		});
	}
};

const applySgrParameters = (sgrParameters, activeStyles) => {
	for (const sgrToken of getSgrTokens(sgrParameters)) {
		applySgrToken(sgrToken, activeStyles);
	}
};

const applySgrResets = (sgrParameters, activeStyles) => {
	for (const sgrToken of getSgrTokens(sgrParameters)) {
		const [code] = sgrToken;
		applySgrResetCode(code, activeStyles);
	}
};

const applyLeadingSgrResets = (string, activeStyles) => {
	let remainder = string;

	while (remainder.length > 0) {
		if (remainder.startsWith(ANSI_ESCAPE) && remainder[1] !== '\\') {
			const match = ANSI_ESCAPE_REGEX.exec(remainder);
			if (!match) {
				break;
			}

			if (match.groups.sgr !== undefined) {
				applySgrResets(match.groups.sgr, activeStyles);
			}

			remainder = remainder.slice(match[0].length);
			continue;
		}

		if (remainder.startsWith(ANSI_ESCAPE_CSI)) {
			const match = ANSI_ESCAPE_CSI_REGEX.exec(remainder);
			if (!match || match.groups.sgr === undefined) {
				break;
			}

			applySgrResets(match.groups.sgr, activeStyles);
			remainder = remainder.slice(match[0].length);
			continue;
		}

		break;
	}
};

const getClosingSgrSequence = activeStyles => [...activeStyles].reverse().map(activeStyle => wrapAnsiCode(activeStyle.close)).join('');
const getOpeningSgrSequence = activeStyles => activeStyles.map(activeStyle => wrapAnsiCode(activeStyle.open)).join('');

// Calculate the length of words split on ' ', ignoring
// the extra characters added by ANSI escape codes
const wordLengths = string => string.split(' ').map(word => stringWidth(word));

// Wrap a long word across multiple rows
// ANSI escape codes do not count towards length
const wrapWord = (rows, word, columns) => {
	const characters = getGraphemes(word);

	let isInsideEscape = false;
	let isInsideLinkEscape = false;
	let visible = stringWidth(stripAnsi(rows.at(-1)));

	for (const [index, character] of characters.entries()) {
		const characterLength = stringWidth(character);

		if (visible + characterLength <= columns) {
			rows[rows.length - 1] += character;
		} else {
			rows.push(character);
			visible = 0;
		}

		if (ESCAPES.has(character) && !(isInsideLinkEscape && character === ANSI_ESCAPE && characters[index + 1] === '\\')) {
			isInsideEscape = true;

			const ansiEscapeLinkCandidate = characters.slice(index + 1, index + 1 + ANSI_ESCAPE_LINK.length).join('');
			isInsideLinkEscape = ansiEscapeLinkCandidate === ANSI_ESCAPE_LINK;
		}

		if (isInsideEscape) {
			if (isInsideLinkEscape) {
				if (
					character === ANSI_ESCAPE_BELL
					|| (character === '\\' && index > 0 && characters[index - 1] === ANSI_ESCAPE) // ST terminator (ESC \)
				) {
					isInsideEscape = false;
					isInsideLinkEscape = false;
				}
			} else if (character === ANSI_SGR_TERMINATOR) {
				isInsideEscape = false;
			}

			continue;
		}

		visible += characterLength;

		if (visible === columns && index < characters.length - 1) {
			rows.push('');
			visible = 0;
		}
	}

	// It's possible that the last row we copy over is only
	// ANSI escape characters, handle this edge-case
	if (!visible && rows.at(-1).length > 0 && rows.length > 1) {
		rows[rows.length - 2] += rows.pop();
	}
};

// Trims spaces from a string ignoring invisible sequences
const stringVisibleTrimSpacesRight = string => {
	const words = string.split(' ');
	let last = words.length;

	while (last > 0) {
		if (stringWidth(words[last - 1]) > 0) {
			break;
		}

		last--;
	}

	if (last === words.length) {
		return string;
	}

	return words.slice(0, last).join(' ') + words.slice(last).join('');
};

const expandTabs = line => {
	if (!line.includes('\t')) {
		return line;
	}

	const segments = line.split('\t');
	let visible = 0;
	let expandedLine = '';

	for (const [index, segment] of segments.entries()) {
		expandedLine += segment;
		visible += stringWidth(segment);

		if (index < segments.length - 1) {
			const spaces = TAB_SIZE - (visible % TAB_SIZE);
			expandedLine += ' '.repeat(spaces);
			visible += spaces;
		}
	}

	return expandedLine;
};

// The wrap-ansi module can be invoked in either 'hard' or 'soft' wrap mode.
//
// 'hard' will never allow a string to take up more than columns characters.
//
// 'soft' allows long words to expand past the column length.
const exec = (string, columns, options = {}) => {
	if (options.trim !== false && string.trim() === '') {
		return '';
	}

	let returnValue = '';
	let escapeUrl;
	const activeStyles = [];

	const lengths = wordLengths(string);
	let rows = [''];

	for (const [index, word] of string.split(' ').entries()) {
		if (options.trim !== false) {
			rows[rows.length - 1] = rows.at(-1).trimStart();
		}

		let rowLength = stringWidth(rows.at(-1));

		if (index !== 0) {
			if (rowLength >= columns && (options.wordWrap === false || options.trim === false)) {
				// If we start with a new word but the current row length equals the length of the columns, add a new row
				rows.push('');
				rowLength = 0;
			}

			if (rowLength > 0 || options.trim === false) {
				rows[rows.length - 1] += ' ';
				rowLength++;
			}
		}

		// In 'hard' wrap mode, the length of a line is never allowed to extend past 'columns'
		if (options.hard && options.wordWrap !== false && lengths[index] > columns) {
			const remainingColumns = columns - rowLength;
			const breaksStartingThisLine = 1 + Math.floor((lengths[index] - remainingColumns - 1) / columns);
			const breaksStartingNextLine = Math.floor((lengths[index] - 1) / columns);
			if (breaksStartingNextLine < breaksStartingThisLine) {
				rows.push('');
			}

			wrapWord(rows, word, columns);
			continue;
		}

		if (rowLength + lengths[index] > columns && rowLength > 0 && lengths[index] > 0) {
			if (options.wordWrap === false && rowLength < columns) {
				wrapWord(rows, word, columns);
				continue;
			}

			rows.push('');
		}

		if (rowLength + lengths[index] > columns && options.wordWrap === false) {
			wrapWord(rows, word, columns);
			continue;
		}

		rows[rows.length - 1] += word;
	}

	if (options.trim !== false) {
		rows = rows.map(row => stringVisibleTrimSpacesRight(row));
	}

	const preString = rows.join('\n');
	const pre = getGraphemes(preString);

	// We need to keep a separate index as `String#slice()` works on Unicode code units, while `pre` is an array of grapheme clusters.
	let preStringIndex = 0;

	for (const [index, character] of pre.entries()) {
		returnValue += character;

		if (character === ANSI_ESCAPE && pre[index + 1] !== '\\') {
			const {groups} = ANSI_ESCAPE_REGEX.exec(preString.slice(preStringIndex)) || {groups: {}};
			if (groups.sgr !== undefined) {
				applySgrParameters(groups.sgr, activeStyles);
			} else if (groups.uri !== undefined) {
				escapeUrl = groups.uri.length === 0 ? undefined : groups.uri;
			}
		} else if (character === ANSI_ESCAPE_CSI) {
			const {groups} = ANSI_ESCAPE_CSI_REGEX.exec(preString.slice(preStringIndex)) || {groups: {}};
			if (groups.sgr !== undefined) {
				applySgrParameters(groups.sgr, activeStyles);
			}
		}

		if (pre[index + 1] === '\n') {
			if (escapeUrl) {
				returnValue += wrapAnsiHyperlink('');
			}

			returnValue += getClosingSgrSequence(activeStyles);
		} else if (character === '\n') {
			const openingStyles = [...activeStyles];
			applyLeadingSgrResets(preString.slice(preStringIndex + 1), openingStyles);
			returnValue += getOpeningSgrSequence(openingStyles);

			if (escapeUrl) {
				returnValue += wrapAnsiHyperlink(escapeUrl);
			}
		}

		preStringIndex += character.length;
	}

	return returnValue;
};

// For each newline, invoke the method separately
export default function wrapAnsi(string, columns, options) {
	return String(string)
		.normalize()
		.replaceAll('\r\n', '\n')
		.split('\n')
		.map(line => exec(expandTabs(line), columns, options))
		.join('\n');
}

```

### File: package.json
```json
{
	"name": "wrap-ansi",
	"version": "10.0.0",
	"description": "Wordwrap a string with ANSI escape codes",
	"license": "MIT",
	"repository": "chalk/wrap-ansi",
	"funding": "https://github.com/chalk/wrap-ansi?sponsor=1",
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
	"engines": {
		"node": ">=20"
	},
	"scripts": {
		"test": "xo && nyc ava && tsd"
	},
	"files": [
		"index.js",
		"index.d.ts"
	],
	"keywords": [
		"wrap",
		"break",
		"wordwrap",
		"wordbreak",
		"linewrap",
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
		"log",
		"logging",
		"command-line",
		"text"
	],
	"dependencies": {
		"ansi-styles": "^6.2.3",
		"string-width": "^8.2.0",
		"strip-ansi": "^7.1.2"
	},
	"devDependencies": {
		"ava": "^6.4.1",
		"chalk": "^5.6.2",
		"coveralls": "^3.1.1",
		"has-ansi": "^6.0.2",
		"nyc": "^17.1.0",
		"tsd": "^0.33.0",
		"xo": "^1.2.3"
	}
}

```

### File: readme.md
```md
# wrap-ansi

> Wordwrap a string with [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles)

## Install

```sh
npm install wrap-ansi
```

## Usage

```js
import chalk from 'chalk';
import wrapAnsi from 'wrap-ansi';

const input = 'The quick brown ' + chalk.red('fox jumped over ') +
	'the lazy ' + chalk.green('dog and then ran away with the unicorn.');

console.log(wrapAnsi(input, 20));
```

<img width="331" src="screenshot.png">

## API

### wrapAnsi(string, columns, options?)

Wrap words to the specified column width.

#### string

Type: `string`

A string with ANSI escape codes, like one styled by [`chalk`](https://github.com/chalk/chalk).

Newline characters will be normalized to `\n`.

Tab characters are expanded to spaces using 8-column tab stops before wrapping.

#### columns

Type: `number`

The number of columns to wrap the text to.

#### options

Type: `object`

##### hard

Type: `boolean`\
Default: `false`

By default the wrap is soft, meaning long words may extend past the column width. Setting this to `true` will make it hard wrap at the column width.

##### wordWrap

Type: `boolean`\
Default: `true`

By default, an attempt is made to split words at spaces, ensuring that they don't extend past the configured columns. If wordWrap is `false`, each column will instead be completely filled splitting words as necessary.

##### trim

Type: `boolean`\
Default: `true`

Whitespace on all lines is removed by default. Set this option to `false` if you don't want to trim.

## Related

- [slice-ansi](https://github.com/chalk/slice-ansi) - Slice a string with ANSI escape codes
- [cli-truncate](https://github.com/sindresorhus/cli-truncate) - Truncate a string to a specific width in the terminal
- [chalk](https://github.com/chalk/chalk) - Terminal string styling done right
- [jsesc](https://github.com/mathiasbynens/jsesc) - Generate ASCII-only output from Unicode strings. Useful for creating test fixtures.

```

### File: index.d.ts
```ts
export type Options = {
	/**
	By default the wrap is soft, meaning long words may extend past the column width. Setting this to `true` will make it hard wrap at the column width.

	@default false
	*/
	readonly hard?: boolean;

	/**
	By default, an attempt is made to split words at spaces, ensuring that they don't extend past the configured columns. If wordWrap is `false`, each column will instead be completely filled splitting words as necessary.

	@default true
	*/
	readonly wordWrap?: boolean;

	/**
	Whitespace on all lines is removed by default. Set this option to `false` if you don't want to trim.

	@default true
	*/
	readonly trim?: boolean;
};

/**
Wrap words to the specified column width.

@param string - A string with ANSI escape codes, like one styled by [`chalk`](https://github.com/chalk/chalk). Newline characters will be normalized to `\n`. Tab characters are expanded to spaces using 8-column tab stops before wrapping.
@param columns - The number of columns to wrap the text to.

@example
```
import chalk from 'chalk';
import wrapAnsi from 'wrap-ansi';

const input = 'The quick brown ' + chalk.red('fox jumped over ') +
	'the lazy ' + chalk.green('dog and then ran away with the unicorn.');

console.log(wrapAnsi(input, 20));
```
*/
export default function wrapAnsi(string: string, columns: number, options?: Options): string;

```

### File: index.test-d.ts
```ts
import {expectType} from 'tsd';
import wrapAnsi from './index.js';

expectType<string>(wrapAnsi('input', 80));
expectType<string>(wrapAnsi('input', 80, {}));
expectType<string>(wrapAnsi('input', 80, {hard: true}));
expectType<string>(wrapAnsi('input', 80, {hard: false}));
expectType<string>(wrapAnsi('input', 80, {trim: true}));
expectType<string>(wrapAnsi('input', 80, {trim: false}));
expectType<string>(wrapAnsi('input', 80, {wordWrap: true}));
expectType<string>(wrapAnsi('input', 80, {wordWrap: false}));

```

### File: test.js
```js
import test from 'ava';
import chalk from 'chalk';
import hasAnsi from 'has-ansi';
import stripAnsi from 'strip-ansi';
import wrapAnsi from './index.js';

chalk.level = 1;

// When "hard" is false

const fixture = 'The quick brown ' + chalk.red('fox jumped over ') + 'the lazy ' + chalk.green('dog and then ran away with the unicorn.');
const fixture2 = '12345678\n901234567890';
const fixture3 = '12345678\n901234567890 12345';
const fixture4 = '12345678\n';
const fixture5 = '12345678\n ';

test('wraps string at 20 characters', t => {
	const result = wrapAnsi(fixture, 20);

	t.is(result, 'The quick brown \u001B[31mfox\u001B[39m\n\u001B[31mjumped over \u001B[39mthe lazy\n\u001B[32mdog and then ran\u001B[39m\n\u001B[32maway with the\u001B[39m\n\u001B[32municorn.\u001B[39m');
	t.true(stripAnsi(result).split('\n').every(line => line.length <= 20));
});

test('wraps string at 30 characters', t => {
	const result = wrapAnsi(fixture, 30);

	t.is(result, 'The quick brown \u001B[31mfox jumped\u001B[39m\n\u001B[31mover \u001B[39mthe lazy \u001B[32mdog and then ran\u001B[39m\n\u001B[32maway with the unicorn.\u001B[39m');
	t.true(stripAnsi(result).split('\n').every(line => line.length <= 30));
});

test('does not break strings longer than "cols" characters', t => {
	const result = wrapAnsi(fixture, 5, {hard: false});

	t.is(result, 'The\nquick\nbrown\n\u001B[31mfox\u001B[39m\n\u001B[31mjumped\u001B[39m\n\u001B[31mover\u001B[39m\n\u001B[39mthe\nlazy\n\u001B[32mdog\u001B[39m\n\u001B[32mand\u001B[39m\n\u001B[32mthen\u001B[39m\n\u001B[32mran\u001B[39m\n\u001B[32maway\u001B[39m\n\u001B[32mwith\u001B[39m\n\u001B[32mthe\u001B[39m\n\u001B[32municorn.\u001B[39m');
	t.true(stripAnsi(result).split('\n').some(line => line.length > 5));
});

test('handles colored string that wraps on to multiple lines', t => {
	const result = wrapAnsi(chalk.green('hello world') + ' hey!', 5, {hard: false});
	const lines = result.split('\n');
	t.true(hasAnsi(lines[0]));
	t.true(hasAnsi(lines[1]));
	t.false(hasAnsi(lines[2]));
});

test('does not prepend newline if first string is greater than "cols"', t => {
	const result = wrapAnsi(chalk.green('hello') + '-world', 5, {hard: false});
	t.is(result.split('\n').length, 1);
});

// When "hard" is true

test('breaks strings longer than "cols" characters', t => {
	const result = wrapAnsi(fixture, 5, {hard: true});

	t.is(result, 'The\nquick\nbrown\n\u001B[31mfox j\u001B[39m\n\u001B[31mumped\u001B[39m\n\u001B[31mover\u001B[39m\n\u001B[39mthe\nlazy\n\u001B[32mdog\u001B[39m\n\u001B[32mand\u001B[39m\n\u001B[32mthen\u001B[39m\n\u001B[32mran\u001B[39m\n\u001B[32maway\u001B[39m\n\u001B[32mwith\u001B[39m\n\u001B[32mthe\u001B[39m\n\u001B[32munico\u001B[39m\n\u001B[32mrn.\u001B[39m');
	t.true(stripAnsi(result).split('\n').every(line => line.length <= 5));
});

test('removes last row if it contained only ansi escape codes', t => {
	const result = wrapAnsi(chalk.green('helloworld'), 2, {hard: true});
	t.true(stripAnsi(result).split('\n').every(x => x.length === 2));
});

test('does not prepend newline if first word is split', t => {
	const result = wrapAnsi(chalk.green('hello') + 'world', 5, {hard: true});
	t.is(result.split('\n').length, 2);
});

test('takes into account line returns inside input', t => {
	t.is(wrapAnsi(fixture2, 10, {hard: true}), '12345678\n9012345678\n90');
});

test('word wrapping', t => {
	t.is(wrapAnsi(fixture3, 15), '12345678\n901234567890\n12345');
});

test('does not pre-wrap long words when hard wrapping with wordWrap false', t => {
	const defaultResult = wrapAnsi('hi, this https://IsAReallyLongWordButIDoNotKnowHowItShouldBehave.com', 32, {hard: true});
	t.is(defaultResult, 'hi, this\nhttps://IsAReallyLongWordButIDoN\notKnowHowItShouldBehave.com');

	const result = wrapAnsi('hi, this https://IsAReallyLongWordButIDoNotKnowHowItShouldBehave.com', 32, {hard: true, wordWrap: false});
	t.is(result, 'hi, this https://IsAReallyLongWo\nrdButIDoNotKnowHowItShouldBehave\n.com');

	const result2 = wrapAnsi('hi, this IsAReallyLongWordButIDoNotKnowHowItShouldBehave', 32, {hard: true, wordWrap: false});
	t.is(result2, 'hi, this IsAReallyLongWordButIDo\nNotKnowHowItShouldBehave');
});

test('no word-wrapping', t => {
	const result = wrapAnsi(fixture3, 15, {wordWrap: false});
	t.is(result, '12345678\n901234567890 12\n345');

	const result2 = wrapAnsi(fixture3, 5, {wordWrap: false});
	t.is(result2, '12345\n678\n90123\n45678\n90 12\n345');

	const result3 = wrapAnsi(fixture5, 5, {wordWrap: false});
	t.is(result3, '12345\n678\n');

	const result4 = wrapAnsi(fixture, 5, {wordWrap: false});
	t.is(result4, 'The q\nuick\nbrown\n\u001B[31mfox j\u001B[39m\n\u001B[31mumped\u001B[39m\n\u001B[31mover\u001B[39m\n\u001B[39mthe l\nazy \u001B[32md\u001B[39m\n\u001B[32mog an\u001B[39m\n\u001B[32md the\u001B[39m\n\u001B[32mn ran\u001B[39m\n\u001B[32maway\u001B[39m\n\u001B[32mwith\u001B[39m\n\u001B[32mthe u\u001B[39m\n\u001B[32mnicor\u001B[39m\n\u001B[32mn.\u001B[39m');
});

test('no word-wrapping and no trimming', t => {
	const result = wrapAnsi(fixture3, 13, {wordWrap: false, trim: false});
	t.is(result, '12345678\n901234567890 \n12345');

	const result2 = wrapAnsi(fixture4, 5, {wordWrap: false, trim: false});
	t.is(result2, '12345\n678\n');

	const result3 = wrapAnsi(fixture5, 5, {wordWrap: false, trim: false});
	t.is(result3, '12345\n678\n ');

	const result4 = wrapAnsi(fixture, 5, {wordWrap: false, trim: false});
	t.is(result4, 'The q\nuick \nbrown\n \u001B[31mfox \u001B[39m\n\u001B[31mjumpe\u001B[39m\n\u001B[31md ove\u001B[39m\n\u001B[31mr \u001B[39mthe\n lazy\n \u001B[32mdog \u001B[39m\n\u001B[32mand t\u001B[39m\n\u001B[32mhen r\u001B[39m\n\u001B[32man aw\u001B[39m\n\u001B[32may wi\u001B[39m\n\u001B[32mth th\u001B[39m\n\u001B[32me uni\u001B[39m\n\u001B[32mcorn.\u001B[39m');
});

test('supports fullwidth characters', t => {
	t.is(wrapAnsi('안녕하세', 4, {hard: true}), '안녕\n하세');
});

test('supports unicode surrogate pairs', t => {
	t.is(wrapAnsi('a\uD83C\uDE00bc', 2, {hard: true}), 'a\n\uD83C\uDE00\nbc');
	t.is(wrapAnsi('a\uD83C\uDE00bc\uD83C\uDE00d\uD83C\uDE00', 2, {hard: true}), 'a\n\uD83C\uDE00\nbc\n\uD83C\uDE00\nd\n\uD83C\uDE00');
});

test('does not split multi-codepoint grapheme clusters across lines', t => {
	// ZWJ family emoji (7 codepoints, width 2)
	t.is(wrapAnsi('a👨‍👩‍👧‍👦b', 2, {hard: true}), 'a\n👨‍👩‍👧‍👦\nb');

	// Flag emoji (2 regional indicators, width 2)
	t.is(wrapAnsi('a🇺🇸b', 2, {hard: true}), 'a\n🇺🇸\nb');

	// Skin tone modifier (2 codepoints, width 2)
	t.is(wrapAnsi('a👋🏽b', 2, {hard: true}), 'a\n👋🏽\nb');

	// Tamil combining character (2 codepoints, width 1)
	t.is(wrapAnsi('நிநி', 1, {hard: true}), 'நி\nநி');

	// Multiple grapheme clusters fitting on one line
	t.is(wrapAnsi('🇺🇸🇬🇧', 4, {hard: true}), '🇺🇸🇬🇧');
	t.is(wrapAnsi('🇺🇸🇬🇧', 3, {hard: true}), '🇺🇸\n🇬🇧');

	// Grapheme cluster at exact column boundary
	t.is(wrapAnsi('ab👨‍👩‍👧‍👦cd', 4, {hard: true}), 'ab👨‍👩‍👧‍👦\ncd');
	t.is(wrapAnsi('ab🇺🇸cd', 4, {hard: true}), 'ab🇺🇸\ncd');

	// Soft wrapping does not split grapheme clusters
	t.is(wrapAnsi('test 👨‍👩‍👧‍👦', 4), 'test\n👨‍👩‍👧‍👦');

	// Colored grapheme clusters preserve ANSI codes across wraps
	t.is(stripAnsi(wrapAnsi(chalk.red('a👨‍👩‍👧‍👦b'), 2, {hard: true})), 'a\n👨‍👩‍👧‍👦\nb');
});

test('#23, properly wraps whitespace with no trimming', t => {
	t.is(wrapAnsi('   ', 2, {trim: false}), '  \n ');
	t.is(wrapAnsi('   ', 2, {trim: false, hard: true}), '  \n ');
});

test('#24, trims leading and trailing whitespace only on actual wrapped lines and only with trimming', t => {
	t.is(wrapAnsi('   foo   bar   ', 3), 'foo\nbar');
	t.is(wrapAnsi('   foo   bar   ', 6), 'foo\nbar');
	t.is(wrapAnsi('   foo   bar   ', 42), 'foo   bar');
	t.is(wrapAnsi('   foo   bar   ', 42, {trim: false}), '   foo   bar   ');
});

test('#24, trims leading and trailing whitespace inside a color block only on actual wrapped lines and only with trimming', t => {
	t.is(wrapAnsi(chalk.blue('   foo   bar   '), 6), chalk.blue('foo\nbar'));
	t.is(wrapAnsi(chalk.blue('   foo   bar   '), 42), chalk.blue('foo   bar'));
	t.is(wrapAnsi(chalk.blue('   foo   bar   '), 42, {trim: false}), chalk.blue('   foo   bar   '));
});

test('#25, properly wraps whitespace between words with no trimming', t => {
	t.is(wrapAnsi('foo bar', 3), 'foo\nbar');
	t.is(wrapAnsi('foo bar', 3, {hard: true}), 'foo\nbar');
	t.is(wrapAnsi('foo bar', 3, {trim: false}), 'foo\n \nbar');
	t.is(wrapAnsi('foo bar', 3, {trim: false, hard: true}), 'foo\n \nbar');
});

test('#26, does not multiply leading spaces with no trimming', t => {
	t.is(wrapAnsi(' a ', 10, {trim: false}), ' a ');
	t.is(wrapAnsi('   a ', 10, {trim: false}), '   a ');
});

test('#27, does not remove spaces in line with ansi escapes when no trimming', t => {
	t.is(wrapAnsi(chalk.bgGreen(` ${chalk.black('OK')} `), 100, {trim: false}), chalk.bgGreen(` ${chalk.black('OK')} `));
	t.is(wrapAnsi(chalk.bgGreen(`  ${chalk.black('OK')} `), 100, {trim: false}), chalk.bgGreen(`  ${chalk.black('OK')} `));
	t.is(wrapAnsi(chalk.bgGreen(' hello '), 10, {hard: true, trim: false}), chalk.bgGreen(' hello '));
});

test('#43, preserves nested foreground and background styles on every wrapped line', t => {
	const result = wrapAnsi(chalk.bgGreen.black('test'), 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[42m\u001B[30mte\u001B[39m\u001B[49m\n\u001B[42m\u001B[30mst\u001B[39m\u001B[49m');
});

test('#43, preserves stacked modifiers and colors on every wrapped line', t => {
	const result = wrapAnsi(chalk.blue.bold('test'), 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[34m\u001B[1mte\u001B[22m\u001B[39m\n\u001B[34m\u001B[1mst\u001B[22m\u001B[39m');
});

test('#43, preserves combined SGR parameters across wrapped lines', t => {
	const input = '\u001B[1;34mtest\u001B[39;22m';
	const result = wrapAnsi(input, 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[1;34mte\u001B[39m\u001B[22m\n\u001B[1m\u001B[34mst\u001B[39;22m');
});

test('#43, preserves truecolor foreground and background styles on every wrapped line', t => {
	const input = '\u001B[48;2;255;0;0m\u001B[38;2;0;0;0mtest\u001B[39m\u001B[49m';
	const result = wrapAnsi(input, 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[48;2;255;0;0m\u001B[38;2;0;0;0mte\u001B[39m\u001B[49m\n\u001B[48;2;255;0;0m\u001B[38;2;0;0;0mst\u001B[39m\u001B[49m');
});

test('#43, does not treat malformed extended color parameters as modifiers', t => {
	const malformedForeground = wrapAnsi('\u001B[38;2;255mab\u001B[0m', 1, {hard: true, trim: false, wordWrap: false});
	const malformedBackground = wrapAnsi('\u001B[48;5mab\u001B[0m', 1, {hard: true, trim: false, wordWrap: false});
	t.is(malformedForeground, '\u001B[38;2;255ma\nb\u001B[0m');
	t.is(malformedBackground, '\u001B[48;5ma\nb\u001B[0m');
});

test('#43, treats omitted SGR params as reset', t => {
	const colorThenReset = wrapAnsi('\u001B[31;mab\u001B[0m', 1, {hard: true, trim: false, wordWrap: false});
	const boldResetThenColor = wrapAnsi('\u001B[1;;31mab\u001B[0m', 1, {hard: true, trim: false, wordWrap: false});
	t.is(colorThenReset, '\u001B[31;ma\nb\u001B[0m');
	t.is(boldResetThenColor, '\u001B[1;;31ma\u001B[39m\n\u001B[31mb\u001B[0m');
});

test('#43, preserves C1 CSI SGR styles across wrapped lines', t => {
	const result = wrapAnsi('\u009B1;34mtest\u009B39;22m', 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u009B1;34mte\u001B[39m\u001B[22m\n\u001B[1m\u001B[34mst\u009B39;22m');
});

test('#43, preserves underline color SGR styles across wrapped lines', t => {
	const result = wrapAnsi('\u001B[58;5;196mtest\u001B[59m', 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[58;5;196mte\u001B[59m\n\u001B[58;5;196mst\u001B[59m');
});

test('#43, preserves bold and dim styles across wrapped lines', t => {
	const result = wrapAnsi('\u001B[1m\u001B[2mtest\u001B[22m', 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[1m\u001B[2mte\u001B[22m\u001B[22m\n\u001B[1m\u001B[2mst\u001B[22m');
});

test('#43, clears both bold and dim when reset 22 appears at wrapped line start', t => {
	const result = wrapAnsi('\u001B[1m\u001B[2mab\u001B[22mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[1m\u001B[2ma\u001B[22m\u001B[22m\n\u001B[1m\u001B[2mb\u001B[22m\u001B[22m\n\u001B[22mc\nd');
});

test('#43, does not reopen styles that are reset by a combined SGR sequence at wrapped line start', t => {
	const result = wrapAnsi('\u001B[1;2;31mab\u001B[22;39mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[1;2;31ma\u001B[39m\u001B[22m\u001B[22m\n\u001B[1m\u001B[2m\u001B[31mb\u001B[39m\u001B[22m\u001B[22m\n\u001B[22;39mc\nd');
});

test('#43, handles C1 SGR reset at wrapped line start for stacked modifiers', t => {
	const result = wrapAnsi('\u009B1m\u009B2mab\u009B22mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u009B1m\u009B2ma\u001B[22m\u001B[22m\n\u001B[1m\u001B[2mb\u001B[22m\u001B[22m\n\u009B22mc\nd');
});

test('#43, does not duplicate reopen output when the same modifier is applied repeatedly', t => {
	const result = wrapAnsi('\u001B[1m\u001B[1mtest\u001B[22m', 2, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[1m\u001B[1mte\u001B[22m\n\u001B[1mst\u001B[22m');
});

test('#43, does not reopen modifiers that are immediately reset at wrapped line start', t => {
	const result = wrapAnsi('\u001B[1mab\u001B[22mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[1ma\u001B[22m\n\u001B[1mb\u001B[22m\n\u001B[22mc\nd');
});

test('#43, does not reopen colors that are immediately reset at wrapped line start', t => {
	const result = wrapAnsi('\u001B[31mab\u001B[39mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[31ma\u001B[39m\n\u001B[31mb\u001B[39m\n\u001B[39mc\nd');
});

test('#43, does not reopen background when reset at wrapped line start while preserving foreground', t => {
	const result = wrapAnsi('\u001B[31m\u001B[42mab\u001B[49mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[31m\u001B[42ma\u001B[49m\u001B[39m\n\u001B[31m\u001B[42mb\u001B[49m\u001B[39m\n\u001B[31m\u001B[49mc\u001B[39m\n\u001B[31md');
});

test('#43, does not reopen non-22 modifiers that are immediately reset at wrapped line start', t => {
	const result = wrapAnsi('\u001B[9mab\u001B[29mcd', 1, {hard: true, trim: false, wordWrap: false});
	t.is(result, '\u001B[9ma\u001B[29m\n\u001B[9mb\u001B[29m\n\u001B[29mc\nd');
});

test('#43, does not reopen styles reset after a leading hyperlink escape at wrapped line start', t => {
	const belResult = wrapAnsi('\u001B[31mab\u001B]8;;https://example.com\u0007\u001B[39mc\u001B]8;;\u0007', 1, {hard: true, trim: false, wordWrap: false});
	const stResult = wrapAnsi('\u001B[31mab\u001B]8;;https://example.com\u001B\\\u001B[39mc\u001B]8;;\u001B\\', 1, {hard: true, trim: false, wordWrap: false});
	t.is(belResult, '\u001B[31ma\u001B[39m\n\u001B[31mb\u001B[39m\n\u001B]8;;https://example.com\u0007\
... [TRUNCATED]
```

### File: .github\security.md
```md
# Security Policy

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security). Tidelift will coordinate the fix and disclosure.

```

