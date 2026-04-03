---
id: github.com-wbthomason-packer.nvim-5f36edee-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:43.557414
---

# KNOWLEDGE EXTRACT: github.com_wbthomason_packer.nvim_5f36edee
> **Extracted on:** 2026-04-01 12:27:50
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521832/github.com_wbthomason_packer.nvim_5f36edee

---

## File: `.gitignore`
```
# Compiled Lua sources
luac.out

# luarocks build files
*.src.rock
*.zip
*.tar.gz

# Object files
*.o
*.os
*.ko
*.obj
*.elf

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo
*.def
*.exp

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Vim swap files
*.swp

doc/tags
```

## File: `.lua-format`
```
align_args: true
align_parameter: true
align_table_field: true
break_after_functioncall_lp: false
break_after_functiondef_lp: false
break_after_operator: false 
break_after_table_lb: true
break_before_functioncall_rp: true
break_before_functiondef_rp: true
break_before_table_rb: true
chop_down_kv_table: true
chop_down_parameter: true
chop_down_table: false
column_limit: 100
column_table_limit: 100
continuation_indent_width: 2
double_quote_to_single_quote: false
extra_sep_at_table_end: false
indent_width: 2
keep_simple_control_block_one_line: true
keep_simple_function_one_line: true
single_quote_to_double_quote: false
spaces_before_call: 1
tab_width: 2
table_sep: ','
use_tab: false
```

## File: `Dockerfile`
```
FROM archlinux:base-devel
WORKDIR /setup
RUN pacman -Sy git neovim python --noconfirm
RUN useradd -m test

USER test
RUN git clone --depth 1 https://github.com/nvim-lua/plenary.nvim ~/.local/share/nvim/site/pack/vendor/start/plenary.nvim
RUN mkdir -p /home/test/.cache/nvim/packer.nvim
RUN touch /home/test/.cache/nvim/packer.nvim/test_completion{,1,2,3}

USER test
RUN mkdir -p /home/test/.local/share/nvim/site/pack/packer/start/packer.nvim/
WORKDIR /home/test/.local/share/nvim/site/pack/packer/start/packer.nvim/
COPY . ./

USER root
RUN chmod 777 -R /home/test/.local/share/nvim/site/pack/packer/start/packer.nvim
RUN touch /home/test/.cache/nvim/packer.nvim/not_writeable

USER test
ENTRYPOINT make test
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2017 Wil Thomason

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

## File: `Makefile`
```
test:
	nvim --headless --noplugin -u tests/minimal.vim -c "PlenaryBustedDirectory tests/ { minimal_init = './tests/minimal.vim' }"
run:
	docker build . -t neovim-stable:latest && docker run --rm -it --entrypoint bash neovim-stable:latest
run-test:
	docker build . -t neovim-stable:latest && docker run --rm neovim-stable:latest
```

## File: `README.md`
```markdown
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
git clone https://github.com/wbthomason/packer.nvim "$env:LOCALAPPDATA\nvim-data\site\pack\packer\start\packer.nvim"
```

Then you can write your plugin specification in Lua, e.g. (in `~/.config/nvim/lua/plugins.lua`):

```lua
-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'

  -- Simple plugins can be specified as strings
  use 'rstacruz/vim-closer'

  -- Lazy loading:
  -- Load on specific commands
  use {'tpope/vim-dispatch', opt = true, cmd = {'Dispatch', 'Make', 'Focus', 'Start'}}

  -- Load on an autocommand event
  use {'andymass/vim-matchup', event = 'VimEnter'}

  -- Load on a combination of conditions: specific filetypes or commands
  -- Also run code after load (see the "config" key)
  use {
    'w0rp/ale',
    ft = {'sh', 'zsh', 'bash', 'c', 'cpp', 'cmake', 'html', 'markdown', 'racket', 'vim', 'tex'},
    cmd = 'ALEEnable',
    config = 'vim.cmd[[ALEEnable]]'
  }

  -- Plugins can have dependencies on other plugins
  use {
    'haorenW1025/completion-nvim',
    opt = true,
    requires = {{'hrsh7th/vim-vsnip', opt = true}, {'hrsh7th/vim-vsnip-integ', opt = true}}
  }

  -- Plugins can also depend on rocks from luarocks.org:
  use {
    'my/supercoolplugin',
    rocks = {'lpeg', {'lua-cjson', version = '2.1.0'}}
  }

  -- You can specify rocks in isolation
  use_rocks 'penlight'
  use_rocks {'lua-resty-http', 'lpeg'}

  -- Local plugins can be included
  use '~/projects/personal/hover.nvim'

  -- Plugins can have post-install/update hooks
  use {'iamcco/markdown-preview.nvim', run = 'cd app && yarn install', cmd = 'MarkdownPreview'}

  -- Post-install/update hook with neovim command
  use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }

  -- Post-install/update hook with call of vimscript function with argument
  use { 'glacambre/firenvim', run = function() vim.fn['firenvim#install'](0) end }

  -- Use specific branch, dependency and run lua file after load
  use {
    'glepnir/galaxyline.nvim', branch = 'main', config = function() require'statusline' end,
    requires = {'kyazdani42/nvim-web-devicons'}
  }

  -- Use dependency and run lua function after load
  use {
    'lewis6991/gitsigns.nvim', requires = { 'nvim-lua/plenary.nvim' },
    config = function() require('gitsigns').setup() end
  }

  -- You can specify multiple plugins in a single call
  use {'tjdevries/colorbuddy.vim', {'nvim-treesitter/nvim-treesitter', opt = true}}

  -- You can alias plugin names
  use {'dracula/vim', as = 'dracula'}
end)
```

Note that if you get linter complaints about `use` being an undefined global, these errors are
spurious - `packer` injects `use` into the scope of the function passed to `startup`.
If these errors bother you, the easiest fix is to simply specify `use` as an argument to the
function you pass to `startup`, e.g.
```lua
packer.startup(function(use)
...your config...
end)
```

`packer` provides the following commands after you've run and configured `packer` with `require('packer').startup(...)`:

```
-- You must run this or `PackerSync` whenever you make changes to your plugin configuration
-- Regenerate compiled loader file
:PackerCompile

-- Remove any disabled or unused plugins
:PackerClean

-- Clean, then install missing plugins
:PackerInstall

-- Clean, then update and install plugins
-- supports the `--preview` flag as an optional first argument to preview updates
:PackerUpdate

-- Perform `PackerUpdate` and then `PackerCompile`
-- supports the `--preview` flag as an optional first argument to preview updates
:PackerSync

-- Show list of installed plugins
:PackerStatus

-- Loads opt plugin immediately
:PackerLoad completion-nvim ale
```

You can configure Neovim to automatically run `:PackerCompile` whenever `plugins.lua` is updated with
[an autocommand](https://neovim.io/doc/user/autocmd.html#:autocmd):

```
augroup packer_user_config
  autocmd!
  autocmd BufWritePost plugins.lua source <afile> | PackerCompile
augroup end
```

This autocommand can be placed in your `init.vim`, or any other startup file as per your setup.
Placing this in `plugins.lua` could look like this:

```lua
vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerCompile
  augroup end
]])
```

## Bootstrapping

If you want to automatically install and set up `packer.nvim` on any machine you clone your configuration to,
add the following snippet (which is due to @Iron-E and @khuedoan) somewhere in your config **before** your first usage of `packer`:

```lua
local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'
  -- My plugins here
  -- use 'foo1/bar1.nvim'
  -- use 'foo2/bar2.nvim'

  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if packer_bootstrap then
    require('packer').sync()
  end
end)
```

You can also use the following command (with `packer` bootstrapped) to have `packer` setup your
configuration (or simply run updates) and close once all operations are completed:

```sh
$ nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'
```

## Usage

The above snippets give some examples of `packer` features and use. Examples include:

- My dotfiles:
  - [Specification file](https://github.com/wbthomason/dotfiles/blob/linux/neovim/.config/nvim/lua/plugins.lua)
  - [Loading file](https://github.com/wbthomason/dotfiles/blob/linux/neovim/.config/nvim/lua/plugins.lua)
  - [Generated lazy-loader file](https://github.com/wbthomason/dotfiles/blob/linux/neovim/.config/nvim/plugin/packer_compiled.lua)
- An example using the `startup` method: [tjdevries](https://github.com/tjdevries/config_manager/blob/master/xdg_config/nvim/lua/tj/plugins.lua)
    - Using this method, you do not require a "loading" file. You can simply `lua require('plugins')` from your `init.vim`

The following is a more in-depth explanation of `packer`'s features and use.

### The `startup` function
`packer` provides `packer.startup(spec)`, which is used in the above examples.

`startup` is a convenience function for simple setup and can be invoked as follows:
- `spec` can be a function: `packer.startup(function() use 'tjdevries/colorbuddy.vim' end)`
- `spec` can be a table with a function as its first element and config overrides as another element:
  `packer.startup({function() use 'tjdevries/colorbuddy.vim' end, config = { ... }})`
- `spec` can be a table with a table of plugin specifications as its first element, config overrides as another element, and optional rock specifications as another element:
 `packer.startup({{'tjdevries/colorbuddy.vim'}, config = { ... }, rocks = { ... }})`

### Custom Initialization
You are not required to use `packer.startup` if you prefer a more manual setup with finer control
over configuration and loading.

To take this approach, load `packer` like any other Lua module. You must call `packer.init()` before
performing any operations; it is recommended to call `packer.reset()` if you may be re-running your
specification code (e.g. by sourcing your plugin specification file with `luafile`).

You may pass a table of configuration values to `packer.init()` to customize its operation. The
default configuration values (and structure of the configuration table) are:
```lua
local packer = require('packer')
packer.util = require('packer.util')

packer.init({
  ensure_dependencies = true, -- Should packer install plugin dependencies?
  snapshot = nil, -- Name of the snapshot you would like to load at startup
  snapshot_path = packer.util.join_paths(vim.fn.stdpath('cache'), 'packer.nvim'), -- Default save directory for snapshots
  package_root  = packer.util.join_paths(vim.fn.stdpath('data'), 'site', 'pack'),
  compile_path  = packer.util.join_paths(vim.fn.stdpath('config'), 'plugin', 'packer_compiled.lua'),
  plugin_package = 'packer', -- The default package for plugins
  max_jobs = nil, -- Limit the number of simultaneous jobs. nil means no limit
  auto_clean = true, -- During sync(), remove unused plugins
  compile_on_sync = true, -- During sync(), run packer.compile()
  disable_commands = false, -- Disable creating commands
  opt_default = false, -- Default to using opt (as opposed to start) plugins
  transitive_opt = true, -- Make dependencies of opt plugins also opt by default
  transitive_disable = true, -- Automatically disable dependencies of disabled plugins
  auto_reload_compiled = true, -- Automatically reload the compiled file after creating it.
  preview_updates = false, -- If true, always preview updates before choosing which plugins to update, same as `PackerUpdate --preview`.
  git = {
    cmd = 'git', -- The base command for git operations
    subcommands = { -- Format strings for git subcommands
      update         = 'pull --ff-only --progress --rebase=false --force',
      install        = 'clone --depth %i --no-single-branch --progress',
      fetch          = 'fetch --depth 999999 --progress --force',
      checkout       = 'checkout %s --',
      update_branch  = 'merge --ff-only @{u}',
      current_branch = 'branch --show-current',
      diff           = 'log --color=never --pretty=format:FMT --no-show-signature HEAD@{1}...HEAD',
      diff_fmt       = '%%h %%s (%%cr)',
      get_rev        = 'rev-parse --short HEAD',
      get_msg        = 'log --color=never --pretty=format:FMT --no-show-signature HEAD -n 1',
      submodules     = 'submodule update --init --recursive --progress'
    },
    depth = 1, -- Git clone depth
    clone_timeout = 60, -- Timeout, in seconds, for git clones
    default_url_format = 'https://github.com/%s' -- Lua format string used for "aaa/bbb" style plugins
  },
  display = {
    non_interactive = false, -- If true, disable display windows for all operations
    compact = false, -- If true, fold updates results by default
    open_fn  = nil, -- An optional function to open a window for packer's display
    open_cmd = '65vnew \\[packer\\]', -- An optional command to open a window for packer's display
    working_sym = '⟳', -- The symbol for a plugin being installed/updated
    error_sym = '✗', -- The symbol for a plugin with an error in installation/updating
    done_sym = '✓', -- The symbol for a plugin which has completed installation/updating
    removed_sym = '-', -- The symbol for an unused plugin which was removed
    moved_sym = '→', -- The symbol for a plugin which was moved (e.g. from opt to start)
    header_sym = '━', -- The symbol for the header line in packer's display
    show_all_info = true, -- Should packer show all update details automatically?
    prompt_border = 'double', -- Border style of prompt popups.
    keybindings = { -- Keybindings for the display window
      quit = 'q',
      toggle_update = 'u', -- only in preview
      continue = 'c', -- only in preview
      toggle_info = '<CR>',
      diff = 'd',
      prompt_revert = 'r',
    }
  },
  luarocks = {
    python_cmd = 'python' -- Set the python command to use for running hererocks
  },
  log = { level = 'warn' }, -- The default print log level. One of: "trace", "debug", "info", "warn", "error", "fatal".
  profile = {
    enable = false,
    threshold = 1, -- integer in milliseconds, plugins which load faster than this won't be shown in profile output
  },
  autoremove = false, -- Remove disabled or unused plugins without prompting the user
})
```

### Specifying plugins

`packer` is based around declarative specification of plugins. You can declare a plugin using the
function `packer.use`, which I highly recommend locally binding to `use` for conciseness.

`use` takes either a string or a table. If a string is provided, it is treated as a plugin location
for a non-optional plugin with no additional configuration. Plugin locations may be specified as

1. Absolute paths to a local plugin
2. Full URLs (treated as plugins managed with `git`)
3. `username/repo` paths (treated as Github `git` plugins)

A table given to `use` can take two forms:

1. A list of plugin specifications (strings or tables)
2. A table specifying a single plugin. It must have a plugin location string as its first element,
   and may additionally have a number of optional keyword elements, shown below:
```lua
use {
  'myusername/example',        -- The plugin location string
  -- The following keys are all optional
  disable = boolean,           -- Mark a plugin as inactive
  as = string,                 -- Specifies an alias under which to install the plugin
  installer = function,        -- Specifies custom installer. See "custom installers" below.
  updater = function,          -- Specifies custom updater. See "custom installers" below.
  after = string or list,      -- Specifies plugins to load before this plugin. See "sequencing" below
  rtp = string,                -- Specifies a subdirectory of the plugin to add to runtimepath.
  opt = boolean,               -- Manually marks a plugin as optional.
  bufread = boolean,           -- Manually specifying if a plugin needs BufRead after being loaded
  branch = string,             -- Specifies a git branch to use
  tag = string,                -- Specifies a git tag to use. Supports '*' for "latest tag"
  commit = string,             -- Specifies a git commit to use
  lock = boolean,              -- Skip updating this plugin in updates/syncs. Still cleans.
  run = string, function, or table, -- Post-update/install hook. See "update/install hooks".
  requires = string or list,   -- Specifies plugin dependencies. See "dependencies".
  rocks = string or list,      -- Specifies Luarocks dependencies for the plugin
  config = string or function, -- Specifies code to run after this plugin is loaded.
  -- The setup key implies opt = true
  setup = string or function,  -- Specifies code to run before this plugin is loaded. The code is ran even if
                               -- the plugin is waiting for other conditions (ft, cond...) to be met.
  -- The following keys all imply lazy-loading and imply opt = true
  cmd = string or list,        -- Specifies commands which load this plugin. Can be an autocmd pattern.
  ft = string or list,         -- Specifies filetypes which load this plugin.
  keys = string or list,       -- Specifies maps which load this plugin. See "Keybindings".
  event = string or list,      -- Specifies autocommand events which load this plugin.
  fn = string or list          -- Specifies functions which load this plugin.
  cond = string, function, or list of strings/functions,   -- Specifies a conditional test to load this plugin
  module = string or list      -- Specifies Lua module names for require. When requiring a string which starts
                               -- with one of these module names, the plugin will be loaded.
  module_pattern = string/list -- Specifies Lua pattern of Lua module names for require. When
                               -- requiring a string which matches one of these patterns, the plugin will be loaded.
}
```

For the `cmd` option, the command may be a full command, or an autocommand pattern. If the command contains any
non-alphanumeric characters, it is assumed to be a pattern, and instead of creating a stub command, it creates
a CmdUndefined autocmd to load the plugin when a command that matches the pattern is invoked.

#### Checking plugin statuses
You can check whether or not a particular plugin is installed with `packer` as well as if that plugin is loaded.
To do this you can check for the plugin's name in the `packer_plugins` global table.
Plugins in this table are saved using only the last section of their names
e.g. `tpope/vim-fugitive` if installed will be under the key `vim-fugitive`.

```lua
if packer_plugins["vim-fugitive"] and packer_plugins["vim-fugitive"].loaded then
print("Vim fugitive is loaded")
-- other custom logic
end
```
**NOTE:** this table is only available *after* `packer_compiled.vim` is loaded so cannot be used till *after* plugins
have been loaded.

#### Luarocks support

You may specify that a plugin requires one or more Luarocks packages using the `rocks` key. This key
takes either a string specifying the name of a package (e.g. `rocks=lpeg`), or a list specifying one or more packages.
Entries in the list may either be strings, a list of strings or a table --- the latter case is used to specify arguments such as the
particular version of a package.
all supported luarocks keys are allowed except: `tree` and `local`. Environment variables for the luarocks command can also be
specified using the `env` key which takes a table as the value as shown below.
```lua
rocks = {'lpeg', {'lua-cjson', version = '2.1.0'}}
use_rocks {'lua-cjson', 'lua-resty-http'}
use_rocks {'luaformatter', server = 'https://luarocks.org/dev'}
use_rocks {'openssl' env = {OPENSSL_DIR = "/path/to/dir"}}
```

Currently, `packer` only supports equality constraints on package versions.

`packer` also provides the function `packer.luarocks.install_commands()`, which creates the
`PackerRocks <cmd> <packages...>` command. `<cmd>` must be one of "install" or "remove";
`<packages...>` is one or more package names (currently, version restrictions are not supported with
this command). Running `PackerRocks` will install or remove the given packages. You can use this
command even if you don't use `packer` to manage your plugins. However, please note that (1)
packages installed through `PackerRocks` **will** be removed by calls to `packer.luarocks.clean()`
(unless they are also part of a `packer` plugin specification), and (2) you will need to manually
invoke `packer.luarocks.setup_paths` (or otherwise modify your `package.path`) to ensure that Neovim
can find the installed packages.

Finally, `packer` provides the function `packer.use_rocks`, which takes a string or table specifying
one or more Luarocks packages as in the `rocks` key. You can use this to ensure that `packer`
downloads and manages some rocks which you want to use, but which are not associated with any
particular plugin.

#### Custom installers

You may specify a custom installer & updater for a plugin using the `installer` and `updater` keys.
Note that either both or none of these keys are required. These keys should be functions which take
as an argument a `display` object (from `lua/packer/display.lua`) and return an async function (per
`lua/packer/async.lua`) which (respectively) installs/updates the given plugin.

Providing the `installer`/`updater` keys overrides plugin type detection, but you still need to
provide a location string for the name of the plugin.

#### Update/install hooks

You may specify operations to be run after successful installs/updates of a plugin with the `run`
key. This key may either be a Lua function, which will be called with the `plugin` table for this
plugin (containing the information passed to `use` as well as output from the installation/update
commands, the installation path of the plugin, etc.), a string, or a table of functions and strings.

If an element of `run` is a string, then either:

1. If the first character of `run` is ":", it is treated as a Neovim command and executed.
2. Otherwise, `run` is treated as a shell command and run in the installation directory of the
   plugin via `$SHELL -c '<run>'`.

#### Dependencies

Plugins may specify dependencies via the `requires` key. This key can be a string or a list (table).

If `requires` is a string, it is treated as specifying a single plugin. If a plugin with the name
given in `requires` is already known in the managed set, nothing happens. Otherwise, the string is
treated as a plugin location string and the corresponding plugin is added to the managed set.

If `requires` is a list, it is treated as a list of plugin specifications following the format given
above.

If `ensure_dependencies` is true, the plugins specified in `requires` will be installed.

Plugins specified in `requires` are removed when no active plugins require them.

#### Sequencing

You may specify a loading order for plugins using the `after` key. This key can be a string or a
list (table).

If `after` is a string, it must be the name of another plugin managed by `packer` (e.g. the final segment of a plugin's path - for a Github plugin `FooBar/Baz`, the name would be just `Baz`). If `after` is a table, it must be a list of plugin names. If a plugin has an alias (i.e. uses the `as` key), this alias is its name.

The set of plugins specified in a plugin's `after` key must **all** be loaded before the plugin
using `after` will be loaded. For example, in the specification
```lua
  use {'FooBar/Baz', ft = 'bax'}
  use {'Something/Else', after = 'Baz'}
```
the plugin `Else` will only be loaded after the plugin `Baz`, which itself is only loaded for files
with `bax` filetype.

#### Keybindings

Plugins may be lazy-loaded on the use of keybindings/maps. Individual keybindings are specified either as a string (in which case they are treated as normal mode maps) or a table in the format `{mode, map}`.

### Performing plugin management operations
`packer` exposes the following functions for common plugin management operations. In all of the
below, `plugins` is an optional table of plugin names; if not provided, the default is "all managed
plugins":

- `packer.install(plugins)`: Install the specified plugins if they are not already installed
- `packer.update(plugins)`: Update the specified plugins, installing any that are missing
- `packer.update(opts, plugins)`: First argument can be a table specifying options, such as `{preview_updates = true}` to preview potential changes before updating (same as `PackerUpdate --preview`).
- `packer.clean()`: Remove any disabled or no longer managed plugins
- `packer.sync(plugins)`: Perform a `clean` followed by an `update`.
- `packer.sync(opts, plugins)`: Can take same optional options as `update`.
- `packer.compile(path)`: Compile lazy-loader code and save to `path`.
- `packer.snapshot(snapshot_name, ...)`: Creates a snapshot file that will live under `config.snapshot_path/<snapshot_name>`. If `snapshot_name` is an absolute path, then that will be the location where the snapshot will be taken. Optionally, a list of plugins name can be provided to selectively choose the plugins to snapshot.
- `packer.rollback(snapshot_name, ...)`: Rollback plugins status a snapshot file that will live under `config.snapshot_path/<snapshot_name>`. If `snapshot_name` is an absolute path, then that will be the location where the snapshot will be taken. Optionally, a list of plugins name can be provided to selectively choose which plugins to revert.
- `packer.delete(snapshot_name)`: Deletes a snapshot file under `config.snapshot_path/<snapshot_name>`. If `snapshot_name` is an absolute path, then that will be the location where the snapshot will be deleted.

### Extending `packer`
You can add custom key handlers to `packer` by calling `packer.set_handler(name, func)` where `name`
is the key you wish to handle and `func` is a function with the signature `func(plugins, plugin,
value)` where `plugins` is the global table of managed plugins, `plugin` is the table for a specific
plugin, and `value` is the value associated with key `name` in `plugin`.

### Compiling Lazy-Loaders
To optimize startup time, `packer.nvim` compiles code to perform the lazy-loading operations you
specify. This means that you do not need to load `packer.nvim` unless you want to perform some
plugin management operations.

To generate the compiled code, call `packer.compile(path)`, where `path` is some file path on your
`runtimepath`, with a `.vim` extension. This will generate a blend of Lua and Vimscript to load and
configure all your lazy-loaded plugins (e.g. generating commands, autocommands, etc.) and save it to
`path`. Then, when you start vim, the file at `path` is loaded (because `path` must be on your
`runtimepath`), and lazy-loading works.

If `path` is not provided to `packer.compile`, the output file will default to the value of
`config.compile_path`.

The option `compile_on_sync`, which defaults to `true`, will run `packer.compile()` during
`packer.sync()`, if set to `true`. Note that otherwise, you **must** run `packer.compile` yourself
to generate the lazy-loader file!

**NOTE:** If you use a function value for `config` or `setup` keys in any plugin specifications, it
**must not** have any upvalues (i.e. captures). We currently use Lua's `string.dump` to compile
config/setup functions to bytecode, which has this limitation.
Additionally, if functions are given for these keys, the functions will be passed the plugin
name and information table as arguments.

### User autocommands
`packer` runs most of its operations asyncronously. If you would like to implement automations that
require knowing when the operations are complete, you can use the following `User` autocmds (see
`:help User` for more info on how to use):

- `PackerComplete`: Fires after install, update, clean, and sync asynchronous operations finish.
- `PackerCompileDone`: Fires after compiling (see [the section on compilation](#compiling-lazy-loaders))

### Using a floating window
You can configure Packer to use a floating window for command outputs by passing a utility
function to `packer`'s config:
```lua
packer.startup({function()
  -- Your plugins here
end,
config = {
  display = {
    open_fn = require('packer.util').float,
  }
}})
```

By default, this floating window will show doubled borders. If you want to customize the window
appearance, you can pass a configuration to `float`, which is the same configuration that would be
passed to `nvim_open_win`:
```lua
packer.startup({function()
  -- Your plugins here
end,
config = {
  display = {
    open_fn = function()
      return require('packer.util').float({ border = 'single' })
    end
  }
}})
```

## Profiling
Packer has built in functionality that can allow you to profile the time taken loading your plugins.
In order to use this functionality you must either enable profiling in your config, or pass in an argument
when running packer compile.

#### Setup via config
```lua
config = {
  profile = {
    enable = true,
    threshold = 1 -- the amount in ms that a plugin's load time must be over for it to be included in the profile
  }
}
```

#### Using the packer compile command
```vim
:PackerCompile profile=true
" or
:PackerCompile profile=false
```

#### Profiling usage
This will rebuild your `packer_compiled.vim` with profiling code included. In order to visualise the output of the profile
restart your neovim and run `PackerProfile`. This will open a window with the output of your profiling.

## Debugging
`packer.nvim` logs to `stdpath(cache)/packer.nvim.log`. Looking at this file is usually a good start
if something isn't working as expected.

## Compatibility and known issues

- **2021-07-31:** If you're on macOS, note that building Neovim with the version of `luv` from `homebrew` [will cause any `packer` command to crash](https://github.com/wbthomason/packer.nvim/issues/496#issuecomment-890371022). More about this issue at [neovim/neovim#15054](https://github.com/neovim/neovim/issues/15054).
- **2021-07-28:** `packer` will now highlight commits/plugin names with potentially breaking changes
  (determined by looking for `breaking change` or `breaking_change`, case insensitive, in the update
  commit bodies and headers) as `WarningMsg` in the status window.
- **2021-06-06**: Your Neovim must include https://github.com/neovim/neovim/pull/14659; `packer` uses the `noautocmd` key.
- **2021-04-19**: `packer` now provides built-in profiling for your config via the `packer_compiled`
  file. Take a look at [the docs](#profiling) for more information!
- **2021-02-18**: Having trouble with Luarocks on macOS? See [this issue](https://github.com/wbthomason/packer.nvim/issues/180).
- **2021-01-19**: Basic Luarocks support has landed! Use the `rocks` key with a string or table to specify packages to install.
- **2020-12-10**: The `disable_commands` configuration flag now affects non-`startup` use as well. This means that, by default, `packer` will create commands for basic operations for you.
- **2020-11-13**: There is now a default implementation for a floating window `open_fn` in `packer.util`.
- **2020-09-04:** Due to changes to the Neovim `extmark` api (see: https://github.com/neovim/neovim/commit/3853276d9cacc99a2698117e904475dbf7033383), users will need to update to a version of Neovim **after** the aforementioned PR was merged. There are currently shims around the changed functions which should maintain support for earlier versions of Neovim, but these are intended to be temporary and will be removed by **2020-10-04**. Therefore Packer will not work with Neovim v0.4.4, which was released before the `extmark` change.

## Contributors
Many thanks to those who have contributed to the project! PRs and issues are always welcome. This
list is infrequently updated; please feel free to bug me if you're not listed here and you would
like to be.

- [@akinsho](https://github.com/akinsho)
- [@nanotee](https://github.com/nanotee)
- [@weilbith](https://github.com/weilbith)
- [@Iron-E](https://github.com/Iron-E)
- [@tjdevries](https://github.com/tjdevries)
- [@numToStr](https://github.com/numToStr)
- [@fsouza](https://github.com/fsouza)
- [@gbrlsnchs](https://github.com/gbrlsnchs)
- [@lewis6991](https://github.com/lewis6991)
- [@TimUntersberger](https://github.com/TimUntersberger)
- [@bfredl](https://github.com/bfredl)
- [@sunjon](https://github.com/sunjon)
- [@gwerbin](https://github.com/gwerbin)
- [@shadmansaleh](https://github.com/shadmansaleh)
- [@ur4ltz](https://github.com/ur4ltz)
- [@EdenEast](https://github.com/EdenEast)
- [@khuedoan](https://github.com/khuedoan)
- [@kevinhwang91](https://github.com/kevinhwang91)
- [@runiq](https://github.com/runiq)
- [@n3wborn](https://github.com/n3wborn)
- [@deathlyfrantic](https://github.com/deathlyfrantic)
- [@doctoromer](https://github.com/doctoromer)
- [@elianiva](https://github.com/elianiva)
- [@dundargoc](https://github.com/dundargoc)
- [@jdelkins](https://github.com/jdelkins)
- [@dsully](https://github.com/dsully)
```

## File: `selene.toml`
```
std="vim"
```

## File: `stylua.toml`
```
indent_type = "Spaces"
indent_width = 2
quote_style = "AutoPreferSingle"
no_call_parentheses = true
```

## File: `vim.toml`
```
[selene]
base = "lua51"
name = "vim"

[vim]
any = true

[jit]
any = true

[[describe.args]]
type = "string"
[[describe.args]]
type = "function"

[[it.args]]
type = "string"
[[it.args]]
type = "function"

[[before_each.args]]
type = "function"
[[after_each.args]]
type = "function"

[assert.is_not]
any = true

[[assert.equals.args]]
type = "any"
[[assert.equals.args]]
type = "any"
[[assert.equals.args]]
type = "any"
required = false

[[assert.same.args]]
type = "any"
[[assert.same.args]]
type = "any"

[[assert.truthy.args]]
type = "any"

[[assert.spy.args]]
type = "any"

[[assert.stub.args]]
type = "any"
```

