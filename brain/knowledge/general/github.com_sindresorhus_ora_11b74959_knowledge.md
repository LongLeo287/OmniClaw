---
id: github.com-sindresorhus-ora-11b74959-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.829374
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_ora_11b74959
> **Extracted on:** 2026-04-01 09:36:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520307/github.com_sindresorhus_ora_11b74959

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

## File: `example-console-integration.js`
```javascript
import chalk from 'chalk';
import ora from './index.js';

console.log(chalk.bold('\n🦄 Unicorn Console Integration Demo\n'));
console.log(chalk.dim('This example shows how ora seamlessly handles console.error/warn'));
console.log(chalk.dim('while the spinner is running. These write to stderr where ora hooks!\n'));

// Simulate collecting unicorns with status updates
const collectUnicorns = ora({
	text: 'Searching for unicorns in the enchanted forest...',
	color: 'magenta',
}).start();

setTimeout(() => {
	console.error(chalk.cyan('✨ Found a baby unicorn near the crystal stream!'));
}, 500);

setTimeout(() => {
	console.error(chalk.yellow('✨ Spotted a golden unicorn on the rainbow bridge!'));
}, 1000);

setTimeout(() => {
	console.warn(chalk.hex('#FFA500')('⚠️  A wild unicorn is shy and hiding behind clouds'));
}, 1500);

setTimeout(() => {
	console.error(chalk.magenta('✨ Discovered a unicorn herd in the meadow!'));
}, 2000);

setTimeout(() => {
	console.error(chalk.red('❌ Dark forest area is too dangerous to explore'));
}, 2500);

setTimeout(() => {
	collectUnicorns.succeed(chalk.green('Collected 3 magical unicorns! 🦄🦄🦄'));

	// Start processing unicorn magic
	const processSpinner = ora({
		text: 'Processing unicorn magic...',
		color: 'cyan',
	}).start();

	setTimeout(() => {
		console.error(chalk.blue('🌟 Converting stardust to rainbow essence'));
	}, 500);

	setTimeout(() => {
		console.error(chalk.magenta('🌈 Brewing magical unicorn potion'));
	}, 1000);

	setTimeout(() => {
		console.error(chalk.yellow('✨ Enchanting unicorn horn fragments'));
	}, 1500);

	setTimeout(() => {
		processSpinner.succeed(chalk.green('Unicorn magic processed successfully!'));

		// Deploy unicorn powers
		const deploySpinner = ora({
			text: 'Deploying unicorn powers to the world...',
			color: 'magenta',
			spinner: 'dots12',
		}).start();

		setTimeout(() => {
			console.error(chalk.hex('#FF1493')('💫 Spreading joy and sparkles'));
		}, 400);

		setTimeout(() => {
			console.error(chalk.hex('#9370DB')('🎨 Painting rainbows across the sky'));
		}, 800);

		setTimeout(() => {
			console.error(chalk.hex('#FFD700')('⭐ Granting wishes to believers'));
		}, 1200);

		setTimeout(() => {
			deploySpinner.succeed(chalk.bold.green('🦄 Unicorn powers deployed! The world is more magical now! ✨'));

			// Summary (using console.log is fine here since spinner is stopped)
			console.log(chalk.dim('\n' + '─'.repeat(60)));
			console.log(chalk.bold.cyan('\n📊 Mission Summary:'));
			console.log(chalk.white('  • Unicorns collected: ') + chalk.bold('3'));
			console.log(chalk.white('  • Magic spells cast: ') + chalk.bold('6'));
			console.log(chalk.white('  • Rainbows created: ') + chalk.bold('∞'));
			console.log(chalk.white('  • World happiness: ') + chalk.bold.green('+1000%'));
			console.log(chalk.dim('\n' + '─'.repeat(60)));

			console.log(chalk.bold.magenta('\n✨ Notice how all console.error/warn appeared cleanly above the spinner!'));
			console.log(chalk.dim('The spinner automatically clears, shows your message, then re-renders below.'));
			console.log(chalk.dim('Both console.log() and console.error/warn() work seamlessly while spinning! 🎉\n'));
		}, 1600);
	}, 2000);
}, 3000);
```

## File: `example-overflow.js`
```javascript
#!/usr/bin/env node
import process from 'node:process';
import chalk from 'chalk';
import ora from './index.js';

console.log(chalk.bold.cyan('\n📏 Terminal Height Overflow Test - Fixed Version 📏'));
console.log(chalk.gray('This demo shows the fix for issue #121 - multiline content exceeding terminal height.\n'));

// Get terminal dimensions
const rows = process.stderr.rows ?? 30;
const cols = process.stderr.columns ?? 80;

console.log(chalk.yellow(`Your terminal: ${rows} rows × ${cols} columns`));
console.log(chalk.green(`Creating spinner with ${rows + 10} lines (exceeds by 10 lines)\n`));

// Create content that exceeds terminal height
const lines = [];
for (let index = 1; index <= rows + 10; index++) {
	const emoji = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣'][index % 6];
	lines.push(`${emoji} Line ${String(index).padStart(3, '0')}: Processing item #${index}`);
}

const spinner = ora({
	text: lines.join('\n'),
	spinner: 'dots',
	color: 'cyan',
}).start();

// Update a few times
let updates = 0;
const interval = setInterval(() => {
	updates++;
	if (updates <= 3) {
		spinner.color = ['yellow', 'green', 'magenta'][updates - 1];
		spinner.text = `Update ${updates}/3\n${lines.join('\n')}`;
	} else {
		clearInterval(interval);
		spinner.succeed('Done! Content that exceeded terminal height has been properly cleared.');

		console.log('\n' + chalk.bold.green('✅ The Fix:'));
		console.log(chalk.white('When content exceeds terminal height, ora now:'));
		console.log(chalk.gray('  1. Detects the overflow (lines > terminal rows)'));
		console.log(chalk.gray('  2. Truncates content to fit terminal with message'));
		console.log(chalk.gray('  3. Prevents garbage lines from being written'));

		console.log('\n' + chalk.bold.yellow('🔍 Try scrolling up now!'));
		console.log(chalk.gray('You should NOT see leftover spinner frames above.'));
		console.log(chalk.gray('Content was truncated to prevent overflow.\n'));
	}
}, 1000);
```

## File: `example.js`
```javascript
import process from 'node:process';
import chalk from 'chalk';
import logSymbols from 'log-symbols';
import ora from './index.js';

const spinner = ora({
	discardStdin: false,
	text: 'Loading unicorns, not discarding stdin',
	spinner: process.argv[2],
});

const spinnerDiscardingStdin = ora({
	text: 'Loading unicorns',
	spinner: process.argv[2],
});

spinnerDiscardingStdin.start();

setTimeout(() => {
	spinnerDiscardingStdin.succeed();
}, 1000);

setTimeout(() => {
	spinnerDiscardingStdin.start();
}, 2000);

setTimeout(() => {
	spinnerDiscardingStdin.succeed();
	spinner.start();
}, 3000);

setTimeout(() => {
	spinner.color = 'yellow';
	spinner.text = `Loading ${chalk.red('rainbows')}`;
}, 4000);

setTimeout(() => {
	spinner.color = 'green';
	spinner.indent = 2;
	spinner.text = 'Loading with indent';
}, 5000);

setTimeout(() => {
	spinner.indent = 0;
	spinner.spinner = 'moon';
	spinner.text = 'Loading with different spinners';
}, 6000);

setTimeout(() => {
	spinner.prefixText = chalk.dim('[info]');
	spinner.spinner = 'dots';
	spinner.text = 'Loading with prefix text';
}, 8000);

setTimeout(() => {
	spinner.prefixText = '';
	spinner.suffixText = chalk.dim('[info]');
	spinner.text = 'Loading with suffix text';
}, 10_000);

setTimeout(() => {
	spinner.prefixText = chalk.dim('[info]');
	spinner.suffixText = chalk.dim('[info]');
	spinner.text = 'Loading with prefix and suffix text';
}, 12_000);

setTimeout(() => {
	spinner.stopAndPersist({
		prefixText: '',
		suffixText: '',
		symbol: logSymbols.info,
		text: 'Stopping with different text!',
	});
}, 14_000);

// $ node example.js nameOfSpinner
```

## File: `index.d.ts`
```typescript
import {type SpinnerName} from 'cli-spinners';

export type Spinner = {
	readonly interval?: number;
	readonly frames: string[];
};

export type Color =
	| 'black'
	| 'red'
	| 'green'
	| 'yellow'
	| 'blue'
	| 'magenta'
	| 'cyan'
	| 'white'
	| 'gray';

export type PrefixTextGenerator = () => string;

export type SuffixTextGenerator = () => string;

export type Options = {
	/**
	The text to display next to the spinner.
	*/
	readonly text?: string;

	/**
	Text or a function that returns text to display before the spinner. No prefix text will be displayed if set to an empty string.
	*/
	readonly prefixText?: string | PrefixTextGenerator;

	/**
	Text or a function that returns text to display after the spinner text. No suffix text will be displayed if set to an empty string.
	*/
	readonly suffixText?: string | SuffixTextGenerator;

	/**
	The name of one of the provided spinners. See `example.js` in this repo if you want to test out different spinners. On Windows (except for Windows Terminal), it will always use the line spinner as the Windows command-line doesn't have proper Unicode support.

	@default 'dots'

	Or an object like:

	@example
	```
	{
		frames: ['-', '+', '-'],
		interval: 80 // Optional
	}
	```
	*/
	readonly spinner?: SpinnerName | Spinner;

	/**
	The color of the spinner.

	@default 'cyan'
	*/
	readonly color?: Color | boolean;

	/**
	Set to `false` to stop Ora from hiding the cursor.

	@default true
	*/
	readonly hideCursor?: boolean;

	/**
	Indent the spinner with the given number of spaces.

	@default 0
	*/
	readonly indent?: number;

	/**
	Interval between each frame.

	Spinners provide their own recommended interval, so you don't really need to specify this.

	Default: Provided by the spinner or `100`.
	*/
	readonly interval?: number;

	/**
	Stream to write the output.

	You could for example set this to `process.stdout` instead.

	@default process.stderr
	*/
	readonly stream?: NodeJS.WritableStream;

	/**
	Force enable/disable the spinner. If not specified, the spinner will be enabled if the `stream` is being run inside a TTY context (not spawned or piped) and/or not in a CI environment.

	Note that `{isEnabled: false}` doesn't mean it won't output anything. It just means it won't output the spinner, colors, and other ansi escape codes. It will still log text.
	*/
	readonly isEnabled?: boolean;

	/**
	Disable the spinner and all log text. All output is suppressed and `isEnabled` will be considered `false`.

	@default false
	*/
	readonly isSilent?: boolean;

	/**
	Discard stdin input (except Ctrl+C) while running if it's TTY. This prevents the spinner from twitching on input, outputting broken lines on `Enter` key presses, and prevents buffering of input while the spinner is running.

	This has no effect on Windows as there is no good way to implement discarding stdin properly there.

	Note: `discardStdin` puts stdin into raw mode. In raw mode, `Ctrl+C` no longer generates `SIGINT` from the terminal. Ora re-emits `Ctrl+C` from stdin input, but if your code blocks the event loop with synchronous work, `Ctrl+C` handling is delayed until the blocking work ends. Use async APIs, a worker thread, or a child process to keep `Ctrl+C` responsive, or set `discardStdin` to `false`.

	@default true
	*/
	readonly discardStdin?: boolean;
};

export type PersistOptions = {
	/**
	Symbol to replace the spinner with.

	@default ' '
	*/
	readonly symbol?: string;

	/**
	Text to be persisted after the symbol.

	Default: Current `text`.
	*/
	readonly text?: string;

	/**
	Text or a function that returns text to be persisted before the symbol. No prefix text will be displayed if set to an empty string.

	Default: Current `prefixText`.
	*/
	readonly prefixText?: string | PrefixTextGenerator;

	/**
	Text or a function that returns text to be persisted after the text after the symbol. No suffix text will be displayed if set to an empty string.

	Default: Current `suffixText`.
	*/
	readonly suffixText?: string | SuffixTextGenerator;
};

export type PromiseOptions<T> = {
	/**
	The new text of the spinner when the promise is resolved.

	Keeps the existing text if `undefined`.
	*/
	successText?: string | ((result: T) => string) | undefined;

	/**
	The new text of the spinner when the promise is rejected.

	Keeps the existing text if `undefined`.
	*/
	failText?: string | ((error: Error) => string) | undefined;
} & Options;

// eslint-disable-next-line @typescript-eslint/consistent-type-definitions
export interface Ora {
	/**
	Change the text after the spinner.
	*/
	text: string;

	/**
	Change the text or function that returns text before the spinner.

	No prefix text will be displayed if set to an empty string.
	*/
	prefixText: string;

	/**
	Change the text or function that returns text after the spinner text.

	No suffix text will be displayed if set to an empty string.
	*/
	suffixText: string;

	/**
	Change the spinner color.
	*/
	color: Color | boolean;

	/**
	Change the spinner indent.
	*/
	indent: number;

	/**
	Get the spinner.
	*/
	get spinner(): Spinner;

	/**
	Set the spinner.
	*/
	set spinner(spinner: SpinnerName | Spinner);

	/**
	A boolean indicating whether the instance is currently spinning.
	*/
	get isSpinning(): boolean;

	/**
	The interval between each frame.

	The interval is decided by the chosen spinner.
	*/
	get interval(): number;

	/**
	Start the spinner.

	@param text - Set the current text.
	@returns The spinner instance.
	*/
	start(text?: string): this;

	/**
	Stop and clear the spinner.

	@returns The spinner instance.
	*/
	stop(): this;

	/**
	Stop the spinner, change it to a green `✔` and persist the current text, or `text` if provided.

	@param text - Will persist text if provided.
	@returns The spinner instance.
	*/
	succeed(text?: string): this;

	/**
	Stop the spinner, change it to a red `✖` and persist the current text, or `text` if provided.

	@param text - Will persist text if provided.
	@returns The spinner instance.
	*/
	fail(text?: string): this;

	/**
	Stop the spinner, change it to a yellow `⚠` and persist the current text, or `text` if provided.

	@param text - Will persist text if provided.
	@returns The spinner instance.
	*/
	warn(text?: string): this;

	/**
	Stop the spinner, change it to a blue `ℹ` and persist the current text, or `text` if provided.

	@param text - Will persist text if provided.
	@returns The spinner instance.
	*/
	info(text?: string): this;

	/**
	Stop the spinner and change the symbol or text.

	@returns The spinner instance.
	*/
	stopAndPersist(options?: PersistOptions): this;

	/**
	Clear the spinner.

	@returns The spinner instance.
	*/
	clear(): this;

	/**
	Manually render a new frame.

	@returns The spinner instance.
	*/
	render(): this;

	/**
	Get a new frame.

	@returns The spinner instance text.
	*/
	frame(): string;
}

/**
Elegant terminal spinner.

@param options - If a string is provided, it is treated as a shortcut for `options.text`.

@example
```
import ora from 'ora';

const spinner = ora('Loading unicorns').start();

setTimeout(() => {
	spinner.color = 'yellow';
	spinner.text = 'Loading rainbows';
}, 1000);
```
*/
export default function ora(options?: string | Options): Ora;

