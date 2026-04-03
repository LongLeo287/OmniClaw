---
id: github.com-chalk-chalk-9852230e-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:37.014127
---

# KNOWLEDGE EXTRACT: github.com_chalk_chalk_9852230e
> **Extracted on:** 2026-04-01 08:27:06
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519537/github.com_chalk_chalk_9852230e

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
coverage
.nyc_output
```

## File: `.npmrc`
```
package-lock=false
```

## File: `benchmark.js`
```javascript
/* globals suite, bench */
import chalk from './index.js';

suite('chalk', () => {
	const chalkRed = chalk.red;
	const chalkBgRed = chalk.bgRed;
	const chalkBlueBgRed = chalk.blue.bgRed;
	const chalkBlueBgRedBold = chalk.blue.bgRed.bold;

	const blueStyledString = 'the fox jumps' + chalk.blue('over the lazy dog') + '!';

	bench('1 style', () => {
		chalk.red('the fox jumps over the lazy dog');
	});

	bench('2 styles', () => {
		chalk.blue.bgRed('the fox jumps over the lazy dog');
	});

	bench('3 styles', () => {
		chalk.blue.bgRed.bold('the fox jumps over the lazy dog');
	});

	bench('cached: 1 style', () => {
		chalkRed('the fox jumps over the lazy dog');
	});

	bench('cached: 2 styles', () => {
		chalkBlueBgRed('the fox jumps over the lazy dog');
	});

	bench('cached: 3 styles', () => {
		chalkBlueBgRedBold('the fox jumps over the lazy dog');
	});

	bench('cached: 1 style with newline', () => {
		chalkRed('the fox jumps\nover the lazy dog');
	});

	bench('cached: 1 style nested intersecting', () => {
		chalkRed(blueStyledString);
	});

	bench('cached: 1 style nested non-intersecting', () => {
		chalkBgRed(blueStyledString);
	});

	bench('cached: 1 style template literal', () => {
		// eslint-disable-next-line no-unused-expressions
		chalkRed`the fox jumps over the lazy dog`;
	});

	bench('cached: nested styles template literal', () => {
		// eslint-disable-next-line no-unused-expressions
		chalkRed`the fox {bold jumps} over the {underline lazy} dog`;
	});
});
```

## File: `code-of-conduct.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at sindresorhus@gmail.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
```

## File: `contributing.md`
```markdown
# Contributing to Chalk

Please note that this project is released with a [Contributor Code of Conduct](../../../vault/archives/archive_legacy/AutoGPT/docs/content/code-of-conduct.md). By participating in this project you agree to abide by its terms.
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
	"name": "chalk",
	"version": "5.6.2",
	"description": "Terminal string styling done right",
	"license": "MIT",
	"repository": "chalk/chalk",
	"funding": "https://github.com/chalk/chalk?sponsor=1",
	"type": "module",
	"main": "./source/index.js",
	"exports": "./source/index.js",
	"imports": {
		"#ansi-styles": "./source/vendor/ansi-styles/index.js",
		"#supports-color": {
			"node": "./source/vendor/supports-color/index.js",
			"default": "./source/vendor/supports-color/browser.js"
		}
	},
	"types": "./source/index.d.ts",
	"sideEffects": false,
	"engines": {
		"node": "^12.17.0 || ^14.13 || >=16.0.0"
	},
	"scripts": {
		"test": "xo && c8 ava && tsd",
		"bench": "matcha benchmark.js"
	},
	"files": [
		"source",
		"!source/index.test-d.ts"
	],
	"keywords": [
		"color",
		"colour",
		"colors",
		"terminal",
		"console",
		"cli",
		"string",
		"ansi",
		"style",
		"styles",
		"tty",
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
		"@types/node": "^16.11.10",
		"ava": "^3.15.0",
		"c8": "^7.10.0",
		"color-convert": "^2.0.1",
		"execa": "^6.0.0",
		"log-update": "^5.0.0",
		"matcha": "^0.7.0",
		"tsd": "^0.19.0",
		"xo": "^0.57.0",
		"yoctodelay": "^2.0.0"
	},
	"xo": {
		"rules": {
			"unicorn/prefer-string-slice": "off",
			"@typescript-eslint/consistent-type-imports": "off",
			"@typescript-eslint/consistent-type-exports": "off",
			"@typescript-eslint/consistent-type-definitions": "off",
			"unicorn/expiring-todo-comments": "off"
		}
	},
	"c8": {
		"reporter": [
			"text",
			"lcov"
		],
		"exclude": [
			"source/vendor"
		]
	}
}
```

## File: `readme.md`
```markdown
<h1 align="center">
	<br>
	<br>
	<img width="320" src="media/logo.svg" alt="Chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

