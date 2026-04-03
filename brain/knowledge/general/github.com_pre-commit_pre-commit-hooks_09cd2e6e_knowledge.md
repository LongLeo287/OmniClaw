---
id: github.com-pre-commit-pre-commit-hooks-09cd2e6e-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.605025
---

# KNOWLEDGE EXTRACT: github.com_pre-commit_pre-commit-hooks_09cd2e6e
> **Extracted on:** 2026-04-01 09:52:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520497/github.com_pre-commit_pre-commit-hooks_09cd2e6e

---

## File: `.gitignore`
```
*.egg-info
*.py[co]
.*.sw[a-z]
.coverage
.tox
dist
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
-   id: check-added-large-files
    name: check for added large files
    description: prevents giant files from being committed.
    entry: check-added-large-files
    language: python
    stages: [pre-commit, pre-push, manual]
    minimum_pre_commit_version: 3.2.0
-   id: check-ast
    name: check python ast
    description: simply checks whether the files parse as valid python.
    entry: check-ast
    language: python
    types: [python]
-   id: check-byte-order-marker
    name: check-byte-order-marker (removed)
    description: (removed) use fix-byte-order-marker instead.
    entry: pre-commit-hooks-removed check-byte-order-marker fix-byte-order-marker https://github.com/pre-commit/pre-commit-hooks
    language: python
    types: [text]
-   id: check-builtin-literals
    name: check builtin type constructor use
    description: requires literal syntax when initializing empty or zero python builtin types.
    entry: check-builtin-literals
    language: python
    types: [python]
-   id: check-case-conflict
    name: check for case conflicts
    description: checks for files that would conflict in case-insensitive filesystems.
    entry: check-case-conflict
    language: python
-   id: check-docstring-first
    name: check docstring is first (deprecated)
    description: checks a common error of defining a docstring after code.
    entry: check-docstring-first
    language: python
    types: [python]
-   id: check-executables-have-shebangs
    name: check that executables have shebangs
    description: ensures that (non-binary) executables have a shebang.
    entry: check-executables-have-shebangs
    language: python
    types: [text, executable]
    stages: [pre-commit, pre-push, manual]
    minimum_pre_commit_version: 3.2.0
-   id: check-illegal-windows-names
    name: check illegal windows names
    entry: Illegal Windows filenames detected
    language: fail
    files: '(?i)((^|/)(CON|PRN|AUX|NUL|COM[\d¹²³]|LPT[\d¹²³])(\.|/|$)|[<>:\"\\|?*\x00-\x1F]|/[^/]*[\.\s]/|[^/]*[\.\s]$)'
-   id: check-json
    name: check json
    description: checks json files for parseable syntax.
    entry: check-json
    language: python
    types: [json]
-   id: check-shebang-scripts-are-executable
    name: check that scripts with shebangs are executable
    description: ensures that (non-binary) files with a shebang are executable.
    entry: check-shebang-scripts-are-executable
    language: python
    types: [text]
    stages: [pre-commit, pre-push, manual]
    minimum_pre_commit_version: 3.2.0
-   id: pretty-format-json
    name: pretty format json
    description: sets a standard for formatting json files.
    entry: pretty-format-json
    language: python
    types: [json]
-   id: check-merge-conflict
    name: check for merge conflicts
    description: checks for files that contain merge conflict strings.
    entry: check-merge-conflict
    language: python
    types: [text]
-   id: check-symlinks
    name: check for broken symlinks
    description: checks for symlinks which do not point to anything.
    entry: check-symlinks
    language: python
    types: [symlink]
-   id: check-toml
    name: check toml
    description: checks toml files for parseable syntax.
    entry: check-toml
    language: python
    types: [toml]
-   id: check-vcs-permalinks
    name: check vcs permalinks
    description: ensures that links to vcs websites are permalinks.
    entry: check-vcs-permalinks
    language: python
    types: [text]
-   id: check-xml
    name: check xml
    description: checks xml files for parseable syntax.
    entry: check-xml
    language: python
    types: [xml]
-   id: check-yaml
    name: check yaml
    description: checks yaml files for parseable syntax.
    entry: check-yaml
    language: python
    types: [yaml]
-   id: debug-statements
    name: debug statements (python)
    description: checks for debugger imports and py37+ `breakpoint()` calls in python source.
    entry: debug-statement-hook
    language: python
    types: [python]
-   id: destroyed-symlinks
    name: detect destroyed symlinks
    description: detects symlinks which are changed to regular files with a content of a path which that symlink was pointing to.
    entry: destroyed-symlinks
    language: python
    types: [file]
    stages: [pre-commit, pre-push, manual]
-   id: detect-aws-credentials
    name: detect aws credentials
    description: detects *your* aws credentials from the aws cli credentials file.
    entry: detect-aws-credentials
    language: python
    types: [text]
-   id: detect-private-key
    name: detect private key
    description: detects the presence of private keys.
    entry: detect-private-key
    language: python
    types: [text]
-   id: double-quote-string-fixer
    name: fix double quoted strings
    description: replaces double quoted strings with single quoted strings.
    entry: double-quote-string-fixer
    language: python
    types: [python]
-   id: end-of-file-fixer
    name: fix end of files
    description: ensures that a file is either empty, or ends with one newline.
    entry: end-of-file-fixer
    language: python
    types: [text]
    stages: [pre-commit, pre-push, manual]
    minimum_pre_commit_version: 3.2.0
-   id: file-contents-sorter
    name: file contents sorter
    description: sorts the lines in specified files (defaults to alphabetical). you must provide list of target files as input in your .pre-commit-config.yaml file.
    entry: file-contents-sorter
    language: python
    files: '^$'
-   id: fix-byte-order-marker
    name: fix utf-8 byte order marker
    description: removes utf-8 byte order marker.
    entry: fix-byte-order-marker
    language: python
    types: [text]
-   id: fix-encoding-pragma
    name: fix python encoding pragma (removed)
    description: (removed) use pyupgrade instead.
    entry: pre-commit-hooks-removed fix-encoding-pragma pyupgrade https://github.com/asottile/pyupgrade
    language: python
    types: [python]
-   id: forbid-new-submodules
    name: forbid new submodules
    description: prevents addition of new git submodules.
    language: python
    entry: forbid-new-submodules
    types: [directory]
-   id: forbid-submodules
    name: forbid submodules
    description: forbids any submodules in the repository
    language: fail
    entry: 'submodules are not allowed in this repository:'
    types: [directory]
-   id: mixed-line-ending
    name: mixed line ending
    description: replaces or checks mixed line ending.
    entry: mixed-line-ending
    language: python
    types: [text]
-   id: name-tests-test
    name: python tests naming
    description: verifies that test files are named correctly.
    entry: name-tests-test
    language: python
    files: (^|/)tests/.+\.py$
-   id: no-commit-to-branch
    name: "don't commit to branch"
    entry: no-commit-to-branch
    language: python
    pass_filenames: false
    always_run: true
-   id: requirements-txt-fixer
    name: fix requirements.txt
    description: sorts entries in requirements.txt.
    entry: requirements-txt-fixer
    language: python
    files: (requirements|constraints).*\.txt$
-   id: sort-simple-yaml
    name: sort simple yaml files
    description: sorts simple yaml files which consist only of top-level keys, preserving comments and blocks.
    language: python
    entry: sort-simple-yaml
    files: '^$'
-   id: trailing-whitespace
    name: trim trailing whitespace
    description: trims trailing whitespace.
    entry: trailing-whitespace-fixer
    language: python
    types: [text]
    stages: [pre-commit, pre-push, manual]
    minimum_pre_commit_version: 3.2.0
```

## File: `CHANGELOG.md`
```markdown
6.0.0 - 2025-08-09
==================

## Fixes
- `check-shebang-scripts-are-executable`: improve error message.
    - #1115 PR by @homebysix.

## Migrating
- now requires python >= 3.9.
    - #1098 PR by @asottile.
- `file-contents-sorter`: disallow `--unique` and `--ignore-case` at the same
  time.
    - #1095 PR by @nemacysts.
    - #794 issue by @teksturi.
- Removed `check-byte-order-marker` and `fix-encoding-pragma`.
    - `check-byte-order-marker`: migrate to `fix-byte-order-marker`.
    - `fix-encoding-pragma`: migrate to `pyupgrade`.
    - #1034 PR by @mxr.
    - #1032 issue by @mxr.
    - #522 PR by @jgowdy.

5.0.0 - 2024-10-05
==================

### Features
- `requirements-txt-fixer`: also remove `pkg_resources==...`.
    - #850 PR by @ericfrederich.
    - #1030 issue by @ericfrederich.
- `check-illegal-windows-names`: new hook!
    - #1044 PR by @ericfrederich.
    - #589 issue by @ericfrederich.
    - #1049 PR by @Jeffrey-Lim.
- `pretty-format-json`: continue processing even if a file has a json error.
    - #1039 PR by @amarvin.
    - #1038 issue by @amarvin.

### Fixes
- `destroyed-symlinks`: set `stages` to `[pre-commit, pre-push, manual]`
    - PR #1085 by @AdrianDC.

### Migrating
- pre-commit-hooks now requires `pre-commit>=3.2.0`.
- use non-deprecated names for `stages`.
    - #1093 PR by @asottile.

4.6.0 - 2024-04-06
==================

### Features
- `requirements-txt-fixer`: remove duplicate packages.
    - #1014 PR by @vhoulbreque-withings.
    - #960 issue @csibe17.

### Migrating
- `fix-encoding-pragma`: deprecated -- will be removed in 5.0.0.  use
  [pyupgrade](https://github.com/asottile/pyupgrade) or some other tool.
    - #1033 PR by @mxr.
    - #1032 issue by @mxr.

4.5.0 - 2023-10-07
==================

### Features
- `requirements-txt-fixer`: also sort `constraints.txt` by default.
    - #857 PR by @lev-blit.
    - #830 issue by @PLPeeters.
- `debug-statements`: add `bpdb` debugger.
    - #942 PR by @mwip.
    - #941 issue by @mwip.

### Fixes
- `file-contents-sorter`: fix sorting an empty file.
    - #944 PR by @RoelAdriaans.
    - #935 issue by @paduszyk.
- `double-quote-string-fixer`: don't rewrite inside f-strings in 3.12+.
    - #973 PR by @asottile.
    - #971 issue by @XuehaiPan.

## Migrating
- now requires python >= 3.8.
    - #926 PR by @asottile.
    - #927 PR by @asottile.

4.4.0 - 2022-11-23
==================

### Features
- `forbid-submodules`: new hook which outright bans submodules.
    - #815 PR by @asottile.
    - #707 issue by @ChiefGokhlayeh.

4.3.0 - 2022-06-07
==================

### Features
- `check-executables-have-shebangs`: use `git config core.fileMode` to
  determine if it should query `git`.
    - #730 PR by @Kurt-von-Laven.
- `name-tests-test`: add `--pytest-test-first` test convention.
    - #779 PR by @asottile.

### Fixes
- `check-shebang-scripts-are-executable`: update windows instructions.
    - #774 PR by @mdeweerd.
    - #770 issue by @mdeweerd.
- `check-toml`: use stdlib `tomllib` when available.
    - #771 PR by @DanielNoord.
    - #755 issue by @sognetic.
- `check-added-large-files`: don't run on non-file `stages`.
    - #778 PR by @asottile.
    - #777 issue by @skyj.

4.2.0 - 2022-04-06
==================

### Features
- `name-tests-test`: updated display text.
    - #713 PR by @asottile.
- `check-docstring-first`: make output more parsable.
    - #748 PR by @asottile.
- `check-merge-conflict`: make output more parsable.
    - #748 PR by @asottile.
- `debug-statements`: make output more parsable.
    - #748 PR by @asottile.

### Fixes
- `check-merge-conflict`: fix detection of `======` conflict marker on windows.
    - #748 PR by @asottile.

### Updating
- Drop python<3.7.
    - #719 PR by @asottile.
- Changed default branch from `master` to `main`.
    - #744 PR by @asottile.

4.1.0 - 2021-12-22
==================

### Features
- `debug-statements`: add `pdbr` debugger.
    - #614 PR by @cansarigol.
- `detect-private-key`: add detection for additional key types.
    - #658 PR by @ljmf00.
- `check-executables-have-shebangs`: improve messaging on windows.
    - #689 PR by @pujitm.
    - #686 issue by @jmerdich.
- `check-added-large-files`: support `--enforce-all` with `git-lfs`.
    - #674 PR by @amartani.
    - #560 issue by @jeremy-coulon.

### Fixes
- `check-case-conflict`: improve performance.
    - #626 PR by @guykisel.
    - #625 issue by @guykisel.
- `forbid-new-submodules`: fix false-negatives for `pre-push`.
    - #619 PR by @m-khvoinitsky.
    - #609 issue by @m-khvoinitsky.
- `check-merge-conflict`: fix execution in git worktrees.
    - #662 PR by @errsyn.
    - #638 issue by @daschuer.

### Misc.
- Normalize case of hook names and descriptions.
    - #671 PR by @dennisroche.
    - #673 PR by @revolter.

4.0.1 - 2021-05-16
==================

### Fixes
- `check-shebang-scripts-are-executable` fix entry point.
    - #602 issue by @Person-93.
    - #603 PR by @scop.

4.0.0 - 2021-05-14
==================

### Features
- `check-json`: report duplicate keys.
    - #558 PR by @AdityaKhursale.
    - #554 issue by @adamchainz.
- `no-commit-to-branch`: add `main` to default blocked branches.
    - #565 PR by @ndevenish.
- `check-case-conflict`: check conflicts in directory names as well.
    - #575 PR by @slsyy.
    - #70 issue by @andyjack.
- `check-vcs-permalinks`: forbid other branch names.
    - #582 PR by @jack1142.
    - #581 issue by @jack1142.
- `check-shebang-scripts-are-executable`: new hook which ensures shebang'd
  scripts are executable.
    - #545 PR by @scop.

### Fixes
- `check-executables-have-shebangs`: Short circuit shebang lookup on windows.
    - #544 PR by @scop.
- `requirements-txt-fixer`: Fix comments which have indentation
    - #549 PR by @greshilov.
    - #548 issue by @greshilov.
- `pretty-format-json`: write to stdout using UTF-8 encoding.
    - #571 PR by @jack1142.
    - #570 issue by @jack1142.
- Use more inclusive language.
    - #599 PR by @asottile.

### Breaking changes
- Remove deprecated hooks: `flake8`, `pyflakes`, `autopep8-wrapper`.
    - #597 PR by @asottile.


3.4.0 - 2020-12-15
==================

### Features
- `file-contents-sorter`: Add `--unique` argument
    - #524 PR by @danielhoherd.
- `check-vcs-permalinks`: Add `--additional-github-domain` option
    - #530 PR by @youngminz.
- New hook: `destroyed-symlinks` to detect unintentional symlink-breakages on
  windows.
    - #511 PR by @m-khvoinitsky.

3.3.0 - 2020-10-20
==================

### Features
- `file-contents-sorter`: add `--ignore-case` option for case-insensitive
  sorting
    - #514 PR by @Julian.
- `check-added-large-files`: add `--enforce-all` option to check non-added
  files as well
    - #519 PR by @mshawcroft.
    - #518 issue by @mshawcroft.
- `fix-byte-order-marker`: new hook which fixes UTF-8 byte-order marker.
    - #522 PR by @jgowdy.

### Deprecations
- `check-byte-order-marker` is now deprecated for `fix-byte-order-marker`

3.2.0 - 2020-07-30
==================

### Features
- `debug-statements`: add support for `pydevd_pycharm` debugger
    - #502 PR by @jgeerds.

### Fixes
- `check-executables-have-shebangs`: fix git-quoted files on windows (spaces,
  non-ascii, etc.)
    - #509 PR by @pawamoy.
    - #508 issue by @pawamoy.

3.1.0 - 2020-05-20
==================

### Features
- `check-executables-have-shebangs`: on windows, validate the mode bits using
  `git`
    - #480 PR by @mxr.
    - #435 issue by @dstandish.
- `requirements-txt-fixer`: support more operators
    - #483 PR by @mxr.
    - #331 issue by @hackedd.

### Fixes
- `pre-commit-hooks-removed`: Fix when removed hooks used `args`
    - #487 PR by @pedrocalleja.
    - #485 issue by @pedrocalleja.

3.0.1 - 2020-05-16
==================

### Fixes
- `check-toml`: use UTF-8 encoding to load toml files
    - #479 PR by @mxr.
    - #474 issue by @staticdev.

3.0.0 - 2020-05-14
==================

### Features
- `detect-aws-credentials`: skip empty aws keys
    - #450 PR by @begoon.
    - #449 issue by @begoon.
- `debug-statements`: add detection `wdb` debugger
    - #452 PR by @itsdkey.
    - #451 issue by @itsdkey.
- `requirements-txt-fixer`: support line continuation for dependencies
    - #469 PR by @aniketbhatnagar.
    - #465 issue by @aniketbhatnagar.

### Fixes
- `detect-aws-credentials`: fix `UnicodeDecodeError` when running on non-UTF8
  files.
    - #453 PR by @asottile.
    - #393 PR by @a7p
    - #346 issue by @rpdelaney.

### Updating
- pre-commit/pre-commit-hooks now requires python3.6.1+
    - #447 PR by @asottile.
    - #455 PR by @asottile.
- `flake8` / `pyflakes` have been removed, use `flake8` from `pycqa/flake8`
  instead:

  ```yaml
  -   repo: https://gitlab.com/pycqa/flake8
      rev: 3.8.1
      hooks:
      -   id: flake8
  ```

    - #476 PR by @asottile.
    - #477 PR by @asottile.
    - #344 issue by @asottile.


2.5.0 - 2020-02-04
==================

### Fixes
- Fix sorting of requirements which use `egg=...`
    - #425 PR by @vinayinvicible.
- Fix over-eager regular expression for test filename matching
    - #429 PR by @rrauenza.

### Updating
- Use `flake8` from `pycqa/flake8` instead:

  ```yaml
  -   repo: https://gitlab.com/pycqa/flake8
      rev: 3.7.9
      hooks:
      -   id: flake8
  ```

2.4.0 - 2019-10-28
==================

### Features
- Add diff output to `pretty-format-json` when run without `--autofix`.
    - #408 PR by @joepin.
- Add `--chars` option to `trailing-whitespace` fixer to control which
  characters are stripped instead of all whitespace.
    - #421 PR by @iconmaster5326.

### Fixes
- Fix `requirements-txt-fixer` when file does not end in a newline.
    - #414 issue by @barakreif.
    - #415 PR by @barakreif.
- Fix double printing of filename in `pretty-format-json`.
    - #419 PR by @asottile.

2.3.0 - 2019-08-05
==================

### Features
- Add `rpdb` to detected debuggers in `debug-statements`
    - #389 PR by @danlamanna.
- Add `check-toml` hook
    - #400 PR by @MarSoft.
    - #400 PR by @ssbarnea.

### Fixes
- Add `__main__` block to `pre_commit.file_contents_sorter` so it can be
  invoked using `python -m`
    - #405 PR by @squeaky-pl.

### Misc.
- Fix `git-lfs` tests in azure pipelines
    - #403 PR by @ssbarnea.

2.2.3 - 2019-05-16
==================

### Fixes
- Handle CRLF line endings in `double-quote-string-fixer`
    - #385 issue by @Trim21.
    - #386 PR by @asottile.

2.2.2 - 2019-05-15
==================

### Fixes
- Handle CRLF line endings in `fix-encoding-pragma`
    - #384 PR by @asottile.

2.2.1 - 2019-04-21
==================

### Fixes
- Use UTF-8 to load yaml files
    - #377 issue by @roottool.
    - #378 PR by @roottool.

2.2.0 - 2019-04-20
==================

### Features
- Switch from `pyyaml` to `ruamel.yaml`
    - This enforces (among other things) duplicate key checking in yaml.
    - #351 PR by @asottile.
- Add a new `--pattern` option to `no-commit-to-branch` for regex matching
  branch names.
    - #375 issue by @marcjay.
    - #376 PR by @marcjay.

### Fixes
- Set `require_serial: true` for flake8
    - flake8 internally uses multiprocessing.
    - #358 PR by @asottile.
- Don't run `check-executables-have-shebangs` / `trailing-whitespace` hooks
  during the `commit-msg` stage.
    - #361 issue by @revolter.
    - #362 PR by @revolter.
- Run `check-byte-order-marker` against `types: [text]`
    - #371 PR by @tobywf.
    - #372 PR by @tobywf.
- Do not require UTF-8-encoded files for `check-docstring-first`
    - #345 issue by @x007007007.
    - #374 PR by @asottile.

### Misc.
- `pre-commit-hooks` now is type checked with mypy.
    - #360 PR by @asottile.

2.1.0 - 2018-12-26
==================

### Features
- Detect PGP/GPG private keys in `detect-private-key`
    - #329 PR by @rpdelaney.
- Report filenames when fixing files in `mixed-line-endings`
    - #341 PR by @gimbo.
    - #340 issuey by @gimbo.

### Fixes
- Handle CRLF / CR line endings in `end-of-file-fixer`
    - #327 PR by @mtkennerly.

### Docs

- Clarify and document arguments for `detect-aws-credentials`
    - #333 PR by @rpdelaney.
- Clarify `autopep8-wrapper` is deprecated in description
    - #343 PR by @TheKevJames.


2.0.0 - 2018-10-12
==================

### Breaking changes

- `autopep8-wrapper` has been moved to
  [pre-commit/mirrors-autopep8][mirrors-autopep8]
    - #92 issue by @asottile.
    - #319 issue by @blaggacao.
    - #321 PR by @asottile.
- `trailing-whitespace` defaults to `--no-markdown-linebreak-ext`
    - #310 issue by @asottile.
    - #324 PR by @asottile.
- `hooks.yaml` (legacy pre-commit hook metadata) deleted
    - #323 PR by @asottile.
- pre-`types` compatibility metadata removed
    - #323 PR @asottile.

### Docs

- Correct documentation for `no-commit-to-branch`
    - #318 PR by @milin.

### Updating

- Minimum supported version of `pre-commit` is now 0.15.0
- Use `autopep8` from [pre-commit/mirrors-autopep8][mirrors-autopep8]
- To keep mardown hard linebreaks, for `trailing-whitespace` use
  `args: [--markdown-linebreak-ext=md,markdown]` (the previous default value)

[mirrors-autopep8]: https://github.com/pre-commit/mirrors-autopep8

1.4.0-1 - 2018-09-27
====================

(Note: this is a tag-only release as no code changes occurred)

### Fixes
- Don't run `end-of-file-fixer` during `commit-msg` stage
    - #315 issue by @revolter.
    - #317 PR by @revolter.

1.4.0 - 2018-07-22
==================

### Features
- `no-commit-to-branch`: allow `--branch` to be specified multiple times
    - #190 PR by @moas.
    - #294 PR by @asottile.
- `check-merge-conflict`: add `--assume-in-merge` to force checks outside of a
  merge commit situation
    - #300 issue by @vinayinvicible.
    - #301 PR by @vinayinvicible.

### Fixes
- Don't match whitespace in VCS urls
    - #293 PR by @asottile.
- Fix invalid escape sequences
    - #296 PR by @asottile.
- Fix `ResourcesWarning`s
    - #297 PR by @asottile.

### Misc
- Test against python3.7
    - #304 PR by @expobrain.

1.3.0 - 2018-05-28
==================

### Features
- Add an `--unsafe` argument to `check-yaml` to allow custom yaml tags
    - #273 issue by @blackillzone.
    - #274 PR by @asottile.
- Automatically remove `pkg-resources==0.0.0` in `requirements-txt-fixer`
    - #275 PR by @nvtkaszpir.
- Detect `breakpoint()` (python3.7+) in `debug-statements` hook.
    - #283 PR by @asottile.
- Detect sshcom and putty hooks in `detect-private-key`
    - #287 PR by @vin01.

### Fixes
- Open files as UTF-8 (`autopep8-wrapper`, `check-docstring-first`,
  `double-quote-string-fixer`)
    - #279 PR by @nvtkaszpir.
- Fix `AttributeError` in `check-builtin-literals` for some functions
    - #285 issue by @EgoWumpus.
    - #286 PR by @asottile.

1.2.3 - 2018-02-28
==================

### Fixes
- `trailing-whitespace` entrypoint was incorrect.
    - f6780b9 by @asottile.

1.2.2 - 2018-02-28
==================

### Fixes
- `trailing-whitespace` no longer adds a missing newline at end-of-file
    - #270 issue by @fractos.
    - #271 PR by @asottile.

1.2.1-1 - 2018-02-24
====================

(Note: this is a tag-only release as no code changes occurred)

### Fixes:
- Don't pass filenames for `no-commit-to-branch`
    - #268 issue by @dongyuzheng.
    - #269 PR by @asottile.

1.2.1 - 2018-02-19
==================
### Fixes:
- `detect-aws-credentials` false positive when key was empty
    - #258 issue by @PVSec.
    - #260 PR by @PVSec.
- `no-commit-to-branch` no longer crashes when not on a branch
    - #265 issue by @hectorv.
    - #266 PR by @asottile.

1.2.0 - 2018-01-13
==================
### Features:
- Add new `check-builtin-literals` hook.
    - #249 #251 PR by @benwebber.
- `pretty-format-json` no longer depends on `simplejson`.
    - #254 PR by @cas--.
- `detect-private-key` now detects gcp keys.
    - #255 issue by @SaMnCo @nicain.
    - #256 PR by @nicain.

1.1.1 - 2017-10-19
==================
### Fixes:
- Fix output interleaving in `check-vcs-permalinks` under python3.
    - #245 PR by @asottile.

1.1.0 - 2017-10-12
==================
### Features:
- `check-yaml` gains a `--allow-multiple-documents` (`-m`) argument to allow
  linting of files using the
  [multi document syntax](http://www.yaml.org/spec/1.2/spec.html#YAML)
    - pre-commit/pre-commit#635 issue by @geekobi.
    - #244 PR by @asottile.

1.0.0 - 2017-10-09
==================
### Features:
- New hook: `check-vcs-permalinks` for ensuring permalinked github urls.
    - #241 PR by @asottile.

### Fixes:
- Fix `trailing-whitespace` for non-utf8 files on macos
    - #242 PR by @asottile.
- Fix `requirements-txt-fixer` for files ending in comments
    - #243 PR by @asottile.

0.9.5 - 2017-09-27
==================
- Fix mixed-line-endings `--fix=...` when whole file is a different ending

0.9.4 - 2017-09-19
==================
- Fix entry point for `mixed-line-ending`

0.9.3 - 2017-09-07
==================
- New hook: `mixed-line-ending`

0.9.2 - 2017-08-21
==================
- Report full python version in `check-ast`.
- Apply a more strict regular expression for `name-tests-test`
- Upgrade binding for `git-lfs` for `check-added-large-files`.  The oldest
  version that is supported is 2.2.1 (2.2.0 will incorrectly refer to all
  files as "lfs" (false negative) and earlier versions will crash.
- `debug-statements` now works for non-utf-8 files.

0.9.1 - 2017-07-02
==================
- Add `check-executables-have-shebangs` hook.

0.9.0 - 2017-07-02
==================
- Add `sort-simple-yaml` hook
- Fix `requirements-txt-fixer` for empty files
- Add `file-contents-sorter` hook for sorting flat files
- `check-merge-conflict` now recognizes rebase conflicts
- Metadata now uses `types` (and therefore requires pre-commit 0.15.0).  This
  allows the text processing hooks to match *all* text files (and to match
  files which would only be classifiable by their shebangs).

0.8.0 - 2017-06-06
==================
- Add flag allowing missing keys to `detect-aws-credentials`
- Handle django default `tests.py` in `name-tests-test`
- Add `--no-ensure-ascii` option to `pretty-format-json`
- Add `no-commit-to-branch` hook

0.7.1 - 2017-02-07
==================
- Don't false positive on files where trailing whitespace isn't changed.

0.7.0 - 2017-01-21
==================
- Improve search for detecting aws keys
- Add .pre-commit-hooks.yaml for forward compatibility

0.6.1 - 2016-11-30
==================
- trailing-whitespace-hook: restore original file on catastrophic failure
- trailing-whitespace-hook: support crlf
- check-yaml: Use safe_load
- check-json: allow custom key sort
- check-json: display filename for non-utf8 files
- New hook: forbid-new-submodules

0.6.0 - 2016-08-12
==================
- Merge conflict detection no longer crashes on binary files
- Indentation in json may be an arbitrary separator
- Editable requirements are properly sorted
- Encoding pragma fixer pragma is configurable

0.5.1 - 2016-05-16
==================
- Add a --no-sort-keys to json pretty formatter
- Add a --remove to fix-encoding-pragma

0.5.0 - 2016-04-05
==================
- Add check-byte-order-marker
- Add check-synlinks
- check-large-files-added understands git-lfs
- Support older git
- Fix regex for --django in test name checker
- Add fix-encoding-pragma hook
- requirements-txt-fixer now sorts like latest pip
- Add check-ast hook
- Add detect-aws-credentials hook
- Allow binary files to pass private key hook
- Add pretty-format-json hook

0.4.2 - 2015-05-31
==================
- Add --django to test name checker
- Add check-merge-conflict hook
- Remove dependency on plumbum
- Add q as a debug statement
- Don't detect markup titles as conflicts
- Teach trailing-whitespace about markdown
- Quickfix for pyflakes - flake8 version conflict

0.4.1 - 2015-03-08
==================
- Respect configuration when running autopep8
- Quickfix for pep8 version conflicts

0.4.0 - 2015-02-22
==================
- Fix trailing-whitespace on OS X
- Add check-added-large-files hook
- Add check-docstring-first hook
- Add requirements-txt-fixer hook
- Add check-case-conflict hook
- Use yaml's CLoader when available in check-yaml for more speed
- Add check-xml hook
- Fix end-of-file-fixer for windows
- Add double-quote-string-fixer hook

0.3.0 - 2014-08-22
==================
- Add autopep8-wrapper hook

0.2.0 - 2014-08-19
==================
- Add check-json hook

0.1.1 - 2014-06-19
==================
- Don't crash on non-parseable files for debug-statement-hook

0.1.0 - 2014-06-07
==================
- Initial Release
```