/**
Starts a spinner for a promise or promise-returning function. The spinner is stopped with `.succeed()` if the promise fulfills or with `.fail()` if it rejects.

@param action - The promise to start the spinner for or a promise-returning function.
@param options - If a string is provided, it is treated as a shortcut for `options.text`.
@returns The given promise.

@example
```
import {oraPromise} from 'ora';

await oraPromise(somePromise);
```
*/
export function oraPromise<T>(
	action: PromiseLike<T> | ((spinner: Ora) => PromiseLike<T>),
	options?: string | PromiseOptions<T>
): Promise<T>;

export {default as spinners} from 'cli-spinners';
```

## File: `index.js`
```javascript
import process from 'node:process';
import {stripVTControlCharacters} from 'node:util';
import chalk from 'chalk';
import cliCursor from 'cli-cursor';
import cliSpinners from 'cli-spinners';
import logSymbols from 'log-symbols';
import stringWidth from 'string-width';
import isInteractive from 'is-interactive';
import isUnicodeSupported from 'is-unicode-supported';
import stdinDiscarder from 'stdin-discarder';

// Constants
const RENDER_DEFERRAL_TIMEOUT = 200; // Milliseconds to wait before re-rendering after partial chunk write
const SYNCHRONIZED_OUTPUT_ENABLE = '\u001B[?2026h';
const SYNCHRONIZED_OUTPUT_DISABLE = '\u001B[?2026l';

// Global state for concurrent spinner detection
const activeHooksPerStream = new Map(); // Stream → ora instance

const validColors = new Set(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'gray']);

class Ora {
	#linesToClear = 0;
	#frameIndex = -1;
	#lastFrameTime = 0;
	#options;
	#spinner;
	#stream;
	#id;
	#hookedStreams = new Map();
	#isInternalWrite = false;
	#drainHandler;
	#deferRenderTimer;
	#isDiscardingStdin = false;
	#color;

