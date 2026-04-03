---
id: pre-commit-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:01.790741
---

# KNOWLEDGE EXTRACT: pre-commit
> **Extracted on:** 2026-03-30 17:51:08
> **Source:** pre-commit

---

## File: `mirrors-eslint.md`
```markdown
# 📦 pre-commit/mirrors-eslint [🔖 PENDING/APPROVE]
🔗 https://github.com/pre-commit/mirrors-eslint


## Meta
- **Stars:** ⭐ 85 | **Forks:** 🍴 34
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Mirror of eslint node package for pre-commit.

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mirrors-mypy.md`
```markdown
# 📦 pre-commit/mirrors-mypy [🔖 PENDING/APPROVE]
🔗 https://github.com/pre-commit/mirrors-mypy


## Meta
- **Stars:** ⭐ 348 | **Forks:** 🍴 51
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Mirror of mypy for pre-commit

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pre-commit-hooks.md`
```markdown
# 📦 pre-commit/pre-commit-hooks [🔖 PENDING/APPROVE]
🔗 https://github.com/pre-commit/pre-commit-hooks


## Meta
- **Stars:** ⭐ 6431 | **Forks:** 🍴 779
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Some out-of-the-box hooks for pre-commit

## README (trích đầu)
```
[![build status](https://github.com/pre-commit/pre-commit-hooks/actions/workflows/main.yml/badge.svg)](https://github.com/pre-commit/pre-commit-hooks/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit-hooks/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit-hooks/main)

pre-commit-hooks
================

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0  # Use the ref you want to point at
    hooks:
    -   id: trailing-whitespace
    # -   id: ...
```

### Hooks available

#### `check-added-large-files`
Prevent giant files from being committed.
  - Specify what is "too large" with `args: ['--maxkb=123']` (default=500kB).
  - Limits checked files to those indicated as staged for addition by git.
  - If `git-lfs` is installed, lfs files will be skipped
    (requires `git-lfs>=2.2.1`)
  - `--enforce-all` - Check all listed files not just those staged for
    addition.

#### `check-ast`
Simply check whether files parse as valid python.

#### `check-builtin-literals`
Require literal syntax when initializing empty or zero Python builtin types.
  - Allows calling constructors with positional arguments (e.g., `list('abc')`).
  - Allows calling constructors from the `builtins` (`__builtin__`) namespace (`builtins.list()`).
  - Ignore this requirement for specific builtin types with `--ignore=type1,type2,…`.
  - Forbid `dict` keyword syntax with `--no-allow-dict-kwargs`.

#### `check-case-conflict`
Check for files with names that would conflict on a case-insensitive filesystem like MacOS HFS+ or Windows FAT.

#### `check-executables-have-shebangs`
Checks that non-binary executables have a proper shebang.

#### `check-illegal-windows-names`
Check for files that cannot be created on Windows.

#### `check-json`
Attempts to load all json files to verify syntax.

#### `check-merge-conflict`
Check for files that contain merge conflict strings.
  - `--assume-in-merge` - Allows running the hook when there is no ongoing merge operation

#### `check-shebang-scripts-are-executable`
Checks that scripts with shebangs are executable.

#### `check-symlinks`
Checks for symlinks which do not point to anything.

#### `check-toml`
Attempts to load all TOML files to verify syntax.

#### `check-vcs-permalinks`
Ensures that links to vcs websites are permalinks.
  - `--additional-github-domain DOMAIN` - Add check for specified domain.
    Can be repeated multiple times.  for example, if your company uses
    GitHub Enterprise you may use something like
    `--additional-github-domain github.example.com`

#### `check-xml`
Attempts to load all xml files to verify syntax.

#### `check-yaml`
Attempts to load all yaml files to verify syntax.
  - `--allow-multiple-documents` - allo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pygrep-hooks.md`
```markdown
# 📦 pre-commit/pygrep-hooks [🔖 PENDING/APPROVE]
🔗 https://github.com/pre-commit/pygrep-hooks


## Meta
- **Stars:** ⭐ 239 | **Forks:** 🍴 38
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-02-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A collection of fast, cheap, regex based pre-commit hooks.

## README (trích đầu)
```
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

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

