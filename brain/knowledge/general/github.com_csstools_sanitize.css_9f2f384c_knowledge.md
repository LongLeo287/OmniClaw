---
id: github.com-csstools-sanitize.css-9f2f384c-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:42.523753
---

# KNOWLEDGE EXTRACT: github.com_csstools_sanitize.css_9f2f384c
> **Extracted on:** 2026-04-01 09:15:07
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520050/github.com_csstools_sanitize.css_9f2f384c

---

## File: `.editorconfig`
```
root = true

[*]
charset = utf-8
end_of_line = lf
indent_size = 2
indent_style = space
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false
```

## File: `.gitignore`
```
node_modules
package-lock.json
yarn.lock
.*
!.editorconfig
!.gitignore
!.travis.yml
*.log*
```

## File: `.travis.yml`
```yaml
# https://docs.travis-ci.com/user/travis-lint

language: node_js

node_js:
  - stable
```

## File: `CHANGELOG.md`
```markdown
# Changes to sanitize.css

### 13.0.0 (September 14, 2021)

- Added: `:where` too all selectors, reducing specificity to nearly zero.
- Added: All elements now use `background-repeat: no repeat`.
- Removed: Overly specific `select` selector.
- Removed: Unnecessary focus outline fix previously used in Firefox.
- Removed: Unnecessary `evergreen.css`, `forms.evergreen.css`, and `pages.css`.
- Fixed: Prevent zero-width space from consuming space in Safari.
- Changed: Browser support from "last three versions" to "last two versions".

#### assets.css

- Added: `video` to sizing restrictions.

#### font/system-ui.css

- Added: Support for `system-ui` font family in Firefox.

#### font/ui-monospace.css

- Added: Support for `ui-monospace` font family in Chrome, Edge, and Firefox.

### 12.0.1 (August 20, 2020)

- Fixed: Used case-insensitive attribute selectors in the evergreen variations.

### 12.0.0 (August 20, 2020)

- Added: Correct table border color inheritance in all Chrome, Edge, and Safari.
- Added: Remove text indentation from table contents in Chrome, Edge, and
  Safari.
- Added: Correct the inheritance of horizontal rule border color in Firefox.
- Added: Prevent overflow of a `pre` container in all browsers (opinionated).
- Added: Evergreen variations of sanitize.css (basically, without IE support).
- Added: Reduce animations, scrolling effects, and transitions when requested in
  all browsers (opinionated) to `reduce-motion.css`.
- Updated: Move size restrictions (opinionated) in all browsers to `assets.css`.
- Removed: Tapping delay style, except in IE 10, where it matters.
- Removed: Border and padding from color and range `input` in all browsers.
- Fixed: Announce `nav ol, nav ul` list semantics on Safari with VoiceOver.

### 11.0.1 (May 20, 2020)

- Fixed: Documentation is updated.

> This release is primarily made to update the polyfill used by cdnjs.

### 11.0.0 (June 3, 2019)

- Changed: Opinionated `select` background styling in `forms.css` is no longer
  applied when `multiple` or `size` attributes are also present.

### 10.0.0 (June 3, 2019)

- Added: Opinionated page measure via `page.css`.
- Added: Opinionated `border` normalization on form controls to match UA.
- Added: Opinionated `font` and `letter-spacing` as `inherit` on form controls.
- Added: Opinionated normalization of select controls.
- Added: Opinionated normalization of placeholders in Internet Explorer.
- Added: Opinionated `border` removal on iframes in all browsers.
- Removed: Opinionated `border-radius` on form controls.
- Removed: Opinionated `box-shadow` on form controls to match UA expectations.
- Fixed: `Edge` comments without `Chrome` are are changed to `Edge 18-`.
- Fixed: `Chrome` comments without `Edge` have `Edge` added.
- Fixed: Nested list `dl` normalizations split.
- Fixed: Logical `margin-block` normalization changed to `margin`.
- Fixed: Used consistent quotes around typefaces in `typography.css`.

> These fixes were brought in from normalize.css v10.1.0.

### 9.0.0 (May 16, 2019)

- Removed: Opinionated removal of text shadow on text selections due to bugs in
  High Contrast mode.
- Removed: Opinionated removal of repeating backgrounds in all browsers due to
  form control unstyling.
- Removed: Opinionated interface typography in all browsers, which is moved to
  forms.css and typography.css.
- Changed: Visually hidden content now uses some less aggressive selectors.
- Added: Opinionated interface typography in all browsers via typography.css.
- Added: Opinionated standards-like form styling in all browsers via forms.css.
- Added: Opinionated removal of the grey highlight when tapping links in iOS.

### 8.0.1 (May 12, 2019)

- Fixed: Typo of `browers` typo to `browsers`

### 8.0.0 (October 8, 2018)

- Changed: Apply `aria-disabled` disabled styles when `[aria-disabled="true"]`
- Changed: Apply `svg { fill: currentColor }` when `svg:not([fill])`
- Fixed: Apply appropriate system font fallbacks for KDE Plasma

### 7.0.3 (September 4, 2018)

- Fix disabled cursor

### 7.0.2 (September 4, 2018)

- Fixed: Restored form control margin normalizations in Firefox
- Updated: Ordering of a few rules (opinionated)

### 7.0.1 (August 25, 2018)

- Added: Support the 4-space tab width in Firefox (opinionated)

### 7.0.0 (August 22, 2018)

- Added: System font in all browsers (opinionated)
- Added: System monospace user interface font in all browsers (opinionated)
- Added: 4-space tab width in all browsers (opinionated)
- Removed: Unnecessary form control margin normalizations in Firefox
- Removed: Opinionated fieldset padding in all browsers
- Removed: Normalzations for `::-moz-focus-inner` and `:-moz-focusring` fixed
  in Firefox 53 (https://bugzilla.mozilla.org/show_bug.cgi?id=140562)
- Fixed: Correction of cursor style of increment and decrement buttons in
  Safari, not Chrome
- Fixed: Text style of placeholders in Chrome, Edge, and Safari

### 6.0.0 (June 24, 2018)

- Added: `word-break: break-word` to `html`
- Added: `font-family: inherit` on form elements
- Added: normalize.css updates
- Added: `box-sizing: border-box` to `*, ::before, ::after`
- Removed: `box-sizing: border-box` from `html` and `box-sizing: inherit` from
  `html`
- Removed: `color: inherit` and `background-color: transparent` from
  `form`

### 5.0.0 (March 1, 2017)

- Added: normalize.css v6 parity, including `summary` display
- Added: form elements to inherit line-height from html
- Removed: font styles on `html`
- Removed: unnecessary `border-spacing` zeroing

### 4.1.0 (July 1, 2016)

- Updated: The focus removal on `:hover` now targets `a:hover`

### 4.0.0 (June 20, 2016)

- Added: All improvements from normalize.css v4.1.1
- Added: Documentation for each opinionated feature
- Added: Universal `background-repeat: no-repeat`
- Removed: Reset of universal `margin` and `padding`
- Removed: Inheritance of `font-size` on elements (form controls still have it)
- Removed: Pre-compiled files that used variables
- Updated: `abbr[title]` styled using `border-bottom` over `text-decoration`
- Updated: Tests and linting

#### Why are variables removed in v4?

Variables were there for developers to override styles in sanitize.css without
editing the original file or overriding the rule. However, you *should* override
the rule so that your change is explicit, and so that your source maps
accurately indicate your changes coming from your files.

### 3.3.0 (March 3, 2016)

- Added: `b` and `strong` normalization
- Added: `::-moz-focus-inner` normalization
- Added: `hr` normalization
- Added: `svg` fill as the current color
- Updated: Organized rules into normalization, universal inheritance,
           opinionated defaults, and configurable defaults
- Updated: Moved source and compiled libraries

### 3.2.0 (February 3, 2016)

- Added: `selection.less`
- Updated: Use `root`-prefixed values across all formats
- Updated: Documentation

## 3.1.1 (February 1, 2016)

- Updated: `box-sizing` variable corrected to `border-box` in sass, scss, styl

### 3.1.0 (February 1, 2016)

- Added: Project configuration (.editorconfig)
- Added: Style linting rules and tests
- Added: `touch-action: manipulation` to remove delays during mobile tapping
- Removed: `text-rendering` due to performance issues
- Updated: `::selection` color variable corrected to `--selection-color`
- Updated: Use direct nesting

### 3.0.0 (October 23, 2015)

- Added: Normalization for **iOS 8+**
- Added: `background-repeat` for all elements
- Added: CONTRIBUTING.md
- Updated: background color and color for `:root` previously `html`
- Updated: `::selection` color to `#ffffff`
- Updated: dist from CSS source using PostCSS, cssnext, and cssnano
- Updated: Documentation