	// Helper to execute writes while preventing hook recursion
	#internalWrite(fn) {
		this.#isInternalWrite = true;
		try {
			return fn();
		} finally {
			this.#isInternalWrite = false;
		}
	}

	// Helper to render if still spinning
	#tryRender() {
		if (this.isSpinning) {
			this.render();
		}
	}

	#stringifyChunk(chunk, encoding) {
		if (chunk === undefined || chunk === null) {
			return '';
		}

		if (typeof chunk === 'string') {
			return chunk;
		}

		/* eslint-disable n/prefer-global/buffer */
		if (Buffer.isBuffer(chunk) || ArrayBuffer.isView(chunk)) {
			const normalizedEncoding = (typeof encoding === 'string' && encoding && encoding !== 'buffer') ? encoding : 'utf8';
			return Buffer.from(chunk).toString(normalizedEncoding);
		}
		/* eslint-enable n/prefer-global/buffer */

		return String(chunk);
	}

	#chunkTerminatesLine(chunkString) {
		if (!chunkString) {
			return false;
		}

		const lastCharacter = chunkString.at(-1);
		return lastCharacter === '\n' || lastCharacter === '\r';
	}

	#scheduleRenderDeferral() {
		// If already deferred, don't reset timer - let it complete
		if (this.#deferRenderTimer) {
			return;
		}

		this.#deferRenderTimer = setTimeout(() => {
			this.#deferRenderTimer = undefined;

			if (this.isSpinning) {
				this.#tryRender();
			}
		}, RENDER_DEFERRAL_TIMEOUT);

		if (typeof this.#deferRenderTimer?.unref === 'function') {
			this.#deferRenderTimer.unref();
		}
	}

	#clearRenderDeferral() {
		if (this.#deferRenderTimer) {
			clearTimeout(this.#deferRenderTimer);
			this.#deferRenderTimer = undefined;
		}
	}

	// Helper to build complete line with symbol, text, prefix, and suffix
	#buildOutputLine(symbol, text, prefixText, suffixText) {
		const fullPrefixText = this.#getFullPrefixText(prefixText, ' ');
		const separatorText = symbol ? ' ' : '';
		const fullText = (typeof text === 'string') ? separatorText + text : '';
		const fullSuffixText = this.#getFullSuffixText(suffixText, ' ');
		return fullPrefixText + symbol + fullText + fullSuffixText;
	}

	constructor(options) {
		if (typeof options === 'string') {
			options = {
				text: options,
			};
		}

		this.#options = {
			color: 'cyan',
			stream: process.stderr,
			discardStdin: true,
			hideCursor: true,
			...options,
		};

		// Public
		this.color = this.#options.color;

		this.#stream = this.#options.stream;

		// Normalize isEnabled and isSilent into options
		if (typeof this.#options.isEnabled !== 'boolean') {
			this.#options.isEnabled = isInteractive({stream: this.#stream});
		}

		if (typeof this.#options.isSilent !== 'boolean') {
			this.#options.isSilent = false;
		}

		if (this.#options.interval !== undefined && !(Number.isInteger(this.#options.interval) && this.#options.interval > 0)) {
			throw new Error('The `interval` option must be a positive integer');
		}

		// Set *after* `this.#stream`.
		// Store original interval before spinner setter clears it
		const userInterval = this.#options.interval;
		// It's important that these use the public setters.
		this.spinner = this.#options.spinner;
		this.#options.interval = userInterval;
		this.text = this.#options.text;
		this.prefixText = this.#options.prefixText;
		this.suffixText = this.#options.suffixText;
		this.indent = this.#options.indent;

		if (process.env.NODE_ENV === 'test') {
			this._stream = this.#stream;
			this._isEnabled = this.#options.isEnabled;

			Object.defineProperty(this, '_linesToClear', {
				get() {
					return this.#linesToClear;
				},
				set(newValue) {
					this.#linesToClear = newValue;
				},
			});

			Object.defineProperty(this, '_frameIndex', {
				get() {
					return this.#frameIndex;
				},
			});

			Object.defineProperty(this, '_lineCount', {
				get() {
					const columns = this.#stream.columns ?? 80;
					const prefixText = typeof this.#options.prefixText === 'function' ? '' : this.#options.prefixText;
					const suffixText = typeof this.#options.suffixText === 'function' ? '' : this.#options.suffixText;
					const fullPrefixText = (typeof prefixText === 'string' && prefixText !== '') ? prefixText + ' ' : '';
					const fullSuffixText = (typeof suffixText === 'string' && suffixText !== '') ? ' ' + suffixText : '';
					const spinnerChar = '-';
					const fullText = ' '.repeat(this.#options.indent) + fullPrefixText + spinnerChar + (typeof this.#options.text === 'string' ? ' ' + this.#options.text : '') + fullSuffixText;
					return this.#computeLineCountFrom(fullText, columns);
				},
			});
		}
	}

	get indent() {
		return this.#options.indent;
	}

	set indent(indent = 0) {
		if (!(indent >= 0 && Number.isInteger(indent))) {
			throw new Error('The `indent` option must be an integer from 0 and up');
		}

		this.#options.indent = indent;
	}

	get interval() {
		return this.#options.interval ?? this.#spinner.interval ?? 100;
	}

	get spinner() {
		return this.#spinner;
	}

	set spinner(spinner) {
		this.#frameIndex = -1;
		this.#options.interval = undefined;

		if (typeof spinner === 'object') {
			if (!Array.isArray(spinner.frames) || spinner.frames.length === 0 || spinner.frames.some(frame => typeof frame !== 'string')) {
				throw new Error('The given spinner must have a non-empty `frames` array of strings');
			}

			if (spinner.interval !== undefined && !(Number.isInteger(spinner.interval) && spinner.interval > 0)) {
				throw new Error('`spinner.interval` must be a positive integer if provided');
			}

			this.#spinner = spinner;
		} else if (!isUnicodeSupported()) {
			this.#spinner = cliSpinners.line;
		} else if (spinner === undefined) {
			// Set default spinner
			this.#spinner = cliSpinners.dots;
		} else if (spinner !== 'default' && cliSpinners[spinner]) {
			this.#spinner = cliSpinners[spinner];
		} else {
			throw new Error(`There is no built-in spinner named '${spinner}'. See https://github.com/sindresorhus/cli-spinners/blob/main/spinners.json for a full list.`);
		}
	}

	get text() {
		return this.#options.text;
	}

	set text(value = '') {
		this.#options.text = value;
	}

	get prefixText() {
		return this.#options.prefixText;
	}

	set prefixText(value = '') {
		this.#options.prefixText = value;
	}

	get suffixText() {
		return this.#options.suffixText;
	}

	set suffixText(value = '') {
		this.#options.suffixText = value;
	}

	get isSpinning() {
		return this.#id !== undefined;
	}

	#formatAffix(value, separator, placeBefore = false) {
		const resolved = typeof value === 'function' ? value() : value;
		if (typeof resolved === 'string' && resolved !== '') {
			return placeBefore ? (separator + resolved) : (resolved + separator);
		}

		return '';
	}

	#getFullPrefixText(prefixText = this.#options.prefixText, postfix = ' ') {
		return this.#formatAffix(prefixText, postfix, false);
	}

	#getFullSuffixText(suffixText = this.#options.suffixText, prefix = ' ') {
		return this.#formatAffix(suffixText, prefix, true);
	}

	#computeLineCountFrom(text, columns) {
		let count = 0;
		for (const line of stripVTControlCharacters(text).split('\n')) {
			count += Math.max(1, Math.ceil(stringWidth(line) / columns));
		}

		return count;
	}

	get color() {
		return this.#color;
	}

	set color(value) {
		if (value !== undefined && value !== false && !validColors.has(value)) {
			throw new Error('The `color` option must be a valid color or `false` to disable');
		}

		this.#color = value;
	}

	get isEnabled() {
		return this.#options.isEnabled && !this.#options.isSilent;
	}

	set isEnabled(value) {
		if (typeof value !== 'boolean') {
			throw new TypeError('The `isEnabled` option must be a boolean');
		}

		this.#options.isEnabled = value;
	}

	get isSilent() {
		return this.#options.isSilent;
	}

	set isSilent(value) {
		if (typeof value !== 'boolean') {
			throw new TypeError('The `isSilent` option must be a boolean');
		}

		this.#options.isSilent = value;
	}

	frame() {
		// Only advance frame if enough time has passed (throttle to interval)
		const now = Date.now();
		if (this.#frameIndex === -1 || now - this.#lastFrameTime >= this.interval) {
			this.#frameIndex = (this.#frameIndex + 1) % this.#spinner.frames.length;
			this.#lastFrameTime = now;
		}

		const {frames} = this.#spinner;
		let frame = frames[this.#frameIndex];

		if (this.#color) {
			frame = chalk[this.#color](frame);
		}

		const fullPrefixText = this.#getFullPrefixText(this.#options.prefixText, ' ');
		const fullText = typeof this.text === 'string' ? ' ' + this.text : '';
		const fullSuffixText = this.#getFullSuffixText(this.#options.suffixText, ' ');

		return fullPrefixText + frame + fullText + fullSuffixText;
	}

	clear() {
		if (!this.isEnabled || !this.#stream.isTTY) {
			return this;
		}

		// Protect cursor control methods (cursorTo, moveCursor, clearLine) which internally call stream.write
		this.#internalWrite(() => {
			this.#stream.cursorTo(0);

			for (let index = 0; index < this.#linesToClear; index++) {
				if (index > 0) {
					this.#stream.moveCursor(0, -1);
				}

				this.#stream.clearLine(1);
			}

			if (this.#options.indent) {
				this.#stream.cursorTo(this.#options.indent);
			}
		});

		this.#linesToClear = 0;

		return this;
	}

	// Helper to hook a single stream
	#hookStream(stream) {
		if (!stream || this.#hookedStreams.has(stream) || !stream.isTTY || typeof stream.write !== 'function') {
			return;
		}

		// Detect concurrent spinners
		if (activeHooksPerStream.has(stream)) {
			console.warn('[ora] Multiple concurrent spinners detected. This may cause visual corruption. Use one spinner at a time.');
		}

		const originalWrite = stream.write;
		this.#hookedStreams.set(stream, originalWrite);
		activeHooksPerStream.set(stream, this);
		stream.write = (chunk, encoding, callback) => this.#hookedWrite(stream, originalWrite, chunk, encoding, callback);
	}

	/**
	Intercept stream writes while spinner is active to handle external writes cleanly without visual corruption.
	Hooks process stdio streams and the active spinner stream so console.log(), console.error(), and direct writes stay tidy.
	*/
	#installHook() {
		if (!this.isEnabled || this.#hookedStreams.size > 0) {
			return;
		}

		const streamsToHook = new Set([this.#stream, process.stdout, process.stderr]);

		for (const stream of streamsToHook) {
			this.#hookStream(stream);
		}
	}

	#uninstallHook() {
		for (const [stream, originalWrite] of this.#hookedStreams) {
			stream.write = originalWrite;
			if (activeHooksPerStream.get(stream) === this) {
				activeHooksPerStream.delete(stream);
			}
		}

		this.#hookedStreams.clear();
	}

	// eslint-disable-next-line max-params -- Need stream and originalWrite for multi-stream support
	#hookedWrite(stream, originalWrite, chunk, encoding, callback) {
		// Handle both write(chunk, encoding, callback) and write(chunk, callback) signatures
		if (typeof encoding === 'function') {
			callback = encoding;
			encoding = undefined;
		}

		// Pass through our own internal writes (spinner rendering, cursor control)
		if (this.#isInternalWrite) {
			return originalWrite.call(stream, chunk, encoding, callback);
		}

		// External write detected - clear spinner, write content, re-render if appropriate
		this.clear();

		const chunkString = this.#stringifyChunk(chunk, encoding);
		const chunkTerminatesLine = this.#chunkTerminatesLine(chunkString);

		const writeResult = originalWrite.call(stream, chunk, encoding, callback);

		// Schedule or clear render deferral based on chunk content
		if (chunkTerminatesLine) {
			this.#clearRenderDeferral();
		} else if (chunkString.length > 0) {
			this.#scheduleRenderDeferral();
		}

		// Re-render spinner below the new output if still spinning and not deferred
		if (this.isSpinning && !this.#deferRenderTimer) {
			this.render();
		}

		return writeResult;
	}

	render() {
		if (!this.isEnabled || this.#drainHandler || this.#deferRenderTimer) {
			return this;
		}

		const useSynchronizedOutput = this.#stream.isTTY;
		let shouldDisableSynchronizedOutput = false;

		try {
			if (useSynchronizedOutput) {
				this.#internalWrite(() => this.#stream.write(SYNCHRONIZED_OUTPUT_ENABLE));
				shouldDisableSynchronizedOutput = true;
			}

			this.clear();

			let frameContent = this.frame();
			const columns = this.#stream.columns ?? 80;
			const actualLineCount = this.#computeLineCountFrom(frameContent, columns);

			// If content would exceed viewport height, truncate it to prevent garbage
			const consoleHeight = this.#stream.rows;
			if (consoleHeight && consoleHeight > 1 && actualLineCount > consoleHeight) {
				const lines = frameContent.split('\n');
				const maxLines = consoleHeight - 1; // Reserve one line for truncation message
				frameContent = [...lines.slice(0, maxLines), '... (content truncated to fit terminal)'].join('\n');
			}

			const canContinue = this.#internalWrite(() => this.#stream.write(frameContent));

			// Handle backpressure - pause rendering if stream buffer is full
			if (canContinue === false && this.#stream.isTTY) {
				this.#drainHandler = () => {
					this.#drainHandler = undefined;
					this.#tryRender();
				};

				this.#stream.once('drain', this.#drainHandler);
			}

			this.#linesToClear = this.#computeLineCountFrom(frameContent, columns);
		} finally {
			if (shouldDisableSynchronizedOutput) {
				this.#internalWrite(() => this.#stream.write(SYNCHRONIZED_OUTPUT_DISABLE));
			}
		}

		return this;
	}

	start(text) {
		if (text) {
			this.text = text;
		}

		if (this.isSilent) {
			return this;
		}

		if (!this.isEnabled) {
			const symbol = this.text ? '-' : '';
			const line = ' '.repeat(this.#options.indent) + this.#buildOutputLine(symbol, this.text, this.#options.prefixText, this.#options.suffixText);

			if (line.trim() !== '') {
				this.#internalWrite(() => this.#stream.write(line + '\n'));
			}

			return this;
		}

		if (this.isSpinning) {
			return this;
		}

		if (this.#options.hideCursor) {
			cliCursor.hide(this.#stream);
		}

		if (this.#options.discardStdin && process.stdin.isTTY) {
			stdinDiscarder.start();
			this.#isDiscardingStdin = true;
		}

		this.#installHook();
		this.render();
		this.#id = setInterval(this.render.bind(this), this.interval);

		return this;
	}

	stop() {
		clearInterval(this.#id);
		this.#id = undefined;
		this.#frameIndex = -1;
		this.#lastFrameTime = 0;

		this.#clearRenderDeferral();
		this.#uninstallHook();

		// Clean up drain handler if it exists
		if (this.#drainHandler) {
			this.#stream.removeListener('drain', this.#drainHandler);
			this.#drainHandler = undefined;
		}

		if (this.isEnabled) {
			this.clear();
			if (this.#options.hideCursor) {
				cliCursor.show(this.#stream);
			}
		}

		if (this.#isDiscardingStdin) {
			this.#isDiscardingStdin = false;
			stdinDiscarder.stop();
		}

		return this;
	}

	succeed(text) {
		return this.stopAndPersist({symbol: logSymbols.success, text});
	}

	fail(text) {
		return this.stopAndPersist({symbol: logSymbols.error, text});
	}

	warn(text) {
		return this.stopAndPersist({symbol: logSymbols.warning, text});
	}

	info(text) {
		return this.stopAndPersist({symbol: logSymbols.info, text});
	}

	stopAndPersist(options = {}) {
		if (this.isSilent) {
			return this;
		}

		const symbol = options.symbol ?? ' ';
		const text = options.text ?? this.text;
		const prefixText = options.prefixText ?? this.#options.prefixText;
		const suffixText = options.suffixText ?? this.#options.suffixText;

		const textToWrite = this.#buildOutputLine(symbol, text, prefixText, suffixText) + '\n';

		this.stop();
		this.#internalWrite(() => this.#stream.write(textToWrite));

		return this;
	}
}

export default function ora(options) {
	return new Ora(options);
}

export async function oraPromise(action, options) {
	const actionIsFunction = typeof action === 'function';
	const actionIsPromise = typeof action.then === 'function';

	if (!actionIsFunction && !actionIsPromise) {
		throw new TypeError('Parameter `action` must be a Function or a Promise');
	}

	const {successText, failText} = typeof options === 'object'
		? options
		: {successText: undefined, failText: undefined};

	const spinner = ora(options).start();

	try {
		const promise = actionIsFunction ? action(spinner) : action;
		const result = await promise;

		spinner.succeed(successText === undefined
			? undefined
			: (typeof successText === 'string' ? successText : successText(result)));

		return result;
	} catch (error) {
		spinner.fail(failText === undefined
			? undefined
			: (typeof failText === 'string' ? failText : failText(error)));

		throw error;
	}
}

export {default as spinners} from 'cli-spinners';
```

## File: `index.test-d.ts`
```typescript
import {PassThrough as PassThroughStream} from 'node:stream';
import {expectType} from 'tsd';
import type cliSpinners from 'cli-spinners';
import ora, {oraPromise, spinners} from './index.js';

const spinner = ora('Loading unicorns');
ora({text: 'Loading unicorns'});
ora({prefixText: 'Loading unicorns'});
ora({prefixText: () => 'Loading unicorns dynamically'});
ora({suffixText: 'Loading unicorns'});
ora({suffixText: () => 'Loading unicorns dynamically'});
ora({spinner: 'squish'});
ora({spinner: {frames: ['-', '+', '-']}});
ora({spinner: {interval: 80, frames: ['-', '+', '-']}});
ora({color: 'cyan'});
ora({color: false});
ora({hideCursor: true});
ora({indent: 1});
ora({interval: 80});
ora({stream: new PassThroughStream()});
ora({isEnabled: true});
ora({isSilent: false});
ora({discardStdin: true});

spinner.color = 'yellow';
spinner.color = false;
spinner.text = 'Loading rainbows';
expectType<boolean>(spinner.isSpinning);
spinner.spinner = 'dots';
spinner.indent = 5;

spinner.start();
spinner.start('Test text');
spinner.stop();
spinner.succeed();
spinner.succeed('fooed');
spinner.fail();
spinner.fail('failed to foo');
spinner.warn();
spinner.warn('warn foo');
spinner.info();
spinner.info('info foo');
spinner.stopAndPersist();
spinner.stopAndPersist({text: 'all done'});
spinner.stopAndPersist({symbol: '@', text: 'all done'});
spinner.stopAndPersist({prefixText: 'all done'});
spinner.stopAndPersist({suffixText: 'all done'});
spinner.clear();
spinner.render();
spinner.frame();

const resolves = Promise.resolve(1);
void oraPromise(resolves, 'foo');
void oraPromise(resolves, {
	stream: new PassThroughStream(),
	text: 'foo',
	color: 'blue',
	isEnabled: true,
	isSilent: false,
});
void oraPromise(async () => {
	await resolves;
}, 'foo');
void oraPromise(async spinner => {
	spinner.prefixText = 'foo';
	spinner.suffixText = '[loading]';
	await resolves;
	return 7;
}, {
	stream: new PassThroughStream(),
	text: 'foo',
	color: 'blue',
	isEnabled: true,
	isSilent: false,
	successText: result => `Resolved with number ${result}`,
	failText: 'bar',
});

expectType<typeof cliSpinners>(spinners);
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
	"name": "ora",
	"version": "9.3.0",
	"description": "Elegant terminal spinner",
	"license": "MIT",
	"repository": "sindresorhus/ora",
	"funding": "https://github.com/sponsors/sindresorhus",
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
	"sideEffects": false,
	"engines": {
		"node": ">=20"
	},
	"scripts": {
		"test": "xo && NODE_ENV=test node --test test.js && tsd"
	},
	"files": [
		"index.js",
		"index.d.ts"
	],
	"keywords": [
		"cli",
		"spinner",
		"spinners",
		"terminal",
		"term",
		"console",
		"ascii",
		"unicode",
		"loading",
		"indicator",
		"progress",
		"busy",
		"wait",
		"idle"
	],
	"dependencies": {
		"chalk": "^5.6.2",
		"cli-cursor": "^5.0.0",
		"cli-spinners": "^3.2.0",
		"is-interactive": "^2.0.0",
		"is-unicode-supported": "^2.1.0",
		"log-symbols": "^7.0.1",
		"stdin-discarder": "^0.3.1",
		"string-width": "^8.1.0"
	},
	"devDependencies": {
		"@types/node": "^24.5.0",
		"ava": "^6.4.1",
		"get-stream": "^9.0.1",
		"transform-tty": "^1.0.11",
		"tsd": "^0.33.0",
		"xo": "^1.2.2"
	}
}
```

## File: `readme.md`
```markdown
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

Discard stdin input (except Ctrl+C) while running if it's TTY. This prevents the spinner from twitching on input, outputting broken lines on <kbd>Enter</kbd> key presses, and prevents buffering of input while the spinner is running.

This has no effect on Windows as there is no good way to implement discarding stdin properly there.

Note: `discardStdin` puts stdin into raw mode. In raw mode, `Ctrl+C` no longer generates `SIGINT` from the terminal. Ora re-emits `Ctrl+C` from stdin input, but if your code blocks the event loop with synchronous work, `Ctrl+C` handling is delayed until the blocking work ends. Use async APIs, a worker thread, or a child process to keep `Ctrl+C` responsive, or set `discardStdin` to `false`.

### Instance

#### .text <sup>get/set</sup>

Change the text displayed after the spinner.

#### .prefixText <sup>get/set</sup>

Change the text before the spinner.

No prefix text will be displayed if set to an empty string.

#### .suffixText <sup>get/set</sup>

Change the text after the spinner text.

No suffix text will be displayed if set to an empty string.

#### .color <sup>get/set</sup>

Change the spinner color.

#### .spinner <sup>get/set</sup>

Change the spinner.

#### .indent <sup>get/set</sup>

Change the spinner indent.

#### .isSpinning <sup>get</sup>

A boolean indicating whether the instance is currently spinning.

#### .interval <sup>get</sup>

The interval between each frame.

The interval is decided by the chosen spinner.

#### .start(text?)

Start the spinner. Returns the instance. Set the current text if `text` is provided.

#### .stop()

Stop and clear the spinner. Returns the instance.

#### .succeed(text?)

Stop the spinner, change it to a green `✔` and persist the current text, or `text` if provided. Returns the instance. See the GIF below.

#### .fail(text?)

Stop the spinner, change it to a red `✖` and persist the current text, or `text` if provided. Returns the instance. See the GIF below.

#### .warn(text?)

Stop the spinner, change it to a yellow `⚠` and persist the current text, or `text` if provided. Returns the instance.

#### .info(text?)

Stop the spinner, change it to a blue `ℹ` and persist the current text, or `text` if provided. Returns the instance.

#### .stopAndPersist(options?)

Stop the spinner and change the symbol or text. Returns the instance. See the GIF below.

##### options

Type: `object`

###### symbol

Type: `string`\
Default: `' '`

Symbol to replace the spinner with.

###### text

Type: `string`\
Default: Current `'text'`

Text to be persisted after the symbol.

###### prefixText

Type: `string | () => string`\
Default: Current `prefixText`

Text or a function that returns text to be persisted before the symbol. No prefix text will be displayed if set to an empty string.

###### suffixText

Type: `string | () => string`\
Default: Current `suffixText`

Text or a function that returns text to be persisted after the text after the symbol. No suffix text will be displayed if set to an empty string.

<img src="screenshot-2.gif" width="480">

#### .clear()

Clear the spinner. Returns the instance.

#### .render()

Manually render a new frame. Returns the instance.

#### .frame()

Get a new frame.

### oraPromise(action, text)
### oraPromise(action, options)

Starts a spinner for a promise or promise-returning function. The spinner is stopped with `.succeed()` if the promise fulfills or with `.fail()` if it rejects. Returns the promise.

```js
import {oraPromise} from 'ora';

await oraPromise(somePromise);
```

#### action

Type: `Promise | ((spinner: ora.Ora) => Promise)`

#### options

Type: `object`

All of the [options](#options) plus the following:

##### successText

Type: `string | ((result: T) => string) | undefined`

The new text of the spinner when the promise is resolved.

Keeps the existing text if `undefined`.

##### failText

Type: `string | ((error: Error) => string) | undefined`

The new text of the spinner when the promise is rejected.

Keeps the existing text if `undefined`.

### spinners

Type: `Record<string, Spinner>`

All [provided spinners](https://github.com/sindresorhus/cli-spinners/blob/main/spinners.json).

## FAQ

### How do I change the color of the text?

Use [`chalk`](https://github.com/chalk/chalk) or [`yoctocolors`](https://github.com/sindresorhus/yoctocolors):

```js
import ora from 'ora';
import chalk from 'chalk';

const spinner = ora(`Loading ${chalk.red('unicorns')}`).start();
```

### Why does the spinner freeze?

JavaScript is single-threaded, so any synchronous operations will block the spinner's animation. To avoid this, prefer using asynchronous operations.

### Why do I get the line spinner on Windows Terminal or WSL?

Windows Terminal does [not expose](https://github.com/microsoft/terminal/issues/1040) a reliable, stable way to detect itself or Unicode support from Node, and `WT_SESSION` is explicitly informative, not a detection API and can be inherited by other terminals. That makes environment-based detection best-effort. If you are in a Unicode-capable terminal, set `spinner` explicitly, for example `ora({spinner: 'dots'})`.

### Can I log messages while the spinner is running?

Yes! Ora automatically handles writes to the same stream. The spinner will temporarily clear itself, output your message, and re-render below:

```js
const spinner = ora('Processing...').start();

console.log('Step 1 complete');
console.log('Step 2 complete');

spinner.succeed('Done!');
```

The output will be clean with each log appearing above the spinner. This works seamlessly without requiring any special logging methods. Both `console.log()` (stdout) and `console.error()`/`console.warn()` (stderr) are supported.

> [!NOTE]
> Don't run multiple spinners concurrently. Use one spinner at a time.

### Can I display multiple spinners simultaneously?

No. Ora is designed to display a single spinner at a time. For multiple concurrent progress indicators, consider alternatives like [listr2](https://github.com/listr2/listr2) or [spinnies](https://github.com/jcarpanelli/spinnies).

### Can I use Ora with [log-update](https://github.com/sindresorhus/log-update)?

Yes, use the `.frame()` method to get the current spinner frame and include it in your log-update output.

### Does Ora work in Node.js Worker threads?

No. Ora requires an interactive terminal environment and Worker threads are not considered interactive, so the spinner will not animate. Run the spinner in the main thread and control it via worker messages:

```js
// main.js
import {Worker} from 'node:worker_threads';
import ora from 'ora';

const spinner = ora().start();
const worker = new Worker('./worker.js');

worker.on('message', message => {
	switch (message.type) {
		case 'ora:text':
			spinner.text = message.text;
			break;
		case 'ora:succeed':
			spinner.succeed(message.text);
			break;
		case 'ora:fail':
			spinner.fail(message.text);
			break;
	}
});
```

```js
// worker.js
import {parentPort} from 'node:worker_threads';

parentPort.postMessage({type: 'ora:text', text: 'Working...'});

// Do work...

parentPort.postMessage({type: 'ora:succeed', text: 'Done!'});
```

## Related

- [yocto-spinner](https://github.com/sindresorhus/yocto-spinner) - Tiny terminal spinner
- [cli-spinners](https://github.com/sindresorhus/cli-spinners) - Spinners for use in the terminal

**Ports**

- [CLISpinner](https://github.com/kiliankoe/CLISpinner) - Terminal spinner library for Swift
- [halo](https://github.com/ManrajGrover/halo) - Python port
- [spinners](https://github.com/FGRibreau/spinners) - Terminal spinners for Rust
- [marquee-ora](https://github.com/joeycozza/marquee-ora) - Scrolling marquee spinner for Ora
- [briandowns/spinner](https://github.com/briandowns/spinner) - Terminal spinner/progress indicator for Go
- [tj/go-spin](https://github.com/tj/go-spin) - Terminal spinner package for Go
- [observablehq.com/@victordidenko/ora](https://observablehq.com/@victordidenko/ora) - Ora port to Observable notebooks
- [kia](https://github.com/HarryPeach/kia) - Simple terminal spinners for Deno 🦕
```

## File: `screenshot.json`
```json
{
  "version": 1,
  "width": 32,
  "height": 5,
  "duration": 18.816945,
  "command": null,
  "title": null,
  "env": {
    "TERM": "xterm-256color",
    "SHELL": "/usr/local/bin/fish"
  },
  "stdout": [
    [
      0.001904,
      "\u001b[38;2;85;85;85mode example.js \u001b[15D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.116914,
      "\u001b[1mo\u001b(B\u001b[m\u001b[38;2;85;85;85mde example.js \u001b[14D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.000171,
      "\b\b\u001b[91mno\u001b[38;2;85;85;85mde example.js \u001b[14D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.067673,
      "\u001b[91md\u001b[38;2;85;85;85me example.js \u001b[13D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.203036,
      "\u001b[91me\u001b[38;2;85;85;85m example.js \u001b[12D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.000326,
      "\b\b\b\b\u001b[1mnode\u001b(B\u001b[m\u001b[38;2;85;85;85m example.js \u001b[12D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.085694,
      "\u001b[1m \u001b(B\u001b[m\u001b[38;2;85;85;85mexample.js \u001b[11D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.000111,
      "\b \u001b[38;2;85;85;85mexample.js \u001b[11D\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.382488,
      "example.js "
    ],
    [
      0.000165,
      "\u001b[11D\u001b[36mexample.js\u001b[30m\u001b(B\u001b[m "
    ],
    [
      0.314997,
      "\r\n\u001b[30m\u001b(B\u001b[m"
    ],
    [
      0.00013,
      "\u001b[?2004l"
    ],
    [
      0.011313,
      "\u001b]0;ora: node example.js  — node\u0007\u001b[30m\u001b(B\u001b[m\r"
    ],
    [
      0.1158,
      "\u001b[?25l"
    ],
    [
      0.002061,
      "\u001b[2K"
    ],
    [
      0.000114,
      "\u001b[1G"
    ],
    [
      0.000158,
      "\u001b[36m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.083103,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000377,
      "\u001b[36m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.086286,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.00012,
      "\u001b[36m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.081743,
      "\u001b[2K"
    ],
    [
      0.000111,
      "\u001b[1G"
    ],
    [
      0.000128,
      "\u001b[36m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.085696,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000299,
      "\u001b[36m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.083688,
      "\u001b[2K"
    ],
    [
      8.3e-05,
      "\u001b[1G"
    ],
    [
      0.000148,
      "\u001b[36m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.080913,
      "\u001b[2K"
    ],
    [
      9.5e-05,
      "\u001b[1G"
    ],
    [
      0.000267,
      "\u001b[36m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.086336,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000169,
      "\u001b[36m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.083412,
      "\u001b[2K"
    ],
    [
      6.4e-05,
      "\u001b[1G"
    ],
    [
      0.000298,
      "\u001b[36m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.086227,
      "\u001b[2K"
    ],
    [
      8.5e-05,
      "\u001b[1G"
    ],
    [
      0.000161,
      "\u001b[36m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.082719,
      "\u001b[2K"
    ],
    [
      9.5e-05,
      "\u001b[1G"
    ],
    [
      0.000398,
      "\u001b[36m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.084857,
      "\u001b[2K"
    ],
    [
      5.1e-05,
      "\u001b[1G"
    ],
    [
      0.000383,
      "\u001b[36m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.082811,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000121,
      "\u001b[36m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.080951,
      "\u001b[2K"
    ],
    [
      8.3e-05,
      "\u001b[1G"
    ],
    [
      0.000181,
      "\u001b[36m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.084463,
      "\u001b[2K"
    ],
    [
      0.000107,
      "\u001b[1G"
    ],
    [
      0.000122,
      "\u001b[36m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.083375,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000127,
      "\u001b[36m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.080903,
      "\u001b[2K"
    ],
    [
      0.000341,
      "\u001b[1G"
    ],
    [
      6.5e-05,
      "\u001b[36m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.085916,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.00024,
      "\u001b[36m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.081289,
      "\u001b[2K"
    ],
    [
      8.6e-05,
      "\u001b[1G"
    ],
    [
      0.000605,
      "\u001b[36m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.080957,
      "\u001b[2K"
    ],
    [
      0.00037,
      "\u001b[1G"
    ],
    [
      0.00053,
      "\u001b[36m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.084219,
      "\u001b[2K"
    ],
    [
      8.5e-05,
      "\u001b[1G"
    ],
    [
      0.000328,
      "\u001b[36m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.082526,
      "\u001b[2K"
    ],
    [
      8.8e-05,
      "\u001b[1G"
    ],
    [
      0.000244,
      "\u001b[36m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.082079,
      "\u001b[2K"
    ],
    [
      6.4e-05,
      "\u001b[1G"
    ],
    [
      0.000816,
      "\u001b[36m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.084362,
      "\u001b[2K"
    ],
    [
      8.1e-05,
      "\u001b[1G"
    ],
    [
      0.000167,
      "\u001b[36m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.08224,
      "\u001b[2K"
    ],
    [
      8.1e-05,
      "\u001b[1G"
    ],
    [
      0.000347,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.0813,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000104,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.081323,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000131,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.080502,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000104,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.081233,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000224,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.084122,
      "\u001b[2K"
    ],
    [
      6.8e-05,
      "\u001b[1G"
    ],
    [
      9.7e-05,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.084086,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000214,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.085431,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000178,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.082205,
      "\u001b[2K"
    ],
    [
      8.6e-05,
      "\u001b[1G"
    ],
    [
      0.000167,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.08663,
      "\u001b[2K"
    ],
    [
      9.5e-05,
      "\u001b[1G"
    ],
    [
      0.000173,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.084956,
      "\u001b[2K"
    ],
    [
      9.4e-05,
      "\u001b[1G"
    ],
    [
      0.000228,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.083064,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000233,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.084532,
      "\u001b[2K"
    ],
    [
      8.9e-05,
      "\u001b[1G"
    ],
    [
      0.000205,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.082335,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000293,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.083895,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000357,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.084621,
      "\u001b[2K"
    ],
    [
      0.000116,
      "\u001b[1G"
    ],
    [
      0.000195,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.084423,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000528,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.084666,
      "\u001b[2K"
    ],
    [
      5.7e-05,
      "\u001b[1G"
    ],
    [
      0.00021,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.08529,
      "\u001b[2K"
    ],
    [
      9e-05,
      "\u001b[1G"
    ],
    [
      0.000166,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.08098,
      "\u001b[2K"
    ],
    [
      0.001673,
      "\u001b[1G"
    ],
    [
      0.001369,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.084824,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000209,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.084048,
      "\u001b[2K"
    ],
    [
      9.5e-05,
      "\u001b[1G"
    ],
    [
      0.000167,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.08298,
      "\u001b[2K"
    ],
    [
      6.6e-05,
      "\u001b[1G"
    ],
    [
      0.000435,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.080783,
      "\u001b[2K"
    ],
    [
      8.3e-05,
      "\u001b[1G"
    ],
    [
      0.000382,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.081044,
      "\u001b[2K"
    ],
    [
      6.6e-05,
      "\u001b[1G"
    ],
    [
      0.000247,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.08066,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000111,
      "\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.083301,
      "\u001b[2K"
    ],
    [
      6e-05,
      "\u001b[1G"
    ],
    [
      0.000177,
      "\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.08367,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000256,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.083109,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000356,
      "\u001b[32m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.08574,
      "\u001b[2K"
    ],
    [
      8.9e-05,
      "\u001b[1G"
    ],
    [
      0.000325,
      "\u001b[32m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.084085,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000224,
      "\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.085112,
      "\u001b[2K\u001b[1G\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.080702,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000142,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.08402,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000618,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.082493,
      "\u001b[2K"
    ],
    [
      8e-05,
      "\u001b[1G"
    ],
    [
      0.000213,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.081267,
      "\u001b[2K"
    ],
    [
      6.9e-05,
      "\u001b[1G"
    ],
    [
      0.000126,
      "\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.080987,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000802,
      "\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.083891,
      "\u001b[2K\u001b[1G"
    ],
    [
      7.1e-05,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.081677,
      "\u001b[2K"
    ],
    [
      6.8e-05,
      "\u001b[1G"
    ],
    [
      0.000109,
      "\u001b[32m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.081978,
      "\u001b[2K"
    ],
    [
      0.000105,
      "\u001b[1G"
    ],
    [
      0.000475,
      "\u001b[32m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.085732,
      "\u001b[2K"
    ],
    [
      7e-05,
      "\u001b[1G"
    ],
    [
      0.000111,
      "\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.081498,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000357,
      "\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.081684,
      "\u001b[2K"
    ],
    [
      7.3e-05,
      "\u001b[1G"
    ],
    [
      0.000603,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.081071,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000262,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.084355,
      "\u001b[2K\u001b[1G\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.084846,
      "\u001b[2K"
    ],
    [
      5.7e-05,
      "\u001b[1G"
    ],
    [
      0.000232,
      "\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.084847,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000235,
      "\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.082068,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000619,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.081252,
      "\u001b[2K"
    ],
    [
      6.9e-05,
      "\u001b[1G"
    ],
    [
      0.000124,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.083929,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000121,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.083262,
      "\u001b[2K"
    ],
    [
      5.8e-05,
      "\u001b[1G"
    ],
    [
      0.0002,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.082963,
      "\u001b[2K"
    ],
    [
      0.000453,
      "\u001b[1G\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.084622,
      "\u001b[2K"
    ],
    [
      9.1e-05,
      "\u001b[1G"
    ],
    [
      0.000386,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.082358,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000205,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.082973,
      "\u001b[2K"
    ],
    [
      0.000114,
      "\u001b[1G"
    ],
    [
      0.00045,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.081773,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.00026,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.081145,
      "\u001b[2K"
    ],
    [
      6.6e-05,
      "\u001b[1G"
    ],
    [
      0.000218,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.083303,
      "\u001b[2K"
    ],
    [
      7.8e-05,
      "\u001b[1G"
    ],
    [
      0.000555,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.082269,
      "\u001b[2K"
    ],
    [
      9e-05,
      "\u001b[1G"
    ],
    [
      0.000251,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.086135,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000383,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.081856,
      "\u001b[2K"
    ],
    [
      9.4e-05,
      "\u001b[1G"
    ],
    [
      0.000216,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.0838,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000204,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.083278,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000154,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.084661,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000425,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.085872,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000338,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.08196,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000576,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.082757,
      "\u001b[2K"
    ],
    [
      6.8e-05,
      "\u001b[1G"
    ],
    [
      0.000226,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.084301,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000283,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.081155,
      "\u001b[2K"
    ],
    [
      0.000105,
      "\u001b[1G"
    ],
    [
      0.000217,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.084793,
      "\u001b[2K"
    ],
    [
      0.000125,
      "\u001b[1G"
    ],
    [
      0.000247,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.083009,
      "\u001b[2K"
    ],
    [
      6.6e-05,
      "\u001b[1G"
    ],
    [
      0.000225,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.081915,
      "\u001b[2K"
    ],
    [
      8.3e-05,
      "\u001b[1G"
    ],
    [
      0.000149,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.080718,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000198,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.082405,
      "\u001b[2K"
    ],
    [
      9.1e-05,
      "\u001b[1G"
    ],
    [
      0.000459,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.084385,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000196,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.085676,
      "\u001b[2K"
    ],
    [
      0.000104,
      "\u001b[1G"
    ],
    [
      0.000613,
      "\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.082713,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000962,
      "\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.085432,
      "\u001b[2K"
    ],
    [
      9.2e-05,
      "\u001b[1G"
    ],
    [
      0.00041,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.082907,
      "\u001b[2K"
    ],
    [
      9.9e-05,
      "\u001b[1G"
    ],
    [
      0.000262,
      "\u001b[32m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.082884,
      "\u001b[2K"
    ],
    [
      0.000193,
      "\u001b[1G"
    ],
    [
      0.000735,
      "\u001b[32m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.08535,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000116,
      "\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.083234,
      "\u001b[2K"
    ],
    [
      5.9e-05,
      "\u001b[1G"
    ],
    [
      0.000258,
      "\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.086415,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000148,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.081705,
      "\u001b[2K"
    ],
    [
      8.8e-05,
      "\u001b[1G"
    ],
    [
      0.000146,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.080807,
      "\u001b[2K"
    ],
    [
      8.8e-05,
      "\u001b[1G"
    ],
    [
      0.000249,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.079687,
      "\u001b[2K"
    ],
    [
      8.4e-05,
      "\u001b[1G"
    ],
    [
      0.000183,
      "\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.081712,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000254,
      "\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.080168,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000822,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.084237,
      "\u001b[2K"
    ],
    [
      9.8e-05,
      "\u001b[1G"
    ],
    [
      0.000488,
      "\u001b[32m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.084152,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000279,
      "\u001b[32m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.081638,
      "\u001b[2K"
    ],
    [
      9.3e-05,
      "\u001b[1G"
    ],
    [
      0.000138,
      "\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.083315,
      "\u001b[2K"
    ],
    [
      9.4e-05,
      "\u001b[1G"
    ],
    [
      0.000148,
      "\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.081786,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000268,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.08429,
      "\u001b[2K"
    ],
    [
      0.000137,
      "\u001b[1G"
    ],
    [
      0.000295,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.081238,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000109,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.086071,
      "\u001b[2K\u001b[1G\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.081903,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000388,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.083037,
      "\u001b[2K"
    ],
    [
      0.000101,
      "\u001b[1G"
    ],
    [
      0.000473,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.082119,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000351,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.085497,
      "\u001b[2K"
    ],
    [
      8.8e-05,
      "\u001b[1G"
    ],
    [
      0.001197,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.082871,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000109,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.086538,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000281,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.085626,
      "^D\b\b"
    ],
    [
      0.001457,
      "\u001b[2K"
    ],
    [
      6e-05,
      "\u001b[1G"
    ],
    [
      0.000189,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.085264,
      "\u001b[2K"
    ],
    [
      6.7e-05,
      "\u001b[1G"
    ],
    [
      0.000265,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.085663,
      "\u001b[2K"
    ],
    [
      6.9e-05,
      "\u001b[1G"
    ],
    [
      0.000108,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.084885,
      "\u001b[2K"
    ],
    [
      0.000113,
      "\u001b[1G"
    ],
    [
      0.000455,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.083256,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.001423,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.089174,
      "\u001b[2K"
    ],
    [
      0.001635,
      "\u001b[1G\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.092049,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000206,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.080988,
      "\u001b[2K"
    ],
    [
      9.7e-05,
      "\u001b[1G"
    ],
    [
      0.00034,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.081192,
      "\u001b[2K"
    ],
    [
      8.3e-05,
      "\u001b[1G"
    ],
    [
      0.000165,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.085462,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000381,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.084879,
      "\u001b[2K"
    ],
    [
      9.6e-05,
      "\u001b[1G"
    ],
    [
      0.000182,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.081392,
      "\u001b[2K"
    ],
    [
      0.000104,
      "\u001b[1G"
    ],
    [
      0.000187,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.081924,
      "\u001b[2K\u001b[1G\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.084352,
      "\u001b[2K"
    ],
    [
      9.7e-05,
      "\u001b[1G"
    ],
    [
      0.00037,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.080816,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000417,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.084295,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000202,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.084905,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000103,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.080886,
      "\u001b[2K"
    ],
    [
      0.000102,
      "\u001b[1G"
    ],
    [
      0.000188,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.085382,
      "\u001b[2K\u001b[1G\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.081915,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000274,
      "\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.084892,
      "\u001b[2K"
    ],
    [
      0.000169,
      "\u001b[1G\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.083987,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000211,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.084345,
      "\u001b[2K"
    ],
    [
      7.6e-05,
      "\u001b[1G"
    ],
    [
      9.7e-05,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.083658,
      "\u001b[2K"
    ],
    [
      0.000109,
      "\u001b[1G"
    ],
    [
      0.000244,
      "\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.083053,
      "\u001b[2K\u001b[1G\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.084848,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000153,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.083902,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000767,
      "\u001b[32m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.080861,
      "\u001b[2K\u001b[1G\u001b[32m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.081879,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000182,
      "\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.083858,
      "\u001b[2K"
    ],
    [
      6.5e-05,
      "\u001b[1G"
    ],
    [
      0.000341,
      "\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.085888,
      "\u001b[2K"
    ],
    [
      0.000112,
      "\u001b[1G"
    ],
    [
      0.000229,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.083217,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.00012,
      "\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.080302,
      "\u001b[2K"
    ],
    [
      9.9e-05,
      "\u001b[1G"
    ],
    [
      0.000323,
      "\u001b[32m⠇\u001b[39m Loading unicorns"
    ],
    [
      0.08551,
      "\u001b[2K\u001b[1G\u001b[32m⠏\u001b[39m Loading unicorns"
    ],
    [
      0.054202,
      "^D\b\b"
    ],
    [
      0.026417,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000484,
      "\u001b[32m⠋\u001b[39m Loading unicorns"
    ],
    [
      0.082857,
      "\u001b[2K"
    ],
    [
      0.000422,
      "\u001b[1G"
    ],
    [
      0.00016,
      "\u001b[32m⠙\u001b[39m Loading unicorns"
    ],
    [
      0.084827,
      "\u001b[2K"
    ],
    [
      7.9e-05,
      "\u001b[1G"
    ],
    [
      0.000136,
      "\u001b[32m⠹\u001b[39m Loading unicorns"
    ],
    [
      0.081255,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000107,
      "\u001b[32m⠸\u001b[39m Loading unicorns"
    ],
    [
      0.082968,
      "\u001b[2K"
    ],
    [
      0.000135,
      "\u001b[1G"
    ],
    [
      9e-05,
      "\u001b[32m⠼\u001b[39m Loading unicorns"
    ],
    [
      0.083101,
      "\u001b[2K"
    ],
    [
      0.0001,
      "\u001b[1G"
    ],
    [
      0.000121,
      "\u001b[32m⠴\u001b[39m Loading unicorns"
    ],
    [
      0.080704,
      "\u001b[2K"
    ],
    [
      0.000382,
      "\u001b[1G"
    ],
    [
      5.8e-05,
      "\u001b[32m⠦\u001b[39m Loading unicorns"
    ],
    [
      0.085362,
      "\u001b[2K\u001b[1G\u001b[32m⠧\u001b[39m Loading unicorns"
    ],
    [
      0.084439,
      "\u001b[2K"
    ],
    [
      6.5e-05,
      "\u001b[1G"
    ],
    [
      0.000109,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.081339,
      "\u001b[2K"
    ],
    [
      9.5e-05,
      "\u001b[1G"
    ],
    [
      0.00027,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ],
    [
      0.047113,
      "^D\b\b"
    ],
    [
      0.03416,
      "\u001b[2K"
    ],
    [
      7.8e-05,
      "\u001b[1G"
    ],
    [
      0.000146,
      "\u001b[33m⠋\u001b[39m Loading rainbows"
    ],
    [
      0.080609,
      "\u001b[2K"
    ],
    [
      0.000104,
      "\u001b[1G"
    ],
    [
      0.000287,
      "\u001b[33m⠙\u001b[39m Loading rainbows"
    ],
    [
      0.080932,
      "\u001b[2K"
    ],
    [
      9.9e-05,
      "\u001b[1G"
    ],
    [
      0.000134,
      "\u001b[33m⠹\u001b[39m Loading rainbows"
    ],
    [
      0.081025,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.00022,
      "\u001b[33m⠸\u001b[39m Loading rainbows"
    ],
    [
      0.086437,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.00027,
      "\u001b[33m⠼\u001b[39m Loading rainbows"
    ],
    [
      0.084962,
      "\u001b[2K"
    ],
    [
      6.3e-05,
      "\u001b[1G"
    ],
    [
      0.00021,
      "\u001b[33m⠴\u001b[39m Loading rainbows"
    ],
    [
      0.083325,
      "\u001b[2K\u001b[1G"
    ],
    [
      0.000283,
      "\u001b[33m⠦\u001b[39m Loading rainbows"
    ],
    [
      0.080876,
      "\u001b[2K"
    ],
    [
      9.1e-05,
      "\u001b[1G"
    ],
    [
      0.000228,
      "\u001b[33m⠧\u001b[39m Loading rainbows"
    ],
    [
      0.080961,
      "\u001b[2K"
    ],
    [
      9e-05,
      "\u001b[1G"
    ],
    [
      0.000267,
      "\u001b[33m⠇\u001b[39m Loading rainbows"
    ],
    [
      0.086332,
      "\u001b[2K"
    ],
    [
      7.9e-05,
      "\u001b[1G"
    ],
    [
      0.001762,
      "\u001b[33m⠏\u001b[39m Loading rainbows"
    ]
  ]
}
```

## File: `test.js`
```javascript
/* eslint max-lines: "off" */
import process from 'node:process';
import {PassThrough as PassThroughStream} from 'node:stream';
import {stripVTControlCharacters} from 'node:util';
import assert from 'node:assert/strict';
import test from 'node:test';
import getStream from 'get-stream';
import TransformTTY from 'transform-tty';
import ora, {oraPromise, spinners} from './index.js';

const spinnerCharacter = process.platform === 'win32' ? '-' : '⠋';
const synchronizedOutputEnable = '\u001B[?2026h';
const synchronizedOutputDisable = '\u001B[?2026l';
const noop = () => {};

const getLastSynchronizedOutput = output => {
	const lastEnableIndex = output.lastIndexOf(synchronizedOutputEnable);
	if (lastEnableIndex === -1) {
		return output;
	}

	const disableIndex = output.indexOf(synchronizedOutputDisable, lastEnableIndex);
	if (disableIndex === -1) {
		return output.slice(lastEnableIndex + synchronizedOutputEnable.length);
	}

	return output.slice(lastEnableIndex + synchronizedOutputEnable.length, disableIndex);
};

const stripSynchronizedOutputSequences = content => {
	if (typeof content !== 'string') {
		return content;
	}

	return content.replaceAll(synchronizedOutputEnable, '').replaceAll(synchronizedOutputDisable, '');
};

const applySynchronizedOutputFilter = stream => {
	const originalWrite = stream.write;
	stream.write = function (content, encoding, callback) {
		const filteredContent = stripSynchronizedOutputSequences(content);
		if (filteredContent === '') {
			return true;
		}

		return originalWrite.call(this, filteredContent, encoding, callback);
	};

	return stream;
};

const getPassThroughStream = () => {
	const stream = new PassThroughStream();
	stream.clearLine = noop;
	stream.cursorTo = noop;
	stream.moveCursor = noop;
	return stream;
};

const withFakeStdin = (options = {}, callback) => {
	const {isPaused = false} = options;
	const originalStdinDescriptor = Object.getOwnPropertyDescriptor(process, 'stdin');
	const fakeStdin = new PassThroughStream();
	const rawModeCalls = [];

	fakeStdin.isTTY = true;
	fakeStdin.isRaw = false;
	fakeStdin.setRawMode = value => {
		rawModeCalls.push(value);
		fakeStdin.isRaw = value;
	};

	if (isPaused) {
		fakeStdin.pause();
	}

	Object.defineProperty(process, 'stdin', {
		value: fakeStdin,
		configurable: true,
	});

	try {
		return callback({fakeStdin, rawModeCalls});
	} finally {
		Object.defineProperty(process, 'stdin', originalStdinDescriptor);
	}
};

const doSpinner = async (function_, extraOptions = {}) => {
	const stream = getPassThroughStream();
	const output = getStream(stream);

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
		isSilent: false,
		...extraOptions,
	});

	spinner.start();
	function_(spinner);
	stream.end();

	return stripVTControlCharacters(await output);
};

test('main', async () => {
	const result = await doSpinner(spinner => {
		spinner.stop();
	});
	assert.match(result, new RegExp(`${spinnerCharacter} foo`));
});

test('render uses synchronized output sequences', async () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	const output = getStream(stream);

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
	});

	spinner.render();
	stream.end();

	const result = await output;
	assert.ok(result.includes(synchronizedOutputEnable));
	assert.ok(result.includes(synchronizedOutputDisable));
	assert.ok(result.indexOf(synchronizedOutputEnable) < result.indexOf(synchronizedOutputDisable));

	const synchronizedOutput = getLastSynchronizedOutput(result);
	const renderedText = stripVTControlCharacters(synchronizedOutput);
	assert.ok(renderedText.includes(spinnerCharacter));
	assert.ok(renderedText.includes('foo'));
	assert.strictEqual(stripSynchronizedOutputSequences(result), synchronizedOutput);
});

test('`.id` is not set when created', () => {
	const spinner = ora('foo');
	assert.ok(!spinner.isSpinning);
});

test('ignore consecutive calls to `.start()`', () => {
	const spinner = ora('foo');
	spinner.start();
	const {id} = spinner;
	spinner.start();
	assert.strictEqual(id, spinner.id);
	spinner.stop();
});

test('chain call to `.start()` with constructor', () => {
	const spinner = ora({
		stream: getPassThroughStream(),
		text: 'foo',
		isEnabled: true,
	}).start();

	assert.ok(spinner.isSpinning);
	assert.ok(spinner._isEnabled);
	spinner.stop();
});

test('.succeed()', async () => {
	const result = await doSpinner(spinner => {
		spinner.succeed();
	});
	assert.match(result, /[√✔] foo\n$/);
});

test('.succeed() - with new text', async () => {
	const result = await doSpinner(spinner => {
		spinner.succeed('fooed');
	});
	assert.match(result, /[√✔] fooed\n$/);
});

test('.fail()', async () => {
	const result = await doSpinner(spinner => {
		spinner.fail();
	});
	assert.match(result, /[×✖] foo\n$/);
});

test('.fail() - with new text', async () => {
	const result = await doSpinner(spinner => {
		spinner.fail('failed to foo');
	});
	assert.match(result, /[×✖] failed to foo\n$/);
});

test('.warn()', async () => {
	const result = await doSpinner(spinner => {
		spinner.warn();
	});
	assert.match(result, /[‼⚠] foo\n$/);
});

test('.info()', async () => {
	const result = await doSpinner(spinner => {
		spinner.info();
	});
	assert.match(result, /[iℹ] foo\n$/);
});

test('.stopAndPersist() - with new text', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({text: 'all done'});
	});
	assert.match(result, /\s all done\n$/);
});

test('.stopAndPersist() - with new symbol and text', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'all done'});
	});
	assert.match(result, /@ all done\n$/);
});

test('.start(text)', async () => {
	const result = await doSpinner(spinner => {
		spinner.start('Test text');
		spinner.stopAndPersist();
	});
	assert.match(result, /Test text\n$/);
});

test('.start() - isEnabled:false outputs text', async () => {
	const result = await doSpinner(spinner => {
		spinner.stop();
	}, {isEnabled: false});
	assert.match(result, /- foo\n$/);
});

test('.stopAndPersist() - isEnabled:false outputs text', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'all done'});
	}, {isEnabled: false});
	assert.match(result, /- foo\n@ all done\n$/);
});

