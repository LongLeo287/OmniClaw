---
id: csstools-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.021473
---

# KNOWLEDGE EXTRACT: csstools
> **Extracted on:** 2026-03-30 17:35:41
> **Source:** csstools

---

## File: `normalize.css.md`
```markdown
# 📦 csstools/normalize.css [🔖 PENDING/APPROVE]
🔗 https://github.com/csstools/normalize.css
🌐 https://csstools.github.io/normalize.css

## Meta
- **Stars:** ⭐ 650 | **Forks:** 🍴 66
- **Language:** HTML | **License:** CC0-1.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A cross-browser CSS foundation

## README (trích đầu)
```
# @csstools/normalize.css [<img src="https://csstools.github.io/normalize.css/logo.svg" alt="normalize" width="90" height="90" align="right">][@csstools/normalize.css]

[@csstools/normalize.css] is a CSS library that provides consistent,
cross-browser default styling of HTML elements.

## Usage

```html
<link href="https://unpkg.com/@csstools/normalize.css" rel="stylesheet" />
```

## Install

```sh
npm install @csstools/normalize.css --save
```

#### Webpack Usage

Import [@csstools/normalize.css] in CSS:

```css
@import '~@csstools/normalize.css';
```

Alternatively, import [@csstools/normalize.css] in JS:

```js
import '@csstools/normalize.css';
```

In `webpack.config.js`, use the appropriate loaders:

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      }
    ]
  }
}
```

**Download**

See https://csstools.github.io/normalize.css/latest/normalize.css

## What does it do?

* Normalizes styles for a wide range of elements.
* Corrects bugs and common browser inconsistencies.
* Explains what code does using detailed comments.

## Browser support

* Chrome (last 3)
* Edge (last 3)
* Firefox (last 3)
* Firefox ESR
* Opera (last 3)
* Safari (last 2)
* iOS Safari (last 2)

## Contributing

Please read the [contribution guidelines](CONTRIBUTING.md) in order to make the
contribution process easy and effective for everyone involved.

## Similar Projects

- [modern-normalize.css](https://github.com/sindresorhus/modern-normalize) - An
alternative to normalize.css, adhering to a minimal set of normalizations and
common developer expectations and preferences.
- [opinionate.css](https://github.com/adamgruber/opinionate.css) - A supplement
to normalize.css with opinionated rules.
- [remedy.css](https://github.com/mozdevs/cssremedy) - An alternative to
normalize.css, adhering to different common developer expectations and
preferences.
- [sanitize.css](https://github.com/csstools/sanitize.css) - An alternative to
normalize.css, adhering to common developer expectations and preferences.

## Differences from `necolas/normalize.css`

Nicolas Gallagher and I started writing normalize.css together. I named and
created the normalize.css repository with the help of Paul Irish and Ben Alman.
I transferred the repository to Nicolas, who turned it into a “household” CSS
library.

Later, I resumed authorship of normalize.css with Luciano Battagliero. Together,
we tagged, deprecated, and removed “opinionated” styles — styles developers
often prefer but which do not fix bugs or “normalize” browser differences.

Later, Nicolas resumed authorship and the issue of whether to include or omit
the opinionated styles forced us to split.

I continue working on the normalize.css project, currently under the “csstools”
tag. I hope one day our differences are resolved and the projects are one again.

## Acknowledgements

normalize.css is a project by [Jonathan Neal](https://github.com/jonathantneal),
co-
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `sanitize.css.md`
```markdown
# 📦 csstools/sanitize.css [🔖 PENDING/APPROVE]
🔗 https://github.com/csstools/sanitize.css
🌐 https://csstools.github.io/sanitize.css

## Meta
- **Stars:** ⭐ 5290 | **Forks:** 🍴 305
- **Language:** CSS | **License:** CC0-1.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A best-practices CSS foundation

## README (trích đầu)
```
# sanitize.css [<img src="https://csstools.github.io/sanitize.css/logo.svg" alt="sanitize" width="90" height="90" align="right">][sanitize.css]

[sanitize.css] is a CSS library that provides consistent, cross-browser
default styling of HTML elements alongside useful defaults.

**sanitize.css** is developed alongside [normalize.css], which means every
normalization is included, and every normalization and opinion are clearly
marked and documented.

**sanitize.css** wraps styles in zero-specificity selectors using `:where()`.

## Usage

```html
<link href="https://cdn.skypack.dev/sanitize.css" rel="stylesheet" />
```

[Learn more about `sanitize.css`](#features).

#### Forms CSS

A separate stylesheet that normalizes form controls without side effects.

```html
<link href="https://unpkg.com/sanitize.css/forms.css" rel="stylesheet" />
```

[Learn more about `forms.css`](#forms).

#### Assets CSS

A separate stylesheet that applies a comfortable measure to plain documents.

```html
<link href="https://unpkg.com/sanitize.css/assets.css" rel="stylesheet" />
```

[Learn more about `assets.css`](#assets).

#### Typography CSS

A separate stylesheet that normalizes typography using system interface fonts.

```html
<link href="https://unpkg.com/sanitize.css/typography.css" rel="stylesheet" />
```

[Learn more about `typography.css`](#typography).

#### Reduce Motion CSS

A separate stylesheet for restricting motion when the user has requested this at system level.

```html
<link href="https://unpkg.com/sanitize.css/reduce-motion.css" rel="stylesheet" />
```

[Learn more about `reduce-motion.css`](#reduce-motion).

#### System-UI

A separate stylesheet that adds support for using `system-ui` in Firefox.

```html
<link href="https://unpkg.com/sanitize.css/system-ui.css" rel="stylesheet" />
```

#### UI-Monospace

A separate stylesheet that adds support for using `ui-monospace` in Chrome, Edge, and Firefox.

```html
<link href="https://unpkg.com/sanitize.css/ui-monospace.css" rel="stylesheet" />
```

## Install

```sh
npm install sanitize.css --save
```

#### Webpack Usage

Import [sanitize.css] in CSS:

```css
@import '~sanitize.css';
@import '~sanitize.css/forms.css';
@import '~sanitize.css/typography.css';
```

Alternatively, import [sanitize.css] in JS:

```js
import 'sanitize.css';
import 'sanitize.css/forms.css';
import 'sanitize.css/typography.css';
```

In `webpack.config.js`, be sure to use the appropriate loaders:

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      }
    ]
  }
}
```

**Download**

See https://csstools.github.io/sanitize.css/latest/sanitize.css

## What does it do?

* Normalizes styles for a wide range of elements.
* Corrects bugs and common browser inconsistencies.
* Provides common, useful defaults.
* Explains what code does using detailed comments.

## Browser support

* Chrome (last 2)
* Edge (last 2)
* Firefox (last 2)
* Firefox ESR
* Opera (last 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