### 2.1.1 (October 5, 2015)

- Updated: bower.json

### 2.1.1 (October 5, 2015)

- Added: CSS version
- Updated: Use percentage `font-size` on `:root`
- Updated: Documentation
- Removed: `background-color` inheritance

### 2.0.0 (September 3, 2015)

- Added: Visually hidden element style `[hidden][aria-hidden="false"]`
- Added: Currently updating element style `[aria-busy="true"]`
- Added: Trigger element style `[aria-controls]`
- Added: Color style for `html`
- Added: CHANGELOG.md
- Removed: Standards-breaking visually hidden style `[hidden~="screen"]`
- Removed: Standards-breaking IE-proprietary style `[unselectable="on"]`
- Removed: Prefix-less properties and the use of Autoprefixer
- Updated: Form styling
- Updated: Support for the latest **Chrome**, **Edge**, **Firefox**,
           and **Safari**
- Updated: Licensing reference in package.json
- Updated: Development dependencies
- Updated: README.md and code documentation

### 1.2.0 (June 16, 2015)

- Added: Control over options via Sass variables
- Added: Overflow normalization on :root
- Added: `font-style` inheritance
- Updated: Support for the latest **Firefox**
- Removed: Redundant inheritance in ::before and ::after
- Removed: redundant cursor inheritance in anchor and form controls

### 1.1.0 (March 20, 2015)

- Added: Form support
- Updated: Normalization
- Updated: Border assignment

### 1.0.0 (11 6, 2012)

- Updated: Moved from normalize.css to sanitize.css

> Normalize.css had and still has opinionated, developer-centric styles. For
example, `sub` and `sup` elements are styled to not impact the line height of
text, and `table`, `th`, and `td` omit all spacing. As Nicolas pushed
Normalize.css into maturity, future preferences like these no longer had a
place in the project. Almost a year later, Sanitize was officially branded.
Where Normalize.css conservatively follows user agent consensus and results
in more pre-styled elements, Sanitize.css liberally follows developer
consensus and results in more unstyled elements.

### 0.0.0 (4 21, 2011)

- Added: Normalize.css
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to sanitize.css

Please review this document in order to make the contribution process easy and
effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of
the developers managing and developing this project. In return, we will
reciprocate that respect in addressing your issues, patches, and features.

## Using the issue tracker

