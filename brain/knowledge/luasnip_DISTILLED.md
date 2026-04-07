---
id: luasnip
type: knowledge
owner: OA_Triage
---
# luasnip
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
> CC=your_compiler_program`. Also, make sure `%GIT%/bin` directory is added in
> the `$PATH` so that `make` can use `%GIT%/bin/sh.exe`.
> 
> On FreeBSD (and/or systems that do not install the GNU make package as the default)
> make commands will fail as the Makefile does not align with the expected syntax of the
> BSD variant of make. The solution is to install the GNU variant of make:
> 'pkg install gmake' on FreeBSD.

## Keymaps
In Vim script, with `<Tab>` for jumping forward/expanding a snippet, `<Shift-Tab>` for
jumping backward, and `<Ctrl-E>` for changing the current choice when in a
`choiceNode`...
```vim
" press <Tab> to expand or jump in a snippet. These can also be mapped separately
" via <Plug>luasnip-expand-snippet and <Plug>luasnip-jump-next.
imap <silent><expr> <Tab> luasnip#expand_or_jumpable() ? '<Plug>luasnip-expand-or-jump' : '<Tab>'
" -1 for jumping backwards.
inoremap <silent> <S-Tab> <cmd>lua require'luasnip'.jump(-1)<Cr>

snoremap <silent> <Tab> <cmd>lua require('luasnip').jump(1)<Cr>
snoremap <silent> <S-Tab> <cmd>lua require('luasnip').jump(-1)<Cr>

" For changing choices in choiceNodes (not strictly necessary for a basic setup).
imap <silent><expr> <C-E> luasnip#choice_active() ? '<Plug>luasnip-next-choice' : '<C-E>'
smap <silent><expr> <C-E> luasnip#choice_active() ? '<Plug>luasnip-next-choice' : '<C-E>'
```

... or in Lua, with a different set of keys: `<Ctrl-K>` for expanding, `<Ctrl-L>`
for jumping forward, `<Ctrl-J>` for jumping backward, and `<Ctrl-E>` for
changing the active choice.

```lua
local ls = require("luasnip")

vim.keymap.set({"i"}, "<C-K>", function() ls.expand() end, {silent = true})
vim.keymap.set({"i", "s"}, "<C-L>", function() ls.jump( 1) end, {silent = true})
vim.keymap.set({"i", "s"}, "<C-J>", function() ls.jump(-1) end, {silent = true})

