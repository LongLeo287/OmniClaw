---
id: wtfjs
type: knowledge
owner: OA_Triage
---
# wtfjs
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "wtfjs",
  "version": "1.22.8",
  "description": "A list of funny and tricky JavaScript examples",
  "bin": {
    "wtfjs": "wtfjs.js"
  },
  "scripts": {
    "toc": "npx doctoc --github --title '# Table of Contents' --maxlevel 2 README*.md",
    "format": "prettier --write .",
    "test": "prettier --check .",
    "release": "npx semantic-release",
    "prepare": "husky install"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/denysdovhan/wtfjs.git"
  },
  "keywords": [
    "javascript",
    "specification",
    "notes",
    "wtf",
    "learning",
    "guide",
    "handbook"
  ],
  "author": "Denys Dovhan <denysdovhan@gmail.com> (http://denysdovhan.com)",
  "license": "WTFPL 2.0",
  "bugs": {
    "url": "https://github.com/denysdovhan/wtfjs/issues"
  },
  "homepage": "https://github.com/denysdovhan/wtfjs#readme",
  "devDependencies": {
    "@semantic-release/git": "^10.0.1",
    "doctoc": "^2.1.0",
    "husky": "^8.0.1",
    "lint-staged": "^13.0.0",
    "prettier": "^2.6.2",
    "semantic-release": "^19.0.2"
  },
  "dependencies": {
    "boxen": "^7.0.0",
    "chalk": "^5.0.1",
    "default-pager": "^1.1.0",
    "meow": "^10.1.4",
    "msee": "^0.3.3",
    "through2": "^4.0.2",
    "update-notifier": "^6.0.2"
  },
  "lint-staged": {
    "README*.md": [
      "npm run toc",
      "prettier --write --ignore-unknown"
    ],
    "**/*": "prettier --write --ignore-unknown"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "prettier": {
    "embeddedLanguageFormatting": "off"
  },
  "release": {
    "plugins": [
      "@semantic-release/commit-analyzer",
      "@semantic-release/release-notes-generator",
      "@semantic-release/npm",
      "@semantic-release/github",
      [
        "@semantic-release/git",
        {
          "assets": [
            "README*.md",
            "*.js",
            "package.json",
            "package-lock.json"
          ]
        }
      ]
    ]
  }
}

```

### File: README.md
```md
[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua/)

# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]
[![Patreon][patreon-image]][patreon-url]
[![Buy Me A Coffee][bmc-image]][bmc-url]

> A list of funny and tricky JavaScript examples

JavaScript is a great language. It has a simple syntax, large ecosystem and, what is most important, a great community.

At the same time, we all know that JavaScript is quite a funny language with tricky parts. Some of them can quickly turn our everyday job into hell, and some of them can make us laugh out loud.