## File: `doc/packer.txt`
```
*packer.txt*                      A use-package inspired Neovim plugin manager
*packer.nvim*

Author: Wil Thomason <wil.thomason@gmail.com>

CONTENTS                                        *packer-contents*
Introduction                                    |packer-introduction|
  Features                                      |packer-intro-features|
  Requirements                                  |packer-intro-requirements|
  Quickstart                                    |packer-intro-quickstart|
Usage                                           |packer-usage|
API                                             |packer-api|
==============================================================================
INTRODUCTION                                    *packer-introduction*

This is a Neovim plugin manager. It is written in Lua, uses the native
|packages| feature, and has features for declarative plugin configuration
inspired by the `use-package` library from Emacs.

==============================================================================
REQUIREMENTS                                     *packer-intro-requirements*

- You need to be running Neovim v0.5.0+; `packer` makes use of extmarks and
  other newly-added Neovim features.
- Your version of Neovim must be compiled with LuaJIT support; `packer` relies
  on this to detect whether you are running Windows or a Unix-like OS (for path
  separators)
- If you are on Windows 10, you need developer mode enabled in order to use
  local plugins (creating symbolic links requires admin privileges on Windows
  - credit to @TimUntersberger for this note)

==============================================================================
FEATURES                                         *packer-intro-features*

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
- Support for saving/restoring snapshots for plugin versions (`git` only)

==============================================================================
QUICKSTART                                       *packer-intro-quickstart*

To get started, first clone this repository to somewhere on your `packpath`, e.g.: >sh
  git clone https://github.com/wbthomason/packer.nvim\
   ~/.local/share/nvim/site/pack/packer/opt/packer.nvim


Then you can write your plugin specification in Lua, e.g. (in `~/.config/nvim/lua/plugins.lua`): >lua

  -- This file can be loaded by calling `lua require('plugins')` from your init.vim

  -- Only required if you have packer in your `opt` pack
  vim.cmd [[packadd packer.nvim]]
  -- Only if your version of Neovim doesn't have https://github.com/neovim/neovim/pull/12632 merged
  vim._update_package_paths()

  return require('packer').startup(function()
    -- Packer can manage itself as an optional plugin
    use {'wbthomason/packer.nvim', opt = true}

    -- Simple plugins can be specified as strings
    use '9mm/vim-closer'

    -- Lazy loading:
    -- Load on specific commands
    use {'tpope/vim-dispatch', opt = true, cmd = {'Dispatch', 'Make', 'Focus', 'Start'}}

    -- Load on an autocommand event
    use {'andymass/vim-matchup', event = 'VimEnter *'}

    -- Load on a combination of conditions: specific filetypes or commands
    -- Also run code after load (see the "config" key)
    use {
      'w0rp/ale',
      ft = {'sh', 'zsh', 'bash', 'c', 'cpp', 'cmake', 'html', 'markdown', 'racket', 'vim', 'tex'},
      cmd = 'ALEEnable',
      config = 'vim.cmd[[ALEEnable]]'
    }

    -- Plugins can have dependencies on other plugins
    use {
      'haorenW1025/completion-nvim',
      opt = true,
      requires = {{'hrsh7th/vim-vsnip', opt = true}, {'hrsh7th/vim-vsnip-integ', opt = true}}
    }

    -- Local plugins can be included
    use '~/projects/personal/hover.nvim'

    -- Plugins can have post-install/update hooks
    use {'iamcco/markdown-preview.nvim', run = 'cd app && yarn install', cmd = 'MarkdownPreview'}

    -- You can specify multiple plugins in a single call
    use {'tjdevries/colorbuddy.vim', {'nvim-treesitter/nvim-treesitter', opt = true}}

    -- You can alias plugin names
    use {'dracula/vim', as = 'dracula'}
  end)

`packer` provides the following commands after you've run and configured `packer` with `require('packer').startup(...)`: *packer-default-commands* *packer-commands*

`PackerClean`                                   *packer-commands-clean*
Remove any disabled or unused plugins.

`PackerCompile`                                 *packer-commands-compile*
You must run this or `PackerSync` whenever you make changes to your plugin
configuration. Regenerate compiled loader file.

`PackerInstall`                                 *packer-commands-install*
Clean, then install missing plugins.

`PackerUpdate`                                  *packer-commands-update*
Clean, then update and install plugins.
Supports the `--preview` flag as an optional first argument to preview
updates.

`PackerSync`                                    *packer-commands-sync*
Perform `PackerUpdate` and then `PackerCompile`.
Supports the `--preview` flag as an optional first argument to preview
updates.

`PackerLoad`                                    *packer-commands-load*
Loads opt plugin immediately

`PackerSnapshot`                                    *packer-commands-snapshot*
Snapshots your plugins to a file

`PackerSnapshotDelete`                                    *packer-commands-delete*
Deletes a snapshot

`PackerSnapshotRollback`                                    *packer-commands-rollback*
Rolls back plugins' commit specified by the snapshot
==============================================================================
USAGE                                          *packer-usage*

Although the example in |packer-intro-quickstart| will be enough to get you
going for basic usage, `packer` has a number of other features and options
detailed in this section.

STARTUP                                        *packer-startup*

The easiest way to use `packer` is via the |packer.startup()| function. In
short, `startup` is a convenience function for simple setup, and is invoked as
`packer.startup(spec)`, where:

- `spec` can be a function: >lua
  packer.startup(function() use 'tjdevries/colorbuddy.vim' end)
- `spec` can be a table with a function as its first element and config
  overrides as another element: >lua
  packer.startup({
    function() use 'tjdevries/colorbuddy.vim' end, config = { ... }
    })
- `spec` can be a table with a table of plugin specifications as its first
  element, config overrides as another element, and optional rock
  specifications as another element: >lua
  packer.startup({{'tjdevries/colorbuddy.vim'}, config = { ... }, rocks = { ... }})

See |packer-configuration| for the allowed configuration keys.

`startup` will handle calling |packer.init()| and |packer.reset()| for you, as
well as creating the commands given in |packer-commands|.

CUSTOM INITIALIZATION                          *packer-custom-initialization*
If you prefer a more manual setup with finer control over configuration and
loading, you may use custom initialization for `packer`. This approach has the
benefit of not requiring that the `packer` plugin be loaded unless you want to
perform plugin management operations, but it is more involved to use.

To take this approach, load `packer` like any other Lua module. You must call
|packer.init()| before performing any operations; it is recommended to call
|packer.reset()| if you may be re-running your specification code (e.g. by
sourcing your plugin specification file with `luafile`).

See |packer.init()| for more details on initialization; in short, `init` takes
a table of configuration values like that which can be passed to `startup`.

If you use custom initialization, you'll probably want to define commands to
load `packer` and perform common package management operations. The following
commands work well for this purpose: >vim

  command! -nargs=* -complete=customlist,v:lua.require'packer'.plugin_complete  PackerInstall lua require('packer').install(<f-args>)
  command! -nargs=* -complete=customlist,v:lua.require'packer'.plugin_complete PackerUpdate lua require('packer').update(<f-args>)
  command! -nargs=* -complete=customlist,v:lua.require'packer'.plugin_complete PackerSync lua require('packer').sync(<f-args>)
  command! PackerClean packadd packer.nvim | lua require('plugins').clean()
  command! PackerCompile packadd packer.nvim | lua require('plugins').compile('~/.config/nvim/plugin/packer_load.vim')
  command! -bang -nargs=+ -complete=customlist,v:lua.require'packer'.loader_complete PackerLoad lua require('packer').loader(<f-args>, '<bang>')

CONFIGURATION                                  *packer-configuration*
`packer` provides the following configuration variables, presented in the
structure of the `config` table expected by `startup` or `init`, with their
default values: >lua
  {
    ensure_dependencies   = true, -- Should packer install plugin dependencies?
    package_root   = util.join_paths(vim.fn.stdpath('data'), 'site', 'pack'),
    compile_path = util.join_paths(vim.fn.stdpath('config'), 'plugin', 'packer_compiled.lua'),
    plugin_package = 'packer', -- The default package for plugins
    max_jobs = nil, -- Limit the number of simultaneous jobs. nil means no limit
    auto_clean = true, -- During sync(), remove unused plugins
    compile_on_sync = true, -- During sync(), run packer.compile()
    disable_commands = false, -- Disable creating commands
    opt_default = false, -- Default to using opt (as opposed to start) plugins
    transitive_opt = true, -- Make dependencies of opt plugins also opt by default
    transitive_disable = true, -- Automatically disable dependencies of disabled plugins
    auto_reload_compiled = true, -- Automatically reload the compiled file after creating it.
    preview_updates = false, -- If true, always preview updates before choosing which plugins to update, same as `PackerUpdate --preview`.
    git = {
      cmd = 'git', -- The base command for git operations
      subcommands = { -- Format strings for git subcommands
        update         = 'pull --ff-only --progress --rebase=false --force',
        install        = 'clone --depth %i --no-single-branch --progress',
        fetch          = 'fetch --depth 999999 --progress --force',
        checkout       = 'checkout %s --',
        update_branch  = 'merge --ff-only @{u}',
        current_branch = 'branch --show-current',
        diff           = 'log --color=never --pretty=format:FMT --no-show-signature HEAD@{1}...HEAD',
        diff_fmt       = '%%h %%s (%%cr)',
        get_rev        = 'rev-parse --short HEAD',
        get_msg        = 'log --color=never --pretty=format:FMT --no-show-signature HEAD -n 1',
        submodules     = 'submodule update --init --recursive --progress'
      },
      depth = 1, -- Git clone depth
      clone_timeout = 60, -- Timeout, in seconds, for git clones
      default_url_format = 'https://github.com/%s' -- Lua format string used for "aaa/bbb" style plugins
    },
    log = { level = 'warn' }, -- The default print log level. One of: "trace", "debug", "info", "warn", "error", "fatal".
    display = {
      non_interactive = false, -- If true, disable display windows for all operations
      compact = false, -- If true, fold updates results by default
      open_fn  = nil, -- An optional function to open a window for packer's display
      open_cmd = '65vnew \\[packer\\]', -- An optional command to open a window for packer's display
      working_sym = '⟳', -- The symbol for a plugin being installed/updated
      error_sym = '✗', -- The symbol for a plugin with an error in installation/updating
      done_sym = '✓', -- The symbol for a plugin which has completed installation/updating
      removed_sym = '-', -- The symbol for an unused plugin which was removed
      moved_sym = '→', -- The symbol for a plugin which was moved (e.g. from opt to start)
      header_sym = '━', -- The symbol for the header line in packer's display
      show_all_info = true, -- Should packer show all update details automatically?
      prompt_border = 'double', -- Border style of prompt popups.
      keybindings = { -- Keybindings for the display window
        quit = 'q',
        toggle_update = 'u', -- only in preview
        continue = 'c', -- only in preview
        toggle_info = '<CR>',
        diff = 'd',
        prompt_revert = 'r',
      }
    }
    autoremove = false, -- Remove disabled or unused plugins without prompting the user
  }

SPECIFYING PLUGINS                             *packer-specifying-plugins*
`packer` is based around declarative specification of plugins. You can declare
a plugin using the function |packer.use()|, which I highly recommend locally
binding to `use` for conciseness.

`use` takes either a string or a table. If a string is provided, it is treated
as a plugin location for a non-optional plugin with no additional
configuration. Plugin locations may be specified as:
  1. Absolute paths to a local plugin
  2. Full URLs (treated as plugins managed with `git`)
  3. `username/repo` paths (treated as Github `git` plugins)

A table given to `use` can take two forms:
  1. A list of plugin specifications (strings or tables)
  2. A table specifying a single plugin. It must have a plugin location string
  as its first element, and may additionally have a number of optional keyword
  elements, detailed in |packer.use()|

CONFIGURING PLUGINS                            *packer-plugin-configuration*
`packer` allows you to configure plugins either before they are loaded (the
`setup` key described in |packer.use()|) or after they are loaded (the
`config` key described in |packer.use()|).
If functions are given for these keys, the functions will be passed the plugin
name and information table as arguments.

PLUGIN STATUSES                                 *packer-plugin-status*
You can check whether or not a particular plugin is installed with `packer` as
well as if that plugin is loaded. To do this you can check for the plugin's
name in the `packer_plugins` global table. Plugins in this table are saved
using only the last section of their names e.g. `tpope/vim-fugitive` if
installed will be under the key `vim-fugitive`.
>lua
  if packer_plugins["vim-fugitive"] and packer_plugins["vim-fugitive"].loaded then
  print("Vim fugitive is loaded")
  -- other custom logic
  end

CUSTOM INSTALLERS                              *packer-custom-installers*
You may specify a custom installer & updater for a plugin using the
`installer` and `updater` keys in a plugin specification. Note that either
both or none of these keys are required. These keys should be functions which
take as an argument a `display` object (from `lua/packer/display.lua`) and
return an async function (per `lua/packer/async.lua`) which (respectively)
installs/updates the given plugin.

Providing the `installer`/`updater` keys overrides plugin type detection, but
you still need to provide a location string for the name of the plugin.

POST-UPDATE HOOKS                              *packer-plugin-hooks*
You may specify operations to be run after successful installs/updates of a
plugin with the `run` key. This key may either be a Lua function, which will be
called with the `plugin` table for this plugin (containing the information
passed to `use` as well as output from the installation/update commands, the
installation path of the plugin, etc.), a string, or a table of functions and
strings.

If an element of `run` is a string, then either:

1. If the first character of `run` is ":", it is treated as a Neovim command and
executed.
2. Otherwise, `run` is treated as a shell command and run in the installation
directory of the plugin via `$SHELL -c '<run>'`.

DEPENDENCIES                                   *packer-plugin-dependencies*
Plugins may specify dependencies via the `requires` key in their specification
table. This key can be a string or a list (table).

If `requires` is a string, it is treated as specifying a single plugin. If a
plugin with the name given in `requires` is already known in the managed set,
nothing happens. Otherwise, the string is treated as a plugin location string
and the corresponding plugin is added to the managed set.

If `requires` is a list, it is treated as a list of plugin specifications
following the format given above.

If `ensure_dependencies` is true, the plugins specified in `requires` will be
installed.

Plugins specified in `requires` are removed when no active plugins require
them.

LUAROCKS                                       *packer-plugin-luarocks*

You may specify that a plugin requires one or more Luarocks packages using the
`rocks` key. This key takes either a string specifying the name of a package
(e.g. `rocks=lpeg`), or a list specifying one or more packages. Entries in the
list may either be strings or lists --- the latter case is used to specify a
particular version of a package, e.g. `rocks = {'lpeg', {'lua-cjson',
'2.1.0'}}`.

Currently, `packer` only supports equality constraints on package versions.

`packer` also provides the function `packer.luarocks.install_commands()`, which
creates the `PackerRocks <cmd> <packages...>` command. `<cmd>` must be one of
"install" or "remove"; `<packages...>` is one or more package names (currently,
version restrictions are not supported with this command). Running `PackerRocks`
will install or remove the given packages. You can use this command even if you
don't use `packer` to manage your plugins. However, please note that (1)
packages installed through `PackerRocks` **will** be removed by calls to
`packer.luarocks.clean()` (unless they are also part of a `packer` plugin
specification), and (2) you will need to manually invoke
`packer.luarocks.setup_paths` (or otherwise modify your `package.path`) to
ensure that Neovim can find the installed packages.

Finally, `packer` provides the function `packer.use_rocks`, which takes a string
or table specifying one or more Luarocks packages as in the `rocks` key. You can
use this to ensure that `packer` downloads and manages some rocks which you want
to use, but which are not associated with any particular plugin.

SEQUENCING                                     *packer-plugin-sequencing*

You may specify a loading order for plugins using the `after` key. This key can
be a string or a list (table).

If `after` is a string, it must be the name of another plugin managed by
`packer` (e.g. the final segment of a plugin's path - for a Github plugin
`FooBar/Baz`, the name would be just `Baz`). If `after` is a table, it must be a
list of plugin names. If a plugin has an alias (i.e. uses the `as` key), this
alias is its name.

The set of plugins specified in a plugin's `after` key must *all* be loaded
before the plugin using `after` will be loaded. For example, in the
specification >lua
  use {'FooBar/Baz', ft = 'bax'}
  use {'Something/Else', after = 'Baz'}

the plugin `Else` will only be loaded after the plugin `Baz`, which itself is
only loaded for files with `bax` filetype.

KEYBINDINGS                                    *packer-plugin-keybindings*
Plugins may be lazy-loaded on the use of keybindings/maps. Individual
keybindings are specified under the `keys` key in a plugin specification
either as a string (in which case they are treated as normal mode maps) or a
table in the format `{mode, map}`.

LAZY-LOADING                                   *packer-lazy-load*
To optimize startup time, `packer.nvim` compiles code to perform the
lazy-loading operations you specify. This means that you do not need to load
`packer.nvim` unless you want to perform some plugin management operations.

To generate the compiled code, call `packer.compile(path)`, where `path` is
some file path on your `runtimepath`, with a `.vim` extension. This will
generate a blend of Lua and Vimscript to load and configure all your
lazy-loaded plugins (e.g. generating commands, autocommands, etc.) and save it
to `path`. Then, when you start vim, the file at `path` is loaded (because
`path` must be on your `runtimepath`), and lazy-loading works.

If `path` is not provided to |packer.compile()|, the output file will default
to the value of `config.compile_path`.

The option `compile_on_sync`, which defaults to `true`, will run
`packer.compile()` during `packer.sync()`, if set to `true`.
Note that otherwise, you **must** run `packer.compile` yourself to generate
the lazy-loader file!

USING A FLOATING WINDOW                        *packer-floating-window*
You can configure Packer to use a floating window for command outputs by
passing a utility function to `packer`'s config: >lua

  packer.startup({function()
    -- Your plugins here
  end,
  config = {
    display = {
      open_fn = require('packer.util').float,
    }
  }})
<
By default, this floating window will show doubled borders. If you want to
customize the window appearance, you can pass a configuration to `float`,
which is the same configuration that would be passed to |nvim_open_win|: >lua

  packer.startup({function()
    -- Your plugins here
  end,
  config = {
    display = {
      open_fn = function()
        return require('packer.util').float({ border = 'single' })
      end
    }
  }})
<
PROFILING PLUGINS                              *packer-profiling*
You can measure how long it takes your plugins to load using packer's builtin
profiling functionality.
In order to use this functionality you must either enable profiling in your config, or pass in an argument
when running packer compile.

Setup via config >lua
  config = {
    profile = {
      enable = true,
      threshold = 1 -- the amount in ms that a plugin's load time must be over for it to be included in the profile
    }
  }
<

Using the packer compile command
>vim
  :PackerCompile profile=true
  " or
  :PackerCompile profile=false
<

NOTE you can also set a `threshold` in your profile config which is a number
in `ms` above which plugin load times will be show e.g. if you set a threshold
value of `3` then any plugin that loads slower than `3ms` will not be included in
the output window.

This will rebuild your `packer_compiled.vim` with profiling code included. In order to visualise the output of the profile
Restart your neovim and run `PackerProfile`. This will open a window with the output of your profiling.

EXTENDING PACKER                               *packer-extending*
You can add custom key handlers to `packer` by calling
`packer.set_handler(name, func)` where `name` is the key you wish to handle
and `func` is a function with the signature `func(plugins, plugin, value)`
where `plugins` is the global table of managed plugins, `plugin` is the table
for a specific plugin, and `value` is the value associated with key `name` in
`plugin`.

RESULTS WINDOW KEYBINDINGS                     *packer-results-keybindings*
Once an operation completes, the results are shown in the display window.
`packer` sets up default keybindings for this window:

q                    close the display window
<CR>                 toggle information about a particular plugin
r                    revert an update

They can be configured by changing the value of `config.display.keybindings`
(see |packer-configuration|). Setting it to `false` will disable all keybindings.
Setting any of its keys to `false` will disable the corresponding keybinding.

USER AUTOCMDS                                  *packer-user-autocmds*
`packer` runs most of its operations asyncronously. If you would like to
implement automations that require knowing when the operations are complete,
you can use the following User autocmds (see |User| for more info on how to
use):

`PackerComplete`       Fires after install, update, clean, and sync
                     asynchronous operations finish.
`PackerCompileDone`    Fires after compiling (see |packer-lazy-load|)

==============================================================================
API                                            *packer-api*

clean()		                                     *packer.clean()*
`clean` scans for and removes all disabled or no longer managed plugins. It is
invoked without arguments.

compile()		                                   *packer.compile()*
`compile` builds lazy-loader code from your plugin specification and saves it
to either `config.compile_path` if it is invoked with no argument, or to the
path it is invoked with if it is given a single argument. This path should end
in `.vim` and be on your |runtimepath| in order for lazy-loading to work. You
**must** call `compile` to update lazy-loaders after your configuration
changes.

init()		                                     *packer.init()*
Initializes `packer`; must be called before any calls to any other `packer`
function. Takes an optional table of configuration values as described in
|packer-configuration|.

install()		                                   *packer.install()*
`install` installs any missing plugins, runs post-update hooks, and updates
rplugins (|remote-plugin|) and helptags.

It can be invoked with no arguments or with a list of plugin names to install.
These plugin names must already be managed by `packer` via a call to
|packer.use()|.

reset()		                                     *packer.reset()*
`reset` empties the set of managed plugins. Called with no arguments; used to
ensure plugin specifications are reinitialized if the specification file is
reloaded. Called by |packer.startup()| or manually before calling
|packer.use()|.

set_handler()		                               *packer.set_handler()*
`set_handler` allows custom extension of `packer`. See |packer-extending| for
details.

startup()		                                   *packer.startup()*
`startup` is a convenience function for simple setup. See |packer-startup| for
details.

sync()		                                     *packer.sync()*
`sync` runs |packer.clean()| followed by |packer.update()|.

Supports options as the first argument, see |packer.update()|.

update()		                                   *packer.update()*
`update` installs any missing plugins, updates all installed plugins, runs
post-update hooks, and updates rplugins (|remote-plugin|) and helptags.

It can be invoked with no arguments or with a list of plugin names to update.
These plugin names must already be managed by `packer` via a call to
|packer.use()|.

Additionally, the first argument can be a table specifying options,
such as `update({preview_updates = true}, ...)` to preview potential changes before updating
(same as `PackerUpdate --preview`).

snapshot(snapshot_name, ...)		                                *packer.snapshot()*
`snapshot` takes the rev of all the installed plugins and serializes them into a Lua table which will be saved under `config.snapshot_path` (which is the directory that will hold all the snapshots files) as `config.snapshot_path/<snapshot_name>` or an absolute path provided by the users.
Optionally plugins name can be specified so that only those plugins will be
snapshotted.
Snapshot files can be loaded manually via `dofile` which will return a table with the plugins name as keys the commit short hash as value.

delete(snapshot_name)		                                *packer.delete()*
`delete` deletes a snapshot given the name or the absolute path.

rollback(snapshot_name, ...)		                                *packer.rollback()*
`rollback` reverts all plugins or only the specified as extra arguments to the commit specified in the snapshot file

use()		                                       *packer.use()*
`use` allows you to add one or more plugins to the managed set. It can be
invoked as follows:
- With a single plugin location string, e.g. `use <STRING>`
- With a single plugin specification table, e.g. >lua
  use {
    'myusername/example',        -- The plugin location string
    -- The following keys are all optional
    disable = boolean,           -- Mark a plugin as inactive
    as = string,                 -- Specifies an alias under which to install the plugin
    installer = function,        -- Specifies custom installer. See |packer-custom-installers|
    updater = function,          -- Specifies custom updater. See |packer-custom-installers|
    after = string or list,      -- Specifies plugins to load before this plugin.
    rtp = string,                -- Specifies a subdirectory of the plugin to add to runtimepath.
    opt = boolean,               -- Manually marks a plugin as optional.
    bufread = boolean,           -- Manually specifying if a plugin needs BufRead after being loaded
    branch = string,             -- Specifies a git branch to use
    tag = string,                -- Specifies a git tag to use. Supports '*' for "latest tag"
    commit = string,             -- Specifies a git commit to use
    lock = boolean,              -- Skip updating this plugin in updates/syncs. Still cleans.
    run = string, function, or table  -- Post-update/install hook. See |packer-plugin-hooks|
    requires = string or list    -- Specifies plugin dependencies. See |packer-plugin-dependencies|
    config = string or function, -- Specifies code to run after this plugin is loaded.
    rocks = string or list,      -- Specifies Luarocks dependencies for the plugin
    -- The following keys all imply lazy-loading
    cmd = string or list,        -- Specifies commands which load this plugin.  Can be an autocmd pattern.
    ft = string or list,         -- Specifies filetypes which load this plugin.
    keys = string or list,       -- Specifies maps which load this plugin. See |packer-plugin-keybindings|
    event = string or list,      -- Specifies autocommand events which load this plugin.
    fn = string or list          -- Specifies functions which load this plugin.
    cond = string, function, or list of strings/functions,   -- Specifies a conditional test to load this plugin
    setup = string or function,  -- Specifies code to run before this plugin is loaded. The code is ran even if
                                 -- the plugin is waiting for other conditions (ft, cond...) to be met.
    module = string or list      -- Specifies Lua module names for require. When requiring a string which starts
                                 -- with one of these module names, the plugin will be loaded.
    module_pattern = string/list -- Specifies Lua pattern of Lua module names for require. When requiring a string
                                 -- which matches one of these patterns, the plugin will be loaded.
  }
- With a list of plugins specified in either of the above two forms

For the *cmd* option, the command may be a full command, or an autocommand pattern. If the command contains any
non-alphanumeric characters, it is assumed to be a pattern, and instead of creating a stub command, it creates
a CmdUndefined autocmd to load the plugin when a command that matches the pattern is invoked.

 vim:tw=78:ts=2:ft=help:norl:
```

