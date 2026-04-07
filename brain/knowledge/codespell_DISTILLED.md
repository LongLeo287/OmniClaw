---
id: codespell
type: knowledge
owner: OA_Triage
---
# codespell
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: .pre-commit-config.yaml
```yaml
---
files: ^(.*\.(py|json|md|sh|yaml|yml|in|cfg|txt|rst|toml|precommit-toml|wordlist))$
exclude: ^(\.[^/]*cache/.*)$
repos:
  - repo: https://github.com/executablebooks/mdformat
    # Do this before other tools "fixing" the line endings
    rev: 1.0.0
    hooks:
      - id: mdformat
        name: Format Markdown
        entry: mdformat # Executable to run, with fixed options
        language: python
        types: [markdown]
        args: [--wrap, "75", --number]
        additional_dependencies:
          - mdformat-toc
          - mdformat-beautysh
          # -mdformat-shfmt
          # -mdformat-tables
          - mdformat-config
          - mdformat-black
          - mdformat-web
          - mdformat-gfm
  - repo: https://github.com/Lucas-C/pre-commit-hooks-markup
    rev: v1.0.1
    hooks:
      - id: rst-linter
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: no-commit-to-branch
        args: [--branch, main]
      - id: check-yaml
        args: [--unsafe]
      - id: debug-statements
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-json
      - id: mixed-line-ending
      - id: check-builtin-literals
      - id: check-ast
      - id: check-merge-conflict
      - id: check-executables-have-shebangs
      - id: check-shebang-scripts-are-executable
      - id: check-docstring-first
      - id: fix-byte-order-marker
      - id: check-case-conflict
      - id: check-toml
      - id: file-contents-sorter
        files: dictionary.*\.txt$|\.wordlist$
        args: [--ignore-case]
  - repo: https://github.com/adrienverge/yamllint.git
    rev: v1.38.0
    hooks:
      - id: yamllint
        args:
          - --no-warnings
          - -d
          - "{extends: relaxed, rules: {line-length: {max: 90}}}"
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.8
    hooks:
      - id: ruff-check
      - id: ruff-format
  - repo: https://github.com/rbubley/mirrors-prettier
    rev: v3.8.1
    hooks:
      - id: prettier
        types_or: [yaml, markdown, html, css, scss, javascript, json]
  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.2
    hooks:
      - id: codespell
        args: [--toml, pyproject-codespell.precommit-toml]
        additional_dependencies:
          - tomli
  - repo: https://github.com/abravalheri/validate-pyproject
    rev: v0.25
    hooks:
      - id: validate-pyproject
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.19.1
    hooks:
      - id: mypy
        args: ["--config-file", "pyproject.toml"]
        additional_dependencies:
          - pytest
          - tomli
          - types-chardet

ci:
  autoupdate_schedule: weekly

```

### File: .pre-commit-hooks.yaml
```yaml
- id: codespell
  name: codespell
  description: Checks for common misspellings in text files.
  entry: codespell
  language: python
  types: [text]

```

### File: .devcontainer\devcontainer.json
```json
{
  "name": "Codespell Development Environment",
  "image": "mcr.microsoft.com/devcontainers/python:1-3",
  "customizations": {
    "vscode": {
      "extensions": [
        "github.vscode-github-actions",
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "postCreateCommand": "bash .devcontainer/post_create.sh"
}

```

### File: .devcontainer\post_create.sh
```sh
git config --global --add safe.directory /workspaces/codespell

sudo apt-get update
sudo apt-get install -y libaspell-dev

pip install --upgrade \
    aspell-python-py3 \
    pip \
    setuptools \
    setuptools_scm \
    wheel
pip install -e '.[dev]'

pre-commit install --install-hooks

```

### File: tools\gen_OX.sh
```sh
#!/bin/bash

one_of() {
   LIST="$*"
   echo '\(\('"${LIST// /\\)\\|\\(}"'\)\)'
}

SUFFIXES=(
   "ize"
   "izes"
   "izer"
   "izable"
   "ized"
   "izing"
   "izement"
   "ization"
   "izations"
)
PAT1="$(one_of "${SUFFIXES[@]}")$"

# choose US for these ones
EXCEPTIONS=(
   'defenc'
   'focuss'
)
PAT2="^$(one_of "${EXCEPTIONS[@]}")"

# these one should be left out
IGNORE=(
   'storey'
   'practise'
   'programme'
   'licence'
   'metre'
)
PAT3="^$(one_of "${IGNORE[@]}")"

(
   grep -e "$PAT1" -e "$PAT2" "$1" | grep -v "$PAT3" | grep -v '^\(colouris\)\|\(favouris\)'
   for i in e es ed ing ation ations er able; do
      echo "colouris$i->colouriz$i"
      echo "coloriz$i->colouriz$i"
   done
   for i in e es ed ing able; do
      echo "favouris$i->favouriz$i"
      echo "favoriz$i->favouriz$i"
   done
   grep -v -e "$PAT1" -e "$PAT2" "$1" | grep -v "$PAT3" | sed 's/^\(.*\)->\(.*\)$/\2->\1/'
) | sort -f -t- -k 1b,1

```

