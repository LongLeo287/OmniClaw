---
id: github.com-junegunn-vim-plug-45d664eb-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:17.093311
---

# KNOWLEDGE EXTRACT: github.com_junegunn_vim-plug_45d664eb
> **Extracted on:** 2026-04-01 08:57:40
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519882/github.com_junegunn_vim-plug_45d664eb

---

## File: `.gitignore`
```
doc/tags
```

## File: `.travis.yml`
```yaml
language: minimal
env:
  global:
    - DEPS=$HOME/deps
    - PATH=$DEPS/bin:$PATH
jobs:
  include:
    - env: ENV=vim80-bionic
      dist: bionic
      stage: vim8
    - env: ENV=vim-nightly
      dist: trusty
      stage: vim8
    - env: ENV=neovim-stable
      dist: bionic
      addons: {apt: {packages: [neovim], sources: [{sourceline: 'ppa:neovim-ppa/stable'}]}}
      stage: neovim
    - env: ENV=neovim-nightly
      dist: bionic
      addons: {apt: {packages: [neovim], sources: [{sourceline: 'ppa:neovim-ppa/unstable'}]}}
      stage: neovim
    - env: ENV=vim74-trusty-python
      dist: trusty
      stage: vim74
    - env: ENV=vim74-xenial-python3
      dist: xenial
      stage: vim74
    - env: ENV=vim74-trusty-ruby
      dist: trusty
      addons: {apt: {packages: [vim-nox]}}
      stage: vim74
    - env: ENV=vim74-xenial-ruby
      dist: xenial
      addons: {apt: {packages: [vim-nox]}}
      stage: vim74
    - env: ENV=osx-highsierra
      os: osx
      osx_image: xcode9.4
      stage: vim8
install: |
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

  C_OPTS="--prefix=$DEPS --with-features=huge --disable-gui "
  case "$ENV" in
    vim-*)
      ;;
    neovim-*)
      mkdir -p ${DEPS}/bin
      ln -s /usr/bin/nvim ${DEPS}/bin/vim
      export VADER_OUTPUT_FILE=/dev/stderr
      return
      ;;
    vim74-* | vim80-*)
      mkdir -p ${DEPS}/bin
      ln -s /usr/bin/vim.nox ${DEPS}/bin/vim
      return
      ;;
    *)
      return
      ;;
  esac

  git clone --depth 1 https://github.com/vim/vim
  cd vim
  export PATH=/usr/bin:$PATH
  ./configure $C_OPTS
  make
  make install
  cd -
script: test/run !
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2017 Junegunn Choi

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

```vim
call plug#begin()

" List your plugins here
Plug 'tpope/vim-sensible'

call plug#end()
```

Reload the file or restart Vim, then you can,

* `:PlugInstall` to install the plugins
* `:PlugUpdate` to install or update the plugins
* `:PlugDiff` to review the changes from the last update
* `:PlugClean` to remove plugins no longer in the list

> [!NOTE]
> That's basically all you need to know to get started. The rest of the
> document is for advanced users who want to know more about the features and
> options.

> [!TIP]
> `plug#end()` automatically executes `filetype plugin indent on` and `syntax
> enable`. We believe this is a good default for most users, but if you don't
> want this behavior, you can revert the settings after the call.
>
> ```vim
> call plug#end()
> filetype indent off   " Disable file-type-specific indentation
> syntax off            " Disable syntax highlighting
> ```

### Getting Help

- See [tutorial] page to learn more about the basics of vim-plug
- See [tips] and [FAQ] pages for common problems and questions

[tutorial]: https://github.com/junegunn/vim-plug/wiki/tutorial
[tips]: https://github.com/junegunn/vim-plug/wiki/tips
[FAQ]: https://github.com/junegunn/vim-plug/wiki/faq

## Examples

The following examples demonstrate the additional features of vim-plug.

### Vim script example

```vim
call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes

" Shorthand notation for GitHub; translates to https://github.com/junegunn/seoul256.vim.git
Plug 'junegunn/seoul256.vim'

" Any valid git URL is allowed
Plug 'https://github.com/junegunn/vim-easy-align.git'

" Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
Plug 'fatih/vim-go', { 'tag': '*' }

" Using a non-default branch
Plug 'neoclide/coc.nvim', { 'branch': 'release' }

" Use 'dir' option to install plugin in a non-default directory
Plug 'junegunn/fzf', { 'dir': '~/.fzf' }

" Post-update hook: run a shell command after installing or updating the plugin
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

" Post-update hook can be a lambda expression
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }

" If the vim plugin is in a subdirectory, use 'rtp' option to specify its path
Plug 'nsf/gocode', { 'rtp': 'vim' }

" On-demand loading: loaded when the specified command is executed
Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }

" On-demand loading: loaded when a file with a specific file type is opened
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

" Unmanaged plugin (manually installed and updated)
Plug '~/my-prototype-plugin'

" Call plug#end to update &runtimepath and initialize the plugin system.
" - It automatically executes `filetype plugin indent on` and `syntax enable`
call plug#end()
" You can revert the settings after the call like so:
"   filetype indent off   " Disable file-type-specific indentation
"   syntax off            " Disable syntax highlighting

" Color schemes should be loaded after plug#end().
" We prepend it with 'silent!' to ignore errors when it's not yet installed.
silent! colorscheme seoul256
```

### Lua example for Neovim

In Neovim, you can write your configuration in a Lua script file named
`init.lua`. The following code is the Lua script equivalent to the Vim script
example above.

```lua
local vim = vim
local Plug = vim.fn['plug#']

vim.call('plug#begin')

-- Shorthand notation for GitHub; translates to https://github.com/junegunn/seoul256.vim.git
Plug('junegunn/seoul256.vim')

-- Any valid git URL is allowed
Plug('https://github.com/junegunn/vim-easy-align.git')

-- Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
Plug('fatih/vim-go', { ['tag'] = '*' })

-- Using a non-default branch
Plug('neoclide/coc.nvim', { ['branch'] = 'release' })

-- Use 'dir' option to install plugin in a non-default directory
Plug('junegunn/fzf', { ['dir'] = '~/.fzf' })

-- Post-update hook: run a shell command after installing or updating the plugin
Plug('junegunn/fzf', { ['dir'] = '~/.fzf', ['do'] = './install --all' })

-- Post-update hook can be a lambda expression
Plug('junegunn/fzf', { ['do'] = function()
  vim.fn['fzf#install']()
end })

-- If the vim plugin is in a subdirectory, use 'rtp' option to specify its path
Plug('nsf/gocode', { ['rtp'] = 'vim' })

-- On-demand loading: loaded when the specified command is executed
Plug('preservim/nerdtree', { ['on'] = 'NERDTreeToggle' })

-- On-demand loading: loaded when a file with a specific file type is opened
Plug('tpope/vim-fireplace', { ['for'] = 'clojure' })

-- Unmanaged plugin (manually installed and updated)
Plug('~/my-prototype-plugin')

vim.call('plug#end')

