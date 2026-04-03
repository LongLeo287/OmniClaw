---
id: github.com-isaacs-node-lru-cache-980f3c84-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:09.243445
---

# KNOWLEDGE EXTRACT: github.com_isaacs_node-lru-cache_980f3c84
> **Extracted on:** 2026-04-01 16:13:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524977/github.com_isaacs_node-lru-cache_980f3c84

---

## File: `.gitignore`
```
/.tap
/node_modules
/dist
/docs
```

## File: `.prettierignore`
```
/node_modules
/tsconfig.json
/package-lock.json
/package.json
/LICENSE.md
/example
/.github
/dist
/.env
/tap-snapshots
/.nyc_output
/coverage
/benchmark
/.tap
/test/fixture
/test/fixtures
/.tshy
/docs
```

## File: `.prettierrc.json`
```json
{
  "experimentalTernaries": true,
  "semi": false,
  "printWidth": 75,
  "tabWidth": 2,
  "useTabs": false,
  "singleQuote": true,
  "jsxSingleQuote": false,
  "bracketSameLine": true,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

## File: `.taprc`
```
# vim: set filetype=yaml :
node-arg:
  - "--expose-gc"
plugin:
  - "@tapjs/clock"
```

## File: `CHANGELOG.md`
```markdown
# cringe lorg

## 11.2

- Add the `perf` option to specify `performance`, `Date`, or any
  other object with a `now()` method that returns a number.

## 11.1

- Add the `onInsert` method

## 11.0

- Drop support for node less than v20

## 10.4

- Accidental minor update, should've been patch.

## 10.3

- add `forceFetch()` method
- set `disposeReason` to `'expire'` when it's the result of a TTL
  expiration, or `'fetch'` when it's the result of an aborted
  or `undefined`-returning `fetch()`
- add `memo()` method

## 10.2

- types: implement the `Map<K, V>` interface

## 10.1

- add `cache.info(key)` to get value as well as ttl and size
  information.

## 10.0

- `cache.fetch()` return type is now `Promise<V | undefined>`
  instead of `Promise<V | void>`. This is an irrelevant change
  practically speaking, but can require changes for TypeScript
  users.

## 9.1

- `cache.set(key, undefined)` is now an alias for
  `cache.delete(key)`

## 9.0

- Use named export only, no default export.
- Bring back minimal polyfill. If this polyfill ends up being
  used, then a warning is printed, as it is not safe for use
  outside of LRUCache.

## 8.0

- The `fetchContext` option was renamed to `context`, and may no
  longer be set on the cache instance itself.
- Rewritten in TypeScript, so pretty much all the types moved
  around a lot.
- The AbortController/AbortSignal polyfill is removed. For this
  reason, **Node version 16.14.0 or higher is now required**.
- Internal properties were moved to actual private class
  properties.
- Keys and values must not be `null` or `undefined`.
- Minified export available at `'lru-cache/min'`, for both CJS
  and MJS builds.

## 7.18

- Add support for internal state investigation through the use of
  a `status` option to `has()`, `set()`, `get()`, and `fetch()`.

## 7.17

- Add `signal` option for `fetch` to pass a user-supplied
  AbortSignal
- Add `ignoreFetchAbort` and `allowStaleOnFetchAbort` options

## 7.16.2

- Fail fetch() promises when they are aborted

## 7.16

- Add `allowStaleOnFetchRejection` option

## 7.15

- Provide both ESM and CommonJS exports

## 7.14

- Add `maxEntrySize` option to prevent caching items above a
  given calculated size.

## 7.13

- Add `forceRefresh` option to trigger a call to the
  `fetchMethod` even if the item is found in cache, and not
  older than its `ttl`.

## 7.12

- Add `fetchContext` option to provide additional information to
  the `fetchMethod`
- 7.12.1: Fix bug where adding an item with size greater than
  `maxSize` would cause bizarre behavior.

## 7.11

- Add 'noDeleteOnStaleGet' option, to suppress behavior where a
  `get()` of a stale item would remove it from the cache.

## 7.10

- Add `noDeleteOnFetchRejection` option, to suppress behavior
  where a failed `fetch` will delete a previous stale value.
- Ship types along with the package, rather than relying on
  out of date types coming from DefinitelyTyped.

## 7.9

- Better AbortController polyfill, supporting
  `signal.addEventListener('abort')` and `signal.onabort`.
- (7.9.1) Drop item from cache instead of crashing with an
  `unhandledRejection` when the `fetchMethod` throws an error or
  returns a rejected Promise.

## 7.8

- add `updateAgeOnHas` option
- warnings sent to `console.error` if `process.emitWarning` unavailable

## 7.7

- fetch: provide options and abort signal

## 7.6

- add cache.getRemainingTTL(key)
- Add async cache.fetch() method, fetchMethod option
- Allow unbounded storage if maxSize or ttl set

## 7.5

- defend against mutation while iterating
- Add rentries, rkeys, rvalues
- remove bundler and unnecessary package.json fields

## 7.4