## File: `lua/packer.lua`
```
-- TODO: Performance analysis/tuning
-- TODO: Merge start plugins?
local util = require 'packer.util'

local join_paths = util.join_paths
local stdpath = vim.fn.stdpath

-- Config
local packer = {}
local config_defaults = {
  ensure_dependencies = true,
  snapshot = nil,
  snapshot_path = join_paths(stdpath 'cache', 'packer.nvim'),
  package_root = join_paths(stdpath 'data', 'site', 'pack'),
  compile_path = join_paths(stdpath 'config', 'plugin', 'packer_compiled.lua'),
  plugin_package = 'packer',
  max_jobs = nil,
  auto_clean = true,
  compile_on_sync = true,
  disable_commands = false,
  opt_default = false,
  transitive_opt = true,
  transitive_disable = true,
  auto_reload_compiled = true,
  preview_updates = false,
  git = {
    mark_breaking_changes = true,
    cmd = 'git',
    subcommands = {
      update = 'pull --ff-only --progress --rebase=false --force',
      update_head = 'merge FETCH_HEAD',
      install = 'clone --depth %i --no-single-branch --progress',
      fetch = 'fetch --depth 999999 --progress --force',
      checkout = 'checkout %s --',
      update_branch = 'merge --ff-only @{u}',
      current_branch = 'rev-parse --abbrev-ref HEAD',
      diff = 'log --color=never --pretty=format:FMT --no-show-signature %s...%s',
      diff_fmt = '%%h %%s (%%cr)',
      git_diff_fmt = 'show --no-color --pretty=medium %s',
      get_rev = 'rev-parse --short HEAD',
      get_header = 'log --color=never --pretty=format:FMT --no-show-signature HEAD -n 1',
      get_bodies = 'log --color=never --pretty=format:"===COMMIT_START===%h%n%s===BODY_START===%b" --no-show-signature HEAD@{1}...HEAD',
      get_fetch_bodies = 'log --color=never --pretty=format:"===COMMIT_START===%h%n%s===BODY_START===%b" --no-show-signature HEAD...FETCH_HEAD',
      submodules = 'submodule update --init --recursive --progress',
      revert = 'reset --hard HEAD@{1}',
      revert_to = 'reset --hard %s --',
      tags_expand_fmt = 'tag -l %s --sort -version:refname',
    },
    depth = 1,
    clone_timeout = 60,
    default_url_format = 'https://github.com/%s.git',
  },
  display = {
    non_interactive = false,
    compact = false,
    open_fn = nil,
    open_cmd = '65vnew',
    working_sym = '⟳',
    error_sym = '✗',
    done_sym = '✓',
    removed_sym = '-',
    moved_sym = '→',
    item_sym = '•',
    header_sym = '━',
    header_lines = 2,
    title = 'packer.nvim',
    show_all_info = true,
    prompt_border = 'double',
    keybindings = {
      quit = 'q',
      toggle_update = 'u',
      continue = 'c',
      toggle_info = '<CR>',
      diff = 'd',
      prompt_revert = 'r',
      retry = 'R',
    },
  },
  luarocks = { python_cmd = 'python' },
  log = { level = 'warn' },
  profile = { enable = false },
  autoremove = false,
}

--- Initialize global namespace for use for callbacks and other data generated whilst packer is
--- running
_G._packer = _G._packer or {}

local config = vim.tbl_extend('force', {}, config_defaults)
local plugins = nil
local plugin_specifications = nil
local rocks = nil

local configurable_modules = {
  clean = false,
  compile = false,
  display = false,
  handlers = false,
  install = false,
  plugin_types = false,
  plugin_utils = false,
  update = false,
  luarocks = false,
  log = false,
  snapshot = false,
}

local function require_and_configure(module_name)
  local fully_qualified_name = 'packer.' .. module_name
  local module = require(fully_qualified_name)
  if not configurable_modules[module_name] and module.cfg then
    configurable_modules[module_name] = true
    module.cfg(config)
    return module
  end

  return module
end

--- Initialize packer
-- Forwards user configuration to sub-modules, resets the set of managed plugins, and ensures that
-- the necessary package directories exist
packer.init = function(user_config)
  user_config = user_config or {}
  config = util.deep_extend('force', config, user_config)
  packer.reset()
  config.package_root = vim.fn.fnamemodify(config.package_root, ':p')
  local _
  config.package_root, _ = string.gsub(config.package_root, util.get_separator() .. '$', '', 1)
  config.pack_dir = join_paths(config.package_root, config.plugin_package)
  config.opt_dir = join_paths(config.pack_dir, 'opt')
  config.start_dir = join_paths(config.pack_dir, 'start')

  local plugin_utils = require_and_configure 'plugin_utils'
  plugin_utils.ensure_dirs()

  require_and_configure 'snapshot'

  if not config.disable_commands then
    packer.make_commands()
  end

  if vim.fn.mkdir(config.snapshot_path, 'p') ~= 1 then
    require_and_configure('log').warn("Couldn't create " .. config.snapshot_path)
  end
end

packer.make_commands = function()
  vim.cmd [[command! -nargs=+ -complete=customlist,v:lua.require'packer.snapshot'.completion.create PackerSnapshot  lua require('packer').snapshot(<f-args>)]]
  vim.cmd [[command! -nargs=+ -complete=customlist,v:lua.require'packer.snapshot'.completion.rollback PackerSnapshotRollback  lua require('packer').rollback(<f-args>)]]
  vim.cmd [[command! -nargs=+ -complete=customlist,v:lua.require'packer.snapshot'.completion.snapshot PackerSnapshotDelete lua require('packer.snapshot').delete(<f-args>)]]
  vim.cmd [[command! -nargs=* -complete=customlist,v:lua.require'packer'.plugin_complete PackerInstall lua require('packer').install(<f-args>)]]
  vim.cmd [[command! -nargs=* -complete=customlist,v:lua.require'packer'.plugin_complete PackerUpdate lua require('packer').update(<f-args>)]]
  vim.cmd [[command! -nargs=* -complete=customlist,v:lua.require'packer'.plugin_complete PackerSync lua require('packer').sync(<f-args>)]]
  vim.cmd [[command! PackerClean             lua require('packer').clean()]]
  vim.cmd [[command! -nargs=* PackerCompile  lua require('packer').compile(<q-args>)]]
  vim.cmd [[command! PackerStatus            lua require('packer').status()]]
  vim.cmd [[command! PackerProfile           lua require('packer').profile_output()]]
  vim.cmd [[command! -bang -nargs=+ -complete=customlist,v:lua.require'packer'.loader_complete PackerLoad lua require('packer').loader(<f-args>, '<bang>' == '!')]]
end

packer.reset = function()
  plugins = {}
  plugin_specifications = {}
  rocks = {}
end

--- Add a Luarocks package to be managed
packer.use_rocks = function(rock)
  if type(rock) == 'string' then
    rock = { rock }
  end
  if not vim.tbl_islist(rock) and type(rock[1]) == 'string' then
    rocks[rock[1]] = rock
  else
    for _, r in ipairs(rock) do
      local rock_name = (type(r) == 'table') and r[1] or r
      rocks[rock_name] = r
    end
  end
end

--- The main logic for adding a plugin (and any dependencies) to the managed set
-- Can be invoked with (1) a single plugin spec as a string, (2) a single plugin spec table, or (3)
-- a list of plugin specs
-- TODO: This should be refactored into its own module and the various keys should be implemented
-- (as much as possible) as ordinary handlers
local manage = nil
manage = function(plugin_data)
  local plugin_spec = plugin_data.spec
  local spec_line = plugin_data.line
  local spec_type = type(plugin_spec)
  if spec_type == 'string' then
    plugin_spec = { plugin_spec }
  elseif spec_type == 'table' and #plugin_spec > 1 then
    for _, spec in ipairs(plugin_spec) do
      manage { spec = spec, line = spec_line }
    end
    return
  end

  local log = require_and_configure 'log'
  if plugin_spec[1] == vim.NIL or plugin_spec[1] == nil then
    log.warn('No plugin name provided at line ' .. spec_line .. '!')
    return
  end

  local name, path = util.get_plugin_short_name(plugin_spec)

  if name == '' then
    log.warn('"' .. plugin_spec[1] .. '" is an invalid plugin name!')
    return
  end

  if plugins[name] and not plugins[name].from_requires then
    log.warn('Plugin "' .. name .. '" is used twice! (line ' .. spec_line .. ')')
    return
  end

  if plugin_spec.as and plugins[plugin_spec.as] then
    log.error(
      'The alias '
        .. plugin_spec.as
        .. ', specified for '
        .. path
        .. ' at '
        .. spec_line
        .. ' is already used as another plugin name!'
    )
    return
  end

  -- Handle aliases
  plugin_spec.short_name = name
  plugin_spec.name = path
  plugin_spec.path = path

  -- Some config keys modify a plugin type
  if plugin_spec.opt then
    plugin_spec.manual_opt = true
  elseif plugin_spec.opt == nil and config.opt_default then
    plugin_spec.manual_opt = true
    plugin_spec.opt = true
  end

  local compile = require_and_configure 'compile'
  for _, key in ipairs(compile.opt_keys) do
    if plugin_spec[key] ~= nil then
      plugin_spec.opt = true
      break
    end
  end

  plugin_spec.install_path = join_paths(plugin_spec.opt and config.opt_dir or config.start_dir, plugin_spec.short_name)

  local plugin_utils = require_and_configure 'plugin_utils'
  local plugin_types = require_and_configure 'plugin_types'
  local handlers = require_and_configure 'handlers'
  if not plugin_spec.type then
    plugin_utils.guess_type(plugin_spec)
  end
  if plugin_spec.type ~= plugin_utils.custom_plugin_type then
    plugin_types[plugin_spec.type].setup(plugin_spec)
  end
  for k, v in pairs(plugin_spec) do
    if handlers[k] then
      handlers[k](plugins, plugin_spec, v)
    end
  end
  plugins[plugin_spec.short_name] = plugin_spec
  if plugin_spec.rocks then
    packer.use_rocks(plugin_spec.rocks)
  end

  -- Add the git URL for displaying in PackerStatus and PackerSync.
  plugins[plugin_spec.short_name].url = util.remove_ending_git_url(plugin_spec.url)

  if plugin_spec.requires and config.ensure_dependencies then
    -- Handle single plugins given as strings or single plugin specs given as tables
    if
      type(plugin_spec.requires) == 'string'
      or (
        type(plugin_spec.requires) == 'table'
        and not vim.tbl_islist(plugin_spec.requires)
        and #plugin_spec.requires == 1
      )
    then
      plugin_spec.requires = { plugin_spec.requires }
    end
    for _, req in ipairs(plugin_spec.requires) do
      if type(req) == 'string' then
        req = { req }
      end
      local req_name_segments = vim.split(req[1], '/')
      local req_name = req_name_segments[#req_name_segments]
      -- this flag marks a plugin as being from a require which we use to allow
      -- multiple requires for a plugin without triggering a duplicate warning *IF*
      -- the plugin is from a `requires` field and the full specification has not been called yet.
      -- @see: https://github.com/wbthomason/packer.nvim/issues/258#issuecomment-876568439
      req.from_requires = true
      if not plugins[req_name] then
        if config.transitive_opt and plugin_spec.manual_opt then
          req.opt = true
          if type(req.after) == 'string' then
            req.after = { req.after, plugin_spec.short_name }
          elseif type(req.after) == 'table' then
            local already_after = false
            for _, name in ipairs(req.after) do
              already_after = already_after or (name == plugin_spec.short_name)
            end
            if not already_after then
              table.insert(req.after, plugin_spec.short_name)
            end
          elseif req.after == nil then
            req.after = plugin_spec.short_name
          end
        end

        if config.transitive_disable and plugin_spec.disable then
          req.disable = true
        end

        manage { spec = req, line = spec_line }
      end
    end
  end
end

--- Add a new keyword handler
packer.set_handler = function(name, func)
  require_and_configure('handlers')[name] = func
end

--- Add a plugin to the managed set
packer.use = function(plugin_spec)
  plugin_specifications[#plugin_specifications + 1] = {
    spec = plugin_spec,
    line = debug.getinfo(2, 'l').currentline,
  }
end

local function manage_all_plugins()
  local log = require_and_configure 'log'
  log.debug 'Processing plugin specs'
  if plugins == nil or next(plugins) == nil then
    for _, spec in ipairs(plugin_specifications) do
      manage(spec)
    end
  end
end

packer.__manage_all = manage_all_plugins

--- Hook to fire events after packer operations
packer.on_complete = vim.schedule_wrap(function()
  vim.cmd [[doautocmd User PackerComplete]]
end)

--- Hook to fire events after packer compilation
packer.on_compile_done = function()
  local log = require_and_configure 'log'

  vim.cmd [[doautocmd User PackerCompileDone]]
  log.debug 'packer.compile: Complete'
end

--- Clean operation:
-- Finds plugins present in the `packer` package but not in the managed set
packer.clean = function(results)
  local plugin_utils = require_and_configure 'plugin_utils'
  local a = require 'packer.async'
  local async = a.sync
  local await = a.wait
  local luarocks = require_and_configure 'luarocks'
  local clean = require_and_configure 'clean'
  require_and_configure 'display'

  manage_all_plugins()
  async(function()
    local luarocks_clean_task = luarocks.clean(rocks, results, nil)
    if luarocks_clean_task ~= nil then
      await(luarocks_clean_task)
    end
    local fs_state = await(plugin_utils.get_fs_state(plugins))
    await(clean(plugins, fs_state, results))
    packer.on_complete()
  end)()
end

--- Install operation:
-- Takes an optional list of plugin names as an argument. If no list is given, operates on all
-- managed plugins.
-- Installs missing plugins, then updates helptags and rplugins
packer.install = function(...)
  local log = require_and_configure 'log'
  log.debug 'packer.install: requiring modules'
  local plugin_utils = require_and_configure 'plugin_utils'
  local a = require 'packer.async'
  local async = a.sync
  local await = a.wait
  local luarocks = require_and_configure 'luarocks'
  local clean = require_and_configure 'clean'
  local install = require_and_configure 'install'
  local display = require_and_configure 'display'

  manage_all_plugins()
  local install_plugins
  if ... then
    install_plugins = { ... }
  end
  async(function()
    local fs_state = await(plugin_utils.get_fs_state(plugins))
    if not install_plugins then
      install_plugins = vim.tbl_keys(fs_state.missing)
    end
    if #install_plugins == 0 then
      log.info 'All configured plugins are installed'
      packer.on_complete()
      return
    end

    await(a.main)
    local start_time = vim.fn.reltime()
    local results = {}
    await(clean(plugins, fs_state, results))
    await(a.main)
    log.debug 'Gathering install tasks'
    local tasks, display_win = install(plugins, install_plugins, results)
    if next(tasks) then
      log.debug 'Gathering Luarocks tasks'
      local luarocks_ensure_task = luarocks.ensure(rocks, results, display_win)
      if luarocks_ensure_task ~= nil then
        table.insert(tasks, luarocks_ensure_task)
      end
      table.insert(tasks, 1, function()
        return not display.status.running
      end)
      table.insert(tasks, 1, config.max_jobs and config.max_jobs or (#tasks - 1))
      log.debug 'Running tasks'
      display_win:update_headline_message(#tasks - 2 .. ' / ' .. #tasks - 2 .. ' install tasks')
      a.interruptible_wait_pool(unpack(tasks))
      local install_paths = {}
      for plugin_name, r in pairs(results.installs) do
        if r.ok then
          table.insert(install_paths, results.plugins[plugin_name].install_path)
        end
      end

      await(a.main)
      plugin_utils.update_helptags(install_paths)
      plugin_utils.update_rplugins()
      local delta = string.gsub(vim.fn.reltimestr(vim.fn.reltime(start_time)), ' ', '')
      display_win:final_results(results, delta)
      packer.on_complete()
    else
      log.info 'Nothing to install!'
      packer.on_complete()
    end
  end)()
end

-- Filter out options specified as the first argument to update or sync
-- returns the options table and the plugin names
local filter_opts_from_plugins = function(...)
  local args = { ... }
  local opts = {}
  if not vim.tbl_isempty(args) then
    local first = args[1]
    if type(first) == 'table' then
      table.remove(args, 1)
      opts = first
    elseif first == '--preview' then
      table.remove(args, 1)
      opts = { preview_updates = true }
    end
  end
  if opts.preview_updates == nil and config.preview_updates then
    opts.preview_updates = true
  end
  return opts, util.nonempty_or(args, vim.tbl_keys(plugins))
end

--- Update operation:
-- Takes an optional list of plugin names as an argument. If no list is given, operates on all
-- managed plugins.
-- Fixes plugin types, installs missing plugins, then updates installed plugins and updates helptags
-- and rplugins
-- Options can be specified in the first argument as either a table or explicit `'--preview'`.
packer.update = function(...)
  local log = require_and_configure 'log'
  log.debug 'packer.update: requiring modules'
  local plugin_utils = require_and_configure 'plugin_utils'
  local a = require 'packer.async'
  local async = a.sync
  local await = a.wait
  local luarocks = require_and_configure 'luarocks'
  local clean = require_and_configure 'clean'
  local install = require_and_configure 'install'
  local display = require_and_configure 'display'
  local update = require_and_configure 'update'

  manage_all_plugins()

  local opts, update_plugins = filter_opts_from_plugins(...)
  async(function()
    local start_time = vim.fn.reltime()
    local results = {}
    local fs_state = await(plugin_utils.get_fs_state(plugins))
    local missing_plugins, installed_plugins = util.partition(vim.tbl_keys(fs_state.missing), update_plugins)
    update.fix_plugin_types(plugins, missing_plugins, results, fs_state)
    await(clean(plugins, fs_state, results))
    local _
    _, missing_plugins = util.partition(vim.tbl_keys(results.moves), missing_plugins)
    log.debug 'Gathering install tasks'
    await(a.main)
    local tasks, display_win = install(plugins, missing_plugins, results)
    local update_tasks
    log.debug 'Gathering update tasks'
    await(a.main)
    update_tasks, display_win = update(plugins, installed_plugins, display_win, results, opts)
    vim.list_extend(tasks, update_tasks)
    log.debug 'Gathering luarocks tasks'
    local luarocks_ensure_task = luarocks.ensure(rocks, results, display_win)
    if luarocks_ensure_task ~= nil then
      table.insert(tasks, luarocks_ensure_task)
    end

    if #tasks == 0 then
      return
    end

    table.insert(tasks, 1, function()
      return not display.status.running
    end)
    table.insert(tasks, 1, config.max_jobs and config.max_jobs or (#tasks - 1))
    display_win:update_headline_message(#tasks - 2 .. ' / ' .. #tasks - 2 .. ' update tasks')
    log.debug 'Running tasks'
    a.interruptible_wait_pool(unpack(tasks))
    local install_paths = {}
    for plugin_name, r in pairs(results.installs) do
      if r.ok then
        table.insert(install_paths, results.plugins[plugin_name].install_path)
      end
    end

    for plugin_name, r in pairs(results.updates) do
      if r.ok then
        table.insert(install_paths, results.plugins[plugin_name].install_path)
      end
    end

    await(a.main)
    plugin_utils.update_helptags(install_paths)
    plugin_utils.update_rplugins()
    local delta = string.gsub(vim.fn.reltimestr(vim.fn.reltime(start_time)), ' ', '')
    display_win:final_results(results, delta, opts)
    packer.on_complete()
  end)()
end

--- Sync operation:
-- Takes an optional list of plugin names as an argument. If no list is given, operates on all
-- managed plugins.
-- Runs (in sequence):
--  - Update plugin types
--  - Clean stale plugins
--  - Install missing plugins and update installed plugins
--  - Update helptags and rplugins
packer.sync = function(...)
  local log = require_and_configure 'log'
  log.debug 'packer.sync: requiring modules'
  local plugin_utils = require_and_configure 'plugin_utils'
  local a = require 'packer.async'
  local async = a.sync
  local await = a.wait
  local luarocks = require_and_configure 'luarocks'
  local clean = require_and_configure 'clean'
  local install = require_and_configure 'install'
  local display = require_and_configure 'display'
  local update = require_and_configure 'update'

  manage_all_plugins()

  local opts, sync_plugins = filter_opts_from_plugins(...)
  async(function()
    local start_time = vim.fn.reltime()
    local results = {}
    local fs_state = await(plugin_utils.get_fs_state(plugins))
    local missing_plugins, installed_plugins = util.partition(vim.tbl_keys(fs_state.missing), sync_plugins)

    await(a.main)
    update.fix_plugin_types(plugins, missing_plugins, results, fs_state)
    local _
    _, missing_plugins = util.partition(vim.tbl_keys(results.moves), missing_plugins)
    if config.auto_clean then
      await(clean(plugins, fs_state, results))
      _, installed_plugins = util.partition(vim.tbl_keys(results.removals), installed_plugins)
    end

    await(a.main)
    log.debug 'Gathering install tasks'
    local tasks, display_win = install(plugins, missing_plugins, results)
    local update_tasks
    log.debug 'Gathering update tasks'
    await(a.main)
    update_tasks, display_win = update(plugins, installed_plugins, display_win, results, opts)
    vim.list_extend(tasks, update_tasks)
    log.debug 'Gathering luarocks tasks'
    local luarocks_clean_task = luarocks.clean(rocks, results, display_win)
    if luarocks_clean_task ~= nil then
      table.insert(tasks, luarocks_clean_task)
    end

    local luarocks_ensure_task = luarocks.ensure(rocks, results, display_win)
    if luarocks_ensure_task ~= nil then
      table.insert(tasks, luarocks_ensure_task)
    end
    if #tasks == 0 then
      return
    end

    table.insert(tasks, 1, function()
      return not display.status.running
    end)
    table.insert(tasks, 1, config.max_jobs and config.max_jobs or (#tasks - 1))
    log.debug 'Running tasks'
    display_win:update_headline_message(#tasks - 2 .. ' / ' .. #tasks - 2 .. ' sync tasks')
    a.interruptible_wait_pool(unpack(tasks))
    local install_paths = {}
    for plugin_name, r in pairs(results.installs) do
      if r.ok then
        table.insert(install_paths, results.plugins[plugin_name].install_path)
      end
    end

    for plugin_name, r in pairs(results.updates) do
      if r.ok then
        table.insert(install_paths, results.plugins[plugin_name].install_path)
      end
    end

    await(a.main)
    if config.compile_on_sync then
      packer.compile(nil, false)
    end
    plugin_utils.update_helptags(install_paths)
    plugin_utils.update_rplugins()
    local delta = string.gsub(vim.fn.reltimestr(vim.fn.reltime(start_time)), ' ', '')
    display_win:final_results(results, delta, opts)
    packer.on_complete()
  end)()
end

packer.status = function()
  local async = require('packer.async').sync
  local display = require_and_configure 'display'
  local log = require_and_configure 'log'
  manage_all_plugins()
  async(function()
    local display_win = display.open(config.display.open_fn or config.display.open_cmd)
    if _G.packer_plugins ~= nil then
      display_win:status(_G.packer_plugins)
    else
      log.warn 'packer_plugins table is nil! Cannot run packer.status()!'
    end
  end)()
end

local function reload_module(name)
  if name then
    package.loaded[name] = nil
    return require(name)
  end
end

--- Search through all the loaded packages for those that
--- return a function, then cross reference them with all
--- the plugin configs and setups and if there are any matches
--- reload the user module.
local function refresh_configs(plugs)
  local reverse_index = {}
  for k, v in pairs(package.loaded) do
    if type(v) == 'function' then
      reverse_index[v] = k
    end
  end
  for _, plugin in pairs(plugs) do
    local cfg = reload_module(reverse_index[plugin.config])
    local setup = reload_module(reverse_index[plugin.setup])
    if cfg then
      plugin.config = cfg
    end
    if setup then
      plugin.setup = setup
    end
  end
end

local function parse_value(value)
  if value == 'true' then
    return true
  end
  if value == 'false' then
    return false
  end
  return value
end

local function parse_args(args)
  local result = {}
  if args then
    local parts = vim.split(args, ' ')
    for _, part in ipairs(parts) do
      if part then
        if part:find '=' then
          local key, value = unpack(vim.split(part, '='))
          result[key] = parse_value(value)
        end
      end
    end
  end
  return result
end

--- Update the compiled lazy-loader code
--- Takes an optional argument of a path to which to output the resulting compiled code
packer.compile = function(raw_args, move_plugins)
  local compile = require_and_configure 'compile'
  local log = require_and_configure 'log'
  local a = require 'packer.async'
  local async = a.sync
  local await = a.wait

  manage_all_plugins()
  async(function()
    if move_plugins ~= false then
      local update = require_and_configure 'update'
      local plugin_utils = require_and_configure 'plugin_utils'
      local fs_state = await(plugin_utils.get_fs_state(plugins))
      await(a.main)
      update.fix_plugin_types(plugins, vim.tbl_keys(fs_state.missing), {}, fs_state)
    end
    local args = parse_args(raw_args)
    local output_path = args.output_path or config.compile_path
    local output_lua = vim.fn.fnamemodify(output_path, ':e') == 'lua'
    local should_profile = args.profile
    -- the user might explicitly choose for this value to be false in which case
    -- an or operator will not work
    if should_profile == nil then
      should_profile = config.profile.enable
    end
    refresh_configs(plugins)
    -- NOTE: we copy the plugins table so the in memory value is not mutated during compilation
    local compiled_loader = compile(vim.deepcopy(plugins), output_lua, should_profile)
    output_path = vim.fn.expand(output_path, true)
    vim.fn.mkdir(vim.fn.fnamemodify(output_path, ':h'), 'p')
    local output_file = io.open(output_path, 'w')
    output_file:write(compiled_loader)
    output_file:close()
    if config.auto_reload_compiled then
      local configs_to_run = {}
      if _G.packer_plugins ~= nil then
        for plugin_name, plugin_info in pairs(_G.packer_plugins) do
          if plugin_info.loaded and plugin_info.config and plugins[plugin_name] and plugins[plugin_name].cmd then
            configs_to_run[plugin_name] = plugin_info.config
          end
        end
      end

      vim.cmd('source ' .. output_path)
      for plugin_name, plugin_config in pairs(configs_to_run) do
        for _, config_line in ipairs(plugin_config) do
          local success, err = pcall(loadstring(config_line), plugin_name, _G.packer_plugins[plugin_name])
          if not success then
            log.error('Error running config for ' .. plugin_name .. ': ' .. vim.inspect(err))
          end
        end
      end
    end
    log.info 'Finished compiling lazy-loaders!'
    packer.on_compile_done()
  end)()
end

packer.profile_output = function()
  local async = require('packer.async').sync
  local display = require_and_configure 'display'
  local log = require_and_configure 'log'

  manage_all_plugins()
  if _G._packer.profile_output then
    async(function()
      local display_win = display.open(config.display.open_fn or config.display.open_cmd)
      display_win:profile_output(_G._packer.profile_output)
    end)()
  else
    log.warn 'You must run PackerCompile with profiling enabled first e.g. PackerCompile profile=true'
  end
end

-- Load plugins
-- @param plugins string String of space separated plugins names
--                      intended for PackerLoad command
--                or list of plugin names as independent strings
packer.loader = function(...)
  local plugin_names = { ... }
  local force = plugin_names[#plugin_names] == true
  if type(plugin_names[#plugin_names]) == 'boolean' then
    plugin_names[#plugin_names] = nil
  end

  -- We make a new table here because it's more convenient than expanding a space-separated string
  -- into the existing plugin_names
  local plugin_list = {}
  for _, plugin_name in ipairs(plugin_names) do
    vim.list_extend(
      plugin_list,
      vim.tbl_filter(function(name)
        return #name > 0
      end, vim.split(plugin_name, ' '))
    )
  end

  require 'packer.load'(plugin_list, {}, _G.packer_plugins, force)
end

-- Completion for not yet loaded plugins
-- Intended to provide completion for PackerLoad command
packer.loader_complete = function(lead, _, _)
  local completion_list = {}
  for name, plugin in pairs(_G.packer_plugins) do
    if vim.startswith(name, lead) and not plugin.loaded then
      table.insert(completion_list, name)
    end
  end
  table.sort(completion_list)
  return completion_list
end

-- Completion user plugins
-- Intended to provide completion for PackerUpdate/Sync/Install command
packer.plugin_complete = function(lead, _, _)
  local completion_list = vim.tbl_filter(function(name)
    return vim.startswith(name, lead)
  end, vim.tbl_keys(_G.packer_plugins))
  table.sort(completion_list)
  return completion_list
end

---Snapshots installed plugins
---@param snapshot_name string absolute path or just a snapshot name
packer.snapshot = function(snapshot_name, ...)
  local async = require('packer.async').sync
  local await = require('packer.async').wait
  local snapshot = require 'packer.snapshot'
  local log = require_and_configure 'log'
  local args = { ... }
  snapshot_name = snapshot_name or require('os').date '%Y-%m-%d'
  local snapshot_path = vim.fn.expand(snapshot_name)

  local fmt = string.format
  log.debug(fmt('Taking snapshots of currently installed plugins to %s...', snapshot_name))
  if vim.fn.fnamemodify(snapshot_name, ':p') ~= snapshot_path then -- is not absolute path
    if config.snapshot_path == nil then
      log.warn 'config.snapshot_path is not set'
      return
    else
      snapshot_path = util.join_paths(config.snapshot_path, snapshot_path) -- set to default path
    end
  end

  manage_all_plugins()

  local target_plugins = plugins
  if next(args) ~= nil then -- provided extra args
    target_plugins = vim.tbl_filter( -- filter plugins
      function(plugin)
        for k, plugin_shortname in pairs(args) do
          if plugin_shortname == plugin.short_name then
            args[k] = nil
            return true
          end
        end
        return false
      end,
      plugins
    )
  end

  local write_snapshot = true

  if vim.fn.filereadable(snapshot_path) == 1 then
    vim.ui.select(
      { 'Replace', 'Cancel' },
      { prompt = fmt("Do you want to replace '%s'?", snapshot_path) },
      function(_, idx)
        write_snapshot = idx == 1
      end
    )
  end

  async(function()
    if write_snapshot then
      await(snapshot.create(snapshot_path, target_plugins))
        :map_ok(function(ok)
          log.info(ok.message)
          if next(ok.failed) then
            log.warn("Couldn't snapshot " .. vim.inspect(ok.failed))
          end
        end)
        :map_err(function(err)
          log.warn(err.message)
        end)
    end
  end)()
end

---Instantly rolls back plugins to a previous state specified by `snapshot_name`
---If `snapshot_name` doesn't exist an error will be displayed
---@param snapshot_name string @name of the snapshot or the absolute path to the snapshot
---@vararg string @ if provided, the only plugins to be rolled back,
---otherwise all the plugins will be rolled back
packer.rollback = function(snapshot_name, ...)
  local args = { ... }
  local a = require 'packer.async'
  local async = a.sync
  local await = a.wait
  local wait_all = a.wait_all
  local snapshot = require 'packer.snapshot'
  local log = require_and_configure 'log'
  local fmt = string.format

  async(function()
    manage_all_plugins()

    local snapshot_path = vim.loop.fs_realpath(util.join_paths(config.snapshot_path, snapshot_name))
      or vim.loop.fs_realpath(snapshot_name)

    if snapshot_path == nil then
      local warn = fmt("Snapshot '%s' is wrong or doesn't exist", snapshot_name)
      log.warn(warn)
      return
    end

    local target_plugins = plugins

    if next(args) ~= nil then -- provided extra args
      target_plugins = vim.tbl_filter(function(plugin)
        for _, plugin_sname in pairs(args) do
          if plugin_sname == plugin.short_name then
            return true
          end
        end
        return false
      end, plugins)
    end

    await(snapshot.rollback(snapshot_path, target_plugins))
      :map_ok(function(ok)
        await(a.main)
        log.info('Rollback to "' .. snapshot_path .. '" completed')
        if next(ok.failed) then
          log.warn("Couldn't rollback " .. vim.inspect(ok.failed))
        end
      end)
      :map_err(function(err)
        await(a.main)
        log.error(err)
      end)

    packer.on_complete()
  end)()
end

packer.config = config

--- Convenience function for simple setup
-- Can be invoked as follows:
--  spec can be a function:
--  packer.startup(function() use 'tjdevries/colorbuddy.vim' end)
--
--  spec can be a table with a function as its first element and config overrides as another
--  element:
--  packer.startup({function() use 'tjdevries/colorbuddy.vim' end, config = { ... }})
--
--  spec can be a table with a table of plugin specifications as its first element, config overrides
--  as another element, and an optional table of Luarocks rock specifications as another element:
--  packer.startup({{'tjdevries/colorbuddy.vim'}, config = { ... }, rocks = { ... }})
packer.startup = function(spec)
  local log = require 'packer.log'
  local user_func = nil
  local user_config = nil
  local user_plugins = nil
  local user_rocks = nil
  if type(spec) == 'function' then
    user_func = spec
  elseif type(spec) == 'table' then
    if type(spec[1]) == 'function' then
      user_func = spec[1]
    elseif type(spec[1]) == 'table' then
      user_plugins = spec[1]
      user_rocks = spec.rocks
    else
      log.error 'You must provide a function or table of specifications as the first element of the argument to startup!'
      return
    end

    -- NOTE: It might be more convenient for users to allow arbitrary config keys to be specified
    -- and to merge them, but I feel that only avoids a single layer of nesting and adds more
    -- complication here, so I'm not sure if the benefit justifies the cost
    user_config = spec.config
  end

  packer.init(user_config)
  packer.reset()
  log = require_and_configure 'log'

  if user_func then
    setfenv(user_func, vim.tbl_extend('force', getfenv(), { use = packer.use, use_rocks = packer.use_rocks }))
    local status, err = pcall(user_func, packer.use, packer.use_rocks)
    if not status then
      log.error('Failure running setup function: ' .. vim.inspect(err))
      error(err)
    end
  else
    packer.use(user_plugins)
    if user_rocks then
      packer.use_rocks(user_rocks)
    end
  end

  if config.snapshot ~= nil then
    packer.rollback(config.snapshot)
  end

  return packer
end

return packer
```

## File: `lua/packer/async.lua`
```
-- Adapted from https://ms-jpq.github.io/neovim-async-tutorial/
local log = require 'packer.log'
local yield = coroutine.yield
local resume = coroutine.resume
local thread_create = coroutine.create

local function EMPTY_CALLBACK() end
local function step(func, callback)
  local thread = thread_create(func)
  local tick = nil
  tick = function(...)
    local ok, val = resume(thread, ...)
    if ok then
      if type(val) == 'function' then
        val(tick)
      else
        (callback or EMPTY_CALLBACK)(val)
      end
    else
      log.error('Error in coroutine: ' .. val);
      (callback or EMPTY_CALLBACK)(nil)
    end
  end

  tick()
end

local function wrap(func)
  return function(...)
    local params = { ... }
    return function(tick)
      params[#params + 1] = tick
      return func(unpack(params))
    end
  end
end

local function join(...)
  local thunks = { ... }
  local thunk_all = function(s)
    if #thunks == 0 then
      return s()
    end
    local to_go = #thunks
    local results = {}
    for i, thunk in ipairs(thunks) do
      local callback = function(...)
        results[i] = { ... }
        if to_go == 1 then
          s(unpack(results))
        else
          to_go = to_go - 1
        end
      end

      thunk(callback)
    end
  end

  return thunk_all
end

local function wait_all(...)
  return yield(join(...))
end

local function pool(n, interrupt_check, ...)
  local thunks = { ... }
  return function(s)
    if #thunks == 0 then
      return s()
    end
    local remaining = { select(n + 1, unpack(thunks)) }
    local results = {}
    local to_go = #thunks
    local make_callback = nil
    make_callback = function(idx, left)
      local i = (left == nil) and idx or (idx + left)
      return function(...)
        results[i] = { ... }
        to_go = to_go - 1
        if to_go == 0 then
          s(unpack(results))
        elseif not interrupt_check or not interrupt_check() then
          if remaining and #remaining > 0 then
            local next_task = table.remove(remaining)
            next_task(make_callback(n, #remaining + 1))
          end
        end
      end
    end

    for i = 1, math.min(n, #thunks) do
      local thunk = thunks[i]
      thunk(make_callback(i))
    end
  end
end

local function wait_pool(limit, ...)
  return yield(pool(limit, false, ...))
end

local function interruptible_wait_pool(limit, interrupt_check, ...)
  return yield(pool(limit, interrupt_check, ...))
end

local function main(f)
  vim.schedule(f)
end

local M = {
  --- Wrapper for functions that do not take a callback to make async functions
  sync = wrap(step),
  --- Alias for yielding to await the result of an async function
  wait = yield,
  --- Await the completion of a full set of async functions
  wait_all = wait_all,
  --- Await the completion of a full set of async functions, with a limit on how many functions can
  --  run simultaneously
  wait_pool = wait_pool,
  --- Like wait_pool, but additionally checks at every function completion to see if a condition is
  --  met indicating that it should keep running the remaining tasks
  interruptible_wait_pool = interruptible_wait_pool,
  --- Wrapper for functions that do take a callback to make async functions
  wrap = wrap,
  --- Convenience function to ensure a function runs on the main "thread" (i.e. for functions which
  --  use Neovim functions, etc.)
  main = main,
}

return M
```

