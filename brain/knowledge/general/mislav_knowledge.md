---
id: mislav-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.771263
---

# KNOWLEDGE EXTRACT: mislav
> **Extracted on:** 2026-03-30 17:42:52
> **Source:** mislav

---

## File: `bump-homebrew-formula-action.md`
```markdown
# 📦 mislav/bump-homebrew-formula-action [🔖 PENDING/APPROVE]
🔗 https://github.com/mislav/bump-homebrew-formula-action


## Meta
- **Stars:** ⭐ 198 | **Forks:** 🍴 43
- **Language:** TypeScript | **License:** Unlicense
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Automatically bump Homebrew formula after a release

## README (trích đầu)
```
A minimal GitHub action that uses the GitHub API to bump a Homebrew formula
after a new release in your repository.

Usage example:

```yml
on:
  push:
    tags: 'v*'

jobs:
  homebrew:
    name: Bump Homebrew formula
    runs-on: ubuntu-latest
    steps:
      - uses: mislav/bump-homebrew-formula-action@v4
        with:
          # By default, this will edit the `my_formula.rb` formula in
          # homebrew-core to update its "url" field to:
          # `https://github.com/OWNER/REPO/archive/refs/tags/<tag-name>.tar.gz`
          # The "sha256" formula field will get automatically recomputed.
          formula-name: my_formula
        env:
          # the personal access token should have "repo" & "workflow" scopes
          COMMITTER_TOKEN: ${{ secrets.COMMITTER_TOKEN }}
```

The `COMMITTER_TOKEN` secret is required because this action will want to write
to an external repository. You can [generate a new Personal Access Token (classic)
here](https://github.com/settings/tokens) and give it `repo` and `workflow` scopes.

## How it works

Given a Homebrew formula `Formula/my_formula.rb` in the
[homebrew-core](https://github.com/Homebrew/homebrew-core) repo:

```rb
class MyFormula < Formula
  url "https://github.com/me/myproject/archive/refs/tags/v1.2.3.tar.gz"
  sha256 "<OLDSHA>"
  # ...
end
```

After we push a `v2.0.0` git tag to a project that has this action configured,
the formula will be updated to:

```rb
class MyFormula < Formula
  url "https://github.com/me/myproject/archive/refs/tags/v2.0.0.tar.gz"
  sha256 "<NEWSHA>"
  # ...
end
```

This action can update the following Homebrew formula fields:

- `version`
- `url`
- `sha256` - for non-git `download-url` action input
- `tag` - for git-based `download-url`
- `revision` - for git-based `download-url`

## Action inputs

Formula parameters:

- `formula-name`: the name of the Homebrew formula to bump. Defaults to
  lower-cased repository name.

- `formula-path`: the relative path of the Homebrew formula file to edit within the `homebrew-tap` repository. Defaults to
  `Formula/<letter>/<formula-name>.rb` for homebrew-core formulae and `Formula/<formula-name>.rb` otherwise.

- `tag-name`: the git tag name to bump the formula to. Defaults to the
  currently pushed tag.

- `download-url`: the package download URL for the Homebrew formula.

  Defaults to `https://github.com/OWNER/REPO/archive/refs/tags/<tag-name>.tar.gz`, where `OWNER/REPO` is the repository that is running the Actions workflow.

- `download-sha256`: the SHA256 checksum of the archive at `download-url`.
  Defaults to calculating the checksum by fetching the archive at run time.

Repository parameters:

- `homebrew-tap`: the full GitHub repository name (in the `NAME/OWNER` format) where the Homebrew formula should be updated. Defaults
  to `Homebrew/homebrew-core`.

- `push-to`: a specific fork of `homebrew-tap` where the edit should be pushed to.
  Defaults to creating or reusing a personal fork of the owner of COMMITTER_TOKEN.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

