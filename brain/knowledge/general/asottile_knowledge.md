---
id: asottile-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:50.688385
---

# KNOWLEDGE EXTRACT: asottile
> **Extracted on:** 2026-03-30 17:29:11
> **Source:** asottile

---

## File: `pyupgrade.md`
```markdown
# 📦 asottile/pyupgrade [🔖 PENDING/APPROVE]
🔗 https://github.com/asottile/pyupgrade


## Meta
- **Stars:** ⭐ 4062 | **Forks:** 🍴 208
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A tool (and pre-commit hook) to automatically upgrade syntax for newer versions of the language.

## README (trích đầu)
```
[![build status](https://github.com/asottile/pyupgrade/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/pyupgrade/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/pyupgrade/main.svg)](https://results.pre-commit.ci/latest/github/asottile/pyupgrade/main)

pyupgrade
=========

A tool (and pre-commit hook) to automatically upgrade syntax for newer
versions of the language.

## Installation

```bash
pip install pyupgrade
```

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/asottile/pyupgrade
    rev: v3.21.2
    hooks:
    -   id: pyupgrade
```

## Implemented features

### Set literals

```diff
-set(())
+set()
-set([])
+set()
-set((1,))
+{1}
-set((1, 2))
+{1, 2}
-set([1, 2])
+{1, 2}
-set(x for x in y)
+{x for x in y}
-set([x for x in y])
+{x for x in y}
```

### Dictionary comprehensions

```diff
-dict((a, b) for a, b in y)
+{a: b for a, b in y}
-dict([(a, b) for a, b in y])
+{a: b for a, b in y}
```

### Replace unnecessary lambdas in `collections.defaultdict` calls

```diff
-defaultdict(lambda: [])
+defaultdict(list)
-defaultdict(lambda: list())
+defaultdict(list)
-defaultdict(lambda: {})
+defaultdict(dict)
-defaultdict(lambda: dict())
+defaultdict(dict)
-defaultdict(lambda: ())
+defaultdict(tuple)
-defaultdict(lambda: tuple())
+defaultdict(tuple)
-defaultdict(lambda: set())
+defaultdict(set)
-defaultdict(lambda: 0)
+defaultdict(int)
-defaultdict(lambda: 0.0)
+defaultdict(float)
-defaultdict(lambda: 0j)
+defaultdict(complex)
-defaultdict(lambda: '')
+defaultdict(str)
```

### Format Specifiers

```diff
-'{0} {1}'.format(1, 2)
+'{} {}'.format(1, 2)
-'{0}' '{1}'.format(1, 2)
+'{}' '{}'.format(1, 2)
```

### printf-style string formatting

Availability:
- Unless `--keep-percent-format` is passed.

```diff
-'%s %s' % (a, b)
+'{} {}'.format(a, b)
-'%r %2f' % (a, b)
+'{!r} {:2f}'.format(a, b)
-'%(a)s %(b)s' % {'a': 1, 'b': 2}
+'{a} {b}'.format(a=1, b=2)
```

### Unicode literals

```diff
-u'foo'
+'foo'
-u"foo"
+'foo'
-u'''foo'''
+'''foo'''
```

### Invalid escape sequences

```diff
 # strings with only invalid sequences become raw strings
-'\d'
+r'\d'
 # strings with mixed valid / invalid sequences get escaped
-'\n\d'
+'\n\\d'
-u'\d'
+r'\d'
 # this fixes a syntax error in python3.3+
-'\N'
+r'\N'
```

### `is` / `is not` comparison to constant literals

In python3.8+, comparison to literals becomes a `SyntaxWarning` as the success
of those comparisons is implementation specific (due to common object caching).

```diff
-x is 5
+x == 5
-x is not 5
+x != 5
-x is 'foo'
+x == 'foo'
```

### `.encode()` to bytes literals

```diff
-'foo'.encode()
+b'foo'
-'foo'.encode('ascii')
+b'foo'
-'foo'.encode('utf-8')
+b'foo'
-u'foo'.encode()
+b'foo'
-'\xa0'.encode('latin1')
+b'\xa0'
```

### extraneous parens in `print(...)`

A fix for [python-modernize/python-modernize#178]

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

