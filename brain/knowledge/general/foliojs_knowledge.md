---
id: foliojs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.372812
---

# KNOWLEDGE EXTRACT: foliojs
> **Extracted on:** 2026-03-30 17:37:22
> **Source:** foliojs

---

## File: `linebreak.md`
```markdown
# 📦 foliojs/linebreak [🔖 PENDING/APPROVE]
🔗 https://github.com/foliojs/linebreak


## Meta
- **Stars:** ⭐ 227 | **Forks:** 🍴 45
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A JS implementation of the Unicode Line Breaking Algorithm (UAX #14)

## README (trích đầu)
```
# linebreak
An implementation of the Unicode Line Breaking Algorithm (UAX #14)

> Line breaking, also known as word wrapping, is the process of breaking a section of text into lines such that it will fit in the
> available width of a page, window or other display area. The Unicode Line Breaking Algorithm performs part of this process.
> Given an input text, it produces a set of positions called "break opportunities" that are appropriate points to begin a new line.
> The selection of actual line break positions from the set of break opportunities is not covered by the Unicode Line Breaking Algorithm,
> but is in the domain of higher level software with knowledge of the available width and the display size of the text.

This is a JavaScript implementation of the [Unicode Line Breaking Algorithm](http://www.unicode.org/reports/tr14/#SampleCode) for Node.js
(and browsers I guess). Currently supports Unicode version 13. It is used by [PDFKit](http://github.com/devongovett/pdfkit/) for
line wrapping text in PDF documents, but since the algorithm knows nothing about the actual visual appearance or layout of text,
it could be used for other things as well.

## Installation

You can install via npm

    npm install linebreak

## Example

```javascript
var LineBreaker = require('linebreak');

var lorem = 'lorem ipsum...';
var breaker = new LineBreaker(lorem);
var last = 0;
var bk;

while (bk = breaker.nextBreak()) {
  // get the string between the last break and this one
  var word = lorem.slice(last, bk.position);
  console.log(word);

  // you can also check bk.required to see if this was a required break...
  if (bk.required) {
    console.log('\n\n');
  }

  last = bk.position;
}
```

## Development Notes

In order to use the library, you shouldn't need to know this, but if you're interested in
contributing or fixing bugs, these things might be of interest.

* The `src/classes.js` file is automatically generated from `LineBreak.txt` in the Unicode
  database by `src/generate_data.js`. It should be rare that you need to run this, but
  you may if, for instance, you want to change the Unicode version.

* You can run the tests using `npm test`. They are written using `mocha`, and generated from
  `LineBreakTest.txt` from the Unicode database, which is included in the repository for performance
  reasons while running them. About 50 of the over 7600 tests are currently skipped due to
  implementation differences. It appears that some of the tests may be wrong or use different
  tailoring from the spec. To update the `LineBreakTest.txt` file, use the script
  `test/update_test_file.js`, which downloads and updates the tests for the new Unicode version.

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

