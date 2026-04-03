---
id: chalk-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.611323
---

# KNOWLEDGE EXTRACT: chalk
> **Extracted on:** 2026-03-30 17:31:16
> **Source:** chalk

---

## File: `ansi-regex.md`
```markdown
# 📦 chalk/ansi-regex [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/ansi-regex


## Meta
- **Stars:** ⭐ 204 | **Forks:** 🍴 89
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-12
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Regular expression for matching ANSI escape codes

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `ansi-styles.md`
```markdown
# 📦 chalk/ansi-styles [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/ansi-styles


## Meta
- **Stars:** ⭐ 453 | **Forks:** 🍴 79
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
ANSI escape codes for styling strings in the terminal

## README (trích đầu)
```
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

Raw escape codes (i.e. without the CSI escape prefix `\u001B[` and render mode postfix `m`) are available under `styles.codes`, which returns a `Map` with the open codes as keys
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `chalk.md`
```markdown
# 📦 chalk/chalk [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/chalk


## Meta
- **Stars:** ⭐ 23089 | **Forks:** 🍴 940
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🖍 Terminal string styling done right

## README (trích đầu)
```
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

Exa
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `slice-ansi.md`
```markdown
# 📦 chalk/slice-ansi [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/slice-ansi


## Meta
- **Stars:** ⭐ 51 | **Forks:** 🍴 18
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Slice a string with ANSI escape codes

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `strip-ansi.md`
```markdown
# 📦 chalk/strip-ansi [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/strip-ansi


## Meta
- **Stars:** ⭐ 504 | **Forks:** 🍴 44
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Strip ANSI escape codes from a string

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `supports-color.md`
```markdown
# 📦 chalk/supports-color [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/supports-color


## Meta
- **Stars:** ⭐ 366 | **Forks:** 🍴 90
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-12
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Detect whether a terminal supports color

## README (trích đầu)
```
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
- [Josh Junon](https://
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `wrap-ansi.md`
```markdown
# 📦 chalk/wrap-ansi [🔖 PENDING/APPROVE]
🔗 https://github.com/chalk/wrap-ansi


## Meta
- **Stars:** ⭐ 136 | **Forks:** 🍴 28
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Wordwrap a string with ANSI escape codes

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