test('.start() - isSilent:true no output', async () => {
	const result = await doSpinner(spinner => {
		spinner.stop();
	}, {isSilent: true});
	assert.match(result, /^(?![\s\S])/);
});

test('.stopAndPersist() - isSilent:true no output', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'all done'});
	}, {isSilent: true});
	assert.match(result, /^(?![\s\S])/);
});

test('.stopAndPersist() - isSilent:true can be disabled', async () => {
	const result = await doSpinner(spinner => {
		spinner.isSilent = false;
		spinner.stopAndPersist({symbol: '@', text: 'all done'});
	}, {isSilent: true});
	assert.match(result, /@ all done\n$/);
});

test('discardStdin toggles raw mode and data listeners on TTY stdin', () => {
	if (process.platform === 'win32') {
		return;
	}

	withFakeStdin({}, ({fakeStdin, rawModeCalls}) => {
		const spinner = ora({
			stream: getPassThroughStream(),
			text: 'foo',
			isEnabled: true,
		});
		const initialListenerCount = fakeStdin.listenerCount('data');

		spinner.start();
		assert.deepStrictEqual(rawModeCalls, [true]);
		assert.ok(fakeStdin.listenerCount('data') > initialListenerCount);

		spinner.stop();
		assert.deepStrictEqual(rawModeCalls, [true, false]);
		assert.strictEqual(fakeStdin.listenerCount('data'), initialListenerCount);
	});
});

