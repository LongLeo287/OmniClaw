---
id: djLint
type: knowledge
owner: OA_Triage
---
# djLint
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "djlint",
  "version": "1.36.4",
  "description": "HTML Template Linter and Formatter",
  "keywords": [
    "html template linter",
    "html template formatter",
    "jinja template linter",
    "jinja template formatter",
    "nunjucks template linter",
    "nunjucks template formatter",
    "twig template linter",
    "twig template formatter",
    "handlebars template linter",
    "handlebars template formatter",
    "mustache template linter",
    "mustache template formatter",
    "golang template linter",
    "golang template formatter",
    "angular template linter",
    "angular template formatter"
  ],
  "homepage": "https://djlint.com",
  "bugs": {
    "url": "https://github.com/djlint/djLint/issues"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/djlint/djLint.git"
  },
  "license": "GPL-3.0-or-later",
  "author": {
    "name": "Christopher Pickering",
    "url": "https://going.bg"
  },
  "files": [],
  "scripts": {
    "postinstall": "python3 -m pip install --upgrade djlint==1.36.4"
  },
  "devDependencies": {
    "@ianvs/prettier-plugin-sort-imports": "4.7.1",
    "prettier": "3.8.1",
    "prettier-plugin-packagejson": "3.0.2"
  }
}

```

### File: README.md
```md
<h1 align="center">
  <br>
  <a href="https://www.djlint.com"><img src="https://raw.githubusercontent.com/djlint/djLint/master/docs/src/static/img/icon.png" alt="djLint Logo" width="270"></a>
  <br>
</h1>
<h3 align="center">🏗️ Maintainers needed, please reach out on discord or email!</h3>
<h4 align="center">The missing formatter and linter for HTML templates.</h4>

<p align="center">
    <a href="https://twitter.com/intent/tweet?text=djLint%20%7C%20The%20missing%20formatter%20and%20linter%20for%20HTML%20templates.&url=https://djlint.com/&hashtags=djlint,html-templates,django,jinja,developers"><img alt="tweet" src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social" /></a>
    <a href="https://discord.gg/taghAqebzU">
     <img src="https://badgen.net/discord/online-members/taghAqebzU?icon=discord&label" alt="Discord Chat">
   </a>
    </p>
    <p align="center">
   <a href="https://codecov.io/gh/djlint/djlint">
     <img src="https://codecov.io/gh/djlint/djlint/branch/master/graph/badge.svg?token=eNTG721BAA" alt="Codecov Status">
   </a>
   <a href="https://www.codacy.com/gh/djlint/djlint/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=djlint/djlint&amp;utm_campaign=Badge_Grade">
     <img src="https://app.codacy.com/project/badge/Grade/dba6338b0e7a4de896b45b382574f369" alt="Codacy Status">
   </a>
   <a href="https://pepy.tech/project/djlint">
     <img src="https://pepy.tech/badge/djlint" alt="Downloads">
   </a>
   <a href="https://www.npmjs.com/package/djlint">
       <img alt="npm" src="https://img.shields.io/npm/dt/djlint?label=npm%20downloads">
   </a>
   <a href="https://pypi.org/project/djlint/">
     <img src="https://img.shields.io/pypi/v/djlint" alt="Pypi Download">
   </a>
</p>

<h4 align="center"><a href="https://www.djlint.com">How to use</a> • <a href="https://www.djlint.com/ru/">Как пользоваться</a> • <a href="https://www.djlint.com/fr/">Utilisation</a></h4>
<h4 align="center">What lang are you using?</h4>

<p align="center">
   <a href="https://djlint.com/docs/languages/django/">Django</a> • <a href="https://djlint.com/docs/languages/jinja/">Jinja</a> • <a href="https://djlint.com/docs/languages/nunjucks/">Nunjucks</a> • <a href="https://djlint.com/docs/languages/twig/">Twig</a> • <a href="https://djlint.com/docs/languages/handlebars/">Handlebars</a> • <a href="https://djlint.com/docs/languages/mustach/">Mustache</a> • <a href="https://djlint.com/docs/languages/golang/">GoLang</a> • <a href="https://djlint.com/docs/languages/angular/">Angular</a>
</p>

<p align="center">
  <img src="https://github.com/djlint/djLint/blob/aa9097660d4a2e840450de5456f656c42bc7dd34/docs/src/static/img/demo-min.gif" alt="demo" width="600">
</p>

## 🤔 For What?

Once upon a time all the other programming languages had a formatter and linter. Css, javascript, python, the c suite, typescript, ruby, php, go, swift, and you know the others. The cool kids on the block.

