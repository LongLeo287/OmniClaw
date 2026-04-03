---
id: rcarriga-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:06.708643
---

# KNOWLEDGE EXTRACT: rcarriga
> **Extracted on:** 2026-03-30 17:52:59
> **Source:** rcarriga

---

## File: `nvim-dap-ui.md`
```markdown
# 📦 rcarriga/nvim-dap-ui [🔖 PENDING/APPROVE]
🔗 https://github.com/rcarriga/nvim-dap-ui


## Meta
- **Stars:** ⭐ 3303 | **Forks:** 🍴 124
- **Language:** Lua | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A UI for nvim-dap

## README (trích đầu)
```
# nvim-dap-ui

## Introduction

A UI for [nvim-dap](https://github.com/mfussenegger/nvim-dap) which provides a
good out of the box configuration.

![preview](https://user-images.githubusercontent.com/24252670/191198389-a1321363-c0f1-4ff1-b663-ab1350d2b393.png)

## Installation

Install with your favourite package manager alongside nvim-dap and nvim-nio

[**dein**](https://github.com/Shougo/dein.vim):

```vim
call dein#add("mfussenegger/nvim-dap")
call dein#add("nvim-neotest/nvim-nio")
call dein#add("rcarriga/nvim-dap-ui")
```

[**vim-plug**](https://github.com/junegunn/vim-plug)

```vim
Plug 'mfussenegger/nvim-dap'
Plug 'nvim-neotest/nvim-nio'
Plug 'rcarriga/nvim-dap-ui'
```

[**packer.nvim**](https://github.com/wbthomason/packer.nvim)

```lua
use { "rcarriga/nvim-dap-ui", requires = {"mfussenegger/nvim-dap", "nvim-neotest/nvim-nio"} }
```

[**lazy.nvim**](https://github.com/folke/lazy.nvim)

```lua
{ "rcarriga/nvim-dap-ui", dependencies = {"mfussenegger/nvim-dap", "nvim-neotest/nvim-nio"} }
```

It is highly recommended to use [lazydev.nvim](https://github.com/folke/lazydev.nvim) to enable type checking for nvim-dap-ui to get
type checking, documentation and autocompletion for all API functions.

```lua
require("lazydev").setup({
  library = { "nvim-dap-ui" },
})
```

The default icons use [codicons](https://github.com/microsoft/vscode-codicons).
It's recommended to use this [fork](https://github.com/ChristianChiarulli/neovim-codicons) which fixes alignment issues
for the terminal. If your terminal doesn't support font fallback and you need to have icons included in your font, you can patch it via [Font Patcher](https://github.com/ryanoasis/nerd-fonts#option-8-patch-your-own-font). 
There is a simple step by step guide [here](https://github.com/mortepau/codicons.nvim#how-to-patch-fonts).

## Configuration

nvim-dap-ui is built on the idea of "elements". These elements are windows
which provide different features.

Elements are grouped into layouts which can be placed on any side of the screen.
There can be any number of layouts, containing whichever elements desired.

Elements can also be displayed temporarily in a floating window.

Each element has a set of *mappings* for element-specific possible actions, detailed below for each element.
The total set of actions/mappings and their default shortcuts are:
- `edit`: `e`
- `expand`: `<CR>` or left click
- `open`: `o`
- `remove`: `d`
- `repl`: `r`
- `toggle`: `t`

See `:h dapui.setup()` for configuration options and defaults.


### Variable Scopes

![image](https://user-images.githubusercontent.com/24252670/126842891-c5175f13-5eb7-4d0a-9dae-620c4d31448a.png)

Element ID: `scopes`

Displays the available scopes and variables within them.

Mappings:

- `edit`: Edit the value of a variable
- `expand`: Toggle showing any children of variable.
- `repl`: Send variable to REPL

### Threads and Stack Frames

![image](https://user-images.githubusercontent.com/24252670/126843106-5dce09dc-49d0-4aaa-ba98-fd8f1
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

