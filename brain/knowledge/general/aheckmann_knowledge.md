---
id: aheckmann-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:42.162702
---

# KNOWLEDGE EXTRACT: aheckmann
> **Extracted on:** 2026-03-30 17:29:05
> **Source:** aheckmann

---

## File: `gm.md`
```markdown
# 📦 aheckmann/gm [🔖 PENDING/APPROVE]
🔗 https://github.com/aheckmann/gm


## Meta
- **Stars:** ⭐ 6978 | **Forks:** 🍴 622
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GraphicsMagick for node

## README (trích đầu)
```
# 2025-02-24 This project is not maintained

Instead of using this project, execute the `gm` or `magick` binaries using
[`cross-spawn`](https://www.npmjs.com/package/cross-spawn) directly.

Nearly [15 years ago](https://github.com/aheckmann/gm/commit/defc7360d70d87f7a13da4f6e2ef0104594776b9) I started this project as part of my start up which I sold later that year (2010). Having not used this project in over a decade and with no contributors for years, it's time to officially sunset `gm`.

No further Issues will be addressed. No Pull Requests will be merged. No new commits or npm releases will be made.

---

😍 _Massive **thank you** to [everyone](https://github.com/aheckmann/gm/graphs/contributors) who contributed to this project over the years._ 😍

---

## I want to continue using gm. What do I do?

All past `gm` releases published to the npm registry will continue to be available for install. However, you should **prioritize moving off of this project to an alternative** because the risk of unpatched vulnerabilities in this project will continue to _increase_ over time. No new commits will land and no new releases will be published.

The most obvious alternative to `gm` I see is installing [cross-spawn](https://www.npmjs.com/package/cross-spawn) and executing the GraphicsMagick or ImageMagick binaries directly, after all, that's pretty much all this project did. There may be other `gm` alternatives on npm but I don't what they are offhand so you'll need to search for something suitable yourself.

---


# gm [![Build Status](https://travis-ci.org/aheckmann/gm.png?branch=master)](https://travis-ci.org/aheckmann/gm)  [![NPM Version](https://img.shields.io/npm/v/gm.svg?style=flat)](https://www.npmjs.org/package/gm)

GraphicsMagick and ImageMagick for node

## Bug Reports

When reporting bugs please include the version of graphicsmagick/imagemagick you're using (gm -version/convert -version) as well as the version of this module and copies of any images you're having problems with.

## Getting started
First download and install [GraphicsMagick](http://www.graphicsmagick.org/) or [ImageMagick](http://www.imagemagick.org/). In Mac OS X, you can simply use [Homebrew](http://mxcl.github.io/homebrew/) and do:

    brew install imagemagick
    brew install graphicsmagick

then either use npm:

    npm install gm

or clone the repo:

    git clone git://github.com/aheckmann/gm.git


## Use ImageMagick instead of gm

Subclass `gm` to enable [ImageMagick 7+](https://imagemagick.org/script/porting.php)

```js
const fs = require('fs')
const gm = require('gm').subClass({ imageMagick: '7+' });
```

Or, to enable ImageMagick legacy mode (for ImageMagick version < 7)

```js
const fs = require('fs')
const gm = require('gm').subClass({ imageMagick: true });
```

## Specify the executable path

Optionally specify the path to the executable.

```js
const fs = require('fs')
const gm = require('gm').subClass({
  appPath: String.raw`C:\Program Files\ImageMagick-7.1.0-Q1
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