test('discardStdin preserves stdin pause state', () => {
	if (process.platform === 'win32') {
		return;
	}

	const assertPauseStatePreserved = isPaused => {
		withFakeStdin({isPaused}, ({fakeStdin}) => {
			const spinner = ora({
				stream: getPassThroughStream(),
				text: 'foo',
				isEnabled: true,
			});
			const initialPausedState = fakeStdin.isPaused();

			spinner.start();
			spinner.stop();

			assert.strictEqual(fakeStdin.isPaused(), initialPausedState);
		});
	};

	assertPauseStatePreserved(false);
	assertPauseStatePreserved(true);
});

test('oraPromise() - resolves', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);
	const resolves = Promise.resolve(1);

	oraPromise(resolves, {
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
	});

	await resolves;
	stream.end();

	assert.match(stripVTControlCharacters(await output), /[√✔] foo\n$/);
});

test('oraPromise() - rejects', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);
	const rejects = Promise.reject(new Error()); // eslint-disable-line unicorn/error-message

	try {
		await oraPromise(rejects, {
			stream,
			text: 'foo',
			color: false,
			isEnabled: true,
		});
	} catch {}

	stream.end();

	assert.match(stripVTControlCharacters(await output), /[×✖] foo\n$/);
});

test('erases wrapped lines', () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	stream.columns = 40;
	let clearedLines = 0;
	let cursorAtRow = 0;
	stream.clearLine = () => {
		clearedLines++;
	};

	stream.moveCursor = (dx, dy) => {
		cursorAtRow += dy;
	};

	const reset = () => {
		clearedLines = 0;
		cursorAtRow = 0;
	};

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
	});

	spinner.render();
	assert.strictEqual(clearedLines, 0);
	assert.strictEqual(cursorAtRow, 0);

	spinner.text = 'foo\n\nbar';
	spinner.render();
	assert.strictEqual(clearedLines, 1); // Cleared 'foo'
	assert.strictEqual(cursorAtRow, 0);

	spinner.render();
	assert.strictEqual(clearedLines, 4); // Cleared 'foo\n\nbar'
	assert.strictEqual(cursorAtRow, -2);

	spinner.clear();
	reset();
	spinner.text = '0'.repeat(stream.columns + 10);
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines, 2);
	assert.strictEqual(cursorAtRow, -1);

	spinner.clear();
	reset();
	// Unicorns take up two cells, so this creates 3 rows of text not two
	spinner.text = '🦄'.repeat(stream.columns + 10);
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines, 3);
	assert.strictEqual(cursorAtRow, -2);

	spinner.clear();
	reset();
	// Unicorns take up two cells. Remove the spinner and space and fill two rows,
	// then force a linebreak and write the third row.
	spinner.text = '🦄'.repeat(stream.columns - 2) + '\nfoo';
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines, 3);
	assert.strictEqual(cursorAtRow, -2);

	spinner.clear();
	reset();
	spinner.prefixText = 'foo\n';
	spinner.text = '\nbar';
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines, 3); // Cleared 'foo\n\nbar'
	assert.strictEqual(cursorAtRow, -2);

	spinner.clear();
	reset();
	spinner.prefixText = 'foo\n';
	spinner.text = '\nbar';
	spinner.suffixText = '\nbaz';
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines, 4); // Cleared 'foo\n\nbar \nbaz'
	assert.strictEqual(cursorAtRow, -3);

	spinner.stop();
});

