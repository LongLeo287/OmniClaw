---
id: github.com-chalk-ansi-styles-e97b99ca-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:36.992585
---

# KNOWLEDGE EXTRACT: github.com_chalk_ansi-styles_e97b99ca
> **Extracted on:** 2026-04-01 14:31:06
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523932/github.com_chalk_ansi-styles_e97b99ca

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
export type CSPair = { // eslint-disable-line @typescript-eslint/naming-convention
	/**
	The ANSI terminal control sequence for starting this style.
	*/
	readonly open: string;

	/**
	The ANSI terminal control sequence for ending this style.
	*/
	readonly close: string;
};

export type ColorBase = {
	/**
	The ANSI terminal control sequence for ending this color.
	*/
	readonly close: string;

	ansi(code: number): string;

	ansi256(code: number): string;

	ansi16m(red: number, green: number, blue: number): string;
};

export type Modifier = {
	/**
	Resets the current color chain.
	*/
	readonly reset: CSPair;

	/**
	Make text bold.
	*/
	readonly bold: CSPair;

	/**
	Emitting only a small amount of light.
	*/
	readonly dim: CSPair;

	/**
	Make text italic. (Not widely supported)
	*/
	readonly italic: CSPair;

	/**
	Make text underline. (Not widely supported)
	*/
	readonly underline: CSPair;

	/**
	Make text overline.

	Supported on VTE-based terminals, the GNOME terminal, mintty, and Git Bash.
	*/
	readonly overline: CSPair;

	/**
	Inverse background and foreground colors.
	*/
	readonly inverse: CSPair;

	/**
	Prints the text, but makes it invisible.
	*/
	readonly hidden: CSPair;

	/**
	Puts a horizontal line through the center of the text. (Not widely supported)
	*/
	readonly strikethrough: CSPair;
};

export type ForegroundColor = {
	readonly black: CSPair;
	readonly red: CSPair;
	readonly green: CSPair;
	readonly yellow: CSPair;
	readonly blue: CSPair;
	readonly cyan: CSPair;
	readonly magenta: CSPair;
	readonly white: CSPair;

	/**
	Alias for `blackBright`.
	*/
	readonly gray: CSPair;

	/**
	Alias for `blackBright`.
	*/
	readonly grey: CSPair;

	readonly blackBright: CSPair;
	readonly redBright: CSPair;
	readonly greenBright: CSPair;
	readonly yellowBright: CSPair;
	readonly blueBright: CSPair;
	readonly cyanBright: CSPair;
	readonly magentaBright: CSPair;
	readonly whiteBright: CSPair;
};

export type BackgroundColor = {
	readonly bgBlack: CSPair;
	readonly bgRed: CSPair;
	readonly bgGreen: CSPair;
	readonly bgYellow: CSPair;
	readonly bgBlue: CSPair;
	readonly bgCyan: CSPair;
	readonly bgMagenta: CSPair;
	readonly bgWhite: CSPair;

	/**
	Alias for `bgBlackBright`.
	*/
	readonly bgGray: CSPair;

	/**
	Alias for `bgBlackBright`.
	*/
	readonly bgGrey: CSPair;

	readonly bgBlackBright: CSPair;
	readonly bgRedBright: CSPair;
	readonly bgGreenBright: CSPair;
	readonly bgYellowBright: CSPair;
	readonly bgBlueBright: CSPair;
	readonly bgCyanBright: CSPair;
	readonly bgMagentaBright: CSPair;
	readonly bgWhiteBright: CSPair;
};

export type ConvertColor = {
	/**
	Convert from the RGB color space to the ANSI 256 color space.

	@param red - (`0...255`)
	@param green - (`0...255`)
	@param blue - (`0...255`)
	*/
	rgbToAnsi256(red: number, green: number, blue: number): number;

	/**
	Convert from the RGB HEX color space to the RGB color space.

	@param hex - A hexadecimal string containing RGB data.
	*/
	hexToRgb(hex: string): [red: number, green: number, blue: number];

	/**
	Convert from the RGB HEX color space to the ANSI 256 color space.

	@param hex - A hexadecimal string containing RGB data.
	*/
	hexToAnsi256(hex: string): number;

	/**
	Convert from the ANSI 256 color space to the ANSI 16 color space.

	@param code - A number representing the ANSI 256 color.
	*/
	ansi256ToAnsi(code: number): number;

	/**
	Convert from the RGB color space to the ANSI 16 color space.

	@param red - (`0...255`)
	@param green - (`0...255`)
	@param blue - (`0...255`)
	*/
	rgbToAnsi(red: number, green: number, blue: number): number;

	/**
	Convert from the RGB HEX color space to the ANSI 16 color space.

	@param hex - A hexadecimal string containing RGB data.
	*/
	hexToAnsi(hex: string): number;
};

