---
id: wtfjs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.222817
---

# KNOWLEDGE EXTRACT: wtfjs
> **Extracted on:** 2026-03-30 22:06:07
> **Source:** wtfjs

---

## File: `.editorconfig`
```
root = true

[*]
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[package.json]
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

## File: `.gitignore`
```
.DS_Store
node_modules
npm-debug.log
```

## File: `CONTRIBUTING.md`
```markdown
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

## File: `LICENSE`
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

Copyright (C) 2017 Denys Dovhan

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```

## File: `package.json`
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

## File: `README-fr-fr.md`
```markdown
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
> La raison pour laquelle `document.all` retourne `false` lors de l'utilisation de l'opérateur d'égalité stricte ([Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)) avec `undefined` et `true` lors de l'utilisation de l'opérateur d'égalité abstraite ([Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)) est due à la violation volontaire de la spécification qui le permet explicitement.
>
> &mdash; [“Obsolete features - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) sur WhatWG - HTML spec.
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) sur YDKJS - Types & Grammar.

## La valeur minimale est supérieure à zéro

`Number.MIN_VALUE` est le plus petit nombre, qui est supérieur à zéro :

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 Explication :

> `Number.MIN_VALUE` est `5e-324`, c'est-à-dire le plus petit nombre positif pouvant être représenté dans la précision flottante et donc, c'est aussi le plus près que possible de zéro. Il définit la meilleure résolution que vous pouvez atteindre avec des valeurs flottantes.
>
> Maintenant, la plus petite valeur globale est `Number.NEGATIVE_INFINITY`, bien que cette dernière ne soit pas vraiment numérique au sens strict.
>
> &mdash; [“Why is `0` less than `Number.MIN_VALUE` in JavaScript?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) at StackOverflow

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## Fonction n'est pas une fonction

> ⚠️ Une erreur présente dans la v5.5 (V8) ou inférieure de Node.js (Node.js <=7) ⚠️

Vous êtes tous au courant de l'irritant _undefined is not a function_, mais qu'en est-il de ceci :

```js
// Déclare une classe qui _extends_ `null`
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 Explication :

Ceci ne fait pas partie de la spécification. C'est seulement une erreur qui a depuis été corrigé, il ne devrait donc plus y avoir de problème à l'avenir.

## Ajout de tableaux

Et si vous essayiez d'additionner deux tableaux ?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 Explication :

C'est la concaténation ! Etape par étape, ça ressemble à ceci :

```js
[1, 2, 3] +
  [4, 5, 6][
    // appelle toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concaténation
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## Les virgules finales dans un tableau

Vous avez créé un tableau avec 4 éléments vides. Malgré tout, vous obtiendrez un tableau avec seulement trois éléments, à cause des virgules finales.

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 Explication :

> Les **virgules finales** (_trailing commas_ en anglais) peuvent être utiles lors de l'ajout de nouveaux éléments, de paramètres ou de propriétés à du code JavaScript. Si vous voulez ajouter une nouvelle propriété, vous pouvez tout simplement ajouter une nouvelle ligne sans modifier la ligne précédente si cette ligne utilise déjà une virgule finale. Cela rend plus clair les différences dans un système de contrôle de version et l'édition de code pourrait être moins difficile.
>
> &mdash; [Virgules finales (trailing commas)](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Virgules_finales) sur MDN.

## L'égalité des tableaux est un monstre

En JavaScript, l'égalité des tableaux est un monstre, comme vous pouvez le voir ci-dessous :

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 Explication :

Vous devriez regarder très attentivement les exemples ci-dessus ! Ce comportement est décrit dans la section [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) de la spécification.

## `undefined` et `Number`

Si nous ne transmettons aucun argument dans le constructeur `Number`, nous obtiendrons `0`. La valeur `undefined` est attribuée aux arguments formels en l'absence d'arguments, alors vous pouvez vous attendre à ce que `Number` sans argument utilise `undefined` comme valeur de paramètre. Toutefois, quand nous lui passons `undefined` directement, nous obtiendrons `NaN` en retour.

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 Explication :

Selon la spécification :

1. Si aucun argument n'a été passé lors de l'appel de la fonction, `n` est `+0`.
2. Sinon, `n` est ? `ToNumber(value)`.
3. Dans le cas d'`undefined`, `ToNumber(undefined)` doit retourner `NaN`.

Voici les sections correspondantes :

- [**20.1.1** The Number Constructor](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` est un méchant

`parseInt` est célèbre pour ses bizarreries:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 Explication :** Ce résultat est dû au fait que `parseInt` continue d'analyser caractère par caractère la chaîne jusqu'à ce qu'il rencontre un caractère qu'il ne connaît pas. Le `f` dans `'f*ck'` correspond au chiffre hexadécimal `15`.

Analyser `Infinity` comme entier est quelque chose…

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

Soyez prudent avec l'analyse de `null` aussi :

```js
parseInt(null, 24); // -> 23
```

**💡 Explication :**

> `parsetInt` convertit `null` sous forme de chaîne `"null"` et essait de la convertir. Pour les bases comprises entre 0 et 23, `parseInt` ne peut convertir aucun chiffre, donc `parseInt` renvoie `NaN`. Sur 24, `"n"`, la 14ème lettre, est ajoutée au système de numération. Sur 31, `"u"`, la 21ème lettre, est ajoutée et la chaîne entière peut être décodée. Sur 37, il n'y a plus de jeu de valeur numérique valide pouvant être générée, donc, `NaN` est renvoyé.
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) sur StackOverflow.

N'oubliez pas les octaux:

```js
parseInt("06"); // 6
parseInt("08"); // 8 si support ECMAScript 5
parseInt("08"); // 0 si pas support ECMAScript 5
```

**💡 Explication :** Si la chaîne d'entrée commence par 0, la base est égale à 8 (octal) ou à 10 (décimal). La base choisie dépend de l'implémentation. ECMAScript 5 indique que la valeur 10 (décimal) est utilisée, mais tous les navigateurs ne le prennent pas encore en charge. Pour cette raison, spécifiez toujours une base lorsque vous utilisez `parseInt`.

`parseInt` convertit toujours une entrée en chaîne :

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Soyez prudent lors d'analyse de valeurs en virgule flottante :

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 Explication :** `parseInt` prend une chaîne de caractère comme argument et retourne un entier sur la base spécifiée. `parseInt` supprime aussi tout ce que suit, incluant le premier non-chiffre de la chaîne transmise en paramètre. `0.000001` est converti en chaîne `"0.000001"`, et `parseInt` retourne `0`. Quand `0.0000001` est converti en chaîne, il est traité comme `"1e-7"` et retourne donc `1`. `1/1999999` est interprété comme étant `5.00000250000125e-7` et retourne `5`.

## Math avec `true` et `false`

Faisons des maths :

```js
true +
  true(
    // -> 2
    true + true
  ) *
    (true + true) -
  true; // -> 3
```

Hmmm… 🤔

### 💡 Explication :

Avec le constructeur `Number`, nous pouvons forcer les valeurs aux nombres. Il est assez évident que `true` sera forcé à `1`.

```js
Number(true); // -> 1
```

L'opérateur unaire `+` tente de convertir sa valeur en nombre. Il peut convertir des représentations d'entiers et de nombres flottants sous forme de chaîne, de même que les valeurs `true`, `false` et `null`. S'il ne peut pas analyser une valeur particulière, il sera évalué à `NaN`. Cela signifie que nous pouvons contraindre `true` à `1` plus facilement :

```js
+true; // -> 1
```

Lorsque vous effectuez une addition ou une multiplication, la méthode `ToNumber` est appelée. Selon la spécification, cette méthode retourne :

> Si `argument` est **true**, retourne **1**. Si `argument` est **false**, retourne **+0**.

C'est pourquoi nous pouvons ajouter des valeurs booléennes en tant que nombres réguliers et obtenir des résultats corrects.

Les sections correspondantes :

- [**12.5.6** Unary `+` Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## Les commentaires HTML sont valides en JavaScript

Vous serez impressionné, mais `<!--` (connu sous le nom de commentaire HTML) est aussi valide comme commentaire en JavaScript.

```js
// commentaire valide
<!-- commentaire valide aussi
```

### 💡 Explication :

Impressionné ? Les commentaires de type HTML étaient à la base destinés à permettre aux navigateurs ne comprenant pas la balise `<script>` de se dégrader avec élégance. Ces navigateurs, par exemple Netscape 1.x, ne sont plus populaires aujourd'hui. Il est donc inutile de mettre des commenaitres HTML dans vos balises `<script>`.

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` n'est ~~pas~~ un nombre

`typeof` `NaN` est un `'number'` :

```js
typeof NaN; // -> 'number'
```

### 💡 Explication :

Explications sur le fonctionnement des opérateurs `typeof` et `instanceof` :

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` et `null` sont des objets

```js
typeof []; // -> "object"
typeof null; // -> "object"

// however
null instanceof Object; // false
```

### 💡 Explication :

Le comportement de l'opérateur `typeof` est défini dans la section suivante de la spécification :

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

Selon la spécification, l'opérateur `typeof` renvoie une chaîne : [Table 35: `typeof` Operator Results](https://www.ecma-international.org/ecma-262/#table-35). Pour les objets `null`, ordinaires, _standard exotic_ et _non-standard exotic_, qui n'implémentent pas `[[Call]]`, il retourne la chaîne `"object"`.

En revanche, vous pouvez vérifier le type d'un objet en utilisant la méthode `toString`.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## Nombres magiquement croissant

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 Explication :

Ceci est dû à la norme IEEE 754-2008 concernant l'arithmétique binaire en virgule flottante. À cette échelle, un nombre s'arrondit au nombre pair le plus près. Plus d'infos :

- [**6.1.6** The Number Type](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) sur Wikipedia

## Précision de `0.1 + 0.2`

Une blague bien connue. L'ajout de `0.1` et de `0.2` est mortellement précis :

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 Explication :

La réponse à la question [”Is floating point math broken?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) sur StackOverflow:

> Les constantes `0.2` et `0.3` seront également des approximations à leurs vraies valeurs. Il arrive que le `double` le plus proche de `0.2` soit supérieur au nombre rationnel `0.2`, mais que le `double` le plus proche de `0.3` soit inférieur au nombre rationnel `0.3`. La somme de `0.1` et `0.2` finit donc par être supérieure au nombre rationnel `0.3` et donc, en désaccord avec la constante de votre code.

Le problème est tellement connu qu'il y a même un site web appelé [0.30000000000000004.com](http://0.30000000000000004.com/). Il est récurrent pour tous les langages utilisant des mathématiques avec des virgules flottantes, pas seulement JavaScript.

## Patching de numéros

Vous pouvez ajouter vos propres méthodes pour encapsuler des objets comme `Number` ou `String`.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 Explication :

De toute évidence, vous pouvez _extend_ l'objet `Number` comme n'importe quel autre objet en JavaScript, mais ce n'est toutefois pas recommandé si le comportement de la méthode définie ne fait partie de la spécification. Voici donc la liste des propriétés de `Number` :

- [**20.1** Number Objects](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## Comparaison de trois nombres

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 Explication :

Pourquoi est-ce que cela fonctionne ainsi ? Et bien le problème se trouve dans la première partie de l'expression. Voici comment cela fonctionne :

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

Nous pouvons résoudre ce problème avec _l'opérateur Supérieur ou égal à (`>=`)_ :

```js
3 > 2 >= 1; // true
```

En savoir plus sur les opérateurs relationnels dans la spécification :

- [**12.10** Relational Operators](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## Math drôle

Souvent, les résultats d'opérations arithmétiques en JavaScript peuvent être assez inattendus. Considérez ces exemples :

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 Explication :

Que se passe-t-il dans les quatre premiers exemples ? Voici un petit tableau pour comprendre les additions en JavaScript :

```
Nombre  + Nombre  -> addition
Booléen + Nombre  -> addition
Booléen + Booléen -> addition
Nombre  + Chaîne -> concaténation
Chaîne  + Booléen -> concaténation
Chaîne  + Chaîne  -> concaténation
```

Qu'en est-il des autres exemples ? Les méthodes `ToPrimitive` et `ToString` sont implicitement appelées pour `[]` et `{}` avant une addition. En lire plus sur le processus d'évalution dans la spécification :

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

## Addition de RegExps

Saviez-vous que vous pouviez ajouter des nombres comme dans l'exemple ci-dessous ?

```js
// Remplacement de la méthode toString
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 Explication :

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## Les chaînes ne sont pas des instances de `String`

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 Explication :

Le constructeur `String` retourne une chaîne :

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

Essayons avec un `new` :

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> "object"
```

Un objet ? Qu'est-ce que c'est ?

```js
new String("str"); // -> [String: 'str']
```

Plus d'infos sur le constructeur `String` dans la spécification :

- [**21.1.1** The String Constructor](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## Appeler des fonctions avec des caractères accent grave

Déclarons une fonction qui enregistre tous les paramètres dans la console :

```js
function f(...args) {
  return args;
}
```

Aucun doute, vous savez qu'il est possible d'appeler cette fonction comme ceci :

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

Mais saviez-vous que vous pouvez appeler n'importe quelle fonction avec des caractères accent grave (_backticks_ en anglais) ?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 Explication :

Bon, ce n'est pas du tout magique si vous êtes familier des _littéraux de gabarits étiquetés_. Dans l'exemple ci-dessus, la fonction `f` est une étiquette pour littéral de gabarit. Les étiquettes avant un littéral de gabarit vous permettent d'analyser les littéraux de gabarits avec une fonction. Le premier argument d'une fonction étiquetée contient un tableau avec comme valeurs des chaînes. Les arguments restants sont liés aux expressions. Exemple :

```js
function template(strings, ...keys) {
  // fait quelque chose avec `strings` et `keys`…
}
```

Voici la [magic behind](http://mxstbr.blog/2016/11/styled-components-magic-explained/) la célébre bibliothèque appelée [💅 styled-components](https://www.styled-components.com/), qui est populaire dans la communauté React.

Lien vers la spécification :

- [**12.3.7** Tagged Templates](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## Call call call

> Trouvé par [@cramforce](http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 Explication :

Attention, ceci pourrait vous casser la tête ! Essayez de reproduire ce code dans votre tête : nous appliquons la méthode `call` en utilisant la méthode `apply`. Plus d'infos :

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## Une propriété `constructor`

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 Explication :

Considérez cet exemple étape par étape :

```js
// Déclare une nouvelle constante qui est une chaîne : "constructor"
const c = "constructor";

// `c` est une chaîne
c; // -> 'constructor'

// Pour obtenir le constructeur de la chaîne
c[c]; // -> [Function: String]

// Pour obtenir le constructeur du constructeur
c[c][c]; // -> [Function: Function]

// Appelle la Fonction constructeur et passe
// le corps d'une nouvelle fonction comme argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// Et ensuite appelle cette fonction anonyme
// Le résultat est un retour de console avec la chaîne "WTF?"
c[c][c]('console.log("WTF?")')(); // > "WTF?"
```

Un `Object.prototype.constructor` renvoie une référence à la fonction constructeur `Object` qui a créé l'instance de l'objet. Dans le cas des chaînes, il s'agit de `String`, dans le cas des nombres, il s'agit de `Number`, et ainsi de suite.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## Object en tant que clé de la propriété d'un objet

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 Explication :

Pourquoi est-ce que ça marche ? Ici, nous utilisons un _Computed property name_. Quand vous passez un objet entre ces crochets, l'objet est forcé de devenir une chaîne, alors nous obtenons la clé `[objet Object]` et la valeur `{}`.

Nous pouvons créer des enfers de crochets et de parenthèses comme dans l'exemple ci-dessous :

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

En savoir plus sur les objets littéraux ici:

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN
- [**12.2.6** Object Initializer](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## Accéder aux prototypes avec `__proto__`

Comme nous le savons, les primitives n’ont pas de prototypes. Cependant, si nous essayons d'obtenir une valeur de `__proto__` pour les primitives, nous obtiendrions ceci :

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 Explication :

Cela se produit car lorsque quelque chose n'a pas de prototype, il sera encapsulé dans un objet à l'aide de la méthode `ToObject`. Donc, étape par étape :

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

Voici plus d'infos sur `__proto__` :

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

Quel est le résultat de l'expression ci-dessous ?

```js
`${{ Object }}`;
```

La réponse est :

```js
// -> '[object Object]'
```

### 💡 Explication :

Nous avons défini un objet avec une propriété `Object` en utilisant une _propriété de notation raccourcie_ :

```js
{
  Object: Object;
}
```

Ensuite, nous avons passé cet objet au litéral de gabarit, ce qui fait que la méthode `toString` appelle donc cet objet. Voilà pourquoi nous obtenons la chaîne `'[object Object]'`.

- [**12.2.9** Template Literals](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [Initialisateur d'objet](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Initialisateur_objet) sur MDN.

## Déstructuration avec des valeurs par défaut

Considérez cet exemple :

```js
let x,
  { x: y = 1 } = { x };
y;
```

L'exemple ci-dessus est une bonne question pour un entretien. Quelle est la valeur de `y` ? La réponse est :

```js
// -> 1
```

### 💡 Explication :

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

Avec l'exemple ci-dessus :

1. On déclare `x` sans valeur, donc sa valeur est `undefined`.
2. Ensuite, nous intégrons la valeur de `x` dans la propriété de l'objet `x`.
3. Ensuite, nous extrayons la valeur de `x` en utilisant la déstructuration pour l'assigner à `y`. Si la valeur n'est pas déinie, nous utiliserons `1` comme valeur par défaut.
4. Retourne la valeur de `y`.

- [Initialisateur d'objet](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Initialisateur_objet) sur MDN.

## Points et propagation

Des exemples intéressants pourraient être composés avec la propagation de tableaux. Considérez cela :

```js
[...[..."..."]].length; // -> 3
```

### 💡 Explication :

Pourquoi `3` ? Lorsque nous utilisons le _[spread operator](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer)_, la méthode `@@iterator` est appelée et l'itérateur renvoyé est utilisé pour obtenir les valeurs à itérer. L'itérateur par défaut pour une chaîne étend une chaîne en caractères. Après sa propagation, ces caractères sont empaquetés dans un tableau. Ensuite, ce tableau est à nouveau propagé et empaqueté encore une fois dans un tableau.

Une chaîne `'...'` est composée de trois caractères `.`, donc, la longueur du tableau résultant est de `3`.

Maintenant, étape par étape :

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

Évidemment, nous pouvons étendre et encapsuler les éléments d’un tableau autant de fois que nous le souhaitons :

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// etc.
```

## Étiquettes

Peu de programmeurs connaissent les étiquettes en JavaScript. Elles sont plutôt intéressantes :

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// -> first
// -> undefined
```

### 💡 Explication :

La déclaration étiquetée est utilisée avec les déclarations `break` ou `continue`. Vous pouvez utiliser une étiquette pour identifier une boucle, puis ensuite, utiliser la déclaration `break` ou `continue` pour indiquer si un programme doit interrompre la boucle ou poursuivre son exécution.

Dans l'exemple ci-dessus, nous identifions une étiquette `foo`. Ensuite, `console.log('first');` est exécuté et l'exécution est interrompue.

En savoir plus sur les étiquettes en JavaScript :

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Label](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Instructions/label) sur MDN.

## Étiquettes imbriquées

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 Explication :

Similaire aux exemples précédents, suivez ces liens pour plus d'infos :

- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labeled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Label](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Instructions/label) sur MDN.

## `Try...catch` insidieux

Que retournera cette expression ? `2` ou `3` ?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

La réponse est `3`. Surprenant ?

### 💡 Explication :

- [**13.15** The `try` Statement](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## Est-ce un héritage multiple ?

Regardez l'exemple ci-dessous :

```js
new class F extends (String, Array) {}(); // -> F []
```

Est-ce un héritage multiple ? Non.

### 💡 Explication :

L'élément intéressant est la valeur de la clause `extends` (`(String, Array)`). L'opérateur de groupement retourne toujours son dernier argument, donc `(String, Array)` est en réalité simplement `Array`. Cela signifie que nous venons de créer une classe qui _extends_ `Array`.

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## Un générateur qui se `yield` lui-même

Considérez cet exemple de générateur qui se `yield` lui-même :

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

Comme vous pouvez le constater, la valeur renvoyée est un objet dont la `valeur` est égale à `f`. Dans ce cas, nous pouvons faire quelque chose semblable à ça :

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 Explication :

Pour comprendre pourquoi cela fonctionne ainsi, lisez ces sections de la spécification :

- [**25** Control Abstraction Objects](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** Generator Objects](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## Une classe de classe

Considérez cette syntaxe obfusquée :

```js
typeof new class {
  class() {}
}(); // -> "object"
```

Il semblerait que nous déclarions une classe à l'intérieur d'une classe. Cela devrait être une erreur, cependant, nous obtenons la chaîne `"object"`.

### 💡 Explication :

Depuis ECMAScript 5, les _mots clés_ sont autorisés en tant que _noms de propriétés_. Réfléchissez comment vous le feriez pour cet exemple d'objet simple :

```js
const foo = {
  class: function() {}
};
```

Et les définitions de méthode abrégée standard d'ES6. Aussi, les classes peuvent être anonymes. Donc, si nous supprimons la partie `: function`, nous obtiendrons :

```js
class {
  class() {}
}
```

Le résultat d'une classe par défaut est toujours un objet simple. Et son `typeof` devrait retourner `"object"`.

Plus d'infos ici :

- [**14.3** Method Definitions](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## Objets incoercibles

Avec des symboles bien connus, il existe un moyen de se débarrasser de la coercition de type. Examinez l'exemple ci-dessous :

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError(
      "inCoercible ne doit pas être appelé avec null ou undefined"
    );
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Tente de transformer un objet incoercible");
  };

  return res;
}
```

Maintenant, nous pouvons l'utiliser de cette manière :

```js
// objets
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Tente de transformer un objet incoercible
foo + "evil"; // -> TypeError: Tente de transformer un objet incoercible

// chaînes
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Tente de transformer un objet incoercible
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Tente de transformer un objet incoercible

// nombres
const baz = nonCoercible(1);

baz == 1; // -> Tente de transformer un objet incoercible
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 Explication :

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## Fonctions fléchées complexes

Considérez l'exemple ci-dessous :

```js
let f = () => 10;
f(); // -> 10
```

D'accord, d'accord, mais qu'en est-il de celui-ci :

```js
let f = () => {};
f(); // -> undefined
```

### 💡 Explication :

Vous pourriez vous attendre à obtenir `{}` au lieu d'`undefined`. C'est dû au fait que les accolades font partie de la syntaxe des fonctions fléchées; `f` renverra donc `undefined`. Il est cependant possible de renvoyer l'objet `{}` directement à partir d'une fonction fléchée en mettant la valeur de retour entre parenthèses :

```js
let f = () => ({});
f(); // -> {}
```

## Les fonctions fléchées ne peuvent pas être un constructeur

Considérez l'exemple ci-dessous :

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

Maintenant, essayez de faire la même chose avec une fonction fléchée :

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 Explication :

Les fonctions fléchées ne peuvent pas être utilisées en tant que constructeurs et produiront une erreur si elles sont utilisées avec `new` parce qu'elles ont un _lexical `this`_ et pas de propriété `prototype`, cela n'aurait donc pas beaucoup de sens.

## `arguments` et fonctions fléchées

Considérez l'exemple ci-dessous :

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

Maintenant, essayez de faire la même chose avec une fonction fléchée :

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 Explication :

Les fonctions fléchées sont une version allégée des fonctions standards dans laquelle l'accent est mis sur la taille et le _lexical `this`_. En même temps, les fonctions fléchées ne fournissent pas de liaison pour l'objet `arguments`. Comme alternative valable, utilisez les paramètres `rest` pour obtenir le même résultat :

```js
let f = (...args) => args;
f("a");
```

- [Fonctions fléchées](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Fonctions/Fonctions_fl%C3%A9ch%C3%A9es) sur MDN.

## Retour difficile

La déclaration `return` est compliquée aussi. Considérez ceci :

```js
(function() {
  return;
  {
    b: 10;
  }
})(); // -> undefined
```

### 💡 Explication :

`return` et l'expression renvoyée doivent être sur la même ligne :

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

Cela est dû au concept appelé "Insertion Automatique du Point-Virgule", qui insère automatiquement des points-virgules à la fin de la plupart des nouvelles lignes. Dans le premier exemple, un point-virgule est inséré entre `return` et l'objet littéral. La fonction renvoie donc `undefined` et l'objet littéral n'est jamais évalué.

- [**11.9.1** Rules of Automatic Semicolon Insertion](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** The `return` Statement](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## Chaînage d'affectations sur un objet

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

De droite à gauche, `{n: 2}` est affecté à `foo`, et le résultat de cette affectation `{n: 2}` est affecté à `foo.x`. C'est pourquoi `bar` retourne `{n: 1, x: {n: 2}}`, puisque `bar` est une référence à `foo`. Mais pourquoi `foo.x` retourne `undefined`, alors que ce n'est pas le cas pour `bar.x` ?

### 💡 Explication :

`foo` et `bar` font référence au même objet `{n: 1}`, et les _lvalues_ sont résolues avant les assignations. `foo = {n: 2}` crée un nouvel objet, et donc `foo` est mis à jour pour référencer ce nouvel objet. L'astuce ici est `foo` dans `foo.x = …`, car une _lvalue_ a été résolue au préalable et fait toujours référence à l'objet précédent `foo = {n: 1}` et donc le met à jour en ajoutant la valeur `x`.

Après cette chaîne d'assignation, `bar`, quant à lui, fait toujours référence à l'ancien objet `foo`, alors que `foo` fait référence au nouvel objet `{n: 2}`, où `x` n'existe pas.

C'est équivalent à :

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// `bar.x` pointe sur l'adresse du nouvel objet `foo`
// ce n'est pas équivalent à : `bar.x = {n: 2}`
```

## Accéder aux propriétés d'un objet avec des tableaux

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

Qu'en est-il des tableaux pseudo-multidimensionnels ?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 Explication :

L'opérateur `[]` convertit l'expression passée en utilisant `toString`. Transformer un tableau composé d'un seul élément vers une chaîne est similaire à transformer l'élément du tableau en chaîne :

```js
["property"].toString(); // -> 'property'
```

## Opérateurs `null` et relationnels

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 Explication :

En bref, si `null < 0` est `false`, alors `null >= 0` est `true`. Lisez une explication détaillée [ici](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274).

## `Number.toFixed()` affiche différents nombres

`Number.toFixed()` peut se comporter étrangement selon le navigateur utilisé. Voir cet exemple :

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 Explication :

Alors que votre premier instinct peut être que IE11 a correct et que Firefox et Chrome ont faux, la réalité est que Firefox et Chrome obéissent plus directement aux normes relatives aux nombres (IEEE-754 Floating Point), alors qu'IE11 les désobéit minutieusement dans (ce qui est probablement) un effort de donner des résultats plus clairs.

Vous pouvez voir pourquoi cela se produit avec quelques tests rapides :

```js
// Confirme le résultat curieux d'arrondir `5` vers le bas
(0.7875).toFixed(3); // -> 0.787
// Il semble que ce soit juste `5` lorsque vous développez
//  les limites de la précision de flottement de 64 bits (double précision)
(0.7875).toFixed(14); // -> 0.78750000000000
// Mais que se passe-t-il si vous allez au-delà de la limite ?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

Les nombres à virgule flottante ne sont pas stockés sous forme de liste de chiffres décimaux en interne, mais par le biais d'une méthodologie plus complexe qui produit de minuscules inexactitudes qui sont généralement arrondies par des appels à `toString` ou des appels similaires, mais qui sont réellement présentes en interne.

Dans ce cas, le `5` sur la fin était en réalité une fraction extrêmement petite, en dessous d'un vrai `5`. Si vous arrondissez à une longueur raisonnable, vous obtenez un `5`… mais ce n'est en réalité pas un `5` en interne.

Ceci étant dit, IE11 rapportera la valeur entrée uniquement avec des zéros ajoutés à la fin, même dans le cas de `toFixed(20)`, car cela semble forcer la valeur arrondie pour réduire les problèmes liées aux limites matérielles.

Voir pour référence `NOTE 2` sur la définition de ECMA-262 pour `toFixed`.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` est moins que `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 Explication :

- [Why is Math.max() less than Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) par Charlie Harvey.

## Comparer `null` à `0`

Les expressions suivantes semblent introduire une contradiction :

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

Comment `null` peut-il être ni égal ni supérieur à `0`, si `null >= 0` est en fait `true` ? (Ceci fonctionne de la même manière avec inférieur ou égal à (`<=`).)

### 💡 Explication :

Les méthodes d'évaluation de ces trois expressions sont toutes différentes et sont responsables de la production de ce comportement inattendu.

Premièrement, la comparaison d'égalité abstraite `null == 0`. Normalement, si cet opérateur ne peut pas comparer correctement les valeurs d'un côté comme de l'autre, il convertit les deux en nombres et compare ensuite les nombres. Alors, vous pouvez vous attendre au comportement suivant :

```js
// Ce n'est pas ce qui se passe
(null == 0 + null) == +0;
0 == 0;
true;
```

Cependant, suite à une lecture attentive de la spécification, la transformation du nombre n'a pas lieu sur un côté qui est `null` ou `undefined`. Par conséquent, si vous avez `null` sur un des deux côté du signe égal, l'autre côté doit être `null` ou `undefined` pour que l'expression retourne `true`. Comme ce n'est pas le cas, `false` est renvoyé.

Ensuite, la comparaison relationnelle `null > 0`. L'algorithme ici, contrairement à celui de l'opérateur d'égalité abstraite, _va_ convertir `null` à un nombre. Donc, nous obtenons ce comportement :

```js
null > 0
+null = +0
0 > 0
false
```

Finalement, la comparaison relationnelle `null >= 0`. Vous pourriez soutenir que cette expression devrait être le résultat de `null > 0 || null == 0`; si tel était le cas, les résultats ci-dessus signifieraient que ceci serait aussi `false`. Toutefois, l'opérateur `>=` fonctionne d'une manière très différente, qui est simplement d'utiliser le contraire de l'opérateur `<`. Parce que notre exemple ci-dessus, utilisant l'opérateur supérieur à, s'applique également à l'opérateur inférieur à, cela signifie que cette expression est réellement évaluée de la manière suivante :

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## Même redéclaration d'une variable

JavaScript autorise la redéclaration de variables :

```js
a;
a;
// Ceci est aussi valide
a, a;
```

Et ça fonctionne aussi en mode `strict` :

```js
var a, a, a;
var a;
var a;
```

### 💡 Explication :

Toutes les définitions fusionnent en une seule définition.

- [**13.3.2** Variable Statement](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## Comportement par défaut d'`Array.prototype.sort()`

Imaginez que vous ayez besoin de trier un tableau composé de nombres.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 Explication :

L'ordre de tri par défaut est construit lors de la transformation des éléments en chaînes, puis en comparant leurs séquences de valeurs unitaires sur le jeu de caractères UTF-16.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### Indice

Passez `comparefn` si vous essayez de trier n'importe quoi d'autre qu'une chaîne.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

# 📚 Autres ressources

- [wtfjs.com](http://wtfjs.com/) — une collection d'irrégularités spéciales très particulières, d'incohérences et de moments terriblement non intuitifs pour le langage du Web.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — Un discours éclair de Gary Bernhardt de CodeMash 2012.
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — Kyle Simpsons parle des tentatives de Forward 2 pour "sortir de l'absurdité" du JavaScript. Il veut vous aider à produire un code plus propre, plus élégant et plus lisible, puis inspirer les gens à contribuer à la communauté open-source.

# 🎓 Licence

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
```

## File: `README-hi.md`
```markdown
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
>    2. If `y` is **NaN**, return **false**.
>    3. … … …
>
> &mdash; [**7.2.14** सख्त समानता की तुलना](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

Following the definition of `NaN` from the IEEE:

> चार परस्पर अनन्य संबंध संभव हैं: से कम, बराबर, अधिक से अधिक, और अव्यवस्थित। आखिरी मामला तब उठता है जब कम से कम एक ऑपरेंड NaN होता है। प्रत्येक NaN अपने आप सहित हर चीज के साथ अनियंत्रित की तुलना करेगा।
>
> &mdash; [“IEEE754 NaN मानों के लिए झूठी वापसी करने वाली सभी तुलनाओं के लिए तर्क क्या है?”](https://stackoverflow.com/questions/1565164/1573715#1573715) at StackOverflow

## यह विफल है

आपको विश्वास नहीं होगा, लेकिन …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 व्याख्या:

प्रतीकों के उस द्रव्यमान को टुकड़ों में तोड़कर, हम देखते हैं कि निम्न पैटर्न अक्सर होता है:

```js
![] + []; // -> 'false'
![]; // -> false
```

इसलिए हम `[]` को `गलत` में जोड़ने का प्रयास करते हैं। लेकिन कई आंतरिक फ़ंक्शन कॉल के कारण (`बाइनरी + ऑपरेटर` ->` ToPrimitive` -> `[[DefaultValue]]`) हम एक स्ट्रिंग के लिए सही ऑपरेंड को परिवर्तित करते हैं:

```js
![] + [].toString(); // 'false'
```

एक स्ट्रिंग के रूप में एक सरणी के रूप में सोचकर हम इसके पहले चरित्र तक पहुंच सकते हैं `[0]`:

```js
"false"[0]; // -> 'f'
```

बाकी स्पष्ट है, लेकिन `i` मुश्किल है। `विफल 'में` i` स्ट्रिंग को उत्पन्न करके' 'falseundefined'` को पकड़ा जाता है और सूचकांक पर तत्व को पकड़ा जाता है `[' 10 ']`'

## `[]` is truthy, but not `true`

एक सरणी एक सत्य मूल्य है, हालांकि, यह `सत्य` के बराबर नहीं है।

```js
!![]       // -> true
[] == true // -> false
```

### 💡 व्याख्या:

यहाँ ECMA-262 विनिर्देश में संबंधित वर्गों के लिंक दिए गए हैं:

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` is falsy, but not `false`

इस तथ्य के बावजूद कि `null` एक मिथ्या मूल्य है, यह` false` के बराबर नहीं है।

```js
!!null; // -> false
null == false; // -> false
```

इसी समय, अन्य झूठे मूल्य, जैसे `0` या` `` `` झूठ` के बराबर हैं।

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 व्याख्या:

विवरण पिछले उदाहरण के समान है। यहाँ इसी लिंक है:

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` is an object, but it is undefined

> ⚠️ यह ब्राउज़र API का हिस्सा है और यह Node.js वातावरण में काम नहीं करेगा⚠️

इस तथ्य के बावजूद कि `document.all` एक सरणी जैसी वस्तु है और यह पृष्ठ में DOM नोड्स तक पहुँच प्रदान करता है, यह` टाइपोफ` फ़ंक्शन को `अपरिभाषित` के रूप में प्रतिक्रिया देता है।

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

इसी समय, ` document.all`` अपरिभाषित ` के बराबर नहीं है।

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

But at the same time:

```js
document.all == null; // -> true
```

### 💡 व्याख्या:

> `document.all` विशेष रूप से IE के पुराने संस्करणों के साथ DOM तत्वों को एक्सेस करने का एक तरीका हुआ करता था। हालांकि यह कभी भी एक मानक नहीं रहा है, लेकिन इसका इस्तेमाल वृद्धावस्था के जेएस कोड में किया जाता था। जब मानक नए एपीआई (जैसे `document.getElementById`) के साथ आगे बढ़ा, तो यह एपीआई कॉल अप्रचलित हो गई और मानक समिति को तय करना था कि इसके साथ क्या करना है। इसके व्यापक उपयोग के कारण उन्होंने एपीआई रखने का फैसला किया, लेकिन जावास्क्रिप्ट विनिर्देश के विलफुल उल्लंघन का परिचय दिया।
> इसका उपयोग करने पर कारण `झूठ` का जवाब देता है [Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison) with `undefined` while `true` when using the [Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) स्पष्ट रूप से अनुमति देता है कि विनिर्देश के विलफुल उल्लंघन के कारण है।
>
> &mdash; [“Obsolete features - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) at WhatWG - HTML spec
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) at YDKJS - Types & Grammar

## न्यूनतम मान शून्य से अधिक है

`Number.MIN_VALUE` सबसे छोटी संख्या है, जो शून्य से अधिक है:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 व्याख्या:

> ` नंबर .IN_VALUE`` 5e-324 ` है, यानी सबसे छोटी धनात्मक संख्या जिसे फ्लोट प्रिसिजन के भीतर दर्शाया जा सकता है, यानी कि आप शून्य के जितना करीब हो सकते हैं। यह सबसे अच्छे रिज़ॉल्यूशन को परिभाषित करता है जो तैरता है जो आपको दे सकता है
>
> अब कुल मिलाकर सबसे छोटा मूल्य है `नंबर.नैगेटिव_इनफिनिटी` हालांकि यह एक सख्त अर्थ में वास्तव में संख्यात्मक नहीं है।
>
> &mdash; [“Why is `0` less than `Number.MIN_VALUE` in JavaScript?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) at StackOverflow

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## फंक्शन कोई फंक्शन नहीं है

> ⚠️ V8 v5.5 या निम्न में मौजूद बग (Node.js <= 7)⚠️

आप सभी को पता है कि कष्टप्रद _undefined एक function_ नहीं है, लेकिन इस बारे में क्या?

```js
// Declare a class which extends null
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 व्याख्या:

यह स्पेसिफिकेशन का हिस्सा नहीं है। यह केवल एक बग है जिसे अब ठीक कर दिया गया है, इसलिए भविष्य में इसके साथ कोई समस्या नहीं होनी चाहिए।

## Adding arrays

यदि आप दो सरणियों को जोड़ने का प्रयास करते हैं तो क्या होगा?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 व्याख्या:

संघात होता है। चरण-दर-चरण, ऐसा दिखता है:

```js
[1, 2, 3] +
  [4, 5, 6][
    // call toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concatenation
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## सरणी में अल्पविराम

आपने 4 खाली तत्वों के साथ एक सरणी बनाई है। सभी के बावजूद, आपको अल्पविराम के कारण तीन तत्वों के साथ एक सरणी मिलेगी:

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 व्याख्या:

> **Trailing commas** (कभी-कभी "अंतिम कॉमा" कहा जाता है) जावास्क्रिप्ट कोड में नए तत्वों, मापदंडों या गुणों को जोड़ते समय उपयोगी हो सकता है। यदि आप एक नई संपत्ति जोड़ना चाहते हैं, तो आप बस पिछली पंक्ति को संशोधित किए बिना एक नई रेखा जोड़ सकते हैं यदि वह रेखा पहले से ही एक अल्पविराम का उपयोग करती है। इससे संस्करण-नियंत्रण अलग-अलग हो जाता है और एडिटिंग कोड कम परेशानी वाला हो सकता है।
>
> &mdash; [Trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) at MDN

## ऐरे समानता एक राक्षस है

JS में Array समानता एक राक्षस है, जैसा कि आप नीचे देख सकते हैं:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 व्याख्या:

आपको उपरोक्त उदाहरणों के लिए बहुत सावधानी से देखना चाहिए! व्यवहार अनुभाग में वर्णित है[**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) of the specification.

## `undefined` and `Number`

यदि हम `नंबर` कंस्ट्रक्टर में कोई तर्क नहीं देते हैं, तो हम` 0` प्राप्त करेंगे। मान 'अपरिभाषित' को औपचारिक तर्कों के लिए सौंपा गया है जब कोई वास्तविक तर्क नहीं हैं, तो आप उम्मीद कर सकते हैं कि बिना तर्क के `संख्या` अपने पैरामीटर के मान के रूप में`अपरिभाषित 'लेता है। हालाँकि, जब हम`अपरिभाषित` पास करते हैं, तो हम` NaN` प्राप्त करेंगे।

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 व्याख्या:

विनिर्देश के अनुसार:

1. यदि इस फ़ंक्शन के आह्वान पर कोई तर्क नहीं दिया गया, तो `n` को` + 0` होने दें।
2. और, चलो `n` हो? `ToNumber (मान)`।
3. `अपरिभाषित` के मामले में,`ToNumber (अपरिभाषित)`को` NaN` वापस करना चाहिए।

Here's the corresponding section:

- [**20.1.1** The Number Constructor](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` एक बुरा आदमी है

`parseInt` अपने quirks द्वारा प्रसिद्ध है:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 व्याख्या:** ऐसा इसलिए होता है क्योंकि `parseInt` चरित्र-दर-चरित्र को तब तक जारी रखेगा, जब तक कि वह एक चरित्र को हिट न कर दे, जो उसे पता नहीं है। `F` in` 'f * ck'` हेक्साडेसिमल अंक `15` है।

पूर्णांक के लिए `इन्फिनिटी` को पार्स करना कुछ…

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

Be careful with parsing `null` too:

```js
parseInt(null, 24); // -> 23
```

**💡 व्याख्या:**

> यह `null` को स्ट्रिंग` `null” ` में परिवर्तित कर रहा है और इसे परिवर्तित करने का प्रयास कर रहा है। 23 के माध्यम से मूलांक 0 के लिए, ऐसे कोई अंक नहीं हैं जो इसे रूपांतरित कर सकते हैं, इसलिए यह NaN लौटाता है। 24 में, 14 वें अक्षर `` एन '', को अंक प्रणाली में जोड़ा जाता है। 31 पर, 21 वें अक्षर `` यू '' को जोड़ा जाता है और पूरे स्ट्रिंग को डिकोड किया जा सकता है। 37 पर अब कोई वैध अंक सेट नहीं है जो उत्पन्न किया जा सकता है और  `NaN` को लौटा दिया जाता है।
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) at StackOverflow

अष्टक के बारे में मत भूलना:

```js
parseInt("06"); // 6
parseInt("08"); // 8 if support ECMAScript 5
parseInt("08"); // 0 if not support ECMAScript 5
```

**💡 व्याख्या:**यदि इनपुट स्ट्रिंग "0" से शुरू होती है, तो मूलांक आठ (अष्टक) या 10 (दशमलव) है। वास्तव में जो मूलांक चुना गया है वह कार्यान्वयन-निर्भर है। ECMAScript 5 निर्दिष्ट करता है कि 10 (दशमलव) का उपयोग किया जाता है, लेकिन सभी ब्राउज़र अभी तक इसका समर्थन नहीं करते हैं। इस कारण से `parseInt` का उपयोग करते समय हमेशा एक मूलांक निर्दिष्ट करें।

`parseInt` always convert input to string:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

फ़्लोटिंग पॉइंट मानों को पार्स करते समय सावधान रहें

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 व्याख्या:** `ParseInt` एक स्ट्रिंग तर्क लेता है और निर्दिष्ट मूलांक का पूर्णांक देता है। `ParseInt` भी स्ट्रिंग पैरामीटर में पहले गैर-अंक के बाद और सहित कुछ भी स्ट्रिप्स। `0.000001` को स्ट्रिंग में परिवर्तित किया जाता है `0.000001` और ` पार्सेइंट`` 0 ` देता है। जब `0.0000001` को एक स्ट्रिंग में परिवर्तित किया जाता है तो इसे`'1e-7' 'के रूप में माना जाता है और इसलिए`parseInt`` 1` देता है। `1 / 1999999` की व्याख्या` 5.00000250000125e-7` और `पार्सेइंट`` 5` के रूप में की जाती है।

## `सत्य` और` असत्य` के साथ गणित

चलो कुछ गणित करते हैं:

```js
true +
  true(
    // -> 2
    true + true
  ) *
    (true + true) -
  true; // -> 3
```

हममम ... 🤔

### 💡 व्याख्या:

हम मानों को 'संख्या' निर्माता के साथ संख्याओं में भिन्न कर सकते हैं। यह काफी स्पष्ट है कि ` सच`` 1 ` के लिए मजबूर किया जाएगा:

```js
Number(true); // -> 1
```

यूनीरी प्लस ऑपरेटर अपने मूल्य को एक संख्या में बदलने का प्रयास करता है। यह पूर्णांकों और फ़्लोट्स के स्ट्रिंग अभ्यावेदन को परिवर्तित कर सकता है, साथ ही साथ गैर-स्ट्रिंग मान `सत्य`,` असत्य`, और `अशक्त`। यदि यह किसी विशेष मूल्य को पार्स नहीं कर सकता है, तो यह `NaN` का मूल्यांकन करेगा। इसका मतलब है कि हम `सच` को` 1` आसान कर सकते हैं:

```js
+true; // -> 1
```

जब आप जोड़ या गुणा कर रहे होते हैं, तो `ToNumber` विधि लागू होती है। विनिर्देश के अनुसार, यह विधि वापस आती है:

> If `argument` is **true**, return **1**. If `argument` is **false**, return **+0**.

इसलिए हम बूलियन मूल्यों को नियमित संख्या के रूप में जोड़ सकते हैं और सही परिणाम प्राप्त कर सकते हैं।

संगत अनुभाग:

- [**12.5.6** Unary `+` Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## HTML टिप्पणियाँ जावास्क्रिप्ट में मान्य हैं

आप प्रभावित होंगे, लेकिन `<! -` (जिसे HTML टिप्पणी के रूप में जाना जाता है) जावास्क्रिप्ट में एक मान्य टिप्पणी है।

```js
// valid comment
<!-- valid comment too
```

### 💡 व्याख्या:

Impressed? HTML जैसी टिप्पणियों का उद्देश्य उन ब्राउज़रों को अनुमति देना था जो समझ में नहीं आते थे`<script>` सुंदर ढंग से नीचा दिखाने के लिए टैग। ये ब्राउज़र, उदा। नेटस्केप 1.x अब लोकप्रिय नहीं हैं। तो अब आपके स्क्रिप्ट टैग में HTML कमेंट्स डालने का कोई मतलब नहीं है।

चूंकि Node.js V8 इंजन पर आधारित है, इसलिए HTML- जैसी टिप्पणियां Node.js रनटाइम द्वारा भी समर्थित हैं। इसके अलावा, वे विनिर्देश का एक हिस्सा हैं:

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` is ~~not~~ a number

Type of `NaN` is a `'number'`:

```js
typeof NaN; // -> 'number'
```

### 💡 व्याख्या:

व्याख्याs of how `typeof` and `instanceof` operators work:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` and `null` are objects

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// however
null instanceof Object; // false
```

### 💡 व्याख्या:

विनिर्देशन के इस भाग में `टाइपोफ़ 'ऑपरेटर के व्यवहार को परिभाषित किया गया है:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

विनिर्देशन के अनुसार, `टाइपऑफ़` ऑपरेटर [तालिका 35:` टाइपोफ़ `ऑपरेटर परिणाम] (https://www.ecma-international.org/ecma-262/#table-35) के अनुसार एक स्ट्रिंग लौटाता है। `Null`, साधारण, मानक विदेशी और गैर-मानक विदेशी वस्तुओं के लिए, जो`[[कॉल]]`को लागू नहीं करते हैं, यह स्ट्रिंग` `ऑब्जेक्ट`` लौटाता है।

हालाँकि, आप `toString` विधि का उपयोग करके किसी ऑब्जेक्ट के प्रकार की जाँच कर सकते हैं।

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## Magically increasing numbers

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 व्याख्या:

यह बाइनरी फ्लोटिंग-पॉइंट अंकगणित के लिए IEEE 754-2008 मानक के कारण होता है। इस पैमाने पर, यह निकटतम सम संख्या में गोल होता है। अधिक पढ़ें:

- [**6.1.6** The Number Type](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) on Wikipedia

## Precision of `0.1 + 0.2`

A well-known joke. An addition of `0.1` and `0.2` is deadly precise:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 व्याख्या:

The answer for the [”Is floating point math broken?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) question on StackOverflow:

> आपके कार्यक्रम में स्थिरांक `0.2` और` 0.3` भी उनके वास्तविक मूल्यों के सन्निकटन होंगे। ऐसा होता है कि निकटतम `डबल` से` 0.2` तर्कसंगत संख्या `0.2` से बड़ा है, लेकिन निकटतम` डबल` से `0.3` तर्कसंगत संख्या` 0.3` से छोटा है। `0.1` और` 0.2` हवाओं का योग तर्कसंगत संख्या `0.3` से बड़ा है और इसलिए आपके कोड में निरंतरता से असहमत है।

यह समस्या इतनी ज्ञात है कि यहां तक ​​कि एक वेबसाइट भी है जिसका नाम [0.30000000000000004.com] (http://0.30000000000000004.com/) है। यह हर भाषा में होता है जो फ़्लोटिंग पॉइंट गणित का उपयोग करता है, न कि केवल जावास्क्रिप्ट।

## पैचिंग नंबर

आप रैपर ऑब्जेक्ट्स को `नंबर` या` स्ट्रिंग` जैसे तरीकों से जोड़ सकते हैं।

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 व्याख्या:

जाहिर है, आप जावास्क्रिप्ट में किसी भी अन्य ऑब्जेक्ट की तरह `नंबर` ऑब्जेक्ट का विस्तार कर सकते हैं। हालाँकि, यह अनुशंसित नहीं है यदि परिभाषित पद्धति का व्यवहार विनिर्देश का हिस्सा नहीं है। यहाँ `नंबर` की संपत्तियों की सूची दी गई है:

- [**20.1** Number Objects](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## Comparison of three numbers

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 व्याख्या:

इस तरह से काम क्यों करता है? खैर, समस्या एक अभिव्यक्ति के पहले भाग में है। यहां देखिए यह कैसे काम करता है:

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

हम इसे ठीक कर सकते हैं _Greater than or equal operator (`>=`)_:

```js
3 > 2 >= 1; // true
```

विनिर्देश में रिलेशनल ऑपरेटरों के बारे में अधिक पढ़ें:

- [**12.10** संबंधपरक संकारक](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## मजेदार गणित

अक्सर जावास्क्रिप्ट में अंकगणितीय संचालन के परिणाम काफी अप्रत्याशित हो सकते हैं। इन उदाहरणों पर विचार करें:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 व्याख्या:

पहले चार उदाहरणों में क्या हो रहा है? जावास्क्रिप्ट में अतिरिक्त समझने के लिए यहां एक छोटी तालिका दी गई है:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

अन्य उदाहरणों के बारे में क्या? एक `ToPrimitive` और` ToString` तरीकों को इसके अलावा `[]` और `{} के लिए निहित किया जा रहा है। विनिर्देश में मूल्यांकन प्रक्रिया के बारे में और पढ़ें:

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

## RegExps का जोड़

क्या आप जानते हैं कि आप इस तरह से नंबर जोड़ सकते हैं?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 व्याख्या:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## स्ट्रिंग्स `स्ट्रिंग` के उदाहरण नहीं हैं

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 व्याख्या:

`स्ट्रिंग` कंस्ट्रक्टर एक स्ट्रिंग लौटाता है:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

Let's try with a `new`:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

वस्तु? वह क्या है?

```js
new String("str"); // -> [String: 'str']
```

विनिर्देश में स्ट्रिंग निर्माता के बारे में अधिक जानकारी:

- [**21.1.1** The String Constructor](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## बैकटिक्स के साथ कॉलिंग फ़ंक्शन

आइए एक फ़ंक्शन की घोषणा करते हैं जो कंसोल में सभी पैराम्स को लॉग करता है:

```js
function f(...args) {
  return args;
}
```

कोई शक नहीं, आप जानते हैं कि आप इस फ़ंक्शन को इस तरह से कॉल कर सकते हैं:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

लेकिन क्या आप जानते हैं कि आप किसी भी फंक्शन को बैकटिक्स कह सकते हैं।

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 व्याख्या:

यदि आप _Tagged टेम्पलेट शाब्दिक_ से परिचित हैं, तो यह बिल्कुल भी जादू नहीं है। ऊपर दिए गए उदाहरण में, `f` फ़ंक्शन टेम्प्लेट शाब्दिक के लिए एक टैग है। टेम्प्लेट शाब्दिक से पहले टैग आपको फ़ंक्शन के साथ टेम्प्लेट शाब्दिकता को पार्स करने की अनुमति देता है। टैग फ़ंक्शन के पहले तर्क में स्ट्रिंग मानों की एक सरणी होती है। शेष तर्क भावों से संबंधित हैं। उदाहरण:

```js
function template(strings, ...keys) {
  // do something with strings and keys…
}
```

यह [जादू के पीछे] (http://mxstbr.blog/2016/11/styled-compenders-magic-explained/) प्रसिद्ध पुस्तकालय जिसे [led स्टाइल-कंपोनेंट्स] कहा जाता है (https://www.styled-compenders.com) /), जो प्रतिक्रिया समुदाय में लोकप्रिय है।

विनिर्देशन के लिए लिंक:

- [**12.3.7** Tagged Templates](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## पुकार पुकार पुकार

> Found by [@cramforce](http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 व्याख्या:

ध्यान दें, यह आपके दिमाग को तोड़ सकता है! अपने सिर में इस कोड को पुन: उत्पन्न करने का प्रयास करें: हम `लागू` विधि का उपयोग करके` कॉल` विधि लागू कर रहे हैं। अधिक पढ़ें:

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## A `constructor` property

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 व्याख्या:

आइए इस उदाहरण पर विचार करें चरण-दर-चरण:

```js
// Declare a new constant which is a string 'constructor'
const c = "constructor";

// c is a string
c; // -> 'constructor'

// Getting a constructor of string
c[c]; // -> [Function: String]

// Getting a constructor of constructor
c[c][c]; // -> [Function: Function]

// Call the Function constructor and pass
// the body of new function as an argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// And then call this anonymous function
// The result is console-logging a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

एक `Object.prototyp.constructor` उदाहरण ऑब्जेक्ट बनाने वाले` Object` कंस्ट्रक्टर फ़ंक्शन का संदर्भ देता है। स्ट्रिंग के साथ मामले में यह `स्ट्रिंग` है, संख्या के मामले में यह` नंबर` और इसी तरह है।

- एमडीएन के लिए [`Object.prototyp.constructor`] (https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
- [** 19.1.3.1 ** Object.prototype.constructor] (https://www.ecma-international.org/ecma-262/#sec-object.prototyp.constructor)

## वस्तु की संपत्ति की कुंजी के रूप में वस्तु

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 व्याख्या:

यह काम क्यों करता है? यहां हम एक _Computed संपत्ति name_ का उपयोग कर रहे हैं। जब आप उन कोष्ठकों के बीच एक वस्तु को पास करते हैं, तो यह एक स्ट्रिंग के लिए आपत्ति करता है, इसलिए हमें संपत्ति कुंजी `'[ऑब्जेक्ट ऑब्जेक्ट]` `और मूल्य` {} `मिलता है।

हम इस तरह "कोष्ठक नरक" बना सकते हैं:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

वस्तु शाब्दिक के बारे में यहाँ और अधिक पढ़ें:

- एमडीएन पर (ऑब्जेक्ट इनिशलाइज़र] (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Oference/Object_initializer)
- [** १२.२.६ ** वस्तु इनिशियलाइज़र] (http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## प्रोटोटाइपिंग को `__proto__` के साथ एक्सेस करना

जैसा कि हम जानते हैं, आदिमों के प्रोटोटाइप नहीं हैं। हालांकि, अगर हम आदिम के लिए `__proto__` का मान प्राप्त करने का प्रयास करते हैं, तो हमें यह मिलेगा:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 व्याख्या:

ऐसा इसलिए होता है क्योंकि जब किसी चीज़ का प्रोटोटाइप नहीं होता है, तो इसे `ToObject` मेथड का इस्तेमाल करके रैपर ऑब्जेक्ट में लपेट दिया जाएगा। तो, चरण-दर-चरण:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

यहाँ `__proto__` के बारे में अधिक जानकारी है:

- [** B.2.2.1 ** Object.prototype। ** proto **] (https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [** 7.1.13 ** ToObject (`तर्क`)] (https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `$ {{वस्तु}}` ``

नीचे दिए गए अभिव्यक्ति का परिणाम क्या है?

```js
`${{ Object }}`;
```

The answer is:

```js
// -> '[object Object]'
```

### 💡 व्याख्या:

हमने एक ऑब्जेक्ट को एक संपत्ति के साथ परिभाषित किया है `Object` का उपयोग करके _Shorthand संपत्ति अंकन_:

`` `Js { वस्तु वस्तु; } `` `

फिर हमने इस ऑब्जेक्ट को टेम्पलेट शाब्दिक में पास कर दिया है, इसलिए उस ऑब्जेक्ट के लिए `toString` विधि कॉल करता है। इसलिए हमें स्ट्रिंग मिलती है `'[ऑब्जेक्ट ऑब्जेक्ट]'`।

- [** १२.२.९ ** टेम्पलेट साहित्य] (https://www.ecma-international.org/ecma-262/#sec-template-literals)
- एमडीएन पर (ऑब्जेक्ट इनिशलाइज़र] (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Oference/Object_initializer)

## डिफ़ॉल्ट मानों के साथ विनाशकारी

इस उदाहरण पर विचार करें:

```js
let x,
  { x: y = 1 } = { x };
y;
```

उपरोक्त उदाहरण एक साक्षात्कार के लिए एक महान कार्य है। `Y` का मूल्य क्या है? उत्तर है:

```js
// -> 1
```

### 💡 व्याख्या:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

ऊपर के उदाहरण के साथ:

1. हम `x` को बिना किसी मूल्य के घोषित करते हैं, इसलिए यह` अपरिभाषित` है।
2. फिर हम `x` का मान ऑब्जेक्ट प्रॉपर्टी` x` में पैक करते हैं।
3. फिर हम विध्वंस का उपयोग करके `x` का मान निकालते हैं और` y` को असाइन करना चाहते हैं। यदि मान परिभाषित नहीं है, तो हम डिफ़ॉल्ट मान के रूप में `1` का उपयोग करने जा रहे हैं।
4. `y` का मान लौटाएँ।

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## डॉट्स और फैल रहा है

ऐरे के प्रसार के साथ दिलचस्प उदाहरणों की रचना की जा सकती है। इस पर विचार करो:

```js
[...[..."..."]].length; // -> 3
```

### 💡 व्याख्या:

क्यों `3`? जब हम [स्प्रेड ऑपरेटर] (http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer) का उपयोग करते हैं, तो '@@ इट्रेटर' विधि को कहा जाता है, और लौटा हुआ पुनरावृत्ति है मूल्यों को पुनरावृत्त करने के लिए उपयोग किया जाता है। स्ट्रिंग के लिए डिफ़ॉल्ट पुनरावृत्ति एक स्ट्रिंग को वर्णों में फैलाता है। फैलने के बाद, हम इन पात्रों को एक सरणी में पैक करते हैं। फिर हम इस सरणी को फिर से फैलाते हैं और इसे वापस सरणी में पैक करते हैं।

A `'...'` स्ट्रिंग में तीन ``वर्ण होते हैं, इसलिए परिणामी सरणी की लंबाई`3` है।

अब, चरण-दर-चरण:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

जाहिर है, हम सरणी के तत्वों को जितनी बार चाहें उतनी बार फैला और लपेट सकते हैं:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## लेबल

कई प्रोग्रामर जावास्क्रिप्ट में लेबल के बारे में नहीं जानते हैं। वे दिलचस्प हैं:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 व्याख्या:

लेबल स्टेटमेंट का उपयोग `ब्रेक` या` जारी` स्टेटमेंट के साथ किया जाता है। आप लूप की पहचान करने के लिए एक लेबल का उपयोग कर सकते हैं, और फिर प्रोग्राम को लूप को बाधित करना चाहिए या इसके निष्पादन को जारी रखने के लिए `ब्रेक` या` जारी` बयान का उपयोग करें।

ऊपर दिए गए उदाहरण में, हम एक लेबल `foo` की पहचान करते हैं। उसके बाद `कंसोल.लॉग ('पहले');` निष्पादित होता है और फिर हम निष्पादन को बाधित करते हैं।

जावास्क्रिप्ट में लेबल के बारे में और पढ़ें:

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## Nested labels

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 व्याख्या:

पिछले उदाहरणों के समान, इन लिंक का अनुसरण करें:

- [** १२.१६ ** कोमा संचालक (`,`)] (https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [** 13.13 ** लेबल किए गए विवरण] (https://tc39.github.io/ecma262/#sec-labelled-statements)
- [लेबल किए गए कथन] (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) MDN पर

## कपटी `कोशिश..चेक`

यह अभिव्यक्ति क्या लौटेगी? `2` या` 3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

उत्तर `3` है। आश्चर्य चकित?

### # व्याख्या:

- [** 13.15 ** द `कोशिश` स्टेटमेंट] (https://www.ecma-international.org/ecma-262/#sec-try-statement)

## क्या यह कई विरासत है?

नीचे दिए गए उदाहरण पर एक नज़र डालें:

```js
new class F extends (String, Array) {}(); // -> F []
```

क्या यह एक बहु विरासत है? नहीं।

### # व्याख्या:

दिलचस्प हिस्सा `फैली` खंड (`(स्ट्रिंग, सरणी)` का मूल्य है। ग्रुपिंग ऑपरेटर हमेशा अपना अंतिम तर्क देता है, इसलिए `(स्ट्रिंग, एरे)` वास्तव में सिर्फ `एरे` है। इसका मतलब है कि हमने सिर्फ एक वर्ग बनाया है जो `एरे` का विस्तार करता है।

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## एक जनरेटर जो खुद उपजता है

एक जनरेटर के इस उदाहरण पर विचार करें जो स्वयं उपज देता है:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

जैसा कि आप देख सकते हैं, लौटाया गया मान एक वस्तु है जिसका ` मान`` एफ ` के बराबर है। उस मामले में, हम ऐसा कुछ कर सकते हैं:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 व्याख्या:

यह समझने के लिए कि यह इस तरह क्यों काम करता है, विनिर्देश के इन वर्गों को पढ़ें:

- [** २५ ** नियंत्रण अमूर्त वस्तुएं] (https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [** २५.३ ** जेनरेटर ऑब्जेक्ट] (https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## कक्षा का एक वर्ग

इस ओफ़्सेटेड सिंटैक्स प्लेइंग पर विचार करें:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

ऐसा लगता है जैसे हम क्लास के अंदर क्लास घोषित कर रहे हैं। एक त्रुटि होनी चाहिए, हालांकि, हमें स्ट्रिंग '' ऑब्जेक्ट '' मिलता है।

### # व्याख्या:

ECMAScript 5 युग के बाद से _keywords_ को _property names_ के रूप में अनुमति दी गई है। तो इस सरल वस्तु उदाहरण के रूप में इसके बारे में सोचो:

```js
const foo = {
  class: function() {}
};
```

और ईएस 6 मानकीकृत शॉर्टहैंड विधि परिभाषाएं। साथ ही, कक्षाएं अनाम हो सकती हैं। इसलिए यदि हम ड्रॉप करते हैं `: फ़ंक्शन` भाग, हम प्राप्त करने जा रहे हैं:

```js
class {
  class() {}
}
```

डिफ़ॉल्ट वर्ग का परिणाम हमेशा एक साधारण वस्तु होती है। और इसके टाइपोफ को `ऑब्जेक्ट'` वापस करना चाहिए।

यहाँ और पढ़ें:

- [** १४.३ ** विधि परिभाषाएँ] (https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [** १४.५ ** कक्षा परिभाषाएँ] (https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## गैर-सहकर्मी वस्तुएं

प्रसिद्ध प्रतीकों के साथ, प्रकार की जबरदस्ती से छुटकारा पाने का एक तरीका है। जरा देखो तो:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

अब हम इसका उपयोग इस तरह कर सकते हैं:

```js
// objects
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// strings
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// numbers
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 व्याख्या:

- [सेर्गेई रुबनोव द्वारा एक तस्वीर] (https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [** ६.१.५.१ ** अच्छी तरह से ज्ञात प्रतीक] (https://www.ecma-international.org/ecma-262/#sec-well-ogn-symbols)

## मुश्किल तीर कार्य

नीचे दिए गए उदाहरण पर विचार करें:

```js
let f = () => 10;
f(); // -> 10
```

ठीक है, ठीक है, लेकिन इस बारे में क्या:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 व्याख्या:

आप `अपरिभाषित` के बजाय`{}`की उम्मीद कर सकते हैं। ऐसा इसलिए है क्योंकि घुंघराले ब्रेसिज़ तीर फ़ंक्शन के सिंटैक्स का हिस्सा हैं, इसलिए `f` अपरिभाषित वापस आ जाएगा। हालांकि, ब्रैकेट के साथ रिटर्न वैल्यू को संलग्न करके, तीर फ़ंक्शन से सीधे `{}` ऑब्जेक्ट को वापस करना संभव है।

```js
let f = () => ({});
f(); // -> {}
```

## एरो फ़ंक्शंस एक निर्माता नहीं हो सकता है

नीचे दिए गए उदाहरण पर विचार करें:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

अब, एक तीर फ़ंक्शन के साथ ऐसा करने का प्रयास करें:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 व्याख्या:

एरो फ़ंक्शंस को कंस्ट्रक्टर के रूप में इस्तेमाल नहीं किया जा सकता है और नए के साथ उपयोग किए जाने पर एक त्रुटि होगी। क्योंकि एक शाब्दिक `यह` है, और एक` प्रोटोटाइप` संपत्ति नहीं है, इसलिए यह बहुत मतलब नहीं होगा।

## `तर्क` और तीर कार्य

नीचे दिए गए उदाहरण पर विचार करें:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

अब, एक तीर फ़ंक्शन के साथ ऐसा करने का प्रयास करें:

`` `Js let f = () => तर्क; च ( "एक"); // -> अनट्रेक्टेड रेफरेंस: तर्क को परिभाषित नहीं किया गया है `` `

### # व्याख्या:

एरो फ़ंक्शंस शॉर्ट और लेक्सिकल `this` होने पर ध्यान देने के साथ नियमित फ़ंक्शंस का एक हल्का संस्करण है। उसी समय एरो फ़ंक्शंस `आर्ग्यूमेंट्स` ऑब्जेक्ट के लिए बाइंडिंग प्रदान नहीं करते हैं। एक वैध विकल्प के रूप में एक ही परिणाम प्राप्त करने के लिए `बाकी मापदंडों` का उपयोग करें:

```js
let f = (...args) => args;
f("a");
```

- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) at MDN.

## मुश्किल वापसी

`वापसी` बयान भी मुश्किल है। इस पर विचार करो:

```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```

### 💡 व्याख्या:

`वापसी` और लौटी हुई अभिव्यक्ति एक ही पंक्ति में होनी चाहिए:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

यह एक अवधारणा के कारण है जिसे स्वचालित अर्धविराम सम्मिलन कहा जाता है, जो स्वचालित रूप से अधिकांश न्यूक्लियर के बाद अर्धविराम सम्मिलित करता है। पहले उदाहरण में, `रिटर्न` स्टेटमेंट और ऑब्जेक्ट शाब्दिक के बीच एक अर्धविराम डाला जाता है, इसलिए फ़ंक्शन` अपरिभाषित` देता है और ऑब्जेक्ट शाब्दिक का कभी मूल्यांकन नहीं किया जाता है।

- [** 11.9.1 ** स्वचालित अर्धविराम सम्मिलन के नियम] (https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [** 13.10 ** द `रिटर्न` स्टेटमेंट] (https://www.ecma-international.org/ecma-262/#sec-return-statement)

## ऑब्जेक्ट पर कार्य असाइन करना

```js
var foo = {n: 1};
var bar = foo;

foo.x = foo = {n: 2};

foo.x // -> undefined
foo   // -> {n: 2}
bar   // -> {n: 1, x: {n: 2}}
```

दाएं से बाएं, `{n: 2}` को फू को सौंपा गया है, और इस असाइनमेंट का परिणाम `{n: 2}` को foo.x को सौंपा गया है, इसीलिए बार `{n: 1, x: {है n: 2}} `के रूप में बार फू के लिए एक संदर्भ है। लेकिन क्यों foo.x अपरिभाषित है जबकि bar.x नहीं है?

### 💡 व्याख्या:

फू और बार एक ही ऑब्जेक्ट को संदर्भित करते हैं `{n: 1}`, और लवलीन को असाइनमेंट से पहले हल किया जाता है। `foo = {n: 2}` एक नई वस्तु बना रहा है, और इसलिए उस नई वस्तु को संदर्भित करने के लिए foo अपडेट किया गया है। यहाँ चाल को 'foo.x = ...' में foo किया गया है क्योंकि एक लैवल्यू को पहले से हल किया गया था और अभी भी पुराने `foo = {n: 1}` ऑब्जेक्ट को संदर्भित करता है और इसे x मान जोड़कर अपडेट करें। उस श्रृंखला असाइनमेंट के बाद, बार अभी भी पुराने फू ऑब्जेक्ट को संदर्भित करता है, लेकिन फू नए `{n: 2}` ऑब्जेक्ट को संदर्भित करता है, जहां एक्स मौजूद नहीं है।

यह इसके बराबर है:

```js
var foo = {n: 1};
var bar = foo;

foo = {n: 2} // -> {n: 2}
bar.x = foo // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## सरणियों के साथ ऑब्जेक्ट गुण तक पहुँचना

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

छद्म बहुआयामी सरणियों के बारे में क्या?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 व्याख्या:

कोष्ठक `[]` परिचालक उत्तीर्ण अभिव्यक्ति को `स्ट्रींग` का उपयोग करके परिवर्तित करता है। स्ट्रिंग में एक तत्व तत्व को परिवर्तित करना स्ट्रिंग में निहित तत्व को परिवर्तित करने के लिए एक समान है:

```js
["property"].toString(); // -> 'property'
```

## Null and Relational Operators

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 व्याख्या:

लंबी कहानी छोटी, यदि ` शून्य`` 0 ` से कम है, तो `झूठा` है, तो` शून्य` = 0` `सत्य` है। इसके लिए [यहाँ] (https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274) की गहन व्याख्या पढ़ें।

## `Number.toFixed ()` विभिन्न संख्याएँ प्रदर्शित करता है

`Number.toFixed ()` विभिन्न ब्राउज़रों में थोड़ा अजीब व्यवहार कर सकता है। इस उदाहरण को देखें:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 व्याख्या:

हालांकि आपकी पहली वृत्ति यह हो सकती है कि IE11 सही है और फ़ायरफ़ॉक्स / क्रोम गलत है, वास्तविकता यह है कि फ़ायरफ़ॉक्स / क्रोम अधिक सीधे संख्याओं के लिए मानक मान रहे हैं (IEEE-754 फ़्लोटिंग पॉइंट), जबकि IE11 उन्हें पूरी तरह से अवज्ञा करता है (जो शायद है ) स्पष्ट परिणाम देने का प्रयास।

आप देख सकते हैं कि कुछ त्वरित परीक्षणों के साथ ऐसा क्यों होता है:

```js
// 5 नीचे गोलाई के विषम परिणाम की पुष्टि करें
(0.7875).toFixed(3); // -> 0.787
// It looks like it's just a 5 when you expand to the
// limits of 64-bit (double-precision) float accuracy
(0.7875).toFixed(14); // -> 0.78750000000000
// But what if you go beyond the limit?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

फ़्लोटिंग पॉइंट नंबरों को आंतरिक रूप से दशमलव अंकों की एक सूची के रूप में संग्रहीत नहीं किया जाता है, लेकिन एक अधिक जटिल कार्यप्रणाली के माध्यम से जो छोटी अशुद्धि पैदा करता है जो आमतौर पर स्ट्रींग और इसी तरह की कॉल से गोल होते हैं, लेकिन वास्तव में आंतरिक रूप से मौजूद होते हैं।

इस मामले में, कि अंत में "5" वास्तव में एक सच के नीचे एक बहुत छोटा सा अंश था। किसी भी उचित लंबाई पर इसे 5 के रूप में प्रस्तुत करना ... लेकिन यह वास्तव में आंतरिक रूप से 5 नहीं है।

IE11, हालांकि, केवल (शून्य) मामले में भी अंत तक संलग्न शून्य के साथ मूल्य इनपुट की रिपोर्ट करेगा, क्योंकि यह हार्डवेयर सीमाओं से परेशानियों को कम करने के लिए मूल्य को जबरन गोल करना प्रतीत होता है।

संदर्भ के लिए देखें `नोट 2` ECMA-262 पर` toFixed` के लिए परिभाषा।

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` less than `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 व्याख्या:

- चार्ली हार्वे द्वारा Math.max () Math.min () से कम क्यों है? (Https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min)

## तुलना `null` से` 0` तक

निम्नलिखित अभिव्यक्तियाँ विरोधाभास का परिचय देती हैं:

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

`Null` न तो बराबर हो सकता है और न ही` 0` से अधिक, अगर `null> = 0` वास्तव में` true` है? (यह भी उसी तरह से कम के साथ काम करता है।)

### 💡 व्याख्या:

जिस तरह से इन तीनों भावों का मूल्यांकन किया जाता है, वे सभी भिन्न हैं और इस अप्रत्याशित व्यवहार के उत्पादन के लिए जिम्मेदार हैं।

सबसे पहले, अमूर्त समानता तुलना `null == 0`। आम तौर पर, यदि यह ऑपरेटर दोनों तरफ के मूल्यों की ठीक से तुलना नहीं कर सकता है, तो यह दोनों संख्याओं में परिवर्तित हो जाता है और संख्याओं की तुलना करता है। फिर, आप निम्न व्यवहार की अपेक्षा कर सकते हैं:

```js
// This is not what happens
(null == 0 + null) == +0;
0 == 0;
true;
```

हालांकि, कल्पना के एक करीबी पढ़ने के अनुसार, संख्या रूपांतरण वास्तव में उस तरफ नहीं होता है जो `अशक्त` या` अपरिभाषित` है। इसलिए, यदि आपके पास समान चिह्न के एक तरफ `null` है, तो दूसरी तरफ` true` वापस करने के लिए अभिव्यक्ति के लिए `null` या` अनिर्धारित` होना चाहिए। चूंकि यह मामला नहीं है, `झूठ` वापस आ गया है।

अगला, संबंधपरक तुलना `अशक्त> 0`। एल्गोरिथ्म यहाँ, अमूर्त समानता ऑपरेटर के विपरीत, _will_ एक संख्या के लिए `null` कन्वर्ट। इसलिए, हमें यह व्यवहार मिलता है:

```js
null > 0
+null = +0
0 > 0
false
```

अंत में, संबंधपरक तुलना `शून्य> = 0`। आप तर्क दे सकते हैं कि यह अभिव्यक्ति `शून्य> 0 का परिणाम होना चाहिए null == 0`; अगर ऐसा होता, तो उपरोक्त परिणामों का मतलब यह होगा कि यह भी `गलत` होगा। हालांकि, वास्तव में `> =` ऑपरेटर बहुत अलग तरीके से काम करता है, जो मूल रूप से `<` ऑपरेटर के विपरीत लेना है। क्योंकि ऊपर से ऑपरेटर से अधिक के साथ हमारा उदाहरण भी ऑपरेटर से कम के लिए है, इसका मतलब है कि इस अभिव्यक्ति का वास्तव में मूल्यांकन किया जाता है:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## समान परिवर्तनशील पुनर्वितरण

JS चरों को फिर से दिखाने की अनुमति देता है:

```js
a;
a;
// यह भी मान्य है
a, a;
```

सख्त मोड में भी काम करता है:

```js
var a, a, a;
var a;
var a;
```

### 💡 व्याख्या:

सभी परिभाषाओं को एक परिभाषा में मिला दिया गया है।

- [** 13.3.2 ** चर कथन] (https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## डिफ़ॉल्ट व्यवहार Array.prototyp.sort ()

कल्पना करें कि आपको संख्याओं की एक संख्या को क्रमबद्ध करना होगा।

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 व्याख्या:

डिफ़ॉल्ट सॉर्ट ऑर्डर तत्वों को स्ट्रिंग्स में परिवर्तित करने पर बनाया गया है, फिर UTF-16 कोड इकाइयों के उनके अनुक्रमों की तुलना करते हैं।

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### संकेत

यदि आप कुछ भी लेकिन स्ट्रिंग को क्रमबद्ध करने की कोशिश करते हैं, तो 'तुलना' पास करें।

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

# 📚 अन्य संसाधन

- [wtfjs.com] (http://wtfjs.com/) - वेब की भाषा के लिए उन विशेष अनियमितताओं, विसंगतियों और सीधे सादे दर्दभरे क्षणों का एक संग्रह।
- [वट] (https://www.destroyallsoftware.com/talks/wat) - कोडमश 2012 से गैरी बर्नहार्ट द्वारा एक बिजली की बात
- [क्या ... जावास्क्रिप्ट?] (Https://www.youtube.com/watch?v=2pL28CcEijU) - काइल सिम्पसन फॉरवर्ड 2 के लिए जावास्क्रिप्ट से "पागल को बाहर निकालने" का प्रयास करते हैं। वह क्लीनर, अधिक सुरुचिपूर्ण, अधिक पठनीय कोड बनाने में आपकी सहायता करना चाहता है, फिर लोगों को खुले स्रोत समुदाय में योगदान करने के लिए प्रेरित करता है।

# 🎓 License

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
```

## File: `README-it-it.md`
```markdown
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

`Number.MIN_VALUE` è il numero più piccolo rappresentabile, che è maggiore di zero:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 Spiegazione:

> `Number.MIN_VALUE` è `5e-324`, ovvero il più piccolo numero positivo che può essere rappresentato con precisione float, cioè quello che si può ottenere il più vicino possibile allo zero. Definisce la migliore risoluzione che un tipo di dato float può fornire.
>
> Il numero più piccolo in assoluto è `Number.NEGATIVE_INFINITY` nonostante non sia effettivamente un tipo numerico.
>
> &mdash; [“Why is `0` less than `Number.MIN_VALUE` in JavaScript?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) at StackOverflow

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## function non è una function

> ⚠️ Un bug presente in V8 v5.5 o inferiore (Node.js <=7) ⚠️

Tutti conoscerete la noiosa _undefined is not a function_, ma questa?

```js
// Dichiara una classe che estende null
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 Spiegazione:

Questo non è parte delle specifiche. È semplicemente un bug che ora è stato risolto, quindi non dovrebbero esserci problemi con questo in futuro.

## Sommare array

E se provassimo a sommare due array?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 Spiegazione:

Viene svolta la concatenazione. il procedimento step-by-step è il seguente:

```js
[1, 2, 3] +
  [4, 5, 6][
    // chiama toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concatenazione
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## "Trailing commas" in un array

Creiamo un array con 4 elementi vuoti. Nonostante ciò, si ottiene un array con 3 elementi, a causa delle "trailing commas":

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 Spiegazione:

> **Trailing commas** (anche chiamate "final commas") sono utili quando si aggiungono nuovi elementi, parametri o proprietà in codice JavaScript. Se si vuole aggiungere una nuova proprietà si può semplicemente aggiungere una nuova riga senza modificare quella precedente, se quella linea presenta già una virgola alla fine. Questo rende i diffs dei sistemi di version-control più puliti e modificare il codice è leggermente meno problematico.
>
> &mdash; [Trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) at MDN

## L'operatore di uguaglianza sugli array è un mostro

L'operatore di uguaglianza sugli array in JS è un mostro, come possiamo osservare sotto:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 Spiegazione:

Guarda attentamente gli esempi precedenti! Il comportamento viene spiegato nella sezione [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) delle specifiche.

## `undefined` e `Number`

Se non passiamo argomenti al costruttore di `Number`, otteniamo `0`. Il valore `undefined` viene assegnato di default quando non viene passato alcun valore, quindi possiamo aspettarci che `Number` senza parametri prenda `undefined` come valore del suo parametro. Invece quando inseriamo `undefined`, otteniamo `NaN`.

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 Spiegazione:

In base alle specifiche:

1. Se non viene passato alcun parametro durante l'invocazione della funzione, `n` viene valorizzato a `+0`.
2. Altrimenti, `n` sarà il risultato di `ToNumber(value)`.
3. Nel caso di `undefined`, `ToNumber(undefined)` deve restituire `NaN`.

Qui la sezione corrispondente:

- [**20.1.1** The Number Constructor](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` è bast\*\*do

`parseInt` è famoso per le sue stranezze:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 Spiegazione:** Questo avviene perchè `parseInt` continuerà a svolgere il parsing carattere per carattere fino a che non trova un carattere che non riconosce. La `f` in `'f*ck'` è la rappresentazione esadecimale di `15`.

Svolgere il parsing di `Infinity` a integer è qualcosa di...

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

Attenzione anche quando si svolge il parsing di `null`:

```js
parseInt(null, 24); // -> 23
```

**💡 Spiegazione:**

> Si sta convertendo `null` alla stringa `"null"` e provando poi a convertirla a sua volta. Per le radici da 0 a 23, non ci sono numerali per svolgere la conversione, quindi viene restituito NaN. A 24, `"n"`, la 14-esima lettera, viene aggiunta al sistema di numerazione. A 31, `"u"`, la 21-esima lettera, viene aggiunta e l'intera stringa può essere decodificata. A 37 non c'è più un valido insieme di numerazione che si può generare quindi viene restituito `NaN`.
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) at StackOverflow

Non dimentichiamoci del sistema di numerazione ottale:

```js
parseInt("06"); // 6
parseInt("08"); // 8 se  è presente il supporto a ECMAScript 5
parseInt("08"); // 0 se assente il supporto a ECMAScript 5
```

**💡 Spiegazione:** Se la stringa in input inizia con "0", la radice è 8 (octal) o 10 (decimal). Quale radice viene scelta dipende dall'implementazione. ECMAScript 5 specifica l'utilizzo di 10 (decimal), Ma non è ancora supportata da tutti i browser. Per questo motivo è sempre meglio specificare una radice quando si utilizza `parseInt`.

`parseInt` converte sempre l'input in stringa:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Attenzione quando si svolge il parsin di valori in virgola mobile:

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 Spiegazione:** `ParseInt` prende una stringa come argomento e restituisce un intero in base alla radice specificata. `ParseInt` inoltre elimina tutto ciò che viene dopo e incluso il primo carattere non numerico nella stringa passata come parametro. `0.000001` Viene convertito nella stringa `"0.000001"` e `parseInt` restituisce `0`. Quando `0.0000001` viene convertito in stringa viene interpretato come `"1e-7"` e quindi `parseInt` restituisce `1`. `1/1999999` viene interpretato come `5.00000250000125e-7` e `parseInt` restituisce `5`.

## Math con `true` e `false`

Facciamo un po' di calcoli:

```js
true -
  true +
  // -> 2
  (true + true) *
    (true + true) -
  true; // -> 3
```

Hmmm... 🤔

### 💡 Spiegazione:

Possiamo forzare dei valori a numeri utilizzando il costruttore di `Number`. È abbastanza ovvio che `true` venga forzato a `1`:

```js
Number(true); // -> 1
```

L'operatore unario `+` prova a convertire il suo valore in un numero. Può convertire la rappresentazione testuale di interie e float, così come i valori non testuali `true`, `false`, e `null`. Se non riesce a svolgere il parsing di un particolare valore, restuituirà `NaN`. Questo significa che possiamo forzare facilmente `true` a `1`:

```js
+true; // -> 1
```

Quando svolgiamo addizioni o moltiplicazioni, viene invocato il metodo `ToNumber`. In base alla specifica questo metodo restituisce:

> Se `parametro` è **true**, restituisci **1**. Se `parametro` è **false**, restituisci **+0**.

È questo il motivo per il quale possiamo sommare valori booleani e ottenere risultati corretti.

Sezioni corrispondenti:

- [**12.5.6** Unary `+` Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## I commenti HTML sono validi anche in JavaScript

Non ci crederai, ma `<!--` (ovvero un commento in HTML) è un commento valido in JavaScript.

```js
// commento valido
<!-- anche questo
```

### 💡 Spiegazione:

Stupito? Commenti HTML-like sono stati pensati per permettere ai browser che non capivano il tag `<script>` di degradare in modo soft. Questi browser, ad esempio Netscape 1.x non sono più diffusi. Quindi non c'è proprio più alcun motivo per inserire commenti HTML nei tag `script`

Dato che Node.js è basato sull'engine V8, i commenti HTML-like sono supportati anche dal runtime di the Node.js. Inoltre sono parte delle specifiche:

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` è ~~not~~ a number

Il tipo di `NaN` è `'number'`:

```js
typeof NaN; // -> 'number'
```

### 💡 Spiegazione:

Spiegazione di come funzionano gli operatori `typeof` e `instanceof`:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` e `null` sono objects

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// però
null instanceof Object; // false
```

### 💡 Spiegazione:

Il comportamento dell'operatore `typeof` è definito nella seguente sezione delle specifiche:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

Secondo le specifiche, l'operatore `typeof` restituisce una stringa in base alla [Table 35: `typeof` Operator Results](https://www.ecma-international.org/ecma-262/#table-35). Per `null`, gli oggetti ordinari, esotici standard e non standard che non implementano `[[Call]]`, restituisce la stringa `"object"`.

Comunque si può anche controllare il tipo di un oggetto utilizzando il metodo `toString`.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## Incrementare numeri magicamente

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 Spiegazione:

Questo è causato dallo standard IEEE 754-2008 per l'aritmetica binaria dei numeri in virgola mobile. A questa grandezze numeriche, arrotonda al numero pari più vicino. Leggi di più qui:

- [**6.1.6** The Number Type](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) on Wikipedia

## La precisione di `0.1 + 0.2`

Un giochino ben noto. La somma di `0.1` e `0.2` è completamente sbagliata:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 Spiegazione:

La risposta alla domanda [”La matematica in virgola mobile è completamente rotta? ”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) su StackOverflow:

> Le costanti `0.2` e `0.3` nel programma saranno approssimazioni del loro vero valore. Il valore `double` più vicino a `0.2` è più grande del numero razionale `0.2` ma il `double` più vicino a `0.3` è più piccolo del numero razionale `0.3`. La somma di `0.1` e `0.2` risulta essere più grande del numero razionale `0.3` e quindi risultando diverso dalla costante presente nel codice.

Questo problema è talmente noto che esiste anche il sito web [0.30000000000000004.com](http://0.30000000000000004.com/). Capita in tutti i linguaggi di programmazione che svolgono calcoli in virgola mobile, non solo JavaScript.

## Patchare numeri

Possiamo aggiungere metodi nostri agli oggetti wrapper come `Number` o `String`.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 Spiegazione:

Ovviamente possiamo estendere l'oggetto `Number` così come ogni altro oggetto in JavaScript. Non è comunque una pratica consigliata se il metodo definito non è parte delle specifiche. Ecco la lista delle proprietà dell'oggetto `Number`:

- [**20.1** Number Objects](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## Confrontare tre numeri

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 Spiegazione:

Perchè funziona in questo modo? Beh, il problema è nella prima parte dell'espressione. Ecco come funziona:

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

Possiamo correggerlo con l'operatore _Greater than or equal (`>=`)_:

```js
3 > 2 >= 1; // true
```

Leggi più a riguardo degli operatori relazionali nelle specifiche:

- [**12.10** Relational Operators](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## Matematica spassosa

Spesso il risultato delle operazioni aritmetiche in JavaScript risulta essere abbastanza strano. Consideriamo questi esempi:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 Spiegazione:

Cosa succede nei primi quattro esempi? Ecco una piccola tabella per comprendere la somma in JavaScript:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

E per quanto riguarda gli altri esempi? I metodi `ToPrimitive` e `ToString` vengono chiamati implicitamente per `[]` e `{}` prima della somma. Leggi di più riguardo a questo processo nelle specifiche:

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

In particolare l'eccezione è in `{} + []`. Il motivo per cui differisce da `[] + {}` è che, senza parentesi, viene interpretato come un blocco di codice seguito dall'operatore unario +, convertendo `[]` in un numero. Come viene spiegato di seguito:

```js
{
  // qui un blocco di codice
}
+[]; // -> 0
```

Per ottenere lo stesso risultato di `[] + {}` possiamo racchiuderlo tra parentesi.

```js
({} + []); // -> [object Object]
```

## Somma di RegExps

Sapevi che si possono sommare numero in questo modo?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 Spiegazione:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## Le stringhe non sono istanze di `String`

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 Spiegazione:

Il costruttore di `String` restituisce una stringa:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

Proviamo con `new`:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

Object? eh?

```js
new String("str"); // -> [String: 'str']
```

Più informazioni sul costruttore di String nelle specifiche:

- [**21.1.1** The String Constructor](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## Richiamare funzioni con le backticks

Dichiariamo una funzione che logga tutti i parametri nella console:

```js
function f(...args) {
  return args;
}
```

Senza dubbio, saprai che possiamo richiamarla nel modo seguente:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

Ma sapevi di poter chiamare qualsiasi funzione con le backticks?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 Spiegazione:

Beh, questa non è per niente magia se hai familiarità con i _Tagged template literals_. Nell'esempio precedente, la funzione f `f` è un tag per i template literal. I tag prima dei template literals permettono di svolgere il parsing dei template con una funzione. Il primo parametro di una "funzione tag" contiene un array di stringhe. I parametri restanti sono relativi alle espressioni. Ad esempio:

```js
function template(strings, ...keys) {
  // fai qualcosa con strings and keys…
}
```

Questa è la [magia dietro](http://mxstbr.blog/2016/11/styled-components-magic-explained/) famosa libreria chiamata [💅 styled-components](https://www.styled-components.com/), molto popolare tra la community di React.

Link alle specifiche:

- [**12.3.7** Tagged Templates](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## Call call call

> Trovato da [@cramforce](http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 Spiegazione:

Attenzione, ti può mettere in crisi il cervello! Prova ad eseguire questo codice a mente: stiamo applicando il metodo `call` usando il metodo `apply`.
Leggi di più:

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## Una proprietà chiamata `constructor`

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 Spiegazione:

Consideriamo questo esempio passo passo:

```js
// Dichiariamo una costante che è la stringa 'constructor'
const c = "constructor";

// c è una stringa
c; // -> 'constructor'

// Otteniamo il costruttore di string
c[c]; // -> [Function: String]

// Otteniamo il costruttore di constructor
c[c][c]; // -> [Function: Function]

// chiamiamo la funzione costruttore e gli passiamo
// il corpo di una nuova funzione come parametro
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// Chiamiamo la funzione anonima risultante
// Il risultato è loggare sulla console la stringa 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

`Object.prototype.constructor` restituisce un riferimento al costruttore di `Object` che ha creato l'oggetto. Con le stringhe è `String`, nel caso dei numeri è `Number` e così via.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## Un Object usato come key nelle property di un oggetto

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 Spiegazione:

Perchè funziona così? Qui stiamo utilizzando le _Computed property name_. Quando passiamo un oggetto tra parentesi quadre, forza la conversione di quell'oggetto a stringa, quindi otteniamo la proprietà `'[object Object]'` e il valore `{}`.

Possiamo realizzare un "brackets hell" in questo modo:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

Leggi di più a riguardo degli object literals qui:

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN
- [**12.2.6** Object Initializer](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## Accedere ai prototypes con `__proto__`

Come sappiamo, i tipi primitivi non hanno prototipi. Però, se proviamo ad ottenere il valore di `__proto__` per i tipi primitivi, otteniamo questo:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 Spiegazione:

Questo accade perchè quando qualcosa non ha un prototype, verrà inserito in un oggetto wrapper con un metodo `ToObject`. Quindi, passo passo:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

Qui più informazioni riguardo a `__proto__`:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

Quale è il risultato dell'espressione qui sotto?

```js
`${{ Object }}`;
```

La risposta è:

```js
// -> '[object Object]'
```

### 💡 Spiegazione:

Abbiamo definito un oggetto con una proprietà `Object` usando la _Shorthand property notation_:

```js
{
  Object: Object;
}
```

Quindi abbiamo passato questo oggetto al template literal, seguirà la chiamata al metodo `toString` per quell'oggetto. Ecco perchè otteniamo la stringa `'[object Object]'`.

- [**12.2.9** Template Literals](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Destructuring con valori di default

Considera l'esempio seguente:

```js
let x,
  { x: y = 1 } = { x };
y;
```

L'esempio precedente è un ottima domanda per un colloquio di lavoro. Quale è il valore di `y`? La risposta è:

```js
// -> 1
```

### 💡 Spiegazione:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

Con l'esempio precedente:

1. Dichiariamo `x` senza alcun valore, quindi risulta `undefined`.
2. Quindi inseriamo il valore di `x` all'interno della proprietà `x` dell'oggetto.
3. Quindi estraiamo il valore di `x` usando il destructuring e lo assegniamo a `y`. Se il valore non è definito, allora utilizziamo `1` come valore di default.
4. Restituiamo il valore di `y`.

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) su MDN

## Puntini e lo spreading

Si possono realizzare esempi interessanti utilizzando l'operatore di spreading e gli array. Considera questo:

```js
[...[..."..."]].length; // -> 3
```

### 💡 Spiegazione:

Perchè `3`? Quando utilizziamo [l'operatore di spread](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer), viene chiamato il metodo `@@iterator`, e l'iteratore che viene restituito viene utilizzato per ottenere i valori sui quali iterare. L'iteratore di default per le stringhe separa la stringa in caratteri. Dopo lo spreading, vengono inseriti questi valori in un array. Quindi viene svolto nuovamente lo spread sull'array e il risultato viene nuovamente inserito al suo interno.

La stringa `'...'` è composta da tre caratteri `.`, quindi la dimensione dell'array risultante è `3`.

Ora, passo passo:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

Chiaramente, possiamo svolgere questo procedimento di spread e wrap quante volte vogliamo:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## Labels

Sono in pochi i programmatori che sono a conoscenza delle Labels in JavaScript. Sono abbastanza interessanti:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 Spiegazione:

L'istruzione etichettata viene utilizzata con le istruzioni di `break` o `continue`. Possiamo usare un'etichetta per identificare costrutto iterativo, e usare le istruzioni `break` o `continue` per indicare se il programma deve interrompere l'iterazione o continuarla.

Nell'esempio precedente, identifichiamo l'etichetta `foo`. Dopo che `console.log('first');` viene eseguita l'esecuzione viene fermata.

Approfondisci le etichette in JavaScript:

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) su MDN

## Labels annidate

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 Spiegazione:

Simile agli esempi precedenti, clicca sui seguenti link:

- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) su MDN

## Un `try..catch` insidioso

Cosa restituisce questa espressione? `2` o `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

La risposta è `3`. Sorpreso?

### 💡 Spiegazione:

- [**13.15** The `try` Statement](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## Si tratta di ereditarietà multipla?

Dai uno sguardo all'esempio sottostante:

```js
new class F extends (String, Array) {}(); // -> F []
```

Si tratta di ereditarietà multipla? Negativo.

### 💡 Spiegazione:

La parte interessante è il valore della clausola (`(String, Array)`) di `extends`. L'operatore di grouping restituisce sempre il suo ultimo parametro, quindi `(String, Array)` è semplicemente `Array`. Questo significa che abbiamo creato una classe che estende `Array`.

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## Un generator che produce se stesso

Guarda questo esempio di generator che produce se stesso:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

Come possiamo notare, il valore restituito è un oggetto con `value` uguale a `f`. In quel caso, possiamo fare una cosa del genere:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and così via
// …
```

### 💡 Spiegazione:

Per capirne il suo funzionamento, leggi queste sezioni delle specifiche:

- [**25** Control Abstraction Objects](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** Generator Objects](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## Una classe di tipo class

Considera questa sintassi offuscata in gioco:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

Sembra la dichiarazione di una classe all'interno di un'altra classe. Dovrebbe essere un errore, invece otteniamo `'object'`.

### 💡 Spiegazione:

Da ECMAScript 5, possiamo usare le _keywords_ come _property names_. Quindi immaginalo come nel seguente esempio:

```js
const foo = {
  class: function() {}
};
```

ES6 ha standardizzato la definizione compatta per i metodi. Inoltre, le classi possono essere anonime. Quindi se togliamo la parte con `: function`, otteniamo:

```js
class {
  class() {}
}
```

Il risultato di una default class è sempre un oggetto semplice. E il tuo typeof dovrebbe restituire `'object'`.

Leggi di più qui:

- [**14.3** Method Definitions](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## Oggetti non-coercible

Con i ben noti, esiste un modo per evitare la type-coercion. Guarda un po':

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

Adesso possiamo utilizzarla in questo modo:

```js
// objects
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// strings
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// numbers
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 Spiegazione:

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## Arrow functions strambe

Considera l'esempio sottostante:

```js
let f = () => 10;
f(); // -> 10
```

Okay, va bene, ma guarda questo:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 Spiegazione:

Potresti aspettarti `{}` anzichè `undefined`. Questo è perchè le parentesi graffe fanno parte della sintassi per le arrow functions, quindi `f` restituirà undefined. È comunque possibile restituire l'oggetto `{}` direttamente da una arrow function, racchiudendo il valore di ritorno tra parentesi.

```js
let f = () => ({});
f(); // -> {}
```

## Arrow functions non possono essere un costruttore

Considera l'esempio sottostante:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> f { 'a': 1 }
```

Ora, prova a fare la stessa cosa con una arrow function:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 Spiegazione:

Le arrow function non possono essere utilizzate come costruttore e lanceranno un errore se usate con `new`. Dato che hanno un `this` lessicale, e non hanno la proprietà `prototype`, non avrebbe molto senso.

## `arguments` e arrow functions

Considera l'esempio sottostante:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

Ora, prova a fare la stessa cosa con una arrow function:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 Spiegazione:

Le arrow functions sono una versione alleggerita delle funzioni tradizionali con un focus sull'essere concise e con un `this` lessicale. Allo stesso tempo le arrow function non forniscono un binding per l'oggetto `arguments`. Un'alternativa valida per ottenere lo stesso risultato è utilizzare i `rest parameters`:

```js
let f = (...args) => args;
f("a");
```

- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) at MDN.

## Uno strano return

anche l'istruzione `return` può essere complicata. Considera questo:

<!-- prettier-ignore-start -->
```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```
<!-- prettier-ignore-end -->

### 💡 Spiegazione:

`return` e l'espressione da restituire devono essere sulla stessa linea:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

Questo a causa di un concetto chiamato Automatic Semicolon Insertion, che inserisce automagicamente punti e virgola dopo la maggior parte degli a capo. Nel primo esempio, c'è un punto e virgola inserito tra l'istruzione `return` e l'oggetto, quindi la funzione restituisce `undefined` e l'oggetto non viene mai valutato.

- [**11.9.1** Rules of Automatic Semicolon Insertion](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** The `return` Statement](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## Concatenare assegnamenti su un object

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

Da destra a sinistra, `{n: 2}` viene assegnato a foo, e il risultato di questo assegnamento `{n: 2}` viene assegnato a foo.x, ecco perchè bar è `{n: 1, x: {n: 2}}` in quanto bar è un riferimento a foo. Ma perchè foo.x è undefined mentre bar.x non lo è?

### 💡 Spiegazione:

Foo e bar referenziano lo stesso oggetto `{n: 1}`, e gli lvalues vengono risolti prima dell'assegnamento. `foo = {n: 2}` sta creando un nuovo oggetto, quindi foo viene aggiornato per referenziare il nuovo oggetto. Il trick qui è in `foo.x = ...` in quanto il lvalue è stato risolto precedentemente e referenzia ancora il vecchio oggetto `foo = {n: 1}` e lo aggiorna inserendo il valore x. Dopo questa catena di assegnamenti, bar continua a referenziare il vecchio oggetto foo, ma foo referenzia il nuovo oggetto `{n: 2}`, dove x non esiste.

È equivalente a:

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## Accedere alle properties di un object con gli array

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

E per quanto concerne gli array pseudo-multidimensionali?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 Spiegazione:

L'operatore parentesi quadre `[]` converte l'espressione usando il metodo `toString`. Convertire un array di un solo elemento in una stringa è come convertire l'elemento contenuto nell'array in stringa.

```js
["property"].toString(); // -> 'property'
```

## Null e gli operatori relazionali

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 Spiegazione:

Per farla breve, se `null` che è minore di `0` è `false`, allora `null >= 0` è `true`. Leggi la spiegazione approfondita per questo [qui](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274).

## `Number.toFixed()` mostra numeri diversi

`Number.toFixed()` può comportarsi in modo bizzarro in certi browser. Guarda l'esempio seguente:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 Spiegazione:

L'istinto potrebbe farci pensare che IE11 sia corretto e Firefox/Chrome sbaglino, la realtà è che Firefox/Chrome stanno rispettando gli standard per i numeri in virgola mobile (IEEE-754 Floating Point), mentre IE11 sta evitando di rispettarli (quello che probabilmente è) uno sforzo per restituire dei risultati più chiari.

Possiamo vedere perchè questo accade con un semplice test:

```js
// Confermare lo strano risultato dell'arrotondamento per difetto di 5
(0.7875).toFixed(3); // -> 0.787
// Sembra essere 5 quando si estende il
// limite a 64-bit (double-precision) di precisione
(0.7875).toFixed(14); // -> 0.78750000000000
// Ma se si supera il limite?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

I numeri floating point non sono memorizzati come una sequenza di cifre decimali, ma attraverso un metodo più elaborato che produce delle piccole inacuratezze the solitamente vengono eliminate dalle chiamate a toString o simili, ma queste imprecisioni rimangono comunque presenti internamente.

In questo caso, il "5" alla fine era un numero infinitesimamente più piccolo del vero 5. Arrotondandolo ad una precisione ragionevole verrà mostrato come 5... ma internamente non è un 5.

IE11, invece, mostrerà il valore dato in input con degli zeri in coda, anche nel caso di toFixed(20), in quanto sembra forzare l'arrotondamento del valore per evitare problematiche causate dai limiti hardware.

Guarda il riferimento a `NOTE 2` sulla definizione per `toFixed` nelle specifiche ECMA-262.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` più piccolo di `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 Spiegazione:

- [Perchè Math.max() è più piccolo di Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) by Charlie Harvey

## Confrontare `null` con `0`

La seguente espressione sembra introdurre una contraddizione:

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

Come può `null` non essere uguale a, o maggiore di `0`, se `null >= 0` è effettivamente `true`? (Funziona anche con "inferiore a" nello stesso modo.)

### 💡 Spiegazione:

Il modo in cui queste tre espressioni vengono valutate sono tutti diversi ed è per questo che viene prodotto questo comportamento un po' inaspettato.

Per prima cosa analizziamo il comportamento dell'operatore di abstract equality comparison, `null == 0`.
Solitamente, se l'operatore non riesce a confrontare i suoi operanti in modo opportuno, li converte in numeri e compara questi ultimo. Quindi ci si può aspettare il seguente comportamento:

```js
// This is not what happens
(null == 0 + null) == +0;
0 == 0;
true;
```

Invece, secondo una lettura attenta delle specifiche, la conversione a numero non avviene per l'operando che ha valore `null` o `undefined`. Quindi, se abbiamo `null` da un lato del simbolo uguale, l'altro lato deve essere `null` o `undefined` per fare in modo che venga restituito `true`. Dato che non è questo il caso, verrà restituito `false`.

Ora analizziamo l'operatore di comparazione `null > 0`. Qui l'algoritmo, a differenza dell'operatore di abstract equality, _convertirà_ `null` in un numero. Quindi il comportamento sarà il seguente:

```js
null > 0
+null = +0
0 > 0
false
```

Infine, analizziamo l'operatore relazionale `null >= 0`. Si può obiettare che questa espressione dovrebbe essere il risultato di `null > 0 || null == 0`; se fosse così, allora il risultato dell'espressione dovrebbe essere `false`. Invece l'operatore `>=` funziona in un modo completamente diverso, dove praticamente prende l'opposto dell'operatore `<`. Dato che l'esempio con l'operatore "maggiore di" produce lo stesso valore dell'operatore "minore di", l'espressione verrà valutata nel modo seguente:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## Alcune ridichiarazioni di variabili

JS permette la ridichiarazione di variabili:

```js
a;
a;
// È valida anche questa
a, a;
```

Funziona anche in modalità strict:

```js
var a, a, a;
var a;
var a;
```

### 💡 Spiegazione:

Tutte le definizione sono state unite in una sola.

- [**13.3.2** Variable Statement](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## Comportamento di default di Array.prototype.sort()

Supponiamo di voler ordinare un array di numeri.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 Spiegazione:

L'ordinamento di default viene realizzato convertendo gli elementi in stringhe, quindi confrontando i loro valore in UTF-16.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### Suggerimento

Passa una `comparefn` se vuoi ordinare qualcosa che non è una stringa.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

## resolve() non restituisce un'istanza di Promise

```javascript
const theObject = {
  a: 7
};
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // -> Instance object di Promise

thePromise.then(value => {
  console.log(value === theObject); // -> true
  console.log(value); // -> { a: 7 }
});
```

Il `value` che viene risolto da `thePromise` è esattamente `theObject`.

E se inserissimo un'altra `Promise` all'interno della funzione `resolve`?

```javascript
const theObject = new Promise((resolve, reject) => {
  resolve(7);
}); // -> Promise instance object
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // -> Promise instance object

thePromise.then(value => {
  console.log(value === theObject); // -> false
  console.log(value); // -> 7
});
```

### 💡 Spiegazione:

> Questa funzione appiattisce livelli annidati di oggetti promise-like (ad esempio una promise che risolve a una promise che risolve a qualcosa) in un singolo livello.

&ndash; [Promise.resolve() on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

La specifica è [ECMAScript 25.6.1.3.2 Promise Resolve Functions](https://tc39.es/ecma262/#sec-promise-resolve-functions). But it is not quite human-friendly.

# 📚 Other resources

- [wtfjs.com](http://wtfjs.com/) — una raccolta di irregolarità e stranezze davvero speciali con un pizzico di momenti dolorosamente controintuitivi per il linguaggio del web.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — A lightning talk by Gary Bernhardt from CodeMash 2012
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — Il talk di Kyle Simpsons alla Forward 2 che prova a "estrarre le stramberie” da JavaScript. Il suo desiderio è aiutare a scrivere un codice più pulito, elegante e leggibile, ispirare le persone a contribuire alla community open source.

# 🎓 License

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
```

## File: `README-kr.md`
```markdown
# 아니 X발? 자바스크립트 이게 뭐야??

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> 재미있고 교묘한 JavaScript 예제

JavaScript는 훌륭한 언어입니다. JavaScript는 구문이 단순하며 큰 생태계를 가지고 있습니다. 가장 중요한 점은 훌륭한 공동체를 가지고 있다는 것입니다.

동시에, 우리 모두는 JavaScript가 까다로운 부분을 가진 꽤 재미있는 언어라는 것을 알고 있습니다. 몇몇 특징은 우리의 일상적인 일을 순식간에 지옥으로 바꾸기도 하고, 우리를 크게 웃게 만들기도 합니다.

WTFJS의 아이디어는 [Brian Leroux](https://twitter.com/brianleroux)에 속해있습니다. 이 목록들은 그의 이야기에서 꽤 영감을 받았습니다. [**“WTFJS”** at dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# NPM 패키지 메뉴스크립트

이 핸드북은 `npm`를 이용하여 설치할 수 있습니다. 그냥 실행합시다:

```
$ npm install -g wtfjs
```

이제 당신은 커맨드 창에서 'wtfjs'를 실행할 수 있게 되었습니다. 당신이 선택한 '$PAGER'에서 'wtfjs'가 열릴 것 입니다. 아니면 계속 여기서 읽어도 됩니다.

출처는 <https://github.com/denysdovhan/wtfjs> 여기에서 확인 할 수 있습니다.

# 번역

현재, **wtfjs**는 아래와 같은 언어로 번역되었습니다:

- [中文版](./README-zh-cn.md)
- [हिंदी](./README-hi.md)
- [Français](./README-fr-fr.md)
- [Português do Brasil](./README-pt-br.md)
- [Polski](./README-pl-pl.md)
- [Italiano](./README-it-it.md)
- [Russian](https://habr.com/ru/company/mailru/blog/335292/) (on Habr.com)
- [한국어](./README-kr.md)

[**다른 번역 **][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D

<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [💪🏻 시작하기에 앞서](#-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0%EC%97%90-%EC%95%9E%EC%84%9C)
- [✍🏻 표기법](#-%ED%91%9C%EA%B8%B0%EB%B2%95)
- [👀 예제](#-%EC%98%88%EC%A0%9C)
  - [`[]`와 `![]은 같다`](#%EC%99%80-%EC%9D%80-%EA%B0%99%EB%8B%A4)
  - [`true`는 `![]`와 같지 않지만, `[]`와도 같지 않다](#true%EB%8A%94-%EC%99%80-%EA%B0%99%EC%A7%80-%EC%95%8A%EC%A7%80%EB%A7%8C-%EC%99%80%EB%8F%84-%EA%B0%99%EC%A7%80-%EC%95%8A%EB%8B%A4)
  - [true는 false](#true%EB%8A%94-false)
  - [baNaNa](#banana)
  - [`NaN`은 `NaN`이 아니다](#nan%EC%9D%80-nan%EC%9D%B4-%EC%95%84%EB%8B%88%EB%8B%A4)
  - [이것은 실패다](#%EC%9D%B4%EA%B2%83%EC%9D%80-%EC%8B%A4%ED%8C%A8%EB%8B%A4)
  - [`[]`은 truthy 이지만 `true`는 아니다](#%EC%9D%80-truthy-%EC%9D%B4%EC%A7%80%EB%A7%8C-true%EB%8A%94-%EC%95%84%EB%8B%88%EB%8B%A4)
  - [`null`은 falsy 이지만 `false`은 아니다](#null%EC%9D%80-falsy-%EC%9D%B4%EC%A7%80%EB%A7%8C-false%EC%9D%80-%EC%95%84%EB%8B%88%EB%8B%A4)
  - [`document.all`은 객체이지만 `undefined`이다](#documentall%EC%9D%80-%EA%B0%9D%EC%B2%B4%EC%9D%B4%EC%A7%80%EB%A7%8C-undefined%EC%9D%B4%EB%8B%A4)
  - [최소 값은 0 보다 크다](#%EC%B5%9C%EC%86%8C-%EA%B0%92%EC%9D%80-0-%EB%B3%B4%EB%8B%A4-%ED%81%AC%EB%8B%A4)
  - [함수는 함수가 아니다](#%ED%95%A8%EC%88%98%EB%8A%94-%ED%95%A8%EC%88%98%EA%B0%80-%EC%95%84%EB%8B%88%EB%8B%A4)
  - [배열 추가](#%EB%B0%B0%EC%97%B4-%EC%B6%94%EA%B0%80)
  - [배열의 후행 쉼표](#%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%9B%84%ED%96%89-%EC%89%BC%ED%91%9C)
  - [배열 평등은 몬스터](#%EB%B0%B0%EC%97%B4-%ED%8F%89%EB%93%B1%EC%9D%80-%EB%AA%AC%EC%8A%A4%ED%84%B0)
  - [`undefined`과 `Number`](#undefined%EA%B3%BC-number)
  - [`parseInt`은 나쁜 놈이다](#parseint%EC%9D%80-%EB%82%98%EC%81%9C-%EB%86%88%EC%9D%B4%EB%8B%A4)
  - [`true`와 `false`를 이용한 수학](#true%EC%99%80-false%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%88%98%ED%95%99)
  - [HTML 주석은 JavaScript에서도 유효하다](#html-%EC%A3%BC%EC%84%9D%EC%9D%80-javascript%EC%97%90%EC%84%9C%EB%8F%84-%EC%9C%A0%ED%9A%A8%ED%95%98%EB%8B%A4)
  - [`NaN`은 숫자가 아니다](#nan%EC%9D%80-%EC%88%AB%EC%9E%90%EA%B0%80-%EC%95%84%EB%8B%88%EB%8B%A4)
  - [`[]`과 `null`은 객체이다](#%EA%B3%BC-null%EC%9D%80-%EA%B0%9D%EC%B2%B4%EC%9D%B4%EB%8B%A4)
  - [마법처럼 증가하는 숫자](#%EB%A7%88%EB%B2%95%EC%B2%98%EB%9F%BC-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EC%88%AB%EC%9E%90)
  - [정확도 `0.1 + 0.2`](#%EC%A0%95%ED%99%95%EB%8F%84-01--02)
  - [패치 번호](#%ED%8C%A8%EC%B9%98-%EB%B2%88%ED%98%B8)
  - [세 숫자의 비교](#%EC%84%B8-%EC%88%AB%EC%9E%90%EC%9D%98-%EB%B9%84%EA%B5%90)
  - [재미있는 수학](#%EC%9E%AC%EB%AF%B8%EC%9E%88%EB%8A%94-%EC%88%98%ED%95%99)
  - [RegExps 추가](#regexps-%EC%B6%94%EA%B0%80)
  - [문자열은 `String`의 인스턴스가 아니다](#%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%80-string%EC%9D%98-%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4%EA%B0%80-%EC%95%84%EB%8B%88%EB%8B%A4)
  - [backticks으로 함수 호출](#backticks%EC%9C%BC%EB%A1%9C-%ED%95%A8%EC%88%98-%ED%98%B8%EC%B6%9C)
  - [Call call call](#call-call-call)
  - [`constructor` 속성](#constructor-%EC%86%8D%EC%84%B1)
  - [객체 속성의 키로서의 객체](#%EA%B0%9D%EC%B2%B4-%EC%86%8D%EC%84%B1%EC%9D%98-%ED%82%A4%EB%A1%9C%EC%84%9C%EC%9D%98-%EA%B0%9D%EC%B2%B4)
  - [`__proto__`을 사용한 프로토 타입 접근](#__proto__%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%ED%86%A0-%ED%83%80%EC%9E%85-%EC%A0%91%EA%B7%BC)
  - [`` `${{Object}}` ``](#-object-)
  - [디폴트 값으로 구조 해제](#%EB%94%94%ED%8F%B4%ED%8A%B8-%EA%B0%92%EC%9C%BC%EB%A1%9C-%EA%B5%AC%EC%A1%B0-%ED%95%B4%EC%A0%9C)
  - [Dots와 spreading](#dots%EC%99%80-spreading)
  - [라벨](#%EB%9D%BC%EB%B2%A8)
  - [중첩된 라벨들](#%EC%A4%91%EC%B2%A9%EB%90%9C-%EB%9D%BC%EB%B2%A8%EB%93%A4)
  - [교활한 `try..catch`](#%EA%B5%90%ED%99%9C%ED%95%9C-trycatch)
  - [이것은 다중 상속인가?](#%EC%9D%B4%EA%B2%83%EC%9D%80-%EB%8B%A4%EC%A4%91-%EC%83%81%EC%86%8D%EC%9D%B8%EA%B0%80)
  - [스스로 생성되는 Generator](#%EC%8A%A4%EC%8A%A4%EB%A1%9C-%EC%83%9D%EC%84%B1%EB%90%98%EB%8A%94-generator)
  - [클래스의 클래스](#%ED%81%B4%EB%9E%98%EC%8A%A4%EC%9D%98-%ED%81%B4%EB%9E%98%EC%8A%A4)
  - [강제할 수 없는 객체](#%EA%B0%95%EC%A0%9C%ED%95%A0-%EC%88%98-%EC%97%86%EB%8A%94-%EA%B0%9D%EC%B2%B4)
  - [까다로운 화살표 함수](#%EA%B9%8C%EB%8B%A4%EB%A1%9C%EC%9A%B4-%ED%99%94%EC%82%B4%ED%91%9C-%ED%95%A8%EC%88%98)
  - [화살표 함수는 생성자가 될 수 없다](#%ED%99%94%EC%82%B4%ED%91%9C-%ED%95%A8%EC%88%98%EB%8A%94-%EC%83%9D%EC%84%B1%EC%9E%90%EA%B0%80-%EB%90%A0-%EC%88%98-%EC%97%86%EB%8B%A4)
  - [`arguments`와 화살표 함수](#arguments%EC%99%80-%ED%99%94%EC%82%B4%ED%91%9C-%ED%95%A8%EC%88%98)
  - [까다로운 return](#%EA%B9%8C%EB%8B%A4%EB%A1%9C%EC%9A%B4-return)
  - [객체에 할당 연결](#%EA%B0%9D%EC%B2%B4%EC%97%90-%ED%95%A0%EB%8B%B9-%EC%97%B0%EA%B2%B0)
  - [배열을 사용한 객체 속성 접근 s](#%EB%B0%B0%EC%97%B4%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%EA%B0%9D%EC%B2%B4-%EC%86%8D%EC%84%B1-%EC%A0%91%EA%B7%BC-s)
  - [Null 및 관계 연산자](#null-%EB%B0%8F-%EA%B4%80%EA%B3%84-%EC%97%B0%EC%82%B0%EC%9E%90)
  - [`Number.toFixed()` 다른 숫자 표시](#numbertofixed-%EB%8B%A4%EB%A5%B8-%EC%88%AB%EC%9E%90-%ED%91%9C%EC%8B%9C)
  - [`Math.max()` 이하 `Math.min()`](#mathmax-%EC%9D%B4%ED%95%98-mathmin)
  - [`null`과 `0` 비교](#null%EA%B3%BC-0-%EB%B9%84%EA%B5%90)
  - [동일한 변수 재선언](#%EB%8F%99%EC%9D%BC%ED%95%9C-%EB%B3%80%EC%88%98-%EC%9E%AC%EC%84%A0%EC%96%B8)
  - [디폴트 동작 Array.prototype.sort()](#%EB%94%94%ED%8F%B4%ED%8A%B8-%EB%8F%99%EC%9E%91-arrayprototypesort)
  - [resolve()은 Promise instance를 반환하지 않는다](#resolve%EC%9D%80-promise-instance%EB%A5%BC-%EB%B0%98%ED%99%98%ED%95%98%EC%A7%80-%EC%95%8A%EB%8A%94%EB%8B%A4)
- [📚 기타 resources](#-%EA%B8%B0%ED%83%80-resources)
- [🎓 License](#-license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->

# 💪🏻 시작하기에 앞서

> &mdash; _[**“Just for Fun: 우연한 혁명가의 이야기”**](https://en.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

이 목록의 주요 목표는 가능한 JavaScript의 몇 가지의 엄청난 예제들을 모으고, 작동 방식을 설명하는 것 입니다. 이전에 우리가 몰랐던 것들을 배우는 것이 재미있기 때문입니다.

당신이 초보자라면, 이 노트를 사용하여 JavaScript에 대해 자세히 알아볼 수 있을 것입니다. 이 노트의 설명을 읽는 것에 더 많은 시간을 할애할 수 있기를 바랍니다.

당신이 전문 개발자라면, 우리가 사랑하는 JavaScript의 모든 기이한 점과 예상치 못한 것들에 대한 예시에 훌륭한 참조로 간주할 수 있습니다.

어쨌든, 이것을 읽읍시다. 당신은 아마 새로운 것들을 찾을 수 있을 것입니다.

# ✍🏻 표기법

**`// ->`** 식의 결과를 표시하는 데 사용됩니다. 예를 들면:

```js
1 + 1; // -> 2
```

**`// >`** `console.log` 또는 다른 출력의 결과를 의미합니다. 예를 들면:

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** 설명에 사용되는 주석입니다. 예를 들면:

```js
// Assigning a function to foo constant
const foo = function() {};
```

# 👀 예제

## `[]`와 `![]은 같다`

배열은 배열이 아닙니다:

```js
[] == ![]; // -> true
```

### 💡 설명:

추상 항등 연산자는 양쪽을 숫자로 변환하여 비교하고, 서로 다른 이유로 양 쪽의 숫자는 `0`이 됩니다. 배열은 truthy 하므로, 오른쪽의 값은 `0`을 강요하는 truthy value의 반대 값 즉, `false`입니다. 그러나 왼쪽은 빈 배열은 먼저 boolean이 되지 않고 숫자로 강제 변환되고 빈 배열은 truthy 임에도 불구하고 `0`으로 강요됩니다.

이 표현식이 어떻게 단순화 되는지는 아래와 같습니다:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

참조 [`[]`은 truthy 이지만 `true`은 아니다](#%EC%9D%80-truthy-%EC%9D%B4%EC%A7%80%EB%A7%8C-true%EB%8A%94-%EC%95%84%EB%8B%88%EB%8B%A4).

- [**12.5.9** 논리 연산자 NOT (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** 추상 평등](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true`는 `![]`와 같지 않지만, `[]`와도 같지 않다

배열은 `true`와 같지 않지만 배열이 아닌것도 `true`와 같지 않습니다;
배열은 `false`와 같지만 배열이 아닌것도 `false`와 같습니다:

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 설명:

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

- [**7.2.13** 추상 평등 비교](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## true는 false

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 설명:

다음 단계를 고려합시다:

```js
// true is 'truthy' and represented by value 1 (number), 'true' in string form is NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' is not the empty string, so it's a truthy value
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** 추상 평등 비교](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

이것은 JavaScript에서 구식 농담이지만 재해석 되었습니다. 원본은 다음과 같습니다:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 설명:

식은 `'foo' + (+'bar')`으로 평가되고 숫자가 아닌 `'bar'` 형태로 변환됩니다.

- [**12.8.3** 덧셈 연산자 (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 단항 + 연산자](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN`은 `NaN`이 아니다

```js
NaN === NaN; // -> false
```

### 💡 설명:

아래의 사항들로 동작의 논리를 엄격하게 정의합니다:

> 1. 만약 `Type(x)`와 `Type(y)`가 다르면 **false**를 반환합니다.
> 2. 만약 `Type(x)`이 숫자이고
>    1. `x`가 **NaN**이면 **false**를 반환합니다.
>    2. `y`가 **NaN**이면 **false**를 반환합니다.
>    3. … … …
>
> &mdash; [**7.2.14** 염격한 평등 비교](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

IEEE에서 정의한 `NaN`:

> 4 개의 상호 배타적인 관계 : 보다 작음, 같음, 보다 큼, 순서 없음. 마지막의 경우 하나 이상의 피연산자가 NaN일 때 발생합니다. 모든 NaN은 자신을 포함한 모든 것과 순서 없이 비교해야 합니다.
>
> &mdash; [“IEEE754 NaN 값에 false를 반환하는 것의 근거는 무엇입니까?”](https://stackoverflow.com/questions/1565164/1573715#1573715) StackOverflow에서

## 이것은 실패다

당신은 믿지 않을지도 모르지만 …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 설명:

기호를 하나하나 나누면 아래와 같은 패턴이 자주 발생하는 것을 알 수 있습니다:

```js
![] + []; // -> 'false'
![]; // -> false
```

그래서 `[]`를 `false`으로 바꾸는 시도를 해봅니다. 하지만 많은 내부 함수 호출(`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`)때문에 오른쪽 피 연산 문자열로 변환하게 됩니다:

```js
![] + [].toString(); // 'false'
```

문자열을 배열로 생각하면 `[0]`을 통해 첫 번째 문자에 접근할 수 있습니다:

```js
"false"[0]; // -> 'f'
```

나머지는 분명하지만 `i`는 꽤 까다롭습니다. `fail` 속 `i`는 'falseundefined'라는 문자열을 생성하고 `['10']` 인덱스를 사용하여 요소를 잡습니다.

## `[]`은 truthy 이지만 `true`는 아니다

배열은 truthy 한 값이지만 `true`와 같지는 않다.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 설명:

다음은 ECMA-262 명세된 것의 세션에 대한 링크입니다:

- [**12.5.9** 논리 NOT 연산자 (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** 추상 평등 비교](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null`은 falsy 이지만 `false`은 아니다

`null`은 falsy 값이라는 사실에도 불구하고 `false`는 아닙니다.

```js
!!null; // -> false
null == false; // -> false
```

동시에 `0` 또는 `''`와 같은 falsy 값은 `false`와 동일합니다.

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 설명:

설명은 이전 예제와 동일합니다. 다음은 해당 링크입니다:

- [**7.2.13** 추상 평등 비교](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all`은 객체이지만 `undefined`이다

> ⚠️ 이 파트는 브라우저 API 의 일부이며 Node.js 환경에서는 작동하지 않습니다.⚠️

`document.all`은 배열과 같은 클래스이고 페이지의 DOM 노드에 대한 엑세스를 제공한다는 사실에도 불구하고 `typeof`함수의 `undefined`으로 반응합니다.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

동시에 `document.all`은 `undefined`와 동일하지 않습니다.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

하지만 동시에:

```js
document.all == null; // -> true
```

### 💡 설명:

> 특히 이전 버전의 IE에서 `document.all`은 DOM 요소에 접근하는 방법을 사용했습니다. 이것은 표준이 된 적은 없지만 이전 JavaScript 코드에서 사용되었습니다. 새로운 APIs(`document.getElementById`와 같은)에서 표준이 진행되었을 때 이 API 호출은 쓸모 없게 되었고 표준 위원회는 이를 어떻게 처리할지 결정해야 했습니다. 광범위하게 사용되기 때문에 그들은 API를 유지하기로 결정했지만 JavaScript 명세된 것을 고의로 위반했습니다.
> 이것이 `undefined`의 상황에서 [엄격한 평등 비교](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)을 사용했을 때 `false`를 응답하고 [추상 평등 비교](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)을 사용할 때 `true`로 응답하는 이유는 명시적으로 허용하는 명세된 것의 의도적인 위반 때문입니다.
>
> &mdash; [“오래된 특징 - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) WhatWG의 HTML 명세된 것
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) YDKJS의 Types & Grammar

## 최소 값은 0 보다 크다

`Number.MIN_VALUE`은 0 보다 큰 가장 작은 숫자입니다:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 설명:

> `Number.MIN_VALUE`은 `5e-324`입니다. 즉, 부동 소수점 정밀도 내에서 표현할 수 있는 가장 작은 양수입니다. 이 말은 0 에 도달할 수 있는 가장 가까운 값이라는 의미 입니다. 이것은 소수가 제공할 수 있는 최상의 값이라고 정의할 수 있습니다.
>
> 비록 엄격하게 실제로 숫자는 아니지만 전체적으로 가장 작은 값은 `Number.NEGATIVE_INFINITY`이라고 할 수 있습니다.
>
> &mdash; [“자바 스크립트에서 왜 `0`은 `Number.MIN_VALUE`보다 작습니까?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) StackOverflow에서

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## 함수는 함수가 아니다

> ⚠️ V8 v5.5 또는 그 이하의 버전에서는 버그가 있을 수 있습니다.(Node.js <=7) ⚠️

이것을 _undefined is not a function_ 모두가 알고 있지만 이건 어떨까요?

```js
// Declare a class which extends null
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 설명:

이것은 명세된 것의 일부가 아닙니다. 현재 수정된 버그 일 뿐이므로 향후 아무 문제 없을 것입니다.

## 배열 추가

두 개의 배열을 추가하려면 어떻게 해야 할까요?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 설명:

연결이 발생합니다.차근차근 다음을 봅시다:

```js
[1, 2, 3] +
  [4, 5, 6][
    // call toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concatenation
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## 배열의 후행 쉼표

4 개의 빈 배열을 만듭니다. 그럼에도 불구하고 후행 쉼표로 인해 세가지 , 요소가 있는 배열을 얻게 됩니다:

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 설명:

> **후행 쉼표** ("마지막 쉼표"라고도 함)는 JavaScript 에 새로운 요소, 매개 변수 또는 속성을 추가할 때 유용하게 사용할 수 있습니다. 만약 새 속성을 추가하려는 상황에서 이미 후행 쉼표를 사용하고 있는 경우 이전 마지막 줄을 수정하지 않고 새 줄을 추가할 수 있습니다. 이렇게 하면 버전 관리가 더 깔끔 해지고 코드 편집이 덜 번거로울 수 있습니다.
>
> &mdash; [후행 쉼표](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) MDN에서

## 배열 평등은 몬스터

배열 평등은 아래에서 볼 수 있듯 JavaScript에서는 몬스터입니다:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 설명:

아래의 예제를 주의 깊게 살펴 보아야 합니다! 이 동작은 [**7.2.13** 추상 동등 비교](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)에 설명되어 있습니다.

## `undefined`과 `Number`

`Number`생성자에 인수를 전달하지 않으면 `0` 값을 얻게 됩니다. 실제 인수가 없는 경우 `undefined`값이 형식 인수에 할당되기 때문에 인수가 없는 `Number`는 매개 변수 값으로 `undefined`를 사용합니다. 그러나 `undefined`를 통과하면 `NaN`을 얻을 수 있습니다.

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 설명:

명세된 것에 따르면:

1. 함수의 호출로 인수가 전달되지 않은 경우 `n`은 `+0`이 됩니다.
2. 또는 let `n` be ? `ToNumber(value)`.
3. `undefined`의 경우 `ToNumber(undefined)`는 `NaN`으로 반환해야 합니다.

다음은 해당 부분입니다:

- [**20.1.1** 숫자 생성자](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt`은 나쁜 놈이다

`parseInt`은 특이한 점으로 유명합니다:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 설명:** 이는 `parseInt`알 수 없는 문자에 도달할 때까지 문자별로 계속 구문 분석을 하기 때문에 발생합니다. `'f*ck'`에서 `f`는 16 진수로 `15`입니다.

`Infinity`정수로 파싱하는 것은…

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

`null`을 파싱하는 것에도 주의합시다:

```js
parseInt(null, 24); // -> 23
```

**💡 설명:**

> `null`을 문자열 `"null"`로 변환하려고 합니다. 0 부터 23 까지의 기수에 대해서 변환할 수 있는 숫자가 없으므로 NaN을 반환합니다. 24 에, `"n"`, 14 번째 문자가 숫자 체계에 추가됩니다. 31에, `"u"`, 21 번째 문자가 추가되고 전체 문자열을 디코딩 할 수 있게 되었습니다. 37에서 더 이상 생성할 수 있는 유효 숫자 집합이 없으며 `NaN`이 반환됩니다.
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) StackOverflow에서

8 진수에 대해서 잊지맙시다:

```js
parseInt("06"); // 6
parseInt("08"); // 8 if support ECMAScript 5
parseInt("08"); // 0 if not support ECMAScript 5
```

**💡 설명:** 입력 문자열이 "0"으로 시작하는 경우, 기수는 8 (octal) 또는 10 (decimal)입니다. 정확히는 어떤 기수가 선택되는가는 구현에 따라 다릅니다. ECMAScript 5는 10 (decimal)진수를 사용하도록 지정하지만 모든 브라우저가 이것을 지원하지는 않습니다. 그러므로 `parseInt`을 사용할 때는 항상 기수를 지정합시다.

`parseInt`항상 입력을 문자열로 변환:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

부동 소수점값을 파싱하는 동안 주의하세요.

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 설명:** `ParseInt`은 문자열 인수를 취하고 지정된 기수의 정수를 반환합니다. 또한 `ParseInt`은 문자열 매개 변수에서 첫 번째가 아닌 숫자를 포함하여 모든 것을 제거합니다. `0.000001`은 문자열 "0.000001"`로 바뀌고`parseInt`은`0`으로 반환됩니다.`0.0000001`이 문자열로 변환되면`"1e-7"`로 되므로`parseInt`은`1`을 반환합니다.`1/1999999`은`5.00000250000125e-7`로 해석되고`parseInt`은`5`을 리턴합니다.

## `true`와 `false`를 이용한 수학

몇 가지 수학을 해봅시다:

```js
true -
  true +
  // -> 2
  (true + true) * (true + true) -
  true; // -> 3
```

흠… 🤔

### 💡 설명:

`Number`생성자를 사용하여 값을 숫자로 강제 변환할 수 있습니다. `true`가 `1`로 강제되는 것은 분명합니다:

```js
Number(true); // -> 1
```

단항 더하기 연산자는 값을 숫자로 변환하려고 합니다. 이것은 정수와 소수의 문자열 표현일 뿐아니라 비문자열인 `true`, `false`와 `null`값도 변환할 수 있습니다. 특정 값을 파싱할 수 없는 경우 `NaN`으로 평가됩니다. 그것은 더 쉽게 `true`를 `1`로 강제할 수 있음을 의미합니다:

```js
+true; // -> 1
```

덧셈 또는 곱셈을 수행할 때 `ToNumber`메서드가 호출됩니다. 명세된 것에 따르면 아래의 메서드를 반환합니다:

> 만약 `argument`이 **true**이면 **1**이 반환됩니다. 만약`argument`이 **false**이면 **+0**이 반환됩니다.

이 때문에 boolean 값을 일반 숫자로 추가하고 올바른 결과를 얻을 수 있습니다.

해당 부분:

- [**12.5.6** 단항 `+` 연산자](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** 더하기 연산자(`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## HTML 주석은 JavaScript에서도 유효하다

이것이 `<!--` (HTML 주석으로 알려진) JavaScript에서도 주석으로 사용될 수 있다는 것이 깊은 인상을 남깁니다.

```js
// valid comment
<!-- valid comment too
```

### 💡 설명:

인상 깊었나요? 이는 HTML 과 유사한 주석 `<script>` 태그를 이해하지 못하는 브라우저가 정상적으로 저하되도록 하기 위한 것 입니다. Netscape 1.x과 같은 브라우저는 더 이상 인기가 없습니다. 따라서 더 이상 스크립트 태그에 HTML 주석을 넣을 필요가 없습니다.

Node.js는 V8 엔진을 기반으로 하기때문에 Node.js 런타임에서도 HTML 과 유사한 주석을 지원합니다. 또한 그것은 명시된 것의 일부입니다:

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN`은 숫자가 아니다

`NaN`의 타입은 `'number'`이다:

```js
typeof NaN; // -> 'number'
```

### 💡 설명:

`typeof`와 `instanceof`운영의 작동 방식에 대한 설명:

- [**12.5.5** `typeof` 운영](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** 런타임 의미론: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]`과 `null`은 객체이다

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// however
null instanceof Object; // false
```

### 💡 설명:

`typeof`연산자의 동작은 명시된 섹션에서 정의됩니다:

- [**12.5.5** `typeof` 운영자](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

명시된 것에 의하면 `typeof`연산자는 [Table 35: `typeof` 연산자 결과](https://www.ecma-international.org/ecma-262/#table-35)에 따라 문자열을 반환합니다. `[[Call]]`을 구현하지 않는 `null`, 일반, 표준 이국 및 비표준 이국 객체의 경우 문자열 `"object"`을 반환합니다.

그러나 `toString` 메서드를 사용하여 개체의 유형을 확인할 수 있습니다.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## 마법처럼 증가하는 숫자

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 설명:

이는 이진 부동 소수점 산술에 대한 IEEE 754-2008 표준으로 인해 발생합니다. 이 척도에서는 가장 가까운 짝수로 반올림됩니다. 더 읽어보기:

- [**6.1.6** 숫자 유형](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) on Wikipedia

## 정확도 `0.1 + 0.2`

잘 알려진 농담. `0.1`과 `0.2`의 추가는 is 매우 정확합니다:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 설명:

[”부동 소수점 수학이 깨졌습니까?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken)에 대한 대답 StackOverflow에서:

> 프로그램에서 상수 `0.2`와 `0.3`은 실제 값에 대한 근사치가 됩니다. `0.2`에 가장 가까운 `double`이 유리수 `0.2`보다 크지만 `0.3`에 가장 가까운 `double`이 유리수 `0.3`보다 작습니다. `0.1`과 `0.2`의 합은 유리수 `0.3`보다 커지기 때문에 코드의 상수와 일치하지 않습니다.

이 문제는 [0.30000000000000004.com](http://0.30000000000000004.com/)이라고 불리는 웹사이트에도 있을 정도로 잘 알려져 있습니다. JavaScript 뿐만 아니라 부동 소수점 수학을 사용하는 모든 언어에서 발생합니다.

## 패치 번호

`Number` 또는 `String`과 같은 객체에 자신의 방법을 추가할 수 있습니다.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 설명:

분명히, `Number`객체를 JavaScript에서 다른 객체처럼 확장할 수 있습니다. 그러나, 정의된 메서드의 동작이 명시된 것의 일부가 아닌 경우 권장되지 않습니다. `Number`의 속성 목록은 다음과 같습니다:

- [**20.1** 숫자 객체](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## 세 숫자의 비교

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 설명:

왜 이렇게 작동할까요? 음, 문제는 표현의 첫 부분에 있습니다. 어떻게 작동하는지 봅시다:

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

우리는 이것을 크거나 같음 연산자(`>=`)로 이 문제를 해결할 수 있습니다:

```js
3 > 2 >= 1; // true
```

명시된 것을 읽으면서 관계 연산자에 대해 자세히 알아봅시다:

- [**12.10** 관계 연산자](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## 재미있는 수학

종종 JavaScript에서 산술 연산 결과는 예상치 못한 결과일 수 있습니다. 아래의 예들을 고려합시다:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 설명:

처음 4 가지 예시에서 무슨 일이 일어나고 있나요? JavaScript에서 덧셈을 이해하기 위한 작은 표 입니다:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

다른 예들을 추가하면 어떨까요? `ToPrimitive`과 `ToString` 메서드는 덧셈을 하기 전 `[]`과 `{}`을 암시적으로 요구합니다. 아래의 명시를 통해 평가 프로세스에 대해 자세히 알아봅시다:

- [**12.8.3** 더하기 연산자 (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

특히, `{} + []` 여기에 예외가 있습니다. `[] + {}`는 괄호가 없으면 코드 블록으로 해석한 다음 단항 +로 해석되어 `[]`숫자로 변환하기 때문입니다. 다음을 따릅니다:

```js
{
  // a code block here
}
+[]; // -> 0
```

`[] + {}`와 동일한 출력을 얻으려면 괄호로 묶으면 가능합니다.

```js
({} + []); // -> [object Object]
```

## RegExps 추가

아래와 같은 숫자를 추가할 수 있다는 것을 알고 있었나요?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 설명:

- [**21.2.5.10** RegExp.prototype.source 얻기](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## 문자열은 `String`의 인스턴스가 아니다

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 설명:

`String` 생성자는 문자열을 반환합니다:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

`new`로 다음을 시도해 봅시다:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

객체? 그게 뭔가요?

```js
new String("str"); // -> [String: 'str']
```

문자열 생성자에 대한 추가 정보가 명시된 것:

- [**21.1.1** 문자열 생성자](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## backticks으로 함수 호출

모든 매개 변수를 콘솔에 기록하는 함수를 선언해 보겠습니다:

```js
function f(...args) {
  return args;
}
```

의심할 여지없이 함수를 다음과 같이 호출할 수 있습니다:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

그러나 backticks를 사용하여 모든 함수를 호출할 수 있다는 것을 알고있나요?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 설명:

음, 당신이 _Tagged template literals_ 에 친숙하다면 이것이 놀랍지는 않을 겁니다. 위의 예에서 `f`함수는 템플릿 리터럴에 대한 태그입니다. 템플릿 리터럴앞의 태그를 사용하면 함수로 템플릿 리터럴을 파싱할 수 있습니다. 태그 함수의 첫 번째 인수는 문자열 값의 배열을 포함합니다. 나머지 인수는 표현식과 관련이 있습니다. 예:

```js
function template(strings, ...keys) {
  // do something with strings and keys…
}
```

이 [magic behind](http://mxstbr.blog/2016/11/styled-components-magic-explained/)는 [💅 styled-components](https://www.styled-components.com/)라 불리는 React community에서 인기있는 유명한 도서관에 있습니다.

명세서를 링크합니다:

- [**12.3.7** 태그된 템플릿](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## Call call call

> [@cramforce](http://twitter.com/cramforce)에 의해 발견됨.

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 설명:

당신의 마음을 아프게 할 수 있으니 주의하세요! 이 코드를 머릿속에 재현해봅시다. `apply`메소드를 사용하여 `call`을 적용하고 있습니다. 더 읽어보기:

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## `constructor` 속성

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 설명:

이 예제를 차근차근 살펴봅시다:

```js
// Declare a new constant which is a string 'constructor'
const c = "constructor";

// c is a string
c; // -> 'constructor'

// Getting a constructor of string
c[c]; // -> [Function: String]

// Getting a constructor of constructor
c[c][c]; // -> [Function: Function]

// Call the Function constructor and pass
// the body of new function as an argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// And then call this anonymous function
// The result is console-logging a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

`Object.prototype.constructor`는 인스턴스 객체를 생성한 `Object` 생성자 함수에 대한 참조를 반환합니다. 문자열의 경우 `String`, 숫자의 경우 `Number`를 의미합니다.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## 객체 속성의 키로서의 객체

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 설명:

왜 그렇게 작동할까요? 여기에서 _Computed property name_ 을 사용합니다. 이러한 대괄호 사이에 객체를 전달하면 객체를 문자열로 강제 변환하기 때문에 속성 키 `'[object Object]'`와 `{}`값을 얻습니다.

다음과 같이 "대괄호 지옥"을 만들 수 있습니다:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

여기에서 객체 리터럴에 대해 자세히 알아보세요:

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN
- [**12.2.6** Object Initializer](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## `__proto__`을 사용한 프로토 타입 접근

아시다시피 primitives 에는 prototypes 이 없습니다. 그러나, `__proto__` primitives 에 대한 값을 얻으려고 한다면 다음과 같이 할 수 있습니다:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 설명:

이것은 프로토타입이 없는 무언가가 `ToObject` 메소드를 사용하여 래퍼 객체로 래핑되기 때문에 발생합니다. 차근차근 살펴봅시다:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

`__proto__`에 대한 자세한 정보는 아래와 같습니다:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

아래 식의 결과는 무엇일까요?

```js
`${{ Object }}`;
```

답은:

```js
// -> '[object Object]'
```

### 💡 설명:

_Shorthand property notation_ 을 `Object` 사용하여 속성이 있는 객체를 정의했습니다:

```js
{
  Object: Object;
}
```

그 다음 객체를 템플릿 리터럴에 전달 했으므로 `toString`메서드가 해당 객체를 호출합니다. 이것이 문자열 `'[object Object]'`을 얻는 이유입니다.

- [**12.2.9** Template Literals](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## 디폴트 값으로 구조 해제

이 예시를 고려하세요:

```js
let x,
  { x: y = 1 } = { x };
y;
```

위의 예시는 다음과 같은 질문을 위한 훌륭한 일입니다. `y`의 값은 무엇인가요? 그 답은:

```js
// -> 1
```

### 💡 설명:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

위의 예에서:

1. 값을 지정하지 않고 `x`를 선언하므로 이는 `undefined`입니다.
2. 그 다음 `x`값을 객체 속성 `x`로 압축합니다.
3. 그 다음 구조화를 사용하여 `x`값을 추출하고 `y`에 할당합니다. 값이 정의되어 있지않으면 `1`을 기본값으로 사용합니다.
4. `y`의 값을 반환합니다.

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Dots와 spreading

배열의 확산으로 흥미로운 예를 구성할 수 있습니다. 이를 고려하세요:

```js
[...[..."..."]].length; // -> 3
```

### 💡 설명:

왜 `3`일까요? [spread operator](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer)을 사용할 때 `@@iterator`메소드가 호출되고 반환된 Iterator는 반복할 값을 얻는데 사용됩니다. 문자열의 기본 Iterator는 문자열을 문자로 확산합니다. 확산 후 이러한 문자를 배열로 압축합니다. 그런 다음 이 배열을 다시 확산하고 배열로 다시 압축합니다.

문자열 `'...'`은 세 개의`.`로 구성되며 문자열의 길이는 `3`입니다.

이제 차근차근 살펴봅시다:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

분명하게 우리는 원하는 양의 배열 요소를 펼치고 래핑할 수 있습니다:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## 라벨

JavaScript에서 라벨에 대해 아는 프로그래머는 많지 않습니다. 라벨들은 꽤 재미있습니다:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 설명:

라벨 되어있는 문장들은 `break` 또는 `continue`문과 함께 사용됩니다. 라벨을 사용하여 루프를 식별할 수 있고 `break` 또는 `continue`문을 사용해 프로그램이 루프를 중단해야 하는지 또는 실행을 계속해야 하는지에 대한 여부를 알 수 있습니다.
위의 예를 보면 `foo`라는 라벨을 볼 수 있습니다. 그 뒤로 `console.log('first');`을 실행한 후 실행을 중단합니다.

JavaScript의 라벨에 대해 더 읽을거리:

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## 중첩된 라벨들

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 설명:

이전의 예와 유사합니다. 다음 링크를 따르세요:

- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## 교활한 `try..catch`

이 표현은 무엇을 반환할까요? `2`? 아니면 `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

정답은 `3`입니다. 놀랐나요?

### 💡 설명:

- [**13.15** The `try` Statement](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## 이것은 다중 상속인가?

아래의 예를 살펴보세요:

```js
new class F extends (String, Array) {}(); // -> F []
```

다중 상속인 것 같습니까? 아닙니다.

### 💡 설명:

흥미로운 부분은 `extends` 절 (`(String, Array)`)의 값입니다. 그룹화 연산자는 항상 마지막 인수를 반환하기 때문에 `(String, Array)`은 사실 `Array`입니다. 그 말은 이제 막 `Array`를 확장하는 클래스를 만들었다는 이야기입니다.

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## 스스로 생성되는 Generator

스스로 생성되는 Generator의 예를 살펴봅시다:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

보이는 것처럼 리턴된 값은 이것의 `value`와 `f`가 같은 객체입니다. 이러한 경우 아래와 같은 일을 해볼 수 있습니다:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 설명:

이러한 일들이 작동하는 이유를 이해하려면 다음 명세서를 읽으십시오:

- [**25** Control Abstraction Objects](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** Generator Objects](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## 클래스의 클래스

아래의 읽기 애매한 구문을 생각해봅시다:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

마치 클래스 내부에 클래스를 선언하는 것 같습니다. 오류여야 하지만 문자열 `'object'`을 얻었습니다.

### 💡 설명:

ECMAScript 5 시대부터 _keywords_ 는 _property names_ 으로 허용됩니다. 따라서 아래와 같은 간단한 객체 예제로 생각합시다:

```js
const foo = {
  class: function() {}
};
```

그리고 ES6에서 축약 메소드 정의를 표준화하였습니다. 또한 클래스는 익명이 될 수 있습니다. 그래서 우리가 `: function`부분을 지우면 아래와 같은 결과 값을 얻을 것 입니다:

```js
class {
  class() {}
}
```

디폴트 클래스의 결과 값은 항상 단순한 객체입니다. 그리고 이것의 타입은 `'object'`이어야 합니다.

더 읽을거리:

- [**14.3** Method Definitions](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## 강제할 수 없는 객체

잘 알려진 기호를 사용하면 유형 강제를 제거할 수 있습니다. 아래를 보세요:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

이제 우리는 아래와 같이 사용할 수 있습니다:

```js
// objects
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// strings
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// numbers
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 설명:

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## 까다로운 화살표 함수

아래의 예를 고려하세요 w:

```js
let f = () => 10;
f(); // -> 10
```

좋아요, 하지만 이건 어떨까요?:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 설명:

`undefined` 대신 `{}`을 기대할 수도 있습니다. 이것({}) 또한 화살표 함수의 구문 중 하나이기 때문에 `f`는 undefined 으로 리턴될 것입니다. 하지만 리턴 값을 괄호로 묶어서 화살표 함수에 직접 `{}` 객체를 리턴할 수는 있습니다.

```js
let f = () => ({});
f(); // -> {}
```

## 화살표 함수는 생성자가 될 수 없다

아래의 예를 생각해봅시다:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> f { 'a': 1 }
```

이제, 화살표 함수를 이용하여 동일하게 시도해봅시다:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 설명:

화살표 함수는 생성자로 사용할 수 없으며 new 와 함께 사용하면 오류가 발생합니다. 왜냐하면 렉시컬 범위의 `this`가 있고 `prototype`이 없기 때문에 그래서 말이 안될 것 입니다.

## `arguments`와 화살표 함수

아래의 예를 생각해봅시다 w:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

이제, 화살표 함수를 이용하여 동일하게 시도해봅시다 n:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 설명:

화살표 함수는 짧고 렉시컬 범위의 `this`에 초점을 둔 기존 함수의 경량화된 버전입니다. 동시에 화살표 함수는 `arguments`객체에 대한 바인딩을 제공하지 않습니다. 유효한 대안으로 `rest parameters`을 사용하여 같은 결과를 얻을 수 있습니다:

```js
let f = (...args) => args;
f("a");
```

- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) at MDN.

## 까다로운 return

`return` 구문 또한 까다롭습니다. 이것을 생각해봅시다:

<!-- prettier-ignore-start -->
```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```
<!-- prettier-ignore-end -->

### 💡 설명:

`return`과 반환된 표현식은 같은 줄에 있어야 합니다:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

이는 대부분 줄 바꿈 뒤에 세미콜론을 자동으로 삽입하는 자동 세미콜론 삽입이라는 개념 때문입니다. 첫번째 예시에서 `return`문과 객체 리터럴 사이에 세미콜론이 삽입되어 있으므로 함수는 `undefined`를 반환하고 객체 리터럴은 평가되지 않습니다.

- [**11.9.1** Rules of Automatic Semicolon Insertion](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** The `return` Statement](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## 객체에 할당 연결

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

오른쪽에서 왼쪽으로, `{n: 2}`이 foo에 할당되고, 이 할당의 결과`{n: 2}`는 foo.x 에 할당되어 있고, bar는 foo를 할당하고 있기 때문에 bar는 `{n: 1, x: {n: 2}}`입니다. 그런데 bar.x가 아닌 반면에 foo.x는 왜 정의되지 않은 것일까요?

### 💡 설명:

Foo와 bar는 같은 객체 `{n: 1}`를 참조하고 있고 lvalues는 할당되기 전에 결정됩니다. `foo = {n: 2}`은 새로운 객체를 생성하고 있으므로 foo는 새로운 객체를 참조하도록 업데이트됩니다. 트릭은 `foo.x = ...`의 foo 에 있습니다. lvalue 값은 사전에 확인되었고 여전히 이전 `foo = {n:1}` 객체를 참조하고 x 값을 추가하여 업데이트합니다. 체인 할당 후에도 bar는 여전히 이전의 foo 객체를 참조하지만 foo는 x가 존재하지 않는 새로운 `{n: 2}`객체를 참조합니다.

다음과 동일합니다:

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## 배열을 사용한 객체 속성 접근 s

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

다차원 배열의 수도코드는 무엇입니까?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 설명:

대괄호 연산자 `[]`는 `toString`을 사용하여 전달된 식을 변환합니다. 단일 요소 배열을 문자열으로 변환하는 것은 포함된 요소를 문자열로 변환하는 것과 유사합니다:

```js
["property"].toString(); // -> 'property'
```

## Null 및 관계 연산자

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 설명:

긴 얘기를 짧게 하자면, 만약 `null`이 `0` 보다 작으면 `false`이고 `null >= 0`은 `true`입니다. 여기에서 이에 대한 자세한 설명을 읽으십시오 [여기](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274).

## `Number.toFixed()` 다른 숫자 표시

`Number.toFixed()`는 다른 브라우저에서 약간 이상하게 작동할 수 있습니다. 아래 예를 확인하세요:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 설명:

본능적으로 IE11은 올바르고 Firefox/Chrome이 잘못되었다고 생각할 수 있지만 사실은 Firefox/Chrome이 더 직접적으로 숫자의 표준(IEEE-754 Floating Point)을 준수하고 있는 반면 IE11는 더 명확한 결과를 제공하기 위한 노력으로 그것들을 미세하게 거역하고 있습니다.

몇 가지 간단한 테스트를 통해 이 문제가 발생하는 이유를 확인할 수 있습니다:

```js
// Confirm the odd result of rounding a 5 down
(0.7875).toFixed(3); // -> 0.787
// It looks like it's just a 5 when you expand to the
// limits of 64-bit (double-precision) float accuracy
(0.7875).toFixed(14); // -> 0.78750000000000
// But what if you go beyond the limit?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

부동 소수점 번호는 내부적으로 10진수 리스트로 저장되는 것이 아니라 대게 toString과 유사한 호출에 의해 반올림되지만 실제로 내부적으로는 매우 복잡한 방법론을 통해 저장됩니다.

이 경우 끝에 있는 "5"는 실제로 진짜 5 보다 매우 작은 부분입니다.합리적인 길이로 반올림하면 5...으로 렌더링되지만 실제로는 내부적으로 5는 아닙니다.

그러나 IE11은 하드웨어 한계에서 문제를 줄이기 위해 값을 강제로 반올림하는 것처럼 보이기 때문에 toFixed(20)의 사례에서도 끝에 0만 추가한 값을 입력 보고 할 것입니다.

`toFixed`에 대한 ECMA-262 정의의 `NOTE 2`를 참고하세요.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` 이하 `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 설명:

- [Why is Math.max() less than Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) by Charlie Harvey

## `null`과 `0` 비교

다음 표현들은 모순을 의미한것 같습니다:

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

만약 `null >= 0`이 실제로 `true`이면 어떻게 `null`이 `0`과 같지도 않고 크지도 않을까요? (이는 보다 적은 경우에도 동일하게 작동합니다.)

### 💡 설명:

이 세가지 식이 평가되는 방식은 모두 다르며 예기치 않은 동작들을 생성합니다.

첫째, 추상 평등 비교 `null == 0`입니다. 일반적으로 이 연산자가 양쪽 값을 제대로 비교할 수없으면 둘 다 숫자로 변환한 후 숫자를 비교합니다. 그러면 다음 동작을 예상할 수 있습니다:

```js
// This is not what happens
(null == 0 + null) == +0;
0 == 0;
true;
```

그러나 spec을 자세히 읽어보면 숫자 변환은 `null`이나 `undefined`의 한 면에서는 일어나지 않습니다. 그러므로 등호 한쪽에 `null`이 있으면 다른 한쪽에 `null` 또는 `undefined`가 있어야 `true`를 리턴합니다. 이 경우 그렇지 않기 때문에`false`을 리턴합니다.

다음은 관계 비교 `null > 0`입나다. 여기서 알고리즘은 추상 평등 연산자와 달리 `null`을 숫자로 변환합니다. 따라서 다음과 같은 동작이 발생합니다:

```js
null > 0 + null = +0;
0 > 0;
false;
```

마지막으로 관계 비교 `null >= 0`입니다. 이 표현이 `null > 0 || null == 0`의 결과라고 주장할 수 있는데, 만약 그렇다면, 위의 결과는 이 역시 `false`라는 것을 의미할 것입니다. 그러나 사실 `>=`연산자는 매우 다른 방식으로 작동하는데, 이는 기본적으로 `<`연산자와 반대되는 방식입니다. 위보다 큰 연산자를 사용한 예도 연산자보다 작기 때문에 이 식은 실제로 다음과 같이 평가됩니다.

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## 동일한 변수 재선언

JavaScript에서는 변수를 다시 선언할 수 있습니다:

```js
a;
a;
// This is also valid
a, a;
```

strict 모드에서도 작동합니다:

```js
var a, a, a;
var a;
var a;
```

### 💡 설명:

모든 정의가 하나의 정의로 병합됩니다.

- [**13.3.2** Variable Statement](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## 디폴트 동작 Array.prototype.sort()

숫자 배열을 정렬해야 한다고 상상해보세요.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 설명:

기본 정렬 순서는 요소들을 문자열로 변환한 후 UTF-16 코드 단위 값의 시퀀스를 비교할 때 작성됩니다.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### 힌트

문자열 이외의 정렬을 시도하면 `comparefn`을 통과시키세요.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

## resolve()은 Promise instance를 반환하지 않는다

```javascript
const theObject = {
  a: 7
};
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // -> Promise instance object

thePromise.then(value => {
  console.log(value === theObject); // -> true
  console.log(value); // -> { a: 7 }
});
```

`value`는 `thePromise` 정확하게 말하면 `theObject`에서 해결되는 것 입니다.

`resolve`함수에 또 다른 `Promise`를 넣는 것은 어떨까요?

```javascript
const theObject = new Promise((resolve, reject) => {
  resolve(7);
}); // -> Promise instance object
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // -> Promise instance object

thePromise.then(value => {
  console.log(value === theObject); // -> false
  console.log(value); // -> 7
});
```

### 💡 설명:

> 이 함수는 promise 같은 객체의 중첩된 레이어(예시: 무언가로 해결되는 promise으로 해결되는 promise)를 단일 레이어로 평탄화합니다.

&ndash; [Promise.resolve() on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

명세서는 [ECMAScript 25.6.1.3.2 Promise Resolve Functions](https://tc39.es/ecma262/#sec-promise-resolve-functions)입니다. 하지만 그것은 인간 친화적이지 않습니다.

# 📚 기타 resources

- [wtfjs.com](http://wtfjs.com/) — a collection of those very special irregularities, inconsistencies and just plain painfully unintuitive moments for the language of the web.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — A lightning talk by Gary Bernhardt from CodeMash 2012
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — Kyle Simpsons talk for Forward 2 attempts to “pull out the crazy” from JavaScript. He wants to help you produce cleaner, more elegant, more readable code, then inspire people to contribute to the open source community.

# 🎓 License

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
```

## File: `README-pl-pl.md`
```markdown
# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> Lista zabawnych i podchwytliwych przykładów JavaScript

JavaScript to świetny język. Ma prostą składnię, duży ekosystem i, co najważniejsze, wspaniałą społeczność.

Jednocześnie wszyscy wiemy, że JavaScript jest dość zabawnym językiem z podchwytliwymi częściami. Niektóre z nich mogą szybko zamienić naszą codzienną pracę w piekło, a niektóre mogą rozśmieszyć nas na głos.

Oryginalny pomysł na WTFJS należy do [Brian Leroux](https://twitter.com/brianleroux). Ta lista jest bardzo zainspirowana jego przemową
[**“WTFJS”** na dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# Node Packaged Manuscript

Możesz zainstalować ten podręcznik za pomocą `npm`. Po prostu uruchom:

```
$ npm install -g wtfjs
```

Powinieneś być teraz w stanie uruchomić `wtfjs` w linii poleceń. Spowoduje to otwarcie instrukcji w wybranym `$PAGER`. W przeciwnym razie możesz kontynuować czytanie tutaj.

Źródło jest dostępne tutaj: <https://github.com/denysdovhan/wtfjs>

# Tłumaczenia

Obecnie są następujące tłumaczenia **wtfjs**:

- [中文版](./README-zh-cn.md)
- [Français](./README-fr-fr.md)
- [Polski](./README-pl-pl.md)

[**Poproś o kolejne tłumaczenie**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D

<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [💪🏻 Motywacja](#-motywacja)
- [✍🏻 Notacja](#-notacja)
- [👀 Przykłady](#-przyk%C5%82ady)
  - [`[]` jest równe `![]`](#-jest-r%C3%B3wne-)
  - [`true` nie jest równe `![]`, ale też nie równe `[]`](#true-nie-jest-r%C3%B3wne--ale-te%C5%BC-nie-r%C3%B3wne-)
  - [prawda to fałsz](#prawda-to-fa%C5%82sz)
  - [baNaNa](#banana)
  - [`NaN` nie jest `NaN`](#nan-nie-jest-nan)
  - [To jest fail](#to-jest-fail)
  - [`[]` jest prawdziwe, ale nie `true`](#-jest-prawdziwe-ale-nie-true)
  - [`null` jest fałszywe, ale nie `false`](#null-jest-fa%C5%82szywe-ale-nie-false)
  - [`document.all` jest obiektem, ale jest undefined](#documentall-jest-obiektem-ale-jest-undefined)
  - [Minimalna wartość jest większa od zera](#minimalna-warto%C5%9B%C4%87-jest-wi%C4%99ksza-od-zera)
  - [funkcja nie jest funkcją](#funkcja-nie-jest-funkcj%C4%85)
  - [Dodawanie tablic](#dodawanie-tablic)
  - [Trailing commas in array](#trailing-commas-in-array)
  - [Równość tablic to potwór](#r%C3%B3wno%C5%9B%C4%87-tablic-to-potw%C3%B3r)
  - [`undefined` oraz `Number`](#undefined-oraz-number)
  - [`parseInt` jest złym gościem](#parseint-jest-z%C5%82ym-go%C5%9Bciem)
  - [Matematyka z `true` i `false`](#matematyka-z-true-i-false)
  - [Komentarze HTML są obowiązujące w JavaScript](#komentarze-html-s%C4%85-obowi%C4%85zuj%C4%85ce-w-javascript)
  - [`NaN` is ~~not~~ a number](#nan-is-not-a-number)
  - [`[]` i `null` są obiektami](#-i-null-s%C4%85-obiektami)
  - [Magicznie rosnące liczby](#magicznie-rosn%C4%85ce-liczby)
  - [Precyzja `0.1 + 0.2`](#precyzja-01--02)
  - [Patching numbers](#patching-numbers)
  - [Porównanie trzech liczb](#por%C3%B3wnanie-trzech-liczb)
  - [Zabawna matematyka](#zabawna-matematyka)
  - [Dodanie RegExps](#dodanie-regexps)
  - [Stringi nie są instancjami `String`](#stringi-nie-s%C4%85-instancjami-string)
  - [Wywoływanie funkcji za pomocą backticksa](#wywo%C5%82ywanie-funkcji-za-pomoc%C4%85-backticksa)
  - [Call call call](#call-call-call)
  - [Właściwość `constructor`](#w%C5%82a%C5%9Bciwo%C5%9B%C4%87-constructor)
  - [Obiekt jako klucz właściwości obiektu](#obiekt-jako-klucz-w%C5%82a%C5%9Bciwo%C5%9Bci-obiektu)
  - [Dostęp do prototypów za pomocą `__proto__`](#dost%C4%99p-do-prototyp%C3%B3w-za-pomoc%C4%85-__proto__)
  - [`` `${{Object}}` ``](#-object-)
  - [Destrukturyzacja z wartościami domyślnymi](#destrukturyzacja-z-warto%C5%9Bciami-domy%C5%9Blnymi)
  - [Dots and spreading](#dots-and-spreading)
  - [Etykiety](#etykiety)
  - [Zagnieżdżone etykiety](#zagnie%C5%BCd%C5%BCone-etykiety)
  - [Podstępny `try..catch`](#podst%C4%99pny-trycatch)
  - [Czy to wielokrotne dziedziczenie?](#czy-to-wielokrotne-dziedziczenie)
  - [A generator which yields itself](#a-generator-which-yields-itself)
  - [Klasa klasy](#klasa-klasy)
  - [Non-coercible objects](#non-coercible-objects)
  - [Podstępne funkcje strzałkowe](#podst%C4%99pne-funkcje-strza%C5%82kowe)
  - [Funkcje strzałkowe nie mogą być konstruktorami](#funkcje-strza%C5%82kowe-nie-mog%C4%85-by%C4%87-konstruktorami)
  - [`arguments` i funkcje strzałkowe](#arguments-i-funkcje-strza%C5%82kowe)
  - [Podstępny return](#podst%C4%99pny-return)
  - [Chaining assignments on object](#chaining-assignments-on-object)
  - [Dostęp do właściwości obiektu za pomocą tablic](#dost%C4%99p-do-w%C5%82a%C5%9Bciwo%C5%9Bci-obiektu-za-pomoc%C4%85-tablic)
  - [Null and Relational Operators](#null-and-relational-operators)
  - [`Number.toFixed()` display different numbers](#numbertofixed-display-different-numbers)
  - [`Math.max()` mniej niż `Math.min()`](#mathmax-mniej-ni%C5%BC-mathmin)
  - [Comparing `null` to `0`](#comparing-null-to-0)
  - [Redeklaracja tej samej zmiennej](#redeklaracja-tej-samej-zmiennej)
  - [Domyślne zachowanie Array.prototype.sort()](#domy%C5%9Blne-zachowanie-arrayprototypesort)
- [📚 Inne materiały](#-inne-materia%C5%82y)
- [🎓 Licencja](#-licencja)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->

# 💪🏻 Motywacja

> Dla zabawy
>
> &mdash; _[**“Just for Fun: The Story of an Accidental Revolutionary”**](https://en.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

Głównym celem tej listy jest zebranie szalonych przykładów i wyjaśnienie, w jaki sposób działają, jeśli to możliwe. Tylko dlatego, że fajnie jest nauczyć się czegoś, czego wcześniej nie znaliśmy.

Jeśli jesteś początkujący, możesz skorzystać z tych notatek, aby głębiej zagłębić się w JavaScript. Mam nadzieję, że te notatki zmotywują cię do spędzenia więcej czasu na czytaniu specyfikacji.

Jeśli jesteś profesjonalnym programistą, możesz rozważyć te przykłady, jako świetne źródło informacji o wszystkich dziwactwach i nieoczekiwanych krawędziach naszego ukochanego JavaScript.

W każdym razie po prostu przeczytaj to. Prawdopodobnie znajdziesz coś nowego.

# ✍🏻 Notacja

**`// ->`** służy do wyświetlenia wyniku wyrażenia. Na przykład:

```js
1 + 1; // -> 2
```

**`// >`** oznacza wynik `console.log` lub wyświetlenie innego wyniku. Na przykład:

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** jest tylko komentarzem używanym w celu wyjaśnienia. Przykład:

```js
// Assigning a function to foo constant
const foo = function() {};
```

# 👀 Przykłady

## `[]` jest równe `![]`

Tablica jest równa zanegowanej tablicy:

```js
[] == ![]; // -> true
```

### 💡 Wytłumaczenie:

Abstrakcyjny operator równości przekształca obie strony na liczby, aby je porównać, a obie strony stają się liczbą `0` z różnych powodów. Tablice są prawdziwe, więc po prawej stronie przeciwieństwem prawdziwej wartości jest `false`, który jest następnie wymuszany na `0`. Po lewej jednak pusta tablica jest wymuszana na liczbę, nie będąc najpierw wartością logiczną, a puste tablice są wymuszane na `0`, mimo że są prawdziwe.

Oto jak to wyrażenie upraszcza:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

Zobacz też [`[]` jest prawdziwe, ale nie `true`](##-jest-prawdziwe-ale-nie-true).

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true` nie jest równe `![]`, ale też nie równe `[]`

Tablica nie jest równa `true`, ale zanegowana tablica też nie jest równa `true`;
Tablica jest równa `false`, zanegowana tablica również jest równa `false`:

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 Wytłumaczenie:

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

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## prawda to fałsz

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 Wytłumaczenie:

Rozważ to krok po kroku:

```js
// true is 'truthy' and represented by value 1 (number), 'true' in string form is NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' is not the empty string, so it's a truthy value
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

To stary żart w JavaScript, ale odnowiony. Oto oryginał:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 Wytłumaczenie:

Wyrażenie jest oceniane jako `'foo' + (+'bar')`, które konwertuje `'bar'` nie na liczbę.

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 Unary + Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` nie jest `NaN`

```js
NaN === NaN; // -> false
```

### 💡 Wytłumaczenie:

Specyfikacja ściśle określa logikę tego zachowania:

> 1. Jeśli `Type(x)` jest różny od `Type(y)`, zwraca **false**.
> 2. Jeśli `Type(x)` jest Number, wtedy
>    1. Jeśli `x` jest **NaN**, zwraca **false**.
>    2. Jeśli `y` jest **NaN**, zwraca **false**.
>    3. … … …
>
> &mdash; [**7.2.14** Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

Zgodnie z definicją `NaN` z IEEE:

> Możliwe są cztery wzajemnie wykluczające się relacje: mniejszy, równy, większy niż i nieuporządkowany. Ostatni przypadek powstaje, gdy co najmniej jednym operandem jest NaN. Każdy NaN porównuje się nieuporządkowany ze wszystkim, w tym samym sobą.
>
> &mdash; [“What is the rationale for all comparisons returning false for IEEE754 NaN values?”](https://stackoverflow.com/questions/1565164/1573715#1573715) at StackOverflow

## To jest fail

Nie uwierzyłbyś, ale …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 Wytłumaczenie:

Po rozbiciu masy symboli na części zauważamy, że często występuje następujący wzór:

```js
![] + []; // -> 'false'
![]; // -> false
```

Więc próbujemy dodać `[]` do `false`. Ale z powodu wielu wywołań funkcji wewnętrznych (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`) w końcu konwertujemy odpowiedni operand na ciąg:

```js
![] + [].toString(); // 'false'
```

Myśląc o łańcuchu jako tablicy, możemy uzyskać dostęp do jego pierwszego znaku za pośrednictwem `[0]`:

```js
"false"[0]; // -> 'f'
```

Reszta jest oczywista, ale `i` jest podchwytliwe. `i` w `fail` jest pobierany przez generowanie ciągu `'falseundefined'` i łapanie elementu na indeks `['10']`

## `[]` jest prawdziwe, ale nie `true`

Tablica jest prawdziwą wartością, jednak nie jest równa `true`.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 Wytłumaczenie:

Oto linki do odpowiednich sekcji specyfikacji ECMA-262:

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` jest fałszywe, ale nie `false`

Pomimo faktu, że`null` jest wartością fałszywą, nie jest równa `false`.

```js
!!null; // -> false
null == false; // -> false
```

W tym samym czasie inne wartości fałszywe, takie jak `0` lub `''` są równe do `false`.

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 Wytłumaczenie:

Wytłumaczenie jest takie samo jak w poprzednim przykładzie. Oto odpowiedni link:

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` jest obiektem, ale jest undefined

> ⚠️ Jest to część interfejsu API przeglądarki i nie będzie działać w środowisku Node.js ⚠️

Pomimo faktu, że `document.all` jest obiektem tablicowym i daje dostęp do węzłów DOM na stronie, odpowiada na funkcję `typeof` jako `undefined`.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

W tym samym czasie, `document.all` nie jest równe `undefined`.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

Ale w tym samym czasie:

```js
document.all == null; // -> true
```

### 💡 Wytłumaczenie:

> `document.all` kiedyś był sposobem na dostęp do elementów DOM, w szczególności w starszych wersjach IE. Chociaż nigdy nie był standardem, był szeroko stosowany w starszym kodzie JS. Kiedy standard rozwijał się z nowymi interfejsami API (takimi jak `document.getElementById`), to wywołanie interfejsu API stało się przestarzałe i komitet standardowy musiał zdecydować, co z nim zrobić. Ze względu na szerokie zastosowanie postanowili zachować interfejs API, ale wprowadzili umyślne naruszenie specyfikacji JavaScript.
> Powód, dla którego reaguje na `false` podczas korzystania ze [Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison) z `undefined` gdy `true` podczas korzystania z [Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) wynika z umyślnego naruszenia specyfikacji, która wyraźnie na to pozwala.
>
> &mdash; [“Obsolete features - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) na WhatWG - HTML spec
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) na YDKJS - Types & Grammar

## Minimalna wartość jest większa od zera

`Number.MIN_VALUE` jest najmniejszą liczbą, która jest większa od zera:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 Wytłumaczenie:

> `Number.MIN_VALUE` jest `5e-324`, np. najmniejsza liczba dodatnia, która może być reprezentowana z precyzją zmiennoprzecinkową, tj. jest tak blisko, jak można dojść do zera. Określa najlepszą rozdzielczość, jaką mogą zaoferować floaty.
>
> Teraz ogólna najmniejsza wartość to `Number.NEGATIVE_INFINITY` chociaż nie jest to tak naprawdę liczbowe w ścisłym tego słowa znaczeniu.
>
> &mdash; [“Why is `0` less than `Number.MIN_VALUE` in JavaScript?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) na StackOverflow

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## funkcja nie jest funkcją

> ⚠️ Bug obecny w wersji V8 5.5 lub nowszej (Node.js <=7) ⚠️

Wszyscy wiecie o irytującym _niezdefiniowany nie jest funkcją_, ale co z tym?

```js
// Declare a class which extends null
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 Wytłumaczenie:

To nie jest część specyfikacji. To tylko błąd, który został już naprawiony, więc nie powinno być z tym problemu w przyszłości.

## Dodawanie tablic

Co jeśli spróbujesz dodać dwie tablice?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 Wytłumaczenie:

Zachodzi konkatenacja. Krok po kroku wygląda to tak:

```js
[1, 2, 3] +
  [4, 5, 6][
    // call toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concatenation
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## Trailing commas in array

Utworzyłeś tablicę z 4 pustymi elementami. Mimo wszystko otrzymasz tablicę z trzema elementami ze względu na końcowe przecinki:

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 Wytłumaczenie:

> **Trailing commas** (czasami nazywane "final commas") może być przydatne podczas dodawania nowych elementów, parametrów lub właściwości do kodu JavaScript. Jeśli chcesz dodać nową właściwość, możesz po prostu dodać nową linię bez modyfikowania poprzedniej poprzedniej linii, jeśli linia ta już używa przecinka końcowego. To sprawia, że różnice w kontroli wersji są czystsze, a edycja kodu może być mniej kłopotliwa.
>
> &mdash; [Trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) na MDN

## Równość tablic to potwór

Równość tablic jest potworem w JS, jak widać poniżej:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 Wytłumaczenie:

Powinieneś uważnie obserwować powyższe przykłady! Zachowanie opisano w rozdziale [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) specyfikacji.

## `undefined` oraz `Number`

Jeśli nie przekażemy żadnych argumentów do konstruktura `Number`, otrzymamy `0`. Wartość `undefined` jest przypisana do formalnych argumentów, gdy nie ma rzeczywistych argumentów, więc możesz się spodziewać, że `Number` bez argumentów dostanie `undefined` jako wartość jego parametru. Jednak kiedy przekażemy `undefined`, dostaniemy `NaN`.

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 Wytłumaczenie:

Zgodnie ze specyfikacją:

1. Jeśli do wywołania tej funkcji nie zostaną przekazane żadne argumenty, pozwól `n` być `+0`.
2. Inaczej, pozwól `n` być ? `ToNumber(value)`.
3. W przypadku `undefined`, `ToNumber(undefined)` powinno zwrócić `NaN`.

Oto odpowiednia sekcja:

- [**20.1.1** The Number Constructor](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` jest złym gościem

`parseInt` słynie ze swoich dziwactw:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 Wytłumaczenie:** Dzieje się tak, ponieważ `parseInt` będzie kontynuować analizowanie znak po znaku, dopóki nie trafi na postać, której nie zna. `f` w `'f*ck'` jest cyfrą szesnastkową `15`.

Parsowanie `Infinity` do integer jest czymś…

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

Uważaj na parsowanie `null` także:

```js
parseInt(null, 24); // -> 23
```

**💡 Wytłumaczenie:**

> Konwertuje `null` na string `"null"` i próbuje to przekonwertować. W przypadku podstaw od 0 do 23 nie ma cyfr, które mógłby przekonwertować, więc zwraca NaN. Na 24, `"n"`, 14ta litera, jest dodawana do systemu liczbowego. Na 31, `"u"`, 21sza litera, jest dodawana, a cały ciąg można dekodować. Na 37 nie ma już żadnego poprawnego zestawu liczb, który można by wygenerować i `NaN` jest zwrócony.
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) na StackOverflow

Nie zapomnij o ósemkach:

```js
parseInt("06"); // 6
parseInt("08"); // 8 if support ECMAScript 5
parseInt("08"); // 0 if not support ECMAScript 5
```

**💡 Wytłumaczenie:** Jeśli ciąg wejściowy zaczyna się od "0", podstawa to osiem (ósemka) lub 10 (dziesiętnie). To, która podstawa jest wybrana, zależy od implementacji. ECMAScript 5 określa, że używana jest liczba 10 (dziesiętna), ale nie wszystkie przeglądarki obsługują to jeszcze. Z tego powodu zawsze określaj podstawę podczas używania `parseInt`.

`parseInt` zawsze konwertuj dane wejściowe na ciąg:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Zachowaj ostrożność podczas analizowania wartości zmiennoprzecinkowych

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 Wytłumaczenie:** `ParseInt` pobiera argument ciągu i zwraca liczbę całkowitą określonej podstawy. `ParseInt` usuwa również wszystko po pierwszej wartości cyfrowej i włącznie z nią w parametrze ciągu. `0.000001` jest konwertowany na ciąg znaków `"0.000001"` i `parseInt` zwraca `0`. Gdy `0.0000001` jest konwertowany na ciąg, który jest traktowany jako `"1e-7"` i stąd `parseInt` zwraca `1`. `1/1999999` jest interpretowane jako `5.00000250000125e-7` i `parseInt` zwraca `5`.

## Matematyka z `true` i `false`

Zróbmy trochę matematyki:

```js
true +
  true(
    // -> 2
    true + true
  ) *
    (true + true) -
  true; // -> 3
```

Hmmm… 🤔

### 💡 Wytłumaczenie:

Możemy narzucić wartości do liczb za pomocą konstruktora `Number`. To całkiem oczywiste że `true` będzie zmienione na `1`:

```js
Number(true); // -> 1
```

Jednoargumentowy operator plus próbuje przeliczyć swoją wartość na liczbę. Może konwertować reprezentacje ciągu liczb całkowitych i liczb zmiennoprzecinkowych, a także wartości nie łańcuchowe `true`, `false`, i `null`. Jeśli nie może przeanalizować określonej wartości, oceni to jako `NaN`. To oznacza, że możemy narzucić `true` na `1` łatwiej:

```js
+true; // -> 1
```

Podczas dodawania lub mnożenia, metoda `ToNumber` jest przywoływana. Zgodnie ze specyfikacją ta metoda zwraca:

> Jeśli `argument` jest **true**, zwraca **1**. Jeśli `argument` jest **false**, zwraca **+0**.

Dlatego możemy dodawać wartości logiczne jako liczby regularne i uzyskiwać prawidłowe wyniki.

Odpowiednie sekcje:

- [**12.5.6** Unary `+` Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## Komentarze HTML są obowiązujące w JavaScript

Będziesz pod wrażeniem, ale `<!--` (który jest znany jako komentarz HTML) jest poprawnym komentarzem w JavaScript.

```js
// valid comment
<!-- valid comment too
```

### 💡 Wytłumaczenie:

Pod wrażeniem? Komentarze w formacie HTML miały umożliwić przeglądarkom, które nie rozumieją tagu `<script>` degradować z wdziękiem. Te przeglądarki, np. Netscape 1.x nie są już popularne. Dlatego naprawdę nie ma sensu umieszczać komentarzy HTML w tagach skryptu.

Ponieważ Node.js jest oparty na silniku V8, komentarze podobne do HTML są obsługiwane również przez środowisko uruchomieniowe Node.js. Ponadto są częścią specyfikacji:

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` is ~~not~~ a number

Typ `NaN` jest `'number'`:

```js
typeof NaN; // -> 'number'
```

### 💡 Wytłumaczenie:

Wytłumaczenia jak operatory `typeof` i `instanceof` działają:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` i `null` są obiektami

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// however
null instanceof Object; // false
```

### 💡 Wytłumaczenie:

Zachowanie operatora `typeof` jest zdefiniowane w tej sekcji specyfikacji:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

Zgodnie ze specyfikacją, operator `typeof` zwraca ciąg zgodnie z [Table 35: `typeof` Operator Results](https://www.ecma-international.org/ecma-262/#table-35). For `null`, ordinary, standard exotic and non-standard exotic objects, which do not implement `[[Call]]`, it returns the string `"object"`.

Możesz jednak sprawdzić typ obiektu, używając metody `toString`.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## Magicznie rosnące liczby

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 Wytłumaczenie:

Jest to spowodowane standardem IEEE 754-2008 dla binarnej arytmetyki zmiennoprzecinkowej. W tej skali zaokrągla się do najbliższej liczby parzystej. Czytaj więcej:

- [**6.1.6** The Number Type](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) on Wikipedia

## Precyzja `0.1 + 0.2`

Dobrze znany żart. An addition of `0.1` and `0.2` is deadly precise:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 Wytłumaczenie:

Odpowiedź na pytanie [”Is floating point math broken?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) ze StackOverflow:

> Stałe `0.2` i `0.3` w twoim programie będzie również przybliżenie ich prawdziwych wartości. Zdarza się, że najbliższa `double` do `0.2` jest większa niż liczba wymierna `0.2`, ale najbliższa `double` do `0.3` jest mniejsza niż liczba wymierna `0.3`. Suma `0.1` i `0.2` kończy się na wartości większej od liczby wymiernej `0.3`, a zatem nie zgadza się ze stałą w kodzie.

Ten problem jest tak znany, że istnieje nawet strona internetowa o nazwie [0.30000000000000004.com](http://0.30000000000000004.com/). Występuje w każdym języku wykorzystującym matematykę zmiennoprzecinkową, nie tylko JavaScript.

## Patching numbers

Możesz dodać własne metody do wrapowania obiektów takich jak `Number` lub `String`.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 Wytłumaczenie:

Oczywiście możesz rozszerzyć obiekt `Number` jak każdy inny obiekt w JavaScript. Jednak nie jest zalecane, jeśli zachowanie zdefiniowanej metody nie jest częścią specyfikacji. Oto lista właściwości `Number`:

- [**20.1** Number Objects](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## Porównanie trzech liczb

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 Wytłumaczenie:

Dlaczego to działa w ten sposób? Problem tkwi w pierwszej części wyrażenia. Oto jak to działa:

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

Możemy to naprawić za pomocą _Operatora większy lub równy (`>=`)_:

```js
3 > 2 >= 1; // true
```

Przeczytaj więcej o operatorach relacyjnych w specyfikacji:

- [**12.10** Relational Operators](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## Zabawna matematyka

Często wyniki operacji arytmetycznych w JavaScript mogą być dość nieoczekiwane. Rozważ te przykłady:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 Wytłumaczenie:

Co dzieje się w pierwszych czterech przykładach? Oto mała tabelka, aby zrozumieć dodawanie w JavaScript:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

Co z innymi przykładami? Metody `ToPrimitive` i `ToString` są domyślnie wywoływane dla `[]` i `{}` przed dodaniem. Przeczytaj więcej o procesie oceny w specyfikacji:

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

Szczególnie, `{} + []` tutaj jest wyjątek. Powód, dla którego się różni z `[] + {}` polega na tym, że bez nawiasów interpretuje się go jako blok kodu, a następnie jako jedność +, konwertując `[]` na liczbę. Wygląda następująco:

```js
{
  // a code block here
}
+[]; // -> 0
```

Aby uzyskać ten sam wynik jak `[] + {}` możemy owrapować to w nawias.

```js
({} + []); // -> [object Object]
```

## Dodanie RegExps

Czy wiesz, że możesz dodawać takie liczby?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 Wytłumaczenie:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## Stringi nie są instancjami `String`

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 Wytłumaczenie:

Konstruktor `String` zwraca string:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

Spróbujmy z `new`:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

Obiekt? Co to jest?

```js
new String("str"); // -> [String: 'str']
```

Więcej informacji o konstruktorze String w specyfikacji:

- [**21.1.1** The String Constructor](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## Wywoływanie funkcji za pomocą backticksa

Zadeklarujmy funkcję, która rejestruje wszystkie parametry w konsoli:

```js
function f(...args) {
  return args;
}
```

Bez wątpienia wiesz, że możesz wywołać tę funkcję w następujący sposób:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

Ale czy wiesz, że możesz wywołać dowolną funkcję za pomocą backticksa?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 Wytłumaczenie:

Cóż, to wcale nie jest magia, jeśli jesteś obeznany z _Tagged template literals_. W powyższym przykładzie, funkcja `f` jest znacznikiem literału szablonu. Tagi przed literałem szablonu umożliwiają analizowanie literałów szablonu za pomocą funkcji. Pierwszy argument funkcji znacznika zawiera tablicę wartości ciągów. Pozostałe argumenty są powiązane z wyrażeniami. Przykład:

```js
function template(strings, ...keys) {
  // do something with strings and keys…
}
```

To jest [magia z tyłu](http://mxstbr.blog/2016/11/styled-components-magic-explained/) słynnej biblioteki o nazwie [💅 styled-components](https://www.styled-components.com/), która jest popularna w społeczności React.

Link do specyfikacji:

- [**12.3.7** Tagged Templates](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## Call call call

> Znalezione przez [@cramforce](http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 Wytłumaczenie:

Uwaga, może to popsuć ci umysł! Spróbuj odtworzyć ten kod w swojej głowie: stosujemy metodę `call` za pomocą metody`apply`. Czytaj więcej:

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## Właściwość `constructor`

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 Wytłumaczenie:

Rozważmy ten przykład krok po kroku:

```js
// Declare a new constant which is a string 'constructor'
const c = "constructor";

// c is a string
c; // -> 'constructor'

// Getting a constructor of string
c[c]; // -> [Function: String]

// Getting a constructor of constructor
c[c][c]; // -> [Function: Function]

// Call the Function constructor and pass
// the body of new function as an argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// And then call this anonymous function
// The result is console-logging a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

`Object.prototype.constructor` zwraca referencję do funkcji konstruktora `Object` który utworzył obiekt instancji. W przypadku łańcuchów jest to `String`, w przypadku liczb jest to `Number` i tak dalej.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) na MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## Obiekt jako klucz właściwości obiektu

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 Wytłumaczenie:

Dlaczego to działa? Tutaj używamy _Computed property name_. Gdy przekazujesz obiekt między tymi nawiasami, wymusza on obiekt na ciąg, więc otrzymujemy klucz właściwości `'[object Object]'` i wartość `{}`.

Możemy zrobić "brackets hell" jak tutaj:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

Przeczytaj więcej na temat literałów obiektowych tutaj:

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) na MDN
- [**12.2.6** Object Initializer](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## Dostęp do prototypów za pomocą `__proto__`

Jak wiemy, prymitywy nie mają prototypów. Jeśli jednak spróbujemy uzyskać wartość `__proto__` dla prymitywów otrzymalibyśmy to:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 Wytłumaczenie:

Dzieje się tak, ponieważ gdy coś nie ma prototypu, zostanie ono zawinięte w obiekt wrappera za pomocą metody `ToObject`. Więc krok po kroku:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

Oto więcej informacji na temat `__proto__`:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

Jaki jest wynik poniższego wyrażenia?

```js
`${{ Object }}`;
```

Odpowiedź to:

```js
// -> '[object Object]'
```

### 💡 Wytłumaczenie:

Zdefiniowaliśmy obiekt z właściwością `Object` używając _Shorthand property notation_:

```js
{
  Object: Object;
}
```

Następnie przekazaliśmy ten obiekt do literału szablonu, więc metoda `toString` wywołuje ten obiekt. Właśnie dlatego otrzymujemy string `'[object Object]'`.

- [**12.2.9** Template Literals](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Destrukturyzacja z wartościami domyślnymi

Rozważ ten przykład:

```js
let x,
  { x: y = 1 } = { x };
y;
```

Powyższy przykład to świetne zadanie na rozmowę kwalifikacyjną. Jaka jest wartość `y`? Odpowiedź to:

```js
// -> 1
```

### 💡 Wytłumaczenie:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

W powyższym przykładzie:

1. Deklarujemy `x` z brakiem wartości, więc jest `undefined`.
2. Wtedy pakujemy wartość `x` we własność obiektu `x`.
3. Następnie wyodrębniamy wartość `x` używając destrukturyzacji i chcemy to przypisać do `y`. Jeśli wartość nie zostanie zdefiniowana, wówczas użyjemy „`1` jako wartości domyślnej.
4. Zwróć wartość `y` .

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Dots and spreading

Ciekawe przykłady można skomponować z rozmieszczaniem tablic. Rozważ to:

```js
[...[..."..."]].length; // -> 3
```

### 💡 Wytłumaczenie:

Czemu `3`? Kiedy korzystamy ze [spread operatora](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer), metoda `@@iterator` jest wywołana, a zwrócony iterator służy do uzyskania wartości do iteracji. Domyślny iterator łańcucha rozdziela łańcuch na znaki. Po rozłożeniu pakujemy te znaki do tablicy. Następnie rozkładamy tę tablicę ponownie i pakujemy z powrotem do tablicy.

String `'...'` składa się z trzech znaków `.`, więc długość wynikowej tablicy wynosi `3`.

Teraz krok po kroku:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

Oczywiście możemy rozkładać i wrapować elementy tablicy tyle razy, ile chcemy:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## Etykiety

Niewielu programistów wie o etykietach w JavaScript. Są dość interesujące:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 Wytłumaczenie:

Instrukcja z etykietą jest używana z instrukcją `break` lub `continue`. Możesz użyć etykiety do zidentyfikowania pętli, a następnie użyć instrukcji `break` lub `continue`, aby wskazać, czy program powinien przerwać pętlę, czy kontynuować jej wykonywanie.

W powyższym przykładzie identyfikujemy etykietę `foo`. Po tym `console.log ('first');` wykonuje, a następnie przerywamy wykonywanie.

Przeczytaj więcej o etykietach w JavaScript:

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## Zagnieżdżone etykiety

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 Wytłumaczenie:

Podobnie jak w poprzednich przykładach, skorzystaj z poniższych linków:

- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## Podstępny `try..catch`

Co zwróci to wyrażenie?? `2` czy `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

Odpowiedź to `3`. Zaskoczony?

### 💡 Wytłumaczenie:

- [**13.15** The `try` Statement](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## Czy to wielokrotne dziedziczenie?

Spójrz na poniższy przykład:

```js
new class F extends (String, Array) {}(); // -> F []
```

Czy to wielokrotne dziedziczenie? Nie.

### 💡 Wytłumaczenie:

Interesującą częścią jest wartość klauzuli `extends` (`(String, Array)`). Operator grupowania zawsze zwraca ostatni argument, więc `(String, Array)` jest właściwie po prostu `Array`. Oznacza to, że właśnie stworzyliśmy klasę, która rozszerza `Array`.

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## A generator which yields itself

Consider this example of a generator which yields itself:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

Jak widać, zwrócona wartość jest obiektem wraz z nią `value` równa do `f`. W takim przypadku możemy zrobić coś takiego:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 Wytłumaczenie:

Aby zrozumieć, dlaczego to działa w ten sposób, przeczytaj następujące sekcje specyfikacji:

- [**25** Control Abstraction Objects](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** Generator Objects](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## Klasa klasy

Rozważ tę zaciemnioną składnię:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

Wygląda na to, że deklarujemy klasę wewnątrz klasy. Powinien być jednak błąd, ale otrzymujemy ciąg `'object'`.

### 💡 Wytłumaczenie:

Od ery ECMAScript 5 _słowa kluczowe_ są dozwolone jako _nazwy własności_. Pomyśl o tym jako o tym prostym przykładzie obiektu:

```js
const foo = {
  class: function() {}
};
```

I znormalizowane skróty definicji metod ES6. Ponadto klasy mogą być anonimowe. Więc jeśli opuścimy część `:function`, otrzymamy:

```js
class {
  class() {}
}
```

Wynik domyślnej klasy jest zawsze prostym obiektem. I jego typ powinien zwrócić `'object'`.

Przeczytaj więcej tutaj:

- [**14.3** Method Definitions](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## Non-coercible objects

Dzięki dobrze znanym symbolom można pozbyć się typu coercion. Spójrz:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

Teraz możemy użyć tego w następujący sposób:

```js
// objects
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// strings
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// numbers
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 Wytłumaczenie:

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## Podstępne funkcje strzałkowe

Rozważ poniższy przykład:

```js
let f = () => 10;
f(); // -> 10
```

Okej, w porządku, ale co z tym:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 Wytłumaczenie:

Możesz oczekiwać `{}` zamiast `undefined`. Wynika to z faktu, że nawiasy klamrowe są częścią składni funkcji strzałkowych, więc `f` zwróci niezdefiniowane. Możliwe jest jednak zwrócenie obiektu `{}` bezpośrednio z funkcji strzałkowej, poprzez umieszczenie wartości zwracanej w nawiasach.

```js
let f = () => ({});
f(); // -> {}
```

## Funkcje strzałkowe nie mogą być konstruktorami

Rozważ poniższy przykład:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

Teraz spróbuj zrobić to samo z funkcją strzałkową:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 Wytłumaczenie:

Funkcje strzałkowe nie mogą być używane jako konstruktory i będą zgłaszać błąd, gdy będą używane z nowym. Ponieważ ma leksykalne `this` i nie ma właściwości `prototype`, więc nie miałoby to większego sensu.

## `arguments` i funkcje strzałkowe

Rozważ poniższy przykład:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

Teraz spróbuj zrobić to samo z funkcją strzałkową:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 Wytłumaczenie:

Funkcje strzałkowe to lekka wersja zwykłych funkcji z naciskiem na bycie krótkim i leksykalnym `this`. Jednocześnie funkcje strzałkowe nie zapewniają wiązania dla obiektu `arguments`. Jako prawidłową alternatywę użyj `rest parameters`, aby osiągnąć ten sam wynik:

```js
let f = (...args) => args;
f("a");
```

- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) na MDN.

## Podstępny return

Wyrażenie `return` jest również podstępne. Rozważ to:

<!-- prettier-ignore-start -->
```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```
<!-- prettier-ignore-end -->

### 💡 Wytłumaczenie:

`return` i zwrócone wyrażenie musi znajdować się w tym samym wierszu:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

Wynika to z koncepcji o nazwie Automatyczne wstawianie średników, która automatycznie wstawia średniki po większości nowych linii. W pierwszym przykładzie między wyrażeniem `return` a literałem obiektu wstawiono średnik, więc funkcja zwraca `undefined`, a literał obiektu nigdy nie jest oceniany.

- [**11.9.1** Rules of Automatic Semicolon Insertion](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** The `return` Statement](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## Chaining assignments on object

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

Z prawej do lewej, `{n: 2}` jest przypisany do foo, a wynik tego przypisania `{n: 2}` jest do foo.x, i dlatego bar jest `{n: 1, x: {n: 2}}` jako bar jest referencją do foo. Ale czemu foo.x jest undefined podczas gdy bar.x nie jest ?

### 💡 Wytłumaczenie:

Foo and bar references the same object `{n: 1}`, and lvalues are resolved before assignations. `foo = {n: 2}` is creating a new object, and so foo is updated to reference that new object. The trick here is foo in `foo.x = ...` as a lvalue was resolved beforehand and still reference the old `foo = {n: 1}` object and update it by adding the x value. After that chain assignments, bar still reference the old foo object, but foo reference the new `{n: 2}` object, where x is not existing.

Jest to równoważne z:

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## Dostęp do właściwości obiektu za pomocą tablic

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

Co z tablicami pseudo-wielowymiarowymi?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 Wytłumaczenie:

Operator nawiasów klamrowych `[]` konwertuje przekazane wyrażenie za pomocą `toString`. Konwersja tablicy jednoelementowej na ciąg znaków jest zbliżona do konwersji zawartego elementu na ciąg znaków:

```js
["property"].toString(); // -> 'property'
```

## Null and Relational Operators

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 Wytłumaczenie:

Long story short, if `null` is less than `0` is `false`, then `null >= 0` is `true`. Read in-depth Wytłumaczenie for this [here](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274).

## `Number.toFixed()` display different numbers

`Number.toFixed()` może zachowywać się trochę dziwnie w różnych przeglądarkach. Sprawdź ten przykład:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 Wytłumaczenie:

Podczas gdy twoim pierwszym instynktem może być to, że IE11 jest poprawny, a Firefox / Chrome są w błędzie, w rzeczywistości Firefox / Chrome bardziej bezpośrednio przestrzegają standardów liczbowych (zmiennoprzecinkowy IEEE-754), podczas gdy IE11 nieznacznie ich nie przestrzega (prawdopodobnie), aby dać wyraźniejsze wyniki.

Możesz zobaczyć, dlaczego tak się dzieje po kilku szybkich testach:

```js
// Confirm the odd result of rounding a 5 down
(0.7875).toFixed(3); // -> 0.787
// It looks like it's just a 5 when you expand to the
// limits of 64-bit (double-precision) float accuracy
(0.7875).toFixed(14); // -> 0.78750000000000
// But what if you go beyond the limit?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

Floating point numbers are not stored as a list of decimal digits internally, but through a more complicated methodology that produces tiny inaccuracies that are usually rounded away by toString and similar calls, but are actually present internally.

In this case, that "5" on the end was actually an extremely tiny fraction below a true 5. Rounding it at any reasonable length will render it as a 5... but it is actually not a 5 internally.

IE11, however, will report the value input with only zeros appended to the end even in the toFixed(20) case, as it seems to be forcibly rounding the value to reduce the troubles from hardware limits.

See for reference `NOTE 2` on the ECMA-262 definition for `toFixed`.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` mniej niż `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 Wytłumaczenie:

- [Why is Math.max() less than Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) od Charlie Harvey

## Comparing `null` to `0`

Następujące wyrażenia wydają się wprowadzać w sprzeczność:

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

Jak `null` nie może być ani równy ani większy od `0`, jeśli `null>=0' jest w rzeczywistości`true`? (Działa to również z mniej niż w ten sam sposób.)

### 💡 Wytłumaczenie:

Sposób oceny tych trzech wyrażeń jest różny i jest odpowiedzialny za wywołanie tego nieoczekiwanego zachowania.

Po pierwsze, abstrakcyjne porównanie równości `null == 0`. Zwykle, jeśli ten operator nie może poprawnie porównać wartości po obu stronach, konwertuje obie liczby na liczby i porównuje liczby. Następnie możesz spodziewać się następującego zachowania:

```js
// This is not what happens
(null == 0 + null) == +0;
0 == 0;
true;
```

Jednak, zgodnie z dokładnym odczytaniem specyfikacji, konwersja liczb tak naprawdę nie zachodzi po stronie, która jest `null` lub `undefined`. Dlatego jeśli po jednej stronie znaku równości występuje `null`, druga strona musi być `null` lub `undefined`, aby wyrażenie mogło zwrócić `true`. Ponieważ tak nie jest, zwracane jest `false`.

Następnie relacyjne porównanie `null> 0`. Algorytm tutaj, w przeciwieństwie do abstrakcyjnego operatora równości, _przekonwertuje_ `null` na liczbę. Dlatego otrzymujemy takie zachowanie:

```js
null > 0
+null = +0
0 > 0
false
```

Wreszcie relacyjne porównanie `null >= 0`. Można argumentować, że to wyrażenie powinno być wynikiem `null> 0 || null == 0`; gdyby tak było, powyższe wyniki oznaczałyby, że byłoby to również `false`. Jednak operator `> =` w rzeczywistości działa w zupełnie inny sposób, co w zasadzie ma przeciwne działanie niż operator `<`. Ponieważ nasz przykład z operatorem większym niż powyżej odnosi się również do operatora mniejszego niż, oznacza to, że to wyrażenie jest w rzeczywistości oceniane tak:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## Redeklaracja tej samej zmiennej

JS pozwala na ponowne zdefiniowanie zmiennych:

```js
a;
a;
// This is also valid
a, a;
```

Działa również w trybie ścisłym:

```js
var a, a, a;
var a;
var a;
```

### 💡 Wytłumaczenie:

Wszystkie definicje są scalone w jedną definicję.

- [**13.3.2** Variable Statement](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## Domyślne zachowanie Array.prototype.sort()

Wyobraź sobie, że musisz posortować tablicę liczb.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 Wytłumaczenie:

Domyślna kolejność sortowania opiera się na konwersji elementów na ciągi, a następnie porównaniu ich sekwencji wartości jednostek kodu UTF-16.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### Wskazówka

Przekaż `comparefn` jeśli spróbujesz posortować cokolwiek poza ciągiem znaków.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

# 📚 Inne materiały

- [wtfjs.com](http://wtfjs.com/) — zbiór tych bardzo wyjątkowych nieprawidłowości, niespójności i po prostu bolesnie nieintuicyjnych momentów dla języka webowego.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — Lightning talk od Gary Bernhardt z CodeMash 2012
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — Kyle Simpsons mówi dla Forward 2 o próbach "wyciągnięcia szaleństwa" z JavaScript. Chce pomóc ci w tworzeniu czystszego, bardziej eleganckiego, bardziej czytelnego kodu, a następnie zainspirować ludzi do współpracy w społeczności open source.

# 🎓 Licencja

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square

Wersja polska od @[mbiesiad](https://github.com/mbiesiad)
```

## File: `README-pt-br.md`
```markdown
# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> Uma lista de exemplos engraçados e truques com JavaScript

JavaScript é uma excelente linguagem. Ela tem uma sintaxe simples, um ecossistema grande e, o mais importante, uma grande comunidade.

Ao mesmo tempo, todos nós sabemos que o JavaScript é uma linguagem engraçada com várias partes complicadas. Algumas delas porem rapidamente transformar seu trabalho em um inferno, e outras podem nos fazer gargalhar.

A ideia original para o WTFJS é do [Brian Leroux](https://twitter.com/brianleroux). Essa lista é inspirada por sua talk [**“WTFJS”** no dotJS 2012](https://www.youtube.com/watch?v=et8xNAc2ic8):

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# Node Packaged Manuscript

Você pode instalar esse manual usando o `npm`. É só rodar o comando:

```
$ npm install -g wtfjs
```

Você poderá rodar `wtfjs` na sua linha de comando. Esse comando vai abrir o manual na sua `$PAGER` selecionada ou você pode continuar lendo aqui mesmo.

O código-fonte está disponível aqui <https://github.com/denysdovhan/wtfjs>.

# Traduções

Atualmente, temos essas traduções disponíveis de **wtfjs**:

- [English (original)](./README.md)
- [中文版](./README-zh-cn.md)
- [Português do Brasil](./README-pt-br.md)

[**Solicite outra tradução**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

# Table of Contents

- [💪🏻 Motivação](#-motiva%C3%A7%C3%A3o)
- [✍🏻 Notação](#-nota%C3%A7%C3%A3o)
- [👀 Exemplos](#-exemplos)
  - [`[]` é igual a `![]`](#-%C3%A9-igual-a-)
  - [`true` não é igual a `![]`, nem igual a `[]` também](#true-n%C3%A3o-%C3%A9-igual-a--nem-igual-a--tamb%C3%A9m)
  - [true é false](#true-%C3%A9-false)
  - [baNaNa](#banana)
  - [`NaN` não é um `NaN`](#nan-n%C3%A3o-%C3%A9-um-nan)
  - [É uma falha](#%C3%A9-uma-falha)
  - [`[]` é verdadeiro, mas não `true`](#-%C3%A9-verdadeiro-mas-n%C3%A3o-true)
  - [`null` é falso, mas não `false`](#null-%C3%A9-falso-mas-n%C3%A3o-false)
  - [`document.all` é um objeto (object), mas é indefinido (undefined)](#documentall-%C3%A9-um-objeto-object-mas-%C3%A9-indefinido-undefined)
  - [Valor mínimo é maior que zero](#valor-m%C3%ADnimo-%C3%A9-maior-que-zero)
  - [function não é uma function](#function-n%C3%A3o-%C3%A9-uma-function)
  - [Somando arrays](#somando-arrays)
  - [Vírgulas finais em arrays](#v%C3%ADrgulas-finais-em-arrays)
  - [Igualdade entre arrays é um monstro](#igualdade-entre-arrays-%C3%A9-um-monstro)
  - [`undefined` e `Number`](#undefined-e-number)
  - [`parseInt` é um vilão](#parseint-%C3%A9-um-vil%C3%A3o)
  - [Matemática com `true` e `false`](#matem%C3%A1tica-com-true-e-false)
  - [Comentários HTML são válidos no JavaScript](#coment%C3%A1rios-html-s%C3%A3o-v%C3%A1lidos-no-javascript)
  - [`NaN` ~~não~~ é um número](#nan-n%C3%A3o-%C3%A9-um-n%C3%BAmero)
  - [`[]` e `null` são objetos](#-e-null-s%C3%A3o-objetos)
  - [Aumentando números magicamente](#aumentando-n%C3%BAmeros-magicamente)
  - [Precisão de `0.1 + 0.2`](#precis%C3%A3o-de-01--02)
  - [Patching numbers](#patching-numbers)
  - [Comparação de três números](#compara%C3%A7%C3%A3o-de-tr%C3%AAs-n%C3%BAmeros)
  - [Matemática engraçada](#matem%C3%A1tica-engra%C3%A7ada)
  - [Soma de RegExps](#soma-de-regexps)
  - [Strings não são instâncias `String`](#strings-n%C3%A3o-s%C3%A3o-inst%C3%A2ncias-string)
  - [Chamando funções com backticks](#chamando-fun%C3%A7%C3%B5es-com-backticks)
  - [Call call call](#call-call-call)
  - [Uma propriedade `constructor`](#uma-propriedade-constructor)
  - [Objeto como uma chave de uma propriedade de objeto](#objeto-como-uma-chave-de-uma-propriedade-de-objeto)
  - [Acessando protótipos com `__proto__`](#acessando-prot%C3%B3tipos-com-__proto__)
  - [`` `${{Object}}` ``](#-object-)
  - [Desestruturação com valores padrão](#desestrutura%C3%A7%C3%A3o-com-valores-padr%C3%A3o)
  - [Pontos e dispersão](#pontos-e-dispers%C3%A3o)
  - [Rótulos](#r%C3%B3tulos)
  - [Rótulos aninhados](#r%C3%B3tulos-aninhados)
  - [`try..catch` traidor](#trycatch-traidor)
  - [Isto é herança múltipla?](#isto-%C3%A9-heran%C3%A7a-m%C3%BAltipla)
  - [Um gerador que produz a si mesmo](#um-gerador-que-produz-a-si-mesmo)
  - [Uma classe de classe](#uma-classe-de-classe)
  - [Objetos não coercíveis](#objetos-n%C3%A3o-coerc%C3%ADveis)
  - [Arrow functions traiçoeiras](#arrow-functions-trai%C3%A7oeiras)
  - [Arrow functions não podem ser construtores](#arrow-functions-n%C3%A3o-podem-ser-construtores)
  - [`arguments` e arrow functions](#arguments-e-arrow-functions)
  - [Retorno traiçoeiro](#retorno-trai%C3%A7oeiro)
  - [Encadeamento atribuições em um objeto](#encadeamento-atribui%C3%A7%C3%B5es-em-um-objeto)
  - [Acessando propriedades de objetos usando arrays](#acessando-propriedades-de-objetos-usando-arrays)
  - [Null e Operadores Relacionais](#null-e-operadores-relacionais)
  - [`Number.toFixed()` mostra números diferentes](#numbertofixed-mostra-n%C3%BAmeros-diferentes)
  - [`Math.max()` menor que `Math.min()`](#mathmax-menor-que-mathmin)
  - [Comparando `null` com `0`](#comparando-null-com-0)
  - [Redeclaração da mesma variável](#redeclara%C3%A7%C3%A3o-da-mesma-vari%C3%A1vel)
  - [Comportamento padrão Array.prototype.sort()](#comportamento-padr%C3%A3o-arrayprototypesort)
- [📚 Outros recursos](#-outros-recursos)
- [🎓 Licença](#-licen%C3%A7a)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 💪🏻 Motivação

> Just for fun
>
> &mdash; _[**“Just for Fun: The Story of an Accidental Revolutionary”**](https://en.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

O objetivo dessa lista era coletar alguns exemplos malucos e explicar como eles funcionam, se possível. Apenas porque é legal aprender algo que nós não conhecemos.

Se você é um iniciante, você poderá utilizar esses pontos para se aprofundar no JavaScript. Eu espero que esses pontos te motivem em gastar um pouco mais de tempo lendo as especificações.

Se você já é um desenvolvedor profissional, você pode considerar esses exemplos como uma excelente referência para todos as peculiaridades e pontos inesperados do nosso amado JavaScript.

Em todo caso, leia. Você provavelmemte irá aprender algo novo.

# ✍🏻 Notação

**`// ->`** é utilizado para mostrar o resultado de uma expressão. Por exemplo:

```js
1 + 1; // -> 2
```

**`// >`** significa o resultado de `console.log` ou qualquer outra saída. Por exemplo:

```js
console.log("hello, world!"); // -> hello, world!
```

**`//`** são apenas comentários para as explicações. Exemplo:

```js
// Atribuindo uma função para a constante foo
const foo = function() {};
```

# 👀 Exemplos

## `[]` é igual a `![]`

Array é igual a not array:

```js
[] == ![]; // -> true
```

### 💡 Explicação:

O operador abstrato de igualdade converte os dois lados em números para compará-los, e os dois lados se tornam `0` por razões diferentes. Arrays são verdadeiros (truthy), então na direita, o oposto de um valor verdadeiro é `false`, o que é coagido para `0`. Na esquerda, todavia, um array vazio é coagido para um número sem se tornar um booleano (boolean) primeiro, e arrays vazios sempre forçados para `0`, apesar de serem verdadeiros.

Aqui está uma simplificação dessa expressão:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

Veja também [`[]` is truthy, but not `true`](#-is-truthy-but-not-true).

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true` não é igual a `![]`, nem igual a `[]` também

Array não é igual a `true`, mas not Array também não é igual a `true`'
Array é igual a `false`, not Array é igual a `false` também:

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 Explicação:

```js
true == []; // -> false
true == ![]; // -> false

// De acordo com a especificação

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

// De acordo com a especificação

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> true

![]; // -> false

false == false; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## true é false

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 Explicação:

Considere esse passo-a-passo:

```js
// true é 'truthy' e representado pelo valor 1 (number), 'true' como string é NaN.
true == "true"; // -> false
false == "false"; // -> false

// 'false' não é uma string vazia, então ele é um valor verdadeiro (truthy)
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

Essa é uma piada antiga no JavaScript, mas remasterizada. Aqui está a forma original:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 Explicação:

A expressão é avaliada como `'foo' + (+'bar')`, o que converte `bar` para um "não número" (NaN - Not a Number).

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 Unary + Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` não é um `NaN`

```js
NaN === NaN; // -> false
```

### 💡 Explicação:

A especificação define estritamente a lógica por trás desse comportamento:

> 1. Se `Type(x)` é diferente de `Type(y)`, retorne **false**.
> 2. Se `Type(x)` é um Number, então
>    1. Se `x` é um **NaN**, retorne **false**.
>    2. Se `y` é um **NaN**, retorne **false**.
>    3. … … …
>
> &mdash; [**7.2.14** Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

Seguindo a definição de `NaN` do IEEE:

> Quatro relações de exclusões mútuas são possíveis: menor que (less than), igual (equal), maior que (greater than), e não ordenado (unordered). O último caso surge quando, pelo menos, um operador é um NaN. Todo NaN deve comprarar não ordenado (unordered) com tudo, incluindo a si mesmo.
>
> &mdash; [“What is the rationale for all comparisons returning false for IEEE754 NaN values?”](https://stackoverflow.com/questions/1565164/1573715#1573715) no StackOverflow

## É uma falha

Você não vai acreditar, mas ...

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 Explicação:

Quando nós quebramos esses símbolos em pedaços, percebemos que o esse padrão se repete com frequência:

```js
![] + []; // -> 'false'
![]; // -> false
```

Então nós tentamos adicionar `[]` para `false`. Mas devido a um número interno de chamadas de função (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`) nós acabamos convertendo o operador da direita para uma string:

```js
![] + [].toString(); // 'false'
```

Pensando em uma string como um array nós conseguimos acessar seu primeiro caractere usando `[0]`:

```js
"false"[0]; // -> 'f'
```

O resto é óbvio, mas o `i` é ardiloso. O `i` em `fail` é pego através da geração da string `'falseundefined'` e pegando o element no índice `['10']`

## `[]` é verdadeiro, mas não `true`

Um array é um valor verdadeiro (truthy), porém, não é igual a `true`.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 Explicação:

Aqui estão links das seções correspondentes especificação do ECMA-262:

- [**12.5.9** Logical NOT Operator (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` é falso, mas não `false`

Apesar do fato que `null` é um valor falso (falsy), ele não é igual a `false`.

```js
!!null; // -> false
null == false; // -> false
```

Ao mesmo tempo, outro valor falso (falsy), como `0` ou `''` são iguais a `false`.

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 Explicação:

A explicação é a mesma dos exemplos anteriores. Aqui está o link correspondente:

- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` é um objeto (object), mas é indefinido (undefined)

> ⚠️ Esta é a parte da API Browser e não irá funcionar em um ambiente com Node.js - apenas em navegadores ⚠️

Apesar de document.all`ser um objeto parecido com um array, ele dá acesso aos nós do DOM na página, e responde como`undefined`na função`typeof`.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

Ao mesmo tempo, `document.all` não é igual a `undefined`.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

Mas ao mesmo tempo:

```js
document.all == null; // -> true
```

### 💡 Explicação:

> `document.all` é usado como uma maneira de acessar todos os elementos do DOM, em particular com versões legadas do IE. Mesmo nunca tendo se tornado um padrão, foi amplamente usado nas eras antigas do JS. Quando o padrão progrediu com novas APIs (como `document.getElementById`) essa API (document.all) se tornou obsoleta e o comitê padrão teve que decidir o que fazer com ela. Por conta do amplo uso eles decidiram deixar a API mas introduziram uma violação intencional da especificação do JavaScript.
> A razão que ele retorna como `false` quando usamos o [Comparador Estrito de Igualdade](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison) com `undefined` e `true` quando usamos o [Comparador Abstrado de Igualdade](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) é devido a essa violação intencional que explicitamente permite isso.
>
> &mdash; [“Obsolete features - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) em WhatWG - HTML spec
>
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) em YDKJS - Types & Grammar

## Valor mínimo é maior que zero

`Number.MIN_VALUE` é o menor número, que ainda é maior que zero:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 Explicação:

> `Number.MIN_VALUE` é igual a `5e-324`, ou seja, o menor número positivo que pode ser representado com precisão float; ou seja, o mais próximo possível de zero. Isso define a melhor resolução que pontos flutuantes (floats) podem fornecer.
>
> Agora, o menor valor geral é `Number.NEGATIVE_INFINITY`, embora ele não seja realmente numérico em um senso estrito.
>
> &mdash; [“Why is `0` less than `Number.MIN_VALUE` in JavaScript?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) no StackOverflow

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## function não é uma function

> ⚠️ Um bug presenta na V8 v5.5 or anterior (Node.js <=7) ⚠️

Todos vocês conhecem a chatice de _undefined is not a function_, mas e quanto a isso?

```js
// Declare uma classe que extende de null
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 Explicação:

Isto não é parte da especificação. É apenas um bug que já foi arrumado, então isso não deverá ser um problema no futuro.

## Somando arrays

E se você tentar somar dois arrays?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 Explicação:

A concatenação ocorre. Passo-a-passo, ela ocorre mais ou menos assim:

```js
[1, 2, 3] +
  [4, 5, 6][
    // call toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concatenation
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## Vírgulas finais em arrays

Você criou um array com 4 elementos vazios. Apesar disso, você terá um array com três elementos, por conta das vírgulas finais (trailing commas):

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 Explicação:

> **Trailing commas** (também chamadas de "final commas", ou em português, "vírgulas finais") são úteis quando você adiciona novos elementos, parâmetros ou propriedades em um código JS. Caso se você quer adicionar uma nova propriedade, você pode simplesmente adicionar uma nova linha sem modificar a anterior se ela já utiliza uma trailling comma. Isso faz com que os _diffs_ no versionamento de código sejam mais limpos, e também a edição do código menos problemática.
>
> &mdash; [Trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) no MDN

## Igualdade entre arrays é um monstro

Igualdade de arrays é um monstro no JS, como você pode ver abaixo:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 Explicação:

Você deve observar bem cautelosamente os exemplos acima! O comportamento é descrito na seção [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) da especificação.

## `undefined` e `Number`

Se nós não passarmos nenhum argumento em um construtor `Number`, nós teremos `0` como retorno. O valor `undefined` é atribuído em argumentos formais quando não não existem argumentos, então você deve esperar que `Number` sem argumentos receba `undefined` como um valor dos seus parâmetros. Todavia, quando passamos `undefined`, o retorno será `NaN`.

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 Explicação:

De acordo com a especificação:

1. Se nenhum argumento for passado na chamada da função, `n` será `+0`.
2. Se não, `n` será ? `ToNumber(value)`.
3. Em caso de `undefined`, `ToNumber(undefined)` deve retornar `NaN`.

Aqui está a seção correspondente:

- [**20.1.1** The Number Constructor](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` é um vilão

`parseInt` é famoso por suas peculiaridades:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 Explicação:**

Isso acontece porque `parseInt` vai continuar parseando caractere por caractere até que ele atinja um caractere desconhecido. O `f` em `f*ck` é o dígito hexadecimal `15`.

Se você parsear `Infinity` para um inteiro…

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

Tenha cuidado quando parsear um `null` também:

```js
parseInt(null, 24); // -> 23
```

**💡 Explicação:**

> Ele converte `null` para uma string `"null"` e tenta fazer o parse. Para raízes de 0 a 23, não existem numerais que ele possa converter, então ele retorna NaN. Em 24, `"n"`, a 14ª letra, é adicionada ao sistema numérico. Em 31, `"u"`, a 21ª letra, é adicionada e a string inteira poderá ser decodificada. Em 37 onde não existe mais nenhum numeral válido definido que poderá ser gerado, o retorno é `NaN`.
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) no StackOverflow

Não se esqueça dos octals:

```js
parseInt("06"); // 6
parseInt("08"); // 8 se suporta ECMAScript 5
parseInt("08"); // 0 se não suporta ECMAScript 5
```

**💡 Explicação:**

Se uma string de entrada começa com "0", a raiz é oito (octal) ou 10 (decimal). A raiz que é escolhida dependerá da implementação. O ECMAScript 5 define que a 10 (decimal) é utilizada, mas nem todos os navegadores suportam isso ainda. Por essa razão sempre deixe explícito qual será a raiz utilizada quando você usar o `parseInt`.

`parseInt` sempre converte a entrada para string:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Tenha cuidado quando tentar fazer o parse de valores _floating ponts_ (pontos flutuantes)

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 Explicação:**

`ParseInt` recebe uma string como argumento e retorna um inteiro da raiz específica. `ParseInt` também remove tudo depois e incluindo o primeiro _non-digit_ (não dígito) no parâmetro como string. `0.000001` é convertido para a string `"0.000001"` e o `parseInt` retorna `0`. Quando `0.0000001` é convertido para uma string ele é tratado como `"1e-7"` e, portanto, `parseInt` retorna `1`. `1/1999999` é interpretado como `5.00000250000125e-7` e o `parseInt` retorna `5`.

## Matemática com `true` e `false`

Vamos fazer algumas contas:

```js
true +
  true(
    // -> 2
    true + true
  ) *
    (true + true) -
  true; // -> 3
```

Hmmm… 🤔

### 💡 Explicação:

Podemos forçar valores números com o construtor `Number`. É bem óbvio que `true` será forçado para `1`:

```js
Number(true); // -> 1
```

O operador unário _soma_ (i++) tenta converter o valor para um número. Ele pode converter representações de inteiros e flutuantes em strings, bem como os valores que não são stings, como `true`, `false` e `null`. Se ele não conseguir parsear um valor particular, então será avaliado como `NaN`. Isso significa que nós podemos forçar `true` para `1` facilmente:

```js
+true; // -> 1
```

Quando você realiza uma adição ou uma multiplicacão, o método `ToNumber` é invocado.
De acordo com a especificação, esse método retorna:

> Se `argument` é **true**, o retorno será **1**. Se `argumento` é `false`, o retorno será **0**.

Por isso podemos adicionar valores booleanos (boolean) como números regulares e obtermos os resultados corretos.

Seções correspondentes:

- [**12.5.6** Unary `+` Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## Comentários HTML são válidos no JavaScript

Você ficará impressionado, mas `<!--` (sintaxe de comentários do HTML) são comentários válidos no JavaScript.

```js
// comentário válido
<!-- comentário válido também
```

### 💡 Explicação:

Impressionado? Comentários HTML se destinavam a permitir que navegadores que não interpretavam a tag `<script>` fossem degradados normalmente. Esses browsers, e.x. Netscape 1.x, não são mais populares. Portanto, não precisamos mais colocar comentários HTML em suas tags script.

Como o Node.js é baseado na V8, comentários HTML são suportados pela runtime do Node.js também. Além disso, eles fazem parte da especificação:

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` ~~não~~ é um número

O tipo `NaN` é um `'number'`:

```js
typeof NaN; // -> 'number'
```

### 💡 Explicação:

Explicações de como os operadores `typeof` e `instanceof` funcionam:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` e `null` são objetos

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// contudo
null instanceof Object; // false
```

### 💡 Explicação:

O comportamento do operador `typeof` é definido nessa seção da especificação:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

De acordo com a especificação, o operador `typeof` retorna uma string de acordo com a [Table 35: `typeof` Operator Results](https://www.ecma-international.org/ecma-262/#table-35). Para `null`, objetos exóticos comuns e exóticos não padronizados, que não implementam `[[Call]]`, o retorno será a string `"object"`.

Todavia, você poderá verificar o tipo de um objeto usando o método `toString`.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## Aumentando números magicamente

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 Explicação:

Isso é causado pelo padrão IEEE 754-2008 para _Binary Floating-Point Arithmetic_ (Aritmética de binários de ponto flutuante). Nessa escala, ele arredonda para o número par mais próximo. Leia mais:

- [**6.1.6** The Number Type](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) na Wikipedia

## Precisão de `0.1 + 0.2`

Uma piada bastante conhecida. Uma adição de `0.1` e `0.2` é mortalmente precisa:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 Explicação:

A responsta para a pergunta [”Is floating point math broken?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) no StackOverflow:

> As constantes `0.2` and `0.3` no seu programa serão também aproximações dos seus valores verdadeiros. Isso ocorre quando o `double` mais próximo de `0.2` é maior que o número racional `0.2`, mas o `double` mais próximo de `0.3` é menor que o número racional `0.3`. A soma de `0.1` e `0.2` acaba sendo maior que o número racional `0.3`, e, portanto, discorda da constante em seu código.

Esse problema é tão conhecido que existe um website chamado [0.30000000000000004.com](http://0.30000000000000004.com/). Isso ocorre em todas as linguagens que utilizam _floating-point math_ (matemática de ponto flutuante), não apenas no JavaScript.

## Patching numbers

Você pode adicionar seus próprios métodos em objetos como `Number` ou `String`.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 Explicação:

Obviamente você pode extender o objeto `Number` como qualquer outro no JavaScript, contudo, não é recomendado se o comportamento do método definido não for parte da especificação. Aqui está a lista de propriedades do `Number`:

- [**20.1** Number Objects](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## Comparação de três números

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 Explicação:

Por que isso funciona assim? Bem, o problema está na primeira parte da expressão. Aqui está como isso funciona:

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

Nós podemos resolver isso com o operador _Maior ou igual que (`>=`)_;

```js
3 > 2 >= 1; // true
```

Leia mais sobre os operadores Relacionais na especificação:

- [**12.10** Relational Operators](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## Matemática engraçada

Geralmente os resultados de operações aritméticas em JavaScript podem ser inespererados. Considere esses exemplos:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 Explicação:

O que está acontecendo com os primeiros quatro exemplos? Aqui está uma tabela para entender a soma no JavaScript:

```
Number  + Number  -> adição
Boolean + Number  -> adição
Boolean + Boolean -> adição
Number  + String  -> concatenação
String  + Boolean -> concatenação
String  + String  -> concatenação
```

E quanto aos outros exempos? Os métodos `ToPrimitive` e `ToString` estão sendo chamados implicitamente por `[]` e `{}` antes da adição. Leia mais sobre o processo de evaluação na especificação:

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

## Soma de RegExps

Você sabia que você pode somar números dessa forma?

```js
// Adicione um método toString
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 Explicação:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## Strings não são instâncias `String`

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 Explicação:

O construtor `String` retorna uma string:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

Vamos tentar com um `new`:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

Objeto? O que é isso?

```js
new String("str"); // -> [String: 'str']
```

Mais informações sobre o construtor String na especificação:

- [**21.1.1** The String Constructor](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## Chamando funções com backticks

Vamos declarar uma função que irá logar todos os parâmetros no console:

```js
function f(...args) {
  return args;
}
```

Sem dúvida, você sabe que uma função pode ser chamada assim:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

Mas você sabia que você pode chamar qualquer função usando _backticks_ (crases)?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 Explicação:

Bom, isso não é uma mágica se você está familiarizado com _Tagged template literals_. No exemplo acima, a função `f` é uma tag para template literal. Tags antes do template literal permitem que você faça o parse do template literals com uma função. O primeiro argumento de uma função tag contém um array de valores em string. O restante dos argumentos são relacionados às expressões. Exemplo:

```js
function template(strings, ...keys) {
  // faça algo com as strings e as chaves...
}
```

Esta é a [mágica por trás](http://mxstbr.blog/2016/11/styled-components-magic-explained/) de uma lib famosa, chamada [💅 styled-components](https://www.styled-components.com/) - que é bem conhecida na comunidade React.

Link para a especificação:

- [**12.3.7** Tagged Templates](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## Call call call

> Achado por [@cramforce](http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 Explicação:

Atenção, isso vai explodir sua mente! Tente reproduzir esse código na sua cabeça: estamos aplicando o método `call` usando o método `apply`. Leia mais:

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## Uma propriedade `constructor`

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 Explicação:

Vamos considerar esse exemplo passo-a-passo:

```js
// Declare uma nova constante, com um valor 'constructor' em string
const c = "constructor";

// c é uma string
c; // -> 'constructor'

// Recuperando o construtor da string
c[c]; // -> [Function: String]

// Recuperando o construtor do construtor
c[c][c]; // -> [Function: Function]

// Chame a função e passe o corpo
// de uma nova função como argumento
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// E então chame essa função anônima
// O Resultado será um log no console com a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

Um `Object.prototype.constructor` retorna a referência da função construtora `Object` que criou a instância do objeto. Em casos com strings ele é `String`, em casos com números ele é um `Number`, e assim por diante.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) no MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## Objeto como uma chave de uma propriedade de objeto

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 Explicação:

Por que isso funciona assim? Aqui estamos usando uma _Computed property name_. Quando você passa um objeto dentro desses colchetes (`{ }`), ele força o objeto para uma string, e então temos a chave `'[object Object]'` com o valor `{}`.

Nós podemos fazer o _"brackets hell"_ dessa forma:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// estrutura:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

Leia mais sobre _object literals_ aqui:

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) no MDN
- [**12.2.6** Object Initializer](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## Acessando protótipos com `__proto__`

Como nós sabemos, os primitivos não tem protótipos. Contudo, se nós tentarmos recuperar o valor de um `__proto__` para primitivos, teremos o seguinte retorno:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 Explicação:

Isso acontece porque quando algo não possui um protótipo, ele será envolvido em um objeto usando o método `ToObject`. Então, seguindo essa linha:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

Aqui temos mais informações sobre `__proto__`:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

Qual é o resultado da expressão abaixo?

```js
`${{ Object }}`;
```

A resposta é:

```js
// -> '[object Object]'
```

### 💡 Explicação:

Nós definimos um objeto com a propriedade `Object` usando a _Shorthand property notation_ (notação curta de propriedade).

```js
{
  Object: Object;
}
```

Então nós passamos esse objeto para o template literal, e o método `toString` chama por aquele objeto. Por isso temos a string `'[object Object]'`.

- [**12.2.9** Template Literals](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Desestruturação com valores padrão

Considere o exemplo:

```js
let x,
  { x: y = 1 } = { x };
y;
```

O exemplo acima é uma excelente tarefa para uma entrevista. Qual é o valor de `y`? A resposta é:

```js
// -> 1
```

### 💡 Explicação:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

Com o exemplo acima:

1. Nós declaramos `x` sem nenhum valor, então ele é `undefined`.
2. Então nós empacotamos o valor de `x` dentro da propriedade `x` do objeto.
3. Depois nós extraímos o valor de `x` usando a desestruturação e queremos atribuí-lo para `y`. Se o valor não for definido, então usaremos `1` como default.
4. Retornarmos o valor de `y`.

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) no MDN

## Pontos e dispersão

Exemplos interessantes podem ser compostos com _spreading_ (dispersão) de arrays. Considere o seguinte:

```js
[...[..."..."]].length; // -> 3
```

### 💡 Explicação:

Por que `3`? Quando utilizamos o [spread operator](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer), o método `@@iterator` é chamado, e o iterator retornado é utilizado para obter os valores para ser iterado. O iterador padrão para string dispersa uma string em caracteres. Depois de dispersar, nós empacotamos esses valores dentro de um array. E então dispersamos esse array novamente e empacotamos de volta em um array.

Uma string de `'...'` consistem em três caracteres de `.`, então o tamanho do array resultante será `3`.

Agora, detalhadamente:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

Obviamente, nós podemos dispersar e envolver elementos de um array quantas vezes quisermos:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// e assim vai ...
```

## Rótulos

Poucos programadores conhecem sobre rótulos no JavaScript, e eles são interessantes:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 Explicação:

A sentença rotulada é utilizada com os comandos `break` ou `continue`. Você pode utilizar um rótulo para identificar um laço de repetição, e então usar os comandos `break` ou `continue` para indicar quando um programa deverá interromper ou continuar a execução de um loop.

No exemplo acima, nós identificamos o rótulo `foo`. Depois disso, é executado o that `console.log('first');` e depois interrompemos a execução.

Leia mais sobre rótulos no JavaScript:

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) no MDN

## Rótulos aninhados

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 Explicação:

Parecido com os exemplos anteriores, acesse esses links:

- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) no MDN

## `try..catch` traidor

O que a seguinte expressão irá retornar? `2` ou `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

A resposta é `3`. Surpreso?

### 💡 Explicação:

- [**13.15** The `try` Statement](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## Isto é herança múltipla?

Observe o exemplo abaixo:

```js
new class F extends (String, Array) {}(); // -> F []
```

Isto é uma herança múltipla? Não.

### 💡 Explicação:

A parte interessante é o valor da cláusula `extends` (`(String, Array)`). O operador de agrupamento sempre retorna seu último argmento, então `(String, Array)` é somente `Array`.
Isso significa que nós criamos uma classe que extende um `Array`.

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## Um gerador que produz a si mesmo

Considere o exemplo de um gerador que produz a si mesmo:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

Como você pode ver, o valor retornado é um objeto com seu `value` igual a `f`. Nesse caso, nós podemos fazer algo assim:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// e assim por diante
// ...
```

### 💡 Explicação:

Para entender porque isso funciona assim, leia essas seções da especificação:

- [**25** Control Abstraction Objects](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** Generator Objects](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## Uma classe de classe

Considere essa sintaxe ofuscada:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

Parece que estamos declarando uma classe dentro de outra. Isso deveria ser um erro, contudo, nós obtemos uma string com `'object'`.

### 💡 Explicação:

Desde o ECMAScript 5, _palavras reservadas_ são permitidas como _nomes de propriedades_. Pense nisso como esse exemplo simples de objeto:

```js
const foo = {
  class: function() {}
};
```

O ES6 padronizou o atalho para definição de métodos. Também, classes podem ser anônimas. Então, se removermos a parte `: function`, teremos o seguinte resultado:

```js
class {
  class() {}
}
```

O resultado de uma classe padrão será sempre um objeto simples. E o seu tipo deverá ser `'object'`.

Leia mais aqui:

- [**14.3** Method Definitions](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## Objetos não coercíveis

Com símbolos bem conhecidos, aqui está uma maneira de se livrar da coerção de tipo. Dê uma olhada:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

Agora podemos usar isso dessa forma:

```js
// objetos
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// strings
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// números
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 Explicação:

- [Um gist de Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## Arrow functions traiçoeiras

Considere o exemplo abaixo:

```js
let f = () => 10;
f(); // -> 10
```

Tá bom, legal, mas e agora isso:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 Explicação:

Você provavelmente espera `{}` ao invés de `undefined`. Isso se dá porque os colchetes (`{}`) são parte da sintaxe das arrow functions, então `f` retornará indefinido. Contudo é possível retornar o objeto `{}` diretamente da arrow function, fechando seu valor dentro das chaves (parênteses).

```js
let f = () => ({});
f(); // -> {}
```

## Arrow functions não podem ser construtores

Considere o exemplo abaixo:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

Agora, tente fazer o mesmo com uma arrow function:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 Explicação:

Arrow functions não podem ser utilizadas como construtores e irão devolver um erro quando utilizadas com `new`. Porque elas possuem seu `this` léxico, e elas não possuem uma propriedade `prototype`, então isso não faria sentido.

## `arguments` e arrow functions

Considere o exemplo abaixo:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

Agora tente o mesmo com uma arrow function:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 Explicação:

Arrow functions são uma versão mais leve das funções regulares, com um foco em serem curtas e com o `this` léxico. Ao mesmo, arrow functions não fornecem uma ligacão para o objeto `argumentos`. Como uma alternativa, utilize os `rest parameters` para ter o mesmo resultado:

```js
let f = (...args) => args;
f("a");
```

- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) no MDN.

## Retorno traiçoeiro

A sentença `return` também é traiçoeira. Considere o seguinte:

```js
(function() {
  return;
  {
    b: 10;
  }
})(); // -> undefined
```

### 💡 Explicação:

`return` e a expressão retornada precisam estar na mesma linha:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

Isso se dá por causa do conceito chamado _Automatic Semicolon Insertion_ (Inserção Automática de Ponto e vírgula), que magicamente insere o ponto e vírgula (`;`) após a maioria das novas linhas. No primeiro exemplo, existe um ponto e vírgula entre a sentença `return` e o objeto, então a função retorna `undefined` e o objeto nunca é avaliado.

- [**11.9.1** Rules of Automatic Semicolon Insertion](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** The `return` Statement](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## Encadeamento atribuições em um objeto

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

Da direita para a esquerda, `{n: 2}` é atribuído para `foo`, e o resultado dessa atribuição `{n: 2}` é atribuído para `foo.x`, e por isso `bar` é `{n: 1, x: {n: 2}}`, pois `bar` é uma referência a `foo`. Mas por que `foo.x` é indefinido enquanto `bar.x` não?

### 💡 Explicação:

Foo e bar referenciam o mesmo objeto `{n: 1}`, e l-values são resolvidos antes das atribuições. `foo = {n: 2}` está criando um novo objeto, e então foo é atualizado para referenciar esse novo objeto. O truque aqui é que foo em `foo.x = ...` como um l-value foi resolvido antes e continua referenciando o objeto antigo `foo = {n: 1}` e o atualiza adicionando o valor de x. Depois desse encadeamento, bar continua referenciando o objeto antigo foo, mas foo referencia o novo objeto `{n: 2}`, onde x não existe.

É equivalente a:

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// bar.x aponta para o novo objeto foo
// e não é equivalente a: bar.x = {n: 2}
```

## Acessando propriedades de objetos usando arrays

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

E quanto aos arrays pseudo-multidimensionais>

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 Explicação:

O operator de colchete `[]` converte a expressão passada usando `toString`. A conversão de um array de um elemento em uma string é semelhante à conversão de um elemento contido em uma string:

```js
["property"].toString(); // -> 'property'
```

## Null e Operadores Relacionais

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 Explicação:

Em resumo, se `null` é menos que `0` e `false`, então `null >= 0` é `true`. Leia a explicação mais detalhada disso [aqui](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274).

## `Number.toFixed()` mostra números diferentes

`Number.toFixed()` pode ter um comportamento estranho em navegadores diferentes. Veja esse exemplo:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 Explicação:

Enquanto seu primeiro instinto é achar que o IE11 está correto e Firefox/Chrome estão errados, a realidade é que Firefox/Chrome são mais obedientes em padrões de números (IEEE-754 Floating Point), enquanto o IE11 é desobediente na tentativa de dar resultados mais claros.

Você pode ver isso acontecendo com alguns testes rápidos:

```js
// Confirme o resultado ímpar do arredondamento de 5 para baixo
(0.7875).toFixed(3); // -> 0.787
// Parece que é apenas 5 quando você expande para os
// limites da precisão de flutuação de 64 bits (precisão dupla)
(0.7875).toFixed(14); // -> 0.78750000000000
// Mas e se formos além do limite?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

Números de ponto flutuante não são salvos internamente como uma lista de dígitos decimais, mas com uma metodologia um pouco mais complicada que produz pequenas imprecisões que são usualmente arredondadas por `toString` ou chamadas similares, mas estão presentes internamente.

Nese caso, aquele "5" no final era atualmente uma fração extremamente pequena abaixo de um 5 verdadeiro. Arredondá-lo a qualquer comprimento razoável o tornará um 5... mas na verdade não é um 5 internamente.

O IE11, no entanto, relatará a entrada de valor apenas com zeros anexados ao final, mesmo no caso toFixed(20), pois parece estar arredondando à força o valor para reduzir os problemas dos limites de hardware.

Veja por referência `NOTE 2` na definição do `toFixed` no ECMA-262.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` menor que `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 Explicação:

- [Por que Math.max() é menor que Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) by Charlie Harvey

## Comparando `null` com `0`

As seguintes expressões parecem introduzir uma contradição:

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

Como `null` não pode ser igual nem maior que`0`, se `null> = 0` é realmente `true`? (Isso também funciona com menor que da mesma maneira.)

### 💡 Explicação:

O jeito que essas três expressões são avaliadas são diferentes e são responsáveis por produzirem esse comportamento inesperado.

Primeiro, a comparação abstrata de igualdade `null == 0`. Normalmente, se o operador não pode comparar os valores dos dois lados, ele converte ambos em números e compara os números. Então, você poderá esperar o seguinte comportamento:

```js
// Isso não é o que acontece
(null == 0 + null) == +0;
0 == 0;
true;
```

Contudo, de acordo com a leitura da especificação, a conversão de números não pode acontecer em um lado que é `null` ou `undefined`. Portanto, se você tem `null` em um lado do sinal de igual, o outro lado precisa ser `null` ou `undefined` para que essa expressão retorne `true`. Como não é esse o caso, o retorno é `false`.

Depois, a comparação relacional `null > 0`. Aqui o algoritmo, diferentemente do operador abstrato de comparação, _irá_ converter `null` em um número. Portanto, temos o seguinte comportamento:

```js
null > 0
+null = +0
0 > 0
false
```

Finalmente, a comparação relacional `null >= 0`. Você pode argumentar que essa expressão deveria ser o resultado de `null > 0 || null == 0`; se fosse esse o caso, então os resultados acima deveriam mostrar que isso também seria `false`. Todavia, o operador `>=` funciona de uma maneira diferente, onde basicamente ele se comporta de maneira oposta ao operador `<`. Como nosso exemplo acima com o operador _maior que_ também é válido para o operador _menor que_, isso significa que essa expressão é realmente avaliada da seguinte forma:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## Redeclaração da mesma variável

JS nos permite declarar variáveis das seguintes formas:

```js
a;
a;
// This is also valid
a, a;
```

Funciona também no modo estrito:

```js
var a, a, a;
var a;
var a;
```

### 💡 Explicação:

Todas as definições são combinadas em uma definição.

- [**13.3.2** Variable Statement](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## Comportamento padrão Array.prototype.sort()

Imagine que você precisa ordenar um array de números.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 Explicação:

A ordem padrão de ordenacão é feita na conversão dos elementos em texto, e depois comparando suas sequências de valores de unidades de código em UFT-16.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### Dica

Passe `comparefn` se você tentar ordenar algo que não seja string.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

# 📚 Outros recursos

- [wtfjs.com](http://wtfjs.com/) — uma coleção dessas várias irregularidades especiais, inconsistências e momentos dolorosos para cada linguagem da web.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — Uma excelente palestra de Gary Bernhardt no CodeMash 2012
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — uma talk de Kyle Simpson para o Forward 2, que tenta “pull out the crazy” do JavaScript. Ele te ajuda a produzir código limpo, elegante, legível e inspirar a contribuir com a comunidade open source.

# 🎓 Licença

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
```

## File: `README-si.md`
```markdown
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

# Table of Contents

- [What the f\*ck JavaScript?](#what-the-f%5Cck-javascript)
  - [Node හි ඇසුරුම් කරන ලද අත්පිටපත](#node-%E0%B7%84%E0%B7%92-%E0%B6%87%E0%B7%83%E0%B7%94%E0%B6%BB%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%9A%E0%B6%BB%E0%B6%B1-%E0%B6%BD%E0%B6%AF-%E0%B6%85%E0%B6%AD%E0%B7%8A%E0%B6%B4%E0%B7%92%E0%B6%A7%E0%B6%B4%E0%B6%AD)
  - [පරිවර්තන](#%E0%B6%B4%E0%B6%BB%E0%B7%92%E0%B7%80%E0%B6%BB%E0%B7%8A%E0%B6%AD%E0%B6%B1)
- [පටුන](#%E0%B6%B4%E0%B6%A7%E0%B7%94%E0%B6%B1)
- [💪 දිරිගැන්වුම](#-%E0%B6%AF%E0%B7%92%E0%B6%BB%E0%B7%92%E0%B6%9C%E0%B7%90%E0%B6%B1%E0%B7%8A%E0%B7%80%E0%B7%94%E0%B6%B8)
- [✍🏻 අංකනය](#-%E0%B6%85%E0%B6%82%E0%B6%9A%E0%B6%B1%E0%B6%BA)
- [👀 උදාහරණ](#-%E0%B6%8B%E0%B6%AF%E0%B7%8F%E0%B7%84%E0%B6%BB%E0%B6%AB)
  - [`[]` සහ `![]` සමානය](#-%E0%B7%83%E0%B7%84--%E0%B7%83%E0%B6%B8%E0%B7%8F%E0%B6%B1%E0%B6%BA)
  - [`true`, `![]`ට සම නොවේ, නමුත් `[]` ට ද සම නොවේ.](#true-%E0%B6%A7-%E0%B7%83%E0%B6%B8-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-%E0%B6%B1%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A--%E0%B6%A7-%E0%B6%AF-%E0%B7%83%E0%B6%B8-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A)
  - [සත්‍යය අසත්‍ය ය](#%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%85%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA-%E0%B6%BA)
  - [baNaNa](#banana)
  - [`NaN` යනු `NaN` නොවේ](#nan-%E0%B6%BA%E0%B6%B1%E0%B7%94-nan-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A)
  - [එය අසාර්ථකත්වයකි](#%E0%B6%91%E0%B6%BA-%E0%B6%85%E0%B7%83%E0%B7%8F%E0%B6%BB%E0%B7%8A%E0%B6%AE%E0%B6%9A%E0%B6%AD%E0%B7%8A%E0%B7%80%E0%B6%BA%E0%B6%9A%E0%B7%92)
  - [`[]` සත්‍යමය නමුත් `true` නොවේ](#-%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%B8%E0%B6%BA-%E0%B6%B1%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A-true-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A)
  - [`null` අසත්‍යමය මුත් `අසත්‍ය` නොවේ](#null-%E0%B6%85%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%B8%E0%B6%BA-%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A-%E0%B6%85%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A)
  - [`document.all` යනු වස්තුවකි, නමුත් එය අර්ථ විරහිතය.](#documentall-%E0%B6%BA%E0%B6%B1%E0%B7%94-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%92-%E0%B6%B1%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A-%E0%B6%91%E0%B6%BA-%E0%B6%85%E0%B6%BB%E0%B7%8A%E0%B6%AE-%E0%B7%80%E0%B7%92%E0%B6%BB%E0%B7%84%E0%B7%92%E0%B6%AD%E0%B6%BA)
  - [අවම අගය, ශුන්‍යය ට වඩා විශාල ය.](#%E0%B6%85%E0%B7%80%E0%B6%B8-%E0%B6%85%E0%B6%9C%E0%B6%BA-%E0%B7%81%E0%B7%94%E0%B6%B1%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%A7-%E0%B7%80%E0%B6%A9%E0%B7%8F-%E0%B7%80%E0%B7%92%E0%B7%81%E0%B7%8F%E0%B6%BD-%E0%B6%BA)
  - [කෘත්‍යය, කෘත්‍යයක් නොවේ](#%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%9A%E0%B7%8A-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A)
  - [අරාවන් ආකලනය](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B6%86%E0%B6%9A%E0%B6%BD%E0%B6%B1%E0%B6%BA)
  - [අරාවක පසුයෙදුම් කොමා](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%9A-%E0%B6%B4%E0%B7%83%E0%B7%94%E0%B6%BA%E0%B7%99%E0%B6%AF%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%9A%E0%B7%9C%E0%B6%B8%E0%B7%8F)
  - [අරාවන් සැසඳීම යක්ෂයෙකි](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B7%83%E0%B7%90%E0%B7%83%E0%B6%B3%E0%B7%93%E0%B6%B8-%E0%B6%BA%E0%B6%9A%E0%B7%8A%E0%B7%82%E0%B6%BA%E0%B7%99%E0%B6%9A%E0%B7%92)
  - [`undefined` සහ `Number`](#undefined-%E0%B7%83%E0%B7%84-number)
  - [`parseInt` නරක මිනිසෙකි](#parseint-%E0%B6%B1%E0%B6%BB%E0%B6%9A-%E0%B6%B8%E0%B7%92%E0%B6%B1%E0%B7%92%E0%B7%83%E0%B7%99%E0%B6%9A%E0%B7%92)
  - [Math with `true` and `false`](#math-with-true-and-false)
  - [JavaScript හි HTML ටීකාවන් වලංගු ය.](#javascript-%E0%B7%84%E0%B7%92-html-%E0%B6%A7%E0%B7%93%E0%B6%9A%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B7%80%E0%B6%BD%E0%B6%82%E0%B6%9C%E0%B7%94-%E0%B6%BA)
  - [`NaN` is ~~not~~ a number](#nan-is-not-a-number)
  - [`[]` සහ `null` වස්තූන් ය.](#-%E0%B7%83%E0%B7%84-null-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%96%E0%B6%B1%E0%B7%8A-%E0%B6%BA)
  - [ඉන්ද්‍රජාලිකව වැඩිවන සංඛ්‍යා](#%E0%B6%89%E0%B6%B1%E0%B7%8A%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%A2%E0%B7%8F%E0%B6%BD%E0%B7%92%E0%B6%9A%E0%B7%80-%E0%B7%80%E0%B7%90%E0%B6%A9%E0%B7%92%E0%B7%80%E0%B6%B1-%E0%B7%83%E0%B6%82%E0%B6%9B%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F)
  - [`0.1 + 0.2` හි නිරවද්‍යතාව](#01--02-%E0%B7%84%E0%B7%92-%E0%B6%B1%E0%B7%92%E0%B6%BB%E0%B7%80%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%AD%E0%B7%8F%E0%B7%80)
  - [සංඛ්‍යා පූරණය](#%E0%B7%83%E0%B6%82%E0%B6%9B%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F-%E0%B6%B4%E0%B7%96%E0%B6%BB%E0%B6%AB%E0%B6%BA)
  - [සංඛ්‍යා තුනක් සැසඳීම](#%E0%B7%83%E0%B6%82%E0%B6%9B%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F-%E0%B6%AD%E0%B7%94%E0%B6%B1%E0%B6%9A%E0%B7%8A-%E0%B7%83%E0%B7%90%E0%B7%83%E0%B6%B3%E0%B7%93%E0%B6%B8)
  - [හාස්‍යජනක ගණිතය](#%E0%B7%84%E0%B7%8F%E0%B7%83%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%A2%E0%B6%B1%E0%B6%9A-%E0%B6%9C%E0%B6%AB%E0%B7%92%E0%B6%AD%E0%B6%BA)
  - [සෙවුම් ප්‍රකාශන ආකලනය](#%E0%B7%83%E0%B7%99%E0%B7%80%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%9A%E0%B7%8F%E0%B7%81%E0%B6%B1-%E0%B6%86%E0%B6%9A%E0%B6%BD%E0%B6%B1%E0%B6%BA)
  - [පෙළ `String` හි නිදර්ශකයක් නොවේ](#%E0%B6%B4%E0%B7%99%E0%B7%85-string-%E0%B7%84%E0%B7%92-%E0%B6%B1%E0%B7%92%E0%B6%AF%E0%B6%BB%E0%B7%8A%E0%B7%81%E0%B6%9A%E0%B6%BA%E0%B6%9A%E0%B7%8A-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A)
  - [පසුලකුණු සමඟ කෘත්‍යයන් ඇමතීම](#%E0%B6%B4%E0%B7%83%E0%B7%94%E0%B6%BD%E0%B6%9A%E0%B7%94%E0%B6%AB%E0%B7%94-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A-%E0%B6%87%E0%B6%B8%E0%B6%AD%E0%B7%93%E0%B6%B8)
  - [අමතන්න අමතන්න අමතන්න](#%E0%B6%85%E0%B6%B8%E0%B6%AD%E0%B6%B1%E0%B7%8A%E0%B6%B1-%E0%B6%85%E0%B6%B8%E0%B6%AD%E0%B6%B1%E0%B7%8A%E0%B6%B1-%E0%B6%85%E0%B6%B8%E0%B6%AD%E0%B6%B1%E0%B7%8A%E0%B6%B1)
  - [තැනුම් ගුණාංගයක්](#%E0%B6%AD%E0%B7%90%E0%B6%B1%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%9C%E0%B7%94%E0%B6%AB%E0%B7%8F%E0%B6%82%E0%B6%9C%E0%B6%BA%E0%B6%9A%E0%B7%8A)
  - [වස්තුවක්, වස්තුවක ගුණයක යතුර ලෙස](#%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%8A-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A-%E0%B6%9C%E0%B7%94%E0%B6%AB%E0%B6%BA%E0%B6%9A-%E0%B6%BA%E0%B6%AD%E0%B7%94%E0%B6%BB-%E0%B6%BD%E0%B7%99%E0%B7%83)
  - [`__proto__` සමඟ මූලාකෘති වෙත ප්‍රවේශ වීම](#__proto__-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B6%B8%E0%B7%96%E0%B6%BD%E0%B7%8F%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%92-%E0%B7%80%E0%B7%99%E0%B6%AD-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%80%E0%B7%9A%E0%B7%81-%E0%B7%80%E0%B7%93%E0%B6%B8)
  - [`` `${{Object}}` ``](#-object-)
  - [පෙරනිමි අගයන් සමඟ බිඳීම](#%E0%B6%B4%E0%B7%99%E0%B6%BB%E0%B6%B1%E0%B7%92%E0%B6%B8%E0%B7%92-%E0%B6%85%E0%B6%9C%E0%B6%BA%E0%B6%B1%E0%B7%8A-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B6%B6%E0%B7%92%E0%B6%B3%E0%B7%93%E0%B6%B8)
  - [තිත් සහ ව්‍යාප්ත කිරීම](#%E0%B6%AD%E0%B7%92%E0%B6%AD%E0%B7%8A-%E0%B7%83%E0%B7%84-%E0%B7%80%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F%E0%B6%B4%E0%B7%8A%E0%B6%AD-%E0%B6%9A%E0%B7%92%E0%B6%BB%E0%B7%93%E0%B6%B8)
  - [නම් පත්](#%E0%B6%B1%E0%B6%B8%E0%B7%8A-%E0%B6%B4%E0%B6%AD%E0%B7%8A)
  - [කූඩු කළ නම්පත්](#%E0%B6%9A%E0%B7%96%E0%B6%A9%E0%B7%94-%E0%B6%9A%E0%B7%85-%E0%B6%B1%E0%B6%B8%E0%B7%8A%E0%B6%B4%E0%B6%AD%E0%B7%8A)
  - [ද්‍රෝහී `try..catch`](#%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%9D%E0%B7%84%E0%B7%93-trycatch)
  - [මෙය බහු උරුමය ද?](#%E0%B6%B8%E0%B7%99%E0%B6%BA-%E0%B6%B6%E0%B7%84%E0%B7%94-%E0%B6%8B%E0%B6%BB%E0%B7%94%E0%B6%B8%E0%B6%BA-%E0%B6%AF)
  - [තමා විසින්ම නිපදවා ගන්නා උත්පාදකයෙක්](#%E0%B6%AD%E0%B6%B8%E0%B7%8F-%E0%B7%80%E0%B7%92%E0%B7%83%E0%B7%92%E0%B6%B1%E0%B7%8A%E0%B6%B8-%E0%B6%B1%E0%B7%92%E0%B6%B4%E0%B6%AF%E0%B7%80%E0%B7%8F-%E0%B6%9C%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B7%8F-%E0%B6%8B%E0%B6%AD%E0%B7%8A%E0%B6%B4%E0%B7%8F%E0%B6%AF%E0%B6%9A%E0%B6%BA%E0%B7%99%E0%B6%9A%E0%B7%8A)
  - [පන්තියක පන්තියක්](#%E0%B6%B4%E0%B6%B1%E0%B7%8A%E0%B6%AD%E0%B7%92%E0%B6%BA%E0%B6%9A-%E0%B6%B4%E0%B6%B1%E0%B7%8A%E0%B6%AD%E0%B7%92%E0%B6%BA%E0%B6%9A%E0%B7%8A)
  - [ආයාස නොකළ හැකි වස්තූන්](#%E0%B6%86%E0%B6%BA%E0%B7%8F%E0%B7%83-%E0%B6%B1%E0%B7%9C%E0%B6%9A%E0%B7%85-%E0%B7%84%E0%B7%90%E0%B6%9A%E0%B7%92-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%96%E0%B6%B1%E0%B7%8A)
  - [උපක්‍රමශීලී ඊතල කෘත්‍යයන්](#%E0%B6%8B%E0%B6%B4%E0%B6%9A%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%B8%E0%B7%81%E0%B7%93%E0%B6%BD%E0%B7%93-%E0%B6%8A%E0%B6%AD%E0%B6%BD-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A)
  - [ඊතල කෘත්‍යයන්ට තනන්නෙකු විය නොහැක](#%E0%B6%8A%E0%B6%AD%E0%B6%BD-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A%E0%B6%A7-%E0%B6%AD%E0%B6%B1%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B7%99%E0%B6%9A%E0%B7%94-%E0%B7%80%E0%B7%92%E0%B6%BA-%E0%B6%B1%E0%B7%9C%E0%B7%84%E0%B7%90%E0%B6%9A)
  - [`arguments` සහ ඊතල කෘත්‍යයන්](#arguments-%E0%B7%83%E0%B7%84-%E0%B6%8A%E0%B6%AD%E0%B6%BD-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A)
  - [උපක්‍රමශීලී ප්‍රතිදානය](#%E0%B6%8B%E0%B6%B4%E0%B6%9A%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%B8%E0%B7%81%E0%B7%93%E0%B6%BD%E0%B7%93-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%AD%E0%B7%92%E0%B6%AF%E0%B7%8F%E0%B6%B1%E0%B6%BA)
  - [වස්තුවක් මත පැවරුම් බැඳීම](#%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%8A-%E0%B6%B8%E0%B6%AD-%E0%B6%B4%E0%B7%90%E0%B7%80%E0%B6%BB%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%B6%E0%B7%90%E0%B6%B3%E0%B7%93%E0%B6%B8)
  - [අරාවන් සමඟ වස්තුන්හි ගුණ වෙත ප්‍රවේශ වීම](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B6%B1%E0%B7%8A%E0%B7%84%E0%B7%92-%E0%B6%9C%E0%B7%94%E0%B6%AB-%E0%B7%80%E0%B7%99%E0%B6%AD-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%80%E0%B7%9A%E0%B7%81-%E0%B7%80%E0%B7%93%E0%B6%B8)
  - [අභිශුන්‍යය සහ බන්ධුතා කාරක](#%E0%B6%85%E0%B6%B7%E0%B7%92%E0%B7%81%E0%B7%94%E0%B6%B1%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B7%83%E0%B7%84-%E0%B6%B6%E0%B6%B1%E0%B7%8A%E0%B6%B0%E0%B7%94%E0%B6%AD%E0%B7%8F-%E0%B6%9A%E0%B7%8F%E0%B6%BB%E0%B6%9A)
  - [`Number.toFixed()` වෙනස් අංක පෙන්වයි](#numbertofixed-%E0%B7%80%E0%B7%99%E0%B6%B1%E0%B7%83%E0%B7%8A-%E0%B6%85%E0%B6%82%E0%B6%9A-%E0%B6%B4%E0%B7%99%E0%B6%B1%E0%B7%8A%E0%B7%80%E0%B6%BA%E0%B7%92)
  - [`Math.min()`ට වඩා `Math.max()` කුඩා ය](#mathmin%E0%B6%A7-%E0%B7%80%E0%B6%A9%E0%B7%8F-mathmax-%E0%B6%9A%E0%B7%94%E0%B6%A9%E0%B7%8F-%E0%B6%BA)
  - [`null` සහ `0` සැසඳීම](#null-%E0%B7%83%E0%B7%84-0-%E0%B7%83%E0%B7%90%E0%B7%83%E0%B6%B3%E0%B7%93%E0%B6%B8)
  - [එකම විචල්‍යය ප්‍රති ප්‍රකාශ කිරීම](#%E0%B6%91%E0%B6%9A%E0%B6%B8-%E0%B7%80%E0%B7%92%E0%B6%A0%E0%B6%BD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%AD%E0%B7%92-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%9A%E0%B7%8F%E0%B7%81-%E0%B6%9A%E0%B7%92%E0%B6%BB%E0%B7%93%E0%B6%B8)
  - [සාමාන්‍ය හැසිරීම Array.prototype.sort()](#%E0%B7%83%E0%B7%8F%E0%B6%B8%E0%B7%8F%E0%B6%B1%E0%B7%8A%E2%80%8D%E0%B6%BA-%E0%B7%84%E0%B7%90%E0%B7%83%E0%B7%92%E0%B6%BB%E0%B7%93%E0%B6%B8-arrayprototypesort)
- [📚 වෙනත් සම්පත්](#-%E0%B7%80%E0%B7%99%E0%B6%B1%E0%B6%AD%E0%B7%8A-%E0%B7%83%E0%B6%B8%E0%B7%8A%E0%B6%B4%E0%B6%AD%E0%B7%8A)
- [🎓 බලපත්‍රය](#-%E0%B6%B6%E0%B6%BD%E0%B6%B4%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%BA)
- [What the f\*ck JavaScript?](#what-the-f%5Cck-javascript-1)
  - [Node හි ඇසුරුම් කරන ලද අත්පිටපත](#node-%E0%B7%84%E0%B7%92-%E0%B6%87%E0%B7%83%E0%B7%94%E0%B6%BB%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%9A%E0%B6%BB%E0%B6%B1-%E0%B6%BD%E0%B6%AF-%E0%B6%85%E0%B6%AD%E0%B7%8A%E0%B6%B4%E0%B7%92%E0%B6%A7%E0%B6%B4%E0%B6%AD-1)
  - [පරිවර්තන](#%E0%B6%B4%E0%B6%BB%E0%B7%92%E0%B7%80%E0%B6%BB%E0%B7%8A%E0%B6%AD%E0%B6%B1-1)
- [පටුන](#%E0%B6%B4%E0%B6%A7%E0%B7%94%E0%B6%B1-1)
- [💪 දිරිගැන්වුම](#-%E0%B6%AF%E0%B7%92%E0%B6%BB%E0%B7%92%E0%B6%9C%E0%B7%90%E0%B6%B1%E0%B7%8A%E0%B7%80%E0%B7%94%E0%B6%B8-1)
- [✍🏻 අංකනය](#-%E0%B6%85%E0%B6%82%E0%B6%9A%E0%B6%B1%E0%B6%BA-1)
- [👀 උදාහරණ](#-%E0%B6%8B%E0%B6%AF%E0%B7%8F%E0%B7%84%E0%B6%BB%E0%B6%AB-1)
  - [`[]` සහ `![]` සමානය](#-%E0%B7%83%E0%B7%84--%E0%B7%83%E0%B6%B8%E0%B7%8F%E0%B6%B1%E0%B6%BA-1)
  - [`true`, `![]`ට සම නොවේ, නමුත් `[]` ට ද සම නොවේ.](#true-%E0%B6%A7-%E0%B7%83%E0%B6%B8-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-%E0%B6%B1%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A--%E0%B6%A7-%E0%B6%AF-%E0%B7%83%E0%B6%B8-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-1)
  - [සත්‍යය අසත්‍ය ය](#%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%85%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA-%E0%B6%BA-1)
  - [baNaNa](#banana-1)
  - [`NaN` යනු `NaN` නොවේ](#nan-%E0%B6%BA%E0%B6%B1%E0%B7%94-nan-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-1)
  - [එය අසාර්ථකත්වයකි](#%E0%B6%91%E0%B6%BA-%E0%B6%85%E0%B7%83%E0%B7%8F%E0%B6%BB%E0%B7%8A%E0%B6%AE%E0%B6%9A%E0%B6%AD%E0%B7%8A%E0%B7%80%E0%B6%BA%E0%B6%9A%E0%B7%92-1)
  - [`[]` සත්‍යමය නමුත් `true` නොවේ](#-%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%B8%E0%B6%BA-%E0%B6%B1%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A-true-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-1)
  - [`null` අසත්‍යමය මුත් `අසත්‍ය` නොවේ](#null-%E0%B6%85%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%B8%E0%B6%BA-%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A-%E0%B6%85%E0%B7%83%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-1)
  - [`document.all` යනු වස්තුවකි, නමුත් එය අර්ථ විරහිතය.](#documentall-%E0%B6%BA%E0%B6%B1%E0%B7%94-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%92-%E0%B6%B1%E0%B6%B8%E0%B7%94%E0%B6%AD%E0%B7%8A-%E0%B6%91%E0%B6%BA-%E0%B6%85%E0%B6%BB%E0%B7%8A%E0%B6%AE-%E0%B7%80%E0%B7%92%E0%B6%BB%E0%B7%84%E0%B7%92%E0%B6%AD%E0%B6%BA-1)
  - [අවම අගය, ශුන්‍යය ට වඩා විශාල ය.](#%E0%B6%85%E0%B7%80%E0%B6%B8-%E0%B6%85%E0%B6%9C%E0%B6%BA-%E0%B7%81%E0%B7%94%E0%B6%B1%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%A7-%E0%B7%80%E0%B6%A9%E0%B7%8F-%E0%B7%80%E0%B7%92%E0%B7%81%E0%B7%8F%E0%B6%BD-%E0%B6%BA-1)
  - [කෘත්‍යය, කෘත්‍යයක් නොවේ](#%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%9A%E0%B7%8A-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-1)
  - [අරාවන් ආකලනය](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B6%86%E0%B6%9A%E0%B6%BD%E0%B6%B1%E0%B6%BA-1)
  - [අරාවක පසුයෙදුම් කොමා](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%9A-%E0%B6%B4%E0%B7%83%E0%B7%94%E0%B6%BA%E0%B7%99%E0%B6%AF%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%9A%E0%B7%9C%E0%B6%B8%E0%B7%8F-1)
  - [අරාවන් සැසඳීම යක්ෂයෙකි](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B7%83%E0%B7%90%E0%B7%83%E0%B6%B3%E0%B7%93%E0%B6%B8-%E0%B6%BA%E0%B6%9A%E0%B7%8A%E0%B7%82%E0%B6%BA%E0%B7%99%E0%B6%9A%E0%B7%92-1)
  - [`undefined` සහ `Number`](#undefined-%E0%B7%83%E0%B7%84-number-1)
  - [`parseInt` නරක මිනිසෙකි](#parseint-%E0%B6%B1%E0%B6%BB%E0%B6%9A-%E0%B6%B8%E0%B7%92%E0%B6%B1%E0%B7%92%E0%B7%83%E0%B7%99%E0%B6%9A%E0%B7%92-1)
  - [Math with `true` and `false`](#math-with-true-and-false-1)
  - [JavaScript හි HTML ටීකාවන් වලංගු ය.](#javascript-%E0%B7%84%E0%B7%92-html-%E0%B6%A7%E0%B7%93%E0%B6%9A%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B7%80%E0%B6%BD%E0%B6%82%E0%B6%9C%E0%B7%94-%E0%B6%BA-1)
  - [`NaN` is ~~not~~ a number](#nan-is-not-a-number-1)
  - [`[]` සහ `null` වස්තූන් ය.](#-%E0%B7%83%E0%B7%84-null-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%96%E0%B6%B1%E0%B7%8A-%E0%B6%BA-1)
  - [ඉන්ද්‍රජාලිකව වැඩිවන සංඛ්‍යා](#%E0%B6%89%E0%B6%B1%E0%B7%8A%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%A2%E0%B7%8F%E0%B6%BD%E0%B7%92%E0%B6%9A%E0%B7%80-%E0%B7%80%E0%B7%90%E0%B6%A9%E0%B7%92%E0%B7%80%E0%B6%B1-%E0%B7%83%E0%B6%82%E0%B6%9B%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F-1)
  - [`0.1 + 0.2` හි නිරවද්‍යතාව](#01--02-%E0%B7%84%E0%B7%92-%E0%B6%B1%E0%B7%92%E0%B6%BB%E0%B7%80%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%AD%E0%B7%8F%E0%B7%80-1)
  - [සංඛ්‍යා පූරණය](#%E0%B7%83%E0%B6%82%E0%B6%9B%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F-%E0%B6%B4%E0%B7%96%E0%B6%BB%E0%B6%AB%E0%B6%BA-1)
  - [සංඛ්‍යා තුනක් සැසඳීම](#%E0%B7%83%E0%B6%82%E0%B6%9B%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F-%E0%B6%AD%E0%B7%94%E0%B6%B1%E0%B6%9A%E0%B7%8A-%E0%B7%83%E0%B7%90%E0%B7%83%E0%B6%B3%E0%B7%93%E0%B6%B8-1)
  - [හාස්‍යජනක ගණිතය](#%E0%B7%84%E0%B7%8F%E0%B7%83%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%A2%E0%B6%B1%E0%B6%9A-%E0%B6%9C%E0%B6%AB%E0%B7%92%E0%B6%AD%E0%B6%BA-1)
  - [සෙවුම් ප්‍රකාශන ආකලනය](#%E0%B7%83%E0%B7%99%E0%B7%80%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%9A%E0%B7%8F%E0%B7%81%E0%B6%B1-%E0%B6%86%E0%B6%9A%E0%B6%BD%E0%B6%B1%E0%B6%BA-1)
  - [පෙළ `String` හි නිදර්ශකයක් නොවේ](#%E0%B6%B4%E0%B7%99%E0%B7%85-string-%E0%B7%84%E0%B7%92-%E0%B6%B1%E0%B7%92%E0%B6%AF%E0%B6%BB%E0%B7%8A%E0%B7%81%E0%B6%9A%E0%B6%BA%E0%B6%9A%E0%B7%8A-%E0%B6%B1%E0%B7%9C%E0%B7%80%E0%B7%9A-1)
  - [පසුලකුණු සමඟ කෘත්‍යයන් ඇමතීම](#%E0%B6%B4%E0%B7%83%E0%B7%94%E0%B6%BD%E0%B6%9A%E0%B7%94%E0%B6%AB%E0%B7%94-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A-%E0%B6%87%E0%B6%B8%E0%B6%AD%E0%B7%93%E0%B6%B8-1)
  - [අමතන්න අමතන්න අමතන්න](#%E0%B6%85%E0%B6%B8%E0%B6%AD%E0%B6%B1%E0%B7%8A%E0%B6%B1-%E0%B6%85%E0%B6%B8%E0%B6%AD%E0%B6%B1%E0%B7%8A%E0%B6%B1-%E0%B6%85%E0%B6%B8%E0%B6%AD%E0%B6%B1%E0%B7%8A%E0%B6%B1-1)
  - [තැනුම් ගුණාංගයක්](#%E0%B6%AD%E0%B7%90%E0%B6%B1%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%9C%E0%B7%94%E0%B6%AB%E0%B7%8F%E0%B6%82%E0%B6%9C%E0%B6%BA%E0%B6%9A%E0%B7%8A-1)
  - [වස්තුවක්, වස්තුවක ගුණයක යතුර ලෙස](#%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%8A-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A-%E0%B6%9C%E0%B7%94%E0%B6%AB%E0%B6%BA%E0%B6%9A-%E0%B6%BA%E0%B6%AD%E0%B7%94%E0%B6%BB-%E0%B6%BD%E0%B7%99%E0%B7%83-1)
  - [`__proto__` සමඟ මූලාකෘති වෙත ප්‍රවේශ වීම](#__proto__-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B6%B8%E0%B7%96%E0%B6%BD%E0%B7%8F%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%92-%E0%B7%80%E0%B7%99%E0%B6%AD-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%80%E0%B7%9A%E0%B7%81-%E0%B7%80%E0%B7%93%E0%B6%B8-1)
  - [`` `${{Object}}` ``](#-object--1)
  - [පෙරනිමි අගයන් සමඟ බිඳීම](#%E0%B6%B4%E0%B7%99%E0%B6%BB%E0%B6%B1%E0%B7%92%E0%B6%B8%E0%B7%92-%E0%B6%85%E0%B6%9C%E0%B6%BA%E0%B6%B1%E0%B7%8A-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B6%B6%E0%B7%92%E0%B6%B3%E0%B7%93%E0%B6%B8-1)
  - [තිත් සහ ව්‍යාප්ත කිරීම](#%E0%B6%AD%E0%B7%92%E0%B6%AD%E0%B7%8A-%E0%B7%83%E0%B7%84-%E0%B7%80%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B7%8F%E0%B6%B4%E0%B7%8A%E0%B6%AD-%E0%B6%9A%E0%B7%92%E0%B6%BB%E0%B7%93%E0%B6%B8-1)
  - [නම් පත්](#%E0%B6%B1%E0%B6%B8%E0%B7%8A-%E0%B6%B4%E0%B6%AD%E0%B7%8A-1)
  - [කූඩු කළ නම්පත්](#%E0%B6%9A%E0%B7%96%E0%B6%A9%E0%B7%94-%E0%B6%9A%E0%B7%85-%E0%B6%B1%E0%B6%B8%E0%B7%8A%E0%B6%B4%E0%B6%AD%E0%B7%8A-1)
  - [ද්‍රෝහී `try..catch`](#%E0%B6%AF%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%9D%E0%B7%84%E0%B7%93-trycatch-1)
  - [මෙය බහු උරුමය ද?](#%E0%B6%B8%E0%B7%99%E0%B6%BA-%E0%B6%B6%E0%B7%84%E0%B7%94-%E0%B6%8B%E0%B6%BB%E0%B7%94%E0%B6%B8%E0%B6%BA-%E0%B6%AF-1)
  - [තමා විසින්ම නිපදවා ගන්නා උත්පාදකයෙක්](#%E0%B6%AD%E0%B6%B8%E0%B7%8F-%E0%B7%80%E0%B7%92%E0%B7%83%E0%B7%92%E0%B6%B1%E0%B7%8A%E0%B6%B8-%E0%B6%B1%E0%B7%92%E0%B6%B4%E0%B6%AF%E0%B7%80%E0%B7%8F-%E0%B6%9C%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B7%8F-%E0%B6%8B%E0%B6%AD%E0%B7%8A%E0%B6%B4%E0%B7%8F%E0%B6%AF%E0%B6%9A%E0%B6%BA%E0%B7%99%E0%B6%9A%E0%B7%8A-1)
  - [පන්තියක පන්තියක්](#%E0%B6%B4%E0%B6%B1%E0%B7%8A%E0%B6%AD%E0%B7%92%E0%B6%BA%E0%B6%9A-%E0%B6%B4%E0%B6%B1%E0%B7%8A%E0%B6%AD%E0%B7%92%E0%B6%BA%E0%B6%9A%E0%B7%8A-1)
  - [ආයාස නොකළ හැකි වස්තූන්](#%E0%B6%86%E0%B6%BA%E0%B7%8F%E0%B7%83-%E0%B6%B1%E0%B7%9C%E0%B6%9A%E0%B7%85-%E0%B7%84%E0%B7%90%E0%B6%9A%E0%B7%92-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%96%E0%B6%B1%E0%B7%8A-1)
  - [උපක්‍රමශීලී ඊතල කෘත්‍යයන්](#%E0%B6%8B%E0%B6%B4%E0%B6%9A%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%B8%E0%B7%81%E0%B7%93%E0%B6%BD%E0%B7%93-%E0%B6%8A%E0%B6%AD%E0%B6%BD-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A-1)
  - [ඊතල කෘත්‍යයන්ට තනන්නෙකු විය නොහැක](#%E0%B6%8A%E0%B6%AD%E0%B6%BD-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A%E0%B6%A7-%E0%B6%AD%E0%B6%B1%E0%B6%B1%E0%B7%8A%E0%B6%B1%E0%B7%99%E0%B6%9A%E0%B7%94-%E0%B7%80%E0%B7%92%E0%B6%BA-%E0%B6%B1%E0%B7%9C%E0%B7%84%E0%B7%90%E0%B6%9A-1)
  - [`arguments` සහ ඊතල කෘත්‍යයන්](#arguments-%E0%B7%83%E0%B7%84-%E0%B6%8A%E0%B6%AD%E0%B6%BD-%E0%B6%9A%E0%B7%98%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA%E0%B6%B1%E0%B7%8A-1)
  - [උපක්‍රමශීලී ප්‍රතිදානය](#%E0%B6%8B%E0%B6%B4%E0%B6%9A%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%B8%E0%B7%81%E0%B7%93%E0%B6%BD%E0%B7%93-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%AD%E0%B7%92%E0%B6%AF%E0%B7%8F%E0%B6%B1%E0%B6%BA-1)
  - [වස්තුවක් මත පැවරුම් බැඳීම](#%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B7%80%E0%B6%9A%E0%B7%8A-%E0%B6%B8%E0%B6%AD-%E0%B6%B4%E0%B7%90%E0%B7%80%E0%B6%BB%E0%B7%94%E0%B6%B8%E0%B7%8A-%E0%B6%B6%E0%B7%90%E0%B6%B3%E0%B7%93%E0%B6%B8-1)
  - [අරාවන් සමඟ වස්තුන්හි ගුණ වෙත ප්‍රවේශ වීම](#%E0%B6%85%E0%B6%BB%E0%B7%8F%E0%B7%80%E0%B6%B1%E0%B7%8A-%E0%B7%83%E0%B6%B8%E0%B6%9F-%E0%B7%80%E0%B7%83%E0%B7%8A%E0%B6%AD%E0%B7%94%E0%B6%B1%E0%B7%8A%E0%B7%84%E0%B7%92-%E0%B6%9C%E0%B7%94%E0%B6%AB-%E0%B7%80%E0%B7%99%E0%B6%AD-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B7%80%E0%B7%9A%E0%B7%81-%E0%B7%80%E0%B7%93%E0%B6%B8-1)
  - [අභිශුන්‍යය සහ බන්ධුතා කාරක](#%E0%B6%85%E0%B6%B7%E0%B7%92%E0%B7%81%E0%B7%94%E0%B6%B1%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B7%83%E0%B7%84-%E0%B6%B6%E0%B6%B1%E0%B7%8A%E0%B6%B0%E0%B7%94%E0%B6%AD%E0%B7%8F-%E0%B6%9A%E0%B7%8F%E0%B6%BB%E0%B6%9A-1)
  - [`Number.toFixed()` වෙනස් අංක පෙන්වයි](#numbertofixed-%E0%B7%80%E0%B7%99%E0%B6%B1%E0%B7%83%E0%B7%8A-%E0%B6%85%E0%B6%82%E0%B6%9A-%E0%B6%B4%E0%B7%99%E0%B6%B1%E0%B7%8A%E0%B7%80%E0%B6%BA%E0%B7%92-1)
  - [`Math.min()`ට වඩා `Math.max()` කුඩා ය](#mathmin%E0%B6%A7-%E0%B7%80%E0%B6%A9%E0%B7%8F-mathmax-%E0%B6%9A%E0%B7%94%E0%B6%A9%E0%B7%8F-%E0%B6%BA-1)
  - [`null` සහ `0` සැසඳීම](#null-%E0%B7%83%E0%B7%84-0-%E0%B7%83%E0%B7%90%E0%B7%83%E0%B6%B3%E0%B7%93%E0%B6%B8-1)
  - [එකම විචල්‍යය ප්‍රති ප්‍රකාශ කිරීම](#%E0%B6%91%E0%B6%9A%E0%B6%B8-%E0%B7%80%E0%B7%92%E0%B6%A0%E0%B6%BD%E0%B7%8A%E2%80%8D%E0%B6%BA%E0%B6%BA-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%AD%E0%B7%92-%E0%B6%B4%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%9A%E0%B7%8F%E0%B7%81-%E0%B6%9A%E0%B7%92%E0%B6%BB%E0%B7%93%E0%B6%B8-1)
  - [සාමාන්‍ය හැසිරීම Array.prototype.sort()](#%E0%B7%83%E0%B7%8F%E0%B6%B8%E0%B7%8F%E0%B6%B1%E0%B7%8A%E2%80%8D%E0%B6%BA-%E0%B7%84%E0%B7%90%E0%B7%83%E0%B7%92%E0%B6%BB%E0%B7%93%E0%B6%B8-arrayprototypesort-1)
- [📚 වෙනත් සම්පත්](#-%E0%B7%80%E0%B7%99%E0%B6%B1%E0%B6%AD%E0%B7%8A-%E0%B7%83%E0%B6%B8%E0%B7%8A%E0%B6%B4%E0%B6%AD%E0%B7%8A-1)
- [🎓 බලපත්‍රය](#-%E0%B6%B6%E0%B6%BD%E0%B6%B4%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%BA-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> හාස්‍යජනක සහ දුරවබෝධ JavaScript උදාහරණ

JavaScript යනු විශිෂ්ට ක්‍රමලේඛන භාෂාවකි.එයට සරල වින්‍යාසයක් සහ පුළුල් පද්ධතියක් ඇති අතර වඩාත්ම වැදගත් කරුණක් ලෙස එය සතුව විශිෂ්ට ප්‍රජාවක් සිටී.කෙසේ නමුත් JavaScript ක්‍රමලේඛන භාෂාවේ වටහා ගැනීමට දුෂ්කර කොටස් ද ඇති බව අපි සියල්ලෝම දනිමු. මෙවැනි සමහරක් කො ටස් අපගේ එදිනෙදා ක්‍රමලේඛන කාර්යයන් ඉක්මනින් මහත් අවුලට පත් කිරීමට සමත් අතර තවත් සමහරක් අපව මහා හඬින් සිනහ නැංවීමට සමත්ය.

WTFJS සඳහා මුල් අදහසේ හිමිකම Brian Leroux සතුය.මෙම ලැයිස්තුව ඔහුගේ [2012 DOTJS හි WTFJS දේශනය](https://www.youtube.com/watch?v=et8xNAc2ic8) විසින් පොළඹවන ලද්දකි.

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

## Node හි ඇසුරුම් කරන ලද අත්පිටපත

ඔබට මෙම අත්පොත npm හරහා ස්ථාපනය කරගත හැකිය.මේ සඳහා පහත විධානය ක්‍රියාත්මක කරන්න.

    $ npm install -g wtfjs

දැන් ඔබට විධාන පෙළ හරහා wtfjs ක්‍රියාත්මක කළ හැකි විය යුතුය. මෙය තෝරාගත් $PAGER හි අත්පිටපත විවෘත කරනු ඇත. එසේ නැත්නම් ඔබට මෙහිදී නොනැවතී කියවිය හැකිය.

මූලය මෙහිදී ලබාගත හැක: https://github.com/denysdovhan/wtfjs

## පරිවර්තන

දැනට wtfjs හි පහත පරිවර්තන පවතී.

- [中文版](https://github.com/denysdovhan/wtfjs/blob/master/README-zh-cn.md)

[නව පරිවර්තනයක් ඉල්ලන්න](https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D)

# පටුන

- [💪 දිරිගැන්වුම](#-දිරිගැන්වුම)
- [✍🏻 අංකනය](#-අංකනය)
- [👀 උදාහරණ](#-උදාහරණ)
  - [`[]` සහ `![] සම වේ`](#-සහ--සමානය)
  - [`true` සහ `![]` සම නොවේ, නමුත් `[]` ද සම නොවේ.](#true-ට-සම-නොවේ-නමුත්--ට-ද-සම-නොවේ)
  - [සත්‍යය අසත්‍යය](#සත්යය-අසත්ය-ය)
  - [baNaNa](#banana)
  - [`NaN` යනු `NaN` නොවේ](#nan-යනු-nan-නොවේ)
  - [එය අසාර්ථකත්වයකි]()
  - [`[]` සත්‍යමය මුත් `සත්‍ය` නොවේ](#-is-truthy-but-not-true)
  - [null අසත්‍යමය මුත් `අසත්‍ය` නොවේ](#null-අසත්යමය-මුත්-අසත්ය-නොවේ)
  - [`document.all` යනු වස්තුවකි , නමුත් එය අර්ථ විරහිතය ](#documentall-යනු-වස්තුවකි-නමුත්-එය-අර්ථ-විරහිතය)
  - [අවම අගය ශුන්‍යයට වඩා විශාලය](#අවම-අගය-ශුන්යය-ට-වඩා-විශාල-ය)
  - [කෘත්‍යය කෘත්‍යයක් නොවේ](#කෘත්යය-කෘත්යයක්-නොවේ)
  - [අරාවන් ආකලනය](#අරාවන්-ආකලනය)
  - [අරාවක පසුයෙදුම් කොමා](#අරාවක-පසුයෙදුම්-කොමා)
  - [අරාවන් සමානතාව යක්ෂයෙකි](#array-equality-is-a-monster)
  - [`undefined` සහ `Number`](#undefined-සහ-number)
  - [`parseInt` නරක පුද්ගලයෙකි](#parseint-is-a-bad-guy)
  - [`සත්‍ය` සහ `අසත්‍ය` සමඟ ගණිතය](#math-with-true-and-false)
  - [JavaScript හි HTML ටීකාවන් වලංගුය](#javascript-හි-html-ටීකාවන්-වලංගු-ය)
  - [`NaN` යනු සංඛ්‍යාවක් නොවේ](#nan-is-not-a-number)
  - [`[]` සහ `null` යනු වස්තූන් ය](#-සහ-null-වස්තූන්-ය)
  - [ඉන්ද්‍රජාලික ව ඉහළ යන අංක](#ඉන්ද්රජාලිකව-වැඩිවන-සංඛ්යා)
  - [`0.1 + 0.2` හි නිරවද්‍යතාව]()
  - [සංඛ්‍යා ඌනපූර්ණය](#patching-numbers)
  - [අංක තුනක් සැසඳීම](#සංඛ්යා-තුනක්-සැසඳීම)
  - [හාස්‍යජනක ගණිතය](#හාස්යජනක-ගණිතය)
  - [සෙවුම් ප්‍රකාශන ආකලනය](#addition-of-regexps)
  - [පෙළ, `String` හි නිදර්ශක නොවේ](#පෙළ--string-හි-නිදර්ශකයක්-නොවේ)
  - [පසුලකුණු සමඟ කෘත්‍යයන් ඇමතීම](#පසුලකුණු-සමඟ-කෘත්යයන්-ඇමතීම)
  - [අමතන්න අමතන්න අමතන්න]()
  - [`ඉදිකරන්නා` ගුණයක්](#a-constructor-property)
  - [වස්තුව, වස්තුවක ගුණයක යතුරක් ලෙස](#object-as-a-key-of-objects-property)
  - [ `__proto__` සමඟ මූලාකෘති වෙත ප්‍රවේශ වීම](#__proto__-සමඟ-මූලාකෘති-වෙත-ප්රවේශ-වීම)
  - [`` `${{Object}}` ``](#object)
  - [පෙරනිමි අගයන් සමඟ බිඳීම](#පෙරනිමි-අගයන්-සමඟ-බිඳීම)
  - [තිත් සහ ව්‍යාප්ත කිරීම](#තිත්-සහ-ව්යාප්ත-කිරීම)
  - [නම්පත්](#නම්-පත්)
  - [කූඩු කළ නම්පත්](#කූඩු-කළ-නම්පත්)
  - [ද්‍රෝහී `try..catch`](#ද්රෝහී-trycatch)
  - [මෙය බහු උරුමය ද?](#මෙය-බහු-උරුමය-ද)
  - [තමා විසින්ම උත්පාදනය වන උත්පාදකයෙක්](#තමා-විසින්ම-නිපදවා-ගන්නා-උත්පාදකයෙක්)
  - [පන්තියක පන්තියක්](#පන්තියක-පන්තියක්)
  - [ආයාස නොකළැකි වස්තූන්](#non-coercible-objects)
  - [උපක්‍රමශීලී ඊතල කෘත්‍යයන්](#උපක්රමශීලී-ඊතල-කෘත්යයන්)
  - [ඊතල කෘත්‍යයන්ට තනන්නෙකු විය නොහැක](#ඊතල-කෘත්යයන්ට-තනන්නෙකු-විය-නොහැක)
  - [`පරාමිතික අගයන්` සහ ඊතල කෘත්‍යයන්]()
  - [උපායශීලී ප්‍රතිදානය](#උපක්රමශීලී-ප්රතිදානය)
  - [වස්තුවක් මත පැවරුම් බැඳීම](#වස්තුවක්-මත-පැවරුම්-බැඳීම)
  - [අරාවන් සමඟ වස්තුවක ගුණ වෙත ප්‍රවේශ වීම](#අරාවන්-සමඟ-වස්තුන්හි-ගුණ-වෙත-ප්රවේශ-වීම)
  - [අභිශුන්‍යය සහ බන්ධුතා කාරක](#අභිශුන්යය--සහ-බන්ධුතා-කාරක)
  - [`Number.toFixed()` වෙනස් අංක පෙන්වයි](#numbertofixed-වෙනස්-අංක-පෙන්වයි)
  - [`Math.max()`, `Math.min()`ට වඩා කුඩා ය](#mathminට-වඩා-mathmax-කුඩා-ය)
  - [`අභිශුන්‍යය` සහ `ශුන්‍යය` සැසඳීම](#null-සහ-0-සැසඳීම)
  - [එකම විචල්‍යය ප්‍රතිප්‍රකාශ කිරීම](#එකම-විචල්යය-ප්රති-ප්රකාශ-කිරීම)
  - [සාමාන්‍ය හැසිරීම Array.prototype.sort()](#සාමාන්ය-හැසිරීම-arrayprototypesort)
- [වෙනත් සම්පත්](#-වෙනත්-සම්පත්)
- [🎓 බලපත්‍රය](#-බලපත්රය)

# 💪 දිරිගැන්වුම

> හුදෙක් විනෝදය උදෙසා
>
> &mdash; _[**“හුදෙක් විනෝදය උදෙසා: අහඹු විප්ලවයක කතාව”**](https://en.wikipedia.org/wiki/Just_for_Fun), ලීනස් ටොවාල්ඩ්ස්_

මෙම ලැයිස්තුවේ මූලික අරමුණ වන්නේ උන්මාදනීය උදාහරණ එක්රැස් කිරීම සහ හැකිනම් ඒවා පැහැදිලි කිරීමයි; මක් නිසාද යත් අප මීට පෙර නොදැන සිටි දෙයක් ඉගෙනීම විනෝදජනක බැවිනි.

ඔබ ආධුනිකයකු නම් , JavaScript හි ගැඹුරට පිවිසෙන්නට මෙම සටහන් උපකාරී වනු ඇත. පිරිවිතර වැඩියෙන් කියවන්නට සහ ඒ සමඟ කල් ගෙවන්නට මෙම සටහන් ඔබට අභිප්‍රේරණයක් වනු ඇතැයි මම බලාපොරොත්තු වෙමි.

ඔබ වෘත්තීමය සංවර්ධකයෙකු නම්, ඔබට මෙම උදාහරණ අපගේ ආදරණීය JavaScript හි අනපේක්ෂිත සහ අසාමාන්‍ය අංශ පිළිබඳ යොමුවක් ලෙස සැලකිය හැක.

කවුරුන් හෝ වේවා, හුදෙක් මෙය කියවන්න. බොහෝ විට ඔබ අලුත් දෙයක් සොයා ගනු ඇත.

# ✍🏻 අංකනය

**`// ->`** භාවිත කෙරෙන්නේ ප්‍රකාශනයක ප්‍රතිඵලය දැක්වීමටයි. උදා:

```js
1 + 1; // -> 2
```

**`// >`** මඟින් අදහස් වන්නේ console . log () හෝ වෙනත් ප්‍රතිදානයක ප්‍රතිඵලයකි. :

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** යනු හුදෙක් විවරණය සඳහා යොදා ගත් ටීකාවකි. උදා:

```js
// foo නියතයට කෘත්‍යයක් පැවරීම
const foo = function() {};
```

# 👀 උදාහරණ

## `[]` සහ `![]` සමානය

අරාව, නැත අරාව ට සමානය:

```js
[] == ![]; // -> true
```

### 💡 විවරණය:

වියුක්ත සමානතා කාරකය, සැසඳීම සඳහා දෙපසම සංඛ්‍යා බවට හරවයි, මෙවිට දෙපසම වෙනස් හේතු නිසා 0 බවට පත් වේ. අරාවන් සත්‍යමය බැවින් මෙහි දකුණු පස අසත්‍ය යන්නට ද අනතුරුව 0 බවට ද පත්වේ. කෙසේ නමුත් වම් පසෙහි හිස් අරාවක් බූලියානු අගයක් බවට පත් නොවී ම සංඛ්‍යාවක් බවට පත් වේ.(සත්‍යමය වීම නොසලකා, හිස් අරාවන් 0 බවට පත් කෙරේ.)

පහත දැක්වෙන්නේ මෙම ප්‍රකාශනය සරල වන ආකාරයයි.:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

[`[]` සත්‍යමය මුත් `සත්‍ය` නොවේ](#-is-truthy-but-not-true) ද බලන්න.

- [**12.5.9** තාර්කික නිශේධ කාරකය (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** වියුක්ති සමානතා සංසන්දනය](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true`, `![]`ට සම නොවේ, නමුත් `[]` ට ද සම නොවේ.

අරාව සත්‍ය නොවන මුත් නැත අරාව ද සත්‍ය නොවේ
අරාව අසත්‍ය ය, එහෙත් නැත අරාව ද අසත්‍ය ය.

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 විවරණය:

```js
true == []; // -> false
true == ![]; // -> false

// පිරිවිතරයට අනුව

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

// පිරිවිතරයට අනුව

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> false

![]; // -> false

false == false; // -> true
```

- [**7.2.13** වියුක්ති සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## සත්‍යය අසත්‍ය ය

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 විවරණය:

මෙය පියවරෙන් පියවර සලකන්න:

```js
//
true සත්‍යමය වන අතර අගය 1 මඟින් නිරූපණය වේ. පෙළ මාදිලියේදී 'true' යනු සංඛ්‍යාවක් නොවේ
true == "true"; // -> false
false == "false"; // -> false

//  ‘false’ යනු හිස් පෙළක් නොවේ, එමනිසා එය සත්‍යමය අගයකි
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** වියුක්ති සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

මෙය JavaScriptහි පැරණි, එහෙත් වැඩිදියුණු කරන ලද විහිළුවකි.මුල් පිටපත පහත දැක්වේ:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 විවරණය:

මෙම ප්‍රකාශනය `'foo' + (+'bar')` ලෙස නිර්ණය වේ; `'bar'`, “සංඛ්‍යාවක් නොවේ( NaN )” යන්නට පරිවර්තනය වේ.

- [**12.8.3** ආකලන කාරකය (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 ඒකක + කාරකය](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` යනු `NaN` නොවේ

```js
NaN === NaN; // -> false
```

### 💡 විවරණය:

පිරිවිතරය දැඩි ලෙස ම, මෙම හැසිරීමට හේතුවන තර්කය අර්ථ දක්වයි:

> 1. `Type(x)` සහ `Type(y)` වෙනස් නම්, **false** ප්‍රතිදානය කරන්න.
> 2. `Type(x)` සංඛ්‍යාවක් නම්, එවිට,
>    1. If `x`, **NaN** නම්, **false** දෙන්න.
>    2. If `y`, **NaN** නම්, **false** දෙන්න.
>    3. … … …
>
> &mdash; [**7.2.14** දැඩි සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

IEEE හි `NaN` කාරකය පිළිබඳ අර්ථ දැක්වීම අනුගමනය කරමින්:

> අන්‍යොන්‍ය වශයෙන් බහිෂ්කාර බන්ධුතා හතරක් වලංගුය: වඩා කුඩා, සමාන, වඩා විශාල, සහ අපිළිවෙළ වශයෙනි. අවම වශයෙන් එක සම්ප්‍රදානයක් හෝ සංඛ්‍යාවක් නොවන විට අවසාන අවස්ථාව උද්ගත වේ. සෑම “සංඛ්‍යාවක් නොවේ” අගයක් ම , තමා ද ඇතුළු ව, සියල්ල සමඟ අපිළිවෙල සසඳයි.
>
> &mdash; [“IEEE754 සංඛ්‍යාවක් නොවේ අගයන් සැසඳීම් සියල්ල සඳහා අසත්‍ය ප්‍රතිදානය වීමට හේතුව කුමක් ද?”](https://stackoverflow.com/questions/1565164/1573715#1573715) at StackOverflow

## එය අසාර්ථකත්වයකි

ඔබ විශ්වාස නොකරනු ඇත, නමුත් …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 විවරණය:

ඉහත සංකේත පෙළ කැබලිවලට කඩා ගැනීම මඟින්, පහත රටාව නිතර ඇතිවන බව අප හඳුනා ගනී:

```js
![] + []; // -> 'false'
![]; // -> false
```

ඉතින් අපි `false` ට [] එකතු කිරීමට තැත් කරමු. නමුත් අභ්‍යන්තර කෘත්‍ය ඇමතුම් ගණනාවක් නිසා (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`), එය, දකුණු පස පෙළ ට පරිවර්තනය කිරීමෙන් අවසන් වේ.

```js
![] + [].toString(); // 'false'
```

පෙළ අරාවක් ලෙස සැලකීමෙන්, `[0]` මඟින් අපට එහි පළමු අක්ෂරය වෙත ප්‍රවේශ විය හැකිය:

```js
"false"[0]; // -> 'f'
```

ඉතිරිය ප්‍රත්‍යක්ෂ ය., නමුත් i නොමඟ යවන සුළු ය. “fail” හි i යන්න, `['10']` ස්ථානයේ ඇති අවයවය ග්‍රහණය කිරීමෙන් සහ පෙළ `'falseundefined'` උත්පාදනය වීමෙන් ග්‍රහණය කෙරෙනු ලැබේ.

## `[]` සත්‍යමය නමුත් `true` නොවේ

අරාවක් යනු සත්‍යමය අගයකි, කෙසේ නමුත් එය `true` ට සමාන නොවේ.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 විවරණය:

ECMA-262 පිරිවිතරයෙහි අදාළ කොටස් වලට සබැඳි පහත දැක්වේ:

- [**12.5.9** තාර්කික NOT කාරකය (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** වියුක්ත සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` අසත්‍යමය මුත් `අසත්‍ය` නොවේ

`null` අසත්‍යමය යන්න නොසලකා, එය `false` යන්නට සම නොවේ

```js
!!null; // -> false
null == false; // -> false
```

කෙසේ නමුත්, `0` සහ `””` වැනි අසත්‍යමය අගයන් `false` ට සම වේ

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 විවරණය:

විවරණය ඉහත උදාහරණය සඳහා පරිදි ම වේ. අදාළ සබැඳිය පහත දැක්වේ:

- [**7.2.13** වියුක්ත සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` යනු වස්තුවකි, නමුත් එය අර්ථ විරහිතය.

> ⚠️ මෙය පිරික්සුම් යෙදුම් ක්‍රමලේඛ අතුරුමුහුණතේ කොටසක් වන අතර Node.js පරිසරයක ක්‍රියා නොකරනු ඇත ⚠️

`document.all` යන්න අරාවක් වැනි වස්තුවක් ය යන්න නොසලකා, එය, පිටුවේ DOM අවයව වෙත ප්‍රවේශය සපයයි. එය `typeof` කෘත්‍යය ට අර්ථ විරහිත ය යන්නෙන් ප්‍රතිචාර දක්වයි.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

තව ද, `document.all`, `undefined` ට සම නොවේ.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

නමුත්:

```js
document.all == null; // -> true
```

### 💡 විවරණය:

> `document.all`, විශේෂයෙන් IE හි පැරණි මාදිලියන්හිදී, DOM අවයව වෙත ප්‍රවේශ වීමේ මාර්ගයක් ලෙස සැලකුණි. එය කිසි විටෙකත් සම්මතයක් නොවුව ද පැරණි JS කේතයේ එය පුළුල්ව භාවිත විනි. සම්මතය නව අතුරුමුහුණත් සමඟ ප්‍රගමනය වන වූ විට මෙම අතුරුමුහුණත් ඇමතුම යල්පිනූ අතර සම්මත සම්පාදන කොමිසමට එමඟින් කරන්නේ කුමක්ද යන්න තීරණය කිරීමට සිදුව තිබිණි. නමුත් එහි පුළුල් භාවිතය නිසා ඔවුන්, පිරිවිතරයට සචින්ත්‍ය උල්ලංඝනයක් එක් කරමින්, එම අතුරුමුහුණත පවත්වා ගැනීමට තීරණය කරන ලදී.
> දැඩි සමානතා සැසඳීමේ දී එය `false` ට `undefined` ලෙසත්, වියුක්ති සමානතා සැසඳීමේ දී `true` ලෙසත් ප්‍රතිචාර දැක්වීමට හේතුව පිරිවිතරයේ සචින්ත්ය උල්ලංඝනය කිරීමයි.
>
> &mdash; [“යල්පිනු විශේෂාංග - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) at WhatWG - HTML spec
> &mdash; [“පරිච්ජේදය 4 - ToBoolean - අසත්‍යමය අගයන්”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) at YDKJS - Types & Grammar

## අවම අගය, ශුන්‍යය ට වඩා විශාල ය.

`Number.MIN_VALUE` යනු කුඩා ම සංඛ්‍යාවයි; එය ශුන්‍යය ට වඩා විශාල ය:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 විවරණය:

> `Number.MIN_VALUE` හි අගය `5e-324` වන අතර එය float හි නිරවද්‍යතාව යටතේ නිරූපණය කළ හැකි කුඩාම ධන සංඛ්‍යාවයි. එය float දත්ත වර්ගයට ලබා දිය හැකි හොඳම විභේදනය අර්ථ දක්වයි.
>
> තදබල ලෙස සැලකීමේදී සත්‍ය වශයෙන් ම සංඛ්‍යාත්මක නොවුවත්,දැන් සමස්ත කුඩාතම අගය `Number.NEGATIVE_INFINITY` වේ.
>
> &mdash; ["JavaScript හි දී `Number.MIN_VALUE` ට වඩා ශුන්‍යය කුඩා වන්නේ මන් ද?"](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) StackOverflow හි

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## කෘත්‍යය, කෘත්‍යයක් නොවේ

> ⚠️ V8 v5.5 හෝ පහළ (Node.js <=7) පවතින දෝෂයකි ⚠️

ඔබ සැවොම කරදරකාරී _undefined is not a function_ දනී, නමුත් මෙය කුමක් ද?

```js
// null දීර්ඝ කරන පන්තියක් අර්ථ දැක්වීම
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 විවරණය:

මෙය පිරිවිතරයෙහි කොටසක් නොවේ. මෙය මේ වන විට නිරාකරණය කර ඇති දෝෂයකි, එමනිසා අනාගතයේදී මෙවැනි ගැටළුවක් පැන නොනඟිනු ඇත.

## අරාවන් ආකලනය

ඔබ අරාවන් දෙකක් එකතු කිරීමට තැත් කළහොත් කුමක් සිදුවනු ඇත් ද?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 විවරණය:

සමෝච්ජය සිදුවේ. මෙය පියවරෙන් පියවර, පහත පරිදි දැක්විය හැක:

```js
[1, 2, 3] +
  [4, 5, 6][
    //toString() කැඳවන්න
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// සමෝච්ජය
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## අරාවක පසුයෙදුම් කොමා

ඔබ හිස් අයිතම 4 ක අරාවක් නිර්මාණය කර ඇත. කෙසේ නමුත් පසු යෙදුම් කොමාවන් නිසා, ඔබට අවයව 3කින් සමන්විත අරාවක් ලැබෙනු ඇත:

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 විවරණය:

> JavaScript කේතයට නව අවයව, පරාමිතීන් හෝ ගුණාංග එක් කිරීමේදී **පසුයෙදුම් කොමා** ( සමහර විට **අවසන් කොමා** ලෙස හැඳින්වෙන) ප්‍රයෝජනවත් විය හැක. ඔබට නව ගුණයක් එක් කිරීමට අවශ්‍ය විට, කලින් අවසාන පේලිය දැනටමත් පසුයෙදුම් කොමාවක් භාවිත කරන්නේ නම්, ඔබට සරලවම එම පේලිය විකෘත කිරීමකින් තොරව නව පේළියක් එක් කළ හැක. මෙය පිටපත්-පාලන වෙනස්කම් පිරිසිදුව පවත්වා ගන්නා අතරම කේත සංස්කරණ බාධා අවම කරයි.
>
> &mdash; [පසුයෙදුම් කොමා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) at MDN

## අරාවන් සැසඳීම යක්ෂයෙකි

ඔබ ට පහත දැකිය හැකි පරිදි, අරාවන් සැසඳීම යක්ෂයෙකි:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 විවරණය:

ඔබ ඉහත උදාහරණ සඳහා මහත් පරීක්ෂාවෙන් සිටිය යුතුය! මෙම හැසිරීම, පිරිවිතරයේ [**7.2.13** වියුක්ත සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) අංශයේ විස්තර කෙරේ.

## `undefined` සහ `Number`

අප, `Number ` තනන්නාට කිසිදු පරාමිතියක් යොමු නොකරයි නම්, අපට 0 ලැබේ. සත්‍ය පරාමිතීන් නොමැතිවිට නිල පරාමිතීන්ට`අර්ථ විරහිත` අගය පැවරෙයි. මෙනිසා පරාමිති නොමැති `Number`, `අර්ථ විරහිත` යන්න එහි පරාමිතියේ අගය ලෙස ගනු ඇතැයි ඔබ බලාපොරොත්තු විය හැකිය. කෙසේ නමුත්, අප `අර්ථ විරහිත` යොමු කළ විට අපට `සංඛ්‍යාවක් නොවේ` යන්න ලැබේ

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 විවරණය:

පිරිවිතරයට අනුව:

1. මෙම කෘත්‍යයේ ඇමතීමට කිසිදු පරාමිතියක් ලබා දී නැත්නම්, `n = `+0`.ලෙස ගනිමු.
2. නැතිනම්. `n = `ToNumber(value)`.` ලෙස ගනිමු
3. `අර්ථ විරහිත` වීමක දී, `ToNumber(undefined)` විසින් `NaN` ප්‍රතිදානය කළ යුතුය.

අනුකූල අංශය පහත පරිදි වේ:

- [**20.1.1** සංඛ්‍යා තනන්නා](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` නරක මිනිසෙකි

`parseInt`, එහි චරිත ලක්ෂණ නිසා ප්‍රසිද්ධය:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 විවරණය:** මෙය සිදුවන්නේ කුමක් නිසා ද යත්, `parseInt` විසින් එය නොදන්නා අක්ෂරයක් හමු වනතුරු අකුරෙන් අකුර අඛණ්ඩව විග්‍රහ කරන බැවිනි. `'f*ck'` හි `f` යනු අගය `15` වන සොළොස්වන පාදයේ සංඛ්‍යාවයි.

`අනන්තය`, `පූර්ණ සංඛ්‍යාවක්` බවට විග්‍රහ කිරීම තරමක් වැදගත්ය

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

null විග්‍රහ කිරීමේදී ද ප්‍රවේශම් වන්න.:

```js
parseInt(null, 24); // -> 23
```

**💡 විවරණය:**

> එය අභිශුන්‍යය, පෙළ `null ` බවට පරිවර්තනය කිරීමට උත්සාහ කරයි. පාදම 0 සිට 23 දක්වා එයට පරිවර්තනය කළ හැකි සංඛ්‍යාවක් නොමැති නිසා එය `සංඛ්‍යාවක් නොවේ` යන්න ප්‍රතිදානය කරයි. 24 හිදී, 14 වනඅක්ෂරය වන n , සංඛ්‍යා පද්ධතියට එක් වේ. 31 හි දී, 21 වන අක්ෂරය වන “u ” එක් කෙරෙන අතර සම්පූර්ණ පෙළ විකේතනය කළ හැකි වේ. 37 හිදී, තවදුරටත්, ජනිත කළ හැකි වලංගු සංඛ්‍යාත්මක කුලකයක් නොමැති බැවින් `සංඛ්‍යාවක් නොවේ` යන්න ප්‍රතිදානය වේ.
>
> &mdash; [“parseInt(null, 24) === 23… මොකක්?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) StackOverflow හි

අෂ්ටක අමතක නොකරන්න:

```js
parseInt("06"); // 6
parseInt("08"); // 8 if support ECMAScript 5
parseInt("08"); // 0 if not support ECMAScript 5
```

**💡 විවරණය:** ප්‍රතිදාන පෙළ “0” න් ආරම්භ වේ නම් , පාදය අට (8) හෝ දහය (10) වේ. නිශ්චිතවම කුමන පාදය තොරාගැනේද යන්න ක්‍රියාකාරීත්වය මත රඳා පවතී. 10 භාවිත වන බව ECMAScript 5 මඟින් නිශ්චය කෙරෙන මුත් සියලු වෙබ් පිරික්සුම් තවම මෙයට සහය නොදක්වයි. මේ හේතුව නිසා `parseInt ` භාවිතයේ දී සෑම විටම පාදය සඳහන් කරන්න.

`parseInt` සැමවිටම ප්‍රදානය පෙළ බවට හරවයි:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Be careful while parsing floating point values

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 විවරණය:** `ParseInt` විසින් පෙළ පරාමිතියක් ගෙන සඳහන් කරන ලද පාදයේ නිඛිලයක් ප්‍රතිදානය කරයි.තව ද එමඟින්, යොමු කළ පෙළ පරාමිතියේ, පළමු අංකයක් නොවන අක්ෂරය සහ ඊට පසු සියල්ල ඉවත් කරනු ලැබේ. `0.000001`, `"0.000001"` නම් පෙළ බවට පරිවර්තනය වන අතර `parseInt ` විසින් 0 ප්‍රතිදානය කෙරෙයි. `0.000001` පෙළ බවට හැරවූ විට එය `"1e-7"` ලෙස සැලකෙන අතර එහෙයින් `parseInt` විසින් `1` ප්‍රතිදානය කෙරෙයි. `1/1999999`, `5.00000250000125e-7` ලෙස නිරූපණය කෙරෙන අතර `parseInt` විසින් `5` ප්‍රතිදානය කෙරේ.

## Math with `true` and `false`

අපි ගණනය කිරීමක යෙදෙමු:

```js
true +
  true(
    // -> 2
    true + true
  ) *
    (true + true) -
  true; // -> 3
```

හ්ම්… 🤔

### 💡 විවරණය:

`Number` තනන්නා මඟින් අපට අගයන් සංඛ්‍යා බවට පත් කළ හැකිය. `true`, `1` බවට හැරවෙන බව ඉතා ප්‍රත්‍යක්ෂය.:

```js
Number(true); // -> 1
```

ඒකක ආකලන කාරකය, එහි අගය සංඛ්‍යාවක් බවට පත්කිරීමට උත්සාහ කරයි. එයට, නිඛිල සහ දශම සංඛ්‍යා වල පෙළ නිරූපණයන් මෙන්ම පෙළ අගයන් නොවන `true`, `false ` සහ `null ` ද පරිවර්තනය කළ හැකිය. එයට කිසියම් අගයක් පරිවර්තනය කළ නොහැකි නම්, එය `Nan ` ලෙස නිර්ණය වේ. මෙයින් අදහස්වන්නේ අපට ඉතා පහසුවෙන් `true ` යන්න `1` බවට හැරවිය හැකි බවයි:

```js
+true; // -> 1
```

ඔබ එකතු කිරීම හෝ ගුණ කිරීම කරන විට, `ToNumber` විධිය ව්‍යකෘත වේ. පිරිවිතරය ට අනුව මෙම විධියෙන් ලබා දෙන්නේ:

> පරාමිතිය **සත්‍ය** නම්, **1** ප්‍රතිදානය කරන්න. **අසත්‍ය** නම් **+0** ප්‍රතිදානය කරන්න.

අපට සාමාන්‍ය සංඛ්‍යා පරිදි බූලියානු අගයන් ආකලනය කර නිවැරදි පිළිතුරු ලබා ගත හැක්කේ මේ නිසා ය..

අනුකූල අංශ:

- [**12.5.6** ඒකක `+` කාරකය](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** ආකලන කාරකය (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## JavaScript හි HTML ටීකාවන් වලංගු ය.

ඔබ පුදුම වනු ඇත, නමුත් `<!--`(HTML ටීකා ලෙස හැඳින්වෙන) යනු JavaScript හි වලංගු ටීකාවකි.

```js
// valid comment
<!-- valid comment too
```

### 💡 විවරණය:

HTML ආකාර ටීකාවන්හි අරමුණ වූයේ <script /> ඇමුණුමට සහය නොදක්වන වෙබ් පිරික්සුම් වලට සහය වීමයි. මෙම පිරික්සුම් (උදා: Netscape 1.x ආදී) තව දුරටත් ජනප්‍රිය නොවේ. එමනිසා ඔබේ <script /> ඇමිණුම් වටා HTML ටීකාවන් යෙදීමට කිසිදු සාධාරණ හේතුවක් නැත.

V8 engine මත Node.js පදනම් වී ඇති බැවින්, Node . js විසින් ද HTML-ආකාරයේ ටීකා සඳහා සහය දක්වයි. තව ද, එය පිරිවිතරයෙහි කොටසකි:

- [**B.1.3** HTML-ආකාරයේ ටීකාවන්](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` is ~~not~~ a number

`NaN ` හි වර්ගය `සංඛ්‍යා` වේ.:

```js
typeof NaN; // -> 'number'
```

### 💡 විවරණය:

`typeof` සහ `instanceof` ක්‍රියා කරන ආකාරය පිළිබඳ විවරණයන්:

- [**12.5.5** `typeof` කාරකය](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` සහ `null` වස්තූන් ය.

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// however
null instanceof Object; // false
```

### 💡 විවරණය:

`typeof` කාරකයේ හැසිරීම, පිරිවිතරයේ මෙම කොටසේ අර්ථ දැක්වේ:

- [**12.5.5** `typeof` කාරකය](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

පිරිවිතරයට අනුව, [වගුව 35: `typeof` කාරකයේ ප්‍රතිඵල ](https://www.ecma-international.org/ecma-262/#table-35). ට අනුකූලව `typeof ` කාරකය විසින් පෙළ ප්‍රතිදානය කරයි. `[[Call]]` ක්‍රියාත්මක නොකරන අභිශුන්‍යය , සාමාන්‍ය, සම්මත විදේශීය සහ අසම්මත විදේශීය වස්තුන් සඳහා, එය `“object ”` පෙළ ප්‍රතිදානය කරයි.

කෙසේ නමුත්, `toString` විධිය භාවිතයෙන් ඔබට වස්තුවක වර්ගය පරීක්ෂා කළ හැකිය.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## ඉන්ද්‍රජාලිකව වැඩිවන සංඛ්‍යා

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 විවරණය:

මෙයට හේතු වන්නේ ද්විමය දශම අංක ගණිතය සඳහා වන IEEE 754-2008 සම්මතයයි. මෙම පරිමාණයේ දී, එය ළඟම ඉරට්ටේ සංඛ්‍යාවට වටයයි. වැඩිදුර කියවන්න:

- Wikipedia හි [**6.1.6** සංඛ්‍යා වර්ගය ](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)

## `0.1 + 0.2` හි නිරවද්‍යතාව

හොඳින් දන්නා විහිළුවකි. An addition of `0.1` and `0.2` is deadly precise:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 විවරණය:

StackOverflow හි [”දශම සංඛ්‍යා අංක ගණිතය බිඳවැටී ද?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) ප්‍රශ්නයට පිළිතුර:

ඔබේ ක්‍රමලේඛයේ `0.2` සහ `0.3`, ඒවායේ සත්‍ය අගයන්ට නිමානය කිරීම් වේ. `0.2` ට සමීපම දශම සංඛ්‍යාව `0.2` ට වඩා විශාල වන අතර `0.3` ට සමීපම දශම සංඛ්‍යාව, `0.3` ට සම වේ.`0.1` සහ `0.2` හි එකතුව `0.3` තාත්වික සංඛ්‍යාවට වඩා විශාල වී එය ඔබේ කේතයේ නියතයට අසමාන වේ.

මෙම ප්‍රශ්නය කෙතරම් ප්‍රසිද්ධ ද යත් [0.30000000000000004.com](http://0.30000000000000004.com) නමින් වෙබ් අඩවියක් පවා ඇත.එය JavaScript හි පමණක් නොව දශම සංඛ්‍යා ගණිතය භාවිත කරන සෑම භාෂාවකම ඇත

## සංඛ්‍යා පූරණය

ඔබට, `Number ` සහ `String `වැනි දැවටුම් වස්තූන් වලට ඔබේම විධීන් එක් කළ හැකිය.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 විවරණය:

ප්‍රත්‍යක්ෂව ම, JavaScript හි වෙනත් ඕනෑම වස්තුවක් මෙන් ඔබට `Number` වස්තුව දීර්ඝ කළ හැකිය. කෙසේ නමුත්, අර්ථ දක්වන ලද විධිය, පිරිවිතරයේ කොටසක් නොවේ නම්, එය නිර්දේශ කරනු නොලැබේ.  
`Number`' හි ගුණාංග ලැයිස්තුවක් පහත දැක්වේ.

- [**20.1** සංඛ්‍යා වස්තූන් ](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## සංඛ්‍යා තුනක් සැසඳීම

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 විවරණය:

මෙය ඒ අයුරින් ක්‍රියා කරන්නේ මන්ද? ප්‍රශ්නය ඇත්තේ ප්‍රකාශනයක පළමු කොටසේ ය.මෙය ක්‍රියා කරන්නේ මෙසේය.

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

_Greater than or equal operator (`>=`)_ මඟින් අපට මෙය සැකසිය හැකිය:

```js
3 > 2 >= 1; // true
```

බන්ධුතා කාරක පිළිබඳ පිරිවිතරයෙහි වැඩිදුර කියවන්න:

- [**12.10** බන්ධුතා කාරක](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## හාස්‍යජනක ගණිතය

බොහෝ විට JavaScript හි අංක ගණිතය කර්ම වල ප්‍රතිඵල අනපේක්ෂිත විය හැකිය. පහත උදාහරණ සලකන්න:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 විවරණය:

පළමු උදාහරණ හතරෙහි සිදුවන්නේ කුමක් ද? JavaScript හි ආකලනය වටහා ගැනීම සඳහා කුඩා වගුවක් පහත දැක්වේ.:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

අනෙකුත් උදාහරණ පිළිබඳ කවරේ ද? `[]` සහ `{}` සඳහා, ආකලනයට පෙර, `ToPrimitive` සහ `ToString` විධීන් සම්පුර්ණයෙන් අමතනු ලැබේ. පිරිවිතරයේ ඇගයීම් ක්‍රියාවලිය පිළිබඳව වැඩිදුර කියවන්න.

- [**12.8.3** ආකලන කාරකය (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

## සෙවුම් ප්‍රකාශන ආකලනය

ඔබට මේ අයුරින් සං ඛ්‍යා එකතු කළ හැකි බව ඔබ දැන සිටියා ද?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 විවරණය:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## පෙළ `String` හි නිදර්ශකයක් නොවේ

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 විවරණය:

`String` තනන්නා පෙළ ප්‍රතිදානය කරයි:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

අපි `new` සමඟ උත්සාහ කරමු:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

වස්තුවක්? එය කුමක් ද?

```js
new String("str"); // -> [String: 'str']
```

පෙළ තනන්නා පිළිබඳ වැඩිදුර තොරතුරු පිරිවිතරයෙන්:

- [**21.1.1** පෙළ තනන්නා](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## පසුලකුණු සමඟ කෘත්‍යයන් ඇමතීම

අපි, කොන්සෝලයට සියලු පරාමිතීන් සටහන් කරන කෘත්‍යයක් ප්‍රකාශ කරමු:

```js
function f(...args) {
  return args;
}
```

මෙම කෘත්‍යය පහත පරිදි ඇමතිය හැකි බව ඔබ දන්නවාට සැක නැත:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

නමුත්, ඔබට ඕනෑම කෘත්‍යයක් පසුලකුණු සමඟ ඇමතිය හැකි බව ඔබ දැන සිටියාද?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 විවරණය:

ඔබ _Tagged template literals_ පිළිබඳ දන්නේ නම් මෙය කිසිසේත් ම ඉන්ද්‍රජාලයක් නොවේ. ඉහත උදාහරණයේ, `f ` කෘත්‍යය , ආකෘති වචනාර්ථයක ඇමිණුමකි . ආකෘති වචනාර්ථයට පෙර ඇමිණුම්, කෘත්‍යයක් ඇසුරෙන් ආකෘති වචනාර්ථ බිඳීමට ඔබට ඉඩ දෙයි. ඇමිණුම් කෘත්‍යයක පළමු පරාමිතියේ පෙළ අගයන් සහිත අරාවක් අඩංගුය. ඉතිරි පරාමිතීන් ප්‍රකාශනවලට සම්බන්ධ වේ. උදාහරණය:

```js
function template(strings, ...keys) {
  // do something with strings and keys…
}
```

React ප්‍රජාවේ ජනප්‍රිය, [පිටුපස ක්‍රියාත්මක ඉන්ද්‍රජාලය](http://mxstbr.blog/2016/11/styled-components-magic-explained/) famous library called [💅 styled-components](https://www.styled-components.com/), මෙයයි.

පිරිවිතරයට සබැඳිය:

- [**12.3.7** ඇමිණු ආකෘති](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## අමතන්න අමතන්න අමතන්න

> [@cramforce] විසින් සොයා ගන්නා ලදී(http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 විවරණය:

අවධානයට, එය ඔබේ මනස බිඳිය හැකියි. මෙම කේතය ඔබේ මනසේ නැවත උත්පාදනයට උත්සාහ කරන්න: අපි `apply` විධිය භාවිතයෙන් `call ` විධිය යොදමු. වැඩිදුර කියවන්න.

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## තැනුම් ගුණාංගයක්

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 විවරණය:

අපි පියවරෙන් පියවර මෙම උදාහරණය සලකා බලමු:

```js
// අගය පෙළ “constructor” වන ලෙස නව නියතයක් අර්ථ දැක්වීම
const c = "constructor";

// c යනු වාක්‍යයකි( පෙළ )
c; // -> 'constructor'

// Getting a constructor of string
c[c]; // -> [Function: String]

// Getting a constructor of constructor
c[c][c]; // -> [Function: Function]

// Call the Function constructor and pass
// the body of new function as an argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// And then call this anonymous function
// The result is console-logging a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

`Object.prototype.constructor` විසින් නිදර්ශක වස්තුව තැනු `Object` තැනුම් කෘත්‍යයට යොමුවක් ප්‍රතිදානය කරයි. එය පෙළ විෂයෙහි `String ` , සංඛ්‍යා විෂයෙහි `Number ` ආදී වශයෙන් වේ.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## වස්තුවක්, වස්තුවක ගුණයක යතුර ලෙස

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 විවරණය:

මෙය මෙලෙසින් ක්‍රියා කරන්නේ මන් ද? මෙහි අප භාවිත කරන්නේ _Computed property name_ කි. මෙම වරහන් තුළ ඔබ වස්තුවක් යොමු කළ විට, එය එම වස්තුව පෙළ බවට හරවයි. එමනිසා අපට `'[object Object]'` සහ `{}` අගය ලැබේ.

අපට වරහන් ජාලාව මෙලෙස තැනිය හැක:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

වස්තු වචනාර්ථ පිළිබඳ මෙහි දී වැඩිදුර කියවන්න:

- [වස්තු අරඹන්නා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN
- [**12.2.6** වස්තු අරඹන්නා](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## `__proto__` සමඟ මූලාකෘති වෙත ප්‍රවේශ වීම

අප දන්නා පරිදි, ප්‍රාථමික දත්ත වර්ග වලට මුලාකෘති නොමැත. කෙසේ වෙතත්, ප්‍රාථමික දත්ත වර්ග සඳහා `__proto__` හි අගය ගැනීමට උත්සාහ කළහොත්, අපට මෙය ලැබෙනු ඇත:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 විවරණය:

මෙසේ වීමට හේතුව නම් යමකට මූලාකෘතියක් නොමැති විට, එය `ToObject ` මඟින් දැවටී දැවටුම් වස්තුවක් බවට පත් වීමයි. එමනිසා, පියවරෙන් පියවර:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

`__proto__` පිළිබඳ වැඩිදුර තොරතුරු මෙතැනින්:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

පහත ප්‍රකාශනයේ ප්‍රතිඵලය කුමක් ද?

```js
`${{ Object }}`;
```

පිළිතුර නම්:

```js
// -> '[object Object]'
```

### 💡 විවරණය:

අපි කෙටිඅත් ගුණාංග අංකනය භාවිතයෙන් `Object ` ගුණාංගය සහිත වස්තුවක් අර්ථ දැක්වූයෙමු:

```js
{
  Object: Object;
}
```

ඉනික්බිති අපි මෙම වස්තුව ආකෘති වචනාර්ථයට යොමු කර තිබේ. එබැවින් එම වස්තුව උදෙසා `toString` විධිය ආමන්ත්‍රණය කෙරේ. අපට `'[object Object]'` පෙළ ලැබෙන්නේ මේ නිසා ය.

- [**12.2.9** ආකෘති වචනාර්ථ](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [වස්තු ආරම්භ කරන්නා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## පෙරනිමි අගයන් සමඟ බිඳීම

මෙම උදාහරණය සලකන්න:

```js
let x,
  { x: y = 1 } = { x };
y;
```

සම්මුඛ පරීක්ෂණයක් සඳහා ඉහත උදාහරණය කදිමය. y හි අගය කුමක් ද? පිළිතුර නම්:

```js
// -> 1
```

### 💡 විවරණය:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

ඉහත උදාහරණයේ,

1. අපි අගයක් රහිතව x ප්‍රකාශ කරමු. එබැවින් එය `අර්ථ විරහිත`ය.
2. ඉනික්බිති අපි x හි අගය , x වස්තු ගුණාංගය වෙත ඇසුරුම් කරමු.
3. ඉන්පසු, අපි විඛණ්ඩනය භාවිතයෙන් x හි අගය ලබා ගෙන y ට පැවරිය යුතු වෙමු. අගය අර්ථ දක්වා නැත්නම්, 1 පෙරනිමි අගය ලෙස භාවිත කරමු.
4. y හි අගය ප්‍රතිදානය කරමු.

- [වස්තු ආරම්භ කරන්නා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## තිත් සහ ව්‍යාප්ත කිරීම

අරාවන් ව්‍යාප්තිය සමඟින් සිත් ඇදගන්නා සුළු උදාහරණ පබැඳිය හැකි ය. මෙය සලකන්න:

```js
[...[..."..."]].length; // -> 3
```

### 💡 විවරණය:

`3` ලැබෙන්නේ මන් ද? අප [ව්‍යාප්ති කාරකය](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer) භාවිත කරන විට, `@@iterator` විධිය ආමන්ත්‍රණය කෙරෙන අතර ප්‍රතිදානය වන පුනරාවර්තනය, පුනරාවර්තනය වීමට නියමිත අගය ලබා ගැනීමට භාවිත වේ. පෙළ සඳහා පෙරනිමි පුනරාවර්තකය, පෙළ, අක්ෂර බවට ව්‍යාප්ත කරයි. ව්‍යාප්ත වීමෙන් පසු, අපි මෙම අක්ෂර අරාවකට ගොනු කර ගනිමු. ඉනික්බිති අපි මෙම අරාව නැවත ව්‍යාප්ත කොට නැවතත් අරාවකට ගොනු කර ගනිමු.

`’...’` පෙළ, `.` අක්ෂර 3 කින් සමන්විත වේ. එමනිසා ප්‍රතිඵලය වන අරාවෙහි දිග `3` වේ.

දැන්, පියවරෙන් පියවර:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

ප්‍රත්යක්ෂවම, ඕනෑම අවස්ථා ගණනකදී, අපට අරාවක අවයවයන් ව්‍යාප්ත කර දැවටිය හැකි ය:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## නම් පත්

ක්‍රමලේඛකයන් වැඩි දෙනෙක් JavaScript හි නම් පත් පිළිබඳ නොදනී. ඒවා ඉතා සිත් ගන්නා සුළු ය:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 විවරණය:

නම් කළ ප්‍රකාශනය `break` හෝ `continue` ප්‍රකාශ සමඟ භාවිත වේ. ඔබට චක්‍රීය දාමයක් හඳුනා ගැනීම සඳහා නම්පතක් භාවිත කළ හැක, ඉනික්බිති ව, වැඩසටහන විසින් දාමයට බාධා කළ යුතු ද, නැතහොත් දිගටම පවත්වා ගත යුතු ද යන්න, `break` හෝ `continue` ප්‍රකාශනයක් මඟින් දැක්විය හැකිය.

ඉහත උදාහරණයේ, අපි `foo` නමැති නම්පත හඳුනාගනිමු. එයට පසු `console.log('first');` ක්‍රියාත්මක වන අතර ඉනික්බිති අප ක්‍රියාකාරීත්වයට බාධා කරමු.

JavaScriptහි නම්පත් පිළිබඳ වැඩිදුර කියවන්න:

- [**13.13** නම්කරන ලද ප්‍රකාශ](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [නම්කරන ලද ප්‍රකාශන](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## කූඩු කළ නම්පත්

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 විවරණය:

පෙර උදාහරණ මෙන් ම, පහත සබැඳි අනුගමනය කරන්න:

- [**12.16** කොමාව කාරකය (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## ද්‍රෝහී `try..catch`

මෙම ප්‍රකාශනය කුමක් ප්‍රතිදානය කරනු ඇත් ද? `2` හෝ `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

පිළිතුර `3`. පුදුම වුණා ද?

### 💡 විවරණය:

- [**13.15** `try` ප්‍රකාශය](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## මෙය බහු උරුමය ද?

පහත උදාහරණය බලන්න:

```js
new class F extends (String, Array) {}(); // -> F []
```

ෙය බහු උරුමය ද? නැත.

### 💡 විවරණය:

සිත් ඇදගන්නා සුළු කොටස නම් `extends` වාක්‍යංශයේ (`(String, Array)`) කොටසයි කණ්ඩායම් කාරකය සැමවිටම එහි අවසන් පරාමිතික අගය ප්‍රතිදානය කරයි. එමනිසා, `(String, Array)` යනු සත්‍ය වශයෙන් ම `Array ` වේ. එයින් අදහස් වන්නේ අප අරාව දීර්ඝ කෙරෙන පන්තියක් නිර්මාණය කර ඇති බවයි.

- [**14.5** පන්ති අර්ථ දැක්වීම්](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** කොමාව කාරකය (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## තමා විසින්ම නිපදවා ගන්නා උත්පාදකයෙක්

ස්වයං උත්පාදනයේ යෙදෙන උත්පාදකය පිළිබඳ පහත උදාහරණය සලකන්න:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

ඔබට දැකිය හැකි පරිදි, ප්‍රතිදාන අගය, එහි `අගය`, `f ` ට සමාන වූ වස්තුවකි.මෙම අවස්ථාවේ දී අපට මෙවැන්නක් කළ හැකි ය:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // සහ නැවත
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // සහ නැවත
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 විවරණය:

මෙය මේ අයුරින් ක්‍රියා කරන්නේ මන්දැයි වටහා ගැනීම සඳහා පිරිවිතරයේ පහත අංශ කියවන්න:

- [**25** වියුක්ති වස්තුන් පාලනය කරන්න](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** උත්පාදක වස්තු](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## පන්තියක පන්තියක්

පහත අපැහැදිලි ක්‍රමලේඛ ව්‍යාකරණය සලකන්න:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

පන්තියක් තුළ පන්තියක් අර්ථ දැක්වෙන සෙයක් පෙනේ. වැරැද්දක් විය යුතු මුත් පෙළ `'object'` ලැබේ.

### 💡 විවරණය:

ECMAScript 5 යුගයේ පටන්, _keywords_ , _property names_ ලෙස යෙදීමට අවසර ඇත. එබැවින්, මෙම සරල වස්තු උදාහරණය සහ :

```js
const foo = {
  class: function() {}
};
```

ES6 සම්මත විධි අර්ථ දැක්වීම් ලෙසින් මෙය ගැන සිතන්න . එමෙන් ම, පන්ති අඥාත විය හැකිය. එමනිසා, `: function` කොටස අතහැරිය හොත් අපට මෙය ලැබේ:

```js
class {
  class() {}
}
```

සාමාන්‍ය පන්තියක ප්‍රතිඵලය සැමවිටම සරල වස්තුවකි. සහ එහි `typeof` විසින් `'object'` ප්‍රතිදානය කළ යුතුය.

මෙහි දී වැඩිදුර කියවන්න:

- [**14.3** විධි අර්ථ දැක්වීම්](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** පන්ති අර්ථ දැක්වීම්](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## ආයාස නොකළ හැකි වස්තූන්

හොඳින් දන්නා සංකේත සමඟ, වර්ග පරිවර්තනයෙන් මිදීම සඳහා ක්‍රමයක් ඇත. මෙය බලන්න:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

දැන් අපට මෙය, මෙලෙස භාවිත කළ හැක:

```js
// වස්තූන්
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// පෙළ
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// සංඛ්‍යා
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 විවරණය:

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## උපක්‍රමශීලී ඊතල කෘත්‍යයන්

පහත උදාහරණය සලකන්න:

```js
let f = () => 10;
f(); // -> 10
```

හොඳයි. නමුත් මෙය පිළිබඳව කෙසේ ද:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 විවරණය:

ඔබ `undefined` වෙනුවට `{}` බලාපොරොත්තු වූවා විය හැකි ය. මෙයට හේතුව නම්, සඟල වරහන් යනු ඊතල කෘත්‍යයන් හි ව්‍යාකරණයේ කොටසක් වීමයි. එමනිසා, `f ` අර්ථ විරහිත යන්න ප්‍රතිදානය කරනු ඇත.කෙසේ නමුත්, ප්‍රතිදාන අගය වරහන් මඟින් වට කිරීම මඟින්, ඊතල කෘත්‍යයකින් ඍජුවම `{}` ප්‍රතිදානය කළ හැකිය.

```js
let f = () => ({});
f(); // -> {}
```

## ඊතල කෘත්‍යයන්ට තනන්නෙකු විය නොහැක

පහත උදාහරණය සලකන්න:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

දැන්, ඊතල කෘත්‍යයන් සමඟ එයම සිදු කිරීමට උත්සාහ කරන්න:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 විවරණය:

තැනුම් ව්‍යුහයන් ලෙස ඊතල කෘත්‍යයන් භාවිත කළ නොහැකි අතර,`new` සමඟ භාවිත කළ විට දෝෂයක් දක්වනු ඇත. මක් නිසා ද යත්, එය සතුව වචනාර්ථ `this ` ඇති අතර `මූලාකෘති` ගුණය නොමැත. එමනිසා එය එතරම් අර්ථාන්විත නොවේ.

## `arguments` සහ ඊතල කෘත්‍යයන්

පහත උදාහරණය සලකන්න:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

දැන්, ඊතල කෘත්‍යයන් සමඟ එයම සිදු කිරීමට උත්සාහ කරන්න:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 විවරණය:

ඊතල කෘත්‍යයන් යනු ලුහුඬු බව සහ `this` මත අවධානය යොමු කරන, සාමාන්‍ය කෘත්‍යයන් හි සැහැල්ලු මාදිලියකි. තව ද, ඊතල කෘත්‍යයන් `arguments` වස්තුව සඳහා බැඳීම් නොසපයයි. වලංගු විකල්පයක් වශයෙන් එකම ප්‍රතිඵලය සඳහා `rest` පරාමිතිය භාවිත කරන්න.

```js
let f = (...args) => args;
f("a");
```

- [ඊතල කෘත්‍යයන්](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) at MDN.

## උපක්‍රමශීලී ප්‍රතිදානය

ප්‍රතිදාන ප්‍රකාශය ද උපක්‍රමශීලීය. මෙය සලකන්න:

```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```

### 💡 විවරණය:

`return` සහ ප්‍රතිදාන ප්‍රකාශය එකම පේළියේ තිබිය යුතුය:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

මෙයට හේතුව ස්වයංක්‍රීය අර්ධ සලකුණු ඇතුළු කිරීම හෙවත් අලුත් පේළියකින් පසු ස්වයංක්‍රීය ව අර්ධ සලකුණු ඇතුලත් කිරීමයි. පළමු උදාහරණයේ ප්‍රතිදාන ප්‍රකාශය සහ වස්තු වචනාර්ථය අතරට අර්ධ සලකුණක් ඇතුළත් ව ඇත. එමනිසා කෘත්‍යය `අර්ථ විරහිත ය` යන්න ප්‍රතිදානය කරන අතර වස්තු වචනාර්ථය කිසි ලෙසකින් වත් නිර්ණය නොවේ.

- [**11.9.1** ස්වයංක්‍රීය අර්ධ සලකුණු ඇතුළු කිරීම පිළිබඳ නීති](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** ප්‍රතිදාන ප්‍රකාශය](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## වස්තුවක් මත පැවරුම් බැඳීම

```js
var foo = {n: 1};
var bar = foo;

foo.x = foo = {n: 2};

foo.x // -> undefined
foo   // -> {n: 2}
bar   // -> {n: 1, x: {n: 2}}
```

දකුණේ සිට වමට , foo ට `{n: 2}` පැවරෙන අතර, මෙම පැවරුමේ අගය වන `{n: 2}`, foo.x ට පැවරේ. bar , foo ට යොමු කරන නිසා, bar හි අගය `{n: 1, x: {n: 2}}` වේ. නමුත් foo.x අර්ථ විරහිත වෙමින් bar.x එසේ නොවන්නේ මන්ද?

### 💡 පවිවරණය:

Foo සහ bar, `{n: 1}` නම් එකම වස්තුව පරිශීලනය කරන අතර පැවරුම් වලට පෙර වම් පස අගයන් විසඳේ.`foo = {n: 2}` නව වස්තුවක් නිර්මාණය කරන බැවින්, එම නව වස්තුව පෙන්නුම් කිරීම සඳහා foo යාවත්කාලීන වේ. මෙහිදී සිදුවන ඉන්ද්‍රජාලය නම් `foo.x = ...` හි foo, වම් පස අගයක් ලෙස අකල්හි විසඳෙන අතර ම පැරණි `foo = {n: 1}` පෙන්නුම් කරමින් x අගය එක් කොට එය යාවත්කාලීන කිරීමයි. මෙම පැවරුම් බැඳීම් වලට පසුව, bar තවමත් පැරණි foo වස්තුව පෙන්නුම් කරන මුත්, foo , x අන්තර්ගත නොවන නව `{n: 2}` වස්තුව පෙන්නුම් කරයි.

එය මෙයට සමාන වේ:

```js
var foo = {n: 1};
var bar = foo;

foo = {n: 2} // -> {n: 2}
bar.x = foo // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## අරාවන් සමඟ වස්තුන්හි ගුණ වෙත ප්‍රවේශ වීම

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

ව්‍යාජ-බහුමාන අරාවන් පිළිබඳ කෙසේ ද?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 විවරණය:

කොටු වරහන් `[]` කාරකය, `toString` භාවිතයෙන්, ොමු කරන ලද ප්‍රකාශනය පරිවර්තනය කරයි. ඒක අවයව අරාවක් පෙළ බවට පරිවර්තනය කිරීම, අන්තර්ගත අවයවය පෙළ බවට පරිවර්තනය කිරීමට සමානය.

```js
["property"].toString(); // -> 'property'
```

## අභිශුන්‍යය සහ බන්ධුතා කාරක

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 විවරණය:

සැකෙවින් පවසන්නේ නම්, අභිශුන්‍යය `0` ට වඩා කුඩා බව අසත්‍ය නම්, `null >= 0` සත්‍ය විය යුතුයි. මේ සඳහා වන ගැඹුරු විවරණය [මෙහිදී](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274) කියවන්න.

## `Number.toFixed()` වෙනස් අංක පෙන්වයි

`Number.toFixed()` විවිධ වෙබ් පිරික්සුම් හි දී තරමක් වෙනස් ලෙස හැසිරිය හැක. මෙම උදාහරණය බලන්න:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 විවරණය:

ඔබේ පළමු අදහස “IE11 නිවැරදි අතර Firefox/Chrome වැරදි ය” යන්න විය හැකි වුවත්, සත්‍යය නම්, Firefox/Chrome, සංඛ්‍යා සඳහා වන සම්මුති වලට (IEEE-754 Floating Point) වඩා ඍජුවම ගරු කරන අතර, වඩා පැහැදිලි ප්‍රතිඵලයක් ලබා දීමට දරන උත්සාහය ක දී IE11 විසින් ඒවා ට ගරු නොකරන බවයි.

මෙය ඇතිවන්නේ කෙසේද යන්න ක්ෂණික පරීක්ෂා කීපයක් මඟින් ඔබට දැකගත හැකිය:

```js
// Confirm the odd result of rounding a 5 down
(0.7875).toFixed(3); // -> 0.787
// It looks like it's just a 5 when you expand to the
// limits of 64-bit (double-precision) float accuracy
(0.7875).toFixed(14); // -> 0.78750000000000
// But what if you go beyond the limit?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

දශම සංඛ්‍යා, අභ්‍යන්තරිකව තැන්පත් ව පවතින්නේ දශම සංඛ්‍යා සමූහයක් ලෙස නොව `toString` සහ සමාන ඇමතුම් වලින් වැටයිය හැකි දෝෂ නිපදවන, නමුත් අභ්‍යන්තරයේ නිවැරදිව ඉදිරිපත් කෙරෙන සංකීර්ණ ක්‍රියාදාමයක් මඟිනි .

මෙම අවස්ථාවේදී , අග ඇති 5, සත්‍ය වශයෙන්ම, සත්‍ය 5 ට වඩා අතිශයින් ම කුඩා භාගයකි. එය සාධාරණ දිගකට වැටයීම මඟින් 5 ලෙස දර්ශනය කෙරේ . නමුත් එය අභ්‍යන්තරිකව සත්‍ය වශයෙන් ම 5 නොවේ.

කෙසේ නමුත් ඒ IE 11, toFixed(20) අවස්ථාවේදී පවා, අවසානයට 0 එක් කරමින් පමණක් අගය වාර්තා කරයි . එය දෘඩාංග මඟින් වන දෝෂ අවම කර ගැනීම සඳහා බලයෙන් අගයන් වැටයීමක් කරන සෙයක් පෙනේ.

`NOTE 2` යොමුවේ `toFixed` සඳහා ECMA-262 අර්ථ දැක්වීම බලන්න.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.min()`ට වඩා `Math.max()` කුඩා ය

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 විවරණය:

- [Math.min()ට වඩා Math.max() කුඩා වන්නේ මන් ද?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) by Charlie Harvey

## `null` සහ `0` සැසඳීම

පහත ප්‍රකාශන පරස්පර විරෝධී බවක් හඳුන්වා දෙන සෙයක් පෙනේ.

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

`null >= 0`, `true` නම්, `null` , 0ට සමාන හෝ 0 ට වඩා විශාල හෝ නොවන්නේ කෙසේ ද?(මෙය `වඩා කුඩායි` සමඟ ද මෙලෙසම ක්‍රියා කරයි)

### 💡 විවරණය:

මෙම ප්‍රකාශන තුන නිර්ණය වන ආකාරය එකිනෙකට වෙනස් වීම, මෙම අනපේක්ෂිත හැසිරීමට වගකිව යුතුය.

පළමුව, වියුක්ති සමානතා සැසඳීම `null == 0`. සාමාන්‍ය පරිදි, මෙම කාරකයට එක පසෙක හෝ අගයන් නිසි ලෙස සැසඳිය නොහැකි නම්,එය දෙපසම සංඛ්‍යා බවට හරවා සංඛ්‍යා සසඳයි. ඉනික්බිති, ඔබ පහත බලාපොරොත්තු විය හැකි ය:

```js
// සිදුවන්නේ මෙය නොවේ
(null == 0 + null) == +0;
0 == 0;
true;
```

කෙසේ නමුත්, `null` හෝ `undefined` ඇති පැත්තක මෙම පරිවර්තනය සිදු නොවේ. එමනිසා, ඔබේ සමාන ලකුණෙන් එක පසෙක `null ` ඇත්නම්, ප්‍රකාශනය `සත්‍යය` ප්‍රතිදානය කිරීම සඳහා, අනෙක් පස `null` හෝ `undefined` විය යුතුමය. මෙය මෙහිදී සිදු නොවන නිසා `අසත්‍ය` ප්‍රතිදානය වේ.

මීළඟට, `null > 0` සැසඳීම යි. ඇල්ගොරිතමය, වියුක්ති සමානතා කාරකයේ දී මෙන් නොව, `null ` යන්න සංඛ්‍යාවක් බවට හරවයි. මෙනිසා, අපට මෙම හැසිරීම ලැබේ:

```js
null > 0
+null = +0
0 > 0
false
```

අවසානයේ, `null >= 0` සැසඳීම යි. මෙම ප්‍රකාශනය `null > 0 || null == 0` හි ප්‍රතිඵලය විය යුතු බවට ඔබට තර්ක කළ හැකිය; මෙය සත්‍ය නම්, ඉහත ප්‍රතිපල වලින් ගම්‍ය වන්නේ මෙය `අසත්‍ය` ද විය හැකි බවයි. කෙසේ නමුත්, ඇත්ත වශයෙන් ම `>=` කාරකය ක්‍රියා කරන්නේ ඉතා වෙනස් ආකාරයකිනි;කෙසේද යත් මූලිකවම `<` හි විරුද්ධාර්ථය ගැනීමෙනි. `වඩා විශාල` කාරකය යොදාගත් ඉහත උදාහරණය, `වඩා කුඩා` කාරකයට ද වලංගු නිසා, මෙයින් අදහස් වන්නේ මෙම ප්‍රකාශනය සත්‍ය වශයෙන් ම පහත පරිදි නිර්ණය වන බවයි:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** වියුක්ති බන්ධුතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** වියුක්ති සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## එකම විචල්‍යය ප්‍රති ප්‍රකාශ කිරීම

JS, විචල්‍ය ප්‍රති ප්‍රකාශනයට ඉඩ දෙයි:

```js
a;
a;
// මෙයද වලංගුය
a, a;
```

දැඩි මාදිලියේ දී ද ක්‍රියා කරයි:

```js
var a, a, a;
var a;
var a;
```

### 💡 විවරණය:

සියලු අර්ථ දැක්වීම් එක් අර්ථ දැක්වීමකට ඒකාබද්ධ වේ.

- [**13.3.2** විචල්‍ය ප්‍රකාශය](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## සාමාන්‍ය හැසිරීම Array.prototype.sort()

ඔබට සංඛ්‍යා අරාවක් පිළිවෙළ කිරීමට අවශ්‍ය යයි සිතමු.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 විවරණය:

සාමාන්‍ය පිළියෙළ කිරීම් අනුපිළිවෙල, අවයව පෙළ බවට පරිවර්තනය කොට, එම UTF-16 කේත ඒකක සැසඳීම මත තැනී ඇත.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### ඉඟිය

පෙළ හැර වෙන යමක් පිළියෙළ කිරීමේදී `comparefn` යොමු කරන්න.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

# 📚 වෙනත් සම්පත්

- [wtfjs.com](http://wtfjs.com/) — ජාලයේ භාෂාව සඳහා වන, අති විශේෂ අසාමාන්‍යතාවන් , නොගැළපීම්, සහ සරලව ම වේදනාකාරී දුරවබෝධ අවස්ථා වල එකතුවකි.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — CodeMash 2012 හි දී Gary Bernhardt සිදු කළ පෙරළිකාර දේශනයක්
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — JavaScriptහි වික්ෂිප්ත භාවය ඉවත් කිරීම සඳහා වන උත්සාහයන් දෙකක් ඇතුලත් Kyle Simpsons ගේ දේශනය යි. වඩා පිරිසිදු, වඩා අලංකාර, වඩාත් කියවීමට පහසු කේත ජනනයට ඔබට සහය වීමට සහ ඉනික්බිති විවෘත කේත ප්‍රජාවට දායක වීමට මිනිසුන් දිරි ගැන්වීමට ඔහුට අවශ්‍ය ය.

# 🎓 බලපත්‍රය

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square

# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]

> හාස්‍යජනක සහ දුරවබෝධ JavaScript උදාහරණ

JavaScript යනු විශිෂ්ට ක්‍රමලේඛන භාෂාවකි.එයට සරල වින්‍යාසයක් සහ පුළුල් පද්ධතියක් ඇති අතර වඩාත්ම වැදගත් කරුණක් ලෙස එය සතුව විශිෂ්ට ප්‍රජාවක් සිටී.කෙසේ නමුත් JavaScript ක්‍රමලේඛන භාෂාවේ වටහා ගැනීමට දුෂ්කර කොටස් ද ඇති බව අපි සියල්ලෝම දනිමු. මෙවැනි සමහරක් කො ටස් අපගේ එදිනෙදා ක්‍රමලේඛන කාර්යයන් ඉක්මනින් මහත් අවුලට පත් කිරීමට සමත් අතර තවත් සමහරක් අපව මහා හඬින් සිනහ නැංවීමට සමත්ය.

WTFJS සඳහා මුල් අදහසේ හිමිකම Brian Leroux සතුය.මෙම ලැයිස්තුව ඔහුගේ [2012 DOTJS හි WTFJS දේශනය](https://www.youtube.com/watch?v=et8xNAc2ic8) විසින් පොළඹවන ලද්දකි.

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

## Node හි ඇසුරුම් කරන ලද අත්පිටපත

ඔබට මෙම අත්පොත npm හරහා ස්ථාපනය කරගත හැකිය.මේ සඳහා පහත විධානය ක්‍රියාත්මක කරන්න.

    $ npm install -g wtfjs

දැන් ඔබට විධාන පෙළ හරහා wtfjs ක්‍රියාත්මක කළ හැකි විය යුතුය. මෙය තෝරාගත් $PAGER හි අත්පිටපත විවෘත කරනු ඇත. එසේ නැත්නම් ඔබට මෙහිදී නොනැවතී කියවිය හැකිය.

මූලය මෙහිදී ලබාගත හැක: https://github.com/denysdovhan/wtfjs

## පරිවර්තන

දැනට wtfjs හි පහත පරිවර්තන පවතී.

- [中文版](https://github.com/denysdovhan/wtfjs/blob/master/README-zh-cn.md)

[නව පරිවර්තනයක් ඉල්ලන්න](https://github.com/denysdovhan/wtfjs/issues/new?title=Translation%20Request:%20%5BPlease%20enter%20language%20here%5D&body=I%20am%20able%20to%20translate%20this%20language%20%5Byes/no%5D)

# පටුන

- [💪 දිරිගැන්වුම](#-දිරිගැන්වුම)
- [✍🏻 අංකනය](#-අංකනය)
- [👀 උදාහරණ](#-උදාහරණ)
  - [`[]` සහ `![] සම වේ`](#-සහ--සමානය)
  - [`true` සහ `![]` සම නොවේ, නමුත් `[]` ද සම නොවේ.](#true-ට-සම-නොවේ-නමුත්--ට-ද-සම-නොවේ)
  - [සත්‍යය අසත්‍යය](#සත්යය-අසත්ය-ය)
  - [baNaNa](#banana)
  - [`NaN` යනු `NaN` නොවේ](#nan-යනු-nan-නොවේ)
  - [එය අසාර්ථකත්වයකි]()
  - [`[]` සත්‍යමය මුත් `සත්‍ය` නොවේ](#-is-truthy-but-not-true)
  - [null අසත්‍යමය මුත් `අසත්‍ය` නොවේ](#null-අසත්යමය-මුත්-අසත්ය-නොවේ)
  - [`document.all` යනු වස්තුවකි , නමුත් එය අර්ථ විරහිතය ](#documentall-යනු-වස්තුවකි-නමුත්-එය-අර්ථ-විරහිතය)
  - [අවම අගය ශුන්‍යයට වඩා විශාලය](#අවම-අගය-ශුන්යය-ට-වඩා-විශාල-ය)
  - [කෘත්‍යය කෘත්‍යයක් නොවේ](#කෘත්යය-කෘත්යයක්-නොවේ)
  - [අරාවන් ආකලනය](#අරාවන්-ආකලනය)
  - [අරාවක පසුයෙදුම් කොමා](#අරාවක-පසුයෙදුම්-කොමා)
  - [අරාවන් සමානතාව යක්ෂයෙකි](#array-equality-is-a-monster)
  - [`undefined` සහ `Number`](#undefined-සහ-number)
  - [`parseInt` නරක පුද්ගලයෙකි](#parseint-is-a-bad-guy)
  - [`සත්‍ය` සහ `අසත්‍ය` සමඟ ගණිතය](#math-with-true-and-false)
  - [JavaScript හි HTML ටීකාවන් වලංගුය](#javascript-හි-html-ටීකාවන්-වලංගු-ය)
  - [`NaN` යනු සංඛ්‍යාවක් නොවේ](#nan-is-not-a-number)
  - [`[]` සහ `null` යනු වස්තූන් ය](#-සහ-null-වස්තූන්-ය)
  - [ඉන්ද්‍රජාලික ව ඉහළ යන අංක](#ඉන්ද්රජාලිකව-වැඩිවන-සංඛ්යා)
  - [`0.1 + 0.2` හි නිරවද්‍යතාව]()
  - [සංඛ්‍යා ඌනපූර්ණය](#patching-numbers)
  - [අංක තුනක් සැසඳීම](#සංඛ්යා-තුනක්-සැසඳීම)
  - [හාස්‍යජනක ගණිතය](#හාස්යජනක-ගණිතය)
  - [සෙවුම් ප්‍රකාශන ආකලනය](#addition-of-regexps)
  - [පෙළ, `String` හි නිදර්ශක නොවේ](#පෙළ--string-හි-නිදර්ශකයක්-නොවේ)
  - [පසුලකුණු සමඟ කෘත්‍යයන් ඇමතීම](#පසුලකුණු-සමඟ-කෘත්යයන්-ඇමතීම)
  - [අමතන්න අමතන්න අමතන්න]()
  - [`ඉදිකරන්නා` ගුණයක්](#a-constructor-property)
  - [වස්තුව, වස්තුවක ගුණයක යතුරක් ලෙස](#object-as-a-key-of-objects-property)
  - [ `__proto__` සමඟ මූලාකෘති වෙත ප්‍රවේශ වීම](#__proto__-සමඟ-මූලාකෘති-වෙත-ප්රවේශ-වීම)
  - [`` `${{Object}}` ``](#object)
  - [පෙරනිමි අගයන් සමඟ බිඳීම](#පෙරනිමි-අගයන්-සමඟ-බිඳීම)
  - [තිත් සහ ව්‍යාප්ත කිරීම](#තිත්-සහ-ව්යාප්ත-කිරීම)
  - [නම්පත්](#නම්-පත්)
  - [කූඩු කළ නම්පත්](#කූඩු-කළ-නම්පත්)
  - [ද්‍රෝහී `try..catch`](#ද්රෝහී-trycatch)
  - [මෙය බහු උරුමය ද?](#මෙය-බහු-උරුමය-ද)
  - [තමා විසින්ම උත්පාදනය වන උත්පාදකයෙක්](#තමා-විසින්ම-නිපදවා-ගන්නා-උත්පාදකයෙක්)
  - [පන්තියක පන්තියක්](#පන්තියක-පන්තියක්)
  - [ආයාස නොකළැකි වස්තූන්](#non-coercible-objects)
  - [උපක්‍රමශීලී ඊතල කෘත්‍යයන්](#උපක්රමශීලී-ඊතල-කෘත්යයන්)
  - [ඊතල කෘත්‍යයන්ට තනන්නෙකු විය නොහැක](#ඊතල-කෘත්යයන්ට-තනන්නෙකු-විය-නොහැක)
  - [`පරාමිතික අගයන්` සහ ඊතල කෘත්‍යයන්]()
  - [උපායශීලී ප්‍රතිදානය](#උපක්රමශීලී-ප්රතිදානය)
  - [වස්තුවක් මත පැවරුම් බැඳීම](#වස්තුවක්-මත-පැවරුම්-බැඳීම)
  - [අරාවන් සමඟ වස්තුවක ගුණ වෙත ප්‍රවේශ වීම](#අරාවන්-සමඟ-වස්තුන්හි-ගුණ-වෙත-ප්රවේශ-වීම)
  - [අභිශුන්‍යය සහ බන්ධුතා කාරක](#අභිශුන්යය--සහ-බන්ධුතා-කාරක)
  - [`Number.toFixed()` වෙනස් අංක පෙන්වයි](#numbertofixed-වෙනස්-අංක-පෙන්වයි)
  - [`Math.max()`, `Math.min()`ට වඩා කුඩා ය](#mathminට-වඩා-mathmax-කුඩා-ය)
  - [`අභිශුන්‍යය` සහ `ශුන්‍යය` සැසඳීම](#null-සහ-0-සැසඳීම)
  - [එකම විචල්‍යය ප්‍රතිප්‍රකාශ කිරීම](#එකම-විචල්යය-ප්රති-ප්රකාශ-කිරීම)
  - [සාමාන්‍ය හැසිරීම Array.prototype.sort()](#සාමාන්ය-හැසිරීම-arrayprototypesort)
- [වෙනත් සම්පත්](#-වෙනත්-සම්පත්)
- [🎓 බලපත්‍රය](#-බලපත්රය)

# 💪 දිරිගැන්වුම

> හුදෙක් විනෝදය උදෙසා
>
> &mdash; _[**“හුදෙක් විනෝදය උදෙසා: අහඹු විප්ලවයක කතාව”**](https://en.wikipedia.org/wiki/Just_for_Fun), ලීනස් ටොවාල්ඩ්ස්_

මෙම ලැයිස්තුවේ මූලික අරමුණ වන්නේ උන්මාදනීය උදාහරණ එක්රැස් කිරීම සහ හැකිනම් ඒවා පැහැදිලි කිරීමයි; මක් නිසාද යත් අප මීට පෙර නොදැන සිටි දෙයක් ඉගෙනීම විනෝදජනක බැවිනි.

ඔබ ආධුනිකයකු නම් , JavaScript හි ගැඹුරට පිවිසෙන්නට මෙම සටහන් උපකාරී වනු ඇත. පිරිවිතර වැඩියෙන් කියවන්නට සහ ඒ සමඟ කල් ගෙවන්නට මෙම සටහන් ඔබට අභිප්‍රේරණයක් වනු ඇතැයි මම බලාපොරොත්තු වෙමි.

ඔබ වෘත්තීමය සංවර්ධකයෙකු නම්, ඔබට මෙම උදාහරණ අපගේ ආදරණීය JavaScript හි අනපේක්ෂිත සහ අසාමාන්‍ය අංශ පිළිබඳ යොමුවක් ලෙස සැලකිය හැක.

කවුරුන් හෝ වේවා, හුදෙක් මෙය කියවන්න. බොහෝ විට ඔබ අලුත් දෙයක් සොයා ගනු ඇත.

# ✍🏻 අංකනය

**`// ->`** භාවිත කෙරෙන්නේ ප්‍රකාශනයක ප්‍රතිඵලය දැක්වීමටයි. උදා:

```js
1 + 1; // -> 2
```

**`// >`** මඟින් අදහස් වන්නේ console . log () හෝ වෙනත් ප්‍රතිදානයක ප්‍රතිඵලයකි. :

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** යනු හුදෙක් විවරණය සඳහා යොදා ගත් ටීකාවකි. උදා:

```js
// foo නියතයට කෘත්‍යයක් පැවරීම
const foo = function() {};
```

# 👀 උදාහරණ

## `[]` සහ `![]` සමානය

අරාව, නැත අරාව ට සමානය:

```js
[] == ![]; // -> true
```

### 💡 විවරණය:

වියුක්ත සමානතා කාරකය, සැසඳීම සඳහා දෙපසම සංඛ්‍යා බවට හරවයි, මෙවිට දෙපසම වෙනස් හේතු නිසා 0 බවට පත් වේ. අරාවන් සත්‍යමය බැවින් මෙහි දකුණු පස අසත්‍ය යන්නට ද අනතුරුව 0 බවට ද පත්වේ. කෙසේ නමුත් වම් පසෙහි හිස් අරාවක් බූලියානු අගයක් බවට පත් නොවී ම සංඛ්‍යාවක් බවට පත් වේ.(සත්‍යමය වීම නොසලකා, හිස් අරාවන් 0 බවට පත් කෙරේ.)

පහත දැක්වෙන්නේ මෙම ප්‍රකාශනය සරල වන ආකාරයයි.:

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

[`[]` සත්‍යමය මුත් `සත්‍ය` නොවේ](#-is-truthy-but-not-true) ද බලන්න.

- [**12.5.9** තාර්කික නිශේධ කාරකය (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** වියුක්ති සමානතා සංසන්දනය](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true`, `![]`ට සම නොවේ, නමුත් `[]` ට ද සම නොවේ.

අරාව සත්‍ය නොවන මුත් නැත අරාව ද සත්‍ය නොවේ
අරාව අසත්‍ය ය, එහෙත් නැත අරාව ද අසත්‍ය ය.

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 විවරණය:

```js
true == []; // -> false
true == ![]; // -> false

// පිරිවිතරයට අනුව

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

// පිරිවිතරයට අනුව

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> false

![]; // -> false

false == false; // -> true
```

- [**7.2.13** වියුක්ති සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## සත්‍යය අසත්‍ය ය

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 විවරණය:

මෙය පියවරෙන් පියවර සලකන්න:

```js
//
true සත්‍යමය වන අතර අගය 1 මඟින් නිරූපණය වේ. පෙළ මාදිලියේදී 'true' යනු සංඛ්‍යාවක් නොවේ
true == "true"; // -> false
false == "false"; // -> false

//  ‘false’ යනු හිස් පෙළක් නොවේ, එමනිසා එය සත්‍යමය අගයකි
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** වියුක්ති සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a"; // -> 'baNaNa'
```

මෙය JavaScriptහි පැරණි, එහෙත් වැඩිදියුණු කරන ලද විහිළුවකි.මුල් පිටපත පහත දැක්වේ:

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 විවරණය:

මෙම ප්‍රකාශනය `'foo' + (+'bar')` ලෙස නිර්ණය වේ; `'bar'`, “සංඛ්‍යාවක් නොවේ( NaN )” යන්නට පරිවර්තනය වේ.

- [**12.8.3** ආකලන කාරකය (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 ඒකක + කාරකය](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` යනු `NaN` නොවේ

```js
NaN === NaN; // -> false
```

### 💡 විවරණය:

පිරිවිතරය දැඩි ලෙස ම, මෙම හැසිරීමට හේතුවන තර්කය අර්ථ දක්වයි:

> 1. `Type(x)` සහ `Type(y)` වෙනස් නම්, **false** ප්‍රතිදානය කරන්න.
> 2. `Type(x)` සංඛ්‍යාවක් නම්, එවිට,
>    1. If `x`, **NaN** නම්, **false** දෙන්න.
>    2. If `y`, **NaN** නම්, **false** දෙන්න.
>    3. … … …
>
> &mdash; [**7.2.14** දැඩි සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

IEEE හි `NaN` කාරකය පිළිබඳ අර්ථ දැක්වීම අනුගමනය කරමින්:

> අන්‍යොන්‍ය වශයෙන් බහිෂ්කාර බන්ධුතා හතරක් වලංගුය: වඩා කුඩා, සමාන, වඩා විශාල, සහ අපිළිවෙළ වශයෙනි. අවම වශයෙන් එක සම්ප්‍රදානයක් හෝ සංඛ්‍යාවක් නොවන විට අවසාන අවස්ථාව උද්ගත වේ. සෑම “සංඛ්‍යාවක් නොවේ” අගයක් ම , තමා ද ඇතුළු ව, සියල්ල සමඟ අපිළිවෙල සසඳයි.
>
> &mdash; [“IEEE754 සංඛ්‍යාවක් නොවේ අගයන් සැසඳීම් සියල්ල සඳහා අසත්‍ය ප්‍රතිදානය වීමට හේතුව කුමක් ද?”](https://stackoverflow.com/questions/1565164/1573715#1573715) at StackOverflow

## එය අසාර්ථකත්වයකි

ඔබ විශ්වාස නොකරනු ඇත, නමුත් …

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 විවරණය:

ඉහත සංකේත පෙළ කැබලිවලට කඩා ගැනීම මඟින්, පහත රටාව නිතර ඇතිවන බව අප හඳුනා ගනී:

```js
![] + []; // -> 'false'
![]; // -> false
```

ඉතින් අපි `false` ට [] එකතු කිරීමට තැත් කරමු. නමුත් අභ්‍යන්තර කෘත්‍ය ඇමතුම් ගණනාවක් නිසා (`binary + Operator` -> `ToPrimitive` -> `[[DefaultValue]]`), එය, දකුණු පස පෙළ ට පරිවර්තනය කිරීමෙන් අවසන් වේ.

```js
![] + [].toString(); // 'false'
```

පෙළ අරාවක් ලෙස සැලකීමෙන්, `[0]` මඟින් අපට එහි පළමු අක්ෂරය වෙත ප්‍රවේශ විය හැකිය:

```js
"false"[0]; // -> 'f'
```

ඉතිරිය ප්‍රත්‍යක්ෂ ය., නමුත් i නොමඟ යවන සුළු ය. “fail” හි i යන්න, `['10']` ස්ථානයේ ඇති අවයවය ග්‍රහණය කිරීමෙන් සහ පෙළ `'falseundefined'` උත්පාදනය වීමෙන් ග්‍රහණය කෙරෙනු ලැබේ.

## `[]` සත්‍යමය නමුත් `true` නොවේ

අරාවක් යනු සත්‍යමය අගයකි, කෙසේ නමුත් එය `true` ට සමාන නොවේ.

```js
!![]       // -> true
[] == true // -> false
```

### 💡 විවරණය:

ECMA-262 පිරිවිතරයෙහි අදාළ කොටස් වලට සබැඳි පහත දැක්වේ:

- [**12.5.9** තාර්කික NOT කාරකය (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** වියුක්ත සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` අසත්‍යමය මුත් `අසත්‍ය` නොවේ

`null` අසත්‍යමය යන්න නොසලකා, එය `false` යන්නට සම නොවේ

```js
!!null; // -> false
null == false; // -> false
```

කෙසේ නමුත්, `0` සහ `””` වැනි අසත්‍යමය අගයන් `false` ට සම වේ

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 විවරණය:

විවරණය ඉහත උදාහරණය සඳහා පරිදි ම වේ. අදාළ සබැඳිය පහත දැක්වේ:

- [**7.2.13** වියුක්ත සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` යනු වස්තුවකි, නමුත් එය අර්ථ විරහිතය.

> ⚠️ මෙය පිරික්සුම් යෙදුම් ක්‍රමලේඛ අතුරුමුහුණතේ කොටසක් වන අතර Node.js පරිසරයක ක්‍රියා නොකරනු ඇත ⚠️

`document.all` යන්න අරාවක් වැනි වස්තුවක් ය යන්න නොසලකා, එය, පිටුවේ DOM අවයව වෙත ප්‍රවේශය සපයයි. එය `typeof` කෘත්‍යය ට අර්ථ විරහිත ය යන්නෙන් ප්‍රතිචාර දක්වයි.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

තව ද, `document.all`, `undefined` ට සම නොවේ.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

නමුත්:

```js
document.all == null; // -> true
```

### 💡 විවරණය:

> `document.all`, විශේෂයෙන් IE හි පැරණි මාදිලියන්හිදී, DOM අවයව වෙත ප්‍රවේශ වීමේ මාර්ගයක් ලෙස සැලකුණි. එය කිසි විටෙකත් සම්මතයක් නොවුව ද පැරණි JS කේතයේ එය පුළුල්ව භාවිත විනි. සම්මතය නව අතුරුමුහුණත් සමඟ ප්‍රගමනය වන වූ විට මෙම අතුරුමුහුණත් ඇමතුම යල්පිනූ අතර සම්මත සම්පාදන කොමිසමට එමඟින් කරන්නේ කුමක්ද යන්න තීරණය කිරීමට සිදුව තිබිණි. නමුත් එහි පුළුල් භාවිතය නිසා ඔවුන්, පිරිවිතරයට සචින්ත්‍ය උල්ලංඝනයක් එක් කරමින්, එම අතුරුමුහුණත පවත්වා ගැනීමට තීරණය කරන ලදී.
> දැඩි සමානතා සැසඳීමේ දී එය `false` ට `undefined` ලෙසත්, වියුක්ති සමානතා සැසඳීමේ දී `true` ලෙසත් ප්‍රතිචාර දැක්වීමට හේතුව පිරිවිතරයේ සචින්ත්ය උල්ලංඝනය කිරීමයි.
>
> &mdash; [“යල්පිනු විශේෂාංග - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) at WhatWG - HTML spec
> &mdash; [“පරිච්ජේදය 4 - ToBoolean - අසත්‍යමය අගයන්”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) at YDKJS - Types & Grammar

## අවම අගය, ශුන්‍යය ට වඩා විශාල ය.

`Number.MIN_VALUE` යනු කුඩා ම සංඛ්‍යාවයි; එය ශුන්‍යය ට වඩා විශාල ය:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 විවරණය:

> `Number.MIN_VALUE` හි අගය `5e-324` වන අතර එය float හි නිරවද්‍යතාව යටතේ නිරූපණය කළ හැකි කුඩාම ධන සංඛ්‍යාවයි. එය float දත්ත වර්ගයට ලබා දිය හැකි හොඳම විභේදනය අර්ථ දක්වයි.
>
> තදබල ලෙස සැලකීමේදී සත්‍ය වශයෙන් ම සංඛ්‍යාත්මක නොවුවත්,දැන් සමස්ත කුඩාතම අගය `Number.NEGATIVE_INFINITY` වේ.
>
> &mdash; ["JavaScript හි දී `Number.MIN_VALUE` ට වඩා ශුන්‍යය කුඩා වන්නේ මන් ද?"](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) StackOverflow හි

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## කෘත්‍යය, කෘත්‍යයක් නොවේ

> ⚠️ V8 v5.5 හෝ පහළ (Node.js <=7) පවතින දෝෂයකි ⚠️

ඔබ සැවොම කරදරකාරී _undefined is not a function_ දනී, නමුත් මෙය කුමක් ද?

```js
// null දීර්ඝ කරන පන්තියක් අර්ථ දැක්වීම
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 විවරණය:

මෙය පිරිවිතරයෙහි කොටසක් නොවේ. මෙය මේ වන විට නිරාකරණය කර ඇති දෝෂයකි, එමනිසා අනාගතයේදී මෙවැනි ගැටළුවක් පැන නොනඟිනු ඇත.

## අරාවන් ආකලනය

ඔබ අරාවන් දෙකක් එකතු කිරීමට තැත් කළහොත් කුමක් සිදුවනු ඇත් ද?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 විවරණය:

සමෝච්ජය සිදුවේ. මෙය පියවරෙන් පියවර, පහත පරිදි දැක්විය හැක:

```js
[1, 2, 3] +
  [4, 5, 6][
    //toString() කැඳවන්න
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// සමෝච්ජය
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## අරාවක පසුයෙදුම් කොමා

ඔබ හිස් අයිතම 4 ක අරාවක් නිර්මාණය කර ඇත. කෙසේ නමුත් පසු යෙදුම් කොමාවන් නිසා, ඔබට අවයව 3කින් සමන්විත අරාවක් ලැබෙනු ඇත:

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 විවරණය:

> JavaScript කේතයට නව අවයව, පරාමිතීන් හෝ ගුණාංග එක් කිරීමේදී **පසුයෙදුම් කොමා** ( සමහර විට **අවසන් කොමා** ලෙස හැඳින්වෙන) ප්‍රයෝජනවත් විය හැක. ඔබට නව ගුණයක් එක් කිරීමට අවශ්‍ය විට, කලින් අවසාන පේලිය දැනටමත් පසුයෙදුම් කොමාවක් භාවිත කරන්නේ නම්, ඔබට සරලවම එම පේලිය විකෘත කිරීමකින් තොරව නව පේළියක් එක් කළ හැක. මෙය පිටපත්-පාලන වෙනස්කම් පිරිසිදුව පවත්වා ගන්නා අතරම කේත සංස්කරණ බාධා අවම කරයි.
>
> &mdash; [පසුයෙදුම් කොමා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) at MDN

## අරාවන් සැසඳීම යක්ෂයෙකි

ඔබ ට පහත දැකිය හැකි පරිදි, අරාවන් සැසඳීම යක්ෂයෙකි:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 විවරණය:

ඔබ ඉහත උදාහරණ සඳහා මහත් පරීක්ෂාවෙන් සිටිය යුතුය! මෙම හැසිරීම, පිරිවිතරයේ [**7.2.13** වියුක්ත සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) අංශයේ විස්තර කෙරේ.

## `undefined` සහ `Number`

අප, `Number ` තනන්නාට කිසිදු පරාමිතියක් යොමු නොකරයි නම්, අපට 0 ලැබේ. සත්‍ය පරාමිතීන් නොමැතිවිට නිල පරාමිතීන්ට`අර්ථ විරහිත` අගය පැවරෙයි. මෙනිසා පරාමිති නොමැති `Number`, `අර්ථ විරහිත` යන්න එහි පරාමිතියේ අගය ලෙස ගනු ඇතැයි ඔබ බලාපොරොත්තු විය හැකිය. කෙසේ නමුත්, අප `අර්ථ විරහිත` යොමු කළ විට අපට `සංඛ්‍යාවක් නොවේ` යන්න ලැබේ

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 විවරණය:

පිරිවිතරයට අනුව:

1. මෙම කෘත්‍යයේ ඇමතීමට කිසිදු පරාමිතියක් ලබා දී නැත්නම්, `n = `+0`.ලෙස ගනිමු.
2. නැතිනම්. `n = `ToNumber(value)`.` ලෙස ගනිමු
3. `අර්ථ විරහිත` වීමක දී, `ToNumber(undefined)` විසින් `NaN` ප්‍රතිදානය කළ යුතුය.

අනුකූල අංශය පහත පරිදි වේ:

- [**20.1.1** සංඛ්‍යා තනන්නා](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` නරක මිනිසෙකි

`parseInt`, එහි චරිත ලක්ෂණ නිසා ප්‍රසිද්ධය:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 විවරණය:** මෙය සිදුවන්නේ කුමක් නිසා ද යත්, `parseInt` විසින් එය නොදන්නා අක්ෂරයක් හමු වනතුරු අකුරෙන් අකුර අඛණ්ඩව විග්‍රහ කරන බැවිනි. `'f*ck'` හි `f` යනු අගය `15` වන සොළොස්වන පාදයේ සංඛ්‍යාවයි.

`අනන්තය`, `පූර්ණ සංඛ්‍යාවක්` බවට විග්‍රහ කිරීම තරමක් වැදගත්ය

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

null විග්‍රහ කිරීමේදී ද ප්‍රවේශම් වන්න.:

```js
parseInt(null, 24); // -> 23
```

**💡 විවරණය:**

> එය අභිශුන්‍යය, පෙළ `null ` බවට පරිවර්තනය කිරීමට උත්සාහ කරයි. පාදම 0 සිට 23 දක්වා එයට පරිවර්තනය කළ හැකි සංඛ්‍යාවක් නොමැති නිසා එය `සංඛ්‍යාවක් නොවේ` යන්න ප්‍රතිදානය කරයි. 24 හිදී, 14 වනඅක්ෂරය වන n , සංඛ්‍යා පද්ධතියට එක් වේ. 31 හි දී, 21 වන අක්ෂරය වන “u ” එක් කෙරෙන අතර සම්පූර්ණ පෙළ විකේතනය කළ හැකි වේ. 37 හිදී, තවදුරටත්, ජනිත කළ හැකි වලංගු සංඛ්‍යාත්මක කුලකයක් නොමැති බැවින් `සංඛ්‍යාවක් නොවේ` යන්න ප්‍රතිදානය වේ.
>
> &mdash; [“parseInt(null, 24) === 23… මොකක්?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) StackOverflow හි

අෂ්ටක අමතක නොකරන්න:

```js
parseInt("06"); // 6
parseInt("08"); // 8 if support ECMAScript 5
parseInt("08"); // 0 if not support ECMAScript 5
```

**💡 විවරණය:** ප්‍රතිදාන පෙළ “0” න් ආරම්භ වේ නම් , පාදය අට (8) හෝ දහය (10) වේ. නිශ්චිතවම කුමන පාදය තොරාගැනේද යන්න ක්‍රියාකාරීත්වය මත රඳා පවතී. 10 භාවිත වන බව ECMAScript 5 මඟින් නිශ්චය කෙරෙන මුත් සියලු වෙබ් පිරික්සුම් තවම මෙයට සහය නොදක්වයි. මේ හේතුව නිසා `parseInt ` භාවිතයේ දී සෑම විටම පාදය සඳහන් කරන්න.

`parseInt` සැමවිටම ප්‍රදානය පෙළ බවට හරවයි:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Be careful while parsing floating point values

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 විවරණය:** `ParseInt` විසින් පෙළ පරාමිතියක් ගෙන සඳහන් කරන ලද පාදයේ නිඛිලයක් ප්‍රතිදානය කරයි.තව ද එමඟින්, යොමු කළ පෙළ පරාමිතියේ, පළමු අංකයක් නොවන අක්ෂරය සහ ඊට පසු සියල්ල ඉවත් කරනු ලැබේ. `0.000001`, `"0.000001"` නම් පෙළ බවට පරිවර්තනය වන අතර `parseInt ` විසින් 0 ප්‍රතිදානය කෙරෙයි. `0.000001` පෙළ බවට හැරවූ විට එය `"1e-7"` ලෙස සැලකෙන අතර එහෙයින් `parseInt` විසින් `1` ප්‍රතිදානය කෙරෙයි. `1/1999999`, `5.00000250000125e-7` ලෙස නිරූපණය කෙරෙන අතර `parseInt` විසින් `5` ප්‍රතිදානය කෙරේ.

## Math with `true` and `false`

අපි ගණනය කිරීමක යෙදෙමු:

```js
true +
  true(
    // -> 2
    true + true
  ) *
    (true + true) -
  true; // -> 3
```

හ්ම්… 🤔

### 💡 විවරණය:

`Number` තනන්නා මඟින් අපට අගයන් සංඛ්‍යා බවට පත් කළ හැකිය. `true`, `1` බවට හැරවෙන බව ඉතා ප්‍රත්‍යක්ෂය.:

```js
Number(true); // -> 1
```

ඒකක ආකලන කාරකය, එහි අගය සංඛ්‍යාවක් බවට පත්කිරීමට උත්සාහ කරයි. එයට, නිඛිල සහ දශම සංඛ්‍යා වල පෙළ නිරූපණයන් මෙන්ම පෙළ අගයන් නොවන `true`, `false ` සහ `null ` ද පරිවර්තනය කළ හැකිය. එයට කිසියම් අගයක් පරිවර්තනය කළ නොහැකි නම්, එය `Nan ` ලෙස නිර්ණය වේ. මෙයින් අදහස්වන්නේ අපට ඉතා පහසුවෙන් `true ` යන්න `1` බවට හැරවිය හැකි බවයි:

```js
+true; // -> 1
```

ඔබ එකතු කිරීම හෝ ගුණ කිරීම කරන විට, `ToNumber` විධිය ව්‍යකෘත වේ. පිරිවිතරය ට අනුව මෙම විධියෙන් ලබා දෙන්නේ:

> පරාමිතිය **සත්‍ය** නම්, **1** ප්‍රතිදානය කරන්න. **අසත්‍ය** නම් **+0** ප්‍රතිදානය කරන්න.

අපට සාමාන්‍ය සංඛ්‍යා පරිදි බූලියානු අගයන් ආකලනය කර නිවැරදි පිළිතුරු ලබා ගත හැක්කේ මේ නිසා ය..

අනුකූල අංශ:

- [**12.5.6** ඒකක `+` කාරකය](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** ආකලන කාරකය (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## JavaScript හි HTML ටීකාවන් වලංගු ය.

ඔබ පුදුම වනු ඇත, නමුත් `<!--`(HTML ටීකා ලෙස හැඳින්වෙන) යනු JavaScript හි වලංගු ටීකාවකි.

```js
// valid comment
<!-- valid comment too
```

### 💡 විවරණය:

HTML ආකාර ටීකාවන්හි අරමුණ වූයේ <script /> ඇමුණුමට සහය නොදක්වන වෙබ් පිරික්සුම් වලට සහය වීමයි. මෙම පිරික්සුම් (උදා: Netscape 1.x ආදී) තව දුරටත් ජනප්‍රිය නොවේ. එමනිසා ඔබේ <script /> ඇමිණුම් වටා HTML ටීකාවන් යෙදීමට කිසිදු සාධාරණ හේතුවක් නැත.

V8 engine මත Node.js පදනම් වී ඇති බැවින්, Node . js විසින් ද HTML-ආකාරයේ ටීකා සඳහා සහය දක්වයි. තව ද, එය පිරිවිතරයෙහි කොටසකි:

- [**B.1.3** HTML-ආකාරයේ ටීකාවන්](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` is ~~not~~ a number

`NaN ` හි වර්ගය `සංඛ්‍යා` වේ.:

```js
typeof NaN; // -> 'number'
```

### 💡 විවරණය:

`typeof` සහ `instanceof` ක්‍රියා කරන ආකාරය පිළිබඳ විවරණයන්:

- [**12.5.5** `typeof` කාරකය](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` සහ `null` වස්තූන් ය.

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// however
null instanceof Object; // false
```

### 💡 විවරණය:

`typeof` කාරකයේ හැසිරීම, පිරිවිතරයේ මෙම කොටසේ අර්ථ දැක්වේ:

- [**12.5.5** `typeof` කාරකය](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)

පිරිවිතරයට අනුව, [වගුව 35: `typeof` කාරකයේ ප්‍රතිඵල ](https://www.ecma-international.org/ecma-262/#table-35). ට අනුකූලව `typeof ` කාරකය විසින් පෙළ ප්‍රතිදානය කරයි. `[[Call]]` ක්‍රියාත්මක නොකරන අභිශුන්‍යය , සාමාන්‍ය, සම්මත විදේශීය සහ අසම්මත විදේශීය වස්තුන් සඳහා, එය `“object ”` පෙළ ප්‍රතිදානය කරයි.

කෙසේ නමුත්, `toString` විධිය භාවිතයෙන් ඔබට වස්තුවක වර්ගය පරීක්ෂා කළ හැකිය.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## ඉන්ද්‍රජාලිකව වැඩිවන සංඛ්‍යා

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 විවරණය:

මෙයට හේතු වන්නේ ද්විමය දශම අංක ගණිතය සඳහා වන IEEE 754-2008 සම්මතයයි. මෙම පරිමාණයේ දී, එය ළඟම ඉරට්ටේ සංඛ්‍යාවට වටයයි. වැඩිදුර කියවන්න:

- Wikipedia හි [**6.1.6** සංඛ්‍යා වර්ගය ](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)

## `0.1 + 0.2` හි නිරවද්‍යතාව

හොඳින් දන්නා විහිළුවකි. An addition of `0.1` and `0.2` is deadly precise:

```js
0.1 +
  0.2(
    // -> 0.30000000000000004
    0.1 + 0.2
  ) ===
  0.3; // -> false
```

### 💡 විවරණය:

StackOverflow හි [”දශම සංඛ්‍යා අංක ගණිතය බිඳවැටී ද?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) ප්‍රශ්නයට පිළිතුර:

ඔබේ ක්‍රමලේඛයේ `0.2` සහ `0.3`, ඒවායේ සත්‍ය අගයන්ට නිමානය කිරීම් වේ. `0.2` ට සමීපම දශම සංඛ්‍යාව `0.2` ට වඩා විශාල වන අතර `0.3` ට සමීපම දශම සංඛ්‍යාව, `0.3` ට සම වේ.`0.1` සහ `0.2` හි එකතුව `0.3` තාත්වික සංඛ්‍යාවට වඩා විශාල වී එය ඔබේ කේතයේ නියතයට අසමාන වේ.

මෙම ප්‍රශ්නය කෙතරම් ප්‍රසිද්ධ ද යත් [0.30000000000000004.com](http://0.30000000000000004.com) නමින් වෙබ් අඩවියක් පවා ඇත.එය JavaScript හි පමණක් නොව දශම සංඛ්‍යා ගණිතය භාවිත කරන සෑම භාෂාවකම ඇත

## සංඛ්‍යා පූරණය

ඔබට, `Number ` සහ `String `වැනි දැවටුම් වස්තූන් වලට ඔබේම විධීන් එක් කළ හැකිය.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0)
  .isOne()(
    // -> false
    7
  )
  .isOne(); // -> false
```

### 💡 විවරණය:

ප්‍රත්‍යක්ෂව ම, JavaScript හි වෙනත් ඕනෑම වස්තුවක් මෙන් ඔබට `Number` වස්තුව දීර්ඝ කළ හැකිය. කෙසේ නමුත්, අර්ථ දක්වන ලද විධිය, පිරිවිතරයේ කොටසක් නොවේ නම්, එය නිර්දේශ කරනු නොලැබේ.  
`Number`' හි ගුණාංග ලැයිස්තුවක් පහත දැක්වේ.

- [**20.1** සංඛ්‍යා වස්තූන් ](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## සංඛ්‍යා තුනක් සැසඳීම

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 විවරණය:

මෙය ඒ අයුරින් ක්‍රියා කරන්නේ මන්ද? ප්‍රශ්නය ඇත්තේ ප්‍රකාශනයක පළමු කොටසේ ය.මෙය ක්‍රියා කරන්නේ මෙසේය.

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

_Greater than or equal operator (`>=`)_ මඟින් අපට මෙය සැකසිය හැකිය:

```js
3 > 2 >= 1; // true
```

බන්ධුතා කාරක පිළිබඳ පිරිවිතරයෙහි වැඩිදුර කියවන්න:

- [**12.10** බන්ධුතා කාරක](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## හාස්‍යජනක ගණිතය

බොහෝ විට JavaScript හි අංක ගණිතය කර්ම වල ප්‍රතිඵල අනපේක්ෂිත විය හැකිය. පහත උදාහරණ සලකන්න:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 විවරණය:

පළමු උදාහරණ හතරෙහි සිදුවන්නේ කුමක් ද? JavaScript හි ආකලනය වටහා ගැනීම සඳහා කුඩා වගුවක් පහත දැක්වේ.:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

අනෙකුත් උදාහරණ පිළිබඳ කවරේ ද? `[]` සහ `{}` සඳහා, ආකලනයට පෙර, `ToPrimitive` සහ `ToString` විධීන් සම්පුර්ණයෙන් අමතනු ලැබේ. පිරිවිතරයේ ඇගයීම් ක්‍රියාවලිය පිළිබඳව වැඩිදුර කියවන්න.

- [**12.8.3** ආකලන කාරකය (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

## සෙවුම් ප්‍රකාශන ආකලනය

ඔබට මේ අයුරින් සං ඛ්‍යා එකතු කළ හැකි බව ඔබ දැන සිටියා ද?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 විවරණය:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## පෙළ `String` හි නිදර්ශකයක් නොවේ

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 විවරණය:

`String` තනන්නා පෙළ ප්‍රතිදානය කරයි:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

අපි `new` සමඟ උත්සාහ කරමු:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

වස්තුවක්? එය කුමක් ද?

```js
new String("str"); // -> [String: 'str']
```

පෙළ තනන්නා පිළිබඳ වැඩිදුර තොරතුරු පිරිවිතරයෙන්:

- [**21.1.1** පෙළ තනන්නා](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## පසුලකුණු සමඟ කෘත්‍යයන් ඇමතීම

අපි, කොන්සෝලයට සියලු පරාමිතීන් සටහන් කරන කෘත්‍යයක් ප්‍රකාශ කරමු:

```js
function f(...args) {
  return args;
}
```

මෙම කෘත්‍යය පහත පරිදි ඇමතිය හැකි බව ඔබ දන්නවාට සැක නැත:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

නමුත්, ඔබට ඕනෑම කෘත්‍යයක් පසුලකුණු සමඟ ඇමතිය හැකි බව ඔබ දැන සිටියාද?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 විවරණය:

ඔබ _Tagged template literals_ පිළිබඳ දන්නේ නම් මෙය කිසිසේත් ම ඉන්ද්‍රජාලයක් නොවේ. ඉහත උදාහරණයේ, `f ` කෘත්‍යය , ආකෘති වචනාර්ථයක ඇමිණුමකි . ආකෘති වචනාර්ථයට පෙර ඇමිණුම්, කෘත්‍යයක් ඇසුරෙන් ආකෘති වචනාර්ථ බිඳීමට ඔබට ඉඩ දෙයි. ඇමිණුම් කෘත්‍යයක පළමු පරාමිතියේ පෙළ අගයන් සහිත අරාවක් අඩංගුය. ඉතිරි පරාමිතීන් ප්‍රකාශනවලට සම්බන්ධ වේ. උදාහරණය:

```js
function template(strings, ...keys) {
  // do something with strings and keys…
}
```

React ප්‍රජාවේ ජනප්‍රිය, [පිටුපස ක්‍රියාත්මක ඉන්ද්‍රජාලය](http://mxstbr.blog/2016/11/styled-components-magic-explained/) famous library called [💅 styled-components](https://www.styled-components.com/), මෙයයි.

පිරිවිතරයට සබැඳිය:

- [**12.3.7** ඇමිණු ආකෘති](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## අමතන්න අමතන්න අමතන්න

> [@cramforce] විසින් සොයා ගන්නා ලදී(http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 විවරණය:

අවධානයට, එය ඔබේ මනස බිඳිය හැකියි. මෙම කේතය ඔබේ මනසේ නැවත උත්පාදනයට උත්සාහ කරන්න: අපි `apply` විධිය භාවිතයෙන් `call ` විධිය යොදමු. වැඩිදුර කියවන්න.

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## තැනුම් ගුණාංගයක්

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 විවරණය:

අපි පියවරෙන් පියවර මෙම උදාහරණය සලකා බලමු:

```js
// අගය පෙළ “constructor” වන ලෙස නව නියතයක් අර්ථ දැක්වීම
const c = "constructor";

// c යනු වාක්‍යයකි( පෙළ )
c; // -> 'constructor'

// Getting a constructor of string
c[c]; // -> [Function: String]

// Getting a constructor of constructor
c[c][c]; // -> [Function: Function]

// Call the Function constructor and pass
// the body of new function as an argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// And then call this anonymous function
// The result is console-logging a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

`Object.prototype.constructor` විසින් නිදර්ශක වස්තුව තැනු `Object` තැනුම් කෘත්‍යයට යොමුවක් ප්‍රතිදානය කරයි. එය පෙළ විෂයෙහි `String ` , සංඛ්‍යා විෂයෙහි `Number ` ආදී වශයෙන් වේ.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## වස්තුවක්, වස්තුවක ගුණයක යතුර ලෙස

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 විවරණය:

මෙය මෙලෙසින් ක්‍රියා කරන්නේ මන් ද? මෙහි අප භාවිත කරන්නේ _Computed property name_ කි. මෙම වරහන් තුළ ඔබ වස්තුවක් යොමු කළ විට, එය එම වස්තුව පෙළ බවට හරවයි. එමනිසා අපට `'[object Object]'` සහ `{}` අගය ලැබේ.

අපට වරහන් ජාලාව මෙලෙස තැනිය හැක:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

වස්තු වචනාර්ථ පිළිබඳ මෙහි දී වැඩිදුර කියවන්න:

- [වස්තු අරඹන්නා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN
- [**12.2.6** වස්තු අරඹන්නා](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## `__proto__` සමඟ මූලාකෘති වෙත ප්‍රවේශ වීම

අප දන්නා පරිදි, ප්‍රාථමික දත්ත වර්ග වලට මුලාකෘති නොමැත. කෙසේ වෙතත්, ප්‍රාථමික දත්ත වර්ග සඳහා `__proto__` හි අගය ගැනීමට උත්සාහ කළහොත්, අපට මෙය ලැබෙනු ඇත:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 විවරණය:

මෙසේ වීමට හේතුව නම් යමකට මූලාකෘතියක් නොමැති විට, එය `ToObject ` මඟින් දැවටී දැවටුම් වස්තුවක් බවට පත් වීමයි. එමනිසා, පියවරෙන් පියවර:

```js
(1)
  .__proto__(
    // -> [Number: 0]
    1
  )
  .__proto__.__proto__(
    // -> {}
    1
  ).__proto__.__proto__.__proto__; // -> null
```

`__proto__` පිළිබඳ වැඩිදුර තොරතුරු මෙතැනින්:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

පහත ප්‍රකාශනයේ ප්‍රතිඵලය කුමක් ද?

```js
`${{ Object }}`;
```

පිළිතුර නම්:

```js
// -> '[object Object]'
```

### 💡 විවරණය:

අපි කෙටිඅත් ගුණාංග අංකනය භාවිතයෙන් `Object ` ගුණාංගය සහිත වස්තුවක් අර්ථ දැක්වූයෙමු:

```js
{
  Object: Object;
}
```

ඉනික්බිති අපි මෙම වස්තුව ආකෘති වචනාර්ථයට යොමු කර තිබේ. එබැවින් එම වස්තුව උදෙසා `toString` විධිය ආමන්ත්‍රණය කෙරේ. අපට `'[object Object]'` පෙළ ලැබෙන්නේ මේ නිසා ය.

- [**12.2.9** ආකෘති වචනාර්ථ](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [වස්තු ආරම්භ කරන්නා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## පෙරනිමි අගයන් සමඟ බිඳීම

මෙම උදාහරණය සලකන්න:

```js
let x,
  { x: y = 1 } = { x };
y;
```

සම්මුඛ පරීක්ෂණයක් සඳහා ඉහත උදාහරණය කදිමය. y හි අගය කුමක් ද? පිළිතුර නම්:

```js
// -> 1
```

### 💡 විවරණය:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

ඉහත උදාහරණයේ,

1. අපි අගයක් රහිතව x ප්‍රකාශ කරමු. එබැවින් එය `අර්ථ විරහිත`ය.
2. ඉනික්බිති අපි x හි අගය , x වස්තු ගුණාංගය වෙත ඇසුරුම් කරමු.
3. ඉන්පසු, අපි විඛණ්ඩනය භාවිතයෙන් x හි අගය ලබා ගෙන y ට පැවරිය යුතු වෙමු. අගය අර්ථ දක්වා නැත්නම්, 1 පෙරනිමි අගය ලෙස භාවිත කරමු.
4. y හි අගය ප්‍රතිදානය කරමු.

- [වස්තු ආරම්භ කරන්නා](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## තිත් සහ ව්‍යාප්ත කිරීම

අරාවන් ව්‍යාප්තිය සමඟින් සිත් ඇදගන්නා සුළු උදාහරණ පබැඳිය හැකි ය. මෙය සලකන්න:

```js
[...[..."..."]].length; // -> 3
```

### 💡 විවරණය:

`3` ලැබෙන්නේ මන් ද? අප [ව්‍යාප්ති කාරකය](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer) භාවිත කරන විට, `@@iterator` විධිය ආමන්ත්‍රණය කෙරෙන අතර ප්‍රතිදානය වන පුනරාවර්තනය, පුනරාවර්තනය වීමට නියමිත අගය ලබා ගැනීමට භාවිත වේ. පෙළ සඳහා පෙරනිමි පුනරාවර්තකය, පෙළ, අක්ෂර බවට ව්‍යාප්ත කරයි. ව්‍යාප්ත වීමෙන් පසු, අපි මෙම අක්ෂර අරාවකට ගොනු කර ගනිමු. ඉනික්බිති අපි මෙම අරාව නැවත ව්‍යාප්ත කොට නැවතත් අරාවකට ගොනු කර ගනිමු.

`’...’` පෙළ, `.` අක්ෂර 3 කින් සමන්විත වේ. එමනිසා ප්‍රතිඵලය වන අරාවෙහි දිග `3` වේ.

දැන්, පියවරෙන් පියවර:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

ප්‍රත්යක්ෂවම, ඕනෑම අවස්ථා ගණනකදී, අපට අරාවක අවයවයන් ව්‍යාප්ත කර දැවටිය හැකි ය:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## නම් පත්

ක්‍රමලේඛකයන් වැඩි දෙනෙක් JavaScript හි නම් පත් පිළිබඳ නොදනී. ඒවා ඉතා සිත් ගන්නා සුළු ය:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 විවරණය:

නම් කළ ප්‍රකාශනය `break` හෝ `continue` ප්‍රකාශ සමඟ භාවිත වේ. ඔබට චක්‍රීය දාමයක් හඳුනා ගැනීම සඳහා නම්පතක් භාවිත කළ හැක, ඉනික්බිති ව, වැඩසටහන විසින් දාමයට බාධා කළ යුතු ද, නැතහොත් දිගටම පවත්වා ගත යුතු ද යන්න, `break` හෝ `continue` ප්‍රකාශනයක් මඟින් දැක්විය හැකිය.

ඉහත උදාහරණයේ, අපි `foo` නමැති නම්පත හඳුනාගනිමු. එයට පසු `console.log('first');` ක්‍රියාත්මක වන අතර ඉනික්බිති අප ක්‍රියාකාරීත්වයට බාධා කරමු.

JavaScriptහි නම්පත් පිළිබඳ වැඩිදුර කියවන්න:

- [**13.13** නම්කරන ලද ප්‍රකාශ](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [නම්කරන ලද ප්‍රකාශන](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## කූඩු කළ නම්පත්

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 විවරණය:

පෙර උදාහරණ මෙන් ම, පහත සබැඳි අනුගමනය කරන්න:

- [**12.16** කොමාව කාරකය (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## ද්‍රෝහී `try..catch`

මෙම ප්‍රකාශනය කුමක් ප්‍රතිදානය කරනු ඇත් ද? `2` හෝ `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

පිළිතුර `3`. පුදුම වුණා ද?

### 💡 විවරණය:

- [**13.15** `try` ප්‍රකාශය](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## මෙය බහු උරුමය ද?

පහත උදාහරණය බලන්න:

```js
new class F extends (String, Array) {}(); // -> F []
```

ෙය බහු උරුමය ද? නැත.

### 💡 විවරණය:

සිත් ඇදගන්නා සුළු කොටස නම් `extends` වාක්‍යංශයේ (`(String, Array)`) කොටසයි කණ්ඩායම් කාරකය සැමවිටම එහි අවසන් පරාමිතික අගය ප්‍රතිදානය කරයි. එමනිසා, `(String, Array)` යනු සත්‍ය වශයෙන් ම `Array ` වේ. එයින් අදහස් වන්නේ අප අරාව දීර්ඝ කෙරෙන පන්තියක් නිර්මාණය කර ඇති බවයි.

- [**14.5** පන්ති අර්ථ දැක්වීම්](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** කොමාව කාරකය (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## තමා විසින්ම නිපදවා ගන්නා උත්පාදකයෙක්

ස්වයං උත්පාදනයේ යෙදෙන උත්පාදකය පිළිබඳ පහත උදාහරණය සලකන්න:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

ඔබට දැකිය හැකි පරිදි, ප්‍රතිදාන අගය, එහි `අගය`, `f ` ට සමාන වූ වස්තුවකි.මෙම අවස්ථාවේ දී අපට මෙවැන්නක් කළ හැකි ය:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // සහ නැවත
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // සහ නැවත
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 විවරණය:

මෙය මේ අයුරින් ක්‍රියා කරන්නේ මන්දැයි වටහා ගැනීම සඳහා පිරිවිතරයේ පහත අංශ කියවන්න:

- [**25** වියුක්ති වස්තුන් පාලනය කරන්න](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** උත්පාදක වස්තු](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## පන්තියක පන්තියක්

පහත අපැහැදිලි ක්‍රමලේඛ ව්‍යාකරණය සලකන්න:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

පන්තියක් තුළ පන්තියක් අර්ථ දැක්වෙන සෙයක් පෙනේ. වැරැද්දක් විය යුතු මුත් පෙළ `'object'` ලැබේ.

### 💡 විවරණය:

ECMAScript 5 යුගයේ පටන්, _keywords_ , _property names_ ලෙස යෙදීමට අවසර ඇත. එබැවින්, මෙම සරල වස්තු උදාහරණය සහ :

```js
const foo = {
  class: function() {}
};
```

ES6 සම්මත විධි අර්ථ දැක්වීම් ලෙසින් මෙය ගැන සිතන්න . එමෙන් ම, පන්ති අඥාත විය හැකිය. එමනිසා, `: function` කොටස අතහැරිය හොත් අපට මෙය ලැබේ:

```js
class {
  class() {}
}
```

සාමාන්‍ය පන්තියක ප්‍රතිඵලය සැමවිටම සරල වස්තුවකි. සහ එහි `typeof` විසින් `'object'` ප්‍රතිදානය කළ යුතුය.

මෙහි දී වැඩිදුර කියවන්න:

- [**14.3** විධි අර්ථ දැක්වීම්](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** පන්ති අර්ථ දැක්වීම්](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## ආයාස නොකළ හැකි වස්තූන්

හොඳින් දන්නා සංකේත සමඟ, වර්ග පරිවර්තනයෙන් මිදීම සඳහා ක්‍රමයක් ඇත. මෙය බලන්න:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

දැන් අපට මෙය, මෙලෙස භාවිත කළ හැක:

```js
// වස්තූන්
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// පෙළ
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// සංඛ්‍යා
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 විවරණය:

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## උපක්‍රමශීලී ඊතල කෘත්‍යයන්

පහත උදාහරණය සලකන්න:

```js
let f = () => 10;
f(); // -> 10
```

හොඳයි. නමුත් මෙය පිළිබඳව කෙසේ ද:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 විවරණය:

ඔබ `undefined` වෙනුවට `{}` බලාපොරොත්තු වූවා විය හැකි ය. මෙයට හේතුව නම්, සඟල වරහන් යනු ඊතල කෘත්‍යයන් හි ව්‍යාකරණයේ කොටසක් වීමයි. එමනිසා, `f ` අර්ථ විරහිත යන්න ප්‍රතිදානය කරනු ඇත.කෙසේ නමුත්, ප්‍රතිදාන අගය වරහන් මඟින් වට කිරීම මඟින්, ඊතල කෘත්‍යයකින් ඍජුවම `{}` ප්‍රතිදානය කළ හැකිය.

```js
let f = () => ({});
f(); // -> {}
```

## ඊතල කෘත්‍යයන්ට තනන්නෙකු විය නොහැක

පහත උදාහරණය සලකන්න:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

දැන්, ඊතල කෘත්‍යයන් සමඟ එයම සිදු කිරීමට උත්සාහ කරන්න:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 විවරණය:

තැනුම් ව්‍යුහයන් ලෙස ඊතල කෘත්‍යයන් භාවිත කළ නොහැකි අතර,`new` සමඟ භාවිත කළ විට දෝෂයක් දක්වනු ඇත. මක් නිසා ද යත්, එය සතුව වචනාර්ථ `this ` ඇති අතර `මූලාකෘති` ගුණය නොමැත. එමනිසා එය එතරම් අර්ථාන්විත නොවේ.

## `arguments` සහ ඊතල කෘත්‍යයන්

පහත උදාහරණය සලකන්න:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

දැන්, ඊතල කෘත්‍යයන් සමඟ එයම සිදු කිරීමට උත්සාහ කරන්න:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 විවරණය:

ඊතල කෘත්‍යයන් යනු ලුහුඬු බව සහ `this` මත අවධානය යොමු කරන, සාමාන්‍ය කෘත්‍යයන් හි සැහැල්ලු මාදිලියකි. තව ද, ඊතල කෘත්‍යයන් `arguments` වස්තුව සඳහා බැඳීම් නොසපයයි. වලංගු විකල්පයක් වශයෙන් එකම ප්‍රතිඵලය සඳහා `rest` පරාමිතිය භාවිත කරන්න.

```js
let f = (...args) => args;
f("a");
```

- [ඊතල කෘත්‍යයන්](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) at MDN.

## උපක්‍රමශීලී ප්‍රතිදානය

ප්‍රතිදාන ප්‍රකාශය ද උපක්‍රමශීලීය. මෙය සලකන්න:

```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```

### 💡 විවරණය:

`return` සහ ප්‍රතිදාන ප්‍රකාශය එකම පේළියේ තිබිය යුතුය:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

මෙයට හේතුව ස්වයංක්‍රීය අර්ධ සලකුණු ඇතුළු කිරීම හෙවත් අලුත් පේළියකින් පසු ස්වයංක්‍රීය ව අර්ධ සලකුණු ඇතුලත් කිරීමයි. පළමු උදාහරණයේ ප්‍රතිදාන ප්‍රකාශය සහ වස්තු වචනාර්ථය අතරට අර්ධ සලකුණක් ඇතුළත් ව ඇත. එමනිසා කෘත්‍යය `අර්ථ විරහිත ය` යන්න ප්‍රතිදානය කරන අතර වස්තු වචනාර්ථය කිසි ලෙසකින් වත් නිර්ණය නොවේ.

- [**11.9.1** ස්වයංක්‍රීය අර්ධ සලකුණු ඇතුළු කිරීම පිළිබඳ නීති](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** ප්‍රතිදාන ප්‍රකාශය](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## වස්තුවක් මත පැවරුම් බැඳීම

```js
var foo = {n: 1};
var bar = foo;

foo.x = foo = {n: 2};

foo.x // -> undefined
foo   // -> {n: 2}
bar   // -> {n: 1, x: {n: 2}}
```

දකුණේ සිට වමට , foo ට `{n: 2}` පැවරෙන අතර, මෙම පැවරුමේ අගය වන `{n: 2}`, foo.x ට පැවරේ. bar , foo ට යොමු කරන නිසා, bar හි අගය `{n: 1, x: {n: 2}}` වේ. නමුත් foo.x අර්ථ විරහිත වෙමින් bar.x එසේ නොවන්නේ මන්ද?

### 💡 පවිවරණය:

Foo සහ bar, `{n: 1}` නම් එකම වස්තුව පරිශීලනය කරන අතර පැවරුම් වලට පෙර වම් පස අගයන් විසඳේ.`foo = {n: 2}` නව වස්තුවක් නිර්මාණය කරන බැවින්, එම නව වස්තුව පෙන්නුම් කිරීම සඳහා foo යාවත්කාලීන වේ. මෙහිදී සිදුවන ඉන්ද්‍රජාලය නම් `foo.x = ...` හි foo, වම් පස අගයක් ලෙස අකල්හි විසඳෙන අතර ම පැරණි `foo = {n: 1}` පෙන්නුම් කරමින් x අගය එක් කොට එය යාවත්කාලීන කිරීමයි. මෙම පැවරුම් බැඳීම් වලට පසුව, bar තවමත් පැරණි foo වස්තුව පෙන්නුම් කරන මුත්, foo , x අන්තර්ගත නොවන නව `{n: 2}` වස්තුව පෙන්නුම් කරයි.

එය මෙයට සමාන වේ:

```js
var foo = {n: 1};
var bar = foo;

foo = {n: 2} // -> {n: 2}
bar.x = foo // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## අරාවන් සමඟ වස්තුන්හි ගුණ වෙත ප්‍රවේශ වීම

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

ව්‍යාජ-බහුමාන අරාවන් පිළිබඳ කෙසේ ද?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 විවරණය:

කොටු වරහන් `[]` කාරකය, `toString` භාවිතයෙන්, ොමු කරන ලද ප්‍රකාශනය පරිවර්තනය කරයි. ඒක අවයව අරාවක් පෙළ බවට පරිවර්තනය කිරීම, අන්තර්ගත අවයවය පෙළ බවට පරිවර්තනය කිරීමට සමානය.

```js
["property"].toString(); // -> 'property'
```

## අභිශුන්‍යය සහ බන්ධුතා කාරක

```js
null > 0; // false
null == 0; // false

null >= 0; // true
```

### 💡 විවරණය:

සැකෙවින් පවසන්නේ නම්, අභිශුන්‍යය `0` ට වඩා කුඩා බව අසත්‍ය නම්, `null >= 0` සත්‍ය විය යුතුයි. මේ සඳහා වන ගැඹුරු විවරණය [මෙහිදී](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274) කියවන්න.

## `Number.toFixed()` වෙනස් අංක පෙන්වයි

`Number.toFixed()` විවිධ වෙබ් පිරික්සුම් හි දී තරමක් වෙනස් ලෙස හැසිරිය හැක. මෙම උදාහරණය බලන්න:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 විවරණය:

ඔබේ පළමු අදහස “IE11 නිවැරදි අතර Firefox/Chrome වැරදි ය” යන්න විය හැකි වුවත්, සත්‍යය නම්, Firefox/Chrome, සංඛ්‍යා සඳහා වන සම්මුති වලට (IEEE-754 Floating Point) වඩා ඍජුවම ගරු කරන අතර, වඩා පැහැදිලි ප්‍රතිඵලයක් ලබා දීමට දරන උත්සාහය ක දී IE11 විසින් ඒවා ට ගරු නොකරන බවයි.

මෙය ඇතිවන්නේ කෙසේද යන්න ක්ෂණික පරීක්ෂා කීපයක් මඟින් ඔබට දැකගත හැකිය:

```js
// Confirm the odd result of rounding a 5 down
(0.7875).toFixed(3); // -> 0.787
// It looks like it's just a 5 when you expand to the
// limits of 64-bit (double-precision) float accuracy
(0.7875).toFixed(14); // -> 0.78750000000000
// But what if you go beyond the limit?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

දශම සංඛ්‍යා, අභ්‍යන්තරිකව තැන්පත් ව පවතින්නේ දශම සංඛ්‍යා සමූහයක් ලෙස නොව `toString` සහ සමාන ඇමතුම් වලින් වැටයිය හැකි දෝෂ නිපදවන, නමුත් අභ්‍යන්තරයේ නිවැරදිව ඉදිරිපත් කෙරෙන සංකීර්ණ ක්‍රියාදාමයක් මඟිනි .

මෙම අවස්ථාවේදී , අග ඇති 5, සත්‍ය වශයෙන්ම, සත්‍ය 5 ට වඩා අතිශයින් ම කුඩා භාගයකි. එය සාධාරණ දිගකට වැටයීම මඟින් 5 ලෙස දර්ශනය කෙරේ . නමුත් එය අභ්‍යන්තරිකව සත්‍ය වශයෙන් ම 5 නොවේ.

කෙසේ නමුත් ඒ IE 11, toFixed(20) අවස්ථාවේදී පවා, අවසානයට 0 එක් කරමින් පමණක් අගය වාර්තා කරයි . එය දෘඩාංග මඟින් වන දෝෂ අවම කර ගැනීම සඳහා බලයෙන් අගයන් වැටයීමක් කරන සෙයක් පෙනේ.

`NOTE 2` යොමුවේ `toFixed` සඳහා ECMA-262 අර්ථ දැක්වීම බලන්න.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.min()`ට වඩා `Math.max()` කුඩා ය

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 විවරණය:

- [Math.min()ට වඩා Math.max() කුඩා වන්නේ මන් ද?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) by Charlie Harvey

## `null` සහ `0` සැසඳීම

පහත ප්‍රකාශන පරස්පර විරෝධී බවක් හඳුන්වා දෙන සෙයක් පෙනේ.

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

`null >= 0`, `true` නම්, `null` , 0ට සමාන හෝ 0 ට වඩා විශාල හෝ නොවන්නේ කෙසේ ද?(මෙය `වඩා කුඩායි` සමඟ ද මෙලෙසම ක්‍රියා කරයි)

### 💡 විවරණය:

මෙම ප්‍රකාශන තුන නිර්ණය වන ආකාරය එකිනෙකට වෙනස් වීම, මෙම අනපේක්ෂිත හැසිරීමට වගකිව යුතුය.

පළමුව, වියුක්ති සමානතා සැසඳීම `null == 0`. සාමාන්‍ය පරිදි, මෙම කාරකයට එක පසෙක හෝ අගයන් නිසි ලෙස සැසඳිය නොහැකි නම්,එය දෙපසම සංඛ්‍යා බවට හරවා සංඛ්‍යා සසඳයි. ඉනික්බිති, ඔබ පහත බලාපොරොත්තු විය හැකි ය:

```js
// සිදුවන්නේ මෙය නොවේ
(null == 0 + null) == +0;
0 == 0;
true;
```

කෙසේ නමුත්, `null` හෝ `undefined` ඇති පැත්තක මෙම පරිවර්තනය සිදු නොවේ. එමනිසා, ඔබේ සමාන ලකුණෙන් එක පසෙක `null ` ඇත්නම්, ප්‍රකාශනය `සත්‍යය` ප්‍රතිදානය කිරීම සඳහා, අනෙක් පස `null` හෝ `undefined` විය යුතුමය. මෙය මෙහිදී සිදු නොවන නිසා `අසත්‍ය` ප්‍රතිදානය වේ.

මීළඟට, `null > 0` සැසඳීම යි. ඇල්ගොරිතමය, වියුක්ති සමානතා කාරකයේ දී මෙන් නොව, `null ` යන්න සංඛ්‍යාවක් බවට හරවයි. මෙනිසා, අපට මෙම හැසිරීම ලැබේ:

```js
null > 0
+null = +0
0 > 0
false
```

අවසානයේ, `null >= 0` සැසඳීම යි. මෙම ප්‍රකාශනය `null > 0 || null == 0` හි ප්‍රතිඵලය විය යුතු බවට ඔබට තර්ක කළ හැකිය; මෙය සත්‍ය නම්, ඉහත ප්‍රතිපල වලින් ගම්‍ය වන්නේ මෙය `අසත්‍ය` ද විය හැකි බවයි. කෙසේ නමුත්, ඇත්ත වශයෙන් ම `>=` කාරකය ක්‍රියා කරන්නේ ඉතා වෙනස් ආකාරයකිනි;කෙසේද යත් මූලිකවම `<` හි විරුද්ධාර්ථය ගැනීමෙනි. `වඩා විශාල` කාරකය යොදාගත් ඉහත උදාහරණය, `වඩා කුඩා` කාරකයට ද වලංගු නිසා, මෙයින් අදහස් වන්නේ මෙම ප්‍රකාශනය සත්‍ය වශයෙන් ම පහත පරිදි නිර්ණය වන බවයි:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** වියුක්ති බන්ධුතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** වියුක්ති සමානතා සැසඳීම](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## එකම විචල්‍යය ප්‍රති ප්‍රකාශ කිරීම

JS, විචල්‍ය ප්‍රති ප්‍රකාශනයට ඉඩ දෙයි:

```js
a;
a;
// මෙයද වලංගුය
a, a;
```

දැඩි මාදිලියේ දී ද ක්‍රියා කරයි:

```js
var a, a, a;
var a;
var a;
```

### 💡 විවරණය:

සියලු අර්ථ දැක්වීම් එක් අර්ථ දැක්වීමකට ඒකාබද්ධ වේ.

- [**13.3.2** විචල්‍ය ප්‍රකාශය](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## සාමාන්‍ය හැසිරීම Array.prototype.sort()

ඔබට සංඛ්‍යා අරාවක් පිළිවෙළ කිරීමට අවශ්‍ය යයි සිතමු.

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 විවරණය:

සාමාන්‍ය පිළියෙළ කිරීම් අනුපිළිවෙල, අවයව පෙළ බවට පරිවර්තනය කොට, එම UTF-16 කේත ඒකක සැසඳීම මත තැනී ඇත.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### ඉඟිය

පෙළ හැර වෙන යමක් පිළියෙළ කිරීමේදී `comparefn` යොමු කරන්න.

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

# 📚 වෙනත් සම්පත්

- [wtfjs.com](http://wtfjs.com/) — ජාලයේ භාෂාව සඳහා වන, අති විශේෂ අසාමාන්‍යතාවන් , නොගැළපීම්, සහ සරලව ම වේදනාකාරී දුරවබෝධ අවස්ථා වල එකතුවකි.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — CodeMash 2012 හි දී Gary Bernhardt සිදු කළ පෙරළිකාර දේශනයක්
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — JavaScriptහි වික්ෂිප්ත භාවය ඉවත් කිරීම සඳහා වන උත්සාහයන් දෙකක් ඇතුලත් Kyle Simpsons ගේ දේශනය යි. වඩා පිරිසිදු, වඩා අලංකාර, වඩාත් කියවීමට පහසු කේත ජනනයට ඔබට සහය වීමට සහ ඉනික්බිති විවෘත කේත ප්‍රජාවට දායක වීමට මිනිසුන් දිරි ගැන්වීමට ඔහුට අවශ්‍ය ය.

# 🎓 බලපත්‍රය

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
```

## File: `README-zh-cn.md`
```markdown
# What the f\*ck JavaScript?

[![WTFPL 2.0][license-image]][license-url]
[![NPM version][npm-image]][npm-url]
[![Patreon][patreon-image]][patreon-url]
[![Buy Me A Coffee][bmc-image]][bmc-url]

> 一个有趣和棘手的 JavaScript 示例列表。

JavaScript 是一个不错的语言。它的语法简单，生态系统也很庞大，最重要的是，它拥有最伟大的社区力量。

我们知道，JavaScript 是一个非常有趣的语言，但同时也充满了各种奇怪的行为。这些奇怪的行为有时会搞砸我们的日常工作，有时则会让我们忍俊不禁。

WTFJS 的灵感源于 [Brian Leroux](https://twitter.com/brianleroux)。这个列表受到他 [在 2012 年的 dotJS 上的演讲 **“WTFJS”**](https://www.youtube.com/watch?v=et8xNAc2ic8) 的高度启发：

[![dotJS 2012 - Brian Leroux - WTFJS](https://img.youtube.com/vi/et8xNAc2ic8/0.jpg)](https://www.youtube.com/watch?v=et8xNAc2ic8)

# 适用于 NodeJS 的指南手册

你可以通过 `npm` 安装该项目的指南手册。只需运行：

```
$ npm install -g wtfjs
```

然后在命令行中运行 `wtfjs`，将会在命令行中打开手册并跳转至你选择的页数 `$PAGER`。这不是必需的步骤，你也可以继续在这里阅读。

源码在此处: <https://github.com/denysdovhan/wtfjs>

# 翻译

如今，**wtfjs** 已被翻译成多种语言:

- [中文](./README-zh-cn.md)
- [हिंदी](./README-hi.md)
- [Français](./README-fr-fr.md)
- [Português do Brasil](./README-pt-br.md)
- [Polski](./README-pl-pl.md)
- [Italiano](./README-it-it.md)
- [Russian](https://habr.com/ru/company/mailru/blog/335292/) (on Habr.com)
- [한국어](./README-kr.md)

[**点此添加新语言的翻译**][tr-request]

[tr-request]: https://github.com/denysdovhan/wtfjs/blob/master/CONTRIBUTING.md#translations

**注意:** 翻译由该语言的译者维护，因此可能缺失部分例子，或存在过时的例子等。

<!-- prettier-ignore-start -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [💪🏻 初衷](#-%E5%88%9D%E8%A1%B7)
- [✍🏻 符号](#-%E7%AC%A6%E5%8F%B7)
- [👀 例子](#-%E4%BE%8B%E5%AD%90)
  - [`[]` 等于 `![]`](#-%E7%AD%89%E4%BA%8E-)
  - [`true` 不等于 `![]`，也不等于 `[]`](#true-%E4%B8%8D%E7%AD%89%E4%BA%8E-%E4%B9%9F%E4%B8%8D%E7%AD%89%E4%BA%8E-)
  - [true 是 false](#true-%E6%98%AF-false)
  - [baNaNa](#banana)
  - [`NaN` 不是 `NaN`](#nan-%E4%B8%8D%E6%98%AF-nan)
  - [奇怪的 `Object.is()` 和 `===`](#%E5%A5%87%E6%80%AA%E7%9A%84-objectis-%E5%92%8C-)
  - [它是 fail](#%E5%AE%83%E6%98%AF-fail)
  - [`[]` 是真值，但不等于 `true`](#-%E6%98%AF%E7%9C%9F%E5%80%BC%E4%BD%86%E4%B8%8D%E7%AD%89%E4%BA%8E-true)
  - [`null` 是假值，但又不等于 `false`](#null-%E6%98%AF%E5%81%87%E5%80%BC%E4%BD%86%E5%8F%88%E4%B8%8D%E7%AD%89%E4%BA%8E-false)
  - [`document.all` 是一个 object，但又同时是 undefined](#documentall-%E6%98%AF%E4%B8%80%E4%B8%AA-object%E4%BD%86%E5%8F%88%E5%90%8C%E6%97%B6%E6%98%AF-undefined)
  - [最小值大于零](#%E6%9C%80%E5%B0%8F%E5%80%BC%E5%A4%A7%E4%BA%8E%E9%9B%B6)
  - [函数不是函数](#%E5%87%BD%E6%95%B0%E4%B8%8D%E6%98%AF%E5%87%BD%E6%95%B0)
  - [数组相加](#%E6%95%B0%E7%BB%84%E7%9B%B8%E5%8A%A0)
- [数组中的尾逗号](#%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E5%B0%BE%E9%80%97%E5%8F%B7)
  - [数组的相等性是深水猛兽](#%E6%95%B0%E7%BB%84%E7%9A%84%E7%9B%B8%E7%AD%89%E6%80%A7%E6%98%AF%E6%B7%B1%E6%B0%B4%E7%8C%9B%E5%85%BD)
  - [`undefined` 和 `Number`](#undefined-%E5%92%8C-number)
  - [`parseInt` 是一个坏蛋](#parseint-%E6%98%AF%E4%B8%80%E4%B8%AA%E5%9D%8F%E8%9B%8B)
  - [`true` 和 `false` 的数学运算](#true-%E5%92%8C-false-%E7%9A%84%E6%95%B0%E5%AD%A6%E8%BF%90%E7%AE%97)
  - [HTML 注释在 JavaScript 中有效](#html-%E6%B3%A8%E9%87%8A%E5%9C%A8-javascript-%E4%B8%AD%E6%9C%89%E6%95%88)
  - [`NaN` ~~不是~~一个数值](#nan-%E4%B8%8D%E6%98%AF%E4%B8%80%E4%B8%AA%E6%95%B0%E5%80%BC)
  - [`[]` 和 `null` 是对象](#-%E5%92%8C-null-%E6%98%AF%E5%AF%B9%E8%B1%A1)
  - [神奇的数字增长](#%E7%A5%9E%E5%A5%87%E7%9A%84%E6%95%B0%E5%AD%97%E5%A2%9E%E9%95%BF)
  - [`0.1 + 0.2` 精度计算](#01--02-%E7%B2%BE%E5%BA%A6%E8%AE%A1%E7%AE%97)
  - [扩展数字的方法](#%E6%89%A9%E5%B1%95%E6%95%B0%E5%AD%97%E7%9A%84%E6%96%B9%E6%B3%95)
  - [三个数字的比较](#%E4%B8%89%E4%B8%AA%E6%95%B0%E5%AD%97%E7%9A%84%E6%AF%94%E8%BE%83)
  - [有趣的数学](#%E6%9C%89%E8%B6%A3%E7%9A%84%E6%95%B0%E5%AD%A6)
  - [正则表达式的加法](#%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E7%9A%84%E5%8A%A0%E6%B3%95)
  - [字符串不是 `String` 的实例](#%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%8D%E6%98%AF-string-%E7%9A%84%E5%AE%9E%E4%BE%8B)
  - [用反引号调用函数](#%E7%94%A8%E5%8F%8D%E5%BC%95%E5%8F%B7%E8%B0%83%E7%94%A8%E5%87%BD%E6%95%B0)
  - [到底 call 了谁](#%E5%88%B0%E5%BA%95-call-%E4%BA%86%E8%B0%81)
  - [`constructor` 属性](#constructor-%E5%B1%9E%E6%80%A7)
  - [将对象做为另一个对象的 key](#%E5%B0%86%E5%AF%B9%E8%B1%A1%E5%81%9A%E4%B8%BA%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%AF%B9%E8%B1%A1%E7%9A%84-key)
  - [访问原型 `__proto__`](#%E8%AE%BF%E9%97%AE%E5%8E%9F%E5%9E%8B-__proto__)
  - [`` `${{Object}}` ``](#-object-)
  - [使用默认值解构](#%E4%BD%BF%E7%94%A8%E9%BB%98%E8%AE%A4%E5%80%BC%E8%A7%A3%E6%9E%84)
  - [点和扩展运算符](#%E7%82%B9%E5%92%8C%E6%89%A9%E5%B1%95%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [标签](#%E6%A0%87%E7%AD%BE)
  - [嵌套标签](#%E5%B5%8C%E5%A5%97%E6%A0%87%E7%AD%BE)
  - [阴险的 `try..catch`](#%E9%98%B4%E9%99%A9%E7%9A%84-trycatch)
  - [这是多重继承吗？](#%E8%BF%99%E6%98%AF%E5%A4%9A%E9%87%8D%E7%BB%A7%E6%89%BF%E5%90%97)
  - [yield 返回自身的生成器](#yield-%E8%BF%94%E5%9B%9E%E8%87%AA%E8%BA%AB%E7%9A%84%E7%94%9F%E6%88%90%E5%99%A8)
  - [类的类](#%E7%B1%BB%E7%9A%84%E7%B1%BB)
  - [不可转换类型的对象](#%E4%B8%8D%E5%8F%AF%E8%BD%AC%E6%8D%A2%E7%B1%BB%E5%9E%8B%E7%9A%84%E5%AF%B9%E8%B1%A1)
  - [棘手的箭头函数](#%E6%A3%98%E6%89%8B%E7%9A%84%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0)
  - [箭头函数不能作为构造函数](#%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0%E4%B8%8D%E8%83%BD%E4%BD%9C%E4%B8%BA%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
  - [`arguments` 和箭头函数](#arguments-%E5%92%8C%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0)
  - [棘手的返回](#%E6%A3%98%E6%89%8B%E7%9A%84%E8%BF%94%E5%9B%9E)
  - [对象的链式赋值](#%E5%AF%B9%E8%B1%A1%E7%9A%84%E9%93%BE%E5%BC%8F%E8%B5%8B%E5%80%BC)
  - [使用数组访问对象属性](#%E4%BD%BF%E7%94%A8%E6%95%B0%E7%BB%84%E8%AE%BF%E9%97%AE%E5%AF%B9%E8%B1%A1%E5%B1%9E%E6%80%A7)
  - [`Number.toFixed()` 显示不同的数字](#numbertofixed-%E6%98%BE%E7%A4%BA%E4%B8%8D%E5%90%8C%E7%9A%84%E6%95%B0%E5%AD%97)
  - [`min` 大于 `max`](#min-%E5%A4%A7%E4%BA%8E-max)
  - [比较 `null` 和 `0`](#%E6%AF%94%E8%BE%83-null-%E5%92%8C-0)
  - [相同变量重复声明](#%E7%9B%B8%E5%90%8C%E5%8F%98%E9%87%8F%E9%87%8D%E5%A4%8D%E5%A3%B0%E6%98%8E)
  - [Array.prototype.sort() 的默认行为](#arrayprototypesort-%E7%9A%84%E9%BB%98%E8%AE%A4%E8%A1%8C%E4%B8%BA)
  - [resolve() 不会返回 Promise 实例](#resolve-%E4%B8%8D%E4%BC%9A%E8%BF%94%E5%9B%9E-promise-%E5%AE%9E%E4%BE%8B)
  - [`{}{}` 是 undefined](#-%E6%98%AF-undefined)
  - [`arguments` 绑定](#arguments-%E7%BB%91%E5%AE%9A)
  - [来自地狱的 `alert`](#%E6%9D%A5%E8%87%AA%E5%9C%B0%E7%8B%B1%E7%9A%84-alert)
  - [没有尽头的计时](#%E6%B2%A1%E6%9C%89%E5%B0%BD%E5%A4%B4%E7%9A%84%E8%AE%A1%E6%97%B6)
  - [`setTimeout` 对象](#settimeout-%E5%AF%B9%E8%B1%A1)
  - [点点运算符](#%E7%82%B9%E7%82%B9%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [再 new 一次](#%E5%86%8D-new-%E4%B8%80%E6%AC%A1)
  - [你应该用上分号](#%E4%BD%A0%E5%BA%94%E8%AF%A5%E7%94%A8%E4%B8%8A%E5%88%86%E5%8F%B7)
  - [用空格分割（split）字符串](#%E7%94%A8%E7%A9%BA%E6%A0%BC%E5%88%86%E5%89%B2split%E5%AD%97%E7%AC%A6%E4%B8%B2)
  - [对字符串 stringify](#%E5%AF%B9%E5%AD%97%E7%AC%A6%E4%B8%B2-stringify)
  - [对数字和 `true` 的非严格相等比较](#%E5%AF%B9%E6%95%B0%E5%AD%97%E5%92%8C-true-%E7%9A%84%E9%9D%9E%E4%B8%A5%E6%A0%BC%E7%9B%B8%E7%AD%89%E6%AF%94%E8%BE%83)
- [其他资源](#%E5%85%B6%E4%BB%96%E8%B5%84%E6%BA%90)
- [🤝 捐赠支持](#-%E6%8D%90%E8%B5%A0%E6%94%AF%E6%8C%81)
- [🎓 许可证](#-%E8%AE%B8%E5%8F%AF%E8%AF%81)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- prettier-ignore-end -->

# 💪🏻 初衷

> 只是因为好玩
>
> &mdash; _[**“只是为了好玩：一个意外革命的故事”**](https://en.m.wikipedia.org/wiki/Just_for_Fun), Linus Torvalds_

这个列表的主要目的是收集一些疯狂的例子，并尽可能解释它们的原理。我很喜欢学习以前不了解的东西。

如果您是初学者，您可以根据此笔记深入了解 JavaScript。我希望它会激励你在阅读规范上投入更多时间和精力。

如果您是专业开发人员，您将从这些例子中看到人见人爱的 JavaScript 也充满了非预期的边界行为。

总之，古人云：三人行，必有我师焉。我相信这些例子总能让你学习到新的知识。

> **⚠️ Note:** 如果这些例子帮助到你，请[务必赞助收集了这些例子的作者](#-supporting).

# ✍🏻 符号

**`// ->`** 表示表达式的结果。例如：

```js
1 + 1; // -> 2
```

**`// >`** 表示 `console.log` 等输出的结果。例如：

```js
console.log("hello, world!"); // > hello, world!
```

**`//`** 则是用于解释的注释。例如：

```js
// 将一个函数赋值给 foo 常量
const foo = function() {};
```

# 👀 例子

## `[]` 等于 `![]`

数组等于一个数组取反：

```js
[] == ![]; // -> true
```

### 💡 说明：

抽象相等运算符会将其两端的表达式转换为数字值进行比较，尽管这个例子中，左右两端均被转换为 `0`，但原因各不相同。数组总是真值（truthy）,因此右值的数组取反后总是为 `false`，然后在抽象相等比较中被被类型转换为 `0`。而左值则是另一种情形，空数组没有被转换为布尔值的话，尽管在逻辑上是真值（truthy），但在抽象相等比较中，会被类型转换为数字 `0`。

该表达式的运算步骤如下：

```js
+[] == +![];
0 == +false;
0 == 0;
true;
```

了解更多：[`[]` 是真值，但并非 `true`](#-is-truthy-but-not-true).

- [**12.5.9** 逻辑非运算符 (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** 抽象相等比较 ](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `true` 不等于 `![]`，也不等于 `[]`

数组不等于 `true`，但数组取反也不等于 `true`；
数组等于 `false`数组取反也等于 `false`：

```js
true == []; // -> false
true == ![]; // -> false

false == []; // -> true
false == ![]; // -> true
```

### 💡 说明:

```js
true == []; // -> false
true == ![]; // -> false

// 根据规范

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

// 根据规范

false == []; // -> true

toNumber(false); // -> 0
toNumber([]); // -> 0

0 == 0; // -> true

false == ![]; // -> true

![]; // -> false

false == false; // -> true
```

- [**7.2.15** 抽象相等比较](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

## true 是 false

```js
!!"false" == !!"true"; // -> true
!!"false" === !!"true"; // -> true
```

### 💡 说明：

考虑以下步骤：

```js
// true 是真值（truthy），并且隐式转换为数字1，而字符串 'true' 会被转换为 NaN。
true == "true"; // -> false
false == "false"; // -> false

// 'false' 不是空字符串，所以它的值是 true
!!"false"; // -> true
!!"true"; // -> true
```

- [**7.2.13** 抽象相等比较](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## baNaNa

```js
"b" + "a" + +"a" + "a";
```

这是用 JavaScript 写的老派笑话，原版如下：

```js
"foo" + +"bar"; // -> 'fooNaN'
```

### 💡 说明：

这个表达式可以转化成 `'foo' + (+'bar')`，但无法将`'bar'`强制转化成数值。

- [**12.8.3** 加法运算符 (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [12.5.6 一元 + 运算符](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)

## `NaN` 不是 `NaN`

```js
NaN === NaN; // -> false
```

### 💡 说明：

规范严格定义了这种行为背后的逻辑：

> 1. 如果 `Type(x)` 不同于 `Type(y)`，返回 **false**。
> 2. 如果 `Type(x)` 数值, 然后
>    1. 如果 `x` 是 **NaN**，返回 **false**。
>    2. 如果 `y` 是 **NaN**，返回 **false**。
>    3. ……
>
> &mdash; [**7.2.14** 严格模式相等比较 ](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)

根据 IEEE 对 NaN 的定义：

> 有四种可能的相互排斥的关系：小于、等于、大于和无序。当比较操作中至少一个操作数是 NaN 时，便是无序的关系。换句话说，NaN 对任何事物包括其本身比较都应当是无序关系。
>
> &mdash; StackOverflow 上的 [“为什么对于 IEEE754 NaN 值的所有比较返回 false？”](https://stackoverflow.com/questions/1565164/1573715#1573715)

## 奇怪的 `Object.is()` 和 `===`

`Object.is()` 用于判断两个值是否相同。和 `===` 操作符像作用类似，但它也有一些奇怪的行为：

```javascript
Object.is(NaN, NaN); // -> true
NaN === NaN; // -> false

Object.is(-0, 0); // -> false
-0 === 0; // -> true

Object.is(NaN, 0 / 0); // -> true
NaN === 0 / 0; // -> false
```

### 💡 说明:

在 JavaScript “语言”中，`NaN` 和 `NaN` 的值是相同的，但却不是严格相等。`NaN === NaN` 返回 false 是因为历史包袱，记住这个特例就行了。

基于同样的原因，`-0` 和 `0` 是严格相等的，但它们的值却不同。

关于 `NaN === NaN` 的更多细节，请参阅上一个例子。

- [这是 TC39 中关于 Object.is 的规范](https://tc39.es/ecma262/#sec-object.is)
- MDN 上的[相等比较与相同值比较](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

## 它是 fail

你可能不会相信，但……

```js
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'
```

### 💡 说明：

将大量的符号分解成片段，我们注意到，以下表达式经常出现：

```js
![] + []; // -> 'false'
![]; // -> false
```

所以我们尝试将 `[]` 和 `false` 加起来。但是因为一些内部函数调用（`binary + Operator` - >`ToPrimitive` - >`[[DefaultValue]` ]），我们最终将右边的操作数转换为一个字符串：

```js
![] + [].toString(); // 'false'
```

将字符串作为数组，我们可以通过`[0]`来访问它的第一个字符：

```js
"false"[0]; // -> 'f'
```

剩下的部分以此类推，不过此处的 `i` 字符是比较讨巧的。`fail` 中的 `i` 来自于生成的字符串 `falseundefined`，通过指定序号 `['10']` 取得的。

更多的例子：

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

- [烧脑预警：疯狂的 JavaScript](http://patriciopalladino.com/blog/2012/08/09/non-alphanumeric-javascript.html)
- [写个句子干嘛要用字母](https://bluewings.github.io/en/writing-a-sentence-without-using-the-alphabet/#weird-javascript-generator) — 用 JavaScript 生成任意短语

## `[]` 是真值，但不等于 `true`

数组是一个真值，但却不等于 `true`。

```js
!![]       // -> true
[] == true // -> false
```

### 💡 说明：

以下是 ECMA-262 规范中相应部分的链接：

- [**12.5.9** 逻辑非运算符 (`!`)](https://www.ecma-international.org/ecma-262/#sec-logical-not-operator)
- [**7.2.13** 抽象相等比较](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `null` 是假值，但又不等于 `false`

尽管 `null` 是假值，但它不等于 `false`。

```js
!!null; // -> false
null == false; // -> false
```

但是，别的被当作假值的却等于 `false`，如 `0` 或 `''`。

```js
0 == false; // -> true
"" == false; // -> true
```

### 💡 说明：

跟前面的例子相同。这是一个相应的链接：

- [**7.2.13** 抽象相等比较](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)

## `document.all` 是一个 object，但又同时是 undefined

> ⚠️ 这是浏览器 API 的一部分，对于 Node.js 环境无效 ⚠️

尽管 document.all 是一个类数组对象（array-like object），并且通过它可以访问页面中的 DOM 节点，但在通过 `typeof` 的检测结果是 `undefined`。

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

同时，`document.all` 不等于 `undefined`。

```js
document.all === undefined; // -> false
typeof document.all; // -> 'undefined'
```

但是同时，`document.all` 不等于 `undefined`：

```js
document.all === undefined; // -> false
document.all == null; // -> true
```

不过：

```js
document.all == null; // -> true
```

### 💡 说明：

> `document.all` 作为访问页面 DOM 节点的一种方式，在早期版本的 IE 浏览器中较为流行。尽管这一 API 从未成为标准，但被广泛使用在早期的 JS 代码中。当标准演变出新的 API（例如 `document.getElementById`）时，这个 API 调用就被废弃了。因为这个 API 的使用范围较为广泛，标准委员会决定保留这个 API，但有意地引入一个违反 JavaScript 标准的规范。
> 这个有意的对违反标准的规范明确地允许该 API 与 `undefined` 使用[严格相等比较](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison)得出 `false` 而使用[抽象相等比较](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) 得出 `true`。
>
> &mdash; [“废弃功能 - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) at WhatWG - HTML spec
> &mdash; YDKJS（你不懂 JS） - 类型与语法 中的 [“第 4 章 - ToBoolean - 假值](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects)

## 最小值大于零

`Number.MIN_VALUE` 是最小的数字，大于零：

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 说明：

> `Number.MIN_VALUE` 是 `5e-324`，即可以在浮点精度内表示的最小正数，也是在该精度内无限接近零的数字。它定义了浮点数的最高精度。

> 现在，整体最小的值是 `Number.NEGATIVE_INFINITY`，尽管这在严格意义上并不是真正的数字。
>
> &mdash; StackOverflow 上的[“为什么在 JavaScript 中 `0` 小于 `Number.MIN_VALUE`？”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript)

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## 函数不是函数

> ⚠️ V8 v5.5 或更低版本中出现的 Bug（Node.js <= 7） ⚠️

大家都知道 _undefined 不是 function_ 对吧？但是你知道这个吗？

```js
// 声明一个继承null的类
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 说明：

这不是规范的一部分。这只是一个缺陷，且已经修复了。所以将来不会有这个问题。

### Super constructor null of Foo is not a constructor (Foo 的超类的构造函数 null 不是构造函数)

这是前述缺陷的后续行为，在现代环境中可以复现（在 Chrome 71 和 Node.js v11.8.0 测试成功）。

```js
class Foo extends null {}
new Foo() instanceof null;
// > TypeError: Super constructor null of Foo is not a constructor
```

### 💡 说明：

这并不是缺陷，因为：

```js
Object.getPrototypeOf(Foo.prototype); // -> null
```

若当前类没有构造函数，则在构造该类时会顺次调用其原型链上的构造函数，而本例中其父类没有构造函数。补充一下，`null` 也是一个 `object`：

```js
typeof null === "object";
```

因此，你可以继承 `null`（尽管在面向对象编程的世界里这是不允许的），但是却不能调用 `null` 的构造函数。若你把代码改成这样：

```js
class Foo extends null {
  constructor() {
    console.log("something");
  }
}
```

将会报错：

```
ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor
// 引用错误：在访问`this`或返回之前，你需要在子类中先调用super构造函数
```

但是当你加上 `super` 时：

```js
class Foo extends null {
  constructor() {
    console.log(111);
    super();
  }
}
```

JS 抛出错误：

```
TypeError: Super constructor null of Foo is not a constructor
// 类型错误：Foo的超类的构造函数null不是构造函数
```

- [@geekjob](https://github.com/geekjob) 发布的 [对该问题的解释](https://github.com/denysdovhan/wtfjs/pull/102#discussion_r259143582)

## 数组相加

如果你尝试将两个数组相加：

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 说明：

数组之间会发生串联。步骤如下：

```js
[1, 2, 3] +
  [4, 5, 6][
    // 调用 toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// 串联
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

# 数组中的尾逗号

假设你想要创建了一个包含 4 个空元素的数组。如下所示，最终只能得到一个包含三个元素的数组，原因在于尾逗号：

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 说明：

> **尾逗号** （trailing commas，有时也称为“最后逗号”（final commas）） 在向 JavaScript 代码中添加新元素、参数或属性时非常有用。如果您想添加一个新属性，若前一行已经有尾逗号，你无需修改前一行，只要添加一个新行并加上尾逗号即可。这使得版本控制历史较为干净，编辑代码也很简单。
>
> &mdash; MDN 上的 [尾逗号](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas)

## 数组的相等性是深水猛兽

数组之间进行相等比较是 JS 中的深水猛兽，看看这些例子：

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 说明：

仔细阅读上面的例子！规范中的 [**7.2.13** 抽象相等比较](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) 一节描述了这些行为。

## `undefined` 和 `Number`

无参数调用 `Number` 构造函数会返回 `0`。我们知道，当函数没有接受到指定位置的实际参数时，该处的形式参数的值会是 `undefined`。因此，你可能觉得当我们传入 `undefined` 时应当同样返回 `0`。然而实际上传入 `undefined` 返回的是 `NaN`。

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 说明：

根据规范：

1. 若无参数调用该函数，`n` 将为 `+0`。
2. 否则，`n` 将为？`ToNumber(value)`。
3. 如果值为 `undefined`，`ToNumber(undefined)` 应该返回 `NaN`。

这是相应的部分：

- [**20.1.1** Number 构造函数 ](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` 是一个坏蛋

`parseInt` 以它的怪异而出名。

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 说明：**
这是因为 `parseInt` 会持续解析直到它解析到一个不识别的字符，`'f*ck'` 中的 `f` 是 16 进制下的 `15`。

解析 `Infinity` 到整数也很有意思……

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

也要小心解析 `null`：

```js
parseInt(null, 24); // -> 23
```

**💡 说明：**

> 它将 `null` 转换成字符串 `'null'`，并尝试转换它。对于基数 0 到 23，没有可以转换的数字，因此返回 NaN。而当基数为 24 时，第 14 个字母`“n”`也可以作数字用。当基数为 31 时，第 21 个字母`“u”`进入数字的行列，此时整个字符串都可以解析了。而当基数增加到 37 以上，已经超出了数字和字母所能表达的数字范围，因此一律返回 `NaN`。
>
> &mdash; StackOverflow 上的 [“parseInt(null, 24) === 23 什么鬼”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what)

不要忘记八进制：

```js
parseInt("06"); // 6
parseInt("08"); // 8 如果支持 ECMAScript 5
parseInt("08"); // 0 如果不支持 ECMAScript 5
```

**💡 说明：**
当输入的字符串以“0”开始时，根据实现的不同，会被解释为八进制或十进制。ECMAScript 5 明确表示应当使用十进制，但有部分浏览器仍不支持。因此推荐在调用 `parseInt` 函数时总是传入表示基数的第二个参数。

`parseInt` 会先将参数值转换为字符串：

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

解析浮点数的时候要注意

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 说明：** `parseInt` 接受字符串参数并返回一个指定基数下的整数。`parseInt` 会将字符串中首个非数字字符（字符集由基数决定）及其后的内容全部截断。如 `0.000001` 被转换为 `"0.000001"`，因此 `parseInt` 返回 `0`。而 `0.0000001` 转换为字符串会变成 `"1e-7"`，因此 `parseInt` 返回 `1`。`1/1999999` 被转换为 `5.00000250000125e-7`，所以 `parseInt` 返回 `5`。

## `true` 和 `false` 的数学运算

做一下数学计算：

```js
true + true; // -> 2
(true + true) * (true + true) - true; // -> 3
```

嗯……🤔

### 💡 说明：

我们可以用 `Number` 构造函数将值强制转化成数值。很明显，`true` 将被强制转换为 `1` ：

```js
Number(true); // -> 1
```

一元加运算符会尝试将其值转换成数字。它可以转换字符串形式表达的整数和浮点数，以及非字符串值 `true`、`false` 和 `null`。如果它不能解析特定的值，它将转化为 `NaN`。这意味着我们可以有更简便的方式将 `true` 转换成 `1`：

```js
+true; // -> 1
```

当你执行加法或乘法时，将会 `ToNumber` 方法。根据规范，该方法的返回值为：

> 如果`参数`是 **true**，返回 **1**。如果`参数`是 **false**，则返回 **+0**。

因此我们可以将布尔值相加并得到正确的结果

相应章节：

- [**12.5.6** 一元 `+` 运算符 ](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** 加法运算符（`+`） ](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## HTML 注释在 JavaScript 中有效

你可能会感到震惊，`<!--` (这是 HTML 注释格式）也是一个有效的 JavaScript 注释。

```js
// 有效注释
<!-- 也是有效的注释
```

### 💡 说明：

震惊吗？类 HTML 注释旨在容许不理解 `<script>` 标签的浏览器优雅降级。这些浏览器，例如 Netscape 1.x 已经不再流行。因此，在脚本标记中添加 HTML 注释是没有意义的。

由于 Node.js 基于 V8 引擎，Node.js 运行时也支持类似 HTML 的注释。而且，它们是规范的一部分：

- [**B.1.3** 类 HTML 注释 ](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` ~~不是~~一个数值

`NaN` 类型是 `'number'`：

```js
typeof NaN; // -> 'number'
```

### 💡 说明：

`typeof` 和 `instanceof` 运算符的工作原理：

- [**12.5.5** `typeof` 操作符](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** 运行时语法：InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` 和 `null` 是对象

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// 然而
null instanceof Object; // false
```

### 💡 说明：

`typeof` 运算符的行为在本节的规范中定义：

- [**13.5.3** `typeof` 操作符](https://262.ecma-international.org/12.0/#sec-typeof-operator)

根据规范，`typeof` 操作符返回一个字符串，且必须符合 [Table 37: `typeof` 操作符 返回值](https://262.ecma-international.org/12.0/#table-typeof-operator-results)。对于没有实现 `[[Call]]` 的 `null`、普通对象、标准特异对象和非标准特异对象，它返回字符串 `"object“`。

但是，你可以使用 `toString` 方法检查对象的类型。

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## 神奇的数字增长

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 说明：

这是由 IEEE 754-2008 二进制浮点运算标准引起的。极大的数字会被四舍五入到最近的偶数。阅读更多：

- [**6.1.6** 数字类型](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- 维基百科上的 [IEEE 754](https://en.m.wikipedia.org/wiki/IEEE_754)

## `0.1 + 0.2` 精度计算

来自 JavaScript 的知名笑话。`0.1` 和 `0.2` 相加是存在精度错误的

```js
0.1 + 0.2; // -> 0.30000000000000004
0.1 + 0.2 === 0.3; // -> false
```

### 💡 说明：

来自于 StackOverflow 上的问题[“浮点计算坏了？”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken)的答案：

> 程序中的常量 `0.2` 和 `0.3` 是最接近真实值的近似值。最接近 `0.2` 的 `double` 大于有理数 `0.2`，但最接近 `0.3` 的 `double` 小于有理数 `0.3`。`0.1` 和 `0.2` 的和大于有理数 `0.3`，因此在程序中进行常量比较会得到假。

这个问题太过于出名，甚至有一个网站叫 [0.30000000000000004.com](http://0.30000000000000004.com/)。这不仅仅是 JavaScript 特有的问题，在其他采用浮点计算的语言中也广泛存在。

## 扩展数字的方法

你可以向包装对象添加自己的方法，比如 `Number` 或 `String`。

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0).isOne(); // -> false
(7).isOne(); // -> false
```

### 💡 说明：

显然，在 JavaScript 中扩展 `Number` 对象和扩展其他对象并无不同之处。但是，扩展不符合规范的函数行为是不推荐的。以下是 `Number` 属性的列表：

- [**20.1** Number 对象](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## 三个数字的比较

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 说明：

为什么会这样呢？其实问题在于表达式的第一部分。以下是它的工作原理：

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

我们可以用 _大于或等于运算符（`>=`）_：

```js
3 > 2 >= 1; // true
```

详细了解规范中的关系运算符：

- [**12.10** 关系操作符](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## 有趣的数学

通常 JavaScript 中的算术运算的结果可能是非常难以预料的。 考虑这些例子：

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 说明：

前四个例子发生了什么？你可以参考此处的给出的关于 JavaScript 中的加法的对照表：

```
Number  + Number  -> 加法
Boolean + Number  -> 加法
Boolean + Boolean -> 加法
Number  + String  -> 串联字符串
String  + Boolean -> 串联字符串
String  + String  -> 串联字符串
```

那其他例子呢？在相加之前，`[]` 和 `{}` 隐式调用 `ToPrimitive` 和 `ToString` 方法。详细了解规范中的求值过程：

- [**12.8.3** 加法操作符 (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

不过需要注意此处的 `{} + []`，这是一个例外。你可以发现它的求值结果与 `[] + {}` 不同，这是因为当我们不加括号时，它被当作是一个空的代码块和一个一元加法运算符，这个运算符会把其后的 `[]` 转换为数字。具体如下：

```js
{
  // 代码块
}
+[]; // -> 0
```

当我们加上括号，情况就不一样了：

```js
({} + []); // -> [object Object]
```

## 正则表达式的加法

你知道可以做这样的运算吗？

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 说明：

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## 字符串不是 `String` 的实例

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 说明：

`String` 构造函数返回一个字符串：

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

再试试 `new`：

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

对象？啥玩意？

```js
new String("str"); // -> [String: 'str']
```

有关规范中的 String 构造函数的更多信息：

- [**21.1.1** String 构造函数](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## 用反引号调用函数

我们来声明一个返回所有参数的函数：

```js
function f(...args) {
  return args;
}
```

你肯定知道调用这个函数的方式应当是：

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

但是你知道你还可以使用反引号调用任意函数吗？

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 说明：

其实，如果你熟悉 _标签模板字面量_，你会知道这不是什么魔法。在上面的例子中，`f` 函数是模板字面量的标签。你可以定义这个标签以使用函数解析模板文字。标签函数的第一个参数是包含字符串的数组，剩余的参数与表达式有关。例：

```js
function template(strings, ...keys) {
  // 操作字符串和键值
}
```

这也是在 React 社区很流行的库[💅 styled-components](https://www.styled-components.com/)的[背后的秘密](http://mxstbr.blog/2016/11/styled-components-magic-explained/)。

规范的链接：

- [**12.3.7** 标签模板](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## 到底 call 了谁

> 由 [@cramforce](http://twitter.com/cramforce) 发现

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 说明：

注意，这可能会击碎你的三观！尝试在您的头脑中重现此代码：我们使用 `apply` 方法调用 `call` 方法。阅读更多：

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## `constructor` 属性

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 说明：

让我们逐步分解这个例子：

```js
// 声明一个新的常量字符串 'constructor'
const c = "constructor";

// c 是一个字符串
c; // -> 'constructor'

// 获取字符串的构造函数
c[c]; // -> [Function: String]

// 获取构造函数的构造函数
c[c][c]; // -> [Function: Function]

// 调用函数构造函数并将新函数的主体作为参数传递
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// 然后调用这个匿名函数得到的结果是一个字符串 'WTF'
c[c][c]('console.log("WTF?")')(); // > WTF
```

`Object.prototype.constructor` 返回一个创建示例对象的 `Object` 构造函数引用。当当前对象是字符串时，它是 `String`；当当前对象是数字时，它是 `Number`；以此类推。

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## 将对象做为另一个对象的 key

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 说明：

为何可以正常运行？这里我们使用的是 _计算属性_。当你将对象用方括号括起来当作对象的属性名时，它会将对象强制转换成一个字符串，所以我们得到属性键是 `[object Object]`，其值为 `{}`。

体验一下简单的“括号地狱”：

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// 结构:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

关于对象字面量，点击这里阅读更多：

- [对象初始化](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## 访问原型 `__proto__`

我们知道，原始数据（premitives）是没有原型的。但是，如果我们尝试获取原始数据的 `__proto__` 属性的值，我们会得到这样的一个结果：

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 说明：

这是因为原始数据的没有原型，它将使用 `ToObject` 方法包装在包装器对象中。这个步骤如下所示：

```js
(1).__proto__; // -> [Number: 0]
(1).__proto__.__proto__; // -> {}
(1).__proto__.__proto__.__proto__; // -> null
```

以下是关于 `__proto__`的更多信息：

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

下面的表达式结果如何？

```js
`${{ Object }}`;
```

答案是：

```js
// -> '[object Object]'
```

### 💡 说明：

我们通过 _简写属性表示_ 使用一个 `Object` 属性定义了一个对象：

```js
{
  Object: Object;
}
```

然后我们将该对象传递给模板文字，`toString` 方法调用该对象。这就是为什么我们得到字符串 `'[object Object]'`。

- [**12.2.9** 模板字面量](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- MDN 上的 [对象初始化](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)

## 使用默认值解构

考虑这个例子：

```js
let x,
  { x: y = 1 } = { x };
y;
```

这在面试中是一个很好的问题。问 `y` 的值是什么？ 答案是：

```js
// -> 1
```

### 💡 说明：

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

以上示例：

1. 我们声明了 `x`，但没有立刻赋值，所以它是 `undefined`。
2. 我们将 `x` 的值打包到对象属性 `x` 中。
3. 我们使用解构来提取 `x` 的值，并且要将这个值赋给 `y`。如果未定义该值，那么我们将使用 `1` 作为默认值。
4. 返回 `y` 的值。

- MDN 上的 [对象初始化](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)

## 点和扩展运算符

数组的扩展可以组成有趣的例子。考虑这个：

```js
[...[..."..."]].length; // -> 3
```

### 💡 说明：

为什么是 3？当我们使用[扩展运算符](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer)时，`@@iterator` 方法会被调用，而返回的迭代器用于获取要迭代的值。字符串的默认迭代器按字符展开字符串。展开之后，我们把这些字符打包成一个数组。然后再展开这个数组并再打包回数组。

一个 `'...'` 字符串包含 `.` ，所以结果数组的长度将 `3`。

现在，一步一步的看：

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

显然，我们可以展开和包装数组的元素任意多次，只要你想：

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// 以此类推 …
```

## 标签

很多程序员不知道 JavaScript 中也有标签，并且很有趣：

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 说明：

带标签的语句与 `break` 或 `continue` 语句一起使用。您可以使用标签来标识循环，然后使用 `break` 或 `continue` 语句来指示程序是否应该中断循环或继续执行它。

在上面的例子中，我们识别一个标签 `foo`。然后 `console.log（'first'）;` 执行，然后中断执行。

详细了解 JavaScript 中的标签：

- [**13.13** 标签语句 ](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [标签语句](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## 嵌套标签

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 说明：

和上面的例子类似，请遵循以下链接：

- [**12.16** 逗号运算符(`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** 标签语句](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [标签语句](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## 阴险的 `try..catch`

这个表达式将返回什么？`2` 还是 `3`？

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

答案是 `3`。惊讶吗？

### 💡 说明：

- [**13.15** `try` 语句](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## 这是多重继承吗？

看下面的例子：

```js
new class F extends (String, Array) {}(); // -> F []
```

这是多重继承吗？不。

### 💡 说明：

有趣的部分是 `extends` 子句的值（`（String，Array）`）。分组运算符总是返回其最后一个参数，所以 `（String，Array）` 实际上只是 `Array`。 这意味着我们刚刚创建了一个扩展 `Array` 的类。

- [**14.5** 类定义 ](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** 逗号运算符 (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## yield 返回自身的生成器

考虑这个 yield 返回自身的生成器例子：

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

如您所见，返回的值是一个值等于 `f` 的对象。那样的话，我们可以做这样的事情：

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // 再一次
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // 再一次
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// 以此类推
// …
```

### 💡 说明：

要理解为什么这样工作，请阅读规范的这些部分：

- [**25** 控制流抽象对象](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** 生成器对象](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## 类的类

考虑这个混淆语法：

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

似乎我们在类内部声明了一个类。应该是个错误，然而，我们得到一个 `'object'` 字符串。

### 💡 说明：

ECMAScript 5 时代以来，允许 _关键字_ 作为 _属性名称_。请看下面这个简单的对象示例：

```js
const foo = {
  class: function() {}
};
```

还有 ES6 标准中的简写方法定义。此外，类也可以是匿名的。因此，如果我们删去 `: function` 部分，将会得到：

```js
class {
  class() {}
}
```

默认类的结果总是一个简单的对象。其类型应返回 `'object'` 。

在这里阅读更多

- [**14.3** 方法定义](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** 类定义](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## 不可转换类型的对象

有一种方法可以摆脱类型的转换，那就是使用内置符号：

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

现在我们可以这样使用：

```js
// 对象
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// 字符串
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// 数字
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 说明：

- [Sergey Rubanov 的 gist](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** 内置符号](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## 棘手的箭头函数

考虑下面的例子：

```js
let f = () => 10;
f(); // -> 10
```

这看起来没问题，但是如果这样呢？

```js
let f = () => {};
f(); // -> undefined
```

### 💡 说明：

你可能觉得应该返回 `{}` 而不是 `undefined`。这是因为花括号是箭头函数语法的一部分，所以 `f` 会返回 `undefined`。不过要从箭头函数明确返回 `{}` 对象也是有可能的，这时你需要用括号把返回值括起来。

```js
let f = () => ({});
f(); // -> {}
```

## 箭头函数不能作为构造函数

考虑下面的例子：

```js
let f = function() {
  this.a = 1;
};
new f(); // -> { 'a': 1 }
```

现在，试着用箭头函数做同样的事情：

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 说明：

箭头函数不能作为构造函数调用，并且会在 `new` 的时候抛出错误。因为它具有词域 `this`，而且它也没有 `prototype` 属性，所以这样做没什么意义。

## `arguments` 和箭头函数

考虑下面的例子：

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

现在，试着用箭头函数做同样的事情：

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 说明：

箭头函数是常规函数的轻量级版本，注重于短小和词域 `this`。同时箭头函数不提供 `arguments` 对象的绑定。你可以使用 `剩余参数（rest parameters）` 来得到同样的结果：

```js
let f = (...args) => args;
f("a");
```

- MDN 上的 [箭头函数](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

## 棘手的返回

`return` 语句是很棘手的. 看下面的代码:

<!-- prettier-ignore-start -->
```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```
<!-- prettier-ignore-end -->

### 💡 说明：

`return` 和返回的表达式必须在同一行:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

这是因为一个叫自动分号插入的概念，它会在大部分换行处插入分号。第一个例子里，`return` 语句和对象字面量中间被插入了一个分号。所以函数返回 `undefined`，其后的对象字面量永远不会被求值。

- [**11.9.1** 自动分号插入的规则](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** `return` 语句](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## 对象的链式赋值

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

从右到左，`{n: 2}` 被赋值给 `foo`，而此赋值的结果 `{n: 2}` 被赋值给 `foo.x`，因此 `bar` 是 `{n: 1, x: {n: 2}}`，毕竟 `bar` 是 `foo` 的一个引用。但为什么 `foo.x` 是 `undefined` 而 `bar.x` 不是呢？

### 💡 说明：

`foo` 和 `bar` 引用同一个对象 `{n: 1}`，而左值在赋值前解析。`foo = {n: 2}` 是创建一个新对象，所以 `foo` 被更新为引用那个新的对象。因为 `foo.x = ...` 中的 `foo` 作为左值在赋值前就被解析并依然引用旧的 `foo = {n: 1}` 对象并为其添加了 `x` 值。在链式赋值之后，`bar` 依然引用旧的 `foo` 对象，但 `foo` 更新为没有 `x` 属性的 `{n: 2}` 对象。

它等价于：

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// bar.x 指向新的 foo 对象的地址
// 这不等价于：bar.x = {n: 2}
```

## 使用数组访问对象属性

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1
```

那关于伪多维数组创建对象呢？

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 说明：

`[]` 操作符会使用 `toString` 将传递的表达式转换为字符串。将单元素数组转换为字符串，相当于将这个元素转换为字符串：

```js
["property"].toString(); // -> 'property'`
```

## `Number.toFixed()` 显示不同的数字

`Number.toFixed()` 在不同的浏览器中会表现得有点奇怪。看看这个例子：

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 说明：

尽管你的第一直觉可能是 IE11 是正确的而 Firefox/Chrome 错了，事实是 Firefox/Chrome 更直接地遵循数字运算的标准（IEEE-754 Floating Point），而 IE11 经常违反它们（可能）去努力得出更清晰的结果。

你可以通过一些快速的测试来了解为什么它们发生：

```js
// 确认 5 向下取整的奇怪结果
(0.7875).toFixed(3); // -> 0.787
// 当你展开到 64 位（双精度）浮点数准确度限制时看起来就是一个 5
(0.7875).toFixed(14); // -> 0.78750000000000
// 但如果你超越这个限制呢？
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

浮点数在计算机内部不是以一系列十进制数字的形式存储的，而是通过一个可以产生一点点通常会被 toString 或者其他调用取整的不准确性的更复杂的方法，但它实际上在内部会被表示。

在这里，那个结尾的 "5" 实际上是一个极其小的略小于 5 的分数。将其以任何常理的长度取整它都会被看作一个 5，但它在内部通常不是 5。

然而 IE11 会直接在这个数字后面补 0，甚至在 toFixed(20) 的时候也是这样，因为它看起来强制取整了值来减少硬件限制带来的问题。

详见 ECMA-262 中 `NOTE 2` 的 `toFixed` 的定义。

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `min` 大于 `max`

我发现一个神奇的例子：

```js
Math.min() > Math.max(); // -> true
Math.min() < Math.max(); // -> false
```

### 💡 说明：

这是一个简单的例子。我们一步一步来：

```js
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Infinity > -Infinity; // -> true
```

为什么是这样呢？其实 `Math.max()` 并不会返回最大的正数，即 `Number.MAX_VALUE`。

`Math.max` 接受两个参数，将它们转换到数字，比较之后返回最大的那个。若没有传入参数，结果将是 -∞。若参数中存在 `NaN`，则返回 `NaN`。

反过来，当 `Math.min` 没有传入参数，会返回 ∞。

- [**15.8.2.11** Math.max](https://262.ecma-international.org/5.1/#sec-15.8.2.11)
- [**15.8.2.11** Math.min](https://262.ecma-international.org/5.1/#sec-15.8.2.12)
- [为什么 `Math.max()` 小于 `Math.min()`？](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min)## `Math.max()` 小于 `Math.min()`

```js
Math.min(1, 4, 7, 2); // -> 1
Math.max(1, 4, 7, 2); // -> 7
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Math.min() > Math.max(); // -> true
```

### 💡 说明：

- Charlie Harvey 的 [Why is Math.max() less than Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min)

## 比较 `null` 和 `0`

下面的表达式似乎有点矛盾：

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

既然 `null >= 0` 返回 `true`，为什么 `null` 既不等于也不大于 `0`？（对于小于比较也可以得出相似的结果。）

### 💡 说明：

这三个表达式的求值方式各不相同，因此产生了非预期的结果。
首先，对于 `null == 0` 这个抽象相等比较操作，通常当该运算符不能正确地比较两边的值，则它会将两边的值都转换为数字，再对数字进行比较。那么，您可能会期望以下行为：

```js
// 事实并非如此
(null == 0 + null) == +0;
0 == 0;
true;
```

然而，仔细阅读规范就会发现，数字转换实际上并没有发生在 `null` 或 `undefined` 的一侧。也就是说，如果在等号的一侧有 `null`，则当另一侧的表达式为 `null` 或 `undefined`就返回 `true`；反之则返回 `false`。

接下来，对于 `null > 0` 这个比较关系。与抽象相等运算符的算法不同，它 _会_ 先将 `null` 转换为一个数字。因此，我们得到这样的行为:

```js
null > 0
+null = +0
0 > 0
false
```

最后一个，对于 `null >= 0` 的比较关系。你可能认为这个表达式应该等同于 `null > 0 || null == 0` 的结果；如果真是这样，那么基于上述的讨论，这里的结果也应当是 `false` 才对。然而，`>=` 操作符的工作方式实际上是 `<` 操作符的取反。在我们上述的讨论中，关于大于运算符的论述也适用于小于运算符，也就是说这个表达式的值是这样出来的：

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** 抽象关系比较](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.13** 抽象相等比较](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison)
- [一篇深入浅出的说明](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274)

## 相同变量重复声明

JS 允许重复声明变量：

```js
a;
a;
// 这也是有效的
a, a;
```

严格模式也可以运行：

```js
var a, a, a;
var a;
var a;
```

### 💡 解释：

所有的定义都被合并成一条定义。

- [**13.3.2** 变量表达式](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## Array.prototype.sort() 的默认行为

假设你需要对数组排序。

```
[ 10, 1, 3 ].sort() // -> [ 1, 10, 3 ]
```

### 💡 说明：

默认的排序算法基于将给定元素转换为字符串，然后比较它们的 UTF-16 序列中的值。

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### 提示

传入一个 `compareFn` 比较函数，对非字符串的其他值排序。

```
[ 10, 1, 3 ].sort((a, b) => a - b) // -> [ 1, 3, 10 ]
```

## resolve() 不会返回 Promise 实例

```javascript
const theObject = {
  a: 7
};
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // -> Promise 实例对象

thePromise.then(value => {
  console.log(value === theObject); // -> true
  console.log(value); // -> { a: 7 }
});
```

从 `thePromise` 接收到的 `value` 值确实是 `theObject`。

那么，如果向 `resolve` 传入另外一个 `Promise` 会怎样？

```javascript
const theObject = new Promise((resolve, reject) => {
  resolve(7);
}); // -> Promise 实例对象
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // -> Promise 实例对象

thePromise.then(value => {
  console.log(value === theObject); // -> false
  console.log(value); // -> 7
});
```

### 💡 说明：

> 此函数将类 promise 对象的多层嵌套平铺到单层嵌套。（例如上述的 promise 函数 resolve 了另一个会 resolve 出其他对象的 promise 函数）

&ndash; [MDN 上的 Promise.resolve()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

官方规范是 [ECMAScript 25.6.1.3.2 Promise 的 Resolve 函数](https://tc39.es/ecma262/#sec-promise-resolve-functions)，但是这一章节对人类非常不友好。

## `{}{}` 是 undefined

你可以在终端测试一下。类似这样的结构会返回最后定义的对象中的值。

```js
{}{}; // -> undefined
{}{}{}; // -> undefined
{}{}{}{}; // -> undefined
{foo: 'bar'}{}; // -> 'bar'
{}{foo: 'bar'}; // -> 'bar'
{}{foo: 'bar'}{}; // -> 'bar'
{a: 'b'}{c:' d'}{}; // -> 'd'
{a: 'b', c: 'd'}{}; // > SyntaxError: Unexpected token ':'
({}{}); // > SyntaxError: Unexpected token '{'
```

### 💡 说明：

解析到 `{}` 会返回 `undefined`，而解析 `{foo: 'bar'}{}`时，表达式 `{foo: 'bar'}` 返回 `'bar'`。

`{}` 有两重含义：表示对象，或表示代码块。例如，在 `() => {}` 中的 `{}` 表示代码块。所以我们必须加上括号：`() => ({})` 才能让它正确地返回一个对象。

因此，我们现在将 `{foo: 'bar'}` 当作代码块使用，则可以在终端中这样写：

```js
if (true) {
  foo: "bar";
} // -> 'bar'
```

啊哈，一样的结果！所以 `{foo: 'bar'}{}` 中的花括号就是表示代码块。

## `arguments` 绑定

考虑以下函数：

```js
function a(x) {
  arguments[0] = "hello";
  console.log(x);
}

a(); // > undefined
a(1); // > "hello"
```

### 💡 说明

`arguments` 是一个类数组对象，包含了所有传入当前函数的参数。当没有传入参数时，该对象中就不存在 `x` 属性，也就无法覆盖。

- [arguments 对象](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) on MDN

## 来自地狱的 `alert`

如题，从地狱而来的代码：

```js
[666]["\155\141\160"]["\143\157\156\163\164\162\165\143\164\157\162"](
  "\141\154\145\162\164(666)"
)(666); // alert(666)
```

### 💡 说明

这一串代码是基于多个采用了八进制转义序列的字符串构造的。

任何码值小于 256 的字符（又称扩展 ASCII 码表域）都可以用 `\` 加上其八进制代码的转义方式写出来。上面这个简单的例子就是将 `alert` 编码到八进制转义序列。

- [Martin Kleppe 的推特](https://twitter.com/aemkei/status/897172907222237185)
- [JavaScript 字符转义序列](https://mathiasbynens.be/notes/javascript-escapes#octal)
- [多行 JavaScript 字符串](https://davidwalsh.name/multiline-javascript-strings)

## 没有尽头的计时

如果我们对 `setTimeout` 赋予无限大会如何？

```js
setTimeout(() => console.log("called"), Infinity); // -> <timeoutId>
// > 'called'
```

结果是，它会立即运行，并没有等待无限长的时间。

### 💡 说明：

通常运行时内部会将延时存储为一个 32 位的有符号整数，而上述代码会导致运行时在解析延时参数时发生整数溢出，从而使函数立即执行而不等待。

例如，在 Node.js 中我们可以看到这样的警告信息：

```
(node:1731) TimeoutOverflowWarning: Infinity does not fit into a 32-bit signed integer.
Timeout duration was set to 1.
(Use `node --trace-warnings ...` to show where the warning was created)
```

- [WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout) on MDN
- [Node.js 文档中关于计时器的章节](https://nodejs.org/api/timers.html#timers_settimeout_callback_delay_args)
- W3C 上的 [计时器]](https://www.w3.org/TR/2011/WD-html5-20110525/timers.html)

## `setTimeout` 对象

如果我们给 `setTimeout` 的回调函数参数传非函数值会发生什么？

```js
setTimeout(123, 100); // -> <timeoutId>
// > 'called'
```

没问题。

```js
setTimeout('{a: 1}', 100); // -> <timeoutId>
// > 'called'
```

这个也没问题。

```js
setTimeout({a: 1}, 100); // -> <timeoutId>
// > 'Uncaught SyntaxError: Unexpected identifier               setTimeout (async) (anonymous) @ VM__:1'
// 未捕获的语法错误：非预期的标识符
```

抛出了一个 **SyntaxError**（语法错误）。

这种错误很容易发生，尤其是当你有个函数返回一个对象，但是你忘了将其传进函数，直接就在这里调用了！不过，如果 `content-policy` 设置为 `self` 会怎么样呢？

```js
setTimeout(123, 100); // -> <timeoutId>
// > console.error("[Report Only] Refused to evaluate a string as JavaScript because 'unsafe-eval' is not an allowed source of script in the following Content Security Policy directive: "script-src 'report-sample' 'self' ")
// [仅报告] 拒绝将字符串当作JavaScript求值，因为内容安全策略（CSP，Content Security Policy）指令被设置为 "script-src 'report-sample' 'self'"，在该指令模式下不允许 'unsafe-eval' 的脚本源。
```

终端会拒绝执行！

### 💡 说明：

`WindowOrWorkerGlobalScope.setTimeout()` 的第一个参数可以是代码（`code`），代码会被传递到 `eval` 函数，这是不好的。`eval` 会把所有输入强制转换为字符串，然后进行求值，那么对象会变成 `'[object Object]'`；嗯，你也看到了，这里确实有一个非法标识符 `'Unexpected identifier'`。

- [eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) on MDN (don't use this)
- [WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout) on MDN
- [内容安全策略](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)
- W3C 上的 [计时器](https://www.w3.org/TR/2011/WD-html5-20110525/timers.html)

## 点点运算符

现在尝试把一个数字转换到字符串：

```js
27.toString() // > Uncaught SyntaxError: Invalid or unexpected token
// 未捕获的语法错误：非法或非预期的词元（token）
```

如果我们再加上一个点呢？

```js
27..toString(); // -> '27'
```

那为什么第一个例子错了呢？

### 💡 说明：

这是文法的限制。

`.` 运算符存在歧义，它既可以当属性访问符，也可以是小数点，这取决于它在代码中的位置。

规范中定义了 `.` 运算符仅在特定的位置使用时会被当作小数点，这个定义写在 ECMAScript 的数字字面量语法一节中。

所以，当你想要在数字后加属性访问器的点号时，应当加上括号，或再加上一个点，以使该表达式合法。

```js
(27).toString(); // -> '27'
// or
27..toString(); // -> '27'
```

- [JavaScript 中 toString 的用法](https://stackoverflow.com/questions/6853865/usage-of-tostring-in-javascript/6853910#6853910) on StackOverflow
- [为什么 10..toString() 可行，而 10.toString() 却不行？](https://stackoverflow.com/questions/13149282/why-does-10-tostring-work-but-10-tostring-does-not/13149301#13149301)

## 再 new 一次

这仅仅是一个用于娱乐的例子。

```js
class Foo extends Function {
  constructor(val) {
    super();
    this.prototype.val = val;
  }
}

new new Foo(":D")().val; // -> ':D'
```

### 💡 说明：

JavaScript 与其他面向对象语言不同，它的构造函数仅是一个比较特殊的函数。虽然 class 语法糖让你可以创建一个字面上的类，但实例化后它就变成了函数，因此它可以再次实例化。

虽然我没有测试过，但我觉得最后的那个表达式应该是这样分析的：

```js
new new Foo(":D")().val(new newFooInstance()).val;
veryNewFooInstance.val;
// -> ':D'
```

再补充一下，运行 `new Function('return "bar";')` 必然会创建一个内容为 `return "bar";` 的函数对象。而`Foo`类的构造函数中的 `super()` 调用的是 `Function` 的构造函数，所以自然而然我们可以在它上面添加更多的操作。

```js
class Foo extends Function {
  constructor(val) {
    super(`
      this.val = arguments[0];
    `);
    this.prototype.val = val;
  }
}

var foo = new new Foo(":D")("D:");
foo.val; // -> 'D:'
delete foo.val; // 移除这个实例的“val”属性，让它退回（defer back）到他的原型的“val”属性
foo.val; // -> ':D'
```

- [扩展 Function 的类：再 new 一次](https://github.com/denysdovhan/wtfjs/issues/78)

## 你应该用上分号

下面这个应该是标准的 JavaScript……吧？不，它炸了！

```js
class SomeClass {
  ["array"] = []
  ["string"] = "str"
}

new SomeClass().array; // -> 'str'
```

woc……？

### 💡 说明：

嗯，你没猜错，这又是自动分号插入的功劳。

上面这个例子实际上会被转换为：

```js
class SomeClass {
  ["array"] = ([]["string"] = "str");
}
```

看到了吧，`str` 这个字符串被赋值到属性 `array` 上。

- Ryan Cavanaugh 发布的 [关于这个例子的原创推特](https://twitter.com/SeaRyanC/status/1148726605222535168)
- [TC39 会议中关于它的讨论](https://github.com/tc39/notes/blob/master/meetings/2017-09/sept-26.md)

## 用空格分割（split）字符串

你试过用空格分割字符串吗？

```js
"".split(""); // -> []
// 但是……
"".split(" "); // -> [""]
```

### 💡 说明：

这是预期行为。它会在输入的字符串中遍历，一旦发现分隔符，就在此处分割。但若你传入的是空字符串，它找不到分隔符，因此返回该字符串。

规范引用如下：

> 它会从左向右搜索字符串，并根据 `separator`（分隔符）决定子字符串的分割位置；分割位置的字符仅用于分割，不会包含在返回的数组中。

- [**22.1.3.21** String.prototype.split](https://tc39.es/ecma262/#sec-string.prototype.split)
- Ryan Cavanaugh 发布的 [关于这个例子的原创推特](https://twitter.com/SeaRyanC/status/1331656278104440833)
- Nabil Tharwat 发布的 [包含解释的推特](https://twitter.com/kl13nt/status/1331742810932916227?s=20)

## 对字符串 stringify

这会导致一个缺陷，我曾经修了好几天：

```js
JSON.stringify("production") === "production"; // -> false
```

### 💡 说明：

先看看 `JSON.stringify` 的返回值：

```js
JSON.stringify("production"); // -> '"production"'
```

原来是被“字串化”了，所以这也难怪：

```js
'"production"' === "production"; // -> false
```

- [ECMA-404 JSON 数据内部变动标准](https://www.json.org/json-en.html)

## 对数字和 `true` 的非严格相等比较

```js
1 == true; // -> true
// 但是……
Boolean(1.1); // -> true
1.1 == true; // -> false
```

### 💡 说明：

根据规范：

> 比较 x == y 时，当 x 和 y 都有值，会返回 true 或 false。比较过程如下所述：
>
> 4. 若 `Type(x)` 是数字且 `Type(y)` 是字符串，则会返回 `x == ! ToNumber(y)` 的结果。

所以比较过程是这样的：

```js
1 == true;
1 == Number(true);
1 == 1; // -> true
// 但是……
1.1 == true;
1.1 == Number(true);
1.1 == 1; // -> false
```

- [**7.2.15** 抽象相等比较](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

# 其他资源

- [wtfjs.com](http://wtfjs.com/) — 一些非常特别的不规范与不一致的集合，以及对于 web 编程语言来说非常痛苦的时光。
- [Wat](https://www.destroyallsoftware.com/talks/wat) — CodeMash 2012 中 Gary Bernhardt 的演讲
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — Kyle Simpsons 在 Forward 2 的演讲，描述了“疯狂的 JavaScript”。他希望帮助你写出更干净、更优雅、更易读的代码，鼓励人们为开源社区做出贡献。
- [Zeros in JavaScript](http://zero.milosz.ca/) — 针对 JavaScript 中的 `==`、`===`、`+` 和 `*` 的真值表。

# 🤝 捐赠支持

你好！这个项目是我在空闲时间做的，作为我的主要工作的补充。我希望你在阅读这篇文章时保持愉快的心情。请考虑支持我 🙏。

每一次捐赠对我来说意义重大。你的捐赠是对我的工作的肯定：我的工作有价值。

**🙏 感谢您的支持！ 🙏**

| 服务             |                     链接                     |                                                                    动作                                                                    |
| ---------------- | :------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| **Patreon**      |        [Become a patron][patreon-url]        | <a href="https://patreon.com/denysdovhan"><img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="120px"></a> |
| **BuyMeACoffee** |     [Buy me a cup of ☕️ or 🥤][bmc-url]     |    <a href="https://buymeacoffee.com/denysdovhan"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" width="120px"></a>     |
| **Bitcoin**      |     `1EJsKs6rPsqa7QLoVLpe3wgcdL9Q8WmDxE`     |      <img src="https://user-images.githubusercontent.com/3459374/107130426-0ae4f800-68d6-11eb-9b86-15bf33467615.png" width="120px"/>       |
| **Ethereum**     | `0x6aF39C917359897ae6969Ad682C14110afe1a0a1` |      <img src="https://user-images.githubusercontent.com/3459374/107130370-55b24000-68d5-11eb-93f5-075355c7fcd4.png" width="120px"/>       |

> **⚠️ 提示：** 我现居乌克兰，乌克兰的银行账户没办法绑定 PayPal 或 Stripe 之类的账户。所以我没法开启 Github Sponsors、OpenCollective 和其他依赖于这些服务的捐赠渠道。对不起，目前您只能通过这些方式支持我。

# 🎓 许可证

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
[patreon-url]: https://patreon.com/denysdovhan
[patreon-image]: https://img.shields.io/badge/support-patreon-F96854.svg?style=flat-square
[bmc-url]: https://patreon.com/denysdovhan
[bmc-image]: https://img.shields.io/badge/support-buymeacoffee-222222.svg?style=flat-square
```

## File: `README.md`
```markdown
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

Despite the fact that `document.all` is an array-like object and it gives access to the DOM nodes in the page, it responds to the `typeof` function as `undefined`.

```js
document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'
```

At the same time, `document.all` is not equal to `undefined`.

```js
document.all === undefined; // -> false
document.all === null; // -> false
```

But at the same time:

```js
document.all == null; // -> true
```

### 💡 Explanation:

> `document.all` used to be a way to access DOM elements, in particular with old versions of IE. While it has never been a standard it was broadly used in the old age JS code. When the standard progressed with new APIs (such as `document.getElementById`) this API call became obsolete and the standard committee had to decide what to do with it. Because of its broad use they decided to keep the API but introduce a willful violation of the JavaScript specification.
> The reason why it responds to `false` when using the [Strict Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-strict-equality-comparison) with `undefined` while `true` when using the [Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison) is due to the willful violation of the specification that explicitly allows that.
>
> &mdash; [“Obsolete features - document.all”](https://html.spec.whatwg.org/multipage/obsolete.html#dom-document-all) at WhatWG - HTML spec
> &mdash; [“Chapter 4 - ToBoolean - Falsy values”](https://github.com/getify/You-Dont-Know-JS/blob/0d79079b61dad953bbfde817a5893a49f7e889fb/types%20%26%20grammar/ch4.md#falsy-objects) at YDKJS - Types & Grammar

## Minimal value is greater than zero

`Number.MIN_VALUE` is the smallest number, which is greater than zero:

```js
Number.MIN_VALUE > 0; // -> true
```

### 💡 Explanation:

> `Number.MIN_VALUE` is `5e-324`, i.e. the smallest positive number that can be represented within float precision, i.e. that's as close as you can get to zero. It defines the best resolution that floats can give you.
>
> Now the overall smallest value is `Number.NEGATIVE_INFINITY` although it's not really numeric in a strict sense.
>
> &mdash; [“Why is `0` less than `Number.MIN_VALUE` in JavaScript?”](https://stackoverflow.com/questions/26614728/why-is-0-less-than-number-min-value-in-javascript) at StackOverflow

- [**20.1.2.9** Number.MIN_VALUE](https://www.ecma-international.org/ecma-262/#sec-number.min_value)

## function is not a function

> ⚠️ A bug present in V8 v5.5 or lower (Node.js <=7) ⚠️

All of you know about the annoying _undefined is not a function_, but what about this?

```js
// Declare a class which extends null
class Foo extends null {}
// -> [Function: Foo]

new Foo() instanceof null;
// > TypeError: function is not a function
// >     at … … …
```

### 💡 Explanation:

This is not a part of the specification. It's just a bug that has now been fixed, so there shouldn't be a problem with it in the future.

### Super constructor null of Foo is not a constructor

It's continuation of story with previous bug in modern environment (tested with Chrome 71 and Node.js v11.8.0).

```js
class Foo extends null {}
new Foo() instanceof null;
// > TypeError: Super constructor null of Foo is not a constructor
```

### 💡 Explanation:

This is not a bug because:

```js
Object.getPrototypeOf(Foo.prototype); // -> null
```

If the class has no constructor the call from prototype chain. But in the parent has no constructor. Just in case, I’ll clarify that `null` is an object:

```js
typeof null === "object";
```

Therefore, you can inherit from it (although in the world of the OOP for such terms would have beaten me). So you can't call the null constructor. If you change this code:

```js
class Foo extends null {
  constructor() {
    console.log("something");
  }
}
```

You see the error:

```
ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor
```

And if you add `super`:

```js
class Foo extends null {
  constructor() {
    console.log(111);
    super();
  }
}
```

JS throws an error:

```
TypeError: Super constructor null of Foo is not a constructor
```

- [An explanation of this issue](https://github.com/denysdovhan/wtfjs/pull/102#discussion_r259143582) by [@geekjob](https://github.com/geekjob)

## Adding arrays

What if you try to add two arrays?

```js
[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'
```

### 💡 Explanation:

The concatenation happens. Step-by-step, it looks like this:

```js
[1, 2, 3] +
  [4, 5, 6][
    // call toString()
    (1, 2, 3)
  ].toString() +
  [4, 5, 6].toString();
// concatenation
"1,2,3" + "4,5,6";
// ->
("1,2,34,5,6");
```

## Trailing commas in array

You've created an array with 4 empty elements. Despite all, you'll get an array with three elements, because of trailing commas:

```js
let a = [, , ,];
a.length; // -> 3
a.toString(); // -> ',,'
```

### 💡 Explanation:

> **Trailing commas** (sometimes called "final commas") can be useful when adding new elements, parameters, or properties to JavaScript code. If you want to add a new property, you can simply add a new line without modifying the previously last line if that line already uses a trailing comma. This makes version-control diffs cleaner and editing code might be less troublesome.
>
> &mdash; [Trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) at MDN

## Array equality is a monster

Array equality is a monster in JS, as you can see below:

```js
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

### 💡 Explanation:

You should watch very carefully for the above examples! The behaviour is described in section [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison) of the specification.

## `undefined` and `Number`

If we don't pass any arguments into the `Number` constructor, we'll get `0`. The value `undefined` is assigned to formal arguments when there are no actual arguments, so you might expect that `Number` without arguments takes `undefined` as a value of its parameter. However, when we pass `undefined`, we will get `NaN`.

```js
Number(); // -> 0
Number(undefined); // -> NaN
```

### 💡 Explanation:

According to the specification:

1. If no arguments were passed to this function's invocation, let `n` be `+0`.
2. Else, let `n` be ? `ToNumber(value)`.
3. In case of `undefined`, `ToNumber(undefined)` should return `NaN`.

Here's the corresponding section:

- [**20.1.1** The Number Constructor](https://www.ecma-international.org/ecma-262/#sec-number-constructor)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## `parseInt` is a bad guy

`parseInt` is famous by its quirks:

```js
parseInt("f*ck"); // -> NaN
parseInt("f*ck", 16); // -> 15
```

**💡 Explanation:** This happens because `parseInt` will continue parsing character-by-character until it hits a character it doesn't know. The `f` in `'f*ck'` is the hexadecimal digit `15`.

Parsing `Infinity` to integer is something…

```js
//
parseInt("Infinity", 10); // -> NaN
// ...
parseInt("Infinity", 18); // -> NaN...
parseInt("Infinity", 19); // -> 18
// ...
parseInt("Infinity", 23); // -> 18...
parseInt("Infinity", 24); // -> 151176378
// ...
parseInt("Infinity", 29); // -> 385849803
parseInt("Infinity", 30); // -> 13693557269
// ...
parseInt("Infinity", 34); // -> 28872273981
parseInt("Infinity", 35); // -> 1201203301724
parseInt("Infinity", 36); // -> 1461559270678...
parseInt("Infinity", 37); // -> NaN
```

Be careful with parsing `null` too:

```js
parseInt(null, 24); // -> 23
```

**💡 Explanation:**

> It's converting `null` to the string `"null"` and trying to convert it. For radixes 0 through 23, there are no numerals it can convert, so it returns NaN. At 24, `"n"`, the 14th letter, is added to the numeral system. At 31, `"u"`, the 21st letter, is added and the entire string can be decoded. At 37 on there is no longer any valid numeral set that can be generated and `NaN` is returned.
>
> &mdash; [“parseInt(null, 24) === 23… wait, what?”](https://stackoverflow.com/questions/6459758/parseintnull-24-23-wait-what) at StackOverflow

Don't forget about octals:

```js
parseInt("06"); // 6
parseInt("08"); // 8 if support ECMAScript 5
parseInt("08"); // 0 if not support ECMAScript 5
```

**💡 Explanation:** If the input string begins with "0", radix is eight (octal) or 10 (decimal). Exactly which radix is chosen is implementation-dependent. ECMAScript 5 specifies that 10 (decimal) is used, but not all browsers support this yet. For this reason always specify a radix when using `parseInt`.

`parseInt` always convert input to string:

```js
parseInt({ toString: () => 2, valueOf: () => 1 }); // -> 2
Number({ toString: () => 2, valueOf: () => 1 }); // -> 1
```

Be careful while parsing floating point values

```js
parseInt(0.000001); // -> 0
parseInt(0.0000001); // -> 1
parseInt(1 / 1999999); // -> 5
```

**💡 Explanation:** `ParseInt` takes a string argument and returns an integer of the specified radix. `ParseInt` also strips anything after and including the first non-digit in the string parameter. `0.000001` is converted to a string `"0.000001"` and the `parseInt` returns `0`. When `0.0000001` is converted to a string it is treated as `"1e-7"` and hence `parseInt` returns `1`. `1/1999999` is interpreted as `5.00000250000125e-7` and `parseInt` returns `5`.

## Math with `true` and `false`

Let's do some math:

```js
true + true; // -> 2
(true + true) * (true + true) - true; // -> 3
```

Hmmm… 🤔

### 💡 Explanation:

We can coerce values to numbers with the `Number` constructor. It's quite obvious that `true` will be coerced to `1`:

```js
Number(true); // -> 1
```

The unary plus operator attempts to convert its value into a number. It can convert string representations of integers and floats, as well as the non-string values `true`, `false`, and `null`. If it cannot parse a particular value, it will evaluate to `NaN`. That means we can coerce `true` to `1` easier:

```js
+true; // -> 1
```

When you're performing addition or multiplication, the `ToNumber` method is invoked. According to the specification, this method returns:

> If `argument` is **true**, return **1**. If `argument` is **false**, return **+0**.

That's why we can add boolean values as regular numbers and get correct results.

Corresponding sections:

- [**12.5.6** Unary `+` Operator](https://www.ecma-international.org/ecma-262/#sec-unary-plus-operator)
- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.3** ToNumber(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tonumber)

## HTML comments are valid in JavaScript

You will be impressed, but `<!--` (which is known as HTML comment) is a valid comment in JavaScript.

```js
// valid comment
<!-- valid comment too
```

### 💡 Explanation:

Impressed? HTML-like comments were intended to allow browsers that didn't understand the `<script>` tag to degrade gracefully. These browsers, e.g. Netscape 1.x are no longer popular. So there is really no point in putting HTML comments in your script tags anymore.

Since Node.js is based on the V8 engine, HTML-like comments are supported by the Node.js runtime too. Moreover, they're a part of the specification:

- [**B.1.3** HTML-like Comments](https://www.ecma-international.org/ecma-262/#sec-html-like-comments)

## `NaN` is ~~not~~ a number

Type of `NaN` is a `'number'`:

```js
typeof NaN; // -> 'number'
```

### 💡 Explanation:

Explanations of how `typeof` and `instanceof` operators work:

- [**12.5.5** The `typeof` Operator](https://www.ecma-international.org/ecma-262/#sec-typeof-operator)
- [**12.10.4** Runtime Semantics: InstanceofOperator(`O`,`C`)](https://www.ecma-international.org/ecma-262/#sec-instanceofoperator)

## `[]` and `null` are objects

```js
typeof []; // -> 'object'
typeof null; // -> 'object'

// however
null instanceof Object; // false
```

### 💡 Explanation:

The behavior of `typeof` operator is defined in this section of the specification:

- [**13.5.3** The `typeof` Operator](https://262.ecma-international.org/12.0/#sec-typeof-operator)

According to the specification, the `typeof` operator returns a string according to [Table 37: `typeof` Operator Results](https://262.ecma-international.org/12.0/#table-typeof-operator-results). For `null`, ordinary, standard exotic and non-standard exotic objects, which do not implement `[[Call]]`, it returns the string `"object"`.

However, you can check the type of an object by using the `toString` method.

```js
Object.prototype.toString.call([]);
// -> '[object Array]'

Object.prototype.toString.call(new Date());
// -> '[object Date]'

Object.prototype.toString.call(null);
// -> '[object Null]'
```

## Magically increasing numbers

```js
999999999999999; // -> 999999999999999
9999999999999999; // -> 10000000000000000

10000000000000000; // -> 10000000000000000
10000000000000000 + 1; // -> 10000000000000000
10000000000000000 + 1.1; // -> 10000000000000002
```

### 💡 Explanation:

This is caused by IEEE 754-2008 standard for Binary Floating-Point Arithmetic. At this scale, it rounds to the nearest even number. Read more:

- [**6.1.6** The Number Type](https://www.ecma-international.org/ecma-262/#sec-ecmascript-language-types-number-type)
- [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) on Wikipedia

## Precision of `0.1 + 0.2`

A well-known joke. An addition of `0.1` and `0.2` is deadly precise:

```js
0.1 + 0.2; // -> 0.30000000000000004
0.1 + 0.2 === 0.3; // -> false
```

### 💡 Explanation:

The answer for the [”Is floating point math broken?”](https://stackoverflow.com/questions/588004/is-floating-point-math-broken) question on StackOverflow:

> The constants `0.2` and `0.3` in your program will also be approximations to their true values. It happens that the closest `double` to `0.2` is larger than the rational number `0.2` but that the closest `double` to `0.3` is smaller than the rational number `0.3`. The sum of `0.1` and `0.2` winds up being larger than the rational number `0.3` and hence disagreeing with the constant in your code.

This problem is so known that there is even a website called [0.30000000000000004.com](http://0.30000000000000004.com/). It occurs in every language that uses floating-point math, not just JavaScript.

## Patching numbers

You can add your own methods to wrapper objects like `Number` or `String`.

```js
Number.prototype.isOne = function() {
  return Number(this) === 1;
};

(1.0).isOne(); // -> true
(1).isOne(); // -> true
(2.0).isOne(); // -> false
(7).isOne(); // -> false
```

### 💡 Explanation:

Obviously, you can extend the `Number` object like any other object in JavaScript. However, it's not recommended if the behavior of the defined method is not a part of the specification. Here is the list of `Number`'s properties:

- [**20.1** Number Objects](https://www.ecma-international.org/ecma-262/#sec-number-objects)

## Comparison of three numbers

```js
1 < 2 < 3; // -> true
3 > 2 > 1; // -> false
```

### 💡 Explanation:

Why does this work that way? Well, the problem is in the first part of an expression. Here's how it works:

```js
1 < 2 < 3; // 1 < 2 -> true
true < 3; // true -> 1
1 < 3; // -> true

3 > 2 > 1; // 3 > 2 -> true
true > 1; // true -> 1
1 > 1; // -> false
```

We can fix this with _Greater than or equal operator (`>=`)_:

```js
3 > 2 >= 1; // true
```

Read more about Relational operators in the specification:

- [**12.10** Relational Operators](https://www.ecma-international.org/ecma-262/#sec-relational-operators)

## Funny math

Often the results of arithmetic operations in JavaScript might be quite unexpected. Consider these examples:

```js
 3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

### 💡 Explanation:

What's happening in the first four examples? Here's a small table to understand addition in JavaScript:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

What about other examples? A `ToPrimitive` and `ToString` methods are being implicitly called for `[]` and `{}` before addition. Read more about evaluation process in the specification:

- [**12.8.3** The Addition Operator (`+`)](https://www.ecma-international.org/ecma-262/#sec-addition-operator-plus)
- [**7.1.1** ToPrimitive(`input` [,`PreferredType`])](https://www.ecma-international.org/ecma-262/#sec-toprimitive)
- [**7.1.12** ToString(`argument`)](https://www.ecma-international.org/ecma-262/#sec-tostring)

Notably, `{} + []` here is the exception. The reason why it differs from `[] + {}` is that, without parenthesis, it is interpreted as a code block and then a unary +, converting `[]` into a number. It sees the following:

```js
{
  // a code block here
}
+[]; // -> 0
```

To get the same output as `[] + {}` we can wrap it in parenthesis.

```js
({} + []); // -> [object Object]
```

## Addition of RegExps

Did you know you can add numbers like this?

```js
// Patch a toString method
RegExp.prototype.toString =
  function() {
    return this.source;
  } /
  7 /
  -/5/; // -> 2
```

### 💡 Explanation:

- [**21.2.5.10** get RegExp.prototype.source](https://www.ecma-international.org/ecma-262/#sec-get-regexp.prototype.source)

## Strings aren't instances of `String`

```js
"str"; // -> 'str'
typeof "str"; // -> 'string'
"str" instanceof String; // -> false
```

### 💡 Explanation:

The `String` constructor returns a string:

```js
typeof String("str"); // -> 'string'
String("str"); // -> 'str'
String("str") == "str"; // -> true
```

Let's try with a `new`:

```js
new String("str") == "str"; // -> true
typeof new String("str"); // -> 'object'
```

Object? What's that?

```js
new String("str"); // -> [String: 'str']
```

More information about the String constructor in the specification:

- [**21.1.1** The String Constructor](https://www.ecma-international.org/ecma-262/#sec-string-constructor)

## Calling functions with backticks

Let's declare a function which logs all params into the console:

```js
function f(...args) {
  return args;
}
```

No doubt, you know you can call this function like this:

```js
f(1, 2, 3); // -> [ 1, 2, 3 ]
```

But did you know you can call any function with backticks?

```js
f`true is ${true}, false is ${false}, array is ${[1, 2, 3]}`;
// -> [ [ 'true is ', ', false is ', ', array is ', '' ],
// ->   true,
// ->   false,
// ->   [ 1, 2, 3 ] ]
```

### 💡 Explanation:

Well, this is not magic at all if you're familiar with _Tagged template literals_. In the example above, `f` function is a tag for template literal. Tags before template literal allow you to parse template literals with a function. The first argument of a tag function contains an array of string values. The remaining arguments are related to the expressions. Example:

```js
function template(strings, ...keys) {
  // do something with strings and keys…
}
```

This is the [magic behind](http://mxstbr.blog/2016/11/styled-components-magic-explained/) famous library called [💅 styled-components](https://www.styled-components.com/), which is popular in the React community.

Link to the specification:

- [**12.3.7** Tagged Templates](https://www.ecma-international.org/ecma-262/#sec-tagged-templates)

## Call call call

> Found by [@cramforce](http://twitter.com/cramforce)

```js
console.log.call.call.call.call.call.apply(a => a, [1, 2]);
```

### 💡 Explanation:

Attention, it could break your mind! Try to reproduce this code in your head: we're applying the `call` method using the `apply` method. Read more:

- [**19.2.3.3** Function.prototype.call(`thisArg`, ...`args`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.call)
- [**19.2.3.1 ** Function.prototype.apply(`thisArg`, `argArray`)](https://www.ecma-international.org/ecma-262/#sec-function.prototype.apply)

## A `constructor` property

```js
const c = "constructor";
c[c][c]('console.log("WTF?")')(); // > WTF?
```

### 💡 Explanation:

Let's consider this example step-by-step:

```js
// Declare a new constant which is a string 'constructor'
const c = "constructor";

// c is a string
c; // -> 'constructor'

// Getting a constructor of string
c[c]; // -> [Function: String]

// Getting a constructor of constructor
c[c][c]; // -> [Function: Function]

// Call the Function constructor and pass
// the body of new function as an argument
c[c][c]('console.log("WTF?")'); // -> [Function: anonymous]

// And then call this anonymous function
// The result is console-logging a string 'WTF?'
c[c][c]('console.log("WTF?")')(); // > WTF?
```

An `Object.prototype.constructor` returns a reference to the `Object` constructor function that created the instance object. In case with strings it is `String`, in case with numbers it is `Number` and so on.

- [`Object.prototype.constructor`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor) at MDN
- [**19.1.3.1** Object.prototype.constructor](https://www.ecma-international.org/ecma-262/#sec-object.prototype.constructor)

## Object as a key of object's property

```js
{ [{}]: {} } // -> { '[object Object]': {} }
```

### 💡 Explanation:

Why does this work so? Here we're using a _Computed property name_. When you pass an object between those brackets, it coerces object to a string, so we get the property key `'[object Object]'` and the value `{}`.

We can make "brackets hell" like this:

```js
({ [{}]: { [{}]: {} } }[{}][{}]); // -> {}

// structure:
// {
//   '[object Object]': {
//     '[object Object]': {}
//   }
// }
```

Read more about object literals here:

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN
- [**12.2.6** Object Initializer](http://www.ecma-international.org/ecma-262/6.0/#sec-object-initializer)

## Accessing prototypes with `__proto__`

As we know, primitives don't have prototypes. However, if we try to get a value of `__proto__` for primitives, we would get this:

```js
(1).__proto__.__proto__.__proto__; // -> null
```

### 💡 Explanation:

This happens because when something doesn't have a prototype, it will be wrapped into a wrapper object using the `ToObject` method. So, step-by-step:

```js
(1).__proto__; // -> [Number: 0]
(1).__proto__.__proto__; // -> {}
(1).__proto__.__proto__.__proto__; // -> null
```

Here is more information about `__proto__`:

- [**B.2.2.1** Object.prototype.**proto**](https://www.ecma-international.org/ecma-262/#sec-object.prototype.__proto__)
- [**7.1.13** ToObject(`argument`)](https://www.ecma-international.org/ecma-262/#sec-toobject)

## `` `${{Object}}` ``

What is the result of the expression below?

```js
`${{ Object }}`;
```

The answer is:

```js
// -> '[object Object]'
```

### 💡 Explanation:

We defined an object with a property `Object` using _Shorthand property notation_:

```js
{
  Object: Object;
}
```

Then we've passed this object to the template literal, so the `toString` method calls for that object. That's why we get the string `'[object Object]'`.

- [**12.2.9** Template Literals](https://www.ecma-international.org/ecma-262/#sec-template-literals)
- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Destructuring with default values

Consider this example:

```js
let x,
  { x: y = 1 } = { x };
y;
```

The example above is a great task for an interview. What the value of `y`? The answer is:

```js
// -> 1
```

### 💡 Explanation:

```js
let x,
  { x: y = 1 } = { x };
y;
//  ↑       ↑           ↑    ↑
//  1       3           2    4
```

With the example above:

1. We declare `x` with no value, so it's `undefined`.
2. Then we pack the value of `x` into the object property `x`.
3. Then we extract the value of `x` using destructuring and want to assign it to `y`. If the value is not defined, then we're going to use `1` as the default value.
4. Return the value of `y`.

- [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) at MDN

## Dots and spreading

Interesting examples could be composed with spreading of arrays. Consider this:

```js
[...[..."..."]].length; // -> 3
```

### 💡 Explanation:

Why `3`? When we use the [spread operator](http://www.ecma-international.org/ecma-262/6.0/#sec-array-initializer), the `@@iterator` method is called, and the returned iterator is used to obtain the values to be iterated. The default iterator for string spreads a string into characters. After spreading, we pack these characters into an array. Then we spread this array again and pack it back to an array.

A `'...'` string consists with three `.` characters, so the length of resulting array is `3`.

Now, step-by-step:

```js
[...'...']             // -> [ '.', '.', '.' ]
[...[...'...']]        // -> [ '.', '.', '.' ]
[...[...'...']].length // -> 3
```

Obviously, we can spread and wrap the elements of an array as many times as we want:

```js
[...'...']                 // -> [ '.', '.', '.' ]
[...[...'...']]            // -> [ '.', '.', '.' ]
[...[...[...'...']]]       // -> [ '.', '.', '.' ]
[...[...[...[...'...']]]]  // -> [ '.', '.', '.' ]
// and so on …
```

## Labels

Not many programmers know about labels in JavaScript. They are kind of interesting:

```js
foo: {
  console.log("first");
  break foo;
  console.log("second");
}

// > first
// -> undefined
```

### 💡 Explanation:

The labeled statement is used with `break` or `continue` statements. You can use a label to identify a loop, and then use the `break` or `continue` statements to indicate whether a program should interrupt the loop or continue its execution.

In the example above, we identify a label `foo`. After that `console.log('first');` executes and then we interrupt the execution.

Read more about labels in JavaScript:

- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## Nested labels

```js
a: b: c: d: e: f: g: 1, 2, 3, 4, 5; // -> 5
```

### 💡 Explanation:

Similar to previous examples, follow these links:

- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)
- [**13.13** Labelled Statements](https://tc39.github.io/ecma262/#sec-labelled-statements)
- [Labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) at MDN

## Insidious `try..catch`

What will this expression return? `2` or `3`?

```js
(() => {
  try {
    return 2;
  } finally {
    return 3;
  }
})();
```

The answer is `3`. Surprised?

### 💡 Explanation:

- [**13.15** The `try` Statement](https://www.ecma-international.org/ecma-262/#sec-try-statement)

## Is this multiple inheritance?

Take a look at the example below:

```js
new class F extends (String, Array) {}(); // -> F []
```

Is this a multiple inheritance? Nope.

### 💡 Explanation:

The interesting part is the value of the `extends` clause (`(String, Array)`). The grouping operator always returns its last argument, so `(String, Array)` is actually just `Array`. That means we've just created a class which extends `Array`.

- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)
- [**12.16** Comma Operator (`,`)](https://www.ecma-international.org/ecma-262/#sec-comma-operator)

## A generator which yields itself

Consider this example of a generator which yields itself:

```js
(function* f() {
  yield f;
})().next();
// -> { value: [GeneratorFunction: f], done: false }
```

As you can see, the returned value is an object with its `value` equal to `f`. In that case, we can do something like this:

```js
(function* f() {
  yield f;
})()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()(
    // -> { value: [GeneratorFunction: f], done: false }

    // and again
    function* f() {
      yield f;
    }
  )()
  .next()
  .value()
  .next()
  .value()
  .next()
  .value()
  .next();
// -> { value: [GeneratorFunction: f], done: false }

// and so on
// …
```

### 💡 Explanation:

To understand why this works that way, read these sections of the specification:

- [**25** Control Abstraction Objects](https://www.ecma-international.org/ecma-262/#sec-control-abstraction-objects)
- [**25.3** Generator Objects](https://www.ecma-international.org/ecma-262/#sec-generator-objects)

## A class of class

Consider this obfuscated syntax playing:

```js
typeof new class {
  class() {}
}(); // -> 'object'
```

It seems like we're declaring a class inside of class. Should be an error, however, we get the string `'object'`.

### 💡 Explanation:

Since ECMAScript 5 era, _keywords_ are allowed as _property names_. So think about it as this simple object example:

```js
const foo = {
  class: function() {}
};
```

And ES6 standardized shorthand method definitions. Also, classes can be anonymous. So if we drop `: function` part, we're going to get:

```js
class {
  class() {}
}
```

The result of a default class is always a simple object. And its typeof should return `'object'`.

Read more here:

- [**14.3** Method Definitions](https://www.ecma-international.org/ecma-262/#sec-method-definitions)
- [**14.5** Class Definitions](https://www.ecma-international.org/ecma-262/#sec-class-definitions)

## Non-coercible objects

With well-known symbols, there's a way to get rid of type coercion. Take a look:

```js
function nonCoercible(val) {
  if (val == null) {
    throw TypeError("nonCoercible should not be called with null or undefined");
  }

  const res = Object(val);

  res[Symbol.toPrimitive] = () => {
    throw TypeError("Trying to coerce non-coercible object");
  };

  return res;
}
```

Now we can use this like this:

```js
// objects
const foo = nonCoercible({ foo: "foo" });

foo * 10; // -> TypeError: Trying to coerce non-coercible object
foo + "evil"; // -> TypeError: Trying to coerce non-coercible object

// strings
const bar = nonCoercible("bar");

bar + "1"; // -> TypeError: Trying to coerce non-coercible object
bar.toString() + 1; // -> bar1
bar === "bar"; // -> false
bar.toString() === "bar"; // -> true
bar == "bar"; // -> TypeError: Trying to coerce non-coercible object

// numbers
const baz = nonCoercible(1);

baz == 1; // -> TypeError: Trying to coerce non-coercible object
baz === 1; // -> false
baz.valueOf() === 1; // -> true
```

### 💡 Explanation:

- [A gist by Sergey Rubanov](https://gist.github.com/chicoxyzzy/5dd24608e886adf5444499896dff1197)
- [**6.1.5.1** Well-Known Symbols](https://www.ecma-international.org/ecma-262/#sec-well-known-symbols)

## Tricky arrow functions

Consider the example below:

```js
let f = () => 10;
f(); // -> 10
```

Okay, fine, but what about this:

```js
let f = () => {};
f(); // -> undefined
```

### 💡 Explanation:

You might expect `{}` instead of `undefined`. This is because the curly braces are part of the syntax of the arrow functions, so `f` will return undefined. It is however possible to return the `{}` object directly from an arrow function, by enclosing the return value with brackets.

```js
let f = () => ({});
f(); // -> {}
```

## Arrow functions can not be a constructor

Consider the example below:

```js
let f = function() {
  this.a = 1;
};
new f(); // -> f { 'a': 1 }
```

Now, try do to the same with an arrow function:

```js
let f = () => {
  this.a = 1;
};
new f(); // -> TypeError: f is not a constructor
```

### 💡 Explanation:

Arrow functions cannot be used as constructors and will throw an error when used with `new`. Because they have a lexical `this`, and do not have a `prototype` property, so it would not make much sense.

## `arguments` and arrow functions

Consider the example below:

```js
let f = function() {
  return arguments;
};
f("a"); // -> { '0': 'a' }
```

Now, try do to the same with an arrow function:

```js
let f = () => arguments;
f("a"); // -> Uncaught ReferenceError: arguments is not defined
```

### 💡 Explanation:

Arrow functions are a lightweight version of regular functions with a focus on being short and lexical `this`. At the same time arrow functions do not provide a binding for the `arguments` object. As a valid alternative use the `rest parameters` to achieve the same result:

```js
let f = (...args) => args;
f("a");
```

- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) at MDN.

## Tricky return

`return` statement is also tricky. Consider this:

<!-- prettier-ignore-start -->
```js
(function() {
  return
  {
    b: 10;
  }
})(); // -> undefined
```
<!-- prettier-ignore-end -->

### 💡 Explanation:

`return` and the returned expression must be in the same line:

```js
(function() {
  return {
    b: 10
  };
})(); // -> { b: 10 }
```

This is because of a concept called Automatic Semicolon Insertion, which automagically inserts semicolons after most newlines. In the first example, there is a semicolon inserted between the `return` statement and the object literal, so the function returns `undefined` and the object literal is never evaluated.

- [**11.9.1** Rules of Automatic Semicolon Insertion](https://www.ecma-international.org/ecma-262/#sec-rules-of-automatic-semicolon-insertion)
- [**13.10** The `return` Statement](https://www.ecma-international.org/ecma-262/#sec-return-statement)

## Chaining assignments on object

```js
var foo = { n: 1 };
var bar = foo;

foo.x = foo = { n: 2 };

foo.x; // -> undefined
foo; // -> {n: 2}
bar; // -> {n: 1, x: {n: 2}}
```

From right to left, `{n: 2}` is assigned to foo, and the result of this assignment `{n: 2}` is assigned to foo.x, that's why bar is `{n: 1, x: {n: 2}}` as bar is a reference to foo. But why foo.x is undefined while bar.x is not ?

### 💡 Explanation:

Foo and bar references the same object `{n: 1}`, and lvalues are resolved before assignations. `foo = {n: 2}` is creating a new object, and so foo is updated to reference that new object. The trick here is foo in `foo.x = ...` as a lvalue was resolved beforehand and still reference the old `foo = {n: 1}` object and update it by adding the x value. After that chain assignments, bar still reference the old foo object, but foo reference the new `{n: 2}` object, where x is not existing.

It's equivalent to:

```js
var foo = { n: 1 };
var bar = foo;

foo = { n: 2 }; // -> {n: 2}
bar.x = foo; // -> {n: 1, x: {n: 2}}
// bar.x point to the address of the new foo object
// it's not equivalent to: bar.x = {n: 2}
```

## Accessing object properties with arrays

```js
var obj = { property: 1 };
var array = ["property"];

obj[array]; // -> 1

// this also works with nested arrays
var nestedArray = [[[[[[[[[["property"]]]]]]]]]];
obj[nestedArray]; // -> 1
```

What about pseudo-multidimensional arrays?

```js
var map = {};
var x = 1;
var y = 2;
var z = 3;

map[[x, y, z]] = true;
map[[x + 10, y, z]] = true;

map["1,2,3"]; // -> true
map["11,2,3"]; // -> true
```

### 💡 Explanation:

The brackets `[]` operator converts the passed expression using `toString`. Converting a one-element array to a string is akin to converting the contained element to the string:

```js
["property"].toString(); // -> 'property'
```

## `Number.toFixed()` display different numbers

`Number.toFixed()` can behave a bit strange in different browsers. Check out this example:

```js
(0.7875).toFixed(3);
// Firefox: -> 0.787
// Chrome: -> 0.787
// IE11: -> 0.788
(0.7876).toFixed(3);
// Firefox: -> 0.788
// Chrome: -> 0.788
// IE11: -> 0.788
```

### 💡 Explanation:

While your first instinct may be that IE11 is correct and Firefox/Chrome are wrong, the reality is that Firefox/Chrome are more directly obeying standards for numbers (IEEE-754 Floating Point), while IE11 is minutely disobeying them in (what is probably) an effort to give clearer results.

You can see why this occurs with a few quick tests:

```js
// Confirm the odd result of rounding a 5 down
(0.7875).toFixed(3); // -> 0.787
// It looks like it's just a 5 when you expand to the
// limits of 64-bit (double-precision) float accuracy
(0.7875).toFixed(14); // -> 0.78750000000000
// But what if you go beyond the limit?
(0.7875).toFixed(20); // -> 0.78749999999999997780
```

Floating point numbers are not stored as a list of decimal digits internally, but through a more complicated methodology that produces tiny inaccuracies that are usually rounded away by toString and similar calls, but are actually present internally.

In this case, that "5" on the end was actually an extremely tiny fraction below a true 5. Rounding it at any reasonable length will render it as a 5... but it is actually not a 5 internally.

IE11, however, will report the value input with only zeros appended to the end even in the toFixed(20) case, as it seems to be forcibly rounding the value to reduce the troubles from hardware limits.

See for reference `NOTE 2` on the ECMA-262 definition for `toFixed`.

- [**20.1.3.3** Number.prototype.toFixed (`fractionDigits`)](https://www.ecma-international.org/ecma-262//#sec-number.prototype.tofixed)

## `Math.max()` less than `Math.min()`

I find this example hilarious:

```js
Math.min() > Math.max(); // -> true
Math.min() < Math.max(); // -> false
```

### 💡 Explanation:

This is a simple one. Let's consider each part of this expression separately:

```js
Math.min(); // -> Infinity
Math.max(); // -> -Infinity
Infinity > -Infinity; // -> true
```

Why so? Well, `Math.max()` is not the same thing as `Number.MAX_VALUE`. It does not return the largest possible number.

`Math.max` takes arguments, tries to convert the to numbers, compares each one and then returns the largest remaining. If no arguments are given, the result is −∞. If any value is `NaN`, the result is `NaN`.

The opposite is happening for `Math.min`. `Math.min` returns ∞, if no arguments are given.

- [**15.8.2.11** Math.max](https://262.ecma-international.org/5.1/#sec-15.8.2.11)
- [**15.8.2.11** Math.min](https://262.ecma-international.org/5.1/#sec-15.8.2.12)
- [Why is `Math.max()` less than `Math.min()`?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min) by Charlie Harvey

## Comparing `null` to `0`

The following expressions seem to introduce a contradiction:

```js
null == 0; // -> false
null > 0; // -> false
null >= 0; // -> true
```

How can `null` be neither equal to nor greater than `0`, if `null >= 0` is actually `true`? (This also works with less than in the same way.)

### 💡 Explanation:

The way these three expressions are evaluated are all different and are responsible for producing this unexpected behavior.

First, the abstract equality comparison `null == 0`. Normally, if this operator can't compare the values on either side properly, it converts both to numbers and compares the numbers. Then, you might expect the following behavior:

```js
// This is not what happens
(null == 0 + null) == +0;
0 == 0;
true;
```

However, according to a close reading of the spec, the number conversion doesn't actually happen on a side that is `null` or `undefined`. Therefore, if you have `null` on one side of the equal sign, the other side must be `null` or `undefined` for the expression to return `true`. Since this is not the case, `false` is returned.

Next, the relational comparison `null > 0`. The algorithm here, unlike that of the abstract equality operator, _will_ convert `null` to a number. Therefore, we get this behavior:

```js
null > 0
+null = +0
0 > 0
false
```

Finally, the relational comparison `null >= 0`. You could argue that this expression should be the result of `null > 0 || null == 0`; if this were the case, then the above results would mean that this would also be `false`. However, the `>=` operator in fact works in a very different way, which is basically to take the opposite of the `<` operator. Because our example with the greater than operator above also holds for the less than operator, that means this expression is actually evaluated like so:

```js
null >= 0;
!(null < 0);
!(+null < +0);
!(0 < 0);
!false;
true;
```

- [**7.2.12** Abstract Relational Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-relational-comparison)
- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)
- [An in-depth explanation](https://blog.campvanilla.com/javascript-the-curious-case-of-null-0-7b131644e274)

## Same variable redeclaration

JS allows to redeclare variables:

```js
a;
a;
// This is also valid
a, a;
```

Works also in strict mode:

```js
var a, a, a;
var a;
var a;
```

### 💡 Explanation:

All definitions are merged into one definition.

- [**13.3.2** Variable Statement](https://www.ecma-international.org/ecma-262/#sec-variable-statement)

## Default behavior Array.prototype.sort()

Imagine that you need to sort an array of numbers.

```js
[10, 1, 3].sort(); // -> [ 1, 10, 3 ]
```

### 💡 Explanation:

The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code units values.

- [**22.1.3.25** Array.prototype.sort ( comparefn )](https://www.ecma-international.org/ecma-262/#sec-array.prototype.sort)

### Hint

Pass `compareFn` if you try to sort anything but string.

```js
[10, 1, 3].sort((a, b) => a - b); // -> [ 1, 3, 10 ]
```

## resolve() won't return Promise instance

```js
const theObject = {
  a: 7
};
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // Promise instance object

thePromise.then(value => {
  console.log(value === theObject); // > true
  console.log(value); // > { a: 7 }
});
```

The `value` which is resolved from `thePromise` is exactly `theObject`.

How about input another `Promise` into the `resolve` function?

```js
const theObject = new Promise((resolve, reject) => {
  resolve(7);
}); // Promise instance object
const thePromise = new Promise((resolve, reject) => {
  resolve(theObject);
}); // Promise instance object

thePromise.then(value => {
  console.log(value === theObject); // > false
  console.log(value); // > 7
});
```

### 💡 Explanation:

> This function flattens nested layers of promise-like objects (e.g. a promise that resolves to a promise that resolves to something) into a single layer.

- [Promise.resolve() on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

The specification is [ECMAScript 25.6.1.3.2 Promise Resolve Functions](https://tc39.es/ecma262/#sec-promise-resolve-functions). But it is not quite human-friendly.

## `{}{}` is undefined

Write them in the console. They will return the value defined in the last object.

```js
{}{}; // -> undefined
{}{}{}; // -> undefined
{}{}{}{}; // -> undefined
{foo: 'bar'}{}; // -> 'bar'
{}{foo: 'bar'}; // -> 'bar'
{}{foo: 'bar'}{}; // -> 'bar'
{a: 'b'}{c:' d'}{}; // -> 'd'
{a: 'b', c: 'd'}{}; // > SyntaxError: Unexpected token ':'
({}{}); // > SyntaxError: Unexpected token '{'
```

### 💡 Explanation:

When inspecting each `{}`, they returns undefined. If you inspect `{foo: 'bar'}{}`, you will find `{foo: 'bar'}` is `'bar'`.

There are two meanings for `{}`: an object or a block. For example, the `{}` in `() => {}` means block. So we need to use `() => ({})` to return an object.

Let's use `{foo: 'bar'}` as a block. Write this snippet in your console:

```js
if (true) {
  foo: "bar";
} // -> 'bar'
```

Surprisingly, it behaviors the same! You can guess here that `{foo: 'bar'}{}` is a block.

## `arguments` binding

Consider this function:

```js
function a(x) {
  arguments[0] = "hello";
  console.log(x);
}

a(); // > undefined
a(1); // > "hello"
```

### 💡 Explanation:

`arguments` is an Array-like object that contains the values of the arguments passed to that function. When no arguments are passed, then there's no `x` to override.

- [The arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) on MDN

## An `alert` from hell

This on is literally from hell:

```js
[666]["\155\141\160"]["\143\157\156\163\164\162\165\143\164\157\162"](
  "\141\154\145\162\164(666)"
)(666); // alert(666)
```

### 💡 Explanation:

This one is based on octal escape sequences and multiple strings.

Any character with a character code lower than 256 (i.e. any character in the extended ASCII range) can be escaped using its octal-encoded character code, prefixed with `\`. An example above is basically and `alert` ecoded by octal escape sequances.

- [Martin Kleppe tweet about it](https://twitter.com/aemkei/status/897172907222237185)
- [JavaScript character escape sequences](https://mathiasbynens.be/notes/javascript-escapes#octal)
- [Multi-Line JavaScript Strings](https://davidwalsh.name/multiline-javascript-strings)

## An infinite timeout

Guess what would happen if we set an infinite timeout?

```js
setTimeout(() => console.log("called"), Infinity); // -> <timeoutId>
// > 'called'
```

It will executed immediately instead of infinity delay.

### 💡 Explanation:

Usually, runtime stores the delay as a 32-bit signed integer internally. This causes an integer overflow, resulting in the timeout being executed immediately.

For example, in Node.js we will get this warning:

```
(node:1731) TimeoutOverflowWarning: Infinity does not fit into a 32-bit signed integer.
Timeout duration was set to 1.
(Use `node --trace-warnings ...` to show where the warning was created)
```

- [WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout) on MDN
- [Node.js Documentation on Timers](https://nodejs.org/api/timers.html#timers_settimeout_callback_delay_args)
- [Timers](https://www.w3.org/TR/2011/WD-html5-20110525/timers.html) on W3C

## A `setTimeout` object

Guess what would happen if we set an callback that's not a function to `setTimeout`?

```js
setTimeout(123, 100); // -> <timeoutId>
// > 'called'
```

This is fine.

```js
setTimeout('{a: 1}', 100); // -> <timeoutId>
// > 'called'
```

This is also fine.

```js
setTimeout({a: 1}, 100); // -> <timeoutId>
// > 'Uncaught SyntaxError: Unexpected identifier               setTimeout (async) (anonymous) @ VM__:1'
```

This throws an **SyntaxError**.

Note that this can easily happen if your function returns an object and you call it here instead of passing it! What if the content - policy is set to `self`?

```js
setTimeout(123, 100); // -> <timeoutId>
// > console.error("[Report Only] Refused to evaluate a string as JavaScript because 'unsafe-eval' is not an allowed source of script in the following Content Security Policy directive: "script-src 'report-sample' 'self' ")
```

The console refuses to run it at all!

### 💡 Explanation:

`WindowOrWorkerGlobalScope.setTimeout()` can be called with `code` as first argument, which will be passed on to `eval`, which is bad. Eval will coerce her input to String, and evaluate what is produced, so Objects becomes `'[object Object]'` which has hmmm ... an `'Unexpected identifier'`!

- [eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) on MDN (don't use this)
- [WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout) on MDN
- [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)
- [Timers](https://www.w3.org/TR/2011/WD-html5-20110525/timers.html) on W3C

## Double dot

Let's try to coerce a number to a string:

```js
27.toString() // > Uncaught SyntaxError: Invalid or unexpected token
```

Maybe we should try with two dots?

```js
27..toString(); // -> '27'
```

But why doesn't first example work?

### 💡 Explanation:

It's just a language grammar limitation.

The `.` character presents an ambiguity. It can be understood to be the member operator, or a decimal, depending on its placement.

The specification's interpretation of the `.` character in that particular position is that it will be a decimal. This is defined by the numeric literal syntax of ECMAScript.

You must always use parenthesis or an addition dot to make such expression valid.

```js
(27).toString(); // -> '27'
// or
27..toString(); // -> '27'
```

- [Usage of toString in JavaScript](https://stackoverflow.com/questions/6853865/usage-of-tostring-in-javascript/6853910#6853910) on StackOverflow
- [Why does 10..toString() work, but 10.toString() does not?](https://stackoverflow.com/questions/13149282/why-does-10-tostring-work-but-10-tostring-does-not/13149301#13149301)

## Extra Newness

I present this as an oddity for your amusement.

```js
class Foo extends Function {
  constructor(val) {
    super();
    this.prototype.val = val;
  }
}

new new Foo(":D")().val; // -> ':D'
```

### 💡 Explanation:

Constructors in JavaScript are just functions with some special treatment. By extending Function using the class syntax you create a class that, when instantiated, is now a function, which you can then additionally instantiate.

While not exhaustively tested, I believe the last statement can be analyzed thus:

```js
new new Foo(":D")().val(new newFooInstance()).val;
veryNewFooInstance.val;
// -> ':D'
```

As a tiny addendum, doing `new Function('return "bar";')` of course creates a function with the body `return "bar";`. Since `super()` in the constructor of our `Foo` class is calling `Function`'s constructor, it should come as no surprise now to see that we can additionally manipulate things in there.

```js
class Foo extends Function {
  constructor(val) {
    super(`
      this.val = arguments[0];
    `);
    this.prototype.val = val;
  }
}

var foo = new new Foo(":D")("D:");
foo.val; // -> 'D:'
delete foo.val; // remove the instance prop 'val', deferring back to the prototype's 'val'.
foo.val; // -> ':D'
```

- [Class Extends Function: Extra Newness](https://github.com/denysdovhan/wtfjs/issues/78)

## Why you should use semicolons

Writing some standard JavaScript… and then BOOM!

```js
class SomeClass {
  ["array"] = []
  ["string"] = "str"
}

new SomeClass().array; // -> 'str'
```

What the …?

### 💡 Explanation:

Once again, this is all thanks to the Automatic Semicolon Insertion.

An example above is basically the same as:

```js
class SomeClass {
  ["array"] = ([]["string"] = "str");
}
```

You basically assign a string `str` into an `array` property.

- [An original tweet with an example](https://twitter.com/SeaRyanC/status/1148726605222535168) by Ryan Cavanaugh
- [TC39 meeting when they debated about it](https://github.com/tc39/notes/blob/master/meetings/2017-09/sept-26.md)

## Split a string by a space

Have you ever tried to split a string by a space?

```js
"".split(""); // -> []
// but…
"".split(" "); // -> [""]
```

### 💡 Explanation:

This is expected behaviour. Its responsibility is to divide the input string every time a separator occurs in that input string. When you pass in an empty string it'll never find a separator and thus return that string.

Let's quote the specification:

> The substrings are determined by searching from left to right for occurrences of `separator`; these occurrences are not part of any String in the returned array, but serve to divide up the String value.

- [**22.1.3.21** String.prototype.split](https://tc39.es/ecma262/#sec-string.prototype.split)
- [An original tween with an example](https://twitter.com/SeaRyanC/status/1331656278104440833) by Ryan Cavanaugh
- [A tween with an explanation](https://twitter.com/kl13nt/status/1331742810932916227?s=20) by Nabil Tharwat

## A stringified string

This caused a bug that I've been solving for a few days:

```js
JSON.stringify("production") === "production"; // -> false
```

### 💡 Explanation:

Let's see what `JSON.stringify` is returning:

```js
JSON.stringify("production"); // -> '"production"'
```

It is actually a stringified string, so it's true:

```js
'"production"' === "production"; // -> false
```

- [ECMA-404 The JSON Data Interchange Standard.](https://www.json.org/json-en.html)

## Non-strict comparison of a number to `true`

```js
1 == true; // -> true
// but…
Boolean(1.1); // -> true
1.1 == true; // -> false
```

### 💡 Explanation:

According to the specification:

> The comparison x == y, where x and y are values, produces true or false. Such a comparison is performed as follows:
>
> 4. If `Type(x)` is Number and `Type(y)` is String, return the result of the comparison `x == ! ToNumber(y)`.

So this comparison is performed like this:

```js
1 == true;
1 == Number(true);
1 == 1; // -> true
// but…
1.1 == true;
1.1 == Number(true);
1.1 == 1; // -> false
```

- [**7.2.15** Abstract Equality Comparison](https://262.ecma-international.org/11.0/index.html#sec-abstract-equality-comparison)

# 📚 Other resources

- [wtfjs.com](http://wtfjs.com/) — a collection of those very special irregularities, inconsistencies and just plain painfully unintuitive moments for the language of the web.
- [Wat](https://www.destroyallsoftware.com/talks/wat) — A lightning talk by Gary Bernhardt from CodeMash 2012
- [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU) — Kyle Simpsons talk for Forward 2 attempts to “pull out the crazy” from JavaScript. He wants to help you produce cleaner, more elegant, more readable code, then inspire people to contribute to the open source community.
- [Zeros in JavaScript](http://zero.milosz.ca/) — a comparison table of `==`, `===`, `+` and `*` in JavaScript.

# 🤝 Supporting

Hi! I work on this project in my spare time, in addition to my primary job. I hope you enjoy reading it. If you do, please, consider supporting me 🙏.

Every single donation is important. Your donation is gonna make a clear statement: My work is valued.

**🙏 Thank you for your support! 🙏**

| Service          |                     Link                     |                                                                   Action                                                                   |
| ---------------- | :------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| **Patreon**      |        [Become a patron][patreon-url]        | <a href="https://patreon.com/denysdovhan"><img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="120px"></a> |
| **BuyMeACoffee** |     [Buy me a cup of ☕️ or 🥤][bmc-url]     |    <a href="https://buymeacoffee.com/denysdovhan"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" width="120px"></a>     |
| **Bitcoin**      |     `1EJsKs6rPsqa7QLoVLpe3wgcdL9Q8WmDxE`     |      <img src="https://user-images.githubusercontent.com/3459374/107130426-0ae4f800-68d6-11eb-9b86-15bf33467615.png" width="120px"/>       |
| **Ethereum**     | `0x6aF39C917359897ae6969Ad682C14110afe1a0a1` |      <img src="https://user-images.githubusercontent.com/3459374/107130370-55b24000-68d5-11eb-93f5-075355c7fcd4.png" width="120px"/>       |

> **⚠️ Note:** I live in Ukraine and services like PayPal and Stripe don't work with Ukrainian bank accounts. This means there's no way for me to set up GitHub Sponsors, OpenCollective, or services relied on them. Sorry, those are the only ways you can support me for now.

# 🎓 License

[![CC 4.0][license-image]][license-url]

&copy; [Denys Dovhan](http://denysdovhan.com)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square
[npm-url]: https://npmjs.org/package/wtfjs
[npm-image]: https://img.shields.io/npm/v/wtfjs.svg?style=flat-square
[patreon-url]: https://patreon.com/denysdovhan
[patreon-image]: https://img.shields.io/badge/support-patreon-F96854.svg?style=flat-square
[bmc-url]: https://patreon.com/denysdovhan
[bmc-image]: https://img.shields.io/badge/support-buymeacoffee-222222.svg?style=flat-square
```

## File: `wtfjs.js`
```javascript
#!/usr/bin/env node

const fs = require("fs");
const obj = require("through2").obj;
const pager = require("default-pager");
const msee = require("msee");
const join = require("path").join;
const boxen = require("boxen");
const chalk = require("chalk");
const updateNotifier = require("update-notifier");
const pkg = require("./package.json");
const meow = require("meow");

const cli = meow(
  [
    "Usage",
    "  wtfjs",
    "",
    "Options",
    "  --lang, -l  Translation language",
    "",
    "Examples",
    "  wtfjs",
    "  wtfjs --lang pt-br",
  ],
  {
    flags: {
      lang: {
        type: "string",
        alias: "l",
        default: "",
      },
    },
  }
);

const boxenOpts = {
  borderColor: "yellow",
  margin: {
    bottom: 1,
  },
  padding: {
    right: 1,
    left: 1,
  },
};

const mseeOpts = {
  paragraphEnd: "\n\n",
};

const notifier = updateNotifier({ pkg });

process.env.PAGER = process.env.PAGER || "less";
process.env.LESS = process.env.LESS || "FRX";

const lang = (cli.flags.lang || "")
  .toLowerCase()
  .split("-")
  .map((l, i) => (i === 0 ? l : l.toUpperCase()))
  .join("-");

const translation = join(
  __dirname,
  !lang ? "./README.md" : `./README-${lang}.md`
);

fs.stat(translation, function (err, stats) {
  if (err) {
    console.log("The %s translation does not exist", chalk.bold(lang));
    return;
  }

  fs.createReadStream(translation)
    .pipe(
      obj(function (chunk, enc, cb) {
        const message = [];

        if (notifier.update) {
          message.push(
            `Update available: {green.bold ${notifier.update.latest}} {dim current: ${notifier.update.current}}`
          );
          message.push(`Run {blue npm install -g ${pkg.name}} to update.`);
          this.push(boxen(message.join("\n"), boxenOpts));
        }

        this.push(msee.parse(chunk.toString(), mseeOpts));
        cb();
      })
    )
    .pipe(pager());
});
```

