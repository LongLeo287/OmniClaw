---
id: innobead-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.361087
---

# KNOWLEDGE EXTRACT: innobead
> **Extracted on:** 2026-03-30 17:38:10
> **Source:** innobead

---

## File: `huber.md`
```markdown
# 📦 innobead/huber [🔖 PENDING/APPROVE]
🔗 https://github.com/innobead/huber
🌐 https://innobead.github.io/huber/

## Meta
- **Stars:** ⭐ 223 | **Forks:** 🍴 13
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-19
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Huber: simplify GitHub package management

## README (trích đầu)
```
<div align="center" style="text-align: center;">
<img src="https://raw.githubusercontent.com/innobead/huber/HEAD/docs/src/images/huber_logo.png" alt="huber" style="width:300px;"/>
</div>

<div align="center">

[![crates.io](https://img.shields.io/crates/v/huber.svg)](https://crates.io/crates/huber)
[![Releases](https://img.shields.io/github/release/innobead/huber/all.svg)](https://github.com/innobead/huber/releases)
[![GitHub](https://img.shields.io/github/license/innobead/huber)](https://github.com/innobead/huber/blob/master/LICENSE)
[![Docs](https://img.shields.io/badge/docs-latest-green.svg)](https://innobead.github.io/huber/)

</div>

**Huber** is a command-line interface tool for managing packages released from GitHub repositories. It allows you to install, update, and manage packages from GitHub repository releases in a simple and efficient way.

What features does Huber provide?

- Manage (install, update, uninstall, show, current) multiple version packages from GitHub repository releases
- Search popular GitHub repositories that Huber manages in a [curated list](docs/src/contributing/huber-managed-packages.md)
- Manage your own repositories to install packages you need
- Lock and unlock installed package versions
- Save and restore package versions
- and more..., please check the documentation for more details

> [!NOTE]  
> This documentation is for the version starting from 1.0.0. If you are using older versions, suggest upgrading to the latest version.

# Installation

Huber is supported on Linux, macOS, and Windows platforms.

- Linux (x86_64/amd64, aarch64/arm64, arm)
- MacOS (x86_64/amd64, aarch64/arm64)
- Windows (x86_64/amd64)

You can install Huber via the following methods:

**Cargo:**

```shell
cargo install huber
```

**Shell script:**

```shell
curl -sfSL https://raw.githubusercontent.com/innobead/huber/main/hack/install.sh | sh -
```

**PowerShell:**

```powershell
. { iwr -useb https://raw.githubusercontent.com/innobead/huber/main/hack/windows/install.ps1 } | iex; install
```

**Precompiled binaries:**

Download Huber executables from [GitHub releases](https://github.com/innobead/huber/releases)

# Getting Started

After installing Huber, you can start using it by running the `huber` command.

```console
$ huber --help
Huber, simplify GitHub package management

Usage: huber [OPTIONS] <COMMAND>

Commands:
  config       Manage Huber configurations
  current      Update the current package versions
  completions  Show command completions for the specified shell
  flush        Remove outdated installed artifacts
  info         Show package information
  install      Install packages
  repo         Manage repositories
  reset        Reset Huber
  search       Search package
  self-update  Update huber
  show         Show installed packages
  uninstall    Uninstall packages
  update       Updates the installed packages
  save         Save the installed package list to a file
  load         Load installed packages from a file gen
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