/**
Basic modifier names.
*/
export type ModifierName = keyof Modifier;

/**
Basic foreground color names.

[More colors here.](https://github.com/chalk/chalk/blob/main/readme.md#256-and-truecolor-color-support)
*/
export type ForegroundColorName = keyof ForegroundColor;

/**
Basic background color names.

[More colors here.](https://github.com/chalk/chalk/blob/main/readme.md#256-and-truecolor-color-support)
*/
export type BackgroundColorName = keyof BackgroundColor;

/**
Basic color names. The combination of foreground and background color names.

[More colors here.](https://github.com/chalk/chalk/blob/main/readme.md#256-and-truecolor-color-support)
*/
export type ColorName = ForegroundColorName | BackgroundColorName;

/**
Basic modifier names.
*/
export const modifierNames: readonly ModifierName[];

/**
Basic foreground color names.
*/
export const foregroundColorNames: readonly ForegroundColorName[];

/**
Basic background color names.
*/
export const backgroundColorNames: readonly BackgroundColorName[];

/*
Basic color names. The combination of foreground and background color names.
*/
export const colorNames: readonly ColorName[];

declare const ansiStyles: {
	readonly modifier: Modifier;
	readonly color: ColorBase & ForegroundColor;
	readonly bgColor: ColorBase & BackgroundColor;
	readonly codes: ReadonlyMap<number, number>;
} & ForegroundColor & BackgroundColor & Modifier & ConvertColor;

export default ansiStyles;
```

## File: `index.js`
```javascript
const ANSI_BACKGROUND_OFFSET = 10;

const wrapAnsi16 = (offset = 0) => code => `\u001B[${code + offset}m`;

const wrapAnsi256 = (offset = 0) => code => `\u001B[${38 + offset};5;${code}m`;

const wrapAnsi16m = (offset = 0) => (red, green, blue) => `\u001B[${38 + offset};2;${red};${green};${blue}m`;

const blackBright = [90, 39];
const bgBlackBright = [100, 49];

const styles = {
	modifier: {
		reset: [0, 0],
		// 21 isn't widely supported and 22 does the same thing
		bold: [1, 22],
		dim: [2, 22],
		italic: [3, 23],
		underline: [4, 24],
		overline: [53, 55],
		inverse: [7, 27],
		hidden: [8, 28],
		strikethrough: [9, 29],
	},
	color: {
		black: [30, 39],
		red: [31, 39],
		green: [32, 39],
		yellow: [33, 39],
		blue: [34, 39],
		magenta: [35, 39],
		cyan: [36, 39],
		white: [37, 39],

		// Bright color
		blackBright,
		gray: blackBright,
		grey: blackBright,
		redBright: [91, 39],
		greenBright: [92, 39],
		yellowBright: [93, 39],
		blueBright: [94, 39],
		magentaBright: [95, 39],
		cyanBright: [96, 39],
		whiteBright: [97, 39],
	},
	bgColor: {
		bgBlack: [40, 49],
		bgRed: [41, 49],
		bgGreen: [42, 49],
		bgYellow: [43, 49],
		bgBlue: [44, 49],
		bgMagenta: [45, 49],
		bgCyan: [46, 49],
		bgWhite: [47, 49],

		// Bright color
		bgBlackBright,
		bgGray: bgBlackBright,
		bgGrey: bgBlackBright,
		bgRedBright: [101, 49],
		bgGreenBright: [102, 49],
		bgYellowBright: [103, 49],
		bgBlueBright: [104, 49],
		bgMagentaBright: [105, 49],
		bgCyanBright: [106, 49],
		bgWhiteBright: [107, 49],
	},
};

export const modifierNames = Object.keys(styles.modifier);
export const foregroundColorNames = Object.keys(styles.color);
export const backgroundColorNames = Object.keys(styles.bgColor);
export const colorNames = [...foregroundColorNames, ...backgroundColorNames];