vim.keymap.set({"i", "s"}, "<C-E>", function()
	if ls.choice_active() then
		ls.change_choice(1)
	end
end, {silent = true})
```

`nvim-cmp`'s wiki also contains [an example](https://github.com/hrsh7th/nvim-cmp/wiki/Example-mappings#luasnip) for
setting up a super-tab-like mapping.

## Add Snippets

Check out [the doc](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#loaders) for a general explanation of the
loaders and their benefits. The following list serves only as a short overview.

- **VS Code-like**: To use existing VS Code style snippets from a plugin (e.g. [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets)) simply install the plugin and then add
    ```lua
    require("luasnip.loaders.from_vscode").lazy_load()
    ```
	somewhere in your Neovim config. LuaSnip will then load the snippets contained in the plugin on startup.
  You can also easily **load your own custom VSCode style snippets** by passing the path to the custom snippet-directory to the load function:
    ```lua
    -- load snippets from path/of/your/nvim/config/my-cool-snippets
    require("luasnip.loaders.from_vscode").lazy_load({ paths = { "./my-cool-snippets" } })
    ```
        > NOTE:
        > It's mandatory to have a `package.json` file in the snippet directory. For examples, see [friendly-snippets](https://github.com/rafamadriz/friendly-snippets/blob/main/package.json).
	For more info on the VS Code loader, check the [examples](https://github.com/L3MON4D3/LuaSnip/blob/b5a72f1fbde545be101fcd10b70bcd51ea4367de/Examples/snippets.lua#L501) or [documentation](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#loaders).

- **SnipMate-like**: Very similar to VS Code packages; install a plugin that provides snippets and call the `load`-function:
    ```lua
    require("luasnip.loaders.from_snipmate").lazy_load()
    ```
    The SnipMate format is very simple, so adding **custom snippets** only requires a few steps:
    - add a directory beside your `init.vim` (or any other place that is in your `runtimepath`) named `snippets`.
    - inside that directory, create files named `<filetype>.snippets` and add snippets for the given filetype in it (for inspiration, check [honza/vim-snippets](https://github.com/honza/vim-snippets/tree/master/snippets)).  
        ```snipmate
        # comment
        snippet <trigger> <description>
        <snippet-body>
        snippet if C-style if
        if ($1)
        	$0
        ```
    Again, there are some [examples](https://github.com/L3MON4D3/LuaSnip/blob/b5a72f1fbde545be101fcd10b70bcd51ea4367de/Examples/snippets.lua#L517) and [documentation](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#snipmate).  
- **Lua**: Add the snippets by calling `require("luasnip").add_snippets(filetype, snippets)`. An example for this can be found [here](https://github.com/L3MON4D3/LuaSnip/blob/master/Examples/snippets.lua#L190).  
This can also be done much cleaner, with all the benefits that come with using a loader, by using the [loader for Lua](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#lua)

There's also a repository collecting snippets for various languages, [molleweide/LuaSnip-snippets.nvim](https://github.com/molleweide/LuaSnip-snippets.nvim)

## Documentation

### Getting started

You have two main choices: use SnipMate/VS Code snippets (easier) or write snippets in Lua (more complex but also more feature-rich).
Here are some suggestions for getting started in either case:

* **SnipMate or VS Code snippets**: if you only want to write/load SnipMate or VS Code snippets and ignore Lua snippets (and this is definitely recommended if you don't yet need Lua snippets' more complicated features), check out the sections on loading [VS Code](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#vscode) or [SnipMate](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#snipmate) packages in `DOC.md`.
  Of those two, SnipMate is definitely the more comfortable way of writing snippets.
* **Lua snippets**: we suggest first watching or reading one of the introductory guides in the [Resources for new users](#resources-for-new-users) section below.
  After getting familiar with the basics, you should check out the important LuaSnip features in the following list:
  * [`config`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#config-options): Notable: `region_check_events` for jumping to the end of snippets the cursor is no longer inside of,
    `delete_check_events` for cleaning up snippets whose text was deleted,
    and `enable_autosnippets` to enable automatic snippet expansion.
  * [`extras`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#extras): This module contains many functions that make writing snippets
    significantly easier;
    `fmt` and `lambda` are especially useful.
  * [`lua-loader`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#lua):
    A very useful way to load snippets, more comfortable than calling `add_snippets`.  
    Also supports hot reload (limited to buffers in the same Neovim instance as the edited file) and [jumping to the files that provide snippets to the
    current buffer](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#edit_snippets).
  * Advanced nodes:
    [`functionNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#functionnode),
    [`dynamicNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#dynamicnode),
    [`choiceNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#choicenode) and [`restoreNode`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#restorenode).  
    Instead of reading about them in the doc, the first three are explained very
    well in [this video](https://www.youtube.com/watch?v=KtQZRAkgLqo) by TJ
    DeVries.

### Official docs and examples

Note: instead of immediately reading the official documentation, you may want to check out the [Resources for new users](#resources-for-new-users) section below since the docs are written more as a reference manual than as a tutorial for new users.

- [`DOC.md`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md) is the main documentation—it gives an overview of how to write snippets, explains the role and use case of each LuaSnip node, shows how to load snippets from Lua, VS Code, and SnipMate formats, and covers the available LuaSnip API.
- `:help luasnip.txt` is a plain text version of `DOC.md` available with Neovim's `:help` feature.
- The file [`Examples/snippets.lua`](https://github.com/L3MON4D3/LuaSnip/blob/master/Examples/snippets.lua) contains many example snippets written in Lua—we highly recommend looking through (or better yet, `:luafile`ing) these example snippets before using LuaSnip's advanced features.
- The [Wiki](https://github.com/L3MON4D3/LuaSnip/wiki) contains some useful LuaSnip extensions and some examples of advanced snippets and configs.
- Configuration is documented [in `DOC.md`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#config-options) as well.

【中文版】DOC in Chinese is [here](https://zjp-cn.github.io/neovim0.6-blogs/nvim/luasnip/doc1.html).

### Resources for new users
Here are some LuaSnip videos and tutorials on the Web:
- [Introductory](https://www.youtube.com/watch?v=Dn800rlPIho) and [advanced](https://www.youtube.com/watch?v=KtQZRAkgLqo) YouTube videos by the one and only [TJ DeVries](https://github.com/tjdevries). Unfortunately there were some breaking changes in LuaSnip since these videos were recorded:
  * Snippets are now added via [`ls.add_snippets`](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md#adding-snippets) instead of with `ls.snippets = {}`
- A [guide to writing snippets in Lua](https://www.ejmastnak.com/tutorials/vim-latex/luasnip/) with LaTeX-themed GIFs and real-life examples by [@ejmastnak](https://github.com/ejmastnak)
- A [collection of LuaSnip guides](https://evesdropper.dev/files/luasnip) by [@evesdropper](https://github.com/evesdropper), with most of them also in a LaTeX context
- An introductory LuaSnip [video tutorial for beginners](https://www.youtube.com/watch?v=ub0REXjhpmk) by Ziontee113

Inspired by [vsnip.vim](https://github.com/hrsh7th/vim-vsnip/)

```

### File: DOC.md
```md
```
            __                       ____
           /\ \                     /\  _`\           __
           \ \ \      __  __     __ \ \,\L\_\    ___ /\_\  _____
            \ \ \  __/\ \/\ \  /'__`\\/_\__ \  /' _ `\/\ \/\ '__`\
             \ \ \L\ \ \ \_\ \/\ \L\.\_/\ \L\ \/\ \/\ \ \ \ \ \L\ \
              \ \____/\ \____/\ \__/.\_\ `\____\ \_\ \_\ \_\ \ ,__/
               \/___/  \/___/  \/__/\/_/\/_____/\/_/\/_/\/_/\ \ \/
                                                             \ \_\
                                                              \/_/
```

LuaSnip is a snippet engine written entirely in Lua. It has some great
features like inserting text (`luasnip-function-node`) or nodes
(`luasnip-dynamic-node`) based on user input, parsing LSP syntax and switching
nodes (`luasnip-choice-node`).
For basic setup like mappings and installing, check the README.

All code snippets in this help assume the following:

```lua
local ls = require("luasnip")
local s = ls.snippet
local sn = ls.snippet_node
local isn = ls.indent_snippet_node
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node
local c = ls.choice_node
local d = ls.dynamic_node
local r = ls.restore_node
local events = require("luasnip.util.events")
local ai = require("luasnip.nodes.absolute_indexer")
local opt = require("luasnip.nodes.optional_arg")
local extras = require("luasnip.extras")
local l = extras.lambda
local rep = extras.rep
local p = extras.partial
local m = extras.match
local n = extras.nonempty
local dl = extras.dynamic_lambda
local fmt = require("luasnip.extras.fmt").fmt
local fmta = require("luasnip.extras.fmt").fmta
local conds = require("luasnip.extras.expand_conditions")
local postfix = require("luasnip.extras.postfix").postfix
local types = require("luasnip.util.types")
local parse = require("luasnip.util.parser").parse_snippet
local ms = ls.multi_snippet
local k = require("luasnip.nodes.key_indexer").new_key
```

As noted in the [Loaders-Lua](#lua)-section:

> By default, the names from [`luasnip.config.snip_env`][snip-env-src] will be used, but it's possible to customize them by setting `snip_env` in `setup`. 

Furthermore, note that while this document assumes you have defined `ls` to be `require("luasnip")`, it is **not** provided in the default set of variables.

<!-- panvimdoc-ignore-start -->

Note: the source code of snippets in GIFs is actually
[here](https://github.com/zjp-CN/neovim0.6-blogs/commit/2bff84ef53f8da5db9dcf2c3d97edb11b2bf68cd),
and it's slightly different from the code below.

<!-- panvimdoc-ignore-end -->

# Basics
In LuaSnip, snippets are made up of `nodes`. These can contain either

- static text (`textNode`)
- text that can be edited (`insertNode`)
- text that can be generated from the contents of other nodes (`functionNode`)
- other nodes
    - `choiceNode`: allows choosing between two nodes (which might contain more
    nodes)
    - `restoreNode`: store and restore input to nodes
- or nodes that can be generated based on input (`dynamicNode`).

Snippets are always created using the `s(trigger:string, nodes:table)`-function.
It is explained in more detail in [Snippets](#snippets), but the gist is that
it creates a snippet that contains the nodes specified in `nodes`, which will be
inserted into a buffer if the text before the cursor matches `trigger` when
`ls.expand` is called.  

## Jump-Index
Nodes that can be jumped to (`insertNode`, `choiceNode`, `dynamicNode`,
`restoreNode`, `snippetNode`) all require a "jump-index" so LuaSnip knows the
order in which these nodes are supposed to be visited ("jumped to").  

```lua
s("trig", {
	i(1), t"text", i(2), t"text again", i(3)
})
```

These indices don't "run" through the entire snippet, like they do in
TextMate-snippets (`"$1 ${2: $3 $4}"`), they restart at 1 in each nested
snippetNode:
```lua
s("trig", {
	i(1), t" ", sn(2, {
		t" ", i(1), t" ", i(2)
	})
})
```
(roughly equivalent to the given TextMate-snippet).

## Adding Snippets
The snippets for a given filetype have to be added to LuaSnip via
`ls.add_snippets(filetype, snippets)`. Snippets that should be accessible
globally (in all filetypes) have to be added to the special filetype `all`.
```lua
ls.add_snippets("all", {
	s("ternary", {
		-- equivalent to "${1:cond} ? ${2:then} : ${3:else}"
		i(1, "cond"), t(" ? "), i(2, "then"), t(" : "), i(3, "else")
	})
})
```
It is possible to make snippets from one filetype available to another using
`ls.filetype_extend`, more info on that in the section [API](#api-2).

## Snippet Insertion
When a new snippet is expanded, it can be connected with the snippets that have
already been expanded in the buffer in various ways.  
First of all, Luasnip distinguishes between root-snippets and child-snippets.
The latter are nested inside other snippets, so when jumping through a snippet,
one may also traverse the child-snippets expanded inside it, more or less as if
the child just contains more nodes of the parent.  
Root-snippets are of course characterized by not being child-snippets.  
When expanding a new snippet, it becomes a child of the snippet whose region it
is expanded inside, and a root if it is not inside any snippet's region.  
If it is inside another snippet, the specific node it is inside is determined,
and the snippet then nested inside that node.

* If that node is interactive (for example, an `insertNode`), the new snippet
  will be traversed when the node is visited, as long as the
  configuration-option `link_children` is enabled. If it is not enabled, it is
  possible to jump from the snippet to the node, but not the other way around.
* If that node is not interactive, the snippet will be linked to the currently
  active node, also such that it will not be jumped to again once it is left.
  This is to prevent jumping large distances across the buffer as much as
  possible. There may still be one large jump from the snippet back to the
  current node it is nested inside, but that seems hard to avoid.  
  Thus, one should design snippets such that the regions where other snippets
  may be expanded are inside `insertNodes`.

If the snippet is not a child, but a root, it can be linked up with the roots
immediately adjacent to it by enabling `link_roots` in `setup`.
Since by default only one root is remembered, one should also set `keep_roots`
if `link_roots` is enabled. The two are separate options, since roots that are
not linked can still be reached by `ls.activate_node()`. This setup (remember
roots, but don't jump to them) is useful for a super-tab like mapping (`<Tab>`
and jump on the same key), where one would like to still enter previous roots.
Since there would almost always be more jumps if the roots are linked, regular
`<Tab>` would not work almost all the time, and thus `link_roots` has to stay
disabled.

# Node

Every node accepts, as its last parameter, an optional table of arguments.
There are some common ones (which are listed here), and some that only apply to
some nodes (`user_args` for function/dynamicNode). These `opts` are
only mentioned if they accept options that are not common to all nodes.

Common opts:

* `node_ext_opts` and `merge_node_ext_opts`: Control `ext_opts` (most likely
  highlighting) of the node. Described in detail in [ext_opts](#ext_opts)
* `key`: The node can be referred to by this key. Useful for either
  [Key Indexer](#key-indexer) or for finding the node at runtime (See
  [Snippets-API](#snippets-api)), for example inside a `dynamicNode`. The keys
  do not have to be unique across the entire lifetime of the snippet, but at any
  point in time, the snippet may contain each key only once. This means it is
  fine to return a keyed node from a `dynamicNode`, because even if it will be
  generated multiple times, those will not be valid at the same time.
* `node_callbacks`: Define event-callbacks for this node (see
  [events](#events)).  
  Accepts a table that maps an event, e.g. `events.enter` to the callback
  (essentially the same as `callbacks` passed to `s`, only that there is no
  first mapping from jump-index to the table of callbacks).

## API

- `get_jump_index()`: this method returns the jump-index of a node. If a node 
  doesn't have a jump-index, this method returns `nil` instead.
- `get_buf_position(opts) -> {from_position, to_position}`:
  Determines the range of the buffer occupied by this node. `from`- and
  `to_position` are `row,column`-tuples, `0,0`-indexed (first line is 0, first
  column is 0) and end-inclusive (see `:h api-indexing`, this is extmarks
  indexing).
  - `opts`: `table|nil`, options, valid keys are:
    - `raw`: `bool`, default `true`. This can be used to switch between
	  byte-columns (`raw=true`) and visual columns (`raw=false`). This makes a
	  difference if the line contains characters represented by multiple bytes
	  in UTF, for example `ÿ`.

# Snippets

The most direct way to define snippets is `s`:
```lua
s({trig="trigger"}, {})
```
(This snippet is useless beyond serving as a minimal example)

`s(context, nodes, opts) -> snippet`

- `context`: Either table or a string. Passing a string is equivalent to passing

  ```lua
  {
  	trig = context
  }
  ```

  The following keys are valid:
  - `trig`: string, the trigger of the snippet. If the text in front of (to the
    left of) the cursor when `ls.expand()` is called matches it, the snippet
    will be expanded.  
    By default, "matches" means the text in front of the cursor matches the
    trigger exactly, this behavior can be modified through `trigEngine`
  - `name`: string, can be used by e.g. `nvim-compe` to identify the snippet.
  - `desc` (or `dscr`): string, description of the snippet, \n-separated or table
    for multiple lines.
  - `wordTrig`: boolean, if true, the snippet is only expanded if the word
    (`[%w_]+`) before the cursor matches the trigger entirely.
    True by default.
  - `regTrig`: boolean, whether the trigger should be interpreted as a
    Lua pattern. False by default.  
    Consider setting `trigEngine` to `"pattern"` instead, it is more expressive,
    and in line with other settings.
  - `trigEngine`: (function|string), determines how `trig` is interpreted, and
    what it means for it to "match" the text in front of the cursor.  
    This behavior can be completely customized by passing a function, but the
    predefined ones, which are accessible by passing their identifier, should
    suffice in most cases:
    * `"plain"`: the default-behavior, the trigger has to match the text before
      the cursor exactly.
    * `"pattern"`: the trigger is interpreted as a Lua pattern, and is a match if
      `trig .. "$"` matches the line up to the cursor. Capture-groups will be
      accessible as `snippet.captures`.
    * `"ecma"`: the trigger is interpreted as an ECMAscript-regex, and is a
      match if `trig .. "$"` matches the line up to the cursor. Capture-groups
      will be accessible as `snippet.captures`.  
      This `trigEngine` requires `jsregexp` (see
      [LSP-snippets-transformations](#transformations)) to be installed, if it
      is not, this engine will behave like `"plain"`.
    * `"vim"`: the trigger is interpreted as a vim-regex, and is a match if
      `trig .. "$"` matches the line up to the cursor. As with the other
      regex/pattern-engines, captures will be available as `snippet.captures`,
      but there is one caveat: the matching is done using `matchlist`, so for
      now empty-string submatches will be interpreted as unmatched, and the
      corresponding `snippet.capture[i]` will be `nil` (this will most likely
      change, don't rely on this behavior).

    Besides these predefined engines, it is also possible to create new ones:
    Instead of a string, pass a function which satisfies
    `trigEngine(trigger, opts) -> (matcher(line_to_cursor, trigger) ->
    whole_match, captures)`
    (i.e. the function receives `trig` and `trigEngineOpts` can, for example,
    precompile a regex, and then returns a function responsible for determining
    whether the current cursor-position (represented by the line up to the
    cursor) matches the trigger (it is passed again here so engines which don't
    do any trigger-specific work (like compilation) can just return a static
    `matcher`), and what the capture-groups are).  
    The `lua`-engine, for example, can be implemented like this:
    ```lua
    local function matcher(line_to_cursor, trigger)
        -- look for match which ends at the cursor.
        -- put all results into a list, there might be many capture-groups.
        local find_res = { line_to_cursor:find(trigger .. "$") }

        if #find_res > 0 then
            -- if there is a match, determine matching string, and the
            -- capture-groups.
            local captures = {}
            -- find_res[1] is `from`, find_res[2] is `to` (which we already know
            -- anyway).
            local from = find_res[1]
            local match = line_to_cursor:sub(from, #line_to_cursor)
            -- collect capture-groups.
            for i = 3, #find_res do
                captures[i - 2] = find_res[i]
            end
            return match, captures
        else
            return nil
        end
    end

    local function engine(trigger)
        -- don't do any special work here, can't precompile lua-pattern.
        return matcher
    end
    ```
    The predefined engines are defined in
    [`trig_engines.lua`](https://github.com/L3MON4D3/LuaSnip/blob/master/lua/luasnip/nodes/util/trig_engines.lua),
    read it for more examples.

  - `trigEngineOpts`: `table<string, any>`, options for the used `trigEngine`.  
    The valid options are:
    * `max_len`: number, upper bound on the length of the trigger.  
      If this is set, the `line_to_cursor` will be truncated (from the cursor of
      course) to `max_len` characters before performing the match.  
      This is implemented because feeding long `line_to_cursor` into e.g. the
      pattern-`trigEngine` will hurt performance quite a bit (see issue
      Luasnip#1103).  
      This option is implemented for all `trigEngines`. 

  - `docstring`: string, textual representation of the snippet, specified like
    `desc`. Overrides docstrings loaded from `json`.
  - `docTrig`: string, used as `line_to_cursor` during docstring-generation.
    This might be relevant if the snippet relies on specific values in the
    capture-groups (for example, numbers, which won't work with the default
    `$CAPTURESN` used during docstring-generation)
  - `hidden`: boolean, hint for completion-engines.
    If set, the snippet should not show up when querying snippets.
  - `priority`: positive number, Priority of the snippet, 1000 by default.  
	Snippets with high priority will be matched to a trigger before those with a
	lower one.
    The priority for multiple snippets can also be set in `add_snippets`.
  - `snippetType`: string, should be either `snippet` or `autosnippet` (ATTENTION:

... [TRUNCATED]
```

### File: data\DOC-template.md
```md
```
            __                       ____
           /\ \                     /\  _`\           __
           \ \ \      __  __     __ \ \,\L\_\    ___ /\_\  _____
            \ \ \  __/\ \/\ \  /'__`\\/_\__ \  /' _ `\/\ \/\ '__`\
             \ \ \L\ \ \ \_\ \/\ \L\.\_/\ \L\ \/\ \/\ \ \ \ \ \L\ \
              \ \____/\ \____/\ \__/.\_\ `\____\ \_\ \_\ \_\ \ ,__/
               \/___/  \/___/  \/__/\/_/\/_____/\/_/\/_/\/_/\ \ \/
                                                             \ \_\
                                                              \/_/
```

LuaSnip is a snippet engine written entirely in Lua. It has some great
features like inserting text (`luasnip-function-node`) or nodes
(`luasnip-dynamic-node`) based on user input, parsing LSP syntax and switching
nodes (`luasnip-choice-node`).
For basic setup like mappings and installing, check the README.

All code snippets in this help assume the following:

```lua
local ls = require("luasnip")
local s = ls.snippet
local sn = ls.snippet_node
local isn = ls.indent_snippet_node
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node
local c = ls.choice_node
local d = ls.dynamic_node
local r = ls.restore_node
local events = require("luasnip.util.events")
local ai = require("luasnip.nodes.absolute_indexer")
local opt = require("luasnip.nodes.optional_arg")
local extras = require("luasnip.extras")
local l = extras.lambda
local rep = extras.rep
local p = extras.partial
local m = extras.match
local n = extras.nonempty
local dl = extras.dynamic_lambda
local fmt = require("luasnip.extras.fmt").fmt
local fmta = require("luasnip.extras.fmt").fmta
local conds = require("luasnip.extras.expand_conditions")
local postfix = require("luasnip.extras.postfix").postfix
local types = require("luasnip.util.types")
local parse = require("luasnip.util.parser").parse_snippet
local ms = ls.multi_snippet
local k = require("luasnip.nodes.key_indexer").new_key
```

As noted in the [Loaders-Lua](#lua)-section:

> By default, the names from [`luasnip.config.snip_env`][snip-env-src] will be used, but it's possible to customize them by setting `snip_env` in `setup`. 

Furthermore, note that while this document assumes you have defined `ls` to be `require("luasnip")`, it is **not** provided in the default set of variables.

<!-- panvimdoc-ignore-start -->

Note: the source code of snippets in GIFs is actually
[here](https://github.com/zjp-CN/neovim0.6-blogs/commit/2bff84ef53f8da5db9dcf2c3d97edb11b2bf68cd),
and it's slightly different from the code below.

<!-- panvimdoc-ignore-end -->

# Basics
In LuaSnip, snippets are made up of `nodes`. These can contain either

- static text (`textNode`)
- text that can be edited (`insertNode`)
- text that can be generated from the contents of other nodes (`functionNode`)
- other nodes
    - `choiceNode`: allows choosing between two nodes (which might contain more
    nodes)
    - `restoreNode`: store and restore input to nodes
- or nodes that can be generated based on input (`dynamicNode`).

Snippets are always created using the `s(trigger:string, nodes:table)`-function.
It is explained in more detail in [Snippets](#snippets), but the gist is that
it creates a snippet that contains the nodes specified in `nodes`, which will be
inserted into a buffer if the text before the cursor matches `trigger` when
`ls.expand` is called.  

## Jump-Index
Nodes that can be jumped to (`insertNode`, `choiceNode`, `dynamicNode`,
`restoreNode`, `snippetNode`) all require a "jump-index" so LuaSnip knows the
order in which these nodes are supposed to be visited ("jumped to").  

```lua
s("trig", {
	i(1), t"text", i(2), t"text again", i(3)
})
```

These indices don't "run" through the entire snippet, like they do in
TextMate-snippets (`"$1 ${2: $3 $4}"`), they restart at 1 in each nested
snippetNode:
```lua
s("trig", {
	i(1), t" ", sn(2, {
		t" ", i(1), t" ", i(2)
	})
})
```
(roughly equivalent to the given TextMate-snippet).

## Adding Snippets
The snippets for a given filetype have to be added to LuaSnip via
`ls.add_snippets(filetype, snippets)`. Snippets that should be accessible
globally (in all filetypes) have to be added to the special filetype `all`.
```lua
ls.add_snippets("all", {
	s("ternary", {
		-- equivalent to "${1:cond} ? ${2:then} : ${3:else}"
		i(1, "cond"), t(" ? "), i(2, "then"), t(" : "), i(3, "else")
	})
})
```
It is possible to make snippets from one filetype available to another using
`ls.filetype_extend`, more info on that in the section [API](#api-2).

## Snippet Insertion
When a new snippet is expanded, it can be connected with the snippets that have
already been expanded in the buffer in various ways.  
First of all, Luasnip distinguishes between root-snippets and child-snippets.
The latter are nested inside other snippets, so when jumping through a snippet,
one may also traverse the child-snippets expanded inside it, more or less as if
the child just contains more nodes of the parent.  
Root-snippets are of course characterized by not being child-snippets.  
When expanding a new snippet, it becomes a child of the snippet whose region it
is expanded inside, and a root if it is not inside any snippet's region.  
If it is inside another snippet, the specific node it is inside is determined,
and the snippet then nested inside that node.

* If that node is interactive (for example, an `insertNode`), the new snippet
  will be traversed when the node is visited, as long as the
  configuration-option `link_children` is enabled. If it is not enabled, it is
  possible to jump from the snippet to the node, but not the other way around.
* If that node is not interactive, the snippet will be linked to the currently
  active node, also such that it will not be jumped to again once it is left.
  This is to prevent jumping large distances across the buffer as much as
  possible. There may still be one large jump from the snippet back to the
  current node it is nested inside, but that seems hard to avoid.  
  Thus, one should design snippets such that the regions where other snippets
  may be expanded are inside `insertNodes`.

If the snippet is not a child, but a root, it can be linked up with the roots
immediately adjacent to it by enabling `link_roots` in `setup`.
Since by default only one root is remembered, one should also set `keep_roots`
if `link_roots` is enabled. The two are separate options, since roots that are
not linked can still be reached by `ls.activate_node()`. This setup (remember
roots, but don't jump to them) is useful for a super-tab like mapping (`<Tab>`
and jump on the same key), where one would like to still enter previous roots.
Since there would almost always be more jumps if the roots are linked, regular
`<Tab>` would not work almost all the time, and thus `link_roots` has to stay
disabled.

# Node

Every node accepts, as its last parameter, an optional table of arguments.
There are some common ones (which are listed here), and some that only apply to
some nodes (`user_args` for function/dynamicNode). These `opts` are
only mentioned if they accept options that are not common to all nodes.

Common opts:

* `node_ext_opts` and `merge_node_ext_opts`: Control `ext_opts` (most likely
  highlighting) of the node. Described in detail in [ext_opts](#ext_opts)
* `key`: The node can be referred to by this key. Useful for either
  [Key Indexer](#key-indexer) or for finding the node at runtime (See
  [Snippets-API](#snippets-api)), for example inside a `dynamicNode`. The keys
  do not have to be unique across the entire lifetime of the snippet, but at any
  point in time, the snippet may contain each key only once. This means it is
  fine to return a keyed node from a `dynamicNode`, because even if it will be
  generated multiple times, those will not be valid at the same time.
* `node_callbacks`: Define event-callbacks for this node (see
  [events](#events)).  
  Accepts a table that maps an event, e.g. `events.enter` to the callback
  (essentially the same as `callbacks` passed to `s`, only that there is no
  first mapping from jump-index to the table of callbacks).

## API

- `get_jump_index()`: this method returns the jump-index of a node. If a node 
  doesn't have a jump-index, this method returns `nil` instead.
- `get_buf_position(opts) -> {from_position, to_position}`:
  Determines the range of the buffer occupied by this node. `from`- and
  `to_position` are `row,column`-tuples, `0,0`-indexed (first line is 0, first
  column is 0) and end-inclusive (see `:h api-indexing`, this is extmarks
  indexing).
  - `opts`: `table|nil`, options, valid keys are:
    - `raw`: `bool`, default `true`. This can be used to switch between
	  byte-columns (`raw=true`) and visual columns (`raw=false`). This makes a
	  difference if the line contains characters represented by multiple bytes
	  in UTF, for example `ÿ`.

# Snippets

The most direct way to define snippets is `s`:
```lua
s({trig="trigger"}, {})
```
(This snippet is useless beyond serving as a minimal example)

`s(context, nodes, opts) -> snippet`

- `context`: Either table or a string. Passing a string is equivalent to passing

  ```lua
  {
  	trig = context
  }
  ```

  The following keys are valid:
  - `trig`: string, the trigger of the snippet. If the text in front of (to the
    left of) the cursor when `ls.expand()` is called matches it, the snippet
    will be expanded.  
    By default, "matches" means the text in front of the cursor matches the
    trigger exactly, this behavior can be modified through `trigEngine`
  - `name`: string, can be used by e.g. `nvim-compe` to identify the snippet.
  - `desc` (or `dscr`): string, description of the snippet, \n-separated or table
    for multiple lines.
  - `wordTrig`: boolean, if true, the snippet is only expanded if the word
    (`[%w_]+`) before the cursor matches the trigger entirely.
    True by default.
  - `regTrig`: boolean, whether the trigger should be interpreted as a
    Lua pattern. False by default.  
    Consider setting `trigEngine` to `"pattern"` instead, it is more expressive,
    and in line with other settings.
  - `trigEngine`: (function|string), determines how `trig` is interpreted, and
    what it means for it to "match" the text in front of the cursor.  
    This behavior can be completely customized by passing a function, but the
    predefined ones, which are accessible by passing their identifier, should
    suffice in most cases:
    * `"plain"`: the default-behavior, the trigger has to match the text before
      the cursor exactly.
    * `"pattern"`: the trigger is interpreted as a Lua pattern, and is a match if
      `trig .. "$"` matches the line up to the cursor. Capture-groups will be
      accessible as `snippet.captures`.
    * `"ecma"`: the trigger is interpreted as an ECMAscript-regex, and is a
      match if `trig .. "$"` matches the line up to the cursor. Capture-groups
      will be accessible as `snippet.captures`.  
      This `trigEngine` requires `jsregexp` (see
      [LSP-snippets-transformations](#transformations)) to be installed, if it
      is not, this engine will behave like `"plain"`.
    * `"vim"`: the trigger is interpreted as a vim-regex, and is a match if
      `trig .. "$"` matches the line up to the cursor. As with the other
      regex/pattern-engines, captures will be available as `snippet.captures`,
      but there is one caveat: the matching is done using `matchlist`, so for
      now empty-string submatches will be interpreted as unmatched, and the
      corresponding `snippet.capture[i]` will be `nil` (this will most likely
      change, don't rely on this behavior).

    Besides these predefined engines, it is also possible to create new ones:
    Instead of a string, pass a function which satisfies
    `trigEngine(trigger, opts) -> (matcher(line_to_cursor, trigger) ->
    whole_match, captures)`
    (i.e. the function receives `trig` and `trigEngineOpts` can, for example,
    precompile a regex, and then returns a function responsible for determining
    whether the current cursor-position (represented by the line up to the
    cursor) matches the trigger (it is passed again here so engines which don't
    do any trigger-specific work (like compilation) can just return a static
    `matcher`), and what the capture-groups are).  
    The `lua`-engine, for example, can be implemented like this:
    ```lua
    local function matcher(line_to_cursor, trigger)
        -- look for match which ends at the cursor.
        -- put all results into a list, there might be many capture-groups.
        local find_res = { line_to_cursor:find(trigger .. "$") }

        if #find_res > 0 then
            -- if there is a match, determine matching string, and the
            -- capture-groups.
            local captures = {}
            -- find_res[1] is `from`, find_res[2] is `to` (which we already know
            -- anyway).
            local from = find_res[1]
            local match = line_to_cursor:sub(from, #line_to_cursor)
            -- collect capture-groups.
            for i = 3, #find_res do
                captures[i - 2] = find_res[i]
            end
            return match, captures
        else
            return nil
        end
    end

    local function engine(trigger)
        -- don't do any special work here, can't precompile lua-pattern.
        return matcher
    end
    ```
    The predefined engines are defined in
    [`trig_engines.lua`](https://github.com/L3MON4D3/LuaSnip/blob/master/lua/luasnip/nodes/util/trig_engines.lua),
    read it for more examples.

  - `trigEngineOpts`: `table<string, any>`, options for the used `trigEngine`.  
    The valid options are:
    * `max_len`: number, upper bound on the length of the trigger.  
      If this is set, the `line_to_cursor` will be truncated (from the cursor of
      course) to `max_len` characters before performing the match.  
      This is implemented because feeding long `line_to_cursor` into e.g. the
      pattern-`trigEngine` will hurt performance quite a bit (see issue
      Luasnip#1103).  
      This option is implemented for all `trigEngines`. 

  - `docstring`: string, textual representation of the snippet, specified like
    `desc`. Overrides docstrings loaded from `json`.
  - `docTrig`: string, used as `line_to_cursor` during docstring-generation.
    This might be relevant if the snippet relies on specific values in the
    capture-groups (for example, numbers, which won't work with the default
    `$CAPTURESN` used during docstring-generation)
  - `hidden`: boolean, hint for completion-engines.
    If set, the snippet should not show up when querying snippets.
  - `priority`: positive number, Priority of the snippet, 1000 by default.  
	Snippets with high priority will be matched to a trigger before those with a
	lower one.
    The priority for multiple snippets can also be set in `add_snippets`.
  - `snippetType`: string, should be either `snippet` or `autosnippet` (ATTENTION:

... [TRUNCATED]
```

### File: data\project-dictionary.txt
```txt
personal_ws-1.1 en 130 utf-8
AbsoluteIndexer
Autosnippets
Cfigure
Cimg
DeVries
ECMAscript
Env
GIFs
IDEs
IndentSnippetNode
LSP
LaTeX
Lua
LuaRock
LuaSnip
LuaSnip's
MiB
MultiSnippet
MultiSnippets
Neovim
Neovim's
Noderef
PascalCase
README
SnipMate
SnippetProxy
Snippetstring
Snippetstrings
TJ
TextMate
Treesitter
UTF
VSCode
VSCode's
Ziontee
aa
amongst
anytext
argnode
argnodes
args
autocommand
autocommands
autosnippet
autosnippets
autotriggered
backtick
boolean
choiceNode
choiceNode's
choiceNodes
cmp
compe
config
configs
counterintuitive
customizability
customizable
datetime
de
deserialized
docstring
docstrings
dynamicNode
dynamicNode's
dynamicNodes
eg
ejmastnak
env
evesdropper
extmark
extmarks
filetype
filetypes
fmt
fn
fts
functionNode
functionNodes
get's
globals
honza
ie
infinitum
ing
insertNode
insertNodes
jsregexp
jumpable
jumplist
keymaps
lsp
lua
luasnip
luasnip's
metamethod
mistyped
molleweide
multiline
namespace
namespaces
nilsnip
nvim
otf
panvimdoc
plaintext
pos
posnil
postfix
pre
precompile
predefining
rafamadriz
restoreNode
restoreNodes
runtime
snippetNode
snippetNodes
submatches
superset
tabstop
tabstops
textNode
textNodes
th
there'd
treesitter
truthy
varargs
vsnip

```

### File: doc\luasnip.txt
```txt
*luasnip.txt*          For NeoVim 0.7-0.11          Last change: 2026 March 21

==============================================================================
Table of Contents                                  *luasnip-table-of-contents*

1. Basics                                                     |luasnip-basics|
  - Jump-Index                                     |luasnip-basics-jump-index|
  - Adding Snippets                           |luasnip-basics-adding-snippets|
  - Snippet Insertion                       |luasnip-basics-snippet-insertion|
2. Node                                                         |luasnip-node|
  - API                                                     |luasnip-node-api|
3. Snippets                                                 |luasnip-snippets|
  - Data                                               |luasnip-snippets-data|
4. TextNode                                                 |luasnip-textnode|
5. InsertNode                                             |luasnip-insertnode|
6. FunctionNode                                         |luasnip-functionnode|
7. Node Reference                                     |luasnip-node-reference|
8. ChoiceNode                                             |luasnip-choicenode|
9. SnippetNode                                           |luasnip-snippetnode|
10. IndentSnippetNode                              |luasnip-indentsnippetnode|
11. DynamicNode                                          |luasnip-dynamicnode|
  - Self-dependent DynamicNode|luasnip-dynamicnode-self-dependent-dynamicnode|
12. RestoreNode                                          |luasnip-restorenode|
13. Snippetstring                                      |luasnip-snippetstring|
14. Key Indexer                                          |luasnip-key-indexer|
15. Optional Noderef                                |luasnip-optional-noderef|
16. Absolute Indexer                                |luasnip-absolute-indexer|
17. MultiSnippet                                        |luasnip-multisnippet|
18. Extras                                                    |luasnip-extras|
  - Lambda                                             |luasnip-extras-lambda|
  - Match                                               |luasnip-extras-match|
  - Repeat                                             |luasnip-extras-repeat|
  - Partial                                           |luasnip-extras-partial|
  - Nonempty                                         |luasnip-extras-nonempty|
  - Dynamic Lambda                             |luasnip-extras-dynamic-lambda|
  - fmt                                                   |luasnip-extras-fmt|
  - Conditions                                     |luasnip-extras-conditions|
  - On The Fly-Snippets                   |luasnip-extras-on-the-fly-snippets|
  - select_choice                               |luasnip-extras-select_choice|
  - Filetype-Functions                     |luasnip-extras-filetype-functions|
  - Postfix-Snippet                           |luasnip-extras-postfix-snippet|
  - Treesitter-Postfix-Snippet     |luasnip-extras-treesitter-postfix-snippet|
  - Snippet List                                 |luasnip-extras-snippet-list|
  - Snippet Location                         |luasnip-extras-snippet-location|
19. Extend Decorator                                |luasnip-extend-decorator|
20. LSP-Snippets                                        |luasnip-lsp-snippets|
  - SnipMate Parser                     |luasnip-lsp-snippets-snipmate-parser|
  - Transformations                     |luasnip-lsp-snippets-transformations|
21. Variables                                              |luasnip-variables|
  - Environment Namespaces          |luasnip-variables-environment-namespaces|
  - LSP-Variables                            |luasnip-variables-lsp-variables|
22. Loaders                                                  |luasnip-loaders|
  - Snippet-specific filetypes    |luasnip-loaders-snippet-specific-filetypes|
  - VS-Code                                          |luasnip-loaders-vs-code|
  - SNIPMATE                                        |luasnip-loaders-snipmate|
  - Lua                                                  |luasnip-loaders-lua|
  - edit_snippets                              |luasnip-loaders-edit_snippets|
23. SnippetProxy                                        |luasnip-snippetproxy|
24. ext_opts                                                |luasnip-ext_opts|
25. Docstrings                                            |luasnip-docstrings|
26. Docstring-Cache                                  |luasnip-docstring-cache|
27. Events                                                    |luasnip-events|
28. Cleanup                                                  |luasnip-cleanup|
29. Logging                                                  |luasnip-logging|
30. Source                                                    |luasnip-source|
31. Selection                                              |luasnip-selection|
32. Config-Options                                    |luasnip-config-options|
33. Troubleshooting                                  |luasnip-troubleshooting|
  - Adding Snippets                  |luasnip-troubleshooting-adding-snippets|
34. API                                                          |luasnip-api|
>
                __                       ____
               /\ \                     /\  _`\           __
               \ \ \      __  __     __ \ \,\L\_\    ___ /\_\  _____
                \ \ \  __/\ \/\ \  /'__`\\/_\__ \  /' _ `\/\ \/\ '__`\
                 \ \ \L\ \ \ \_\ \/\ \L\.\_/\ \L\ \/\ \/\ \ \ \ \ \L\ \
                  \ \____/\ \____/\ \__/.\_\ `\____\ \_\ \_\ \_\ \ ,__/
                   \/___/  \/___/  \/__/\/_/\/_____/\/_/\/_/\/_/\ \ \/
                                                                 \ \_\
                                                                  \/_/
<

LuaSnip is a snippet engine written entirely in Lua. It has some great features
like inserting text (`luasnip-function-node`) or nodes (`luasnip-dynamic-node`)
based on user input, parsing LSP syntax and switching nodes
(`luasnip-choice-node`). For basic setup like mappings and installing, check
the README.

All code snippets in this help assume the following:

>lua
    local ls = require("luasnip")
    local s = ls.snippet
    local sn = ls.snippet_node
    local isn = ls.indent_snippet_node
    local t = ls.text_node
    local i = ls.insert_node
    local f = ls.function_node
    local c = ls.choice_node
    local d = ls.dynamic_node
    local r = ls.restore_node
    local events = require("luasnip.util.events")
    local ai = require("luasnip.nodes.absolute_indexer")
    local opt = require("luasnip.nodes.optional_arg")
    local extras = require("luasnip.extras")
    local l = extras.lambda
    local rep = extras.rep
    local p = extras.partial
    local m = extras.match
    local n = extras.nonempty
    local dl = extras.dynamic_lambda
    local fmt = require("luasnip.extras.fmt").fmt
    local fmta = require("luasnip.extras.fmt").fmta
    local conds = require("luasnip.extras.expand_conditions")
    local postfix = require("luasnip.extras.postfix").postfix
    local types = require("luasnip.util.types")
    local parse = require("luasnip.util.parser").parse_snippet
    local ms = ls.multi_snippet
    local k = require("luasnip.nodes.key_indexer").new_key
<

As noted in the |luasnip-loaders-lua|-section:


  By default, the names from
  [`luasnip.config.snip_env`](https://github.com/L3MON4D3/LuaSnip/blob/master/lua/luasnip/default_config.lua#L22-L104)
  will be used, but it’s possible to customize them by setting `snip_env` in
  `setup`.
Furthermore, note that while this document assumes you have defined `ls` to be
`require("luasnip")`, it is **not** provided in the default set of variables.


==============================================================================
1. Basics                                                     *luasnip-basics*

In LuaSnip, snippets are made up of `nodes`. These can contain either

- static text (`textNode`)
- text that can be edited (`insertNode`)
- text that can be generated from the contents of other nodes (`functionNode`)
- other nodes
  - `choiceNode`: allows choosing between two nodes (which might contain more
    nodes)
  - `restoreNode`: store and restore input to nodes
- or nodes that can be generated based on input (`dynamicNode`).

Snippets are always created using the
`s(trigger:string, nodes:table)`-function. It is explained in more detail in
|luasnip-snippets|, but the gist is that it creates a snippet that contains the
nodes specified in `nodes`, which will be inserted into a buffer if the text
before the cursor matches `trigger` when `ls.expand` is called.


JUMP-INDEX                                         *luasnip-basics-jump-index*

Nodes that can be jumped to (`insertNode`, `choiceNode`, `dynamicNode`,
`restoreNode`, `snippetNode`) all require a "jump-index" so LuaSnip knows the
order in which these nodes are supposed to be visited ("jumped to").

>lua
    s("trig", {
        i(1), t"text", i(2), t"text again", i(3)
    })
<

These indices don’t "run" through the entire snippet, like they do in
TextMate-snippets (`"$1 ${2: $3 $4}"`), they restart at 1 in each nested
snippetNode:

>lua
    s("trig", {
        i(1), t" ", sn(2, {
            t" ", i(1), t" ", i(2)
        })
    })
<

(roughly equivalent to the given TextMate-snippet).


ADDING SNIPPETS                               *luasnip-basics-adding-snippets*

The snippets for a given filetype have to be added to LuaSnip via
`ls.add_snippets(filetype, snippets)`. Snippets that should be accessible
globally (in all filetypes) have to be added to the special filetype `all`.

>lua
    ls.add_snippets("all", {
        s("ternary", {
            -- equivalent to "${1:cond} ? ${2:then} : ${3:else}"
            i(1, "cond"), t(" ? "), i(2, "then"), t(" : "), i(3, "else")
        })
    })
<

It is possible to make snippets from one filetype available to another using
`ls.filetype_extend`, more info on that in the section |luasnip-api|.


SNIPPET INSERTION                           *luasnip-basics-snippet-insertion*

When a new snippet is expanded, it can be connected with the snippets that have
already been expanded in the buffer in various ways.
First of all, Luasnip distinguishes between root-snippets and child-snippets.
The latter are nested inside other snippets, so when jumping through a snippet,
one may also traverse the child-snippets expanded inside it, more or less as if
the child just contains more nodes of the parent.
Root-snippets are of course characterized by not being child-snippets.
When expanding a new snippet, it becomes a child of the snippet whose region it
is expanded inside, and a root if it is not inside any snippet’s region.
If it is inside another snippet, the specific node it is inside is determined,
and the snippet then nested inside that node.

- If that node is interactive (for example, an `insertNode`), the new snippet
  will be traversed when the node is visited, as long as the
  configuration-option `link_children` is enabled. If it is not enabled, it is
  possible to jump from the snippet to the node, but not the other way around.
- If that node is not interactive, the snippet will be linked to the currently
  active node, also such that it will not be jumped to again once it is left.
  This is to prevent jumping large distances across the buffer as much as
  possible. There may still be one large jump from the snippet back to the
  current node it is nested inside, but that seems hard to avoid.
  Thus, one should design snippets such that the regions where other snippets
  may be expanded are inside `insertNodes`.

If the snippet is not a child, but a root, it can be linked up with the roots
immediately adjacent to it by enabling `link_roots` in `setup`. Since by
default only one root is remembered, one should also set `keep_roots` if
`link_roots` is enabled. The two are separate options, since roots that are not
linked can still be reached by `ls.activate_node()`. This setup (remember
roots, but don’t jump to them) is useful for a super-tab like mapping
(`<Tab>` and jump on the same key), where one would like to still enter
previous roots. Since there would almost always be more jumps if the roots are
linked, regular `<Tab>` would not work almost all the time, and thus
`link_roots` has to stay disabled.


==============================================================================
2. Node                                                         *luasnip-node*

Every node accepts, as its last parameter, an optional table of arguments.
There are some common ones (which are listed here), and some that only apply to
some nodes (`user_args` for function/dynamicNode). These `opts` are only
mentioned if they accept options that are not common to all nodes.

Common opts:

- `node_ext_opts` and `merge_node_ext_opts`: Control `ext_opts` (most likely
  highlighting) of the node. Described in detail in |luasnip-ext_opts|
- `key`: The node can be referred to by this key. Useful for either
  |luasnip-key-indexer| or for finding the node at runtime (See
  |luasnip-snippets-api|), for example inside a `dynamicNode`. The keys
  do not have to be unique across the entire lifetime of the snippet, but at any
  point in time, the snippet may contain each key only once. This means it is
  fine to return a keyed node from a `dynamicNode`, because even if it will be
  generated multiple times, those will not be valid at the same time.
- `node_callbacks`: Define event-callbacks for this node (see
  |luasnip-events|).
  Accepts a table that maps an event, e.g. `events.enter` to the callback
  (essentially the same as `callbacks` passed to `s`, only that there is no
  first mapping from jump-index to the table of callbacks).


API                                                         *luasnip-node-api*

- `get_jump_index()`: this method returns the jump-index of a node. If a node
  doesn’t have a jump-index, this method returns `nil` instead.
- `get_buf_position(opts) -> {from_position, to_position}`:
  Determines the range of the buffer occupied by this node. `from`- and
  `to_position` are `row,column`-tuples, `0,0`-indexed (first line is 0, first
  column is 0) and end-inclusive (see |api-indexing|, this is extmarks
  indexing).
  - `opts`: `table|nil`, options, valid keys are:
    - `raw`: `bool`, default `true`. This can be used to switch between
      byte-columns (`raw=true`) and visual columns (`raw=false`). This makes a
      difference if the line contains characters represented by multiple bytes
      in UTF, for example `ÿ`.


==============================================================================
3. Snippets                                                 *luasnip-snippets*

The most direct way to define
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
