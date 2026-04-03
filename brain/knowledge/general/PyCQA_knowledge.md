---
id: pycqa-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:04.073848
---

# KNOWLEDGE EXTRACT: PyCQA
> **Extracted on:** 2026-03-30 17:51:30
> **Source:** PyCQA

---

## File: `bandit.md`
```markdown
# 📦 PyCQA/bandit [🔖 PENDING/APPROVE]
🔗 https://github.com/PyCQA/bandit
🌐 https://bandit.readthedocs.io

## Meta
- **Stars:** ⭐ 7887 | **Forks:** 🍴 744
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Bandit is a tool designed to find common security issues in Python code.

## README (trích đầu)
```
.. image:: https://raw.githubusercontent.com/pycqa/bandit/main/logo/logotype-sm.png
    :alt: Bandit

======

.. image:: https://github.com/PyCQA/bandit/actions/workflows/pythonpackage.yml/badge.svg?branch=main
    :target: https://github.com/PyCQA/bandit/actions?query=workflow%3A%22Build+and+Test+Bandit%22+branch%3Amain
    :alt: Build Status

.. image:: https://readthedocs.org/projects/bandit/badge/?version=latest
    :target: https://readthedocs.org/projects/bandit/
    :alt: Docs Status

.. image:: https://img.shields.io/pypi/v/bandit.svg
    :target: https://pypi.org/project/bandit/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/bandit.svg
    :target: https://pypi.org/project/bandit/
    :alt: Python Versions

.. image:: https://img.shields.io/pypi/format/bandit.svg
    :target: https://pypi.org/project/bandit/
    :alt: Format

.. image:: https://img.shields.io/badge/license-Apache%202-blue.svg
    :target: https://github.com/PyCQA/bandit/blob/main/LICENSE
    :alt: License

.. image:: https://img.shields.io/discord/825463413634891776.svg
    :target: https://discord.gg/qYxpadCgkx
    :alt: Discord

A security linter from PyCQA

* Free software: Apache license
* Documentation: https://bandit.readthedocs.io/en/latest/
* Source: https://github.com/PyCQA/bandit
* Bugs: https://github.com/PyCQA/bandit/issues
* Contributing: https://github.com/PyCQA/bandit/blob/main/CONTRIBUTING.md

Overview
--------

Bandit is a tool designed to find common security issues in Python code. To do
this Bandit processes each file, builds an AST from it, and runs appropriate
plugins against the AST nodes. Once Bandit has finished scanning all the files
it generates a report.

Bandit was originally developed within the OpenStack Security Project and
later rehomed to PyCQA.

.. image:: https://raw.githubusercontent.com/pycqa/bandit/main/bandit-terminal.png
    :alt: Bandit Example Screen Shot

Show Your Style
---------------

.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

Use our badge in your project's README!