function assembleStyles() {
	const codes = new Map();

	for (const [groupName, group] of Object.entries(styles)) {
		for (const [styleName, style] of Object.entries(group)) {
			styles[styleName] = {
				open: `\u001B[${style[0]}m`,
				close: `\u001B[${style[1]}m`,
			};

			group[styleName] = styles[styleName];

			codes.set(style[0], style[1]);
		}

		Object.defineProperty(styles, groupName, {
			value: group,
			enumerable: false,
		});
	}

	Object.defineProperty(styles, 'codes', {
		value: codes,
		enumerable: false,
	});

	styles.color.close = '\u001B[39m';
	styles.bgColor.close = '\u001B[49m';

	styles.color.ansi = wrapAnsi16();
	styles.color.ansi256 = wrapAnsi256();
	styles.color.ansi16m = wrapAnsi16m();
	styles.bgColor.ansi = wrapAnsi16(ANSI_BACKGROUND_OFFSET);
	styles.bgColor.ansi256 = wrapAnsi256(ANSI_BACKGROUND_OFFSET);
	styles.bgColor.ansi16m = wrapAnsi16m(ANSI_BACKGROUND_OFFSET);

	// From https://github.com/Qix-/color-convert/blob/3f0e0d4e92e235796ccb17f6e85c72094a651f49/conversions.js
	Object.defineProperties(styles, {
		rgbToAnsi256: {
			value(red, green, blue) {
				// We use the extended greyscale palette here, with the exception of
				// black and white. normal palette only has 4 greyscale shades.
				if (red === green && green === blue) {
					if (red < 8) {
						return 16;
					}

					if (red > 248) {
						return 231;
					}

					return Math.round(((red - 8) / 247) * 24) + 232;
				}

				return 16
					+ (36 * Math.round(red / 255 * 5))
					+ (6 * Math.round(green / 255 * 5))
					+ Math.round(blue / 255 * 5);
			},
			enumerable: false,
		},
		hexToRgb: {
			value(hex) {
				const matches = /[a-f\d]{6}|[a-f\d]{3}/i.exec(hex.toString(16));
				if (!matches) {
					return [0, 0, 0];
				}

				let [colorString] = matches;

				if (colorString.length === 3) {
					colorString = [...colorString].map(character => character + character).join('');
				}

				const integer = Number.parseInt(colorString, 16);

				return [
					/* eslint-disable no-bitwise */
					(integer >> 16) & 0xFF,
					(integer >> 8) & 0xFF,
					integer & 0xFF,
					/* eslint-enable no-bitwise */
				];
			},
			enumerable: false,
		},
		hexToAnsi256: {
			value: hex => styles.rgbToAnsi256(...styles.hexToRgb(hex)),
			enumerable: false,
		},
		ansi256ToAnsi: {
			value(code) {
				if (code < 8) {
					return 30 + code;
				}

				if (code < 16) {
					return 90 + (code - 8);
				}

				let red;
				let green;
				let blue;

				if (code >= 232) {
					red = (((code - 232) * 10) + 8) / 255;
					green = red;
					blue = red;
				} else {
					code -= 16;

					const remainder = code % 36;

					red = Math.floor(code / 36) / 5;
					green = Math.floor(remainder / 6) / 5;
					blue = (remainder % 6) / 5;
				}

				const value = Math.max(red, green, blue) * 2;

				if (value === 0) {
					return 30;
				}

				// eslint-disable-next-line no-bitwise
				let result = 30 + ((Math.round(blue) << 2) | (Math.round(green) << 1) | Math.round(red));

				if (value === 2) {
					result += 60;
				}

				return result;
			},
			enumerable: false,
		},
		rgbToAnsi: {
			value: (red, green, blue) => styles.ansi256ToAnsi(styles.rgbToAnsi256(red, green, blue)),
			enumerable: false,
		},
		hexToAnsi: {
			value: hex => styles.ansi256ToAnsi(styles.hexToAnsi256(hex)),
			enumerable: false,
		},
	});

	return styles;
}

const ansiStyles = assembleStyles();

export default ansiStyles;
```

## File: `index.test-d.ts`
```typescript
import {expectAssignable, expectError, expectType} from 'tsd';
import ansiStyles, {
	type BackgroundColorName,
	type ColorName,
	type CSPair,
	type ForegroundColorName,
	type ModifierName,
} from './index.js';

expectType<ReadonlyMap<number, number>>(ansiStyles.codes);

