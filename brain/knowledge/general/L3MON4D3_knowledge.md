---
id: l3mon4d3-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:02.186479
---

# KNOWLEDGE EXTRACT: L3MON4D3
> **Extracted on:** 2026-03-30 17:38:57
> **Source:** L3MON4D3

---

## File: `LuaSnip.md`
```markdown
# 📦 L3MON4D3/LuaSnip [🔖 PENDING/APPROVE]
🔗 https://github.com/L3MON4D3/LuaSnip


## Meta
- **Stars:** ⭐ 4308 | **Forks:** 🍴 267
- **Language:** Lua | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Snippet Engine for Neovim written in Lua.

## README (trích đầu)
```
[![LuaSnip](https://img.shields.io/matrix/luasnip:matrix.org?label=Matrix&logo=matrix)](https://matrix.to/#/%23luasnip:matrix.org)
# LuaSnip
https://user-images.githubusercontent.com/41961280/122515860-5179fa00-d00e-11eb-91f7-331893f61fbf.mp4

# Features
- Tabstops
- Text-Transformations using Lua functions
- Conditional Expansion
- Defining nested Snippets
- Filetype-specific Snippets
- Choices
- Dynamic Snippet creation
- Regex-Trigger
- Autotriggered Snippets
- Easy Postfix Snippets
- Fast
- Parse [LSP-Style](https://microsoft.github.io/language-server-protocol/specification#snippet_syntax) Snippets either directly in Lua, as a VSCode package or a SnipMate snippet collection.
- Expand LSP-Snippets with [nvim-compe](https://github.com/hrsh7th/nvim-compe) (or its' successor, [nvim-cmp](https://github.com/hrsh7th/nvim-cmp) (requires [cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)))
- Snippet history (jump back into older snippets)
- Resolve filetype at the cursor using Treesitter

# Drawbacks
- Snippets that make use of the entire functionality of this plugin have to be defined in Lua (but 95% of snippets can be written in LSP-syntax).

# Requirements
Neovim >= 0.7 (extmarks)
`jsregexp` for `lsp-snippet-transformations` (see [here](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#transformations) for some tips on installing it).

# Setup
## Install
* With your preferred plugin manager i.e. [vim-plug](https://github.com/junegunn/vim-plug), [Packer](https://github.com/wbthomason/packer.nvim) or [lazy](https://github.com/folke/lazy.nvim)  
  **Packer**:
  ```lua
  use({
  	"L3MON4D3/LuaSnip",
  	-- follow latest release.
  	tag = "v2.*", -- Replace <CurrentMajor> by the latest released major (first number of latest release)
  	-- install jsregexp (optional!:).
  	run = "make install_jsregexp"
  })
  ```
  **lazy**:
  ```lua
  {
  	"L3MON4D3/LuaSnip",
  	-- follow latest release.
  	version = "v2.*", -- Replace <CurrentMajor> by the latest released major (first number of latest release)
  	-- install jsregexp (optional!).
  	build = "make install_jsregexp"
  }
  ```
  **vim-plug**:
  ```vim
  " follow latest release and install jsregexp.
  Plug 'L3MON4D3/LuaSnip', {'tag': 'v2.*', 'do': 'make install_jsregexp'} " Replace <CurrentMajor> by the latest released major (first number of latest release)
  ```
  Check the `Releases`-section to the right for the latest major version.

* LuaSnip uses [Semantic Versioning](https://semver.org) (with some leeway, big patches might end up as a Minor version)!  
  Releases will be tagged as `vMajor.Minor.Patch`, we recommend following the latest Major release.  
  Consider watching the repository's releases so you're notified when a new version becomes available.

> [!NOTE]
> On Windows, you need a C compiler and `make` to install `jsregexp`. If your
> compiler choice is not `gcc`, `clang`, or `zig`, you need to explicitly
> specify the `CC` variable in the build command: `make install_jsregexp
> CC
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