## File: `LICENSE`
```
Copyright (c) 2014 pre-commit dev team: Anthony Sottile, Ken Struys

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
  - `--allow-multiple-documents` - allow yaml files which use the
    [multi-document syntax](http://www.yaml.org/spec/1.2/spec.html#YAML)
  - `--unsafe` - Instead of loading the files, simply parse them for syntax.
    A syntax-only check enables extensions and unsafe constructs which would
    otherwise be forbidden.  Using this option removes all guarantees of
    portability to other yaml implementations.
    Implies `--allow-multiple-documents`.

#### `debug-statements`
Check for debugger imports and py37+ `breakpoint()` calls in python source.

#### `destroyed-symlinks`
Detects symlinks which are changed to regular files with a content of a path
which that symlink was pointing to.
This usually happens on Windows when a user clones a repository that has
symlinks but they do not have the permission to create symlinks.

#### `detect-aws-credentials`
Checks for the existence of AWS secrets that you have set up with the AWS CLI.
The following arguments are available:
- `--credentials-file CREDENTIALS_FILE` - additional AWS CLI style
  configuration file in a non-standard location to fetch configured
  credentials from. Can be repeated multiple times.
- `--allow-missing-credentials` - Allow hook to pass when no credentials are detected.

#### `detect-private-key`
Checks for the existence of private keys.

#### `double-quote-string-fixer`
This hook replaces double quoted strings with single quoted strings.

#### `end-of-file-fixer`
Makes sure files end in a newline and only a newline.

#### `file-contents-sorter`
Sort the lines in specified files (defaults to alphabetical).
You must provide the target [`files`](https://pre-commit.com/#config-files) as input.
Note that this hook WILL remove blank lines and does NOT respect any comments.
All newlines will be converted to line feeds (`\n`).

The following arguments are available:
- `--ignore-case` - fold lower case to upper case characters.
- `--unique` - ensure each line is unique.

#### `fix-byte-order-marker`
removes UTF-8 byte order marker

#### `forbid-new-submodules`
Prevent addition of new git submodules.

This is intended as a helper to migrate away from submodules.  If you want to
ban them entirely use `forbid-submodules`

#### `forbid-submodules`
forbids any submodules in the repository.

#### `mixed-line-ending`
Replaces or checks mixed line ending.
  - `--fix={auto,crlf,lf,no}`
      - `auto` - Replaces automatically the most frequent line ending. This is the default argument.
      - `crlf`, `lf` - Forces to replace line ending by respectively CRLF and LF.
          - This option isn't compatible with git setup check-in LF check-out CRLF as git smudge this later than the hook is invoked.
      - `no` - Checks if there is any mixed line ending without modifying any file.

#### `name-tests-test`
verifies that test files are named correctly.
- `--pytest` (the default): ensure tests match `.*_test\.py`
- `--pytest-test-first`: ensure tests match `test_.*\.py`
- `--django` / `--unittest`: ensure tests match `test.*\.py`

#### `no-commit-to-branch`
Protect specific branches from direct checkins.
  - Use `args: [--branch, staging, --branch, main]` to set the branch.
    Both `main` and `master` are protected by default if no branch argument is set.
  - `-b` / `--branch` may be specified multiple times to protect multiple
    branches.
  - `-p` / `--pattern` can be used to protect branches that match a supplied regex
    (e.g. `--pattern, release/.*`). May be specified multiple times.

Note that `no-commit-to-branch` is configured by default to [`always_run`](https://pre-commit.com/#config-always_run).
As a result, it will ignore any setting of [`files`](https://pre-commit.com/#config-files),
[`exclude`](https://pre-commit.com/#config-exclude), [`types`](https://pre-commit.com/#config-types)
or [`exclude_types`](https://pre-commit.com/#config-exclude_types).
Set [`always_run: false`](https://pre-commit.com/#config-always_run) to allow this hook to be skipped according to these
file filters. Caveat: In this configuration, empty commits (`git commit --allow-empty`) would always be allowed by this hook.

#### `pretty-format-json`
Checks that all your JSON files are pretty.  "Pretty"
here means that keys are sorted and indented.  You can configure this with
the following commandline options:
  - `--autofix` - automatically format json files
  - `--indent ...` - Control the indentation (either a number for a number of spaces or a string of whitespace).  Defaults to 2 spaces.
  - `--no-ensure-ascii` preserve unicode characters instead of converting to escape sequences
  - `--no-sort-keys` - when autofixing, retain the original key ordering (instead of sorting the keys)
  - `--top-keys comma,separated,keys` - Keys to keep at the top of mappings.

#### `requirements-txt-fixer`
Sorts entries in requirements.txt and constraints.txt and removes incorrect entry for `pkg-resources==0.0.0`

#### `sort-simple-yaml`
Sorts simple YAML files which consist only of top-level
keys, preserving comments and blocks.

Note that `sort-simple-yaml` by default matches no `files` as it enforces a
very specific format.  You must opt in to this by setting [`files`](https://pre-commit.com/#config-files), for example:

```yaml
    -   id: sort-simple-yaml
        files: ^config/simple/
```


#### `trailing-whitespace`
Trims trailing whitespace.
  - To preserve Markdown [hard linebreaks](https://github.github.com/gfm/#hard-line-break)
    use `args: [--markdown-linebreak-ext=md]` (or other extensions used
    by your markdownfiles).  If for some reason you want to treat all files
    as markdown, use `--markdown-linebreak-ext=*`.
  - By default, this hook trims all whitespace from the ends of lines.
    To specify a custom set of characters to trim instead, use `args: [--chars,"<chars to trim>"]`.

### Deprecated / replaced hooks

- `check-byte-order-marker`: instead use fix-byte-order-marker
- `fix-encoding-pragma`: instead use [`pyupgrade`](https://github.com/asottile/pyupgrade)
- `check-docstring-first`: fundamentally flawed, deprecated without replacement.


### As a standalone package

If you'd like to use these hooks, they're also available as a standalone package.

Simply `pip install pre-commit-hooks`
```

## File: `requirements-dev.txt`
```
covdefaults
coverage
pytest
```

## File: `setup.cfg`
```
[metadata]
name = pre_commit_hooks
version = 6.0.0
description = Some out-of-the-box hooks for pre-commit.
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/pre-commit/pre-commit-hooks
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
    ruamel.yaml>=0.15
    tomli>=1.1.0;python_version<"3.11"
python_requires = >=3.10

[options.packages.find]
exclude =
    tests*
    testing*

[options.entry_points]
console_scripts =
    check-added-large-files = pre_commit_hooks.check_added_large_files:main
    check-ast = pre_commit_hooks.check_ast:main
    check-builtin-literals = pre_commit_hooks.check_builtin_literals:main
    check-case-conflict = pre_commit_hooks.check_case_conflict:main
    check-docstring-first = pre_commit_hooks.check_docstring_first:main
    check-executables-have-shebangs = pre_commit_hooks.check_executables_have_shebangs:main
    check-json = pre_commit_hooks.check_json:main
    check-merge-conflict = pre_commit_hooks.check_merge_conflict:main
    check-shebang-scripts-are-executable = pre_commit_hooks.check_shebang_scripts_are_executable:main
    check-symlinks = pre_commit_hooks.check_symlinks:main
    check-toml = pre_commit_hooks.check_toml:main
    check-vcs-permalinks = pre_commit_hooks.check_vcs_permalinks:main
    check-xml = pre_commit_hooks.check_xml:main
    check-yaml = pre_commit_hooks.check_yaml:main
    debug-statement-hook = pre_commit_hooks.debug_statement_hook:main
    destroyed-symlinks = pre_commit_hooks.destroyed_symlinks:main
    detect-aws-credentials = pre_commit_hooks.detect_aws_credentials:main
    detect-private-key = pre_commit_hooks.detect_private_key:main
    double-quote-string-fixer = pre_commit_hooks.string_fixer:main
    end-of-file-fixer = pre_commit_hooks.end_of_file_fixer:main
    file-contents-sorter = pre_commit_hooks.file_contents_sorter:main
    fix-byte-order-marker = pre_commit_hooks.fix_byte_order_marker:main
    forbid-new-submodules = pre_commit_hooks.forbid_new_submodules:main
    mixed-line-ending = pre_commit_hooks.mixed_line_ending:main
    name-tests-test = pre_commit_hooks.tests_should_end_in_test:main
    no-commit-to-branch = pre_commit_hooks.no_commit_to_branch:main
    pre-commit-hooks-removed = pre_commit_hooks.removed:main
    pretty-format-json = pre_commit_hooks.pretty_format_json:main
    requirements-txt-fixer = pre_commit_hooks.requirements_txt_fixer:main
    sort-simple-yaml = pre_commit_hooks.sort_simple_yaml:main
    trailing-whitespace-fixer = pre_commit_hooks.trailing_whitespace_fixer:main

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
envlist = py,pre-commit

[testenv]
deps = -rrequirements-dev.txt
setenv =
    GIT_AUTHOR_NAME = "test"
    GIT_COMMITTER_NAME = "test"
    GIT_AUTHOR_EMAIL = "test@example.com"
    GIT_COMMITTER_EMAIL = "test@example.com"
commands =
    coverage erase
    coverage run -m pytest {posargs:tests}
    coverage report

[testenv:pre-commit]
skip_install = true
deps = pre-commit
commands = pre-commit run --all-files --show-diff-on-failure

[pep8]
ignore=E265,E501,W504
```

## File: `pre_commit_hooks/check_added_large_files.py`
```python
from __future__ import annotations

import argparse
import math
import os
import subprocess
from collections.abc import Sequence

from pre_commit_hooks.util import added_files
from pre_commit_hooks.util import zsplit


def filter_lfs_files(filenames: set[str]) -> None:  # pragma: no cover (lfs)
    """Remove files tracked by git-lfs from the set."""
    if not filenames:
        return

    check_attr = subprocess.run(
        ('git', 'check-attr', 'filter', '-z', '--stdin'),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        encoding='utf-8',
        check=True,
        input='\0'.join(filenames),
    )
    stdout = zsplit(check_attr.stdout)
    for i in range(0, len(stdout), 3):
        filename, filter_tag = stdout[i], stdout[i + 2]
        if filter_tag == 'lfs':
            filenames.remove(filename)


def find_large_added_files(
        filenames: Sequence[str],
        maxkb: int,
        *,
        enforce_all: bool = False,
) -> int:
    # Find all added files that are also in the list of files pre-commit tells
    # us about
    retv = 0
    filenames_filtered = set(filenames)
    filter_lfs_files(filenames_filtered)

    if not enforce_all:
        filenames_filtered &= added_files()

    for filename in filenames_filtered:
        kb = math.ceil(os.stat(filename).st_size / 1024)
        if kb > maxkb:
            print(f'{filename} ({kb} KB) exceeds {maxkb} KB.')
            retv = 1

    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--enforce-all', action='store_true',
        help='Enforce all files are checked, not just staged files.',
    )
    parser.add_argument(
        '--maxkb', type=int, default=500,
        help='Maximum allowable KB for added files',
    )
    args = parser.parse_args(argv)

    return find_large_added_files(
        args.filenames,
        args.maxkb,
        enforce_all=args.enforce_all,
    )


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_ast.py`
```python
from __future__ import annotations

import argparse
import ast
import platform
import sys
import traceback
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:

        try:
            with open(filename, 'rb') as f:
                ast.parse(f.read(), filename=filename)
        except SyntaxError:
            impl = platform.python_implementation()
            version = sys.version.split()[0]
            print(f'{filename}: failed parsing with {impl} {version}:')
            tb = '    ' + traceback.format_exc().replace('\n', '\n    ')
            print(f'\n{tb}')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_builtin_literals.py`