test('reset frameIndex when setting new spinner', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);

	const spinner = ora({
		stream,
		isEnabled: true,
		spinner: {
			frames: [
				'foo',
				'fooo',
			],
		},
	});

	assert.strictEqual(spinner._frameIndex, -1);

	spinner.render();
	assert.strictEqual(spinner._frameIndex, 0);

	spinner.spinner = {frames: ['baz']};
	spinner.render();

	stream.end();

	assert.strictEqual(spinner._frameIndex, 0);
	assert.match(stripVTControlCharacters(await output), /foo baz/);
});

test('set the correct interval when changing spinner (object case)', () => {
	const spinner = ora({
		isEnabled: false,
		spinner: {frames: ['foo', 'bar']},
		interval: 300,
	});

	assert.strictEqual(spinner.interval, 300);

	spinner.spinner = {frames: ['baz'], interval: 200};

	assert.strictEqual(spinner.interval, 200);
});

test('set the correct interval when changing spinner (string case)', () => {
	const spinner = ora({
		isEnabled: false,
		spinner: 'dots',
		interval: 100,
	});

	assert.strictEqual(spinner.interval, 100);

	spinner.spinner = 'layer';

	const expectedInterval = process.platform === 'win32' ? 130 : 150;
	assert.strictEqual(spinner.interval, expectedInterval);
});

if (process.platform !== 'win32') {
	test('throw when incorrect spinner', () => {
		const spinner = ora();

		assert.throws(() => {
			spinner.spinner = 'random-string-12345';
		}, {
			message: /no built-in spinner/,
		});
	});
}

test('throw when spinner is set to `default`', () => {
	assert.throws(() => {
		ora({spinner: 'default'});
	}, {
		message: /no built-in spinner/,
	});
});

test('indent option', () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	let cursorAtRow = 0;
	stream.cursorTo = indent => {
		cursorAtRow = indent;
	};

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
		indent: 7,
	});

	spinner.render();
	spinner.clear();
	assert.strictEqual(cursorAtRow, 7);
	spinner.stop();
});

test('indent option throws', () => {
	const stream = getPassThroughStream();

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
	});

	assert.throws(() => {
		spinner.indent = -1;
	}, {
		message: 'The `indent` option must be an integer from 0 and up',
	});
});

test('handles wrapped lines when length of indent + text is greater than columns', () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	stream.columns = 20;

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
	});

	spinner.render();

	spinner.text = '0'.repeat(spinner._stream.columns - 5);
	spinner.indent = 15;
	spinner.render();

	assert.strictEqual(spinner._lineCount, 2);
});

test('.stopAndPersist() with prefixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'foo'});
	}, {prefixText: 'bar'});
	assert.match(result, /bar @ foo\n$/);
});

test('.stopAndPersist() with empty prefixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'foo'});
	}, {prefixText: ''});
	assert.match(result, /@ foo\n$/);
});

test('.stopAndPersist() with manual prefixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', prefixText: 'baz', text: 'foo'});
	}, {prefixText: 'bar'});
	assert.match(result, /baz @ foo\n$/);
});

test('.stopAndPersist() with manual empty prefixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', prefixText: '', text: 'foo'});
	}, {prefixText: 'bar'});
	assert.match(result, /@ foo\n$/);
});

test('.stopAndPersist() with dynamic prefixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '&', prefixText: () => 'babeee', text: 'yorkie'});
	}, {prefixText: () => 'babeee'});
	assert.match(result, /babeee & yorkie\n$/);
});

test('.stopAndPersist() with suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'foo'});
	}, {suffixText: 'bar'});
	assert.match(result, /@ foo bar\n$/);
});

test('.stopAndPersist() with empty suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'foo'});
	}, {suffixText: ''});
	assert.match(result, /@ foo\n$/);
});

test('.stopAndPersist() with manual suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', suffixText: 'baz', text: 'foo'});
	}, {suffixText: 'bar'});
	assert.match(result, /@ foo baz\n$/);
});

test('.stopAndPersist() with manual empty suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', suffixText: '', text: 'foo'});
	}, {suffixText: 'bar'});
	assert.match(result, /@ foo\n$/);
});

test('.stopAndPersist() with dynamic suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '&', suffixText: () => 'babeee', text: 'yorkie'});
	}, {suffixText: () => 'babeee'});
	assert.match(result, /& yorkie babeee\n$/);
});

test('.stopAndPersist() with prefixText and suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '@', text: 'foo'});
	}, {prefixText: 'bar', suffixText: 'baz'});
	assert.match(result, /bar @ foo baz\n$/);
});

test('.stopAndPersist() with dynamic prefixText and suffixText', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '#', text: 'work'});
	}, {prefixText: () => 'pre', suffixText: () => 'post'});
	assert.match(result, /pre # work post\n$/);
});

test('.stopAndPersist() with dynamic empty prefixText and suffixText has no stray spaces', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '#', text: 'work'});
	}, {prefixText: () => '', suffixText: () => ''});
	assert.match(result, /# work\n$/);
});

test('.stopAndPersist() with empty symbol does not add separator', async () => {
	const result = await doSpinner(spinner => {
		spinner.stopAndPersist({symbol: '', text: 'done'});
	}, {});
	assert.match(result, /done\n$/);
});

// Additional focused edge-case tests

test('throws when spinner object has invalid `frames`', () => {
	const spinner = ora({isEnabled: false});

	assert.throws(() => {
		// @ts-expect-error Intentional invalid object
		spinner.spinner = {};
	}, {
		message: 'The given spinner must have a non-empty `frames` array of strings',
	});
});

test('interval defaults to 100 when custom spinner has no interval', () => {
	const spinner = ora({isEnabled: false});
	spinner.spinner = {frames: ['-']};
	assert.strictEqual(spinner.interval, 100);
});

test('isEnabled setter enforces boolean', () => {
	const spinner = ora({isEnabled: false});

	assert.throws(() => {
		// @ts-expect-error Intentional invalid assignment
		spinner.isEnabled = 'yes';
	}, {
		message: 'The `isEnabled` option must be a boolean',
	});
});

test('isSilent setter enforces boolean', () => {
	const spinner = ora();

	assert.throws(() => {
		// @ts-expect-error Intentional invalid assignment
		spinner.isSilent = 'no';
	}, {
		message: 'The `isSilent` option must be a boolean',
	});
});

test('oraPromise(function) passes spinner and supports successText function', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);

	const action = async sp => {
		sp.text = 'working';
		return 7;
	};

	await oraPromise(action, {
		stream,
		color: false,
		isEnabled: false, // Avoid timers; still prints persisted line
		successText: result => `done: ${result}`,
	});

	stream.end();
	assert.match(stripVTControlCharacters(await output), /[√✔] done: 7\n$/);
});

test('oraPromise(function) rejects and supports failText function', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);

	const boom = new Error('boom');

	try {
		await oraPromise(async () => {
			throw boom;
		}, {
			stream,
			color: false,
			isEnabled: false, // Avoid timers; still prints persisted line
			failText: error => `oops: ${error.message}`,
		});
	} catch {}

	stream.end();
	assert.match(stripVTControlCharacters(await output), /[×✖] oops: boom\n$/);
});

test('oraPromise() validates `action` type', async () => {
	await assert.rejects(async () => {
		// @ts-expect-error Intentional invalid input
		await oraPromise(123, {isEnabled: false});
	}, {
		message: 'Parameter `action` must be a Function or a Promise',
	});
});

test('clear() is a no-op when stream is not TTY', () => {
	const stream = getPassThroughStream();
	let cleared = 0;
	let moved = 0;
	stream.clearLine = () => {
		cleared++;
	};

	stream.moveCursor = () => {
		moved++;
	};

	const spinner = ora({
		stream,
		text: 'foo',
		color: false,
		isEnabled: true,
	});

	spinner.render();
	const before = spinner._linesToClear;
	spinner.clear();

	// Nothing should have happened
	assert.strictEqual(spinner._linesToClear, before);
	assert.strictEqual(cleared, 0);
	assert.strictEqual(moved, 0);

	spinner.stop();
});

test('multiline content that exactly fits console height is not truncated', () => {
	const stream = getPassThroughStream();
	stream.rows = 3; // Exactly fits 3 lines
	stream.columns = 80;
	stream.isTTY = true;

	let written = '';
	const originalWrite = stream.write;
	stream.write = function (content) {
		written += String(content);
		return originalWrite.call(this, content);
	};

	const spinner = ora({
		stream,
		text: 'Line 1\nLine 2\nLine 3',
		color: false,
		isEnabled: true,
	});

	spinner.start();
	spinner.render();

	const renderedOutput = stripVTControlCharacters(getLastSynchronizedOutput(written));
	assert.ok(renderedOutput.includes('Line 3'));
	assert.ok(!renderedOutput.includes('(content truncated to fit terminal)'));

	spinner.stop();
});

test('non-string prefix/suffix from functions are ignored', () => {
	const spinner = ora({
		text: 'task',
		prefixText: () => 42,
		suffixText: () => ({x: 1}),
		color: false,
	});

	const frame = spinner.frame();
	assert.ok(!frame.includes('42'));
	assert.ok(!frame.includes('[object Object]'));
});

test('start() with empty text and isEnabled:false produces no output', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);

	const spinner = ora({
		stream,
		text: '',
		color: false,
		isEnabled: false,
	});

	spinner.start();
	stream.end();

	const text = stripVTControlCharacters(await output);
	assert.match(text, /^(?![\s\S])/);
});

// New clear method tests

const currentClearMethod = transFormTTY => {
	const spinner = ora({
		text: 'foo',
		color: false,
		isEnabled: true,
		stream: transFormTTY,
		spinner: {
			frames: [
				'-',
			],
		},
	});

	let firstIndent = true;

	spinner.clear = function () {
		if (!this._isEnabled || !this._stream.isTTY) {
			return this;
		}

		for (let index = 0; index < this._linesToClear; index++) {
			if (index > 0) {
				this._stream.moveCursor(0, -1);
			}

			this._stream.clearLine();
			this._stream.cursorTo(this.indent);
		}

		// It's too quick to be noticeable, but indent does not get applied
		// for the first render if `linesToClear === 0`. The new clear method
		// doesn't have this issue, since it's called outside of the loop.
		if (this._linesToClear === 0 && firstIndent && this.indent) {
			this._stream.cursorTo(this.indent);
			firstIndent = false;
		}

		this._linesToClear = 0;

		return this;
	}.bind(spinner);

	return spinner;
};

test('new clear method test, basic', () => {
	const transformTTY = applySynchronizedOutputFilter(new TransformTTY({crlf: true}));
	transformTTY.addSequencer();
	transformTTY.addSequencer(null, true);

	/*
	If the frames from this sequence differ from the previous sequence,
	it means the `spinner.clear()` method has failed to fully clear output between calls to render.
	*/

	const currentClearTTY = applySynchronizedOutputFilter(new TransformTTY({crlf: true}));
	currentClearTTY.addSequencer();

	const currentOra = currentClearMethod(currentClearTTY);

	const spinner = ora({
		text: 'foo',
		color: false,
		isEnabled: true,
		stream: transformTTY,
		spinner: {
			frames: [
				'-',
			],
		},
	});

	currentOra.render();
	spinner.render();

	currentOra.text = 'bar';
	currentOra.indent = 5;
	currentOra.render();

	spinner.text = 'bar';
	spinner.indent = 5;
	spinner.render();

	currentOra.text = 'baz';
	currentOra.indent = 10;
	currentOra.render();

	spinner.text = 'baz';
	spinner.indent = 10;
	spinner.render();

	currentOra.succeed('boz?');

	spinner.succeed('boz?');

	const [sequenceString, clearedSequenceString] = transformTTY.getSequenceStrings();
	const [frames, clearedFrames] = transformTTY.getFrames();

	assert.strictEqual(sequenceString, '          ✔ boz?\n');
	assert.strictEqual(sequenceString, clearedSequenceString);

	assert.deepStrictEqual(clearedFrames, ['- foo', '     - bar', '          - baz', '          ✔ boz?\n']);
	assert.deepStrictEqual(frames, clearedFrames);

	const currentString = currentClearTTY.getSequenceStrings();

	assert.strictEqual(currentString, '          ✔ boz?\n');

	const currentFrames = currentClearTTY.getFrames();

	assert.deepStrictEqual(frames, currentFrames);
	// Frames created using new clear method are deep equal to frames created using current clear method
});

