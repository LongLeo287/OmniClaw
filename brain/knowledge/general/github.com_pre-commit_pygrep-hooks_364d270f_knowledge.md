---
id: github.com-pre-commit-pygrep-hooks-364d270f-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.623420
---

# KNOWLEDGE EXTRACT: github.com_pre-commit_pygrep-hooks_364d270f
> **Extracted on:** 2026-04-01 09:15:42
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520062/github.com_pre-commit_pygrep-hooks_364d270f

---

## File: `.gitignore`
```
*.pyc
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
        additional_dependencies: [types-pyyaml]
-   repo: local
    hooks:
    -   id: generate-readme
        name: generate readme
        entry: ./generate-readme
        language: python
        additional_dependencies: [pyyaml]
        files: ^(\.pre-commit-hooks.yaml|generate-readme)$
        pass_filenames: false
    -   id: run-tests
        name: run tests
        entry: pytest tests
        language: python
        additional_dependencies: [pre-commit, pytest]
        always_run: true
        pass_filenames: false
```

## File: `.pre-commit-hooks.yaml`
```yaml
-   id: python-check-blanket-noqa
    name: check blanket noqa
    description: 'Enforce that `noqa` annotations always occur with specific codes. Sample annotations: `# noqa: F401`, `# noqa: F401,W203`'
    entry: '(?i)# noqa(?!: )'
    language: pygrep
    types: [python]
-   id: python-check-blanket-type-ignore
    name: check blanket type ignore
    description: 'Enforce that `# type: ignore` annotations always occur with specific codes. Sample annotations: `# type: ignore[attr-defined]`, `# type: ignore[attr-defined, name-defined]`'
    entry: '# type:? *ignore(?!\[|\w)'
    language: pygrep
    types: [python]