```python
from __future__ import annotations

import argparse
import ast
from collections.abc import Sequence
from typing import NamedTuple


BUILTIN_TYPES = {
    'complex': '0j',
    'dict': '{}',
    'float': '0.0',
    'int': '0',
    'list': '[]',
    'str': "''",
    'tuple': '()',
}


class Call(NamedTuple):
    name: str
    line: int
    column: int


class Visitor(ast.NodeVisitor):
    def __init__(
            self,
            ignore: set[str],
            allow_dict_kwargs: bool = True,
    ) -> None:
        self.builtin_type_calls: list[Call] = []
        self.allow_dict_kwargs = allow_dict_kwargs
        self._disallowed = BUILTIN_TYPES.keys() - ignore

    def _check_dict_call(self, node: ast.Call) -> bool:
        return self.allow_dict_kwargs and bool(node.keywords)

    def visit_Call(self, node: ast.Call) -> None:
        if (
            # Ignore functions that are object attributes (`foo.bar()`).
            # Assume that if the user calls `builtins.list()`, they know what
            # they're doing.
            isinstance(node.func, ast.Name) and
            node.func.id in self._disallowed and
            (node.func.id != 'dict' or not self._check_dict_call(node)) and
            not node.args
        ):
            self.builtin_type_calls.append(
                Call(node.func.id, node.lineno, node.col_offset),
            )

        self.generic_visit(node)


def check_file(
        filename: str,
        *,
        ignore: set[str],
        allow_dict_kwargs: bool = True,
) -> list[Call]:
    with open(filename, 'rb') as f:
        tree = ast.parse(f.read(), filename=filename)
    visitor = Visitor(ignore=ignore, allow_dict_kwargs=allow_dict_kwargs)
    visitor.visit(tree)
    return visitor.builtin_type_calls


def parse_ignore(value: str) -> set[str]:
    return set(value.split(','))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--ignore', type=parse_ignore, default=set())

    mutex = parser.add_mutually_exclusive_group(required=False)
    mutex.add_argument('--allow-dict-kwargs', action='store_true')
    mutex.add_argument(
        '--no-allow-dict-kwargs',
        dest='allow_dict_kwargs', action='store_false',
    )
    mutex.set_defaults(allow_dict_kwargs=True)

    args = parser.parse_args(argv)

    rc = 0
    for filename in args.filenames:
        calls = check_file(
            filename,
            ignore=args.ignore,
            allow_dict_kwargs=args.allow_dict_kwargs,
        )
        if calls:
            rc = rc or 1
        for call in calls:
            print(
                f'{filename}:{call.line}:{call.column}: '
                f'replace {call.name}() with {BUILTIN_TYPES[call.name]}',
            )
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_case_conflict.py`
```python
from __future__ import annotations

import argparse
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Sequence

from pre_commit_hooks.util import added_files
from pre_commit_hooks.util import cmd_output


def lower_set(iterable: Iterable[str]) -> set[str]:
    return {x.lower() for x in iterable}


def parents(file: str) -> Iterator[str]:
    path_parts = file.split('/')
    path_parts.pop()
    while path_parts:
        yield '/'.join(path_parts)
        path_parts.pop()


def directories_for(files: set[str]) -> set[str]:
    return {parent for file in files for parent in parents(file)}


def find_conflicting_filenames(filenames: Sequence[str]) -> int:
    repo_files = set(cmd_output('git', 'ls-files').splitlines())
    repo_files |= directories_for(repo_files)
    relevant_files = set(filenames) | added_files()
    relevant_files |= directories_for(relevant_files)
    repo_files -= relevant_files
    retv = 0

    # new file conflicts with existing file
    conflicts = lower_set(repo_files) & lower_set(relevant_files)

    # new file conflicts with other new file
    lowercase_relevant_files = lower_set(relevant_files)
    for filename in set(relevant_files):
        if filename.lower() in lowercase_relevant_files:
            lowercase_relevant_files.remove(filename.lower())
        else:
            conflicts.add(filename.lower())

    if conflicts:
        conflicting_files = [
            x for x in repo_files | relevant_files
            if x.lower() in conflicts
        ]
        for filename in sorted(conflicting_files):
            print(f'Case-insensitivity conflict found: {filename}')
        retv = 1

    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )

    args = parser.parse_args(argv)

    return find_conflicting_filenames(args.filenames)


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_docstring_first.py`
```python
from __future__ import annotations

import argparse
import io
import tokenize
from collections.abc import Sequence
from tokenize import tokenize as tokenize_tokenize

NON_CODE_TOKENS = frozenset((
    tokenize.COMMENT, tokenize.ENDMARKER, tokenize.NEWLINE, tokenize.NL,
    tokenize.ENCODING,
))


def check_docstring_first(src: bytes, filename: str = '<unknown>') -> int:
    """Returns nonzero if the source has what looks like a docstring that is
    not at the beginning of the source.

    A string will be considered a docstring if it is a STRING token with a
    col offset of 0.
    """
    found_docstring_line = None
    found_code_line = None

    tok_gen = tokenize_tokenize(io.BytesIO(src).readline)
    for tok_type, _, (sline, scol), _, _ in tok_gen:
        # Looks like a docstring!
        if tok_type == tokenize.STRING and scol == 0:
            if found_docstring_line is not None:
                print(
                    f'{filename}:{sline}: Multiple module docstrings '
                    f'(first docstring on line {found_docstring_line}).',
                )
                return 1
            elif found_code_line is not None:
                print(
                    f'{filename}:{sline}: Module docstring appears after code '
                    f'(code seen on line {found_code_line}).',
                )
                return 1
            else:
                found_docstring_line = sline
        elif tok_type not in NON_CODE_TOKENS and found_code_line is None:
            found_code_line = sline

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            contents = f.read()
        retv |= check_docstring_first(contents, filename=filename)

    return retv
```

## File: `pre_commit_hooks/check_executables_have_shebangs.py`
```python
"""Check that executable text files have a shebang."""
from __future__ import annotations

import argparse
import shlex
import sys
from collections.abc import Generator
from collections.abc import Sequence
from typing import NamedTuple

from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit

EXECUTABLE_VALUES = frozenset(('1', '3', '5', '7'))


def check_executables(paths: list[str]) -> int:
    fs_tracks_executable_bit = cmd_output(
        'git', 'config', 'core.fileMode', retcode=None,
    ).strip()
    if fs_tracks_executable_bit == 'false':  # pragma: win32 cover
        return _check_git_filemode(paths)
    else:  # pragma: win32 no cover
        retv = 0
        for path in paths:
            if not has_shebang(path):
                _message(path)
                retv = 1

        return retv


class GitLsFile(NamedTuple):
    mode: str
    filename: str


def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile]:
    outs = cmd_output('git', 'ls-files', '-z', '--stage', '--', *paths)
    for out in zsplit(outs):
        metadata, filename = out.split('\t')
        mode, _, _ = metadata.split()
        yield GitLsFile(mode, filename)


def _check_git_filemode(paths: Sequence[str]) -> int:
    seen: set[str] = set()
    for ls_file in git_ls_files(paths):
        is_executable = any(b in EXECUTABLE_VALUES for b in ls_file.mode[-3:])
        if is_executable and not has_shebang(ls_file.filename):
            _message(ls_file.filename)
            seen.add(ls_file.filename)

    return int(bool(seen))


def has_shebang(path: str) -> int:
    with open(path, 'rb') as f:
        first_bytes = f.read(2)

    return first_bytes == b'#!'


def _message(path: str) -> None:
    print(
        f'{path}: marked executable but has no (or invalid) shebang!\n'
        f"  If it isn't supposed to be executable, try: "
        f'`chmod -x {shlex.quote(path)}`\n'
        f'  If on Windows, you may also need to: '
        f'`git add --chmod=-x {shlex.quote(path)}`\n'
        f'  If it is supposed to be executable, double-check its shebang.',
        file=sys.stderr,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    return check_executables(args.filenames)


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_json.py`
```python
from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from typing import Any


def raise_duplicate_keys(
        ordered_pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    d = {}
    for key, val in ordered_pairs:
        if key in d:
            raise ValueError(f'Duplicate key: {key}')
        else:
            d[key] = val
    return d


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'rb') as f:
            try:
                json.load(f, object_pairs_hook=raise_duplicate_keys)
            except ValueError as exc:
                print(f'{filename}: Failed to json decode ({exc})')
                retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_merge_conflict.py`
```python
from __future__ import annotations

import argparse
import os.path
from collections.abc import Sequence

from pre_commit_hooks.util import cmd_output


CONFLICT_PATTERNS = [
    b'<<<<<<< ',
    b'======= ',
    b'=======\r\n',
    b'=======\n',
    b'>>>>>>> ',
]


def is_in_merge() -> bool:
    git_dir = cmd_output('git', 'rev-parse', '--git-dir').rstrip()
    return (
        os.path.exists(os.path.join(git_dir, 'MERGE_MSG')) and
        (
            os.path.exists(os.path.join(git_dir, 'MERGE_HEAD')) or
            os.path.exists(os.path.join(git_dir, 'rebase-apply')) or
            os.path.exists(os.path.join(git_dir, 'rebase-merge'))
        )
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--assume-in-merge', action='store_true')
    args = parser.parse_args(argv)

    if not is_in_merge() and not args.assume_in_merge:
        return 0

    retcode = 0
    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile, start=1):
                for pattern in CONFLICT_PATTERNS:
                    if line.startswith(pattern):
                        print(
                            f'{filename}:{i}: Merge conflict string '
                            f'{pattern.strip().decode()!r} found',
                        )
                        retcode = 1

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_shebang_scripts_are_executable.py`
```python
"""Check that text files with a shebang are executable."""
from __future__ import annotations

import argparse
import shlex
import sys
from collections.abc import Sequence

from pre_commit_hooks.check_executables_have_shebangs import EXECUTABLE_VALUES
from pre_commit_hooks.check_executables_have_shebangs import git_ls_files
from pre_commit_hooks.check_executables_have_shebangs import has_shebang


def check_shebangs(paths: list[str]) -> int:
    # Cannot optimize on non-executability here if we intend this check to
    # work on win32 -- and that's where problems caused by non-executability
    # (elsewhere) are most likely to arise from.
    return _check_git_filemode(paths)


def _check_git_filemode(paths: Sequence[str]) -> int:
    seen: set[str] = set()
    for ls_file in git_ls_files(paths):
        is_executable = any(b in EXECUTABLE_VALUES for b in ls_file.mode[-3:])
        if not is_executable and has_shebang(ls_file.filename):
            _message(ls_file.filename)
            seen.add(ls_file.filename)

    return int(bool(seen))


def _message(path: str) -> None:
    print(
        f'{path}: has a shebang but is not marked executable!\n'
        f'  If it is supposed to be executable, try: '
        f'`chmod +x {shlex.quote(path)}`\n'
        f'  If on Windows, you may also need to: '
        f'`git add --chmod=+x {shlex.quote(path)}`\n'
        f'  If it is not supposed to be executable, double-check its shebang '
        f'is wanted.\n',
        file=sys.stderr,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    return check_shebangs(args.filenames)


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_symlinks.py`
```python
from __future__ import annotations

import argparse
import os.path
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Checks for broken symlinks.')
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        if (
                os.path.islink(filename) and
                not os.path.exists(filename)
        ):  # pragma: no cover (symlink support required)
            print(f'{filename}: Broken symlink')
            retv = 1

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_toml.py`
```python
from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

if sys.version_info >= (3, 11):  # pragma: >=3.11 cover
    import tomllib
else:  # pragma: <3.11 cover
    import tomli as tomllib


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            with open(filename, mode='rb') as fp:
                tomllib.load(fp)
        except tomllib.TOMLDecodeError as exc:
            print(f'{filename}: {exc}')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_vcs_permalinks.py`
```python
from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from re import Pattern


def _get_pattern(domain: str) -> Pattern[bytes]:
    regex = (
        rf'https://{domain}/[^/ ]+/[^/ ]+/blob/'
        r'(?![a-fA-F0-9]{4,64}/)([^/. ]+)/[^# ]+#L\d+'
    )
    return re.compile(regex.encode())


def _check_filename(filename: str, patterns: list[Pattern[bytes]]) -> int:
    retv = 0
    with open(filename, 'rb') as f:
        for i, line in enumerate(f, 1):
            for pattern in patterns:
                if pattern.search(line):
                    sys.stdout.write(f'{filename}:{i}:')
                    sys.stdout.flush()
                    sys.stdout.buffer.write(line)
                    retv = 1
    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument(
        '--additional-github-domain',
        dest='additional_github_domains',
        action='append',
        default=['github.com'],
    )
    args = parser.parse_args(argv)

    patterns = [
        _get_pattern(domain)
        for domain in args.additional_github_domains
    ]

    retv = 0

    for filename in args.filenames:
        retv |= _check_filename(filename, patterns)

    if retv:
        print()
        print('Non-permanent github link detected.')
        print('On any page on github press [y] to load a permalink.')
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_xml.py`
```python
from __future__ import annotations

import argparse
import xml.sax.handler
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='XML filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    handler = xml.sax.handler.ContentHandler()
    for filename in args.filenames:
        try:
            with open(filename, 'rb') as xml_file:
                xml.sax.parse(xml_file, handler)
        except xml.sax.SAXException as exc:
            print(f'{filename}: Failed to xml parse ({exc})')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/check_yaml.py`
```python
from __future__ import annotations

import argparse
from collections.abc import Generator
from collections.abc import Sequence
from typing import Any
from typing import NamedTuple

import ruamel.yaml

yaml = ruamel.yaml.YAML(typ='safe')


def _exhaust(gen: Generator[str]) -> None:
    for _ in gen:
        pass


def _parse_unsafe(*args: Any, **kwargs: Any) -> None:
    _exhaust(yaml.parse(*args, **kwargs))


def _load_all(*args: Any, **kwargs: Any) -> None:
    _exhaust(yaml.load_all(*args, **kwargs))


class Key(NamedTuple):
    multi: bool
    unsafe: bool


LOAD_FNS = {
    Key(multi=False, unsafe=False): yaml.load,
    Key(multi=False, unsafe=True): _parse_unsafe,
    Key(multi=True, unsafe=False): _load_all,
    Key(multi=True, unsafe=True): _parse_unsafe,
}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--multi', '--allow-multiple-documents', action='store_true',
    )
    parser.add_argument(
        '--unsafe', action='store_true',
        help=(
            'Instead of loading the files, simply parse them for syntax.  '
            'A syntax-only check enables extensions and unsafe constructs '
            'which would otherwise be forbidden.  Using this option removes '
            'all guarantees of portability to other yaml implementations.  '
            'Implies --allow-multiple-documents'
        ),
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    load_fn = LOAD_FNS[Key(multi=args.multi, unsafe=args.unsafe)]

    retval = 0
    for filename in args.filenames:
        try:
            with open(filename, encoding='UTF-8') as f:
                load_fn(f)
        except ruamel.yaml.YAMLError as exc:
            print(exc)
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/debug_statement_hook.py`
```python
from __future__ import annotations

import argparse
import ast
import traceback
from collections.abc import Sequence
from typing import NamedTuple


DEBUG_STATEMENTS = {
    'bpdb',
    'ipdb',
    'pdb',
    'pdbr',
    'pudb',
    'pydevd_pycharm',
    'q',
    'rdb',
    'rpdb',
    'wdb',
}


class Debug(NamedTuple):
    line: int
    col: int
    name: str
    reason: str


class DebugStatementParser(ast.NodeVisitor):
    def __init__(self) -> None:
        self.breakpoints: list[Debug] = []

    def visit_Import(self, node: ast.Import) -> None:
        for name in node.names:
            if name.name in DEBUG_STATEMENTS:
                st = Debug(node.lineno, node.col_offset, name.name, 'imported')
                self.breakpoints.append(st)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module in DEBUG_STATEMENTS:
            st = Debug(node.lineno, node.col_offset, node.module, 'imported')
            self.breakpoints.append(st)

    def visit_Call(self, node: ast.Call) -> None:
        """python3.7+ breakpoint()"""
        if isinstance(node.func, ast.Name) and node.func.id == 'breakpoint':
            st = Debug(node.lineno, node.col_offset, node.func.id, 'called')
            self.breakpoints.append(st)
        self.generic_visit(node)


def check_file(filename: str) -> int:
    try:
        with open(filename, 'rb') as f:
            ast_obj = ast.parse(f.read(), filename=filename)
    except SyntaxError:
        print(f'{filename} - Could not parse ast')
        print()
        print('\t' + traceback.format_exc().replace('\n', '\n\t'))
        print()
        return 1

    visitor = DebugStatementParser()
    visitor.visit(ast_obj)

    for bp in visitor.breakpoints:
        print(f'{filename}:{bp.line}:{bp.col}: {bp.name} {bp.reason}')

    return int(bool(visitor.breakpoints))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= check_file(filename)
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/destroyed_symlinks.py`
```python
from __future__ import annotations

import argparse
import shlex
import subprocess
from collections.abc import Sequence

from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit

ORDINARY_CHANGED_ENTRIES_MARKER = '1'
PERMS_LINK = '120000'
PERMS_NONEXIST = '000000'


def find_destroyed_symlinks(files: Sequence[str]) -> list[str]:
    destroyed_links: list[str] = []
    if not files:
        return destroyed_links
    for line in zsplit(
        cmd_output('git', 'status', '--porcelain=v2', '-z', '--', *files),
    ):
        splitted = line.split(' ')
        if splitted and splitted[0] == ORDINARY_CHANGED_ENTRIES_MARKER:
            # https://git-scm.com/docs/git-status#_changed_tracked_entries
            (
                _, _, _,
                mode_HEAD,
                mode_index,
                _,
                hash_HEAD,
                hash_index,
                *path_splitted,
            ) = splitted
            path = ' '.join(path_splitted)
            if (
                    mode_HEAD == PERMS_LINK and
                    mode_index != PERMS_LINK and
                    mode_index != PERMS_NONEXIST
            ):
                if hash_HEAD == hash_index:
                    # if old and new hashes are equal, it's not needed to check
                    # anything more, we've found a destroyed symlink for sure
                    destroyed_links.append(path)
                else:
                    # if old and new hashes are *not* equal, it doesn't mean
                    # that everything is OK - new file may be altered
                    # by something like trailing-whitespace and/or
                    # mixed-line-ending hooks so we need to go deeper
                    SIZE_CMD = ('git', 'cat-file', '-s')
                    size_index = int(cmd_output(*SIZE_CMD, hash_index).strip())
                    size_HEAD = int(cmd_output(*SIZE_CMD, hash_HEAD).strip())

                    # in the worst case new file may have CRLF added
                    # so check content only if new file is bigger
                    # not more than 2 bytes compared to the old one
                    if size_index <= size_HEAD + 2:
                        head_content = subprocess.check_output(
                            ('git', 'cat-file', '-p', hash_HEAD),
                        ).rstrip()
                        index_content = subprocess.check_output(
                            ('git', 'cat-file', '-p', hash_index),
                        ).rstrip()
                        if head_content == index_content:
                            destroyed_links.append(path)
    return destroyed_links


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    destroyed_links = find_destroyed_symlinks(files=args.filenames)
    if destroyed_links:
        print('Destroyed symlinks:')
        for destroyed_link in destroyed_links:
            print(f'- {destroyed_link}')
        print('You should unstage affected files:')
        print(f'\tgit reset HEAD -- {shlex.join(destroyed_links)}')
        print(
            'And retry commit. As a long term solution '
            'you may try to explicitly tell git that your '
            'environment does not support symlinks:',
        )
        print('\tgit config core.symlinks false')
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/detect_aws_credentials.py`
```python
from __future__ import annotations

import argparse
import configparser
import os
from collections.abc import Sequence
from typing import NamedTuple


class BadFile(NamedTuple):
    filename: str
    key: str


def get_aws_cred_files_from_env() -> set[str]:
    """Extract credential file paths from environment variables."""
    return {
        os.environ[env_var]
        for env_var in (
            'AWS_CONFIG_FILE', 'AWS_CREDENTIAL_FILE',
            'AWS_SHARED_CREDENTIALS_FILE', 'BOTO_CONFIG',
        )
        if env_var in os.environ
    }


def get_aws_secrets_from_env() -> set[str]:
    """Extract AWS secrets from environment variables."""
    keys = set()
    for env_var in (
        'AWS_SECRET_ACCESS_KEY', 'AWS_SECURITY_TOKEN', 'AWS_SESSION_TOKEN',
    ):
        if os.environ.get(env_var):
            keys.add(os.environ[env_var])
    return keys


def get_aws_secrets_from_file(credentials_file: str) -> set[str]:
    """Extract AWS secrets from configuration files.

    Read an ini-style configuration file and return a set with all found AWS
    secret access keys.
    """
    aws_credentials_file_path = os.path.expanduser(credentials_file)
    if not os.path.exists(aws_credentials_file_path):
        return set()

    parser = configparser.ConfigParser()
    try:
        parser.read(aws_credentials_file_path)
    except configparser.MissingSectionHeaderError:
        return set()

    keys = set()
    for section in parser.sections():
        for var in (
            'aws_secret_access_key', 'aws_security_token',
            'aws_session_token',
        ):
            try:
                key = parser.get(section, var).strip()
                if key:
                    keys.add(key)
            except configparser.NoOptionError:
                pass
    return keys


def check_file_for_aws_keys(
        filenames: Sequence[str],
        keys: set[bytes],
) -> list[BadFile]:
    """Check if files contain AWS secrets.

    Return a list of all files containing AWS secrets and keys found, with all
    but the first four characters obfuscated to ease debugging.
    """
    bad_files = []

    for filename in filenames:
        with open(filename, 'rb') as content:
            text_body = content.read()
            for key in keys:
                # naively match the entire file, low chance of incorrect
                # collision
                if key in text_body:
                    key_hidden = key.decode()[:4].ljust(28, '*')
                    bad_files.append(BadFile(filename, key_hidden))
    return bad_files


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+', help='Filenames to run')
    parser.add_argument(
        '--credentials-file',
        dest='credentials_file',
        action='append',
        default=[
            '~/.aws/config', '~/.aws/credentials', '/etc/boto.cfg', '~/.boto',
        ],
        help=(
            'Location of additional AWS credential file from which to get '
            'secret keys. Can be passed multiple times.'
        ),
    )
    parser.add_argument(
        '--allow-missing-credentials',
        dest='allow_missing_credentials',
        action='store_true',
        help='Allow hook to pass when no credentials are detected.',
    )
    args = parser.parse_args(argv)

    credential_files = set(args.credentials_file)

    # Add the credentials files configured via environment variables to the set
    # of files to to gather AWS secrets from.
    credential_files |= get_aws_cred_files_from_env()

    keys: set[str] = set()
    for credential_file in credential_files:
        keys |= get_aws_secrets_from_file(credential_file)

    # Secrets might be part of environment variables, so add such secrets to
    # the set of keys.
    keys |= get_aws_secrets_from_env()

    if not keys and args.allow_missing_credentials:
        return 0

    if not keys:
        print(
            'No AWS keys were found in the configured credential files and '
            'environment variables.\nPlease ensure you have the correct '
            'setting for --credentials-file',
        )
        return 2

    keys_b = {key.encode() for key in keys}
    bad_filenames = check_file_for_aws_keys(args.filenames, keys_b)
    if bad_filenames:
        for bad_file in bad_filenames:
            print(f'AWS secret found in {bad_file.filename}: {bad_file.key}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/detect_private_key.py`
```python
from __future__ import annotations

import argparse
from collections.abc import Sequence

BLACKLIST = [
    b'BEGIN RSA PRIVATE KEY',
    b'BEGIN DSA PRIVATE KEY',
    b'BEGIN EC PRIVATE KEY',
    b'BEGIN OPENSSH PRIVATE KEY',
    b'BEGIN PRIVATE KEY',
    b'PuTTY-User-Key-File-2',
    b'BEGIN SSH2 ENCRYPTED PRIVATE KEY',
    b'BEGIN PGP PRIVATE KEY BLOCK',
    b'BEGIN ENCRYPTED PRIVATE KEY',
    b'BEGIN OpenVPN Static key V1',
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    private_key_files = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            content = f.read()
            if any(line in content for line in BLACKLIST):
                private_key_files.append(filename)

    if private_key_files:
        for private_key_file in private_key_files:
            print(f'Private key found: {private_key_file}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/end_of_file_fixer.py`
