---
id: nvim-telescope-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:13.501839
---

# KNOWLEDGE EXTRACT: nvim-telescope
> **Extracted on:** 2026-03-30 17:49:32
> **Source:** nvim-telescope

---

## File: `telescope.nvim.md`
```markdown
# 📦 nvim-telescope/telescope.nvim [🔖 PENDING/APPROVE]
🔗 https://github.com/nvim-telescope/telescope.nvim


## Meta
- **Stars:** ⭐ 19233 | **Forks:** 🍴 943
- **Language:** Lua | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Find, Filter, Preview, Pick. All lua, all the time.

## README (trích đầu)
```
# telescope.nvim

[![LuaRocks](https://img.shields.io/luarocks/v/Conni2461/telescope.nvim?logo=lua&color=purple)](https://luarocks.org/modules/Conni2461/telescope.nvim)

Gaze deeply into unknown regions using the power of the moon.

## What Is Telescope?

`telescope.nvim` is a highly extendable fuzzy finder over lists. Built on the
latest awesome features from `neovim` core. Telescope is centered around
modularity, allowing for easy customization.

Community driven builtin [pickers](#pickers), [sorters](#sorters) and
[previewers](#previewers).

![Preview](https://i.imgur.com/TTTja6t.gif)
<sub>For more showcases of Telescope, please visit the [Showcase
section](https://github.com/nvim-telescope/telescope.nvim/wiki/Showcase) in the
Telescope Wiki</sub>

## Telescope Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Customization](#customization)
- [Default Mappings](#default-mappings)
- [Pickers](#pickers)
- [Previewers](#previewers)
- [Sorters](#sorters)
- [Layout](#layout-display)
- [Themes](#themes)
- [Commands](#vim-commands)
- [Autocmds](#autocmds)
- [Extensions](#extensions)
- [API](#api)
- [Media](#media)
- [Contributing](#contributing)
- [Changelog](https://github.com/nvim-telescope/telescope.nvim/blob/master/doc/telescope_changelog.txt)

## Getting Started

This section should guide you to run your first builtin pickers.

[Neovim (>v0.10.4)](https://github.com/neovim/neovim/releases/tag/v0.10.4) or the
latest neovim nightly commit is required for `telescope.nvim` to work.
The neovim version also needs to be compiled with LuaJIT; PUC Lua is not fully supported,
both for performance reasons and because extensions may rely on FFI.

### Required dependencies

- [nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim) is required.

### Suggested dependencies

- [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) is required for
  `live_grep` and `grep_string` and is the first priority for `find_files`.

We also strongly suggest installing a native telescope sorter to significantly improve
sorting performance:
* [telescope-fzf-native.nvim](https://github.com/nvim-telescope/telescope-fzf-native.nvim)
or
* [telescope-fzy-native.nvim](https://github.com/nvim-telescope/telescope-fzy-native.nvim).
For more information and a performance benchmark take a look at the
[Extensions](https://github.com/nvim-telescope/telescope.nvim/wiki/Extensions)
wiki.

### Optional dependencies

- [sharkdp/fd](https://github.com/sharkdp/fd) (finder)
- [devicons](https://github.com/nvim-tree/nvim-web-devicons) (icons)

### Installation

We recommend pinning to the latest release
[tag](https://github.com/nvim-telescope/telescope.nvim/tags),
e.g. using [lazy.nvim](https://github.com/folke/lazy.nvim)

```lua
{
    'nvim-telescope/telescope.nvim', version = '*',
    dependencies = {
        'nvim-lua/plenary.nvim',
        -- optional but recommended
        { 'nvim-telescope/telescope-fzf-native.nvim', build = 'make' },
    }
}
``
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