HTML templates were left out there on their own, in the cold, unformatted and unlinted :( The dirty corner in your repository. Something had to change.

**djLint is a community build project to and add consistency to html templates.**

## ✨ How?

Grab it with `pip`

```bash
pip install djlint
```

_Or with the npm experimental install - Note, this requires python and pip to be on your system path._

```bash
npm i djlint
```

Lint your project

```bash
djlint . --extension=html.j2 --lint
```

Check your format

```bash
djlint . --extension=html.j2 --check
```

Fix my format!

```bash
djlint . --extension=html.j2 --reformat
```

## 💙 Like it?

Add a badge to your projects `readme.md`:

```md
[![Code style: djlint](https://img.shields.io/badge/html%20style-djlint-blue.svg)](https://www.djlint.com)
```

Add a badge to your `readme.rst`:

```rst
.. image:: https://img.shields.io/badge/html%20style-djlint-blue.svg
   :target: https://www.djlint.com
```

Looks like this:

[![djLint](https://img.shields.io/badge/html%20style-djLint-blue.svg)](https://github.com/djlint/djlint)

## 🛠️ Can I help?

Yes!

_Would you like to add a rule to the linter?_ Take a look at the [linter docs](https://djlint.com/docs/linter/) and [source code](https://github.com/djlint/djLint/blob/master/djlint/rules.yaml)

_Are you a regex pro?_ Benchmark and submit a pr with improved regex for the [linter rules](https://github.com/djlint/djLint/blob/master/djlint/rules.yaml)

**⚠️ Help Needed! ⚠️** _Good with python?_ djLint was an experimental project and is catching on with other devs. Help out with a rewrite of the formatter to improve speed and html style for edge cases. Contribute on the [2.0 branch](https://github.com/djlint/djLint/tree/block_indent)

## 🏃 Other Tools Of Note

- [DjHTML](https://github.com/rtts/djhtml) A pure-Python Django/Jinja template indenter without dependencies.
- [HTMLHint](https://htmlhint.com) Static code analysis tool you need for your HTML
- [curlylint](https://www.curlylint.org) Experimental HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid

```

### File: docs\package.json
```json
{
  "name": "djlint_docs",
  "version": "1.0.84",
  "description": "",
  "keywords": [],
  "license": "AGPL-3.0-or-later",
  "author": "Christopher Pickering",
  "main": "index.js",
  "scripts": {
    "build": "ELEVENTY_PRODUCTION=true eleventy",
    "start": "eleventy --serve --watch"
  },
  "browserslist": "> 2%, not dead",
  "dependencies": {
    "@codemirror/lang-html": "^6.4.3",
    "@codemirror/state": "^6.2.0",
    "@creativebulma/bulma-divider": "^1.1.0",
    "@fontsource/crimson-pro": "^5.0.0",
    "@fontsource/rasa": "^5.0.0",
    "@quasibit/eleventy-plugin-schema": "1.11.1",
    "@rollup/plugin-node-resolve": "^16.0.0",
    "@sindresorhus/slugify": "^3.0.0",
    "animate-sass": "^0.8.2",
    "animate.css": "github:animate-css/animate.css",
    "codemirror": "^6.0.1",
    "eleventy-critical-css": "^2.0.2",
    "eleventy-plugin-i18n": "^0.1.3",
    "eleventy-plugin-rev": "^2.0.0",
    "eleventy-sass": "^2.2.1",
    "md5": "^2.3.0",
    "rollup": "^4.8.0"
  },
  "devDependencies": {
    "@11ty/eleventy": "2.0.1",
    "@11ty/eleventy-img": "^6.0.0",
    "@11ty/eleventy-plugin-syntaxhighlight": "5.0.2",
    "@fontsource/inter": "^5.0.16",
    "@fortawesome/fontawesome-free": "^6.4.0",
    "@fullhuman/postcss-purgecss": "8.0.0",
    "@toycode/markdown-it-class": "1.2.4",
    "algoliasearch": "^5.0.0",
    "autoprefixer": "^10.4.14",
    "bulma": "0.9.4",
    "bulma-pricingtable": "0.2.0",
    "cssnano": "^7.0.0",
    "eleventy-plugin-edit-on-github": "1.1.0",
    "eleventy-plugin-metagen": "^1.8.3",
    "esbuild": "^0.28.0",
    "fontawesome-subset": "4.6.0",
    "html-minifier": "4.0.0",
    "markdown-it": "^14.0.0",
    "markdown-it-anchor": "9.2.0",
    "markdown-it-div": "1.1.0",
    "markdown-it-imsize": "2.0.1",
    "outdent": "0.8.0",
    "postcss-cli": "^11.0.0",
    "postcss-nested": "7.0.2",
    "prismjs": "1.30.0",
    "sass": "^1.60.0",
    "slugify": "^1.6.6"
  }
}

```

### File: docs\readme.md
```md
# djLint Docs

Docs are made with [11ty](https://www.11ty.dev).

## Running the docs website locally

1. change into the docs dir. `cd docs`
2. install node deps. `npm install --ignore-scripts`
3. turn on the website. `npm start`

## How the demo works

The demo is running python as a webworker in web assembly from [pyodide](https://pyodide.org/en/stable/index.html).

When the page is access a webworker starts, downloads python, installs djLint and deps (notice the wheels in `/src/static/py` that are updated when a new release is created.).

Once the worker responds "ready" the web UI is shown.

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-case-conflict
      - id: check-executables-have-shebangs
      - id: check-illegal-windows-names
      - id: check-merge-conflict
      - id: check-shebang-scripts-are-executable
      - id: check-symlinks
      - id: check-xml
      - id: destroyed-symlinks
      - id: end-of-file-fixer
      - id: fix-byte-order-marker
      - id: mixed-line-ending
        args:
          - --fix=lf
      - id: trailing-whitespace
  - repo: https://github.com/tombi-toml/tombi-pre-commit
    rev: v0.9.14
    hooks:
      - id: tombi-format
        exclude: ^uv.lock$
  - repo: https://github.com/rbubley/mirrors-prettier
    rev: v3.8.1
    hooks:
      - id: prettier
        args:
          - --object-wrap=collapse
          - --no-config
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.15.9
    hooks:
      - id: ruff-check
        args:
          - --fix
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.20.0
    hooks:
      - id: mypy
        args:
          - --scripts-are-modules
        additional_dependencies:
          - click
          - cssbeautifier
          - jsbeautifier
          - json5
          - pathspec
          - pytest
          - tomli
          - types-colorama
          - types-pyyaml
          - types-regex
          - types-tqdm
          - typing-extensions

```

### File: .pre-commit-hooks.yaml
```yaml
- id: djlint
  name: djLint linting
  entry: djlint
  types_or: [html]
  language: python

- id: djlint-django
  name: djLint linting for Django
  entry: djlint --profile=django
  types_or: [html]
  language: python

- id: djlint-jinja
  name: djLint linting for Jinja
  entry: djlint --profile=jinja
  types_or: [jinja]
  language: python

- id: djlint-nunjucks
  name: djLint linting for Nunjucks
  entry: djlint --profile=nunjucks
  types_or: [nunjucks]
  language: python

- id: djlint-handlebars
  name: djLint linting for Handlebars/Mustache
  entry: djlint --profile=handlebars
  types_or: [handlebars]
  language: python

- id: djlint-golang
  name: djLint linting for Golang templates
  entry: djlint --profile=golang
  types_or: [gotmpl]
  language: python

- id: djlint-reformat
  name: djLint formatting
  entry: djlint --reformat
  types_or: [html]
  language: python

- id: djlint-reformat-django
  name: djLint formatting for Django
  entry: djlint --reformat --profile=django
  types_or: [html]
  language: python

- id: djlint-reformat-jinja
  name: djLint formatting for Jinja
  entry: djlint --reformat --profile=jinja
  types_or: [jinja]
  language: python

- id: djlint-reformat-nunjucks
  name: djLint formatting for Nunjucks
  entry: djlint --reformat --profile=nunjucks
  types_or: [nunjucks]
  language: python

- id: djlint-reformat-handlebars
  name: djLint formatting for Handlebars/Mustache
  entry: djlint --reformat --profile=handlebars
  types_or: [handlebars]
  language: python

- id: djlint-reformat-golang
  name: djLint formatting for Golang templates
  entry: djlint --reformat --profile=golang
  types_or: [gotmpl]
  language: python

```

### File: CHANGELOG.md
```md
# Changelog

[Semantic Versioning](https://semver.org/)

## [1.36.4] - 2024-12-24

- Fix specific mixture of quotes and escaped quotes (e.g. in a json string in an html attribute) breaks the html. Thanks, @oliverhaas.
- Fix broken formatting of template tags inside template tags. Thanks, @oliverhass.

## [1.36.3] - 2024-11-29

This release reverts the following changes from the last release as they caused issues:

- Fix specific mixture of quotes and escaped quotes (e.g. in a json string in an html attribute) breaks the html. Issue #1048.
- Resolve exclude paths. Issue #1047.

## [1.36.2] - 2024-11-28

Fix:

- Fix specific mixture of quotes and escaped quotes (e.g. in a json string in an html attribute) breaks the html. Thanks, @oliverhaas.
- Resolve exclude paths. Thanks, @antoineauger.

Performance:

- Minor regex indent optimization. Thanks, @oliverhaas.

## [1.36.1] - 2024-11-07

- Improve performance by ~30%. Thanks, @oliverhaas.

## [1.36.0] - 2024-11-05

### Feature

- Add support for `djlint.toml` config file. The format is identical to `pyproject.toml`, but it does not use `[tool.djlint]` table.

### Fix

- Do not format HTML in attributes. Thanks, @oliverhaas.
- Fix using `js_config` instead of `css_config`.

### Performance

- Increase performance by ~30% by using regex more efficiently and caching more stuff.

## [1.35.4] - 2024-11-01

Compiled [mypyc](https://mypyc.readthedocs.io/en/stable/introduction.html) wheels are now also available, which improve performance by ~21% over Pure Python. They will be automatically installed by your package manager when available for your platform. Pure Python wheel is still available.

Other changes have been made to improve performance, thanks to @JCWasmx86. See the [commits](https://github.com/djlint/djLint/compare/v1.35.3...v1.35.4) for more details.

Formatting performance comparison with the previous version (tested on <https://github.com/openedx/edx-platform> with single thread):

| Version             | Seconds |
| ------------------- | ------- |
| v1.35.3             | 20.39   |
| v1.35.4 pure Python | 14.39   |
| v1.35.4 compiled    | 11.35   |

## [1.35.3] - 2024-10-30

This release significantly improves performance, especially for large files and large projects.

Formatting <https://github.com/openedx/edx-platform> took 87 seconds in the previous version, now it takes only 4 seconds (>2000% speedup)! Tested on a 32-core computer.

- Performance improved by caching some functions. Thanks to @JCWasmx86!
- Removed the limitation on the number of workers introduced in v1.35.0.
- Drop Python 3.8 support.

## [1.35.2] - 2024-08-29

- Fix npm publishing

## [1.35.1] - 2024-08-29

- Fix npm publishing

## [1.35.0] - 2024-08-29

- Unpin dependencies upper bounds.
- Use min(cpu_count, files_count, 4) workers. Use a thread instead of a process if only one worker will be used. This gives the best performance and low resource usage.
- Refactor the code.
- Fix max attribute length with longer regex custom html tags (#884)
- Fix Jinja formatting issues (#715)
- Fix: not detecting tabs as a valid seperation between tags (#813)
- Fix: Add ignore for sms links (#815)
- Fix: Allow attributes on <title> (#830)

```

### File: package-lock.json
```json
{
  "name": "djlint",
  "version": "1.36.4",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "djlint",
      "version": "1.36.4",
      "hasInstallScript": true,
      "license": "GPL-3.0-or-later",
      "devDependencies": {
        "@ianvs/prettier-plugin-sort-imports": "4.7.1",
        "prettier": "3.8.1",
        "prettier-plugin-packagejson": "3.0.2"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
      "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
      "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.2",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.2.tgz",
      "integrity": "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.28.6.tgz",
      "integrity": "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.28.6",
        "@babel/parser": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.0.tgz",
      "integrity": "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@ianvs/prettier-plugin-sort-imports": {
      "version": "4.7.1",
      "resolved": "https://registry.npmjs.org/@ianvs/prettier-plugin-sort-imports/-/prettier-plugin-sort-imports-4.7.1.tgz",
      "integrity": "sha512-jmTNYGlg95tlsoG3JLCcuC4BrFELJtLirLAkQW/71lXSyOhVt/Xj7xWbbGcuVbNq1gwWgSyMrPjJc9Z30hynVw==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@babel/generator": "^7.26.2",
        "@babel/parser": "^7.26.2",
        "@babel/traverse": "^7.25.9",
        "@babel/types": "^7.26.0",
        "semver": "^7.5.2"
      },
      "peerDependencies": {
        "@prettier/plugin-oxc": "^0.0.4 || ^0.1.0",
        "@vue/compiler-sfc": "2.7.x || 3.x",
        "content-tag": "^4.0.0",
        "prettier": "2 || 3 || ^4.0.0-0",
        "prettier-plugin-ember-template-tag": "^2.1.0"
      },
      "peerDependenciesMeta": {
        "@prettier/plugin-oxc": {
          "optional": true
        },
        "@vue/compiler-sfc": {
          "optional": true
        },
        "content-tag": {
          "optional": true
        },
        "prettier-plugin-ember-template-tag": {
          "optional": true
        }
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/detect-indent": {
      "version": "7.0.2",
      "resolved": "https://registry.npmjs.org/detect-indent/-/detect-indent-7.0.2.tgz",
      "integrity": "sha512-y+8xyqdGLL+6sh0tVeHcfP/QDd8gUgbasolJJpY7NgeQGSZ739bDtSiaiDgtoicy+mtYB81dKLxO9xRhCyIB3A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.20"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/detect-newline": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/detect-newline/-/detect-newline-4.0.1.tgz",
      "integrity": "sha512-qE3Veg1YXzGHQhlA6jzebZN2qVf6NX+A7m7qlhCGG30dJixrAQhYOsJjsnBjJkCSmuOPpCk30145fr8FV0bzog==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^12.20.0 || ^14.13.1 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/git-hooks-list": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/git-hooks-list/-/git-hooks-list-4.2.1.tgz",
      "integrity": "sha512-WNvqJjOxxs/8ZP9+DWdwWJ7cDsd60NHf39XnD82pDVrKO5q7xfPqpkK6hwEAmBa/ZSEE4IOoR75EzbbIuwGlMw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/fisker/git-hooks-list?sponsor=1"
      }
    },
    "node_modules/is-plain-obj": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-4.1.0.tgz",
      "integrity": "sha512-+Pgi+vMuUNkJyExiMBt5IlFoMyKnr5zhJ4Uspz58WOhBF5QoIZkFyNHIbBAtHwzVAgk5RtndVNsDRN61/mmDqg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.4.tgz",
      "integrity": "sha512-QP88BAKvMam/3NxH6vj2o21R6MjxZUAd6nlwAS/pnGvN9IVLocLHxGYIzFhg6fUQ+5th6P4dv4eW9jX3DSIj7A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/prettier": {
      "version": "3.8.1",
      "resolved": "https://registry.npmjs.org/prettier/-/prettier-3.8.1.tgz",
      "integrity": "sha512-UOnG6LftzbdaHZcKoPFtOcCKztrQ57WkHDeRD9t/PTQtmT0NHSeWWepj6pS0z/N7+08BHFDQVUrfmfMRcZwbMg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "prettier": "bin/prettier.cjs"
      },
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com/prettier/prettier?sponsor=1"
      }
    },
    "node_modules/prettier-plugin-packagejson": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/prettier-plugin-packagejson/-/prettier-plugin-packagejson-3.0.2.tgz",
      "integrity": "sha512-kmoj3hEynXwoHDo8ZhmWAIjRBoQWCDUVackiWfSDWdgD0rS3LGB61T9zoVbume/cotYdCoadUh4sqViAmXvpBQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "sort-package-json": "^3.6.0"
      },
      "peerDependencies": {
        "prettier": "^3"
      },
      "peerDependenciesMeta": {
        "prettier": {
          "optional": true
        }
      }
    },
    "node_modules/semver": {
      "version": "7.7.4",
      "resolved": "https://registry.npmjs.org/semver/-/semver-7.7.4.tgz",
      "integrity": "sha512-vFKC2IEtQnVhpT78h1Yp8wzwrf8CM+MzKMHGJZfBtzhZNycRFnXsHk6E5TxIkkMsgNS7mdX3AGB7x2QM2di4lA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/sort-object-keys": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/sort-object-keys/-/sort-object-keys-2.1.0.tgz",
      "integrity": "sha512-SOiEnthkJKPv2L6ec6HMwhUcN0/lppkeYuN1x63PbyPRrgSPIuBJCiYxYyvWRTtjMlOi14vQUCGUJqS6PLVm8g==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/sort-package-json": {
      "version": "3.6.1",
      "resolved": "https://registry.npmjs.org/sort-package-json/-/sort-package-json-3.6.1.tgz",
      "integrity": "sha512-Chgejw1+10p2D0U2tB7au1lHtz6TkFnxmvZktyBCRyV0GgmF6nl1IxXxAsPtJVsUyg/fo+BfCMAVVFUVRkAHrQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "detect-indent": "^7.0.2",
        "detect-newline": "^4.0.1",
        "git-hooks-list": "^4.1.1",
        "is-plain-obj": "^4.1.0",
        "semver": "^7.7.3",
        "sort-object-keys": "^2.0.1",
        "tinyglobby": "^0.2.15"
      },
      "bin": {
        "sort-package-json": "cli.js"
      },
      "engines": {
        "node": ">=20"
      }
    },
    "node_modules/tinyglobby": {
      "version": "0.2.15",
      "resolved": "https://re
... [TRUNCATED]
```

### File: .github\pull_request_template.md
```md
# Pull Request Check List

Resolves: #issue-number-here

- [ ] Added **tests** for changed code.
- [ ] Updated **documentation** for changed code.

<!-- If you have *any* questions to *any* of the points above, just **submit and ask**!  This checklist is here to *help* you, not to deter you from contributing! -->

```

### File: .github\renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "configMigration": true,
  "dependencyDashboard": false,
  "docker-compose": { "enabled": true },
  "extends": ["config:recommended"],
  "lockFileMaintenance": { "enabled": true, "schedule": ["at any time"] },
  "packageRules": [
    {
      "matchCurrentVersion": "!/^0/",
      "matchUpdateTypes": ["minor"],
      "automerge": true
    },
    {
      "matchUpdateTypes": ["lockFileMaintenance", "patch", "replacement"],
      "automerge": true
    },
    {
      "matchDepTypes": ["dependency-groups"],
      "matchManagers": ["pep621"],
      "automerge": true
    },
    {
      "matchDepTypes": ["devDependencies"],
      "matchManagers": ["npm"],
      "automerge": true
    },
    { "matchManagers": ["github-actions", "pre-commit"], "automerge": true }
  ],
  "prConcurrentLimit": 0,
  "prHourlyLimit": 0,
  "pre-commit": { "enabled": true },
  "rollbackPrs": true,
  "semanticCommits": "enabled",
  "schedule": ["at any time"]
}

```

### File: docs\.eleventy.js
```js
const Image = require("@11ty/eleventy-img");
const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const slugify = require("slugify");
const metagen = require("eleventy-plugin-metagen");
const i18n = require("eleventy-plugin-i18n");
const translations = require("./src/_data/i18n");
const locales = require("./src/_data/locales");
const fs = require("fs");
const outdent = require("outdent");
const schema = require("@quasibit/eleventy-plugin-schema");
const editOnGithub = require("eleventy-plugin-edit-on-github");
const i18n_func = require("eleventy-plugin-i18n/i18n.js");
const rollupper = require("./src/_utils/rollupper");
const { nodeResolve } = require("@rollup/plugin-node-resolve");
const eleventySass = require("eleventy-sass");
const pluginRev = require("eleventy-plugin-rev");
const purgecss = require("@fullhuman/postcss-purgecss");
const postcss = require("postcss");

const slugifyCustom = (s) =>
  slugify(s, { lower: true, remove: /[*+~.()'"!:@]/g });

async function imageShortcode(
  src,
  alt,
  sizes,
  type = "asdf",
  loading = "lazy",
  decoding = "async",
) {
  let metadata = await Image(src, {
    widths: [24, 300, 400, 500, 600, 800, 1200],
    formats: ["webp", "png"],
    sharpWebpOptions: { options: { quality: 70 } },
    outputDir: "./_site/static/img/",
    urlPath: "/static/img/",
  });

  let imageAttributes = { alt, sizes, loading: loading, decoding: decoding };

  if (type == "boxed") {
    return (
      `<div class="block"><div class="box is-inlineblock">` +
      Image.generateHTML(metadata, imageAttributes) +
      `</div></div>`
    );
  }
  // using custom code so that we can return the highest src in img as old browsers don't auto upscale.
  let lowsrc = metadata.png[0];
  let highsrc = metadata.png[metadata.png.length - 1];
  return `<picture>
    ${Object.values(metadata)
      .map((imageFormat) => {
        return `  <source type="${
          imageFormat[0].sourceType
        }" srcset="${imageFormat
          .map((entry) => entry.srcset)
          .join(", ")}" sizes="${sizes}">`;
      })
      .join("\n")}
      <img
        src="${highsrc.url}"
        width="${highsrc.width}"
        height="${highsrc.height}"
        alt="${alt}"
        loading="lazy"
        decoding="async">
    </picture>`;
}

// from https://github.com/pusher/docs/blob/main/.eleventy.js
// widont is a function that takes a string and replaces the space between the last two words with a non breaking space. This stops typographic widows forming
const widont = (string) => {
  return string.split(" ").length > 2
    ? string.replace(/\s([^\s<]+)\s*$/, "\u00A0$1")
    : string;
};

module.exports = function (eleventyConfig) {
  eleventyConfig.addGlobalData(
    "djlint_version",
    require("../package.json").version,
  );
  eleventyConfig.setUseGitIgnore(false);
  eleventyConfig.addFilter("widont", widont);
  eleventyConfig.addWatchTarget("./src/static/");
  eleventyConfig.addNunjucksAsyncShortcode("image", imageShortcode);
  if (process.env.ELEVENTY_PRODUCTION == true) {
    eleventyConfig.addTransform(
      "htmlmin",
      require("./src/_utils/minify-html.js"),
    );
  }
  eleventyConfig.addPlugin(syntaxHighlight);
  eleventyConfig.addPlugin(metagen);
  eleventyConfig.addPlugin(schema);
  eleventyConfig.addPlugin(rollupper, {
    rollup: {
      output: { format: "umd", dir: "_site/static/js" },
      plugins: [nodeResolve()],
    },
  });
  eleventyConfig.addPlugin(editOnGithub, {
    // required
    github_edit_repo: "https://github.com/djlint/djLint",
    // optional: defaults
    github_edit_path: "/docs/", // non-root location in git url. root is assumed
    github_edit_branch: "master",
    github_edit_text: (page) => {
      i18n_options = Object.assign(
        {},
        { translations, fallbackLocales: { "*": "en-US" } },
      );

      return `<span class="icon-text"><span class="icon mr-1"><i class="fas fa-pencil"></i></span><span>${i18n_func(
        "edit_page",
        undefined,
        undefined,
        i18n_options,
        page,
      )}</span></span>`;
      return x.inputPath;
    },
    github_edit_class: "edit-on-github",
    github_edit_tag: "a",
    github_edit_attributes: 'target="_blank" rel="noopener"',
    github_edit_wrapper: undefined, //ex: "<div stuff>${edit_on_github}</div>"
  });

  /* Markdown Plugins */
  const markdownItAnchor = require("markdown-it-anchor");
  const markdownIt = require("markdown-it")({
    html: true,
    breaks: true,
    linkify: true,
    typographer: true,
  });

  const opts = {
    level: [2, 3, 4, 5],
    permalink: markdownItAnchor.permalink.linkInsideHeader({
      class: "link bn",
      symbol: "∞",
      placement: "before",
    }),
    slugify: slugifyCustom,
  };

  const mapping = {
    h1: "title is-1",
    h2: "title is-2",
    h3: "title is-3",
    h4: "title is-4",
    h5: "title is-5",
    h6: "title is-5",
    p: "block",
    table: "table",
  };

  markdownIt
    .use(markdownItAnchor, opts)
    .use(require("markdown-it-imsize"), { autofill: true })
    .use(require("@toycode/markdown-it-class"), mapping)
    .use(require("markdown-it-div"), "div", {});

  eleventyConfig.setLibrary("md", markdownIt);

  // copy font
  eleventyConfig.addPassthroughCopy({
    "./node_modules/@fontsource/inter/files": "static/font/inter/files",
  });
  eleventyConfig.addPassthroughCopy({
    "./node_modules/@fontsource/rasa/files": "static/font/rasa/files",
  });
  eleventyConfig.addPassthroughCopy({
    "./node_modules/@fontsource/crimson-pro/files":
      "static/font/crimson-pro/files",
  });

  // copy images
  eleventyConfig.addPassthroughCopy({ "src/static/img": "static/img" });

  // copy robots
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });

  // copy favicon
  eleventyConfig.addPassthroughCopy({
    "src/static/img/favicon.ico": "favicon.ico",
  });

  // copy wheels
  eleventyConfig.addPassthroughCopy({ "src/static/py": "static/py" });

  // copy python
  eleventyConfig.addPassthroughCopy({
    "src/static/js/worker.js": "static/js/worker.js",
  });

  eleventyConfig.addFilter("jsonify", (text) => {
    return JSON.stringify(text).replace(/(?:\\n\s*){2,}/g, "\\n");
  });

  eleventyConfig.addFilter("niceDate", (value) => {
    try {
      const options = { year: "numeric", month: "short", day: "numeric" };
      return value.toLocaleDateString("en-us", options);
    } catch (e) {
      return value;
    }
  });

  eleventyConfig.addFilter("year", (value) => {
    try {
      const options = { year: "numeric" };
      return value.toLocaleDateString("en-us", options);
    } catch (e) {
      return value;
    }
  });

  eleventyConfig.addFilter("algExcerpt", (text) => {
    return text
      .replace(/<code class="language-.*?">.*?<\/code>/gs, "")
      .replace(/<.*?>/g, "")
      .substring(0, 8000);
  });

  eleventyConfig.addCollection("algolia", function (collection) {
    return collection.getFilteredByGlob("**/*.md");
  });

  const icons = {
    note: '<span class="icon has-text-info mr-1"><i class="fas fa-pencil"></i></span>',
  };

  eleventyConfig.addShortcode("admonition", function (icon, title, text) {
    return outdent`
    <article class="message ${icon} box">
      <div class="message-header">
        <p>${icons[icon]} ${title}</p>
      </div>
      <div class="message-body">${markdownIt.render(text)}</div>
    </article>`;
  });

  eleventyConfig.addFilter("markdown", (value) => {
    return `${markdownIt.render(value)}`;
  });

  eleventyConfig.addPlugin(pluginRev);

  eleventyConfig.addPlugin(eleventySass, [
    {
      rev: true,
      postcss: postcss([
        require("postcss-nested"),
        purgecss({
          content: ["./src/**/*.njk", "./src/**/*.md", "./src/**/*.js"],
          safelist: {
            deep: [
              /headShake/,
              /zoomIn/,
              /fadeInUp/,
              /pre/,
              /code/,
              /block/,
              /box/,
              /title/,
              /is-\d/,
              /table/,
              /message/,
              /message-header/,
              /message-body/,
              /panel-block/,
              /p-3/,
              /my-3/,
              /is-block/,
              /is-justify-content-space-between/,
              /is-light/,
              /is-active/,
              /is-info/,
              /is-link/,
              /fa-*/,
              /mr-1/,
              /mr-2/,
              /has-text-info/,
              /has-background-white-ter/,
              /is-rounded/,
            ],
          },
        }),
        require("autoprefixer"),
        require("cssnano"),
      ]),
    },
  ]);

  const { fontawesomeSubset } = require("fontawesome-subset");
  fontawesomeSubset(
    {
      brands: ["discord", "github"],
      regular: ["envelope"],
      solid: [
        "globe",
        "circle-arrow-right",
        "pencil",
        "infinity",
        "download",
        "code-commit",
        "spinner",
        "circle-question",
      ],
    },
    "_site/static/font/fontawesome/webfonts",
  );

  eleventyConfig.addPlugin(i18n, {
    translations,
    fallbackLocales: { "*": "en-US" },
  });

  eleventyConfig.addFilter("baseUrl", (text) => {
    return text.replace(/(?:ru)\//g, "");
  });

  eleventyConfig.addFilter("i18n_locale", (current_locale, locale_list) => {
    return locale_list.filter((x) => {
      return x.code === (current_locale ?? "en-US");
    })[0].label;
  });

  eleventyConfig.addFilter("i18n_urls", (page, all) => {
    var locale_urls = locales
      .map((x) => {
        if (x.url != "") return x.url;
      })
      .filter((x) => {
        return x !== undefined;
      });

    var split_url = page.split("/").length > 1 ? page.split("/")[1] : "";

    // find the current locale
    var active_local = "";

    locale_urls.forEach((locale) => {
      if (locale === split_url) {
        active_local = locale;
        return true;
      }
      return false;
    });

    // get remaining locales
    var remaining_locals = locales
      .map((x) => {
        return x.url;
      })
      .filter((x) => {
        return x !== active_local;
      });

    var i18n_pages = [];

    var valid_urls = all.map((x) => {
      return x.url;
    });

    remaining_locals.forEach((x) => {
      var new_url = ("/" + page.replace(active_local, x)).replace(
        /\/{2,}/,
        "/",
      );
      if (valid_urls.indexOf(new_url) !== -1) {
        i18n_pages.push({
          url: new_url,
          meta: locales.filter((y) => {
            return y.url === x;
          })[0],
        });
      }
    });

    return i18n_pages;
  });

  return {
    dir: {
      input: "src",
      formats: "njk",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    templateFormats: ["md", "html", "njk", "11ty.js"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
    passthroughFileCopy: true,
  };
};

```

### File: tests\conftest.py
```py
"""Djlint test config."""

from __future__ import annotations

import difflib
import shutil
import tempfile
from pathlib import Path
from types import SimpleNamespace
from typing import TYPE_CHECKING

import pytest
from click.testing import CliRunner
from colorama import Fore, Style

from djlint import main as djlint
from djlint.settings import Config

if TYPE_CHECKING:
    import os
    from collections.abc import Iterator, Mapping
    from typing import TextIO

    from typing_extensions import Any

    from djlint.types import LintError


@pytest.fixture
def runner() -> CliRunner:
    """Click runner for djlint tests."""
    return CliRunner()


@pytest.fixture
def tmp_file() -> Iterator[tempfile._TemporaryFileWrapper[bytes]]:
    """Create a temp file for formatting."""
    tmp = tempfile.NamedTemporaryFile(delete=False)  # noqa: SIM115
    try:
        with tmp:
            yield tmp
    finally:
        Path(tmp.name).unlink(missing_ok=True)


def printer(expected: str, source: str, actual: str) -> None:
    width, _ = shutil.get_terminal_size()

    expected_text = "Expected"
    actual_text = "Actual"
    diff_text = "Diff"
    source_text = "Source"

    expected_width = (width - len(expected_text) - 2) // 2
    actual_width = (width - len(actual_text) - 2) // 2
    diff_width = (width - len(diff_text) - 2) // 2
    source_width = (width - len(source_text) - 2) // 2

    color = {"-": Fore.YELLOW, "+": Fore.GREEN, "@": Style.BRIGHT + Fore.BLUE}

    print()
    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * source_width} {source_text} {'─' * source_width}{Style.RESET_ALL}"
    )
    print()
    print(source)
    print()
    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * expected_width} {expected_text} {'─' * expected_width}{Style.RESET_ALL}"
    )
    print()
    print(expected)
    print()
    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * actual_width} {actual_text} {'─' * actual_width}{Style.RESET_ALL}"
    )
    print()
    print(actual)
    print()
    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * diff_width} {diff_text} {'─' * diff_width}{Style.RESET_ALL}"
    )
    print()
    for diff in tuple(
        difflib.unified_diff(expected.split("\n"), actual.split("\n"))
    )[2:]:
        print(f"{color.get(diff[:1], Style.RESET_ALL)}{diff}{Style.RESET_ALL}")


def lint_printer(
    source: str, expected: list[LintError], actual: list[LintError]
) -> None:
    width, _ = shutil.get_terminal_size()

    expected_text = "Expected Rules"
    actual_text = "Actual"
    source_text = "Source"

    expected_width = (width - len(expected_text) - 2) // 2
    actual_width = (width - len(actual_text) - 2) // 2
    source_width = (width - len(source_text) - 2) // 2

    print()
    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * source_width} {source_text} {'─' * source_width}{Style.RESET_ALL}"
    )
    print()
    print(source)
    print()

    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * expected_width} {expected_text} {'─' * expected_width}{Style.RESET_ALL}"
    )
    print()
    for x in expected:
        print(
            f"{Fore.RED}{Style.BRIGHT}{x['code']}{Style.RESET_ALL} {x['line']} {x['match']}"
        )
        print(f"     {x['message']}")
        print()

    print(
        f"{Fore.BLUE}{Style.BRIGHT}{'─' * actual_width} {actual_text} {'─' * actual_width}{Style.RESET_ALL}"
    )
    print()

    for x in actual:
        print(
            f"{Fore.RED}{Style.BRIGHT}{x['code']}{Style.RESET_ALL} {x['line']} {x['match']}"
        )
        print(f"     {x['message']}")
        print()
    if not actual:
        print(f"{Fore.YELLOW}No codes found.{Style.RESET_ALL}")
        print()

    else:
        print(f"{Fore.YELLOW}{actual}{Style.RESET_ALL}")
        print()


def write_to_file(the_file: str | os.PathLike[str], the_text: bytes) -> None:
    """Shortcode for write some bytes to a file."""
    Path(the_file).write_bytes(the_text)


def reformat(
    the_file: TextIO, runner: CliRunner, the_text: bytes, profile: str = "html"
) -> SimpleNamespace:
    write_to_file(the_file.name, the_text)
    result = runner.invoke(
        djlint, (the_file.name, "--profile", profile, "--reformat")
    )
    return SimpleNamespace(
        text=Path(the_file.name).read_text(encoding="utf-8"),
        exit_code=result.exit_code,
    )


def config_builder(args: Mapping[str, Any] | None = None) -> Config:
    if args:
        return Config("dummy/source.html", **args)
    return Config("dummy/source.html")


@pytest.fixture
def basic_config() -> Config:
    """Return a config object with default basic options."""
    return Config("dummy/source.html")


@pytest.fixture
def django_config() -> Config:
    """Return a config object with django profile."""
    return Config("dummy/source.html", profile="django")


@pytest.fixture
def jinja_config() -> Config:
    """Return a config object with jinja."""
    return Config("dummy/source.html", profile="jinja")


@pytest.fixture
def handlebars_config() -> Config:
    """Return a config object with handlebars."""
    return Config("dummy/source.html", profile="handlebars")


@pytest.fixture
def nunjucks_config() -> Config:
    """Return a config object with nunjucks."""
    return Config("dummy/source.html", profile="nunjucks")

```

### File: tests\test_cli.py
```py
"""Test for cli inputs.

uv run pytest tests/test_cli.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from djlint import main as djlint

if TYPE_CHECKING:
    from click.testing import CliRunner


def test_cli(runner: CliRunner) -> None:
    # missing options:
    result = runner.invoke(
        djlint,
        (
            "-",
            "--check",
            "--blank-line-after-tag",
            "p",
            "--blank-line-before-tag",
            "p",
            "--custom-blocks",
            "toc",
            "--custom-html",
            "asdf",
            "--exclude",
            ".asdf",
            "--extend-exclude",
            ".asdf",
            "--extension",
            "html.dj",
            "--format-attribute-template-tags",
            "--format-css",
            "--format-js",
            "--ignore",
            "H014,H015",
            "--ignore-blocks",
            "raw",
            "--ignore-case",
            "--include",
            "H014",
            "--indent",
            "4",
            "--linter-output-format",
            "{code}",
            "--max-attribute-length",
            "9",
            "--max-line-length",
            "100",
            "--preserve-blank-lines",
            "--preserve-leading-space",
            "--profile",
            "django",
            "--require-pragma",
            "--use-gitignore",
            "--per-file-ignores",
            "test.html",
            "H014",
            "--per-file-ignores",
            "test2.html",
            "H015",
            "--indent-css",
            "4",
            "--indent-js",
            "4",
        ),
        input="<div></div>\n",
    )

    print(result.output)

    assert result.exit_code == 0

```

### File: tests\__init__.py
```py

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: "\U0001F682 Feature Request"
about: Do you have an idea for a new feature or improvement?
title: "[FEATURE]"
labels: enhancement
---

<!--
    Thanks for wanting to make djLint better.

    Have you...
-->

- [ ] I've searched the [issues](https://github.com/djlint/djLint/issues)
- [ ] I've read the [docs](https://djlint.com)

## Feature Request

<!-- Thanks! 🤠 -->

```

### File: .github\ISSUE_TEMPLATE\formatter_but_report.md
```md
---
name: "\U0001F9A0 Formatter Bug Report"
about: You've found a bug?
title: "[BUG] [Formatter]"
labels: [":microbe: bug", ":sponge: formatter"]
---

<!--
    Thanks for finding and submitting an issue.

    Have you...
-->

- [ ] I'm on the [latest version](https://pypi.org/project/djlint/) of djLint
- [ ] I've searched the [issues](https://github.com/djlint/djLint/issues)
- [ ] I've read the [docs](https://djlint.com)

## System Info

- OS: e.g. ubuntu 20.04
- Python Version (`python --version`)
- djLint Version (`djlint --version`)
- template language: e.g. mustache

## Issue

<!-- A clear and concise description of what the bug is. -->

## How To Reproduce

<!-- Steps to reproduce the behavior -->

<!-- Thanks! 🤠 -->

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