```python
from __future__ import annotations

import argparse
import os
from collections.abc import Sequence
from typing import IO


def fix_file(file_obj: IO[bytes]) -> int:
    # Test for newline at end of file
    # Empty files will throw IOError here
    try:
        file_obj.seek(-1, os.SEEK_END)
    except OSError:
        return 0
    last_character = file_obj.read(1)
    # last_character will be '' for an empty file
    if last_character not in {b'\n', b'\r'} and last_character != b'':
        # Needs this seek for windows, otherwise IOError
        file_obj.seek(0, os.SEEK_END)
        file_obj.write(b'\n')
        return 1

    while last_character in {b'\n', b'\r'}:
        # Deal with the beginning of the file
        if file_obj.tell() == 1:
            # If we've reached the beginning of the file and it is all
            # linebreaks then we can make this file empty
            file_obj.seek(0)
            file_obj.truncate()
            return 1

        # Go back two bytes and read a character
        file_obj.seek(-2, os.SEEK_CUR)
        last_character = file_obj.read(1)

    # Our current position is at the end of the file just before any amount of
    # newlines.  If we find extraneous newlines, then backtrack and trim them.
    position = file_obj.tell()
    remaining = file_obj.read()
    for sequence in (b'\n', b'\r\n', b'\r'):
        if remaining == sequence:
            return 0
        elif remaining.startswith(sequence):
            file_obj.seek(position + len(sequence))
            file_obj.truncate()
            return 1

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        # Read as binary so we can read byte-by-byte
        with open(filename, 'rb+') as file_obj:
            ret_for_file = fix_file(file_obj)
            if ret_for_file:
                print(f'Fixing {filename}')
            retv |= ret_for_file

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/file_contents_sorter.py`
```python
"""
A very simple pre-commit hook that, when passed one or more filenames
as arguments, will sort the lines in those files.

An example use case for this: you have a deploy-allowlist.txt file
in a repo that contains a list of filenames that is used to specify
files to be included in a docker container. This file has one filename
per line. Various users are adding/removing lines from this file; using
this hook on that file should reduce the instances of git merge
conflicts and keep the file nicely ordered.
"""
from __future__ import annotations

import argparse
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Sequence
from typing import Any
from typing import IO

PASS = 0
FAIL = 1


def sort_file_contents(
    f: IO[bytes],
    key: Callable[[bytes], Any] | None,
    *,
    unique: bool = False,
) -> int:
    before = list(f)
    lines: Iterable[bytes] = (
        line.rstrip(b'\n\r') for line in before if line.strip()
    )
    if unique:
        lines = set(lines)
    after = sorted(lines, key=key)

    before_string = b''.join(before)
    after_string = b'\n'.join(after)

    if after_string:
        after_string += b'\n'

    if before_string == after_string:
        return PASS
    else:
        f.seek(0)
        f.write(after_string)
        f.truncate()
        return FAIL


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+', help='Files to sort')

    mutex = parser.add_mutually_exclusive_group(required=False)
    mutex.add_argument(
        '--ignore-case',
        action='store_const',
        const=bytes.lower,
        default=None,
        help='fold lower case to upper case characters',
    )
    mutex.add_argument(
        '--unique',
        action='store_true',
        help='ensure each line is unique',
    )

    args = parser.parse_args(argv)

    retv = PASS

    for arg in args.filenames:
        with open(arg, 'rb+') as file_obj:
            ret_for_file = sort_file_contents(
                file_obj, key=args.ignore_case, unique=args.unique,
            )

            if ret_for_file:
                print(f'Sorting {arg}')

            retv |= ret_for_file

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/fix_byte_order_marker.py`
```python
from __future__ import annotations

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        with open(filename, 'rb') as f_b:
            bts = f_b.read(3)

        if bts == b'\xef\xbb\xbf':
            with open(filename, newline='', encoding='utf-8-sig') as f:
                contents = f.read()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                f.write(contents)

            print(f'{filename}: removed byte-order marker')
            retv = 1

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/forbid_new_submodules.py`
```python
from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from pre_commit_hooks.util import cmd_output


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    if (
        'PRE_COMMIT_FROM_REF' in os.environ and
        'PRE_COMMIT_TO_REF' in os.environ
    ):
        diff_arg = '...'.join((
            os.environ['PRE_COMMIT_FROM_REF'],
            os.environ['PRE_COMMIT_TO_REF'],
        ))
    else:
        diff_arg = '--staged'
    added_diff = cmd_output(
        'git', 'diff', '--diff-filter=A', '--raw', diff_arg, '--',
        *args.filenames,
    )
    retv = 0
    for line in added_diff.splitlines():
        metadata, filename = line.split('\t', 1)
        new_mode = metadata.split(' ')[1]
        if new_mode == '160000':
            print(f'{filename}: new submodule introduced')
            retv = 1

    if retv:
        print()
        print('This commit introduces new submodules.')
        print('Did you unintentionally `git add .`?')
        print('To fix: git rm {thesubmodule}  # no trailing slash')
        print('Also check .gitmodules')

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/mixed_line_ending.py`
```python
from __future__ import annotations

import argparse
import collections
from collections.abc import Sequence


CRLF = b'\r\n'
LF = b'\n'
CR = b'\r'
# Prefer LF to CRLF to CR, but detect CRLF before LF
ALL_ENDINGS = (CR, CRLF, LF)
FIX_TO_LINE_ENDING = {'cr': CR, 'crlf': CRLF, 'lf': LF}


def _fix(filename: str, contents: bytes, ending: bytes) -> None:
    new_contents = b''.join(
        line.rstrip(b'\r\n') + ending for line in contents.splitlines(True)
    )
    with open(filename, 'wb') as f:
        f.write(new_contents)


def fix_filename(filename: str, fix: str) -> int:
    with open(filename, 'rb') as f:
        contents = f.read()

    counts: dict[bytes, int] = collections.defaultdict(int)

    for line in contents.splitlines(True):
        for ending in ALL_ENDINGS:
            if line.endswith(ending):
                counts[ending] += 1
                break

    # Some amount of mixed line endings
    mixed = sum(bool(x) for x in counts.values()) > 1

    if fix == 'no' or (fix == 'auto' and not mixed):
        return mixed

    if fix == 'auto':
        max_ending = LF
        max_lines = 0
        # ordering is important here such that lf > crlf > cr
        for ending_type in ALL_ENDINGS:
            # also important, using >= to find a max that prefers the last
            if counts[ending_type] >= max_lines:
                max_ending = ending_type
                max_lines = counts[ending_type]

        _fix(filename, contents, max_ending)
        return 1
    else:
        target_ending = FIX_TO_LINE_ENDING[fix]
        # find if there are lines with *other* endings
        # It's possible there's no line endings of the target type
        counts.pop(target_ending, None)
        other_endings = bool(sum(counts.values()))
        if other_endings:
            _fix(filename, contents, target_ending)
        return other_endings


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--fix',
        choices=('auto', 'no') + tuple(FIX_TO_LINE_ENDING),
        default='auto',
        help='Replace line ending with the specified. Default is "auto"',
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        if fix_filename(filename, args.fix):
            if args.fix == 'no':
                print(f'{filename}: mixed line endings')
            else:
                print(f'{filename}: fixed mixed line endings')
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/no_commit_to_branch.py`
```python
from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import AbstractSet

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


def is_on_branch(
        protected: AbstractSet[str],
        patterns: AbstractSet[str] = frozenset(),
) -> bool:
    try:
        ref_name = cmd_output('git', 'symbolic-ref', 'HEAD')
    except CalledProcessError:
        return False
    chunks = ref_name.strip().split('/')
    branch_name = '/'.join(chunks[2:])
    return branch_name in protected or any(
        re.match(p, branch_name) for p in patterns
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--branch', action='append',
        help='branch to disallow commits to, may be specified multiple times',
    )
    parser.add_argument(
        '-p', '--pattern', action='append',
        help=(
            'regex pattern for branch name to disallow commits to, '
            'may be specified multiple times'
        ),
    )
    args = parser.parse_args(argv)

    protected = frozenset(args.branch or ('master', 'main'))
    patterns = frozenset(args.pattern or ())
    return int(is_on_branch(protected, patterns))


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/pretty_format_json.py`
```python
from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping
from collections.abc import Sequence
from difflib import unified_diff


def _get_pretty_format(
        contents: str,
        indent: str,
        ensure_ascii: bool = True,
        sort_keys: bool = True,
        top_keys: Sequence[str] = (),
) -> str:
    def pairs_first(pairs: Sequence[tuple[str, str]]) -> Mapping[str, str]:
        before = [pair for pair in pairs if pair[0] in top_keys]
        before = sorted(before, key=lambda x: top_keys.index(x[0]))
        after = [pair for pair in pairs if pair[0] not in top_keys]
        if sort_keys:
            after.sort()
        return dict(before + after)
    json_pretty = json.dumps(
        json.loads(contents, object_pairs_hook=pairs_first),
        indent=indent,
        ensure_ascii=ensure_ascii,
    )
    return f'{json_pretty}\n'


def _autofix(filename: str, new_contents: str) -> None:
    print(f'Fixing file {filename}')
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(new_contents)


def parse_num_to_int(s: str) -> int | str:
    """Convert string numbers to int, leaving strings as is."""
    try:
        return int(s)
    except ValueError:
        return s


def parse_topkeys(s: str) -> list[str]:
    return s.split(',')


def get_diff(source: str, target: str, file: str) -> str:
    source_lines = source.splitlines(True)
    target_lines = target.splitlines(True)
    diff = unified_diff(source_lines, target_lines, fromfile=file, tofile=file)
    return ''.join(diff)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--autofix',
        action='store_true',
        dest='autofix',
        help='Automatically fixes encountered not-pretty-formatted files',
    )
    parser.add_argument(
        '--indent',
        type=parse_num_to_int,
        default='2',
        help=(
            'The number of indent spaces or a string to be used as delimiter'
            ' for indentation level e.g. 4 or "\t" (Default: 2)'
        ),
    )
    parser.add_argument(
        '--no-ensure-ascii',
        action='store_true',
        dest='no_ensure_ascii',
        default=False,
        help=(
            'Do NOT convert non-ASCII characters to Unicode escape sequences '
            '(\\uXXXX)'
        ),
    )
    parser.add_argument(
        '--no-sort-keys',
        action='store_true',
        dest='no_sort_keys',
        default=False,
        help='Keep JSON nodes in the same order',
    )
    parser.add_argument(
        '--top-keys',
        type=parse_topkeys,
        dest='top_keys',
        default=[],
        help='Ordered list of keys to keep at the top of JSON hashes',
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    status = 0

    for json_file in args.filenames:
        with open(json_file, encoding='UTF-8') as f:
            contents = f.read()

        try:
            pretty_contents = _get_pretty_format(
                contents, args.indent, ensure_ascii=not args.no_ensure_ascii,
                sort_keys=not args.no_sort_keys, top_keys=args.top_keys,
            )
        except ValueError:
            print(
                f'Input File {json_file} is not a valid JSON, consider using '
                f'check-json',
            )
            status = 1
        else:
            if contents != pretty_contents:
                if args.autofix:
                    _autofix(json_file, pretty_contents)
                else:
                    diff_output = get_diff(
                        contents,
                        pretty_contents,
                        json_file,
                    )
                    sys.stdout.buffer.write(diff_output.encode())

                status = 1

    return status


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/removed.py`
```python
from __future__ import annotations

import sys
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    hookid, new_hookid, url = argv[:3]
    raise SystemExit(
        f'`{hookid}` has been removed -- use `{new_hookid}` from {url}',
    )


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/requirements_txt_fixer.py`
```python
from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import IO


PASS = 0
FAIL = 1


class Requirement:
    UNTIL_COMPARISON = re.compile(b'={2,3}|!=|~=|>=?|<=?')
    UNTIL_SEP = re.compile(rb'[^;\s]+')

    def __init__(self) -> None:
        self.value: bytes | None = None
        self.comments: list[bytes] = []

    @property
    def name(self) -> bytes:
        assert self.value is not None, self.value
        name = self.value.lower()
        for egg in (b'#egg=', b'&egg='):
            if egg in self.value:
                return name.partition(egg)[-1]

        m = self.UNTIL_SEP.match(name)
        assert m is not None

        name = m.group()
        m = self.UNTIL_COMPARISON.search(name)
        if not m:
            return name

        return name[:m.start()]

    def __lt__(self, requirement: Requirement) -> bool:
        # \n means top of file comment, so always return True,
        # otherwise just do a string comparison with value.
        assert self.value is not None, self.value
        if self.value == b'\n':
            return True
        elif requirement.value == b'\n':
            return False
        else:
            # if 2 requirements have the same name, the one with comments
            # needs to go first (so that when removing duplicates, the one
            # with comments is kept)
            if self.name == requirement.name:
                return bool(self.comments) > bool(requirement.comments)
            return self.name < requirement.name

    def is_complete(self) -> bool:
        return (
            self.value is not None and
            not self.value.rstrip(b'\r\n').endswith(b'\\')
        )

    def append_value(self, value: bytes) -> None:
        if self.value is not None:
            self.value += value
        else:
            self.value = value


def fix_requirements(f: IO[bytes]) -> int:
    requirements: list[Requirement] = []
    before = list(f)
    after: list[bytes] = []

    before_string = b''.join(before)

    # adds new line in case one is missing
    # AND a change to the requirements file is needed regardless:
    if before and not before[-1].endswith(b'\n'):
        before[-1] += b'\n'

    # If the file is empty (i.e. only whitespace/newlines) exit early
    if before_string.strip() == b'':
        return PASS

    for line in before:
        # If the most recent requirement object has a value, then it's
        # time to start building the next requirement object.

        if not len(requirements) or requirements[-1].is_complete():
            requirements.append(Requirement())

        requirement = requirements[-1]

        # If we see a newline before any requirements, then this is a
        # top of file comment.
        if len(requirements) == 1 and line.strip() == b'':
            if (
                    len(requirement.comments) and
                    requirement.comments[0].startswith(b'#')
            ):
                requirement.value = b'\n'
            else:
                requirement.comments.append(line)
        elif line.lstrip().startswith(b'#') or line.strip() == b'':
            requirement.comments.append(line)
        else:
            requirement.append_value(line)

    # if a file ends in a comment, preserve it at the end
    if requirements[-1].value is None:
        rest = requirements.pop().comments
    else:
        rest = []

    # find and remove pkg-resources==0.0.0
    # which is automatically added by broken pip package under Debian
    requirements = [
        req for req in requirements
        if req.value not in [
            b'pkg-resources==0.0.0\n',
            b'pkg_resources==0.0.0\n',
        ]
    ]

    # sort the requirements and remove duplicates
    prev = None
    for requirement in sorted(requirements):
        after.extend(requirement.comments)
        assert requirement.value, requirement.value
        if prev is None or requirement.value != prev.value:
            after.append(requirement.value)
            prev = requirement
    after.extend(rest)

    after_string = b''.join(after)

    if before_string == after_string:
        return PASS
    else:
        f.seek(0)
        f.write(after_string)
        f.truncate()
        return FAIL


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = PASS

    for arg in args.filenames:
        with open(arg, 'rb+') as file_obj:
            ret_for_file = fix_requirements(file_obj)

            if ret_for_file:
                print(f'Sorting {arg}')

            retv |= ret_for_file

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/sort_simple_yaml.py`
```python
"""Sort a simple YAML file, keeping blocks of comments and definitions
together.

We assume a strict subset of YAML that looks like:

    # block of header comments
    # here that should always
    # be at the top of the file

    # optional comments
    # can go here
    key: value
    key: value

    key: value

In other words, we don't sort deeper than the top layer, and might corrupt
complicated YAML files.
"""
from __future__ import annotations

import argparse
from collections.abc import Sequence


QUOTES = ["'", '"']


def sort(lines: list[str]) -> list[str]:
    """Sort a YAML file in alphabetical order, keeping blocks together.

    :param lines: array of strings (without newlines)
    :return: sorted array of strings
    """
    # make a copy of lines since we will clobber it
    lines = list(lines)
    new_lines = parse_block(lines, header=True)

    for block in sorted(parse_blocks(lines), key=first_key):
        if new_lines:
            new_lines.append('')
        new_lines.extend(block)

    return new_lines


def parse_block(lines: list[str], header: bool = False) -> list[str]:
    """Parse and return a single block, popping off the start of `lines`.

    If parsing a header block, we stop after we reach a line that is not a
    comment. Otherwise, we stop after reaching an empty line.

    :param lines: list of lines
    :param header: whether we are parsing a header block
    :return: list of lines that form the single block
    """
    block_lines = []
    while lines and lines[0] and (not header or lines[0].startswith('#')):
        block_lines.append(lines.pop(0))
    return block_lines


def parse_blocks(lines: list[str]) -> list[list[str]]:
    """Parse and return all possible blocks, popping off the start of `lines`.

    :param lines: list of lines
    :return: list of blocks, where each block is a list of lines
    """
    blocks = []

    while lines:
        if lines[0] == '':
            lines.pop(0)
        else:
            blocks.append(parse_block(lines))

    return blocks


def first_key(lines: list[str]) -> str:
    """Returns a string representing the sort key of a block.

    The sort key is the first YAML key we encounter, ignoring comments, and
    stripping leading quotes.

    >>> print(test)
    # some comment
    'foo': true
    >>> first_key(test)
    'foo'
    """
    for line in lines:
        if line.startswith('#'):
            continue
        if any(line.startswith(quote) for quote in QUOTES):
            return line[1:]
        return line
    else:
        return ''  # not actually reached in reality


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retval = 0

    for filename in args.filenames:
        with open(filename, 'r+') as f:
            lines = [line.rstrip() for line in f.readlines()]
            new_lines = sort(lines)

            if lines != new_lines:
                print(f'Fixing file `{filename}`')
                f.seek(0)
                f.write('\n'.join(new_lines) + '\n')
                f.truncate()
                retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/string_fixer.py`
```python
from __future__ import annotations

import argparse
import io
import re
import sys
import tokenize
from collections.abc import Sequence

if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
    FSTRING_START = tokenize.FSTRING_START
    FSTRING_END = tokenize.FSTRING_END
else:  # pragma: <3.12 cover
    FSTRING_START = FSTRING_END = -1

START_QUOTE_RE = re.compile('^[a-zA-Z]*"')


def handle_match(token_text: str) -> str:
    if '"""' in token_text or "'''" in token_text:
        return token_text

    match = START_QUOTE_RE.match(token_text)
    if match is not None:
        meat = token_text[match.end():-1]
        if '"' in meat or "'" in meat:
            return token_text
        else:
            return match.group().replace('"', "'") + meat + "'"
    else:
        return token_text


def get_line_offsets_by_line_no(src: str) -> list[int]:
    # Padded so we can index with line number
    offsets = [-1, 0]
    for line in src.splitlines(True):
        offsets.append(offsets[-1] + len(line))
    return offsets


def fix_strings(filename: str) -> int:
    with open(filename, encoding='UTF-8', newline='') as f:
        contents = f.read()
    line_offsets = get_line_offsets_by_line_no(contents)

    # Basically a mutable string
    splitcontents = list(contents)

    fstring_depth = 0

    # Iterate in reverse so the offsets are always correct
    tokens_l = list(tokenize.generate_tokens(io.StringIO(contents).readline))
    tokens = reversed(tokens_l)
    for token_type, token_text, (srow, scol), (erow, ecol), _ in tokens:
        if token_type == FSTRING_START:  # pragma: >=3.12 cover
            fstring_depth += 1
        elif token_type == FSTRING_END:  # pragma: >=3.12 cover
            fstring_depth -= 1
        elif fstring_depth == 0 and token_type == tokenize.STRING:
            new_text = handle_match(token_text)
            splitcontents[
                line_offsets[srow] + scol:
                line_offsets[erow] + ecol
            ] = new_text

    new_contents = ''.join(splitcontents)
    if contents != new_contents:
        with open(filename, 'w', encoding='UTF-8', newline='') as f:
            f.write(new_contents)
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        return_value = fix_strings(filename)
        if return_value != 0:
            print(f'Fixing strings in {filename}')
        retv |= return_value

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/tests_should_end_in_test.py`
```python
from __future__ import annotations

import argparse
import os.path
import re
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    mutex = parser.add_mutually_exclusive_group()
    mutex.add_argument(
        '--pytest',
        dest='pattern',
        action='store_const',
        const=r'.*_test\.py',
        default=r'.*_test\.py',
        help='(the default) ensure tests match %(const)s',
    )
    mutex.add_argument(
        '--pytest-test-first',
        dest='pattern',
        action='store_const',
        const=r'test_.*\.py',
        help='ensure tests match %(const)s',
    )
    mutex.add_argument(
        '--django', '--unittest',
        dest='pattern',
        action='store_const',
        const=r'test.*\.py',
        help='ensure tests match %(const)s',
    )
    args = parser.parse_args(argv)

    retcode = 0
    reg = re.compile(args.pattern)
    for filename in args.filenames:
        base = os.path.basename(filename)
        if (
                not reg.fullmatch(base) and
                not base == '__init__.py' and
                not base == 'conftest.py'
        ):
            retcode = 1
            print(f'{filename} does not match pattern "{args.pattern}"')

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/trailing_whitespace_fixer.py`
```python
from __future__ import annotations

import argparse
import os
from collections.abc import Sequence


def _fix_file(
        filename: str,
        is_markdown: bool,
        chars: bytes | None,
) -> bool:
    with open(filename, mode='rb') as file_processed:
        lines = file_processed.readlines()
    newlines = [_process_line(line, is_markdown, chars) for line in lines]
    if newlines != lines:
        with open(filename, mode='wb') as file_processed:
            for line in newlines:
                file_processed.write(line)
        return True
    else:
        return False


def _process_line(
        line: bytes,
        is_markdown: bool,
        chars: bytes | None,
) -> bytes:
    if line[-2:] == b'\r\n':
        eol = b'\r\n'
        line = line[:-2]
    elif line[-1:] == b'\n':
        eol = b'\n'
        line = line[:-1]
    else:
        eol = b''
    # preserve trailing two-space for non-blank lines in markdown files
    if is_markdown and (not line.isspace()) and line.endswith(b'  '):
        return line[:-2].rstrip(chars) + b'  ' + eol
    return line.rstrip(chars) + eol


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--no-markdown-linebreak-ext',
        action='store_true',
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        '--markdown-linebreak-ext',
        action='append',
        default=[],
        metavar='*|EXT[,EXT,...]',
        help=(
            'Markdown extensions (or *) to not strip linebreak spaces.  '
            'default: %(default)s'
        ),
    )
    parser.add_argument(
        '--chars',
        help=(
            'The set of characters to strip from the end of lines.  '
            'Defaults to all whitespace characters.'
        ),
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    if args.no_markdown_linebreak_ext:
        print('--no-markdown-linebreak-ext now does nothing!')

    md_args = args.markdown_linebreak_ext
    if '' in md_args:
        parser.error('--markdown-linebreak-ext requires a non-empty argument')
    all_markdown = '*' in md_args
    # normalize extensions; split at ',', lowercase, and force 1 leading '.'
    md_exts = [
        '.' + x.lower().lstrip('.') for x in ','.join(md_args).split(',')
    ]

    # reject probable "eaten" filename as extension: skip leading '.' with [1:]
    for ext in md_exts:
        if any(c in ext[1:] for c in r'./\:'):
            parser.error(
                f'bad --markdown-linebreak-ext extension '
                f'{ext!r} (has . / \\ :)\n'
                f"  (probably filename; use '--markdown-linebreak-ext=EXT')",
            )
    chars = None if args.chars is None else args.chars.encode()
    return_code = 0
    for filename in args.filenames:
        _, extension = os.path.splitext(filename.lower())
        md = all_markdown or extension in md_exts
        if _fix_file(filename, md, chars):
            print(f'Fixing {filename}')
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
```