// - Static colors -
// -- Namespaced --
// --- Foreground color ---
expectType<CSPair>(ansiStyles.color.black);
expectType<CSPair>(ansiStyles.color.red);
expectType<CSPair>(ansiStyles.color.green);
expectType<CSPair>(ansiStyles.color.yellow);
expectType<CSPair>(ansiStyles.color.blue);
expectType<CSPair>(ansiStyles.color.cyan);
expectType<CSPair>(ansiStyles.color.magenta);
expectType<CSPair>(ansiStyles.color.white);

expectType<CSPair>(ansiStyles.color.gray);
expectType<CSPair>(ansiStyles.color.grey);

expectType<CSPair>(ansiStyles.color.blackBright);
expectType<CSPair>(ansiStyles.color.redBright);
expectType<CSPair>(ansiStyles.color.greenBright);
expectType<CSPair>(ansiStyles.color.yellowBright);
expectType<CSPair>(ansiStyles.color.blueBright);
expectType<CSPair>(ansiStyles.color.cyanBright);
expectType<CSPair>(ansiStyles.color.magentaBright);
expectType<CSPair>(ansiStyles.color.whiteBright);

expectType<string>(ansiStyles.color.close);

// --- Background color ---
expectType<CSPair>(ansiStyles.bgColor.bgBlack);
expectType<CSPair>(ansiStyles.bgColor.bgRed);
expectType<CSPair>(ansiStyles.bgColor.bgGreen);
expectType<CSPair>(ansiStyles.bgColor.bgYellow);
expectType<CSPair>(ansiStyles.bgColor.bgBlue);
expectType<CSPair>(ansiStyles.bgColor.bgCyan);
expectType<CSPair>(ansiStyles.bgColor.bgMagenta);
expectType<CSPair>(ansiStyles.bgColor.bgWhite);

expectType<CSPair>(ansiStyles.bgColor.bgGray);
expectType<CSPair>(ansiStyles.bgColor.bgGrey);

expectType<CSPair>(ansiStyles.bgColor.bgBlackBright);
expectType<CSPair>(ansiStyles.bgColor.bgRedBright);
expectType<CSPair>(ansiStyles.bgColor.bgGreenBright);
expectType<CSPair>(ansiStyles.bgColor.bgYellowBright);
expectType<CSPair>(ansiStyles.bgColor.bgBlueBright);
expectType<CSPair>(ansiStyles.bgColor.bgCyanBright);
expectType<CSPair>(ansiStyles.bgColor.bgMagentaBright);
expectType<CSPair>(ansiStyles.bgColor.bgWhiteBright);

expectType<string>(ansiStyles.bgColor.close);

// --- Modifiers ---
expectType<CSPair>(ansiStyles.modifier.bold);
expectType<CSPair>(ansiStyles.modifier.dim);
expectType<CSPair>(ansiStyles.modifier.hidden);
expectType<CSPair>(ansiStyles.modifier.inverse);
expectType<CSPair>(ansiStyles.modifier.italic);
expectType<CSPair>(ansiStyles.modifier.reset);
expectType<CSPair>(ansiStyles.modifier.strikethrough);
expectType<CSPair>(ansiStyles.modifier.underline);
expectType<CSPair>(ansiStyles.modifier.overline);

// -- Top level --
// --- Foreground color ---
expectType<CSPair>(ansiStyles.black);
expectType<CSPair>(ansiStyles.red);
expectType<CSPair>(ansiStyles.green);
expectType<CSPair>(ansiStyles.yellow);
expectType<CSPair>(ansiStyles.blue);
expectType<CSPair>(ansiStyles.cyan);
expectType<CSPair>(ansiStyles.magenta);
expectType<CSPair>(ansiStyles.white);

expectType<CSPair>(ansiStyles.gray);
expectType<CSPair>(ansiStyles.grey);

expectType<CSPair>(ansiStyles.blackBright);
expectType<CSPair>(ansiStyles.redBright);
expectType<CSPair>(ansiStyles.greenBright);
expectType<CSPair>(ansiStyles.yellowBright);
expectType<CSPair>(ansiStyles.blueBright);
expectType<CSPair>(ansiStyles.cyanBright);
expectType<CSPair>(ansiStyles.magentaBright);
expectType<CSPair>(ansiStyles.whiteBright);

