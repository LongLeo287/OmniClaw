---
id: github.com-sindresorhus-is-a4e7f3f6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.795355
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_is_a4e7f3f6
> **Extracted on:** 2026-04-01 12:00:46
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521645/github.com_sindresorhus_is_a4e7f3f6

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
/distribution
.tsimp
```

## File: `.npmrc`
```
package-lock=false
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
	"name": "@sindresorhus/is",
	"version": "7.2.0",
	"description": "Type check values",
	"license": "MIT",
	"repository": "sindresorhus/is",
	"funding": "https://github.com/sindresorhus/is?sponsor=1",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": {
		"types": "./distribution/index.d.ts",
		"default": "./distribution/index.js"
	},
	"sideEffects": false,
	"engines": {
		"node": ">=18"
	},
	"scripts": {
		"build": "del distribution && tsc",
		"test": "tsc --noEmit && xo && ava",
		"prepare": "npm run build"
	},
	"files": [
		"distribution"
	],
	"keywords": [
		"type",
		"types",
		"is",
		"check",
		"checking",
		"validate",
		"validation",
		"utility",
		"util",
		"typeof",
		"instanceof",
		"object",
		"assert",
		"assertion",
		"test",
		"kind",
		"primitive",
		"verify",
		"compare",
		"typescript",
		"typeguards",
		"types"
	],
	"devDependencies": {
		"@sindresorhus/tsconfig": "^6.0.0",
		"@types/jsdom": "^21.1.7",
		"@types/node": "^20.14.10",
		"@types/zen-observable": "^0.8.7",
		"ava": "^6.1.3",
		"del-cli": "^5.1.0",
		"expect-type": "^0.19.0",
		"jsdom": "^24.1.0",
		"rxjs": "^7.8.1",
		"tempy": "^3.1.0",
		"tsimp": "2.0.11",
		"typescript": "5.5.3",
		"xo": "^0.58.0",
		"zen-observable": "^0.10.0"
	},
	"ava": {
		"environmentVariables": {
			"TSIMP_DIAG": "error"
		},
		"extensions": {
			"ts": "module"
		},
		"nodeArguments": [
			"--import=tsimp/import"
		]
	}
}
```

## File: `readme.md`
```markdown
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
> [Prefer using `Uint8Array` instead of `Buffer`.](https://sindresorhus.com/blog/goodbye-nodejs-buffer)

##### .blob(value)
##### .object(value)

Keep in mind that [functions are objects too](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions).

##### .numericString(value)

Returns `true` for a string that represents a number satisfying `is.number`, for example, `'42'` and `'-8.3'`.

Note: `'NaN'` returns `false`, but `'Infinity'` and `'-Infinity'` return `true`.

##### .regExp(value)
##### .date(value)
##### .error(value)
##### .nativePromise(value)
##### .promise(value)

Returns `true` for any object with a `.then()` and `.catch()` method. Prefer this one over `.nativePromise()` as you usually want to allow userland promise implementations too.

##### .generator(value)

Returns `true` for any object that implements its own `.next()` and `.throw()` methods and has a function definition for `Symbol.iterator`.

##### .generatorFunction(value)

##### .asyncFunction(value)

Returns `true` for any `async` function that can be called with the `await` operator.

```js
is.asyncFunction(async () => {});
//=> true

is.asyncFunction(() => {});
//=> false
```

##### .asyncGenerator(value)

```js
is.asyncGenerator(
	(async function * () {
		yield 4;
	})()
);
//=> true

is.asyncGenerator(
	(function * () {
		yield 4;
	})()
);
//=> false
```

##### .asyncGeneratorFunction(value)

```js
is.asyncGeneratorFunction(async function * () {
	yield 4;
});
//=> true

is.asyncGeneratorFunction(function * () {
	yield 4;
});
//=> false
```

##### .boundFunction(value)

Returns `true` for any `bound` function.

```js
is.boundFunction(() => {});
//=> true

is.boundFunction(function () {}.bind(null));
//=> true

is.boundFunction(function () {});
//=> false
```

##### .map(value)
##### .set(value)
##### .weakMap(value)
##### .weakSet(value)
##### .weakRef(value)

#### Typed arrays

##### .int8Array(value)
##### .uint8Array(value)
##### .uint8ClampedArray(value)
##### .int16Array(value)
##### .uint16Array(value)
##### .int32Array(value)
##### .uint32Array(value)
##### .float32Array(value)
##### .float64Array(value)
##### .bigInt64Array(value)
##### .bigUint64Array(value)

#### Structured data

##### .arrayBuffer(value)
##### .sharedArrayBuffer(value)
##### .dataView(value)

##### .enumCase(value, enum)

TypeScript-only. Returns `true` if `value` is a member of `enum`.

```ts
enum Direction {
	Ascending = 'ascending',
	Descending = 'descending'
}

is.enumCase('ascending', Direction);
//=> true

is.enumCase('other', Direction);
//=> false
```

#### Emptiness

##### .emptyString(value)

Returns `true` if the value is a `string` and the `.length` is 0.

##### .emptyStringOrWhitespace(value)

Returns `true` if `is.emptyString(value)` or if it's a `string` that is all whitespace.

##### .nonEmptyString(value)

Returns `true` if the value is a `string` and the `.length` is more than 0.

##### .nonEmptyStringAndNotWhitespace(value)

Returns `true` if the value is a `string` that is not empty and not whitespace.

```js
const values = ['property1', '', null, 'property2', '    ', undefined];

values.filter(is.nonEmptyStringAndNotWhitespace);
//=> ['property1', 'property2']
```

##### .emptyArray(value)

Returns `true` if the value is an `Array` and the `.length` is 0.

##### .nonEmptyArray(value)

Returns `true` if the value is an `Array` and the `.length` is more than 0.

##### .emptyObject(value)

Returns `true` if the value is an `Object` and `Object.keys(value).length` is 0.

Please note that `Object.keys` returns only own enumerable properties. Hence something like this can happen:

```js
const object1 = {};

Object.defineProperty(object1, 'property1', {
	value: 42,
	writable: true,
	enumerable: false,
	configurable: true
});

is.emptyObject(object1);
//=> true
```

##### .nonEmptyObject(value)

Returns `true` if the value is an `Object` and `Object.keys(value).length` is more than 0.

##### .emptySet(value)

Returns `true` if the value is a `Set` and the `.size` is 0.

##### .nonEmptySet(Value)

Returns `true` if the value is a `Set` and the `.size` is more than 0.

##### .emptyMap(value)

Returns `true` if the value is a `Map` and the `.size` is 0.

##### .nonEmptyMap(value)

Returns `true` if the value is a `Map` and the `.size` is more than 0.

#### Miscellaneous

##### .directInstanceOf(value, class)

Returns `true` if `value` is a direct instance of `class`.

```js
is.directInstanceOf(new Error(), Error);
//=> true

class UnicornError extends Error {}

is.directInstanceOf(new UnicornError(), Error);
//=> false
```

##### .urlInstance(value)

Returns `true` if `value` is an instance of the [`URL` class](https://developer.mozilla.org/en-US/docs/Web/API/URL).

```js
const url = new URL('https://example.com');

is.urlInstance(url);
//=> true
```

##### .urlString(value)

Returns `true` if `value` is a URL string.

Note: this only does basic checking using the [`URL` class](https://developer.mozilla.org/en-US/docs/Web/API/URL) constructor.

```js
const url = 'https://example.com';

is.urlString(url);
//=> true

is.urlString(new URL(url));
//=> false
```

##### .truthy(value)

Returns `true` for all values that evaluate to true in a boolean context:

```js
is.truthy('🦄');
//=> true

is.truthy(undefined);
//=> false
```

##### .falsy(value)

Returns `true` if `value` is one of: `false`, `0`, `''`, `null`, `undefined`, `NaN`.

##### .nan(value)
##### .nullOrUndefined(value)
##### .primitive(value)

JavaScript primitives are as follows:

- `null`
- `undefined`
- `string`
- `number`
- `boolean`
- `symbol`
- `bigint`

##### .integer(value)

##### .safeInteger(value)

Returns `true` if `value` is a [safe integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger).

##### .plainObject(value)

An object is plain if it's created by either `{}`, `new Object()`, or `Object.create(null)`.

##### .iterable(value)
##### .asyncIterable(value)
##### .class(value)

Returns `true` if the value is a class constructor.

##### .typedArray(value)

##### .arrayLike(value)

A `value` is array-like if it is not a function and has a `value.length` that is a safe integer greater than or equal to 0.

```js
is.arrayLike(document.forms);
//=> true

function foo() {
	is.arrayLike(arguments);
	//=> true
}
foo();
```

##### .tupleLike(value, guards)

A `value` is tuple-like if it matches the provided `guards` array both in `.length` and in types.

```js
is.tupleLike([1], [is.number]);
//=> true
```

```js
function foo() {
	const tuple = [1, '2', true];
	if (is.tupleLike(tuple, [is.number, is.string, is.boolean])) {
		tuple // [number, string, boolean]
	}
}

foo();
```

##### .positiveNumber(value)

Check if `value` is a number and is more than 0.

##### .negativeNumber(value)

Check if `value` is a number and is less than 0.

##### .inRange(value, range)

Check if `value` (number) is in the given `range`. The range is an array of two values, lower bound and upper bound, in no specific order.

```js
is.inRange(3, [0, 5]);
is.inRange(3, [5, 0]);
is.inRange(0, [-2, 2]);
```

##### .inRange(value, upperBound)

Check if `value` (number) is in the range of `0` to `upperBound`.

```js
is.inRange(3, 10);
```

##### .htmlElement(value)

Returns `true` if `value` is an [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement).

##### .nodeStream(value)

Returns `true` if `value` is a Node.js [stream](https://nodejs.org/api/stream.html).

```js
import fs from 'node:fs';

is.nodeStream(fs.createReadStream('unicorn.png'));
//=> true
```

##### .observable(value)

Returns `true` if `value` is an `Observable`.

```js
import {Observable} from 'rxjs';

is.observable(new Observable());
//=> true
```

##### .infinite(value)

Check if `value` is `Infinity` or `-Infinity`.

##### .evenInteger(value)

Returns `true` if `value` is an even integer.

##### .oddInteger(value)

Returns `true` if `value` is an odd integer.

##### .propertyKey(value)

Returns `true` if `value` can be used as an object property key (either `string`, `number`, or `symbol`).

##### .formData(value)

Returns `true` if `value` is an instance of the [`FormData` class](https://developer.mozilla.org/en-US/docs/Web/API/FormData).

```js
const data = new FormData();

is.formData(data);
//=> true
```

##### .urlSearchParams(value)

Returns `true` if `value` is an instance of the [`URLSearchParams` class](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams).

```js
const searchParams = new URLSearchParams();

is.urlSearchParams(searchParams);
//=> true
```

##### .any(predicate | predicate[], ...values)

Using a single `predicate` argument, returns `true` if **any** of the input `values` returns true in the `predicate`:

```js
is.any(is.string, {}, true, '🦄');
//=> true

is.any(is.boolean, 'unicorns', [], new Map());
//=> false
```

Using an array of `predicate[]`, returns `true` if **any** of the input `values` returns true for **any** of the `predicates` provided in an array:

```js
is.any([is.string, is.number], {}, true, '🦄');
//=> true

is.any([is.boolean, is.number], 'unicorns', [], new Map());
//=> false
```

##### .any(predicate[])

Using an array of `predicate[]` without values, returns a combined type guard that checks if a value matches **any** of the predicates:

```js
const isStringOrNumber = is.any([is.string, is.number]);

isStringOrNumber('hello');
//=> true

isStringOrNumber(123);
//=> true

isStringOrNumber(true);
//=> false
```

This is useful for composing with other methods like `is.optional`:

```js
is.optional(value, is.any([is.string, is.number]));
```

An empty predicate array currently returns a predicate that always returns `false`. This will throw in the next major release.

##### .all(predicate, ...values)

Returns `true` if **all** of the input `values` returns true in the `predicate`:

```js
is.all(is.object, {}, new Map(), new Set());
//=> true

is.all(is.string, '🦄', [], 'unicorns');
//=> false
```

##### .all(predicate[])

Using an array of `predicate[]` without values, returns a combined type guard that checks if a value matches **all** of the predicates:

```js
const isArrayAndNonEmpty = is.all([is.array, is.nonEmptyArray]);

isArrayAndNonEmpty(['hello']);
//=> true

isArrayAndNonEmpty([]);
//=> false
```

This is useful for composing with other methods like `is.optional`:

```js
is.optional(value, is.all([is.object, is.plainObject]));
```

An empty predicate array currently returns a predicate that always returns `true`. This will throw in the next major release.

##### .optional(value, predicate)

Returns `true` if `value` is `undefined` or satisfies the given `predicate`.

```js
is.optional(undefined, is.string);
//=> true

is.optional('🦄', is.string);
//=> true

is.optional(123, is.string);
//=> false
```

##### .validDate(value)

Returns `true` if the value is a valid date.

All [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date) objects have an internal timestamp value which is the number of milliseconds since the [Unix epoch](https://developer.mozilla.org/en-US/docs/Glossary/Unix_time). When a new `Date` is constructed with bad inputs, no error is thrown. Instead, a new `Date` object is returned. But the internal timestamp value is set to `NaN`, which is an `'Invalid Date'`. Bad inputs can be an non-parsable date string, a non-numeric value or a number that is outside of the expected range for a date value.

```js
const valid = new Date('2000-01-01');

is.date(valid);
//=> true
valid.getTime();
//=> 946684800000
valid.toUTCString();
//=> 'Sat, 01 Jan 2000 00:00:00 GMT'
is.validDate(valid);
//=> true

const invalid = new Date('Not a parsable date string');

is.date(invalid);
//=> true
invalid.getTime();
//=> NaN
invalid.toUTCString();
//=> 'Invalid Date'
is.validDate(invalid);
//=> false
```

##### .validLength(value)

Returns `true` if the value is a safe integer that is greater than or equal to zero.

This can be useful to confirm that a value is a valid count of something, ie. 0 or more.

##### .whitespaceString(value)

Returns `true` if the value is a string with only whitespace characters.

## Type guards

When using `is` together with TypeScript, [type guards](http://www.typescriptlang.org/docs/handbook/advanced-types.html#type-guards-and-differentiating-types) are being used extensively to infer the correct type inside if-else statements.

```ts
import is from '@sindresorhus/is';

const padLeft = (value: string, padding: string | number) => {
	if (is.number(padding)) {
		// `padding` is typed as `number`
		return Array(padding + 1).join(' ') + value;
	}

	if (is.string(padding)) {
		// `padding` is typed as `string`
		return padding + value;
	}

	throw new TypeError(`Expected 'padding' to be of type 'string' or 'number', got '${is(padding)}'.`);
}

padLeft('🦄', 3);
//=> '   🦄'

padLeft('🦄', '🌈');
//=> '🌈🦄'
```

## Type assertions

The type guards are also available as [type assertions](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#assertion-functions), which throw an error for unexpected types. It is a convenient one-line version of the often repetitive "if-not-expected-type-throw" pattern.

```ts
import {assert} from '@sindresorhus/is';

const handleMovieRatingApiResponse = (response: unknown) => {
	assert.plainObject(response);
	// `response` is now typed as a plain `object` with `unknown` properties.

	assert.number(response.rating);
	// `response.rating` is now typed as a `number`.

	assert.string(response.title);
	// `response.title` is now typed as a `string`.

	return `${response.title} (${response.rating * 10})`;
};

handleMovieRatingApiResponse({rating: 0.87, title: 'The Matrix'});
//=> 'The Matrix (8.7)'

// This throws an error.
handleMovieRatingApiResponse({rating: '🦄'});
```

### Optional assertion

Asserts that `value` is `undefined` or satisfies the provided `assertion`.

```ts
import {assert} from '@sindresorhus/is';

assert.optional(undefined, assert.string);
// Passes without throwing

assert.optional('🦄', assert.string);
// Passes without throwing

assert.optional(123, assert.string);
// Throws: Expected value which is `string`, received value of type `number`
```

## Generic type parameters

The type guards and type assertions are aware of [generic type parameters](https://www.typescriptlang.org/docs/handbook/generics.html), such as `Promise<T>` and `Map<Key, Value>`. The default is `unknown` for most cases, since `is` cannot check them at runtime. If the generic type is known at compile-time, either implicitly (inferred) or explicitly (provided), `is` propagates the type so it can be used later.

Use generic type parameters with caution. They are only checked by the TypeScript compiler, and not checked by `is` at runtime. This can lead to unexpected behavior, where the generic type is _assumed_ at compile-time, but actually is something completely different at runtime. It is best to use `unknown` (default) and type-check the value of the generic type parameter at runtime with `is` or `assert`.

```ts
import {assert} from '@sindresorhus/is';

async function badNumberAssumption(input: unknown) {
	// Bad assumption about the generic type parameter fools the compile-time type system.
	assert.promise<number>(input);
	// `input` is a `Promise` but only assumed to be `Promise<number>`.

	const resolved = await input;
	// `resolved` is typed as `number` but was not actually checked at runtime.

	// Multiplication will return NaN if the input promise did not actually contain a number.
	return 2 * resolved;
}

async function goodNumberAssertion(input: unknown) {
	assert.promise(input);
	// `input` is typed as `Promise<unknown>`

	const resolved = await input;
	// `resolved` is typed as `unknown`

	assert.number(resolved);
	// `resolved` is typed as `number`

	// Uses runtime checks so only numbers will reach the multiplication.
	return 2 * resolved;
}

badNumberAssumption(Promise.resolve('An unexpected string'));
//=> NaN

// This correctly throws an error because of the unexpected string value.
goodNumberAssertion(Promise.resolve('An unexpected string'));
```

## FAQ

### Why yet another type checking module?

There are hundreds of type checking modules on npm, unfortunately, I couldn't find any that fit my needs:

- Includes both type methods and ability to get the type
- Types of primitives returned as lowercase and object types as camelcase
- Covers all built-ins
- Unsurprising behavior
- Well-maintained
- Comprehensive test suite

For the ones I found, pick 3 of these.

The most common mistakes I noticed in these modules was using `instanceof` for type checking, forgetting that functions are objects, and omitting `symbol` as a primitive.

### Why not just use `instanceof` instead of this package?

`instanceof` does not work correctly for all types and it does not work across [realms](https://stackoverflow.com/a/49832343/64949). Examples of realms are iframes, windows, web workers, and the `vm` module in Node.js.

## Related

- [environment](https://github.com/sindresorhus/environment) - Check which JavaScript environment your code is running in at runtime
- [is-stream](https://github.com/sindresorhus/is-stream) - Check if something is a Node.js stream
- [is-observable](https://github.com/sindresorhus/is-observable) - Check if a value is an Observable
- [file-type](https://github.com/sindresorhus/file-type) - Detect the file type of a Buffer/Uint8Array
- [is-ip](https://github.com/sindresorhus/is-ip) - Check if a string is an IP address
- [is-array-sorted](https://github.com/sindresorhus/is-array-sorted) - Check if an Array is sorted
- [is-error-constructor](https://github.com/sindresorhus/is-error-constructor) - Check if a value is an error constructor
- [is-empty-iterable](https://github.com/sindresorhus/is-empty-iterable) - Check if an Iterable is empty
- [is-blob](https://github.com/sindresorhus/is-blob) - Check if a value is a Blob - File-like object of immutable, raw data
- [has-emoji](https://github.com/sindresorhus/has-emoji) - Check whether a string has any emoji

## Maintainers

- [Sindre Sorhus](https://github.com/sindresorhus)
- [Giora Guttsait](https://github.com/gioragutt)
- [Brandon Smith](https://github.com/brandon93s)
```

## File: `tsconfig.json`
```json
{
	"extends": "@sindresorhus/tsconfig",
	"include": [
		"source"
	],
}
```

## File: `source/index.ts`
```typescript
import type {
	ArrayLike,
	Class,
	Falsy,
	NodeStream,
	NonEmptyString,
	ObservableLike,
	Predicate,
	Primitive,
	TypedArray,
	UrlString,
	WeakRef,
	Whitespace,
} from './types.js';
import {keysOf} from './utilities.js';

// From type-fest.
type ExtractFromGlobalConstructors<Name extends string> =
	Name extends string
		? typeof globalThis extends Record<Name, new (...arguments_: any[]) => infer T> ? T : never
		: never;

type NodeBuffer = ExtractFromGlobalConstructors<'Buffer'>;

const typedArrayTypeNames = [
	'Int8Array',
	'Uint8Array',
	'Uint8ClampedArray',
	'Int16Array',
	'Uint16Array',
	'Int32Array',
	'Uint32Array',
	'Float32Array',
	'Float64Array',
	'BigInt64Array',
	'BigUint64Array',
] as const;

type TypedArrayTypeName = typeof typedArrayTypeNames[number];

function isTypedArrayName(name: unknown): name is TypedArrayTypeName {
	return typedArrayTypeNames.includes(name as TypedArrayTypeName);
}

const objectTypeNames = [
	'Function',
	'Generator',
	'AsyncGenerator',
	'GeneratorFunction',
	'AsyncGeneratorFunction',
	'AsyncFunction',
	'Observable',
	'Array',
	'Buffer',
	'Blob',
	'Object',
	'RegExp',
	'Date',
	'Error',
	'Map',
	'Set',
	'WeakMap',
	'WeakSet',
	'WeakRef',
	'ArrayBuffer',
	'SharedArrayBuffer',
	'DataView',
	'Promise',
	'URL',
	'FormData',
	'URLSearchParams',
	'HTMLElement',
	'NaN',
	...typedArrayTypeNames,
] as const;

type ObjectTypeName = typeof objectTypeNames[number];

function isObjectTypeName(name: unknown): name is ObjectTypeName {
	return objectTypeNames.includes(name as ObjectTypeName);
}

const primitiveTypeNames = [
	'null',
	'undefined',
	'string',
	'number',
	'bigint',
	'boolean',
	'symbol',
] as const;

type PrimitiveTypeName = typeof primitiveTypeNames[number];

function isPrimitiveTypeName(name: unknown): name is PrimitiveTypeName {
	return primitiveTypeNames.includes(name as PrimitiveTypeName);
}

export type TypeName = ObjectTypeName | PrimitiveTypeName;

const assertionTypeDescriptions = [
	'positive number',
	'negative number',
	'Class',
	'string with a number',
	'null or undefined',
	'Iterable',
	'AsyncIterable',
	'native Promise',
	'EnumCase',
	'string with a URL',
	'truthy',
	'falsy',
	'primitive',
	'integer',
	'plain object',
	'TypedArray',
	'array-like',
	'tuple-like',
	'Node.js Stream',
	'infinite number',
	'empty array',
	'non-empty array',
	'empty string',
	'empty string or whitespace',
	'non-empty string',
	'non-empty string and not whitespace',
	'empty object',
	'non-empty object',
	'empty set',
	'non-empty set',
	'empty map',
	'non-empty map',
	'PropertyKey',
	'even integer',
	'odd integer',
	'T',
	'in range',
	'predicate returns truthy for any value',
	'predicate returns truthy for all values',
	'valid Date',
	'valid length',
	'whitespace string',
	...objectTypeNames,
	...primitiveTypeNames,
] as const;

export type AssertionTypeDescription = typeof assertionTypeDescriptions[number];

const getObjectType = (value: unknown): ObjectTypeName | undefined => {
	const objectTypeName = Object.prototype.toString.call(value).slice(8, -1);

	if (/HTML\w+Element/.test(objectTypeName) && isHtmlElement(value)) {
		return 'HTMLElement';
	}

	if (isObjectTypeName(objectTypeName)) {
		return objectTypeName;
	}

	return undefined;
};

function detect(value: unknown): TypeName {
	if (value === null) {
		return 'null';
	}

	switch (typeof value) {
		case 'undefined': {
			return 'undefined';
		}

		case 'string': {
			return 'string';
		}

		case 'number': {
			return Number.isNaN(value) ? 'NaN' : 'number';
		}

		case 'boolean': {
			return 'boolean';
		}

		case 'function': {
			return 'Function';
		}

		case 'bigint': {
			return 'bigint';
		}

		case 'symbol': {
			return 'symbol';
		}

		default:
	}

	if (isObservable(value)) {
		return 'Observable';
	}

	if (isArray(value)) {
		return 'Array';
	}

	if (isBuffer(value)) {
		return 'Buffer';
	}

	const tagType = getObjectType(value);
	if (tagType && tagType !== 'Object') {
		return tagType;
	}

	if (hasPromiseApi(value)) {
		return 'Promise';
	}

	if (value instanceof String || value instanceof Boolean || value instanceof Number) {
		throw new TypeError('Please don\'t use object wrappers for primitive types');
	}

	return 'Object';
}

function hasPromiseApi<T = unknown>(value: unknown): value is Promise<T> {
	return isFunction((value as Promise<T>)?.then) && isFunction((value as Promise<T>)?.catch);
}

const is = Object.assign(
	detect,
	{
		all: isAll,
		any: isAny,
		array: isArray,
		arrayBuffer: isArrayBuffer,
		arrayLike: isArrayLike,
		asyncFunction: isAsyncFunction,
		asyncGenerator: isAsyncGenerator,
		asyncGeneratorFunction: isAsyncGeneratorFunction,
		asyncIterable: isAsyncIterable,
		bigint: isBigint,
		bigInt64Array: isBigInt64Array,
		bigUint64Array: isBigUint64Array,
		blob: isBlob,
		boolean: isBoolean,
		boundFunction: isBoundFunction,
		buffer: isBuffer,
		class: isClass,
		dataView: isDataView,
		date: isDate,
		detect,
		directInstanceOf: isDirectInstanceOf,
		emptyArray: isEmptyArray,
		emptyMap: isEmptyMap,
		emptyObject: isEmptyObject,
		emptySet: isEmptySet,
		emptyString: isEmptyString,
		emptyStringOrWhitespace: isEmptyStringOrWhitespace,
		enumCase: isEnumCase,
		error: isError,
		evenInteger: isEvenInteger,
		falsy: isFalsy,
		float32Array: isFloat32Array,
		float64Array: isFloat64Array,
		formData: isFormData,
		function: isFunction,
		generator: isGenerator,
		generatorFunction: isGeneratorFunction,
		htmlElement: isHtmlElement,
		infinite: isInfinite,
		inRange: isInRange,
		int16Array: isInt16Array,
		int32Array: isInt32Array,
		int8Array: isInt8Array,
		integer: isInteger,
		iterable: isIterable,
		map: isMap,
		nan: isNan,
		nativePromise: isNativePromise,
		negativeNumber: isNegativeNumber,
		nodeStream: isNodeStream,
		nonEmptyArray: isNonEmptyArray,
		nonEmptyMap: isNonEmptyMap,
		nonEmptyObject: isNonEmptyObject,
		nonEmptySet: isNonEmptySet,
		nonEmptyString: isNonEmptyString,
		nonEmptyStringAndNotWhitespace: isNonEmptyStringAndNotWhitespace,
		null: isNull,
		nullOrUndefined: isNullOrUndefined,
		number: isNumber,
		numericString: isNumericString,
		object: isObject,
		observable: isObservable,
		oddInteger: isOddInteger,
		plainObject: isPlainObject,
		positiveNumber: isPositiveNumber,
		primitive: isPrimitive,
		promise: isPromise,
		propertyKey: isPropertyKey,
		regExp: isRegExp,
		safeInteger: isSafeInteger,
		set: isSet,
		sharedArrayBuffer: isSharedArrayBuffer,
		string: isString,
		symbol: isSymbol,
		truthy: isTruthy,
		tupleLike: isTupleLike,
		typedArray: isTypedArray,
		uint16Array: isUint16Array,
		uint32Array: isUint32Array,
		uint8Array: isUint8Array,
		uint8ClampedArray: isUint8ClampedArray,
		undefined: isUndefined,
		urlInstance: isUrlInstance,
		urlSearchParams: isUrlSearchParams,
		urlString: isUrlString,
		optional: isOptional,
		validDate: isValidDate,
		validLength: isValidLength,
		weakMap: isWeakMap,
		weakRef: isWeakRef,
		weakSet: isWeakSet,
		whitespaceString: isWhitespaceString,
	},
);

function isAbsoluteModule2(remainder: 0 | 1) {
	return (value: unknown): value is number => isInteger(value) && Math.abs(value % 2) === remainder;
}

type TypeGuard<T> = (value: unknown) => value is T;

function validatePredicateArray(predicateArray: readonly Predicate[], allowEmpty: boolean) {
	if (predicateArray.length === 0) {
		if (allowEmpty) {
			// Next major release: throw for empty predicate arrays to avoid vacuous results.
			// throw new TypeError('Invalid predicate array');
		} else {
			throw new TypeError('Invalid predicate array');
		}

		return;
	}

	for (const predicate of predicateArray) {
		if (!isFunction(predicate)) {
			throw new TypeError(`Invalid predicate: ${JSON.stringify(predicate)}`);
		}
	}
}

// Predicate factory overloads - return a type guard when called with only predicates
export function isAll<T1>(predicates: [TypeGuard<T1>]): TypeGuard<T1>;
export function isAll<T1, T2>(predicates: [TypeGuard<T1>, TypeGuard<T2>]): TypeGuard<T1 & T2>;
export function isAll<T1, T2, T3>(predicates: [TypeGuard<T1>, TypeGuard<T2>, TypeGuard<T3>]): TypeGuard<T1 & T2 & T3>;
export function isAll<T1, T2, T3, T4>(predicates: [TypeGuard<T1>, TypeGuard<T2>, TypeGuard<T3>, TypeGuard<T4>]): TypeGuard<T1 & T2 & T3 & T4>;
export function isAll<T1, T2, T3, T4, T5>(predicates: [TypeGuard<T1>, TypeGuard<T2>, TypeGuard<T3>, TypeGuard<T4>, TypeGuard<T5>]): TypeGuard<T1 & T2 & T3 & T4 & T5>;
export function isAll(predicates: ReadonlyArray<TypeGuard<unknown>>): TypeGuard<unknown>;
export function isAll(predicates: readonly Predicate[]): Predicate;
// Evaluator overload - check if all values match the predicate
export function isAll(predicate: Predicate | readonly Predicate[], ...values: unknown[]): boolean;
export function isAll(predicate: Predicate | readonly Predicate[], ...values: unknown[]): boolean | Predicate {
	if (Array.isArray(predicate)) {
		const predicateArray = predicate as readonly Predicate[];
		validatePredicateArray(predicateArray, values.length === 0);

		const combinedPredicate = (value: unknown) => predicateArray.every(singlePredicate => singlePredicate(value));
		if (values.length === 0) {
			return combinedPredicate;
		}

		return predicateOnArray(Array.prototype.every, combinedPredicate, values);
	}

	return predicateOnArray(Array.prototype.every, predicate as Predicate, values);
}

// Predicate factory overloads - return a type guard when called with only predicates
export function isAny<T1>(predicates: [TypeGuard<T1>]): TypeGuard<T1>;
export function isAny<T1, T2>(predicates: [TypeGuard<T1>, TypeGuard<T2>]): TypeGuard<T1 | T2>;
export function isAny<T1, T2, T3>(predicates: [TypeGuard<T1>, TypeGuard<T2>, TypeGuard<T3>]): TypeGuard<T1 | T2 | T3>;
export function isAny<T1, T2, T3, T4>(predicates: [TypeGuard<T1>, TypeGuard<T2>, TypeGuard<T3>, TypeGuard<T4>]): TypeGuard<T1 | T2 | T3 | T4>;
export function isAny<T1, T2, T3, T4, T5>(predicates: [TypeGuard<T1>, TypeGuard<T2>, TypeGuard<T3>, TypeGuard<T4>, TypeGuard<T5>]): TypeGuard<T1 | T2 | T3 | T4 | T5>;
export function isAny(predicates: ReadonlyArray<TypeGuard<unknown>>): TypeGuard<unknown>;
export function isAny(predicates: readonly Predicate[]): Predicate;
// Evaluator overload - check if any value matches any predicate
export function isAny(predicate: Predicate | readonly Predicate[], ...values: unknown[]): boolean;
export function isAny(predicate: Predicate | readonly Predicate[], ...values: unknown[]): boolean | Predicate {
	if (Array.isArray(predicate)) {
		const predicateArray = predicate as readonly Predicate[];
		validatePredicateArray(predicateArray, values.length === 0);

		const combinedPredicate = (value: unknown) => predicateArray.some(singlePredicate => singlePredicate(value));
		if (values.length === 0) {
			return combinedPredicate;
		}

		return predicateOnArray(Array.prototype.some, combinedPredicate, values);
	}

	return predicateOnArray(Array.prototype.some, predicate as Predicate, values);
}

export function isOptional<T>(value: unknown, predicate: (value: unknown) => value is T): value is T | undefined {
	return isUndefined(value) || predicate(value);
}

export function isArray<T = unknown>(value: unknown, assertion?: (value: T) => value is T): value is T[] {
	if (!Array.isArray(value)) {
		return false;
	}

	if (!isFunction(assertion)) {
		return true;
	}

	// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
	return value.every(element => assertion(element));
}

export function isArrayBuffer(value: unknown): value is ArrayBuffer {
	return getObjectType(value) === 'ArrayBuffer';
}

export function isArrayLike<T = unknown>(value: unknown): value is ArrayLike<T> {
	return !isNullOrUndefined(value) && !isFunction(value) && isValidLength((value as ArrayLike<T>).length);
}

export function isAsyncFunction<T = unknown>(value: unknown): value is ((...arguments_: any[]) => Promise<T>) {
	return getObjectType(value) === 'AsyncFunction';
}

export function isAsyncGenerator(value: unknown): value is AsyncGenerator {
	return isAsyncIterable(value) && isFunction((value as AsyncGenerator).next) && isFunction((value as AsyncGenerator).throw);
}

export function isAsyncGeneratorFunction(value: unknown): value is ((...arguments_: any[]) => Promise<unknown>) {
	return getObjectType(value) === 'AsyncGeneratorFunction';
}

export function isAsyncIterable<T = unknown>(value: unknown): value is AsyncIterable<T> {
	return isFunction((value as AsyncIterable<T>)?.[Symbol.asyncIterator]);
}

export function isBigint(value: unknown): value is bigint {
	return typeof value === 'bigint';
}

export function isBigInt64Array(value: unknown): value is BigInt64Array {
	return getObjectType(value) === 'BigInt64Array';
}

export function isBigUint64Array(value: unknown): value is BigUint64Array {
	return getObjectType(value) === 'BigUint64Array';
}

export function isBlob(value: unknown): value is Blob {
	return getObjectType(value) === 'Blob';
}

export function isBoolean(value: unknown): value is boolean {
	return value === true || value === false;
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isBoundFunction(value: unknown): value is Function {
	return isFunction(value) && !Object.hasOwn(value, 'prototype');
}

/**
Note: [Prefer using `Uint8Array` instead of `Buffer`.](https://sindresorhus.com/blog/goodbye-nodejs-buffer)
*/
export function isBuffer(value: unknown): value is NodeBuffer {
	// eslint-disable-next-line @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-call
	return (value as any)?.constructor?.isBuffer?.(value) ?? false;
}

export function isClass<T = unknown>(value: unknown): value is Class<T> {
	return isFunction(value) && /^class(\s+|{)/.test(value.toString());
}

export function isDataView(value: unknown): value is DataView {
	return getObjectType(value) === 'DataView';
}

export function isDate(value: unknown): value is Date {
	return getObjectType(value) === 'Date';
}

export function isDirectInstanceOf<T>(instance: unknown, class_: Class<T>): instance is T {
	if (instance === undefined || instance === null) {
		return false;
	}

	return Object.getPrototypeOf(instance) === class_.prototype;
}

export function isEmptyArray(value: unknown): value is never[] {
	return isArray(value) && value.length === 0;
}

export function isEmptyMap(value: unknown): value is Map<never, never> {
	return isMap(value) && value.size === 0;
}

export function isEmptyObject<Key extends keyof any = string>(value: unknown): value is Record<Key, never> {
	return isObject(value) && !isMap(value) && !isSet(value) && Object.keys(value).length === 0;
}

export function isEmptySet(value: unknown): value is Set<never> {
	return isSet(value) && value.size === 0;
}

export function isEmptyString(value: unknown): value is '' {
	return isString(value) && value.length === 0;
}

export function isEmptyStringOrWhitespace(value: unknown): value is '' | Whitespace {
	return isEmptyString(value) || isWhitespaceString(value);
}

export function isEnumCase<T = unknown>(value: unknown, targetEnum: T): value is T[keyof T] {
	// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
	return Object.values(targetEnum as any).includes(value as string);
}

export function isError(value: unknown): value is Error {
	// TODO: Use `Error.isError` when targeting Node.js 24.`
	return getObjectType(value) === 'Error';
}

export function isEvenInteger(value: unknown): value is number {
	return isAbsoluteModule2(0)(value);
}

// Example: `is.falsy = (value: unknown): value is (not true | 0 | '' | undefined | null) => Boolean(value);`
export function isFalsy(value: unknown): value is Falsy {
	return !value;
}

// TODO: Support detecting Float16Array when targeting Node.js 24.

export function isFloat32Array(value: unknown): value is Float32Array {
	return getObjectType(value) === 'Float32Array';
}

export function isFloat64Array(value: unknown): value is Float64Array {
	return getObjectType(value) === 'Float64Array';
}

export function isFormData(value: unknown): value is FormData {
	return getObjectType(value) === 'FormData';
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isFunction(value: unknown): value is Function {
	return typeof value === 'function';
}

export function isGenerator(value: unknown): value is Generator {
	return isIterable(value) && isFunction((value as Generator)?.next) && isFunction((value as Generator)?.throw);
}

export function isGeneratorFunction(value: unknown): value is GeneratorFunction {
	return getObjectType(value) === 'GeneratorFunction';
}

// eslint-disable-next-line @typescript-eslint/naming-convention
const NODE_TYPE_ELEMENT = 1;

// eslint-disable-next-line @typescript-eslint/naming-convention
const DOM_PROPERTIES_TO_CHECK: Array<(keyof HTMLElement)> = [
	'innerHTML',
	'ownerDocument',
	'style',
	'attributes',
	'nodeValue',
];

export function isHtmlElement(value: unknown): value is HTMLElement {
	return isObject(value)
		&& (value as HTMLElement).nodeType === NODE_TYPE_ELEMENT
		&& isString((value as HTMLElement).nodeName)
		&& !isPlainObject(value)
		&& DOM_PROPERTIES_TO_CHECK.every(property => property in value);
}

export function isInfinite(value: unknown): value is number {
	return value === Number.POSITIVE_INFINITY || value === Number.NEGATIVE_INFINITY;
}

export function isInRange(value: number, range: number | [number, number]): value is number {
	if (isNumber(range)) {
		return value >= Math.min(0, range) && value <= Math.max(range, 0);
	}

	if (isArray(range) && range.length === 2) {
		return value >= Math.min(...range) && value <= Math.max(...range);
	}

	throw new TypeError(`Invalid range: ${JSON.stringify(range)}`);
}

export function isInt16Array(value: unknown): value is Int16Array {
	return getObjectType(value) === 'Int16Array';
}

export function isInt32Array(value: unknown): value is Int32Array {
	return getObjectType(value) === 'Int32Array';
}

export function isInt8Array(value: unknown): value is Int8Array {
	return getObjectType(value) === 'Int8Array';
}

export function isInteger(value: unknown): value is number {
	return Number.isInteger(value);
}

export function isIterable<T = unknown>(value: unknown): value is Iterable<T> {
	return isFunction((value as Iterable<T>)?.[Symbol.iterator]);
}

export function isMap<Key = unknown, Value = unknown>(value: unknown): value is Map<Key, Value> {
	return getObjectType(value) === 'Map';
}

export function isNan(value: unknown) {
	return Number.isNaN(value);
}

export function isNativePromise<T = unknown>(value: unknown): value is Promise<T> {
	return getObjectType(value) === 'Promise';
}

export function isNegativeNumber(value: unknown): value is number {
	return isNumber(value) && value < 0;
}

export function isNodeStream(value: unknown): value is NodeStream {
	return isObject(value) && isFunction((value as NodeStream).pipe) && !isObservable(value);
}

export function isNonEmptyArray<T = unknown, Item = unknown>(value: T | Item[]): value is [Item, ...Item[]] {
	return isArray(value) && value.length > 0;
}

export function isNonEmptyMap<Key = unknown, Value = unknown>(value: unknown): value is Map<Key, Value> {
	return isMap(value) && value.size > 0;
}

// TODO: Use `not` operator here to remove `Map` and `Set` from type guard:
// - https://github.com/Microsoft/TypeScript/pull/29317
export function isNonEmptyObject<Key extends keyof any = string, Value = unknown>(value: unknown): value is Record<Key, Value> {
	return isObject(value) && !isMap(value) && !isSet(value) && Object.keys(value).length > 0;
}

export function isNonEmptySet<T = unknown>(value: unknown): value is Set<T> {
	return isSet(value) && value.size > 0;
}

// TODO: Use `not ''` when the `not` operator is available.
export function isNonEmptyString(value: unknown): value is NonEmptyString {
	return isString(value) && value.length > 0;
}

// TODO: Use `not ''` when the `not` operator is available.
export function isNonEmptyStringAndNotWhitespace(value: unknown): value is NonEmptyString {
	return isString(value) && !isEmptyStringOrWhitespace(value);
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isNull(value: unknown): value is null {
	return value === null;
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isNullOrUndefined(value: unknown): value is null | undefined {
	return isNull(value) || isUndefined(value);
}

export function isNumber(value: unknown): value is number {
	return typeof value === 'number' && !Number.isNaN(value);
}

export function isNumericString(value: unknown): value is `${number}` {
	return isString(value) && !isEmptyStringOrWhitespace(value) && !Number.isNaN(Number(value));
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isObject(value: unknown): value is object {
	return !isNull(value) && (typeof value === 'object' || isFunction(value));
}

export function isObservable(value: unknown): value is ObservableLike {
	if (!value) {
		return false;
	}

	// eslint-disable-next-line no-use-extend-native/no-use-extend-native, @typescript-eslint/no-unsafe-call
	if (Symbol.observable !== undefined && value === (value as any)[Symbol.observable]?.()) {
		return true;
	}

	// eslint-disable-next-line @typescript-eslint/no-unsafe-call
	if (value === (value as any)['@@observable']?.()) {
		return true;
	}

	return false;
}

export function isOddInteger(value: unknown): value is number {
	return isAbsoluteModule2(1)(value);
}

export function isPlainObject<Value = unknown>(value: unknown): value is Record<PropertyKey, Value> {
	// From: https://github.com/sindresorhus/is-plain-obj/blob/main/index.js
	if (typeof value !== 'object' || value === null) {
		return false;
	}

	// eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
	const prototype = Object.getPrototypeOf(value);

	return (prototype === null || prototype === Object.prototype || Object.getPrototypeOf(prototype) === null) && !(Symbol.toStringTag in value) && !(Symbol.iterator in value);
}

export function isPositiveNumber(value: unknown): value is number {
	return isNumber(value) && value > 0;
}

export function isPrimitive(value: unknown): value is Primitive {
	return isNull(value) || isPrimitiveTypeName(typeof value);
}

export function isPromise<T = unknown>(value: unknown): value is Promise<T> {
	return isNativePromise(value) || hasPromiseApi(value);
}

// `PropertyKey` is any value that can be used as an object key (string, number, or symbol)
export function isPropertyKey(value: unknown): value is PropertyKey {
	return isAny([isString, isNumber, isSymbol], value);
}

export function isRegExp(value: unknown): value is RegExp {
	return getObjectType(value) === 'RegExp';
}

export function isSafeInteger(value: unknown): value is number {
	return Number.isSafeInteger(value);
}

export function isSet<T = unknown>(value: unknown): value is Set<T> {
	return getObjectType(value) === 'Set';
}

export function isSharedArrayBuffer(value: unknown): value is SharedArrayBuffer {
	return getObjectType(value) === 'SharedArrayBuffer';
}

export function isString(value: unknown): value is string {
	return typeof value === 'string';
}

export function isSymbol(value: unknown): value is symbol {
	return typeof value === 'symbol';
}

// Example: `is.truthy = (value: unknown): value is (not false | not 0 | not '' | not undefined | not null) => Boolean(value);`
// eslint-disable-next-line unicorn/prefer-native-coercion-functions
export function isTruthy<T>(value: T | Falsy): value is T {
	return Boolean(value);
}

// eslint-disable-next-line @typescript-eslint/ban-types
type ResolveTypesOfTypeGuardsTuple<TypeGuardsOfT, ResultOfT extends unknown[] = [] > =
	TypeGuardsOfT extends [TypeGuard<infer U>, ...infer TOthers]
		? ResolveTypesOfTypeGuardsTuple<TOthers, [...ResultOfT, U]>
		: TypeGuardsOfT extends undefined[]
			? ResultOfT
			: never;

export function isTupleLike<T extends Array<TypeGuard<unknown>>>(value: unknown, guards: [...T]): value is ResolveTypesOfTypeGuardsTuple<T> {
	if (isArray(guards) && isArray(value) && guards.length === value.length) {
		return guards.every((guard, index) => guard(value[index]));
	}

	return false;
}

export function isTypedArray(value: unknown): value is TypedArray {
	return isTypedArrayName(getObjectType(value));
}

export function isUint16Array(value: unknown): value is Uint16Array {
	return getObjectType(value) === 'Uint16Array';
}

export function isUint32Array(value: unknown): value is Uint32Array {
	return getObjectType(value) === 'Uint32Array';
}

export function isUint8Array(value: unknown): value is Uint8Array {
	return getObjectType(value) === 'Uint8Array';
}

export function isUint8ClampedArray(value: unknown): value is Uint8ClampedArray {
	return getObjectType(value) === 'Uint8ClampedArray';
}

export function isUndefined(value: unknown): value is undefined {
	return value === undefined;
}

export function isUrlInstance(value: unknown): value is URL {
	return getObjectType(value) === 'URL';
}

// eslint-disable-next-line unicorn/prevent-abbreviations
export function isUrlSearchParams(value: unknown): value is URLSearchParams {
	return getObjectType(value) === 'URLSearchParams';
}

export function isUrlString(value: unknown): value is UrlString {
	if (!isString(value)) {
		return false;
	}

	try {
		new URL(value); // eslint-disable-line no-new
		return true;
	} catch {
		return false;
	}
}

export function isValidDate(value: unknown): value is Date {
	return isDate(value) && !isNan(Number(value));
}

export function isValidLength(value: unknown): value is number {
	return isSafeInteger(value) && value >= 0;
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isWeakMap<Key extends object = object, Value = unknown>(value: unknown): value is WeakMap<Key, Value> {
	return getObjectType(value) === 'WeakMap';
}

// eslint-disable-next-line @typescript-eslint/ban-types, unicorn/prevent-abbreviations
export function isWeakRef(value: unknown): value is WeakRef<object> {
	return getObjectType(value) === 'WeakRef';
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function isWeakSet(value: unknown): value is WeakSet<object> {
	return getObjectType(value) === 'WeakSet';
}

export function isWhitespaceString(value: unknown): value is Whitespace {
	return isString(value) && /^\s+$/.test(value);
}

type ArrayMethod = (function_: (value: unknown, index: number, array: unknown[]) => boolean, thisArgument?: unknown) => boolean;

function predicateOnArray(method: ArrayMethod, predicate: Predicate, values: unknown[]) {
	if (!isFunction(predicate)) {
		throw new TypeError(`Invalid predicate: ${JSON.stringify(predicate)}`);
	}

	if (values.length === 0) {
		throw new TypeError('Invalid number of values');
	}

	return method.call(values, predicate);
}

function typeErrorMessage(description: AssertionTypeDescription, value: unknown): string {
	return `Expected value which is \`${description}\`, received value of type \`${is(value)}\`.`;
}

function unique<T>(values: T[]): T[] {
	// eslint-disable-next-line unicorn/prefer-spread
	return Array.from(new Set(values));
}

const andFormatter = new Intl.ListFormat('en', {style: 'long', type: 'conjunction'});
const orFormatter = new Intl.ListFormat('en', {style: 'long', type: 'disjunction'});

function typeErrorMessageMultipleValues(expectedType: AssertionTypeDescription | AssertionTypeDescription[], values: unknown[]): string {
	const uniqueExpectedTypes = unique((isArray(expectedType) ? expectedType : [expectedType]).map(value => `\`${value}\``));
	const uniqueValueTypes = unique(values.map(value => `\`${is(value)}\``));
	return `Expected values which are ${orFormatter.format(uniqueExpectedTypes)}. Received values of type${uniqueValueTypes.length > 1 ? 's' : ''} ${andFormatter.format(uniqueValueTypes)}.`;
}

// Type assertions have to be declared with an explicit type.
type Assert = {
	// Unknowns.
	undefined: (value: unknown, message?: string) => asserts value is undefined;
	string: (value: unknown, message?: string) => asserts value is string;
	number: (value: unknown, message?: string) => asserts value is number;
	positiveNumber: (value: unknown, message?: string) => asserts value is number;
	negativeNumber: (value: unknown, message?: string) => asserts value is number;
	bigint: (value: unknown, message?: string) => asserts value is bigint;
	// eslint-disable-next-line @typescript-eslint/ban-types
	function: (value: unknown, message?: string) => asserts value is Function;
	// eslint-disable-next-line @typescript-eslint/ban-types
	null: (value: unknown, message?: string) => asserts value is null;
	class: <T = unknown>(value: unknown, message?: string) => asserts value is Class<T>;
	boolean: (value: unknown, message?: string) => asserts value is boolean;
	symbol: (value: unknown, message?: string) => asserts value is symbol;
	numericString: (value: unknown, message?: string) => asserts value is `${number}`;
	array: <T = unknown>(value: unknown, assertion?: (element: unknown) => asserts element is T, message?: string) => asserts value is T[];
	buffer: (value: unknown, message?: string) => asserts value is NodeBuffer;
	blob: (value: unknown, message?: string) => asserts value is Blob;
	// eslint-disable-next-line @typescript-eslint/ban-types
	nullOrUndefined: (value: unknown, message?: string) => asserts value is null | undefined;
	object: <Key extends keyof any = string, Value = unknown>(value: unknown, message?: string) => asserts value is Record<Key, Value>;
	iterable: <T = unknown>(value: unknown, message?: string) => asserts value is Iterable<T>;
	asyncIterable: <T = unknown>(value: unknown, message?: string) => asserts value is AsyncIterable<T>;
	generator: (value: unknown, message?: string) => asserts value is Generator;
	asyncGenerator: (value: unknown, message?: string) => asserts value is AsyncGenerator;
	nativePromise: <T = unknown>(value: unknown, message?: string) => asserts value is Promise<T>;
	promise: <T = unknown>(value: unknown, message?: string) => asserts value is Promise<T>;
	generatorFunction: (value: unknown, message?: string) => asserts value is GeneratorFunction;
	asyncGeneratorFunction: (value: unknown, message?: string) => asserts value is AsyncGeneratorFunction;
	// eslint-disable-next-line @typescript-eslint/ban-types
	asyncFunction: (value: unknown, message?: string) => asserts value is Function;
	// eslint-disable-next-line @typescript-eslint/ban-types
	boundFunction: (value: unknown, message?: string) => asserts value is Function;
	regExp: (value: unknown, message?: string) => asserts value is RegExp;
	date: (value: unknown, message?: string) => asserts value is Date;
	error: (value: unknown, message?: string) => asserts value is Error;
	map: <Key = unknown, Value = unknown>(value: unknown, message?: string) => asserts value is Map<Key, Value>;
	set: <T = unknown>(value: unknown, message?: string) => asserts value is Set<T>;
	// eslint-disable-next-line @typescript-eslint/ban-types
	weakMap: <Key extends object = object, Value = unknown>(value: unknown, message?: string) => asserts value is WeakMap<Key, Value>;
	// eslint-disable-next-line @typescript-eslint/ban-types
	weakSet: <T extends object = object>(value: unknown, message?: string) => asserts value is WeakSet<T>;
	// eslint-disable-next-line @typescript-eslint/ban-types
	weakRef: <T extends object = object>(value: unknown, message?: string) => asserts value is WeakRef<T>;
	int8Array: (value: unknown, message?: string) => asserts value is Int8Array;
	uint8Array: (value: unknown, message?: string) => asserts value is Uint8Array;
	uint8ClampedArray: (value: unknown, message?: string) => asserts value is Uint8ClampedArray;
	int16Array: (value: unknown, message?: string) => asserts value is Int16Array;
	uint16Array: (value: unknown, message?: string) => asserts value is Uint16Array;
	int32Array: (value: unknown, message?: string) => asserts value is Int32Array;
	uint32Array: (value: unknown, message?: string) => asserts value is Uint32Array;
	float32Array: (value: unknown, message?: string) => asserts value is Float32Array;
	float64Array: (value: unknown, message?: string) => asserts value is Float64Array;
	bigInt64Array: (value: unknown, message?: string) => asserts value is BigInt64Array;
	bigUint64Array: (value: unknown, message?: string) => asserts value is BigUint64Array;
	arrayBuffer: (value: unknown, message?: string) => asserts value is ArrayBuffer;
	sharedArrayBuffer: (value: unknown, message?: string) => asserts value is SharedArrayBuffer;
	dataView: (value: unknown, message?: string) => asserts value is DataView;
	enumCase: <T = unknown>(value: unknown, targetEnum: T, message?: string) => asserts value is T[keyof T];
	urlInstance: (value: unknown, message?: string) => asserts value is URL;
	urlString: (value: unknown, message?: string) => asserts value is UrlString;
	truthy: <T>(value: T | Falsy, message?: string) => asserts value is T;
	falsy: (value: unknown, message?: string) => asserts value is Falsy;
	nan: (value: unknown, message?: string) => asserts value is number;
	primitive: (value: unknown, message?: string) => asserts value is Primitive;
	integer: (value: unknown, message?: string) => asserts value is number;
	safeInteger: (value: unknown, message?: string) => asserts value is number;
	plainObject: <Value = unknown>(value: unknown, message?: string) => asserts value is Record<PropertyKey, Value>;
	typedArray: (value: unknown, message?: string) => asserts value is TypedArray;
	arrayLike: <T = unknown>(value: unknown, message?: string) => asserts value is ArrayLike<T>;
	tupleLike: <T extends Array<TypeGuard<unknown>>>(value: unknown, guards: [...T], message?: string) => asserts value is ResolveTypesOfTypeGuardsTuple<T>;
	htmlElement: (value: unknown, message?: string) => asserts value is HTMLElement;
	observable: (value: unknown, message?: string) => asserts value is ObservableLike;
	nodeStream: (value: unknown, message?: string) => asserts value is NodeStream;
	infinite: (value: unknown, message?: string) => asserts value is number;
	emptyArray: (value: unknown, message?: string) => asserts value is never[];
	nonEmptyArray: <T = unknown, Item = unknown>(value: T | Item[], message?: string) => asserts value is [Item, ...Item[]];
	emptyString: (value: unknown, message?: string) => asserts value is '';
	emptyStringOrWhitespace: (value: unknown, message?: string) => asserts value is '' | Whitespace;
	nonEmptyString: (value: unknown, message?: string) => asserts value is string;
	nonEmptyStringAndNotWhitespace: (value: unknown, message?: string) => asserts value is string;
	emptyObject: <Key extends keyof any = string>(value: unknown, message?: string) => asserts value is Record<Key, never>;
	nonEmptyObject: <Key extends keyof any = string, Value = unknown>(value: unknown, message?: string) => asserts value is Record<Key, Value>;
	emptySet: (value: unknown, message?: string) => asserts value is Set<never>;
	nonEmptySet: <T = unknown>(value: unknown, message?: string) => asserts value is Set<T>;
	emptyMap: (value: unknown, message?: string) => asserts value is Map<never, never>;
	nonEmptyMap: <Key = unknown, Value = unknown>(value: unknown, message?: string) => asserts value is Map<Key, Value>;
	propertyKey: (value: unknown, message?: string) => asserts value is PropertyKey;
	formData: (value: unknown, message?: string) => asserts value is FormData;
	urlSearchParams: (value: unknown, message?: string) => asserts value is URLSearchParams;
	validDate: (value: unknown, message?: string) => asserts value is Date;
	validLength: (value: unknown, message?: string) => asserts value is number;
	whitespaceString: (value: unknown, message?: string) => asserts value is string;

	// Numbers.
	evenInteger: (value: number, message?: string) => asserts value is number;
	oddInteger: (value: number, message?: string) => asserts value is number;

	// Two arguments.
	directInstanceOf: <T>(instance: unknown, class_: Class<T>, message?: string) => asserts instance is T;
	inRange: (value: number, range: number | [number, number], message?: string) => asserts value is number;

	// Variadic functions.
	any: (predicate: Predicate | readonly Predicate[], ...values: unknown[]) => void | never;
	all: (predicate: Predicate | readonly Predicate[], ...values: unknown[]) => void | never;

	/**
	Asserts that `value` is `undefined` or satisfies the provided `assertion`.

	Useful for optional inputs.
	*/
	optional: <T>(value: unknown, assertion: (value: unknown, message?: string) => asserts value is T, message?: string) => asserts value is T | undefined;
};

export const assert: Assert = {
	all: assertAll,
	any: assertAny,
	optional: assertOptional,
	array: assertArray,
	arrayBuffer: assertArrayBuffer,
	arrayLike: assertArrayLike,
	asyncFunction: assertAsyncFunction,
	asyncGenerator: assertAsyncGenerator,
	asyncGeneratorFunction: assertAsyncGeneratorFunction,
	asyncIterable: assertAsyncIterable,
	bigint: assertBigint,
	bigInt64Array: assertBigInt64Array,
	bigUint64Array: assertBigUint64Array,
	blob: assertBlob,
	boolean: assertBoolean,
	boundFunction: assertBoundFunction,
	buffer: assertBuffer,
	class: assertClass,
	dataView: assertDataView,
	date: assertDate,
	directInstanceOf: assertDirectInstanceOf,
	emptyArray: assertEmptyArray,
	emptyMap: assertEmptyMap,
	emptyObject: assertEmptyObject,
	emptySet: assertEmptySet,
	emptyString: assertEmptyString,
	emptyStringOrWhitespace: assertEmptyStringOrWhitespace,
	enumCase: assertEnumCase,
	error: assertError,
	evenInteger: assertEvenInteger,
	falsy: assertFalsy,
	float32Array: assertFloat32Array,
	float64Array: assertFloat64Array,
	formData: assertFormData,
	function: assertFunction,
	generator: assertGenerator,
	generatorFunction: assertGeneratorFunction,
	htmlElement: assertHtmlElement,
	infinite: assertInfinite,
	inRange: assertInRange,
	int16Array: assertInt16Array,
	int32Array: assertInt32Array,
	int8Array: assertInt8Array,
	integer: assertInteger,
	iterable: assertIterable,
	map: assertMap,
	nan: assertNan,
	nativePromise: assertNativePromise,
	negativeNumber: assertNegativeNumber,
	nodeStream: assertNodeStream,
	nonEmptyArray: assertNonEmptyArray,
	nonEmptyMap: assertNonEmptyMap,
	nonEmptyObject: assertNonEmptyObject,
	nonEmptySet: assertNonEmptySet,
	nonEmptyString: assertNonEmptyString,
	nonEmptyStringAndNotWhitespace: assertNonEmptyStringAndNotWhitespace,
	null: assertNull,
	nullOrUndefined: assertNullOrUndefined,
	number: assertNumber,
	numericString: assertNumericString,
	object: assertObject,
	observable: assertObservable,
	oddInteger: assertOddInteger,
	plainObject: assertPlainObject,
	positiveNumber: assertPositiveNumber,
	primitive: assertPrimitive,
	promise: assertPromise,
	propertyKey: assertPropertyKey,
	regExp: assertRegExp,
	safeInteger: assertSafeInteger,
	set: assertSet,
	sharedArrayBuffer: assertSharedArrayBuffer,
	string: assertString,
	symbol: assertSymbol,
	truthy: assertTruthy,
	tupleLike: assertTupleLike,
	typedArray: assertTypedArray,
	uint16Array: assertUint16Array,
	uint32Array: assertUint32Array,
	uint8Array: assertUint8Array,
	uint8ClampedArray: assertUint8ClampedArray,
	undefined: assertUndefined,
	urlInstance: assertUrlInstance,
	urlSearchParams: assertUrlSearchParams,
	urlString: assertUrlString,
	validDate: assertValidDate,
	validLength: assertValidLength,
	weakMap: assertWeakMap,
	weakRef: assertWeakRef,
	weakSet: assertWeakSet,
	whitespaceString: assertWhitespaceString,
};

const methodTypeMap = {
	isArray: 'Array',
	isArrayBuffer: 'ArrayBuffer',
	isArrayLike: 'array-like',
	isAsyncFunction: 'AsyncFunction',
	isAsyncGenerator: 'AsyncGenerator',
	isAsyncGeneratorFunction: 'AsyncGeneratorFunction',
	isAsyncIterable: 'AsyncIterable',
	isBigint: 'bigint',
	isBigInt64Array: 'BigInt64Array',
	isBigUint64Array: 'BigUint64Array',
	isBlob: 'Blob',
	isBoolean: 'boolean',
	isBoundFunction: 'Function',
	isBuffer: 'Buffer',
	isClass: 'Class',
	isDataView: 'DataView',
	isDate: 'Date',
	isDirectInstanceOf: 'T',
	isEmptyArray: 'empty array',
	isEmptyMap: 'empty map',
	isEmptyObject: 'empty object',
	isEmptySet: 'empty set',
	isEmptyString: 'empty string',
	isEmptyStringOrWhitespace: 'empty string or whitespace',
	isEnumCase: 'EnumCase',
	isError: 'Error',
	isEvenInteger: 'even integer',
	isFalsy: 'falsy',
	isFloat32Array: 'Float32Array',
	isFloat64Array: 'Float64Array',
	isFormData: 'FormData',
	isFunction: 'Function',
	isGenerator: 'Generator',
	isGeneratorFunction: 'GeneratorFunction',
	isHtmlElement: 'HTMLElement',
	isInfinite: 'infinite number',
	isInRange: 'in range',
	isInt16Array: 'Int16Array',
	isInt32Array: 'Int32Array',
	isInt8Array: 'Int8Array',
	isInteger: 'integer',
	isIterable: 'Iterable',
	isMap: 'Map',
	isNan: 'NaN',
	isNativePromise: 'native Promise',
	isNegativeNumber: 'negative number',
	isNodeStream: 'Node.js Stream',
	isNonEmptyArray: 'non-empty array',
	isNonEmptyMap: 'non-empty map',
	isNonEmptyObject: 'non-empty object',
	isNonEmptySet: 'non-empty set',
	isNonEmptyString: 'non-empty string',
	isNonEmptyStringAndNotWhitespace: 'non-empty string and not whitespace',
	isNull: 'null',
	isNullOrUndefined: 'null or undefined',
	isNumber: 'number',
	isNumericString: 'string with a number',
	isObject: 'Object',
	isObservable: 'Observable',
	isOddInteger: 'odd integer',
	isPlainObject: 'plain object',
	isPositiveNumber: 'positive number',
	isPrimitive: 'primitive',
	isPromise: 'Promise',
	isPropertyKey: 'PropertyKey',
	isRegExp: 'RegExp',
	isSafeInteger: 'integer',
	isSet: 'Set',
	isSharedArrayBuffer: 'SharedArrayBuffer',
	isString: 'string',
	isSymbol: 'symbol',
	isTruthy: 'truthy',
	isTupleLike: 'tuple-like',
	isTypedArray: 'TypedArray',
	isUint16Array: 'Uint16Array',
	isUint32Array: 'Uint32Array',
	isUint8Array: 'Uint8Array',
	isUint8ClampedArray: 'Uint8ClampedArray',
	isUndefined: 'undefined',
	isUrlInstance: 'URL',
	isUrlSearchParams: 'URLSearchParams',
	isUrlString: 'string with a URL',
	isValidDate: 'valid Date',
	isValidLength: 'valid length',
	isWeakMap: 'WeakMap',
	isWeakRef: 'WeakRef',
	isWeakSet: 'WeakSet',
	isWhitespaceString: 'whitespace string',
} as const;

type IsMethodName = keyof typeof methodTypeMap;
const isMethodNames: IsMethodName[] = keysOf(methodTypeMap);

function isIsMethodName(value: unknown): value is IsMethodName {
	return isMethodNames.includes(value as IsMethodName);
}

export function assertAll(predicate: Predicate | readonly Predicate[], ...values: unknown[]): void | never {
	if (values.length === 0) {
		throw new TypeError('Invalid number of values');
	}

	if (!isAll(predicate, ...values)) {
		const predicateFunction = predicate as Predicate;
		const expectedType = !Array.isArray(predicate) && isIsMethodName(predicateFunction.name) ? methodTypeMap[predicateFunction.name] : 'predicate returns truthy for all values';
		throw new TypeError(typeErrorMessageMultipleValues(expectedType, values));
	}
}

export function assertAny(predicate: Predicate | readonly Predicate[], ...values: unknown[]): void | never {
	if (values.length === 0) {
		throw new TypeError('Invalid number of values');
	}

	if (!isAny(predicate, ...values)) {
		const predicates = Array.isArray(predicate) ? predicate as readonly Predicate[] : [predicate as Predicate];
		const expectedTypes = predicates.map(singlePredicate => isIsMethodName(singlePredicate.name) ? methodTypeMap[singlePredicate.name] : 'predicate returns truthy for any value');
		throw new TypeError(typeErrorMessageMultipleValues(expectedTypes, values));
	}
}

export function assertOptional<T>(value: unknown, assertion: (value: unknown, message?: string) => asserts value is T, message?: string): asserts value is T | undefined {
	if (!isUndefined(value)) {
		assertion(value, message);
	}
}

export function assertArray<T = unknown>(value: unknown, assertion?: (element: unknown, message?: string) => asserts element is T, message?: string): asserts value is T[] {
	if (!isArray(value)) {
		throw new TypeError(message ?? typeErrorMessage('Array', value));
	}

	if (assertion) {
		for (const element of value) {
			// @ts-expect-error: "Assertions require every name in the call target to be declared with an explicit type annotation."
			assertion(element, message);
		}
	}
}

export function assertArrayBuffer(value: unknown, message?: string): asserts value is ArrayBuffer {
	if (!isArrayBuffer(value)) {
		throw new TypeError(message ?? typeErrorMessage('ArrayBuffer', value));
	}
}

export function assertArrayLike<T = unknown>(value: unknown, message?: string): asserts value is ArrayLike<T> {
	if (!isArrayLike(value)) {
		throw new TypeError(message ?? typeErrorMessage('array-like', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertAsyncFunction(value: unknown, message?: string): asserts value is Function {
	if (!isAsyncFunction(value)) {
		throw new TypeError(message ?? typeErrorMessage('AsyncFunction', value));
	}
}

export function assertAsyncGenerator(value: unknown, message?: string): asserts value is AsyncGenerator {
	if (!isAsyncGenerator(value)) {
		throw new TypeError(message ?? typeErrorMessage('AsyncGenerator', value));
	}
}

export function assertAsyncGeneratorFunction(value: unknown, message?: string): asserts value is AsyncGeneratorFunction {
	if (!isAsyncGeneratorFunction(value)) {
		throw new TypeError(message ?? typeErrorMessage('AsyncGeneratorFunction', value));
	}
}

export function assertAsyncIterable<T = unknown>(value: unknown, message?: string): asserts value is AsyncIterable<T> {
	if (!isAsyncIterable(value)) {
		throw new TypeError(message ?? typeErrorMessage('AsyncIterable', value));
	}
}

export function assertBigint(value: unknown, message?: string): asserts value is bigint {
	if (!isBigint(value)) {
		throw new TypeError(message ?? typeErrorMessage('bigint', value));
	}
}

export function assertBigInt64Array(value: unknown, message?: string): asserts value is BigInt64Array {
	if (!isBigInt64Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('BigInt64Array', value));
	}
}

export function assertBigUint64Array(value: unknown, message?: string): asserts value is BigUint64Array {
	if (!isBigUint64Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('BigUint64Array', value));
	}
}

export function assertBlob(value: unknown, message?: string): asserts value is Blob {
	if (!isBlob(value)) {
		throw new TypeError(message ?? typeErrorMessage('Blob', value));
	}
}

export function assertBoolean(value: unknown, message?: string): asserts value is boolean {
	if (!isBoolean(value)) {
		throw new TypeError(message ?? typeErrorMessage('boolean', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertBoundFunction(value: unknown, message?: string): asserts value is Function {
	if (!isBoundFunction(value)) {
		throw new TypeError(message ?? typeErrorMessage('Function', value));
	}
}

/**
Note: [Prefer using `Uint8Array` instead of `Buffer`.](https://sindresorhus.com/blog/goodbye-nodejs-buffer)
*/
export function assertBuffer(value: unknown, message?: string): asserts value is NodeBuffer {
	if (!isBuffer(value)) {
		throw new TypeError(message ?? typeErrorMessage('Buffer', value));
	}
}

export function assertClass<T>(value: unknown, message?: string): asserts value is Class<T> {
	if (!isClass(value)) {
		throw new TypeError(message ?? typeErrorMessage('Class', value));
	}
}

export function assertDataView(value: unknown, message?: string): asserts value is DataView {
	if (!isDataView(value)) {
		throw new TypeError(message ?? typeErrorMessage('DataView', value));
	}
}

export function assertDate(value: unknown, message?: string): asserts value is Date {
	if (!isDate(value)) {
		throw new TypeError(message ?? typeErrorMessage('Date', value));
	}
}

export function assertDirectInstanceOf<T>(instance: unknown, class_: Class<T>, message?: string): asserts instance is T {
	if (!isDirectInstanceOf(instance, class_)) {
		throw new TypeError(message ?? typeErrorMessage('T', instance));
	}
}

export function assertEmptyArray(value: unknown, message?: string): asserts value is never[] {
	if (!isEmptyArray(value)) {
		throw new TypeError(message ?? typeErrorMessage('empty array', value));
	}
}

export function assertEmptyMap(value: unknown, message?: string): asserts value is Map<never, never> {
	if (!isEmptyMap(value)) {
		throw new TypeError(message ?? typeErrorMessage('empty map', value));
	}
}

export function assertEmptyObject<Key extends keyof any = string>(value: unknown, message?: string): asserts value is Record<Key, never> {
	if (!isEmptyObject(value)) {
		throw new TypeError(message ?? typeErrorMessage('empty object', value));
	}
}

export function assertEmptySet(value: unknown, message?: string): asserts value is Set<never> {
	if (!isEmptySet(value)) {
		throw new TypeError(message ?? typeErrorMessage('empty set', value));
	}
}

export function assertEmptyString(value: unknown, message?: string): asserts value is '' {
	if (!isEmptyString(value)) {
		throw new TypeError(message ?? typeErrorMessage('empty string', value));
	}
}

export function assertEmptyStringOrWhitespace(value: unknown, message?: string): asserts value is '' | Whitespace {
	if (!isEmptyStringOrWhitespace(value)) {
		throw new TypeError(message ?? typeErrorMessage('empty string or whitespace', value));
	}
}

export function assertEnumCase<T = unknown>(value: unknown, targetEnum: T, message?: string): asserts value is T[keyof T] {
	if (!isEnumCase(value, targetEnum)) {
		throw new TypeError(message ?? typeErrorMessage('EnumCase', value));
	}
}

export function assertError(value: unknown, message?: string): asserts value is Error {
	if (!isError(value)) {
		throw new TypeError(message ?? typeErrorMessage('Error', value));
	}
}

export function assertEvenInteger(value: number, message?: string): asserts value is number {
	if (!isEvenInteger(value)) {
		throw new TypeError(message ?? typeErrorMessage('even integer', value));
	}
}

export function assertFalsy(value: unknown, message?: string): asserts value is Falsy {
	if (!isFalsy(value)) {
		throw new TypeError(message ?? typeErrorMessage('falsy', value));
	}
}

export function assertFloat32Array(value: unknown, message?: string): asserts value is Float32Array {
	if (!isFloat32Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Float32Array', value));
	}
}

export function assertFloat64Array(value: unknown, message?: string): asserts value is Float64Array {
	if (!isFloat64Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Float64Array', value));
	}
}

export function assertFormData(value: unknown, message?: string): asserts value is FormData {
	if (!isFormData(value)) {
		throw new TypeError(message ?? typeErrorMessage('FormData', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertFunction(value: unknown, message?: string): asserts value is Function {
	if (!isFunction(value)) {
		throw new TypeError(message ?? typeErrorMessage('Function', value));
	}
}

export function assertGenerator(value: unknown, message?: string): asserts value is Generator {
	if (!isGenerator(value)) {
		throw new TypeError(message ?? typeErrorMessage('Generator', value));
	}
}

export function assertGeneratorFunction(value: unknown, message?: string): asserts value is GeneratorFunction {
	if (!isGeneratorFunction(value)) {
		throw new TypeError(message ?? typeErrorMessage('GeneratorFunction', value));
	}
}

export function assertHtmlElement(value: unknown, message?: string): asserts value is HTMLElement {
	if (!isHtmlElement(value)) {
		throw new TypeError(message ?? typeErrorMessage('HTMLElement', value));
	}
}

export function assertInfinite(value: unknown, message?: string): asserts value is number {
	if (!isInfinite(value)) {
		throw new TypeError(message ?? typeErrorMessage('infinite number', value));
	}
}

export function assertInRange(value: number, range: number | [number, number], message?: string): asserts value is number {
	if (!isInRange(value, range)) {
		throw new TypeError(message ?? typeErrorMessage('in range', value));
	}
}

export function assertInt16Array(value: unknown, message?: string): asserts value is Int16Array {
	if (!isInt16Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Int16Array', value));
	}
}

export function assertInt32Array(value: unknown, message?: string): asserts value is Int32Array {
	if (!isInt32Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Int32Array', value));
	}
}

export function assertInt8Array(value: unknown, message?: string): asserts value is Int8Array {
	if (!isInt8Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Int8Array', value));
	}
}

export function assertInteger(value: unknown, message?: string): asserts value is number {
	if (!isInteger(value)) {
		throw new TypeError(message ?? typeErrorMessage('integer', value));
	}
}

export function assertIterable<T = unknown>(value: unknown, message?: string): asserts value is Iterable<T> {
	if (!isIterable(value)) {
		throw new TypeError(message ?? typeErrorMessage('Iterable', value));
	}
}

export function assertMap<Key = unknown, Value = unknown>(value: unknown, message?: string): asserts value is Map<Key, Value> {
	if (!isMap(value)) {
		throw new TypeError(message ?? typeErrorMessage('Map', value));
	}
}

export function assertNan(value: unknown, message?: string): asserts value is number {
	if (!isNan(value)) {
		throw new TypeError(message ?? typeErrorMessage('NaN', value));
	}
}

export function assertNativePromise<T = unknown>(value: unknown, message?: string): asserts value is Promise<T> {
	if (!isNativePromise(value)) {
		throw new TypeError(message ?? typeErrorMessage('native Promise', value));
	}
}

export function assertNegativeNumber(value: unknown, message?: string): asserts value is number {
	if (!isNegativeNumber(value)) {
		throw new TypeError(message ?? typeErrorMessage('negative number', value));
	}
}

export function assertNodeStream(value: unknown, message?: string): asserts value is NodeStream {
	if (!isNodeStream(value)) {
		throw new TypeError(message ?? typeErrorMessage('Node.js Stream', value));
	}
}

export function assertNonEmptyArray<T = unknown, Item = unknown>(value: T | Item[], message?: string): asserts value is [Item, ...Item[]] {
	if (!isNonEmptyArray(value)) {
		throw new TypeError(message ?? typeErrorMessage('non-empty array', value));
	}
}

export function assertNonEmptyMap<Key = unknown, Value = unknown>(value: unknown, message?: string): asserts value is Map<Key, Value> {
	if (!isNonEmptyMap(value)) {
		throw new TypeError(message ?? typeErrorMessage('non-empty map', value));
	}
}

export function assertNonEmptyObject<Key extends keyof any = string, Value = unknown>(value: unknown, message?: string): asserts value is Record<Key, Value> {
	if (!isNonEmptyObject(value)) {
		throw new TypeError(message ?? typeErrorMessage('non-empty object', value));
	}
}

export function assertNonEmptySet<T = unknown>(value: unknown, message?: string): asserts value is Set<T> {
	if (!isNonEmptySet(value)) {
		throw new TypeError(message ?? typeErrorMessage('non-empty set', value));
	}
}

export function assertNonEmptyString(value: unknown, message?: string): asserts value is string {
	if (!isNonEmptyString(value)) {
		throw new TypeError(message ?? typeErrorMessage('non-empty string', value));
	}
}

export function assertNonEmptyStringAndNotWhitespace(value: unknown, message?: string): asserts value is string {
	if (!isNonEmptyStringAndNotWhitespace(value)) {
		throw new TypeError(message ?? typeErrorMessage('non-empty string and not whitespace', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertNull(value: unknown, message?: string): asserts value is null {
	if (!isNull(value)) {
		throw new TypeError(message ?? typeErrorMessage('null', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertNullOrUndefined(value: unknown, message?: string): asserts value is null | undefined {
	if (!isNullOrUndefined(value)) {
		throw new TypeError(message ?? typeErrorMessage('null or undefined', value));
	}
}

export function assertNumber(value: unknown, message?: string): asserts value is number {
	if (!isNumber(value)) {
		throw new TypeError(message ?? typeErrorMessage('number', value));
	}
}

export function assertNumericString(value: unknown, message?: string): asserts value is `${number}` {
	if (!isNumericString(value)) {
		throw new TypeError(message ?? typeErrorMessage('string with a number', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertObject(value: unknown, message?: string): asserts value is object {
	if (!isObject(value)) {
		throw new TypeError(message ?? typeErrorMessage('Object', value));
	}
}

export function assertObservable(value: unknown, message?: string): asserts value is ObservableLike {
	if (!isObservable(value)) {
		throw new TypeError(message ?? typeErrorMessage('Observable', value));
	}
}

export function assertOddInteger(value: number, message?: string): asserts value is number {
	if (!isOddInteger(value)) {
		throw new TypeError(message ?? typeErrorMessage('odd integer', value));
	}
}

export function assertPlainObject<Value = unknown>(value: unknown, message?: string): asserts value is Record<PropertyKey, Value> {
	if (!isPlainObject(value)) {
		throw new TypeError(message ?? typeErrorMessage('plain object', value));
	}
}

export function assertPositiveNumber(value: unknown, message?: string): asserts value is number {
	if (!isPositiveNumber(value)) {
		throw new TypeError(message ?? typeErrorMessage('positive number', value));
	}
}

export function assertPrimitive(value: unknown, message?: string): asserts value is Primitive {
	if (!isPrimitive(value)) {
		throw new TypeError(message ?? typeErrorMessage('primitive', value));
	}
}

export function assertPromise<T = unknown>(value: unknown, message?: string): asserts value is Promise<T> {
	if (!isPromise(value)) {
		throw new TypeError(message ?? typeErrorMessage('Promise', value));
	}
}

export function assertPropertyKey(value: unknown, message?: string): asserts value is number {
	if (!isPropertyKey(value)) {
		throw new TypeError(message ?? typeErrorMessage('PropertyKey', value));
	}
}

export function assertRegExp(value: unknown, message?: string): asserts value is RegExp {
	if (!isRegExp(value)) {
		throw new TypeError(message ?? typeErrorMessage('RegExp', value));
	}
}

export function assertSafeInteger(value: unknown, message?: string): asserts value is number {
	if (!isSafeInteger(value)) {
		throw new TypeError(message ?? typeErrorMessage('integer', value));
	}
}

export function assertSet<T = unknown>(value: unknown, message?: string): asserts value is Set<T> {
	if (!isSet(value)) {
		throw new TypeError(message ?? typeErrorMessage('Set', value));
	}
}

export function assertSharedArrayBuffer(value: unknown, message?: string): asserts value is SharedArrayBuffer {
	if (!isSharedArrayBuffer(value)) {
		throw new TypeError(message ?? typeErrorMessage('SharedArrayBuffer', value));
	}
}

export function assertString(value: unknown, message?: string): asserts value is string {
	if (!isString(value)) {
		throw new TypeError(message ?? typeErrorMessage('string', value));
	}
}

export function assertSymbol(value: unknown, message?: string): asserts value is symbol {
	if (!isSymbol(value)) {
		throw new TypeError(message ?? typeErrorMessage('symbol', value));
	}
}

export function assertTruthy<T>(value: T | Falsy, message?: string): asserts value is T {
	if (!isTruthy(value)) {
		throw new TypeError(message ?? typeErrorMessage('truthy', value));
	}
}

export function assertTupleLike<T extends Array<TypeGuard<unknown>>>(value: unknown, guards: [...T], message?: string): asserts value is ResolveTypesOfTypeGuardsTuple<T> {
	if (!isTupleLike(value, guards)) {
		throw new TypeError(message ?? typeErrorMessage('tuple-like', value));
	}
}

export function assertTypedArray(value: unknown, message?: string): asserts value is TypedArray {
	if (!isTypedArray(value)) {
		throw new TypeError(message ?? typeErrorMessage('TypedArray', value));
	}
}

export function assertUint16Array(value: unknown, message?: string): asserts value is Uint16Array {
	if (!isUint16Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Uint16Array', value));
	}
}

export function assertUint32Array(value: unknown, message?: string): asserts value is Uint32Array {
	if (!isUint32Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Uint32Array', value));
	}
}

export function assertUint8Array(value: unknown, message?: string): asserts value is Uint8Array {
	if (!isUint8Array(value)) {
		throw new TypeError(message ?? typeErrorMessage('Uint8Array', value));
	}
}

export function assertUint8ClampedArray(value: unknown, message?: string): asserts value is Uint8ClampedArray {
	if (!isUint8ClampedArray(value)) {
		throw new TypeError(message ?? typeErrorMessage('Uint8ClampedArray', value));
	}
}

export function assertUndefined(value: unknown, message?: string): asserts value is undefined {
	if (!isUndefined(value)) {
		throw new TypeError(message ?? typeErrorMessage('undefined', value));
	}
}

export function assertUrlInstance(value: unknown, message?: string): asserts value is URL {
	if (!isUrlInstance(value)) {
		throw new TypeError(message ?? typeErrorMessage('URL', value));
	}
}

// eslint-disable-next-line unicorn/prevent-abbreviations
export function assertUrlSearchParams(value: unknown, message?: string): asserts value is URLSearchParams {
	if (!isUrlSearchParams(value)) {
		throw new TypeError(message ?? typeErrorMessage('URLSearchParams', value));
	}
}

export function assertUrlString(value: unknown, message?: string): asserts value is UrlString {
	if (!isUrlString(value)) {
		throw new TypeError(message ?? typeErrorMessage('string with a URL', value));
	}
}

export function assertValidDate(value: unknown, message?: string): asserts value is Date {
	if (!isValidDate(value)) {
		throw new TypeError(message ?? typeErrorMessage('valid Date', value));
	}
}

export function assertValidLength(value: unknown, message?: string): asserts value is number {
	if (!isValidLength(value)) {
		throw new TypeError(message ?? typeErrorMessage('valid length', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertWeakMap<Key extends object = object, Value = unknown>(value: unknown, message?: string): asserts value is WeakMap<Key, Value> {
	if (!isWeakMap(value)) {
		throw new TypeError(message ?? typeErrorMessage('WeakMap', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types, unicorn/prevent-abbreviations
export function assertWeakRef<T extends object = object>(value: unknown, message?: string): asserts value is WeakRef<T> {
	if (!isWeakRef(value)) {
		throw new TypeError(message ?? typeErrorMessage('WeakRef', value));
	}
}

// eslint-disable-next-line @typescript-eslint/ban-types
export function assertWeakSet<T extends object = object>(value: unknown, message?: string): asserts value is WeakSet<T> {
	if (!isWeakSet(value)) {
		throw new TypeError(message ?? typeErrorMessage('WeakSet', value));
	}
}

export function assertWhitespaceString(value: unknown, message?: string): asserts value is string {
	if (!isWhitespaceString(value)) {
		throw new TypeError(message ?? typeErrorMessage('whitespace string', value));
	}
}

export default is;

export type {
	ArrayLike,
	Class,
	NodeStream,
	ObservableLike,
	Predicate,
	Primitive,
	TypedArray,
	UrlString,
} from './types.js';
```

## File: `source/types.ts`
```typescript
// Extracted from https://github.com/sindresorhus/type-fest/blob/78019f42ea888b0cdceb41a4a78163868de57555/index.d.ts

/**
Matches any [primitive value](https://developer.mozilla.org/en-US/docs/Glossary/Primitive).
*/
export type Primitive =
	| null // eslint-disable-line @typescript-eslint/ban-types
	| undefined
	| string
	| number
	| boolean
	| symbol
	| bigint;

/**
Matches a [`class` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes).
*/
type Constructor<T, Arguments extends unknown[] = any[]> = new(...arguments_: Arguments) => T;

/**
Matches a [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes).
*/
export type Class<T, Arguments extends unknown[] = any[]> = Constructor<T, Arguments> & {prototype: T};

/**
Matches any [typed array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), like `Uint8Array` or `Float64Array`.
*/
export type TypedArray =
	| Int8Array
	| Uint8Array
	| Uint8ClampedArray
	| Int16Array
	| Uint16Array
	| Int32Array
	| Uint32Array
	| Float32Array
	| Float64Array
	| BigInt64Array
	| BigUint64Array;

declare global {
	// eslint-disable-next-line @typescript-eslint/consistent-type-definitions -- This must be an `interface` so it can be merged.
	interface SymbolConstructor {
		readonly observable: symbol;
	}
}

/**
Matches a value that is like an [Observable](https://github.com/tc39/proposal-observable).
*/
export type ObservableLike = {
	subscribe(observer: (value: unknown) => void): void;
	[Symbol.observable](): ObservableLike;
};

// eslint-disable-next-line @typescript-eslint/ban-types
export type Falsy = false | 0 | 0n | '' | null | undefined;

export type WeakRef<T extends object> = { // eslint-disable-line @typescript-eslint/ban-types, unicorn/prevent-abbreviations
	readonly [Symbol.toStringTag]: 'WeakRef';
	deref(): T | undefined;
};

export type ArrayLike<T> = {
	readonly [index: number]: T;
	readonly length: number;
};

export type NodeStream = {
	pipe<T extends NodeJS.WritableStream>(destination: T, options?: {end?: boolean}): T;
} & NodeJS.EventEmitter;

export type Predicate = (value: unknown) => boolean;

export type NonEmptyString = string & {0: string};

export type Whitespace = ' ';

/**
A string that represents a valid URL.

This is a branded type to prevent incorrect TypeScript type narrowing.
*/
export type UrlString = string & {readonly __brand: 'UrlString'};
```

## File: `source/utilities.ts`
```typescript
export function keysOf<T extends Record<PropertyKey, unknown>>(value: T): Array<keyof T> {
	return Object.keys(value) as Array<keyof T>;
}
```

## File: `test/test.ts`
```typescript
/* eslint-disable @typescript-eslint/no-empty-function */
import {Buffer} from 'node:buffer';
import fs from 'node:fs';
import net from 'node:net';
import Stream from 'node:stream';
import {inspect} from 'node:util';
import test, {type ExecutionContext} from 'ava';
import {JSDOM} from 'jsdom';
import {Subject, Observable} from 'rxjs';
import {temporaryFile} from 'tempy';
import {expectTypeOf} from 'expect-type';
import ZenObservable from 'zen-observable';
import is, {
	assert,
	type AssertionTypeDescription,
	type Predicate,
	type Primitive,
	type TypedArray,
	type TypeName,
	type UrlString,
} from '../source/index.js';
import {keysOf} from '../source/utilities.js';

class PromiseSubclassFixture<T> extends Promise<T> {}
class ErrorSubclassFixture extends Error {}

const {window} = new JSDOM();
const {document} = window;

const structuredClone = globalThis.structuredClone ?? (x => x);

type Test = Readonly<{
	fixtures: unknown[];
	typename?: TypeName;
	typeDescription?: AssertionTypeDescription;
}>;

// Every entry should be unique and belongs in the most specific type for that entry
const reusableFixtures = {
	asyncFunction: [async function () {}, async () => {}],
	asyncGeneratorFunction: [
		async function * () {},
		async function * () {
			yield 4;
		},
	],
	boundFunction: [() => {}, function () {}.bind(null)], // eslint-disable-line no-extra-bind
	buffer: [Buffer.from('🦄')],
	emptyArray: [[], new Array()], // eslint-disable-line @typescript-eslint/no-array-constructor
	emptyMap: [new Map()],
	emptySet: [new Set()],
	emptyString: ['', String()],
	function: [
		function foo() {}, // eslint-disable-line func-names
		function () {},
	],
	generatorFunction: [
		function * () {},
		function * () {
			yield 4;
		},
	],
	infinite: [Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY],
	integer: [0, -0, 6],
	nativePromise: [Promise.resolve(), PromiseSubclassFixture.resolve()],
	number: [1.4],
	numericString: ['5', '-3.2', 'Infinity', '0x56'],
	plainObject: [
		{x: 1},
		Object.create(null),
		new Object(), // eslint-disable-line no-object-constructor
		structuredClone({x: 1}),
		structuredClone(Object.create(null)),
		structuredClone(new Object()), // eslint-disable-line no-object-constructor
	],
	promise: [Object.create({then() {}, catch() {}})], // eslint-disable-line unicorn/no-thenable
	safeInteger: [(2 ** 53) - 1, -(2 ** 53) + 1],
} as const satisfies Partial<{[K in keyof typeof is]: unknown[]}>;

const primitiveTypes = {
	undefined: {
		fixtures: [
			undefined,
		],
		typename: 'undefined',
	},
	null: {
		fixtures: [
			null,
		],
		typename: 'null',
	},
	string: {
		fixtures: [
			'🦄',
			'hello world',
			...reusableFixtures.emptyString,
			...reusableFixtures.numericString,
		],
		typename: 'string',
	},
	emptyString: {
		fixtures: [...reusableFixtures.emptyString],
		typename: 'string',
		typeDescription: 'empty string',
	},
	number: {
		fixtures: [
			...reusableFixtures.number,
			...reusableFixtures.infinite,
			...reusableFixtures.integer,
			...reusableFixtures.safeInteger,
		],
		typename: 'number',
	},
	bigint: {
		fixtures: [
			1n,
			0n,
			-0n,
			BigInt('1234'),
		],
		typename: 'bigint',
	},
	boolean: {
		fixtures: [
			true, false,
		],
		typename: 'boolean',
	},
	numericString: {
		fixtures: [...reusableFixtures.numericString],
		typename: 'string',
		typeDescription: 'string with a number',
	},
	nan: {
		fixtures: [
			NaN, // eslint-disable-line unicorn/prefer-number-properties
			Number.NaN,
		],
		typename: 'NaN',
		typeDescription: 'NaN',
	},
	nullOrUndefined: {
		fixtures: [
			null,
			undefined,
		],
		typeDescription: 'null or undefined',
	},
	integer: {
		fixtures: [...reusableFixtures.integer, ...reusableFixtures.safeInteger],
		typename: 'number',
		typeDescription: 'integer',
	},
	safeInteger: {
		fixtures: [...reusableFixtures.integer, ...reusableFixtures.safeInteger],
		typename: 'number',
		typeDescription: 'integer',
	},
	infinite: {
		fixtures: [...reusableFixtures.infinite],
		typename: 'number',
		typeDescription: 'infinite number',
	},
} as const satisfies Partial<{[K in keyof typeof is]: Test}>;

const objectTypes = {
	symbol: {
		fixtures: [
			Symbol('🦄'),
		],
		typename: 'symbol',
	},
	array: {
		fixtures: [
			[1, 2],
			Array.from({length: 2}),
			...reusableFixtures.emptyArray,
		],
		typename: 'Array',
	},
	emptyArray: {
		fixtures: [...reusableFixtures.emptyArray],
		typename: 'Array',
		typeDescription: 'empty array',
	},
	function: {
		fixtures: [
			...reusableFixtures.asyncFunction,
			...reusableFixtures.asyncGeneratorFunction,
			...reusableFixtures.boundFunction,
			...reusableFixtures.function,
			...reusableFixtures.generatorFunction,
		],
		typename: 'Function',
	},
	buffer: {
		fixtures: [...reusableFixtures.buffer],
		typename: 'Buffer',
	},
	blob: {
		fixtures: [
			new window.Blob(),
		],
		typename: 'Blob',
	},
	object: {
		fixtures: [
			Object.create({x: 1}),
			...reusableFixtures.plainObject,
		],
		typename: 'Object',
	},
	regExp: {
		fixtures: [
			/\w/,
			new RegExp('\\w'), // eslint-disable-line prefer-regex-literals
		],
		typename: 'RegExp',
	},
	date: {
		fixtures: [
			new Date(),
		],
		typename: 'Date',
	},
	error: {
		fixtures: [
			new Error('🦄'),
			new ErrorSubclassFixture(),
		],
		typename: 'Error',
	},
	nativePromise: {
		fixtures: [...reusableFixtures.nativePromise],
		typename: 'Promise',
		typeDescription: 'native Promise',
	},
	promise: {
		fixtures: [
			...reusableFixtures.nativePromise,
			...reusableFixtures.promise,
		],
		typename: 'Promise',
		typeDescription: 'Promise',
	},
	generator: {
		fixtures: [
			(function * () {
				yield 4;
			})(),
		],
		typename: 'Generator',
	},
	asyncGenerator: {
		fixtures: [
			(async function * () {
				yield 4;
			})(),
		],
		typename: 'AsyncGenerator',
	},
	generatorFunction: {
		fixtures: [...reusableFixtures.generatorFunction],
		typename: 'Function',
		typeDescription: 'GeneratorFunction',
	},
	asyncGeneratorFunction: {
		fixtures: [...reusableFixtures.asyncGeneratorFunction],
		typename: 'Function',
		typeDescription: 'AsyncGeneratorFunction',
	},
	asyncFunction: {
		fixtures: [...reusableFixtures.asyncFunction],
		typename: 'Function',
		typeDescription: 'AsyncFunction',
	},
	boundFunction: {
		fixtures: [...reusableFixtures.boundFunction, ...reusableFixtures.asyncFunction],
		typename: 'Function',
	},
	map: {
		fixtures: [
			new Map([['one', '1']]),
			...reusableFixtures.emptyMap,
		],
		typename: 'Map',
	},
	emptyMap: {
		fixtures: [...reusableFixtures.emptyMap],
		typename: 'Map',
		typeDescription: 'empty map',
	},
	set: {
		fixtures: [
			new Set(['one']),
			...reusableFixtures.emptySet,
		],
		typename: 'Set',
	},
	emptySet: {
		fixtures: [...reusableFixtures.emptySet],
		typename: 'Set',
		typeDescription: 'empty set',
	},
	weakSet: {
		fixtures: [
			new WeakSet(),
		],
		typename: 'WeakSet',
	},
	weakRef: {
		fixtures: [
			new window.WeakRef({}),
		],
		typename: 'WeakRef',
	},
	weakMap: {
		fixtures: [
			new WeakMap(),
		],
		typename: 'WeakMap',
	},
	int8Array: {
		fixtures: [
			new Int8Array(),
		],
		typename: 'Int8Array',
	},
	uint8Array: {
		fixtures: [
			new Uint8Array(),
		],
		typename: 'Uint8Array',
	},
	uint8ClampedArray: {
		fixtures: [
			new Uint8ClampedArray(),
		],
		typename: 'Uint8ClampedArray',
	},
	int16Array: {
		fixtures: [
			new Int16Array(),
		],
		typename: 'Int16Array',
	},
	uint16Array: {
		fixtures: [
			new Uint16Array(),
		],
		typename: 'Uint16Array',
	},
	int32Array: {
		fixtures: [
			new Int32Array(),
		],
		typename: 'Int32Array',
	},
	uint32Array: {
		fixtures: [
			new Uint32Array(),
		],
		typename: 'Uint32Array',
	},
	float32Array: {
		fixtures: [
			new Float32Array(),
		],
		typename: 'Float32Array',
	},
	float64Array: {
		fixtures: [
			new Float64Array(),
		],
		typename: 'Float64Array',
	},
	bigInt64Array: {
		fixtures: [
			new BigInt64Array(),
		],
		typename: 'BigInt64Array',
	},
	bigUint64Array: {
		fixtures: [
			new BigUint64Array(),
		],
		typename: 'BigUint64Array',
	},
	arrayBuffer: {
		fixtures: [
			new ArrayBuffer(10),
		],
		typename: 'ArrayBuffer',
	},
	dataView: {
		fixtures: [
			new DataView(new ArrayBuffer(10)),
		],
		typename: 'DataView',
	},
	plainObject: {
		fixtures: [
			...reusableFixtures.plainObject,
		],
		typename: 'Object',
		typeDescription: 'plain object',
	},
	htmlElement: {
		fixtures: [
			'div',
			'input',
			'span',
			'img',
			'canvas',
			'script',
		]
			.map(fixture => document.createElement(fixture)),
		typeDescription: 'HTMLElement',
	},
	observable: {
		fixtures: [
			new Observable(),
			new Subject(),
			new ZenObservable(() => {}),
		],
		typename: 'Observable',
	},
	nodeStream: {
		fixtures: [
			fs.createReadStream('readme.md'),
			fs.createWriteStream(temporaryFile()),
			new net.Socket(),
			new Stream.Duplex(),
			new Stream.PassThrough(),
			new Stream.Readable(),
			new Stream.Transform(),
			new Stream.Stream(),
			new Stream.Writable(),
		],
		typename: 'Object',
		typeDescription: 'Node.js Stream',
	},
	formData: {
		fixtures: [
			new window.FormData(),
		],
		typename: 'FormData',
	},
} as const satisfies Partial<{[K in keyof typeof is]: Test}>;

const types = {
	...objectTypes,
	...primitiveTypes,
} as const satisfies Partial<{[K in keyof typeof is]: Test}>;

type TypeNameWithFixture = keyof typeof types;

const subClasses = new Map<TypeNameWithFixture, TypeNameWithFixture[]>([
	['uint8Array', ['buffer']], // It's too hard to differentiate the two
	['object', keysOf(objectTypes)],
]);

// This ensures a certain method matches only the types it's supposed to and none of the other methods' types
const exclusivelyTyped = test.macro({
	exec(t: ExecutionContext, type: TypeNameWithFixture) {
		const {fixtures, typeDescription, typename} = types[type] as Test;
		const valueType = typeDescription ?? typename ?? 'unspecified';

		const testAssert: (value: unknown) => never | void = assert[type];
		const testIs: Predicate = is[type];

		for (const fixture of fixtures) {
			t.true(testIs(fixture), `Value: ${inspect(fixture)}`);
			t.notThrows(() => {
				testAssert(fixture);
			});

			if (typename) {
				t.is<TypeName, TypeName>(is(fixture), typename);
			}
		}

		for (const key of keysOf(types).filter(key => key !== type)) {
			if (subClasses.has(type) && subClasses.get(type)?.includes(key)) {
				continue;
			}

			for (let i = 0; i < types[key].fixtures.length; i += 1) {
				const fixture: unknown = types[key].fixtures[i];

				if (fixtures.includes(fixture)) {
					continue;
				}

				t.false(testIs(fixture), `${key}.fixture[${i}]: ${inspect(fixture)} should not be ${type}`);
				t.throws(() => {
					testAssert(fixture);
				}, {
					message: `Expected value which is \`${valueType}\`, received value of type \`${is(fixture)}\`.`,
				});
			}
		}
	},
	title(_, type: TypeNameWithFixture) {
		return `is.${type}`;
	},
});

for (const type of keysOf(types)) {
	test(exclusivelyTyped, type);
}

test('is.positiveNumber', t => {
	t.true(is.positiveNumber(6));
	t.true(is.positiveNumber(1.4));
	t.true(is.positiveNumber(Number.POSITIVE_INFINITY));

	t.notThrows(() => {
		assert.positiveNumber(6);
	});
	t.notThrows(() => {
		assert.positiveNumber(1.4);
	});
	t.notThrows(() => {
		assert.positiveNumber(Number.POSITIVE_INFINITY);
	});

	t.false(is.positiveNumber(0));
	t.false(is.positiveNumber(-0));
	t.false(is.positiveNumber(-6));
	t.false(is.positiveNumber(-1.4));
	t.false(is.positiveNumber(Number.NEGATIVE_INFINITY));

	t.throws(() => {
		assert.positiveNumber(0);
	});
	t.throws(() => {
		assert.positiveNumber(-0);
	});
	t.throws(() => {
		assert.positiveNumber(-6);
	});
	t.throws(() => {
		assert.positiveNumber(-1.4);
	});
	t.throws(() => {
		assert.positiveNumber(Number.NEGATIVE_INFINITY);
	});
});

test('is.negativeNumber', t => {
	t.true(is.negativeNumber(-6));
	t.true(is.negativeNumber(-1.4));
	t.true(is.negativeNumber(Number.NEGATIVE_INFINITY));

	t.notThrows(() => {
		assert.negativeNumber(-6);
	});
	t.notThrows(() => {
		assert.negativeNumber(-1.4);
	});
	t.notThrows(() => {
		assert.negativeNumber(Number.NEGATIVE_INFINITY);
	});

	t.false(is.negativeNumber(0));
	t.false(is.negativeNumber(-0));
	t.false(is.negativeNumber(6));
	t.false(is.negativeNumber(1.4));
	t.false(is.negativeNumber(Number.POSITIVE_INFINITY));

	t.throws(() => {
		assert.negativeNumber(0);
	});
	t.throws(() => {
		assert.negativeNumber(-0);
	});
	t.throws(() => {
		assert.negativeNumber(6);
	});
	t.throws(() => {
		assert.negativeNumber(1.4);
	});
	t.throws(() => {
		assert.negativeNumber(Number.POSITIVE_INFINITY);
	});
});

test('is.numericString supplemental', t => {
	t.false(is.numericString(''));
	t.false(is.numericString(' '));
	t.false(is.numericString(' \t\t\n'));
	t.false(is.numericString(1));
	t.throws(() => {
		assert.numericString('');
	});
	t.throws(() => {
		assert.numericString(1);
	});
});

test('is.array supplemental', t => {
	t.true(is.array([1, 2, 3], is.number));
	t.false(is.array([1, '2', 3], is.number));

	t.notThrows(() => {
		assert.array([1, 2], assert.number);
	});

	t.throws(() => {
		assert.array([1, '2'], assert.number);
	});

	t.notThrows(() => {
		const x: unknown[] = [1, 2, 3];
		assert.array(x, assert.number);
		x[0]?.toFixed(0);
	});

	t.notThrows(() => {
		const x: unknown[] = [1, 2, 3];
		if (is.array<number>(x, is.number)) {
			x[0]?.toFixed(0);
		}
	});

	t.throws(() => {
		assert.array([1, '2'], assert.number, 'Expected numbers');
	}, {message: /Expected numbers/});
});

test('is.boundFunction supplemental', t => {
	t.false(is.boundFunction(function () {})); // eslint-disable-line prefer-arrow-callback

	t.throws(() => {
		assert.boundFunction(function () {}); // eslint-disable-line prefer-arrow-callback
	});
});

test('is.asyncFunction supplemental', t => {
	const fixture = async () => {};
	if (is.asyncFunction(fixture)) {
		t.true(is.function(fixture().then));

		t.notThrows(() => {
			assert.function(fixture().then);
		});
	}
});

test('is.asyncGenerator supplemental', t => {
	const fixture = (async function * () {
		yield 4;
	})();
	if (is.asyncGenerator(fixture)) {
		t.true(is.function(fixture.next));
	}
});

test('is.asyncGeneratorFunction supplemental', t => {
	const fixture = async function * () {
		yield 4;
	};

	if (is.asyncGeneratorFunction(fixture)) {
		t.true(is.function(fixture().next));
	}
});

test('is.enumCase', t => {
	enum NonNumericalEnum {
		Key1 = 'key1',
		Key2 = 'key2',
	}

	t.true(is.enumCase('key1', NonNumericalEnum));
	t.notThrows(() => {
		assert.enumCase('key1', NonNumericalEnum);
	});

	t.false(is.enumCase('invalid', NonNumericalEnum));
	t.throws(() => {
		assert.enumCase('invalid', NonNumericalEnum);
	});
});

test('is.directInstanceOf', t => {
	const error = new Error('fixture');
	const errorSubclass = new ErrorSubclassFixture();

	t.true(is.directInstanceOf(error, Error));
	t.true(is.directInstanceOf(errorSubclass, ErrorSubclassFixture));
	t.notThrows(() => {
		assert.directInstanceOf(error, Error);
	});
	t.notThrows(() => {
		assert.directInstanceOf(errorSubclass, ErrorSubclassFixture);
	});

	t.false(is.directInstanceOf(error, ErrorSubclassFixture));
	t.false(is.directInstanceOf(errorSubclass, Error));
	t.throws(() => {
		assert.directInstanceOf(error, ErrorSubclassFixture);
	});
	t.throws(() => {
		assert.directInstanceOf(errorSubclass, Error);
	});

	t.false(is.directInstanceOf(undefined, Error));
	t.false(is.directInstanceOf(null, Error));
});

test('is.urlInstance', t => {
	const url = new URL('https://example.com');
	t.true(is.urlInstance(url));
	t.false(is.urlInstance({}));
	t.false(is.urlInstance(undefined));
	t.false(is.urlInstance(null));

	t.notThrows(() => {
		assert.urlInstance(url);
	});
	t.throws(() => {
		assert.urlInstance({});
	});
	t.throws(() => {
		assert.urlInstance(undefined);
	});
	t.throws(() => {
		assert.urlInstance(null);
	});
});

test('is.urlString', t => {
	const url = 'https://example.com';
	t.true(is.urlString(url));
	t.false(is.urlString(new URL(url)));
	t.false(is.urlString({}));
	t.false(is.urlString(undefined));
	t.false(is.urlString(null));

	t.notThrows(() => {
		assert.urlString(url);
	});
	t.throws(() => {
		assert.urlString(new URL(url));
	});
	t.throws(() => {
		assert.urlString({});
	});
	t.throws(() => {
		assert.urlString(undefined);
	});
	t.throws(() => {
		assert.urlString(null);
	});
});

// Type test for urlString narrowing fix (issue #212)
// This test demonstrates that the fix allows proper type narrowing in both branches
(() => {
	const value: unknown = 'test';

	if (is.urlString(value)) {
		// ✅ In true branch: value is narrowed to UrlString
		expectTypeOf(value).toEqualTypeOf<UrlString>();
		expectTypeOf(value).toMatchTypeOf<string>();
	} else {
		// ✅ In false branch: value remains unknown (not incorrectly narrowed)
		expectTypeOf(value).toEqualTypeOf<unknown>();

		// ✅ Manual narrowing to string still works
		if (typeof value === 'string') {
			expectTypeOf(value).toEqualTypeOf<string>();
		}
	}
})();

test('is.truthy', t => {
	t.true(is.truthy('unicorn'));
	t.true(is.truthy('🦄'));
	t.true(is.truthy(new Set()));
	t.true(is.truthy(Symbol('🦄')));
	t.true(is.truthy(true));
	t.true(is.truthy(1));
	t.true(is.truthy(1n));
	t.true(is.truthy(BigInt(1)));

	t.notThrows(() => {
		assert.truthy('unicorn');
	});

	t.notThrows(() => {
		assert.truthy('🦄');
	});

	t.notThrows(() => {
		assert.truthy(new Set());
	});

	t.notThrows(() => {
		assert.truthy(Symbol('🦄'));
	});

	t.notThrows(() => {
		assert.truthy(true);
	});

	t.notThrows(() => {
		assert.truthy(1);
	});

	t.notThrows(() => {
		assert.truthy(1n);
	});

	t.notThrows(() => {
		assert.truthy(BigInt(1));
	});

	// Checks that `assert.truthy` narrow downs boolean type to `true`.
	{
		const booleans = [true, false];
		const function_ = (value: true) => value;
		assert.truthy(booleans[0]);
		function_(booleans[0]);
	}

	// Checks that `assert.truthy` excludes zero value from number type.
	{
		const bits: Array<0 | 1> = [1, 0, -0];
		const function_ = (value: 1) => value;
		assert.truthy(bits[0]);
		function_(bits[0]);
	}

	// Checks that `assert.truthy` excludes zero value from bigint type.
	{
		const bits: Array<0n | 1n> = [1n, 0n, -0n];
		const function_ = (value: 1n) => value;
		assert.truthy(bits[0]);
		function_(bits[0]);
	}

	// Checks that `assert.truthy` excludes empty string from string type.
	{
		const strings: Array<'nonEmpty' | ''> = ['nonEmpty', ''];
		const function_ = (value: 'nonEmpty') => value;
		assert.truthy(strings[0]);
		function_(strings[0]);
	}

	// Checks that `assert.truthy` excludes undefined from mixed type.
	{
		const maybeUndefineds = ['🦄', undefined];
		const function_ = (value: string) => value;
		assert.truthy(maybeUndefineds[0]);
		function_(maybeUndefineds[0]);
	}

	// Checks that `assert.truthy` excludes null from mixed type.
	{
		const maybeNulls = ['🦄', null];
		const function_ = (value: string) => value;
		assert.truthy(maybeNulls[0]);
		function_(maybeNulls[0]);
	}
});

test('is.falsy', t => {
	t.true(is.falsy(false));
	t.true(is.falsy(0));
	t.true(is.falsy(''));
	t.true(is.falsy(null));
	t.true(is.falsy(undefined));
	t.true(is.falsy(Number.NaN));
	t.true(is.falsy(0n));
	t.true(is.falsy(BigInt(0)));

	t.notThrows(() => {
		assert.falsy(false);
	});

	t.notThrows(() => {
		assert.falsy(0);
	});

	t.notThrows(() => {
		assert.falsy('');
	});

	t.notThrows(() => {
		assert.falsy(null);
	});

	t.notThrows(() => {
		assert.falsy(undefined);
	});

	t.notThrows(() => {
		assert.falsy(Number.NaN);
	});

	t.notThrows(() => {
		assert.falsy(0n);
	});

	t.notThrows(() => {
		assert.falsy(BigInt(0));
	});

	// Checks that `assert.falsy` narrow downs boolean type to `false`.
	{
		const booleans = [false, true];
		const function_ = (value?: false) => value;
		assert.falsy(booleans[0]);
		function_(booleans[0]);
	}

	// Checks that `assert.falsy` narrow downs number type to `0`.
	{
		const bits = [0, -0, 1];
		const function_ = (value?: 0) => value;
		assert.falsy(bits[0]);
		function_(bits[0]);
		assert.falsy(bits[1]);
		function_(bits[1]);
	}

	// Checks that `assert.falsy` narrow downs bigint type to `0n`.
	{
		const bits = [0n, -0n, 1n];
		const function_ = (value?: 0n) => value;
		assert.falsy(bits[0]);
		function_(bits[0]);
		assert.falsy(bits[1]);
		function_(bits[1]);
	}

	// Checks that `assert.falsy` narrow downs string type to empty string.
	{
		const strings = ['', 'nonEmpty'];
		const function_ = (value?: '') => value;
		assert.falsy(strings[0]);
		function_(strings[0]);
	}

	// Checks that `assert.falsy` can narrow down mixed type to undefined.
	{
		const maybeUndefineds = [undefined, Symbol('🦄')];
		const function_ = (value: undefined) => value;
		assert.falsy(maybeUndefineds[0]);
		function_(maybeUndefineds[0]);
	}

	// Checks that `assert.falsy` can narrow down mixed type to null.
	{
		const maybeNulls = [null, Symbol('🦄')];
		// eslint-disable-next-line @typescript-eslint/ban-types
		const function_ = (value?: null) => value;
		assert.falsy(maybeNulls[0]);
		function_(maybeNulls[0]);
	}
});

test('is.primitive', t => {
	const primitives: Primitive[] = [
		undefined,
		null,
		'🦄',
		6,
		Number.POSITIVE_INFINITY,
		Number.NEGATIVE_INFINITY,
		true,
		false,
		Symbol('🦄'),
		6n,
	];

	for (const element of primitives) {
		t.true(is.primitive(element));
		t.notThrows(() => {
			assert.primitive(element);
		});
	}
});

test('is.integer supplemental', t => {
	t.false(is.integer(1.4));
	t.throws(() => {
		assert.integer(1.4);
	});
});

test('is.safeInteger supplemental', t => {
	t.false(is.safeInteger(2 ** 53));
	t.false(is.safeInteger(-(2 ** 53)));
	t.throws(() => {
		assert.safeInteger(2 ** 53);
	});
	t.throws(() => {
		assert.safeInteger(-(2 ** 53));
	});
});

test('is.iterable', t => {
	t.true(is.iterable(''));
	t.true(is.iterable([]));
	t.true(is.iterable(new Map()));
	t.false(is.iterable(null));
	t.false(is.iterable(undefined));
	t.false(is.iterable(0));
	t.false(is.iterable(Number.NaN));
	t.false(is.iterable(Number.POSITIVE_INFINITY));
	t.false(is.iterable({}));

	t.notThrows(() => {
		assert.iterable('');
	});
	t.notThrows(() => {
		assert.iterable([]);
	});
	t.notThrows(() => {
		assert.iterable(new Map());
	});
	t.throws(() => {
		assert.iterable(null);
	});
	t.throws(() => {
		assert.iterable(undefined);
	});
	t.throws(() => {
		assert.iterable(0);
	});
	t.throws(() => {
		assert.iterable(Number.NaN);
	});
	t.throws(() => {
		assert.iterable(Number.POSITIVE_INFINITY);
	});
	t.throws(() => {
		assert.iterable({});
	});
});

test('is.asyncIterable', t => {
	t.true(is.asyncIterable({
		[Symbol.asyncIterator]() {},
	}));

	t.false(is.asyncIterable(null));
	t.false(is.asyncIterable(undefined));
	t.false(is.asyncIterable(0));
	t.false(is.asyncIterable(Number.NaN));
	t.false(is.asyncIterable(Number.POSITIVE_INFINITY));
	t.false(is.asyncIterable({}));

	t.notThrows(() => {
		assert.asyncIterable({
			[Symbol.asyncIterator]() {},
		});
	});

	t.throws(() => {
		assert.asyncIterable(null);
	});
	t.throws(() => {
		assert.asyncIterable(undefined);
	});
	t.throws(() => {
		assert.asyncIterable(0);
	});
	t.throws(() => {
		assert.asyncIterable(Number.NaN);
	});
	t.throws(() => {
		assert.asyncIterable(Number.POSITIVE_INFINITY);
	});
	t.throws(() => {
		assert.asyncIterable({});
	});
});

test('is.class', t => {
	class Foo {} // eslint-disable-line @typescript-eslint/no-extraneous-class

	// Note: Using new Function to prevent whitespace modifications in tsimp
	const minifiedClass = new Function('return class{};'); // eslint-disable-line no-new-func

	const classDeclarations = [
		Foo,
		class Bar extends Foo {},
		minifiedClass(),
	];

	for (const classDeclaration of classDeclarations) {
		t.true(is.class(classDeclaration));

		t.notThrows(() => {
			assert.class(classDeclaration);
		});
	}
});

test('is.typedArray', t => {
	const typedArrays: TypedArray[] = [
		new Int8Array(),
		new Uint8Array(),
		new Uint8ClampedArray(),
		new Uint16Array(),
		new Int32Array(),
		new Uint32Array(),
		new Float32Array(),
		new Float64Array(),
		new BigInt64Array(),
		new BigUint64Array(),
	];

	for (const item of typedArrays) {
		t.true(is.typedArray(item));

		t.notThrows(() => {
			assert.typedArray(item);
		});
	}

	t.false(is.typedArray(new ArrayBuffer(1)));
	t.false(is.typedArray([]));
	t.false(is.typedArray({}));

	t.throws(() => {
		assert.typedArray(new ArrayBuffer(1));
	});
	t.throws(() => {
		assert.typedArray([]);
	});
	t.throws(() => {
		assert.typedArray({});
	});
});

test('is.arrayLike', t => {
	(function () {
		t.true(is.arrayLike(arguments)); // eslint-disable-line prefer-rest-params
	})();

	t.true(is.arrayLike([]));
	t.true(is.arrayLike('unicorn'));

	t.false(is.arrayLike({}));
	t.false(is.arrayLike(() => {}));
	t.false(is.arrayLike(new Map()));

	(function () {
		t.notThrows(function () {
			assert.arrayLike(arguments); // eslint-disable-line prefer-rest-params
		});
	})();

	t.notThrows(() => {
		assert.arrayLike([]);
	});
	t.notThrows(() => {
		assert.arrayLike('unicorn');
	});

	t.throws(() => {
		assert.arrayLike({});
	});
	t.throws(() => {
		assert.arrayLike(() => {});
	});
	t.throws(() => {
		assert.arrayLike(new Map());
	});
});

test('is.tupleLike', t => {
	(function () {
		t.false(is.tupleLike(arguments, [])); // eslint-disable-line prefer-rest-params
	})();

	t.true(is.tupleLike([], []));
	t.true(is.tupleLike([1, '2', true, {}, [], undefined, null], [is.number, is.string, is.boolean, is.object, is.array, is.undefined, is.nullOrUndefined]));
	t.false(is.tupleLike('unicorn', [is.string]));

	t.false(is.tupleLike({}, []));
	t.false(is.tupleLike(() => {}, [is.function]));
	t.false(is.tupleLike(new Map(), [is.map]));

	(function () {
		t.throws(function () {
			assert.tupleLike(arguments, []); // eslint-disable-line prefer-rest-params
		});
	})();

	t.notThrows(() => {
		assert.tupleLike([], []);
	});
	t.throws(() => {
		assert.tupleLike('unicorn', [is.string]);
	});

	t.throws(() => {
		assert.tupleLike({}, [is.object]);
	});
	t.throws(() => {
		assert.tupleLike(() => {}, [is.function]);
	});
	t.throws(() => {
		assert.tupleLike(new Map(), [is.map]);
	});

	{
		const tuple = [[false, 'unicorn'], 'string', true];

		if (is.tupleLike(tuple, [is.array, is.string, is.boolean])) {
			if (is.tupleLike(tuple[0], [is.boolean, is.string])) { // eslint-disable-line unicorn/no-lonely-if
				const value = tuple[0][1];
				expectTypeOf(value).toEqualTypeOf<string>();
			}
		}
	}

	{
		const tuple = [{isTest: true}, '1', true, null];

		if (is.tupleLike(tuple, [is.nonEmptyObject, is.string, is.boolean, is.null])) {
			const value = tuple[0];
			expectTypeOf(value).toEqualTypeOf<Record<string | number | symbol, unknown>>();
		}
	}

	{
		const tuple = [1, '1', true, null, undefined];

		if (is.tupleLike(tuple, [is.number, is.string, is.boolean, is.undefined, is.null])) {
			const numericValue = tuple[0];
			const stringValue = tuple[1];
			const booleanValue = tuple[2];
			const undefinedValue = tuple[3];
			const nullValue = tuple[4];
			expectTypeOf(numericValue).toEqualTypeOf<number>();
			expectTypeOf(stringValue).toEqualTypeOf<string>();
			expectTypeOf(booleanValue).toEqualTypeOf<boolean>();
			expectTypeOf(undefinedValue).toEqualTypeOf<undefined>();
			// eslint-disable-next-line @typescript-eslint/ban-types
			expectTypeOf(nullValue).toEqualTypeOf<null>();
		}
	}
});

test('is.inRange', t => {
	const x = 3;

	t.true(is.inRange(x, [0, 5]));
	t.true(is.inRange(x, [5, 0]));
	t.true(is.inRange(x, [-5, 5]));
	t.true(is.inRange(x, [5, -5]));
	t.false(is.inRange(x, [4, 8]));
	t.true(is.inRange(-7, [-5, -10]));
	t.true(is.inRange(-5, [-5, -10]));
	t.true(is.inRange(-10, [-5, -10]));

	t.true(is.inRange(x, 10));
	t.true(is.inRange(0, 0));
	t.true(is.inRange(-2, -3));
	t.false(is.inRange(x, 2));
	t.false(is.inRange(-3, -2));

	t.throws(() => {
		// @ts-expect-error invalid argument
		is.inRange(0, []);
	});

	t.throws(() => {
		// @ts-expect-error invalid argument
		is.inRange(0, [5]);
	});

	t.throws(() => {
		// @ts-expect-error invalid argument
		is.inRange(0, [1, 2, 3]);
	});

	t.notThrows(() => {
		assert.inRange(x, [0, 5]);
	});

	t.notThrows(() => {
		assert.inRange(x, [5, 0]);
	});

	t.notThrows(() => {
		assert.inRange(x, [-5, 5]);
	});

	t.notThrows(() => {
		assert.inRange(x, [5, -5]);
	});

	t.throws(() => {
		assert.inRange(x, [4, 8]);
	});

	t.notThrows(() => {
		assert.inRange(-7, [-5, -10]);
	});

	t.notThrows(() => {
		assert.inRange(-5, [-5, -10]);
	});

	t.notThrows(() => {
		assert.inRange(-10, [-5, -10]);
	});

	t.notThrows(() => {
		assert.inRange(x, 10);
	});

	t.notThrows(() => {
		assert.inRange(0, 0);
	});

	t.notThrows(() => {
		assert.inRange(-2, -3);
	});

	t.throws(() => {
		assert.inRange(x, 2);
	});

	t.throws(() => {
		assert.inRange(-3, -2);
	});

	t.throws(() => {
		// @ts-expect-error invalid argument
		assert.inRange(0, []);
	});

	t.throws(() => {
		// @ts-expect-error invalid argument
		assert.inRange(0, [5]);
	});

	t.throws(() => {
		// @ts-expect-error invalid argument
		assert.inRange(0, [1, 2, 3]);
	});
});

test('is.htmlElement supplemental', t => {
	t.false(is.htmlElement({nodeType: 1, nodeName: 'div'}));
	t.throws(() => {
		assert.htmlElement({nodeType: 1, nodeName: 'div'});
	});

	const tagNames = [
		'div',
		'input',
		'span',
		'img',
		'canvas',
		'script',
	] as const;

	for (const tagName of tagNames) {
		const element = document.createElement(tagName);
		t.is(is(element), 'HTMLElement');
	}

	const nonHtmlElements = [
		document.createTextNode('data'),
		document.createProcessingInstruction('xml-stylesheet', 'href="mycss.css" type="text/css"'),
		document.createComment('This is a comment'),
		document,
		document.implementation.createDocumentType('svg:svg', '-//W3C//DTD SVG 1.1//EN', 'https://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'),
		document.createDocumentFragment(),
	] as const;

	for (const element of nonHtmlElements) {
		t.throws(() => {
			assert.htmlElement(element);
		});
	}
});

test('is.evenInteger', t => {
	for (const element of [-6, 2, 4]) {
		t.true(is.evenInteger(element));
		t.notThrows(() => {
			assert.evenInteger(element);
		});
	}

	for (const element of [-3, 1, 5]) {
		t.false(is.evenInteger(element));
		t.throws(() => {
			assert.evenInteger(element);
		});
	}
});

test('is.oddInteger', t => {
	for (const element of [-5, 7, 13]) {
		t.true(is.oddInteger(element));
		t.notThrows(() => {
			assert.oddInteger(element);
		});
	}

	for (const element of [-8, 8, 10]) {
		t.false(is.oddInteger(element));
		t.throws(() => {
			assert.oddInteger(element);
		});
	}
});

test('is.nonEmptyArray', t => {
	t.true(is.nonEmptyArray([1, 2, 3]));
	t.false(is.nonEmptyArray([]));
	t.false(is.nonEmptyArray(new Array())); // eslint-disable-line @typescript-eslint/no-array-constructor

	t.notThrows(() => {
		assert.nonEmptyArray([1, 2, 3]);
	});
	t.throws(() => {
		assert.nonEmptyArray([]);
	});
	t.throws(() => {
		assert.nonEmptyArray(new Array()); // eslint-disable-line @typescript-eslint/no-array-constructor
	});

	{
		const strings = ['🦄', 'unicorn'] as string[] | undefined;
		const function_ = (value: string) => value;

		if (is.nonEmptyArray(strings)) {
			const value = strings[0];
			function_(value);
		}
	}

	{
		const mixed = ['🦄', 'unicorn', 1, 2];
		const function_ = (value: string | number) => value;

		if (is.nonEmptyArray(mixed)) {
			const value = mixed[0];
			function_(value);
		}
	}

	{
		const arrays = [['🦄'], ['unicorn']];
		const function_ = (value: string[]) => value;

		if (is.nonEmptyArray(arrays)) {
			const value = arrays[0];
			function_(value);
		}
	}

	{
		const strings = ['🦄', 'unicorn'] as string[] | undefined;
		const function_ = (value: string) => value;

		assert.nonEmptyArray(strings);

		const value = strings[0];
		function_(value);
	}

	{
		const mixed = ['🦄', 'unicorn', 1, 2];
		const function_ = (value: string | number) => value;

		assert.nonEmptyArray(mixed);

		const value = mixed[0];
		function_(value);
	}

	{
		const arrays = [['🦄'], ['unicorn']];
		const function_ = (value: string[]) => value;

		assert.nonEmptyArray(arrays);

		const value = arrays[0];
		function_(value);
	}
});

test('is.emptyString supplemental', t => {
	t.false(is.emptyString('🦄'));
	t.throws(() => {
		assert.emptyString('🦄');
	});
});

test('is.emptyStringOrWhitespace supplemental', t => {
	t.true(is.emptyStringOrWhitespace('  '));
	t.false(is.emptyStringOrWhitespace('🦄'));
	t.false(is.emptyStringOrWhitespace('unicorn'));

	t.notThrows(() => {
		assert.emptyStringOrWhitespace('  ');
	});
	t.throws(() => {
		assert.emptyStringOrWhitespace('🦄');
	});
	t.throws(() => {
		assert.emptyStringOrWhitespace('unicorn');
	});

	let value = 'test'; // eslint-disable-line prefer-const -- can't use `const` here because then it will be inferred as `never` in the `if` block
	if (is.emptyStringOrWhitespace(value)) {
		value.charAt(0); // Should be inferred as `'' | Whitespace` and not `never`
	} else {
		value.charAt(0); // Should be inferred as `string` and not `never`
	}
});

test('is.nonEmptyString', t => {
	t.false(is.nonEmptyString(''));
	t.false(is.nonEmptyString(String()));
	t.true(is.nonEmptyString('🦄'));

	t.throws(() => {
		assert.nonEmptyString('');
	});
	t.throws(() => {
		assert.nonEmptyString(String());
	});
	t.notThrows(() => {
		assert.nonEmptyString('🦄');
	});
});

test('is.nonEmptyStringAndNotWhitespace', t => {
	t.false(is.nonEmptyStringAndNotWhitespace(' '));
	t.true(is.nonEmptyStringAndNotWhitespace('🦄'));

	for (const value of [null, undefined, 5, Number.NaN, {}, []]) {
		t.false(is.nonEmptyStringAndNotWhitespace(value));

		t.throws(() => {
			assert.nonEmptyStringAndNotWhitespace(value);
		});
	}

	t.throws(() => {
		assert.nonEmptyStringAndNotWhitespace('');
	});

	t.notThrows(() => {
		assert.nonEmptyStringAndNotWhitespace('🦄');
	});
});

test('is.emptyObject', t => {
	t.true(is.emptyObject({}));
	t.true(is.emptyObject(new Object())); // eslint-disable-line no-object-constructor
	t.false(is.emptyObject({unicorn: '🦄'}));

	t.notThrows(() => {
		assert.emptyObject({});
	});
	t.notThrows(() => {
		assert.emptyObject(new Object()); // eslint-disable-line no-object-constructor
	});
	t.throws(() => {
		assert.emptyObject({unicorn: '🦄'});
	});
});

test('is.nonEmptyObject', t => {
	const foo = {};
	is.nonEmptyObject(foo);

	t.false(is.nonEmptyObject({}));
	t.false(is.nonEmptyObject(new Object())); // eslint-disable-line no-object-constructor
	t.true(is.nonEmptyObject({unicorn: '🦄'}));

	t.throws(() => {
		assert.nonEmptyObject({});
	});
	t.throws(() => {
		assert.nonEmptyObject(new Object()); // eslint-disable-line no-object-constructor
	});
	t.notThrows(() => {
		assert.nonEmptyObject({unicorn: '🦄'});
	});
});

test('is.nonEmptySet', t => {
	const temporarySet = new Set();
	t.false(is.nonEmptySet(temporarySet));
	t.throws(() => {
		assert.nonEmptySet(temporarySet);
	});

	temporarySet.add(1);
	t.true(is.nonEmptySet(temporarySet));
	t.notThrows(() => {
		assert.nonEmptySet(temporarySet);
	});
});

test('is.nonEmptyMap', t => {
	const temporaryMap = new Map();
	t.false(is.nonEmptyMap(temporaryMap));
	t.throws(() => {
		assert.nonEmptyMap(temporaryMap);
	});

	temporaryMap.set('unicorn', '🦄');
	t.true(is.nonEmptyMap(temporaryMap));
	t.notThrows(() => {
		assert.nonEmptyMap(temporaryMap);
	});
});

test('is.propertyKey', t => {
	t.true(is.propertyKey('key'));
	t.true(is.propertyKey(42));
	t.true(is.propertyKey(Symbol('')));

	t.false(is.propertyKey(null));
	t.false(is.propertyKey(undefined));
	t.false(is.propertyKey(true));
	t.false(is.propertyKey({}));
	t.false(is.propertyKey([]));
	t.false(is.propertyKey(new Map()));
	t.false(is.propertyKey(new Set()));
});

test('is.any', t => {
	t.true(is.any(is.string, {}, true, '🦄'));
	t.true(is.any(is.object, false, {}, 'unicorns'));
	t.false(is.any(is.boolean, '🦄', [], 3));
	t.false(is.any(is.integer, true, 'lol', {}));
	t.true(is.any([is.string, is.number], {}, true, '🦄'));
	t.false(is.any([is.boolean, is.number], 'unicorns', [], new Map()));
	t.is(typeof is.any([is.string, is.number]), 'function');

	t.throws(() => {
		// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
		is.any(null as any, true);
	});

	t.throws(() => {
		is.any([], 'value');
	});

	t.throws(() => {
		is.any(is.string);
	});

	t.notThrows(() => {
		assert.any(is.string, {}, true, '🦄');
	});

	t.notThrows(() => {
		assert.any(is.object, false, {}, 'unicorns');
	});

	t.throws(() => {
		assert.any([is.string, is.number]);
	});

	t.throws(() => {
		assert.any(is.boolean, '🦄', [], 3);
	});

	t.throws(() => {
		assert.any(is.integer, true, 'lol', {});
	});

	t.throws(() => {
		// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
		assert.any(null as any, true);
	});

	t.throws(() => {
		assert.any([], 'value');
	});

	t.throws(() => {
		assert.any(is.string);
	});

	t.throws(() => {
		assert.any(is.string, 1, 2, 3);
	}, {
		// Includes expected type and removes duplicates from received types:
		message: /Expected values which are `string`. Received values of type `number`./,
	});

	t.throws(() => {
		assert.any(is.string, 1, [4]);
	}, {
		// Includes expected type and lists all received types:
		message: /Expected values which are `string`. Received values of types `number` and `Array`./,
	});

	t.throws(() => {
		assert.any([is.string, is.nullOrUndefined], 1);
	}, {
		// Handles array as first argument:
		message: /Expected values which are `string` or `null or undefined`. Received values of type `number`./,
	});

	t.throws(() => {
		assert.any([is.string, is.number, is.boolean], null, undefined, Number.NaN);
	}, {
		// Handles more than 2 expected and received types:
		message: /Expected values which are `string`, `number`, or `boolean`. Received values of types `null`, `undefined`, and `NaN`./,
	});

	t.throws(() => {
		assert.any(() => false, 1);
	}, {
		// Default type assertion message
		message: /Expected values which are `predicate returns truthy for any value`./,
	});
});

test('is.all', t => {
	t.true(is.all(is.object, {}, new Set(), new Map()));
	t.true(is.all(is.boolean, true, false));
	t.false(is.all(is.string, '🦄', []));
	t.false(is.all(is.set, new Map(), {}));

	t.true(is.all(is.array, ['1'], ['2']));
	t.true(is.all([is.string, is.nonEmptyString], '🦄', 'unicorns'));
	t.false(is.all([is.string, is.number], '🦄'));

	t.throws(() => {
		// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
		is.all(null as any, true);
	});

	t.throws(() => {
		is.all([], 'value');
	});

	t.throws(() => {
		is.all(is.string);
	});

	t.notThrows(() => {
		assert.all(is.object, {}, new Set(), new Map());
	});

	t.notThrows(() => {
		assert.all(is.boolean, true, false);
	});

	t.throws(() => {
		assert.all([is.string, is.number]);
	});

	t.notThrows(() => {
		assert.all([is.string, is.nonEmptyString], '🦄', 'unicorns');
	});

	t.throws(() => {
		assert.all(is.string, '🦄', []);
	});

	t.throws(() => {
		assert.all([is.string, is.number], '🦄');
	});

	t.throws(() => {
		assert.all(is.set, new Map(), {});
	});

	t.throws(() => {
		// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
		assert.all(null as any, true);
	});

	t.throws(() => {
		assert.all([], 'value');
	});

	t.throws(() => {
		assert.all(is.string);
	});

	t.throws(() => {
		assert.all(is.string, 1, 2, 3);
	}, {
		// Includes expected type and removes duplicates from received types:
		message: /Expected values which are `string`. Received values of type `number`./,
	});

	t.throws(() => {
		assert.all(is.string, 1, [4]);
	}, {
		// Includes expected type and lists all received types:
		message: /Expected values which are `string`. Received values of types `number` and `Array`./,
	});

	t.throws(() => {
		assert.all(() => false, 1);
	}, {
		// Default type assertion message
		message: /Expected values which are `predicate returns truthy for all values`./,
	});
});

test('is.any as predicate factory', t => {
	// Returns a type guard function when called with only predicates
	const isStringOrNumber = is.any([is.string, is.number]);
	t.is(typeof isStringOrNumber, 'function');
	t.true(isStringOrNumber('hello'));
	t.true(isStringOrNumber(123));
	t.false(isStringOrNumber(true));
	t.false(isStringOrNumber({}));

	// Type narrowing works correctly
	const value: unknown = 'test';
	if (isStringOrNumber(value)) {
		// TypeScript should narrow to string | number
		const narrowed: string | number = value;
		t.pass(`narrowed to: ${typeof narrowed}`);
	}

	// Works with is.optional
	t.true(is.optional(undefined, is.any([is.string, is.number])));
	t.true(is.optional('test', is.any([is.string, is.number])));
	t.true(is.optional(42, is.any([is.string, is.number])));
	t.false(is.optional(true, is.any([is.string, is.number])));

	const predicateArray: Predicate[] = [is.string, is.number];
	const isStringOrNumberFromArray = is.any(predicateArray);
	t.is(typeof isStringOrNumberFromArray, 'function');
	t.true(isStringOrNumberFromArray('hello'));
	t.true(isStringOrNumberFromArray(123));
	t.false(isStringOrNumberFromArray(true));

	// Type narrowing with is.optional
	const optionalValue: unknown = undefined;
	if (is.optional(optionalValue, is.any([is.string, is.number]))) {
		// TypeScript should narrow to string | number | undefined
		const narrowed: string | number | undefined = optionalValue;
		t.pass(`optional narrowed to: ${typeof narrowed}`);
	}

	// Works with more predicates
	const isStringOrNumberOrBoolean = is.any([is.string, is.number, is.boolean]);
	t.true(isStringOrNumberOrBoolean('hello'));
	t.true(isStringOrNumberOrBoolean(123));
	t.true(isStringOrNumberOrBoolean(true));
	t.false(isStringOrNumberOrBoolean({}));

	t.throws(() => {
		// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
		is.any([is.string, 123 as any]);
	});
});

test('is.all as predicate factory', t => {
	// Returns a type guard function when called with only predicates
	const isArrayAndNonEmpty = is.all([is.array, is.nonEmptyArray]);
	t.is(typeof isArrayAndNonEmpty, 'function');
	t.true(isArrayAndNonEmpty(['hello']));
	t.false(isArrayAndNonEmpty([]));
	t.false(isArrayAndNonEmpty('hello'));

	// Type narrowing works correctly
	const value: unknown = ['test'];
	if (isArrayAndNonEmpty(value)) {
		// TypeScript should narrow to the intersection type
		t.true(Array.isArray(value));
		t.true(value.length > 0);
	}

	// Works with is.optional
	t.true(is.optional(undefined, is.all([is.object, is.plainObject])));
	t.true(is.optional({foo: 'bar'}, is.all([is.object, is.plainObject])));
	t.false(is.optional([], is.all([is.object, is.plainObject])));

	t.throws(() => {
		// eslint-disable-next-line @typescript-eslint/no-unsafe-argument
		is.all([is.string, 123 as any]);
	});
});

test('is.formData supplemental', t => {
	const data = new window.FormData();
	t.true(is.formData(data));
	t.false(is.formData({}));
	t.false(is.formData(undefined));
	t.false(is.formData(null));

	t.notThrows(() => {
		assert.formData(data);
	});
	t.throws(() => {
		assert.formData({});
	});
	t.throws(() => {
		assert.formData(undefined);
	});
	t.throws(() => {
		assert.formData(null);
	});
});

test('is.urlSearchParams', t => {
	const searchParameters = new URLSearchParams();
	t.true(is.urlSearchParams(searchParameters));
	t.false(is.urlSearchParams({}));
	t.false(is.urlSearchParams(undefined));
	t.false(is.urlSearchParams(null));

	t.notThrows(() => {
		assert.urlSearchParams(searchParameters);
	});
	t.throws(() => {
		assert.urlSearchParams({});
	});
	t.throws(() => {
		assert.urlSearchParams(undefined);
	});
	t.throws(() => {
		assert.urlSearchParams(null);
	});
});

test('is.validDate', t => {
	t.true(is.validDate(new Date()));
	t.false(is.validDate(new Date('x')));
	t.notThrows(() => {
		assert.validDate(new Date());
	});
	t.throws(() => {
		assert.validDate(new Date('x'));
	});
});

test('is.validLength', t => {
	t.true(is.validLength(1));
	t.true(is.validLength(0));
	t.false(is.validLength(-1));
	t.false(is.validLength(0.1));
	t.notThrows(() => {
		assert.validLength(1);
	});
	t.throws(() => {
		assert.validLength(-1);
	});
});

test('is.whitespaceString', t => {
	t.true(is.whitespaceString(' '));
	t.true(is.whitespaceString('   '));
	t.true(is.whitespaceString(' 　 '));
	t.true(is.whitespaceString('\u3000'));
	t.true(is.whitespaceString('　'));
	t.false(is.whitespaceString(''));
	t.false(is.whitespaceString('-'));
	t.false(is.whitespaceString(' hi '));
});

test('assert', t => {
	// Contrived test showing that TypeScript acknowledges the type assertion in `assert.number()`.
	// Real--world usage includes asserting user input, but here we use a random number/string generator.
	t.plan(2);

	const getNumberOrStringRandomly = (): number | string => {
		const random = Math.random();

		if (random < 0.5) {
			return 'sometimes this function returns text';
		}

		return random;
	};

	const canUseOnlyNumber = (badlyTypedArgument: any): number => {
		// Narrow the type to number, or throw an error at runtime for non-numbers.
		assert.number(badlyTypedArgument);

		// Both the type and runtime value is number.
		return 1000 * badlyTypedArgument;
	};

	const badlyTypedVariable: any = getNumberOrStringRandomly();

	t.true(is.number(badlyTypedVariable) || is.string(badlyTypedVariable));

	// Using try/catch for test purposes only.
	try {
		const result = canUseOnlyNumber(badlyTypedVariable);

		// Got lucky, the input was a number yielding a good result.
		t.true(is.number(result));
	} catch {
		// Assertion was tripped.
		t.true(is.string(badlyTypedVariable));
	}
});

test('custom assertion message', t => {
	const message = 'Custom error message';

	t.throws(() => {
		assert.array(undefined, undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.arrayBuffer(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.arrayLike(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.asyncFunction(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.asyncGenerator(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.asyncGeneratorFunction(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.asyncIterable(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.bigInt64Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.bigUint64Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.bigint(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.blob(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.boolean(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.boundFunction(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.buffer(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.class(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.dataView(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.date(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.directInstanceOf(undefined, Error, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.emptyArray(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.emptyMap(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.emptyObject(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.emptySet(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.emptyString(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.emptyStringOrWhitespace(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		enum Enum {}
		assert.enumCase('invalid', Enum, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.error(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.evenInteger(33, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.falsy(true, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.float32Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.float64Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.formData(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.function(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.generator(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.generatorFunction(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.htmlElement(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.inRange(5, [1, 2], message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.infinite(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.int16Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.int32Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.int8Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.integer(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.iterable(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.map(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nan(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nativePromise(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.negativeNumber(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nodeStream(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nonEmptyArray(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nonEmptyMap(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nonEmptyObject(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nonEmptySet(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nonEmptyString(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nonEmptyStringAndNotWhitespace(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.null(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.nullOrUndefined(false, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.number(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.numericString(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.object(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.observable(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.oddInteger(42, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.plainObject(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.positiveNumber(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.primitive([], message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.promise(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.propertyKey(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.regExp(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.safeInteger(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.set(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.sharedArrayBuffer(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.string(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.symbol(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.truthy(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.tupleLike(undefined, [], message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.typedArray(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.uint16Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.uint32Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.uint8Array(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.uint8ClampedArray(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.undefined(false, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.urlInstance(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.urlSearchParams(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.urlString(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.validDate(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.validLength(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.weakMap(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.weakRef(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.weakSet(undefined, message);
	}, {instanceOf: TypeError, message});

	t.throws(() => {
		assert.whitespaceString(undefined, message);
	}, {instanceOf: TypeError, message});
});

test('is.optional', t => {
	t.true(is.optional(undefined, is.string));
	t.true(is.optional('🦄', is.string));
	t.false(is.optional(123, is.string));
	t.false(is.optional(null, is.string));
});

test('assert.optional', t => {
	t.notThrows(() => {
		assert.optional(undefined, assert.string);
	});

	t.notThrows(() => {
		assert.optional('🦄', assert.string);
	});

	t.throws(() => {
		assert.optional(123, assert.string);
	});

	t.throws(() => {
		assert.optional(null, assert.string);
	});
});
```