## File: `pre_commit_hooks/util.py`
```python
from __future__ import annotations

import subprocess
from typing import Any


class CalledProcessError(RuntimeError):
    pass


def added_files() -> set[str]:
    cmd = ('git', 'diff', '--staged', '--name-only', '--diff-filter=A')
    return set(cmd_output(*cmd).splitlines())


def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def zsplit(s: str) -> list[str]:
    s = s.strip('\0')
    if s:
        return s.split('\0')
    else:
        return []
```

## File: `testing/util.py`
```python
from __future__ import annotations

import os.path
import subprocess


TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


def get_resource_path(path):
    return os.path.join(TESTING_DIR, 'resources', path)


def git_commit(*args, **kwargs):
    cmd = ('git', 'commit', '--no-gpg-sign', '--no-verify', '--no-edit', *args)
    subprocess.check_call(cmd, **kwargs)
```

## File: `testing/resources/aws_config_with_multiple_sections.ini`
```
# file with AWS access key ids, AWS secret access keys and AWS session tokens in multiple sections
[default]
aws_access_key_id = AKIASLARTIBARTFAST11
aws_secret_access_key = 7xebzorgm5143ouge9gvepxb2z70bsb2rtrh099e
[production]
aws_access_key_id = AKIAVOGONSVOGONS0042
aws_secret_access_key = z2rpgs5uit782eapz5l1z0y2lurtsyyk6hcfozlb
[staging]
aws_access_key_id = AKIAJIMMINYCRICKET0A
aws_secret_access_key = ixswosj8gz3wuik405jl9k3vdajsnxfhnpui38ez
[test]
aws_session_token = foo
```

## File: `testing/resources/aws_config_with_secret.ini`
```
# file with an AWS access key id and an AWS secret access key
[production]
aws_access_key_id = AKIAVOGONSVOGONS0042
aws_secret_access_key = z2rpgs5uit782eapz5l1z0y2lurtsyyk6hcfozlb
```

## File: `testing/resources/aws_config_with_secret_and_session_token.ini`
```
# file with an AWS access key id, an AWS secret access key and an AWS session token
[production]
aws_access_key_id = AKIAVOGONSVOGONS0042
aws_secret_access_key = z2rpgs5uit782eapz5l1z0y2lurtsyyk6hcfozlb
aws_session_token = foo
```

## File: `testing/resources/aws_config_with_session_token.ini`
```
# file with an AWS session token
[production]
aws_session_token = foo
```

## File: `testing/resources/aws_config_without_secrets.ini`
```
# file with an AWS access key id but no AWS secret access key
[production]
aws_access_key_id = AKIASLARTIBARTFAST11
```

## File: `testing/resources/aws_config_without_secrets_with_spaces.ini`
```
# file with an AWS access key id but no valid AWS secret access key only space characters
[production]
aws_access_key_id = AKIASLARTARGENTINA86
aws_secret_access_key =
```

## File: `testing/resources/bad_json.notjson`
```
{
    "hello": "world",
}
```

## File: `testing/resources/bad_xml.notxml`
```
<im><not><terminated><lol>
```

## File: `testing/resources/bad_yaml.notyaml`
```
# It's surprisingly hard to make invalid yaml
a: "
```

## File: `testing/resources/cannot_parse_ast.notpy`
```
if True:
```

## File: `testing/resources/duplicate_key_json.notjson`
```
{
    "hello": "world",
    "hello": "planet"
}
```

## File: `testing/resources/non_ascii_pretty_formatted_json.json`
```json
{
  "alist": [
    2,
    34,
    234
  ],
  "blah": null,
  "foo": "bar",
  "non_ascii": "中文にほんご한국어"
}
```

## File: `testing/resources/nonsense.txt`
```
some nonsense text generated at https://baconipsum.com/
Bacon ipsum dolor amet ipsum fugiat pastrami pork belly, non ball tip flank est short loin. Fatback landjaeger meatloaf flank. Sunt boudin duis occaecat mollit velit. Capicola lorem frankfurter doner strip steak jerky rump elit laborum mollit. Venison cupidatat laboris duis ut chuck proident mollit. Minim do rump, eu jerky ham turkey chuck in tempor venison pariatur voluptate landjaeger beef.

Duis aliqua esse, exercitation in ball tip ut capicola sausage dolore frankfurter occaecat. Duis in nulla consequat salami. Est shoulder tempor commodo shankle short ribs. In meatball aliqua boudin tenderloin, meatloaf leberkas hamburger quis pig dolore ea eu. Ham hock ex laboris, filet mignon sunt doner cillum short loin prosciutto voluptate.

Occaecat pork doner meatloaf nulla biltong ullamco tenderloin culpa brisket. Culpa jowl ea shank t-bone shankle voluptate nostrud incididunt leberkas pork loin. Bacon kevin jerky pork belly t-bone labore duis. Boudin corned beef adipisicing aute, fatback ribeye nulla pancetta anim venison. Short ribs kevin pastrami cow drumstick velit. Turkey exercitation jowl, fatback labore swine do voluptate.
```

## File: `testing/resources/not_pretty_formatted_json.json`
```json
{
    "foo":
    "bar",
        "alist": [2, 34, 234],
  "blah": null
}
```

## File: `testing/resources/ok_json.json`
```json
{
    "hello": "world"
}
```

## File: `testing/resources/ok_xml.xml`
```xml
<document>
    <hello>Hi</hello>
    <world>Earth</world>
</document>
```

## File: `testing/resources/ok_yaml.yaml`
```yaml
im: ok yaml
```

## File: `testing/resources/pretty_formatted_json.json`
```json
{
  "alist": [
    2,
    34,
    234
  ],
  "blah": null,
  "foo": "bar"
}
```

## File: `testing/resources/tab_pretty_formatted_json.json`
```json
{
	"alist": [
		2,
		34,
		234
	],
	"blah": null,
	"foo": "bar"
}
```

## File: `testing/resources/top_sorted_json.json`
```json
{
  "01-alist": [
    2,
    34,
    234
  ],
  "alist": [
    2,
    34,
    234
  ],
  "00-foo": "bar",
  "02-blah": null,
  "blah": null,
  "foo": "bar"
}
```

## File: `testing/resources/unsorted_pretty_formatted_json.json`
```json
{
  "foo": "bar",
  "alist": [
    34,
    2,
    234
  ],
  "blah": null
}
```

## File: `tests/check_added_large_files_test.py`
```python
from __future__ import annotations

import shutil

import pytest

from pre_commit_hooks.check_added_large_files import find_large_added_files
from pre_commit_hooks.check_added_large_files import main
from pre_commit_hooks.util import cmd_output
from testing.util import git_commit


def test_nothing_added(temp_git_dir):
    with temp_git_dir.as_cwd():
        assert find_large_added_files(['f.py'], 0) == 0


def test_adding_something(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')

        # Should fail with max size of 0
        assert find_large_added_files(['f.py'], 0) == 1


def test_add_something_giant(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write('a' * 10000)

        # Should not fail when not added
        assert find_large_added_files(['f.py'], 0) == 0

        cmd_output('git', 'add', 'f.py')

        # Should fail with strict bound
        assert find_large_added_files(['f.py'], 0) == 1

        # Should also fail with actual bound
        assert find_large_added_files(['f.py'], 9) == 1

        # Should pass with higher bound
        assert find_large_added_files(['f.py'], 10) == 0


def test_enforce_all(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write('a' * 10000)

        # Should fail, when not staged with enforce_all
        assert find_large_added_files(['f.py'], 0, enforce_all=True) == 1

        # Should pass, when not staged without enforce_all
        assert find_large_added_files(['f.py'], 0, enforce_all=False) == 0


def test_added_file_not_in_pre_commits_list(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')

        # Should pass even with a size of 0
        assert find_large_added_files(['g.py'], 0) == 0


def test_integration(temp_git_dir):
    with temp_git_dir.as_cwd():
        assert main(argv=[]) == 0

        temp_git_dir.join('f.py').write('a' * 10000)
        cmd_output('git', 'add', 'f.py')

        # Should not fail with default
        assert main(argv=['f.py']) == 0

        # Should fail with --maxkb
        assert main(argv=['--maxkb', '9', 'f.py']) == 1


def has_gitlfs():
    return shutil.which('git-lfs') is not None


xfailif_no_gitlfs = pytest.mark.xfail(
    not has_gitlfs(), reason='This test requires git-lfs',
)


@xfailif_no_gitlfs
def test_allows_gitlfs(temp_git_dir):  # pragma: no cover
    with temp_git_dir.as_cwd():
        cmd_output('git', 'lfs', 'install', '--local')
        temp_git_dir.join('f.py').write('a' * 10000)
        cmd_output('git', 'lfs', 'track', 'f.py')
        cmd_output('git', 'add', '--', '.')
        # Should succeed
        assert main(('--maxkb', '9', 'f.py')) == 0


@xfailif_no_gitlfs
def test_moves_with_gitlfs(temp_git_dir):  # pragma: no cover
    with temp_git_dir.as_cwd():
        cmd_output('git', 'lfs', 'install', '--local')
        cmd_output('git', 'lfs', 'track', 'a.bin', 'b.bin')
        # First add the file we're going to move
        temp_git_dir.join('a.bin').write('a' * 10000)
        cmd_output('git', 'add', '--', '.')
        git_commit('-am', 'foo')
        # Now move it and make sure the hook still succeeds
        cmd_output('git', 'mv', 'a.bin', 'b.bin')
        assert main(('--maxkb', '9', 'b.bin')) == 0


@xfailif_no_gitlfs
def test_enforce_allows_gitlfs(temp_git_dir):  # pragma: no cover
    with temp_git_dir.as_cwd():
        cmd_output('git', 'lfs', 'install', '--local')
        temp_git_dir.join('f.py').write('a' * 10000)
        cmd_output('git', 'lfs', 'track', 'f.py')
        cmd_output('git', 'add', '--', '.')
        # With --enforce-all large files on git lfs should succeed
        assert main(('--enforce-all', '--maxkb', '9', 'f.py')) == 0


@xfailif_no_gitlfs
def test_enforce_allows_gitlfs_after_commit(temp_git_dir):  # pragma: no cover
    with temp_git_dir.as_cwd():
        cmd_output('git', 'lfs', 'install', '--local')
        temp_git_dir.join('f.py').write('a' * 10000)
        cmd_output('git', 'lfs', 'track', 'f.py')
        cmd_output('git', 'add', '--', '.')
        git_commit('-am', 'foo')
        # With --enforce-all large files on git lfs should succeed
        assert main(('--enforce-all', '--maxkb', '9', 'f.py')) == 0
```

## File: `tests/check_ast_test.py`
```python
from __future__ import annotations

from pre_commit_hooks.check_ast import main
from testing.util import get_resource_path


def test_failing_file():
    ret = main([get_resource_path('cannot_parse_ast.notpy')])
    assert ret == 1


def test_passing_file():
    ret = main([__file__])
    assert ret == 0
```

## File: `tests/check_builtin_literals_test.py`
```python
from __future__ import annotations

import ast

import pytest

from pre_commit_hooks.check_builtin_literals import Call
from pre_commit_hooks.check_builtin_literals import main
from pre_commit_hooks.check_builtin_literals import Visitor

BUILTIN_CONSTRUCTORS = '''\
import builtins

c1 = complex()
d1 = dict()
f1 = float()
i1 = int()
l1 = list()
s1 = str()
t1 = tuple()

c2 = builtins.complex()
d2 = builtins.dict()
f2 = builtins.float()
i2 = builtins.int()
l2 = builtins.list()
s2 = builtins.str()
t2 = builtins.tuple()
'''
BUILTIN_LITERALS = '''\
c1 = 0j
d1 = {}
f1 = 0.0
i1 = 0
l1 = []
s1 = ''
t1 = ()
'''


@pytest.mark.parametrize(
    ('expression', 'calls'),
    [
        # see #285
        ('x[0]()', []),
        # complex
        ('0j', []),
        ('complex()', [Call('complex', 1, 0)]),
        ('complex(0, 0)', []),
        ("complex('0+0j')", []),
        ('builtins.complex()', []),
        # float
        ('0.0', []),
        ('float()', [Call('float', 1, 0)]),
        ("float('0.0')", []),
        ('builtins.float()', []),
        # int
        ('0', []),
        ('int()', [Call('int', 1, 0)]),
        ("int('0')", []),
        ('builtins.int()', []),
        # list
        ('[]', []),
        ('list()', [Call('list', 1, 0)]),
        ("list('abc')", []),
        ("list([c for c in 'abc'])", []),
        ("list(c for c in 'abc')", []),
        ('builtins.list()', []),
        # str
        ("''", []),
        ('str()', [Call('str', 1, 0)]),
        ("str('0')", []),
        ('builtins.str()', []),
        # tuple
        ('()', []),
        ('tuple()', [Call('tuple', 1, 0)]),
        ("tuple('abc')", []),
        ("tuple([c for c in 'abc'])", []),
        ("tuple(c for c in 'abc')", []),
        ('builtins.tuple()', []),
    ],
)
def test_non_dict_exprs(expression, calls):
    visitor = Visitor(ignore=set())
    visitor.visit(ast.parse(expression))
    assert visitor.builtin_type_calls == calls


@pytest.mark.parametrize(
    ('expression', 'calls'),
    [
        ('{}', []),
        ('dict()', [Call('dict', 1, 0)]),
        ('dict(a=1, b=2, c=3)', []),
        ("dict(**{'a': 1, 'b': 2, 'c': 3})", []),
        ("dict([(k, v) for k, v in [('a', 1), ('b', 2), ('c', 3)]])", []),
        ("dict((k, v) for k, v in [('a', 1), ('b', 2), ('c', 3)])", []),
        ('builtins.dict()', []),
    ],
)
def test_dict_allow_kwargs_exprs(expression, calls):
    visitor = Visitor(ignore=set())
    visitor.visit(ast.parse(expression))
    assert visitor.builtin_type_calls == calls


@pytest.mark.parametrize(
    ('expression', 'calls'),
    [
        ('dict()', [Call('dict', 1, 0)]),
        ('dict(a=1, b=2, c=3)', [Call('dict', 1, 0)]),
        ("dict(**{'a': 1, 'b': 2, 'c': 3})", [Call('dict', 1, 0)]),
        ('builtins.dict()', []),
        pytest.param('f(dict())', [Call('dict', 1, 2)], id='nested'),
    ],
)
def test_dict_no_allow_kwargs_exprs(expression, calls):
    visitor = Visitor(ignore=set(), allow_dict_kwargs=False)
    visitor.visit(ast.parse(expression))
    assert visitor.builtin_type_calls == calls


def test_ignore_constructors():
    visitor = Visitor(
        ignore={'complex', 'dict', 'float', 'int', 'list', 'str', 'tuple'},
    )
    visitor.visit(ast.parse(BUILTIN_CONSTRUCTORS))
    assert visitor.builtin_type_calls == []


def test_failing_file(tmpdir):
    f = tmpdir.join('f.py')
    f.write(BUILTIN_CONSTRUCTORS)
    rc = main([str(f)])
    assert rc == 1


def test_passing_file(tmpdir):
    f = tmpdir.join('f.py')
    f.write(BUILTIN_LITERALS)
    rc = main([str(f)])
    assert rc == 0


def test_failing_file_ignore_all(tmpdir):
    f = tmpdir.join('f.py')
    f.write(BUILTIN_CONSTRUCTORS)
    rc = main(['--ignore=complex,dict,float,int,list,str,tuple', str(f)])
    assert rc == 0
```

## File: `tests/check_case_conflict_test.py`
```python
from __future__ import annotations

import sys

import pytest

from pre_commit_hooks.check_case_conflict import find_conflicting_filenames
from pre_commit_hooks.check_case_conflict import main
from pre_commit_hooks.check_case_conflict import parents
from pre_commit_hooks.util import cmd_output
from testing.util import git_commit

skip_win32 = pytest.mark.skipif(
    sys.platform == 'win32',
    reason='case conflicts between directories and files',
)


def test_parents():
    assert set(parents('a')) == set()
    assert set(parents('a/b')) == {'a'}
    assert set(parents('a/b/c')) == {'a/b', 'a'}
    assert set(parents('a/b/c/d')) == {'a/b/c', 'a/b', 'a'}


def test_nothing_added(temp_git_dir):
    with temp_git_dir.as_cwd():
        assert find_conflicting_filenames(['f.py']) == 0


def test_adding_something(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')

        assert find_conflicting_filenames(['f.py']) == 0


def test_adding_something_with_conflict(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')
        temp_git_dir.join('F.py').write("print('hello world')")
        cmd_output('git', 'add', 'F.py')

        assert find_conflicting_filenames(['f.py', 'F.py']) == 1


@skip_win32  # pragma: win32 no cover
def test_adding_files_with_conflicting_directories(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir('dir').join('x').write('foo')
        temp_git_dir.mkdir('DIR').join('y').write('foo')
        cmd_output('git', 'add', '-A')

        assert find_conflicting_filenames([]) == 1


@skip_win32  # pragma: win32 no cover
def test_adding_files_with_conflicting_deep_directories(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir('x').mkdir('y').join('z').write('foo')
        temp_git_dir.join('X').write('foo')
        cmd_output('git', 'add', '-A')

        assert find_conflicting_filenames([]) == 1


@skip_win32  # pragma: win32 no cover
def test_adding_file_with_conflicting_directory(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir('dir').join('x').write('foo')
        temp_git_dir.join('DIR').write('foo')
        cmd_output('git', 'add', '-A')

        assert find_conflicting_filenames([]) == 1


def test_added_file_not_in_pre_commits_list(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')

        assert find_conflicting_filenames(['g.py']) == 0


def test_file_conflicts_with_committed_file(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')
        git_commit('-m', 'Add f.py')

        temp_git_dir.join('F.py').write("print('hello world')")
        cmd_output('git', 'add', 'F.py')

        assert find_conflicting_filenames(['F.py']) == 1


@skip_win32  # pragma: win32 no cover
def test_file_conflicts_with_committed_dir(temp_git_dir):
    with temp_git_dir.as_cwd():
        temp_git_dir.mkdir('dir').join('x').write('foo')
        cmd_output('git', 'add', '-A')
        git_commit('-m', 'Add f.py')

        temp_git_dir.join('DIR').write('foo')
        cmd_output('git', 'add', '-A')

        assert find_conflicting_filenames([]) == 1


def test_integration(temp_git_dir):
    with temp_git_dir.as_cwd():
        assert main(argv=[]) == 0

        temp_git_dir.join('f.py').write("print('hello world')")
        cmd_output('git', 'add', 'f.py')

        assert main(argv=['f.py']) == 0

        temp_git_dir.join('F.py').write("print('hello world')")
        cmd_output('git', 'add', 'F.py')

        assert main(argv=['F.py']) == 1
```

## File: `tests/check_docstring_first_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.check_docstring_first import check_docstring_first
from pre_commit_hooks.check_docstring_first import main


# Contents, expected, expected_output
TESTS = (
    # trivial
    (b'', 0, ''),
    # Acceptable
    (b'"foo"', 0, ''),
    # Docstring after code
    (
        b'from __future__ import unicode_literals\n'
        b'"foo"\n',
        1,
        '{filename}:2: Module docstring appears after code '
        '(code seen on line 1).\n',
    ),
    # Test double docstring
    (
        b'"The real docstring"\n'
        b'from __future__ import absolute_import\n'
        b'"fake docstring"\n',
        1,
        '{filename}:3: Multiple module docstrings '
        '(first docstring on line 1).\n',
    ),
    # Test multiple lines of code above
    (
        b'import os\n'
        b'import sys\n'
        b'"docstring"\n',
        1,
        '{filename}:3: Module docstring appears after code '
        '(code seen on line 1).\n',
    ),
    # String literals in expressions are ok.
    (b'x = "foo"\n', 0, ''),
)


all_tests = pytest.mark.parametrize(
    ('contents', 'expected', 'expected_out'), TESTS,
)


@all_tests
def test_unit(capsys, contents, expected, expected_out):
    assert check_docstring_first(contents) == expected
    assert capsys.readouterr()[0] == expected_out.format(filename='<unknown>')


@all_tests
def test_integration(tmpdir, capsys, contents, expected, expected_out):
    f = tmpdir.join('test.py')
    f.write_binary(contents)
    assert main([str(f)]) == expected
    assert capsys.readouterr()[0] == expected_out.format(filename=str(f))


def test_arbitrary_encoding(tmpdir):
    f = tmpdir.join('f.py')
    contents = '# -*- coding: cp1252\nx = "£"'.encode('cp1252')
    f.write_binary(contents)
    assert main([str(f)]) == 0
```

## File: `tests/check_executables_have_shebangs_test.py`
```python
from __future__ import annotations

import os
import sys

import pytest

from pre_commit_hooks import check_executables_have_shebangs
from pre_commit_hooks.check_executables_have_shebangs import main
from pre_commit_hooks.util import cmd_output

skip_win32 = pytest.mark.skipif(
    sys.platform == 'win32',
    reason="non-git checks aren't relevant on windows",
)


@skip_win32  # pragma: win32 no cover
@pytest.mark.parametrize(
    'content', (
        b'#!/bin/bash\nhello world\n',
        b'#!/usr/bin/env python3.6',
        b'#!python',
        '#!☃'.encode(),
    ),
)
def test_has_shebang(content, tmpdir):
    path = tmpdir.join('path')
    path.write(content, 'wb')
    assert main((str(path),)) == 0


