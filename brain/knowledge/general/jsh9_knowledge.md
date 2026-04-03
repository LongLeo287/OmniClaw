---
id: jsh9-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.567155
---

# KNOWLEDGE EXTRACT: jsh9
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jsh9

---

## File: `pydoclint.md`
```markdown
# 📦 jsh9/pydoclint [🔖 PENDING/APPROVE]
🔗 https://github.com/jsh9/pydoclint
🌐 https://pypi.org/project/pydoclint/

## Meta
- **Stars:** ⭐ 207 | **Forks:** 🍴 22
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A very fast Python docstring linter

## README (trích đầu)
```
# pydoclint

[![Downloads](https://static.pepy.tech/badge/pydoclint)](https://pepy.tech/project/pydoclint)
[![Downloads](https://static.pepy.tech/badge/pydoclint/month)](https://pepy.tech/project/pydoclint)
[![Downloads](https://static.pepy.tech/badge/pydoclint/week)](https://pepy.tech/project/pydoclint)

_Pydoclint_ is a Python docstring linter to check whether a docstring's
sections (arguments, returns, raises, ...) match the function signature or
function implementation.

It runs really fast. In fact, it can be thousands of times faster than
[darglint](https://github.com/terrencepreilly/darglint) (or its maintained fork
[darglint2](https://github.com/akaihola/darglint2)).

Here is a comparison of linting time on some famous Python projects:

|                                                              | pydoclint | darglint                          |
| ------------------------------------------------------------ | --------- | --------------------------------- |
| [numpy](https://github.com/numpy/numpy)                      | 2.0 sec   | 49 min 9 sec (1,475x slower)      |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 2.4 sec   | 3 hr 5 min 33 sec (4,639x slower) |

Additionally, _pydoclint_ can detect quite a few style violations that darglint
cannot.

Currently, _pydoclint_ supports three docstring styles:
[numpy](https://numpydoc.readthedocs.io/en/latest/format.html),
[Google](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html),
and
[Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html),
with some
[minor style deviations](https://jsh9.github.io/pydoclint/style_deviations.html).

Another note: this linter and [pydocstyle](https://github.com/PyCQA/pydocstyle)
serves complementary purposes. It is recommended that you use both together.

The full documentation of _pydoclint_ (including this README) can be found
here: [https://jsh9.github.io/pydoclint](https://jsh9.github.io/pydoclint)

The corresponding Github repository of _pydoclint_ is:
[https://github.com/jsh9/pydoclint](https://github.com/jsh9/pydoclint)

<!--TOC-->

______________________________________________________________________

**Table of Contents**

- [1. Installation](#1-installation)
- [2. Usage](#2-usage)
  - [2.1. As a native command line tool](#21-as-a-native-command-line-tool)
  - [2.2. As a _flake8_ plugin](#22-as-a-flake8-plugin)
  - [2.3. Native vs _flake8_](#23-native-vs-flake8)
  - [2.4. As a pre-commit hook](#24-as-a-pre-commit-hook)
    - [2.4.1. Native mode](#241-native-mode)
    - [2.4.2. As a _flake8_ plugin](#242-as-a-flake8-plugin)
  - [2.5. How to configure _pydoclint_](#25-how-to-configure-pydoclint)
  - [2.6. How to ignore certain violations](#26-how-to-ignore-certain-violations)
  - [2.7. Additional tips, tricks, and pitfalls](#27-additional-tips-tricks-and-pitfalls)
    - [2.7.1. How to _not_ document certain functions?](#271-how-to-not-document-certain-functions)
    - [2.7.2. How to gradu
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

