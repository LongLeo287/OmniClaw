---
id: netromdk-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.381863
---

# KNOWLEDGE EXTRACT: netromdk
> **Extracted on:** 2026-03-30 17:49:10
> **Source:** netromdk

---

## File: `vermin.md`
```markdown
# 📦 netromdk/vermin [🔖 PENDING/APPROVE]
🔗 https://github.com/netromdk/vermin


## Meta
- **Stars:** ⭐ 513 | **Forks:** 🍴 28
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-16
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Concurrently detect the minimum Python versions needed to run code

## README (trích đầu)
```
|Test Status| |Analyze Status| |CodeQL Status| |Coverage| |PyPI version| |Commits since last| |Downloads| |CII best practices|

.. |PyPI version| image:: https://badge.fury.io/py/vermin.svg
   :target: https://pypi.python.org/pypi/vermin/

.. |Test Status| image:: https://github.com/netromdk/vermin/workflows/Test/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/actions

.. |Analyze Status| image:: https://github.com/netromdk/vermin/workflows/Analyze/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/actions

.. |CodeQL Status| image:: https://github.com/netromdk/vermin/workflows/CodeQL/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/security/code-scanning

.. |Snyk Status| image:: https://github.com/netromdk/vermin/workflows/Snyk%20Schedule/badge.svg?branch=master
   :target: https://github.com/netromdk/vermin/actions

.. |Coverage| image:: https://coveralls.io/repos/github/netromdk/vermin/badge.svg?branch=master
   :target: https://coveralls.io/github/netromdk/vermin?branch=master

.. |Commits since last| image:: https://img.shields.io/github/commits-since/netromdk/vermin/latest.svg

.. |Downloads| image:: https://static.pepy.tech/personalized-badge/vermin?period=total&units=international_system&left_color=gray&right_color=blue&left_text=Downloads
   :target: https://pepy.tech/project/vermin

.. |CII best practices| image:: https://bestpractices.coreinfrastructure.org/projects/6451/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/6451

Vermin
******

Concurrently detect the minimum Python versions needed to run code. Additionally, since the code is
vanilla Python, and it doesn't have any external dependencies, it can be run with v3+ but still
includes detection of v2.x functionality.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and
matches against internal dictionaries with **4140** rules, covering v2.0-2.7 and v3.0-3.14, divided
into **190** modules, **2888** classes/functions/constants members of modules, **932** kwargs of
functions, **4** strftime directives, **3** bytes format directives, **3** array typecodes, **3**
codecs error handler names, **20** codecs encodings, **78** builtin generic annotation types, **9**
builtin dict union (``|``) types, **8** builtin dict union merge (``|=``) types, and **2** user
function decorators.

Backports of the standard library, like ``typing``, can be enabled for better results. Get full list
of backports via ``--help``.

The project is fairly well-tested with **4362** unit and integration tests that are executed on
Linux, macOS, and Windows.

It is recommended to use the most recent Python version to run Vermin on projects since Python's own
language parser is used to detect language features, like f-strings since Python 3.6 etc.


Table of Contents
=================

* `Usage <#usage>`__
* `Features <#features>`__
* `Caveats <#caveats>`__
* `Configuration File <#configu
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