@skip_win32  # pragma: win32 no cover
@pytest.mark.parametrize(
    'content', (
        b'',
        b' #!python\n',
        b'\n#!python\n',
        b'python\n',
        '☃'.encode(),
    ),
)
def test_bad_shebang(content, tmpdir, capsys):
    path = tmpdir.join('path')
    path.write(content, 'wb')
    assert main((str(path),)) == 1
    _, stderr = capsys.readouterr()
    assert stderr.startswith(f'{path}: marked executable but')


def test_check_git_filemode_passing(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('git', 'init', '.')

        f = tmpdir.join('f')
        f.write('#!/usr/bin/env bash')
        f_path = str(f)
        cmd_output('chmod', '+x', f_path)
        cmd_output('git', 'add', f_path)
        cmd_output('git', 'update-index', '--chmod=+x', f_path)

        g = tmpdir.join('g').ensure()
        g_path = str(g)
        cmd_output('git', 'add', g_path)

        # this is potentially a problem, but not something the script intends
        # to check for -- we're only making sure that things that are
        # executable have shebangs
        h = tmpdir.join('h')
        h.write('#!/usr/bin/env bash')
        h_path = str(h)
        cmd_output('git', 'add', h_path)

        files = (f_path, g_path, h_path)
        assert check_executables_have_shebangs._check_git_filemode(files) == 0


def test_check_git_filemode_passing_unusual_characters(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('git', 'init', '.')

        f = tmpdir.join('mañana.txt')
        f.write('#!/usr/bin/env bash')
        f_path = str(f)
        cmd_output('chmod', '+x', f_path)
        cmd_output('git', 'add', f_path)
        cmd_output('git', 'update-index', '--chmod=+x', f_path)

        files = (f_path,)
        assert check_executables_have_shebangs._check_git_filemode(files) == 0


def test_check_git_filemode_failing(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('git', 'init', '.')

        f = tmpdir.join('f').ensure()
        f_path = str(f)
        cmd_output('chmod', '+x', f_path)
        cmd_output('git', 'add', f_path)
        cmd_output('git', 'update-index', '--chmod=+x', f_path)

        files = (f_path,)
        assert check_executables_have_shebangs._check_git_filemode(files) == 1


@pytest.mark.parametrize(
    ('content', 'mode', 'expected'),
    (
        pytest.param('#!python', '+x', 0, id='shebang with executable'),
        pytest.param('#!python', '-x', 0, id='shebang without executable'),
        pytest.param('', '+x', 1, id='no shebang with executable'),
        pytest.param('', '-x', 0, id='no shebang without executable'),
    ),
)
def test_git_executable_shebang(temp_git_dir, content, mode, expected):
    with temp_git_dir.as_cwd():
        path = temp_git_dir.join('path')
        path.write(content)
        cmd_output('git', 'add', str(path))
        cmd_output('chmod', mode, str(path))
        cmd_output('git', 'update-index', f'--chmod={mode}', str(path))

        # simulate how identify chooses that something is executable
        filenames = [path for path in [str(path)] if os.access(path, os.X_OK)]

        assert main(filenames) == expected
```

## File: `tests/check_illegal_windows_names_test.py`
```python
from __future__ import annotations

import os.path
import re

import pytest

from pre_commit_hooks.check_yaml import yaml


@pytest.fixture(scope='module')
def hook_re():
    here = os.path.dirname(__file__)
    with open(os.path.join(here, '..', '.pre-commit-hooks.yaml')) as f:
        hook_defs = yaml.load(f)
    hook, = (
        hook
        for hook in hook_defs
        if hook['id'] == 'check-illegal-windows-names'
    )
    yield re.compile(hook['files'])


@pytest.mark.parametrize(
    's',
    (
        pytest.param('aux.txt', id='with ext'),
        pytest.param('aux', id='without ext'),
        pytest.param('AuX.tXt', id='capitals'),
        pytest.param('com7.dat', id='com with digit'),
        pytest.param(':', id='bare colon'),
        pytest.param('file:Zone.Identifier', id='mid colon'),
        pytest.param('path/COM¹.json', id='com with superscript'),
        pytest.param('dir/LPT³.toml', id='lpt with superscript'),
        pytest.param('with < less than', id='with less than'),
        pytest.param('Fast or Slow?.md', id='with question mark'),
        pytest.param('with "double" quotes', id='with double quotes'),
        pytest.param('with_null\x00byte', id='with null byte'),
        pytest.param('ends_with.', id='ends with period'),
        pytest.param('ends_with ', id='ends with space'),
        pytest.param('ends_with\t', id='ends with tab'),
        pytest.param('dir/ends./with.txt', id='directory ends with period'),
        pytest.param('dir/ends /with.txt', id='directory ends with space'),
    ),
)
def test_check_illegal_windows_names_matches(hook_re, s):
    assert hook_re.search(s)


@pytest.mark.parametrize(
    's',
    (
        pytest.param('README.md', id='standard file'),
        pytest.param('foo.aux', id='as ext'),
        pytest.param('com.dat', id='com without digit'),
        pytest.param('.python-version', id='starts with period'),
        pytest.param(' pseudo nan', id='with spaces'),
        pytest.param('!@#$%^&;=≤\'~`¡¿€🤗', id='with allowed characters'),
        pytest.param('path.to/file.py', id='standard path'),
    ),
)
def test_check_illegal_windows_names_does_not_match(hook_re, s):
    assert hook_re.search(s) is None
```

## File: `tests/check_json_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.check_json import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('bad_json.notjson', 1),
        ('bad_json_latin1.nonjson', 1),
        ('ok_json.json', 0),
        ('duplicate_key_json.notjson', 1),
    ),
)
def test_main(capsys, filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval
    if expected_retval == 1:
        stdout, _ = capsys.readouterr()
        assert filename in stdout


def test_non_utf8_file(tmpdir):
    f = tmpdir.join('t.json')
    f.write_binary(b'\xa9\xfe\x12')
    assert main((str(f),))
```

## File: `tests/check_merge_conflict_test.py`
```python
from __future__ import annotations

import os
import shutil

import pytest

from pre_commit_hooks.check_merge_conflict import main
from pre_commit_hooks.util import cmd_output
from testing.util import get_resource_path
from testing.util import git_commit


@pytest.fixture
def f1_is_a_conflict_file(tmpdir):
    # Make a merge conflict
    repo1 = tmpdir.join('repo1')
    repo1_f1 = repo1.join('f1')
    repo2 = tmpdir.join('repo2')
    repo2_f1 = repo2.join('f1')

    cmd_output('git', 'init', '--', str(repo1))
    with repo1.as_cwd():
        repo1_f1.ensure()
        cmd_output('git', 'add', '.')
        git_commit('-m', 'commit1')

    cmd_output('git', 'clone', str(repo1), str(repo2))

    # Commit in mainline
    with repo1.as_cwd():
        repo1_f1.write('parent\n')
        git_commit('-am', 'mainline commit2')

    # Commit in clone and pull
    with repo2.as_cwd():
        repo2_f1.write('child\n')
        git_commit('-am', 'clone commit2')
        cmd_output('git', 'pull', '--no-rebase', retcode=None)
        # We should end up in a merge conflict!
        f1 = repo2_f1.read()
        assert f1.startswith(
            '<<<<<<< HEAD\n'
            'child\n'
            '=======\n'
            'parent\n'
            '>>>>>>>',
        ) or f1.startswith(
            '<<<<<<< HEAD\n'
            'child\n'
            # diff3 conflict style git merges add this line:
            '||||||| merged common ancestors\n'
            '=======\n'
            'parent\n'
            '>>>>>>>',
        ) or f1.startswith(
            # .gitconfig with [pull] rebase = preserve causes a rebase which
            # flips parent / child
            '<<<<<<< HEAD\n'
            'parent\n'
            '=======\n'
            'child\n'
            '>>>>>>>',
        )
        assert os.path.exists(os.path.join('.git', 'MERGE_MSG'))
        yield repo2


@pytest.fixture
def repository_pending_merge(tmpdir):
    # Make a (non-conflicting) merge
    repo1 = tmpdir.join('repo1')
    repo1_f1 = repo1.join('f1')
    repo2 = tmpdir.join('repo2')
    repo2_f1 = repo2.join('f1')
    repo2_f2 = repo2.join('f2')
    cmd_output('git', 'init', str(repo1))
    with repo1.as_cwd():
        repo1_f1.ensure()
        cmd_output('git', 'add', '.')
        git_commit('-m', 'commit1')

    cmd_output('git', 'clone', str(repo1), str(repo2))

    # Commit in mainline
    with repo1.as_cwd():
        repo1_f1.write('parent\n')
        git_commit('-am', 'mainline commit2')

    # Commit in clone and pull without committing
    with repo2.as_cwd():
        repo2_f2.write('child\n')
        cmd_output('git', 'add', '.')
        git_commit('-m', 'clone commit2')
        cmd_output('git', 'pull', '--no-commit', '--no-rebase')
        # We should end up in a pending merge
        assert repo2_f1.read() == 'parent\n'
        assert repo2_f2.read() == 'child\n'
        assert os.path.exists(os.path.join('.git', 'MERGE_HEAD'))
        yield repo2


@pytest.mark.usefixtures('f1_is_a_conflict_file')
def test_merge_conflicts_git(capsys):
    assert main(['f1']) == 1
    out, _ = capsys.readouterr()
    assert out == (
        "f1:1: Merge conflict string '<<<<<<<' found\n"
        "f1:3: Merge conflict string '=======' found\n"
        "f1:5: Merge conflict string '>>>>>>>' found\n"
    )


@pytest.mark.parametrize(
    'contents', (b'<<<<<<< HEAD\n', b'=======\n', b'>>>>>>> main\n'),
)
def test_merge_conflicts_failing(contents, repository_pending_merge):
    repository_pending_merge.join('f2').write_binary(contents)
    assert main(['f2']) == 1


@pytest.mark.parametrize(
    'contents', (b'# <<<<<<< HEAD\n', b'# =======\n', b'import mod', b''),
)
def test_merge_conflicts_ok(contents, f1_is_a_conflict_file):
    f1_is_a_conflict_file.join('f1').write_binary(contents)
    assert main(['f1']) == 0


@pytest.mark.usefixtures('f1_is_a_conflict_file')
def test_ignores_binary_files():
    shutil.copy(get_resource_path('img1.jpg'), 'f1')
    assert main(['f1']) == 0


def test_does_not_care_when_not_in_a_merge(tmpdir):
    f = tmpdir.join('README.md')
    f.write_binary(b'problem\n=======\n')
    assert main([str(f.realpath())]) == 0


def test_care_when_assumed_merge(tmpdir):
    f = tmpdir.join('README.md')
    f.write_binary(b'problem\n=======\n')
    assert main([str(f.realpath()), '--assume-in-merge']) == 1


def test_worktree_merge_conflicts(f1_is_a_conflict_file, tmpdir, capsys):
    worktree = tmpdir.join('worktree')
    cmd_output('git', 'worktree', 'add', str(worktree))
    with worktree.as_cwd():
        cmd_output(
            'git', 'pull', '--no-rebase', 'origin', 'HEAD', retcode=None,
        )
        msg = f1_is_a_conflict_file.join('.git/worktrees/worktree/MERGE_MSG')
        assert msg.exists()
        test_merge_conflicts_git(capsys)
```

## File: `tests/check_shebang_scripts_are_executable_test.py`
```python
from __future__ import annotations

import os

import pytest

from pre_commit_hooks.check_shebang_scripts_are_executable import \
    _check_git_filemode
from pre_commit_hooks.check_shebang_scripts_are_executable import main
from pre_commit_hooks.util import cmd_output


def test_check_git_filemode_passing(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('git', 'init', '.')

        f = tmpdir.join('f')
        f.write('#!/usr/bin/env bash')
        f_path = str(f)
        cmd_output('chmod', '+x', f_path)
        cmd_output('git', 'add', f_path)
        cmd_output('git', 'update-index', '--chmod=+x', f_path)

        g = tmpdir.join('g').ensure()
        g_path = str(g)
        cmd_output('git', 'add', g_path)

        files = [f_path, g_path]
        assert _check_git_filemode(files) == 0

        # this is the one we should trigger on
        h = tmpdir.join('h')
        h.write('#!/usr/bin/env bash')
        h_path = str(h)
        cmd_output('git', 'add', h_path)

        files = [h_path]
        assert _check_git_filemode(files) == 1


def test_check_git_filemode_passing_unusual_characters(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('git', 'init', '.')

        f = tmpdir.join('mañana.txt')
        f.write('#!/usr/bin/env bash')
        f_path = str(f)
        cmd_output('chmod', '+x', f_path)
        cmd_output('git', 'add', f_path)
        cmd_output('git', 'update-index', '--chmod=+x', f_path)

        files = (f_path,)
        assert _check_git_filemode(files) == 0


def test_check_git_filemode_failing(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('git', 'init', '.')

        f = tmpdir.join('f').ensure()
        f.write('#!/usr/bin/env bash')
        f_path = str(f)
        cmd_output('git', 'add', f_path)

        files = (f_path,)
        assert _check_git_filemode(files) == 1


@pytest.mark.parametrize(
    ('content', 'mode', 'expected'),
    (
        pytest.param('#!python', '+x', 0, id='shebang with executable'),
        pytest.param('#!python', '-x', 1, id='shebang without executable'),
        pytest.param('', '+x', 0, id='no shebang with executable'),
        pytest.param('', '-x', 0, id='no shebang without executable'),
    ),
)
def test_git_executable_shebang(temp_git_dir, content, mode, expected):
    with temp_git_dir.as_cwd():
        path = temp_git_dir.join('path')
        path.write(content)
        cmd_output('git', 'add', str(path))
        cmd_output('chmod', mode, str(path))
        cmd_output('git', 'update-index', f'--chmod={mode}', str(path))

        # simulate how identify chooses that something is executable
        filenames = [path for path in [str(path)] if os.access(path, os.X_OK)]

        assert main(filenames) == expected
```

## File: `tests/check_symlinks_test.py`
```python
from __future__ import annotations

import os

import pytest

from pre_commit_hooks.check_symlinks import main


xfail_symlink = pytest.mark.xfail(os.name == 'nt', reason='No symlink support')


@xfail_symlink
@pytest.mark.parametrize(
    ('dest', 'expected'), (('exists', 0), ('does-not-exist', 1)),
)
def test_main(tmpdir, dest, expected):  # pragma: no cover (symlinks)
    tmpdir.join('exists').ensure()
    symlink = tmpdir.join('symlink')
    symlink.mksymlinkto(tmpdir.join(dest))
    assert main((str(symlink),)) == expected


def test_main_normal_file(tmpdir):
    assert main((str(tmpdir.join('f').ensure()),)) == 0
```

## File: `tests/check_toml_test.py`
```python
from __future__ import annotations

from pre_commit_hooks.check_toml import main


def test_toml_bad(tmpdir):
    filename = tmpdir.join('f')
    filename.write("""
key = # INVALID

= "no key name"  # INVALID
""")
    ret = main((str(filename),))
    assert ret == 1


def test_toml_good(tmpdir):
    filename = tmpdir.join('f')
    filename.write(
        """
# This is a TOML document.

title = "TOML Example"

[owner]
name = "John"
dob = 1979-05-27T07:32:00-08:00 # First class dates
""",
    )
    ret = main((str(filename),))
    assert ret == 0


def test_toml_good_unicode(tmpdir):
    filename = tmpdir.join('f')
    filename.write_binary('letter = "\N{SNOWMAN}"\n'.encode())
    ret = main((str(filename),))
    assert ret == 0
```

## File: `tests/check_vcs_permalinks_test.py`
```python
from __future__ import annotations

from pre_commit_hooks.check_vcs_permalinks import main


def test_trivial(tmpdir):
    f = tmpdir.join('f.txt').ensure()
    assert not main((str(f),))


def test_passing(tmpdir):
    f = tmpdir.join('f.txt')
    f.write_binary(
        # permalinks are ok
        b'https://github.com/asottile/test/blob/649e6/foo%20bar#L1\n'
        # tags are ok
        b'https://github.com/asottile/test/blob/1.0.0/foo%20bar#L1\n'
        # links to files but not line numbers are ok
        b'https://github.com/asottile/test/blob/main/foo%20bar\n'
        # regression test for overly-greedy regex
        b'https://github.com/ yes / no ? /blob/main/foo#L1\n',
    )
    assert not main((str(f),))


def test_failing(tmpdir, capsys):
    with tmpdir.as_cwd():
        tmpdir.join('f.txt').write_binary(
            b'https://github.com/asottile/test/blob/main/foo#L1\n'
            b'https://example.com/asottile/test/blob/main/foo#L1\n',
        )

        assert main(('f.txt', '--additional-github-domain', 'example.com'))
        out, _ = capsys.readouterr()
        assert out == (
            'f.txt:1:https://github.com/asottile/test/blob/main/foo#L1\n'
            'f.txt:2:https://example.com/asottile/test/blob/main/foo#L1\n'
            '\n'
            'Non-permanent github link detected.\n'
            'On any page on github press [y] to load a permalink.\n'
        )
```

## File: `tests/check_xml_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.check_xml import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('bad_xml.notxml', 1),
        ('ok_xml.xml', 0),
    ),
)
def test_main(filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval
```

## File: `tests/check_yaml_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.check_yaml import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('bad_yaml.notyaml', 1),
        ('ok_yaml.yaml', 0),
    ),
)
def test_main(filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval


def test_main_allow_multiple_documents(tmpdir):
    f = tmpdir.join('test.yaml')
    f.write('---\nfoo\n---\nbar\n')

    # should fail without the setting
    assert main((str(f),))

    # should pass when we allow multiple documents
    assert not main(('--allow-multiple-documents', str(f)))


def test_fails_even_with_allow_multiple_documents(tmpdir):
    f = tmpdir.join('test.yaml')
    f.write('[')
    assert main(('--allow-multiple-documents', str(f)))


def test_main_unsafe(tmpdir):
    f = tmpdir.join('test.yaml')
    f.write(
        'some_foo: !vault |\n'
        '    $ANSIBLE_VAULT;1.1;AES256\n'
        '    deadbeefdeadbeefdeadbeef\n',
    )
    # should fail "safe" check
    assert main((str(f),))
    # should pass when we allow unsafe documents
    assert not main(('--unsafe', str(f)))


def test_main_unsafe_still_fails_on_syntax_errors(tmpdir):
    f = tmpdir.join('test.yaml')
    f.write('[')
    assert main(('--unsafe', str(f)))
```

## File: `tests/conftest.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.util import cmd_output


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join('gits')
    cmd_output('git', 'init', '--', str(git_dir))
    yield git_dir
```

## File: `tests/debug_statement_hook_test.py`
```python
from __future__ import annotations

import ast

from pre_commit_hooks.debug_statement_hook import Debug
from pre_commit_hooks.debug_statement_hook import DebugStatementParser
from pre_commit_hooks.debug_statement_hook import main
from testing.util import get_resource_path


def test_no_breakpoints():
    visitor = DebugStatementParser()
    visitor.visit(ast.parse('import os\nfrom foo import bar\n'))
    assert visitor.breakpoints == []


def test_finds_debug_import_attribute_access():
    visitor = DebugStatementParser()
    visitor.visit(ast.parse('import ipdb; ipdb.set_trace()'))
    assert visitor.breakpoints == [Debug(1, 0, 'ipdb', 'imported')]


def test_finds_debug_import_from_import():
    visitor = DebugStatementParser()
    visitor.visit(ast.parse('from pudb import set_trace; set_trace()'))
    assert visitor.breakpoints == [Debug(1, 0, 'pudb', 'imported')]


def test_finds_breakpoint():
    visitor = DebugStatementParser()
    visitor.visit(ast.parse('breakpoint()'))
    assert visitor.breakpoints == [Debug(1, 0, 'breakpoint', 'called')]


def test_returns_one_for_failing_file(tmpdir):
    f_py = tmpdir.join('f.py')
    f_py.write('def f():\n    import pdb; pdb.set_trace()')
    ret = main([str(f_py)])
    assert ret == 1


def test_returns_zero_for_passing_file():
    ret = main([__file__])
    assert ret == 0


def test_syntaxerror_file():
    ret = main([get_resource_path('cannot_parse_ast.notpy')])
    assert ret == 1


def test_non_utf8_file(tmpdir):
    f_py = tmpdir.join('f.py')
    f_py.write_binary('# -*- coding: cp1252 -*-\nx = "€"\n'.encode('cp1252'))
    assert main((str(f_py),)) == 0


def test_py37_breakpoint(tmpdir, capsys):
    f_py = tmpdir.join('f.py')
    f_py.write('def f():\n    breakpoint()\n')
    assert main((str(f_py),)) == 1
    out, _ = capsys.readouterr()
    assert out == f'{f_py}:2:4: breakpoint called\n'
```

## File: `tests/destroyed_symlinks_test.py`
```python
from __future__ import annotations

import os
import subprocess

import pytest

from pre_commit_hooks.destroyed_symlinks import find_destroyed_symlinks
from pre_commit_hooks.destroyed_symlinks import main
from testing.util import git_commit

TEST_SYMLINK = 'test_symlink'
TEST_SYMLINK_TARGET = '/doesnt/really/matters'
TEST_FILE = 'test_file'
TEST_FILE_RENAMED = f'{TEST_FILE}_renamed'


@pytest.fixture
def repo_with_destroyed_symlink(tmpdir):
    source_repo = tmpdir.join('src')
    os.makedirs(source_repo, exist_ok=True)
    test_repo = tmpdir.join('test')
    with source_repo.as_cwd():
        subprocess.check_call(('git', 'init'))
        os.symlink(TEST_SYMLINK_TARGET, TEST_SYMLINK)
        with open(TEST_FILE, 'w') as f:
            print('some random content', file=f)
        subprocess.check_call(('git', 'add', '.'))
        git_commit('-m', 'initial')
        assert b'120000 ' in subprocess.check_output(
            ('git', 'cat-file', '-p', 'HEAD^{tree}'),
        )
    subprocess.check_call(
        ('git', '-c', 'core.symlinks=false', 'clone', source_repo, test_repo),
    )
    with test_repo.as_cwd():
        subprocess.check_call(
            ('git', 'config', '--local', 'core.symlinks', 'true'),
        )
        subprocess.check_call(('git', 'mv', TEST_FILE, TEST_FILE_RENAMED))
    assert not os.path.islink(test_repo.join(TEST_SYMLINK))
    yield test_repo


def test_find_destroyed_symlinks(repo_with_destroyed_symlink):
    with repo_with_destroyed_symlink.as_cwd():
        assert find_destroyed_symlinks([]) == []
        assert main([]) == 0

        subprocess.check_call(('git', 'add', TEST_SYMLINK))
        assert find_destroyed_symlinks([TEST_SYMLINK]) == [TEST_SYMLINK]
        assert find_destroyed_symlinks([]) == []
        assert main([]) == 0
        assert find_destroyed_symlinks([TEST_FILE_RENAMED, TEST_FILE]) == []
        ALL_STAGED = [TEST_SYMLINK, TEST_FILE_RENAMED]
        assert find_destroyed_symlinks(ALL_STAGED) == [TEST_SYMLINK]
        assert main(ALL_STAGED) != 0

        with open(TEST_SYMLINK, 'a') as f:
            print(file=f)  # add trailing newline
        subprocess.check_call(['git', 'add', TEST_SYMLINK])
        assert find_destroyed_symlinks(ALL_STAGED) == [TEST_SYMLINK]
        assert main(ALL_STAGED) != 0

        with open(TEST_SYMLINK, 'w') as f:
            print('0' * len(TEST_SYMLINK_TARGET), file=f)
        subprocess.check_call(('git', 'add', TEST_SYMLINK))
        assert find_destroyed_symlinks(ALL_STAGED) == []
        assert main(ALL_STAGED) == 0

        with open(TEST_SYMLINK, 'w') as f:
            print('0' * (len(TEST_SYMLINK_TARGET) + 3), file=f)
        subprocess.check_call(('git', 'add', TEST_SYMLINK))
        assert find_destroyed_symlinks(ALL_STAGED) == []
        assert main(ALL_STAGED) == 0
```

## File: `tests/detect_aws_credentials_test.py`
```python
from __future__ import annotations

from unittest.mock import patch

import pytest

from pre_commit_hooks.detect_aws_credentials import get_aws_cred_files_from_env
from pre_commit_hooks.detect_aws_credentials import get_aws_secrets_from_env
from pre_commit_hooks.detect_aws_credentials import get_aws_secrets_from_file
from pre_commit_hooks.detect_aws_credentials import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('env_vars', 'values'),
    (
        ({}, set()),
        ({'AWS_PLACEHOLDER_KEY': '/foo'}, set()),
        ({'AWS_CONFIG_FILE': '/foo'}, {'/foo'}),
        ({'AWS_CREDENTIAL_FILE': '/foo'}, {'/foo'}),
        ({'AWS_SHARED_CREDENTIALS_FILE': '/foo'}, {'/foo'}),
        ({'BOTO_CONFIG': '/foo'}, {'/foo'}),
        ({'AWS_PLACEHOLDER_KEY': '/foo', 'AWS_CONFIG_FILE': '/bar'}, {'/bar'}),
        (
            {
                'AWS_PLACEHOLDER_KEY': '/foo', 'AWS_CONFIG_FILE': '/bar',
                'AWS_CREDENTIAL_FILE': '/baz',
            },
            {'/bar', '/baz'},
        ),
        (
            {
                'AWS_CONFIG_FILE': '/foo', 'AWS_CREDENTIAL_FILE': '/bar',
                'AWS_SHARED_CREDENTIALS_FILE': '/baz',
            },
            {'/foo', '/bar', '/baz'},
        ),
    ),
)
def test_get_aws_credentials_file_from_env(env_vars, values):
    with patch.dict('os.environ', env_vars, clear=True):
        assert get_aws_cred_files_from_env() == values


@pytest.mark.parametrize(
    ('env_vars', 'values'),
    (
        ({}, set()),
        ({'AWS_PLACEHOLDER_KEY': 'foo'}, set()),
        ({'AWS_SECRET_ACCESS_KEY': 'foo'}, {'foo'}),
        ({'AWS_SECURITY_TOKEN': 'foo'}, {'foo'}),
        ({'AWS_SESSION_TOKEN': 'foo'}, {'foo'}),
        ({'AWS_SESSION_TOKEN': ''}, set()),
        ({'AWS_SESSION_TOKEN': 'foo', 'AWS_SECURITY_TOKEN': ''}, {'foo'}),
        (
            {'AWS_PLACEHOLDER_KEY': 'foo', 'AWS_SECRET_ACCESS_KEY': 'bar'},
            {'bar'},
        ),
        (
            {'AWS_SECRET_ACCESS_KEY': 'foo', 'AWS_SECURITY_TOKEN': 'bar'},
            {'foo', 'bar'},
        ),
    ),
)
def test_get_aws_secrets_from_env(env_vars, values):
    """Test that reading secrets from environment variables works."""
    with patch.dict('os.environ', env_vars, clear=True):
        assert get_aws_secrets_from_env() == values


@pytest.mark.parametrize(
    ('filename', 'expected_keys'),
    (
        (
            'aws_config_with_secret.ini',
            {'z2rpgs5uit782eapz5l1z0y2lurtsyyk6hcfozlb'},
        ),
        ('aws_config_with_session_token.ini', {'foo'}),
        (
            'aws_config_with_secret_and_session_token.ini',
            {'z2rpgs5uit782eapz5l1z0y2lurtsyyk6hcfozlb', 'foo'},
        ),
        (
            'aws_config_with_multiple_sections.ini',
            {
                '7xebzorgm5143ouge9gvepxb2z70bsb2rtrh099e',
                'z2rpgs5uit782eapz5l1z0y2lurtsyyk6hcfozlb',
                'ixswosj8gz3wuik405jl9k3vdajsnxfhnpui38ez',
                'foo',
            },
        ),
        ('aws_config_without_secrets.ini', set()),
        ('aws_config_without_secrets_with_spaces.ini', set()),
        ('nonsense.txt', set()),
        ('ok_json.json', set()),
    ),
)
def test_get_aws_secrets_from_file(filename, expected_keys):
    """Test that reading secrets from files works."""
    keys = get_aws_secrets_from_file(get_resource_path(filename))
    assert keys == expected_keys


@pytest.mark.parametrize(
    ('filename', 'expected_retval'),
    (
        ('aws_config_with_secret.ini', 1),
        ('aws_config_with_session_token.ini', 1),
        ('aws_config_with_multiple_sections.ini', 1),
        ('aws_config_without_secrets.ini', 0),
        ('aws_config_without_secrets_with_spaces.ini', 0),
        ('nonsense.txt', 0),
        ('ok_json.json', 0),
    ),
)
def test_detect_aws_credentials(filename, expected_retval):
    # with a valid credentials file
    ret = main((
        get_resource_path(filename),
        '--credentials-file',
        'testing/resources/aws_config_with_multiple_sections.ini',
    ))
    assert ret == expected_retval


def test_allows_arbitrarily_encoded_files(tmpdir):
    src_ini = tmpdir.join('src.ini')
    src_ini.write(
        '[default]\n'
        'aws_access_key_id=AKIASDFASDF\n'
        'aws_secret_Access_key=9018asdf23908190238123\n',
    )
    arbitrary_encoding = tmpdir.join('f')
    arbitrary_encoding.write_binary(b'\x12\x9a\xe2\xf2')
    ret = main((str(arbitrary_encoding), '--credentials-file', str(src_ini)))
    assert ret == 0


@patch('pre_commit_hooks.detect_aws_credentials.get_aws_secrets_from_file')
@patch('pre_commit_hooks.detect_aws_credentials.get_aws_secrets_from_env')
def test_non_existent_credentials(mock_secrets_env, mock_secrets_file, capsys):
    """Test behavior with no configured AWS secrets."""
    mock_secrets_env.return_value = set()
    mock_secrets_file.return_value = set()
    ret = main((
        get_resource_path('aws_config_without_secrets.ini'),
        '--credentials-file=testing/resources/credentailsfilethatdoesntexist',
    ))
    assert ret == 2
    out, _ = capsys.readouterr()
    assert out == (
        'No AWS keys were found in the configured credential files '
        'and environment variables.\nPlease ensure you have the '
        'correct setting for --credentials-file\n'
    )


@patch('pre_commit_hooks.detect_aws_credentials.get_aws_secrets_from_file')
@patch('pre_commit_hooks.detect_aws_credentials.get_aws_secrets_from_env')
def test_non_existent_credentials_with_allow_flag(
        mock_secrets_env, mock_secrets_file,
):
    mock_secrets_env.return_value = set()
    mock_secrets_file.return_value = set()
    ret = main((
        get_resource_path('aws_config_without_secrets.ini'),
        '--credentials-file=testing/resources/credentailsfilethatdoesntexist',
        '--allow-missing-credentials',
    ))
    assert ret == 0
```

## File: `tests/detect_private_key_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.detect_private_key import main

# Input, expected return value
TESTS = (
    (b'-----BEGIN RSA PRIVATE KEY-----', 1),
    (b'-----BEGIN DSA PRIVATE KEY-----', 1),
    (b'-----BEGIN EC PRIVATE KEY-----', 1),
    (b'-----BEGIN OPENSSH PRIVATE KEY-----', 1),
    (b'PuTTY-User-Key-File-2: ssh-rsa', 1),
    (b'---- BEGIN SSH2 ENCRYPTED PRIVATE KEY ----', 1),
    (b'-----BEGIN ENCRYPTED PRIVATE KEY-----', 1),
    (b'-----BEGIN OpenVPN Static key V1-----', 1),
    (b'ssh-rsa DATA', 0),
    (b'ssh-dsa DATA', 0),
    # Some arbitrary binary data
    (b'\xa2\xf1\x93\x12', 0),
)


@pytest.mark.parametrize(('input_s', 'expected_retval'), TESTS)
def test_main(input_s, expected_retval, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)
    assert main([str(path)]) == expected_retval
```

## File: `tests/end_of_file_fixer_test.py`
```python
from __future__ import annotations

import io

import pytest

from pre_commit_hooks.end_of_file_fixer import fix_file
from pre_commit_hooks.end_of_file_fixer import main


# Input, expected return value, expected output
TESTS = (
    (b'foo\n', 0, b'foo\n'),
    (b'', 0, b''),
    (b'\n\n', 1, b''),
    (b'\n\n\n\n', 1, b''),
    (b'foo', 1, b'foo\n'),
    (b'foo\n\n\n', 1, b'foo\n'),
    (b'\xe2\x98\x83', 1, b'\xe2\x98\x83\n'),
    (b'foo\r\n', 0, b'foo\r\n'),
    (b'foo\r\n\r\n\r\n', 1, b'foo\r\n'),
    (b'foo\r', 0, b'foo\r'),
    (b'foo\r\r\r\r', 1, b'foo\r'),
)


@pytest.mark.parametrize(('input_s', 'expected_retval', 'output'), TESTS)
def test_fix_file(input_s, expected_retval, output):
    file_obj = io.BytesIO(input_s)
    ret = fix_file(file_obj)
    assert file_obj.getvalue() == output
    assert ret == expected_retval


@pytest.mark.parametrize(('input_s', 'expected_retval', 'output'), TESTS)
def test_integration(input_s, expected_retval, output, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)

    ret = main([str(path)])
    file_output = path.read_binary()

    assert file_output == output
    assert ret == expected_retval
```

## File: `tests/file_contents_sorter_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.file_contents_sorter import FAIL
from pre_commit_hooks.file_contents_sorter import main
from pre_commit_hooks.file_contents_sorter import PASS


@pytest.mark.parametrize(
    ('input_s', 'argv', 'expected_retval', 'output'),
    (
        (b'', [], PASS, b''),
        (b'\n', [], FAIL, b''),
        (b'\n\n', [], FAIL, b''),
        (b'lonesome\n', [], PASS, b'lonesome\n'),
        (b'missing_newline', [], FAIL, b'missing_newline\n'),
        (b'newline\nmissing', [], FAIL, b'missing\nnewline\n'),
        (b'missing\nnewline', [], FAIL, b'missing\nnewline\n'),
        (b'alpha\nbeta\n', [], PASS, b'alpha\nbeta\n'),
        (b'beta\nalpha\n', [], FAIL, b'alpha\nbeta\n'),
        (b'C\nc\n', [], PASS, b'C\nc\n'),
        (b'c\nC\n', [], FAIL, b'C\nc\n'),
        (b'mag ical \n tre vor\n', [], FAIL, b' tre vor\nmag ical \n'),
        (b'@\n-\n_\n#\n', [], FAIL, b'#\n-\n@\n_\n'),
        (b'extra\n\n\nwhitespace\n', [], FAIL, b'extra\nwhitespace\n'),
        (b'whitespace\n\n\nextra\n', [], FAIL, b'extra\nwhitespace\n'),
        (
            b'fee\nFie\nFoe\nfum\n',
            [],
            FAIL,
            b'Fie\nFoe\nfee\nfum\n',
        ),
        (
            b'Fie\nFoe\nfee\nfum\n',
            [],
            PASS,
            b'Fie\nFoe\nfee\nfum\n',
        ),
        (
            b'fee\nFie\nFoe\nfum\n',
            ['--ignore-case'],
            PASS,
            b'fee\nFie\nFoe\nfum\n',
        ),
        (
            b'Fie\nFoe\nfee\nfum\n',
            ['--ignore-case'],
            FAIL,
            b'fee\nFie\nFoe\nfum\n',
        ),
        (
            b'Fie\nFoe\nfee\nfee\nfum\n',
            ['--ignore-case'],
            FAIL,
            b'fee\nfee\nFie\nFoe\nfum\n',
        ),
        (
            b'Fie\nFoe\nfee\nfum\n',
            ['--unique'],
            PASS,
            b'Fie\nFoe\nfee\nfum\n',
        ),
        (
            b'Fie\nFie\nFoe\nfee\nfum\n',
            ['--unique'],
            FAIL,
            b'Fie\nFoe\nfee\nfum\n',
        ),
    ),
)
def test_integration(input_s, argv, expected_retval, output, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)

    output_retval = main([str(path)] + argv)

    assert path.read_binary() == output
    assert output_retval == expected_retval


@pytest.mark.parametrize(
    ('input_s', 'argv'),
    (
        (
            b'fee\nFie\nFoe\nfum\n',
            ['--unique', '--ignore-case'],
        ),
        (
            b'fee\nfee\nFie\nFoe\nfum\n',
            ['--unique', '--ignore-case'],
        ),
    ),
)
def test_integration_invalid_args(input_s, argv, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)

    with pytest.raises(SystemExit):
        main([str(path)] + argv)
```

## File: `tests/fix_byte_order_marker_test.py`
```python
from __future__ import annotations

from pre_commit_hooks import fix_byte_order_marker


def test_failure(tmpdir):
    f = tmpdir.join('f.txt')
    f.write_text('ohai', encoding='utf-8-sig')
    assert fix_byte_order_marker.main((str(f),)) == 1


def test_success(tmpdir):
    f = tmpdir.join('f.txt')
    f.write_text('ohai', encoding='utf-8')
    assert fix_byte_order_marker.main((str(f),)) == 0
```

## File: `tests/forbid_new_submodules_test.py`
```python
from __future__ import annotations

import os
import subprocess
from unittest import mock

import pytest

from pre_commit_hooks.forbid_new_submodules import main
from testing.util import git_commit


@pytest.fixture
def git_dir_with_git_dir(tmpdir):
    with tmpdir.as_cwd():
        subprocess.check_call(('git', 'init', '.'))
        git_commit('--allow-empty', '-m', 'init')
        subprocess.check_call(('git', 'init', 'foo'))
        git_commit('--allow-empty', '-m', 'init', cwd=str(tmpdir.join('foo')))
        yield


@pytest.mark.parametrize(
    'cmd',
    (
        # Actually add the submodule
        ('git', 'submodule', 'add', './foo'),
        # Sneaky submodule add (that doesn't show up in .gitmodules)
        ('git', 'add', 'foo'),
    ),
)
def test_main_new_submodule(git_dir_with_git_dir, capsys, cmd):
    subprocess.check_call(cmd)
    assert main(('random_non-related_file',)) == 0
    assert main(('foo',)) == 1
    out, _ = capsys.readouterr()
    assert out.startswith('foo: new submodule introduced\n')


def test_main_new_submodule_committed(git_dir_with_git_dir, capsys):
    rev_parse_cmd = ('git', 'rev-parse', 'HEAD')
    from_ref = subprocess.check_output(rev_parse_cmd).decode().strip()
    subprocess.check_call(('git', 'submodule', 'add', './foo'))
    git_commit('-m', 'new submodule')
    to_ref = subprocess.check_output(rev_parse_cmd).decode().strip()
    with mock.patch.dict(
        os.environ,
        {'PRE_COMMIT_FROM_REF': from_ref, 'PRE_COMMIT_TO_REF': to_ref},
    ):
        assert main(('random_non-related_file',)) == 0
        assert main(('foo',)) == 1
    out, _ = capsys.readouterr()
    assert out.startswith('foo: new submodule introduced\n')


def test_main_no_new_submodule(git_dir_with_git_dir):
    open('test.py', 'a+').close()
    subprocess.check_call(('git', 'add', 'test.py'))
    assert main(('test.py',)) == 0
```

## File: `tests/mixed_line_ending_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.mixed_line_ending import main


@pytest.mark.parametrize(
    ('input_s', 'output'),
    (
        # mixed with majority of 'LF'
        (b'foo\r\nbar\nbaz\n', b'foo\nbar\nbaz\n'),
        # mixed with majority of 'CRLF'
        (b'foo\r\nbar\nbaz\r\n', b'foo\r\nbar\r\nbaz\r\n'),
        # mixed with majority of 'CR'
        (b'foo\rbar\nbaz\r', b'foo\rbar\rbaz\r'),
        # mixed with as much 'LF' as 'CRLF'
        (b'foo\r\nbar\n', b'foo\nbar\n'),
        # mixed with as much 'LF' as 'CR'
        (b'foo\rbar\n', b'foo\nbar\n'),
        # mixed with as much 'CRLF' as 'CR'
        (b'foo\r\nbar\r', b'foo\r\nbar\r\n'),
        # mixed with as much 'CRLF' as 'LF' as 'CR'
        (b'foo\r\nbar\nbaz\r', b'foo\nbar\nbaz\n'),
    ),
)
def test_mixed_line_ending_fixes_auto(input_s, output, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)
    ret = main((str(path),))

    assert ret == 1
    assert path.read_binary() == output


def test_non_mixed_no_newline_end_of_file(tmpdir):
    path = tmpdir.join('f.txt')
    path.write_binary(b'foo\nbar\nbaz')
    assert not main((str(path),))
    # the hook *could* fix the end of the file, but leaves it alone
    # this is mostly to document the current behaviour
    assert path.read_binary() == b'foo\nbar\nbaz'


def test_mixed_no_newline_end_of_file(tmpdir):
    path = tmpdir.join('f.txt')
    path.write_binary(b'foo\r\nbar\nbaz')
    assert main((str(path),))
    # the hook rewrites the end of the file, this is slightly inconsistent
    # with the non-mixed case but I think this is the better behaviour
    # this is mostly to document the current behaviour
    assert path.read_binary() == b'foo\nbar\nbaz\n'


@pytest.mark.parametrize(
    ('fix_option', 'input_s'),
    (
        # All --fix=auto with uniform line endings should be ok
        ('--fix=auto', b'foo\r\nbar\r\nbaz\r\n'),
        ('--fix=auto', b'foo\rbar\rbaz\r'),
        ('--fix=auto', b'foo\nbar\nbaz\n'),
        # --fix=crlf with crlf endings
        ('--fix=crlf', b'foo\r\nbar\r\nbaz\r\n'),
        # --fix=lf with lf endings
        ('--fix=lf', b'foo\nbar\nbaz\n'),
    ),
)
def test_line_endings_ok(fix_option, input_s, tmpdir, capsys):
    path = tmpdir.join('input.txt')
    path.write_binary(input_s)
    ret = main((fix_option, str(path)))

    assert ret == 0
    assert path.read_binary() == input_s
    out, _ = capsys.readouterr()
    assert out == ''


def test_no_fix_does_not_modify(tmpdir, capsys):
    path = tmpdir.join('input.txt')
    contents = b'foo\r\nbar\rbaz\nwomp\n'
    path.write_binary(contents)
    ret = main(('--fix=no', str(path)))

    assert ret == 1
    assert path.read_binary() == contents
    out, _ = capsys.readouterr()
    assert out == f'{path}: mixed line endings\n'


def test_fix_lf(tmpdir, capsys):
    path = tmpdir.join('input.txt')
    path.write_binary(b'foo\r\nbar\rbaz\n')
    ret = main(('--fix=lf', str(path)))

    assert ret == 1
    assert path.read_binary() == b'foo\nbar\nbaz\n'
    out, _ = capsys.readouterr()
    assert out == f'{path}: fixed mixed line endings\n'


def test_fix_crlf(tmpdir):
    path = tmpdir.join('input.txt')
    path.write_binary(b'foo\r\nbar\rbaz\n')
    ret = main(('--fix=crlf', str(path)))

    assert ret == 1
    assert path.read_binary() == b'foo\r\nbar\r\nbaz\r\n'


def test_fix_lf_all_crlf(tmpdir):
    """Regression test for #239"""
    path = tmpdir.join('input.txt')
    path.write_binary(b'foo\r\nbar\r\n')
    ret = main(('--fix=lf', str(path)))

    assert ret == 1
    assert path.read_binary() == b'foo\nbar\n'
```

## File: `tests/no_commit_to_branch_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.no_commit_to_branch import is_on_branch
from pre_commit_hooks.no_commit_to_branch import main
from pre_commit_hooks.util import cmd_output
from testing.util import git_commit


def test_other_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'anotherbranch')
        assert is_on_branch({'placeholder'}) is False


def test_multi_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'another/branch')
        assert is_on_branch({'placeholder'}) is False


