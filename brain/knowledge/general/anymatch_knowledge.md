# Knowledge Dump for anymatch

## File: .travis.yml
```
sudo: false
arch:
    - amd64
    - ppc64le
language: node_js
node_js:
  - node
  - '10'
  - '8'

```

## File: examples.js
```
const inspect = require('util').inspect;
const i = function (val) {return inspect(val, {colors: true})};

const origAnymatch = require('./').default;
console.log("const anymatch = require('anymatch');\n");

const matchers = [
  'path/to/file.js',
  'path/anyjs/**/*.js',
  /foo.js$/,
  (string => string.includes('bar') && string.length > 10)
];

console.log('const matchers =',
  i(matchers).replace('[Function]', matchers[3].toString() + ''), ';\n');

const anymatch = (...args) => {
  let arg1 = args[0] === matchers ? `matchers` : i(args[0]);
  let str = `anymatch(${arg1}, ${i(args[1])}`;
  if (args[2]) str += `, ${i(args[2])}`;
  str += `);`
  console.log(`${str} // ${i(origAnymatch(...args))}`)
};

anymatch(matchers, 'path/to/file.js'); // true
anymatch(matchers, 'path/anyjs/baz.js'); // true
anymatch(matchers, 'path/to/foo.js'); // true
anymatch(matchers, 'path/to/bar.js'); // true
anymatch(matchers, 'bar.js'); // false

// returnIndex = true
anymatch(matchers, 'foo.js', true); // 2
anymatch(matchers, 'path/anyjs/foo.js', true); // 1

// using globs to match directories and their children
anymatch('node_modules', 'node_modules'); // true
anymatch('node_modules', 'node_modules/somelib/index.js'); // false
anymatch('node_modules/**', 'node_modules/somelib/index.js'); // true
anymatch('node_modules/**', '/absolute/path/to/node_modules/somelib/index.js'); // false
anymatch('**/node_modules/**', '/absolute/path/to/node_modules/somelib/index.js'); // true

const matcher = origAnymatch(matchers);
matcher('path/to/file.js'); // true
matcher('path/anyjs/baz.js', true); // 1

// console.log(i(['foo.js', 'bar.js'].filter(matcher))); // ['foo.js']
console.log( '\nconst matcher = anymatch(matchers);' );
console.log("['foo.js', 'bar.js'].filter(matcher);",
    " //", i(['foo.js', 'bar.js'].filter(matcher) )); // ['foo.js']

```

## File: index.d.ts
```
type AnymatchFn = (testString: string) => boolean;
type AnymatchPattern = string|RegExp|AnymatchFn;
type AnymatchMatcher = AnymatchPattern|AnymatchPattern[]
type AnymatchTester = {
  (testString: string|any[], returnIndex: true): number;
  (testString: string|any[]): boolean;
}

type PicomatchOptions = {dot: boolean};

declare const anymatch: {
  (matchers: AnymatchMatcher): AnymatchTester;
  (matchers: AnymatchMatcher, testString: null, returnIndex: true | PicomatchOptions): AnymatchTester;
  (matchers: AnymatchMatcher, testString: string|any[], returnIndex: true | PicomatchOptions): number;
  (matchers: AnymatchMatcher, testString: string|any[]): boolean;
}

export {AnymatchMatcher as Matcher}
export {AnymatchTester as Tester}
export default anymatch

```

## File: index.js
```
'use strict';

Object.defineProperty(exports, "__esModule", { value: true });

const picomatch = require('picomatch');
const normalizePath = require('normalize-path');

/**
 * @typedef {(testString: string) => boolean} AnymatchFn
 * @typedef {string|RegExp|AnymatchFn} AnymatchPattern
 * @typedef {AnymatchPattern|AnymatchPattern[]} AnymatchMatcher
 */
const BANG = '!';
const DEFAULT_OPTIONS = {returnIndex: false};
const arrify = (item) => Array.isArray(item) ? item : [item];

/**
 * @param {AnymatchPattern} matcher
 * @param {object} options
 * @returns {AnymatchFn}
 */
