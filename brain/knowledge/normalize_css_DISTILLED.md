---
id: normalize.css
type: knowledge
owner: OA_Triage
---
# normalize.css
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@csstools/normalize.css",
  "version": "12.1.1",
  "description": "A cross-browser CSS foundation",
  "author": "Jonathan Neal <jonathantneal@hotmail.com>",
  "contributors": [
    "Jonathan Neal <jonathantneal@hotmail.com> (http://jonathantneal.com/)",
    "Nicolas Gallagher <nicolas@nicolasgallagher.com> (http://nicolasgallagher.com/)",
    "Luciano Battagliero <lucianobattagliero+git@gmail.com> (https://lucianobattagliero.com/)"
  ],
  "license": "CC0-1.0",
  "repository": "csstools/normalize.css",
  "homepage": "https://github.com/csstools/normalize.css#readme",
  "bugs": "https://github.com/csstools/normalize.css/issues",
  "main": "normalize.css",
  "style": "normalize.css",
  "files": [
    "normalize.css",
    "opinionated.css"
  ],
  "scripts": {
    "test": "echo \"no test\""
  },
  "keywords": [
    "css",
    "normalizes",
    "browsers",
    "fixes"
  ]
}

```

### File: README.md
```md
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
co-created with [Nicolas Gallagher](https://github.com/necolas).

[@csstools/normalize.css]: https://github.com/csstools/normalize.css

```

### File: CHANGELOG.md
```md
# Changes to @csstools/normalize.css

### 12.1.1 (December 29, 2023)

- Fixed: normalize `text-size-adjust` in the most backwards compatible way.

### 12.1.0 (December 29, 2023)

- Added: `text-size-adjust` [#25](https://github.com/csstools/normalize.css/issues/25)
- Fixed: group `pre` with `code`, `kbd`, `samp` [#24](https://github.com/csstools/normalize.css/issues/24)

### 12.0.0 (September 15, 2021)

- Changed: normalize.css no longer contributes specificity.
- Changed: normalize.css fixes now respect `writing-mode`.
- Removed: Fixes for older browsers, and all fixes for IE.
- Fixed: `table` uses correct `border-color: currentColor` normalization.

### 11.0.1 (August 20, 2020)

- Fixed: Used case-insensitive attribute selectors in the evergreen variations.

### 11.0.0 (August 20, 2020)

- Added: Correct table border color inheritance in all Chrome, Edge, and Safari.
- Added: Remove text indentation from table contents in Chrome, Edge, and
  Safari.
- Added: Correct the inheritance of border color in Firefox.
- Added: Evergreen variations of normalize.css (basically, without IE support).

### 10.1.0 (June 3, 2019)

- Fixed: `Edge` comments without `Chrome` are are changed to `Edge 18-`.
- Fixed: `Chrome` comments without `Edge` have `Edge` added.
- Fixed: Nested list `dl` normalizations split.
- Fixed: Logical `margin-block` normalization changed to `margin`.

### 10.0.0 (May 16, 2019)

- Added: Removal of the margin on nested lists in Chrome and Safari.
- Added: opinionated.css, normalize.css with classic opinionated styles.
- Changed: Reverted license to prehistory state, or CC0-1.0 as intended.

> There are now 2 versions of normalize.css. Nicolas Gallagher and I started
> writing normalize.css together. I named and created the normalize.css
> repository with the help of Paul Irish and Ben Alman. I transferred the
> repository to Necolas, who made it into a “household” CSS library. Much
> later I resumed management of normalize.css with Luciano Battagliero. We
> tagged, deprecated, and removed “opinionated” styles — styles developers
> often prefer but which do not fix bugs or “normalize” browser differences.
> Necolas disagreed with this change, and resolved the matter AFAIK by removing
> all of the other contributors, locking discussion threads, wiping my name
> (and his) from all files, and blocking me from being able to follow the
> project.
>
> I may later create a new project with a new name, but for now I intend to
> continue working on the normalize.css project, sometimes under the
> “csstools” tag. I hope one day our differences are resolved and the projects
> will be one again.
>
> For reference within this project:
> normalize.css resolves bugs and common browser inconsistencies.
> opinionated.css does the same while preserving the classic opinionated styles.

---

### 9.0.1 (September 4, 2018)

- Changed: Restored `::-moz-focus-inner` and `:-moz-focusring` normalizations
  confirmed necessary in Firefox 61.
- Changed: Sorted the `::-webkit-inner-spin-button` and
  `::-webkit-outer-spin-button` pseudo-class selectors.
- Updated: Tests.

### 9.0.0 (August 22, 2018)

- Fixed: Cursor style of increment and decrement buttons in Safari, not Chrome.
- Fixed: Text style of placeholders in Chrome, Edge, and Safari.
- Removed: unnecessary form control margin normalizations in Firefox.
- Removed: opinionated fieldset padding in all browsers.
- Removed: `::-moz-focus-inner` and `:-moz-focusring` normalizations fixed in
  Firefox 53 https://bugzilla.mozilla.org/show_bug.cgi?id=140562

---

### 8.0.0 (June 15, 2018)

- Removed: Normalizations for unsupported browsers, such as Android 4-,
  Chrome 57-, Firefox 52-, IE 8-, and Safari 7-.
- Removed: Removal of gaps on link underlines in iOS and Safari.
- Changed: Selector weight on form control normalizations.
- Removed: Removal of search input cancel button in Chrome and Safari.
- Added: Dialog styles for Edge, IE, and Safari.
- Added: Tests for every single feature.
- Updated: Documentation to be more clear and helpful.

---

### 7.0.0 (May 26, 2017)

- Changed: Separated out selector targeted fixes for readability.
- Updated: Browser landscape of abbr[title] fixes.
- Updated: Browser landscape of details fixes.
- Fixed: Browser landscape of displays.
- Removed: Opinionated changes on sub and sup elements.

---

### 6.0.0 (March 26, 2017)

- Removed: All opinionated rules.
- Fixed: Document heading comment.
- Updated: Support for `abbr[title]`.

> At the time of this writing, for anyone who still wants/needs the opinionated
> rules, see [opinionate.css](https://github.com/adamgruber/opinionate.css)_.

---

### 5.0.0 (October 3, 2016)

- Added: Normalized sections not already present from
  https://html.spec.whatwg.org/multipage/.
- Removed: `::placeholder` styles due to a bug in Edge.
- Removed: `optgroup` normalization needed by the previous font reset.
- Changed: Moved unsorted rules into their respective sections.
- Changed: Explicitly defined font resets on form controls.
- Updated: `summary` style in all browsers.
- Updated: Text-size-adjust documentation for IE on Windows Phone
- Updated: OS X reference to macOS
- Updated: Semver strategy.

---

### 4.2.0 (June 30, 2016)

- Fixed: `line-height` in all browsers.
- Fixed: `optgroup` font inheritance.
- Updated: Project heading.

### 4.1.1 (April 12, 2016)

- Updated: Project heading.

### 4.1.0 (April 11, 2016)

- Added: Normalized placeholders in Chrome, Edge, and Safari.
- Added: Normalized `text-decoration-skip` property in Safari.
- Added: Normalized file select buttons.
- Added: Normalized search input outlines in Safari.
- Removed: Opinionated cursor styles on buttons.
- Changed: Limited Firefox focus normalizations to buttons.
- Changed: Restored `main` to package.json.
- Changed: Restored proper overflow to certain `select` elements.
- Updated: Stylelint configuration.
- Updated: Tests.

### 4.0.0 (March 19, 2016)

- Added: Correct font weight for `b` and `strong` in Chrome, Edge, and Safari.
- Removed: Unnecessary normalization of `line-height` for `input`.
- Removed: Unnecessary normalization of `color` for form controls.
- Removed: Unnecessary `box-sizing` for `input[type="search"]` in Chrome, Edge,
  Firefox, IE, and Safari.
- Removed: Opinionated table resets.
- Removed: Opinionated `pre` overflow.
- Removed: Selector weight from some input selectors.
- Updated: Normalization of `border-style` for `img`.
- Updated: Normalization of `color` inheritance for `legend`.
- Updated: Normalization of `background-color` for `mark`.
- Updated: Normalization of `outline` for `:-moz-focusring` removed by a
  previous Normalization in Firefox.
- Updated: Opinionated style of `outline-width` for `a:active` and `a:hover`.
- Updated: Comments to identify opinionated styles.
- Updated: Comments to specify browser/versions affected by all changes.
- Updated: Comments to use one voice.
- Fixed: inconsistent `overflow` for `hr` in Edge and IE.
- Fixed: inconsistent `box-sizing` for `hr` in Firefox.
- Fixed: inconsistent `text-decoration` and `border-bottom` for `abbr[title]`
  in Chrome, Edge, Firefox IE, Opera, and Safari.
- Fixed: inheritance and scaling of `font-size` for preformatted text.
- Fixed: `legend` text wrapping not present in Edge and IE.

---

### 3.0.3 (March 30, 2015)

- Added: `main` property.
- Removed: Unnecessary vendor prefixes.

### 3.0.2 (October 4, 2014)

- Added: `menu` element to HTML5 display definitions.
- Changed: alter `background-color` of links in IE 10.

### 3.0.1 (March 27, 2014)

- Added: package.json for npm support.

### 3.0.0 (January 28, 2014)

### 3.0.0-rc.1 (January 26, 2014)

- Added: Explicit tests for each normalization.
- Added: Normalizations for `optgroup`.
- Added: Display for `progress` in IE 8/9.
- Removed: `textarea` alignment modification.
- Removed: `a:focus` outline normalization.
- Removed: default table cell padding.
- Fixed: i18n for `q` element.
- Fixed: `pre` text formatting and overflow.
- Fixed: Vertical alignment of `progress`.
- Fixed: `button` overflow in IE 8/9/10.
- Fixed: number input button cursor in Chrome on OS X.
- Fixed: `figure` margin normalization.
- Fixed: `font` and `color` inheritance for forms.

---

### 2.1.3 (August 26, 2013)

- Fixed: component.json.
- Removed: the gray background color from active links in IE 10.

### 2.1.2 (May 11, 2013)

- Changed: Reverted root `color` and `background` normalizations.

### 2.1.1 (April 8, 2013)

- Added: root `color` and `background` normalizations to counter the effects of
- system color schemes.

### 2.1.0 (January 21, 2013)

- Added: Normalization of `text-transform` for `button` and `select`.
- Added: Normalization of `h1` margin when within HTML5 sectioning elements.
- Added: Normalization of `hr` element.
- Added: `main` element to HTML5 display definitions.
- Removed: unnecessary `pre` styles.
- Fixed: cursor style for disabled button `input`.

### 2.0.1 (August 20, 2012)

- Removed: stray IE 6/7 `inline-block` hack from HTML5 display settings.

### 2.0.0 (August 19, 2012)

- Removed: Legacy browser form normalizations.
- Removed: List normalizations.
- Removed: heading normalizations except `h1` font size.
- Removed: Support for IE 6/7, Firefox < 4, and Safari < 5.
- Added: `quotes` normalizations.
- Changed: Form elements automatically inherit `font-family` from ancestor.

---

### 1.0.1 (August 19, 2012)

- Changed: Adjusted `small` font size normalization.

### 1.0.0 (August 14, 2012)

- Added: MIT License.
- Added: Hide `audio` elements without controls in iOS 5.
- Added: Heading margins and font size.
- Removed: scrollbar normalization.
- Removed: excess padding from checkbox and radio inputs in IE 7.
- Changed: Moved font-family normalization from `body` to `html`.
- Added: IE9 correction for SVG overflow.
- Added: Fix for legend not inheriting color in IE 6/7/8/9.

### Prehistory

- Initial version

```

### File: CONTRIBUTING.md
```md
# Contributing to normalize.css

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
   git clone git@github.com:YOUR_USER/normalize.css.git

   # Navigate to the newly cloned directory
   cd normalize.css

   # Assign the original repo to a remote called "upstream"
   git remote add upstream git@github.com:csstools/normalize.css.git

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
   1. Copy the latest normalize.css and test.html from the master branch into
      the root directory, the `latest` directory, and a new directory named
      after the new version: `0.0.0`.
   2. Update the normalize.css version and supported browsers in `index.html`.

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

[already been reported]: https://github.com/csstools/normalize.css/issues
[fork this project]:     https://github.com/csstools/normalize.css/fork
[live example]:          https://codepen.io/pen
[open a pull request]:   https://help.github.com/articles/using-pull-requests/
[reduced test case]:     https://css-tricks.com/reduced-test-cases/

```

### File: LICENSE.md
```md
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

### File: normalize.css
```css
/* Document
 * ========================================================================== */

/**
 * 1. Correct the line height in all browsers.
 * 2. Prevent adjustments of font size after orientation changes in iOS.
 */

:where(html) {
  line-height: 1.15; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
  text-size-adjust: 100%; /* 2 */
}

/* Sections
 * ========================================================================== */

/**
 * Correct the font size and margin on `h1` elements within `section` and
 * `article` contexts in Chrome, Edge, Firefox, and Safari.
 */

:where(h1) {
  font-size: 2em;
  margin-block-end: 0.67em;
  margin-block-start: 0.67em;
}

/* Grouping content
 * ========================================================================== */

/**
 * Remove the margin on nested lists in Chrome, Edge, and Safari.
 */

:where(dl, ol, ul) :where(dl, ol, ul) {
  margin-block-end: 0;
  margin-block-start: 0;
}

/**
 * Add the correct box sizing in Firefox.
 */

:where(hr) {
  box-sizing: content-box;
  height: 0;
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

:where(code, kbd, pre, samp) {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
 * Add the correct font size in all browsers.
 */

:where(small) {
  font-size: 80%;
}

/* Tabular data
 * ========================================================================== */

/**
 * Correct table border color in Chrome, Edge, and Safari.
 */

:where(table) {
  border-color: currentColor;
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
 * Remove the inheritance of text transform in Firefox.
 */

:where(button) {
  text-transform: none;
}

/**
 * Correct the inability to style buttons in iOS and Safari.
 */

:where(button, input:is([type="button" i], [type="reset" i], [type="submit" i])) {
  -webkit-appearance: button;
}

/**
 * Add the correct vertical alignment in Chrome, Edge, and Firefox.
 */

:where(progress) {
  vertical-align: baseline;
}

/**
 * Remove the inheritance of text transform in Firefox.
 */

:where(select) {
  text-transform: none;
}

/**
 * Remove the margin in Firefox and Safari.
 */

:where(textarea) {
  margin: 0;
}

/**
 * 1. Correct the odd appearance in Chrome, Edge, and Safari.
 * 2. Correct the outline style in Safari.
 */

:where(input[type="search" i]) {
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

/**
 * Remove the inner border and padding of focus outlines in Firefox.
 */

:where(button, input:is([type="button" i], [type="color" i], [type="reset" i], [type="submit" i]))::-moz-focus-inner {
  border-style: none;
  padding: 0;
}

/**
 * Restore the focus outline styles unset by the previous rule in Firefox.
 */

:where(button, input:is([type="button" i], [type="color" i], [type="reset" i], [type="submit" i]))::-moz-focusring {
  outline: 1px dotted ButtonText;
}

/**
 * Remove the additional :invalid styles in Firefox.
 */

:where(:-moz-ui-invalid) {
  box-shadow: none;
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
 * Add the correct display in all browsers.
 */

:where(summary) {
  display: list-item;
}

```

### File: opinionated.css
```css
/* Document
 * ========================================================================== */

/**
 * 1. Correct the line height in all browsers.
 * 2. Prevent adjustments of font size after orientation changes in iOS.
 */

:where(html) {
  line-height: 1.15; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
  text-size-adjust: 100%; /* 2 */
}

/* Sections
 * ========================================================================== */

/**
 * Remove the margin in all browsers. (opinionated)
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
  margin-block-end: 0.67em;
  margin-block-start: 0.67em;
}

/* Grouping content
 * ========================================================================== */

/**
 * Remove the margin on nested lists in Chrome, Edge, and Safari.
 */

:where(dl, ol, ul) :where(dl, ol, ul) {
  margin-block-end: 0;
  margin-block-start: 0;
}

/**
 * Add the correct box sizing in Firefox.
 */

:where(hr) {
  box-sizing: content-box;
  height: 0;
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

:where(code, kbd, pre, samp) {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
 * Add the correct font size in all browsers.
 */

:where(small) {
  font-size: 80%;
}

/* Tabular data
 * ========================================================================== */

/**
 * Correct table border color in Chrome, Edge, and Safari.
 */

:where(table) {
  border-color: currentColor;
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
 * Remove the inheritance of text transform in Firefox.
 */

:where(button) {
  text-transform: none;
}

/**
 * Correct the inability to style buttons in iOS and Safari.
 */

:where(button, input:is([type="button" i], [type="reset" i], [type="submit" i])) {
  -webkit-appearance: button;
}

/**
 * Add the correct vertical alignment in Chrome, Edge, and Firefox.
 */

:where(progress) {
  vertical-align: baseline;
}

/**
 * Remove the inheritance of text transform in Firefox.
 */

:where(select) {
  text-transform: none;
}

/**
 * Remove the margin in Firefox and Safari.
 */

:where(textarea) {
  margin: 0;
}

/**
 * 1. Correct the odd appearance in Chrome, Edge, and Safari.
 * 2. Correct the outline style in Safari.
 */

:where(input[type="search" i]) {
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

/**
 * Remove the inner border and padding of focus outlines in Firefox.
 */

:where(button, input:is([type="button" i], [type="color" i], [type="reset" i], [type="submit" i]))::-moz-focus-inner {
  border-style: none;
  padding: 0;
}

/**
 * Restore the focus outline styles unset by the previous rule in Firefox.
 */

:where(button, input:is([type="button" i], [type="color" i], [type="reset" i], [type="submit" i]))::-moz-focusring {
  outline: 1px dotted ButtonText;
}

/**
 * Remove the additional :invalid styles in Firefox.
 */

:where(:-moz-ui-invalid) {
  box-shadow: none;
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
 * Add the correct display in all browsers.
 */

:where(summary) {
  display: list-item;
}

```

### File: package-lock.json
```json
{
  "name": "@csstools/normalize.css",
  "version": "12.1.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "@csstools/normalize.css",
      "version": "12.1.1",
      "license": "CC0-1.0"
    }
  }
}

```

### File: SECURITY.md
```md
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

### File: test.html
```html
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>normalize.css: tests</title>
<script src="https://rawgit.com/aFarkas/html5shiv/gh-pages/dist/html5shiv.min.js"></script>
<link rel="stylesheet" href="normalize.css">
<style>
  /*! suit-test v0.1.0 | MIT License | github.com/suitcss */

  .Test {
    background: #fff;
    counter-reset: test-describe;
  }

  .Test-describe::before {
    content: counter(test-describe);
    counter-increment: test-describe;
  }

  .Test-describe {
    counter-reset: test-it;
    font-size: 1.5em;
    margin: 60px 0 20px;
  }

  .Test-it::before {
    content: counter(test-describe) "." counter(test-it);
    counter-increment: test-it;
  }

  .Test-title {
    font-size: 2em;
    font-family: sans-serif;
    padding: 20px;
    margin: 20px 0;
    background: #eee;
    color: #999;
  }

  .Test-describe,
  .Test-it {
    background: #eee;
    border-left: 5px solid #666;
    color: #666;
    font-family: sans-serif;
    font-weight: bold;
    margin: 20px 0;
    padding: 0.75em 20px;
  }

  .Test-describe::before,
  .Test-it::before {
    color: #999;
    display: inline-block;
    margin-right: 10px;
    min-width: 30px;
    text-transform: uppercase;
  }

  /**
   * Highlight the bounds of direct children of a test block
   */

  .Test-run--highlightEl > * {
    outline: 1px solid #add8e6;
  }
</style>

<div class="Test">
  <h1 class="Test-title"><a href="https://github.com/csstools/normalize.css">normalize.css</a>: tests</h1>

  <h2 class="Test-describe"><code>html</code></h2>
  <h3 class="Test-it">should have a line height of 1.15</h3>
  <div class="Test-run">
    abcdefghijklmnopqrstuvwxyz
  </div>
  <h3 class="Test-it">should not adjust font size after orientation changes</h3>
  <div class="Test-run">
    abcdefghijklmnopqrstuvwxyz
  </div>

  <h2 class="Test-describe"><code>h1</code></h2>
  <h3 class="Test-it">should not change size within an <code>article</code> or <code>section</code></h3>
  <div class="Test-run">
    <h1>Heading (control)</h1>
    <article>
      <h1>Heading (in article)</h1>
    </article>
    <section>
      <h1>Heading (in section)</h1>
    </section>
  </div>

  <h2 class="Test-describe"><code>hr</code></h2>
  <h3 class="Test-it">should have a <code>content-box</code> box model</h3>
  <div class="Test-run">
    <hr style="height:2px; border:solid #add8e6; border-width:2px 0;">
  </div>

  <h2 class="Test-describe"><code>main</code></h2>
  <h3 class="Test-it">should display as block</h3>
  <div class="Test-run Test-run--highlightEl">
    <main>main</main>
  </div>

  <h2 class="Test-describe"><code>pre</code></h2>
  <h3 class="Test-it">should render text at the same absolute size as normal text</h3>
  <div class="Test-run">
    <span>span: abcdefghijklmnopqrstuvwxyz.</span><br>
    <pre>pre: abcdefghijklmnopqrstuvwxyz.</pre>
  </div>

  <h2 class="Test-describe"><code>a</code></h2>
  <h3 class="Test-it">should have a transparent background when active</h3>
  <div class="Test-run">
    <a href="#non">dummy anchor</a>
  </div>

  <h2 class="Test-describe"><code>abbr[title]</code></h2>
  <h3 class="Test-it">should have a dotted underline text decoration with an underline fallback</h3>
  <div class="Test-run">
    <abbr title="abbreviation">abbr</abbr>
  </div>

  <h2 class="Test-describe"><code>b</code>, <code>strong</code></h2>
  <h3 class="Test-it">should have a bolder font-weight</h3>
  <div class="Test-run">
    <p>
      <b>b</b>
      <strong>strong</strong>
    </p>
    <p style="font-weight:300;">
      <b>b</b>
      <strong>strong from font-weight:300</strong>
    </p>
  </div>

  <h2 class="Test-describe"><code>code</code>, <code>kbd</code>, <code>samp</code></h2>
  <h3 class="Test-it">should render text at the same absolute size as normal text</h3>
  <div class="Test-run">
    <span>span: abcdefghijklmnopqrstuvwxyz.</span><br>
    <code>code: abcdefghijklmnopqrstuvwxyz.</code><br>
    <kbd>kbd: abcdefghijklmnopqrstuvwxyz.</kbd><br>
    <samp>samp: abcdefghijklmnopqrstuvwxyz.</samp>
  </div>

  <h2 class="Test-describe"><code>small</code></h2>
  <h3 class="Test-it">should render equally small in all browsers</h3>
  <div class="Test-run">
    control. <small>small.</small>
  </div>

  <h2 class="Test-describe"><code>audio</code>, <code>video</code></h2>
  <h3 class="Test-it">should display as inline-block</h3>
  <div class="Test-run">
    <audio controls></audio>
    <video controls></video>
  </div>

  <h2 class="Test-describe"><code>audio</code></h2>
  <h3 class="Test-it">should not display</h3>
  <div class="Test-run">
    <audio></audio>
  </div>

  <h2 class="Test-describe"><code>img</code></h2>
  <h3 class="Test-it">should not have a border when wrapped in an anchor</h3>
  <div class="Test-run">
    <a href="#non">
      <!-- scaled-up 1px image -->
      <img style="background-color:#add8e6; vertical-align:top;" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="100" height="100">
    </a>
  </div>

  <h2 class="Test-describe"><code>svg</code></h2>
  <h3 class="Test-it">should not overflow</h3>
  <div class="Test-run Test-run--highlightEl">
    <svg width="100px" height="100px">
      <circle cx="100" cy="100" r="100" fill="#add8e6" />
    </svg>
  </div>

  <h2 class="Test-describe"><code>button</code>, <code>input</code>, <code>optgroup</code>, <code>select</code>, <code>textarea</code></h2>
  <h3 class="Test-it">should have no margin</h3>
  <div class="Test-run">
    <button>button</button><br>
    <input value="input"><br>
    <select style="border:1px solid #999;">
      <optgroup label="optgroup">
        <option>option</option>
      </optgroup>
      <option>option</option>
    </select><br>
    <textarea>textarea</textarea>
  </div>

  <h2 class="Test-describe"><code>button</code></h2>
  <h3 class="Test-it">should have visible overflow</h3>
  <div class="Test-run" id="button-overflow">
    <style>
      #button-overflow button:after {
        content: "";
        background: #add8e6;
        display: inline-block;
        height: 10px;
        position: relative;
        right: -20px;
        width: 10px;
      }
    </style>
    <button>abcdefghijklmnopqrstuvwxyz</button>
  </div>

  <h2 class="Test-describe"><code>button</code></h2>
  <h3 class="Test-it">should not inherit <code>text-transform</code></h3>
  <div class="Test-run" style="text-transform:uppercase;">
    <button>button</button>
  </div>

  <h2 class="Test-describe"><code>button</code> and button-style <code>input</code></h2>
  <h3 class="Test-it">should be styleable</h3>
  <div class="Test-run" id="button-like-style">
    <style>
      #button-like-style button,
      #button-like-style input {
        background: #add8e6;
        border: 2px solid black;
        border-radius: 2px;
        padding: 5px;
      }
    </style>
    <p><button>button</button></p>
    <p><input type="image" src="//placehold.it/90x24" alt="input (image)"></p>
    <p><input type="button" value="input (button)"></p>
    <p><input type="file" value="input (file)"></p>
    <p><input type="reset" value="input (reset)"></p>
    <p><input type="submit" value="input (submit)"></p>
  </div>

  <h2 class="Test-describe"><code>fieldset</code></h2>
  <h3 class="Test-it">should have consistent border, padding, and margin</h3>
  <div class="Test-run">
    <fieldset>
      <div style="width:100%; height:100px; background:#add8e6;"></div>
    </fieldset>
  </div>

  <h2 class="Test-describe"><code>legend</code></h2>
  <h3 class="Test-it">should wrap text</h3>
  <div class="Test-run">
    <fieldset style="width: 34em;">
      <legend>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et me.</legend>
    </fieldset>
  </div>
  <h3 class="Test-it">should inherit color</h3>
  <div class="Test-run" style="color:#add8e6;">
    <fieldset>
      <legend>legend</legend>
    </fieldset>
  </div>
  <h3 class="Test-it">should not have padding</h3>
  <div class="Test-run">
    <fieldset>
      <legend>legend</legend>
    </fieldset>
  </div>

  <h2 class="Test-describe"><code>progress</code></h2>
  <h3 class="Test-it">should display as inline-block</h3>
  <div class="Test-run">
    <progress value="70" max="100">70%</progress>
  </div>
  <h3 class="Test-it">should have baseline alignment</h3>
  <div class="Test-run">
    abc <progress value="70" max="100">70%</progress> xyz
  </div>

  <h2 class="Test-describe"><code>select</code></h2>
  <h3 class="Test-it">should not inherit <code>text-transform</code></h3>
  <div class="Test-run" style="text-transform:uppercase;">
    <select><option>option</option></select>
  </div>

  <h2 class="Test-describe"><code>textarea</code></h2>
  <h3 class="Test-it">should not have a scrollbar unless overflowing</h3>
  <div class="Test-run">
    <textarea>textarea</textarea>
  </div>

  <h2 class="Test-describe"><code>[type="checkbox"]</code>, <code>[type="radio"]</code></h2>
  <h3 class="Test-it">should have a <code>border-box</code> box model</h3>
  <div class="Test-run Test-run--highlightEl" id="radio-box-model">
    <style>
      #radio-box-model {
        width: 200px;
        border: 1px solid red;
      }

      #radio-box-model input {
        width: 100%;
        border: 5px solid #add8e6;
        display: block;
        position: relative;
      }
    </style>
    <input type="checkbox">
    <input type="radio" name="rad">
  </div>
  <h3 class="Test-it">should not have padding</h3>
  <div class="Test-run Test-run--highlightEl">
    <input type="checkbox">
    <input type="radio" name="rad">
  </div>

  <h2 class="Test-describe"><code>[type="number"]</code></h2>
  <h3 class="Test-it">should display a default cursor for the decrement button's click target in Chrome</h3>
  <div class="Test-run">
    <input style="height:50px; font-size:15px;" type="number" id="in" min="0" max="10" value="5">
  </div>

  <h2 class="Test-describe"><code>[type="search"]</code></h2>
  <h3 class="Test-it">should be styleable</h3>
  <div class="Test-run">
    <input type="search" style="border:1px solid #add8e6; padding:10px; width:200px;">
  </div>

  <h2 class="Test-describe"><code>::placeholder</code></h2>
  <h3 class="Test-it">placeholder should be styleable</h3>
  <div class="Test-run">
    <input type="text" placeholder="placeholder text" style="color: blue;">
  </div>

  <h2 class="Test-describe"><code>::file-upload-button</code></h2>
  <h3 class="Test-it">should be styleable</h3>
  <div class="Test-run">
    <input type="file" style="border:1px solid #add8e6; padding:10px; width:200px;">
  </div>

  <h2 class="Test-describe">::focus-inner, ::focusring</h2>
  <h3 class="Test-it">should not have extra inner padding in Firefox</h3>
  <div class="Test-run" id="button-input-padding">
    <style>
      #button-input-padding button,
      #button-input-padding input {
        padding: 10px 20px;
      }
    </style>
    <p><button>button</button></p>
    <p><input type="button" value="input (button)"></p>
    <p><input type="reset" value="input (reset)"></p>
    <p><input type="submit" value="input (submit)"></p>
  </div>

  <h2 class="Test-describe"><code>details</code></h2>
  <h3 class="Test-it">should display as block</h3>
  <div class="Test-run">
    <details></details>
  </div>

  <h2 class="Test-describe"><code>dialog</code></h2>
  <h3 class="Test-it">should be absolutely positioned</h3>
  <div class="Test-run" style="position:relative; height:3em;">
    <dialog open>dialog</dialog>
  </div>

  <h2 class="Test-describe"><code>summary</code></h2>
  <h3 class="Test-it">should display as list-item</h3>
  <div class="Test-run">
    <details>
      <summary>Summary</summary>
      <p>More information</p>
    </details>
  </div>
</div>

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