def test_multi_branch_fail(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'another/branch')
        assert is_on_branch({'another/branch'}) is True


def test_exact_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'branchname')
        assert is_on_branch({'branchname'}) is True


def test_main_branch_call(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'other')
        assert main(('--branch', 'other')) == 1


@pytest.mark.parametrize('branch_name', ('b1', 'b2'))
def test_forbid_multiple_branches(temp_git_dir, branch_name):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', branch_name)
        assert main(('--branch', 'b1', '--branch', 'b2'))


def test_branch_pattern_fail(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'another/branch')
        assert is_on_branch(set(), {'another/.*'}) is True


@pytest.mark.parametrize('branch_name', ('somebranch', 'another/branch'))
def test_branch_pattern_multiple_branches_fail(temp_git_dir, branch_name):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', branch_name)
        assert main(('--branch', 'somebranch', '--pattern', 'another/.*'))


def test_main_default_call(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'anotherbranch')
        assert main(()) == 0


def test_not_on_a_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        git_commit('--allow-empty', '-m1')
        head = cmd_output('git', 'rev-parse', 'HEAD').strip()
        cmd_output('git', 'checkout', head)
        # we're not on a branch!
        assert main(()) == 0


@pytest.mark.parametrize('branch_name', ('master', 'main'))
def test_default_branch_names(temp_git_dir, branch_name):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', branch_name)
        assert main(()) == 1
