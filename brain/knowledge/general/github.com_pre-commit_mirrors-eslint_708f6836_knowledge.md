---
id: github.com-pre-commit-mirrors-eslint-708f6836-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.550714
---

# KNOWLEDGE EXTRACT: github.com_pre-commit_mirrors-eslint_708f6836
> **Extracted on:** 2026-04-01 11:39:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521432/github.com_pre-commit_mirrors-eslint_708f6836

---

## File: `.npmignore`
```
*
```

## File: `.pre-commit-hooks.yaml`
```yaml
-   id: eslint
    name: eslint
    description: ''
    entry: eslint
    language: node
    'types': [javascript]
    args: []
    require_serial: false
    additional_dependencies: ["eslint@10.1.0"]
    minimum_pre_commit_version: '0'
```

## File: `.version`
```
10.1.0
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
eslint mirror
================

Mirror of eslint package for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For eslint: see https://github.com/eslint/eslint


### Using eslint with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: eslint
```

When using plugins with `eslint` you'll need to declare them under
`additional_dependencies`. For example:

```yaml
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: eslint
        additional_dependencies:
        -   eslint@4.15.0
        -   eslint-config-google@0.7.1
        -   eslint-loader@1.6.1
        -   eslint-plugin-react@6.10.3
        -   babel-eslint@6.1.2
```

By default only `*.js` files are taken into consideration.
If you want to use eslint on TypeScript codebases you need
to start from this template:

```yaml
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: eslint
        files: \.[jt]sx?$  # *.js, *.jsx, *.ts and *.tsx
        types: [file]
```
```

## File: `package.json`
```json
{
    "name": "placeholder_package",
    "description": "Note: double curly-braces because python .format",
    "version": "0.0.0"
}
```

