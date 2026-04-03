---
id: github.com-hrsh7th-cmp-nvim-lsp-417e20a7-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:07.790600
---

# KNOWLEDGE EXTRACT: github.com_hrsh7th_cmp-nvim-lsp_417e20a7
> **Extracted on:** 2026-04-01 15:58:58
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524875/github.com_hrsh7th_cmp-nvim-lsp_417e20a7

---

## File: `.gitignore`
```
/doc/tags
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2021 hrsh7th

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
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

## File: `after/plugin/cmp_nvim_lsp.lua`
```
require('cmp_nvim_lsp').setup()
```

## File: `doc/cmp-nvim-lsp.txt`
```
*cmp-nvim-lsp*

==============================================================================
CONTENTS                                                 *cmp-nvim-lsp-contents*

FAQ                                                           |cmp-nvim-lsp-faq|



==============================================================================
FAQ                                                           *cmp-nvim-lsp-faq*

How to disable specific LSP server's cmpletion?~

  You can disable specific LSP server's cmpletion by adding the following

>
  require('lspconfig')[%YOUR_LSP_SERVER%].setup {
    on_attach = function(client)
      client.server_capabilities.completionProvider = false
    end
  }
<



==============================================================================
 vim:tw=78:ts=2:et:ft=help:norl:

```

## File: `lua/cmp_nvim_lsp/init.lua`
```
local source = require('cmp_nvim_lsp.source')

local M = {}

---Registered client and source mapping.
M.client_source_map = {}

---Setup cmp-nvim-lsp source.
M.setup = function()
  vim.api.nvim_create_autocmd('InsertEnter', {
    group = vim.api.nvim_create_augroup('cmp_nvim_lsp', { clear = true }),
    pattern = '*',
    callback = M._on_insert_enter
  })
end

local if_nil = function(val, default)
  if val == nil then return default end
  return val
end

-- Backported from vim.deprecate (0.9.0+)
local function deprecate(name, alternative, version, plugin, backtrace)
  local message = name .. ' is deprecated'
  plugin = plugin or 'Nvim'
  message = alternative and (message .. ', use ' .. alternative .. ' instead.') or message
  message = message
    .. ' See :h deprecated\nThis function will be removed in '
    .. plugin
    .. ' version '
    .. version
  if vim.notify_once(message, vim.log.levels.WARN) and backtrace ~= false then
    vim.notify(debug.traceback('', 2):sub(2), vim.log.levels.WARN)
  end
end

M.default_capabilities = function(override)
  override = override or {}

  return {
    textDocument = {
      completion = {
        dynamicRegistration = if_nil(override.dynamicRegistration, false),
        completionItem = {
          snippetSupport = if_nil(override.snippetSupport, true),
          commitCharactersSupport = if_nil(override.commitCharactersSupport, true),
          deprecatedSupport = if_nil(override.deprecatedSupport, true),
          preselectSupport = if_nil(override.preselectSupport, true),
          tagSupport = if_nil(override.tagSupport, {
            valueSet = {
              1, -- Deprecated
            }
          }),
          insertReplaceSupport = if_nil(override.insertReplaceSupport, true),
          resolveSupport = if_nil(override.resolveSupport, {
              properties = {
                  "documentation",
                  "additionalTextEdits",
                  "insertTextFormat",
                  "insertTextMode",
                  "command",
              },
          }),
          insertTextModeSupport = if_nil(override.insertTextModeSupport, {
            valueSet = {
              1, -- asIs
              2, -- adjustIndentation
            }
          }),
          labelDetailsSupport = if_nil(override.labelDetailsSupport, true),
        },
        contextSupport = if_nil(override.snippetSupport, true),
        insertTextMode = if_nil(override.insertTextMode, 1),
        completionList = if_nil(override.completionList, {
          itemDefaults = {
            'commitCharacters',
            'editRange',
            'insertTextFormat',
            'insertTextMode',
            'data',
          }
        })
      },
    },
  }
end

---Backwards compatibility
M.update_capabilities = function(_, override)
  local _deprecate = vim.deprecate or deprecate
  _deprecate('cmp_nvim_lsp.update_capabilities', 'cmp_nvim_lsp.default_capabilities', '1.0.0', 'cmp-nvim-lsp')
  return M.default_capabilities(override)
end


---Refresh sources on InsertEnter.
M._on_insert_enter = function()
  local cmp = require('cmp')

  local allowed_clients = {}

  local get_clients = (
    vim.lsp.get_clients ~= nil and vim.lsp.get_clients -- nvim 0.10+
    or vim.lsp.get_active_clients
  )

  -- register all active clients.
  for _, client in ipairs(get_clients()) do
    allowed_clients[client.id] = client
    if not M.client_source_map[client.id] then
      local s = source.new(client)
      if s:is_available() then
        M.client_source_map[client.id] = cmp.register_source('nvim_lsp', s)
      end
    end
  end

  -- register all buffer clients (early register before activation)
  for _, client in ipairs(get_clients({ bufnr = 0 })) do
    allowed_clients[client.id] = client
    if not M.client_source_map[client.id] then
      local s = source.new(client)
      if s:is_available() then
        M.client_source_map[client.id] = cmp.register_source('nvim_lsp', s)
      end
    end
  end

  -- unregister stopped/detached clients.
  for client_id, source_id in pairs(M.client_source_map) do
    if not allowed_clients[client_id] or allowed_clients[client_id]:is_stopped() then
      cmp.unregister_source(source_id)
      M.client_source_map[client_id] = nil
    end
  end
