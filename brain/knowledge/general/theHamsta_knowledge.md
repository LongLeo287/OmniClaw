---
id: thehamsta-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.948500
---

# KNOWLEDGE EXTRACT: theHamsta
> **Extracted on:** 2026-03-30 17:54:16
> **Source:** theHamsta

---

## File: `nvim-dap-virtual-text.md`
```markdown
# 📦 theHamsta/nvim-dap-virtual-text [🔖 PENDING/APPROVE]
🔗 https://github.com/theHamsta/nvim-dap-virtual-text


## Meta
- **Stars:** ⭐ 1063 | **Forks:** 🍴 34
- **Language:** Lua | **License:** GPL-3.0
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# nvim-dap-virtual-text

This plugin adds virtual text support to [nvim-dap](https://github.com/mfussenegger/nvim-dap).
[nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) is used to find variable definitions.

```vim
Plug 'mfussenegger/nvim-dap'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'theHamsta/nvim-dap-virtual-text'
```

> [!NOTE]
>
> With Neovim 0.9 and above, `nvim-treesitter` is not hard a dependency.
> This plugin only needs the parsers for the languages you want to use it with
> and `locals.scm` queries defining references and definitions of variables
> (typically provided by nvim-treesitter).

The hlgroup for the virtual text is `NvimDapVirtualText` (linked to `Comment`).
Exceptions that caused the debugger to stop are displayed as `NvimDapVirtualTextError`
(linked to `DiagnosticVirtualTextError`). Changed and new variables will be highlighted with
`NvimDapVirtualTextChanged` (default linked to `DiagnosticVirtualTextWarn`).

The behavior of this plugin can be activated and controlled via a `setup` call

```lua
require("nvim-dap-virtual-text").setup()
```

Wrap this call with `lua <<EOF` when you are using viml for your config:

```vim
lua <<EOF
require("nvim-dap-virtual-text").setup()
EOF
```

or with additional options:
```lua
require("nvim-dap-virtual-text").setup {
    enabled = true,                        -- enable this plugin (the default)
    enabled_commands = true,               -- create commands DapVirtualTextEnable, DapVirtualTextDisable, DapVirtualTextToggle, (DapVirtualTextForceRefresh for refreshing when debug adapter did not notify its termination)
    highlight_changed_variables = true,    -- highlight changed values with NvimDapVirtualTextChanged, else always NvimDapVirtualText
    highlight_new_as_changed = false,      -- highlight new variables in the same way as changed variables (if highlight_changed_variables)
    show_stop_reason = true,               -- show stop reason when stopped for exceptions
    commented = false,                     -- prefix virtual text with comment string
    only_first_definition = true,          -- only show virtual text at first definition (if there are multiple)
    all_references = false,                -- show virtual text on all all references of the variable (not only definitions)
    clear_on_continue = false,             -- clear virtual text on "continue" (might cause flickering when stepping)
    --- A callback that determines how a variable is displayed or whether it should be omitted
    --- @param variable Variable https://microsoft.github.io/debug-adapter-protocol/specification#Types_Variable
    --- @param buf number
    --- @param stackframe dap.StackFrame https://microsoft.github.io/debug-adapter-protocol/specification#Types_StackFrame
    --- @param node userdata tree-sitter node identified as variable definition of reference (see `:h tsnode`)
    --- @param options nvim_dap_virtual_text_options Current options for nvim-dap-
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