[![Coverage Status](https://codecov.io/gh/chalk/chalk/branch/main/graph/badge.svg)](https://codecov.io/gh/chalk/chalk)
[![npm dependents](https://badgen.net/npm/dependents/chalk)](https://www.npmjs.com/package/chalk?activeTab=dependents)
[![Downloads](https://badgen.net/npm/dt/chalk)](https://www.npmjs.com/package/chalk)

![](media/screenshot.png)

## Info

- [Why not switch to a smaller coloring package?](https://github.com/chalk/chalk?tab=readme-ov-file#why-not-switch-to-a-smaller-coloring-package)
- See [yoctocolors](https://github.com/sindresorhus/yoctocolors) for a smaller alternative

## Highlights

- Expressive API
- Highly performant
- No dependencies
- Ability to nest styles
- [256/Truecolor color support](#256-and-truecolor-color-support)
- Auto-detects color support
- Doesn't extend `String.prototype`
- Clean and focused
- Actively maintained
- [Used by ~115,000 packages](https://www.npmjs.com/browse/depended/chalk) as of July 4, 2024

## Install

```sh
npm install chalk
```

**IMPORTANT:** Chalk 5 is ESM. If you want to use Chalk with TypeScript or a build tool, you will probably want to use Chalk 4 for now. [Read more.](https://github.com/chalk/chalk/releases/tag/v5.0.0)

## Usage

```js
import chalk from 'chalk';

console.log(chalk.blue('Hello world!'));
```

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```js
import chalk from 'chalk';

const log = console.log;

// Combine styled and normal strings
log(chalk.blue('Hello') + ' World' + chalk.red('!'));

// Compose multiple styles using the chainable API
log(chalk.blue.bgRed.bold('Hello world!'));

// Pass in multiple arguments
log(chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz'));

// Nest styles
log(chalk.red('Hello', chalk.underline.bgBlue('world') + '!'));

// Nest styles of the same type even (color, underline, background)
log(chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
));

// ES2015 template literal
log(`
CPU: ${chalk.red('90%')}
RAM: ${chalk.green('40%')}
DISK: ${chalk.yellow('70%')}
`);

// Use RGB colors in terminal emulators that support it.
log(chalk.rgb(123, 45, 67).underline('Underlined reddish color'));
log(chalk.hex('#DEADED').bold('Bold gray!'));
```

Easily define your own themes:

```js
import chalk from 'chalk';

const error = chalk.bold.red;
const warning = chalk.hex('#FFA500'); // Orange color

console.log(error('Error!'));
console.log(warning('Warning!'));
```

Take advantage of console.log [string substitution](https://nodejs.org/brain/knowledge/docs_legacy/latest/api/console.html#console_console_log_data_args):

```js
import chalk from 'chalk';

const name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> 'Hello Sindre'
```

## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `chalk.red.yellow.green` is equivalent to `chalk.green`.

Multiple arguments will be separated by space.

### chalk.level

Specifies the level of color support.

Color support is automatically detected, but you can override it by setting the `level` property. You should however only do this in your own code as it applies globally to all Chalk consumers.

If you need to change this in a reusable module, create a new instance:

```js
import {Chalk} from 'chalk';

const customChalk = new Chalk({level: 0});
```

| Level | Description |
| :---: | :--- |
| `0` | All colors disabled |
| `1` | Basic color support (16 colors) |
| `2` | 256 color support |
| `3` | Truecolor support (16 million colors) |

### supportsColor

Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, use the environment variable `FORCE_COLOR=1` (level 1), `FORCE_COLOR=2` (level 2), or `FORCE_COLOR=3` (level 3) to forcefully enable color, or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.

Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.

### chalkStderr and supportsColorStderr

`chalkStderr` contains a separate instance configured with color support detected for `stderr` stream instead of `stdout`. Override rules from `supportsColor` apply to this too. `supportsColorStderr` is exposed for convenience.

### modifierNames, foregroundColorNames, backgroundColorNames, and colorNames

All supported style strings are exposed as an array of strings for convenience. `colorNames` is the combination of `foregroundColorNames` and `backgroundColorNames`.

This can be useful if you wrap Chalk and need to validate input:

```js
import {modifierNames, foregroundColorNames} from 'chalk';

console.log(modifierNames.includes('bold'));
//=> true

console.log(foregroundColorNames.includes('pink'));
//=> false
```

## Styles

### Modifiers

- `reset` - Reset the current style.
- `bold` - Make the text bold.
- `dim` - Make the text have lower opacity.
- `italic` - Make the text italic. *(Not widely supported)*
- `underline` - Put a horizontal line below the text. *(Not widely supported)*
- `overline` - Put a horizontal line above the text. *(Not widely supported)*
- `inverse` - Invert background and foreground colors.
- `hidden` - Print the text but make it invisible.
- `strikethrough` - Puts a horizontal line through the center of the text. *(Not widely supported)*
- `visible` - Print the text only when Chalk has a color level above zero. Can be useful for things that are purely cosmetic.

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

## 256 and Truecolor color support

Chalk supports 256 colors and [Truecolor](https://github.com/termstandard/colors) (16 million colors) on supported terminal apps.

Colors are downsampled from 16 million RGB values to an ANSI color format that is supported by the terminal emulator (or by specifying `{level: n}` as a Chalk option). For example, Chalk configured to run at level 1 (basic color support) will downsample an RGB value of #FF0000 (red) to 31 (ANSI escape for red).

Examples:

- `chalk.hex('#DEADED').underline('Hello, world!')`
- `chalk.rgb(15, 100, 204).inverse('Hello!')`

Background versions of these models are prefixed with `bg` and the first level of the module capitalized (e.g. `hex` for foreground colors and `bgHex` for background colors).

- `chalk.bgHex('#DEADED').underline('Hello, world!')`
- `chalk.bgRgb(15, 100, 204).inverse('Hello!')`

The following color models can be used:

- [`rgb`](https://en.wikipedia.org/wiki/RGB_color_model) - Example: `chalk.rgb(255, 136, 0).bold('Orange!')`
- [`hex`](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) - Example: `chalk.hex('#FF8800').bold('Orange!')`
- [`ansi256`](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) - Example: `chalk.bgAnsi256(194)('Honeydew, more or less')`

## Browser support

Since Chrome 69, ANSI escape codes are natively supported in the developer console.

## Windows

If you're on Windows, do yourself a favor and use [Windows Terminal](https://github.com/microsoft/terminal) instead of `cmd.exe`.

## FAQ

### Why not switch to a smaller coloring package?

Chalk may be larger, but there is a reason for that. It offers a more user-friendly API, well-documented types, supports millions of colors, and covers edge cases that smaller alternatives miss. Chalk is mature, reliable, and built to last.

But beyond the technical aspects, there's something more critical: trust and long-term maintenance. I have been active in open source for over a decade, and I'm committed to keeping Chalk maintained. Smaller packages might seem appealing now, but there's no guarantee they will be around for the long term, or that they won't become malicious over time.

Chalk is also likely already in your dependency tree (since 100K+ packages depend on it), so switching won’t save space—in fact, it might increase it. npm deduplicates dependencies, so multiple Chalk instances turn into one, but adding another package alongside it will increase your overall size.

If the goal is to clean up the ecosystem, switching away from Chalk won’t even make a dent. The real problem lies with packages that have very deep dependency trees (for example, those including a lot of polyfills). Chalk has no dependencies. It's better to focus on impactful changes rather than minor optimizations.

If absolute package size is important to you, I also maintain [yoctocolors](https://github.com/sindresorhus/yoctocolors), one of the smallest color packages out there.

*\- [Sindre](https://github.com/sindresorhus)*

### But the smaller coloring package has benchmarks showing it is faster

[Micro-benchmarks are flawed](https://sindresorhus.com/blog/micro-benchmark-fallacy) because they measure performance in unrealistic, isolated scenarios, often giving a distorted view of real-world performance. Don't believe marketing fluff. All the coloring packages are more than fast enough.

## Related

- [chalk-template](https://github.com/chalk/chalk-template) - [Tagged template literals](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Template_literals#tagged_templates) support for this module
- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [strip-ansi-stream](https://github.com/chalk/strip-ansi-stream) - Strip ANSI escape codes from a stream
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes
- [slice-ansi](https://github.com/chalk/slice-ansi) - Slice a string with ANSI escape codes
- [color-convert](https://github.com/qix-/color-convert) - Converts colors between different models
- [chalk-animation](https://github.com/bokub/chalk-animation) - Animate strings in the terminal
- [gradient-string](https://github.com/bokub/gradient-string) - Apply color gradients to strings
- [chalk-pipe](https://github.com/LitoMore/chalk-pipe) - Create chalk style schemes with simpler style strings
- [terminal-link](https://github.com/sindresorhus/terminal-link) - Create clickable links in the terminal

*(Not accepting additional entries)*

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)
```

## File: `examples/rainbow.js`
```javascript
import {setTimeout as delay} from 'node:timers/promises';
import convertColor from 'color-convert';
import updateLog from 'log-update';
import chalk from '../source/index.js';

const ignoreChars = /[^!-~]/g;

function rainbow(string, offset) {
	if (!string || string.length === 0) {
		return string;
	}

	const hueStep = 360 / string.replaceAll(ignoreChars, '').length;

	let hue = offset % 360;
	const characters = [];
	for (const character of string) {
		if (ignoreChars.test(character)) {
			characters.push(character);
		} else {
			characters.push(chalk.hex(convertColor.hsl.hex(hue, 100, 50))(character));
			hue = (hue + hueStep) % 360;
		}
	}

	return characters.join('');
}

async function animateString(string) {
	for (let index = 0; index < 360 * 5; index++) {
		updateLog(rainbow(string, index));
		await delay(2); // eslint-disable-line no-await-in-loop
	}
}

console.log();
await animateString('We hope you enjoy Chalk! <3');
console.log();
```

## File: `examples/screenshot.js`
```javascript
import process from 'node:process';
import styles from 'ansi-styles';
import chalk from '../source/index.js';

// Generates screenshot
for (const key of Object.keys(styles)) {
	let returnValue = key;

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
		returnValue = chalk.black(returnValue);
	}

	process.stdout.write(chalk[key](returnValue) + ' ');
}
```

## File: `source/index.d.ts`
```typescript
// TODO: Make it this when TS suports that.
// import {ModifierName, ForegroundColor, BackgroundColor, ColorName} from '#ansi-styles';
// import {ColorInfo, ColorSupportLevel} from '#supports-color';
import {
	ModifierName,
	ForegroundColorName,
	BackgroundColorName,
	ColorName,
} from './vendor/ansi-styles/index.js';
import {ColorInfo, ColorSupportLevel} from './vendor/supports-color/index.js';

export interface Options {
	/**
	Specify the color support for Chalk.

	By default, color support is automatically detected based on the environment.

	Levels:
	- `0` - All colors disabled.
	- `1` - Basic 16 colors support.
	- `2` - ANSI 256 colors support.
	- `3` - Truecolor 16 million colors support.
	*/
	readonly level?: ColorSupportLevel;
}

/**
Return a new Chalk instance.
*/
export const Chalk: new (options?: Options) => ChalkInstance; // eslint-disable-line @typescript-eslint/naming-convention

export interface ChalkInstance {
	(...text: unknown[]): string;

	/**
	The color support for Chalk.

	By default, color support is automatically detected based on the environment.

	Levels:
	- `0` - All colors disabled.
	- `1` - Basic 16 colors support.
	- `2` - ANSI 256 colors support.
	- `3` - Truecolor 16 million colors support.
	*/
	level: ColorSupportLevel;

	/**
	Use RGB values to set text color.

	@example
	```
	import chalk from 'chalk';

	chalk.rgb(222, 173, 237);
	```
	*/
	rgb: (red: number, green: number, blue: number) => this;

	/**
	Use HEX value to set text color.

	@param color - Hexadecimal value representing the desired color.

	@example
	```
	import chalk from 'chalk';

	chalk.hex('#DEADED');
	```
	*/
	hex: (color: string) => this;

	/**
	Use an [8-bit unsigned number](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) to set text color.

	@example
	```
	import chalk from 'chalk';

	chalk.ansi256(201);
	```
	*/
	ansi256: (index: number) => this;

	/**
	Use RGB values to set background color.

	@example
	```
	import chalk from 'chalk';

	chalk.bgRgb(222, 173, 237);
	```
	*/
	bgRgb: (red: number, green: number, blue: number) => this;

	/**
	Use HEX value to set background color.

	@param color - Hexadecimal value representing the desired color.

	@example
	```
	import chalk from 'chalk';

	chalk.bgHex('#DEADED');
	```
	*/
	bgHex: (color: string) => this;

	/**
	Use a [8-bit unsigned number](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) to set background color.

	@example
	```
	import chalk from 'chalk';

	chalk.bgAnsi256(201);
	```
	*/
	bgAnsi256: (index: number) => this;

	/**
	Modifier: Reset the current style.
	*/
	readonly reset: this;

	/**
	Modifier: Make the text bold.
	*/
	readonly bold: this;

	/**
	Modifier: Make the text have lower opacity.
	*/
	readonly dim: this;

	/**
	Modifier: Make the text italic. *(Not widely supported)*
	*/
	readonly italic: this;

	/**
	Modifier: Put a horizontal line below the text. *(Not widely supported)*
	*/
	readonly underline: this;

	/**
	Modifier: Put a horizontal line above the text. *(Not widely supported)*
	*/
	readonly overline: this;

	/**
	Modifier: Invert background and foreground colors.
	*/
	readonly inverse: this;

	/**
	Modifier: Print the text but make it invisible.
	*/
	readonly hidden: this;

	/**
	Modifier: Puts a horizontal line through the center of the text. *(Not widely supported)*
	*/
	readonly strikethrough: this;

	/**
	Modifier: Print the text only when Chalk has a color level above zero.

	Can be useful for things that are purely cosmetic.
	*/
	readonly visible: this;

	readonly black: this;
	readonly red: this;
	readonly green: this;
	readonly yellow: this;
	readonly blue: this;
	readonly magenta: this;
	readonly cyan: this;
	readonly white: this;

	/*
	Alias for `blackBright`.
	*/
	readonly gray: this;

	/*
	Alias for `blackBright`.
	*/
	readonly grey: this;

	readonly blackBright: this;
	readonly redBright: this;
	readonly greenBright: this;
	readonly yellowBright: this;
	readonly blueBright: this;
	readonly magentaBright: this;
	readonly cyanBright: this;
	readonly whiteBright: this;

	readonly bgBlack: this;
	readonly bgRed: this;
	readonly bgGreen: this;
	readonly bgYellow: this;
	readonly bgBlue: this;
	readonly bgMagenta: this;
	readonly bgCyan: this;
	readonly bgWhite: this;

	/*
	Alias for `bgBlackBright`.
	*/
	readonly bgGray: this;

	/*
	Alias for `bgBlackBright`.
	*/
	readonly bgGrey: this;

	readonly bgBlackBright: this;
	readonly bgRedBright: this;
	readonly bgGreenBright: this;
	readonly bgYellowBright: this;
	readonly bgBlueBright: this;
	readonly bgMagentaBright: this;
	readonly bgCyanBright: this;
	readonly bgWhiteBright: this;
}

/**
Main Chalk object that allows to chain styles together.

Call the last one as a method with a string argument.

Order doesn't matter, and later styles take precedent in case of a conflict.

This simply means that `chalk.red.yellow.green` is equivalent to `chalk.green`.
*/
declare const chalk: ChalkInstance;

export const supportsColor: ColorInfo;

export const chalkStderr: typeof chalk;
export const supportsColorStderr: typeof supportsColor;

export {
	ModifierName, ForegroundColorName, BackgroundColorName, ColorName,
	modifierNames, foregroundColorNames, backgroundColorNames, colorNames,
// } from '#ansi-styles';
} from './vendor/ansi-styles/index.js';

export {
	ColorInfo,
	ColorSupport,
	ColorSupportLevel,
// } from '#supports-color';
} from './vendor/supports-color/index.js';

// TODO: Remove these aliases in the next major version
/**
@deprecated Use `ModifierName` instead.

Basic modifier names.
*/
export type Modifiers = ModifierName;

/**
@deprecated Use `ForegroundColorName` instead.

Basic foreground color names.

[More colors here.](https://github.com/chalk/chalk/blob/main/readme.md#256-and-truecolor-color-support)
*/
export type ForegroundColor = ForegroundColorName;

/**
@deprecated Use `BackgroundColorName` instead.

Basic background color names.

[More colors here.](https://github.com/chalk/chalk/blob/main/readme.md#256-and-truecolor-color-support)
*/
export type BackgroundColor = BackgroundColorName;

/**
@deprecated Use `ColorName` instead.

Basic color names. The combination of foreground and background color names.

[More colors here.](https://github.com/chalk/chalk/blob/main/readme.md#256-and-truecolor-color-support)
*/
export type Color = ColorName;

/**
@deprecated Use `modifierNames` instead.

Basic modifier names.
*/
export const modifiers: readonly Modifiers[];

/**
@deprecated Use `foregroundColorNames` instead.

Basic foreground color names.
*/
export const foregroundColors: readonly ForegroundColor[];

/**
@deprecated Use `backgroundColorNames` instead.

Basic background color names.
*/
export const backgroundColors: readonly BackgroundColor[];

/**
@deprecated Use `colorNames` instead.

Basic color names. The combination of foreground and background color names.
*/
export const colors: readonly Color[];

export default chalk;
```

## File: `source/index.js`
```javascript
import ansiStyles from '#ansi-styles';
import supportsColor from '#supports-color';
import { // eslint-disable-line import/order
	stringReplaceAll,
	stringEncaseCRLFWithFirstIndex,
} from './utilities.js';

const {stdout: stdoutColor, stderr: stderrColor} = supportsColor;

const GENERATOR = Symbol('GENERATOR');
const STYLER = Symbol('STYLER');
const IS_EMPTY = Symbol('IS_EMPTY');

// `supportsColor.level` → `ansiStyles.color[name]` mapping
const levelMapping = [
	'ansi',
	'ansi',
	'ansi256',
	'ansi16m',
];

const styles = Object.create(null);

const applyOptions = (object, options = {}) => {
	if (options.level && !(Number.isInteger(options.level) && options.level >= 0 && options.level <= 3)) {
		throw new Error('The `level` option should be an integer from 0 to 3');
	}

	// Detect level if not set manually
	const colorLevel = stdoutColor ? stdoutColor.level : 0;
	object.level = options.level === undefined ? colorLevel : options.level;
};

export class Chalk {
	constructor(options) {
		// eslint-disable-next-line no-constructor-return
		return chalkFactory(options);
	}
}

const chalkFactory = options => {
	const chalk = (...strings) => strings.join(' ');
	applyOptions(chalk, options);

	Object.setPrototypeOf(chalk, createChalk.prototype);

	return chalk;
};

function createChalk(options) {
	return chalkFactory(options);
}

Object.setPrototypeOf(createChalk.prototype, Function.prototype);

for (const [styleName, style] of Object.entries(ansiStyles)) {
	styles[styleName] = {
		get() {
			const builder = createBuilder(this, createStyler(style.open, style.close, this[STYLER]), this[IS_EMPTY]);
			Object.defineProperty(this, styleName, {value: builder});
			return builder;
		},
	};
}

styles.visible = {
	get() {
		const builder = createBuilder(this, this[STYLER], true);
		Object.defineProperty(this, 'visible', {value: builder});
		return builder;
	},
};

const getModelAnsi = (model, level, type, ...arguments_) => {
	if (model === 'rgb') {
		if (level === 'ansi16m') {
			return ansiStyles[type].ansi16m(...arguments_);
		}

		if (level === 'ansi256') {
			return ansiStyles[type].ansi256(ansiStyles.rgbToAnsi256(...arguments_));
		}

		return ansiStyles[type].ansi(ansiStyles.rgbToAnsi(...arguments_));
	}

	if (model === 'hex') {
		return getModelAnsi('rgb', level, type, ...ansiStyles.hexToRgb(...arguments_));
	}

	return ansiStyles[type][model](...arguments_);
};

const usedModels = ['rgb', 'hex', 'ansi256'];

for (const model of usedModels) {
	styles[model] = {
		get() {
			const {level} = this;
			return function (...arguments_) {
				const styler = createStyler(getModelAnsi(model, levelMapping[level], 'color', ...arguments_), ansiStyles.color.close, this[STYLER]);
				return createBuilder(this, styler, this[IS_EMPTY]);
			};
		},
	};

	const bgModel = 'bg' + model[0].toUpperCase() + model.slice(1);
	styles[bgModel] = {
		get() {
			const {level} = this;
			return function (...arguments_) {
				const styler = createStyler(getModelAnsi(model, levelMapping[level], 'bgColor', ...arguments_), ansiStyles.bgColor.close, this[STYLER]);
				return createBuilder(this, styler, this[IS_EMPTY]);
			};
		},
	};
}

const proto = Object.defineProperties(() => {}, {
	...styles,
	level: {
		enumerable: true,
		get() {
			return this[GENERATOR].level;
		},
		set(level) {
			this[GENERATOR].level = level;
		},
	},
});

const createStyler = (open, close, parent) => {
	let openAll;
	let closeAll;
	if (parent === undefined) {
		openAll = open;
		closeAll = close;
	} else {
		openAll = parent.openAll + open;
		closeAll = close + parent.closeAll;
	}

	return {
		open,
		close,
		openAll,
		closeAll,
		parent,
	};
};

const createBuilder = (self, _styler, _isEmpty) => {
	// Single argument is hot path, implicit coercion is faster than anything
	// eslint-disable-next-line no-implicit-coercion
	const builder = (...arguments_) => applyStyle(builder, (arguments_.length === 1) ? ('' + arguments_[0]) : arguments_.join(' '));

	// We alter the prototype because we must return a function, but there is
	// no way to create a function with a different prototype
	Object.setPrototypeOf(builder, proto);

	builder[GENERATOR] = self;
	builder[STYLER] = _styler;
	builder[IS_EMPTY] = _isEmpty;

	return builder;
};

const applyStyle = (self, string) => {
	if (self.level <= 0 || !string) {
		return self[IS_EMPTY] ? '' : string;
	}

	let styler = self[STYLER];

	if (styler === undefined) {
		return string;
	}

	const {openAll, closeAll} = styler;
	if (string.includes('\u001B')) {
		while (styler !== undefined) {
			// Replace any instances already present with a re-opening code
			// otherwise only the part of the string until said closing code
			// will be colored, and the rest will simply be 'plain'.
			string = stringReplaceAll(string, styler.close, styler.open);

			styler = styler.parent;
		}
	}

	// We can move both next actions out of loop, because remaining actions in loop won't have
	// any/visible effect on parts we add here. Close the styling before a linebreak and reopen
	// after next line to fix a bleed issue on macOS: https://github.com/chalk/chalk/pull/92
	const lfIndex = string.indexOf('\n');
	if (lfIndex !== -1) {
		string = stringEncaseCRLFWithFirstIndex(string, closeAll, openAll, lfIndex);
	}

	return openAll + string + closeAll;
};

Object.defineProperties(createChalk.prototype, styles);

const chalk = createChalk();
export const chalkStderr = createChalk({level: stderrColor ? stderrColor.level : 0});

export {
	modifierNames,
	foregroundColorNames,
	backgroundColorNames,
	colorNames,

	// TODO: Remove these aliases in the next major version
	modifierNames as modifiers,
	foregroundColorNames as foregroundColors,
	backgroundColorNames as backgroundColors,
	colorNames as colors,
} from './vendor/ansi-styles/index.js';

export {
	stdoutColor as supportsColor,
	stderrColor as supportsColorStderr,
};

export default chalk;
```

## File: `source/index.test-d.ts`
```typescript
import {
	expectType,
	expectAssignable,
	expectError,
	expectDeprecated,
} from 'tsd';
import chalk, {
	Chalk,
	ChalkInstance,
	ColorInfo,
	ColorSupport,
	ColorSupportLevel,
	chalkStderr,
	supportsColor,
	supportsColorStderr,
	ModifierName,
	ForegroundColorName,
	BackgroundColorName,
	ColorName,
	Modifiers,
} from './index.js';

// - supportsColor -
expectType<ColorInfo>(supportsColor);
if (supportsColor) {
	expectType<ColorSupport>(supportsColor);
	expectType<ColorSupportLevel>(supportsColor.level);
	expectType<boolean>(supportsColor.hasBasic);
	expectType<boolean>(supportsColor.has256);
	expectType<boolean>(supportsColor.has16m);
}

// - stderr -
expectAssignable<ChalkInstance>(chalkStderr);
expectType<ColorInfo>(supportsColorStderr);
if (supportsColorStderr) {
	expectType<boolean>(supportsColorStderr.hasBasic);
	expectType<boolean>(supportsColorStderr.has256);
	expectType<boolean>(supportsColorStderr.has16m);
}

// -- `supportsColorStderr` is not a member of the Chalk interface --
expectError(chalk.reset.supportsColorStderr);

// -- `supportsColor` is not a member of the Chalk interface --
expectError(chalk.reset.supportsColor);

// - Chalk -
// -- Instance --
expectType<ChalkInstance>(new Chalk({level: 1}));

// -- Properties --
expectType<ColorSupportLevel>(chalk.level);

// -- Color methods --
expectType<ChalkInstance>(chalk.rgb(0, 0, 0));
expectType<ChalkInstance>(chalk.hex('#DEADED'));
expectType<ChalkInstance>(chalk.ansi256(0));
expectType<ChalkInstance>(chalk.bgRgb(0, 0, 0));
expectType<ChalkInstance>(chalk.bgHex('#DEADED'));
expectType<ChalkInstance>(chalk.bgAnsi256(0));

// -- Modifiers --
expectType<string>(chalk.reset('foo'));
expectType<string>(chalk.bold('foo'));
expectType<string>(chalk.dim('foo'));
expectType<string>(chalk.italic('foo'));
expectType<string>(chalk.underline('foo'));
expectType<string>(chalk.overline('foo'));
expectType<string>(chalk.inverse('foo'));
expectType<string>(chalk.hidden('foo'));
expectType<string>(chalk.strikethrough('foo'));
expectType<string>(chalk.visible('foo'));
expectType<string>(chalk.reset`foo`);
expectType<string>(chalk.bold`foo`);
expectType<string>(chalk.dim`foo`);
expectType<string>(chalk.italic`foo`);
expectType<string>(chalk.underline`foo`);
expectType<string>(chalk.inverse`foo`);
expectType<string>(chalk.hidden`foo`);
expectType<string>(chalk.strikethrough`foo`);
expectType<string>(chalk.visible`foo`);

// -- Colors --
expectType<string>(chalk.black('foo'));
expectType<string>(chalk.red('foo'));
expectType<string>(chalk.green('foo'));
expectType<string>(chalk.yellow('foo'));
expectType<string>(chalk.blue('foo'));
expectType<string>(chalk.magenta('foo'));
expectType<string>(chalk.cyan('foo'));
expectType<string>(chalk.white('foo'));
expectType<string>(chalk.gray('foo'));
expectType<string>(chalk.grey('foo'));
expectType<string>(chalk.blackBright('foo'));
expectType<string>(chalk.redBright('foo'));
expectType<string>(chalk.greenBright('foo'));
expectType<string>(chalk.yellowBright('foo'));
expectType<string>(chalk.blueBright('foo'));
expectType<string>(chalk.magentaBright('foo'));
expectType<string>(chalk.cyanBright('foo'));
expectType<string>(chalk.whiteBright('foo'));
expectType<string>(chalk.bgBlack('foo'));
expectType<string>(chalk.bgRed('foo'));
expectType<string>(chalk.bgGreen('foo'));
expectType<string>(chalk.bgYellow('foo'));
expectType<string>(chalk.bgBlue('foo'));
expectType<string>(chalk.bgMagenta('foo'));
expectType<string>(chalk.bgCyan('foo'));
expectType<string>(chalk.bgWhite('foo'));
expectType<string>(chalk.bgBlackBright('foo'));
expectType<string>(chalk.bgRedBright('foo'));
expectType<string>(chalk.bgGreenBright('foo'));
expectType<string>(chalk.bgYellowBright('foo'));
expectType<string>(chalk.bgBlueBright('foo'));
expectType<string>(chalk.bgMagentaBright('foo'));
expectType<string>(chalk.bgCyanBright('foo'));
expectType<string>(chalk.bgWhiteBright('foo'));
expectType<string>(chalk.black`foo`);
expectType<string>(chalk.red`foo`);
expectType<string>(chalk.green`foo`);
expectType<string>(chalk.yellow`foo`);
expectType<string>(chalk.blue`foo`);
expectType<string>(chalk.magenta`foo`);
expectType<string>(chalk.cyan`foo`);
expectType<string>(chalk.white`foo`);
expectType<string>(chalk.gray`foo`);
expectType<string>(chalk.grey`foo`);
expectType<string>(chalk.blackBright`foo`);
expectType<string>(chalk.redBright`foo`);
expectType<string>(chalk.greenBright`foo`);
expectType<string>(chalk.yellowBright`foo`);
expectType<string>(chalk.blueBright`foo`);
expectType<string>(chalk.magentaBright`foo`);
expectType<string>(chalk.cyanBright`foo`);
expectType<string>(chalk.whiteBright`foo`);
expectType<string>(chalk.bgBlack`foo`);
expectType<string>(chalk.bgRed`foo`);
expectType<string>(chalk.bgGreen`foo`);
expectType<string>(chalk.bgYellow`foo`);
expectType<string>(chalk.bgBlue`foo`);
expectType<string>(chalk.bgMagenta`foo`);
expectType<string>(chalk.bgCyan`foo`);
expectType<string>(chalk.bgWhite`foo`);
expectType<string>(chalk.bgBlackBright`foo`);
expectType<string>(chalk.bgRedBright`foo`);
expectType<string>(chalk.bgGreenBright`foo`);
expectType<string>(chalk.bgYellowBright`foo`);
expectType<string>(chalk.bgBlueBright`foo`);
expectType<string>(chalk.bgMagentaBright`foo`);
expectType<string>(chalk.bgCyanBright`foo`);
expectType<string>(chalk.bgWhiteBright`foo`);

// -- Complex --
expectType<string>(chalk.red.bgGreen.underline('foo'));
expectType<string>(chalk.underline.red.bgGreen('foo'));

// -- Complex template literal --
expectType<string>(chalk.underline``);
expectType<string>(chalk.red.bgGreen.bold`Hello {italic.blue ${name}}`);
expectType<string>(chalk.strikethrough.cyanBright.bgBlack`Works with {reset {bold numbers}} {bold.red ${1}}`);

// -- Modifiers types
expectAssignable<ModifierName>('strikethrough');
expectError<ModifierName>('delete');

// -- Foreground types
expectAssignable<ForegroundColorName>('red');
expectError<ForegroundColorName>('pink');

// -- Background types
expectAssignable<BackgroundColorName>('bgRed');
expectError<BackgroundColorName>('bgPink');

// -- Color types --
expectAssignable<ColorName>('red');
expectAssignable<ColorName>('bgRed');
expectError<ColorName>('hotpink');
expectError<ColorName>('bgHotpink');
```

## File: `source/utilities.js`
```javascript
// TODO: When targeting Node.js 16, use `String.prototype.replaceAll`.
export function stringReplaceAll(string, substring, replacer) {
	let index = string.indexOf(substring);
	if (index === -1) {
		return string;
	}

	const substringLength = substring.length;
	let endIndex = 0;
	let returnValue = '';
	do {
		returnValue += string.slice(endIndex, index) + substring + replacer;
		endIndex = index + substringLength;
		index = string.indexOf(substring, endIndex);
	} while (index !== -1);

	returnValue += string.slice(endIndex);
	return returnValue;
}

export function stringEncaseCRLFWithFirstIndex(string, prefix, postfix, index) {
	let endIndex = 0;
	let returnValue = '';
	do {
		const gotCR = string[index - 1] === '\r';
		returnValue += string.slice(endIndex, (gotCR ? index - 1 : index)) + prefix + (gotCR ? '\r\n' : '\n') + postfix;
		endIndex = index + 1;
		index = string.indexOf('\n', endIndex);
	} while (index !== -1);

	returnValue += string.slice(endIndex);
	return returnValue;
}
```

## File: `test/_fixture.js`
```javascript
import chalk, {chalkStderr} from '../source/index.js';

console.log(`${chalk.hex('#ff6159')('testout')} ${chalkStderr.hex('#ff6159')('testerr')}`);
```

## File: `test/chalk.js`
```javascript
import process from 'node:process';
import test from 'ava';
import chalk, {Chalk, chalkStderr} from '../source/index.js';

chalk.level = 3;
chalkStderr.level = 3;

console.log('TERM:', process.env.TERM || '[none]');
console.log('platform:', process.platform || '[unknown]');

test('don\'t add any styling when called as the base function', t => {
	t.is(chalk('foo'), 'foo');
});

test('support multiple arguments in base function', t => {
	t.is(chalk('hello', 'there'), 'hello there');
});

test('support automatic casting to string', t => {
	t.is(chalk(['hello', 'there']), 'hello,there');
	t.is(chalk(123), '123');

	t.is(chalk.bold(['foo', 'bar']), '\u001B[1mfoo,bar\u001B[22m');
	t.is(chalk.green(98_765), '\u001B[32m98765\u001B[39m');
});

test('style string', t => {
	t.is(chalk.underline('foo'), '\u001B[4mfoo\u001B[24m');
	t.is(chalk.red('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(chalk.bgRed('foo'), '\u001B[41mfoo\u001B[49m');
});

test('support applying multiple styles at once', t => {
	t.is(chalk.red.bgGreen.underline('foo'), '\u001B[31m\u001B[42m\u001B[4mfoo\u001B[24m\u001B[49m\u001B[39m');
	t.is(chalk.underline.red.bgGreen('foo'), '\u001B[4m\u001B[31m\u001B[42mfoo\u001B[49m\u001B[39m\u001B[24m');
});

test('support nesting styles', t => {
	t.is(
		chalk.red('foo' + chalk.underline.bgBlue('bar') + '!'),
		'\u001B[31mfoo\u001B[4m\u001B[44mbar\u001B[49m\u001B[24m!\u001B[39m',
	);
});

test('support nesting styles of the same type (color, underline, bg)', t => {
	t.is(
		chalk.red('a' + chalk.yellow('b' + chalk.green('c') + 'b') + 'c'),
		'\u001B[31ma\u001B[33mb\u001B[32mc\u001B[39m\u001B[31m\u001B[33mb\u001B[39m\u001B[31mc\u001B[39m',
	);
});

test('reset all styles with `.reset()`', t => {
	t.is(chalk.reset(chalk.red.bgGreen.underline('foo') + 'foo'), '\u001B[0m\u001B[31m\u001B[42m\u001B[4mfoo\u001B[24m\u001B[49m\u001B[39mfoo\u001B[0m');
});

test('support caching multiple styles', t => {
	const {red, green} = chalk.red;
	const redBold = red.bold;
	const greenBold = green.bold;

	t.not(red('foo'), green('foo'));
	t.not(redBold('bar'), greenBold('bar'));
	t.not(green('baz'), greenBold('baz'));
});

test('alias gray to grey', t => {
	t.is(chalk.grey('foo'), '\u001B[90mfoo\u001B[39m');
});

test('support variable number of arguments', t => {
	t.is(chalk.red('foo', 'bar'), '\u001B[31mfoo bar\u001B[39m');
});

test('support falsy values', t => {
	t.is(chalk.red(0), '\u001B[31m0\u001B[39m');
});

test('don\'t output escape codes if the input is empty', t => {
	t.is(chalk.red(), '');
	t.is(chalk.red.blue.black(), '');
});

test('keep Function.prototype methods', t => {
	t.is(Reflect.apply(chalk.grey, null, ['foo']), '\u001B[90mfoo\u001B[39m');
	t.is(chalk.reset(chalk.red.bgGreen.underline.bind(null)('foo') + 'foo'), '\u001B[0m\u001B[31m\u001B[42m\u001B[4mfoo\u001B[24m\u001B[49m\u001B[39mfoo\u001B[0m');
	t.is(chalk.red.blue.black.call(null), '');
});

test('line breaks should open and close colors', t => {
	t.is(chalk.grey('hello\nworld'), '\u001B[90mhello\u001B[39m\n\u001B[90mworld\u001B[39m');
});

test('line breaks should open and close colors with CRLF', t => {
	t.is(chalk.grey('hello\r\nworld'), '\u001B[90mhello\u001B[39m\r\n\u001B[90mworld\u001B[39m');
});

test('properly convert RGB to 16 colors on basic color terminals', t => {
	t.is(new Chalk({level: 1}).hex('#FF0000')('hello'), '\u001B[91mhello\u001B[39m');
	t.is(new Chalk({level: 1}).bgHex('#FF0000')('hello'), '\u001B[101mhello\u001B[49m');
});

test('properly convert RGB to 256 colors on basic color terminals', t => {
	t.is(new Chalk({level: 2}).hex('#FF0000')('hello'), '\u001B[38;5;196mhello\u001B[39m');
	t.is(new Chalk({level: 2}).bgHex('#FF0000')('hello'), '\u001B[48;5;196mhello\u001B[49m');
	t.is(new Chalk({level: 3}).bgHex('#FF0000')('hello'), '\u001B[48;2;255;0;0mhello\u001B[49m');
});

test('don\'t emit RGB codes if level is 0', t => {
	t.is(new Chalk({level: 0}).hex('#FF0000')('hello'), 'hello');
	t.is(new Chalk({level: 0}).bgHex('#FF0000')('hello'), 'hello');
});

test('supports blackBright color', t => {
	t.is(chalk.blackBright('foo'), '\u001B[90mfoo\u001B[39m');
});

test('sets correct level for chalkStderr and respects it', t => {
	t.is(chalkStderr.level, 3);
	t.is(chalkStderr.red.bold('foo'), '\u001B[31m\u001B[1mfoo\u001B[22m\u001B[39m');
});

test('keeps function prototype methods', t => {
	t.is(chalk.apply(chalk, ['foo']), 'foo');
	t.is(chalk.bind(chalk, 'foo')(), 'foo');
	t.is(chalk.call(chalk, 'foo'), 'foo');
});
```

## File: `test/instance.js`
```javascript
import test from 'ava';
import chalk, {Chalk} from '../source/index.js';

chalk.level = 1;

test('create an isolated context where colors can be disabled (by level)', t => {
	const instance = new Chalk({level: 0});
	t.is(instance.red('foo'), 'foo');
	t.is(chalk.red('foo'), '\u001B[31mfoo\u001B[39m');
	instance.level = 2;
	t.is(instance.red('foo'), '\u001B[31mfoo\u001B[39m');
});

test('the `level` option should be a number from 0 to 3', t => {
	/* eslint-disable no-new */
	t.throws(() => {
		new Chalk({level: 10});
	}, {message: /should be an integer from 0 to 3/});

	t.throws(() => {
		new Chalk({level: -1});
	}, {message: /should be an integer from 0 to 3/});
	/* eslint-enable no-new */
});
```

## File: `test/level.js`
```javascript
import {fileURLToPath} from 'node:url';
import test from 'ava';
import {execaNode} from 'execa';
import chalk from '../source/index.js';

chalk.level = 1;

test('don\'t output colors when manually disabled', t => {
	const oldLevel = chalk.level;
	chalk.level = 0;
	t.is(chalk.red('foo'), 'foo');
	chalk.level = oldLevel;
});

test('enable/disable colors based on overall chalk .level property, not individual instances', t => {
	const oldLevel = chalk.level;
	chalk.level = 1;
	const {red} = chalk;
	t.is(red.level, 1);
	chalk.level = 0;
	t.is(red.level, chalk.level);
	chalk.level = oldLevel;
});

test('propagate enable/disable changes from child colors', t => {
	const oldLevel = chalk.level;
	chalk.level = 1;
	const {red} = chalk;
	t.is(red.level, 1);
	t.is(chalk.level, 1);
	red.level = 0;
	t.is(red.level, 0);
	t.is(chalk.level, 0);
	chalk.level = 1;
	t.is(red.level, 1);
	t.is(chalk.level, 1);
	chalk.level = oldLevel;
});

test('disable colors if they are not supported', async t => {
	const {stdout} = await execaNode(fileURLToPath(new URL('_fixture.js', import.meta.url)));
	t.is(stdout, 'testout testerr');
});
```

## File: `test/no-color-support.js`
```javascript
import test from 'ava';
import chalk from '../source/index.js';

// TODO: Do this when ESM supports loader hooks
// Spoof supports-color
// require('./_supports-color')(__dirname, {
// 	stdout: {
// 		level: 0,
// 		hasBasic: false,
// 		has256: false,
// 		has16m: false
// 	},
// 	stderr: {
// 		level: 0,
// 		hasBasic: false,
// 		has256: false,
// 		has16m: false
// 	}
// });

test('colors can be forced by using chalk.level', t => {
	chalk.level = 1;
	t.is(chalk.green('hello'), '\u001B[32mhello\u001B[39m');
});
```

## File: `test/visible.js`
```javascript
import test from 'ava';
import chalk, {Chalk} from '../source/index.js';

chalk.level = 1;

test('visible: normal output when level > 0', t => {
	const instance = new Chalk({level: 3});
	t.is(instance.visible.red('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.red.visible('foo'), '\u001B[31mfoo\u001B[39m');
});

test('visible: no output when level is too low', t => {
	const instance = new Chalk({level: 0});
	t.is(instance.visible.red('foo'), '');
	t.is(instance.red.visible('foo'), '');
});

test('test switching back and forth between level == 0 and level > 0', t => {
	const instance = new Chalk({level: 3});
	t.is(instance.red('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.visible.red('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.red.visible('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.visible('foo'), 'foo');
	t.is(instance.red('foo'), '\u001B[31mfoo\u001B[39m');

	instance.level = 0;
	t.is(instance.red('foo'), 'foo');
	t.is(instance.visible('foo'), '');
	t.is(instance.visible.red('foo'), '');
	t.is(instance.red.visible('foo'), '');
	t.is(instance.red('foo'), 'foo');

	instance.level = 3;
	t.is(instance.red('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.visible.red('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.red.visible('foo'), '\u001B[31mfoo\u001B[39m');
	t.is(instance.visible('foo'), 'foo');
	t.is(instance.red('foo'), '\u001B[31mfoo\u001B[39m');
});
```

