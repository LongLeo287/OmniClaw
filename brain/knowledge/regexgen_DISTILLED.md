---
id: regexgen
type: knowledge
owner: OA_Triage
---
# regexgen
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
const Trie = require('./src/trie');

/**
 * Generates a regular expression that matches the given input strings.
 * @param {Array<string>} inputs
 * @param {string} flags
 * @return {RegExp}
 */
function regexgen(inputs, flags) {
  let trie = new Trie;
  trie.addAll(inputs);
  return trie.toRegExp(flags);
}

regexgen.Trie = Trie;
module.exports = regexgen;

```

### File: package.json
```json
{
  "name": "regexgen",
  "version": "1.3.0",
  "description": "Generate regular expressions that match a set of strings",
  "main": "index.js",
  "bin": {
    "regexgen": "bin/cli.js"
  },
  "dependencies": {
    "jsesc": "^2.3.0",
    "regenerate": "^1.3.2"
  },
  "devDependencies": {
    "mocha": "^3.2.0"
  },
  "scripts": {
    "test": "mocha"
  },
  "engines": {
    "node": ">= 6"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/devongovett/regexgen.git"
  },
  "keywords": [
    "regex",
    "trie",
    "regular",
    "expression"
  ],
  "author": "Devon Govett <devongovett@gmail.com>",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/devongovett/regexgen/issues"
  },
  "homepage": "https://github.com/devongovett/regexgen#readme",
  "runkitExample": "const regexgen = require('regexgen');\n\nregexgen(['foobar', 'foobaz', 'foozap', 'fooza']);"
}

```

### File: README.md
```md
# regexgen

Generates regular expressions that match a set of strings.

## Installation