-- Color schemes should be loaded after plug#end().
-- We prepend it with 'silent!' to ignore errors when it's not yet installed.
vim.cmd('silent! colorscheme seoul256')
```

## Commands

| Command                             | Description                                                        |
| ----------------------------------- | ------------------------------------------------------------------ |
| `PlugInstall [name ...] [#threads]` | Install plugins                                                    |
| `PlugUpdate [name ...] [#threads]`  | Install or update plugins                                          |
| `PlugClean[!]`                      | Remove unlisted plugins (bang version will clean without prompt)   |
| `PlugUpgrade`                       | Upgrade vim-plug itself                                            |
| `PlugStatus`                        | Check the status of plugins                                        |
| `PlugDiff`                          | Examine changes from the previous update and the pending changes   |
| `PlugSnapshot[!] [output path]`     | Generate script for restoring the current snapshot of the plugins  |

## `Plug` options

| Option                  | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| `branch`/`tag`/`commit` | Branch/tag/commit of the repository to use                  |
| `rtp`                   | Subdirectory that contains Vim plugin                       |
| `dir`                   | Custom directory for the plugin                             |
| `as`                    | Use different name for the plugin                           |
| `do`                    | Post-update hook (string or funcref)                        |
| `on`                    | On-demand loading: Commands or `<Plug>`-mappings            |
| `for`                   | On-demand loading: File types                               |
| `frozen`                | Do not remove and do not update unless explicitly specified |

## Global options

| Flag                | Default                           | Description                                            |
| ------------------- | --------------------------------- | ------------------------------------------------------ |
| `g:plug_threads`    | 16                                | Default number of threads to use                       |
| `g:plug_timeout`    | 60                                | Time limit of each task in seconds (*Ruby & Python*)   |
| `g:plug_retries`    | 2                                 | Number of retries in case of timeout (*Ruby & Python*) |
| `g:plug_shallow`    | 1                                 | Use shallow clone                                      |
| `g:plug_window`     | `-tabnew`                         | Command to open plug window                            |
| `g:plug_pwindow`    | `vertical rightbelow new`         | Command to open preview window in `PlugDiff`           |
| `g:plug_url_format` | `https://git::@github.com/%s.git` | `printf` format to build repo URL (Only applies to the subsequent `Plug` commands) |


## Keybindings

- `D` - `PlugDiff`
- `S` - `PlugStatus`
- `R` - Retry failed update or installation tasks
- `U` - Update plugins in the selected range
- `q` - Abort the running tasks or close the window
- `:PlugStatus`
    - `L` - Load plugin
- `:PlugDiff`
    - `X` - Revert the update

## Post-update hooks

There are some plugins that require extra steps after installation or update.
In that case, use the `do` option to describe the task to be performed.

```vim
Plug 'Shougo/vimproc.vim', { 'do': 'make' }
Plug 'ycm-core/YouCompleteMe', { 'do': './install.py' }
```

If the value starts with `:`, it will be recognized as a Vim command.

```vim
Plug 'fatih/vim-go', { 'do': ':GoInstallBinaries' }
```

To call a Vim function, you can pass a lambda expression like so:

```vim
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
```

If you need more control, you can pass a reference to a Vim function that
takes a dictionary argument.

```vim
function! BuildYCM(info)
  " info is a dictionary with 3 fields
  " - name:   name of the plugin
  " - status: 'installed', 'updated', or 'unchanged'
  " - force:  set on PlugInstall! or PlugUpdate!
  if a:info.status == 'installed' || a:info.force
    !./install.py
  endif
endfunction

Plug 'ycm-core/YouCompleteMe', { 'do': function('BuildYCM') }
```

A post-update hook is executed inside the directory of the plugin and only run
when the repository has changed, but you can force it to run unconditionally
with the bang-versions of the commands: `PlugInstall!` and `PlugUpdate!`.

> [!TIP]
> Make sure to escape BARs and double-quotes when you write the `do` option
> inline as they are mistakenly recognized as command separator or the start of
> the trailing comment.
>
> ```vim
> Plug 'junegunn/fzf', { 'do': 'yes \| ./install' }
> ```
>
> But you can avoid the escaping if you extract the inline specification using a
> variable (or any Vim script expression) as follows:
>
> ```vim
> let g:fzf_install = 'yes | ./install'
> Plug 'junegunn/fzf', { 'do': g:fzf_install }
> ```

### `PlugInstall!` and `PlugUpdate!`

The installer takes the following steps when installing/updating a plugin:

1. `git clone` or `git fetch` from its origin
2. Check out branch, tag, or commit and optionally `git merge` remote branch
3. If the plugin was updated (or installed for the first time)
    1. Update submodules
    2. Execute post-update hooks

The commands with the `!` suffix ensure that all steps are run unconditionally.

## On-demand loading of plugins

```vim
" NERD tree will be loaded on the first invocation of NERDTreeToggle command
Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }

" Multiple commands
Plug 'junegunn/vim-github-dashboard', { 'on': ['GHDashboard', 'GHActivity'] }

" Loaded when clojure file is opened
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

" Multiple file types
Plug 'kovisoft/paredit', { 'for': ['clojure', 'scheme'] }

" On-demand loading on both conditions
Plug 'junegunn/vader.vim',  { 'on': 'Vader', 'for': 'vader' }

" Code to execute when the plugin is lazily loaded on demand
Plug 'junegunn/goyo.vim', { 'for': 'markdown' }
autocmd! User goyo.vim echom 'Goyo is now loaded!'
```

> [!NOTE]
> #### Should I set up on-demand loading?
>
> You probably don't need to.
>
> A properly implemented Vim plugin should already load lazily without any
> help from a plugin manager (`:help autoload`). So there are few cases where
> these options actually make much sense. Making a plugin load faster is
> the responsibility of the plugin developer, not the user. If you find
> a plugin that takes too long to load, consider opening an issue on the
> plugin's issue tracker.
>
> Let me give you a perspective. The time it takes to load a plugin is usually
> less than 2 or 3ms on modern computers. So unless you use a very large
> number of plugins, you are unlikely to save more than 50ms. If you have
> spent an hour carefully setting up the options to shave off 50ms, you
> will have to start Vim 72,000 times just to break even. You should ask
> yourself if that's a good investment of your time.
>
> Make sure that you're tackling the right problem by breaking down the
> startup time of Vim using `--startuptime`.
>
> ```sh
> vim --startuptime /tmp/log
> ```
>
> On-demand loading should only be used as a last resort. It is basically
> a hacky workaround and is not always guaranteed to work.

> [!TIP]
> You can pass an empty list to `on` or `for` option to disable the loading
> of the plugin. You can manually load the plugin using `plug#load(NAMES...)`
> function.
>
> See https://github.com/junegunn/vim-plug/wiki/tips#loading-plugins-manually


## Collaborators

- [Jan Edmund Lazo](https://github.com/janlazo) - Windows support
- [Jeremy Pallats](https://github.com/starcraftman) - Python installer

## License

MIT
```

## File: `plug.vim`
```
" vim-plug: Vim plugin manager
" ============================
"
" 1. Download plug.vim and put it in 'autoload' directory
"
"   # Vim
"   curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
"     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
"
"   # Neovim
"   sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
"     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
"
" 2. Add a vim-plug section to your ~/.vimrc (or ~/.config/nvim/init.vim for Neovim)
"
"   call plug#begin()
"
"   " List your plugins here
"   Plug 'tpope/vim-sensible'
"
"   call plug#end()
"
" 3. Reload the file or restart Vim, then you can,
"
"     :PlugInstall to install plugins
"     :PlugUpdate  to update plugins
"     :PlugDiff    to review the changes from the last update
"     :PlugClean   to remove plugins no longer in the list
"
" For more information, see https://github.com/junegunn/vim-plug
"
"
" Copyright (c) 2024 Junegunn Choi
"
" MIT License
"
" Permission is hereby granted, free of charge, to any person obtaining
" a copy of this software and associated documentation files (the
" "Software"), to deal in the Software without restriction, including
" without limitation the rights to use, copy, modify, merge, publish,
" distribute, sublicense, and/or sell copies of the Software, and to
" permit persons to whom the Software is furnished to do so, subject to
" the following conditions:
"
" The above copyright notice and this permission notice shall be
" included in all copies or substantial portions of the Software.
"
" THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
" EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
" MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
" NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
" LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
" OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
" WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

if exists('g:loaded_plug')
  finish
endif
let g:loaded_plug = 1

let s:cpo_save = &cpo
set cpo&vim

let s:plug_src = 'https://github.com/junegunn/vim-plug.git'
let s:plug_tab = get(s:, 'plug_tab', -1)
let s:plug_buf = get(s:, 'plug_buf', -1)
let s:mac_gui = has('gui_macvim') && has('gui_running')
let s:is_win = has('win32')
let s:nvim = has('nvim-0.2') || (has('nvim') && exists('*jobwait') && !s:is_win)
let s:vim8 = has('patch-8.0.0039') && exists('*job_start')
let s:shell_error = 0
if s:is_win && &shellslash
  set noshellslash
  let s:me = resolve(expand('<sfile>:p'))
  set shellslash
else
  let s:me = resolve(expand('<sfile>:p'))
endif
let s:base_spec = { 'branch': '', 'frozen': 0 }
let s:TYPE = {
\   'string':  type(''),
\   'list':    type([]),
\   'dict':    type({}),
\   'funcref': type(function('call'))
\ }
let s:loaded = get(s:, 'loaded', {})
let s:triggers = get(s:, 'triggers', {})

function! s:is_powershell(shell)
  return a:shell =~# 'powershell\(\.exe\)\?$' || a:shell =~# 'pwsh\(\.exe\)\?$'
endfunction

function! s:isabsolute(dir) abort
  return a:dir =~# '^/' || (has('win32') && a:dir =~? '^\%(\\\|[A-Z]:\)')
endfunction

function! s:git_dir(dir) abort
  let gitdir = s:trim(a:dir) . '/.git'
  if isdirectory(gitdir)
    return gitdir
  endif
  if !filereadable(gitdir)
    return ''
  endif
  let gitdir = matchstr(get(readfile(gitdir), 0, ''), '^gitdir: \zs.*')
  if len(gitdir) && !s:isabsolute(gitdir)
    let gitdir = a:dir . '/' . gitdir
  endif
  return isdirectory(gitdir) ? gitdir : ''
endfunction

function! s:git_origin_url(dir) abort
  let gitdir = s:git_dir(a:dir)
  let config = gitdir . '/config'
  if empty(gitdir) || !filereadable(config)
    return ''
  endif
  return matchstr(join(readfile(config)), '\[remote "origin"\].\{-}url\s*=\s*\zs\S*\ze')
endfunction

function! s:git_revision(dir) abort
  let gitdir = s:git_dir(a:dir)
  let head = gitdir . '/HEAD'
  if empty(gitdir) || !filereadable(head)
    return ''
  endif

  let line = get(readfile(head), 0, '')
  let ref = matchstr(line, '^ref: \zs.*')
  if empty(ref)
    return line
  endif

  if filereadable(gitdir . '/' . ref)
    return get(readfile(gitdir . '/' . ref), 0, '')
  endif

  if filereadable(gitdir . '/packed-refs')
    for line in readfile(gitdir . '/packed-refs')
      if line =~# ' ' . ref
        return matchstr(line, '^[0-9a-f]*')
      endif
    endfor
  endif

  return ''
endfunction

function! s:git_local_branch(dir) abort
  let gitdir = s:git_dir(a:dir)
  let head = gitdir . '/HEAD'
  if empty(gitdir) || !filereadable(head)
    return ''
  endif
  let branch = matchstr(get(readfile(head), 0, ''), '^ref: refs/heads/\zs.*')
  return len(branch) ? branch : 'HEAD'
endfunction

function! s:git_origin_branch(spec)
  if len(a:spec.branch)
    return a:spec.branch
  endif

  " The file may not be present if this is a local repository
  let gitdir = s:git_dir(a:spec.dir)
  let origin_head = gitdir.'/refs/remotes/origin/HEAD'
  if len(gitdir) && filereadable(origin_head)
    return matchstr(get(readfile(origin_head), 0, ''),
                  \ '^ref: refs/remotes/origin/\zs.*')
  endif

  " The command may not return the name of a branch in detached HEAD state
  let result = s:lines(s:system('git symbolic-ref --short HEAD', a:spec.dir))
  return s:shell_error ? '' : result[-1]
endfunction

if s:is_win
  function! s:plug_call(fn, ...)
    let shellslash = &shellslash
    try
      set noshellslash
      return call(a:fn, a:000)
    finally
      let &shellslash = shellslash
    endtry
  endfunction
else
  function! s:plug_call(fn, ...)
    return call(a:fn, a:000)
  endfunction
endif

function! s:plug_getcwd()
  return s:plug_call('getcwd')
endfunction

function! s:plug_fnamemodify(fname, mods)
  return s:plug_call('fnamemodify', a:fname, a:mods)
endfunction

function! s:plug_expand(fmt)
  return s:plug_call('expand', a:fmt, 1)
endfunction

function! s:plug_tempname()
  return s:plug_call('tempname')
endfunction

function! plug#begin(...)
  if a:0 > 0
    let home = s:path(s:plug_fnamemodify(s:plug_expand(a:1), ':p'))
  elseif exists('g:plug_home')
    let home = s:path(g:plug_home)
  elseif has('nvim')
    let home = stdpath('data') . '/plugged'
  elseif !empty(&rtp)
    let home = s:path(split(&rtp, ',')[0]) . '/plugged'
  else
    return s:err('Unable to determine plug home. Try calling plug#begin() with a path argument.')
  endif
  if s:plug_fnamemodify(home, ':t') ==# 'plugin' && s:plug_fnamemodify(home, ':h') ==# s:first_rtp
    return s:err('Invalid plug home. '.home.' is a standard Vim runtime path and is not allowed.')
  endif

  let g:plug_home = home
  let g:plugs = {}
  let g:plugs_order = []
  let s:triggers = {}

  call s:define_commands()
  return 1
endfunction

function! s:define_commands()
  command! -nargs=+ -bar Plug call plug#(<args>)
  if !executable('git')
    return s:err('`git` executable not found. Most commands will not be available. To suppress this message, prepend `silent!` to `call plug#begin(...)`.')
  endif
  if has('win32')
  \ && &shellslash
  \ && (&shell =~# 'cmd\(\.exe\)\?$' || s:is_powershell(&shell))
    return s:err('vim-plug does not support shell, ' . &shell . ', when shellslash is set.')
  endif
  if !has('nvim')
    \ && (has('win32') || has('win32unix'))
    \ && !has('multi_byte')
    return s:err('Vim needs +multi_byte feature on Windows to run shell commands. Enable +iconv for best results.')
  endif
  command! -nargs=* -bar -bang -complete=customlist,s:names PlugInstall call s:install(<bang>0, [<f-args>])
  command! -nargs=* -bar -bang -complete=customlist,s:names PlugUpdate  call s:update(<bang>0, [<f-args>])
  command! -nargs=0 -bar -bang PlugClean call s:clean(<bang>0)
  command! -nargs=0 -bar PlugUpgrade if s:upgrade() | execute 'source' s:esc(s:me) | endif
  command! -nargs=0 -bar PlugStatus  call s:status()
  command! -nargs=0 -bar PlugDiff    call s:diff()
  command! -nargs=? -bar -bang -complete=file PlugSnapshot call s:snapshot(<bang>0, <f-args>)
endfunction

function! s:to_a(v)
  return type(a:v) == s:TYPE.list ? a:v : [a:v]
endfunction

function! s:to_s(v)
  return type(a:v) == s:TYPE.string ? a:v : join(a:v, "\n") . "\n"
endfunction

function! s:glob(from, pattern)
  return s:lines(globpath(a:from, a:pattern))
endfunction

function! s:source(from, ...)
  let found = 0
  for pattern in a:000
    for vim in s:glob(a:from, pattern)
      execute 'source' s:esc(vim)
      let found = 1
    endfor
  endfor
  return found
endfunction

function! s:assoc(dict, key, val)
  let a:dict[a:key] = add(get(a:dict, a:key, []), a:val)
endfunction

function! s:ask(message, ...)
  call inputsave()
  echohl WarningMsg
  let answer = input(a:message.(a:0 ? ' (y/N/a) ' : ' (y/N) '))
  echohl None
  call inputrestore()
  echo "\r"
  return (a:0 && answer =~? '^a') ? 2 : (answer =~? '^y') ? 1 : 0
endfunction

function! s:ask_no_interrupt(...)
  try
    return call('s:ask', a:000)
  catch
    return 0
  endtry
endfunction

function! s:lazy(plug, opt)
  return has_key(a:plug, a:opt) &&
        \ (empty(s:to_a(a:plug[a:opt]))         ||
        \  !isdirectory(a:plug.dir)             ||
        \  len(s:glob(s:rtp(a:plug), 'plugin')) ||
        \  len(s:glob(s:rtp(a:plug), 'after/plugin')))
endfunction

function! plug#end()
  if !exists('g:plugs')
    return s:err('plug#end() called without calling plug#begin() first')
  endif

  if exists('#PlugLOD')
    augroup PlugLOD
      autocmd!
    augroup END
    augroup! PlugLOD
  endif
  let lod = { 'ft': {}, 'map': {}, 'cmd': {} }

  if get(g:, 'did_load_filetypes', 0)
    filetype off
  endif
  for name in g:plugs_order
    if !has_key(g:plugs, name)
      continue
    endif
    let plug = g:plugs[name]
    if get(s:loaded, name, 0) || !s:lazy(plug, 'on') && !s:lazy(plug, 'for')
      let s:loaded[name] = 1
      continue
    endif

    if has_key(plug, 'on')
      let s:triggers[name] = { 'map': [], 'cmd': [] }
      for cmd in s:to_a(plug.on)
        if cmd =~? '^<Plug>.\+'
          if empty(mapcheck(cmd)) && empty(mapcheck(cmd, 'i'))
            call s:assoc(lod.map, cmd, name)
          endif
          call add(s:triggers[name].map, cmd)
        elseif cmd =~# '^[A-Z]'
          let cmd = substitute(cmd, '!*$', '', '')
          if exists(':'.cmd) != 2
            call s:assoc(lod.cmd, cmd, name)
          endif
          call add(s:triggers[name].cmd, cmd)
        else
          call s:err('Invalid `on` option: '.cmd.
          \ '. Should start with an uppercase letter or `<Plug>`.')
        endif
      endfor
    endif

    if has_key(plug, 'for')
      let types = s:to_a(plug.for)
      if !empty(types)
        augroup filetypedetect
        call s:source(s:rtp(plug), 'ftdetect/**/*.vim', 'after/ftdetect/**/*.vim')
        if has('nvim-0.5.0')
          call s:source(s:rtp(plug), 'ftdetect/**/*.lua', 'after/ftdetect/**/*.lua')
        endif
        augroup END
      endif
      for type in types
        call s:assoc(lod.ft, type, name)
      endfor
    endif
  endfor

  for [cmd, names] in items(lod.cmd)
    execute printf(
    \ has('patch-7.4.1898')
    \ ? 'command! -nargs=* -range -bang -complete=file %s call s:lod_cmd(%s, "<bang>", <line1>, <line2>, <q-args>, <q-mods> ,%s)'
    \ : 'command! -nargs=* -range -bang -complete=file %s call s:lod_cmd(%s, "<bang>", <line1>, <line2>, <q-args>, %s)'
    \ , cmd, string(cmd), string(names))
  endfor

  for [map, names] in items(lod.map)
    for [mode, map_prefix, key_prefix] in
          \ [['i', '<C-\><C-O>', ''], ['n', '', ''], ['v', '', 'gv'], ['o', '', '']]
      execute printf(
      \ '%snoremap <silent> %s %s:<C-U>call <SID>lod_map(%s, %s, %s, "%s")<CR>',
      \ mode, map, map_prefix, string(map), string(names), mode != 'i', key_prefix)
    endfor
  endfor

  for [ft, names] in items(lod.ft)
    augroup PlugLOD
      execute printf('autocmd FileType %s call <SID>lod_ft(%s, %s)',
            \ ft, string(ft), string(names))
    augroup END
  endfor

  call s:reorg_rtp()
  filetype plugin indent on
  if has('vim_starting')
    if has('syntax') && !exists('g:syntax_on')
      syntax enable
    end
  else
    call s:reload_plugins()
  endif
endfunction

function! s:loaded_names()
  return filter(copy(g:plugs_order), 'get(s:loaded, v:val, 0)')
endfunction

function! s:load_plugin(spec)
  call s:source(s:rtp(a:spec), 'plugin/**/*.vim', 'after/plugin/**/*.vim')
  if has('nvim-0.5.0')
    call s:source(s:rtp(a:spec), 'plugin/**/*.lua', 'after/plugin/**/*.lua')
  endif
endfunction

function! s:reload_plugins()
  for name in s:loaded_names()
    call s:load_plugin(g:plugs[name])
  endfor
endfunction

function! s:trim(str)
  return substitute(a:str, '[\/]\+$', '', '')
endfunction

function! s:version_requirement(val, min)
  for idx in range(0, len(a:min) - 1)
    let v = get(a:val, idx, 0)
    if     v < a:min[idx] | return 0
    elseif v > a:min[idx] | return 1
    endif
  endfor
  return 1
endfunction

function! s:git_version_requirement(...)
  if !exists('s:git_version')
    let s:git_version = map(split(split(s:system(['git', '--version']))[2], '\.'), 'str2nr(v:val)')
  endif
  return s:version_requirement(s:git_version, a:000)
endfunction

function! s:progress_opt(base)
  return a:base && !s:is_win &&
        \ s:git_version_requirement(1, 7, 1) ? '--progress' : ''
endfunction

function! s:rtp(spec)
  return s:path(a:spec.dir . get(a:spec, 'rtp', ''))
endfunction

if s:is_win
  function! s:path(path)
    return s:trim(substitute(a:path, '/', '\', 'g'))
  endfunction

  function! s:dirpath(path)
    return s:path(a:path) . '\'
  endfunction

  function! s:is_local_plug(repo)
    return a:repo =~? '^[a-z]:\|^[%~]'
  endfunction

  " Copied from fzf
  function! s:wrap_cmds(cmds)
    let cmds = [
      \ '@echo off',
      \ 'setlocal enabledelayedexpansion']
    \ + (type(a:cmds) == type([]) ? a:cmds : [a:cmds])
    \ + ['endlocal']
    if has('iconv')
      if !exists('s:codepage')
        let s:codepage = libcallnr('kernel32.dll', 'GetACP', 0)
      endif
      return map(cmds, printf('iconv(v:val."\r", "%s", "cp%d")', &encoding, s:codepage))
    endif
    return map(cmds, 'v:val."\r"')
  endfunction

  function! s:batchfile(cmd)
    let batchfile = s:plug_tempname().'.bat'
    call writefile(s:wrap_cmds(a:cmd), batchfile)
    let cmd = plug#shellescape(batchfile, {'shell': &shell, 'script': 0})
    if s:is_powershell(&shell)
      let cmd = '& ' . cmd
    endif
    return [batchfile, cmd]
  endfunction
else
  function! s:path(path)
    return s:trim(a:path)
  endfunction

  function! s:dirpath(path)
    return substitute(a:path, '[/\\]*$', '/', '')
  endfunction

  function! s:is_local_plug(repo)
    return a:repo[0] =~ '[/$~]'
  endfunction
endif

function! s:err(msg)
  echohl ErrorMsg
  echom '[vim-plug] '.a:msg
  echohl None
endfunction

function! s:warn(cmd, msg)
  echohl WarningMsg
  execute a:cmd 'a:msg'
  echohl None
endfunction

function! s:esc(path)
  return escape(a:path, ' ')
endfunction

function! s:escrtp(path)
  return escape(a:path, ' ,')
endfunction

function! s:remove_rtp()
  for name in s:loaded_names()
    let rtp = s:rtp(g:plugs[name])
    execute 'set rtp-='.s:escrtp(rtp)
    let after = globpath(rtp, 'after')
    if isdirectory(after)
      execute 'set rtp-='.s:escrtp(after)
    endif
  endfor
endfunction

function! s:reorg_rtp()
  if !empty(s:first_rtp)
    execute 'set rtp-='.s:first_rtp
    execute 'set rtp-='.s:last_rtp
  endif

  " &rtp is modified from outside
  if exists('s:prtp') && s:prtp !=# &rtp
    call s:remove_rtp()
    unlet! s:middle
  endif

  let s:middle = get(s:, 'middle', &rtp)
  let rtps     = map(s:loaded_names(), 's:rtp(g:plugs[v:val])')
  let afters   = filter(map(copy(rtps), 'globpath(v:val, "after")'), '!empty(v:val)')
  let rtp      = join(map(rtps, 'escape(v:val, ",")'), ',')
                 \ . ','.s:middle.','
                 \ . join(map(afters, 'escape(v:val, ",")'), ',')
  let &rtp     = substitute(substitute(rtp, ',,*', ',', 'g'), '^,\|,$', '', 'g')
  let s:prtp   = &rtp

  if !empty(s:first_rtp)
    execute 'set rtp^='.s:first_rtp
    execute 'set rtp+='.s:last_rtp
  endif
endfunction

function! s:doautocmd(...)
  if exists('#'.join(a:000, '#'))
    execute 'doautocmd' ((v:version > 703 || has('patch442')) ? '<nomodeline>' : '') join(a:000)
  endif
endfunction

function! s:dobufread(names)
  for name in a:names
    let path = s:rtp(g:plugs[name])
    for dir in ['ftdetect', 'ftplugin', 'after/ftdetect', 'after/ftplugin']
      if len(finddir(dir, path))
        if exists('#BufRead')
          doautocmd BufRead
        endif
        return
      endif
    endfor
  endfor
endfunction

function! plug#load(...)
  if a:0 == 0
    return s:err('Argument missing: plugin name(s) required')
  endif
  if !exists('g:plugs')
    return s:err('plug#begin was not called')
  endif
  let names = a:0 == 1 && type(a:1) == s:TYPE.list ? a:1 : a:000
  let unknowns = filter(copy(names), '!has_key(g:plugs, v:val)')
  if !empty(unknowns)
    let s = len(unknowns) > 1 ? 's' : ''
    return s:err(printf('Unknown plugin%s: %s', s, join(unknowns, ', ')))
  end
  let unloaded = filter(copy(names), '!get(s:loaded, v:val, 0)')
  if !empty(unloaded)
    for name in unloaded
      call s:lod([name], ['ftdetect', 'after/ftdetect', 'plugin', 'after/plugin'])
    endfor
    call s:dobufread(unloaded)
    return 1
  end
  return 0
endfunction

function! s:remove_triggers(name)
  if !has_key(s:triggers, a:name)
    return
  endif
  for cmd in s:triggers[a:name].cmd
    execute 'silent! delc' cmd
  endfor
  for map in s:triggers[a:name].map
    execute 'silent! unmap' map
    execute 'silent! iunmap' map
  endfor
  call remove(s:triggers, a:name)
endfunction

function! s:lod(names, types, ...)
  for name in a:names
    call s:remove_triggers(name)
    let s:loaded[name] = 1
  endfor
  call s:reorg_rtp()

  for name in a:names
    let rtp = s:rtp(g:plugs[name])
    for dir in a:types
      call s:source(rtp, dir.'/**/*.vim')
      if has('nvim-0.5.0')  " see neovim#14686
        call s:source(rtp, dir.'/**/*.lua')
      endif
    endfor
    if a:0
      if !s:source(rtp, a:1) && !empty(s:glob(rtp, a:2))
        execute 'runtime' a:1
      endif
      call s:source(rtp, a:2)
    endif
    call s:doautocmd('User', name)
  endfor
endfunction

function! s:lod_ft(pat, names)
  let syn = 'syntax/'.a:pat.'.vim'
  call s:lod(a:names, ['plugin', 'after/plugin'], syn, 'after/'.syn)
  execute 'autocmd! PlugLOD FileType' a:pat
  call s:doautocmd('filetypeplugin', 'FileType')
  call s:doautocmd('filetypeindent', 'FileType')
endfunction

if has('patch-7.4.1898')
  function! s:lod_cmd(cmd, bang, l1, l2, args, mods, names)
    call s:lod(a:names, ['ftdetect', 'after/ftdetect', 'plugin', 'after/plugin'])
    call s:dobufread(a:names)
    execute printf('%s %s%s%s %s', a:mods, (a:l1 == a:l2 ? '' : (a:l1.','.a:l2)), a:cmd, a:bang, a:args)
  endfunction
else
  function! s:lod_cmd(cmd, bang, l1, l2, args, names)
    call s:lod(a:names, ['ftdetect', 'after/ftdetect', 'plugin', 'after/plugin'])
    call s:dobufread(a:names)
    execute printf('%s%s%s %s', (a:l1 == a:l2 ? '' : (a:l1.','.a:l2)), a:cmd, a:bang, a:args)
  endfunction
endif

function! s:lod_map(map, names, with_prefix, prefix)
  call s:lod(a:names, ['ftdetect', 'after/ftdetect', 'plugin', 'after/plugin'])
  call s:dobufread(a:names)
  let extra = ''
  while 1
    let c = getchar(0)
    if c == 0
      break
    endif
    let extra .= nr2char(c)
  endwhile

  if a:with_prefix
    let prefix = v:count ? v:count : ''
    let prefix .= '"'.v:register.a:prefix
    if mode(1) == 'no'
      if v:operator == 'c'
        let prefix = "\<esc>" . prefix
      endif
      let prefix .= v:operator
    endif
    call feedkeys(prefix, 'n')
  endif
  call feedkeys(substitute(a:map, '^<Plug>', "\<Plug>", '') . extra)
endfunction

function! plug#(repo, ...)
  if a:0 > 1
    return s:err('Invalid number of arguments (1..2)')
  endif

  try
    let repo = s:trim(a:repo)
    let opts = a:0 == 1 ? s:parse_options(a:1) : s:base_spec
    let name = get(opts, 'as', s:plug_fnamemodify(repo, ':t:s?\.git$??'))
    let spec = extend(s:infer_properties(name, repo), opts)
    if !has_key(g:plugs, name)
      call add(g:plugs_order, name)
    endif
    let g:plugs[name] = spec
    let s:loaded[name] = get(s:loaded, name, 0)
  catch
    return s:err(repo . ' ' . v:exception)
  endtry
endfunction

function! s:parse_options(arg)
  let opts = copy(s:base_spec)
  let type = type(a:arg)
  let opt_errfmt = 'Invalid argument for "%s" option of :Plug (expected: %s)'
  if type == s:TYPE.string
    if empty(a:arg)
      throw printf(opt_errfmt, 'tag', 'string')
    endif
    let opts.tag = a:arg
  elseif type == s:TYPE.dict
    for opt in ['branch', 'tag', 'commit', 'rtp', 'dir', 'as']
      if has_key(a:arg, opt)
      \ && (type(a:arg[opt]) != s:TYPE.string || empty(a:arg[opt]))
        throw printf(opt_errfmt, opt, 'string')
      endif
    endfor
    for opt in ['on', 'for']
      if has_key(a:arg, opt)
      \ && type(a:arg[opt]) != s:TYPE.list
      \ && (type(a:arg[opt]) != s:TYPE.string || empty(a:arg[opt]))
        throw printf(opt_errfmt, opt, 'string or list')
      endif
    endfor
    if has_key(a:arg, 'do')
      \ && type(a:arg.do) != s:TYPE.funcref
      \ && (type(a:arg.do) != s:TYPE.string || empty(a:arg.do))
        throw printf(opt_errfmt, 'do', 'string or funcref')
    endif
    call extend(opts, a:arg)
    if has_key(opts, 'dir')
      let opts.dir = s:dirpath(s:plug_expand(opts.dir))
    endif
  else
    throw 'Invalid argument type (expected: string or dictionary)'
  endif
  return opts
endfunction

function! s:infer_properties(name, repo)
  let repo = a:repo
  if s:is_local_plug(repo)
    return { 'dir': s:dirpath(s:plug_expand(repo)) }
  else
    if repo =~ ':'
      let uri = repo
    else
      if repo !~ '/'
        throw printf('Invalid argument: %s (implicit `vim-scripts'' expansion is deprecated)', repo)
      endif
      let fmt = get(g:, 'plug_url_format', 'https://git::@github.com/%s.git')
      let uri = printf(fmt, repo)
    endif
    return { 'dir': s:dirpath(g:plug_home.'/'.a:name), 'uri': uri }
  endif
endfunction

function! s:install(force, names)
  call s:update_impl(0, a:force, a:names)
endfunction

function! s:update(force, names)
  call s:update_impl(1, a:force, a:names)
endfunction

function! plug#helptags()
  if !exists('g:plugs')
    return s:err('plug#begin was not called')
  endif
  for spec in values(g:plugs)
    let docd = join([s:rtp(spec), 'doc'], '/')
    if isdirectory(docd)
      silent! execute 'helptags' s:esc(docd)
    endif
  endfor
  return 1
endfunction

function! s:syntax()
  syntax clear
  syntax region plug1 start=/\%1l/ end=/\%2l/ contains=plugNumber
  syntax region plug2 start=/\%2l/ end=/\%3l/ contains=plugBracket,plugX,plugAbort
  syn match plugNumber /[0-9]\+[0-9.]*/ contained
  syn match plugBracket /[[\]]/ contained
  syn match plugX /x/ contained
  syn match plugAbort /\~/ contained
  syn match plugDash /^-\{1}\ /
  syn match plugPlus /^+/
  syn match plugStar /^*/
  syn match plugMessage /\(^- \)\@<=.*/
  syn match plugName /\(^- \)\@<=[^ ]*:/
  syn match plugSha /\%(: \)\@<=[0-9a-f]\{4,}$/
  syn match plugTag /(tag: [^)]\+)/
  syn match plugInstall /\(^+ \)\@<=[^:]*/
  syn match plugUpdate /\(^* \)\@<=[^:]*/
  syn match plugCommit /^  \X*[0-9a-f]\{7,9} .*/ contains=plugRelDate,plugEdge,plugTag
  syn match plugEdge /^  \X\+$/
  syn match plugEdge /^  \X*/ contained nextgroup=plugSha
  syn match plugSha /[0-9a-f]\{7,9}/ contained
  syn match plugRelDate /([^)]*)$/ contained
  syn match plugNotLoaded /(not loaded)$/
  syn match plugError /^x.*/
  syn region plugDeleted start=/^\~ .*/ end=/^\ze\S/
  syn match plugH2 /^.*:\n-\+$/
  syn match plugH2 /^-\{2,}/
  syn keyword Function PlugInstall PlugStatus PlugUpdate PlugClean
  hi def link plug1       Title
  hi def link plug2       Repeat
  hi def link plugH2      Type
  hi def link plugX       Exception
  hi def link plugAbort   Ignore
  hi def link plugBracket Structure
  hi def link plugNumber  Number

  hi def link plugDash    Special
  hi def link plugPlus    Constant
  hi def link plugStar    Boolean

  hi def link plugMessage Function
  hi def link plugName    Label
  hi def link plugInstall Function
  hi def link plugUpdate  Type

  hi def link plugError   Error
  hi def link plugDeleted Ignore
  hi def link plugRelDate Comment
  hi def link plugEdge    PreProc
  hi def link plugSha     Identifier
  hi def link plugTag     Constant

  hi def link plugNotLoaded Comment
endfunction

function! s:lpad(str, len)
  return a:str . repeat(' ', a:len - len(a:str))
endfunction

function! s:lines(msg)
  return split(a:msg, "[\r\n]")
endfunction

function! s:lastline(msg)
  return get(s:lines(a:msg), -1, '')
endfunction

function! s:new_window()
  execute get(g:, 'plug_window', '-tabnew')
endfunction

function! s:plug_window_exists()
  let buflist = tabpagebuflist(s:plug_tab)
  return !empty(buflist) && index(buflist, s:plug_buf) >= 0
endfunction

function! s:switch_in()
  if !s:plug_window_exists()
    return 0
  endif

  if winbufnr(0) != s:plug_buf
    let s:pos = [tabpagenr(), winnr(), winsaveview()]
    execute 'normal!' s:plug_tab.'gt'
    let winnr = bufwinnr(s:plug_buf)
    execute winnr.'wincmd w'
    call add(s:pos, winsaveview())
  else
    let s:pos = [winsaveview()]
  endif

  setlocal modifiable
  return 1
endfunction

function! s:switch_out(...)
  call winrestview(s:pos[-1])
  setlocal nomodifiable
  if a:0 > 0
    execute a:1
  endif

  if len(s:pos) > 1
    execute 'normal!' s:pos[0].'gt'
    execute s:pos[1] 'wincmd w'
    call winrestview(s:pos[2])
  endif
endfunction

function! s:finish_bindings()
  nnoremap <silent> <buffer> R  :call <SID>retry()<cr>
  nnoremap <silent> <buffer> D  :PlugDiff<cr>
  nnoremap <silent> <buffer> S  :PlugStatus<cr>
  nnoremap <silent> <buffer> U  :call <SID>status_update()<cr>
  xnoremap <silent> <buffer> U  :call <SID>status_update()<cr>
  nnoremap <silent> <buffer> ]] :silent! call <SID>section('')<cr>
  nnoremap <silent> <buffer> [[ :silent! call <SID>section('b')<cr>
endfunction

function! s:prepare(...)
  if empty(s:plug_getcwd())
    throw 'Invalid current working directory. Cannot proceed.'
  endif

  for evar in ['$GIT_DIR', '$GIT_WORK_TREE']
    if exists(evar)
      throw evar.' detected. Cannot proceed.'
    endif
  endfor

  call s:job_abort(0)
  if s:switch_in()
    if b:plug_preview == 1
      pc
    endif
    enew
  else
    call s:new_window()
  endif

  nnoremap <silent> <buffer> q :call <SID>close_pane()<cr>
  if a:0 == 0
    call s:finish_bindings()
  endif
  let b:plug_preview = -1
  let s:plug_tab = tabpagenr()
  let s:plug_buf = winbufnr(0)
  call s:assign_name()

  for k in ['<cr>', 'L', 'o', 'X', 'd', 'dd']
    execute 'silent! unmap <buffer>' k
  endfor
  setlocal buftype=nofile bufhidden=wipe nobuflisted nolist noswapfile nowrap cursorline modifiable nospell
  if exists('+colorcolumn')
    setlocal colorcolumn=
  endif
  setf vim-plug
  if exists('g:syntax_on')
    call s:syntax()
  endif
endfunction

function! s:close_pane()
  if b:plug_preview == 1
    pc
    let b:plug_preview = -1
  elseif exists('s:jobs') && !empty(s:jobs)
    call s:job_abort(1)
  else
    bd
  endif
endfunction

function! s:assign_name()
  " Assign buffer name
  let prefix = '[Plugins]'
  let name   = prefix
  let idx    = 2
  while bufexists(name)
    let name = printf('%s (%s)', prefix, idx)
    let idx = idx + 1
  endwhile
  silent! execute 'f' fnameescape(name)
endfunction

function! s:chsh(swap)
  let prev = [&shell, &shellcmdflag, &shellredir]
  if !s:is_win
    set shell=sh
  endif
  if a:swap
    if s:is_powershell(&shell)
      let &shellredir = '2>&1 | Out-File -Encoding UTF8 %s'
    elseif &shell =~# 'sh' || &shell =~# 'cmd\(\.exe\)\?$'
      set shellredir=>%s\ 2>&1
    endif
  endif
  return prev
endfunction

function! s:bang(cmd, ...)
  let batchfile = ''
  try
    let [sh, shellcmdflag, shrd] = s:chsh(a:0)
    " FIXME: Escaping is incomplete. We could use shellescape with eval,
    "        but it won't work on Windows.
    let cmd = a:0 ? s:with_cd(a:cmd, a:1) : a:cmd
    if s:is_win
      let [batchfile, cmd] = s:batchfile(cmd)
    endif
    let g:_plug_bang = (s:is_win && has('gui_running') ? 'silent ' : '').'!'.escape(cmd, '#!%')
    execute "normal! :execute g:_plug_bang\<cr>\<cr>"
  finally
    unlet g:_plug_bang
    let [&shell, &shellcmdflag, &shellredir] = [sh, shellcmdflag, shrd]
    if s:is_win && filereadable(batchfile)
      call delete(batchfile)
    endif
  endtry
  return v:shell_error ? 'Exit status: ' . v:shell_error : ''
endfunction

function! s:regress_bar()
  let bar = substitute(getline(2)[1:-2], '.*\zs=', 'x', '')
  call s:progress_bar(2, bar, len(bar))
endfunction

function! s:is_updated(dir)
  return !empty(s:system_chomp(['git', 'log', '--pretty=format:%h', 'HEAD...HEAD@{1}'], a:dir))
endfunction

function! s:do(pull, force, todo)
  if has('nvim')
    " Reset &rtp to invalidate Neovim cache of loaded Lua modules
    " See https://github.com/junegunn/vim-plug/pull/1157#issuecomment-1809226110
    let &rtp = &rtp
  endif
  for [name, spec] in items(a:todo)
    if !isdirectory(spec.dir)
      continue
    endif
    let installed = has_key(s:update.new, name)
    let updated = installed ? 0 :
      \ (a:pull && index(s:update.errors, name) < 0 && s:is_updated(spec.dir))
    if a:force || installed || updated
      execute 'cd' s:esc(spec.dir)
      call append(3, '- Post-update hook for '. name .' ... ')
      let error = ''
      let type = type(spec.do)
      if type == s:TYPE.string
        if spec.do[0] == ':'
          if !get(s:loaded, name, 0)
            let s:loaded[name] = 1
            call s:reorg_rtp()
          endif
          call s:load_plugin(spec)
          try
            execute spec.do[1:]
          catch
            let error = v:exception
          endtry
          if !s:plug_window_exists()
            cd -
            throw 'Warning: vim-plug was terminated by the post-update hook of '.name
          endif
        else
          let error = s:bang(spec.do)
        endif
      elseif type == s:TYPE.funcref
        try
          call s:load_plugin(spec)
          let status = installed ? 'installed' : (updated ? 'updated' : 'unchanged')
          call spec.do({ 'name': name, 'status': status, 'force': a:force })
        catch
          let error = v:exception
        endtry
      else
        let error = 'Invalid hook type'
      endif
      call s:switch_in()
      call setline(4, empty(error) ? (getline(4) . 'OK')
                                 \ : ('x' . getline(4)[1:] . error))
      if !empty(error)
        call add(s:update.errors, name)
        call s:regress_bar()
      endif
      cd -
    endif
  endfor
endfunction

function! s:hash_match(a, b)
  return stridx(a:a, a:b) == 0 || stridx(a:b, a:a) == 0
endfunction

function! s:disable_credential_helper()
  return s:git_version_requirement(2) && get(g:, 'plug_disable_credential_helper', 1)
endfunction

function! s:checkout(spec)
  let sha = a:spec.commit
  let output = s:git_revision(a:spec.dir)
  let error = 0
  if !empty(output) && !s:hash_match(sha, s:lines(output)[0])
    let credential_helper = s:disable_credential_helper() ? '-c credential.helper= ' : ''
    let output = s:system(
          \ 'git '.credential_helper.'fetch --depth 999999 && git checkout '.plug#shellescape(sha).' --', a:spec.dir)
    let error = s:shell_error
  endif
  return [output, error]
endfunction

function! s:finish(pull)
  let new_frozen = len(filter(keys(s:update.new), 'g:plugs[v:val].frozen'))
  if new_frozen
    let s = new_frozen > 1 ? 's' : ''
    call append(3, printf('- Installed %d frozen plugin%s', new_frozen, s))
  endif
  call append(3, '- Finishing ... ') | 4
  redraw
  call plug#helptags()
  call plug#end()
  call setline(4, getline(4) . 'Done!')
  redraw
  let msgs = []
  if !empty(s:update.errors)
    call add(msgs, "Press 'R' to retry.")
  endif
  if a:pull && len(s:update.new) < len(filter(getline(5, '$'),
                \ "v:val =~ '^- ' && v:val !~# 'Already up.to.date'"))
    call add(msgs, "Press 'D' to see the updated changes.")
  endif
  echo join(msgs, ' ')
  call s:finish_bindings()
endfunction

function! s:retry()
  if empty(s:update.errors)
    return
  endif
  echo
  call s:update_impl(s:update.pull, s:update.force,
        \ extend(copy(s:update.errors), [s:update.threads]))
endfunction

function! s:is_managed(name)
  return has_key(g:plugs[a:name], 'uri')
endfunction

function! s:names(...)
  return sort(filter(keys(g:plugs), 'stridx(v:val, a:1) == 0 && s:is_managed(v:val)'))
endfunction

function! s:check_ruby()
  silent! ruby require 'thread'; VIM::command("let g:plug_ruby = '#{RUBY_VERSION}'")
  if !exists('g:plug_ruby')
    redraw!
    return s:warn('echom', 'Warning: Ruby interface is broken')
  endif
  let ruby_version = split(g:plug_ruby, '\.')
  unlet g:plug_ruby
  return s:version_requirement(ruby_version, [1, 8, 7])
endfunction

function! s:update_impl(pull, force, args) abort
  let sync = index(a:args, '--sync') >= 0 || has('vim_starting')
  let args = filter(copy(a:args), 'v:val != "--sync"')
  let threads = (len(args) > 0 && args[-1] =~ '^[1-9][0-9]*$') ?
                  \ remove(args, -1) : get(g:, 'plug_threads', 16)

  let managed = filter(deepcopy(g:plugs), 's:is_managed(v:key)')
  let todo = empty(args) ? filter(managed, '!v:val.frozen || !isdirectory(v:val.dir)') :
                         \ filter(managed, 'index(args, v:key) >= 0')

  if empty(todo)
    return s:warn('echo', 'No plugin to '. (a:pull ? 'update' : 'install'))
  endif

  if !s:is_win && s:git_version_requirement(2, 3)
    let s:git_terminal_prompt = exists('$GIT_TERMINAL_PROMPT') ? $GIT_TERMINAL_PROMPT : ''
    let $GIT_TERMINAL_PROMPT = 0
    for plug in values(todo)
      let plug.uri = substitute(plug.uri,
            \ '^https://git::@github\.com', 'https://github.com', '')
    endfor
  endif

  if !isdirectory(g:plug_home)
    try
      call mkdir(g:plug_home, 'p')
    catch
      return s:err(printf('Invalid plug directory: %s. '.
              \ 'Try to call plug#begin with a valid directory', g:plug_home))
    endtry
  endif

  if has('nvim') && !exists('*jobwait') && threads > 1
    call s:warn('echom', '[vim-plug] Update Neovim for parallel installer')
  endif

  let use_job = s:nvim || s:vim8
  let python = (has('python') || has('python3')) && !use_job
  let ruby = has('ruby') && !use_job && (v:version >= 703 || v:version == 702 && has('patch374')) && !(s:is_win && has('gui_running')) && threads > 1 && s:check_ruby()

  let s:update = {
    \ 'start':   reltime(),
    \ 'all':     todo,
    \ 'todo':    copy(todo),
    \ 'errors':  [],
    \ 'pull':    a:pull,
    \ 'force':   a:force,
    \ 'new':     {},
    \ 'threads': (python || ruby || use_job) ? min([len(todo), threads]) : 1,
    \ 'bar':     '',
    \ 'fin':     0
  \ }

  call s:prepare(1)
  call append(0, ['', ''])
  normal! 2G
  silent! redraw

  " Set remote name, overriding a possible user git config's clone.defaultRemoteName
  let s:clone_opt = ['--origin', 'origin']
  if get(g:, 'plug_shallow', 1)
    call extend(s:clone_opt, ['--depth', '1'])
    if s:git_version_requirement(1, 7, 10)
      call add(s:clone_opt, '--no-single-branch')
    endif
  endif

  if has('win32unix') || has('wsl')
    call extend(s:clone_opt, ['-c', 'core.eol=lf', '-c', 'core.autocrlf=input'])
  endif

  let s:submodule_opt = s:git_version_requirement(2, 8) ? ' --jobs='.threads : ''

  " Python version requirement (>= 2.7)
  if python && !has('python3') && !ruby && !use_job && s:update.threads > 1
    redir => pyv
    silent python import platform; print platform.python_version()
    redir END
    let python = s:version_requirement(
          \ map(split(split(pyv)[0], '\.'), 'str2nr(v:val)'), [2, 6])
  endif

  if (python || ruby) && s:update.threads > 1
    try
      let imd = &imd
      if s:mac_gui
        set noimd
      endif
      if ruby
        call s:update_ruby()
      else
        call s:update_python()
      endif
    catch
      let lines = getline(4, '$')
      let printed = {}
      silent! 4,$d _
      for line in lines
        let name = s:extract_name(line, '.', '')
        if empty(name) || !has_key(printed, name)
          call append('$', line)
          if !empty(name)
            let printed[name] = 1
            if line[0] == 'x' && index(s:update.errors, name) < 0
              call add(s:update.errors, name)
            end
          endif
        endif
      endfor
    finally
      let &imd = imd
      call s:update_finish()
    endtry
  else
    call s:update_vim()
    while use_job && sync
      sleep 100m
      if s:update.fin
        break
      endif
    endwhile
  endif
endfunction

function! s:log4(name, msg)
  call setline(4, printf('- %s (%s)', a:msg, a:name))
  redraw
endfunction

function! s:update_finish()
  if exists('s:git_terminal_prompt')
    let $GIT_TERMINAL_PROMPT = s:git_terminal_prompt
  endif
  if s:switch_in()
    call append(3, '- Updating ...') | 4
    for [name, spec] in items(filter(copy(s:update.all), 'index(s:update.errors, v:key) < 0 && (s:update.force || s:update.pull || has_key(s:update.new, v:key))'))
      let [pos, _] = s:logpos(name)
      if !pos
        continue
      endif
      let out = ''
      let error = 0
      if has_key(spec, 'commit')
        call s:log4(name, 'Checking out '.spec.commit)
        let [out, error] = s:checkout(spec)
      elseif has_key(spec, 'tag')
        let tag = spec.tag
        if tag =~ '\*'
          let tags = s:lines(s:system('git tag --list '.plug#shellescape(tag).' --sort -version:refname 2>&1', spec.dir))
          if !s:shell_error && !empty(tags)
            let tag = tags[0]
            call s:log4(name, printf('Latest tag for %s -> %s', spec.tag, tag))
            call append(3, '')
          endif
        endif
        call s:log4(name, 'Checking out '.tag)
        let out = s:system('git checkout -q '.plug#shellescape(tag).' -- 2>&1', spec.dir)
        let error = s:shell_error
      endif
      if !error && filereadable(spec.dir.'/.gitmodules') &&
            \ (s:update.force || has_key(s:update.new, name) || s:is_updated(spec.dir))
        call s:log4(name, 'Updating submodules. This may take a while.')
        let out .= s:bang('git submodule update --init --recursive'.s:submodule_opt.' 2>&1', spec.dir)
        let error = v:shell_error
      endif
      let msg = s:format_message(error ? 'x': '-', name, out)
      if error
        call add(s:update.errors, name)
        call s:regress_bar()
        silent execute pos 'd _'
        call append(4, msg) | 4
      elseif !empty(out)
        call setline(pos, msg[0])
      endif
      redraw
    endfor
    silent 4 d _
    try
      call s:do(s:update.pull, s:update.force, filter(copy(s:update.all), 'index(s:update.errors, v:key) < 0 && has_key(v:val, "do")'))
    catch
      call s:warn('echom', v:exception)
      call s:warn('echo', '')
      return
    endtry
    call s:finish(s:update.pull)
    call setline(1, 'Updated. Elapsed time: ' . split(reltimestr(reltime(s:update.start)))[0] . ' sec.')
    call s:switch_out('normal! gg')
  endif
endfunction

function! s:mark_aborted(name, message)
  let attrs = { 'running': 0, 'error': 1, 'abort': 1, 'lines': [a:message] }
  let s:jobs[a:name] = extend(get(s:jobs, a:name, {}), attrs)
endfunction

function! s:job_abort(cancel)
  if (!s:nvim && !s:vim8) || !exists('s:jobs')
    return
  endif

  for [name, j] in items(s:jobs)
    if s:nvim
      silent! call jobstop(j.jobid)
    elseif s:vim8
      silent! call job_stop(j.jobid)
    endif
    if j.new
      call s:rm_rf(g:plugs[name].dir)
    endif
    if a:cancel
      call s:mark_aborted(name, 'Aborted')
    endif
  endfor

  if a:cancel
    for todo in values(s:update.todo)
      let todo.abort = 1
    endfor
  else
    let s:jobs = {}
  endif
endfunction

function! s:last_non_empty_line(lines)
  let len = len(a:lines)
  for idx in range(len)
    let line = a:lines[len-idx-1]
    if !empty(line)
      return line
    endif
  endfor
  return ''
endfunction

function! s:bullet_for(job, ...)
  if a:job.running
    return a:job.new ? '+' : '*'
  endif
  if get(a:job, 'abort', 0)
    return '~'
  endif
  return a:job.error ? 'x' : get(a:000, 0, '-')
endfunction

function! s:job_out_cb(self, data) abort
  let self = a:self
  let data = remove(self.lines, -1) . a:data
  let lines = map(split(data, "\n", 1), 'split(v:val, "\r", 1)[-1]')
  call extend(self.lines, lines)
  " To reduce the number of buffer updates
  let self.tick = get(self, 'tick', -1) + 1
  if !self.running || self.tick % len(s:jobs) == 0
    let result = self.error ? join(self.lines, "\n") : s:last_non_empty_line(self.lines)
    if len(result)
      call s:log(s:bullet_for(self), self.name, result)
    endif
  endif
endfunction

function! s:job_exit_cb(self, data) abort
  let a:self.running = 0
  let a:self.error = a:data != 0
  call s:reap(a:self.name)
  call s:tick()
endfunction

function! s:job_cb(fn, job, ch, data)
  if !s:plug_window_exists() " plug window closed
    return s:job_abort(0)
  endif
  call call(a:fn, [a:job, a:data])
endfunction

function! s:nvim_cb(job_id, data, event) dict abort
  return (a:event == 'stdout' || a:event == 'stderr') ?
    \ s:job_cb('s:job_out_cb',  self, 0, join(a:data, "\n")) :
    \ s:job_cb('s:job_exit_cb', self, 0, a:data)
endfunction

function! s:spawn(name, spec, queue, opts)
  let job = { 'name': a:name, 'spec': a:spec, 'running': 1, 'error': 0, 'lines': [''],
            \ 'new': get(a:opts, 'new', 0), 'queue': copy(a:queue) }
  let Item = remove(job.queue, 0)
  let argv = type(Item) == s:TYPE.funcref ? call(Item, [a:spec]) : Item
  let s:jobs[a:name] = job

  if s:nvim
    if has_key(a:opts, 'dir')
      let job.cwd = a:opts.dir
    endif
    call extend(job, {
    \ 'on_stdout': function('s:nvim_cb'),
    \ 'on_stderr': function('s:nvim_cb'),
    \ 'on_exit':   function('s:nvim_cb'),
    \ })
    let jid = s:plug_call('jobstart', argv, job)
    if jid > 0
      let job.jobid = jid
    else
      let job.running = 0
      let job.error   = 1
      let job.lines   = [jid < 0 ? argv[0].' is not executable' :
            \ 'Invalid arguments (or job table is full)']
    endif
  elseif s:vim8
    let cmd = join(map(copy(argv), 'plug#shellescape(v:val, {"script": 0})'))
    if has_key(a:opts, 'dir')
      let cmd = s:with_cd(cmd, a:opts.dir, 0)
    endif
    let argv = s:is_win ? ['cmd', '/s', '/c', '"'.cmd.'"'] : ['sh', '-c', cmd]
    let jid = job_start(s:is_win ? join(argv, ' ') : argv, {
    \ 'out_cb':   function('s:job_cb', ['s:job_out_cb',  job]),
    \ 'err_cb':   function('s:job_cb', ['s:job_out_cb',  job]),
    \ 'exit_cb':  function('s:job_cb', ['s:job_exit_cb', job]),
    \ 'err_mode': 'raw',
    \ 'out_mode': 'raw'
    \})
    if job_status(jid) == 'run'
      let job.jobid = jid
    else
      let job.running = 0
      let job.error   = 1
      let job.lines   = ['Failed to start job']
    endif
  else
    let job.lines = s:lines(call('s:system', has_key(a:opts, 'dir') ? [argv, a:opts.dir] : [argv]))
    let job.error = s:shell_error != 0
    let job.running = 0
  endif
endfunction

function! s:reap(name)
  let job = remove(s:jobs, a:name)
  if job.error
    call add(s:update.errors, a:name)
  elseif get(job, 'new', 0)
    let s:update.new[a:name] = 1
  endif

  let more = len(get(job, 'queue', []))
  let result = job.error ? join(job.lines, "\n") : s:last_non_empty_line(job.lines)
  if len(result)
    call s:log(s:bullet_for(job), a:name, result)
  endif

  if !job.error && more
    let job.spec.queue = job.queue
    let s:update.todo[a:name] = job.spec
  else
    let s:update.bar .= s:bullet_for(job, '=')
    call s:bar()
  endif
endfunction

function! s:bar()
  if s:switch_in()
    let total = len(s:update.all)
    call setline(1, (s:update.pull ? 'Updating' : 'Installing').
          \ ' plugins ('.len(s:update.bar).'/'.total.')')
    call s:progress_bar(2, s:update.bar, total)
    call s:switch_out()
  endif
endfunction

function! s:logpos(name)
  let max = line('$')
  for i in range(4, max > 4 ? max : 4)
    if getline(i) =~# '^[-+x*] '.a:name.':'
      for j in range(i + 1, max > 5 ? max : 5)
        if getline(j) !~ '^ '
          return [i, j - 1]
        endif
      endfor
      return [i, i]
    endif
  endfor
  return [0, 0]
endfunction

function! s:log(bullet, name, lines)
  if s:switch_in()
    let [b, e] = s:logpos(a:name)
    if b > 0
      silent execute printf('%d,%d d _', b, e)
      if b > winheight('.')
        let b = 4
      endif
    else
      let b = 4
    endif
    " FIXME For some reason, nomodifiable is set after :d in vim8
    setlocal modifiable
    call append(b - 1, s:format_message(a:bullet, a:name, a:lines))
    call s:switch_out()
  endif
endfunction

function! s:update_vim()
  let s:jobs = {}

  call s:bar()
  call s:tick()
endfunction

function! s:checkout_command(spec)
  let a:spec.branch = s:git_origin_branch(a:spec)
  return ['git', 'checkout', '-q', a:spec.branch, '--']
endfunction

function! s:merge_command(spec)
  let a:spec.branch = s:git_origin_branch(a:spec)
  return ['git', 'merge', '--ff-only', 'origin/'.a:spec.branch]
endfunction

function! s:tick()
  let pull = s:update.pull
  let prog = s:progress_opt(s:nvim || s:vim8)
while 1 " Without TCO, Vim stack is bound to explode
  if empty(s:update.todo)
    if empty(s:jobs) && !s:update.fin
      call s:update_finish()
      let s:update.fin = 1
    endif
    return
  endif

  let name = keys(s:update.todo)[0]
  let spec = remove(s:update.todo, name)
  if get(spec, 'abort', 0)
    call s:mark_aborted(name, 'Skipped')
    call s:reap(name)
    continue
  endif

  let queue = get(spec, 'queue', [])
  let new = empty(globpath(spec.dir, '.git', 1))

  if empty(queue)
    call s:log(new ? '+' : '*', name, pull ? 'Updating ...' : 'Installing ...')
    redraw
  endif

  let has_tag = has_key(spec, 'tag')
  if len(queue)
    call s:spawn(name, spec, queue, { 'dir': spec.dir })
  elseif !new
    let [error, _] = s:git_validate(spec, 0)
    if empty(error)
      if pull
        let cmd = s:disable_credential_helper() ? ['git', '-c', 'credential.helper=', 'fetch'] : ['git', 'fetch']
        if has_tag && !empty(globpath(spec.dir, '.git/shallow'))
          call extend(cmd, ['--depth', '99999999'])
        endif
        if !empty(prog)
          call add(cmd, prog)
        endif
        let queue = [cmd, split('git remote set-head origin -a')]
        if !has_tag && !has_key(spec, 'commit')
          call extend(queue, [function('s:checkout_command'), function('s:merge_command')])
        endif
        call s:spawn(name, spec, queue, { 'dir': spec.dir })
      else
        let s:jobs[name] = { 'running': 0, 'lines': ['Already installed'], 'error': 0 }
      endif
    else
      let s:jobs[name] = { 'running': 0, 'lines': s:lines(error), 'error': 1 }
    endif
  else
    let cmd = ['git', 'clone']
    if !has_tag
      call extend(cmd, s:clone_opt)
    endif
    if !empty(prog)
      call add(cmd, prog)
    endif
    call s:spawn(name, spec, [extend(cmd, [spec.uri, s:trim(spec.dir)]), function('s:checkout_command'), function('s:merge_command')], { 'new': 1 })
  endif

  if !s:jobs[name].running
    call s:reap(name)
  endif
  if len(s:jobs) >= s:update.threads
    break
  endif
endwhile
endfunction

function! s:update_python()
let py_exe = has('python') ? 'python' : 'python3'
execute py_exe "<< EOF"
import datetime
import functools
import os
try:
  import queue
except ImportError:
  import Queue as queue
import random
import re
import shutil
import signal
import subprocess
import tempfile
import threading as thr
import time
import traceback
import vim

G_NVIM = vim.eval("has('nvim')") == '1'
G_PULL = vim.eval('s:update.pull') == '1'
G_RETRIES = int(vim.eval('get(g:, "plug_retries", 2)')) + 1
G_TIMEOUT = int(vim.eval('get(g:, "plug_timeout", 60)'))
G_CLONE_OPT = ' '.join(vim.eval('s:clone_opt'))
G_PROGRESS = vim.eval('s:progress_opt(1)')
G_LOG_PROB = 1.0 / int(vim.eval('s:update.threads'))
G_STOP = thr.Event()
G_IS_WIN = vim.eval('s:is_win') == '1'

class PlugError(Exception):
  def __init__(self, msg):
    self.msg = msg
class CmdTimedOut(PlugError):
  pass
class CmdFailed(PlugError):
  pass
class InvalidURI(PlugError):
  pass
class Action(object):
  INSTALL, UPDATE, ERROR, DONE = ['+', '*', 'x', '-']

class Buffer(object):
  def __init__(self, lock, num_plugs, is_pull):
    self.bar = ''
    self.event = 'Updating' if is_pull else 'Installing'
    self.lock = lock
    self.maxy = int(vim.eval('winheight(".")'))
    self.num_plugs = num_plugs

  def __where(self, name):
    """ Find first line with name in current buffer. Return line num. """
    found, lnum = False, 0
    matcher = re.compile('^[-+x*] {0}:'.format(name))
    for line in vim.current.buffer:
      if matcher.search(line) is not None:
        found = True
        break
      lnum += 1

    if not found:
      lnum = -1
    return lnum

  def header(self):
    curbuf = vim.current.buffer
    curbuf[0] = self.event + ' plugins ({0}/{1})'.format(len(self.bar), self.num_plugs)

    num_spaces = self.num_plugs - len(self.bar)
    curbuf[1] = '[{0}{1}]'.format(self.bar, num_spaces * ' ')

    with self.lock:
      vim.command('normal! 2G')
      vim.command('redraw')

  def write(self, action, name, lines):
    first, rest = lines[0], lines[1:]
    msg = ['{0} {1}{2}{3}'.format(action, name, ': ' if first else '', first)]
    msg.extend(['    ' + line for line in rest])

    try:
      if action == Action.ERROR:
        self.bar += 'x'
        vim.command("call add(s:update.errors, '{0}')".format(name))
      elif action == Action.DONE:
        self.bar += '='

      curbuf = vim.current.buffer
      lnum = self.__where(name)
      if lnum != -1: # Found matching line num
        del curbuf[lnum]
        if lnum > self.maxy and action in set([Action.INSTALL, Action.UPDATE]):
          lnum = 3
      else:
        lnum = 3
      curbuf.append(msg, lnum)

      self.header()
    except vim.error:
      pass

class Command(object):
  CD = 'cd /d' if G_IS_WIN else 'cd'

  def __init__(self, cmd, cmd_dir=None, timeout=60, cb=None, clean=None):
    self.cmd = cmd
    if cmd_dir:
      self.cmd = '{0} {1} && {2}'.format(Command.CD, cmd_dir, self.cmd)
    self.timeout = timeout
    self.callback = cb if cb else (lambda msg: None)
    self.clean = clean if clean else (lambda: None)
    self.proc = None

  @property
  def alive(self):
    """ Returns true only if command still running. """
    return self.proc and self.proc.poll() is None

  def execute(self, ntries=3):
    """ Execute the command with ntries if CmdTimedOut.
        Returns the output of the command if no Exception.
    """
    attempt, finished, limit = 0, False, self.timeout

    while not finished:
      try:
        attempt += 1
        result = self.try_command()
        finished = True
        return result
      except CmdTimedOut:
        if attempt != ntries:
          self.notify_retry()
          self.timeout += limit
        else:
          raise

  def notify_retry(self):
    """ Retry required for command, notify user. """
    for count in range(3, 0, -1):
      if G_STOP.is_set():
        raise KeyboardInterrupt
      msg = 'Timeout. Will retry in {0} second{1} ...'.format(
            count, 's' if count != 1 else '')
      self.callback([msg])
      time.sleep(1)
    self.callback(['Retrying ...'])

  def try_command(self):
    """ Execute a cmd & poll for callback. Returns list of output.
        Raises CmdFailed   -> return code for Popen isn't 0
        Raises CmdTimedOut -> command exceeded timeout without new output
    """
    first_line = True

    try:
      tfile = tempfile.NamedTemporaryFile(mode='w+b')
      preexec_fn = not G_IS_WIN and os.setsid or None
      self.proc = subprocess.Popen(self.cmd, stdout=tfile,
                                   stderr=subprocess.STDOUT,
                                   stdin=subprocess.PIPE, shell=True,
                                   preexec_fn=preexec_fn)
      thrd = thr.Thread(target=(lambda proc: proc.wait()), args=(self.proc,))
      thrd.start()

      thread_not_started = True
      while thread_not_started:
        try:
          thrd.join(0.1)
          thread_not_started = False
        except RuntimeError:
          pass

      while self.alive:
        if G_STOP.is_set():
          raise KeyboardInterrupt

        if first_line or random.random() < G_LOG_PROB:
          first_line = False
          line = '' if G_IS_WIN else nonblock_read(tfile.name)
          if line:
            self.callback([line])

        time_diff = time.time() - os.path.getmtime(tfile.name)
        if time_diff > self.timeout:
          raise CmdTimedOut(['Timeout!'])

        thrd.join(0.5)

      tfile.seek(0)
      result = [line.decode('utf-8', 'replace').rstrip() for line in tfile]

      if self.proc.returncode != 0:
        raise CmdFailed([''] + result)

      return result
    except:
      self.terminate()
      raise

  def terminate(self):
    """ Terminate process and cleanup. """
    if self.alive:
      if G_IS_WIN:
        os.kill(self.proc.pid, signal.SIGINT)
      else:
        os.killpg(self.proc.pid, signal.SIGTERM)
    self.clean()

class Plugin(object):
  def __init__(self, name, args, buf_q, lock):
    self.name = name
    self.args = args
    self.buf_q = buf_q
    self.lock = lock
    self.tag = args.get('tag', 0)

  def manage(self):
    try:
      if os.path.exists(self.args['dir']):
        self.update()
      else:
        self.install()
        with self.lock:
          thread_vim_command("let s:update.new['{0}'] = 1".format(self.name))
    except PlugError as exc:
      self.write(Action.ERROR, self.name, exc.msg)
    except KeyboardInterrupt:
      G_STOP.set()
      self.write(Action.ERROR, self.name, ['Interrupted!'])
    except:
      # Any exception except those above print stack trace
      msg = 'Trace:\n{0}'.format(traceback.format_exc().rstrip())
      self.write(Action.ERROR, self.name, msg.split('\n'))
      raise

  def install(self):
    target = self.args['dir']
    if target[-1] == '\\':
      target = target[0:-1]

    def clean(target):
      def _clean():
        try:
          shutil.rmtree(target)
        except OSError:
          pass
      return _clean

    self.write(Action.INSTALL, self.name, ['Installing ...'])
    callback = functools.partial(self.write, Action.INSTALL, self.name)
    cmd = 'git clone {0} {1} {2} {3} 2>&1'.format(
          '' if self.tag else G_CLONE_OPT, G_PROGRESS, self.args['uri'],
          esc(target))
    com = Command(cmd, None, G_TIMEOUT, callback, clean(target))
    result = com.execute(G_RETRIES)
    self.write(Action.DONE, self.name, result[-1:])

  def repo_uri(self):
    cmd = 'git rev-parse --abbrev-ref HEAD 2>&1 && git config -f .git/config remote.origin.url'
    command = Command(cmd, self.args['dir'], G_TIMEOUT,)
    result = command.execute(G_RETRIES)
    return result[-1]

  def update(self):
    actual_uri = self.repo_uri()
    expect_uri = self.args['uri']
    regex = re.compile(r'^(?:\w+://)?(?:[^@/]*@)?([^:/]*(?::[0-9]*)?)[:/](.*?)(?:\.git)?/?$')
    ma = regex.match(actual_uri)
    mb = regex.match(expect_uri)
    if ma is None or mb is None or ma.groups() != mb.groups():
      msg = ['',
             'Invalid URI: {0}'.format(actual_uri),
             'Expected     {0}'.format(expect_uri),
             'PlugClean required.']
      raise InvalidURI(msg)

    if G_PULL:
      self.write(Action.UPDATE, self.name, ['Updating ...'])
      callback = functools.partial(self.write, Action.UPDATE, self.name)
      fetch_opt = '--depth 99999999' if self.tag and os.path.isfile(os.path.join(self.args['dir'], '.git/shallow')) else ''
      cmd = 'git fetch {0} {1} 2>&1'.format(fetch_opt, G_PROGRESS)
      com = Command(cmd, self.args['dir'], G_TIMEOUT, callback)
      result = com.execute(G_RETRIES)
      self.write(Action.DONE, self.name, result[-1:])
    else:
      self.write(Action.DONE, self.name, ['Already installed'])

  def write(self, action, name, msg):
    self.buf_q.put((action, name, msg))

class PlugThread(thr.Thread):
  def __init__(self, tname, args):
    super(PlugThread, self).__init__()
    self.tname = tname
    self.args = args

  def run(self):
    thr.current_thread().name = self.tname
    buf_q, work_q, lock = self.args

    try:
      while not G_STOP.is_set():
        name, args = work_q.get_nowait()
        plug = Plugin(name, args, buf_q, lock)
        plug.manage()
        work_q.task_done()
    except queue.Empty:
      pass

class RefreshThread(thr.Thread):
  def __init__(self, lock):
    super(RefreshThread, self).__init__()
    self.lock = lock
    self.running = True

  def run(self):
    while self.running:
      with self.lock:
        thread_vim_command('noautocmd normal! a')
      time.sleep(0.33)

  def stop(self):
    self.running = False

if G_NVIM:
  def thread_vim_command(cmd):
    vim.session.threadsafe_call(lambda: vim.command(cmd))
else:
  def thread_vim_command(cmd):
    vim.command(cmd)

def esc(name):
  return '"' + name.replace('"', '\"') + '"'

def nonblock_read(fname):
  """ Read a file with nonblock flag. Return the last line. """
  fread = os.open(fname, os.O_RDONLY | os.O_NONBLOCK)
  buf = os.read(fread, 100000).decode('utf-8', 'replace')
  os.close(fread)

  line = buf.rstrip('\r\n')
  left = max(line.rfind('\r'), line.rfind('\n'))
  if left != -1:
    left += 1
    line = line[left:]

  return line

def main():
  thr.current_thread().name = 'main'
  nthreads = int(vim.eval('s:update.threads'))
  plugs = vim.eval('s:update.todo')
  mac_gui = vim.eval('s:mac_gui') == '1'

  lock = thr.Lock()
  buf = Buffer(lock, len(plugs), G_PULL)
  buf_q, work_q = queue.Queue(), queue.Queue()
  for work in plugs.items():
    work_q.put(work)

  start_cnt = thr.active_count()
  for num in range(nthreads):
    tname = 'PlugT-{0:02}'.format(num)
    thread = PlugThread(tname, (buf_q, work_q, lock))
    thread.start()
  if mac_gui:
    rthread = RefreshThread(lock)
    rthread.start()

  while not buf_q.empty() or thr.active_count() != start_cnt:
    try:
      action, name, msg = buf_q.get(True, 0.25)
      buf.write(action, name, ['OK'] if not msg else msg)
      buf_q.task_done()
    except queue.Empty:
      pass
    except KeyboardInterrupt:
      G_STOP.set()

  if mac_gui:
    rthread.stop()
    rthread.join()

main()
EOF
endfunction

function! s:update_ruby()
  ruby << EOF
  module PlugStream
    SEP = ["\r", "\n", nil]
    def get_line
      buffer = ''
      loop do
        char = readchar rescue return
        if SEP.include? char.chr
          buffer << $/
          break
        else
          buffer << char
        end
      end
      buffer
    end
  end unless defined?(PlugStream)

  def esc arg
    %["#{arg.gsub('"', '\"')}"]
  end

  def killall pid
    pids = [pid]
    if /mswin|mingw|bccwin/ =~ RUBY_PLATFORM
      pids.each { |pid| Process.kill 'INT', pid.to_i rescue nil }
    else
      unless `which pgrep 2> /dev/null`.empty?
        children = pids
        until children.empty?
          children = children.map { |pid|
            `pgrep -P #{pid}`.lines.map { |l| l.chomp }
          }.flatten
          pids += children
        end
      end
      pids.each { |pid| Process.kill 'TERM', pid.to_i rescue nil }
    end
  end

  def compare_git_uri a, b
    regex = %r{^(?:\w+://)?(?:[^@/]*@)?([^:/]*(?::[0-9]*)?)[:/](.*?)(?:\.git)?/?$}
    regex.match(a).to_a.drop(1) == regex.match(b).to_a.drop(1)
  end

  require 'thread'
  require 'fileutils'
  require 'timeout'
  running = true
  iswin = VIM::evaluate('s:is_win').to_i == 1
  pull  = VIM::evaluate('s:update.pull').to_i == 1
  base  = VIM::evaluate('g:plug_home')
  all   = VIM::evaluate('s:update.todo')
  limit = VIM::evaluate('get(g:, "plug_timeout", 60)')
  tries = VIM::evaluate('get(g:, "plug_retries", 2)') + 1
  nthr  = VIM::evaluate('s:update.threads').to_i
  maxy  = VIM::evaluate('winheight(".")').to_i
  vim7  = VIM::evaluate('v:version').to_i <= 703 && RUBY_PLATFORM =~ /darwin/
  cd    = iswin ? 'cd /d' : 'cd'
  tot   = VIM::evaluate('len(s:update.todo)') || 0
  bar   = ''
  skip  = 'Already installed'
  mtx   = Mutex.new
  take1 = proc { mtx.synchronize { running && all.shift } }
  logh  = proc {
    cnt = bar.length
    $curbuf[1] = "#{pull ? 'Updating' : 'Installing'} plugins (#{cnt}/#{tot})"
    $curbuf[2] = '[' + bar.ljust(tot) + ']'
    VIM::command('normal! 2G')
    VIM::command('redraw')
  }
  where = proc { |name| (1..($curbuf.length)).find { |l| $curbuf[l] =~ /^[-+x*] #{name}:/ } }
  log   = proc { |name, result, type|
    mtx.synchronize do
      ing  = ![true, false].include?(type)
      bar += type ? '=' : 'x' unless ing
      b = case type
          when :install  then '+' when :update then '*'
          when true, nil then '-' else
            VIM::command("call add(s:update.errors, '#{name}')")
            'x'
          end
      result =
        if type || type.nil?
          ["#{b} #{name}: #{result.lines.to_a.last || 'OK'}"]
        elsif result =~ /^Interrupted|^Timeout/
          ["#{b} #{name}: #{result}"]
        else
          ["#{b} #{name}"] + result.lines.map { |l| "    " << l }
        end
      if lnum = where.call(name)
        $curbuf.delete lnum
        lnum = 4 if ing && lnum > maxy
      end
      result.each_with_index do |line, offset|
        $curbuf.append((lnum || 4) - 1 + offset, line.gsub(/\e\[./, '').chomp)
      end
      logh.call
    end
  }
  bt = proc { |cmd, name, type, cleanup|
    tried = timeout = 0
    begin
      tried += 1
      timeout += limit
      fd = nil
      data = ''
      if iswin
        Timeout::timeout(timeout) do
          tmp = VIM::evaluate('tempname()')
          system("(#{cmd}) > #{tmp}")
          data = File.read(tmp).chomp
          File.unlink tmp rescue nil
        end
      else
        fd = IO.popen(cmd).extend(PlugStream)
        first_line = true
        log_prob = 1.0 / nthr
        while line = Timeout::timeout(timeout) { fd.get_line }
          data << line
          log.call name, line.chomp, type if name && (first_line || rand < log_prob)
          first_line = false
        end
        fd.close
      end
      [$? == 0, data.chomp]
    rescue Timeout::Error, Interrupt => e
      if fd && !fd.closed?
        killall fd.pid
        fd.close
      end
      cleanup.call if cleanup
      if e.is_a?(Timeout::Error) && tried < tries
        3.downto(1) do |countdown|
          s = countdown > 1 ? 's' : ''
          log.call name, "Timeout. Will retry in #{countdown} second#{s} ...", type
          sleep 1
        end
        log.call name, 'Retrying ...', type
        retry
      end
      [false, e.is_a?(Interrupt) ? "Interrupted!" : "Timeout!"]
    end
  }
  main = Thread.current
  threads = []
  watcher = Thread.new {
    if vim7
      while VIM::evaluate('getchar(1)')
        sleep 0.1
      end
    else
      require 'io/console' # >= Ruby 1.9
      nil until IO.console.getch == 3.chr
    end
    mtx.synchronize do
      running = false
      threads.each { |t| t.raise Interrupt } unless vim7
    end
    threads.each { |t| t.join rescue nil }
    main.kill
  }
  refresh = Thread.new {
    while true
      mtx.synchronize do
        break unless running
        VIM::command('noautocmd normal! a')
      end
      sleep 0.2
    end
  } if VIM::evaluate('s:mac_gui') == 1

  clone_opt = VIM::evaluate('s:clone_opt').join(' ')
  progress = VIM::evaluate('s:progress_opt(1)')
  nthr.times do
    mtx.synchronize do
      threads << Thread.new {
        while pair = take1.call
          name = pair.first
          dir, uri, tag = pair.last.values_at *%w[dir uri tag]
          exists = File.directory? dir
          ok, result =
            if exists
              chdir = "#{cd} #{iswin ? dir : esc(dir)}"
              ret, data = bt.call "#{chdir} && git rev-parse --abbrev-ref HEAD 2>&1 && git config -f .git/config remote.origin.url", nil, nil, nil
              current_uri = data.lines.to_a.last
              if !ret
                if data =~ /^Interrupted|^Timeout/
                  [false, data]
                else
                  [false, [data.chomp, "PlugClean required."].join($/)]
                end
              elsif !compare_git_uri(current_uri, uri)
                [false, ["Invalid URI: #{current_uri}",
                         "Expected:    #{uri}",
                         "PlugClean required."].join($/)]
              else
                if pull
                  log.call name, 'Updating ...', :update
                  fetch_opt = (tag && File.exist?(File.join(dir, '.git/shallow'))) ? '--depth 99999999' : ''
                  bt.call "#{chdir} && git fetch #{fetch_opt} #{progress} 2>&1", name, :update, nil
                else
                  [true, skip]
                end
              end
            else
              d = esc dir.sub(%r{[\\/]+$}, '')
              log.call name, 'Installing ...', :install
              bt.call "git clone #{clone_opt unless tag} #{progress} #{uri} #{d} 2>&1", name, :install, proc {
                FileUtils.rm_rf dir
              }
            end
          mtx.synchronize { VIM::command("let s:update.new['#{name}'] = 1") } if !exists && ok
          log.call name, result, ok
        end
      } if running
    end
  end
  threads.each { |t| t.join rescue nil }
  logh.call
  refresh.kill if refresh
  watcher.kill
EOF
endfunction

function! s:shellesc_cmd(arg, script)
  let escaped = substitute('"'.a:arg.'"', '[&|<>()@^!"]', '^&', 'g')
  return substitute(escaped, '%', (a:script ? '%' : '^') . '&', 'g')
endfunction

function! s:shellesc_ps1(arg)
  return "'".substitute(escape(a:arg, '\"'), "'", "''", 'g')."'"
endfunction

function! s:shellesc_sh(arg)
  return "'".substitute(a:arg, "'", "'\\\\''", 'g')."'"
endfunction

" Escape the shell argument based on the shell.
" Vim and Neovim's shellescape() are insufficient.
" 1. shellslash determines whether to use single/double quotes.
"    Double-quote escaping is fragile for cmd.exe.
" 2. It does not work for powershell.
" 3. It does not work for *sh shells if the command is executed
"    via cmd.exe (ie. cmd.exe /c sh -c command command_args)
" 4. It does not support batchfile syntax.
"
" Accepts an optional dictionary with the following keys:
" - shell: same as Vim/Neovim 'shell' option.
"          If unset, fallback to 'cmd.exe' on Windows or 'sh'.
" - script: If truthy and shell is cmd.exe, escape for batchfile syntax.
function! plug#shellescape(arg, ...)
  if a:arg =~# '^[A-Za-z0-9_/:.-]\+$'
    return a:arg
  endif
  let opts = a:0 > 0 && type(a:1) == s:TYPE.dict ? a:1 : {}
  let shell = get(opts, 'shell', s:is_win ? 'cmd.exe' : 'sh')
  let script = get(opts, 'script', 1)
  if shell =~# 'cmd\(\.exe\)\?$'
    return s:shellesc_cmd(a:arg, script)
  elseif s:is_powershell(shell)
    return s:shellesc_ps1(a:arg)
  endif
  return s:shellesc_sh(a:arg)
endfunction

function! s:glob_dir(path)
  return map(filter(s:glob(a:path, '**'), 'isdirectory(v:val)'), 's:dirpath(v:val)')
endfunction

function! s:progress_bar(line, bar, total)
  call setline(a:line, '[' . s:lpad(a:bar, a:total) . ']')
endfunction

function! s:compare_git_uri(a, b)
  " See `git help clone'
  " https:// [user@] github.com[:port] / junegunn/vim-plug [.git]
  "          [git@]  github.com[:port] : junegunn/vim-plug [.git]
  " file://                            / junegunn/vim-plug        [/]
  "                                    / junegunn/vim-plug        [/]
  let pat = '^\%(\w\+://\)\='.'\%([^@/]*@\)\='.'\([^:/]*\%(:[0-9]*\)\=\)'.'[:/]'.'\(.\{-}\)'.'\%(\.git\)\=/\?$'
  let ma = matchlist(a:a, pat)
  let mb = matchlist(a:b, pat)
  return ma[1:2] ==# mb[1:2]
endfunction

function! s:format_message(bullet, name, message)
  if a:bullet != 'x'
    return [printf('%s %s: %s', a:bullet, a:name, s:lastline(a:message))]
  else
    let lines = map(s:lines(a:message), '"    ".v:val')
    return extend([printf('x %s:', a:name)], lines)
  endif
endfunction

function! s:with_cd(cmd, dir, ...)
  let script = a:0 > 0 ? a:1 : 1
  let pwsh = s:is_powershell(&shell)
  let cd = s:is_win && !pwsh ? 'cd /d' : 'cd'
  let sep = pwsh ? ';' : '&&'
  return printf('%s %s %s %s', cd, plug#shellescape(a:dir, {'script': script, 'shell': &shell}), sep, a:cmd)
endfunction

function! s:system_job(cmd) abort
  let tmp = tempname()
  let job = job_start(['/bin/sh', '-c', a:cmd], {
  \ 'out_io': 'file',
  \ 'out_name': tmp,
  \ 'err_io': 'out',
  \})
  while job_status(job) ==# 'run'
    sleep 1m
  endwhile
  let s:shell_error = job_info(job).exitval
  let result = filereadable(tmp) ? join(readfile(tmp, 'b'), "\n") : ''
  silent! call delete(tmp)
  return result
endfunction

function! s:system(cmd, ...)
  let batchfile = ''
  try
    let [sh, shellcmdflag, shrd] = s:chsh(1)
    if type(a:cmd) == s:TYPE.list
      " Neovim's system() supports list argument to bypass the shell
      " but it cannot set the working directory for the command.
      " Assume that the command does not rely on the shell.
      if has('nvim') && a:0 == 0
        let ret = system(a:cmd)
        let s:shell_error = v:shell_error
        return ret
      endif
      let cmd = join(map(copy(a:cmd), 'plug#shellescape(v:val, {"shell": &shell, "script": 0})'))
      if s:is_powershell(&shell)
        let cmd = '& ' . cmd
      endif
    else
      let cmd = a:cmd
    endif
    if a:0 > 0
      let cmd = s:with_cd(cmd, a:1, type(a:cmd) != s:TYPE.list)
    endif
    if s:is_win && type(a:cmd) != s:TYPE.list
      let [batchfile, cmd] = s:batchfile(cmd)
    endif
    if s:vim8 && has('gui_running') && !s:is_win
      return s:system_job(cmd)
    endif
    let ret = system(cmd)
    let s:shell_error = v:shell_error
    return ret
  finally
    let [&shell, &shellcmdflag, &shellredir] = [sh, shellcmdflag, shrd]
    if s:is_win && filereadable(batchfile)
      call delete(batchfile)
    endif
  endtry
endfunction

function! s:system_chomp(...)
  let ret = call('s:system', a:000)
  return s:shell_error ? '' : substitute(ret, '\n$', '', '')
endfunction

function! s:git_validate(spec, check_branch)
  let err = ''
  if isdirectory(a:spec.dir)
    let result = [s:git_local_branch(a:spec.dir), s:git_origin_url(a:spec.dir)]
    let remote = result[-1]
    if empty(remote)
      let err = join([remote, 'PlugClean required.'], "\n")
    elseif !s:compare_git_uri(remote, a:spec.uri)
      let err = join(['Invalid URI: '.remote,
                    \ 'Expected:    '.a:spec.uri,
                    \ 'PlugClean required.'], "\n")
    elseif !a:check_branch
      return ['', 0]
    elseif has_key(a:spec, 'commit')
      let sha = s:git_revision(a:spec.dir)
      if empty(sha)
        let err = join(add(result, 'PlugClean required.'), "\n")
      elseif !s:hash_match(sha, a:spec.commit)
        let err = join([printf('Invalid HEAD (expected: %s, actual: %s)',
                              \ a:spec.commit[:6], sha[:6]),
                      \ 'PlugUpdate required.'], "\n")
      endif
    elseif has_key(a:spec, 'tag')
      let tag = s:system_chomp('git describe --exact-match --tags HEAD 2>&1', a:spec.dir)
      if a:spec.tag !=# tag && a:spec.tag !~ '\*'
        let err = printf('Invalid tag: %s (expected: %s). Try PlugUpdate.',
              \ (empty(tag) ? 'N/A' : tag), a:spec.tag)
      endif
    elseif a:check_branch
      let current_branch = result[0]
      let origin_branch = s:git_origin_branch(a:spec)
      if origin_branch !=# current_branch
        let err = printf('Invalid branch: %s (expected: %s). Try PlugUpdate.',
              \ current_branch, origin_branch)
      endif
      if empty(err)
        let ahead_behind = split(s:lastline(s:system([
          \ 'git', 'rev-list', '--count', '--left-right',
          \ printf('HEAD...origin/%s', origin_branch)
          \ ], a:spec.dir)), '\t')
        if s:shell_error || len(ahead_behind) != 2
          let err = "Failed to compare with the origin. The default branch might have changed.\nPlugClean required."
        else
          let [ahead, behind] = ahead_behind
          if ahead && behind
            " Only mention PlugClean if diverged, otherwise it's likely to be
            " pushable (and probably not that messed up).
            let err = printf(
                  \ "Diverged from origin/%s (%d commit(s) ahead and %d commit(s) behind!\n"
                  \ .'Backup local changes and run PlugClean and PlugUpdate to reinstall it.', origin_branch, ahead, behind)
          elseif ahead
            let err = printf("Ahead of origin/%s by %d commit(s).\n"
                  \ .'Cannot update until local changes are pushed.',
                  \ origin_branch, ahead)
          endif
        endif
      endif
    endif
  else
    let err = 'Not found'
  endif
  return [err, err =~# 'PlugClean']
endfunction

function! s:rm_rf(dir)
  if isdirectory(a:dir)
    return s:system(s:is_win
    \ ? 'rmdir /S /Q '.plug#shellescape(a:dir)
    \ : ['rm', '-rf', a:dir])
  endif
endfunction

function! s:clean(force)
  call s:prepare()
  call append(0, 'Searching for invalid plugins in '.g:plug_home)
  call append(1, '')

  " List of valid directories
  let dirs = []
  let errs = {}
  let [cnt, total] = [0, len(g:plugs)]
  for [name, spec] in items(g:plugs)
    if !s:is_managed(name) || get(spec, 'frozen', 0)
      call add(dirs, spec.dir)
    else
      let [err, clean] = s:git_validate(spec, 1)
      if clean
        let errs[spec.dir] = s:lines(err)[0]
      else
        call add(dirs, spec.dir)
      endif
    endif
    let cnt += 1
    call s:progress_bar(2, repeat('=', cnt), total)
    normal! 2G
    redraw
  endfor

  let allowed = {}
  for dir in dirs
    let allowed[s:dirpath(s:plug_fnamemodify(dir, ':h:h'))] = 1
    let allowed[dir] = 1
    for child in s:glob_dir(dir)
      let allowed[child] = 1
    endfor
  endfor

  let todo = []
  let found = sort(s:glob_dir(g:plug_home))
  while !empty(found)
    let f = remove(found, 0)
    if !has_key(allowed, f) && isdirectory(f)
      call add(todo, f)
      call append(line('$'), '- ' . f)
      if has_key(errs, f)
        call append(line('$'), '    ' . errs[f])
      endif
      let found = filter(found, 'stridx(v:val, f) != 0')
    end
  endwhile

  4
  redraw
  if empty(todo)
    call append(line('$'), 'Already clean.')
  else
    let s:clean_count = 0
    call append(3, ['Directories to delete:', ''])
    redraw!
    if a:force || s:ask_no_interrupt('Delete all directories?')
      call s:delete([6, line('$')], 1)
    else
      call setline(4, 'Cancelled.')
      nnoremap <silent> <buffer> d :set opfunc=<sid>delete_op<cr>g@
      nmap     <silent> <buffer> dd d_
      xnoremap <silent> <buffer> d :<c-u>call <sid>delete_op(visualmode(), 1)<cr>
      echo 'Delete the lines (d{motion}) to delete the corresponding directories'
    endif
  endif
  4
  setlocal nomodifiable
endfunction

function! s:delete_op(type, ...)
  call s:delete(a:0 ? [line("'<"), line("'>")] : [line("'["), line("']")], 0)
endfunction

function! s:delete(range, force)
  let [l1, l2] = a:range
  let force = a:force
  let err_count = 0
  while l1 <= l2
    let line = getline(l1)
    if line =~ '^- ' && isdirectory(line[2:])
      execute l1
      redraw!
      let answer = force ? 1 : s:ask('Delete '.line[2:].'?', 1)
      let force = force || answer > 1
      if answer
        let err = s:rm_rf(line[2:])
        setlocal modifiable
        if empty(err)
          call setline(l1, '~'.line[1:])
          let s:clean_count += 1
        else
          delete _
          call append(l1 - 1, s:format_message('x', line[1:], err))
          let l2 += len(s:lines(err))
          let err_count += 1
        endif
        let msg = printf('Removed %d directories.', s:clean_count)
        if err_count > 0
          let msg .= printf(' Failed to remove %d directories.', err_count)
        endif
        call setline(4, msg)
        setlocal nomodifiable
      endif
    endif
    let l1 += 1
  endwhile
endfunction

function! s:upgrade()
  echo 'Downloading the latest version of vim-plug'
  redraw
  let tmp = s:plug_tempname()
  let new = tmp . '/plug.vim'

  try
    let out = s:system(['git', 'clone', '--depth', '1', s:plug_src, tmp])
    if s:shell_error
      return s:err('Error upgrading vim-plug: '. out)
    endif

    if readfile(s:me) ==# readfile(new)
      echo 'vim-plug is already up-to-date'
      return 0
    else
      call rename(s:me, s:me . '.old')
      call rename(new, s:me)
      unlet g:loaded_plug
      echo 'vim-plug has been upgraded'
      return 1
    endif
  finally
    silent! call s:rm_rf(tmp)
  endtry
endfunction

function! s:upgrade_specs()
  for spec in values(g:plugs)
    let spec.frozen = get(spec, 'frozen', 0)
  endfor
endfunction

function! s:status()
  call s:prepare()
  call append(0, 'Checking plugins')
  call append(1, '')

  let ecnt = 0
  let unloaded = 0
  let [cnt, total] = [0, len(g:plugs)]
  for [name, spec] in items(g:plugs)
    let is_dir = isdirectory(spec.dir)
    if has_key(spec, 'uri')
      if is_dir
        let [err, _] = s:git_validate(spec, 1)
        let [valid, msg] = [empty(err), empty(err) ? 'OK' : err]
      else
        let [valid, msg] = [0, 'Not found. Try PlugInstall.']
      endif
    else
      if is_dir
        let [valid, msg] = [1, 'OK']
      else
        let [valid, msg] = [0, 'Not found.']
      endif
    endif
    let cnt += 1
    let ecnt += !valid
    " `s:loaded` entry can be missing if PlugUpgraded
    if is_dir && get(s:loaded, name, -1) == 0
      let unloaded = 1
      let msg .= ' (not loaded)'
    endif
    call s:progress_bar(2, repeat('=', cnt), total)
    call append(3, s:format_message(valid ? '-' : 'x', name, msg))
    normal! 2G
    redraw
  endfor
  call setline(1, 'Finished. '.ecnt.' error(s).')
  normal! gg
  setlocal nomodifiable
  if unloaded
    echo "Press 'L' on each line to load plugin, or 'U' to update"
    nnoremap <silent> <buffer> L :call <SID>status_load(line('.'))<cr>
    xnoremap <silent> <buffer> L :call <SID>status_load(line('.'))<cr>
  end
endfunction

function! s:extract_name(str, prefix, suffix)
  return matchstr(a:str, '^'.a:prefix.' \zs[^:]\+\ze:.*'.a:suffix.'$')
endfunction

function! s:status_load(lnum)
  let line = getline(a:lnum)
  let name = s:extract_name(line, '-', '(not loaded)')
  if !empty(name)
    call plug#load(name)
    setlocal modifiable
    call setline(a:lnum, substitute(line, ' (not loaded)$', '', ''))
    setlocal nomodifiable
  endif
endfunction

function! s:status_update() range
  let lines = getline(a:firstline, a:lastline)
  let names = filter(map(lines, 's:extract_name(v:val, "[x-]", "")'), '!empty(v:val)')
  if !empty(names)
    echo
    execute 'PlugUpdate' join(names)
  endif
endfunction

function! s:is_preview_window_open()
  silent! wincmd P
  if &previewwindow
    wincmd p
    return 1
  endif
endfunction

function! s:find_name(lnum)
  for lnum in reverse(range(1, a:lnum))
    let line = getline(lnum)
    if empty(line)
      return ''
    endif
    let name = s:extract_name(line, '-', '')
    if !empty(name)
      return name
    endif
  endfor
  return ''
endfunction

function! s:preview_commit()
  if b:plug_preview < 0
    let b:plug_preview = !s:is_preview_window_open()
  endif

  let sha = matchstr(getline('.'), '^  \X*\zs[0-9a-f]\{7,9}')
  if empty(sha)
    let name = matchstr(getline('.'), '^- \zs[^:]*\ze:$')
    if empty(name)
      return
    endif
    let title = 'HEAD@{1}..'
    let command = 'git diff --no-color HEAD@{1}'
  else
    let title = sha
    let command = 'git show --no-color --pretty=medium '.sha
    let name = s:find_name(line('.'))
  endif

  if empty(name) || !has_key(g:plugs, name) || !isdirectory(g:plugs[name].dir)
    return
  endif

  if !s:is_preview_window_open()
    execute get(g:, 'plug_pwindow', 'vertical rightbelow new')
    execute 'e' title
  else
    execute 'pedit' title
    wincmd P
  endif
  setlocal previewwindow filetype=git buftype=nofile bufhidden=wipe nobuflisted modifiable
  let batchfile = ''
  try
    let [sh, shellcmdflag, shrd] = s:chsh(1)
    let cmd = 'cd '.plug#shellescape(g:plugs[name].dir).' && '.command
    if s:is_win
      let [batchfile, cmd] = s:batchfile(cmd)
    endif
    execute 'silent %!' cmd
  finally
    let [&shell, &shellcmdflag, &shellredir] = [sh, shellcmdflag, shrd]
    if s:is_win && filereadable(batchfile)
      call delete(batchfile)
    endif
  endtry
  setlocal nomodifiable
  nnoremap <silent> <buffer> q :q<cr>
  wincmd p
endfunction

function! s:section(flags)
  call search('\(^[x-] \)\@<=[^:]\+:', a:flags)
endfunction

function! s:format_git_log(line)
  let indent = '  '
  let tokens = split(a:line, nr2char(1))
  if len(tokens) != 5
    return indent.substitute(a:line, '\s*$', '', '')
  endif
  let [graph, sha, refs, subject, date] = tokens
  let tag = matchstr(refs, 'tag: [^,)]\+')
  let tag = empty(tag) ? ' ' : ' ('.tag.') '
  return printf('%s%s%s%s%s (%s)', indent, graph, sha, tag, subject, date)
endfunction

function! s:append_ul(lnum, text)
  call append(a:lnum, ['', a:text, repeat('-', len(a:text))])
endfunction

function! s:diff()
  call s:prepare()
  call append(0, ['Collecting changes ...', ''])
  let cnts = [0, 0]
  let bar = ''
  let total = filter(copy(g:plugs), 's:is_managed(v:key) && isdirectory(v:val.dir)')
  call s:progress_bar(2, bar, len(total))
  for origin in [1, 0]
    let plugs = reverse(sort(items(filter(copy(total), (origin ? '' : '!').'(has_key(v:val, "commit") || has_key(v:val, "tag"))'))))
    if empty(plugs)
      continue
    endif
    call s:append_ul(2, origin ? 'Pending updates:' : 'Last update:')
    for [k, v] in plugs
      let branch = s:git_origin_branch(v)
      if len(branch)
        let range = origin ? '..origin/'.branch : 'HEAD@{1}..'
        let cmd = ['git', 'log', '--graph', '--color=never']
        if s:git_version_requirement(2, 10, 0)
          call add(cmd, '--no-show-signature')
        endif
        call extend(cmd, ['--pretty=format:%x01%h%x01%d%x01%s%x01%cr', range])
        if has_key(v, 'rtp')
          call extend(cmd, ['--', v.rtp])
        endif
        let diff = s:system_chomp(cmd, v.dir)
        if !empty(diff)
          let ref = has_key(v, 'tag') ? (' (tag: '.v.tag.')') : has_key(v, 'commit') ? (' '.v.commit) : ''
          call append(5, extend(['', '- '.k.':'.ref], map(s:lines(diff), 's:format_git_log(v:val)')))
          let cnts[origin] += 1
        endif
      endif
      let bar .= '='
      call s:progress_bar(2, bar, len(total))
      normal! 2G
      redraw
    endfor
    if !cnts[origin]
      call append(5, ['', 'N/A'])
    endif
  endfor
  call setline(1, printf('%d plugin(s) updated.', cnts[0])
        \ . (cnts[1] ? printf(' %d plugin(s) have pending updates.', cnts[1]) : ''))

  if cnts[0] || cnts[1]
    nnoremap <silent> <buffer> <plug>(plug-preview) :silent! call <SID>preview_commit()<cr>
    if empty(maparg("\<cr>", 'n'))
      nmap <buffer> <cr> <plug>(plug-preview)
    endif
    if empty(maparg('o', 'n'))
      nmap <buffer> o <plug>(plug-preview)
    endif
  endif
  if cnts[0]
    nnoremap <silent> <buffer> X :call <SID>revert()<cr>
    echo "Press 'X' on each block to revert the update"
  endif
  normal! gg
  setlocal nomodifiable
endfunction

function! s:revert()
  if search('^Pending updates', 'bnW')
    return
  endif

  let name = s:find_name(line('.'))
  if empty(name) || !has_key(g:plugs, name) ||
    \ input(printf('Revert the update of %s? (y/N) ', name)) !~? '^y'
    return
  endif

  call s:system('git reset --hard HEAD@{1} && git checkout '.plug#shellescape(g:plugs[name].branch).' --', g:plugs[name].dir)
  setlocal modifiable
  normal! "_dap
  setlocal nomodifiable
  echo 'Reverted'
endfunction

function! s:snapshot(force, ...) abort
  call s:prepare()
  setf vim
  call append(0, ['" Generated by vim-plug',
                \ '" '.strftime("%c"),
                \ '" :source this file in vim to restore the snapshot',
                \ '" or execute: vim -S snapshot.vim',
                \ '', '', 'PlugUpdate!'])
  1
  let anchor = line('$') - 3
  let names = sort(keys(filter(copy(g:plugs),
        \'has_key(v:val, "uri") && isdirectory(v:val.dir)')))
  for name in reverse(names)
    let sha = has_key(g:plugs[name], 'commit') ? g:plugs[name].commit : s:git_revision(g:plugs[name].dir)
    if !empty(sha)
      call append(anchor, printf("silent! let g:plugs['%s'].commit = '%s'", name, sha))
      redraw
    endif
  endfor

  if a:0 > 0
    let fn = s:plug_expand(a:1)
    if filereadable(fn) && !(a:force || s:ask(a:1.' already exists. Overwrite?'))
      return
    endif
    call writefile(getline(1, '$'), fn)
    echo 'Saved as '.a:1
    silent execute 'e' s:esc(fn)
    setf vim
  endif
endfunction

function! s:split_rtp()
  return split(&rtp, '\\\@<!,')
endfunction

let s:first_rtp = s:escrtp(get(s:split_rtp(), 0, ''))
let s:last_rtp  = s:escrtp(get(s:split_rtp(), -1, ''))

if exists('g:plugs')
  let g:plugs_order = get(g:, 'plugs_order', keys(g:plugs))
  call s:upgrade_specs()
  call s:define_commands()
endif

let &cpo = s:cpo_save
unlet s:cpo_save
```

## File: `doc/plug.txt`
```
plug.txt	plug	Last change: Jun 1 2024
PLUG - TABLE OF CONTENTS                                         *plug* *plug-toc*
==============================================================================

  vim-plug                          |vim-plug|
    Pros.                           |plug-pros|
    Installation                    |plug-installation|
    Usage                           |plug-usage|
      Getting Help                  |plug-getting-help|
    Examples                        |plug-examples|
      Vim script example            |plug-vim-script-example|
      Lua example for Neovim        |plug-lua-example-for-neovim|
    Commands                        |plug-commands|
    Plug options                    |plug-options|
    Global options                  |plug-global-options|
    Keybindings                     |plug-keybindings|
    Post-update hooks               |plug-post-update-hooks|
      PlugInstall! and PlugUpdate!  |pluginstall-and-plugupdate|
    On-demand loading of plugins    |plug-on-demand-loading-of-plugins|
    Collaborators                   |plug-collaborators|
    License                         |plug-license|

VIM-PLUG                                                              *vim-plug*
==============================================================================

A minimalist Vim plugin manager.


PROS.                                                                *plug-pros*
==============================================================================

 - Minimalist design
   - Just one file with no dependencies. Super easy to set up.
   - Concise, intuitive syntax that you can learn within minutes. No
     boilerplate code required.
   - No feature bloat
 - Extremely stable with flawless backward compatibility
   - Works perfectly with all versions of Vim since 2006 and all versions of
     Neovim ever released
 - {Super-fast}{1} parallel installation/update
 - Creates shallow clones to minimize disk space usage and download time
 - On-demand loading for {faster startup time}{2}
 - Can review and rollback updates
 - Branch/tag/commit support
 - Post-update hooks
 - Support for externally managed plugins

  {1} https://raw.githubusercontent.com/junegunn/i/master/vim-plug/40-in-4.gif
  {2} https://github.com/junegunn/vim-startuptime-benchmark#result


INSTALLATION                                                 *plug-installation*
==============================================================================

{Download plug.vim}{3} and put it in the "autoload" directory.

       {3} https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim


USAGE                                                               *plug-usage*
==============================================================================

Add a vim-plug section to your `~/.vimrc` (or `init.vim` for Neovim)

                                                           *plug#begin* *plug#end*

 1. Begin the section with `call plug#begin()`
 2. List the plugins with `Plug` commands
 3. End the section with `call plug#end()`

For example,
>
    call plug#begin()

    " List your plugins here
    Plug 'tpope/vim-sensible'

    call plug#end()
<
Reload the file or restart Vim, then you can,

                                            *:PlugInstall* *:PlugUpdate* *:PlugDiff*

 - `:PlugInstall` to install the plugins
 - `:PlugUpdate` to install or update the plugins
 - `:PlugDiff` to review the changes from the last update

[!NOTE] That's basically all you need to know to get started. The rest of the
document is for advanced users who want to know more about the features and
options.


< Getting Help >______________________________________________________________~
                                                             *plug-getting-help*

 - See {tutorial}{4} page to learn more about the basics of vim-plug
 - See {tips}{5} and {FAQ}{6} pages for common problems and questions

                        {4} https://github.com/junegunn/vim-plug/wiki/tutorial
                        {5} https://github.com/junegunn/vim-plug/wiki/tips
                        {6} https://github.com/junegunn/vim-plug/wiki/faq


EXAMPLES                                                         *plug-examples*
==============================================================================

The following examples demonstrate the additional features of vim-plug.


< Vim script example >________________________________________________________~
                                                       *plug-vim-script-example*
>
    call plug#begin()
    " The default plugin directory will be as follows:
    "   - Vim (Linux/macOS): '~/.vim/plugged'
    "   - Vim (Windows): '~/vimfiles/plugged'
    "   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
    " You can specify a custom plugin directory by passing it as the argument
    "   - e.g. `call plug#begin('~/.vim/plugged')`
    "   - Avoid using standard Vim directory names like 'plugin'

    " Make sure you use single quotes

    " Shorthand notation for GitHub; translates to https://github.com/junegunn/seoul256.vim.git
    Plug 'junegunn/seoul256.vim'

    " Any valid git URL is allowed
    Plug 'https://github.com/junegunn/vim-easy-align.git'

    " Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
    Plug 'fatih/vim-go', { 'tag': '*' }

    " Using a non-default branch
    Plug 'neoclide/coc.nvim', { 'branch': 'release' }

    " Use 'dir' option to install plugin in a non-default directory
    Plug 'junegunn/fzf', { 'dir': '~/.fzf' }

    " Post-update hook: run a shell command after installing or updating the plugin
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

    " Post-update hook can be a lambda expression
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }

    " If the vim plugin is in a subdirectory, use 'rtp' option to specify its path
    Plug 'nsf/gocode', { 'rtp': 'vim' }

    " On-demand loading: loaded when the specified command is executed
    Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }

    " On-demand loading: loaded when a file with a specific file type is opened
    Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

    " Unmanaged plugin (manually installed and updated)
    Plug '~/my-prototype-plugin'

    " Call plug#end to update &runtimepath and initialize the plugin system.
    " - It automatically executes `filetype plugin indent on` and `syntax enable`
    call plug#end()
    " You can revert the settings after the call like so:
    "   filetype indent off   " Disable file-type-specific indentation
    "   syntax off            " Disable syntax highlighting

    " Color schemes should be loaded after plug#end().
    " We prepend it with 'silent!' to ignore errors when it's not yet installed.
    silent! colorscheme seoul256
<

< Lua example for Neovim >____________________________________________________~
                                                   *plug-lua-example-for-neovim*

In Neovim, you can write your configuration in a Lua script file named
`init.lua`. The following code is the Lua script equivalent to the Vim script
example above.
>
    local vim = vim
    local Plug = vim.fn['plug#']

    vim.call('plug#begin')

    -- Shorthand notation for GitHub; translates to https://github.com/junegunn/seoul256.vim.git
    Plug('junegunn/seoul256.vim')

    -- Any valid git URL is allowed
    Plug('https://github.com/junegunn/vim-easy-align.git')

    -- Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
    Plug('fatih/vim-go', { ['tag'] = '*' })

    -- Using a non-default branch
    Plug('neoclide/coc.nvim', { ['branch'] = 'release' })

    -- Use 'dir' option to install plugin in a non-default directory
    Plug('junegunn/fzf', { ['dir'] = '~/.fzf' })

    -- Post-update hook: run a shell command after installing or updating the plugin
    Plug('junegunn/fzf', { ['dir'] = '~/.fzf', ['do'] = './install --all' })

    -- Post-update hook can be a lambda expression
    Plug('junegunn/fzf', { ['do'] = function()
      vim.fn['fzf#install']()
    end })

    -- If the vim plugin is in a subdirectory, use 'rtp' option to specify its path
    Plug('nsf/gocode', { ['rtp'] = 'vim' })

    -- On-demand loading: loaded when the specified command is executed
    Plug('preservim/nerdtree', { ['on'] = 'NERDTreeToggle' })

    -- On-demand loading: loaded when a file with a specific file type is opened
    Plug('tpope/vim-fireplace', { ['for'] = 'clojure' })

    -- Unmanaged plugin (manually installed and updated)
    Plug('~/my-prototype-plugin')

    vim.call('plug#end')

    -- Color schemes should be loaded after plug#end().
    -- We prepend it with 'silent!' to ignore errors when it's not yet installed.
    vim.cmd('silent! colorscheme seoul256')
<

COMMANDS                                                         *plug-commands*
==============================================================================

 -------------------------------------+------------------------------------------------------------------
 Command                              | Description                                                      ~
 -------------------------------------+------------------------------------------------------------------
  `PlugInstall [name ...] [#threads]`  | Install plugins
  `PlugUpdate [name ...] [#threads]`   | Install or update plugins
  `PlugClean[!]`                       | Remove unlisted plugins (bang version will clean without prompt)
  `PlugUpgrade`                        | Upgrade vim-plug itself
  `PlugStatus`                         | Check the status of plugins
  `PlugDiff`                           | Examine changes from the previous update and the pending changes
  `PlugSnapshot[!] [output path]`      | Generate script for restoring the current snapshot of the plugins
 -------------------------------------+------------------------------------------------------------------


PLUG OPTIONS                                                      *plug-options*
==============================================================================

                                                               *<Plug>-mappings*

 ------------------------+------------------------------------------------------------
 Option                  | Description                                                ~
 ------------------------+------------------------------------------------------------
  `branch` / `tag` / `commit`  | Branch/tag/commit of the repository to use
  `rtp`                    | Subdirectory that contains Vim plugin
  `dir`                    | Custom directory for the plugin
  `as`                     | Use different name for the plugin
  `do`                     | Post-update hook (string or funcref)
  `on`                     | On-demand loading: Commands or <Plug>-mappings
  `for`                    | On-demand loading: File types
  `frozen`                 | Do not remove and do not update unless explicitly specified
 ------------------------+------------------------------------------------------------


GLOBAL OPTIONS                                             *plug-global-options*
==============================================================================

     *g:plug_threads* *g:plug_timeout* *g:plug_retries* *g:plug_shallow* *g:plug_window*
                                              *g:plug_pwindow* *g:plug_url_format*

 --------------------+-----------------------------------+-----------------------------------------------------------------------------------
 Flag                | Default                           | Description                                                                       ~
 --------------------+-----------------------------------+-----------------------------------------------------------------------------------
  `g:plug_threads`     | 16                                | Default number of threads to use
  `g:plug_timeout`     | 60                                | Time limit of each task in seconds (Ruby & Python)
  `g:plug_retries`     | 2                                 | Number of retries in case of timeout (Ruby & Python)
  `g:plug_shallow`     | 1                                 | Use shallow clone
  `g:plug_window`      |  `-tabnew`                          | Command to open plug window
  `g:plug_pwindow`     |  `vertical rightbelow new`          | Command to open preview window in  `PlugDiff`
  `g:plug_url_format`  |  `https://git::@github.com/%s.git`  |  `printf`  format to build repo URL (Only applies to the subsequent  `Plug`  commands)
 --------------------+-----------------------------------+-----------------------------------------------------------------------------------


KEYBINDINGS                                                   *plug-keybindings*
==============================================================================

 - `D` - `PlugDiff`
 - `S` - `PlugStatus`
 - `R` - Retry failed update or installation tasks
 - `U` - Update plugins in the selected range
 - `q` - Close the window
 - `:PlugStatus`
   - `L` - Load plugin
 - `:PlugDiff`
   - `X` - Revert the update


POST-UPDATE HOOKS                                       *plug-post-update-hooks*
==============================================================================

There are some plugins that require extra steps after installation or update.
In that case, use the `do` option to describe the task to be performed.
>
    Plug 'Shougo/vimproc.vim', { 'do': 'make' }
    Plug 'ycm-core/YouCompleteMe', { 'do': './install.py' }
<
If the value starts with `:`, it will be recognized as a Vim command.
>
    Plug 'fatih/vim-go', { 'do': ':GoInstallBinaries' }
<
To call a Vim function, you can pass a lambda expression like so:
>
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
<
If you need more control, you can pass a reference to a Vim function that
takes a dictionary argument.
>
    function! BuildYCM(info)
      " info is a dictionary with 3 fields
      " - name:   name of the plugin
      " - status: 'installed', 'updated', or 'unchanged'
      " - force:  set on PlugInstall! or PlugUpdate!
      if a:info.status == 'installed' || a:info.force
        !./install.py
      endif
    endfunction

    Plug 'ycm-core/YouCompleteMe', { 'do': function('BuildYCM') }
<
A post-update hook is executed inside the directory of the plugin and only run
when the repository has changed, but you can force it to run unconditionally
with the bang-versions of the commands: `PlugInstall!` and `PlugUpdate!`.

[!TIP] Make sure to escape BARs and double-quotes when you write the `do`
option inline as they are mistakenly recognized as command separator or the
start of the trailing comment.
>
    Plug 'junegunn/fzf', { 'do': 'yes \| ./install' }
<
But you can avoid the escaping if you extract the inline specification using a
variable (or any Vim script expression) as follows:
>
    let g:fzf_install = 'yes | ./install'
    Plug 'junegunn/fzf', { 'do': g:fzf_install }
<

< PlugInstall! and PlugUpdate! >______________________________________________~
                                                    *pluginstall-and-plugupdate*

The installer takes the following steps when installing/updating a plugin:

 1. `git clone` or `git fetch` from its origin
 2. Check out branch, tag, or commit and optionally `git merge` remote branch
 3. If the plugin was updated (or installed for the first time)
   1. Update submodules
   2. Execute post-update hooks

The commands with the `!` suffix ensure that all steps are run
unconditionally.


ON-DEMAND LOADING OF PLUGINS                 *plug-on-demand-loading-of-plugins*
==============================================================================
>
    " NERD tree will be loaded on the first invocation of NERDTreeToggle command
    Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }

    " Multiple commands
    Plug 'junegunn/vim-github-dashboard', { 'on': ['GHDashboard', 'GHActivity'] }

    " Loaded when clojure file is opened
    Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

    " Multiple file types
    Plug 'kovisoft/paredit', { 'for': ['clojure', 'scheme'] }

    " On-demand loading on both conditions
    Plug 'junegunn/vader.vim',  { 'on': 'Vader', 'for': 'vader' }

    " Code to execute when the plugin is lazily loaded on demand
    Plug 'junegunn/goyo.vim', { 'for': 'markdown' }
    autocmd! User goyo.vim echom 'Goyo is now loaded!'
<
[!NOTE] #### Should I set up on-demand loading?

You probably don't need to.

A properly implemented Vim plugin should already load lazily without any help
from a plugin manager (`:help autoload`). So there are few cases where these
options actually make much sense. Making a plugin load faster is the
responsibility of the plugin developer, not the user. If you find a plugin
that takes too long to load, consider opening an issue on the plugin's issue
tracker.

Let me give you a perspective. The time it takes to load a plugin is usually
less than 2 or 3ms on modern computers. So unless you use a very large number
of plugins, you are unlikely to save more than 50ms. If you have spent an hour
carefully setting up the options to shave off 50ms, you will have to start Vim
72,000 times just to break even. You should ask yourself if that's a good
investment of your time.

Make sure that you're tackling the right problem by breaking down the startup
time of Vim using `--startuptime`.
>
    vim --startuptime /tmp/log
<
On-demand loading should only be used as a last resort. It is basically a
hacky workaround and is not always guaranteed to work.

                                                                     *plug#load*

[!TIP] You can pass an empty list to `on` or `for` option to disable the
loading of the plugin. You can manually load the plugin using
`plug#load(NAMES...)` function.

See https://github.com/junegunn/vim-plug/wiki/tips#loading-plugins-manually


COLLABORATORS                                               *plug-collaborators*
==============================================================================

 - {Jan Edmund Lazo}{7} - Windows support
 - {Jeremy Pallats}{8} - Python installer

                                           {7} https://github.com/janlazo
                                           {8} https://github.com/starcraftman


LICENSE                                                           *plug-license*
==============================================================================

MIT

==============================================================================
vim:tw=78:sw=2:ts=2:ft=help:norl:nowrap:
```

## File: `test/README.md`
```markdown
Test cases for vim-plug
=======================

### Prerequisite

- [Vader.vim](https://github.com/junegunn/vader.vim)

### Run

```
./run

./run !
```

### TODO

Test cases for the following features are currently missing:

- Output formatting
- Timeout or interrupt cleaning up git processes
- User prompt in PlugClean command
- Single-threaded installer
- Windows support

```

## File: `test/functional.vader`
```
Execute (plug#shellescape() works without optional arguments):
  if has('unix')
    AssertEqual "''", plug#shellescape("")
    AssertEqual "'foo'\\'''", plug#shellescape("foo'")
  endif

Execute (plug#shellescape() ignores invalid optional argument):
  if has('unix')
    AssertEqual "''", plug#shellescape("", '')
    AssertEqual "'foo'\\'''", plug#shellescape("foo'", [])
  endif

Execute (plug#shellescape() depends on the shell):
  AssertEqual "'foo'\\'''", plug#shellescape("foo'", {'shell': 'sh'})
  AssertEqual '^"foo''^"', plug#shellescape("foo'", {'shell': 'cmd.exe'})
  AssertEqual "'foo'''", plug#shellescape("foo'", {'shell': 'powershell'})
  AssertEqual "'foo'''", plug#shellescape("foo'", {'shell': 'powershell.exe'})
  AssertEqual "'foo'''", plug#shellescape("foo'", {'shell': 'pwsh'})

Execute (plug#shellescape() supports non-trivial cmd.exe escaping):
  " batchfile
  AssertEqual '^"^^%%PATH^^%%^"', plug#shellescape("^%PATH^%", {
  \ 'shell': 'cmd.exe',
  \ })
  AssertEqual '^"^^%%PATH^^%%^"', plug#shellescape("^%PATH^%", {
  \ 'shell': 'cmd.exe',
  \ 'script': 1,
  \ })
  " command prompt
  AssertEqual '^"^^^%PATH^^^%^"', plug#shellescape("^%PATH^%", {
  \ 'shell': 'cmd.exe',
  \ 'script': 0,
  \ }),

Execute (plug#shellescape() supports non-trivial powershell.exe escaping):
  AssertEqual '''\"Foo\\''''\\Bar\"''', plug#shellescape('"Foo\''\Bar"', {
  \ 'shell': 'powershell',
  \ }),
  AssertEqual '''\"Foo\\''''\\Bar\"''', plug#shellescape('"Foo\''\Bar"', {
  \ 'shell': 'powershell.exe',
  \ }),
```

## File: `test/regressions.vader`
```
**********************************************************************
Execute (#112 On-demand loading should not suppress messages from ftplugin):
  call ResetPlug()
  call plug#begin('$PLUG_FIXTURES')
  Plug '$PLUG_FIXTURES/ftplugin-msg', { 'for': 'c' }
  call plug#end()

  redir => out
  tabnew a.c
  redir END
  Assert stridx(out, 'ftplugin-c') >= 0, 'Unexpected output (1): '.out

* The same applies to plug#load())
  call ResetPlug()
  redir => out
  call plug#load('ftplugin-msg')
  redir END
  Assert stridx(out, 'ftplugin-c') >= 0, 'Unexpected output (2): '.out
  q


**********************************************************************
Execute (#114 Should not contain empty path in &rtp):
  call plug#begin('/tmp/vim-plug-test/plugged')
  call plug#end()

  Log &rtp
  Assert &rtp !~ ',,', 'Commas'
  Assert &rtp !~ '^,', 'Comma prefix'
  Assert &rtp !~ ',$', 'Comma suffix'

**********************************************************************
Execute (#130 Proper cleanup of on-demand loading triggers):
  augroup PlugLOD
    autocmd!
  augroup END

  " Cleared on command
  call ReloadPlug()
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/vim-emoji', { 'on':  ['EmojiCommand', 'EmojiCommand2', '<Plug>(EmojiMapping)'] }
  call plug#end()
  PlugInstall | q
  call mkdir(g:plugs['vim-emoji'].dir.'/after/plugin', 'p')

  Assert exists(':EmojiCommand'), 'EmojiCommand not defined'
  Assert exists(':EmojiCommand2'), 'EmojiCommand2 not defined'
  Assert !empty(mapcheck('<Plug>(EmojiMapping)')), '<Plug>(EmojiMapping) not defined'

  silent! EmojiCommand

  Assert !exists(':EmojiCommand'), 'EmojiCommand defined'
  Assert !exists(':EmojiCommand2'), 'EmojiCommand2 defined'
  Assert empty(mapcheck('<Plug>(EmojiMapping)')), '<Plug>(EmojiMapping) defined'

  " Cleared on FileType
  call ReloadPlug()
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/vim-emoji', { 'on': ['EmojiCommandExtra', '<Plug>(EmojiMappingExtra)'], 'for': ['emoji'] }
  call plug#end()

  Assert exists(':EmojiCommandExtra'), 'EmojiCommandExtra not defined'
  Assert !empty(mapcheck('<Plug>(EmojiMappingExtra)')), '<Plug>(EmojiMappingExtra) not defined'

  setf emoji

  Assert !exists(':EmojiCommandExtra'), 'EmojiCommandExtra defined'
  Assert empty(mapcheck('<Plug>(EmojiMappingExtra)')), '<Plug>(EmojiMappingExtra) defined'

**********************************************************************
Execute (#131 Syntax error):
  call plug#begin('/proc/no-permission')
  Plug 'junegunn/vim-emoji'
  call plug#end()

  redir => out
  silent PlugInstall
  redir END
  Assert out =~ 'Invalid plug directory: /proc/no-permission', out

**********************************************************************
Execute (#139-1 Using new remote branch):
  " Make sure to remove the clone
  call plug#begin('/tmp/vim-plug-test/plugged')
  call plug#end()
  PlugClean!

  " Install master branch
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug expand('file:////tmp/vim-plug-test/new-branch')
  call plug#end()
  PlugUpdate

  unlet! g:foo g:bar g:baz
  call ResetPlug()
  call plug#load('new-branch')
  Assert exists('g:foo'),  'g:foo should be found (1)'
  Assert !exists('g:bar'), 'g:bar should not be found (1)'
  Assert !exists('g:baz'), 'g:baz should not be found (1)'

  " Create a new branch on origin
  call system('cd /tmp/vim-plug-test/new-branch && git checkout -b new &&'
      \. 'echo "let g:bar = 1" > plugin/bar.vim && git add plugin/bar.vim &&'
      \. 'git commit -m second')

  " We're setting up two plugins so that parallel installer is used
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/seoul256.vim'
  Plug expand('file:////tmp/vim-plug-test/new-branch'), { 'branch': 'new' }
  call plug#end()
  PlugUpdate
  silent %y
  Log @"
  Assert @" !~? 'error', 'Should be able to use new remote branch: ' . @"

  unlet! g:foo g:bar g:baz
  call ResetPlug()
  call plug#load('new-branch')
  Assert exists('g:foo'),  'g:foo should be found (2)'
  Assert exists('g:bar'),  'g:bar should be found (2)'
  Assert !exists('g:baz'), 'g:baz should not be found (2)'

  call PlugStatusSorted()

Expect:
  - new-branch: OK
  - seoul256.vim: OK
  Finished. 0 error(s).
  [==]

Execute (#139-2 Using yet another new remote branch):
  " Create another branch on origin
  call system('cd /tmp/vim-plug-test/new-branch && git checkout master &&'
      \. 'git checkout -b brand-new &&'
      \. 'echo "let g:baz = 1" > plugin/baz.vim && git add plugin/baz.vim &&'
      \. 'git commit -m third')

  " Test Vim installer here
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug expand('file:////tmp/vim-plug-test/new-branch'), { 'branch': 'brand-new' }
  call plug#end()
  PlugUpdate
  silent %y
  Log @"
  Assert @" !~? 'error', 'Should be able to use new remote branch: ' . @"

  unlet! g:foo g:bar g:baz
  call ResetPlug()
  call plug#load('new-branch')
  Assert exists('g:foo'),  'g:foo should be found'
  Assert !exists('g:bar'), 'g:bar should not be found'
  Assert exists('g:baz'),  'g:baz should be found'

  call PlugStatusSorted()

Expect:
  - new-branch: OK
  Finished. 0 error(s).
  [=]

Execute (#139-3 Should fail when not possible to fast-forward):
  " Commit on cloned repo
  call system('cd /tmp/vim-plug-test/plugged/new-branch && git checkout master &&'
      \. 'touch foobar && git add foobar && git commit -m foobar')

  " Different commit on remote
  call system('cd /tmp/vim-plug-test/new-branch && git checkout master &&'
      \. 'touch foobaz && git add foobaz && git commit -m foobaz')

  for multi in [0, 1]
    call plug#begin('/tmp/vim-plug-test/plugged')
    if multi
      Plug 'junegunn/seoul256.vim'
    endif
    Plug expand('file:////tmp/vim-plug-test/new-branch')
    call plug#end()
    PlugUpdate
    silent %y
    Assert @" =~ 'Not possible to fast-forward', @"
  endfor
  q

**********************************************************************
Execute (#145: Merging on-demand loading triggers - cmd):
  unlet! g:xxx g:yyy
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'on': 'XXX' }
  Plug '$PLUG_FIXTURES/yyy', { 'on': ['XXX', 'YYY'] }
  call plug#end()

  silent! XXX

  Assert exists('g:xxx'), 'xxx is not loaded'
  Assert exists('g:yyy'), 'yyy is not loaded'
  Assert !exists(':YYY')

Execute (#145: Merging on-demand loading triggers - map):
  unlet! g:xxx g:yyy

  call ReloadPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'on': '<Plug>(xxx)' }
  Plug '$PLUG_FIXTURES/yyy', { 'on': ['<Plug>(xxx)' ,'<Plug>(yyy)' ] }
  call plug#end()

  Assert !empty(mapcheck("<Plug>(xxx)"))
  Assert !empty(mapcheck("<Plug>(yyy)"))

# FIXME feedkeys() cannot be tested with Vader
  call plug#load('xxx', 'yyy')
  Assert empty(mapcheck("<Plug>(xxx)"))
  Assert empty(mapcheck("<Plug>(yyy)"))

**********************************************************************
Execute (#159: shell=/bin/tcsh):
  let org = &shell
  try
    set shell=/bin/tcsh
    call plug#begin('/tmp/vim-plug-test/plugged')
    Plug 'junegunn/seoul256.vim'
    call plug#end()

    PlugStatus
    Log getline(1, '$')
    q
    AssertEqual '/bin/tcsh', &shell
  finally
    let &shell = org
  endtry

**********************************************************************
Execute (#154: Spaces in &rtp should not be escaped):
  call plug#begin('/tmp/vim-plug-test/plug it')
  Plug 'foo/seoul256 vim'
  call plug#end()
  Log &rtp
  Assert stridx(&rtp, 'plug it/seoul256 vim') >= 0

**********************************************************************
Execute (#184: Duplicate entries in &rtp):
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'foo/plugin1'
    \| Plug 'foo/plugin0'

  Plug 'foo/plugin2'
    \| Plug 'foo/plugin0'
    \| Plug 'foo/plugin1'
  call plug#end()

  Log &rtp
  AssertEqual 3, len(filter(split(&rtp, ','), 'stridx(v:val, "plugged") >= 0'))

**********************************************************************
Execute (#236: Plugin removed from &rtp when .vimrc is reloaded):
  unlet! g:loaded_easy_align_plugin
  silent! delc EasyAlign

  call ReloadPlug()
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/vim-easy-align', { 'on': 'EasyAlign' }
  call plug#end()
  PlugInstall | q

  Assert &rtp !~ '/vim-easy-align', 'Plugin should not be in &rtp'
  %EasyAlign=
  Assert &rtp =~ '/vim-easy-align', 'Plugin should be in &rtp'

  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/vim-easy-align', { 'on': 'EasyAlign' }
  call plug#end()
  Assert &rtp =~ '/vim-easy-align', 'Plugin should still be in &rtp'

**********************************************************************
Execute (#350: Ruby installer failed to unshallow tagged plugin on update):
  call plug#begin('/tmp/vim-plug-test/plugged')
  call plug#end()
  PlugClean!

  " Shallow clone. We should have at least 2 plugins to enable parallel installer.
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/vim-easy-align'
  Plug 'junegunn/seoul256.vim'
  call plug#end()
  PlugUpdate
  Assert filereadable(g:plugs['vim-easy-align'].dir.'/.git/shallow')

  " Now unshallowed
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/vim-easy-align', { 'tag': '2.9.0' }
  Plug 'junegunn/seoul256.vim'
  call plug#end()
  PlugUpdate
  Assert !filereadable(g:plugs['vim-easy-align'].dir.'/.git/shallow')
  q

**********************************************************************
Execute (#474: Load ftdetect files in filetypedetect augroup):
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/rust.vim', { 'for': 'rust', 'commit': '115d321d383eb96d438466c56cc871fcc1bd0faa' }
  call plug#end()
  PlugInstall!
  q

  tabnew /tmp/vim-plug-test/any.rs
  AssertEqual 'rust', &filetype
  Log &filetype
  filetype detect
  AssertEqual 'rust', &filetype
  Log &filetype
  bd

**********************************************************************
Execute (#489/#587 On-demand loading with 'on' option should trigger BufRead autocmd w/o nomodeline):
  call plug#begin('$PLUG_FIXTURES')
  Plug 'foo/ftplugin-msg', { 'on': 'XXX' }
  call plug#end()

  tabnew a.java
  call setline(1, '// vim: set filetype=lava:')
  redir => out
  silent! XXX
  redir END
  Assert stridx(out, 'ftplugin-java') >= 0
  AssertEqual 'lava', &filetype
  q!

**********************************************************************
Execute (Cursor moved to another window during post-update hook):
  function! DoSplit(...)
    new
    call setline(1, 'empty')
  endfunction
  call plug#begin('/tmp/vim-plug-test/plugged')
  Plug 'junegunn/rust.vim', { 'do': function('DoSplit') }
  call plug#end()
  PlugInstall!
  AssertEqual 1, line('$')
  AssertEqual 'empty', getline(1)
  q!
  q

**********************************************************************
Execute (#593 Add plugin to &rtp before running post-update hook with : prefix):
  call ReloadPlug()
  call plug#begin()
  Plug 'junegunn/vim-pseudocl', { 'on': 'XXX', 'do': ':let g:bar = pseudocl#complete#extract_words(''a b'')' }
  call plug#end()
  PlugInstall!
  AssertEqual ['a', 'b'], g:bar

**********************************************************************
Execute (#602 Confusion with branch name and path name):
  call plug#begin()
  Plug expand('file:////tmp/vim-plug-test/new-branch'), { 'branch': 'plugin' }
  call plug#end()
  PlugUpdate
  call PlugStatusSorted()

Expect:
  - new-branch: OK
  Finished. 0 error(s).
  [=]

**********************************************************************
Execute (PlugStatus showed error with wildcard tag):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'tag': '*' }
  call plug#end()
  PlugUpdate
  call PlugStatusSorted()

Expect:
  - vim-easy-align: OK
  Finished. 0 error(s).
  [=]
```

## File: `test/run`
```
#!/bin/bash

# Privileged mode, ignores $CDPATH etc.
set -p
set -eu

cd "$(dirname "${BASH_SOURCE[0]}")"

export BASE="$PWD"
export PLUG_SRC="$PWD/../plug.vim"
export PLUG_FIXTURES="$PWD/fixtures"
mkdir -p "$PLUG_FIXTURES"
export TEMP=/tmp/vim-plug-test
rm -rf "$TEMP"
mkdir -p "$TEMP"

cat > $TEMP/mini-vimrc << VIMRC
set rtp+=$TEMP/junegunn/vader.vim
set shell=/bin/bash
VIMRC

clone() {
  if [ ! -d "$2" ]; then
    git clone "$1" "$2"
  fi
}

clone_repos() (
  cd $TEMP
  mkdir -p junegunn vim-scripts jg
  for repo in vader.vim goyo.vim rust.vim seoul256.vim vim-easy-align vim-fnr \
              vim-oblique vim-pseudocl vim-redis vim-emoji; do
    clone https://github.com/junegunn/${repo}.git junegunn/$repo &
  done
  clone https://github.com/vim-scripts/beauty256.git vim-scripts/beauty256 &
  clone https://github.com/junegunn/fzf.git fzf &
  clone https://github.com/yous/subsubmodule.git yous/subsubmodule && \
    (cd yous/subsubmodule && git submodule update --init --recursive &) &
  wait

  clone junegunn/vim-emoji jg/vim-emoji
  cd junegunn/seoul256.vim && git checkout no-t_co && git checkout master
)

make_dirs() (
  rm -rf "$PLUG_FIXTURES/$1"
  mkdir -p "$PLUG_FIXTURES/$1"
  cd "$PLUG_FIXTURES/$1"
  mkdir -p autoload colors ftdetect ftplugin indent plugin syntax
  for d in *; do
    [ -d "$d" ] || continue
    cat > "$d/xxx.vim" << EOF
    " echom expand('<sfile>')
    let g:total_order = get(g:, 'total_order', [])
    let g:$2 = get(g:, '$2', [])
    let s:name = join(filter(['$2', '${1:4}', '$d'], '!empty(v:val)'), '/')
    call add(g:$2, s:name)
    call add(g:total_order, s:name)
EOF
  done
)

gitinit() (
  cd "$PLUG_FIXTURES/$1"
  git init -b master
  git commit -m 'commit' --allow-empty
)

prepare() {
  make_dirs xxx/ xxx
  make_dirs xxx/after xxx
  mkdir -p "$PLUG_FIXTURES/xxx/doc"
  cat > "$PLUG_FIXTURES/xxx/doc/xxx.txt" << DOC
hello *xxx*
DOC
  gitinit xxx

  make_dirs yyy/ yyy
  make_dirs yyy/after yyy
  mkdir -p "$PLUG_FIXTURES/yyy/rtp/doc"
  cat > "$PLUG_FIXTURES/yyy/rtp/doc/yyy.txt" << DOC
hello *yyy*
DOC
  gitinit yyy

  make_dirs z1/ z1
  make_dirs z2/ z2

  rm -rf "$PLUG_FIXTURES/ftplugin-msg"
  mkdir -p "$PLUG_FIXTURES"/ftplugin-msg/{plugin,ftplugin}
  echo "echomsg 'ftplugin-c'" > "$PLUG_FIXTURES/ftplugin-msg/ftplugin/c.vim"
  echo "echomsg 'ftplugin-java'" > "$PLUG_FIXTURES/ftplugin-msg/ftplugin/java.vim"

  chmod +w "$PLUG_FIXTURES/cant-delete/autoload" || rm -rf "$PLUG_FIXTURES/cant-delete"
  mkdir -p "$PLUG_FIXTURES/cant-delete/autoload"
  touch "$PLUG_FIXTURES/cant-delete/autoload/cant-delete.vim"
  chmod -w "$PLUG_FIXTURES/cant-delete/autoload"

  rm -rf $TEMP/new-branch
  cd $TEMP
  git init new-branch -b master
  cd new-branch
  mkdir plugin
  echo 'let g:foo = 1' > plugin/foo.vim
  git add plugin/foo.vim
  git commit -m initial
  git checkout -b plugin
  git checkout master

  cd "$BASE"
}

select_vim() {
  local vim=/usr/bin/vim
  if [ -n "${DEPS:-}" ] && [ -e "${DEPS}/bin/vim" ]; then
    vim="${DEPS}/bin/vim"
  elif [ -e "/usr/local/bin/vim" ]; then
    vim=/usr/local/bin/vim
  fi
  echo $vim
}

clone_repos
prepare

git --version
vim=$(select_vim)
echo "Selected Vim: $vim"
if [ "${1:-}" = '!' ]; then
  FAIL=0
  $vim -Nu $TEMP/mini-vimrc -c 'Vader! test.vader' > /dev/null || FAIL=1
  prepare
  $vim -Nu $TEMP/mini-vimrc -c 'let g:plug_threads = 1 | Vader! test.vader' > /dev/null || FAIL=1
  test $FAIL -eq 0
else
  $vim -Nu $TEMP/mini-vimrc -c 'Vader test.vader'
fi
```

## File: `test/test.vader`
```
Execute (Initialize test environment):
  Save &rtp, g:plugs, g:plug_home, g:plug_window
  unlet! g:plugs g:plug_home g:plug_window

  let g:plug_url_format = 'file:///tmp/vim-plug-test/%s'
  let g:base_rtp        = &rtp
  let g:first_rtp       = split(&rtp, ',')[0]
  let g:last_rtp        = split(&rtp, ',')[-1]
  let g:temp_plugged    = tempname()
  if !exists('$PLUG_SRC')
    let $PLUG_SRC = globpath(&rtp, 'autoload/plug.vim')
  endif
  let $PLUG_TMP = fnamemodify(tempname(), ':h').'/plug.vim'

  " Temporarily patch plug.vim
  call system('cp "$PLUG_SRC" "$PLUG_TMP"')
  let patch =
  \ ['function! ResetPlug()', 'let s:loaded = {}', 'endfunction',
  \  'function! CompareURI(a, b)', 'return s:compare_git_uri(a:a, a:b)', 'endfunction']

  call writefile(extend(readfile($PLUG_TMP), patch), $PLUG_TMP)

  set t_Co=256
  colo default
  pclose

  function! PlugStatusSorted()
    PlugStatus
    %y
    q
    normal! P
    %sort
    g/^$/d
  endfunction

  function! AssertExpect(bang, pat, cnt, ...)
    let op = a:bang ? '==#' : '=~#'
    let args = [a:cnt, len(filter(getline(1, '$'), "v:val ".op." '".a:pat."'"))] + a:000
    call call('vader#assert#equal', args)
  endfunction
  command! -nargs=+ -bang AssertExpect call AssertExpect('<bang>' == '!', <args>)

  function! EnsureLoaded()
    if has('vim_starting')
      runtime! plugin/**/*.vim
    endif
  endfunction

  function! RmRf(file)
    call system(printf('rm -rf "%s"', a:file))
  endfunction

  function! ReloadPlug()
    call ResetPlug()
    source $PLUG_TMP
    let &rtp = g:base_rtp
  endfunction

  function! GitBranch(repo)
    return system(printf('cd %s && git rev-parse --abbrev-ref HEAD', g:plugs[a:repo].dir))[:-2]
  endfunction

  function! GitTag(repo)
    return system(printf('cd %s && git describe --tags', g:plugs[a:repo].dir))[:-2]
  endfunction

  function! GitCommit(repo)
    return system(printf('cd %s && git rev-parse HEAD', g:plugs[a:repo].dir))[:-2]
  endfunction

  source $PLUG_TMP

Execute (Print Interpreter Version):
  redir => out
  if has('ruby')
    silent! ruby puts 'Ruby: ' + RUBY_VERSION
  endif
  if has('python')
    silent! python import sys; svi = sys.version_info; print 'Python: {}.{}.{}'.format(svi[0], svi[1], svi[2])
  endif
  if has('python3')
    silent! python3 import sys; svi = sys.version_info; print('Python: {}.{}.{}'.format(svi[0], svi[1], svi[2]))
  endif
  redir END
  Log split(out, '\n')

Include: workflow.vader
Include: regressions.vader
Include: functional.vader

Execute (Cleanup):
  silent! call RmRf(g:temp_plugged)
  silent! unlet g:plugs g:plug_home g:plug_url_format
  silent! unlet g:temp_plugged g:first_rtp g:last_rtp g:base_rtp out
  silent! delf PlugStatusSorted
  silent! delf AssertExpect
  silent! delf PlugUpdated
  silent! delf EnsureLoaded
  silent! delf ReloadPlug
  silent! delc AssertExpect
  silent! unmap /
  silent! unmap ?
  call delete($PLUG_TMP)

  Restore

```

## File: `test/workflow.vader`
```
Execute (plug#end() before plug#begin() should fail):
  redir => out
  silent! AssertEqual 0, plug#end()
  redir END
  Assert stridx(out, 'plug#end() called without calling plug#begin() first') >= 0

Execute (plug#begin() without path argument):
  call plug#begin()
  AssertEqual split(&rtp, ',')[0].'/plugged', g:plug_home
  unlet g:plug_home

Execute (plug#begin() without path argument with empty &rtp):
  let save_rtp = &rtp
  set rtp=
  redir => out
  AssertEqual 0, plug#begin()
  redir END
  Assert stridx(out, 'Unable to determine plug home') >= 0
  let &rtp = save_rtp
  unlet save_rtp

Execute (Standard runtime path is not allowed):
  redir => out
  silent! AssertEqual 0, plug#begin(split(&rtp, ',')[0].'/plugin')
  redir END
  Log out
  Assert stridx(out, 'Invalid plug home') >= 0

Execute (plug#begin(path)):
  call plug#begin(g:temp_plugged.'/')
  Assert g:plug_home !~ '[/\\]$', 'Trailing / should be stripped from g:plug_home'

  AssertEqual 0, len(g:plugs)
  AssertEqual g:temp_plugged, g:plug_home
  AssertEqual g:base_rtp, &rtp

Execute (Subsequent plug#begin() calls will reuse g:plug_home):
  call plug#begin()
  AssertEqual g:temp_plugged, g:plug_home

Execute (Test Plug command):
^ Git repo with branch (DEPRECATED. USE BRANCH OPTION)
  Plug 'junegunn/seoul256.vim', { 'branch': 'yes-t_co' }
  AssertEqual 'file:///tmp/vim-plug-test/junegunn/seoul256.vim', g:plugs['seoul256.vim'].uri
  AssertEqual join([g:temp_plugged, 'seoul256.vim/'], '/'), g:plugs['seoul256.vim'].dir
  AssertEqual 'yes-t_co', g:plugs['seoul256.vim'].branch

  Plug 'junegunn/seoul256.vim', { 'branch': 'no-t_co' } " Using branch option
  AssertEqual 'no-t_co', g:plugs['seoul256.vim'].branch

^ Git repo with tag (DEPRECATED. USE TAG OPTION)
  redir => out
  silent Plug 'foo/bar.vim', ''
  redir END
  Assert out =~ 'Invalid argument for "tag" option of :Plug (expected: string)'
  Plug 'junegunn/goyo.vim', '1.5.2'
  AssertEqual 'file:///tmp/vim-plug-test/junegunn/goyo.vim', g:plugs['goyo.vim'].uri
  AssertEqual join([g:temp_plugged, 'goyo.vim/'], '/'), g:plugs['goyo.vim'].dir
  AssertEqual '1.5.2', g:plugs['goyo.vim'].tag

  redir => out
  silent Plug 'foo/bar.vim', {'tag': ''}
  redir END
  Assert out =~ 'Invalid argument for "tag" option of :Plug (expected: string)'
  Plug 'junegunn/goyo.vim', { 'tag': '1.5.3' } " Using tag option
  AssertEqual '1.5.3', g:plugs['goyo.vim'].tag

  " Git URI
  Plug 'file:///tmp/vim-plug-test/jg/vim-emoji'
  AssertEqual 'file:///tmp/vim-plug-test/jg/vim-emoji', g:plugs['vim-emoji'].uri
  AssertEqual '', g:plugs['vim-emoji'].branch
  AssertEqual join([g:temp_plugged, 'vim-emoji/'], '/'), g:plugs['vim-emoji'].dir

  " vim-scripts/
  Plug 'vim-scripts/beauty256'
  AssertEqual 'file:///tmp/vim-plug-test/vim-scripts/beauty256', g:plugs.beauty256.uri
  AssertEqual '', g:plugs.beauty256.branch

  AssertEqual 4, len(g:plugs)

  redir => out
  Plug 'beauty256'
  redir END
  Assert out =~ 'Invalid argument: beauty256'

Execute (Plug command with dictionary option):
  Log string(g:plugs)
  for opt in ['branch', 'tag', 'commit', 'rtp', 'dir', 'as']
    let opts = {}
    let opts[opt] = ''
    redir => out
    silent Plug 'foo/bar.vim', opts
    redir END
    Assert out =~ 'Invalid argument for "'.opt.'" option of :Plug (expected: string)'
  endfor
  for opt in ['on', 'for']
    let opts = {}
    let opts[opt] = ''
    redir => out
    silent Plug 'foo/bar.vim', opts
    redir END
    Assert out =~ 'Invalid argument for "'.opt.'" option of :Plug (expected: string or list)'
  endfor
  redir => out
  silent Plug 'foo/bar.vim', {'do': ''}
  redir END
  Assert out =~ 'Invalid argument for "do" option of :Plug (expected: string or funcref)'
  Plug 'junegunn/seoul256.vim', { 'branch': 'no-t_co', 'rtp': '././' }
  AssertEqual join([g:temp_plugged, 'seoul256.vim/'], '/'), g:plugs['seoul256.vim'].dir
  AssertEqual '././', g:plugs['seoul256.vim'].rtp

  Log string(g:plugs)
  AssertEqual 4, len(g:plugs)

Execute (PlugStatus before installation):
  PlugStatus
  AssertExpect 'Not found', 4
  q

Execute (PlugClean before installation):
  PlugClean
  AssertExpect 'Already clean', 1
  q

Execute (plug#end() updates &rtp):
  " Plug 'junegunn/goyo.vim', { 'tag': '1.5.3' }
  " Plug 'file:///tmp/vim-plug-test/jg/vim-emoji'
  " Plug 'beauty256'
  " Plug 'junegunn/seoul256.vim', { 'branch': 'no-t_co', 'rtp': '././' }
  call plug#end()
  Assert len(&rtp) > len(g:base_rtp)
  AssertEqual g:first_rtp, split(&rtp, ',')[0]
  AssertEqual g:last_rtp, split(&rtp, ',')[-1]

Execute (Yet, plugins are not available):
  Assert empty(globpath(&rtp, 'autoload/emoji.vim'))

Execute (PlugInstall):
  PlugInstall
  q

Execute (Plugin available after installation):
  Assert !empty(globpath(&rtp, 'autoload/emoji.vim'))

Execute (PlugClean after installation):
  PlugClean
  AssertExpect 'Already clean', 1
  q

Execute (PlugStatus after installation):
  PlugStatus
  Log getline(1, '$')
  AssertExpect 'OK', 4
  q

Execute (PlugUpdate - tagged plugin should not fail (#174)):
  PlugUpdate goyo.vim
  Log getline(1, '$')
  AssertExpect '^- goyo.vim', 1
  q

Execute (Change tag of goyo.vim):
  call plug#begin()
  Plug 'junegunn/goyo.vim', { 'tag': '9.9.9' }
  call plug#end()

Execute (PlugStatus):
  call PlugStatusSorted()

Expect:
      Invalid tag: 1.5.3 (expected: 9.9.9). Try PlugUpdate.
  Finished. 1 error(s).
  [=]
  x goyo.vim:

Execute (Remove tag of goyo.vim):
  call plug#begin()
  Plug 'junegunn/goyo.vim'
  call plug#end()

Execute (PlugStatus):
  call PlugStatusSorted()

Expect:
      Invalid branch: HEAD (expected: master). Try PlugUpdate.
  Finished. 1 error(s).
  [=]
  x goyo.vim:

Execute (PlugUpdate to set the right branch):
  PlugUpdate
  call PlugStatusSorted()

Expect:
  - goyo.vim: OK
  Finished. 0 error(s).
  [=]

Execute (Change branch of seoul256.vim):
  call plug#begin()
  Plug 'junegunn/seoul256.vim'
  Plug 'file:///tmp/vim-plug-test/jg/vim-emoji'
  call plug#end()

Execute (PlugStatus):
  call PlugStatusSorted()

Expect:
      Invalid branch: no-t_co (expected: master). Try PlugUpdate.
  - vim-emoji: OK
  Finished. 1 error(s).
  [==]
  x seoul256.vim:

Execute (PlugUpdate to switch branch, then PlugStatus):
  PlugUpdate
  call PlugStatusSorted()

Expect:
  - seoul256.vim: OK
  - vim-emoji: OK
  Finished. 0 error(s).
  [==]

Execute (Change tag of seoul256.vim):
  call plug#begin()
  Plug 'junegunn/seoul256.vim', { 'tag': 'no-such-tag' }
  call plug#end()
  call PlugStatusSorted()

Expect:
      Invalid tag: N/A (expected: no-such-tag). Try PlugUpdate.
  Finished. 1 error(s).
  [=]
  x seoul256.vim:

Execute (Change URI of seoul256.vim):
  call plug#begin()
  Plug 'junegunn.choi/seoul256.vim'
  Plug 'file:///tmp/vim-plug-test/jg/vim-emoji'
  call plug#end()

Execute (PlugStatus):
  call PlugStatusSorted()

Expect:
      Expected:    file:///tmp/vim-plug-test/junegunn.choi/seoul256.vim
      Invalid URI: file:///tmp/vim-plug-test/junegunn/seoul256.vim
      PlugClean required.
  - vim-emoji: OK
  Finished. 1 error(s).
  [==]
  x seoul256.vim:

Execute (Corrected the URI but ahead of upstream):
  call plug#begin()
  Plug 'junegunn/seoul256.vim'
  Plug 'file:///tmp/vim-plug-test/jg/vim-emoji'
  call plug#end()
  for _ in range(3)
    call system(printf('cd "%s" && git commit --allow-empty -m "dummy"', g:plugs['seoul256.vim'].dir))
  endfor
  call PlugStatusSorted()

Expect:
      Ahead of origin/master by 3 commit(s).
      Cannot update until local changes are pushed.
  - vim-emoji: OK
  Finished. 1 error(s).
  [==]
  x seoul256.vim:

# TODO: does not work due to inputsave()
# Do (PlugClean):
#   :PlugClean\<Enter>y\<Enter>
#   ggyG
#   q
#   PGdd

Execute (PlugClean! keeps seoul256.vim):
  PlugClean!
  " Two removed, emoji and seoul256 left
  AssertEqual 'Removed 2 directories.', getline(4)
  AssertExpect '^\~ ', 2
  AssertExpect 'Diverged', 0
  Assert !empty(globpath(&rtp, 'colors/seoul256.vim'))
  Assert !empty(globpath(&rtp, 'autoload/emoji.vim'))
  q

Execute (Make seoul256 to be diverged):
  call plug#begin()
  Plug 'junegunn/seoul256.vim'
  Plug 'file:///tmp/vim-plug-test/jg/vim-emoji'
  call plug#end()
  call system(printf(join([
    \ 'cd "%s"',
    \ 'git fetch --unshallow',
    \ 'git reset "@{u}~1"',
    \ 'git commit --allow-empty -m "diverged1"',
    \ 'git commit --allow-empty -m "diverged2"'], ' && '),
    \ g:plugs['seoul256.vim'].dir))
  Assert empty(v:shell_error), 'Got shell error: '.v:shell_error
  call PlugStatusSorted()

Expect:
      Backup local changes and run PlugClean and PlugUpdate to reinstall it.
      Diverged from origin/master (2 commit(s) ahead and 1 commit(s) behind!
  - vim-emoji: OK
  Finished. 1 error(s).
  [==]
  x seoul256.vim:

Execute (PlugClean! removes seoul256.vim):
  PlugClean!
  " One removed, emoji left
  AssertEqual 'Removed 1 directories.', getline(4)
  AssertExpect '^\~ ', 1
  AssertExpect 'Diverged', 1
  Assert empty(globpath(&rtp, 'colors/seoul256.vim'))
  Assert !empty(globpath(&rtp, 'autoload/emoji.vim'))
  q

Execute (Change GIT URI of vim-emoji):
  call plug#begin()
  Plug 'junegunn/seoul256.vim'
  Plug 'junegunn/vim-emoji'
  call plug#end()

Execute (PlugStatus):
  call PlugStatusSorted()

Expect:
      Expected:    file:///tmp/vim-plug-test/junegunn/vim-emoji
      Invalid URI: file:///tmp/vim-plug-test/jg/vim-emoji
      Not found. Try PlugInstall.
      PlugClean required.
  Finished. 2 error(s).
  [==]
  x seoul256.vim:
  x vim-emoji:

Execute (PlugClean! to remove vim-emoji):
  PlugClean!
  AssertExpect '^\~ ', 1
  AssertEqual 'Removed 1 directories.', getline(4)
  Assert empty(globpath(&rtp, 'colors/seoul256.vim')), 'seoul256.vim was removed'
  Assert empty(globpath(&rtp, 'autoload/emoji.vim')), 'emoji was removed'
  q

Execute (PlugUpdate to install both again):
  PlugUpdate
  AssertExpect '^- [^:]*:', 2
  Assert !empty(globpath(&rtp, 'colors/seoul256.vim')), 'seoul256.vim should be found'
  Assert !empty(globpath(&rtp, 'autoload/emoji.vim')), 'vim-emoji should be found'
  q

Execute (PlugUpdate only to find out plugins are up-to-date, D key to check):
  PlugUpdate
  AssertExpect 'Already up.to.date', 2, 'Expected 2 times "Already up-to-date", but got: '.string(getline(1, '$'))
  normal D
  AssertEqual '0 plugin(s) updated.', getline(1)
  q

Execute (PlugDiff - 'No updates.'):
  PlugDiff
  Log getline(1, '$')
  AssertEqual '0 plugin(s) updated.', getline(1)
  Assert empty(mapcheck('o'))
  Assert empty(mapcheck('X'))
  Assert empty(mapcheck("\<cr>"))
  q

Execute (New commits on remote, PlugUpdate, then PlugDiff):
  let g:plug_window = 'vertical topleft new'
  let g:plug_pwindow = 'above 12new'

  for repo in ['seoul256.vim', 'vim-emoji']
    for _ in range(2)
      call system(printf('cd /tmp/vim-plug-test/junegunn/%s && git commit --allow-empty -m "update"', repo))
    endfor
  endfor
  unlet repo
  PlugUpdate

  " Now we have updates
  normal D
  AssertEqual '2 plugin(s) updated.', getline(1)
  AssertThrows execute('/gpg')

  " Preview commit
  silent! wincmd P
  AssertEqual 0, &previewwindow

  " ]] motion
  execute 'normal ]]'
  let lnum = line('.')
  AssertEqual 3, col('.')

  " Open full diff (empty)
  execute "normal \<cr>"
  wincmd P
  AssertEqual 1, &previewwindow
  AssertEqual 'git', &filetype
  AssertEqual [''], getline(1, '$')
  pclose

  " Open commit preview
  execute "normal j\<cr>"
  wincmd P
  AssertEqual 1, &previewwindow
  AssertEqual 'git', &filetype

  " Close preview window
  pclose

  " Open and go to preview window with a custom mapping
  nmap <buffer> <c-o> <plug>(plug-preview)<c-w>P
  execute "normal \<c-o>"
  AssertEqual 1, &previewwindow, 'Should be on preview window'
  normal q
  AssertEqual 0, &previewwindow, 'Should not be on preview window'

  " ]] motion
  execute 'normal $]]'
  Assert line('.') >= 4
    " 5+ for merge commit
  AssertEqual 3, col('.')

  " [[ motion
  execute 'normal 0[['
  AssertEqual lnum, line('.')
  unlet lnum
  AssertEqual 3, col('.')

  " X key to revert the update
  AssertExpect '^- ', 2
  execute "normal Xn\<cr>"
  AssertExpect '^- ', 2
  execute "normal Xy\<cr>"
  AssertExpect '^- ', 1

  " q will only close preview window
  normal q

  " We no longer have preview window
  silent! wincmd P
  AssertEqual 0, &previewwindow

  " And we're still on main vim-plug window
  AssertEqual 'vim-plug', &filetype
  normal q

  " q should not close preview window if it's already open
  pedit
  PlugDiff
  AssertExpect '^- ', 1
  execute "normal ]]j\<cr>"
  normal q

  silent! wincmd P
  AssertEqual 1, &previewwindow
  pclose

  unlet g:plug_window g:plug_pwindow

Execute (Test g:plug_pwindow):
  let g:plug_pwindow = 'below 5new'
  PlugDiff
  AssertExpect '^- ', 1
  execute "normal ]]jo"

  AssertEqual 0, &previewwindow
  AssertEqual 1, winnr()
  wincmd P
  AssertEqual 1, &previewwindow
  AssertEqual 2, winnr()
  AssertEqual 5, winheight('.')
  wincmd p

  " Close preview window
  normal q

  " Close main window
  normal q
  unlet g:plug_pwindow

Execute (#572 - Commit preview should work with non-POSIX-compliant &shell):
  " Invalid shell
  let shell = &shell
  set shell=shellfish

  try
    " Preview commit should still work
    PlugDiff
    execute "normal ]]jo"
    wincmd P
    Log getline(1, '$')
    Assert getline(1) =~ 'commit', 'Preview window is empty'
    AssertEqual 'shellfish', &shell
  finally
    " Restore &shell
    let &shell = shell
    unlet shell
    pclose
    q
  endtry

Execute (Reuse Plug window in another tab):
  let tabnr = tabpagenr()
  PlugDiff
  tab new new-tab
  set buftype=nofile
  PlugUpdate
  normal D
  AssertExpect '^- ', 1
  normal q
  AssertEqual tabnr, tabpagenr()
  normal! gt
  q
  unlet tabnr

Execute (contd. PlugDiff should not show inverted history):
  " Additional PlugUpdate to clear diff
  PlugUpdate
  PlugDiff
  Log getline(1, '$')

  " Checking out older revisions
  for repo in values(g:plugs)
    call system(printf('cd %s && git reset HEAD^ --hard', shellescape(repo.dir)))
  endfor
  unlet repo

  " PlugDiff should not report the changes i.e. git log --left-only
  PlugDiff
  Log getline(1, '$')
  AssertEqual '0 plugin(s) updated.', getline(1)
  q

**********************************************************************
~ PlugDiff to see the pending changes
**********************************************************************

Execute (PlugDiff):
  call plug#begin()
  call plug#end()
  PlugClean!

  call plug#begin()
  Plug 'file://'.expand('$PLUG_FIXTURES').'/xxx'
  Plug 'file://'.expand('$PLUG_FIXTURES').'/yyy'
  call plug#end()
  PlugInstall
  Log getline(1, '$')

  call system('cd "$PLUG_FIXTURES/xxx" && git commit --allow-empty -m update-xxx && git tag -f xxx')
  call system('cd "$PLUG_FIXTURES/yyy" && git tag -f yyy && git commit --allow-empty -m update-yyy && git tag -f zzz')

  let g:plugs.yyy.tag = 'yyy'
  PlugUpdate
  Log getline(1, '$')

  PlugDiff
  " 1 plugin(s) updated. 1 plugin(s) have pending updates.
  " [==]
  "
  " Last update:
  " ------------
  "
  " - xxx:
  "   166cfff (tag: xxx) update-xxx (1 second ago)
  "
  " Pending updates:
  " ----------------
  "
  " - yyy: (tag: yyy)
  "   c0a064b (tag: zzz) update-yyy (1 second ago)
  "
  Log getline(1, '$')
  AssertEqual 15, line('$')
  AssertEqual '1 plugin(s) updated. 1 plugin(s) have pending updates.', getline(1)
  AssertEqual '[==]', getline(2)
  AssertEqual '- yyy: (tag: yyy)', getline(13)
  Assert getline(8) =~ '(tag: xxx)'
  Assert getline(14) =~ '(tag: zzz)'
  Assert !empty(mapcheck('o'))
  Assert !empty(mapcheck('X'))
  Assert !empty(mapcheck("\<cr>"))
  q

Execute (Do not show diff for commits outside of rtp):
  call plug#begin()
  call plug#end()
  PlugClean!

  call plug#begin()
  Plug 'file://'.expand('$PLUG_FIXTURES').'/xxx'
  Plug 'file://'.expand('$PLUG_FIXTURES').'/yyy', { 'rtp': 'rtp' }
  call plug#end()
  PlugInstall
  Log getline(1, '$')

  call system('cd "$PLUG_FIXTURES/xxx" && git commit --allow-empty -m update-xxx && git tag -f xxx')
  call system('cd "$PLUG_FIXTURES/yyy" && git commit --allow-empty -m update-yyy && git tag -f yyy')

  let g:plugs.yyy.tag = 'yyy'
  PlugUpdate
  Log getline(1, '$')

  PlugDiff
  " 1 plugin(s) updated.
  " [==]
  "
  " Last update:
  " ------------
  "
  " - xxx:
  "   * 7faa9b2 update-xxx (0 seconds ago)
  "
  " Pending updates:
  " ----------------
  "
  " N/A
  "
  Log getline(1, '$')
  AssertEqual 14, line('$')
  AssertEqual '1 plugin(s) updated.', getline(1)
  AssertEqual '[==]', getline(2)
  AssertEqual 'Last update:', getline(4)
  AssertEqual '- xxx:', getline(7)
  Assert !empty(mapcheck('o'))
  Assert !empty(mapcheck('X'))
  Assert !empty(mapcheck("\<cr>"))
  q

**********************************************************************
~ On-demand loading / Partial installation/update ~
**********************************************************************

Execute (Trying to execute on-demand commands when plugin is not installed):
  call ReloadPlug()
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'on': ['EasyAlign', 'LiveEasyAlign!'] }
  call plug#end()

  Assert exists(':EasyAlign')
  Assert exists(':LiveEasyAlign')
  AssertThrows EasyAlign
  AssertThrows LiveEasyAlign
  Assert !exists(':EasyAlign')
  Assert !exists(':LiveEasyAlign')

Execute (New set of plugins):
  call ReloadPlug()
  call plug#begin()
  Plug 'junegunn/vim-fnr'
  Plug 'junegunn/vim-pseudocl'
  Plug 'junegunn/vim-easy-align', { 'on': 'EasyAlign' }
  Plug 'junegunn/vim-redis',      { 'for': 'redis' }
  let user_autocmd = {}
  autocmd! User vim-fnr let user_autocmd.fnr = 1
  autocmd! User vim-easy-align let user_autocmd.easy_align = 1
  autocmd! User vim-redis let user_autocmd.redis = 1
  call plug#end()

Execute (Check commands):
  Assert !exists(':FNR'),          'FNR command should not be found'
  Assert !exists(':RedisExecute'), 'RedisExecute command should not be found'
  Assert empty(user_autocmd)

Execute (Partial PlugInstall):
  PlugInstall vim-fnr vim-easy-align
  AssertExpect 'vim-fnr', 1
  q

  PlugInstall vim-fnr vim-easy-align 1
  AssertExpect 'vim-fnr', 1
  AssertExpect 'vim-easy-align', 1
  AssertEqual g:first_rtp, split(&rtp, ',')[0]
  AssertEqual g:last_rtp, split(&rtp, ',')[-1]
  q

Given (Unaligned code):
  a=1
  aa=2

Execute (Check installed plugins):
  call EnsureLoaded()
  Assert exists(':FNR'),           'FNR command should be found'
  Assert !exists(':RedisExecute'), 'RedisExecute command still should not be found'

  Assert exists(':EasyAlign'), 'EasyAlign command should be found'
  %EasyAlign=

Expect (Aligned code):
  a  = 1
  aa = 2

Then (autocmd executed):
  Assert user_autocmd.easy_align
  AssertEqual 1, len(user_autocmd)

Given:
Execute (Partial PlugUpdate):
  PlugUpdate vim-redis
  q

Execute (On-demand loading based on filetypes):
  Assert !exists(':RedisExecute'), 'RedisExecute command still should not be found'
  set ft=redis
  Assert exists(':RedisExecute'), 'RedisExecute command is now found'
  Assert user_autocmd.redis
  AssertEqual 2, len(user_autocmd)

  autocmd! User
  unlet user_autocmd

**********************************************************************
~ Local (unmanaged) plugins
**********************************************************************

Execute (Add unmanaged plugin):
  let fzf = expand('$PLUG_FIXTURES/fzf')
  call RmRf(fzf)
  Log fzf

  call plug#begin()
  Plug fzf, { 'on': 'SomeCommand' }
  call plug#end()

  " Check uri field
  Assert !has_key(g:plugs.fzf, 'uri'), 'Should not have uri field'

  " Check dir field
  AssertEqual fzf.'/', g:plugs.fzf.dir

  " Trailing slashes and backslashes should be stripped
  for suffix in ['///', '/\/\/']
    call plug#begin()
    Plug fzf.suffix, { 'on': 'SomeCommand' }
    call plug#end()

    " Check dir field
    AssertEqual fzf.'/', g:plugs.fzf.dir
  endfor

Execute (Plug block for following tests):
  call plug#begin()
  Plug 'junegunn/vim-easy-align'
  Plug fzf, { 'on': 'SomeCommand' }
  call plug#end()
  " Remove plugins from previous tests
  PlugClean!
  q

Execute (PlugInstall will only install vim-easy-align):
  PlugInstall
  Log getline(1, '$')
  AssertExpect 'fzf', 0
  q

Execute (PlugUpdate will only update vim-easy-align):
  PlugUpdate
  Log getline(1, '$')
  AssertExpect 'fzf', 0
  q

Execute (PlugClean should not care about unmanaged plugins):
  PlugClean
  Log getline(1, '$')
  AssertExpect 'fzf', 0
  q

Execute (PlugStatus should point out that the plugin is missing):
  PlugStatus
  Log getline(1, '$')
  AssertExpect 'x fzf', 1
  AssertExpect 'Not found', 1
  q

Execute (Deploy unmanaged plugin):
  Assert !exists(':FZF'), ':FZF command should not exist'
  call RmRf(fzf)
  Log system(printf('cp -r "/tmp/vim-plug-test/fzf" "%s"', fzf))

Execute (PlugUpdate still should not care):
  PlugUpdate
  Log getline(1, '$')
  AssertExpect 'fzf', 0
  q

Execute (PlugStatus with no error):
  PlugStatus
  Log getline(1, '$')
  AssertExpect 'x fzf', 0
  AssertExpect 'Not found', 0
  q

Execute (Check &rtp after SomeCommand):
  Log &rtp
  Assert &rtp !~ 'fzf'
  silent! SomeCommand
  Assert &rtp =~ 'fzf'
  AssertEqual g:first_rtp, split(&rtp, ',')[0]
  AssertEqual g:last_rtp, split(&rtp, ',')[-1]

Execute (PlugClean should not care about frozen plugins):
  call plug#begin()
  Plug 'xxx/vim-easy-align', { 'frozen': 1 }
  call plug#end()
  PlugClean
  AssertExpect 'Already clean', 1
  q

Execute (Common parent):
  call plug#begin()
  Plug 'junegunn/vim-pseudocl'
  Plug 'junegunn/vim-fnr'
  Plug 'junegunn/vim-oblique'
  call plug#end()

  PlugInstall
  Log getline(1, '$')
  AssertExpect! '[===]', 1
  q

  unlet fzf

**********************************************************************
~ Frozen plugins
**********************************************************************
- We've decided to install plugins that are frozen: see #113
Execute (Frozen plugin are not ~~installed nor~~ updated):
  " Remove plugins
  call plug#begin()
  call plug#end()
  PlugClean!
  q

  " vim-easy-align is not found, so it will be installed even though it's frozen
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'frozen': 1 }
  call plug#end()
  PlugInstall
  AssertEqual 1, len(filter(getline(1, '$'), 'v:val =~ "vim-easy-align"'))
  q

  " Remove plugins again
  call plug#begin()
  call plug#end()
  PlugClean!
  q

  " PlugUpdate will do the same
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'frozen': 1 }
  call plug#end()
  PlugInstall
  AssertEqual 1, len(filter(getline(1, '$'), 'v:val =~ "vim-easy-align"'))
  q

  " Since vim-easy-align already exists, PlugInstall or PlugUpdate will skip it
  redir => out
  silent PlugInstall
  redir END
  Assert out =~ 'No plugin to install'

  redir => out
  silent PlugUpdate
  redir END
  Assert out =~ 'No plugin to update'

Execute (But you can still install it if the name is given as the argument):
  PlugInstall vim-easy-align
  Log getline(1, '$')
  AssertEqual 1, len(filter(getline(1, '$'), 'v:val =~ "vim-easy-align"'))
  q

  PlugUpdate vim-easy-align
  Log getline(1, '$')
  AssertEqual 1, len(filter(getline(1, '$'), 'v:val =~ "vim-easy-align"'))
  q

**********************************************************************
~ Retry
**********************************************************************

Execute (Retry failed tasks):
  call plug#begin()
  Plug 'junegunn/vim-easy-align'
  Plug 'junegunn/aaaaaaaaaaaaaa'
  call plug#end()

  PlugInstall
  Log getline(1, '$')
  AssertExpect 'x aaa', 1
  AssertExpect '- vim-easy-align', 1
  normal R
  Log getline(1, '$')
  AssertExpect 'x aaa', 1
  AssertExpect '- vim-easy-align', 0
  AssertExpect! '[x]', 1
  q

  call plug#begin()
  Plug 'junegunn/vim-easy-align'
  Plug 'junegunn/aaaaaaaaaaaaaa'
  Plug 'junegunn/bbbbbbbbbbbbbb'
  Plug 'junegunn/cccccccccccccc'
  call plug#end()

  " Ruby installer
  PlugUpdate
  normal R
  AssertExpect '- vim-easy-align', 0
  AssertExpect! '[xxx]', 1
  q

  " Vim installer
  PlugUpdate 1
  normal R
  AssertExpect '- vim-easy-align', 0
  AssertExpect! '[xxx]', 1
  q

**********************************************************************
~ Post-update hook (`do` option)
**********************************************************************

Execute (Cleanup):
  call plug#begin()
  call plug#end()
  PlugClean!
  q

Execute (On install):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': 'touch installed' }
  Plug 'junegunn/vim-pseudocl'
  Plug 'junegunn/seoul256.vim'
  Plug 'junegunn/goyo.vim'
  Plug 'yous/subsubmodule'
  call plug#end()

  silent PlugInstall
  q

  Assert filereadable(g:plugs['vim-easy-align'].dir.'/installed'),
    \ 'vim-easy-align/installed should exist'
  Assert !filereadable(g:plugs['vim-pseudocl'].dir.'/installed'),
    \ 'vim-pseudocl/installed should not exist'
  AssertEqual ' ', system('cd '.g:plugs['subsubmodule'].dir.' && git submodule status')[0],
    \ 'subsubmodule/subsubmodule should be initialized'

Execute (On update):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': 'touch updated' }
  Plug 'junegunn/vim-pseudocl', { 'do': 'touch updated' }
  Plug 'junegunn/seoul256.vim'
  Plug 'junegunn/goyo.vim'
  Plug 'yous/subsubmodule'
  call plug#end()

  " New commits on remote
  call system('cd /tmp/vim-plug-test/junegunn/vim-pseudocl && git commit --allow-empty -m "update"')

  silent PlugUpdate
  Log getline(1, '$')
  q

  Assert !filereadable(g:plugs['vim-easy-align'].dir.'/updated'),
    \ 'vim-easy-align/updated should not exist'
  Assert filereadable(g:plugs['vim-pseudocl'].dir.'/updated'),
    \ 'vim-pseudocl/updated should exist'

Execute (When already installed):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': 'touch installed2' }
  Plug 'junegunn/vim-pseudocl', { 'commit': '7f8cd78' }
  Plug 'junegunn/seoul256.vim', { 'branch': 'no-t_co' }
  Plug 'junegunn/goyo.vim', { 'tag': '1.5.3' }
  Plug 'yous/subsubmodule'
  call plug#end()

  PlugInstall
  q
  Assert !filereadable(g:plugs['vim-easy-align'].dir.'/installed2'),
    \ 'vim-easy-align/installed2 should not exist'
  AssertNotEqual '7f8cd78cb1fe52185b98b16a3749811f0cc508af', GitCommit('vim-pseudocl')
  AssertNotEqual 'no-t_co', GitBranch('seoul256.vim')
  AssertNotEqual '1.5.3', GitTag('goyo.vim')

Execute (PlugInstall!):
  silent PlugInstall!
  q
  Assert filereadable(g:plugs['vim-easy-align'].dir.'/installed2'),
    \ 'vim-easy-align/installed2 should exist'
  AssertEqual '7f8cd78cb1fe52185b98b16a3749811f0cc508af', GitCommit('vim-pseudocl')
  " Was updated to the default branch of origin by previous PlugUpdate
  AssertEqual 'master', GitBranch('seoul256.vim')
  AssertEqual '1.5.3', GitTag('goyo.vim')

Execute (When submodules are not initialized):
  call system(printf('cd %s && git submodule deinit subsubmodule', g:plugs['subsubmodule'].dir))

  silent PlugInstall!
  q

  AssertEqual ' ', system(printf('cd %s && git submodule status', g:plugs['subsubmodule'].dir))[0],
    \ 'subsubmodule/subsubmodule should be initialized'

Execute (When already updated):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': 'touch updated2' }
  Plug 'junegunn/vim-pseudocl', { 'commit': 'dd507ca' }
  Plug 'junegunn/seoul256.vim', { 'branch': 'master' }
  Plug 'junegunn/goyo.vim', { 'tag': '1.6.0' }
  Plug 'yous/subsubmodule'
  call plug#end()

  PlugUpdate
  q
  Assert !filereadable(g:plugs['vim-easy-align'].dir.'/updated2'),
    \ 'vim-easy-align/updated2 should not exist'
  AssertEqual 'dd507ca0d5f3fdf0d522558cc5ecffdabf824469', GitCommit('vim-pseudocl')
  AssertEqual 'master', GitBranch('seoul256.vim')
  AssertEqual '1.6.0', GitTag('goyo.vim')

Execute (PlugUpdate!):
  silent PlugUpdate!
  q
  Assert filereadable(g:plugs['vim-easy-align'].dir.'/updated2'),
    \ 'vim-easy-align/updated2 should exist'

Execute (When submodules are not initialized):
  call system(printf('cd %s && git submodule deinit subsubmodule', g:plugs['subsubmodule'].dir))

^ #481 submodule update should use standard shell
  let sh = &shell
  set sh=/bin/echo
  silent PlugUpdate!
  let &shell = sh
  unlet sh
  q
  AssertEqual ' ', system(printf('cd %s && git submodule status', g:plugs['subsubmodule'].dir))[0],
    \ 'subsubmodule/subsubmodule should be initialized'

Execute (Using Funcref):
  function! PlugUpdated(info)
    call system('touch '. a:info.name . a:info.status . a:info.force . len(a:info))
  endfunction

  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': function('PlugUpdated') }
  Plug 'junegunn/vim-pseudocl',   { 'do': function('PlugUpdated') }
  call plug#end()

  call system('cd /tmp/vim-plug-test/junegunn/vim-easy-align && git commit --allow-empty -m "update"')
  call system('cd '.g:plugs['vim-easy-align'].dir.' && git reset --hard HEAD^')
  call RmRf(g:plugs['vim-pseudocl'].dir)

  PlugUpdate
  Log getline(1, '$')
  q
  Assert filereadable(g:plugs['vim-easy-align'].dir.'/vim-easy-alignupdated03'),
    \ 'vim-easy-align/vim-easy-alignupdated03 should exist'
  Assert filereadable(g:plugs['vim-pseudocl'].dir.'/vim-pseudoclinstalled03'),
    \ 'vim-pseudocl/vim-pseudoclinstalled03 should exist'

  call RmRf(g:plugs['vim-pseudocl'].dir)
  PlugInstall!
  q
  Assert filereadable(g:plugs['vim-easy-align'].dir.'/vim-easy-alignunchanged13'),
    \ 'vim-easy-align/vim-easy-alignunchanged13 should exist'
  Assert filereadable(g:plugs['vim-pseudocl'].dir.'/vim-pseudoclinstalled13'),
    \ 'vim-pseudocl/vim-pseudoclinstalled13 should exist'

  call system('cd '.g:plugs['vim-easy-align'].dir.' && git reset --hard HEAD^')
  PlugUpdate!
  q
  Assert filereadable(g:plugs['vim-easy-align'].dir.'/vim-easy-alignupdated13'),
    \ 'vim-easy-align/vim-easy-alignupdated13 should exist'
  Assert filereadable(g:plugs['vim-pseudocl'].dir.'/vim-pseudoclunchanged13'),
    \ 'vim-pseudocl/vim-pseudoclunchanged13 should exist'

Execute (Post-update hook output; success and failure):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': 'xxx-non-existent-command-xxx' }
  Plug 'junegunn/vim-pseudocl',   { 'do': 'true' }
  call plug#end()

  silent PlugInstall! 1
  AssertEqual '- Post-update hook for vim-pseudocl ... OK', getline(5)
  AssertEqual 'x Post-update hook for vim-easy-align ... Exit status: 127', getline(6)
  q

Execute (Post-update hook output; invalid type or funcref):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': ':echo 1' }
  Plug 'junegunn/vim-pseudocl',   { 'do': function('call') }
  call plug#end()
  let g:plugs['vim-easy-align'].do = 1

  silent PlugInstall! 1
  AssertEqual 'x Post-update hook for vim-pseudocl ... Vim(call):E119: Not enough arguments for function: call', getline(5)
  AssertEqual 'x Post-update hook for vim-easy-align ... Invalid hook type', getline(6)
  q

Execute (Should not run when failed to update):
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'do': 'touch failed'     }
  Plug 'junegunn/vim-pseudocl',   { 'do': 'touch not-failed' }
  call plug#end()

  " Invalid remote URL
  call system(printf('cd %s && git remote set-url origin xxx', g:plugs['vim-easy-align'].dir))

  " New commits on remote
  call system('cd /tmp/vim-plug-test/junegunn/vim-easy-align && git commit --allow-empty -m "update"')
  call system('cd /tmp/vim-plug-test/junegunn/vim-pseudocl && git commit --allow-empty -m "update"')

  silent PlugUpdate
  Log getline(1, '$')
  q

  Assert !filereadable(g:plugs['vim-easy-align'].dir.'/failed'),
    \ 'vim-easy-align/failed should not exist'
  Assert filereadable(g:plugs['vim-pseudocl'].dir.'/not-failed'),
    \ 'vim-pseudocl/not-failed should exist'

Execute (Vim command with : prefix):
  call plug#begin()
  Plug 'junegunn/vim-pseudocl', { 'do': ':call setline(2, 12345)' }
  call plug#end()

  PlugInstall!
  Log getline(1, '$')
  AssertEqual '12345', getline(2)
  q

Execute (Vim command with : prefix closing the window):
  call plug#begin()
  Plug 'junegunn/vim-pseudocl', { 'do': ':close' }
  call plug#end()

  redir => out
  PlugInstall!
  redir END
  Assert out =~ 'vim-plug was terminated'
  Assert out =~ 'of vim-pseudocl'

Execute (Invalid vim command in post-update hook):
  call plug#begin()
  Plug 'junegunn/vim-pseudocl', { 'do': ':nosuchcommand' }
  call plug#end()

  PlugInstall!
  Log getline(1, '$')
  AssertExpect! 'x Post-update hook for vim-pseudocl ... Vim:E492: Not an editor command: nosuchcommand', 1
  q

**********************************************************************
~ Overriding `dir`
**********************************************************************

Execute (Using custom dir):
  call plug#begin()
  Plug 'junegunn/vim-easy-align'
  call plug#end()
  Assert isdirectory(g:plugs['vim-easy-align'].dir)

  call RmRf('/tmp/vim-plug-test/easy-align')
  call plug#begin()
  Plug 'junegunn/vim-easy-align', { 'dir': '/tmp/vim-plug-test/easy-align' }
  call plug#end()
  AssertEqual '/tmp/vim-plug-test/easy-align/', g:plugs['vim-easy-align'].dir

  PlugClean!
  Assert !isdirectory(g:plugs['vim-easy-align'].dir)
  q

  PlugInstall
  q
  Assert isdirectory(g:plugs['vim-easy-align'].dir)

**********************************************************************
~ On-demand loading load order
**********************************************************************
Before (Clear global vars):
  let g:xxx = []
  set rtp-=$PLUG_FIXTURES/xxx/
  set rtp-=$PLUG_FIXTURES/xxx/after

Execute (Immediate loading):
  call ReloadPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx'
  call plug#end()

  " FIXME:
  " Different result when Vader is run from commandline with `-c` option
  Log g:xxx
  if has('vim_starting')
    AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect'], g:xxx
  else
    AssertEqual ['xxx/plugin', 'xxx/after/plugin', 'xxx/ftdetect', 'xxx/after/ftdetect'], g:xxx
  endif

Execute (Command-based on-demand loading):
  call ReloadPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'on': 'XXX' }
  call plug#end()

  AssertEqual [], g:xxx

  silent! XXX
  AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect', 'xxx/plugin', 'xxx/after/plugin'], g:xxx

  setf xxx
  AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect', 'xxx/plugin', 'xxx/after/plugin', 'xxx/ftplugin', 'xxx/after/ftplugin', 'xxx/indent', 'xxx/after/indent', 'xxx/syntax', 'xxx/after/syntax'], g:xxx

Execute (Filetype-based on-demand loading):
  call ReloadPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'for': 'xxx' }
  Plug '$PLUG_FIXTURES/yyy', { 'for': 'yyy' }
  call plug#end()

  AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect'], g:xxx

  setf xxx
  AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect', 'xxx/plugin', 'xxx/after/plugin', 'xxx/syntax', 'xxx/after/syntax', 'xxx/ftplugin', 'xxx/after/ftplugin', 'xxx/indent', 'xxx/after/indent'], g:xxx

  " syntax/xxx.vim and after/syntax/xxx.vim should not be loaded (#410)
  setf yyy
  AssertEqual ['yyy/ftdetect', 'yyy/after/ftdetect', 'yyy/plugin', 'yyy/after/plugin'], g:yyy

Before:

**********************************************************************
~ plug#helptags()
**********************************************************************

Execute (plug#helptags):
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx'
  Plug '$PLUG_FIXTURES/yyy', { 'rtp': 'rtp' }
  call plug#end()
  silent! call delete(expand('$PLUG_FIXTURES/xxx/doc/tags'))
  silent! call delete(expand('$PLUG_FIXTURES/yyy/rtp/doc/tags'))
  Assert !filereadable(expand('$PLUG_FIXTURES/xxx/doc/tags'))
  Assert !filereadable(expand('$PLUG_FIXTURES/yyy/rtp/doc/tags'))
  AssertEqual 1, plug#helptags()
  Assert filereadable(expand('$PLUG_FIXTURES/xxx/doc/tags'))
  Assert filereadable(expand('$PLUG_FIXTURES/yyy/rtp/doc/tags'))

**********************************************************************
~ Manual loading
**********************************************************************

Execute (plug#load - invalid arguments):
  call ResetPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'for': 'xxx' }
  Plug '$PLUG_FIXTURES/yyy', { 'for': 'yyy' }
  call plug#end()
  AssertEqual 0, plug#load()
  AssertEqual 0, plug#load('non-existent-plugin')
  AssertEqual 0, plug#load('non-existent-plugin', 'another-non-existent-plugin')
  AssertEqual 1, plug#load('xxx')
  AssertEqual 0, plug#load('xxx', 'non-existent-plugin')
  AssertEqual 0, plug#load('non-existent-plugin', 'xxx')

Execute (plug#load - list argument (#638)):
  redir => out
  call plug#load(keys(g:plugs))
  redir END
  AssertEqual '', out

Execute (on: []):
  call plug#begin()
  Plug 'junegunn/rust.vim', { 'on': [] }
  call plug#end()
  PlugInstall
  q

Execute (PlugStatus reports (not loaded)):
  PlugStatus
  AssertExpect 'not loaded', 1
  q

Execute (plug#load to load it):
  tabnew test.rs
  " Vader will switch tab to [Vader-workbench] after Log
  " Log &filetype
  AssertEqual 1, plug#load('rust.vim')
  AssertEqual 'rust', &filetype
  q

Execute (PlugStatus should not contain (not loaded)):
  PlugStatus
  AssertExpect 'not loaded', 0
  q

Execute (Load plugin from PlugStatus screen with L key in normal mode):
  call ResetPlug()
  unlet! g:yyy
  call plug#begin()
  Plug '$PLUG_FIXTURES/yyy', { 'on': [] }
  call plug#end()

  PlugStatus
  AssertExpect 'not loaded', 1
  Assert !exists('g:yyy'), 'yyy not loaded'
  /not loaded
  normal L
  AssertExpect 'not loaded', 0
  Assert exists('g:yyy'), 'yyy loaded'
  q

Execute (Load plugin from PlugStatus screen with L key in visual mode):
  call plug#begin()
  Plug '$PLUG_FIXTURES/z1', { 'on':  [] }
  Plug '$PLUG_FIXTURES/z2', { 'for': [] }
  call plug#end()

  PlugStatus
  AssertExpect 'not loaded', 2
  Assert !exists('g:z1'), 'z1 not loaded'
  Assert !exists('g:z2'), 'z2 not loaded'
  normal ggVGL
  AssertExpect 'not loaded', 0
  Assert exists('g:z1'), 'z1 loaded'
  Assert exists('g:z2'), 'z2 loaded'
  q

**********************************************************************
~ g:plug_window
**********************************************************************
Execute (Open plug window in a new tab):
  " Without g:plug_window, plug window is open on the left split
  let tabnr = tabpagenr()
  PlugStatus
  AssertEqual tabnr, tabpagenr()
  AssertEqual 1, winnr()

  " PlugStatus again inside the window should not change the view
  normal S
  AssertEqual tabnr, tabpagenr()
  AssertEqual 1, winnr()
  q

  " Define g:plug_window so that plug window is open in a new tab
  let g:plug_window = 'tabnew'
  PlugStatus
  AssertNotEqual tabnr, tabpagenr()

  " PlugStatus again inside the window should not change the view
  let tabnr = tabpagenr()
  normal S
  AssertEqual tabnr, tabpagenr()
  q
  unlet g:plug_window tabnr

**********************************************************************
~ g:plug_url_format
**********************************************************************
Execute (Using g:plug_url_format):
  let prev_plug_url_format = g:plug_url_format
  call plug#begin()
  let g:plug_url_format = 'git@bitbucket.org:%s.git'
  Plug 'junegunn/seoul256.vim'
  let g:plug_url_format = 'git@bitsocket.org:%s.git'
  Plug 'vim-scripts/beauty256'
  AssertEqual 'git@bitbucket.org:junegunn/seoul256.vim.git', g:plugs['seoul256.vim'].uri
  AssertEqual 'git@bitsocket.org:vim-scripts/beauty256.git', g:plugs['beauty256'].uri
  let g:plug_url_format = prev_plug_url_format

**********************************************************************
~ U
**********************************************************************
Execute (Plug block):
  call plug#begin()
  Plug 'junegunn/vim-easy-align'
  Plug 'junegunn/vim-emoji'
  call plug#end()

Execute (Update plugin with U key in normal mode):
  PlugStatus
  /emoji
  normal U
  Log getline(1, '$')
  AssertExpect 'Updated', 1
  AssertExpect 'vim-emoji', 1
  AssertExpect 'vim-easy-align', 0
  AssertExpect! '[=]', 1

  " From PlugInstall screen
  PlugInstall
  /easy-align
  normal U
  AssertExpect 'Updated', 1
  AssertExpect 'vim-emoji', 0
  AssertExpect 'vim-easy-align', 1
  AssertExpect! '[=]', 1
  q

Execute (Update plugins with U key in visual mode):
  silent! call RmRf(g:plugs['vim-easy-align'].dir)

  PlugStatus
  normal VGU
  Log getline(1, '$')
  AssertExpect 'Updated', 1
  AssertExpect 'vim-emoji', 1
  AssertExpect 'vim-easy-align', 1
  AssertExpect! '[==]', 1

  " From PlugUpdate screen
  normal VGU
  Log getline(1, '$')
  AssertExpect 'Updated', 1
  AssertExpect 'vim-emoji', 1
  AssertExpect 'vim-easy-align', 1
  AssertExpect! '[==]', 1
  q

**********************************************************************
Execute (plug#begin should expand env vars):
  AssertNotEqual '$HOME/.emacs/plugged', expand('$HOME/.emacs/plugged')
  call plug#begin('$HOME/.emacs/plugged')
  AssertEqual expand('$HOME/.emacs/plugged'), g:plug_home

**********************************************************************
Execute (Plug directory with comma):
  call plug#begin(g:temp_plugged . '/p,l,u,g,g,e,d')
  Plug 'junegunn/vim-emoji'
  call plug#end()
  Log &rtp

  PlugInstall
  q
  let found = filter(split(globpath(&rtp, 'README.md'), '\n'), 'v:val =~ ","')
  Log found
  AssertEqual 1, len(found)
  unlet found

**********************************************************************
Execute (Strict load order):
  let g:total_order = []
  call ReloadPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx'
  Plug '$PLUG_FIXTURES/yyy', { 'for': ['xxx'] }
  call plug#end()
  call EnsureLoaded()
  setf xxx
  Log 'Case 1: ' . &rtp
  AssertEqual ['yyy/ftdetect', 'yyy/after/ftdetect', 'xxx/ftdetect', 'xxx/after/ftdetect'], g:total_order[0:3]
  Assert index(g:total_order, 'xxx/plugin') < index(g:total_order, 'yyy/plugin')
  Assert index(g:total_order, 'xxx/after/plugin') < index(g:total_order, 'yyy/after/plugin')
  let len = len(split(&rtp, ','))

  let g:total_order = []
  call ReloadPlug()
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'for': ['xxx'] }
  Plug '$PLUG_FIXTURES/yyy'
  call plug#end()
  call EnsureLoaded()
  set rtp^=manually-prepended
  set rtp+=manually-appended
  setf xxx
  Log 'Case 2: ' . &rtp
  AssertEqual 'manually-prepended', split(&rtp, ',')[3]
  AssertEqual 'manually-appended',  split(&rtp, ',')[-4]
  AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect', 'yyy/ftdetect', 'yyy/after/ftdetect'], g:total_order[0:3]
  Assert index(g:total_order, 'yyy/plugin') < index(g:total_order, 'xxx/plugin')
  Assert index(g:total_order, 'yyy/after/plugin') < index(g:total_order, 'xxx/after/plugin')
  AssertEqual len + 2, len(split(&rtp, ','))

  let g:total_order = []
  call ReloadPlug()
  set rtp^=manually-prepended
  set rtp+=manually-appended
  call plug#begin()
  Plug '$PLUG_FIXTURES/xxx', { 'for': ['xxx'] }
  Plug '$PLUG_FIXTURES/yyy', { 'for': ['xxx'] }
  call plug#end()
  call EnsureLoaded()
  setf xxx
  Log 'Case 3: ' . &rtp
  AssertEqual ['xxx/ftdetect', 'xxx/after/ftdetect', 'yyy/ftdetect', 'yyy/after/ftdetect'], g:total_order[0:3]
  Assert index(g:total_order, 'xxx/plugin') < index(g:total_order, 'yyy/plugin')
  Assert index(g:total_order, 'xxx/after/plugin') < index(g:total_order, 'yyy/after/plugin')
  AssertEqual len + 2, len(split(&rtp, ','))

**********************************************************************
Execute (PlugClean should not try to remove unmanaged plugins inside g:plug_home):
  call plug#begin('$PLUG_FIXTURES')
  Plug '$PLUG_FIXTURES/ftplugin-msg', { 'for': [] }
  Plug '$PLUG_FIXTURES/fzf'
  Plug '$PLUG_FIXTURES/xxx'
  Plug '$PLUG_FIXTURES/yyy'
  Plug '$PLUG_FIXTURES/cant-delete'
  call plug#end()

  " Remove z1, z2
  PlugClean!
  AssertExpect '^\~ ', 2
  AssertExpect 'Already clean', 0

  PlugClean!
  AssertExpect '^\~ ', 0
  AssertExpect 'Already clean', 1
  q

**********************************************************************
Execute (PlugSnapshot / #154 issues with paths containing spaces):
  let $TMPDIR = '/tmp'
  call plug#begin('$TMPDIR/plug with spaces')
  Plug 'junegunn/vim-easy-align'
  Plug 'junegunn/seoul256.vim'
  call plug#end()

  PlugClean!
  PlugInstall
  call plug#load('vim-easy-align') " Should properly handle paths with spaces
  PlugSnapshot
  AssertEqual '" Generated by vim-plug', getline(1)
  AssertEqual 0, stridx(getline(6), "silent! let g:plugs['seoul256.vim'].commit = '")
  AssertEqual 0, stridx(getline(7), "silent! let g:plugs['vim-easy-align'].commit = '")
  AssertEqual 'vim', &filetype

  call delete(g:plug_home.'/snapshot.vim')
  execute 'PlugSnapshot' escape(g:plug_home.'/snapshot.vim', ' ')
  AssertEqual 'vim', &filetype
  AssertEqual 'snapshot.vim', fnamemodify(expand('%'), ':t')
  q

Execute(PlugSnapshot! to overwrite existing file):
  call writefile(['foobar'], g:plug_home.'/snapshot.vim')
  AssertEqual 'foobar', readfile(g:plug_home.'/snapshot.vim')[0]
  execute 'PlugSnapshot!' escape(g:plug_home.'/snapshot.vim', ' ')
  AssertEqual '" Generated by vim-plug', readfile(g:plug_home.'/snapshot.vim')[0]
  q

**********************************************************************
Execute (#221 Shallow-clone and tag option):
  call plug#begin(g:temp_plugged)
  Plug 'junegunn/goyo.vim'
  call plug#end()
  PlugInstall

  execute 'cd' g:plugs['goyo.vim'].dir
  Assert len(split(system('git log --oneline'), '\n')) == 1
  Assert filereadable('.git/shallow')

  Plug 'junegunn/goyo.vim', { 'tag': '1.5.3' }
  PlugUpdate
  q

  Assert len(split(system('git log --oneline'), '\n')) > 1
  Assert system('git describe --tag') =~ '^1.5.3'
  Assert !filereadable('.git/shallow')
  cd -

Execute (#221 Shallow-clone disabled by g:plug_shallow = 0):
  call plug#begin(g:temp_plugged)
  call plug#end()
  PlugClean!

  let g:plug_shallow = 0
  call plug#begin(g:temp_plugged)
  Plug 'junegunn/goyo.vim'
  call plug#end()
  PlugInstall
  q

  execute 'cd' g:plugs['goyo.vim'].dir
  Assert len(split(system('git log --oneline'), '\n')) > 1, 'not shallow'
  Assert !filereadable('.git/shallow'), 'not shallow'
  cd -
  unlet g:plug_shallow

Execute (#221 Shallow-clone disabled by tag):
  call plug#begin(g:temp_plugged)
  call plug#end()
  PlugClean!

  call plug#begin(g:temp_plugged)
  Plug 'junegunn/goyo.vim', { 'tag': '1.5.3' }
  call plug#end()
  Assert !isdirectory(g:plugs['goyo.vim'].dir)
  PlugInstall
  Assert isdirectory(g:plugs['goyo.vim'].dir)
  q

  execute 'cd' g:plugs['goyo.vim'].dir
  Assert system('git describe --tag') =~ '^1.5.3'
  Assert len(split(system('git log --oneline'), '\n')) > 1
  Assert !filereadable('.git/shallow')
  cd -

Execute (Commit hash support):
  " Get goyo back to master
  call plug#begin(g:temp_plugged)
  Plug 'junegunn/goyo.vim'
  call plug#end()
  PlugUpdate

  call plug#begin(g:temp_plugged)
  Plug 'junegunn/goyo.vim',  { 'commit': 'ffffffff' }
  Plug 'junegunn/vim-emoji', { 'commit': '9db7fcfee0d90dafdbcb7a32090c0a9085eb054a' }
  call plug#end()
  PlugUpdate
  Log getline(1, '$')
  AssertEqual 'x goyo.vim:', getline(5)
  AssertEqual '    fatal: invalid reference: ffffffff', getline(6)
  AssertEqual 0, stridx(getline(7), '- vim-emoji: HEAD is now at 9db7fcf')

  let hash = system(printf('cd %s && git rev-parse HEAD', g:plugs['vim-emoji'].dir))[:-2]
  AssertEqual '9db7fcfee0d90dafdbcb7a32090c0a9085eb054a', hash

  " Validate error formatting
  PlugStatus
  Log getline(1, '$')
  AssertEqual ['Finished. 1 error(s).',
              \'[==]',
              \'',
              \'x goyo.vim:'], getline(1, 4)
  Assert getline(5) =~ '    Invalid HEAD (expected: fffffff, actual: [0-9a-f]\{7})'
  AssertEqual ['    PlugUpdate required.',
              \'- vim-emoji: OK'], getline(6, '$')

  " PlugDiff should show pending updates for vim-emoji
  PlugDiff
  Log getline(1, '$')
  AssertEqual '0 plugin(s) updated. 1 plugin(s) have pending updates.', getline(1)
  Assert !empty(mapcheck('o'))
  Assert empty(mapcheck('X'))
  Assert !empty(mapcheck("\<cr>"))

  " The exact hash values in PlugSnapshot output
  PlugSnapshot
  Log getline(1, '$')
  AssertEqual "silent! let g:plugs['goyo.vim'].commit = 'ffffffff'", getline(6)
  AssertEqual "silent! let g:plugs['vim-emoji'].commit = '9db7fcfee0d90dafdbcb7a32090c0a9085eb054a'", getline(7)
  AssertEqual 10, line('$')
  q

Execute (Commit hash support - cleared):
  call plug#begin(g:temp_plugged)
  Plug 'junegunn/goyo.vim'
  Plug 'junegunn/vim-emoji'
  call plug#end()

  PlugInstall
  let hash = system(printf('cd %s && git rev-parse HEAD', g:plugs['vim-emoji'].dir))[:-2]
  AssertEqual '9db7fcfee0d90dafdbcb7a32090c0a9085eb054a', hash

  PlugUpdate
  let hash = system(printf('cd %s && git rev-parse HEAD', g:plugs['vim-emoji'].dir))[:-2]
  AssertNotEqual '9db7fcfee0d90dafdbcb7a32090c0a9085eb054a', hash
  q

Execute (#371 - 'as' option):
  call plug#begin()
  Plug 'jg/goyo.vim'
  Plug 'junegunn/goyo.vim', {'as': 'yogo'}
  call plug#end()
  AssertEqual ['goyo.vim', 'yogo'], sort(keys(g:plugs))
  Log g:plugs
  Assert g:plugs.yogo.dir =~# '/yogo/$'

  call plug#begin()
  Plug 'junegunn/goyo.vim', {'as': 'yogo', 'dir': '/tmp/vim-plug-test/gogo'}
  call plug#end()
  AssertEqual ['yogo'], sort(keys(g:plugs))
  AssertEqual '/tmp/vim-plug-test/gogo/', g:plugs.yogo.dir

Execute (#427 - Tag option with wildcard (requires git 1.9.2 or above)):
  if str2nr(split(split(system('git --version'))[-1], '\.')[0]) < 2
    Log 'tag with wildcard requires git 1.9.2 or above'
  else
    call plug#begin()
    Plug 'junegunn/vim-easy-align', { 'tag': '2.9.*' }
    call plug#end()
    PlugInstall!
    Log getline(1, '$')
    AssertExpect! '- Latest tag for 2.9.* -> 2.9.7 (vim-easy-align)', 1
    q
    AssertEqual '2.9.7', GitTag('vim-easy-align')
  endif

Execute (#530 - Comparison of compatible git URIs):
  " .git suffix
  Assert CompareURI('https://github.com/junegunn/vim-plug.git', 'https://github.com/junegunn/vim-plug')

  " user@
  Assert CompareURI('https://github.com/junegunn/vim-plug.git', 'https://user@github.com/junegunn/vim-plug.git')

  " git::@
  Assert CompareURI('https://github.com/junegunn/vim-plug.git', 'https://git::@github.com/junegunn/vim-plug.git')

  " https and ssh
  Assert CompareURI('https://github.com/junegunn/vim-plug.git', 'git@github.com:junegunn/vim-plug.git')

  " file://
  Assert CompareURI('file:///tmp/vim-plug', '/tmp/vim-plug')
  Assert CompareURI('file:///tmp/vim-plug', '/tmp/vim-plug/')

Execute (#530 - Comparison of incompatible git URIs):
  " Different hostname
  Assert !CompareURI('https://github.com/junegunn/vim-plug.git', 'https://bitbucket.com/junegunn/vim-plug.git')

  " Different repository
  Assert !CompareURI('https://github.com/junegunn/vim-plug.git', 'https://github.com/junegunn/emacs-plug.git')

  " Different port
  Assert !CompareURI('https://github.com/junegunn/vim-plug.git', 'https://github.com:12345/junegunn/vim-plug.git')

Execute (#532 - Reuse plug window):
  let g:plug_window = 'vertical topleft new'
  let g:plug_pwindow = 'above 12new'
  call plug#begin()
  Plug 'junegunn/goyo.vim'
  call plug#end()
  PlugInstall
  call system(printf('cd "%s" && git commit --allow-empty -m "dummy"', g:plugs['goyo.vim'].dir))

  PlugDiff
  AssertEqual 1, winnr(), 'Current window is #1 after PlugDiff (but is '.winnr().')'
  AssertEqual 2, winnr('$'), 'Two windows after PlugDiff (but got '.winnr('$').')'

  " Open preview window
  execute "normal ]]jo"
  AssertEqual 2, winnr(), 'Current window is #2 after opening preview (but is '.winnr().')'
  AssertEqual 3, winnr('$'), 'Three windows with preview (but got '.winnr('$').')'

  " Move plug window to the right
  wincmd L
  AssertEqual 3, winnr(), 'Current window is #3 after moving window (but is '.winnr().')'
  AssertEqual 3, winnr('$'), 'Three windows after moving window (but got '.winnr('$').')'

  " Reuse plug window. Preview window is closed.
  PlugStatus
  AssertEqual 2, winnr(), 'Current window is #2 after PlugStatus (but is '.winnr().')'
  AssertEqual 2, winnr('$'), 'Three windows after PlugStatus (but got '.winnr('$').')'
  q

  unlet g:plug_window g:plug_pwindow

Execute (#766 - Allow cloning into an empty directory):
  let d = '/tmp/vim-plug-test/goyo-already'
  call system('rm -rf ' . d)
  call mkdir(d)
  call plug#begin()
  Plug 'junegunn/goyo.vim', { 'dir': d }
  call plug#end()
  PlugInstall
  AssertExpect! '[=]', 1
  q
  unlet d

Execute (#982 - PlugClean should report when directories cannot be removed):
  call plug#begin('$PLUG_FIXTURES')
  Plug '$PLUG_FIXTURES/ftplugin-msg', { 'for': [] }
  Plug '$PLUG_FIXTURES/fzf'
  Plug '$PLUG_FIXTURES/xxx'
  Plug '$PLUG_FIXTURES/yyy'
  call plug#end()

  " Fail to remove cant-delete
  PlugClean!
  AssertEqual 'Removed 0 directories. Failed to remove 1 directories.', getline(4)
  AssertExpect '^x ', 1
  q

  " Delete tmp but fail to remove cant-delete
  call mkdir(expand('$PLUG_FIXTURES/tmp'))
  PlugClean!
  AssertEqual 'Removed 1 directories. Failed to remove 1 directories.', getline(4)
  AssertExpect '^x ', 1
  AssertExpect '^\~ ', 1
  q
```