## File: `lua/packer/clean.lua`
```
local plugin_utils = require 'packer.plugin_utils'
local a = require 'packer.async'
local display = require 'packer.display'
local log = require 'packer.log'
local util = require 'packer.util'

local await = a.wait
local async = a.sync

local config

local PLUGIN_OPTIONAL_LIST = 1
local PLUGIN_START_LIST = 2

local function is_dirty(plugin, typ)
  return (plugin.opt and typ == PLUGIN_START_LIST) or (not plugin.opt and typ == PLUGIN_OPTIONAL_LIST)
end

-- Find and remove any plugins not currently configured for use
local clean_plugins = function(_, plugins, fs_state, results)
  return async(function()
    log.debug 'Starting clean'
    local dirty_plugins = {}
    results = results or {}
    results.removals = results.removals or {}
    local opt_plugins = vim.deepcopy(fs_state.opt)
    local start_plugins = vim.deepcopy(fs_state.start)
    local missing_plugins = fs_state.missing
    -- test for dirty / 'missing' plugins
    for _, plugin_config in pairs(plugins) do
      local path = plugin_config.install_path
      local plugin_source = nil
      if opt_plugins[path] then
        plugin_source = PLUGIN_OPTIONAL_LIST
        opt_plugins[path] = nil
      elseif start_plugins[path] then
        plugin_source = PLUGIN_START_LIST
        start_plugins[path] = nil
      end

      -- We don't want to report paths which don't exist for removal; that will confuse people
      local path_exists = false
      if missing_plugins[plugin_config.short_name] or plugin_config.disable then
        path_exists = vim.loop.fs_stat(path) ~= nil
      end

      local plugin_missing = path_exists and missing_plugins[plugin_config.short_name]
      local disabled_but_installed = path_exists and plugin_config.disable
      if plugin_missing or is_dirty(plugin_config, plugin_source) or disabled_but_installed then
        dirty_plugins[#dirty_plugins + 1] = path
      end
    end

    -- Any path which was not set to `nil` above will be set to dirty here
    local function mark_remaining_as_dirty(plugin_list)
      for path, _ in pairs(plugin_list) do
        dirty_plugins[#dirty_plugins + 1] = path
      end
    end

    mark_remaining_as_dirty(opt_plugins)
    mark_remaining_as_dirty(start_plugins)
    if next(dirty_plugins) then
      local lines = {}
      for _, path in ipairs(dirty_plugins) do
        table.insert(lines, '  - ' .. path)
      end
      await(a.main)
      if config.autoremove or await(display.ask_user('Removing the following directories. OK? (y/N)', lines)) then
        results.removals = dirty_plugins
        log.debug('Removed ' .. vim.inspect(dirty_plugins))
        for _, path in ipairs(dirty_plugins) do
          local result = vim.fn.delete(path, 'rf')
          if result == -1 then
            log.warn('Could not remove ' .. path)
          end
        end
      else
        log.warn 'Cleaning cancelled!'
      end
    else
      log.info 'Already clean!'
    end
  end)
end

local function cfg(_config)
  config = _config
end

local clean = setmetatable({ cfg = cfg }, { __call = clean_plugins })
return clean
```

## File: `lua/packer/compile.lua`
```
-- Compiling plugin specifications to Lua for lazy-loading
local util = require 'packer.util'
local log = require 'packer.log'
local fmt = string.format
local luarocks = require 'packer.luarocks'

local config
local function cfg(_config)
  config = _config.profile
end

local feature_guard = [[
if !has('nvim-0.5')
  echohl WarningMsg
  echom "Invalid Neovim version for packer.nvim!"
  echohl None
  finish
endif

packadd packer.nvim

try
]]

local feature_guard_lua = [[
if vim.api.nvim_call_function('has', {'nvim-0.5'}) ~= 1 then
  vim.api.nvim_command('echohl WarningMsg | echom "Invalid Neovim version for packer.nvim! | echohl None"')
  return
end

vim.api.nvim_command('packadd packer.nvim')

local no_errors, error_msg = pcall(function()
]]

local enter_packer_compile = [[
_G._packer = _G._packer or {}
_G._packer.inside_compile = true
]]

local exit_packer_compile = [[

_G._packer.inside_compile = false
if _G._packer.needs_bufread == true then
  vim.cmd("doautocmd BufRead")
end
_G._packer.needs_bufread = false
]]

local catch_errors = [[
catch
  echohl ErrorMsg
  echom "Error in packer_compiled: " .. v:exception
  echom "Please check your config for correctness"
  echohl None
endtry
]]

local catch_errors_lua = [[
end)

if not no_errors then
  error_msg = error_msg:gsub('"', '\\"')
  vim.api.nvim_command('echohl ErrorMsg | echom "Error in packer_compiled: '..error_msg..'" | echom "Please check your config for correctness" | echohl None')
end
]]

---@param should_profile boolean
---@return string
local profile_time = function(should_profile)
  return fmt(
    [[
local time
local profile_info
local should_profile = %s
if should_profile then
  local hrtime = vim.loop.hrtime
  profile_info = {}
  time = function(chunk, start)
    if start then
      profile_info[chunk] = hrtime()
    else
      profile_info[chunk] = (hrtime() - profile_info[chunk]) / 1e6
    end
  end
else
  time = function(chunk, start) end
end
]],
    vim.inspect(should_profile)
  )
end

local profile_output = [[
local function save_profiles(threshold)
  local sorted_times = {}
  for chunk_name, time_taken in pairs(profile_info) do
    sorted_times[#sorted_times + 1] = {chunk_name, time_taken}
  end
  table.sort(sorted_times, function(a, b) return a[2] > b[2] end)
  local results = {}
  for i, elem in ipairs(sorted_times) do
    if not threshold or threshold and elem[2] > threshold then
      results[i] = elem[1] .. ' took ' .. elem[2] .. 'ms'
    end
  end
  if threshold then
    table.insert(results, '(Only showing plugins that took longer than ' .. threshold .. ' ms ' .. 'to load)')
  end

  _G._packer.profile_output = results
end
]]

---@param threshold number
---@return string
local conditionally_output_profile = function(threshold)
  if threshold then
    return fmt(
      [[
if should_profile then save_profiles(%d) end
]],
      threshold
    )
  else
    return [[
if should_profile then save_profiles() end
]]
  end
end

local try_loadstring = [[
local function try_loadstring(s, component, name)
  local success, result = pcall(loadstring(s), name, _G.packer_plugins[name])
  if not success then
    vim.schedule(function()
      vim.api.nvim_notify('packer.nvim: Error running ' .. component .. ' for ' .. name .. ': ' .. result, vim.log.levels.ERROR, {})
    end)
  end
  return result
end
]]

local module_loader = [[
local lazy_load_called = {['packer.load'] = true}
local function lazy_load_module(module_name)
  local to_load = {}
  if lazy_load_called[module_name] then return nil end
  lazy_load_called[module_name] = true
  for module_pat, plugin_name in pairs(module_lazy_loads) do
    if not _G.packer_plugins[plugin_name].loaded and string.match(module_name, module_pat) then
      to_load[#to_load + 1] = plugin_name
    end
  end

  if #to_load > 0 then
    require('packer.load')(to_load, {module = module_name}, _G.packer_plugins)
    local loaded_mod = package.loaded[module_name]
    if loaded_mod then
      return function(modname) return loaded_mod end
    end
  end
end

if not vim.g.packer_custom_loader_enabled then
  table.insert(package.loaders, 1, lazy_load_module)
  vim.g.packer_custom_loader_enabled = true
end
]]

local function timed_chunk(chunk, name, output_table)
  output_table = output_table or {}
  output_table[#output_table + 1] = 'time([[' .. name .. ']], true)'
  if type(chunk) == 'string' then
    output_table[#output_table + 1] = chunk
  else
    vim.list_extend(output_table, chunk)
  end

  output_table[#output_table + 1] = 'time([[' .. name .. ']], false)'
  return output_table
end

local function dump_loaders(loaders)
  local result = vim.deepcopy(loaders)
  for k, _ in pairs(result) do
    if result[k].only_setup or result[k].only_sequence then
      result[k].loaded = true
    end
    result[k].only_setup = nil
    result[k].only_sequence = nil
  end

  return vim.inspect(result)
end

local function make_try_loadstring(item, chunk, name)
  local bytecode = string.dump(item, true)
  local executable_string = 'try_loadstring(' .. vim.inspect(bytecode) .. ', "' .. chunk .. '", "' .. name .. '")'
  return executable_string, bytecode
end

local after_plugin_pattern = table.concat({ 'after', 'plugin', [[**/*.\(vim\|lua\)]] }, util.get_separator())
local function detect_after_plugin(name, plugin_path)
  local path = plugin_path .. util.get_separator() .. after_plugin_pattern
  local glob_ok, files = pcall(vim.fn.glob, path, false, true)
  if not glob_ok then
    if string.find(files, 'E77') then
      return { path }
    else
      log.error('Error compiling ' .. name .. ': ' .. vim.inspect(files))
      error(files)
    end
  elseif #files > 0 then
    return files
  end

  return nil
end

local ftdetect_patterns = {
  table.concat({ 'ftdetect', [[**/*.\(vim\|lua\)]] }, util.get_separator()),
  table.concat({ 'after', 'ftdetect', [[**/*.\(vim\|lua\)]] }, util.get_separator()),
}
local function detect_ftdetect(name, plugin_path)
  local paths = {
    plugin_path .. util.get_separator() .. ftdetect_patterns[1],
    plugin_path .. util.get_separator() .. ftdetect_patterns[2],
  }
  local source_paths = {}
  for i = 1, 2 do
    local path = paths[i]
    local glob_ok, files = pcall(vim.fn.glob, path, false, true)
    if not glob_ok then
      if string.find(files, 'E77') then
        source_paths[#source_paths + 1] = path
      else
        log.error('Error compiling ' .. name .. ': ' .. vim.inspect(files))
        error(files)
      end
    elseif #files > 0 then
      vim.list_extend(source_paths, files)
    end
  end

  return source_paths
end

local source_dirs = { 'ftdetect', 'ftplugin', 'after/ftdetect', 'after/ftplugin' }
local function detect_bufread(plugin_path)
  local path = plugin_path
  for i = 1, 4 do
    if #vim.fn.finddir(source_dirs[i], path) > 0 then
      return true
    end
  end
  return false
end

local function make_loaders(_, plugins, output_lua, should_profile)
  local loaders = {}
  local configs = {}
  local rtps = {}
  local setup = {}
  local fts = {}
  local events = {}
  local condition_ids = {}
  local commands = {}
  local keymaps = {}
  local after = {}
  local fns = {}
  local ftdetect_paths = {}
  local module_lazy_loads = {}
  for name, plugin in pairs(plugins) do
    if not plugin.disable then
      plugin.simple_load = true
      local quote_name = "'" .. name .. "'"
      if plugin.config and not plugin.executable_config then
        plugin.simple_load = false
        plugin.executable_config = {}
        if type(plugin.config) ~= 'table' then
          plugin.config = { plugin.config }
        end
        for i, config_item in ipairs(plugin.config) do
          local executable_string = config_item
          if type(config_item) == 'function' then
            local bytecode
            executable_string, bytecode = make_try_loadstring(config_item, 'config', name)
            plugin.config[i] = bytecode
          end

          table.insert(plugin.executable_config, executable_string)
        end
      end

      local path = plugin.install_path
      if plugin.rtp then
        path = util.join_paths(plugin.install_path, plugin.rtp)
        table.insert(rtps, path)
      end

      loaders[name] = {
        loaded = not plugin.opt,
        config = plugin.config,
        path = path,
        only_sequence = plugin.manual_opt == nil,
        only_setup = false,
      }

      if plugin.opt then
        plugin.simple_load = false
        loaders[name].after_files = detect_after_plugin(name, loaders[name].path)
        if plugin.bufread ~= nil then
          loaders[name].needs_bufread = plugin.bufread
        else
          loaders[name].needs_bufread = detect_bufread(loaders[name].path)
        end
      end

      if plugin.setup then
        plugin.simple_load = false
        if type(plugin.setup) ~= 'table' then
          plugin.setup = { plugin.setup }
        end
        for i, setup_item in ipairs(plugin.setup) do
          if type(setup_item) == 'function' then
            plugin.setup[i], _ = make_try_loadstring(setup_item, 'setup', name)
          end
        end

        loaders[name].only_setup = plugin.manual_opt == nil
        setup[name] = plugin.setup
      end

      -- Keep this as first opt loader to maintain only_cond ?
      if plugin.cond ~= nil then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        loaders[name].only_cond = true
        if type(plugin.cond) ~= 'table' then
          plugin.cond = { plugin.cond }
        end

        for _, condition in ipairs(plugin.cond) do
          loaders[name].cond = {}
          if type(condition) == 'function' then
            _, condition = make_try_loadstring(condition, 'condition', name)
          elseif type(condition) == 'string' then
            condition = 'return ' .. condition
          end

          condition_ids[condition] = condition_ids[condition] or {}
          table.insert(loaders[name].cond, condition)
          table.insert(condition_ids[condition], name)
        end
      end

      -- Add the git URL for displaying in PackerStatus and PackerSync. https://github.com/wbthomason/packer.nvim/issues/542
      loaders[name].url = plugin.url

      if plugin.ft then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        loaders[name].only_cond = false
        vim.list_extend(ftdetect_paths, detect_ftdetect(name, loaders[name].path))
        if type(plugin.ft) == 'string' then
          plugin.ft = { plugin.ft }
        end
        for _, ft in ipairs(plugin.ft) do
          fts[ft] = fts[ft] or {}
          table.insert(fts[ft], quote_name)
        end
      end

      if plugin.event then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        loaders[name].only_cond = false
        if type(plugin.event) == 'string' then
          if not plugin.event:find '%s' then
            plugin.event = { plugin.event .. ' *' }
          else
            plugin.event = { plugin.event }
          end
        end

        for _, event in ipairs(plugin.event) do
          if event:sub(#event, -1) ~= '*' and not event:find '%s' then
            event = event .. ' *'
          end
          events[event] = events[event] or {}
          table.insert(events[event], quote_name)
        end
      end

      if plugin.cmd then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        loaders[name].only_cond = false
        if type(plugin.cmd) == 'string' then
          plugin.cmd = { plugin.cmd }
        end

        loaders[name].commands = {}
        for _, command in ipairs(plugin.cmd) do
          commands[command] = commands[command] or {}
          table.insert(loaders[name].commands, command)
          table.insert(commands[command], quote_name)
        end
      end

      if plugin.keys then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        loaders[name].only_cond = false
        if type(plugin.keys) == 'string' then
          plugin.keys = { plugin.keys }
        end
        loaders[name].keys = {}
        for _, keymap in ipairs(plugin.keys) do
          if type(keymap) == 'string' then
            keymap = { '', keymap }
          end
          keymaps[keymap] = keymaps[keymap] or {}
          table.insert(loaders[name].keys, keymap)
          table.insert(keymaps[keymap], quote_name)
        end
      end

      if plugin.after then
        plugin.simple_load = false
        loaders[name].only_setup = false

        if type(plugin.after) == 'string' then
          plugin.after = { plugin.after }
        end

        for _, other_plugin in ipairs(plugin.after) do
          after[other_plugin] = after[other_plugin] or {}
          table.insert(after[other_plugin], name)
        end
      end

      if plugin.wants then
        plugin.simple_load = false
        if type(plugin.wants) == 'string' then
          plugin.wants = { plugin.wants }
        end
        loaders[name].wants = plugin.wants
      end

      if plugin.fn then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        if type(plugin.fn) == 'string' then
          plugin.fn = { plugin.fn }
        end
        for _, fn in ipairs(plugin.fn) do
          fns[fn] = fns[fn] or {}
          table.insert(fns[fn], quote_name)
        end
      end

      if plugin.module or plugin.module_pattern then
        plugin.simple_load = false
        loaders[name].only_sequence = false
        loaders[name].only_setup = false
        loaders[name].only_cond = false

        if plugin.module then
          if type(plugin.module) == 'string' then
            plugin.module = { plugin.module }
          end

          for _, module_name in ipairs(plugin.module) do
            module_lazy_loads['^' .. vim.pesc(module_name)] = name
          end
        else
          if type(plugin.module_pattern) == 'string' then
            plugin.module_pattern = { plugin.module_pattern }
          end

          for _, module_pattern in ipairs(plugin.module_pattern) do
            module_lazy_loads[module_pattern] = name
          end
        end
      end

      if plugin.config and (not plugin.opt or loaders[name].only_setup) then
        plugin.simple_load = false
        plugin.only_config = true
        configs[name] = plugin.executable_config
      end
    end
  end

  local ft_aucmds = {}
  for ft, names in pairs(fts) do
    table.insert(
      ft_aucmds,
      fmt(
        'vim.cmd [[au FileType %s ++once lua require("packer.load")({%s}, { ft = "%s" }, _G.packer_plugins)]]',
        ft,
        table.concat(names, ', '),
        ft
      )
    )
  end

  local event_aucmds = {}
  for event, names in pairs(events) do
    table.insert(
      event_aucmds,
      fmt(
        'vim.cmd [[au %s ++once lua require("packer.load")({%s}, { event = "%s" }, _G.packer_plugins)]]',
        event,
        table.concat(names, ', '),
        event:gsub([[\]], [[\\]])
      )
    )
  end

  local config_lines = {}
  for name, plugin_config in pairs(configs) do
    local lines = { '-- Config for: ' .. name }
    timed_chunk(plugin_config, 'Config for ' .. name, lines)
    vim.list_extend(config_lines, lines)
  end

  local rtp_line = ''
  for _, rtp in ipairs(rtps) do
    rtp_line = rtp_line .. ' .. ",' .. vim.fn.escape(rtp, '\\,') .. '"'
  end

  if rtp_line ~= '' then
    rtp_line = 'vim.o.runtimepath = vim.o.runtimepath' .. rtp_line
  end

  local setup_lines = {}
  for name, plugin_setup in pairs(setup) do
    local lines = { '-- Setup for: ' .. name }
    timed_chunk(plugin_setup, 'Setup for ' .. name, lines)
    if loaders[name].only_setup then
      timed_chunk('vim.cmd [[packadd ' .. name .. ']]', 'packadd for ' .. name, lines)
    end

    vim.list_extend(setup_lines, lines)
  end

  local conditionals = {}
  for _, names in pairs(condition_ids) do
    for _, name in ipairs(names) do
      if loaders[name].only_cond then
        timed_chunk(
          fmt('  require("packer.load")({"%s"}, {}, _G.packer_plugins)', name),
          'Conditional loading of ' .. name,
          conditionals
        )
      end
    end
  end

  local command_defs = {}
  for command, names in pairs(commands) do
    local command_line
    if string.match(command, '^%w+$') then
      -- Better command completions here are due to @folke and @lewis6991
      command_line = fmt(
        [[pcall(vim.api.nvim_create_user_command, '%s', function(cmdargs)
          require('packer.load')({%s}, { cmd = '%s', l1 = cmdargs.line1, l2 = cmdargs.line2, bang = cmdargs.bang, args = cmdargs.args, mods = cmdargs.mods }, _G.packer_plugins)
        end,
        {nargs = '*', range = true, bang = true, complete = function()
          require('packer.load')({%s}, {}, _G.packer_plugins)
          return vim.fn.getcompletion('%s ', 'cmdline')
      end})]],
        command,
        table.concat(names, ', '),
        command,
        table.concat(names, ', '),
        command,
        command
      )
    else
      command_line = fmt(
        'pcall(vim.cmd, [[au CmdUndefined %s ++once lua require"packer.load"({%s}, {}, _G.packer_plugins)]])',
        command,
        table.concat(names, ', ')
      )
    end
    command_defs[#command_defs + 1] = command_line
  end

  local keymap_defs = {}
  for keymap, names in pairs(keymaps) do
    local prefix = nil
    if keymap[1] ~= 'i' then
      prefix = ''
    end
    local escaped_map_lt = string.gsub(keymap[2], '<', '<lt>')
    local escaped_map = string.gsub(escaped_map_lt, '([\\"])', '\\%1')
    local keymap_line = fmt(
      'vim.cmd [[%snoremap <silent> %s <cmd>lua require("packer.load")({%s}, { keys = "%s"%s }, _G.packer_plugins)<cr>]]',
      keymap[1],
      keymap[2],
      table.concat(names, ', '),
      escaped_map,
      prefix == nil and '' or (', prefix = "' .. prefix .. '"')
    )

    table.insert(keymap_defs, keymap_line)
  end

  local sequence_loads = {}
  for pre, posts in pairs(after) do
    if plugins[pre] == nil then
      error(string.format('Dependency %s for %s not found', pre, vim.inspect(posts)))
    end

    if plugins[pre].opt then
      loaders[pre].after = posts
    elseif plugins[pre].only_config then
      loaders[pre].after = posts
      loaders[pre].only_sequence = true
      loaders[pre].only_config = true
    end

    if plugins[pre].simple_load or plugins[pre].opt or plugins[pre].only_config then
      for _, name in ipairs(posts) do
        loaders[name].load_after = {}
        sequence_loads[name] = sequence_loads[name] or {}
        table.insert(sequence_loads[name], pre)
      end
    end
  end

  local fn_aucmds = {}
  for fn, names in pairs(fns) do
    table.insert(
      fn_aucmds,
      fmt(
        'vim.cmd[[au FuncUndefined %s ++once lua require("packer.load")({%s}, {}, _G.packer_plugins)]]',
        fn,
        table.concat(names, ', ')
      )
    )
  end

  local sequence_lines = {}
  local graph = {}
  for name, precedents in pairs(sequence_loads) do
    graph[name] = graph[name] or { in_links = {}, out_links = {} }
    for _, pre in ipairs(precedents) do
      graph[pre] = graph[pre] or { in_links = {}, out_links = {} }
      graph[name].in_links[pre] = true
      table.insert(graph[pre].out_links, name)
    end
  end

  local frontier = {}
  for name, links in pairs(graph) do
    if next(links.in_links) == nil then
      table.insert(frontier, name)
    end
  end

  while next(frontier) ~= nil do
    local plugin = table.remove(frontier)
    if loaders[plugin].only_sequence and not (loaders[plugin].only_setup or loaders[plugin].only_config) then
      table.insert(sequence_lines, 'vim.cmd [[ packadd ' .. plugin .. ' ]]')
      if plugins[plugin].config then
        local lines = { '', '-- Config for: ' .. plugin }
        vim.list_extend(lines, plugins[plugin].executable_config)
        table.insert(lines, '')
        vim.list_extend(sequence_lines, lines)
      end
    end

    for _, name in ipairs(graph[plugin].out_links) do
      if not loaders[plugin].only_sequence then
        loaders[name].only_sequence = false
        loaders[name].load_after[plugin] = true
      end

      graph[name].in_links[plugin] = nil
      if next(graph[name].in_links) == nil then
        table.insert(frontier, name)
      end
    end

    graph[plugin] = nil
  end

  if next(graph) then
    log.warn 'Cycle detected in sequenced loads! Load order may be incorrect'
    -- TODO: This should actually just output the cycle, then continue with toposort. But I'm too
    -- lazy to do that right now, so.
    for plugin, _ in pairs(graph) do
      table.insert(sequence_lines, 'vim.cmd [[ packadd ' .. plugin .. ' ]]')
      if plugins[plugin].config then
        local lines = { '-- Config for: ' .. plugin }
        vim.list_extend(lines, plugins[plugin].config)
        vim.list_extend(sequence_lines, lines)
      end
    end
  end

  -- Output everything:

  -- First, the Lua code
  local result = { (output_lua and '--' or '"') .. ' Automatically generated packer.nvim plugin loader code\n' }
  if output_lua then
    table.insert(result, feature_guard_lua)
  else
    table.insert(result, feature_guard)
    table.insert(result, 'lua << END')
  end
  table.insert(result, enter_packer_compile)
  table.insert(result, profile_time(should_profile))
  table.insert(result, profile_output)
  timed_chunk(luarocks.generate_path_setup(), 'Luarocks path setup', result)
  timed_chunk(try_loadstring, 'try_loadstring definition', result)
  timed_chunk(fmt('_G.packer_plugins = %s\n', dump_loaders(loaders)), 'Defining packer_plugins', result)
  -- Then the runtimepath line
  if rtp_line ~= '' then
    table.insert(result, '-- Runtimepath customization')
    timed_chunk(rtp_line, 'Runtimepath customization', result)
  end

  -- Then the module lazy loads
  if next(module_lazy_loads) then
    table.insert(result, 'local module_lazy_loads = ' .. vim.inspect(module_lazy_loads))
    table.insert(result, module_loader)
  end

  -- Then setups, configs, and conditionals
  if next(setup_lines) then
    vim.list_extend(result, setup_lines)
  end
  if next(config_lines) then
    vim.list_extend(result, config_lines)
  end
  if next(conditionals) then
    table.insert(result, '-- Conditional loads')
    vim.list_extend(result, conditionals)
  end

  -- The sequenced loads
  if next(sequence_lines) then
    table.insert(result, '-- Load plugins in order defined by `after`')
    timed_chunk(sequence_lines, 'Sequenced loading', result)
  end

  -- The command and keymap definitions
  if next(command_defs) then
    table.insert(result, '\n-- Command lazy-loads')
    timed_chunk(command_defs, 'Defining lazy-load commands', result)
    table.insert(result, '')
  end

  if next(keymap_defs) then
    table.insert(result, '-- Keymap lazy-loads')
    timed_chunk(keymap_defs, 'Defining lazy-load keymaps', result)
    table.insert(result, '')
  end

  -- The filetype, event and function autocommands
  local some_ft = next(ft_aucmds) ~= nil
  local some_event = next(event_aucmds) ~= nil
  local some_fn = next(fn_aucmds) ~= nil
  if some_ft or some_event or some_fn then
    table.insert(result, 'vim.cmd [[augroup packer_load_aucmds]]\nvim.cmd [[au!]]')
  end

  if some_ft then
    table.insert(result, '  -- Filetype lazy-loads')
    timed_chunk(ft_aucmds, 'Defining lazy-load filetype autocommands', result)
  end

  if some_event then
    table.insert(result, '  -- Event lazy-loads')
    timed_chunk(event_aucmds, 'Defining lazy-load event autocommands', result)
  end

  if some_fn then
    table.insert(result, '  -- Function lazy-loads')
    timed_chunk(fn_aucmds, 'Defining lazy-load function autocommands', result)
  end

  if some_ft or some_event or some_fn then
    table.insert(result, 'vim.cmd("augroup END")')
  end
  if next(ftdetect_paths) then
    table.insert(result, 'vim.cmd [[augroup filetypedetect]]')
    for _, path in ipairs(ftdetect_paths) do
      local escaped_path = vim.fn.escape(path, ' ')
      timed_chunk('vim.cmd [[source ' .. escaped_path .. ']]', 'Sourcing ftdetect script at: ' .. escaped_path, result)
    end

    table.insert(result, 'vim.cmd("augroup END")')
  end

  table.insert(result, exit_packer_compile)

  table.insert(result, conditionally_output_profile(config.threshold))
  if output_lua then
    table.insert(result, catch_errors_lua)
  else
    table.insert(result, 'END\n')
    table.insert(result, catch_errors)
  end
  return table.concat(result, '\n')
end

local compile = setmetatable({ cfg = cfg }, { __call = make_loaders })

compile.opt_keys = { 'after', 'cmd', 'ft', 'keys', 'event', 'cond', 'setup', 'fn', 'module', 'module_pattern' }

return compile
```