The issue tracker is the preferred channel for [bug reports](#bug-reports),
[feature requests](#feature-requests) and [pull
requests](#pull-requests), but please respect the following restrictions:

* Please **do not** use the issue tracker for personal support requests.
* Please **do not** derail or troll issues. Keep the discussion on topic and
  respect the opinions of others.

## Bug reports

A bug is a _demonstrable problem_ caused by the code in this repository.

1. **Use the GitHub issue search** to see if the issue has
   [already been reported].

2. **Check if the issue has been fixed** by trying to reproduce it using the
   latest `master` branch in the repository.

3. **Isolate the problem** to create a [live example] of a [reduced test case].

A good bug report shouldn't leave others needing to chase you up for more
information. Please be as detailed as possible in your report. What is your
environment? What steps will reproduce the issue? What browser(s) and OS
experience the problem? What would you expect to be the outcome? All these
details will help people to fix any potential bugs.

Example:

> Short and descriptive example bug report title
>
> A summary of the issue and the browser/OS environment in which it occurs. If
> suitable, include the steps required to reproduce the bug.
>
> 1. This is the first step
> 2. This is the second step
> 3. Further steps, etc.
>
> `<url>` - a link to the reduced test case
>
> Any other information you want to share that is relevant to the issue being
> reported. This might include the lines of code that you have identified as
> causing the bug, and potential solutions (and your opinions on their
> merits).

## Feature requests

Feature requests are welcome. Take a moment to find out whether your idea fits
with the scope and aims of the project. It's up to *you* to make a strong case
to convince the project's developers of the merits of this feature. Please
provide as much detail and context as possible.

## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

**Please ask first** before embarking on any significant work, otherwise you
risk spending a lot of time working on something that the project's developers
might not want to merge into the project.

Please adhere to the coding conventions used throughout a project (whitespace,
accurate comments, etc.) and any other requirements (such as test coverage).

Follow this process if you'd like your work considered for inclusion in the
project:

1. To begin: [fork this project], clone your fork, and add our upstream.
   ```bash
   # Clone your fork of the repo into the current directory
   git clone git@github.com:YOUR_USER/sanitize.css.git

   # Navigate to the newly cloned directory
   cd sanitize.css

   # Assign the original repo to a remote called "upstream"
   git remote add upstream git@github.com:csstools/sanitize.css.git

   # Install the tools necessary for testing
   npm install
   ```

2. Create a branch for your feature or fix:
   ```bash
   # Move into a new branch for your feature
   git checkout -b feature/thing
   ```
   ```bash
   # Move into a new branch for your fix
   git checkout -b fix/something
   ```

3. If your code follows our practices, then push your feature branch:
   ```bash
   # Test current code
   npm test
   ```
   ```bash
   # Push the branch for your new feature
   git push origin feature/thing
   ```
   ```bash
   # Or, push the branch for your update
   git push origin update/something
   ```

   Be sure to add a test to the `test.html` file if appropriate, and test
   your change in all supported browsers.


Now [open a pull request] with a clear title and description. Remember,
by submitting a patch, you agree to allow the project owner to license your
work under the same license as that used by the project.

### CSS Conventions

Keep the CSS file as readable as possible by following these guidelines:

- Comments are short and to the point.
- Comments without a number reference the entire rule.
- Comments describe the selector when the selector does not make the
  normalization obvious.
- Comments begin with “Correct the...” when they deal with less obvious side
  effects.
- Rules are sorted by section, cascade, specificity, and then alphabetic order.
- Selectors are sorted by low-to-high specificity and then alphabetic order.
- `in browser` applies to all versions.
- `in browser v+` applies to all versions after and including the version.
- `in browser v-` applies to all versions up to and including the version.
- `in browser v-v` applies to all versions including and between the versions.

## Maintainers

If you have commit access, please follow this process for merging patches and
cutting new releases.

### Accepting patches

1. Check that a patch is within the scope and philosophy of the project.
2. Check that a patch has any necessary tests and a proper, descriptive commit
   message.
3. Test the patch locally.
4. Use GitHub’s merge button with caution or apply the patch locally, squashing
   any commits.

### Releasing a new version

1. Include all new functional changes in CHANGELOG.md.
2. Create an annotated tag for the version: `git tag -m "0.0.0" 0.0.0`.
3. Push the changes and tags to GitHub: `git push --tags origin master`
4. Update the `gh-pages` branch,
   1. Copy the latest sanitize.css and test.html from the master branch into
      the root directory, the `latest` directory, and a new directory named
      after the new version: `0.0.0`.
   2. Update the sanitize.css version and supported browsers in `index.html`.

### Semver strategy

[Semver](http://semver.org/) is a widely accepted method for deciding how
version numbers are incremented in a project. Versions are written as
MAJOR.MINOR.PATCH.

Any change to CSS rules whatsoever is considered backwards-breaking and will
result in a new **major** release. Others changes with no impact on rendering
are considered backwards-compatible and will result in a new **patch** release.

No changes to CSS rules can add functionality in a backwards-compatible manner,
therefore no changes are considered **minor**. For instance, a normalization on
an element selector may override a user style on a universal selector, or a
change to `opacity` might cause [inputs to disappear](https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/3901363/),
or a change to `background-color` might cause [backgrounds to shrink](https://github.com/csstools/sanitize.css/issues/42).

[already been reported]: https://github.com/csstools/sanitize.css/issues
[fork this project]:     https://github.com/csstools/sanitize.css/fork
[live example]:          https://codepen.io/pen
[open a pull request]:   https://help.github.com/articles/using-pull-requests/
[reduced test case]:     https://css-tricks.com/reduced-test-cases/
```

## File: `LICENSE.md`
```markdown
# CC0 1.0 Universal

## Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator and
subsequent owner(s) (each and all, an “owner”) of an original work of
authorship and/or a database (each, a “Work”).

Certain owners wish to permanently relinquish those rights to a Work for the
purpose of contributing to a commons of creative, cultural and scientific works
(“Commons”) that the public can reliably and without fear of later claims of
infringement build upon, modify, incorporate in other works, reuse and
redistribute as freely as possible in any form whatsoever and for any purposes,
including without limitation commercial purposes. These owners may contribute
to the Commons to promote the ideal of a free culture and the further
production of creative, cultural and scientific works, or to gain reputation or
greater distribution for their Work in part through the use and efforts of
others.

For these and/or other purposes and motivations, and without any expectation of
additional consideration or compensation, the person associating CC0 with a
Work (the “Affirmer”), to the extent that he or she is an owner of Copyright
and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and
publicly distribute the Work under its terms, with knowledge of his or her
Copyright and Related Rights in the Work and the meaning and intended legal
effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
   protected by copyright and related or neighboring rights (“Copyright and
   Related Rights”). Copyright and Related Rights include, but are not limited
   to, the following:
   1. the right to reproduce, adapt, distribute, perform, display, communicate,
      and translate a Work;
   2. moral rights retained by the original author(s) and/or performer(s);
   3. publicity and privacy rights pertaining to a person’s image or likeness
      depicted in a Work;
   4. rights protecting against unfair competition in regards to a Work,
      subject to the limitations in paragraph 4(i), below;
   5. rights protecting the extraction, dissemination, use and reuse of data in
      a Work;
   6. database rights (such as those arising under Directive 96/9/EC of the
      European Parliament and of the Council of 11 March 1996 on the legal
      protection of databases, and under any national implementation thereof,
      including any amended or successor version of such directive); and
   7. other similar, equivalent or corresponding rights throughout the world
      based on applicable law or treaty, and any national implementations
      thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention of,
   applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and
   unconditionally waives, abandons, and surrenders all of Affirmer’s Copyright
   and Related Rights and associated claims and causes of action, whether now
   known or unknown (including existing as well as future claims and causes of
   action), in the Work (i) in all territories worldwide, (ii) for the maximum
   duration provided by applicable law or treaty (including future time
   extensions), (iii) in any current or future medium and for any number of
   copies, and (iv) for any purpose whatsoever, including without limitation
   commercial, advertising or promotional purposes (the “Waiver”). Affirmer
   makes the Waiver for the benefit of each member of the public at large and
   to the detriment of Affirmer’s heirs and successors, fully intending that
   such Waiver shall not be subject to revocation, rescission, cancellation,
   termination, or any other legal or equitable action to disrupt the quiet
   enjoyment of the Work by the public as contemplated by Affirmer’s express
   Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason be
   judged legally invalid or ineffective under applicable law, then the Waiver
   shall be preserved to the maximum extent permitted taking into account
   Affirmer’s express Statement of Purpose. In addition, to the extent the
   Waiver is so judged Affirmer hereby grants to each affected person a
   royalty-free, non transferable, non sublicensable, non exclusive,
   irrevocable and unconditional license to exercise Affirmer’s Copyright and
   Related Rights in the Work (i) in all territories worldwide, (ii) for the
   maximum duration provided by applicable law or treaty (including future time
   extensions), (iii) in any current or future medium and for any number of
   copies, and (iv) for any purpose whatsoever, including without limitation
   commercial, advertising or promotional purposes (the “License”). The License
   shall be deemed effective as of the date CC0 was applied by Affirmer to the
   Work. Should any part of the License for any reason be judged legally
   invalid or ineffective under applicable law, such partial invalidity or
   ineffectiveness shall not invalidate the remainder of the License, and in
   such case Affirmer hereby affirms that he or she will not (i) exercise any
   of his or her remaining Copyright and Related Rights in the Work or (ii)
   assert any associated claims and causes of action with respect to the Work,
   in either case contrary to Affirmer’s express Statement of Purpose.

4. Limitations and Disclaimers.
   1. No trademark or patent rights held by Affirmer are waived, abandoned,
      surrendered, licensed or otherwise affected by this document.
   2. Affirmer offers the Work as-is and makes no representations or warranties
      of any kind concerning the Work, express, implied, statutory or
      otherwise, including without limitation warranties of title,
      merchantability, fitness for a particular purpose, non infringement, or
      the absence of latent or other defects, accuracy, or the present or
      absence of errors, whether or not discoverable, all to the greatest
      extent permissible under applicable law.
   3. Affirmer disclaims responsibility for clearing rights of other persons
      that may apply to the Work or any use thereof, including without
      limitation any person’s Copyright and Related Rights in the Work.
      Further, Affirmer disclaims responsibility for obtaining any necessary
      consents, permissions or other rights required for any use of the Work.
   4. Affirmer understands and acknowledges that Creative Commons is not a
      party to this document and has no duty or obligation with respect to this
      CC0 or use of the Work.

For more information, please see
http://creativecommons.org/publicdomain/zero/1.0/.
```

## File: `README.md`
```markdown
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
* Opera (last 2)
* Safari (last 2)
* iOS Safari (last 2)
* Internet Explorer 9+

## Differences

[normalize.css] and [sanitize.css] correct browser bugs while carefully testing
and documenting changes. normalize.css styles adhere to css specifications.
sanitize.css styles adhere to common developer expectations and preferences.
[reset.css] unstyles all elements. Both sanitize.css and normalize.css are
maintained in sync.

## Features

##### Box sizing defaults to border-box

```css
*, ::before, ::after {
  box-sizing: border-box;
}
```

##### Backgrounds do not repeat by default

```css
*, ::before, ::after {
  background-repeat: no-repeat;
}
```

##### Pseudo-elements inherit text decoration and vertical alignment

```css
::before,
::after {
  text-decoration: inherit;
  vertical-align: inherit;
}
```

##### Cursors only change to hint non-obvious interfaces

```css
html {
  cursor: default;
}
```

##### Text has a comfortable line height in all browsers

```css
html {
  line-height: 1.5;
}
```

##### Tabs appear the same on the web as in a typical editor

```css
html {
  tab-size: 4;
}
```

##### Words break to prevent overflow

```css
html {
  word-break: break-all;
}
```

##### Documents do not use a margin for outer padding

```css
body {
  margin: 0;
}
```

##### Navigation lists do not include a marker style

```css
nav ol, nav ul {
  list-style: none;
  padding: 0;
}
```

##### Media elements align to the text center of other content

```css
audio, canvas, iframe, img, svg, video {
  vertical-align: middle;
}
```

##### SVGs fallback to the current text color

```css
svg:not([fill]) {
  fill: currentColor;
}
```

##### Tables do not include additional border spacing

```css
table {
  border-collapse: collapse;
}
```

##### Textareas only resize vertically by default

```css
textarea {
  resize: vertical;
}
```

##### Single taps are dispatched immediately on clickable elements

```css
a, area, button, input, label, select, summary, textarea, [tabindex] {
  -ms-touch-action: manipulation;
  touch-action: manipulation;
}
```

##### ARIA roles include visual cursor hints

```css
[aria-busy="true"] {
  cursor: progress;
}

[aria-controls] {
  cursor: pointer;
}

[aria-disabled="true"], [disabled] {
  cursor: default;
}
```

##### Visually hidden content remains accessible

```css
[aria-hidden="false"][hidden] {
  display: initial;
}

[aria-hidden="false"][hidden]:not(:focus) {
  clip: rect(0, 0, 0, 0);
  position: absolute;
}
```

---

## Forms

[sanitize.css] includes a separate stylesheet for normalizing forms using
minimal, standards-like styling.

```html
<link href="https://unpkg.com/sanitize.css" rel="stylesheet" />
<link href="https://unpkg.com/sanitize.css/forms.css" rel="stylesheet" />
```

### Forms Features

##### Form controls appear visually consistent and restyle consistently

```css
button, input, select, textarea {
  background-color: transparent;
  border: 1px solid WindowFrame;
  color: inherit;
  font: inherit;
  letter-spacing: inherit;
  padding: 0.25em 0.375em;
}

[type="color"],
[type="range"] {
  border-width: 0;
  padding: 0;
}
```

##### Expandable select controls appear visually consistent

```css
select {
  -moz-appearance: none;
  -webkit-appearance: none;
  background: no-repeat right center / 1em;
  border-radius: 0;
  padding-right: 1em;
}

select:not([multiple]):not([size]) {
  background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='4'%3E%3Cpath d='M4 0h6L7 4'/%3E%3C/svg%3E");
}

::-ms-expand {
  display: none;
}
```

##### Placeholders appear visually consistent in Internet Explorer

```css
:-ms-input-placeholder {
  color: rgba(0, 0, 0, 0.54);
}
```

## Assets

[sanitize.css] includes a separate stylesheet for normalizing restricting the
size of assets in all browsers.

```html
<link href="https://unpkg.com/sanitize.css" rel="stylesheet" />
<link href="https://unpkg.com/sanitize.css/assets.css" rel="stylesheet" />
```

### Assets Features

##### Assets use a comfortable measure in all browsers

```css
iframe,
img,
input,
select,
textarea {
  height: auto;
  max-width: 100%;
}
```

## Typography

[sanitize.css] includes a separate stylesheet for normalizing typography using
system interface fonts.

```html
<link href="https://unpkg.com/sanitize.css" rel="stylesheet" />
<link href="https://unpkg.com/sanitize.css/typography.css" rel="stylesheet" />
```

### Typography Features

##### Typography uses the default system font

```css
html {
  font-family:
    system-ui,
    /* macOS 10.11-10.12 */ -apple-system,
    /* Windows 6+ */ Segoe UI,
    /* Android 4+ */ Roboto,
    /* Ubuntu 10.10+ */ Ubuntu,
    /* Gnome 3+ */ Cantarell,
    /* KDE Plasma 5+ */ Noto Sans,
    /* fallback */ sans-serif,
    /* macOS emoji */ "Apple Color Emoji",
    /* Windows emoji */ "Segoe UI Emoji",
    /* Windows emoji */ "Segoe UI Symbol",
    /* Linux emoji */ "Noto Color Emoji";
}
```

##### Pre-formatted and code-formatted text uses the monospace system font

```css
code, kbd, pre, samp {
  font-family:
    /* macOS 10.10+ */ Menlo,
    /* Windows 6+ */ Consolas,
    /* Android 4+ */ Roboto Mono,
    /* Ubuntu 10.10+ */ Ubuntu Monospace,
    /* KDE Plasma 5+ */ Noto Mono,
    /* KDE Plasma 4+ */ Oxygen Mono,
    /* Linux/OpenOffice fallback */ Liberation Mono,
    /* fallback */ monospace;
}
```

## Reduce Motion

[sanitize.css] includes a separate stylesheet for restricting motion when the
user has requested this at a system level.

```html
<link href="https://unpkg.com/sanitize.css" rel="stylesheet" />
<link href="https://unpkg.com/sanitize.css/reduce-motion.css" rel="stylesheet" />
```

### Reduce Motion Features

##### Animations, scrolling effects, transitions and view transitions are reduced in all browsers

```css
@media (prefers-reduced-motion: reduce) {
  *,
  ::before,
  ::after {
    animation-delay: -1ms !important;
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    background-attachment: initial !important;
    scroll-behavior: auto !important;
    transition-delay: 0s !important;
    transition-duration: 0s !important;
  }

  @view-transition {
    navigation: none !important;
  }
}
```

## Contributing

Please read the [contribution guidelines](CONTRIBUTING.md) in order to make the
contribution process easy and effective for everyone involved.

## Acknowledgements

sanitize.css is a project by [Jonathan Neal](https://github.com/jonathantneal),
built upon normalize.css, a project by
[Jonathan Neal](https://github.com/jonathantneal),
co-created with [Nicolas Gallagher](https://github.com/necolas).

[normalize.css]: https://github.com/csstools/normalize.css
[reset.css]: http://meyerweb.com/eric/tools/css/reset/
[sanitize.css]: https://github.com/csstools/sanitize.css
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

Only the latest version of plugins and packages will receive security patches.  
Please reach out if you need extended support for an older version.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :x:                |
| < 4.0   | :x:                |

## Security contact information

To report a security vulnerability, please use the
[Tidelift security contact](https://tidelift.com/security).
Tidelift will coordinate the fix and disclosure.
```

## File: `assets.css`
```css
/**
 * Restrict sizing to the page width in all browsers (opinionated).
 */

:where(iframe, img, input, video, select, textarea) {
  max-width: 100%;
}

/**
 * Preserve aspect ratio
 */

:where(iframe, img[width][height], input, video, select, textarea) {
  height: auto;
}
```

## File: `forms.css`
```css
/**
 * 1. Change the inconsistent appearance in all browsers (opinionated).
 * 2. Add typography inheritance in all browsers (opinionated).
 */

:where(button, input, select, textarea) {
  background-color: transparent; /* 1 */
  border: 1px solid WindowFrame; /* 1 */
  color: inherit; /* 1 */
  font: inherit; /* 2 */
  letter-spacing: inherit; /* 2 */
  padding: 0.25em 0.375em; /* 1 */
}

/**
 * Change the inconsistent appearance in all browsers (opinionated).
 */

:where(select) {
  -webkit-appearance: none;
  appearance: none;
  background: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='4'%3E%3Cpath d='M4 0h6L7 4'/%3E%3C/svg%3E") no-repeat right center / 1em;
  border-radius: 0;
  padding-right: 1em;
}

/**
 * Don't show the arrow for multiple choice selects
 */

:where(select[multiple]) {
  background-image: none;
}

/**
 * Remove the border and padding in all browsers (opinionated).
 */

:where([type="color" i], [type="range" i]) {
  border-width: 0;
  padding: 0;
}
```

## File: `package.json`
```json
{
  "name": "sanitize.css",
  "version": "13.0.0",
  "description": "A best-practices CSS foundation",
  "author": "Jonathan Neal <jonathantneal@hotmail.com>",
  "contributors": [
    "Jonathan Neal <jonathantneal@hotmail.com> (http://jonathantneal.com/)",
    "Nicolas Gallagher <nicolas@nicolasgallagher.com> (http://nicolasgallagher.com/)"
  ],
  "license": "CC0-1.0",
  "repository": "csstools/sanitize.css",
  "homepage": "https://github.com/csstools/sanitize.css#readme",
  "bugs": "https://github.com/csstools/sanitize.css/issues",
  "main": "sanitize.css",
  "style": "sanitize.css",
  "files": [
    "assets.css",
    "forms.css",
    "reduce-motion.css",
    "sanitize.css",
    "system-ui.css",
    "typography.css",
    "ui-monospace.css"
  ],
  "scripts": {
    "prepublishOnly": "npm test",
    "test": "stylelint *.css"
  },
  "devDependencies": {
    "stylelint": "^13.13.1",
    "stylelint-config-standard": "^22.0.0"
  },
  "stylelint": {
    "extends": "stylelint-config-standard",
    "rules": {
      "font-family-no-duplicate-names": [
        true,
        {
          "ignoreFontFamilyNames": [
            "monospace"
          ]
        }
      ],
      "no-descending-specificity": [
        null
      ]
    }
  },
  "keywords": [
    "css",
    "normalizes",
    "sanitizes",
    "browsers",
    "fixes"
  ]
}
```

## File: `reduce-motion.css`
```css
/*
 * 1. Remove animations when motion is reduced (opinionated).
 * 2. Remove fixed background attachments when motion is reduced (opinionated).
 * 3. Remove timed scrolling behaviors when motion is reduced (opinionated).
 * 4. Remove transitions when motion is reduced (opinionated).
 * 5. Remove view-transitions when motion is reduced (opinionated).
 */

@media (prefers-reduced-motion: reduce) {
  *,
  ::before,
  ::after {
    animation-delay: -1ms !important; /* 1 */
    animation-duration: 1ms !important; /* 1 */
    animation-iteration-count: 1 !important; /* 1 */
    background-attachment: initial !important; /* 2 */
    scroll-behavior: auto !important; /* 3 */
    transition-delay: 0s !important; /* 4 */
    transition-duration: 0s !important; /* 4 */
  }

  @view-transition {
    navigation: none !important; /* 5 */
  }
}
```

## File: `sanitize.css`
```css
/* Document
 * ========================================================================== */

/**
 * 1. Add border box sizing in all browsers (opinionated).
 * 2. Backgrounds do not repeat by default (opinionated).
 * 3. Masks do not repeat by default (opinionated).
 */

*,
::before,
::after {
  box-sizing: border-box; /* 1 */
  background-repeat: no-repeat; /* 2 */
  mask-repeat: no-repeat; /* 3 */
}

/**
 * 1. Add text decoration inheritance in all browsers (opinionated).
 * 2. Add vertical alignment inheritance in all browsers (opinionated).
 */

::before,
::after {
  text-decoration: inherit; /* 1 */
  vertical-align: inherit; /* 2 */
}

/**
 * 1. Use the default cursor in all browsers (opinionated).
 * 2. Change the line height in all browsers (opinionated).
 * 3. Breaks words to prevent overflow in all browsers (opinionated).
 * 4. Use a 4-space tab width in all browsers (opinionated).
 * 5. Remove the grey highlight on links in iOS (opinionated).
 * 6. Prevent adjustments of font size after orientation changes in iOS.
 */

:where(:root) {
  cursor: default; /* 1 */
  line-height: 1.5; /* 2 */
  overflow-wrap: break-word; /* 3 */
  -moz-tab-size: 4; /* 4 */
  tab-size: 4; /* 4 */
  -webkit-tap-highlight-color: transparent; /* 5 */
  -webkit-text-size-adjust: 100%; /* 6 */
  text-size-adjust: 100%; /* 6 */
}

/* Sections
 * ========================================================================== */

/**
 * Remove the margin in all browsers (opinionated).
 */

:where(body) {
  margin: 0;
}

/**
 * Correct the font size and margin on `h1` elements within `section` and
 * `article` contexts in Chrome, Edge, Firefox, and Safari.
 */

:where(h1) {
  font-size: 2em;
  margin: 0.67em 0;
}

/* Grouping content
 * ========================================================================== */

/**
 * Remove the margin on nested lists in Chrome, Edge, and Safari.
 */

:where(dl, ol, ul) :where(dl, ol, ul) {
  margin: 0;
}

/**
 * Add the correct box sizing in Firefox.
 */

:where(hr) {
  height: 0;
}

/**
 * Remove the list style on navigation lists in all browsers (opinionated).
 */

:where(nav) :where(ol, ul) {
  list-style-type: none;
  padding: 0;
}

/**
 * Prevent VoiceOver from ignoring list semantics in Safari (opinionated).
 */

:where(nav li)::before {
  content: "\200B";
  float: left;
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 * 3. Prevent overflow of the container in all browsers (opinionated).
 */

:where(pre) {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
  overflow: auto; /* 3 */
}

/* Text-level semantics
 * ========================================================================== */

/**
 * Add the correct text decoration in Safari.
 */

:where(abbr[title]) {
  text-decoration: underline;
  text-decoration: underline dotted;
}

/**
 * Add the correct font weight in Chrome, Edge, and Safari.
 */

:where(b, strong) {
  font-weight: bolder;
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */

:where(code, kbd, samp) {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
 * Add the correct font size in all browsers.
 */

:where(small) {
  font-size: 80%;
}

/* Embedded content
 * ========================================================================== */

/*
 * Change the alignment on media elements in all browsers (opinionated).
 */

:where(audio, canvas, iframe, img, svg, video) {
  vertical-align: middle;
}

/**
 * Remove the border on iframes in all browsers (opinionated).
 */

:where(iframe) {
  border-style: none;
}

/**
 * Change the fill color to match the text color in all browsers (opinionated).
 */

:where(svg:not([fill])) {
  fill: currentColor;
}

/* Tabular data
 * ========================================================================== */

/**
 * 1. Collapse border spacing in all browsers (opinionated).
 * 2. Correct table border color in Chrome, Edge, and Safari.
 * 3. Remove text indentation from table contents in Chrome, Edge, and Safari.
 */

:where(table) {
  border-collapse: collapse; /* 1 */
  border-color: currentColor; /* 2 */
  text-indent: 0; /* 3 */
}

/* Forms
 * ========================================================================== */

/**
 * Remove the margin on controls in Safari.
 */

:where(button, input, select) {
  margin: 0;
}

/**
 * Correct the inability to style buttons in iOS and Safari.
 */

:where(button, [type="button" i], [type="reset" i], [type="submit" i]) {
  -webkit-appearance: button;
}

/**
 * Change the inconsistent appearance in all browsers (opinionated).
 */

:where(fieldset) {
  border: 1px solid #a0a0a0;
}

/**
 * Add the correct vertical alignment in Chrome, Edge, and Firefox.
 */

:where(progress) {
  vertical-align: baseline;
}

/**
 * 1. Remove the margin in Firefox and Safari.
 * 3. Change the resize direction in all browsers (opinionated).
 */

:where(textarea) {
  margin: 0; /* 1 */
  resize: vertical; /* 3 */
}

/**
 * 1. Correct the odd appearance in Chrome, Edge, and Safari.
 * 2. Correct the outline style in Safari.
 */

:where([type="search" i]) {
  -webkit-appearance: textfield; /* 1 */
  outline-offset: -2px; /* 2 */
}

/**
 * Correct the cursor style of increment and decrement buttons in Safari.
 */

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
  height: auto;
}

/**
 * Correct the text style of placeholders in Chrome, Edge, and Safari.
 */

::-webkit-input-placeholder {
  color: inherit;
  opacity: 0.54;
}

/**
 * Remove the inner padding in Chrome, Edge, and Safari on macOS.
 */

::-webkit-search-decoration {
  -webkit-appearance: none;
}

/**
 * 1. Correct the inability to style upload buttons in iOS and Safari.
 * 2. Change font properties to `inherit` in Safari.
 */

::-webkit-file-upload-button {
  -webkit-appearance: button; /* 1 */
  font: inherit; /* 2 */
}

/* Interactive
 * ========================================================================== */

/*
 * Add the correct styles in Safari.
 */

:where(dialog) {
  background-color: white;
  border: solid;
  color: black;
  height: -moz-fit-content;
  height: fit-content;
  left: 0;
  margin: auto;
  padding: 1em;
  position: absolute;
  right: 0;
  width: -moz-fit-content;
  width: fit-content;
}

:where(dialog:not([open])) {
  display: none;
}

/*
 * Add the correct display in Safari.
 */

:where(details > summary:first-of-type) {
  display: list-item;
}

/* Accessibility
 * ========================================================================== */

/**
 * Change the cursor on busy elements in all browsers (opinionated).
 */

:where([aria-busy="true" i]) {
  cursor: progress;
}

/*
 * Change the cursor on disabled, not-editable, or otherwise
 * inoperable elements in all browsers (opinionated).
 */

:where([aria-disabled="true" i], [disabled]) {
  cursor: not-allowed;
}

/*
 * Change the display on visually hidden accessible elements
 * in all browsers (opinionated).
 */

:where([aria-hidden="false" i][hidden]) {
  display: initial;
}

:where([aria-hidden="false" i][hidden]:not(:focus)) {
  clip: rect(0, 0, 0, 0);
  position: absolute;
}
```

## File: `system-ui.css`
```css
/**
 * Add the correct system-ui font-family in Firefox.
 */

@font-face {
  font-family: system-ui;
  src: local(".AppleSystemUIFont"), local("Segoe UI"), local("Ubuntu"), local("Roboto-Regular"), local("HelveticaNeue");
}

@font-face {
  font-family: system-ui;
  font-style: italic;
  src: local(".AppleSystemUIFont"), local("Segoe UI Italic"), local("Ubuntu-Italic"), local("Roboto-Italic"), local("HelveticaNeue-Italic");
}

@font-face {
  font-family: system-ui;
  font-weight: bold;
  src: local(".AppleSystemUIFont"), local("Segoe UI Bold"), local("Ubuntu-Bold"), local("Roboto-Bold"), local("HelveticaNeue-Bold");
}

@font-face {
  font-family: system-ui;
  font-style: italic;
  font-weight: bold;
  src: local(".AppleSystemUIFont"), local("Segoe UI Bold Italic"), local("Ubuntu-BoldItalic"), local("Roboto-BoldItalic"), local("HelveticaNeue-BoldItalic");
}
```

## File: `typography.css`
```css
/**
 * Use the default user interface font in all browsers (opinionated).
 */

html {
  font-family:
    system-ui,
    /* macOS 10.11-10.12 */ -apple-system,
    /* Windows 6+ */ "Segoe UI",
    /* Android 4+ */ "Roboto",
    /* Ubuntu 10.10+ */ "Ubuntu",
    /* Gnome 3+ */ "Cantarell",
    /* KDE Plasma 5+ */ "Noto Sans",
    /* fallback */ sans-serif,
    /* macOS emoji */ "Apple Color Emoji",
    /* Windows emoji */ "Segoe UI Emoji",
    /* Windows emoji */ "Segoe UI Symbol",
    /* Linux emoji */ "Noto Color Emoji";
}

/**
 * Use the default monospace user interface font in all browsers (opinionated).
 */

code,
kbd,
samp,
pre {
  font-family:
    ui-monospace,
    /* macOS 10.10+ */ "Menlo",
    /* Windows 6+ */ "Consolas",
    /* Android 4+ */ "Roboto Mono",
    /* Ubuntu 10.10+ */ "Ubuntu Monospace",
    /* KDE Plasma 5+ */ "Noto Mono",
    /* KDE Plasma 4+ */ "Oxygen Mono",
    /* Linux/OpenOffice fallback */ "Liberation Mono",
    /* fallback */ monospace,
    /* macOS emoji */ "Apple Color Emoji",
    /* Windows emoji */ "Segoe UI Emoji",
    /* Windows emoji */ "Segoe UI Symbol",
    /* Linux emoji */ "Noto Color Emoji";
}
```

## File: `ui-monospace.css`
```css
/**
 * Add the correct system-ui font-family in Chrome, Edge, and Firefox.
 */

@font-face {
  font-family: ui-monospace;
  src: local(".AppleSystemUIFontMonospaced-Regular"), local("Segoe UI Mono"), local("UbuntuMono"), local("Roboto-Mono"), local("Menlo");
}

@font-face {
  font-family: ui-monospace;
  font-style: italic;
  src: local(".AppleSystemUIFontMonospaced-RegularItalic"), local("Segoe UI Mono Italic"), local("UbuntuMono-Italic"), local("Roboto-Mono-Italic"), local("Menlo-Italic");
}

@font-face {
  font-family: ui-monospace;
  font-weight: bold;
  src: local(".AppleSystemUIFontMonospaced-Bold"), local("Segoe UI Mono Bold"), local("UbuntuMono-Bold"), local("Roboto-Mono-Bold"), local("Menlo-Bold");
}

@font-face {
  font-family: ui-monospace;
  font-style: italic;
  font-weight: bold;
  src: local(".AppleSystemUIFontMonospaced-BoldItalic"), local("Segoe UI Mono Bold Italic"), local("UbuntuMono-BoldItalic"), local("Roboto-Mono-BoldItalic"), local("Menlo-BoldItalic");
}
```

