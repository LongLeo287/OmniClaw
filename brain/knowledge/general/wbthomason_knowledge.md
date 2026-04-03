---
id: wbthomason-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.516397
---

# KNOWLEDGE EXTRACT: wbthomason
> **Extracted on:** 2026-03-30 18:01:16
> **Source:** wbthomason

---

## File: `packer.nvim.md`
```markdown
# 📦 wbthomason/packer.nvim [🔖 PENDING/APPROVE]
🔗 https://github.com/wbthomason/packer.nvim


## Meta
- **Stars:** ⭐ 8108 | **Forks:** 🍴 267
- **Language:** Lua | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A use-package inspired plugin manager for Neovim. Uses native packages, supports Luarocks dependencies, written in Lua, allows for expressive config

## README (trích đầu)
```
**NOTICE:**

This repository is currently unmaintained. For the time being (as of August, 2023), it is recommended to use one of the following plugin managers instead:

- [lazy.nvim](https://github.com/folke/lazy.nvim): Most stable and maintained plugin manager for Nvim.
- [pckr.nvim](https://github.com/lewis6991/pckr.nvim): Spiritual successor of packer.nvim. Functional but not as stable as lazy.nvim.

# packer.nvim

[![Gitter](https://badges.gitter.im/packer-nvim/community.svg)](https://gitter.im/packer-nvim/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

[`use-package`](https://github.com/jwiegley/use-package) inspired plugin/package management for
Neovim.

Have questions? Start a [discussion](https://github.com/wbthomason/packer.nvim/discussions).

Have a problem or idea? Make an [issue](https://github.com/wbthomason/packer.nvim/issues) or a [PR](https://github.com/wbthomason/packer.nvim/pulls).

**Packer is built on native packages. You may wish to read `:h packages` before continuing**

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Quickstart](#quickstart)
4. [Bootstrapping](#bootstrapping)
5. [Usage](#usage)
    1. [The startup function](#the-startup-function)
    2. [Custom Initialization](#custom-initialization)
    3. [Specifying Plugins](#specifying-plugins)
    4. [Performing plugin management operations](#performing-plugin-management-operations)
    5. [Extending packer](#extending-packer)
    6. [Compiling Lazy-Loaders](#compiling-lazy-loaders)
	7. [User autocommands](#user-autocommands)
	8. [Using a floating window](#using-a-floating-window)
6. [Profiling](#profiling)
7. [Debugging](#debugging)
8. [Compatibility and known issues](#compatibility-and-known-issues)
9. [Contributors](#contributors)

## Features
- Declarative plugin specification
- Support for dependencies
- Support for Luarocks dependencies
- Expressive configuration and lazy-loading options
- Automatically compiles efficient lazy-loading code to improve startup time
- Uses native packages
- Extensible
- Written in Lua, configured in Lua
- Post-install/update hooks
- Uses jobs for async installation
- Support for `git` tags, branches, revisions, submodules
- Support for local plugins

## Requirements
- You need to be running **Neovim v0.5.0+**
- If you are on Windows 10, you need developer mode enabled in order to use local plugins (creating
  symbolic links requires admin privileges on Windows - credit to @TimUntersberger for this note)

## Quickstart
To get started, first clone this repository to somewhere on your `packpath`, e.g.:

> Unix, Linux Installation

```shell
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

If you use Arch Linux, there is also [an AUR
package](https://aur.archlinux.org/packages/nvim-packer-git/).

> Windows Powershell Installation

```shell
git clone https://github.com/wbthomason/packer.nvim "$env:LOCALAPPDATA\
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

