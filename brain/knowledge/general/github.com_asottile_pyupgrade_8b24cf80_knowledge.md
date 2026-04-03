---
id: github.com-asottile-pyupgrade-8b24cf80-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:33.035514
---

# KNOWLEDGE EXTRACT: github.com_asottile_pyupgrade_8b24cf80
> **Extracted on:** 2026-04-01 13:27:21
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522464/github.com_asottile_pyupgrade_8b24cf80

---

## File: `.gitignore`
```
*.egg-info
*.pyc
/.coverage
/.tox
```

## File: `.pre-commit-config.yaml`
```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: debug-statements
    -   id: double-quote-string-fixer
    -   id: name-tests-test
    -   id: requirements-txt-fixer
-   repo: https://github.com/asottile/setup-cfg-fmt
    rev: v3.2.0
    hooks:
    -   id: setup-cfg-fmt
-   repo: https://github.com/asottile/reorder-python-imports
    rev: v3.16.0
    hooks:
    -   id: reorder-python-imports
        args: [--py310-plus, --add-import, 'from __future__ import annotations']
-   repo: https://github.com/asottile/add-trailing-comma
    rev: v4.0.0
    hooks:
    -   id: add-trailing-comma
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
```

## File: `.pre-commit-hooks.yaml`
```yaml
-   id: pyupgrade
    name: pyupgrade
    description: Automatically upgrade syntax for newer versions.
    entry: pyupgrade
    language: python
    types: [python]
    # for backward compatibility
    files: ''
    minimum_pre_commit_version: 0.15.0
```

## File: `LICENSE`
```
Copyright (c) 2017 Anthony Sottile

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `README.md`
```markdown
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

```diff
 # ok: printing an empty tuple
 print(())
 # ok: printing a tuple
 print((1,))
 # ok: parenthesized generator argument
 sum((i for i in range(3)), [])
 # fixed:
-print(("foo"))
+print("foo")
```

[python-modernize/python-modernize#178]: https://github.com/python-modernize/python-modernize/issues/178

### constant fold `isinstance` / `issubclass` / `except`

```diff
-isinstance(x, (int, int))
+isinstance(x, int)

-issubclass(y, (str, str))
+issubclass(y, str)

 try:
     raises()
-except (Error1, Error1, Error2):
+except (Error1, Error2):
     pass
```

### unittest deprecated aliases

Rewrites [deprecated unittest method aliases](https://docs.python.org/3/library/unittest.html#deprecated-aliases) to their non-deprecated forms.

```diff
 from unittest import TestCase


 class MyTests(TestCase):
     def test_something(self):
-        self.failUnlessEqual(1, 1)
+        self.assertEqual(1, 1)
-        self.assertEquals(1, 1)
+        self.assertEqual(1, 1)
```

### `super()` calls

```diff
 class C(Base):
     def f(self):
-        super(C, self).f()
+        super().f()
```

### "new style" classes

#### rewrites class declaration

```diff
-class C(object): pass
+class C: pass
-class C(B, object): pass
+class C(B): pass
```

#### removes `__metaclass__ = type` declaration

```diff
 class C:
-    __metaclass__ = type
```

### forced `str("native")` literals

```diff
-str()
+''
-str("foo")
+"foo"
```

### `.encode("utf-8")`

```diff
-"foo".encode("utf-8")
+"foo".encode()
```

### `# coding: ...` comment

as of [PEP 3120], the default encoding for python source is UTF-8

```diff
-# coding: utf-8
 x = 1
```

[PEP 3120]: https://www.python.org/dev/peps/pep-3120/

### `__future__` import removal

Availability:
- by default removes `nested_scopes`, `generators`, `with_statement`,
  `absolute_import`, `division`, `print_function`, `unicode_literals`
- `--py37-plus` will also remove `generator_stop`

```diff
-from __future__ import with_statement
```

### Remove unnecessary py3-compat imports

```diff
-from io import open
-from six.moves import map
-from builtins import object  # python-future
```

### import replacements

Availability:
- `--py36-plus` (and others) will replace imports

see also [reorder-python-imports](https://github.com/asottile/reorder_python_imports#removing--rewriting-obsolete-six-imports)

some examples:

```diff
-from collections import deque, Mapping
+from collections import deque
+from collections.abc import Mapping
```

```diff
-from typing import Sequence
+from collections.abc import Sequence
```

```diff
-from typing_extensions import Concatenate
+from typing import Concatenate
```

### rewrite `mock` imports

Availability:
- [Unless `--keep-mock` is passed on the commandline](https://github.com/asottile/pyupgrade/issues/314).

```diff
-from mock import patch
+from unittest.mock import patch
```

### `yield` => `yield from`

```diff
 def f():
-    for x in y:
-        yield x
+    yield from y
-    for a, b in c:
-        yield (a, b)
+    yield from c
```

### Python2 and old Python3.x blocks

```diff
 import sys
-if sys.version_info < (3,):  # also understands `six.PY2` (and `not`), `six.PY3` (and `not`)
-    print('py2')
-else:
-    print('py3')
+print('py3')
```

Availability:
- `--py36-plus` will remove Python <= 3.5 only blocks
- `--py37-plus` will remove Python <= 3.6 only blocks
- so on and so forth

```diff
 # using --py36-plus for this example

 import sys
-if sys.version_info < (3, 6):
-    print('py3.5')
-else:
-    print('py3.6+')
+print('py3.6+')

-if sys.version_info <= (3, 5):
-    print('py3.5')
-else:
-    print('py3.6+')
+print('py3.6+')

-if sys.version_info >= (3, 6):
-    print('py3.6+')
-else:
-    print('py3.5')
+print('py3.6+')
```

Note that `if` blocks without an `else` will not be rewritten as it could introduce a syntax error.

### remove `six` compatibility code

```diff
-six.text_type
+str
-six.binary_type
+bytes
-six.class_types
+(type,)
-six.string_types
+(str,)
-six.integer_types
+(int,)
-six.unichr
+chr
-six.iterbytes
+iter
-six.print_(...)
+print(...)
-six.exec_(c, g, l)
+exec(c, g, l)
-six.advance_iterator(it)
+next(it)
-six.next(it)
+next(it)
-six.callable(x)
+callable(x)
-six.moves.range(x)
+range(x)
-six.moves.xrange(x)
+range(x)


-from six import text_type
-text_type
+str

-@six.python_2_unicode_compatible
 class C:
     def __str__(self):
         return u'C()'

-class C(six.Iterator): pass
+class C: pass

-class C(six.with_metaclass(M, B)): pass
+class C(B, metaclass=M): pass

-@six.add_metaclass(M)
-class C(B): pass
+class C(B, metaclass=M): pass

-isinstance(..., six.class_types)
+isinstance(..., type)
-issubclass(..., six.integer_types)
+issubclass(..., int)
-isinstance(..., six.string_types)
+isinstance(..., str)

-six.b('...')
+b'...'
-six.u('...')
+'...'
-six.byte2int(bs)
+bs[0]
-six.indexbytes(bs, i)
+bs[i]
-six.int2byte(i)
+bytes((i,))
-six.iteritems(dct)
+dct.items()
-six.iterkeys(dct)
+dct.keys()
-six.itervalues(dct)
+dct.values()
-next(six.iteritems(dct))
+next(iter(dct.items()))
-next(six.iterkeys(dct))
+next(iter(dct.keys()))
-next(six.itervalues(dct))
+next(iter(dct.values()))
-six.viewitems(dct)
+dct.items()
-six.viewkeys(dct)
+dct.keys()
-six.viewvalues(dct)
+dct.values()
-six.create_unbound_method(fn, cls)
+fn
-six.get_unbound_function(meth)
+meth
-six.get_method_function(meth)
+meth.__func__
-six.get_method_self(meth)
+meth.__self__
-six.get_function_closure(fn)
+fn.__closure__
-six.get_function_code(fn)
+fn.__code__
-six.get_function_defaults(fn)
+fn.__defaults__
-six.get_function_globals(fn)
+fn.__globals__
-six.raise_from(exc, exc_from)
+raise exc from exc_from
-six.reraise(tp, exc, tb)
+raise exc.with_traceback(tb)
-six.reraise(*sys.exc_info())
+raise
-six.assertCountEqual(self, a1, a2)
+self.assertCountEqual(a1, a2)
-six.assertRaisesRegex(self, e, r, fn)
+self.assertRaisesRegex(e, r, fn)
-six.assertRegex(self, s, r)
+self.assertRegex(s, r)

 # note: only for *literals*
-six.ensure_binary('...')
+b'...'
-six.ensure_str('...')
+'...'
-six.ensure_text('...')
+'...'
```

### `open` alias

```diff
-with io.open('f.txt') as f:
+with open('f.txt') as f:
     ...
```


### redundant `open` modes

```diff
-open("foo", "U")
+open("foo")
-open("foo", "Ur")
+open("foo")
-open("foo", "Ub")
+open("foo", "rb")
-open("foo", "rUb")
+open("foo", "rb")
-open("foo", "r")
+open("foo")
-open("foo", "rt")
+open("foo")
-open("f", "r", encoding="UTF-8")
+open("f", encoding="UTF-8")
-open("f", "wt")
+open("f", "w")
```


### `OSError` aliases

```diff
 # also understands:
 # - IOError
 # - WindowsError
 # - mmap.error and uses of `from mmap import error`
 # - select.error and uses of `from select import error`
 # - socket.error and uses of `from socket import error`

 def throw():
-    raise EnvironmentError('boom')
+    raise OSError('boom')

 def catch():
     try:
         throw()
-    except EnvironmentError:
+    except OSError:
         handle_error()
```

### `TimeoutError` aliases

Availability:
- `--py310-plus` for `socket.timeout`
- `--py311-plus` for `asyncio.TimeoutError`

```diff

 def throw(a):
     if a:
-        raise asyncio.TimeoutError('boom')
+        raise TimeoutError('boom')
     else:
-        raise socket.timeout('boom')
+        raise TimeoutError('boom')

 def catch(a):
     try:
         throw(a)
-    except (asyncio.TimeoutError, socket.timeout):
+    except TimeoutError:
         handle_error()
```

### `typing.Text` str alias

```diff
-def f(x: Text) -> None:
+def f(x: str) -> None:
     ...
```


### Unpacking list comprehensions

```diff
-foo, bar, baz = [fn(x) for x in items]
+foo, bar, baz = (fn(x) for x in items)
```


### Rewrite `xml.etree.cElementTree` to `xml.etree.ElementTree`

```diff
-import xml.etree.cElementTree as ET
+import xml.etree.ElementTree as ET
-from xml.etree.cElementTree import XML
+from xml.etree.ElementTree import XML
```


### Rewrite `type` of primitive

```diff
-type('')
+str
-type(b'')
+bytes
-type(0)
+int
-type(0.)
+float
```

### `typing.NamedTuple` / `typing.TypedDict` py36+ syntax

Availability:
- `--py36-plus` is passed on the commandline.

```diff
-NT = typing.NamedTuple('NT', [('a', int), ('b', Tuple[str, ...])])
+class NT(typing.NamedTuple):
+    a: int
+    b: Tuple[str, ...]

-D1 = typing.TypedDict('D1', a=int, b=str)
+class D1(typing.TypedDict):
+    a: int
+    b: str

-D2 = typing.TypedDict('D2', {'a': int, 'b': str})
+class D2(typing.TypedDict):
+    a: int
+    b: str
```

### f-strings

Availability:
- `--py36-plus` is passed on the commandline.

```diff
-'{foo} {bar}'.format(foo=foo, bar=bar)
+f'{foo} {bar}'
-'{} {}'.format(foo, bar)
+f'{foo} {bar}'
-'{} {}'.format(foo.bar, baz.womp)
+f'{foo.bar} {baz.womp}'
-'{} {}'.format(f(), g())
+f'{f()} {g()}'
-'{x}'.format(**locals())
+f'{x}'
```

_note_: `pyupgrade` is intentionally timid and will not create an f-string
if it would make the expression longer or if the substitution parameters are
sufficiently complicated (as this can decrease readability).


### `subprocess.run`: replace `universal_newlines` with `text`

Availability:
- `--py37-plus` is passed on the commandline.

```diff
-output = subprocess.run(['foo'], universal_newlines=True)
+output = subprocess.run(['foo'], text=True)
```


### `subprocess.run`: replace `stdout=subprocess.PIPE, stderr=subprocess.PIPE` with `capture_output=True`

Availability:
- `--py37-plus` is passed on the commandline.

```diff
-output = subprocess.run(['foo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
+output = subprocess.run(['foo'], capture_output=True)
```


### remove parentheses from `@functools.lru_cache()`

Availability:
- `--py38-plus` is passed on the commandline.

```diff
 import functools

-@functools.lru_cache()
+@functools.lru_cache
 def expensive():
     ...
```

### shlex.join

Availability:
- `--py38-plus` is passed on the commandline.

```diff
-' '.join(shlex.quote(arg) for arg in cmd)
+shlex.join(cmd)
```

### replace `@functools.lru_cache(maxsize=None)` with shorthand

Availability:
- `--py39-plus` is passed on the commandline.

```diff
 import functools

-@functools.lru_cache(maxsize=None)
+@functools.cache
 def expensive():
     ...
```


### pep 585 typing rewrites

Availability:
- File imports `from __future__ import annotations`
    - Unless `--keep-runtime-typing` is passed on the commandline.
- `--py39-plus` is passed on the commandline.

```diff
-def f(x: List[str]) -> None:
+def f(x: list[str]) -> None:
     ...
```


### pep 604 typing rewrites

Availability:
- File imports `from __future__ import annotations`
    - Unless `--keep-runtime-typing` is passed on the commandline.
- `--py310-plus` is passed on the commandline.

```diff
-def f() -> Optional[str]:
+def f() -> str | None:
     ...
```

```diff
-def f() -> Union[int, str]:
+def f() -> int | str:
     ...
```

### pep 696 TypeVar defaults

Availability:
- File imports `from __future__ import annotations`
    - Unless `--keep-runtime-typing` is passed on the commandline.
- `--py313-plus` is passed on the commandline.

```diff
-def f() -> Generator[int, None, None]:
+def f() -> Generator[int]:
     yield 1
```

```diff
-async def f() -> AsyncGenerator[int, None]:
+async def f() -> AsyncGenerator[int]:
     yield 1
```

### remove quoted annotations

Availability:
- File imports `from __future__ import annotations`

```diff
-def f(x: 'queue.Queue[int]') -> C:
+def f(x: queue.Queue[int]) -> C:
```


### use `datetime.UTC` alias

Availability:
- `--py311-plus` is passed on the commandline.

```diff
 import datetime

-datetime.timezone.utc
+datetime.UTC
```
```

## File: `requirements-dev.txt`
```
covdefaults>=2.1.0
coverage
pytest
```

## File: `setup.cfg`
```
[metadata]
name = pyupgrade
version = 3.21.2
description = A tool to automatically upgrade syntax for newer versions.
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/asottile/pyupgrade
author = Anthony Sottile
author_email = asottile@umich.edu
license = MIT
license_files = LICENSE
classifiers =
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy

[options]
packages = find:
install_requires =
    tokenize-rt>=6.1.0
python_requires = >=3.10

[options.packages.find]
exclude =
    tests*
    testing*

[options.entry_points]
console_scripts =
    pyupgrade = pyupgrade._main:main

[bdist_wheel]
universal = True

[coverage:run]
plugins = covdefaults

[mypy]
check_untyped_defs = true
disallow_any_generics = true
disallow_incomplete_defs = true
disallow_untyped_defs = true
warn_redundant_casts = true
warn_unused_ignores = true

[mypy-testing.*]
disallow_untyped_defs = false

[mypy-tests.*]
disallow_untyped_defs = false
```

## File: `setup.py`
```python
from __future__ import annotations

from setuptools import setup
setup()
```

## File: `tox.ini`
```
[tox]
envlist = py,pypy3,pre-commit

[testenv]
deps = -rrequirements-dev.txt
commands =
    coverage erase
    coverage run -m pytest {posargs:tests}
    coverage report

[testenv:pre-commit]
skip_install = true
deps = pre-commit
commands = pre-commit run --all-files --show-diff-on-failure

[pep8]
ignore = E265,E501,W504
```

## File: `pyupgrade/__main__.py`
```python
from __future__ import annotations

from pyupgrade._main import main

if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pyupgrade/_ast_helpers.py`
```python
from __future__ import annotations

import ast
import warnings
from collections.abc import Container

from tokenize_rt import Offset


def ast_parse(contents_text: str) -> ast.Module:
    # intentionally ignore warnings, we might be fixing warning-ridden syntax
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return ast.parse(contents_text.encode())


def ast_to_offset(node: ast.expr | ast.stmt) -> Offset:
    return Offset(node.lineno, node.col_offset)


def is_name_attr(
        node: ast.AST,
        imports: dict[str, set[str]],
        mods: tuple[str, ...],
        names: Container[str],
) -> bool:
    return (
        isinstance(node, ast.Name) and
        node.id in names and
        any(node.id in imports[mod] for mod in mods)
    ) or (
        isinstance(node, ast.Attribute) and
        isinstance(node.value, ast.Name) and
        node.value.id in mods and
        node.attr in names
    )


def has_starargs(call: ast.Call) -> bool:
    return (
        any(k.arg is None for k in call.keywords) or
        any(isinstance(a, ast.Starred) for a in call.args)
    )


def contains_await(node: ast.AST) -> bool:
    for node_ in ast.walk(node):
        if isinstance(node_, ast.Await):
            return True
    else:
        return False


def is_async_listcomp(node: ast.ListComp) -> bool:
    return (
        any(gen.is_async for gen in node.generators) or
        contains_await(node)
    )


def is_type_check(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Call) and
        isinstance(node.func, ast.Name) and
        node.func.id in {'isinstance', 'issubclass'} and
        len(node.args) == 2 and
        not has_starargs(node)
    )
```

## File: `pyupgrade/_data.py`
```python
from __future__ import annotations

import ast
import collections
import pkgutil
from collections.abc import Callable
from collections.abc import Iterable
from typing import NamedTuple
from typing import Protocol
from typing import TypeVar

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade import _plugins

Version = tuple[int, ...]


class Settings(NamedTuple):
    min_version: Version = (3,)
    keep_percent_format: bool = False
    keep_mock: bool = False
    keep_runtime_typing: bool = False


class State(NamedTuple):
    settings: Settings
    from_imports: dict[str, set[str]]
    in_annotation: bool = False


AST_T = TypeVar('AST_T', bound=ast.AST)
TokenFunc = Callable[[int, list[Token]], None]
ASTFunc = Callable[[State, AST_T, ast.AST], Iterable[tuple[Offset, TokenFunc]]]

RECORD_FROM_IMPORTS = frozenset((
    '__future__',
    'asyncio',
    'collections',
    'collections.abc',
    'functools',
    'mmap',
    'os',
    'select',
    'six',
    'six.moves',
    'socket',
    'subprocess',
    'sys',
    'typing',
    'typing_extensions',
))

FUNCS: ASTCallbackMapping  # python/mypy#17566
FUNCS = collections.defaultdict(list)  # type: ignore[assignment]


def register(tp: type[AST_T]) -> Callable[[ASTFunc[AST_T]], ASTFunc[AST_T]]:
    def register_decorator(func: ASTFunc[AST_T]) -> ASTFunc[AST_T]:
        FUNCS[tp].append(func)
        return func
    return register_decorator


class ASTCallbackMapping(Protocol):
    def __getitem__(self, tp: type[AST_T]) -> list[ASTFunc[AST_T]]: ...


def visit(
        funcs: ASTCallbackMapping,
        tree: ast.Module,
        settings: Settings,
) -> dict[Offset, list[TokenFunc]]:
    initial_state = State(
        settings=settings,
        from_imports=collections.defaultdict(set),
    )

    nodes: list[tuple[State, ast.AST, ast.AST]] = [(initial_state, tree, tree)]

    ret = collections.defaultdict(list)
    while nodes:
        state, node, parent = nodes.pop()

        tp = type(node)
        for ast_func in funcs[tp]:
            for offset, token_func in ast_func(state, node, parent):
                ret[offset].append(token_func)

        if (
                isinstance(node, ast.ImportFrom) and
                not node.level and
                node.module in RECORD_FROM_IMPORTS
        ):
            state.from_imports[node.module].update(
                name.name for name in node.names if not name.asname
            )

        for name in reversed(node._fields):
            value = getattr(node, name)
            if name in {'annotation', 'returns'}:
                next_state = state._replace(in_annotation=True)
            else:
                next_state = state

            if isinstance(value, ast.AST):
                nodes.append((next_state, value, node))
            elif isinstance(value, list):
                for value in reversed(value):
                    if isinstance(value, ast.AST):
                        nodes.append((next_state, value, node))
    return ret


def _import_plugins() -> None:
    plugins_path = _plugins.__path__
    mod_infos = pkgutil.walk_packages(plugins_path, f'{_plugins.__name__}.')
    for _, name, _ in mod_infos:
        __import__(name, fromlist=['_trash'])


_import_plugins()
```

## File: `pyupgrade/_main.py`
```python
from __future__ import annotations

import argparse
import ast
import re
import sys
import tokenize
from collections.abc import Sequence
from re import Match

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import parse_string_literal
from tokenize_rt import reversed_enumerate
from tokenize_rt import rfind_string_parts
from tokenize_rt import src_to_tokens
from tokenize_rt import Token
from tokenize_rt import tokens_to_src
from tokenize_rt import UNIMPORTANT_WS

from pyupgrade._ast_helpers import ast_parse
from pyupgrade._data import FUNCS
from pyupgrade._data import Settings
from pyupgrade._data import visit
from pyupgrade._string_helpers import DotFormatPart
from pyupgrade._string_helpers import is_codec
from pyupgrade._string_helpers import parse_format
from pyupgrade._string_helpers import unparse_parsed_string
from pyupgrade._token_helpers import is_close
from pyupgrade._token_helpers import is_open
from pyupgrade._token_helpers import remove_brace


def inty(s: str) -> bool:
    try:
        int(s)
        return True
    except (ValueError, TypeError):
        return False


def _fixup_dedent_tokens(tokens: list[Token]) -> None:
    """For whatever reason the DEDENT / UNIMPORTANT_WS tokens are misordered

    | if True:
    |     if True:
    |         pass
    |     else:
    |^    ^- DEDENT
    |+----UNIMPORTANT_WS
    """
    for i, token in enumerate(tokens):
        if token.name == UNIMPORTANT_WS and tokens[i + 1].name == 'DEDENT':
            tokens[i], tokens[i + 1] = tokens[i + 1], tokens[i]


def _fix_plugins(contents_text: str, settings: Settings) -> str:
    try:
        ast_obj = ast_parse(contents_text)
    except SyntaxError:
        return contents_text

    callbacks = visit(FUNCS, ast_obj, settings)

    if not callbacks:
        return contents_text

    try:
        tokens = src_to_tokens(contents_text)
    except tokenize.TokenError:  # pragma: no cover (bpo-2180)
        return contents_text

    _fixup_dedent_tokens(tokens)

    for i, token in reversed_enumerate(tokens):
        if not token.src:
            continue
        # though this is a defaultdict, by using `.get()` this function's
        # self time is almost 50% faster
        for callback in callbacks.get(token.offset, ()):
            callback(i, tokens)

    return tokens_to_src(tokens).lstrip()


# https://docs.python.org/3/reference/lexical_analysis.html
ESCAPE_STARTS = frozenset((
    '\n', '\r', '\\', "'", '"', 'a', 'b', 'f', 'n', 'r', 't', 'v',
    '0', '1', '2', '3', '4', '5', '6', '7',  # octal escapes
    'x',  # hex escapes
))
ESCAPE_RE = re.compile(r'\\.', re.DOTALL)
NAMED_ESCAPE_NAME = re.compile(r'\{[^}]+\}')


def _fix_escape_sequences(token: Token) -> Token:
    prefix, rest = parse_string_literal(token.src)
    actual_prefix = prefix.lower()

    if 'r' in actual_prefix or '\\' not in rest:
        return token

    is_bytestring = 'b' in actual_prefix

    def _is_valid_escape(match: Match[str]) -> bool:
        c = match.group()[1]
        return (
            c in ESCAPE_STARTS or
            (not is_bytestring and c in 'uU') or
            (
                not is_bytestring and
                c == 'N' and
                bool(NAMED_ESCAPE_NAME.match(rest, match.end()))
            )
        )

    has_valid_escapes = False
    has_invalid_escapes = False
    for match in ESCAPE_RE.finditer(rest):
        if _is_valid_escape(match):
            has_valid_escapes = True
        else:
            has_invalid_escapes = True

    def cb(match: Match[str]) -> str:
        matched = match.group()
        if _is_valid_escape(match):
            return matched
        else:
            return fr'\{matched}'

    if has_invalid_escapes and (has_valid_escapes or 'u' in actual_prefix):
        return token._replace(src=prefix + ESCAPE_RE.sub(cb, rest))
    elif has_invalid_escapes and not has_valid_escapes:
        return token._replace(src=prefix + 'r' + rest)
    else:
        return token


def _remove_u_prefix(token: Token) -> Token:
    prefix, rest = parse_string_literal(token.src)
    if 'u' not in prefix.lower():
        return token
    else:
        new_prefix = prefix.replace('u', '').replace('U', '')
        return token._replace(src=new_prefix + rest)


def _fix_extraneous_parens(tokens: list[Token], i: int) -> None:
    # search forward for another non-coding token
    i += 1
    while tokens[i].name in NON_CODING_TOKENS:
        i += 1
    # if we did not find another brace, return immediately
    if tokens[i].src != '(':
        return

    start = i
    depth = 1
    while depth:
        i += 1
        # found comma or yield at depth 1: this is a tuple / coroutine
        if depth == 1 and tokens[i].src in {',', 'yield'}:
            return
        elif is_open(tokens[i]):
            depth += 1
        elif is_close(tokens[i]):
            depth -= 1
    end = i

    # empty tuple
    if all(t.name in NON_CODING_TOKENS for t in tokens[start + 1:i]):
        return

    # search forward for the next non-coding token
    i += 1
    while tokens[i].name in NON_CODING_TOKENS:
        i += 1

    if tokens[i].src == ')':
        remove_brace(tokens, end)
        remove_brace(tokens, start)


def _remove_fmt(tup: DotFormatPart) -> DotFormatPart:
    if tup[1] is None:
        return tup
    else:
        return (tup[0], '', tup[2], tup[3])


def _fix_format_literal(tokens: list[Token], end: int) -> None:
    parts = rfind_string_parts(tokens, end)
    parsed_parts = []
    last_int = -1
    for i in parts:
        # f'foo {0}'.format(...) would get turned into a SyntaxError
        prefix, _ = parse_string_literal(tokens[i].src)
        if 'f' in prefix.lower():  # pragma: <3.12 cover
            return

        try:
            parsed = parse_format(tokens[i].src)
        except ValueError:
            # the format literal was malformed, skip it
            return

        # The last segment will always be the end of the string and not a
        # format, slice avoids the `None` format key
        for _, fmtkey, spec, _ in parsed[:-1]:
            if (
                    fmtkey is not None and inty(fmtkey) and
                    int(fmtkey) == last_int + 1 and
                    spec is not None and '{' not in spec
            ):
                last_int += 1
            else:
                return

        parsed_parts.append([_remove_fmt(tup) for tup in parsed])

    for i, parsed in zip(parts, parsed_parts):
        tokens[i] = tokens[i]._replace(src=unparse_parsed_string(parsed))


def _fix_encode_to_binary(tokens: list[Token], i: int) -> None:
    parts = rfind_string_parts(tokens, i - 2)
    if not parts:
        return

    # .encode()
    if (
            i + 2 < len(tokens) and
            tokens[i + 1].src == '(' and
            tokens[i + 2].src == ')'
    ):
        victims = slice(i - 1, i + 3)
        latin1_ok = False
    # .encode('encoding')
    elif (
            i + 3 < len(tokens) and
            tokens[i + 1].src == '(' and
            tokens[i + 2].name == 'STRING' and
            tokens[i + 3].src == ')'
    ):
        victims = slice(i - 1, i + 4)
        prefix, rest = parse_string_literal(tokens[i + 2].src)
        if 'f' in prefix.lower():  # pragma: <3.12 cover
            return
        encoding = ast.literal_eval(prefix + rest)
        if is_codec(encoding, 'ascii') or is_codec(encoding, 'utf-8'):
            latin1_ok = False
        elif is_codec(encoding, 'iso8859-1'):
            latin1_ok = True
        else:
            return
    else:
        return

    for part in parts:
        prefix, rest = parse_string_literal(tokens[part].src)
        escapes = set(ESCAPE_RE.findall(rest))
        if (
                not rest.isascii() or
                '\\u' in escapes or
                '\\U' in escapes or
                '\\N' in escapes or
                ('\\x' in escapes and not latin1_ok) or
                'f' in prefix.lower()
        ):
            return

    for part in parts:
        prefix, rest = parse_string_literal(tokens[part].src)
        prefix = 'b' + prefix.replace('u', '').replace('U', '')
        tokens[part] = tokens[part]._replace(src=prefix + rest)
    del tokens[victims]


# copied from 3.15 @ 0ac890bea7
_cookie_re = re.compile(r'^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)', re.ASCII)


def _fix_tokens(contents_text: str) -> str:
    try:
        tokens = src_to_tokens(contents_text)
    except tokenize.TokenError:
        return contents_text
    for i, token in reversed_enumerate(tokens):
        if token.name == 'STRING':
            tokens[i] = _fix_escape_sequences(_remove_u_prefix(tokens[i]))
        elif token.matches(name='OP', src='('):
            _fix_extraneous_parens(tokens, i)
        elif token.src == 'format' and i > 0 and tokens[i - 1].src == '.':
            _fix_format_literal(tokens, i - 2)
        elif token.src == 'encode' and i > 0 and tokens[i - 1].src == '.':
            _fix_encode_to_binary(tokens, i)
        elif (
                token.utf8_byte_offset == 0 and
                token.line < 3 and
                token.name == 'COMMENT' and
                _cookie_re.match(token.src)
        ):
            del tokens[i]
            assert tokens[i].name == 'NL', tokens[i].name
            del tokens[i]
    return tokens_to_src(tokens).lstrip()


def _fix_file(filename: str, args: argparse.Namespace) -> int:
    if filename == '-':
        contents_bytes = sys.stdin.buffer.read()
    else:
        with open(filename, 'rb') as fb:
            contents_bytes = fb.read()

    try:
        contents_text_orig = contents_text = contents_bytes.decode()
    except UnicodeDecodeError:
        print(f'{filename} is non-utf-8 (not supported)')
        return 1

    contents_text = _fix_plugins(
        contents_text,
        settings=Settings(
            min_version=args.min_version,
            keep_percent_format=args.keep_percent_format,
            keep_mock=args.keep_mock,
            keep_runtime_typing=args.keep_runtime_typing,
        ),
    )
    contents_text = _fix_tokens(contents_text)

    if filename == '-':
        print(contents_text, end='')
    elif contents_text != contents_text_orig:
        print(f'Rewriting {filename}', file=sys.stderr)
        with open(filename, 'w', encoding='UTF-8', newline='') as f:
            f.write(contents_text)

    if args.exit_zero_even_if_changed:
        return 0
    else:
        return contents_text != contents_text_orig


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--exit-zero-even-if-changed', action='store_true')
    parser.add_argument('--keep-percent-format', action='store_true')
    parser.add_argument('--keep-mock', action='store_true')
    parser.add_argument('--keep-runtime-typing', action='store_true')
    parser.add_argument(
        '--py3-plus', '--py3-only',
        action='store_const', dest='min_version', default=(3,), const=(3,),
    )
    parser.add_argument(
        '--py36-plus',
        action='store_const', dest='min_version', const=(3, 6),
    )
    parser.add_argument(
        '--py37-plus',
        action='store_const', dest='min_version', const=(3, 7),
    )
    parser.add_argument(
        '--py38-plus',
        action='store_const', dest='min_version', const=(3, 8),
    )
    parser.add_argument(
        '--py39-plus',
        action='store_const', dest='min_version', const=(3, 9),
    )
    parser.add_argument(
        '--py310-plus',
        action='store_const', dest='min_version', const=(3, 10),
    )
    parser.add_argument(
        '--py311-plus',
        action='store_const', dest='min_version', const=(3, 11),
    )
    parser.add_argument(
        '--py312-plus',
        action='store_const', dest='min_version', const=(3, 12),
    )
    parser.add_argument(
        '--py313-plus',
        action='store_const', dest='min_version', const=(3, 13),
    )
    parser.add_argument(
        '--py314-plus',
        action='store_const', dest='min_version', const=(3, 14),
    )
    args = parser.parse_args(argv)

    ret = 0
    for filename in args.filenames:
        ret |= _fix_file(filename, args)
    return ret


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pyupgrade/_string_helpers.py`
```python
from __future__ import annotations

import codecs
import string
from typing import Optional

from tokenize_rt import curly_escape
from tokenize_rt import NAMED_UNICODE_RE

DotFormatPart = tuple[str, Optional[str], Optional[str], Optional[str]]

_stdlib_parse_format = string.Formatter().parse


def parse_format(s: str) -> list[DotFormatPart]:
    """handle named escape sequences"""
    ret: list[DotFormatPart] = []

    for part in NAMED_UNICODE_RE.split(s):
        if NAMED_UNICODE_RE.fullmatch(part):
            if not ret or ret[-1][1:] != (None, None, None):
                ret.append((part, None, None, None))
            else:
                ret[-1] = (ret[-1][0] + part, None, None, None)
        else:
            first = True
            for tup in _stdlib_parse_format(part):
                if not first or not ret:
                    ret.append(tup)
                else:
                    ret[-1] = (ret[-1][0] + tup[0], *tup[1:])
                first = False

    if not ret:
        ret.append((s, None, None, None))

    return ret


def unparse_parsed_string(parsed: list[DotFormatPart]) -> str:
    def _convert_tup(tup: DotFormatPart) -> str:
        ret, field_name, format_spec, conversion = tup
        ret = curly_escape(ret)
        if field_name is not None:
            ret += '{' + field_name
            if conversion:
                ret += '!' + conversion
            if format_spec:
                ret += ':' + format_spec
            ret += '}'
        return ret

    return ''.join(_convert_tup(tup) for tup in parsed)


def is_codec(encoding: str, name: str) -> bool:
    try:
        return codecs.lookup(encoding).name == name
    except LookupError:
        return False
```

## File: `pyupgrade/_token_helpers.py`
```python
from __future__ import annotations

import ast
import keyword
from collections.abc import Sequence
from typing import NamedTuple

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import Token
from tokenize_rt import tokens_to_src
from tokenize_rt import UNIMPORTANT_WS

_OPENING = frozenset('([{')
_CLOSING = frozenset(')]}')
KEYWORDS = frozenset(keyword.kwlist)


def immediately_paren(func: str, tokens: list[Token], i: int) -> bool:
    return tokens[i].src == func and tokens[i + 1].src == '('


class Victims(NamedTuple):
    starts: list[int]
    ends: list[int]
    first_comma_index: int | None
    arg_index: int


def is_open(token: Token) -> bool:
    return token.name == 'OP' and token.src in _OPENING


def is_close(token: Token) -> bool:
    return token.name == 'OP' and token.src in _CLOSING


def _find_token(tokens: list[Token], i: int, name: str, src: str) -> int:
    while not tokens[i].matches(name=name, src=src):
        i += 1
    return i


def find_name(tokens: list[Token], i: int, src: str) -> int:
    return _find_token(tokens, i, 'NAME', src)


def find_op(tokens: list[Token], i: int, src: str) -> int:
    return _find_token(tokens, i, 'OP', src)


def find_call(tokens: list[Token], i: int) -> int:
    depth = 0
    while depth or not tokens[i].matches(name='OP', src='('):
        if is_open(tokens[i]):  # pragma: >3.12 cover
            depth += 1
        elif is_close(tokens[i]):
            # why max(...)? --
            # ("something").method(...)
            #  ^--start   target--^
            depth = max(depth - 1, 0)
        i += 1
    return i


def find_end(tokens: list[Token], i: int) -> int:
    while tokens[i].name != 'NEWLINE':
        i += 1

    return i + 1


def _arg_token_index(tokens: list[Token], i: int, arg: ast.expr) -> int:
    offset = (arg.lineno, arg.col_offset)
    while tokens[i].offset != offset:
        i += 1
    i += 1
    while tokens[i].name in NON_CODING_TOKENS:
        i += 1
    return i


def victims(
        tokens: list[Token],
        start: int,
        arg: ast.expr,
        gen: bool,
) -> Victims:
    starts = [start]
    start_depths = [1]
    ends: list[int] = []
    first_comma_index = None
    arg_depth = None
    arg_index = _arg_token_index(tokens, start, arg)
    depth = 1
    i = start + 1

    while depth:
        is_start_brace = is_open(tokens[i])
        is_end_brace = is_close(tokens[i])

        if i == arg_index:
            arg_depth = depth

        if is_start_brace:
            depth += 1

        # Remove all braces before the first element of the inner
        # comprehension's target.
        if is_start_brace and arg_depth is None:
            start_depths.append(depth)
            starts.append(i)

        if (
                tokens[i].matches(name='OP', src=',') and
                depth == arg_depth and
                first_comma_index is None
        ):
            first_comma_index = i

        if is_end_brace and depth in start_depths:
            if tokens[i - 2].src == ',' and tokens[i - 1].src == ' ':
                ends.extend((i - 2, i - 1, i))
            elif tokens[i - 1].src == ',':
                ends.extend((i - 1, i))
            else:
                ends.append(i)
            if depth > 1 and tokens[i + 1].src == ',':
                ends.append(i + 1)

        if is_end_brace:
            depth -= 1

        i += 1
    # May need to remove a trailing comma for a comprehension
    if gen:
        i -= 2
        while tokens[i].name in NON_CODING_TOKENS:
            i -= 1
        if tokens[i].src == ',':
            ends.append(i)

    return Victims(starts, sorted(set(ends)), first_comma_index, arg_index)


def find_closing_bracket(tokens: list[Token], i: int) -> int:
    assert tokens[i].src in _OPENING
    depth = 1
    i += 1
    while depth:
        if is_open(tokens[i]):
            depth += 1
        elif is_close(tokens[i]):
            depth -= 1
        i += 1
    return i - 1


def find_block_start(tokens: list[Token], i: int) -> int:
    depth = 0
    while depth or not tokens[i].matches(name='OP', src=':'):
        if is_open(tokens[i]):
            depth += 1
        elif is_close(tokens[i]):
            depth -= 1
        i += 1
    return i


class Block(NamedTuple):
    start: int
    colon: int
    block: int
    end: int
    line: bool

    def _initial_indent(self, tokens: list[Token]) -> int:
        if tokens[self.start].src.isspace():
            return len(tokens[self.start].src)
        else:
            return 0

    def _minimum_indent(self, tokens: list[Token]) -> int:
        block_indent = None
        for i in range(self.block, self.end):
            if (
                    tokens[i - 1].name in ('NL', 'NEWLINE') and
                    tokens[i].name in ('INDENT', UNIMPORTANT_WS) and
                    # comments can have arbitrary indentation so ignore them
                    tokens[i + 1].name != 'COMMENT'
            ):
                token_indent = len(tokens[i].src)
                if block_indent is None:
                    block_indent = token_indent
                else:
                    block_indent = min(block_indent, token_indent)

        assert block_indent is not None
        return block_indent

    def dedent(self, tokens: list[Token]) -> None:
        if self.line:
            return
        initial_indent = self._initial_indent(tokens)
        diff = self._minimum_indent(tokens) - initial_indent
        for i in range(self.block, self.end):
            if (
                    tokens[i - 1].name in ('DEDENT', 'NL', 'NEWLINE') and
                    tokens[i].name in ('INDENT', UNIMPORTANT_WS)
            ):
                # make sure we preserve *at least* the initial indent
                s = tokens[i].src
                s = s[:initial_indent] + s[initial_indent + diff:]
                tokens[i] = tokens[i]._replace(src=s)

    def replace_condition(self, tokens: list[Token], new: list[Token]) -> None:
        start = self.start
        while tokens[start].name == 'UNIMPORTANT_WS':
            start += 1
        tokens[start:self.colon] = new

    def _trim_end(self, tokens: list[Token]) -> Block:
        """the tokenizer reports the end of the block at the beginning of
        the next block
        """
        i = last_token = self.end - 1
        while tokens[i].name in NON_CODING_TOKENS | {'DEDENT', 'NEWLINE'}:
            # if we find an indented comment inside our block, keep it
            if (
                    tokens[i].name in {'NL', 'NEWLINE'} and
                    tokens[i + 1].name == UNIMPORTANT_WS and
                    len(tokens[i + 1].src) > self._initial_indent(tokens)
            ):
                break
            # otherwise we've found another line to remove
            elif tokens[i].name in {'NL', 'NEWLINE'}:
                last_token = i
            i -= 1
        return self._replace(end=last_token + 1)

    @classmethod
    def find(
            cls,
            tokens: list[Token],
            i: int,
            trim_end: bool = False,
    ) -> Block:
        if i > 0 and tokens[i - 1].name in {'INDENT', UNIMPORTANT_WS}:
            i -= 1
        start = i
        colon = find_block_start(tokens, i)

        j = colon + 1
        while (
                tokens[j].name != 'NEWLINE' and
                tokens[j].name in NON_CODING_TOKENS
        ):
            j += 1

        if tokens[j].name == 'NEWLINE':  # multi line block
            block = j + 1
            while tokens[j].name != 'INDENT':
                j += 1
            level = 1
            j += 1
            while level:
                level += {'INDENT': 1, 'DEDENT': -1}.get(tokens[j].name, 0)
                j += 1
            ret = cls(start, colon, block, j, line=False)
            if trim_end:
                return ret._trim_end(tokens)
            else:
                return ret
        else:  # single line block
            block = j
            j = find_end(tokens, j)
            return cls(start, colon, block, j, line=True)


def _is_on_a_line_by_self(tokens: list[Token], i: int) -> bool:
    return (
        tokens[i - 2].name == 'NL' and
        tokens[i - 1].name == UNIMPORTANT_WS and
        tokens[i + 1].name == 'NL'
    )


def remove_brace(tokens: list[Token], i: int) -> None:
    if _is_on_a_line_by_self(tokens, i):
        del tokens[i - 1:i + 2]
    else:
        del tokens[i]


def remove_base_class(i: int, tokens: list[Token]) -> None:
    # look forward and backward to find commas / parens
    brace_stack = []
    j = i
    while tokens[j].src not in {',', ':'}:
        if tokens[j].src == ')':
            brace_stack.append(j)
        j += 1
    right = j

    if tokens[right].src == ':':
        brace_stack.pop()
    else:
        # if there's a close-paren after a trailing comma
        j = right + 1
        while tokens[j].name in NON_CODING_TOKENS:
            j += 1
        if tokens[j].src == ')':
            while tokens[j].src != ':':
                j += 1
            right = j

    if brace_stack:
        last_part = brace_stack[-1]
    else:
        last_part = i

    j = i
    while brace_stack:
        if tokens[j].src == '(':
            brace_stack.pop()
        j -= 1

    while tokens[j].src not in {',', '('}:
        j -= 1
    left = j

    # single base, remove the entire bases
    if tokens[left].src == '(' and tokens[right].src == ':':
        del tokens[left:right]
    # multiple bases, base is first
    elif tokens[left].src == '(' and tokens[right].src != ':':
        # if there's space / comment afterwards remove that too
        while tokens[right + 1].name in {UNIMPORTANT_WS, 'COMMENT'}:
            right += 1
        del tokens[left + 1:right + 1]
    # multiple bases, base is not first
    else:
        del tokens[left:last_part + 1]


def remove_decorator(i: int, tokens: list[Token]) -> None:
    while tokens[i - 1].src != '@':
        i -= 1
    if i > 1 and tokens[i - 2].name not in {'NEWLINE', 'NL'}:
        i -= 1
    end = i + 1
    while tokens[end].name != 'NEWLINE':
        end += 1
    del tokens[i - 1:end + 1]


def parse_call_args(
        tokens: list[Token],
        i: int,
) -> tuple[list[tuple[int, int]], int]:
    args = []
    depth = 1
    i += 1
    arg_start = i

    while depth:
        if depth == 1 and tokens[i].src == ',':
            args.append((arg_start, i))
            arg_start = i + 1
        elif is_open(tokens[i]):
            depth += 1
        elif is_close(tokens[i]):
            depth -= 1
            # if we're at the end, append that argument
            if not depth and tokens_to_src(tokens[arg_start:i]).strip():
                args.append((arg_start, i))

        i += 1

    return args, i


def arg_str(tokens: list[Token], start: int, end: int) -> str:
    return tokens_to_src(tokens[start:end]).strip()


def _arg_str_no_comment(tokens: list[Token], start: int, end: int) -> str:
    arg_tokens = [
        token for token in tokens[start:end]
        if token.name != 'COMMENT'
    ]
    return tokens_to_src(arg_tokens).strip()


def _arg_contains_newline(tokens: list[Token], start: int, end: int) -> bool:
    while tokens[start].name in {'NL', 'NEWLINE', UNIMPORTANT_WS}:
        start += 1
    for i in range(start, end):
        if tokens[i].name in {'NL', 'NEWLINE'}:
            return True
    else:
        return False


def replace_call(
        tokens: list[Token],
        start: int,
        end: int,
        args: list[tuple[int, int]],
        tmpl: str,
        *,
        parens: Sequence[int] = (),
) -> None:
    arg_strs = [arg_str(tokens, *arg) for arg in args]
    for paren in parens:
        arg_strs[paren] = f'({arg_strs[paren]})'

    # there are a few edge cases which cause syntax errors when the first
    # argument contains newlines (especially when moved outside of a natural
    # continuation context)
    if _arg_contains_newline(tokens, *args[0]) and 0 not in parens:
        # this attempts to preserve more of the whitespace by using the
        # original non-stripped argument string
        arg_strs[0] = f'({tokens_to_src(tokens[slice(*args[0])])})'

    start_rest = args[0][1] + 1
    while (
            start_rest < end and
            tokens[start_rest].name in {'COMMENT', UNIMPORTANT_WS}
    ):
        start_rest += 1

    # Remove trailing comma
    end_rest = end - 1
    if tokens[end_rest - 1].matches(name='OP', src=','):
        end_rest -= 1

    rest = tokens_to_src(tokens[start_rest:end_rest])
    src = tmpl.format(args=arg_strs, rest=rest)
    tokens[start:end] = [Token('CODE', src)]


def find_and_replace_call(
        i: int,
        tokens: list[Token],
        *,
        template: str,
        parens: tuple[int, ...] = (),
) -> None:
    j = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, j)
    replace_call(tokens, i, end, func_args, template, parens=parens)


def replace_name(i: int, tokens: list[Token], *, name: str, new: str) -> None:
    # preserve token offset in case we need to match it later
    new_token = tokens[i]._replace(name='CODE', src=new)
    j = i
    while not tokens[j].matches(name='NAME', src=name):
        # timid: if we see a parenthesis here, skip it
        if tokens[j].src == ')':
            return
        j += 1
    tokens[i:j + 1] = [new_token]


def delete_argument(
        i: int, tokens: list[Token],
        func_args: Sequence[tuple[int, int]],
) -> None:
    if i == 0:
        # delete leading whitespace before next token
        end_idx, _ = func_args[i + 1]
        while tokens[end_idx].name == 'UNIMPORTANT_WS':
            end_idx += 1

        del tokens[func_args[i][0]:end_idx]
    else:
        del tokens[func_args[i - 1][1]:func_args[i][1]]


def replace_argument(
        i: int,
        tokens: list[Token],
        func_args: Sequence[tuple[int, int]],
        *,
        new: str,
) -> None:
    start_idx, end_idx = func_args[i]
    # don't replace leading whitespace / newlines
    while tokens[start_idx].name in {'UNIMPORTANT_WS', 'NL'}:
        start_idx += 1
    tokens[start_idx:end_idx] = [Token('SRC', new)]


def constant_fold_tuple(i: int, tokens: list[Token]) -> None:
    start = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, start)
    arg_strs = [_arg_str_no_comment(tokens, *arg) for arg in func_args]

    unique_args = tuple(dict.fromkeys(arg_strs))

    if len(unique_args) > 1:
        joined = '({})'.format(', '.join(unique_args))
    elif tokens[start - 1].name != 'UNIMPORTANT_WS':
        joined = f' {unique_args[0]}'
    else:
        joined = unique_args[0]

    tokens[start:end] = [Token('CODE', joined)]


def has_space_before(i: int, tokens: list[Token]) -> bool:
    return i >= 1 and tokens[i - 1].name in {UNIMPORTANT_WS, 'INDENT'}


def indented_amount(i: int, tokens: list[Token]) -> str:
    if i == 0:
        return ''
    elif has_space_before(i, tokens):
        if i >= 2 and tokens[i - 2].name in {'NL', 'NEWLINE', 'DEDENT'}:
            return tokens[i - 1].src
        else:  # inline import
            raise ValueError('not at beginning of line')
    elif tokens[i - 1].name not in {'NL', 'NEWLINE', 'DEDENT'}:
        raise ValueError('not at beginning of line')
    else:
        return ''
```

## File: `pyupgrade/_plugins/collections_abc.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._plugins.imports import REPLACE_EXACT
from pyupgrade._token_helpers import replace_name

COLLECTIONS_ABC_ATTRS = frozenset(
    attr for mod, attr in REPLACE_EXACT[(3,)] if mod == 'collections'
)


@register(ast.Attribute)
def visit_Attribute(
        state: State,
        node: ast.Attribute,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.value, ast.Name) and
            node.value.id == 'collections' and
            node.attr in COLLECTIONS_ABC_ATTRS
    ):
        new_attr = f'collections.abc.{node.attr}'
        func = functools.partial(replace_name, name=node.attr, new=new_attr)
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/constant_fold.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_type_check
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import constant_fold_tuple


def _to_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        base = _to_name(node.value)
        if base is None:
            return None
        else:
            return f'{base}.{node.attr}'
    else:
        return None


def _can_constant_fold(node: ast.Tuple) -> bool:
    seen = set()
    for el in node.elts:
        name = _to_name(el)
        if name is not None:
            if name in seen:
                return True
            else:
                seen.add(name)
    else:
        return False


def _cbs(node: ast.AST | None) -> Iterable[tuple[Offset, TokenFunc]]:
    if isinstance(node, ast.Tuple) and _can_constant_fold(node):
        yield ast_to_offset(node), constant_fold_tuple


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if is_type_check(node):
        yield from _cbs(node.args[1])


@register(ast.Try)
def visit_Try(
        state: State,
        node: ast.Try,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    for handler in node.handlers:
        yield from _cbs(handler.type)
```

## File: `pyupgrade/_plugins/datetime_utc_alias.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import replace_name


@register(ast.Attribute)
def visit_Attribute(
        state: State,
        node: ast.Attribute,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            state.settings.min_version >= (3, 11) and
            node.attr == 'utc' and
            isinstance(node.value, ast.Attribute) and
            node.value.attr == 'timezone' and
            isinstance(node.value.value, ast.Name) and
            node.value.value.id == 'datetime'
    ):
        func = functools.partial(
            replace_name,
            name='utc',
            new='datetime.UTC',
        )
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/default_encoding.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._string_helpers import is_codec
from pyupgrade._token_helpers import find_call
from pyupgrade._token_helpers import find_closing_bracket


def _fix_default_encoding(i: int, tokens: list[Token]) -> None:
    i = find_call(tokens, i + 1)
    j = find_closing_bracket(tokens, i)
    del tokens[i + 1:j]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.func, ast.Attribute) and (
                (
                    isinstance(node.func.value, ast.Constant) and
                    isinstance(node.func.value.value, str)
                ) or
                isinstance(node.func.value, ast.JoinedStr)
            ) and
            node.func.attr == 'encode' and
            not has_starargs(node) and
            len(node.args) == 1 and
            isinstance(node.args[0], ast.Constant) and
            isinstance(node.args[0].value, str) and
            is_codec(node.args[0].value, 'utf-8')
    ):
        yield ast_to_offset(node), _fix_default_encoding
```

## File: `pyupgrade/_plugins/defaultdict_lambda.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args


def _eligible_lambda_replacement(lambda_expr: ast.Lambda) -> str | None:
    if isinstance(lambda_expr.body, ast.Constant):
        if lambda_expr.body.value == 0:
            return type(lambda_expr.body.value).__name__
        elif lambda_expr.body.value == '':
            return 'str'
        else:
            return None
    elif isinstance(lambda_expr.body, ast.List) and not lambda_expr.body.elts:
        return 'list'
    elif isinstance(lambda_expr.body, ast.Tuple) and not lambda_expr.body.elts:
        return 'tuple'
    elif isinstance(lambda_expr.body, ast.Dict) and not lambda_expr.body.keys:
        return 'dict'
    elif (
            isinstance(lambda_expr.body, ast.Call) and
            isinstance(lambda_expr.body.func, ast.Name) and
            not lambda_expr.body.args and
            not lambda_expr.body.keywords and
            lambda_expr.body.func.id in {'dict', 'list', 'set', 'tuple'}
    ):
        return lambda_expr.body.func.id
    else:
        return None


def _fix_defaultdict_first_arg(
        i: int,
        tokens: list[Token],
        *,
        replacement: str,
) -> None:
    start = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, start)

    tokens[slice(*func_args[0])] = [Token('CODE', replacement)]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            is_name_attr(
                node.func,
                state.from_imports,
                ('collections',),
                ('defaultdict',),
            ) and
            node.args and
            isinstance(node.args[0], ast.Lambda)
    ):
        replacement = _eligible_lambda_replacement(node.args[0])
        if replacement is None:
            return

        func = functools.partial(
            _fix_defaultdict_first_arg,
            replacement=replacement,
        )
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/dict_literals.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token
from tokenize_rt import UNIMPORTANT_WS

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import immediately_paren
from pyupgrade._token_helpers import remove_brace
from pyupgrade._token_helpers import victims


def _fix_dict_comp(
        i: int,
        tokens: list[Token],
        arg: ast.ListComp | ast.GeneratorExp,
) -> None:
    if not immediately_paren('dict', tokens, i):
        return

    dict_victims = victims(tokens, i + 1, arg, gen=True)
    elt_victims = victims(tokens, dict_victims.arg_index, arg.elt, gen=True)

    del dict_victims.starts[0]
    end_index = dict_victims.ends.pop()

    tokens[end_index] = Token('OP', '}')
    for index in reversed(dict_victims.ends):
        remove_brace(tokens, index)
    # See #6, Fix SyntaxError from rewriting dict((a, b)for a, b in y)
    if tokens[elt_victims.ends[-1] + 1].src == 'for':
        tokens.insert(elt_victims.ends[-1] + 1, Token(UNIMPORTANT_WS, ' '))
    for index in reversed(elt_victims.ends):
        remove_brace(tokens, index)
    assert elt_victims.first_comma_index is not None
    tokens[elt_victims.first_comma_index] = Token('OP', ':')
    for index in reversed(dict_victims.starts + elt_victims.starts):
        remove_brace(tokens, index)
    tokens[i:i + 2] = [Token('OP', '{')]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            not isinstance(parent, ast.FormattedValue) and
            isinstance(node.func, ast.Name) and
            node.func.id == 'dict' and
            len(node.args) == 1 and
            not node.keywords and
            isinstance(node.args[0], (ast.ListComp, ast.GeneratorExp)) and
            isinstance(node.args[0].elt, (ast.Tuple, ast.List)) and
            len(node.args[0].elt.elts) == 2
    ):
        func = functools.partial(_fix_dict_comp, arg=node.args[0])
        yield ast_to_offset(node.func), func
```

## File: `pyupgrade/_plugins/exceptions.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable
from typing import NamedTuple

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._data import Version
from pyupgrade._token_helpers import constant_fold_tuple
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args
from pyupgrade._token_helpers import replace_name


class _Target(NamedTuple):
    target: str
    module: str | None
    name: str
    min_version: Version


_TARGETS = (
    _Target('OSError', 'mmap', 'error', (3,)),
    _Target('OSError', 'os', 'error', (3,)),
    _Target('OSError', 'select', 'error', (3,)),
    _Target('OSError', 'socket', 'error', (3,)),
    _Target('OSError', None, 'IOError', (3,)),
    _Target('OSError', None, 'EnvironmentError', (3,)),
    _Target('OSError', None, 'WindowsError', (3,)),
    _Target('TimeoutError', 'socket', 'timeout', (3, 10)),
    _Target('TimeoutError', 'asyncio', 'TimeoutError', (3, 11)),
)


def _fix_except(
        i: int,
        tokens: list[Token],
        *,
        at_idx: dict[int, _Target],
) -> None:
    start = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, start)

    for i, target in reversed(at_idx.items()):
        tokens[slice(*func_args[i])] = [Token('NAME', target.target)]

    constant_fold_tuple(start, tokens)


def _get_rewrite(
        node: ast.AST,
        state: State,
        targets: list[_Target],
) -> _Target | None:
    for target in targets:
        if (
                target.module is None and
                isinstance(node, ast.Name) and
                node.id == target.name
        ):
            return target
        elif (
                target.module is not None and
                isinstance(node, ast.Name) and
                node.id == target.name and
                node.id in state.from_imports[target.module]
        ):
            return target
        elif (
                target.module is not None and
                isinstance(node, ast.Attribute) and
                isinstance(node.value, ast.Name) and
                node.attr == target.name and
                node.value.id == target.module
        ):
            return target
    else:
        return None


def _alias_cbs(
        node: ast.expr,
        state: State,
        targets: list[_Target],
) -> Iterable[tuple[Offset, TokenFunc]]:
    target = _get_rewrite(node, state, targets)
    if target is not None:
        func = functools.partial(
            replace_name,
            name=target.name,
            new=target.target,
        )
        yield ast_to_offset(node), func


@register(ast.Raise)
def visit_Raise(
        state: State,
        node: ast.Raise,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    targets = [
        target for target in _TARGETS
        if state.settings.min_version >= target.min_version
    ]
    if node.exc is not None:
        yield from _alias_cbs(node.exc, state, targets)
        if isinstance(node.exc, ast.Call):
            yield from _alias_cbs(node.exc.func, state, targets)


@register(ast.Try)
def visit_Try(
        state: State,
        node: ast.Try,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    targets = [
        target for target in _TARGETS
        if state.settings.min_version >= target.min_version
    ]
    for handler in node.handlers:
        if isinstance(handler.type, ast.Tuple):
            at_idx = {}
            for i, elt in enumerate(handler.type.elts):
                target = _get_rewrite(elt, state, targets)
                if target is not None:
                    at_idx[i] = target

            if at_idx:
                func = functools.partial(_fix_except, at_idx=at_idx)
                yield ast_to_offset(handler.type), func
        elif handler.type is not None:
            yield from _alias_cbs(handler.type, state, targets)
```

## File: `pyupgrade/_plugins/format_locals.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import rfind_string_parts
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_closing_bracket
from pyupgrade._token_helpers import find_op


def _fix(i: int, tokens: list[Token]) -> None:
    dot_pos = find_op(tokens, i, '.')
    open_pos = find_op(tokens, dot_pos, '(')
    close_pos = find_closing_bracket(tokens, open_pos)
    for string_idx in rfind_string_parts(tokens, dot_pos - 1):
        tok = tokens[string_idx]
        tokens[string_idx] = tok._replace(src=f'f{tok.src}')
    del tokens[dot_pos:close_pos + 1]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            state.settings.min_version >= (3, 6) and
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Constant) and
            isinstance(node.func.value.value, str) and
            node.func.attr == 'format' and
            len(node.args) == 0 and
            len(node.keywords) == 1 and
            node.keywords[0].arg is None and
            isinstance(node.keywords[0].value, ast.Call) and
            isinstance(node.keywords[0].value.func, ast.Name) and
            node.keywords[0].value.func.id == 'locals' and
            len(node.keywords[0].value.args) == 0 and
            len(node.keywords[0].value.keywords) == 0
    ):
        yield ast_to_offset(node), _fix
```

## File: `pyupgrade/_plugins/fstrings.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import parse_string_literal
from tokenize_rt import Token
from tokenize_rt import tokens_to_src

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import contains_await
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._string_helpers import parse_format
from pyupgrade._string_helpers import unparse_parsed_string
from pyupgrade._token_helpers import parse_call_args


def _skip_unimportant_ws(tokens: list[Token], i: int) -> int:
    while tokens[i].name == 'UNIMPORTANT_WS':
        i += 1
    return i


def _to_fstring(
    src: str, tokens: list[Token], args: list[tuple[int, int]],
) -> str:
    params = {}
    i = 0
    for start, end in args:
        start = _skip_unimportant_ws(tokens, start)
        if tokens[start].name == 'NAME':
            after = _skip_unimportant_ws(tokens, start + 1)
            if tokens[after].src == '=':  # keyword argument
                params[tokens[start].src] = tokens_to_src(
                    tokens[after + 1:end],
                ).strip()
                continue
        params[str(i)] = tokens_to_src(tokens[start:end]).strip()
        i += 1

    parts = []
    i = 0

    # need to remove `u` prefix so it isn't invalid syntax
    prefix, rest = parse_string_literal(src)
    new_src = 'f' + prefix.translate({ord('u'): None, ord('U'): None}) + rest

    for s, name, spec, conv in parse_format(new_src):
        if name is not None:
            k, dot, rest = name.partition('.')
            name = ''.join((params[k or str(i)], dot, rest))
            if not k:  # named and auto params can be in different orders
                i += 1
        parts.append((s, name, spec, conv))
    return unparse_parsed_string(parts)


def _fix_fstring(i: int, tokens: list[Token]) -> None:
    token = tokens[i]

    paren = i + 3
    if tokens_to_src(tokens[i + 1:paren + 1]) != '.format(':
        return

    args, end = parse_call_args(tokens, paren)
    # if it spans more than one line, bail
    if tokens[end - 1].line != token.line:
        return

    args_src = tokens_to_src(tokens[paren:end])
    if '\\' in args_src or '"' in args_src or "'" in args_src:
        return

    tokens[i] = token._replace(src=_to_fstring(token.src, tokens, args))
    del tokens[i + 1:end]


def _format_params(call: ast.Call) -> set[str]:
    params = {str(i) for i, arg in enumerate(call.args)}
    for kwd in call.keywords:
        # kwd.arg can't be None here because we exclude starargs
        assert kwd.arg is not None
        params.add(kwd.arg)
    return params


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if state.settings.min_version < (3, 6):
        return

    if (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Constant) and
            isinstance(node.func.value.value, str) and
            node.func.attr == 'format' and
            not has_starargs(node)
    ):
        try:
            parsed = parse_format(node.func.value.value)
        except ValueError:
            return

        params = _format_params(node)
        seen = set()
        i = 0
        for _, name, spec, _ in parsed:
            # timid: difficult to rewrite correctly
            if spec is not None and '{' in spec:
                break
            if name is not None:
                candidate, _, _ = name.partition('.')
                # timid: could make the f-string longer
                if candidate and candidate in seen:
                    break
                # timid: bracketed
                elif '[' in name:
                    break
                seen.add(candidate)

                key = candidate or str(i)
                # their .format() call is broken currently
                if key not in params:
                    break
                if not candidate:
                    i += 1
        else:
            if (
                    state.settings.min_version >= (3, 7) or
                    not contains_await(node)
            ):
                yield ast_to_offset(node), _fix_fstring
```

## File: `pyupgrade/_plugins/identity_equality.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc


def _fix_is_literal(
        i: int,
        tokens: list[Token],
        *,
        op: ast.Is | ast.IsNot,
) -> None:
    while tokens[i].src != 'is':
        i -= 1
    if isinstance(op, ast.Is):
        tokens[i] = tokens[i]._replace(src='==')
    else:
        tokens[i] = tokens[i]._replace(src='!=')
        # since we iterate backward, the empty tokens keep the same length
        i += 1
        while tokens[i].src != 'not':
            tokens[i] = Token('EMPTY', '')
            i += 1
        tokens[i] = Token('EMPTY', '')


def _is_literal(n: ast.AST) -> bool:
    return (
        isinstance(n, ast.Constant) and
        n.value not in {True, False} and
        isinstance(n.value, (str, bytes, int, float))
    )


@register(ast.Compare)
def visit_Compare(
        state: State,
        node: ast.Compare,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    left = node.left
    for op, right in zip(node.ops, node.comparators):
        if (
                isinstance(op, (ast.Is, ast.IsNot)) and
                (_is_literal(left) or _is_literal(right))
        ):
            func = functools.partial(_fix_is_literal, op=op)
            yield ast_to_offset(right), func
        left = right
```

## File: `pyupgrade/_plugins/imports.py`
```python
from __future__ import annotations

import ast
import bisect
import collections
import functools
from collections.abc import Iterable
from collections.abc import Mapping
from typing import NamedTuple

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_end
from pyupgrade._token_helpers import find_name
from pyupgrade._token_helpers import has_space_before
from pyupgrade._token_helpers import indented_amount

# GENERATED VIA generate-imports
# Using reorder-python-imports==3.16.0
REMOVALS = {
    (3,): {
        '__future__': {
            'absolute_import', 'division', 'generators', 'nested_scopes',
            'print_function', 'unicode_literals', 'with_statement',
        },
        'builtins': {
            '*', 'ascii', 'bytes', 'chr', 'dict', 'filter', 'hex', 'input',
            'int', 'isinstance', 'list', 'map', 'max', 'min', 'next', 'object',
            'oct', 'open', 'pow', 'range', 'round', 'str', 'super', 'zip',
        },
        'io': {'open'},
        'six': {'callable', 'next'},
        'six.moves': {'filter', 'input', 'map', 'range', 'zip'},
    },
    (3, 7): {'__future__': {'generator_stop'}},
    (3, 14): {'__future__': {'annotations'}},
}
REMOVALS[(3,)]['six.moves.builtins'] = REMOVALS[(3,)]['builtins']
REPLACE_EXACT = {
    (3,): {
        ('collections', 'AsyncGenerator'): 'collections.abc',
        ('collections', 'AsyncIterable'): 'collections.abc',
        ('collections', 'AsyncIterator'): 'collections.abc',
        ('collections', 'Awaitable'): 'collections.abc',
        ('collections', 'ByteString'): 'collections.abc',
        ('collections', 'Callable'): 'collections.abc',
        ('collections', 'Collection'): 'collections.abc',
        ('collections', 'Container'): 'collections.abc',
        ('collections', 'Coroutine'): 'collections.abc',
        ('collections', 'Generator'): 'collections.abc',
        ('collections', 'Hashable'): 'collections.abc',
        ('collections', 'ItemsView'): 'collections.abc',
        ('collections', 'Iterable'): 'collections.abc',
        ('collections', 'Iterator'): 'collections.abc',
        ('collections', 'KeysView'): 'collections.abc',
        ('collections', 'Mapping'): 'collections.abc',
        ('collections', 'MappingView'): 'collections.abc',
        ('collections', 'MutableMapping'): 'collections.abc',
        ('collections', 'MutableSequence'): 'collections.abc',
        ('collections', 'MutableSet'): 'collections.abc',
        ('collections', 'Reversible'): 'collections.abc',
        ('collections', 'Sequence'): 'collections.abc',
        ('collections', 'Set'): 'collections.abc',
        ('collections', 'Sized'): 'collections.abc',
        ('collections', 'ValuesView'): 'collections.abc',
        ('pipes', 'quote'): 'shlex',
        ('six', 'BytesIO'): 'io',
        ('six', 'StringIO'): 'io',
        ('six', 'wraps'): 'functools',
        ('six.moves', 'StringIO'): 'io',
        ('six.moves', 'UserDict'): 'collections',
        ('six.moves', 'UserList'): 'collections',
        ('six.moves', 'UserString'): 'collections',
        ('six.moves', 'filterfalse'): 'itertools',
        ('six.moves', 'getcwd'): 'os',
        ('six.moves', 'getcwdb'): 'os',
        ('six.moves', 'getoutput'): 'subprocess',
        ('six.moves', 'intern'): 'sys',
        ('six.moves', 'reduce'): 'functools',
        ('six.moves', 'zip_longest'): 'itertools',
        ('six.moves.urllib', 'error'): 'urllib',
        ('six.moves.urllib', 'parse'): 'urllib',
        ('six.moves.urllib', 'request'): 'urllib',
        ('six.moves.urllib', 'response'): 'urllib',
        ('six.moves.urllib', 'robotparser'): 'urllib',
    },
    (3, 6): {
        ('typing_extensions', 'AbstractSet'): 'typing',
        ('typing_extensions', 'AnyStr'): 'typing',
        ('typing_extensions', 'AsyncIterable'): 'typing',
        ('typing_extensions', 'AsyncIterator'): 'typing',
        ('typing_extensions', 'Awaitable'): 'typing',
        ('typing_extensions', 'BinaryIO'): 'typing',
        ('typing_extensions', 'Callable'): 'typing',
        ('typing_extensions', 'ClassVar'): 'typing',
        ('typing_extensions', 'Collection'): 'typing',
        ('typing_extensions', 'Container'): 'typing',
        ('typing_extensions', 'Coroutine'): 'typing',
        ('typing_extensions', 'DefaultDict'): 'typing',
        ('typing_extensions', 'Dict'): 'typing',
        ('typing_extensions', 'FrozenSet'): 'typing',
        ('typing_extensions', 'Generic'): 'typing',
        ('typing_extensions', 'Hashable'): 'typing',
        ('typing_extensions', 'IO'): 'typing',
        ('typing_extensions', 'ItemsView'): 'typing',
        ('typing_extensions', 'Iterable'): 'typing',
        ('typing_extensions', 'Iterator'): 'typing',
        ('typing_extensions', 'KeysView'): 'typing',
        ('typing_extensions', 'List'): 'typing',
        ('typing_extensions', 'Mapping'): 'typing',
        ('typing_extensions', 'MappingView'): 'typing',
        ('typing_extensions', 'Match'): 'typing',
        ('typing_extensions', 'MutableMapping'): 'typing',
        ('typing_extensions', 'MutableSequence'): 'typing',
        ('typing_extensions', 'MutableSet'): 'typing',
        ('typing_extensions', 'Optional'): 'typing',
        ('typing_extensions', 'Pattern'): 'typing',
        ('typing_extensions', 'Reversible'): 'typing',
        ('typing_extensions', 'Sequence'): 'typing',
        ('typing_extensions', 'Set'): 'typing',
        ('typing_extensions', 'Sized'): 'typing',
        ('typing_extensions', 'TYPE_CHECKING'): 'typing',
        ('typing_extensions', 'Text'): 'typing',
        ('typing_extensions', 'TextIO'): 'typing',
        ('typing_extensions', 'Tuple'): 'typing',
        ('typing_extensions', 'Type'): 'typing',
        ('typing_extensions', 'Union'): 'typing',
        ('typing_extensions', 'ValuesView'): 'typing',
        ('typing_extensions', 'cast'): 'typing',
        ('typing_extensions', 'no_type_check'): 'typing',
        ('typing_extensions', 'no_type_check_decorator'): 'typing',
    },
    (3, 7): {
        ('mypy_extensions', 'NoReturn'): 'typing',
        ('typing_extensions', 'ChainMap'): 'typing',
        ('typing_extensions', 'Counter'): 'typing',
        ('typing_extensions', 'Deque'): 'typing',
        ('typing_extensions', 'ForwardRef'): 'typing',
        ('typing_extensions', 'NoReturn'): 'typing',
    },
    (3, 8): {
        ('mypy_extensions', 'TypedDict'): 'typing',
        ('typing_extensions', 'Final'): 'typing',
        ('typing_extensions', 'OrderedDict'): 'typing',
    },
    (3, 9): {
        ('typing', 'AsyncGenerator'): 'collections.abc',
        ('typing', 'AsyncIterable'): 'collections.abc',
        ('typing', 'AsyncIterator'): 'collections.abc',
        ('typing', 'Awaitable'): 'collections.abc',
        ('typing', 'ByteString'): 'collections.abc',
        ('typing', 'ChainMap'): 'collections',
        ('typing', 'Collection'): 'collections.abc',
        ('typing', 'Container'): 'collections.abc',
        ('typing', 'Coroutine'): 'collections.abc',
        ('typing', 'Counter'): 'collections',
        ('typing', 'Generator'): 'collections.abc',
        ('typing', 'Hashable'): 'collections.abc',
        ('typing', 'ItemsView'): 'collections.abc',
        ('typing', 'Iterable'): 'collections.abc',
        ('typing', 'Iterator'): 'collections.abc',
        ('typing', 'KeysView'): 'collections.abc',
        ('typing', 'Mapping'): 'collections.abc',
        ('typing', 'MappingView'): 'collections.abc',
        ('typing', 'Match'): 're',
        ('typing', 'MutableMapping'): 'collections.abc',
        ('typing', 'MutableSequence'): 'collections.abc',
        ('typing', 'MutableSet'): 'collections.abc',
        ('typing', 'OrderedDict'): 'collections',
        ('typing', 'Pattern'): 're',
        ('typing', 'Reversible'): 'collections.abc',
        ('typing', 'Sequence'): 'collections.abc',
        ('typing', 'Sized'): 'collections.abc',
        ('typing', 'ValuesView'): 'collections.abc',
        ('typing.re', 'Match'): 're',
        ('typing.re', 'Pattern'): 're',
        ('typing_extensions', 'Annotated'): 'typing',
        ('typing_extensions', 'get_type_hints'): 'typing',
    },
    (3, 10): {
        ('typing', 'Callable'): 'collections.abc',
        ('typing_extensions', 'Concatenate'): 'typing',
        ('typing_extensions', 'Literal'): 'typing',
        ('typing_extensions', 'NewType'): 'typing',
        ('typing_extensions', 'ParamSpecArgs'): 'typing',
        ('typing_extensions', 'ParamSpecKwargs'): 'typing',
        ('typing_extensions', 'TypeAlias'): 'typing',
        ('typing_extensions', 'TypeGuard'): 'typing',
        ('typing_extensions', 'get_args'): 'typing',
        ('typing_extensions', 'get_origin'): 'typing',
        ('typing_extensions', 'is_typeddict'): 'typing',
    },
    (3, 11): {
        ('typing_extensions', 'Any'): 'typing',
        ('typing_extensions', 'LiteralString'): 'typing',
        ('typing_extensions', 'Never'): 'typing',
        ('typing_extensions', 'NotRequired'): 'typing',
        ('typing_extensions', 'Required'): 'typing',
        ('typing_extensions', 'Self'): 'typing',
        ('typing_extensions', 'assert_never'): 'typing',
        ('typing_extensions', 'assert_type'): 'typing',
        ('typing_extensions', 'clear_overloads'): 'typing',
        ('typing_extensions', 'final'): 'typing',
        ('typing_extensions', 'get_overloads'): 'typing',
        ('typing_extensions', 'overload'): 'typing',
        ('typing_extensions', 'reveal_type'): 'typing',
    },
    (3, 12): {
        ('typing_extensions', 'NamedTuple'): 'typing',
        ('typing_extensions', 'SupportsAbs'): 'typing',
        ('typing_extensions', 'SupportsBytes'): 'typing',
        ('typing_extensions', 'SupportsComplex'): 'typing',
        ('typing_extensions', 'SupportsFloat'): 'typing',
        ('typing_extensions', 'SupportsIndex'): 'typing',
        ('typing_extensions', 'SupportsInt'): 'typing',
        ('typing_extensions', 'SupportsRound'): 'typing',
        ('typing_extensions', 'TypeAliasType'): 'typing',
        ('typing_extensions', 'Unpack'): 'typing',
        ('typing_extensions', 'dataclass_transform'): 'typing',
        ('typing_extensions', 'override'): 'typing',
    },
    (3, 13): {
        ('typing_extensions', 'AsyncContextManager'): 'typing',
        ('typing_extensions', 'AsyncGenerator'): 'typing',
        ('typing_extensions', 'ContextManager'): 'typing',
        ('typing_extensions', 'Generator'): 'typing',
        ('typing_extensions', 'NoDefault'): 'typing',
        ('typing_extensions', 'ParamSpec'): 'typing',
        ('typing_extensions', 'Protocol'): 'typing',
        ('typing_extensions', 'ReadOnly'): 'typing',
        ('typing_extensions', 'TypeIs'): 'typing',
        ('typing_extensions', 'TypeVar'): 'typing',
        ('typing_extensions', 'TypeVarTuple'): 'typing',
        ('typing_extensions', 'TypedDict'): 'typing',
        ('typing_extensions', 'deprecated'): 'warnings',
        ('typing_extensions', 'get_protocol_members'): 'typing',
        ('typing_extensions', 'is_protocol'): 'typing',
        ('typing_extensions', 'runtime_checkable'): 'typing',
    },
    (3, 14): {
        ('typing_extensions', 'evaluate_forward_ref'): 'typing',
    },
}
REPLACE_MODS = {
    'six.moves.BaseHTTPServer': 'http.server',
    'six.moves.CGIHTTPServer': 'http.server',
    'six.moves.SimpleHTTPServer': 'http.server',
    'six.moves._dummy_thread': '_thread',
    'six.moves._thread': '_thread',
    'six.moves.builtins': 'builtins',
    'six.moves.cPickle': 'pickle',
    'six.moves.collections_abc': 'collections.abc',
    'six.moves.configparser': 'configparser',
    'six.moves.copyreg': 'copyreg',
    'six.moves.dbm_gnu': 'dbm.gnu',
    'six.moves.dbm_ndbm': 'dbm.ndbm',
    'six.moves.email_mime_base': 'email.mime.base',
    'six.moves.email_mime_image': 'email.mime.image',
    'six.moves.email_mime_multipart': 'email.mime.multipart',
    'six.moves.email_mime_nonmultipart': 'email.mime.nonmultipart',
    'six.moves.email_mime_text': 'email.mime.text',
    'six.moves.html_entities': 'html.entities',
    'six.moves.html_parser': 'html.parser',
    'six.moves.http_client': 'http.client',
    'six.moves.http_cookiejar': 'http.cookiejar',
    'six.moves.http_cookies': 'http.cookies',
    'six.moves.queue': 'queue',
    'six.moves.reprlib': 'reprlib',
    'six.moves.socketserver': 'socketserver',
    'six.moves.tkinter': 'tkinter',
    'six.moves.tkinter_colorchooser': 'tkinter.colorchooser',
    'six.moves.tkinter_commondialog': 'tkinter.commondialog',
    'six.moves.tkinter_constants': 'tkinter.constants',
    'six.moves.tkinter_dialog': 'tkinter.dialog',
    'six.moves.tkinter_dnd': 'tkinter.dnd',
    'six.moves.tkinter_filedialog': 'tkinter.filedialog',
    'six.moves.tkinter_font': 'tkinter.font',
    'six.moves.tkinter_messagebox': 'tkinter.messagebox',
    'six.moves.tkinter_scrolledtext': 'tkinter.scrolledtext',
    'six.moves.tkinter_simpledialog': 'tkinter.simpledialog',
    'six.moves.tkinter_tix': 'tkinter.tix',
    'six.moves.tkinter_tkfiledialog': 'tkinter.filedialog',
    'six.moves.tkinter_tksimpledialog': 'tkinter.simpledialog',
    'six.moves.tkinter_ttk': 'tkinter.ttk',
    'six.moves.urllib.error': 'urllib.error',
    'six.moves.urllib.parse': 'urllib.parse',
    'six.moves.urllib.request': 'urllib.request',
    'six.moves.urllib.response': 'urllib.response',
    'six.moves.urllib.robotparser': 'urllib.robotparser',
    'six.moves.urllib_error': 'urllib.error',
    'six.moves.urllib_parse': 'urllib.parse',
    'six.moves.urllib_robotparser': 'urllib.robotparser',
    'six.moves.winreg': '_winreg',
    'six.moves.xmlrpc_client': 'xmlrpc.client',
    'six.moves.xmlrpc_server': 'xmlrpc.server',
    'xml.etree.cElementTree': 'xml.etree.ElementTree',
}
# END GENERATED


@functools.cache
def _for_version(
        version: tuple[int, ...],
        *,
        keep_mock: bool,
) -> tuple[
        Mapping[str, set[str]],
        Mapping[tuple[str, str], str],
        Mapping[str, str],
]:
    removals = collections.defaultdict(set)
    for ver, ver_removals in REMOVALS.items():
        if ver <= version:
            for base, names in ver_removals.items():
                removals[base].update(names)

    exact = {}
    for ver, ver_exact in REPLACE_EXACT.items():
        if ver <= version:
            exact.update(ver_exact)

    mods = {**REPLACE_MODS}
    if not keep_mock:
        exact['mock', 'mock'] = 'unittest'
        mods.update({
            'mock': 'unittest.mock',
            'mock.mock': 'unittest.mock',
        })

    return removals, exact, mods


def _remove_import(i: int, tokens: list[Token]) -> None:
    del tokens[i:find_end(tokens, i)]


class FromImport(NamedTuple):
    start: int
    mod_start: int
    mod_end: int
    names: tuple[int, ...]
    ends: tuple[int, ...]
    end: int

    @classmethod
    def parse(cls, i: int, tokens: list[Token]) -> FromImport:
        if has_space_before(i, tokens):
            start = i - 1
        else:
            start = i

        j = i + 1
        # XXX: does not handle explicit relative imports
        while tokens[j].name != 'NAME':
            j += 1
        mod_start = j

        import_token = find_name(tokens, j, 'import')
        j = import_token - 1
        while tokens[j].name != 'NAME':
            j -= 1
        mod_end = j

        end = find_end(tokens, import_token)

        # XXX: does not handle `*` imports
        names = [
            j
            for j in range(import_token + 1, end)
            if tokens[j].name == 'NAME'
        ]
        ends_by_offset = {}
        for i in reversed(range(len(names))):
            if tokens[names[i]].src == 'as':
                ends_by_offset[names[i - 1]] = names[i + 1]
                del names[i:i + 2]
        ends = tuple(ends_by_offset.get(pos, pos) for pos in names)

        return cls(start, mod_start, mod_end + 1, tuple(names), ends, end)

    def remove_self(self, tokens: list[Token]) -> None:
        del tokens[self.start:self.end]

    def replace_modname(self, tokens: list[Token], modname: str) -> None:
        tokens[self.mod_start:self.mod_end] = [Token('CODE', modname)]

    def remove_parts(self, tokens: list[Token], idxs: list[int]) -> None:
        for idx in reversed(idxs):
            if idx == 0:  # look forward until next name and del
                del tokens[self.names[idx]:self.names[idx + 1]]
            else:  # look backward for comma and del
                j = self.names[idx]
                while tokens[j].src != ',':
                    j -= 1
                del tokens[j:self.ends[idx] + 1]


def _alias_to_s(alias: ast.alias) -> str:
    if alias.asname:
        return f'{alias.name} as {alias.asname}'
    else:
        return alias.name


def _replace_from_modname(
        i: int,
        tokens: list[Token],
        *,
        modname: str,
) -> None:
    FromImport.parse(i, tokens).replace_modname(tokens, modname)


def _replace_from_mixed(
        i: int,
        tokens: list[Token],
        *,
        removal_idxs: list[int],
        exact_moves: list[tuple[int, str, ast.alias]],
        module_moves: list[tuple[int, str, ast.alias]],
) -> None:
    try:
        indent = indented_amount(i, tokens)
    except ValueError:
        return

    parsed = FromImport.parse(i, tokens)

    added_from_imports = collections.defaultdict(list)
    for idx, mod, alias in exact_moves:
        added_from_imports[mod].append(_alias_to_s(alias))
        bisect.insort(removal_idxs, idx)

    new_imports = []
    for idx, new_mod, alias in module_moves:
        new_mod, _, new_sym = new_mod.rpartition('.')
        new_alias = ast.alias(name=new_sym, asname=alias.asname)
        if new_mod:
            added_from_imports[new_mod].append(_alias_to_s(new_alias))
        else:
            new_imports.append(f'{indent}import {_alias_to_s(new_alias)}\n')
        bisect.insort(removal_idxs, idx)

    new_imports.extend(
        f'{indent}from {mod} import {", ".join(names)}\n'
        for mod, names in added_from_imports.items()
    )
    new_imports.sort()

    if new_imports and tokens[parsed.end - 1].src != '\n':
        new_imports.insert(0, '\n')

    tokens[parsed.end:parsed.end] = [Token('CODE', ''.join(new_imports))]

    # all names rewritten -- delete import
    if len(parsed.names) == len(removal_idxs):
        parsed.remove_self(tokens)
    else:
        parsed.remove_parts(tokens, removal_idxs)


@register(ast.ImportFrom)
def visit_ImportFrom(
        state: State,
        node: ast.ImportFrom,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    removals, exact, mods = _for_version(
        state.settings.min_version,
        keep_mock=state.settings.keep_mock,
    )

    # we don't have any relative rewrites
    if node.level != 0 or node.module is None:
        return

    mod = node.module

    removal_idxs = []
    if node.col_offset == 0:
        removals_for_mod = removals.get(mod)
        if removals_for_mod is not None:
            removal_idxs = [
                i
                for i, alias in enumerate(node.names)
                if not alias.asname and alias.name in removals_for_mod
            ]

    exact_moves = []
    for i, alias in enumerate(node.names):
        new_mod = exact.get((mod, alias.name))
        if new_mod is not None:
            exact_moves.append((i, new_mod, alias))

    module_moves = []
    for i, alias in enumerate(node.names):
        new_mod = mods.get(f'{node.module}.{alias.name}')
        if new_mod is not None and (alias.asname or alias.name == new_mod):
            module_moves.append((i, new_mod, alias))

    if len(removal_idxs) == len(node.names):
        yield ast_to_offset(node), _remove_import
    elif (
            len(exact_moves) == len(node.names) and
            len({mod for _, mod, _ in exact_moves}) == 1
    ):
        _, modname, _ = exact_moves[0]
        func = functools.partial(_replace_from_modname, modname=modname)
        yield ast_to_offset(node), func
    elif removal_idxs or exact_moves or module_moves:
        func = functools.partial(
            _replace_from_mixed,
            removal_idxs=removal_idxs,
            exact_moves=exact_moves,
            module_moves=module_moves,
        )
        yield ast_to_offset(node), func
    elif mod in mods:
        func = functools.partial(_replace_from_modname, modname=mods[mod])
        yield ast_to_offset(node), func


def _replace_import(
        i: int,
        tokens: list[Token],
        *,
        exact_moves: list[tuple[int, str, ast.alias]],
        to_from: list[tuple[int, str, str, ast.alias]],
) -> None:
    try:
        indent = indented_amount(i, tokens)
    except ValueError:
        return

    if has_space_before(i, tokens):
        start = i - 1
    else:
        start = i
    end = find_end(tokens, i)

    parts = []
    start_idx = None
    end_idx = None
    for j in range(i + 1, end):
        if start_idx is None and tokens[j].name == 'NAME':
            start_idx = j
            end_idx = j + 1
        elif start_idx is not None and tokens[j].name == 'NAME':
            end_idx = j + 1
        elif tokens[j].src == ',':
            assert start_idx is not None and end_idx is not None
            parts.append((start_idx, end_idx))
            start_idx = end_idx = None

    assert start_idx is not None and end_idx is not None
    parts.append((start_idx, end_idx))

    for idx, new_mod, alias in reversed(exact_moves):
        new_alias = ast.alias(name=new_mod, asname=alias.asname)
        tokens[slice(*parts[idx])] = [Token('CODE', _alias_to_s(new_alias))]

    new_imports = sorted(
        f'{indent}from {new_mod} import '
        f'{_alias_to_s(ast.alias(name=new_sym, asname=alias.asname))}\n'
        for _, new_mod, new_sym, alias in to_from
    )

    if new_imports and tokens[end - 1].src != '\n':
        new_imports.insert(0, '\n')

    tokens[end:end] = [Token('CODE', ''.join(new_imports))]

    if len(to_from) == len(parts):
        del tokens[start:end]
    else:
        for idx, _, _, _ in reversed(to_from):
            if idx == 0:  # look forward until next name and del
                del tokens[parts[idx][0]:parts[idx + 1][0]]
            else:  # look backward for comma and del
                j = part_end = parts[idx][0]
                while tokens[j].src != ',':
                    j -= 1
                del tokens[j:part_end + 1]


@register(ast.Import)
def visit_Import(
        state: State,
        node: ast.Import,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    _, _, mods = _for_version(
        state.settings.min_version,
        keep_mock=state.settings.keep_mock,
    )

    to_from = []
    exact_moves = []
    for i, alias in enumerate(node.names):
        new_mod = mods.get(alias.name)
        if new_mod is not None:
            alias_base, _, _ = alias.name.partition('.')
            new_mod_base, _, new_sym = new_mod.rpartition('.')
            if new_mod_base and new_sym == alias_base:
                to_from.append((i, new_mod_base, new_sym, alias))
            elif alias.asname is not None:
                exact_moves.append((i, new_mod, alias))

    if to_from or exact_moves:
        func = functools.partial(
            _replace_import,
            exact_moves=exact_moves,
            to_from=to_from,
        )
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/io_open.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_op


def _replace_io_open(i: int, tokens: list[Token]) -> None:
    j = find_op(tokens, i, '(')
    tokens[i:j] = [tokens[i]._replace(name='NAME', src='open')]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'io' and
            node.func.attr == 'open'
    ):
        yield ast_to_offset(node.func), _replace_io_open
```

## File: `pyupgrade/_plugins/legacy.py`
```python
from __future__ import annotations

import ast
import collections
import contextlib
import functools
from collections.abc import Generator
from collections.abc import Iterable
from typing import Any

from tokenize_rt import Offset
from tokenize_rt import Token
from tokenize_rt import tokens_to_src

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import Block
from pyupgrade._token_helpers import find_and_replace_call
from pyupgrade._token_helpers import find_block_start
from pyupgrade._token_helpers import find_name

FUNC_TYPES = (ast.Lambda, ast.FunctionDef, ast.AsyncFunctionDef)


def _fix_yield(i: int, tokens: list[Token]) -> None:
    in_token = find_name(tokens, i, 'in')
    colon = find_block_start(tokens, i)
    block = Block.find(tokens, i, trim_end=True)
    container = tokens_to_src(tokens[in_token + 1:colon]).strip()
    tokens[i:block.end] = [Token('CODE', f'yield from {container}\n')]


def _all_isinstance(
        vals: Iterable[Any],
        tp: type[Any] | tuple[type[Any], ...],
) -> bool:
    return all(isinstance(v, tp) for v in vals)


def _fields_same(n1: ast.AST, n2: ast.AST) -> bool:
    for (a1, v1), (a2, v2) in zip(ast.iter_fields(n1), ast.iter_fields(n2)):
        # ignore ast attributes, they'll be covered by walk
        if a1 != a2:
            return False
        elif _all_isinstance((v1, v2), ast.AST):
            continue
        elif _all_isinstance((v1, v2), (list, tuple)):
            if len(v1) != len(v2):
                return False
            # ignore sequences which are all-ast, they'll be covered by walk
            elif _all_isinstance(v1, ast.AST) and _all_isinstance(v2, ast.AST):
                continue
            elif v1 != v2:
                return False
        elif v1 != v2:
            return False
    return True


def _targets_same(target: ast.AST, yield_value: ast.AST) -> bool:
    for t1, t2 in zip(ast.walk(target), ast.walk(yield_value)):
        # ignore `ast.Load` / `ast.Store`
        if _all_isinstance((t1, t2), ast.expr_context):
            continue
        elif type(t1) is not type(t2):
            return False
        elif not _fields_same(t1, t2):
            return False
    else:
        return True


class Scope:
    def __init__(self, node: ast.AST) -> None:
        self.node = node

        self.reads: set[str] = set()
        self.writes: set[str] = set()

        self.yield_from_fors: set[Offset] = set()
        self.yield_from_names: dict[str, set[Offset]]
        self.yield_from_names = collections.defaultdict(set)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self._scopes: list[Scope] = []
        self.super_offsets: set[Offset] = set()
        self.yield_offsets: set[Offset] = set()

    @contextlib.contextmanager
    def _scope(self, node: ast.AST) -> Generator[None]:
        self._scopes.append(Scope(node))
        try:
            yield
        finally:
            info = self._scopes.pop()
            # discard any that were referenced outside of the loop
            for name in info.reads:
                offsets = info.yield_from_names[name]
                info.yield_from_fors.difference_update(offsets)
            self.yield_offsets.update(info.yield_from_fors)
            if self._scopes:
                cell_reads = info.reads - info.writes
                self._scopes[-1].reads.update(cell_reads)

    def _visit_scope(self, node: ast.AST) -> None:
        with self._scope(node):
            self.generic_visit(node)

    visit_ClassDef = _visit_scope
    visit_Lambda = visit_FunctionDef = visit_AsyncFunctionDef = _visit_scope
    visit_ListComp = visit_SetComp = _visit_scope
    visit_DictComp = visit_GeneratorExp = _visit_scope

    def visit_Name(self, node: ast.Name) -> None:
        if self._scopes:
            if isinstance(node.ctx, ast.Load):
                self._scopes[-1].reads.add(node.id)
            elif isinstance(node.ctx, (ast.Store, ast.Del)):
                self._scopes[-1].writes.add(node.id)
            else:
                raise AssertionError(node)

        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if (
                isinstance(node.func, ast.Name) and
                node.func.id == 'super' and
                len(node.args) == 2 and
                isinstance(node.args[1], ast.Name) and
                # there are at least two scopes
                len(self._scopes) >= 2 and
                # the last scope is a function where the first arg is arg2
                isinstance(self._scopes[-1].node, FUNC_TYPES) and
                self._scopes[-1].node.args.args and
                node.args[1].id == self._scopes[-1].node.args.args[0].arg
        ):
            args = node.args[0]
            scope = len(self._scopes) - 2
            current_scope = self._scopes[scope]
            # if in nested classes, all names in arg1 must match the scopes
            while (
                    isinstance(args, ast.Attribute) and
                    scope > 0 and
                    isinstance(current_scope.node, ast.ClassDef) and
                    args.attr == current_scope.node.name
            ):
                args = args.value
                scope -= 1
                current_scope = self._scopes[scope]
            # now check if it is outer most class and its name match
            if (
                    isinstance(args, ast.Name) and
                    isinstance(current_scope.node, ast.ClassDef) and
                    args.id == current_scope.node.name and
                    # an enclosing scope cannot be a class
                    (
                        scope == 0 or
                        not isinstance(
                            self._scopes[scope - 1].node,
                            ast.ClassDef,
                        )
                    )
            ):
                self.super_offsets.add(ast_to_offset(node))

        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:
        if (
            len(self._scopes) >= 1 and
            not isinstance(self._scopes[-1].node, ast.AsyncFunctionDef) and
            len(node.body) == 1 and
            isinstance(node.body[0], ast.Expr) and
            isinstance(node.body[0].value, ast.Yield) and
            node.body[0].value.value is not None and
            _targets_same(node.target, node.body[0].value.value) and
            not node.orelse
        ):
            offset = ast_to_offset(node)
            func_info = self._scopes[-1]
            func_info.yield_from_fors.add(offset)
            for target_node in ast.walk(node.target):
                if (
                        isinstance(target_node, ast.Name) and
                        isinstance(target_node.ctx, ast.Store)
                ):
                    func_info.yield_from_names[target_node.id].add(offset)
            # manually visit, but with target+body as a separate scope
            self.visit(node.iter)
            with self._scope(node):
                self.visit(node.target)
                for stmt in node.body:
                    self.visit(stmt)
                assert not node.orelse
        else:
            self.generic_visit(node)


@register(ast.Module)
def visit_Module(
        state: State,
        node: ast.Module,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    visitor = Visitor()
    visitor.visit(node)

    super_func = functools.partial(find_and_replace_call, template='super()')
    for offset in visitor.super_offsets:
        yield offset, super_func

    for offset in visitor.yield_offsets:
        yield offset, _fix_yield
```

## File: `pyupgrade/_plugins/lru_cache.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_and_replace_call
from pyupgrade._token_helpers import find_op


def _remove_call(i: int, tokens: list[Token]) -> None:
    i = find_op(tokens, i, '(')
    j = find_op(tokens, i, ')')
    del tokens[i:j + 1]


def _is_literal_kwarg(
        keyword: ast.keyword, name: str, value: bool | None,
) -> bool:
    return (
        keyword.arg == name and
        isinstance(keyword.value, ast.Constant) and
        keyword.value.value is value
    )


def _eligible(keywords: list[ast.keyword]) -> bool:
    if len(keywords) == 1:
        return _is_literal_kwarg(keywords[0], 'maxsize', None)
    elif len(keywords) == 2:
        return (
            (
                _is_literal_kwarg(keywords[0], 'maxsize', None) and
                _is_literal_kwarg(keywords[1], 'typed', False)
            ) or
            (
                _is_literal_kwarg(keywords[1], 'maxsize', None) and
                _is_literal_kwarg(keywords[0], 'typed', False)
            )
        )
    else:
        return False


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            state.settings.min_version >= (3, 8) and
            not node.args and
            not node.keywords and
            is_name_attr(
                node.func,
                state.from_imports,
                ('functools',),
                ('lru_cache',),
            )
    ):
        yield ast_to_offset(node), _remove_call
    elif (
            state.settings.min_version >= (3, 9) and
            isinstance(node.func, ast.Attribute) and
            node.func.attr == 'lru_cache' and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'functools' and
            not node.args and
            _eligible(node.keywords)
    ):
        func = functools.partial(
            find_and_replace_call, template='functools.cache',
        )
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/metaclass_type.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_end


def _remove_metaclass_type(i: int, tokens: list[Token]) -> None:
    j = find_end(tokens, i)
    del tokens[i:j]


@register(ast.Assign)
def visit_Assign(
        state: State,
        node: ast.Assign,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            len(node.targets) == 1 and
            isinstance(node.targets[0], ast.Name) and
            node.targets[0].col_offset == 0 and
            node.targets[0].id == '__metaclass__' and
            isinstance(node.value, ast.Name) and
            node.value.id == 'type'
    ):
        yield ast_to_offset(node), _remove_metaclass_type
```

## File: `pyupgrade/_plugins/mock.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_name


def _fix_mock_mock(i: int, tokens: list[Token]) -> None:
    j = find_name(tokens, i + 1, 'mock')
    del tokens[i + 1:j + 1]


@register(ast.Attribute)
def visit_Attribute(
        state: State,
        node: ast.Attribute,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            not state.settings.keep_mock and
            isinstance(node.value, ast.Name) and
            node.value.id == 'mock' and
            node.attr == 'mock'
    ):
        yield ast_to_offset(node), _fix_mock_mock
```

## File: `pyupgrade/_plugins/native_literals.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args
from pyupgrade._token_helpers import replace_call

SIX_NATIVE_STR = frozenset(('ensure_str', 'ensure_text', 'text_type'))


def _fix_literal(i: int, tokens: list[Token], *, empty: str) -> None:
    j = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, j)
    if any(tok.name == 'NL' for tok in tokens[i:end]):
        return
    if func_args:
        replace_call(tokens, i, end, func_args, '{args[0]}')
    else:
        tokens[i:end] = [tokens[i]._replace(name='STRING', src=empty)]


def is_a_native_literal_call(
        node: ast.Call,
        from_imports: dict[str, set[str]],
) -> bool:
    return (
        (
            is_name_attr(node.func, from_imports, ('six',), SIX_NATIVE_STR) or
            isinstance(node.func, ast.Name) and node.func.id == 'str'
        ) and
        not node.keywords and
        not has_starargs(node) and
        (
            len(node.args) == 0 or
            (
                len(node.args) == 1 and
                isinstance(node.args[0], ast.Constant) and
                isinstance(node.args[0].value, str)
            )
        )
    )


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if is_a_native_literal_call(node, state.from_imports):
        func = functools.partial(_fix_literal, empty="''")
        yield ast_to_offset(node), func
    elif (
            isinstance(node.func, ast.Name) and node.func.id == 'bytes' and
            not node.keywords and not has_starargs(node) and
            (
                len(node.args) == 0 or (
                    len(node.args) == 1 and
                    isinstance(node.args[0], ast.Constant) and
                    isinstance(node.args[0].value, bytes)
                )
            )
    ):
        func = functools.partial(_fix_literal, empty="b''")
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/new_style_classes.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import remove_base_class


@register(ast.ClassDef)
def visit_ClassDef(
        state: State,
        node: ast.ClassDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    for base in node.bases:
        if isinstance(base, ast.Name) and base.id == 'object':
            yield ast_to_offset(base), remove_base_class
```

## File: `pyupgrade/_plugins/open_mode.py`
```python
from __future__ import annotations

import ast
import functools
import itertools
from collections.abc import Iterable
from typing import NamedTuple

from tokenize_rt import Offset
from tokenize_rt import Token
from tokenize_rt import tokens_to_src

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import delete_argument
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args


def _plus(args: tuple[str, ...]) -> tuple[str, ...]:
    return args + tuple(f'{arg}+' for arg in args)


def _permute(*args: str) -> tuple[str, ...]:
    return tuple(''.join(p) for s in args for p in itertools.permutations(s))


MODE_REMOVE = frozenset(_permute('U', 'r', 'rU', 'rt'))
MODE_REPLACE_R = frozenset(_permute('Ub'))
MODE_REMOVE_T = frozenset(_plus(_permute('at', 'rt', 'wt', 'xt')))
MODE_REMOVE_U = frozenset(_permute('rUb'))
MODE_REPLACE = MODE_REPLACE_R | MODE_REMOVE_T | MODE_REMOVE_U


class FunctionArg(NamedTuple):
    arg_idx: int
    value: ast.expr


def _fix_open_mode(i: int, tokens: list[Token], *, arg_idx: int) -> None:
    j = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, j)
    mode = tokens_to_src(tokens[slice(*func_args[arg_idx])])
    mode_stripped = mode.split('=')[-1]
    mode_stripped = ast.literal_eval(mode_stripped.strip())
    if mode_stripped in MODE_REMOVE:
        delete_argument(arg_idx, tokens, func_args)
    elif mode_stripped in MODE_REPLACE_R:
        new_mode = mode.replace('U', 'r')
        tokens[slice(*func_args[arg_idx])] = [Token('SRC', new_mode)]
    elif mode_stripped in MODE_REMOVE_T:
        new_mode = mode.replace('t', '')
        tokens[slice(*func_args[arg_idx])] = [Token('SRC', new_mode)]
    elif mode_stripped in MODE_REMOVE_U:
        new_mode = mode.replace('U', '')
        tokens[slice(*func_args[arg_idx])] = [Token('SRC', new_mode)]
    else:
        raise AssertionError(f'unreachable: {mode!r}')


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            (
                (
                    isinstance(node.func, ast.Name) and
                    node.func.id == 'open'
                ) or (
                    isinstance(node.func, ast.Attribute) and
                    isinstance(node.func.value, ast.Name) and
                    node.func.value.id == 'io' and
                    node.func.attr == 'open'
                )
            ) and
            not has_starargs(node)
    ):
        if (
                len(node.args) >= 2 and
                isinstance(node.args[1], ast.Constant) and
                isinstance(node.args[1].value, str)
        ):
            if (
                node.args[1].value in MODE_REPLACE or
                (len(node.args) == 2 and node.args[1].value in MODE_REMOVE)
            ):
                func = functools.partial(_fix_open_mode, arg_idx=1)
                yield ast_to_offset(node), func
        elif node.keywords and (len(node.keywords) + len(node.args) > 1):
            mode = next(
                (
                    FunctionArg(n, keyword.value)
                    for n, keyword in enumerate(node.keywords)
                    if keyword.arg == 'mode'
                ),
                None,
            )
            if (
                mode is not None and
                isinstance(mode.value, ast.Constant) and
                isinstance(mode.value.value, str) and
                (
                    mode.value.value in MODE_REMOVE or
                    mode.value.value in MODE_REPLACE
                )
            ):
                func = functools.partial(
                    _fix_open_mode,
                    arg_idx=len(node.args) + mode.arg_idx,
                )
                yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/percent_format.py`
```python
from __future__ import annotations

import ast
import functools
import re
from collections.abc import Generator
from collections.abc import Iterable
from re import Match
from re import Pattern
from typing import Optional

from tokenize_rt import Offset
from tokenize_rt import Token
from tokenize_rt import tokens_to_src

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._string_helpers import curly_escape
from pyupgrade._token_helpers import KEYWORDS
from pyupgrade._token_helpers import remove_brace
from pyupgrade._token_helpers import victims

PercentFormatPart = tuple[
    Optional[str],
    Optional[str],
    Optional[str],
    Optional[str],
    str,
]
PercentFormat = tuple[str, Optional[PercentFormatPart]]

MAPPING_KEY_RE = re.compile(r'\(([^()]*)\)')
CONVERSION_FLAG_RE = re.compile('[#0+ -]*')
WIDTH_RE = re.compile(r'(?:\*|\d*)')
PRECISION_RE = re.compile(r'(?:\.(?:\*|\d*))?')
LENGTH_RE = re.compile('[hlL]?')


def _must_match(regex: Pattern[str], string: str, pos: int) -> Match[str]:
    match = regex.match(string, pos)
    assert match is not None
    return match


def _parse_percent_format(s: str) -> tuple[PercentFormat, ...]:
    def _parse_inner() -> Generator[PercentFormat]:
        string_start = 0
        string_end = 0
        in_fmt = False

        i = 0
        while i < len(s):
            if not in_fmt:
                try:
                    i = s.index('%', i)
                except ValueError:  # no more % fields!
                    yield s[string_start:], None
                    return
                else:
                    string_end = i
                    i += 1
                    in_fmt = True
            else:
                key_match = MAPPING_KEY_RE.match(s, i)
                if key_match:
                    key: str | None = key_match.group(1)
                    i = key_match.end()
                else:
                    key = None

                conversion_flag_match = _must_match(CONVERSION_FLAG_RE, s, i)
                conversion_flag = conversion_flag_match.group() or None
                i = conversion_flag_match.end()

                width_match = _must_match(WIDTH_RE, s, i)
                width = width_match.group() or None
                i = width_match.end()

                precision_match = _must_match(PRECISION_RE, s, i)
                precision = precision_match.group() or None
                i = precision_match.end()

                # length modifier is ignored
                i = _must_match(LENGTH_RE, s, i).end()

                try:
                    conversion = s[i]
                except IndexError:
                    raise ValueError('end-of-string while parsing format')
                i += 1

                fmt = (key, conversion_flag, width, precision, conversion)
                yield s[string_start:string_end], fmt

                in_fmt = False
                string_start = i

        if in_fmt:
            raise ValueError('end-of-string while parsing format')

    return tuple(_parse_inner())


def _simplify_conversion_flag(flag: str) -> str:
    parts: list[str] = []
    for c in flag:
        if c in parts:
            continue
        c = c.replace('-', '<')
        parts.append(c)
        if c == '<' and '0' in parts:
            parts.remove('0')
        elif c == '+' and ' ' in parts:
            parts.remove(' ')
    return ''.join(parts)


def _percent_to_format(s: str) -> str:
    def _handle_part(part: PercentFormat) -> str:
        s, fmt = part
        s = curly_escape(s)

        if fmt is None:
            return s
        else:
            key, conversion_flag, width, precision, conversion = fmt
            if conversion == '%':
                return s + '%'
            parts = [s, '{']
            if conversion == 's':
                conversion = ''
            if key:
                parts.append(key)
            if conversion in {'r', 'a'}:
                converter = f'!{conversion}'
                conversion = ''
            else:
                converter = ''
            if any((conversion_flag, width, precision, conversion)):
                parts.append(':')
            if conversion_flag:
                parts.append(_simplify_conversion_flag(conversion_flag))
            parts.extend(x for x in (width, precision, conversion) if x)
            parts.extend(converter)
            parts.append('}')
            return ''.join(parts)

    return ''.join(_handle_part(part) for part in _parse_percent_format(s))


def _fix_percent_format_tuple(
        i: int,
        tokens: list[Token],
        *,
        node_right: ast.Tuple,
) -> None:
    # TODO: this is overly timid
    paren = i + 4
    if tokens_to_src(tokens[i + 1:paren + 1]) != ' % (':
        return

    fmt_victims = victims(tokens, paren, node_right, gen=False)
    fmt_victims.ends.pop()

    for index in reversed(fmt_victims.starts + fmt_victims.ends):
        remove_brace(tokens, index)

    newsrc = _percent_to_format(tokens[i].src)
    tokens[i] = tokens[i]._replace(src=newsrc)
    tokens[i + 1:paren] = [Token('Format', '.format'), Token('OP', '(')]


def _fix_percent_format_dict(
        i: int,
        tokens: list[Token],
        *,
        node_right: ast.Dict,
) -> None:
    seen_keys: set[str] = set()
    keys = {}

    for k in node_right.keys:
        # not a string key
        if not isinstance(k, ast.Constant) or not isinstance(k.value, str):
            return
        # duplicate key
        elif k.value in seen_keys:
            return
        # not an identifier
        elif not k.value.isidentifier():
            return
        # a keyword
        elif k.value in KEYWORDS:
            return
        seen_keys.add(k.value)
        keys[ast_to_offset(k)] = k.value

    # TODO: this is overly timid
    brace = i + 4
    if tokens_to_src(tokens[i + 1:brace + 1]) != ' % {':
        return

    fmt_victims = victims(tokens, brace, node_right, gen=False)
    brace_end = fmt_victims.ends[-1]

    key_indices = []
    for j, token in enumerate(tokens[brace:brace_end], brace):
        key = keys.pop(token.offset, None)
        if key is None:
            continue
        # we found the key, but the string didn't match (implicit join?)
        elif ast.literal_eval(token.src) != key:
            return
        # the map uses some strange syntax that's not `'key': value`
        elif tokens[j + 1].src != ':' or tokens[j + 2].src != ' ':
            return
        else:
            key_indices.append((j, key))
    assert not keys, keys

    tokens[brace_end] = tokens[brace_end]._replace(src=')')
    for key_index, s in reversed(key_indices):
        tokens[key_index:key_index + 3] = [Token('CODE', f'{s}=')]
    newsrc = _percent_to_format(tokens[i].src)
    tokens[i] = tokens[i]._replace(src=newsrc)
    tokens[i + 1:brace + 1] = [Token('CODE', '.format'), Token('OP', '(')]


@register(ast.BinOp)
def visit_BinOp(
        state: State,
        node: ast.BinOp,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            not state.settings.keep_percent_format and
            isinstance(node.op, ast.Mod) and
            isinstance(node.left, ast.Constant) and
            isinstance(node.left.value, str)
    ):
        try:
            parsed = _parse_percent_format(node.left.value)
        except ValueError:
            pass
        else:
            for _, fmt in parsed:
                if not fmt:
                    continue
                key, conversion_flag, width, precision, conversion = fmt
                # timid: these require out-of-order parameter consumption
                if width == '*' or precision == '.*':
                    break
                # these conversions require modification of parameters
                if conversion in {'d', 'i', 'u', 'c'}:
                    break
                # timid: py2: %#o formats different from {:#o} (--py3?)
                if '#' in (conversion_flag or '') and conversion == 'o':
                    break
                # no equivalent in format
                if key == '':
                    break
                # timid: py2: conversion is subject to modifiers (--py3?)
                nontrivial_fmt = any((conversion_flag, width, precision))
                if conversion == '%' and nontrivial_fmt:
                    break
                # no equivalent in format
                if conversion in {'a', 'r'} and nontrivial_fmt:
                    break
                # %s with None and width is not supported
                if width and conversion == 's':
                    break
                # all dict substitutions must be named
                if isinstance(node.right, ast.Dict) and not key:
                    break
            else:
                if isinstance(node.right, ast.Tuple):
                    func = functools.partial(
                        _fix_percent_format_tuple,
                        node_right=node.right,
                    )
                    yield ast_to_offset(node), func
                elif isinstance(node.right, ast.Dict):
                    func = functools.partial(
                        _fix_percent_format_dict,
                        node_right=node.right,
                    )
                    yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/set_literals.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_closing_bracket
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import immediately_paren
from pyupgrade._token_helpers import remove_brace
from pyupgrade._token_helpers import victims

SET_TRANSFORM = (ast.List, ast.ListComp, ast.GeneratorExp, ast.Tuple)


def _fix_set_empty_literal(i: int, tokens: list[Token]) -> None:
    i = find_op(tokens, i, '(')
    j = find_closing_bracket(tokens, i)
    del tokens[i + 1:j]


def _fix_set_literal(i: int, tokens: list[Token], *, arg: ast.expr) -> None:
    # TODO: this could be implemented with a little extra logic
    if not immediately_paren('set', tokens, i):
        return

    gen = isinstance(arg, ast.GeneratorExp)
    set_victims = victims(tokens, i + 1, arg, gen=gen)

    del set_victims.starts[0]
    end_index = set_victims.ends.pop()

    tokens[end_index] = Token('OP', '}')
    for index in reversed(set_victims.starts + set_victims.ends):
        remove_brace(tokens, index)
    tokens[i:i + 2] = [Token('OP', '{')]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            not isinstance(parent, ast.FormattedValue) and
            isinstance(node.func, ast.Name) and
            node.func.id == 'set' and
            len(node.args) == 1 and
            not node.keywords and
            isinstance(node.args[0], SET_TRANSFORM)
    ):
        arg, = node.args
        if isinstance(arg, (ast.List, ast.Tuple)) and not arg.elts:
            yield ast_to_offset(node.func), _fix_set_empty_literal
        else:
            func = functools.partial(_fix_set_literal, arg=arg)
            yield ast_to_offset(node.func), func
```

## File: `pyupgrade/_plugins/shlex_join.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_name
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import victims


def _fix_shlex_join(i: int, tokens: list[Token], *, arg: ast.expr) -> None:
    j = find_op(tokens, i, '(')
    comp_victims = victims(tokens, j, arg, gen=True)
    k = find_name(tokens, comp_victims.arg_index, 'in') + 1
    while tokens[k].name in NON_CODING_TOKENS:
        k += 1
    tokens[comp_victims.ends[0]:comp_victims.ends[-1] + 1] = [Token('OP', ')')]
    tokens[i:k] = [Token('CODE', 'shlex.join'), Token('OP', '(')]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if state.settings.min_version < (3, 8):
        return

    if (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Constant) and
            node.func.value.value == ' ' and
            node.func.attr == 'join' and
            not node.keywords and
            len(node.args) == 1 and
            isinstance(node.args[0], (ast.ListComp, ast.GeneratorExp)) and
            isinstance(node.args[0].elt, ast.Call) and
            isinstance(node.args[0].elt.func, ast.Attribute) and
            isinstance(node.args[0].elt.func.value, ast.Name) and
            node.args[0].elt.func.value.id == 'shlex' and
            node.args[0].elt.func.attr == 'quote' and
            not node.args[0].elt.keywords and
            len(node.args[0].elt.args) == 1 and
            isinstance(node.args[0].elt.args[0], ast.Name) and
            len(node.args[0].generators) == 1 and
            isinstance(node.args[0].generators[0].target, ast.Name) and
            not node.args[0].generators[0].ifs and
            not node.args[0].generators[0].is_async and
            node.args[0].elt.args[0].id == node.args[0].generators[0].target.id
    ):
        func = functools.partial(_fix_shlex_join, arg=node.args[0])
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/six_base_classes.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import remove_base_class


@register(ast.ClassDef)
def visit_ClassDef(
        state: State,
        node: ast.ClassDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    for base in node.bases:
        if is_name_attr(base, state.from_imports, ('six',), ('Iterator',)):
            yield ast_to_offset(base), remove_base_class
```

## File: `pyupgrade/_plugins/six_calls.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_and_replace_call
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args
from pyupgrade._token_helpers import replace_call

_EXPR_NEEDS_PARENS: tuple[type[ast.expr], ...] = (
    ast.Await, ast.BinOp, ast.BoolOp, ast.Compare, ast.GeneratorExp, ast.IfExp,
    ast.Lambda, ast.UnaryOp, ast.NamedExpr,
)

SIX_CALLS = {
    'u': '{args[0]}',
    'byte2int': '{args[0]}[0]',
    'indexbytes': '{args[0]}[{rest}]',
    'iteritems': '{args[0]}.items()',
    'iterkeys': '{args[0]}.keys()',
    'itervalues': '{args[0]}.values()',
    'viewitems': '{args[0]}.items()',
    'viewkeys': '{args[0]}.keys()',
    'viewvalues': '{args[0]}.values()',
    'create_unbound_method': '{args[0]}',
    'get_unbound_function': '{args[0]}',
    'get_method_function': '{args[0]}.__func__',
    'get_method_self': '{args[0]}.__self__',
    'get_function_closure': '{args[0]}.__closure__',
    'get_function_code': '{args[0]}.__code__',
    'get_function_defaults': '{args[0]}.__defaults__',
    'get_function_globals': '{args[0]}.__globals__',
    'assertCountEqual': '{args[0]}.assertCountEqual({rest})',
    'assertRaisesRegex': '{args[0]}.assertRaisesRegex({rest})',
    'assertRegex': '{args[0]}.assertRegex({rest})',
}
SIX_INT2BYTE_TMPL = 'bytes(({args[0]},))'
RAISE_FROM_TMPL = 'raise {args[0]} from {args[1]}'
RERAISE_TMPL = 'raise'
RERAISE_2_TMPL = 'raise {args[1]}.with_traceback(None)'
RERAISE_3_TMPL = 'raise {args[1]}.with_traceback({args[2]})'


def _fix_six_b(i: int, tokens: list[Token]) -> None:
    j = find_op(tokens, i, '(')
    if (
            tokens[j + 1].name == 'STRING' and
            tokens[j + 1].src.isascii() and
            tokens[j + 2].src == ')'
    ):
        func_args, end = parse_call_args(tokens, j)
        replace_call(tokens, i, end, func_args, 'b{args[0]}')


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if isinstance(node.func, ast.Name):
        name = node.func.id
    elif isinstance(node.func, ast.Attribute):
        name = node.func.attr
    else:
        return

    if (
            is_name_attr(
                node.func,
                state.from_imports,
                ('six',),
                ('iteritems', 'iterkeys', 'itervalues'),
            ) and
            node.args and
            not has_starargs(node) and
            # parent is next(...)
            isinstance(parent, ast.Call) and
            isinstance(parent.func, ast.Name) and
            parent.func.id == 'next'
    ):
        func = functools.partial(
            find_and_replace_call,
            template=f'iter({SIX_CALLS[name]})',
        )
        yield ast_to_offset(node), func
    elif (
            is_name_attr(
                node.func,
                state.from_imports,
                ('six',),
                SIX_CALLS,
            ) and
            node.args and
            not has_starargs(node)
    ):
        if isinstance(node.args[0], _EXPR_NEEDS_PARENS):
            parens: tuple[int, ...] = (0,)
        else:
            parens = ()
        func = functools.partial(
            find_and_replace_call,
            template=SIX_CALLS[name],
            parens=parens,
        )
        yield ast_to_offset(node), func
    elif (
            is_name_attr(
                node.func,
                state.from_imports,
                ('six',),
                ('int2byte',),
            ) and
            node.args and
            not has_starargs(node)
    ):
        func = functools.partial(
            find_and_replace_call,
            template=SIX_INT2BYTE_TMPL,
        )
        yield ast_to_offset(node), func
    elif (
            is_name_attr(
                node.func,
                state.from_imports,
                ('six',),
                ('b', 'ensure_binary'),
            ) and
            not node.keywords and
            not has_starargs(node) and
            len(node.args) == 1 and
            isinstance(node.args[0], ast.Constant) and
            isinstance(node.args[0].value, str)
    ):
        yield ast_to_offset(node), _fix_six_b
    elif (
            isinstance(parent, ast.Expr) and
            is_name_attr(
                node.func,
                state.from_imports,
                ('six',),
                ('raise_from',),
            ) and
            node.args and
            not has_starargs(node)
    ):
        func = functools.partial(
            find_and_replace_call,
            template=RAISE_FROM_TMPL,
        )
        yield ast_to_offset(node), func
    elif (
            isinstance(parent, ast.Expr) and
            is_name_attr(
                node.func,
                state.from_imports,
                ('six',),
                ('reraise',),
            )
    ):
        if (
                len(node.args) == 2 and
                not node.keywords and
                not has_starargs(node)
        ):
            func = functools.partial(
                find_and_replace_call,
                template=RERAISE_2_TMPL,
            )
            yield ast_to_offset(node), func
        elif (
                len(node.args) == 3 and
                not node.keywords and
                not has_starargs(node)
        ):
            func = functools.partial(
                find_and_replace_call,
                template=RERAISE_3_TMPL,
            )
            yield ast_to_offset(node), func
        elif (
                len(node.args) == 1 and
                not node.keywords and
                isinstance(node.args[0], ast.Starred) and
                isinstance(node.args[0].value, ast.Call) and
                is_name_attr(
                    node.args[0].value.func,
                    state.from_imports,
                    ('sys',),
                    ('exc_info',),
                )
        ):
            func = functools.partial(
                find_and_replace_call,
                template=RERAISE_TMPL,
            )
            yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/six_metaclasses.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import arg_str
from pyupgrade._token_helpers import find_block_start
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args
from pyupgrade._token_helpers import remove_decorator
from pyupgrade._token_helpers import replace_call


def _fix_add_metaclass(i: int, tokens: list[Token]) -> None:
    j = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, j)
    metaclass = f'metaclass={arg_str(tokens, *func_args[0])}'
    # insert `metaclass={args[0]}` into `class:`
    # search forward for the `class` token
    j = i + 1
    while not tokens[j].matches(name='NAME', src='class'):
        j += 1
    class_token = j
    # then search forward for a `:` token, not inside a brace
    j = find_block_start(tokens, j)
    last_paren = -1
    for k in range(class_token, j):
        if tokens[k].src == ')':
            last_paren = k

    if last_paren == -1:
        tokens.insert(j, Token('CODE', f'({metaclass})'))
    else:
        insert = last_paren - 1
        while tokens[insert].name in NON_CODING_TOKENS:
            insert -= 1
        if tokens[insert].src == '(':  # no bases
            src = metaclass
        elif tokens[insert].src != ',':
            src = f', {metaclass}'
        else:
            src = f' {metaclass},'
        tokens.insert(insert + 1, Token('CODE', src))
    remove_decorator(i, tokens)


def _fix_with_metaclass(i: int, tokens: list[Token]) -> None:
    j = find_op(tokens, i, '(')
    func_args, end = parse_call_args(tokens, j)
    if len(func_args) == 1:
        tmpl = 'metaclass={args[0]}'
    elif len(func_args) == 2:
        base = arg_str(tokens, *func_args[1])
        if base == 'object':
            tmpl = 'metaclass={args[0]}'
        else:
            tmpl = '{rest}, metaclass={args[0]}'
    else:
        tmpl = '{rest}, metaclass={args[0]}'
    replace_call(tokens, i, end, func_args, tmpl)


@register(ast.ClassDef)
def visit_ClassDef(
        state: State,
        node: ast.ClassDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    for decorator in node.decorator_list:
        if (
                isinstance(decorator, ast.Call) and
                is_name_attr(
                    decorator.func,
                    state.from_imports,
                    ('six',),
                    ('add_metaclass',),
                ) and
                not has_starargs(decorator)
        ):
            yield ast_to_offset(decorator), _fix_add_metaclass

    if (
            len(node.bases) == 1 and
            isinstance(node.bases[0], ast.Call) and
            is_name_attr(
                node.bases[0].func,
                state.from_imports,
                ('six',),
                ('with_metaclass',),
            ) and
            not has_starargs(node.bases[0])
    ):
        yield ast_to_offset(node.bases[0]), _fix_with_metaclass
```

## File: `pyupgrade/_plugins/six_remove_decorators.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import remove_decorator


@register(ast.ClassDef)
def visit_ClassDef(
        state: State,
        node: ast.ClassDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    for decorator in node.decorator_list:
        if is_name_attr(
                decorator,
                state.from_imports,
                ('six',),
                ('python_2_unicode_compatible',),
        ):
            yield ast_to_offset(decorator), remove_decorator
```

## File: `pyupgrade/_plugins/six_simple.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_type_check
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._plugins.imports import REMOVALS
from pyupgrade._plugins.native_literals import is_a_native_literal_call
from pyupgrade._token_helpers import replace_name

NAMES = {
    'text_type': 'str',
    'binary_type': 'bytes',
    'class_types': '(type,)',
    'string_types': '(str,)',
    'integer_types': '(int,)',
    'unichr': 'chr',
    'iterbytes': 'iter',
    'print_': 'print',
    'exec_': 'exec',
    'advance_iterator': 'next',
    'next': 'next',
    'callable': 'callable',
}
NAMES_MOVES = REMOVALS[(3,)]['six.moves']
NAMES_TYPE_CTX = {
    'class_types': 'type',
    'string_types': 'str',
    'integer_types': 'int',
}


@register(ast.Attribute)
def visit_Attribute(
        state: State,
        node: ast.Attribute,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.value, ast.Name) and
            node.value.id == 'six' and
            node.attr in NAMES
    ):
        # these will be handled by the native literals plugin
        if (
                isinstance(parent, ast.Call) and
                is_a_native_literal_call(parent, state.from_imports)
        ):
            return

        if node.attr in NAMES_TYPE_CTX and is_type_check(parent):
            new = NAMES_TYPE_CTX[node.attr]
        else:
            new = NAMES[node.attr]

        func = functools.partial(replace_name, name=node.attr, new=new)
        yield ast_to_offset(node), func
    elif (
            isinstance(node.value, ast.Attribute) and
            isinstance(node.value.value, ast.Name) and
            node.value.value.id == 'six' and
            node.value.attr == 'moves' and
            node.attr == 'xrange'
    ):
        func = functools.partial(replace_name, name=node.attr, new='range')
        yield ast_to_offset(node), func
    elif (
            isinstance(node.value, ast.Attribute) and
            isinstance(node.value.value, ast.Name) and
            node.value.value.id == 'six' and
            node.value.attr == 'moves' and
            node.attr in NAMES_MOVES
    ):
        func = functools.partial(replace_name, name=node.attr, new=node.attr)
        yield ast_to_offset(node), func


@register(ast.Name)
def visit_Name(
        state: State,
        node: ast.Name,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            node.id in state.from_imports['six'] and
            node.id in NAMES
    ):
        # these will be handled by the native literals plugin
        if (
                isinstance(parent, ast.Call) and
                is_a_native_literal_call(parent, state.from_imports)
        ):
            return

        if node.id in NAMES_TYPE_CTX and is_type_check(parent):
            new = NAMES_TYPE_CTX[node.id]
        else:
            new = NAMES[node.id]

        func = functools.partial(replace_name, name=node.id, new=new)
        yield ast_to_offset(node), func
    elif (
            node.id in state.from_imports['six.moves'] and
            node.id in {'xrange', 'range'}
    ):
        func = functools.partial(replace_name, name=node.id, new='range')
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/subprocess_run.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import delete_argument
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args
from pyupgrade._token_helpers import replace_argument


def _use_capture_output(
    i: int,
    tokens: list[Token],
    *,
    stdout_arg_idx: int,
    stderr_arg_idx: int,
) -> None:
    j = find_op(tokens, i, '(')
    func_args, _ = parse_call_args(tokens, j)
    if stdout_arg_idx < stderr_arg_idx:
        delete_argument(stderr_arg_idx, tokens, func_args)
        replace_argument(
            stdout_arg_idx,
            tokens,
            func_args,
            new='capture_output=True',
        )
    else:
        replace_argument(
            stdout_arg_idx,
            tokens,
            func_args,
            new='capture_output=True',
        )
        delete_argument(stderr_arg_idx, tokens, func_args)


def _replace_universal_newlines_with_text(
    i: int,
    tokens: list[Token],
    *,
    arg_idx: int,
) -> None:
    j = find_op(tokens, i, '(')
    func_args, _ = parse_call_args(tokens, j)
    for i in range(*func_args[arg_idx]):
        if tokens[i].src == 'universal_newlines':
            tokens[i] = tokens[i]._replace(src='text')
            break
    else:
        raise AssertionError('`universal_newlines` argument not found')


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            state.settings.min_version >= (3, 7) and
            is_name_attr(
                node.func,
                state.from_imports,
                ('subprocess',),
                ('check_output', 'run'),
            )
    ):
        stdout_idx = None
        stderr_idx = None
        universal_newlines_idx = None
        skip_universal_newlines_rewrite = False
        for n, keyword in enumerate(node.keywords):
            if keyword.arg == 'stdout' and is_name_attr(
                keyword.value,
                state.from_imports,
                ('subprocess',),
                ('PIPE',),
            ):
                stdout_idx = n
            elif keyword.arg == 'stderr' and is_name_attr(
                keyword.value,
                state.from_imports,
                ('subprocess',),
                ('PIPE',),
            ):
                stderr_idx = n
            elif keyword.arg == 'universal_newlines':
                universal_newlines_idx = n
            elif keyword.arg == 'text' or keyword.arg is None:
                skip_universal_newlines_rewrite = True
        if (
                universal_newlines_idx is not None and
                not skip_universal_newlines_rewrite
        ):
            func = functools.partial(
                _replace_universal_newlines_with_text,
                arg_idx=len(node.args) + universal_newlines_idx,
            )
            yield ast_to_offset(node), func
        if stdout_idx is not None and stderr_idx is not None:
            func = functools.partial(
                _use_capture_output,
                stdout_arg_idx=len(node.args) + stdout_idx,
                stderr_arg_idx=len(node.args) + stderr_idx,
            )
            yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/type_of_primitive.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_closing_bracket
from pyupgrade._token_helpers import find_op

_TYPES = {
    bool: 'bool',
    bytes: 'bytes',
    str: 'str',
    int: 'int',
    float: 'float',
    complex: 'complex',
}


def _rewrite_type_of_primitive(
        i: int,
        tokens: list[Token],
        *,
        src: str,
) -> None:
    open_paren = find_op(tokens, i + 1, '(')
    j = find_closing_bracket(tokens, open_paren)
    tokens[i] = tokens[i]._replace(src=src)
    del tokens[i + 1:j + 1]


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.func, ast.Name) and
            node.func.id == 'type' and
            len(node.args) == 1 and
            isinstance(node.args[0], ast.Constant) and
            node.args[0].value not in {Ellipsis, None}
    ):
        func = functools.partial(
            _rewrite_type_of_primitive,
            src=_TYPES[type(node.args[0].value)],
        )
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/typing_classes.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token
from tokenize_rt import UNIMPORTANT_WS

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import KEYWORDS


def _unparse(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return ''.join((_unparse(node.value), '.', node.attr))
    elif isinstance(node, ast.Subscript):
        if isinstance(node.slice, ast.Tuple):
            if len(node.slice.elts) == 1:
                slice_s = f'{_unparse(node.slice.elts[0])},'
            else:
                slice_s = ', '.join(_unparse(elt) for elt in node.slice.elts)
        else:
            slice_s = _unparse(node.slice)
        return f'{_unparse(node.value)}[{slice_s}]'
    elif (
            isinstance(node, ast.Constant) and
            isinstance(node.value, (str, bytes))
    ):
        return repr(node.value)
    elif isinstance(node, ast.Constant) and node.value is Ellipsis:
        return '...'
    elif isinstance(node, ast.List):
        return '[{}]'.format(', '.join(_unparse(elt) for elt in node.elts))
    elif isinstance(node, ast.Constant) and node.value in {True, False, None}:
        return repr(node.value)
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return f'{_unparse(node.left)} | {_unparse(node.right)}'
    else:
        raise NotImplementedError(ast.dump(node))


def _typed_class_replacement(
        tokens: list[Token],
        i: int,
        call: ast.Call,
        types: dict[str, ast.expr],
) -> tuple[int, str]:
    while i > 0 and tokens[i - 1].name == 'DEDENT':
        i -= 1
    if i > 0 and tokens[i - 1].name in {'INDENT', UNIMPORTANT_WS}:
        indent = f'{tokens[i - 1].src}{" " * 4}'
    else:
        indent = ' ' * 4

    # NT = NamedTuple("nt", [("a", int)])
    # ^i                                 ^end
    end = i + 1
    comments = []
    while end < len(tokens) and tokens[end].name != 'NEWLINE':
        token = tokens[end]
        if token.name == 'COMMENT':
            comments.append(token)
        end += 1

    parts = []
    for k, v in types.items():
        while comments and (v.lineno, v.col_offset) > comments[0].offset:
            comment = comments.pop(0)
            parts.append(f'{indent}{comment.src}')

        member = f'{indent}{k}: {_unparse(v)}'

        if comments and v.lineno == comments[0].line:
            comment = comments.pop(0)
            member += f'  {comment.src}'

        parts.append(member)

    parts.extend(f'{indent}{x.src}' for x in comments)

    attrs = '\n'.join(parts)
    return end, attrs


def _fix_named_tuple(i: int, tokens: list[Token], *, call: ast.Call) -> None:
    types = {
        tup.elts[0].value: tup.elts[1]
        for tup in call.args[1].elts  # type: ignore  # (checked below)
    }
    end, attrs = _typed_class_replacement(tokens, i, call, types)
    src = f'class {tokens[i].src}({_unparse(call.func)}):\n{attrs}'
    tokens[i:end] = [Token('CODE', src)]


def _fix_kw_typed_dict(i: int, tokens: list[Token], *, call: ast.Call) -> None:
    types = {
        arg.arg: arg.value
        for arg in call.keywords
        if arg.arg is not None
    }
    end, attrs = _typed_class_replacement(tokens, i, call, types)
    src = f'class {tokens[i].src}({_unparse(call.func)}):\n{attrs}'
    tokens[i:end] = [Token('CODE', src)]


def _fix_dict_typed_dict(
        i: int,
        tokens: list[Token],
        *,
        call: ast.Call,
) -> None:
    types = {
        k.value: v
        for k, v in zip(
            call.args[1].keys,  # type: ignore  # (checked below)
            call.args[1].values,  # type: ignore  # (checked below)
        )
    }
    if call.keywords:
        total = call.keywords[0].value.value  # type: ignore # (checked below)  # noqa: E501
        end, attrs = _typed_class_replacement(tokens, i, call, types)
        src = (
            f'class {tokens[i].src}('
            f'{_unparse(call.func)}, total={total}'
            f'):\n'
            f'{attrs}'
        )
        tokens[i:end] = [Token('CODE', src)]
    else:
        end, attrs = _typed_class_replacement(tokens, i, call, types)
        src = f'class {tokens[i].src}({_unparse(call.func)}):\n{attrs}'
        tokens[i:end] = [Token('CODE', src)]


@register(ast.Assign)
def visit_Assign(
        state: State,
        node: ast.Assign,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if state.settings.min_version < (3, 6):
        return

    if (
            # NT = ...("NT", ...)
            len(node.targets) == 1 and
            isinstance(node.targets[0], ast.Name) and
            isinstance(node.value, ast.Call) and
            len(node.value.args) >= 1 and
            isinstance(node.value.args[0], ast.Constant) and
            isinstance(node.value.args[0].value, str) and
            node.targets[0].id == node.value.args[0].value and
            not has_starargs(node.value)
    ):
        if (
                is_name_attr(
                    node.value.func,
                    state.from_imports,
                    ('typing',),
                    ('NamedTuple',),
                ) and
                len(node.value.args) == 2 and
                not node.value.keywords and
                isinstance(node.value.args[1], (ast.List, ast.Tuple)) and
                len(node.value.args[1].elts) > 0 and
                all(
                    isinstance(tup, ast.Tuple) and
                    len(tup.elts) == 2 and
                    isinstance(tup.elts[0], ast.Constant) and
                    isinstance(tup.elts[0].value, str) and
                    tup.elts[0].value.isidentifier() and
                    tup.elts[0].value not in KEYWORDS
                    for tup in node.value.args[1].elts
                )
        ):
            func = functools.partial(_fix_named_tuple, call=node.value)
            yield ast_to_offset(node), func
        elif (
                is_name_attr(
                    node.value.func,
                    state.from_imports,
                    ('typing', 'typing_extensions'),
                    ('TypedDict',),
                ) and
                len(node.value.args) == 1 and
                len(node.value.keywords) > 0 and
                not any(
                    keyword.arg == 'total'
                    for keyword in node.value.keywords
                )
        ):
            func = functools.partial(_fix_kw_typed_dict, call=node.value)
            yield ast_to_offset(node), func
        elif (
                is_name_attr(
                    node.value.func,
                    state.from_imports,
                    ('typing', 'typing_extensions'),
                    ('TypedDict',),
                ) and
                len(node.value.args) == 2 and
                (
                    not node.value.keywords or
                    (
                        len(node.value.keywords) == 1 and
                        node.value.keywords[0].arg == 'total' and
                        isinstance(node.value.keywords[0].value, ast.Constant)
                    )
                ) and
                isinstance(node.value.args[1], ast.Dict) and
                node.value.args[1].keys and
                all(
                    isinstance(k, ast.Constant) and
                    isinstance(k.value, str) and
                    k.value.isidentifier() and
                    k.value not in KEYWORDS
                    for k in node.value.args[1].keys
                )
        ):
            func = functools.partial(_fix_dict_typed_dict, call=node.value)
            yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/typing_pep563.py`
```python
from __future__ import annotations

import ast
import functools
import sys
from collections.abc import Iterable
from collections.abc import Sequence

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import Token
from pyupgrade._data import TokenFunc


def _supported_version(state: State) -> bool:
    return (
        state.settings.min_version >= (3, 14) or
        'annotations' in state.from_imports['__future__']
    )


def _dequote(i: int, tokens: list[Token], *, new: str) -> None:
    end = i + 1
    for j in range(end, len(tokens)):
        if tokens[j].name == 'STRING':
            end = j + 1
        elif tokens[j].name not in NON_CODING_TOKENS:
            break
    else:
        raise AssertionError('past end?')
    tokens[i:end] = [tokens[i]._replace(src=new)]


def _get_name(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return node.attr
    else:
        raise AssertionError(f'expected Name or Attribute: {ast.dump(node)}')


def _get_keyword_value(
        keywords: list[ast.keyword],
        keyword: str,
) -> ast.expr | None:
    for kw in keywords:
        if kw.arg == keyword:
            return kw.value
    else:
        return None


def _process_call(node: ast.Call) -> Iterable[ast.AST]:
    name = _get_name(node.func)
    args = node.args
    keywords = node.keywords
    if name == 'TypedDict':
        if keywords:
            for keyword in keywords:
                yield keyword.value
        elif len(args) != 2:  # garbage
            pass
        elif isinstance(args[1], ast.Dict):
            yield from args[1].values
        else:
            raise AssertionError(f'expected ast.Dict: {ast.dump(args[1])}')
    elif name == 'NamedTuple':
        if len(args) == 2:
            fields: ast.expr | None = args[1]
        elif keywords:
            fields = _get_keyword_value(keywords, 'fields')
        else:  # garbage
            fields = None

        if isinstance(fields, ast.List):
            for elt in fields.elts:
                if isinstance(elt, ast.Tuple) and len(elt.elts) == 2:
                    yield elt.elts[1]
        elif fields is not None:
            raise AssertionError(f'expected ast.List: {ast.dump(fields)}')
    elif name in {
        'Arg',
        'DefaultArg',
        'NamedArg',
        'DefaultNamedArg',
        'VarArg',
        'KwArg',
    }:
        if args:
            yield args[0]
        else:
            keyword_value = _get_keyword_value(keywords, 'type')
            if keyword_value is not None:
                yield keyword_value


def _process_subscript(node: ast.Subscript) -> Iterable[ast.AST]:
    name = _get_name(node.value)
    if name == 'Annotated':
        if isinstance(node.slice, ast.Tuple) and node.slice.elts:
            yield node.slice.elts[0]
    elif name != 'Literal':
        yield node.slice


def _replace_string_literal(
        annotation: ast.expr,
) -> Iterable[tuple[Offset, TokenFunc]]:
    nodes: list[ast.AST] = [annotation]
    while nodes:
        node = nodes.pop()
        if isinstance(node, ast.Call):
            nodes.extend(_process_call(node))
        elif isinstance(node, ast.Subscript):
            nodes.extend(_process_subscript(node))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            func = functools.partial(_dequote, new=node.value)
            yield ast_to_offset(node), func
        else:
            for name in node._fields:
                value = getattr(node, name)
                if isinstance(value, ast.AST):
                    nodes.append(value)
                elif isinstance(value, list):
                    nodes.extend(value)


def _process_args(
        args: Sequence[ast.arg | None],
) -> Iterable[tuple[Offset, TokenFunc]]:
    for arg in args:
        if arg is not None and arg.annotation is not None:
            yield from _replace_string_literal(arg.annotation)


def _visit_func(
        state: State,
        node: ast.AsyncFunctionDef | ast.FunctionDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if not _supported_version(state):
        return

    yield from _process_args([node.args.vararg, node.args.kwarg])
    yield from _process_args(node.args.args)
    yield from _process_args(node.args.kwonlyargs)
    yield from _process_args(node.args.posonlyargs)
    if node.returns is not None:
        yield from _replace_string_literal(node.returns)


register(ast.AsyncFunctionDef)(_visit_func)
register(ast.FunctionDef)(_visit_func)


@register(ast.AnnAssign)
def visit_AnnAssign(
        state: State,
        node: ast.AnnAssign,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if not _supported_version(state):
        return
    yield from _replace_string_literal(node.annotation)


if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
    @register(ast.TypeVar)
    def visit_TypeVar(
            state: State,
            node: ast.TypeVar,
            parent: ast.AST,
    ) -> Iterable[tuple[Offset, TokenFunc]]:
        if node.bound is not None:
            yield from _replace_string_literal(node.bound)
```

## File: `pyupgrade/_plugins/typing_pep585.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import replace_name

PEP585_BUILTINS = frozenset((
    'Dict', 'FrozenSet', 'List', 'Set', 'Tuple', 'Type',
))


def _should_rewrite(state: State) -> bool:
    return (
        state.settings.min_version >= (3, 9) or (
            not state.settings.keep_runtime_typing and
            state.in_annotation and
            'annotations' in state.from_imports['__future__']
        )
    )


@register(ast.Attribute)
def visit_Attribute(
        state: State,
        node: ast.Attribute,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            _should_rewrite(state) and
            isinstance(node.value, ast.Name) and
            node.value.id == 'typing' and
            node.attr in PEP585_BUILTINS
    ):
        func = functools.partial(
            replace_name,
            name=node.attr,
            new=node.attr.lower(),
        )
        yield ast_to_offset(node), func


@register(ast.Name)
def visit_Name(
        state: State,
        node: ast.Name,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            _should_rewrite(state) and
            node.id in state.from_imports['typing'] and
            node.id in PEP585_BUILTINS
    ):
        func = functools.partial(
            replace_name,
            name=node.id,
            new=node.id.lower(),
        )
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/typing_pep604.py`
```python
from __future__ import annotations

import ast
import functools
import sys
from collections.abc import Iterable

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_closing_bracket
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import is_close
from pyupgrade._token_helpers import is_open


def _fix_optional(i: int, tokens: list[Token]) -> None:
    j = find_op(tokens, i, '[')
    k = find_closing_bracket(tokens, j)
    if tokens[j].line == tokens[k].line:
        tokens[k] = Token('CODE', ' | None')
        del tokens[i:j + 1]
    else:
        tokens[j] = tokens[j]._replace(src='(')
        tokens[k] = tokens[k]._replace(src=')')
        tokens[i:j] = [Token('CODE', 'None | ')]


def _fix_union(
        i: int,
        tokens: list[Token],
        *,
        arg_count: int,
) -> None:
    depth = 1
    parens_done = []
    open_parens = []
    commas = []
    coding_depth = None

    j = find_op(tokens, i, '[')
    k = j + 1
    while depth:
        # it's possible our first coding token is a close paren
        # so make sure this is separate from the if chain below
        if (
                tokens[k].name not in NON_CODING_TOKENS and
                tokens[k].src != '(' and
                coding_depth is None
        ):
            if tokens[k].src == ')':  # the coding token was an empty tuple
                coding_depth = depth - 1
            else:
                coding_depth = depth

        if is_open(tokens[k]):
            if tokens[k].src == '(':
                open_parens.append((depth, k))

            depth += 1
        elif is_close(tokens[k]):
            if tokens[k].src == ')':
                paren_depth, open_paren = open_parens.pop()
                parens_done.append((paren_depth, (open_paren, k)))

            depth -= 1
        elif tokens[k].src == ',':
            commas.append((depth, k))

        k += 1
    k -= 1

    assert coding_depth is not None
    assert not open_parens, open_parens
    comma_depth = min((depth for depth, _ in commas), default=sys.maxsize)
    min_depth = min(comma_depth, coding_depth)

    to_delete = [
        paren
        for depth, positions in parens_done
        if depth < min_depth
        for paren in positions
    ]

    if comma_depth <= coding_depth:
        comma_positions = [k for depth, k in commas if depth == comma_depth]
        if len(comma_positions) == arg_count:
            to_delete.append(comma_positions.pop())
    else:
        comma_positions = []

    to_delete.sort()

    if tokens[j].line == tokens[k].line:
        del tokens[k]
        for comma in comma_positions:
            tokens[comma] = Token('CODE', ' |')
        for paren in reversed(to_delete):
            del tokens[paren]
        del tokens[i:j + 1]
    else:
        tokens[j] = tokens[j]._replace(src='(')
        tokens[k] = tokens[k]._replace(src=')')

        for comma in comma_positions:
            tokens[comma] = Token('CODE', ' |')
        for paren in reversed(to_delete):
            del tokens[paren]
        del tokens[i:j]


def _supported_version(state: State) -> bool:
    return (
        state.in_annotation and (
            state.settings.min_version >= (3, 10) or (
                not state.settings.keep_runtime_typing and
                'annotations' in state.from_imports['__future__']
            )
        )
    )


def _any_arg_is_str(node_slice: ast.expr) -> bool:
    return (
        (
            isinstance(node_slice, ast.Constant) and
            isinstance(node_slice.value, str)
        ) or (
            isinstance(node_slice, ast.Tuple) and
            any(
                isinstance(elt, ast.Constant) and
                isinstance(elt.value, str)
                for elt in node_slice.elts
            )
        )
    )


@register(ast.Subscript)
def visit_Subscript(
        state: State,
        node: ast.Subscript,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if not _supported_version(state):
        return

    # don't rewrite forward annotations (unless we know they will be dequoted)
    if 'annotations' not in state.from_imports['__future__']:
        if _any_arg_is_str(node.slice):
            return

    if is_name_attr(
            node.value,
            state.from_imports,
            ('typing',),
            ('Optional',),
    ):
        yield ast_to_offset(node), _fix_optional
    elif is_name_attr(node.value, state.from_imports, ('typing',), ('Union',)):
        if isinstance(node.slice, ast.Slice):  # not a valid annotation
            return

        if isinstance(node.slice, ast.Tuple):
            if node.slice.elts:
                arg_count = len(node.slice.elts)
            else:
                return  # empty Union
        else:
            arg_count = 1

        func = functools.partial(_fix_union, arg_count=arg_count)
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/typing_pep646_unpack.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_closing_bracket
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import remove_brace


def _replace_unpack_with_star(i: int, tokens: list[Token]) -> None:
    start = find_op(tokens, i, '[')
    end = find_closing_bracket(tokens, start)

    remove_brace(tokens, end)
    # replace `Unpack` with `*`
    tokens[i:start + 1] = [tokens[i]._replace(name='OP', src='*')]


@register(ast.Subscript)
def visit_Subscript(
    state: State,
    node: ast.Subscript,
    parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if state.settings.min_version < (3, 11):
        return

    if is_name_attr(node.value, state.from_imports, ('typing',), ('Unpack',)):
        if isinstance(parent, ast.Subscript):
            yield ast_to_offset(node.value), _replace_unpack_with_star


def _visit_func(
        state: State,
        node: ast.AsyncFunctionDef | ast.FunctionDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if state.settings.min_version < (3, 11):
        return

    vararg = node.args.vararg
    if (
            vararg is not None and
            isinstance(vararg.annotation, ast.Subscript) and
            is_name_attr(
                vararg.annotation.value,
                state.from_imports,
                ('typing',), ('Unpack',),
            )
    ):
        yield ast_to_offset(vararg.annotation.value), _replace_unpack_with_star


@register(ast.AsyncFunctionDef)
def visit_AsyncFunctionDef(
        state: State,
        node: ast.AsyncFunctionDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    yield from _visit_func(state, node, parent)


@register(ast.FunctionDef)
def visit_FunctionDef(
        state: State,
        node: ast.FunctionDef,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    yield from _visit_func(state, node, parent)
```

## File: `pyupgrade/_plugins/typing_pep696_typevar_defaults.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_op
from pyupgrade._token_helpers import parse_call_args


def _fix_typevar_default(i: int, tokens: list[Token]) -> None:
    j = find_op(tokens, i, '[')
    args, end = parse_call_args(tokens, j)
    # remove the trailing `None` arguments
    del tokens[args[0][1]:args[-1][1]]


def _should_rewrite(state: State) -> bool:
    return (
        state.settings.min_version >= (3, 13) or (
            not state.settings.keep_runtime_typing and
            state.in_annotation and
            'annotations' in state.from_imports['__future__']
        )
    )


def _is_none(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and node.value is None


@register(ast.Subscript)
def visit_Subscript(
        state: State,
        node: ast.Subscript,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if not _should_rewrite(state):
        return

    if (
            is_name_attr(
                node.value,
                state.from_imports,
                ('collections.abc', 'typing', 'typing_extensions'),
                ('Generator',),
            ) and
            isinstance(node.slice, ast.Tuple) and
            len(node.slice.elts) == 3 and
            _is_none(node.slice.elts[1]) and
            _is_none(node.slice.elts[2])
    ):
        yield ast_to_offset(node), _fix_typevar_default
    elif (
            is_name_attr(
                node.value,
                state.from_imports,
                ('collections.abc', 'typing', 'typing_extensions'),
                ('AsyncGenerator',),
            ) and
            isinstance(node.slice, ast.Tuple) and
            len(node.slice.elts) == 2 and
            _is_none(node.slice.elts[1])
    ):
        yield ast_to_offset(node), _fix_typevar_default
```

## File: `pyupgrade/_plugins/typing_text.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import replace_name


@register(ast.Attribute)
def visit_Attribute(
        state: State,
        node: ast.Attribute,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.value, ast.Name) and
            node.value.id == 'typing' and
            node.attr == 'Text'
    ):
        func = functools.partial(replace_name, name=node.attr, new='str')
        yield ast_to_offset(node), func


@register(ast.Name)
def visit_Name(
        state: State,
        node: ast.Name,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if node.id in state.from_imports['typing'] and node.id == 'Text':
        func = functools.partial(replace_name, name=node.id, new='str')
        yield ast_to_offset(node), func
```

## File: `pyupgrade/_plugins/unittest_aliases.py`
```python
from __future__ import annotations

import ast
import functools
from collections.abc import Iterable

from tokenize_rt import Offset

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import has_starargs
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import replace_name

METHOD_MAPPING = {
    'assertEquals': 'assertEqual',
    'failUnlessEqual': 'assertEqual',
    'failIfEqual': 'assertNotEqual',
    'failUnless': 'assertTrue',
    'assert_': 'assertTrue',
    'failIf': 'assertFalse',
    'failUnlessRaises': 'assertRaises',
    'failUnlessAlmostEqual': 'assertAlmostEqual',
    'failIfAlmostEqual': 'assertNotAlmostEqual',
    'assertNotEquals': 'assertNotEqual',
    'assertAlmostEquals': 'assertAlmostEqual',
    'assertNotAlmostEquals': 'assertNotAlmostEqual',
    'assertRegexpMatches': 'assertRegex',
    'assertNotRegexpMatches': 'assertNotRegex',
    'assertRaisesRegexp': 'assertRaisesRegex',
}

FUNCTION_MAPPING = {
    'findTestCases': 'defaultTestLoader.loadTestsFromModule',
    'makeSuite': 'defaultTestLoader.loadTestsFromTestCase',
    'getTestCaseNames': 'defaultTestLoader.getTestCaseNames',
}


@register(ast.Call)
def visit_Call(
        state: State,
        node: ast.Call,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'self' and
            node.func.attr in METHOD_MAPPING
    ):
        func = functools.partial(
            replace_name,
            name=node.func.attr,
            new=f'self.{METHOD_MAPPING[node.func.attr]}',
        )
        yield ast_to_offset(node.func), func
    elif (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'unittest' and
            node.func.attr in FUNCTION_MAPPING and
            not has_starargs(node) and
            not node.keywords and
            len(node.args) == 1
    ):
        func = functools.partial(
            replace_name,
            name=node.func.attr,
            new=f'unittest.{FUNCTION_MAPPING[node.func.attr]}',
        )
        yield ast_to_offset(node.func), func
```

## File: `pyupgrade/_plugins/unpack_list_comprehension.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_async_listcomp
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import find_closing_bracket


def _replace_list_comprehension(i: int, tokens: list[Token]) -> None:
    start = i
    end = find_closing_bracket(tokens, start)
    tokens[start] = tokens[start]._replace(src='(')
    tokens[end] = tokens[end]._replace(src=')')


@register(ast.Assign)
def visit_Assign(
        state: State,
        node: ast.Assign,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:
    if (
            len(node.targets) == 1 and
            isinstance(node.targets[0], ast.Tuple) and
            isinstance(node.value, ast.ListComp) and
            not is_async_listcomp(node.value)
    ):
        yield ast_to_offset(node.value), _replace_list_comprehension
```

## File: `pyupgrade/_plugins/versioned_branches.py`
```python
from __future__ import annotations

import ast
from collections.abc import Iterable
from typing import cast

from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._data import Version
from pyupgrade._token_helpers import Block


def _find_if_else_block(tokens: list[Token], i: int) -> tuple[Block, Block]:
    if_block = Block.find(tokens, i)
    i = if_block.end
    while tokens[i].src != 'else':
        i += 1
    else_block = Block.find(tokens, i, trim_end=True)
    return if_block, else_block


def _fix_py3_block(i: int, tokens: list[Token]) -> None:
    if tokens[i].src == 'if':
        if_block = Block.find(tokens, i)
        if_block.dedent(tokens)
        del tokens[if_block.start:if_block.block]
    else:
        if_block = Block.find(tokens, i)
        if_block.replace_condition(tokens, [Token('NAME', 'else')])


def _fix_py2_block(i: int, tokens: list[Token]) -> None:
    if tokens[i].src == 'if':
        if_block, else_block = _find_if_else_block(tokens, i)
        else_block.dedent(tokens)
        del tokens[if_block.start:else_block.block]
    else:
        if_block, else_block = _find_if_else_block(tokens, i)
        del tokens[if_block.start:else_block.start]


def _fix_remove_block(i: int, tokens: list[Token]) -> None:
    block = Block.find(tokens, i)
    del tokens[block.start:block.end]


def _fix_py2_convert_elif(i: int, tokens: list[Token]) -> None:
    if_block = Block.find(tokens, i)
    # wasn't actually followed by an `elif`
    if tokens[if_block.end].src != 'elif':
        return
    tokens[if_block.end] = Token('CODE', tokens[i].src)
    _fix_remove_block(i, tokens)


def _fix_py3_block_else(i: int, tokens: list[Token]) -> None:
    if tokens[i].src == 'if':
        if_block, else_block = _find_if_else_block(tokens, i)
        if_block.dedent(tokens)
        del tokens[if_block.end:else_block.end]
        del tokens[if_block.start:if_block.block]
    else:
        if_block, else_block = _find_if_else_block(tokens, i)
        del tokens[if_block.end:else_block.end]
        if_block.replace_condition(tokens, [Token('NAME', 'else')])


def _fix_py3_convert_elif(i: int, tokens: list[Token]) -> None:
    if_block = Block.find(tokens, i)
    # wasn't actually followed by an `elif`
    if tokens[if_block.end].src != 'elif':
        return
    tokens[if_block.end] = Token('CODE', tokens[i].src)
    if_block.dedent(tokens)
    del tokens[if_block.start:if_block.block]


def _eq(test: ast.Compare, n: int) -> bool:
    return _cmp(test, ast.Eq, n)


def _lt(test: ast.Compare, n: int) -> bool:
    return _cmp(test, ast.Lt, n)


def _gte(test: ast.Compare, n: int) -> bool:
    return _cmp(test, ast.GtE, n)


def _cmp(test: ast.Compare, op: type[ast.cmpop], n: int) -> bool:
    return (
        isinstance(test.ops[0], op) and
        isinstance(test.comparators[0], ast.Constant) and
        test.comparators[0].value == n
    )


def _compare_to_3(
    test: ast.Compare,
    op: type[ast.cmpop] | tuple[type[ast.cmpop], ...],
    minor: int = 0,
) -> bool:
    if not (
            isinstance(test.ops[0], op) and
            isinstance(test.comparators[0], ast.Tuple) and
            len(test.comparators[0].elts) >= 1 and
            all(
                isinstance(n, ast.Constant) and isinstance(n.value, int)
                for n in test.comparators[0].elts
            )
    ):
        return False

    # checked above but mypy needs help
    ast_elts = cast('list[ast.Constant]', test.comparators[0].elts)
    # padding a 0 for compatibility with (3,) used as a spec
    elts = tuple(e.value for e in ast_elts) + (0,)

    return elts[:2] == (3, minor) and all(n == 0 for n in elts[2:])


@register(ast.If)
def visit_If(
        state: State,
        node: ast.If,
        parent: ast.AST,
) -> Iterable[tuple[Offset, TokenFunc]]:

    min_version: Version
    if state.settings.min_version == (3,):
        min_version = (3, 0)
    else:
        min_version = state.settings.min_version
    assert len(min_version) >= 2

    if (
            # if six.PY2:
            is_name_attr(
                node.test,
                state.from_imports,
                ('six',),
                ('PY2',),
            ) or
            # if not six.PY3:
            (
                isinstance(node.test, ast.UnaryOp) and
                isinstance(node.test.op, ast.Not) and
                is_name_attr(
                    node.test.operand,
                    state.from_imports,
                    ('six',),
                    ('PY3',),
                )
            ) or
            # sys.version_info == 2 or < (3,)
            # or < (3, n) or <= (3, n) (with n<m)
            (
                isinstance(node.test, ast.Compare) and
                is_name_attr(
                    node.test.left,
                    state.from_imports,
                    ('sys',),
                    ('version_info',),
                ) and
                len(node.test.ops) == 1 and (
                    _eq(node.test, 2) or
                    _compare_to_3(node.test, ast.Lt, min_version[1]) or
                    any(
                        _compare_to_3(node.test, (ast.Lt, ast.LtE), minor)
                        for minor in range(min_version[1])
                    )
                )
            ) or
            # sys.version_info[0] == 2 or < 3
            # sys.version_info.major == 2 or < 3
            (
                isinstance(node.test, ast.Compare) and
                (
                    (
                        isinstance(node.test.left, ast.Subscript) and
                        isinstance(node.test.left.slice, ast.Constant) and
                        node.test.left.slice.value == 0
                    ) or
                    (
                        isinstance(node.test.left, ast.Attribute) and
                        node.test.left.attr == 'major'
                    )
                ) and
                is_name_attr(
                    node.test.left.value,
                    state.from_imports,
                    ('sys',),
                    ('version_info',),
                ) and
                len(node.test.ops) == 1 and
                (
                    _eq(node.test, 2) or
                    _lt(node.test, 3)
                )
            )
    ):
        if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            yield ast_to_offset(node), _fix_py2_convert_elif
        elif node.orelse:
            yield ast_to_offset(node), _fix_py2_block
        elif node.col_offset == 0:
            yield ast_to_offset(node), _fix_remove_block
    elif (
            # if six.PY3:
            is_name_attr(
                node.test,
                state.from_imports,
                ('six',),
                ('PY3',),
            ) or
            # if not six.PY2:
            (
                isinstance(node.test, ast.UnaryOp) and
                isinstance(node.test.op, ast.Not) and
                is_name_attr(
                    node.test.operand,
                    state.from_imports,
                    ('six',),
                    ('PY2',),
                )
            ) or
            # sys.version_info == 3 or >= (3,) or > (3,)
            # sys.version_info >= (3, n) (with n<=m)
            # or sys.version_info > (3, n) (with n<m)
            (
                isinstance(node.test, ast.Compare) and
                is_name_attr(
                    node.test.left,
                    state.from_imports,
                    ('sys',),
                    ('version_info',),
                ) and
                len(node.test.ops) == 1 and (
                    _eq(node.test, 3) or
                    _compare_to_3(node.test, (ast.Gt, ast.GtE)) or
                    _compare_to_3(node.test, ast.GtE, min_version[1]) or
                    any(
                        _compare_to_3(node.test, (ast.Gt, ast.GtE), minor)
                        for minor in range(min_version[1])
                    )
                )
            ) or
            # sys.version_info[0] == 3 or >= 3
            # sys.version_info.major == 3 or >= 3
            (
                isinstance(node.test, ast.Compare) and
                (
                    (
                        isinstance(node.test.left, ast.Subscript) and
                        isinstance(node.test.left.slice, ast.Constant) and
                        node.test.left.slice.value == 0
                    ) or
                    (
                        isinstance(node.test.left, ast.Attribute) and
                        node.test.left.attr == 'major'
                    )
                ) and
                is_name_attr(
                    node.test.left.value,
                    state.from_imports,
                    ('sys',),
                    ('version_info',),
                ) and
                len(node.test.ops) == 1 and
                (
                    _eq(node.test, 3) or
                    _gte(node.test, 3)
                )
            )
    ):
        if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            yield ast_to_offset(node), _fix_py3_convert_elif
        elif node.orelse:
            yield ast_to_offset(node), _fix_py3_block_else
        else:
            yield ast_to_offset(node), _fix_py3_block
```

## File: `testing/generate-imports`
```
#!/usr/bin/env python3
from __future__ import annotations

import collections
import importlib.metadata
import os.path
import re
import sys

import reorder_python_imports

FROM_IMPORT_RE = re.compile(r'^from ([^ ]+) import (.*)$')
REPLACE_RE = re.compile(r'^([^=]+)=([^:]+)(?::(.*))?$')


def _set_inline(v: set[str]) -> str:
    return f'{{{", ".join(repr(s) for s in sorted(v))}}}'


def _dict_set_inline(ver: tuple[int, ...], dct: dict[str, set[str]]) -> str:
    items_s = ', '.join(f'{k!r}: {_set_inline(v)}' for k, v in dct.items())
    return f'    {ver!r}: {{{items_s}}},'


def _set_fit(v: set[str]) -> str:
    ret = ''

    vals = sorted(v)
    pending = f'{" " * 12}{vals[0]!r},'

    for s in vals[1:]:
        if len(pending) + len(repr(s)) + 2 < 80:
            pending += f' {s!r},'
        else:
            ret += f'{pending}\n'
            pending = f'{" " * 12}{s!r},'

    ret += f'{pending}\n'

    return f'{{\n{ret}{" " * 8}}}'


def _removals() -> dict[tuple[int, ...], dict[str, set[str]]]:
    removals: dict[tuple[int, ...], dict[str, set[str]]]
    removals = collections.defaultdict(lambda: collections.defaultdict(set))
    for k, v in reorder_python_imports.REMOVALS.items():
        if k <= (3, 6):
            k = (3,)
        for s in v:
            match = FROM_IMPORT_RE.match(s)
            assert match is not None
            removals[k][match[1]].add(match[2])
    return removals


def _replacements() -> tuple[
    dict[tuple[int, ...], dict[tuple[str, str], str]],
    dict[str, str],
]:
    exact: dict[tuple[int, ...], dict[tuple[str, str], str]]
    exact = collections.defaultdict(dict)
    mods = {}

    for ver, vals in reorder_python_imports.REPLACES.items():
        replaces = reorder_python_imports.Replacements.make([
            reorder_python_imports._validate_replace_import(s)
            for s in vals
            if 'mock' not in s
        ])
        if replaces.exact:
            exact[ver].update(replaces.exact)
        if replaces.mods:
            mods.update(replaces.mods)

    return exact, mods


def main() -> int:
    version = importlib.metadata.version('reorder-python-imports')

    exact, mods = _replacements()

    print(f'# GENERATED VIA {os.path.basename(sys.argv[0])}')
    print(f'# Using reorder-python-imports=={version}')
    print('REMOVALS = {')
    for ver, dct in sorted(_removals().items()):
        dct_inline = _dict_set_inline(ver, dct)
        if len(dct_inline) < 80:
            print(dct_inline)
        else:
            print(f'    {ver!r}: {{')
            for k, v in sorted(dct.items()):
                set_line = f'        {k!r}: {_set_inline(v)},'
                if len(set_line) < 80:
                    print(set_line)
                else:
                    print(f'        {k!r}: {_set_fit(v)},')
            print('    },')
    print('}')
    print("REMOVALS[(3,)]['six.moves.builtins'] = REMOVALS[(3,)]['builtins']")
    print('REPLACE_EXACT = {')
    for ver, replaces in sorted(exact.items()):
        print(f'    {ver}: {{')
        for replace_k, replace_v in sorted(replaces.items()):
            print(f'        {replace_k}: {replace_v!r},')
        print('    },')
    print('}')
    print('REPLACE_MODS = {')
    for mod_from, mod_to in sorted(mods.items()):
        print(f'    {mod_from!r}: {mod_to!r},')
    print('}')
    print('# END GENERATED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `tests/main_test.py`
```python
from __future__ import annotations

import io
import re
import sys
from unittest import mock

import pytest

from pyupgrade._main import main


def test_main_trivial():
    assert main(()) == 0


def test_main_noop(tmpdir, capsys):
    with pytest.raises(SystemExit):
        main(('--help',))
    out, err = capsys.readouterr()
    version_options = sorted(set(re.findall(r'--py\d+-plus', out)))

    s = '''\
from sys import version_info
x=version_info
def f():
    global x, y

f'hello snowman: \\N{SNOWMAN}'
'''
    f = tmpdir.join('f.py')
    f.write(s)

    assert main((f.strpath,)) == 0
    assert f.read() == s

    for version_option in version_options:
        assert main((f.strpath, version_option)) == 0
        assert f.read() == s


def test_main_changes_a_file(tmpdir, capsys):
    f = tmpdir.join('f.py')
    f.write('x = set((1, 2, 3))\n')
    assert main((f.strpath,)) == 1
    out, err = capsys.readouterr()
    assert err == f'Rewriting {f.strpath}\n'
    assert f.read() == 'x = {1, 2, 3}\n'


def test_main_keeps_line_endings(tmpdir, capsys):
    f = tmpdir.join('f.py')
    f.write_binary(b'x = set((1, 2, 3))\r\n')
    assert main((f.strpath,)) == 1
    assert f.read_binary() == b'x = {1, 2, 3}\r\n'


def test_main_syntax_error(tmpdir):
    f = tmpdir.join('f.py')
    f.write('from __future__ import print_function\nprint 1\n')
    assert main((f.strpath,)) == 0


def test_main_non_utf8_bytes(tmpdir, capsys):
    f = tmpdir.join('f.py')
    f.write_binary('# -*- coding: cp1252 -*-\nx = €\n'.encode('cp1252'))
    assert main((f.strpath,)) == 1
    out, _ = capsys.readouterr()
    assert out == f'{f.strpath} is non-utf-8 (not supported)\n'


def test_keep_percent_format(tmpdir):
    f = tmpdir.join('f.py')
    f.write('"%s" % (1,)')
    assert main((f.strpath, '--keep-percent-format')) == 0
    assert f.read() == '"%s" % (1,)'
    assert main((f.strpath,)) == 1
    assert f.read() == '"{}".format(1)'


def test_keep_mock(tmpdir):
    f = tmpdir.join('f.py')
    f.write('from mock import patch\n')
    assert main((f.strpath, '--keep-mock')) == 0
    assert f.read() == 'from mock import patch\n'
    assert main((f.strpath,)) == 1
    assert f.read() == 'from unittest.mock import patch\n'


def test_py3_plus_argument_unicode_literals(tmpdir):
    f = tmpdir.join('f.py')
    f.write('u""')
    assert main((f.strpath,)) == 1
    assert f.read() == '""'


def test_py3_plus_super(tmpdir):
    f = tmpdir.join('f.py')
    f.write(
        'class C(Base):\n'
        '    def f(self):\n'
        '        super(C, self).f()\n',
    )
    assert main((f.strpath,)) == 1
    assert f.read() == (
        'class C(Base):\n'
        '    def f(self):\n'
        '        super().f()\n'
    )


def test_py3_plus_new_style_classes(tmpdir):
    f = tmpdir.join('f.py')
    f.write('class C(object): pass\n')
    assert main((f.strpath,)) == 1
    assert f.read() == 'class C: pass\n'


def test_py3_plus_oserror(tmpdir):
    f = tmpdir.join('f.py')
    f.write('raise EnvironmentError(1, 2)\n')
    assert main((f.strpath,)) == 1
    assert f.read() == 'raise OSError(1, 2)\n'


def test_py36_plus_fstrings(tmpdir):
    f = tmpdir.join('f.py')
    f.write('"{} {}".format(hello, world)')
    assert main((f.strpath,)) == 0
    assert f.read() == '"{} {}".format(hello, world)'
    assert main((f.strpath, '--py36-plus')) == 1
    assert f.read() == 'f"{hello} {world}"'


def test_py37_plus_removes_annotations(tmpdir):
    f = tmpdir.join('f.py')
    f.write('from __future__ import generator_stop\nx = 1\n')
    assert main((f.strpath,)) == 0
    assert main((f.strpath, '--py36-plus')) == 0
    assert main((f.strpath, '--py37-plus')) == 1
    assert f.read() == 'x = 1\n'


def test_py38_plus_removes_no_arg_decorators(tmpdir):
    f = tmpdir.join('f.py')
    f.write(
        'import functools\n\n'
        '@functools.lru_cache()\n'
        'def expensive():\n'
        '   ...',
    )
    assert main((f.strpath,)) == 0
    assert main((f.strpath, '--py36-plus')) == 0
    assert main((f.strpath, '--py37-plus')) == 0
    assert main((f.strpath, '--py38-plus')) == 1
    assert f.read() == (
        'import functools\n\n'
        '@functools.lru_cache\n'
        'def expensive():\n'
        '   ...'
    )


def test_noop_token_error(tmpdir):
    f = tmpdir.join('f.py')
    f.write(
        # force some rewrites (ast is ok https://bugs.python.org/issue2180)
        'set(())\n'
        '"%s" % (1,)\n'
        'six.b("foo")\n'
        '"{}".format(a)\n'
        # token error
        'x = \\\n'
        '5\\\n',
    )
    assert main((f.strpath, '--py36-plus')) == 0


def test_main_exit_zero_even_if_changed(tmpdir):
    f = tmpdir.join('t.py')
    f.write('set((1, 2))\n')
    assert not main((str(f), '--exit-zero-even-if-changed'))
    assert f.read() == '{1, 2}\n'
    assert not main((str(f), '--exit-zero-even-if-changed'))


def test_main_stdin_no_changes(capsys):
    stdin = io.TextIOWrapper(io.BytesIO(b'{1, 2}\n'), 'UTF-8')
    with mock.patch.object(sys, 'stdin', stdin):
        assert main(('-',)) == 0
    out, err = capsys.readouterr()
    assert out == '{1, 2}\n'


def test_main_stdin_with_changes(capsys):
    stdin = io.TextIOWrapper(io.BytesIO(b'set((1, 2))\n'), 'UTF-8')
    with mock.patch.object(sys, 'stdin', stdin):
        assert main(('-',)) == 1
    out, err = capsys.readouterr()
    assert out == '{1, 2}\n'
```

## File: `tests/string_helpers_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._string_helpers import parse_format
from pyupgrade._string_helpers import unparse_parsed_string


@pytest.mark.parametrize(
    's',
    (
        '', 'foo', '{}', '{0}', '{named}', '{!r}', '{:>5}', '{{', '}}',
        '{0!s:15}',
    ),
)
def test_roundtrip_text(s):
    assert unparse_parsed_string(parse_format(s)) == s


def test_parse_format_starts_with_named():
    # technically not possible since our string always starts with quotes
    assert parse_format(r'\N{snowman} hi {0} hello') == [
        (r'\N{snowman} hi ', '0', '', None),
        (' hello', None, None, None),
    ]


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('{:}', '{}'),
        ('{0:}', '{0}'),
        ('{0!r:}', '{0!r}'),
    ),
)
def test_intentionally_not_round_trip(s, expected):
    # Our unparse simplifies empty parts, whereas stdlib allows them
    ret = unparse_parsed_string(parse_format(s))
    assert ret == expected
```

## File: `tests/_plugins/typing_pep604_test.py`
```python
from __future__ import annotations

import pytest
from tokenize_rt import src_to_tokens
from tokenize_rt import tokens_to_src

from pyupgrade._plugins.typing_pep604 import _fix_union


@pytest.mark.parametrize(
    ('s', 'arg_count', 'expected'),
    (
        ('Union[a, b]', 2, 'a | b'),
        ('Union[(a, b)]', 2, 'a | b'),
        ('Union[(a,)]', 1, 'a'),
        ('Union[(((a, b)))]', 2, 'a | b'),
        pytest.param('Union[((a), b)]', 2, '(a) | b', id='wat'),
        ('Union[(((a,), b))]', 2, '(a,) | b'),
        ('Union[((a,), (a, b))]', 2, '(a,) | (a, b)'),
        ('Union[((a))]', 1, 'a'),
        ('Union[a()]', 1, 'a()'),
        ('Union[a(b, c)]', 1, 'a(b, c)'),
        ('Union[(a())]', 1, 'a()'),
        ('Union[(())]', 1, '()'),
    ),
)
def test_fix_union_edge_cases(s, arg_count, expected):
    tokens = src_to_tokens(s)
    _fix_union(0, tokens, arg_count=arg_count)
    assert tokens_to_src(tokens) == expected
```

## File: `tests/features/binary_literals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        '"☃".encode("UTF-8")',
        '"\\u2603".encode("UTF-8")',
        '"\\U0001f643".encode("UTF-8")',
        '"\\N{SNOWMAN}".encode("UTF-8")',
        '"\\xa0".encode("UTF-8")',
        # not byte literal compatible
        '"y".encode("utf16")',
        # can't rewrite f-strings
        'f"{x}".encode()',
        # not a `.encode()` call
        '"foo".encode', '("foo".encode)',
        # encode, but not a literal
        'x.encode()',
        # the codec / string is an f-string
        'str.encode(f"{c}")', '"foo".encode(f"{c}")',
        pytest.param('wat.encode(b"unrelated")', id='unrelated .encode(...)'),
    ),
)
def test_binary_literals_noop(s):
    assert _fix_tokens(s) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('"foo".encode()', 'b"foo"'),
        ('"foo".encode("ascii")', 'b"foo"'),
        ('"foo".encode("utf-8")', 'b"foo"'),
        ('"\\xa0".encode("latin1")', 'b"\\xa0"'),
        (r'"\\u wot".encode()', r'b"\\u wot"'),
        (r'"\\x files".encode()', r'b"\\x files"'),
        (
            'f(\n'
            '    "foo"\n'
            '    "bar".encode()\n'
            ')\n',

            'f(\n'
            '    b"foo"\n'
            '    b"bar"\n'
            ')\n',
        ),
    ),
)
def test_binary_literals(s, expected):
    assert _fix_tokens(s) == expected
```

## File: `tests/features/capture_output_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'import subprocess\n'
            'subprocess.run(["foo"], stdout=subprocess.PIPE, '
            'stderr=subprocess.PIPE)\n',
            (3,),
            id='not Python3.7+',
        ),
        pytest.param(
            'from foo import run\n'
            'import subprocess\n'
            'run(["foo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n',
            (3, 7),
            id='run imported, but not from subprocess',
        ),
        pytest.param(
            'from foo import PIPE\n'
            'from subprocess import run\n'
            'subprocess.run(["foo"], stdout=PIPE, stderr=PIPE)\n',
            (3, 7),
            id='PIPE imported, but not from subprocess',
        ),
        pytest.param(
            'from subprocess import run\n'
            'run(["foo"], stdout=None, stderr=PIPE)\n',
            (3, 7),
            id='stdout not subprocess.PIPE',
        ),
    ),
)
def test_fix_capture_output_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import subprocess\n'
            'subprocess.run(["foo"], stdout=subprocess.PIPE, '
            'stderr=subprocess.PIPE)\n',
            'import subprocess\n'
            'subprocess.run(["foo"], capture_output=True)\n',
            id='subprocess.run and subprocess.PIPE attributes',
        ),
        pytest.param(
            'from subprocess import run, PIPE\n'
            'run(["foo"], stdout=PIPE, stderr=PIPE)\n',
            'from subprocess import run, PIPE\n'
            'run(["foo"], capture_output=True)\n',
            id='run and PIPE imported from subprocess',
        ),
        pytest.param(
            'from subprocess import run, PIPE\n'
            'run(["foo"], shell=True, stdout=PIPE, stderr=PIPE)\n',
            'from subprocess import run, PIPE\n'
            'run(["foo"], shell=True, capture_output=True)\n',
            id='other argument used too',
        ),
        pytest.param(
            'import subprocess\n'
            'subprocess.run(["foo"], stderr=subprocess.PIPE, '
            'stdout=subprocess.PIPE)\n',
            'import subprocess\n'
            'subprocess.run(["foo"], capture_output=True)\n',
            id='stderr used before stdout',
        ),
        pytest.param(
            'import subprocess\n'
            'subprocess.run(stderr=subprocess.PIPE, args=["foo"], '
            'stdout=subprocess.PIPE)\n',
            'import subprocess\n'
            'subprocess.run(args=["foo"], capture_output=True)\n',
            id='stdout is first argument',
        ),
        pytest.param(
            'import subprocess\n'
            'subprocess.run(\n'
            '    stderr=subprocess.PIPE, \n'
            '    args=["foo"], \n'
            '    stdout=subprocess.PIPE,\n'
            ')\n',
            'import subprocess\n'
            'subprocess.run(\n'
            '    args=["foo"], \n'
            '    capture_output=True,\n'
            ')\n',
            id='stdout is first argument, multiline',
        ),
        pytest.param(
            'subprocess.run(\n'
            '    "foo",\n'
            '    stdout=subprocess.PIPE,\n'
            '    stderr=subprocess.PIPE,\n'
            '    universal_newlines=True,\n'
            ')',
            'subprocess.run(\n'
            '    "foo",\n'
            '    capture_output=True,\n'
            '    text=True,\n'
            ')',
            id='both universal_newlines and capture_output rewrite',
        ),
        pytest.param(
            'subprocess.run(\n'
            '    f"{x}(",\n'
            '    stdout=subprocess.PIPE,\n'
            '    stderr=subprocess.PIPE,\n'
            ')',

            'subprocess.run(\n'
            '    f"{x}(",\n'
            '    capture_output=True,\n'
            ')',

            id='3.12: fstring with open brace',
        ),
        pytest.param(
            'subprocess.run(\n'
            '    f"{x})",\n'
            '    stdout=subprocess.PIPE,\n'
            '    stderr=subprocess.PIPE,\n'
            ')',

            'subprocess.run(\n'
            '    f"{x})",\n'
            '    capture_output=True,\n'
            ')',

            id='3.12: fstring with close brace',
        ),
    ),
)
def test_fix_capture_output(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 7)))
    assert ret == expected
```

## File: `tests/features/collections_abc_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


def test_collections_abc_noop():
    src = 'if isinstance(x, collections.defaultdict): pass\n'
    assert _fix_plugins(src, settings=Settings()) == src


@pytest.mark.parametrize(
    ('src', 'expected'),
    (
        pytest.param(
            'if isinstance(x, collections.Sized):\n'
            '    print(len(x))\n',
            'if isinstance(x, collections.abc.Sized):\n'
            '    print(len(x))\n',
            id='Attribute reference for Sized class',
        ),
    ),
)
def test_collections_abc_rewrite(src, expected):
    assert _fix_plugins(src, settings=Settings()) == expected
```

## File: `tests/features/constant_fold_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'isinstance(x, str)',
            id='isinstance nothing duplicated',
        ),
        pytest.param(
            'issubclass(x, str)',
            id='issubclass nothing duplicated',
        ),
        pytest.param(
            'try: ...\n'
            'except Exception: ...\n',
            id='try-except nothing duplicated',
        ),
        pytest.param(
            'isinstance(x, (str, (str,)))',
            id='only consider flat tuples',
        ),
        pytest.param(
            'isinstance(x, (f(), a().g))',
            id='only consider names and dotted names',
        ),
    ),
)
def test_constant_fold_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'isinstance(x, (str, str, int))',

            'isinstance(x, (str, int))',

            id='isinstance',
        ),
        pytest.param(
            'issubclass(x, (str, str, int))',

            'issubclass(x, (str, int))',

            id='issubclass',
        ),
        pytest.param(
            'try: ...\n'
            'except (Exception, Exception, TypeError): ...\n',

            'try: ...\n'
            'except (Exception, TypeError): ...\n',

            id='except',
        ),

        pytest.param(
            'isinstance(x, (str, str))',

            'isinstance(x, str)',

            id='folds to 1',
        ),

        pytest.param(
            'isinstance(x, (a.b, a.b, a.c))',
            'isinstance(x, (a.b, a.c))',
            id='folds dotted names',
        ),
        pytest.param(
            'try: ...\n'
            'except(a, a): ...\n',

            'try: ...\n'
            'except a: ...\n',

            id='deduplication to 1 does not cause syntax error with except',
        ),
    ),
)
def test_constant_fold(s, expected):
    assert _fix_plugins(s, settings=Settings()) == expected
```

## File: `tests/features/datetime_utc_alias_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s',),
    (
        pytest.param(
            'import datetime\n'
            'print(datetime.timezone(-1))',

            id='not rewriting timezone object to alias',
        ),
    ),
)
def test_fix_datetime_utc_alias_noop(s):
    assert _fix_plugins(s, settings=Settings(min_version=(3,))) == s
    assert _fix_plugins(s, settings=Settings(min_version=(3, 11))) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import datetime\n'
            'print(datetime.timezone.utc)',

            'import datetime\n'
            'print(datetime.UTC)',

            id='rewriting to alias',
        ),
    ),
)
def test_fix_datetime_utc_alias(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3,))) == s
    assert _fix_plugins(s, settings=Settings(min_version=(3, 11))) == expected
```

## File: `tests/features/default_encoding_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('"asd".encode("utf-8")', '"asd".encode()'),
        ('f"asd".encode("utf-8")', 'f"asd".encode()'),
        ('f"{3}asd".encode("utf-8")', 'f"{3}asd".encode()'),
        ('fr"asd".encode("utf-8")', 'fr"asd".encode()'),
        ('r"asd".encode("utf-8")', 'r"asd".encode()'),
        ('"asd".encode("utf8")', '"asd".encode()'),
        ('"asd".encode("UTF-8")', '"asd".encode()'),
        pytest.param(
            '"asd".encode(("UTF-8"))',
            '"asd".encode()',
            id='parenthesized encoding',
        ),
        (
            'sys.stdout.buffer.write(\n    "a"\n    "b".encode("utf-8")\n)',
            'sys.stdout.buffer.write(\n    "a"\n    "b".encode()\n)',
        ),
        (
            'x = (\n'
            '    "y\\u2603"\n'
            ').encode("utf-8")\n',
            'x = (\n'
            '    "y\\u2603"\n'
            ').encode()\n',
        ),
        pytest.param(
            'f"{x}(".encode("utf-8")',
            'f"{x}(".encode()',
            id='3.12+ handle open brace in fstring',
        ),
        pytest.param(
            'f"{foo(bar)}(".encode("utf-8")',
            'f"{foo(bar)}(".encode()',
            id='f-string with function call',
        ),
    ),
)
def test_fix_encode(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.parametrize(
    's',
    (
        # non-utf-8 codecs should not be changed
        '"asd".encode("unknown-codec")',
        '"asd".encode("ascii")',

        # only autofix string literals to avoid false positives
        'x="asd"\nx.encode("utf-8")',

        # the current version is too timid to handle these
        '"asd".encode("utf-8", "strict")',
        '"asd".encode(encoding="utf-8")',
    ),
)
def test_fix_encode_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s
```

## File: `tests/features/defaultdict_lambda_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s',),
    (
        pytest.param(
            'from collections import defaultdict as dd\n\n'
            'dd(lambda: set())\n',
            id='not following as imports',
        ),
        pytest.param(
            'from collections2 import defaultdict\n\n'
            'dd(lambda: dict())\n',
            id='not following unknown import',
        ),
        pytest.param(
            'from .collections import defaultdict\n'
            'defaultdict(lambda: list())\n',
            id='relative imports',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: {1}))\n',
            id='non empty set',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: [1]))\n'
            'defaultdict(lambda: list([1])))\n',
            id='non empty list',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: {1: 2})\n',
            id='non empty dict, literal',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: dict([(1,2),])))\n',
            id='non empty dict, call with args',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: dict(a=[1]))\n',
            id='non empty dict, call with kwargs',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: (1,))\n',
            id='non empty tuple, literal',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: tuple([1]))\n',
            id='non empty tuple, calls with arg',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: "AAA")\n'
            'defaultdict(lambda: \'BBB\')\n',
            id='non empty string',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: 10)\n'
            'defaultdict(lambda: -2)\n',
            id='non zero integer',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: 0.2)\n'
            'defaultdict(lambda: 0.00000001)\n'
            'defaultdict(lambda: -2.3)\n',
            id='non zero float',
        ),
        pytest.param(
            'import collections\n'
            'collections.defaultdict(lambda: None)\n',
            id='lambda: None is not equivalent to defaultdict()',
        ),
    ),
)
def test_fix_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: set())\n',
            'from collections import defaultdict\n\n'
            'defaultdict(set)\n',
            id='call with attr, set()',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: list())\n',
            'from collections import defaultdict\n\n'
            'defaultdict(list)\n',
            id='call with attr, list()',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: dict())\n',
            'from collections import defaultdict\n\n'
            'defaultdict(dict)\n',
            id='call with attr, dict()',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: tuple())\n',
            'from collections import defaultdict\n\n'
            'defaultdict(tuple)\n',
            id='call with attr, tuple()',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: [])\n',
            'from collections import defaultdict\n\n'
            'defaultdict(list)\n',
            id='call with attr, []',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: {})\n',
            'from collections import defaultdict\n\n'
            'defaultdict(dict)\n',
            id='call with attr, {}',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: ())\n',
            'from collections import defaultdict\n\n'
            'defaultdict(tuple)\n',
            id='call with attr, ()',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: "")\n',
            'from collections import defaultdict\n\n'
            'defaultdict(str)\n',
            id='call with attr, empty string (double quote)',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: \'\')\n',
            'from collections import defaultdict\n\n'
            'defaultdict(str)\n',
            id='call with attr, empty string (single quote)',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: 0)\n',
            'from collections import defaultdict\n\n'
            'defaultdict(int)\n',
            id='call with attr, int',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: 0.0)\n',
            'from collections import defaultdict\n\n'
            'defaultdict(float)\n',
            id='call with attr, float',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: 0.0000)\n',
            'from collections import defaultdict\n\n'
            'defaultdict(float)\n',
            id='call with attr, long float',
        ),
        pytest.param(
            'from collections import defaultdict\n\n'
            'defaultdict(lambda: [], {1: []})\n',
            'from collections import defaultdict\n\n'
            'defaultdict(list, {1: []})\n',
            id='defauldict with kwargs',
        ),
        pytest.param(
            'import collections\n\n'
            'collections.defaultdict(lambda: set())\n'
            'collections.defaultdict(lambda: list())\n'
            'collections.defaultdict(lambda: dict())\n'
            'collections.defaultdict(lambda: tuple())\n'
            'collections.defaultdict(lambda: [])\n'
            'collections.defaultdict(lambda: {})\n'
            'collections.defaultdict(lambda: "")\n'
            'collections.defaultdict(lambda: \'\')\n'
            'collections.defaultdict(lambda: 0)\n'
            'collections.defaultdict(lambda: 0.0)\n'
            'collections.defaultdict(lambda: 0.00000)\n'
            'collections.defaultdict(lambda: 0j)\n',
            'import collections\n\n'
            'collections.defaultdict(set)\n'
            'collections.defaultdict(list)\n'
            'collections.defaultdict(dict)\n'
            'collections.defaultdict(tuple)\n'
            'collections.defaultdict(list)\n'
            'collections.defaultdict(dict)\n'
            'collections.defaultdict(str)\n'
            'collections.defaultdict(str)\n'
            'collections.defaultdict(int)\n'
            'collections.defaultdict(float)\n'
            'collections.defaultdict(float)\n'
            'collections.defaultdict(complex)\n',
            id='call with attr',
        ),
    ),
)
def test_fix_defaultdict(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/dict_literals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # Don't touch irrelevant code
        'x = 5',
        'dict()',
        # Don't touch syntax errors
        '(',
        # Don't touch strange looking calls
        'dict ((a, b) for a, b in y)',
        # Don't rewrite kwargd dicts
        'dict(((a, b) for a, b in y), x=1)',
        'dict(((a, b) for a, b in y), **kwargs)',
        pytest.param(
            'f"{dict((a, b) for a, b in y)}"',
            id='directly inside f-string placeholder',
        ),
    ),
)
def test_fix_dict_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        # dict of generator expression
        ('dict((a, b) for a, b in y)', '{a: b for a, b in y}'),
        ('dict((a, b,) for a, b in y)', '{a: b for a, b in y}'),
        ('dict((a, b, ) for a, b in y)', '{a: b for a, b in y}'),
        ('dict([a, b] for a, b in y)', '{a: b for a, b in y}'),
        # Parenthesized target
        ('dict(((a, b)) for a, b in y)', '{a: b for a, b in y}'),
        # dict of list comprehension
        ('dict([(a, b) for a, b in y])', '{a: b for a, b in y}'),
        # ast doesn't tell us about the tuple in the list
        ('dict([(a, b), c] for a, b, c in y)', '{(a, b): c for a, b, c in y}'),
        # ast doesn't tell us about parenthesized keys
        ('dict(((a), b) for a, b in y)', '{(a): b for a, b in y}'),
        # Nested dictcomps
        (
            'dict((k, dict((k2, v2) for k2, v2 in y2)) for k, y2 in y)',
            '{k: {k2: v2 for k2, v2 in y2} for k, y2 in y}',
        ),
        # This doesn't get fixed by autopep8 and can cause a syntax error
        ('dict((a, b)for a, b in y)', '{a: b for a, b in y}'),
        # Need to remove trailing commas on the element
        (
            'dict(\n'
            '    (\n'
            '        a,\n'
            '        b,\n'
            '    )\n'
            '    for a, b in y\n'
            ')',
            # Ideally, this'll go through some other formatting tool before
            # being committed.  Shrugs!
            '{\n'
            '        a:\n'
            '        b\n'
            '    for a, b in y\n'
            '}',
        ),
        # Don't gobble the last paren in a dictcomp
        (
            'x(\n'
            '    dict(\n'
            '        (a, b) for a, b in y\n'
            '    )\n'
            ')',
            'x(\n'
            '    {\n'
            '        a: b for a, b in y\n'
            '    }\n'
            ')',
        ),
    ),
)
def test_dictcomps(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/encoding_cookie_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            '# line 1\n# line 2\n# coding: utf-8\n',
            id='only on first two lines',
        ),
    ),
)
def test_noop(s):
    assert _fix_tokens(s) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            '# coding: utf-8',
            '',
        ),
        (
            '# coding: us-ascii\nx = 1\n',
            'x = 1\n',
        ),
        (
            '#!/usr/bin/env python\n'
            '# coding: utf-8\n'
            'x = 1\n',

            '#!/usr/bin/env python\n'
            'x = 1\n',
        ),
    ),
)
def test_rewrite(s, expected):
    assert _fix_tokens(s) == expected
```

## File: `tests/features/escape_sequences_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        '""',
        r'r"\d"', r"r'\d'", r'r"""\d"""', r"r'''\d'''",
        r'rb"\d"',
        # make sure we don't replace an already valid string
        r'"\\d"',
        # this is already a proper unicode escape
        r'"\u2603"',
        # don't touch already valid escapes
        r'"\r\n"',
        # python3.3+ named unicode escapes
        r'"\N{SNOWMAN}"',
        # don't touch escaped newlines
        '"""\\\n"""', '"""\\\r\n"""', '"""\\\r"""',
    ),
)
def test_fix_escape_sequences_noop(s):
    assert _fix_tokens(s) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        # no valid escape sequences, make a raw literal
        (r'"\d"', r'r"\d"'),
        # when there are valid escape sequences, need to use backslashes
        (r'"\n\d"', r'"\n\\d"'),
        # this gets un-u'd and raw'd
        (r'u"\d"', r'r"\d"'),
        # `rb` is not a valid string prefix in python2.x
        (r'b"\d"', r'br"\d"'),
        # 8 and 9 aren't valid octal digits
        (r'"\8"', r'r"\8"'), (r'"\9"', r'r"\9"'),
        # explicit byte strings should not honor string-specific escapes
        ('b"\\u2603"', 'br"\\u2603"'),
        # do not make a raw string for escaped newlines
        ('"""\\\n\\q"""', '"""\\\n\\\\q"""'),
        ('"""\\\r\n\\q"""', '"""\\\r\n\\\\q"""'),
        ('"""\\\r\\q"""', '"""\\\r\\\\q"""'),
        # python2.x allows \N, in python3.3+ this is a syntax error
        (r'"\N"', r'r"\N"'), (r'"\N\n"', r'"\\N\n"'),
        (r'"\N{SNOWMAN}\q"', r'"\N{SNOWMAN}\\q"'),
        (r'b"\N{SNOWMAN}"', r'br"\N{SNOWMAN}"'),
    ),
)
def test_fix_escape_sequences(s, expected):
    assert _fix_tokens(s) == expected
```

## File: `tests/features/exceptions_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'try: ...\n'
            'except Exception:\n'
            '    raise',
            id='empty raise',
        ),
        pytest.param(
            'try: ...\n'
            'except: ...\n',
            id='empty try-except',
        ),
        pytest.param(
            'try: ...\n'
            'except AssertionError: ...\n',
            id='unrelated exception type as name',
        ),
        pytest.param(
            'try: ...\n'
            'except (AssertionError,): ...\n',
            id='unrelated exception type as tuple',
        ),
        pytest.param(
            'try: ...\n'
            'except OSError: ...\n',
            id='already rewritten name',
        ),
        pytest.param(
            'try: ...\n'
            'except (TypeError, OSError): ...\n',
            id='already rewritten tuple',
        ),
        pytest.param(
            'from .os import error\n'
            'raise error(1)\n',
            id='same name as rewrite but relative import',
        ),
        pytest.param(
            'from os import error\n'
            'def f():\n'
            '    error = 3\n'
            '    return error\n',
            id='not rewriting outside of raise or except',
        ),
        pytest.param(
            'from os import error as the_roof\n'
            'raise the_roof()\n',
            id='ignoring imports with aliases',
        ),
        # TODO: could probably rewrite these but leaving for now
        pytest.param(
            'import os\n'
            'try: ...\n'
            'except (os).error: ...\n',
            id='weird parens',
        ),
    ),
)
def test_fix_exceptions_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'raise socket.timeout()',
            (3, 9),
            id='raise socket.timeout is noop <3.10',
        ),
        pytest.param(
            'try: ...\n'
            'except socket.timeout: ...\n',
            (3, 9),
            id='except socket.timeout is noop <3.10',
        ),
        pytest.param(
            'raise asyncio.TimeoutError()',
            (3, 10),
            id='raise asyncio.TimeoutError() is noop <3.11',
        ),
        pytest.param(
            'try: ...\n'
            'except asyncio.TimeoutError: ...\n',
            (3, 10),
            id='except asyncio.TimeoutError() is noop <3.11',
        ),
    ),
)
def test_fix_exceptions_version_specific_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'raise mmap.error(1)\n',
            'raise OSError(1)\n',
            id='mmap.error',
        ),
        pytest.param(
            'raise os.error(1)\n',
            'raise OSError(1)\n',
            id='os.error',
        ),
        pytest.param(
            'raise select.error(1)\n',
            'raise OSError(1)\n',
            id='select.error',
        ),
        pytest.param(
            'raise socket.error(1)\n',
            'raise OSError(1)\n',
            id='socket.error',
        ),
        pytest.param(
            'raise IOError(1)\n',
            'raise OSError(1)\n',
            id='IOError',
        ),
        pytest.param(
            'raise EnvironmentError(1)\n',
            'raise OSError(1)\n',
            id='EnvironmentError',
        ),
        pytest.param(
            'raise WindowsError(1)\n',
            'raise OSError(1)\n',
            id='WindowsError',
        ),
        pytest.param(
            'raise os.error\n',
            'raise OSError\n',
            id='raise exception type without call',
        ),
        pytest.param(
            'from os import error\n'
            'raise error(1)\n',
            'from os import error\n'
            'raise OSError(1)\n',
            id='raise via from import',
        ),
        pytest.param(
            'try: ...\n'
            'except WindowsError: ...\n',

            'try: ...\n'
            'except OSError: ...\n',

            id='except of name',
        ),
        pytest.param(
            'try: ...\n'
            'except os.error: ...\n',

            'try: ...\n'
            'except OSError: ...\n',

            id='except of dotted name',
        ),
        pytest.param(
            'try: ...\n'
            'except (WindowsError,): ...\n',

            'try: ...\n'
            'except OSError: ...\n',

            id='except of name in tuple',
        ),
        pytest.param(
            'try: ...\n'
            'except (os.error,): ...\n',

            'try: ...\n'
            'except OSError: ...\n',

            id='except of dotted name in tuple',
        ),
        pytest.param(
            'try: ...\n'
            'except (WindowsError, KeyError, OSError): ...\n',

            'try: ...\n'
            'except (OSError, KeyError): ...\n',

            id='deduplicates exception types',
        ),
        pytest.param(
            'try: ...\n'
            'except (os.error, WindowsError, OSError): ...\n',

            'try: ...\n'
            'except OSError: ...\n',

            id='deduplicates to a single type',
        ),
        pytest.param(
            'try: ...\n'
            'except(os.error, WindowsError, OSError): ...\n',

            'try: ...\n'
            'except OSError: ...\n',

            id='deduplicates to a single type without whitespace',
        ),
        pytest.param(
            'from wat import error\n'
            'try: ...\n'
            'except (WindowsError, error): ...\n',

            'from wat import error\n'
            'try: ...\n'
            'except (OSError, error): ...\n',

            id='leave unrelated error names alone',
        ),
        pytest.param(
            'try: ...\n'
            'except (\n'
            '    BaseException,\n'
            '    BaseException # b\n'
            '): ...\n',

            'try: ...\n'
            'except BaseException: ...\n',

            id='dedupe with comment.  see #932',
        ),
        pytest.param(
            'try: ...\n'
            'except (\n'
            '    A, A,\n'
            '    B  # b\n'
            '): ...\n',

            'try: ...\n'
            'except (A, B): ...\n',

            id='dedupe other exception, one contains comment.  see #932',
        ),
    ),
)
def test_fix_exceptions(s, expected):
    assert _fix_plugins(s, settings=Settings()) == expected


@pytest.mark.parametrize(
    ('s', 'expected', 'version'),
    (
        pytest.param(
            'raise socket.timeout(1)\n',
            'raise TimeoutError(1)\n',
            (3, 10),
            id='socket.timeout',
        ),
        pytest.param(
            'raise asyncio.TimeoutError(1)\n',
            'raise TimeoutError(1)\n',
            (3, 11),
            id='asyncio.TimeoutError',
        ),
    ),
)
def test_fix_exceptions_versioned(s, expected, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == expected


def test_can_rewrite_disparate_names():
    s = '''\
try: ...
except (asyncio.TimeoutError, WindowsError): ...
'''
    expected = '''\
try: ...
except (TimeoutError, OSError): ...
'''

    assert _fix_plugins(s, settings=Settings(min_version=(3, 11))) == expected
```

## File: `tests/features/extra_parens_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        'print("hello world")',
        'print((1, 2, 3))',
        'print(())',
        'print((\n))',
        # don't touch parenthesized generators
        'sum((block.code for block in blocks), [])',
        # don't touch coroutine yields
        'def f():\n'
        '    x = int((yield 1))\n',
    ),
)
def test_fix_extra_parens_noop(s):
    assert _fix_tokens(s) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('print(("hello world"))', 'print("hello world")'),
        ('print(("foo{}".format(1)))', 'print("foo{}".format(1))'),
        ('print((((1))))', 'print(1)'),
        (
            'print(\n'
            '    ("foo{}".format(1))\n'
            ')',

            'print(\n'
            '    "foo{}".format(1)\n'
            ')',
        ),
        (
            'print(\n'
            '    (\n'
            '        "foo"\n'
            '    )\n'
            ')\n',

            'print(\n'
            '        "foo"\n'
            ')\n',
        ),
        pytest.param(
            'def f():\n'
            '    x = int(((yield 1)))\n',

            'def f():\n'
            '    x = int((yield 1))\n',

            id='extra parens on coroutines are instead reduced to 2',
        ),
        pytest.param(
            'f((f"{x})"))',
            'f(f"{x})")',
            id='3.12: handle close brace in fstring body',
        ),
        pytest.param(
            'f((f"{x}("))',
            'f(f"{x}(")',
            id='3.12: handle open brace in fstring body',
        ),
    ),
)
def test_fix_extra_parens(s, expected):
    assert _fix_tokens(s) == expected
```

## File: `tests/features/format_literals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        # Don't touch syntax errors
        '"{0}"format(1)',
        pytest.param("'{}'.format(1)", id='already upgraded'),
        # Don't touch invalid format strings
        "'{'.format(1)", "'}'.format(1)",
        # Don't touch non-format strings
        "x = ('{0} {1}',)\n",
        # Don't touch non-incrementing integers
        "'{0} {0}'.format(1)",
        # Formats can be embedded in formats, leave these alone?
        "'{0:<{1}}'.format(1, 4)",
        # don't attempt to fix this, garbage in garbage out
        "'{' '0}'.format(1)",
        # comment looks like placeholder but is not!
        '("{0}" # {1}\n"{2}").format(1, 2, 3)',
        # don't touch f-strings (these are wrong but don't make it worse)
        'f"{0}".format(a)',
        # shouldn't touch the format spec
        r'"{}\N{SNOWMAN}".format("")',
    ),
)
def test_format_literals_noop(s):
    assert _fix_tokens(s) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        # Simplest case
        ("'{0}'.format(1)", "'{}'.format(1)"),
        ("'{0:x}'.format(30)", "'{:x}'.format(30)"),
        ("x = '{0}'.format(1)", "x = '{}'.format(1)"),
        # Multiline strings
        ("'''{0}\n{1}\n'''.format(1, 2)", "'''{}\n{}\n'''.format(1, 2)"),
        # Multiple implicitly-joined strings
        ("'{0}' '{1}'.format(1, 2)", "'{}' '{}'.format(1, 2)"),
        # Multiple implicitly-joined strings over lines
        (
            'print(\n'
            "    'foo{0}'\n"
            "    'bar{1}'.format(1, 2)\n"
            ')',
            'print(\n'
            "    'foo{}'\n"
            "    'bar{}'.format(1, 2)\n"
            ')',
        ),
        # Multiple implicitly-joind strings over lines with comments
        (
            'print(\n'
            "    'foo{0}'  # ohai\n"
            "    'bar{1}'.format(1, 2)\n"
            ')',
            'print(\n'
            "    'foo{}'  # ohai\n"
            "    'bar{}'.format(1, 2)\n"
            ')',
        ),
        # joined by backslash
        (
            'x = "foo {0}" \\\n'
            '    "bar {1}".format(1, 2)',
            'x = "foo {}" \\\n'
            '    "bar {}".format(1, 2)',
        ),
        # parenthesized string literals
        ('("{0}").format(1)', '("{}").format(1)'),
        pytest.param(
            r'"\N{snowman} {0}".format(1)',
            r'"\N{snowman} {}".format(1)',
            id='named escape sequence',
        ),
    ),
)
def test_format_literals(s, expected):
    assert _fix_tokens(s) == expected
```

## File: `tests/features/format_locals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            '"{x}".format(**locals())',
            (3,),
            id='not 3.6+',
        ),
        pytest.param(
            '"{x} {y}".format(x, **locals())',
            (3, 6),
            id='mixed locals() and params',
        ),
    ),
)
def test_fix_format_locals_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            '"{x}".format(**locals())',
            'f"{x}"',
            id='normal case',
        ),
        pytest.param(
            '"{x}" "{y}".format(**locals())',
            'f"{x}" f"{y}"',
            id='joined strings',
        ),
        pytest.param(
            '(\n'
            '    "{x}"\n'
            '    "{y}"\n'
            ').format(**locals())\n',
            '(\n'
            '    f"{x}"\n'
            '    f"{y}"\n'
            ')\n',
            id='joined strings with parens',
        ),
    ),
)
def test_fix_format_locals(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == expected
```

## File: `tests/features/fstrings_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # syntax error
        '(',
        # invalid format strings
        "'{'.format(a)", "'}'.format(a)",
        # weird syntax
        '"{}" . format(x)',
        # spans multiple lines
        '"{}".format(\n    a,\n)',
        # starargs
        '"{} {}".format(*a)', '"{foo} {bar}".format(**b)"',
        # likely makes the format longer
        '"{0} {0}".format(arg)', '"{x} {x}".format(arg)',
        '"{x.y} {x.z}".format(arg)',
        # bytestrings don't participate in `.format()` or `f''`
        # but are legal in python 2
        'b"{} {}".format(a, b)',
        # for now, too difficult to rewrite correctly
        '"{:{}}".format(x, y)',
        '"{a[b]}".format(a=a)',
        '"{a.a[b]}".format(a=a)',
        # not enough placeholders / placeholders missing
        '"{}{}".format(a)', '"{a}{b}".format(a=a)',
        # backslashes and quotes cannot nest
        r'''"{}".format(a['\\'])''',
        '"{}".format(a["b"])',
        "'{}'.format(a['b'])",
        # await only becomes keyword in Python 3.7+
        "async def c(): return '{}'.format(await 3)",
        "async def c(): return '{}'.format(1 + await 3)",
    ),
)
def test_fix_fstrings_noop(s):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('"{} {}".format(a, b)', 'f"{a} {b}"'),
        ('"{1} {0}".format(a, b)', 'f"{b} {a}"'),
        ('"{x.y}".format(x=z)', 'f"{z.y}"'),
        ('"{.x} {.y}".format(a, b)', 'f"{a.x} {b.y}"'),
        ('"{} {}".format(a.b, c.d)', 'f"{a.b} {c.d}"'),
        ('"{}".format(a())', 'f"{a()}"'),
        ('"{}".format(a.b())', 'f"{a.b()}"'),
        ('"{}".format(a.b().c())', 'f"{a.b().c()}"'),
        ('"hello {}!".format(name)', 'f"hello {name}!"'),
        ('"{}{{}}{}".format(escaped, y)', 'f"{escaped}{{}}{y}"'),
        ('"{}{b}{}".format(a, c, b=b)', 'f"{a}{b}{c}"'),
        ('"{}".format(0x0)', 'f"{0x0}"'),
        pytest.param(
            r'"\N{snowman} {}".format(a)',
            r'f"\N{snowman} {a}"',
            id='named escape sequences',
        ),
        pytest.param(
            'u"foo{}".format(1)',
            'f"foo{1}"',
            id='u-prefixed format',
        ),
    ),
)
def test_fix_fstrings(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == expected


def test_fix_fstrings_await_py37():
    s = "async def c(): return '{}'.format(await 1+foo())"
    expected = "async def c(): return f'{await 1+foo()}'"
    assert _fix_plugins(s, settings=Settings(min_version=(3, 7))) == expected
```

## File: `tests/features/identity_equality_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        'x is True',
        'x is False',
        'x is None',
        'x is (not 5)',
        'x is 5 + 5',
        # pyupgrade is timid about containers since the original can be
        # always-False, but the rewritten code could be `True`.
        'x is ()',
        'x is []',
        'x is {}',
        'x is {1}',
    ),
)
def test_fix_is_compare_to_literal_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param('x is 5', 'x == 5', id='`is`'),
        pytest.param('x is not 5', 'x != 5', id='`is not`'),
        pytest.param('x is ""', 'x == ""', id='string'),
        pytest.param('x is u""', 'x == u""', id='unicode string'),
        pytest.param('x is b""', 'x == b""', id='bytes'),
        pytest.param('x is 1.5', 'x == 1.5', id='float'),
        pytest.param('x == 5 is 5', 'x == 5 == 5', id='compound compare'),
        pytest.param(
            'if (\n'
            '    x is\n'
            '    5\n'
            '): pass\n',

            'if (\n'
            '    x ==\n'
            '    5\n'
            '): pass\n',

            id='multi-line `is`',
        ),
        pytest.param(
            'if (\n'
            '    x is\n'
            '    not 5\n'
            '): pass\n',

            'if (\n'
            '    x != 5\n'
            '): pass\n',

            id='multi-line `is not`',
        ),
    ),
)
def test_fix_is_compare_to_literal(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/import_removals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'min_version'),
    (
        ('', (3,)),
        ('from foo import bar', (3,)),
        ('from __future__ import unknown', (3,)),
        ('from __future__ import annotations', (3,)),
        ('from six import *', (3,)),
        ('from six.moves import map as notmap', (3,)),
        ('from unrelated import queue as map', (3,)),
        pytest.param(
            'if True:\n'
            '    from six.moves import map\n',
            (3,),
            id='import removal not at module scope',
        ),
    ),
)
def test_import_removals_noop(s, min_version):
    assert _fix_plugins(s, settings=Settings(min_version=min_version)) == s


@pytest.mark.parametrize(
    ('s', 'min_version', 'expected'),
    (
        ('from __future__ import generators\n', (3,), ''),
        ('from __future__ import generators', (3,), ''),
        ('from __future__ import division\n', (3,), ''),
        ('from __future__ import division\n', (3, 6), ''),
        ('from __future__ import (generators,)', (3,), ''),
        ('from __future__ import print_function', (3, 8), ''),
        ('from builtins import map', (3,), ''),
        ('from builtins import *', (3,), ''),
        ('from six.moves import map', (3,), ''),
        ('from six.moves.builtins import map', (3,), ''),
        pytest.param(
            'from __future__ import absolute_import, annotations\n',
            (3,),
            'from __future__ import annotations\n',
            id='remove at beginning single line',
        ),
        pytest.param(
            'from __future__ import (\n'
            '    absolute_import,\n'
            '    annotations,\n'
            ')',
            (3,),
            'from __future__ import (\n'
            '    annotations,\n'
            ')',
            id='remove at beginning paren continuation',
        ),
        pytest.param(
            'from __future__ import \\\n'
            '    absolute_import, \\\n'
            '    annotations\n',
            (3,),
            'from __future__ import \\\n'
            '    annotations\n',
            id='remove at beginning backslash continuation',
        ),
        pytest.param(
            'from __future__ import annotations, absolute_import\n',
            (3,),
            'from __future__ import annotations\n',
            id='remove at end single line',
        ),
        pytest.param(
            'from __future__ import (\n'
            '    annotations,\n'
            '    absolute_import,\n'
            ')',
            (3,),
            'from __future__ import (\n'
            '    annotations,\n'
            ')',
            id='remove at end paren continuation',
        ),
        pytest.param(
            'from __future__ import \\\n'
            '    annotations, \\\n'
            '    absolute_import\n',
            (3,),
            'from __future__ import \\\n'
            '    annotations\n',
            id='remove at end backslash continuation',
        ),
        pytest.param(
            'from __future__ import (\n'
            '    absolute_import,\n'
            '    annotations,\n'
            '    division,\n'
            ')',
            (3,),
            'from __future__ import (\n'
            '    annotations,\n'
            ')',
            id='remove multiple',
        ),
        pytest.param(
            'from __future__ import with_statement\n'
            '\n'
            'import os.path\n',
            (3,),
            'import os.path\n',
            id='remove top-file whitespace',
        ),
        pytest.param(
            'from six . moves import map', (3,), '',
            id='weird whitespace in dotted name',
        ),
        pytest.param(
            'from io import open, BytesIO as BIO\n'
            'from io import BytesIO as BIO, open\n',
            (3,),
            'from io import BytesIO as BIO\n'
            'from io import BytesIO as BIO\n',
            id='removal with import-as',
        ),
    ),
)
def test_import_removals(s, min_version, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=min_version))
    assert ret == expected
```

## File: `tests/features/import_replaces_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'min_version'),
    (
        pytest.param('from a import b', (3,), id='unrelated import'),
        pytest.param(
            'from .xml.etree.cElementTree import XML\n',
            (3,),
            id='leave relative imports alone',
        ),
        pytest.param(
            'if True: from six.moves import getcwd, StringIO\n',
            (3,),
            id='inline from-import with space',
        ),
        pytest.param(
            'if True:from six.moves import getcwd, StringIO\n',
            (3,),
            id='inline from-import without space',
        ),
        pytest.param(
            'if True:import mock, sys\n',
            (3,),
            id='inline import-import',
        ),
        pytest.param(
            'import xml.etree.cElementTree',
            (3,),
            id='import without alias',
        ),
        pytest.param(
            'from xml.etree import cElementTree',
            (3,),
            id='from import of module without alias',
        ),
        pytest.param(
            'from typing import Callable\n',
            (3, 9),
            id='skip rewriting of Callable in 3.9 since it is broken',
        ),
    ),
)
def test_import_replaces_noop(s, min_version):
    assert _fix_plugins(s, settings=Settings(min_version=min_version)) == s


def test_mock_noop_keep_mock():
    """This would've been rewritten if keep_mock were False"""
    s = (
        'from mock import patch\n'
        '\n'
        'patch("func")'
    )
    settings = Settings(keep_mock=True)
    assert _fix_plugins(s, settings=settings) == s


@pytest.mark.parametrize(
    ('s', 'min_version', 'expected'),
    (
        pytest.param(
            'from collections import Mapping\n',
            (3,),
            'from collections.abc import Mapping\n',
            id='one-name replacement',
        ),
        pytest.param(
            'from collections import Mapping as MAP\n',
            (3,),
            'from collections.abc import Mapping as MAP\n',
            id='one-name replacement with alias',
        ),
        pytest.param(
            'from collections import Mapping, Sequence\n',
            (3,),
            'from collections.abc import Mapping, Sequence\n',
            id='multi-name replacement',
        ),
        pytest.param(
            'from collections import Counter, Mapping\n',
            (3,),
            'from collections import Counter\n'
            'from collections.abc import Mapping\n',
            id='one name rewritten to new module',
        ),
        pytest.param(
            'from collections import Counter, Mapping',
            (3,),
            'from collections import Counter\n'
            'from collections.abc import Mapping\n',
            id='one name rewritten to new module, no eol',
        ),
        pytest.param(
            'from collections import (Counter, \n'
            '                         Mapping)\n',
            (3,),
            'from collections import (Counter)\n'
            'from collections.abc import Mapping\n',
            id='one name rewritten with parens',
        ),
        pytest.param(
            'from collections import Counter, \\\n'
            '                         Mapping\n',
            (3,),
            'from collections import Counter\n'
            'from collections.abc import Mapping\n',
            id='one name rewritten with backslash',
        ),
        pytest.param(
            'from collections import Counter, Mapping, Sequence\n',
            (3,),
            'from collections import Counter\n'
            'from collections.abc import Mapping, Sequence\n',
            id='multiple names rewritten to new module',
        ),
        pytest.param(
            'from six.moves import getcwd, StringIO\n',
            (3,),
            'from io import StringIO\n'
            'from os import getcwd\n',
            id='all imports rewritten but to multiple modules',
        ),
        pytest.param(
            'from collections import Mapping as mapping, Counter\n',
            (3,),
            'from collections import Counter\n'
            'from collections.abc import Mapping as mapping\n',
            id='new import with aliased name',
        ),
        pytest.param(
            'if True:\n'
            '    from xml.etree import cElementTree as ET\n',
            (3,),
            'if True:\n'
            '    from xml.etree import ElementTree as ET\n',
            id='indented and full import replaced',
        ),
        pytest.param(
            'if True:\n'
            '    from collections import Mapping, Counter\n',
            (3,),
            'if True:\n'
            '    from collections import Counter\n'
            '    from collections.abc import Mapping\n',
            id='indented from-import being added',
        ),
        pytest.param(
            'if True:\n'
            '    from six.moves import queue, urllib_request\n',
            (3,),
            'if True:\n'
            '    from six.moves import urllib_request\n'
            '    import queue\n',
            id='indented import-import being added',
        ),
        pytest.param(
            'if True:\n'
            '    import mock\n',
            (3,),
            'if True:\n'
            '    from unittest import mock\n',
            id='indented import-import rewritten',
        ),
        pytest.param(
            'if True:\n'
            '    if True:\n'
            '        pass\n'
            '    from collections import Mapping, Counter\n',
            (3,),
            'if True:\n'
            '    if True:\n'
            '        pass\n'
            '    from collections import Counter\n'
            '    from collections.abc import Mapping\n',
            id='indented import after dedent',
        ),
        pytest.param(
            'if True: from collections import Mapping\n',
            (3,),
            'if True: from collections.abc import Mapping\n',
            id='inline import, only one replacement',
        ),
        pytest.param(
            'import os\n'
            'from collections import Counter, Mapping\n'
            'import sys\n',
            (3,),
            'import os\n'
            'from collections import Counter\n'
            'from collections.abc import Mapping\n'
            'import sys\n',
            id='other imports left alone',
        ),
        pytest.param(
            'from six.moves import urllib_request, filter, getcwd\n',
            (3,),
            'from six.moves import urllib_request\n'
            'from os import getcwd\n',
            id='replaces and removals and one remaining',
        ),
        pytest.param(
            'from six.moves import filter, getcwd\n',
            (3,),
            'from os import getcwd\n',
            id='replaces and removals and no remaining',
        ),
        pytest.param(
            'from six.moves.queue import Queue\n',
            (3,),
            'from queue import Queue\n',
            id='module replacement',
        ),
        pytest.param(
            'from xml.etree.cElementTree import XML\n',
            (3,),
            'from xml.etree.ElementTree import XML\n',
            id='relative import func',
        ),
        pytest.param(
            'from xml.etree.cElementTree import XML, Element\n',
            (3,),
            'from xml.etree.ElementTree import XML, Element\n',
            id='import multiple objects',
        ),
        pytest.param(
            'from six.moves import queue\n',
            (3,),
            'import queue\n',
            id='from import a module to an import-import',
        ),
        pytest.param(
            'from six.moves import queue, map, getcwd\n',
            (3,),
            'from os import getcwd\n'
            'import queue\n',
            id='removal, rename, module rename',
        ),
        pytest.param(
            'from xml.etree import cElementTree as ET\n',
            (3,),
            'from xml.etree import ElementTree as ET\n',
            id='from import a module but aliased',
        ),
        pytest.param(
            'import xml.etree.cElementTree as ET',
            (3,),
            'import xml.etree.ElementTree as ET',
            id='import with alias',
        ),
        pytest.param(
            'import contextlib, xml.etree.cElementTree as ET\n',
            (3,),
            'import contextlib, xml.etree.ElementTree as ET\n',
            id='can rewrite multiple import imports',
        ),
        pytest.param(
            'import mock\n',
            (3,),
            'from unittest import mock\n',
            id='rewrites mock import',
        ),
        pytest.param(
            'import mock.mock\n',
            (3,),
            'from unittest import mock\n',
            id='rewrites mock.mock import',
        ),
        pytest.param(
            'import contextlib, mock, sys\n',
            (3,),
            'import contextlib, sys\n'
            'from unittest import mock\n',
            id='mock rewriting multiple imports in middle',
        ),
        pytest.param(
            'import mock, sys\n',
            (3,),
            'import sys\n'
            'from unittest import mock\n',
            id='mock rewriting multiple imports at beginning',
        ),
        pytest.param(
            'import mock, sys',
            (3,),
            'import sys\n'
            'from unittest import mock\n',
            id='adds import-import no eol',
        ),
        pytest.param(
            'from mock import mock\n',
            (3,),
            'from unittest import mock\n',
            id='mock import mock import',
        ),
        pytest.param(
            'from typing import Callable\n',
            (3, 10),
            'from collections.abc import Callable\n',
            id='typing.Callable is rewritable in 3.10+ only',
        ),
        pytest.param(
            'from typing import Optional, Sequence as S\n',
            (3, 10),
            'from typing import Optional\n'
            'from collections.abc import Sequence as S\n',
            id='aliasing in multi from import',
        ),
    ),
)
def test_import_replaces(s, min_version, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=min_version))
    assert ret == expected
```

## File: `tests/features/io_open_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


def test_fix_io_open_noop():
    src = '''\
from io import open
with open("f.txt") as f:
    print(f.read())
'''
    expected = '''\
with open("f.txt") as f:
    print(f.read())
'''
    ret = _fix_plugins(src, settings=Settings())
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'import io\n\n'
            'with io.open("f.txt", mode="r", buffering=-1, **kwargs) as f:\n'
            '   print(f.read())\n',

            'import io\n\n'
            'with open("f.txt", mode="r", buffering=-1, **kwargs) as f:\n'
            '   print(f.read())\n',
        ),
    ),
)
def test_fix_io_open(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/lru_cache_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'min_version'),
    (
        pytest.param(
            'from functools import lru_cache as lru_cache2\n\n'
            '@lru_cache2()\n'
            'def foo():\n'
            '    pass\n',
            (3, 8),
            id='not following as imports',
        ),
        pytest.param(
            'from functools import lru_cache\n\n'
            '@lru_cache(max_size=1024)\n'
            'def foo():\n'
            '    pass\n',
            (3, 8),
            id='not rewriting calls with args',
        ),
        pytest.param(
            'from functools2 import lru_cache\n\n'
            '@lru_cache()\n'
            'def foo():\n'
            '    pass\n',
            (3, 8),
            id='not following unknown import',
        ),
        pytest.param(
            'from functools import lru_cache\n\n'
            '@lru_cache()\n'
            'def foo():\n'
            '    pass\n',
            (3,),
            id='not rewriting below 3.8',
        ),
        pytest.param(
            'from .functools import lru_cache\n'
            '@lru_cache()\n'
            'def foo(): pass\n',
            (3, 8),
            id='relative imports',
        ),
    ),
)
def test_fix_no_arg_decorators_noop(s, min_version):
    assert _fix_plugins(s, settings=Settings(min_version=min_version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from functools import lru_cache\n\n'
            '@lru_cache()\n'
            'def foo():\n'
            '    pass\n',
            'from functools import lru_cache\n\n'
            '@lru_cache\n'
            'def foo():\n'
            '    pass\n',
            id='call without attr',
        ),
        pytest.param(
            'import functools\n\n'
            '@functools.lru_cache()\n'
            'def foo():\n'
            '    pass\n',
            'import functools\n\n'
            '@functools.lru_cache\n'
            'def foo():\n'
            '    pass\n',
            id='call with attr',
        ),
    ),
)
def test_fix_no_arg_decorators(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 8)))
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'min_version'),
    (
        pytest.param(
            'from functools import lru_cache\n'
            '@lru_cache(maxsize=None)\n'
            'def foo(): pass\n',
            (3, 9),
            id='from imported',
        ),
        pytest.param(
            'from functools import lru_cache\n'
            '@lru_cache(maxsize=1024)\n'
            'def foo(): pass\n',
            (3, 9),
            id='unrelated parameter',
        ),
        pytest.param(
            'import functools\n\n'
            '@functools.lru_cache(maxsize=None, typed=True)\n'
            'def foo():\n'
            '    pass\n',
            (3, 9),
            id='typed=True',
        ),
        pytest.param(
            'import functools\n\n'
            '@functools.lru_cache(maxsize=None, typed=False, foo=False)\n'
            'def foo():\n'
            '    pass\n',
            (3, 9),
            id='invalid keyword',
        ),
    ),
)
def test_fix_maxsize_none_decorators_noop(s, min_version):
    assert _fix_plugins(s, settings=Settings(min_version=min_version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import functools\n\n'
            '@functools.lru_cache(maxsize=None)\n'
            'def foo():\n'
            '    pass\n',
            'import functools\n\n'
            '@functools.cache\n'
            'def foo():\n'
            '    pass\n',
            id='call with attr',
        ),
        pytest.param(
            'import functools\n\n'
            '@functools.lru_cache(maxsize=None, typed=False)\n'
            'def foo():\n'
            '    pass\n',
            'import functools\n\n'
            '@functools.cache\n'
            'def foo():\n'
            '    pass\n',
            id='call with attr, maxsize=None then typed=False',
        ),
        pytest.param(
            'import functools\n\n'
            '@functools.lru_cache(typed=False, maxsize=None)\n'
            'def foo():\n'
            '    pass\n',
            'import functools\n\n'
            '@functools.cache\n'
            'def foo():\n'
            '    pass\n',
            id='call with attr, typed=False then maxsize=None',
        ),
    ),
)
def test_fix_maxsize_none_decorators(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 9)))
    assert ret == expected
```

## File: `tests/features/metaclass_type_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'x = type\n'
            '__metaclass__ = x\n',
            id='not rewriting "type" rename',
        ),
        pytest.param(
            'def foo():\n'
            '    __metaclass__ = type\n',
            id='not rewriting function scope',
        ),
        pytest.param(
            'class Foo:\n'
            '    __metaclass__ = type\n',
            id='not rewriting class scope',
        ),
        pytest.param(
            '__metaclass__, __meta_metaclass__ = type, None\n',
            id='not rewriting multiple assignment',
        ),
    ),
)
def test_metaclass_type_assignment_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            '__metaclass__ = type',
            '',
            id='module-scope assignment',
        ),
        pytest.param(
            '__metaclass__  =   type',
            '',
            id='module-scope assignment with extra whitespace',
        ),
        pytest.param(
            '__metaclass__ = (\n'
            '   type\n'
            ')\n',
            '',
            id='module-scope assignment across newline',
        ),
        pytest.param(
            '__metaclass__ = type\n'
            'a = 1\n',
            'a = 1\n',
            id='replace with code after it',
        ),
    ),
)
def test_fix_metaclass_type_assignment(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/mock_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import mock.mock\n'
            '\n'
            'mock.mock.patch("func1")\n'
            'mock.patch("func2")\n',
            'from unittest import mock\n'
            '\n'
            'mock.patch("func1")\n'
            'mock.patch("func2")\n',
            id='double mock absolute import func',
        ),
        pytest.param(
            'import mock.mock\n'
            '\n'
            'mock.mock.patch.object(Foo, "func1")\n'
            'mock.patch.object(Foo, "func2")\n',
            'from unittest import mock\n'
            '\n'
            'mock.patch.object(Foo, "func1")\n'
            'mock.patch.object(Foo, "func2")\n',
            id='double mock absolute import func attr',
        ),
    ),
)
def test_fix_mock(s, expected):
    assert _fix_plugins(s, settings=Settings()) == expected
```

## File: `tests/features/native_literals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        'str(1)',
        'str("foo"\n"bar")',  # creates a syntax error
        'str(*a)', 'str("foo", *a)',
        'str(**k)', 'str("foo", **k)',
        'str("foo", encoding="UTF-8")',
        'bytes("foo", encoding="UTF-8")',
        'bytes(b"foo"\nb"bar")',
        'bytes("foo"\n"bar")',
        'bytes(*a)', 'bytes("foo", *a)',
        'bytes("foo", **a)',
    ),
)
def test_fix_native_literals_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('str()', "''"),
        ('str("foo")', '"foo"'),
        ('str("""\nfoo""")', '"""\nfoo"""'),
        ('six.ensure_str("foo")', '"foo"'),
        ('six.ensure_text("foo")', '"foo"'),
        ('six.text_type("foo")', '"foo"'),
        pytest.param(
            'from six import text_type\n'
            'text_type("foo")\n',

            'from six import text_type\n'
            '"foo"\n',

            id='from import of rewritten name',
        ),
        ('bytes()', "b''"),
        ('bytes(b"foo")', 'b"foo"'),
        ('bytes(b"""\nfoo""")', 'b"""\nfoo"""'),
    ),
)
def test_fix_native_literals(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/new_style_classes_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # syntax error
        'x = (',
        # does not inherit from `object`
        'class C(B): pass',
    ),
)
def test_fix_classes_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'class C(object): pass',
            'class C: pass',
        ),
        (
            'class C(\n'
            '    object,\n'
            '): pass',
            'class C: pass',
        ),
        (
            'class C(B, object): pass',
            'class C(B): pass',
        ),
        (
            'class C(B, (object)): pass',
            'class C(B): pass',
        ),
        (
            'class C(B, ( object )): pass',
            'class C(B): pass',
        ),
        (
            'class C((object)): pass',
            'class C: pass',
        ),
        (
            'class C(\n'
            '    B,\n'
            '    object,\n'
            '): pass\n',
            'class C(\n'
            '    B,\n'
            '): pass\n',
        ),
        (
            'class C(\n'
            '    B,\n'
            '    object\n'
            '): pass\n',
            'class C(\n'
            '    B\n'
            '): pass\n',
        ),
        # only legal in python2
        (
            'class C(object, B): pass',
            'class C(B): pass',
        ),
        (
            'class C((object), B): pass',
            'class C(B): pass',
        ),
        (
            'class C(( object ), B): pass',
            'class C(B): pass',
        ),
        (
            'class C(\n'
            '    object,\n'
            '    B,\n'
            '): pass',
            'class C(\n'
            '    B,\n'
            '): pass',
        ),
        (
            'class C(\n'
            '    object,  # comment!\n'
            '    B,\n'
            '): pass',
            'class C(\n'
            '    B,\n'
            '): pass',
        ),
        (
            'class C(object, metaclass=ABCMeta): pass',
            'class C(metaclass=ABCMeta): pass',
        ),
    ),
)
def test_fix_classes(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/open_mode_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins
from pyupgrade._plugins.open_mode import _permute
from pyupgrade._plugins.open_mode import _plus


def test_plus():
    assert _plus(('a',)) == ('a', 'a+')
    assert _plus(('a', 'b')) == ('a', 'b', 'a+', 'b+')


def test_permute():
    assert _permute('ab') == ('ab', 'ba')
    assert _permute('abc') == ('abc', 'acb', 'bac', 'bca', 'cab', 'cba')


@pytest.mark.parametrize(
    's',
    (
        # already a reduced mode
        'open("foo", "w")',
        'open("foo", mode="w")',
        'open("foo", "rb")',
        # nonsense mode
        'open("foo", "Uw")',
        'open("foo", qux="r")',
        'open("foo", 3)',
        'open(mode="r")',
        # don't remove this, they meant to use `encoding=`
        'open("foo", "r", "utf-8")',
    ),
)
def test_fix_open_mode_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('open("foo", "U")', 'open("foo")'),
        ('open("foo", mode="U")', 'open("foo")'),
        ('open("foo", "Ur")', 'open("foo")'),
        ('open("foo", mode="Ur")', 'open("foo")'),
        ('open("foo", "Ub")', 'open("foo", "rb")'),
        ('open("foo", mode="Ub")', 'open("foo", mode="rb")'),
        ('open("foo", "rUb")', 'open("foo", "rb")'),
        ('open("foo", mode="rUb")', 'open("foo", mode="rb")'),
        ('open("foo", "r")', 'open("foo")'),
        ('open("foo", mode="r")', 'open("foo")'),
        ('open("foo", "rt")', 'open("foo")'),
        ('open("foo", mode="rt")', 'open("foo")'),
        ('open("f", "r", encoding="UTF-8")', 'open("f", encoding="UTF-8")'),
        (
            'open("f", mode="r", encoding="UTF-8")',
            'open("f", encoding="UTF-8")',
        ),
        (
            'open(file="f", mode="r", encoding="UTF-8")',
            'open(file="f", encoding="UTF-8")',
        ),
        (
            'open("f", encoding="UTF-8", mode="r")',
            'open("f", encoding="UTF-8")',
        ),
        (
            'open(file="f", encoding="UTF-8", mode="r")',
            'open(file="f", encoding="UTF-8")',
        ),
        (
            'open(mode="r", encoding="UTF-8", file="t.py")',
            'open(encoding="UTF-8", file="t.py")',
        ),
        pytest.param('open(f, u"r")', 'open(f)', id='string with u flag'),
        pytest.param(
            'io.open("foo", "r")',
            'open("foo")',
            id='io.open also rewrites modes in a single pass',
        ),
        ('open("foo", "wt")', 'open("foo", "w")'),
        ('open("foo", "xt")', 'open("foo", "x")'),
        ('open("foo", "at")', 'open("foo", "a")'),
        ('open("foo", "wt+")', 'open("foo", "w+")'),
        ('open("foo", "rt+")', 'open("foo", "r+")'),
    ),
)
def test_fix_open_mode(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/percent_format_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins
from pyupgrade._plugins.percent_format import _parse_percent_format
from pyupgrade._plugins.percent_format import _percent_to_format
from pyupgrade._plugins.percent_format import _simplify_conversion_flag


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            '""', (
                ('""', None),
            ),
        ),
        (
            '"%%"', (
                ('"', (None, None, None, None, '%')),
                ('"', None),
            ),
        ),
        (
            '"%s"', (
                ('"', (None, None, None, None, 's')),
                ('"', None),
            ),
        ),
        (
            '"%s two! %s"', (
                ('"', (None, None, None, None, 's')),
                (' two! ', (None, None, None, None, 's')),
                ('"', None),
            ),
        ),
        (
            '"%(hi)s"', (
                ('"', ('hi', None, None, None, 's')),
                ('"', None),
            ),
        ),
        (
            '"%()s"', (
                ('"', ('', None, None, None, 's')),
                ('"', None),
            ),
        ),
        (
            '"%#o"', (
                ('"', (None, '#', None, None, 'o')),
                ('"', None),
            ),
        ),
        (
            '"% #0-+d"', (
                ('"', (None, ' #0-+', None, None, 'd')),
                ('"', None),
            ),
        ),
        (
            '"%5d"', (
                ('"', (None, None, '5', None, 'd')),
                ('"', None),
            ),
        ),
        (
            '"%*d"', (
                ('"', (None, None, '*', None, 'd')),
                ('"', None),
            ),
        ),
        (
            '"%.f"', (
                ('"', (None, None, None, '.', 'f')),
                ('"', None),
            ),
        ),
        (
            '"%.5f"', (
                ('"', (None, None, None, '.5', 'f')),
                ('"', None),
            ),
        ),
        (
            '"%.*f"', (
                ('"', (None, None, None, '.*', 'f')),
                ('"', None),
            ),
        ),
        (
            '"%ld"', (
                ('"', (None, None, None, None, 'd')),
                ('"', None),
            ),
        ),
        (
            '"%(complete)#4.4f"', (
                ('"', ('complete', '#', '4', '.4', 'f')),
                ('"', None),
            ),
        ),
    ),
)
def test_parse_percent_format(s, expected):
    assert _parse_percent_format(s) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('%s', '{}'),
        ('%%%s', '%{}'),
        ('%(foo)s', '{foo}'),
        ('%2f', '{:2f}'),
        ('%r', '{!r}'),
        ('%a', '{!a}'),
    ),
)
def test_percent_to_format(s, expected):
    assert _percent_to_format(s) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('', ''),
        (' ', ' '),
        ('   ', ' '),
        ('#0- +', '#<+'),
        ('-', '<'),
    ),
)
def test_simplify_conversion_flag(s, expected):
    assert _simplify_conversion_flag(s) == expected


@pytest.mark.parametrize(
    's',
    (
        # cannot determine whether `unknown_type` is tuple or not
        '"%s" % unknown_type',
        # format of bytestring cannot be changed to `.format(...)`
        'b"%s" % (b"bytestring",)',
        # out-of-order parameter consumption
        '"%*s" % (5, "hi")', '"%.*s" % (5, "hi")',
        # potential conversion to int required
        '"%d" % (flt,)', '"%i" % (flt,)', '"%u" % (flt,)',
        # potential conversion to character required
        '"%c" % (some_string,)',
        # different output vs .format() in python 2
        '"%#o" % (123,)',
        # no format equivalent
        '"%()s" % {"": "empty"}',
        # different output in python2 / python 3
        '"%4%" % ()',
        # no equivalent in format specifier
        '"%.2r" % (1.25)', '"%.2a" % (1.25)',
        pytest.param('"%8s" % (None,)', id='unsafe width-string conversion'),
        # non-string mod
        'i % 3',
        # dict format but not keyed arguments
        '"%s" % {"k": "v"}',
        # dict format must have valid identifiers
        '"%()s" % {"": "bar"}',
        '"%(1)s" % {"1": "bar"}',
        # don't trigger `SyntaxError: keyword argument repeated`
        '"%(a)s" % {"a": 1, "a": 2}',
        # don't rewrite string-joins in dict literal
        '"%(ab)s" % {"a" "b": 1}',
        # don't rewrite strangely styled things
        '"%(a)s" % {"a"  :  1}',
        # don't rewrite non-str keys
        '"%(1)s" % {1: 2, "1": 2}',
        # don't rewrite keyword keys
        '"%(and)s" % {"and": 2}',
        # invalid string formats
        '"%" % {}', '"%(hi)" % {}', '"%2" % {}',
    ),
)
def test_percent_format_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        # tuple
        ('"trivial" % ()', '"trivial".format()'),
        ('"%s" % ("simple",)', '"{}".format("simple")'),
        ('"%s" % ("%s" % ("nested",),)', '"{}".format("{}".format("nested"))'),
        ('"%s%% percent" % (15,)', '"{}% percent".format(15)'),
        ('"%3f" % (15,)', '"{:3f}".format(15)'),
        ('"%-5f" % (5,)', '"{:<5f}".format(5)'),
        ('"%9f" % (5,)', '"{:9f}".format(5)'),
        ('"brace {} %s" % (1,)', '"brace {{}} {}".format(1)'),
        (
            '"%s" % (\n'
            '    "trailing comma",\n'
            ')\n',
            '"{}".format(\n'
            '    "trailing comma",\n'
            ')\n',
        ),
        # dict
        ('"%(k)s" % {"k": "v"}', '"{k}".format(k="v")'),
        ('"%(to_list)s" % {"to_list": []}', '"{to_list}".format(to_list=[])'),
        # \N escapes
        (
            r'"%s \N{snowman}" % (a,)',
            r'"{} \N{snowman}".format(a)',
        ),
        (
            r'"%(foo)s \N{snowman}" % {"foo": 1}',
            r'"{foo} \N{snowman}".format(foo=1)',
        ),
    ),
)
def test_percent_format(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.xfail
@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        # currently the approach does not attempt to consider joined strings
        (
            'paren_continue = (\n'
            '    "foo %s "\n'
            '    "bar %s" % (x, y)\n'
            ')\n',
            'paren_continue = (\n'
            '    "foo {} "\n'
            '    "bar {}".format(x, y)\n'
            ')\n',
        ),
        (
            'paren_string = (\n'
            '    "foo %s "\n'
            '    "bar %s"\n'
            ') % (x, y)\n',
            'paren_string = (\n'
            '    "foo {} "\n'
            '    "bar {}"\n'
            ').format(x, y)\n',
        ),
        (
            'paren_continue = (\n'
            '    "foo %(foo)s "\n'
            '    "bar %(bar)s" % {"foo": x, "bar": y}\n'
            ')\n',
            'paren_continue = (\n'
            '    "foo {foo} "\n'
            '    "bar {bar}".format(foo=x, bar=y)\n'
            ')\n',
        ),
        (
            'paren_string = (\n'
            '    "foo %(foo)s "\n'
            '    "bar %(bar)s"\n'
            ') % {"foo": x, "bar": y}\n',
            'paren_string = (\n'
            '    "foo {foo} "\n'
            '    "bar {bar}"\n'
            ').format(foo=x, bar=y)\n',
        ),
    ),
)
def test_percent_format_todo(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/set_literals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # Don't touch empty set literals
        'set()',
        # Don't touch weird looking function calls -- use autopep8 or such
        # first
        'set ((1, 2))',
        pytest.param(
            'f"{set((1, 2))}"',
            id='set directly inside f-string placeholder',
        ),
        pytest.param(
            'f"{set(x for x in y)}"',
            id='set comp directly inside f-string placeholder',
        ),
    ),
)
def test_fix_sets_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        # Take a set literal with an empty tuple / list and remove the arg
        ('set(())', 'set()'),
        ('set([])', 'set()'),
        pytest.param('set (())', 'set ()', id='empty, weird ws'),
        # Remove spaces in empty set literals
        ('set(( ))', 'set()'),
        # Some "normal" test cases
        ('set((1, 2))', '{1, 2}'),
        ('set([1, 2])', '{1, 2}'),
        ('set(x for x in y)', '{x for x in y}'),
        ('set([x for x in y])', '{x for x in y}'),
        # These are strange cases -- the ast doesn't tell us about the parens
        # here so we have to parse ourselves
        ('set((x for x in y))', '{x for x in y}'),
        ('set(((1, 2)))', '{1, 2}'),
        # The ast also doesn't tell us about the start of the tuple in this
        # generator expression
        ('set((a, b) for a, b in y)', '{(a, b) for a, b in y}'),
        # The ast also doesn't tell us about the start of the tuple for
        # tuple of tuples
        ('set(((1, 2), (3, 4)))', '{(1, 2), (3, 4)}'),
        # Lists where the first element is a tuple also gives the ast trouble
        # The first element lies about the offset of the element
        ('set([(1, 2), (3, 4)])', '{(1, 2), (3, 4)}'),
        (
            'set(\n'
            '    [(1, 2)]\n'
            ')',
            '{\n'
            '    (1, 2)\n'
            '}',
        ),
        ('set([((1, 2)), (3, 4)])', '{((1, 2)), (3, 4)}'),
        # And it gets worse
        ('set((((1, 2),),))', '{((1, 2),)}'),
        # Some multiline cases
        ('set(\n(1, 2))', '{\n1, 2}'),
        ('set((\n1,\n2,\n))\n', '{\n1,\n2,\n}\n'),
        # Nested sets
        (
            'set((frozenset(set((1, 2))), frozenset(set((3, 4)))))',
            '{frozenset({1, 2}), frozenset({3, 4})}',
        ),
        # Remove trailing commas on inline things
        ('set((1,))', '{1}'),
        ('set((1, ))', '{1}'),
        # Remove trailing commas after things
        ('set([1, 2, 3,],)', '{1, 2, 3}'),
        ('set((x for x in y),)', '{x for x in y}'),
        (
            'set(\n'
            '    (x for x in y),\n'
            ')',
            '{\n'
            '    x for x in y\n'
            '}',
        ),
        (
            'set(\n'
            '    [\n'
            '        99, 100,\n'
            '    ],\n'
            ')\n',
            '{\n'
            '        99, 100,\n'
            '}\n',
        ),
        pytest.param('set((\n))', 'set()', id='empty literal with newline'),
        pytest.param(
            'set((f"{x}(",))',
            '{f"{x}("}',
            id='3.12 fstring containing open brace',
        ),
        pytest.param(
            'set((f"{x})",))',
            '{f"{x})"}',
            id='3.12 fstring containing close brace',
        ),
    ),
)
def test_sets(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/shlex_join_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'from shlex import quote\n'
            '" ".join(quote(arg) for arg in cmd)\n',
            (3, 8),
            id='quote from-imported',
        ),
        pytest.param(
            'import shlex\n'
            '"wat".join(shlex.quote(arg) for arg in cmd)\n',
            (3, 8),
            id='not joined with space',
        ),
        pytest.param(
            'import shlex\n'
            '" ".join(shlex.quote(arg) for arg in cmd)\n',
            (3, 7),
            id='3.8+ feature',
        ),
    ),
)
def test_shlex_join_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import shlex\n'
            '" ".join(shlex.quote(arg) for arg in cmd)\n',

            'import shlex\n'
            'shlex.join(cmd)\n',

            id='generator expression',
        ),
        pytest.param(
            'import shlex\n'
            '" ".join([shlex.quote(arg) for arg in cmd])\n',

            'import shlex\n'
            'shlex.join(cmd)\n',

            id='list comprehension',
        ),
        pytest.param(
            'import shlex\n'
            '" ".join([shlex.quote(arg) for arg in cmd],)\n',

            'import shlex\n'
            'shlex.join(cmd)\n',

            id='removes trailing comma',
        ),
        pytest.param(
            'import shlex\n'
            '" ".join([shlex.quote(arg) for arg in ["a", "b", "c"]],)\n',

            'import shlex\n'
            'shlex.join(["a", "b", "c"])\n',

            id='more complicated iterable',
        ),
    ),
)
def test_shlex_join_fixes(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 8))) == expected
```

## File: `tests/features/six_b_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # non-ascii bytestring
        'print(six.b("£"))',
        # extra whitespace
        'print(six.b(   "123"))',
        # cannot determine args to rewrite them
        'six.b(*a)',
    ),
)
def test_six_b_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'six.b("123")',
            'b"123"',
        ),
        (
            'six.b(r"123")',
            'br"123"',
        ),
        (
            r'six.b("\x12\xef")',
            r'b"\x12\xef"',
        ),
        (
            'six.ensure_binary("foo")',
            'b"foo"',
        ),
        (
            'from six import b\n\n' r'b("\x12\xef")',
            'from six import b\n\n' r'b"\x12\xef"',
        ),
    ),
)
def test_six_b(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/six_remove_decorators_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            '@six.python_2_unicode_compatible\n'
            'class C: pass',

            'class C: pass',
        ),
        (
            '@six.python_2_unicode_compatible\n'
            '@other_decorator\n'
            'class C: pass',

            '@other_decorator\n'
            'class C: pass',
        ),
        pytest.param(
            '@  six.python_2_unicode_compatible\n'
            'class C: pass\n',

            'class C: pass\n',

            id='weird spacing at the beginning python_2_unicode_compatible',
        ),
        (
            'from six import python_2_unicode_compatible\n'
            '@python_2_unicode_compatible\n'
            'class C: pass',

            'from six import python_2_unicode_compatible\n'
            'class C: pass',
        ),
    ),
)
def test_fix_six_remove_decorators(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/six_simple_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # renaming things for weird reasons
        'from six import MAXSIZE as text_type\n'
        'isinstance(s, text_type)\n',
        # parenthesized part of attribute
        '(\n'
        '    six\n'
        ').text_type(u)\n',
        pytest.param(
            'from .six import text_type\n'
            'isinstance("foo", text_type)\n',
            id='relative import might not be six',
        ),
        pytest.param(
            'foo.range(3)',
            id='Range, but not from six.moves',
        ),
    ),
)
def test_six_simple_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'isinstance(s, six.text_type)',
            'isinstance(s, str)',
        ),
        pytest.param(
            'isinstance(s, six   .    string_types)',
            'isinstance(s, str)',
            id='weird spacing on six.attr',
        ),
        (
            'isinstance(s, six.string_types)',
            'isinstance(s, str)',
        ),
        (
            'issubclass(tp, six.string_types)',
            'issubclass(tp, str)',
        ),
        (
            'STRING_TYPES = six.string_types',
            'STRING_TYPES = (str,)',
        ),
        (
            'from six import string_types\n'
            'isinstance(s, string_types)\n',

            'from six import string_types\n'
            'isinstance(s, str)\n',
        ),
        (
            'from six import string_types\n'
            'STRING_TYPES = string_types\n',

            'from six import string_types\n'
            'STRING_TYPES = (str,)\n',
        ),
        pytest.param(
            'six.moves.range(3)\n',

            'range(3)\n',

            id='six.moves.range',
        ),
        pytest.param(
            'six.moves.xrange(3)\n',

            'range(3)\n',

            id='six.moves.xrange',
        ),
        pytest.param(
            'from six.moves import xrange\n'
            'xrange(3)\n',

            'from six.moves import xrange\n'
            'range(3)\n',

            id='six.moves.xrange, from import',
        ),
    ),
)
def test_fix_six_simple(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/six_test.py`
```python
from __future__ import annotations

import sys

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # syntax error
        'x = (',
        # unrelated
        'from os import path',
        'from six import moves',
        'a[0]()',
        # unrelated decorator
        '@mydec\n'
        'class C: pass',
        # don't rewrite things that would become `raise` in non-statements
        'print(six.raise_from(exc, exc_from))',
        # intentionally not handling this case due to it being a bug (?)
        'class C(six.with_metaclass(Meta, B), D): pass',
        # cannot determine args to rewrite them
        'six.reraise(*err)', 'six.u(*a)',
        'six.reraise(a, b, tb=c)',
        'class C(six.with_metaclass(*a)): pass',
        '@six.add_metaclass(*a)\n'
        'class C: pass\n',
        # next is shadowed
        'next()',
        ('traceback.format_exc(*sys.exc_info())'),
        pytest.param('six.iteritems()', id='wrong argument count'),
        pytest.param(
            'from six import iteritems as items\n'
            'items(foo)\n',
            id='ignore as renaming',
        ),
    ),
)
def test_fix_six_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'six.byte2int(b"f")',
            'b"f"[0]',
        ),
        (
            'six.get_unbound_function(meth)\n',
            'meth\n',
        ),
        (
            'from six import get_unbound_function\n'
            'get_unbound_function(meth)\n',

            'from six import get_unbound_function\n'
            'meth\n',
        ),
        (
            'six.indexbytes(bs, i)\n',
            'bs[i]\n',
        ),
        (
            'six.assertCountEqual(\n'
            '   self,\n'
            '   arg1,\n'
            '   arg2,\n'
            ')',

            'self.assertCountEqual(\n'
            '   arg1,\n'
            '   arg2,\n'
            ')',
        ),
        (
            'six.assertCountEqual(\n'
            '   self,\\\n'
            '   arg1,\n'
            '   arg2,\n'
            ')',

            'self.assertCountEqual(\\\n'
            '   arg1,\n'
            '   arg2,\n'
            ')',
        ),
        (
            'six.assertCountEqual(\n'
            '   self,  # hello\n'
            '   arg1,\n'
            '   arg2,\n'
            ')',

            'self.assertCountEqual(\n'
            '   arg1,\n'
            '   arg2,\n'
            ')',
        ),
        (
            'six.assertCountEqual(\n'
            '   self,\n'
            '   arg1,\n'
            '   (1, 2, 3),\n'
            ')',

            'self.assertCountEqual(\n'
            '   arg1,\n'
            '   (1, 2, 3),\n'
            ')',
        ),
        pytest.param(
            'six.u ("bar")',
            '"bar"',
            id='weird spacing six.u',
        ),
        pytest.param(
            'from six import u\nu ("bar")',
            'from six import u\n"bar"',
            id='weird spacing u',
        ),
        (
            'six.raise_from(exc, exc_from)\n',
            'raise exc from exc_from\n',
        ),
        pytest.param(
            'six.raise_from(\n'
            '    e,\n'
            '    f,\n'
            ')',

            'raise e from f',

            id='six raise_from across multiple lines',
        ),
        (
            'six.reraise(tp, exc, tb)\n',
            'raise exc.with_traceback(tb)\n',
        ),
        (
            'six.reraise(tp, exc)\n',
            'raise exc.with_traceback(None)\n',
        ),
        (
            'six.reraise(*sys.exc_info())\n',
            'raise\n',
        ),
        (
            'from sys import exc_info\n'
            'six.reraise(*exc_info())\n',

            'from sys import exc_info\n'
            'raise\n',
        ),
        (
            'from six import raise_from\n'
            'raise_from(exc, exc_from)\n',

            'from six import raise_from\n'
            'raise exc from exc_from\n',
        ),
        (
            'six.reraise(\n'
            '   tp,\n'
            '   exc,\n'
            '   tb,\n'
            ')\n',
            'raise exc.with_traceback(tb)\n',
        ),
        pytest.param(
            'six.raise_from (exc, exc_from)',
            'raise exc from exc_from',
            id='weird spacing six.raise_from',
        ),
        pytest.param(
            'from six import raise_from\nraise_from (exc, exc_from)',
            'from six import raise_from\nraise exc from exc_from',
            id='weird spacing raise_from',
        ),
        (
            'class C(six.with_metaclass(M)): pass',

            'class C(metaclass=M): pass',
        ),
        (
            'class C(six.with_metaclass(M, B)): pass',

            'class C(B, metaclass=M): pass',
        ),
        (
            'class C(six.with_metaclass(M, B1, B2)): pass',

            'class C(B1, B2, metaclass=M): pass',
        ),
        (
            'from six import with_metaclass\n'
            'class C(with_metaclass(M, B)): pass\n',

            'from six import with_metaclass\n'
            'class C(B, metaclass=M): pass\n',
        ),
        pytest.param(
            'class C(six.with_metaclass (M, B)): pass',
            'class C(B, metaclass=M): pass',
            id='weird spacing six.with_metaclass',
        ),
        pytest.param(
            'from six import with_metaclass\n'
            'class C(with_metaclass (M, B)): pass',

            'from six import with_metaclass\n'
            'class C(B, metaclass=M): pass',

            id='weird spacing with_metaclass',
        ),
        pytest.param(
            'from six import with_metaclass\n'
            'class C(with_metaclass(M, object)): pass',

            'from six import with_metaclass\n'
            'class C(metaclass=M): pass',

            id='elide object base in with_metaclass',
        ),
        pytest.param(
            'class C(six.with_metaclass(M, B,)): pass',

            'class C(B, metaclass=M): pass',

            id='with_metaclass and trailing comma',
        ),
        pytest.param(
            '@six.add_metaclass(M)\n'
            'class C: pass\n',

            'class C(metaclass=M): pass\n',

            id='basic six.add_metaclass',
        ),
        pytest.param(
            'from six import add_metaclass\n'
            '@add_metaclass(M)\n'
            'class C: pass\n',

            'from six import add_metaclass\n'
            'class C(metaclass=M): pass\n',

            id='basic add_metaclass',
        ),
        pytest.param(
            '@six.add_metaclass(M)\n'
            'class C(): pass\n',

            'class C(metaclass=M): pass\n',

            id='basic six.add_metaclass, no bases but parens',
        ),
        pytest.param(
            '@six.add_metaclass(M)\n'
            'class C(A): pass\n',

            'class C(A, metaclass=M): pass\n',

            id='add_metaclass, one base',
        ),
        pytest.param(
            '@six.add_metaclass(M)\n'
            'class C(\n'
            '    A,\n'
            '): pass\n',

            'class C(\n'
            '    A, metaclass=M,\n'
            '): pass\n',

            id='add_metaclass, base with trailing comma',
        ),
        pytest.param(
            'x = (object,)\n'
            '@six.add_metaclass(M)\n'
            'class C(x[:][0]): pass\n',

            'x = (object,)\n'
            'class C(x[:][0], metaclass=M): pass\n',

            id='add_metaclass, weird base that contains a :',
        ),
        pytest.param(
            'if True:\n'
            '    @six.add_metaclass(M)\n'
            '    class C: pass\n',

            'if True:\n'
            '    class C(metaclass=M): pass\n',

            id='add_metaclass, indented',
        ),
        pytest.param(
            '@six.add_metaclass(M)\n'
            '@unrelated(f"class{x}")\n'
            'class C: pass\n',

            '@unrelated(f"class{x}")\n'
            'class C(metaclass=M): pass\n',

            id='add_metaclass, 3.12: fstring between add_metaclass and class',
        ),
        pytest.param(
            'print(six.itervalues({1:2}))\n',
            'print({1:2}.values())\n',
            id='six.itervalues',
        ),
        pytest.param(
            'print(next(six.itervalues({1:2})))\n',
            'print(next(iter({1:2}.values())))\n',
            id='six.itervalues inside next(...)',
        ),
        pytest.param(
            'for _ in six.itervalues({} or y): pass',
            'for _ in ({} or y).values(): pass',
            id='needs parenthesizing for BoolOp',
        ),
        pytest.param(
            'for _ in six.itervalues({} | y): pass',
            'for _ in ({} | y).values(): pass',
            id='needs parenthesizing for BinOp',
        ),
        pytest.param(
            'six.int2byte(x | y)',
            'bytes((x | y,))',
            id='no parenthesize for int2byte BinOP',
        ),
        pytest.param(
            'six.iteritems(+weird_dct)',
            '(+weird_dct).items()',
            id='needs parenthesizing for UnaryOp',
        ),
        pytest.param(
            'x = six.get_method_function(lambda: x)',
            'x = (lambda: x).__func__',
            id='needs parenthesizing for Lambda',
        ),
        pytest.param(
            'for _ in six.itervalues(x if 1 else y): pass',
            'for _ in (x if 1 else y).values(): pass',
            id='needs parenthesizing for IfExp',
        ),
        # this one is bogus / impossible, but parenthesize it anyway
        pytest.param(
            'six.itervalues(x for x in y)',
            '(x for x in y).values()',
            id='needs parentehsizing for GeneratorExp',
        ),
        pytest.param(
            'async def f():\n'
            '    return six.iteritems(await y)\n',
            'async def f():\n'
            '    return (await y).items()\n',
            id='needs parenthesizing for Await',
        ),
        # this one is bogus / impossible, but parenthesize it anyway
        pytest.param(
            'six.itervalues(x < y)',
            '(x < y).values()',
            id='needs parentehsizing for Compare',
        ),
        pytest.param(
            'x = six.itervalues(\n'
            '    # comment\n'
            '    x\n'
            ')',
            'x = (\n'
            '    # comment\n'
            '    x\n'
            ').values()',
            id='multiline first argument with comment',
        ),
        pytest.param(
            'x = six.itervalues(\n'
            '    # comment\n'
            '    x,\n'
            ')',
            # TODO: ideally this would preserve whitespace better
            'x = (\n'
            '    # comment\n'
            '    x).values()',
            id='multiline first argument with comment, trailing comma',
        ),
        pytest.param(
            'x = six.moves.map(str, ints)\n',
            'x = map(str, ints)\n',
            id='six.moves builtin attrs',
        ),
        pytest.param(
            'for _ in six.itervalues(x := y): pass',
            'for _ in (x := y).values(): pass',
            id='needs parenthesizing for NamedExpr',
        ),
    ),
)
def test_fix_six(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'import six\n\nclass C(six.Iterator): pass',
            'import six\n\nclass C: pass',
        ),
        (
            'from six import Iterator\n'
            '\n'
            'class C(Iterator): pass',
            'from six import Iterator\n'
            '\n'
            'class C: pass',
        ),
        (
            'import six\n'
            '\n'
            'class C(\n'
            '    six.Iterator,\n'
            '): pass',
            'import six\n'
            '\n'
            'class C: pass',
        ),
        (
            'class C(object, six.Iterator): pass',
            'class C: pass',
        ),
        (
            'class C(six.Iterator, metaclass=ABCMeta): pass',
            'class C(metaclass=ABCMeta): pass',
        ),
        (
            'class C(six.Iterator, object, metaclass=ABCMeta): pass',
            'class C(metaclass=ABCMeta): pass',
        ),
        (
            'from six import Iterator\n'
            '\n'
            'class C(Iterator, metaclass=ABCMeta): pass',
            'from six import Iterator\n'
            '\n'
            'class C(metaclass=ABCMeta): pass',
        ),
    ),
)
def test_fix_base_classes(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.xfail(sys.version_info < (3, 12), reason='3.12+ feature')
def test_rewriting_in_fstring():
    ret = _fix_plugins('f"{six.text_type}"', settings=Settings())
    assert ret == 'f"{str}"'
```

## File: `tests/features/super_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_plugins
from pyupgrade._main import Settings


@pytest.mark.parametrize(
    's',
    (
        # syntax error
        'x(',

        'class C(Base):\n'
        '    def f(self):\n'
        '        super().f()\n',

        # super class doesn't match class name
        'class C(Base):\n'
        '    def f(self):\n'
        '        super(Base, self).f()\n',
        'class Outer:\n'  # common nesting
        '    class C(Base):\n'
        '        def f(self):\n'
        '            super(C, self).f()\n',
        'class Outer:\n'  # higher levels of nesting
        '    class Inner:\n'
        '        class C(Base):\n'
        '            def f(self):\n'
        '                super(Inner.C, self).f()\n',
        'class Outer:\n'  # super arg1 nested in unrelated name
        '    class C(Base):\n'
        '        def f(self):\n'
        '            super(some_module.Outer.C, self).f()\n',

        # super outside of a class (technically legal!)
        'def f(self):\n'
        '    super(C, self).f()\n',

        # super used in a comprehension
        'class C(Base):\n'
        '    def f(self):\n'
        '        return [super(C, self).f() for _ in ()]\n',
        'class C(Base):\n'
        '    def f(self):\n'
        '        return {super(C, self).f() for _ in ()}\n',
        'class C(Base):\n'
        '    def f(self):\n'
        '        return (super(C, self).f() for _ in ())\n',
        'class C(Base):\n'
        '    def f(self):\n'
        '        return {True: super(C, self).f() for _ in ()}\n',
        # nested comprehension
        'class C(Base):\n'
        '    def f(self):\n'
        '        return [\n'
        '            (\n'
        '                [_ for _ in ()],\n'
        '                super(C, self).f(),\n'
        '            )\n'
        '            for _ in ()'
        '        ]\n',
        # super in a closure
        'class C(Base):\n'
        '    def f(self):\n'
        '        def g():\n'
        '            super(C, self).f()\n'
        '        g()\n',
        'class C(Base):\n'
        '    def f(self):\n'
        '        g = lambda: super(C, self).f()\n'
        '        g()\n',
    ),
)
def test_fix_super_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'class C(Base):\n'
            '    def f(self):\n'
            '        super(C, self).f()\n',
            'class C(Base):\n'
            '    def f(self):\n'
            '        super().f()\n',
        ),
        (
            'class C(Base):\n'
            '    def f(self):\n'
            '        super (C, self).f()\n',
            'class C(Base):\n'
            '    def f(self):\n'
            '        super().f()\n',
        ),
        (
            'class Outer:\n'
            '    class C(Base):\n'
            '        def f(self):\n'
            '            super (Outer.C, self).f()\n',
            'class Outer:\n'
            '    class C(Base):\n'
            '        def f(self):\n'
            '            super().f()\n',
        ),
        (
            'def f():\n'
            '    class Outer:\n'
            '        class C(Base):\n'
            '            def f(self):\n'
            '                super(Outer.C, self).f()\n',
            'def f():\n'
            '    class Outer:\n'
            '        class C(Base):\n'
            '            def f(self):\n'
            '                super().f()\n',
        ),
        (
            'class A:\n'
            '    class B:\n'
            '        class C:\n'
            '            def f(self):\n'
            '                super(A.B.C, self).f()\n',
            'class A:\n'
            '    class B:\n'
            '        class C:\n'
            '            def f(self):\n'
            '                super().f()\n',
        ),
        (
            'class C(Base):\n'
            '    f = lambda self: super(C, self).f()\n',
            'class C(Base):\n'
            '    f = lambda self: super().f()\n',
        ),
        (
            'class C(Base):\n'
            '    @classmethod\n'
            '    def f(cls):\n'
            '        super(C, cls).f()\n',
            'class C(Base):\n'
            '    @classmethod\n'
            '    def f(cls):\n'
            '        super().f()\n',
        ),
        pytest.param(
            'class C:\n'
            '    async def foo(self):\n'
            '        super(C, self).foo()\n',

            'class C:\n'
            '    async def foo(self):\n'
            '        super().foo()\n',

            id='async def super',
        ),
    ),
)
def test_fix_super(s, expected):
    assert _fix_plugins(s, settings=Settings()) == expected
```

## File: `tests/features/type_of_primitive_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'type(None)\n',
            id='NoneType',
        ),
        pytest.param(
            'type(...)\n',
            id='ellipsis',
        ),
        pytest.param(
            'foo = "foo"\n'
            'type(foo)\n',
            id='String assigned to variable',
        ),
    ),
)
def test_fix_type_of_primitive_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'type("")\n',

            'str\n',

            id='Empty string -> str',
        ),
        pytest.param(
            'type(0)\n',

            'int\n',

            id='zero -> int',
        ),
        pytest.param(
            'type(0.)\n',

            'float\n',

            id='decimal zero -> float',
        ),
        pytest.param(
            'type(0j)\n',

            'complex\n',

            id='0j -> complex',
        ),
        pytest.param(
            'type(b"")\n',

            'bytes\n',

            id='Empty bytes string -> bytes',
        ),
        pytest.param(
            'type(True)\n',

            'bool\n',

            id='bool',
        ),
    ),
)
def test_fix_type_of_primitive(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/typing_classes_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        '',

        pytest.param(
            'from typing import NamedTuple as wat\n'
            'C = wat("C", ("a", int))\n',
            id='currently not following as imports',
        ),

        pytest.param('C = typing.NamedTuple("C", ())', id='no types'),
        pytest.param('C = typing.NamedTuple("C")', id='not enough args'),
        pytest.param(
            'C = typing.NamedTuple("C", (), nonsense=1)',
            id='namedtuple with named args',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", {"foo": int, "bar": str})',
            id='namedtuple without a list/tuple',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [["a", str], ["b", int]])',
            id='namedtuple without inner tuples',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [(), ()])',
            id='namedtuple but inner tuples are incorrect length',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [(not_a_str, str)])',
            id='namedtuple but attribute name is not a string',
        ),

        pytest.param(
            'C = typing.NamedTuple("C", [("def", int)])',
            id='uses keyword',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [("not-ok", int)])',
            id='uses non-identifier',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", *types)',
            id='NamedTuple starargs',
        ),
        pytest.param(
            'from .typing import NamedTuple\n'
            'C = NamedTuple("C", [("a", int)])\n',
            id='relative imports',
        ),
    ),
)
def test_typing_named_tuple_noop(s):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from typing import NamedTuple\n'
            'C = NamedTuple("C", [("a", int), ("b", str)])\n',

            'from typing import NamedTuple\n'
            'class C(NamedTuple):\n'
            '    a: int\n'
            '    b: str\n',
            id='typing from import',
        ),
        pytest.param(
            'import typing\n'
            'C = typing.NamedTuple("C", [("a", int), ("b", str)])\n',

            'import typing\n'
            'class C(typing.NamedTuple):\n'
            '    a: int\n'
            '    b: str\n',

            id='import typing',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [("a", List[int])])',

            'class C(typing.NamedTuple):\n'
            '    a: List[int]',

            id='generic attribute types',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [("a", Mapping[int, str])])',

            'class C(typing.NamedTuple):\n'
            '    a: Mapping[int, str]',

            id='generic attribute types with multi types',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [("a", "Queue[int]")])',

            'class C(typing.NamedTuple):\n'
            "    a: 'Queue[int]'",

            id='quoted type names',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [("a", Tuple[int, ...])])',

            'class C(typing.NamedTuple):\n'
            '    a: Tuple[int, ...]',

            id='type with ellipsis',
        ),
        pytest.param(
            'C = typing.NamedTuple("C", [("a", Callable[[Any], None])])',

            'class C(typing.NamedTuple):\n'
            '    a: Callable[[Any], None]',

            id='type containing a list',
        ),
        pytest.param(
            'if False:\n'
            '    pass\n'
            'C = typing.NamedTuple("C", [("a", int)])\n',

            'if False:\n'
            '    pass\n'
            'class C(typing.NamedTuple):\n'
            '    a: int\n',

            id='class directly after block',
        ),
        pytest.param(
            'if True:\n'
            '    C = typing.NamedTuple("C", [("a", int)])\n',

            'if True:\n'
            '    class C(typing.NamedTuple):\n'
            '        a: int\n',

            id='indented',
        ),
        pytest.param(
            'if True:\n'
            '    ...\n'
            '    C = typing.NamedTuple("C", [("a", int)])\n',

            'if True:\n'
            '    ...\n'
            '    class C(typing.NamedTuple):\n'
            '        a: int\n',

            id='indented, but on next line',
        ),
        pytest.param(
            # mypy treats Tuple[int] and Tuple[int,] the same so in practice
            # preserving this doesn't really matter
            'C = typing.NamedTuple("C", [("a", Tuple[int,])])',

            'class C(typing.NamedTuple):\n'
            '    a: Tuple[int,]',

            id='actually a tuple in generic argument',
        ),
        pytest.param(
            'from typing import NamedTuple\n'
            'C = NamedTuple(  # 1\n'
            '    # 2\n'
            '    "C",  # 3\n'
            '    # 4\n'
            '    [("x", "int")],  # 5\n'
            '    # 6\n'
            ')  # 7\n',

            'from typing import NamedTuple\n'
            'class C(NamedTuple):\n'
            '    # 1\n'
            '    # 2\n'
            '    # 3\n'
            '    # 4\n'
            "    x: 'int'  # 5\n"
            '    # 6\n'
            '    # 7\n',

            id='preserves comments in all positions',
        ),
        pytest.param(
            'from typing import NamedTuple, Optional\n'
            'DeferredNode = NamedTuple(\n'
            '    "DeferredNode",\n'
            '    [\n'
            '        ("active_typeinfo", Optional[int]),  # this member (and\n'
            '                                             # its semantics)\n'
            '    ]\n'
            ')\n',

            'from typing import NamedTuple, Optional\n'
            'class DeferredNode(NamedTuple):\n'
            '    active_typeinfo: Optional[int]  # this member (and\n'
            '    # its semantics)\n',

            id='preserves comments without alignment',
        ),
        pytest.param(
            'from typing import NamedTuple\n'
            'Foo = NamedTuple("Foo", [("union", str | None)])',

            'from typing import NamedTuple\n'
            'class Foo(NamedTuple):\n'
            '    union: str | None',

            id='BitOr unparse error',
        ),
    ),
)
def test_fix_typing_named_tuple(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == expected


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'from wat import TypedDict\n'
            'Q = TypedDict("Q")\n',
            id='from imported from elsewhere',
        ),
        pytest.param('D = typing.TypedDict("D")', id='no typed kwargs'),
        pytest.param('D = typing.TypedDict("D", {})', id='no typed args'),
        pytest.param('D = typing.TypedDict("D", {}, a=int)', id='both'),
        pytest.param('D = typing.TypedDict("D", 1)', id='not a dict'),
        pytest.param(
            'D = typing.TypedDict("D", {1: str})',
            id='key is not a string',
        ),
        pytest.param(
            'D = typing.TypedDict("D", {"a-b": str})',
            id='key is not an identifier',
        ),
        pytest.param(
            'D = typing.TypedDict("D", {"class": str})',
            id='key is a keyword',
        ),
        pytest.param(
            'D = typing.TypedDict("D", {**d, "a": str})',
            id='dictionary splat operator',
        ),
        pytest.param(
            'C = typing.TypedDict("C", *types)',
            id='starargs',
        ),
        pytest.param(
            'D = typing.TypedDict("D", **types)',
            id='starstarkwargs',
        ),
        pytest.param(
            'D = typing.TypedDict("D", x=int, total=False)',
            id='kw_typed_dict with total',
        ),
    ),
)
def test_typing_typed_dict_noop(s):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from typing import TypedDict\n'
            'D = TypedDict("D", a=int)\n',

            'from typing import TypedDict\n'
            'class D(TypedDict):\n'
            '    a: int\n',

            id='keyword TypedDict from imported',
        ),
        pytest.param(
            'import typing\n'
            'D = typing.TypedDict("D", a=int)\n',

            'import typing\n'
            'class D(typing.TypedDict):\n'
            '    a: int\n',

            id='keyword TypedDict from attribute',
        ),
        pytest.param(
            'import typing\n'
            'D = typing.TypedDict("D", {"a": int})\n',

            'import typing\n'
            'class D(typing.TypedDict):\n'
            '    a: int\n',

            id='TypedDict from dict literal',
        ),
        pytest.param(
            'import typing\n'
            'D = typing.TypedDict("D", {"a": typing.Literal["b", b"c"]})\n',

            'import typing\n'
            'class D(typing.TypedDict):\n'
            "    a: typing.Literal['b', b'c']\n",

            id='with Literal of bytes',
        ),
        pytest.param(
            'import typing\n'
            'D = typing.TypedDict("D", {"a": int}, total=False)\n',

            'import typing\n'
            'class D(typing.TypedDict, total=False):\n'
            '    a: int\n',

            id='TypedDict from dict literal with total',
        ),
        pytest.param(
            'import typing\n'
            'D = typing.TypedDict("D", {\n'
            '    # first comment\n'
            '    "a": int,  # inline comment\n'
            '    # second comment\n'
            '    "b": str,\n'
            '    # third comment\n'
            '}, total=False)\n',

            'import typing\n'
            'class D(typing.TypedDict, total=False):\n'
            '    # first comment\n'
            '    a: int  # inline comment\n'
            '    # second comment\n'
            '    b: str\n'
            '    # third comment\n',

            id='preserves comments',
        ),
        pytest.param(
            'from typing_extensions import TypedDict\n'
            'D = TypedDict("D", a=int)\n',

            'from typing_extensions import TypedDict\n'
            'class D(TypedDict):\n'
            '    a: int\n',

            id='keyword TypedDict from typing_extensions',
        ),
        pytest.param(
            'import typing_extensions\n'
            'D = typing_extensions.TypedDict("D", {"a": int})\n',

            'import typing_extensions\n'
            'class D(typing_extensions.TypedDict):\n'
            '    a: int\n',

            id='dict TypedDict from typing_extensions',
        ),
        pytest.param(
            'import typing_extensions\n'
            'D = typing_extensions.TypedDict("D", {"a": int}, total=True)\n',

            'import typing_extensions\n'
            'class D(typing_extensions.TypedDict, total=True):\n'
            '    a: int\n',

            id='keyword TypedDict from typing_extensions, with total',
        ),
        pytest.param(
            'from typing import List\n'
            'from typing_extensions import TypedDict\n'
            'Foo = TypedDict("Foo", {"lsts": List[List[int]]})',

            'from typing import List\n'
            'from typing_extensions import TypedDict\n'
            'class Foo(TypedDict):\n'
            '    lsts: List[List[int]]',

            id='index unparse error',
        ),
        pytest.param(
            'import typing\n'
            'if True:\n'
            '    if False:\n'
            '        pass\n'
            '    D = typing.TypedDict("D", a=int)\n',

            'import typing\n'
            'if True:\n'
            '    if False:\n'
            '        pass\n'
            '    class D(typing.TypedDict):\n'
            '        a: int\n',

            id='right after a dedent',
        ),
        pytest.param(
            'from typing import TypedDict\n'
            'Foo = TypedDict("Foo", {"union": str | int | None})',

            'from typing import TypedDict\n'
            'class Foo(TypedDict):\n'
            '    union: str | int | None',

            id='BitOr unparse error',
        ),
    ),
)
def test_typing_typed_dict(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == expected
```

## File: `tests/features/typing_pep563_test.py`
```python
from __future__ import annotations

import sys

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'from typing import Literal\n'
            'x: "str"\n',
            id='missing __future__ import',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Literal["foo", "bar"]\n',
            id='Literal',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x = TypeVar("x", "str")\n',
            id='TypeVar',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x = cast(x, "str")\n',
            id='cast',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'X = List["MyClass"]\n',
            id='Alias',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'X: MyCallable("X")\n',
            id='Custom callable',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'def foo(x, *args, **kwargs): ...\n',
            id='Untyped',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'def foo(*, inplace): ...\n',
            id='Kwonly, untyped',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Annotated[1:2] = ...\n',
            id='Annotated with invalid slice',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'def f[X](x: X) -> X: return x\n',
            id='TypeVar without bound',
        ),
    ),
)
def test_fix_typing_pep563_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from __future__ import annotations\n'
            'def foo(var: "MyClass") -> "MyClass":\n'
            '   x: "MyClass"\n',

            'from __future__ import annotations\n'
            'def foo(var: MyClass) -> MyClass:\n'
            '   x: MyClass\n',

            id='Simple annotation',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'async def foo(var: "MyClass") -> "MyClass":\n'
            '   ...\n',

            'from __future__ import annotations\n'
            'async def foo(var: MyClass) -> MyClass:\n'
            '   ...\n',

            id='simple async annotation',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'def foo(*, inplace: "bool"): ...\n',

            'from __future__ import annotations\n'
            'def foo(*, inplace: bool): ...\n',

            id='Kwonly, typed',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'def foo(*args: "str", **kwargs: "int"): ...\n',

            'from __future__ import annotations\n'
            'def foo(*args: str, **kwargs: int): ...\n',

            id='Vararg and kwarg typed',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Tuple["MyClass"]\n',

            'from __future__ import annotations\n'
            'x: Tuple[MyClass]\n',

            id='Tuple',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Callable[["MyClass"], None]\n',

            'from __future__ import annotations\n'
            'x: Callable[[MyClass], None]\n',

            id='List within Callable',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'class Foo(NamedTuple):\n'
            '    x: "MyClass"\n',

            'from __future__ import annotations\n'
            'class Foo(NamedTuple):\n'
            '    x: MyClass\n',

            id='Inherit from NamedTuple',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'class D(TypedDict):\n'
            '    E: TypedDict("E", foo="int", total=False)\n',

            'from __future__ import annotations\n'
            'class D(TypedDict):\n'
            '    E: TypedDict("E", foo=int, total=False)\n',

            id='TypedDict keyword syntax',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'class D(TypedDict):\n'
            '    E: TypedDict("E", {"foo": "int"})\n',

            'from __future__ import annotations\n'
            'class D(TypedDict):\n'
            '    E: TypedDict("E", {"foo": int})\n',

            id='TypedDict dict syntax',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'class D(typing.TypedDict):\n'
            '    E: typing.TypedDict("E", {"foo": "int"})\n',

            'from __future__ import annotations\n'
            'class D(typing.TypedDict):\n'
            '    E: typing.TypedDict("E", {"foo": int})\n',

            id='typing.TypedDict',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'class D(TypedDict):\n'
            '    E: TypedDict("E")\n',

            'from __future__ import annotations\n'
            'class D(TypedDict):\n'
            '    E: TypedDict("E")\n',

            id='TypedDict no type (invalid syntax)',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Annotated["str", "metadata"]\n',

            'from __future__ import annotations\n'
            'x: Annotated[str, "metadata"]\n',

            id='Annotated',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: typing.Annotated["str", "metadata"]\n',

            'from __future__ import annotations\n'
            'x: typing.Annotated[str, "metadata"]\n',

            id='typing.Annotated',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Annotated[()]\n',

            'from __future__ import annotations\n'
            'x: Annotated[()]\n',

            id='Empty Annotated (garbage)',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: Arg("str", "name")\n',

            'from __future__ import annotations\n'
            'x: Arg(str, "name")\n',

            id='Arg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: DefaultArg("str", "name")\n',

            'from __future__ import annotations\n'
            'x: DefaultArg(str, "name")\n',

            id='DefaultArg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedArg("str", "name")\n',

            'from __future__ import annotations\n'
            'x: NamedArg(str, "name")\n',

            id='NamedArg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: DefaultNamedArg("str", "name")\n',

            'from __future__ import annotations\n'
            'x: DefaultNamedArg(str, "name")\n',

            id='DefaultNamedArg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: DefaultNamedArg("str", name="name")\n',

            'from __future__ import annotations\n'
            'x: DefaultNamedArg(str, name="name")\n',

            id='DefaultNamedArg with one keyword argument',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: DefaultNamedArg(name="name", type="str")\n',

            'from __future__ import annotations\n'
            'x: DefaultNamedArg(name="name", type=str)\n',

            id='DefaultNamedArg with keyword arguments',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: DefaultNamedArg(name="name", quox="str")\n',

            'from __future__ import annotations\n'
            'x: DefaultNamedArg(name="name", quox="str")\n',

            id='DefaultNamedArg with invalid arguments',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: DefaultNamedArg(name="name")\n',

            'from __future__ import annotations\n'
            'x: DefaultNamedArg(name="name")\n',

            id='DefaultNamedArg with no type (invalid syntax)',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: VarArg("str")\n',

            'from __future__ import annotations\n'
            'x: VarArg(str)\n',

            id='VarArg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: List[List[List["MyClass"]]]\n',

            'from __future__ import annotations\n'
            'x: List[List[List[MyClass]]]\n',

            id='Nested',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedTuple("X", [("foo", "int"), ("bar", "str")])\n',

            'from __future__ import annotations\n'
            'x: NamedTuple("X", [("foo", int), ("bar", str)])\n',

            id='NamedTuple with types, no kwarg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedTuple("X", fields=[("foo", "int"), ("bar", "str")])\n',

            'from __future__ import annotations\n'
            'x: NamedTuple("X", fields=[("foo", int), ("bar", str)])\n',

            id='NamedTuple with types, one kwarg',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedTuple(typename="X", fields=[("foo", "int")])\n',

            'from __future__ import annotations\n'
            'x: NamedTuple(typename="X", fields=[("foo", int)])\n',

            id='NamedTuple with types, two kwargs',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedTuple("X", [("foo",), ("bar",)])\n',

            'from __future__ import annotations\n'
            'x: NamedTuple("X", [("foo",), ("bar",)])\n',

            id='NamedTuple with length-1 tuples (invalid syntax)',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedTuple("X", ["foo", "bar"])\n',

            'from __future__ import annotations\n'
            'x: NamedTuple("X", ["foo", "bar"])\n',

            id='NamedTuple with missing types (invalid syntax)',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: NamedTuple()\n',

            'from __future__ import annotations\n'
            'x: NamedTuple()\n',

            id='NamedTuple with no args (invalid syntax)',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'def foo(var0, /, var1: "MyClass") -> "MyClass":\n'
            '   x: "MyClass"\n',

            'from __future__ import annotations\n'
            'def foo(var0, /, var1: MyClass) -> MyClass:\n'
            '   x: MyClass\n',

            id='posonly args',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'x: (\n'
            '    "int | "\n'
            '    "str"\n'
            ')\n',

            'from __future__ import annotations\n'
            'x: (\n'
            '    int | str\n'
            ')\n',

            id='multiline implicit-concat annotation',
        ),
    ),
)
def test_fix_typing_pep563(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 7)))
    assert ret == expected


def test_fixes_in_py314():
    src = 'def f(x: "X") -> "Y": pass\n'
    expected = 'def f(x: X) -> Y: pass\n'
    ret = _fix_plugins(src, settings=Settings(min_version=(3, 14)))
    assert ret == expected


@pytest.mark.xfail(sys.version_info < (3, 12), reason='3.12+ syntax')
def test_typevar_bound():
    src = '''\
from __future__ import annotations
def f[T: "int"](t: T) -> T:
    return t
'''
    expected = '''\
from __future__ import annotations
def f[T: int](t: T) -> T:
    return t
'''
    ret = _fix_plugins(src, settings=Settings())
    assert ret == expected
```

## File: `tests/features/typing_pep585_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'x = lambda foo: None',
            (3, 9),
            id='lambdas do not have type annotations',
        ),
        pytest.param(
            'from typing import List\n'
            'x: List[int]\n',
            (3, 8),
            id='not python 3.9+',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import List\n'
            'SomeAlias = List[int]\n',
            (3, 8),
            id='not in a type annotation context',
        ),
        pytest.param(
            'from typing import Union\n'
            'x: Union[int, str]\n',
            (3, 9),
            id='not a PEP 585 type',
        ),
    ),
)
def test_fix_generic_types_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


def test_noop_keep_runtime_typing():
    s = '''\
from __future__ import annotations
from typing import List
def f(x: List[str]) -> None: ...
'''
    assert _fix_plugins(s, settings=Settings(keep_runtime_typing=True)) == s


def test_keep_runtime_typing_ignored_in_py39():
    s = '''\
from __future__ import annotations
from typing import List
def f(x: List[str]) -> None: ...
'''
    expected = '''\
from __future__ import annotations
from typing import List
def f(x: list[str]) -> None: ...
'''
    settings = Settings(min_version=(3, 9), keep_runtime_typing=True)
    assert _fix_plugins(s, settings=settings) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from typing import List\n'
            'x: List[int]\n',

            'from typing import List\n'
            'x: list[int]\n',

            id='from import of List',
        ),
        pytest.param(
            'import typing\n'
            'x: typing.List[int]\n',

            'import typing\n'
            'x: list[int]\n',

            id='import of typing + typing.List',
        ),
        pytest.param(
            'from typing import List\n'
            'SomeAlias = List[int]\n',
            'from typing import List\n'
            'SomeAlias = list[int]\n',
            id='not in a type annotation context',
        ),
    ),
)
def test_fix_generic_types(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 9)))
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import List\n'
            'x: List[int]\n',

            'from __future__ import annotations\n'
            'from typing import List\n'
            'x: list[int]\n',

            id='variable annotations',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import List\n'
            'def f(x: List[int]) -> None: ...\n',

            'from __future__ import annotations\n'
            'from typing import List\n'
            'def f(x: list[int]) -> None: ...\n',

            id='argument annotations',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import List\n'
            'def f() -> List[int]: ...\n',

            'from __future__ import annotations\n'
            'from typing import List\n'
            'def f() -> list[int]: ...\n',

            id='return annotations',
        ),
    ),
)
def test_fix_generic_types_future_annotations(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/typing_pep604_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'from typing import Union\n'
            'x: Union[int, str]\n',
            (3, 9),
            id='<3.10 Union',
        ),
        pytest.param(
            'from typing import Optional\n'
            'x: Optional[str]\n',
            (3, 9),
            id='<3.10 Optional',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Union\n'
            'SomeAlias = Union[int, str]\n',
            (3, 9),
            id='<3.9 not in a type annotation context',
        ),
        # https://github.com/python/mypy/issues/9945
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Union\n'
            'SomeAlias = Union[int, str]\n',
            (3, 10),
            id='3.10+ not in a type annotation context',
        ),
        # https://github.com/python/mypy/issues/9998
        pytest.param(
            'from typing import Union\n'
            'def f() -> Union[()]: ...\n',
            (3, 10),
            id='3.10+ empty Union',
        ),
        # https://github.com/asottile/pyupgrade/issues/567
        pytest.param(
            'from typing import Optional\n'
            'def f() -> Optional["str"]: ...\n',
            (3, 10),
            id='3.10+ Optional of forward reference',
        ),
        pytest.param(
            'from typing import Union\n'
            'def f() -> Union[int, "str"]: ...\n',
            (3, 10),
            id='3.10+ Union of forward reference',
        ),
        pytest.param(
            'from typing import Union\n'
            'def f() -> Union[1:2]: ...\n',
            (3, 10),
            id='invalid Union slicing',
        ),
    ),
)
def test_fix_pep604_types_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


def test_noop_keep_runtime_typing():
    s = '''\
from __future__ import annotations
from typing import Union
def f(x: Union[int, str]) -> None: ...
'''
    assert _fix_plugins(s, settings=Settings(keep_runtime_typing=True)) == s


def test_keep_runtime_typing_ignored_in_py310():
    s = '''\
from __future__ import annotations
from typing import Union
def f(x: Union[int, str]) -> None: ...
'''
    expected = '''\
from __future__ import annotations
from typing import Union
def f(x: int | str) -> None: ...
'''
    settings = Settings(min_version=(3, 10), keep_runtime_typing=True)
    assert _fix_plugins(s, settings=settings) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from typing import Union\n'
            'x: Union[int, str]\n',

            'from typing import Union\n'
            'x: int | str\n',

            id='Union rewrite',
        ),
        pytest.param(
            'x: typing.Union[int]\n',

            'x: int\n',

            id='Union of only one value',
        ),
        pytest.param(
            'x: typing.Union[Foo[str, int], str]\n',

            'x: Foo[str, int] | str\n',

            id='Union containing a value with brackets',
        ),
        pytest.param(
            'x: typing.Union[typing.List[str], str]\n',

            'x: list[str] | str\n',

            id='Union containing pep585 rewritten type',
        ),
        pytest.param(
            'x: typing.Union[int, str,]\n',

            'x: int | str\n',

            id='Union trailing comma',
        ),
        pytest.param(
            'x: typing.Union[(int, str)]\n',

            'x: int | str\n',

            id='Union, parenthesized tuple',
        ),
        pytest.param(
            'x: typing.Union[\n'
            '    int,\n'
            '    str\n'
            ']\n',

            'x: (\n'
            '    int |\n'
            '    str\n'
            ')\n',

            id='Union multiple lines',
        ),
        pytest.param(
            'x: typing.Union[\n'
            '    int,\n'
            '    str,\n'
            ']\n',

            'x: (\n'
            '    int |\n'
            '    str\n'
            ')\n',

            id='Union multiple lines with trailing commas',
        ),
        pytest.param(
            'from typing import Optional\n'
            'x: Optional[str]\n',

            'from typing import Optional\n'
            'x: str | None\n',

            id='Optional rewrite',
        ),
        pytest.param(
            'x: typing.Optional[\n'
            '    ComplicatedLongType[int]\n'
            ']\n',

            'x: None | (\n'
            '    ComplicatedLongType[int]\n'
            ')\n',

            id='Optional rewrite multi-line',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Optional\n'
            'x: Optional["str"]\n',

            'from __future__ import annotations\n'
            'from typing import Optional\n'
            'x: str | None\n',

            id='Optional rewrite with forward reference',
        ),
        pytest.param(
            'from typing import Union, Sequence\n'
            'def f(x: Union[Union[A, B], Sequence[Union[C, D]]]): pass\n',

            'from typing import Union\n'
            'from collections.abc import Sequence\n'
            'def f(x: A | B | Sequence[C | D]): pass\n',

            id='nested unions',
        ),
        pytest.param(
            'from typing import Annotated, Union\n'
            'x: Union[str, Annotated[int, f"{x})"]]\n',

            'from typing import Annotated, Union\n'
            'x: str | Annotated[int, f"{x})"]\n',

            id='union, 3.12: ignore close brace in fstring',
        ),
        pytest.param(
            'from typing import Annotated, Union\n'
            'x: Union[str, Annotated[int, f"{x}("]]\n',

            'from typing import Annotated, Union\n'
            'x: str | Annotated[int, f"{x}("]\n',

            id='union, 3.12: ignore open brace in fstring',
        ),
        pytest.param(
            'from typing import Annotated, Optional\n'
            'x: Optional[Annotated[int, f"{x}("]]\n',

            'from typing import Annotated, Optional\n'
            'x: Annotated[int, f"{x}("] | None\n',

            id='optional, 3.12: ignore open brace in fstring',
        ),
        pytest.param(
            'from typing import Annotated, Optional\n'
            'x: Optional[Annotated[int, f"{x})"]]\n',

            'from typing import Annotated, Optional\n'
            'x: Annotated[int, f"{x})"] | None\n',

            id='optional, 3.12: ignore close brace in fstring',
        ),
    ),
)
def test_fix_pep604_types(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 10))) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Union\n'
            'x: Union[int, str]\n',

            'from __future__ import annotations\n'
            'from typing import Union\n'
            'x: int | str\n',

            id='variable annotations',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Union\n'
            'def f(x: Union[int, str]) -> None: ...\n',

            'from __future__ import annotations\n'
            'from typing import Union\n'
            'def f(x: int | str) -> None: ...\n',

            id='argument annotations',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Union\n'
            'def f() -> Union[int, str]: ...\n',

            'from __future__ import annotations\n'
            'from typing import Union\n'
            'def f() -> int | str: ...\n',

            id='return annotations',
        ),
    ),
)
def test_fix_generic_types_future_annotations(s, expected):
    assert _fix_plugins(s, settings=Settings()) == expected


# TODO: test multi-line as well
```

## File: `tests/features/typing_pep646_unpack_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s',),
    (
        pytest.param(
            'from typing import Unpack\n'
            'foo(Unpack())',
            id='Not a subscript',
        ),
        pytest.param(
            'from typing import TypeVarTuple, Unpack\n'
            'Shape = TypeVarTuple("Shape")\n'
            'class Foo(Unpack[Shape]):\n'
            '    pass',
            id='Not inside a subscript',
        ),
        pytest.param(
            'from typing import Unpack\n'
            'from typing import TypedDict\n'
            'class D(TypedDict):\n'
            '    x: int\n'
            'def f(**kwargs: Unpack[D]) -> None: pass\n',
            id='3.12 TypedDict for kwargs',
        ),
    ),
)
def test_fix_pep646_noop(s):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 11))) == s
    assert _fix_plugins(s, settings=Settings(min_version=(3, 10))) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'from typing import Generic, TypeVarTuple, Unpack\n'
            "Shape = TypeVarTuple('Shape')\n"
            'class C(Generic[Unpack[Shape]]):\n'
            '    pass',

            'from typing import Generic, TypeVarTuple, Unpack\n'
            "Shape = TypeVarTuple('Shape')\n"
            'class C(Generic[*Shape]):\n'
            '    pass',
        ),
        (
            'from typing import Generic, TypeVarTuple, Unpack\n'
            "Shape = TypeVarTuple('Shape')\n"
            'class C(Generic[Unpack  [Shape]]):\n'
            '    pass',

            'from typing import Generic, TypeVarTuple, Unpack\n'
            "Shape = TypeVarTuple('Shape')\n"
            'class C(Generic[*Shape]):\n'
            '    pass',
        ),
        pytest.param(
            'from typing import Unpack\n'
            'def f(*args: Unpack[tuple[int, ...]]): pass\n',

            'from typing import Unpack\n'
            'def f(*args: *tuple[int, ...]): pass\n',

            id='Unpack for *args',
        ),
    ),
)
def test_typing_unpack(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 11))) == expected
    assert _fix_plugins(s, settings=Settings(min_version=(3, 10))) == s
```

## File: `tests/features/typing_pep696_typevar_defaults_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'from collections.abc import Generator\n'
            'def f() -> Generator[int, None, None]: yield 1\n',
            (3, 12),
            id='not 3.13+, no __future__.annotations',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from collections.abc import Generator\n'
            'def f() -> Generator[int]: yield 1\n',
            (3, 12),
            id='already converted!',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from collections.abc import Generator\n'
            'def f() -> Generator[int, int, None]: yield 1\n'
            'def g() -> Generator[int, int, int]: yield 1\n',
            (3, 12),
            id='non-None send/return type',
        ),
    ),
)
def test_fix_pep696_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


def test_fix_pep696_noop_keep_runtime_typing():
    settings = Settings(min_version=(3, 12), keep_runtime_typing=True)
    s = '''\
from __future__ import annotations
from collections.abc import Generator
def f() -> Generator[int, None, None]: yield 1
'''
    assert _fix_plugins(s, settings=settings) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from __future__ import annotations\n'
            'from typing import Generator\n'
            'def f() -> Generator[int, None, None]: yield 1\n',

            'from __future__ import annotations\n'
            'from collections.abc import Generator\n'
            'def f() -> Generator[int]: yield 1\n',

            id='typing.Generator',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from typing_extensions import Generator\n'
            'def f() -> Generator[int, None, None]: yield 1\n',

            'from __future__ import annotations\n'
            'from typing_extensions import Generator\n'
            'def f() -> Generator[int]: yield 1\n',

            id='typing_extensions.Generator',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from collections.abc import Generator\n'
            'def f() -> Generator[int, None, None]: yield 1\n',

            'from __future__ import annotations\n'
            'from collections.abc import Generator\n'
            'def f() -> Generator[int]: yield 1\n',

            id='collections.abc.Generator',
        ),
        pytest.param(
            'from __future__ import annotations\n'
            'from collections.abc import AsyncGenerator\n'
            'async def f() -> AsyncGenerator[int, None]: yield 1\n',

            'from __future__ import annotations\n'
            'from collections.abc import AsyncGenerator\n'
            'async def f() -> AsyncGenerator[int]: yield 1\n',

            id='collections.abc.AsyncGenerator',
        ),
    ),
)
def test_fix_pep696_with_future_annotations(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 12))) == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from collections.abc import Generator\n'
            'def f() -> Generator[int, None, None]: yield 1\n',

            'from collections.abc import Generator\n'
            'def f() -> Generator[int]: yield 1\n',

            id='Generator',
        ),
        pytest.param(
            'from collections.abc import AsyncGenerator\n'
            'async def f() -> AsyncGenerator[int, None]: yield 1\n',

            'from collections.abc import AsyncGenerator\n'
            'async def f() -> AsyncGenerator[int]: yield 1\n',

            id='AsyncGenerator',
        ),
    ),
)
def test_fix_pep696_with_3_13(s, expected):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 13))) == expected
```

## File: `tests/features/typing_text_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'class Text: ...\n'
            'text = Text()\n',
            id='not a type annotation',
        ),
    ),
)
def test_fix_typing_text_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'from typing import Text\n'
            'x: Text\n',

            'from typing import Text\n'
            'x: str\n',

            id='from import of Text',
        ),
        pytest.param(
            'import typing\n'
            'x: typing.Text\n',

            'import typing\n'
            'x: str\n',

            id='import of typing + typing.Text',
        ),
        pytest.param(
            'from typing import Text\n'
            'SomeAlias = Text\n',
            'from typing import Text\n'
            'SomeAlias = str\n',
            id='not in a type annotation context',
        ),
    ),
)
def test_fix_typing_text(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/unicode_literals_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._main import _fix_tokens


@pytest.mark.parametrize(
    's',
    (
        pytest.param('(', id='syntax errors are unchanged'),
        # Regression: string containing newline
        pytest.param('"""with newline\n"""', id='string containing newline'),
        pytest.param(
            'def f():\n'
            '    return"foo"\n',
            id='Regression: no space between return and string',
        ),
    ),
)
def test_unicode_literals_noop(s):
    assert _fix_tokens(s) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param("u''", "''", id='it removes u prefix'),
    ),
)
def test_unicode_literals(s, expected):
    assert _fix_tokens(s) == expected
```

## File: `tests/features/unittest_aliases_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'class ExampleTests:\n'
            '    def test_something(self):\n'
            '        self.assertEqual(1, 1)\n',
            id='not a deprecated alias',
        ),
        'unittest.makeSuite(Tests, "arg")',
        'unittest.makeSuite(Tests, prefix="arg")',
    ),
)
def test_fix_unittest_aliases_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'class ExampleTests:\n'
            '    def test_something(self):\n'
            '        self.assertEquals(1, 1)\n',

            'class ExampleTests:\n'
            '    def test_something(self):\n'
            '        self.assertEqual(1, 1)\n',
        ),
        (
            'class ExampleTests:\n'
            '    def test_something(self):\n'
            '        self.assertNotEquals(1, 2)\n',

            'class ExampleTests:\n'
            '    def test_something(self):\n'
            '        self.assertNotEqual(1, 2)\n',
        ),
    ),
)
def test_fix_unittest_aliases(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'unittest.findTestCases(MyTests)',
            'unittest.defaultTestLoader.loadTestsFromModule(MyTests)',
        ),
        (
            'unittest.makeSuite(MyTests)',
            'unittest.defaultTestLoader.loadTestsFromTestCase(MyTests)',
        ),
        (
            'unittest.getTestCaseNames(MyTests)',
            'unittest.defaultTestLoader.getTestCaseNames(MyTests)',
        ),
    ),
)
def test_fix_unittest_aliases_py311(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 11)))
    assert ret == expected
```

## File: `tests/features/universal_newlines_to_text_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    ('s', 'version'),
    (
        pytest.param(
            'import subprocess\n'
            'subprocess.run(["foo"], universal_newlines=True)\n',
            (3,),
            id='not Python3.7+',
        ),
        pytest.param(
            'from foo import run\n'
            'run(["foo"], universal_newlines=True)\n',
            (3, 7),
            id='run imported, but not from subprocess',
        ),
        pytest.param(
            'from subprocess import run\n'
            'run(["foo"], shell=True)\n',
            (3, 7),
            id='universal_newlines not used',
        ),
        pytest.param(
            'import subprocess\n'
            'subprocess.run(\n'
            '   ["foo"],\n'
            '   text=True,\n'
            '   universal_newlines=True\n'
            ')\n',
            (3, 7),
            id='both text and universal_newlines',
        ),
        pytest.param(
            'import subprocess\n'
            'subprocess.run(\n'
            '   ["foo"],\n'
            '   universal_newlines=True,\n'
            '   **kwargs,\n'
            ')\n',
            (3, 7),
            id='both **kwargs and universal_newlines',
        ),
    ),
)
def test_fix_universal_newlines_to_text_noop(s, version):
    assert _fix_plugins(s, settings=Settings(min_version=version)) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import subprocess\n'
            'subprocess.run(["foo"], universal_newlines=True)\n',

            'import subprocess\n'
            'subprocess.run(["foo"], text=True)\n',

            id='subprocess.run attribute',
        ),
        pytest.param(
            'import subprocess\n'
            'subprocess.check_output(["foo"], universal_newlines=True)\n',

            'import subprocess\n'
            'subprocess.check_output(["foo"], text=True)\n',

            id='subprocess.check_output attribute',
        ),
        pytest.param(
            'from subprocess import run\n'
            'run(["foo"], universal_newlines=True)\n',

            'from subprocess import run\n'
            'run(["foo"], text=True)\n',

            id='run imported from subprocess',
        ),
        pytest.param(
            'from subprocess import run\n'
            'run(["foo"], universal_newlines=universal_newlines)\n',

            'from subprocess import run\n'
            'run(["foo"], text=universal_newlines)\n',

            id='universal_newlines appears as value',
        ),
        pytest.param(
            'from subprocess import run\n'
            'run(["foo"], *foo, universal_newlines=universal_newlines)\n',

            'from subprocess import run\n'
            'run(["foo"], *foo, text=universal_newlines)\n',

            id='with starargs',
        ),
    ),
)
def test_fix_universal_newlines_to_text(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 7)))
    assert ret == expected
```

## File: `tests/features/unpack_list_comprehension_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        pytest.param(
            'foo = [fn(x) for x in items]',
            id='assignment to single variable',
        ),
        pytest.param(
            'x, = [await foo for foo in bar]',
            id='async comprehension',
        ),
    ),
)
def test_fix_typing_text_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'foo, bar, baz = [fn(x) for x in items]\n',

            'foo, bar, baz = (fn(x) for x in items)\n',

            id='single-line assignment',
        ),
        pytest.param(
            'foo, bar, baz = [[i for i in fn(x)] for x in items]\n',

            'foo, bar, baz = ([i for i in fn(x)] for x in items)\n',

            id='nested list comprehension',
        ),
        pytest.param(
            'foo, bar, baz = [\n'
            '    fn(x)\n'
            '    for x in items\n'
            ']\n',

            'foo, bar, baz = (\n'
            '    fn(x)\n'
            '    for x in items\n'
            ')\n',

            id='multi-line assignment',
        ),
    ),
)
def test_fix_typing_text(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected
```

## File: `tests/features/versioned_branches_test.py`
```python
from __future__ import annotations

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins


@pytest.mark.parametrize(
    's',
    (
        # skip `if` without `else` as it could cause a SyntaxError
        'if True:\n'
        '    if six.PY2:\n'
        '        pass\n',
        pytest.param(
            'if six.PY2:\n'
            '    2\n'
            'else:\n'
            '    if False:\n'
            '        3\n',
            id='py2 indistinguisable at ast level from `elif`',
        ),
        pytest.param(
            'if six.PY3:\n'
            '    3\n'
            'else:\n'
            '    if False:\n'
            '        2\n',
            id='py3 indistinguisable at ast level from `elif`',
        ),
        # don't rewrite version compares with not 3.0 compares
        'if sys.version_info >= (3, 6):\n'
        '    3.6\n'
        'else:\n'
        '    3.5\n',
        # don't try and think about `sys.version`
        'from sys import version\n'
        'if sys.version[0] > "2":\n'
        '    3\n'
        'else:\n'
        '    2\n',
        pytest.param(
            'from .sys import version_info\n'
            'if version_info < (3,):\n'
            '    print("2")\n'
            'else:\n'
            '    print("3")\n',
            id='relative imports',
        ),
    ),
)
def test_fix_py2_block_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'if six.PY2:\n'
            '    print("py2")\n'
            'else:\n'
            '    print("py3")\n',

            'print("py3")\n',

            id='six.PY2',
        ),
        pytest.param(
            'if six.PY2:\n'
            '    if True:\n'
            '        print("py2!")\n'
            '    else:\n'
            '        print("???")\n'
            'else:\n'
            '    print("py3")\n',

            'print("py3")\n',

            id='six.PY2, nested ifs',
        ),
        pytest.param(
            'if six.PY2: print("PY2!")\n'
            'else:       print("PY3!")\n',

            'print("PY3!")\n',

            id='six.PY2, oneline',
        ),
        pytest.param(
            'if six.PY2: print("PY2!")\n'
            'else:       print("PY3!")',

            'print("PY3!")',

            id='six.PY2, oneline, no newline at end of file',
        ),
        pytest.param(
            'if True:\n'
            '    if six.PY2:\n'
            '        print("PY2")\n'
            '    else:\n'
            '        print("PY3")\n',

            'if True:\n'
            '    print("PY3")\n',

            id='six.PY2, indented',
        ),
        pytest.param(
            'if six.PY2: print(1 if True else 3)\n'
            'else:\n'
            '   print("py3")\n',

            'print("py3")\n',

            id='six.PY2, `else` token inside oneline if\n',
        ),
        pytest.param(
            'if six.PY2:\n'
            '    def f():\n'
            '        print("py2")\n'
            'else:\n'
            '    def f():\n'
            '        print("py3")\n',

            'def f():\n'
            '    print("py3")\n',

            id='six.PY2, multiple indents in block',
        ),
        pytest.param(
            'if not six.PY2:\n'
            '    print("py3")\n'
            'else:\n'
            '    print("py2")\n'
            '\n'
            '\n'
            'x = 1\n',

            'print("py3")\n'
            '\n'
            '\n'
            'x = 1\n',

            id='not six.PY2, remove second block',
        ),
        pytest.param(
            'if not six.PY2:\n'
            '    print("py3")\n'
            'else:\n'
            '    print("py2")',

            'print("py3")\n',

            id='not six.PY2, no end of line',
        ),
        pytest.param(
            'if not six.PY2:\n'
            '    print("py3")\n'
            'else:\n'
            '    print("py2")\n'
            '    # ohai\n'
            '\n'
            'x = 1\n',

            'print("py3")\n'
            '\n'
            'x = 1\n',

            id='not six.PY2: else block ends in comment',
        ),
        pytest.param(
            'if not six.PY2: print("py3")\n'
            'else: print("py2")\n',

            'print("py3")\n',

            id='not six.PY2, else is single line',
        ),
        pytest.param(
            'if six.PY3:\n'
            '    print("py3")\n'
            'else:\n'
            '    print("py2")\n',

            'print("py3")\n',

            id='six.PY3',
        ),
        pytest.param(
            'if True:\n'
            '    if six.PY3:\n'
            '        print("py3")\n'
            '    else:\n'
            '        print("py2")\n',

            'if True:\n'
            '    print("py3")\n',

            id='indented six.PY3',
        ),
        pytest.param(
            'from six import PY3\n'
            'if not PY3:\n'
            '    print("py2")\n'
            'else:\n'
            '    print("py3")\n',

            'from six import PY3\n'
            'print("py3")\n',

            id='not PY3',
        ),
        pytest.param(
            'def f():\n'
            '    if six.PY2:\n'
            '        try:\n'
            '            yield\n'
            '        finally:\n'
            '            pass\n'
            '    else:\n'
            '        yield\n',

            'def f():\n'
            '    yield\n',

            id='six.PY2, finally',
        ),
        pytest.param(
            'class C:\n'
            '    def g():\n'
            '        pass\n'
            '\n'
            '    if six.PY2:\n'
            '        def f(py2):\n'
            '            pass\n'
            '    else:\n'
            '        def f(py3):\n'
            '            pass\n'
            '\n'
            '    def h():\n'
            '        pass\n',

            'class C:\n'
            '    def g():\n'
            '        pass\n'
            '\n'
            '    def f(py3):\n'
            '        pass\n'
            '\n'
            '    def h():\n'
            '        pass\n',

            id='six.PY2 in class\n',
        ),
        pytest.param(
            'if True:\n'
            '    if six.PY2:\n'
            '        2\n'
            '    else:\n'
            '        3\n'
            '\n'
            '    # comment\n',

            'if True:\n'
            '    3\n'
            '\n'
            '    # comment\n',

            id='six.PY2, comment after',
        ),
        pytest.param(
            'if six.PY2:\n'
            '    def f():\n'
            '        print("py2")\n'
            '    def g():\n'
            '        print("py2")\n'
            'else:\n'
            '    def f():\n'
            '        print("py3")\n'
            '    def g():\n'
            '        print("py3")\n',

            'def f():\n'
            '    print("py3")\n'
            'def g():\n'
            '    print("py3")\n',

            id='six.PY2 multiple functions',
        ),
        pytest.param(
            'if True:\n'
            '    if six.PY3:\n'
            '        3\n'
            '    else:\n'
            '        2\n'
            '\n'
            '    # comment\n',

            'if True:\n'
            '    3\n'
            '\n'
            '    # comment\n',

            id='six.PY3, comment after',
        ),
        pytest.param(
            'if sys.version_info == 2:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info == 2',
        ),
        pytest.param(
            'if sys.version_info[0] == 2:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info[0] == 2',
        ),
        pytest.param(
            'if sys.version_info[0] < 3:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info[0] < 3',
        ),
        pytest.param(
            'if sys.version_info.major == 2:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info.major == 2',
        ),
        pytest.param(
            'if sys.version_info.major < 3:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info.major < 3',
        ),
        pytest.param(
            'if sys.version_info < (3,):\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info < (3,)',
        ),
        pytest.param(
            'if sys.version_info < (3, 0):\n'
            '    2\n'
            'else:\n'
            '    3\n',

            '3\n',

            id='sys.version_info < (3, 0)',
        ),
        pytest.param(
            'if sys.version_info == 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='sys.version_info == 3',
        ),
        pytest.param(
            'if sys.version_info > (3,):\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='sys.version_info > (3,)',
        ),
        pytest.param(
            'if sys.version_info >= (3,):\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='sys.version_info >= (3,)',
        ),
        pytest.param(
            'if sys.version_info[0] == 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='sys.version_info[0]== 3',
        ),
        pytest.param(
            'if sys.version_info[0] >= 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='sys.version_info[0] >= 3',
        ),
        pytest.param(
            'if sys.version_info.major == 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='testme sys.version_info.major == 3',
        ),
        pytest.param(
            'if sys.version_info.major >= 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            '3\n',

            id='sys.version_info.major >= 3',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info > (3,):\n'
            '    3\n'
            'else:\n'
            '    2\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, > (3,)',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info[0] == 2:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, [0] == 2',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info[0] < 3:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, [0] < 3',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info.major == 2:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, .major == 2',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info.major < 3:\n'
            '    2\n'
            'else:\n'
            '    3\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, .major < 3',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info[0] == 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, [0] == 3',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info[0] >= 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, [0] >= 3',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info.major == 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, .major == 3',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info.major >= 3:\n'
            '    3\n'
            'else:\n'
            '    2\n',

            'from sys import version_info\n'
            '3\n',

            id='from sys import version_info, .major >= 3',
        ),
        pytest.param(
            'if True:\n'
            '    print(1)\n'
            'elif six.PY2:\n'
            '    print(2)\n'
            'else:\n'
            '    print(3)\n',

            'if True:\n'
            '    print(1)\n'
            'else:\n'
            '    print(3)\n',

            id='elif six.PY2 else',
        ),
        pytest.param(
            'if True:\n'
            '    print(1)\n'
            'elif six.PY3:\n'
            '    print(3)\n'
            'else:\n'
            '    print(2)\n',

            'if True:\n'
            '    print(1)\n'
            'else:\n'
            '    print(3)\n',

            id='elif six.PY3 else',
        ),
        pytest.param(
            'if True:\n'
            '    print(1)\n'
            'elif six.PY3:\n'
            '    print(3)\n',

            'if True:\n'
            '    print(1)\n'
            'else:\n'
            '    print(3)\n',

            id='elif six.PY3 no else',
        ),
        pytest.param(
            'def f():\n'
            '    if True:\n'
            '        print(1)\n'
            '    elif six.PY3:\n'
            '        print(3)\n',

            'def f():\n'
            '    if True:\n'
            '        print(1)\n'
            '    else:\n'
            '        print(3)\n',

            id='elif six.PY3 no else, indented',
        ),
        pytest.param(
            'if True:\n'
            '    if sys.version_info > (3,):\n'
            '        print(3)\n'
            '    # comment\n'
            '    print(2+3)\n',

            'if True:\n'
            '    print(3)\n'
            '    # comment\n'
            '    print(2+3)\n',

            id='comment after dedented block',
        ),
        pytest.param(
            'print("before")\n'
            'if six.PY2:\n'
            '    pass\n'
            'print("after")\n',

            'print("before")\n'
            'print("after")\n',
            id='can remove no-else if at module scope',
        ),
        pytest.param(
            'if six.PY2:\n'
            '    pass\n'
            'elif False:\n'
            '    pass\n',

            'if False:\n'
            '    pass\n',

            id='elif becomes if',
        ),
    ),
)
def test_fix_py2_blocks(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ('if six.PY3: print(3)\n', 'print(3)\n'),
        (
            'if six.PY3:\n'
            '    print(3)\n',

            'print(3)\n',
        ),
    ),
)
def test_fix_py3_only_code(s, expected):
    ret = _fix_plugins(s, settings=Settings())
    assert ret == expected


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        pytest.param(
            'import sys\n'
            'if sys.version_info > (3, 5):\n'
            '    3+6\n'
            'else:\n'
            '    3-5\n',

            'import sys\n'
            '3+6\n',
            id='sys.version_info > (3, 5)',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info > (3, 5):\n'
            '    3+6\n'
            'else:\n'
            '    3-5\n',

            'from sys import version_info\n'
            '3+6\n',
            id='from sys import version_info, > (3, 5)',
        ),
        pytest.param(
            'import sys\n'
            'if sys.version_info >= (3, 6):\n'
            '    3+6\n'
            'else:\n'
            '    3-5\n',

            'import sys\n'
            '3+6\n',
            id='sys.version_info >= (3, 6)',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info >= (3, 6):\n'
            '    3+6\n'
            'else:\n'
            '    3-5\n',

            'from sys import version_info\n'
            '3+6\n',
            id='from sys import version_info, >= (3, 6)',
        ),
        pytest.param(
            'import sys\n'
            'if sys.version_info < (3, 6):\n'
            '    3-5\n'
            'else:\n'
            '    3+6\n',

            'import sys\n'
            '3+6\n',
            id='sys.version_info < (3, 6)',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info < (3, 6):\n'
            '    3-5\n'
            'else:\n'
            '    3+6\n',

            'from sys import version_info\n'
            '3+6\n',
            id='from sys import version_info, < (3, 6)',
        ),
        pytest.param(
            'import sys\n'
            'if sys.version_info <= (3, 5):\n'
            '    3-5\n'
            'else:\n'
            '    3+6\n',

            'import sys\n'
            '3+6\n',
            id='sys.version_info <= (3, 5)',
        ),
        pytest.param(
            'from sys import version_info\n'
            'if version_info <= (3, 5):\n'
            '    3-5\n'
            'else:\n'
            '    3+6\n',

            'from sys import version_info\n'
            '3+6\n',
            id='from sys import version_info, <= (3, 5)',
        ),
        pytest.param(
            'import sys\n'
            'if sys.version_info >= (3, 6):\n'
            '    pass',

            'import sys\n'
            'pass',
            id='sys.version_info >= (3, 6), noelse',
        ),
        pytest.param(
            'if six.PY3:\n'
            '    pass\n'
            'elif False:\n'
            '    pass\n',

            'pass\n'
            'if False:\n'
            '    pass\n',

            id='elif becomes if',
        ),
    ),
)
def test_fix_py3x_only_code(s, expected):
    ret = _fix_plugins(s, settings=Settings(min_version=(3, 6)))
    assert ret == expected


@pytest.mark.parametrize(
    's',
    (
        # both branches are still relevant in the following cases
        'import sys\n'
        'if sys.version_info > (3, 7):\n'
        '    3-6\n'
        'else:\n'
        '    3+7\n',

        'import sys\n'
        'if sys.version_info < (3, 7):\n'
        '    3-6\n'
        'else:\n'
        '    3+7\n',

        'import sys\n'
        'if sys.version_info >= (3, 7):\n'
        '    3+7\n'
        'else:\n'
        '    3-6\n',

        'import sys\n'
        'if sys.version_info <= (3, 7):\n'
        '    3-7\n'
        'else:\n'
        '    3+8\n',

        'import sys\n'
        'if sys.version_info <= (3, 6):\n'
        '    3-6\n'
        'else:\n'
        '    3+7\n',

        'import sys\n'
        'if sys.version_info > (3, 6):\n'
        '    3+7\n'
        'else:\n'
        '    3-6\n',
    ),
)
def test_fix_py3x_only_noop(s):
    assert _fix_plugins(s, settings=Settings(min_version=(3, 6))) == s
```

## File: `tests/features/yield_from_test.py`
```python
from __future__ import annotations

import ast

import pytest

from pyupgrade._data import Settings
from pyupgrade._main import _fix_plugins
from pyupgrade._plugins.legacy import _fields_same
from pyupgrade._plugins.legacy import _targets_same


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (
            'def f():\n'
            '    for x in y:\n'
            '        yield x',
            'def f():\n'
            '    yield from y\n',
        ),
        (
            'def f():\n'
            '    for x in [1, 2, 3]:\n'
            '        yield x',
            'def f():\n'
            '    yield from [1, 2, 3]\n',
        ),
        (
            'def f():\n'
            '    for x in {x for x in y}:\n'
            '        yield x',
            'def f():\n'
            '    yield from {x for x in y}\n',
        ),
        (
            'def f():\n'
            '    for x in (1, 2, 3):\n'
            '        yield x',
            'def f():\n'
            '    yield from (1, 2, 3)\n',
        ),
        (
            'def f():\n'
            '    for x, y in {3: "x", 6: "y"}:\n'
            '        yield x, y',
            'def f():\n'
            '    yield from {3: "x", 6: "y"}\n',
        ),
        (
            'def f():  # Comment one\n'
            '    # Comment two\n'
            '    for x, y in {  # Comment three\n'
            '       3: "x",  # Comment four\n'
            '       # Comment five\n'
            '       6: "y"  # Comment six\n'
            '    }:  # Comment seven\n'
            '       # Comment eight\n'
            '       yield x, y  # Comment nine\n'
            '       # Comment ten',
            'def f():  # Comment one\n'
            '    # Comment two\n'
            '    yield from {  # Comment three\n'
            '       3: "x",  # Comment four\n'
            '       # Comment five\n'
            '       6: "y"  # Comment six\n'
            '    }\n',
        ),
        (
            'def f():\n'
            '    for x, y in [{3: (3, [44, "long ss"]), 6: "y"}]:\n'
            '        yield x, y',
            'def f():\n'
            '    yield from [{3: (3, [44, "long ss"]), 6: "y"}]\n',
        ),
        (
            'def f():\n'
            '    for x, y in z():\n'
            '        yield x, y',
            'def f():\n'
            '    yield from z()\n',
        ),
        (
            'def f():\n'
            '    def func():\n'
            '        # This comment is preserved\n'
            '\n'
            '        for x, y in z():  # Comment one\n'
            '\n'
            '            # Comment two\n'
            '            yield x, y  # Comment three\n'
            '            # Comment four\n'
            '\n\n'
            '# Comment\n'
            'def g():\n'
            '    print(3)',
            'def f():\n'
            '    def func():\n'
            '        # This comment is preserved\n'
            '\n'
            '        yield from z()\n'
            '\n\n'
            '# Comment\n'
            'def g():\n'
            '    print(3)',
        ),
        (
            'async def f():\n'
            '    for x in [1, 2]:\n'
            '        yield x\n'
            '\n'
            '    def g():\n'
            '        for x in [1, 2, 3]:\n'
            '            yield x\n'
            '\n'
            '    for x in [1, 2]:\n'
            '        yield x\n'
            '\n'
            '    return g',
            'async def f():\n'
            '    for x in [1, 2]:\n'
            '        yield x\n'
            '\n'
            '    def g():\n'
            '        yield from [1, 2, 3]\n'
            '\n'
            '    for x in [1, 2]:\n'
            '        yield x\n'
            '\n'
            '    return g',
        ),
        pytest.param(
            'def f():\n'
            '    for x in y:\n'
            '        yield x\n'
            '    for z in x:\n'
            '        yield z\n',
            'def f():\n'
            '    for x in y:\n'
            '        yield x\n'
            '    yield from x\n',
            id='leave one loop alone (referenced after assignment)',
        ),
        pytest.param(
            'def f(y):\n'
            '   for x in f"{y}:":\n'
            '       yield x\n',

            'def f(y):\n'
            '   yield from f"{y}:"\n',

            id='3.12: colon in fstring',
        ),
        pytest.param(
            'def f(y):\n'
            '   for x in f"{y}(":\n'
            '       yield x\n',

            'def f(y):\n'
            '   yield from f"{y}("\n',

            id='3.12: open brace in fstring',
        ),
        pytest.param(
            'def f(y):\n'
            '   for x in f"{y})":\n'
            '       yield x\n',

            'def f(y):\n'
            '   yield from f"{y})"\n',

            id='3.13: close brace in fstring',
        ),
    ),
)
def test_fix_yield_from(s, expected):
    assert _fix_plugins(s, settings=Settings()) == expected


@pytest.mark.parametrize(
    's',
    (
        'def f():\n'
        '    for x in z:\n'
        '        yield',
        'def f():\n'
        '    for x in z:\n'
        '        yield y',
        'def f():\n'
        '    for x, y in z:\n'
        '        yield x',
        'def f():\n'
        '    for x, y in z:\n'
        '        yield y',
        'def f():\n'
        '    for a, b in z:\n'
        '        yield x, y',
        'def f():\n'
        '    for x, y in z:\n'
        '        yield y, x',
        'def f():\n'
        '    for x, y, c in z:\n'
        '        yield x, y',
        'def f():\n'
        '    for x in z:\n'
        '        x = 22\n'
        '        yield x',
        'def f():\n'
        '    for x in z:\n'
        '        yield x\n'
        '    else:\n'
        '        print("boom!")\n',
        pytest.param(
            'def f():\n'
            '    for x in range(5):\n'
            '        yield x\n'
            '    print(x)\n',
            id='variable referenced after loop',
        ),
        pytest.param(
            'def f():\n'
            '    def g():\n'
            '        print(x)\n'
            '    for x in range(5):\n'
            '        yield x\n'
            '    g()\n',
            id='variable referenced after loop, but via function',
        ),
        pytest.param(
            'def f():\n'
            '    def g():\n'
            '        def h():\n'
            '           print(x)\n'
            '        return h\n'
            '    for x in range(5):\n'
            '        yield x\n'
            '    g()()\n',
            id='variable referenced after loop, but via nested function',
        ),
        pytest.param(
            'def f(x):\n'
            '    del x\n',
            id='regression with del ctx (#306)',
        ),
    ),
)
def test_fix_yield_from_noop(s):
    assert _fix_plugins(s, settings=Settings()) == s


def test_targets_same():
    assert _targets_same(ast.parse('global a, b'), ast.parse('global a, b'))
    assert not _targets_same(ast.parse('global a'), ast.parse('global b'))


def _get_body(expr):
    body = ast.parse(expr).body[0]
    assert isinstance(body, ast.Expr)
    return body.value


def test_fields_same():
    assert not _fields_same(_get_body('x'), _get_body('1'))
```