`regexgen` can be installed using [npm](https://npmjs.com):

```
npm install regexgen
```

## Example

The simplest use is to simply pass an array of strings to `regexgen`:

```javascript
const regexgen = require('regexgen');

regexgen(['foobar', 'foobaz', 'foozap', 'fooza']); // => /foo(?:zap?|ba[rz])/
```

You can also use the `Trie` class directly:

```javascript
const {Trie} = require('regexgen');

let t = new Trie;
t.add('foobar');
t.add('foobaz');

t.toRegExp(); // => /fooba[rz]/
```

## CLI

`regexgen` also has a simple CLI to generate regexes using inputs from the command line.

```shell
$ regexgen
Usage: regexgen [-gimuy] string1 string2 string3...
```

The optional first parameter is the [flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp) to add
to the regex (e.g. `-i` for a case insensitive match).

## ES2015 and Unicode

By default `regexgen` will output a standard JavaScript regular expression, with Unicode codepoints converted into UCS-2 surrogate pairs.

If desired, you can request an ES2015-compatible Unicode regular expression by supplying the `-u` flag, which results in those codepoints being retained.

```shell
$ regexgen 👩 👩‍💻 👩🏻‍💻 👩🏼‍💻 👩🏽‍💻 👩🏾‍💻 👩🏿‍💻
/\uD83D\uDC69(?:(?:\uD83C[\uDFFB-\uDFFF])?\u200D\uD83D\uDCBB)?/

$ regexgen -u 👩 👩‍💻 👩🏻‍💻 👩🏼‍💻 👩🏽‍💻 👩🏾‍💻 👩🏿‍💻
/\u{1F469}(?:[\u{1F3FB}-\u{1F3FF}]?\u200D\u{1F4BB})?/u
```


Such regular expressions are compatible with current versions of Node, as well as the latest browsers, and may be more transferrable to other languages.

## How does it work?

1. Generate a [Trie](https://en.wikipedia.org/wiki/Trie) containing all of the input strings.
   This is a tree structure where each edge represents a single character. This removes
   redundancies at the start of the strings, but common branches further down are not merged.

2. A trie can be seen as a tree-shaped deterministic finite automaton (DFA), so DFA algorithms
   can be applied. In this case, we apply [Hopcroft's DFA minimization algorithm](https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft.27s_algorithm)
   to merge the nondistinguishable states.

3. Convert the resulting minimized DFA to a regular expression. This is done using
   [Brzozowski's algebraic method](http://cs.stackexchange.com/questions/2016/how-to-convert-finite-automata-to-regular-expressions#2392),
   which is quite elegant. It expresses the DFA as a system of equations which can be solved
   for a resulting regex. Along the way, some additional optimizations are made, such
   as hoisting common substrings out of an alternation, and using character class ranges.
   This produces an an [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
   (AST) for the regex, which is then converted to a string and compiled to a JavaScript
   `RegExp` object.

## License

MIT

```

### File: bin\cli.js
```js
#!/usr/bin/env node

const regexgen = require('../');

let args = process.argv.slice(2);
let flags = '';
if (args.length && args[0][0] === '-') {
  flags = args.shift().slice(1);
}

if (args.length === 0) {
  console.log('Usage: regexgen [-gimuy] string1 string2 string3...');
  process.exit(1);
}

console.log(regexgen(args, flags));

```

### File: src\ast.js
```js
const jsesc = require('jsesc');
const regenerate = require('regenerate');

/**
 * Represents an alternation (e.g. `foo|bar`)
 */
class Alternation {
  constructor(...options) {
    this.precedence = 1;
    this.options = this.flatten(options);
    this.options.sort((a, b) => b.length - a.length);
  }

  flatten(options) {
    return options.reduce((res, option) => res.concat(
      option instanceof Alternation ? this.flatten(option.options) : option
    ), []);
  }

  get length() {
    return this.options[0].length;
  }

  toString(flags) {
    return this.options.map(o => parens(o, this, flags)).join('|');
  }
}

/**
 * Represents a character class (e.g. [0-9a-z])
 */
class CharClass {
  constructor(a, b) {
    this.precedence = 1;
    this.set = regenerate(a, b);
  }

  get length() {
    return 1;
  }

  get isSingleCharacter() {
    return !this.set.toArray().some(c => c > 0xffff);
  }

  get isSingleCodepoint() {
    return true;
  }

  toString(flags) {
    return this.set.toString({
      hasUnicodeFlag: flags && flags.indexOf('u') !== -1
    });
  }

  getCharClass() {
    return this.set;
  }
}

/**
 * Represents a concatenation (e.g. `foo`)
 */
class Concatenation {
  constructor(a, b) {
    this.precedence = 2;
    this.a = a;
    this.b = b;
  }

  get length() {
    return this.a.length + this.b.length;
  }

  toString(flags) {
    return parens(this.a, this, flags) + parens(this.b, this, flags);
  }

  getLiteral(side) {
    if (side === 'start' && this.a.getLiteral) {
      return this.a.getLiteral(side);
    }

    if (side === 'end' && this.b.getLiteral) {
      return this.b.getLiteral(side);
    }
  }

  removeSubstring(side, len) {
    let {a, b} = this;
    if (side === 'start' && a.removeSubstring) {
      a = a.removeSubstring(side, len);
    }

    if (side === 'end' && b.removeSubstring) {
      b = b.removeSubstring(side, len);
    }

    return a.isEmpty ? b : b.isEmpty ? a : new Concatenation(a, b);
  }
}

/**
 * Represents a repetition (e.g. `a*` or `a?`)
 */
class Repetition {
  constructor(expr, type) {
    this.precedence = 3;
    this.expr = expr;
    this.type = type;
  }

  get length() {
    return this.expr.length;
  }

  toString(flags) {
    return parens(this.expr, this, flags) + this.type;
  }
}

/**
 * Represents a literal (e.g. a string)
 */
class Literal {
  constructor(value) {
    this.precedence = 2;
    this.value = value;
  }

  get isEmpty() {
    return !this.value;
  }

  get isSingleCharacter() {
    return this.length === 1;
  }

  get isSingleCodepoint() {
    return Array.from(this.value).length === 1;
  }

  get length() {
    return this.value.length;
  }

  toString(flags) {
    return jsesc(this.value, { es6: flags && flags.indexOf('u') !== -1 })
      .replace(/[\t\n\f\r\$\(\)\*\+\-\.\?\[\]\^\|]/g, '\\$&')

      // special handling to not escape curly braces which are part of Unicode escapes
      .replace(/(\\u\{[a-z0-9]+\})|([\{\}])/ig, (match, unicode, brace) => unicode || '\\' + brace);
  }

  getCharClass() {
    if (this.isSingleCodepoint) {
      return this.value;
    }
  }

  getLiteral() {
    return this.value;
  }

  removeSubstring(side, len) {
    if (side === 'start') {
      return new Literal(this.value.slice(len));
    }

    if (side === 'end') {
      return new Literal(this.value.slice(0, this.value.length - len));
    }
  }
}

function parens(exp, parent, flags) {
  let isUnicode = flags && flags.indexOf('u') !== -1;
  let str = exp.toString(flags);
  if (exp.precedence < parent.precedence && !exp.isSingleCharacter && !(isUnicode && exp.isSingleCodepoint)) {
    return '(?:' + str + ')';
  }

  return str;
}

exports.Alternation = Alternation;
exports.CharClass = CharClass;
exports.Concatenation = Concatenation;
exports.Repetition = Repetition;
exports.Literal = Literal;

```

### File: src\map.js
```js
/**
 * This ES6 Map subclass calls the getter function passed to
 * the constructor to initialize undefined properties when they
 * are first retrieved.
 */
class DefaultMap extends Map {
  constructor(iterable, defaultGetter) {
    if (typeof iterable === 'function') {
      defaultGetter = iterable;
      iterable = null;
    }

    super(iterable);
    this.defaultGetter = defaultGetter;
  }

  get(key) {
    if (!super.has(key)) {
      let res = this.defaultGetter(key);
      this.set(key, res);
      return res;
    }

    return super.get(key);
  }
}

module.exports = DefaultMap;

```

### File: src\minimize.js
```js
const Map = require('./map');
const Set = require('./set');
const State = require('./state');

/**
 * Implements Hopcroft's DFA minimization algorithm.
 * https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft.27s_algorithm
 *
 * @param {State} root - the initial state of the DFA
 * @return {State} - the new initial state
 */
function minimize(root) {
  let states = new Set(root.visit());
  let finalStates = states.filter(s => s.accepting);

  // Create a map of incoming transitions to each state, grouped by character.
  let transitions = new Map(k => new Map(k => new Set));
  for (let s of states) {
    for (let [t, st] of s.transitions) {
      transitions.get(st).get(t).add(s);
    }
  }

  let P = new Set([finalStates, states.difference(finalStates)]);
  let W = new Set(P);

  while (W.size > 0) {
    let A = W.shift();

    // Collect states that have transitions leading to states in A, grouped by character.
    let t = new Map(k => new Set);
    for (let s of A) {
      for (let [T, X] of transitions.get(s)) {
        t.get(T).addAll(X);
      }
    }

    for (let X of t.values()) {
      for (let Y of P) {
        let i = X.intersection(Y);
        if (i.size === 0) {
          continue;
        }

        let d = Y.difference(X);
        if (d.size === 0) {
          continue;
        }

        P.replace(Y, i, d);

        let y = W.find(v => v.equals(Y));
        if (y) {
          W.replace(y, i, d);
        } else if (i.size <= d.size) {
          W.add(i);
        } else {
          W.add(d);
        }
      }
    }
  }

  // Each set S in P now represents a state in the minimized DFA.
  // Build the new states and transitions.
  let newStates = new Map(k => new State);
  let initial = null;

  for (let S of P) {
    let first = S.first();
    let s = newStates.get(S);
    for (let [c, old] of first.transitions) {
      s.transitions.set(c, newStates.get(P.find(v => v.has(old))));
    }

    s.accepting = first.accepting;

    if (S.has(root)) {
      initial = s;
    }
  }

  return initial;
}

module.exports = minimize;

```

### File: src\regex.js
```js
const {Alternation, CharClass, Concatenation, Repetition, Literal} = require('./ast');

/**
 * Implements Brzozowski's algebraic method to convert a DFA into a regular
 * expression pattern.
 * http://cs.stackexchange.com/questions/2016/how-to-convert-finite-automata-to-regular-expressions#2392
 *
 * @param {State} root - the initial state of the DFA
 * @param {string} flags - The flags to add to the regex.
 * @return {String} - the converted regular expression pattern
 */
function toRegex(root, flags) {
  let states = Array.from(root.visit());

  // Setup the system of equations A and B from Arden's Lemma.
  // A represents a state transition table for the given DFA.
  // B is a vector of accepting states in the DFA, marked as epsilons.
  let A = [];
  let B = [];

  for (let i = 0; i < states.length; i++) {
    let a = states[i];
    if (a.accepting) {
      B[i] = new Literal('');
    }

    A[i] = [];
    for (let [t, s] of a.transitions) {
      let j = states.indexOf(s);
      A[i][j] = A[i][j] ? union(A[i][j], new Literal(t)) : new Literal(t);
    }
  }

  // Solve the of equations
  for (let n = states.length - 1; n >= 0; n--) {
    if (A[n][n] != null) {
      B[n] = concat(star(A[n][n]), B[n]);
      for (let j = 0; j < n; j++) {
        A[n][j] = concat(star(A[n][n]), A[n][j]);
      }
    }

    for (let i = 0; i < n; i++) {
      if (A[i][n] != null) {
        B[i] = union(B[i], concat(A[i][n], B[n]));
        for (let j = 0; j < n; j++) {
          A[i][j] = union(A[i][j], concat(A[i][n], A[n][j]));
        }
      }
    }
  }

  return B[0].toString(flags);
}

/**
 * Creates a repetition if `exp` exists.
 */
function star(exp) {
  return exp ? new Repetition(exp, '*') : null;
}

/**
 * Creates a union between two expressions
 */
function union(a, b) {
  if (a != null && b != null && a !== b) {
    // Hoist common substrings at the start and end of the options
    let start, end, res;
    [a, b, start] = removeCommonSubstring(a, b, 'start');
    [a, b, end] = removeCommonSubstring(a, b, 'end');

    // If a or b is empty, make an optional group instead
    if (a.isEmpty || b.isEmpty) {
      res = new Repetition(a.isEmpty ? b : a, '?');
    } else if (a instanceof Repetition && a.type === '?') {
      res = new Repetition(new Alternation(a.expr, b), '?');
    } else if (b instanceof Repetition && b.type === '?') {
      res = new Repetition(new Alternation(a, b.expr), '?');
    } else {
      // Check if we can make a character class instead of an alternation
      let ac = a.getCharClass && a.getCharClass();
      let bc = b.getCharClass && b.getCharClass();
      if (ac && bc) {
        res = new CharClass(ac, bc);
      } else {
        res = new Alternation(a, b);
      }
    }

    if (start) {
      res = new Concatenation(new Literal(start), res);
    }

    if (end) {
      res = new Concatenation(res, new Literal(end));
    }

    return res;
  }

  return a || b;
}

/**
 * Removes the common prefix or suffix from the two expressions
 */
function removeCommonSubstring(a, b, side) {
  let al = a.getLiteral && a.getLiteral(side);
  let bl = b.getLiteral && b.getLiteral(side);
  if (!al || !bl) {
    return [a, b, null];
  }

  let s = commonSubstring(al, bl, side);
  if (!s) {
    return [a, b, ''];
  }

  a = a.removeSubstring(side, s.length);
  b = b.removeSubstring(side, s.length);

  return [a, b, s];
}

/**
 * Finds the common prefix or suffix between to strings
 */
function commonSubstring(a, b, side) {
  let dir = side === 'start' ? 1 : -1;
  a = Array.from(a);
  b = Array.from(b);
  let ai = dir === 1 ? 0 : a.length - 1;
  let ae = dir === 1 ? a.length : -1;
  let bi = dir === 1 ? 0 : b.length - 1;
  let be = dir === 1 ? b.length : -1;
  let res = '';

  for (; ai !== ae && bi !== be && a[ai] === b[bi]; ai += dir, bi += dir) {
    if (dir === 1) {
      res += a[ai];
    } else {
      res = a[ai] + res;
    }
  }

  return res;
}

/**
 * Creates a concatenation between expressions a and b
 */
function concat(a, b) {
  if (a == null || b == null) {
    return null;
  }

  if (a.isEmpty) {
    return b;
  }

  if (b.isEmpty) {
    return a;
  }

  // Combine literals
  if (a instanceof Literal && b instanceof Literal) {
    return new Literal(a.value + b.value);
  }

  if (a instanceof Literal && b instanceof Concatenation && b.a instanceof Literal) {
    return new Concatenation(new Literal(a.value + b.a.value), b.b);
  }

  if (b instanceof Literal && a instanceof Concatenation && a.b instanceof Literal) {
    return new Concatenation(a.a, new Literal(a.b.value + b.value));
  }

  return new Concatenation(a, b);
}

module.exports = toRegex;

```

### File: src\set.js
```js
/**
 * This class extends the native ES6 Set class with some additional methods
 */
class ExtendedSet extends Set {
  filter(fn) {
    let res = new ExtendedSet;
    for (let x of this) {
      if (fn(x)) {
        res.add(x);
      }
    }

    return res;
  }

  difference(b) {
    return this.filter(x => !b.has(x));
  }

  intersection(b) {
    return this.filter(x => b.has(x));
  }

  equals(b) {
    if (this.size !== b.size) {
      return false;
    }

    for (let x of this) {
      if (!b.has(x)) {
        return false;
      }
    }

    return true;
  }

  find(fn) {
    for (let x of this) {
      if (fn(x)) {
        return x;
      }
    }

    return null;
  }

  first() {
    return this.values().next().value;
  }

  shift() {
    let v = this.first();
    this.delete(v);
    return v;
  }

  replace(search, ...replacements) {
    if (this.delete(search)) {
      this.addAll(replacements);
    }
  }

  addAll(items) {
    for (let x of items) {
      this.add(x);
    }
  }
}

module.exports = ExtendedSet;

```

### File: src\state.js
```js
const Map = require('./map');

/**
 * Represents a state in a DFA.
 */
class State {
  constructor() {
    this.accepting = false;
    this.transitions = new Map(k => new State);
  }

  /**
   * A generator that yields all states in the subtree
   * starting with this state.
   */
  *visit(visited = new Set) {
    if (visited.has(this)) return;
    visited.add(this);

    yield this;
    for (let state of this.transitions.values()) {
      yield* state.visit(visited);
    }
  }
}

module.exports = State;

```

### File: src\trie.js
```js
const State = require('./state');
const minimize = require('./minimize');
const toRegex = require('./regex');

/**
 * A Trie represents a set of strings in a tree data structure
 * where each edge represents a single character.
 * https://en.wikipedia.org/wiki/Trie
 */
class Trie {
  constructor() {
    this.alphabet = new Set;
    this.root = new State;
  }

  /**
   * Adds the given string to the trie.
   * @param {string} string - the string to add
   */
  add(string) {
    let node = this.root;
    for (let char of string) {
      this.alphabet.add(char);
      node = node.transitions.get(char);
    }

    node.accepting = true;
  }

  /**
   * Adds the given array of strings to the trie.
   * @param {Array<string>} strings - the array of strings to add
   */
  addAll(strings) {
    for (let string of strings) {
      this.add(string);
    }
  }

  /**
   * Returns a minimal DFA representing the strings in the trie.
   * @return {State} - the starting state of the minimal DFA
   */
  minimize() {
    return minimize(this.root);
  }

  /**
   * Returns a regex pattern that matches the strings in the trie.
   * @param {string} flags - The flags to add to the regex.
   * @return {string} pattern - The regex pattern.
   */
  toString(flags) {
    return toRegex(this.minimize(), flags);
  }

  /**
   * Returns a regex that matches the strings in the trie.
   * @param {string} flags - The flags to add to the regex.
   * @return {RegExp}
   */
  toRegExp(flags) {
    return new RegExp(this.toString(flags), flags);
  }
}

module.exports = Trie;

```

### File: test\test.js
```js
const assert = require('assert');
const regexgen = require('../');

describe('regexgen', function () {
  it('should generate a char class', function () {
    assert.deepEqual(regexgen(['a', 'b', 'c']), /[a-c]/);
  });

  it('should generate an alternation', function () {
    assert.deepEqual(regexgen(['abc', '123']), /123|abc/);
  });

  it('should extract common prefixes at the start', function () {
    assert.deepEqual(regexgen(['foobar', 'foozap']), /foo(?:zap|bar)/);
  });

  it('should extract common prefixes at the end', function () {
    assert.deepEqual(regexgen(['barfoo', 'zapfoo']), /(?:zap|bar)foo/);
  });

  it('should extract common prefixes at the start and end', function () {
    assert.deepEqual(regexgen(['foobarfoo', 'foozapfoo']), /foo(?:zap|bar)foo/);
  });

  it('should generate an optional group', function () {
    assert.deepEqual(regexgen(['foo', 'foobar']), /foo(?:bar)?/);
  });

  it('should generate multiple optional groups', function () {
    assert.deepEqual(regexgen(['f', 'fo', 'fox']), /f(?:ox?)?/);
  });

  it('should escape meta characters', function () {
    assert.deepEqual(regexgen(['foo|bar[test]+']), /foo\|bar\[test\]\+/);
    assert.deepEqual(regexgen(['u{}\\iu']), /u\{\}\\iu/);
  });

  it('should escape non-ascii characters', function () {
    assert.deepEqual(regexgen(['🎉']), /\uD83C\uDF89/);
  });

  it('should support regex flags', function () {
    assert.deepEqual(regexgen(['a', 'b', 'c'], 'g'), /[a-c]/g);
  });

  it('should support using the Trie class directly', function () {
    let t = new regexgen.Trie;
    t.add('foobar');
    t.add('foobaz');

    assert.deepEqual(t.toString(), 'fooba[rz]');
    assert.deepEqual(t.toRegExp(), /fooba[rz]/);

    let t2 = new regexgen.Trie;
    t2.addAll(['foobar', 'foobaz']);

    assert.deepEqual(t2.toString(), 'fooba[rz]');
    assert.deepEqual(t2.toRegExp(), /fooba[rz]/);
  });

  it('should work with optional groups', function () {
    assert.deepEqual(regexgen(['a', 'abc']), /a(?:bc)?/);
  });

  it('should wrap optional character classes in parens if they contain non-BMP codepoints', function () {
    assert.deepEqual(regexgen(['\u261D', '\u261D\u{1f3fb}', '\u261D\u{1f3fc}']), /\u261D(?:\uD83C[\uDFFB\uDFFC])?/);
  });

  it('should wrap optional literals in parens if they contain more than one code unit', function () {
    assert.deepEqual(regexgen(['\u261D', '\u261D\u{1f3fb}']), /\u261D(?:\uD83C\uDFFB)?/);
  });

  it('should retain non-BMP codepoints when the Unicode flag is passed', function () {
    assert.deepEqual(regexgen(['\u261D', '\u261D\u{1f3fb}'], 'u'), /\u261D\u{1F3FB}?/u);
    assert.deepEqual(
      regexgen(['\u{1F3F4}', '\u{1F3F4}\u{E0067}\u{E0062}\u{E0065}\u{E006E}\u{E0067}', '\u{1F3F4}\u{E0067}\u{E0062}\u{E0077}\u{E006C}\u{E0073}', '\u{1F3F4}\u{E0067}\u{E0062}\u{E0073}\u{E0063}\u{E0074}'], 'u'),
      /\u{1F3F4}(?:\u{E0067}\u{E0062}(?:\u{E0073}\u{E0063}\u{E0074}|\u{E0077}\u{E006C}\u{E0073}|\u{E0065}\u{E006E}\u{E0067}))?/u
    );
  });

  it('should handle non-BMP codepoint ranges correctly', function() {
    assert.deepEqual(
      regexgen(['\u{1F311}', '\u{1F312}', '\u{1F313}', '\u{1F314}', '\u{1F315}', '\u{1F316}', '\u{1F317}', '\u{1F318}'], 'u'),
      /[\u{1F311}-\u{1F318}]/u
    );
  });

  it('should correctly extract common prefix from multiple alternations', function () {
    assert.deepEqual(regexgen(['abjv', 'abxcjv', 'abydjv', 'abzejv']), /ab(?:ze|yd|xc)?jv/);
  });

  it('should sort alternation options correctly (#10)', function () {
    let s = '\uD83C\uDFCA\uD83C\uDFFD\u200D\u2640\uFE0F';
    let r = regexgen([
      '\uD83C\uDDF7\uD83C\uDDFC',
      '\uD83C\uDDF8\uD83C\uDDE6',
      '\uD83C\uDFCA\uD83C\uDFFD',
      s
    ]);

    assert.deepEqual(s.match(r)[0], s);
  });

  it('should sort non-BMP alternation options correctly', function () {
    let r = regexgen(
      [
        // shrug emoji
        '\u{1F937}\u200D',
        // shrug emoji with fitzpatrick modifiers
        '\u{1F937}\u{1F3FB}\u200D',
        '\u{1F937}\u{1F3FC}\u200D',
        '\u{1F937}\u{1F3FD}\u200D',
        '\u{1F937}\u{1F3FE}\u200D',
        '\u{1F937}\u{1F3FF}\u200D',
        // shrug emoji with gender modifier
        '\u{1F937}\u200D\u2640\uFE0F',
        // shrug emoji with gender and fitzpatrick modifiers
        '\u{1F937}\u{1F3FB}\u200D\u2640\uFE0F',
        '\u{1F937}\u{1F3FC}\u200D\u2640\uFE0F',
        '\u{1F937}\u{1F3FD}\u200D\u2640\uFE0F',
        '\u{1F937}\u{1F3FE}\u200D\u2640\uFE0F',
        '\u{1F937}\u{1F3FF}\u200D\u2640\uFE0F'
      ],
      'u'
    );

    assert.deepEqual(r, /\u{1F937}[\u{1F3FB}-\u{1F3FF}]?\u200D(?:\u2640\uFE0F)?/u);
    assert.deepEqual('\u{1F937}\u{1F3FB}\u200D\u2640\uFE0F'.match(r)[0], '\u{1F937}\u{1F3FB}\u200D\u2640\uFE0F');
  });

  it('should sort alternations of alternations correctly', function () {
    let r = regexgen(['aef', 'aghz', 'ayz', 'abcdz', 'abcd']);
    let s = 'abcdz';

    assert.deepEqual(s.match(r)[0], s);
    assert.deepEqual(r, /a(?:(?:bcd|gh|y)z|bcd|ef)/);
  });
});

```

