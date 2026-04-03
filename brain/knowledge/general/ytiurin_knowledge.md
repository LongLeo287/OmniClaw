---
id: ytiurin-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.693393
---

# KNOWLEDGE EXTRACT: ytiurin
> **Extracted on:** 2026-03-30 18:01:26
> **Source:** ytiurin

---

## File: `hyphen.md`
```markdown
# 📦 ytiurin/hyphen [🔖 PENDING/APPROVE]
🔗 https://github.com/ytiurin/hyphen
🌐 https://ytiurin.github.io/hyphen/

## Meta
- **Stars:** ⭐ 233 | **Forks:** 🍴 25
- **Language:** JavaScript | **License:** ISC
- **Last updated:** 2026-03-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Text hyphenation in Javascript.

## README (trích đầu)
```
![Franklin M. Liang's hyphenation algorithm](https://ytiurin.github.io/hyphen/01.png)

[![npm version](https://badge.fury.io/js/hyphen.svg)](https://badge.fury.io/js/hyphen)<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-10-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

# hyphen

[Demo page](https://ytiurin.github.io/hyphen/)

This is a text hyphenation library, based on Franklin M. Liang's [hyphenation algorithm](https://tug.org/docs/liang/ "Frank Liang wrote his Stanford Ph.D. thesis on a hyphenation algorithm that is standard in TeX, and has been adapted to numerous languages."). In core of the algorithm lies a set of hyphenation patterns. They are extracted from hand-hyphenated dictionaries. Patterns for this library were taken from [ctan.org](https://ctan.org/ "The Comprehensive TEX Archive Network (CTAN) is the central place for all kinds of material around TEX.") and ported to Javascript.

```javascript
import { hyphenate } from "hyphen/en";

(async () => {
  const text = "A certain king had a beautiful garden";

  const result = await hyphenate(text);
  // result is "A cer\u00ADtain king had a beau\u00ADti\u00ADful garden"
})();
```

## Hyphenate HTML

Processor will automaticly skip HTML tags hyphenation.

```javascript
import { hyphenate } from "hyphen/en";

(async () => {
  const text = "<blockquote>A certain king had a beautiful garden</blockquote>";

  const result = await hyphenate(text);
  // result is "<blockquote>A cer\u00ADtain king had a beau\u00ADti\u00ADful garden</blockquote>"
})();
```

## Select language

To hypehante text in any other supported language, just change the `import` source. For example for German language, import a hyphenation function from a `"hyphen/de"` source.

```javascript
import { hyphenate } from "hyphen/de";

(async () => {
  const text = "Ein gewisser König hatte einen wunderschönen Garten";

  const result = await hyphenate(text);
  // result is "Ein ge\u00ADwis\u00ADser Kö\u00ADnig hat\u00ADte einen wun\u00ADder\u00ADschö\u00ADnen Gar\u00ADten"
})();
```

## Multilingual hyphenation

It is possible to use many langauges on the same page.

```javascript
import { hyphenate as hyphenateEn } from "hyphen/en";
import { hyphenate as hyphenateDe } from "hyphen/de";

(async () => {
  const english = "A certain king had a beautiful garden";

  const englishResult = await hyphenateEn(english);
  // result is "A cer\u00ADtain king had a beau\u00ADti\u00ADful garden"

  const deutch = "Ein gewisser König hatte einen wunderschönen Garten";

  const deutchResult = await hyphenateDe(deutch);
  // result is "Ein ge\u00ADwis\u00ADser Kö\u00ADnig hat\u00ADte einen wun\u00ADder\u00ADschö\u00ADnen Gar\u00ADten"
})();
```

## Sync version

Use a sync version when you need to write a synchronous code.

```javascript
import { hyphenateSync as hyphenate } from "hyphen/en";

const text = "A
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