const createPattern = (matcher, options) => {
  if (typeof matcher === 'function') {
    return matcher;
  }
  if (typeof matcher === 'string') {
    const glob = picomatch(matcher, options);
    return (string) => matcher === string || glob(string);
  }
  if (matcher instanceof RegExp) {
    return (string) => matcher.test(string);
  }
  return (string) => false;
};

/**
 * @param {Array<Function>} patterns
 * @param {Array<Function>} negPatterns
 * @param {String|Array} args
 * @param {Boolean} returnIndex
 * @returns {boolean|number}
 */
const matchPatterns = (patterns, negPatterns, args, returnIndex) => {
  const isList = Array.isArray(args);
  const _path = isList ? args[0] : args;
  if (!isList && typeof _path !== 'string') {
    throw new TypeError('anymatch: second argument must be a string: got ' +
      Object.prototype.toString.call(_path))
  }
  const path = normalizePath(_path, false);

  for (let index = 0; index < negPatterns.length; index++) {
    const nglob = negPatterns[index];
    if (nglob(path)) {
      return returnIndex ? -1 : false;
    }
  }

  const applied = isList && [path].concat(args.slice(1));
  for (let index = 0; index < patterns.length; index++) {
    const pattern = patterns[index];
    if (isList ? pattern(...applied) : pattern(path)) {
      return returnIndex ? index : true;
    }
  }

  return returnIndex ? -1 : false;
};

/**
 * @param {AnymatchMatcher} matchers
 * @param {Array|string} testString
 * @param {object} options
 * @returns {boolean|number|Function}
 */
const anymatch = (matchers, testString, options = DEFAULT_OPTIONS) => {
  if (matchers == null) {
    throw new TypeError('anymatch: specify first argument');
  }
  const opts = typeof options === 'boolean' ? {returnIndex: options} : options;
  const returnIndex = opts.returnIndex || false;

  // Early cache for matchers.
  const mtchers = arrify(matchers);
  const negatedGlobs = mtchers
    .filter(item => typeof item === 'string' && item.charAt(0) === BANG)
    .map(item => item.slice(1))
    .map(item => picomatch(item, opts));
  const patterns = mtchers
    .filter(item => typeof item !== 'string' || (typeof item === 'string' && item.charAt(0) !== BANG))
    .map(matcher => createPattern(matcher, opts));

  if (testString == null) {
    return (testString, ri = false) => {
      const returnIndex = typeof ri === 'boolean' ? ri : false;
      return matchPatterns(patterns, negatedGlobs, testString, returnIndex);
    }
  }

  return matchPatterns(patterns, negatedGlobs, testString, returnIndex);
};

anymatch.default = anymatch;
module.exports = anymatch;

```

## File: package.json
```
{
  "name": "anymatch",
  "version": "3.1.3",
  "description": "Matches strings against configurable strings, globs, regular expressions, and/or functions",
  "files": [
    "index.js",
    "index.d.ts"
  ],
  "dependencies": {
    "normalize-path": "^3.0.0",
    "picomatch": "^2.0.4"
  },
  "author": {
    "name": "Elan Shanker",
    "url": "https://github.com/es128"
  },
  "license": "ISC",
  "homepage": "https://github.com/micromatch/anymatch",
  "repository": {
    "type": "git",
    "url": "https://github.com/micromatch/anymatch"
  },
  "keywords": [
    "match",
    "any",
    "string",
    "file",
    "fs",
    "list",
    "glob",
    "regex",
    "regexp",
    "regular",
    "expression",
    "function"
  ],
  "scripts": {
    "test": "nyc mocha",
    "mocha": "mocha"
  },
  "devDependencies": {
    "mocha": "^6.1.3",
    "nyc": "^14.0.0"
  },
  "engines": {
    "node": ">= 8"
  }
}

