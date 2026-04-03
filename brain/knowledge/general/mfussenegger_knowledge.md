---
id: mfussenegger-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.767868
---

# KNOWLEDGE EXTRACT: mfussenegger
> **Extracted on:** 2026-03-30 17:42:48
> **Source:** mfussenegger

---

## File: `nvim-dap.md`
```markdown
# 📦 mfussenegger/nvim-dap [🔖 PENDING/APPROVE]
🔗 https://github.com/mfussenegger/nvim-dap
🌐 https://codeberg.org/mfussenegger/nvim-dap

## Meta
- **Stars:** ⭐ 7022 | **Forks:** 🍴 255
- **Language:** Lua | **License:** GPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Debug Adapter Protocol client implementation for Neovim

## README (trích đầu)
```
# DAP (Debug Adapter Protocol)

`nvim-dap` is a Debug Adapter Protocol client implementation for [Neovim][1].
`nvim-dap` allows you to:

- Launch an application to debug
- Attach to running applications and debug them
- Set breakpoints and step through code
- Inspect the state of the application

![demo][demo]

## Installation

[![LuaRocks](https://img.shields.io/luarocks/v/mfussenegger/nvim-dap?logo=lua&color=purple)](https://luarocks.org/modules/mfussenegger/nvim-dap)

- Install nvim-dap like any other Neovim plugin:
  - `git clone https://codeberg.org/mfussenegger/nvim-dap.git ~/.config/nvim/pack/plugins/start/nvim-dap`
  - Or with [vim-plug][11]: `Plug 'mfussenegger/nvim-dap'`
  - Or with [packer.nvim][12]: `use 'mfussenegger/nvim-dap'`
- Generate the documentation for nvim-dap using `:helptags ALL` or
  `:helptags <PATH-TO-PLUGIN/doc/>`

Supported Neovim versions:

- Latest nightly
- 0.11.x (Recommended)
- 0.10.4

You'll need to install and configure a debug adapter per language. See

- [:help dap.txt](doc/dap.txt)
- the [Debug-Adapter Installation][5] wiki
- `:help dap-adapter`
- `:help dap-configuration`

## Usage

A typical debug flow consists of:

- Setting breakpoints via `:DapToggleBreakpoint` or `:lua
  require'dap'.toggle_breakpoint()`.
- Launching debug sessions and resuming execution via `:DapNew` and
  `:DapContinue` or `:lua require'dap'.continue()`.
- Stepping through code via `:DapStepOver`, `:DapStepInto` or the corresponding
  functions `:lua require'dap'.step_over()` and `:lua
  require'dap'.step_into()`.
- Inspecting the state:
  - Via the built-in REPL: `:lua require'dap'.repl.open()`
    - Try typing an expression followed by ENTER to evaluate it.
    - Try commands like `.help`, `.frames`, `.threads`.
    - Variables with structure can be expanded and collapsed with ENTER on the
      corresponding line.
  - Via the widget UI (`:help dap-widgets`). Typically you'd inspect values,
    threads, stacktrace ad-hoc when needed instead of showing the information
    all the time, but you can also create sidebars for a permanent display
  - Via UI extensions:
    - IDE like: [nvim-dap-ui][15]
    - Middle ground between the IDE like nvim-dap-ui and the built-in widgets: [nvim-dap-view][nvim-dap-view]
    - Show inline values: [nvim-dap-virtual-text][7]

See [:help dap.txt](doc/dap.txt), `:help dap-mapping` and `:help dap-api`.

**Tip:**

The arrow keys are good candidates for keymaps to step through code as their
direction resembles the direction you'll step to.

- Down: Step over
- Right: Step into
- Left: Step out
- Up: Restart frame

You can setup keymaps temporary during a debug session using event listeners.
See `:help dap-listeners`.

## Supported languages

In theory all of the languages for which a debug adapter exists should be
supported.

- [Available debug adapters][13]
- [nvim-dap Debug-Adapter Installation & Configuration][5]

The Wiki is community maintained. If you got an adapter working that isn't
listed yet, pl
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

