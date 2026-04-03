---
id: junegunn-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.724657
---

# KNOWLEDGE EXTRACT: junegunn
> **Extracted on:** 2026-03-30 17:38:14
> **Source:** junegunn

---

## File: `vim-plug.md`
```markdown
# 📦 junegunn/vim-plug [🔖 PENDING/APPROVE]
🔗 https://github.com/junegunn/vim-plug
🌐 https://junegunn.github.io/vim-plug/

## Meta
- **Stars:** ⭐ 35598 | **Forks:** 🍴 1949
- **Language:** Vim Script | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
:hibiscus: Minimalist Vim Plugin Manager

## README (trích đầu)
```
<h1 title="vim-plug">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./plug-dark.png">
    <img src="./plug.png" height="75" alt="vim-plug">
  </picture>
  <a href="https://github.com/junegunn/vim-plug/actions/workflows/test.yml?query=branch%3Amaster">
    <img src="https://img.shields.io/github/actions/workflow/status/junegunn/vim-plug/test.yml?branch=master">
  </a>
</h1>

A minimalist Vim plugin manager.

<img src="https://raw.githubusercontent.com/junegunn/i/master/vim-plug/installer.gif" height="450">

## Pros.

- Minimalist design
    - Just one file with no dependencies. Super easy to set up.
    - Concise, intuitive syntax that you can learn within minutes. No boilerplate code required.
    - No feature bloat
- Extremely stable with flawless backward compatibility
    - Works perfectly with all versions of Vim since 2006 and all versions of Neovim ever released
- [Super-fast][40/4] parallel installation/update
- Creates shallow clones to minimize disk space usage and download time
- On-demand loading for [faster startup time][startup-time]
- Can review and rollback updates
- Branch/tag/commit support
- Post-update hooks
- Support for externally managed plugins

[40/4]: https://raw.githubusercontent.com/junegunn/i/master/vim-plug/40-in-4.gif
[startup-time]: https://github.com/junegunn/vim-startuptime-benchmark#result

## Installation

[Download plug.vim](https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim)
and put it in the "autoload" directory.

<details>
<summary>Click to see the instructions</summary>

### Vim

#### Unix

```sh
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

You can automate the process by putting the command in your Vim configuration
file as suggested [here][auto].

[auto]: https://github.com/junegunn/vim-plug/wiki/tips#automatic-installation

#### Windows (PowerShell)

```powershell
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni $HOME/vimfiles/autoload/plug.vim -Force
```

### Neovim

#### Unix, Linux

```sh
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

#### Linux (Flatpak)

```sh
curl -fLo ~/.var/app/io.neovim.nvim/data/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

#### Windows (PowerShell)

```powershell
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni "$(@($env:XDG_DATA_HOME, $env:LOCALAPPDATA)[$null -eq $env:XDG_DATA_HOME])/nvim-data/site/autoload/plug.vim" -Force
```

</details>

## Usage

Add a vim-plug section to your `~/.vimrc` (or `~/.config/nvim/init.vim` for Neovim)

1. Begin the section with `call plug#begin()`
1. List the plugins with `Plug` commands
1. End the section with `call plug#end()`

For example,
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