```

## File: README.md
```
anymatch [![Build Status](https://travis-ci.org/micromatch/anymatch.svg?branch=master)](https://travis-ci.org/micromatch/anymatch) [![Coverage Status](https://img.shields.io/coveralls/micromatch/anymatch.svg?branch=master)](https://coveralls.io/r/micromatch/anymatch?branch=master)
======
Javascript module to match a string against a regular expression, glob, string,
or function that takes the string as an argument and returns a truthy or falsy
value. The matcher can also be an array of any or all of these. Useful for
allowing a very flexible user-defined config to define things like file paths.

__Note: This module has Bash-parity, please be aware that Windows-style backslashes are not supported as separators. See https://github.com/micromatch/micromatch#backslashes for more information.__


Usage
-----
```sh
npm install anymatch
```

#### anymatch(matchers, testString, [returnIndex], [options])
* __matchers__: (_Array|String|RegExp|Function_)
String to be directly matched, string with glob patterns, regular expression
test, function that takes the testString as an argument and returns a truthy
value if it should be matched, or an array of any number and mix of these types.
* __testString__: (_String|Array_) The string to test against the matchers. If
passed as an array, the first element of the array will be used as the
`testString` for non-function matchers, while the entire array will be applied
as the arguments for function matchers.
* __options__: (_Object_ [optional]_) Any of the [picomatch](https://github.com/micromatch/picomatch#options) options.
    * __returnIndex__: (_Boolean [optional]_) If true, return the array index of
the first matcher that that testString matched, or -1 if no match, instead of a
boolean result.

```js
const anymatch = require('anymatch');

const matchers = [ 'path/to/file.js', 'path/anyjs/**/*.js', /foo.js$/, string => string.includes('bar') && string.length > 10 ] ;

anymatch(matchers, 'path/to/file.js'); // true
anymatch(matchers, 'path/anyjs/baz.js'); // true
anymatch(matchers, 'path/to/foo.js'); // true
anymatch(matchers, 'path/to/bar.js'); // true
anymatch(matchers, 'bar.js'); // false

// returnIndex = true
anymatch(matchers, 'foo.js', {returnIndex: true}); // 2
anymatch(matchers, 'path/anyjs/foo.js', {returnIndex: true}); // 1

// any picomatc

// using globs to match directories and their children
anymatch('node_modules', 'node_modules'); // true
anymatch('node_modules', 'node_modules/somelib/index.js'); // false
anymatch('node_modules/**', 'node_modules/somelib/index.js'); // true
anymatch('node_modules/**', '/absolute/path/to/node_modules/somelib/index.js'); // false
anymatch('**/node_modules/**', '/absolute/path/to/node_modules/somelib/index.js'); // true

const matcher = anymatch(matchers);
['foo.js', 'bar.js'].filter(matcher);  // [ 'foo.js' ]
anymatch master* ❯

```

#### anymatch(matchers)
You can also pass in only your matcher(s) to get a curried function that has
already been bound to the provided matching criteria. This can be used as an
`Array#filter` callback.

```js
var matcher = anymatch(matchers);

matcher('path/to/file.js'); // true
matcher('path/anyjs/baz.js', true); // 1

['foo.js', 'bar.js'].filter(matcher); // ['foo.js']
```

Changelog
----------
[See release notes page on GitHub](https://github.com/micromatch/anymatch/releases)

- **v3.0:** Removed `startIndex` and `endIndex` arguments. Node 8.x-only.
- **v2.0:** [micromatch](https://github.com/jonschlinkert/micromatch) moves away from minimatch-parity and inline with Bash. This includes handling backslashes differently (see https://github.com/micromatch/micromatch#backslashes for more information).
- **v1.2:** anymatch uses [micromatch](https://github.com/jonschlinkert/micromatch)
for glob pattern matching. Issues with glob pattern matching should be
reported directly to the [micromatch issue tracker](https://github.com/jonschlinkert/micromatch/issues).

License
-------
[ISC](https://raw.github.com/micromatch/anymatch/master/LICENSE)

```

## File: test.js
```
'use strict';

let anymatch = require('./');
let assert = require('assert');
let path = require('path');

describe('anymatch', () => {
  var matchers = [
    'path/to/file.js',
    'path/anyjs/**/*.js',
    /foo.js$/,
    (string => string.indexOf('/bar') !== -1 && string.length > 10)
  ];
  it('should resolve string matchers', () => {
    assert(anymatch(matchers, 'path/to/file.js'));
    assert(anymatch(matchers[0], 'path/to/file.js'));
    assert(!anymatch(matchers[0], 'bar.js'));
  });
  it('should resolve glob matchers', () => {
    assert.equal(true, anymatch(matchers, 'path/anyjs/baz.js'));
    assert.equal(true, anymatch(matchers[1], 'path/anyjs/baz.js'));
    assert.equal(false, anymatch(matchers[1], 'bar.js'));
  });
  it('should resolve regexp matchers', () => {
    assert.equal(true, anymatch(matchers, 'path/to/foo.js'));
    assert.equal(true, anymatch(matchers[2], 'path/to/foo.js'));
    assert.equal(false, anymatch(matchers[2], 'bar.js'));
  });
  it('should resolve function matchers', () => {
    assert.equal(true, anymatch(matchers, 'path/to/bar.js'));
    assert.equal(true, anymatch(matchers[3], 'path/to/bar.js'));
    assert.equal(false, anymatch(matchers[3], 'bar.js'));
  });
  it('should return false for unmatched strings', () => {
    assert.equal(false, anymatch(matchers, 'bar.js'));
  });
  it('should ignore improperly typed matchers', () => {
    var emptyObj = {};
    assert.equal(false, anymatch(emptyObj, ''));
    assert.equal(false, anymatch(Infinity, ''));
  });
  it('should keep trailing separators on paths to match /*/ globs', () => {
    assert.equal(true, anymatch('path/to/*/', 'path/to/dir/'));
  });

  describe('with returnIndex = true', () => {
    it('should return the array index of first positive matcher', () => {
      var result = anymatch(matchers, 'foo.js', true);
      assert.equal(result, 2);
    });
    it('should return 0 if provided non-array matcher', () => {
      var result = anymatch(matchers[2], 'foo.js', true);
      assert.equal(result, 0);
    });
    it('should return -1 if no match', () => {
      var result = anymatch(matchers, 'bar.js', true);
      assert.equal(result, -1);
    });
  });

  describe('curried matching function', () => {
    var matchFn;
    before(() => {
      matchFn = anymatch(matchers);
    });
    it('should resolve matchers', () => {
      assert.equal(true, matchFn('path/to/file.js'));
      assert.equal(true, matchFn('path/anyjs/baz.js'));
      assert.equal(true, matchFn('path/to/foo.js'));
      assert.equal(true, matchFn('path/to/bar.js'));
      assert.equal(false, matchFn('bar.js'));
    });
    it('should be usable as an Array.prototype.filter callback', () => {
      var arr = [
        'path/to/file.js',
        'path/anyjs/baz.js',
        'path/to/foo.js',
        'path/to/bar.js',
        'bar.js',
        'foo.js'
      ];
      var expected = arr.slice();
      expected.splice(arr.indexOf('bar.js'), 1);
      assert.deepEqual(arr.filter(matchFn), expected);
    });
    it('should bind individual criterion', () => {
      assert(anymatch(matchers[0])('path/to/file.js'));
      assert(!anymatch(matchers[0])('path/to/other.js'));
      assert(anymatch(matchers[1])('path/anyjs/baz.js'));
      assert(!anymatch(matchers[1])('path/to/baz.js'));
      assert(anymatch(matchers[2])('path/to/foo.js'));
      assert(!anymatch(matchers[2])('path/to/foo.js.bak'));
      assert(anymatch(matchers[3])('path/to/bar.js'));
      assert(!anymatch(matchers[3])('bar.js'));
    });
  });

  describe('extra args', () => {
    it('should not allow no args', () => {
      assert.throws(() => anymatch());
    })
    it('should not allow bad testString', () => {
      assert.throws(() => anymatch(matchers, { path: 'path/to/bar.js' }));
    });
    it('should allow string to be passed as first member of an array', () => {
      assert.doesNotThrow(() => anymatch(matchers, ['path/to/bar.js']));
    });

    it('should pass extra args to function matchers', () => {
      matchers.push((string, arg1, arg2) => arg1 || arg2);
      assert(!anymatch(matchers, 'bar.js'), '1');
      assert(!anymatch(matchers, ['bar.js', 0]), '2');
      assert(anymatch(matchers, ['bar.js', true]), '3');
      assert(anymatch(matchers, ['bar.js', 0, true]), '4');
      // with returnIndex
      assert.equal(anymatch(matchers, ['bar.js', 1], true), 4, '5');
      // curried versions
      var matchFn1 = anymatch(matchers);
      var matchFn2 = anymatch(matchers[4]);
      assert(!matchFn1(['bar.js', 0]), '6');
      assert(!matchFn2(['bar.js', 0]), '7');
      assert(matchFn1(['bar.js', true]), '8');
      assert(matchFn2(['bar.js', true]), '9');
      assert(matchFn1(['bar.js', 0, true]), '10');
      assert(matchFn2(['bar.js', 0, true]), '11');
      // curried with returnIndex
      assert.equal(matchFn1(['bar.js', 1], true), 4, '12');
      assert.equal(matchFn2(['bar.js', 1], true), 0, '13');
      assert.equal(matchFn1(['bar.js', 0], true), -1, '14');
      assert.equal(matchFn2(['bar.js', 0], true), -1, '15');
      matchers.pop();
    });
  });

  describe('glob negation', () => {
    after(matchers.splice.bind(matchers, 4, 3));

    it('should respect negated globs included in a matcher array', () => {
      assert(anymatch(matchers, 'path/anyjs/no/no.js'), 'matches existing glob');
      matchers.push('!path/anyjs/no/*.js');
      assert(!anymatch(matchers, 'path/anyjs/no/no.js'), 'should be negated');
      assert(!anymatch(matchers)('path/anyjs/no/no.js'), 'should be negated (curried)');
    });
    it('should not break returnIndex option', () => {
      assert.equal(anymatch(matchers, 'path/anyjs/yes.js', true), 1);
      assert.equal(anymatch(matchers)('path/anyjs/yes.js', true), 1);
      assert.equal(anymatch(matchers, 'path/anyjs/no/no.js', true), -1);
      assert.equal(anymatch(matchers)('path/anyjs/no/no.js', true), -1);
    });
    it('should allow negated globs to negate non-glob matchers', () => {
      assert.equal(anymatch(matchers, 'path/to/bar.js', true), 3);
      matchers.push('!path/to/bar.*');
      assert(!anymatch(matchers, 'path/to/bar.js'));
    });
    it('should not match negated matchers if positive matchers do not match', () => {
      assert(!anymatch(matchers, 'path/anyjs/no/no.ts'), 'does not match existing glob');
      matchers.push('!path/anyjs/ts/*.js');
      assert(!anymatch(matchers, 'path/anyjs/no/no.ts'), 'should not be negated');
      assert(!anymatch(matchers)('path/anyjs/no/no.ts'), 'should not be negated (curried)');
    })
  });

  describe('windows paths', () => {
    var origSep = path.sep;
    before(() => {
      path.sep = '\\';
    });
    after(() => {
      path.sep = origSep;
    });

    it('should resolve backslashes against string matchers', () => {
      assert(anymatch(matchers, 'path\\to\\file.js'));
      assert(anymatch(matchers)('path\\to\\file.js'));
    });
    it('should resolve backslashes against glob matchers', () => {
      assert(anymatch(matchers, 'path\\anyjs\\file.js'));
      assert(anymatch(matchers)('path\\anyjs\\file.js'));
    });
    it('should resolve backslashes against regex matchers', () => {
      assert(anymatch(/path\/to\/file\.js/, 'path\\to\\file.js'));
      assert(anymatch(/path\/to\/file\.js/)('path\\to\\file.js'));
    });
    it('should resolve backslashes against function matchers', () => {
      assert(anymatch(matchers, 'path\\to\\bar.js'));
      assert(anymatch(matchers)('path\\to\\bar.js'));
    });
    it('should still correctly handle forward-slash paths', () => {
      assert(anymatch(matchers, 'path/to/file.js'));
      assert(anymatch(matchers)('path/to/file.js'));
      assert(!anymatch(matchers, 'path/no/no.js'));
      assert(!anymatch(matchers)('path/no/no.js'));
    });
  });

  describe('picomatch options', () => {
    it('should support picomatch options', () => {
      assert.equal(false, anymatch('path/to/?dotfile', 'path/to/.dotfile'));
      assert.equal(true, anymatch('path/to/?dotfile', 'path/to/.dotfile', { dot: true }));
    });
  });
});

```