The original idea for WTFJS belongs to [Brian Leroux](https://twitter.com/brianleroux). This list is highly inspired by his talk [**“WTFJS”** at dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# Node Packaged Manuscript

You can install this handbook using `npm`. Just run:

```
$ npm install -g wtfjs
```

You should be able to run `wtfjs` at the command line now. This will open the manual in your selected `$PAGER`. Otherwise, you may continue reading on here.

The source is available here: <https://github.com/denysdovhan/wtfjs>

# Translations

Currently, there are these translations of **wtfjs**:

- [中文](./README-zh-cn.md)
- [हिंदी](./README-hi.md)
- [Français](./README-fr-fr.md)
- [Português do Brasil](./README-pt-br.md)
- [Polski](./README-pl-pl.md)
- [Italiano](./README-it-it.md)
- [한국어](./README-kr.md)

[**Help translating to your language**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/blob/master/CONTRIBUTING.md#translations

**Note:** Translations are maintained by their translators. They may not contain every example, and existing examples may be outdated.

<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [💪🏻 Motivation](#-motivation)
- [✍🏻 Notation](#-notation)
- [👀 Examples](#-examples)
  - [`[]` is equal `![]`](#-is-equal-)
  - [`true` is not equal `![]`, but not equal `[]` too](#true-is-not-equal--but-not-equal--too)
  - [true is false](#true-is-false)
  - [baNaNa](#banana)
  - [`NaN` is not a `NaN`](#nan-is-not-a-nan)
  - [`Object.is()` and `===` weird cases](#objectis-and--weird-cases)
  - [It's a fail](#its-a-fail)
  - [`[]` is truthy, but not `true`](#-is-truthy-but-not-true)
  - [`null` is falsy, but not `false`](#null-is-falsy-but-not-false)
  - [`document.all` is an object, but it is undefined](#documentall-is-an-object-but-it-is-undefined)
  - [Minimal value is greater than zero](#minimal-value-is-greater-than-zero)
  - [function is not a function](#function-is-not-a-function)
  - [Adding arrays](#adding-arrays)
  - [Trailing commas in array](#trailing-commas-in-array)
  - [Array equality is a monster](#array-equality-is-a-monster)
  - [`undefined` and `Number`](#undefined-and-number)
  - [`parseInt` is a bad guy](#parseint-is-a-bad-guy)
  - [Math with `true` and `false`](#math-with-true-and-false)
  - [HTML comments are valid in JavaScript](#html-comments-are-valid-in-javascript)
  - [`NaN` is ~~not~~ a number](#nan-is-not-a-number)
  - [`[]` and `null` are objects](#-and-null-are-objects)
  - [Magically increasing numbers](#magically-increasing-numbers)
  - [Precision of `0.1 + 0.2`](#precision-of-01--02)
  - [Patching numbers](#patching-numbers)
  - [Comparison of three numbers](#comparison-of-three-numbers)
  - [Funny math](#funny-math)
  - [Addition of RegExps](#addition-of-regexps)
  - [Strings aren't instances of `String`](#strings-arent-instances-of-string)
  - [Calling functions with backticks](#calling-functions-with-backticks)
  - [Call call call](#call-call-call)
  - [A `constructor` property](#a-constructor-property)
  - [Object as a key of object's property](#object-as-a-key-of-objects-property)
  - [Accessing prototypes with `__proto__`](#accessing-prototypes-with-__proto__)
  - [`` `${{Object}}` ``](#-object-)
  - [Destructuring with default values](#destructuring-with-default-values)
  - [Dots and spreading](#dots-and-spreading)
  - [Labels](#labels)
  - [Nested labels](#nested-labels)
  - [Insidious `try..catch`](#insidious-trycatch)
  - [Is this multiple inheritance?](#is-this-multiple-inheritance)
  - [A generator which yields itself](#a-generator-which-yields-itself)
  - [A class of class](#a-class-of-class)
  - [Non-coercible objects](#non-coercible-objects)
  - [Tricky arrow functions](#tricky-arrow-functions)
  - [Arrow functions can not be a constructor](#arrow-functions-can-not-be-a-constructor)
  - [`arguments` and arrow functions](#arguments-and-arrow-functions)
  - [Tricky return](#tricky-return)
  - [Chaining assignments on object](#chaining-assignments-on-object)
  - [Accessing object properties with arrays](#accessing-object-properties-with-arrays)
  - [`Number.toFixed()` display different numbers](#numbertofixed-display-different-numbers)
  - [`Math.max()` less than `Math.min()`](#mathmax-less-than-mathmin)
  - [Comparing `null` to `0`](#comparing-null-to-0)
  - [Same variable redeclaration](#same-variable-redeclaration)
  - [Default behavior Array.prototype.sort()](#default-behavior-arrayprototypesort)
  - [resolve() won't return Promise instance](#resolve-wont-return-promise-instance)
  - [`{}{}` is undefined](#-is-undefined)
  - [`arguments` binding](#arguments-binding)
  - [An `alert` from hell](#an-alert-from-hell)
  - [An infinite timeout](#an-infinite-timeout)
  - [A `setTimeout` object](#a-settimeout-object)
  - [Double dot](#double-dot)
  - [Extra Newness](#extra-newness)
  - [Why you should use semicolons](#why-you-should-use-semicolons)
  - [Split a string by a space](#split-a-string-by-a-space)
  - [A stringified string](#a-stringified-string)
  - [Non-strict comparison of a number to `true`](#non-strict-comparison-of-a-number-to-true)
- [📚 Other resources](#-other-resources)
- [🤝 Supporting](#-supporting)
- [🎓 License](#-license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->

# 💪🏻 Motivation

> Just for fun
>
> &mdash; _[**“Just for Fun: The Story of an Accidental Revolutionary”**](https://en.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

The primary goal of this list is to collect some crazy examples and explain how they work, if possible. Just because it's fun to learn something that we didn't know before.

If you are a beginner, you can use these notes to get a deeper dive into JavaScript. I hope these notes will motivate you to spend more time reading the specification.

If you are a professional developer, you can consider these examples as a great reference for all of the quirks and unexpected edges of our beloved JavaScript.

In any case, just read this. You're probably going to find something new.

> **⚠️ Note:** If you enjoy reading this document, please, [consider supporting the author of this collection](#-supporting).

# ✍🏻 Notation

**`// ->`** is used to show the result of an expression. For example:

```js
1 + 1; // -> 2
```

**`// >`** means the result of `console.log` or another output. For example:

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** is just a comment used for explanations. Example:

```js
// Assigning a function to foo constant
const foo = function() {};
```

# 👀 Examples

## `[]` is equal `![]`

Array is equal not array:

```js
[] == ![]; // -> true
```

### 💡 Explanation:

The abstract equality operator converts both sides to numbers to compare them, and both sides become the number `0` for different reasons. Arrays are truthy, so on the right, the opposite of a truthy value is `false`, which is then coerced to `0`. On the left, however, an empty array is coerced to a number without becoming a boolean first, and empty arrays are coerced to `0`, despite being truthy.

Here is how this expression simplifies:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

See also [`[]` is truthy, but not `true`](#-is-truthy-but-not-true).

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

## `true` is not equal `![]`, but not equal `[]` too

Array is not equal `true`, but not Array is not equal `true` too;
Array is equal `false`, not Array is equal `false` too:

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 Explanation:

```js
true == []; // -> false
true == ![]; // -> false

// According to the specification

true == []; // -> false

toNumber(true); // -> 1
toNumber([]); // -> 0

1 == 0; // -> false

true == ![]; // -> false

![]; // -> false

true == false; // -> false
```

```js
false == []; // -> true
false == ![]; // -> true

// According to the specification

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> true

![]; // -> false

false == false; // -> true
```

- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

## true is false

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 Explanation:

Consider this step-by-step:

```js
// true is 'truthy' and represented by value 1 (number), 'true' in string form is NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' is not the empty string, so it's a truthy value
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

This is an old-school joke in JavaScript, but remastered. Here's the original one:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 Explanation:

The expression is evaluated as `'foo' + (+'bar')`, which converts `'bar'` to not a number.

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 Unary + Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` is not a `NaN`

```js
NaN === NaN; // -> false
```

### 💡 Explanation:

The specification strictly defines the logic behind this behavior:

> 1. If `Type(x)` is different from `Type(y)`, return **false**.
> 2. If `Type(x)` is Number, then
>    1. If `x` is **NaN**, return **false**.
>    2. If `y` is **NaN**, return **false**.
>    3. … … …
>
> &mdash; [**7.2.14** Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

Following the definition of `NaN` from the IEEE:

> Four mutually exclusive relations are possible: less than, equal, greater than, and unordered. The last case arises when at least one operand is NaN. Every NaN shall compare unordered with everything, including itself.
>
> &mdash; [“What is the rationale for all comparisons returning false for IEEE754 NaN values?”](https://stackoverflow.com/questions/1565164/1573715#1573715) at StackOverflow

## `Object.is()` and `===` weird cases

`Object.is()` determines if two values have the same value or not. It works similar to the `===` operator but there are a few weird cases:

```javascript
Object.is(NaN, NaN); // -> true
NaN === NaN; // -> false

Object.is(-0, 0); // -> false
-0 === 0; // -> true

Object.is(NaN, 0 / 0); // -> true
NaN === 0 / 0; // -> false
```

### 💡 Explanation:

In JavaScript lingo, `NaN` and `NaN` are the same value but they're not strictly equal. `NaN === NaN` being false is apparently due to historical reasons so it would probably be better to accept it as it is.

Similarly, `-0` and `0` are strictly equal, but they're not the same value.

For more details about `NaN === NaN`, see the above case.

- [Here are the TC39 specs about Object.is](https://tc39.es/ecma262/#sec-object.is)
- [Equality comparisons and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) on MDN

## It's a fail

You would not believe, but …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 Explanation:

By breaking that mass of symbols into pieces, we notice that the following pattern occurs often:

```js
![] + []; // -> 'false'
![]; // -> false
```

So we try adding `[]` to `false`. But due to a number of internal function calls (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`) we end up converting the right operand to a string:

```js
![] + [].toString(); // 'false'
```

Thinking of a string as an array we can access its first character via `[0]`:

```js
"false"[0]; // -> 'f'
```

The rest is obvious, but the `i` is tricky. The `i` in `fail` is grabbed by generating the string `'falseundefined'` and grabbing the element on index `['10']`.

More examples:

```js
+![]          // -> 0
+!![]         // -> 1
!![]          // -> true
![]           // -> false
[][[]]        // -> undefined
+!![] / +![]  // -> Infinity
[] + {}       // -> "[object Object]"
+{}           // -> NaN
```

- [Brainfuck beware: JavaScript is after you!](http://patriciopalladino.com/blog/2012/08/09/non-alphanumeric-javascript.html)
- [Writing a sentence without using the Alphabet](https://bluewings.github.io/en/writing-a-sentence-without-using-the-alphabet/#weird-javascript-generator) — generate any phrase using JavaScript

## `[]` is truthy, but not `true`

An array is a truthy value, however, it's not equal to `true`.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 Explanation:

Here are links to the corresponding sections in the ECMA-262 specification:

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

## `null` is falsy, but not `false`

Despite the fact that `null` is a falsy value, it's not equal to `false`.

```js
!!null; // -> false
null == false; // -> false
```

At the same time, other falsy values, like `0` or `''` are equal to `false`.

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 Explanation:

The explanation is the same as for previous example. Here's the corresponding link:

- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

## `document.all` is an object, but it is undefined

> ⚠️ This is part of the Browser API and won't work in a Node.js environment ⚠️

Despit
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing Guidelines

This guide will help you to contribute to this project smoothly. Please, read carefully to make your contribution process easier.

Usually, this project has two types of contributions: _new examples_ and _translations_.

## New Examples

**New examples will be accepted only if they have an explanation.** Preferably, the explanation should contain links to the specification, blog posts, forum publications.

If you don't know why an example works the way it works, ask for help on [the discussion forum](https://github.com/denysdovhan/wtfjs/discussions).

Issues without explanations will be closed.

## Translations

**If you want a translation, please, make one.** Issues with translation requests will be closed in favor of PRs.

Before sending a PR with translation, please check if there are any existing PRs with translation to your language.

**You have to find someone who speaks your language natively to read, check and verify your translation.** That's how we are trying to prevent typos and mistakes.

---

Thanks for understanding, have fun!

```

### File: README-fr-fr.md
```md
# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> Une liste d'exemples JavaScript drôles et délicats

Le JavaScript est un langage formidable! Il possède une syntaxe simple, un grand écosystème et, le plus important de tout, une immense communauté.

En même temps, nous savons tous que le JavaScript est un langage assez amusant comprenant des aspects plus complexes que d'autres. Certains d'entre eux peuvent rapidement faire de notre travail quotidien un enfer, tout comme d'autres peuvent nous faire rire aux éclats.

L'idée originale de WTFJS appartient à [Brian Leroux](https://twitter.com/brianleroux). Cette liste est fortement inspirée par son discours [**“WTFJS”** at dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# Le Manuscript sous forme de paquet Node

Vous pouvez installer ce manuel en utilisant `npm`. Pour cela, il suffit d'exécuter :

```
$ npm install -g wtfjs
```

Vous devriez pouvoir ensuite utiliser `wtfjs` en ligne de commande. Cela ouvrira le manuel dans votre terminal. Sinon, vous pouvez continuer à lire ici tout simplement.

La source du _package_ est disponible ici: <https://github.com/denysdovhan/wtfjs>

# Traductions

Actuellement, il existe des traductions de ** wtfjs ** pour les langues suivantes :

- [中文版](./README-zh-cn.md)
- [Français](./README-fr-fr.md)

[**Demander une autre traduction**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D

<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [💪🏻 Motivation](#-motivation)
- [✍🏻 Notation](#-notation)
- [👀 Exemples](#-exemples)
  - [`[]` est égal à `![]`](#-est-%C3%A9gal-%C3%A0-)
  - [`true` n'est pas égal à `![]`, mais pas égal à `[]` aussi](#true-nest-pas-%C3%A9gal-%C3%A0--mais-pas-%C3%A9gal-%C3%A0--aussi)
  - [true est faux](#true-est-faux)
  - [baNaNa](#banana)
  - [`NaN` n'est pas un `NaN`](#nan-nest-pas-un-nan)
  - [C'est un échec](#cest-un-%C3%A9chec)
  - [`[]` est truthy, mais pas `true`](#-est-truthy-mais-pas-true)
  - [`null` est falsy, mais pas `faux`](#null-est-falsy-mais-pas-faux)
  - [`document.all` est un objet, mais il est `undefined`](#documentall-est-un-objet-mais-il-est-undefined)
  - [La valeur minimale est supérieure à zéro](#la-valeur-minimale-est-sup%C3%A9rieure-%C3%A0-z%C3%A9ro)
  - [Fonction n'est pas une fonction](#fonction-nest-pas-une-fonction)
  - [Ajout de tableaux](#ajout-de-tableaux)
  - [Les virgules finales dans un tableau](#les-virgules-finales-dans-un-tableau)
  - [L'égalité des tableaux est un monstre](#l%C3%A9galit%C3%A9-des-tableaux-est-un-monstre)
  - [`undefined` et `Number`](#undefined-et-number)
  - [`parseInt` est un méchant](#parseint-est-un-m%C3%A9chant)
  - [Math avec `true` et `false`](#math-avec-true-et-false)
  - [Les commentaires HTML sont valides en JavaScript](#les-commentaires-html-sont-valides-en-javascript)
  - [`NaN` n'est ~~pas~~ un nombre](#nan-nest-pas-un-nombre)
  - [`[]` et `null` sont des objets](#-et-null-sont-des-objets)
  - [Nombres magiquement croissant](#nombres-magiquement-croissant)
  - [Précision de `0.1 + 0.2`](#pr%C3%A9cision-de-01--02)
  - [Patching de numéros](#patching-de-num%C3%A9ros)
  - [Comparaison de trois nombres](#comparaison-de-trois-nombres)
  - [Math drôle](#math-dr%C3%B4le)
  - [Addition de RegExps](#addition-de-regexps)
  - [Les chaînes ne sont pas des instances de `String`](#les-cha%C3%AEnes-ne-sont-pas-des-instances-de-string)
  - [Appeler des fonctions avec des caractères accent grave](#appeler-des-fonctions-avec-des-caract%C3%A8res-accent-grave)
  - [Call call call](#call-call-call)
  - [Une propriété `constructor`](#une-propri%C3%A9t%C3%A9-constructor)
  - [Object en tant que clé de la propriété d'un objet](#object-en-tant-que-cl%C3%A9-de-la-propri%C3%A9t%C3%A9-dun-objet)
  - [Accéder aux prototypes avec `__proto__`](#acc%C3%A9der-aux-prototypes-avec-__proto__)
  - [`` `${{Object}}` ``](#-object-)
  - [Déstructuration avec des valeurs par défaut](#d%C3%A9structuration-avec-des-valeurs-par-d%C3%A9faut)
  - [Points et propagation](#points-et-propagation)
  - [Étiquettes](#%C3%A9tiquettes)
  - [Étiquettes imbriquées](#%C3%A9tiquettes-imbriqu%C3%A9es)
  - [`Try...catch` insidieux](#trycatch-insidieux)
  - [Est-ce un héritage multiple ?](#est-ce-un-h%C3%A9ritage-multiple-)
  - [Un générateur qui se `yield` lui-même](#un-g%C3%A9n%C3%A9rateur-qui-se-yield-lui-m%C3%AAme)
  - [Une classe de classe](#une-classe-de-classe)
  - [Objets incoercibles](#objets-incoercibles)
  - [Fonctions fléchées complexes](#fonctions-fl%C3%A9ch%C3%A9es-complexes)
  - [Les fonctions fléchées ne peuvent pas être un constructeur](#les-fonctions-fl%C3%A9ch%C3%A9es-ne-peuvent-pas-%C3%AAtre-un-constructeur)
  - [`arguments` et fonctions fléchées](#arguments-et-fonctions-fl%C3%A9ch%C3%A9es)
  - [Retour difficile](#retour-difficile)
  - [Chaînage d'affectations sur un objet](#cha%C3%AEnage-daffectations-sur-un-objet)
  - [Accéder aux propriétés d'un objet avec des tableaux](#acc%C3%A9der-aux-propri%C3%A9t%C3%A9s-dun-objet-avec-des-tableaux)
  - [Opérateurs `null` et relationnels](#op%C3%A9rateurs-null-et-relationnels)
  - [`Number.toFixed()` affiche différents nombres](#numbertofixed-affiche-diff%C3%A9rents-nombres)
  - [`Math.max()` est moins que `Math.min()`](#mathmax-est-moins-que-mathmin)
  - [Comparer `null` à `0`](#comparer-null-%C3%A0-0)
  - [Même redéclaration d'une variable](#m%C3%AAme-red%C3%A9claration-dune-variable)
  - [Comportement par défaut d'`Array.prototype.sort()`](#comportement-par-d%C3%A9faut-darrayprototypesort)
- [📚 Autres ressources](#-autres-ressources)
- [🎓 Licence](#-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->

# 💪🏻 Motivation

> Juste pour le fun
>
> &mdash; _[**“Just for Fun: The Story of an Accidental Revolutionary”**](https://archive.org/details/justforfun00linu), Linus Torvalds_

L'objectif principal de cette liste est de rassembler quelques exemples loufoques et d'expliquer leur fonctionnement, quand c'est possible. 😉 Tout simplement parce qu'il est amusant d'apprendre quelque chose qu'on ne connaissait pas auparavant.

Si vous êtes débutant, vous pouvez aussi utiliser ces notes pour approfondir vos connaissances en JavaScript. J'espère qu'elles vous inciteront à passer plus de temps à lire la spécification.

Si vous êtes un développeur professionnel, vous pouvez considérer ces exemples comme une excellente référence pour toutes les bizarreries et comportements inattendus de notre langage bien-aimé, le JavaScript.

Dans tous les cas, lisez ce qui suit. Vous y trouverez probablement quelque chose de nouveau !

# ✍🏻 Notation

**`// ->`** est utilisé pour afficher le résultat d'une expression. Par exemple :

```js
1 + 1; // -> 2
```

**`// >`** définit le résultat de `console.log` ou tout autre sortie. Par exemple :

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** indique un commentaire utilisé pour donner des explications. Par exemple :

```js
// Assigner une fonction la constant foo
const foo = function() {};
```

# 👀 Exemples

## `[]` est égal à `![]`

Tableau est égal à pas tableau

```js
[] == ![]; // -> true
```

### 💡 Explication :

L'opérateur de comparaison d'égalité faible convertit les deux côtés en nombres pour les comparer. Pour différentes raisons, les deux côtés deviennent le nombre `0`.

Les tableaux sont truthy, donc à droite, on trouve l'opposé d'une valeur truthy, soit `false`, qui est ensuite forcé à `0`. A gauche, puisqu'un tableau vide est forcé à `0` automatiquement, sans devoir être précédemment transformé en booléen, on trouve aussi `0`, malgré le fait qu'un tableau soit truthy.

Voici comment cette expression se simplifie:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

Voir aussi [`[]` est truthy, mais pas `true`](#-est-truthy-mais-pas-true).

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true` n'est pas égal à `![]`, mais pas égal à `[]` aussi

Un tableau n'est pas égal à `true`, tout comme pas tableau. Un tableau est égal à `false`, pas tableau est égal à `false` aussi :

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 Explication :

```js
true == []; // -> false
true == ![]; // -> false

// Selon la spécification

true == []; // -> false

toNumber(true); // -> 1
toNumber([]); // -> 0

1 == 0; // -> false

true == ![]; // -> false

![]; // -> false

true == false; // -> false
```

```js
false == []; // -> true
false == ![]; // -> true

// Selon la spécification

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> false

![]; // -> false

false == false; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## true est faux

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 Explication :

Considérez ceci étape par étape :

```js
// `true` est 'truthy' et est représenté par la valeur 1 (nombre), 'true' sous forme de chaîne est NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' n'est pas une chaîne vide, donc c'est une valeur `truthy`
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

Ceci est une blague "old school" en JavaScript, mais remasterisée. Voici l'originale :

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 Explication :

L'expression est évaluée comme `'foo' + (+'bar')`, ce qui convertit `'bar'` à `NaN`.

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 Unary + Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` n'est pas un `NaN`

```js
NaN === NaN; // -> false
```

### 💡 Explication :

La spécification définit strictement la logique derrière ce comportement :

> 1. Si `Type(x)` est différent de `Type(y)`, retourne **false**.
> 2. Si `Type(x)` est `Number`, alors
>    1. Si `x` est **NaN**, retourne **false**.
>    2. Si `y` est **NaN**, retourne **false**.
>    3. … … …
>
> &mdash; [**7.2.14** Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

Sur la base de la définition de `NaN` de l'IEEE :

> Quatre relations mutuellement exclusives sont possibles : inférieur à, égal, supérieur à, et non ordonné. Le dernier cas survient quand au moins un opérande est `NaN`. Tous les `NaN` doivent se comparer de manière non ordonnée avec tout, y compris avec lui-même.
>
> &mdash; [“What is the rationale for all comparisons returning false for IEEE754 NaN values?”](https://stackoverflow.com/questions/1565164/1573715#1573715) sur StackOverflow.

## C'est un échec

Vous ne le croiriez pas, mais …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 Explication :

En brisant cette masse de symboles en morceaux, nous remarquons que le schéma suivant se produit souvent :

```js
![] + []; // -> 'false'
![]; // -> false
```

Donc, nous essayons d'ajouter `[]` à `false`, mais en raison d'un certain nombre d'appels de fonctions internes (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`), nous finissons par convertir l'opérande de droite en chaîne :

```js
![] + [].toString(); // 'false'
```

En considérant une chaîne comme un tableau, nous pouvons accéder à son premier caractère via `[0]` :

```js
"false"[0]; // -> 'f'
```

Le reste est évident, sauf pour le `i`. Le `i` dans `fail` est saisi en générant la chaîne `"falseundefined"` et en saisissant l'éléments sur l'index `[10]`.

## `[]` est truthy, mais pas `true`

Un tableau est une valeur `truthy`, mais n'est pas égal à `true`.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 Explication :

Voici des liens vers les sections correspondantes de la spécification ECMA-262 :

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` est falsy, mais pas `faux`

Malgré le fait que `null` soit une valeur `falsy`, elle n'est pas égale à `false`.

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 Explication :

L'explication est la même que pour l'exemple précédent. Voici le lien correspondant :

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` est un objet, mais il est `undefined`

> ⚠️ Ceci fait partie de la Browser API et ne fonctionnera pas dans un environnement Node.js ⚠️

Malgré le fait que `document.all` soit un objet de type tableau et qu'il donne accès aux nœuds DOM de la page, il répond à la fonction `typeof` comme étant `undefined`.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

En même temps, `document.all` n'est pas égal à `undefined`.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

Mais, parallèlement :

```js
document.all == null; // -> true
```

### 💡 Explication :

> `document.all` était anciennement un moyen d'accéder aux éléments DOM, principalement avec les anciennes versions d'IE. Bien que cela n'ait jamais été une norme, `document.all` était largement utilisé dans "l'ancien code JS". Quand la norme a progressé avec la venue de nouvelles API (par exemple, `document.getElementById`), l'API `document.all` est devenue obsolète et le comité de normes a dû décider ce qu'ils allaient en faire. En raison de sa large utilisation, ils ont décidé de la conserver, mais d'introduire une violation volontaire de la spécification JavaScript.
> La raison pour laquelle `document.all` retourne `false` lors de l'utilisation de l'opérateur d'égalité stricte ([Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)) avec `undefined` et `true` lors de l'utilisation de l'opérateur d'égalité abstraite ([Abstract Equality Comparison](https://www.ecma-international.
... [TRUNCATED]
```

### File: README-hi.md
```md
# f\*ck जावास्क्रिप्ट क्या है

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> मजाकिया और मुश्किल जावास्क्रिप्ट उदाहरणों की एक सूची

जावास्क्रिप्ट एक महान भाषा है। इसका एक सरल वाक्यविन्यास है, एक बड़ा पारिस्थितिकी तंत्र, और, जो सबसे महत्वपूर्ण है, एक महान समुदाय।

उसी समय, हम सभी जानते हैं कि जावास्क्रिप्ट मुश्किल भागों के साथ काफी मज़ेदार भाषा है। उनमें से कुछ हमारी रोज़मर्रा की नौकरी को जल्दी से नरक में बदल सकते हैं, और उनमें से कुछ हमें ज़ोर से हँसा सकते हैं।

WTFJS के लिए मूल विचार है [Brian Leroux](https://twitter.com/brianleroux). यह सूची उनकी बातों से प्रेरित है [**“WTFJS”** at dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# Node पैकेज्ड पांडुलिपि

आप इस हैंडबुक को `npm` का उपयोग करके स्थापित कर सकते हैं। यहां जाओ:

```
$ npm install -g wtfjs
```

अब आपको कमांड लाइन पर `wtfjs` चलाने में सक्षम होना चाहिए। यह आपके चयनित `$ PAGER` में मैनुअल को खोलेगा। अन्यथा, आप यहां पढ़ना जारी रख सकते हैं।

स्रोत यहां उपलब्ध है: <https://github.com/denysdovhan/wtfjs>

# Translations

Currently, there are these translations of **wtfjs**:

- [中文版](./README-zh-cn.md)
- [हिन्दी](./README-hi.md)

[**एक और अनुवाद का अनुरोध करें**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

# Table of Contents

- [💪🏻 प्रेरणा](#-%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%B0%E0%A4%A3%E0%A4%BE)
- [✍🏻 नोटेशन](#-%E0%A4%A8%E0%A5%8B%E0%A4%9F%E0%A5%87%E0%A4%B6%E0%A4%A8)
- [👀 उदाहरण](#-%E0%A4%89%E0%A4%A6%E0%A4%BE%E0%A4%B9%E0%A4%B0%E0%A4%A3)
  - [`[]` के बराबर`![]`](#-%E0%A4%95%E0%A5%87-%E0%A4%AC%E0%A4%B0%E0%A4%BE%E0%A4%AC%E0%A4%B0)
  - [`true` is not equal `![]`, but not equal `[]` too](#true-is-not-equal--but-not-equal--too)
  - [true is false](#true-is-false)
  - [baNaNa](#banana)
  - [`NaN` is not a `NaN`](#nan-is-not-a-nan)
  - [यह विफल है](#%E0%A4%AF%E0%A4%B9-%E0%A4%B5%E0%A4%BF%E0%A4%AB%E0%A4%B2-%E0%A4%B9%E0%A5%88)
  - [`[]` is truthy, but not `true`](#-is-truthy-but-not-true)
  - [`null` is falsy, but not `false`](#null-is-falsy-but-not-false)
  - [`document.all` is an object, but it is undefined](#documentall-is-an-object-but-it-is-undefined)
  - [न्यूनतम मान शून्य से अधिक है](#%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE-%E0%A4%AE%E0%A4%BE%E0%A4%A8-%E0%A4%B6%E0%A5%82%E0%A4%A8%E0%A5%8D%E0%A4%AF-%E0%A4%B8%E0%A5%87-%E0%A4%85%E0%A4%A7%E0%A4%BF%E0%A4%95-%E0%A4%B9%E0%A5%88)
  - [फंक्शन कोई फंक्शन नहीं है](#%E0%A4%AB%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B6%E0%A4%A8-%E0%A4%95%E0%A5%8B%E0%A4%88-%E0%A4%AB%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B6%E0%A4%A8-%E0%A4%A8%E0%A4%B9%E0%A5%80%E0%A4%82-%E0%A4%B9%E0%A5%88)
  - [Adding arrays](#adding-arrays)
  - [सरणी में अल्पविराम](#%E0%A4%B8%E0%A4%B0%E0%A4%A3%E0%A5%80-%E0%A4%AE%E0%A5%87%E0%A4%82-%E0%A4%85%E0%A4%B2%E0%A5%8D%E0%A4%AA%E0%A4%B5%E0%A4%BF%E0%A4%B0%E0%A4%BE%E0%A4%AE)
  - [ऐरे समानता एक राक्षस है](#%E0%A4%90%E0%A4%B0%E0%A5%87-%E0%A4%B8%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A4%A4%E0%A4%BE-%E0%A4%8F%E0%A4%95-%E0%A4%B0%E0%A4%BE%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%B8-%E0%A4%B9%E0%A5%88)
  - [`undefined` and `Number`](#undefined-and-number)
  - [`parseInt` एक बुरा आदमी है](#parseint-%E0%A4%8F%E0%A4%95-%E0%A4%AC%E0%A5%81%E0%A4%B0%E0%A4%BE-%E0%A4%86%E0%A4%A6%E0%A4%AE%E0%A5%80-%E0%A4%B9%E0%A5%88)
  - [`सत्य` और` असत्य` के साथ गणित](#%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%AF-%E0%A4%94%E0%A4%B0-%E0%A4%85%E0%A4%B8%E0%A4%A4%E0%A5%8D%E0%A4%AF-%E0%A4%95%E0%A5%87-%E0%A4%B8%E0%A4%BE%E0%A4%A5-%E0%A4%97%E0%A4%A3%E0%A4%BF%E0%A4%A4)
  - [HTML टिप्पणियाँ जावास्क्रिप्ट में मान्य हैं](#html-%E0%A4%9F%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%AA%E0%A4%A3%E0%A4%BF%E0%A4%AF%E0%A4%BE%E0%A4%81-%E0%A4%9C%E0%A4%BE%E0%A4%B5%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%95%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AA%E0%A5%8D%E0%A4%9F-%E0%A4%AE%E0%A5%87%E0%A4%82-%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A5%8D%E0%A4%AF-%E0%A4%B9%E0%A5%88%E0%A4%82)
  - [`NaN` is ~~not~~ a number](#nan-is-not-a-number)
  - [`[]` and `null` are objects](#-and-null-are-objects)
  - [Magically increasing numbers](#magically-increasing-numbers)
  - [Precision of `0.1 + 0.2`](#precision-of-01--02)
  - [पैचिंग नंबर](#%E0%A4%AA%E0%A5%88%E0%A4%9A%E0%A4%BF%E0%A4%82%E0%A4%97-%E0%A4%A8%E0%A4%82%E0%A4%AC%E0%A4%B0)
  - [Comparison of three numbers](#comparison-of-three-numbers)
  - [मजेदार गणित](#%E0%A4%AE%E0%A4%9C%E0%A5%87%E0%A4%A6%E0%A4%BE%E0%A4%B0-%E0%A4%97%E0%A4%A3%E0%A4%BF%E0%A4%A4)
  - [RegExps का जोड़](#regexps-%E0%A4%95%E0%A4%BE-%E0%A4%9C%E0%A5%8B%E0%A4%A1%E0%A4%BC)
  - [स्ट्रिंग्स `स्ट्रिंग` के उदाहरण नहीं हैं](#%E0%A4%B8%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%82%E0%A4%97%E0%A5%8D%E0%A4%B8-%E0%A4%B8%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%82%E0%A4%97-%E0%A4%95%E0%A5%87-%E0%A4%89%E0%A4%A6%E0%A4%BE%E0%A4%B9%E0%A4%B0%E0%A4%A3-%E0%A4%A8%E0%A4%B9%E0%A5%80%E0%A4%82-%E0%A4%B9%E0%A5%88%E0%A4%82)
  - [बैकटिक्स के साथ कॉलिंग फ़ंक्शन](#%E0%A4%AC%E0%A5%88%E0%A4%95%E0%A4%9F%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B8-%E0%A4%95%E0%A5%87-%E0%A4%B8%E0%A4%BE%E0%A4%A5-%E0%A4%95%E0%A5%89%E0%A4%B2%E0%A4%BF%E0%A4%82%E0%A4%97-%E0%A4%AB%E0%A4%BC%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B6%E0%A4%A8)
  - [पुकार पुकार पुकार](#%E0%A4%AA%E0%A5%81%E0%A4%95%E0%A4%BE%E0%A4%B0-%E0%A4%AA%E0%A5%81%E0%A4%95%E0%A4%BE%E0%A4%B0-%E0%A4%AA%E0%A5%81%E0%A4%95%E0%A4%BE%E0%A4%B0)
  - [A `constructor` property](#a-constructor-property)
  - [वस्तु की संपत्ति की कुंजी के रूप में वस्तु](#%E0%A4%B5%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%81-%E0%A4%95%E0%A5%80-%E0%A4%B8%E0%A4%82%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%BF-%E0%A4%95%E0%A5%80-%E0%A4%95%E0%A5%81%E0%A4%82%E0%A4%9C%E0%A5%80-%E0%A4%95%E0%A5%87-%E0%A4%B0%E0%A5%82%E0%A4%AA-%E0%A4%AE%E0%A5%87%E0%A4%82-%E0%A4%B5%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%81)
  - [प्रोटोटाइपिंग को `__proto__` के साथ एक्सेस करना](#%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%9F%E0%A5%8B%E0%A4%9F%E0%A4%BE%E0%A4%87%E0%A4%AA%E0%A4%BF%E0%A4%82%E0%A4%97-%E0%A4%95%E0%A5%8B-__proto__-%E0%A4%95%E0%A5%87-%E0%A4%B8%E0%A4%BE%E0%A4%A5-%E0%A4%8F%E0%A4%95%E0%A5%8D%E0%A4%B8%E0%A5%87%E0%A4%B8-%E0%A4%95%E0%A4%B0%E0%A4%A8%E0%A4%BE)
  - [`` `$ {{वस्तु}}` ``](#--%E0%A4%B5%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%81-)
  - [डिफ़ॉल्ट मानों के साथ विनाशकारी](#%E0%A4%A1%E0%A4%BF%E0%A4%AB%E0%A4%BC%E0%A5%89%E0%A4%B2%E0%A5%8D%E0%A4%9F-%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A5%8B%E0%A4%82-%E0%A4%95%E0%A5%87-%E0%A4%B8%E0%A4%BE%E0%A4%A5-%E0%A4%B5%E0%A4%BF%E0%A4%A8%E0%A4%BE%E0%A4%B6%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%80)
  - [डॉट्स और फैल रहा है](#%E0%A4%A1%E0%A5%89%E0%A4%9F%E0%A5%8D%E0%A4%B8-%E0%A4%94%E0%A4%B0-%E0%A4%AB%E0%A5%88%E0%A4%B2-%E0%A4%B0%E0%A4%B9%E0%A4%BE-%E0%A4%B9%E0%A5%88)
  - [लेबल](#%E0%A4%B2%E0%A5%87%E0%A4%AC%E0%A4%B2)
  - [Nested labels](#nested-labels)
  - [कपटी `कोशिश..चेक`](#%E0%A4%95%E0%A4%AA%E0%A4%9F%E0%A5%80-%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A4%BF%E0%A4%B6%E0%A4%9A%E0%A5%87%E0%A4%95)
  - [क्या यह कई विरासत है?](#%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE-%E0%A4%AF%E0%A4%B9-%E0%A4%95%E0%A4%88-%E0%A4%B5%E0%A4%BF%E0%A4%B0%E0%A4%BE%E0%A4%B8%E0%A4%A4-%E0%A4%B9%E0%A5%88)
  - [एक जनरेटर जो खुद उपजता है](#%E0%A4%8F%E0%A4%95-%E0%A4%9C%E0%A4%A8%E0%A4%B0%E0%A5%87%E0%A4%9F%E0%A4%B0-%E0%A4%9C%E0%A5%8B-%E0%A4%96%E0%A5%81%E0%A4%A6-%E0%A4%89%E0%A4%AA%E0%A4%9C%E0%A4%A4%E0%A4%BE-%E0%A4%B9%E0%A5%88)
  - [कक्षा का एक वर्ग](#%E0%A4%95%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE-%E0%A4%95%E0%A4%BE-%E0%A4%8F%E0%A4%95-%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%97)
  - [गैर-सहकर्मी वस्तुएं](#%E0%A4%97%E0%A5%88%E0%A4%B0-%E0%A4%B8%E0%A4%B9%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A5%80-%E0%A4%B5%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%81%E0%A4%8F%E0%A4%82)
  - [मुश्किल तीर कार्य](#%E0%A4%AE%E0%A5%81%E0%A4%B6%E0%A5%8D%E0%A4%95%E0%A4%BF%E0%A4%B2-%E0%A4%A4%E0%A5%80%E0%A4%B0-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF)
  - [एरो फ़ंक्शंस एक निर्माता नहीं हो सकता है](#%E0%A4%8F%E0%A4%B0%E0%A5%8B-%E0%A4%AB%E0%A4%BC%E0%A4%82%E0%A4%95%E0%A5%8D%E0%A4%B6%E0%A4%82%E0%A4%B8-%E0%A4%8F%E0%A4%95-%E0%A4%A8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%AE%E0%A4%BE%E0%A4%A4%E0%A4%BE-%E0%A4%A8%E0%A4%B9%E0%A5%80%E0%A4%82-%E0%A4%B9%E0%A5%8B-%E0%A4%B8%E0%A4%95%E0%A4%A4%E0%A4%BE-%E0%A4%B9%E0%A5%88)
  - [`तर्क` और तीर कार्य](#%E0%A4%A4%E0%A4%B0%E0%A5%8D%E0%A4%95-%E0%A4%94%E0%A4%B0-%E0%A4%A4%E0%A5%80%E0%A4%B0-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF)
  - [मुश्किल वापसी](#%E0%A4%AE%E0%A5%81%E0%A4%B6%E0%A5%8D%E0%A4%95%E0%A4%BF%E0%A4%B2-%E0%A4%B5%E0%A4%BE%E0%A4%AA%E0%A4%B8%E0%A5%80)
  - [ऑब्जेक्ट पर कार्य असाइन करना](#%E0%A4%91%E0%A4%AC%E0%A5%8D%E0%A4%9C%E0%A5%87%E0%A4%95%E0%A5%8D%E0%A4%9F-%E0%A4%AA%E0%A4%B0-%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF-%E0%A4%85%E0%A4%B8%E0%A4%BE%E0%A4%87%E0%A4%A8-%E0%A4%95%E0%A4%B0%E0%A4%A8%E0%A4%BE)
  - [सरणियों के साथ ऑब्जेक्ट गुण तक पहुँचना](#%E0%A4%B8%E0%A4%B0%E0%A4%A3%E0%A4%BF%E0%A4%AF%E0%A5%8B%E0%A4%82-%E0%A4%95%E0%A5%87-%E0%A4%B8%E0%A4%BE%E0%A4%A5-%E0%A4%91%E0%A4%AC%E0%A5%8D%E0%A4%9C%E0%A5%87%E0%A4%95%E0%A5%8D%E0%A4%9F-%E0%A4%97%E0%A5%81%E0%A4%A3-%E0%A4%A4%E0%A4%95-%E0%A4%AA%E0%A4%B9%E0%A5%81%E0%A4%81%E0%A4%9A%E0%A4%A8%E0%A4%BE)
  - [Null and Relational Operators](#null-and-relational-operators)
  - [`Number.toFixed ()` विभिन्न संख्याएँ प्रदर्शित करता है](#numbertofixed--%E0%A4%B5%E0%A4%BF%E0%A4%AD%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A8-%E0%A4%B8%E0%A4%82%E0%A4%96%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%8F%E0%A4%81-%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A6%E0%A4%B0%E0%A5%8D%E0%A4%B6%E0%A4%BF%E0%A4%A4-%E0%A4%95%E0%A4%B0%E0%A4%A4%E0%A4%BE-%E0%A4%B9%E0%A5%88)
  - [`Math.max()` less than `Math.min()`](#mathmax-less-than-mathmin)
  - [तुलना `null` से` 0` तक](#%E0%A4%A4%E0%A5%81%E0%A4%B2%E0%A4%A8%E0%A4%BE-null-%E0%A4%B8%E0%A5%87-0-%E0%A4%A4%E0%A4%95)
  - [समान परिवर्तनशील पुनर्वितरण](#%E0%A4%B8%E0%A4%AE%E0%A4%BE%E0%A4%A8-%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%A4%E0%A4%A8%E0%A4%B6%E0%A5%80%E0%A4%B2-%E0%A4%AA%E0%A5%81%E0%A4%A8%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%BF%E0%A4%A4%E0%A4%B0%E0%A4%A3)
  - [डिफ़ॉल्ट व्यवहार Array.prototyp.sort ()](#%E0%A4%A1%E0%A4%BF%E0%A4%AB%E0%A4%BC%E0%A5%89%E0%A4%B2%E0%A5%8D%E0%A4%9F-%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%B5%E0%A4%B9%E0%A4%BE%E0%A4%B0-arrayprototypsort-)
- [📚 अन्य संसाधन](#-%E0%A4%85%E0%A4%A8%E0%A5%8D%E0%A4%AF-%E0%A4%B8%E0%A4%82%E0%A4%B8%E0%A4%BE%E0%A4%A7%E0%A4%A8)
- [🎓 License](#-license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 💪🏻 प्रेरणा

> सिर्फ मनोरंजन के लिए
>
> &mdash; _[**“सिर्फ मनोरंजन के लिए: एक्सीडेंटल रिवोल्यूशनरी की कहानी”**](https://en.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

इस सूची का प्राथमिक लक्ष्य कुछ पागल उदाहरणों को इकट्ठा करना और यह बताना है कि यदि संभव हो तो वे कैसे काम करते हैं। सिर्फ इसलिए कि कुछ ऐसा सीखना मजेदार है जिसे हम पहले नहीं जानते थे।

यदि आप एक शुरुआती हैं, तो आप इन नोटों का उपयोग जावास्क्रिप्ट में गहरा गोता लगाने के लिए कर सकते हैं। मुझे उम्मीद है कि ये नोट्स आपको विनिर्देश पढ़ने में अधिक समय बिताने के लिए प्रेरित करेंगे।

यदि आप एक पेशेवर डेवलपर हैं, तो आप इन उदाहरणों पर सभी उद्धरणों और हमारे प्रिय जावास्क्रिप्ट के अप्रत्याशित किनारों के लिए एक महान संदर्भ के रूप में विचार कर सकते हैं।

किसी भी मामले में, बस इसे पढ़ें। आप शायद कुछ नया खोजने जा रहे हैं।

# ✍🏻 नोटेशन

**`// ->`** एक अभिव्यक्ति का परिणाम दिखाने के लिए प्रयोग किया जाता है. उदाहरण के लिए:

```js
1 + 1; // -> 2
```

**`// >`** का परिणाम है `console.log` या कोई अन्य आउटपुट। उदाहरण के लिए:

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** स्पष्टीकरण के लिए इस्तेमाल की जाने वाली टिप्पणी मात्र है। उदाहरण:

```js
// Assigning a function to foo constant
const foo = function() {};
```

# 👀 उदाहरण

## `[]` के बराबर`![]`

array समान नहीं है:

```js
[] == ![]; // -> true
```

### 💡 व्याख्या:

अमूर्त समानता ऑपरेटर उनकी तुलना करने के लिए दोनों पक्षों को संख्याओं में परिवर्तित करता है और दोनों पक्ष अलग-अलग कारणों से संख्या `0` बन जाते हैं। एरे सत्य हैं, इसलिए दाईं ओर, एक सत्य मूल्य के विपरीत `गलत` है, जो तब` 0` के लिए मजबूर है। बाईं ओर, हालांकि, एक खाली सरणी पहले एक बूलियन बनने के बिना एक संख्या के लिए मजबूर की जाती है, और खाली सरणियों को सत्य होने के बावजूद `0` के लिए मजबूर किया जाता है।

इस प्रकार यह अभिव्यक्ति सरल है:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

See also [`[]` is truthy, but not `true`](#-is-truthy-but-not-true).

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true` is not equal `![]`, but not equal `[]` too

Array बराबर नहीं है `true`, लेकिन Array बराबर नहीं है` true` भी नहीं;
Array बराबर है 'false', Array बराबर है 'false' भी:

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 व्याख्या:

```js
true == []; // -> false
true == ![]; // -> false

// विनिर्देश के अनुसार

true == []; // -> false

toNumber(true); // -> 1
toNumber([]); // -> 0

1 == 0; // -> false

true == ![]; // -> false

![]; // -> false

true == false; // -> false
```

```js
false == []; // -> true
false == ![]; // -> true

// विनिर्देश के अनुसार

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> false

![]; // -> false

false == false; // -> true
```

- [**7.2.13** सार समानता](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## true is false

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 व्याख्या:

Consider this step-by-step:

```js
// true is 'truthy' and represented by value 1 (number), 'true' in string form is NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' is not the empty string, so it's a truthy value
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** सार समानता](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

यह जावास्क्रिप्ट में एक पुराने स्कूल का मजाक है, लेकिन फिर से बनाया गया है। यहाँ मूल एक है:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 व्याख्या:

अभिव्यक्ति का मूल्यांकन `'फू' + (+ 'बार') के रूप में किया जाता है, जो संख्या को नहीं करने के लिए` 'बार'` को परिवर्तित करता है।

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 Unary + Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` is not a `NaN`

```js
NaN === NaN; // -> false
```

### 💡 व्याख्या:

विनिर्देश इस व्यवहार के पीछे तर्क को सख्ती से परिभाषित करता है:

> 1. If `Type(x)` is different from `Type(y)`, return **false**.
> 2. If `Type(x)` is Number, then
>    1. If `x` is **NaN**, return **false**.
>    2. If `y` is **NaN**, return **false*
... [TRUNCATED]
```

### File: README-it-it.md
```md
# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> Una raccolta di snippet ingannevoli e divertenti scritti in JavaScript

JavaScript è un ottimo linguaggio. Ha una sintassi semplice, un grande ecosistema e, quello che conta veramente, una community fantastica.

Allo stesso tempo, sappiamo che JavaScript è un linguaggio abbastanza strano con delle parti cervellotiche. Alcune di queste possono rendere il nostro lavoro un inferno, alcune invece possono farci ridere a crepapelle.

L'idea per WTFJS è di [Brian Leroux](https://twitter.com/brianleroux). Questo elenco è largamente ispirato al suo talk [**“WTFJS”** at dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# Node Packaged Manuscript

Puoi installare questo manuale con `npm`. Lancia semplicemente:

```
$ npm install -g wtfjs
```

Ora dovresti essere in grado di eseguire `wtfjs` dalla riga di comando. Altrimenti puoi continuare tranquillamente a leggerlo qui.

Il codice sorgente lo puoi trovare qui: <https://github.com/denysdovhan/wtfjs>

# Traduzioni

Attualmente **wtfjs** è disponibile nelle seguenti lingue:

- [中文版](./README-zh-cn.md)
- [Français](./README-fr-fr.md)
- [Português do Brasil](./README-pt-br.md)
- [Polski](./README-pl-pl.md)
- [Italiano](./README-it-it.md)

[**Richiedi un'altra traduzione**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D

<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [💪🏻 Motivazione](#-motivazione)
- [✍🏻 Notazione](#-notazione)
- [👀 Esempi](#-esempi)
  - [`[]` è uguale a `![]`](#-%C3%A8-uguale-a-)
  - [`true` è diverso da `![]`, ma anche diverso da `[]`](#true-%C3%A8-diverso-da--ma-anche-diverso-da-)
  - [true è false](#true-%C3%A8-false)
  - [baNaNa](#banana)
  - [`NaN` non è `NaN`](#nan-non-%C3%A8-nan)
  - [È un fail](#%C3%A8-un-fail)
  - [`[]` è truthy, ma non `true`](#-%C3%A8-truthy-ma-non-true)
  - [`null` è falsy, ma non `false`](#null-%C3%A8-falsy-ma-non-false)
  - [`document.all` è un object, ma è undefined](#documentall-%C3%A8-un-object-ma-%C3%A8-undefined)
  - [Il numero più piccolo rappresentabile è maggiore di zero](#il-numero-pi%C3%B9-piccolo-rappresentabile-%C3%A8-maggiore-di-zero)
  - [function non è una function](#function-non-%C3%A8-una-function)
  - [Sommare array](#sommare-array)
  - ["Trailing commas" in un array](#trailing-commas-in-un-array)
  - [L'operatore di uguaglianza sugli array è un mostro](#loperatore-di-uguaglianza-sugli-array-%C3%A8-un-mostro)
  - [`undefined` e `Number`](#undefined-e-number)
  - [`parseInt` è bast\*\*do](#parseint-%C3%A8-bast%5C%5Cdo)
  - [Math con `true` e `false`](#math-con-true-e-false)
  - [I commenti HTML sono validi anche in JavaScript](#i-commenti-html-sono-validi-anche-in-javascript)
  - [`NaN` è ~~not~~ a number](#nan-%C3%A8-not-a-number)
  - [`[]` e `null` sono objects](#-e-null-sono-objects)
  - [Incrementare numeri magicamente](#incrementare-numeri-magicamente)
  - [La precisione di `0.1 + 0.2`](#la-precisione-di-01--02)
  - [Patchare numeri](#patchare-numeri)
  - [Confrontare tre numeri](#confrontare-tre-numeri)
  - [Matematica spassosa](#matematica-spassosa)
  - [Somma di RegExps](#somma-di-regexps)
  - [Le stringhe non sono istanze di `String`](#le-stringhe-non-sono-istanze-di-string)
  - [Richiamare funzioni con le backticks](#richiamare-funzioni-con-le-backticks)
  - [Call call call](#call-call-call)
  - [Una proprietà chiamata `constructor`](#una-propriet%C3%A0-chiamata-constructor)
  - [Un Object usato come key nelle property di un oggetto](#un-object-usato-come-key-nelle-property-di-un-oggetto)
  - [Accedere ai prototypes con `__proto__`](#accedere-ai-prototypes-con-__proto__)
  - [`` `${{Object}}` ``](#-object-)
  - [Destructuring con valori di default](#destructuring-con-valori-di-default)
  - [Puntini e lo spreading](#puntini-e-lo-spreading)
  - [Labels](#labels)
  - [Labels annidate](#labels-annidate)
  - [Un `try..catch` insidioso](#un-trycatch-insidioso)
  - [Si tratta di ereditarietà multipla?](#si-tratta-di-ereditariet%C3%A0-multipla)
  - [Un generator che produce se stesso](#un-generator-che-produce-se-stesso)
  - [Una classe di tipo class](#una-classe-di-tipo-class)
  - [Oggetti non-coercible](#oggetti-non-coercible)
  - [Arrow functions strambe](#arrow-functions-strambe)
  - [Arrow functions non possono essere un costruttore](#arrow-functions-non-possono-essere-un-costruttore)
  - [`arguments` e arrow functions](#arguments-e-arrow-functions)
  - [Uno strano return](#uno-strano-return)
  - [Concatenare assegnamenti su un object](#concatenare-assegnamenti-su-un-object)
  - [Accedere alle properties di un object con gli array](#accedere-alle-properties-di-un-object-con-gli-array)
  - [Null e gli operatori relazionali](#null-e-gli-operatori-relazionali)
  - [`Number.toFixed()` mostra numeri diversi](#numbertofixed-mostra-numeri-diversi)
  - [`Math.max()` più piccolo di `Math.min()`](#mathmax-pi%C3%B9-piccolo-di-mathmin)
  - [Confrontare `null` con `0`](#confrontare-null-con-0)
  - [Alcune ridichiarazioni di variabili](#alcune-ridichiarazioni-di-variabili)
  - [Comportamento di default di Array.prototype.sort()](#comportamento-di-default-di-arrayprototypesort)
  - [resolve() non restituisce un'istanza di Promise](#resolve-non-restituisce-unistanza-di-promise)
- [📚 Other resources](#-other-resources)
- [🎓 License](#-license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->

# 💪🏻 Motivazione

> Just for fun
>
> &mdash; _[**“Just for Fun: The Story of an Accidental Revolutionary”**](https://en.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

Lo scopo principale di questo elenco è quello di raccogliere alcuni esempi strambi e mostrarne il loro funzionamento, se possibile. Semplicemente per il fatto che è divertente imparare qualcosa che non sapevamo prima.

Se sei un principiante puoi utilizzare questi appunti per approfondire JavaScript. Spero che questi appunti ti motivino a leggerne le specifiche.

Se sei uno sviluppatore senior, considera questi esempi come un'ottimo punto di riferimento per tutte quelle stranezze e stramberie del tuo amato JavaScript.

Ad ogni modo, leggilo. Probabilmente imparerai qualcosa di nuovo.

# ✍🏻 Notazione

**`// ->`** viene utilizzato per indicare il risultato di un'espressione. Ad esempio:

```js
1 + 1; // -> 2
```

**`// >`** significa il risultato di `console.log` o di un altro output. Ad esempio:

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** è semplicemente un commento utilizzato per le spiegazioni. Esempio:

```js
// Assegnare una funzione ad una costante
const foo = function() {};
```

# 👀 Esempi

## `[]` è uguale a `![]`

Array è uguale a not array:

```js
[] == ![]; // -> true
```

### 💡 Spiegazione:

L'opratore di abstract equality converte entrambi gli operandi prima di confrontarli, e diventano entrambi `0` per ragioni differenti. Gli Array sono truthy, quindi sulla destra, l'opposto di un valore truthy è `false`, che viene quindi forzato a diventare uno `0`. Sul lato sinistro però l'array vuoto viene forzato a diventare un numero senza prima essere convertito in un valore booleano, e gli array vuoti vengono forzati a `0` a prescindere che siano truthy.

Qui possiamo vedere come viene semplificata l'espressione:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

Vedi anche [`[]` è truthy, ma non `true`](#-is-truthy-but-not-true).

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true` è diverso da `![]`, ma anche diverso da `[]`

Array è diverso da `true`, ma anche not Array è diverso da `true`;
Array è uguale a `false`, ma anche not Array è uguale a `false`:

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 Spiegazione:

```js
true == []; // -> false
true == ![]; // -> false

// Secondo le specifiche

true == []; // -> false

toNumber(true); // -> 1
toNumber([]); // -> 0

1 == 0; // -> false

true == ![]; // -> false

![]; // -> false

true == false; // -> false
```

```js
false == []; // -> true
false == ![]; // -> true

// Secondo le specifiche

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> true

![]; // -> false

false == false; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## true è false

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 Spiegazione:

Considera questo, step-by-step:

```js
// true è 'truthy' e rappresentato dal valore 1 (number), 'true' in formato stringa è NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' non è la stringa vuota, quindi è un valore truthy
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

Questo è un giochino old-school in JavaScript, rivisitato. L'originale è questo:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 Spiegazione:

L'espressione viene valutata come `'foo' + (+'bar')`, che converte `'bar'` in "not a number".

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 Unary + Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` non è `NaN`

```js
NaN === NaN; // -> false
```

### 💡 Spiegazione:

Le specifiche definiscono rigorosamente la logica dietro a questo comportamento:

> 1. Se `Type(x)` è diverso da `Type(y)`, return **false**.
> 2. Se `Type(x)` è Number, allora
>    1. Se `x` è **NaN**, return **false**.
>    2. Se `y` è **NaN**, return **false**.
>    3. … … …
>
> &mdash; [**7.2.14** Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

Seguendo la definizione di `NaN` da quella dell'IEEE:

> Sono possibili quattro relazioni mutuamente esclusive: less than, equal, greater than, e unordered. L'ultimo caso si presenta quando almeno un operando è NaN. Tutt i NaN se comparati risulteranno unordered, inclusa la comparazione con se stesso.
>
> &mdash; [“What is the rationale for all comparisons returning false for IEEE754 NaN values?”](https://stackoverflow.com/questions/1565164/1573715#1573715) at StackOverflow

## È un fail

Non crederai ai tuoi occhi, ma...

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 Spiegazione:

Rompendo quell'ammasso di simboli in pezzettini, possiamo notare che il seguente pattern si ripete spesso:

```js
![] + []; // -> 'false'
![]; // -> false
```

Quindi proviamo a sommare `[]` a `false`. Ma a causa di una serie di chiamate interne (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`) otteniamo la conversione dell'operando a destra in una stringa:

```js
![] + [].toString(); // 'false'
```

Se pensiamo ad una stringa come un Array, possiamo accedere al suo primo elemento con `[0]`:

```js
"false"[0]; // -> 'f'
```

Il resto è ovvio, ma la `i` è complicata. La `i` in `fail` viene ottenuta generando la stringa `'falseundefined'` e prendendo l'elemento all'indice `['10']`

## `[]` è truthy, ma non `true`

Un array è un valore truthy, ma non è uguale a `true`.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 Spiegazione:

Ecco i link alle sezioni corrispondenti della specifica ECMA-262:

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` è falsy, ma non `false`

Nonostante il fatto che `null` sia un valore falsy, non è uguale a `false`.

```js
!!null; // -> false
null == false; // -> false
```

Allo stesso modo, altri valori falsy, come `0` o `''` sono uguali a `false`.

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 Spiegazione:

La spiegazione è la stessa dell'esempio precedente. Ecco il link corrispondente:

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` è un object, ma è undefined

> ⚠️ Questo fa parte delle Browser API e non funziona su Node.js ⚠️

Nonostante il fatto che `document.all` sia un oggetto array-like e permette l'accesso al DOM della pagina, risponde alla funzione `typeof` con `undefined`.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

Allo stesso modo, `document.all` è diverso da `undefined`.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

Ma contemporaneamente:

```js
document.all == null; // -> true
```

### 💡 Spiegazione:

> `document.all` veniva utilizzato per accedere agli elementi del DOM, nelle vecchie versioni di IE. Nonostante non sia mai diventato uno standard, veniva ampiamente utilizzato in codice JS non proprio recentissimo. Quando vennero rilasciate le nuove APIs (come `document.getElementById`) questa API divenne obsoleta e il comitato dello standard dovette decidere cosa farne. A causa del suo uso spropositato l'API venne mantenuta ma venne introdotta una violazione intenzionale nelle speficiche di JavaScript.
> Il motivo per il quale risponde a `false` quando si utilizza l'operatore di [Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison) con `undefined`, mentre `true` quando si utilizza l'operatore di [Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) è a causa della violazione intenzionale inserita nella specifica che la permette in modo esplicito.

> &mdash; [“Obsolete features - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) at WhatWG - HTML spec
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) at YDKJS - Types & Grammar

## Il numero più piccolo rappresentabile è maggiore di zero

`Number.MIN_VALUE` è il numero più pic
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
