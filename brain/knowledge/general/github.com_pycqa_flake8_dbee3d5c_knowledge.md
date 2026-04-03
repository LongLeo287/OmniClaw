---
id: github.com-pycqa-flake8-dbee3d5c-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:15.668642
---

# KNOWLEDGE EXTRACT: github.com_pycqa_flake8_dbee3d5c
> **Extracted on:** 2026-04-01 08:32:08
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519612/github.com_pycqa_flake8_dbee3d5c

---

## File: `.bandit.yml`
```yaml
skips:
- B101  # Ignore defensive `assert`s (especially useful for mypy)
- B404  # Ignore warnings about importing subprocess
- B603  # Ignore warnings about calling subprocess.Popen without shell=True
- B607  # Ignore warnings about calling subprocess.Popen without a full path to executable
```

## File: `.gitignore`
```
*.egg
*.egg-info
*.log
*.pyc
*.sw*
*.zip
.cache
.coverage
.coverage.*
.eggs
.tox
/.mypy_cache
build
dist
docs/build/html/*
```

## File: `.mailmap`
```
Ian Stapleton Cordasco <graffatcolmingov@gmail.com> Ian Cordasco <graffatcolmingov@gmail.com>
Ian Stapleton Cordasco <graffatcolmingov@gmail.com> Ian Cordasco <sigmavirus24@users.noreply.github.com>
Ian Stapleton Cordasco <graffatcolmingov@gmail.com> Ian Cordasco <ian.cordasco@rackspace.com>
Ian Stapleton Cordasco <graffatcolmingov@gmail.com> Ian Cordasco <icordasc+bitbucket@coglib.com>
```

## File: `.pre-commit-config.yaml`
```yaml
repos:
-   repo: https://github.com/asottile/add-trailing-comma
    rev: v4.0.0
    hooks:
    -   id: add-trailing-comma
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
    -   id: check-yaml
    -   id: debug-statements
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
        exclude: ^tests/fixtures/
-   repo: https://github.com/asottile/setup-cfg-fmt
    rev: v3.2.0
    hooks:
    -   id: setup-cfg-fmt
-   repo: https://github.com/asottile/reorder-python-imports
    rev: v3.16.0
    hooks:
    -   id: reorder-python-imports
        args: [
            --application-directories, '.:src',
            --py310-plus,
            --add-import, 'from __future__ import annotations',
        ]
-   repo: https://github.com/asottile/pyupgrade
    rev: v3.21.2
    hooks:
    -   id: pyupgrade
        args: [--py310-plus]
-   repo: https://github.com/hhatto/autopep8
    rev: v2.3.2
    hooks:
    -   id: autopep8
-   repo: https://github.com/PyCQA/flake8
    rev: 7.3.0
    hooks:
    -   id: flake8
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.19.1
    hooks:
    -   id: mypy
        exclude: ^(docs/|example-plugin/)
```

## File: `.pre-commit-hooks.yaml`
```yaml
-   id: flake8
    name: flake8
    description: '`flake8` is a command-line utility for enforcing style consistency across Python projects.'
    entry: flake8
    language: python
    types: [python]
    require_serial: true
```

## File: `.pylintrc`
```
[MASTER]

# Specify a configuration file.
#rcfile=

# Python code to execute, usually for sys.path manipulation such as
# pygtk.require().
#init-hook=

# Add files or directories to the blacklist. They should be base names, not
# paths.
ignore=CVS,.git,flake8.egg-info

# Pickle collected data for later comparisons.
persistent=yes

# List of plugins (as comma separated values of python modules names) to load,
# usually to register additional checkers.
load-plugins=

# Use multiple processes to speed up Pylint.
jobs=4

# Allow loading of arbitrary C extensions. Extensions are imported into the
# active Python interpreter and may run arbitrary code.
unsafe-load-any-extension=no

# A comma-separated list of package or module names from where C extensions may
# be loaded. Extensions are loading into the active Python interpreter and may
# run arbitrary code
extension-pkg-whitelist=

# Allow optimization of some AST trees. This will activate a peephole AST
# optimizer, which will apply various small optimizations. For instance, it can
# be used to obtain the result of joining multiple strings with the addition
# operator. Joining a lot of strings can lead to a maximum recursion error in
# Pylint and this flag can prevent that. It has one side effect, the resulting
# AST will be different than the one from reality.
optimize-ast=no


[MESSAGES CONTROL]

# Only show warnings with the listed confidence levels. Leave empty to show
# all. Valid levels: HIGH, INFERENCE, INFERENCE_FAILURE, UNDEFINED
confidence=INFERENCE_FAILURE

# Enable the message, report, category or checker with the given id(s). You can
# either give multiple identifier separated by comma (,) or put this option
# multiple time. See also the "--disable" option for examples.
#enable=

# Disable the message, report, category or checker with the given id(s). You
# can either give multiple identifiers separated by comma (,) or put this
# option multiple times (only on the command line, not in the configuration
# file where it should appear only once).You can also use "--disable=all" to
# disable everything first and then reenable specific checks. For example, if
# you want to run only the similarities checker, you can use "--disable=all
# --enable=similarities". If you want to run only the classes checker, but have
# no Warning level messages displayed, use"--disable=all --enable=classes
# --disable=W"
disable=intern-builtin,nonzero-method,parameter-unpacking,backtick,raw_input-builtin,dict-view-method,filter-builtin-not-iterating,long-builtin,unichr-builtin,input-builtin,unicode-builtin,file-builtin,map-builtin-not-iterating,delslice-method,apply-builtin,cmp-method,setslice-method,coerce-method,long-suffix,raising-string,import-star-module-level,buffer-builtin,reload-builtin,unpacking-in-except,print-statement,hex-method,old-octal-literal,metaclass-assignment,dict-iter-method,range-builtin-not-iterating,using-cmp-argument,indexing-exception,no-absolute-import,coerce-builtin,getslice-method,suppressed-message,execfile-builtin,round-builtin,useless-suppression,reduce-builtin,old-raise-syntax,zip-builtin-not-iterating,cmp-builtin,xrange-builtin,standarderror-builtin,old-division,oct-method,next-method-called,old-ne-operator,basestring-builtin


[REPORTS]

# Set the output format. Available formats are text, parseable, colorized, msvs
# (visual studio) and html. You can also give a reporter class, eg
# mypackage.mymodule.MyReporterClass.
output-format=text

# Put messages in a separate file for each module / package specified on the
# command line instead of printing them on stdout. Reports (if any) will be
# written in a file name "pylint_global.[txt|html]".
files-output=no

# Tells whether to display a full report or only the messages
reports=no

# Python expression which should return a note less than 10 (10 is the highest
# note). You have access to the variables errors warning, statement which
# respectively contain the number of errors / warnings messages and the total
# number of statements analyzed. This is used by the global evaluation report
# (RP0004).
evaluation=10.0 - ((float(5 * error + warning + refactor + convention) / statement) * 10)

# Template used to display messages. This is a python new-style format string
# used to format the message information. See doc for all details
#msg-template=


[BASIC]

# List of builtins function names that should not be used, separated by a comma
bad-functions=map,filter

# Good variable names which should always be accepted, separated by a comma
good-names=i,j,k,ex,Run,_

# Bad variable names which should always be refused, separated by a comma
bad-names=foo,bar,baz,toto,tutu,tata

# Colon-delimited sets of names that determine each other's naming style when
# the name regexes allow several styles.
name-group=

# Include a hint for the correct naming format with invalid-name
include-naming-hint=yes

# Regular expression matching correct argument names
argument-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming hint for argument names
argument-name-hint=[a-z_][a-z0-9_]{2,30}$

# Regular expression matching correct attribute names
attr-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming hint for attribute names
attr-name-hint=[a-z_][a-z0-9_]{2,30}$

# Regular expression matching correct constant names
const-rgx=(([A-Z_][A-Z0-9_]*)|(__.*__))$

# Naming hint for constant names
const-name-hint=(([A-Z_][A-Z0-9_]*)|(__.*__))$

# Regular expression matching correct class names
class-rgx=[A-Z_][a-zA-Z0-9]+$

# Naming hint for class names
class-name-hint=[A-Z_][a-zA-Z0-9]+$

# Regular expression matching correct inline iteration names
inlinevar-rgx=[A-Za-z_][A-Za-z0-9_]*$

# Naming hint for inline iteration names
inlinevar-name-hint=[A-Za-z_][A-Za-z0-9_]*$

# Regular expression matching correct class attribute names
class-attribute-rgx=([A-Za-z_][A-Za-z0-9_]{2,30}|(__.*__))$

# Naming hint for class attribute names
class-attribute-name-hint=([A-Za-z_][A-Za-z0-9_]{2,30}|(__.*__))$

# Regular expression matching correct function names
function-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming hint for function names
function-name-hint=[a-z_][a-z0-9_]{2,30}$

# Regular expression matching correct module names
module-rgx=(([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$

# Naming hint for module names
module-name-hint=(([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$

# Regular expression matching correct method names
method-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming hint for method names
method-name-hint=[a-z_][a-z0-9_]{2,30}$

# Regular expression matching correct variable names
variable-rgx=[a-z_][a-z0-9_]{2,30}$

# Naming hint for variable names
variable-name-hint=[a-z_][a-z0-9_]{2,30}$

# Regular expression which should only match function or class names that do
# not require a docstring.
no-docstring-rgx=^_

# Minimum line length for functions/classes that require docstrings, shorter
# ones are exempt.
docstring-min-length=-1


[ELIF]

# Maximum number of nested blocks for function / method body
max-nested-blocks=5


[FORMAT]

# Maximum number of characters on a single line.
max-line-length=100

# Regexp for a line that is allowed to be longer than the limit.
ignore-long-lines=^\s*(# )?<?https?://\S+>?$

# Allow the body of an if to be on the same line as the test if there is no
# else.
single-line-if-stmt=no

# List of optional constructs for which whitespace checking is disabled. `dict-
# separator` is used to allow tabulation in dicts, etc.: {1  : 1,\n222: 2}.
# `trailing-comma` allows a space between comma and closing bracket: (a, ).
# `empty-line` allows space-only lines.
no-space-check=trailing-comma,dict-separator

# Maximum number of lines in a module
max-module-lines=1000

# String used as indentation unit. This is usually "    " (4 spaces) or "\t" (1
# tab).
indent-string='    '

# Number of spaces of indent required inside a hanging  or continued line.
indent-after-paren=4

# Expected format of line ending, e.g. empty (any line ending), LF or CRLF.
expected-line-ending-format=


[LOGGING]

# Logging modules to check that the string format arguments are in logging
# function parameter format
logging-modules=logging


[MISCELLANEOUS]

# List of note tags to take in consideration, separated by a comma.
notes=FIXME,XXX,TODO


[SIMILARITIES]

# Minimum lines number of a similarity.
min-similarity-lines=4

# Ignore comments when computing similarities.
ignore-comments=yes

# Ignore docstrings when computing similarities.
ignore-docstrings=yes

# Ignore imports when computing similarities.
ignore-imports=no


[SPELLING]

# Spelling dictionary name. Available dictionaries: none. To make it working
# install python-enchant package.
spelling-dict=

# List of comma separated words that should not be checked.
spelling-ignore-words=

# A path to a file that contains private dictionary; one word per line.
spelling-private-dict-file=

# Tells whether to store unknown words to indicated private dictionary in
# --spelling-private-dict-file option instead of raising a message.
spelling-store-unknown-words=no


[TYPECHECK]

# Tells whether missing members accessed in mixin class should be ignored. A
# mixin class is detected if its name ends with "mixin" (case insensitive).
ignore-mixin-members=yes

# List of module names for which member attributes should not be checked
# (useful for modules/projects where namespaces are manipulated during runtime
# and thus existing member attributes cannot be deduced by static analysis. It
# supports qualified module names, as well as Unix pattern matching.
ignored-modules=

# List of classes names for which member attributes should not be checked
# (useful for classes with attributes dynamically set). This supports can work
# with qualified names.
ignored-classes=

# List of members which are set dynamically and missed by pylint inference
# system, and so shouldn't trigger E1101 when accessed. Python regular
# expressions are accepted.
generated-members=


[VARIABLES]

# Tells whether we should check for unused import in __init__ files.
init-import=no

# A regular expression matching the name of dummy variables (i.e. expectedly
# not used).
dummy-variables-rgx=_$|dummy

# List of additional names supposed to be defined in builtins. Remember that
# you should avoid to define new builtins when possible.
additional-builtins=

# List of strings which can identify a callback function by name. A callback
# name must start or end with one of those strings.
callbacks=cb_,_cb


[CLASSES]

# List of method names used to declare (i.e. assign) instance attributes.
defining-attr-methods=__init__,__new__,setUp

# List of valid names for the first argument in a class method.
valid-classmethod-first-arg=cls

# List of valid names for the first argument in a metaclass class method.
valid-metaclass-classmethod-first-arg=mcs

# List of member names, which should be excluded from the protected access
# warning.
exclude-protected=_asdict,_fields,_replace,_source,_make


[DESIGN]

# Maximum number of arguments for function / method
max-args=20

# Argument names that match this expression will be ignored. Default to name
# with leading underscore
ignored-argument-names=_.*

# Maximum number of locals for function / method body
max-locals=20

# Maximum number of return / yield for function / method body
max-returns=6

# Maximum number of branch for function / method body
max-branches=12

# Maximum number of statements in function / method body
max-statements=50

# Maximum number of parents for a class (see R0901).
max-parents=7

# Maximum number of attributes for a class (see R0902).
max-attributes=10

# Minimum number of public methods for a class (see R0903).
min-public-methods=2

# Maximum number of public methods for a class (see R0904).
max-public-methods=20

# Maximum number of boolean expressions in an if statement
max-bool-expr=5


[IMPORTS]
# Create a graph of every (i.e. internal and external) dependencies in the
# given file (report RP0402 must not be disabled)
import-graph=

# Create a graph of external dependencies in the given file (report RP0402 must
# not be disabled)
ext-import-graph=

# Create a graph of internal dependencies in the given file (report RP0402 must
# not be disabled)
int-import-graph=
```

## File: `.readthedocs.yaml`
```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
python:
  install:
  - path: .
  - requirements: docs/source/requirements.txt
sphinx:
  configuration: docs/source/conf.py
```

## File: `CONTRIBUTING.rst`
```
Please refer to `Contributing to Flake8
<https://flake8.pycqa.org/en/latest/internal/contributing.html>`_
on our website.
```

## File: `CONTRIBUTORS.txt`
```
Project created by Tarek Ziadé.

Contributors (by order of appearance) :

- Tamás Gulácsi
- Nicolas Dumazet
- Stefan Scherfke
- Chris Adams
- Ben Bass
- Ask Solem
- Steven Kryskalla
- Gustavo Picon
- Jannis Leidel
- Miki Tebeka
- David Cramer
- Peter Teichman
- Ian Cordasco
- Oleg Broytman
- Marc Labbé
- Bruno Miguel Custódio
- Florent Xicluna
- Austin Morton
- Michael McNeil Forbes
- Christian Long
- Tyrel Souza
- Corey Farwell
- Michael Penkov
- Anthony Sottile
```

## File: `LICENSE`
```
== Flake8 License (MIT) ==

Copyright (C) 2011-2013 Tarek Ziade <tarek@ziade.org>
Copyright (C) 2012-2016 Ian Cordasco <graffatcolmingov@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.rst`
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

## File: `dev-requirements.txt`
```
tox
```

## File: `pytest.ini`
```
[pytest]
norecursedirs = .git .* *.egg* docs dist build
addopts = -rw
filterwarnings = error
```

## File: `setup.cfg`
```
[metadata]
name = flake8
version = attr: flake8.__version__
description = the modular source code checker: pep8 pyflakes and co
long_description = file: README.rst
long_description_content_type = text/x-rst
url = https://github.com/pycqa/flake8
author = Tarek Ziade
author_email = tarek@ziade.org
maintainer = Ian Stapleton Cordasco
maintainer_email = graffatcolmingov@gmail.com
license = MIT
license_files = LICENSE
classifiers =
    Development Status :: 5 - Production/Stable
    Environment :: Console
    Framework :: Flake8
    Intended Audience :: Developers
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Topic :: Software Development :: Libraries :: Python Modules
    Topic :: Software Development :: Quality Assurance

[options]
packages = find:
install_requires =
    mccabe>=0.7.0,<0.8.0
    pycodestyle>=2.14.0,<2.15.0
    pyflakes>=3.4.0,<3.5.0
python_requires = >=3.10
package_dir =
    =src

[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    flake8 = flake8.main.cli:main
flake8.extension =
    F = flake8.plugins.pyflakes:FlakesChecker
    E = flake8.plugins.pycodestyle:pycodestyle_logical
    W = flake8.plugins.pycodestyle:pycodestyle_physical
flake8.report =
    default = flake8.formatting.default:Default
    pylint = flake8.formatting.default:Pylint
    quiet-filename = flake8.formatting.default:FilenameOnly
    quiet-nothing = flake8.formatting.default:Nothing

[bdist_wheel]
universal = 1

[coverage:run]
source =
    flake8
    tests
plugins = covdefaults

[coverage:report]
fail_under = 97

[mypy]
check_untyped_defs = true
disallow_any_generics = true
disallow_incomplete_defs = true
disallow_untyped_defs = true
no_implicit_optional = true
warn_unused_ignores = true

[mypy-tests.*]
disallow_untyped_defs = false
```

## File: `setup.py`
```python
"""Packaging logic for Flake8."""
from __future__ import annotations

import os
import sys

import setuptools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

setuptools.setup()
```

## File: `tox.ini`
```
[tox]
minversion=2.3.1
envlist = py,flake8,linters,docs

[testenv]
deps =
    pytest!=3.0.5,!=5.2.3
    coverage>=6
    covdefaults
commands =
    coverage run -m pytest {posargs}
    coverage report
    # ensure 100% coverage of tests
    coverage report --fail-under 100 --include tests/*

# Dogfood our current main version
[testenv:dogfood]
skip_install = true
deps =
    wheel
commands =
    python setup.py -qq bdist_wheel
    pip install --force-reinstall -U --pre --find-links ./dist/ flake8
    flake8 --version
    flake8 src/flake8/ tests/ setup.py

# Linters
[testenv:flake8]
skip_install = true
deps =
    flake8
    flake8-bugbear
    flake8-docstrings>=1.3.1
    flake8-typing-imports>=1.1
    pep8-naming
commands =
    flake8 src/flake8/ tests/ setup.py

[testenv:pylint]
skip_install = true
deps =
    pyflakes
    pylint!=2.5.0
commands =
    pylint src/flake8

[testenv:doc8]
skip_install = true
deps =
    sphinx
    doc8
commands =
    doc8 docs/source/

[testenv:pre-commit]
skip_install = true
deps = pre-commit
commands =
    pre-commit run --all-files --show-diff-on-failure

[testenv:bandit]
skip_install = true
deps =
    bandit
commands =
    bandit -r src/flake8/ -c .bandit.yml

[testenv:linters]
skip_install = true
deps =
    {[testenv:flake8]deps}
    {[testenv:pylint]deps}
    {[testenv:doc8]deps}
    {[testenv:readme]deps}
    {[testenv:bandit]deps}
commands =
    {[testenv:flake8]commands}
    {[testenv:pylint]commands}
    {[testenv:doc8]commands}
    {[testenv:readme]commands}
    {[testenv:bandit]commands}

# Documentation
[testenv:docs]
deps =
    -rdocs/source/requirements.txt
commands =
    sphinx-build -E -W -c docs/source/ -b html docs/source/ docs/build/html

[testenv:serve-docs]
skip_install = true
changedir = docs/build/html
deps =
commands =
    python -m http.server {posargs}

[testenv:readme]
deps =
    readme_renderer
commands =
    python setup.py check -r -s

# Release tooling
[testenv:build]
skip_install = true
deps =
    wheel
    setuptools
commands =
    python setup.py -q sdist bdist_wheel

[testenv:release]
skip_install = true
deps =
    {[testenv:build]deps}
    twine >= 1.5.0
commands =
    {[testenv:build]commands}
    twine upload --skip-existing dist/*

[flake8]
extend-ignore = E203
per-file-ignores =
    src/flake8/formatting/_windows_color.py: N806
    tests/*: D
max-complexity = 10
```

## File: `docs/source/conf.py`
```python
#
# flake8 documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 19 07:14:10 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
from __future__ import annotations

import flake8

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "2.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx_prompt",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "flake8"
copyright = "2016, Ian Stapleton Cordasco"
author = "Ian Stapleton Cordasco"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = flake8.__version__
# The full version, including alpha/beta/rc tags.
release = flake8.__version__

rst_epilog = """
.. |Flake8| replace:: :program:`Flake8`
"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "flake8doc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "flake8.tex",
        "flake8 Documentation",
        "Ian Stapleton Cordasco",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Flake8",
        "Flake8 Documentation",
        "Tarek Ziade",
        "Flake8",
        "Code checking using pycodestyle, pyflakes and mccabe",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "packaging": ("https://packaging.python.org/en/latest/", None),
    "setuptools": ("https://setuptools.pypa.io/en/latest/", None),
}

extlinks = {
    "issue": ("https://github.com/pycqa/flake8/issues/%s", "#%s"),
    "pull": ("https://github.com/pycqa/flake8/pull/%s", "#%s"),
}

autodoc_typehints = "description"
```

## File: `docs/source/faq.rst`
```
============================
 Frequently Asked Questions
============================

When is Flake8 released?
========================

|Flake8| is released *as necessary*. Sometimes there are specific goals and
drives to get to a release. Usually, we release as users report and fix
bugs.


How can I help Flake8 release faster?
=====================================

Look at the next milestone. If there's work you can help us complete, that
will help us get to the next milestone. If there's a show-stopping bug that
needs to be released, let us know but please be kind. |Flake8| is developed
and released entirely on volunteer time.


What is the next version of Flake8?
===================================

In general we try to use milestones to indicate this. If the last release
on PyPI is 3.1.5 and you see a milestone for 3.2.0 in GitHub, there's a
good chance that 3.2.0 is the next release.


Why does Flake8 use ranges for its dependencies?
================================================

|Flake8| uses ranges for mccabe, pyflakes, and pycodestyle because each of
those projects tend to add *new* checks in minor releases. It has been an
implicit design goal of |Flake8|'s to make the list of error codes stable in
its own minor releases. That way if you install something from the 2.5
series today, you will not find new checks in the same series in a month
from now when you install it again.

|Flake8|'s dependencies tend to avoid new checks in patch versions which is
why |Flake8| expresses its dependencies roughly as::

    pycodestyle >= 2.0.0, < 2.1.0
    pyflakes >= 0.8.0, != 1.2.0, != 1.2.1, != 1.2.2, < 1.3.0
    mccabe >= 0.5.0, < 0.6.0

This allows those projects to release patch versions that fix bugs and for
|Flake8| users to consume those fixes.


Should I file an issue when a new version of a dependency is available?
=======================================================================

**No.** The current Flake8 core team (of one person) is also
a core developer of pycodestyle, pyflakes, and mccabe. They are aware of
these releases.
```

## File: `docs/source/glossary.rst`
```
.. _glossary:

================================================
 Glossary of Terms Used in Flake8 Documentation
================================================

.. glossary::
    :sorted:

    formatter
        A :term:`plugin` that augments the output of |Flake8| when passed
        to :option:`flake8 --format`.

    plugin
        A package that is typically installed from PyPI to augment the
        behaviour of |Flake8| either through adding one or more additional
        :term:`check`\ s or providing additional :term:`formatter`\ s.

    check
        A piece of logic that corresponds to an error code. A check may
        be a style check (e.g., check the length of a given line against
        the user configured maximum) or a lint check (e.g., checking for
        unused imports) or some other check as defined by a plugin.

    error
    error code
    violation
        The symbol associated with a specific :term:`check`. For example,
        pycodestyle implements :term:`check`\ s that look for whitespace
        around binary operators and will either return an error code of
        ``W503`` or ``W504``.

    warning
        Typically the ``W`` class of :term:`error code`\ s from pycodestyle.

    class
    error class
        A larger grouping of related :term:`error code`\ s. For example,
        ``W503`` and ``W504`` are two codes related to whitespace. ``W50``
        would be the most specific class of codes relating to whitespace.
        ``W`` would be the warning class that subsumes all whitespace
        errors.

    pyflakes
        The project |Flake8| depends on to lint files (check for unused
        imports, variables, etc.). This uses the ``F`` :term:`class` of
        :term:`error code`\ s reported by |Flake8|.

    pycodestyle
        The project |Flake8| depends on to provide style enforcement.
        pycodestyle implements :term:`check`\ s for :pep:`8`. This uses the
        ``E`` and ``W`` :term:`class`\ es of :term:`error code`\ s.

    mccabe
        The project |Flake8| depends on to calculate the McCabe complexity
        of a unit of code (e.g., a function). This uses the ``C``
        :term:`class` of :term:`error code`\ s.
```

## File: `docs/source/index.rst`
```
.. flake8 documentation master file, created by
   sphinx-quickstart on Tue Jan 19 07:14:10 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============================================
 Flake8: Your Tool For Style Guide Enforcement
===============================================

Quickstart
==========

.. _installation-guide:

Installation
------------

To install |Flake8|, open an interactive shell and run:

.. code::

    python<version> -m pip install flake8

If you want |Flake8| to be installed for your default Python installation, you
can instead use:

.. code::

    python -m pip install flake8

.. note::

    It is **very** important to install |Flake8| on the *correct* version of
    Python for your needs. If you want |Flake8| to properly parse new language
    features in Python 3.5 (for example), you need it to be installed on 3.5
    for |Flake8| to understand those features. In many ways, Flake8 is tied to
    the version of Python on which it runs.

Using Flake8
------------

To start using |Flake8|, open an interactive shell and run:

.. code::

    flake8 path/to/code/to/check.py
    # or
    flake8 path/to/code/

.. note::

    If you have installed |Flake8| on a particular version of Python (or on
    several versions), it may be best to instead run ``python<version> -m
    flake8``.

If you only want to see the instances of a specific warning or error, you can
*select* that error like so:

.. code::

    flake8 --select E123,W503 path/to/code/

Alternatively, if you want to add a specific warning or error to *ignore*:

.. code::

    flake8 --extend-ignore E203,W234 path/to/code/

Please read our user guide for more information about how to use and configure
|Flake8|.

FAQ and Glossary
================

.. toctree::
    :maxdepth: 2

    faq
    glossary

User Guide
==========

All users of |Flake8| should read this portion of the documentation. This
provides examples and documentation around |Flake8|'s assortment of options
and how to specify them on the command-line or in configuration files.

.. toctree::
    :maxdepth: 2

    user/index

Plugin Developer Guide
======================

If you're maintaining a plugin for |Flake8| or creating a new one, you should
read this section of the documentation. It explains how you can write your
plugins and distribute them to others.

.. toctree::
    :maxdepth: 2

    plugin-development/index

Contributor Guide
=================

If you are reading |Flake8|'s source code for fun or looking to contribute,
you should read this portion of the documentation. This is a mix of documenting
the internal-only interfaces |Flake8| and documenting reasoning for Flake8's
design.

.. toctree::
    :maxdepth: 2

    internal/index

Release Notes and History
=========================

.. toctree::
    :maxdepth: 2

    release-notes/index

General Indices
===============

* :ref:`genindex`
* :ref:`Index of Documented Public Modules <modindex>`
* :ref:`Glossary of terms <glossary>`
```

## File: `docs/source/requirements.txt`
```
sphinx>=2.1.0,!=3.1.0
sphinx-rtd-theme>=1.2.2
sphinx-prompt>=1.8.0
docutils!=0.18
```

## File: `docs/source/internal/checker.rst`
```
====================
 How Checks are Run
====================

In |Flake8| 2.x, |Flake8| delegated check running to pep8. In 3.0 |Flake8|
takes on that responsibility. This has allowed for simpler
handling of the ``--jobs`` parameter (using :mod:`multiprocessing`) and
simplified our fallback if something goes awry with concurrency.
At the lowest level we have a |FileChecker|. Instances of |FileChecker| are
created for *each* file to be analyzed by |Flake8|. Each instance, has a copy
of all of the plugins registered with setuptools in the ``flake8.extension``
entry-point group.

The |FileChecker| instances are managed by an instance of |Manager|. The
|Manager| instance handles creating sub-processes with
:mod:`multiprocessing` module and falling back to running checks in serial if
an operating system level error arises. When creating |FileChecker| instances,
the |Manager| is responsible for determining if a particular file has been
excluded.


Processing Files
----------------

Unfortunately, since |Flake8| took over check running from pep8/pycodestyle,
it also had to take over parsing and processing files for the checkers
to use. Since it couldn't reuse pycodestyle's functionality (since it did not
separate cleanly the processing from check running) that function was isolated
into the :class:`~flake8.processor.FileProcessor` class. We moved
several helper functions into the :mod:`flake8.processor` module (see also
:ref:`Processor Utility Functions <processor_utility_functions>`).


API Reference
-------------

.. autoclass:: flake8.checker.FileChecker
    :members:

.. autoclass:: flake8.checker.Manager
    :members:

.. autoclass:: flake8.processor.FileProcessor
    :members:


.. _processor_utility_functions:

Utility Functions
`````````````````

.. autofunction:: flake8.processor.count_parentheses

.. autofunction:: flake8.processor.expand_indent

.. autofunction:: flake8.processor.is_eol_token

.. autofunction:: flake8.processor.is_multiline_string

.. autofunction:: flake8.processor.mutate_string

.. autofunction:: flake8.processor.token_is_newline

.. Substitutions
.. |FileChecker| replace:: :class:`~flake8.checker.FileChecker`
.. |Manager| replace:: :class:`~flake8.checker.Manager`
```

## File: `docs/source/internal/cli.rst`
```
Command Line Interface
======================

The command line interface of |Flake8| is modeled as an application via
:class:`~flake8.main.cli.Application`. When a user runs ``flake8`` at their
command line, :func:`~flake8.main.cli.main` is run which handles
management of the application.

User input is parsed *twice* to accommodate logging and verbosity options
passed by the user as early as possible.
This is so as much logging can be produced as possible.

The default |Flake8| options are registered by
:func:`~flake8.main.options.register_default_options`. Trying to register
these options in plugins will result in errors.


API Documentation
-----------------

.. autofunction:: flake8.main.cli.main

.. autoclass:: flake8.main.application.Application
    :members:

.. autofunction:: flake8.main.options.register_default_options
```

## File: `docs/source/internal/contributing.rst`
```
========================
 Contributing to Flake8
========================

There are many ways to contribute to |Flake8|, and we encourage them all:

- contributing bug reports and feature requests

- contributing documentation (and yes that includes this document)

- reviewing and triaging bugs and merge requests

Before you go any further, please allow me to reassure you that I do want
*your* contribution. If you think your contribution might not be valuable, I
reassure you that any help you can provide *is* valuable.


Code of Conduct
===============

|Flake8| adheres to the `Python Code Quality Authority's Code of Conduct`_.
Any violations of the Code of Conduct should be reported to Ian Stapleton
Cordasco (graffatcolmingov [at] gmail [dot] com).


Setting Up A Development Environment
====================================

To contribute to |Flake8|'s development, you simply need:

- Python (one of the versions we support)

- `tox`_

  We suggest installing this like:

  .. prompt:: bash

        pip install --user tox

  Or

  .. prompt:: bash

        python<version> -m pip install --user tox

- your favorite editor


Filing a Bug
============

When filing a bug against |Flake8|, please fill out the issue template as it
is provided to you by `GitHub`_. If your bug is in reference to one of the
checks that |Flake8| reports by default, please do not report them to |Flake8|
unless |Flake8| is doing something to prevent the check from running or you
have some reason to believe |Flake8| is inhibiting the effectiveness of the
check.

**Please search for closed and open bug reports before opening new ones.**

All bug reports about checks should go to their respective projects:

- Error codes starting with ``E`` and ``W`` should be reported to
  `pycodestyle`_.

- Error codes starting with ``F`` should be reported to `pyflakes`_

- Error codes starting with ``C`` should be reported to `mccabe`_


Requesting a New Feature
========================

When requesting a new feature in |Flake8|, please fill out the issue template.
Please also note if there are any existing alternatives to your new feature
either via plugins, or combining command-line options. Please provide example
use cases. For example, do not ask for a feature like this:

    I need feature frobulate for my job.

Instead ask:

    I need |Flake8| to frobulate these files because my team expects them to
    frobulated but |Flake8| currently does not frobulate them. We tried using
    ``--filename`` but we could not create a pattern that worked.

The more you explain about *why* you need a feature, the more likely we are to
understand your needs and help you to the best of our ability.


Contributing Documentation
==========================

To contribute to |Flake8|'s documentation, you might want to first read a
little about reStructuredText or Sphinx. |Flake8| has a :ref:`guide of best
practices <docs-style>` when contributing to our documentation. For the most
part, you should be fine following the structure and style of the rest of
|Flake8|'s documentation.

All of |Flake8|'s documentation is written in reStructuredText and rendered by
Sphinx. The source (reStructuredText) lives in ``docs/source/``. To build
the documentation the way our Continuous Integration does, run:

.. prompt:: bash

    tox -e docs

To view the documentation locally, you can also run:

.. prompt:: bash

    tox -e serve-docs

You can run the latter in a separate terminal and continuously re-run the
documentation generation and refresh the documentation you're working on.

.. note::

    We lint our documentation just like we lint our code.
    You should also run:

    .. prompt:: bash

        tox -e linters

    After making changes and before pushing them to ensure that they will
    pass our CI tests.


Contributing Code
=================

|Flake8| development happens on `GitHub`_. Code contributions should be
submitted there.

Merge requests should:

- Fix one issue and fix it well

  Fix the issue, but do not include extraneous refactoring or code
  reformatting. In other words, keep the diff short, but only as short
  as is necessary to fix the bug appropriately and add sufficient testing
  around it. Long diffs are fine, so long as everything that it includes
  is necessary to the purpose of the merge request.

- Have descriptive titles and descriptions

  Searching old merge requests is made easier when a merge request is well
  described.

- Have commits that follow this style:

  .. code::

        Create a short title that is 50 characters long

        Ensure the title and commit message use the imperative voice. The
        commit and you are doing something. Also, please ensure that the
        body of the commit message does not exceed 72 characters.

        The body may have multiple paragraphs as necessary.

        The final line of the body references the issue appropriately.

- Follow the guidelines in :ref:`writing-code`

- Avoid having :code:`.gitignore` file in your PR

  Changes to :code:`.gitignore` will rarely be accepted.

  If you need to add files to :code:`.gitignore` you have multiple options

  - Create a global :code:`.gitignore` file
  - Create/update :code:`.git/info/exclude` file.

  Both these options are explained in detail `here <https://help.github.com/en/articles/ignoring-files#create-a-global-gitignore>`_


Reviewing and Triaging Issues and Merge Requests
================================================

When reviewing other people's merge requests and issues, please be
**especially** mindful of how the words you choose can be read by someone
else. We strive for professional code reviews that do not insult the
contributor's intelligence or impugn their character. The code review
should be focused on the code, its effectiveness, and whether it is
appropriate for |Flake8|.

If you have the ability to edit an issue or merge request's labels, please do
so to make search and prioritization easier.

|Flake8| uses milestones with both issues and merge requests. This provides
direction for other contributors about when an issue or merge request will be
delivered.


.. links
.. _Python Code Quality Authority's Code of Conduct:
    https://meta.pycqa.org/code-of-conduct.html

.. _tox:
    https://tox.readthedocs.io/

.. _GitHub:
    https://github.com/pycqa/flake8

.. _pycodestyle:
    https://github.com/pycqa/pycodestyle

.. _pyflakes:
    https://github.com/pyflakes/pyflakes

.. _mccabe:
    https://github.com/pycqa/mccabe
```

## File: `docs/source/internal/formatters.rst`
```
=====================
 Built-in Formatters
=====================

By default |Flake8| has two formatters built-in, ``default`` and ``pylint``.
These correspond to two classes |DefaultFormatter| and |PylintFormatter|.

In |Flake8| 2.0, pep8 handled formatting of errors and also allowed users to
specify an arbitrary format string as a parameter to ``--format``. In order
to allow for this backwards compatibility, |Flake8| 3.0 made two choices:

#. To not limit a user's choices for ``--format`` to the format class names

#. To make the default formatter attempt to use the string provided by the
   user if it cannot find a formatter with that name.

Default Formatter
=================

The |DefaultFormatter| continues to use the same default format string as
pep8: ``'%(path)s:%(row)d:%(col)d: %(code)s %(text)s'``.

To provide the default functionality it overrides two methods:

#. ``after_init``

#. ``format``

The former allows us to inspect the value provided to ``--format`` by the
user and alter our own format based on that value. The second simply uses
that format string to format the error.

.. autoclass:: flake8.formatting.default.Default
    :members:

Pylint Formatter
================

The |PylintFormatter| simply defines the default Pylint format string from
pep8: ``'%(path)s:%(row)d: [%(code)s] %(text)s'``.

.. autoclass:: flake8.formatting.default.Pylint
    :members:


.. |DefaultFormatter| replace:: :class:`~flake8.formatting.default.Default`
.. |PylintFormatter| replace:: :class:`~flake8.formatting.default.Pylint`
```

## File: `docs/source/internal/index.rst`
```
==============================
 Exploring Flake8's Internals
==============================

While writing |Flake8| 3.0, the developers attempted to capture some reasoning
and decision information in internal documentation meant for future developers
and maintainers. Most of this information is unnecessary for users and plugin
developers. Some of it, however, is linked to from the plugin development
documentation.

Keep in mind that not everything will be here and you may need to help pull
information out of the developers' heads and into these documents. Please
pull gently.

.. toctree::
    :maxdepth: 2

    contributing
    writing-documentation
    writing-code
    releases
    start-to-finish
    checker
    cli
    formatters
    option_handling
    plugin_handling
    utils
```

## File: `docs/source/internal/option_handling.rst`
```
Option and Configuration Handling
=================================

Option Management
-----------------

Command-line options are often also set in configuration files for |Flake8|.
While not all options are meant to be parsed from configuration files, many
default options are also parsed from configuration files as well as
most plugin options.

In |Flake8| 2, plugins received a :class:`optparse.OptionParser` instance and
called :meth:`optparse.OptionParser.add_option` to register options. If the
plugin author also wanted to have that option parsed from config files they
also had to do something like:

.. code-block:: python

    parser.config_options.append('my_config_option')
    parser.config_options.extend(['config_opt1', 'config_opt2'])

This was previously undocumented and led to a lot of confusion about why
registered options were not automatically parsed from configuration files.

Since |Flake8| 3 was rewritten from scratch, we decided to take a different
approach to configuration file parsing. Instead of needing to know about an
undocumented attribute that pep8 looks for, |Flake8| 3 now accepts a parameter
to ``add_option``, specifically ``parse_from_config`` which is a boolean
value.

|Flake8| does this by creating its own abstractions on top of :mod:`argparse`.
The first abstraction is the :class:`flake8.options.manager.Option` class. The
second is the :class:`flake8.options.manager.OptionManager`. In fact, we add
three new parameters:

- ``parse_from_config``

- ``comma_separated_list``

- ``normalize_paths``

The last two are not specifically for configuration file handling, but they
do improve that dramatically. We found that there were options that, when
specified in a configuration file, often necessitated being split across
multiple lines and those options were almost always comma-separated. For
example, let's consider a user's list of ignored error codes for a project:

.. code-block:: ini

    [flake8]
    ignore =
        # Reasoning
        E111,
        # Reasoning
        E711,
        # Reasoning
        E712,
        # Reasoning
        E121,
        # Reasoning
        E122,
        # Reasoning
        E123,
        # Reasoning
        E131,
        # Reasoning
        E251

It makes sense here to allow users to specify the value this way, but, the
standard library's :class:`configparser.RawConfigParser` class does returns a
string that looks like

.. code-block:: python

    "\nE111,  \nE711,  \nE712,  \nE121,  \nE122,  \nE123,  \nE131,  \nE251  "

This means that a typical call to :meth:`str.split` with ``','`` will not be
sufficient here. Telling |Flake8| that something is a comma-separated list
(e.g., ``comma_separated_list=True``) will handle this for you. |Flake8| will
return:

.. code-block:: python

    ["E111", "E711", "E712", "E121", "E122", "E123", "E131", "E251"]

Next let's look at how users might like to specify their ``exclude`` list.
Presently OpenStack's Nova project has this line in their `tox.ini`_:

.. code-block:: ini

    exclude = .venv,.git,.tox,dist,doc,*openstack/common/*,*lib/python*,*egg,build,tools/xenserver*,releasenotes

We think we can all agree that this would be easier to read like this:

.. code-block:: ini

    exclude =
        .venv,
        .git,
        .tox,
        dist,
        doc,
        *openstack/common/*,
        *lib/python*,
        *egg,
        build,
        tools/xenserver*,
        releasenotes

In this case, since these are actually intended to be paths, we would specify
both ``comma_separated_list=True`` and ``normalize_paths=True`` because we
want the paths to be provided to us with some consistency (either all absolute
paths or not).

Now let's look at how this will actually be used. Most plugin developers
will receive an instance of :class:`~flake8.options.manager.OptionManager` so
to ease the transition we kept the same API as the
:class:`optparse.OptionParser` object. The only difference is that
:meth:`~flake8.options.manager.OptionManager.add_option` accepts the three
extra arguments we highlighted above.

.. _tox.ini:
    https://github.com/openstack/nova/blob/3eb190c4cfc0eefddac6c2cc1b94a699fb1687f8/tox.ini#L155

Configuration File Management
-----------------------------

In |Flake8| 2, configuration file discovery and management was handled by
pep8.  In pep8's 1.6 release series, it drastically broke how discovery and
merging worked (as a result of trying to improve it). To avoid a dependency
breaking |Flake8| again in the future, we have created our own discovery and
management in 3.0.0. In 4.0.0 we have once again changed how this works and we
removed support for user-level config files.

- Project files (files stored in the current directory) are read next and
  merged on top of the user file. In other words, configuration in project
  files takes precedence over configuration in user files.

- **New in 3.0.0** The user can specify ``--append-config <path-to-file>``
  repeatedly to include extra configuration files that should be read and
  take precedence over user and project files.

- **New in 3.0.0** The user can specify ``--config <path-to-file>`` to so this
  file is the only configuration file used. This is a change from |Flake8| 2
  where pep8 would simply merge this configuration file into the configuration
  generated by user and project files (where this takes precedence).

- **New in 3.0.0** The user can specify ``--isolated`` to disable
  configuration via discovered configuration files.

To facilitate the configuration file management, we've taken a different
approach to discovery and management of files than pep8. In pep8 1.5, 1.6, and
1.7 configuration discovery and management was centralized in `66 lines of
very terse python`_ which was confusing and not very explicit. The terseness
of this function (|Flake8| 3.0.0's authors believe) caused the confusion and
problems with pep8's 1.6 series. As such, |Flake8| has separated out
discovery, management, and merging into a module to make reasoning about each
of these pieces easier and more explicit (as well as easier to test).

Configuration file discovery and raw ini reading is managed by
:func:`~flake8.options.config.load_config`.  This produces a loaded
:class:`~configparser.RawConfigParser` and a config directory (which will be
used later to normalize paths).

Next, :func:`~flake8.options.config.parse_config` parses options using the
types in the ``OptionManager``.

Most of this is done in :func:`~flake8.options.aggregator.aggregate_options`.

Aggregating Configuration File and Command Line Arguments
---------------------------------------------------------

:func:`~flake8.options.aggregator.aggregate_options` accepts an instance of
:class:`~flake8.options.manager.OptionManager` and does the work to parse the
command-line arguments.

After parsing the configuration file, we determine the default ignore list. We
use the defaults from the OptionManager and update those with the parsed
configuration files. Finally we parse the user-provided options one last time
using the option defaults and configuration file values as defaults. The
parser merges on the command-line specified arguments for us so we have our
final, definitive, aggregated options.

.. _66 lines of very terse python:
    https://github.com/PyCQA/pep8/blob/b8088a2b6bc5b76bece174efad877f764529bc74/pep8.py#L1981..L2047

API Documentation
-----------------

.. autofunction:: flake8.options.aggregator.aggregate_options

.. autoclass:: flake8.options.manager.Option
    :members: __init__, normalize, to_argparse

.. autoclass:: flake8.options.manager.OptionManager
    :members:
    :special-members:

.. autofunction:: flake8.options.config.load_config

.. autofunction:: flake8.options.config.parse_config
```

## File: `docs/source/internal/plugin_handling.rst`
```
Plugin Handling
===============

Plugin Management
-----------------

|Flake8| 3.0 added support for other plugins besides those which define
new checks. It now supports:

- extra checks

- alternative report formatters

Default Plugins
---------------

Finally, |Flake8| has always provided its own plugin shim for Pyflakes. As
part of that we carry our own shim in-tree and now store that in
:mod:`flake8.plugins.pyflakes`.

|Flake8| also registers plugins for pycodestyle. Each check in pycodestyle
requires different parameters and it cannot easily be shimmed together like
Pyflakes was. As such, plugins have a concept of a "group". If you look at our
:file:`setup.py` you will see that we register pycodestyle checks roughly like
so:

.. code::

    pycodestyle.<check-name> = pycodestyle:<check-name>

We do this to identify that ``<check-name>>`` is part of a group. This also
enables us to special-case how we handle reporting those checks. Instead of
reporting each check in the ``--version`` output, we only report
``pycodestyle`` once.

API Documentation
-----------------

.. autofunction:: flake8.plugins.finder.parse_plugin_options

.. autofunction:: flake8.plugins.finder.find_plugins

.. autofunction:: flake8.plugins.finder.load_plugins
```

## File: `docs/source/internal/releases.rst`
```
==================
 Releasing Flake8
==================

There is not much that is hard to find about how |Flake8| is released.

- We use **major** releases (e.g., 2.0.0, 3.0.0, etc.) for big, potentially
  backwards incompatible, releases.

- We use **minor** releases (e.g., 2.1.0, 2.2.0, 3.1.0, 3.2.0, etc.) for
  releases that contain features and dependency version changes.

- We use **patch** releases (e.g., 2.1.1, 2.1.2, 3.0.1, 3.0.10, etc.) for
  releases that contain *only* bug fixes.

In this sense we follow semantic versioning. But we follow it as more of a set
of guidelines. We're also not perfect, so we may make mistakes, and that's
fine.


Major Releases
==============

Major releases are often associated with backwards incompatibility. |Flake8|
hopes to avoid those, but will occasionally need them.

Historically, |Flake8| has generated major releases for:

- Unvendoring dependencies (2.0)

- Large scale refactoring (2.0, 3.0, 5.0, 6.0)

- Subtly breaking CLI changes (3.0, 4.0, 5.0, 6.0, 7.0)

- Breaking changes to its plugin interface (3.0)

Major releases can also contain:

- Bug fixes (which may have backwards incompatible solutions)

- New features

- Dependency changes


Minor Releases
==============

Minor releases often have new features in them, which we define roughly as:

- New command-line flags

- New behaviour that does not break backwards compatibility

- New errors detected by dependencies, e.g., by raising the upper limit on
  PyFlakes we introduce F405

- Bug fixes


Patch Releases
==============

Patch releases should only ever have bug fixes in them.

We do not update dependency constraints in patch releases. If you do not
install |Flake8| from PyPI, there is a chance that your packager is using
different requirements. Some downstream redistributors have been known to
force a new version of PyFlakes, pep8/PyCodestyle, or McCabe into place.
Occasionally this will cause breakage when using |Flake8|. There is little
we can do to help you in those cases.


Process
=======

To prepare a release, we create a file in :file:`docs/source/release-notes/`
named: ``{{ release_number }}.rst`` (e.g., ``3.0.0.rst``). We note bug fixes,
improvements, and dependency version changes as well as other items of note
for users.

Before releasing, the following tox test environments must pass:

- Python 3.9 (a.k.a., ``tox -e py39``)

- Python 3.13 (a.k.a., ``tox -e py313``)

- PyPy 3 (a.k.a., ``tox -e pypy3``)

- Linters (a.k.a., ``tox -e linters``)

We tag the most recent commit that passes those items and contains our release
notes.

Finally, we run ``tox -e release`` to build source distributions (e.g.,
``flake8-3.0.0.tar.gz``), universal wheels, and upload them to PyPI with
Twine.
```

## File: `docs/source/internal/start-to-finish.rst`
```
==================================
 What Happens When You Run Flake8
==================================

Given |Flake8| 3.0's new organization and structure, it might be a bit much
for some people to understand what happens from when you call ``flake8`` on the
command-line to when it completes. This section aims to give you something of
a technical overview of what exactly happens.


Invocation
==========

The exact way that we end up in our ``main`` function for Flake8 depends on
how you invoke it. If you do something like:

.. prompt:: bash

    flake8

Then your shell looks up where ``flake8`` the executable lives and executes
it. In almost every case, this is a tiny python script generated by
``setuptools`` using the console script entry points that |Flake8| declares
in its :file:`setup.py`. This might look something like:

.. code-block:: python

    #!/path/to/python<version>
    # EASY-INSTALL-ENTRY-SCRIPT: 'flake8==3.0.0','console_scripts','flake8'
    __requires__ = 'flake8==3.0.0'
    import sys
    from pkg_resources import load_entry_point

    if __name__ == '__main__':
        sys.exit(
            load_entry_point('flake8==3.0.0', 'console_scripts', 'flake8')()
        )

If instead you invoke it like:

.. prompt:: bash

    python -m flake8

Then you're relying on Python to find :mod:`flake8.__main__` and run that. In
both cases, however, you end up in :func:`flake8.main.cli.main`. This is the
primary way that users will end up starting Flake8. This function creates an
instance of |Application|.

Application Logic
=================

When we create our |Application| instance, we record the start time and parse
our command-line arguments so we can configure the verbosity of |Flake8|'s
logging. For the most part, every path then calls
:meth:`~flake8.main.application.Application.run` which in turn calls:

- :meth:`~flake8.main.application.Application.initialize`
- :meth:`~flake8.main.application.Application.run_checks`
- :meth:`~flake8.main.application.Application.report_errors`
- :meth:`~flake8.main.application.Application.report_benchmarks`

Our Git hook, however, runs these individually.

Application Initialization
--------------------------

:meth:`~flake8.main.application.Application.initialize` loads all of our
:term:`plugin`\ s, registers the options for those plugins, parses the
command-line arguments, makes our formatter (as selected by the user), makes
our :class:`~flake8.style_guide.StyleGuide` and finally makes our
:class:`file checker manager <flake8.checker.Manager>`.

Running Our Checks
------------------

:meth:`~flake8.main.application.Application.run_checks` then creates an
instance of :class:`flake8.checker.FileChecker` for each file to be checked
after aggregating all of the files that are not excluded and match the
provided file-patterns. Then, if we're on a system that supports
:mod:`multiprocessing` **and** :option:`flake8 --jobs` is either ``auto`` or
a number greater than 1, we will begin processing the files in subprocesses.
Otherwise, we'll run the checks in parallel.

After we start running the checks, we start aggregating the reported
:term:`violation`\ s in the main process. After the checks are done running,
we record the end time.

Reporting Violations
--------------------

Next, the application takes the violations from the file checker manager, and
feeds them through the :class:`~flake8.style_guide.StyleGuide`. This
relies on a :class:`~flake8.style_guide.DecisionEngine` instance to determine
whether the particular :term:`error code` is selected or ignored and then
appropriately sends it to the formatter (or not).

Reporting Benchmarks
--------------------

Finally, if the user has asked to see benchmarks (i.e., :option:`flake8
--benchmark`) then we print the benchmarks.


Exiting
=======

Once :meth:`~flake8.main.application.Application.run` has finished, we then
call :meth:`~flake8.main.application.Application.exit` which looks at how
many errors were reported and whether the user specified :option:`flake8
--exit-zero` and exits with the appropriate exit code.


.. Replacements
.. |Application| replace:: :class:`~flake8.main.application.Application`
```

## File: `docs/source/internal/utils.rst`
```
===================
 Utility Functions
===================

|Flake8| has a few utility functions that it uses internally.

.. warning::

    As should be implied by where these are documented, these are all
    **internal** utility functions. Their signatures and return types
    may change between releases without notice.

    Bugs reported about these **internal** functions will be closed
    immediately.

    If functions are needed by plugin developers, they may be requested
    in the bug tracker and after careful consideration they *may* be added
    to the *documented* stable API.

.. autofunction:: flake8.utils.parse_comma_separated_list

:func:`~flake8.utils.parse_comma_separated_list` takes either a string like

.. code-block:: python

    "E121,W123,F904"
    "E121,\nW123,\nF804"
    " E121,\n\tW123,\n\tF804 "
    " E121\n\tW123 \n\tF804"

And converts it to a list that looks as follows

.. code-block:: python

    ["E121", "W123", "F904"]

This function helps normalize any kind of comma-separated input you or |Flake8|
might receive. This is most helpful when taking advantage of |Flake8|'s
additional parameters to :class:`~flake8.options.manager.Option`.

.. autofunction:: flake8.utils.normalize_path

This utility takes a string that represents a path and returns the absolute
path if the string has a ``/`` in it. It also removes trailing ``/``\ s.

.. autofunction:: flake8.utils.normalize_paths

This function utilizes :func:`~flake8.utils.normalize_path` to normalize a
sequence of paths.  See :func:`~flake8.utils.normalize_path` for what defines a
normalized path.

.. autofunction:: flake8.utils.stdin_get_value

This function retrieves and caches the value provided on ``sys.stdin``. This
allows plugins to use this to retrieve ``stdin`` if necessary.

.. autofunction:: flake8.utils.is_using_stdin

Another helpful function that is named only to be explicit given it is a very
trivial check, this checks if the user specified ``-`` in their arguments to
|Flake8| to indicate we should read from stdin.

.. autofunction:: flake8.utils.fnmatch

The standard library's :func:`fnmatch.fnmatch` is excellent at deciding if a
filename matches a single pattern. In our use case, however, we typically have
a list of patterns and want to know if the filename matches any of them. This
function abstracts that logic away with a little extra logic.
```

## File: `docs/source/internal/writing-code.rst`
```
.. _writing-code:

=========================
 Writing Code for Flake8
=========================

The maintainers of |Flake8| unsurprisingly have some opinions about the style
of code maintained in the project.

At the time of this writing, |Flake8| enables all of PyCodeStyle's checks, all
of PyFlakes' checks, and sets a maximum complexity value (for McCabe) of 10.
On top of that, we enforce PEP-0257 style doc-strings via PyDocStyle
(disabling only D203) and Google's import order style using
flake8-import-order.

The last two are a little unusual, so we provide examples below.


PEP-0257 style doc-strings
==========================

|Flake8| attempts to document both internal interfaces as well as our API and
doc-strings provide a very convenient way to do so. Even if a function, class,
or method isn't included specifically in our documentation having a doc-string
is still preferred. Further, |Flake8| has some style preferences that are not
checked by PyDocStyle.

For example, while most people will never read the doc-string for
:func:`flake8.main.git.hook` that doc-string still provides value to the
maintainers and future collaborators. They (very explicitly) describe the
purpose of the function, a little of what it does, and what parameters it
accepts as well as what it returns.

.. code-block:: python

    # src/flake8/main/git.py
    def hook(lazy: bool = False, strict: bool = False) -> int:
        """Execute Flake8 on the files in git's index.

        Determine which files are about to be committed and run Flake8 over them
        to check for violations.

        :param lazy:
            Find files not added to the index prior to committing. This is useful
            if you frequently use ``git commit -a`` for example. This defaults to
            False since it will otherwise include files not in the index.
        :param strict:
            If True, return the total number of errors/violations found by Flake8.
            This will cause the hook to fail.
        :returns:
            Total number of errors found during the run.
        """
        # NOTE(sigmavirus24): Delay import of application until we need it.
        from flake8.main import application
        app = application.Application()
        with make_temporary_directory() as tempdir:
            filepaths = list(copy_indexed_files_to(tempdir, lazy))
            app.initialize(['.'])
            app.options.exclude = update_excludes(app.options.exclude, tempdir)
            app.run_checks(filepaths)

        app.report_errors()
        if strict:
            return app.result_count
        return 0

Note that we begin the description of the parameter on a new-line and
indented 4 spaces.

Following the above examples and guidelines should help you write doc-strings
that are stylistically correct for |Flake8|.


Imports
=======

|Flake8| follows the import guidelines that Google published in their Python
Style Guide. In short this includes:

- Only importing modules

- Grouping imports into

  * standard library imports

  * third-party dependency imports

  * local application imports

- Ordering imports alphabetically

In practice this would look something like:

.. code-block:: python

    import configparser
    import logging
    from os import path

    import requests

    from flake8 import exceptions
    from flake8.formatting import base

As a result, of the above, we do not:

- Import objects into a namespace to make them accessible from that namespace

- Import only the objects we're using

- Add comments explaining that an import is a standard library module or
  something else


Other Stylistic Preferences
===========================

Finally, |Flake8| has a few other stylistic preferences that it does not
presently enforce automatically.

Multi-line Function/Method Calls
--------------------------------

When you find yourself having to split a call to a function or method up
across multiple lines, insert a new-line after the opening parenthesis, e.g.,

.. code-block:: python

    # src/flake8/main/options.py
    add_option(
        '-v', '--verbose', default=0, action='count',
        parse_from_config=True,
        help='Print more information about what is happening in flake8.'
             ' This option is repeatable and will increase verbosity each '
             'time it is repeated.',
    )

    # src/flake8/formatting/base.py
    def show_statistics(self, statistics):
        """Format and print the statistics."""
        for error_code in statistics.error_codes():
            stats_for_error_code = statistics.statistics_for(error_code)
            statistic = next(stats_for_error_code)
            count = statistic.count
            count += sum(stat.count for stat in stats_for_error_code)
            self._write(f'{count:<5} {error_code} {statistic.message}')

In the first example, we put a few of the parameters all on one line, and then
added the last two on their own. In the second example, each parameter has its
own line. This particular rule is a little subjective. The general idea is
that putting one parameter per-line is preferred, but sometimes it's
reasonable and understandable to group a few together on one line.

Comments
--------

If you're adding an important comment, be sure to sign it. In |Flake8| we
generally sign comments by preceding them with ``NOTE(<name>)``. For example,

.. code-block:: python

    # NOTE(sigmavirus24): The format strings are a little confusing, even
    # to me, so here's a quick explanation:
    # We specify the named value first followed by a ':' to indicate we're
    # formatting the value.
    # Next we use '<' to indicate we want the value left aligned.
    # Then '10' is the width of the area.
    # For floats, finally, we only want only want at most 3 digits after
    # the decimal point to be displayed. This is the precision and it
    # can not be specified for integers which is why we need two separate
    # format strings.
    float_format = '{value:<10.3} {statistic}'.format
    int_format = '{value:<10} {statistic}'.format

Ian is well known across most websites as ``sigmavirus24`` so he signs his
comments that way.

Verbs Belong in Function Names
------------------------------

|Flake8| prefers that functions have verbs in them. If you're writing a
function that returns a generator of files then ``generate_files`` will always
be preferable to ``make_files`` or ``files``.
```

## File: `docs/source/internal/writing-documentation.rst`
```
.. _docs-style:

==================================
 Writing Documentation for Flake8
==================================

The maintainers of |Flake8| believe strongly in benefit of style guides.
Hence, for all contributors who wish to work on our documentation, we've
put together a loose set of guidelines and best practices when adding to
our documentation.


View the docs locally before submitting
=======================================

You can and should generate the docs locally before you submit a pull request
with your changes. You can build the docs by running:

.. prompt:: bash

    tox -e docs

From the directory containing the ``tox.ini`` file (which also contains the
``docs/`` directory that this file lives in).

.. note::

    If the docs don't build locally, they will not build in our continuous
    integration system. We will generally not merge any pull request that
    fails continuous integration.


Run the docs linter tests before submitting
===========================================

You should run the ``doc8`` linter job before you're ready to commit and fix
any errors found.


Capitalize Flake8 in prose
==========================

We believe that by capitalizing |Flake8| in prose, we can help reduce
confusion between the command-line usage of ``flake8`` and the project.

We also have defined a global replacement ``|Flake8|`` that should be used
and will replace each instance with ``:program:`Flake8```.


Use the prompt directive for command-line examples
==================================================

When documenting something on the command-line, use the ``.. prompt::``
directive to make it easier for users to copy and paste into their terminal.

Example:

.. code-block:: restructuredtext

    .. prompt:: bash

        flake8 --select E123,W503 dir/
        flake8 --ignore E24,W504 dir


Wrap lines around 79 characters
===============================

We use a maximum line-length in our documentation that is similar to the
default in |Flake8|. Please wrap lines at 79 characters (or less).


Use two new-lines before new sections
=====================================

After the final paragraph of a section and before the next section title,
use two new-lines to separate them. This makes reading the plain-text
document a little nicer. Sphinx ignores these when rendering so they have
no semantic meaning.

Example:

.. code-block:: restructuredtext

    Section Header
    ==============

    Paragraph.


    Next Section Header
    ===================

    Paragraph.


Surround document titles with equal symbols
===========================================

To indicate the title of a document, we place an equal number of ``=`` symbols
on the lines before and after the title. For example:

.. code-block:: restructuredtext

    ==================================
     Writing Documentation for Flake8
    ==================================

Note also that we "center" the title by adding a leading space and having
extra ``=`` symbols at the end of those lines.


Use the option template for new options
=======================================

All of |Flake8|'s command-line options are documented in the User Guide. Each
option is documented individually using the ``.. option::`` directive provided
by Sphinx. At the top of the document, in a reStructuredText comment, is a
template that should be copied and pasted into place when documening new
options.

.. note::

    The ordering of the options page is the order that options are printed
    in the output of:

    .. prompt:: bash

        flake8 --help

    Please insert your option documentation according to that order.


Use anchors for easy reference linking
======================================

Use link anchors to allow for other areas of the documentation to use the
``:ref:`` role for intralinking documentation. Example:

.. code-block:: restructuredtext

    .. _use-anchors:

    Use anchors for easy reference linking
    ======================================

.. code-block:: restructuredtext

    Somewhere in this paragraph we will :ref:`reference anchors
    <use-anchors>`.

.. note::

    You do not need to provide custom text for the ``:ref:`` if the title of
    the section has a title that is sufficient.


Keep your audience in mind
==========================

|Flake8|'s documentation has three distinct (but not separate) audiences:

#. Users

#. Plugin Developers

#. Flake8 Developers and Contributors

At the moment, you're one of the third group (because you're contributing
or thinking of contributing).

Consider that most Users aren't very interested in the internal working of
|Flake8|. When writing for Users, focus on how to do something or the
behaviour of a certain piece of configuration or invocation.

Plugin developers will only care about the internals of |Flake8| as much as
they will have to interact with that. Keep discussions of internal to the
mininmum required.

Finally, Flake8 Developers and Contributors need to know how everything fits
together. We don't need detail about every line of code, but cogent
explanations and design specifications will help future developers understand
the Hows and Whys of |Flake8|'s internal design.
```

## File: `docs/source/plugin-development/formatters.rst`
```
.. _formatting-plugins:

===========================================
 Developing a Formatting Plugin for Flake8
===========================================

|Flake8| allowed for custom formatting plugins in version
3.0.0. Let's write a plugin together:

.. code-block:: python

    from flake8.formatting import base


    class Example(base.BaseFormatter):
        """Flake8's example formatter."""

        pass

We notice, as soon as we start, that we inherit from |Flake8|'s
:class:`~flake8.formatting.base.BaseFormatter` class. If we follow the
:ref:`instructions to register a plugin <register-a-plugin>` and try to use
our example formatter, e.g., ``flake8 --format=example`` then
|Flake8| will fail because we did not implement the ``format`` method.
Let's do that next.

.. code-block:: python

    class Example(base.BaseFormatter):
        """Flake8's example formatter."""

        def format(self, error):
            return 'Example formatter: {0!r}'.format(error)

With that we're done. Obviously this isn't a very useful formatter, but it
should highlight the simplicity of creating a formatter with Flake8. If we
wanted to instead create a formatter that aggregated the results and returned
XML, JSON, or subunit we could also do that. |Flake8| interacts with the
formatter in two ways:

#. It creates the formatter and provides it the options parsed from the
   configuration files and command-line

#. It uses the instance of the formatter and calls ``handle`` with the error.

By default :meth:`flake8.formatting.base.BaseFormatter.handle` simply calls
the ``format`` method and then ``write``. Any extra handling you wish to do
for formatting purposes should override the ``handle`` method.

API Documentation
=================

.. autoclass:: flake8.formatting.base.BaseFormatter
    :members:
```

## File: `docs/source/plugin-development/index.rst`
```
============================
 Writing Plugins for Flake8
============================

Since |Flake8| 2.0, the |Flake8| tool has allowed for extensions and custom
plugins. In |Flake8| 3.0, we're expanding that ability to customize and
extend **and** we're attempting to thoroughly document it. Some of the
documentation in this section may reference third-party documentation to
reduce duplication and to point you, the developer, towards the authoritative
documentation for those pieces.

Getting Started
===============

To get started writing a |Flake8| :term:`plugin` you first need:

- An idea for a plugin

- An available package name on PyPI

- One or more versions of Python installed

- A text editor or IDE of some kind

- An idea of what *kind* of plugin you want to build:

  * Formatter

  * Check

Once you've gathered these things, you can get started.

All plugins for |Flake8| must be registered via
:external+packaging:doc:`entry points<specifications/entry-points>`. In this
section we cover:

- How to register your plugin so |Flake8| can find it

- How to make |Flake8| provide your check plugin with information (via
  command-line flags, function/class parameters, etc.)

- How to make a formatter plugin

- How to write your check plugin so that it works with |Flake8| 2.x and 3.x


Video Tutorial
==============

Here's a tutorial which goes over building an ast checking plugin from scratch:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto; margin-bottom: 1em;">
        <iframe src="https://www.youtube.com/embed/ot5Z4KQPBL8" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

Detailed Plugin Development Documentation
=========================================

.. toctree::
    :caption: Plugin Developer Documentation
    :maxdepth: 2

    registering-plugins
    plugin-parameters
    formatters
```

## File: `docs/source/plugin-development/plugin-parameters.rst`
```
.. _plugin-parameters:

==========================================
 Receiving Information For A Check Plugin
==========================================

Plugins to |Flake8| have a great deal of information that they can request
from a :class:`~flake8.processor.FileProcessor` instance. Historically,
|Flake8| has supported two types of plugins:

#. classes that accept parsed abstract syntax trees (ASTs)

#. functions that accept a range of arguments

|Flake8| now does not distinguish between the two types of plugins. Any plugin
can accept either an AST or a range of arguments. Further, any plugin that has
certain callable attributes can also register options and receive parsed
options.


Indicating Desired Data
=======================

|Flake8| inspects the plugin's signature to determine what parameters it
expects using :func:`flake8.plugins.finder._parameters_for`.
:attr:`flake8.plugins.finder.LoadedPlugin.parameters` caches the values so that
each plugin makes that fairly expensive call once per plugin. When processing
a file, a plugin can ask for any of the following:

- :attr:`~flake8.processor.FileProcessor.blank_before`
- :attr:`~flake8.processor.FileProcessor.blank_lines`
- :attr:`~flake8.processor.FileProcessor.checker_state`
- :attr:`~flake8.processor.FileProcessor.indent_char`
- :attr:`~flake8.processor.FileProcessor.indent_level`
- :attr:`~flake8.processor.FileProcessor.line_number`
- :attr:`~flake8.processor.FileProcessor.logical_line`
- :attr:`~flake8.processor.FileProcessor.multiline`
- :attr:`~flake8.processor.FileProcessor.noqa`
- :attr:`~flake8.processor.FileProcessor.previous_indent_level`
- :attr:`~flake8.processor.FileProcessor.previous_logical`
- :attr:`~flake8.processor.FileProcessor.previous_unindented_logical_line`
- :attr:`~flake8.processor.FileProcessor.tokens`

Some properties are set once per file for plugins which iterate itself over
the data instead of being called on each physical or logical line.

- :attr:`~flake8.processor.FileProcessor.filename`
- :attr:`~flake8.processor.FileProcessor.file_tokens`
- :attr:`~flake8.processor.FileProcessor.lines`
- :attr:`~flake8.processor.FileProcessor.max_line_length`
- :attr:`~flake8.processor.FileProcessor.max_doc_length`
- :attr:`~flake8.processor.FileProcessor.total_lines`
- :attr:`~flake8.processor.FileProcessor.verbose`

These parameters can also be supplied to plugins working on each line
separately.

Plugins that depend on ``physical_line`` or ``logical_line`` are run on each
physical or logical line once. These parameters should be the first in the
list of arguments (with the exception of ``self``). Plugins that need an AST
(e.g., PyFlakes and McCabe) should depend on ``tree``. These plugins will run
once per file. The parameters listed above can be combined with
``physical_line``, ``logical_line``, and ``tree``.


Registering Options
===================

Any plugin that has callable attributes ``add_options`` and
``parse_options`` can parse option information and register new options.

Your ``add_options`` function should expect to receive an instance of
|OptionManager|. An |OptionManager| instance behaves very similarly to
:class:`optparse.OptionParser`. It, however, uses the layer that |Flake8| has
developed on top of :mod:`argparse` to also handle configuration file parsing.
:meth:`~flake8.options.manager.OptionManager.add_option` creates an |Option|
which accepts the same parameters as :mod:`optparse` as well as three extra
boolean parameters:

- ``parse_from_config``

  The command-line option should also be parsed from config files discovered
  by |Flake8|.

  .. note::

      This takes the place of appending strings to a list on the
      :class:`optparse.OptionParser`.

- ``comma_separated_list``

  The value provided to this option is a comma-separated list. After parsing
  the value, it should be further broken up into a list. This also allows us
  to handle values like:

  .. code::

      E123,E124,
      E125,
        E126

- ``normalize_paths``

  The value provided to this option is a path. It should be normalized to be
  an absolute path. This can be combined with ``comma_separated_list`` to
  allow a comma-separated list of paths.

Each of these options works individually or can be combined. Let's look at a
couple examples from |Flake8|. In each example, we will have
``option_manager`` which is an instance of |OptionManager|.

.. code-block:: python

    option_manager.add_option(
        '--max-line-length', type='int', metavar='n',
        default=defaults.MAX_LINE_LENGTH, parse_from_config=True,
        help='Maximum allowed line length for the entirety of this run. '
             '(Default: %(default)s)',
    )

Here we are adding the ``--max-line-length`` command-line option which is
always an integer and will be parsed from the configuration file. Since we
provide a default, we take advantage of :mod:`argparse`\ 's willingness to
display that in the help text with ``%(default)s``.

.. code-block:: python

    option_manager.add_option(
        '--select', metavar='errors', default='',
        parse_from_config=True, comma_separated_list=True,
        help='Comma-separated list of errors and warnings to enable.'
             ' For example, ``--select=E4,E51,W234``. (Default: %(default)s)',
    )

In adding the ``--select`` command-line option, we're also indicating to the
|OptionManager| that we want the value parsed from the config files and parsed
as a comma-separated list.

.. code-block:: python

    option_manager.add_option(
        '--exclude', metavar='patterns', default=defaults.EXCLUDE,
        comma_separated_list=True, parse_from_config=True,
        normalize_paths=True,
        help='Comma-separated list of files or directories to exclude.'
             '(Default: %(default)s)',
    )

Finally, we show an option that uses all three extra flags. Values from
``--exclude`` will be parsed from the config, converted from a comma-separated
list, and then each item will be normalized.

For information about other parameters to
:meth:`~flake8.options.manager.OptionManager.add_option` refer to the
documentation of :mod:`argparse`.


Accessing Parsed Options
========================

When a plugin has a callable ``parse_options`` attribute, |Flake8| will call
it and attempt to provide the |OptionManager| instance, the parsed options
which will be an instance of :class:`argparse.Namespace`, and the extra
arguments that were not parsed by the |OptionManager|. If that fails, we will
just pass the :class:`argparse.Namespace`. In other words, your
``parse_options`` callable will have one of the following signatures:

.. code-block:: python

    def parse_options(option_manager, options, args):
        pass
    # or
    def parse_options(options):
        pass

.. substitutions
.. |OptionManager| replace:: :class:`~flake8.options.manager.OptionManager`
.. |Option| replace:: :class:`~flake8.options.manager.Option`
```

## File: `docs/source/plugin-development/registering-plugins.rst`
```
.. _register-a-plugin:

==================================
 Registering a Plugin with Flake8
==================================

To register any kind of plugin with |Flake8|, you need:

#. A way to install the plugin (whether it is packaged on its own or
   as part of something else). In this section, we will use a ``setup.py``
   written for an example plugin.

#. A name for your plugin that will (ideally) be unique.

|Flake8| relies on functionality provided by build tools called
:external+packaging:doc:`entry points<specifications/entry-points>`. These
allow any package to register a plugin with |Flake8| via that package's
metadata.

Let's presume that we already have our plugin written and it's in a module
called ``flake8_example``. We will also assume ``setuptools`` is used as a
:external+packaging:term:`Build Backend`, but be aware that most backends
support entry points.

We might have a ``setup.py`` that looks something like:

.. code-block:: python

    import setuptools

    requires = [
        "flake8 > 3.0.0",
    ]

    flake8_entry_point = # ...

    setuptools.setup(
        name="flake8_example",
        license="MIT",
        version="0.1.0",
        description="our extension to flake8",
        author="Me",
        author_email="example@example.com",
        url="https://github.com/me/flake8_example",
        packages=[
            "flake8_example",
        ],
        install_requires=requires,
        entry_points={
            flake8_entry_point: [
                'X = flake8_example:ExamplePlugin',
            ],
        },
        classifiers=[
            "Framework :: Flake8",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Quality Assurance",
        ],
    )

Note specifically these lines:

.. code-block:: python

    flake8_entry_point = # ...

    setuptools.setup(
        # snip ...
        entry_points={
            flake8_entry_point: [
                'X = flake8_example:ExamplePlugin',
            ],
        },
        # snip ...
    )

We tell setuptools to register our entry point ``X`` inside the specific
grouping of entry-points that flake8 should look in.

|Flake8| presently looks at two groups:

- ``flake8.extension``

- ``flake8.report``

If your plugin is one that adds checks to |Flake8|, you will use
``flake8.extension``. If your plugin performs extra report
handling (formatting, filtering, etc.) it will use ``flake8.report``.

If our ``ExamplePlugin`` is something that adds checks, our code would look
like:

.. code-block:: python

    setuptools.setup(
        # snip ...
        entry_points={
            'flake8.extension': [
                'X = flake8_example:ExamplePlugin',
            ],
        },
        # snip ...
    )

The ``X`` in checking plugins define what error codes it is going to report.
So if the plugin reports only the error code ``X101`` your entry-point would
look like::

    X101 = flake8_example:ExamplePlugin

In the above case, the entry-point name and the error code produced by your
plugin are the same.

If your plugin reports several error codes that all start with ``X10``, then
it would look like::

    X10 = flake8_example:ExamplePlugin

In this case as well as the following case, your entry-point name acts as
a prefix to the error codes produced by your plugin.

If all of your plugin's error codes start with ``X1`` then it would look
like::

    X1 = flake8_example:ExamplePlugin

Finally, if all of your plugin's error codes start with just ``X`` then it
would look like the original example.

|Flake8| requires each entry point to be unique amongst all plugins installed
in the users environment. Selecting an entry point that is already used can
cause plugins to be deactivated without warning!

**Please Note:** Your entry point does not need to be exactly 4 characters
as of |Flake8| 3.0. Single letter entry point prefixes (such as the
'X' in the examples above) have caused issues in the past.  As such,
please consider using a 2 or 3 character entry point prefix,
i.e., ``ABC`` is better than ``A`` but ``ABCD`` is invalid.
*A 3 letters entry point prefix followed by 3 numbers (i.e.* ``ABC123`` *)
is currently the longest allowed entry point name.*

.. _off-by-default:

If your plugin is intended to be opt-in, it can set the attribute
``off_by_default = True``. Users of your plugin will then need to utilize
:ref:`enable-extensions<option-enable-extensions>` with your plugin's entry
point.

.. seealso::

    The :external+setuptools:doc:`setuptools user guide <userguide/entry_point>`
    about entry points.
```

## File: `docs/source/release-notes/0.6.0.rst`
```
0.6 - 2010-02-15
----------------

- Fix the McCabe metric on some loops
```

## File: `docs/source/release-notes/0.7.0.rst`
```
0.7 - 2010-02-18
----------------

- Fix pep8 initialization when run through Hg
- Make pep8 short options work when run through the command line
- Skip duplicates when controlling files via Hg
```

## File: `docs/source/release-notes/0.8.0.rst`
```
0.8 - 2011-02-27
----------------

- fixed hg hook
- discard unexisting files on hook check
```

## File: `docs/source/release-notes/0.9.0.rst`
```
0.9 - 2011-11-09
----------------

- update pep8 version to 0.6.1
- mccabe check: gracefully handle compile failure
```

## File: `docs/source/release-notes/1.0.0.rst`
```
1.0 - 2011-11-29
----------------

- Deactivates by default the complexity checker
- Introduces the complexity option in the HG hook and the command line.
```

## File: `docs/source/release-notes/1.1.0.rst`
```
1.1 - 2012-02-14
----------------

- fixed the value returned by --version
- allow the flake8: header to be more generic
- fixed the "hg hook raises 'physical lines'" bug
- allow three argument form of raise
- now uses setuptools if available, for 'develop' command
```

## File: `docs/source/release-notes/1.2.0.rst`
```
1.2 - 2012-02-12
----------------

- added a git hook
- now Python 3 compatible
- mccabe and pyflakes have warning codes like pep8 now
```

## File: `docs/source/release-notes/1.3.0.rst`
```
1.3 - 2012-03-12
----------------

- fixed false W402 warning on exception blocks.
```

## File: `docs/source/release-notes/1.3.1.rst`
```
1.3.1 - 2012-05-19
------------------

- fixed support for Python 2.5
```

## File: `docs/source/release-notes/1.4.0.rst`
```
1.4 - 2012-07-12
----------------

- git_hook: Only check staged changes for compliance
- use pep8 1.2
```

## File: `docs/source/release-notes/1.5.0.rst`
```
1.5 - 2012-10-13
----------------

- fixed the stdin
- make sure mccabe catches the syntax errors as warnings
- pep8 upgrade
- added max_line_length default value
- added Flake8Command and entry points if setuptools is around
- using the setuptools console wrapper when available
```

## File: `docs/source/release-notes/1.6.0.rst`
```
1.6 - 2012-11-16
----------------

- changed the signatures of the ``check_file`` function in flake8/run.py,
  ``skip_warning`` in flake8/util.py and the ``check``, ``checkPath``
  functions in flake8/pyflakes.py.
- fix ``--exclude`` and ``--ignore`` command flags (#14, #19)
- fix the git hook that wasn't catching files not already added to the index
  (#29)
- pre-emptively includes the addition to pep8 to ignore certain lines.
  Add ``# nopep8`` to the end of a line to ignore it. (#37)
- ``check_file`` can now be used without any special prior setup (#21)
- unpacking exceptions will no longer cause an exception (#20)
- fixed crash on non-existent file (#38)
```

## File: `docs/source/release-notes/1.6.1.rst`
```
1.6.1 - 2012-11-24
------------------

- fixed the mercurial hook, a change from a previous patch was not properly
  applied
- fixed an assumption about warnings/error messages that caused an exception
  to be thrown when McCabe is used
```

## File: `docs/source/release-notes/1.6.2.rst`
```
1.6.2 - 2012-11-25
------------------

- fixed the NameError: global name 'message' is not defined (#46)
```

## File: `docs/source/release-notes/1.7.0.rst`
```
1.7.0 - 2012-12-21
------------------

- Fixes part of #35: Exception for no WITHITEM being an attribute of Checker
  for Python 3.3
- Support stdin
- Incorporate @phd's builtins pull request
- Fix the git hook
- Update pep8.py to the latest version
```

## File: `docs/source/release-notes/2.0.0.rst`
```
2.0.0 - 2013-02-23
------------------

- Pyflakes errors are prefixed by an ``F`` instead of an ``E``
- McCabe complexity warnings are prefixed by a ``C`` instead of a ``W``
- Flake8 supports extensions through entry points
- Due to the above support, we **require** setuptools
- We publish the `documentation <https://flake8.readthedocs.io/>`_
- Fixes #13: pep8, pyflakes and mccabe become external dependencies
- Split run.py into main.py, engine.py and hooks.py for better logic
- Expose our parser for our users
- New feature: Install git and hg hooks automagically
- By relying on pyflakes (0.6.1), we also fixed #45 and #35
```

## File: `docs/source/release-notes/2.1.0.rst`
```
2.1.0 - 2013-10-26
------------------

- Add FLAKE8_LAZY and FLAKE8_IGNORE environment variable support to git and
  mercurial hooks
- Force git and mercurial hooks to repsect configuration in setup.cfg
- Only check staged files if that is specified
- Fix hook file permissions
- Fix the git hook on python 3
- Ignore non-python files when running the git hook
- Ignore .tox directories by default
- Flake8 now reports the column number for PyFlakes messages
```

## File: `docs/source/release-notes/2.2.0.rst`
```
2.2.0 - 2014-06-22
------------------

- New option ``doctests`` to run Pyflakes checks on doctests too
- New option ``jobs`` to launch multiple jobs in parallel
- Turn on using multiple jobs by default using the CPU count
- Add support for ``python -m flake8`` on Python 2.7 and Python 3
- Fix Git and Mercurial hooks: issues #88, #133, #148 and #149
- Fix crashes with Python 3.4 by upgrading dependencies
- Fix traceback when running tests with Python 2.6
- Fix the setuptools command ``python setup.py flake8`` to read
  the project configuration
```

## File: `docs/source/release-notes/2.2.1.rst`
```
2.2.1 - 2014-06-30
------------------

- Turn off multiple jobs by default. To enable automatic use of all CPUs, use
  ``--jobs=auto``. Fixes #155 and #154.
```

## File: `docs/source/release-notes/2.2.2.rst`
```
2.2.2 - 2014-07-04
------------------

- Re-enable multiprocessing by default while fixing the issue Windows users
  were seeing.
```

## File: `docs/source/release-notes/2.2.3.rst`
```
2.2.3 - 2014-08-25
------------------

- Actually turn multiprocessing on by default
```

## File: `docs/source/release-notes/2.2.4.rst`
```
2.2.4 - 2014-10-09
------------------

- Fix bugs triggered by turning multiprocessing on by default (again)

  Multiprocessing is forcibly disabled in the following cases:

  - Passing something in via stdin

  - Analyzing a diff

  - Using windows

- Fix --install-hook when there are no config files present for pep8 or
  flake8.

- Fix how the setuptools command parses excludes in config files

- Fix how the git hook determines which files to analyze (Thanks Chris
  Buccella!)
```

## File: `docs/source/release-notes/2.2.5.rst`
```
2.2.5 - 2014-10-19
------------------

- Flush standard out when using multiprocessing

- Make the check for "# flake8: noqa" more strict
```

## File: `docs/source/release-notes/2.3.0.rst`
```
2.3.0 - 2015-01-04
------------------

- **Feature**: Add ``--output-file`` option to specify a file to write to
  instead of ``stdout``.

- **Bug** Fix interleaving of output while using multiprocessing
  (:issue:`60`)
```

## File: `docs/source/release-notes/2.4.0.rst`
```
2.4.0 - 2015-03-07
------------------

- **Bug** Print filenames when using multiprocessing and ``-q`` option.
  (:issue:`74`)

- **Bug** Put upper cap on dependencies. The caps for 2.4.0 are:

  - ``pep8 < 1.6`` (Related to :issue:`78`)

  - ``mccabe < 0.4``

  - ``pyflakes < 0.9``

  See also :issue:`75`

- **Bug** Files excluded in a config file were not being excluded when flake8
  was run from a git hook. (:issue:`2`)

- **Improvement** Print warnings for users who are providing mutually
  exclusive options to flake8. (:issue:`51`, :issue:`386`)

- **Feature** Allow git hook configuration to live in ``.git/config``.
  See the updated `VCS hooks docs`_ for more details. (:issue:`387`)

.. _VCS hooks docs: https://flake8.readthedocs.io/en/latest/user/using-hooks.html
```

## File: `docs/source/release-notes/2.4.1.rst`
```
2.4.1 - 2015-05-18
------------------

- **Bug** Do not raise a ``SystemError`` unless there were errors in the
  setuptools command. (:issue:`82`, :issue:`390`)

- **Bug** Do not verify dependencies of extensions loaded via entry-points.

- **Improvement** Blacklist versions of pep8 we know are broken
```

## File: `docs/source/release-notes/2.5.0.rst`
```
2.5.0 - 2015-10-26
------------------

- **Improvement** Raise cap on PyFlakes for Python 3.5 support

- **Improvement** Avoid deprecation warnings when loading extensions
  (:issue:`102`, :issue:`445`)

- **Improvement** Separate logic to enable "off-by-default" extensions
  (:issue:`110`)

- **Bug** Properly parse options to setuptools Flake8 command (:issue:`408`)

- **Bug** Fix exceptions when output on stdout is truncated before Flake8
  finishes writing the output (:issue:`112`)

- **Bug** Fix error on OS X where Flake8 can no longer acquire or create new
  semaphores (:issue:`117`)
```

## File: `docs/source/release-notes/2.5.1.rst`
```
2.5.1 - 2015-12-08
------------------

- **Bug** Properly look for ``.flake8`` in current working directory
  (:issue:`458`)

- **Bug** Monkey-patch ``pep8.stdin_get_value`` to cache the actual value in
  stdin. This helps plugins relying on the function when run with
  multiprocessing. (:issue:`460`, :issue:`462`)
```

## File: `docs/source/release-notes/2.5.2.rst`
```
2.5.2 - 2016-01-30
------------------

- **Bug** Parse ``output_file`` and ``enable_extensions`` from config files

- **Improvement** Raise upper bound on mccabe plugin to allow for version
  0.4.0
```

## File: `docs/source/release-notes/2.5.3.rst`
```
2.5.3 - 2016-02-11
------------------

- **Bug** Actually parse ``output_file`` and ``enable_extensions`` from config
  files
```

## File: `docs/source/release-notes/2.5.4.rst`
```
2.5.4 - 2016-02-11
------------------

- **Bug** Missed an attribute rename during the v2.5.3 release.
```

## File: `docs/source/release-notes/2.5.5.rst`
```
2.5.5 - 2016-06-14
------------------

- **Bug** Fix setuptools integration when parsing config files

- **Bug** Don't pass the user's config path as the config_file when creating a
  StyleGuide
```

## File: `docs/source/release-notes/2.6.0.rst`
```
2.6.0 - 2016-06-15
------------------

- **Requirements Change** Switch to pycodestyle as all future pep8 releases
  will use that package name

- **Improvement** Allow for Windows users on *select* versions of Python to
  use ``--jobs`` and multiprocessing

- **Improvement** Update bounds on McCabe

- **Improvement** Update bounds on PyFlakes and blacklist known broken
  versions

- **Improvement** Handle new PyFlakes warning with a new error code: F405
```

## File: `docs/source/release-notes/2.6.1.rst`
```
2.6.1 - 2016-06-25
------------------

- **Bug** Update the config files to search for to include ``setup.cfg`` and
  ``tox.ini``. This was broken in 2.5.5 when we stopped passing
  ``config_file`` to our Style Guide
```

## File: `docs/source/release-notes/2.6.2.rst`
```
2.6.2 - 2016-06-25
------------------

- **Bug** Fix packaging error during release process.
```

## File: `docs/source/release-notes/3.0.0.rst`
```
3.0.0 -- 2016-07-25
-------------------

- Rewrite our documentation from scratch! (https://flake8.pycqa.org)

- Drop explicit support for Pythons 2.6, 3.2, and 3.3.

- Remove dependence on pep8/pycodestyle for file processing, plugin
  dispatching, and more. We now control all of this while keeping backwards
  compatibility.

- ``--select`` and ``--ignore`` can now both be specified and try to find the
  most specific rule from each. For example, if you do ``--select E --ignore
  E123`` then we will report everything that starts with ``E`` except for
  ``E123``. Previously, you would have had to do ``--ignore E123,F,W`` which
  will also still work, but the former should be far more intuitive.

- Add support for in-line ``# noqa`` comments to specify **only** the error
  codes to be ignored, e.g., ``# noqa: E123,W503``

- Add entry-point for formatters as well as a base class that new formatters
  can inherit from. See the documentation for more details.

- Add detailed verbose output using the standard library logging module.

- Enhance our usage of optparse for plugin developers by adding new parameters
  to the ``add_option`` that plugins use to register new options.

- Update ``--install-hook`` to require the name of version control system hook
  you wish to install a Flake8.

- Stop checking sub-directories more than once via the setuptools command

- When passing a file on standard-in, allow the caller to specify
  ``--stdin-display-name`` so the output is properly formatted

- The Git hook now uses ``sys.executable`` to format the shebang line.
  This allows Flake8 to install a hook script from a virtualenv that points to
  that virtualenv's Flake8 as opposed to a global one (without the virtualenv
  being sourced).

- Print results in a deterministic and consistent ordering when used with
  multiprocessing

- When using ``--count``, the output is no longer written to stderr.

- AST plugins can either be functions or classes and all plugins can now
  register options so long as there are callable attributes named as we
  expect.

- Stop forcibly re-adding ``.tox``, ``.eggs``, and ``*.eggs`` to
  ``--exclude``. Flake8 2.x started always appending those three patterns
  to any exclude list (including the default and any user supplied list).
  Flake8 3 has stopped adding these in, so you may see errors when upgrading
  due to these patterns no longer being forcibly excluded by default if you
  have your own exclude patterns specified.

  To fix this, add the appropriate patterns to your exclude patterns list.

  .. note::

      This item was added in November of 2016, as a result of a bug
      report.
```

## File: `docs/source/release-notes/3.0.1.rst`
```
3.0.1 -- 2016-07-25
-------------------

- Fix regression in handling of ``# noqa`` for multiline strings.
  (See also :issue:`1024`)

- Fix regression in handling of ``--output-file`` when not also using
  ``--verbose``. (See also :issue:`1026`)

- Fix regression in handling of ``--quiet``. (See also :issue:`1026`)

- Fix regression in handling of ``--statistics``. (See also :issue:`1026`)
```

## File: `docs/source/release-notes/3.0.2.rst`
```
3.0.2 -- 2016-07-26
-------------------

- Fix local config file discovery.  (See also :issue:`528`)

- Fix indexing of column numbers. We accidentally were starting column indices
  at 0 instead of 1.

- Fix regression in handling of errors like E402 that rely on a combination of
  attributes. (See also :issue:`530`)
```

## File: `docs/source/release-notes/3.0.3.rst`
```
3.0.3 -- 2016-07-30
-------------------

- Disable ``--jobs`` for any version of Python on Windows.
  (See also `this Python bug report`_)

- Raise exception when entry_point in plugin not callable.
  This raises an informative error when a plugin fails to load because its
  entry_point is not callable, which can happen with a plugin which is buggy or
  not updated for the current version of flake8. This is nicer than raising a
  `PicklingError` about failing to pickle a module (See also :issue:`1014`)

- Fix ``# noqa`` comments followed by a ``:`` and explanation broken by
  3.0.0 (See also :issue:`1025`)

- Always open our output file in append mode so we do not overwrite log
  messages. (See also :issue:`535`)

- When normalizing path values read from configuration, keep in context the
  directory where the configuration was found so that relative paths work.
  (See also :issue:`1036`)

- Fix issue where users were unable to ignore plugin errors that were on
  by default. (See also :issue:`1037`)

- Fix our legacy API StyleGuide's ``init_report`` method to actually override
  the previous formatter. (See also :issue:`136`)


.. links
.. _this Python bug report:
    https://bugs.python.org/issue27649
```

## File: `docs/source/release-notes/3.0.4.rst`
```
3.0.4 -- 2016-08-08
-------------------

- Side-step a Pickling Error when using Flake8 with multiprocessing on Unix
  systems. (See also :issue:`1014`)

- Fix an Attribute Error raised when dealing with Invalid Syntax. (See also
  :issue:`539`)

- Fix an unhandled Syntax Error when tokenizing files. (See also
  :issue:`540`)
```

## File: `docs/source/release-notes/3.1.0.rst`
```
3.1.0 -- 2016-11-14
-------------------

You can view the `3.1.0 milestone`_ on GitHub for more details.

- Add ``--bug-report`` flag to make issue reporters' lives easier.

- Collect configuration files from the current directory when using our Git
  hook. (See also :issue:`142`, :issue:`150`, :issue:`155`)

- Avoid unhandled exceptions when dealing with SyntaxErrors. (See also
  :issue:`146`, :issue:`170`)

- Exit early if the value for ``--diff`` is empty. (See also :issue:`158`)

- Handle empty ``--stdin-display-name`` values. (See also :issue:`167`)

- Properly report the column number of Syntax Errors. We were assuming that
  all reports of column numbers were 0-indexed, however, SyntaxErrors report
  the column number as 1-indexed. This caused us to report a column number
  that was 1 past the actual position. Further, when combined with
  SyntaxErrors that occur at a newline, this caused the position to be
  visually off by two. (See also :issue:`169`)

- Fix the behaviour of ``--enable-extensions``. Previously, items specified
  here were still ignored due to the fact that the off-by-default extension
  codes were being left in the ``ignore`` list. (See also :issue:`171`)

- Fix problems around ``--select`` and ``--ignore`` behaviour that prevented
  codes that were neither explicitly selected nor explicitly ignored from
  being reported. (See also :issue:`174`)

- Truly be quiet when the user specifies ``-q`` one or more times. Previously,
  we were showing the if the user specified ``-q`` and ``--show-source``. We
  have fixed this bug. (See also :issue:`177`)

- Add new File Processor attribute, ``previous_unindented_logical_line`` to
  accommodate pycodestyle 2.1.0. (See also :issue:`178`)

- When something goes wrong, exit non-zero. (See also :issue:`180`,
  :issue:`141`)

- Add ``--tee`` as an option to allow use of ``--output-file`` and printing to
  standard out.

- Allow the git plugin to actually be lazy when collecting files.

- Allow for pycodestyle 2.1 series and pyflakes 1.3 series.

.. links
.. _3.1.0 milestone:
    https://github.com/pycqa/flake8/milestone/12
```

## File: `docs/source/release-notes/3.1.1.rst`
```
3.1.1 -- 2016-11-14
-------------------

You can view the `3.1.1 milestone`_ on GitHub for more details.

- Do not attempt to install/distribute a ``man`` file with the Python package;
  leave this for others to do. (See also :issue:`186`)

- Fix packaging bug where wheel version constraints specified in setup.cfg did
  not match the constraints in setup.py. (See also :issue:`187`)

.. links
.. _3.1.1 milestone:
    https://github.com/pycqa/flake8/milestone/13
```

## File: `docs/source/release-notes/3.2.0.rst`
```
3.2.0 -- 2016-11-14
-------------------

You can view the `3.2.0 milestone`_ on GitHub for more details.

- Allow for pycodestyle 2.2.0 which fixes a bug in E305 (See also
  :issue:`188`)

.. links
.. _3.2.0 milestone:
    https://github.com/pycqa/flake8/milestone/14
```

## File: `docs/source/release-notes/3.2.1.rst`
```
3.2.1 -- 2016-11-21
-------------------

You can view the `3.2.1 milestone`_ on GitHub for more details.

- Fix subtle bug when deciding whether to report an on-by-default's violation
  (See also :issue:`189`)

- Fix another bug around SyntaxErrors not being reported at the right column
  and row (See also :issue:`191` and :issue:`169` for a related, previously
  fixed bug)

- Fix regression from 2.x where we run checks against explicitly provided
  files, even if they don't match the filename patterns. (See also
  :issue:`198`)

.. links
.. _3.2.1 milestone:
    https://github.com/pycqa/flake8/milestone/15
```

## File: `docs/source/release-notes/3.3.0.rst`
```
3.3.0 -- 2017-02-06
-------------------

You can view the `3.3.0 milestone`_ on GitHub for more details.

- Add support for Python 3.6 (via dependencies). **Note** Flake8 does not
  guarantee that all plugins will support Python 3.6.

- Added unique error codes for all missing PyFlakes messages. (14 new
  codes, see "Error / Violation Codes")

- Dramatically improve the performance of Flake8. (See also :issue:`829`)

- Display the local file path instead of the temporary file path when
  using the git hook. (See also :issue:`176`)

- Add methods to Report class that will be called when Flake8 starts and
  finishes processing a file. (See also :issue:`183`)

- Fix problem where hooks should only check \*.py files. (See also
  :issue:`200`)

- Fix handling of SyntaxErrors that do not include physical line information.
  (See also :issue:`542`)

- Update upper bound on PyFlakes to allow for PyFlakes 1.5.0.  (See also
  :issue:`549`)

- Update setuptools integration to less eagerly deduplicate packages.
  (See also :issue:`552`)

- Force ``flake8 --version`` to be repeatable between invocations. (See also
  :issue:`554`)

.. all links
.. _3.3.0 milestone:
    https://github.com/pycqa/flake8/milestone/16
```

## File: `docs/source/release-notes/3.4.0.rst`
```
3.4.0 -- 2017-07-27
-------------------

You can view the `3.4.0 milestone`_ on GitHub for more details.

- Refine logic around ``--select`` and ``--ignore`` when combined with the
  default values for each. (See also :issue:`572`)

- Handle spaces as an alternate separate for error codes, e.g.,
  ``--ignore 'E123 E234'``. (See also :issue:`580`)

- Filter out empty select and ignore codes, e.g., ``--ignore E123,,E234``.
  (See also :issue:`581`)

- Specify dependencies appropriately in ``setup.py`` (See also :issue:`592`)

- Fix bug in parsing ``--quiet`` and ``--verbose`` from config files.
  (See also :issue:`1169`)

- Remove unused import of ``os`` in the git hook template (See also
  :issue:`1170`)

.. all links
.. _3.4.0 milestone:
    https://github.com/pycqa/flake8/milestone/17
```

## File: `docs/source/release-notes/3.4.1.rst`
```
3.4.1 -- 2017-07-28
-------------------

You can view the `3.4.1 milestone`_ on GitHub for more details.

- Fix minor regression when users specify only a ``--select`` list with items
  in the enabled/extended select list.  (See also :issue:`605`)

.. all links
.. _3.4.1 milestone:
    https://github.com/pycqa/flake8/milestone/18
```

## File: `docs/source/release-notes/3.5.0.rst`
```
3.5.0 -- 2017-10-23
-------------------

You can view the `3.5.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Allow for PyFlakes 1.6.0 (See also :issue:`1058`)

- Start using new PyCodestyle checks for bare excepts and ambiguous identifier
  (See also :issue:`611`)

Features
~~~~~~~~

- Print out information about configuring VCS hooks (See also :issue:`586`)

- Allow users to develop plugins "local" to a repository without using
  setuptools. See our documentation on local plugins for more information.
  (See also :issue:`608`)

Bugs Fixed
~~~~~~~~~~

- Catch and helpfully report ``UnicodeDecodeError``\ s when parsing
  configuration files. (See also :issue:`609`)


.. all links
.. _3.5.0 milestone:
    https://github.com/pycqa/flake8/milestone/19
```

## File: `docs/source/release-notes/3.6.0.rst`
```
3.6.0 -- 2018-10-23
-------------------

You can view the `3.6.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycodestyle has been updated to >= 2.4.0, < 2.5.0 (See also :issue:`1068`,
  :issue:`652`, :issue:`869`, :issue:`881`, :issue:`1239`)

- Pyflakes has been updated to >= 2.0.0, < 2.1.0 (See also :issue:`655`,
  :issue:`883`)

- flake8 requires python 2.x >= 2.7 or python 3.x >= 3.4 (See also
  :issue:`876`)

Features
~~~~~~~~

- Add ``paths`` to allow local plugins to exist outside of ``sys.path`` (See
  also :issue:`1067`, :issue:`1237`)

- Copy ``setup.cfg`` files to the temporary git hook execution directory (See
  also :issue:`1299`)

- Only skip a file if ``# flake8: noqa`` is on a line by itself (See also
  :issue:`259`, :issue:`873`)

- Provide a better user experience for broken plugins (See also :issue:`1178`)

- Report ``E902`` when a file passed on the command line does not exist (See
  also :issue:`645`, :issue:`878`)

- Add ``--extend-ignore`` for extending the default ``ignore`` instead of
  overriding it (See also :issue:`1061`, :issue:`1180`)

Bugs Fixed
~~~~~~~~~~

- Respect a formatter's newline setting when printing (See also :issue:`1238`)

- Fix leaking of processes in the legacy api (See also :issue:`650`,
  :issue:`879`)

- Fix a ``SyntaxWarning`` for an invalid escape sequence (See also
  :issue:`1186`)

- Fix ``DeprecationWarning`` due to import of ``abc`` classes from the
  ``collections`` module (See also :issue:`887`)

- Defer ``setuptools`` import to improve flake8 startup time (See also
  :issue:`1190`)

- Fix inconsistent line endings in ``FileProcessor.lines`` when running under
  python 3.x (See also :issue:`263`, :issue:`889`)


.. all links
.. _3.6.0 milestone:
    https://github.com/pycqa/flake8/milestone/20
```

## File: `docs/source/release-notes/3.7.0.rst`
```
3.7.0 -- 2019-01-29
-------------------

You can view the `3.7.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add dependency on ``entrypoints`` >= 0.3, < 0.4 (See also :issue:`897`,
  :issue:`1197`)

- Pyflakes has been updated to >= 2.1.0, < 2.2.0 (See also :issue:`912`,
  :issue:`913`)

- pycodestyle has been updated to >= 2.5.0, < 2.6.0 (See also :issue:`915`)

Features
~~~~~~~~

- Add support for ``per-file-ignores`` (See also :issue:`892`, :issue:`511`,
  :issue:`911`, :issue:`277`)

- Enable use of ``float`` and ``complex`` option types (See also :issue:`894`,
  :issue:`258`)

- Improve startup performance by switching from ``pkg_resources`` to
  ``entrypoints`` (See also :issue:`897`)

- Add metadata for use through the `pre-commit`_ git hooks framework (See also
  :issue:`901`, :issue:`1196`)

- Allow physical line checks to return more than one result (See also
  :issue:`902`)

- Allow ``# noqa:X123`` comments without space between the colon and codes
  list (See also :issue:`906`, :issue:`276`)

- Remove broken and unused ``flake8.listen`` plugin type (See also
  :issue:`907`, :issue:`663`)

.. all links
.. _3.7.0 milestone:
    https://github.com/pycqa/flake8/milestone/22
.. _pre-commit:
    https://pre-commit.com/
```

## File: `docs/source/release-notes/3.7.1.rst`
```
3.7.1 -- 2019-01-30
-------------------

You can view the `3.7.1 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix capitalized filenames in ``per-file-ignores`` setting (See also
  :issue:`917`, :issue:`287`)

.. all links
.. _3.7.1 milestone:
    https://github.com/pycqa/flake8/milestone/23
```

## File: `docs/source/release-notes/3.7.2.rst`
```
3.7.2 -- 2019-01-30
-------------------

You can view the `3.7.2 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix broken ``flake8 --diff`` (regressed in 3.7.0) (See also :issue:`919`,
  :issue:`667`)

- Fix typo in plugin exception reporting (See also :issue:`908`,
  :issue:`668`)

- Fix ``AttributeError`` while attempting to use the legacy api (regressed in
  3.7.0) (See also :issue:`1198`, :issue:`673`)

.. all links
.. _3.7.2 milestone:
    https://github.com/pycqa/flake8/milestone/24
```

## File: `docs/source/release-notes/3.7.3.rst`
```
3.7.3 -- 2019-01-30
-------------------

You can view the `3.7.3 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix imports of ``typing`` in python 3.5.0 / 3.5.1 (See also :issue:`1199`,
  :issue:`674`)

- Fix ``flake8 --statistics`` (See also :issue:`920`, :issue:`675`)

- Gracefully ignore ``flake8-per-file-ignores`` plugin if installed (See also
  :issue:`1201`, :issue:`671`)

- Improve error message for malformed ``per-file-ignores`` (See also
  :issue:`921`, :issue:`288`)


.. all links
.. _3.7.3 milestone:
    https://github.com/pycqa/flake8/milestone/25
```

## File: `docs/source/release-notes/3.7.4.rst`
```
3.7.4 -- 2019-01-31
-------------------

You can view the `3.7.4 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix performance regression with lots of ``per-file-ignores`` and errors
  (See also :issue:`922`, :issue:`677`)


.. all links
.. _3.7.4 milestone:
    https://github.com/pycqa/flake8/milestone/26
```

## File: `docs/source/release-notes/3.7.5.rst`
```
3.7.5 -- 2019-02-04
-------------------

You can view the `3.7.5 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix reporting of pyflakes "referenced before assignment" error (See also
  :issue:`923`, :issue:`679`)


.. all links
.. _3.7.5 milestone:
    https://github.com/pycqa/flake8/milestone/27
```

## File: `docs/source/release-notes/3.7.6.rst`
```
3.7.6 -- 2019-02-18
-------------------

You can view the `3.7.6 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix ``--per-file-ignores`` for multi-letter error codes (See also
  :issue:`1203`, :issue:`683`)

- Improve flake8 speed when only 1 filename is passed (See also :issue:`1204`)


.. all links
.. _3.7.6 milestone:
    https://github.com/pycqa/flake8/milestone/28
```

## File: `docs/source/release-notes/3.7.7.rst`
```
3.7.7 -- 2019-02-25
-------------------

You can view the `3.7.7 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix crashes in plugins causing ``flake8`` to hang while unpickling errors
  (See also :issue:`1206`, :issue:`681`)


.. all links
.. _3.7.7 milestone:
    https://github.com/pycqa/flake8/milestone/29
```

## File: `docs/source/release-notes/3.7.8.rst`
```
3.7.8 -- 2019-07-08
-------------------

You can view the `3.7.8 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix handling of ``Application.parse_preliminary_options_and_args`` when
  argv is an empty list (See also :issue:`1303`, :issue:`694`)

- Fix crash when a file parses but fails to tokenize (See also :issue:`1210`,
  :issue:`1088`)

- Log the full traceback on plugin exceptions (See also :issue:`926`)

- Fix ``# noqa: ...`` comments with multi-letter codes (See also :issue:`931`,
  :issue:`1101`)


.. all links
.. _3.7.8 milestone:
    https://github.com/pycqa/flake8/milestone/30
```

## File: `docs/source/release-notes/3.7.9.rst`
```
3.7.9 -- 2019-10-28
-------------------

You can view the `3.7.9 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Disable multiprocessing when the multiprocessing method is ``spawn`` (such
  as on macos in python3.8) (See also :issue:`956`, :issue:`315`)


.. all links
.. _3.7.9 milestone:
    https://github.com/pycqa/flake8/milestone/32
```

## File: `docs/source/release-notes/3.8.0.rst`
```
3.8.0 -- 2020-05-11
-------------------

You can view the `3.8.0 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix logical checks which report positions out of bounds (See also
  :issue:`987`, :issue:`723`)

- Fix ``--exclude=.*`` accidentally matching ``.`` and ``..`` (See also
  :issue:`441`, :issue:`360`)

Deprecations
~~~~~~~~~~~~

- Add deprecation message for vcs hooks (See also :issue:`985`,
  :issue:`296`)


3.8.0a2 -- 2020-04-24
---------------------

You can view the `3.8.0 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix ``type="str"`` optparse options (See also :issue:`984`)


3.8.0a1 -- 2020-04-24
---------------------

You can view the `3.8.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove dependency on ``entrypoints`` and add dependency on
  ``importlib-metadata`` (only for ``python<3.8``) (See also :issue:`1297`,
  :issue:`297`)

- Pyflakes has been updated to >= 2.2.0, < 2.3.0 (See also :issue:`982`)

- pycodestyle has been updated to >= 2.6.0a1, < 2.7.0 (See also :issue:`983`)

Features
~~~~~~~~

- Add ``--extend-exclude`` option to add to ``--exclude`` without overwriting
  (See also :issue:`1211`, :issue:`1091`)

- Move argument parsing from ``optparse`` to ``argparse`` (See also
  :issue:`939`

- Group plugin options in ``--help`` (See also :issue:`1219`, :issue:`294`)

- Remove parsing of ``verbose`` from configuration files as it was not
  consistently applied (See also :issue:`1245`, :issue:`245`)

- Remove parsing of ``output_file`` from configuration files as it was not
  consistently applied (See also :issue:`1246`)

- Resolve configuration files relative to ``cwd`` instead of common prefix of
  passed filenames.  You may need to change ``flake8 subproject`` to
  ``cd subproject && flake8 .`` (See also :issue:`952`)

- Officially support python3.8 (See also :issue:`963`)

- ``--disable-noqa`` now also disables ``# flake8: noqa`` (See also
  :issue:`1296`, :issue:`318`)

- Ensure that a missing file produces a ``E902`` error (See also :issue:`1262`,
  :issue:`328`)

- ``# noqa`` comments now apply to all of the lines in an explicit ``\``
  continuation or in a line continued by a multi-line string (See also
  :issue:`1266`, :issue:`621`)

Bugs Fixed
~~~~~~~~~~

- Fix ``--exclude=./t.py`` to only match ``t.py`` at the top level (See also
  :issue:`1208`, :issue:`628`)

- Fix ``--show-source`` when a file is indented with tabs (See also
  :issue:`1218`, :issue:`719`)

- Fix crash when ``--max-line-length`` is given a non-integer (See also
  :issue:`939`, :issue:`704`)

- Prevent flip-flopping of ``indent_char`` causing extra ``E101`` errors (See
  also :issue:`949`, `pycodestyle#886`_)

- Only enable multiprocessing when the method is ``fork`` fixing issues
  on macos with python3.8+ (See also :issue:`955`, :issue:`315`) (note: this
  fix also landed in 3.7.9)

- ``noqa`` is now only handled by flake8 fixing specific-noqa.  Plugins
  requesting this parameter will always receive ``False`` (See also
  :issue:`1214`, :issue:`1104`)

- Fix duplicate loading of plugins when invoked via ``python -m flake8`` (See
  also :issue:`1297`)

- Fix early exit when ``--exit-zero`` and ``--diff`` are provided and the diff
  is empty (See also :issue:`970`)

- Consistently split lines when ``\f`` is present when reading from stdin (See
  also :issue:`976`, :issue:`202`)

Deprecations
~~~~~~~~~~~~

- ``python setup.py flake8`` (setuptools integration) is now deprecated and
  will be removed in a future version (See also :issue:`935`, :issue:`1098`)

- ``type='string'`` (optparse) types are deprecated, use
  ``type=callable`` (argparse) instead.  Support for ``type='string'`` will
  be removed in a future version (See also :issue:`939`)

- ``%default`` in plugin option help text is deprecated, use ``%(default)s``
  instead.  Support for ``%default`` will be removed in a future version (See
  also :issue:`939`)

- optparse-style ``action='callback'`` setting for options is deprecated, use
  argparse action classes instead.  This will be removed in a future version
  (See also :issue:`939`)


.. all links
.. _3.8.0 milestone:
    https://github.com/pycqa/flake8/milestone/31

.. issue links
.. _pycodestyle#886:
   https://github.com/PyCQA/pycodestyle/issues/886
```

## File: `docs/source/release-notes/3.8.1.rst`
```
3.8.1 -- 2020-05-11
-------------------

You can view the `3.8.1 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix ``--output-file`` (regression in 3.8.0) (See also :issue:`990`,
  :issue:`725`)


.. all links
.. _3.8.1 milestone:
    https://github.com/pycqa/flake8/milestone/33
```

## File: `docs/source/release-notes/3.8.2.rst`
```
3.8.2 -- 2020-05-22
-------------------

You can view the `3.8.2 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Improve performance by eliminating unnecessary sort (See also :issue:`991`)

- Improve messaging of ``--jobs`` argument by utilizing ``argparse`` (See also
  :issue:`1269`, :issue:`1110`)

- Fix file configuration options to be relative to the config passed on the
  command line (See also :issue:`442`, :issue:`736`)

- Fix incorrect handling of ``--extend-exclude`` by treating its values as
  files (See also :issue:`1271`, :issue:`738`)

.. all links
.. _3.8.2 milestone:
    https://github.com/pycqa/flake8/milestone/34
```

## File: `docs/source/release-notes/3.8.3.rst`
```
3.8.3 -- 2020-06-08
-------------------

You can view the `3.8.3 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Also catch ``SyntaxError`` when tokenizing (See also :issue:`992`,
  :issue:`747`)

- Fix ``--jobs`` default display in ``flake8 --help`` (See also :issue:`1272`,
  :issue:`750`)

.. all links
.. _3.8.3 milestone:
    https://github.com/pycqa/flake8/milestone/35
```

## File: `docs/source/release-notes/3.8.4.rst`
```
3.8.4 -- 2020-10-02
-------------------

You can view the `3.8.4 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix multiprocessing errors on platforms without ``sem_open`` syscall.  (See
  also :issue:`1282`)

- Fix skipping of physical checks on the last line of a file which does not
  end in a newline (See also :issue:`997`)

.. all links
.. _3.8.4 milestone:
    https://github.com/pycqa/flake8/milestone/36
```

## File: `docs/source/release-notes/3.9.0.rst`
```
3.9.0 -- 2021-03-14
-------------------

You can view the `3.9.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Pyflakes has been updated to >= 2.3.0, < 2.4.0 (See also :issue:`1006`)

- pycodestyle has been updated to >= 2.7.0, < 2.8.0 (See also :issue:`1007`)

Deprecations
~~~~~~~~~~~~

- Drop support for python 3.4 (See also :issue:`1283`)

Features
~~~~~~~~

- Add ``--no-show-source`` option to disable ``--show-source`` (See also
  :issue:`995`)

Bugs Fixed
~~~~~~~~~~

- Fix handling of ``crlf`` line endings when linting stdin (See also
  :issue:`1002`)


.. all links
.. _3.9.0 milestone:
    https://github.com/pycqa/flake8/milestone/37
```

## File: `docs/source/release-notes/3.9.1.rst`
```
3.9.1 -- 2021-04-15
-------------------

You can view the `3.9.1 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix codes being ignored by plugins utilizing ``extend_default_ignore`` (See
  also :pull:`1317`)


.. all links
.. _3.9.1 milestone:
    https://github.com/PyCQA/flake8/milestone/38
```

## File: `docs/source/release-notes/3.9.2.rst`
```
3.9.2 -- 2021-05-08
-------------------

You can view the `3.9.2 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix error message for ``E111`` in ``pycodestyle`` (See also :pull:`1328`,
  :issue:`1327`).

Deprecations
~~~~~~~~~~~~

- ``indent_size_str`` is deprecated, use ``str(indent_size)`` instead (See
  also :pull:`1328`, :issue:`1327`).


.. all links
.. _3.9.2 milestone:
    https://github.com/PyCQA/flake8/milestone/40
```

## File: `docs/source/release-notes/4.0.0.rst`
```
4.0.0 -- 2021-10-10
-------------------

You can view the `4.0.0 milestone`_ on GitHub for more details.

Backwards Incompatible Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove ``--install-hook`` vcs integration (See also :issue:`1008`).
- Remove ``setuptools`` command (See also :issue:`1009`).
- Migrate from GitLab to GitHub (See also :pull:`1305`).
- Due to constant confusion by users, user-level |Flake8| configuration files
  are no longer supported. Files will not be searched for in the user's home
  directory (e.g., ``~/.flake8``) nor in the XDG config directory (e.g.,
  ``~/.config/flake8``).  (See also :pull:`1404`).

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycodestyle has been updated to >= 2.8.0, < 2.9.0 (See also :pull:`1406`).
- Pyflakes has been updated to >= 2.4.0, < 2.5.0 (See also :pull:`1406`).
- flake8 requires python >= 3.6 (See also :issue:`1010`).

Features
~~~~~~~~

- Add ``--extend-select`` option (See also :pull:`1312` :issue:`1061`).
- Automatically create directories for output files (See also :pull:`1329`).

Bugs Fixed
~~~~~~~~~~

- ``ast`` parse before tokenizing to improve ``SyntaxError`` errors (See also
  :pull:`1320` :issue:`740`).
- Fix warning in ``--indent-size`` argparse help (See also :pull:`1367`).
- Fix handling ``SyntaxError`` in python 3.10+ (See also :pull:`1374`
  :issue:`1372`).
- Fix writing non-cp1252-encodable when output is piped on windows (See also
  :pull:`1382` :issue:`1381`).

.. all links
.. _4.0.0 milestone:
    https://github.com/PyCQA/flake8/milestone/39
```

## File: `docs/source/release-notes/4.0.1.rst`
```
4.0.1 -- 2021-10-11
-------------------

You can view the `4.0.1 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix parallel execution collecting a ``SyntaxError`` (See also :pull:`1410`
  :issue:`1408`).


.. all links
.. _4.0.1 milestone:
    https://github.com/PyCQA/flake8/milestone/41
```

## File: `docs/source/release-notes/5.0.0.rst`
```
5.0.0 -- 2022-07-30
-------------------

You can view the `5.0.0 milestone`_ on GitHub for more details.

Backwards Incompatible Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove ``indent_size_str`` (See also :pull:`1411`).
- Remove some dead code (See also :pull:`1453`, :pull:`1540`, :pull:`1541`).
- Missing explicitly-specified configuration is now an error (See also
  :issue:`1497`, :pull:`1498`).
- Always read configuration files as UTF-8 (See also :issue:`1532`,
  :pull:`1533`).
- Remove manpage from docs -- use ``help2man`` or related tools instead (See
  also :pull:`1557`).
- Forbid invalid plugin codes (See also :issue:`325`, :pull:`1579`).


Deprecations
~~~~~~~~~~~~

- Deprecate ``--diff`` option (See also :issue:`1389`, :pull:`1441`).


New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycodestyle has been updated to >= 2.9.0, < 2.10.0 (See also :pull:`1626`).
- Pyflakes has been updated to >= 2.5.0, < 2.6.0 (See also :pull:`1625`).
- mccabe has been updated to >= 0.7.0, < 0.8.0 (See also :pull:`1542`).


Features
~~~~~~~~

- Add colors to output, configurable via ``--color`` (See also :issue:`1379`,
  :pull:`1440`).
- Add ``.nox`` to the default exclude list (See also :issue:`1442`,
  :pull:`1443`).
- Don't consider a config file which does not contain flake8 settings (See
  also :issue:`199`, :pull:`1472`).
- Duplicate ``local-plugins`` names are now allowed (See also :issue:`362`,
  :pull:`1504`).
- Consider ``.`` to be a path in config files (See also :issue:`1494`,
  :pull:`1508`)
- Add ``--require-plugins`` option taking distribution names (See also
  :issue:`283`, :pull:`1535`).
- Improve performance by removing debug logs (See also :pull:`1537`,
  :pull:`1544`).
- Include failing file path in plugin execution error (See also :issue:`265`,
  :pull:`1543`).
- Improve performance by pre-generating a ``pycodestyle`` plugin (See also
  :pull:`1545`).
- Properly differentiate between explicitly ignored / selected and default
  ignored / selected options (See also :issue:`284`, :pull:`1576`,
  :pull:`1609`).


Bugs Fixed
~~~~~~~~~~

- Fix physical line plugins not receiving all lines in the case of
  triple-quoted strings (See also :issue:`1534`, :pull:`1536`).
- Fix duplicate error logging in the case of plugin issues (See also
  :pull:`1538`).
- Fix inconsistent ordering of ``--ignore`` in ``--help`` (See also
  :issue:`1550`, :pull:`1552`).
- Fix memory leak of style guides by avoiding ``@lru_cache`` of a method (See
  also :pull:`1573`).
- Fix ignoring of configuration files exactly in the home directory (See also
  :issue:`1617`, :pull:`1618`).

.. all links
.. _5.0.0 milestone:
    https://github.com/PyCQA/flake8/milestone/42
```

## File: `docs/source/release-notes/5.0.1.rst`
```
5.0.1 -- 2022-07-31
-------------------

You can view the `5.0.1 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix duplicate plugin discovery on misconfigured pythons (See also
  :issue:`1627`, :pull:`1631`).


.. all links
.. _5.0.1 milestone:
    https://github.com/PyCQA/flake8/milestone/43
```

## File: `docs/source/release-notes/5.0.2.rst`
```
5.0.2 -- 2022-08-01
-------------------

You can view the `5.0.2 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Fix execution on python == 3.8.0 (See also :issue:`1637`, :pull:`1641`).
- Fix config discovery when home does not exist (See also :issue:`1640`,
  :pull:`1642`).


.. all links
.. _5.0.2 milestone:
    https://github.com/PyCQA/flake8/milestone/44
```

## File: `docs/source/release-notes/5.0.3.rst`
```
5.0.3 -- 2022-08-01
-------------------

You can view the `5.0.3 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Work around partial reads of configuration files with syntax errors (See
  also :issue:`1647`, :pull:`1648`).


.. all links
.. _5.0.3 milestone:
    https://github.com/PyCQA/flake8/milestone/45
```

## File: `docs/source/release-notes/5.0.4.rst`
```
5.0.4 -- 2022-08-03
-------------------

You can view the `5.0.4 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Set a lower bound on ``importlib-metadata`` to prevent ``RecursionError``
  (See also :issue:`1650`, :pull:`1653`).


.. all links
.. _5.0.4 milestone:
    https://github.com/PyCQA/flake8/milestone/46
```

## File: `docs/source/release-notes/6.0.0.rst`
```
6.0.0 -- 2022-11-23
-------------------

You can view the `6.0.0 milestone`_ on GitHub for more details.

Backwards Incompatible Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove ``--diff`` option (See also :issue:`1389`, :pull:`1720`).
- Produce an error when invalid codes are specified in configuration (See also
  :issue:`1689`, :pull:`1713`).
- Produce an error if the file specified in ``--extend-config`` does not exist
  (See also :issue:`1729`, :pull:`1732`).
- Remove ``optparse`` compatibility support (See also :pull:`1739`).

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycodestyle has been updated to >= 2.10.0, < 2.11.0 (See also :pull:`1746`).
- Pyflakes has been updated to >= 3.0.0, < 3.1.0 (See also :pull:`1748`).

Features
~~~~~~~~

- Require python >= 3.8.1 (See also :pull:`1633`, :pull:`1741`).
- List available formatters in for ``--format`` option in ``--help`` (See also
  :issue:`223`, :pull:`1624`).
- Improve multiprocessing performance (See also :pull:`1723`).
- Enable multiprocessing on non-fork platforms (See also :pull:`1723`).
- Ensure results are sorted when discovered from files (See also :issue:`1670`,
  :pull:`1726`).

.. all links
.. _6.0.0 milestone:
    https://github.com/PyCQA/flake8/milestone/47
```

## File: `docs/source/release-notes/6.1.0.rst`
```
6.1.0 -- 2023-07-29
-------------------

You can view the `6.1.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Pyflakes has been updated to >= 3.1.0, < 3.2.0 (See also :pull:`1847`).
- pycodestyle has been updated to >= 2.11.0, < 2.12.0 (See also :pull:`1848`).

Features
~~~~~~~~

- Deprecate ``--include-in-doctest``, ``--exclude-from-doctest`` (See also
  :issue:`1747`, :pull:`1768`).
- Add support for python 3.12 (See also :pull:`1832`, :pull:`1849`,
  :pull:`1850`).

.. all links
.. _6.1.0 milestone:
    https://github.com/PyCQA/flake8/milestone/48
```

## File: `docs/source/release-notes/7.0.0.rst`
```
7.0.0 -- 2024-01-04
-------------------

You can view the `7.0.0 milestone`_ on GitHub for more details.

Backwards Incompatible Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove ``--include-in-doctest`` and ``--exclude-from-doctest`` options.
  (See also :issue:`1747`, :pull:`1854`)

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Pyflakes has been updated to >= 3.2.0, < 3.3.0 (See also :pull:`1906`).

.. all links
.. _7.0.0 milestone:
    https://github.com/PyCQA/flake8/milestone/49
```

## File: `docs/source/release-notes/7.1.0.rst`
```
7.1.0 -- 2024-06-15
-------------------

You can view the `7.1.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycodestyle has been updated to >= 2.12.0, < 2.13.0 (See also :pull:`1939`).

.. all links
.. _7.1.0 milestone:
    https://github.com/PyCQA/flake8/milestone/50
```

## File: `docs/source/release-notes/7.1.1.rst`
```
7.1.1 -- 2024-08-04
-------------------

You can view the `7.1.1 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Properly preserve escaped `{` and `}` in fstrings in logical lines in 3.12+.
  (See also :issue:`1948`, :pull:`1949`).


.. all links
.. _7.1.1 milestone:
    https://github.com/PyCQA/flake8/milestone/51
```

## File: `docs/source/release-notes/7.1.2.rst`
```
7.1.2 -- 2025-02-16
-------------------

You can view the `7.1.2 milestone`_ on GitHub for more details.

Bugs Fixed
~~~~~~~~~~

- Avoid starting unnecessary processes when "# files" < "jobs".
  (See also :pull:`1966`).


.. all links
.. _7.1.2 milestone:
    https://github.com/PyCQA/flake8/milestone/52
```

## File: `docs/source/release-notes/7.2.0.rst`
```
7.2.0 -- 2025-03-29
-------------------

You can view the `7.2.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- pycodestyle has been updated to >= 2.13.0, < 2.14.0 (See also :pull:`1974`).
- pyflakes has been updated to >= 3.3.0, < 3.4.0 (See also :pull:`1974`).

Features
~~~~~~~~

- Require python >= 3.9 (See also :pull:`1973`).

.. all links
.. _7.2.0 milestone:
    https://github.com/PyCQA/flake8/milestone/53
```

## File: `docs/source/release-notes/7.3.0.rst`
```
7.3.0 -- 2025-06-20
-------------------

You can view the `7.3.0 milestone`_ on GitHub for more details.

New Dependency Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added support for python 3.14 (See also :pull:`1983`).
- pycodestyle has been updated to >= 2.14.0, < 2.15.0 (See also :pull:`1985`).
- Pyflakes has been updated to >= 3.4.0, < 3.5.0 (See also :pull:`1985`).

.. all links
.. _7.3.0 milestone:
    https://github.com/PyCQA/flake8/milestone/54
```

## File: `docs/source/release-notes/index.rst`
```
===========================
 Release Notes and History
===========================

All of the release notes that have been recorded for Flake8 are organized here
with the newest releases first.

7.x Release Series
==================

.. toctree::
   7.3.0
   7.2.0
   7.1.2
   7.1.1
   7.1.0
   7.0.0

6.x Release Series
==================

.. toctree::
   6.1.0
   6.0.0

5.x Release Series
==================

.. toctree::
   5.0.4
   5.0.3
   5.0.2
   5.0.1
   5.0.0

4.x Release Series
==================

.. toctree::
   4.0.1
   4.0.0

3.x Release Series
==================

.. toctree::
    3.9.2
    3.9.1
    3.9.0
    3.8.4
    3.8.3
    3.8.2
    3.8.1
    3.8.0
    3.7.9
    3.7.8
    3.7.7
    3.7.6
    3.7.5
    3.7.4
    3.7.3
    3.7.2
    3.7.1
    3.7.0
    3.6.0
    3.5.0
    3.4.1
    3.4.0
    3.3.0
    3.2.1
    3.2.0
    3.1.1
    3.1.0
    3.0.4
    3.0.3
    3.0.2
    3.0.1
    3.0.0

2.x Release Series
==================

.. toctree::
    2.6.2
    2.6.1
    2.6.0
    2.5.5
    2.5.4
    2.5.3
    2.5.2
    2.5.1
    2.5.0
    2.4.1
    2.4.0
    2.3.0
    2.2.5
    2.2.4
    2.2.3
    2.2.2
    2.2.1
    2.2.0
    2.1.0
    2.0.0

1.x Release Series
==================

.. toctree::
    1.7.0
    1.6.2
    1.6.1
    1.6.0
    1.5.0
    1.4.0
    1.3.1
    1.3.0
    1.2.0
    1.1.0
    1.0.0

0.x Release Series
==================

.. toctree::
    0.9.0
    0.8.0
    0.7.0
    0.6.0
```

## File: `docs/source/user/configuration.rst`
```
.. _configuration:

====================
 Configuring Flake8
====================

Once you have learned how to :ref:`invoke <invocation>` |Flake8|, you will soon
want to learn how to configure it so you do not have to specify the same
options every time you use it.

This section will show you how to make

.. prompt:: bash

    flake8

Remember that you want to specify certain options without writing

.. prompt:: bash

    flake8 --select E123,W456 --enable-extensions H111


Configuration Locations
=======================

|Flake8| supports storing its configuration in your project in one of
``setup.cfg``, ``tox.ini``, or ``.flake8``.

Values set at the command line have highest priority, then those in the
project configuration file, and finally there are the defaults. However,
there are additional command line options which can alter this.


Project Configuration
---------------------

|Flake8| is written with the understanding that people organize projects into
sub-directories. Let's take for example |Flake8|'s own project structure

.. code::

    flake8
    ├── docs
    │   ├── build
    │   └── source
    │       ├── _static
    │       ├── _templates
    │       ├── dev
    │       ├── internal
    │       └── user
    ├── flake8
    │   ├── formatting
    │   ├── main
    │   ├── options
    │   └── plugins
    └── tests
        ├── fixtures
        │   └── config_files
        ├── integration
        └── unit

In the top-level ``flake8`` directory (which contains ``docs``, ``flake8``,
and ``tests``) there's also ``tox.ini`` and ``setup.cfg`` files. In our case,
we keep our |Flake8| configuration in ``tox.ini``. Regardless of whether you
keep your config in ``.flake8``, ``setup.cfg``, or ``tox.ini`` we expect you
to use INI to configure |Flake8| (since each of these files already uses INI
as a format). This means that any |Flake8| configuration you wish to set needs
to be in the ``flake8`` section, which means it needs to start like so:

.. code-block:: ini

    [flake8]

Each command-line option that you want to specify in your config file can
be named in either of two ways:

#. Using underscores (``_``) instead of hyphens (``-``)

#. Simply using hyphens (without the leading hyphens)

.. note::

    Not every |Flake8| command-line option can be specified in the
    configuration file. See :ref:`our list of options <options-list>` to
    determine which options will be parsed from the configuration files.

Let's actually look at |Flake8|'s own configuration section:

.. code-block:: ini

    [flake8]
    extend-ignore = E203
    exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
    max-complexity = 10

This is equivalent to:

.. prompt:: bash

    flake8 --extend-ignore E203 \
             --exclude .git,__pycache__,docs/source/conf.py,old,build,dist \
             --max-complexity 10

In our case, if we wanted to, we could also do

.. code-block:: ini

    [flake8]
    extend-ignore = E203
    exclude =
        .git,
        __pycache__,
        docs/source/conf.py,
        old,
        build,
        dist
    max-complexity = 10

This allows us to add comments for why we're excluding items, e.g.

.. code-block:: ini

    [flake8]
    extend-ignore = E203
    exclude =
        # No need to traverse our git directory
        .git,
        # There's no value in checking cache directories
        __pycache__,
        # The conf file is mostly autogenerated, ignore it
        docs/source/conf.py,
        # The old directory contains Flake8 2.0
        old,
        # This contains our built documentation
        build,
        # This contains builds of flake8 that we don't want to check
        dist
    max-complexity = 10

.. note::

    Following the recommended settings for
    `Python's configparser <https://docs.python.org/3/library/configparser.html#customizing-parser-behaviour>`_,
    |Flake8| does not support inline comments for any of the keys. So while
    this is fine:

    .. code-block:: ini

        [flake8]
        per-file-ignores =
            # imported but unused
            __init__.py: F401

    this is not:

    .. code-block:: ini

        [flake8]
        per-file-ignores =
            __init__.py: F401 # imported but unused


.. note::

    If you're using Python 2, you will notice that we download the
    :mod:`configparser` backport from PyPI. That backport enables us to
    support this behaviour on all supported versions of Python.

    Please do **not** open issues about this dependency to |Flake8|.

.. note::

    You can also specify ``--max-complexity`` as ``max_complexity = 10``.

This is also useful if you have a long list of error codes to ignore. Let's
look at a portion of a project's Flake8 configuration in their ``tox.ini``:

.. code-block:: ini

    [flake8]
    # it's not a bug that we aren't using all of hacking, ignore:
    # H101: Use TODO(NAME)
    # H202: assertRaises Exception too broad
    # H233: Python 3.x incompatible use of print operator
    # H301: one import per line
    # H306: imports not in alphabetical order (time, os)
    # H401: docstring should not start with a space
    # H403: multi line docstrings should end on a new line
    # H404: multi line docstring should start without a leading new line
    # H405: multi line docstring summary not separated with an empty line
    # H501: Do not use self.__dict__ for string formatting
    extend-ignore = H101,H202,H233,H301,H306,H401,H403,H404,H405,H501

They use the comments to describe the check but they could also write this as:

.. code-block:: ini

    [flake8]
    # it's not a bug that we aren't using all of hacking
    extend-ignore =
        # H101: Use TODO(NAME)
        H101,
        # H202: assertRaises Exception too broad
        H202,
        # H233: Python 3.x incompatible use of print operator
        H233,
        # H301: one import per line
        H301,
        # H306: imports not in alphabetical order (time, os)
        H306,
        # H401: docstring should not start with a space
        H401,
        # H403: multi line docstrings should end on a new line
        H403,
        # H404: multi line docstring should start without a leading new line
        H404,
        # H405: multi line docstring summary not separated with an empty line
        H405,
        # H501: Do not use self.__dict__ for string formatting
        H501

Or they could use each comment to describe **why** they've ignored the check.
|Flake8| knows how to parse these lists and will appropriately handle
these situations.


Using Local Plugins
-------------------

.. versionadded:: 3.5.0

|Flake8| allows users to write plugins that live locally in a project. These
plugins do not need to use setuptools or any of the other overhead associated
with plugins distributed on PyPI. To use these plugins, users must specify
them in their configuration file (i.e., ``.flake8``, ``setup.cfg``, or
``tox.ini``). This must be configured in a separate INI section named
``flake8:local-plugins``.

Users may configure plugins that check source code, i.e., ``extension``
plugins, and plugins that report errors, i.e., ``report`` plugins.

An example configuration might look like:

.. code-block:: ini

    [flake8:local-plugins]
    extension =
        MC1 = project.flake8.checkers:MyChecker1
        MC2 = project.flake8.checkers:MyChecker2
    report =
        MR1 = project.flake8.reporters:MyReporter1
        MR2 = project.flake8.reporters:MyReporter2

|Flake8| will also, however, allow for commas to separate the plugins for
example:

.. code-block:: ini

    [flake8:local-plugins]
    extension =
        MC1 = project.flake8.checkers:MyChecker1,
        MC2 = project.flake8.checkers:MyChecker2
    report =
        MR1 = project.flake8.reporters:MyReporter1,
        MR2 = project.flake8.reporters:MyReporter2

These configurations will allow you to select your own custom reporter plugin
that you've designed or will utilize your new check classes.

If your package is installed in the same virtualenv that |Flake8| will run
from, and your local plugins are part of that package, you're all set; |Flake8|
will be able to import your local plugins. However, if you are working on a
project that isn't set up as an installable package, or |Flake8| doesn't run
from the same virtualenv your code runs in, you may need to tell |Flake8| where
to import your local plugins from. You can do this via the ``paths`` option in
the ``local-plugins`` section of your config:

.. code-block:: ini

    [flake8:local-plugins]
    extension =
      MC1 = myflake8plugin:MyChecker1
    paths =
      ./path/to

Relative paths will be interpreted relative to the config file. Multiple paths
can be listed (comma separated just like ``exclude``) as needed. If your local
plugins have any dependencies, it's up to you to ensure they are installed in
whatever Python environment |Flake8| runs in.

.. note::

    These plugins otherwise follow the same guidelines as regular plugins.
```

## File: `docs/source/user/error-codes.rst`
```
.. _error_codes:

=========================
 Error / Violation Codes
=========================

Flake8 and its plugins assign a code to each message that we refer to as an
:term:`error code` (or :term:`violation`). Most plugins will list their error
codes in their documentation or README.

Flake8 installs ``pycodestyle``, ``pyflakes``, and ``mccabe`` by default and
generates its own :term:`error code`\ s for ``pyflakes``:

+------+---------------------------------------------------------------------+
| Code | Example Message                                                     |
+======+=====================================================================+
| F401 | ``module`` imported but unused                                      |
+------+---------------------------------------------------------------------+
| F402 | import ``module`` from line ``N`` shadowed by loop variable         |
+------+---------------------------------------------------------------------+
| F403 | 'from ``module`` import \*' used; unable to detect undefined names  |
+------+---------------------------------------------------------------------+
| F404 | future import(s) ``name`` after other statements                    |
+------+---------------------------------------------------------------------+
| F405 | ``name`` may be undefined, or defined from star imports: ``module`` |
+------+---------------------------------------------------------------------+
| F406 | 'from ``module`` import \*' only allowed at module level            |
+------+---------------------------------------------------------------------+
| F407 | an undefined ``__future__`` feature name was imported               |
+------+---------------------------------------------------------------------+
+------+---------------------------------------------------------------------+
| F501 | invalid ``%`` format literal                                        |
+------+---------------------------------------------------------------------+
| F502 | ``%`` format expected mapping but got sequence                      |
+------+---------------------------------------------------------------------+
| F503 | ``%`` format expected sequence but got mapping                      |
+------+---------------------------------------------------------------------+
| F504 | ``%`` format unused named arguments                                 |
+------+---------------------------------------------------------------------+
| F505 | ``%`` format missing named arguments                                |
+------+---------------------------------------------------------------------+
| F506 | ``%`` format mixed positional and named arguments                   |
+------+---------------------------------------------------------------------+
| F507 | ``%`` format mismatch of placeholder and argument count             |
+------+---------------------------------------------------------------------+
| F508 | ``%`` format with ``*`` specifier requires a sequence               |
+------+---------------------------------------------------------------------+
| F509 | ``%`` format with unsupported format character                      |
+------+---------------------------------------------------------------------+
| F521 | ``.format(...)`` invalid format string                              |
+------+---------------------------------------------------------------------+
| F522 | ``.format(...)`` unused named arguments                             |
+------+---------------------------------------------------------------------+
| F523 | ``.format(...)`` unused positional arguments                        |
+------+---------------------------------------------------------------------+
| F524 | ``.format(...)`` missing argument                                   |
+------+---------------------------------------------------------------------+
| F525 | ``.format(...)`` mixing automatic and manual numbering              |
+------+---------------------------------------------------------------------+
| F541 | f-string without any placeholders                                   |
+------+---------------------------------------------------------------------+
| F542 | t-string without any placeholders                                   |
+------+---------------------------------------------------------------------+
+------+---------------------------------------------------------------------+
| F601 | dictionary key ``name`` repeated with different values              |
+------+---------------------------------------------------------------------+
| F602 | dictionary key variable ``name`` repeated with different values     |
+------+---------------------------------------------------------------------+
| F621 | too many expressions in an assignment with star-unpacking           |
+------+---------------------------------------------------------------------+
| F622 | two or more starred expressions in an assignment ``(a, *b, *c = d)``|
+------+---------------------------------------------------------------------+
| F631 | assertion test is a tuple, which is always ``True``                 |
+------+---------------------------------------------------------------------+
| F632 | use ``==/!=`` to compare ``str``, ``bytes``, and ``int`` literals   |
+------+---------------------------------------------------------------------+
| F633 | use of ``>>`` is invalid with ``print`` function                    |
+------+---------------------------------------------------------------------+
| F634 | if test is a tuple, which is always ``True``                        |
+------+---------------------------------------------------------------------+
+------+---------------------------------------------------------------------+
| F701 | a ``break`` statement outside of a ``while`` or ``for`` loop        |
+------+---------------------------------------------------------------------+
| F702 | a ``continue`` statement outside of a ``while`` or ``for`` loop     |
+------+---------------------------------------------------------------------+
| F704 | a ``yield`` or ``yield from`` statement outside of a function       |
+------+---------------------------------------------------------------------+
| F706 | a ``return`` statement outside of a function/method                 |
+------+---------------------------------------------------------------------+
| F707 | an ``except:`` block as not the last exception handler              |
+------+---------------------------------------------------------------------+
| F721 | syntax error in doctest                                             |
+------+---------------------------------------------------------------------+
| F722 | syntax error in forward annotation                                  |
+------+---------------------------------------------------------------------+
| F723 | syntax error in type comment                                        |
+------+---------------------------------------------------------------------+
+------+---------------------------------------------------------------------+
| F811 | redefinition of unused ``name`` from line ``N``                     |
+------+---------------------------------------------------------------------+
| F821 | undefined name ``name``                                             |
+------+---------------------------------------------------------------------+
| F822 | undefined name ``name`` in ``__all__``                              |
+------+---------------------------------------------------------------------+
| F823 | local variable ``name`` ... referenced before assignment            |
+------+---------------------------------------------------------------------+
| F824 | ``global name`` / ``nonlocal name`` is unused: name is never        |
|      | assigned in scope                                                   |
+------+---------------------------------------------------------------------+
| F831 | duplicate argument ``name`` in function definition                  |
+------+---------------------------------------------------------------------+
| F841 | local variable ``name`` is assigned to but never used               |
+------+---------------------------------------------------------------------+
+------+---------------------------------------------------------------------+
| F901 | ``raise NotImplemented`` should be ``raise NotImplementedError``    |
+------+---------------------------------------------------------------------+

We also report one extra error: ``E999``. We report ``E999`` when we fail to
compile a file into an Abstract Syntax Tree for the plugins that require it.

``mccabe`` only ever reports one :term:`violation` - ``C901`` based on the
complexity value provided by the user.

Users should also reference `pycodestyle's list of error codes`_.


.. links
.. _pycodestyle's list of error codes:
    https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes
```

## File: `docs/source/user/index.rst`
```
==============
 Using Flake8
==============

|Flake8| can be used in many ways. A few:

- invoked on the command-line

- invoked via Python

This guide will cover all of these and the nuances for using |Flake8|.

.. note::

    This portion of |Flake8|'s documentation does not cover installation. See
    the :ref:`installation-guide` section for how to install |Flake8|.

.. toctree::
    :maxdepth: 2

    invocation
    configuration
    options
    error-codes
    violations
    using-plugins
    using-hooks
    python-api

.. config files
.. command-line tutorial
.. VCS usage
.. installing and using plugins
```

## File: `docs/source/user/invocation.rst`
```
.. _invocation:

=================
 Invoking Flake8
=================

Once you have :ref:`installed <installation-guide>` |Flake8|, you can begin
using it. Most of the time, you will be able to generically invoke |Flake8|
like so:

.. prompt:: bash

    flake8 ...

Where you simply allow the shell running in your terminal to locate |Flake8|.
In some cases, though, you may have installed |Flake8| for multiple versions
of Python (e.g., Python 3.13 and Python 3.14) and you need to call a specific
version. In that case, you will have much better results using:

.. prompt:: bash

    python3.13 -m flake8

Or

.. prompt:: bash

    python3.14 -m flake8

Since that will tell the correct version of Python to run |Flake8|.

.. note::

    Installing |Flake8| once will not install it on both Python 3.13 and
    Python 3.14. It will only install it for the version of Python that
    is running pip.

It is also possible to specify command-line options directly to |Flake8|:

.. prompt:: bash

    flake8 --select E123

Or

.. prompt:: bash

    python<version> -m flake8 --select E123

.. note::

    This is the last time we will show both versions of an invocation.
    From now on, we'll simply use ``flake8`` and assume that the user
    knows they can instead use ``python<version> -m flake8``.

It's also possible to narrow what |Flake8| will try to check by specifying
exactly the paths and directories you want it to check. Let's assume that
we have a directory with python files and sub-directories which have python
files (and may have more sub-directories) called ``my_project``. Then if
we only want errors from files found inside ``my_project`` we can do:

.. prompt:: bash

    flake8 my_project

And if we only want certain errors (e.g., ``E123``) from files in that
directory we can also do:

.. prompt:: bash

    flake8 --select E123 my_project

If you want to explore more options that can be passed on the command-line,
you can use the ``--help`` option:

.. prompt:: bash

    flake8 --help

And you should see something like:

.. code::

    Usage: flake8 [options] file file ...

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit

      ...
```

## File: `docs/source/user/options.rst`
```
.. _options-list:

================================================
 Full Listing of Options and Their Descriptions
================================================

..
    NOTE(sigmavirus24): When adding new options here, please follow the
    following _rough_ template:

    .. option:: --<opt-name>[=<descriptive-name-of-parameter>]

        :ref:`Go back to index <top>`

        Active description of option's purpose (note that each description
        starts with an active verb)

        Command-line usage:

        .. prompt:: bash

            flake8 --<opt-name>[=<example-parameter(s)>] [positional params]

        This **can[ not]** be specified in config files.

        (If it can be, an example using .. code-block:: ini)

    Thank you for your contribution to Flake8's documentation.

.. _top:

Index of Options
================

- :option:`flake8 --version`

- :option:`flake8 --help`

- :option:`flake8 --verbose`

- :option:`flake8 --quiet`

- :option:`flake8 --color`

- :option:`flake8 --count`

- :option:`flake8 --exclude`

- :option:`flake8 --extend-exclude`

- :option:`flake8 --filename`

- :option:`flake8 --stdin-display-name`

- :option:`flake8 --format`

- :option:`flake8 --hang-closing`

- :option:`flake8 --ignore`

- :option:`flake8 --extend-ignore`

- :option:`flake8 --per-file-ignores`

- :option:`flake8 --max-line-length`

- :option:`flake8 --max-doc-length`

- :option:`flake8 --indent-size`

- :option:`flake8 --select`

- :option:`flake8 --extend-select`

- :option:`flake8 --disable-noqa`

- :option:`flake8 --show-source`

- :option:`flake8 --statistics`

- :option:`flake8 --require-plugins`

- :option:`flake8 --enable-extensions`

- :option:`flake8 --exit-zero`

- :option:`flake8 --jobs`

- :option:`flake8 --output-file`

- :option:`flake8 --tee`

- :option:`flake8 --append-config`

- :option:`flake8 --config`

- :option:`flake8 --isolated`

- :option:`flake8 --builtins`

- :option:`flake8 --doctests`

- :option:`flake8 --benchmark`

- :option:`flake8 --bug-report`

- :option:`flake8 --max-complexity`


Options and their Descriptions
==============================

.. program:: flake8

.. option:: --version

    :ref:`Go back to index <top>`

    Show |Flake8|'s version as well as the versions of all plugins
    installed.

    Command-line usage:

    .. prompt:: bash

        flake8 --version

    This **can not** be specified in config files.


.. option:: -h, --help

    :ref:`Go back to index <top>`

    Show a description of how to use |Flake8| and its options.

    Command-line usage:

    .. prompt:: bash

        flake8 --help
        flake8 -h

    This **can not** be specified in config files.


.. option::  -v, --verbose

    :ref:`Go back to index <top>`

    Increase the verbosity of |Flake8|'s output. Each time you specify
    it, it will print more and more information.

    Command-line example:

    .. prompt:: bash

        flake8 -vv

    This **can not** be specified in config files.


.. option:: -q, --quiet

    :ref:`Go back to index <top>`

    Decrease the verbosity of |Flake8|'s output. Each time you specify it,
    it will print less and less information.

    Command-line example:

    .. prompt:: bash

        flake8 -q

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        quiet = 1

.. option:: --color

    :ref:`Go back to index <top>`

    Whether to use color in output. Defaults to ``auto``.

    Possible options are ``auto``, ``always``, and ``never``.

    This **can not** be specified in config files.

    When color is enabled, the following substitutions are enabled:

    - ``%(bold)s``
    - ``%(black)s``
    - ``%(red)s``
    - ``%(green)s``
    - ``%(yellow)s``
    - ``%(blue)s``
    - ``%(magenta)s``
    - ``%(cyan)s``
    - ``%(white)s``
    - ``%(reset)s``


.. option:: --count

    :ref:`Go back to index <top>`

    Print the total number of errors.

    Command-line example:

    .. prompt:: bash

        flake8 --count dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        count = True


.. option:: --exclude=<patterns>

    :ref:`Go back to index <top>`

    Provide a comma-separated list of glob patterns to exclude from checks.

    This defaults to: ``.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg``

    Example patterns:

    - ``*.pyc`` will match any file that ends with ``.pyc``

    - ``__pycache__`` will match any path that has ``__pycache__`` in it

    - ``lib/python`` will look expand that using :func:`os.path.abspath` and
      look for matching paths

    Command-line example:

    .. prompt:: bash

        flake8 --exclude=*.pyc dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        exclude =
            .tox,
            __pycache__


.. option:: --extend-exclude=<patterns>

    :ref:`Go back to index <top>`

    .. versionadded:: 3.8.0

    Provide a comma-separated list of glob patterns to add to the list of excluded ones.
    Similar considerations as in :option:`--exclude` apply here with regard to the
    value.

    The difference to the :option:`--exclude` option is, that this option can be
    used to selectively add individual patterns without overriding the default
    list entirely.

    Command-line example:

    .. prompt:: bash

        flake8 --extend-exclude=legacy/,vendor/ dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        extend-exclude =
            legacy/,
            vendor/
        extend-exclude = legacy/,vendor/


.. option:: --filename=<patterns>

    :ref:`Go back to index <top>`

    Provide a comma-separate list of glob patterns to include for checks.

    This defaults to: ``*.py``

    Example patterns:

    - ``*.py`` will match any file that ends with ``.py``

    - ``__pycache__`` will match any path that has ``__pycache__`` in it

    - ``lib/python`` will look expand that using :func:`os.path.abspath` and
      look for matching paths

    Command-line example:

    .. prompt:: bash

        flake8 --filename=*.py dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        filename =
            example.py,
            another-example*.py


.. option:: --stdin-display-name=<display_name>

    :ref:`Go back to index <top>`

    Provide the name to use to report warnings and errors from code on stdin.

    Instead of reporting an error as something like:

    .. code::

        stdin:82:73 E501 line too long

    You can specify this option to have it report whatever value you want
    instead of stdin.

    This defaults to: ``stdin``

    Command-line example:

    .. prompt:: bash

        cat file.py | flake8 --stdin-display-name=file.py -

    This **can not** be specified in config files.


.. option:: --format=<format>

    :ref:`Go back to index <top>`

    Select the formatter used to display errors to the user.

    This defaults to: ``default``

    By default, there are two formatters available:

    - default
    - pylint

    Other formatters can be installed. Refer to their documentation for the
    name to use to select them. Further, users can specify their own format
    string. The variables available are:

    - code
    - col
    - path
    - row
    - text

    The default formatter has a format string of:

    .. code-block:: python

        '%(path)s:%(row)d:%(col)d: %(code)s %(text)s'

    Command-line example:

    .. prompt:: bash

        flake8 --format=pylint dir/
        flake8 --format='%(path)s::%(row)d,%(col)d::%(code)s::%(text)s' dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        format=pylint
        format=%(path)s::%(row)d,%(col)d::%(code)s::%(text)s


.. option:: --hang-closing

    :ref:`Go back to index <top>`

    Toggle whether pycodestyle should enforce matching the indentation of the
    opening bracket's line. When you specify this, it will prefer that you
    hang the closing bracket rather than match the indentation.

    Command-line example:

    .. prompt:: bash

        flake8 --hang-closing dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        hang_closing = True
        hang-closing = True


.. option:: --ignore=<errors>

    :ref:`Go back to index <top>`

    Specify a list of codes to ignore. The list is expected to be
    comma-separated, and does not need to specify an error code exactly.
    Since |Flake8| 3.0, this **can** be combined with :option:`--select`. See
    :option:`--select` for more information.

    For example, if you wish to only ignore ``W234``, then you can specify
    that. But if you want to ignore all codes that start with ``W23`` you
    need only specify ``W23`` to ignore them. This also works for ``W2`` and
    ``W`` (for example).

    This defaults to: ``E121,E123,E126,E226,E24,E704,W503,W504``

    Command-line example:

    .. prompt:: bash

        flake8 --ignore=E121,E123 dir/
        flake8 --ignore=E24,E704 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        ignore =
            E121,
            E123
        ignore = E121,E123


.. option:: --extend-ignore=<errors>

    :ref:`Go back to index <top>`

    .. versionadded:: 3.6.0

    Specify a list of codes to add to the list of ignored ones. Similar
    considerations as in :option:`--ignore` apply here with regard to the
    value.

    The difference to the :option:`--ignore` option is, that this option can be
    used to selectively add individual codes without overriding the default
    list entirely.

    Command-line example:

    .. prompt:: bash

        flake8 --extend-ignore=E4,E51,W234 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        extend-ignore =
            E4,
            E51,
            W234
        extend-ignore = E4,E51,W234


.. option:: --per-file-ignores=<filename:errors>[ <filename:errors>]

    :ref:`Go back to index <top>`

    .. versionadded:: 3.7.0

    Specify a list of mappings of files and the codes that should be ignored
    for the entirety of the file. This allows for a project to have a default
    list of violations that should be ignored as well as file-specific
    violations for files that have not been made compliant with the project
    rules.

    This option supports syntax similar to :option:`--exclude` such that glob
    patterns will also work here.

    This can be combined with both :option:`--ignore` and
    :option:`--extend-ignore` to achieve a full flexibility of style options.

    Command-line usage:

    .. prompt:: bash

        flake8 --per-file-ignores='project/__init__.py:F401 setup.py:E121'
        flake8 --per-file-ignores='project/*/__init__.py:F401 setup.py:E121'

    This **can** be specified in config files.

    .. code-block:: ini

        per-file-ignores =
            project/__init__.py:F401
            setup.py:E121
            other_project/*:W9

.. option:: --max-line-length=<n>

    :ref:`Go back to index <top>`

    Set the maximum length that any line (with some exceptions) may be.

    Exceptions include lines that are either strings or comments which are
    entirely URLs. For example:

    .. code-block:: python

        # https://some-super-long-domain-name.com/with/some/very/long/path

        url = '''\
            https://...
        '''

    This defaults to: ``79``

    Command-line example:

    .. prompt:: bash

        flake8 --max-line-length 99 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        max-line-length = 79

.. option:: --max-doc-length=<n>

    :ref:`Go back to index <top>`

    Set the maximum length that a comment or docstring line may be.

    By default, there is no limit on documentation line length.

    Command-line example:

    .. prompt:: bash

        flake8 --max-doc-length 99 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        max-doc-length = 79

.. option:: --indent-size=<n>

    :ref:`Go back to index <top>`

    Set the number of spaces used for indentation.

    By default, 4.

    Command-line example:

    .. prompt:: bash

        flake8 --indent-size 2 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        indent-size = 2

.. option:: --select=<errors>

    :ref:`Go back to index <top>`

    **You usually do not need to specify this option as the default includes
    all installed plugin codes.**

    Specify the list of error codes you wish |Flake8| to report. Similarly to
    :option:`--ignore`. You can specify a portion of an error code to get all
    that start with that string. For example, you can use ``E``, ``E4``,
    ``E43``, and ``E431``.

    Command-line example:

    .. prompt:: bash

        flake8 --select=E431,E5,W,F dir/
        flake8 --select=E,W dir/

    This can also be combined with :option:`--ignore`:

    .. prompt:: bash

        flake8 --select=E --ignore=E432 dir/

    This will report all codes that start with ``E``, but ignore ``E432``
    specifically. This is more flexibly than the |Flake8| 2.x and 1.x used
    to be.

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        select =
            E431,
            W,
            F


.. option:: --extend-select=<errors>

    :ref:`Go back to index <top>`

    .. versionadded:: 4.0.0

    **You usually do not need to specify this option as the default includes
    all installed plugin codes.**

    Specify a list of codes to add to the list of selected ones. Similar
    considerations as in :option:`--select` apply here with regard to the
    value.

    The difference to the :option:`--select` option is, that this option can be
    used to selectively add individual codes without overriding the default
    list entirely.

    Command-line example:

    .. prompt:: bash

        flake8 --extend-select=E4,E51,W234 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        extend-select =
            E4,
            E51,
            W234


.. option:: --disable-noqa

    :ref:`Go back to index <top>`

    Report all errors, even if it is on the same line as a ``# NOQA`` comment.
    ``# NOQA`` can be used to silence messages on specific lines. Sometimes,
    users will want to see what errors are being silenced without editing the
    file. This option allows you to see all the warnings, errors, etc.
    reported.

    Command-line example:

    .. prompt:: bash

        flake8 --disable-noqa dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        disable_noqa = True
        disable-noqa = True


.. option:: --show-source

    :ref:`Go back to index <top>`

    Print the source code generating the error/warning in question.

    Command-line example:

    .. prompt:: bash

        flake8 --show-source dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        show_source = True
        show-source = True


.. option:: --statistics

    :ref:`Go back to index <top>`

    Count the number of occurrences of each error/warning code and
    print a report.

    Command-line example:

    .. prompt:: bash

        flake8 --statistics

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        statistics = True


.. option:: --require-plugins=<names>

    :ref:`Go back to index <top>`

    Require specific plugins to be installed before running.

    This option takes a list of distribution names (usually the name you would
    use when running ``pip install``).

    Command-line example:

    .. prompt:: bash

        flake8 --require-plugins=flake8-2020,flake8-typing-extensions dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        require-plugins =
            flake8-2020
            flake8-typing-extensions


.. _option-enable-extensions:

.. option:: --enable-extensions=<errors>

    :ref:`Go back to index <top>`

    Enable :ref:`off-by-default<off-by-default>` extensions.

    Plugins to |Flake8| have the option of registering themselves as
    off-by-default. These plugins will not be loaded unless enabled by this
    option.

    Command-line example:

    .. prompt:: bash

        flake8 --enable-extensions=H111 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        enable-extensions =
            H111,
            G123
        enable_extensions =
            H111,
            G123


.. option:: --exit-zero

    :ref:`Go back to index <top>`

    Force |Flake8| to use the exit status code 0 even if there are errors.

    By default |Flake8| will exit with a non-zero integer if there are errors.

    Command-line example:

    .. prompt:: bash

        flake8 --exit-zero dir/

    This **can not** be specified in config files.


.. option:: --jobs=<n>

    :ref:`Go back to index <top>`

    Specify the number of subprocesses that |Flake8| will use to run checks in
    parallel.

    .. note::

        This option is ignored on platforms where ``fork`` is not a
        supported ``multiprocessing`` method.

    This defaults to: ``auto``

    The default behaviour will use the number of CPUs on your machine as
    reported by :func:`multiprocessing.cpu_count`.

    Command-line example:

    .. prompt:: bash

        flake8 --jobs=8 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        jobs = 8


.. option:: --output-file=<path>

    :ref:`Go back to index <top>`

    Redirect all output to the specified file.

    Command-line example:

    .. prompt:: bash

        flake8 --output-file=output.txt dir/
        flake8 -vv --output-file=output.txt dir/


.. option:: --tee

    :ref:`Go back to index <top>`

    Also print output to stdout if output-file has been configured.

    Command-line example:

    .. prompt:: bash

        flake8 --tee --output-file=output.txt dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        tee = True


.. option:: --append-config=<config>

    :ref:`Go back to index <top>`

    .. versionadded:: 3.6.0

    Provide extra config files to parse in after and in addition to the files
    that |Flake8| found on its own. Since these files are the last ones read
    into the Configuration Parser, so it has the highest precedence if it
    provides an option specified in another config file.

    Command-line example:

    .. prompt:: bash

        flake8 --append-config=my-extra-config.ini dir/

    This **can not** be specified in config files.


.. option:: --config=<config>

    :ref:`Go back to index <top>`

    Provide a path to a config file that will be the only config file read and
    used. This will cause |Flake8| to ignore all other config files that
    exist.

    Command-line example:

    .. prompt:: bash

        flake8 --config=my-only-config.ini dir/

    This **can not** be specified in config files.


.. option:: --isolated

    :ref:`Go back to index <top>`

    Ignore any config files and use |Flake8| as if there were no config files
    found.

    Command-line example:

    .. prompt:: bash

        flake8 --isolated dir/

    This **can not** be specified in config files.


.. option:: --builtins=<builtins>

    :ref:`Go back to index <top>`

    Provide a custom list of builtin functions, objects, names, etc.

    This allows you to let pyflakes know about builtins that it may
    not immediately recognize so it does not report warnings for using
    an undefined name.

    This is registered by the default PyFlakes plugin.

    Command-line example:

    .. prompt:: bash

        flake8 --builtins=_,_LE,_LW dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        builtins =
            _,
            _LE,
            _LW


.. option:: --doctests

    :ref:`Go back to index <top>`

    Enable PyFlakes syntax checking of doctests in docstrings.

    This is registered by the default PyFlakes plugin.

    Command-line example:

    .. prompt:: bash

        flake8 --doctests dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        doctests = True


.. option:: --benchmark

    :ref:`Go back to index <top>`

    Collect and print benchmarks for this run of |Flake8|. This aggregates the
    total number of:

    - tokens
    - physical lines
    - logical lines
    - files

    and the number of elapsed seconds.

    Command-line usage:

    .. prompt:: bash

        flake8 --benchmark dir/

    This **can not** be specified in config files.


.. option:: --bug-report

    :ref:`Go back to index <top>`

    Generate information necessary to file a complete bug report for Flake8.
    This will pretty-print a JSON blob that should be copied and pasted into a
    bug report for Flake8.

    Command-line usage:

    .. prompt:: bash

        flake8 --bug-report

    The output should look vaguely like:

    .. code-block:: js

        {
          "dependencies": [
            {
              "dependency": "setuptools",
              "version": "25.1.1"
            }
          ],
          "platform": {
            "python_implementation": "CPython",
            "python_version": "2.7.12",
            "system": "Darwin"
          },
          "plugins": [
            {
              "plugin": "mccabe",
              "version": "0.5.1"
            },
            {
              "plugin": "pycodestyle",
              "version": "2.0.0"
            },
            {
              "plugin": "pyflakes",
              "version": "1.2.3"
            }
          ],
          "version": "3.1.0.dev0"
        }

    This **can not** be specified in config files.


.. option:: --max-complexity=<n>

    :ref:`Go back to index <top>`

    Set the maximum allowed McCabe complexity value for a block of code.

    This option is provided by the ``mccabe`` dependency's |Flake8| plugin.

    Command-line usage:

    .. prompt:: bash

        flake8 --max-complexity 15 dir/

    This **can** be specified in config files.

    Example config file usage:

    .. code-block:: ini

        max-complexity = 15
```

## File: `docs/source/user/python-api.rst`
```
===================
 Public Python API
===================

|Flake8| 3.0.0 presently does not have a public, stable Python API.

When it does it will be located in :mod:`flake8.api` and that will
be documented here.


Legacy API
==========

When |Flake8| broke its hard dependency on the tricky internals of
pycodestyle, it lost the easy backwards compatibility as well. To help
existing users of that API we have :mod:`flake8.api.legacy`. This module
includes a couple classes (which are documented below) and a function.

The main usage that the developers of Flake8 observed was using the
:func:`~flake8.api.legacy.get_style_guide` function and then calling
:meth:`~flake8.api.legacy.StyleGuide.check_files`. To a lesser extent,
people also seemed to use the :meth:`~flake8.api.legacy.Report.get_statistics`
method on what ``check_files`` returns. We then sought to preserve that
API in this module.

Let's look at an example piece of code together:

.. code-block:: python

    from flake8.api import legacy as flake8


    style_guide = flake8.get_style_guide(ignore=['E24', 'W503'])
    report = style_guide.check_files([...])
    assert report.get_statistics('E') == [], 'Flake8 found violations'

This represents the basic universal usage of all existing Flake8 2.x
integrations. Each example we found was obviously slightly different,
but this is kind of the gist, so let's walk through this.

Everything that is backwards compatible for our API is in the
:mod:`flake8.api.legacy` submodule. This is to indicate, clearly, that
the old API is being used.

We create a |StyleGuide| by calling |style_guide|.  We can pass options
to |style_guide| that correspond to the command-line options one might use.
For example, we can pass ``ignore``, ``select``, ``exclude``, ``format``, etc.
Our legacy API, does not enforce legacy behaviour, so we can combine
``ignore`` and ``select`` like we might on the command-line, e.g.,

.. code-block:: python

    style_guide = flake8.get_style_guide(
        ignore=['E24', 'W5'],
        select=['E', 'W', 'F'],
        format='pylint',
    )

Once we have our |StyleGuide| we can use the same methods that we used before,
namely

.. automethod:: flake8.api.legacy.StyleGuide.check_files

.. automethod:: flake8.api.legacy.StyleGuide.excluded

.. automethod:: flake8.api.legacy.StyleGuide.init_report

.. automethod:: flake8.api.legacy.StyleGuide.input_file

.. warning::

    These are not *perfectly* backwards compatible. Not all arguments are
    respected, and some of the types necessary for something to work have
    changed.

Most people, we observed, were using
:meth:`~flake8.api.legacy.StyleGuide.check_files`. You can use this to specify
a list of filenames or directories to check. In |Flake8| 3.0, however, we
return a different object that has similar methods. We return a |Report| which
has the method

.. automethod:: flake8.api.legacy.Report.get_statistics

Most usage of this method that we noted was as documented above. Keep in mind,
however, that it provides a list of strings and not anything more malleable.


Autogenerated Legacy Documentation
----------------------------------

.. automodule:: flake8.api.legacy
    :members:

.. autoclass:: flake8.api.legacy.StyleGuide
    :members: options, paths

.. autoclass:: flake8.api.legacy.Report
    :members: total_errors


.. |style_guide| replace:: :func:`flake8.api.legacy.get_style_guide`
.. |StyleGuide| replace:: :class:`flake8.api.legacy.StyleGuide`
.. |Report| replace:: :class:`flake8.api.legacy.Report`
```

## File: `docs/source/user/using-hooks.rst`
```
=============================
 Using Version Control Hooks
=============================

Usage with the `pre-commit`_ git hooks framework
================================================

|Flake8| can be included as a hook for `pre-commit`_.  The easiest way to get
started is to add this configuration to your ``.pre-commit-config.yaml``:

.. code-block:: yaml

    -   repo: https://github.com/pycqa/flake8
        rev: ''  # pick a git hash / tag to point to
        hooks:
        -   id: flake8

See the `pre-commit docs`_ for how to customize this configuration.

Checked-in python files will be passed as positional arguments.  ``flake8``
will always lint explicitly passed arguments (:option:`flake8 --exclude` has
no effect).  Instead use ``pre-commit``'s ``exclude: ...`` regex to exclude
files.  ``pre-commit`` won't ever pass untracked files to ``flake8`` so
excluding ``.git`` / ``.tox`` / etc. is unnecessary.

.. code-block:: yaml

        -   id: flake8
            exclude: ^testing/(data|examples)/

``pre-commit`` creates an isolated environment for hooks.  To use ``flake8``
plugins, use the ``additional_dependencies`` setting.

.. code-block:: yaml

        -   id: flake8
            additional_dependencies: [flake8-docstrings]

.. _pre-commit:
    https://pre-commit.com/
.. _pre-commit docs:
    https://pre-commit.com/#pre-commit-configyaml---hooks
```

## File: `docs/source/user/using-plugins.rst`
```
==================================
 Using Plugins For Fun and Profit
==================================

|Flake8| is useful on its own but a lot of |Flake8|'s popularity is due to
its extensibility. Our community has developed :term:`plugin`\ s that augment
|Flake8|'s behaviour. Most of these plugins are uploaded to PyPI_. The
developers of these plugins often have some style they wish to enforce.

For example, `flake8-docstrings`_ adds a check for :pep:`257` style
conformance. Others attempt to enforce consistency, like `flake8-quotes`_.

.. note::

    The accuracy or reliability of these plugins may vary wildly from plugin
    to plugin and not all plugins are guaranteed to work with |Flake8| 3.0.

To install a third-party plugin, make sure that you know which version of
Python (or pip) you used to install |Flake8|. You can then use the most
appropriate of:

.. prompt:: bash

    pip install <plugin-name>
    pip3 install <plugin-name>
    python -m pip install <plugin-name>
    python3 -m pip install <plugin-name>
    python3.9 -m pip install <plugin-name>

To install the plugin, where ``<plugin-name>`` is the package name on PyPI_.
To verify installation use:

.. prompt:: bash

    flake8 --version
    python<version> -m flake8 --version

To see the plugin's name and version in the output.

.. seealso:: :ref:`How to Invoke Flake8 <invocation>`

After installation, most plugins immediately start reporting :term:`error`\ s.
Check the plugin's documentation for which error codes it returns and if it
disables any by default.

.. note::

    You can use both :option:`flake8 --select` and :option:`flake8 --ignore`
    with plugins.

Some plugins register new options, so be sure to check :option:`flake8 --help`
for new flags and documentation. These plugins may also allow these flags to
be specified in your configuration file. Hopefully, the plugin authors have
documented this for you.

.. seealso:: :ref:`Configuring Flake8 <configuration>`


.. _PyPI:
    https://pypi.org/
.. _flake8-docstrings:
    https://pypi.org/project/flake8-docstrings/
.. _flake8-quotes:
    https://pypi.org/project/flake8-quotes/
```

## File: `docs/source/user/violations.rst`
```
===================================
 Selecting and Ignoring Violations
===================================

It is possible to select and ignore certain violations reported by |Flake8|
and the plugins we've installed. It's also possible as of |Flake8| 3.0 to
combine usage of :option:`flake8 --select` and :option:`flake8 --ignore`. This
chapter of the User Guide aims to educate about how Flake8 will report errors
based on different inputs.



Ignoring Violations with Flake8
===============================

By default, |Flake8| has a list of error codes that it ignores. The list used
by a version of |Flake8| may be different than the list used by a different
version. To see the default list, :option:`flake8 --help` will
show the output with the current default list.

Extending the Default Ignore List
---------------------------------

If we want to extend the default list of ignored error codes, we can use
:option:`flake8 --extend-ignore` to specify a comma-separated list of codes
for a specific run on the command line, e.g.,

.. prompt:: bash

    flake8 --extend-ignore=E1,E23 path/to/files/ path/to/more/files

This tells |Flake8| to ignore any error codes starting with ``E1`` and ``E23``,
in addition the default ignore list. To view the default error code ignore
list, run :option:`flake8 --help` and refer to the help text for
:option:`flake8 --ignore`.


..
   The section below used to be titled `Changing the Default Ignore List`, but
   was renamed for clarity.
   Explicitly retain the old section anchor so as to not break links:

.. _changing-the-ignore-list:

Overriding the Default Ignore List
----------------------------------

If we want to *completely* override the default list of ignored error codes, we
can use :option:`flake8 --ignore` to specify a comma-separated list of codes
for a specific run on the command-line, e.g.,

.. prompt:: bash

    flake8 --ignore=E1,E23,W503 path/to/files/ path/to/more/files/

This tells |Flake8| to *only* ignore error codes starting with ``E1``, ``E23``,
or ``W503`` while it is running.

.. note::

    The documentation for :option:`flake8 --ignore` shows examples for how
    to change the ignore list in the configuration file. See also
    :ref:`configuration` as well for details about how to use configuration
    files.


In-line Ignoring Errors
-----------------------

In some cases, we might not want to ignore an error code (or class of error
codes) for the entirety of our project. Instead, we might want to ignore the
specific error code on a specific line. Let's take for example a line like

.. code-block:: python

    example = lambda: 'example'

Sometimes we genuinely need something this simple. We could instead define
a function like we normally would. Note, in some contexts this distracts from
what is actually happening. In those cases, we can also do:

.. code-block:: python

    example = lambda: 'example'  # noqa: E731

This will only ignore the error from pycodestyle that checks for lambda
assignments and generates an ``E731``. If there are other errors on the line
then those will be reported. ``# noqa`` is case-insensitive, without the colon
the part after ``# noqa`` would be ignored.

.. note::

    If we ever want to disable |Flake8| respecting ``# noqa`` comments, we can
    refer to :option:`flake8 --disable-noqa`.

If we instead had more than one error that we wished to ignore, we could
list all of the errors with commas separating them:

.. code-block:: python

    # noqa: E731,E123

Finally, if we have a particularly bad line of code, we can ignore every error
using simply ``# noqa`` with nothing after it.

Contents before and after the ``# noqa: ...`` portion are ignored so multiple
comments may appear on one line.  Here are several examples:

.. code-block:: python

    # mypy requires `# type: ignore` to appear first
    x = 5  # type: ignore  # noqa: ABC123

    # can use to add useful user information to a noqa comment
    y = 6  # noqa: ABC456  # TODO: will fix this later


Ignoring Entire Files
---------------------

Imagine a situation where we are adding |Flake8| to a codebase. Let's further
imagine that with the exception of a few particularly bad files, we can add
|Flake8| easily and move on with our lives. There are two ways to ignore the
file:

#. By explicitly adding it to our list of excluded paths (see: :option:`flake8
   --exclude`)

#. By adding ``# flake8: noqa`` to the file

The former is the **recommended** way of ignoring entire files. By using our
exclude list, we can include it in our configuration file and have one central
place to find what files aren't included in |Flake8| checks. The latter has the
benefit that when we run |Flake8| with :option:`flake8 --disable-noqa` all of
the errors in that file will show up without having to modify our
configuration. Both exist so we can choose which is better for us.



Selecting Violations with Flake8
================================

|Flake8| has a default list of violation classes that we use. This list is:

- ``C90``

  All ``C90`` class violations are reported when the user specifies
  :option:`flake8 --max-complexity`

- ``E``

  All ``E`` class violations are "errors" reported by pycodestyle

- ``F``

  All ``F`` class violations are reported by pyflakes

- ``W``

  All ``W`` class violations are "warnings" reported by pycodestyle

This list can be overridden by specifying :option:`flake8 --select`. Just as
specifying :option:`flake8 --ignore` will change the behaviour of |Flake8|, so
will :option:`flake8 --select`.

Let's look through some examples using this sample code:

.. code-block:: python

    # example.py
    def foo():
        print(
                    "Hello"
            "World"
            )

By default, if we run ``flake8`` on this file we'll get:

.. prompt:: bash

    flake8 example.py

.. code:: text

    example.py:4:9: E131 continuation line unaligned for hanging indent

Now let's select all ``E`` class violations:

.. prompt:: bash

    flake8 --select E example.py

.. code:: text

    example.py:3:17: E126 continuation line over-indented for hanging indent
    example.py:4:9: E131 continuation line unaligned for hanging indent
    example.py:5:9: E121 continuation line under-indented for hanging indent

Suddenly we now have far more errors that are reported to us. Using
``--select`` alone will override the default ``--ignore`` list. In these cases,
the user is telling us that they want all ``E`` violations and so we ignore
our list of violations that we ignore by default.

We can also be highly specific. For example, we can do

.. prompt:: bash

    flake8 --select E121 example.py

.. code:: text

    example.py:5:9: E121 continuation line under-indented for hanging indent

We can also specify lists of items to select both on the command-line and in
our configuration files.

.. prompt:: bash

    flake8 --select E121,E131 example.py

.. code:: text

    example.py:4:9: E131 continuation line unaligned for hanging indent
    example.py:5:9: E121 continuation line under-indented for hanging indent



Selecting and Ignoring Simultaneously For Fun and Profit
========================================================

Prior to |Flake8| 3.0, all handling of :option:`flake8 --select` and
:option:`flake8 --ignore` was delegated to pycodestyle. Its handling of the
options significantly differs from how |Flake8| 3.0 has been designed.

pycodestyle has always preferred ``--ignore`` over ``--select`` and will
ignore ``--select`` if the user provides both. |Flake8| 3.0 will now do its
best to intuitively combine both options provided by the user. Let's look at
some examples using:

.. code-block:: python

    # example.py
    import os


    def foo():
        var = 1
        print(
                    "Hello"
            "World"
            )

If we run |Flake8| with its default settings we get:

.. prompt:: bash

    flake8 example.py

.. code:: text

    example.py:1:1: F401 'os' imported but unused
    example.py:5:5: F841 local variable 'var' is assigned to but never used
    example.py:8:9: E131 continuation line unaligned for hanging indent

Now let's select all ``E`` and ``F`` violations including those in the default
ignore list.

.. prompt:: bash

    flake8 --select E,F example.py

.. code:: text

    example.py:1:1: F401 'os' imported but unused
    example.py:5:5: F841 local variable 'var' is assigned to but never used
    example.py:7:17: E126 continuation line over-indented for hanging indent
    example.py:8:9: E131 continuation line unaligned for hanging indent
    example.py:9:9: E121 continuation line under-indented for hanging indent

Now let's selectively ignore some of these while selecting the rest:

.. prompt:: bash

    flake8 --select E,F --ignore F401,E121 example.py

.. code:: text

    example.py:5:5: F841 local variable 'var' is assigned to but never used
    example.py:7:17: E126 continuation line over-indented for hanging indent
    example.py:8:9: E131 continuation line unaligned for hanging indent

Via this example, we can see that the *most specific* **user-specified** rule
will win. So in the above, we had very vague select rules and two very
specific ignore rules. Let's look at a different example:

.. prompt:: bash

    flake8 --select F401,E131 --ignore E,F example.py

.. code:: text

    example.py:1:1: F401 'os' imported but unused
    example.py:8:9: E131 continuation line unaligned for hanging indent

In this case, we see that since our selected violation codes were more
specific those were reported.
```

## File: `example-plugin/setup.py`
```python
from __future__ import annotations

import setuptools

setuptools.setup(
    name="flake8-example-plugin",
    license="MIT",
    version="1.0.0",
    description="Example plugin to Flake8",
    author="Ian Cordasco",
    author_email="graffatcolmingov@gmail.com",
    url="https://github.com/pycqa/flake8",
    package_dir={"": "src/"},
    packages=["flake8_example_plugin"],
    entry_points={
        "flake8.extension": [
            "X1 = flake8_example_plugin:ExampleOne",
            "X2 = flake8_example_plugin:ExampleTwo",
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
```

## File: `example-plugin/src/flake8_example_plugin/__init__.py`
```python
"""Module for an example Flake8 plugin."""
from __future__ import annotations

from .off_by_default import ExampleTwo
from .on_by_default import ExampleOne

__all__ = (
    "ExampleOne",
    "ExampleTwo",
)
```

## File: `example-plugin/src/flake8_example_plugin/off_by_default.py`
```python
"""Our first example plugin."""
from __future__ import annotations


class ExampleTwo:
    """Second Example Plugin."""

    off_by_default = True

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        """Do nothing."""
        yield (
            1,
            0,
            "X200 The off-by-default plugin was enabled",
            "OffByDefaultPlugin",
        )
```

## File: `example-plugin/src/flake8_example_plugin/on_by_default.py`
```python
"""Our first example plugin."""
from __future__ import annotations


class ExampleOne:
    """First Example Plugin."""

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        """Do nothing."""
        yield from []
```

## File: `src/flake8/__init__.py`
```python
"""Top-level module for Flake8.

This module

- initializes logging for the command-line tool
- tracks the version of the package
- provides a way to configure logging for the command-line tool

.. autofunction:: flake8.configure_logging

"""
from __future__ import annotations

import logging
import sys

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.NullHandler())

__version__ = "7.3.0"
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

_VERBOSITY_TO_LOG_LEVEL = {
    # output more than warnings but not debugging info
    1: logging.INFO,  # INFO is a numerical level of 20
    # output debugging information
    2: logging.DEBUG,  # DEBUG is a numerical level of 10
}

LOG_FORMAT = (
    "%(name)-25s %(processName)-11s %(relativeCreated)6d "
    "%(levelname)-8s %(message)s"
)


def configure_logging(
    verbosity: int,
    filename: str | None = None,
    logformat: str = LOG_FORMAT,
) -> None:
    """Configure logging for flake8.

    :param verbosity:
        How verbose to be in logging information.
    :param filename:
        Name of the file to append log information to.
        If ``None`` this will log to ``sys.stderr``.
        If the name is "stdout" or "stderr" this will log to the appropriate
        stream.
    """
    if verbosity <= 0:
        return

    verbosity = min(verbosity, max(_VERBOSITY_TO_LOG_LEVEL))
    log_level = _VERBOSITY_TO_LOG_LEVEL[verbosity]

    if not filename or filename in ("stderr", "stdout"):
        fileobj = getattr(sys, filename or "stderr")
        handler_cls: type[logging.Handler] = logging.StreamHandler
    else:
        fileobj = filename
        handler_cls = logging.FileHandler

    handler = handler_cls(fileobj)
    handler.setFormatter(logging.Formatter(logformat))
    LOG.addHandler(handler)
    LOG.setLevel(log_level)
    LOG.debug(
        "Added a %s logging handler to logger root at %s", filename, __name__,
    )
```

## File: `src/flake8/__main__.py`
```python
"""Module allowing for ``python -m flake8 ...``."""
from __future__ import annotations

from flake8.main.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
```

## File: `src/flake8/_compat.py`
```python
from __future__ import annotations

import sys
import tokenize

if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
    FSTRING_START = tokenize.FSTRING_START
    FSTRING_MIDDLE = tokenize.FSTRING_MIDDLE
    FSTRING_END = tokenize.FSTRING_END
else:  # pragma: <3.12 cover
    FSTRING_START = FSTRING_MIDDLE = FSTRING_END = -1

if sys.version_info >= (3, 14):  # pragma: >=3.14 cover
    TSTRING_START = tokenize.TSTRING_START
    TSTRING_MIDDLE = tokenize.TSTRING_MIDDLE
    TSTRING_END = tokenize.TSTRING_END
else:  # pragma: <3.14 cover
    TSTRING_START = TSTRING_MIDDLE = TSTRING_END = -1
```

## File: `src/flake8/checker.py`
```python
"""Checker Manager and Checker classes."""
from __future__ import annotations

import argparse
import contextlib
import errno
import logging
import multiprocessing.pool
import operator
import signal
import tokenize
from collections.abc import Generator
from collections.abc import Sequence
from typing import Any
from typing import Optional

from flake8 import defaults
from flake8 import exceptions
from flake8 import processor
from flake8 import utils
from flake8._compat import FSTRING_START
from flake8._compat import TSTRING_START
from flake8.discover_files import expand_paths
from flake8.options.parse_args import parse_args
from flake8.plugins.finder import Checkers
from flake8.plugins.finder import LoadedPlugin
from flake8.style_guide import StyleGuideManager

Results = list[tuple[str, int, int, str, Optional[str]]]

LOG = logging.getLogger(__name__)

SERIAL_RETRY_ERRNOS = {
    # ENOSPC: Added by sigmavirus24
    # > On some operating systems (OSX), multiprocessing may cause an
    # > ENOSPC error while trying to create a Semaphore.
    # > In those cases, we should replace the customized Queue Report
    # > class with pep8's StandardReport class to ensure users don't run
    # > into this problem.
    # > (See also: https://github.com/pycqa/flake8/issues/117)
    errno.ENOSPC,
    # NOTE(sigmavirus24): When adding to this list, include the reasoning
    # on the lines before the error code and always append your error
    # code. Further, please always add a trailing `,` to reduce the visual
    # noise in diffs.
}

_mp: tuple[Checkers, argparse.Namespace] | None = None


@contextlib.contextmanager
def _mp_prefork(
    plugins: Checkers, options: argparse.Namespace,
) -> Generator[None]:
    # we can save significant startup work w/ `fork` multiprocessing
    global _mp
    _mp = plugins, options
    try:
        yield
    finally:
        _mp = None


def _mp_init(argv: Sequence[str]) -> None:
    global _mp

    # Ensure correct signaling of ^C using multiprocessing.Pool.
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    # for `fork` this'll already be set
    if _mp is None:
        plugins, options = parse_args(argv)
        _mp = plugins.checkers, options


def _mp_run(filename: str) -> tuple[str, Results, dict[str, int]]:
    assert _mp is not None, _mp
    plugins, options = _mp
    return FileChecker(
        filename=filename, plugins=plugins, options=options,
    ).run_checks()


class Manager:
    """Manage the parallelism and checker instances for each plugin and file.

    This class will be responsible for the following:

    - Determining the parallelism of Flake8, e.g.:

      * Do we use :mod:`multiprocessing` or is it unavailable?

      * Do we automatically decide on the number of jobs to use or did the
        user provide that?

    - Falling back to a serial way of processing files if we run into an
      OSError related to :mod:`multiprocessing`

    - Organizing the results of each checker so we can group the output
      together and make our output deterministic.
    """

    def __init__(
        self,
        style_guide: StyleGuideManager,
        plugins: Checkers,
        argv: Sequence[str],
    ) -> None:
        """Initialize our Manager instance."""
        self.style_guide = style_guide
        self.options = style_guide.options
        self.plugins = plugins
        self.jobs = self._job_count()
        self.statistics = {
            "files": 0,
            "logical lines": 0,
            "physical lines": 0,
            "tokens": 0,
        }
        self.exclude = (*self.options.exclude, *self.options.extend_exclude)
        self.argv = argv
        self.results: list[tuple[str, Results, dict[str, int]]] = []

    def _process_statistics(self) -> None:
        for _, _, statistics in self.results:
            for statistic in defaults.STATISTIC_NAMES:
                self.statistics[statistic] += statistics[statistic]
        self.statistics["files"] += len(self.filenames)

    def _job_count(self) -> int:
        # First we walk through all of our error cases:
        # - multiprocessing library is not present
        # - the user provided stdin and that's not something we can handle
        #   well
        # - the user provided some awful input

        if utils.is_using_stdin(self.options.filenames):
            LOG.warning(
                "The --jobs option is not compatible with supplying "
                "input using - . Ignoring --jobs arguments.",
            )
            return 0

        jobs = self.options.jobs

        # If the value is "auto", we want to let the multiprocessing library
        # decide the number based on the number of CPUs. However, if that
        # function is not implemented for this particular value of Python we
        # default to 1
        if jobs.is_auto:
            try:
                return multiprocessing.cpu_count()
            except NotImplementedError:
                return 0

        # Otherwise, we know jobs should be an integer and we can just convert
        # it to an integer
        return jobs.n_jobs

    def _handle_results(self, filename: str, results: Results) -> int:
        style_guide = self.style_guide
        reported_results_count = 0
        for error_code, line_number, column, text, physical_line in results:
            reported_results_count += style_guide.handle_error(
                code=error_code,
                filename=filename,
                line_number=line_number,
                column_number=column,
                text=text,
                physical_line=physical_line,
            )
        return reported_results_count

    def report(self) -> tuple[int, int]:
        """Report all of the errors found in the managed file checkers.

        This iterates over each of the checkers and reports the errors sorted
        by line number.

        :returns:
            A tuple of the total results found and the results reported.
        """
        results_reported = results_found = 0
        self.results.sort(key=operator.itemgetter(0))
        for filename, results, _ in self.results:
            results.sort(key=operator.itemgetter(1, 2))
            with self.style_guide.processing_file(filename):
                results_reported += self._handle_results(filename, results)
            results_found += len(results)
        return (results_found, results_reported)

    def run_parallel(self) -> None:
        """Run the checkers in parallel."""
        with _mp_prefork(self.plugins, self.options):
            pool = _try_initialize_processpool(self.jobs, self.argv)

        if pool is None:
            self.run_serial()
            return

        pool_closed = False
        try:
            self.results = list(pool.imap_unordered(_mp_run, self.filenames))
            pool.close()
            pool.join()
            pool_closed = True
        finally:
            if not pool_closed:
                pool.terminate()
                pool.join()

    def run_serial(self) -> None:
        """Run the checkers in serial."""
        self.results = [
            FileChecker(
                filename=filename,
                plugins=self.plugins,
                options=self.options,
            ).run_checks()
            for filename in self.filenames
        ]

    def run(self) -> None:
        """Run all the checkers.

        This will intelligently decide whether to run the checks in parallel
        or whether to run them in serial.

        If running the checks in parallel causes a problem (e.g.,
        :issue:`117`) this also implements fallback to serial processing.
        """
        try:
            if self.jobs > 1 and len(self.filenames) > 1:
                self.run_parallel()
            else:
                self.run_serial()
        except KeyboardInterrupt:
            LOG.warning("Flake8 was interrupted by the user")
            raise exceptions.EarlyQuit("Early quit while running checks")

    def start(self) -> None:
        """Start checking files.

        :param paths:
            Path names to check. This is passed directly to
            :meth:`~Manager.make_checkers`.
        """
        LOG.info("Making checkers")
        self.filenames = tuple(
            expand_paths(
                paths=self.options.filenames,
                stdin_display_name=self.options.stdin_display_name,
                filename_patterns=self.options.filename,
                exclude=self.exclude,
            ),
        )
        self.jobs = min(len(self.filenames), self.jobs)

    def stop(self) -> None:
        """Stop checking files."""
        self._process_statistics()


class FileChecker:
    """Manage running checks for a file and aggregate the results."""

    def __init__(
        self,
        *,
        filename: str,
        plugins: Checkers,
        options: argparse.Namespace,
    ) -> None:
        """Initialize our file checker."""
        self.options = options
        self.filename = filename
        self.plugins = plugins
        self.results: Results = []
        self.statistics = {
            "tokens": 0,
            "logical lines": 0,
            "physical lines": 0,
        }
        self.processor = self._make_processor()
        self.display_name = filename
        self.should_process = False
        if self.processor is not None:
            self.display_name = self.processor.filename
            self.should_process = not self.processor.should_ignore_file()
            self.statistics["physical lines"] = len(self.processor.lines)

    def __repr__(self) -> str:
        """Provide helpful debugging representation."""
        return f"FileChecker for {self.filename}"

    def _make_processor(self) -> processor.FileProcessor | None:
        try:
            return processor.FileProcessor(self.filename, self.options)
        except OSError as e:
            # If we can not read the file due to an IOError (e.g., the file
            # does not exist or we do not have the permissions to open it)
            # then we need to format that exception for the user.
            # NOTE(sigmavirus24): Historically, pep8 has always reported this
            # as an E902. We probably *want* a better error code for this
            # going forward.
            self.report("E902", 0, 0, f"{type(e).__name__}: {e}")
            return None

    def report(
        self,
        error_code: str | None,
        line_number: int,
        column: int,
        text: str,
    ) -> str:
        """Report an error by storing it in the results list."""
        if error_code is None:
            error_code, text = text.split(" ", 1)

        # If we're recovering from a problem in _make_processor, we will not
        # have this attribute.
        if hasattr(self, "processor") and self.processor is not None:
            line = self.processor.noqa_line_for(line_number)
        else:
            line = None

        self.results.append((error_code, line_number, column, text, line))
        return error_code

    def run_check(self, plugin: LoadedPlugin, **arguments: Any) -> Any:
        """Run the check in a single plugin."""
        assert self.processor is not None, self.filename
        try:
            params = self.processor.keyword_arguments_for(
                plugin.parameters, arguments,
            )
        except AttributeError as ae:
            raise exceptions.PluginRequestedUnknownParameters(
                plugin_name=plugin.display_name, exception=ae,
            )
        try:
            return plugin.obj(**arguments, **params)
        except Exception as all_exc:
            LOG.critical(
                "Plugin %s raised an unexpected exception",
                plugin.display_name,
                exc_info=True,
            )
            raise exceptions.PluginExecutionFailed(
                filename=self.filename,
                plugin_name=plugin.display_name,
                exception=all_exc,
            )

    @staticmethod
    def _extract_syntax_information(exception: Exception) -> tuple[int, int]:
        if (
            len(exception.args) > 1
            and exception.args[1]
            and len(exception.args[1]) > 2
        ):
            token = exception.args[1]
            row, column = token[1:3]
        elif (
            isinstance(exception, tokenize.TokenError)
            and len(exception.args) == 2
            and len(exception.args[1]) == 2
        ):
            token = ()
            row, column = exception.args[1]
        else:
            token = ()
            row, column = (1, 0)

        return row, column

    def run_ast_checks(self) -> None:
        """Run all checks expecting an abstract syntax tree."""
        assert self.processor is not None, self.filename
        ast = self.processor.build_ast()

        for plugin in self.plugins.tree:
            checker = self.run_check(plugin, tree=ast)
            # If the plugin uses a class, call the run method of it, otherwise
            # the call should return something iterable itself
            try:
                runner = checker.run()
            except AttributeError:
                runner = checker
            for line_number, offset, text, _ in runner:
                self.report(
                    error_code=None,
                    line_number=line_number,
                    column=offset,
                    text=text,
                )

    def run_logical_checks(self) -> None:
        """Run all checks expecting a logical line."""
        assert self.processor is not None
        comments, logical_line, mapping = self.processor.build_logical_line()
        if not mapping:
            return
        self.processor.update_state(mapping)

        LOG.debug('Logical line: "%s"', logical_line.rstrip())

        for plugin in self.plugins.logical_line:
            self.processor.update_checker_state_for(plugin)
            results = self.run_check(plugin, logical_line=logical_line) or ()
            for offset, text in results:
                line_number, column_offset = find_offset(offset, mapping)
                if line_number == column_offset == 0:
                    LOG.warning("position of error out of bounds: %s", plugin)
                self.report(
                    error_code=None,
                    line_number=line_number,
                    column=column_offset,
                    text=text,
                )

        self.processor.next_logical_line()

    def run_physical_checks(self, physical_line: str) -> None:
        """Run all checks for a given physical line.

        A single physical check may return multiple errors.
        """
        assert self.processor is not None
        for plugin in self.plugins.physical_line:
            self.processor.update_checker_state_for(plugin)
            result = self.run_check(plugin, physical_line=physical_line)

            if result is not None:
                # This is a single result if first element is an int
                column_offset = None
                try:
                    column_offset = result[0]
                except (IndexError, TypeError):
                    pass

                if isinstance(column_offset, int):
                    # If we only have a single result, convert to a collection
                    result = (result,)

                for result_single in result:
                    column_offset, text = result_single
                    self.report(
                        error_code=None,
                        line_number=self.processor.line_number,
                        column=column_offset,
                        text=text,
                    )

    def process_tokens(self) -> None:
        """Process tokens and trigger checks.

        Instead of using this directly, you should use
        :meth:`flake8.checker.FileChecker.run_checks`.
        """
        assert self.processor is not None
        parens = 0
        statistics = self.statistics
        file_processor = self.processor
        prev_physical = ""
        for token in file_processor.generate_tokens():
            statistics["tokens"] += 1
            self.check_physical_eol(token, prev_physical)
            token_type, text = token[0:2]
            if token_type == tokenize.OP:
                parens = processor.count_parentheses(parens, text)
            elif parens == 0:
                if processor.token_is_newline(token):
                    self.handle_newline(token_type)
            prev_physical = token[4]

        if file_processor.tokens:
            # If any tokens are left over, process them
            self.run_physical_checks(file_processor.lines[-1])
            self.run_logical_checks()

    def run_checks(self) -> tuple[str, Results, dict[str, int]]:
        """Run checks against the file."""
        if self.processor is None or not self.should_process:
            return self.display_name, self.results, self.statistics

        try:
            self.run_ast_checks()
            self.process_tokens()
        except (SyntaxError, tokenize.TokenError) as e:
            code = "E902" if isinstance(e, tokenize.TokenError) else "E999"
            row, column = self._extract_syntax_information(e)
            self.report(code, row, column, f"{type(e).__name__}: {e.args[0]}")
            return self.display_name, self.results, self.statistics

        logical_lines = self.processor.statistics["logical lines"]
        self.statistics["logical lines"] = logical_lines
        return self.display_name, self.results, self.statistics

    def handle_newline(self, token_type: int) -> None:
        """Handle the logic when encountering a newline token."""
        assert self.processor is not None
        if token_type == tokenize.NEWLINE:
            self.run_logical_checks()
            self.processor.reset_blank_before()
        elif len(self.processor.tokens) == 1:
            # The physical line contains only this token.
            self.processor.visited_new_blank_line()
            self.processor.delete_first_token()
        else:
            self.run_logical_checks()

    def check_physical_eol(
        self, token: tokenize.TokenInfo, prev_physical: str,
    ) -> None:
        """Run physical checks if and only if it is at the end of the line."""
        assert self.processor is not None
        if token.type == FSTRING_START:  # pragma: >=3.12 cover
            self.processor.fstring_start(token.start[0])
        elif token.type == TSTRING_START:  # pragma: >=3.14 cover
            self.processor.tstring_start(token.start[0])
        # a newline token ends a single physical line.
        elif processor.is_eol_token(token):
            # if the file does not end with a newline, the NEWLINE
            # token is inserted by the parser, but it does not contain
            # the previous physical line in `token[4]`
            if token.line == "":
                self.run_physical_checks(prev_physical)
            else:
                self.run_physical_checks(token.line)
        elif processor.is_multiline_string(token):
            # Less obviously, a string that contains newlines is a
            # multiline string, either triple-quoted or with internal
            # newlines backslash-escaped. Check every physical line in the
            # string *except* for the last one: its newline is outside of
            # the multiline string, so we consider it a regular physical
            # line, and will check it like any other physical line.
            #
            # Subtleties:
            # - have to wind self.line_number back because initially it
            #   points to the last line of the string, and we want
            #   check_physical() to give accurate feedback
            for line in self.processor.multiline_string(token):
                self.run_physical_checks(line)


def _try_initialize_processpool(
    job_count: int,
    argv: Sequence[str],
) -> multiprocessing.pool.Pool | None:
    """Return a new process pool instance if we are able to create one."""
    try:
        return multiprocessing.Pool(job_count, _mp_init, initargs=(argv,))
    except OSError as err:
        if err.errno not in SERIAL_RETRY_ERRNOS:
            raise
    except ImportError:
        pass

    return None


def find_offset(
    offset: int, mapping: processor._LogicalMapping,
) -> tuple[int, int]:
    """Find the offset tuple for a single offset."""
    if isinstance(offset, tuple):
        return offset

    for token in mapping:
        token_offset = token[0]
        if offset <= token_offset:
            position = token[1]
            break
    else:
        position = (0, 0)
        offset = token_offset = 0
    return (position[0], position[1] + offset - token_offset)
```

## File: `src/flake8/defaults.py`
```python
"""Constants that define defaults."""
from __future__ import annotations

import re

EXCLUDE = (
    ".svn",
    "CVS",
    ".bzr",
    ".hg",
    ".git",
    "__pycache__",
    ".tox",
    ".nox",
    ".eggs",
    "*.egg",
)
IGNORE = ("E121", "E123", "E126", "E226", "E24", "E704", "W503", "W504")
MAX_LINE_LENGTH = 79
INDENT_SIZE = 4

# Other constants
WHITESPACE = frozenset(" \t")

STATISTIC_NAMES = ("logical lines", "physical lines", "tokens")

NOQA_INLINE_REGEXP = re.compile(
    # We're looking for items that look like this:
    # ``# noqa``
    # ``# noqa: E123``
    # ``# noqa: E123,W451,F921``
    # ``# noqa:E123,W451,F921``
    # ``# NoQA: E123,W451,F921``
    # ``# NOQA: E123,W451,F921``
    # ``# NOQA:E123,W451,F921``
    # We do not want to capture the ``: `` that follows ``noqa``
    # We do not care about the casing of ``noqa``
    # We want a comma-separated list of errors
    r"# noqa(?::[\s]?(?P<codes>([A-Z]+[0-9]+(?:[,\s]+)?)+))?",
    re.IGNORECASE,
)

NOQA_FILE = re.compile(r"\s*# flake8[:=]\s*noqa", re.I)

VALID_CODE_PREFIX = re.compile("^[A-Z]{1,3}[0-9]{0,3}$", re.ASCII)
```

## File: `src/flake8/discover_files.py`
```python
"""Functions related to discovering paths."""
from __future__ import annotations

import logging
import os.path
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Sequence

from flake8 import utils

LOG = logging.getLogger(__name__)


def _filenames_from(
    arg: str,
    *,
    predicate: Callable[[str], bool],
) -> Generator[str]:
    """Generate filenames from an argument.

    :param arg:
        Parameter from the command-line.
    :param predicate:
        Predicate to use to filter out filenames. If the predicate
        returns ``True`` we will exclude the filename, otherwise we
        will yield it. By default, we include every filename
        generated.
    :returns:
        Generator of paths
    """
    if predicate(arg):
        return

    if os.path.isdir(arg):
        for root, sub_directories, files in os.walk(arg):
            # NOTE(sigmavirus24): os.walk() will skip a directory if you
            # remove it from the list of sub-directories.
            for directory in tuple(sub_directories):
                joined = os.path.join(root, directory)
                if predicate(joined):
                    sub_directories.remove(directory)

            for filename in files:
                joined = os.path.join(root, filename)
                if not predicate(joined):
                    yield joined
    else:
        yield arg


def expand_paths(
    *,
    paths: Sequence[str],
    stdin_display_name: str,
    filename_patterns: Sequence[str],
    exclude: Sequence[str],
) -> Generator[str]:
    """Expand out ``paths`` from commandline to the lintable files."""
    if not paths:
        paths = ["."]

    def is_excluded(arg: str) -> bool:
        if arg == "-":
            # if the stdin_display_name is the default, always include it
            if stdin_display_name == "stdin":
                return False
            arg = stdin_display_name

        return utils.matches_filename(
            arg,
            patterns=exclude,
            log_message='"%(path)s" has %(whether)sbeen excluded',
            logger=LOG,
        )

    return (
        filename
        for path in paths
        for filename in _filenames_from(path, predicate=is_excluded)
        if (
            # always lint `-`
            filename == "-"
            # always lint explicitly passed (even if not matching filter)
            or path == filename
            # otherwise, check the file against filtered patterns
            or utils.fnmatch(filename, filename_patterns)
        )
    )
```

## File: `src/flake8/exceptions.py`
```python
"""Exception classes for all of Flake8."""
from __future__ import annotations


class Flake8Exception(Exception):
    """Plain Flake8 exception."""


class EarlyQuit(Flake8Exception):
    """Except raised when encountering a KeyboardInterrupt."""


class ExecutionError(Flake8Exception):
    """Exception raised during execution of Flake8."""


class FailedToLoadPlugin(Flake8Exception):
    """Exception raised when a plugin fails to load."""

    FORMAT = 'Flake8 failed to load plugin "%(name)s" due to %(exc)s.'

    def __init__(self, plugin_name: str, exception: Exception) -> None:
        """Initialize our FailedToLoadPlugin exception."""
        self.plugin_name = plugin_name
        self.original_exception = exception
        super().__init__(plugin_name, exception)

    def __str__(self) -> str:
        """Format our exception message."""
        return self.FORMAT % {
            "name": self.plugin_name,
            "exc": self.original_exception,
        }


class PluginRequestedUnknownParameters(Flake8Exception):
    """The plugin requested unknown parameters."""

    FORMAT = '"%(name)s" requested unknown parameters causing %(exc)s'

    def __init__(self, plugin_name: str, exception: Exception) -> None:
        """Pop certain keyword arguments for initialization."""
        self.plugin_name = plugin_name
        self.original_exception = exception
        super().__init__(plugin_name, exception)

    def __str__(self) -> str:
        """Format our exception message."""
        return self.FORMAT % {
            "name": self.plugin_name,
            "exc": self.original_exception,
        }


class PluginExecutionFailed(Flake8Exception):
    """The plugin failed during execution."""

    FORMAT = '{fname}: "{plugin}" failed during execution due to {exc!r}'

    def __init__(
        self,
        filename: str,
        plugin_name: str,
        exception: Exception,
    ) -> None:
        """Utilize keyword arguments for message generation."""
        self.filename = filename
        self.plugin_name = plugin_name
        self.original_exception = exception
        super().__init__(filename, plugin_name, exception)

    def __str__(self) -> str:
        """Format our exception message."""
        return self.FORMAT.format(
            fname=self.filename,
            plugin=self.plugin_name,
            exc=self.original_exception,
        )
```

## File: `src/flake8/processor.py`
```python
"""Module containing our file processor that tokenizes a file for checks."""
from __future__ import annotations

import argparse
import ast
import functools
import logging
import tokenize
from collections.abc import Generator
from typing import Any

from flake8 import defaults
from flake8 import utils
from flake8._compat import FSTRING_END
from flake8._compat import FSTRING_MIDDLE
from flake8._compat import TSTRING_END
from flake8._compat import TSTRING_MIDDLE
from flake8.plugins.finder import LoadedPlugin

LOG = logging.getLogger(__name__)
NEWLINE = frozenset([tokenize.NL, tokenize.NEWLINE])

SKIP_TOKENS = frozenset(
    [tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT],
)

_LogicalMapping = list[tuple[int, tuple[int, int]]]
_Logical = tuple[list[str], list[str], _LogicalMapping]


class FileProcessor:
    """Processes a file and holds state.

    This processes a file by generating tokens, logical and physical lines,
    and AST trees. This also provides a way of passing state about the file
    to checks expecting that state. Any public attribute on this object can
    be requested by a plugin. The known public attributes are:

    - :attr:`blank_before`
    - :attr:`blank_lines`
    - :attr:`checker_state`
    - :attr:`indent_char`
    - :attr:`indent_level`
    - :attr:`line_number`
    - :attr:`logical_line`
    - :attr:`max_line_length`
    - :attr:`max_doc_length`
    - :attr:`multiline`
    - :attr:`noqa`
    - :attr:`previous_indent_level`
    - :attr:`previous_logical`
    - :attr:`previous_unindented_logical_line`
    - :attr:`tokens`
    - :attr:`file_tokens`
    - :attr:`total_lines`
    - :attr:`verbose`
    """

    #: always ``False``, included for compatibility
    noqa = False

    def __init__(
        self,
        filename: str,
        options: argparse.Namespace,
        lines: list[str] | None = None,
    ) -> None:
        """Initialize our file processor.

        :param filename: Name of the file to process
        """
        self.options = options
        self.filename = filename
        self.lines = lines if lines is not None else self.read_lines()
        self.strip_utf_bom()

        # Defaults for public attributes
        #: Number of preceding blank lines
        self.blank_before = 0
        #: Number of blank lines
        self.blank_lines = 0
        #: Checker states for each plugin?
        self._checker_states: dict[str, dict[Any, Any]] = {}
        #: Current checker state
        self.checker_state: dict[Any, Any] = {}
        #: User provided option for hang closing
        self.hang_closing = options.hang_closing
        #: Character used for indentation
        self.indent_char: str | None = None
        #: Current level of indentation
        self.indent_level = 0
        #: Number of spaces used for indentation
        self.indent_size = options.indent_size
        #: Line number in the file
        self.line_number = 0
        #: Current logical line
        self.logical_line = ""
        #: Maximum line length as configured by the user
        self.max_line_length = options.max_line_length
        #: Maximum docstring / comment line length as configured by the user
        self.max_doc_length = options.max_doc_length
        #: Whether the current physical line is multiline
        self.multiline = False
        #: Previous level of indentation
        self.previous_indent_level = 0
        #: Previous logical line
        self.previous_logical = ""
        #: Previous unindented (i.e. top-level) logical line
        self.previous_unindented_logical_line = ""
        #: Current set of tokens
        self.tokens: list[tokenize.TokenInfo] = []
        #: Total number of lines in the file
        self.total_lines = len(self.lines)
        #: Verbosity level of Flake8
        self.verbose = options.verbose
        #: Statistics dictionary
        self.statistics = {"logical lines": 0}
        self._fstring_start = self._tstring_start = -1

    @functools.cached_property
    def file_tokens(self) -> list[tokenize.TokenInfo]:
        """Return the complete set of tokens for a file."""
        line_iter = iter(self.lines)
        return list(tokenize.generate_tokens(lambda: next(line_iter)))

    def fstring_start(self, lineno: int) -> None:  # pragma: >=3.12 cover
        """Signal the beginning of an fstring."""
        self._fstring_start = lineno

    def tstring_start(self, lineno: int) -> None:  # pragma: >=3.14 cover
        """Signal the beginning of an tstring."""
        self._tstring_start = lineno

    def multiline_string(self, token: tokenize.TokenInfo) -> Generator[str]:
        """Iterate through the lines of a multiline string."""
        if token.type == FSTRING_END:  # pragma: >=3.12 cover
            start = self._fstring_start
        elif token.type == TSTRING_END:  # pragma: >=3.14 cover
            start = self._tstring_start
        else:
            start = token.start[0]

        self.multiline = True
        self.line_number = start
        # intentionally don't include the last line, that line will be
        # terminated later by a future end-of-line
        for _ in range(start, token.end[0]):
            yield self.lines[self.line_number - 1]
            self.line_number += 1
        self.multiline = False

    def reset_blank_before(self) -> None:
        """Reset the blank_before attribute to zero."""
        self.blank_before = 0

    def delete_first_token(self) -> None:
        """Delete the first token in the list of tokens."""
        del self.tokens[0]

    def visited_new_blank_line(self) -> None:
        """Note that we visited a new blank line."""
        self.blank_lines += 1

    def update_state(self, mapping: _LogicalMapping) -> None:
        """Update the indent level based on the logical line mapping."""
        (start_row, start_col) = mapping[0][1]
        start_line = self.lines[start_row - 1]
        self.indent_level = expand_indent(start_line[:start_col])
        if self.blank_before < self.blank_lines:
            self.blank_before = self.blank_lines

    def update_checker_state_for(self, plugin: LoadedPlugin) -> None:
        """Update the checker_state attribute for the plugin."""
        if "checker_state" in plugin.parameters:
            self.checker_state = self._checker_states.setdefault(
                plugin.entry_name, {},
            )

    def next_logical_line(self) -> None:
        """Record the previous logical line.

        This also resets the tokens list and the blank_lines count.
        """
        if self.logical_line:
            self.previous_indent_level = self.indent_level
            self.previous_logical = self.logical_line
            if not self.indent_level:
                self.previous_unindented_logical_line = self.logical_line
        self.blank_lines = 0
        self.tokens = []

    def build_logical_line_tokens(self) -> _Logical:  # noqa: C901
        """Build the mapping, comments, and logical line lists."""
        logical = []
        comments = []
        mapping: _LogicalMapping = []
        length = 0
        previous_row = previous_column = None
        for token_type, text, start, end, line in self.tokens:
            if token_type in SKIP_TOKENS:
                continue
            if not mapping:
                mapping = [(0, start)]
            if token_type == tokenize.COMMENT:
                comments.append(text)
                continue
            if token_type == tokenize.STRING:
                text = mutate_string(text)
            elif token_type in {
                FSTRING_MIDDLE,
                TSTRING_MIDDLE,
            }:  # pragma: >=3.12 cover  # noqa: E501
                # A curly brace in an FSTRING_MIDDLE token must be an escaped
                # curly brace. Both 'text' and 'end' will account for the
                # escaped version of the token (i.e. a single brace) rather
                # than the raw double brace version, so we must counteract this
                brace_offset = text.count("{") + text.count("}")
                text = "x" * (len(text) + brace_offset)
                end = (end[0], end[1] + brace_offset)
            if previous_row is not None and previous_column is not None:
                (start_row, start_column) = start
                if previous_row != start_row:
                    row_index = previous_row - 1
                    column_index = previous_column - 1
                    previous_text = self.lines[row_index][column_index]
                    if previous_text == "," or (
                        previous_text not in "{[(" and text not in "}])"
                    ):
                        text = f" {text}"
                elif previous_column != start_column:
                    text = line[previous_column:start_column] + text
            logical.append(text)
            length += len(text)
            mapping.append((length, end))
            (previous_row, previous_column) = end
        return comments, logical, mapping

    def build_ast(self) -> ast.AST:
        """Build an abstract syntax tree from the list of lines."""
        return ast.parse("".join(self.lines))

    def build_logical_line(self) -> tuple[str, str, _LogicalMapping]:
        """Build a logical line from the current tokens list."""
        comments, logical, mapping_list = self.build_logical_line_tokens()
        joined_comments = "".join(comments)
        self.logical_line = "".join(logical)
        self.statistics["logical lines"] += 1
        return joined_comments, self.logical_line, mapping_list

    def keyword_arguments_for(
        self,
        parameters: dict[str, bool],
        arguments: dict[str, Any],
    ) -> dict[str, Any]:
        """Generate the keyword arguments for a list of parameters."""
        ret = {}
        for param, required in parameters.items():
            if param in arguments:
                continue
            try:
                ret[param] = getattr(self, param)
            except AttributeError:
                if required:
                    raise
                else:
                    LOG.warning(
                        'Plugin requested optional parameter "%s" '
                        "but this is not an available parameter.",
                        param,
                    )
        return ret

    def generate_tokens(self) -> Generator[tokenize.TokenInfo]:
        """Tokenize the file and yield the tokens."""
        for token in tokenize.generate_tokens(self.next_line):
            if token[2][0] > self.total_lines:
                break
            self.tokens.append(token)
            yield token

    def _noqa_line_range(self, min_line: int, max_line: int) -> dict[int, str]:
        line_range = range(min_line, max_line + 1)
        joined = "".join(self.lines[min_line - 1: max_line])
        return dict.fromkeys(line_range, joined)

    @functools.cached_property
    def _noqa_line_mapping(self) -> dict[int, str]:
        """Map from line number to the line we'll search for `noqa` in."""
        try:
            file_tokens = self.file_tokens
        except (tokenize.TokenError, SyntaxError):
            # if we failed to parse the file tokens, we'll always fail in
            # the future, so set this so the code does not try again
            return {}
        else:
            ret = {}

            min_line = len(self.lines) + 2
            max_line = -1
            for tp, _, (s_line, _), (e_line, _), _ in file_tokens:
                if tp == tokenize.ENDMARKER or tp == tokenize.DEDENT:
                    continue

                min_line = min(min_line, s_line)
                max_line = max(max_line, e_line)

                if tp in (tokenize.NL, tokenize.NEWLINE):
                    ret.update(self._noqa_line_range(min_line, max_line))

                    min_line = len(self.lines) + 2
                    max_line = -1

            return ret

    def noqa_line_for(self, line_number: int) -> str | None:
        """Retrieve the line which will be used to determine noqa."""
        # NOTE(sigmavirus24): Some plugins choose to report errors for empty
        # files on Line 1. In those cases, we shouldn't bother trying to
        # retrieve a physical line (since none exist).
        return self._noqa_line_mapping.get(line_number)

    def next_line(self) -> str:
        """Get the next line from the list."""
        if self.line_number >= self.total_lines:
            return ""
        line = self.lines[self.line_number]
        self.line_number += 1
        if self.indent_char is None and line[:1] in defaults.WHITESPACE:
            self.indent_char = line[0]
        return line

    def read_lines(self) -> list[str]:
        """Read the lines for this file checker."""
        if self.filename == "-":
            self.filename = self.options.stdin_display_name or "stdin"
            lines = self.read_lines_from_stdin()
        else:
            lines = self.read_lines_from_filename()
        return lines

    def read_lines_from_filename(self) -> list[str]:
        """Read the lines for a file."""
        try:
            with tokenize.open(self.filename) as fd:
                return fd.readlines()
        except (SyntaxError, UnicodeError):
            # If we can't detect the codec with tokenize.detect_encoding, or
            # the detected encoding is incorrect, just fallback to latin-1.
            with open(self.filename, encoding="latin-1") as fd:
                return fd.readlines()

    def read_lines_from_stdin(self) -> list[str]:
        """Read the lines from standard in."""
        return utils.stdin_get_lines()

    def should_ignore_file(self) -> bool:
        """Check if ``flake8: noqa`` is in the file to be ignored.

        :returns:
            True if a line matches :attr:`defaults.NOQA_FILE`,
            otherwise False
        """
        if not self.options.disable_noqa and any(
            defaults.NOQA_FILE.match(line) for line in self.lines
        ):
            return True
        elif any(defaults.NOQA_FILE.search(line) for line in self.lines):
            LOG.warning(
                "Detected `flake8: noqa` on line with code. To ignore an "
                "error on a line use `noqa` instead.",
            )
            return False
        else:
            return False

    def strip_utf_bom(self) -> None:
        """Strip the UTF bom from the lines of the file."""
        if not self.lines:
            # If we have nothing to analyze quit early
            return

        # If the first byte of the file is a UTF-8 BOM, strip it
        if self.lines[0][:1] == "\uFEFF":
            self.lines[0] = self.lines[0][1:]
        elif self.lines[0][:3] == "\xEF\xBB\xBF":
            self.lines[0] = self.lines[0][3:]


def is_eol_token(token: tokenize.TokenInfo) -> bool:
    """Check if the token is an end-of-line token."""
    return token[0] in NEWLINE or token[4][token[3][1]:].lstrip() == "\\\n"


def is_multiline_string(token: tokenize.TokenInfo) -> bool:
    """Check if this is a multiline string."""
    return token.type in {FSTRING_END, TSTRING_END} or (
        token.type == tokenize.STRING and "\n" in token.string
    )


def token_is_newline(token: tokenize.TokenInfo) -> bool:
    """Check if the token type is a newline token type."""
    return token[0] in NEWLINE


def count_parentheses(current_parentheses_count: int, token_text: str) -> int:
    """Count the number of parentheses."""
    if token_text in "([{":  # nosec
        return current_parentheses_count + 1
    elif token_text in "}])":  # nosec
        return current_parentheses_count - 1
    return current_parentheses_count


def expand_indent(line: str) -> int:
    r"""Return the amount of indentation.

    Tabs are expanded to the next multiple of 8.

    >>> expand_indent('    ')
    4
    >>> expand_indent('\t')
    8
    >>> expand_indent('       \t')
    8
    >>> expand_indent('        \t')
    16
    """
    return len(line.expandtabs(8))


# NOTE(sigmavirus24): This was taken wholesale from
# https://github.com/PyCQA/pycodestyle. The in-line comments were edited to be
# more descriptive.
def mutate_string(text: str) -> str:
    """Replace contents with 'xxx' to prevent syntax matching.

    >>> mutate_string('"abc"')
    '"xxx"'
    >>> mutate_string("'''abc'''")
    "'''xxx'''"
    >>> mutate_string("r'abc'")
    "r'xxx'"
    """
    # NOTE(sigmavirus24): If there are string modifiers (e.g., b, u, r)
    # use the last "character" to determine if we're using single or double
    # quotes and then find the first instance of it
    start = text.index(text[-1]) + 1
    end = len(text) - 1
    # Check for triple-quoted strings
    if text[-3:] in ('"""', "'''"):
        start += 2
        end -= 2
    return text[:start] + "x" * (end - start) + text[end:]
```

## File: `src/flake8/statistics.py`
```python
"""Statistic collection logic for Flake8."""
from __future__ import annotations

from collections.abc import Generator
from typing import NamedTuple

from flake8.violation import Violation


class Statistics:
    """Manager of aggregated statistics for a run of Flake8."""

    def __init__(self) -> None:
        """Initialize the underlying dictionary for our statistics."""
        self._store: dict[Key, Statistic] = {}

    def error_codes(self) -> list[str]:
        """Return all unique error codes stored.

        :returns:
            Sorted list of error codes.
        """
        return sorted({key.code for key in self._store})

    def record(self, error: Violation) -> None:
        """Add the fact that the error was seen in the file.

        :param error:
            The Violation instance containing the information about the
            violation.
        """
        key = Key.create_from(error)
        if key not in self._store:
            self._store[key] = Statistic.create_from(error)
        self._store[key].increment()

    def statistics_for(
        self, prefix: str, filename: str | None = None,
    ) -> Generator[Statistic]:
        """Generate statistics for the prefix and filename.

        If you have a :class:`Statistics` object that has recorded errors,
        you can generate the statistics for a prefix (e.g., ``E``, ``E1``,
        ``W50``, ``W503``) with the optional filter of a filename as well.

        .. code-block:: python

            >>> stats = Statistics()
            >>> stats.statistics_for('E12',
                                     filename='src/flake8/statistics.py')
            <generator ...>
            >>> stats.statistics_for('W')
            <generator ...>

        :param prefix:
            The error class or specific error code to find statistics for.
        :param filename:
            (Optional) The filename to further filter results by.
        :returns:
            Generator of instances of :class:`Statistic`
        """
        matching_errors = sorted(
            key for key in self._store if key.matches(prefix, filename)
        )
        for error_code in matching_errors:
            yield self._store[error_code]


class Key(NamedTuple):
    """Simple key structure for the Statistics dictionary.

    To make things clearer, easier to read, and more understandable, we use a
    namedtuple here for all Keys in the underlying dictionary for the
    Statistics object.
    """

    filename: str
    code: str

    @classmethod
    def create_from(cls, error: Violation) -> Key:
        """Create a Key from :class:`flake8.violation.Violation`."""
        return cls(filename=error.filename, code=error.code)

    def matches(self, prefix: str, filename: str | None) -> bool:
        """Determine if this key matches some constraints.

        :param prefix:
            The error code prefix that this key's error code should start with.
        :param filename:
            The filename that we potentially want to match on. This can be
            None to only match on error prefix.
        :returns:
            True if the Key's code starts with the prefix and either filename
            is None, or the Key's filename matches the value passed in.
        """
        return self.code.startswith(prefix) and (
            filename is None or self.filename == filename
        )


class Statistic:
    """Simple wrapper around the logic of each statistic.

    Instead of maintaining a simple but potentially hard to reason about
    tuple, we create a class which has attributes and a couple
    convenience methods on it.
    """

    def __init__(
        self, error_code: str, filename: str, message: str, count: int,
    ) -> None:
        """Initialize our Statistic."""
        self.error_code = error_code
        self.filename = filename
        self.message = message
        self.count = count

    @classmethod
    def create_from(cls, error: Violation) -> Statistic:
        """Create a Statistic from a :class:`flake8.violation.Violation`."""
        return cls(
            error_code=error.code,
            filename=error.filename,
            message=error.text,
            count=0,
        )

    def increment(self) -> None:
        """Increment the number of times we've seen this error in this file."""
        self.count += 1
```

## File: `src/flake8/style_guide.py`
```python
"""Implementation of the StyleGuide used by Flake8."""
from __future__ import annotations

import argparse
import contextlib
import copy
import enum
import functools
import logging
from collections.abc import Generator
from collections.abc import Sequence

from flake8 import defaults
from flake8 import statistics
from flake8 import utils
from flake8.formatting import base as base_formatter
from flake8.violation import Violation

__all__ = ("StyleGuide",)

LOG = logging.getLogger(__name__)


class Selected(enum.Enum):
    """Enum representing an explicitly or implicitly selected code."""

    Explicitly = "explicitly selected"
    Implicitly = "implicitly selected"


class Ignored(enum.Enum):
    """Enum representing an explicitly or implicitly ignored code."""

    Explicitly = "explicitly ignored"
    Implicitly = "implicitly ignored"


class Decision(enum.Enum):
    """Enum representing whether a code should be ignored or selected."""

    Ignored = "ignored error"
    Selected = "selected error"


def _explicitly_chosen(
    *,
    option: list[str] | None,
    extend: list[str] | None,
) -> tuple[str, ...]:
    ret = [*(option or []), *(extend or [])]
    return tuple(sorted(ret, reverse=True))


def _select_ignore(
    *,
    option: list[str] | None,
    default: tuple[str, ...],
    extended_default: list[str],
    extend: list[str] | None,
) -> tuple[str, ...]:
    # option was explicitly set, ignore the default and extended default
    if option is not None:
        ret = [*option, *(extend or [])]
    else:
        ret = [*default, *extended_default, *(extend or [])]
    return tuple(sorted(ret, reverse=True))


class DecisionEngine:
    """A class for managing the decision process around violations.

    This contains the logic for whether a violation should be reported or
    ignored.
    """

    def __init__(self, options: argparse.Namespace) -> None:
        """Initialize the engine."""
        self.cache: dict[str, Decision] = {}

        self.selected_explicitly = _explicitly_chosen(
            option=options.select,
            extend=options.extend_select,
        )
        self.ignored_explicitly = _explicitly_chosen(
            option=options.ignore,
            extend=options.extend_ignore,
        )

        self.selected = _select_ignore(
            option=options.select,
            default=(),
            extended_default=options.extended_default_select,
            extend=options.extend_select,
        )
        self.ignored = _select_ignore(
            option=options.ignore,
            default=defaults.IGNORE,
            extended_default=options.extended_default_ignore,
            extend=options.extend_ignore,
        )

    def was_selected(self, code: str) -> Selected | Ignored:
        """Determine if the code has been selected by the user.

        :param code: The code for the check that has been run.
        :returns:
            Selected.Implicitly if the selected list is empty,
            Selected.Explicitly if the selected list is not empty and a match
            was found,
            Ignored.Implicitly if the selected list is not empty but no match
            was found.
        """
        if code.startswith(self.selected_explicitly):
            return Selected.Explicitly
        elif code.startswith(self.selected):
            return Selected.Implicitly
        else:
            return Ignored.Implicitly

    def was_ignored(self, code: str) -> Selected | Ignored:
        """Determine if the code has been ignored by the user.

        :param code:
            The code for the check that has been run.
        :returns:
            Selected.Implicitly if the ignored list is empty,
            Ignored.Explicitly if the ignored list is not empty and a match was
            found,
            Selected.Implicitly if the ignored list is not empty but no match
            was found.
        """
        if code.startswith(self.ignored_explicitly):
            return Ignored.Explicitly
        elif code.startswith(self.ignored):
            return Ignored.Implicitly
        else:
            return Selected.Implicitly

    def make_decision(self, code: str) -> Decision:
        """Decide if code should be ignored or selected."""
        selected = self.was_selected(code)
        ignored = self.was_ignored(code)
        LOG.debug(
            "The user configured %r to be %r, %r",
            code,
            selected,
            ignored,
        )

        if isinstance(selected, Selected) and isinstance(ignored, Selected):
            return Decision.Selected
        elif isinstance(selected, Ignored) and isinstance(ignored, Ignored):
            return Decision.Ignored
        elif (
            selected is Selected.Explicitly
            and ignored is not Ignored.Explicitly
        ):
            return Decision.Selected
        elif (
            selected is not Selected.Explicitly
            and ignored is Ignored.Explicitly
        ):
            return Decision.Ignored
        elif selected is Ignored.Implicitly and ignored is Selected.Implicitly:
            return Decision.Ignored
        elif (
            selected is Selected.Explicitly and ignored is Ignored.Explicitly
        ) or (
            selected is Selected.Implicitly and ignored is Ignored.Implicitly
        ):
            # we only get here if it was in both lists: longest prefix wins
            select = next(s for s in self.selected if code.startswith(s))
            ignore = next(s for s in self.ignored if code.startswith(s))
            if len(select) > len(ignore):
                return Decision.Selected
            else:
                return Decision.Ignored
        else:
            raise AssertionError(f"unreachable {code} {selected} {ignored}")

    def decision_for(self, code: str) -> Decision:
        """Return the decision for a specific code.

        This method caches the decisions for codes to avoid retracing the same
        logic over and over again. We only care about the select and ignore
        rules as specified by the user in their configuration files and
        command-line flags.

        This method does not look at whether the specific line is being
        ignored in the file itself.

        :param code: The code for the check that has been run.
        """
        decision = self.cache.get(code)
        if decision is None:
            decision = self.make_decision(code)
            self.cache[code] = decision
            LOG.debug('"%s" will be "%s"', code, decision)
        return decision


class StyleGuideManager:
    """Manage multiple style guides for a single run."""

    def __init__(
        self,
        options: argparse.Namespace,
        formatter: base_formatter.BaseFormatter,
        decider: DecisionEngine | None = None,
    ) -> None:
        """Initialize our StyleGuide.

        .. todo:: Add parameter documentation.
        """
        self.options = options
        self.formatter = formatter
        self.stats = statistics.Statistics()
        self.decider = decider or DecisionEngine(options)
        self.style_guides: list[StyleGuide] = []
        self.default_style_guide = StyleGuide(
            options, formatter, self.stats, decider=decider,
        )
        self.style_guides = [
            self.default_style_guide,
            *self.populate_style_guides_with(options),
        ]

        self.style_guide_for = functools.cache(self._style_guide_for)

    def populate_style_guides_with(
        self, options: argparse.Namespace,
    ) -> Generator[StyleGuide]:
        """Generate style guides from the per-file-ignores option.

        :param options:
            The original options parsed from the CLI and config file.
        :returns:
            A copy of the default style guide with overridden values.
        """
        per_file = utils.parse_files_to_codes_mapping(options.per_file_ignores)
        for filename, violations in per_file:
            yield self.default_style_guide.copy(
                filename=filename, extend_ignore_with=violations,
            )

    def _style_guide_for(self, filename: str) -> StyleGuide:
        """Find the StyleGuide for the filename in particular."""
        return max(
            (g for g in self.style_guides if g.applies_to(filename)),
            key=lambda g: len(g.filename or ""),
        )

    @contextlib.contextmanager
    def processing_file(self, filename: str) -> Generator[StyleGuide]:
        """Record the fact that we're processing the file's results."""
        guide = self.style_guide_for(filename)
        with guide.processing_file(filename):
            yield guide

    def handle_error(
        self,
        code: str,
        filename: str,
        line_number: int,
        column_number: int,
        text: str,
        physical_line: str | None = None,
    ) -> int:
        """Handle an error reported by a check.

        :param code:
            The error code found, e.g., E123.
        :param filename:
            The file in which the error was found.
        :param line_number:
            The line number (where counting starts at 1) at which the error
            occurs.
        :param column_number:
            The column number (where counting starts at 1) at which the error
            occurs.
        :param text:
            The text of the error message.
        :param physical_line:
            The actual physical line causing the error.
        :returns:
            1 if the error was reported. 0 if it was ignored. This is to allow
            for counting of the number of errors found that were not ignored.
        """
        guide = self.style_guide_for(filename)
        return guide.handle_error(
            code, filename, line_number, column_number, text, physical_line,
        )


class StyleGuide:
    """Manage a Flake8 user's style guide."""

    def __init__(
        self,
        options: argparse.Namespace,
        formatter: base_formatter.BaseFormatter,
        stats: statistics.Statistics,
        filename: str | None = None,
        decider: DecisionEngine | None = None,
    ):
        """Initialize our StyleGuide.

        .. todo:: Add parameter documentation.
        """
        self.options = options
        self.formatter = formatter
        self.stats = stats
        self.decider = decider or DecisionEngine(options)
        self.filename = filename
        if self.filename:
            self.filename = utils.normalize_path(self.filename)

    def __repr__(self) -> str:
        """Make it easier to debug which StyleGuide we're using."""
        return f"<StyleGuide [{self.filename}]>"

    def copy(
        self,
        filename: str | None = None,
        extend_ignore_with: Sequence[str] | None = None,
    ) -> StyleGuide:
        """Create a copy of this style guide with different values."""
        filename = filename or self.filename
        options = copy.deepcopy(self.options)
        options.extend_ignore = options.extend_ignore or []
        options.extend_ignore.extend(extend_ignore_with or [])
        return StyleGuide(
            options, self.formatter, self.stats, filename=filename,
        )

    @contextlib.contextmanager
    def processing_file(self, filename: str) -> Generator[StyleGuide]:
        """Record the fact that we're processing the file's results."""
        self.formatter.beginning(filename)
        yield self
        self.formatter.finished(filename)

    def applies_to(self, filename: str) -> bool:
        """Check if this StyleGuide applies to the file.

        :param filename:
            The name of the file with violations that we're potentially
            applying this StyleGuide to.
        :returns:
            True if this applies, False otherwise
        """
        if self.filename is None:
            return True
        return utils.matches_filename(
            filename,
            patterns=[self.filename],
            log_message=f'{self!r} does %(whether)smatch "%(path)s"',
            logger=LOG,
        )

    def should_report_error(self, code: str) -> Decision:
        """Determine if the error code should be reported or ignored.

        This method only cares about the select and ignore rules as specified
        by the user in their configuration files and command-line flags.

        This method does not look at whether the specific line is being
        ignored in the file itself.

        :param code:
            The code for the check that has been run.
        """
        return self.decider.decision_for(code)

    def handle_error(
        self,
        code: str,
        filename: str,
        line_number: int,
        column_number: int,
        text: str,
        physical_line: str | None = None,
    ) -> int:
        """Handle an error reported by a check.

        :param code:
            The error code found, e.g., E123.
        :param filename:
            The file in which the error was found.
        :param line_number:
            The line number (where counting starts at 1) at which the error
            occurs.
        :param column_number:
            The column number (where counting starts at 1) at which the error
            occurs.
        :param text:
            The text of the error message.
        :param physical_line:
            The actual physical line causing the error.
        :returns:
            1 if the error was reported. 0 if it was ignored. This is to allow
            for counting of the number of errors found that were not ignored.
        """
        disable_noqa = self.options.disable_noqa
        # NOTE(sigmavirus24): Apparently we're provided with 0-indexed column
        # numbers so we have to offset that here.
        if not column_number:
            column_number = 0
        error = Violation(
            code,
            filename,
            line_number,
            column_number + 1,
            text,
            physical_line,
        )
        error_is_selected = (
            self.should_report_error(error.code) is Decision.Selected
        )
        is_not_inline_ignored = error.is_inline_ignored(disable_noqa) is False
        if error_is_selected and is_not_inline_ignored:
            self.formatter.handle(error)
            self.stats.record(error)
            return 1
        return 0
```

## File: `src/flake8/utils.py`
```python
"""Utility methods for flake8."""
from __future__ import annotations

import fnmatch as _fnmatch
import functools
import io
import logging
import os
import platform
import re
import sys
import textwrap
import tokenize
from collections.abc import Sequence
from re import Pattern
from typing import NamedTuple

from flake8 import exceptions

COMMA_SEPARATED_LIST_RE = re.compile(r"[,\s]")
LOCAL_PLUGIN_LIST_RE = re.compile(r"[,\t\n\r\f\v]")
NORMALIZE_PACKAGE_NAME_RE = re.compile(r"[-_.]+")


def parse_comma_separated_list(
    value: str, regexp: Pattern[str] = COMMA_SEPARATED_LIST_RE,
) -> list[str]:
    """Parse a comma-separated list.

    :param value:
        String to be parsed and normalized.
    :param regexp:
        Compiled regular expression used to split the value when it is a
        string.
    :returns:
        List of values with whitespace stripped.
    """
    assert isinstance(value, str), value

    separated = regexp.split(value)
    item_gen = (item.strip() for item in separated)
    return [item for item in item_gen if item]


class _Token(NamedTuple):
    tp: str
    src: str


_CODE, _FILE, _COLON, _COMMA, _WS = "code", "file", "colon", "comma", "ws"
_EOF = "eof"
_FILE_LIST_TOKEN_TYPES = [
    (re.compile(r"[A-Z]+[0-9]*(?=$|\s|,)"), _CODE),
    (re.compile(r"[^\s:,]+"), _FILE),
    (re.compile(r"\s*:\s*"), _COLON),
    (re.compile(r"\s*,\s*"), _COMMA),
    (re.compile(r"\s+"), _WS),
]


def _tokenize_files_to_codes_mapping(value: str) -> list[_Token]:
    tokens = []
    i = 0
    while i < len(value):
        for token_re, token_name in _FILE_LIST_TOKEN_TYPES:
            match = token_re.match(value, i)
            if match:
                tokens.append(_Token(token_name, match.group().strip()))
                i = match.end()
                break
        else:
            raise AssertionError("unreachable", value, i)
    tokens.append(_Token(_EOF, ""))

    return tokens


def parse_files_to_codes_mapping(  # noqa: C901
    value_: Sequence[str] | str,
) -> list[tuple[str, list[str]]]:
    """Parse a files-to-codes mapping.

    A files-to-codes mapping a sequence of values specified as
    `filenames list:codes list ...`.  Each of the lists may be separated by
    either comma or whitespace tokens.

    :param value: String to be parsed and normalized.
    """
    if not isinstance(value_, str):
        value = "\n".join(value_)
    else:
        value = value_

    ret: list[tuple[str, list[str]]] = []
    if not value.strip():
        return ret

    class State:
        seen_sep = True
        seen_colon = False
        filenames: list[str] = []
        codes: list[str] = []

    def _reset() -> None:
        if State.codes:
            for filename in State.filenames:
                ret.append((filename, State.codes))
        State.seen_sep = True
        State.seen_colon = False
        State.filenames = []
        State.codes = []

    def _unexpected_token() -> exceptions.ExecutionError:
        return exceptions.ExecutionError(
            f"Expected `per-file-ignores` to be a mapping from file exclude "
            f"patterns to ignore codes.\n\n"
            f"Configured `per-file-ignores` setting:\n\n"
            f"{textwrap.indent(value.strip(), '    ')}",
        )

    for token in _tokenize_files_to_codes_mapping(value):
        # legal in any state: separator sets the sep bit
        if token.tp in {_COMMA, _WS}:
            State.seen_sep = True
        # looking for filenames
        elif not State.seen_colon:
            if token.tp == _COLON:
                State.seen_colon = True
                State.seen_sep = True
            elif State.seen_sep and token.tp == _FILE:
                State.filenames.append(token.src)
                State.seen_sep = False
            else:
                raise _unexpected_token()
        # looking for codes
        else:
            if token.tp == _EOF:
                _reset()
            elif State.seen_sep and token.tp == _CODE:
                State.codes.append(token.src)
                State.seen_sep = False
            elif State.seen_sep and token.tp == _FILE:
                _reset()
                State.filenames.append(token.src)
                State.seen_sep = False
            else:
                raise _unexpected_token()

    return ret


def normalize_paths(
    paths: Sequence[str], parent: str = os.curdir,
) -> list[str]:
    """Normalize a list of paths relative to a parent directory.

    :returns:
        The normalized paths.
    """
    assert isinstance(paths, list), paths
    return [normalize_path(p, parent) for p in paths]


def normalize_path(path: str, parent: str = os.curdir) -> str:
    """Normalize a single-path.

    :returns:
        The normalized path.
    """
    # NOTE(sigmavirus24): Using os.path.sep and os.path.altsep allow for
    # Windows compatibility with both Windows-style paths (c:\foo\bar) and
    # Unix style paths (/foo/bar).
    separator = os.path.sep
    # NOTE(sigmavirus24): os.path.altsep may be None
    alternate_separator = os.path.altsep or ""
    if (
        path == "."
        or separator in path
        or (alternate_separator and alternate_separator in path)
    ):
        path = os.path.abspath(os.path.join(parent, path))
    return path.rstrip(separator + alternate_separator)


@functools.lru_cache(maxsize=1)
def stdin_get_value() -> str:
    """Get and cache it so plugins can use it."""
    stdin_value = sys.stdin.buffer.read()
    fd = io.BytesIO(stdin_value)
    try:
        coding, _ = tokenize.detect_encoding(fd.readline)
        fd.seek(0)
        return io.TextIOWrapper(fd, coding).read()
    except (LookupError, SyntaxError, UnicodeError):
        return stdin_value.decode("utf-8")


def stdin_get_lines() -> list[str]:
    """Return lines of stdin split according to file splitting."""
    return list(io.StringIO(stdin_get_value()))


def is_using_stdin(paths: list[str]) -> bool:
    """Determine if we're going to read from stdin.

    :param paths:
        The paths that we're going to check.
    :returns:
        True if stdin (-) is in the path, otherwise False
    """
    return "-" in paths


def fnmatch(filename: str, patterns: Sequence[str]) -> bool:
    """Wrap :func:`fnmatch.fnmatch` to add some functionality.

    :param filename:
        Name of the file we're trying to match.
    :param patterns:
        Patterns we're using to try to match the filename.
    :param default:
        The default value if patterns is empty
    :returns:
        True if a pattern matches the filename, False if it doesn't.
        ``True`` if patterns is empty.
    """
    if not patterns:
        return True
    return any(_fnmatch.fnmatch(filename, pattern) for pattern in patterns)


def matches_filename(
    path: str,
    patterns: Sequence[str],
    log_message: str,
    logger: logging.Logger,
) -> bool:
    """Use fnmatch to discern if a path exists in patterns.

    :param path:
        The path to the file under question
    :param patterns:
        The patterns to match the path against.
    :param log_message:
        The message used for logging purposes.
    :returns:
        True if path matches patterns, False otherwise
    """
    if not patterns:
        return False
    basename = os.path.basename(path)
    if basename not in {".", ".."} and fnmatch(basename, patterns):
        logger.debug(log_message, {"path": basename, "whether": ""})
        return True

    absolute_path = os.path.abspath(path)
    match = fnmatch(absolute_path, patterns)
    logger.debug(
        log_message,
        {"path": absolute_path, "whether": "" if match else "not "},
    )
    return match


def get_python_version() -> str:
    """Find and format the python implementation and version.

    :returns:
        Implementation name, version, and platform as a string.
    """
    return "{} {} on {}".format(
        platform.python_implementation(),
        platform.python_version(),
        platform.system(),
    )


def normalize_pypi_name(s: str) -> str:
    """Normalize a distribution name according to PEP 503."""
    return NORMALIZE_PACKAGE_NAME_RE.sub("-", s).lower()
```

## File: `src/flake8/violation.py`
```python
"""Contains the Violation error class used internally."""
from __future__ import annotations

import functools
import linecache
import logging
from re import Match
from typing import NamedTuple

from flake8 import defaults
from flake8 import utils


LOG = logging.getLogger(__name__)


@functools.lru_cache(maxsize=512)
def _find_noqa(physical_line: str) -> Match[str] | None:
    return defaults.NOQA_INLINE_REGEXP.search(physical_line)


class Violation(NamedTuple):
    """Class representing a violation reported by Flake8."""

    code: str
    filename: str
    line_number: int
    column_number: int
    text: str
    physical_line: str | None

    def is_inline_ignored(self, disable_noqa: bool) -> bool:
        """Determine if a comment has been added to ignore this line.

        :param disable_noqa:
            Whether or not users have provided ``--disable-noqa``.
        :returns:
            True if error is ignored in-line, False otherwise.
        """
        physical_line = self.physical_line
        # TODO(sigmavirus24): Determine how to handle stdin with linecache
        if disable_noqa:
            return False

        if physical_line is None:
            physical_line = linecache.getline(self.filename, self.line_number)
        noqa_match = _find_noqa(physical_line)
        if noqa_match is None:
            LOG.debug("%r is not inline ignored", self)
            return False

        codes_str = noqa_match.groupdict()["codes"]
        if codes_str is None:
            LOG.debug("%r is ignored by a blanket ``# noqa``", self)
            return True

        codes = set(utils.parse_comma_separated_list(codes_str))
        if self.code in codes or self.code.startswith(tuple(codes)):
            LOG.debug(
                "%r is ignored specifically inline with ``# noqa: %s``",
                self,
                codes_str,
            )
            return True

        LOG.debug(
            "%r is not ignored inline with ``# noqa: %s``", self, codes_str,
        )
        return False
```

## File: `src/flake8/api/__init__.py`
```python
"""Module containing all public entry-points for Flake8.

This is the only submodule in Flake8 with a guaranteed stable API. All other
submodules are considered internal only and are subject to change.
"""
from __future__ import annotations
```

## File: `src/flake8/api/legacy.py`
```python
"""Module containing shims around Flake8 2.x behaviour.

Previously, users would import :func:`get_style_guide` from ``flake8.engine``.
In 3.0 we no longer have an "engine" module but we maintain the API from it.
"""
from __future__ import annotations

import argparse
import logging
import os.path
from typing import Any

from flake8.discover_files import expand_paths
from flake8.formatting import base as formatter
from flake8.main import application as app
from flake8.options.parse_args import parse_args

LOG = logging.getLogger(__name__)


__all__ = ("get_style_guide",)


class Report:
    """Public facing object that mimic's Flake8 2.0's API.

    .. note::

        There are important changes in how this object behaves compared to
        the object provided in Flake8 2.x.

    .. warning::

        This should not be instantiated by users.

    .. versionchanged:: 3.0.0
    """

    def __init__(self, application: app.Application) -> None:
        """Initialize the Report for the user.

        .. warning:: This should not be instantiated by users.
        """
        assert application.guide is not None
        self._application = application
        self._style_guide = application.guide
        self._stats = self._style_guide.stats

    @property
    def total_errors(self) -> int:
        """Return the total number of errors."""
        return self._application.result_count

    def get_statistics(self, violation: str) -> list[str]:
        """Get the list of occurrences of a violation.

        :returns:
            List of occurrences of a violation formatted as:
            {Count} {Error Code} {Message}, e.g.,
            ``8 E531 Some error message about the error``
        """
        return [
            f"{s.count} {s.error_code} {s.message}"
            for s in self._stats.statistics_for(violation)
        ]


class StyleGuide:
    """Public facing object that mimic's Flake8 2.0's StyleGuide.

    .. note::

        There are important changes in how this object behaves compared to
        the StyleGuide object provided in Flake8 2.x.

    .. warning::

        This object should not be instantiated directly by users.

    .. versionchanged:: 3.0.0
    """

    def __init__(self, application: app.Application) -> None:
        """Initialize our StyleGuide."""
        self._application = application
        self._file_checker_manager = application.file_checker_manager

    @property
    def options(self) -> argparse.Namespace:
        """Return application's options.

        An instance of :class:`argparse.Namespace` containing parsed options.
        """
        assert self._application.options is not None
        return self._application.options

    @property
    def paths(self) -> list[str]:
        """Return the extra arguments passed as paths."""
        assert self._application.options is not None
        return self._application.options.filenames

    def check_files(self, paths: list[str] | None = None) -> Report:
        """Run collected checks on the files provided.

        This will check the files passed in and return a :class:`Report`
        instance.

        :param paths:
            List of filenames (or paths) to check.
        :returns:
            Object that mimic's Flake8 2.0's Reporter class.
        """
        assert self._application.options is not None
        self._application.options.filenames = paths
        self._application.run_checks()
        self._application.report_errors()
        return Report(self._application)

    def excluded(self, filename: str, parent: str | None = None) -> bool:
        """Determine if a file is excluded.

        :param filename:
            Path to the file to check if it is excluded.
        :param parent:
            Name of the parent directory containing the file.
        :returns:
            True if the filename is excluded, False otherwise.
        """

        def excluded(path: str) -> bool:
            paths = tuple(
                expand_paths(
                    paths=[path],
                    stdin_display_name=self.options.stdin_display_name,
                    filename_patterns=self.options.filename,
                    exclude=self.options.exclude,
                ),
            )
            return not paths

        return excluded(filename) or (
            parent is not None and excluded(os.path.join(parent, filename))
        )

    def init_report(
        self,
        reporter: type[formatter.BaseFormatter] | None = None,
    ) -> None:
        """Set up a formatter for this run of Flake8."""
        if reporter is None:
            return
        if not issubclass(reporter, formatter.BaseFormatter):
            raise ValueError(
                "Report should be subclass of "
                "flake8.formatter.BaseFormatter.",
            )
        self._application.formatter = reporter(self.options)
        self._application.guide = None
        # NOTE(sigmavirus24): This isn't the intended use of
        # Application#make_guide but it works pretty well.
        # Stop cringing... I know it's gross.
        self._application.make_guide()
        self._application.file_checker_manager = None
        self._application.make_file_checker_manager([])

    def input_file(
        self,
        filename: str,
        lines: Any | None = None,
        expected: Any | None = None,
        line_offset: Any | None = 0,
    ) -> Report:
        """Run collected checks on a single file.

        This will check the file passed in and return a :class:`Report`
        instance.

        :param filename:
            The path to the file to check.
        :param lines:
            Ignored since Flake8 3.0.
        :param expected:
            Ignored since Flake8 3.0.
        :param line_offset:
            Ignored since Flake8 3.0.
        :returns:
            Object that mimic's Flake8 2.0's Reporter class.
        """
        return self.check_files([filename])


def get_style_guide(**kwargs: Any) -> StyleGuide:
    r"""Provision a StyleGuide for use.

    :param \*\*kwargs:
        Keyword arguments that provide some options for the StyleGuide.
    :returns:
        An initialized StyleGuide
    """
    application = app.Application()
    application.plugins, application.options = parse_args([])
    # We basically want application.initialize to be called but with these
    # options set instead before we make our formatter, notifier, internal
    # style guide and file checker manager.
    options = application.options
    for key, value in kwargs.items():
        try:
            getattr(options, key)
            setattr(options, key, value)
        except AttributeError:
            LOG.error('Could not update option "%s"', key)
    application.make_formatter()
    application.make_guide()
    application.make_file_checker_manager([])
    return StyleGuide(application)
```

## File: `src/flake8/formatting/__init__.py`
```python
"""Submodule containing the default formatters for Flake8."""
from __future__ import annotations
```

## File: `src/flake8/formatting/_windows_color.py`
```python
"""ctypes hackery to enable color processing on windows.

See: https://github.com/pre-commit/pre-commit/blob/cb40e96/pre_commit/color.py
"""
from __future__ import annotations

import sys

if sys.platform == "win32":  # pragma: no cover (windows)

    def _enable() -> None:
        from ctypes import POINTER
        from ctypes import windll
        from ctypes import WinError
        from ctypes import WINFUNCTYPE
        from ctypes.wintypes import BOOL
        from ctypes.wintypes import DWORD
        from ctypes.wintypes import HANDLE

        STD_ERROR_HANDLE = -12
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 4

        def bool_errcheck(result, func, args):
            if not result:
                raise WinError()
            return args

        GetStdHandle = WINFUNCTYPE(HANDLE, DWORD)(
            ("GetStdHandle", windll.kernel32),
            ((1, "nStdHandle"),),
        )

        GetConsoleMode = WINFUNCTYPE(BOOL, HANDLE, POINTER(DWORD))(
            ("GetConsoleMode", windll.kernel32),
            ((1, "hConsoleHandle"), (2, "lpMode")),
        )
        GetConsoleMode.errcheck = bool_errcheck

        SetConsoleMode = WINFUNCTYPE(BOOL, HANDLE, DWORD)(
            ("SetConsoleMode", windll.kernel32),
            ((1, "hConsoleHandle"), (1, "dwMode")),
        )
        SetConsoleMode.errcheck = bool_errcheck

        # As of Windows 10, the Windows console supports (some) ANSI escape
        # sequences, but it needs to be enabled using `SetConsoleMode` first.
        #
        # More info on the escape sequences supported:
        # https://msdn.microsoft.com/en-us/library/windows/desktop/mt638032(v=vs.85).aspx
        stderr = GetStdHandle(STD_ERROR_HANDLE)
        flags = GetConsoleMode(stderr)
        SetConsoleMode(stderr, flags | ENABLE_VIRTUAL_TERMINAL_PROCESSING)

    try:
        _enable()
    except OSError:
        terminal_supports_color = False
    else:
        terminal_supports_color = True
else:  # pragma: win32 no cover
    terminal_supports_color = True
```

## File: `src/flake8/formatting/base.py`
```python
"""The base class and interface for all formatting plugins."""
from __future__ import annotations

import argparse
import os
import sys
from typing import IO

from flake8.formatting import _windows_color
from flake8.statistics import Statistics
from flake8.violation import Violation


class BaseFormatter:
    """Class defining the formatter interface.

    .. attribute:: options

        The options parsed from both configuration files and the command-line.

    .. attribute:: filename

        If specified by the user, the path to store the results of the run.

    .. attribute:: output_fd

        Initialized when the :meth:`start` is called. This will be a file
        object opened for writing.

    .. attribute:: newline

        The string to add to the end of a line. This is only used when the
        output filename has been specified.
    """

    def __init__(self, options: argparse.Namespace) -> None:
        """Initialize with the options parsed from config and cli.

        This also calls a hook, :meth:`after_init`, so subclasses do not need
        to call super to call this method.

        :param options:
            User specified configuration parsed from both configuration files
            and the command-line interface.
        """
        self.options = options
        self.filename = options.output_file
        self.output_fd: IO[str] | None = None
        self.newline = "\n"
        self.color = options.color == "always" or (
            options.color == "auto"
            and sys.stdout.isatty()
            and _windows_color.terminal_supports_color
        )
        self.after_init()

    def after_init(self) -> None:
        """Initialize the formatter further."""

    def beginning(self, filename: str) -> None:
        """Notify the formatter that we're starting to process a file.

        :param filename:
            The name of the file that Flake8 is beginning to report results
            from.
        """

    def finished(self, filename: str) -> None:
        """Notify the formatter that we've finished processing a file.

        :param filename:
            The name of the file that Flake8 has finished reporting results
            from.
        """

    def start(self) -> None:
        """Prepare the formatter to receive input.

        This defaults to initializing :attr:`output_fd` if :attr:`filename`
        """
        if self.filename:
            dirname = os.path.dirname(os.path.abspath(self.filename))
            os.makedirs(dirname, exist_ok=True)
            self.output_fd = open(self.filename, "a")

    def handle(self, error: Violation) -> None:
        """Handle an error reported by Flake8.

        This defaults to calling :meth:`format`, :meth:`show_source`, and
        then :meth:`write`. To extend how errors are handled, override this
        method.

        :param error:
            This will be an instance of
            :class:`~flake8.violation.Violation`.
        """
        line = self.format(error)
        source = self.show_source(error)
        self.write(line, source)

    def format(self, error: Violation) -> str | None:
        """Format an error reported by Flake8.

        This method **must** be implemented by subclasses.

        :param error:
            This will be an instance of
            :class:`~flake8.violation.Violation`.
        :returns:
            The formatted error string.
        """
        raise NotImplementedError(
            "Subclass of BaseFormatter did not implement" " format.",
        )

    def show_statistics(self, statistics: Statistics) -> None:
        """Format and print the statistics."""
        for error_code in statistics.error_codes():
            stats_for_error_code = statistics.statistics_for(error_code)
            statistic = next(stats_for_error_code)
            count = statistic.count
            count += sum(stat.count for stat in stats_for_error_code)
            self._write(f"{count:<5} {error_code} {statistic.message}")

    def show_benchmarks(self, benchmarks: list[tuple[str, float]]) -> None:
        """Format and print the benchmarks."""
        # NOTE(sigmavirus24): The format strings are a little confusing, even
        # to me, so here's a quick explanation:
        # We specify the named value first followed by a ':' to indicate we're
        # formatting the value.
        # Next we use '<' to indicate we want the value left aligned.
        # Then '10' is the width of the area.
        # For floats, finally, we only want only want at most 3 digits after
        # the decimal point to be displayed. This is the precision and it
        # can not be specified for integers which is why we need two separate
        # format strings.
        float_format = "{value:<10.3} {statistic}".format
        int_format = "{value:<10} {statistic}".format
        for statistic, value in benchmarks:
            if isinstance(value, int):
                benchmark = int_format(statistic=statistic, value=value)
            else:
                benchmark = float_format(statistic=statistic, value=value)
            self._write(benchmark)

    def show_source(self, error: Violation) -> str | None:
        """Show the physical line generating the error.

        This also adds an indicator for the particular part of the line that
        is reported as generating the problem.

        :param error:
            This will be an instance of
            :class:`~flake8.violation.Violation`.
        :returns:
            The formatted error string if the user wants to show the source.
            If the user does not want to show the source, this will return
            ``None``.
        """
        if not self.options.show_source or error.physical_line is None:
            return ""

        # Because column numbers are 1-indexed, we need to remove one to get
        # the proper number of space characters.
        indent = "".join(
            c if c.isspace() else " "
            for c in error.physical_line[: error.column_number - 1]
        )
        # Physical lines have a newline at the end, no need to add an extra
        # one
        return f"{error.physical_line}{indent}^"

    def _write(self, output: str) -> None:
        """Handle logic of whether to use an output file or print()."""
        if self.output_fd is not None:
            self.output_fd.write(output + self.newline)
        if self.output_fd is None or self.options.tee:
            sys.stdout.buffer.write(output.encode() + self.newline.encode())

    def write(self, line: str | None, source: str | None) -> None:
        """Write the line either to the output file or stdout.

        This handles deciding whether to write to a file or print to standard
        out for subclasses. Override this if you want behaviour that differs
        from the default.

        :param line:
            The formatted string to print or write.
        :param source:
            The source code that has been formatted and associated with the
            line of output.
        """
        if line:
            self._write(line)
        if source:
            self._write(source)

    def stop(self) -> None:
        """Clean up after reporting is finished."""
        if self.output_fd is not None:
            self.output_fd.close()
            self.output_fd = None
```

## File: `src/flake8/formatting/default.py`
```python
"""Default formatting class for Flake8."""
from __future__ import annotations

from flake8.formatting import base
from flake8.violation import Violation

COLORS = {
    "bold": "\033[1m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[m",
}
COLORS_OFF = {k: "" for k in COLORS}


class SimpleFormatter(base.BaseFormatter):
    """Simple abstraction for Default and Pylint formatter commonality.

    Sub-classes of this need to define an ``error_format`` attribute in order
    to succeed. The ``format`` method relies on that attribute and expects the
    ``error_format`` string to use the old-style formatting strings with named
    parameters:

    * code
    * text
    * path
    * row
    * col

    """

    error_format: str

    def format(self, error: Violation) -> str | None:
        """Format and write error out.

        If an output filename is specified, write formatted errors to that
        file. Otherwise, print the formatted error to standard out.
        """
        return self.error_format % {
            "code": error.code,
            "text": error.text,
            "path": error.filename,
            "row": error.line_number,
            "col": error.column_number,
            **(COLORS if self.color else COLORS_OFF),
        }


class Default(SimpleFormatter):
    """Default formatter for Flake8.

    This also handles backwards compatibility for people specifying a custom
    format string.
    """

    error_format = (
        "%(bold)s%(path)s%(reset)s"
        "%(cyan)s:%(reset)s%(row)d%(cyan)s:%(reset)s%(col)d%(cyan)s:%(reset)s "
        "%(bold)s%(red)s%(code)s%(reset)s %(text)s"
    )

    def after_init(self) -> None:
        """Check for a custom format string."""
        if self.options.format.lower() != "default":
            self.error_format = self.options.format


class Pylint(SimpleFormatter):
    """Pylint formatter for Flake8."""

    error_format = "%(path)s:%(row)d: [%(code)s] %(text)s"


class FilenameOnly(SimpleFormatter):
    """Only print filenames, e.g., flake8 -q."""

    error_format = "%(path)s"

    def after_init(self) -> None:
        """Initialize our set of filenames."""
        self.filenames_already_printed: set[str] = set()

    def show_source(self, error: Violation) -> str | None:
        """Do not include the source code."""

    def format(self, error: Violation) -> str | None:
        """Ensure we only print each error once."""
        if error.filename not in self.filenames_already_printed:
            self.filenames_already_printed.add(error.filename)
            return super().format(error)
        else:
            return None


class Nothing(base.BaseFormatter):
    """Print absolutely nothing."""

    def format(self, error: Violation) -> str | None:
        """Do nothing."""

    def show_source(self, error: Violation) -> str | None:
        """Do not print the source."""
```

## File: `src/flake8/main/__init__.py`
```python
"""Module containing the logic for the Flake8 entry-points."""
from __future__ import annotations
```

## File: `src/flake8/main/application.py`
```python
"""Module containing the application logic for Flake8."""
from __future__ import annotations

import argparse
import json
import logging
import time
from collections.abc import Sequence

import flake8
from flake8 import checker
from flake8 import defaults
from flake8 import exceptions
from flake8 import style_guide
from flake8.formatting.base import BaseFormatter
from flake8.main import debug
from flake8.options.parse_args import parse_args
from flake8.plugins import finder
from flake8.plugins import reporter


LOG = logging.getLogger(__name__)


class Application:
    """Abstract our application into a class."""

    def __init__(self) -> None:
        """Initialize our application."""
        #: The timestamp when the Application instance was instantiated.
        self.start_time = time.time()
        #: The timestamp when the Application finished reported errors.
        self.end_time: float | None = None

        self.plugins: finder.Plugins | None = None
        #: The user-selected formatter from :attr:`formatting_plugins`
        self.formatter: BaseFormatter | None = None
        #: The :class:`flake8.style_guide.StyleGuideManager` built from the
        #: user's options
        self.guide: style_guide.StyleGuideManager | None = None
        #: The :class:`flake8.checker.Manager` that will handle running all of
        #: the checks selected by the user.
        self.file_checker_manager: checker.Manager | None = None

        #: The user-supplied options parsed into an instance of
        #: :class:`argparse.Namespace`
        self.options: argparse.Namespace | None = None
        #: The number of errors, warnings, and other messages after running
        #: flake8 and taking into account ignored errors and lines.
        self.result_count = 0
        #: The total number of errors before accounting for ignored errors and
        #: lines.
        self.total_result_count = 0
        #: Whether or not something catastrophic happened and we should exit
        #: with a non-zero status code
        self.catastrophic_failure = False

    def exit_code(self) -> int:
        """Return the program exit code."""
        if self.catastrophic_failure:
            return 1
        assert self.options is not None
        if self.options.exit_zero:
            return 0
        else:
            return int(self.result_count > 0)

    def make_formatter(self) -> None:
        """Initialize a formatter based on the parsed options."""
        assert self.plugins is not None
        assert self.options is not None
        self.formatter = reporter.make(self.plugins.reporters, self.options)

    def make_guide(self) -> None:
        """Initialize our StyleGuide."""
        assert self.formatter is not None
        assert self.options is not None
        self.guide = style_guide.StyleGuideManager(
            self.options, self.formatter,
        )

    def make_file_checker_manager(self, argv: Sequence[str]) -> None:
        """Initialize our FileChecker Manager."""
        assert self.guide is not None
        assert self.plugins is not None
        self.file_checker_manager = checker.Manager(
            style_guide=self.guide,
            plugins=self.plugins.checkers,
            argv=argv,
        )

    def run_checks(self) -> None:
        """Run the actual checks with the FileChecker Manager.

        This method encapsulates the logic to make a
        :class:`~flake8.checker.Manger` instance run the checks it is
        managing.
        """
        assert self.file_checker_manager is not None

        self.file_checker_manager.start()
        try:
            self.file_checker_manager.run()
        except exceptions.PluginExecutionFailed as plugin_failed:
            print(str(plugin_failed))
            print("Run flake8 with greater verbosity to see more details")
            self.catastrophic_failure = True
        LOG.info("Finished running")
        self.file_checker_manager.stop()
        self.end_time = time.time()

    def report_benchmarks(self) -> None:
        """Aggregate, calculate, and report benchmarks for this run."""
        assert self.options is not None
        if not self.options.benchmark:
            return

        assert self.file_checker_manager is not None
        assert self.end_time is not None
        time_elapsed = self.end_time - self.start_time
        statistics = [("seconds elapsed", time_elapsed)]
        add_statistic = statistics.append
        for statistic in defaults.STATISTIC_NAMES + ("files",):
            value = self.file_checker_manager.statistics[statistic]
            total_description = f"total {statistic} processed"
            add_statistic((total_description, value))
            per_second_description = f"{statistic} processed per second"
            add_statistic((per_second_description, int(value / time_elapsed)))

        assert self.formatter is not None
        self.formatter.show_benchmarks(statistics)

    def report_errors(self) -> None:
        """Report all the errors found by flake8 3.0.

        This also updates the :attr:`result_count` attribute with the total
        number of errors, warnings, and other messages found.
        """
        LOG.info("Reporting errors")
        assert self.file_checker_manager is not None
        results = self.file_checker_manager.report()
        self.total_result_count, self.result_count = results
        LOG.info(
            "Found a total of %d violations and reported %d",
            self.total_result_count,
            self.result_count,
        )

    def report_statistics(self) -> None:
        """Aggregate and report statistics from this run."""
        assert self.options is not None
        if not self.options.statistics:
            return

        assert self.formatter is not None
        assert self.guide is not None
        self.formatter.show_statistics(self.guide.stats)

    def initialize(self, argv: Sequence[str]) -> None:
        """Initialize the application to be run.

        This finds the plugins, registers their options, and parses the
        command-line arguments.
        """
        self.plugins, self.options = parse_args(argv)

        if self.options.bug_report:
            info = debug.information(flake8.__version__, self.plugins)
            print(json.dumps(info, indent=2, sort_keys=True))
            raise SystemExit(0)

        self.make_formatter()
        self.make_guide()
        self.make_file_checker_manager(argv)

    def report(self) -> None:
        """Report errors, statistics, and benchmarks."""
        assert self.formatter is not None
        self.formatter.start()
        self.report_errors()
        self.report_statistics()
        self.report_benchmarks()
        self.formatter.stop()

    def _run(self, argv: Sequence[str]) -> None:
        self.initialize(argv)
        self.run_checks()
        self.report()

    def run(self, argv: Sequence[str]) -> None:
        """Run our application.

        This method will also handle KeyboardInterrupt exceptions for the
        entirety of the flake8 application. If it sees a KeyboardInterrupt it
        will forcibly clean up the :class:`~flake8.checker.Manager`.
        """
        try:
            self._run(argv)
        except KeyboardInterrupt as exc:
            print("... stopped")
            LOG.critical("Caught keyboard interrupt from user")
            LOG.exception(exc)
            self.catastrophic_failure = True
        except exceptions.ExecutionError as exc:
            print("There was a critical error during execution of Flake8:")
            print(exc)
            LOG.exception(exc)
            self.catastrophic_failure = True
        except exceptions.EarlyQuit:
            self.catastrophic_failure = True
            print("... stopped while processing files")
        else:
            assert self.options is not None
            if self.options.count:
                print(self.result_count)
```

## File: `src/flake8/main/cli.py`
```python
"""Command-line implementation of flake8."""
from __future__ import annotations

import sys
from collections.abc import Sequence

from flake8.main import application


def main(argv: Sequence[str] | None = None) -> int:
    """Execute the main bit of the application.

    This handles the creation of an instance of :class:`Application`, runs it,
    and then exits the application.

    :param argv:
        The arguments to be passed to the application for parsing.
    """
    if argv is None:
        argv = sys.argv[1:]

    app = application.Application()
    app.run(argv)
    return app.exit_code()
```

## File: `src/flake8/main/debug.py`
```python
"""Module containing the logic for our debugging logic."""
from __future__ import annotations

import platform
from typing import Any

from flake8.plugins.finder import Plugins


def information(version: str, plugins: Plugins) -> dict[str, Any]:
    """Generate the information to be printed for the bug report."""
    versions = sorted(
        {
            (loaded.plugin.package, loaded.plugin.version)
            for loaded in plugins.all_plugins()
            if loaded.plugin.package not in {"flake8", "local"}
        },
    )
    return {
        "version": version,
        "plugins": [
            {"plugin": plugin, "version": version}
            for plugin, version in versions
        ],
        "platform": {
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "system": platform.system(),
        },
    }
```

## File: `src/flake8/main/options.py`
```python
"""Contains the logic for all of the default options for Flake8."""
from __future__ import annotations

import argparse

from flake8 import defaults
from flake8.options.manager import OptionManager


def stage1_arg_parser() -> argparse.ArgumentParser:
    """Register the preliminary options on our OptionManager.

    The preliminary options include:

    - ``-v``/``--verbose``
    - ``--output-file``
    - ``--append-config``
    - ``--config``
    - ``--isolated``
    - ``--enable-extensions``
    """
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        "-v",
        "--verbose",
        default=0,
        action="count",
        help="Print more information about what is happening in flake8. "
        "This option is repeatable and will increase verbosity each "
        "time it is repeated.",
    )

    parser.add_argument(
        "--output-file", default=None, help="Redirect report to a file.",
    )

    # Config file options

    parser.add_argument(
        "--append-config",
        action="append",
        default=[],
        help="Provide extra config files to parse in addition to the files "
        "found by Flake8 by default. These files are the last ones read "
        "and so they take the highest precedence when multiple files "
        "provide the same option.",
    )

    parser.add_argument(
        "--config",
        default=None,
        help="Path to the config file that will be the authoritative config "
        "source. This will cause Flake8 to ignore all other "
        "configuration files.",
    )

    parser.add_argument(
        "--isolated",
        default=False,
        action="store_true",
        help="Ignore all configuration files.",
    )

    # Plugin enablement options

    parser.add_argument(
        "--enable-extensions",
        help="Enable plugins and extensions that are otherwise disabled "
        "by default",
    )

    parser.add_argument(
        "--require-plugins",
        help="Require specific plugins to be installed before running",
    )

    return parser


class JobsArgument:
    """Type callback for the --jobs argument."""

    def __init__(self, arg: str) -> None:
        """Parse and validate the --jobs argument.

        :param arg: The argument passed by argparse for validation
        """
        self.is_auto = False
        self.n_jobs = -1
        if arg == "auto":
            self.is_auto = True
        elif arg.isdigit():
            self.n_jobs = int(arg)
        else:
            raise argparse.ArgumentTypeError(
                f"{arg!r} must be 'auto' or an integer.",
            )

    def __repr__(self) -> str:
        """Representation for debugging."""
        return f"{type(self).__name__}({str(self)!r})"

    def __str__(self) -> str:
        """Format our JobsArgument class."""
        return "auto" if self.is_auto else str(self.n_jobs)


def register_default_options(option_manager: OptionManager) -> None:
    """Register the default options on our OptionManager.

    The default options include:

    - ``-q``/``--quiet``
    - ``--color``
    - ``--count``
    - ``--exclude``
    - ``--extend-exclude``
    - ``--filename``
    - ``--format``
    - ``--hang-closing``
    - ``--ignore``
    - ``--extend-ignore``
    - ``--per-file-ignores``
    - ``--max-line-length``
    - ``--max-doc-length``
    - ``--indent-size``
    - ``--select``
    - ``--extend-select``
    - ``--disable-noqa``
    - ``--show-source``
    - ``--statistics``
    - ``--exit-zero``
    - ``-j``/``--jobs``
    - ``--tee``
    - ``--benchmark``
    - ``--bug-report``
    """
    add_option = option_manager.add_option

    add_option(
        "-q",
        "--quiet",
        default=0,
        action="count",
        parse_from_config=True,
        help="Report only file names, or nothing. This option is repeatable.",
    )

    add_option(
        "--color",
        choices=("auto", "always", "never"),
        default="auto",
        help="Whether to use color in output.  Defaults to `%(default)s`.",
    )

    add_option(
        "--count",
        action="store_true",
        parse_from_config=True,
        help="Print total number of errors to standard output after "
        "all other output.",
    )

    add_option(
        "--exclude",
        metavar="patterns",
        default=",".join(defaults.EXCLUDE),
        comma_separated_list=True,
        parse_from_config=True,
        normalize_paths=True,
        help="Comma-separated list of files or directories to exclude. "
        "(Default: %(default)s)",
    )

    add_option(
        "--extend-exclude",
        metavar="patterns",
        default="",
        parse_from_config=True,
        comma_separated_list=True,
        normalize_paths=True,
        help="Comma-separated list of files or directories to add to the list "
        "of excluded ones.",
    )

    add_option(
        "--filename",
        metavar="patterns",
        default="*.py",
        parse_from_config=True,
        comma_separated_list=True,
        help="Only check for filenames matching the patterns in this comma-"
        "separated list. (Default: %(default)s)",
    )

    add_option(
        "--stdin-display-name",
        default="stdin",
        help="The name used when reporting errors from code passed via stdin. "
        "This is useful for editors piping the file contents to flake8. "
        "(Default: %(default)s)",
    )

    # TODO(sigmavirus24): Figure out --first/--repeat

    # NOTE(sigmavirus24): We can't use choices for this option since users can
    # freely provide a format string and that will break if we restrict their
    # choices.
    add_option(
        "--format",
        metavar="format",
        default="default",
        parse_from_config=True,
        help=(
            f"Format errors according to the chosen formatter "
            f"({', '.join(sorted(option_manager.formatter_names))}) "
            f"or a format string containing %%-style "
            f"mapping keys (code, col, path, row, text). "
            f"For example, "
            f"``--format=pylint`` or ``--format='%%(path)s %%(code)s'``. "
            f"(Default: %(default)s)"
        ),
    )

    add_option(
        "--hang-closing",
        action="store_true",
        parse_from_config=True,
        help="Hang closing bracket instead of matching indentation of opening "
        "bracket's line.",
    )

    add_option(
        "--ignore",
        metavar="errors",
        parse_from_config=True,
        comma_separated_list=True,
        help=(
            f"Comma-separated list of error codes to ignore (or skip). "
            f"For example, ``--ignore=E4,E51,W234``. "
            f"(Default: {','.join(defaults.IGNORE)})"
        ),
    )

    add_option(
        "--extend-ignore",
        metavar="errors",
        parse_from_config=True,
        comma_separated_list=True,
        help="Comma-separated list of error codes to add to the list of "
        "ignored ones. For example, ``--extend-ignore=E4,E51,W234``.",
    )

    add_option(
        "--per-file-ignores",
        default="",
        parse_from_config=True,
        help="A pairing of filenames and violation codes that defines which "
        "violations to ignore in a particular file. The filenames can be "
        "specified in a manner similar to the ``--exclude`` option and the "
        "violations work similarly to the ``--ignore`` and ``--select`` "
        "options.",
    )

    add_option(
        "--max-line-length",
        type=int,
        metavar="n",
        default=defaults.MAX_LINE_LENGTH,
        parse_from_config=True,
        help="Maximum allowed line length for the entirety of this run. "
        "(Default: %(default)s)",
    )

    add_option(
        "--max-doc-length",
        type=int,
        metavar="n",
        default=None,
        parse_from_config=True,
        help="Maximum allowed doc line length for the entirety of this run. "
        "(Default: %(default)s)",
    )
    add_option(
        "--indent-size",
        type=int,
        metavar="n",
        default=defaults.INDENT_SIZE,
        parse_from_config=True,
        help="Number of spaces used for indentation (Default: %(default)s)",
    )

    add_option(
        "--select",
        metavar="errors",
        parse_from_config=True,
        comma_separated_list=True,
        help=(
            "Limit the reported error codes to codes prefix-matched by this "
            "list.  "
            "You usually do not need to specify this option as the default "
            "includes all installed plugin codes.  "
            "For example, ``--select=E4,E51,W234``."
        ),
    )

    add_option(
        "--extend-select",
        metavar="errors",
        parse_from_config=True,
        comma_separated_list=True,
        help=(
            "Add additional error codes to the default ``--select``.  "
            "You usually do not need to specify this option as the default "
            "includes all installed plugin codes.  "
            "For example, ``--extend-select=E4,E51,W234``."
        ),
    )

    add_option(
        "--disable-noqa",
        default=False,
        parse_from_config=True,
        action="store_true",
        help='Disable the effect of "# noqa". This will report errors on '
        'lines with "# noqa" at the end.',
    )

    # TODO(sigmavirus24): Decide what to do about --show-pep8

    add_option(
        "--show-source",
        action="store_true",
        parse_from_config=True,
        help="Show the source generate each error or warning.",
    )
    add_option(
        "--no-show-source",
        action="store_false",
        dest="show_source",
        parse_from_config=False,
        help="Negate --show-source",
    )

    add_option(
        "--statistics",
        action="store_true",
        parse_from_config=True,
        help="Count errors.",
    )

    # Flake8 options

    add_option(
        "--exit-zero",
        action="store_true",
        help='Exit with status code "0" even if there are errors.',
    )

    add_option(
        "-j",
        "--jobs",
        default="auto",
        parse_from_config=True,
        type=JobsArgument,
        help="Number of subprocesses to use to run checks in parallel. "
        'This is ignored on Windows. The default, "auto", will '
        "auto-detect the number of processors available to use. "
        "(Default: %(default)s)",
    )

    add_option(
        "--tee",
        default=False,
        parse_from_config=True,
        action="store_true",
        help="Write to stdout and output-file.",
    )

    # Benchmarking

    add_option(
        "--benchmark",
        default=False,
        action="store_true",
        help="Print benchmark information about this run of Flake8",
    )

    # Debugging

    add_option(
        "--bug-report",
        action="store_true",
        help="Print information necessary when preparing a bug report",
    )
```

## File: `src/flake8/options/__init__.py`
```python
"""Package containing the option manager and config management logic.

- :mod:`flake8.options.config` contains the logic for finding, parsing, and
  merging configuration files.

- :mod:`flake8.options.manager` contains the logic for managing customized
  Flake8 command-line and configuration options.

- :mod:`flake8.options.aggregator` uses objects from both of the above modules
  to aggregate configuration into one object used by plugins and Flake8.

"""
from __future__ import annotations
```

## File: `src/flake8/options/aggregator.py`
```python
"""Aggregation function for CLI specified options and config file options.

This holds the logic that uses the collected and merged config files and
applies the user-specified command-line configuration on top of it.
"""
from __future__ import annotations

import argparse
import configparser
import logging
from collections.abc import Sequence

from flake8.options import config
from flake8.options.manager import OptionManager

LOG = logging.getLogger(__name__)


def aggregate_options(
    manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
    argv: Sequence[str] | None,
) -> argparse.Namespace:
    """Aggregate and merge CLI and config file options."""
    # Get defaults from the option parser
    default_values = manager.parse_args([])

    # Get the parsed config
    parsed_config = config.parse_config(manager, cfg, cfg_dir)

    # store the plugin-set extended default ignore / select
    default_values.extended_default_ignore = manager.extended_default_ignore
    default_values.extended_default_select = manager.extended_default_select

    # Merge values parsed from config onto the default values returned
    for config_name, value in parsed_config.items():
        dest_name = config_name
        # If the config name is somehow different from the destination name,
        # fetch the destination name from our Option
        if not hasattr(default_values, config_name):
            dest_val = manager.config_options_dict[config_name].dest
            assert isinstance(dest_val, str)
            dest_name = dest_val

        LOG.debug(
            'Overriding default value of (%s) for "%s" with (%s)',
            getattr(default_values, dest_name, None),
            dest_name,
            value,
        )
        # Override the default values with the config values
        setattr(default_values, dest_name, value)

    # Finally parse the command-line options
    return manager.parse_args(argv, default_values)
```

## File: `src/flake8/options/config.py`
```python
"""Config handling logic for Flake8."""
from __future__ import annotations

import configparser
import logging
import os.path
from typing import Any

from flake8 import exceptions
from flake8.defaults import VALID_CODE_PREFIX
from flake8.options.manager import OptionManager

LOG = logging.getLogger(__name__)


def _stat_key(s: str) -> tuple[int, int]:
    # same as what's used by samefile / samestat
    st = os.stat(s)
    return st.st_ino, st.st_dev


def _find_config_file(path: str) -> str | None:
    # on windows if the homedir isn't detected this returns back `~`
    home = os.path.expanduser("~")
    try:
        home_stat = _stat_key(home) if home != "~" else None
    except OSError:  # FileNotFoundError / PermissionError / etc.
        home_stat = None

    dir_stat = _stat_key(path)
    while True:
        for candidate in ("setup.cfg", "tox.ini", ".flake8"):
            cfg = configparser.RawConfigParser()
            cfg_path = os.path.join(path, candidate)
            try:
                cfg.read(cfg_path, encoding="UTF-8")
            except (UnicodeDecodeError, configparser.ParsingError) as e:
                LOG.warning("ignoring unparseable config %s: %s", cfg_path, e)
            else:
                # only consider it a config if it contains flake8 sections
                if "flake8" in cfg or "flake8:local-plugins" in cfg:
                    return cfg_path

        new_path = os.path.dirname(path)
        new_dir_stat = _stat_key(new_path)
        if new_dir_stat == dir_stat or new_dir_stat == home_stat:
            break
        else:
            path = new_path
            dir_stat = new_dir_stat

    # did not find any configuration file
    return None


def load_config(
    config: str | None,
    extra: list[str],
    *,
    isolated: bool = False,
) -> tuple[configparser.RawConfigParser, str]:
    """Load the configuration given the user options.

    - in ``isolated`` mode, return an empty configuration
    - if a config file is given in ``config`` use that, otherwise attempt to
      discover a configuration using ``tox.ini`` / ``setup.cfg`` / ``.flake8``
    - finally, load any ``extra`` configuration files
    """
    pwd = os.path.abspath(".")

    if isolated:
        return configparser.RawConfigParser(), pwd

    if config is None:
        config = _find_config_file(pwd)

    cfg = configparser.RawConfigParser()
    if config is not None:
        if not cfg.read(config, encoding="UTF-8"):
            raise exceptions.ExecutionError(
                f"The specified config file does not exist: {config}",
            )
        cfg_dir = os.path.dirname(config)
    else:
        cfg_dir = pwd

    # TODO: remove this and replace it with configuration modifying plugins
    # read the additional configs afterwards
    for filename in extra:
        if not cfg.read(filename, encoding="UTF-8"):
            raise exceptions.ExecutionError(
                f"The specified config file does not exist: {filename}",
            )

    return cfg, cfg_dir


def parse_config(
    option_manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
) -> dict[str, Any]:
    """Parse and normalize the typed configuration options."""
    if "flake8" not in cfg:
        return {}

    config_dict = {}

    for option_name in cfg["flake8"]:
        option = option_manager.config_options_dict.get(option_name)
        if option is None:
            LOG.debug('Option "%s" is not registered. Ignoring.', option_name)
            continue

        # Use the appropriate method to parse the config value
        value: Any
        if option.type is int or option.action == "count":
            value = cfg.getint("flake8", option_name)
        elif option.action in {"store_true", "store_false"}:
            value = cfg.getboolean("flake8", option_name)
        else:
            value = cfg.get("flake8", option_name)

        LOG.debug('Option "%s" returned value: %r', option_name, value)

        final_value = option.normalize(value, cfg_dir)

        if option_name in {"ignore", "extend-ignore"}:
            for error_code in final_value:
                if not VALID_CODE_PREFIX.match(error_code):
                    raise ValueError(
                        f"Error code {error_code!r} "
                        f"supplied to {option_name!r} option "
                        f"does not match {VALID_CODE_PREFIX.pattern!r}",
                    )

        assert option.config_name is not None
        config_dict[option.config_name] = final_value

    return config_dict
```

## File: `src/flake8/options/manager.py`
```python
"""Option handling and Option management logic."""
from __future__ import annotations

import argparse
import enum
import functools
import logging
from collections.abc import Callable
from collections.abc import Sequence
from typing import Any

from flake8 import utils
from flake8.plugins.finder import Plugins

LOG = logging.getLogger(__name__)

# represent a singleton of "not passed arguments".
# an enum is chosen to trick mypy
_ARG = enum.Enum("_ARG", "NO")


def _flake8_normalize(
    value: str,
    *args: str,
    comma_separated_list: bool = False,
    normalize_paths: bool = False,
) -> str | list[str]:
    ret: str | list[str] = value
    if comma_separated_list and isinstance(ret, str):
        ret = utils.parse_comma_separated_list(value)

    if normalize_paths:
        if isinstance(ret, str):
            ret = utils.normalize_path(ret, *args)
        else:
            ret = utils.normalize_paths(ret, *args)

    return ret


class Option:
    """Our wrapper around an argparse argument parsers to add features."""

    def __init__(
        self,
        short_option_name: str | _ARG = _ARG.NO,
        long_option_name: str | _ARG = _ARG.NO,
        # Options below are taken from argparse.ArgumentParser.add_argument
        action: str | type[argparse.Action] | _ARG = _ARG.NO,
        default: Any | _ARG = _ARG.NO,
        type: Callable[..., Any] | _ARG = _ARG.NO,
        dest: str | _ARG = _ARG.NO,
        nargs: int | str | _ARG = _ARG.NO,
        const: Any | _ARG = _ARG.NO,
        choices: Sequence[Any] | _ARG = _ARG.NO,
        help: str | _ARG = _ARG.NO,
        metavar: str | _ARG = _ARG.NO,
        required: bool | _ARG = _ARG.NO,
        # Options below here are specific to Flake8
        parse_from_config: bool = False,
        comma_separated_list: bool = False,
        normalize_paths: bool = False,
    ) -> None:
        """Initialize an Option instance.

        The following are all passed directly through to argparse.

        :param short_option_name:
            The short name of the option (e.g., ``-x``). This will be the
            first argument passed to ``ArgumentParser.add_argument``
        :param long_option_name:
            The long name of the option (e.g., ``--xtra-long-option``). This
            will be the second argument passed to
            ``ArgumentParser.add_argument``
        :param default:
            Default value of the option.
        :param dest:
            Attribute name to store parsed option value as.
        :param nargs:
            Number of arguments to parse for this option.
        :param const:
            Constant value to store on a common destination. Usually used in
            conjunction with ``action="store_const"``.
        :param choices:
            Possible values for the option.
        :param help:
            Help text displayed in the usage information.
        :param metavar:
            Name to use instead of the long option name for help text.
        :param required:
            Whether this option is required or not.

        The following options may be passed directly through to :mod:`argparse`
        but may need some massaging.

        :param type:
            A callable to normalize the type (as is the case in
            :mod:`argparse`).
        :param action:
            Any action allowed by :mod:`argparse`.

        The following parameters are for Flake8's option handling alone.

        :param parse_from_config:
            Whether or not this option should be parsed out of config files.
        :param comma_separated_list:
            Whether the option is a comma separated list when parsing from a
            config file.
        :param normalize_paths:
            Whether the option is expecting a path or list of paths and should
            attempt to normalize the paths to absolute paths.
        """
        if (
            long_option_name is _ARG.NO
            and short_option_name is not _ARG.NO
            and short_option_name.startswith("--")
        ):
            short_option_name, long_option_name = _ARG.NO, short_option_name

        # flake8 special type normalization
        if comma_separated_list or normalize_paths:
            type = functools.partial(
                _flake8_normalize,
                comma_separated_list=comma_separated_list,
                normalize_paths=normalize_paths,
            )

        self.short_option_name = short_option_name
        self.long_option_name = long_option_name
        self.option_args = [
            x
            for x in (short_option_name, long_option_name)
            if x is not _ARG.NO
        ]
        self.action = action
        self.default = default
        self.type = type
        self.dest = dest
        self.nargs = nargs
        self.const = const
        self.choices = choices
        self.help = help
        self.metavar = metavar
        self.required = required
        self.option_kwargs: dict[str, Any | _ARG] = {
            "action": self.action,
            "default": self.default,
            "type": self.type,
            "dest": self.dest,
            "nargs": self.nargs,
            "const": self.const,
            "choices": self.choices,
            "help": self.help,
            "metavar": self.metavar,
            "required": self.required,
        }

        # Set our custom attributes
        self.parse_from_config = parse_from_config
        self.comma_separated_list = comma_separated_list
        self.normalize_paths = normalize_paths

        self.config_name: str | None = None
        if parse_from_config:
            if long_option_name is _ARG.NO:
                raise ValueError(
                    "When specifying parse_from_config=True, "
                    "a long_option_name must also be specified.",
                )
            self.config_name = long_option_name[2:].replace("-", "_")

        self._opt = None

    @property
    def filtered_option_kwargs(self) -> dict[str, Any]:
        """Return any actually-specified arguments."""
        return {
            k: v for k, v in self.option_kwargs.items() if v is not _ARG.NO
        }

    def __repr__(self) -> str:  # noqa: D105
        parts = []
        for arg in self.option_args:
            parts.append(arg)
        for k, v in self.filtered_option_kwargs.items():
            parts.append(f"{k}={v!r}")
        return f"Option({', '.join(parts)})"

    def normalize(self, value: Any, *normalize_args: str) -> Any:
        """Normalize the value based on the option configuration."""
        if self.comma_separated_list and isinstance(value, str):
            value = utils.parse_comma_separated_list(value)

        if self.normalize_paths:
            if isinstance(value, list):
                value = utils.normalize_paths(value, *normalize_args)
            else:
                value = utils.normalize_path(value, *normalize_args)

        return value

    def to_argparse(self) -> tuple[list[str], dict[str, Any]]:
        """Convert a Flake8 Option to argparse ``add_argument`` arguments."""
        return self.option_args, self.filtered_option_kwargs


class OptionManager:
    """Manage Options and OptionParser while adding post-processing."""

    def __init__(
        self,
        *,
        version: str,
        plugin_versions: str,
        parents: list[argparse.ArgumentParser],
        formatter_names: list[str],
    ) -> None:
        """Initialize an instance of an OptionManager."""
        self.formatter_names = formatter_names
        self.parser = argparse.ArgumentParser(
            prog="flake8",
            usage="%(prog)s [options] file file ...",
            parents=parents,
            epilog=f"Installed plugins: {plugin_versions}",
        )
        self.parser.add_argument(
            "--version",
            action="version",
            version=(
                f"{version} ({plugin_versions}) "
                f"{utils.get_python_version()}"
            ),
        )
        self.parser.add_argument("filenames", nargs="*", metavar="filename")

        self.config_options_dict: dict[str, Option] = {}
        self.options: list[Option] = []
        self.extended_default_ignore: list[str] = []
        self.extended_default_select: list[str] = []

        self._current_group: argparse._ArgumentGroup | None = None

    # TODO: maybe make this a free function to reduce api surface area
    def register_plugins(self, plugins: Plugins) -> None:
        """Register the plugin options (if needed)."""
        groups: dict[str, argparse._ArgumentGroup] = {}

        def _set_group(name: str) -> None:
            try:
                self._current_group = groups[name]
            except KeyError:
                group = self.parser.add_argument_group(name)
                self._current_group = groups[name] = group

        for loaded in plugins.all_plugins():
            add_options = getattr(loaded.obj, "add_options", None)
            if add_options:
                _set_group(loaded.plugin.package)
                add_options(self)

            if loaded.plugin.entry_point.group == "flake8.extension":
                self.extend_default_select([loaded.entry_name])

        # isn't strictly necessary, but seems cleaner
        self._current_group = None

    def add_option(self, *args: Any, **kwargs: Any) -> None:
        """Create and register a new option.

        See parameters for :class:`~flake8.options.manager.Option` for
        acceptable arguments to this method.

        .. note::

            ``short_option_name`` and ``long_option_name`` may be specified
            positionally as they are with argparse normally.
        """
        option = Option(*args, **kwargs)
        option_args, option_kwargs = option.to_argparse()
        if self._current_group is not None:
            self._current_group.add_argument(*option_args, **option_kwargs)
        else:
            self.parser.add_argument(*option_args, **option_kwargs)
        self.options.append(option)
        if option.parse_from_config:
            name = option.config_name
            assert name is not None
            self.config_options_dict[name] = option
            self.config_options_dict[name.replace("_", "-")] = option
        LOG.debug('Registered option "%s".', option)

    def extend_default_ignore(self, error_codes: Sequence[str]) -> None:
        """Extend the default ignore list with the error codes provided.

        :param error_codes:
            List of strings that are the error/warning codes with which to
            extend the default ignore list.
        """
        LOG.debug("Extending default ignore list with %r", error_codes)
        self.extended_default_ignore.extend(error_codes)

    def extend_default_select(self, error_codes: Sequence[str]) -> None:
        """Extend the default select list with the error codes provided.

        :param error_codes:
            List of strings that are the error/warning codes with which
            to extend the default select list.
        """
        LOG.debug("Extending default select list with %r", error_codes)
        self.extended_default_select.extend(error_codes)

    def parse_args(
        self,
        args: Sequence[str] | None = None,
        values: argparse.Namespace | None = None,
    ) -> argparse.Namespace:
        """Proxy to calling the OptionParser's parse_args method."""
        if values:
            self.parser.set_defaults(**vars(values))
        return self.parser.parse_args(args)
```

## File: `src/flake8/options/parse_args.py`
```python
"""Procedure for parsing args, config, loading plugins."""
from __future__ import annotations

import argparse
from collections.abc import Sequence

import flake8
from flake8.main import options
from flake8.options import aggregator
from flake8.options import config
from flake8.options import manager
from flake8.plugins import finder


def parse_args(
    argv: Sequence[str],
) -> tuple[finder.Plugins, argparse.Namespace]:
    """Procedure for parsing args, config, loading plugins."""
    prelim_parser = options.stage1_arg_parser()

    args0, rest = prelim_parser.parse_known_args(argv)
    # XXX (ericvw): Special case "forwarding" the output file option so
    # that it can be reparsed again for the BaseFormatter.filename.
    if args0.output_file:
        rest.extend(("--output-file", args0.output_file))

    flake8.configure_logging(args0.verbose, args0.output_file)

    cfg, cfg_dir = config.load_config(
        config=args0.config,
        extra=args0.append_config,
        isolated=args0.isolated,
    )

    plugin_opts = finder.parse_plugin_options(
        cfg,
        cfg_dir,
        enable_extensions=args0.enable_extensions,
        require_plugins=args0.require_plugins,
    )
    raw_plugins = finder.find_plugins(cfg, plugin_opts)
    plugins = finder.load_plugins(raw_plugins, plugin_opts)

    option_manager = manager.OptionManager(
        version=flake8.__version__,
        plugin_versions=plugins.versions_str(),
        parents=[prelim_parser],
        formatter_names=list(plugins.reporters),
    )
    options.register_default_options(option_manager)
    option_manager.register_plugins(plugins)

    opts = aggregator.aggregate_options(option_manager, cfg, cfg_dir, rest)

    for loaded in plugins.all_plugins():
        parse_options = getattr(loaded.obj, "parse_options", None)
        if parse_options is None:
            continue

        # XXX: ideally we wouldn't have two forms of parse_options
        try:
            parse_options(
                option_manager,
                opts,
                opts.filenames,
            )
        except TypeError:
            parse_options(opts)

    return plugins, opts
```

## File: `src/flake8/plugins/__init__.py`
```python
"""Submodule of built-in plugins and plugin managers."""
from __future__ import annotations
```

## File: `src/flake8/plugins/finder.py`
```python
"""Functions related to finding and loading plugins."""
from __future__ import annotations

import configparser
import importlib.metadata
import inspect
import itertools
import logging
import sys
from collections.abc import Generator
from collections.abc import Iterable
from typing import Any
from typing import NamedTuple

from flake8 import utils
from flake8.defaults import VALID_CODE_PREFIX
from flake8.exceptions import ExecutionError
from flake8.exceptions import FailedToLoadPlugin

LOG = logging.getLogger(__name__)

FLAKE8_GROUPS = frozenset(("flake8.extension", "flake8.report"))

BANNED_PLUGINS = {
    "flake8-colors": "5.0",
    "flake8-per-file-ignores": "3.7",
}


class Plugin(NamedTuple):
    """A plugin before loading."""

    package: str
    version: str
    entry_point: importlib.metadata.EntryPoint


class LoadedPlugin(NamedTuple):
    """Represents a plugin after being imported."""

    plugin: Plugin
    obj: Any
    parameters: dict[str, bool]

    @property
    def entry_name(self) -> str:
        """Return the name given in the packaging metadata."""
        return self.plugin.entry_point.name

    @property
    def display_name(self) -> str:
        """Return the name for use in user-facing / error messages."""
        return f"{self.plugin.package}[{self.entry_name}]"


class Checkers(NamedTuple):
    """Classified plugins needed for checking."""

    tree: list[LoadedPlugin]
    logical_line: list[LoadedPlugin]
    physical_line: list[LoadedPlugin]


class Plugins(NamedTuple):
    """Classified plugins."""

    checkers: Checkers
    reporters: dict[str, LoadedPlugin]
    disabled: list[LoadedPlugin]

    def all_plugins(self) -> Generator[LoadedPlugin]:
        """Return an iterator over all :class:`LoadedPlugin`s."""
        yield from self.checkers.tree
        yield from self.checkers.logical_line
        yield from self.checkers.physical_line
        yield from self.reporters.values()

    def versions_str(self) -> str:
        """Return a user-displayed list of plugin versions."""
        return ", ".join(
            sorted(
                {
                    f"{loaded.plugin.package}: {loaded.plugin.version}"
                    for loaded in self.all_plugins()
                    if loaded.plugin.package not in {"flake8", "local"}
                },
            ),
        )


class PluginOptions(NamedTuple):
    """Options related to plugin loading."""

    local_plugin_paths: tuple[str, ...]
    enable_extensions: frozenset[str]
    require_plugins: frozenset[str]

    @classmethod
    def blank(cls) -> PluginOptions:
        """Make a blank PluginOptions, mostly used for tests."""
        return cls(
            local_plugin_paths=(),
            enable_extensions=frozenset(),
            require_plugins=frozenset(),
        )


def _parse_option(
    cfg: configparser.RawConfigParser,
    cfg_opt_name: str,
    opt: str | None,
) -> list[str]:
    # specified on commandline: use that
    if opt is not None:
        return utils.parse_comma_separated_list(opt)
    else:
        # ideally this would reuse our config parsing framework but we need to
        # parse this from preliminary options before plugins are enabled
        for opt_name in (cfg_opt_name, cfg_opt_name.replace("_", "-")):
            val = cfg.get("flake8", opt_name, fallback=None)
            if val is not None:
                return utils.parse_comma_separated_list(val)
        else:
            return []


def parse_plugin_options(
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
    *,
    enable_extensions: str | None,
    require_plugins: str | None,
) -> PluginOptions:
    """Parse plugin loading related options."""
    paths_s = cfg.get("flake8:local-plugins", "paths", fallback="").strip()
    paths = utils.parse_comma_separated_list(paths_s)
    paths = utils.normalize_paths(paths, cfg_dir)

    return PluginOptions(
        local_plugin_paths=tuple(paths),
        enable_extensions=frozenset(
            _parse_option(cfg, "enable_extensions", enable_extensions),
        ),
        require_plugins=frozenset(
            _parse_option(cfg, "require_plugins", require_plugins),
        ),
    )


def _flake8_plugins(
    eps: Iterable[importlib.metadata.EntryPoint],
    name: str,
    version: str,
) -> Generator[Plugin]:
    pyflakes_meta = importlib.metadata.distribution("pyflakes").metadata
    pycodestyle_meta = importlib.metadata.distribution("pycodestyle").metadata

    for ep in eps:
        if ep.group not in FLAKE8_GROUPS:
            continue

        if ep.name == "F":
            yield Plugin(pyflakes_meta["name"], pyflakes_meta["version"], ep)
        elif ep.name in "EW":
            # pycodestyle provides both `E` and `W` -- but our default select
            # handles those
            # ideally pycodestyle's plugin entrypoints would exactly represent
            # the codes they produce...
            yield Plugin(
                pycodestyle_meta["name"], pycodestyle_meta["version"], ep,
            )
        else:
            yield Plugin(name, version, ep)


def _find_importlib_plugins() -> Generator[Plugin]:
    # some misconfigured pythons (RHEL) have things on `sys.path` twice
    seen = set()
    for dist in importlib.metadata.distributions():
        # assigned to prevent continual reparsing
        eps = dist.entry_points

        # perf: skip parsing `.metadata` (slow) if no entry points match
        if not any(ep.group in FLAKE8_GROUPS for ep in eps):
            continue

        # assigned to prevent continual reparsing
        meta = dist.metadata

        if meta["name"] in seen:
            continue
        else:
            seen.add(meta["name"])

        if meta["name"] in BANNED_PLUGINS:
            LOG.warning(
                "%s plugin is obsolete in flake8>=%s",
                meta["name"],
                BANNED_PLUGINS[meta["name"]],
            )
            continue
        elif meta["name"] == "flake8":
            # special case flake8 which provides plugins for pyflakes /
            # pycodestyle
            yield from _flake8_plugins(eps, meta["name"], meta["version"])
            continue

        for ep in eps:
            if ep.group in FLAKE8_GROUPS:
                yield Plugin(meta["name"], meta["version"], ep)


def _find_local_plugins(
    cfg: configparser.RawConfigParser,
) -> Generator[Plugin]:
    for plugin_type in ("extension", "report"):
        group = f"flake8.{plugin_type}"
        for plugin_s in utils.parse_comma_separated_list(
            cfg.get("flake8:local-plugins", plugin_type, fallback="").strip(),
            regexp=utils.LOCAL_PLUGIN_LIST_RE,
        ):
            name, _, entry_str = plugin_s.partition("=")
            name, entry_str = name.strip(), entry_str.strip()
            ep = importlib.metadata.EntryPoint(name, entry_str, group)
            yield Plugin("local", "local", ep)


def _check_required_plugins(
    plugins: list[Plugin],
    expected: frozenset[str],
) -> None:
    plugin_names = {
        utils.normalize_pypi_name(plugin.package) for plugin in plugins
    }
    expected_names = {utils.normalize_pypi_name(name) for name in expected}
    missing_plugins = expected_names - plugin_names

    if missing_plugins:
        raise ExecutionError(
            f"required plugins were not installed!\n"
            f"- installed: {', '.join(sorted(plugin_names))}\n"
            f"- expected: {', '.join(sorted(expected_names))}\n"
            f"- missing: {', '.join(sorted(missing_plugins))}",
        )


def find_plugins(
    cfg: configparser.RawConfigParser,
    opts: PluginOptions,
) -> list[Plugin]:
    """Discovers all plugins (but does not load them)."""
    ret = [*_find_importlib_plugins(), *_find_local_plugins(cfg)]

    # for determinism, sort the list
    ret.sort()

    _check_required_plugins(ret, opts.require_plugins)

    return ret


def _parameters_for(func: Any) -> dict[str, bool]:
    """Return the parameters for the plugin.

    This will inspect the plugin and return either the function parameters
    if the plugin is a function or the parameters for ``__init__`` after
    ``self`` if the plugin is a class.

    :returns:
        A dictionary mapping the parameter name to whether or not it is
        required (a.k.a., is positional only/does not have a default).
    """
    is_class = not inspect.isfunction(func)
    if is_class:
        func = func.__init__

    parameters = {
        parameter.name: parameter.default is inspect.Parameter.empty
        for parameter in inspect.signature(func).parameters.values()
        if parameter.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD
    }

    if is_class:
        parameters.pop("self", None)

    return parameters


def _load_plugin(plugin: Plugin) -> LoadedPlugin:
    try:
        obj = plugin.entry_point.load()
    except Exception as e:
        raise FailedToLoadPlugin(plugin.package, e)

    if not callable(obj):
        err = TypeError("expected loaded plugin to be callable")
        raise FailedToLoadPlugin(plugin.package, err)

    return LoadedPlugin(plugin, obj, _parameters_for(obj))


def _import_plugins(
    plugins: list[Plugin],
    opts: PluginOptions,
) -> list[LoadedPlugin]:
    sys.path.extend(opts.local_plugin_paths)
    return [_load_plugin(p) for p in plugins]


def _classify_plugins(
    plugins: list[LoadedPlugin],
    opts: PluginOptions,
) -> Plugins:
    tree = []
    logical_line = []
    physical_line = []
    reporters = {}
    disabled = []

    for loaded in plugins:
        if (
            getattr(loaded.obj, "off_by_default", False)
            and loaded.plugin.entry_point.name not in opts.enable_extensions
        ):
            disabled.append(loaded)
        elif loaded.plugin.entry_point.group == "flake8.report":
            reporters[loaded.entry_name] = loaded
        elif "tree" in loaded.parameters:
            tree.append(loaded)
        elif "logical_line" in loaded.parameters:
            logical_line.append(loaded)
        elif "physical_line" in loaded.parameters:
            physical_line.append(loaded)
        else:
            raise NotImplementedError(f"what plugin type? {loaded}")

    for loaded in itertools.chain(tree, logical_line, physical_line):
        if not VALID_CODE_PREFIX.match(loaded.entry_name):
            raise ExecutionError(
                f"plugin code for `{loaded.display_name}` does not match "
                f"{VALID_CODE_PREFIX.pattern}",
            )

    return Plugins(
        checkers=Checkers(
            tree=tree,
            logical_line=logical_line,
            physical_line=physical_line,
        ),
        reporters=reporters,
        disabled=disabled,
    )


def load_plugins(
    plugins: list[Plugin],
    opts: PluginOptions,
) -> Plugins:
    """Load and classify all flake8 plugins.

    - first: extends ``sys.path`` with ``paths`` (to import local plugins)
    - next: converts the ``Plugin``s to ``LoadedPlugins``
    - finally: classifies plugins into their specific types
    """
    return _classify_plugins(_import_plugins(plugins, opts), opts)
```

## File: `src/flake8/plugins/pycodestyle.py`
```python
"""Generated using ./bin/gen-pycodestyle-plugin."""
# fmt: off
from __future__ import annotations

from collections.abc import Generator
from typing import Any

from pycodestyle import ambiguous_identifier as _ambiguous_identifier
from pycodestyle import bare_except as _bare_except
from pycodestyle import blank_lines as _blank_lines
from pycodestyle import break_after_binary_operator as _break_after_binary_operator  # noqa: E501
from pycodestyle import break_before_binary_operator as _break_before_binary_operator  # noqa: E501
from pycodestyle import comparison_negative as _comparison_negative
from pycodestyle import comparison_to_singleton as _comparison_to_singleton
from pycodestyle import comparison_type as _comparison_type
from pycodestyle import compound_statements as _compound_statements
from pycodestyle import continued_indentation as _continued_indentation
from pycodestyle import explicit_line_join as _explicit_line_join
from pycodestyle import extraneous_whitespace as _extraneous_whitespace
from pycodestyle import imports_on_separate_lines as _imports_on_separate_lines
from pycodestyle import indentation as _indentation
from pycodestyle import maximum_doc_length as _maximum_doc_length
from pycodestyle import maximum_line_length as _maximum_line_length
from pycodestyle import missing_whitespace as _missing_whitespace
from pycodestyle import missing_whitespace_after_keyword as _missing_whitespace_after_keyword  # noqa: E501
from pycodestyle import module_imports_on_top_of_file as _module_imports_on_top_of_file  # noqa: E501
from pycodestyle import python_3000_invalid_escape_sequence as _python_3000_invalid_escape_sequence  # noqa: E501
from pycodestyle import tabs_obsolete as _tabs_obsolete
from pycodestyle import tabs_or_spaces as _tabs_or_spaces
from pycodestyle import trailing_blank_lines as _trailing_blank_lines
from pycodestyle import trailing_whitespace as _trailing_whitespace
from pycodestyle import whitespace_around_comma as _whitespace_around_comma
from pycodestyle import whitespace_around_keywords as _whitespace_around_keywords  # noqa: E501
from pycodestyle import whitespace_around_named_parameter_equals as _whitespace_around_named_parameter_equals  # noqa: E501
from pycodestyle import whitespace_around_operator as _whitespace_around_operator  # noqa: E501
from pycodestyle import whitespace_before_comment as _whitespace_before_comment
from pycodestyle import whitespace_before_parameters as _whitespace_before_parameters  # noqa: E501


def pycodestyle_logical(
    blank_before: Any,
    blank_lines: Any,
    checker_state: Any,
    hang_closing: Any,
    indent_char: Any,
    indent_level: Any,
    indent_size: Any,
    line_number: Any,
    lines: Any,
    logical_line: Any,
    max_doc_length: Any,
    noqa: Any,
    previous_indent_level: Any,
    previous_logical: Any,
    previous_unindented_logical_line: Any,
    tokens: Any,
    verbose: Any,
) -> Generator[tuple[int, str]]:
    """Run pycodestyle logical checks."""
    yield from _ambiguous_identifier(logical_line, tokens)
    yield from _bare_except(logical_line, noqa)
    yield from _blank_lines(logical_line, blank_lines, indent_level, line_number, blank_before, previous_logical, previous_unindented_logical_line, previous_indent_level, lines)  # noqa: E501
    yield from _break_after_binary_operator(logical_line, tokens)
    yield from _break_before_binary_operator(logical_line, tokens)
    yield from _comparison_negative(logical_line)
    yield from _comparison_to_singleton(logical_line, noqa)
    yield from _comparison_type(logical_line, noqa)
    yield from _compound_statements(logical_line)
    yield from _continued_indentation(logical_line, tokens, indent_level, hang_closing, indent_char, indent_size, noqa, verbose)  # noqa: E501
    yield from _explicit_line_join(logical_line, tokens)
    yield from _extraneous_whitespace(logical_line)
    yield from _imports_on_separate_lines(logical_line)
    yield from _indentation(logical_line, previous_logical, indent_char, indent_level, previous_indent_level, indent_size)  # noqa: E501
    yield from _maximum_doc_length(logical_line, max_doc_length, noqa, tokens)
    yield from _missing_whitespace(logical_line, tokens)
    yield from _missing_whitespace_after_keyword(logical_line, tokens)
    yield from _module_imports_on_top_of_file(logical_line, indent_level, checker_state, noqa)  # noqa: E501
    yield from _python_3000_invalid_escape_sequence(logical_line, tokens, noqa)
    yield from _whitespace_around_comma(logical_line)
    yield from _whitespace_around_keywords(logical_line)
    yield from _whitespace_around_named_parameter_equals(logical_line, tokens)
    yield from _whitespace_around_operator(logical_line)
    yield from _whitespace_before_comment(logical_line, tokens)
    yield from _whitespace_before_parameters(logical_line, tokens)


def pycodestyle_physical(
    indent_char: Any,
    line_number: Any,
    lines: Any,
    max_line_length: Any,
    multiline: Any,
    noqa: Any,
    physical_line: Any,
    total_lines: Any,
) -> Generator[tuple[int, str]]:
    """Run pycodestyle physical checks."""
    ret = _maximum_line_length(physical_line, max_line_length, multiline, line_number, noqa)  # noqa: E501
    if ret is not None:
        yield ret
    ret = _tabs_obsolete(physical_line)
    if ret is not None:
        yield ret
    ret = _tabs_or_spaces(physical_line, indent_char)
    if ret is not None:
        yield ret
    ret = _trailing_blank_lines(physical_line, lines, line_number, total_lines)
    if ret is not None:
        yield ret
    ret = _trailing_whitespace(physical_line)
    if ret is not None:
        yield ret
```

## File: `src/flake8/plugins/pyflakes.py`
```python
"""Plugin built-in to Flake8 to treat pyflakes as a plugin."""
from __future__ import annotations

import argparse
import ast
import logging
from collections.abc import Generator
from typing import Any

import pyflakes.checker

from flake8.options.manager import OptionManager

LOG = logging.getLogger(__name__)

FLAKE8_PYFLAKES_CODES = {
    "UnusedImport": "F401",
    "ImportShadowedByLoopVar": "F402",
    "ImportStarUsed": "F403",
    "LateFutureImport": "F404",
    "ImportStarUsage": "F405",
    "ImportStarNotPermitted": "F406",
    "FutureFeatureNotDefined": "F407",
    "PercentFormatInvalidFormat": "F501",
    "PercentFormatExpectedMapping": "F502",
    "PercentFormatExpectedSequence": "F503",
    "PercentFormatExtraNamedArguments": "F504",
    "PercentFormatMissingArgument": "F505",
    "PercentFormatMixedPositionalAndNamed": "F506",
    "PercentFormatPositionalCountMismatch": "F507",
    "PercentFormatStarRequiresSequence": "F508",
    "PercentFormatUnsupportedFormatCharacter": "F509",
    "StringDotFormatInvalidFormat": "F521",
    "StringDotFormatExtraNamedArguments": "F522",
    "StringDotFormatExtraPositionalArguments": "F523",
    "StringDotFormatMissingArgument": "F524",
    "StringDotFormatMixingAutomatic": "F525",
    "FStringMissingPlaceholders": "F541",
    "TStringMissingPlaceholders": "F542",
    "MultiValueRepeatedKeyLiteral": "F601",
    "MultiValueRepeatedKeyVariable": "F602",
    "TooManyExpressionsInStarredAssignment": "F621",
    "TwoStarredExpressions": "F622",
    "AssertTuple": "F631",
    "IsLiteral": "F632",
    "InvalidPrintSyntax": "F633",
    "IfTuple": "F634",
    "BreakOutsideLoop": "F701",
    "ContinueOutsideLoop": "F702",
    "YieldOutsideFunction": "F704",
    "ReturnOutsideFunction": "F706",
    "DefaultExceptNotLast": "F707",
    "DoctestSyntaxError": "F721",
    "ForwardAnnotationSyntaxError": "F722",
    "RedefinedWhileUnused": "F811",
    "UndefinedName": "F821",
    "UndefinedExport": "F822",
    "UndefinedLocal": "F823",
    "UnusedIndirectAssignment": "F824",
    "DuplicateArgument": "F831",
    "UnusedVariable": "F841",
    "UnusedAnnotation": "F842",
    "RaiseNotImplemented": "F901",
}


class FlakesChecker(pyflakes.checker.Checker):
    """Subclass the Pyflakes checker to conform with the flake8 API."""

    with_doctest = False

    def __init__(self, tree: ast.AST, filename: str) -> None:
        """Initialize the PyFlakes plugin with an AST tree and filename."""
        super().__init__(
            tree, filename=filename, withDoctest=self.with_doctest,
        )

    @classmethod
    def add_options(cls, parser: OptionManager) -> None:
        """Register options for PyFlakes on the Flake8 OptionManager."""
        parser.add_option(
            "--builtins",
            parse_from_config=True,
            comma_separated_list=True,
            help="define more built-ins, comma separated",
        )
        parser.add_option(
            "--doctests",
            default=False,
            action="store_true",
            parse_from_config=True,
            help="also check syntax of the doctests",
        )

    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None:
        """Parse option values from Flake8's OptionManager."""
        if options.builtins:
            cls.builtIns = cls.builtIns.union(options.builtins)
        cls.with_doctest = options.doctests

    def run(self) -> Generator[tuple[int, int, str, type[Any]]]:
        """Run the plugin."""
        for message in self.messages:
            col = getattr(message, "col", 0)
            yield (
                message.lineno,
                col,
                "{} {}".format(
                    FLAKE8_PYFLAKES_CODES.get(type(message).__name__, "F999"),
                    message.message % message.message_args,
                ),
                message.__class__,
            )
```

## File: `src/flake8/plugins/reporter.py`
```python
"""Functions for constructing the requested report plugin."""
from __future__ import annotations

import argparse
import logging

from flake8.formatting.base import BaseFormatter
from flake8.plugins.finder import LoadedPlugin

LOG = logging.getLogger(__name__)


def make(
    reporters: dict[str, LoadedPlugin],
    options: argparse.Namespace,
) -> BaseFormatter:
    """Make the formatter from the requested user options.

    - if :option:`flake8 --quiet` is specified, return the ``quiet-filename``
      formatter.
    - if :option:`flake8 --quiet` is specified at least twice, return the
      ``quiet-nothing`` formatter.
    - otherwise attempt to return the formatter by name.
    - failing that, assume it is a format string and return the ``default``
      formatter.
    """
    format_name = options.format
    if options.quiet == 1:
        format_name = "quiet-filename"
    elif options.quiet >= 2:
        format_name = "quiet-nothing"

    try:
        format_plugin = reporters[format_name]
    except KeyError:
        LOG.warning(
            "%r is an unknown formatter.  Falling back to default.",
            format_name,
        )
        format_plugin = reporters["default"]

    return format_plugin.obj(options)
```

## File: `tests/__init__.py`
```python
"""This is here because mypy doesn't understand PEP 420."""
from __future__ import annotations
```

## File: `tests/conftest.py`
```python
"""Test configuration for py.test."""
from __future__ import annotations

import sys

import flake8

flake8.configure_logging(2, "test-logs-%s.%s.log" % sys.version_info[0:2])
```

## File: `tests/integration/test_aggregator.py`
```python
"""Test aggregation of config files and command-line options."""
from __future__ import annotations

import os

import pytest

from flake8.main import options
from flake8.options import aggregator
from flake8.options import config
from flake8.options import manager


@pytest.fixture
def optmanager():
    """Create a new OptionManager."""
    option_manager = manager.OptionManager(
        version="3.0.0",
        plugin_versions="",
        parents=[],
        formatter_names=[],
    )
    options.register_default_options(option_manager)
    return option_manager


@pytest.fixture
def flake8_config(tmp_path):
    cfg_s = """\
[flake8]
ignore =
    E123,
    W234,
    E111
exclude =
    foo/,
    bar/,
    bogus/
quiet = 1
"""
    cfg = tmp_path.joinpath("tox.ini")
    cfg.write_text(cfg_s)
    return str(cfg)


def test_aggregate_options_with_config(optmanager, flake8_config):
    """Verify we aggregate options and config values appropriately."""
    arguments = [
        "flake8",
        "--select",
        "E11,E34,E402,W,F",
        "--exclude",
        "tests/*",
    ]
    cfg, cfg_dir = config.load_config(flake8_config, [])
    options = aggregator.aggregate_options(
        optmanager,
        cfg,
        cfg_dir,
        arguments,
    )

    assert options.select == ["E11", "E34", "E402", "W", "F"]
    assert options.ignore == ["E123", "W234", "E111"]
    assert options.exclude == [os.path.abspath("tests/*")]


def test_aggregate_options_when_isolated(optmanager, flake8_config):
    """Verify we aggregate options and config values appropriately."""
    arguments = [
        "flake8",
        "--select",
        "E11,E34,E402,W,F",
        "--exclude",
        "tests/*",
    ]
    cfg, cfg_dir = config.load_config(flake8_config, [], isolated=True)
    optmanager.extend_default_ignore(["E8"])
    options = aggregator.aggregate_options(optmanager, cfg, cfg_dir, arguments)

    assert options.select == ["E11", "E34", "E402", "W", "F"]
    assert options.ignore is None
    assert options.exclude == [os.path.abspath("tests/*")]
```

## File: `tests/integration/test_api_legacy.py`
```python
"""Integration tests for the legacy api."""
from __future__ import annotations

from flake8.api import legacy


def test_legacy_api(tmpdir):
    """A basic end-to-end test for the legacy api reporting errors."""
    with tmpdir.as_cwd():
        t_py = tmpdir.join("t.py")
        t_py.write("import os  # unused import\n")

        style_guide = legacy.get_style_guide()
        report = style_guide.check_files([t_py.strpath])
        assert report.total_errors == 1
```

## File: `tests/integration/test_checker.py`
```python
"""Integration tests for the checker submodule."""
from __future__ import annotations

import importlib.metadata
from unittest import mock

import pytest

from flake8 import checker
from flake8.plugins import finder
from flake8.processor import FileProcessor

PHYSICAL_LINE = "# Physical line content"

EXPECTED_REPORT = (1, 1, "T000 Expected Message")
EXPECTED_REPORT_PHYSICAL_LINE = (1, "T000 Expected Message")
EXPECTED_RESULT_PHYSICAL_LINE = ("T000", 0, 1, "Expected Message", None)


class PluginClass:
    """Simple file plugin class yielding the expected report."""

    def __init__(self, tree):
        """Construct a dummy object to provide mandatory parameter."""
        pass

    def run(self):
        """Run class yielding one element containing the expected report."""
        yield EXPECTED_REPORT + (type(self),)


def plugin_func_gen(tree):
    """Yield the expected report."""
    yield EXPECTED_REPORT + (type(plugin_func_gen),)


def plugin_func_list(tree):
    """Return a list of expected reports."""
    return [EXPECTED_REPORT + (type(plugin_func_list),)]


def plugin_func_physical_ret(physical_line):
    """Expect report from a physical_line. Single return."""
    return EXPECTED_REPORT_PHYSICAL_LINE


def plugin_func_physical_none(physical_line):
    """Expect report from a physical_line. No results."""
    return None


def plugin_func_physical_list_single(physical_line):
    """Expect report from a physical_line. List of single result."""
    return [EXPECTED_REPORT_PHYSICAL_LINE]


def plugin_func_physical_list_multiple(physical_line):
    """Expect report from a physical_line. List of multiple results."""
    return [EXPECTED_REPORT_PHYSICAL_LINE] * 2


def plugin_func_physical_gen_single(physical_line):
    """Expect report from a physical_line. Generator of single result."""
    yield EXPECTED_REPORT_PHYSICAL_LINE


def plugin_func_physical_gen_multiple(physical_line):
    """Expect report from a physical_line. Generator of multiple results."""
    for _ in range(3):
        yield EXPECTED_REPORT_PHYSICAL_LINE


def plugin_func_out_of_bounds(logical_line):
    """This produces an error out of bounds."""
    yield 10000, "L100 test"


def mock_file_checker_with_plugin(plugin_target):
    """Get a mock FileChecker class with plugin_target registered.

    Useful as a starting point for mocking reports/results.
    """
    to_load = [
        finder.Plugin(
            "flake-package",
            "9001",
            importlib.metadata.EntryPoint(
                "Q",
                f"{plugin_target.__module__}:{plugin_target.__name__}",
                "flake8.extension",
            ),
        ),
    ]
    opts = finder.PluginOptions.blank()
    plugins = finder.load_plugins(to_load, opts)

    # Prevent it from reading lines from stdin or somewhere else
    with mock.patch(
        "flake8.processor.FileProcessor.read_lines", return_value=["Line 1"],
    ):
        file_checker = checker.FileChecker(
            filename="-",
            plugins=plugins.checkers,
            options=mock.MagicMock(),
        )
    return file_checker


@pytest.mark.parametrize(
    "plugin_target",
    [
        PluginClass,
        plugin_func_gen,
        plugin_func_list,
    ],
)
def test_handle_file_plugins(plugin_target):
    """Test the FileChecker class handling different file plugin types."""
    file_checker = mock_file_checker_with_plugin(plugin_target)

    # Do not actually build an AST
    file_checker.processor.build_ast = lambda: True

    # Forward reports to this mock
    report = mock.Mock()
    file_checker.report = report
    file_checker.run_ast_checks()
    report.assert_called_once_with(
        error_code=None,
        line_number=EXPECTED_REPORT[0],
        column=EXPECTED_REPORT[1],
        text=EXPECTED_REPORT[2],
    )


@pytest.mark.parametrize(
    "plugin_target,len_results",
    [
        (plugin_func_physical_ret, 1),
        (plugin_func_physical_none, 0),
        (plugin_func_physical_list_single, 1),
        (plugin_func_physical_list_multiple, 2),
        (plugin_func_physical_gen_single, 1),
        (plugin_func_physical_gen_multiple, 3),
    ],
)
def test_line_check_results(plugin_target, len_results):
    """Test the FileChecker class handling results from line checks."""
    file_checker = mock_file_checker_with_plugin(plugin_target)

    # Results will be stored in an internal array
    file_checker.run_physical_checks(PHYSICAL_LINE)
    expected = [EXPECTED_RESULT_PHYSICAL_LINE] * len_results
    assert file_checker.results == expected


def test_logical_line_offset_out_of_bounds():
    """Ensure that logical line offsets that are out of bounds do not crash."""

    file_checker = mock_file_checker_with_plugin(plugin_func_out_of_bounds)

    logical_ret = (
        "",
        'print("xxxxxxxxxxx")',
        [(0, (1, 0)), (5, (1, 5)), (6, (1, 6)), (19, (1, 19)), (20, (1, 20))],
    )
    with mock.patch.object(
        FileProcessor,
        "build_logical_line",
        return_value=logical_ret,
    ):
        file_checker.run_logical_checks()
        assert file_checker.results == [("L100", 0, 0, "test", None)]


PLACEHOLDER_CODE = 'some_line = "of" * code'


@pytest.mark.parametrize(
    "results, expected_order",
    [
        # No entries should be added
        ([], []),
        # Results are correctly ordered
        (
            [
                ("A101", 1, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 1, "placeholder error", PLACEHOLDER_CODE),
            ],
            [0, 1],
        ),
        # Reversed order of lines
        (
            [
                ("A101", 2, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 1, 1, "placeholder error", PLACEHOLDER_CODE),
            ],
            [1, 0],
        ),
        # Columns are not ordered correctly
        # (when reports are ordered correctly)
        (
            [
                ("A101", 1, 2, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 1, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 1, "placeholder error", PLACEHOLDER_CODE),
            ],
            [1, 0, 2],
        ),
        (
            [
                ("A101", 2, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 1, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 1, 2, "placeholder error", PLACEHOLDER_CODE),
            ],
            [1, 2, 0],
        ),
        (
            [
                ("A101", 1, 2, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 2, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 1, "placeholder error", PLACEHOLDER_CODE),
            ],
            [0, 2, 1],
        ),
        (
            [
                ("A101", 1, 3, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 2, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 3, 1, "placeholder error", PLACEHOLDER_CODE),
            ],
            [0, 1, 2],
        ),
        (
            [
                ("A101", 1, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 1, 3, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 2, "placeholder error", PLACEHOLDER_CODE),
            ],
            [0, 1, 2],
        ),
        # Previously sort column and message (so reversed) (see bug 196)
        (
            [
                ("A101", 1, 1, "placeholder error", PLACEHOLDER_CODE),
                ("A101", 2, 1, "charlie error", PLACEHOLDER_CODE),
            ],
            [0, 1],
        ),
    ],
)
def test_report_order(results, expected_order):
    """
    Test in which order the results will be reported.

    It gets a list of reports from the file checkers and verifies that the
    result will be ordered independent from the original report.
    """

    def count_side_effect(name, sorted_results):
        """Side effect for the result handler to tell all are reported."""
        return len(sorted_results)

    # To simplify the parameters (and prevent copy & pasting) reuse report
    # tuples to create the expected result lists from the indexes
    expected_results = [results[index] for index in expected_order]

    style_guide = mock.MagicMock(spec=["options", "processing_file"])

    # Create a placeholder manager without arguments or plugins
    # Just add one custom file checker which just provides the results
    manager = checker.Manager(style_guide, finder.Checkers([], [], []), [])
    manager.results = [("placeholder", results, {})]
    # _handle_results is the first place which gets the sorted result
    # Should something non-private be mocked instead?
    handler = mock.Mock(side_effect=count_side_effect)
    with mock.patch.object(manager, "_handle_results", handler):
        assert manager.report() == (len(results), len(results))
        handler.assert_called_once_with("placeholder", expected_results)


def test_acquire_when_multiprocessing_pool_can_initialize():
    """Verify successful importing of hardware semaphore support.

    Mock the behaviour of a platform that has a hardware sem_open
    implementation, and then attempt to initialize a multiprocessing
    Pool object.

    This simulates the behaviour on most common platforms.
    """
    with mock.patch("multiprocessing.Pool") as pool:
        result = checker._try_initialize_processpool(2, [])

    pool.assert_called_once_with(2, checker._mp_init, initargs=([],))
    assert result is pool.return_value


def test_acquire_when_multiprocessing_pool_can_not_initialize():
    """Verify unsuccessful importing of hardware semaphore support.

    Mock the behaviour of a platform that has not got a hardware sem_open
    implementation, and then attempt to initialize a multiprocessing
    Pool object.

    This scenario will occur on platforms such as Termux and on some
    more exotic devices.

    https://github.com/python/cpython/blob/4e02981de0952f54bf87967f8e10d169d6946b40/Lib/multiprocessing/synchronize.py#L30-L33
    """
    with mock.patch("multiprocessing.Pool", side_effect=ImportError) as pool:
        result = checker._try_initialize_processpool(2, [])

    pool.assert_called_once_with(2, checker._mp_init, initargs=([],))
    assert result is None


def test_handling_syntaxerrors_across_pythons():
    """Verify we properly handle exception argument tuples.

    Python 3.10 added more information to the SyntaxError parse token tuple.
    We need to handle that correctly to avoid crashing.
    https://github.com/PyCQA/flake8/issues/1372
    """
    err = SyntaxError(
        "invalid syntax", ("<unknown>", 2, 1, "bad python:\n", 2, 11),
    )
    expected = (2, 1)
    file_checker = checker.FileChecker(
        filename="-",
        plugins=finder.Checkers([], [], []),
        options=mock.MagicMock(),
    )
    actual = file_checker._extract_syntax_information(err)
    assert actual == expected
```

## File: `tests/integration/test_main.py`
```python
"""Integration tests for the main entrypoint of flake8."""
from __future__ import annotations

import json
import os
import sys
from unittest import mock

import pytest

from flake8 import utils
from flake8.main import cli
from flake8.options import config


def test_form_feed_line_split(tmpdir, capsys):
    """Test that form feed is treated the same for stdin."""
    src = "x=1\n\f\ny=1\n"
    expected_out = """\
t.py:1:2: E225 missing whitespace around operator
t.py:3:2: E225 missing whitespace around operator
"""

    with tmpdir.as_cwd():
        tmpdir.join("t.py").write(src)

        with mock.patch.object(utils, "stdin_get_value", return_value=src):
            assert cli.main(["-", "--stdin-display-name=t.py"]) == 1
            out, err = capsys.readouterr()
            assert out == expected_out
            assert err == ""

        assert cli.main(["t.py"]) == 1
        out, err = capsys.readouterr()
        assert out == expected_out
        assert err == ""


def test_e101_indent_char_does_not_reset(tmpdir, capsys):
    """Ensure that E101 with an existing indent_char does not reset it."""
    t_py_contents = """\
if True:
    print('space indented')

s = '''\
\ttab indented
'''  # noqa: E101

if True:
    print('space indented')
"""

    with tmpdir.as_cwd():
        tmpdir.join("t.py").write(t_py_contents)
        assert cli.main(["t.py"]) == 0


def test_statistics_option(tmpdir, capsys):
    """Ensure that `flake8 --statistics` works."""
    with tmpdir.as_cwd():
        tmpdir.join("t.py").write("import os\nimport sys\n")
        assert cli.main(["--statistics", "t.py"]) == 1

    expected = """\
t.py:1:1: F401 'os' imported but unused
t.py:2:1: F401 'sys' imported but unused
2     F401 'os' imported but unused
"""
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""


def test_show_source_option(tmpdir, capsys):
    """Ensure that --show-source and --no-show-source work."""
    with tmpdir.as_cwd():
        tmpdir.join("tox.ini").write("[flake8]\nshow_source = true\n")
        tmpdir.join("t.py").write("import os\n")
        assert cli.main(["t.py"]) == 1

    expected = """\
t.py:1:1: F401 'os' imported but unused
import os
^
"""
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""

    with tmpdir.as_cwd():
        assert cli.main(["t.py", "--no-show-source"]) == 1

    expected = """\
t.py:1:1: F401 'os' imported but unused
"""
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""


def test_errors_sorted(tmpdir, capsys):
    with tmpdir.as_cwd():
        for c in "abcde":
            tmpdir.join(f"{c}.py").write("import os\n")
        assert cli.main(["./"]) == 1

    # file traversal was done in inode-order before
    # this uses a significant number of files such that it's unlikely to pass
    expected = """\
./a.py:1:1: F401 'os' imported but unused
./b.py:1:1: F401 'os' imported but unused
./c.py:1:1: F401 'os' imported but unused
./d.py:1:1: F401 'os' imported but unused
./e.py:1:1: F401 'os' imported but unused
"""
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""


def test_extend_exclude(tmpdir, capsys):
    """Ensure that `flake8 --extend-exclude` works."""
    for d in ["project", "vendor", "legacy", ".git", ".tox", ".hg"]:
        tmpdir.mkdir(d).join("t.py").write("import os\nimport sys\n")

    with tmpdir.as_cwd():
        assert cli.main(["--extend-exclude=vendor,legacy/"]) == 1

    out, err = capsys.readouterr()
    expected_out = """\
./project/t.py:1:1: F401 'os' imported but unused
./project/t.py:2:1: F401 'sys' imported but unused
"""
    assert out == expected_out.replace("/", os.sep)
    assert err == ""


def test_malformed_per_file_ignores_error(tmpdir, capsys):
    """Test the error message for malformed `per-file-ignores`."""
    setup_cfg = """\
[flake8]
per-file-ignores =
    incorrect/*
    values/*
"""
    expected = """\
There was a critical error during execution of Flake8:
Expected `per-file-ignores` to be a mapping from file exclude patterns to ignore codes.

Configured `per-file-ignores` setting:

    incorrect/*
    values/*
"""  # noqa: E501

    with tmpdir.as_cwd():
        tmpdir.join("setup.cfg").write(setup_cfg)
        assert cli.main(["."]) == 1

    out, err = capsys.readouterr()
    assert out == expected


def test_tokenization_error_but_not_syntax_error(tmpdir, capsys):
    """Test that flake8 does not crash on tokenization errors."""
    with tmpdir.as_cwd():
        # this is a crash in the tokenizer, but not in the ast
        tmpdir.join("t.py").write("b'foo' \\\n")
        assert cli.main(["t.py"]) == 1

    if sys.implementation.name == "pypy":  # pragma: no cover (pypy)
        expected = "t.py:1:9: E999 SyntaxError: unexpected end of file (EOF) in multi-line statement\n"  # noqa: E501
    else:  # pragma: no cover (cp310+)
        expected = "t.py:1:10: E999 SyntaxError: unexpected EOF while parsing\n"  # noqa: E501

    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""


def test_tokenization_error_is_a_syntax_error(tmpdir, capsys):
    """Test when tokenize raises a SyntaxError."""
    with tmpdir.as_cwd():
        tmpdir.join("t.py").write("if True:\n    pass\n pass\n")
        assert cli.main(["t.py"]) == 1

    if sys.implementation.name == "pypy":  # pragma: no cover (pypy)
        expected = "t.py:3:3: E999 IndentationError: unindent does not match any outer indentation level\n"  # noqa: E501
    else:  # pragma: no cover (cp310+)
        expected = "t.py:3:7: E999 IndentationError: unindent does not match any outer indentation level\n"  # noqa: E501

    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""


def test_bug_report_successful(capsys):
    """Test that --bug-report does not crash."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(["--bug-report"])
    assert excinfo.value.args[0] == 0
    out, err = capsys.readouterr()
    assert json.loads(out)
    assert err == ""


def test_benchmark_successful(tmp_path, capsys):
    """Test that --benchmark does not crash."""
    fname = tmp_path.joinpath("t.py")
    fname.write_text("print('hello world')\n")

    assert cli.main(["--benchmark", str(fname)]) == 0

    out, err = capsys.readouterr()
    parts = [line.split(maxsplit=1) for line in out.splitlines()]
    assert parts == [
        [mock.ANY, "seconds elapsed"],
        ["1", "total logical lines processed"],
        [mock.ANY, "logical lines processed per second"],
        ["1", "total physical lines processed"],
        [mock.ANY, "physical lines processed per second"],
        ["5", "total tokens processed"],
        [mock.ANY, "tokens processed per second"],
        ["1", "total files processed"],
        [mock.ANY, "files processed per second"],
    ]
    assert err == ""


def test_specific_noqa_does_not_clobber_pycodestyle_noqa(tmpdir, capsys):
    """See https://github.com/pycqa/flake8/issues/1104."""
    with tmpdir.as_cwd():
        tmpdir.join("t.py").write("test = ('ABC' == None)  # noqa: E501\n")
        assert cli.main(["t.py"]) == 1

    expected = """\
t.py:1:15: E711 comparison to None should be 'if cond is None:'
"""
    out, err = capsys.readouterr()
    assert out == expected


def test_specific_noqa_on_line_with_continuation(tmpdir, capsys):
    """See https://github.com/pycqa/flake8/issues/621."""
    t_py_src = '''\
from os \\
    import path  # noqa: F401

x = """
    trailing whitespace: \n
"""  # noqa: W291
'''

    with tmpdir.as_cwd():
        tmpdir.join("t.py").write(t_py_src)
        assert cli.main(["t.py"]) == 0

    out, err = capsys.readouterr()
    assert out == err == ""


def test_physical_line_file_not_ending_in_newline(tmpdir, capsys):
    """See https://github.com/PyCQA/pycodestyle/issues/960."""
    t_py_src = "def f():\n\tpass"

    with tmpdir.as_cwd():
        tmpdir.join("t.py").write(t_py_src)
        assert cli.main(["t.py"]) == 1

    expected = """\
t.py:2:1: W191 indentation contains tabs
t.py:2:6: W292 no newline at end of file
"""
    out, err = capsys.readouterr()
    assert out == expected


def test_physical_line_file_not_ending_in_newline_trailing_ws(tmpdir, capsys):
    """See https://github.com/PyCQA/pycodestyle/issues/960."""
    t_py_src = "x = 1   "

    with tmpdir.as_cwd():
        tmpdir.join("t.py").write(t_py_src)
        assert cli.main(["t.py"]) == 1

    expected = """\
t.py:1:6: W291 trailing whitespace
t.py:1:9: W292 no newline at end of file
"""
    out, err = capsys.readouterr()
    assert out == expected


def test_obtaining_args_from_sys_argv_when_not_explicity_provided(capsys):
    """Test that arguments are obtained from 'sys.argv'."""
    with mock.patch("sys.argv", ["flake8", "--help"]):
        with pytest.raises(SystemExit) as excinfo:
            cli.main()
    assert excinfo.value.args[0] == 0

    out, err = capsys.readouterr()
    assert out.startswith("usage: flake8 [options] file file ...\n")
    assert err == ""


def test_cli_config_option_respected(tmp_path):
    """Test --config is used."""
    config = tmp_path / "flake8.ini"
    config.write_text(
        """\
[flake8]
ignore = F401
""",
    )

    py_file = tmp_path / "t.py"
    py_file.write_text("import os\n")

    assert cli.main(["--config", str(config), str(py_file)]) == 0


def test_cli_isolated_overrides_config_option(tmp_path):
    """Test --isolated overrides --config."""
    config = tmp_path / "flake8.ini"
    config.write_text(
        """\
[flake8]
ignore = F401
""",
    )

    py_file = tmp_path / "t.py"
    py_file.write_text("import os\n")

    assert cli.main(["--isolated", "--config", str(config), str(py_file)]) == 1


def test_file_not_found(tmpdir, capsys):
    """Ensure that a not-found file / directory is an error."""
    with tmpdir.as_cwd():
        assert cli.main(["i-do-not-exist"]) == 1
    out, err = capsys.readouterr()
    assert out.startswith("i-do-not-exist:0:1: E902")
    assert err == ""


def test_output_file(tmpdir, capsys):
    """Ensure that --output-file is honored."""
    tmpdir.join("t.py").write("import os\n")

    with tmpdir.as_cwd():
        assert cli.main(["t.py", "--output-file=a/b/f"]) == 1

    out, err = capsys.readouterr()
    assert out == err == ""

    expected = "t.py:1:1: F401 'os' imported but unused\n"
    assert tmpdir.join("a/b/f").read() == expected


def test_early_keyboard_interrupt_does_not_crash(capsys):
    with mock.patch.object(
        config, "load_config", side_effect=KeyboardInterrupt,
    ):
        assert cli.main(["does-not-exist"]) == 1
    out, err = capsys.readouterr()
    assert out == "... stopped\n"
    assert err == ""


def test_config_file_not_found(tmpdir, capsys):
    """Ensure that an explicitly specified config file which is not found is an
    error"""

    expected = """\
There was a critical error during execution of Flake8:
The specified config file does not exist: missing.cfg
"""

    with tmpdir.as_cwd():
        tmpdir.join("t.py").write("print('hello hello world')\n")
        assert cli.main(["--config", "missing.cfg", "t.py"]) == 1

    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""


def test_format_option_help(capsys):
    """Test that help displays list of available formatters."""
    with pytest.raises(SystemExit):
        cli.main(["--help"])

    out, err = capsys.readouterr()
    assert "(default, pylint, quiet-filename, quiet-nothing)" in out
    assert err == ""
```

## File: `tests/integration/test_plugins.py`
```python
"""Integration tests for plugin loading."""
from __future__ import annotations

import sys

import pytest

from flake8.main.cli import main
from flake8.main.options import register_default_options
from flake8.main.options import stage1_arg_parser
from flake8.options import aggregator
from flake8.options import config
from flake8.options.manager import OptionManager
from flake8.plugins import finder


class ExtensionTestPlugin:
    """Extension test plugin."""

    def __init__(self, tree):
        """Construct an instance of test plugin."""

    def run(self):
        """Do nothing."""

    @classmethod
    def add_options(cls, parser):
        """Register options."""
        parser.add_option("--anopt")


class ReportTestPlugin:
    """Report test plugin."""

    def __init__(self, tree):
        """Construct an instance of test plugin."""

    def run(self):
        """Do nothing."""


@pytest.fixture
def local_config(tmp_path):
    cfg_s = f"""\
[flake8:local-plugins]
extension =
    XE = {ExtensionTestPlugin.__module__}:{ExtensionTestPlugin.__name__}
report =
    XR = {ReportTestPlugin.__module__}:{ReportTestPlugin.__name__}
"""
    cfg = tmp_path.joinpath("tox.ini")
    cfg.write_text(cfg_s)

    return str(cfg)


def test_enable_local_plugin_from_config(local_config):
    """App can load a local plugin from config file."""
    cfg, cfg_dir = config.load_config(local_config, [], isolated=False)
    opts = finder.parse_plugin_options(
        cfg,
        cfg_dir,
        enable_extensions=None,
        require_plugins=None,
    )
    plugins = finder.find_plugins(cfg, opts)
    loaded_plugins = finder.load_plugins(plugins, opts)

    (custom_extension,) = (
        loaded
        for loaded in loaded_plugins.checkers.tree
        if loaded.entry_name == "XE"
    )
    custom_report = loaded_plugins.reporters["XR"]

    assert custom_extension.obj is ExtensionTestPlugin
    assert custom_report.obj is ReportTestPlugin


def test_local_plugin_can_add_option(local_config):
    """A local plugin can add a CLI option."""

    argv = ["--config", local_config, "--anopt", "foo"]

    stage1_parser = stage1_arg_parser()
    stage1_args, rest = stage1_parser.parse_known_args(argv)

    cfg, cfg_dir = config.load_config(
        config=stage1_args.config, extra=[], isolated=False,
    )

    opts = finder.parse_plugin_options(
        cfg,
        cfg_dir,
        enable_extensions=None,
        require_plugins=None,
    )
    plugins = finder.find_plugins(cfg, opts)
    loaded_plugins = finder.load_plugins(plugins, opts)

    option_manager = OptionManager(
        version="123",
        plugin_versions="",
        parents=[stage1_parser],
        formatter_names=[],
    )
    register_default_options(option_manager)
    option_manager.register_plugins(loaded_plugins)

    args = aggregator.aggregate_options(option_manager, cfg, cfg_dir, argv)

    assert args.extended_default_select == ["XE", "C90", "F", "E", "W"]
    assert args.anopt == "foo"


class AlwaysErrors:
    def __init__(self, tree):
        pass

    def run(self):
        yield 1, 0, "ABC123 error", type(self)


class AlwaysErrorsDisabled(AlwaysErrors):
    off_by_default = True


def test_plugin_gets_enabled_by_default(tmp_path, capsys):
    cfg_s = f"""\
[flake8:local-plugins]
extension =
    ABC = {AlwaysErrors.__module__}:{AlwaysErrors.__name__}
"""
    cfg = tmp_path.joinpath("tox.ini")
    cfg.write_text(cfg_s)

    t_py = tmp_path.joinpath("t.py")
    t_py.touch()

    assert main((str(t_py), "--config", str(cfg))) == 1
    out, err = capsys.readouterr()
    assert out == f"{t_py}:1:1: ABC123 error\n"
    assert err == ""


def test_plugin_off_by_default(tmp_path, capsys):
    cfg_s = f"""\
[flake8:local-plugins]
extension =
    ABC = {AlwaysErrorsDisabled.__module__}:{AlwaysErrorsDisabled.__name__}
"""
    cfg = tmp_path.joinpath("tox.ini")
    cfg.write_text(cfg_s)

    t_py = tmp_path.joinpath("t.py")
    t_py.touch()

    cmd = (str(t_py), "--config", str(cfg))

    assert main(cmd) == 0
    out, err = capsys.readouterr()
    assert out == err == ""

    assert main((*cmd, "--enable-extension=ABC")) == 1
    out, err = capsys.readouterr()
    assert out == f"{t_py}:1:1: ABC123 error\n"
    assert err == ""


def yields_physical_line(physical_line):
    yield 0, f"T001 {physical_line!r}"


def test_physical_line_plugin_multiline_string(tmpdir, capsys):
    cfg_s = f"""\
[flake8:local-plugins]
extension =
    T = {yields_physical_line.__module__}:{yields_physical_line.__name__}
"""

    cfg = tmpdir.join("tox.ini")
    cfg.write(cfg_s)

    src = '''\
x = "foo" + """
bar
"""
'''
    t_py = tmpdir.join("t.py")
    t_py.write_binary(src.encode())

    with tmpdir.as_cwd():
        assert main(("t.py", "--config", str(cfg))) == 1

    expected = '''\
t.py:1:1: T001 'x = "foo" + """\\n'
t.py:2:1: T001 'bar\\n'
t.py:3:1: T001 '"""\\n'
'''
    out, err = capsys.readouterr()
    assert out == expected


def test_physical_line_plugin_multiline_fstring(tmpdir, capsys):
    cfg_s = f"""\
[flake8:local-plugins]
extension =
    T = {yields_physical_line.__module__}:{yields_physical_line.__name__}
"""

    cfg = tmpdir.join("tox.ini")
    cfg.write(cfg_s)

    src = '''\
y = 1
x = f"""
hello {y}
"""
'''
    t_py = tmpdir.join("t.py")
    t_py.write_binary(src.encode())

    with tmpdir.as_cwd():
        assert main(("t.py", "--config", str(cfg))) == 1

    expected = '''\
t.py:1:1: T001 'y = 1\\n'
t.py:2:1: T001 'x = f"""\\n'
t.py:3:1: T001 'hello {y}\\n'
t.py:4:1: T001 '"""\\n'
'''
    out, err = capsys.readouterr()
    assert out == expected


def yields_logical_line(logical_line):
    yield 0, f"T001 {logical_line!r}"


def test_logical_line_plugin(tmpdir, capsys):
    cfg_s = f"""\
[flake8]
extend-ignore = F
[flake8:local-plugins]
extension =
    T = {yields_logical_line.__module__}:{yields_logical_line.__name__}
"""

    cfg = tmpdir.join("tox.ini")
    cfg.write(cfg_s)

    src = """\
f'hello world'
"""
    t_py = tmpdir.join("t.py")
    t_py.write_binary(src.encode())

    with tmpdir.as_cwd():
        assert main(("t.py", "--config", str(cfg))) == 1

    expected = """\
t.py:1:1: T001 "f'xxxxxxxxxxx'"
"""
    out, err = capsys.readouterr()
    assert out == expected


def test_escaping_of_fstrings_in_string_redacter(tmpdir, capsys):
    cfg_s = f"""\
[flake8]
extend-ignore = F
[flake8:local-plugins]
extension =
    T = {yields_logical_line.__module__}:{yields_logical_line.__name__}
"""

    cfg = tmpdir.join("tox.ini")
    cfg.write(cfg_s)

    src = """\
f'{{"{hello}": "{world}"}}'
"""
    t_py = tmpdir.join("t.py")
    t_py.write_binary(src.encode())

    with tmpdir.as_cwd():
        assert main(("t.py", "--config", str(cfg))) == 1

    if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
        expected = """\
t.py:1:1: T001 "f'xxx{hello}xxxx{world}xxx'"
"""
    else:  # pragma: <3.12 cover
        expected = """\
t.py:1:1: T001 "f'xxxxxxxxxxxxxxxxxxxxxxxx'"
"""
    out, err = capsys.readouterr()
    assert out == expected


@pytest.mark.xfail(sys.version_info < (3, 14), reason="3.14+")
def test_tstring_logical_line(tmpdir, capsys):  # pragma: >=3.14 cover
    cfg_s = f"""\
[flake8]
extend-ignore = F
[flake8:local-plugins]
extension =
    T = {yields_logical_line.__module__}:{yields_logical_line.__name__}
"""

    cfg = tmpdir.join("tox.ini")
    cfg.write(cfg_s)

    src = """\
t'''
hello {world}
'''
t'{{"{hello}": "{world}"}}'
"""
    t_py = tmpdir.join("t.py")
    t_py.write_binary(src.encode())

    with tmpdir.as_cwd():
        assert main(("t.py", "--config", str(cfg))) == 1

    expected = """\
t.py:1:1: T001 "t'''xxxxxxx{world}x'''"
t.py:4:1: T001 "t'xxx{hello}xxxx{world}xxx'"
"""
    out, err = capsys.readouterr()
    assert out == expected
```

## File: `tests/integration/subdir/aplugin.py`
```python
"""Module that is off sys.path by default, for testing local-plugin-paths."""
from __future__ import annotations


class ExtensionTestPlugin2:
    """Extension test plugin in its own directory."""

    def __init__(self, tree):
        """Construct an instance of test plugin."""

    def run(self):
        """Do nothing."""
```

## File: `tests/unit/conftest.py`
```python
"""Shared fixtures between unit tests."""
from __future__ import annotations

import argparse

import pytest


def options_from(**kwargs):
    """Generate a Values instances with our kwargs."""
    kwargs.setdefault("hang_closing", True)
    kwargs.setdefault("max_line_length", 79)
    kwargs.setdefault("max_doc_length", None)
    kwargs.setdefault("indent_size", 4)
    kwargs.setdefault("verbose", 0)
    kwargs.setdefault("stdin_display_name", "stdin")
    kwargs.setdefault("disable_noqa", False)
    return argparse.Namespace(**kwargs)


@pytest.fixture
def default_options():
    """Fixture returning the default options of flake8."""
    return options_from()
```

## File: `tests/unit/test_application.py`
```python
"""Tests for the Application class."""
from __future__ import annotations

import argparse

import pytest

from flake8.main import application as app


def options(**kwargs):
    """Generate argparse.Namespace for our Application."""
    kwargs.setdefault("verbose", 0)
    kwargs.setdefault("output_file", None)
    kwargs.setdefault("count", False)
    kwargs.setdefault("exit_zero", False)
    return argparse.Namespace(**kwargs)


@pytest.fixture
def application():
    """Create an application."""
    return app.Application()


@pytest.mark.parametrize(
    "result_count, catastrophic, exit_zero, value",
    [
        (0, False, False, 0),
        (0, True, False, 1),
        (2, False, False, 1),
        (2, True, False, 1),
        (0, True, True, 1),
        (2, False, True, 0),
        (2, True, True, 1),
    ],
)
def test_application_exit_code(
    result_count, catastrophic, exit_zero, value, application,
):
    """Verify Application.exit_code returns the correct value."""
    application.result_count = result_count
    application.catastrophic_failure = catastrophic
    application.options = options(exit_zero=exit_zero)

    assert application.exit_code() == value
```

## File: `tests/unit/test_base_formatter.py`
```python
"""Tests for the BaseFormatter object."""
from __future__ import annotations

import argparse
import sys
from unittest import mock

import pytest

from flake8.formatting import _windows_color
from flake8.formatting import base
from flake8.violation import Violation


def options(**kwargs):
    """Create an argparse.Namespace instance."""
    kwargs.setdefault("color", "auto")
    kwargs.setdefault("output_file", None)
    kwargs.setdefault("tee", False)
    return argparse.Namespace(**kwargs)


@pytest.mark.parametrize("filename", [None, "out.txt"])
def test_start(filename):
    """Verify we open a new file in the start method."""
    mock_open = mock.mock_open()
    formatter = base.BaseFormatter(options(output_file=filename))
    with mock.patch("flake8.formatting.base.open", mock_open):
        formatter.start()

    if filename is None:
        assert mock_open.called is False
    else:
        mock_open.assert_called_once_with(filename, "a")


def test_stop():
    """Verify we close open file objects."""
    filemock = mock.Mock()
    formatter = base.BaseFormatter(options())
    formatter.output_fd = filemock
    formatter.stop()

    filemock.close.assert_called_once_with()
    assert formatter.output_fd is None


def test_format_needs_to_be_implemented():
    """Ensure BaseFormatter#format raises a NotImplementedError."""
    formatter = base.BaseFormatter(options())
    with pytest.raises(NotImplementedError):
        formatter.format(
            Violation("A000", "file.py", 1, 1, "error text", None),
        )


def test_show_source_returns_nothing_when_not_showing_source():
    """Ensure we return nothing when users want nothing."""
    formatter = base.BaseFormatter(options(show_source=False))
    assert (
        formatter.show_source(
            Violation("A000", "file.py", 1, 1, "error text", "line"),
        )
        == ""
    )


def test_show_source_returns_nothing_when_there_is_source():
    """Ensure we return nothing when there is no line."""
    formatter = base.BaseFormatter(options(show_source=True))
    assert (
        formatter.show_source(
            Violation("A000", "file.py", 1, 1, "error text", None),
        )
        == ""
    )


@pytest.mark.parametrize(
    ("line1", "line2", "column"),
    [
        (
            "x=1\n",
            " ^",
            2,
        ),
        (
            "    x=(1\n       +2)\n",
            "    ^",
            5,
        ),
        (
            "\tx\t=\ty\n",
            "\t \t \t^",
            6,
        ),
    ],
)
def test_show_source_updates_physical_line_appropriately(line1, line2, column):
    """Ensure the error column is appropriately indicated."""
    formatter = base.BaseFormatter(options(show_source=True))
    error = Violation("A000", "file.py", 1, column, "error", line1)
    output = formatter.show_source(error)
    assert output == line1 + line2


@pytest.mark.parametrize("tee", [False, True])
def test_write_uses_an_output_file(tee, capsys):
    """Verify that we use the output file when it's present."""
    line = "Something to write"
    source = "source"
    filemock = mock.Mock()

    formatter = base.BaseFormatter(options(tee=tee))
    formatter.output_fd = filemock

    formatter.write(line, source)
    if tee:
        assert capsys.readouterr().out == f"{line}\n{source}\n"
    else:
        assert capsys.readouterr().out == ""

    assert filemock.write.called is True
    assert filemock.write.call_count == 2
    assert filemock.write.mock_calls == [
        mock.call(line + formatter.newline),
        mock.call(source + formatter.newline),
    ]


def test_write_produces_stdout(capsys):
    """Verify that we write to stdout without an output file."""
    line = "Something to write"
    source = "source"

    formatter = base.BaseFormatter(options())
    formatter.write(line, source)

    assert capsys.readouterr().out == f"{line}\n{source}\n"


def test_color_always_is_true():
    """Verify that color='always' sets it to True."""
    formatter = base.BaseFormatter(options(color="always"))
    assert formatter.color is True


def _mock_isatty(val):
    attrs = {"isatty.return_value": val}
    return mock.patch.object(sys, "stdout", **attrs)


def _mock_windows_color(val):
    return mock.patch.object(_windows_color, "terminal_supports_color", val)


def test_color_auto_is_true_for_tty():
    """Verify that color='auto' sets it to True for a tty."""
    with _mock_isatty(True), _mock_windows_color(True):
        formatter = base.BaseFormatter(options(color="auto"))
    assert formatter.color is True


def test_color_auto_is_false_without_tty():
    """Verify that color='auto' sets it to False without a tty."""
    with _mock_isatty(False), _mock_windows_color(True):
        formatter = base.BaseFormatter(options(color="auto"))
    assert formatter.color is False


def test_color_auto_is_false_if_not_supported_on_windows():
    """Verify that color='auto' is False if not supported on windows."""
    with _mock_isatty(True), _mock_windows_color(False):
        formatter = base.BaseFormatter(options(color="auto"))
    assert formatter.color is False


def test_color_never_is_false():
    """Verify that color='never' sets it to False despite a tty."""
    with _mock_isatty(True), _mock_windows_color(True):
        formatter = base.BaseFormatter(options(color="never"))
    assert formatter.color is False


class AfterInitFormatter(base.BaseFormatter):
    """Subclass for testing after_init."""

    def after_init(self):
        """Define method to verify operation."""
        self.post_initialized = True


def test_after_init_is_always_called():
    """Verify after_init is called."""
    formatter = AfterInitFormatter(options())
    assert formatter.post_initialized is True


class FormatFormatter(base.BaseFormatter):
    """Subclass for testing format."""

    def format(self, error):
        """Define method to verify operation."""
        return repr(error)


def test_handle_formats_the_error():
    """Verify that a formatter will call format from handle."""
    formatter = FormatFormatter(options(show_source=False))
    filemock = formatter.output_fd = mock.Mock()
    error = Violation(
        code="A001",
        filename="example.py",
        line_number=1,
        column_number=1,
        text="Fake error",
        physical_line="a = 1",
    )

    formatter.handle(error)

    filemock.write.assert_called_once_with(repr(error) + "\n")
```

## File: `tests/unit/test_checker_manager.py`
```python
"""Tests for the Manager object for FileCheckers."""
from __future__ import annotations

import errno
import multiprocessing
from unittest import mock

import pytest

from flake8 import checker
from flake8.main.options import JobsArgument
from flake8.plugins import finder


def style_guide_mock():
    """Create a mock StyleGuide object."""
    return mock.MagicMock(**{"options.jobs": JobsArgument("4")})


def _parallel_checker_manager():
    """Call Manager.run() and return the number of calls to `run_serial`."""
    style_guide = style_guide_mock()
    manager = checker.Manager(style_guide, finder.Checkers([], [], []), [])
    # multiple files is needed for parallel mode
    manager.filenames = ("file1", "file2")
    return manager


def test_oserrors_cause_serial_fall_back():
    """Verify that OSErrors will cause the Manager to fallback to serial."""
    err = OSError(errno.ENOSPC, "Ominous message about spaceeeeee")
    with mock.patch("_multiprocessing.SemLock", side_effect=err):
        manager = _parallel_checker_manager()
        with mock.patch.object(manager, "run_serial") as serial:
            manager.run()
    assert serial.call_count == 1


def test_oserrors_are_reraised():
    """Verify that unexpected OSErrors will cause the Manager to reraise."""
    err = OSError(errno.EAGAIN, "Ominous message")
    with mock.patch("_multiprocessing.SemLock", side_effect=err):
        manager = _parallel_checker_manager()
        with (
            mock.patch.object(manager, "run_serial") as serial,
            pytest.raises(OSError),
        ):
            manager.run()
    assert serial.call_count == 0


def test_multiprocessing_cpu_count_not_implemented():
    """Verify that jobs is 0 if cpu_count is unavailable."""
    style_guide = style_guide_mock()
    style_guide.options.jobs = JobsArgument("auto")

    with mock.patch.object(
        multiprocessing,
        "cpu_count",
        side_effect=NotImplementedError,
    ):
        manager = checker.Manager(style_guide, finder.Checkers([], [], []), [])
    assert manager.jobs == 0


def test_jobs_count_limited_to_file_count():
    style_guide = style_guide_mock()
    style_guide.options.jobs = JobsArgument("4")
    style_guide.options.filenames = ["file1", "file2"]
    manager = checker.Manager(style_guide, finder.Checkers([], [], []), [])
    assert manager.jobs == 4
    manager.start()
    assert manager.jobs == 2


def test_make_checkers():
    """Verify that we create a list of FileChecker instances."""
    style_guide = style_guide_mock()
    style_guide.options.filenames = ["file1", "file2"]
    manager = checker.Manager(style_guide, finder.Checkers([], [], []), [])
    manager.start()
    assert manager.filenames == ("file1", "file2")
```

## File: `tests/unit/test_debug.py`
```python
from __future__ import annotations

import importlib.metadata
from unittest import mock

from flake8.main import debug
from flake8.plugins import finder


def test_debug_information():
    def _plugin(pkg, version, ep_name):
        return finder.LoadedPlugin(
            finder.Plugin(
                pkg,
                version,
                importlib.metadata.EntryPoint(
                    ep_name, "dne:dne", "flake8.extension",
                ),
            ),
            None,
            {},
        )

    plugins = finder.Plugins(
        checkers=finder.Checkers(
            tree=[
                _plugin("pkg1", "1.2.3", "X1"),
                _plugin("pkg1", "1.2.3", "X2"),
                _plugin("pkg2", "4.5.6", "X3"),
            ],
            logical_line=[],
            physical_line=[],
        ),
        reporters={},
        disabled=[],
    )

    info = debug.information("9001", plugins)
    assert info == {
        "version": "9001",
        "plugins": [
            {"plugin": "pkg1", "version": "1.2.3"},
            {"plugin": "pkg2", "version": "4.5.6"},
        ],
        "platform": {
            "python_implementation": mock.ANY,
            "python_version": mock.ANY,
            "system": mock.ANY,
        },
    }
```

## File: `tests/unit/test_decision_engine.py`
```python
"""Tests for the flake8.style_guide.DecisionEngine class."""
from __future__ import annotations

import argparse

import pytest

from flake8 import style_guide


def create_options(**kwargs):
    """Create and return an instance of argparse.Namespace."""
    kwargs.setdefault("select", None)
    kwargs.setdefault("ignore", None)
    kwargs.setdefault("extend_select", None)
    kwargs.setdefault("extend_ignore", None)
    kwargs.setdefault("extended_default_select", ["C90", "F", "E", "W"])
    kwargs.setdefault("extended_default_ignore", [])
    kwargs.setdefault("disable_noqa", False)
    return argparse.Namespace(**kwargs)


@pytest.mark.parametrize(
    "ignore_list,extend_ignore,error_code",
    [
        (["E111", "E121"], [], "E111"),
        (["E111", "E121"], [], "E121"),
        (["E111"], ["E121"], "E121"),
        (["E11", "E12"], [], "E121"),
        (["E2", "E12"], [], "E121"),
        (["E2", "E12"], [], "E211"),
        (["E2", "E3"], ["E12"], "E211"),
    ],
)
def test_was_ignored_ignores_errors(ignore_list, extend_ignore, error_code):
    """Verify we detect users explicitly ignoring an error."""
    decider = style_guide.DecisionEngine(
        create_options(ignore=ignore_list, extend_ignore=extend_ignore),
    )

    assert decider.was_ignored(error_code) is style_guide.Ignored.Explicitly


@pytest.mark.parametrize(
    "ignore_list,extend_ignore,error_code",
    [
        (["E111", "E121"], [], "E112"),
        (["E111", "E121"], [], "E122"),
        (["E11", "E12"], ["E121"], "W121"),
        (["E2", "E12"], [], "E112"),
        (["E2", "E12"], [], "E111"),
        (["E2", "E12"], ["W11", "E3"], "E111"),
    ],
)
def test_was_ignored_implicitly_selects_errors(
    ignore_list, extend_ignore, error_code,
):
    """Verify we detect users does not explicitly ignore an error."""
    decider = style_guide.DecisionEngine(
        create_options(ignore=ignore_list, extend_ignore=extend_ignore),
    )

    assert decider.was_ignored(error_code) is style_guide.Selected.Implicitly


@pytest.mark.parametrize(
    ("select_list", "extend_select", "error_code"),
    (
        (["E111", "E121"], [], "E111"),
        (["E111", "E121"], [], "E121"),
        (["E11", "E12"], [], "E121"),
        (["E2", "E12"], [], "E121"),
        (["E2", "E12"], [], "E211"),
        (["E1"], ["E2"], "E211"),
        ([], ["E2"], "E211"),
        (["E1"], ["E2"], "E211"),
        (["E111"], ["E121"], "E121"),
    ),
)
def test_was_selected_selects_errors(select_list, extend_select, error_code):
    """Verify we detect users explicitly selecting an error."""
    decider = style_guide.DecisionEngine(
        options=create_options(
            select=select_list,
            extend_select=extend_select,
        ),
    )

    assert decider.was_selected(error_code) is style_guide.Selected.Explicitly


def test_was_selected_implicitly_selects_errors():
    """Verify we detect users implicitly selecting an error."""
    error_code = "E121"
    decider = style_guide.DecisionEngine(
        create_options(
            select=None,
            extended_default_select=["E"],
        ),
    )

    assert decider.was_selected(error_code) is style_guide.Selected.Implicitly


@pytest.mark.parametrize(
    "select_list,error_code",
    [
        (["E111", "E121"], "E112"),
        (["E111", "E121"], "E122"),
        (["E11", "E12"], "E132"),
        (["E2", "E12"], "E321"),
        (["E2", "E12"], "E410"),
    ],
)
def test_was_selected_excludes_errors(select_list, error_code):
    """Verify we detect users implicitly excludes an error."""
    decider = style_guide.DecisionEngine(create_options(select=select_list))

    assert decider.was_selected(error_code) is style_guide.Ignored.Implicitly


@pytest.mark.parametrize(
    "select_list,ignore_list,extend_ignore,error_code,expected",
    [
        (["E111", "E121"], [], None, "E111", style_guide.Decision.Selected),
        (["E111", "E121"], [], None, "E112", style_guide.Decision.Ignored),
        (["E111", "E121"], [], None, "E121", style_guide.Decision.Selected),
        (["E111", "E121"], [], None, "E122", style_guide.Decision.Ignored),
        (["E11", "E12"], [], None, "E132", style_guide.Decision.Ignored),
        (["E2", "E12"], [], None, "E321", style_guide.Decision.Ignored),
        (["E2", "E12"], [], None, "E410", style_guide.Decision.Ignored),
        (["E11", "E121"], ["E1"], [], "E112", style_guide.Decision.Selected),
        (["E11", "E121"], [], ["E1"], "E112", style_guide.Decision.Selected),
        (
            ["E111", "E121"],
            ["E2"],
            ["E3"],
            "E122",
            style_guide.Decision.Ignored,
        ),
        (["E11", "E12"], ["E13"], None, "E132", style_guide.Decision.Ignored),
        (["E1", "E3"], ["E32"], None, "E321", style_guide.Decision.Ignored),
        ([], ["E2", "E12"], None, "E410", style_guide.Decision.Ignored),
        (
            ["E4"],
            ["E2", "E12", "E41"],
            None,
            "E410",
            style_guide.Decision.Ignored,
        ),
        (
            ["E41"],
            ["E2", "E12", "E4"],
            None,
            "E410",
            style_guide.Decision.Selected,
        ),
        (["E"], ["F"], None, "E410", style_guide.Decision.Selected),
        (["F"], [], None, "E410", style_guide.Decision.Ignored),
        (["E"], None, None, "E126", style_guide.Decision.Selected),
        (["W"], None, None, "E126", style_guide.Decision.Ignored),
        (["E"], None, None, "W391", style_guide.Decision.Ignored),
        (["E", "W"], ["E13"], None, "E131", style_guide.Decision.Ignored),
        (None, ["E13"], None, "E131", style_guide.Decision.Ignored),
        (
            None,
            None,
            ["W391"],
            "E126",
            style_guide.Decision.Ignored,
        ),
        (
            None,
            None,
            None,
            "W391",
            style_guide.Decision.Selected,
        ),
    ],
)
def test_decision_for(
    select_list, ignore_list, extend_ignore, error_code, expected,
):
    """Verify we decide when to report an error."""
    decider = style_guide.DecisionEngine(
        create_options(
            select=select_list,
            ignore=ignore_list,
            extend_ignore=extend_ignore,
        ),
    )

    assert decider.decision_for(error_code) is expected


def test_implicitly_selected_and_implicitly_ignored_defers_to_length():
    decider = style_guide.DecisionEngine(
        create_options(
            # no options selected by user
            select=None,
            ignore=None,
            extend_select=None,
            extend_ignore=None,
            # a plugin is installed and extends default ignore
            extended_default_select=["P"],
            extended_default_ignore=["P002"],
        ),
    )

    assert decider.decision_for("P001") is style_guide.Decision.Selected
    assert decider.decision_for("P002") is style_guide.Decision.Ignored


def test_user_can_extend_select_to_enable_plugin_default_ignored():
    decider = style_guide.DecisionEngine(
        create_options(
            # user options --extend-select=P002
            select=None,
            ignore=None,
            extend_select=["P002"],
            extend_ignore=None,
            # a plugin is installed and extends default ignore
            extended_default_select=["P"],
            extended_default_ignore=["P002"],
        ),
    )

    assert decider.decision_for("P002") is style_guide.Decision.Selected


def test_plugin_extends_default_ignore_but_extend_selected():
    decider = style_guide.DecisionEngine(
        create_options(
            # user options --extend-select P002 --extend-ignore E501
            select=None,
            ignore=None,
            extend_select=["P002"],
            extend_ignore=["E501"],
            # a plugin is installed and extends default ignore
            extended_default_select=["P"],
            extended_default_ignore=["P002"],
        ),
    )

    assert decider.decision_for("P002") is style_guide.Decision.Selected
```

## File: `tests/unit/test_defaults.py`
```python
from __future__ import annotations

import pytest

from flake8.defaults import VALID_CODE_PREFIX


@pytest.mark.parametrize(
    "s",
    (
        "E",
        "E1",
        "E123",
        "ABC",
        "ABC1",
        "ABC123",
    ),
)
def test_valid_plugin_prefixes(s):
    assert VALID_CODE_PREFIX.match(s)


@pytest.mark.parametrize(
    "s",
    (
        "",
        "A1234",
        "ABCD",
        "abc",
        "a-b",
        "☃",
        "A𝟗",
    ),
)
def test_invalid_plugin_prefixes(s):
    assert VALID_CODE_PREFIX.match(s) is None
```

## File: `tests/unit/test_discover_files.py`
```python
from __future__ import annotations

import os.path

import pytest

from flake8 import utils
from flake8.discover_files import _filenames_from
from flake8.discover_files import expand_paths


@pytest.fixture
def files_dir(tmpdir):
    """Create test dir for testing filenames_from."""
    with tmpdir.as_cwd():
        tmpdir.join("a/b/c.py").ensure()
        tmpdir.join("a/b/d.py").ensure()
        tmpdir.join("a/b/e/f.py").ensure()
        yield tmpdir


def _noop(path):
    return False


def _normpath(s):
    return s.replace("/", os.sep)


def _normpaths(pths):
    return {_normpath(pth) for pth in pths}


@pytest.mark.usefixtures("files_dir")
def test_filenames_from_a_directory():
    """Verify that filenames_from walks a directory."""
    filenames = set(_filenames_from(_normpath("a/b/"), predicate=_noop))
    # should include all files
    expected = _normpaths(("a/b/c.py", "a/b/d.py", "a/b/e/f.py"))
    assert filenames == expected


@pytest.mark.usefixtures("files_dir")
def test_filenames_from_a_directory_with_a_predicate():
    """Verify that predicates filter filenames_from."""
    filenames = set(
        _filenames_from(
            arg=_normpath("a/b/"),
            predicate=lambda path: path.endswith(_normpath("b/c.py")),
        ),
    )
    # should not include c.py
    expected = _normpaths(("a/b/d.py", "a/b/e/f.py"))
    assert filenames == expected


@pytest.mark.usefixtures("files_dir")
def test_filenames_from_a_directory_with_a_predicate_from_the_current_dir():
    """Verify that predicates filter filenames_from."""
    filenames = set(
        _filenames_from(
            arg=_normpath("./a/b"),
            predicate=lambda path: path == "c.py",
        ),
    )
    # none should have matched the predicate so all returned
    expected = _normpaths(("./a/b/c.py", "./a/b/d.py", "./a/b/e/f.py"))
    assert filenames == expected


@pytest.mark.usefixtures("files_dir")
def test_filenames_from_a_single_file():
    """Verify that we simply yield that filename."""
    filenames = set(_filenames_from(_normpath("a/b/c.py"), predicate=_noop))
    assert filenames == {_normpath("a/b/c.py")}


def test_filenames_from_a_single_file_does_not_exist():
    """Verify that a passed filename which does not exist is returned back."""
    filenames = set(_filenames_from(_normpath("d/n/e.py"), predicate=_noop))
    assert filenames == {_normpath("d/n/e.py")}


def test_filenames_from_exclude_doesnt_exclude_directory_names(tmpdir):
    """Verify that we don't greedily exclude subdirs."""
    tmpdir.join("1/dont_return_me.py").ensure()
    tmpdir.join("2/1/return_me.py").ensure()
    exclude = [tmpdir.join("1").strpath]

    def predicate(pth):
        return utils.fnmatch(os.path.abspath(pth), exclude)

    with tmpdir.as_cwd():
        filenames = list(_filenames_from(".", predicate=predicate))
    assert filenames == [os.path.join(".", "2", "1", "return_me.py")]


def test_filenames_from_predicate_applies_to_initial_arg(tmp_path):
    """Test that the predicate is also applied to the passed argument."""
    fname = str(tmp_path.joinpath("f.py"))
    ret = tuple(_filenames_from(fname, predicate=lambda _: True))
    assert ret == ()


def test_filenames_from_predicate_applies_to_dirname(tmp_path):
    """Test that the predicate can filter whole directories."""
    a_dir = tmp_path.joinpath("a")
    a_dir.mkdir()
    a_dir.joinpath("b.py").touch()

    b_py = tmp_path.joinpath("b.py")
    b_py.touch()

    def predicate(p):
        # filter out the /a directory
        return p.endswith("a")

    ret = tuple(_filenames_from(str(tmp_path), predicate=predicate))
    assert ret == (str(b_py),)


def _expand_paths(
    *,
    paths=(".",),
    stdin_display_name="stdin",
    filename_patterns=("*.py",),
    exclude=(),
):
    return set(
        expand_paths(
            paths=paths,
            stdin_display_name=stdin_display_name,
            filename_patterns=filename_patterns,
            exclude=exclude,
        ),
    )


@pytest.mark.usefixtures("files_dir")
def test_expand_paths_honors_exclude():
    expected = _normpaths(("./a/b/c.py", "./a/b/e/f.py"))
    assert _expand_paths(exclude=["d.py"]) == expected


@pytest.mark.usefixtures("files_dir")
def test_expand_paths_defaults_to_dot():
    expected = _normpaths(("./a/b/c.py", "./a/b/d.py", "./a/b/e/f.py"))
    assert _expand_paths(paths=()) == expected


def test_default_stdin_name_is_not_filtered():
    assert _expand_paths(paths=("-",)) == {"-"}


def test_alternate_stdin_name_is_filtered():
    ret = _expand_paths(
        paths=("-",),
        stdin_display_name="wat",
        exclude=("wat",),
    )
    assert ret == set()


def test_filename_included_even_if_not_matching_include(tmp_path):
    some_file = str(tmp_path.joinpath("some/file"))
    assert _expand_paths(paths=(some_file,)) == {some_file}
```

## File: `tests/unit/test_exceptions.py`
```python
"""Tests for the flake8.exceptions module."""
from __future__ import annotations

import pickle

import pytest

from flake8 import exceptions


@pytest.mark.parametrize(
    "err",
    (
        exceptions.FailedToLoadPlugin(
            plugin_name="plugin_name",
            exception=ValueError("boom!"),
        ),
        exceptions.PluginRequestedUnknownParameters(
            plugin_name="plugin_name",
            exception=ValueError("boom!"),
        ),
        exceptions.PluginExecutionFailed(
            filename="filename.py",
            plugin_name="plugin_name",
            exception=ValueError("boom!"),
        ),
    ),
)
def test_pickleable(err):
    """Ensure that our exceptions can cross pickle boundaries."""
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        new_err = pickle.loads(pickle.dumps(err, protocol=proto))
        assert str(err) == str(new_err)
        orig_e = err.original_exception
        new_e = new_err.original_exception
        assert (type(orig_e), orig_e.args) == (type(new_e), new_e.args)
```

## File: `tests/unit/test_file_checker.py`
```python
"""Unit tests for the FileChecker class."""
from __future__ import annotations

import argparse
import importlib.metadata
from unittest import mock

import pytest

import flake8
from flake8 import checker
from flake8.plugins import finder


@mock.patch("flake8.checker.FileChecker._make_processor", return_value=None)
def test_repr(*args):
    """Verify we generate a correct repr."""
    file_checker = checker.FileChecker(
        filename="example.py",
        plugins=finder.Checkers([], [], []),
        options=argparse.Namespace(),
    )
    assert repr(file_checker) == "FileChecker for example.py"


def test_nonexistent_file():
    """Verify that checking non-existent file results in an error."""
    c = checker.FileChecker(
        filename="example.py",
        plugins=finder.Checkers([], [], []),
        options=argparse.Namespace(),
    )

    assert c.processor is None
    assert not c.should_process
    assert len(c.results) == 1
    error = c.results[0]
    assert error[0] == "E902"


def test_raises_exception_on_failed_plugin(tmp_path, default_options):
    """Checks that a failing plugin results in PluginExecutionFailed."""
    fname = tmp_path.joinpath("t.py")
    fname.touch()
    plugin = finder.LoadedPlugin(
        finder.Plugin(
            "plugin-name",
            "1.2.3",
            importlib.metadata.EntryPoint("X", "dne:dne", "flake8.extension"),
        ),
        mock.Mock(side_effect=ValueError),
        {},
    )
    fchecker = checker.FileChecker(
        filename=str(fname),
        plugins=finder.Checkers([], [], []),
        options=default_options,
    )
    with pytest.raises(flake8.exceptions.PluginExecutionFailed) as excinfo:
        fchecker.run_check(plugin)
    expected = (
        f'{fname}: "plugin-name[X]" failed during execution '
        f"due to ValueError()"
    )
    assert str(excinfo.value) == expected
```

## File: `tests/unit/test_file_processor.py`
```python
"""Tests for the FileProcessor class."""
from __future__ import annotations

import ast
import tokenize
from unittest import mock

import pytest

from flake8 import processor


def test_read_lines_splits_lines(default_options):
    """Verify that read_lines splits the lines of the file."""
    file_processor = processor.FileProcessor(__file__, default_options)
    lines = file_processor.lines
    assert len(lines) > 5
    assert lines[0].strip() == '"""Tests for the FileProcessor class."""'


def _lines_from_file(tmpdir, contents, options):
    f = tmpdir.join("f.py")
    # be careful to write the bytes exactly to avoid newline munging
    f.write_binary(contents)
    return processor.FileProcessor(f.strpath, options).lines


def test_read_lines_universal_newlines(tmpdir, default_options):
    r"""Verify that line endings are translated to \n."""
    lines = _lines_from_file(
        tmpdir, b"# coding: utf-8\r\nx = 1\r\n", default_options,
    )
    assert lines == ["# coding: utf-8\n", "x = 1\n"]


def test_read_lines_incorrect_utf_16(tmpdir, default_options):
    """Verify that an incorrectly encoded file is read as latin-1."""
    lines = _lines_from_file(
        tmpdir, b"# coding: utf16\nx = 1\n", default_options,
    )
    assert lines == ["# coding: utf16\n", "x = 1\n"]


def test_read_lines_unknown_encoding(tmpdir, default_options):
    """Verify that an unknown encoding is still read as latin-1."""
    lines = _lines_from_file(
        tmpdir, b"# coding: fake-encoding\nx = 1\n", default_options,
    )
    assert lines == ["# coding: fake-encoding\n", "x = 1\n"]


@pytest.mark.parametrize(
    "first_line",
    [
        '\xEF\xBB\xBF"""Module docstring."""\n',
        '\uFEFF"""Module docstring."""\n',
    ],
)
def test_strip_utf_bom(first_line, default_options):
    r"""Verify that we strip '\xEF\xBB\xBF' from the first line."""
    lines = [first_line]
    file_processor = processor.FileProcessor("-", default_options, lines[:])
    assert file_processor.lines != lines
    assert file_processor.lines[0] == '"""Module docstring."""\n'


@pytest.mark.parametrize(
    "lines, expected",
    [
        (['\xEF\xBB\xBF"""Module docstring."""\n'], False),
        (['\uFEFF"""Module docstring."""\n'], False),
        (["#!/usr/bin/python", "# flake8 is great", "a = 1"], False),
        (["#!/usr/bin/python", "# flake8: noqa", "a = 1"], True),
        (["#!/usr/bin/python", "# flake8:noqa", "a = 1"], True),
        (["# flake8: noqa", "#!/usr/bin/python", "a = 1"], True),
        (["# flake8:noqa", "#!/usr/bin/python", "a = 1"], True),
        (["#!/usr/bin/python", "a = 1", "# flake8: noqa"], True),
        (["#!/usr/bin/python", "a = 1", "# flake8:noqa"], True),
        (["#!/usr/bin/python", "a = 1  # flake8: noqa"], False),
        (["#!/usr/bin/python", "a = 1  # flake8:noqa"], False),
    ],
)
def test_should_ignore_file(lines, expected, default_options):
    """Verify that we ignore a file if told to."""
    file_processor = processor.FileProcessor("-", default_options, lines)
    assert file_processor.should_ignore_file() is expected


def test_should_ignore_file_to_handle_disable_noqa(default_options):
    """Verify that we ignore a file if told to."""
    lines = ["# flake8: noqa"]
    file_processor = processor.FileProcessor("-", default_options, lines)
    assert file_processor.should_ignore_file() is True
    default_options.disable_noqa = True
    file_processor = processor.FileProcessor("-", default_options, lines)
    assert file_processor.should_ignore_file() is False


@mock.patch("flake8.utils.stdin_get_value")
def test_read_lines_from_stdin(stdin_get_value, default_options):
    """Verify that we use our own utility function to retrieve stdin."""
    stdin_get_value.return_value = ""
    processor.FileProcessor("-", default_options)
    stdin_get_value.assert_called_once_with()


@mock.patch("flake8.utils.stdin_get_value")
def test_stdin_filename_attribute(stdin_get_value, default_options):
    """Verify that we update the filename attribute."""
    stdin_get_value.return_value = ""
    file_processor = processor.FileProcessor("-", default_options)
    assert file_processor.filename == "stdin"


@mock.patch("flake8.utils.stdin_get_value")
def test_read_lines_uses_display_name(stdin_get_value, default_options):
    """Verify that when processing stdin we use a display name if present."""
    default_options.stdin_display_name = "display_name.py"
    stdin_get_value.return_value = ""
    file_processor = processor.FileProcessor("-", default_options)
    assert file_processor.filename == "display_name.py"


@mock.patch("flake8.utils.stdin_get_value")
def test_read_lines_ignores_empty_display_name(
    stdin_get_value,
    default_options,
):
    """Verify that when processing stdin we use a display name if present."""
    stdin_get_value.return_value = ""
    default_options.stdin_display_name = ""
    file_processor = processor.FileProcessor("-", default_options)
    assert file_processor.filename == "stdin"


def test_noqa_line_for(default_options):
    """Verify we grab the correct line from the cached lines."""
    file_processor = processor.FileProcessor(
        "-",
        default_options,
        lines=[
            "Line 1\n",
            "Line 2\n",
            "Line 3\n",
        ],
    )

    for i in range(1, 4):
        assert file_processor.noqa_line_for(i) == f"Line {i}\n"


def test_noqa_line_for_continuation(default_options):
    """Verify that the correct "line" is retrieved for continuation."""
    src = '''\
from foo \\
    import bar  # 2

x = """
hello
world
"""  # 7
'''
    lines = src.splitlines(True)
    file_processor = processor.FileProcessor("-", default_options, lines=lines)

    assert file_processor.noqa_line_for(0) is None

    l_1_2 = "from foo \\\n    import bar  # 2\n"
    assert file_processor.noqa_line_for(1) == l_1_2
    assert file_processor.noqa_line_for(2) == l_1_2

    assert file_processor.noqa_line_for(3) == "\n"

    l_4_7 = 'x = """\nhello\nworld\n"""  # 7\n'
    for i in (4, 5, 6, 7):
        assert file_processor.noqa_line_for(i) == l_4_7

    assert file_processor.noqa_line_for(8) is None


def test_noqa_line_for_no_eol_at_end_of_file(default_options):
    """Verify that we properly handle noqa line at the end of the file."""
    src = "from foo \\\nimport bar"  # no end of file newline
    lines = src.splitlines(True)
    file_processor = processor.FileProcessor("-", default_options, lines=lines)

    l_1_2 = "from foo \\\nimport bar"
    assert file_processor.noqa_line_for(1) == l_1_2
    assert file_processor.noqa_line_for(2) == l_1_2


def test_next_line(default_options):
    """Verify we update the file_processor state for each new line."""
    file_processor = processor.FileProcessor(
        "-",
        default_options,
        lines=[
            "Line 1",
            "Line 2",
            "Line 3",
        ],
    )

    for i in range(1, 4):
        assert file_processor.next_line() == f"Line {i}"
        assert file_processor.line_number == i


@pytest.mark.parametrize(
    "params, args, expected_kwargs",
    [
        (
            {"blank_before": True, "blank_lines": True},
            {},
            {"blank_before": 0, "blank_lines": 0},
        ),
        (
            {"noqa": True, "fake": True},
            {"fake": "foo"},
            {"noqa": False},
        ),
        (
            {"blank_before": True, "blank_lines": True, "noqa": True},
            {"blank_before": 10, "blank_lines": 5, "noqa": True},
            {},
        ),
        ({}, {"fake": "foo"}, {}),
        ({"non-existent": False}, {"fake": "foo"}, {}),
    ],
)
def test_keyword_arguments_for(params, args, expected_kwargs, default_options):
    """Verify the keyword args are generated properly."""
    file_processor = processor.FileProcessor(
        "-",
        default_options,
        lines=[
            "Line 1",
        ],
    )
    ret = file_processor.keyword_arguments_for(params, args)

    assert ret == expected_kwargs


def test_keyword_arguments_for_does_not_handle_attribute_errors(
    default_options,
):
    """Verify we re-raise AttributeErrors."""
    file_processor = processor.FileProcessor(
        "-",
        default_options,
        lines=[
            "Line 1",
        ],
    )

    with pytest.raises(AttributeError):
        file_processor.keyword_arguments_for({"fake": True}, {})


def test_processor_split_line(default_options):
    file_processor = processor.FileProcessor(
        "-",
        default_options,
        lines=[
            'x = """\n',
            "contents\n",
            '"""\n',
        ],
    )
    token = tokenize.TokenInfo(
        3,
        '"""\ncontents\n"""',
        (1, 4),
        (3, 3),
        'x = """\ncontents\n"""\n',
    )
    expected = [('x = """\n', 1, True), ("contents\n", 2, True)]
    assert file_processor.multiline is False
    actual = [
        (line, file_processor.line_number, file_processor.multiline)
        for line in file_processor.multiline_string(token)
    ]
    assert file_processor.multiline is False
    assert expected == actual
    assert file_processor.line_number == 3


def test_build_ast(default_options):
    """Verify the logic for how we build an AST for plugins."""
    file_processor = processor.FileProcessor(
        "-", default_options, lines=["a = 1\n"],
    )

    module = file_processor.build_ast()
    assert isinstance(module, ast.Module)


def test_next_logical_line_updates_the_previous_logical_line(default_options):
    """Verify that we update our tracking of the previous logical line."""
    file_processor = processor.FileProcessor(
        "-", default_options, lines=["a = 1\n"],
    )

    file_processor.indent_level = 1
    file_processor.logical_line = "a = 1"
    assert file_processor.previous_logical == ""
    assert file_processor.previous_indent_level == 0

    file_processor.next_logical_line()
    assert file_processor.previous_logical == "a = 1"
    assert file_processor.previous_indent_level == 1


def test_visited_new_blank_line(default_options):
    """Verify we update the number of blank lines seen."""
    file_processor = processor.FileProcessor(
        "-", default_options, lines=["a = 1\n"],
    )

    assert file_processor.blank_lines == 0
    file_processor.visited_new_blank_line()
    assert file_processor.blank_lines == 1


@pytest.mark.parametrize(
    "string, expected",
    [
        ('""', '""'),
        ("''", "''"),
        ('"a"', '"x"'),
        ("'a'", "'x'"),
        ('"x"', '"x"'),
        ("'x'", "'x'"),
        ('"abcdef"', '"xxxxxx"'),
        ("'abcdef'", "'xxxxxx'"),
        ('""""""', '""""""'),
        ("''''''", "''''''"),
        ('"""a"""', '"""x"""'),
        ("'''a'''", "'''x'''"),
        ('"""x"""', '"""x"""'),
        ("'''x'''", "'''x'''"),
        ('"""abcdef"""', '"""xxxxxx"""'),
        ("'''abcdef'''", "'''xxxxxx'''"),
        ('"""xxxxxx"""', '"""xxxxxx"""'),
        ("'''xxxxxx'''", "'''xxxxxx'''"),
    ],
)
def test_mutate_string(string, expected, default_options):
    """Verify we appropriately mutate the string to sanitize it."""
    actual = processor.mutate_string(string)
    assert expected == actual


@pytest.mark.parametrize(
    "string, expected",
    [
        ("    ", 4),
        ("      ", 6),
        ("\t", 8),
        ("\t\t", 16),
        ("       \t", 8),
        ("        \t", 16),
    ],
)
def test_expand_indent(string, expected):
    """Verify we correctly measure the amount of indentation."""
    actual = processor.expand_indent(string)
    assert expected == actual


@pytest.mark.parametrize(
    "current_count, token_text, expected",
    [
        (0, "(", 1),
        (0, "[", 1),
        (0, "{", 1),
        (1, ")", 0),
        (1, "]", 0),
        (1, "}", 0),
        (10, "+", 10),
    ],
)
def test_count_parentheses(current_count, token_text, expected):
    """Verify our arithmetic is correct."""
    assert processor.count_parentheses(current_count, token_text) == expected


def test_nonexistent_file(default_options):
    """Verify that FileProcessor raises IOError when a file does not exist."""
    with pytest.raises(IOError):
        processor.FileProcessor("foobar.py", default_options)
```

## File: `tests/unit/test_filenameonly_formatter.py`
```python
"""Tests for the FilenameOnly formatter object."""
from __future__ import annotations

import argparse

from flake8.formatting import default
from flake8.violation import Violation


def options(**kwargs):
    """Create an argparse.Namespace instance."""
    kwargs.setdefault("color", "auto")
    kwargs.setdefault("output_file", None)
    kwargs.setdefault("tee", False)
    return argparse.Namespace(**kwargs)


def test_caches_filenames_already_printed():
    """Verify we cache filenames when we format them."""
    formatter = default.FilenameOnly(options())
    assert formatter.filenames_already_printed == set()

    formatter.format(Violation("code", "file.py", 1, 1, "text", "l"))
    assert formatter.filenames_already_printed == {"file.py"}


def test_only_returns_a_string_once_from_format():
    """Verify format ignores the second error with the same filename."""
    formatter = default.FilenameOnly(options())
    error = Violation("code", "file.py", 1, 1, "text", "1")

    assert formatter.format(error) == "file.py"
    assert formatter.format(error) is None


def test_show_source_returns_nothing():
    """Verify show_source returns nothing."""
    formatter = default.FilenameOnly(options())
    error = Violation("code", "file.py", 1, 1, "text", "1")

    assert formatter.show_source(error) is None
```

## File: `tests/unit/test_legacy_api.py`
```python
"""Tests for Flake8's legacy API."""
from __future__ import annotations

from unittest import mock

import pytest

from flake8.api import legacy as api
from flake8.formatting import base as formatter


def test_styleguide_options():
    """Show that we proxy the StyleGuide.options attribute."""
    app = mock.Mock()
    app.options = "options"
    style_guide = api.StyleGuide(app)
    assert style_guide.options == "options"


def test_styleguide_paths():
    """Show that we proxy the StyleGuide.paths attribute."""
    app = mock.Mock()
    app.options.filenames = ["paths"]
    style_guide = api.StyleGuide(app)
    assert style_guide.paths == ["paths"]


def test_styleguide_check_files():
    """Verify we call the right application methods."""
    paths = ["foo", "bar"]
    app = mock.Mock()
    style_guide = api.StyleGuide(app)
    report = style_guide.check_files(paths)

    assert app.options.filenames == paths
    app.run_checks.assert_called_once_with()
    app.report_errors.assert_called_once_with()
    assert isinstance(report, api.Report)


def test_styleguide_excluded():
    """Verify we delegate to our file checker manager.

    When we add the parent argument, we don't check that is_path_excluded was
    called only once.
    """
    style_guide = api.get_style_guide(exclude=["file*", "*/parent/*"])
    assert not style_guide.excluded("unrelated.py")
    assert style_guide.excluded("file.py")
    assert style_guide.excluded("test.py", "parent")


def test_styleguide_init_report_does_nothing():
    """Verify if we use None that we don't call anything."""
    app = mock.Mock()
    style_guide = api.StyleGuide(app)
    style_guide.init_report()
    assert app.make_formatter.called is False
    assert app.make_guide.called is False


def test_styleguide_init_report_with_non_subclass():
    """Verify we raise a ValueError with non BaseFormatter subclasses."""
    app = mock.Mock()
    style_guide = api.StyleGuide(app)
    with pytest.raises(ValueError):
        style_guide.init_report(object)  # type: ignore
    assert app.make_formatter.called is False
    assert app.make_guide.called is False


def test_styleguide_init_report():
    """Verify we do the right incantation for the Application."""
    app = mock.Mock(guide="fake")
    style_guide = api.StyleGuide(app)

    class FakeFormatter(formatter.BaseFormatter):
        def format(self, *args):
            raise NotImplementedError

    style_guide.init_report(FakeFormatter)
    assert isinstance(app.formatter, FakeFormatter)
    assert app.guide is None
    app.make_guide.assert_called_once_with()


def test_styleguide_input_file():
    """Verify we call StyleGuide.check_files with the filename."""
    app = mock.Mock()
    style_guide = api.StyleGuide(app)
    with mock.patch.object(style_guide, "check_files") as check_files:
        style_guide.input_file("file.py")
    check_files.assert_called_once_with(["file.py"])


def test_report_total_errors():
    """Verify total errors is just a proxy attribute."""
    app = mock.Mock(result_count="Fake count")
    report = api.Report(app)
    assert report.total_errors == "Fake count"


def test_report_get_statistics():
    """Verify that we use the statistics object."""
    stats = mock.Mock()
    stats.statistics_for.return_value = []
    style_guide = mock.Mock(stats=stats)
    app = mock.Mock(guide=style_guide)

    report = api.Report(app)
    assert report.get_statistics("E") == []
    stats.statistics_for.assert_called_once_with("E")
```

## File: `tests/unit/test_main_options.py`
```python
from __future__ import annotations

from flake8.main import options


def test_stage1_arg_parser():
    stage1_parser = options.stage1_arg_parser()
    opts, args = stage1_parser.parse_known_args(
        ["--foo", "--verbose", "src", "setup.py", "--statistics", "--version"],
    )

    assert opts.verbose
    assert args == ["--foo", "src", "setup.py", "--statistics", "--version"]


def test_stage1_arg_parser_ignores_help():
    stage1_parser = options.stage1_arg_parser()
    _, args = stage1_parser.parse_known_args(["--help", "-h"])
    assert args == ["--help", "-h"]
```

## File: `tests/unit/test_nothing_formatter.py`
```python
"""Tests for the Nothing formatter obbject."""
from __future__ import annotations

import argparse

from flake8.formatting import default
from flake8.violation import Violation


def options(**kwargs):
    """Create an argparse.Namespace instance."""
    kwargs.setdefault("color", "auto")
    kwargs.setdefault("output_file", None)
    kwargs.setdefault("tee", False)
    return argparse.Namespace(**kwargs)


def test_format_returns_nothing():
    """Verify Nothing.format returns None."""
    formatter = default.Nothing(options())
    error = Violation("code", "file.py", 1, 1, "text", "1")

    assert formatter.format(error) is None


def test_show_source_returns_nothing():
    """Verify Nothing.show_source returns None."""
    formatter = default.Nothing(options())
    error = Violation("code", "file.py", 1, 1, "text", "1")

    assert formatter.show_source(error) is None
```

## File: `tests/unit/test_option.py`
```python
"""Unit tests for flake8.options.manager.Option."""
from __future__ import annotations

import functools
from unittest import mock

import pytest

from flake8.options import manager


def test_to_argparse():
    """Test conversion to an argparse arguments."""
    opt = manager.Option(
        short_option_name="-t",
        long_option_name="--test",
        action="count",
        parse_from_config=True,
        normalize_paths=True,
    )
    assert opt.normalize_paths is True
    assert opt.parse_from_config is True

    args, kwargs = opt.to_argparse()
    assert args == ["-t", "--test"]
    assert kwargs == {"action": "count", "type": mock.ANY}
    assert isinstance(kwargs["type"], functools.partial)


def test_to_argparse_creates_an_option_as_we_expect():
    """Show that we pass all keyword args to argparse."""
    opt = manager.Option("-t", "--test", action="count")
    args, kwargs = opt.to_argparse()
    assert args == ["-t", "--test"]
    assert kwargs == {"action": "count"}


def test_config_name_generation():
    """Show that we generate the config name deterministically."""
    opt = manager.Option(
        long_option_name="--some-very-long-option-name",
        parse_from_config=True,
    )

    assert opt.config_name == "some_very_long_option_name"


def test_config_name_needs_long_option_name():
    """Show that we error out if the Option should be parsed from config."""
    with pytest.raises(ValueError):
        manager.Option("-s", parse_from_config=True)


def test_dest_is_not_overridden():
    """Show that we do not override custom destinations."""
    opt = manager.Option("-s", "--short", dest="something_not_short")
    assert opt.dest == "something_not_short"
```

## File: `tests/unit/test_option_manager.py`
```python
"""Unit tests for flake.options.manager.OptionManager."""
from __future__ import annotations

import argparse
import os

import pytest

from flake8.main.options import JobsArgument
from flake8.options import manager

TEST_VERSION = "3.0.0b1"


@pytest.fixture
def optmanager():
    """Generate a simple OptionManager with default test arguments."""
    return manager.OptionManager(
        version=TEST_VERSION,
        plugin_versions="",
        parents=[],
        formatter_names=[],
    )


def test_option_manager_creates_option_parser(optmanager):
    """Verify that a new manager creates a new parser."""
    assert isinstance(optmanager.parser, argparse.ArgumentParser)


def test_option_manager_including_parent_options():
    """Verify parent options are included in the parsed options."""
    # GIVEN
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--parent")

    # WHEN
    optmanager = manager.OptionManager(
        version=TEST_VERSION,
        plugin_versions="",
        parents=[parent_parser],
        formatter_names=[],
    )
    options = optmanager.parse_args(["--parent", "foo"])

    # THEN
    assert options.parent == "foo"


def test_parse_args_forwarding_default_values(optmanager):
    """Verify default provided values are present in the final result."""
    namespace = argparse.Namespace(foo="bar")
    options = optmanager.parse_args([], namespace)
    assert options.foo == "bar"


def test_parse_args_forwarding_type_coercion(optmanager):
    """Verify default provided values are type converted from add_option."""
    optmanager.add_option("--foo", type=int)
    namespace = argparse.Namespace(foo="5")
    options = optmanager.parse_args([], namespace)
    assert options.foo == 5


def test_add_option_short_option_only(optmanager):
    """Verify the behaviour of adding a short-option only."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option("-s", help="Test short opt")
    assert optmanager.options[0].short_option_name == "-s"


def test_add_option_long_option_only(optmanager):
    """Verify the behaviour of adding a long-option only."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option("--long", help="Test long opt")
    assert optmanager.options[0].short_option_name is manager._ARG.NO
    assert optmanager.options[0].long_option_name == "--long"


def test_add_short_and_long_option_names(optmanager):
    """Verify the behaviour of using both short and long option names."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option("-b", "--both", help="Test both opts")
    assert optmanager.options[0].short_option_name == "-b"
    assert optmanager.options[0].long_option_name == "--both"


def test_add_option_with_custom_args(optmanager):
    """Verify that add_option handles custom Flake8 parameters."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option("--parse", parse_from_config=True)
    optmanager.add_option("--commas", comma_separated_list=True)
    optmanager.add_option("--files", normalize_paths=True)

    attrs = ["parse_from_config", "comma_separated_list", "normalize_paths"]
    for option, attr in zip(optmanager.options, attrs):
        assert getattr(option, attr) is True


def test_parse_args_normalize_path(optmanager):
    """Show that parse_args handles path normalization."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option("--config", normalize_paths=True)

    options = optmanager.parse_args(["--config", "../config.ini"])
    assert options.config == os.path.abspath("../config.ini")


def test_parse_args_handles_comma_separated_defaults(optmanager):
    """Show that parse_args handles defaults that are comma-separated."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option(
        "--exclude", default="E123,W234", comma_separated_list=True,
    )

    options = optmanager.parse_args([])
    assert options.exclude == ["E123", "W234"]


def test_parse_args_handles_comma_separated_lists(optmanager):
    """Show that parse_args handles user-specified comma-separated lists."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option(
        "--exclude", default="E123,W234", comma_separated_list=True,
    )

    options = optmanager.parse_args(["--exclude", "E201,W111,F280"])
    assert options.exclude == ["E201", "W111", "F280"]


def test_parse_args_normalize_paths(optmanager):
    """Verify parse_args normalizes a comma-separated list of paths."""
    assert optmanager.options == []
    assert optmanager.config_options_dict == {}

    optmanager.add_option(
        "--extra-config", normalize_paths=True, comma_separated_list=True,
    )

    options = optmanager.parse_args(
        ["--extra-config", "../config.ini,tox.ini,flake8/some-other.cfg"],
    )
    assert options.extra_config == [
        os.path.abspath("../config.ini"),
        "tox.ini",
        os.path.abspath("flake8/some-other.cfg"),
    ]


def test_extend_default_ignore(optmanager):
    """Verify that we update the extended default ignore list."""
    assert optmanager.extended_default_ignore == []

    optmanager.extend_default_ignore(["T100", "T101", "T102"])
    assert optmanager.extended_default_ignore == ["T100", "T101", "T102"]


@pytest.mark.parametrize(
    ("s", "is_auto", "n_jobs"),
    (
        ("auto", True, -1),
        ("4", False, 4),
    ),
)
def test_parse_valid_jobs_argument(s, is_auto, n_jobs):
    """Test that --jobs properly parses valid arguments."""
    jobs_opt = JobsArgument(s)
    assert is_auto == jobs_opt.is_auto
    assert n_jobs == jobs_opt.n_jobs


def test_parse_invalid_jobs_argument(optmanager, capsys):
    """Test that --jobs properly rejects invalid arguments."""
    namespace = argparse.Namespace()
    optmanager.add_option("--jobs", type=JobsArgument)
    with pytest.raises(SystemExit):
        optmanager.parse_args(["--jobs=foo"], namespace)
    out, err = capsys.readouterr()
    output = out + err
    expected = (
        "\nflake8: error: argument --jobs: "
        "'foo' must be 'auto' or an integer.\n"
    )
    assert expected in output


def test_jobs_argument_str():
    """Test that JobsArgument has a correct __str__."""
    assert str(JobsArgument("auto")) == "auto"
    assert str(JobsArgument("123")) == "123"


def test_jobs_argument_repr():
    """Test that JobsArgument has a correct __repr__."""
    assert repr(JobsArgument("auto")) == "JobsArgument('auto')"
    assert repr(JobsArgument("123")) == "JobsArgument('123')"
```

## File: `tests/unit/test_options_config.py`
```python
from __future__ import annotations

import configparser
import os.path
from unittest import mock

import pytest

from flake8 import exceptions
from flake8.main.options import register_default_options
from flake8.options import config
from flake8.options.manager import OptionManager


def test_config_not_found_returns_none(tmp_path):
    assert config._find_config_file(str(tmp_path)) is None


def test_config_file_without_section_is_not_considered(tmp_path):
    tmp_path.joinpath("setup.cfg").touch()

    assert config._find_config_file(str(tmp_path)) is None


def test_config_file_with_parse_error_is_not_considered(tmp_path, caplog):
    # the syntax error here is deliberately to trigger a partial parse
    # https://github.com/python/cpython/issues/95546
    tmp_path.joinpath("setup.cfg").write_text("[flake8]\nx = 1\n...")

    assert config._find_config_file(str(tmp_path)) is None

    assert len(caplog.record_tuples) == 1
    ((mod, level, msg),) = caplog.record_tuples
    assert (mod, level) == ("flake8.options.config", 30)
    assert msg.startswith("ignoring unparseable config ")


def test_config_file_with_encoding_error_is_not_considered(tmp_path, caplog):
    tmp_path.joinpath("setup.cfg").write_bytes(b"\xa0\xef\xfe\x12")

    assert config._find_config_file(str(tmp_path)) is None

    assert len(caplog.record_tuples) == 1
    ((mod, level, msg),) = caplog.record_tuples
    assert (mod, level) == ("flake8.options.config", 30)
    assert msg.startswith("ignoring unparseable config ")


@pytest.mark.parametrize("cfg_name", ("setup.cfg", "tox.ini", ".flake8"))
def test_find_config_file_exists_at_path(tmp_path, cfg_name):
    expected = tmp_path.joinpath(cfg_name)
    expected.write_text("[flake8]")

    assert config._find_config_file(str(tmp_path)) == str(expected)


@pytest.mark.parametrize("section", ("flake8", "flake8:local-plugins"))
def test_find_config_either_section(tmp_path, section):
    expected = tmp_path.joinpath("setup.cfg")
    expected.write_text(f"[{section}]")

    assert config._find_config_file(str(tmp_path)) == str(expected)


def test_find_config_searches_upwards(tmp_path):
    subdir = tmp_path.joinpath("d")
    subdir.mkdir()

    expected = tmp_path.joinpath("setup.cfg")
    expected.write_text("[flake8]")

    assert config._find_config_file(str(subdir)) == str(expected)


def test_find_config_ignores_homedir(tmp_path):
    subdir = tmp_path.joinpath("d")
    subdir.mkdir()

    tmp_path.joinpath(".flake8").write_text("[flake8]")

    with mock.patch.object(os.path, "expanduser", return_value=str(tmp_path)):
        assert config._find_config_file(str(subdir)) is None


def test_find_config_ignores_unknown_homedir(tmp_path):
    subdir = tmp_path.joinpath("d")

    with mock.patch.object(os.path, "expanduser", return_value=str(subdir)):
        assert config._find_config_file(str(tmp_path)) is None


def test_load_config_config_specified_skips_discovery(tmpdir):
    tmpdir.join("setup.cfg").write("[flake8]\nindent-size=2\n")
    custom_cfg = tmpdir.join("custom.cfg")
    custom_cfg.write("[flake8]\nindent-size=8\n")

    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(str(custom_cfg), [], isolated=False)

    assert cfg.get("flake8", "indent-size") == "8"
    assert cfg_dir == str(tmpdir)


def test_load_config_no_config_file_does_discovery(tmpdir):
    tmpdir.join("setup.cfg").write("[flake8]\nindent-size=2\n")

    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(None, [], isolated=False)

    assert cfg.get("flake8", "indent-size") == "2"
    assert cfg_dir == str(tmpdir)


def test_load_config_no_config_found_sets_cfg_dir_to_pwd(tmpdir):
    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(None, [], isolated=False)

    assert cfg.sections() == []
    assert cfg_dir == str(tmpdir)


def test_load_config_isolated_ignores_configuration(tmpdir):
    tmpdir.join("setup.cfg").write("[flake8]\nindent-size=2\n")

    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(None, [], isolated=True)

    assert cfg.sections() == []
    assert cfg_dir == str(tmpdir)


def test_load_config_append_config(tmpdir):
    tmpdir.join("setup.cfg").write("[flake8]\nindent-size=2\n")
    other = tmpdir.join("other.cfg")
    other.write("[flake8]\nindent-size=8\n")

    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(None, [str(other)], isolated=False)

    assert cfg.get("flake8", "indent-size") == "8"
    assert cfg_dir == str(tmpdir)


NON_ASCII_CONFIG = "# ☃\n[flake8]\nindent-size=8\n"


def test_load_auto_config_utf8(tmpdir):
    tmpdir.join("setup.cfg").write_text(NON_ASCII_CONFIG, encoding="UTF-8")
    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(None, [], isolated=False)
    assert cfg["flake8"]["indent-size"] == "8"


def test_load_explicit_config_utf8(tmpdir):
    tmpdir.join("t.cfg").write_text(NON_ASCII_CONFIG, encoding="UTF-8")
    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config("t.cfg", [], isolated=False)
    assert cfg["flake8"]["indent-size"] == "8"


def test_load_extra_config_utf8(tmpdir):
    tmpdir.join("setup.cfg").write("[flake8]\nindent-size=2\n")
    tmpdir.join("t.cfg").write_text(NON_ASCII_CONFIG, encoding="UTF-8")
    with tmpdir.as_cwd():
        cfg, cfg_dir = config.load_config(None, ["t.cfg"], isolated=False)
    assert cfg["flake8"]["indent-size"] == "8"


@pytest.fixture
def opt_manager():
    ret = OptionManager(
        version="123", plugin_versions="", parents=[], formatter_names=[],
    )
    register_default_options(ret)
    return ret


def test_parse_config_no_values(tmp_path, opt_manager):
    cfg = configparser.RawConfigParser()
    ret = config.parse_config(opt_manager, cfg, tmp_path)
    assert ret == {}


def test_parse_config_typed_values(tmp_path, opt_manager):
    cfg = configparser.RawConfigParser()
    cfg.add_section("flake8")
    cfg.set("flake8", "indent_size", "2")
    cfg.set("flake8", "hang_closing", "true")
    # test normalizing dashed-options
    cfg.set("flake8", "extend-exclude", "d/1,d/2")

    ret = config.parse_config(opt_manager, cfg, str(tmp_path))
    assert ret == {
        "indent_size": 2,
        "hang_closing": True,
        "extend_exclude": [
            str(tmp_path.joinpath("d/1")),
            str(tmp_path.joinpath("d/2")),
        ],
    }


def test_parse_config_ignores_unknowns(tmp_path, opt_manager, caplog):
    cfg = configparser.RawConfigParser()
    cfg.add_section("flake8")
    cfg.set("flake8", "wat", "wat")

    ret = config.parse_config(opt_manager, cfg, str(tmp_path))
    assert ret == {}

    assert caplog.record_tuples == [
        (
            "flake8.options.config",
            10,
            'Option "wat" is not registered. Ignoring.',
        ),
    ]


def test_load_config_missing_file_raises_exception(capsys):
    with pytest.raises(exceptions.ExecutionError):
        config.load_config("foo.cfg", [])


def test_load_config_missing_append_config_raise_exception():
    with pytest.raises(exceptions.ExecutionError):
        config.load_config(None, ["dont_exist_config.cfg"], isolated=False)


def test_invalid_ignore_codes_raise_error(tmpdir, opt_manager):
    tmpdir.join("setup.cfg").write("[flake8]\nignore = E203, //comment")
    with tmpdir.as_cwd():
        cfg, _ = config.load_config("setup.cfg", [], isolated=False)

    with pytest.raises(ValueError) as excinfo:
        config.parse_config(opt_manager, cfg, tmpdir)

    expected = (
        "Error code '//comment' supplied to 'ignore' option "
        "does not match '^[A-Z]{1,3}[0-9]{0,3}$'"
    )
    (msg,) = excinfo.value.args
    assert msg == expected


def test_invalid_extend_ignore_codes_raise_error(tmpdir, opt_manager):
    tmpdir.join("setup.cfg").write("[flake8]\nextend-ignore = E203, //comment")
    with tmpdir.as_cwd():
        cfg, _ = config.load_config("setup.cfg", [], isolated=False)

    with pytest.raises(ValueError) as excinfo:
        config.parse_config(opt_manager, cfg, tmpdir)

    expected = (
        "Error code '//comment' supplied to 'extend-ignore' option "
        "does not match '^[A-Z]{1,3}[0-9]{0,3}$'"
    )
    (msg,) = excinfo.value.args
    assert msg == expected
```

## File: `tests/unit/test_pyflakes_codes.py`
```python
"""Tests of pyflakes monkey patches."""
from __future__ import annotations

import ast

import pyflakes

from flake8.plugins import pyflakes as pyflakes_shim


def test_all_pyflakes_messages_have_flake8_codes_assigned():
    """Verify all PyFlakes messages have error codes assigned."""
    messages = {
        name
        for name, obj in vars(pyflakes.messages).items()
        if name[0].isupper() and obj.message
    }
    assert messages == set(pyflakes_shim.FLAKE8_PYFLAKES_CODES)


def test_undefined_local_code():
    """In pyflakes 2.1.0 this code's string formatting was changed."""
    src = """\
import sys

def f():
    sys = sys
"""
    tree = ast.parse(src)
    checker = pyflakes_shim.FlakesChecker(tree, "t.py")
    message_texts = [s for _, _, s, _ in checker.run()]
    assert message_texts == [
        "F823 local variable 'sys' defined in enclosing scope on line 1 referenced before assignment",  # noqa: E501
        "F841 local variable 'sys' is assigned to but never used",
    ]
```

## File: `tests/unit/test_statistics.py`
```python
"""Tests for the statistics module in Flake8."""
from __future__ import annotations

import pytest

from flake8 import statistics as stats
from flake8.violation import Violation

DEFAULT_ERROR_CODE = "E100"
DEFAULT_FILENAME = "file.py"
DEFAULT_TEXT = "Default text"


def make_error(**kwargs):
    """Create errors with a bunch of default values."""
    kwargs.setdefault("code", DEFAULT_ERROR_CODE)
    kwargs.setdefault("filename", DEFAULT_FILENAME)
    kwargs.setdefault("line_number", 1)
    kwargs.setdefault("column_number", 1)
    kwargs.setdefault("text", DEFAULT_TEXT)
    return Violation(**kwargs, physical_line=None)


def test_key_creation():
    """Verify how we create Keys from Errors."""
    key = stats.Key.create_from(make_error())
    assert key == (DEFAULT_FILENAME, DEFAULT_ERROR_CODE)
    assert key.filename == DEFAULT_FILENAME
    assert key.code == DEFAULT_ERROR_CODE


@pytest.mark.parametrize(
    "code, filename, args, expected_result",
    [
        # Error prefix matches
        ("E123", "file000.py", ("E", None), True),
        ("E123", "file000.py", ("E1", None), True),
        ("E123", "file000.py", ("E12", None), True),
        ("E123", "file000.py", ("E123", None), True),
        # Error prefix and filename match
        ("E123", "file000.py", ("E", "file000.py"), True),
        ("E123", "file000.py", ("E1", "file000.py"), True),
        ("E123", "file000.py", ("E12", "file000.py"), True),
        ("E123", "file000.py", ("E123", "file000.py"), True),
        # Error prefix does not match
        ("E123", "file000.py", ("W", None), False),
        # Error prefix matches but filename does not
        ("E123", "file000.py", ("E", "file001.py"), False),
        # Error prefix does not match but filename does
        ("E123", "file000.py", ("W", "file000.py"), False),
        # Neither error prefix match nor filename
        ("E123", "file000.py", ("W", "file001.py"), False),
    ],
)
def test_key_matching(code, filename, args, expected_result):
    """Verify Key#matches behaves as we expect with fthe above input."""
    key = stats.Key.create_from(make_error(code=code, filename=filename))
    assert key.matches(*args) is expected_result


def test_statistic_creation():
    """Verify how we create Statistic objects from Errors."""
    stat = stats.Statistic.create_from(make_error())
    assert stat.error_code == DEFAULT_ERROR_CODE
    assert stat.message == DEFAULT_TEXT
    assert stat.filename == DEFAULT_FILENAME
    assert stat.count == 0


def test_statistic_increment():
    """Verify we update the count."""
    stat = stats.Statistic.create_from(make_error())
    assert stat.count == 0
    stat.increment()
    assert stat.count == 1


def test_recording_statistics():
    """Verify that we appropriately create a new Statistic and store it."""
    aggregator = stats.Statistics()
    assert list(aggregator.statistics_for("E")) == []
    aggregator.record(make_error())
    storage = aggregator._store
    for key, value in storage.items():
        assert isinstance(key, stats.Key)
        assert isinstance(value, stats.Statistic)

    assert storage[stats.Key(DEFAULT_FILENAME, DEFAULT_ERROR_CODE)].count == 1


def test_statistics_for_single_record():
    """Show we can retrieve the only statistic recorded."""
    aggregator = stats.Statistics()
    assert list(aggregator.statistics_for("E")) == []
    aggregator.record(make_error())
    statistics = list(aggregator.statistics_for("E"))
    assert len(statistics) == 1
    assert isinstance(statistics[0], stats.Statistic)


def test_statistics_for_filters_by_filename():
    """Show we can retrieve the only statistic recorded."""
    aggregator = stats.Statistics()
    assert list(aggregator.statistics_for("E")) == []
    aggregator.record(make_error())
    aggregator.record(make_error(filename="example.py"))

    statistics = list(aggregator.statistics_for("E", DEFAULT_FILENAME))
    assert len(statistics) == 1
    assert isinstance(statistics[0], stats.Statistic)


def test_statistic_for_retrieves_more_than_one_value():
    """Show this works for more than a couple statistic values."""
    aggregator = stats.Statistics()
    for i in range(50):
        aggregator.record(make_error(code=f"E1{i:02d}"))
        aggregator.record(make_error(code=f"W2{i:02d}"))

    statistics = list(aggregator.statistics_for("E"))
    assert len(statistics) == 50

    statistics = list(aggregator.statistics_for("W22"))
    assert len(statistics) == 10
```

## File: `tests/unit/test_style_guide.py`
```python
"""Tests for the flake8.style_guide.StyleGuide class."""
from __future__ import annotations

import argparse
from unittest import mock

import pytest

from flake8 import statistics
from flake8 import style_guide
from flake8 import utils
from flake8.formatting import base


def create_options(**kwargs):
    """Create and return an instance of argparse.Namespace."""
    kwargs.setdefault("select", [])
    kwargs.setdefault("extended_default_select", [])
    kwargs.setdefault("extended_default_ignore", [])
    kwargs.setdefault("extend_select", [])
    kwargs.setdefault("ignore", [])
    kwargs.setdefault("extend_ignore", [])
    kwargs.setdefault("disable_noqa", False)
    kwargs.setdefault("enable_extensions", [])
    kwargs.setdefault("per_file_ignores", [])
    return argparse.Namespace(**kwargs)


def test_handle_error_does_not_raise_type_errors():
    """Verify that we handle our inputs better."""
    formatter = mock.create_autospec(base.BaseFormatter, instance=True)
    guide = style_guide.StyleGuide(
        create_options(select=["T111"], ignore=[]),
        formatter=formatter,
        stats=statistics.Statistics(),
    )

    assert 1 == guide.handle_error(
        "T111", "file.py", 1, 1, "error found", "a = 1",
    )


def test_style_guide_manager():
    """Verify how the StyleGuideManager creates a default style guide."""
    formatter = mock.create_autospec(base.BaseFormatter, instance=True)
    options = create_options()
    guide = style_guide.StyleGuideManager(options, formatter=formatter)
    assert guide.default_style_guide.options is options
    assert len(guide.style_guides) == 1


PER_FILE_IGNORES_UNPARSED = [
    "first_file.py:W9",
    "second_file.py:F4,F9",
    "third_file.py:E3",
    "sub_dir/*:F4",
]


@pytest.mark.parametrize(
    "style_guide_file,filename,expected",
    [
        ("first_file.py", "first_file.py", True),
        ("first_file.py", "second_file.py", False),
        ("sub_dir/*.py", "first_file.py", False),
        ("sub_dir/*.py", "sub_dir/file.py", True),
        ("sub_dir/*.py", "other_dir/file.py", False),
    ],
)
def test_style_guide_applies_to(style_guide_file, filename, expected):
    """Verify that we match a file to its style guide."""
    formatter = mock.create_autospec(base.BaseFormatter, instance=True)
    options = create_options()
    guide = style_guide.StyleGuide(
        options,
        formatter=formatter,
        stats=statistics.Statistics(),
        filename=style_guide_file,
    )
    assert guide.applies_to(filename) is expected


def test_style_guide_manager_pre_file_ignores_parsing():
    """Verify how the StyleGuideManager creates a default style guide."""
    formatter = mock.create_autospec(base.BaseFormatter, instance=True)
    options = create_options(per_file_ignores=PER_FILE_IGNORES_UNPARSED)
    guide = style_guide.StyleGuideManager(options, formatter=formatter)
    assert len(guide.style_guides) == 5
    expected = [
        utils.normalize_path(p)
        for p in [
            "first_file.py",
            "second_file.py",
            "third_file.py",
            "sub_dir/*",
        ]
    ]
    assert expected == [g.filename for g in guide.style_guides[1:]]


@pytest.mark.parametrize(
    "ignores,violation,filename,handle_error_return",
    [
        (["E1", "E2"], "F401", "first_file.py", 1),
        (["E1", "E2"], "E121", "first_file.py", 0),
        (["E1", "E2"], "F401", "second_file.py", 0),
        (["E1", "E2"], "F401", "third_file.py", 1),
        (["E1", "E2"], "E311", "third_file.py", 0),
        (["E1", "E2"], "F401", "sub_dir/file.py", 0),
    ],
)
def test_style_guide_manager_pre_file_ignores(
    ignores, violation, filename, handle_error_return,
):
    """Verify how the StyleGuideManager creates a default style guide."""
    formatter = mock.create_autospec(base.BaseFormatter, instance=True)
    options = create_options(
        ignore=ignores,
        select=["E", "F", "W"],
        per_file_ignores=PER_FILE_IGNORES_UNPARSED,
    )
    guide = style_guide.StyleGuideManager(options, formatter=formatter)
    assert (
        guide.handle_error(violation, filename, 1, 1, "Fake text")
        == handle_error_return
    )


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("first_file.py", utils.normalize_path("first_file.py")),
        ("second_file.py", utils.normalize_path("second_file.py")),
        ("third_file.py", utils.normalize_path("third_file.py")),
        ("fourth_file.py", None),
        ("sub_dir/__init__.py", utils.normalize_path("sub_dir/*")),
        ("other_dir/__init__.py", None),
    ],
)
def test_style_guide_manager_style_guide_for(filename, expected):
    """Verify the style guide selection function."""
    formatter = mock.create_autospec(base.BaseFormatter, instance=True)
    options = create_options(per_file_ignores=PER_FILE_IGNORES_UNPARSED)
    guide = style_guide.StyleGuideManager(options, formatter=formatter)

    file_guide = guide.style_guide_for(filename)
    assert file_guide.filename == expected
```

## File: `tests/unit/test_utils.py`
```python
"""Tests for flake8's utils module."""
from __future__ import annotations

import io
import logging
import os
import sys
from unittest import mock

import pytest

from flake8 import exceptions
from flake8 import utils

RELATIVE_PATHS = ["flake8", "pep8", "pyflakes", "mccabe"]


@pytest.mark.parametrize(
    "value,expected",
    [
        ("E123,\n\tW234,\n    E206", ["E123", "W234", "E206"]),
        ("E123,W234,E206", ["E123", "W234", "E206"]),
        ("E123 W234 E206", ["E123", "W234", "E206"]),
        ("E123\nW234 E206", ["E123", "W234", "E206"]),
        ("E123\nW234\nE206", ["E123", "W234", "E206"]),
        ("E123,W234,E206,", ["E123", "W234", "E206"]),
        ("E123,W234,E206, ,\n", ["E123", "W234", "E206"]),
        ("E123,W234,,E206,,", ["E123", "W234", "E206"]),
        ("E123, W234,, E206,,", ["E123", "W234", "E206"]),
        ("E123,,W234,,E206,,", ["E123", "W234", "E206"]),
        ("", []),
    ],
)
def test_parse_comma_separated_list(value, expected):
    """Verify that similar inputs produce identical outputs."""
    assert utils.parse_comma_separated_list(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        # empty option configures nothing
        ("", []),
        ("   ", []),
        ("\n\n\n", []),
        # basic case
        (
            "f.py:E123",
            [("f.py", ["E123"])],
        ),
        # multiple filenames, multiple codes
        (
            "f.py,g.py:E,F",
            [("f.py", ["E", "F"]), ("g.py", ["E", "F"])],
        ),
        # demonstrate that whitespace is not important around tokens
        (
            "   f.py  , g.py  : E  , F  ",
            [("f.py", ["E", "F"]), ("g.py", ["E", "F"])],
        ),
        # whitespace can separate groups of configuration
        (
            "f.py:E g.py:F",
            [("f.py", ["E"]), ("g.py", ["F"])],
        ),
        # newlines can separate groups of configuration
        (
            "f.py: E\ng.py: F\n",
            [("f.py", ["E"]), ("g.py", ["F"])],
        ),
        # whitespace can be used in place of commas
        (
            "f.py g.py: E F",
            [("f.py", ["E", "F"]), ("g.py", ["E", "F"])],
        ),
        # go ahead, indent your codes
        (
            "f.py:\n    E,F\ng.py:\n    G,H",
            [("f.py", ["E", "F"]), ("g.py", ["G", "H"])],
        ),
        # capitalized filenames are ok too
        (
            "F.py,G.py: F,G",
            [("F.py", ["F", "G"]), ("G.py", ["F", "G"])],
        ),
        #  it's easier to allow zero filenames or zero codes than forbid it
        (":E", []),
        ("f.py:", []),
        (":E f.py:F", [("f.py", ["F"])]),
        ("f.py: g.py:F", [("g.py", ["F"])]),
        ("f.py:E:", []),
        ("f.py:E.py:", []),
        ("f.py:Eg.py:F", [("Eg.py", ["F"])]),
        # sequences are also valid (?)
        (
            ["f.py:E,F", "g.py:G,H"],
            [("f.py", ["E", "F"]), ("g.py", ["G", "H"])],
        ),
        # six-digits codes are allowed
        (
            "f.py: ABC123",
            [("f.py", ["ABC123"])],
        ),
    ),
)
def test_parse_files_to_codes_mapping(value, expected):
    """Test parsing of valid files-to-codes mappings."""
    assert utils.parse_files_to_codes_mapping(value) == expected


@pytest.mark.parametrize(
    "value",
    (
        # code while looking for filenames
        "E123",
        "f.py,E123",
        "f.py E123",
        # eof while looking for filenames
        "f.py",
        "f.py:E,g.py"
        # colon while looking for codes
        "f.py::",
        # no separator between
        "f.py:E1F1",
    ),
)
def test_invalid_file_list(value):
    """Test parsing of invalid files-to-codes mappings."""
    with pytest.raises(exceptions.ExecutionError):
        utils.parse_files_to_codes_mapping(value)


@pytest.mark.parametrize(
    "value,expected",
    [
        ("flake8", "flake8"),
        (".", os.path.abspath(".")),
        ("../flake8", os.path.abspath("../flake8")),
        ("flake8/", os.path.abspath("flake8")),
    ],
)
def test_normalize_path(value, expected):
    """Verify that we normalize paths provided to the tool."""
    assert utils.normalize_path(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (
            ["flake8", "pep8", "pyflakes", "mccabe"],
            ["flake8", "pep8", "pyflakes", "mccabe"],
        ),
        (
            ["../flake8", "../pep8", "../pyflakes", "../mccabe"],
            [os.path.abspath(f"../{p}") for p in RELATIVE_PATHS],
        ),
    ],
)
def test_normalize_paths(value, expected):
    """Verify we normalizes a sequence of paths provided to the tool."""
    assert utils.normalize_paths(value) == expected


def test_matches_filename_for_excluding_dotfiles():
    """Verify that `.` and `..` are not matched by `.*`."""
    logger = logging.Logger(__name__)
    assert not utils.matches_filename(".", (".*",), "", logger)
    assert not utils.matches_filename("..", (".*",), "", logger)


@pytest.mark.parametrize(
    "filename,patterns,expected",
    [
        ("foo.py", [], True),
        ("foo.py", ["*.pyc"], False),
        ("foo.pyc", ["*.pyc"], True),
        ("foo.pyc", ["*.swp", "*.pyc", "*.py"], True),
    ],
)
def test_fnmatch(filename, patterns, expected):
    """Verify that our fnmatch wrapper works as expected."""
    assert utils.fnmatch(filename, patterns) is expected


def test_stdin_get_value_crlf():
    """Ensure that stdin is normalized from crlf to lf."""
    stdin = io.TextIOWrapper(io.BytesIO(b"1\r\n2\r\n"), "UTF-8")
    with mock.patch.object(sys, "stdin", stdin):
        assert utils.stdin_get_value.__wrapped__() == "1\n2\n"


def test_stdin_unknown_coding_token():
    """Ensure we produce source even for unknown encodings."""
    stdin = io.TextIOWrapper(io.BytesIO(b"# coding: unknown\n"), "UTF-8")
    with mock.patch.object(sys, "stdin", stdin):
        assert utils.stdin_get_value.__wrapped__() == "# coding: unknown\n"


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        ("", ""),
        ("my-plugin", "my-plugin"),
        ("MyPlugin", "myplugin"),
        ("my_plugin", "my-plugin"),
        ("my.plugin", "my-plugin"),
        ("my--plugin", "my-plugin"),
        ("my__plugin", "my-plugin"),
    ),
)
def test_normalize_pypi_name(s, expected):
    assert utils.normalize_pypi_name(s) == expected
```

## File: `tests/unit/test_violation.py`
```python
"""Tests for the flake8.violation.Violation class."""
from __future__ import annotations

from unittest import mock

import pytest

from flake8.violation import Violation


@pytest.mark.parametrize(
    "error_code,physical_line,expected_result",
    [
        ("E111", "a = 1", False),
        ("E121", "a = 1  # noqa: E111", False),
        ("E121", "a = 1  # noqa: E111,W123,F821", False),
        ("E111", "a = 1  # noqa: E111,W123,F821", True),
        ("W123", "a = 1  # noqa: E111,W123,F821", True),
        ("W123", "a = 1  # noqa: E111, W123,F821", True),
        ("E111", "a = 1  # noqa: E11,W123,F821", True),
        ("E121", "a = 1  # noqa:E111,W123,F821", False),
        ("E111", "a = 1  # noqa:E111,W123,F821", True),
        ("W123", "a = 1  # noqa:E111,W123,F821", True),
        ("W123", "a = 1  # noqa:E111, W123,F821", True),
        ("E111", "a = 1  # noqa:E11,W123,F821", True),
        ("E111", "a = 1  # noqa, analysis:ignore", True),
        ("E111", "a = 1  # noqa analysis:ignore", True),
        ("E111", "a = 1  # noqa - We do not care", True),
        ("E111", "a = 1  # noqa: We do not care", True),
        ("E111", "a = 1  # noqa:We do not care", True),
        ("ABC123", "a = 1  # noqa: ABC123", True),
        ("E111", "a = 1  # noqa: ABC123", False),
        ("ABC123", "a = 1  # noqa: ABC124", False),
    ],
)
def test_is_inline_ignored(error_code, physical_line, expected_result):
    """Verify that we detect inline usage of ``# noqa``."""
    error = Violation(error_code, "filename.py", 1, 1, "error text", None)
    # We want `None` to be passed as the physical line so we actually use our
    # monkey-patched linecache.getline value.

    with mock.patch("linecache.getline", return_value=physical_line):
        assert error.is_inline_ignored(False) is expected_result


def test_disable_is_inline_ignored():
    """Verify that is_inline_ignored exits immediately if disabling NoQA."""
    error = Violation("E121", "filename.py", 1, 1, "error text", "line")

    with mock.patch("linecache.getline") as getline:
        assert error.is_inline_ignored(True) is False

    assert getline.called is False
```

## File: `tests/unit/plugins/finder_test.py`
```python
from __future__ import annotations

import configparser
import importlib.metadata
import sys
from unittest import mock

import pytest

from flake8.exceptions import ExecutionError
from flake8.exceptions import FailedToLoadPlugin
from flake8.plugins import finder
from flake8.plugins.pyflakes import FlakesChecker


def _ep(name="X", value="dne:dne", group="flake8.extension"):
    return importlib.metadata.EntryPoint(name, value, group)


def _plugin(package="local", version="local", ep=None):
    if ep is None:
        ep = _ep()
    return finder.Plugin(package, version, ep)


def _loaded(plugin=None, obj=None, parameters=None):
    if plugin is None:
        plugin = _plugin()
    if parameters is None:
        parameters = {"tree": True}
    return finder.LoadedPlugin(plugin, obj, parameters)


def test_loaded_plugin_entry_name_vs_display_name():
    loaded = _loaded(_plugin(package="package-name", ep=_ep(name="Q")))
    assert loaded.entry_name == "Q"
    assert loaded.display_name == "package-name[Q]"


def test_plugins_all_plugins():
    tree_plugin = _loaded(parameters={"tree": True})
    logical_line_plugin = _loaded(parameters={"logical_line": True})
    physical_line_plugin = _loaded(parameters={"physical_line": True})
    report_plugin = _loaded(
        plugin=_plugin(ep=_ep(name="R", group="flake8.report")),
    )

    plugins = finder.Plugins(
        checkers=finder.Checkers(
            tree=[tree_plugin],
            logical_line=[logical_line_plugin],
            physical_line=[physical_line_plugin],
        ),
        reporters={"R": report_plugin},
        disabled=[],
    )

    assert tuple(plugins.all_plugins()) == (
        tree_plugin,
        logical_line_plugin,
        physical_line_plugin,
        report_plugin,
    )


def test_plugins_versions_str():
    plugins = finder.Plugins(
        checkers=finder.Checkers(
            tree=[_loaded(_plugin(package="pkg1", version="1"))],
            logical_line=[_loaded(_plugin(package="pkg2", version="2"))],
            physical_line=[_loaded(_plugin(package="pkg1", version="1"))],
        ),
        reporters={
            # ignore flake8 builtin plugins
            "default": _loaded(_plugin(package="flake8")),
            # ignore local plugins
            "custom": _loaded(_plugin(package="local")),
        },
        disabled=[],
    )
    assert plugins.versions_str() == "pkg1: 1, pkg2: 2"


@pytest.fixture
def pyflakes_dist(tmp_path):
    metadata = """\
Metadata-Version: 2.1
Name: pyflakes
Version: 9000.1.0
"""
    d = tmp_path.joinpath("pyflakes.dist-info")
    d.mkdir()
    d.joinpath("METADATA").write_text(metadata)
    return importlib.metadata.PathDistribution(d)


@pytest.fixture
def pycodestyle_dist(tmp_path):
    metadata = """\
Metadata-Version: 2.1
Name: pycodestyle
Version: 9000.2.0
"""
    d = tmp_path.joinpath("pycodestyle.dist-info")
    d.mkdir()
    d.joinpath("METADATA").write_text(metadata)
    return importlib.metadata.PathDistribution(d)


@pytest.fixture
def flake8_dist(tmp_path):
    metadata = """\
Metadata-Version: 2.1
Name: flake8
Version: 9001
"""
    entry_points = """\
[console_scripts]
flake8 = flake8.main.cli:main

[flake8.extension]
F = flake8.plugins.pyflakes:FlakesChecker
E = flake8.plugins.pycodestyle:pycodestyle_logical
W = flake8.plugins.pycodestyle:pycodestyle_physical

[flake8.report]
default = flake8.formatting.default:Default
pylint = flake8.formatting.default:Pylint
"""
    d = tmp_path.joinpath("flake8.dist-info")
    d.mkdir()
    d.joinpath("METADATA").write_text(metadata)
    d.joinpath("entry_points.txt").write_text(entry_points)
    return importlib.metadata.PathDistribution(d)


@pytest.fixture
def flake8_foo_dist(tmp_path):
    metadata = """\
Metadata-Version: 2.1
Name: flake8-foo
Version: 1.2.3
"""
    eps = """\
[console_scripts]
foo = flake8_foo:main
[flake8.extension]
Q = flake8_foo:Plugin
[flake8.report]
foo = flake8_foo:Formatter
"""
    d = tmp_path.joinpath("flake8_foo.dist-info")
    d.mkdir()
    d.joinpath("METADATA").write_text(metadata)
    d.joinpath("entry_points.txt").write_text(eps)
    return importlib.metadata.PathDistribution(d)


@pytest.fixture
def mock_distribution(pyflakes_dist, pycodestyle_dist):
    dists = {"pyflakes": pyflakes_dist, "pycodestyle": pycodestyle_dist}
    with mock.patch.object(importlib.metadata, "distribution", dists.get):
        yield


def test_flake8_plugins(flake8_dist, mock_distribution):
    """Ensure entrypoints for flake8 are parsed specially."""

    eps = flake8_dist.entry_points
    ret = set(finder._flake8_plugins(eps, "flake8", "9001"))
    assert ret == {
        finder.Plugin(
            "pyflakes",
            "9000.1.0",
            importlib.metadata.EntryPoint(
                "F",
                "flake8.plugins.pyflakes:FlakesChecker",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pycodestyle",
            "9000.2.0",
            importlib.metadata.EntryPoint(
                "E",
                "flake8.plugins.pycodestyle:pycodestyle_logical",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pycodestyle",
            "9000.2.0",
            importlib.metadata.EntryPoint(
                "W",
                "flake8.plugins.pycodestyle:pycodestyle_physical",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "flake8",
            "9001",
            importlib.metadata.EntryPoint(
                "default",
                "flake8.formatting.default:Default",
                "flake8.report",
            ),
        ),
        finder.Plugin(
            "flake8",
            "9001",
            importlib.metadata.EntryPoint(
                "pylint", "flake8.formatting.default:Pylint", "flake8.report",
            ),
        ),
    }


def test_importlib_plugins(
    tmp_path,
    flake8_dist,
    flake8_foo_dist,
    mock_distribution,
    caplog,
):
    """Ensure we can load plugins from importlib.metadata."""

    # make sure flake8-colors is skipped
    flake8_colors_metadata = """\
Metadata-Version: 2.1
Name: flake8-colors
Version: 1.2.3
"""
    flake8_colors_eps = """\
[flake8.extension]
flake8-colors = flake8_colors:ColorFormatter
"""
    flake8_colors_d = tmp_path.joinpath("flake8_colors.dist-info")
    flake8_colors_d.mkdir()
    flake8_colors_d.joinpath("METADATA").write_text(flake8_colors_metadata)
    flake8_colors_d.joinpath("entry_points.txt").write_text(flake8_colors_eps)
    flake8_colors_dist = importlib.metadata.PathDistribution(flake8_colors_d)

    unrelated_metadata = """\
Metadata-Version: 2.1
Name: unrelated
Version: 4.5.6
"""
    unrelated_eps = """\
[console_scripts]
unrelated = unrelated:main
"""
    unrelated_d = tmp_path.joinpath("unrelated.dist-info")
    unrelated_d.mkdir()
    unrelated_d.joinpath("METADATA").write_text(unrelated_metadata)
    unrelated_d.joinpath("entry_points.txt").write_text(unrelated_eps)
    unrelated_dist = importlib.metadata.PathDistribution(unrelated_d)

    with mock.patch.object(
        importlib.metadata,
        "distributions",
        return_value=[
            flake8_dist,
            flake8_colors_dist,
            flake8_foo_dist,
            unrelated_dist,
        ],
    ):
        ret = set(finder._find_importlib_plugins())

    assert ret == {
        finder.Plugin(
            "flake8-foo",
            "1.2.3",
            importlib.metadata.EntryPoint(
                "Q", "flake8_foo:Plugin", "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pycodestyle",
            "9000.2.0",
            importlib.metadata.EntryPoint(
                "E",
                "flake8.plugins.pycodestyle:pycodestyle_logical",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pycodestyle",
            "9000.2.0",
            importlib.metadata.EntryPoint(
                "W",
                "flake8.plugins.pycodestyle:pycodestyle_physical",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pyflakes",
            "9000.1.0",
            importlib.metadata.EntryPoint(
                "F",
                "flake8.plugins.pyflakes:FlakesChecker",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "flake8",
            "9001",
            importlib.metadata.EntryPoint(
                "default",
                "flake8.formatting.default:Default",
                "flake8.report",
            ),
        ),
        finder.Plugin(
            "flake8",
            "9001",
            importlib.metadata.EntryPoint(
                "pylint", "flake8.formatting.default:Pylint", "flake8.report",
            ),
        ),
        finder.Plugin(
            "flake8-foo",
            "1.2.3",
            importlib.metadata.EntryPoint(
                "foo", "flake8_foo:Formatter", "flake8.report",
            ),
        ),
    }

    assert caplog.record_tuples == [
        (
            "flake8.plugins.finder",
            30,
            "flake8-colors plugin is obsolete in flake8>=5.0",
        ),
    ]


def test_duplicate_dists(flake8_dist):
    # some poorly packaged pythons put lib and lib64 on sys.path resulting in
    # duplicates from `importlib.metadata.distributions`
    with mock.patch.object(
        importlib.metadata,
        "distributions",
        return_value=[
            flake8_dist,
            flake8_dist,
        ],
    ):
        ret = list(finder._find_importlib_plugins())

    # we should not have duplicates
    assert len(ret) == len(set(ret))


def test_find_local_plugins_nothing():
    cfg = configparser.RawConfigParser()
    assert set(finder._find_local_plugins(cfg)) == set()


@pytest.fixture
def local_plugin_cfg():
    cfg = configparser.RawConfigParser()
    cfg.add_section("flake8:local-plugins")
    cfg.set("flake8:local-plugins", "extension", "Y=mod2:attr, X = mod:attr")
    cfg.set("flake8:local-plugins", "report", "Z=mod3:attr")
    return cfg


def test_find_local_plugins(local_plugin_cfg):
    ret = set(finder._find_local_plugins(local_plugin_cfg))
    assert ret == {
        finder.Plugin(
            "local",
            "local",
            importlib.metadata.EntryPoint(
                "X",
                "mod:attr",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "local",
            "local",
            importlib.metadata.EntryPoint(
                "Y",
                "mod2:attr",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "local",
            "local",
            importlib.metadata.EntryPoint(
                "Z",
                "mod3:attr",
                "flake8.report",
            ),
        ),
    }


def test_parse_plugin_options_not_specified(tmp_path):
    cfg = configparser.RawConfigParser()
    opts = finder.parse_plugin_options(
        cfg,
        str(tmp_path),
        enable_extensions=None,
        require_plugins=None,
    )
    expected = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        require_plugins=frozenset(),
    )
    assert opts == expected


def test_parse_enabled_from_commandline(tmp_path):
    cfg = configparser.RawConfigParser()
    cfg.add_section("flake8")
    cfg.set("flake8", "enable_extensions", "A,B,C")
    opts = finder.parse_plugin_options(
        cfg,
        str(tmp_path),
        enable_extensions="D,E,F",
        require_plugins=None,
    )
    assert opts.enable_extensions == frozenset(("D", "E", "F"))


@pytest.mark.parametrize("opt", ("enable_extensions", "enable-extensions"))
def test_parse_enabled_from_config(opt, tmp_path):
    cfg = configparser.RawConfigParser()
    cfg.add_section("flake8")
    cfg.set("flake8", opt, "A,B,C")
    opts = finder.parse_plugin_options(
        cfg,
        str(tmp_path),
        enable_extensions=None,
        require_plugins=None,
    )
    assert opts.enable_extensions == frozenset(("A", "B", "C"))


def test_parse_plugin_options_local_plugin_paths_missing(tmp_path):
    cfg = configparser.RawConfigParser()
    opts = finder.parse_plugin_options(
        cfg,
        str(tmp_path),
        enable_extensions=None,
        require_plugins=None,
    )
    assert opts.local_plugin_paths == ()


def test_parse_plugin_options_local_plugin_paths(tmp_path):
    cfg = configparser.RawConfigParser()
    cfg.add_section("flake8:local-plugins")
    cfg.set("flake8:local-plugins", "paths", "./a, ./b")
    opts = finder.parse_plugin_options(
        cfg,
        str(tmp_path),
        enable_extensions=None,
        require_plugins=None,
    )

    expected = (str(tmp_path.joinpath("a")), str(tmp_path.joinpath("b")))
    assert opts.local_plugin_paths == expected


def test_find_plugins(
    tmp_path,
    flake8_dist,
    flake8_foo_dist,
    mock_distribution,
    local_plugin_cfg,
):
    opts = finder.PluginOptions.blank()
    with mock.patch.object(
        importlib.metadata,
        "distributions",
        return_value=[flake8_dist, flake8_foo_dist],
    ):
        ret = finder.find_plugins(local_plugin_cfg, opts)

    assert ret == [
        finder.Plugin(
            "flake8",
            "9001",
            importlib.metadata.EntryPoint(
                "default",
                "flake8.formatting.default:Default",
                "flake8.report",
            ),
        ),
        finder.Plugin(
            "flake8",
            "9001",
            importlib.metadata.EntryPoint(
                "pylint", "flake8.formatting.default:Pylint", "flake8.report",
            ),
        ),
        finder.Plugin(
            "flake8-foo",
            "1.2.3",
            importlib.metadata.EntryPoint(
                "Q", "flake8_foo:Plugin", "flake8.extension",
            ),
        ),
        finder.Plugin(
            "flake8-foo",
            "1.2.3",
            importlib.metadata.EntryPoint(
                "foo", "flake8_foo:Formatter", "flake8.report",
            ),
        ),
        finder.Plugin(
            "local",
            "local",
            importlib.metadata.EntryPoint("X", "mod:attr", "flake8.extension"),
        ),
        finder.Plugin(
            "local",
            "local",
            importlib.metadata.EntryPoint(
                "Y", "mod2:attr", "flake8.extension",
            ),
        ),
        finder.Plugin(
            "local",
            "local",
            importlib.metadata.EntryPoint("Z", "mod3:attr", "flake8.report"),
        ),
        finder.Plugin(
            "pycodestyle",
            "9000.2.0",
            importlib.metadata.EntryPoint(
                "E",
                "flake8.plugins.pycodestyle:pycodestyle_logical",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pycodestyle",
            "9000.2.0",
            importlib.metadata.EntryPoint(
                "W",
                "flake8.plugins.pycodestyle:pycodestyle_physical",
                "flake8.extension",
            ),
        ),
        finder.Plugin(
            "pyflakes",
            "9000.1.0",
            importlib.metadata.EntryPoint(
                "F",
                "flake8.plugins.pyflakes:FlakesChecker",
                "flake8.extension",
            ),
        ),
    ]


def test_find_plugins_plugin_is_present(flake8_foo_dist):
    cfg = configparser.RawConfigParser()
    options_flake8_foo_required = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        require_plugins=frozenset(("flake8-foo",)),
    )
    options_not_required = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        require_plugins=frozenset(),
    )

    with mock.patch.object(
        importlib.metadata,
        "distributions",
        return_value=[flake8_foo_dist],
    ):
        # neither of these raise, `flake8-foo` is satisfied
        finder.find_plugins(cfg, options_flake8_foo_required)
        finder.find_plugins(cfg, options_not_required)


def test_find_plugins_plugin_is_missing(flake8_dist, flake8_foo_dist):
    cfg = configparser.RawConfigParser()
    options_flake8_foo_required = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        require_plugins=frozenset(("flake8-foo",)),
    )
    options_not_required = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        require_plugins=frozenset(),
    )

    with mock.patch.object(
        importlib.metadata,
        "distributions",
        return_value=[flake8_dist],
    ):
        # this is ok, no special requirements
        finder.find_plugins(cfg, options_not_required)

        # but we get a nice error for missing plugins here!
        with pytest.raises(ExecutionError) as excinfo:
            finder.find_plugins(cfg, options_flake8_foo_required)

        (msg,) = excinfo.value.args
        assert msg == (
            "required plugins were not installed!\n"
            "- installed: flake8, pycodestyle, pyflakes\n"
            "- expected: flake8-foo\n"
            "- missing: flake8-foo"
        )


def test_find_plugins_name_normalization(flake8_foo_dist):
    cfg = configparser.RawConfigParser()
    opts = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        # this name will be normalized before checking
        require_plugins=frozenset(("Flake8_Foo",)),
    )

    with mock.patch.object(
        importlib.metadata,
        "distributions",
        return_value=[flake8_foo_dist],
    ):
        finder.find_plugins(cfg, opts)


def test_parameters_for_class_plugin():
    """Verify that we can retrieve the parameters for a class plugin."""

    class FakeCheck:
        def __init__(self, tree):
            raise NotImplementedError

    assert finder._parameters_for(FakeCheck) == {"tree": True}


def test_parameters_for_function_plugin():
    """Verify that we retrieve the parameters for a function plugin."""

    def fake_plugin(physical_line, self, tree, optional=None):
        raise NotImplementedError

    assert finder._parameters_for(fake_plugin) == {
        "physical_line": True,
        "self": True,
        "tree": True,
        "optional": False,
    }


def test_load_plugin_import_error():
    plugin = _plugin(ep=_ep(value="dne:dne"))

    with pytest.raises(FailedToLoadPlugin) as excinfo:
        finder._load_plugin(plugin)

    pkg, e = excinfo.value.args
    assert pkg == "local"
    assert isinstance(e, ModuleNotFoundError)


def test_load_plugin_not_callable():
    plugin = _plugin(ep=_ep(value="os:curdir"))

    with pytest.raises(FailedToLoadPlugin) as excinfo:
        finder._load_plugin(plugin)

    pkg, e = excinfo.value.args
    assert pkg == "local"
    assert isinstance(e, TypeError)
    assert e.args == ("expected loaded plugin to be callable",)


def test_load_plugin_ok():
    plugin = _plugin(ep=_ep(value="flake8.plugins.pyflakes:FlakesChecker"))

    loaded = finder._load_plugin(plugin)

    assert loaded == finder.LoadedPlugin(
        plugin,
        FlakesChecker,
        {"tree": True, "filename": True},
    )


@pytest.fixture
def reset_sys():
    orig_path = sys.path[:]
    orig_modules = sys.modules.copy()
    yield
    sys.path[:] = orig_path
    sys.modules.clear()
    sys.modules.update(orig_modules)


@pytest.mark.usefixtures("reset_sys")
def test_import_plugins_extends_sys_path():
    plugin = _plugin(ep=_ep(value="aplugin:ExtensionTestPlugin2"))

    opts = finder.PluginOptions(
        local_plugin_paths=("tests/integration/subdir",),
        enable_extensions=frozenset(),
        require_plugins=frozenset(),
    )
    ret = finder._import_plugins([plugin], opts)

    import aplugin

    assert ret == [
        finder.LoadedPlugin(
            plugin,
            aplugin.ExtensionTestPlugin2,
            {"tree": True},
        ),
    ]


def test_classify_plugins():
    report_plugin = _loaded(
        plugin=_plugin(ep=_ep(name="R", group="flake8.report")),
    )
    tree_plugin = _loaded(parameters={"tree": True})
    logical_line_plugin = _loaded(parameters={"logical_line": True})
    physical_line_plugin = _loaded(parameters={"physical_line": True})

    classified = finder._classify_plugins(
        [
            report_plugin,
            tree_plugin,
            logical_line_plugin,
            physical_line_plugin,
        ],
        finder.PluginOptions.blank(),
    )

    assert classified == finder.Plugins(
        checkers=finder.Checkers(
            tree=[tree_plugin],
            logical_line=[logical_line_plugin],
            physical_line=[physical_line_plugin],
        ),
        reporters={"R": report_plugin},
        disabled=[],
    )


def test_classify_plugins_enable_a_disabled_plugin():
    obj = mock.Mock(off_by_default=True)
    plugin = _plugin(ep=_ep(name="ABC"))
    loaded = _loaded(plugin=plugin, parameters={"tree": True}, obj=obj)

    normal_opts = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(),
        require_plugins=frozenset(),
    )
    classified_normal = finder._classify_plugins([loaded], normal_opts)
    enabled_opts = finder.PluginOptions(
        local_plugin_paths=(),
        enable_extensions=frozenset(("ABC",)),
        require_plugins=frozenset(),
    )
    classified_enabled = finder._classify_plugins([loaded], enabled_opts)

    assert classified_normal == finder.Plugins(
        checkers=finder.Checkers([], [], []),
        reporters={},
        disabled=[loaded],
    )
    assert classified_enabled == finder.Plugins(
        checkers=finder.Checkers([loaded], [], []),
        reporters={},
        disabled=[],
    )


def test_classify_plugins_does_not_error_on_reporter_prefix():
    # these are ok, don't check their name
    plugin = _plugin(ep=_ep(name="report-er", group="flake8.report"))
    loaded = _loaded(plugin=plugin)

    opts = finder.PluginOptions.blank()
    classified = finder._classify_plugins([loaded], opts)

    assert classified == finder.Plugins(
        checkers=finder.Checkers([], [], []),
        reporters={"report-er": loaded},
        disabled=[],
    )


def test_classify_plugins_errors_on_incorrect_checker_name():
    plugin = _plugin(ep=_ep(name="INVALID", group="flake8.extension"))
    loaded = _loaded(plugin=plugin, parameters={"tree": True})

    with pytest.raises(ExecutionError) as excinfo:
        finder._classify_plugins([loaded], finder.PluginOptions.blank())

    (msg,) = excinfo.value.args
    assert msg == (
        "plugin code for `local[INVALID]` "
        "does not match ^[A-Z]{1,3}[0-9]{0,3}$"
    )


@pytest.mark.usefixtures("reset_sys")
def test_load_plugins():
    plugin = _plugin(ep=_ep(value="aplugin:ExtensionTestPlugin2"))

    opts = finder.PluginOptions(
        local_plugin_paths=("tests/integration/subdir",),
        enable_extensions=frozenset(),
        require_plugins=frozenset(),
    )
    ret = finder.load_plugins([plugin], opts)

    import aplugin

    assert ret == finder.Plugins(
        checkers=finder.Checkers(
            tree=[
                finder.LoadedPlugin(
                    plugin,
                    aplugin.ExtensionTestPlugin2,
                    {"tree": True},
                ),
            ],
            logical_line=[],
            physical_line=[],
        ),
        reporters={},
        disabled=[],
    )
```

## File: `tests/unit/plugins/pycodestyle_test.py`
```python
from __future__ import annotations

import importlib.machinery
import importlib.util
import os.path

import flake8.plugins.pycodestyle

HERE = os.path.dirname(os.path.abspath(__file__))


def test_up_to_date():
    """Validate that the generated pycodestyle plugin is up to date.

    We generate two "meta" plugins for pycodestyle to avoid calling overhead.

    To regenerate run:

        ./bin/gen-pycodestyle-plugin > src/flake8/plugins/pycodestyle.py
    """

    path = os.path.join(HERE, "../../../bin/gen-pycodestyle-plugin")
    name = os.path.basename(path)
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    assert spec is not None
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)

    expected = "".join(f"{line}\n" for line in mod.lines())

    with open(flake8.plugins.pycodestyle.__file__) as f:
        contents = f.read()

    assert contents == expected
```

## File: `tests/unit/plugins/reporter_test.py`
```python
from __future__ import annotations

import argparse
import importlib.metadata

import pytest

from flake8.formatting import default
from flake8.plugins import finder
from flake8.plugins import reporter


def _opts(**kwargs):
    kwargs.setdefault("quiet", 0)
    kwargs.setdefault("color", "never")
    kwargs.setdefault("output_file", None)
    return argparse.Namespace(**kwargs)


@pytest.fixture
def reporters():
    def _plugin(name, cls):
        return finder.LoadedPlugin(
            finder.Plugin(
                "flake8",
                "123",
                importlib.metadata.EntryPoint(
                    name, f"{cls.__module__}:{cls.__name__}", "flake8.report",
                ),
            ),
            cls,
            {"options": True},
        )

    return {
        "default": _plugin("default", default.Default),
        "pylint": _plugin("pylint", default.Pylint),
        "quiet-filename": _plugin("quiet-filename", default.FilenameOnly),
        "quiet-nothing": _plugin("quiet-nothing", default.Nothing),
    }


def test_make_formatter_default(reporters):
    ret = reporter.make(reporters, _opts(format="default"))
    assert isinstance(ret, default.Default)
    assert ret.error_format == default.Default.error_format


def test_make_formatter_quiet_filename(reporters):
    ret = reporter.make(reporters, _opts(format="default", quiet=1))
    assert isinstance(ret, default.FilenameOnly)


@pytest.mark.parametrize("quiet", (2, 3))
def test_make_formatter_very_quiet(reporters, quiet):
    ret = reporter.make(reporters, _opts(format="default", quiet=quiet))
    assert isinstance(ret, default.Nothing)


def test_make_formatter_custom(reporters):
    ret = reporter.make(reporters, _opts(format="pylint"))
    assert isinstance(ret, default.Pylint)


def test_make_formatter_format_string(reporters, caplog):
    ret = reporter.make(reporters, _opts(format="hi %(code)s"))
    assert isinstance(ret, default.Default)
    assert ret.error_format == "hi %(code)s"

    assert caplog.record_tuples == [
        (
            "flake8.plugins.reporter",
            30,
            "'hi %(code)s' is an unknown formatter.  Falling back to default.",
        ),
    ]
```