## File: `lua/packer/display.lua`
```
local api = vim.api
local log = require 'packer.log'
local a = require 'packer.async'
local plugin_utils = require 'packer.plugin_utils'
local fmt = string.format

local function interactive(config)
  return not config.non_interactive and #api.nvim_list_uis() > 0
end

-- Temporary wrappers to compensate for the updated extmark API, until most people have updated to
-- the latest HEAD (2020-09-04)
local function set_extmark(buf, ns, id, line, col)
  if not api.nvim_buf_is_valid(buf) then
    return
  end
  local opts = { id = id }
  local result, mark_id = pcall(api.nvim_buf_set_extmark, buf, ns, line, col, opts)
  if result then
    return mark_id
  end
  -- We must be in an older version of Neovim
  if not id then
    id = 0
  end
  return api.nvim_buf_set_extmark(buf, ns, id, line, col, {})
end

local function get_extmark_by_id(buf, ns, id)
  local result, line, col = pcall(api.nvim_buf_get_extmark_by_id, buf, ns, id, {})
  if result then
    return line, col
  else
    log.error('Failed to get extmark: ' .. line)
  end
  -- We must be in an older version of Neovim
  return api.nvim_buf_get_extmark_by_id(buf, ns, id)
end

local function strip_newlines(raw_lines)
  local lines = {}
  for _, line in ipairs(raw_lines) do
    for _, chunk in ipairs(vim.split(line, '\n')) do
      table.insert(lines, chunk)
    end
  end

  return lines
end

local function unpack_config_value(value, value_type, formatter)
  if value_type == 'string' then
    return { value }
  elseif value_type == 'table' then
    local result = {}
    for _, k in ipairs(value) do
      local item = formatter and formatter(k) or k
      table.insert(result, fmt('  - %s', item))
    end
    return result
  end
  return ''
end

local function format_keys(value)
  local value_type = type(value)
  local mapping = value_type == 'string' and value or value[2]
  local mode = value[1] ~= '' and 'mode: ' .. value[1] or ''
  local line = fmt('"%s", %s', mapping, mode)
  return line
end

local function format_cmd(value)
  return fmt('"%s"', value)
end

---format a configuration value of unknown type into a string or list of strings
---@param key string
---@param value any
---@return string|string[]
local function format_values(key, value)
  local value_type = type(value)
  if key == 'path' then
    local is_opt = value:match 'opt' ~= nil
    return { fmt('"%s"', vim.fn.fnamemodify(value, ':~')), fmt('opt: %s', vim.inspect(is_opt)) }
  elseif key == 'url' then
    return fmt('"%s"', value)
  elseif key == 'keys' then
    return unpack_config_value(value, value_type, format_keys)
  elseif key == 'commands' then
    return unpack_config_value(value, value_type, format_cmd)
  else
    return vim.inspect(value)
  end
end

local status_keys = {
  'path',
  'url',
  'commands',
  'keys',
  'module',
  'as',
  'ft',
  'event',
  'rocks',
  'branch',
  'commit',
  'tag',
  'lock',
}

local config = nil
local keymaps = {
  quit = { rhs = '<cmd>lua require"packer.display".quit()<cr>', action = 'quit' },
  diff = { rhs = '<cmd>lua require"packer.display".diff()<cr>', action = 'show the diff' },
  toggle_update = { rhs = '<cmd>lua require"packer.display".toggle_update()<cr>', action = 'toggle update' },
  continue = { rhs = '<cmd>lua require"packer.display".continue()<cr>', action = 'continue with updates' },
  toggle_info = {
    rhs = '<cmd>lua require"packer.display".toggle_info()<cr>',
    action = 'show more info',
  },
  prompt_revert = {
    rhs = '<cmd>lua require"packer.display".prompt_revert()<cr>',
    action = 'revert an update',
  },
  retry = {
    rhs = '<cmd>lua require"packer.display".retry()<cr>',
    action = 'retry failed operations',
  },
}

--- The order of the keys in a dict-like table isn't guaranteed, meaning the display window can
--- potentially show the keybindings in a different order every time
local default_keymap_display_order = {
  'quit',
  'toggle_info',
  'diff',
  'prompt_revert',
  'retry',
}

--- Utility function to prompt a user with a question in a floating window
local function prompt_user(headline, body, callback)
  if not interactive(config) then
    callback(true)
    return
  end

  local buf = api.nvim_create_buf(false, true)
  local longest_line = 0
  for _, line in ipairs(body) do
    local line_length = string.len(line)
    if line_length > longest_line then
      longest_line = line_length
    end
  end

  local width = math.min(longest_line + 2, math.floor(0.9 * vim.o.columns))
  local height = #body + 3
  local x = (vim.o.columns - width) / 2.0
  local y = (vim.o.lines - height) / 2.0
  local pad_width = math.max(math.floor((width - string.len(headline)) / 2.0), 0)
  api.nvim_buf_set_lines(
    buf,
    0,
    -1,
    true,
    vim.list_extend({
      string.rep(' ', pad_width) .. headline .. string.rep(' ', pad_width),
      '',
    }, body)
  )
  api.nvim_buf_set_option(buf, 'modifiable', false)
  local opts = {
    relative = 'editor',
    width = width,
    height = height,
    col = x,
    row = y,
    focusable = false,
    style = 'minimal',
    border = config.prompt_border,
    noautocmd = true,
  }

  local win = api.nvim_open_win(buf, false, opts)
  local check = vim.loop.new_prepare()
  local prompted = false
  vim.loop.prepare_start(
    check,
    vim.schedule_wrap(function()
      if not api.nvim_win_is_valid(win) then
        return
      end
      vim.loop.prepare_stop(check)
      if not prompted then
        prompted = true
        local ans = string.lower(vim.fn.input 'OK to remove? [y/N] ') == 'y'
        api.nvim_win_close(win, true)
        callback(ans)
      end
    end)
  )
end

local make_update_msg = function(symbol, status, plugin_name, plugin)
  return fmt(
    ' %s %s %s: %s..%s',
    symbol,
    status,
    plugin_name,
    plugin.revs[1],
    plugin.revs[2]
  )
end

local display = {}
local display_mt = {
  --- Check if we have a valid display window
  valid_display = function(self)
    return self and self.interactive and api.nvim_buf_is_valid(self.buf) and api.nvim_win_is_valid(self.win)
  end,
  --- Update the text of the display buffer
  set_lines = function(self, start_idx, end_idx, lines)
    if not self:valid_display() then
      return
    end
    api.nvim_buf_set_option(self.buf, 'modifiable', true)
    api.nvim_buf_set_lines(self.buf, start_idx, end_idx, true, lines)
    api.nvim_buf_set_option(self.buf, 'modifiable', false)
  end,
  get_lines = function(self, start_idx, end_idx)
    if not self:valid_display() then
      return
    end
    return api.nvim_buf_get_lines(self.buf, start_idx, end_idx, true)
  end,
  get_current_line = function(self)
    if not self:valid_display() then
      return
    end
    return api.nvim_get_current_line()
  end,
  --- Start displaying a new task
  task_start = vim.schedule_wrap(function(self, plugin, message)
    if not self:valid_display() then
      return
    end
    if self.marks[plugin] then
      self:task_update(plugin, message)
      return
    end
    display.status.running = true
    self:set_lines(config.header_lines, config.header_lines, {
      fmt(' %s %s: %s', config.working_sym, plugin, message),
    })
    self.marks[plugin] = set_extmark(self.buf, self.ns, nil, config.header_lines, 0)
  end),

  --- Decrement the count of active operations in the headline
  decrement_headline_count = vim.schedule_wrap(function(self)
    if not self:valid_display() then
      return
    end
    local headline = api.nvim_buf_get_lines(self.buf, 0, 1, false)[1]
    local count_start, count_end = string.find(headline, '%d+')
    local count = tonumber(string.sub(headline, count_start, count_end))
    local updated_headline = string.sub(headline, 1, count_start - 1)
      .. tostring(count - 1)
      .. string.sub(headline, count_end + 1)
    api.nvim_buf_set_option(self.buf, 'modifiable', true)
    api.nvim_buf_set_lines(self.buf, 0, 1, false, { updated_headline })
    api.nvim_buf_set_option(self.buf, 'modifiable', false)
  end),

  --- Update a task as having successfully completed
  task_succeeded = vim.schedule_wrap(function(self, plugin, message)
    if not self:valid_display() then
      return
    end
    local line, _ = get_extmark_by_id(self.buf, self.ns, self.marks[plugin])
    self:set_lines(line[1], line[1] + 1, { fmt(' %s %s: %s', config.done_sym, plugin, message) })
    api.nvim_buf_del_extmark(self.buf, self.ns, self.marks[plugin])
    self.marks[plugin] = nil
    self:decrement_headline_count()
  end),

  --- Update a task as having unsuccessfully failed
  task_failed = vim.schedule_wrap(function(self, plugin, message)
    if not self:valid_display() then
      return
    end
    local line, _ = get_extmark_by_id(self.buf, self.ns, self.marks[plugin])
    self:set_lines(line[1], line[1] + 1, { fmt(' %s %s: %s', config.error_sym, plugin, message) })
    api.nvim_buf_del_extmark(self.buf, self.ns, self.marks[plugin])
    self.marks[plugin] = nil
    self:decrement_headline_count()
  end),

  --- Update the status message of a task in progress
  task_update = vim.schedule_wrap(function(self, plugin, message)
    if not self:valid_display() then
      return
    end
    if not self.marks[plugin] then
      return
    end
    local line, _ = get_extmark_by_id(self.buf, self.ns, self.marks[plugin])
    self:set_lines(line[1], line[1] + 1, { fmt(' %s %s: %s', config.working_sym, plugin, message) })
    set_extmark(self.buf, self.ns, self.marks[plugin], line[1], 0)
  end),

  open_preview = function(_, commit, lines)
    if not lines or #lines < 1 then
      return log.warn 'No diff available'
    end
    vim.cmd('pedit ' .. commit)
    vim.cmd [[wincmd P]]
    vim.wo.previewwindow = true
    vim.bo.buftype = 'nofile'
    vim.bo.buflisted = false
    vim.api.nvim_buf_set_lines(0, 0, -1, false, lines)
    vim.api.nvim_buf_set_keymap(0, 'n', 'q', '<cmd>close!<CR>', { silent = true, noremap = true, nowait = true })
    vim.bo.filetype = 'git'
  end,

  --- Update the text of the headline message
  update_headline_message = vim.schedule_wrap(function(self, message)
    if not self:valid_display() then
      return
    end
    local headline = config.title .. ' - ' .. message
    local width = api.nvim_win_get_width(self.win) - 2
    local pad_width = math.max(math.floor((width - string.len(headline)) / 2.0), 0)
    self:set_lines(0, config.header_lines - 1, { string.rep(' ', pad_width) .. headline })
  end),

  --- Setup new syntax group links for the status window
  setup_status_syntax = function(self)
    local highlights = {
      'hi def link packerStatus         Type',
      'hi def link packerStatusCommit   Constant',
      'hi def link packerStatusSuccess  Constant',
      'hi def link packerStatusFail     ErrorMsg',
      'hi def link packerPackageName    Label',
      'hi def link packerPackageNotLoaded    Comment',
      'hi def link packerString         String',
      'hi def link packerBool Boolean',
      'hi def link packerBreakingChange WarningMsg',
    }
    for _, c in ipairs(highlights) do
      vim.cmd(c)
    end
  end,

  setup_profile_syntax = function(_)
    local highlights = {
      'hi def link packerTimeHigh ErrorMsg',
      'hi def link packerTimeMedium WarningMsg',
      'hi def link packerTimeLow String',
      'hi def link packerTimeTrivial Comment',
    }
    for _, c in ipairs(highlights) do
      vim.cmd(c)
    end
  end,

  status = vim.schedule_wrap(function(self, plugins)
    if not self:valid_display() then
      return
    end
    self:setup_status_syntax()
    self:update_headline_message(fmt('Total plugins: %d', vim.tbl_count(plugins)))

    local plugs = {}
    local lines = {}

    local padding = string.rep(' ', 3)
    local rtps = api.nvim_list_runtime_paths()
    for plug_name, plug_conf in pairs(plugins) do
      local load_state = plug_conf.loaded and ''
        or vim.tbl_contains(rtps, plug_conf.path) and ' (manually loaded)'
        or ' (not loaded)'
      local header_lines = { fmt(' %s %s', config.item_sym, plug_name) .. load_state }
      local config_lines = {}
      for key, value in pairs(plug_conf) do
        if vim.tbl_contains(status_keys, key) then
          local details = format_values(key, value)
          if type(details) == 'string' then
            -- insert a position one so that one line details appear above multiline ones
            table.insert(config_lines, 1, fmt('%s%s: %s', padding, key, details))
          else
            details = vim.tbl_map(function(line)
              return padding .. line
            end, details)
            vim.list_extend(config_lines, { fmt('%s%s: ', padding, key), unpack(details) })
          end
          plugs[plug_name] = { lines = config_lines, displayed = false }
        end
      end
      vim.list_extend(lines, header_lines)
    end
    table.sort(lines)
    self.items = plugs
    self:set_lines(config.header_lines, -1, lines)
  end),

  is_previewing = function(self)
    local opts = self.opts or {}
    return opts.preview_updates
  end,

  has_changes = function(self, plugin)
    if plugin.type ~= plugin_utils.git_plugin_type or plugin.revs[1] == plugin.revs[2] then
      return false
    end
    if self:is_previewing() and plugin.commit ~= nil then
      return false
    end
    return true
  end,

  --- Display the final results of an operation
  final_results = vim.schedule_wrap(function(self, results, time, opts)
    self.opts = opts
    if not self:valid_display() then
      return
    end
    local keymap_display_order = {}
    vim.list_extend(keymap_display_order, default_keymap_display_order)
    self.results = results
    self:setup_status_syntax()
    display.status.running = false
    time = tonumber(time)
    self:update_headline_message(fmt('finished in %.3fs', time))
    local raw_lines = {}
    local item_order = {}
    local rocks_items = {}
    if results.removals then
      for _, plugin_dir in ipairs(results.removals) do
        table.insert(item_order, plugin_dir)
        table.insert(raw_lines, fmt(' %s Removed %s', config.removed_sym, plugin_dir))
      end
    end

    if results.moves then
      for plugin, result in pairs(results.moves) do
        table.insert(item_order, plugin)
        table.insert(
          raw_lines,
          fmt(
            ' %s %s %s: %s %s %s',
            result.result.ok and config.done_sym or config.error_sym,
            result.result.ok and 'Moved' or 'Failed to move',
            plugin,
            result.from,
            config.moved_sym,
            result.to
          )
        )
      end
    end

    display.status.any_failed_install = false
    display.status.failed_update_list = {}

    if results.installs then
      for plugin, result in pairs(results.installs) do
        table.insert(item_order, plugin)
        table.insert(
          raw_lines,
          fmt(
            ' %s %s %s',
            result.ok and config.done_sym or config.error_sym,
            result.ok and 'Installed' or 'Failed to install',
            plugin
          )
        )
        display.status.any_failed_install = display.status.any_failed_install or not result.ok
      end
    end

    if results.updates then
      local status_msg = 'Updated'
      if self:is_previewing() then
        status_msg = 'Can update'
        table.insert(keymap_display_order, 1, 'continue')
        table.insert(keymap_display_order, 2, 'toggle_update')
      end
      for plugin_name, result in pairs(results.updates) do
        local plugin = results.plugins[plugin_name]
        local message = {}
        local actual_update = true
        local failed_update = false
        if result.ok then
          if self:has_changes(plugin) then
            table.insert(item_order, plugin_name)
            table.insert(
              message,
              make_update_msg(config.done_sym, status_msg, plugin_name, plugin)
            )
          else
            actual_update = false
            table.insert(message, fmt(' %s %s is already up to date', config.done_sym, plugin_name))
          end
        else
          failed_update = true
          actual_update = false
          table.insert(display.status.failed_update_list, plugin.short_name)
          table.insert(item_order, plugin_name)
          table.insert(message, fmt(' %s Failed to update %s', config.error_sym, plugin_name))
        end

        plugin.actual_update = actual_update
        if actual_update or failed_update then
          vim.list_extend(raw_lines, message)
        end
      end
    end

    if results.luarocks then
      if results.luarocks.installs then
        for package, result in pairs(results.luarocks.installs) do
          if result.err then
            rocks_items[package] = { lines = strip_newlines(result.err.output.data.stderr) }
          end

          table.insert(
            raw_lines,
            fmt(
              ' %s %s %s',
              result.ok and config.done_sym or config.error_sym,
              result.ok and 'Installed' or 'Failed to install',
              package
            )
          )
          display.status.any_failed_install = display.status.any_failed_install or not result.ok
        end
      end

      if results.luarocks.removals then
        for package, result in pairs(results.luarocks.removals) do
          if result.err then
            rocks_items[package] = { lines = strip_newlines(result.err.output.data.stderr) }
          end

          table.insert(
            raw_lines,
            fmt(
              ' %s %s %s',
              result.ok and config.done_sym or config.error_sym,
              result.ok and 'Removed' or 'Failed to remove',
              package
            )
          )
        end
      end
    end

    if #raw_lines == 0 then
      table.insert(raw_lines, ' Everything already up to date!')
    end

    table.insert(raw_lines, '')
    local show_retry = display.status.any_failed_install or #display.status.failed_update_list > 0
    for _, keymap in ipairs(keymap_display_order) do
      if keymaps[keymap].lhs then
        if not (keymap == 'retry') or show_retry then
          table.insert(raw_lines, fmt(" Press '%s' to %s", keymaps[keymap].lhs, keymaps[keymap].action))
        end
      end
    end

    -- Ensure there are no newlines
    local lines = strip_newlines(raw_lines)
    self:set_lines(config.header_lines, -1, lines)
    local plugins = {}
    for plugin_name, plugin in pairs(results.plugins) do
      local plugin_data = { displayed = false, lines = {}, spec = plugin }
      if plugin.output then
        if plugin.output.err and #plugin.output.err > 0 then
          table.insert(plugin_data.lines, '  Errors:')
          for _, line in ipairs(plugin.output.err) do
            line = vim.trim(line)
            if line:find '\n' then
              for sub_line in line:gmatch '[^\r\n]+' do
                table.insert(plugin_data.lines, '    ' .. sub_line)
              end
            else
              table.insert(plugin_data.lines, '    ' .. line)
            end
          end
        end
      end

      if plugin.messages and #plugin.messages > 0 then
        table.insert(plugin_data.lines, fmt('  URL: %s', plugin.url))
        table.insert(plugin_data.lines, '  Commits:')
        for _, msg in ipairs(plugin.messages) do
          for _, line in ipairs(vim.split(msg, '\n')) do
            table.insert(plugin_data.lines, string.rep(' ', 4) .. line)
          end
        end

        table.insert(plugin_data.lines, '')
      end

      if plugin.breaking_commits and #plugin.breaking_commits > 0 then
        vim.cmd('syntax match packerBreakingChange "' .. plugin_name .. '" containedin=packerStatusSuccess')
        for _, commit_hash in ipairs(plugin.breaking_commits) do
          log.warn('Potential breaking change in commit ' .. commit_hash .. ' of ' .. plugin_name)
          vim.cmd('syntax match packerBreakingChange "' .. commit_hash .. '" containedin=packerHash')
        end
      end

      plugins[plugin_name] = plugin_data
    end

    self.items = vim.tbl_extend('keep', plugins, rocks_items)
    self.item_order = item_order
    if config.show_all_info then
      self:show_all_info()
    end
  end),

  --- Toggle the display of detailed information for all plugins in the final results display
  show_all_info = function(self)
    if not self:valid_display() then
      return
    end
    if next(self.items) == nil then
      log.info 'Operations are still running; plugin info is not ready yet'
      return
    end

    local line = config.header_lines + 1
    for _, plugin_name in pairs(self.item_order) do
      local plugin_data = self.items[plugin_name]
      if plugin_data and plugin_data.spec.actual_update and #plugin_data.lines > 0 then
        local next_line
        if config.compact then
          next_line = line + 1
          plugin_data.displayed = false
        else
          self:set_lines(line, line, plugin_data.lines)
          next_line = line + #plugin_data.lines + 1
          plugin_data.displayed = true
        end
        self.marks[plugin_name] = {
          start = set_extmark(self.buf, self.ns, nil, line - 1, 0),
          end_ = set_extmark(self.buf, self.ns, nil, next_line - 1, 0),
        }
        line = next_line
      else
        line = line + 1
      end
    end
  end,

  profile_output = function(self, output)
    self:setup_profile_syntax()
    local result = {}
    for i, line in ipairs(output) do
      result[i] = string.rep(' ', 2) .. line
    end
    self:set_lines(config.header_lines, -1, result)
  end,

  --- Toggle the display of detailed information for a plugin in the final results display
  toggle_info = function(self)
    if not self:valid_display() then
      return
    end
    if self.items == nil or next(self.items) == nil then
      log.info 'Operations are still running; plugin info is not ready yet'
      return
    end

    local plugin_name, cursor_pos = self:find_nearest_plugin()
    if plugin_name == nil then
      log.warn 'No plugin selected!'
      return
    end

    local plugin_data = self.items[plugin_name]
    if plugin_data.displayed then
      self:set_lines(cursor_pos[1], cursor_pos[1] + #plugin_data.lines, {})
      plugin_data.displayed = false
    elseif #plugin_data.lines > 0 then
      self:set_lines(cursor_pos[1], cursor_pos[1], plugin_data.lines)
      plugin_data.displayed = true
    else
      log.info('No further information for ' .. plugin_name)
    end

    api.nvim_win_set_cursor(0, cursor_pos)
  end,

  diff = function(self)
    if not self:valid_display() then
      return
    end
    if next(self.items) == nil then
      log.info 'Operations are still running; plugin info is not ready yet'
      return
    end

    local plugin_name, _ = self:find_nearest_plugin()
    if plugin_name == nil then
      log.warn 'No plugin selected!'
      return
    end

    if not self.items[plugin_name] or not self.items[plugin_name].spec then
      log.warn 'Plugin not available!'
      return
    end

    local plugin_data = self.items[plugin_name].spec
    local current_line = self:get_current_line()
    local commit_pattern = [[[0-9a-f]\{7,9}]]
    local commit_single_pattern = string.format([[\<%s\>]], commit_pattern)
    local commit_range_pattern = string.format([[\<%s\.\.%s\>]], commit_pattern, commit_pattern)
    local commit = vim.fn.matchstr(current_line, commit_range_pattern)
    if commit == '' then
      commit = vim.fn.matchstr(current_line, commit_single_pattern)
    end
    if commit == '' then
      log.warn 'Unable to find the diff for this line'
      return
    end
    plugin_data.diff(commit, function(lines, err)
      if err then
        return log.warn 'Unable to get diff!'
      end
      vim.schedule(function()
        self:open_preview(commit, lines)
      end)
    end)
  end,

  toggle_update = function(self)
    if not self:is_previewing() then
      return
    end
    local plugin_name, _ = self:find_nearest_plugin()
    local plugin = self.items[plugin_name]
    if not plugin then
      log.warn 'Plugin not available!'
      return
    end
    local plugin_data = plugin.spec
    if not plugin_data.actual_update then
      return
    end
    plugin_data.ignore_update = not plugin_data.ignore_update
    self:toggle_plugin_text(plugin_name, plugin_data)
  end,

  toggle_plugin_text = function(self, plugin_name, plugin_data)
    local mark_ids = self.marks[plugin_name]
    local start_idx = get_extmark_by_id(self.buf, self.ns, mark_ids.start)[1]
    local symbol
    local status_msg
    if plugin_data.ignore_update then
      status_msg = [[Won't update]]
      symbol = config.item_sym
    else
      status_msg = 'Can update'
      symbol = config.done_sym
    end
    self:set_lines(
      start_idx,
      start_idx + 1,
      {make_update_msg(symbol, status_msg, plugin_name, plugin_data)}
    )
    -- NOTE we need to reset the mark
    self.marks[plugin_name].start = set_extmark(self.buf, self.ns, nil, start_idx, 0)
  end,

  continue = function(self)
    if not self:is_previewing() then
      return
    end
    local plugins = {}
    for plugin_name, _ in pairs(self.results.updates) do
      local plugin_data = self.items[plugin_name].spec
      if plugin_data.actual_update and not plugin_data.ignore_update then
        table.insert(plugins, plugin_data.short_name)
      end
    end
    if #plugins > 0 then
      require('packer').update({pull_head = true, preview_updates = false}, unpack(plugins))
    else
      log.warn 'No plugins selected!'
    end
  end,

  --- Prompt a user to revert the latest update for a plugin
  prompt_revert = function(self)
    if not self:valid_display() then
      return
    end
    if next(self.items) == nil then
      log.info 'Operations are still running; plugin info is not ready yet'
      return
    end

    local plugin_name, _ = self:find_nearest_plugin()
    if plugin_name == nil then
      log.warn 'No plugin selected!'
      return
    end

    local plugin_data = self.items[plugin_name].spec
    if plugin_data.actual_update then
      prompt_user('Revert update for ' .. plugin_name .. '?', {
        'Do you want to revert '
          .. plugin_name
          .. ' from '
          .. plugin_data.revs[2]
          .. ' to '
          .. plugin_data.revs[1]
          .. '?',
      }, function(ans)
        if ans then
          local r = plugin_data.revert_last()
          if r.ok then
            log.info('Reverted update for ' .. plugin_name)
          else
            log.error('Reverting update for ' .. plugin_name .. ' failed!')
          end
        end
      end)
    else
      log.warn(plugin_name .. " wasn't updated; can't revert!")
    end
  end,

  is_plugin_line = function(self, line)
    for _, sym in pairs { config.item_sym, config.done_sym, config.working_sym, config.error_sym } do
      if string.find(line, sym, 1, true) then
        return true
      end
    end
    return false
  end,

  --- Heuristically find the plugin nearest to the cursor for displaying detailed information
  find_nearest_plugin = function(self)
    if not self:valid_display() then
      return
    end

    local current_cursor_pos = api.nvim_win_get_cursor(0)
    local nb_lines = api.nvim_buf_line_count(0)
    local cursor_pos_y = math.max(current_cursor_pos[1], config.header_lines + 1)
    if cursor_pos_y > nb_lines then
      return
    end
    for i = cursor_pos_y, 1, -1 do
      local curr_line = api.nvim_buf_get_lines(0, i - 1, i, true)[1]
      if self:is_plugin_line(curr_line) then
        for name, _ in pairs(self.items) do
          if string.find(curr_line, name, 1, true) then
            return name, { i, 0 }
          end
        end
      end
    end
  end,
}

display_mt.__index = display_mt

local function look_back(str)
  return string.format([[\(%s\)\@%d<=]], str, #str)
end

-- TODO: Option for no colors
local function make_filetype_cmds(working_sym, done_sym, error_sym)
  return {
    -- Adapted from https://github.com/kristijanhusak/vim-packager
    'setlocal buftype=nofile bufhidden=wipe nobuflisted nolist noswapfile nowrap nospell nonumber norelativenumber nofoldenable signcolumn=no',
    'syntax clear',
    'syn match packerWorking /^ ' .. working_sym .. '/',
    'syn match packerSuccess /^ ' .. done_sym .. '/',
    'syn match packerFail /^ ' .. error_sym .. '/',
    'syn match packerStatus /^+.*—\\zs\\s.*$/',
    'syn match packerStatusSuccess /' .. look_back('^ ' .. done_sym) .. '\\s.*$/',
    'syn match packerStatusFail /' .. look_back('^ ' .. error_sym) .. '\\s.*$/',
    'syn match packerStatusCommit /^\\*.*—\\zs\\s.*$/',
    'syn match packerHash /\\(\\s\\)[0-9a-f]\\{7,8}\\(\\s\\)/',
    'syn match packerRelDate /([^)]*)$/',
    'syn match packerProgress /\\[\\zs[\\=]*/',
    'syn match packerOutput /\\(Output:\\)\\|\\(Commits:\\)\\|\\(Errors:\\)/',
    [[syn match packerTimeHigh /\d\{3\}\.\d\+ms/]],
    [[syn match packerTimeMedium /\d\{2\}\.\d\+ms/]],
    [[syn match packerTimeLow /\d\.\d\+ms/]],
    [[syn match packerTimeTrivial /0\.\d\+ms/]],
    [[syn match packerPackageNotLoaded /(not loaded)$/]],
    [[syn match packerString /\v(''|""|(['"]).{-}[^\\]\2)/]],
    [[syn match packerBool /\<\(false\|true\)\>/]],
    [[syn match packerPackageName /^\ • \zs[^ ]*/]],
    'hi def link packerWorking        SpecialKey',
    'hi def link packerSuccess        Question',
    'hi def link packerFail           ErrorMsg',
    'hi def link packerHash           Identifier',
    'hi def link packerRelDate        Comment',
    'hi def link packerProgress       Boolean',
    'hi def link packerOutput         Type',
  }
end

display.cfg = function(_config)
  config = _config.display
  if config.keybindings then
    for name, lhs in pairs(config.keybindings) do
      if keymaps[name] then
        keymaps[name].lhs = lhs
      end
    end
  end
  config.filetype_cmds = make_filetype_cmds(config.working_sym, config.done_sym, config.error_sym)
end

--- Utility to make the initial display buffer header
local function make_header(disp)
  local width = api.nvim_win_get_width(0)
  local pad_width = math.floor((width - string.len(config.title)) / 2.0)
  api.nvim_buf_set_lines(disp.buf, 0, 1, true, {
    string.rep(' ', pad_width) .. config.title,
    ' ' .. string.rep(config.header_sym, width - 2),
  })
end

--- Initialize options, settings, and keymaps for display windows
local function setup_window(disp)
  api.nvim_buf_set_option(disp.buf, 'filetype', 'packer')
  api.nvim_buf_set_name(disp.buf, '[packer]')
  for _, m in pairs(keymaps) do
    if m.lhs then
      api.nvim_buf_set_keymap(disp.buf, 'n', m.lhs, m.rhs, { nowait = true, silent = true })
    end
  end
  for _, c in ipairs(config.filetype_cmds) do
    vim.cmd(c)
  end
end

--- Open a new display window
-- Takes either a string representing a command or a function returning a (window, buffer) pair.
display.open = function(opener)
  if display.status.disp then
    if api.nvim_win_is_valid(display.status.disp.win) then
      api.nvim_win_close(display.status.disp.win, true)
    end

    display.status.disp = nil
  end

  local disp = setmetatable({}, display_mt)
  disp.marks = {}
  disp.plugins = {}
  disp.interactive = interactive(config)

  if disp.interactive then
    if type(opener) == 'string' then
      vim.cmd(opener)
      disp.win = api.nvim_get_current_win()
      disp.buf = api.nvim_get_current_buf()
    else
      local status, win, buf = opener '[packer]'
      if not status then
        log.error('Failure running opener function: ' .. vim.inspect(win))
        error(win)
      end

      disp.win = win
      disp.buf = buf
    end

    disp.ns = api.nvim_create_namespace ''
    make_header(disp)
    setup_window(disp)
    display.status.disp = disp
  end

  return disp
end

display.status = { running = false, disp = nil }

--- Close a display window and signal that any running operations should terminate
display.quit = function()
  display.status.running = false
  vim.fn.execute('q!', 'silent')
end

display.toggle_info = function()
  if display.status.disp then
    display.status.disp:toggle_info()
  end
end

display.diff = function()
  if display.status.disp then
    display.status.disp:diff()
  end
end

display.toggle_update = function()
  if display.status.disp then
    display.status.disp:toggle_update()
  end
end

display.continue = function()
  if display.status.disp then
    display.status.disp:continue()
  end
end

display.prompt_revert = function()
  if display.status.disp then
    display.status.disp:prompt_revert()
  end
end

display.retry = function()
  if display.status.any_failed_install then
    require('packer').install()
  elseif #display.status.failed_update_list > 0 then
    require('packer').update(unpack(display.status.failed_update_list))
  end
end

--- Async prompt_user
display.ask_user = a.wrap(prompt_user)

return display
```

## File: `lua/packer/handlers.lua`
```
local config = nil

local function cfg(_config)
  config = _config
end

local handlers = {
  cfg = cfg,
}

return handlers
```

## File: `lua/packer/install.lua`
```
local a = require 'packer.async'
local log = require 'packer.log'
local util = require 'packer.util'
local display = require 'packer.display'
local plugin_utils = require 'packer.plugin_utils'

local fmt = string.format
local async = a.sync
local await = a.wait

local config = nil

local function install_plugin(plugin, display_win, results)
  local plugin_name = util.get_plugin_full_name(plugin)
  return async(function()
    display_win:task_start(plugin_name, 'installing...')
    -- TODO: If the user provided a custom function as an installer, we would like to use pcall
    -- here. Need to figure out how that integrates with async code
    local r = await(plugin.installer(display_win))
    r = r:and_then(await, plugin_utils.post_update_hook(plugin, display_win))
    if r.ok then
      display_win:task_succeeded(plugin_name, 'installed')
      log.debug('Installed ' .. plugin_name)
    else
      display_win:task_failed(plugin_name, 'failed to install')
      log.debug(fmt('Failed to install %s: %s', plugin_name, vim.inspect(r.err)))
    end

    results.installs[plugin_name] = r
    results.plugins[plugin_name] = plugin
  end)
end

local function do_install(_, plugins, missing_plugins, results)
  results = results or {}
  results.installs = results.installs or {}
  results.plugins = results.plugins or {}
  local display_win = nil
  local tasks = {}
  if #missing_plugins > 0 then
    display_win = display.open(config.display.open_fn or config.display.open_cmd)
    for _, v in ipairs(missing_plugins) do
      if not plugins[v].disable then
        table.insert(tasks, install_plugin(plugins[v], display_win, results))
      end
    end
  end

  return tasks, display_win
end

local function cfg(_config)
  config = _config
end

local install = setmetatable({ cfg = cfg }, { __call = do_install })

return install
```