-   id: python-check-mock-methods
    name: check for not-real mock methods
    description: >-
        Prevent common mistakes of `assert mck.not_called()`, `assert mck.called_once_with(...)`
        and `mck.assert_called`.
    language: pygrep
    entry: >
        (?x)(
            assert .*\.(
                not_called|
                called_
            )|
            # ''.join(rf'(?<!\b{s})' for s in dir(mock) if s.endswith('Mock')))
            (?<!\bAsyncMock)(?<!\bMagicMock)(?<!\bMock)(?<!\bNonCallableMagicMock)(?<!\bNonCallableMock)(?<!\bPropertyMock)
            \.assert_(
                any_call|
                called|
                called_once|
                called_once_with|
                called_with|
                has_calls|
                not_called
            )($|[^(\w])
        )
    types: [python]
-   id: python-no-eval
    name: check for eval()
    description: 'A quick check for the `eval()` built-in function'
    entry: '\beval\('
    language: pygrep
    types: [python]
-   id: python-no-log-warn
    name: use logger.warning(
    description: 'A quick check for the deprecated `.warn()` method of python loggers'
    entry: '(?<!warnings)\.warn\('
    language: pygrep
    types: [python]
-   id: python-use-type-annotations
    name: type annotations not comments
    description: 'Enforce that python3.6+ type annotations are used instead of type comments'
    entry: '# type(?!: *ignore([^a-zA-Z0-9]|$))'
    language: pygrep
    types: [python]
-   id: rst-backticks
    name: rst ``code`` is two backticks
    description: 'Detect common mistake of using single backticks when writing rst'
    entry: '^(?!    ).*(^| )`[^`]+`([^_]|$)'
    language: pygrep
    types: [rst]
-   id: rst-directive-colons
    name: rst directives end with two colons
    description: 'Detect mistake of rst directive not ending with double colon or space before the double colon'
    entry: '^\s*\.\. [a-z]+(| | :):$'
    language: pygrep
    types: [rst]
-   id: rst-inline-touching-normal
    name: rst ``inline code`` next to normal text
    description: 'Detect mistake of inline code touching normal text in rst'
    entry: '\w``\w'
    language: pygrep
    types: [rst]
-   id: text-unicode-replacement-char
    name: no unicode replacement chars
    description: 'Forbid files which have a UTF-8 Unicode replacement character'
    entry: "\uFFFD"
    language: pygrep
    types: [text]
```

## File: `LICENSE`
```
Copyright (c) 2018 Anthony Sottile

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
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pygrep-hooks/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pygrep-hooks/main)

pygrep-hooks
============

A collection of fast, cheap, regex based pre-commit hooks.


### Adding to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/pre-commit/pygrep-hooks
    rev: v1.10.0  # Use the ref you want to point at
    hooks:
    -   id: python-use-type-annotations
    # ...
```

### Naming conventions

Where possible, these hooks will be prefixed with the file types they target.
For example, a hook which targets python will be called `python-...`.

### Provided hooks

[generated]: # (generated)
- **`python-check-blanket-noqa`**: Enforce that `noqa` annotations always occur with specific codes. Sample annotations: `# noqa: F401`, `# noqa: F401,W203`
- **`python-check-blanket-type-ignore`**: Enforce that `# type: ignore` annotations always occur with specific codes. Sample annotations: `# type: ignore[attr-defined]`, `# type: ignore[attr-defined, name-defined]`
- **`python-check-mock-methods`**: Prevent common mistakes of `assert mck.not_called()`, `assert mck.called_once_with(...)` and `mck.assert_called`.
- **`python-no-eval`**: A quick check for the `eval()` built-in function
- **`python-no-log-warn`**: A quick check for the deprecated `.warn()` method of python loggers
- **`python-use-type-annotations`**: Enforce that python3.6+ type annotations are used instead of type comments
- **`rst-backticks`**: Detect common mistake of using single backticks when writing rst
- **`rst-directive-colons`**: Detect mistake of rst directive not ending with double colon or space before the double colon
- **`rst-inline-touching-normal`**: Detect mistake of inline code touching normal text in rst
- **`text-unicode-replacement-char`**: Forbid files which have a UTF-8 Unicode replacement character
```

## File: `generate-readme`
```
#!/usr/bin/env python3
from __future__ import annotations

import yaml

Loader = getattr(yaml, 'CSafeLoader', yaml.SafeLoader)


def main() -> int:
    with open('.pre-commit-hooks.yaml') as f:
        hooks = yaml.load(f, Loader=Loader)

    with open('README.md') as f:
        contents = f.read()
    before, delim, _ = contents.partition('[generated]: # (generated)\n')

    rest = '\n'.join(
        f'- **`{hook["id"]}`**: {hook["description"]}' for hook in hooks
    )

    with open('README.md', 'w') as f:
        f.write(before + delim + rest + '\n')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `tests/hooks_test.py`
```python
from __future__ import annotations

import re

import pytest
from pre_commit.clientlib import load_manifest
from pre_commit.constants import MANIFEST_FILE

HOOKS = {h['id']: re.compile(h['entry']) for h in load_manifest(MANIFEST_FILE)}


@pytest.mark.parametrize(
    's',
    (
        'x = 1 # type: ignoreme',
        'x = 1  # type: int',
        'x = 1  # type int',
        'x = 1  # type: int  # noqa',
    ),
)
def test_python_use_type_annotations_positive(s):
    assert HOOKS['python-use-type-annotations'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'x = 1',
        'x = 1  # type:ignore',
        'x = 1  # type: ignore',
        'x = 1  # type:  ignore',
        'x = 1  # type: ignore # noqa',
        'x = 1  # type: ignore  # noqa',
        'x = 1  # type: ignore[type-mismatch]',
        'x = 1  # type: ignore=E123',
    ),
)
def test_python_use_type_annotations_negative(s):
    assert not HOOKS['python-use-type-annotations'].search(s)


@pytest.mark.parametrize(
    's',
    (
        '# noqa',
        '# NOQA',
        '# noqa:F401',
        '# noqa:F401,W203',
    ),
)
def test_python_check_blanket_noqa_positive(s):
    assert HOOKS['python-check-blanket-noqa'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'x = 1',
        '# noqa: F401',
        '# noqa: F401, W203',
    ),
)
def test_python_check_blanket_noqa_negative(s):
    assert not HOOKS['python-check-blanket-noqa'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'x = 1  # type: ignore',
        'x = 1  # type ignore',
        'x = 1  # type:ignore',
        'x = 1  # type ignore  # noqa',
    ),
)
def test_python_check_blanket_type_ignore_positive(s):
    assert HOOKS['python-check-blanket-type-ignore'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'x = 1',
        'x = 1  # type: ignore[attr-defined]',
        'x = 1  # type: ignore[attr-defined, name-defined]',
        'x = 1  # type: ignore[type-mismatch]  # noqa',
        'x = 1  # type: Union[int, str]',
        'x = 1  # type: ignoreme',
    ),
)
def test_python_check_blanket_type_ignore_negative(s):
    assert not HOOKS['python-check-blanket-type-ignore'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'assert my_mock.not_called()',
        'assert my_mock.called_once_with()',
        'my_mock.assert_not_called',
        'my_mock.assert_called',
        'my_mock.assert_called_once_with',
        'my_mock.assert_called_once_with# noqa',
        'MyMock.assert_called_once_with',
    ),
)
def test_python_check_mock_methods_positive(s):
    assert HOOKS['python-check-mock-methods'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'assert my_mock.call_count == 1',
        'assert my_mock.called',
        'my_mock.assert_not_called()',
        'my_mock.assert_called()',
        'my_mock.assert_called_once_with()',
        '"""like :meth:`Mock.assert_called_once_with`"""',
        '"""like :meth:`MagicMock.assert_called_once_with`"""',
    ),
)
def test_python_check_mock_methods_negative(s):
    assert not HOOKS['python-check-mock-methods'].search(s)


def test_python_noeval_positive():
    assert HOOKS['python-no-eval'].search('eval("3 + 4")')


def test_python_noeval_negative():
    assert not HOOKS['python-no-eval'].search('literal_eval("{1: 2}")')


@pytest.mark.parametrize(
    's',
    (
        'log.warn("this is deprecated")',
    ),
)
def test_python_no_log_warn_positive(s):
    assert HOOKS['python-no-log-warn'].search(s)


@pytest.mark.parametrize(
    's',
    (
        "warnings.warn('this is ok')",
        'log.warning("this is ok")',
        'from warnings import warn',
        'warn("by itself is also ok")',
    ),
)
def test_python_no_log_warn_negative(s):
    assert not HOOKS['python-no-log-warn'].search(s)


@pytest.mark.parametrize(
    's',
    (
        '`[code]`',
        'i like `_kitty`',
        'i like `_`',
        '`a`',
        '`cd`',
        ' `indented` literal block',
        '> quoted `literal` block',
    ),
)
def test_python_rst_backticks_positive(s):
    assert HOOKS['rst-backticks'].search(s)


@pytest.mark.parametrize(
    's',
    (
        ' ``[code]``',
        'i like _`kitty`',
        'i like `kitty`_',
        '``b``',
        '``ef``',
        '    indented `literal` block',
    ),
)
def test_python_rst_backticks_negative(s):
    assert not HOOKS['rst-backticks'].search(s)


@pytest.mark.parametrize(
    's',
    (
        '``PyMem_Realloc()`` indirectly call``PyObject_Malloc()`` and',
        'This PEP proposes that ``bytes`` and ``bytearray``gain an optimised',
        'Reading this we first see the``break``, which obviously applies to',
        'for using``long_description`` and a corresponding',
        '``inline`` normal``inline',
        '``inline``normal ``inline',
        '``inline``normal',
        '``inline``normal``inline',
        'normal ``inline``normal',
        'normal``inline`` normal',
        'normal``inline``',
        'normal``inline``normal',
    ),
)
def test_python_rst_inline_touching_normal_positive(s):
    assert HOOKS['rst-inline-touching-normal'].search(s)


@pytest.mark.parametrize(
    's',
    (
        '``PyMem_Realloc()`` indirectly call ``PyObject_Malloc()`` and',
        'This PEP proposes that ``bytes`` and ``bytearray`` gain an optimised',
        'Reading this we first see the ``break``, which obviously applies to',
        'for using ``long_description`` and a corresponding',
        '``inline`` normal ``inline',
        '``inline`` normal',
        'normal ``inline`` normal',
        'normal ``inline``',
    ),
)
def test_python_rst_inline_touching_normal_negative(s):
    assert not HOOKS['rst-inline-touching-normal'].search(s)


@pytest.mark.parametrize(
    's',
    (
        str(b'\x80abc', errors='replace'),
    ),
)
def test_text_unicode_replacement_char_positive(s):
    assert HOOKS['text-unicode-replacement-char'].search(s)


@pytest.mark.parametrize(
    's',
    (
        'foo',
    ),
)
def test_text_unicode_replacement_char_negative(s):
    assert not HOOKS['text-unicode-replacement-char'].search(s)


@pytest.mark.parametrize(
    's',
    (
        '    .. warning:',
        '.. warning:',
        '    .. warning ::',
        '.. warning ::',
        '    .. warning :',
        '.. warning :',
    ),
)
def test_rst_directive_colons_positive(s):
    assert HOOKS['rst-directive-colons'].search(s)


@pytest.mark.parametrize(
    's',
    (
        '.. warning::',
        '.. code:: python',
    ),
)
def test_rst_directive_colons_negative(s):
    assert not HOOKS['rst-directive-colons'].search(s)


def test_that_hooks_are_sorted():
    assert list(HOOKS) == sorted(HOOKS)
```

