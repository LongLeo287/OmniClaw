---
id: tieske-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.161683
---

# KNOWLEDGE EXTRACT: Tieske
> **Extracted on:** 2026-03-30 17:54:17
> **Source:** Tieske

---

## File: `date.md`
```markdown
# 📦 Tieske/date [🔖 PENDING/APPROVE]
🔗 https://github.com/Tieske/date
🌐 https://tieske.github.io/date/

## Meta
- **Stars:** ⭐ 275 | **Forks:** 🍴 59
- **Language:** Lua | **License:** MIT
- **Last updated:** 2026-02-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Date & Time module for Lua 5.x

## README (trích đầu)
```
# LuaDate v2.2

[![Unix build](https://img.shields.io/github/actions/workflow/status/Tieske/date/unix_build.yml?branch=master&label=Unix%20build&logo=linux)](https://github.com/Tieske/date/actions/workflows/unix_build.yml)
[![Coveralls code coverage](https://img.shields.io/coveralls/github/Tieske/date?logo=coveralls)](https://coveralls.io/github/Tieske/date)
[![Lint](https://github.com/Tieske/date/workflows/Lint/badge.svg)](https://github.com/Tieske/date/actions/workflows/lint.yml)
[![SemVer](https://img.shields.io/github/v/tag/Tieske/date?color=brightgreen&label=SemVer&logo=semver&sort=semver)](CHANGELOG.md)

Lua Date and Time module for Lua 5.x.

## Features:

* Date and Time string parsing.
* Time addition and subtraction.
* Time span calculation.
* Support ISO 8601 Dates.
* Local time support.
* Lua module (not binary).
* Formats Date and Time like strftime.

## License

[MIT license](http://opensource.org/licenses/MIT).

## Documentation

Documentation is available in the `doc` folder, or [online at Github](http://tieske.github.io/date/).

## Tests

Tests are located in the `spec` directory and can be run using [busted](http://olivinelabs.com/busted/).

## Changelog:

### Releasing:
- search for "copyright" and update all occurences with proper years
- update version in:
  - `README.md` (at the top)
  - `date.lua` (at the top, and exported field `date.version`)
  - `index.html` (appr. line 20)
- update changelog below
- update rockspec
- commit as `release x.y.z` (omit trailing 0)
- tag as `version_x.y.z` (omit trailing 0)
- push commit & tags
- upload rock to luarocks

### Changes:

#### v2.2.1 released 6-Sep-2023
  - fix parsing timezone offset after a decimal number [#33](https://github.com/Tieske/date/pull/33)
  - also accept "," as a decimal separator [#31](https://github.com/Tieske/date/pull/31)
  - fix bad function call (no functional impact) [#34](https://github.com/Tieske/date/pull/34)

#### v2.2
  - add 'centuryflip' to set 2 digit year interpretation [#26](https://github.com/Tieske/date/pull/26)
#### v2.1.3
  - fix rockspec for Lua 5.4
#### v2.1.2
  - fix scientific notation [#9](https://github.com/Tieske/date/pull/9), now available for Lua 5.3
#### v2.1.1
  - fix for '>=' operator [#3](https://github.com/Tieske/date/pull/3), added test suite, added Travis CI, license MIT
#### v2.1
  - Lua 5.2 support. Global 'date' will no longer be set.
#### v2.0
  - original by Jas Latrix

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