## File: `lua/packer/jobs.lua`
```
-- Interface with Neovim job control and provide a simple job sequencing structure
local split = vim.split
local loop = vim.loop
local a = require 'packer.async'
local log = require 'packer.log'
local result = require 'packer.result'

--- Utility function to make a "standard" logging callback for a given set of tables
-- Arguments:
-- - err_tbl: table to which err messages will be logged
-- - data_tbl: table to which data (non-err messages) will be logged
-- - pipe: the pipe for which this callback will be used. Passed in so that we can make sure all
--      output flushes before finishing reading
-- - disp: optional packer.display object for updating task status. Requires `name`
-- - name: optional string name for a current task. Used to update task status
local function make_logging_callback(err_tbl, data_tbl, pipe, disp, name)
  return function(err, data)
    if err then
      table.insert(err_tbl, vim.trim(err))
    end
    if data ~= nil then
      local trimmed = vim.trim(data)
      table.insert(data_tbl, trimmed)
      if disp then
        disp:task_update(name, split(trimmed, '\n')[1])
      end
    else
      loop.read_stop(pipe)
      loop.close(pipe)
    end
  end
end

--- Utility function to make a table for capturing output with "standard" structure
local function make_output_table()
  return { err = { stdout = {}, stderr = {} }, data = { stdout = {}, stderr = {} } }
end

--- Utility function to merge stdout and stderr from two tables with "standard" structure (either
--  the err or data subtables, specifically)
local function extend_output(to, from)
  vim.list_extend(to.stdout, from.stdout)
  vim.list_extend(to.stderr, from.stderr)
  return to
end

--- Wrapper for vim.loop.spawn. Takes a command, options, and callback just like vim.loop.spawn, but
--  (1) makes an async function and (2) ensures that all output from the command has been flushed
--  before calling the callback
local spawn = a.wrap(function(cmd, options, callback)
  local handle = nil
  local timer = nil
  handle, pid = loop.spawn(cmd, options, function(exit_code, signal)
    handle:close()
    if timer ~= nil then
      timer:stop()
      timer:close()
    end

    loop.close(options.stdio[1])
    local check = loop.new_check()
    loop.check_start(check, function()
      for _, pipe in pairs(options.stdio) do
        if not loop.is_closing(pipe) then
          return
        end
      end
      loop.check_stop(check)
      callback(exit_code, signal)
    end)
  end)

  if options.stdio then
    for i, pipe in pairs(options.stdio) do
      if options.stdio_callbacks[i] then
        loop.read_start(pipe, options.stdio_callbacks[i])
      end
    end
  end

  if handle == nil then 
      -- pid is an error string in this case 
      log.error(string.format("Failed spawning command: %s because %s", cmd, pid))
      callback(-1, pid)
      return 
  end

  if options.timeout then
    timer = loop.new_timer()
    timer:start(options.timeout, 0, function()
      timer:stop()
      timer:close()
      if loop.is_active(handle) then
        log.warn('Killing ' .. cmd .. ' due to timeout!')
        loop.process_kill(handle, 'sigint')
        handle:close()
        for _, pipe in pairs(options.stdio) do
          loop.close(pipe)
        end
        callback(-9999, 'sigint')
      end
    end)
  end
end)

--- Utility function to perform a common check for process success and return a result object
local function was_successful(r)
  if r.exit_code == 0 and (not r.output or not r.output.err or #r.output.err == 0) then
    return result.ok(r)
  else
    return result.err(r)
  end
end

--- Main exposed function for the jobs module. Takes a task and options and returns an async
-- function that will run the task with the given opts via vim.loop.spawn
-- Arguments:
--  - task: either a string or table. If string, split, and the first component is treated as the
--    command. If table, first element is treated as the command. All subsequent elements are passed
--    as args
--  - opts: table of options. Can include the keys "options" (like the options table passed to
--    vim.loop.spawn), "success_test" (a function, called like `was_successful` (above)),
--    "capture_output" (either a boolean, in which case default output capture is set up and the
--    resulting tables are included in the result, or a set of tables, in which case output is logged
--    to the given tables)
local run_job = function(task, opts)
  return a.sync(function()
    local options = opts.options or { hide = true }
    local stdout = nil
    local stderr = nil
    local job_result = { exit_code = -1, signal = -1 }
    local success_test = opts.success_test or was_successful
    local uv_err
    local output = make_output_table()
    local callbacks = {}
    local output_valid = false
    if opts.capture_output then
      if type(opts.capture_output) == 'boolean' then
        stdout, uv_err = loop.new_pipe(false)
        if uv_err then
          log.error('Failed to open stdout pipe: ' .. uv_err)
          return result.err()
        end

        stderr, uv_err = loop.new_pipe(false)
        if uv_err then
          log.error('Failed to open stderr pipe: ' .. uv_err)
          return job_result
        end

        callbacks.stdout = make_logging_callback(output.err.stdout, output.data.stdout, stdout)
        callbacks.stderr = make_logging_callback(output.err.stderr, output.data.stderr, stderr)
        output_valid = true
      elseif type(opts.capture_output) == 'table' then
        if opts.capture_output.stdout then
          stdout, uv_err = loop.new_pipe(false)
          if uv_err then
            log.error('Failed to open stdout pipe: ' .. uv_err)
            return job_result
          end

          callbacks.stdout = function(err, data)
            if data ~= nil then
              opts.capture_output.stdout(err, data)
            else
              loop.read_stop(stdout)
              loop.close(stdout)
            end
          end
        end
        if opts.capture_output.stderr then
          stderr, uv_err = loop.new_pipe(false)
          if uv_err then
            log.error('Failed to open stderr pipe: ' .. uv_err)
            return job_result
          end

          callbacks.stderr = function(err, data)
            if data ~= nil then
              opts.capture_output.stderr(err, data)
            else
              loop.read_stop(stderr)
              loop.close(stderr)
            end
          end
        end
      end
    end

    if type(task) == 'string' then
      local split_pattern = '%s+'
      task = split(task, split_pattern)
    end

    local cmd = task[1]
    if opts.timeout then
      options.timeout = 1000 * opts.timeout
    end

    options.cwd = opts.cwd

    local stdin = loop.new_pipe(false)
    options.args = { unpack(task, 2) }
    options.stdio = { stdin, stdout, stderr }
    options.stdio_callbacks = { nil, callbacks.stdout, callbacks.stderr }

    local exit_code, signal = a.wait(spawn(cmd, options))
    job_result = { exit_code = exit_code, signal = signal }
    if output_valid then
      job_result.output = output
    end
    return success_test(job_result)
  end)
end

local jobs = {
  run = run_job,
  logging_callback = make_logging_callback,
  output_table = make_output_table,
  extend_output = extend_output,
}

return jobs
```

## File: `lua/packer/load.lua`
```
local packer_load = nil
local cmd = vim.api.nvim_command
local fmt = string.format

local function verify_conditions(conds, name)
  if conds == nil then
    return true
  end
  for _, cond in ipairs(conds) do
    local success, result
    if type(cond) == 'boolean' then
      result = cond
    elseif type(cond) == 'string' then
      success, result = pcall(loadstring(cond))
      if not success then
        vim.schedule(function()
          vim.api.nvim_notify(
            'packer.nvim: Error running cond for ' .. name .. ': ' .. result,
            vim.log.levels.ERROR,
            {}
          )
        end)
        return false
      end
    end
    if result == false then
      return false
    end
  end
  return true
end

local function loader_clear_loaders(plugin)
  if plugin.commands then
    for _, del_cmd in ipairs(plugin.commands) do
      cmd('silent! delcommand ' .. del_cmd)
    end
  end

  if plugin.keys then
    for _, key in ipairs(plugin.keys) do
      cmd(fmt('silent! %sunmap %s', key[1], key[2]))
    end
  end
end

local function loader_apply_config(plugin, name)
  if plugin.config then
    for _, config_line in ipairs(plugin.config) do
      local success, err = pcall(loadstring(config_line), name, plugin)
      if not success then
        vim.schedule(function()
          vim.api.nvim_notify('packer.nvim: Error running config for ' .. name .. ': ' .. err, vim.log.levels.ERROR, {})
        end)
      end
    end
  end
end

local function loader_apply_wants(plugin, plugins)
  if plugin.wants then
    for _, wanted_name in ipairs(plugin.wants) do
      packer_load({ wanted_name }, {}, plugins)
    end
  end
end

local function loader_apply_after(plugin, plugins, name)
  if plugin.after then
    for _, after_name in ipairs(plugin.after) do
      local after_plugin = plugins[after_name]
      after_plugin.load_after[name] = nil
      if next(after_plugin.load_after) == nil then
        packer_load({ after_name }, {}, plugins)
      end
    end
  end
end

local function apply_cause_side_effects(cause)
  if cause.cmd then
    local lines = cause.l1 == cause.l2 and '' or (cause.l1 .. ',' .. cause.l2)
    -- This is a hack to deal with people who haven't recompiled after updating to the new command
    -- creation logic
    local bang = ''
    if type(cause.bang) == 'string' then
      bang = cause.bang
    elseif type(cause.bang) == 'boolean' and cause.bang then
      bang = '!'
    end
    cmd(fmt('%s %s%s%s %s', cause.mods or '', lines, cause.cmd, bang, cause.args))
  elseif cause.keys then
    local extra = ''
    while true do
      local c = vim.fn.getchar(0)
      if c == 0 then
        break
      end
      extra = extra .. vim.fn.nr2char(c)
    end

    if cause.prefix then
      local prefix = vim.v.count ~= 0 and vim.v.count or ''
      prefix = prefix .. '"' .. vim.v.register .. cause.prefix
      if vim.fn.mode 'full' == 'no' then
        if vim.v.operator == 'c' then
          prefix = '' .. prefix
        end
        prefix = prefix .. vim.v.operator
      end

      vim.fn.feedkeys(prefix, 'n')
    end

    local escaped_keys = vim.api.nvim_replace_termcodes(cause.keys .. extra, true, true, true)
    vim.api.nvim_feedkeys(escaped_keys, 'm', true)
  elseif cause.event then
    cmd(fmt('doautocmd <nomodeline> %s', cause.event))
  elseif cause.ft then
    cmd(fmt('doautocmd <nomodeline> %s FileType %s', 'filetypeplugin', cause.ft))
    cmd(fmt('doautocmd <nomodeline> %s FileType %s', 'filetypeindent', cause.ft))
    cmd(fmt('doautocmd <nomodeline> %s FileType %s', 'syntaxset', cause.ft))
  end
end

packer_load = function(names, cause, plugins, force)
  local some_unloaded = false
  local needs_bufread = false
  local num_names = #names
  for i = 1, num_names do
    local plugin = plugins[names[i]]
    if not plugin then
      local err_message = 'Error: attempted to load ' .. names[i] .. ' which is not present in plugins table!'
      vim.notify(err_message, vim.log.levels.ERROR, { title = 'packer.nvim' })
      error(err_message)
    end

    if not plugin.loaded then
      loader_clear_loaders(plugin)
      if force or verify_conditions(plugin.cond, names[i]) then
        -- Set the plugin as loaded before config is run in case something in the config tries to load
        -- this same plugin again
        plugin.loaded = true
        some_unloaded = true
        needs_bufread = needs_bufread or plugin.needs_bufread
        loader_apply_wants(plugin, plugins)
        cmd('packadd ' .. names[i])
        if plugin.after_files then
          for _, file in ipairs(plugin.after_files) do
            cmd('silent source ' .. file)
          end
        end
        loader_apply_config(plugin, names[i])
        loader_apply_after(plugin, plugins, names[i])
      end
    end
  end

  if not some_unloaded then
    return
  end

  if needs_bufread then
    if _G._packer and _G._packer.inside_compile == true then
      -- delaying BufRead to end of packer_compiled
      _G._packer.needs_bufread = true
    else
      cmd 'doautocmd BufRead'
    end
  end
  -- Retrigger cmd/keymap...
  apply_cause_side_effects(cause)
end

local function load_wrapper(names, cause, plugins, force)
  local success, err_msg = pcall(packer_load, names, cause, plugins, force)
  if not success then
    vim.cmd 'echohl ErrorMsg'
    vim.cmd('echomsg "Error in packer_compiled: ' .. vim.fn.escape(err_msg, '"') .. '"')
    vim.cmd 'echomsg "Please check your config for correctness"'
    vim.cmd 'echohl None'
  end
end

return load_wrapper
```

## File: `lua/packer/log.lua`
```
-- log.lua
--
-- Inspired by rxi/log.lua
-- Modified by tjdevries and can be found at github.com/tjdevries/vlog.nvim
--
-- This library is free software; you can redistribute it and/or modify it
-- under the terms of the MIT license. See LICENSE for details.
-- User configuration section
local default_config = {
  -- Name of the plugin. Prepended to log messages
  plugin = 'packer.nvim',

  -- Should print the output to neovim while running
  use_console = true,

  -- Should highlighting be used in console (using echohl)
  highlights = true,

  -- Should write to a file
  use_file = true,

  -- Any messages above this level will be logged.
  level = 'debug',

  -- Level configuration
  modes = {
    { name = 'trace', hl = 'Comment' },
    { name = 'debug', hl = 'Comment' },
    { name = 'info', hl = 'None' },
    { name = 'warn', hl = 'WarningMsg' },
    { name = 'error', hl = 'ErrorMsg' },
    { name = 'fatal', hl = 'ErrorMsg' },
  },

  -- Which levels should be logged?
  active_levels = { [1] = true, [2] = true, [3] = true, [4] = true, [5] = true, [6] = true },

  -- Can limit the number of decimals displayed for floats
  float_precision = 0.01,
}

-- {{{ NO NEED TO CHANGE
local log = {}

local unpack = unpack or table.unpack

local level_ids = { trace = 1, debug = 2, info = 3, warn = 4, error = 5, fatal = 6 }
log.cfg = function(_config)
  local min_active_level = level_ids[_config.log.level]
  local config = { active_levels = {} }
  if min_active_level then
    for i = min_active_level, 6 do
      config.active_levels[i] = true
    end
  end
  log.new(config, true)
end

log.new = function(config, standalone)
  config = vim.tbl_deep_extend('force', default_config, config)
  local outfile = string.format('%s/%s.log', vim.fn.stdpath 'cache', config.plugin)
  vim.fn.mkdir(vim.fn.stdpath 'cache', 'p')
  local obj
  if standalone then
    obj = log
  else
    obj = {}
  end

  local levels = {}
  for i, v in ipairs(config.modes) do
    levels[v.name] = i
  end

  local round = function(x, increment)
    increment = increment or 1
    x = x / increment
    return (x > 0 and math.floor(x + 0.5) or math.ceil(x - 0.5)) * increment
  end

  local make_string = function(...)
    local t = {}
    for i = 1, select('#', ...) do
      local x = select(i, ...)

      if type(x) == 'number' and config.float_precision then
        x = tostring(round(x, config.float_precision))
      elseif type(x) == 'table' then
        x = vim.inspect(x)
      else
        x = tostring(x)
      end

      t[#t + 1] = x
    end
    return table.concat(t, ' ')
  end

  local console_output = vim.schedule_wrap(function(level_config, info, nameupper, msg)
    local console_lineinfo = vim.fn.fnamemodify(info.short_src, ':t') .. ':' .. info.currentline
    local console_string = string.format('[%-6s%s] %s: %s', nameupper, os.date '%H:%M:%S', console_lineinfo, msg)
    -- Heuristic to check for nvim-notify
    local is_fancy_notify = type(vim.notify) == 'table'
    vim.notify(
      string.format([[%s%s]], is_fancy_notify and '' or ('[' .. config.plugin .. '] '), console_string),
      vim.log.levels[level_config.name:upper()],
      { title = config.plugin }
    )
  end)

  local log_at_level = function(level, level_config, message_maker, ...)
    -- Return early if we're below the config.level
    if level < levels[config.level] then
      return
    end
    local nameupper = level_config.name:upper()

    local msg = message_maker(...)
    local info = debug.getinfo(2, 'Sl')
    local lineinfo = info.short_src .. ':' .. info.currentline

    -- Output to console
    if config.use_console and config.active_levels[level] then
      console_output(level_config, info, nameupper, msg)
    end

    -- Output to log file
    if config.use_file and config.active_levels[level] then
      local fp, err = io.open(outfile, 'a')
      if not fp then
        print(err)
        return
      end

      local str = string.format('[%-6s%s %s] %s: %s\n', nameupper, os.date(), vim.loop.hrtime(), lineinfo, msg)
      fp:write(str)
      fp:close()
    end
  end

  for i, x in ipairs(config.modes) do
    obj[x.name] = function(...)
      return log_at_level(i, x, make_string, ...)
    end

    obj[('fmt_%s'):format(x.name)] = function()
      return log_at_level(i, x, function(...)
        local passed = { ... }
        local fmt = table.remove(passed, 1)
        local inspected = {}
        for _, v in ipairs(passed) do
          table.insert(inspected, vim.inspect(v))
        end
        return string.format(fmt, unpack(inspected))
      end)
    end
  end
end

log.new(default_config, true)
-- }}}

return log
```

## File: `lua/packer/luarocks.lua`
```
-- Add support for installing and cleaning Luarocks dependencies
-- Based off of plenary/neorocks/init.lua in https://github.com/nvim-lua/plenary.nvim
local a = require 'packer.async'
local jobs = require 'packer.jobs'
local log = require 'packer.log'
local result = require 'packer.result'
local util = require 'packer.util'

local fmt = string.format
local async = a.sync
local await = a.wait

local config = nil
local function cfg(_config)
  config = _config.luarocks
end
local function warn_need_luajit()
  log.error 'LuaJIT is required for Luarocks functionality!'
end

local lua_version = nil
if jit then
  local jit_version = string.gsub(jit.version, 'LuaJIT ', '')
  lua_version = { lua = string.gsub(_VERSION, 'Lua ', ''), jit = jit_version, dir = jit_version }
else
  return {
    handle_command = warn_need_luajit,
    install_commands = warn_need_luajit,
    list = warn_need_luajit,
    install_hererocks = warn_need_luajit,
    setup_paths = warn_need_luajit,
    uninstall = warn_need_luajit,
    clean = warn_need_luajit,
    install = warn_need_luajit,
    ensure = warn_need_luajit,
    generate_path_setup = function()
      return ''
    end,
    cfg = cfg,
  }
end

local cache_path = vim.fn.stdpath 'cache'
local rocks_path = util.join_paths(cache_path, 'packer_hererocks')
local hererocks_file = util.join_paths(rocks_path, 'hererocks.py')
local hererocks_install_dir = util.join_paths(rocks_path, lua_version.dir)
local shell_hererocks_dir = vim.fn.shellescape(hererocks_install_dir)
local _hererocks_setup_done = false
local function hererocks_is_setup()
  if _hererocks_setup_done then
    return true
  end
  local path_info = vim.loop.fs_stat(util.join_paths(hererocks_install_dir, 'lib'))
  _hererocks_setup_done = (path_info ~= nil) and (path_info['type'] == 'directory')
  return _hererocks_setup_done
end

local function hererocks_installer(disp)
  return async(function()
    local hererocks_url = 'https://raw.githubusercontent.com/luarocks/hererocks/master/hererocks.py'
    local hererocks_cmd
    await(a.main)
    vim.fn.mkdir(rocks_path, 'p')
    if vim.fn.executable 'curl' > 0 then
      hererocks_cmd = 'curl ' .. hererocks_url .. ' -o ' .. hererocks_file
    elseif vim.fn.executable 'wget' > 0 then
      hererocks_cmd = 'wget ' .. hererocks_url .. ' -O ' .. hererocks_file .. ' --verbose'
    else
      return result.err '"curl" or "wget" is required to install hererocks'
    end

    if disp ~= nil then
      disp:task_start('luarocks-hererocks', 'installing hererocks...')
    end
    local output = jobs.output_table()
    local callbacks = {
      stdout = jobs.logging_callback(output.err.stdout, output.data.stdout, nil, disp, 'luarocks-hererocks'),
      stderr = jobs.logging_callback(output.err.stderr, output.data.stderr),
    }

    local opts = { capture_output = callbacks }
    local r = await(jobs.run(hererocks_cmd, opts)):map_err(function(err)
      return { msg = 'Error installing hererocks', data = err, output = output }
    end)

    local luarocks_cmd = config.python_cmd
      .. ' '
      .. hererocks_file
      .. ' --verbose -j '
      .. lua_version.jit
      .. ' -r latest '
      .. hererocks_install_dir
    r:and_then(await, jobs.run(luarocks_cmd, opts))
      :map_ok(function()
        if disp then
          disp:task_succeeded('luarocks-hererocks', 'installed hererocks!')
        end
      end)
      :map_err(function(err)
        if disp then
          disp:task_failed('luarocks-hererocks', 'failed to install hererocks!')
        end
        log.error('Failed to install hererocks: ' .. vim.inspect(err))
        return { msg = 'Error installing luarocks', data = err, output = output }
      end)
    return r
  end)
end

local function package_patterns(dir)
  local sep = util.get_separator()
  return fmt('%s%s?.lua;%s%s?%sinit.lua', dir, sep, dir, sep, sep)
end

local package_paths = (function()
  local install_path = util.join_paths(hererocks_install_dir, 'lib', 'luarocks', fmt('rocks-%s', lua_version.lua))
  local share_path = util.join_paths(hererocks_install_dir, 'share', 'lua', lua_version.lua)
  return package_patterns(share_path) .. ';' .. package_patterns(install_path)
end)()

local nvim_paths_are_setup = false
local function setup_nvim_paths()
  if not hererocks_is_setup() then
    log.warn 'Tried to setup Neovim Lua paths before hererocks was setup!'
    return
  end

  if nvim_paths_are_setup then
    log.warn 'Tried to setup Neovim Lua paths redundantly!'
    return
  end

  if not string.find(package.path, package_paths, 1, true) then
    package.path = package.path .. ';' .. package_paths
  end

  local install_cpath = util.join_paths(hererocks_install_dir, 'lib', 'lua', lua_version.lua)
  local install_cpath_pattern = fmt('%s%s?.so', install_cpath, util.get_separator())
  if not string.find(package.cpath, install_cpath_pattern, 1, true) then
    package.cpath = package.cpath .. ';' .. install_cpath_pattern
  end

  nvim_paths_are_setup = true
end

local function generate_path_setup_code()
  local package_path_str = vim.inspect(package_paths)
  local install_cpath = util.join_paths(hererocks_install_dir, 'lib', 'lua', lua_version.lua)
  local install_cpath_pattern = fmt('"%s%s?.so"', install_cpath, util.get_separator())
  install_cpath_pattern = vim.fn.escape(install_cpath_pattern, [[\]])
  return [[
local package_path_str = ]] .. package_path_str .. [[

local install_cpath_pattern = ]] .. install_cpath_pattern .. [[

if not string.find(package.path, package_path_str, 1, true) then
  package.path = package.path .. ';' .. package_path_str
end

if not string.find(package.cpath, install_cpath_pattern, 1, true) then
  package.cpath = package.cpath .. ';' .. install_cpath_pattern
end
]]
end

local function activate_hererocks_cmd(install_path)
  local activate_file = 'activate'
  local user_shell = os.getenv 'SHELL'
  local shell = user_shell:gmatch '([^/]*)$'()
  if shell == 'fish' then
    activate_file = 'activate.fish'
  elseif shell == 'csh' then
    activate_file = 'activate.csh'
  end

  return fmt('source %s', util.join_paths(install_path, 'bin', activate_file))
end

local function run_luarocks(args, disp, operation_name)
  local cmd = {
    os.getenv 'SHELL',
    '-c',
    fmt('%s && luarocks --tree=%s %s', activate_hererocks_cmd(hererocks_install_dir), shell_hererocks_dir, args),
  }
  return async(function()
    local output = jobs.output_table()
    local callbacks = {
      stdout = jobs.logging_callback(output.err.stdout, output.data.stdout, nil, disp, operation_name),
      stderr = jobs.logging_callback(output.err.stderr, output.data.stderr),
    }

    local opts = { capture_output = callbacks }
    return await(jobs.run(cmd, opts))
      :map_err(function(err)
        return { msg = fmt('Error running luarocks %s', args), data = err, output = output }
      end)
      :map_ok(function(data)
        return { data = data, output = output }
      end)
  end)
end

local luarocks_keys = { only_server = 'only-server', only_source = 'only-sources' }

local function is_valid_luarock_key(key)
  return not (key == 'tree' or key == 'local')
end

local function format_luarocks_args(package)
  if type(package) ~= 'table' then
    return ''
  end
  local args = {}
  for key, value in pairs(package) do
    if type(key) == 'string' and is_valid_luarock_key(key) then
      local luarock_key = luarocks_keys[key] and luarocks_keys[key] or key
      if luarock_key and type(value) == 'string' then
        table.insert(args, string.format('--%s=%s', key, value))
      elseif key == 'env' and type(value) == 'table' then
        for name, env_value in pairs(value) do
          table.insert(args, string.format('%s=%s', name, env_value))
        end
      end
    end
  end
  return ' ' .. table.concat(args, ' ')
end

local function luarocks_install(package, results, disp)
  return async(function()
    local package_name = type(package) == 'table' and package[1] or package
    if disp then
      disp:task_update('luarocks-install', 'installing ' .. package_name)
    end
    local args = format_luarocks_args(package)
    local version = package.version and ' ' .. package.version .. ' ' or ''
    local install_result = await(run_luarocks('install ' .. package_name .. version .. args, disp, 'luarocks-install'))
    if results then
      results.luarocks.installs[package_name] = install_result
    end
    return install_result
  end)
end

local function install_packages(packages, results, disp)
  return async(function()
    local r = result.ok()
    if not hererocks_is_setup() then
      r:and_then(await, hererocks_installer(disp))
    end
    if disp then
      disp:task_start('luarocks-install', 'installing rocks...')
    end
    if results then
      results.luarocks.installs = {}
    end
    for _, package in ipairs(packages) do
      r:and_then(await, luarocks_install(package, results, disp))
    end
    r:map_ok(function()
      if disp then
        disp:task_succeeded('luarocks-install', 'rocks installed!')
      end
    end):map_err(function()
      if disp then
        disp:task_failed('luarocks-install', 'installing rocks failed!')
      end
    end)
    return r
  end)
end

--- Install the packages specified with `packages` synchronously
local function install_sync(packages)
  return async(function()
    return await(install_packages(packages))
  end)()
end

local function chunk_output(output)
  -- Merge the output to a single line, then split again. Helps to deal with inconsistent
  -- chunking in the output collection
  local res = table.concat(output, '\n')
  return vim.split(res, '\n')
end

local function luarocks_list(disp)
  return async(function()
    local r = result.ok()
    if not hererocks_is_setup() then
      r:and_then(await, hererocks_installer(disp))
    end
    r:and_then(await, run_luarocks 'list --porcelain')
    return r:map_ok(function(data)
      local results = {}
      local output = chunk_output(data.output.data.stdout)
      for _, line in ipairs(output) do
        for l_package, version, status, install_path in string.gmatch(line, '([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)') do
          table.insert(results, {
            name = l_package,
            version = version,
            status = status,
            install_path = install_path,
          })
        end
      end

      return results
    end)
  end)
end

local function luarocks_show(package, disp)
  return async(function()
    local r = result.ok()
    if not hererocks_is_setup() then
      r:and_then(await, hererocks_installer(disp))
    end
    r:and_then(await, run_luarocks('show --porcelain ' .. package))
    return r:map_ok(function(data)
      local output = chunk_output(data.output.data.stdout)
      local dependencies = {}
      for _, line in ipairs(output) do
        local components = {}
        for component in string.gmatch(line, '([^%s]+)') do
          components[#components + 1] = component
        end

        if (components[1] == 'dependency' or components[1] == 'indirect_dependency') and (components[2] ~= 'lua') then
          dependencies[components[2]] = components[2]
        end
      end

      return dependencies
    end)
  end)
end

local function luarocks_remove(package, results, disp)
  return async(function()
    if disp then
      disp:task_update('luarocks-remove', 'removing ' .. package)
    end
    local remove_result = await(run_luarocks('remove ' .. package, disp, 'luarocks-remove'))
    if results then
      results.luarocks.removals[package] = remove_result
    end
    return remove_result
  end)
end

local function uninstall_packages(packages, results, disp)
  return async(function()
    local r = result.ok()
    if not hererocks_is_setup() then
      r:and_then(await, hererocks_installer(disp))
    end
    if disp then
      disp:task_start('luarocks-remove', 'uninstalling rocks...')
    end
    if results then
      results.luarocks.removals = {}
    end
    for _, package in ipairs(packages) do
      local name = type(package) == 'table' and package[1] or package
      r:and_then(await, luarocks_remove(name, results, disp))
    end
    r:map_ok(function()
      if disp then
        disp:task_succeeded('luarocks-remove', 'rocks cleaned!')
      end
    end):map_err(function()
      if disp then
        disp:task_failed('luarocks-remove', 'cleaning rocks failed!')
      end
    end)
    return r
  end)
end

--- Uninstall the packages specified with `packages` synchronously
local function uninstall_sync(packages)
  return async(function()
    return await(uninstall_packages(packages))
  end)()
end

local function clean_rocks(rocks, results, disp)
  return async(function()
    local r = result.ok()
    if not hererocks_is_setup() then
      return r
    end
    r:and_then(await, luarocks_list(disp))
    local installed_packages
    if r.ok then
      installed_packages = r.ok
    else
      return r
    end

    local dependency_info = {}
    for _, package in ipairs(installed_packages) do
      r:and_then(await, luarocks_show(package.name, disp))
      if r.ok then
        dependency_info[package.name] = r.ok
      end
    end

    r = r:map_ok(function()
      local to_remove = {}
      for _, package in ipairs(installed_packages) do
        to_remove[package.name] = package
      end
      for _, rock in pairs(rocks) do
        if type(rock) == 'table' then
          if to_remove[rock[1]] and (not rock.version or to_remove[rock[1]].version == rock.version) then
            to_remove[rock[1]] = nil
          end
        else
          to_remove[rock] = nil
        end
      end

      for rock, dependencies in pairs(dependency_info) do
        if rocks[rock] ~= nil then
          for _, dependency in pairs(dependencies) do
            to_remove[dependency] = nil
          end
        end
      end

      -- Toposort to ensure that we remove packages before their dependencies
      local removal_order = {}
      local frontier = {}
      for rock, _ in pairs(to_remove) do
        if next(dependency_info[rock]) == nil then
          frontier[#frontier + 1] = rock
          dependency_info[rock] = nil
        end
      end

      local inverse_dependencies = {}
      for rock, depends in pairs(dependency_info) do
        for d, _ in pairs(depends) do
          inverse_dependencies[d] = inverse_dependencies[d] or {}
          inverse_dependencies[d][rock] = true
        end
      end

      while #frontier > 0 do
        local rock = table.remove(frontier)
        removal_order[#removal_order + 1] = rock
        local inv_depends = inverse_dependencies[rock]
        if inv_depends ~= nil then
          for depends, _ in pairs(inverse_dependencies[rock]) do
            table.remove(dependency_info[depends])
            if #dependency_info[depends] == 0 then
              frontier[#frontier + 1] = depends
            end
          end
        end
      end

      local reverse_order = {}
      for i = #removal_order, 1, -1 do
        reverse_order[#reverse_order + 1] = removal_order[i]
      end
      return reverse_order
    end)

    if results ~= nil then
      results.luarocks = results.luarocks or {}
    end
    return r:and_then(await, uninstall_packages(r.ok, results, disp))
  end)
end

local function ensure_rocks(rocks, results, disp)
  return async(function()
    local to_install = {}
    for _, rock in pairs(rocks) do
      if type(rock) == 'table' then
        to_install[rock[1]:lower()] = rock
      else
        to_install[rock:lower()] = true
      end
    end

    local r = result.ok()
    if next(to_install) == nil then
      return r
    end
    if disp == nil then
      disp = require('packer.display').open(config.display.open_fn or config.display.open_cmd)
    end
    if not hererocks_is_setup() then
      r = r:and_then(await, hererocks_installer(disp))
    end
    r:and_then(await, luarocks_list(disp))
    r:map_ok(function(installed_packages)
      for _, package in ipairs(installed_packages) do
        local spec = to_install[package.name]
        if spec then
          if type(spec) == 'table' then
            -- if the package is on the system and the spec has no version
            -- or it has a version and that is the version on the system do not install it again
            if not spec.version or (spec.version and spec.version == package.version) then
              to_install[package.name] = nil
            end
          else
            to_install[package.name] = nil
          end
        end
      end

      local package_specs = {}
      for name, spec in pairs(to_install) do
        if type(spec) == 'table' then
          table.insert(package_specs, spec)
        else
          table.insert(package_specs, { name })
        end
      end

      return package_specs
    end)

    results.luarocks = results.luarocks or {}
    return r:and_then(await, install_packages(r.ok, results, disp))
  end)
end

local function handle_command(cmd, ...)
  local task
  local packages = { ... }
  if cmd == 'install' then
    task = install_packages(packages)
  elseif cmd == 'remove' then
    task = uninstall_packages(packages)
  else
    log.warn 'Unrecognized command!'
    return result.err 'Unrecognized command'
  end

  return async(function()
    local r = await(task)
    await(a.main)
    local package_names = vim.fn.escape(vim.inspect(packages), '"')
    return r:map_ok(function(data)
      local operation_name = cmd:sub(1, 1):upper() .. cmd:sub(2)
      log.info(fmt('%sed packages %s', operation_name, package_names))
      return data
    end):map_err(function(err)
      log.error(fmt('Failed to %s packages %s: %s', cmd, package_names, vim.fn.escape(vim.inspect(err), '"\n')))
      return err
    end)
  end)()
end

local function make_commands()
  vim.cmd [[ command! -nargs=+ PackerRocks lua require('packer.luarocks').handle_command(<f-args>) ]]
end

return {
  handle_command = handle_command,
  install_commands = make_commands,
  list = luarocks_list,
  install_hererocks = hererocks_installer,
  setup_paths = setup_nvim_paths,
  uninstall = uninstall_sync,
  clean = clean_rocks,
  install = install_sync,
  ensure = ensure_rocks,
  generate_path_setup = generate_path_setup_code,
  cfg = cfg,
}
```

