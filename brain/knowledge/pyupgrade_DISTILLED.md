---
id: pyupgrade
type: knowledge
owner: OA_Triage
---
# pyupgrade
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: setup.py
```py
from __future__ import annotations

from setuptools import setup
setup()

```

### File: .pre-commit-config.yaml
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

### File: .pre-commit-hooks.yaml
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

### File: requirements-dev.txt
```txt
covdefaults>=2.1.0
coverage
pytest

```

### File: tests\main_test.py
```py
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

### File: tests\string_helpers_test.py
```py
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

### File: tests\__init__.py
```py

```

### File: tests\features\binary_literals_test.py
```py
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

### File: tests\features\capture_output_test.py
```py
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

### File: tests\features\collections_abc_test.py
```py
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

### File: tests\features\constant_fold_test.py
```py
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

### File: tests\features\datetime_utc_alias_test.py
```py
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

### File: tests\features\defaultdict_lambda_test.py
```py
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

### File: tests\features\default_encoding_test.py
```py
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

### File: tests\features\dict_literals_test.py
```py
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

### File: tests\features\encoding_cookie_test.py
```py
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

### File: tests\features\escape_sequences_test.py
```py
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

### File: tests\features\exceptions_test.py
```py
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
