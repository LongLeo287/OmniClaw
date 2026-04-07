---
id: isort
type: knowledge
owner: OA_Triage
---
# isort
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![isort - isort your imports, so you don't have to.](https://raw.githubusercontent.com/pycqa/isort/main/art/logo_large.png)](https://isort.readthedocs.io/)

------------------------------------------------------------------------

[![PyPI version](https://badge.fury.io/py/isort.svg)](https://badge.fury.io/py/isort)
[![Python Version](https://img.shields.io/pypi/pyversions/isort)][pypi status]
[![CI](https://github.com/PyCQA/isort/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/PyCQA/isort/actions/workflows/continuous-integration.yml)
[![Code coverage Status](https://codecov.io/gh/pycqa/isort/branch/main/graph/badge.svg)](https://codecov.io/gh/pycqa/isort)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/isort/)
[![Downloads](https://pepy.tech/badge/isort)](https://pepy.tech/project/isort)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://isort.readthedocs.io/)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/pycqa/isort/?ref=repository-badge)

[pypi status]: https://pypi.org/project/isort/
_________________

[Read Latest Documentation](https://isort.readthedocs.io/) - [Browse GitHub Code Repository](https://github.com/pycqa/isort/)
_________________

# isort your imports, so you don't have to.

isort is a Python utility / library to sort imports alphabetically and
automatically separate into sections and by type. It provides a command line
utility, Python library and [plugins for various
editors](https://github.com/pycqa/isort/wiki/isort-Plugins) to
quickly sort all your imports. It requires Python 3.10+ to run but
supports formatting Python 2 code too.

- [Try isort now from your browser!](../docs/quick_start/0.-try.md)
- [Using black? See the isort and black compatibility guide.](../docs/configuration/black_compatibility.md)
- [isort has official support for pre-commit!](../docs/configuration/pre-commit.md)

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
                         lib9, lib10, lib11, lib12, lib13, lib14, lib15)

from my_lib import Object, Object2, Object3

print("Hey")
print("yo")
```

## Installing isort

Installing isort is as simple as:

```bash
pip install isort
```

## Using isort

**From the command line**:

To run on specific files:

```bash
isort mypythonfile.py mypythonfile2.py
```

To apply recursively:

```bash
isort .
```

If [globstar](https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html)
is enabled, `isort .` is equivalent to:

```bash
isort **/*.py
```

To view proposed changes without applying them:

```bash
isort mypythonfile.py --diff
```

Finally, to atomically run isort against a project, only applying
changes if they don't introduce syntax errors:

```bash
isort --atomic .
```

(Note: this is disabled by default, as it prevents isort from
running against code written using a different version of Python.)

**From within Python**:

```python
import isort

isort.file("pythonfile.py")
```

or:

```python
import isort

sorted_code = isort.code("import b\nimport a\n")
```

## Installing isort's for your preferred text editor

Several plugins have been written that enable to use isort from within a
variety of text-editors. You can find a full list of them [on the isort
wiki](https://github.com/pycqa/isort/wiki/isort-Plugins).
Additionally, I will enthusiastically accept pull requests that include
plugins for other text editors and add documentation for them as I am
notified.

## Multi line output modes

You will notice above the \"multi\_line\_output\" setting. This setting
defines how from imports wrap when they extend past the line\_length
limit and has [12 possible settings](../docs/configuration/multi_line_output_modes.md).

## Indentation

To change the how constant indents appear - simply change the
indent property with the following accepted formats:

-   Number of spaces you would like. For example: 4 would cause standard
    4 space indentation.
-   Tab
-   A verbatim string with quotes around it.

For example:

```python
"    "
```

is equivalent to 4.

For the import styles that use parentheses, you can control whether or
not to include a trailing comma after the last import with the
`include_trailing_comma` option (defaults to `False`).

## Intelligently Balanced Multi-line Imports

As of isort 3.1.0 support for balanced multi-line imports has been
added. With this enabled isort will dynamically change the import length
to the one that produces the most balanced grid, while staying below the
maximum import length defined.

Example:

```python
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
```

Will be produced instead of:

```python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
```

To enable this set `balanced_wrapping` to `True` in your config or pass
the `-e` option into the command line utility.

## Custom Sections and Ordering

isort provides configuration options to change almost every aspect of how
imports are organized, ordered, or grouped together in sections.

[Click here](../docs/configuration/custom_sections_and_ordering.md) for an overview of all these options.

## Skip processing of imports (outside of configuration)

To make isort ignore a single import simply add a comment at the end of
the import line containing the text `isort:skip`:

```python
import module  # isort:skip
```

or:

```python
from xyz import (abc,  # isort:skip
                 yo,
                 hey)
```

To make isort skip an entire file simply add `isort:skip_file` to the
module's doc string:

```python
""" my_module.py
    Best module ever

   isort:skip_file
"""

import b
import a
```

## Adding or removing an import from multiple files

isort can be ran or configured to add / remove imports automatically.

[See a complete guide here.](../docs/configuration/add_or_remove_imports.md)

## Using isort to verify code

The `--check-only` option
-------------------------

isort can also be used to verify that code is correctly formatted
by running it with `-c`. Any files that contain incorrectly sorted
and/or formatted imports will be outputted to `stderr`.

```bash
isort **/*.py -c -v

SUCCESS: /home/timothy/Projects/Open_Source/isort/isort_kate_plugin.py Everything Looks Good!
ERROR: /home/timothy/Projects/Open_Source/isort/isort/isort.py Imports are incorrectly sorted.
```

One great place this can be used is with a pre-commit git hook, such as
this one by \@acdha:

<https://gist.github.com/acdha/8717683>

This can help to ensure a certain level of code quality throughout a
project.

## Git hook

isort provides a hook function that can be integrated into your Git
pre-commit script to check Python code before committing.

[More info here.](../docs/configuration/git_hook.md)

## Spread the word

[![Imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://isort.readthedocs.io/)

Place this badge at the top of your repository to let others know your project uses isort.

For README.md:

```markdown
[![Imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://isort.readthedocs.io/)
```

Or README.rst:

```rst
.. image:: https://img.shields.io/badge/imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://isort.readthedocs.io/
```

## Security contact information

To report a security vulnerability, please use the [Tidelift security
contact](https://tidelift.com/security). Tidelift will coordinate the
fix and disclosure.

## Why isort?

isort simply stands for import sort. It was originally called
"sortImports" however I got tired of typing the extra characters and
came to the realization camelCase is not pythonic.

I wrote isort because in an organization I used to work in the manager
came in one day and decided all code must have alphabetically sorted
imports. The code base was huge - and he meant for us to do it by hand.
However, being a programmer - I\'m too lazy to spend 8 hours mindlessly
performing a function, but not too lazy to spend 16 hours automating it.
I was given permission to open source sortImports and here we are :)

------------------------------------------------------------------------

[Get professionally supported isort with the Tidelift
Subscription](https://tidelift.com/subscription/pkg/pypi-isort?utm_source=pypi-isort&utm_medium=referral&utm_campaign=readme)

Professional support for isort is available as part of the [Tidelift
Subscription](https://tidelift.com/subscription/pkg/pypi-isort?utm_source=pypi-isort&utm_medium=referral&utm_campaign=readme).
Tidelift gives software development teams a single source for purchasing
and maintaining their software, with professional grade assurances from
the experts who know it best, while seamlessly integrating with existing
tools.

------------------------------------------------------------------------

Thanks and I hope you find isort useful!

~Timothy Crosley

```

### File: .cruft.json
```json
{
  "template": "https://github.com/timothycrosley/cookiecutter-python/",
  "commit": "71391fd9999067ef4b38aa05e7116087fac431f8",
  "context": {
    "cookiecutter": {
      "full_name": "Timothy Crosley",
      "email": "timothy.crosley@gmail.com",
      "github_username": "pycqa",
      "project_name": "isort",
      "description": "A Python utility / library to sort Python imports.",
      "version": "4.3.21",
      "_template": "https://github.com/timothycrosley/cookiecutter-python/"
    }
  },
  "directory": "",
  "checkout": null
}

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

```

### File: .pre-commit-hooks.yaml
```yaml
-   id: isort
    name: isort
    entry: isort
    stages: [pre-commit, pre-merge-commit, pre-push, manual]
    require_serial: true
    language: python
    types_or: [cython, pyi, python]
    args: ['--filter-files']
    minimum_pre_commit_version: '3.2.0'

```

### File: .readthedocs.yaml
```yaml
version: 2

sphinx:
  configuration: docs/conf.py
  fail_on_warning: true

build:
  os: ubuntu-lts-latest
  tools:
    python: latest
  jobs:
    pre_create_environment:
        - asdf plugin add uv
        - asdf install uv latest
        - asdf global uv latest
    create_environment:
        - uv venv "${READTHEDOCS_VIRTUALENV_PATH}"
    install:
        - UV_PROJECT_ENVIRONMENT="${READTHEDOCS_VIRTUALENV_PATH}" uv sync --frozen --group docs

```

### File: CHANGELOG.md
```md
Changelog
=========

NOTE: isort follows the [semver](https://semver.org/) versioning standard.
Find out more about isort's release policy [here](../docs/major_releases/release_policy.md).

## Releases

### Unreleased

### 8.0.0 February 19 2026 

  - Removed `--old-finders` and `--magic-placement` flags and `old_finders` configuration option. The legacy finder logic that relied on environment introspection has been removed (#2445) @joao-faria-dev
  - Update the `plone` profile to not clash with `black` (#2456) @ale-rt

### 6.1.0 October 1 2025 

   - Add python 3.14 classifier and badge (#2409) @staticdev
   - Drop use of non-standard pkg_resources API (#2405) @dvarrazzo

### 6.0.1 Febuary 26 2025

   - Add OSError handling in find_imports_in_file (#2331) @kobarity

### 6.0.0 January 27 2025

   - Remove support for Python 3.8 (#2327) @DanielNoord 
   - Python 3.13 support (#2306) @mayty
   - Speed up exists_case_sensitive calls (#2264) @correctmost
   - Ensure that split_on_trailing_comma works with as imports (#2340) @DanielNoord
   - Black profile: enable magic comma (#2236) @MrMino
   - Update line_length and single_line_exclusions in google profile (#2149) @jagapiou
   - Allow --diff to be used with --jobs (#2302) @mnakama
   - Fix wemake profile to have correct character limit (#2241) @sobolevn
   - Fix sort_reexports code mangling (#2283) @Helveg
   - Fix correct group by package tokenization (#2136) @glasnt

### 5.13.2 December 13 2023

   - Apply the bracket fix from issue #471 only for use_parentheses=True (#2184) @bp72
   - Confine pre-commit to stages (#2213) @davidculley
   - Fixed colors extras (#2212) @staticdev

### 5.13.1 December 11 2023

   - Fixed integration tests (#2208) @bp72
   - Fixed normalizing imports from more than one level of parent modules (issue/2152) (#2191) @bp72
   - Remove optional dependencies without extras (#2207) @staticdev

### 5.13.0 December 9 2023

  - Cleanup deprecated extras (#2089) @staticdev
  - Fixed #1989: settings lookup when working in stream based mode
  - Fixed 80 line length for wemake linter (#2183) @skatromb
  - Add support for Python 3.12 (#2175) @hugovk
  - Fixed: add newest version to pre-commit docs (#2190) @AzulGarza
  - Fixed assertions in test_git_hook (#2196) @mgorny
  - Removed check for include_trailing_comma for the Hanging Indent wrap mode (#2192) @bp72
  - Use the standard library tomllib on sufficiently new python (#2202) @eli-schwartz
  - Update pre-commit.md version number (#2197) @nicobako
  - doc: Update black_compatibility.md (#2177) @JSS95
  - Fixed safety sept 2023 (#2178) @staticdev
  - docs: fix black profile documentation (#2163) @nijel
  - Fixed typo: indended -> indented (#2161) @vadimkerr
  - Docs(configuration/options.md): fix missing trailing spaces for hard linebreak (#2157) @JoeyTeng
  - Update pre-commit.md (#2148) @godiard
  - chore: move configurations to pyproject.toml (#2115) @SauravMaheshkar
  - Fixed typo in README (#2112) @stefmolin
  - Update version in pre-commit setup to avoid installation issue with poetry (#2103) @stefmolin
  - Skip .pytype directory by default. (#2098) @manueljacob
  - Fixed a tip block styling in the Config Files section (#2097) @Klavionik
  - Do not cache configuration files (#1995) @kaste
  - Derive settings_path from --filename (#1992) @kaste
  - Fixed year of version 5.12.0 in CHANGELOG.md (#2082) @DjLegolas
  
### 5.12.0 January 28 2023

  - Removed support for Python 3.7
  - Fixed incompatiblity with latest poetry version
  - Added support for directory limitations within built in git hook

### 5.11.5 January 30 2023 [hotfix]
  - Fixed incompatiblity with latest poetry version

### 5.11.4 December 21 2022

  - Fixed #2038 (again): stop installing documentation files to top-level site-packages (#2057) @mgorny
  - CI: only run release workflows for upstream (#2052) @hugovk
  - Tests: remove obsolete toml import from the test suite (#1978) @mgorny
  - CI: bump Poetry 1.3.1 (#2058) @staticdev

### 5.11.3 December 16 2022

  - Fixed #2007: settings for py3.11 (#2040) @staticdev
  - Fixed #2038: packaging pypoetry (#2042) @staticdev
  - Docs: renable portray (#2043) @timothycrosley
  - Ci: add minimum GitHub token permissions for workflows (#1969) @varunsh-coder
  - Ci: general CI improvements (#2041) @staticdev
  - Ci: add release workflow (#2026) @staticdev

### 5.11.2 December 12 2022

  - Hotfix #2034: isort --version is not accurate on 5.11.x releases (#2034) @gschaffner

### 5.11.1 December 12 2022

  - Hotfix #2031: only call `colorama.init` if `colorama` is available (#2032) @tomaarsen

### 5.11.0 December 12 2022

  - Added official support for Python 3.11 (#1996, #2008, #2011) @staticdev
  - Dropped support for Python 3.6 (#2019) @barrelful
  - Fixed problematic tests (#2021, #2022) @staticdev
  - Fixed #1960: Rich compatibility (#1961) @ofek
  - Fixed #1945, #1986: Python 4.0 upper bound dependency resolving issues @staticdev
  - Fixed Pyodide CDN URL (#1991) @andersk
  - Docs: clarify description of use_parentheses (#1941) @mgedmin
  - Fixed #1976: `black` compatibility for `.pyi` files @XuehaiPan
  - Implemented #1683: magic trailing comma option (#1876) @legau
  - Add missing space in unrecoverable exception message (#1933) @andersk
  - Fixed #1895: skip-gitignore: use allow list, not deny list @bmalehorn
  - Fixed #1917: infinite loop for unmatched parenthesis (#1919) @anirudnits
  - Docs: shared profiles (#1896) @matthewhughes934
  - Fixed build-backend values in the example plugins (#1892) @mgorny
  - Remove reference to jamescurtin/isort-action (#1885) @AndrewLane
  - Split long cython import lines (#1931) @davidcollins001
  - Update plone profile: copy of `black`, plus three settings. (#1926) @mauritsvanrees
  - Fixed #1815, #1862: Add a command-line flag to sort all re-exports (#1863) @parafoxia
  - Fixed #1854: `lines_before_imports` appending lines after comments (#1861) @legau
  - Remove redundant `multi_line_output = 3` from "Compatibility with black" (#1858) @jdufresne
  - Add tox config example (#1856) @umonaca
  - Docs: add examples for frozenset and tuple settings (#1822) @sgaist
  - Docs: add multiple config documentation (#1850) @anirudnits

### 5.10.1 November 8 2021
  - Fixed #1819: Occasional inconsistency with multiple src paths.
  - Fixed #1840: skip_file ignored when on the first docstring line

### 5.10.0 November 3 2021
  - Implemented #1796: Switch to `tomli` for pyproject.toml configuration loader.
  - Fixed #1801: CLI bug (--exend-skip-glob, overrides instead of extending).
  - Fixed #1802: respect PATH customization in nested calls to git.
  - Fixed #1838: Append only with certain code snippets incorrectly adds imports.
  - Added official support for Python 3.10

#### Potentially breaking changes:
  - Fixed #1785: `_ast` module incorrectly excluded from stdlib definition.

### 5.9.3 July 28 2021
  - Improved text of skipped file message to mention gitignore feature.
  - Made all exceptions pickleable.
  - Fixed #1779: Pylama integration ignores pylama specific isort config overrides.
  - Fixed #1781: `--from-first` CLI flag shouldn't take any arguments.
  - Fixed #1792: Sorting literals sometimes ignored when placed on first few lines of file.
  - Fixed #1777: extend_skip is not honored wit a git submodule when skip_gitignore=true.

### 5.9.2 July 8th 2021
  - Improved behavior of `isort --check --atomic` against Cython files.
  - Fixed #1769: Future imports added below assignments when no other imports present.
  - Fixed #1772: skip-gitignore will check files not in the git repository.
  - Fixed #1762: in some cases when skip-gitignore is set, isort fails to skip any files.
  - Fixed #1767: Encoding issues surfacing when invalid characters set in `__init__.py` files during placement.
  - Fixed #1771: Improved handling of skips against named streamed in content.

### 5.9.1 June 21st 2021 [hotfix]
  - Fixed #1758: projects with many files and skip_ignore set can lead to a command-line overload.

### 5.9.0 June 21st 2021
  - Improved CLI startup time.
  - Implemented #1697: Provisional support for PEP 582: skip `__pypackages__` directories by default.
  - Implemented #1705: More intuitive handling of isort:skip_file comments on streams.
  - Implemented #1737: Support for using action comments to avoid adding imports to individual files.
  - Implemented #1750: Ability to customize output format lines.
  - Implemented #1732: Support for custom sort functions.
  - Implemented #1722: Improved behavior for running isort in atomic mode over Cython source files.
  - Fixed (https://github.com/PyCQA/isort/pull/1695): added imports being added to doc string in some cases.
  - Fixed (https://github.com/PyCQA/isort/pull/1714): in rare cases line continuation combined with tabs can output invalid code.
  - Fixed (https://github.com/PyCQA/isort/pull/1726): isort ignores reverse_sort when force_sort_within_sections is true.
  - Fixed #1741: comments in hanging indent modes can lead to invalid code.
  - Fixed #1744: repeat noqa comments dropped when * import and non * imports exist from the same package.
  - Fixed #1721: repeat noqa comments on separate from lines with force-single-line set, sometimes get dropped.

#### Goal Zero (Tickets related to aspirational goal of achieving 0 regressions for remaining 5.0.0 lifespan):
  - Implemented #1394: 100% branch coverage (in addition to line coverage) enforced.
  - Implemented #1751: Strict typing enforcement (turned on mypy strict mode).

### 5.8.0 March 20th 2021
  - Fixed #1631: as import comments can in some cases be duplicated.
  - Fixed #1667: extra newline added with float-to-top, after skip, in some cases.
  - Fixed #1594: incorrect placement of noqa comments with multiple from imports.
  - Fixed #1566: in some cases different length limits for dos based line endings.
  - Implemented #1648: Export MyPY type hints.
  - Implemented #1641: Identified import statements now return runnable code.
  - Implemented #1661: Added "wemake" profile.
  - Implemented #1669: Parallel (`-j`) now defaults to number of CPU cores if no value is provided.
  - Implemented #1668: Added a safeguard against accidental usage against /.
  - Implemented #1638 / #1644: Provide a flag `--overwrite-in-place` to ensure same file handle is used after sorting.
  - Implemented #1684: Added support for extending skips with `--extend-skip` and `--extend-skip-glob`.
  - Implemented #1688: Auto identification and skipping of some invalid import statements.
  - Implemented #1645: Ability to reverse the import sorting order.
  - Implemented #1504: Added ability to push star imports to the top to avoid overriding explicitly defined imports.
  - Documented #1685: Skip doesn't support plain directory names, but skip_glob does.

### 5.7.0 December 30th 2020
  - Fixed #1612: In rare circumstances an extra comma is added after import and before comment.
  - Fixed #1593: isort encounters bug in Python 3.6.0.
  - Implemented #1596: Provide ways for extension formatting and file paths to be specified when using streaming input from CLI.
  - Implemented #1583: Ability to output and diff within a single API call to `isort.file`.
  - Implemented #1562, #1592 & #1593: Better more useful fatal error messages.
  - Implemented #1575: Support for automatically fixing mixed indentation of import sections.
  - Implemented #1582: Added a CLI option for skipping symlinks.
  - Implemented #1603: Support for disabling float_to_top from the command line.
  - Implemented #1604: Allow toggling section comments on and off for indented import sections.

### 5.6.4 October 12, 2020
  - Fixed #1556: Empty line added between imports that should be skipped.

### 5.6.3 October 11, 2020
  - Improved packaging of test files alongside source distribution (see: https://github.com/PyCQA/isort/pull/1555).

### 5.6.2 October 10, 2020
  - Fixed #1548: On rare occasions an unecessary empty line can be added when an import is marked as skipped.
  - Fixed #1542: Bug in VERTICAL_PREFIX_FROM_MODULE_IMPORT wrap mode.
  - Fixed #1552: Pylama test dependent on source layout.

#### Goal Zero: (Tickets related to aspirational goal of achieving 0 regressions for remaining 5.0.0 lifespan):
  - Zope added to integration test suite
  - Additional testing of CLI (simulate unseekable streams)

### 5.6.1 [Hotfix] October 8, 2020
  - Fixed #1546: Unstable (non-idempotent) behavior with certain src trees.

### 5.6.0 October 7, 2020
  - Implemented #1433: Provide helpful feedback in case a custom config file is specified without a configuration.
  - Implemented #1494: Default to sorting imports within `.pxd` files.
  - Implemented #1502: Improved float-to-top behavior when there is an existing import section present at top-of-file.
  - Implemented #1511: Support for easily seeing all files isort will be ran against using `isort . --show-files`.
  - Implemented #1487: Improved handling of encoding errors.
  - Improved handling of unsupported configuration option errors (see #1475).
  - Fixed #1463: Better interactive documentation for future option.
  - Fixed #1461: Quiet config option not respected by file API in some circumstances.
  - Fixed #1482: pylama integration is not working correctly out-of-the-box.
  - Fixed #1492: --check does not work with stdin source.
  - Fixed #1499: isort gets confused by single line, multi-line style comments when using float-to-top.
  - Fixed #1525: Some warnings can't be disabled with --quiet.
  - Fixed #1523: in rare cases isort can ignore direct from import if as import is also on same line.

#### Potentially breaking changes:
  - Implemented #1540: Officially support Python 3.9 stdlib imports by default.
  - Fixed #1443: Incorrect third vs first party categorization - namespace packages.
  - Fixed #1486: "Google" profile is not quite Google style.
  - Fixed "PyCharm" profile to always add 2 lines to be consistent with what PyCharm "Optimize Imports" does.

#### Goal Zero: (Tickets related to aspirational goal of achieving 0 regressions for remaining 5.0.0 lifespan):
  - Implemented #1472: Full testing of stdin CLI Options
  - Added additional branch coverage.
  - More projects added to integration test suite.

### 5.5.5 [Hotfix] October 7, 2020
  - Fixed #1539: in extremely rare cases isort 5.5.4 introduces syntax error by removing closing paren.

### 5.5.4 [Hotfix] September 29, 2020
  - Fixed #1507: in rare cases isort changes the content of multiline strings after a yield statement.
  - Fixed #1505: Support case where known_SECTION points to a section not listed in sections.

### 5.5.3 [Hotfix] September 20, 2020
  - Fixed #1488: in rare cases isort can mangle `yield from` or `raise from` statements.

### 5.5.2 [Hotfix] September 9, 2020
  - Fixed #1469: --diff option is ignored when input is from stdin.

### 5.5.1 September 4, 2020
  - Fixed #1454: Ensure indented import sections with import heading and a preceding comment don't cause import sorting loops.
  - Fixed #1453
... [TRUNCATED]
```

### File: docs\conf.py
```py
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "isort"
copyright = "2013-2026, Timothy Crosley"
author = "Timothy Crosley"

extensions = [
    "myst_parser",
    "sphinx_immaterial",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

html_theme = "sphinx_immaterial"
html_title = "isort"
html_static_path = ["../art"]
html_logo = "../art/logo.png"
html_favicon = "../art/logo.png"

myst_heading_anchors = 2

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
# To avoid a lot of errors about problems generating autodoc for the defaults, we ignore them.
autodoc_preserve_defaults = True
autodoc_default_options = {"members": True, "show-inheritance": True, "undoc-members": True}

html_theme_options = {
    "site_url": "https://isort.readthedocs.io/",
    "repo_url": "https://github.com/PyCQA/isort/",
    "repo_name": "isort",
    "palette": {"primary": "deep-orange", "accent": "deep-orange"},
}

```

### File: scripts\build_config_option_docs.py
```py
#! /bin/env python
import dataclasses
import os
from collections.abc import Generator, Iterable
from textwrap import dedent
from typing import Any

from isort.main import _build_arg_parser
from isort.settings import _DEFAULT_SETTINGS as config

OUTPUT_FILE = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../docs/configuration/options.md")
)
MD_NEWLINE = "  "
HUMAN_NAME = {
    "py_version": "Python Version",
    "vn": "Version Number",
    "str": "String",
    "frozenset": "List of Strings",
    "tuple": "List of Strings",
}
CONFIG_DEFAULTS = {"False": "false", "True": "true", "None": ""}
DESCRIPTIONS = {}
IGNORED = {"source", "help", "sources", "directory"}
COLUMNS = ["Name", "Type", "Default", "Python / Config file", "CLI", "Description"]
HEADER = """# Configuration options for isort

As a code formatter isort has opinions. However, it also allows you to have your own. If your opinions disagree with those of isort,
isort will disagree but commit to your way of formatting. To enable this, isort exposes a plethora of options to specify
how you want your imports sorted, organized, and formatted.

Too busy to build your perfect isort configuration? For curated common configurations, see isort's [built-in
profiles](https://isort.readthedocs.io/en/latest/configuration/profiles.html).
"""
parser = _build_arg_parser()


@dataclasses.dataclass
class Example:
    section_complete: str = ""
    cfg: str = ""
    pyproject_toml: str = ""
    cli: str = ""

    def __post_init__(self):
        if self.cfg or self.pyproject_toml or self.cli:
            if self.cfg:
                cfg = dedent(self.cfg).lstrip()
                self.cfg = (
                    dedent(
                        """
                    ### Example `.isort.cfg`

                    ```
                    [settings]
                    {cfg}
                    ```
                    """
                    )
                    .format(cfg=cfg)
                    .lstrip()
                )

            if self.pyproject_toml:
                pyproject_toml = dedent(self.pyproject_toml).lstrip()
                self.pyproject_toml = (
                    dedent(
                        """
                    ### Example `pyproject.toml`

                    ```
                    [tool.isort]
                    {pyproject_toml}
                    ```
                    """
                    )
                    .format(pyproject_toml=pyproject_toml)
                    .lstrip()
                )

            if self.cli:
                cli = dedent(self.cli).lstrip()
                self.cli = (
                    dedent(
                        """
                    ### Example cli usage

                    `{cli}`
                    """
                    )
                    .format(cli=cli)
                    .lstrip()
                )

            sections = [s for s in [self.cfg, self.pyproject_toml, self.cli] if s]
            sections_str = "\n".join(sections)
            self.section_complete = f"""**Examples:**

{sections_str}"""

        else:
            self.section_complete = ""

    def __str__(self):
        return self.section_complete


description_mapping: dict[str, str]
description_mapping = {
    "length_sort_sections": "Sort the given sections by length",
    "forced_separate": "Force certain sub modules to show separately",
    "sections": "What sections isort should display imports for and in what order",
    "known_other": "known_OTHER is how imports of custom sections are defined. "
    "OTHER is a placeholder for the custom section name.",
    "comment_prefix": "Allows customizing how isort prefixes comments that it adds or modifies on import lines"
    "Generally `  #` (two spaces before a pound symbol) is use, though one space is also common.",
    "lines_before_imports": "The number of blank lines to place before imports. -1 for automatic determination",
    "lines_after_imports": "The number of blank lines to place after imports. -1 for automatic determination",
    "lines_between_sections": "The number of lines to place between sections",
    "lines_between_types": "The number of lines to place between direct and from imports",
    "lexicographical": "Lexicographical order is strictly alphabetical order. "
    "For example by default isort will sort `1, 10, 2` into `1, 2, 10` - but with "
    "lexicographical sorting enabled it will remain `1, 10, 2`.",
    "ignore_comments": "If enabled, isort will strip comments that exist within import lines.",
    "constants": "An override list of tokens to always recognize as a CONSTANT for order_by_type regardless of casing.",
    "classes": "An override list of tokens to always recognize as a Class for order_by_type regardless of casing.",
    "variables": "An override list of tokens to always recognize as a var for order_by_type regardless of casing.",
    "auto_identify_namespace_packages": "Automatically determine local namespace packages, generally by lack of any src files before a src containing directory.",
    "namespace_packages": "Manually specify one or more namespace packages.",
    "follow_links": "If `True` isort will follow symbolic links when doing recursive sorting.",
    "git_ignore": "If `True` isort will honor ignores within locally defined .git_ignore files.",
    "formatting_function": "The fully qualified Python path of a function to apply to format code sorted by isort.",
    "group_by_package": "If `True` isort will automatically create section groups by the top-level package they come from.",
    "indented_import_headings": "If `True` isort will apply import headings to indented imports the same way it does unindented ones.",
    "import_headings": "A mapping of import sections to import heading comments that should show above them.",
    "import_footers": "A mapping of import sections to import footer comments that should show below them.",
}

example_mapping: dict[str, Example]
example_mapping = {
    "skip": Example(
        cfg="""
skip=.gitignore,.dockerignore""",
        pyproject_toml="""
skip = [".gitignore", ".dockerignore"]
""",
    ),
    "extend_skip": Example(
        cfg="""
extend_skip=.md,.json""",
        pyproject_toml="""
extend_skip = [".md", ".json"]
""",
    ),
    "skip_glob": Example(
        cfg="""
skip_glob=docs/*
""",
        pyproject_toml="""
skip_glob = ["docs/*"]
""",
    ),
    "extend_skip_glob": Example(
        cfg="""
extend_skip_glob=my_*_module.py,test/*
""",
        pyproject_toml="""
extend_skip_glob = ["my_*_module.py", "test/*"]
""",
    ),
    "known_third_party": Example(
        cfg="""
known_third_party=my_module1,my_module2
""",
        pyproject_toml="""
known_third_party = ["my_module1", "my_module2"]
""",
    ),
    "known_first_party": Example(
        cfg="""
known_first_party=my_module1,my_module2
""",
        pyproject_toml="""
known_first_party = ["my_module1", "my_module2"]
""",
    ),
    "known_local_folder": Example(
        cfg="""
known_local_folder=my_module1,my_module2
""",
        pyproject_toml="""
known_local_folder = ["my_module1", "my_module2"]
""",
    ),
    "known_standard_library": Example(
        cfg="""
known_standard_library=my_module1,my_module2
""",
        pyproject_toml="""
known_standard_library = ["my_module1", "my_module2"]
""",
    ),
    "extra_standard_library": Example(
        cfg="""
extra_standard_library=my_module1,my_module2
""",
        pyproject_toml="""
extra_standard_library = ["my_module1", "my_module2"]
""",
    ),
    "forced_separate": Example(
        cfg="""
forced_separate=glob_exp1,glob_exp2
""",
        pyproject_toml="""
forced_separate = ["glob_exp1", "glob_exp2"]
""",
    ),
    "length_sort_sections": Example(
        cfg="""
length_sort_sections=future,stdlib
""",
        pyproject_toml="""
length_sort_sections = ["future", "stdlib"]
""",
    ),
    "add_imports": Example(
        cfg="""
add_imports=import os,import json
""",
        pyproject_toml="""
add_imports = ["import os", "import json"]
""",
    ),
    "remove_imports": Example(
        cfg="""
remove_imports=os,json
""",
        pyproject_toml="""
remove_imports = ["os", "json"]
""",
    ),
    "single_line_exclusions": Example(
        cfg="""
single_line_exclusions=os,json
""",
        pyproject_toml="""
single_line_exclusions = ["os", "json"]
""",
    ),
    "no_lines_before": Example(
        cfg="""
no_lines_before=future,stdlib
""",
        pyproject_toml="""
no_lines_before = ["future", "stdlib"]
""",
    ),
    "src_paths": Example(
        cfg="""
src_paths = src,tests
""",
        pyproject_toml="""
src_paths = ["src", "tests"]
""",
    ),
    "treat_comments_as_code": Example(
        cfg="""
treat_comments_as_code = # my comment 1, # my other comment
""",
        pyproject_toml="""
treat_comments_as_code = ["# my comment 1", "# my other comment"]
""",
    ),
    "supported_extensions": Example(
        cfg="""
supported_extensions=pyw,ext
""",
        pyproject_toml="""
supported_extensions = ["pyw", "ext"]
""",
    ),
    "blocked_extensions": Example(
        cfg="""
blocked_extensions=pyw,pyc
""",
        pyproject_toml="""
blocked_extensions = ["pyw", "pyc"]
""",
    ),
    "known_other": Example(
        cfg="""
        sections=FUTURE,STDLIB,THIRDPARTY,AIRFLOW,FIRSTPARTY,LOCALFOLDER
        known_airflow=airflow""",
        pyproject_toml="""
            sections = ['FUTURE', 'STDLIB', 'THIRDPARTY', 'AIRFLOW', 'FIRSTPARTY', 'LOCALFOLDER']
            known_airflow = ['airflow']""",
    ),
    "multi_line_output": Example(cfg="multi_line_output=3", pyproject_toml="multi_line_output = 3"),
    "show_version": Example(cli="isort --version"),
    "py_version": Example(
        cli="isort --py 39",
        pyproject_toml="""
py_version=39
""",
        cfg="""
py_version=39
""",
    ),
}


@dataclasses.dataclass
class ConfigOption:
    name: str
    type: type = str
    default: Any = ""
    config_name: str = "**Not Supported**"
    cli_options: Iterable[str] = (" **Not Supported**",)
    description: str = "**No Description**"
    example: Example | None = None

    def __str__(self):
        if self.name in IGNORED:
            return ""

        if self.cli_options == (" **Not Supported**",):
            cli_options = self.cli_options[0]
        else:
            cli_options = "\n\n- " + "\n- ".join(self.cli_options)

        # new line if example otherwise nothing
        example = f"\n{self.example}" if self.example else ""
        return f"""
## {human(self.name)}

{self.description}

**Type:** {human(self.type.__name__)}{MD_NEWLINE}
**Default:** `{str(self.default) or " "}`{MD_NEWLINE}
**Config default:** `{config_default(self.default) or " "}`{MD_NEWLINE}
**Python & Config File Name:** {self.config_name}{MD_NEWLINE}
**CLI Flags:**{cli_options}
{example}"""


def config_default(default: Any) -> str:
    if isinstance(default, (frozenset, tuple)):
        default = list(default)
    default_str = str(default)
    if default_str in CONFIG_DEFAULTS:
        return CONFIG_DEFAULTS[default_str]

    if default_str.startswith("py"):
        return default_str[2:]
    return default_str


def human(name: str) -> str:
    if name in HUMAN_NAME:
        return HUMAN_NAME[name]

    return " ".join(
        part if part in ("of",) else part.capitalize() for part in name.replace("-", "_").split("_")
    )


def config_options() -> Generator[ConfigOption, None, None]:
    cli_actions = {action.dest: action for action in parser._actions}
    for name, default in config.items():
        extra_kwargs = {}
        description: str | None = description_mapping.get(name, None)

        cli = cli_actions.pop(name, None)
        if cli:
            extra_kwargs["cli_options"] = cli.option_strings
            if cli.help and not description:
                description = cli.help

        default_display = default
        if isinstance(default, (set, frozenset)) and len(default) > 0:
            default_display = tuple(sorted(default))

        # todo: refactor place for example params
        # needs to integrate with isort/settings/_Config
        # needs to integrate with isort/main/_build_arg_parser
        yield ConfigOption(
            name=name,
            type=type(default),
            default=default_display,
            config_name=name,
            description=description or "**No Description**",
            example=example_mapping.get(name, None),
            **extra_kwargs,
        )

    for name, cli in cli_actions.items():
        extra_kwargs = {}
        description: str | None = description_mapping.get(name, None)
        if cli.type:
            extra_kwargs["type"] = cli.type
        elif cli.default is not None:
            extra_kwargs["type"] = type(cli.default)

        if cli.help and not description:
            description = cli.help

        yield ConfigOption(
            name=name,
            default=cli.default,
            cli_options=cli.option_strings,
            example=example_mapping.get(name, None),
            description=description or "**No Description**",
            **extra_kwargs,
        )


def document_text() -> str:
    return f"{HEADER}{''.join(str(config_option) for config_option in config_options())}"


def write_document():
    with open(OUTPUT_FILE, "w") as output_file:
        output_file.write(document_text())


if __name__ == "__main__":
    write_document()

```

### File: scripts\build_profile_docs.py
```py
#! /bin/env python
import os
from typing import Any

from isort.profiles import profiles

OUTPUT_FILE = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../docs/configuration/profiles.md")
)

HEADER = """Built-in Profile for isort
========

The following profiles are built into isort to allow easy interoperability with
common projects and code styles.

To use any of the listed profiles, use `isort --profile PROFILE_NAME` from the command line, or `profile=PROFILE_NAME` in your configuration file.

"""


def format_profile(profile_name: str, profile: dict[str, Any]) -> str:
    options = "\n".join(f" - **{name}**: `{value!r}`" for name, value in profile.items())
    return f"""
#{profile_name}

{profile.get("description", "")}
{options}
"""


def document_text() -> str:
    return f"{HEADER}{''.join(format_profile(profile_name, profile) for profile_name, profile in profiles.items())}"


def write_document():
    with open(OUTPUT_FILE, "w") as output_file:
        output_file.write(document_text())


if __name__ == "__main__":
    write_document()

```

### File: scripts\check_acknowledgments.py
```py
#!/usr/bin/env python3
import asyncio
import sys
from getpass import getpass
from pathlib import Path

import httpx
import hug

IGNORED_AUTHOR_LOGINS = {"deepsource-autofix[bot]"}

REPO = "pycqa/isort"
GITHUB_API_CONTRIBUTORS = f"https://api.github.com/repos/{REPO}/contributors"
GITHUB_USER_CONTRIBUTIONS = f"https://github.com/{REPO}/commits?author="
GITHUB_USER_TYPE = "User"
USER_DELIMITER = "-" * 80
PER_PAGE = 100

_ACK_FILE = Path(__file__).parent.parent / "docs" / "contributing" / "4.-acknowledgements.md"
ACKNOWLEDGEMENTS = _ACK_FILE.read_text().lower()


def _user_info(user: dict[str, str], verbose=False) -> str:
    login = "@" + user["login"]
    name = user.get("name")
    display_name = f"{name} ({login})" if name else login
    user_info = f"- {display_name}"
    if verbose:
        contributions = f"  {GITHUB_USER_CONTRIBUTIONS}{user['login']}"
        user_info += "\n" + contributions
    return user_info


@hug.cli()
async def main():
    auth = (input("Github Username: "), getpass())
    async with httpx.AsyncClient() as client:
        page = 0
        results = []
        contributors = []
        while not page or len(results) == PER_PAGE:
            page += 1
            response = await client.get(
                f"{GITHUB_API_CONTRIBUTORS}?per_page={PER_PAGE}&page={page}", auth=auth
            )
            results = response.json()
            contributors.extend(
                contributor
                for contributor in results
                if contributor["type"] == GITHUB_USER_TYPE
                and contributor["login"] not in IGNORED_AUTHOR_LOGINS
                and f"@{contributor['login'].lower()}" not in ACKNOWLEDGEMENTS
            )

        unacknowledged_users = await asyncio.gather(
            *(client.get(contributor["url"], auth=auth) for contributor in contributors)
        )
        unacknowledged_users = [request.json() for request in unacknowledged_users]

        if not unacknowledged_users:
            sys.exit()

        print("Found unacknowledged authors:")
        print()

        for user in unacknowledged_users:
            print(_user_info(user, verbose=True))
            print(USER_DELIMITER)

        print()
        print("Printing again for easy inclusion in Markdown file:")
        print()
        for user in unacknowledged_users:
            print(_user_info(user))

        sys.exit(1)


if __name__ == "__main__":
    main.interface.cli()

```

### File: scripts\clean.sh
```sh
#!/usr/bin/env bash
set -euxo pipefail

uv run isort --profile hug isort/ tests/ scripts/
uv run isort --profile hug example_*/
uv run ruff format

```

### File: scripts\docker.sh
```sh
#!/usr/bin/env bash
set -ux

result=0

for ver in {3.10,3.11,3.12,3.13,3.14,3.15}; do
	# latest tag will override after each build, leaving only the newest python version tagged
	docker build ./ --build-arg VERSION=$ver -t "isort:$ver" -t "isort:latest" && docker run "isort:$ver"
	result=$(( $? + $result ))
done

exit $result

```

### File: scripts\done.sh
```sh
#!/usr/bin/env bash
set -euxo pipefail

./scripts/clean.sh
./scripts/test.sh

```

### File: scripts\mkstdlibs.py
```py
#!/usr/bin/env python3
import re

from stdlibs import py38, py39, py310, py311, py312, py313, py314, py315

PATH = "isort/stdlibs/py{}.py"
VERSIONS = [
    py38,
    py39,
    py310,
    py311,
    py312,
    py313,
    py314,
    py315,
]

DOCSTRING = """
File contains the standard library of Python {}.

DO NOT EDIT. If the standard library changes, a new list should be created
using the mkstdlibs.py script.
"""


for version_module in VERSIONS:
    version_match = re.match(
        r"^stdlibs\.py(?P<major>\d)(?P<minor>\d+)$",
        version_module.__name__,
    )
    version_info = (version_match.groupdict()["major"], version_match.groupdict()["minor"])

    path = PATH.format("".join(version_info))
    with open(path, "w") as stdlib_file:
        docstring = DOCSTRING.format(".".join(version_info))
        stdlib_file.write(f'"""{docstring}"""\n\n')
        stdlib_file.write("stdlib = {\n")
        for module in sorted(version_module.module_names):
            stdlib_file.write(f'    "{module}",\n')
        stdlib_file.write("}\n")

```

### File: scripts\test.sh
```sh
#!/usr/bin/env bash
set -euxo pipefail

uv run coverage run --parallel -m pytest tests/unit/ -s
uv run coverage combine
uv run coverage report
uv run coverage xml

```

### File: scripts\test_integration.sh
```sh
#!/usr/bin/env bash
set -euxo pipefail

uv run pytest tests/integration/ -s

```

### File: tests\__init__.py
```py

```

### File: docs\configuration\action_comments.md
```md
# Action comments

The most basic way to configure the flow of isort within a single file is action comments. These comments are picked up and interpreted by the isort parser during parsing.


## isort: skip_file

Tells isort to skip the entire file.

Example:

```python
# !/bin/python3
# isort: skip_file
import os
import sys

...
```

!!! warning
    This should be placed as high in the file as reasonably possible.
    Since isort uses a streaming architecture, it may have already completed some work before it reaches the comment. Usually, this is okay - but can be confusing if --diff or any interactive options are used from the command line.


## isort: skip

If placed on the same line as (or within the continuation of a) an import statement, isort will not sort this import.
More specifically, it prevents the import statement from being recognized by isort as an import. In consequence, this line will be treated as code and be pushed down to below the import section of the file.

Example:

```python
import b
import a # isort: skip <- this will now stay below b
```
!!! note
    It is recommended to where possible use `# isort: off` and `# isort: on` or `# isort: split` instead as the behavior is more explicit and predictable.

## isort: off

Turns isort parsing off. Every line after an `# isort: off` statement will be passed along unchanged until an `# isort: on` comment or the end of the file.

Example:

```python
import e
import f

# isort: off

import b
import a
```

## isort: on

Turns isort parsing back on. This only makes sense if an `# isort: off` comment exists higher in the file! This allows you to have blocks of unsorted imports, around otherwise sorted ones.

Example:

```python

import e
import f

# isort: off

import b
import a

# isort: on

import c
import d

```

## isort: split

Tells isort the current sort section is finished, and all future imports belong to a new sort grouping.

Example:

```python

import e
import f

# isort: split

import a
import b
import c
import d

```

You can also use it inline to keep an import from having imports above or below it swap position:

```python
import c
import b  # isort: split
import a
```

!!! tip
    isort split is exactly the same as placing an `# isort: on` immediately below an `# isort: off`


## isort: dont-add-imports

Tells isort to not automatically add imports to this file, even if --add-imports is set.

## isort: dont-add-import: [IMPORT_LINE]

Tells isort to not automatically add a particular import, even if --add-imports says to add it.

```

### File: docs\configuration\add_or_remove_imports.md
```md
# Add or remove imports

## Adding an import to multiple files

isort makes it easy to add an import statement across multiple files,
while being assured it's correctly placed.

To add an import to all files:

```bash
isort -a "from __future__ import print_function" *.py
```

To add an import only to files that already have imports:

```bash
isort -a "from __future__ import print_function" --append-only *.py
```

## Removing an import from multiple files

isort also makes it easy to remove an import from multiple files,
without having to be concerned with how it was originally formatted.

From the command line:

```bash
isort --rm "os.system" *.py
```

```

### File: docs\configuration\black_compatibility.md
```md
![isort loves black](https://raw.githubusercontent.com/pycqa/isort/main/art/isort_loves_black.png)

# Compatibility with black

Compatibility with black is very important to the isort project and comes baked in starting with version 5.
All that's required to use isort alongside black is to set the isort profile to "black".

!!! tip
    Beyond the profile, it is common to set [skip_gitignore](./options.md#skip-gitignore) (which is not enabled by default for isort as it requires git to be installed) and [line_length](./options.md#line-length) as it is common to deviate from black's default of 88.


## Using a config file (such as .isort.cfg)

For projects that officially use both isort and black, we recommend setting the black profile in a config file at the root of your project's repository.
That way it's independent of how users call isort (pre-commit, CLI, or editor integration) the black profile will automatically be applied.

For instance, your _pyproject.toml_ file would look something like

```ini
[tool.isort]
profile = "black"
```

Read More about supported [config files](./config_files.md).

## CLI

To use the profile option when calling isort directly from the commandline simply add the --profile black argument: `isort --profile black`.

A demo of how this would look like in your _.travis.yml_

```yaml
language: python
python:
  - "3.10"

install:
  - pip install -r requirements-dev.txt
  - pip install isort black
  - pip install coveralls
script:
  - pytest my-package
  - isort --profile black my-package
  - black --check --diff my-package
after_success:
  - coveralls

```

See [built-in profiles](./profiles.md) for more profiles.

## Integration with pre-commit

You can also set the profile directly when integrating isort within pre-commit.

```yaml
  - repo: https://github.com/pycqa/isort
    rev: 6.0.1
    hooks:
      - id: isort
        args: ["--profile", "black", "--filter-files"]
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
