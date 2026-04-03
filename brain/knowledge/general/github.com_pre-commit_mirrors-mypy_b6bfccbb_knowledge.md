---
id: github.com-pre-commit-mirrors-mypy-b6bfccbb-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.569530
---

# KNOWLEDGE EXTRACT: github.com_pre-commit_mirrors-mypy_b6bfccbb
> **Extracted on:** 2026-04-01 11:42:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521477/github.com_pre-commit_mirrors-mypy_b6bfccbb

---

## File: `.pre-commit-hooks.yaml`
```yaml
-   id: mypy
    name: mypy
    description: ''
    entry: mypy
    language: python
    'types_or': [python, pyi]
    args: ["--ignore-missing-imports", "--scripts-are-modules"]
    require_serial: true
    additional_dependencies: []
    minimum_pre_commit_version: '2.9.2'
```

## File: `.version`
```
1.19.1
```

## File: `LICENSE`
```
Copyright (c) 2014 Anthony Sottile

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
mypy mirror
===========

Mirror of mypy for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit
For mypy: see https://github.com/python/mypy

### Using mypy with pre-commit:

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: mypy
```


By default, mypy will run with `mypy --ignore-missing-imports`, `pre-commit`
runs `mypy` from an isolated virtualenv so it won't have access to those.
To change the arguments, override the `args` as follows:

```yaml
    hooks:
    -   id: mypy
        args: [--strict, --ignore-missing-imports]
```

Because `pre-commit` runs `mypy` from an isolated virtualenv (without your
dependencies) you may also find it useful to add the typed dependencies to
`additional_dependencies` so `mypy` can better perform dynamic analysis:

```yaml
    hooks:
    -   id: mypy
        additional_dependencies: [tokenize-rt==3.2.0]
```

Note that using the `--install-types` is problematic. Mutating the pre-commit
environment at runtime breaks cache and will break parallel builds.
```

## File: `setup.py`
```python
from __future__ import annotations

from setuptools import setup


setup(
    name='pre_commit_placeholder_package',
    version='0.0.0',
    install_requires=['mypy==1.19.1'],
)
```