## File: `lua/packer/plugin_types.lua`
```
local config

local function cfg(_config)
  config = _config
end

local plugin_types = setmetatable({ cfg = cfg }, {
  __index = function(self, k)
    local v = require('packer.plugin_types.' .. k)
    v.cfg(config)
    self[k] = v
    return v
  end,
})

return plugin_types
```

## File: `lua/packer/plugin_utils.lua`
```
local a = require 'packer.async'
local jobs = require 'packer.jobs'
local util = require 'packer.util'
local result = require 'packer.result'
local log = require 'packer.log'

local await = a.wait

local config = nil
local plugin_utils = {}
plugin_utils.cfg = function(_config)
  config = _config
end

plugin_utils.custom_plugin_type = 'custom'
plugin_utils.local_plugin_type = 'local'
plugin_utils.git_plugin_type = 'git'

plugin_utils.guess_type = function(plugin)
  if plugin.installer then
    plugin.type = plugin_utils.custom_plugin_type
  elseif vim.fn.isdirectory(plugin.path) ~= 0 then
    plugin.url = plugin.path
    plugin.type = plugin_utils.local_plugin_type
  elseif
    string.sub(plugin.path, 1, 6) == 'git://'
    or string.sub(plugin.path, 1, 6) == 'ssh://'
    or string.sub(plugin.path, 1, 10) == 'git+ssh://'
    or string.sub(plugin.path, 1, 10) == 'ssh+git://'
    or string.sub(plugin.path, 1, 4) == 'http'
    or string.match(plugin.path, '@')
  then
    plugin.url = plugin.path
    plugin.type = plugin_utils.git_plugin_type
  else
    local path = table.concat(vim.split(plugin.path, '\\', true), '/')
    plugin.url = string.format(config.git.default_url_format, path)
    plugin.type = plugin_utils.git_plugin_type
  end
end

plugin_utils.guess_dir_type = function(dir)
  local globdir = vim.fn.glob(dir)
  local dir_type = (vim.loop.fs_lstat(globdir) or { type = 'noexist' }).type

  --[[ NOTE: We're assuming here that:
             1. users only create custom plugins for non-git repos;
             2. custom plugins don't use symlinks to install;
             otherwise, there's no consistent way to tell from a dir alone… ]]
  if dir_type == 'link' then
    return plugin_utils.local_plugin_type
  elseif vim.loop.fs_stat(globdir .. '/.git') then
    return plugin_utils.git_plugin_type
  elseif dir_type ~= 'noexist' then
    return plugin_utils.custom_plugin_type
  end
end

plugin_utils.helptags_stale = function(dir)
  -- Adapted directly from minpac.vim
  local txts = vim.fn.glob(util.join_paths(dir, '*.txt'), true, true)
  vim.list_extend(txts, vim.fn.glob(util.join_paths(dir, '*.[a-z][a-z]x'), true, true))
  local tags = vim.fn.glob(util.join_paths(dir, 'tags'), true, true)
  vim.list_extend(tags, vim.fn.glob(util.join_paths(dir, 'tags-[a-z][a-z]'), true, true))
  local txt_ftimes = util.map(vim.fn.getftime, txts)
  local tag_ftimes = util.map(vim.fn.getftime, tags)
  if #txt_ftimes == 0 then
    return false
  end
  if #tag_ftimes == 0 then
    return true
  end
  local txt_newest = math.max(unpack(txt_ftimes))
  local tag_oldest = math.min(unpack(tag_ftimes))
  return txt_newest > tag_oldest
end

plugin_utils.update_helptags = vim.schedule_wrap(function(...)
  for _, dir in ipairs(...) do
    local doc_dir = util.join_paths(dir, 'doc')
    if plugin_utils.helptags_stale(doc_dir) then
      log.info('Updating helptags for ' .. doc_dir)
      vim.cmd('silent! helptags ' .. vim.fn.fnameescape(doc_dir))
    end
  end
end)

plugin_utils.update_rplugins = vim.schedule_wrap(function()
  if vim.fn.exists ':UpdateRemotePlugins' == 2 then
    vim.cmd [[silent UpdateRemotePlugins]]
  end
end)

plugin_utils.ensure_dirs = function()
  if vim.fn.isdirectory(config.opt_dir) == 0 then
    vim.fn.mkdir(config.opt_dir, 'p')
  end

  if vim.fn.isdirectory(config.start_dir) == 0 then
    vim.fn.mkdir(config.start_dir, 'p')
  end
end

plugin_utils.list_installed_plugins = function()
  local opt_plugins = {}
  local start_plugins = {}
  local opt_dir_handle = vim.loop.fs_opendir(config.opt_dir, nil, 50)
  if opt_dir_handle then
    local opt_dir_items = vim.loop.fs_readdir(opt_dir_handle)
    while opt_dir_items do
      for _, item in ipairs(opt_dir_items) do
        opt_plugins[util.join_paths(config.opt_dir, item.name)] = true
      end

      opt_dir_items = vim.loop.fs_readdir(opt_dir_handle)
    end
  end

  local start_dir_handle = vim.loop.fs_opendir(config.start_dir, nil, 50)
  if start_dir_handle then
    local start_dir_items = vim.loop.fs_readdir(start_dir_handle)
    while start_dir_items do
      for _, item in ipairs(start_dir_items) do
        start_plugins[util.join_paths(config.start_dir, item.name)] = true
      end

      start_dir_items = vim.loop.fs_readdir(start_dir_handle)
    end
  end

  return opt_plugins, start_plugins
end

plugin_utils.find_missing_plugins = function(plugins, opt_plugins, start_plugins)
  return a.sync(function()
    if opt_plugins == nil or start_plugins == nil then
      opt_plugins, start_plugins = plugin_utils.list_installed_plugins()
    end

    -- NOTE/TODO: In the case of a plugin gaining/losing an alias, this will force a clean and
    -- reinstall
    local missing_plugins = {}
    for _, plugin_name in ipairs(vim.tbl_keys(plugins)) do
      local plugin = plugins[plugin_name]
      if not plugin.disable then
        local plugin_path = util.join_paths(config[plugin.opt and 'opt_dir' or 'start_dir'], plugin.short_name)
        local plugin_installed = (plugin.opt and opt_plugins or start_plugins)[plugin_path]

        await(a.main)
        local guessed_type = plugin_utils.guess_dir_type(plugin_path)
        if not plugin_installed or plugin.type ~= guessed_type then
          missing_plugins[plugin_name] = true
        elseif guessed_type == plugin_utils.git_plugin_type then
          local r = await(plugin.remote_url())
          local remote = r.ok and r.ok.remote or nil
          if remote then
            -- Form a Github-style user/repo string
            local parts = vim.split(remote, '[:/]')
            local repo_name = parts[#parts - 1] .. '/' .. parts[#parts]
            repo_name = repo_name:gsub('%.git', '')

            -- Also need to test for "full URL" plugin names, but normalized to get rid of the
            -- protocol
            local normalized_remote = remote:gsub('https://', ''):gsub('ssh://git@', '')
            local normalized_plugin_name = plugin.name:gsub('https://', ''):gsub('ssh://git@', ''):gsub('\\', '/')
            if (normalized_remote ~= normalized_plugin_name) and (repo_name ~= normalized_plugin_name) then
              missing_plugins[plugin_name] = true
            end
          end
        end
      end
    end

    return missing_plugins
  end)
end

plugin_utils.get_fs_state = function(plugins)
  log.debug 'Updating FS state'
  local opt_plugins, start_plugins = plugin_utils.list_installed_plugins()
  return a.sync(function()
    local missing_plugins = await(plugin_utils.find_missing_plugins(plugins, opt_plugins, start_plugins))
    return { opt = opt_plugins, start = start_plugins, missing = missing_plugins }
  end)
end

plugin_utils.load_plugin = function(plugin)
  if plugin.opt then
    vim.cmd('packadd ' .. plugin.short_name)
  else
    vim.o.runtimepath = vim.o.runtimepath .. ',' .. plugin.install_path
    for _, pat in ipairs {
      table.concat({ 'plugin', '**/*.vim' }, util.get_separator()),
      table.concat({ 'after', 'plugin', '**/*.vim' }, util.get_separator()),
    } do
      local path = util.join_paths(plugin.install_path, pat)
      local glob_ok, files = pcall(vim.fn.glob, path, false, true)
      if not glob_ok then
        if string.find(files, 'E77') then
          vim.cmd('silent exe "source ' .. path .. '"')
        else
          error(files)
        end
      elseif #files > 0 then
        for _, file in ipairs(files) do
          file = file:gsub('\\', '/')
          vim.cmd('silent exe "source ' .. file .. '"')
        end
      end
    end
  end
end

plugin_utils.post_update_hook = function(plugin, disp)
  local plugin_name = util.get_plugin_full_name(plugin)
  return a.sync(function()
    if plugin.run or not plugin.opt then
      await(a.main)
      plugin_utils.load_plugin(plugin)
    end

    if plugin.run then
      if type(plugin.run) ~= 'table' then
        plugin.run = { plugin.run }
      end
      disp:task_update(plugin_name, 'running post update hooks...')
      local hook_result = result.ok()
      for _, task in ipairs(plugin.run) do
        if type(task) == 'function' then
          local success, err = pcall(task, plugin, disp)
          if not success then
            return result.err {
              msg = 'Error running post update hook: ' .. vim.inspect(err),
            }
          end
        elseif type(task) == 'string' then
          if string.sub(task, 1, 1) == ':' then
            await(a.main)
            vim.cmd(string.sub(task, 2))
          else
            local hook_output = { err = {}, output = {} }
            local hook_callbacks = {
              stderr = jobs.logging_callback(hook_output.err, hook_output.output, nil, disp, plugin_name),
              stdout = jobs.logging_callback(hook_output.err, hook_output.output, nil, disp, plugin_name),
            }
            local cmd
            local shell = os.getenv 'SHELL' or vim.o.shell
            if shell:find 'cmd.exe$' then
              cmd = { shell, '/c', task }
            else
              cmd = { shell, '-c', task }
            end
            hook_result = await(jobs.run(cmd, { capture_output = hook_callbacks, cwd = plugin.install_path })):map_err(
              function(err)
                return {
                  msg = string.format('Error running post update hook: %s', table.concat(hook_output.output, '\n')),
                  data = err,
                }
              end
            )

            if hook_result.err then
              return hook_result
            end
          end
        else
          -- TODO/NOTE: This case should also capture output in case of error. The minor difficulty is
          -- what to do if the plugin's run table (i.e. this case) already specifies output handling.

          hook_result = await(jobs.run(task)):map_err(function(err)
            return {
              msg = string.format('Error running post update hook: %s', vim.inspect(err)),
              data = err,
            }
          end)

          if hook_result.err then
            return hook_result
          end
        end
      end

      return hook_result
    else
      return result.ok()
    end
  end)
end

return plugin_utils
```

## File: `lua/packer/result.lua`
```
-- A simple Result<V, E> type to simplify control flow with installers and updaters
local result = {}

local ok_result_mt = {
  and_then = function(self, f, ...)
    local r = f(...)
    if r == nil then
      return result.err('Nil result in and_then! ' .. vim.inspect(debug.traceback()))
    end

    self.ok = r.ok
    self.err = r.err
    setmetatable(self, getmetatable(r))
    return self
  end,
  or_else = function(self)
    return self
  end,
  map_ok = function(self, f)
    self.ok = f(self.ok) or self.ok
    return self
  end,
  map_err = function(self)
    return self
  end,
}

ok_result_mt.__index = ok_result_mt

local err_result_mt = {
  and_then = function(self)
    return self
  end,
  or_else = function(self, f, ...)
    local r = f(...)
    if r == nil then
      return result.err('Nil result in or_else! ' .. vim.inspect(debug.traceback()))
    end

    self.ok = r.ok
    self.err = r.err
    setmetatable(self, getmetatable(r))
    return self
  end,
  map_ok = function(self)
    return self
  end,
  map_err = function(self, f)
    self.err = f(self.err) or self.err
    return self
  end,
}

err_result_mt.__index = err_result_mt

result.ok = function(val)
  if val == nil then
    val = true
  end
  local r = setmetatable({}, ok_result_mt)
  r.ok = val
  return r
end

result.err = function(err)
  if err == nil then
    err = true
  end
  local r = setmetatable({}, err_result_mt)
  r.err = err
  return r
end

return result
```

## File: `lua/packer/snapshot.lua`
```
local a = require 'packer.async'
local util = require 'packer.util'
local log = require 'packer.log'
local plugin_utils = require 'packer.plugin_utils'
local plugin_complete = require('packer').plugin_complete
local result = require 'packer.result'
local async = a.sync
local await = a.wait
local fmt = string.format

local config = {}

local snapshot = {
  completion = {},
}

snapshot.cfg = function(_config)
  config = _config
end

--- Completion for listing snapshots in `config.snapshot_path`
--- Intended to provide completion for PackerSnapshotDelete command
snapshot.completion.snapshot = function(lead, cmdline, pos)
  local completion_list = {}
  if config.snapshot_path == nil then
    return completion_list
  end

  local dir = vim.loop.fs_opendir(config.snapshot_path)

  if dir ~= nil then
    local res = vim.loop.fs_readdir(dir)
    while res ~= nil do
      for _, entry in ipairs(res) do
        if entry.type == 'file' and vim.startswith(entry.name, lead) then
          completion_list[#completion_list + 1] = entry.name
        end
      end

      res = vim.loop.fs_readdir(dir)
    end
  end

  vim.loop.fs_closedir(dir)
  return completion_list
end

--- Completion for listing single plugins before taking snapshot
--- Intended to provide completion for PackerSnapshot command
snapshot.completion.create = function(lead, cmdline, pos)
  local cmd_args = (vim.fn.split(cmdline, ' '))

  if #cmd_args > 1 then
    return plugin_complete(lead, cmdline, pos)
  end

  return {}
end

--- Completion for listing snapshots in `config.snapshot_path` and single plugins after
--- the first argument is provided
--- Intended to provide completion for PackerSnapshotRollback command
snapshot.completion.rollback = function(lead, cmdline, pos)
  local cmd_args = vim.split(cmdline, ' ')

  if #cmd_args > 2 then
    return plugin_complete(lead)
  else
    return snapshot.completion.snapshot(lead, cmdline, pos)
  end
end

--- Creates a with with `completed` and `failed` keys, each containing a map with plugin name as key and commit hash/error as value
--- @param plugins list
--- @return { ok: { failed : table<string, string>, completed : table<string, string>}}
local function generate_snapshot(plugins)
  local completed = {}
  local failed = {}
  local opt, start = plugin_utils.list_installed_plugins()
  local installed = vim.tbl_extend('error', start, opt)

  plugins = vim.tbl_filter(function(plugin)
    if installed[plugin.install_path] and plugin.type == plugin_utils.git_plugin_type then -- this plugin is installed
      return plugin
    end
  end, plugins)
  return async(function()
    for _, plugin in pairs(plugins) do
      local rev = await(plugin.get_rev())

      if rev.err then
        failed[plugin.short_name] =
          fmt("Snapshotting %s failed because of error '%s'", plugin.short_name, vim.inspect(rev.err))
      else
        completed[plugin.short_name] = { commit = rev.ok }
      end
    end

    return result.ok { failed = failed, completed = completed }
  end)
end

---Serializes a table of git-plugins with `short_name` as table key and another
---table with `commit`; the serialized tables will be written in the path `snapshot_path`
---provided, if there is already a snapshot it will be overwritten
---Snapshotting work only with `plugin_utils.git_plugin_type` type of plugins,
---other will be ignored.
---@param snapshot_path string realpath for snapshot file
---@param plugins table<string, any>[]
snapshot.create = function(snapshot_path, plugins)
  assert(type(snapshot_path) == 'string', fmt("filename needs to be a string but '%s' provided", type(snapshot_path)))
  assert(type(plugins) == 'table', fmt("plugins needs to be an array but '%s' provided", type(plugins)))
  return async(function()
    local commits = await(generate_snapshot(plugins))

    await(a.main)
    local snapshot_content = vim.fn.json_encode(commits.ok.completed)

    local status, res = pcall(function()
      return vim.fn.writefile({ snapshot_content }, snapshot_path) == 0
    end)

    if status and res then
      return result.ok {
        message = fmt("Snapshot '%s' complete", snapshot_path),
        completed = commits.ok.completed,
        failed = commits.ok.failed,
      }
    else
      return result.err { message = fmt("Error on creation of snapshot '%s': '%s'", snapshot_path, res) }
    end
  end)
end

local function fetch(plugin)
  local git = require 'packer.plugin_types.git'
  local opts = { capture_output = true, cwd = plugin.install_path, options = { env = git.job_env } }

  return async(function()
    return await(require('packer.jobs').run('git ' .. config.git.subcommands.fetch, opts))
  end)
end

---Rollbacks `plugins` to the hash specified in `snapshot_path` if exists.
---It automatically runs `git fetch --depth 999999 --progress` to retrieve the history
---@param snapshot_path string @ realpath to the snapshot file
---@param plugins list @ of `plugin_utils.git_plugin_type` type of plugins
---@return {ok: {completed: table<string, string>, failed: table<string, string[]>}}
snapshot.rollback = function(snapshot_path, plugins)
  assert(type(snapshot_path) == 'string', 'snapshot_path: expected string but got ' .. type(snapshot_path))
  assert(type(plugins) == 'table', 'plugins: expected table but got ' .. type(snapshot_path))
  log.debug('Rolling back to ' .. snapshot_path)
  local content = vim.fn.readfile(snapshot_path)
  ---@type string
  local plugins_snapshot = vim.fn.json_decode(content)
  if plugins_snapshot == nil then -- not valid snapshot file
    return result.err(fmt("Couldn't load '%s' file", snapshot_path))
  end

  local completed = {}
  local failed = {}

  return async(function()
    for _, plugin in pairs(plugins) do
      local function err_handler(err)
        failed[plugin.short_name] = failed[plugin.short_name] or {}
        failed[plugin.short_name][#failed[plugin.short_name] + 1] = err
      end

      if plugins_snapshot[plugin.short_name] then
        local commit = plugins_snapshot[plugin.short_name].commit
        if commit ~= nil then
          await(fetch(plugin))
            :map_err(err_handler)
            :and_then(await, plugin.revert_to(commit))
            :map_ok(function(ok)
              completed[plugin.short_name] = ok
            end)
            :map_err(err_handler)
        end
      end
    end

    return result.ok { completed = completed, failed = failed }
  end)
end

---Deletes the snapshot provided
---@param snapshot_name string absolute path or just a snapshot name
snapshot.delete = function(snapshot_name)
  assert(type(snapshot_name) == 'string', fmt('Expected string, got %s', type(snapshot_name)))
  ---@type string
  local snapshot_path = vim.loop.fs_realpath(snapshot_name)
    or vim.loop.fs_realpath(util.join_paths(config.snapshot_path, snapshot_name))

  if snapshot_path == nil then
    local warn = fmt("Snapshot '%s' is wrong or doesn't exist", snapshot_name)
    log.warn(warn)
    return
  end

  log.debug('Deleting ' .. snapshot_path)
  if vim.loop.fs_unlink(snapshot_path) then
    local info = 'Deleted ' .. snapshot_path
    log.info(info)
  else
    local warn = "Couldn't delete " .. snapshot_path
    log.warn(warn)
  end
end

return snapshot
```

## File: `lua/packer/update.lua`
```
local util = require 'packer.util'
local result = require 'packer.result'
local display = require 'packer.display'
local a = require 'packer.async'
local log = require 'packer.log'
local plugin_utils = require 'packer.plugin_utils'

local fmt = string.format
local async = a.sync
local await = a.wait

local config = nil

local function get_plugin_status(plugins, plugin_name, start_plugins, opt_plugins)
  local status = {}
  local plugin = plugins[plugin_name]
  status.wrong_type = (plugin.opt and vim.tbl_contains(start_plugins, util.join_paths(config.start_dir, plugin_name)))
    or vim.tbl_contains(opt_plugins, util.join_paths(config.opt_dir, plugin_name))
  return status
end

local function cfg(_config)
  config = _config
end

local function fix_plugin_type(plugin, results, fs_state)
  local from
  local to
  if plugin.opt then
    from = util.join_paths(config.start_dir, plugin.short_name)
    to = util.join_paths(config.opt_dir, plugin.short_name)
    fs_state.opt[to] = true
    fs_state.start[from] = nil
    fs_state.missing[plugin.short_name] = nil
  else
    from = util.join_paths(config.opt_dir, plugin.short_name)
    to = util.join_paths(config.start_dir, plugin.short_name)
    fs_state.start[to] = true
    fs_state.opt[from] = nil
    fs_state.missing[plugin.short_name] = nil
  end

  -- NOTE: If we stored all plugins somewhere off-package-path and used symlinks to put them in the
  -- right directories, this could be lighter-weight
  local success, msg = os.rename(from, to)
  if not success then
    log.error('Failed to move ' .. from .. ' to ' .. to .. ': ' .. msg)
    results.moves[plugin.short_name] = { from = from, to = to, result = result.err(success) }
  else
    log.debug('Moved ' .. plugin.short_name .. ' from ' .. from .. ' to ' .. to)
    results.moves[plugin.short_name] = { from = from, to = to, result = result.ok(success) }
  end
end

local function fix_plugin_types(plugins, plugin_names, results, fs_state)
  log.debug 'Fixing plugin types'
  results = results or {}
  results.moves = results.moves or {}
  -- NOTE: This function can only be run on plugins already installed
  for _, v in ipairs(plugin_names) do
    local plugin = plugins[v]
    local install_dir = util.join_paths(plugin.opt and config.start_dir or config.opt_dir, plugin.short_name)
    if vim.loop.fs_stat(install_dir) ~= nil then
      fix_plugin_type(plugin, results, fs_state)
    end
  end
  log.debug 'Done fixing plugin types'
end

local function update_plugin(plugin, display_win, results, opts)
  local plugin_name = util.get_plugin_full_name(plugin)
  -- TODO: This will have to change when separate packages are implemented
  local install_path = util.join_paths(config.pack_dir, plugin.opt and 'opt' or 'start', plugin.short_name)
  plugin.install_path = install_path
  return async(function()
    if plugin.lock or plugin.disable then
      return
    end
    display_win:task_start(plugin_name, 'updating...')
    local r = await(plugin.updater(display_win, opts))
    if r ~= nil and r.ok then
      local msg = 'up to date'
      if plugin.type == plugin_utils.git_plugin_type then
        local info = r.info
        local actual_update = info.revs[1] ~= info.revs[2]
        msg = actual_update and ('updated: ' .. info.revs[1] .. '...' .. info.revs[2]) or 'already up to date'
        if actual_update and not opts.preview_updates then
          log.debug(fmt('Updated %s: %s', plugin_name, vim.inspect(info)))
          r = r:and_then(await, plugin_utils.post_update_hook(plugin, display_win))
        end
      end

      if r.ok then
        display_win:task_succeeded(plugin_name, msg)
      end
    else
      display_win:task_failed(plugin_name, 'failed to update')
      local errmsg = '<unknown error>'
      if r ~= nil and r.err ~= nil then
        errmsg = r.err
      end
      log.debug(fmt('Failed to update %s: %s', plugin_name, vim.inspect(errmsg)))
    end

    results.updates[plugin_name] = r
    results.plugins[plugin_name] = plugin
  end)
end

local function do_update(_, plugins, update_plugins, display_win, results, opts)
  results = results or {}
  results.updates = results.updates or {}
  results.plugins = results.plugins or {}
  local tasks = {}
  for _, v in ipairs(update_plugins) do
    local plugin = plugins[v]
    if plugin == nil then
      log.error(fmt('Unknown plugin: %s', v))
    end
    if plugin and not plugin.frozen then
      if display_win == nil then
        display_win = display.open(config.display.open_fn or config.display.open_cmd)
      end

      table.insert(tasks, update_plugin(plugin, display_win, results, opts))
    end
  end

  if #tasks == 0 then
    log.info 'Nothing to update!'
  end

  return tasks, display_win
end

local update = setmetatable({ cfg = cfg }, { __call = do_update })

update.get_plugin_status = get_plugin_status
update.fix_plugin_types = fix_plugin_types

return update
```

## File: `lua/packer/util.lua`
```
local util = {}

util.map = function(func, seq)
  local result = {}
  for _, v in ipairs(seq) do
    table.insert(result, func(v))
  end

  return result
end

util.partition = function(sub, seq)
  local sub_vals = {}
  for _, val in ipairs(sub) do
    sub_vals[val] = true
  end

  local result = { {}, {} }
  for _, val in ipairs(seq) do
    if sub_vals[val] then
      table.insert(result[1], val)
    else
      table.insert(result[2], val)
    end
  end

  return unpack(result)
end

util.nonempty_or = function(opt, alt)
  if #opt > 0 then
    return opt
  else
    return alt
  end
end

if jit ~= nil then
  util.is_windows = jit.os == 'Windows'
else
  util.is_windows = package.config:sub(1, 1) == '\\'
end

if util.is_windows and vim.o.shellslash then
  util.use_shellslash = true
else
  util.use_shallslash = false
end

util.get_separator = function()
  if util.is_windows and not util.use_shellslash then
    return '\\'
  end
  return '/'
end

util.strip_trailing_sep = function(path)
  local res, _ = string.gsub(path, util.get_separator() .. '$', '', 1)
  return res
end

util.join_paths = function(...)
  local separator = util.get_separator()
  return table.concat({ ... }, separator)
end

util.get_plugin_short_name = function(plugin)
  local path = vim.fn.expand(plugin[1])
  local name_segments = vim.split(path, util.get_separator())
  local segment_idx = #name_segments
  local name = plugin.as or name_segments[segment_idx]
  while name == '' and segment_idx > 0 do
    name = name_segments[segment_idx]
    segment_idx = segment_idx - 1
  end
  return name, path
end

util.get_plugin_full_name = function(plugin)
  local plugin_name = plugin.name
  if plugin.branch and plugin.branch ~= 'master' then
    -- NOTE: maybe have to change the seperator here too
    plugin_name = plugin_name .. '/' .. plugin.branch
  end

  if plugin.rev then
    plugin_name = plugin_name .. '@' .. plugin.rev
  end

  return plugin_name
end

util.remove_ending_git_url = function(url)
  return vim.endswith(url, '.git') and url:sub(1, -5) or url
end

util.deep_extend = function(policy, ...)
  local result = {}
  local function helper(policy, k, v1, v2)
    if type(v1) ~= 'table' or type(v2) ~= 'table' then
      if policy == 'error' then
        error('Key ' .. vim.inspect(k) .. ' is already present with value ' .. vim.inspect(v1))
      elseif policy == 'force' then
        return v2
      else
        return v1
      end
    else
      return util.deep_extend(policy, v1, v2)
    end
  end

  for _, t in ipairs { ... } do
    for k, v in pairs(t) do
      if result[k] ~= nil then
        result[k] = helper(policy, k, result[k], v)
      else
        result[k] = v
      end
    end
  end

  return result
end

-- Credit to @crs for the original function
util.float = function(opts)
  local last_win = vim.api.nvim_get_current_win()
  local last_pos = vim.api.nvim_win_get_cursor(last_win)
  local columns = vim.o.columns
  local lines = vim.o.lines
  local width = math.ceil(columns * 0.8)
  local height = math.ceil(lines * 0.8 - 4)
  local left = math.ceil((columns - width) * 0.5)
  local top = math.ceil((lines - height) * 0.5 - 1)

  --- TODO: this is an impromptu fix for
  --- https://github.com/wbthomason/packer.nvim/pull/325#issuecomment-832874005
  --- ideally we should decide if the string argument passed to display openers is
  --- required or not
  if type(opts) ~= 'table' then
    opts = {}
  end

  opts = vim.tbl_deep_extend('force', {
    relative = 'editor',
    style = 'minimal',
    border = 'double',
    width = width,
    height = height,
    col = left,
    row = top,
  }, opts or {})

  local buf = vim.api.nvim_create_buf(false, true)
  local win = vim.api.nvim_open_win(buf, true, opts)

  function _G.__packer_restore_cursor()
    vim.api.nvim_set_current_win(last_win)
    vim.api.nvim_win_set_cursor(last_win, last_pos)
  end

  vim.cmd 'autocmd! BufWipeout <buffer> lua __packer_restore_cursor()'

  return true, win, buf
end

return util
```

