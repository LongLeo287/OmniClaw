---
id: cli-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:06.678554
---

# KNOWLEDGE EXTRACT: cli
> **Extracted on:** 2026-03-30 17:34:25
> **Source:** cli

---

## File: `cli.md`
```markdown
# 📦 cli/cli [🔖 PENDING]
🔗 https://github.com/cli/cli
🌐 https://cli.github.com

## Meta
- **Stars:** ⭐ 43388 | **Forks:** 🍴 8163
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
GitHub’s official command line tool

## README (trích đầu)
```
# GitHub CLI

`gh` is GitHub on the command line. It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with `git` and your code.

![screenshot of gh pr status](https://user-images.githubusercontent.com/98482/84171218-327e7a80-aa40-11ea-8cd1-5177fc2d0e72.png)

GitHub CLI is supported for users on GitHub.com, GitHub Enterprise Cloud, and GitHub Enterprise Server 2.20+ with support for macOS, Windows, and Linux.

## Documentation

For [installation options see below](#installation), for usage instructions [see the manual](https://cli.github.com/manual/).

## Contributing

If anything feels off or if you feel that some functionality is missing, please check out the [contributing page](../bmad_repo/CONTRIBUTING.md). There you will find instructions for sharing your feedback, building the tool locally, and submitting pull requests to the project.

If you are a hubber and are interested in shipping new commands for the CLI, check out our [doc on internal contributions](brain/knowledge/docs_legacy/working-with-us.md)

<!-- this anchor is linked to from elsewhere, so avoid renaming it -->
## Installation

### [macOS](brain/knowledge/docs_legacy/install_macos.md)

- [Homebrew](brain/knowledge/docs_legacy/install_macos.md#homebrew)
- [Precompiled binaries](brain/knowledge/docs_legacy/install_macos.md#precompiled-binaries) on [releases page][]

For additional macOS packages and installers, see [community-supported docs](brain/knowledge/docs_legacy/install_macos.md#community-unofficial)

### [Linux & Unix](brain/knowledge/docs_legacy/install_linux.md)

- [Debian, Raspberry Pi, Ubuntu](brain/knowledge/docs_legacy/install_linux.md#debian)
- [Amazon Linux, CentOS, Fedora, openSUSE, RHEL, SUSE](brain/knowledge/docs_legacy/install_linux.md#rpm)
- [Precompiled binaries](brain/knowledge/docs_legacy/install_linux.md#precompiled-binaries) on [releases page][]

For additional Linux & Unix packages and installers, see [community-supported docs](brain/knowledge/docs_legacy/install_linux.md#community-unofficial)

### [Windows](brain/knowledge/docs_legacy/install_windows.md)

- [WinGet](brain/knowledge/docs_legacy/install_windows.md#winget)
- [Precompiled binaries](brain/knowledge/docs_legacy/install_windows.md#precompiled-binaries) on [releases page][]

For additional Windows packages and installers, see [community-supported docs](brain/knowledge/docs_legacy/install_windows.md#community-unofficial)

### Build from source

See here on how to [build GitHub CLI from source](brain/knowledge/docs_legacy/install_source.md).

### GitHub Codespaces

To add GitHub CLI to your codespace, add the following to your [devcontainer file](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-features-to-a-devcontainer-file):

```json
"features": {
  "ghcr.io/devcontainers/features/github-cli:1": {}
}
```

### GitHub Actions

[GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners) have the GitHub CLI pre-installed, which is updated weekly.

If a specific version is needed, your GitHub Actions workflow will need to install it based on the [macOS](#macos), [Linux & Unix](#linux--unix), or [Windows](#windows) instructions above.

For information on all pre-installed tools, see [`actions/
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