```

## File: `tests/pretty_format_json_test.py`
```python
from __future__ import annotations

import os
import shutil

import pytest

from pre_commit_hooks.pretty_format_json import main
from pre_commit_hooks.pretty_format_json import parse_num_to_int
from testing.util import get_resource_path


def test_parse_num_to_int():
    assert parse_num_to_int('0') == 0
    assert parse_num_to_int('2') == 2
    assert parse_num_to_int('\t') == '\t'
    assert parse_num_to_int('  ') == '  '


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('not_pretty_formatted_json.json', 1),
        ('unsorted_pretty_formatted_json.json', 1),
        ('non_ascii_pretty_formatted_json.json', 1),
        ('pretty_formatted_json.json', 0),
    ),
)
def test_main(filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('not_pretty_formatted_json.json', 1),
        ('unsorted_pretty_formatted_json.json', 0),
        ('non_ascii_pretty_formatted_json.json', 1),
        ('pretty_formatted_json.json', 0),
    ),
)
def test_unsorted_main(filename, expected_retval):
    ret = main(['--no-sort-keys', get_resource_path(filename)])
    assert ret == expected_retval


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('not_pretty_formatted_json.json', 1),
        ('unsorted_pretty_formatted_json.json', 1),
        ('non_ascii_pretty_formatted_json.json', 1),
        ('pretty_formatted_json.json', 1),
        ('tab_pretty_formatted_json.json', 0),
    ),
)
def test_tab_main(filename, expected_retval):
    ret = main(['--indent', '\t', get_resource_path(filename)])
    assert ret == expected_retval


def test_non_ascii_main():
    ret = main((
        '--no-ensure-ascii',
        get_resource_path('non_ascii_pretty_formatted_json.json'),
    ))
    assert ret == 0


def test_autofix_main(tmpdir):
    srcfile = tmpdir.join('to_be_json_formatted.json')
    shutil.copyfile(
        get_resource_path('not_pretty_formatted_json.json'),
        str(srcfile),
    )

    # now launch the autofix on that file
    ret = main(['--autofix', str(srcfile)])
    # it should have formatted it
    assert ret == 1

    # file was formatted (shouldn't trigger linter again)
    ret = main([str(srcfile)])
    assert ret == 0


def test_invalid_main(tmpdir):
    srcfile1 = tmpdir.join('not_valid_json.json')
    srcfile1.write(
        '{\n'
        '  // not json\n'
        '  "a": "b"\n'
        '}',
    )
    srcfile2 = tmpdir.join('to_be_json_formatted.json')
    srcfile2.write('{ "a": "b" }')

    # it should have skipped the first file and formatted the second one
    assert main(['--autofix', str(srcfile1), str(srcfile2)]) == 1

    # confirm second file was formatted (shouldn't trigger linter again)
    assert main([str(srcfile2)]) == 0


def test_orderfile_get_pretty_format():
    ret = main((
        '--top-keys=alist', get_resource_path('pretty_formatted_json.json'),
    ))
    assert ret == 0


def test_not_orderfile_get_pretty_format():
    ret = main((
        '--top-keys=blah', get_resource_path('pretty_formatted_json.json'),
    ))
    assert ret == 1


def test_top_sorted_get_pretty_format():
    ret = main((
        '--top-keys=01-alist,alist', get_resource_path('top_sorted_json.json'),
    ))
    assert ret == 0


def test_badfile_main():
    ret = main([get_resource_path('ok_yaml.yaml')])
    assert ret == 1


def test_diffing_output(capsys):
    resource_path = get_resource_path('not_pretty_formatted_json.json')
    expected_retval = 1
    a = os.path.join('a', resource_path)
    b = os.path.join('b', resource_path)
    expected_out = f'''\
--- {a}
+++ {b}
@@ -1,6 +1,9 @@
 {{
-    "foo":
-    "bar",
-        "alist": [2, 34, 234],
-  "blah": null
+  "alist": [
+    2,
+    34,
+    234
+  ],
+  "blah": null,
+  "foo": "bar"
 }}
'''
    actual_retval = main([resource_path])
    actual_out, actual_err = capsys.readouterr()

    assert actual_retval == expected_retval
    assert actual_out == expected_out
    assert actual_err == ''
```

## File: `tests/readme_test.py`
```python
from __future__ import annotations

from pre_commit_hooks.check_yaml import yaml


def test_readme_contains_all_hooks():
    with open('README.md', encoding='UTF-8') as f:
        readme_contents = f.read()
    with open('.pre-commit-hooks.yaml', encoding='UTF-8') as f:
        hooks = yaml.load(f)
    for hook in hooks:
        assert f'`{hook["id"]}`' in readme_contents
```

## File: `tests/removed_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.removed import main


def test_always_fails():
    with pytest.raises(SystemExit) as excinfo:
        main((
            'autopep8-wrapper', 'autopep8',
            'https://github.com/pre-commit/mirrors-autopep8',
            '--foo', 'bar',
        ))
    msg, = excinfo.value.args
    assert msg == (
        '`autopep8-wrapper` has been removed -- '
        'use `autopep8` from https://github.com/pre-commit/mirrors-autopep8'
    )
```

## File: `tests/requirements_txt_fixer_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.requirements_txt_fixer import FAIL
from pre_commit_hooks.requirements_txt_fixer import main
from pre_commit_hooks.requirements_txt_fixer import PASS
from pre_commit_hooks.requirements_txt_fixer import Requirement


@pytest.mark.parametrize(
    ('input_s', 'expected_retval', 'output'),
    (
        (b'', PASS, b''),
        (b'\n', PASS, b'\n'),
        (b'# intentionally empty\n', PASS, b'# intentionally empty\n'),
        (b'foo\n# comment at end\n', PASS, b'foo\n# comment at end\n'),
        (b'foo\nbar\n', FAIL, b'bar\nfoo\n'),
        (b'bar\nfoo\n', PASS, b'bar\nfoo\n'),
        (b'a\nc\nb\n', FAIL, b'a\nb\nc\n'),
        (b'a\nc\nb', FAIL, b'a\nb\nc\n'),
        (b'a\nb\nc', FAIL, b'a\nb\nc\n'),
        (
            b'#comment1\nfoo\n#comment2\nbar\n',
            FAIL,
            b'#comment2\nbar\n#comment1\nfoo\n',
        ),
        (
            b'#comment1\nbar\n#comment2\nfoo\n',
            PASS,
            b'#comment1\nbar\n#comment2\nfoo\n',
        ),
        (b'#comment\n\nfoo\nbar\n', FAIL, b'#comment\n\nbar\nfoo\n'),
        (b'#comment\n\nbar\nfoo\n', PASS, b'#comment\n\nbar\nfoo\n'),
        (
            b'foo\n\t#comment with indent\nbar\n',
            FAIL,
            b'\t#comment with indent\nbar\nfoo\n',
        ),
        (
            b'bar\n\t#comment with indent\nfoo\n',
            PASS,
            b'bar\n\t#comment with indent\nfoo\n',
        ),
        (b'\nfoo\nbar\n', FAIL, b'bar\n\nfoo\n'),
        (b'\nbar\nfoo\n', PASS, b'\nbar\nfoo\n'),
        (
            b'pyramid-foo==1\npyramid>=2\n',
            FAIL,
            b'pyramid>=2\npyramid-foo==1\n',
        ),
        (
            b'a==1\n'
            b'c>=1\n'
            b'bbbb!=1\n'
            b'c-a>=1;python_version>="3.6"\n'
            b'e>=2\n'
            b'd>2\n'
            b'g<2\n'
            b'f<=2\n',
            FAIL,
            b'a==1\n'
            b'bbbb!=1\n'
            b'c>=1\n'
            b'c-a>=1;python_version>="3.6"\n'
            b'd>2\n'
            b'e>=2\n'
            b'f<=2\n'
            b'g<2\n',
        ),
        (b'a==1\nb==1\na==1\n', FAIL, b'a==1\nb==1\n'),
        (
            b'a==1\nb==1\n#comment about a\na==1\n',
            FAIL,
            b'#comment about a\na==1\nb==1\n',
        ),
        (b'ocflib\nDjango\nPyMySQL\n', FAIL, b'Django\nocflib\nPyMySQL\n'),
        (
            b'-e git+ssh://git_url@tag#egg=ocflib\nDjango\nPyMySQL\n',
            FAIL,
            b'Django\n-e git+ssh://git_url@tag#egg=ocflib\nPyMySQL\n',
        ),
        (b'bar\npkg-resources==0.0.0\nfoo\n', FAIL, b'bar\nfoo\n'),
        (b'foo\npkg-resources==0.0.0\nbar\n', FAIL, b'bar\nfoo\n'),
        (b'bar\npkg_resources==0.0.0\nfoo\n', FAIL, b'bar\nfoo\n'),
        (b'foo\npkg_resources==0.0.0\nbar\n', FAIL, b'bar\nfoo\n'),
        (
            b'git+ssh://git_url@tag#egg=ocflib\nDjango\nijk\n',
            FAIL,
            b'Django\nijk\ngit+ssh://git_url@tag#egg=ocflib\n',
        ),
        (
            b'b==1.0.0\n'
            b'c=2.0.0 \\\n'
            b' --hash=sha256:abcd\n'
            b'a=3.0.0 \\\n'
            b'  --hash=sha256:a1b1c1d1',
            FAIL,
            b'a=3.0.0 \\\n'
            b'  --hash=sha256:a1b1c1d1\n'
            b'b==1.0.0\n'
            b'c=2.0.0 \\\n'
            b' --hash=sha256:abcd\n',
        ),
        (
            b'a=2.0.0 \\\n --hash=sha256:abcd\nb==1.0.0\n',
            PASS,
            b'a=2.0.0 \\\n --hash=sha256:abcd\nb==1.0.0\n',
        ),
    ),
)
def test_integration(input_s, expected_retval, output, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)

    output_retval = main([str(path)])

    assert path.read_binary() == output
    assert output_retval == expected_retval


def test_requirement_object():
    top_of_file = Requirement()
    top_of_file.comments.append(b'#foo')
    top_of_file.value = b'\n'

    requirement_foo = Requirement()
    requirement_foo.value = b'foo'

    requirement_bar = Requirement()
    requirement_bar.value = b'bar'

    # This may look redundant, but we need to test both foo.__lt__(bar) and
    # bar.__lt__(foo)
    assert requirement_foo > top_of_file
    assert top_of_file < requirement_foo
    assert requirement_foo > requirement_bar
    assert requirement_bar < requirement_foo
```

## File: `tests/sort_simple_yaml_test.py`
```python
from __future__ import annotations

import os

import pytest

from pre_commit_hooks.sort_simple_yaml import first_key
from pre_commit_hooks.sort_simple_yaml import main
from pre_commit_hooks.sort_simple_yaml import parse_block
from pre_commit_hooks.sort_simple_yaml import parse_blocks
from pre_commit_hooks.sort_simple_yaml import sort

RETVAL_GOOD = 0
RETVAL_BAD = 1
TEST_SORTS = [
    (
        ['c: true', '', 'b: 42', 'a: 19'],
        ['b: 42', 'a: 19', '', 'c: true'],
        RETVAL_BAD,
    ),

    (
        ['# i am', '# a header', '', 'c: true', '', 'b: 42', 'a: 19'],
        ['# i am', '# a header', '', 'b: 42', 'a: 19', '', 'c: true'],
        RETVAL_BAD,
    ),

    (
        ['# i am', '# a header', '', 'already: sorted', '', 'yup: i am'],
        ['# i am', '# a header', '', 'already: sorted', '', 'yup: i am'],
        RETVAL_GOOD,
    ),

    (
        ['# i am', '# a header'],
        ['# i am', '# a header'],
        RETVAL_GOOD,
    ),
]


@pytest.mark.parametrize('bad_lines,good_lines,retval', TEST_SORTS)
def test_integration_good_bad_lines(tmpdir, bad_lines, good_lines, retval):
    file_path = os.path.join(str(tmpdir), 'foo.yaml')

    with open(file_path, 'w') as f:
        f.write('\n'.join(bad_lines) + '\n')

    assert main([file_path]) == retval

    with open(file_path) as f:
        assert [line.rstrip() for line in f.readlines()] == good_lines


def test_parse_header():
    lines = ['# some header', '# is here', '', 'this is not a header']
    assert parse_block(lines, header=True) == ['# some header', '# is here']
    assert lines == ['', 'this is not a header']

    lines = ['this is not a header']
    assert parse_block(lines, header=True) == []
    assert lines == ['this is not a header']


def test_parse_block():
    # a normal block
    lines = ['a: 42', 'b: 17', '', 'c: 19']
    assert parse_block(lines) == ['a: 42', 'b: 17']
    assert lines == ['', 'c: 19']

    # a block at the end
    lines = ['c: 19']
    assert parse_block(lines) == ['c: 19']
    assert lines == []

    # no block
    lines = []
    assert parse_block(lines) == []
    assert lines == []


def test_parse_blocks():
    # normal blocks
    lines = ['a: 42', 'b: 17', '', 'c: 19']
    assert parse_blocks(lines) == [['a: 42', 'b: 17'], ['c: 19']]
    assert lines == []

    # a single block
    lines = ['a: 42', 'b: 17']
    assert parse_blocks(lines) == [['a: 42', 'b: 17']]
    assert lines == []

    # no blocks
    lines = []
    assert parse_blocks(lines) == []
    assert lines == []


def test_first_key():
    # first line
    lines = ['a: 42', 'b: 17', '', 'c: 19']
    assert first_key(lines) == 'a: 42'

    # second line
    lines = ['# some comment', 'a: 42', 'b: 17', '', 'c: 19']
    assert first_key(lines) == 'a: 42'

    # second line with quotes
    lines = ['# some comment', '"a": 42', 'b: 17', '', 'c: 19']
    assert first_key(lines) == 'a": 42'

    # no lines (not a real situation)
    lines = []
    assert first_key(lines) == ''


@pytest.mark.parametrize('bad_lines,good_lines,_', TEST_SORTS)
def test_sort(bad_lines, good_lines, _):
    assert sort(bad_lines) == good_lines
```

## File: `tests/string_fixer_test.py`
```python
from __future__ import annotations

import textwrap

import pytest

from pre_commit_hooks.string_fixer import main

TESTS = (
    # Base cases
    ("''", "''", 0),
    ('""', "''", 1),
    (r'"\'"', r'"\'"', 0),
    (r'"\""', r'"\""', 0),
    (r"'\"\"'", r"'\"\"'", 0),
    # String somewhere in the line
    ('x = "foo"', "x = 'foo'", 1),
    # Test escaped characters
    (r'"\'"', r'"\'"', 0),
    # Docstring
    ('""" Foo """', '""" Foo """', 0),
    (
        textwrap.dedent(
            """
        x = " \\
        foo \\
        "\n
        """,
        ),
        textwrap.dedent(
            """
        x = ' \\
        foo \\
        '\n
        """,
        ),
        1,
    ),
    ('"foo""bar"', "'foo''bar'", 1),
    pytest.param(
        "f'hello{\"world\"}'",
        "f'hello{\"world\"}'",
        0,
        id='ignore nested fstrings',
    ),
)


@pytest.mark.parametrize(('input_s', 'output', 'expected_retval'), TESTS)
def test_rewrite(input_s, output, expected_retval, tmpdir):
    path = tmpdir.join('file.py')
    path.write(input_s)
    retval = main([str(path)])
    assert path.read() == output
    assert retval == expected_retval


def test_rewrite_crlf(tmpdir):
    f = tmpdir.join('f.py')
    f.write_binary(b'"foo"\r\n"bar"\r\n')
    assert main((str(f),))
    assert f.read_binary() == b"'foo'\r\n'bar'\r\n"
```

## File: `tests/tests_should_end_in_test_test.py`
```python
from __future__ import annotations

from pre_commit_hooks.tests_should_end_in_test import main


def test_main_all_pass():
    ret = main(['foo_test.py', 'bar_test.py'])
    assert ret == 0


def test_main_one_fails():
    ret = main(['not_test_ending.py', 'foo_test.py'])
    assert ret == 1


def test_regex():
    assert main(('foo_test_py',)) == 1


def test_main_django_all_pass():
    ret = main((
        '--django', 'tests.py', 'test_foo.py', 'test_bar.py',
        'tests/test_baz.py',
    ))
    assert ret == 0


def test_main_django_one_fails():
    ret = main(['--django', 'not_test_ending.py', 'test_foo.py'])
    assert ret == 1


def test_validate_nested_files_django_one_fails():
    ret = main(['--django', 'tests/not_test_ending.py', 'test_foo.py'])
    assert ret == 1


def test_main_not_django_fails():
    ret = main(['foo_test.py', 'bar_test.py', 'test_baz.py'])
    assert ret == 1


def test_main_django_fails():
    ret = main(['--django', 'foo_test.py', 'test_bar.py', 'test_baz.py'])
    assert ret == 1


def test_main_pytest_test_first():
    assert main(['--pytest-test-first', 'test_foo.py']) == 0
    assert main(['--pytest-test-first', 'foo_test.py']) == 1
```

## File: `tests/trailing_whitespace_fixer_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.trailing_whitespace_fixer import main


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('foo \nbar \n', 'foo\nbar\n'),
        ('bar\t\nbaz\t\n', 'bar\nbaz\n'),
    ),
)
def test_fixes_trailing_whitespace(input_s, expected, tmpdir):
    path = tmpdir.join('file.md')
    path.write(input_s)
    assert main((str(path),)) == 1
    assert path.read() == expected


def test_ok_no_newline_end_of_file(tmpdir):
    filename = tmpdir.join('f')
    filename.write_binary(b'foo\nbar')
    ret = main((str(filename),))
    assert filename.read_binary() == b'foo\nbar'
    assert ret == 0


def test_ok_with_dos_line_endings(tmpdir):
    filename = tmpdir.join('f')
    filename.write_binary(b'foo\r\nbar\r\nbaz\r\n')
    ret = main((str(filename),))
    assert filename.read_binary() == b'foo\r\nbar\r\nbaz\r\n'
    assert ret == 0


@pytest.mark.parametrize('ext', ('md', 'Md', '.md', '*'))
def test_fixes_markdown_files(tmpdir, ext):
    path = tmpdir.join('test.md')
    path.write(
        'foo  \n'  # leaves alone
        'bar \n'  # less than two so it is removed
        'baz    \n'  # more than two so it becomes two spaces
        '\t\n'  # trailing tabs are stripped anyway
        '\n  ',  # whitespace at the end of the file is removed
    )
    ret = main((str(path), f'--markdown-linebreak-ext={ext}'))
    assert ret == 1
    assert path.read() == (
        'foo  \n'
        'bar\n'
        'baz  \n'
        '\n'
        '\n'
    )


@pytest.mark.parametrize('arg', ('--', 'a.b', 'a/b', ''))
def test_markdown_linebreak_ext_badopt(arg):
    with pytest.raises(SystemExit) as excinfo:
        main(['--markdown-linebreak-ext', arg])
    assert excinfo.value.code == 2


def test_prints_warning_with_no_markdown_ext(capsys, tmpdir):
    f = tmpdir.join('f').ensure()
    assert main((str(f), '--no-markdown-linebreak-ext')) == 0
    out, _ = capsys.readouterr()
    assert out == '--no-markdown-linebreak-ext now does nothing!\n'


def test_preserve_non_utf8_file(tmpdir):
    non_utf8_bytes_content = b'<a>\xe9 \n</a>\n'
    path = tmpdir.join('file.txt')
    path.write_binary(non_utf8_bytes_content)
    ret = main([str(path)])
    assert ret == 1
    assert path.size() == (len(non_utf8_bytes_content) - 1)


def test_custom_charset_change(tmpdir):
    # strip spaces only, no tabs
    path = tmpdir.join('file.txt')
    path.write('\ta \t \n')
    ret = main([str(path), '--chars', ' '])
    assert ret == 1
    assert path.read() == '\ta \t\n'


def test_custom_charset_no_change(tmpdir):
    path = tmpdir.join('file.txt')
    path.write('\ta \t\n')
    ret = main([str(path), '--chars', ' '])
    assert ret == 0


def test_markdown_with_custom_charset(tmpdir):
    path = tmpdir.join('file.md')
    path.write('\ta \t   \n')
    ret = main([str(path), '--chars', ' ', '--markdown-linebreak-ext', '*'])
    assert ret == 1
    assert path.read() == '\ta \t  \n'
```

## File: `tests/util_test.py`
```python
from __future__ import annotations

import pytest

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit


def test_raises_on_error():
    with pytest.raises(CalledProcessError):
        cmd_output('sh', '-c', 'exit 1')


def test_output():
    ret = cmd_output('sh', '-c', 'echo hi')
    assert ret == 'hi\n'


@pytest.mark.parametrize('out', ('\0f1\0f2\0', '\0f1\0f2', 'f1\0f2\0'))
def test_check_zsplits_str_correctly(out):
    assert zsplit(out) == ['f1', 'f2']


@pytest.mark.parametrize('out', ('\0\0', '\0', ''))
def test_check_zsplit_returns_empty(out):
    assert zsplit(out) == []
```