// --- Background color ---
expectType<CSPair>(ansiStyles.bgBlack);
expectType<CSPair>(ansiStyles.bgRed);
expectType<CSPair>(ansiStyles.bgGreen);
expectType<CSPair>(ansiStyles.bgYellow);
expectType<CSPair>(ansiStyles.bgBlue);
expectType<CSPair>(ansiStyles.bgCyan);
expectType<CSPair>(ansiStyles.bgMagenta);
expectType<CSPair>(ansiStyles.bgWhite);

expectType<CSPair>(ansiStyles.bgGray);
expectType<CSPair>(ansiStyles.bgGrey);

expectType<CSPair>(ansiStyles.bgBlackBright);
expectType<CSPair>(ansiStyles.bgRedBright);
expectType<CSPair>(ansiStyles.bgGreenBright);
expectType<CSPair>(ansiStyles.bgYellowBright);
expectType<CSPair>(ansiStyles.bgBlueBright);
expectType<CSPair>(ansiStyles.bgCyanBright);
expectType<CSPair>(ansiStyles.bgMagentaBright);
expectType<CSPair>(ansiStyles.bgWhiteBright);

// --- Modifiers ---
expectType<CSPair>(ansiStyles.bold);
expectType<CSPair>(ansiStyles.dim);
expectType<CSPair>(ansiStyles.hidden);
expectType<CSPair>(ansiStyles.inverse);
expectType<CSPair>(ansiStyles.italic);
expectType<CSPair>(ansiStyles.reset);
expectType<CSPair>(ansiStyles.strikethrough);
expectType<CSPair>(ansiStyles.underline);

// --- ModifierName ---
expectAssignable<ModifierName>('strikethrough');
expectError<ModifierName>('delete');

// --- ForegroundColorName ---
expectAssignable<ForegroundColorName>('blue');
expectError<ForegroundColorName>('pink');

// --- ForegroundColorName ---
expectAssignable<BackgroundColorName>('bgBlue');
expectError<BackgroundColorName>('bgPink');

// --- ColorName ---
expectAssignable<ColorName>('blue');
expectAssignable<ColorName>('bgBlue');
expectError<ColorName>('pink');
expectError<ColorName>('bgPink');
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
	"name": "ansi-styles",
	"version": "6.2.3",
	"description": "ANSI escape codes for styling strings in the terminal",
	"license": "MIT",
	"repository": "chalk/ansi-styles",
	"funding": "https://github.com/chalk/ansi-styles?sponsor=1",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": "./index.js",
	"engines": {
		"node": ">=12"
	},
	"scripts": {
		"test": "xo && ava && tsd",
		"screenshot": "svg-term --command='node screenshot' --out=screenshot.svg --padding=3 --width=55 --height=3 --at=1000 --no-cursor"
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
		"log",
		"logging",
		"command-line",
		"text"
	],
	"devDependencies": {
		"ava": "^6.1.3",
		"svg-term-cli": "^2.1.1",
		"tsd": "^0.31.1",
		"xo": "^0.58.0"
	}
}
```

## File: `readme.md`
```markdown
# ansi-styles

> [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors_and_Styles) for styling strings in the terminal

You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

![](screenshot.png)

## Install

```sh
npm install ansi-styles
```

## Usage

```js
import styles from 'ansi-styles';

console.log(`${styles.green.open}Hello world!${styles.green.close}`);


// Color conversion between 256/truecolor
// NOTE: When converting from truecolor to 256 colors, the original color
//       may be degraded to fit the new color palette. This means terminals
//       that do not support 16 million colors will best-match the
//       original color.
console.log(`${styles.color.ansi(styles.rgbToAnsi(199, 20, 250))}Hello World${styles.color.close}`)
console.log(`${styles.color.ansi256(styles.rgbToAnsi256(199, 20, 250))}Hello World${styles.color.close}`)
console.log(`${styles.color.ansi16m(...styles.hexToRgb('#abcdef'))}Hello World${styles.color.close}`)
```

## API

### `open` and `close`

Each style has an `open` and `close` property.

### `modifierNames`, `foregroundColorNames`, `backgroundColorNames`, and `colorNames`

All supported style strings are exposed as an array of strings for convenience. `colorNames` is the combination of `foregroundColorNames` and `backgroundColorNames`.

This can be useful if you need to validate input:

```js
import {modifierNames, foregroundColorNames} from 'ansi-styles';

console.log(modifierNames.includes('bold'));
//=> true

console.log(foregroundColorNames.includes('pink'));
//=> false
```

## Styles

### Modifiers