using Markdown::

    [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

using RST::

    .. image:: https://img.shields.io/badge/security-bandit-yellow.svg
        :target: https://github.com/PyCQA/bandit
        :alt: Security Status

References
----------

Python AST module documentation: https://docs.python.org/3/library/ast.html

Green Tree Snakes - the missing Python AST docs:
https://greentreesnakes.readthedocs.org/en/latest/

Documentation of the various types of AST nodes that Bandit currently covers
or could be extended to cover:
https://greentreesnakes.readthedocs.org/en/latest/nodes.html

Container Images
----------------

Bandit is available as a container image, built within the bandit repository
using GitHub Actions. The image is available on ghcr.io:

.. code-bloc
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `flake8.md`
```markdown
# 📦 PyCQA/flake8 [🔖 PENDING/APPROVE]
🔗 https://github.com/PyCQA/flake8
🌐 https://flake8.pycqa.org

## Meta
- **Stars:** ⭐ 3773 | **Forks:** 🍴 342
- **Language:** Python | **License:** NOASSERTION
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
flake8 is a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.

## README (trích đầu)
```
.. image:: https://github.com/PyCQA/flake8/workflows/main/badge.svg
   :target: https://github.com/PyCQA/flake8/actions?query=workflow%3Amain
   :alt: build status

.. image:: https://results.pre-commit.ci/badge/github/PyCQA/flake8/main.svg
   :target: https://results.pre-commit.ci/latest/github/PyCQA/flake8/main
   :alt: pre-commit.ci status

.. image:: https://img.shields.io/discord/825463413634891776.svg
   :target: https://discord.gg/qYxpadCgkx
   :alt: Discord

========
 Flake8
========

Flake8 is a wrapper around these tools:

- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching the single ``flake8`` command.
It displays the warnings in a per-file, merged output.

It also adds a few features:

- files that contain this line are skipped::

    # flake8: noqa

- lines that contain a ``# noqa`` comment at the end will not issue warnings.
- you can ignore specific errors on a line with ``# noqa: <error>``, e.g.,
  ``# noqa: E234``. Multiple codes can be given, separated by comma. The ``noqa`` token is case insensitive, the colon before the list of codes is required otherwise the part after ``noqa`` is ignored
- Git and Mercurial hooks
- extendable through ``flake8.extension`` and ``flake8.formatting`` entry
  points


Quickstart
==========

See our `quickstart documentation
<https://flake8.pycqa.org/en/latest/index.html#quickstart>`_ for how to install
and get started with Flake8.


Frequently Asked Questions
==========================

Flake8 maintains an `FAQ <https://flake8.pycqa.org/en/latest/faq.html>`_ in its
documentation.


Questions or Feedback
=====================

If you have questions you'd like to ask the developers, or feedback you'd like
to provide, feel free to use the mailing list: code-quality@python.org

We would love to hear from you. Additionally, if you have a feature you'd like
to suggest, the mailing list would be the best place for it.


Links
=====

* `Flake8 Documentation <https://flake8.pycqa.org/en/latest/>`_

* `GitHub Project <https://github.com/pycqa/flake8>`_

* `All (Open and Closed) Issues
  <https://github.com/pycqa/flake8/issues?q=is%3Aissue>`_

* `Code-Quality Archives
  <https://mail.python.org/mailman/listinfo/code-quality>`_

* `Code of Conduct
  <https://flake8.pycqa.org/en/latest/internal/contributing.html#code-of-conduct>`_

* `Getting Started Contributing
  <https://flake8.pycqa.org/en/latest/internal/contributing.html>`_


Maintenance
===========

Flake8 was created by Tarek Ziadé and is currently maintained by `anthony sottile
<https://github.com/sponsors/asottile>`_ and `Ian Cordasco
<https://www.coglib.com/~icordasc/>`_

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `isort.md`
```markdown
# 📦 PyCQA/isort [🔖 PENDING/APPROVE]
🔗 https://github.com/PyCQA/isort
🌐 https://pycqa.github.io/isort/

## Meta
- **Stars:** ⭐ 6925 | **Forks:** 🍴 620
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Python utility / library to sort imports.

## README (trích đầu)
```
[![isort - isort your imports, so you don't have to.](https://raw.githubusercontent.com/pycqa/isort/main/art/logo_large.png)](https://pycqa.github.io/isort/)

------------------------------------------------------------------------

[![PyPI version](https://badge.fury.io/py/isort.svg)](https://badge.fury.io/py/isort)
[![Python Version](https://img.shields.io/pypi/pyversions/isort)][pypi status]
[![Test](https://github.com/PyCQA/isort/actions/workflows/test.yml/badge.svg)](https://github.com/PyCQA/isort/actions/workflows/test.yml)
[![Lint](https://github.com/PyCQA/isort/actions/workflows/lint.yml/badge.svg)](https://github.com/PyCQA/isort/actions/workflows/lint.yml)
[![Code coverage Status](https://codecov.io/gh/pycqa/isort/branch/main/graph/badge.svg)](https://codecov.io/gh/pycqa/isort)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/isort/)
[![Downloads](https://pepy.tech/badge/isort)](https://pepy.tech/project/isort)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/pycqa/isort/?ref=repository-badge)

[pypi status]: https://pypi.org/project/isort/
_________________

[Read Latest Documentation](https://pycqa.github.io/isort/) - [Browse GitHub Code Repository](https://github.com/pycqa/isort/)
_________________

# isort your imports, so you don't have to.

isort is a Python utility / library to sort imports alphabetically and
automatically separate into sections and by type. It provides a command line
utility, Python library and [plugins for various
editors](https://github.com/pycqa/isort/wiki/isort-Plugins) to
quickly sort all your imports. It requires Python 3.10+ to run but
supports formatting Python 2 code too.

- [Try isort now from your browser!](https://pycqa.github.io/isort/docs/quick_start/0.-try.html)
- [Using black? See the isort and black compatibility guide.](https://pycqa.github.io/isort/docs/configuration/black_compatibility.html)
- [isort has official support for pre-commit!](https://pycqa.github.io/isort/docs/configuration/pre-commit.html)

![Example Usage](https://raw.github.com/pycqa/isort/main/example.gif)

Before isort:

```python
from my_lib import Object

import os

from my_lib import Object3

from my_lib import Object2

import sys

from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

import sys

from __future__ import absolute_import

from third_party import lib3

print("Hey")
print("yo")
```

After isort:

```python
from __future__ import absolute_import

import os
import sys

from third_party import (lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8,
                         lib9, lib10, lib11, lib12, lib13, lib14
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