- Add browser optimized webpack bundle, exposed as `'lru-cache/browser'`
- Track size of compiled bundle in CI ([@SuperOleg39](https://github.com/SuperOleg39))
- Add `noUpdateTTL` option for `set()`

## 7.3

- Add `disposeAfter()`
- `set()` returns the cache object
- `delete()` returns boolean indicating whether anything was deleted

## 7.2

- Add reason to dispose() calls.

## 7.1

- Add `ttlResolution` option
- Add `ttlAutopurge` option

## 7.0 - 2022-02

This library changed to a different algorithm and internal data structure
in version 7, yielding significantly better performance, albeit with
some subtle changes as a result.

If you were relying on the internals of LRUCache in version 6 or before, it
probably will not work in version 7 and above.

### Specific API Changes

For the most part, the feature set has been maintained as much as possible.

However, some other cleanup and refactoring changes were made in v7 as
well.

- The `set()`, `get()`, and `has()` functions take options objects
  instead of positional booleans/integers for optional parameters.
- `size` can be set explicitly on `set()`.
- `cache.length` was renamed to the more fitting `cache.size`.
- Deprecations:
  - `stale` option -> `allowStale`
  - `maxAge` option -> `ttl`
  - `length` option -> `sizeCalculation`
  - `length` property -> `size`
  - `del()` method -> `delete()`
  - `prune()` method -> `purgeStale()`
  - `reset()` method -> `clear()`
- The objects used by `cache.load()` and `cache.dump()` are incompatible
  with previous versions.
- `max` and `maxSize` are now two separate options. (Previously, they were
  a single `max` option, which would be based on either count or computed
  size.)
- The function assigned to the `dispose` option is now expected to have signature
  `(value, key, reason)` rather than `(key, value)`, reversing the order of
  `value` and `key`.

## v6 - 2020-07

- Drop support for node v8 and earlier

## v5 - 2018-11

- Add updateAgeOnGet option
- Guards around setting max/maxAge to non-numbers
- Use classes, drop support for old nodes

## v4 - 2015-12

- Improve performance
- add noDisposeOnSet option
- feat(prune): allow users to proactively prune old entries
- Use Symbols for private members
- Add maxAge setter/getter

## v3 - 2015-11

- Add cache.rforEach
- Allow non-string keys

## v2 - 2012-08

- add cache.pop()
- add cache.peek()
- add cache.keys()
- add cache.values()
- fix memory leak
- add `stale` option to return stale values before deleting
- use null-prototype object to avoid hazards
- make options argument an object

## v1 - 2010-05

- initial implementation
```

## File: `CONTRIBUTING.md`
```markdown
Please consider signing [the neveragain.tech pledge](http://neveragain.tech/)
```

## File: `CONTRIBUTORS`
```
# Authors, sorted by whether or not they are me
Isaac Z. Schlueter <i@izs.me>
Brian Cottingham <spiffytech@gmail.com>
Carlos Brito Lage <carlos@carloslage.net>
Jesse Dailey <jesse.dailey@gmail.com>
Kevin O'Hara <kevinohara80@gmail.com>
Marco Rogers <marco.rogers@gmail.com>
Mark Cavage <mcavage@gmail.com>
Marko Mikulicic <marko.mikulicic@isti.cnr.it>
Nathan Rajlich <nathan@tootallnate.net>
Satheesh Natesan <snateshan@myspace-inc.com>
Trent Mick <trentm@gmail.com>
ashleybrener <ashley@starlogik.com>
n4kz <n4kz@n4kz.com>
```

## File: `LICENSE.md`
```markdown
# Blue Oak Model License

Version 1.0.0

## Purpose

This license gives everyone as much permission to work with
this software as possible, while protecting contributors
from liability.

## Acceptance

In order to receive this license, you must agree to its
rules.  The rules of this license are both obligations
under that agreement and conditions to your license.
You must not do anything with this software that triggers
a rule that you cannot or will not follow.

## Copyright

Each contributor licenses you to do everything with this
software that would otherwise infringe that contributor's
copyright in it.

## Notices

You must ensure that everyone who gets a copy of
any part of this software from you, with or without
changes, also gets the text of this license or a link to
<https://blueoakcouncil.org/license/1.0.0>.

## Excuse

If anyone notifies you in writing that you have not
complied with [Notices](#notices), you can keep your
license by taking all practical steps to comply within 30
days after the notice.  If you do not do so, your license
ends immediately.

## Patent

Each contributor licenses you to do everything with this
software that would otherwise infringe any patent claims
they can license or become able to license.

## Reliability

No contributor can revoke this license.

## No Liability

***As far as the law allows, this software comes as is,
without any warranty or condition, and no contributor
will be liable to anyone for any damages related to this
software or this license, under any kind of legal claim.***
```

## File: `README.md`
```markdown
# lru-cache

A cache object that deletes the least-recently-used items.

Specify a max number of the most recently used items that you
want to keep, and this cache will keep that many of the most
recently accessed items.

This is not primarily a TTL cache, and does not make strong TTL
guarantees. There is no preemptive pruning of expired items by
default, but you _may_ set a TTL on the cache or on a single
`set`. If you do so, it will treat expired items as missing, and
delete them when fetched. If you are more interested in TTL
caching than LRU caching, check out
[@isaacs/ttlcache](http://npm.im/@isaacs/ttlcache).

As of version 7, this is one of the most performant LRU
implementations available in JavaScript, and supports a wide
diversity of use cases. However, note that using some of the
features will necessarily impact performance, by causing the
cache to have to do more work. See the "Performance" section
below.

## Installation

```bash
npm install lru-cache --save
```

## Usage

```js
// hybrid module, either works
import { LRUCache } from 'lru-cache'
// or:
const { LRUCache } = require('lru-cache')
// or in minified form for web browsers:
import { LRUCache } from 'http://unpkg.com/lru-cache@9/dist/mjs/index.min.mjs'

// At least one of 'max', 'ttl', or 'maxSize' is required, to prevent
// unsafe unbounded storage.
//
// In most cases, it's best to specify a max for performance, so all
// the required memory allocation is done up-front.
//
// All the other options are optional, see the sections below for
// documentation on what each one does.  Most of them can be
// overridden for specific items in get()/set()
const options = {
  max: 500,

  // for use with tracking overall storage size
  maxSize: 5000,
  sizeCalculation: (value, key) => {
    return 1
  },

  // for use when you need to clean up something when objects
  // are evicted from the cache
  dispose: (value, key, reason) => {
    freeFromMemoryOrWhatever(value)
  },

  // for use when you need to know that an item is being inserted
  // note that this does NOT allow you to prevent the insertion,
  // it just allows you to know about it.
  onInsert: (value, key, reason) => {
    logInsertionOrWhatever(key, value)
  },

  // how long to live in ms
  ttl: 1000 * 60 * 5,

  // return stale items before removing from cache?
  allowStale: false,

  updateAgeOnGet: false,
  updateAgeOnHas: false,

  // async method to use for cache.fetch(), for
  // stale-while-revalidate type of behavior
  fetchMethod: async (key, staleValue, { options, signal, context }) => {},
}

const cache = new LRUCache(options)

cache.set('key', 'value')
cache.get('key') // "value"

// non-string keys ARE fully supported
// but note that it must be THE SAME object, not
// just a JSON-equivalent object.
var someObject = { a: 1 }
cache.set(someObject, 'a value')
// Object keys are not toString()-ed
cache.set('[object Object]', 'a different value')
assert.equal(cache.get(someObject), 'a value')
// A similar object with same keys/values won't work,
// because it's a different object identity
assert.equal(cache.get({ a: 1 }), undefined)

cache.clear() // empty the cache
```

If you put more stuff in the cache, then less recently used items
will fall out. That's what an LRU cache is.

For full description of the API and all options, please see [the
LRUCache typedocs](https://isaacs.github.io/node-lru-cache/)

## Storage Bounds Safety

This implementation aims to be as flexible as possible, within
the limits of safe memory consumption and optimal performance.

At initial object creation, storage is allocated for `max` items.
If `max` is set to zero, then some performance is lost, and item
count is unbounded. Either `maxSize` or `ttl` _must_ be set if
`max` is not specified.

If `maxSize` is set, then this creates a safe limit on the
maximum storage consumed, but without the performance benefits of
pre-allocation. When `maxSize` is set, every item _must_ provide
a size, either via the `sizeCalculation` method provided to the
constructor, or via a `size` or `sizeCalculation` option provided
to `cache.set()`. The size of every item _must_ be a positive
integer.

If neither `max` nor `maxSize` are set, then `ttl` tracking must
be enabled. Note that, even when tracking item `ttl`, items are
_not_ preemptively deleted when they become stale, unless
`ttlAutopurge` is enabled. Instead, they are only purged the
next time the key is requested. Thus, if `ttlAutopurge`, `max`,
and `maxSize` are all not set, then the cache will potentially
grow unbounded.

In this case, a warning is printed to standard error. Future
versions may require the use of `ttlAutopurge` if `max` and
`maxSize` are not specified.

If you truly wish to use a cache that is bound _only_ by TTL
expiration, consider using a `Map` object, and calling
`setTimeout` to delete entries when they expire. It will perform
much better than an LRU cache.

Here is an implementation you may use, under the same
[license](./LICENSE) as this package:

```js
// a storage-unbounded ttl cache that is not an lru-cache
const cache = {
  data: new Map(),
  timers: new Map(),
  set: (k, v, ttl) => {
    if (cache.timers.has(k)) {
      clearTimeout(cache.timers.get(k))
    }
    cache.timers.set(
      k,
      setTimeout(() => cache.delete(k), ttl),
    )
    cache.data.set(k, v)
  },
  get: k => cache.data.get(k),
  has: k => cache.data.has(k),
  delete: k => {
    if (cache.timers.has(k)) {
      clearTimeout(cache.timers.get(k))
    }
    cache.timers.delete(k)
    return cache.data.delete(k)
  },
  clear: () => {
    cache.data.clear()
    for (const v of cache.timers.values()) {
      clearTimeout(v)
    }
    cache.timers.clear()
  },
}
```

If that isn't to your liking, check out
[@isaacs/ttlcache](http://npm.im/@isaacs/ttlcache).

## Storing Undefined Values

This cache never stores undefined values, as `undefined` is used
internally in a few places to indicate that a key is not in the
cache.

You may call `cache.set(key, undefined)`, but this is just
an alias for `cache.delete(key)`. Note that this has the effect
that `cache.has(key)` will return _false_ after setting it to
undefined.

```js
cache.set(myKey, undefined)
cache.has(myKey) // false!
```

If you need to track `undefined` values, and still note that the
key is in the cache, an easy workaround is to use a sigil object
of your own.

```js
import { LRUCache } from 'lru-cache'
const undefinedValue = Symbol('undefined')
const cache = new LRUCache(...)
const mySet = (key, value) =>
  cache.set(key, value === undefined ? undefinedValue : value)
const myGet = (key, value) => {
  const v = cache.get(key)
  return v === undefinedValue ? undefined : v
}
```

## Performance

As of January 2022, version 7 of this library is one of the most
performant LRU cache implementations in JavaScript.

Benchmarks can be extremely difficult to get right. In
particular, the performance of set/get/delete operations on
objects will vary _wildly_ depending on the type of key used. V8
is highly optimized for objects with keys that are short strings,
especially integer numeric strings. Thus any benchmark which
tests _solely_ using numbers as keys will tend to find that an
object-based approach performs the best.

Note that coercing _anything_ to strings to use as object keys is
unsafe, unless you can be 100% certain that no other type of
value will be used. For example:

```js
const myCache = {}
const set = (k, v) => (myCache[k] = v)
const get = k => myCache[k]

set({}, 'please hang onto this for me')
set('[object Object]', 'oopsie')
```

Also beware of "Just So" stories regarding performance. Garbage
collection of large (especially: deep) object graphs can be
incredibly costly, with several "tipping points" where it
increases exponentially. As a result, putting that off until
later can make it much worse, and less predictable. If a library
performs well, but only in a scenario where the object graph is
kept shallow, then that won't help you if you are using large
objects as keys.

In general, when attempting to use a library to improve
performance (such as a cache like this one), it's best to choose
an option that will perform well in the sorts of scenarios where
you'll actually use it.

This library is optimized for repeated gets and minimizing
eviction time, since that is the expected need of a LRU. Set
operations are somewhat slower on average than a few other
options, in part because of that optimization. It is assumed
that you'll be caching some costly operation, ideally as rarely
as possible, so optimizing set over get would be unwise.

If performance matters to you:

1. If it's at all possible to use small integer values as keys,
   and you can guarantee that no other types of values will be
   used as keys, then do that, and use a cache such as
   [lru-fast](https://npmjs.com/package/lru-fast), or
   [mnemonist's
   LRUCache](https://yomguithereal.github.io/mnemonist/lru-cache)
   which uses an Object as its data store.

2. Failing that, if at all possible, use short non-numeric
   strings (ie, less than 256 characters) as your keys, and use
   [mnemonist's
   LRUCache](https://yomguithereal.github.io/mnemonist/lru-cache).

3. If the types of your keys will be anything else, especially
   long strings, strings that look like floats, objects, or some
   mix of types, or if you aren't sure, then this library will
   work well for you.

   If you do not need the features that this library provides
   (like asynchronous fetching, a variety of TTL staleness
   options, and so on), then [mnemonist's
   LRUMap](https://yomguithereal.github.io/mnemonist/lru-map) is
   a very good option, and just slightly faster than this module
   (since it does considerably less).

4. Do not use a `dispose` function, size tracking, or especially
   ttl behavior, unless absolutely needed. These features are
   convenient, and necessary in some use cases, and every attempt
   has been made to make the performance impact minimal, but it
   isn't nothing.

## Testing

When writing tests that involve TTL-related functionality, note
that this module creates an internal reference to the global
`performance` or `Date` objects at import time. If you import it
statically at the top level, those references cannot be mocked or
overridden in your test environment.

To avoid this, dynamically import the package within your tests
so that the references are captured after your mocks are applied.
For example:

```ts
// ❌ Not recommended
import { LRUCache } from 'lru-cache'
// mocking timers, e.g. jest.useFakeTimers()

// ✅ Recommended for TTL tests
// mocking timers, e.g. jest.useFakeTimers()
const { LRUCache } = await import('lru-cache')
```

This ensures that your mocked timers or time sources are
respected when testing TTL behavior.

Additionally, you can pass in a `perf` option when creating your
LRUCache instance. This option accepts any object with a `now`
method that returns a number.

For example, this would be a very bare-bones time-mocking system
you could use in your tests, without any particular test
framework:

```ts
import { LRUCache } from 'lru-cache'

let myClockTime = 0

const cache = new LRUCache<string>({
  max: 10,
  ttl: 1000,
  perf: {
    now: () => myClockTime,
  },
})

// run tests, updating myClockTime as needed
```

## Breaking Changes in Version 7

This library changed to a different algorithm and internal data
structure in version 7, yielding significantly better
performance, albeit with some subtle changes as a result.

If you were relying on the internals of LRUCache in version 6 or
before, it probably will not work in version 7 and above.

## Breaking Changes in Version 8

- The `fetchContext` option was renamed to `context`, and may no
  longer be set on the cache instance itself.
- Rewritten in TypeScript, so pretty much all the types moved
  around a lot.
- The AbortController/AbortSignal polyfill was removed. For this
  reason, **Node version 16.14.0 or higher is now required**.
- Internal properties were moved to actual private class
  properties.
- Keys and values must not be `null` or `undefined`.
- Minified export available at `'lru-cache/min'`, for both CJS
  and MJS builds.

## Breaking Changes in Version 9

- Named export only, no default export.
- AbortController polyfill returned, albeit with a warning when
  used.

## Breaking Changes in Version 10

- `cache.fetch()` return type is now `Promise<V | undefined>`
  instead of `Promise<V | void>`. This is an irrelevant change
  practically speaking, but can require changes for TypeScript
  users.

For more info, see the [change log](CHANGELOG.md).
```

## File: `fixup.sh`
```bash
#!/usr/bin/env bash

esbuild --minify \
  --sourcemap \
  --bundle dist/commonjs/index.js \
  --outfile=dist/commonjs/index.min.js \
  --format=cjs

esbuild --minify \
  --sourcemap \
  --bundle dist/esm/index.js \
  --outfile=dist/esm/index.min.js \
  --format=esm
```

## File: `map.js`
```javascript
module.exports = () => 'index.js'
```

## File: `package.json`
```json
{
  "name": "lru-cache",
  "description": "A cache object that deletes the least-recently-used items.",
  "version": "11.2.7",
  "author": "Isaac Z. Schlueter <i@izs.me>",
  "keywords": [
    "mru",
    "lru",
    "cache"
  ],
  "sideEffects": false,
  "scripts": {
    "build": "npm run prepare",
    "prepare": "tshy && bash fixup.sh",
    "pretest": "npm run prepare",
    "presnap": "npm run prepare",
    "test": "tap",
    "snap": "tap",
    "preversion": "npm test",
    "postversion": "npm publish",
    "prepublishOnly": "git push origin --follow-tags",
    "format": "prettier --write .",
    "typedoc": "typedoc --tsconfig ./.tshy/esm.json ./src/*.ts",
    "benchmark-results-typedoc": "bash scripts/benchmark-results-typedoc.sh",
    "prebenchmark": "npm run prepare",
    "benchmark": "make -C benchmark",
    "preprofile": "npm run prepare",
    "profile": "make -C benchmark profile"
  },
  "main": "./dist/commonjs/index.min.js",
  "types": "./dist/commonjs/index.d.ts",
  "tshy": {
    "exports": {
      "./raw": "./src/index.ts",
      ".": {
        "import": {
          "types": "./dist/esm/index.d.ts",
          "default": "./dist/esm/index.min.js"
        },
        "require": {
          "types": "./dist/commonjs/index.d.ts",
          "default": "./dist/commonjs/index.min.js"
        }
      }
    }
  },
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/isaacs/node-lru-cache.git"
  },
  "devDependencies": {
    "@types/node": "^24.3.0",
    "benchmark": "^2.1.4",
    "esbuild": "^0.25.9",
    "marked": "^4.2.12",
    "mkdirp": "^3.0.1",
    "prettier": "^3.6.2",
    "tap": "^21.1.0",
    "tshy": "^3.0.2",
    "typedoc": "^0.28.12"
  },
  "license": "BlueOak-1.0.0",
  "files": [
    "dist"
  ],
  "engines": {
    "node": "20 || >=22"
  },
  "exports": {
    "./raw": {
      "import": {
        "types": "./dist/esm/index.d.ts",
        "default": "./dist/esm/index.js"
      },
      "require": {
        "types": "./dist/commonjs/index.d.ts",
        "default": "./dist/commonjs/index.js"
      }
    },
    ".": {
      "import": {
        "types": "./dist/esm/index.d.ts",
        "default": "./dist/esm/index.min.js"
      },
      "require": {
        "types": "./dist/commonjs/index.d.ts",
        "default": "./dist/commonjs/index.min.js"
      }
    }
  },
  "type": "module",
  "module": "./dist/esm/index.min.js"
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "declaration": true,
    "declarationMap": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "inlineSources": true,
    "jsx": "react",
    "module": "nodenext",
    "moduleResolution": "nodenext",
    "noUncheckedIndexedAccess": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "sourceMap": true,
    "strict": true,
    "target": "es2022"
  }
}
```

## File: `typedoc.json`
```json
{
  "tsconfig": "./.tshy/esm.json",
  "entryPoints": ["./src/**/*.+(ts|tsx|mts|cts)"],
  "navigationLinks": {
    "GitHub": "https://github.com/isaacs/node-lru-cache",
    "isaacs projects": "https://isaacs.github.io/",
    "benchmark summary": "https://isaacs.github.io/node-lru-cache/benchmark/",
    "benchmark details": "https://isaacs.github.io/node-lru-cache/benchmark/results/"
  }
}
```

## File: `benchmark/.gitignore`
```
.DS_Store
/node_modules
/package.json
/package-lock.json
/impls.txt
/results
/results.md
/profiles
/profile.txt
/isolate*.log
```

## File: `benchmark/CHANGELOG.md`
```markdown
<a name="1.1.0"></a>
# 1.1.0 (2017-10-02)

* 1.0.0 ([4b43691](https://github.com/dominictarr/bench-lru/commit/4b43691))
* Add bench specification ([c55b726](https://github.com/dominictarr/bench-lru/commit/c55b726))
* add hashlru ([09e99a0](https://github.com/dominictarr/bench-lru/commit/09e99a0))
* Add ignore ([4f8b103](https://github.com/dominictarr/bench-lru/commit/4f8b103))
* Add linter and changelog automatization ([8eadb2d](https://github.com/dominictarr/bench-lru/commit/8eadb2d))
* Add UI feedback ([d4a7977](https://github.com/dominictarr/bench-lru/commit/d4a7977))
* Avoid store data ([bf49f44](https://github.com/dominictarr/bench-lru/commit/bf49f44))
* Calculate bundle size ([685dbfa](https://github.com/dominictarr/bench-lru/commit/685dbfa))
* deps ([4c8f827](https://github.com/dominictarr/bench-lru/commit/4c8f827))
* Fix find ([f8c979e](https://github.com/dominictarr/bench-lru/commit/f8c979e))
* Fix scope ([2be6027](https://github.com/dominictarr/bench-lru/commit/2be6027))
* fix typo @chentsulin found ([46eead9](https://github.com/dominictarr/bench-lru/commit/46eead9))
* Improve format ([7dec452](https://github.com/dominictarr/bench-lru/commit/7dec452))
* initial ([e945b02](https://github.com/dominictarr/bench-lru/commit/e945b02))
* Moar runs ([00133bd](https://github.com/dominictarr/bench-lru/commit/00133bd))
* Move round inside bench ([ba91f0c](https://github.com/dominictarr/bench-lru/commit/ba91f0c))
* new results ([cf2a362](https://github.com/dominictarr/bench-lru/commit/cf2a362))
* Re-testing with `tiny-lru`, fixes #4 ([8130d27](https://github.com/dominictarr/bench-lru/commit/8130d27)), closes [#4](https://github.com/dominictarr/bench-lru/issues/4)
* results and discussion ([f566cd2](https://github.com/dominictarr/bench-lru/commit/f566cd2))
* Sort by name ([9c85fb2](https://github.com/dominictarr/bench-lru/commit/9c85fb2))
* Sort results ([60dbed3](https://github.com/dominictarr/bench-lru/commit/60dbed3))
* Sort results ([f294ccc](https://github.com/dominictarr/bench-lru/commit/f294ccc))
* Update ([5c244a6](https://github.com/dominictarr/bench-lru/commit/5c244a6))
* Update deps ([35ac9f7](https://github.com/dominictarr/bench-lru/commit/35ac9f7))
* update readme ([df5c278](https://github.com/dominictarr/bench-lru/commit/df5c278))
* Update README.md ([f5e6dd4](https://github.com/dominictarr/bench-lru/commit/f5e6dd4))
* Updating `data.csv` ([6103c7c](https://github.com/dominictarr/bench-lru/commit/6103c7c))
* Updating a typo ([8286afa](https://github.com/dominictarr/bench-lru/commit/8286afa))
* Updating tiny-lru & re-enabling it's test ([954e28a](https://github.com/dominictarr/bench-lru/commit/954e28a))
* use hashlru, and benchmark reads also ([6fea600](https://github.com/dominictarr/bench-lru/commit/6fea600))



```

## File: `benchmark/LICENSE`
```
Copyright (c) 2016 'Dominic Tarr'

Permission is hereby granted, free of charge, 
to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to 
deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom 
the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice 
shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR 
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `benchmark/Makefile`
```
all: package.json index.js worker.js
	rm -rf results.txt results
	npm run benchmark | tee results.md

impls.txt: fetch-impls.sh
	bash fetch-impls.sh

profile: worker.js
	bash profile.sh

package.json: make-deps.sh impls.txt
	bash make-deps.sh
```

## File: `benchmark/README.md`
```markdown
# bench-lru

benchmark the least-recently-used caches which are available on npm.

## Update: March, 2023

Forked and ported over to be used within the lru-cache project
directly.  Made a bunch of changes to make it easier to run this
on an ongoing basis and detect regressions.

More implementations can be added by adding them to the list in
the `make-deps.sh` script, but for my purposes, the only decently
fast and reasonably correct LRU implementations apart from this
one are hashlru, lru-fast, and especially, mnemonist.  My purpose
is not to win a contest, it's to easily track and debug
performance characteristics of this library.

Run the tests by running `make` in this directory.

## Update: January, 2022

This is a fork of Dominc Tarr's original `bench-lru` script. I've made the
following modifications.

First, I noted that cache performance and correctness in JavaScript is
highly dependent on the types of keys used to store items in the cache.

Specifically:

1. When using keys that aren't strings or symbols, it's possible for keys
   to collide if using an `Object` as the backing store rather than a
   `Map`.
2. When using integer numbers as object keys, V8 is extremely optimized for
   `Object` data storage, especially if the values are also integers.
   However, if the values are numeric strings but numeric _float_ strings,
   performance goes out the window.
3. Long strings are much slower Object keys than long strings.

In the real world, it's quite rare to store 200k integers using the exact
same 200k integers as keys. This iteration of the benchmark uses a variety
of integers, floats, numeric integer strings, numeric float strings, long
strings, strings and integers that collide, objects, and so on, and
disqualifies caches that don't pass a basic correctness smoke test.

Next, the weighting of scores doesn't much match real world use cases
either. In observing several production use cases of LRU caches, the
some consistent patterns can be observed.

Typically, an LRUCache is being used (if it is actually needed) for a case
where:

1. The total data corpus is _very large_, and cannot comfortably fit in
   memory. (If it isn't large, just save it all, don't bother with an
   LRU.)
2. The time required to fetch any given item is significant. (If it isn't,
   just fetch it each time, don't bother with an LRU.)
3. The time over which the data will be accessed is significant, and thus
   the subset of the corpus of data which will _eventually_ need to be
   accessed is by the process is more than can comfortably fit in memory.
4. Items tend to spike in popularity for a while, then become less
   frequenty accessed.

If these criteria are met, an LRUCache is a good fit. If a few of them are
likely, and the others _might_ be true, then it might still be a good fit
to be safe. It's a fairly common need, if somewhat specific.

Given this behavior pattern, the weights in the benchmark were off. Simply
reporting updates per ms next to evictions per ms is a bit unhelpful.
Dominic was correct that evictions are important.

However, an eviction _can only happen_ at the time of making a `set()`
call, which means that you just performed some expensive upstream action to
get the thing that you're caching from its origin.

`update`s (that is, setting a key which is already in the cache) are
extremely rare in normal LRU-friendly workloads. If you already have it in
the cache, don't fetch it upstream or write it again, use the cached one.
That's the whole point!

The _most_ frequent operations an LRUCache is normally called upon for is:
"fetching an item from the queue again".

That is to say, to the greatest extent possible, `get()` performance should
be roughly equivalent, regardless of where in the heirarchy of recency a
given item is found. If fetching the most recently used item is fast, but
fetching the item 50% most recently used, or even least recently used, is
slow, then the cache will perform poorly (and unpredictably!) under real
workloads.

To account for the priorities (and the fact that eviction is much slower in
every cache measured), the following weights are applied to form a
final "score", which is used to sort the list:

1. `evict * 5`
2. `get2 * 5`
3. `get1 * 3`
4. `set * 2`
5. `update * 1`

Note that since `get2` tends to be much faster than `evict` in all caches
tested, this ends up being the most important metric.

Also, I observed that some caches perform very well when `get()` calls are
made in the order in which they were inserted into the cache, but much more
poorly when `get()` calls are made out of order. Under real workloads, a
cache is rarely called upon to list its contents in insertion order, but
instead is used in an unpredictable order.

To accomplish this, the ordering of the data used in the `update` and
`get2` benchmarks is randomized, so that the items need to be constantly
reshuffled, as they would be in a real use case.

### Conclusions from this new approach, and my attempts to make lru-cache perform well

1. Only caches with `Map`-based key stores are capable of handling keys
   that are long string, numeric float strings, or `Symbol` objects with
   adequate performance.

   This was surprising to me! I expected that `Symbol` objects would
   perform well in an `Object` key store, and I suspect that future
   versions of V8 may optimize this code path if more people use it. The
   performance gains on long strings (and especially numeric float strings)
   in `Map` key stores was somewhat surprising as well, but this just shows
   the hazard of optimizing for a benchmark instead of making a benchmark
   match real workloads.

2. Only caches with `Map`-based key stores are capable of handling
   non-string/symbol keys correctly.

3. The garbage-collection penalty for throwing away an object (the approach
   advocated below) is very low for an object full of integer keys and
   numeric values. However, it rises dramatically for almost any other
   shape of data, making linked-list style approaches more effective.

4. Similarly, the gc penalty for object-based linked list approaches makes
   them perform significantly worse than pointer-based linked list
   approaches.

   That is, it's much faster to implement the linked list as two arrays of
   integers and do `this.next[index]` and `this.previous[index]` rather
   than an array of node objects and `node.next` and `node.previous`. No
   amount of object optimization (reusing objects from a pool, etc.)
   seemed able to get around this.

   This wasn't surprising, but it was disappointing. `node.next.value` is
   much more ergonomic and readable than
   `this.valueList[this.next[index]]`.

Almost any of these cache implementations will perform well enough in any
situation where you find yourself with a problem that needs a cache. But
as always, if you are optimizing a hot path and performance matters, make
sure to test it against your actual scenario. If you are strictly using
integers as keys, it's worth using one of the "worse" caches on this list.

## Results

```
int: just an integer
| name                                                           | set   | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|-------|-------|--------|-------|-------|--------|
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 27663 | 63492 | 8780   | 59880 | 6425  | 586107 |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 22396 | 55096 | 9639   | 51282 | 6359  | 507924 |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 37736 | 36765 | 15674  | 35778 | 15974 | 460201 |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 15723 | 46083 | 6388   | 44346 | 12225 | 458938 |
| [hashlru](https://npmjs.com/package/hashlru)                   | 29112 | 31696 | 12747  | 34130 | 12666 | 400039 |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 7313  | 30395 | 8547   | 25445 | 6398  | 273573 |
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 10655 | 20471 | 6796   | 19084 | 5244  | 211159 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 10395 | 20141 | 6662   | 18727 | 5417  | 208595 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 9790  | 20346 | 4652   | 17809 | 5180  | 200215 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 12547 | 16488 | 8921   | 16000 | 6002  | 193489 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 7605  | 17513 | 4121   | 15911 | 4558  | 174215 |
| [lru](https://www.npmjs.com/package/lru)                       | 11779 | 14194 | 5732   | 14914 | 4168  | 167282 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 8107  | 15373 | 7460   | 14296 | 3853  | 160538 |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 9195  | 11179 | 5258   | 15962 | 3995  | 156970 |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 5218  | 12247 | 4380   | 10422 | 3341  | 120372 |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 4985  | 11534 | 4858   | 11001 | 2582  | 117345 |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 7027  | 9896  | 4308   | 8803  | 2876  | 106445 |

strint: stringified integer
| name                                                           | set   | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|-------|-------|--------|-------|-------|--------|
| [hashlru](https://npmjs.com/package/hashlru)                   | 42373 | 37383 | 14025  | 37383 | 13889 | 467280 |
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 18709 | 42105 | 7505   | 41322 | 17094 | 463318 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 18570 | 42373 | 7767   | 40984 | 16807 | 460981 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 16625 | 41408 | 7189   | 40486 | 16026 | 447223 |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 28050 | 42644 | 8120   | 40241 | 6020  | 423457 |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 26702 | 35273 | 11111  | 35273 | 14738 | 420389 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 20222 | 33389 | 10352  | 32787 | 17969 | 404743 |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 12895 | 36166 | 7933   | 36496 | 10995 | 379676 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 11587 | 36232 | 4918   | 36697 | 11461 | 377578 |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 23095 | 4836  | 8150   | 54795 | 6141  | 373528 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 10554 | 29197 | 7719   | 28777 | 7669  | 298648 |
| [lru](https://www.npmjs.com/package/lru)                       | 20964 | 28818 | 5132   | 27894 | 4749  | 296729 |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 7997  | 29240 | 5983   | 28249 | 5267  | 277277 |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 6570  | 26774 | 5072   | 26385 | 6693  | 263924 |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 6037  | 22396 | 6244   | 20263 | 5520  | 214421 |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 8197  | 17668 | 6470   | 19436 | 6234  | 204218 |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 7496  | 15760 | 4614   | 13643 | 3716  | 153681 |

str: string that is not a number
| name                                                           | set  | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|------|-------|--------|-------|-------|--------|
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 7449 | 17637 | 7321   | 16260 | 5587  | 184365 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 6691 | 12788 | 5349   | 11396 | 3661  | 132380 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 6466 | 12821 | 3752   | 11409 | 3662  | 130502 |
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 6568 | 12547 | 5362   | 11142 | 3604  | 129869 |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 7095 | 12531 | 6250   | 10256 | 3142  | 125023 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 7278 | 10341 | 5919   | 9341  | 3801  | 117208 |
| [hashlru](https://npmjs.com/package/hashlru)                   | 9311 | 6517  | 4614   | 6307  | 8478  | 116712 |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 4241 | 9302  | 5745   | 8772  | 4632  | 109153 |
| [lru](https://www.npmjs.com/package/lru)                       | 6711 | 10449 | 5947   | 8937  | 2120  | 106001 |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 4379 | 9770  | 5583   | 9350  | 2702  | 103911 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 5259 | 9315  | 4915   | 9166  | 2539  | 101903 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 5302 | 8897  | 3049   | 8241  | 3269  | 97894  |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 4028 | 8214  | 3213   | 7339  | 2219  | 83701  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 3716 | 7321  | 3600   | 7110  | 2236  | 79725  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 3512 | 7800  | 3361   | 6698  | 2057  | 77560  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 4660 | 6616  | 2740   | 4827  | 1910  | 65593  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 4360 | 5792  | 2826   | 5330  | 1956  | 65352  |

numstr: a mix of integers and strings that look like them
⠴ Benchmarking 1 of 17 caches [hashlru] failed correctness check at key="2"
⠧ Benchmarking 3 of 17 caches [hyperlru-object] failed correctness check at key="2"
⠋ Benchmarking 5 of 17 caches [lru] failed correctness check at key="2"
⠋ Benchmarking 11 of 17 caches [lru-fast] failed correctness check at key="2"
⠦ Benchmarking 13 of 17 caches [secondary-cache] failed correctness check at key="2"
⠹ Benchmarking 14 of 17 caches [simple-lru-cache] failed correctness check at key="2"
⠇ Benchmarking 15 of 17 caches [tiny-lru] failed correctness check at key="2"
⠼ Benchmarking 16 of 17 caches [mnemonist-object] failed correctness check at key="2"
| name                                                           | set   | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|-------|-------|--------|-------|-------|--------|
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 10309 | 18519 | 6470   | 16736 | 6105  | 196850 |
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 10194 | 18587 | 6112   | 16327 | 5863  | 193211 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 9281  | 18382 | 5215   | 16779 | 5757  | 191603 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 11211 | 17483 | 5025   | 15552 | 6085  | 188081 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 7257  | 13996 | 3567   | 13477 | 4880  | 151854 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 7070  | 13803 | 6260   | 12469 | 3387  | 141089 |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 5044  | 12682 | 3731   | 10667 | 3192  | 121160 |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 4302  | 11461 | 3851   | 9901  | 2620  | 109443 |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 6510  | 9276  | 4511   | 8969  | 3217  | 106289 |
| [hashlru](https://npmjs.com/package/hashlru)                   | 0     | 0     | 0      | 0     | 0     | 0      |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 0     | 0     | 0      | 0     | 0     | 0      |
| [lru](https://www.npmjs.com/package/lru)                       | 0     | 0     | 0      | 0     | 0     | 0      |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 0     | 0     | 0      | 0     | 0     | 0      |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 0     | 0     | 0      | 0     | 0     | 0      |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 0     | 0     | 0      | 0     | 0     | 0      |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 0     | 0     | 0      | 0     | 0     | 0      |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 0     | 0     | 0      | 0     | 0     | 0      |

pi: multiples of pi
| name                                                           | set  | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|------|-------|--------|-------|-------|--------|
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 5588 | 11891 | 4519   | 10905 | 3064  | 121213 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 7457 | 9980  | 5838   | 9579  | 3842  | 117797 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 4700 | 10096 | 2950   | 11148 | 2719  | 111973 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 5372 | 10256 | 4248   | 10262 | 2951  | 111825 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 3807 | 8893  | 5237   | 8058  | 2400  | 91820  |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 3269 | 5313  | 3204   | 7968  | 2526  | 78151  |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 3309 | 6709  | 3230   | 6861  | 1837  | 73465  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 3152 | 6234  | 3444   | 6246  | 1694  | 68150  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 2642 | 4103  | 2452   | 4190  | 1508  | 48535  |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 1643 | 2244  | 2016   | 2315  | 836   | 27789  |
| [lru](https://www.npmjs.com/package/lru)                       | 1688 | 1980  | 1744   | 1891  | 1277  | 26900  |
| [hashlru](https://npmjs.com/package/hashlru)                   | 1801 | 1599  | 1362   | 1545  | 1655  | 25761  |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 1358 | 1948  | 1803   | 1998  | 789   | 24298  |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 1326 | 1944  | 1590   | 1994  | 681   | 23449  |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 1542 | 1917  | 1484   | 1803  | 749   | 23079  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 1304 | 1755  | 1473   | 1871  | 663   | 22016  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 1336 | 1597  | 1162   | 1661  | 610   | 19980  |

float: floating point values
| name                                                           | set  | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|------|-------|--------|-------|-------|--------|
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 5420 | 10493 | 3197   | 12255 | 3091  | 122246 |
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 5478 | 11827 | 4633   | 10858 | 3048  | 120600 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 7582 | 10325 | 6209   | 9766  | 3849  | 120423 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 5318 | 8150  | 3664   | 11912 | 3293  | 114775 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 4004 | 8610  | 5488   | 8407  | 2555  | 94136  |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 3327 | 7067  | 3033   | 7776  | 2532  | 82428  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 3077 | 6609  | 3506   | 6414  | 1681  | 69962  |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 3151 | 6279  | 3212   | 6623  | 1698  | 69956  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 2964 | 4551  | 2616   | 4665  | 1701  | 54027  |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 1657 | 2376  | 2028   | 2448  | 846   | 28940  |
| [lru](https://www.npmjs.com/package/lru)                       | 1749 | 2181  | 1821   | 1985  | 1207  | 27822  |
| [hashlru](https://npmjs.com/package/hashlru)                   | 1784 | 1675  | 1456   | 1604  | 1639  | 26264  |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 1662 | 2006  | 1612   | 1917  | 840   | 24739  |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 1367 | 2018  | 1788   | 2071  | 703   | 24446  |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 1368 | 1919  | 1880   | 1975  | 797   | 24233  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 1305 | 1866  | 1515   | 1886  | 684   | 22573  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 1323 | 1662  | 1232   | 1690  | 634   | 20484  |

obj: an object with a single key
⠴ Benchmarking 1 of 17 caches [hashlru] failed correctness check at key={"z":0}
⠧ Benchmarking 3 of 17 caches [hyperlru-object] failed correctness check at key={"z":0}
⠇ Benchmarking 5 of 17 caches [lru] failed correctness check at key={"z":0}
⠼ Benchmarking 11 of 17 caches [lru-fast] failed correctness check at key={"z":0}
⠋ Benchmarking 13 of 17 caches [secondary-cache] failed correctness check at key={"z":0}
⠴ Benchmarking 14 of 17 caches [simple-lru-cache] failed correctness check at key={"z":0}
⠙ Benchmarking 15 of 17 caches [tiny-lru] failed correctness check at key={"z":0}
⠧ Benchmarking 16 of 17 caches [mnemonist-object] failed correctness check at key={"z":0}
| name                                                           | set   | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|-------|-------|--------|-------|-------|--------|
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 10215 | 19822 | 6581   | 19157 | 5623  | 210377 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 9921  | 20429 | 6718   | 18349 | 5548  | 207332 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 8913  | 20387 | 5954   | 18639 | 5366  | 204966 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 11710 | 18100 | 5161   | 16273 | 5700  | 192746 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 7055  | 17227 | 3566   | 16064 | 4551  | 172432 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 7613  | 14286 | 6892   | 12723 | 3630  | 146741 |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 5061  | 12158 | 4043   | 10655 | 3644  | 122134 |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 6129  | 10616 | 5444   | 10304 | 2957  | 115855 |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 4537  | 11056 | 3974   | 9128  | 2557  | 104641 |
| [hashlru](https://npmjs.com/package/hashlru)                   | 0     | 0     | 0      | 0     | 0     | 0      |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 0     | 0     | 0      | 0     | 0     | 0      |
| [lru](https://www.npmjs.com/package/lru)                       | 0     | 0     | 0      | 0     | 0     | 0      |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 0     | 0     | 0      | 0     | 0     | 0      |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 0     | 0     | 0      | 0     | 0     | 0      |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 0     | 0     | 0      | 0     | 0     | 0      |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 0     | 0     | 0      | 0     | 0     | 0      |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 0     | 0     | 0      | 0     | 0     | 0      |

rand: random floating point number
| name                                                           | set  | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|------|-------|--------|-------|-------|--------|
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 4912 | 10644 | 3218   | 11744 | 3027  | 118829 |
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 5789 | 11013 | 4197   | 10834 | 3099  | 118479 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 7524 | 10050 | 5936   | 9398  | 3826  | 117254 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 5640 | 9217  | 3837   | 10846 | 3061  | 112303 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 3982 | 8052  | 5155   | 8651  | 2431  | 92685  |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 3176 | 7246  | 2881   | 7070  | 2488  | 78761  |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 3071 | 6810  | 3150   | 6481  | 1812  | 71187  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 3175 | 6295  | 3386   | 6109  | 1712  | 67726  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 3341 | 4206  | 2594   | 4619  | 1653  | 53254  |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 1669 | 2380  | 1984   | 2350  | 859   | 28507  |
| [lru](https://www.npmjs.com/package/lru)                       | 1723 | 1866  | 1668   | 1829  | 1265  | 26182  |
| [hashlru](https://npmjs.com/package/hashlru)                   | 1790 | 1610  | 1402   | 1546  | 1613  | 25607  |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 1667 | 2060  | 1572   | 1946  | 809   | 24861  |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 1368 | 1958  | 1791   | 1999  | 768   | 24236  |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 1360 | 1952  | 1760   | 1987  | 696   | 23751  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 1205 | 1815  | 1509   | 1949  | 682   | 22519  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 1391 | 1665  | 1217   | 1740  | 645   | 20919  |

sym: a Symbol object
⠼ Benchmarking 5 of 17 caches [lru] failed correctness check TypeError: Cannot convert a Symbol value to a string
    at LRU.set (/Users/isaacs/dev/isaacs/lru-cache/bench-lru/node_modules/lru/index.js:69:41)
    at self.onmessage (evalmachine.<anonymous>:116:38)
    at process.<anonymous> (/Users/isaacs/dev/isaacs/lru-cache/bench-lru/node_modules/tiny-worker/lib/worker.js:60:55)
    at process.emit (node:events:520:28)
    at emit (node:internal/child_process:936:14)
    at processTicksAndRejections (node:internal/process/task_queues:84:21)
| name                                                           | set   | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|-------|-------|--------|-------|-------|--------|
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 9886  | 19361 | 6991   | 17809 | 5445  | 201116 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 9809  | 19455 | 6258   | 17794 | 5430  | 200361 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 9074  | 19417 | 6450   | 17953 | 5359  | 199409 |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 7776  | 20492 | 6831   | 17391 | 5593  | 198779 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 10893 | 17652 | 5375   | 15540 | 5616  | 185897 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 7297  | 14399 | 6925   | 12650 | 3591  | 145921 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 7174  | 14124 | 3938   | 12300 | 4535  | 144833 |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 7758  | 12845 | 6824   | 11682 | 3125  | 134910 |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 6028  | 3537  | 6916   | 16340 | 2874  | 125653 |
| [hashlru](https://npmjs.com/package/hashlru)                   | 9602  | 7148  | 5144   | 6761  | 8264  | 120917 |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 5179  | 12114 | 3814   | 10846 | 3207  | 120779 |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 4636  | 8957  | 6044   | 8981  | 4601  | 110097 |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 4540  | 10959 | 4344   | 8799  | 2696  | 103776 |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 6129  | 8421  | 5045   | 8460  | 2817  | 98951  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 3577  | 7533  | 3856   | 6349  | 2258  | 76644  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 5319  | 7573  | 3177   | 5238  | 2055  | 72999  |
| [lru](https://www.npmjs.com/package/lru)                       | 0     | 0     | 0      | 0     | 0     | 0      |

longstr: a very long string
| name                                                           | set  | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|------|-------|--------|-------|-------|--------|
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 5882 | 11044 | 5009   | 10147 | 3107  | 116175 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 5828 | 11287 | 4102   | 10320 | 2738  | 114909 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 5936 | 9960  | 4827   | 10020 | 3224  | 112799 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 6464 | 9264  | 6291   | 8396  | 3193  | 104956 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 4900 | 8834  | 3499   | 8094  | 2759  | 94066  |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 4700 | 8316  | 5185   | 7997  | 2298  | 91008  |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 3666 | 7862  | 3514   | 6991  | 2044  | 79607  |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 2949 | 6658  | 4930   | 6640  | 2690  | 77452  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 3377 | 7283  | 3492   | 6607  | 1856  | 74410  |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 2248 | 4006  | 4218   | 3946  | 2547  | 53197  |
| [hashlru](https://npmjs.com/package/hashlru)                   | 4003 | 3281  | 2791   | 3078  | 3169  | 51875  |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 2261 | 4432  | 3907   | 4352  | 1616  | 51565  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 3132 | 4287  | 2691   | 4307  | 1282  | 49761  |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 2502 | 3859  | 3854   | 3752  | 1826  | 48325  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 1989 | 3715  | 2690   | 3430  | 1235  | 41138  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 2500 | 3394  | 2086   | 2845  | 1148  | 37233  |
| [lru](https://www.npmjs.com/package/lru)                       | 2345 | 3073  | 2714   | 2903  | 1042  | 36348  |

mix: a mix of all the types
⠦ Benchmarking 1 of 17 caches [hashlru] failed correctness check at key={"z":3}
⠧ Benchmarking 3 of 17 caches [hyperlru-object] failed correctness check at key={"z":3}
⠏ Benchmarking 5 of 17 caches [lru] failed correctness check TypeError: Cannot convert a Symbol value to a string
    at LRU.set (/Users/isaacs/dev/isaacs/lru-cache/bench-lru/node_modules/lru/index.js:69:41)
    at self.onmessage (evalmachine.<anonymous>:116:38)
    at process.<anonymous> (/Users/isaacs/dev/isaacs/lru-cache/bench-lru/node_modules/tiny-worker/lib/worker.js:60:55)
    at process.emit (node:events:520:28)
    at emit (node:internal/child_process:936:14)
    at processTicksAndRejections (node:internal/process/task_queues:84:21)
⠼ Benchmarking 11 of 17 caches [lru-fast] failed correctness check at key={"z":3}
⠴ Benchmarking 13 of 17 caches [secondary-cache] failed correctness check at key={"z":3}
⠙ Benchmarking 14 of 17 caches [simple-lru-cache] failed correctness check at key={"z":3}
⠧ Benchmarking 15 of 17 caches [tiny-lru] failed correctness check at key={"z":3}
⠸ Benchmarking 16 of 17 caches [mnemonist-object] failed correctness check at key={"z":3}
| name                                                           | set  | get1  | update | get2  | evict | score  |
|----------------------------------------------------------------|------|-------|--------|-------|-------|--------|
| [lru-cache-7](https://npmjs.com/package/lru-cache)             | 7457 | 13342 | 5802   | 12195 | 3979  | 141612 |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 8061 | 14015 | 6369   | 11312 | 3975  | 140971 |
| [lru-cache-7-dispose](https://npmjs.com/package/lru-cache)     | 7138 | 13271 | 5321   | 12210 | 3953  | 140225 |
| [lru-cache-7-size](https://npmjs.com/package/lru-cache)        | 6847 | 13405 | 4351   | 12070 | 3757  | 137395 |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 5316 | 9676  | 4381   | 9170  | 2900  | 104391 |
| [lru-cache-7-ttl](https://npmjs.com/package/lru-cache)         | 5708 | 9833  | 3164   | 8333  | 3419  | 102839 |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 4165 | 8624  | 3328   | 7890  | 2557  | 89765  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 3875 | 7758  | 3351   | 7179  | 2017  | 80355  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 4919 | 6256  | 3227   | 6129  | 2147  | 73213  |
| [hashlru](https://npmjs.com/package/hashlru)                   | 0    | 0     | 0      | 0     | 0     | 0      |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 0    | 0     | 0      | 0     | 0     | 0      |
| [lru](https://www.npmjs.com/package/lru)                       | 0    | 0     | 0      | 0     | 0     | 0      |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 0    | 0     | 0      | 0     | 0     | 0      |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 0    | 0     | 0      | 0     | 0     | 0      |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 0    | 0     | 0      | 0     | 0     | 0      |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 0    | 0     | 0      | 0     | 0     | 0      |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 0    | 0     | 0      | 0     | 0     | 0      |
```

The best performers are `lru-cache` version 7 and `mnemonist`'s `LRUMap`, across
most categories. `mnemonist-map` seems to consistently have slightly
better eviction and set performance, and slightly worse get performance,
for many key types. The difference is small enough to be negligible,
which is to be expected.

For object-friendly key spaces (strictly integers or strictly short strings),
`mnemonist`'s `LRUCache` and `hashlru` seem to do the best.

For strictly integer key sets, `lru-fast` lives up to its name, blowing the
other implementations out of the water, but did not perform nearly as well
with other types of keys.

---

What follows below is Dominic Tarr's original discussion from 2016.

_[@isaacs](https://github.com/isaacs)_

---

## Introduction

An LRU cache is a cache with bounded memory use.
The point of a cache is to improve performance,
so how performant are the available implementations?

LRUs achive bounded memory use by removing the oldest items when a threashold number of items
is reached. We measure 3 cases, adding an item, updating an item, and adding items
which push other items out of the LRU.

There is a [previous benchmark](https://www.npmjs.com/package/bench-cache)
but it did not describe it's methodology. (and since it measures the memory used,
but tests everything in the same process, it does not get clear results)

## Benchmark

I run a very simple multi-process benchmark, with 5 iterations to get a median of ops/ms:

1. Set the LRU to fit max N=200,000 items.
2. Add N random numbers to the cache, with keys 0-N.
3. Then update those keys with new random numbers.
4. Then _evict_ those keys, by adding keys N-2N.

### Results

Operations per millisecond (_higher is better_):

| name                                                           | set   | get1  | update | get2  | evict |
| -------------------------------------------------------------- | ----- | ----- | ------ | ----- | ----- |
| [hashlru](https://npmjs.com/package/hashlru)                   | 18536 | 17590 | 17794  | 18332 | 9381  |
| [mnemonist-object](https://www.npmjs.com/package/mnemonist)    | 15314 | 69444 | 35026  | 68966 | 7949  |
| [quick-lru](https://npmjs.com/package/quick-lru)               | 8214  | 4572  | 6777   | 4608  | 6345  |
| [tiny-lru](https://npmjs.com/package/tiny-lru)                 | 6530  | 46296 | 37244  | 42017 | 5961  |
| [lru-fast](https://npmjs.com/package/lru-fast)                 | 5979  | 36832 | 32626  | 40900 | 5929  |
| [mnemonist-map](https://www.npmjs.com/package/mnemonist)       | 6272  | 15785 | 10923  | 16077 | 3738  |
| [lru](https://www.npmjs.com/package/lru)                       | 3927  | 5454  | 5001   | 5366  | 2827  |
| [simple-lru-cache](https://npmjs.com/package/simple-lru-cache) | 3393  | 3855  | 3701   | 3899  | 2496  |
| [hyperlru-object](https://npmjs.com/package/hyperlru-object)   | 3515  | 3953  | 4044   | 4102  | 2495  |
| [js-lru](https://www.npmjs.com/package/js-lru)                 | 3813  | 10010 | 9246   | 10309 | 1843  |
| [secondary-cache](https://npmjs.com/package/secondary-cache)   | 2780  | 5705  | 5790   | 10549 | 1727  |
| [lru-cache](https://npmjs.com/package/lru-cache)               | 2275  | 3388  | 3334   | 3301  | 1593  |
| [hyperlru-map](https://npmjs.com/package/hyperlru-map)         | 2424  | 2508  | 2443   | 2540  | 1552  |
| [modern-lru](https://npmjs.com/package/modern-lru)             | 2710  | 3946  | 3581   | 4021  | 1327  |
| [mkc](https://npmjs.com/packacge/package/mkc)                  | 1559  | 2044  | 1178   | 2161  | 1037  |

We can group the results in a few categories:

- all rounders (mnemonist, lru_cache, tiny-lru, simple-lru-cache, lru-fast) where the performance to add update and evict are comparable.
- fast-write, slow-evict (lru, hashlru, lru-native, modern-lru) these have better set/update times, but for some reason are quite slow to evict items!
- slow in at least 2 categories (lru-cache, mkc, faster-lru-cache, secondary-cache)

## Discussion

It appears that all-round performance is the most difficult to achive, in particular,
performance on eviction is difficult to achive. I think eviction performance is the most important
consideration, because once the cache is _warm_ each subsequent addition causes an eviction,
and actively used, _hot_, cache will run close to it's eviction performance.
Also, some have faster add than update, and some faster update than add.

`modern-lru` gets pretty close to `lru-native` perf.
I wrote `hashlru` after my seeing the other results from this benchmark, it's important to point
out that it does not use the classic LRU algorithm, but has the important properties of the LRU
(bounded memory use and O(1) time complexity)

Splitting the benchmark into multiple processes helps minimize JIT state pollution (gc, turbofan opt/deopt, etc.), and we see a much clearer picture of performance per library.

## Future work

This is still pretty early results, take any difference smaller than an order of magnitude with a grain of salt.

It is necessary to measure the statistical significance of the results to know accurately the relative performance of two closely matched implementations.

I also didn't test the memory usage. This should be done running the benchmarks each in a separate process, so that the memory used by each run is not left over while the next is running.

## Conclusion

Javascript is generally slow, so one of the best ways to make it fast is to write less of it.
LRUs are also quite difficult to implement (linked lists!). In trying to come up with a faster
LRU implementation I realized that something far simpler could do the same job. Especially
given the strengths and weaknesses of javascript, this is significantly faster than any of the
other implementations, _including_ the C implementation. Likely, the overhead of the C<->js boundry
is partly to blame here.

## License

MIT
```

## File: `benchmark/fetch-impls.sh`
```bash
#!/usr/bin/env bash

# get the latest patch in each lru-cache 7.x and up,
# plus mnemonist, hashlru, and lru-fast

nvs=($(
  npm view 'lru-cache@>=7' name | awk -F. '{print $1 "." $2}' | sort -r -V | uniq
)
'mnemonist@0.39'
'hashlru@2'
'lru-fast@0.2')

echo "lru-cache_CURRENT" > impls.txt
for dep in "${nvs[@]}"; do
  name=${dep/@/_}
  echo $name >> impls.txt
done
```

## File: `benchmark/impls.js`
```javascript
const { readFileSync } = require('fs')
const impls = readFileSync(__dirname + '/impls.txt', 'utf8')
  .trim()
  .split('\n')
for (const impl of impls) {
  if (impl.startsWith('lru-cache_')) {
    const req = require(impl)
    const LRUCache = req.LRUCache || req
    exports[impl] = max => new LRUCache({ max })
  } else if (impl.startsWith('mnemonist_')) {
    MnemonistLRUMap = require(impl + '/lru-map-with-delete')
    MnemonistLRUCache = require(impl + '/lru-cache-with-delete')
    exports[impl + '_obj'] = max => new MnemonistLRUCache(max)
    exports[impl + '_map'] = max => new MnemonistLRUMap(max)
  } else if (impl.startsWith('hashlru_')) {
    exports[impl] = require(impl)
  } else if (impl.startsWith('lru-fast_')) {
    const { LRUCache } = require(impl)
    exports[impl] = max => new LRUCache(max)
  } else {
    throw new Error(
      'found an impl i dont know how to create: ' + impl
    )
  }
}

exports['just a Map'] = _ => new Map()

exports['just a null obj'] = _ => {
  const data = Object.create(null)
  return { set: (k, v) => (data[k] = v), get: k => data[k] }
}

exports['just a {}'] = _ => {
  const data = {}
  return { set: (k, v) => (data[k] = v), get: k => data[k] }
}
```

## File: `benchmark/index.js`
```javascript
'use strict'

process.env.__LRU_BENCH_DIR = __dirname
require('mkdirp').sync(__dirname + '/results')

const Worker = require('tiny-worker')
const ora = require('ora')
const caches = Object.keys(require('./impls.js'))
const nth = caches.length
const { writeFileSync } = require('fs')

const types = {
  int: 'just an integer',
  strint: 'stringified integer',
  str: 'string that is not a number',
  numstr: 'a mix of integers and strings that look like them',
  pi: 'multiples of pi',
  float: 'floating point values',
  obj: 'an object with a single key',
  rand: 'random floating point number',
  sym: 'a Symbol object',
  longstr: 'a very long string',
  mix: 'a mix of all the types',
}

if (!process.env.TYPE) {
  const spawn = require('child_process').spawn
  const todo = Object.keys(types)
  const run = () =>
    new Promise(res => {
      const TYPE = todo.shift()
      if (!TYPE) return res()
      console.log(`${TYPE}: ${types[TYPE]}`)
      const child = spawn(process.execPath, [__filename], {
        env: { TYPE },
        stdio: 'inherit',
      })
      child.on('close', () => res(run()))
    })
  run()
} else {
  const spinner = ora(`Starting benchmark of ${nth} caches`).start(),
    promises = []

  caches.forEach((i, idx) => {
    promises.push(
      new Promise((resolve, reject) => {
        return (idx === 0 ? Promise.resolve() : promises[idx - 1])
          .then(() => {
            const worker = new Worker('worker.js')

            worker.onmessage = ev => {
              resolve(ev.data)
              worker.terminate()
            }

            worker.onerror = err => {
              reject(err)
              worker.terminate()
            }

            spinner.text = `Benchmarking ${
              idx + 1
            } of ${nth} caches [${i}]`
            worker.postMessage(i)
          })
          .catch(reject)
      })
    )
  })

  Promise.all(promises)
    .then(results => {
      const toMD = require('markdown-tables')
      const keysort = require('keysort')
      spinner.stop()
      const data = keysort(
        results.map(i => {
          const obj = JSON.parse(i)
          obj.score =
            obj.evict * 5 +
            obj.get2 * 5 +
            obj.get1 * 3 +
            obj.set * 2 +
            obj.update
          return obj
        }),
        'score desc'
      )

      const heading = 'name,set,get1,update,get2,evict,score'
      const csv =
        [heading]
          .concat(
            data.map(
              i =>
                `${i.name},${i.set},${i.get1},${i.update},${i.get2},${i.evict},${i.score}`
            )
          )
          .join('\n') + '\n'
      const resultsFile = `${__dirname}/results/${process.env.TYPE}.csv`
      writeFileSync(resultsFile, csv, 'utf8')
      console.log(toMD(csv))
    })
    .catch(err => {
      console.error(err.stack || err.message || err)
      process.exit(1)
    })
}
```

## File: `benchmark/make-deps.sh`
```bash
#!/usr/bin/env bash

deps=""
install=()
for name in $(cat impls.txt); do
  if [ "$name" = "lru-cache_CURRENT" ]; then
    continue
  fi
  dep=${name/_/@}
  deps="${deps}"'    "'"$name"'": "'"npm:$dep"$'",\n'
done

cat >package.json <<PJ
{
  "//": "Note: this file is programmatically generated, do not edit",
  "name": "bench-lru",
  "author": {
    "email": "dominic.tarr@gmail.com",
    "name": "Dominic Tarr",
    "url": "https://dominictarr.com"
  },
  "dependencies": {
    "lru-cache_CURRENT": "file:../",
${deps}    "tiny-worker": "^2.1.2",
    "ora": "^2.0.0",
    "keysort": "^1.0.2",
    "markdown-tables": "1.1",
    "retsu": "^3.0.1",
    "precise": "^1.1.0"
  },
  "scripts": {
    "benchmark": "NODE_ENV=production node index.js"
  },
  "license": "MIT"
}
PJ
rm package-lock.json
rm -rf node_modules
npm install "${install[@]}"
```

## File: `benchmark/profile.sh`
```bash
#!/usr/bin/env bash

mkdir -p profiles
rm -f isolate-*.log profile.txt
N=1000000 node --prof worker.js
d=profiles/$(date +%s)
node --prof-process isolate-*.log > $d
ln ${PWD}/$d profile.txt
cat profile.txt
```

## File: `benchmark/worker.js`
```javascript
'use strict'

const precise = require('precise')
const retsu = require('retsu')
const dir = process.env.__LRU_BENCH_DIR || __dirname
const caches = require(dir + '/impls.js')
const num = +process.env.N || 10_000
const evict = num * 2
const times = 10
const x = 1e6
const dataOrder = []
const data1 = new Array(evict)
const data2 = new Array(evict)
const data3 = new Array(evict)

const typeGen = {
  numstr: z => (z % 2 === 0 ? z : String(z + 1)),
  pi: z => z * Math.PI,
  float: z => z + z / (evict + 1),
  obj: z => ({ z }),
  strint: z => String(z),
  str: z => 'foo' + z + 'bar',
  rand: z => z * Math.random(),
  sym: z => Symbol(String(z)),
  longstr: z => z + 'z'.repeat(1024 * 4),
  int: z => z,
  mix: z => typeGen[typeKeys[z % (typeKeys.length - 1)]](z),
}
const typeKeys = Object.keys(typeGen)

;(function seed() {
  let z = -1

  const t = process.env.TYPE || 'mix'
  while (++z < evict) {
    const x = typeGen[t](z)
    data1[z] = [x, Math.floor(Math.random() * 1e7)]
    dataOrder.push(z)
  }

  // shuffle up the key orders, so we're not just walking down the list.
  for (const key of dataOrder.sort(() => Math.random() - 0.5)) {
    data2[key] = [data1[key][0], Math.random() * 1e7]
  }

  for (const key of dataOrder.sort(() => Math.random() - 0.5)) {
    data3[key] = data1[key]
  }
})()

const runTest = id => {
  const time = {
    set: [],
    get1: [],
    update: [],
    get2: [],
    evict: [],
  }
  const results = {
    name: id,
    set: 0,
    get1: 0,
    update: 0,
    get2: 0,
    evict: 0,
  }

  let n = -1

  // super rudimentary correctness check
  // make sure that 5 puts get back the same 5 items we put
  // ignore stderr, some caches are complainy about some keys
  let error = console.error
  console.error = () => {}
  try {
    const s = Math.max(5, Math.min(Math.floor(num / 2), 50))
    const m = Math.min(s * 5, num)
    const lru = caches[id](s)
    for (let i = 0; i < s; i++) lru.set(data1[i][0], data1[i][1])
    for (let i = 0; i < s; i++) {
      if (lru.get(data1[i][0]) !== data1[i][1]) {
        if (!process.stdout.isTTY) process.stderr.write(id)
        error(' failed correctness check at key=%j', data1[i][0])
        postMessage(
          JSON.stringify({
            name: id,
            set: 0,
            get1: 0,
            update: 0,
            get2: 0,
            evict: 0,
          })
        )
        process.exit(1)
      }
    }
    if (!/^just a/.test(id) && !/unbounded$/.test(id)) {
      for (let i = s + 1; i < m; i++)
        lru.set(data1[i][0], data1[i][1])
      if (lru.get(data1[0][0])) {
        if (!process.stdout.isTTY) process.stderr.write(id)
        error(' failed eviction correctness check')
        postMessage(
          JSON.stringify({
            name: id,
            set: 0,
            get1: 0,
            update: 0,
            get2: 0,
            evict: 0,
          })
        )
        process.exit(1)
      }
    }
    lru.set('__proto__', { [__filename]: 'pwned' })
    if (lru.get(__filename)) {
      error(' failed prototype pollution check')
      if (!/^just a/.test(id)) {
        postMessage(
          JSON.stringify({
            name: id,
            set: 0,
            get1: 0,
            update: 0,
            get2: 0,
            evict: 0,
          })
        )
        process.exit(1)
      }
    }
  } catch (er) {
    if (!process.stdout.isTTY) process.stderr.write(id)
    error(' failed correctness check', er.stack)
    postMessage(
      JSON.stringify({
        name: id,
        set: 0,
        get1: 0,
        update: 0,
        get2: 0,
        evict: 0,
      })
    )
    process.exit(1)
  }

  console.error = error

  while (++n < times) {
    const lru = caches[id](num)
    const stimer = precise().start()
    for (let i = 0; i < num; i++) lru.set(data1[i][0], data1[i][1])
    time.set.push(stimer.stop().diff() / x)

    const gtimer = precise().start()
    for (let i = 0; i < num; i++) lru.get(data1[i][0])
    time.get1.push(gtimer.stop().diff() / x)

    const utimer = precise().start()
    for (let i = 0; i < num; i++) lru.set(data2[i][0], data2[i][1])
    time.update.push(utimer.stop().diff() / x)

    const g2timer = precise().start()
    for (let i = 0; i < num; i++) lru.get(data3[i][0])
    time.get2.push(g2timer.stop().diff() / x)

    const etimer = precise().start()
    for (let i = num; i < evict; i++)
      lru.set(data1[i][0], data1[i][1])
    time.evict.push(etimer.stop().diff() / x)
  }

  ;['set', 'get1', 'update', 'get2', 'evict'].forEach(i => {
    results[i] = Number(
      (num / retsu.median(time[i]).toFixed(2)).toFixed(0)
    )
  })

  postMessage(JSON.stringify(results))
}

if (typeof self !== 'undefined') {
  self.onmessage = ev => runTest(ev.data)
} else {
  global.postMessage = console.log
  runTest('lru-cache_CURRENT')
}
```

## File: `scripts/.gitignore`
```
heapdump-*
node_modules
```

## File: `scripts/benchmark-results-typedoc.sh`
```bash
#!/usr/bin/env bash
set -x
set -e
mkdir -p docs/benchmark/results
cp -r benchmark/results/* docs/benchmark/results/
echo '<html><title>benchmark results overview</title>' > docs/benchmark/index.html
echo '<body>' >> docs/benchmark/index.html
echo '<p><a href="results/index.html">raw CSV results</a></p>' >> docs/benchmark/index.html
marked < benchmark/results.md >> docs/benchmark/index.html
echo '<html>' > docs/benchmark/results/index.html
echo '<title>benchmark results</title>' >> docs/benchmark/results/index.html
echo '<body><ul>' >> docs/benchmark/results/index.html
ls docs/benchmark/results | while read p; do
  f=$(basename "$p")
  echo '<li><a href="'$f'">'$f'</a></li>' >> docs/benchmark/results/index.html
done
echo '</ul></body></html>' >> docs/benchmark/results/index.html
```

## File: `scripts/package.json`
```json
{
  "dependencies": {
    "heapdump": "^0.3.15"
  }
}
```

## File: `scripts/transpile-to-esm.js`
```javascript
#!/usr/bin/env node

const { readFileSync, writeFileSync } = require('fs')
const { resolve } = require('path')
const cjs = readFileSync(resolve(__dirname, '../index.js'), 'utf8')
const esm = cjs.replace(/module.exports\s*=\s*/, 'export default ')
writeFileSync(resolve(__dirname, '../index.mjs'), esm, 'utf8')
```

## File: `src/index.ts`
```typescript
/**
 * @module LRUCache
 */

// module-private names and types
// this provides the default Perf object source.
// it can be passed in via configuration to override it
// for a single LRU object.
export type Perf = { now: () => number }
const defaultPerf: Perf =
  (
    typeof performance === 'object' &&
    performance &&
    typeof performance.now === 'function'
  ) ?
    performance
  : Date

const warned = new Set<string>()

// either a function or a class
type ForC = ((...a: any[]) => any) | { new (...a: any[]): any }

/* c8 ignore start */
const PROCESS = (
  typeof process === 'object' && !!process ?
    process
  : {}) as { [k: string]: any }
/* c8 ignore start */

const emitWarning = (
  msg: string,
  type: string,
  code: string,
  fn: ForC,
) => {
  typeof PROCESS.emitWarning === 'function' ?
    PROCESS.emitWarning(msg, type, code, fn)
  : console.error(`[${code}] ${type}: ${msg}`)
}

let AC = globalThis.AbortController
let AS = globalThis.AbortSignal

/* c8 ignore start */
if (typeof AC === 'undefined') {
  //@ts-ignore
  AS = class AbortSignal {
    onabort?: (...a: any[]) => any
    _onabort: ((...a: any[]) => any)[] = []
    reason?: any
    aborted: boolean = false
    addEventListener(_: string, fn: (...a: any[]) => any) {
      this._onabort.push(fn)
    }
  }
  //@ts-ignore
  AC = class AbortController {
    constructor() {
      warnACPolyfill()
    }
    signal = new AS()
    abort(reason: any) {
      if (this.signal.aborted) return
      //@ts-ignore
      this.signal.reason = reason
      //@ts-ignore
      this.signal.aborted = true
      //@ts-ignore
      for (const fn of this.signal._onabort) {
        fn(reason)
      }
      this.signal.onabort?.(reason)
    }
  }
  let printACPolyfillWarning =
    PROCESS.env?.LRU_CACHE_IGNORE_AC_WARNING !== '1'
  const warnACPolyfill = () => {
    if (!printACPolyfillWarning) return
    printACPolyfillWarning = false
    emitWarning(
      'AbortController is not defined. If using lru-cache in ' +
        'node 14, load an AbortController polyfill from the ' +
        '`node-abort-controller` package. A minimal polyfill is ' +
        'provided for use by LRUCache.fetch(), but it should not be ' +
        'relied upon in other contexts (eg, passing it to other APIs that ' +
        'use AbortController/AbortSignal might have undesirable effects). ' +
        'You may disable this with LRU_CACHE_IGNORE_AC_WARNING=1 in the env.',
      'NO_ABORT_CONTROLLER',
      'ENOTSUP',
      warnACPolyfill,
    )
  }
}
/* c8 ignore stop */

const shouldWarn = (code: string) => !warned.has(code)

const TYPE = Symbol('type')
export type PosInt = number & { [TYPE]: 'Positive Integer' }
export type Index = number & { [TYPE]: 'LRUCache Index' }

const isPosInt = (n: any): n is PosInt =>
  n && n === Math.floor(n) && n > 0 && isFinite(n)

export type UintArray = Uint8Array | Uint16Array | Uint32Array
export type NumberArray = UintArray | number[]

/* c8 ignore start */
// This is a little bit ridiculous, tbh.
// The maximum array length is 2^32-1 or thereabouts on most JS impls.
// And well before that point, you're caching the entire world, I mean,
// that's ~32GB of just integers for the next/prev links, plus whatever
// else to hold that many keys and values.  Just filling the memory with
// zeroes at init time is brutal when you get that big.
// But why not be complete?
// Maybe in the future, these limits will have expanded.
const getUintArray = (max: number) =>
  !isPosInt(max) ? null
  : max <= Math.pow(2, 8) ? Uint8Array
  : max <= Math.pow(2, 16) ? Uint16Array
  : max <= Math.pow(2, 32) ? Uint32Array
  : max <= Number.MAX_SAFE_INTEGER ? ZeroArray
  : null
/* c8 ignore stop */

class ZeroArray extends Array<number> {
  constructor(size: number) {
    super(size)
    this.fill(0)
  }
}
export type { ZeroArray }
export type { Stack }

export type StackLike = Stack | Index[]
class Stack {
  heap: NumberArray
  length: number
  // private constructor
  static #constructing: boolean = false
  static create(max: number): StackLike {
    const HeapCls = getUintArray(max)
    if (!HeapCls) return []
    Stack.#constructing = true
    const s = new Stack(max, HeapCls)
    Stack.#constructing = false
    return s
  }
  constructor(max: number, HeapCls: { new (n: number): NumberArray }) {
    /* c8 ignore start */
    if (!Stack.#constructing) {
      throw new TypeError('instantiate Stack using Stack.create(n)')
    }
    /* c8 ignore stop */
    this.heap = new HeapCls(max)
    this.length = 0
  }
  push(n: Index) {
    this.heap[this.length++] = n
  }
  pop(): Index {
    return this.heap[--this.length] as Index
  }
}

/**
 * Promise representing an in-progress {@link LRUCache#fetch} call
 */
export type BackgroundFetch<V> = Promise<V | undefined> & {
  __returned: BackgroundFetch<V> | undefined
  __abortController: AbortController
  __staleWhileFetching: V | undefined
}

export type DisposeTask<K, V> = [
  value: V,
  key: K,
  reason: LRUCache.DisposeReason,
]

export namespace LRUCache {
  /**
   * An integer greater than 0, reflecting the calculated size of items
   */
  export type Size = number

  /**
   * Integer greater than 0, representing some number of milliseconds, or the
   * time at which a TTL started counting from.
   */
  export type Milliseconds = number

  /**
   * An integer greater than 0, reflecting a number of items
   */
  export type Count = number

  /**
   * The reason why an item was removed from the cache, passed
   * to the {@link Disposer} methods.
   *
   * - `evict`: The item was evicted because it is the least recently used,
   *   and the cache is full.
   * - `set`: A new value was set, overwriting the old value being disposed.
   * - `delete`: The item was explicitly deleted, either by calling
   *   {@link LRUCache#delete}, {@link LRUCache#clear}, or
   *   {@link LRUCache#set} with an undefined value.
   * - `expire`: The item was removed due to exceeding its TTL.
   * - `fetch`: A {@link OptionsBase#fetchMethod} operation returned
   *   `undefined` or was aborted, causing the item to be deleted.
   */
  export type DisposeReason =
    | 'evict'
    | 'set'
    | 'delete'
    | 'expire'
    | 'fetch'
  /**
   * A method called upon item removal, passed as the
   * {@link OptionsBase.dispose} and/or
   * {@link OptionsBase.disposeAfter} options.
   */
  export type Disposer<K, V> = (
    value: V,
    key: K,
    reason: DisposeReason,
  ) => void

  /**
   * The reason why an item was added to the cache, passed
   * to the {@link Inserter} methods.
   *
   * - `add`: the item was not found in the cache, and was added
   * - `update`: the item was in the cache, with the same value provided
   * - `replace`: the item was in the cache, and replaced
   */
  export type InsertReason = 'add' | 'update' | 'replace'

  /**
   * A method called upon item insertion, passed as the
   * {@link OptionsBase.insert}
   */
  export type Inserter<K, V> = (
    value: V,
    key: K,
    reason: InsertReason,
  ) => void

  /**
   * A function that returns the effective calculated size
   * of an entry in the cache.
   */
  export type SizeCalculator<K, V> = (value: V, key: K) => Size

  /**
   * Options provided to the
   * {@link OptionsBase.fetchMethod} function.
   */
  export interface FetcherOptions<K, V, FC = unknown> {
    signal: AbortSignal
    options: FetcherFetchOptions<K, V, FC>
    /**
     * Object provided in the {@link FetchOptions.context} option to
     * {@link LRUCache#fetch}
     */
    context: FC
  }

  /**
   * Occasionally, it may be useful to track the internal behavior of the
   * cache, particularly for logging, debugging, or for behavior within the
   * `fetchMethod`. To do this, you can pass a `status` object to the
   * {@link LRUCache#fetch}, {@link LRUCache#get}, {@link LRUCache#set},
   * {@link LRUCache#memo}, and {@link LRUCache#has} methods.
   *
   * The `status` option should be a plain JavaScript object. The following
   * fields will be set on it appropriately, depending on the situation.
   */
  export interface Status<V> {
    /**
     * The status of a set() operation.
     *
     * - add: the item was not found in the cache, and was added
     * - update: the item was in the cache, with the same value provided
     * - replace: the item was in the cache, and replaced
     * - miss: the item was not added to the cache for some reason
     */
    set?: 'add' | 'update' | 'replace' | 'miss'

    /**
     * the ttl stored for the item, or undefined if ttls are not used.
     */
    ttl?: Milliseconds

    /**
     * the start time for the item, or undefined if ttls are not used.
     */
    start?: Milliseconds

    /**
     * The timestamp used for TTL calculation
     */
    now?: Milliseconds

    /**
     * the remaining ttl for the item, or undefined if ttls are not used.
     */
    remainingTTL?: Milliseconds

    /**
     * The calculated size for the item, if sizes are used.
     */
    entrySize?: Size

    /**
     * The total calculated size of the cache, if sizes are used.
     */
    totalCalculatedSize?: Size

    /**
     * A flag indicating that the item was not stored, due to exceeding the
     * {@link OptionsBase.maxEntrySize}
     */
    maxEntrySizeExceeded?: true

    /**
     * The old value, specified in the case of `set:'update'` or
     * `set:'replace'`
     */
    oldValue?: V

    /**
     * The results of a {@link LRUCache#has} operation
     *
     * - hit: the item was found in the cache
     * - stale: the item was found in the cache, but is stale
     * - miss: the item was not found in the cache
     */
    has?: 'hit' | 'stale' | 'miss'

    /**
     * The status of a {@link LRUCache#fetch} operation.
     * Note that this can change as the underlying fetch() moves through
     * various states.
     *
     * - inflight: there is another fetch() for this key which is in process
     * - get: there is no {@link OptionsBase.fetchMethod}, so
     *   {@link LRUCache#get} was called.
     * - miss: the item is not in cache, and will be fetched.
     * - hit: the item is in the cache, and was resolved immediately.
     * - stale: the item is in the cache, but stale.
     * - refresh: the item is in the cache, and not stale, but
     *   {@link FetchOptions.forceRefresh} was specified.
     */
    fetch?: 'get' | 'inflight' | 'miss' | 'hit' | 'stale' | 'refresh'

    /**
     * The {@link OptionsBase.fetchMethod} was called
     */
    fetchDispatched?: true

    /**
     * The cached value was updated after a successful call to
     * {@link OptionsBase.fetchMethod}
     */
    fetchUpdated?: true

    /**
     * The reason for a fetch() rejection.  Either the error raised by the
     * {@link OptionsBase.fetchMethod}, or the reason for an
     * AbortSignal.
     */
    fetchError?: Error

    /**
     * The fetch received an abort signal
     */
    fetchAborted?: true

    /**
     * The abort signal received was ignored, and the fetch was allowed to
     * continue.
     */
    fetchAbortIgnored?: true

    /**
     * The fetchMethod promise resolved successfully
     */
    fetchResolved?: true

    /**
     * The fetchMethod promise was rejected
     */
    fetchRejected?: true

    /**
     * The status of a {@link LRUCache#get} operation.
     *
     * - fetching: The item is currently being fetched.  If a previous value
     *   is present and allowed, that will be returned.
     * - stale: The item is in the cache, and is stale.
     * - hit: the item is in the cache
     * - miss: the item is not in the cache
     */
    get?: 'stale' | 'hit' | 'miss'

    /**
     * A fetch or get operation returned a stale value.
     */
    returnedStale?: true
  }

  /**
   * options which override the options set in the LRUCache constructor
   * when calling {@link LRUCache#fetch}.
   *
   * This is the union of {@link GetOptions} and {@link SetOptions}, plus
   * {@link OptionsBase.noDeleteOnFetchRejection},
   * {@link OptionsBase.allowStaleOnFetchRejection},
   * {@link FetchOptions.forceRefresh}, and
   * {@link FetcherOptions.context}
   *
   * Any of these may be modified in the {@link OptionsBase.fetchMethod}
   * function, but the {@link GetOptions} fields will of course have no
   * effect, as the {@link LRUCache#get} call already happened by the time
   * the fetchMethod is called.
   */
  export interface FetcherFetchOptions<K, V, FC = unknown>
    extends Pick<
      OptionsBase<K, V, FC>,
      | 'allowStale'
      | 'updateAgeOnGet'
      | 'noDeleteOnStaleGet'
      | 'sizeCalculation'
      | 'ttl'
      | 'noDisposeOnSet'
      | 'noUpdateTTL'
      | 'noDeleteOnFetchRejection'
      | 'allowStaleOnFetchRejection'
      | 'ignoreFetchAbort'
      | 'allowStaleOnFetchAbort'
    > {
    status?: Status<V>
    size?: Size
  }

  /**
   * Options that may be passed to the {@link LRUCache#fetch} method.
   */
  export interface FetchOptions<K, V, FC>
    extends FetcherFetchOptions<K, V, FC> {
    /**
     * Set to true to force a re-load of the existing data, even if it
     * is not yet stale.
     */
    forceRefresh?: boolean
    /**
     * Context provided to the {@link OptionsBase.fetchMethod} as
     * the {@link FetcherOptions.context} param.
     *
     * If the FC type is specified as unknown (the default),
     * undefined or void, then this is optional.  Otherwise, it will
     * be required.
     */
    context?: FC
    signal?: AbortSignal
    status?: Status<V>
  }
  /**
   * Options provided to {@link LRUCache#fetch} when the FC type is something
   * other than `unknown`, `undefined`, or `void`
   */
  export interface FetchOptionsWithContext<K, V, FC>
    extends FetchOptions<K, V, FC> {
    context: FC
  }
  /**
   * Options provided to {@link LRUCache#fetch} when the FC type is
   * `undefined` or `void`
   */
  export interface FetchOptionsNoContext<K, V>
    extends FetchOptions<K, V, undefined> {
    context?: undefined
  }

  export interface MemoOptions<K, V, FC = unknown>
    extends Pick<
      OptionsBase<K, V, FC>,
      | 'allowStale'
      | 'updateAgeOnGet'
      | 'noDeleteOnStaleGet'
      | 'sizeCalculation'
      | 'ttl'
      | 'noDisposeOnSet'
      | 'noUpdateTTL'
      | 'noDeleteOnFetchRejection'
      | 'allowStaleOnFetchRejection'
      | 'ignoreFetchAbort'
      | 'allowStaleOnFetchAbort'
    > {
    /**
     * Set to true to force a re-load of the existing data, even if it
     * is not yet stale.
     */
    forceRefresh?: boolean
    /**
     * Context provided to the {@link OptionsBase.memoMethod} as
     * the {@link MemoizerOptions.context} param.
     *
     * If the FC type is specified as unknown (the default),
     * undefined or void, then this is optional.  Otherwise, it will
     * be required.
     */
    context?: FC
    status?: Status<V>
  }
  /**
   * Options provided to {@link LRUCache#memo} when the FC type is something
   * other than `unknown`, `undefined`, or `void`
   */
  export interface MemoOptionsWithContext<K, V, FC>
    extends MemoOptions<K, V, FC> {
    context: FC
  }
  /**
   * Options provided to {@link LRUCache#memo} when the FC type is
   * `undefined` or `void`
   */
  export interface MemoOptionsNoContext<K, V>
    extends MemoOptions<K, V, undefined> {
    context?: undefined
  }

  /**
   * Options provided to the
   * {@link OptionsBase.memoMethod} function.
   */
  export interface MemoizerOptions<K, V, FC = unknown> {
    options: MemoizerMemoOptions<K, V, FC>
    /**
     * Object provided in the {@link MemoOptions.context} option to
     * {@link LRUCache#memo}
     */
    context: FC
  }

  /**
   * options which override the options set in the LRUCache constructor
   * when calling {@link LRUCache#memo}.
   *
   * This is the union of {@link GetOptions} and {@link SetOptions}, plus
   * {@link MemoOptions.forceRefresh}, and
   * {@link MemoOptions.context}
   *
   * Any of these may be modified in the {@link OptionsBase.memoMethod}
   * function, but the {@link GetOptions} fields will of course have no
   * effect, as the {@link LRUCache#get} call already happened by the time
   * the memoMethod is called.
   */
  export interface MemoizerMemoOptions<K, V, FC = unknown>
    extends Pick<
      OptionsBase<K, V, FC>,
      | 'allowStale'
      | 'updateAgeOnGet'
      | 'noDeleteOnStaleGet'
      | 'sizeCalculation'
      | 'ttl'
      | 'noDisposeOnSet'
      | 'noUpdateTTL'
    > {
    status?: Status<V>
    size?: Size
    start?: Milliseconds
  }

  /**
   * Options that may be passed to the {@link LRUCache#has} method.
   */
  export interface HasOptions<K, V, FC>
    extends Pick<OptionsBase<K, V, FC>, 'updateAgeOnHas'> {
    status?: Status<V>
  }

  /**
   * Options that may be passed to the {@link LRUCache#get} method.
   */
  export interface GetOptions<K, V, FC>
    extends Pick<
      OptionsBase<K, V, FC>,
      'allowStale' | 'updateAgeOnGet' | 'noDeleteOnStaleGet'
    > {
    status?: Status<V>
  }

  /**
   * Options that may be passed to the {@link LRUCache#peek} method.
   */
  export interface PeekOptions<K, V, FC>
    extends Pick<OptionsBase<K, V, FC>, 'allowStale'> {}

  /**
   * Options that may be passed to the {@link LRUCache#set} method.
   */
  export interface SetOptions<K, V, FC>
    extends Pick<
      OptionsBase<K, V, FC>,
      'sizeCalculation' | 'ttl' | 'noDisposeOnSet' | 'noUpdateTTL'
    > {
    /**
     * If size tracking is enabled, then setting an explicit size
     * in the {@link LRUCache#set} call will prevent calling the
     * {@link OptionsBase.sizeCalculation} function.
     */
    size?: Size
    /**
     * If TTL tracking is enabled, then setting an explicit start
     * time in the {@link LRUCache#set} call will override the
     * default time from `performance.now()` or `Date.now()`.
     *
     * Note that it must be a valid value for whichever time-tracking
     * method is in use.
     */
    start?: Milliseconds
    status?: Status<V>
  }

  /**
   * The type signature for the {@link OptionsBase.fetchMethod} option.
   */
  export type Fetcher<K, V, FC = unknown> = (
    key: K,
    staleValue: V | undefined,
    options: FetcherOptions<K, V, FC>,
  ) => Promise<V | undefined | void> | V | undefined | void

  /**
   * the type signature for the {@link OptionsBase.memoMethod} option.
   */
  export type Memoizer<K, V, FC = unknown> = (
    key: K,
    staleValue: V | undefined,
    options: MemoizerOptions<K, V, FC>,
  ) => V

  /**
   * Options which may be passed to the {@link LRUCache} constructor.
   *
   * Most of these may be overridden in the various options that use
   * them.
   *
   * Despite all being technically optional, the constructor requires that
   * a cache is at minimum limited by one or more of {@link OptionsBase.max},
   * {@link OptionsBase.ttl}, or {@link OptionsBase.maxSize}.
   *
   * If {@link OptionsBase.ttl} is used alone, then it is strongly advised
   * (and in fact required by the type definitions here) that the cache
   * also set {@link OptionsBase.ttlAutopurge}, to prevent potentially
   * unbounded storage.
   *
   * All options are also available on the {@link LRUCache} instance, making
   * it safe to pass an LRUCache instance as the options argumemnt to
   * make another empty cache of the same type.
   *
   * Some options are marked as read-only, because changing them after
   * instantiation is not safe. Changing any of the other options will of
   * course only have an effect on subsequent method calls.
   */
  export interface OptionsBase<K, V, FC> {
    /**
     * The maximum number of items to store in the cache before evicting
     * old entries. This is read-only on the {@link LRUCache} instance,
     * and may not be overridden.
     *
     * If set, then storage space will be pre-allocated at construction
     * time, and the cache will perform significantly faster.
     *
     * Note that significantly fewer items may be stored, if
     * {@link OptionsBase.maxSize} and/or {@link OptionsBase.ttl} are also
     * set.
     *
     * **It is strongly recommended to set a `max` to prevent unbounded growth
     * of the cache.**
     */
    max?: Count

    /**
     * Max time in milliseconds for items to live in cache before they are
     * considered stale.  Note that stale items are NOT preemptively removed by
     * default, and MAY live in the cache, contributing to its LRU max, long
     * after they have expired, unless {@link OptionsBase.ttlAutopurge} is
     * set.
     *
     * If set to `0` (the default value), then that means "do not track
     * TTL", not "expire immediately".
     *
     * Also, as this cache is optimized for LRU/MRU operations, some of
     * the staleness/TTL checks will reduce performance, as they will incur
     * overhead by deleting items.
     *
     * This is not primarily a TTL cache, and does not make strong TTL
     * guarantees. There is no pre-emptive pruning of expired items, but you
     * _may_ set a TTL on the cache, and it will treat expired items as missing
     * when they are fetched, and delete them.
     *
     * Optional, but must be a non-negative integer in ms if specified.
     *
     * This may be overridden by passing an options object to `cache.set()`.
     *
     * At least one of `max`, `maxSize`, or `TTL` is required. This must be a
     * positive integer if set.
     *
     * Even if ttl tracking is enabled, **it is strongly recommended to set a
     * `max` to prevent unbounded growth of the cache.**
     *
     * If ttl tracking is enabled, and `max` and `maxSize` are not set,
     * and `ttlAutopurge` is not set, then a warning will be emitted
     * cautioning about the potential for unbounded memory consumption.
     * (The TypeScript definitions will also discourage this.)
     */
    ttl?: Milliseconds

    /**
     * Minimum amount of time in ms in which to check for staleness.
     * Defaults to 1, which means that the current time is checked
     * at most once per millisecond.
     *
     * Set to 0 to check the current time every time staleness is tested.
     * (This reduces performance, and is theoretically unnecessary.)
     *
     * Setting this to a higher value will improve performance somewhat
     * while using ttl tracking, albeit at the expense of keeping stale
     * items around a bit longer than their TTLs would indicate.
     *
     * @default 1
     */
    ttlResolution?: Milliseconds

    /**
     * Preemptively remove stale items from the cache.
     *
     * Note that this may *significantly* degrade performance, especially if
     * the cache is storing a large number of items. It is almost always best
     * to just leave the stale items in the cache, and let them fall out as new
     * items are added.
     *
     * Note that this means that {@link OptionsBase.allowStale} is a bit
     * pointless, as stale items will be deleted almost as soon as they
     * expire.
     *
     * Use with caution!
     */
    ttlAutopurge?: boolean

    /**
     * When using time-expiring entries with `ttl`, setting this to `true` will
     * make each item's age reset to 0 whenever it is retrieved from cache with
     * {@link LRUCache#get}, causing it to not expire. (It can still fall out
     * of cache based on recency of use, of course.)
     *
     * Has no effect if {@link OptionsBase.ttl} is not set.
     *
     * This may be overridden by passing an options object to `cache.get()`.
     */
    updateAgeOnGet?: boolean

    /**
     * When using time-expiring entries with `ttl`, setting this to `true` will
     * make each item's age reset to 0 whenever its presence in the cache is
     * checked with {@link LRUCache#has}, causing it to not expire. (It can
     * still fall out of cache based on recency of use, of course.)
     *
     * Has no effect if {@link OptionsBase.ttl} is not set.
     */
    updateAgeOnHas?: boolean

    /**
     * Allow {@link LRUCache#get} and {@link LRUCache#fetch} calls to return
     * stale data, if available.
     *
     * By default, if you set `ttl`, stale items will only be deleted from the
     * cache when you `get(key)`. That is, it's not preemptively pruning items,
     * unless {@link OptionsBase.ttlAutopurge} is set.
     *
     * If you set `allowStale:true`, it'll return the stale value *as well as*
     * deleting it. If you don't set this, then it'll return `undefined` when
     * you try to get a stale entry.
     *
     * Note that when a stale entry is fetched, _even if it is returned due to
     * `allowStale` being set_, it is removed from the cache immediately. You
     * can suppress this behavior by setting
     * {@link OptionsBase.noDeleteOnStaleGet}, either in the constructor, or in
     * the options provided to {@link LRUCache#get}.
     *
     * This may be overridden by passing an options object to `cache.get()`.
     * The `cache.has()` method will always return `false` for stale items.
     *
     * Only relevant if a ttl is set.
     */
    allowStale?: boolean

    /**
     * Function that is called on items when they are dropped from the
     * cache, as `dispose(value, key, reason)`.
     *
     * This can be handy if you want to close file descriptors or do
     * other cleanup tasks when items are no longer stored in the cache.
     *
     * **NOTE**: It is called _before_ the item has been fully removed
     * from the cache, so if you want to put it right back in, you need
     * to wait until the next tick. If you try to add it back in during
     * the `dispose()` function call, it will break things in subtle and
     * weird ways.
     *
     * Unlike several other options, this may _not_ be overridden by
     * passing an option to `set()`, for performance reasons.
     *
     * The `reason` will be one of the following strings, corresponding
     * to the reason for the item's deletion:
     *
     * - `evict` Item was evicted to make space for a new addition
     * - `set` Item was overwritten by a new value
     * - `expire` Item expired its TTL
     * - `fetch` Item was deleted due to a failed or aborted fetch, or a
     *   fetchMethod returning `undefined.
     * - `delete` Item was removed by explicit `cache.delete(key)`,
     *   `cache.clear()`, or `cache.set(key, undefined)`.
     */
    dispose?: Disposer<K, V>

    /**
     * Function that is called when new items are inserted into the cache,
     * as `onInsert(value, key, reason)`.
     *
     * This can be useful if you need to perform actions when an item is
     * added, such as logging or tracking insertions.
     *
     * Unlike some other options, this may _not_ be overridden by passing
     * an option to `set()`, for performance and consistency reasons.
     */
    onInsert?: Inserter<K, V>

    /**
     * The same as {@link OptionsBase.dispose}, but called *after* the entry
     * is completely removed and the cache is once again in a clean state.
     *
     * It is safe to add an item right back into the cache at this point.
     * However, note that it is *very* easy to inadvertently create infinite
     * recursion this way.
     */
    disposeAfter?: Disposer<K, V>

    /**
     * Set to true to suppress calling the
     * {@link OptionsBase.dispose} function if the entry key is
     * still accessible within the cache.
     *
     * This may be overridden by passing an options object to
     * {@link LRUCache#set}.
     *
     * Only relevant if `dispose` or `disposeAfter` are set.
     */
    noDisposeOnSet?: boolean

    /**
     * Boolean flag to tell the cache to not update the TTL when setting a new
     * value for an existing key (ie, when updating a value rather than
     * inserting a new value).  Note that the TTL value is _always_ set (if
     * provided) when adding a new entry into the cache.
     *
     * Has no effect if a {@link OptionsBase.ttl} is not set.
     *
     * May be passed as an option to {@link LRUCache#set}.
     */
    noUpdateTTL?: boolean

    /**
     * Set to a positive integer to track the sizes of items added to the
     * cache, and automatically evict items in order to stay below this size.
     * Note that this may result in fewer than `max` items being stored.
     *
     * Attempting to add an item to the cache whose calculated size is greater
     * that this amount will be a no-op. The item will not be cached, and no
     * other items will be evicted.
     *
     * Optional, must be a positive integer if provided.
     *
     * Sets `maxEntrySize` to the same value, unless a different value is
     * provided for `maxEntrySize`.
     *
     * At least one of `max`, `maxSize`, or `TTL` is required. This must be a
     * positive integer if set.
     *
     * Even if size tracking is enabled, **it is strongly recommended to set a
     * `max` to prevent unbounded growth of the cache.**
     *
     * Note also that size tracking can negatively impact performance,
     * though for most cases, only minimally.
     */
    maxSize?: Size

    /**
     * The maximum allowed size for any single item in the cache.
     *
     * If a larger item is passed to {@link LRUCache#set} or returned by a
     * {@link OptionsBase.fetchMethod} or {@link OptionsBase.memoMethod}, then
     * it will not be stored in the cache.
     *
     * Attempting to add an item whose calculated size is greater than
     * this amount will not cache the item or evict any old items, but
     * WILL delete an existing value if one is already present.
     *
     * Optional, must be a positive integer if provided. Defaults to
     * the value of `maxSize` if provided.
     */
    maxEntrySize?: Size

    /**
     * A function that returns a number indicating the item's size.
     *
     * Requires {@link OptionsBase.maxSize} to be set.
     *
     * If not provided, and {@link OptionsBase.maxSize} or
     * {@link OptionsBase.maxEntrySize} are set, then all
     * {@link LRUCache#set} calls **must** provide an explicit
     * {@link SetOptions.size} or sizeCalculation param.
     */
    sizeCalculation?: SizeCalculator<K, V>

    /**
     * Method that provides the implementation for {@link LRUCache#fetch}
     *
     * ```ts
     * fetchMethod(key, staleValue, { signal, options, context })
     * ```
     *
     * If `fetchMethod` is not provided, then `cache.fetch(key)` is equivalent
     * to `Promise.resolve(cache.get(key))`.
     *
     * If at any time, `signal.aborted` is set to `true`, or if the
     * `signal.onabort` method is called, or if it emits an `'abort'` event
     * which you can listen to with `addEventListener`, then that means that
     * the fetch should be abandoned. This may be passed along to async
     * functions aware of AbortController/AbortSignal behavior.
     *
     * The `fetchMethod` should **only** return `undefined` or a Promise
     * resolving to `undefined` if the AbortController signaled an `abort`
     * event. In all other cases, it should return or resolve to a value
     * suitable for adding to the cache.
     *
     * The `options` object is a union of the options that may be provided to
     * `set()` and `get()`. If they are modified, then that will result in
     * modifying the settings to `cache.set()` when the value is resolved, and
     * in the case of
     * {@link OptionsBase.noDeleteOnFetchRejection} and
     * {@link OptionsBase.allowStaleOnFetchRejection}, the handling of
     * `fetchMethod` failures.
     *
     * For example, a DNS cache may update the TTL based on the value returned
     * from a remote DNS server by changing `options.ttl` in the `fetchMethod`.
     */
    fetchMethod?: Fetcher<K, V, FC>

    /**
     * Method that provides the implementation for {@link LRUCache#memo}
     */
    memoMethod?: Memoizer<K, V, FC>

    /**
     * Set to true to suppress the deletion of stale data when a
     * {@link OptionsBase.fetchMethod} returns a rejected promise.
     */
    noDeleteOnFetchRejection?: boolean

    /**
     * Do not delete stale items when they are retrieved with
     * {@link LRUCache#get}.
     *
     * Note that the `get` return value will still be `undefined`
     * unless {@link OptionsBase.allowStale} is true.
     *
     * When using time-expiring entries with `ttl`, by default stale
     * items will be removed from the cache when the key is accessed
     * with `cache.get()`.
     *
     * Setting this option will cause stale items to remain in the cache, until
     * they are explicitly deleted with `cache.delete(key)`, or retrieved with
     * `noDeleteOnStaleGet` set to `false`.
     *
     * This may be overridden by passing an options object to `cache.get()`.
     *
     * Only relevant if a ttl is used.
     */
    noDeleteOnStaleGet?: boolean

    /**
     * Set to true to allow returning stale data when a
     * {@link OptionsBase.fetchMethod} throws an error or returns a rejected
     * promise.
     *
     * This differs from using {@link OptionsBase.allowStale} in that stale
     * data will ONLY be returned in the case that the {@link LRUCache#fetch}
     * fails, not any other times.
     *
     * If a `fetchMethod` fails, and there is no stale value available, the
     * `fetch()` will resolve to `undefined`. Ie, all `fetchMethod` errors are
     * suppressed.
     *
     * Implies `noDeleteOnFetchRejection`.
     *
     * This may be set in calls to `fetch()`, or defaulted on the constructor,
     * or overridden by modifying the options object in the `fetchMethod`.
     */
    allowStaleOnFetchRejection?: boolean

    /**
     * Set to true to return a stale value from the cache when the
     * `AbortSignal` passed to the {@link OptionsBase.fetchMethod} dispatches
     * an `'abort'` event, whether user-triggered, or due to internal cache
     * behavior.
     *
     * Unless {@link OptionsBase.ignoreFetchAbort} is also set, the underlying
     * {@link OptionsBase.fetchMethod} will still be considered canceled, and
     * any value it returns will be ignored and not cached.
     *
     * Caveat: since fetches are aborted when a new value is explicitly
     * set in the cache, this can lead to fetch returning a stale value,
     * since that was the fallback value _at the moment the `fetch()` was
     * initiated_, even though the new updated value is now present in
     * the cache.
     *
     * For example:
     *
     * ```ts
     * const cache = new LRUCache<string, any>({
     *   ttl: 100,
     *   fetchMethod: async (url, oldValue, { signal }) =>  {
     *     const res = await fetch(url, { signal })
     *     return await res.json()
     *   }
     * })
     * cache.set('https://example.com/', { some: 'data' })
     * // 100ms go by...
     * const result = cache.fetch('https://example.com/')
     * cache.set('https://example.com/', { other: 'thing' })
     * console.log(await result) // { some: 'data' }
     * console.log(cache.get('https://example.com/')) // { other: 'thing' }
     * ```
     */
    allowStaleOnFetchAbort?: boolean

    /**
     * Set to true to ignore the `abort` event emitted by the `AbortSignal`
     * object passed to {@link OptionsBase.fetchMethod}, and still cache the
     * resulting resolution value, as long as it is not `undefined`.
     *
     * When used on its own, this means aborted {@link LRUCache#fetch} calls
     * are not immediately resolved or rejected when they are aborted, and
     * instead take the full time to await.
     *
     * When used with {@link OptionsBase.allowStaleOnFetchAbort}, aborted
     * {@link LRUCache#fetch} calls will resolve immediately to their stale
     * cached value or `undefined`, and will continue to process and eventually
     * update the cache when they resolve, as long as the resulting value is
     * not `undefined`, thus supporting a "return stale on timeout while
     * refreshing" mechanism by passing `AbortSignal.timeout(n)` as the signal.
     *
     * For example:
     *
     * ```ts
     * const c = new LRUCache({
     *   ttl: 100,
     *   ignoreFetchAbort: true,
     *   allowStaleOnFetchAbort: true,
     *   fetchMethod: async (key, oldValue, { signal }) => {
     *     // note: do NOT pass the signal to fetch()!
     *     // let's say this fetch can take a long time.
     *     const res = await fetch(`https://slow-backend-server/${key}`)
     *     return await res.json()
     *   },
     * })
     *
     * // this will return the stale value after 100ms, while still
     * // updating in the background for next time.
     * const val = await c.fetch('key', { signal: AbortSignal.timeout(100) })
     * ```
     *
     * **Note**: regardless of this setting, an `abort` event _is still
     * emitted on the `AbortSignal` object_, so may result in invalid results
     * when passed to other underlying APIs that use AbortSignals.
     *
     * This may be overridden in the {@link OptionsBase.fetchMethod} or the
     * call to {@link LRUCache#fetch}.
     */
    ignoreFetchAbort?: boolean

    /**
     * In some cases, you may want to swap out the performance/Date object
     * used for TTL tracking. This should almost certainly NOT be done in
     * production environments!
     *
     * This value defaults to `global.performance` if it has a `now()` method,
     * or the `global.Date` object otherwise.
     */
    perf?: Perf
  }

  export interface OptionsMaxLimit<K, V, FC>
    extends OptionsBase<K, V, FC> {
    max: Count
  }
  export interface OptionsTTLLimit<K, V, FC>
    extends OptionsBase<K, V, FC> {
    ttl: Milliseconds
    ttlAutopurge: boolean
  }
  export interface OptionsSizeLimit<K, V, FC>
    extends OptionsBase<K, V, FC> {
    maxSize: Size
  }

  /**
   * The valid safe options for the {@link LRUCache} constructor
   */
  export type Options<K, V, FC> =
    | OptionsMaxLimit<K, V, FC>
    | OptionsSizeLimit<K, V, FC>
    | OptionsTTLLimit<K, V, FC>

  /**
   * Entry objects used by {@link LRUCache#load} and {@link LRUCache#dump},
   * and returned by {@link LRUCache#info}.
   */
  export interface Entry<V> {
    value: V
    ttl?: Milliseconds
    size?: Size
    start?: Milliseconds
  }
}

/**
 * Default export, the thing you're using this module to get.
 *
 * The `K` and `V` types define the key and value types, respectively. The
 * optional `FC` type defines the type of the `context` object passed to
 * `cache.fetch()` and `cache.memo()`.
 *
 * Keys and values **must not** be `null` or `undefined`.
 *
 * All properties from the options object (with the exception of `max`,
 * `maxSize`, `fetchMethod`, `memoMethod`, `dispose` and `disposeAfter`) are
 * added as normal public members. (The listed options are read-only getters.)
 *
 * Changing any of these will alter the defaults for subsequent method calls.
 */
export class LRUCache<K extends {}, V extends {}, FC = unknown> {
  // options that cannot be changed without disaster
  readonly #max: LRUCache.Count
  readonly #maxSize: LRUCache.Size
  readonly #dispose?: LRUCache.Disposer<K, V>
  readonly #onInsert?: LRUCache.Inserter<K, V>
  readonly #disposeAfter?: LRUCache.Disposer<K, V>
  readonly #fetchMethod?: LRUCache.Fetcher<K, V, FC>
  readonly #memoMethod?: LRUCache.Memoizer<K, V, FC>
  readonly #perf: Perf

  /**
   * {@link LRUCache.OptionsBase.perf}
   */
  get perf() {
    return this.#perf
  }

  /**
   * {@link LRUCache.OptionsBase.ttl}
   */
  ttl: LRUCache.Milliseconds

  /**
   * {@link LRUCache.OptionsBase.ttlResolution}
   */
  ttlResolution: LRUCache.Milliseconds
  /**
   * {@link LRUCache.OptionsBase.ttlAutopurge}
   */
  ttlAutopurge: boolean
  /**
   * {@link LRUCache.OptionsBase.updateAgeOnGet}
   */
  updateAgeOnGet: boolean
  /**
   * {@link LRUCache.OptionsBase.updateAgeOnHas}
   */
  updateAgeOnHas: boolean
  /**
   * {@link LRUCache.OptionsBase.allowStale}
   */
  allowStale: boolean

  /**
   * {@link LRUCache.OptionsBase.noDisposeOnSet}
   */
  noDisposeOnSet: boolean
  /**
   * {@link LRUCache.OptionsBase.noUpdateTTL}
   */
  noUpdateTTL: boolean
  /**
   * {@link LRUCache.OptionsBase.maxEntrySize}
   */
  maxEntrySize: LRUCache.Size
  /**
   * {@link LRUCache.OptionsBase.sizeCalculation}
   */
  sizeCalculation?: LRUCache.SizeCalculator<K, V>
  /**
   * {@link LRUCache.OptionsBase.noDeleteOnFetchRejection}
   */
  noDeleteOnFetchRejection: boolean
  /**
   * {@link LRUCache.OptionsBase.noDeleteOnStaleGet}
   */
  noDeleteOnStaleGet: boolean
  /**
   * {@link LRUCache.OptionsBase.allowStaleOnFetchAbort}
   */
  allowStaleOnFetchAbort: boolean
  /**
   * {@link LRUCache.OptionsBase.allowStaleOnFetchRejection}
   */
  allowStaleOnFetchRejection: boolean
  /**
   * {@link LRUCache.OptionsBase.ignoreFetchAbort}
   */
  ignoreFetchAbort: boolean

  // computed properties
  #size: LRUCache.Count
  #calculatedSize: LRUCache.Size
  #keyMap: Map<K, Index>
  #keyList: (K | undefined)[]
  #valList: (V | BackgroundFetch<V> | undefined)[]
  #next: NumberArray
  #prev: NumberArray
  #head: Index
  #tail: Index
  #free: StackLike
  #disposed?: DisposeTask<K, V>[]
  #sizes?: ZeroArray
  #starts?: ZeroArray
  #ttls?: ZeroArray
  #autopurgeTimers?: (undefined | ReturnType<typeof setTimeout>)[]

  #hasDispose: boolean
  #hasFetchMethod: boolean
  #hasDisposeAfter: boolean
  #hasOnInsert: boolean

  /**
   * Do not call this method unless you need to inspect the
   * inner workings of the cache.  If anything returned by this
   * object is modified in any way, strange breakage may occur.
   *
   * These fields are private for a reason!
   *
   * @internal
   */
  static unsafeExposeInternals<
    K extends {},
    V extends {},
    FC extends unknown = unknown,
  >(c: LRUCache<K, V, FC>) {
    return {
      // properties
      starts: c.#starts,
      ttls: c.#ttls,
      autopurgeTimers: c.#autopurgeTimers,
      sizes: c.#sizes,
      keyMap: c.#keyMap as Map<K, number>,
      keyList: c.#keyList,
      valList: c.#valList,
      next: c.#next,
      prev: c.#prev,
      get head() {
        return c.#head
      },
      get tail() {
        return c.#tail
      },
      free: c.#free,
      // methods
      isBackgroundFetch: (p: any) => c.#isBackgroundFetch(p),
      backgroundFetch: (
        k: K,
        index: number | undefined,
        options: LRUCache.FetchOptions<K, V, FC>,
        context: any,
      ): BackgroundFetch<V> =>
        c.#backgroundFetch(
          k,
          index as Index | undefined,
          options,
          context,
        ),
      moveToTail: (index: number): void => c.#moveToTail(index as Index),
      indexes: (options?: { allowStale: boolean }) => c.#indexes(options),
      rindexes: (options?: { allowStale: boolean }) =>
        c.#rindexes(options),
      isStale: (index: number | undefined) => c.#isStale(index as Index),
    }
  }

  // Protected read-only members

  /**
   * {@link LRUCache.OptionsBase.max} (read-only)
   */
  get max(): LRUCache.Count {
    return this.#max
  }
  /**
   * {@link LRUCache.OptionsBase.maxSize} (read-only)
   */
  get maxSize(): LRUCache.Count {
    return this.#maxSize
  }
  /**
   * The total computed size of items in the cache (read-only)
   */
  get calculatedSize(): LRUCache.Size {
    return this.#calculatedSize
  }
  /**
   * The number of items stored in the cache (read-only)
   */
  get size(): LRUCache.Count {
    return this.#size
  }
  /**
   * {@link LRUCache.OptionsBase.fetchMethod} (read-only)
   */
  get fetchMethod(): LRUCache.Fetcher<K, V, FC> | undefined {
    return this.#fetchMethod
  }
  get memoMethod(): LRUCache.Memoizer<K, V, FC> | undefined {
    return this.#memoMethod
  }
  /**
   * {@link LRUCache.OptionsBase.dispose} (read-only)
   */
  get dispose() {
    return this.#dispose
  }
  /**
   * {@link LRUCache.OptionsBase.onInsert} (read-only)
   */
  get onInsert() {
    return this.#onInsert
  }
  /**
   * {@link LRUCache.OptionsBase.disposeAfter} (read-only)
   */
  get disposeAfter() {
    return this.#disposeAfter
  }

  constructor(options: LRUCache.Options<K, V, FC> | LRUCache<K, V, FC>) {
    const {
      max = 0,
      ttl,
      ttlResolution = 1,
      ttlAutopurge,
      updateAgeOnGet,
      updateAgeOnHas,
      allowStale,
      dispose,
      onInsert,
      disposeAfter,
      noDisposeOnSet,
      noUpdateTTL,
      maxSize = 0,
      maxEntrySize = 0,
      sizeCalculation,
      fetchMethod,
      memoMethod,
      noDeleteOnFetchRejection,
      noDeleteOnStaleGet,
      allowStaleOnFetchRejection,
      allowStaleOnFetchAbort,
      ignoreFetchAbort,
      perf,
    } = options

    if (perf !== undefined) {
      if (typeof perf?.now !== 'function') {
        throw new TypeError(
          'perf option must have a now() method if specified',
        )
      }
    }

    this.#perf = perf ?? defaultPerf

    if (max !== 0 && !isPosInt(max)) {
      throw new TypeError('max option must be a nonnegative integer')
    }

    const UintArray = max ? getUintArray(max) : Array
    if (!UintArray) {
      throw new Error('invalid max value: ' + max)
    }

    this.#max = max
    this.#maxSize = maxSize
    this.maxEntrySize = maxEntrySize || this.#maxSize
    this.sizeCalculation = sizeCalculation
    if (this.sizeCalculation) {
      if (!this.#maxSize && !this.maxEntrySize) {
        throw new TypeError(
          'cannot set sizeCalculation without setting maxSize or maxEntrySize',
        )
      }
      if (typeof this.sizeCalculation !== 'function') {
        throw new TypeError('sizeCalculation set to non-function')
      }
    }

    if (memoMethod !== undefined && typeof memoMethod !== 'function') {
      throw new TypeError('memoMethod must be a function if defined')
    }
    this.#memoMethod = memoMethod

    if (fetchMethod !== undefined && typeof fetchMethod !== 'function') {
      throw new TypeError('fetchMethod must be a function if specified')
    }
    this.#fetchMethod = fetchMethod
    this.#hasFetchMethod = !!fetchMethod

    this.#keyMap = new Map()
    this.#keyList = new Array(max).fill(undefined)
    this.#valList = new Array(max).fill(undefined)
    this.#next = new UintArray(max)
    this.#prev = new UintArray(max)
    this.#head = 0 as Index
    this.#tail = 0 as Index
    this.#free = Stack.create(max)
    this.#size = 0
    this.#calculatedSize = 0

    if (typeof dispose === 'function') {
      this.#dispose = dispose
    }
    if (typeof onInsert === 'function') {
      this.#onInsert = onInsert
    }
    if (typeof disposeAfter === 'function') {
      this.#disposeAfter = disposeAfter
      this.#disposed = []
    } else {
      this.#disposeAfter = undefined
      this.#disposed = undefined
    }
    this.#hasDispose = !!this.#dispose
    this.#hasOnInsert = !!this.#onInsert
    this.#hasDisposeAfter = !!this.#disposeAfter

    this.noDisposeOnSet = !!noDisposeOnSet
    this.noUpdateTTL = !!noUpdateTTL
    this.noDeleteOnFetchRejection = !!noDeleteOnFetchRejection
    this.allowStaleOnFetchRejection = !!allowStaleOnFetchRejection
    this.allowStaleOnFetchAbort = !!allowStaleOnFetchAbort
    this.ignoreFetchAbort = !!ignoreFetchAbort

    // NB: maxEntrySize is set to maxSize if it's set
    if (this.maxEntrySize !== 0) {
      if (this.#maxSize !== 0) {
        if (!isPosInt(this.#maxSize)) {
          throw new TypeError(
            'maxSize must be a positive integer if specified',
          )
        }
      }
      if (!isPosInt(this.maxEntrySize)) {
        throw new TypeError(
          'maxEntrySize must be a positive integer if specified',
        )
      }
      this.#initializeSizeTracking()
    }

    this.allowStale = !!allowStale
    this.noDeleteOnStaleGet = !!noDeleteOnStaleGet
    this.updateAgeOnGet = !!updateAgeOnGet
    this.updateAgeOnHas = !!updateAgeOnHas
    this.ttlResolution =
      isPosInt(ttlResolution) || ttlResolution === 0 ? ttlResolution : 1
    this.ttlAutopurge = !!ttlAutopurge
    this.ttl = ttl || 0
    if (this.ttl) {
      if (!isPosInt(this.ttl)) {
        throw new TypeError('ttl must be a positive integer if specified')
      }
      this.#initializeTTLTracking()
    }

    // do not allow completely unbounded caches
    if (this.#max === 0 && this.ttl === 0 && this.#maxSize === 0) {
      throw new TypeError(
        'At least one of max, maxSize, or ttl is required',
      )
    }
    if (!this.ttlAutopurge && !this.#max && !this.#maxSize) {
      const code = 'LRU_CACHE_UNBOUNDED'
      if (shouldWarn(code)) {
        warned.add(code)
        const msg =
          'TTL caching without ttlAutopurge, max, or maxSize can ' +
          'result in unbounded memory consumption.'
        emitWarning(msg, 'UnboundedCacheWarning', code, LRUCache)
      }
    }
  }

  /**
   * Return the number of ms left in the item's TTL. If item is not in cache,
   * returns `0`. Returns `Infinity` if item is in cache without a defined TTL.
   */
  getRemainingTTL(key: K) {
    return this.#keyMap.has(key) ? Infinity : 0
  }

  #initializeTTLTracking() {
    const ttls = new ZeroArray(this.#max)
    const starts = new ZeroArray(this.#max)
    this.#ttls = ttls
    this.#starts = starts
    const purgeTimers =
      this.ttlAutopurge ?
        new Array<undefined | ReturnType<typeof setTimeout>>(this.#max)
      : undefined
    this.#autopurgeTimers = purgeTimers

    this.#setItemTTL = (index, ttl, start = this.#perf.now()) => {
      starts[index] = ttl !== 0 ? start : 0
      ttls[index] = ttl
      setPurgetTimer(index, ttl)
    }

    this.#updateItemAge = index => {
      starts[index] = ttls[index] !== 0 ? this.#perf.now() : 0
      setPurgetTimer(index, ttls[index])
    }

    // clear out the purge timer if we're setting TTL to 0, and
    // previously had a ttl purge timer running, so it doesn't
    // fire unnecessarily. Don't need to do this if we're not doing
    // autopurge.
    const setPurgetTimer =
      !this.ttlAutopurge ?
        () => {}
      : (index: Index, ttl?: number) => {
          if (purgeTimers?.[index]) {
            clearTimeout(purgeTimers[index])
            purgeTimers[index] = undefined
          }
          if (ttl && ttl !== 0 && purgeTimers) {
            const t = setTimeout(() => {
              if (this.#isStale(index)) {
                this.#delete(this.#keyList[index] as K, 'expire')
              }
            }, ttl + 1)
            // unref() not supported on all platforms
            /* c8 ignore start */
            if (t.unref) {
              t.unref()
            }
            /* c8 ignore stop */
            purgeTimers[index] = t
          }
        }

    this.#statusTTL = (status, index) => {
      if (ttls[index]) {
        const ttl = ttls[index]
        const start = starts[index]
        /* c8 ignore next */
        if (!ttl || !start) return
        status.ttl = ttl
        status.start = start
        status.now = cachedNow || getNow()
        const age = status.now - start
        status.remainingTTL = ttl - age
      }
    }

    // debounce calls to perf.now() to 1s so we're not hitting
    // that costly call repeatedly.
    let cachedNow = 0
    const getNow = () => {
      const n = this.#perf.now()
      if (this.ttlResolution > 0) {
        cachedNow = n
        const t = setTimeout(() => (cachedNow = 0), this.ttlResolution)
        // not available on all platforms
        /* c8 ignore start */
        if (t.unref) {
          t.unref()
        }
        /* c8 ignore stop */
      }
      return n
    }

    this.getRemainingTTL = key => {
      const index = this.#keyMap.get(key)
      if (index === undefined) {
        return 0
      }
      const ttl = ttls[index]
      const start = starts[index]
      if (!ttl || !start) {
        return Infinity
      }
      const age = (cachedNow || getNow()) - start
      return ttl - age
    }

    this.#isStale = index => {
      const s = starts[index]
      const t = ttls[index]
      return !!t && !!s && (cachedNow || getNow()) - s > t
    }
  }

  // conditionally set private methods related to TTL
  #updateItemAge: (index: Index) => void = () => {}
  #statusTTL: (status: LRUCache.Status<V>, index: Index) => void = () => {}
  #setItemTTL: (
    index: Index,
    ttl: LRUCache.Milliseconds,
    start?: LRUCache.Milliseconds,
    // ignore because we never call this if we're not already in TTL mode
    /* c8 ignore start */
  ) => void = () => {}
  /* c8 ignore stop */

  #isStale: (index: Index) => boolean = () => false

  #initializeSizeTracking() {
    const sizes = new ZeroArray(this.#max)
    this.#calculatedSize = 0
    this.#sizes = sizes
    this.#removeItemSize = index => {
      this.#calculatedSize -= sizes[index] as number
      sizes[index] = 0
    }
    this.#requireSize = (k, v, size, sizeCalculation) => {
      // provisionally accept background fetches.
      // actual value size will be checked when they return.
      if (this.#isBackgroundFetch(v)) {
        return 0
      }
      if (!isPosInt(size)) {
        if (sizeCalculation) {
          if (typeof sizeCalculation !== 'function') {
            throw new TypeError('sizeCalculation must be a function')
          }
          size = sizeCalculation(v, k)
          if (!isPosInt(size)) {
            throw new TypeError(
              'sizeCalculation return invalid (expect positive integer)',
            )
          }
        } else {
          throw new TypeError(
            'invalid size value (must be positive integer). ' +
              'When maxSize or maxEntrySize is used, sizeCalculation ' +
              'or size must be set.',
          )
        }
      }
      return size
    }
    this.#addItemSize = (
      index: Index,
      size: LRUCache.Size,
      status?: LRUCache.Status<V>,
    ) => {
      sizes[index] = size
      if (this.#maxSize) {
        const maxSize = this.#maxSize - (sizes[index] as number)
        while (this.#calculatedSize > maxSize) {
          this.#evict(true)
        }
      }
      this.#calculatedSize += sizes[index] as number
      if (status) {
        status.entrySize = size
        status.totalCalculatedSize = this.#calculatedSize
      }
    }
  }

  #removeItemSize: (index: Index) => void = _i => {}
  #addItemSize: (
    index: Index,
    size: LRUCache.Size,
    status?: LRUCache.Status<V>,
  ) => void = (_i, _s, _st) => {}
  #requireSize: (
    k: K,
    v: V | BackgroundFetch<V>,
    size?: LRUCache.Size,
    sizeCalculation?: LRUCache.SizeCalculator<K, V>,
  ) => LRUCache.Size = (
    _k: K,
    _v: V | BackgroundFetch<V>,
    size?: LRUCache.Size,
    sizeCalculation?: LRUCache.SizeCalculator<K, V>,
  ) => {
    if (size || sizeCalculation) {
      throw new TypeError(
        'cannot set size without setting maxSize or maxEntrySize on cache',
      )
    }
    return 0
  };

  *#indexes({ allowStale = this.allowStale } = {}) {
    if (this.#size) {
      for (let i = this.#tail; true; ) {
        if (!this.#isValidIndex(i)) {
          break
        }
        if (allowStale || !this.#isStale(i)) {
          yield i
        }
        if (i === this.#head) {
          break
        } else {
          i = this.#prev[i] as Index
        }
      }
    }
  }

  *#rindexes({ allowStale = this.allowStale } = {}) {
    if (this.#size) {
      for (let i = this.#head; true; ) {
        if (!this.#isValidIndex(i)) {
          break
        }
        if (allowStale || !this.#isStale(i)) {
          yield i
        }
        if (i === this.#tail) {
          break
        } else {
          i = this.#next[i] as Index
        }
      }
    }
  }

  #isValidIndex(index: Index) {
    return (
      index !== undefined &&
      this.#keyMap.get(this.#keyList[index] as K) === index
    )
  }

  /**
   * Return a generator yielding `[key, value]` pairs,
   * in order from most recently used to least recently used.
   */
  *entries() {
    for (const i of this.#indexes()) {
      if (
        this.#valList[i] !== undefined &&
        this.#keyList[i] !== undefined &&
        !this.#isBackgroundFetch(this.#valList[i])
      ) {
        yield [this.#keyList[i], this.#valList[i]] as [K, V]
      }
    }
  }

  /**
   * Inverse order version of {@link LRUCache.entries}
   *
   * Return a generator yielding `[key, value]` pairs,
   * in order from least recently used to most recently used.
   */
  *rentries() {
    for (const i of this.#rindexes()) {
      if (
        this.#valList[i] !== undefined &&
        this.#keyList[i] !== undefined &&
        !this.#isBackgroundFetch(this.#valList[i])
      ) {
        yield [this.#keyList[i], this.#valList[i]]
      }
    }
  }

  /**
   * Return a generator yielding the keys in the cache,
   * in order from most recently used to least recently used.
   */
  *keys() {
    for (const i of this.#indexes()) {
      const k = this.#keyList[i]
      if (k !== undefined && !this.#isBackgroundFetch(this.#valList[i])) {
        yield k
      }
    }
  }

  /**
   * Inverse order version of {@link LRUCache.keys}
   *
   * Return a generator yielding the keys in the cache,
   * in order from least recently used to most recently used.
   */
  *rkeys() {
    for (const i of this.#rindexes()) {
      const k = this.#keyList[i]
      if (k !== undefined && !this.#isBackgroundFetch(this.#valList[i])) {
        yield k
      }
    }
  }

  /**
   * Return a generator yielding the values in the cache,
   * in order from most recently used to least recently used.
   */
  *values() {
    for (const i of this.#indexes()) {
      const v = this.#valList[i]
      if (v !== undefined && !this.#isBackgroundFetch(this.#valList[i])) {
        yield this.#valList[i] as V
      }
    }
  }

  /**
   * Inverse order version of {@link LRUCache.values}
   *
   * Return a generator yielding the values in the cache,
   * in order from least recently used to most recently used.
   */
  *rvalues() {
    for (const i of this.#rindexes()) {
      const v = this.#valList[i]
      if (v !== undefined && !this.#isBackgroundFetch(this.#valList[i])) {
        yield this.#valList[i]
      }
    }
  }

  /**
   * Iterating over the cache itself yields the same results as
   * {@link LRUCache.entries}
   */
  [Symbol.iterator]() {
    return this.entries()
  }

  /**
   * A String value that is used in the creation of the default string
   * description of an object. Called by the built-in method
   * `Object.prototype.toString`.
   */
  [Symbol.toStringTag] = 'LRUCache'

  /**
   * Find a value for which the supplied fn method returns a truthy value,
   * similar to `Array.find()`. fn is called as `fn(value, key, cache)`.
   */
  find(
    fn: (v: V, k: K, self: LRUCache<K, V, FC>) => boolean,
    getOptions: LRUCache.GetOptions<K, V, FC> = {},
  ) {
    for (const i of this.#indexes()) {
      const v = this.#valList[i]
      const value = this.#isBackgroundFetch(v) ? v.__staleWhileFetching : v
      if (value === undefined) continue
      if (fn(value, this.#keyList[i] as K, this)) {
        return this.get(this.#keyList[i] as K, getOptions)
      }
    }
  }

  /**
   * Call the supplied function on each item in the cache, in order from most
   * recently used to least recently used.
   *
   * `fn` is called as `fn(value, key, cache)`.
   *
   * If `thisp` is provided, function will be called in the `this`-context of
   * the provided object, or the cache if no `thisp` object is provided.
   *
   * Does not update age or recenty of use, or iterate over stale values.
   */
  forEach(
    fn: (v: V, k: K, self: LRUCache<K, V, FC>) => any,
    thisp: any = this,
  ) {
    for (const i of this.#indexes()) {
      const v = this.#valList[i]
      const value = this.#isBackgroundFetch(v) ? v.__staleWhileFetching : v
      if (value === undefined) continue
      fn.call(thisp, value, this.#keyList[i] as K, this)
    }
  }

  /**
   * The same as {@link LRUCache.forEach} but items are iterated over in
   * reverse order.  (ie, less recently used items are iterated over first.)
   */
  rforEach(
    fn: (v: V, k: K, self: LRUCache<K, V, FC>) => any,
    thisp: any = this,
  ) {
    for (const i of this.#rindexes()) {
      const v = this.#valList[i]
      const value = this.#isBackgroundFetch(v) ? v.__staleWhileFetching : v
      if (value === undefined) continue
      fn.call(thisp, value, this.#keyList[i] as K, this)
    }
  }

  /**
   * Delete any stale entries. Returns true if anything was removed,
   * false otherwise.
   */
  purgeStale() {
    let deleted = false
    for (const i of this.#rindexes({ allowStale: true })) {
      if (this.#isStale(i)) {
        this.#delete(this.#keyList[i] as K, 'expire')
        deleted = true
      }
    }
    return deleted
  }

  /**
   * Get the extended info about a given entry, to get its value, size, and
   * TTL info simultaneously. Returns `undefined` if the key is not present.
   *
   * Unlike {@link LRUCache#dump}, which is designed to be portable and survive
   * serialization, the `start` value is always the current timestamp, and the
   * `ttl` is a calculated remaining time to live (negative if expired).
   *
   * Always returns stale values, if their info is found in the cache, so be
   * sure to check for expirations (ie, a negative {@link LRUCache.Entry#ttl})
   * if relevant.
   */
  info(key: K): LRUCache.Entry<V> | undefined {
    const i = this.#keyMap.get(key)
    if (i === undefined) return undefined
    const v = this.#valList[i]
    /* c8 ignore start - this isn't tested for the info function,
     * but it's the same logic as found in other places. */
    const value: V | undefined =
      this.#isBackgroundFetch(v) ? v.__staleWhileFetching : v
    if (value === undefined) return undefined
    /* c8 ignore end */
    const entry: LRUCache.Entry<V> = { value }
    if (this.#ttls && this.#starts) {
      const ttl = this.#ttls[i]
      const start = this.#starts[i]
      if (ttl && start) {
        const remain = ttl - (this.#perf.now() - start)
        entry.ttl = remain
        entry.start = Date.now()
      }
    }
    if (this.#sizes) {
      entry.size = this.#sizes[i]
    }
    return entry
  }

  /**
   * Return an array of [key, {@link LRUCache.Entry}] tuples which can be
   * passed to {@link LRUCache#load}.
   *
   * The `start` fields are calculated relative to a portable `Date.now()`
   * timestamp, even if `performance.now()` is available.
   *
   * Stale entries are always included in the `dump`, even if
   * {@link LRUCache.OptionsBase.allowStale} is false.
   *
   * Note: this returns an actual array, not a generator, so it can be more
   * easily passed around.
   */
  dump() {
    const arr: [K, LRUCache.Entry<V>][] = []
    for (const i of this.#indexes({ allowStale: true })) {
      const key = this.#keyList[i]
      const v = this.#valList[i]
      const value: V | undefined =
        this.#isBackgroundFetch(v) ? v.__staleWhileFetching : v
      if (value === undefined || key === undefined) continue
      const entry: LRUCache.Entry<V> = { value }
      if (this.#ttls && this.#starts) {
        entry.ttl = this.#ttls[i]
        // always dump the start relative to a portable timestamp
        // it's ok for this to be a bit slow, it's a rare operation.
        const age = this.#perf.now() - (this.#starts[i] as number)
        entry.start = Math.floor(Date.now() - age)
      }
      if (this.#sizes) {
        entry.size = this.#sizes[i]
      }
      arr.unshift([key, entry])
    }
    return arr
  }

  /**
   * Reset the cache and load in the items in entries in the order listed.
   *
   * The shape of the resulting cache may be different if the same options are
   * not used in both caches.
   *
   * The `start` fields are assumed to be calculated relative to a portable
   * `Date.now()` timestamp, even if `performance.now()` is available.
   */
  load(arr: [K, LRUCache.Entry<V>][]) {
    this.clear()
    for (const [key, entry] of arr) {
      if (entry.start) {
        // entry.start is a portable timestamp, but we may be using
        // node's performance.now(), so calculate the offset, so that
        // we get the intended remaining TTL, no matter how long it's
        // been on ice.
        //
        // it's ok for this to be a bit slow, it's a rare operation.
        const age = Date.now() - entry.start
        entry.start = this.#perf.now() - age
      }
      this.set(key, entry.value, entry)
    }
  }

  /**
   * Add a value to the cache.
   *
   * Note: if `undefined` is specified as a value, this is an alias for
   * {@link LRUCache#delete}
   *
   * Fields on the {@link LRUCache.SetOptions} options param will override
   * their corresponding values in the constructor options for the scope
   * of this single `set()` operation.
   *
   * If `start` is provided, then that will set the effective start
   * time for the TTL calculation. Note that this must be a previous
   * value of `performance.now()` if supported, or a previous value of
   * `Date.now()` if not.
   *
   * Options object may also include `size`, which will prevent
   * calling the `sizeCalculation` function and just use the specified
   * number if it is a positive integer, and `noDisposeOnSet` which
   * will prevent calling a `dispose` function in the case of
   * overwrites.
   *
   * If the `size` (or return value of `sizeCalculation`) for a given
   * entry is greater than `maxEntrySize`, then the item will not be
   * added to the cache.
   *
   * Will update the recency of the entry.
   *
   * If the value is `undefined`, then this is an alias for
   * `cache.delete(key)`. `undefined` is never stored in the cache.
   */
  set(
    k: K,
    v: V | BackgroundFetch<V> | undefined,
    setOptions: LRUCache.SetOptions<K, V, FC> = {},
  ) {
    if (v === undefined) {
      this.delete(k)
      return this
    }
    const {
      ttl = this.ttl,
      start,
      noDisposeOnSet = this.noDisposeOnSet,
      sizeCalculation = this.sizeCalculation,
      status,
    } = setOptions
    let { noUpdateTTL = this.noUpdateTTL } = setOptions

    const size = this.#requireSize(
      k,
      v,
      setOptions.size || 0,
      sizeCalculation,
    )
    // if the item doesn't fit, don't do anything
    // NB: maxEntrySize set to maxSize by default
    if (this.maxEntrySize && size > this.maxEntrySize) {
      if (status) {
        status.set = 'miss'
        status.maxEntrySizeExceeded = true
      }
      // have to delete, in case something is there already.
      this.#delete(k, 'set')
      return this
    }
    let index = this.#size === 0 ? undefined : this.#keyMap.get(k)
    if (index === undefined) {
      // addition
      index = (
        this.#size === 0 ? this.#tail
        : this.#free.length !== 0 ? this.#free.pop()
        : this.#size === this.#max ? this.#evict(false)
        : this.#size) as Index
      this.#keyList[index] = k
      this.#valList[index] = v
      this.#keyMap.set(k, index)
      this.#next[this.#tail] = index
      this.#prev[index] = this.#tail
      this.#tail = index
      this.#size++
      this.#addItemSize(index, size, status)
      if (status) status.set = 'add'
      noUpdateTTL = false
      if (this.#hasOnInsert) {
        this.#onInsert?.(v as V, k, 'add')
      }
    } else {
      // update
      this.#moveToTail(index)
      const oldVal = this.#valList[index] as V | BackgroundFetch<V>
      if (v !== oldVal) {
        if (this.#hasFetchMethod && this.#isBackgroundFetch(oldVal)) {
          oldVal.__abortController.abort(new Error('replaced'))
          const { __staleWhileFetching: s } = oldVal
          if (s !== undefined && !noDisposeOnSet) {
            if (this.#hasDispose) {
              this.#dispose?.(s as V, k, 'set')
            }
            if (this.#hasDisposeAfter) {
              this.#disposed?.push([s as V, k, 'set'])
            }
          }
        } else if (!noDisposeOnSet) {
          if (this.#hasDispose) {
            this.#dispose?.(oldVal as V, k, 'set')
          }
          if (this.#hasDisposeAfter) {
            this.#disposed?.push([oldVal as V, k, 'set'])
          }
        }
        this.#removeItemSize(index)
        this.#addItemSize(index, size, status)
        this.#valList[index] = v
        if (status) {
          status.set = 'replace'
          const oldValue =
            oldVal && this.#isBackgroundFetch(oldVal) ?
              oldVal.__staleWhileFetching
            : oldVal
          if (oldValue !== undefined) status.oldValue = oldValue
        }
      } else if (status) {
        status.set = 'update'
      }

      if (this.#hasOnInsert) {
        this.onInsert?.(v as V, k, v === oldVal ? 'update' : 'replace')
      }
    }
    if (ttl !== 0 && !this.#ttls) {
      this.#initializeTTLTracking()
    }
    if (this.#ttls) {
      if (!noUpdateTTL) {
        this.#setItemTTL(index, ttl, start)
      }
      if (status) this.#statusTTL(status, index)
    }
    if (!noDisposeOnSet && this.#hasDisposeAfter && this.#disposed) {
      const dt = this.#disposed
      let task: DisposeTask<K, V> | undefined
      while ((task = dt?.shift())) {
        this.#disposeAfter?.(...task)
      }
    }
    return this
  }

  /**
   * Evict the least recently used item, returning its value or
   * `undefined` if cache is empty.
   */
  pop(): V | undefined {
    try {
      while (this.#size) {
        const val = this.#valList[this.#head]
        this.#evict(true)
        if (this.#isBackgroundFetch(val)) {
          if (val.__staleWhileFetching) {
            return val.__staleWhileFetching
          }
        } else if (val !== undefined) {
          return val
        }
      }
    } finally {
      if (this.#hasDisposeAfter && this.#disposed) {
        const dt = this.#disposed
        let task: DisposeTask<K, V> | undefined
        while ((task = dt?.shift())) {
          this.#disposeAfter?.(...task)
        }
      }
    }
  }

  #evict(free: boolean) {
    const head = this.#head
    const k = this.#keyList[head] as K
    const v = this.#valList[head] as V
    if (this.#hasFetchMethod && this.#isBackgroundFetch(v)) {
      v.__abortController.abort(new Error('evicted'))
    } else if (this.#hasDispose || this.#hasDisposeAfter) {
      if (this.#hasDispose) {
        this.#dispose?.(v, k, 'evict')
      }
      if (this.#hasDisposeAfter) {
        this.#disposed?.push([v, k, 'evict'])
      }
    }
    this.#removeItemSize(head)
    if (this.#autopurgeTimers?.[head]) {
      clearTimeout(this.#autopurgeTimers[head])
      this.#autopurgeTimers[head] = undefined
    }
    // if we aren't about to use the index, then null these out
    if (free) {
      this.#keyList[head] = undefined
      this.#valList[head] = undefined
      this.#free.push(head)
    }
    if (this.#size === 1) {
      this.#head = this.#tail = 0 as Index
      this.#free.length = 0
    } else {
      this.#head = this.#next[head] as Index
    }
    this.#keyMap.delete(k)
    this.#size--
    return head
  }

  /**
   * Check if a key is in the cache, without updating the recency of use.
   * Will return false if the item is stale, even though it is technically
   * in the cache.
   *
   * Check if a key is in the cache, without updating the recency of
   * use. Age is updated if {@link LRUCache.OptionsBase.updateAgeOnHas} is set
   * to `true` in either the options or the constructor.
   *
   * Will return `false` if the item is stale, even though it is technically in
   * the cache. The difference can be determined (if it matters) by using a
   * `status` argument, and inspecting the `has` field.
   *
   * Will not update item age unless
   * {@link LRUCache.OptionsBase.updateAgeOnHas} is set.
   */
  has(k: K, hasOptions: LRUCache.HasOptions<K, V, FC> = {}) {
    const { updateAgeOnHas = this.updateAgeOnHas, status } = hasOptions
    const index = this.#keyMap.get(k)
    if (index !== undefined) {
      const v = this.#valList[index]
      if (
        this.#isBackgroundFetch(v) &&
        v.__staleWhileFetching === undefined
      ) {
        return false
      }
      if (!this.#isStale(index)) {
        if (updateAgeOnHas) {
          this.#updateItemAge(index)
        }
        if (status) {
          status.has = 'hit'
          this.#statusTTL(status, index)
        }
        return true
      } else if (status) {
        status.has = 'stale'
        this.#statusTTL(status, index)
      }
    } else if (status) {
      status.has = 'miss'
    }
    return false
  }

  /**
   * Like {@link LRUCache#get} but doesn't update recency or delete stale
   * items.
   *
   * Returns `undefined` if the item is stale, unless
   * {@link LRUCache.OptionsBase.allowStale} is set.
   */
  peek(k: K, peekOptions: LRUCache.PeekOptions<K, V, FC> = {}) {
    const { allowStale = this.allowStale } = peekOptions
    const index = this.#keyMap.get(k)
    if (index === undefined || (!allowStale && this.#isStale(index))) {
      return
    }
    const v = this.#valList[index]
    // either stale and allowed, or forcing a refresh of non-stale value
    return this.#isBackgroundFetch(v) ? v.__staleWhileFetching : v
  }

  #backgroundFetch(
    k: K,
    index: Index | undefined,
    options: LRUCache.FetchOptions<K, V, FC>,
    context: any,
  ): BackgroundFetch<V> {
    const v = index === undefined ? undefined : this.#valList[index]
    if (this.#isBackgroundFetch(v)) {
      return v
    }

    const ac = new AC()
    const { signal } = options
    // when/if our AC signals, then stop listening to theirs.
    signal?.addEventListener('abort', () => ac.abort(signal.reason), {
      signal: ac.signal,
    })

    const fetchOpts = {
      signal: ac.signal,
      options,
      context,
    }

    const cb = (v: V | undefined, updateCache = false): V | undefined => {
      const { aborted } = ac.signal
      const ignoreAbort = options.ignoreFetchAbort && v !== undefined
      const proceed =
        options.ignoreFetchAbort ||
        !!(options.allowStaleOnFetchAbort && v !== undefined)
      if (options.status) {
        if (aborted && !updateCache) {
          options.status.fetchAborted = true
          options.status.fetchError = ac.signal.reason
          if (ignoreAbort) options.status.fetchAbortIgnored = true
        } else {
          options.status.fetchResolved = true
        }
      }
      if (aborted && !ignoreAbort && !updateCache) {
        return fetchFail(ac.signal.reason, proceed)
      }
      // either we didn't abort, and are still here, or we did, and ignored
      const bf = p as BackgroundFetch<V>
      // if nothing else has been written there but we're set to update the
      // cache and ignore the abort, or if it's still pending on this specific
      // background request, then write it to the cache.
      const vl = this.#valList[index as Index]
      if (vl === p || (ignoreAbort && updateCache && vl === undefined)) {
        if (v === undefined) {
          if (bf.__staleWhileFetching !== undefined) {
            this.#valList[index as Index] = bf.__staleWhileFetching
          } else {
            this.#delete(k, 'fetch')
          }
        } else {
          if (options.status) options.status.fetchUpdated = true
          this.set(k, v, fetchOpts.options)
        }
      }
      return v
    }

    const eb = (er: any) => {
      if (options.status) {
        options.status.fetchRejected = true
        options.status.fetchError = er
      }
      // do not pass go, do not collect $200
      return fetchFail(er, false)
    }

    const fetchFail = (er: any, proceed: boolean): V | undefined => {
      const { aborted } = ac.signal
      const allowStaleAborted = aborted && options.allowStaleOnFetchAbort
      const allowStale =
        allowStaleAborted || options.allowStaleOnFetchRejection
      const noDelete = allowStale || options.noDeleteOnFetchRejection
      const bf = p as BackgroundFetch<V>
      if (this.#valList[index as Index] === p) {
        // if we allow stale on fetch rejections, then we need to ensure that
        // the stale value is not removed from the cache when the fetch fails.
        const del =
          !noDelete || (!proceed && bf.__staleWhileFetching === undefined)
        if (del) {
          this.#delete(k, 'fetch')
        } else if (!allowStaleAborted) {
          // still replace the *promise* with the stale value,
          // since we are done with the promise at this point.
          // leave it untouched if we're still waiting for an
          // aborted background fetch that hasn't yet returned.
          this.#valList[index as Index] = bf.__staleWhileFetching
        }
      }
      if (allowStale) {
        if (options.status && bf.__staleWhileFetching !== undefined) {
          options.status.returnedStale = true
        }
        return bf.__staleWhileFetching
      } else if (bf.__returned === bf) {
        throw er
      }
    }

    const pcall = (
      res: (v: V | undefined) => void,
      rej: (e: any) => void,
    ) => {
      const fmp = this.#fetchMethod?.(k, v, fetchOpts)
      if (fmp && fmp instanceof Promise) {
        fmp.then(v => res(v === undefined ? undefined : v), rej)
      }
      // ignored, we go until we finish, regardless.
      // defer check until we are actually aborting,
      // so fetchMethod can override.
      ac.signal.addEventListener('abort', () => {
        if (!options.ignoreFetchAbort || options.allowStaleOnFetchAbort) {
          res(undefined)
          // when it eventually resolves, update the cache.
          if (options.allowStaleOnFetchAbort) {
            res = v => cb(v, true)
          }
        }
      })
    }

    if (options.status) options.status.fetchDispatched = true
    const p = new Promise(pcall).then(cb, eb)
    const bf: BackgroundFetch<V> = Object.assign(p, {
      __abortController: ac,
      __staleWhileFetching: v,
      __returned: undefined,
    })

    if (index === undefined) {
      // internal, don't expose status.
      this.set(k, bf, { ...fetchOpts.options, status: undefined })
      index = this.#keyMap.get(k)
    } else {
      this.#valList[index] = bf
    }
    return bf
  }

  #isBackgroundFetch(p: any): p is BackgroundFetch<V> {
    if (!this.#hasFetchMethod) return false
    const b = p as BackgroundFetch<V>
    return (
      !!b &&
      b instanceof Promise &&
      b.hasOwnProperty('__staleWhileFetching') &&
      b.__abortController instanceof AC
    )
  }

  /**
   * Make an asynchronous cached fetch using the
   * {@link LRUCache.OptionsBase.fetchMethod} function.
   *
   * If the value is in the cache and not stale, then the returned
   * Promise resolves to the value.
   *
   * If not in the cache, or beyond its TTL staleness, then
   * `fetchMethod(key, staleValue, { options, signal, context })` is
   * called, and the value returned will be added to the cache once
   * resolved.
   *
   * If called with `allowStale`, and an asynchronous fetch is
   * currently in progress to reload a stale value, then the former
   * stale value will be returned.
   *
   * If called with `forceRefresh`, then the cached item will be
   * re-fetched, even if it is not stale. However, if `allowStale` is also
   * set, then the old value will still be returned. This is useful
   * in cases where you want to force a reload of a cached value. If
   * a background fetch is already in progress, then `forceRefresh`
   * has no effect.
   *
   * If multiple fetches for the same key are issued, then they will all be
   * coalesced into a single call to fetchMethod.
   *
   * Note that this means that handling options such as
   * {@link LRUCache.OptionsBase.allowStaleOnFetchAbort},
   * {@link LRUCache.FetchOptions.signal},
   * and {@link LRUCache.OptionsBase.allowStaleOnFetchRejection} will be
   * determined by the FIRST fetch() call for a given key.
   *
   * This is a known (fixable) shortcoming which will be addresed on when
   * someone complains about it, as the fix would involve added complexity and
   * may not be worth the costs for this edge case.
   *
   * If {@link LRUCache.OptionsBase.fetchMethod} is not specified, then this is
   * effectively an alias for `Promise.resolve(cache.get(key))`.
   *
   * When the fetch method resolves to a value, if the fetch has not
   * been aborted due to deletion, eviction, or being overwritten,
   * then it is added to the cache using the options provided.
   *
   * If the key is evicted or deleted before the `fetchMethod`
   * resolves, then the AbortSignal passed to the `fetchMethod` will
   * receive an `abort` event, and the promise returned by `fetch()`
   * will reject with the reason for the abort.
   *
   * If a `signal` is passed to the `fetch()` call, then aborting the
   * signal will abort the fetch and cause the `fetch()` promise to
   * reject with the reason provided.
   *
   * **Setting `context`**
   *
   * If an `FC` type is set to a type other than `unknown`, `void`, or
   * `undefined` in the {@link LRUCache} constructor, then all
   * calls to `cache.fetch()` _must_ provide a `context` option. If
   * set to `undefined` or `void`, then calls to fetch _must not_
   * provide a `context` option.
   *
   * The `context` param allows you to provide arbitrary data that
   * might be relevant in the course of fetching the data. It is only
   * relevant for the course of a single `fetch()` operation, and
   * discarded afterwards.
   *
   * **Note: `fetch()` calls are inflight-unique**
   *
   * If you call `fetch()` multiple times with the same key value,
   * then every call after the first will resolve on the same
   * promise<sup>1</sup>,
   * _even if they have different settings that would otherwise change
   * the behavior of the fetch_, such as `noDeleteOnFetchRejection`
   * or `ignoreFetchAbort`.
   *
   * In most cases, this is not a problem (in fact, only fetching
   * something once is what you probably want, if you're caching in
   * the first place). If you are changing the fetch() options
   * dramatically between runs, there's a good chance that you might
   * be trying to fit divergent semantics into a single object, and
   * would be better off with multiple cache instances.
   *
   * **1**: Ie, they're not the "same Promise", but they resolve at
   * the same time, because they're both waiting on the same
   * underlying fetchMethod response.
   */

  fetch(
    k: K,
    fetchOptions: unknown extends FC ? LRUCache.FetchOptions<K, V, FC>
    : FC extends undefined | void ? LRUCache.FetchOptionsNoContext<K, V>
    : LRUCache.FetchOptionsWithContext<K, V, FC>,
  ): Promise<undefined | V>

  // this overload not allowed if context is required
  fetch(
    k: unknown extends FC ? K
    : FC extends undefined | void ? K
    : never,
    fetchOptions?: unknown extends FC ? LRUCache.FetchOptions<K, V, FC>
    : FC extends undefined | void ? LRUCache.FetchOptionsNoContext<K, V>
    : never,
  ): Promise<undefined | V>

  async fetch(
    k: K,
    fetchOptions: LRUCache.FetchOptions<K, V, FC> = {},
  ): Promise<undefined | V> {
    const {
      // get options
      allowStale = this.allowStale,
      updateAgeOnGet = this.updateAgeOnGet,
      noDeleteOnStaleGet = this.noDeleteOnStaleGet,
      // set options
      ttl = this.ttl,
      noDisposeOnSet = this.noDisposeOnSet,
      size = 0,
      sizeCalculation = this.sizeCalculation,
      noUpdateTTL = this.noUpdateTTL,
      // fetch exclusive options
      noDeleteOnFetchRejection = this.noDeleteOnFetchRejection,
      allowStaleOnFetchRejection = this.allowStaleOnFetchRejection,
      ignoreFetchAbort = this.ignoreFetchAbort,
      allowStaleOnFetchAbort = this.allowStaleOnFetchAbort,
      context,
      forceRefresh = false,
      status,
      signal,
    } = fetchOptions

    if (!this.#hasFetchMethod) {
      if (status) status.fetch = 'get'
      return this.get(k, {
        allowStale,
        updateAgeOnGet,
        noDeleteOnStaleGet,
        status,
      })
    }

    const options = {
      allowStale,
      updateAgeOnGet,
      noDeleteOnStaleGet,
      ttl,
      noDisposeOnSet,
      size,
      sizeCalculation,
      noUpdateTTL,
      noDeleteOnFetchRejection,
      allowStaleOnFetchRejection,
      allowStaleOnFetchAbort,
      ignoreFetchAbort,
      status,
      signal,
    }

    let index = this.#keyMap.get(k)
    if (index === undefined) {
      if (status) status.fetch = 'miss'
      const p = this.#backgroundFetch(k, index, options, context)
      return (p.__returned = p)
    } else {
      // in cache, maybe already fetching
      const v = this.#valList[index]
      if (this.#isBackgroundFetch(v)) {
        const stale = allowStale && v.__staleWhileFetching !== undefined
        if (status) {
          status.fetch = 'inflight'
          if (stale) status.returnedStale = true
        }
        return stale ? v.__staleWhileFetching : (v.__returned = v)
      }

      // if we force a refresh, that means do NOT serve the cached value,
      // unless we are already in the process of refreshing the cache.
      const isStale = this.#isStale(index)
      if (!forceRefresh && !isStale) {
        if (status) status.fetch = 'hit'
        this.#moveToTail(index)
        if (updateAgeOnGet) {
          this.#updateItemAge(index)
        }
        if (status) this.#statusTTL(status, index)
        return v
      }

      // ok, it is stale or a forced refresh, and not already fetching.
      // refresh the cache.
      const p = this.#backgroundFetch(k, index, options, context)
      const hasStale = p.__staleWhileFetching !== undefined
      const staleVal = hasStale && allowStale
      if (status) {
        status.fetch = isStale ? 'stale' : 'refresh'
        if (staleVal && isStale) status.returnedStale = true
      }
      return staleVal ? p.__staleWhileFetching : (p.__returned = p)
    }
  }

  /**
   * In some cases, `cache.fetch()` may resolve to `undefined`, either because
   * a {@link LRUCache.OptionsBase#fetchMethod} was not provided (turning
   * `cache.fetch(k)` into just an async wrapper around `cache.get(k)`) or
   * because `ignoreFetchAbort` was specified (either to the constructor or
   * in the {@link LRUCache.FetchOptions}). Also, the
   * {@link LRUCache.OptionsBase.fetchMethod} may return `undefined` or `void`, making
   * the test even more complicated.
   *
   * Because inferring the cases where `undefined` might be returned are so
   * cumbersome, but testing for `undefined` can also be annoying, this method
   * can be used, which will reject if `this.fetch()` resolves to undefined.
   */
  forceFetch(
    k: K,
    fetchOptions: unknown extends FC ? LRUCache.FetchOptions<K, V, FC>
    : FC extends undefined | void ? LRUCache.FetchOptionsNoContext<K, V>
    : LRUCache.FetchOptionsWithContext<K, V, FC>,
  ): Promise<V>
  // this overload not allowed if context is required
  forceFetch(
    k: unknown extends FC ? K
    : FC extends undefined | void ? K
    : never,
    fetchOptions?: unknown extends FC ? LRUCache.FetchOptions<K, V, FC>
    : FC extends undefined | void ? LRUCache.FetchOptionsNoContext<K, V>
    : never,
  ): Promise<V>
  async forceFetch(
    k: K,
    fetchOptions: LRUCache.FetchOptions<K, V, FC> = {},
  ): Promise<V> {
    const v = await this.fetch(
      k,
      fetchOptions as unknown extends FC ? LRUCache.FetchOptions<K, V, FC>
      : FC extends undefined | void ? LRUCache.FetchOptionsNoContext<K, V>
      : LRUCache.FetchOptionsWithContext<K, V, FC>,
    )
    if (v === undefined) throw new Error('fetch() returned undefined')
    return v
  }

  /**
   * If the key is found in the cache, then this is equivalent to
   * {@link LRUCache#get}. If not, in the cache, then calculate the value using
   * the {@link LRUCache.OptionsBase.memoMethod}, and add it to the cache.
   *
   * If an `FC` type is set to a type other than `unknown`, `void`, or
   * `undefined` in the LRUCache constructor, then all calls to `cache.memo()`
   * _must_ provide a `context` option. If set to `undefined` or `void`, then
   * calls to memo _must not_ provide a `context` option.
   *
   * The `context` param allows you to provide arbitrary data that might be
   * relevant in the course of fetching the data. It is only relevant for the
   * course of a single `memo()` operation, and discarded afterwards.
   */
  memo(
    k: K,
    memoOptions: unknown extends FC ? LRUCache.MemoOptions<K, V, FC>
    : FC extends undefined | void ? LRUCache.MemoOptionsNoContext<K, V>
    : LRUCache.MemoOptionsWithContext<K, V, FC>,
  ): V
  // this overload not allowed if context is required
  memo(
    k: unknown extends FC ? K
    : FC extends undefined | void ? K
    : never,
    memoOptions?: unknown extends FC ? LRUCache.MemoOptions<K, V, FC>
    : FC extends undefined | void ? LRUCache.MemoOptionsNoContext<K, V>
    : never,
  ): V
  memo(k: K, memoOptions: LRUCache.MemoOptions<K, V, FC> = {}) {
    const memoMethod = this.#memoMethod
    if (!memoMethod) {
      throw new Error('no memoMethod provided to constructor')
    }
    const { context, forceRefresh, ...options } = memoOptions
    const v = this.get(k, options)
    if (!forceRefresh && v !== undefined) return v
    const vv = memoMethod(k, v, {
      options,
      context,
    } as LRUCache.MemoizerOptions<K, V, FC>)
    this.set(k, vv, options)
    return vv
  }

  /**
   * Return a value from the cache. Will update the recency of the cache
   * entry found.
   *
   * If the key is not found, get() will return `undefined`.
   */
  get(k: K, getOptions: LRUCache.GetOptions<K, V, FC> = {}) {
    const {
      allowStale = this.allowStale,
      updateAgeOnGet = this.updateAgeOnGet,
      noDeleteOnStaleGet = this.noDeleteOnStaleGet,
      status,
    } = getOptions
    const index = this.#keyMap.get(k)
    if (index !== undefined) {
      const value = this.#valList[index]
      const fetching = this.#isBackgroundFetch(value)
      if (status) this.#statusTTL(status, index)
      if (this.#isStale(index)) {
        if (status) status.get = 'stale'
        // delete only if not an in-flight background fetch
        if (!fetching) {
          if (!noDeleteOnStaleGet) {
            this.#delete(k, 'expire')
          }
          if (status && allowStale) status.returnedStale = true
          return allowStale ? value : undefined
        } else {
          if (
            status &&
            allowStale &&
            value.__staleWhileFetching !== undefined
          ) {
            status.returnedStale = true
          }
          return allowStale ? value.__staleWhileFetching : undefined
        }
      } else {
        if (status) status.get = 'hit'
        // if we're currently fetching it, we don't actually have it yet
        // it's not stale, which means this isn't a staleWhileRefetching.
        // If it's not stale, and fetching, AND has a __staleWhileFetching
        // value, then that means the user fetched with {forceRefresh:true},
        // so it's safe to return that value.
        if (fetching) {
          return value.__staleWhileFetching
        }
        this.#moveToTail(index)
        if (updateAgeOnGet) {
          this.#updateItemAge(index)
        }
        return value
      }
    } else if (status) {
      status.get = 'miss'
    }
  }

  #connect(p: Index, n: Index) {
    this.#prev[n] = p
    this.#next[p] = n
  }

  #moveToTail(index: Index): void {
    // if tail already, nothing to do
    // if head, move head to next[index]
    // else
    //   move next[prev[index]] to next[index] (head has no prev)
    //   move prev[next[index]] to prev[index]
    // prev[index] = tail
    // next[tail] = index
    // tail = index
    if (index !== this.#tail) {
      if (index === this.#head) {
        this.#head = this.#next[index] as Index
      } else {
        this.#connect(
          this.#prev[index] as Index,
          this.#next[index] as Index,
        )
      }
      this.#connect(this.#tail, index)
      this.#tail = index
    }
  }

  /**
   * Deletes a key out of the cache.
   *
   * Returns true if the key was deleted, false otherwise.
   */
  delete(k: K) {
    return this.#delete(k, 'delete')
  }

  #delete(k: K, reason: LRUCache.DisposeReason) {
    let deleted = false
    if (this.#size !== 0) {
      const index = this.#keyMap.get(k)
      if (index !== undefined) {
        if (this.#autopurgeTimers?.[index]) {
          clearTimeout(this.#autopurgeTimers?.[index])
          this.#autopurgeTimers[index] = undefined
        }
        deleted = true
        if (this.#size === 1) {
          this.#clear(reason)
        } else {
          this.#removeItemSize(index)
          const v = this.#valList[index]
          if (this.#isBackgroundFetch(v)) {
            v.__abortController.abort(new Error('deleted'))
          } else if (this.#hasDispose || this.#hasDisposeAfter) {
            if (this.#hasDispose) {
              this.#dispose?.(v as V, k, reason)
            }
            if (this.#hasDisposeAfter) {
              this.#disposed?.push([v as V, k, reason])
            }
          }
          this.#keyMap.delete(k)
          this.#keyList[index] = undefined
          this.#valList[index] = undefined
          if (index === this.#tail) {
            this.#tail = this.#prev[index] as Index
          } else if (index === this.#head) {
            this.#head = this.#next[index] as Index
          } else {
            const pi = this.#prev[index] as number
            this.#next[pi] = this.#next[index] as number
            const ni = this.#next[index] as number
            this.#prev[ni] = this.#prev[index] as number
          }
          this.#size--
          this.#free.push(index)
        }
      }
    }
    if (this.#hasDisposeAfter && this.#disposed?.length) {
      const dt = this.#disposed
      let task: DisposeTask<K, V> | undefined
      while ((task = dt?.shift())) {
        this.#disposeAfter?.(...task)
      }
    }
    return deleted
  }

  /**
   * Clear the cache entirely, throwing away all values.
   */
  clear() {
    return this.#clear('delete')
  }
  #clear(reason: LRUCache.DisposeReason) {
    for (const index of this.#rindexes({ allowStale: true })) {
      const v = this.#valList[index]
      if (this.#isBackgroundFetch(v)) {
        v.__abortController.abort(new Error('deleted'))
      } else {
        const k = this.#keyList[index]
        if (this.#hasDispose) {
          this.#dispose?.(v as V, k as K, reason)
        }
        if (this.#hasDisposeAfter) {
          this.#disposed?.push([v as V, k as K, reason])
        }
      }
    }

    this.#keyMap.clear()
    this.#valList.fill(undefined)
    this.#keyList.fill(undefined)
    if (this.#ttls && this.#starts) {
      this.#ttls.fill(0)
      this.#starts.fill(0)
      for (const t of this.#autopurgeTimers ?? []) {
        if (t !== undefined) clearTimeout(t)
      }
      this.#autopurgeTimers?.fill(undefined)
    }
    if (this.#sizes) {
      this.#sizes.fill(0)
    }
    this.#head = 0 as Index
    this.#tail = 0 as Index
    this.#free.length = 0
    this.#calculatedSize = 0
    this.#size = 0
    if (this.#hasDisposeAfter && this.#disposed) {
      const dt = this.#disposed
      let task: DisposeTask<K, V> | undefined
      while ((task = dt?.shift())) {
        this.#disposeAfter?.(...task)
      }
    }
  }
}
```

## File: `tap-snapshots/test/basic.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/basic.ts > TAP > basic operation > must match snapshot 1`] = `
Generator [
  Array [
    4,
    4,
  ],
  Array [
    3,
    3,
  ],
  Array [
    2,
    2,
  ],
  Array [
    1,
    1,
  ],
  Array [
    0,
    0,
  ],
]
`

exports[`test/basic.ts > TAP > basic operation > must match snapshot 2`] = `
Generator [
  Array [
    9,
    9,
  ],
  Array [
    8,
    8,
  ],
  Array [
    7,
    7,
  ],
  Array [
    6,
    6,
  ],
  Array [
    5,
    5,
  ],
  Array [
    4,
    4,
  ],
  Array [
    3,
    3,
  ],
  Array [
    2,
    2,
  ],
  Array [
    1,
    1,
  ],
  Array [
    0,
    0,
  ],
]
`

exports[`test/basic.ts > TAP > basic operation > must match snapshot 3`] = `
Generator [
  Array [
    4,
    4,
  ],
  Array [
    3,
    3,
  ],
  Array [
    2,
    2,
  ],
  Array [
    1,
    1,
  ],
  Array [
    0,
    0,
  ],
  Array [
    9,
    9,
  ],
  Array [
    8,
    8,
  ],
  Array [
    7,
    7,
  ],
  Array [
    6,
    6,
  ],
  Array [
    5,
    5,
  ],
]
`

exports[`test/basic.ts > TAP > basic operation > must match snapshot 4`] = `
Generator [
  Array [
    14,
    14,
  ],
  Array [
    13,
    13,
  ],
  Array [
    12,
    12,
  ],
  Array [
    11,
    11,
  ],
  Array [
    10,
    10,
  ],
  Array [
    9,
    9,
  ],
  Array [
    8,
    8,
  ],
  Array [
    7,
    7,
  ],
  Array [
    6,
    6,
  ],
  Array [
    5,
    5,
  ],
]
`

exports[`test/basic.ts > TAP > basic operation > must match snapshot 5`] = `
Generator [
  Array [
    19,
    19,
  ],
  Array [
    18,
    18,
  ],
  Array [
    17,
    17,
  ],
  Array [
    16,
    16,
  ],
  Array [
    15,
    15,
  ],
  Array [
    14,
    14,
  ],
  Array [
    13,
    13,
  ],
  Array [
    12,
    12,
  ],
  Array [
    11,
    11,
  ],
  Array [
    10,
    10,
  ],
]
`

exports[`test/basic.ts > TAP > basic operation > must match snapshot 6`] = `
Generator [
  Array [
    19,
    19,
  ],
  Array [
    18,
    18,
  ],
  Array [
    17,
    17,
  ],
  Array [
    16,
    16,
  ],
  Array [
    15,
    15,
  ],
  Array [
    14,
    14,
  ],
  Array [
    13,
    13,
  ],
  Array [
    12,
    12,
  ],
  Array [
    11,
    11,
  ],
  Array [
    10,
    10,
  ],
]
`

exports[`test/basic.ts > TAP > basic operation > status tracking 1`] = `
Array [
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "update",
  },
  Object {
    "set": "update",
  },
  Object {
    "set": "update",
  },
  Object {
    "set": "update",
  },
  Object {
    "set": "update",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "get": "miss",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "has": "hit",
  },
  Object {
    "set": "add",
  },
  Object {
    "has": "hit",
  },
  Object {
    "get": "hit",
  },
  Object {
    "has": "miss",
  },
]
`

exports[`test/basic.ts > TAP > re-use key before initial fill completed > must match snapshot 1`] = `
Array [
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "set": "add",
  },
  Object {
    "oldValue": 1,
    "set": "replace",
  },
  Object {
    "set": "add",
  },
]
`
```

## File: `tap-snapshots/test/deprecations.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/deprecations.ts TAP does not do deprecation warning without process object > warnings sent to console.error 1`] = `
Array [
  Array [
    "The stale option is deprecated. Please use options.allowStale instead.",
    "DeprecationWarning",
    "LRU_CACHE_OPTION_stale",
    Function LRUCache(classLRUCache),
  ],
  Array [
    "The maxAge option is deprecated. Please use options.ttl instead.",
    "DeprecationWarning",
    "LRU_CACHE_OPTION_maxAge",
    Function LRUCache(classLRUCache),
  ],
  Array [
    "The length option is deprecated. Please use options.sizeCalculation instead.",
    "DeprecationWarning",
    "LRU_CACHE_OPTION_length",
    Function LRUCache(classLRUCache),
  ],
  Array [
    "The reset method is deprecated. Please use cache.clear() instead.",
    "DeprecationWarning",
    "LRU_CACHE_METHOD_reset",
    Function get reset(),
  ],
  Array [
    "The length property is deprecated. Please use cache.size instead.",
    "DeprecationWarning",
    "LRU_CACHE_PROPERTY_length",
    Function get length(),
  ],
  Array [
    "The prune method is deprecated. Please use cache.purgeStale() instead.",
    "DeprecationWarning",
    "LRU_CACHE_METHOD_prune",
    Function get prune(),
  ],
  Array [
    "The del method is deprecated. Please use cache.delete() instead.",
    "DeprecationWarning",
    "LRU_CACHE_METHOD_del",
    Function get del(),
  ],
]
`

exports[`test/deprecations.ts TAP warns exactly once for a given deprecation > must match snapshot 1`] = `
Array [
  Array [
    "The stale option is deprecated. Please use options.allowStale instead.",
    "DeprecationWarning",
    "LRU_CACHE_OPTION_stale",
    Function LRUCache(classLRUCache),
  ],
  Array [
    "The maxAge option is deprecated. Please use options.ttl instead.",
    "DeprecationWarning",
    "LRU_CACHE_OPTION_maxAge",
    Function LRUCache(classLRUCache),
  ],
  Array [
    "The length option is deprecated. Please use options.sizeCalculation instead.",
    "DeprecationWarning",
    "LRU_CACHE_OPTION_length",
    Function LRUCache(classLRUCache),
  ],
  Array [
    "The reset method is deprecated. Please use cache.clear() instead.",
    "DeprecationWarning",
    "LRU_CACHE_METHOD_reset",
    Function get reset(),
  ],
  Array [
    "The length property is deprecated. Please use cache.size instead.",
    "DeprecationWarning",
    "LRU_CACHE_PROPERTY_length",
    Function get length(),
  ],
  Array [
    "The prune method is deprecated. Please use cache.purgeStale() instead.",
    "DeprecationWarning",
    "LRU_CACHE_METHOD_prune",
    Function get prune(),
  ],
  Array [
    "The del method is deprecated. Please use cache.delete() instead.",
    "DeprecationWarning",
    "LRU_CACHE_METHOD_del",
    Function get del(),
  ],
  Array [
    "TTL caching without ttlAutopurge, max, or maxSize can result in unbounded memory consumption.",
    "UnboundedCacheWarning",
    "LRU_CACHE_UNBOUNDED",
    Function LRUCache(classLRUCache),
  ],
]
`
```

## File: `tap-snapshots/test/fetch.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/fetch.ts > TAP > asynchronous fetching > safe to stringify dump 1`] = `
[["key",{"value":1,"ttl":5,"start":12}]]
`

exports[`test/fetch.ts > TAP > asynchronous fetching > status 1 1`] = `
Object {
  "fetch": "miss",
  "fetchDispatched": true,
  "fetchResolved": true,
  "fetchUpdated": true,
  "now": 2,
  "remainingTTL": 5,
  "set": "replace",
  "start": 2,
  "ttl": 5,
}
`

exports[`test/fetch.ts > TAP > asynchronous fetching > status 2 1`] = `
Object {
  "fetch": "hit",
  "now": 2,
  "remainingTTL": 5,
  "start": 2,
  "ttl": 5,
}
`

exports[`test/fetch.ts > TAP > asynchronous fetching > status 3 1`] = `
Object {
  "fetch": "stale",
  "fetchDispatched": true,
  "returnedStale": true,
}
`

exports[`test/fetch.ts > TAP > asynchronous fetching > status 3.1 1`] = `
Object {
  "fetch": "inflight",
  "returnedStale": true,
}
`

exports[`test/fetch.ts > TAP > asynchronous fetching > status 4 1`] = `
Object {
  "fetch": "inflight",
}
`

exports[`test/fetch.ts > TAP > asynchronous fetching > status 5 1`] = `
Object {
  "fetch": "hit",
  "now": 12,
  "remainingTTL": 5,
  "start": 12,
  "ttl": 5,
}
`

exports[`test/fetch.ts > TAP > fetch options, signal > status updates 1`] = `
Array [
  Object {
    "fetch": "miss",
    "fetchAborted": true,
    "fetchDispatched": true,
    "fetchError": Error: deleted {
      "name": "Error",
    },
  },
  Object {
    "fetch": "miss",
    "fetchAborted": true,
    "fetchDispatched": true,
    "fetchError": Error: replaced {
      "name": "Error",
    },
  },
  Object {
    "fetch": "miss",
    "fetchAborted": true,
    "fetchDispatched": true,
    "fetchError": Error: evicted {
      "name": "Error",
    },
  },
  Object {
    "now": 722,
    "remainingTTL": 100,
    "set": "add",
    "start": 722,
    "ttl": 100,
  },
  Object {
    "now": 722,
    "remainingTTL": 100,
    "set": "add",
    "start": 722,
    "ttl": 100,
  },
  Object {
    "now": 722,
    "remainingTTL": 100,
    "set": "add",
    "start": 722,
    "ttl": 100,
  },
  Object {
    "fetch": "miss",
    "fetchDispatched": true,
    "fetchResolved": true,
    "fetchUpdated": true,
    "now": 722,
    "remainingTTL": 1000,
    "set": "replace",
    "start": 722,
    "ttl": 1000,
  },
  Object {
    "fetch": "miss",
    "fetchDispatched": true,
    "fetchResolved": true,
    "fetchUpdated": true,
    "now": 722,
    "remainingTTL": 25,
    "set": "replace",
    "start": 722,
    "ttl": 25,
  },
]
`

exports[`test/fetch.ts > TAP > fetch without fetch method > status update 1`] = `
Object {
  "fetch": "get",
  "get": "hit",
}
`

exports[`test/fetch.ts > TAP > fetchMethod throws > status updates 1`] = `
Array [
  Object {
    "now": 722,
    "remainingTTL": 10,
    "set": "add",
    "start": 722,
    "ttl": 10,
  },
  Object {
    "now": 722,
    "remainingTTL": 10,
    "set": "add",
    "start": 722,
    "ttl": 10,
  },
  Object {
    "fetch": "stale",
    "fetchDispatched": true,
    "fetchError": Error: fetch failure,
    "fetchRejected": true,
    "returnedStale": true,
  },
  Object {
    "fetch": "inflight",
    "returnedStale": true,
  },
  Object {
    "fetch": "inflight",
    "returnedStale": true,
  },
  Object {
    "get": "miss",
  },
  Object {
    "fetch": "stale",
    "fetchDispatched": true,
    "fetchError": Error: fetch failure,
    "fetchRejected": true,
    "returnedStale": true,
  },
  Object {
    "fetch": "inflight",
    "returnedStale": true,
  },
  Object {
    "fetch": "inflight",
    "returnedStale": true,
  },
  Object {
    "get": "miss",
  },
  Object {
    "fetch": "miss",
    "fetchAborted": true,
    "fetchDispatched": true,
    "fetchError": Error: replaced {
      "name": "Error",
    },
  },
  Object {
    "now": 782,
    "remainingTTL": 10,
    "set": "replace",
    "start": 782,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 782,
    "remainingTTL": 10,
    "start": 782,
    "ttl": 10,
  },
  Object {
    "fetch": "miss",
    "fetchDispatched": true,
  },
]
`

exports[`test/fetch.ts > TAP > forceRefresh > status updates 1`] = `
Array [
  Object {
    "fetch": "refresh",
    "fetchDispatched": true,
    "fetchResolved": true,
    "fetchUpdated": true,
    "now": 942,
    "oldValue": 2,
    "remainingTTL": 100,
    "set": "replace",
    "start": 942,
    "ttl": 100,
  },
  Object {
    "fetch": "inflight",
  },
  Object {
    "fetch": "refresh",
    "fetchDispatched": true,
    "fetchResolved": true,
    "fetchUpdated": true,
    "now": 942,
    "oldValue": 100,
    "remainingTTL": 100,
    "set": "replace",
    "start": 942,
    "ttl": 100,
  },
]
`

exports[`test/fetch.ts > TAP > send a signal > status updates 1`] = `
Array [
  Object {
    "fetch": "miss",
    "fetchAborted": true,
    "fetchDispatched": true,
    "fetchError": Error: custom abort signal {
      "name": "Error",
    },
  },
  Object {
    "get": "miss",
  },
]
`

exports[`test/fetch.ts > TAP > verify inflight works as expected > status updates 1`] = `
Array [
  Object {
    "fetch": "inflight",
  },
  Object {
    "fetch": "inflight",
  },
  Object {
    "get": "hit",
  },
]
`
```

## File: `tap-snapshots/test/map-like.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/map-like.ts > TAP > bunch of iteration things > dump 1`] = `
Array [
  Array [
    3,
    Object {
      "size": 1,
      "value": "3",
    },
  ],
  Array [
    4,
    Object {
      "size": 1,
      "value": "4",
    },
  ],
  Array [
    5,
    Object {
      "size": 1,
      "value": "5",
    },
  ],
  Array [
    6,
    Object {
      "size": 1,
      "value": "6",
    },
  ],
  Array [
    7,
    Object {
      "size": 1,
      "value": "7",
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > dump, 7 stale 1`] = `
Array [
  Array [
    3,
    Object {
      "size": 1,
      "start": 0,
      "ttl": 0,
      "value": "3",
    },
  ],
  Array [
    5,
    Object {
      "size": 1,
      "start": 0,
      "ttl": 0,
      "value": "5",
    },
  ],
  Array [
    6,
    Object {
      "size": 1,
      "start": 0,
      "ttl": 0,
      "value": "6",
    },
  ],
  Array [
    4,
    Object {
      "size": 1,
      "start": 0,
      "ttl": 0,
      "value": "new value 4",
    },
  ],
  Array [
    7,
    Object {
      "size": 1,
      "start": -9999,
      "ttl": 1,
      "value": "stale",
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > dump, new value 4 1`] = `
Array [
  Array [
    3,
    Object {
      "size": 1,
      "value": "3",
    },
  ],
  Array [
    5,
    Object {
      "size": 1,
      "value": "5",
    },
  ],
  Array [
    6,
    Object {
      "size": 1,
      "value": "6",
    },
  ],
  Array [
    7,
    Object {
      "size": 1,
      "value": "7",
    },
  ],
  Array [
    4,
    Object {
      "size": 1,
      "value": "new value 4",
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > dump, resolved fetch 99 too late 1`] = `
Array [
  Array [
    3,
    Object {
      "size": 1,
      "value": "3",
    },
  ],
  Array [
    5,
    Object {
      "size": 1,
      "value": "5",
    },
  ],
  Array [
    6,
    Object {
      "size": 1,
      "value": "6",
    },
  ],
  Array [
    7,
    Object {
      "size": 1,
      "value": "7",
    },
  ],
  Array [
    4,
    Object {
      "size": 1,
      "value": "new value 4",
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, dump 1`] = `
Array []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, entries 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, foreach 1`] = `
Array []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, keys 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, rentries 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, rforeach 1`] = `
Array []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, rkeys 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, rvalues 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > empty, values 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > entries 1`] = `
Generator [
  Array [
    7,
    "7",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    4,
    "4",
  ],
  Array [
    3,
    "3",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > entries, 7 stale 1`] = `
Generator [
  Array [
    4,
    "new value 4",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    3,
    "3",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > entries, new value 4 1`] = `
Generator [
  Array [
    4,
    "new value 4",
  ],
  Array [
    7,
    "7",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    3,
    "3",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > entries, resolved fetch 99 too late 1`] = `
Generator [
  Array [
    4,
    "new value 4",
  ],
  Array [
    7,
    "7",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    3,
    "3",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, dump 1`] = `
Array [
  Array [
    0,
    Object {
      "size": 1,
      "value": "0",
    },
  ],
  Array [
    1,
    Object {
      "size": 1,
      "value": "1",
    },
  ],
  Array [
    2,
    Object {
      "size": 1,
      "value": "2",
    },
  ],
  Array [
    123,
    Object {
      "size": 1,
      "value": "123",
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, entries 1`] = `
Generator [
  Array [
    123,
    "123",
  ],
  Array [
    2,
    "2",
  ],
  Array [
    1,
    "1",
  ],
  Array [
    0,
    "0",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, foreach 1`] = `
Array [
  Array [
    123,
    "123",
  ],
  Array [
    2,
    "2",
  ],
  Array [
    1,
    "1",
  ],
  Array [
    0,
    "0",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, keys 1`] = `
Generator [
  123,
  2,
  1,
  0,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, rentries 1`] = `
Generator [
  Array [
    0,
    "0",
  ],
  Array [
    1,
    "1",
  ],
  Array [
    2,
    "2",
  ],
  Array [
    123,
    "123",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, rforeach 1`] = `
Array [
  Array [
    0,
    "0",
  ],
  Array [
    1,
    "1",
  ],
  Array [
    2,
    "2",
  ],
  Array [
    123,
    "123",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, rkeys 1`] = `
Generator [
  0,
  1,
  2,
  123,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, rvalues 1`] = `
Generator [
  "0",
  "1",
  "2",
  "123",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > fetch 123 resolved, values 1`] = `
Generator [
  "123",
  "2",
  "1",
  "0",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > forEach, no thisp 1`] = `
Array [
  Array [
    "new value 4",
    4,
  ],
  Array [
    "6",
    6,
  ],
  Array [
    "5",
    5,
  ],
  Array [
    "3",
    3,
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > forEach, with thisp 1`] = `
Array [
  Array [
    "new value 4",
    4,
    Object {
      "a": 1,
    },
  ],
  Array [
    "6",
    6,
    Object {
      "a": 1,
    },
  ],
  Array [
    "5",
    5,
    Object {
      "a": 1,
    },
  ],
  Array [
    "3",
    3,
    Object {
      "a": 1,
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > forEach, with thisp 2`] = `
Array [
  Array [
    "3",
    3,
    Object {
      "r": 1,
    },
  ],
  Array [
    "5",
    5,
    Object {
      "r": 1,
    },
  ],
  Array [
    "6",
    6,
    Object {
      "r": 1,
    },
  ],
  Array [
    "new value 4",
    4,
    Object {
      "r": 1,
    },
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > keys 1`] = `
Generator [
  7,
  6,
  5,
  4,
  3,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > keys, 7 stale 1`] = `
Generator [
  4,
  6,
  5,
  3,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > keys, new value 4 1`] = `
Generator [
  4,
  7,
  6,
  5,
  3,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > keys, resolved fetch 99 too late 1`] = `
Generator [
  4,
  7,
  6,
  5,
  3,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, dump 1`] = `
Array []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, entries 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, foreach 1`] = `
Array []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, keys 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, rentries 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, rforeach 1`] = `
Array []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, rkeys 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, rvalues 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > pending fetch, values 1`] = `
Generator []
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rentries 1`] = `
Generator [
  Array [
    3,
    "3",
  ],
  Array [
    4,
    "4",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    7,
    "7",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rentries, 7 stale 1`] = `
Generator [
  Array [
    3,
    "3",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    4,
    "new value 4",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rentries, new value 4 1`] = `
Generator [
  Array [
    3,
    "3",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    7,
    "7",
  ],
  Array [
    4,
    "new value 4",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rentries, resolved fetch 99 too late 1`] = `
Generator [
  Array [
    3,
    "3",
  ],
  Array [
    5,
    "5",
  ],
  Array [
    6,
    "6",
  ],
  Array [
    7,
    "7",
  ],
  Array [
    4,
    "new value 4",
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rforEach, no thisp 1`] = `
Array [
  Array [
    "3",
    3,
  ],
  Array [
    "5",
    5,
  ],
  Array [
    "6",
    6,
  ],
  Array [
    "new value 4",
    4,
  ],
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rkeys 1`] = `
Generator [
  3,
  4,
  5,
  6,
  7,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rkeys, 7 stale 1`] = `
Generator [
  3,
  5,
  6,
  4,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rkeys, new value 4 1`] = `
Generator [
  3,
  5,
  6,
  7,
  4,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rkeys, resolved fetch 99 too late 1`] = `
Generator [
  3,
  5,
  6,
  7,
  4,
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rvalues 1`] = `
Generator [
  "3",
  "4",
  "5",
  "6",
  "7",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rvalues, 7 stale 1`] = `
Generator [
  "3",
  "5",
  "6",
  "new value 4",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rvalues, new value 4 1`] = `
Generator [
  "3",
  "5",
  "6",
  "7",
  "new value 4",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > rvalues, resolved fetch 99 too late 1`] = `
Generator [
  "3",
  "5",
  "6",
  "7",
  "new value 4",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > values 1`] = `
Generator [
  "7",
  "6",
  "5",
  "4",
  "3",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > values, 7 stale 1`] = `
Generator [
  "new value 4",
  "6",
  "5",
  "3",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > values, new value 4 1`] = `
Generator [
  "new value 4",
  "7",
  "6",
  "5",
  "3",
]
`

exports[`test/map-like.ts > TAP > bunch of iteration things > values, resolved fetch 99 too late 1`] = `
Generator [
  "new value 4",
  "7",
  "6",
  "5",
  "3",
]
`
```

## File: `tap-snapshots/test/move-to-tail.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/move-to-tail.ts > TAP > list integrity > list after initial fill 1`] = `
Array [
  Object {
    "_": "H",
    "head": 0,
    "index": 0,
    "next": 1,
    "prev": 0,
    "tail": 4,
  },
  Object {
    "_": "1",
    "head": 0,
    "index": 1,
    "next": 2,
    "prev": 0,
    "tail": 4,
  },
  Object {
    "_": "2",
    "head": 0,
    "index": 2,
    "next": 3,
    "prev": 1,
    "tail": 4,
  },
  Object {
    "_": "3",
    "head": 0,
    "index": 3,
    "next": 4,
    "prev": 2,
    "tail": 4,
  },
  Object {
    "_": "T",
    "head": 0,
    "index": 4,
    "next": 0,
    "prev": 3,
    "tail": 4,
  },
]
`

exports[`test/move-to-tail.ts > TAP > list integrity > list after moveToTail 2 1`] = `
Array [
  Object {
    "_": "H",
    "head": 0,
    "index": 0,
    "next": 1,
    "prev": 0,
    "tail": 2,
  },
  Object {
    "_": "1",
    "head": 0,
    "index": 1,
    "next": 3,
    "prev": 0,
    "tail": 2,
  },
  Object {
    "_": "T",
    "head": 0,
    "index": 2,
    "next": 3,
    "prev": 4,
    "tail": 2,
  },
  Object {
    "_": "3",
    "head": 0,
    "index": 3,
    "next": 4,
    "prev": 1,
    "tail": 2,
  },
  Object {
    "_": "4",
    "head": 0,
    "index": 4,
    "next": 2,
    "prev": 3,
    "tail": 2,
  },
]
`

exports[`test/move-to-tail.ts > TAP > list integrity > list after moveToTail 4 1`] = `
Array [
  Object {
    "_": "H",
    "head": 0,
    "index": 0,
    "next": 1,
    "prev": 0,
    "tail": 4,
  },
  Object {
    "_": "1",
    "head": 0,
    "index": 1,
    "next": 3,
    "prev": 0,
    "tail": 4,
  },
  Object {
    "_": "2",
    "head": 0,
    "index": 2,
    "next": 4,
    "prev": 3,
    "tail": 4,
  },
  Object {
    "_": "3",
    "head": 0,
    "index": 3,
    "next": 2,
    "prev": 1,
    "tail": 4,
  },
  Object {
    "_": "T",
    "head": 0,
    "index": 4,
    "next": 2,
    "prev": 2,
    "tail": 4,
  },
]
`
```

## File: `tap-snapshots/test/size-calculation.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/size-calculation.ts > TAP > large item falls out of cache because maxEntrySize > status updates 1`] = `
Array [
  Object {
    "entrySize": 2,
    "set": "add",
    "totalCalculatedSize": 2,
  },
  Object {
    "maxEntrySizeExceeded": true,
    "set": "miss",
  },
  Object {
    "entrySize": 3,
    "set": "add",
    "totalCalculatedSize": 3,
  },
  Object {
    "maxEntrySizeExceeded": true,
    "set": "miss",
  },
]
`

exports[`test/size-calculation.ts > TAP > large item falls out of cache, sizes are kept correct > status updates 1`] = `
Array [
  Object {
    "entrySize": 2,
    "set": "add",
    "totalCalculatedSize": 2,
  },
  Object {
    "maxEntrySizeExceeded": true,
    "set": "miss",
  },
  Object {
    "entrySize": 3,
    "set": "add",
    "totalCalculatedSize": 3,
  },
  Object {
    "maxEntrySizeExceeded": true,
    "set": "miss",
  },
]
`

exports[`test/size-calculation.ts > TAP > store strings, size = length > dump 1`] = `
Array [
  Array [
    "repeated",
    Object {
      "size": 10,
      "value": "jjjjjjjjjj",
    },
  ],
]
`
```

## File: `tap-snapshots/test/ttl.ts.test.cjs`
```
/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/ttl.ts > TAP > tests using Date.now() > set item pre-stale > dump with stale values 1`] = `
Array [
  Array [
    1,
    Object {
      "start": 3316,
      "ttl": 10,
      "value": 1,
    },
  ],
  Array [
    2,
    Object {
      "start": 3305,
      "ttl": 10,
      "value": 2,
    },
  ],
]
`

exports[`test/ttl.ts > TAP > tests using Date.now() > ttl on set, not on cache > status updates 1`] = `
Array [
  Object {
    "now": 2259,
    "remainingTTL": 10,
    "set": "add",
    "start": 2259,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2259,
    "remainingTTL": 10,
    "start": 2259,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2264,
    "remainingTTL": 5,
    "start": 2259,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2269,
    "remainingTTL": 0,
    "start": 2259,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 2270,
    "remainingTTL": -1,
    "start": 2259,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 2270,
    "remainingTTL": -1,
    "start": 2259,
    "ttl": 10,
  },
  Object {
    "now": 2270,
    "remainingTTL": 100,
    "set": "add",
    "start": 2270,
    "ttl": 100,
  },
  Object {
    "has": "hit",
    "now": 2320,
    "remainingTTL": 50,
    "start": 2270,
    "ttl": 100,
  },
  Object {
    "get": "hit",
    "now": 2320,
    "remainingTTL": 50,
    "start": 2270,
    "ttl": 100,
  },
  Object {
    "has": "stale",
    "now": 2371,
    "remainingTTL": -1,
    "start": 2270,
    "ttl": 100,
  },
  Object {
    "get": "stale",
    "now": 2371,
    "remainingTTL": -1,
    "start": 2270,
    "ttl": 100,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "now": 2371,
    "remainingTTL": 10,
    "set": "add",
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 2382,
    "remainingTTL": -1,
    "start": 2371,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 2382,
    "remainingTTL": -1,
    "start": 2371,
    "ttl": 10,
  },
]
`

exports[`test/ttl.ts > TAP > tests using Date.now() > ttl tests defaults > status updates 1`] = `
Array [
  Object {
    "now": 1812,
    "remainingTTL": 10,
    "set": "add",
    "start": 1812,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 1812,
    "remainingTTL": 10,
    "start": 1812,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 1817,
    "remainingTTL": 5,
    "start": 1812,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 1822,
    "remainingTTL": 0,
    "start": 1812,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 1824,
    "remainingTTL": -2,
    "start": 1812,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 1824,
    "remainingTTL": -2,
    "start": 1812,
    "ttl": 10,
  },
  Object {
    "has": "hit",
    "now": 1874,
    "remainingTTL": 50,
    "start": 1824,
    "ttl": 100,
  },
  Object {
    "get": "hit",
    "now": 1874,
    "remainingTTL": 50,
    "start": 1824,
    "ttl": 100,
  },
  Object {
    "get": "stale",
    "now": 1925,
    "remainingTTL": -1,
    "start": 1824,
    "ttl": 100,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "now": 1925,
    "remainingTTL": 10,
    "set": "add",
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 1936,
    "remainingTTL": -1,
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 1936,
    "remainingTTL": -1,
    "start": 1925,
    "ttl": 10,
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
]
`

exports[`test/ttl.ts > TAP > tests using Date.now() > ttl tests with ttlResolution=100 > status updates 1`] = `
Array [
  Object {
    "now": 2136,
    "remainingTTL": 10,
    "set": "add",
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2136,
    "remainingTTL": 10,
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2136,
    "remainingTTL": 10,
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2136,
    "remainingTTL": 10,
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "has": "hit",
    "now": 2136,
    "remainingTTL": 10,
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2136,
    "remainingTTL": 10,
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 2247,
    "remainingTTL": -101,
    "start": 2136,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 2247,
    "remainingTTL": -101,
    "start": 2136,
    "ttl": 10,
  },
]
`

exports[`test/ttl.ts > TAP > tests using Date.now() > ttlAutopurge > status updates 1`] = `
Array [
  Object {
    "now": 2247,
    "remainingTTL": 10,
    "set": "add",
    "start": 2247,
    "ttl": 10,
  },
  Object {
    "now": 2247,
    "remainingTTL": 10,
    "set": "add",
    "start": 2247,
    "ttl": 10,
  },
  Object {
    "now": 2247,
    "oldValue": 2,
    "remainingTTL": 11,
    "set": "replace",
    "start": 2247,
    "ttl": 11,
  },
]
`

exports[`test/ttl.ts > TAP > tests with perf_hooks.performance.now() > set item pre-stale > dump with stale values 1`] = `
Array [
  Array [
    1,
    Object {
      "start": 1506,
      "ttl": 10,
      "value": 1,
    },
  ],
  Array [
    2,
    Object {
      "start": 1495,
      "ttl": 10,
      "value": 2,
    },
  ],
]
`

exports[`test/ttl.ts > TAP > tests with perf_hooks.performance.now() > ttl on set, not on cache > status updates 1`] = `
Array [
  Object {
    "now": 449,
    "remainingTTL": 10,
    "set": "add",
    "start": 449,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 449,
    "remainingTTL": 10,
    "start": 449,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 454,
    "remainingTTL": 5,
    "start": 449,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 459,
    "remainingTTL": 0,
    "start": 449,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 460,
    "remainingTTL": -1,
    "start": 449,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 460,
    "remainingTTL": -1,
    "start": 449,
    "ttl": 10,
  },
  Object {
    "now": 460,
    "remainingTTL": 100,
    "set": "add",
    "start": 460,
    "ttl": 100,
  },
  Object {
    "has": "hit",
    "now": 510,
    "remainingTTL": 50,
    "start": 460,
    "ttl": 100,
  },
  Object {
    "get": "hit",
    "now": 510,
    "remainingTTL": 50,
    "start": 460,
    "ttl": 100,
  },
  Object {
    "has": "stale",
    "now": 561,
    "remainingTTL": -1,
    "start": 460,
    "ttl": 100,
  },
  Object {
    "get": "stale",
    "now": 561,
    "remainingTTL": -1,
    "start": 460,
    "ttl": 100,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "now": 561,
    "remainingTTL": 10,
    "set": "add",
    "start": 561,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 572,
    "remainingTTL": -1,
    "start": 561,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 572,
    "remainingTTL": -1,
    "start": 561,
    "ttl": 10,
  },
]
`

exports[`test/ttl.ts > TAP > tests with perf_hooks.performance.now() > ttl tests defaults > status updates 1`] = `
Array [
  Object {
    "now": 2,
    "remainingTTL": 10,
    "set": "add",
    "start": 2,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 2,
    "remainingTTL": 10,
    "start": 2,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 7,
    "remainingTTL": 5,
    "start": 2,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 12,
    "remainingTTL": 0,
    "start": 2,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 14,
    "remainingTTL": -2,
    "start": 2,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 14,
    "remainingTTL": -2,
    "start": 2,
    "ttl": 10,
  },
  Object {
    "has": "hit",
    "now": 64,
    "remainingTTL": 50,
    "start": 14,
    "ttl": 100,
  },
  Object {
    "get": "hit",
    "now": 64,
    "remainingTTL": 50,
    "start": 14,
    "ttl": 100,
  },
  Object {
    "get": "stale",
    "now": 115,
    "remainingTTL": -1,
    "start": 14,
    "ttl": 100,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "now": 115,
    "remainingTTL": 10,
    "set": "add",
    "start": 115,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 126,
    "remainingTTL": -1,
    "start": 115,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 126,
    "remainingTTL": -1,
    "start": 115,
    "ttl": 10,
  },
  Object {
    "get": "hit",
  },
  Object {
    "get": "hit",
  },
]
`

exports[`test/ttl.ts > TAP > tests with perf_hooks.performance.now() > ttl tests with ttlResolution=100 > status updates 1`] = `
Array [
  Object {
    "now": 326,
    "remainingTTL": 10,
    "set": "add",
    "start": 326,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 326,
    "remainingTTL": 10,
    "start": 326,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 326,
    "remainingTTL": 10,
    "start": 326,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 326,
    "remainingTTL": 10,
    "start": 326,
    "ttl": 10,
  },
  Object {
    "has": "hit",
    "now": 326,
    "remainingTTL": 10,
    "start": 326,
    "ttl": 10,
  },
  Object {
    "get": "hit",
    "now": 326,
    "remainingTTL": 10,
    "start": 326,
    "ttl": 10,
  },
  Object {
    "has": "stale",
    "now": 437,
    "remainingTTL": -101,
    "start": 326,
    "ttl": 10,
  },
  Object {
    "get": "stale",
    "now": 437,
    "remainingTTL": -101,
    "start": 326,
    "ttl": 10,
  },
]
`

exports[`test/ttl.ts > TAP > tests with perf_hooks.performance.now() > ttlAutopurge > status updates 1`] = `
Array [
  Object {
    "now": 437,
    "remainingTTL": 10,
    "set": "add",
    "start": 437,
    "ttl": 10,
  },
  Object {
    "now": 437,
    "remainingTTL": 10,
    "set": "add",
    "start": 437,
    "ttl": 10,
  },
  Object {
    "now": 437,
    "oldValue": 2,
    "remainingTTL": 11,
    "set": "replace",
    "start": 437,
    "ttl": 11,
  },
]
`
```

## File: `test/avoid-memory-leak.ts`
```typescript
#!/usr/bin/env node --no-warnings --loader=ts-node/esm --expose-gc

// https://github.com/isaacs/node-lru-cache/issues/227

import t, { Test } from 'tap'
import { expose } from './fixtures/expose.js'

const maxSize = 100_000
const itemSize = 1_000
const profEvery = 10_000
const n = 1_000_000

if (typeof gc !== 'function') {
  t.plan(0, 'run with --expose-gc')
  process.exit(0)
}

const req = createRequire(import.meta.url)
const tryReq = (mod: string) => {
  try {
    return req(mod)
  } catch (er) {
    t.plan(0, `need ${mod} module`)
    process.exit(0)
  }
}

const v8 = tryReq('v8')

import { LRUCache } from '../dist/esm/index.js'
import { createRequire } from 'module'
const expectItemCount = Math.ceil(maxSize / itemSize)
const max = expectItemCount + 1
const keyRange = expectItemCount * 2

// fine to alloc unsafe, we don't ever look at the data
const makeItem = () => Buffer.allocUnsafe(itemSize)

const prof = (i: number, cache: LRUCache<number, any>) => {
  // run gc so that we know if we're actually leaking memory, or just
  // that the gc is being lazy and not responding until there's memory
  // pressure.
  // @ts-ignore
  gc()
  return {
    i,
    ...v8.getHeapStatistics(),
    valListLength: expose(cache).valList.length,
    freeLength: expose(cache).free.length,
  }
}

const runTest = async (t: Test, cache: LRUCache<any, any>) => {
  // first, fill to expected size
  for (let i = 0; i < expectItemCount; i++) {
    cache.set(i, makeItem())
  }

  // now start the setting and profiling
  const profiles: ReturnType<typeof prof>[] = []
  for (let i = 0; i < n; i++) {
    if (i % profEvery === 0) {
      const profile = prof(i, cache)
      t.ok(
        profile.valListLength <= max,
        `expect valList to have fewer than ${max} items`,
        { found: profile.valListLength },
      )
      t.ok(
        profile.freeLength <= 1,
        'expect free stack to have <= 1 item',
        { found: profile.freeLength },
      )
      t.ok(
        profile.number_of_native_contexts <= 2,
        'expect only 1 or 2 native contexts',
        { found: profile.number_of_native_contexts },
      )
      t.equal(
        profile.number_of_detached_contexts,
        0,
        '0 detached contexts',
      )
      profiles.push(profile)
    }

    const item = makeItem()
    cache.set(i % keyRange, item)
  }

  const profile = prof(n, cache)
  profiles.push(profile)

  // Warning: kludgey inexact test!
  // memory leaks can be hard to catch deterministically.
  // The first few items will tend to be lower, and we'll see
  // *some* modest increase in heap usage from tap itself as it
  // runs the test and builds up its internal results data.
  // But, after the initial few profiles, it should be modest.
  // Considering that the reported bug showed a 10x increase in
  // memory in this reproduction case, 2x is still pretty aggressive,
  // without risking false hits from other node or tap stuff.

  const start = Math.floor(profiles.length / 2)
  const initial = profiles[start]
  for (let i = start; i < profiles.length; i++) {
    const current = profiles[i]
    const delta = current.total_heap_size / initial.total_heap_size
    t.ok(delta < 2, 'memory growth should not be unbounded', {
      delta,
      current,
      initial,
    })
  }
}

t.test('both max and maxSize', t =>
  runTest(
    t,
    new LRUCache({
      maxSize,
      sizeCalculation: s => s.length,
      max,
    }),
  ),
)

t.test('no max, only maxSize', t =>
  runTest(
    t,
    new LRUCache({
      maxSize,
      sizeCalculation: s => s.length,
    }),
  ),
)

t.test('only max, no maxSize', t => runTest(t, new LRUCache({ max })))
```

## File: `test/basic.ts`
```typescript
import { createRequire } from 'module'
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

t.test('verify require works as expected', async t => {
  const req = createRequire(import.meta.url)
  t.equal(
    req.resolve('../'),
    req.resolve('../dist/commonjs/index.min.js'),
    'require resolves to expected module',
  )
  const { LRUCache } = await t.mockImport('../dist/esm/index.js')
  const { LRUCache: LRUCacheRaw } = await t.mockImport('lru-cache/raw')
  t.equal(LRUCache.toString().split(/\r?\n/)[0].trim(), 'class LRUCache {')
  t.equal(
    LRUCache.toString(),
    LRUCacheRaw.toString(),
    './raw endpoint is unminified',
  )
  const { LRUCache: LRUCacheMain } = await t.mockImport('lru-cache')
  const { LRUCache: LRUCacheMin } = await t.mockImport(
    '../dist/esm/index.min.js',
  )
  t.equal(LRUCacheMin.toString(), LRUCacheMain.toString())
})

t.test('basic operation', t => {
  const statuses: LRU.Status<number>[] = []
  const s = (): LRU.Status<number> => {
    const status: LRU.Status<number> = {}
    statuses.push(status)
    return status
  }

  //@ts-expect-error
  t.throws(() => new LRU({ max: 10, perf: {} }), {
    name: 'TypeError',
    message: 'perf option must have a now() method if specified',
  })

  const c = new LRU({ max: 10, perf: Date })
  t.equal(c.perf, Date)
  for (let i = 0; i < 5; i++) {
    t.equal(c.set(i, i, { status: s() }), c)
  }
  for (let i = 0; i < 5; i++) {
    t.equal(c.get(i, { status: s() }), i)
  }
  t.equal(c.size, 5)
  t.matchSnapshot(c.entries())
  t.equal(c.getRemainingTTL(1), Infinity, 'no ttl, so returns Infinity')
  t.equal(c.getRemainingTTL('not in cache'), 0, 'not in cache, no ttl')

  for (let i = 5; i < 10; i++) {
    c.set(i, i, { status: s() })
  }
  // second time to get the update statuses
  for (let i = 5; i < 10; i++) {
    c.set(i, i, { status: s() })
  }
  t.equal(c.size, 10)
  t.matchSnapshot(c.entries())

  for (let i = 0; i < 5; i++) {
    // this doesn't do anything, but shouldn't be a problem.
    c.get(i, { updateAgeOnGet: true, status: s() })
  }
  t.equal(c.size, 10)
  t.matchSnapshot(c.entries())

  for (let i = 5; i < 10; i++) {
    c.get(i, { status: s() })
  }
  for (let i = 10; i < 15; i++) {
    c.set(i, i, { status: s() })
  }
  t.equal(c.size, 10)
  t.matchSnapshot(c.entries())

  for (let i = 15; i < 20; i++) {
    c.set(i, i, { status: s() })
  }
  // got pruned and replaced
  t.equal(c.size, 10)
  t.matchSnapshot(c.entries())

  for (let i = 0; i < 10; i++) {
    t.equal(c.get(i, { status: s() }), undefined)
  }
  t.matchSnapshot(c.entries())

  for (let i = 0; i < 9; i++) {
    c.set(i, i)
  }
  t.equal(c.size, 10)
  t.equal(c.delete(19), true)
  t.equal(c.delete(19), false)
  t.equal(c.size, 9)
  c.set(10, 10, { status: s() })
  t.equal(c.size, 10)

  c.clear()
  t.equal(c.size, 0)
  for (let i = 0; i < 10; i++) {
    c.set(i, i, { status: s() })
  }
  t.equal(c.size, 10)
  t.equal(c.has(0, { status: s() }), true)
  t.equal(c.size, 10)
  c.set(true, 'true', { status: s() })
  t.equal(c.has(true, { status: s() }), true)
  t.equal(c.get(true, { status: s() }), 'true')
  c.set(true, undefined)
  t.equal(c.has(true, { status: s() }), false)

  t.matchSnapshot(statuses, 'status tracking')
  t.end()
})

t.test('bad max values', t => {
  // @ts-expect-error
  t.throws(() => new LRU())
  // @ts-expect-error
  t.throws(() => new LRU(123))
  // @ts-expect-error
  t.throws(() => new LRU({}))
  // @ts-expect-error
  t.throws(() => new LRU(null))
  t.throws(() => new LRU({ max: -123 }))
  t.throws(() => new LRU({ max: 0 }))
  t.throws(() => new LRU({ max: 2.5 }))
  t.throws(() => new LRU({ max: Infinity }))
  t.throws(() => new LRU({ max: Number.MAX_SAFE_INTEGER * 2 }))

  // ok to have a max of 0 if maxSize or ttl are set
  const sizeOnly = new LRU({ maxSize: 100 })

  // setting the size to invalid values
  t.throws(() => sizeOnly.set('foo', 'bar'), TypeError)
  t.throws(() => sizeOnly.set('foo', 'bar', { size: 0 }), TypeError)
  t.throws(() => sizeOnly.set('foo', 'bar', { size: -1 }), TypeError)
  t.throws(
    () =>
      sizeOnly.set('foo', 'bar', {
        sizeCalculation: () => -1,
      }),
    TypeError,
  )
  t.throws(
    () =>
      sizeOnly.set('foo', 'bar', {
        sizeCalculation: () => 0,
      }),
    TypeError,
  )

  const ttlOnly = new LRU({ ttl: 1000, ttlAutopurge: true })
  // cannot set size when not tracking size
  t.throws(() => ttlOnly.set('foo', 'bar', { size: 1 }), TypeError)
  t.throws(() => ttlOnly.set('foo', 'bar', { size: 1 }), TypeError)

  const sizeTTL = new LRU({ maxSize: 100, ttl: 1000 })
  t.type(sizeTTL, LRU)
  t.end()
})

t.test('setting ttl with non-integer values', t => {
  t.throws(() => new LRU({ max: 10, ttl: 10.5 }), TypeError)
  t.throws(() => new LRU({ max: 10, ttl: -10 }), TypeError)
  // @ts-expect-error
  t.throws(() => new LRU({ max: 10, ttl: 'banana' }), TypeError)
  t.throws(() => new LRU({ max: 10, ttl: Infinity }), TypeError)
  t.end()
})

t.test('setting maxSize with non-integer values', t => {
  t.throws(() => new LRU({ max: 10, maxSize: 10.5 }), TypeError)
  t.throws(() => new LRU({ max: 10, maxSize: -10 }), TypeError)
  t.throws(() => new LRU({ max: 10, maxEntrySize: 10.5 }), TypeError)
  t.throws(() => new LRU({ max: 10, maxEntrySize: -10 }), TypeError)
  t.throws(
    // @ts-expect-error
    () => new LRU({ max: 10, maxEntrySize: 'banana' }),
    TypeError,
  )
  t.throws(() => new LRU({ max: 10, maxEntrySize: Infinity }), TypeError)
  // @ts-expect-error
  t.throws(() => new LRU({ max: 10, maxSize: 'banana' }), TypeError)
  t.throws(() => new LRU({ max: 10, maxSize: Infinity }), TypeError)
  t.end()
})

t.test('bad sizeCalculation', t => {
  t.throws(() => {
    // @ts-expect-error
    new LRU({ max: 1, sizeCalculation: true })
  }, TypeError)
  t.throws(() => {
    // @ts-expect-error
    new LRU({ max: 1, maxSize: 1, sizeCalculation: true })
  }, TypeError)
  t.end()
})

t.test('delete from middle, reuses that index', t => {
  const c = new LRU({ max: 5 })
  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  c.delete(2)
  c.set(5, 5)
  t.strictSame(expose(c).valList, [0, 1, 5, 3, 4])
  t.end()
})

t.test('peek does not disturb order', t => {
  const c = new LRU({ max: 5 })
  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  t.equal(c.peek(2), 2)
  t.strictSame([...c.values()], [4, 3, 2, 1, 0])
  t.end()
})

t.test('re-use key before initial fill completed', t => {
  const statuses: LRU.Status<number>[] = []
  const s = (): LRU.Status<number> => {
    const status: LRU.Status<number> = {}
    statuses.push(status)
    return status
  }

  const c = new LRU({ max: 5 })
  c.set(0, 0, { status: s() })
  c.set(1, 1, { status: s() })
  c.set(2, 2, { status: s() })
  c.set(1, 2, { status: s() })
  c.set(3, 3, { status: s() })
  t.same(
    [...c.entries()],
    [
      [3, 3],
      [1, 2],
      [2, 2],
      [0, 0],
    ],
  )
  t.matchSnapshot(statuses)
  t.end()
})
```

## File: `test/delete-while-iterating.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'

t.beforeEach(t => {
  const c = new LRU({ max: 5 })
  c.set(0, 0)
  c.set(1, 1)
  c.set(2, 2)
  c.set(3, 3)
  c.set(4, 4)
  t.context = c
})

t.test('delete evens', t => {
  const c = t.context
  t.same([...c.keys()], [4, 3, 2, 1, 0])

  for (const k of c.keys()) {
    if (k % 2 === 0) {
      c.delete(k)
    }
  }

  t.same([...c.keys()], [3, 1])
  t.end()
})

t.test('delete odds', t => {
  const c = t.context
  t.same([...c.keys()], [4, 3, 2, 1, 0])

  for (const k of c.keys()) {
    if (k % 2 === 1) {
      c.delete(k)
    }
  }

  t.same([...c.keys()], [4, 2, 0])
  t.end()
})

t.test('rdelete evens', t => {
  const c = t.context
  t.same([...c.keys()], [4, 3, 2, 1, 0])

  for (const k of c.rkeys()) {
    if (k % 2 === 0) {
      c.delete(k)
    }
  }

  t.same([...c.keys()], [3, 1])
  t.end()
})

t.test('rdelete odds', t => {
  const c = t.context
  t.same([...c.keys()], [4, 3, 2, 1, 0])

  for (const k of c.rkeys()) {
    if (k % 2 === 1) {
      c.delete(k)
    }
  }

  t.same([...c.keys()], [4, 2, 0])
  t.end()
})

t.test('delete two of them', t => {
  const c = t.context
  t.same([...c.keys()], [4, 3, 2, 1, 0])
  for (const k of c.keys()) {
    if (k === 3) {
      c.delete(3)
      c.delete(4)
    } else if (k === 1) {
      c.delete(1)
      c.delete(0)
    }
  }
  t.same([...c.keys()], [2])
  t.end()
})

t.test('rdelete two of them', t => {
  const c = t.context
  t.same([...c.keys()], [4, 3, 2, 1, 0])
  for (const k of c.rkeys()) {
    if (k === 3) {
      c.delete(3)
      c.delete(4)
    } else if (k === 1) {
      c.delete(1)
      c.delete(0)
    }
  }
  t.same([...c.keys()], [2])
  t.end()
})
```

## File: `test/dispose.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'
import { LRUCache } from '../src/index.js'

t.test('disposal', t => {
  const disposed: any[] = []
  const c = new LRU({
    max: 5,
    dispose: (k, v, r) => disposed.push([k, v, r]),
  })
  for (let i = 0; i < 9; i++) {
    c.set(i, i)
  }
  t.strictSame(disposed, [
    [0, 0, 'evict'],
    [1, 1, 'evict'],
    [2, 2, 'evict'],
    [3, 3, 'evict'],
  ])
  t.equal(c.size, 5)

  c.set(9, 9)
  t.strictSame(disposed, [
    [0, 0, 'evict'],
    [1, 1, 'evict'],
    [2, 2, 'evict'],
    [3, 3, 'evict'],
    [4, 4, 'evict'],
  ])

  disposed.length = 0
  c.set('asdf', 'foo')
  c.set('asdf', 'asdf')
  t.strictSame(disposed, [
    [5, 5, 'evict'],
    ['foo', 'asdf', 'set'],
  ])

  disposed.length = 0
  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  t.strictSame(disposed, [
    [6, 6, 'evict'],
    [7, 7, 'evict'],
    [8, 8, 'evict'],
    [9, 9, 'evict'],
    ['asdf', 'asdf', 'evict'],
  ])

  // dispose both old and current
  disposed.length = 0
  c.set('asdf', 'foo')
  c.delete('asdf')
  t.strictSame(disposed, [
    [0, 0, 'evict'],
    ['foo', 'asdf', 'delete'],
  ])

  // delete non-existing key, no disposal
  disposed.length = 0
  c.delete('asdf')
  t.strictSame(disposed, [])

  // delete via clear()
  disposed.length = 0
  c.clear()
  t.strictSame(disposed, [
    [1, 1, 'delete'],
    [2, 2, 'delete'],
    [3, 3, 'delete'],
    [4, 4, 'delete'],
  ])

  disposed.length = 0
  c.set(3, 3)
  t.equal(c.get(3), 3)
  c.delete(3)
  t.strictSame(disposed, [[3, 3, 'delete']])

  // disposed because of being overwritten
  c.clear()
  disposed.length = 0
  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  c.set(2, 'two')
  t.strictSame(disposed, [[2, 2, 'set']])
  for (let i = 0; i < 5; i++) {
    t.equal(c.get(i), i === 2 ? 'two' : i)
  }
  t.strictSame(disposed, [[2, 2, 'set']])

  c.noDisposeOnSet = true
  c.clear()
  disposed.length = 0
  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  c.set(2, 'two')
  for (let i = 0; i < 5; i++) {
    t.equal(c.get(i), i === 2 ? 'two' : i)
  }
  t.strictSame(disposed, [])

  t.end()
})

t.test('noDisposeOnSet with delete()', t => {
  const disposed: [any, any][] = []
  const dispose = (v: any, k: any) => disposed.push([v, k])

  const c = new LRU({ max: 5, dispose, noDisposeOnSet: true })
  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  for (let i = 0; i < 4; i++) {
    c.set(i, `new ${i}`)
  }
  t.strictSame(disposed, [])
  c.delete(0)
  c.delete(4)
  t.strictSame(disposed, [
    ['new 0', 0],
    [4, 4],
  ])
  disposed.length = 0

  const d = new LRU({ max: 5, dispose })
  for (let i = 0; i < 5; i++) {
    d.set(i, i)
  }
  for (let i = 0; i < 4; i++) {
    d.set(i, `new ${i}`)
  }
  t.strictSame(disposed, [
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
  ])
  d.delete(0)
  d.delete(4)
  t.strictSame(disposed, [
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    ['new 0', 0],
    [4, 4],
  ])

  t.end()
})

t.test('disposeAfter', t => {
  const c = new LRU({
    max: 5,
    disposeAfter: (v, k) => {
      if (k === 2) {
        // increment it every time it gets disposed, but only one time
        c.set(k, (v as number) + 1, { noDisposeOnSet: true })
      }
    },
  })

  for (let i = 0; i < 100; i++) {
    c.set(i, i)
  }
  t.same(
    [...c.entries()],
    [
      [99, 99],
      [98, 98],
      [2, 21],
      [97, 97],
      [96, 96],
    ],
  )
  c.delete(2)
  t.same(
    [...c.entries()],
    [
      [2, 22],
      [99, 99],
      [98, 98],
      [97, 97],
      [96, 96],
    ],
  )
  for (let i = 96; i < 100; i++) {
    c.set(i, i + 1)
  }
  t.same(
    [...c.entries()],
    [
      [99, 100],
      [98, 99],
      [97, 98],
      [96, 97],
      [2, 22],
    ],
  )
  c.clear()
  t.same([...c.entries()], [[2, 23]])

  t.end()
})

t.test('expiration reflected in dispose reason', async t => {
  t.clock.enter()
  t.clock.advance(1)
  const disposes: [number, number, LRUCache.DisposeReason][] = []
  const c = new LRUCache<number, number>({
    ttl: 100,
    max: 5,
    dispose: (v, k, r) => disposes.push([k, v, r]),
  })
  c.set(1, 1)
  c.set(2, 2, { ttl: 10 })
  c.set(3, 3)
  c.set(4, 4)
  c.set(5, 5)
  t.strictSame(disposes, [])
  c.set(6, 6)
  t.strictSame(disposes, [[1, 1, 'evict']])
  c.delete(6)
  c.delete(5)
  c.delete(4)
  // test when it's the last one, and when it's not, because we
  // delete with cache.clear() when it's the only entry.
  t.strictSame(disposes, [
    [1, 1, 'evict'],
    [6, 6, 'delete'],
    [5, 5, 'delete'],
    [4, 4, 'delete'],
  ])
  t.clock.advance(20)
  t.equal(c.get(2), undefined)
  t.strictSame(disposes, [
    [1, 1, 'evict'],
    [6, 6, 'delete'],
    [5, 5, 'delete'],
    [4, 4, 'delete'],
    [2, 2, 'expire'],
  ])
  t.clock.advance(200)
  t.equal(c.get(3), undefined)
  t.strictSame(disposes, [
    [1, 1, 'evict'],
    [6, 6, 'delete'],
    [5, 5, 'delete'],
    [4, 4, 'delete'],
    [2, 2, 'expire'],
    [3, 3, 'expire'],
  ])
})
```

## File: `test/esm-load.mjs`
```
import t from 'tap'
import { LRUCache } from '../dist/esm/index.js'
const c = new LRUCache({ max: 2 })
t.type(c, LRUCache)
c.set(1, 1)
c.set(2, 2)
c.set(3, 3)
t.equal(c.get(1), undefined)
t.equal(c.get(2), 2)
t.equal(c.get(3), 3)
```

## File: `test/fetch.ts`
```typescript
import t from 'tap'
import { BackgroundFetch, LRUCache } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

t.teardown(() => {})

const fn: LRUCache.Fetcher<any, any> = async (_, v) =>
  new Promise(res =>
    queueMicrotask(() => res(v === undefined ? 0 : v + 1)),
  )

const clock = t.clock
clock.enter()
clock.advance(1)

let LRU = LRUCache

const c = new LRU<string, number>({
  fetchMethod: fn,
  max: 5,
  ttl: 5,
})

const getStatusObj = (): LRUCache.Status<number> => ({})

t.test('asynchronous fetching', async t => {
  const s1 = getStatusObj()
  const v1 = await c.fetch('key', { status: s1 })
  t.equal(v1, 0, 'first fetch, no stale data, wait for initial value')
  t.matchSnapshot(s1, 'status 1')
  const s2 = getStatusObj()
  const v2 = await c.fetch('key', { status: s2 })
  t.equal(v2, 0, 'got same cached value')
  t.matchSnapshot(s2, 'status 2')

  clock.advance(10)

  const s3 = getStatusObj()
  const v3 = await c.fetch('key', { allowStale: true, status: s3 })
  t.equal(v3, 0, 'fetch while stale, allowStale, get stale data')
  t.matchSnapshot(s3, 'status 3')
  const s31 = getStatusObj()
  t.equal(
    await c.fetch('key', { allowStale: true, status: s31 }),
    0,
    'get stale data again while re-fetching because stale previously',
  )
  t.matchSnapshot(s31, 'status 3.1')
  const s4 = getStatusObj()
  const v4 = await c.fetch('key', { status: s4 })
  t.equal(v4, 1, 'no allow stale, wait until fresh data available')
  t.matchSnapshot(s4, 'status 4')
  const s5 = getStatusObj()
  const v5 = await c.fetch('key', { status: s5 })
  t.equal(v5, 1, 'fetch while not stale, just get from cache')
  t.matchSnapshot(s5, 'status 5')

  clock.advance(10)

  const v6 = await c.fetch('key', { allowStale: true })
  t.equal(v6, 1, 'fetch while stale, starts new fetch, return stale data')
  const e = expose(c)
  const v = e.valList[0]

  // should not have any promises or cycles in the dump
  const dump = c.dump()
  for (const [_, entry] of dump) {
    t.type(entry.value, 'number')
  }
  t.matchSnapshot(JSON.stringify(dump), 'safe to stringify dump')

  t.equal(e.isBackgroundFetch(v), true)
  t.equal(e.backgroundFetch('key', 0, {}, undefined), v)
  await v
  const v7 = await c.fetch('key', {
    allowStale: true,
    updateAgeOnGet: true,
  })
  t.equal(v7, 2, 'fetch completed, so get new data')

  clock.advance(100)

  const v8 = await c.fetch('key', { allowStale: true })
  const v9 = c.get('key', { allowStale: true })
  t.equal(v8, 2, 'fetch returned stale while fetching')
  t.equal(v9, 2, 'get() returned stale while fetching')

  const v10 = c.fetch('key2')
  const v11 = c.get('key2')
  t.equal(v11, undefined, 'get while fetching but not yet returned')
  t.equal(await v10, 0, 'eventually 0 is returned')
  const v12 = c.get('key2')
  t.equal(v12, 0, 'get cached value after fetch')

  const v13 = c.fetch('key3')
  c.delete('key3')
  await t.rejects(v13, 'rejects, because it was deleted')
  t.equal(c.has('key3'), false, 'not inserted into cache')

  c.fetch('key4')
  clock.advance(100)
  const v15 = await c.fetch('key4', { allowStale: true })
  t.equal(
    v15,
    0,
    'there was no stale data, even though we were ok with that',
  )

  c.set('key5', 0)
  clock.advance(100)
  const v16 = await c.fetch('key5')
  t.equal(v16, 1, 'waited for new data, data in cache was stale')

  c.fetch('key4')
  await Promise.resolve().then(() => {})
  clock.advance(100)
  const v18 = c.get('key4')
  t.equal(
    v18,
    undefined,
    'get while fetching, but did not want stale data',
  )

  const p6 = c.fetch('key6')
  await Promise.resolve().then(() => {})
  clock.advance(100)
  const v20 = c.get('key6', { allowStale: true })
  t.equal(
    v20,
    undefined,
    'get while fetching, but no stale data to return',
  )
  t.equal(await p6, 0)
  clock.advance(100)
  const p7 = c.fetch('key6')
  const status: LRUCache.Status<number> = {}
  const v21 = c.get('key6', { allowStale: true, status })
  t.equal(v21, 0, 'allowStale, got stale data while fetching')
  t.equal(
    status.returnedStale,
    true,
    'status reflects stale data returned',
  )
  clock.advance(100)
  t.equal(await p7, 1, 'eventually updated')
})

t.test('fetchMethod must be a function', async t => {
  // @ts-expect-error
  t.throws(() => new LRU({ fetchMethod: true, max: 2 }))
})

t.test('fetch without fetch method', async t => {
  const c = new LRU({ max: 3 })
  c.set(0, 0)
  c.set(1, 1)
  const status: LRUCache.Status<number> = {}
  t.same(await Promise.all([c.fetch(0, { status }), c.fetch(1)]), [0, 1])
  t.matchSnapshot(status, 'status update')
})

t.test('fetch options, signal', async t => {
  const statuses: LRUCache.Status<number>[] = []
  const s = (): LRUCache.Status<number> => {
    const status: LRUCache.Status<number> = {}
    statuses.push(status)
    return status
  }

  let aborted = false
  const disposed: any[] = []
  const disposedAfter: any[] = []
  const c = new LRU<any, any>({
    max: 3,
    ttl: 100,
    fetchMethod: async (k, oldVal, { signal, options }) => {
      t.ok(options.status, 'received status object')
      // do something async
      await new Promise<void>(res => queueMicrotask(res))
      if (signal.aborted) {
        aborted = true
        return
      }
      if (k === 2) {
        options.ttl = 25
      }
      return (oldVal || 0) + 1
    },
    dispose: (v, k, reason) => {
      disposed.push([v, k, reason])
    },
    disposeAfter: (v, k, reason) => {
      disposedAfter.push([v, k, reason])
    },
  })

  const v1 = c.fetch(2, { status: s() })
  const testp1 = t.rejects(v1, 'aborted by clearing the cache')
  c.delete(2)
  await testp1
  await new Promise<void>(res => queueMicrotask(res))
  t.equal(aborted, true)
  t.same(disposed, [], 'no disposals for aborted promises')
  t.same(disposedAfter, [], 'no disposals for aborted promises')

  aborted = false
  const v2 = c.fetch(2, { status: s() })
  const testp2 = t.rejects(v2, 'rejected, replaced')
  c.set(2, 2)
  await testp2
  await new Promise<void>(res => queueMicrotask(res))
  t.equal(aborted, true)
  t.same(disposed, [], 'no disposals for aborted promises')
  t.same(disposedAfter, [], 'no disposals for aborted promises')
  c.delete(2)
  disposed.length = 0
  disposedAfter.length = 0

  aborted = false
  const v3 = c.fetch(2, { status: s() })
  const testp3 = t.rejects(v3, 'rejected, aborted by evict')
  c.set(3, 3, { status: s() })
  c.set(4, 4, { status: s() })
  c.set(5, 5, { status: s() })
  await testp3
  await new Promise<void>(res => queueMicrotask(res))
  t.equal(aborted, true)
  t.same(disposed, [], 'no disposals for aborted promises')
  t.same(disposedAfter, [], 'no disposals for aborted promises')

  aborted = false
  await c.fetch(6, { ttl: 1000, status: s() })
  t.equal(c.getRemainingTTL(6), 1000, 'overridden ttl in fetch() opts')
  await c.fetch(2, { ttl: 1, status: s() })
  t.equal(c.getRemainingTTL(2), 25, 'overridden ttl in fetchMethod')
  t.matchSnapshot(statuses, 'status updates')
})

t.test('fetchMethod throws', async t => {
  const statuses: LRUCache.Status<number>[] = []
  const s = (): LRUCache.Status<number> => {
    const status: LRUCache.Status<number> = {}
    statuses.push(status)
    return status
  }

  // make sure that even if there's no one to sit around and wait for it,
  // the background fetch throwing doesn't blow anything up.
  const cache = new LRU<string, number>({
    max: 10,
    ttl: 10,
    allowStale: true,
    fetchMethod: async () => {
      throw new Error('fetch failure')
    },
  })
  // seed the cache, and make the values stale.
  // this simulates the case where the fetch() DID work,
  // and replaced the promise with the resolution, but
  // then they got stale.
  cache.set('a', 1, { status: s() })
  cache.set('b', 2, { status: s() })
  clock.advance(20)
  await Promise.resolve().then(() => {})
  const a = await Promise.all([
    cache.fetch('a', { status: s() }),
    cache.fetch('a', { status: s() }),
    cache.fetch('a', { status: s() }),
  ])
  t.strictSame(a, [1, 1, 1])
  // clock advances, promise rejects
  clock.advance(20)
  await Promise.resolve().then(() => {})
  t.equal(cache.get('a', { status: s() }), undefined, 'removed from cache')
  const b = await Promise.all([
    cache.fetch('b', { status: s() }),
    cache.fetch('b', { status: s() }),
    cache.fetch('b', { status: s() }),
  ])
  t.strictSame(b, [2, 2, 2])
  clock.advance(20)
  await Promise.resolve().then(() => {})
  t.equal(cache.get('b', { status: s() }), undefined, 'removed from cache')
  const ap = cache.fetch('a', { status: s() })
  const testap = t.rejects(ap, 'aborted by replace')
  cache.set('a', 99, { status: s() })
  await testap
  t.equal(cache.get('a', { status: s() }), 99, 'did not delete new value')
  t.rejects(cache.fetch('b', { status: s() }), {
    message: 'fetch failure',
  })
  t.matchSnapshot(statuses, 'status updates')
})

t.test('fetchMethod throws, noDeleteOnFetchRejection option', async t => {
  // make sure that even if there's no one to sit around and wait for it,
  // the background fetch throwing doesn't blow anything up.
  let fetchFail = true
  const cache = new LRU<string, number>({
    max: 10,
    ttl: 10,
    allowStale: true,
    noDeleteOnFetchRejection: true,
    fetchMethod: async () => {
      if (fetchFail) {
        throw new Error('fetch failure')
      } else {
        return 1
      }
    },
  })

  // seed the cache, and make the values stale.
  // this simulates the case where the fetch() DID work,
  // and replaced the promise with the resolution, but
  // then they got stale.
  cache.set('a', 1)
  cache.set('b', 2)
  clock.advance(20)
  await Promise.resolve().then(() => {})
  const a = await Promise.all([
    cache.fetch('a'),
    cache.fetch('a'),
    cache.fetch('a'),
  ])
  t.strictSame(a, [1, 1, 1])
  // clock advances, promise rejects
  clock.advance(20)
  await Promise.resolve().then(() => {})
  const e = expose(cache)
  t.equal(e.keyMap.get('a'), 0)
  t.equal(e.valList[0], 1, 'promise replaced with stale value')
  const b = await Promise.all([
    cache.fetch('b'),
    cache.fetch('b'),
    cache.fetch('b'),
  ])
  t.strictSame(b, [2, 2, 2])
  clock.advance(20)
  await Promise.resolve().then(() => {})
  t.equal(e.keyMap.get('b'), 1)
  t.equal(e.valList[1], 2, 'promise replaced with stale value')
  cache.delete('a')
  cache.delete('b')

  // even though we don't noDeleteOnFetchRejection,
  // if there's no stale, we still remove the *promise*.
  const ap = cache.fetch('a')
  const testap = t.rejects(ap, 'aborted by replace')
  cache.set('a', 99)
  await testap
  t.equal(cache.get('a'), 99, 'did not delete, was replaced')
  await t.rejects(cache.fetch('b'), { message: 'fetch failure' })
  t.equal(e.keyMap.get('b'), undefined, 'not in cache')
  t.equal(e.valList[1], undefined, 'not in cache')
})

t.test('fetch context', async t => {
  const cache = new LRU<string, [string, any], string>({
    max: 10,
    ttl: 10,
    allowStale: true,
    noDeleteOnFetchRejection: true,
    fetchMethod: async (k, _, { context, options }) => {
      //@ts-expect-error
      t.equal(options.context, undefined)
      t.equal(context, expectContext)
      return [k, context]
    },
  })

  let expectContext = 'overridden'
  t.strictSame(await cache.fetch('y', { context: 'overridden' }), [
    'y',
    'overridden',
  ])
  expectContext = 'first context'
  t.strictSame(await cache.fetch('x', { context: 'first context' }), [
    'x',
    'first context',
  ])
  // if still in cache, doesn't call fetchMethod again
  t.strictSame(await cache.fetch('x', { context: 'ignored' }), [
    'x',
    'first context',
  ])
})

t.test('forceRefresh', async t => {
  const statuses: LRUCache.Status<number>[] = []
  const s = (): LRUCache.Status<number> => {
    const status: LRUCache.Status<number> = {}
    statuses.push(status)
    return status
  }

  const cache = new LRU<number, number>({
    max: 10,
    allowStale: true,
    ttl: 100,
    fetchMethod: async (k, _, { options }) => {
      t.equal(
        //@ts-expect-error
        options.forceRefresh,
        undefined,
        'do not expose forceRefresh',
      )
      return new Promise<number>(res => queueMicrotask(() => res(k)))
    },
  })

  // put in some values that don't match what fetchMethod returns
  cache.set(1, 100)
  cache.set(2, 200)
  t.equal(await cache.fetch(1), 100)
  // still there, because we're allowing stale, and it's not stale
  const status: LRUCache.Status<number> = {}
  t.equal(
    await cache.fetch(2, {
      forceRefresh: true,
      allowStale: false,
      status,
    }),
    2,
  )
  t.equal(status.fetch, 'refresh', 'status reflects forced refresh')
  t.equal(await cache.fetch(1, { forceRefresh: true }), 100)
  clock.advance(100)
  t.equal(await cache.fetch(2, { forceRefresh: true, status: s() }), 2)
  t.equal(cache.peek(1), 100)
  // if we don't allow stale though, then that means that we wait
  // for the background fetch to complete, so we get the updated value.
  t.equal(await cache.fetch(1, { allowStale: false, status: s() }), 1)

  cache.set(1, 100)
  t.equal(await cache.fetch(1, { allowStale: false }), 100)
  t.equal(
    await cache.fetch(1, {
      forceRefresh: true,
      allowStale: false,
      status: s(),
    }),
    1,
  )

  t.matchSnapshot(statuses, 'status updates')
})

t.test('allowStaleOnFetchRejection', async t => {
  let fetchFail = false
  const c = new LRU<number, number>({
    ttl: 10,
    max: 10,
    allowStaleOnFetchRejection: true,
    fetchMethod: async k => {
      if (fetchFail) throw new Error('fetch rejection')
      return k
    },
  })
  t.equal(await c.fetch(1), 1)
  clock.advance(11)
  fetchFail = true
  const status: LRUCache.Status<number> = {}
  t.equal(await c.fetch(1, { status }), 1)
  t.equal(
    status.returnedStale,
    true,
    'status reflects returned stale value',
  )
  t.equal(await c.fetch(1), 1)
  // if we override it, no go
  await t.rejects(c.fetch(1, { allowStaleOnFetchRejection: false }))
  // that also deletes from the cache
  t.equal(c.get(1), undefined)
})

t.test('placeholder promise is not removed when resolving', async t => {
  const resolves: Record<number, (v: number) => void> = {}
  const c = new LRU<number, number>({
    maxSize: 10,
    sizeCalculation(v) {
      return v
    },
    fetchMethod: k => {
      return new Promise(resolve => (resolves[k] = resolve))
    },
  })
  const p3 = c.fetch(3)
  const p4 = c.fetch(4)
  const p5 = c.fetch(5)

  resolves[4]?.(4)
  await p4

  t.match([...c], [[4, 4]])
  resolves[5]?.(5)
  await p5
  t.match(
    [...c],
    [
      [5, 5],
      [4, 4],
    ],
  )

  resolves[3]?.(3)
  await p3
  t.same(
    [...c],
    [
      [3, 3],
      [5, 5],
    ],
  )

  t.equal(c.size, 2)
  t.equal([...c].length, 2)
})

t.test('send a signal', async t => {
  const statuses: LRUCache.Status<number>[] = []
  const s = (): LRUCache.Status<number> => {
    const status: LRUCache.Status<number> = {}
    statuses.push(status)
    return status
  }

  let aborted: Error | undefined = undefined
  let resolved: boolean = false
  const c = new LRU<number, number>({
    max: 10,
    fetchMethod: async (k, _, { signal, options }) => {
      t.ok(options.status, 'has a status object')
      signal.addEventListener('abort', () => {
        aborted = signal.reason
      })
      return new Promise(res =>
        setTimeout(() => {
          resolved = true
          res(k)
        }, 100),
      )
    },
  })
  const ac = new AbortController()
  const p = c.fetch(1, { signal: ac.signal, status: s() })
  const er = new Error('custom abort signal')
  const testp = t.rejects(p, er)
  ac.abort(er)
  await testp
  t.equal(
    resolved,
    false,
    'should have aborted before fetchMethod resolved',
  )
  t.equal(aborted, er)
  t.equal(ac.signal.reason, er)
  t.equal(c.get(1, { status: s() }), undefined)
  t.matchSnapshot(statuses, 'status updates')
})

t.test('verify inflight works as expected', async t => {
  const statuses: LRUCache.Status<number>[] = []
  const s = (): LRUCache.Status<number> => {
    const status: LRUCache.Status<number> = {}
    statuses.push(status)
    return status
  }
  let called = 0
  const c = new LRUCache({
    max: 5,
    fetchMethod: async () => {
      called++
      await new Promise<void>(res => queueMicrotask(res))
      return {}
    },
  })
  const e = expose(c)
  c.fetch(1)
  const promises: Promise<any>[] = [
    c.fetch(1, { status: s() }),
    c.fetch(1),
    c.fetch(1, { status: s() }),
    c.fetch(1),
  ]
  t.match(e.valList, [Promise, null, null, null, null])
  t.equal(e.isBackgroundFetch(e.valList[0]), true, 'is background fetch')
  t.equal(c.get(1, { status: s() }), undefined, 'get while fetching')
  const a = await Promise.all(promises)
  for (let i = 1; i < a.length; i++) {
    t.equal(a[i], a[0], `index ${i} equal to first returned value`)
  }
  t.equal(called, 1, 'called one time')
  t.matchSnapshot(statuses, 'status updates')
})

t.test('abort, but then keep on fetching anyway', async t => {
  let aborted: Error | undefined = undefined
  let resolved: boolean = false
  let returnUndefined: boolean = false
  const cache = new LRU<number, number>({
    max: 10,
    ignoreFetchAbort: true,
    fetchMethod: async (k, _, { signal, options }) => {
      t.equal(options.ignoreFetchAbort, true, 'aborts ignored')
      signal.addEventListener('abort', () => {
        aborted = signal.reason
      })
      return new Promise(res =>
        setTimeout(() => {
          resolved = true
          if (returnUndefined) res()
          else res(k)
        }, 100),
      )
    },
  })
  const ac = new AbortController()
  const status: LRUCache.Status<number> = {}
  const p = cache.fetch(1, { signal: ac.signal, status })
  const er = new Error('ignored abort signal')
  ac.abort(er)
  clock.advance(100)
  t.equal(await p, 1)
  t.equal(status.fetchAbortIgnored, true, 'status reflects ignored abort')
  t.equal(status.fetchError, er)
  t.equal(status.fetchUpdated, true)

  t.equal(resolved, true, 'aborted, but resolved anyway')
  t.equal(aborted, er)
  t.equal(ac.signal.reason, er)
  t.equal(cache.get(1), 1)

  const p2 = cache.forceFetch(2)
  t.equal(cache.get(2), undefined)
  cache.delete(2)
  t.equal(cache.get(2), undefined)
  clock.advance(100)
  t.equal(await p2, 2)
  t.equal(cache.get(2), undefined)

  // if aborted for cause, we don't save the fetched value
  const p3 = cache.fetch(3)
  t.equal(cache.get(3), undefined)
  cache.set(3, 33)
  t.equal(cache.get(3), 33)
  clock.advance(100)
  t.equal(await p3, 3)
  t.equal(cache.get(3), 33)

  const e = expose(cache)
  returnUndefined = true
  const before = e.valList.slice()
  const p4 = cache.fetch(4)
  clock.advance(100)
  t.equal(await p4, undefined)
  const p5 = cache.forceFetch(4)
  clock.advance(100)
  await t.rejects(p5, { message: 'fetch() returned undefined' })
  t.same(e.valList, before, 'did not update values with undefined')
})

t.test('allowStaleOnFetchAbort', async t => {
  const c = new LRUCache<number, number, undefined>({
    ttl: 10,
    max: 10,
    allowStaleOnFetchAbort: true,
    fetchMethod: async (k, _, { signal }) => {
      return new Promise(res => {
        const t = setTimeout(() => res(k), 100)
        signal.addEventListener('abort', () => {
          clearTimeout(t)
          res()
        })
      })
    },
  })
  c.set(1, 10)
  clock.advance(100)
  const ac = new AbortController()
  const p = c.fetch(1, { signal: ac.signal })
  ac.abort(new Error('gimme the stale value'))
  t.equal(await p, 10)
  t.equal(c.get(1, { allowStale: true, noDeleteOnStaleGet: true }), 10)
  const p2 = c.fetch(1)
  c.set(1, 100)
  t.equal(await p2, 10)
  t.equal(c.get(1), 100)
})

t.test('background update on timeout, return stale', async t => {
  let returnUndefined = false
  const c = new LRUCache<number, number, void>({
    ttl: 10,
    max: 10,
    ignoreFetchAbort: true,
    allowStaleOnFetchAbort: true,
    fetchMethod: async k => {
      return new Promise(res => {
        setTimeout(() => {
          res(returnUndefined ? undefined : k)
        }, 100)
      })
    },
  })
  const e = expose(c)
  c.set(1, 10)
  clock.advance(100)
  const ac = new AbortController()
  const p = c.fetch(1, { signal: ac.signal })
  await new Promise<void>(res => queueMicrotask(res))
  t.match(e.valList[0], { __staleWhileFetching: 10 })
  ac.abort(new Error('gimme the stale value'))
  t.equal(await p, 10)
  t.equal(c.get(1, { allowStale: true }), 10)
  clock.advance(200)
  await new Promise<void>(res => queueMicrotask(res)).then(() => {})
  t.equal(e.valList[0], 1, 'got updated value later')

  c.set(1, 99)
  clock.advance(100)
  returnUndefined = true
  const ac2 = new AbortController()
  const p2 = c.fetch(1, { signal: ac2.signal })
  await new Promise<void>(res => queueMicrotask(res))
  t.match(e.valList[0], { __staleWhileFetching: 99 })
  ac2.abort(new Error('gimme stale 99'))
  t.equal(await p2, 99)
  t.match(e.valList[0], { __staleWhileFetching: 99 })
  t.equal(c.get(1, { allowStale: true }), 99)
  t.match(e.valList[0], { __staleWhileFetching: 99 })
  clock.advance(200)
  await new Promise<void>(res => queueMicrotask(res))
  t.equal(e.valList[0], 99)
})

t.test('fetch context required if set in ctor type', async t => {
  const c = new LRUCache<string, string, { a: number }>({
    max: 5,
    fetchMethod: async (k, _, { context }) => {
      if (k === 'y') t.equal(context, undefined)
      else if (k === 'z') t.same(context, { x: 1 })
      else t.same(context, { a: 1 })
      return k
    },
  })
  c.fetch('x', { context: { a: 1 } })
  //@ts-expect-error
  c.fetch('y')
  //@ts-expect-error
  c.fetch('z', { context: { x: 1 } })

  const c2 = new LRUCache<string, string, void>({
    max: 5,
    fetchMethod: async (k, _, { context }) => {
      if (k === 'y') t.equal(context, undefined)
      else if (k === 'z') t.same(context, { x: 1 })
      else t.same(context, { a: 1 })
      return k
    },
  })
  //@ts-expect-error
  c2.fetch('x', { context: { a: 1 } })
  c2.fetch('y')
  c2.fetch('y', { allowStale: true })
  //@ts-expect-error
  c2.fetch('z', { context: { x: 1 } })

  t.end()
})

t.test('has false for pending fetch without stale val', async t => {
  const c = new LRUCache<number, number>({
    max: 10,
    fetchMethod: async (key: number) =>
      new Promise<number>(r => setTimeout(() => r(key), 10)),
  })
  const e = expose(c)
  {
    const p = c.fetch(1)
    const index = e.keyMap.get(1) as number
    t.not(index, undefined)
    const bf = e.valList[index] as BackgroundFetch<number>
    t.type(bf, Promise, 'pending fetch')
    t.equal(bf.hasOwnProperty('__staleWhileFetching'), true)
    t.equal(c.has(1), false)
    clock.advance(10)
    const res = await p
    t.equal(res, 1)
    t.equal(c.has(1), true)
  }

  {
    // background fetch that DOES have a __staleWhileFetching value
    const p = c.fetch(1, { forceRefresh: true })
    const index = e.keyMap.get(1) as number
    t.not(index, undefined)
    const bf = e.valList[index] as BackgroundFetch<number>
    t.type(bf, Promise, 'pending fetch')
    t.equal(bf.__staleWhileFetching, 1)
    t.equal(c.has(1), true)
    clock.advance(10)
    const res = await p
    t.equal(res, 1)
    t.equal(c.has(1), true)
  }
})

t.test('properly dispose when using fetch', async t => {
  const disposes: [number, number, string][] = []
  const disposeAfters: [number, number, string][] = []
  let i = 0
  const c = new LRUCache<number, number>({
    max: 3,
    ttl: 10,
    dispose: (key, val, reason) => disposes.push([key, val, reason]),
    disposeAfter: (key, val, reason) =>
      disposeAfters.push([key, val, reason]),
    fetchMethod: async () => Promise.resolve(i++),
  })
  t.equal(await c.fetch(1), 0)
  clock.advance(20)
  t.equal(await c.fetch(1), 1)
  t.strictSame(disposes, [[0, 1, 'set']])
  t.strictSame(disposeAfters, [[0, 1, 'set']])
})

t.test('allowStaleOnFetchAbort and ignoreFetchAbort', async t => {
  const c = new LRUCache<number, number, void>({
    ttl: 10,
    max: 10,
    ignoreFetchAbort: true,
    allowStaleOnFetchAbort: true,
    fetchMethod: async k => {
      return new Promise(res => {
        setTimeout(() => {
          res(k)
        }, 100)
      })
    },
  })
  const ac = new AbortController()
  const p = c.fetch(1, { signal: ac.signal })
  await new Promise<void>(res => queueMicrotask(res))
  ac.abort(new Error('gimme the stale value'))
  t.equal(await p, undefined)
  t.equal(c.get(1, { allowStale: true }), undefined)
  clock.advance(200)
  await new Promise<void>(res => queueMicrotask(res)).then(() => {})
  t.equal(c.get(1), 1)
})
```

## File: `test/find.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'

const resolves: Record<
  number,
  (v: { value: number } | Promise<{ value: number }>) => void
> = {}
const c = new LRU<number, { value: number }>({
  max: 5,
  ttl: 1,
  fetchMethod: k =>
    new Promise<{ value: number }>(res => (resolves[k] = res)),
  allowStale: true,
  noDeleteOnStaleGet: true,
})

for (let i = 0; i < 9; i++) {
  c.set(i, { value: i })
}

const p = c.fetch(8, { forceRefresh: true })

t.equal(
  c.find(o => o.value === 4),
  c.get(4),
)

t.equal(
  c.find(o => o.value === 9),
  undefined,
)

t.same(
  c.find(o => o.value === 8),
  { value: 8 },
)

resolves[8]?.({ value: 10 })

new Promise(setImmediate)
  .then(() => p)
  .then(() => {
    t.same(
      c.find(o => o.value === 10),
      c.get(8),
    )
  })

const p99 = c.fetch(99)
t.equal(
  c.find(o => o.value === 99),
  undefined,
)
resolves[99]?.({ value: 99 })
t.equal(
  c.find(o => o.value === 99),
  undefined,
)
new Promise(setImmediate)
  .then(() => p99)
  .then(() => {
    t.same(
      c.find(o => o.value === 99),
      { value: 99 },
    )
    t.equal(
      c.find(o => o.value === 99),
      c.get(99),
    )
  })
```

## File: `test/import.mjs`
```
import t from 'tap'
t.test('import', async t => {
  const imp = await import('../dist/esm/index.js')
  t.equal(Object.getPrototypeOf(imp), null, 'import returns null obj')
  t.equal(typeof imp.LRUCache, 'function', 'LRUCache export is function')
  t.equal(
    imp.LRUCache.toString().split(/\r?\n/)[0].trim(),
    'class LRUCache {',
  )
})
```

## File: `test/info.ts`
```typescript
import t from 'tap'
import { LRUCache } from '../dist/esm/index.js'

t.test('just kv', t => {
  const c = new LRUCache<number, number>({ max: 2 })
  c.set(1, 10)
  c.set(2, 20)
  c.set(3, 30)
  t.equal(c.info(1), undefined)
  t.strictSame(c.info(2), { value: 20 })
  t.strictSame(c.info(3), { value: 30 })
  t.end()
})

t.test('other info', t => {
  const c = new LRUCache<number, number>({
    max: 2,
    ttl: 1000,
    maxSize: 10000,
  })
  c.set(1, 10, { size: 100 })
  c.set(2, 20, { size: 200 })
  c.set(3, 30, { size: 300 })
  t.equal(c.info(1), undefined)
  t.match(c.info(2), {
    value: 20,
    size: 200,
    ttl: Number,
    start: Number,
  })
  t.match(c.info(3), {
    value: 30,
    size: 300,
    ttl: Number,
    start: Number,
  })
  t.end()
})
```

## File: `test/load-check.ts`
```typescript
process.env.TAP_BAIL = '1'
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

const max = 10000
const cache = new LRU<string, number[]>({ max })

import crypto from 'crypto'
const getVal = () => [
  crypto.randomBytes(12).toString('hex'),
  crypto.randomBytes(12).toString('hex'),
  crypto.randomBytes(12).toString('hex'),
  crypto.randomBytes(12).toString('hex'),
]

const seeds = new Array(max * 3)
// fill up the cache to start
for (let i = 0; i < max * 3; i++) {
  const v = getVal()
  seeds[i] = [v.join(':'), v]
}
t.pass('generated seed data')

const verifyCache = () => {
  // walk down the internal list ensuring that every key is the key to that
  // index in the keyMap, and the value matches.
  const e = expose(cache)
  for (const [k, i] of e.keyMap.entries()) {
    const v = e.valList[i] as number[]
    const key = e.keyList[i]
    if (k !== key) {
      t.equal(k, key, 'key at proper index', { k, i })
    }
    if (v.join(':') !== k) {
      t.equal(k, v.join(':'), 'proper value at index', { v, i })
    }
  }
}

let cycles = 0
const cycleLength = Math.floor(max / 100)
while (cycles < max * 5) {
  const r = Math.floor(Math.random() * seeds.length)
  const seed = seeds[r]
  const v = cache.get(seed[0])
  if (v === undefined) {
    cache.set(seed[0], seed[1])
  } else {
    t.equal(v.join(':'), seed[0], 'correct get ' + cycles, {
      seed,
      v,
    })
  }
  if (++cycles % cycleLength === 0) {
    verifyCache()
    t.pass('cycle check ' + cycles)
  }
}
```

## File: `test/load.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'

const c = new LRU<number, number>({ max: 5 })
for (let i = 0; i < 9; i++) {
  c.set(i, i)
}

const d = new LRU(c)
d.load(c.dump())

t.strictSame(d, c)
```

## File: `test/lost-background-fetch.ts`
```typescript
// https://github.com/isaacs/node-lru-cache/issues/389
import t from 'tap'

const clock = t.clock
clock.enter()

const { LRUCache } = await import('../src/index.js')

const c = new LRUCache<number, number, void>({
  ttl: 1000,
  max: 10,
  ignoreFetchAbort: true,
  allowStaleOnFetchAbort: true,
  fetchMethod: async k => {
    return new Promise(res => {
      setTimeout(() => {
        res(k)
      }, 100 * k)
    })
  },
})

const ac = new AbortController()

const p2 = c.fetch(2, { signal: ac.signal })
const p1 = c.fetch(1, { signal: ac.signal })

clock.advance(50)
await new Promise<void>(res => queueMicrotask(res))

ac.abort(new Error('gimme the stale value'))

t.equal(await p1, undefined)
t.equal(await p2, undefined)

t.equal(c.get(1, { allowStale: true }), undefined, 'get expect undef 1')
t.equal(c.get(2, { allowStale: true }), undefined, 'get expect undef 2')

clock.advance(100)
await new Promise<void>(res => queueMicrotask(res)).then(() => {})

t.equal(c.get(1), 1, 'get expect 1')
t.equal(c.get(2), undefined, 'get 2 expect undef')

clock.advance(100)
await new Promise<void>(res => queueMicrotask(res)).then(() => {})

t.equal(c.get(1), 1, 'get expect 1')
t.equal(c.get(2), 2, 'get expect 2')
```

## File: `test/map-like.ts`
```typescript
import t from 'tap'
const clock = t.clock
t.teardown(clock.enter())

import { LRUCache as LRU } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

const entriesFromForeach = <K extends {}, V extends {}>(
  c: LRU<K, V>,
): [k: K, v: V][] => {
  const e: [k: K, v: V][] = []
  c.forEach((v, k) => e.push([k, v]))
  return e
}
const entriesFromRForeach = <K extends {}, V extends {}>(
  c: LRU<K, V>,
): [k: K, v: V][] => {
  const e: [k: K, v: V][] = []
  c.rforEach((v, k) => e.push([k, v]))
  return e
}

t.test('bunch of iteration things', async t => {
  const resolves: Record<number, (s: string) => void> = {}

  const c = new LRU<number, string>({
    max: 5,
    maxSize: 5,
    sizeCalculation: () => 1,
    fetchMethod: k => new Promise(resolve => (resolves[k] = resolve)),
  })

  t.matchSnapshot(c.keys(), 'empty, keys')
  t.matchSnapshot(c.values(), 'empty, values')
  t.matchSnapshot(c.entries(), 'empty, entries')
  t.matchSnapshot(entriesFromForeach(c), 'empty, foreach')
  t.matchSnapshot(c.rkeys(), 'empty, rkeys')
  t.matchSnapshot(c.rvalues(), 'empty, rvalues')
  t.matchSnapshot(c.rentries(), 'empty, rentries')
  t.matchSnapshot(entriesFromRForeach(c), 'empty, rforeach')
  t.matchSnapshot(c.dump(), 'empty, dump')

  const p99 = c.fetch(99)
  const testp99 = t.rejects(p99, 'aborted by eviction')
  const p123 = c.fetch(123)

  t.matchSnapshot(c.keys(), 'pending fetch, keys')
  t.matchSnapshot(c.values(), 'pending fetch, values')
  t.matchSnapshot(c.entries(), 'pending fetch, entries')
  t.matchSnapshot(entriesFromForeach(c), 'pending fetch, foreach')
  t.matchSnapshot(c.rkeys(), 'pending fetch, rkeys')
  t.matchSnapshot(c.rvalues(), 'pending fetch, rvalues')
  t.matchSnapshot(c.rentries(), 'pending fetch, rentries')
  t.matchSnapshot(entriesFromRForeach(c), 'pending fetch, rforeach')
  t.matchSnapshot(c.dump(), 'pending fetch, dump')

  for (let i = 0; i < 3; i++) {
    c.set(i, String(i))
  }

  resolves[123]?.('123')
  t.equal(await p123, '123')
  t.matchSnapshot(c.keys(), 'fetch 123 resolved, keys')
  t.matchSnapshot(c.values(), 'fetch 123 resolved, values')
  t.matchSnapshot(c.entries(), 'fetch 123 resolved, entries')
  t.matchSnapshot(entriesFromForeach(c), 'fetch 123 resolved, foreach')
  t.matchSnapshot(c.rkeys(), 'fetch 123 resolved, rkeys')
  t.matchSnapshot(c.rvalues(), 'fetch 123 resolved, rvalues')
  t.matchSnapshot(c.rentries(), 'fetch 123 resolved, rentries')
  t.matchSnapshot(entriesFromRForeach(c), 'fetch 123 resolved, rforeach')
  t.matchSnapshot(c.dump(), 'fetch 123 resolved, dump')

  for (let i = 3; i < 8; i++) {
    c.set(i, String(i))
  }

  t.matchSnapshot(c.keys(), 'keys')
  t.matchSnapshot(c.values(), 'values')
  t.matchSnapshot(c.entries(), 'entries')
  t.matchSnapshot(c.rkeys(), 'rkeys')
  t.matchSnapshot(c.rvalues(), 'rvalues')
  t.matchSnapshot(c.rentries(), 'rentries')
  t.matchSnapshot(c.dump(), 'dump')

  c.set(4, 'new value 4')
  t.matchSnapshot(c.keys(), 'keys, new value 4')
  t.matchSnapshot(c.values(), 'values, new value 4')
  t.matchSnapshot(c.entries(), 'entries, new value 4')
  t.matchSnapshot(c.rkeys(), 'rkeys, new value 4')
  t.matchSnapshot(c.rvalues(), 'rvalues, new value 4')
  t.matchSnapshot(c.rentries(), 'rentries, new value 4')
  t.matchSnapshot(c.dump(), 'dump, new value 4')

  resolves[99]?.('99')
  await testp99
  t.matchSnapshot(c.keys(), 'keys, resolved fetch 99 too late')
  t.matchSnapshot(c.values(), 'values, resolved fetch 99 too late')
  t.matchSnapshot(c.entries(), 'entries, resolved fetch 99 too late')
  t.matchSnapshot(c.rkeys(), 'rkeys, resolved fetch 99 too late')
  t.matchSnapshot(c.rvalues(), 'rvalues, resolved fetch 99 too late')
  t.matchSnapshot(c.rentries(), 'rentries, resolved fetch 99 too late')
  t.matchSnapshot(c.dump(), 'dump, resolved fetch 99 too late')

  // pretend an entry is stale for some reason
  c.set(7, 'stale', { ttl: 1, size: 1 })
  const e = expose(c)
  const idx = e.keyMap.get(7)
  if (!e.starts) throw new Error('no starts??')
  e.starts[idx as number] = clock.now() - 10000
  const seen: number[] = []
  for (const i of e.indexes()) {
    seen[i] = seen[i] || 0
    seen[i]++
    if ((seen[i] as number) > 2) {
      throw new Error('cycle on ' + i)
    }
  }
  seen.length = 0
  for (const i of e.rindexes()) {
    seen[i] = seen[i] || 0
    seen[i]++
    if ((seen[i] as number) > 2) {
      throw new Error('cycle on ' + i)
    }
  }
  t.matchSnapshot(c.keys(), 'keys, 7 stale')
  t.matchSnapshot(c.values(), 'values, 7 stale')
  t.matchSnapshot(c.entries(), 'entries, 7 stale')
  t.matchSnapshot(c.rkeys(), 'rkeys, 7 stale')
  t.matchSnapshot(c.rvalues(), 'rvalues, 7 stale')
  t.matchSnapshot(c.rentries(), 'rentries, 7 stale')
  t.matchSnapshot(c.dump(), 'dump, 7 stale')

  const feArr: any[] = []
  c.forEach((value, key) => feArr.push([value, key]))
  t.matchSnapshot(feArr, 'forEach, no thisp')
  const rfeArr: any[] = []
  c.rforEach((value, key) => rfeArr.push([value, key]))
  t.matchSnapshot(rfeArr, 'rforEach, no thisp')
  const feArrThisp: any[] = []
  const thisp = { a: 1 }
  c.forEach(function (this: typeof thisp, value, key) {
    feArrThisp.push([value, key, this])
  }, thisp)
  t.matchSnapshot(feArrThisp, 'forEach, with thisp')
  const rfeArrThisp: any[] = []
  const rthisp = { r: 1 }
  c.rforEach(function (this: typeof thisp, value, key) {
    rfeArrThisp.push([value, key, this])
  }, rthisp)
  t.matchSnapshot(rfeArrThisp, 'forEach, with thisp')

  // when cache is empty, these should do nothing
  const empty = new LRU({ max: 10 })
  empty.forEach(() => {
    throw new Error('fail empty forEach')
  })
  empty.rforEach(() => {
    throw new Error('fail empty rforEach')
  })
})
```

## File: `test/memo.ts`
```typescript
import t from 'tap'
import { LRUCache } from '../src/index.js'

t.throws(
  () =>
    new LRUCache<number, number>({
      max: 1,
      //@ts-expect-error
      memoMethod: true,
    }),
)
t.throws(() => new LRUCache({ max: 1 }).memo(3))

t.test('no funny business', t => {
  const memoCalls: number[] = []
  const c = new LRUCache<number, number>({
    max: 5,
    memoMethod: k => {
      memoCalls.push(k)
      return k ** k
    },
  })
  t.equal(c.get(2), undefined)
  const four = c.memo(2)
  const fur = c.memo(2)
  t.equal(four, 4)
  t.equal(fur, 4)
  t.equal(c.get(2), 4)
  t.strictSame(memoCalls, [2], 'only called once')
  t.end()
})

t.test('with context', t => {
  const memoCalls: [number, number | undefined, boolean][] = []
  // if there's a value already, and context is set, assign a shorter TTL
  const memoMethod = (
    k: number,
    v: number | undefined,
    {
      context,
      options,
    }: LRUCache.MemoizerOptions<number, number, boolean>,
  ) => {
    memoCalls.push([k, v, context])
    t.type(context, 'boolean')
    if (context) {
      return k
    } else {
      t.equal(options.noDeleteOnStaleGet, true)
      return k ** k
    }
  }

  const c = new LRUCache<number, number, boolean>({
    memoMethod,
    max: 5,
  })
  t.equal(c.memo(1, { context: true }), 1)
  t.equal(c.memo(1, { context: true }), 1)
  t.equal(c.memo(1, { context: false }), 1)
  t.equal(c.memo(2, { context: false, noDeleteOnStaleGet: true }), 4)
  t.equal(c.memo(2, { context: true }), 4)
  t.equal(c.memo(2, { context: false }), 4)
  t.strictSame(memoCalls, [
    [1, undefined, true],
    [2, undefined, false],
  ])
  t.end()
})
```

## File: `test/move-to-tail.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

const c = new LRU({ max: 5 })
const exp = expose(c)

t.test('list integrity', { bail: true }, t => {
  const e = (index: number) => ({
    index,
    prev: exp.prev[index],
    _:
      index === exp.tail ? 'T'
      : index === exp.head ? 'H'
      : '' + index,
    next: exp.next[index],
    head: exp.head,
    tail: exp.tail,
  })
  const snap = () => {
    const a: ReturnType<typeof e>[] = []
    for (let i = 0; i < 5; i++) {
      a.push(e(i))
    }
    return a
  }
  const integrity = (msg: string) => {
    t.test(msg, { bail: false }, t => {
      for (let i = 0; i < c.max; i++) {
        if (i !== exp.head) {
          t.equal(exp.next[exp.prev[i] as number], i, 'n[p[i]] === i')
        }
        if (i !== exp.tail) {
          t.equal(exp.prev[exp.next[i] as number], i, 'p[n[i]] === i')
        }
      }
      t.end()
    })
  }

  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }

  t.matchSnapshot(snap(), 'list after initial fill')
  integrity('after initial fill')
  exp.moveToTail(2)
  t.matchSnapshot(snap(), 'list after moveToTail 2')
  integrity('after moveToTail 2')
  exp.moveToTail(4)
  t.matchSnapshot(snap(), 'list after moveToTail 4')
  integrity('after moveToTail 4')

  t.end()
})
```

## File: `test/onInsert.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'

t.test('onInsert', t => {
  const inserted: any[] = []
  const c = new LRU({
    max: 5,
    onInsert: (v, k, r) => inserted.push([v, k, r]),
  })

  for (let i = 0; i < 5; i++) {
    c.set(i, i)
  }
  t.strictSame(inserted, [
    [0, 0, 'add'],
    [1, 1, 'add'],
    [2, 2, 'add'],
    [3, 3, 'add'],
    [4, 4, 'add'],
  ])

  t.end()
})

t.test('onInsert with replace', t => {
  const inserted: any[] = []
  const c = new LRU({
    max: 5,
    onInsert: (v, k, r) => inserted.push([v, k, r]),
  })

  c.set(1, 1)
  c.set(2, 2)
  c.set(1, 'one')

  t.strictSame(inserted, [
    [1, 1, 'add'],
    [2, 2, 'add'],
    ['one', 1, 'replace'],
  ])

  t.end()
})

t.test('onInsert with value === undefined', t => {
  const inserted: any[] = []
  const c = new LRU({
    max: 5,
    onInsert: (v, k, r) => inserted.push([v, k, r]),
  })

  c.set(1, 1)
  c.set(1, undefined)
  c.set(2, undefined)
  t.strictSame(inserted, [[1, 1, 'add']])

  t.end()
})

t.test('onInsert with update (same value)', t => {
  const inserted: any[] = []
  const c = new LRU({
    max: 5,
    onInsert: (v, k, r) => inserted.push([v, k, r]),
  })

  c.set(1, 1)
  c.set(1, 1) // update with the same value

  t.strictSame(inserted, [
    [1, 1, 'add'],
    [1, 1, 'update'],
  ])

  t.end()
})
```

## File: `test/pop.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'

const cache = new LRU<number, number>({ max: 5 })
for (let i = 0; i < 5; i++) {
  cache.set(i, i)
}
cache.get(2)
const popped: (number | undefined)[] = []
let p: number | undefined
do {
  p = cache.pop()
  popped.push(p)
} while (p !== undefined)
t.same(popped, [0, 1, 3, 4, 2, undefined])

t.test('pop with background fetches', async t => {
  const resolves: Record<number, (n: number) => void> = {}
  let aborted = false
  const f = new LRU<number, number>({
    max: 5,
    ttl: 10,
    fetchMethod: (k: number, _v, { signal }) => {
      signal.addEventListener('abort', () => (aborted = true))
      return new Promise<number>(res => (resolves[k] = res))
    },
  })

  // a fetch that's in progress with no stale val gets popped
  // without returning anything
  f.set(0, 0)
  let pf = f.fetch(1)
  f.set(2, 2)
  t.equal(f.size, 3)
  t.equal(f.pop(), 0)
  t.equal(f.size, 2)
  t.equal(f.pop(), 2)
  t.equal(f.size, 0)
  t.equal(aborted, true)
  resolves[1]?.(1)
  await t.rejects(pf)

  f.set(0, 0, { ttl: 0 })
  f.set(1, 111)
  await new Promise(r => setTimeout(r, 20))
  pf = f.fetch(1)
  f.set(2, 2, { ttl: 0 })
  t.equal(f.size, 3)
  t.equal(f.pop(), 0)
  t.equal(f.size, 2)
  t.equal(f.pop(), 111)
  t.equal(f.size, 1)
  t.equal(f.pop(), 2)
  t.equal(f.size, 0)
  resolves[1]?.(1)
  await t.rejects(pf)
})

t.test('pop calls dispose and disposeAfter', t => {
  let disposeCalled = 0
  let disposeAfterCalled = 0
  const c = new LRU({
    max: 5,
    dispose: () => disposeCalled++,
    disposeAfter: () => disposeAfterCalled++,
  })
  c.set(0, 0)
  c.set(1, 1)
  c.set(2, 2)
  t.equal(c.pop(), 0)
  t.equal(c.pop(), 1)
  t.equal(c.pop(), 2)
  t.equal(c.pop(), undefined)
  t.equal(c.size, 0)
  t.equal(disposeCalled, 3)
  t.equal(disposeAfterCalled, 3)
  t.end()
})
```

## File: `test/purge-stale-exhaustive.ts`
```typescript
if (typeof performance === 'undefined') {
  Object.assign(global, {
    performance: (await import('perf_hooks')).performance,
  })
}

import assert from 'node:assert'
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

const clock = t.clock
clock.advance(1)

const boolOpts = (n: number): number[][] => {
  const mask = Math.pow(2, n)
  const arr: number[][] = []
  for (let i = 0; i < mask; i++) {
    arr.push(
      (mask + i)
        .toString(2)
        .slice(1)
        .split('')
        .map(n => +n),
    )
  }
  return arr
}

const permute = (arr: number[] | number): number[][] => {
  if (typeof arr === 'number') {
    return permute(Object.keys(new Array(arr).fill('')).map(n => +n))
  }
  if (arr.length === 1) {
    return [arr]
  }
  const permutations = []
  // recurse over selecting any of the items
  for (let i = 0; i < arr.length; i++) {
    const items = arr.slice(0)
    const item = items.splice(i, 1)
    permutations.push(...permute(items).map(perm => item.concat(perm)))
  }
  return permutations
}

const runTestStep = ({
  order,
  stales = -1,
  len,
}: {
  order: number[]
  stales?: number[] | -1
  len: number
}) => {
  // generate stales at this level because it's faster that way,
  // fewer tap pieces to prop it all up.
  if (stales === -1) {
    for (const stales of boolOpts(len)) {
      runTestStep({ order, stales, len })
    }
    return true
  }

  clock.enter()
  const c = new LRU({ max: len, ttl: 100 })
  const e = expose(c)
  // fill the array with index matching k/v
  for (let i = 0; i < len; i++) {
    if (stales[i]) {
      c.set(i, i, { ttl: 1 })
    } else {
      c.set(i, i)
    }
  }

  // now get() items to reorder
  for (const index of order) {
    c.get(index)
  }

  assert.deepEqual([...e.rindexes()], order, 'got expected ordering')

  // advance clock so masked go stale
  clock.advance(10)
  c.purgeStale()
  assert.deepEqual(
    [...e.rindexes()],
    [...e.rindexes({ allowStale: true })],
  )
  // make all go stale
  clock.advance(100)
  c.purgeStale()
  assert.deepEqual([...e.rindexes({ allowStale: true })], [])
  clock.exit()
  return true
}

t.test('exhaustive tests', t => {
  // this is a brutal test.
  // Generate every possible ordering of indexes.
  // then for each ordering, generate every possible arrangement of staleness
  // Verify that purgeStale produces the correct result every time.
  const len = 5
  for (const order of permute(len)) {
    const name = `order=${order.join('')}`
    t.test(name, t => {
      t.plan(1)
      runTestStep({ order, len })
      t.pass('no problems')
    })
  }
  t.end()
})
```

## File: `test/purge-stale-resource-management.ts`
```typescript
if (typeof performance === 'undefined') {
  Object.assign(global, {
    performance: (await import('perf_hooks')).performance,
  })
}

import t from 'tap'

// verify that a large number of ttlAutopurge timeouts won't
// result in a resource exhaustion problem due to timers being
// created.

const clock = t.clock
clock.advance(1)

let timeouts = 0
const origST = global.setTimeout
const newST = function (
  this: any,
  ...args: Parameters<typeof setTimeout>
) {
  ++timeouts
  return origST.apply(this, args)
}
let clears = 0
const origCT = global.clearTimeout
const newCT = function (
  this: any,
  ...args: Parameters<typeof clearTimeout>
) {
  ++clears
  return origCT.apply(this, args)
}

//@ts-ignore
global.setTimeout = newST
//@ts-ignore
global.clearTimeout = newCT

const { LRUCache: LRU } = await import('../dist/esm/index.js')

t.test('a cache that overwrites a hot key many times', async t => {
  const cache = new LRU<string, number>({
    ttl: 10,
    ttlAutopurge: true,
  })

  const N = 10 //_000
  for (let i = 0; i < N; i++) {
    cache.set('hot-key', i)
  }
  t.equal(timeouts, N)
  t.equal(clears, N - 1)

  timeouts = 0
  clears = 0
  cache.set('hot-key', 99, { ttl: 0 })
  const clearsAfterSetTTL0 = clears
  const timeoutsAfterSetTTL0 = timeouts

  t.equal(timeoutsAfterSetTTL0, 0)
  t.equal(clearsAfterSetTTL0, 1)

  timeouts = 0
  clears = 0
  cache.set('hot-key', 100)
  const clearsAfterSetTTLDef = clears
  const timeoutsAfterSetTTLDef = timeouts
  t.equal(clearsAfterSetTTLDef, 0)
  t.equal(timeoutsAfterSetTTLDef, 1)

  timeouts = 0
  clears = 0
  cache.delete('hot-key')
  const clearsAfterDelete = clears
  const timeoutsAfterDelete = timeouts
  t.equal(clearsAfterDelete, 1)
  t.equal(timeoutsAfterDelete, 0)
})

t.test('evicting an item means no need for autopurge', async t => {
  const cache = new LRU<string, number>({
    ttl: 10,
    max: 5,
    ttlAutopurge: true,
  })

  timeouts = 0
  clears = 0
  cache.set('a', 1)
  const clearsAfterSet = clears
  const timeoutsAfterSet = timeouts
  t.equal(clearsAfterSet, 0)
  t.equal(timeoutsAfterSet, 1)

  timeouts = 0
  clears = 0
  cache.set('b', 1, { ttl: 0 })
  cache.set('c', 1, { ttl: 0 })
  cache.set('d', 1, { ttl: 0 })
  cache.set('e', 1, { ttl: 0 })
  cache.set('f', 1, { ttl: 0 })

  const clearsAfterEvict = clears
  const timeoutsAfterEvict = timeouts
  t.equal(clearsAfterEvict, 1)
  t.equal(timeoutsAfterEvict, 0)
})

t.test('clearing list clears autopurge timers', async t => {
  const cache = new LRU<string, number>({
    ttl: 10,
    max: 5,
    ttlAutopurge: true,
  })

  timeouts = 0
  clears = 0
  cache.set('a', 1)
  cache.set('b', 1)
  cache.set('c', 1)
  cache.set('d', 1)
  const clearsAfterSet = clears
  const timeoutsAfterSet = timeouts
  t.equal(clearsAfterSet, 0)
  t.equal(timeoutsAfterSet, 4)

  timeouts = 0
  clears = 0
  cache.clear()

  const clearsAfterClear = clears
  const timeoutsAfterClear = timeouts
  t.equal(clearsAfterClear, 4)
  t.equal(timeoutsAfterClear, 0)
})
```

## File: `test/reverse-iterate-delete-all.ts`
```typescript
// https://github.com/isaacs/node-lru-cache/issues/278
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'
const lru = new LRU<string, string>({
  maxSize: 2,
  sizeCalculation: () => 1,
})
lru.set('x', 'x')
lru.set('y', 'y')
for (const key of lru.rkeys()) {
  lru.delete(key)
}
t.equal(lru.size, 0)
```

## File: `test/size-calculation.ts`
```typescript
import t from 'tap'
import { LRUCache as LRU } from '../dist/esm/index.js'

import { expose } from './fixtures/expose.js'

const checkSize = (c: LRU<any, any>) => {
  const e = expose(c)
  const sizes = e.sizes
  if (!sizes) throw new Error('no sizes??')
  const { calculatedSize, maxSize } = c
  const sum = [...sizes].reduce((a, b) => a + b, 0)
  if (sum !== calculatedSize) {
    console.error({ sum, calculatedSize, sizes }, c, e)
    throw new Error('calculatedSize does not equal sum of sizes')
  }
  if (calculatedSize > maxSize) {
    throw new Error('max size exceeded')
  }
}

t.test('store strings, size = length', t => {
  const c = new LRU<any, string>({
    max: 100,
    maxSize: 100,
    sizeCalculation: n => n.length,
  })

  checkSize(c)
  c.set(5, 'x'.repeat(5))
  checkSize(c)
  c.set(10, 'x'.repeat(10))
  checkSize(c)
  c.set(20, 'x'.repeat(20))
  checkSize(c)
  t.equal(c.calculatedSize, 35)
  c.delete(20)
  checkSize(c)
  t.equal(c.calculatedSize, 15)
  c.delete(5)
  checkSize(c)
  t.equal(c.calculatedSize, 10)
  c.clear()
  checkSize(c)
  t.equal(c.calculatedSize, 0)

  const s = 'x'.repeat(10)
  for (let i = 0; i < 5; i++) {
    c.set(i, s)
    checkSize(c)
  }
  t.equal(c.calculatedSize, 50)

  // the big item goes in, but triggers a prune
  // we don't preemptively prune until we *cross* the max
  c.set('big', 'x'.repeat(100))
  checkSize(c)
  t.equal(c.calculatedSize, 100)
  // override the size on set
  c.set('big', 'y'.repeat(100), { sizeCalculation: () => 10 })
  checkSize(c)
  t.equal(c.size, 1)
  checkSize(c)
  t.equal(c.calculatedSize, 10)
  checkSize(c)
  c.delete('big')
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)

  c.set('repeated', 'i'.repeat(10))
  checkSize(c)
  c.set('repeated', 'j'.repeat(10))
  checkSize(c)
  c.set('repeated', 'i'.repeat(10))
  checkSize(c)
  c.set('repeated', 'j'.repeat(10))
  checkSize(c)
  c.set('repeated', 'i'.repeat(10))
  checkSize(c)
  c.set('repeated', 'j'.repeat(10))
  checkSize(c)
  c.set('repeated', 'i'.repeat(10))
  checkSize(c)
  c.set('repeated', 'j'.repeat(10))
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 10)
  t.equal(c.get('repeated'), 'j'.repeat(10))
  t.matchSnapshot(c.dump(), 'dump')

  t.end()
})

t.test('bad size calculation fn throws on set()', t => {
  const c = new LRU({
    max: 5,
    maxSize: 5,
    // @ts-expect-error
    sizeCalculation: () => {
      return 'asdf'
    },
  })
  t.throws(
    () => c.set(1, '1'.repeat(100)),
    new TypeError(
      'sizeCalculation return invalid (expect positive integer)',
    ),
  )
  t.throws(() => {
    // @ts-expect-error
    c.set(1, '1', { size: 'asdf', sizeCalculation: null })
  }, new TypeError('invalid size value (must be positive integer)'))
  t.throws(() => {
    // @ts-expect-error
    c.set(1, '1', { sizeCalculation: 'asdf' })
  }, new TypeError('sizeCalculation must be a function'))
  t.end()
})

t.test('delete while empty, or missing key, is no-op', t => {
  const c = new LRU({ max: 5, maxSize: 10, sizeCalculation: () => 2 })
  checkSize(c)
  c.set(1, 1)
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 2)
  c.clear()
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  c.delete(1)
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)

  c.set(1, 1)
  checkSize(c)
  c.set(1, 1)
  checkSize(c)
  c.set(1, 1)
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 2)
  c.delete(99)
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 2)
  c.delete(1)
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  c.delete(1)
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.end()
})

t.test('large item falls out of cache, sizes are kept correct', t => {
  const statuses: LRU.Status<number>[] = []
  const s = (): LRU.Status<number> => {
    const status: LRU.Status<number> = {}
    statuses.push(status)
    return status
  }

  const c = new LRU<number, number>({
    maxSize: 10,
    sizeCalculation: () => 100,
  })
  const sizes = expose(c).sizes

  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.same(sizes, [])

  c.set(2, 2, { size: 2, status: s() })
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 2)
  t.same(sizes, [2])

  c.delete(2)
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.same(sizes, [0])

  c.set(1, 1, { status: s() })
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.same(sizes, [0])

  c.set(3, 3, { size: 3, status: s() })
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 3)
  t.same(sizes, [3])

  c.set(4, 4, { status: s() })
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 3)
  t.same(sizes, [3])

  t.matchSnapshot(statuses, 'status updates')
  t.end()
})

t.test('large item falls out of cache because maxEntrySize', t => {
  const statuses: LRU.Status<number>[] = []
  const s = (): LRU.Status<number> => {
    const status: LRU.Status<number> = {}
    statuses.push(status)
    return status
  }

  const c = new LRU<number, number>({
    maxSize: 1000,
    maxEntrySize: 10,
    sizeCalculation: () => 100,
  })
  const sizes = expose(c).sizes

  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.same(sizes, [])

  c.set(2, 2, { size: 2, status: s() })
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 2)
  t.same(sizes, [2])

  c.delete(2)
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.same(sizes, [0])

  c.set(1, 1, { status: s() })
  checkSize(c)
  t.equal(c.size, 0)
  t.equal(c.calculatedSize, 0)
  t.same(sizes, [0])

  c.set(3, 3, { size: 3, status: s() })
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 3)
  t.same(sizes, [3])

  c.set(4, 4, { status: s() })
  checkSize(c)
  t.equal(c.size, 1)
  t.equal(c.calculatedSize, 3)
  t.same(sizes, [3])

  t.matchSnapshot(statuses, 'status updates')
  t.end()
})

t.test('maxEntrySize, no maxSize', async t => {
  const c = new LRU<number, string>({
    max: 10,
    maxEntrySize: 10,
    sizeCalculation: s => s.length,
    fetchMethod: async n => 'x'.repeat(n),
  })
  t.equal(await c.fetch(2), 'xx')
  t.equal(c.size, 1)
  t.equal(await c.fetch(3), 'xxx')
  t.equal(c.size, 2)
  t.equal(await c.fetch(11), 'x'.repeat(11))
  t.equal(c.size, 2)
  t.equal(c.has(11), false)
})
```

## File: `test/ttl.ts`
```typescript
import t, { Test } from 'tap'
import { LRUCache } from '../dist/esm/index.js'
import { expose } from './fixtures/expose.js'

const clock = t.clock

const runTests = (LRU: typeof LRUCache, t: Test) => {
  const statuses: LRUCache.Status<any>[] = []
  const s = (): LRUCache.Status<any> => {
    const status: LRUCache.Status<any> = {}
    statuses.push(status)
    return status
  }

  const { setTimeout, clearTimeout } = global
  t.teardown(() =>
    // @ts-ignore
    Object.assign(global, { setTimeout, clearTimeout }),
  )
  //@ts-ignore
  global.setTimeout = clock.setTimeout.bind(clock)
  //@ts-ignore
  global.clearTimeout = clock.clearTimeout.bind(clock)

  t.test('ttl tests defaults', t => {
    statuses.length = 0
    // have to advance it 1 so we don't start with 0
    // NB: this module will misbehave if you create an entry at a
    // clock time of 0, for example if you are filling an LRU cache
    // in a node lacking perf_hooks, at midnight UTC on 1970-01-01.
    // This is a known bug that I am ok with.
    clock.advance(1)
    const c = new LRU({ max: 5, ttl: 10, ttlResolution: 0 })
    const e = expose(c, LRU)
    c.set(1, 1, { status: s() })
    t.equal(c.get(1, { status: s() }), 1, '1 get not stale', {
      now: clock.now(),
    })
    clock.advance(5)
    t.equal(c.get(1, { status: s() }), 1, '1 get not stale', {
      now: clock.now(),
    })
    t.equal(c.getRemainingTTL(1), 5, '5ms left to live')
    t.equal(c.getRemainingTTL('not in cache'), 0, 'thing doesnt exist')
    clock.advance(5)
    t.equal(c.get(1, { status: s() }), 1, '1 get not stale', {
      now: clock.now(),
    })
    t.equal(c.getRemainingTTL(1), 0, 'almost stale')
    clock.advance(1)
    t.equal(c.getRemainingTTL(1), -1, 'gone stale')
    clock.advance(1)
    t.equal(c.getRemainingTTL(1), -2, 'even more stale')
    t.equal(c.size, 1, 'still there though')
    t.equal(c.has(1, { status: s() }), false, '1 has stale', {
      now: clock.now(),
      index: e.keyMap.get(1),
      stale: e.isStale(e.keyMap.get(1)),
    })
    t.equal(c.get(1, { status: s() }), undefined)
    t.equal(c.size, 0)

    c.set(2, 2, { ttl: 100 })
    clock.advance(50)
    t.equal(c.has(2, { status: s() }), true)
    t.equal(c.get(2, { status: s() }), 2)
    clock.advance(51)
    t.equal(c.has(2), false)
    t.equal(c.get(2, { status: s() }), undefined)

    c.clear()
    for (let i = 0; i < 9; i++) {
      c.set(i, i, { status: s() })
    }
    // now we have 9 items
    // get an expired item from old set
    clock.advance(11)
    t.equal(c.peek(4), undefined)
    t.equal(c.has(4, { status: s() }), false)
    t.equal(c.get(4, { status: s() }), undefined)

    // set an item WITHOUT a ttl on it
    c.set('immortal', true, { ttl: 0 })
    clock.advance(100)
    t.equal(c.getRemainingTTL('immortal'), Infinity)
    t.equal(c.get('immortal', { status: s() }), true)
    c.get('immortal', { updateAgeOnGet: true })
    clock.advance(100)
    t.equal(c.get('immortal', { status: s() }), true)
    t.matchSnapshot(statuses, 'status updates')
    t.end()
  })

  t.test('ttl tests with ttlResolution=100', t => {
    statuses.length = 0
    const c = new LRU({ ttl: 10, ttlResolution: 100, max: 10 })
    const e = expose(c, LRU)
    c.set(1, 1, { status: s() })
    t.equal(c.get(1, { status: s() }), 1, '1 get not stale', {
      now: clock.now(),
    })
    clock.advance(5)
    t.equal(c.get(1, { status: s() }), 1, '1 get not stale', {
      now: clock.now(),
    })
    clock.advance(5)
    t.equal(c.get(1, { status: s() }), 1, '1 get not stale', {
      now: clock.now(),
    })
    clock.advance(1)
    t.equal(c.has(1, { status: s() }), true, '1 has stale', {
      now: clock.now(),
      ttls: e.ttls,
      starts: e.starts,
      index: e.keyMap.get(1),
      stale: e.isStale(e.keyMap.get(1)),
    })
    t.equal(c.get(1, { status: s() }), 1)
    clock.advance(100)
    t.equal(c.has(1, { status: s() }), false, '1 has stale', {
      now: clock.now(),
      ttls: e.ttls,
      starts: e.starts,
      index: e.keyMap.get(1),
      stale: e.isStale(e.keyMap.get(1)),
    })
    t.equal(c.get(1, { status: s() }), undefined)
    t.equal(c.size, 0)
    t.matchSnapshot(statuses, 'status updates')
    t.end()
  })

  t.test('ttlResolution only respected if non-negative integer', t => {
    const invalids = [-1, null, undefined, 'banana', {}]
    for (const i of invalids) {
      //@ts-expect-error
      const c = new LRU({ ttl: 5, ttlResolution: i, max: 5 })
      t.not(c.ttlResolution, i)
      t.equal(c.ttlResolution, Math.floor(c.ttlResolution))
      t.ok(c.ttlResolution >= 0)
    }
    t.end()
  })

  t.test('ttlAutopurge', t => {
    statuses.length = 0
    const c = new LRU({
      ttl: 10,
      ttlAutopurge: true,
      ttlResolution: 0,
    })
    c.set(1, 1, { status: s() })
    c.set(2, 2, { status: s() })
    t.equal(c.size, 2)
    c.set(2, 3, { ttl: 11, status: s() })
    clock.advance(11)
    t.equal(c.size, 1)
    clock.advance(1)
    t.equal(c.size, 0)
    t.matchSnapshot(statuses, 'status updates')
    t.end()
  })

  t.test('ttl on set, not on cache', t => {
    statuses.length = 0
    const c = new LRU({ max: 5, ttlResolution: 0 })
    c.set(1, 1, { ttl: 10, status: s() })
    t.equal(c.get(1, { status: s() }), 1)
    clock.advance(5)
    t.equal(c.get(1, { status: s() }), 1)
    clock.advance(5)
    t.equal(c.get(1, { status: s() }), 1)
    clock.advance(1)
    t.equal(c.has(1, { status: s() }), false)
    t.equal(c.get(1, { status: s() }), undefined)
    t.equal(c.size, 0)

    c.set(2, 2, { ttl: 100, status: s() })
    clock.advance(50)
    t.equal(c.has(2, { status: s() }), true)
    t.equal(c.get(2, { status: s() }), 2)
    clock.advance(51)
    t.equal(c.has(2, { status: s() }), false)
    t.equal(c.get(2, { status: s() }), undefined)

    c.clear()
    for (let i = 0; i < 9; i++) {
      c.set(i, i, { ttl: 10, status: s() })
    }
    // now we have 9 items
    // get an expired item from old set
    clock.advance(11)
    t.equal(c.has(4, { status: s() }), false)
    t.equal(c.get(4, { status: s() }), undefined)

    t.matchSnapshot(statuses, 'status updates')
    t.end()
  })

  t.test('ttl with allowStale', t => {
    const c = new LRU({
      max: 5,
      ttl: 10,
      allowStale: true,
      ttlResolution: 0,
    })
    c.set(1, 1)
    t.equal(c.get(1), 1)
    clock.advance(5)
    t.equal(c.get(1), 1)
    clock.advance(5)
    t.equal(c.get(1), 1)
    clock.advance(1)
    t.equal(c.has(1), false)

    t.equal(c.get(1, { status: s(), noDeleteOnStaleGet: true }), 1)
    t.equal(c.get(1), 1)
    t.equal(c.get(1), undefined)
    t.equal(c.size, 0)

    c.set(2, 2, { ttl: 100 })
    clock.advance(50)
    t.equal(c.has(2), true)
    t.equal(c.get(2), 2)
    clock.advance(51)
    t.equal(c.has(2), false)
    t.equal(c.get(2), 2)
    t.equal(c.get(2), undefined)

    c.clear()
    for (let i = 0; i < 9; i++) {
      c.set(i, i)
    }
    // now we have 9 items
    // get an expired item from old set
    clock.advance(11)
    t.equal(c.has(4), false)
    t.equal(c.get(4), 4)
    t.equal(c.get(4), undefined)

    t.end()
  })

  t.test('ttl with updateAgeOnGet/updateAgeOnHas', t => {
    const c = new LRU({
      max: 5,
      ttl: 10,
      updateAgeOnGet: true,
      updateAgeOnHas: true,
      ttlResolution: 0,
    })
    c.set(1, 1)
    t.equal(c.get(1), 1)
    clock.advance(5)
    t.equal(c.has(1), true)
    clock.advance(5)
    t.equal(c.get(1), 1)
    clock.advance(1)
    t.equal(c.getRemainingTTL(1), 9)
    t.equal(c.has(1), true)
    t.equal(c.getRemainingTTL(1), 10)
    t.equal(c.get(1), 1)
    t.equal(c.size, 1)
    c.clear()

    c.set(2, 2, { ttl: 100 })
    for (let i = 0; i < 10; i++) {
      clock.advance(50)
      t.equal(c.has(2), true)
      t.equal(c.get(2), 2)
    }
    clock.advance(101)
    t.equal(c.has(2), false)
    t.equal(c.get(2), undefined)

    c.clear()
    for (let i = 0; i < 9; i++) {
      c.set(i, i)
    }
    // now we have 9 items
    // get an expired item
    t.equal(c.has(3), false)
    t.equal(c.get(3), undefined)
    clock.advance(11)
    t.equal(c.has(4), false)
    t.equal(c.get(4), undefined)

    t.end()
  })

  t.test('purge stale items', t => {
    const c = new LRU({ max: 10, ttlResolution: 0 })
    for (let i = 0; i < 10; i++) {
      c.set(i, i, { ttl: i + 1 })
    }
    clock.advance(3)
    t.equal(c.size, 10)
    t.equal(c.purgeStale(), true)
    t.equal(c.size, 8)
    t.equal(c.purgeStale(), false)

    clock.advance(100)
    t.equal(c.size, 8)
    t.equal(c.purgeStale(), true)
    t.equal(c.size, 0)
    t.equal(c.purgeStale(), false)
    t.equal(c.size, 0)
    t.end()
  })

  t.test('no update ttl', t => {
    const statuses: LRUCache.Status<number>[] = []
    const s = (): LRUCache.Status<number> => {
      const status: LRUCache.Status<number> = {}
      statuses.push(status)
      return status
    }
    const c = new LRU({
      max: 10,
      ttlResolution: 0,
      noUpdateTTL: true,
      ttl: 10,
    })
    for (let i = 0; i < 3; i++) {
      c.set(i, i)
    }
    clock.advance(9)
    // set, but do not update ttl.  this will fall out.
    c.set(0, 0, { status: s() })

    // set, but update the TTL
    c.set(1, 1, { noUpdateTTL: false, status: s() })
    clock.advance(9)
    c.purgeStale()

    t.equal(
      c.get(2, { status: s() }),
      undefined,
      'fell out of cache normally',
    )
    t.equal(c.get(1, { status: s() }), 1, 'still in cache, ttl updated')
    t.equal(
      c.get(0, { status: s() }),
      undefined,
      'fell out of cache, despite update',
    )

    clock.advance(9)
    c.purgeStale()
    t.equal(
      c.get(1, { status: s() }),
      undefined,
      'fell out of cache after ttl update',
    )

    t.end()
  })

  // https://github.com/isaacs/node-lru-cache/issues/203
  t.test('indexes/rindexes can walk over stale entries', t => {
    const c = new LRU({ max: 10, ttl: 10 })
    const e = expose(c, LRU)
    for (let i = 0; i < 3; i++) {
      c.set(i, i)
    }
    clock.advance(9)
    for (let i = 3; i < 10; i++) {
      c.set(i, i)
    }
    c.get(1)
    c.get(3)
    clock.advance(9)
    const indexes = [...e.indexes()]
    const indexesStale = [...e.indexes({ allowStale: true })]
    const rindexes = [...e.rindexes()]
    const rindexesStale = [...e.rindexes({ allowStale: true })]
    t.same(
      {
        indexes,
        indexesStale,
        rindexes,
        rindexesStale,
      },
      {
        indexes: [3, 9, 8, 7, 6, 5, 4],
        indexesStale: [3, 1, 9, 8, 7, 6, 5, 4, 2, 0],
        rindexes: [4, 5, 6, 7, 8, 9, 3],
        rindexesStale: [0, 2, 4, 5, 6, 7, 8, 9, 1, 3],
      },
    )
    t.end()
  })

  // https://github.com/isaacs/node-lru-cache/issues/203
  t.test('clear() disposes stale entries', t => {
    const disposed: any[] = []
    const disposedAfter: any[] = []
    const c = new LRU({
      max: 3,
      ttl: 10,
      dispose: (v: any, k: any) => disposed.push([v, k]),
      disposeAfter: (v: any, k: any) => disposedAfter.push([v, k]),
    })
    for (let i = 0; i < 4; i++) {
      c.set(i, i)
    }
    t.same(disposed, [[0, 0]])
    t.same(disposedAfter, [[0, 0]])
    clock.advance(20)
    c.clear()
    t.same(disposed, [
      [0, 0],
      [1, 1],
      [2, 2],
      [3, 3],
    ])
    t.same(disposedAfter, [
      [0, 0],
      [1, 1],
      [2, 2],
      [3, 3],
    ])
    t.end()
  })

  t.test('purgeStale() lockup', t => {
    const c = new LRU({
      max: 3,
      ttl: 10,
      updateAgeOnGet: true,
    })
    c.set(1, 1)
    c.set(2, 2)
    c.set(3, 3)
    clock.advance(5)
    c.get(2)
    clock.advance(15)
    c.purgeStale()
    t.pass('did not get locked up')
    t.end()
  })

  t.test('set item pre-stale', t => {
    const c = new LRU({
      max: 3,
      ttl: 10,
      allowStale: true,
    })
    c.set(1, 1)
    t.equal(c.has(1), true)
    t.equal(c.get(1), 1)
    c.set(2, 2, { start: clock.now() - 11 })
    t.equal(c.has(2), false)
    t.equal(c.get(2), 2)
    t.equal(c.get(2), undefined)
    c.set(2, 2, { start: clock.now() - 11 })
    const dump = c.dump()
    t.matchSnapshot(dump, 'dump with stale values')
    const d = new LRU({ max: 3, ttl: 10, allowStale: true })
    d.load(dump)
    t.equal(d.has(2), false)
    t.equal(d.get(2), 2)
    t.equal(d.get(2), undefined)
    t.end()
  })

  t.test('no delete on stale get', t => {
    const c = new LRU({
      noDeleteOnStaleGet: true,
      ttl: 10,
      max: 3,
    })
    c.set(1, 1)
    clock.advance(11)
    t.equal(c.has(1), false)
    t.equal(c.get(1), undefined)
    t.equal(c.get(1, { allowStale: true }), 1)
    t.equal(c.get(1, { allowStale: true, noDeleteOnStaleGet: false }), 1)
    t.equal(c.get(1, { allowStale: true }), undefined)
    t.end()
  })

  t.test('updateAgeOnGet reschedules ttlAutopurge timer', t => {
    const c = new LRU({
      ttl: 100,
      ttlAutopurge: true,
      updateAgeOnGet: true,
      ttlResolution: 0,
    })
    // set an entry
    c.set('a', 1)
    t.equal(c.size, 1)

    // get it before original TTL expires — this should refresh the TTL
    clock.advance(80)
    t.equal(c.get('a'), 1, 'still alive before original TTL')
    t.equal(c.size, 1, 'size is 1 after get')

    // advance past the original TTL (80 + 30 = 110 from set, but only 30 from get)
    clock.advance(30)
    t.equal(
      c.size,
      1,
      'entry survives past original TTL because get refreshed it',
    )
    t.equal(c.get('a'), 1, 'entry is still retrievable')

    // now let the refreshed TTL expire without any more gets
    // after the second get above, the TTL was refreshed again
    // advance past that refreshed TTL (100 + 1 for the timer margin)
    clock.advance(102)
    t.equal(c.size, 0, 'entry is autopurged after refreshed TTL expires')
    t.equal(c.get('a'), undefined, 'entry is gone')

    t.end()
  })

  t.test(
    'updateAgeOnGet + ttlAutopurge: entry eventually purged if not re-accessed',
    t => {
      const c = new LRU({
        ttl: 50,
        ttlAutopurge: true,
        updateAgeOnGet: true,
        ttlResolution: 0,
      })
      c.set('b', 2)
      t.equal(c.size, 1)

      // access once before TTL expires, refreshing the timer
      clock.advance(30)
      t.equal(c.get('b'), 2, 'alive before TTL')

      // do NOT access again — let the refreshed TTL expire
      // the refreshed TTL starts at t=30, expires at t=30+50+1=81
      clock.advance(52)
      t.equal(
        c.size,
        0,
        'entry autopurged after refreshed TTL with no further access',
      )
      t.equal(c.get('b'), undefined, 'entry is gone')

      t.end()
    },
  )

  t.end()
}

t.test('tests with perf_hooks.performance.now()', t => {
  const { performance, Date } = global
  // @ts-ignore
  t.teardown(() => Object.assign(global, { performance, Date }))
  // @ts-ignore
  global.Date = clock.Date
  // @ts-ignore
  global.performance = clock
  const { LRUCache: LRU } = t.mockRequire('../', {})
  runTests(LRU, t)
})

t.test('tests using Date.now()', t => {
  const { performance, Date } = global
  // @ts-ignore
  t.teardown(() => Object.assign(global, { performance, Date }))
  // @ts-ignore
  global.Date = clock.Date
  // @ts-ignore
  global.performance = null
  const { LRUCache: LRU } = t.mockRequire('../', {})
  runTests(LRU, t)
})
```

## File: `test/unbounded-warning.ts`
```typescript
import t from 'tap'
import { LRUCache } from '../dist/esm/index.js'

t.test('emits warning', t => {
  const { emitWarning } = process
  t.teardown(() => {
    process.emitWarning = emitWarning
  })
  const warnings: [string, string, string][] = []
  Object.defineProperty(process, 'emitWarning', {
    value: (msg: string, type: string, code: string) => {
      warnings.push([msg, type, code])
    },
    configurable: true,
    writable: true,
  })
  //@ts-expect-error
  new LRUCache({
    ttl: 100,
  })
  t.same(warnings, [
    [
      'TTL caching without ttlAutopurge, max, or maxSize can result in unbounded memory consumption.',
      'UnboundedCacheWarning',
      'LRU_CACHE_UNBOUNDED',
    ],
  ])
  t.end()
})

t.test('prints to stderr if no process.emitWarning', t => {
  const { LRUCache: LRU } = t.mockRequire('../', {}) as {
    LRUCache: typeof LRUCache
  }
  const { error } = console
  const { emitWarning } = process
  t.teardown(() => {
    console.error = error
    process.emitWarning = emitWarning
  })
  const warnings: [string][] = []
  Object.defineProperty(console, 'error', {
    value: (msg: string) => {
      warnings.push([msg])
    },
    configurable: true,
    writable: true,
  })
  Object.defineProperty(process, 'emitWarning', {
    value: undefined,
    configurable: true,
    writable: true,
  })
  //@ts-expect-error
  new LRU({
    ttl: 100,
  })
  //@ts-expect-error
  new LRU({
    ttl: 100,
  })
  t.same(warnings, [
    [
      '[LRU_CACHE_UNBOUNDED] UnboundedCacheWarning: TTL caching without ttlAutopurge, max, or maxSize can result in unbounded memory consumption.',
    ],
  ])
  t.end()
})
```

## File: `test/warn-missing-ac.ts`
```typescript
import { createRequire } from 'module'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const main = async () => {
  const { default: t } = await import('tap')
  const { spawn } = await import('child_process')

  // need to run both tests in parallel so we don't miss the close event
  t.jobs = 3

  const argv = process.execArgv.filter(a => !a.startsWith('--no-warnings'))
  const warn = spawn(process.execPath, [...argv, __filename, 'child'], {
    env: {
      ...process.env,
      NODE_OPTIONS: '',
    },
  })
  const warnErr: Buffer[] = []
  warn.stderr.on('data', c => warnErr.push(c))

  const noWarn = spawn(process.execPath, [...argv, __filename, 'child'], {
    env: {
      ...process.env,
      LRU_CACHE_IGNORE_AC_WARNING: '1',
      NODE_OPTIONS: '',
    },
  })
  const noWarnErr: Buffer[] = []
  noWarn.stderr.on('data', c => noWarnErr.push(c))

  const noFetch = spawn(
    process.execPath,
    [...argv, __filename, 'child-no-fetch'],
    {
      env: {
        ...process.env,
        NODE_OPTIONS: '',
      },
    },
  )
  const noFetchErr: Buffer[] = []
  noFetch.stderr.on('data', c => noFetchErr.push(c))

  t.test('no warning', async t => {
    await new Promise<void>(r =>
      noWarn.on('close', (code, signal) => {
        t.equal(code, 0)
        t.equal(signal, null)
        r()
      }),
    )
    t.notMatch(
      Buffer.concat(noWarnErr).toString().trim(),
      'NO_ABORT_CONTROLLER',
    )
  })

  t.test('no warning (because no fetch)', async t => {
    await new Promise<void>(r =>
      noFetch.on('close', (code, signal) => {
        t.equal(code, 0)
        t.equal(signal, null)
        r()
      }),
    )
    t.notMatch(
      Buffer.concat(noWarnErr).toString().trim(),
      'NO_ABORT_CONTROLLER',
    )
  })

  t.test('warning', async t => {
    await new Promise<void>(r =>
      warn.on('close', (code, signal) => {
        t.equal(code, 0)
        t.equal(signal, null)
        r()
      }),
    )
    t.match(
      Buffer.concat(warnErr).toString().trim(),
      /NO_ABORT_CONTROLLER/,
    )
  })
}

switch (process.argv[2]) {
  case 'child':
    //@ts-expect-error
    process.emitWarning = null
    //@ts-expect-error
    globalThis.AbortController = undefined
    //@ts-expect-error
    globalThis.AbortSignal = undefined
    const req = createRequire(import.meta.url)
    const { LRUCache } = req('../dist/commonjs/index.js')
    new LRUCache({ max: 1, fetchMethod: async () => 1 }).fetch(1)
    break
  case 'child-no-fetch':
    //@ts-expect-error
    globalThis.AbortController = undefined
    //@ts-expect-error
    globalThis.AbortSignal = undefined
    import('../dist/esm/index.js')
    break
  default:
    main()
}
```

## File: `test/fixtures/expose.ts`
```typescript
import { LRUCache } from '../../dist/esm/index.js'
export const expose = <
  K extends {},
  V extends {},
  FC extends unknown = unknown,
>(
  cache: LRUCache<K, V, FC>,
  LRU = LRUCache,
) => {
  return Object.assign(LRU.unsafeExposeInternals(cache), cache)
}
```