- `reset`
- `bold`
- `dim`
- `italic` *(Not widely supported)*
- `underline`
- `overline` *Supported on VTE-based terminals, the GNOME terminal, mintty, and Git Bash.*
- `inverse`
- `hidden`
- `strikethrough` *(Not widely supported)*

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `blackBright` (alias: `gray`, `grey`)
- `redBright`
- `greenBright`
- `yellowBright`
- `blueBright`
- `magentaBright`
- `cyanBright`
- `whiteBright`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`
- `bgBlackBright` (alias: `bgGray`, `bgGrey`)
- `bgRedBright`
- `bgGreenBright`
- `bgYellowBright`
- `bgBlueBright`
- `bgMagentaBright`
- `bgCyanBright`
- `bgWhiteBright`

## Advanced usage

By default, you get a map of styles, but the styles are also available as groups. They are non-enumerable so they don't show up unless you access them explicitly. This makes it easier to expose only a subset in a higher-level module.

- `styles.modifier`
- `styles.color`
- `styles.bgColor`

###### Example

```js
import styles from 'ansi-styles';

console.log(styles.color.green.open);
```

Raw escape codes (i.e. without the CSI escape prefix `\u001B[` and render mode postfix `m`) are available under `styles.codes`, which returns a `Map` with the open codes as keys and close codes as values.

###### Example

```js
import styles from 'ansi-styles';

console.log(styles.codes.get(36));
//=> 39
```

## 16 / 256 / 16 million (TrueColor) support

`ansi-styles` allows converting between various color formats and ANSI escapes, with support for 16, 256 and [16 million colors](https://github.com/termstandard/colors).

The following color spaces are supported:

- `rgb`
- `hex`
- `ansi256`
- `ansi`

To use these, call the associated conversion function with the intended output, for example:

```js
import styles from 'ansi-styles';

styles.color.ansi(styles.rgbToAnsi(100, 200, 15)); // RGB to 16 color ansi foreground code
styles.bgColor.ansi(styles.hexToAnsi('#C0FFEE')); // HEX to 16 color ansi foreground code

styles.color.ansi256(styles.rgbToAnsi256(100, 200, 15)); // RGB to 256 color ansi foreground code
styles.bgColor.ansi256(styles.hexToAnsi256('#C0FFEE')); // HEX to 256 color ansi foreground code

styles.color.ansi16m(100, 200, 15); // RGB to 16 million color foreground code
styles.bgColor.ansi16m(...styles.hexToRgb('#C0FFEE')); // Hex (RGB) to 16 million color foreground code
```

## Related

- [ansi-escapes](https://github.com/sindresorhus/ansi-escapes) - ANSI escape codes for manipulating the terminal

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)

## For enterprise

Available as part of the Tidelift Subscription.

The maintainers of `ansi-styles` and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use. [Learn more.](https://tidelift.com/subscription/pkg/npm-ansi-styles?utm_source=npm-ansi-styles&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)
```

## File: `screenshot.js`
```javascript
import process from 'node:process';
import ansiStyles from './index.js';

const width = 55;
let lineLength = 0;

for (const [key, value] of Object.entries(ansiStyles)) {
	let code = value.open;
	let projectedLength = lineLength + key.length + 1;

	// We skip `overline` as almost no terminal supports it so we cannot show it off.
	if (
		key === 'reset'
			|| key === 'hidden'
			|| key === 'grey'
			|| key === 'bgGray'
			|| key === 'bgGrey'
			|| key === 'overline'
			|| key.endsWith('Bright')
	) {
		continue;
	}

	if (/^bg[^B]/.test(key)) {
		code = ansiStyles.black.open + code;
	}

	if (width < projectedLength) {
		process.stdout.write('\n');
		lineLength = 0;
		projectedLength = key.length + 1;
	}

	process.stdout.write(code + key + ansiStyles.reset.close + ' ');
	lineLength = projectedLength;
}
```

## File: `test/test.js`
```javascript
import test from 'ava';
import ansiStyles, {
	backgroundColorNames,
	colorNames,
	foregroundColorNames,
	modifierNames,
} from '../index.js';

test('return ANSI escape codes', t => {
	t.is(ansiStyles.green.open, '\u001B[32m');
	t.is(ansiStyles.bgGreen.open, '\u001B[42m');
	t.is(ansiStyles.green.close, '\u001B[39m');
	t.is(ansiStyles.gray.open, ansiStyles.grey.open);
});

test('group related codes into categories', t => {
	t.is(ansiStyles.color.magenta, ansiStyles.magenta);
	t.is(ansiStyles.bgColor.bgYellow, ansiStyles.bgYellow);
	t.is(ansiStyles.modifier.bold, ansiStyles.bold);
});

test('groups should not be enumerable', t => {
	t.not(Object.getOwnPropertyDescriptor(ansiStyles, 'modifier'), undefined);
	t.false(Object.keys(ansiStyles).includes('modifier'));
});

test('support conversion to ansi (16 colors)', t => {
	t.is(ansiStyles.color.ansi(ansiStyles.rgbToAnsi(255, 255, 255)), '\u001B[97m');
	t.is(ansiStyles.color.ansi(ansiStyles.hexToAnsi('#990099')), '\u001B[35m');
	t.is(ansiStyles.color.ansi(ansiStyles.hexToAnsi('#FF00FF')), '\u001B[95m');

	t.is(ansiStyles.bgColor.ansi(ansiStyles.rgbToAnsi(255, 255, 255)), '\u001B[107m');
	t.is(ansiStyles.bgColor.ansi(ansiStyles.hexToAnsi('#990099')), '\u001B[45m');
	t.is(ansiStyles.bgColor.ansi(ansiStyles.hexToAnsi('#FF00FF')), '\u001B[105m');
});

test('support conversion to ansi (256 colors)', t => {
	t.is(ansiStyles.color.ansi256(ansiStyles.rgbToAnsi256(255, 255, 255)), '\u001B[38;5;231m');
	t.is(ansiStyles.color.ansi256(ansiStyles.hexToAnsi256('#990099')), '\u001B[38;5;127m');
	t.is(ansiStyles.color.ansi256(ansiStyles.hexToAnsi256('#FF00FF')), '\u001B[38;5;201m');

	t.is(ansiStyles.bgColor.ansi256(ansiStyles.rgbToAnsi256(255, 255, 255)), '\u001B[48;5;231m');
	t.is(ansiStyles.bgColor.ansi256(ansiStyles.hexToAnsi256('#990099')), '\u001B[48;5;127m');
	t.is(ansiStyles.bgColor.ansi256(ansiStyles.hexToAnsi256('#FF00FF')), '\u001B[48;5;201m');
});

test('support conversion to ansi (16 million colors)', t => {
	t.is(ansiStyles.color.ansi16m(255, 255, 255), '\u001B[38;2;255;255;255m');
	t.is(ansiStyles.color.ansi16m(...ansiStyles.hexToRgb('#990099')), '\u001B[38;2;153;0;153m');
	t.is(ansiStyles.color.ansi16m(...ansiStyles.hexToRgb('#FF00FF')), '\u001B[38;2;255;0;255m');

	t.is(ansiStyles.bgColor.ansi16m(255, 255, 255), '\u001B[48;2;255;255;255m');
	t.is(ansiStyles.bgColor.ansi16m(...ansiStyles.hexToRgb('#990099')), '\u001B[48;2;153;0;153m');
	t.is(ansiStyles.bgColor.ansi16m(...ansiStyles.hexToRgb('#FF00FF')), '\u001B[48;2;255;0;255m');
});

test('16/256/16m color close escapes', t => {
	t.is(ansiStyles.color.close, '\u001B[39m');
	t.is(ansiStyles.bgColor.close, '\u001B[49m');
});

test('export raw ANSI escape codes', t => {
	t.is(ansiStyles.codes.get(0), 0);
	t.is(ansiStyles.codes.get(1), 22);
	t.is(ansiStyles.codes.get(91), 39);
	t.is(ansiStyles.codes.get(40), 49);
	t.is(ansiStyles.codes.get(100), 49);
});

test('rgb → truecolor is stubbed', t => {
	t.is(ansiStyles.color.ansi16m(123, 45, 67), '\u001B[38;2;123;45;67m');
});

test('non-styles should not be exported', t => {
	const isNonStyle = name => name === 'close' || name.startsWith('ansi');
	t.false(modifierNames.some(name => isNonStyle(name)));
	t.false(foregroundColorNames.some(name => isNonStyle(name)));
	t.false(backgroundColorNames.some(name => isNonStyle(name)));
	t.true(backgroundColorNames.every(name => name.startsWith('bg')));
	t.false(colorNames.some(name => isNonStyle(name)));
});
```

