---
id: hrsh7th-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.801997
---

# KNOWLEDGE EXTRACT: hrsh7th
> **Extracted on:** 2026-03-30 17:38:08
> **Source:** hrsh7th

---

## File: `cmp-nvim-lsp.md`
```markdown
# 📦 hrsh7th/cmp-nvim-lsp [🔖 PENDING/APPROVE]
🔗 https://github.com/hrsh7th/cmp-nvim-lsp


## Meta
- **Stars:** ⭐ 1494 | **Forks:** 🍴 70
- **Language:** Lua | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
nvim-cmp source for neovim builtin LSP client

## README (trích đầu)
```
# cmp-nvim-lsp

nvim-cmp source for neovim's built-in language server client.

## Capabilities

Language servers provide different completion results depending on the capabilities of the client. Neovim's default omnifunc has basic support for serving completion candidates. nvim-cmp supports more types of completion candidates, so users must override the capabilities sent to the server such that it can provide these candidates during a completion request. These capabilities are provided via the helper function `require('cmp_nvim_lsp').default_capabilities`

As these candidates are sent on each request, **adding these capabilities will break the built-in omnifunc support for neovim's language server client**. `nvim-cmp` provides manually triggered completion that can replace omnifunc. See `:help cmp-faq` for more details.

## Setup

```lua

require'cmp'.setup {
  sources = {
    { name = 'nvim_lsp' }
  }
}

-- The nvim-cmp almost supports LSP's capabilities so You should advertise it to LSP servers..
local capabilities = require('cmp_nvim_lsp').default_capabilities()

-- An example for configuring `clangd` LSP to use nvim-cmp as a completion engine
require('lspconfig').clangd.setup {
  capabilities = capabilities,
  ...  -- other lspconfig configs
}
```

## Option

`[%LSPCONFIG-NAME%].keyword_pattern`

You can override keyword_pattern for specific language-server like this.

```lua
cmp.setup {
  ...
  sources = {
    {
      name = 'nvim_lsp',
      option = {
        php = {
          keyword_pattern = [=[[\%(\$\k*\)\|\k\+]]=],
        }
      }
    }
  }
  ...
}
```


## Readme!

1. There is a Github issue that documents [breaking changes](https://github.com/hrsh7th/cmp-nvim-lsp/issues/38) for cmp-nvim-lsp. Subscribe to the issue to be notified of upcoming breaking changes.
2. This is my hobby project. You can support me via GitHub sponsors.
3. Bug reports are welcome, but don't expect a fix unless you provide minimal configuration and steps to reproduce your issue.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `nvim-cmp.md`
```markdown
# 📦 hrsh7th/nvim-cmp [🔖 PENDING/APPROVE]
🔗 https://github.com/hrsh7th/nvim-cmp


## Meta
- **Stars:** ⭐ 9375 | **Forks:** 🍴 435
- **Language:** Lua | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A completion plugin for neovim coded in Lua.

## README (trích đầu)
```
# nvim-cmp

A completion engine plugin for neovim written in Lua.
Completion sources are installed from external repositories and "sourced".

https://github.com/hrsh7th/nvim-cmp/assets/22756295/afa70011-9121-4e42-aedd-0153b630eeab

Readme!
====================

1. There is a GitHub issue that documents [breaking changes](https://github.com/hrsh7th/nvim-cmp/issues/231) for nvim-cmp. Subscribe to the issue to be notified of upcoming breaking changes.
2. This is my hobby project. You can support me via GitHub sponsors.
3. Bug reports are welcome, but don't expect a fix unless you provide minimal configuration and steps to reproduce your issue.
4. The `cmp.mapping.preset.*` is pre-defined configuration that aims to mimic neovim's native like behavior. It can be changed without announcement. Please manage key-mapping by yourself.

Concept
====================

- Full support for LSP completion related capabilities
- Powerful customizability via Lua functions
- Smart handling of key mappings
- No flicker


Setup
====================

### Recommended Configuration

This example configuration uses `vim-plug` as the plugin manager and `vim-vsnip` as a snippet plugin.

```vim
call plug#begin(s:plug_dir)
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'
Plug 'hrsh7th/nvim-cmp'

" For vsnip users.
Plug 'hrsh7th/cmp-vsnip'
Plug 'hrsh7th/vim-vsnip'

" For luasnip users.
" Plug 'L3MON4D3/LuaSnip'
" Plug 'saadparwaiz1/cmp_luasnip'

" For mini.snippets users.
" Plug 'echasnovski/mini.snippets'
" Plug 'abeldekat/cmp-mini-snippets'

" For ultisnips users.
" Plug 'SirVer/ultisnips'
" Plug 'quangnguyen30192/cmp-nvim-ultisnips'

" For snippy users.
" Plug 'dcampos/nvim-snippy'
" Plug 'dcampos/cmp-snippy'

call plug#end()

lua <<EOF
  -- Set up nvim-cmp.
  local cmp = require'cmp'

  cmp.setup({
    snippet = {
      -- REQUIRED - you must specify a snippet engine
      expand = function(args)
        vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
        -- require('luasnip').lsp_expand(args.body) -- For `luasnip` users.
        -- require('snippy').expand_snippet(args.body) -- For `snippy` users.
        -- vim.fn["UltiSnips#Anon"](args.body) -- For `ultisnips` users.
        -- vim.snippet.expand(args.body) -- For native neovim snippets (Neovim v0.10+)

        -- For `mini.snippets` users:
        -- local insert = MiniSnippets.config.expand.insert or MiniSnippets.default_insert
        -- insert({ body = args.body }) -- Insert at cursor
        -- cmp.resubscribe({ "TextChangedI", "TextChangedP" })
        -- require("cmp.config").set_onetime({ sources = {} })
      end,
    },
    window = {
      -- completion = cmp.config.window.bordered(),
      -- documentation = cmp.config.window.bordered(),
    },
    mapping = cmp.mapping.preset.insert({
      ['<C-b>'] = cmp.mapping.scroll_docs(-4),
      ['<C-f>'] = cmp.mapping.scroll_docs(4),
      ['<C-Space>'] = cmp.mapping
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