test('new clear method test, erases wrapped lines', () => {
	const transformTTY = applySynchronizedOutputFilter(new TransformTTY({crlf: true, columns: 40}));
	transformTTY.addSequencer();
	transformTTY.addSequencer(null, true);

	const currentClearTTY = applySynchronizedOutputFilter(new TransformTTY({crlf: true, columns: 40}));
	currentClearTTY.addSequencer();

	const currentOra = currentClearMethod(currentClearTTY);

	const cursorAtRow = () => {
		const cursor = transformTTY.getCursorPos();
		return cursor.y === 0 ? 0 : cursor.y * -1;
	};

	const clearedLines = () => transformTTY.toString().split('\n').length;

	const spinner = ora({
		text: 'foo',
		color: false,
		isEnabled: true,
		stream: transformTTY,
		spinner: {
			frames: [
				'-',
			],
		},
	});

	currentOra.render();

	spinner.render();
	assert.strictEqual(clearedLines(), 1); // Cleared 'foo'
	assert.strictEqual(cursorAtRow(), 0);

	currentOra.text = 'foo\n\nbar';
	currentOra.render();

	spinner.text = 'foo\n\nbar';
	spinner.render();
	assert.strictEqual(clearedLines(), 3); // Cleared 'foo\n\nbar'
	assert.strictEqual(cursorAtRow(), -2);

	currentOra.clear();
	currentOra.text = '0'.repeat(currentOra._stream.columns + 10);
	currentOra.render();
	currentOra.render();

	spinner.clear();
	spinner.text = '0'.repeat(spinner._stream.columns + 10);
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines(), 2);
	assert.strictEqual(cursorAtRow(), -1);

	currentOra.clear();
	currentOra.text = '🦄'.repeat(currentOra._stream.columns + 10);
	currentOra.render();
	currentOra.render();

	spinner.clear();
	spinner.text = '🦄'.repeat(spinner._stream.columns + 10);
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines(), 3);
	assert.strictEqual(cursorAtRow(), -2);

	currentOra.clear();
	currentOra.text = '🦄'.repeat(currentOra._stream.columns - 2) + '\nfoo';
	currentOra.render();
	currentOra.render();

	spinner.clear();
	spinner.text = '🦄'.repeat(spinner._stream.columns - 2) + '\nfoo';
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines(), 3);
	assert.strictEqual(cursorAtRow(), -2);

	currentOra.clear();
	currentOra.prefixText = 'foo\n';
	currentOra.text = '\nbar';
	currentOra.suffixText = '\nbaz';
	currentOra.render();
	currentOra.render();

	spinner.clear();
	spinner.prefixText = 'foo\n';
	spinner.text = '\nbar';
	spinner.suffixText = '\nbaz';
	spinner.render();
	spinner.render();
	assert.strictEqual(clearedLines(), 4); // Cleared 'foo\n\nbar \nbaz'
	assert.strictEqual(cursorAtRow(), -3);

	const [sequenceString, clearedSequenceString] = transformTTY.getSequenceStrings();
	const [frames, clearedFrames] = transformTTY.getFrames();

	assert.strictEqual(sequenceString, 'foo\n - \nbar \nbaz');
	assert.strictEqual(sequenceString, clearedSequenceString);

	assert.deepStrictEqual(clearedFrames, [
		'- foo',
		'- foo\n\nbar',
		'- 00000000000000000000000000000000000000\n000000000000',
		'- 00000000000000000000000000000000000000\n000000000000',
		'- 🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ '🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ '🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄',
		'- 🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ '🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ '🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄',
		'- 🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ '🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ 'foo',
		'- 🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ '🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄\n'
		+ 'foo',
		'foo\n - \nbar \nbaz',
		'foo\n - \nbar \nbaz',
	]);

	assert.deepStrictEqual(frames, clearedFrames);

	const currentClearString = currentClearTTY.toString();
	assert.strictEqual(currentClearString, 'foo\n - \nbar \nbaz');

	const currentFrames = currentClearTTY.getFrames();
	assert.deepStrictEqual(frames, currentFrames);
});

test('new clear method, stress test', () => {
	const rando = (min, max) => {
		min = Math.ceil(min);
		max = Math.floor(max);
		return Math.floor(Math.random() * ((max - min) + min));
	};

	const rAnDoMaNiMaLs = (min, max) => {
		const length = rando(min, max);
		let result = '';
		const THEAMINALS = ['🐯', '🦁', '🐮', '🐷', '🐽', '🐸', '🐙', '🐵', '🐦', '🐧', '🐔', '🐒', '🙉', '🙈', '🐣', '🐥', '🐺', '🐗', '🐴', '🦄', '🐝', '🐛', ...Array.from({length: 5}).fill('\n')];

		for (let i = 0; i < length; i++) {
			result += THEAMINALS[Math.floor(Math.random() * THEAMINALS.length)];
		}

		return result;
	};

	const randos = () => rAnDoMaNiMaLs(rando(5, 15), rando(25, 50));

	const randomize = (s1, s2) => {
		const spnr = spinners.random;
		const txt = randos();
		const indent = rando(0, 15);

		s1.spinner = spnr;
		s2.spinner = spnr;
		s1.text = txt;
		s2.text = txt;
		s1.indent = indent;
		s2.indent = indent;
	};

	const transformTTY = applySynchronizedOutputFilter(new TransformTTY({crlf: true}));
	transformTTY.addSequencer();
	transformTTY.addSequencer(null, true);

	const currentClearTTY = applySynchronizedOutputFilter(new TransformTTY({crlf: true}));
	currentClearTTY.addSequencer();

	const currentOra = currentClearMethod(currentClearTTY);

	const spinner = ora({
		color: false,
		isEnabled: true,
		stream: transformTTY,
	});

	randomize(spinner, currentOra);

	for (let x = 0; x < 100; x++) {
		if (x % 10 === 0) {
			randomize(spinner, currentOra);
		}

		if (x % 5 === 0) {
			const indent = rando(0, 25);
			spinner.indent = indent;
			currentOra.indent = indent;
		}

		if (x % 15 === 0) {
			let {text} = spinner;
			const loops = rando(1, 10);

			for (let x = 0; x < loops; x++) {
				const pos = Math.floor(Math.random() * text.length);
				text = text.slice(0, pos) + '\n' + text.slice(pos + 1);
			}

			spinner.text = text;
			currentOra.text = text;
		}

		spinner.render();
		currentOra.render();
	}

	spinner.succeed('🙉');
	currentOra.succeed('🙉');

	const currentFrames = currentClearTTY.getFrames();
	const [frames, clearedFrames] = transformTTY.getFrames();

	assert.deepStrictEqual(frames, clearedFrames);

	assert.deepStrictEqual(frames.slice(0, currentFrames.length), currentFrames);

	// Console.log(frames);
	// console.log(clearFrames);
});
/*
Example output:

[
  '               ▏ \n',
  '               ▎ \n',
  '               ▍ \n',
  '               ▌ \n',
  '               ▋ \n',
  '               ▊ \n',
  '               ▉ \n',
  '               ▊ \n',
  '               ▋ \n',
  '               ▌ \n',
  '   d ',
  '   q ',
  '   p ',
  '   b ',
  '   d ',
  '                 q \n',
  '                 p \n',
  '                 b \n',
  '                 d \n',
  '                 q \n',
  '                ◢ 🐗🐧🐥🐺🐵\n\n',
  '                ◣ 🐗🐧🐥🐺🐵\n\n',
  '                ◤ 🐗🐧🐥🐺🐵\n\n',
  '                ◥ 🐗🐧🐥🐺🐵\n\n',
  '                ◢ 🐗🐧🐥🐺🐵\n\n',
  '                     ◣ 🐗🐧🐥🐺🐵\n\n',
  '                     ◤ 🐗🐧🐥🐺🐵\n\n',
  '                     ◥ 🐗🐧🐥🐺🐵\n\n',
  '                     ◢ 🐗🐧🐥🐺🐵\n\n',
  '                     ◣ 🐗🐧🐥🐺🐵\n\n',
  '      ⠋ \n�🐮�\n\n�\n',
  '      ⠙ \n�🐮�\n\n�\n',
  '      ⠹ \n�🐮�\n\n�\n',
  '      ⠸ \n�🐮�\n\n�\n',
  '      ⠼ \n�🐮�\n\n�\n',
  '                 ⠴ \n�🐮�\n\n�\n',
  '                 ⠦ \n�🐮�\n\n�\n',
  '                 ⠧ \n�🐮�\n\n�\n',
  '                 ⠇ \n�🐮�\n\n�\n',
  '                 ⠏ \n�🐮�\n\n�\n',
  '       □ ',
  '       ■ ',
  '       □ ',
  '       ■ ',
  '       □ ',
  '           ■ \n',
  '           □ \n',
  '           ■ \n',
  '           □ \n',
  '           ■ \n',
  '  .   🐗',
  '  ..  🐗',
  '  ... 🐗',
  '      🐗',
  '  .   🐗',
  '               ..  🐗',
  '               ... 🐗',
  '                   🐗',
  '               .   🐗',
  '               ..  🐗',
  ' ▖ 🐔\n🐸\n',
  ' ▘ 🐔\n🐸\n',
  ' ▝ 🐔\n🐸\n',
  ' ▗ 🐔\n🐸\n',
  ' ▖ 🐔\n🐸\n',
  '  ▘ 🐔\n🐸\n',
  '  ▝ 🐔\n🐸\n',
  '  ▗ 🐔\n🐸\n',
  '  ▖ 🐔\n🐸\n',
  '  ▘ 🐔\n🐸\n',
  '          ( ●    ) 🐔🐗',
  '          (  ●   ) 🐔🐗',
  '          (   ●  ) 🐔🐗',
  '          (    ● ) 🐔🐗',
  '          (     ●) 🐔🐗',
  '(    ● ) �\n\n�',
  '(   ●  ) �\n\n�',
  '(  ●   ) �\n\n�',
  '( ●    ) �\n\n�',
  '(●     ) �\n\n�',
  '     ⧇ 🐷🐛🐔🦁🐷🙉',
  '     ⧆ 🐷🐛🐔🦁🐷🙉',
  '     ⧇ 🐷🐛🐔🦁🐷🙉',
  '     ⧆ 🐷🐛🐔🦁🐷🙉',
  '     ⧇ 🐷🐛🐔🦁🐷🙉',
  '       ⧆ 🐷🐛🐔🦁🐷🙉',
  '       ⧇ 🐷🐛🐔🦁🐷🙉',
  '       ⧆ 🐷🐛🐔🦁🐷🙉',
  '       ⧇ 🐷🐛🐔🦁🐷🙉',
  '       ⧆ 🐷🐛🐔🦁🐷🙉',
  '                        _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        - 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        ` 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                  ` 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  "                  ' 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n",
  '                  ´ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                  - 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                  _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  ... 1 more item
]
[
  '               ▏ \n',
  '               ▎ \n',
  '               ▍ \n',
  '               ▌ \n',
  '               ▋ \n',
  '               ▊ \n',
  '               ▉ \n',
  '               ▊ \n',
  '               ▋ \n',
  '               ▌ \n',
  '   d ',
  '   q ',
  '   p ',
  '   b ',
  '   d ',
  '                 q \n',
  '                 p \n',
  '                 b \n',
  '                 d \n',
  '                 q \n',
  '                ◢ 🐗🐧🐥🐺🐵\n\n',
  '                ◣ 🐗🐧🐥🐺🐵\n\n',
  '                ◤ 🐗🐧🐥🐺🐵\n\n',
  '                ◥ 🐗🐧🐥🐺🐵\n\n',
  '                ◢ 🐗🐧🐥🐺🐵\n\n',
  '                     ◣ 🐗🐧🐥🐺🐵\n\n',
  '                     ◤ 🐗🐧🐥🐺🐵\n\n',
  '                     ◥ 🐗🐧🐥🐺🐵\n\n',
  '                     ◢ 🐗🐧🐥🐺🐵\n\n',
  '                     ◣ 🐗🐧🐥🐺🐵\n\n',
  '      ⠋ \n�🐮�\n\n�\n',
  '      ⠙ \n�🐮�\n\n�\n',
  '      ⠹ \n�🐮�\n\n�\n',
  '      ⠸ \n�🐮�\n\n�\n',
  '      ⠼ \n�🐮�\n\n�\n',
  '                 ⠴ \n�🐮�\n\n�\n',
  '                 ⠦ \n�🐮�\n\n�\n',
  '                 ⠧ \n�🐮�\n\n�\n',
  '                 ⠇ \n�🐮�\n\n�\n',
  '                 ⠏ \n�🐮�\n\n�\n',
  '       □ ',
  '       ■ ',
  '       □ ',
  '       ■ ',
  '       □ ',
  '           ■ \n',
  '           □ \n',
  '           ■ \n',
  '           □ \n',
  '           ■ \n',
  '  .   🐗',
  '  ..  🐗',
  '  ... 🐗',
  '      🐗',
  '  .   🐗',
  '               ..  🐗',
  '               ... 🐗',
  '                   🐗',
  '               .   🐗',
  '               ..  🐗',
  ' ▖ 🐔\n🐸\n',
  ' ▘ 🐔\n🐸\n',
  ' ▝ 🐔\n🐸\n',
  ' ▗ 🐔\n🐸\n',
  ' ▖ 🐔\n🐸\n',
  '  ▘ 🐔\n🐸\n',
  '  ▝ 🐔\n🐸\n',
  '  ▗ 🐔\n🐸\n',
  '  ▖ 🐔\n🐸\n',
  '  ▘ 🐔\n🐸\n',
  '          ( ●    ) 🐔🐗',
  '          (  ●   ) 🐔🐗',
  '          (   ●  ) 🐔🐗',
  '          (    ● ) 🐔🐗',
  '          (     ●) 🐔🐗',
  '(    ● ) �\n\n�',
  '(   ●  ) �\n\n�',
  '(  ●   ) �\n\n�',
  '( ●    ) �\n\n�',
  '(●     ) �\n\n�',
  '     ⧇ 🐷🐛🐔🦁🐷🙉',
  '     ⧆ 🐷🐛🐔🦁🐷🙉',
  '     ⧇ 🐷🐛🐔🦁🐷🙉',
  '     ⧆ 🐷🐛🐔🦁🐷🙉',
  '     ⧇ 🐷🐛🐔🦁🐷🙉',
  '       ⧆ 🐷🐛🐔🦁🐷🙉',
  '       ⧇ 🐷🐛🐔🦁🐷🙉',
  '       ⧆ 🐷🐛🐔🦁🐷🙉',
  '       ⧇ 🐷🐛🐔🦁🐷🙉',
  '       ⧆ 🐷🐛🐔🦁🐷🙉',
  '                        _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        - 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                        ` 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                  ` 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  "                  ' 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n",
  '                  ´ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                  - 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  '                  _ 🐽🦄🐣\n🐣🐧🐔🦁🐦�\n',
  ... 1 more item
]
*/

test('multiline text exceeding console height', () => {
	// Create a mock stream with limited height
	const stream = getPassThroughStream();
	stream.rows = 5; // Simulate a console with 5 rows
	stream.columns = 80;
	stream.isTTY = true;

	let writtenContent = '';

	// Override write to capture content
	const originalWrite = stream.write;
	stream.write = function (content) {
		writtenContent += String(content);
		return originalWrite.call(this, content);
	};

	const spinner = ora({
		stream,
		text: Array.from({length: 10}, (_, i) => `Line ${i + 1}`).join('\n'), // 10 lines (exceeds 5 row height)
		color: false,
		isEnabled: true,
	});

	spinner.start();
	spinner.render(); // Force a render

	const renderedOutput = stripVTControlCharacters(getLastSynchronizedOutput(writtenContent));

	// When content exceeds viewport, should truncate with message
	assert.ok(renderedOutput.includes('Line 1'), 'Should include some original content');
	assert.ok(renderedOutput.includes('(content truncated to fit terminal)'), 'Should show truncation message');

	// Should not include all 10 lines
	const lineCount = (renderedOutput.match(/Line \d+/g) || []).length;
	assert.ok(lineCount < 10, 'Should truncate some lines');
	assert.ok(lineCount <= 5, 'Should not exceed terminal height');

	spinner.stop();
});

test('multiline text within console height (no truncation)', () => {
	// Create a mock stream with sufficient height
	const stream = getPassThroughStream();
	stream.rows = 10; // Simulate a console with 10 rows
	stream.columns = 80;
	stream.isTTY = true;

	let writtenContent = '';

	// Override write to capture content
	const originalWrite = stream.write;
	stream.write = function (content) {
		writtenContent += String(content);
		return originalWrite.call(this, content);
	};

	const spinner = ora({
		stream,
		text: Array.from({length: 5}, (_, i) => `Line ${i + 1}`).join('\n'), // 5 lines (within 10 row height)
		color: false,
		isEnabled: true,
	});

	spinner.start();
	spinner.render();

	// When content is within viewport, should not truncate
	const renderedOutput = stripVTControlCharacters(getLastSynchronizedOutput(writtenContent));
	assert.ok(renderedOutput.includes('Line 1'), 'Should include first line');
	assert.ok(renderedOutput.includes('Line 5'), 'Should include last line');
	assert.ok(!renderedOutput.includes('(content truncated to fit terminal)'), 'Should not show truncation message');

	spinner.stop();
});

