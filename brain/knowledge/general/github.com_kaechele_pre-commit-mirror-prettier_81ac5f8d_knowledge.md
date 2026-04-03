---
id: github.com-kaechele-pre-commit-mirror-prettier-81a
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:17.158958
---

# KNOWLEDGE EXTRACT: github.com_kaechele_pre-commit-mirror-prettier_81ac5f8d
> **Extracted on:** 2026-04-01 14:16:20
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523821/github.com_kaechele_pre-commit-mirror-prettier_81ac5f8d

---

## File: `.npmignore`
```
*
```

## File: `.pre-commit-hooks.yaml`
```yaml
-   id: prettier
    name: prettier
    description: ''
    entry: prettier --write --list-different --ignore-unknown
    language: node
    'types': [text]
    args: []
    require_serial: false
    additional_dependencies: ["prettier@3.8.1"]
    minimum_pre_commit_version: '0'
```

## File: `.version`
```
3.8.1
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2023 Felix Kaechele

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

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

## File: `README.md`
```markdown
# prettier mirror

Mirror of prettier package for pre-commit.

This mirror contains only stable versions.

For notes on how "stable" versions are determined see <https://github.com/kaechele/pre-commit-mirror-maker/blob/main/README.md>

For pre-commit: see <https://github.com/pre-commit/pre-commit>

For prettier: see <https://github.com/prettier/prettier>

## Using prettier with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/kaechele/pre-commit-mirror-prettier
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: prettier
```

*note*: only prettier versions >= 2.1.0 are supported

When using plugins with `prettier` you'll need to declare them under
`additional_dependencies`. For example:

```yaml
-   repo: https://github.com/kaechele/pre-commit-mirror-prettier
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: prettier
        additional_dependencies:
        -   prettier@2.1.2
        -   '@prettier/plugin-xml@0.12.0'
```

By default, all files are passed to `prettier`, if you want to limit the
file list, adjust `types` / `types_or` / `files`:

```yaml
    -   id: prettier
        types_or: [css, javascript]
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