end

return M
```

## File: `lua/cmp_nvim_lsp/source.lua`
```
local source = {}

source.new = function(client)
  local self = setmetatable({}, { __index = source })
  self.client = client
  self.request_ids = {}
  return self
end

---Get debug name.
---@return string
source.get_debug_name = function(self)
  return table.concat({ 'nvim_lsp', self.client.name }, ':')
end

local is_nvim_11_or_newer = vim.fn.has('nvim-0.11') == 1

--- Calls a method on a client object in a way that is compatible with both
--- Neovim 0.10 and 0.11+, handling the dot vs. colon syntax change for methods.
---
--- @param method_name string The name of the method to call (e.g., 'request').
--- @param ... any Variable arguments to be passed to the target method.
--- @return any The return value(s) from the called method.
source._call_client_method = function(self, method_name, ...)
  local method_func = self.client[method_name]

  if is_nvim_11_or_newer then
    -- Nvim 0.11+ requires the colon (:) syntax to avoid deprecation warnings.
    -- The call `obj:method(...)` is syntactic sugar for `obj.method(obj, ...)`.
    -- We replicate this by calling the function and passing the object `obj`
    -- as the first argument, followed by the rest of the arguments.
    return method_func(self.client, ...)
  else
    -- Nvim 0.10 requires the dot (.) syntax for methods with arguments,
    -- because a wrapper already injects the 'self' parameter.
    -- We just call the function directly with its arguments.
    return method_func(...)
  end
end

---Return the source is available.
---@return boolean
source.is_available = function(self)
  -- client is stopped.
  if self:_call_client_method('is_stopped') then
    return false
  end

  -- client is not attached to current buffer.
  local bufnr = vim.api.nvim_get_current_buf()
  local get_clients = (
    vim.lsp.get_clients ~= nil and vim.lsp.get_clients -- nvim 0.10+
    or vim.lsp.get_active_clients
  )
  if vim.tbl_isempty(get_clients({ bufnr = bufnr, id = self.client.id })) then
    return false
  end

  -- client has no completion capability.
  if not self:_get(self.client.server_capabilities, { 'completionProvider' }) then
    return false
  end
  return true;
end

---Get LSP's PositionEncodingKind.
---@return lsp.PositionEncodingKind
source.get_position_encoding_kind = function(self)
  return self:_get(self.client.server_capabilities, { 'positionEncoding' }) or self.client.offset_encoding or 'utf-16'
end

---Get triggerCharacters.
---@return string[]
source.get_trigger_characters = function(self)
  return self:_get(self.client.server_capabilities, { 'completionProvider', 'triggerCharacters' }) or {}
end

---Get get_keyword_pattern.
---@param params cmp.SourceApiParams
---@return string
source.get_keyword_pattern = function(self, params)
  local option
  option = params.option or {}
  option = option[self.client.name] or {}
  return option.keyword_pattern or require('cmp').get_config().completion.keyword_pattern
end

---Resolve LSP CompletionItem.
---@param params cmp.SourceCompletionApiParams
---@param callback function
source.complete = function(self, params, callback)
  local lsp_params = vim.lsp.util.make_position_params(0, self.client.offset_encoding)
  lsp_params.context = {}
  lsp_params.context.triggerKind = params.completion_context.triggerKind
  lsp_params.context.triggerCharacter = params.completion_context.triggerCharacter
  self:_request('textDocument/completion', lsp_params, function(_, response)
    callback(response)
  end)
end

---Resolve LSP CompletionItem.
---@param completion_item lsp.CompletionItem
---@param callback function
source.resolve = function(self, completion_item, callback)
  -- client is stopped.
  if self:_call_client_method('is_stopped') then
    return callback()
  end

  -- client has no completion capability.
  if not self:_get(self.client.server_capabilities, { 'completionProvider', 'resolveProvider' }) then
    return callback()
  end

  self:_request('completionItem/resolve', completion_item, function(_, response)
    callback(response or completion_item)
  end)
end

---Execute LSP CompletionItem.
---@param completion_item lsp.CompletionItem
---@param callback function
source.execute = function(self, completion_item, callback)
  -- client is stopped.
  if self:_call_client_method('is_stopped') then
    return callback()
  end

  -- completion_item has no command.
  if not completion_item.command then
    return callback()
  end

  self:_request('workspace/executeCommand', completion_item.command, function(_, _)
    callback()
  end)
end

---Get object path.
---@param root table
---@param paths string[]
---@return any
source._get = function(_, root, paths)
  local c = root
  for _, path in ipairs(paths) do
    c = c[path]
    if not c then
      return nil
    end
  end
  return c
end

---Send request to nvim-lsp servers with backward compatibility.
---@param method string
---@param params table
---@param callback function
source._request = function(self, method, params, callback)
  if self.request_ids[method] ~= nil then
    self:_call_client_method('cancel_request', self.request_ids[method])
    self.request_ids[method] = nil
  end
  local _, request_id
  _, request_id = self:_call_client_method('request', method, params, function(arg1, arg2, arg3)
    if self.request_ids[method] ~= request_id then
      return
    end
    self.request_ids[method] = nil

    -- Text changed, retry
    if arg1 and arg1.code == -32801 then
      self:_request(method, params, callback)
      return
    end

    if method == arg2 then
      callback(arg1, arg3) -- old signature
    else
      callback(arg1, arg2) -- new signature
    end
  end)
  self.request_ids[method] = request_id
end

return source
```