## File: `lua/packer/plugin_types/git.lua`
```
local util = require 'packer.util'
local jobs = require 'packer.jobs'
local a = require 'packer.async'
local result = require 'packer.result'
local log = require 'packer.log'
local await = a.wait
local async = a.sync
local fmt = string.format

local vim = vim

local git = {}

local blocked_env_vars = {
  GIT_DIR = true,
  GIT_INDEX_FILE = true,
  GIT_OBJECT_DIRECTORY = true,
  GIT_TERMINAL_PROMPT = true,
  GIT_WORK_TREE = true,
  GIT_COMMON_DIR = true,
}

local function ensure_git_env()
  if git.job_env == nil then
    local job_env = {}
    for k, v in pairs(vim.fn.environ()) do
      if not blocked_env_vars[k] then
        table.insert(job_env, k .. '=' .. v)
      end
    end

    table.insert(job_env, 'GIT_TERMINAL_PROMPT=0')
    git.job_env = job_env
  end
end

local function has_wildcard(tag)
  if not tag then
    return false
  end
  return string.match(tag, '*') ~= nil
end

local break_tag_pattern = [=[[bB][rR][eE][aA][kK]!?:]=]
local breaking_change_pattern = [=[[bB][rR][eE][aA][kK][iI][nN][gG][ _][cC][hH][aA][nN][gG][eE]]=]
local type_exclam_pattern = [=[[a-zA-Z]+!:]=]
local type_scope_exclam_pattern = [=[[a-zA-Z]+%([^)]+%)!:]=]
local function mark_breaking_commits(plugin, commit_bodies)
  local commits = vim.gsplit(table.concat(commit_bodies, '\n'), '===COMMIT_START===', true)
  for commit in commits do
    local commit_parts = vim.split(commit, '===BODY_START===')
    local body = commit_parts[2]
    local lines = vim.split(commit_parts[1], '\n')
    local is_breaking = (
      body ~= nil
      and (
        (string.match(body, breaking_change_pattern) ~= nil)
        or (string.match(body, break_tag_pattern) ~= nil)
        or (string.match(body, type_exclam_pattern) ~= nil)
        or (string.match(body, type_scope_exclam_pattern) ~= nil)
      )
    )
      or (
        lines[2] ~= nil
        and (
          (string.match(lines[2], breaking_change_pattern) ~= nil)
          or (string.match(lines[2], break_tag_pattern) ~= nil)
          or (string.match(lines[2], type_exclam_pattern) ~= nil)
          or (string.match(lines[2], type_scope_exclam_pattern) ~= nil)
        )
      )
    if is_breaking then
      plugin.breaking_commits[#plugin.breaking_commits + 1] = lines[1]
    end
  end
end

local config = nil
git.cfg = function(_config)
  config = _config.git
  config.base_dir = _config.package_root
  config.default_base_dir = util.join_paths(config.base_dir, _config.plugin_package)
  config.exec_cmd = config.cmd .. ' '
  ensure_git_env()
end

---Resets a git repo `dest` to `commit`
---@param dest string @ path to the local git repo
---@param commit string @ commit hash
---@return function @ async function
local function reset(dest, commit)
  local reset_cmd = fmt(config.exec_cmd .. config.subcommands.revert_to, commit)
  local opts = { capture_output = true, cwd = dest, options = { env = git.job_env } }
  return async(function()
    return await(jobs.run(reset_cmd, opts))
  end)
end

local handle_checkouts = function(plugin, dest, disp, opts)
  local plugin_name = util.get_plugin_full_name(plugin)
  return async(function()
    if disp ~= nil then
      disp:task_update(plugin_name, 'fetching reference...')
    end
    local output = jobs.output_table()
    local callbacks = {
      stdout = jobs.logging_callback(output.err.stdout, output.data.stdout, nil, disp, plugin_name),
      stderr = jobs.logging_callback(output.err.stderr, output.data.stderr),
    }

    local job_opts = { capture_output = callbacks, cwd = dest, options = { env = git.job_env } }

    local r = result.ok()

    if plugin.tag and has_wildcard(plugin.tag) then
      disp:task_update(plugin_name, fmt('getting tag for wildcard %s...', plugin.tag))
      local fetch_tags = config.exec_cmd .. fmt(config.subcommands.tags_expand_fmt, plugin.tag)
      r:and_then(await, jobs.run(fetch_tags, job_opts))
      local data = output.data.stdout[1]
      if data then
        plugin.tag = vim.split(data, '\n')[1]
      else
        log.warn(
          fmt('Wildcard expansion did not found any tag for plugin %s: defaulting to latest commit...', plugin.name)
        )
        plugin.tag = nil -- Wildcard is not found, then we bypass the tag
      end
    end

    if plugin.branch or (plugin.tag and not opts.preview_updates) then
      local branch_or_tag = plugin.branch and plugin.branch or plugin.tag
      if disp ~= nil then
        disp:task_update(plugin_name, fmt('checking out %s %s...', plugin.branch and 'branch' or 'tag', branch_or_tag))
      end
      r:and_then(await, jobs.run(config.exec_cmd .. fmt(config.subcommands.checkout, branch_or_tag), job_opts))
        :map_err(function(err)
          return {
            msg = fmt(
              'Error checking out %s %s for %s',
              plugin.branch and 'branch' or 'tag',
              branch_or_tag,
              plugin_name
            ),
            data = err,
            output = output,
          }
        end)
    end

    if plugin.commit then
      if disp ~= nil then
        disp:task_update(plugin_name, fmt('checking out %s...', plugin.commit))
      end
      r:and_then(await, jobs.run(config.exec_cmd .. fmt(config.subcommands.checkout, plugin.commit), job_opts))
        :map_err(function(err)
          return {
            msg = fmt('Error checking out commit %s for %s', plugin.commit, plugin_name),
            data = err,
            output = output,
          }
        end)
    end

    return r:map_ok(function(ok)
      return { status = ok, output = output }
    end):map_err(function(err)
      if not err.msg then
        return {
          msg = fmt('Error updating %s: %s', plugin_name, table.concat(err, '\n')),
          data = err,
          output = output,
        }
      end

      err.output = output
      return err
    end)
  end)
end

local get_rev = function(plugin)
  local plugin_name = util.get_plugin_full_name(plugin)

  local rev_cmd = config.exec_cmd .. config.subcommands.get_rev

  return async(function()
    local rev = await(jobs.run(rev_cmd, { cwd = plugin.install_path, options = { env = git.job_env }, capture_output = true }))
      :map_ok(function(ok)
        local _, r = next(ok.output.data.stdout)
        return r
      end)
      :map_err(function(err)
        local _, msg = fmt('%s: %s', plugin_name, next(err.output.data.stderr))
        return msg
      end)

    return rev
  end)
end

local split_messages = function(messages)
  local lines = {}
  for _, message in ipairs(messages) do
    vim.list_extend(lines, vim.split(message, '\n'))
    table.insert(lines, '')
  end
  return lines
end

git.setup = function(plugin)
  local plugin_name = util.get_plugin_full_name(plugin)
  local install_to = plugin.install_path
  local install_cmd =
    vim.split(config.exec_cmd .. fmt(config.subcommands.install, plugin.commit and 999999 or config.depth), '%s+')

  local submodule_cmd = config.exec_cmd .. config.subcommands.submodules
  local rev_cmd = config.exec_cmd .. config.subcommands.get_rev
  local update_cmd = config.exec_cmd .. config.subcommands.update
  local update_head_cmd = config.exec_cmd .. config.subcommands.update_head
  local fetch_cmd = config.exec_cmd .. config.subcommands.fetch
  if plugin.commit or plugin.tag then
    update_cmd = fetch_cmd
  end

  local branch_cmd = config.exec_cmd .. config.subcommands.current_branch
  local current_commit_cmd = vim.split(config.exec_cmd .. config.subcommands.get_header, '%s+')
  for i, arg in ipairs(current_commit_cmd) do
    current_commit_cmd[i] = string.gsub(arg, 'FMT', config.subcommands.diff_fmt)
  end

  if plugin.branch or (plugin.tag and not has_wildcard(plugin.tag)) then
    install_cmd[#install_cmd + 1] = '--branch'
    install_cmd[#install_cmd + 1] = plugin.branch and plugin.branch or plugin.tag
  end

  install_cmd[#install_cmd + 1] = plugin.url
  install_cmd[#install_cmd + 1] = install_to

  local needs_checkout = plugin.tag ~= nil or plugin.commit ~= nil or plugin.branch ~= nil

  plugin.installer = function(disp)
    local output = jobs.output_table()
    local callbacks = {
      stdout = jobs.logging_callback(output.err.stdout, output.data.stdout),
      stderr = jobs.logging_callback(output.err.stderr, output.data.stderr, nil, disp, plugin_name),
    }

    local installer_opts = {
      capture_output = callbacks,
      timeout = config.clone_timeout,
      options = { env = git.job_env },
    }

    return async(function()
      disp:task_update(plugin_name, 'cloning...')
      local r = await(jobs.run(install_cmd, installer_opts))

      installer_opts.cwd = install_to
      r:and_then(await, jobs.run(submodule_cmd, installer_opts))

      if plugin.commit then
        disp:task_update(plugin_name, fmt('checking out %s...', plugin.commit))
        r:and_then(await, jobs.run(config.exec_cmd .. fmt(config.subcommands.checkout, plugin.commit), installer_opts))
          :map_err(function(err)
            return {
              msg = fmt('Error checking out commit %s for %s', plugin.commit, plugin_name),
              data = { err, output },
            }
          end)
      end

      r:and_then(await, jobs.run(current_commit_cmd, installer_opts))
        :map_ok(function(_)
          plugin.messages = output.data.stdout
        end)
        :map_err(function(err)
          plugin.output = { err = output.data.stderr }
          if not err.msg then
            return {
              msg = fmt('Error installing %s: %s', plugin_name, table.concat(output.data.stderr, '\n')),
              data = { err, output },
            }
          end
        end)

      return r
    end)
  end

  plugin.remote_url = function()
    return async(function()
      return await(
        jobs.run(
          fmt('%s remote get-url origin', config.exec_cmd),
          { capture_output = true, cwd = plugin.install_path, options = { env = git.job_env } }
        )
      ):map_ok(function(data)
        return { remote = data.output.data.stdout[1] }
      end)
    end)
  end

  plugin.updater = function(disp, opts)
    return async(function()
      local update_info = { err = {}, revs = {}, output = {}, messages = {} }
      local function exit_ok(r)
        if #update_info.err > 0 or r.exit_code ~= 0 then
          return result.err(r)
        end
        return result.ok(r)
      end

      local rev_onread = jobs.logging_callback(update_info.err, update_info.revs)
      local rev_callbacks = { stdout = rev_onread, stderr = rev_onread }
      disp:task_update(plugin_name, 'checking current commit...')
      local r = await(
        jobs.run(
          rev_cmd,
          { success_test = exit_ok, capture_output = rev_callbacks, cwd = install_to, options = { env = git.job_env } }
        )
      ):map_err(function(err)
        plugin.output = { err = vim.list_extend(update_info.err, update_info.revs), data = {} }

        return {
          msg = fmt('Error getting current commit for %s: %s', plugin_name, table.concat(update_info.revs, '\n')),
          data = err,
        }
      end)

      local current_branch
      disp:task_update(plugin_name, 'checking current branch...')
      r:and_then(
        await,
        jobs.run(
          branch_cmd,
          { success_test = exit_ok, capture_output = true, cwd = install_to, options = { env = git.job_env } }
        )
      )
        :map_ok(function(ok)
          current_branch = ok.output.data.stdout[1]
        end)
        :map_err(function(err)
          plugin.output = { err = vim.list_extend(update_info.err, update_info.revs), data = {} }

          return {
            msg = fmt('Error checking current branch for %s: %s', plugin_name, table.concat(update_info.revs, '\n')),
            data = err,
          }
        end)

      if not needs_checkout then
        local origin_branch = ''
        disp:task_update(plugin_name, 'checking origin branch...')
        local origin_refs_path = util.join_paths(install_to, '.git', 'refs', 'remotes', 'origin', 'HEAD')
        local origin_refs_file = vim.loop.fs_open(origin_refs_path, 'r', 438)
        if origin_refs_file ~= nil then
          local origin_refs_stat = vim.loop.fs_fstat(origin_refs_file)
          -- NOTE: This should check for errors
          local origin_refs = vim.split(vim.loop.fs_read(origin_refs_file, origin_refs_stat.size, 0), '\n')
          vim.loop.fs_close(origin_refs_file)
          if #origin_refs > 0 then
            origin_branch = string.match(origin_refs[1], [[^ref: refs/remotes/origin/(.*)]])
          end
        end

        if current_branch ~= origin_branch then
          needs_checkout = true
          plugin.branch = origin_branch
        end
      end

      local update_callbacks = {
        stdout = jobs.logging_callback(update_info.err, update_info.output),
        stderr = jobs.logging_callback(update_info.err, update_info.output, nil, disp, plugin_name),
      }
      local update_opts = {
        success_test = exit_ok,
        capture_output = update_callbacks,
        cwd = install_to,
        options = { env = git.job_env },
      }

      if needs_checkout then
        r:and_then(await, jobs.run(config.exec_cmd .. config.subcommands.fetch, update_opts))
        r:and_then(await, handle_checkouts(plugin, install_to, disp, opts))
        local function merge_output(res)
          if res.output ~= nil then
            vim.list_extend(update_info.err, res.output.err.stderr)
            vim.list_extend(update_info.err, res.output.err.stdout)
            vim.list_extend(update_info.output, res.output.data.stdout)
            vim.list_extend(update_info.output, res.output.data.stderr)
          end
        end

        r:map_ok(merge_output)
        r:map_err(function(err)
          merge_output(err)
          plugin.output = { err = vim.list_extend(update_info.err, update_info.output), data = {} }
          local errmsg = '<unknown error>'
          if err ~= nil and err.msg ~= nil then
            errmsg = err.msg
          end
          return { msg = errmsg .. ' ' .. table.concat(update_info.output, '\n'), data = err.data }
        end)
      end

      if opts.preview_updates then
        disp:task_update(plugin_name, 'fetching updates...')
        r:and_then(await, jobs.run(fetch_cmd, update_opts))
      elseif opts.pull_head then
        disp:task_update(plugin_name, 'pulling updates from head...')
        r:and_then(await, jobs.run(update_head_cmd, update_opts))
      else
        disp:task_update(plugin_name, 'pulling updates...')
        r:and_then(await, jobs.run(update_cmd, update_opts)):and_then(await, jobs.run(submodule_cmd, update_opts))
      end
      r:map_err(function(err)
        plugin.output = { err = vim.list_extend(update_info.err, update_info.output), data = {} }

        return {
          msg = fmt('Error getting updates for %s: %s', plugin_name, table.concat(update_info.output, '\n')),
          data = err,
        }
      end)

      local post_rev_cmd
      if plugin.tag ~= nil then
        -- NOTE that any tag wildcard should already been expanded to a specific commit at this point
        post_rev_cmd = string.gsub(rev_cmd, 'HEAD', string.format('%s^{}', plugin.tag))
      elseif opts.preview_updates then
        post_rev_cmd = string.gsub(rev_cmd, 'HEAD', 'FETCH_HEAD')
      else
        post_rev_cmd = rev_cmd
      end
      disp:task_update(plugin_name, 'checking updated commit...')
      r:and_then(
        await,
        jobs.run(post_rev_cmd, {
          success_test = exit_ok,
          capture_output = rev_callbacks,
          cwd = install_to,
          options = { env = git.job_env },
        })
      ):map_err(function(err)
        plugin.output = { err = vim.list_extend(update_info.err, update_info.revs), data = {} }
        return {
          msg = fmt('Error checking updated commit for %s: %s', plugin_name, table.concat(update_info.revs, '\n')),
          data = err,
        }
      end)

      if r.ok then
        if update_info.revs[1] ~= update_info.revs[2] then
          local commit_headers_onread = jobs.logging_callback(update_info.err, update_info.messages)
          local commit_headers_callbacks = { stdout = commit_headers_onread, stderr = commit_headers_onread }

          local diff_cmd = string.format(config.subcommands.diff, update_info.revs[1], update_info.revs[2])
          local commit_headers_cmd = vim.split(config.exec_cmd .. diff_cmd, '%s+')
          for i, arg in ipairs(commit_headers_cmd) do
            commit_headers_cmd[i] = string.gsub(arg, 'FMT', config.subcommands.diff_fmt)
          end

          disp:task_update(plugin_name, 'getting commit messages...')
          r:and_then(
            await,
            jobs.run(commit_headers_cmd, {
              success_test = exit_ok,
              capture_output = commit_headers_callbacks,
              cwd = install_to,
              options = { env = git.job_env },
            })
          )

          plugin.output = { err = update_info.err, data = update_info.output }
          if r.ok then
            plugin.messages = update_info.messages
            plugin.revs = update_info.revs
          end

          if config.mark_breaking_changes then
            local commit_bodies = { err = {}, output = {} }
            local commit_bodies_onread = jobs.logging_callback(commit_bodies.err, commit_bodies.output)
            local commit_bodies_callbacks = { stdout = commit_bodies_onread, stderr = commit_bodies_onread }
            local commit_bodies_cmd = config.exec_cmd .. config.subcommands.get_bodies
            if opts.preview_updates then
              commit_bodies_cmd = config.exec_cmd .. config.subcommands.get_fetch_bodies
            end
            disp:task_update(plugin_name, 'checking for breaking changes...')
            r:and_then(
              await,
              jobs.run(commit_bodies_cmd, {
                success_test = exit_ok,
                capture_output = commit_bodies_callbacks,
                cwd = install_to,
                options = { env = git.job_env },
              })
            ):map_ok(function(ok)
              plugin.breaking_commits = {}
              mark_breaking_commits(plugin, commit_bodies.output)
              return ok
            end)
          end
        else
          plugin.revs = update_info.revs
          plugin.messages = update_info.messages
        end
      else
        plugin.output.err = vim.list_extend(plugin.output.err, update_info.messages)
      end

      r.info = update_info
      return r
    end)
  end

  plugin.diff = function(commit, callback)
    async(function()
      local diff_cmd = config.exec_cmd .. fmt(config.subcommands.git_diff_fmt, commit)
      local diff_info = { err = {}, output = {}, messages = {} }
      local diff_onread = jobs.logging_callback(diff_info.err, diff_info.messages)
      local diff_callbacks = { stdout = diff_onread, stderr = diff_onread }
      return await(jobs.run(diff_cmd, { capture_output = diff_callbacks, cwd = install_to, options = { env = git.job_env } }))
        :map_ok(function(_)
          return callback(split_messages(diff_info.messages))
        end)
        :map_err(function(err)
          return callback(nil, err)
        end)
    end)()
  end

  plugin.revert_last = function()
    local r = result.ok()
    async(function()
      local revert_cmd = config.exec_cmd .. config.subcommands.revert
      r:and_then(
        await,
        jobs.run(revert_cmd, { capture_output = true, cwd = install_to, options = { env = git.job_env } })
      )
      if needs_checkout then
        r:and_then(await, handle_checkouts(plugin, install_to, nil, {}))
      end
      return r
    end)()
    return r
  end

  ---Reset the plugin to `commit`
  ---@param commit string
  plugin.revert_to = function(commit)
    assert(type(commit) == 'string', fmt("commit: string expected but '%s' provided", type(commit)))
    return async(function()
      require('packer.log').debug(fmt("Reverting '%s' to commit '%s'", plugin.name, commit))
      return await(reset(install_to, commit))
    end)
  end

  ---Returns HEAD's short hash
  ---@return string
  plugin.get_rev = function()
    return get_rev(plugin)
  end
end

return git
```

## File: `lua/packer/plugin_types/local.lua`
```
local a = require 'packer.async'
local log = require 'packer.log'
local util = require 'packer.util'
local result = require 'packer.result'

local async = a.sync
local await = a.wait
local fmt = string.format

local config = nil
local function cfg(_config)
  config = _config
end

-- Due to #679, we know that fs_symlink requires admin privileges on Windows. This is a workaround,
-- as suggested by @nonsleepr.

local symlink_fn
if util.is_windows then
  symlink_fn = function(path, new_path, flags, callback)
    flags = flags or {}
    flags.junction = true
    return vim.loop.fs_symlink(path, new_path, flags, callback)
  end
else
  symlink_fn = vim.loop.fs_symlink
end

local symlink = a.wrap(symlink_fn)
local unlink = a.wrap(vim.loop.fs_unlink)

local function setup_local(plugin)
  local from = vim.loop.fs_realpath(util.strip_trailing_sep(plugin.path))
  local to = util.strip_trailing_sep(plugin.install_path)

  local plugin_name = util.get_plugin_full_name(plugin)
  plugin.installer = function(disp)
    return async(function()
      disp:task_update(plugin_name, 'making symlink...')
      local err, success = await(symlink(from, to, { dir = true }))
      if not success then
        plugin.output = { err = { err } }
        return result.err(err)
      end
      return result.ok()
    end)
  end

  plugin.updater = function(disp)
    return async(function()
      local r = result.ok()
      disp:task_update(plugin_name, 'checking symlink...')
      local resolved_path = vim.loop.fs_realpath(to)
      if resolved_path ~= from then
        disp:task_update(plugin_name, 'updating symlink...')
        r = await(unlink(to)):and_then(symlink(from, to, { dir = true }))
      end

      return r
    end)
  end

  plugin.revert_last = function(_)
    log.warn "Can't revert a local plugin!"
    return result.ok()
  end
end

return { setup = setup_local, cfg = cfg }
```

## File: `tests/helpers.lua`
```
local util = require 'packer.util'

local M = { base_dir = '/tmp/__packer_tests__' }

---Create a fake git repository
---@param name string
---@param base string
function M.create_git_dir(name, base)
  base = base or M.base_dir
  local repo_path = util.join_paths(base, name)
  local path = util.join_paths(repo_path, '.git')
  if vim.fn.isdirectory(path) > 0 then
    M.cleanup_dirs(path)
  end
  vim.fn.mkdir(path, 'p')
  return repo_path
end

---Remove directories created for test purposes
---@vararg string
function M.cleanup_dirs(...)
  for _, dir in ipairs { ... } do
    vim.fn.delete(dir, 'rf')
  end
end

return M
```

## File: `tests/local_plugin_spec.lua`
```
local a = require('plenary.async_lib.tests')
local await = require('packer.async').wait
local local_plugin = require('packer.plugin_types.local')
local packer_path = vim.fn.stdpath('data') .. '/site/pack/packer/start/'
local helpers = require('tests.helpers')

a.describe('Local plugin -', function()
  a.describe('installer', function()
    local local_plugin_path
    local repo_name = 'test.nvim'
    local plugin_install_path = packer_path .. repo_name

    before_each(function()
      vim.fn.mkdir(packer_path, 'p')
      local_plugin_path = helpers.create_git_dir(repo_name)
    end)

    after_each(function() helpers.cleanup_dirs(local_plugin_path, plugin_install_path) end)

    a.it('should create a symlink', function()
      local plugin_spec = {
        name = local_plugin_path,
        path = local_plugin_path,
        install_path = plugin_install_path
      }

      local_plugin.setup(plugin_spec)
      await(plugin_spec.installer({task_update = function() end}))

      assert.equal('link', vim.loop.fs_lstat(plugin_install_path).type)
    end)
  end)
end)
```

## File: `tests/minimal.vim`
```
set rtp+=.
set rtp+=../plenary.nvim
runtime! plugin/plenary.vim
```

## File: `tests/packer_plugin_utils_spec.lua`
```
local a = require('plenary.async_lib.tests')
local await = require('packer.async').wait
local plugin_utils = require("packer.plugin_utils")
local packer_path = vim.fn.stdpath("data") .. "/site/pack/packer/start/"

a.describe("Packer post update hooks", function()
  local test_plugin_path = packer_path .. "test_plugin/"
  local run_hook = plugin_utils.post_update_hook

  before_each(function() vim.fn.mkdir(test_plugin_path, "p") end)

  after_each(function() vim.fn.delete(test_plugin_path, "rf") end)

  a.it("should run the command in the correct folder", function()
    local plugin_spec = {
      name = "test/test_plugin",
      install_path = test_plugin_path,
      run = "touch 'this_file_should_exist'"
    }

    await(run_hook(plugin_spec, {task_update = function() end}))

    assert.truthy(vim.loop.fs_stat(test_plugin_path .. "this_file_should_exist"))
  end)
end)
```

## File: `tests/packer_use_spec.lua`
```
local packer = require("packer")
local use = packer.use
local packer_path = vim.fn.stdpath("data").."/site/pack/packer/start/"

describe("Packer use tests", function()
  after_each(function()
    packer.reset()
  end)

  it("should set the correct install path", function ()
    local spec = {"test/plugin1"}
    packer.startup(function()
      use(spec)
    end)
    packer.__manage_all()
    assert.truthy(spec.install_path)
    assert.equal(spec.install_path, packer_path .. spec.short_name)
  end)

  it("should add metadata to a plugin from a spec", function ()
    local spec = {"test/plugin1"}
    packer.startup(function()
      use(spec)
    end)
    packer.__manage_all()
    assert.equal(spec.name, "test/plugin1")
    assert.equal(spec.path, "test/plugin1")
  end)
end)
```

## File: `tests/plugin_utils_spec.lua`
```
local a = require('plenary.async_lib.tests')
local await = require('packer.async').wait
local async = require('packer.async').sync
local plugin_utils = require('packer.plugin_utils')
local helpers = require("tests.helpers")

local fmt = string.format

a.describe('Plugin utils -', function()

  a.describe('find_missing_plugins', function()
    local repo_name = "test.nvim"
    local path

    plugin_utils.cfg({start_dir = helpers.base_dir})

    before_each(function() path = helpers.create_git_dir(repo_name) end)

    after_each(function() helpers.cleanup_dirs("tmp/packer") end)

    a.it('should pick up plugins with a different remote URL', function()
      local test_repo_name = fmt('user2/%s', repo_name)
      local plugins = {
        [repo_name] = {
          opt = false,
          type = "git",
          name = fmt("user1/%s", repo_name),
          short_name = repo_name,
          remote_url = function()
            return async(function()
              return {ok = {remote = fmt('https://github.com/%s', test_repo_name)}}
            end)
          end
        }
      }
      local result = await(plugin_utils.find_missing_plugins(plugins, {}, {[path] = true}))
      assert.truthy(result)
      assert.equal(1, #vim.tbl_keys(result))
    end)

    a.it('should not pick up plugins with the same remote URL', function()
      local test_repo_name = fmt('user1/%s', repo_name)
      local plugins = {
        [repo_name] = {
          opt = false,
          type = "git",
          name = test_repo_name,
          short_name = repo_name,
          remote_url = function()
            return async(function()
              return {ok = {remote = fmt('https://github.com/%s', test_repo_name)}}
            end)
          end
        }
      }
      local result = await(plugin_utils.find_missing_plugins(plugins, {}, {[path] = true}))
      assert.truthy(result)
      assert.equal(0, #result)
    end)

    a.it('should handle ssh git urls', function()
      local test_repo_name = fmt('user2/%s', repo_name)
      local plugins = {
        [repo_name] = {
          opt = false,
          type = "git",
          name = fmt("user1/%s", repo_name),
          short_name = repo_name,
          remote_url = function()
            return async(function()
              return {ok = {remote = fmt('git@github.com:%s.git', test_repo_name)}}
            end)
          end
        }
      }
      local result = await(plugin_utils.find_missing_plugins(plugins, {}, {[path] = true}))
      assert.truthy(result)
      assert.equal(1, #vim.tbl_keys(result))
    end)
  end)
end)
```

## File: `tests/snapshot_spec.lua`
```
local before_each = require('plenary.busted').before_each
local a = require 'plenary.async_lib.tests'
local util = require 'packer.util'
local mocked_plugin_utils = require 'packer.plugin_utils'
local log = require 'packer.log'
local async = require('packer.async').sync
local await = require('packer.async').wait
local wait_all = require('packer.async').wait_all
local main = require('packer.async').main
local packer = require 'packer'
local jobs = require 'packer.jobs'
local git = require 'packer.plugin_types.git'
local join_paths = util.join_paths
local stdpath = vim.fn.stdpath
local fmt = string.format

local config = {
  ensure_dependencies = true,
  snapshot = nil,
  snapshot_path = join_paths(stdpath 'cache', 'packer.nvim'),
  package_root = join_paths(stdpath 'data', 'site', 'pack'),
  compile_path = join_paths(stdpath 'config', 'plugin', 'packer_compiled.lua'),
  plugin_package = 'packer',
  max_jobs = nil,
  auto_clean = true,
  compile_on_sync = true,
  disable_commands = false,
  opt_default = false,
  transitive_opt = true,
  transitive_disable = true,
  auto_reload_compiled = true,
  git = {
    mark_breaking_changes = true,
    cmd = 'git',
    subcommands = {
      update = 'pull --ff-only --progress --rebase=false',
      install = 'clone --depth %i --no-single-branch --progress',
      fetch = 'fetch --depth 999999 --progress',
      checkout = 'checkout %s --',
      update_branch = 'merge --ff-only @{u}',
      current_branch = 'rev-parse --abbrev-ref HEAD',
      diff = 'log --color=never --pretty=format:FMT --no-show-signature HEAD@{1}...HEAD',
      diff_fmt = '%%h %%s (%%cr)',
      git_diff_fmt = 'show --no-color --pretty=medium %s',
      get_rev = 'rev-parse --short HEAD',
      get_header = 'log --color=never --pretty=format:FMT --no-show-signature HEAD -n 1',
      get_bodies = 'log --color=never --pretty=format:"===COMMIT_START===%h%n%s===BODY_START===%b" --no-show-signature HEAD@{1}...HEAD',
      submodules = 'submodule update --init --recursive --progress',
      revert = 'reset --hard HEAD@{1}',
      revert_to = 'reset --hard %s --',
    },
    depth = 1,
    clone_timeout = 60,
    default_url_format = 'https://github.com/%s.git',
  },
  display = {
    non_interactive = false,
    open_fn = nil,
    open_cmd = '65vnew',
    working_sym = '⟳',
    error_sym = '✗',
    done_sym = '✓',
    removed_sym = '-',
    moved_sym = '→',
    header_sym = '━',
    header_lines = 2,
    title = 'packer.nvim',
    show_all_info = true,
    prompt_border = 'double',
    keybindings = { quit = 'q', toggle_info = '<CR>', diff = 'd', prompt_revert = 'r' },
  },
  luarocks = { python_cmd = 'python' },
  log = { level = 'trace' },
  profile = { enable = false },
}

git.cfg(config)

--[[ For testing purposes the spec file is made up so that when running `packer`
it could manage itself as if it was in `~/.local/share/nvim/site/pack/packer/start/` --]]
local install_path = vim.fn.getcwd()

mocked_plugin_utils.list_installed_plugins = function()
  return { [install_path] = true }, {}
end

local old_require = _G.require

_G.require = function(modname)
  if modname == 'plugin_utils' then
    return mocked_plugin_utils
  end

  return old_require(modname)
end

local spec = { 'wbthomason/packer.nvim' }

local function exec_cmd(cmd, opts)
  return async(function()
    local r = await(jobs.run(cmd, opts))
    if r.err then
      print(fmt("Failed on command '%s': %s", cmd, vim.inspect(r.err)))
    end
    assert.is_not_nil(r.ok)
    local _, result = next(r.ok.output.data.stdout)
    return result
  end)
end

local snapshotted_plugins = {}
a.describe('Packer testing ', function()
  local snapshot_name = 'test'
  local test_path = join_paths(config.snapshot_path, snapshot_name)
  local snapshot = require 'packer.snapshot'
  snapshot.cfg(config)

  before_each(function()
    packer.reset()
    packer.init(config)
    packer.use(spec)
    packer.__manage_all()
  end)

  after_each(function()
    spec = { 'wbthomason/packer.nvim' }
    spec.install_path = install_path
  end)

  a.describe('snapshot.create()', function()
    a.it(fmt("create snapshot in '%s'", test_path), function()
      local result = await(snapshot.create(test_path, { spec }))
      local stat = vim.loop.fs_stat(test_path)
      assert.truthy(stat)
    end)

    a.it("checking if snapshot content corresponds to plugins'", function()
      async(function()
        local file_content = vim.fn.readfile(test_path)
        snapshotted_plugins = vim.fn.json_decode(file_content)
        local expected_rev = await(spec.get_rev())
        assert.are.equals(expected_rev.ok, snapshotted_plugins['packer.nvim'].commit)
      end)()
    end)
  end)

  a.describe('packer.delete()', function()
    a.it(fmt("delete '%s' snapshot", snapshot_name), function()
      snapshot.delete(snapshot_name)
      local stat = vim.loop.fs_stat(test_path)
      assert.falsy(stat)
    end)
  end)

  a.describe('packer.rollback()', function()
    local rollback_snapshot_name = 'rollback_test'
    local rollback_test_path = join_paths(config.snapshot_path, rollback_snapshot_name)
    local prev_commit_cmd = 'git rev-parse --short HEAD~5'
    local get_rev_cmd = 'git rev-parse --short HEAD'

    local opts = { capture_output = true, cwd = spec.install_path, options = { env = git.job_env } }

    a.it("restore 'packer' to the commit hash HEAD~5", function()
      async(function()
        local commit = await(exec_cmd(prev_commit_cmd, opts))
        snapshotted_plugins['packer.nvim'] = { commit = commit }
        await(main)
        local encoded_json = vim.fn.json_encode(snapshotted_plugins)
        vim.fn.writefile({ encoded_json }, rollback_test_path)
        await(snapshot.rollback(rollback_test_path, { spec }))
        local rev = await(exec_cmd(get_rev_cmd, opts))
        assert.are.equals(snapshotted_plugins['packer.nvim'].commit, rev)
      end)()
    end)
  end)
end)
```