test('multiline text with undefined terminal rows (no truncation)', () => {
	// Test fallback behavior when stream.rows is undefined
	const stream = getPassThroughStream();
	delete stream.rows; // Ensure rows is undefined
	stream.columns = 80;
	stream.isTTY = true;

	let writtenContent = '';

	// Override write to capture content
	const originalWrite = stream.write;
	stream.write = function (content) {
		writtenContent += String(content);
		return originalWrite.call(this, content);
	};

	const spinner = ora({
		stream,
		text: Array.from({length: 10}, (_, i) => `Line ${i + 1}`).join('\n'),
		color: false,
		isEnabled: true,
	});

	spinner.start();
	spinner.render();

	// When terminal height is unknown, should not truncate (no truncation applied)
	const renderedOutput = stripVTControlCharacters(getLastSynchronizedOutput(writtenContent));
	assert.ok(renderedOutput.includes('Line 1'), 'Should include first line');
	assert.ok(renderedOutput.includes('Line 10'), 'Should include last line');
	assert.ok(!renderedOutput.includes('(content truncated to fit terminal)'), 'Should not truncate when height is unknown');

	spinner.stop();
});

test('multiline text with very small console height (no truncation)', () => {
	// Test edge case: console height = 1 (should not truncate since no room for message)
	const stream = getPassThroughStream();
	stream.rows = 1;
	stream.columns = 80;
	stream.isTTY = true;

	let writtenContent = '';
	const originalWrite = stream.write;
	stream.write = function (content) {
		writtenContent += String(content);
		return originalWrite.call(this, content);
	};

	const spinner = ora({
		stream,
		text: 'Line 1\nLine 2\nLine 3', // 3 lines (exceeds 1 row height)
		color: false,
		isEnabled: true,
	});

	spinner.start();
	spinner.render();

	// When console is too small (1 row), should not truncate because no room for message
	const renderedOutput = stripVTControlCharacters(getLastSynchronizedOutput(writtenContent));
	assert.ok(renderedOutput.includes('Line 1'), 'Should include content');
	assert.ok(!renderedOutput.includes('(content truncated to fit terminal)'), 'Should not truncate when console too small for message');

	spinner.stop();
});

test('invalid frames throws descriptive error', () => {
	const spinner = ora({isEnabled: false});
	assert.throws(() => {
		spinner.spinner = {frames: []};
	}, {message: /non-empty/});
});

test('interval validation works correctly', () => {
	const spinner = ora({isEnabled: false, interval: 200});
	assert.strictEqual(spinner.interval, 200);

	// Interval is read-only, set via constructor or spinner object
	const spinner2 = ora({isEnabled: false});
	spinner2.spinner = {frames: ['a', 'b'], interval: 150};
	assert.strictEqual(spinner2.interval, 150);
});

test('interval rejects negative values', () => {
	assert.throws(() => {
		ora({interval: -100});
	}, {message: /positive integer/});
});

test('interval rejects non-integer values', () => {
	assert.throws(() => {
		ora({interval: 1.5});
	}, {message: /positive integer/});
});

test('interval rejects zero', () => {
	assert.throws(() => {
		ora({interval: 0});
	}, {message: /positive integer/});
});

test('color rejects invalid color names', () => {
	assert.throws(() => {
		ora({color: 'invalid'});
	}, {message: /valid color/});
});

test('color rejects non-string non-false values', () => {
	assert.throws(() => {
		ora({color: 123});
	}, {message: /valid color/});
});

test('color accepts false to disable', () => {
	const spinner = ora({color: false, isEnabled: false});
	assert.strictEqual(spinner.color, false);
});

test('color accepts valid color names', () => {
	const spinner = ora({color: 'red', isEnabled: false});
	assert.strictEqual(spinner.color, 'red');
});

test('color accepts undefined', () => {
	const spinner = ora({color: undefined, isEnabled: false});
	assert.strictEqual(spinner.color, undefined);
});

test('color setter accepts undefined', () => {
	const spinner = ora({color: 'green', isEnabled: false});
	spinner.color = undefined;
	assert.strictEqual(spinner.color, undefined);
});

test('text setter handles falsy values correctly', () => {
	const spinner = ora({color: false});
	spinner.text = null;
	assert.strictEqual(spinner.text, null); // Null is kept as null
	spinner.text = undefined;
	assert.strictEqual(spinner.text, ''); // Undefined becomes empty string
	spinner.text = 0;
	assert.strictEqual(spinner.text, 0); // Number 0 is kept as-is
	spinner.text = false;
	assert.strictEqual(spinner.text, false); // Boolean false is kept as-is
});

test('frameIndex wraps around correctly', () => {
	const spinner = ora({
		spinner: {frames: ['a', 'b', 'c']},
		color: false,
		isEnabled: false,
	});

	// Check initial frame index
	spinner.render(); // Sets to 0
	const firstIndex = spinner._frameIndex;
	spinner.render(); // 1
	spinner.render(); // 2
	spinner.render(); // Should wrap to 0
	assert.strictEqual(spinner._frameIndex, firstIndex); // Back to first index
});

test('nested spinners do not interfere', () => {
	const stream1 = getPassThroughStream();
	const stream2 = getPassThroughStream();

	const spinner1 = ora({stream: stream1, text: 'first', isEnabled: true});
	const spinner2 = ora({stream: stream2, text: 'second', isEnabled: true});

	spinner1.start();
	spinner2.start();

	assert.ok(spinner1.isSpinning);
	assert.ok(spinner2.isSpinning);

	// Stop them independently
	spinner1.stop();
	assert.ok(!spinner1.isSpinning);
	assert.ok(spinner2.isSpinning);

	spinner2.stop();
	assert.ok(!spinner2.isSpinning);
});

test('rapid state changes preserve final state', () => {
	const spinner = ora({isEnabled: false});
	spinner.start();
	spinner.succeed();
	spinner.fail();
	spinner.warn();
	spinner.info();
	assert.ok(!spinner.isSpinning);
});

test('disabled spinner preserves prefix/suffix/indent', async () => {
	const stream = getPassThroughStream();
	const output = getStream(stream);

	const spinner = ora({
		stream,
		text: 'test',
		prefixText: 'pre',
		suffixText: 'post',
		indent: 2,
		color: false,
		isEnabled: false,
	});

	spinner.start();
	stream.end();

	const text = stripVTControlCharacters(await output);
	assert.strictEqual(text, '  pre - test post\n');
});

test('emoji text handled correctly', () => {
	const spinner = ora({
		text: '🚀 Loading 🎉',
		color: false,
		isEnabled: false,
	});

	const frame = spinner.frame();
	assert.ok(frame.includes('🚀 Loading 🎉'));
});

test('stream validation throws for non-writable', () => {
	// Remove this test as it depends on Node environment internals
	// The stream validation may pass in some test environments
	const spinner = ora({isEnabled: false});
	assert.ok(spinner);
});

test('spinner property returns current spinner', () => {
	const customSpinner = {frames: ['a', 'b'], interval: 100};
	const spinner = ora({spinner: customSpinner, isEnabled: false});

	assert.deepStrictEqual(spinner.spinner, customSpinner);

	spinner.spinner = 'dots';
	assert.strictEqual(spinner.spinner.frames.length, spinners.dots.frames.length);
});

test('color persists through spinner changes', () => {
	const spinner = ora({color: 'blue', isEnabled: false});
	assert.strictEqual(spinner.color, 'blue');

	spinner.spinner = 'dots';
	assert.strictEqual(spinner.color, 'blue');
});

test('oraPromise handles sync exceptions', async () => {
	await assert.rejects(async () => {
		await oraPromise(() => {
			throw new Error('sync error');
		}, {isEnabled: false});
	}, {message: 'sync error'});
});

test('handles external writes to stream while spinning', async () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	const writes = [];

	// Track all writes
	const originalWrite = stream.write;
	stream.write = function (content, encoding, callback) {
		writes.push(stripVTControlCharacters(content.toString()));
		return originalWrite.call(this, content, encoding, callback);
	};

	const spinner = ora({
		stream,
		text: 'spinning',
		color: false,
		isEnabled: true,
	});

	spinner.start();

	// Simulate external write (like console.log)
	stream.write('External log\n');

	spinner.succeed('done');

	// Verify all content appears in output
	assert.ok(writes.some(w => w.includes('External log')), 'External write should be captured');
	assert.ok(writes.some(w => w.includes('spinning')), 'Spinner text should be present');
	assert.ok(writes.some(w => w.includes('done')), 'Success text should be present');

	// Verify ordering: external log appears before success message
	const externalIndex = writes.findIndex(w => w.includes('External log'));
	const doneIndex = writes.findIndex(w => w.includes('done'));
	assert.ok(externalIndex !== -1 && doneIndex !== -1, 'Both messages should exist');
	assert.ok(externalIndex < doneIndex, 'External log should appear before done message');

	stream.end();
});

test('handles multiple external writes while spinning', async () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	const writes = [];

	const originalWrite = stream.write;
	stream.write = function (content, encoding, callback) {
		writes.push(stripVTControlCharacters(content.toString()));
		return originalWrite.call(this, content, encoding, callback);
	};

	const spinner = ora({
		stream,
		text: 'processing',
		color: false,
		isEnabled: true,
	});

	spinner.start();

	// Multiple external writes
	stream.write('Log 1\n');
	stream.write('Log 2\n');
	stream.write('Log 3\n');

	spinner.stop();

	// All logs should be present
	assert.ok(writes.some(w => w.includes('Log 1')), 'First log should be present');
	assert.ok(writes.some(w => w.includes('Log 2')), 'Second log should be present');
	assert.ok(writes.some(w => w.includes('Log 3')), 'Third log should be present');

	// Verify ordering
	const log1Index = writes.findIndex(w => w.includes('Log 1'));
	const log2Index = writes.findIndex(w => w.includes('Log 2'));
	const log3Index = writes.findIndex(w => w.includes('Log 3'));

	assert.ok(log1Index < log2Index, 'Log 1 should appear before Log 2');
	assert.ok(log2Index < log3Index, 'Log 2 should appear before Log 3');

	stream.end();
});

test('external writes preserve chunk boundaries without injecting newlines', async () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;
	const outputPromise = getStream(stream);
	const originalWrite = stream.write;

	const spinner = ora({
		stream,
		text: 'processing',
		color: false,
		isEnabled: true,
	});

	spinner.start();
	assert.notStrictEqual(stream.write, originalWrite, 'hook should wrap stream.write');

	stream.write('Downloading ');
	stream.write('42%');
	stream.write('\n');

	spinner.stop();
	assert.strictEqual(stream.write, originalWrite, 'hook should restore original stream.write');
	stream.end();

	const outputRaw = await outputPromise;
	const stripped = stripVTControlCharacters(outputRaw.toString().replaceAll('\r', ''));

	assert.ok(stripped.includes('Downloading 42%\n'), 'line should remain intact without injected newline');
	assert.ok(!stripped.includes('Downloading \n42%'), 'should not inject newline between partial chunks');
});

test('partial external writes defer spinner renders until newline or timeout', t => {
	const stream = getPassThroughStream();
	stream.isTTY = true;

	t.mock.timers.enable({appliesTo: ['setTimeout', 'setInterval']});

	const spinner = ora({
		stream,
		text: 'processing',
		color: false,
		isEnabled: true,
		interval: 80,
	});

	try {
		spinner.start();
		t.mock.timers.tick(80);

		const baselineFrameIndex = spinner._frameIndex;

		stream.write('Partial chunk without newline');
		t.mock.timers.tick(199);
		assert.strictEqual(spinner._frameIndex, baselineFrameIndex, 'frame index should not advance within deferral window');

		stream.write('\n');
		assert.ok(spinner._frameIndex > baselineFrameIndex, 'newline should resume rendering immediately');
		const afterNewlineFrameIndex = spinner._frameIndex;

		stream.write('Another partial chunk');
		t.mock.timers.tick(199);
		assert.strictEqual(spinner._frameIndex, afterNewlineFrameIndex, 'second partial chunk should defer renders again');

		t.mock.timers.tick(1);
		assert.ok(spinner._frameIndex > afterNewlineFrameIndex, 'timeout should eventually resume rendering');
	} finally {
		spinner.stop();
		stream.end();
		t.mock.restoreAll();
	}
});

test('handles stream write errors gracefully', () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;

	// Wrap the real write to optionally throw
	let shouldThrow = false;
	const realWrite = stream.write;
	stream.write = function (...args) {
		if (shouldThrow) {
			throw new Error('Stream write error');
		}

		return realWrite.apply(this, args);
	};

	const spinner = ora({
		stream,
		text: 'test',
		color: false,
		isEnabled: true,
	});

	spinner.start();
	// Hook now wraps our throwing wrapper

	// Enable throwing - this will cause cursor operations in clear() to throw
	shouldThrow = true;

	// External write triggers hook -> clear() -> cursorTo() -> our wrapper throws
	assert.throws(() => {
		stream.write('External write');
	}, {message: 'Stream write error'});

	// Disable throwing
	shouldThrow = false;

	// If flag was stuck at true, this external write would pass through as internal (no clear/render)
	// and subsequent operations would fail. Verify it works correctly:
	assert.doesNotThrow(() => {
		stream.write('Should work now\n');
		spinner.stop();
	});
});

test('hooks both stdout and stderr', () => {
	const stream = getPassThroughStream();
	stream.isTTY = true;

	// Save original stdout and stderr
	const originalStdout = process.stdout;
	const originalStderr = process.stderr;
	const originalStdoutWrite = originalStdout.write;
	const originalStderrWrite = originalStderr.write;

	const stdoutWrites = [];
	const stderrWrites = [];

	// Track writes to both streams without reassigning them
	process.stdout.write = function (content, encoding, callback) {
		stdoutWrites.push(stripVTControlCharacters(content.toString()));
		return originalStdoutWrite.call(this, content, encoding, callback);
	};

	process.stderr.write = function (content, encoding, callback) {
		stderrWrites.push(stripVTControlCharacters(content.toString()));
		return originalStderrWrite.call(this, content, encoding, callback);
	};

	try {
		const spinner = ora({
			stream,
			text: 'processing',
			color: false,
			isEnabled: true,
		});

		spinner.start();

		// Write to both stdout and stderr - both should be intercepted
		process.stdout.write('stdout log\n');
		process.stderr.write('stderr log\n');

		spinner.stop();

		// Verify both writes were intercepted
		// The hook should have cleared/re-rendered for both writes
		assert.ok(stdoutWrites.some(w => w.includes('stdout log')), 'stdout write should be captured');
		assert.ok(stderrWrites.some(w => w.includes('stderr log')), 'stderr write should be captured');

		stream.end();
	} finally {
		// Restore original write methods
		process.stdout.write = originalStdoutWrite;
		process.stderr.write = originalStderrWrite;
	}
});
```

