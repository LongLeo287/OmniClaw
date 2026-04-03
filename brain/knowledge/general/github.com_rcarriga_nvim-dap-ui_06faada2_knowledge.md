---
id: github.com-rcarriga-nvim-dap-ui-06faada2-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:17.214577
---

# KNOWLEDGE EXTRACT: github.com_rcarriga_nvim-dap-ui_06faada2
> **Extracted on:** 2026-04-01 15:21:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524456/github.com_rcarriga_nvim-dap-ui_06faada2

---

## File: `.editorconfig`
```
# see https://github.com/CppCXY/EmmyLuaCodeStyle
[*.lua]
# [basic code reformat option]
# optional space/tab
indent_style = space
# if indent_style is space, this is valid
indent_size = 2
# if indent_style is tab, this is valid
tab_width = 2
# none/single/double
quote_style = double
# keep/remove
call_arg_parentheses = keep
# only support number
continuation_indent_size = 2
# if true, continuation_indent_size for local or assign statement is invalid
# however, if the expression list has cross row expression, it will not be aligned to the first expression
local_assign_continuation_align_to_first_expression = false
# function call expression's args will align to first arg
# however, if the args has cross row arg, it will not be aligned to the first arg
align_call_args = false
# if true, all function define params will align to first param
align_function_define_params = true
# if true, format like this "local t = { 1, 2, 3 }"
keep_one_space_between_table_and_bracket = true
# if indent_style is tab, this option is invalid
align_table_field_to_first_field = false
# if true, ormat like this "local t <const> = 1"
keep_one_space_between_namedef_and_attribute = false
# continous line distance
max_continuous_line_distance = 1
# see document for detail
continuous_assign_statement_align_to_equal_sign = true
# see document for detail
continuous_assign_table_field_align_to_equal_sign = true
# if true, the label loses its current indentation
label_no_indent = false
# if true, there will be no indentation in the do statement
do_statement_no_indent = false
# if true, the conditional expression of the if statement will not be a continuation line indent
if_condition_no_continuation_indent = false
# if true, t[#t+1] will not space wrapper '+'
table_append_expression_no_space = false
# if statement will align like switch case 
if_condition_align_with_each_other = false

long_chain_expression_allow_one_space_after_colon = false
# optional crlf/lf/auto, if it is 'auto', in windows it is crlf other platforms are lf
end_of_line = lf

# [line layout]
# The following configuration supports three expressions
# minLine:${n}   
# keepLine   
# KeepLine:${n}

keep_line_after_if_statement = minLine:0
keep_line_after_do_statement = minLine:0
keep_line_after_while_statement = minLine:0
keep_line_after_repeat_statement = minLine:0
keep_line_after_for_statement = minLine:0
keep_line_after_local_or_assign_statement = keepLine
keep_line_after_function_define_statement = keepLine:1

# [diagnostic]
# the following is code diagnostic options
enable_check_codestyle = true
# this mean utf8 length
max_line_length = 120
# this will check text end with new line(format always end with new line)
insert_final_newline = true

# [name style check]
enable_name_style_check = true
# the following is name style check rule 
# base option off/camel_case/snake_case/upper_snake_case/pascal_case/same(filename/first_param/'<const string>', snake_case/pascal_case/camel_case)
# all option can use '|' represent or 
# for example:
# snake_case | upper_snake_case
# same(first_param, snake_case)
# same('m')
local_name_define_style = snake_case
function_param_name_style = snake_case
function_name_define_style = snake_case
local_function_name_define_style = snake_case
table_field_name_define_style = snake_case
global_variable_name_define_style = snake_case|upper_snake_case
module_name_define_style = same('M')|same(filename, snake_case)
require_module_name_style = same(snake_case)
class_name_define_style = same(filename, snake_case)
```

## File: `.gitignore`
```
neovim/
doc/tags
plenary.nvim/
```

## File: `.releaserc.json`
```json
{
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/github",
      {
        "successComment": false
      }
    ]
  ]
}
```

## File: `Dockerfile`
```

ARG NEOVIM_RELEASE=${NEOVIM_RELEASE:-https://github.com/neovim/neovim/releases/download/nightly/nvim-linux64.tar.gz}
FROM ubuntu:21.04
ARG NEOVIM_RELEASE

RUN apt-get update
RUN apt-get -y install git curl tar gcc g++ make
RUN mkdir /neovim
RUN curl -sL ${NEOVIM_RELEASE} | tar xzf - --strip-components=1 -C "/neovim"
RUN git clone --depth 1 https://github.com/nvim-lua/plenary.nvim
RUN git clone --depth 1 https://github.com/tjdevries/tree-sitter-lua

WORKDIR tree-sitter-lua
RUN make dist

RUN mkdir /app
WORKDIR /app

ENTRYPOINT ["bash", "-c", "PATH=/neovim/bin:${PATH} VIM=/neovim/share/nvim/runtime nvim --headless -c 'set rtp+=. | set rtp+=../plenary.nvim/ | set rtp+=../tree-sitter-lua/ | runtime! plugin/plenary.vim | luafile ./scripts/gendocs.lua' -c 'qa'"]
```

## File: `LICENCE.md`
```markdown
MIT License

Copyright (c) 2023 Rónán Carrigan

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

![image](https://user-images.githubusercontent.com/24252670/126843106-5dce09dc-49d0-4aaa-ba98-fd8f17b31414.png)

Element ID: `stacks`

Displays the running threads and their stack frames.

Mappings:

- `open`: Jump to a place within the stack frame.
- `toggle`: Toggle displaying [subtle](https://microsoft.github.io/debug-adapter-protocol/specification#Types_StackFrame) frames

### Watch Expressions

![image](https://user-images.githubusercontent.com/24252670/126843390-4e1575d8-9d7d-4f43-8680-094cfe9eae63.png)

Element ID: `watches`

Allows creation of expressions to watch the value of in the context of the
current frame.
This uses a prompt buffer for input. To enter a new expression, just enter
insert mode and you will see a prompt appear. Press enter to submit

Mappings:

- `expand`: Toggle showing the children of an expression.
- `remove`: Remove the watched expression.
- `edit`: Edit an expression or set the value of a child variable.
- `repl`: Send expression to REPL

### Breakpoints

![image](https://user-images.githubusercontent.com/24252670/126843577-361645e4-6265-40eb-86dc-d6607512a15e.png)

Element ID: `breakpoints`

List all breakpoints currently set.

Mappings:

- `open`: Jump to the location the breakpoint is set
- `toggle`: Enable/disable the selected breakpoint

### REPL

Element ID: `repl`

The REPL provided by nvim-dap.

### Console

Element ID: `console`

The console window used by nvim-dap for the integrated terminal.

## Usage

To get started simply call the setup method on startup, optionally providing
custom settings.

```lua
require("dapui").setup()
```

You can open, close and toggle the windows with corresponding functions:

```lua
require("dapui").open()
require("dapui").close()
require("dapui").toggle()
```

Each of the functions optionally takes either `"sidebar"` or `"tray"` as an
argument to only change the specified component.

You can use nvim-dap events to open and close the windows automatically (`:help dap-extensions`)

```lua
local dap, dapui = require("dap"), require("dapui")
dap.listeners.before.attach.dapui_config = function()
  dapui.open()
end
dap.listeners.before.launch.dapui_config = function()
  dapui.open()
end
dap.listeners.before.event_terminated.dapui_config = function()
  dapui.close()
end
dap.listeners.before.event_exited.dapui_config = function()
  dapui.close()
end
```

### Floating Elements

For elements that are not opened in the tray or sidebar, you can open them in a
floating window.

![image](https://user-images.githubusercontent.com/24252670/126844102-8789effb-4276-4599-afe6-a074b019c38d.png)

```lua
require("dapui").float_element(<element ID>, <optional settings>)
```

If you do not provide an element ID, you will be queried to select one.

The optional settings can included the following keys:

- `width: number` Width of the window
- `height: number` Height of the window
- `enter: boolean` Enter the floating window
- `position: string` Position of floating window. `center` or `nil`

Call the same function again while the window is open and the cursor will jump
to the floating window. The REPL will automatically jump to the floating
window on open.

### Evaluate Expression

For a one time expression evaluation, you can call a hover window to show a value

![image](https://user-images.githubusercontent.com/24252670/126844454-691d691c-4550-46fe-89dc-25e1e9681545.png)

```lua
require("dapui").eval(<expression>)
```

If an expression is not provided it will use the word under the cursor, or if in
visual mode, the currently highlighted text.
You can define a visual mapping like so

```vim
vnoremap <M-k> <Cmd>lua require("dapui").eval()<CR>
```

Call the same function again while the window is open to jump to the eval window.

The same mappings as the variables element apply within the hover window.
```

## File: `stylua.toml`
```
column_width = 100
line_endings = "Unix"
indent_type = "Spaces"
indent_width = 2
quote_style = "AutoPreferDouble"
```

## File: `doc/nvim-dap-ui.txt`
```
nvim-dap-ui.txt*	A UI for nvim-dap.

==============================================================================
nvim-dap-ui                                                        *nvim-dap-ui*

  Setup........................................................|dapui.setup()|
  Configuration Options.........................................|dapui.config|
  Variable Scopes......................................|dapui.elements.scopes|
  Threads and Stack Frames.............................|dapui.elements.stacks|
  REPL...................................................|dapui.elements.repl|
  Watch Expressions...................................|dapui.elements.watches|
  Breakpoints.....................................|dapui.elements.breakpoints|
  Console.............................................|dapui.elements.console|

A UI for nvim-dap which provides a good out of the box configuration.
nvim-dap-ui is built on the idea of "elements". These elements are windows
which provide different features.
Elements are grouped into layouts which can be placed on any side of the
screen. There can be any number of layouts, containing whichever elements
desired.

Elements can also be displayed temporarily in a floating window.

See `:h dapui.setup()` for configuration options and defaults

It is highly recommended to use neodev.nvim to enable type checking for
nvim-dap-ui to get type checking, documentation and autocompletion for
all API functions.

>lua
  require("neodev").setup({
    library = { plugins = { "nvim-dap-ui" }, types = true },
    ...
  })
<

The default icons use codicons(https://github.com/microsoft/vscode-codicons).
It's recommended to use this fork(https://github.com/ChristianChiarulli/neovim-codicons)
which fixes alignment issues for the terminal. If your terminal doesn't
support font fallback and you need to have icons included in your font,
you can patch it via Font Patcher(https://github.com/ryanoasis/nerd-fonts#option-8-patch-your-own-font).
There is a simple step by step guide here: https://github.com/mortepau/codicons.nvim#how-to-patch-fonts.

                                                                 *dapui.setup()*
`setup`({user_config})


Configure nvim-dap-ui
See also ~
|dapui.Config|

Default values:
>lua
  {
    controls = {
      element = "repl",
      enabled = true,
      icons = {
        disconnect = "",
        pause = "",
        play = "",
        run_last = "",
        step_back = "",
        step_into = "",
        step_out = "",
        step_over = "",
        terminate = ""
      }
    },
    element_mappings = {},
    expand_lines = true,
    floating = {
      border = "single",
      mappings = {
        close = { "q", "<Esc>" }
      }
    },
    force_buffers = true,
    icons = {
      collapsed = "",
      current_frame = "",
      expanded = ""
    },
    layouts = { {
        elements = { {
            id = "scopes",
            size = 0.25
          }, {
            id = "breakpoints",
            size = 0.25
          }, {
            id = "stacks",
            size = 0.25
          }, {
            id = "watches",
            size = 0.25
          } },
        position = "left",
        size = 40
      }, {
        elements = { {
            id = "repl",
            size = 0.5
          }, {
            id = "console",
            size = 0.5
          } },
        position = "bottom",
        size = 10
      } },
    mappings = {
      edit = "e",
      expand = { "<CR>", "<2-LeftMouse>" },
      open = "o",
      remove = "d",
      repl = "r",
      toggle = "t"
    },
    render = {
      indent = 1,
      max_value_lines = 100
    }
  }
<
Parameters~
{user_config?} `(dapui.Config)`

Type ~
`(table<string, dapui.Element>)`

Type ~
dapui.Element

                                                        *dapui.FloatElementArgs*
Fields~
{width} `(integer)` Fixed width of window
{height} `(integer)` Fixed height of window
{enter} `(boolean)` Whether or not to enter the window after opening
{title} `(string)` Title of window
{position} `("center")` Position of floating window

                                                         *dapui.float_element()*
`float_element`({elem_name}, {args})

Open a floating window containing the desired element.

If no fixed dimensions are given, the window will expand to fit the contents
of the buffer.
Parameters~
{elem_name} `(string)`
{args?} `(dapui.FloatElementArgs)`

                                                                *dapui.EvalArgs*
Fields~
{context} `(string)` Context to use for evalutate request, defaults to
"hover". Hover requests should have no side effects, if you have errors
with evaluation, try changing context to "repl". See the DAP specification
for more details.
{width} `(integer)` Fixed width of window
{height} `(integer)` Fixed height of window
{enter} `(boolean)` Whether or not to enter the window after opening

                                                                  *dapui.eval()*
`eval`({expr}, {args})

Open a floating window containing the result of evaluting an expression

If no fixed dimensions are given, the window will expand to fit the contents
of the buffer.
Parameters~
{expr?} `(string)` Expression to evaluate. If nil, then in normal more the
current word is used, and in visual mode the currently highlighted text.
{args?} `(dapui.EvalArgs)`

                                                         *dapui.update_render()*
`update_render`({update})

Update the config.render settings and re-render windows
Parameters~
{update} `(dapui.Config.render)` Updated settings, from the `render` table of
the config

                                                               *dapui.CloseArgs*
Fields~
{layout?} `(number)` Index of layout in config

                                                                 *dapui.close()*
`close`({args})

Close one or all of the window layouts
Parameters~
{args?} `(dapui.CloseArgs)`

                                                                *dapui.OpenArgs*
Fields~
{layout?} `(number)` Index of layout in config
{reset?} `(boolean)` Reset windows to original size

                                                                  *dapui.open()*
`open`({args})

Open one or all of the window layouts
Parameters~
{args?} `(dapui.OpenArgs)`

                                                              *dapui.ToggleArgs*
Fields~
{layout?} `(number)` Index of layout in config
{reset?} `(boolean)` Reset windows to original size

                                                                *dapui.toggle()*
`toggle`({args})

Toggle one or all of the window layouts.
Parameters~
{args?} `(dapui.ToggleArgs)`

dapui.elements                                                  *dapui.elements*


Access the elements currently registered. See elements corresponding help
tag for API information.

Fields~
{hover} `(dapui.elements.hover)`
{breakpoints} `(dapui.elements.breakpoints)`
{repl} `(dapui.elements.repl)`
{scopes} `(dapui.elements.scopes)`
{stack} `(dapui.elements.stacks)`
{watches} `(dapui.elements.watches)`
{console} `(dapui.elements.console)`

                                                                 *dapui.Element*
Fields~
{render} `(fun())` Triggers the element to refresh its buffer. Used when
render settings have changed
{buffer} `(fun(): integer)` Gets the current buffer for the element. The
buffer can change over repeated calls
{float_defaults?} `(fun(): dapui.FloatElementArgs)` Default settings for
floating windows. Useful for element windows which should be larger than
their content
{allow_without_session?} `(boolean)` Allows floating the element when
there is no active debug session

                                                      *dapui.register_element()*
`register_element`({name}, {element})

Registers a new element that can be used within layouts or floating windows
Parameters~
{name} `(string)` Name of the element
{element} `(dapui.Element)`


==============================================================================
dapui.config                                                      *dapui.config*

                                                                  *dapui.Config*
Fields~
{icons} `(dapui.Config.icons)`
{mappings} `(table<dapui.Action, string|string[]>)` Keys to trigger actions in elements
{element_mappings} `(table<string, table<dapui.Action, string|string[]>>)` Per-element overrides of global mappings
{expand_lines} `(boolean)` Expand current line to hover window if larger
than window size
{force_buffers} `(boolean)` Prevents other buffers being loaded into
nvim-dap-ui windows
{layouts} `(dapui.Config.layout[])` Layouts to display elements within.
Layouts are opened in the order defined
{floating} `(dapui.Config.floating)` Floating window specific options
{controls} `(dapui.Config.controls)` Controls configuration
{render} `(dapui.Config.render)` Rendering options which can be updated
after initial setup
{select_window?} `(fun(): integer)` A function which returns a window to be
used for opening buffers such as a stack frame location.

                                                            *dapui.Config.icons*
Fields~
{expanded} `(string)`
{collapsed} `(string)`
{current_frame} `(string)`

                                                           *dapui.Config.layout*
Fields~
{elements} `(string[]|dapui.Config.layout.element[])` Elements to display
in this layout
{size} `(number)` Size of the layout in lines/columns
{position} `("left"|"right"|"top"|"bottom")` Which side of editor to open
layout on

                                                   *dapui.Config.layout.element*
Fields~
{id} `(string)` Element ID
{size} `(number)` Size of the element in lines/columns or as proportion of
total editor size (0-1)

                                                         *dapui.Config.floating*
Fields~
{max_height?} `(number)` Maximum height of floating window (integer or float
between 0 and 1)
{max_width?} `(number)` Maximum width of floating window (integer or float
between 0 and 1)
{border} `(string|string[])` Border argument supplied to `nvim_open_win`
{mappings} `(table<dapui.FloatingAction, string|string[]>)` Keys to trigger
actions in elements

                                                         *dapui.Config.controls*
Fields~
{enabled} `(boolean)` Show controls on an element (requires winbar feature)
{element} `(string)` Element to show controls on
{icons} `(dapui.Config.controls.icons)`

                                                   *dapui.Config.controls.icons*
Fields~
{pause} `(string)`
{play} `(string)`
{step_into} `(string)`
{step_over} `(string)`
{step_out} `(string)`
{step_back} `(string)`
{run_last} `(string)`
{terminate} `(string)`

                                                           *dapui.Config.render*
Fields~
{indent} `(integer)` Default indentation size
{max_type_length?} `(integer)` Maximum number of characters to allow a type
name to fill before trimming
{max_value_lines?} `(integer)` Maximum number of lines to allow a value to
fill before trimming
{sort_variables?} `(fun(a: dapui.types.Variable, b: dapui.types.Variable):boolean)` Sorting function to determine
render order of variables.

                                                                  *dapui.Action*
Alias~
`dapui.Action` → `"expand"|"open"|"remove"|"edit"|"repl"|"toggle"`

                                                          *dapui.FloatingAction*
Alias~
`dapui.FloatingAction` → `"close"`


==============================================================================
dapui.elements.scopes                                    *dapui.elements.scopes*

Displays the available scopes and variables within them.

Mappings:
- `edit`: Edit the value of a variable
- `expand`: Toggle showing any children of variable.
- `repl`: Send variable to REPL


==============================================================================
dapui.elements.stacks                                    *dapui.elements.stacks*

Displays the running threads and their stack frames.

Mappings:
- `open`: Jump to a place within the stack frame.
- `toggle`: Toggle displaying subtle frames


==============================================================================
dapui.elements.repl                                        *dapui.elements.repl*

The REPL provided by nvim-dap.


==============================================================================
dapui.elements.watches                                  *dapui.elements.watches*

Allows creation of expressions to watch the value of in the context of the
current frame.
This uses a prompt buffer for input. To enter a new expression, just enter
insert mode and you will see a prompt appear. Press enter to submit

Mappings:

- `expand`: Toggle showing the children of an expression.
- `remove`: Remove the watched expression.
- `edit`: Edit an expression or set the value of a child variable.
- `repl`: Send expression to REPL

                                                  *dapui.elements.watches.add()*
`add`({expr})

Add a new watch expression
Parameters~
{expr?} `(string)`

                                                 *dapui.elements.watches.edit()*
`edit`({index}, {new_expr})

Change the chosen watch expression
Parameters~
{index} `(integer)`
{new_expr} `(string)`

                                               *dapui.elements.watches.remove()*
`remove`({index})

Remove the chosen watch expression

                                                  *dapui.elements.watches.get()*
`get`()

Get the current list of watched expressions
Return~
`(dapui.elements.watches.Watch[])`

                                                  *dapui.elements.watches.Watch*
Fields~
{expression} `(string)`
{expanded} `(boolean)`

                                        *dapui.elements.watches.toggle_expand()*
`toggle_expand`({index})

Toggle the expanded state of the chosen watch expression
Parameters~
{index} `(integer)`


==============================================================================
dapui.elements.breakpoints                          *dapui.elements.breakpoints*

Lists all breakpoints currently set.

Mappings:
- `open`: Jump to the location the breakpoint is set
- `toggle`: Enable/disable the selected breakpoint
- `remove`: Remove breakpoint. Only works on enabled breakpoints.


==============================================================================
dapui.elements.console                                  *dapui.elements.console*

The console window used by nvim-dap for the integrated terminal.


 vim:tw=78:ts=8:noet:ft=help:norl:
```

## File: `lua/dapui/controls.lua`
```
local dap = require("dap")
local config = require("dapui.config")

local M = {}

local controls_active = false
M.refresh_control_panel = function() end

function M.enable_controls(element)
  if controls_active then
    return
  end
  controls_active = true
  local buffer = element.buffer()

  local group = vim.api.nvim_create_augroup("DAPUIControls", {})
  local win = vim.fn.bufwinid(buffer)

  M.refresh_control_panel = function()
    if win then
      local is_current = win == vim.fn.win_getid()
      if not pcall(vim.api.nvim_win_set_option, win, "winbar", M.controls(is_current)) then
        win = nil
      end
      vim.cmd("redrawstatus!")
    end
  end

  local list_id = "dapui_controls"
  local events = {
    "continue",
    "terminate",
    "restart",
    "disconnect",
    "event_terminated",
    "disconnect",
    "event_exited",
    "event_stopped",
    "threads",
    "event_continued",
  }
  for _, event in ipairs(events) do
    dap.listeners.after[event][list_id] = M.refresh_control_panel
  end

  vim.api.nvim_create_autocmd("BufWinEnter", {
    buffer = buffer,
    group = group,
    callback = function(opts)
      if win then
        return
      end

      win = vim.fn.bufwinid(opts.buf)
      if win == -1 then
        win = nil
        return
      end
      M.refresh_control_panel()
      vim.api.nvim_create_autocmd({ "WinClosed", "BufWinLeave" }, {
        group = group,
        buffer = buffer,
        callback = function()
          if win and not vim.api.nvim_win_is_valid(win) then
            win = nil
          end
        end,
      })
    end,
  })
  -- If original buffer is deleted, this will get newest element buffer
  vim.api.nvim_create_autocmd("BufWipeout", {
    buffer = buffer,
    group = group,
    callback = vim.schedule_wrap(function()
      controls_active = false
      M.enable_controls(element)
    end),
  })

  vim.api.nvim_create_autocmd("WinEnter", {
    buffer = buffer,
    group = group,
    callback = function()
      local winbar = M.controls(true)
      vim.api.nvim_win_set_option(vim.api.nvim_get_current_win(), "winbar", winbar)
    end,
  })
  vim.api.nvim_create_autocmd("WinLeave", {
    buffer = buffer,
    group = group,
    callback = function()
      local winbar = M.controls(false)
      vim.api.nvim_win_set_option(vim.api.nvim_get_current_win(), "winbar", winbar)
    end,
  })
end

_G._dapui = {
  play = function()
    local session = dap.session()
    if not session or session.stopped_thread_id then
      dap.continue()
    else
      dap.pause()
    end
  end,
}

setmetatable(_dapui, {
  __index = function(_, key)
    return function()
      return dap[key]()
    end
  end,
})
function M.controls(is_active)
  local session = dap.session()

  local running = (session and not session.stopped_thread_id)

  local avail_hl = function(group, allow_running)
    if not session or (not allow_running and running) then
      return is_active and "DapUIUnavailable" or "DapUIUnavailableNC"
    end
    return group
  end

  local icons = config.controls.icons
  local elems = {
    {
      func = "play",
      icon = running and icons.pause or icons.play,
      hl = is_active and "DapUIPlayPause" or "DapUIPlayPauseNC",
    },
    { func = "step_into", hl = avail_hl(is_active and "DapUIStepInto" or "DapUIStepIntoNC") },
    { func = "step_over", hl = avail_hl(is_active and "DapUIStepOver" or "DapUIStepOverNC") },
    { func = "step_out", hl = avail_hl(is_active and "DapUIStepOut" or "DapUIStepOutNC") },
    { func = "step_back", hl = avail_hl(is_active and "DapUIStepBack" or "DapUIStepBackNC") },
    { func = "run_last", hl = is_active and "DapUIRestart" or "DapUIRestartNC" },
    { func = "terminate", hl = avail_hl(is_active and "DapUIStop" or "DapUIStopNC", true) },
    { func = "disconnect", hl = avail_hl(is_active and "DapUIStop" or "DapUIStopNC", true) },
  }
  local bar = ""
  for _, elem in ipairs(elems) do
    bar = bar
      .. ("  %%#%s#%%0@v:lua._dapui.%s@%s%%#0#"):format(
        elem.hl,
        elem.func,
        elem.icon or icons[elem.func]
      )
  end
  return bar
end

return M
```

## File: `lua/dapui/init.lua`
```
---@tag nvim-dap-ui

---@toc
---@text
--- A UI for nvim-dap which provides a good out of the box configuration.
--- nvim-dap-ui is built on the idea of "elements". These elements are windows
--- which provide different features.
--- Elements are grouped into layouts which can be placed on any side of the
--- screen. There can be any number of layouts, containing whichever elements
--- desired.
---
--- Elements can also be displayed temporarily in a floating window.
---
--- See `:h dapui.setup()` for configuration options and defaults
---
--- It is highly recommended to use neodev.nvim to enable type checking for
--- nvim-dap-ui to get type checking, documentation and autocompletion for
--- all API functions.
---
--- ```lua
---   require("neodev").setup({
---     library = { plugins = { "nvim-dap-ui" }, types = true },
---     ...
---   })
--- ```
---
--- The default icons use codicons(https://github.com/microsoft/vscode-codicons).
--- It's recommended to use this fork(https://github.com/ChristianChiarulli/neovim-codicons)
--- which fixes alignment issues for the terminal. If your terminal doesn't
--- support font fallback and you need to have icons included in your font,
--- you can patch it via Font Patcher(https://github.com/ryanoasis/nerd-fonts#option-8-patch-your-own-font).
--- There is a simple step by step guide here: https://github.com/mortepau/codicons.nvim#how-to-patch-fonts.

local success, _ = pcall(require, "nio")
if not success then
  error(
    "nvim-dap-ui requires nvim-nio to be installed. Install from https://github.com/nvim-neotest/nvim-nio"
  )
end

local dap = require("dap")

---@class dapui
---@nodoc
local dapui = {}

local windows = require("dapui.windows")
local config = require("dapui.config")
local util = require("dapui.util")
local nio = require("nio")
local controls = require("dapui.controls")

---@type table<string, dapui.Element>
---@nodoc
local elements = {}

local open_float = nil

local function query_elem_name()
  local entries = {}
  for name, _ in pairs(elements) do
    if name ~= "hover" then
      entries[#entries + 1] = name
    end
  end
  return nio.ui.select(entries, {
    prompt = "Select an element:",
    format_item = function(entry)
      return entry:sub(1, 1):upper() .. entry:sub(2)
    end,
  })
end

---@toc_entry Setup
---@text
--- Configure nvim-dap-ui
---@seealso |dapui.Config|
---
---@eval return require('dapui.config')._format_default()
---@param user_config? dapui.Config
function dapui.setup(user_config)
  util.stop_render_tasks()

  config.setup(user_config)

  local client = require("dapui.client")(dap.session)

  ---@type table<string, dapui.Element>
  for _, module in pairs({
    "breakpoints",
    "repl",
    "scopes",
    "stacks",
    "watches",
    "hover",
    "console",
  }) do
    local existing_elem = elements[module]
    if existing_elem then
      local buffer = existing_elem.buffer()
      if vim.api.nvim_buf_is_valid(buffer) then
        vim.api.nvim_buf_delete(buffer, { force = true })
      end
    end
    ---@type dapui.Element
    local elem = require("dapui.elements." .. module)(client)

    elements[module] = elem
  end

  local element_buffers = {}
  for name, elem in pairs(elements) do
    element_buffers[name] = elem.buffer
  end
  windows.setup(element_buffers)
end

---@class dapui.FloatElementArgs
---@field width integer Fixed width of window
---@field height integer Fixed height of window
---@field enter boolean Whether or not to enter the window after opening
---@field title string Title of window
---@field position "center" Position of floating window

--- Open a floating window containing the desired element.
---
--- If no fixed dimensions are given, the window will expand to fit the contents
--- of the buffer.
---@param elem_name string
---@param args? dapui.FloatElementArgs
function dapui.float_element(elem_name, args)
  nio.run(function()
    elem_name = elem_name or query_elem_name()
    if not elem_name then
      return
    end
    local elem = elements[elem_name]
    if not elem then
      util.notify("No such element: " .. elem_name, vim.log.levels.ERROR)
      return
    end
    if not elem.allow_without_session and not dap.session() then
      util.notify("No active debug session", vim.log.levels.WARN)
      return
    end
    if open_float then
      return open_float:jump_to()
    end
    local line_no = nio.fn.screenrow()
    local col_no = nio.fn.screencol()
    local position = { line = line_no, col = col_no }
    elem.render()
    args = vim.tbl_deep_extend(
      "keep",
      args or {},
      elem.float_defaults and elem.float_defaults() or {},
      { title = elem_name }
    )
    nio.scheduler()
    open_float = require("dapui.windows").open_float(elem_name, elem, position, args)
    if open_float then
      open_float:listen("close", function()
        open_float = nil
      end)
    end
  end)
end

local prev_expr = nil

---@class dapui.EvalArgs
---@field context string Context to use for evalutate request, defaults to
--- "hover". Hover requests should have no side effects, if you have errors
--- with evaluation, try changing context to "repl". See the DAP specification
--- for more details.
---@field width integer Fixed width of window
---@field height integer Fixed height of window
---@field enter boolean Whether or not to enter the window after opening

--- Open a floating window containing the result of evaluting an expression
---
--- If no fixed dimensions are given, the window will expand to fit the contents
--- of the buffer.
---@param expr? string Expression to evaluate. If nil, then in normal more the
--- current word is used, and in visual mode the currently highlighted text.
---@param args? dapui.EvalArgs
function dapui.eval(expr, args)
  nio.run(function()
    if not dap.session() then
      util.notify("No active debug session", vim.log.levels.WARN)
      return
    end
    args = args or {}
    if not expr then
      expr = util.get_current_expr()
    end
    if open_float then
      if prev_expr == expr then
        open_float:jump_to()
        return
      else
        open_float:close()
      end
    end
    prev_expr = expr
    local elem = dapui.elements.hover
    elem.set_expression(expr, args.context)
    local win_pos = nio.api.nvim_win_get_position(0)
    local position = {
      line = win_pos[1] + nio.fn.winline(),
      col = win_pos[2] + nio.fn.wincol() - 1,
    }
    open_float = require("dapui.windows").open_float("hover", elem, position, args)
    if open_float then
      open_float:listen("close", function()
        open_float = nil
      end)
    end
  end)
end

--- Update the config.render settings and re-render windows
---@param update dapui.Config.render Updated settings, from the `render` table of
--- the config
function dapui.update_render(update)
  config.update_render(update)
  nio.run(function()
    for _, elem in pairs(elements) do
      elem.render()
    end
  end)
end

local function keep_cmdheight(cb)
  local cmd_height = vim.o.cmdheight

  cb()

  vim.o.cmdheight = cmd_height
end

---@class dapui.CloseArgs
---@field layout? number Index of layout in config

--- Close one or all of the window layouts
---@param args? dapui.CloseArgs
function dapui.close(args)
  keep_cmdheight(function()
    args = args or {}
    if type(args) == "number" then
      args = { layout = args }
    end
    local layout = args.layout

    for _, win_layout in ipairs(windows.layouts) do
      win_layout:update_sizes()
    end
    for i, win_layout in ipairs(windows.layouts) do
      if not layout or layout == i then
        win_layout:close()
      end
    end
  end)
end

---@generic T
---@param list T[]
---@return fun(): number, T
---@nodoc
local function reverse(list)
  local i = #list + 1
  return function()
    i = i - 1
    if i <= 0 then
      return nil
    end
    return i, list[i]
  end
end

---@class dapui.OpenArgs
---@field layout? number Index of layout in config
---@field reset? boolean Reset windows to original size

--- Open one or all of the window layouts
---@param args? dapui.OpenArgs
function dapui.open(args)
  keep_cmdheight(function()
    args = args or {}
    if type(args) == "number" then
      args = { layout = args }
    end
    local layout = args.layout

    for _, win_layout in ipairs(windows.layouts) do
      win_layout:update_sizes()
    end
    local closed = {}
    if layout then
      for i = 1, (layout and layout - 1) or #windows.layouts, 1 do
        if windows.layouts[i]:is_open() then
          closed[#closed + 1] = i
          windows.layouts[i]:close()
        end
      end
    end

    for i, win_layout in reverse(windows.layouts) do
      if not layout or layout == i then
        win_layout:open()
      end
    end

    if #closed > 0 then
      for _, i in ipairs(closed) do
        windows.layouts[i]:open()
      end
    end

    for _, win_layout in ipairs(windows.layouts) do
      win_layout:resize(args)
    end
  end)
  dapui.update_render({})
  if config.controls.enabled and config.controls.element ~= "" then
    controls.enable_controls(elements[config.controls.element])
  end
  controls.refresh_control_panel()
end

---@class dapui.ToggleArgs
---@field layout? number Index of layout in config
---@field reset? boolean Reset windows to original size

--- Toggle one or all of the window layouts.
---@param args? dapui.ToggleArgs
function dapui.toggle(args)
  keep_cmdheight(function()
    args = args or {}
    if type(args) == "number" then
      args = { layout = args }
    end
    local layout = args.layout

    for _, win_layout in reverse(windows.layouts) do
      win_layout:update_sizes()
    end

    local closed = {}
    if layout then
      for i = 1, (layout and layout - 1) or #windows.layouts, 1 do
        if windows.layouts[i]:is_open() then
          closed[#closed + 1] = i
          windows.layouts[i]:close()
        end
      end
    end

    for i, win_layout in reverse(windows.layouts) do
      if not layout or layout == i then
        win_layout:toggle()
      end
    end

    for _, i in reverse(closed) do
      windows.layouts[i]:open()
    end

    for _, win_layout in ipairs(windows.layouts) do
      win_layout:resize(args)
    end
  end)
  dapui.update_render({})
  if config.controls.enabled and config.controls.element ~= "" then
    controls.enable_controls(elements[config.controls.element])
  end
  controls.refresh_control_panel()
end

---@text
--- Access the elements currently registered. See elements corresponding help
--- tag for API information.
---
---@class dapui.elements
---@field hover dapui.elements.hover
---@field breakpoints dapui.elements.breakpoints
---@field repl dapui.elements.repl
---@field scopes dapui.elements.scopes
---@field stack dapui.elements.stacks
---@field watches dapui.elements.watches
---@field console dapui.elements.console
dapui.elements = setmetatable({}, {
  __newindex = function()
    error("Elements should be registered instead of adding them to the elements table")
  end,
  __index = function(_, key)
    return elements[key]
  end,
})

---@class dapui.Element
---@field render fun() Triggers the element to refresh its buffer. Used when
--- render settings have changed
---@field buffer fun(): integer Gets the current buffer for the element. The
--- buffer can change over repeated calls
---@field float_defaults? fun(): dapui.FloatElementArgs Default settings for
--- floating windows. Useful for element windows which should be larger than
--- their content
---@field allow_without_session boolean Allows floating the element when
--- there is no active debug session

--- Registers a new element that can be used within layouts or floating windows
---@param name string Name of the element
---@param element dapui.Element
function dapui.register_element(name, element)
  if elements[name] then
    error("Element " .. name .. " already exists")
  end
  elements[name] = element
  windows.register_element(name, element)
  nio.run(function()
    element.render()
  end)
end

return dapui
```

## File: `lua/dapui/util.lua`
```
local config = require("dapui.config")
local nio = require("nio")

local M = {}

local api = nio.api

local render_tasks = {}

function M.stop_render_tasks()
  for _, task in ipairs(render_tasks) do
    task.cancel()
  end
  render_tasks = {}
end

---@return function
function M.create_render_loop(render)
  local render_event = nio.control.event()

  render_tasks[#render_tasks + 1] = nio.run(function()
    while true do
      render_event.wait()
      render_event.clear()
      xpcall(render, function(msg)
        local traceback = debug.traceback(msg, 1)
        M.notify(("Rendering failed: %s"):format(traceback), vim.log.levels.WARN)
      end)
      nio.sleep(10)
    end
  end)

  return function()
    render_event.set()
  end
end

function M.get_current_expr()
  if nio.fn.mode() == "v" then
    local start = nio.fn.getpos("v")
    local finish = nio.fn.getpos(".")
    local lines = M.get_selection(start, finish)
    return table.concat(lines, "\n")
  end
  return nio.fn.expand("<cexpr>")
end

function M.create_buffer(name, options)
  local buf
  return function()
    if not buf then
      buf = name ~= "" and nio.fn.bufnr(name) or -1
    end
    if nio.api.nvim_buf_is_valid(buf) then
      return buf
    end
    buf = nio.api.nvim_create_buf(true, true)
    options = vim.tbl_extend("keep", options or {}, {
      modifiable = false,
      buflisted = false,
    })
    nio.api.nvim_buf_set_name(buf, name)
    for opt, value in pairs(options) do
      nio.api.nvim_buf_set_option(buf, opt, value)
    end
    return buf
  end
end

function M.round(num)
  if num < math.floor(num) + 0.5 then
    return math.floor(num)
  else
    return math.ceil(num)
  end
end

function M.notify(msg, level, opts)
  return vim.schedule_wrap(vim.notify)(
    msg,
    level or vim.log.levels.INFO,
    vim.tbl_extend("keep", opts or {}, {
      title = "nvim-dap-ui",
      icon = "",
      on_open = function(win)
        vim.api.nvim_buf_set_option(vim.api.nvim_win_get_buf(win), "filetype", "markdown")
      end,
    })
  )
end

function M.is_uri(path)
  local scheme = path:match("^([a-z]+)://.*")
  if scheme then
    return true
  else
    return false
  end
end

local function set_opts(win, opts)
  for opt, value in pairs(opts) do
    api.nvim_win_set_option(win, opt, value)
  end
end

function M.select_win()
  if config.select_window then
    return config.select_window()
  end
  local windows = vim.tbl_filter(function(win)
    if api.nvim_win_get_config(win).relative ~= "" then
      return false
    end
    local buf = api.nvim_win_get_buf(win)
    return api.nvim_buf_get_option(buf, "buftype") == ""
  end, api.nvim_tabpage_list_wins(0))

  if #windows < 2 then
    return windows[1]
  end

  local overwritten_opts = {}
  local laststatus = vim.o.laststatus
  vim.o.laststatus = 2

  for i, win in ipairs(windows) do
    overwritten_opts[win] = {
      statusline = api.nvim_win_get_option(win, "statusline"),
      winhl = api.nvim_win_get_option(win, "winhl"),
    }
    set_opts(win, {
      statusline = "%=" .. string.char(64 + i) .. "%=",
      winhl = ("StatusLine:%s,StatusLineNC:%s"):format("DapUIWinSelect", "DapUIWinSelect"),
    })
  end

  vim.cmd("redrawstatus!")
  local index, char
  local ESC, CTRL_C = 27, 22
  print("Select window: ")
  pcall(function()
    while char ~= ESC and char ~= CTRL_C and not windows[index] do
      char = vim.fn.getchar()
      if type(char) == "number" then
        if char >= 65 and char <= 90 then
          -- Upper to lower case
          char = char + 32
        end
        index = char - 96
      end
    end
  end)

  for win, opts in pairs(overwritten_opts) do
    pcall(set_opts, win, opts)
  end

  vim.o.laststatus = laststatus
  vim.cmd("normal! :")

  return windows[index]
end

function M.open_buf(bufnr, line, column)
  local function set_win_pos(win)
    if line then
      api.nvim_win_set_cursor(win, { line, column })
    end
    pcall(api.nvim_set_current_win, win)
  end

  for _, win in pairs(api.nvim_tabpage_list_wins(0)) do
    if api.nvim_win_get_buf(win) == bufnr then
      set_win_pos(win)
      return true
    end
  end

  local success, win = pcall(M.select_win)
  if not success or not win then
    return false
  end
  api.nvim_win_set_buf(win, bufnr)
  set_win_pos(win)
  return true
end

function M.get_selection(start, finish)
  local start_line, start_col = start[2], start[3]
  local finish_line, finish_col = finish[2], finish[3]

  if start_line > finish_line or (start_line == finish_line and start_col > finish_col) then
    start_line, start_col, finish_line, finish_col = finish_line, finish_col, start_line, start_col
  end

  local lines = vim.fn.getline(start_line, finish_line)
  if #lines == 0 then
    return
  end
  lines[#lines] = string.sub(lines[#lines], 1, finish_col)
  lines[1] = string.sub(lines[1], start_col)
  return lines
end

function M.apply_mapping(mappings, func, buffer, label)
  for _, key in pairs(mappings) do
    if type(func) ~= "string" then
      vim.api.nvim_buf_set_keymap(
        buffer,
        "n",
        key,
        "",
        { noremap = true, callback = func, nowait = true, desc = label }
      )
    else
      vim.api.nvim_buf_set_keymap(
        buffer,
        "n",
        key,
        func,
        { noremap = true, nowait = true, desc = label }
      )
    end
  end
end

function M.pretty_name(path)
  if M.is_uri(path) then
    path = vim.uri_to_fname(path)
  end
  return vim.fn.fnamemodify(path, ":t")
end

function M.format_error(error)
  if vim.tbl_isempty(error.body or {}) then
    return error.message
  end
  if not error.body.error then
    return error.body.message
  end
  local formatted = error.body.error.format
  for name, val in pairs(error.body.error.variables or {}) do
    formatted = string.gsub(formatted, "{" .. name .. "}", val)
  end
  return formatted
end

function M.partial(func, ...)
  local args = { ... }
  return function(...)
    local final = vim.list_extend(args, { ... })
    return func(unpack(final))
  end
end

function M.send_to_repl(expression)
  local repl_win = vim.fn.bufwinid("\\[dap-repl") -- incomplete bracket to allow e.g. '[dap-repl-2]'
  if repl_win == -1 then
    M.float_element("repl")
    repl_win = vim.fn.bufwinid("\\[dap-repl\\]")
  end
  api.nvim_set_current_win(repl_win)
  vim.cmd("normal i" .. expression)
end

function M.float_element(elem_name)
  local line_no = vim.fn.screenrow()
  local col_no = vim.fn.screencol()
  local position = { line = line_no, col = col_no }
  local elem = require("dapui.elements." .. elem_name)
  if type(elem) == "function" then elem = elem() end
  return require("dapui.windows").open_float(elem_name, elem, position, elem.settings or {})
end

function M.render_type(maybe_type)
  if not maybe_type then
    return ""
  end
  local max_length = config.render.max_type_length
  if not max_length or max_length == -1 then
    return maybe_type
  end
  if max_length == 0 then
    return ""
  end
  if vim.str_utfindex(maybe_type) <= max_length then
    return maybe_type
  end

  local byte_length = vim.str_byteindex(maybe_type, max_length)
  return string.sub(maybe_type, 1, byte_length) .. "..."
end

---@param value_start integer
---@param value string
---@return string[]
function M.format_value(value_start, value)
  local formatted = {}
  local max_lines = config.render.max_value_lines
  local i = 0
  --- Use gsplit instead of split because adapters can returns very long values
  --- and we want to avoid creating thousands of substrings that we won't use.
  for line in vim.gsplit(value, "\n") do
    i = i + 1

    if max_lines and i > max_lines then
      local line_count = 1
      for _ in value:gmatch("\n") do
        line_count = line_count + 1
      end

      formatted[i - 1] = formatted[i - 1] .. ((" ... [%s more lines]"):format(line_count - i + 1))
      break
    end
    if i > 1 then
      line = string.rep(" ", value_start - 2) .. line
    end
    formatted[i] = line
  end
  return formatted
end

function M.tbl_flatten(t)
  return vim.fn.has("nvim-0.10") == 1 and vim.iter(t):flatten(math.huge):totable()
    or vim.tbl_flatten(t)
end

return M
```

## File: `lua/dapui/client/dap_types.lua`
```
---nvim-dap internal representation of a breakpoint
---@class dapui.types.DAPBreakpoint
---@field line integer
---@field condition? string
---@field logMessage? string
---@field hitCondition? string
---@field state dapui.types.DAPBreakpointState

---@class dapui.types.DAPBreakpointState
---@field verified boolean If true, the breakpoint could be set (but not necessarily at the desired location).
---@field message? string A message about the state of the breakpoint. This is shown to the user and can be used to explain why a breakpoint could not be verified.
```

## File: `lua/dapui/client/init.lua`
```
local dap = require("dap")
local nio = require("nio")
local util = require("dapui.util")
local types = require("dapui.client.types")

---@alias dap.Session Session

---@class dapui.DAPClient
---@field request dapui.DAPRequestsClient
---@field listen dapui.DAPEventListenerClient
---@field session? dapui.SessionProxy
---@field lib dapui.DAPClientLib
---@field breakpoints dapui.BreakpointsProxy
local DAPUIClient = {}

---@class dapui.SessionProxy
---@field current_frame? dapui.types.StackFrame
---@field _frame_set fun(frame: dapui.types.StackFrame)
---@field stopped_thread_id integer
---@field capabilities dapui.types.Capabilities
---@field threads table<integer, dapui.types.Thread>

local proxied_session_keys = {}
for _, key in ipairs({
  "current_frame",
  "_frame_set",
  "stopped_thread_id",
  "capabilities",
  "threads",
}) do
  proxied_session_keys[key] = true
end

---@return dapui.SessionProxy
local function create_session_proxy(session)
  return setmetatable({}, {
    __index = function(_, key)
      if not proxied_session_keys[key] then
        return nil
      end
      local value = session[key]
      if type(value) == "function" then
        return function(...)
          return value(session, ...)
        end
      end
      return value
    end,
  })
end

---@class dapui.client.BreakpointArgs{
---@field condition? string
---@field hit_condition? string
---@field log_message? string

---@class dapui.BreakpointsProxy
---@field get fun(): table<integer, dapui.types.DAPBreakpoint[]>
---@field get_buf fun(bufnr: integer): dapui.types.DAPBreakpoint[]
---@field toggle fun(bufnr: integer, line: integer, args: dapui.client.BreakpointArgs)
---@field remove fun(bufnr: integer, line: integer)

---@return dapui.BreakpointsProxy
local function create_breakpoints_proxy(breakpoints, session_factory)
  local proxy = {}
  local function refresh(bufnr)
    local bps = breakpoints.get(bufnr)
    local session = session_factory()
    if session then
      session:set_breakpoints(bps)
    end
  end

  proxy.get = function()
    return breakpoints.get()
  end
  proxy.get_buf = function(bufnr)
    return breakpoints.get(bufnr)
  end
  proxy.toggle = function(bufnr, line, args)
    breakpoints.toggle(args, bufnr, line)
    refresh(bufnr)
  end
  proxy.remove = function(bufnr, line)
    breakpoints.remove(bufnr, line)
    refresh(bufnr)
  end
  return proxy
end

local Error = function(err, args)
  local err_tbl = vim.tbl_extend("keep", err, args or {})
  err_tbl.traceback = debug.traceback("test", 2)
  return setmetatable(err_tbl, {
    __tostring = function()
      local formatted = util.format_error(err)
      local message = ("DAP error: %s"):format(formatted)
      for name, value in pairs(args) do
        message = message
          .. ("\n%s: %s"):format(name, type(value) ~= "table" and value or vim.inspect(value))
      end
      message = message .. "\n" .. err_tbl.traceback
      return message
    end,
  })
end

---@param session_factory fun(): dap.Session
---@return dapui.DAPClient
local function create_client(session_factory, breakpoints)
  breakpoints = breakpoints or require("dap.breakpoints")
  local request_seqs = {}
  local async_request = nio.wrap(function(command, args, cb)
    local session = session_factory()
    request_seqs[session] = request_seqs[session] or {}
    request_seqs[session][session.seq] = true
    session:request(command, args, function(...)
      request_seqs[session][session.seq] = nil
      cb(...)
    end)
  end, 3)

  local request = setmetatable({}, {
    __index = function(_, command)
      return function(args)
        local start = vim.loop.now()
        local err, body = async_request(command, args)
        local diff = vim.loop.now() - start
        if err then
          error(Error(err, { command = command, args = args }))
        elseif body.error then
          error(Error(body.err, { command = command, args = args }))
        end
        return body
      end
    end,
  })

  local listener_prefix = "DAPClient" .. tostring(vim.loop.now())
  local listener_count = 0
  local listener_ids = {}
  local listen = setmetatable({}, {
    __index = function(_, event)
      return function(listener, opts)
        opts = opts or {}
        local listeners
        if opts.before then
          listeners = dap.listeners.before
        else
          listeners = dap.listeners.after
        end
        local listener_id = listener_prefix .. tostring(listener_count)
        listener_count = listener_count + 1
        local is_event = not types.request[event]
        local key = is_event and "event_" .. event or event
        listener_ids[#listener_ids + 1] = { key, listener_id }

        local wrap = function(inner)
          listeners[key][listener_id] = function(_, ...)
            if inner(...) then
              listeners[key][listener_id] = nil
            end
          end
        end

        if is_event then
          wrap(listener)
        else
          wrap(function(err, body, req, req_seq)
            if (request_seqs[session_factory()] or {})[req_seq] then
              return
            end
            return listener({ error = err, response = body, request = req })
          end)
        end
      end
    end,
  })

  local client = setmetatable({
    breakpoints = create_breakpoints_proxy(breakpoints, session_factory),
    request = request,
    listen = listen,
    shutdown = function()
      for _, listener in ipairs(listener_ids) do
        dap.listeners.before[listener[1]][listener[2]] = nil
        dap.listeners.after[listener[1]][listener[2]] = nil
      end
    end,
  }, {
    __index = function(_, key)
      if key == "session" then
        local session = session_factory()
        if not session then
          return nil
        end
        return create_session_proxy(session)
      end
    end,
  })
  client.lib = require("dapui.client.lib")(client)
  return client
end

return create_client
```

## File: `lua/dapui/client/lib.lua`
```
local util = require("dapui.util")
local nio = require("nio")

---@param client dapui.DAPClient
return function(client)
  ---@class dapui.DAPClientLib
  local client_lib = {}

  ---@param frame dapui.types.StackFrame
  ---@param set_frame boolean Set the current frame of session to given frame
  function client_lib.jump_to_frame(frame, set_frame)
    local opened = (function()
      local line = frame.line
      local column = frame.column
      local source = frame.source
      if not source then
        return
      end

      if (source.sourceReference or 0) > 0 then
        local buf = nio.api.nvim_create_buf(false, true)
        local response = client.request.source({ sourceReference = source.sourceReference })
        if not response.content then
          util.notify("No source available for frame", vim.log.levels.WARN)
          return
        end
        nio.api.nvim_buf_set_lines(buf, 0, 0, true, vim.split(response.content, "\n"))
        nio.api.nvim_buf_set_option(buf, "bufhidden", "delete")
        nio.api.nvim_buf_set_option(buf, "modifiable", false)
        return util.open_buf(buf, line, column)
      end

      if not source.path or not vim.uv.fs_stat(source.path) then
        util.notify("No source available for frame", vim.log.levels.WARN)
        return
      end

      local path = source.path

      if not column or column == 0 then
        column = 1
      end

      local bufnr = vim.uri_to_bufnr(
        util.is_uri(path) and path or vim.uri_from_fname(vim.fn.fnamemodify(path, ":p"))
      )
      nio.fn.bufload(bufnr)
      return util.open_buf(bufnr, line, column)
    end)()
    if opened and set_frame then
      client.session._frame_set(frame)
    end
  end

  ---@param variable dapui.types.Variable
  function client_lib.set_variable(container_ref, variable, value)
    local ok, err = pcall(function()
      if client.session.capabilities.supportsSetExpression and variable.evaluateName then
        local frame_id = client.session.current_frame and client.session.current_frame.id
        client.request.setExpression({
          expression = variable.evaluateName,
          value = value,
          frameId = frame_id,
        })
      elseif client.session.capabilities.supportsSetVariable and container_ref then
        client.request.setVariable({
          variablesReference = container_ref,
          name = variable.name,
          value = value,
        })
      else
        util.notify(
          "Debug server doesn't support setting " .. (variable.evaluateName or variable.name),
          vim.log.levels.WARN
        )
      end
    end)
    if not ok then
      util.notify(util.format_error(err))
    end
  end

  local stop_count = 0
  client.listen.stopped(function()
    stop_count = stop_count + 1
  end)
  client.listen.initialized(function()
    stop_count = 0
  end)

  ---@return integer: The number of times the debugger has stopped
  function client_lib.step_number()
    return stop_count
  end

  return client_lib
end
```

## File: `lua/dapui/client/types.lua`
```
--- Generated on 2023-05-13 08:57:30.479445

---@class dapui.DAPRequestsClient
local DAPUIRequestsClient = {}

---@class dapui.DAPEventListenerClient
local DAPUIEventListenerClient = {}

---@class dapui.client.ListenerOpts
---@field before boolean Run before event/request is processed by nvim-dap
--- Arguments for `attach` request. Additional attributes are implementation specific.
---@class dapui.types.AttachRequestArguments
---@field field__restart? any[] | boolean | integer | number | table<string,any> | string Arbitrary data from the previous, restarted session. The data is sent as the `restart` attribute of the `terminated` event. The client should leave the data intact.

--- The `attach` request is sent from the client to the debug adapter to attach to a debuggee that is already running.
--- Since attaching is debugger/runtime specific, the arguments for this request are not part of this specification.
---@async
---@param args dapui.types.AttachRequestArguments
function DAPUIRequestsClient.attach(args) end

---@class dapui.types.attachRequestListenerArgs
---@field request dapui.types.AttachRequestArguments
---@field error? table

---@param listener fun(args: dapui.types.attachRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.attach(listener, opts) end

--- The checksum of an item calculated by the specified algorithm.
---@class dapui.types.Checksum
---@field algorithm "MD5"|"SHA1"|"SHA256"|"timestamp" The algorithm used to calculate this checksum.
---@field checksum string Value of the checksum, encoded as a hexadecimal value.

--- A `Source` is a descriptor for source code.
--- It is returned from the debug adapter as part of a `StackFrame` and it is used by clients when specifying breakpoints.
---@class dapui.types.Source
---@field name? string The short name of the source. Every source returned from the debug adapter has a name. When sending a source to the debug adapter this name is optional.
---@field path? string The path of the source to be shown in the UI. It is only used to locate and load the content of the source if no `sourceReference` is specified (or its value is 0).
---@field sourceReference? integer If the value > 0 the contents of the source must be retrieved through the `source` request (even if a path is specified). Since a `sourceReference` is only valid for a session, it can not be used to persist a source. The value should be less than or equal to 2147483647 (2^31-1).
---@field presentationHint? "normal"|"emphasize"|"deemphasize" A hint for how to present the source in the UI. A value of `deemphasize` can be used to indicate that the source is not available or that it is skipped on stepping.
---@field origin? string The origin of this source. For example, 'internal module', 'inlined content from source map', etc.
---@field sources? dapui.types.Source[] A list of sources that are related to this source. These may be the source that generated this source.
---@field adapterData? any[] | boolean | integer | number | table<string,any> | string Additional data that a debug adapter might want to loop through the client. The client should leave the data intact and persist it across sessions. The client should not interpret the data.
---@field checksums? dapui.types.Checksum[] The checksums associated with this file.

--- Arguments for `breakpointLocations` request.
---@class dapui.types.BreakpointLocationsArguments
---@field source dapui.types.Source The source location of the breakpoints; either `source.path` or `source.reference` must be specified.
---@field line integer Start line of range to search possible breakpoint locations in. If only the line is specified, the request returns all possible locations in that line.
---@field column? integer Start position within `line` to search possible breakpoint locations in. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based. If no column is given, the first position in the start line is assumed.
---@field endLine? integer End line of range to search possible breakpoint locations in. If no end line is given, then the end line is assumed to be the start line.
---@field endColumn? integer End position within `endLine` to search possible breakpoint locations in. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based. If no end column is given, the last position in the end line is assumed.

--- Properties of a breakpoint location returned from the `breakpointLocations` request.
---@class dapui.types.BreakpointLocation
---@field line integer Start line of breakpoint location.
---@field column? integer The start position of a breakpoint location. Position is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field endLine? integer The end line of breakpoint location if the location covers a range.
---@field endColumn? integer The end position of a breakpoint location (if the location covers a range). Position is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.

---@class dapui.types.BreakpointLocationsResponse
---@field breakpoints dapui.types.BreakpointLocation[] Sorted set of possible breakpoint locations.

--- The `breakpointLocations` request returns all possible locations for source breakpoints in a given range.
--- Clients should only call this request if the corresponding capability `supportsBreakpointLocationsRequest` is true.
---@async
---@param args dapui.types.BreakpointLocationsArguments
---@return dapui.types.BreakpointLocationsResponse
function DAPUIRequestsClient.breakpointLocations(args) end

---@class dapui.types.breakpointLocationsRequestListenerArgs
---@field request dapui.types.BreakpointLocationsArguments
---@field error? table
---@field response dapui.types.BreakpointLocationsResponse

---@param listener fun(args: dapui.types.breakpointLocationsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.breakpointLocations(listener, opts) end

--- Arguments for `cancel` request.
---@class dapui.types.CancelArguments
---@field requestId? integer The ID (attribute `seq`) of the request to cancel. If missing no request is cancelled. Both a `requestId` and a `progressId` can be specified in one request.
---@field progressId? string The ID (attribute `progressId`) of the progress to cancel. If missing no progress is cancelled. Both a `requestId` and a `progressId` can be specified in one request.

--- The `cancel` request is used by the client in two situations:
--- - to indicate that it is no longer interested in the result produced by a specific request issued earlier
--- - to cancel a progress sequence. Clients should only call this request if the corresponding capability `supportsCancelRequest` is true.
--- This request has a hint characteristic: a debug adapter can only be expected to make a 'best effort' in honoring this request but there are no guarantees.
--- The `cancel` request may return an error if it could not cancel an operation but a client should refrain from presenting this error to end users.
--- The request that got cancelled still needs to send a response back. This can either be a normal result (`success` attribute true) or an error response (`success` attribute false and the `message` set to `cancelled`).
--- Returning partial results from a cancelled request is possible but please note that a client has no generic way for detecting that a response is partial or not.
--- The progress that got cancelled still needs to send a `progressEnd` event back.
--- A client should not assume that progress just got cancelled after sending the `cancel` request.
---@async
---@param args dapui.types.CancelArguments
function DAPUIRequestsClient.cancel(args) end

---@class dapui.types.cancelRequestListenerArgs
---@field request dapui.types.CancelArguments
---@field error? table

---@param listener fun(args: dapui.types.cancelRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.cancel(listener, opts) end

--- Arguments for `completions` request.
---@class dapui.types.CompletionsArguments
---@field frameId? integer Returns completions in the scope of this stack frame. If not specified, the completions are returned for the global scope.
---@field text string One or more source lines. Typically this is the text users have typed into the debug console before they asked for completion.
---@field column integer The position within `text` for which to determine the completion proposals. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field line? integer A line for which to determine the completion proposals. If missing the first line of the text is assumed.

--- `CompletionItems` are the suggestions returned from the `completions` request.
---@class dapui.types.CompletionItem
---@field label string The label of this completion item. By default this is also the text that is inserted when selecting this completion.
---@field text? string If text is returned and not an empty string, then it is inserted instead of the label.
---@field sortText? string A string that should be used when comparing this item with other items. If not returned or an empty string, the `label` is used instead.
---@field detail? string A human-readable string with additional information about this item, like type or symbol information.
---@field type? "method"|"function"|"constructor"|"field"|"variable"|"class"|"interface"|"module"|"property"|"unit"|"value"|"enum"|"keyword"|"snippet"|"text"|"color"|"file"|"reference"|"customcolor" The item's type. Typically the client uses this information to render the item in the UI with an icon.
---@field start? integer Start position (within the `text` attribute of the `completions` request) where the completion text is added. The position is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based. If the start position is omitted the text is added at the location specified by the `column` attribute of the `completions` request.
---@field length? integer Length determines how many characters are overwritten by the completion text and it is measured in UTF-16 code units. If missing the value 0 is assumed which results in the completion text being inserted.
---@field selectionStart? integer Determines the start of the new selection after the text has been inserted (or replaced). `selectionStart` is measured in UTF-16 code units and must be in the range 0 and length of the completion text. If omitted the selection starts at the end of the completion text.
---@field selectionLength? integer Determines the length of the new selection after the text has been inserted (or replaced) and it is measured in UTF-16 code units. The selection can not extend beyond the bounds of the completion text. If omitted the length is assumed to be 0.

---@class dapui.types.CompletionsResponse
---@field targets dapui.types.CompletionItem[] The possible completions for .

--- Returns a list of possible completions for a given caret position and text.
--- Clients should only call this request if the corresponding capability `supportsCompletionsRequest` is true.
---@async
---@param args dapui.types.CompletionsArguments
---@return dapui.types.CompletionsResponse
function DAPUIRequestsClient.completions(args) end

---@class dapui.types.completionsRequestListenerArgs
---@field request dapui.types.CompletionsArguments
---@field error? table
---@field response dapui.types.CompletionsResponse

---@param listener fun(args: dapui.types.completionsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.completions(listener, opts) end

--- Arguments for `configurationDone` request.
---@class dapui.types.ConfigurationDoneArguments

--- This request indicates that the client has finished initialization of the debug adapter.
--- So it is the last request in the sequence of configuration requests (which was started by the `initialized` event).
--- Clients should only call this request if the corresponding capability `supportsConfigurationDoneRequest` is true.
---@async
---@param args dapui.types.ConfigurationDoneArguments
function DAPUIRequestsClient.configurationDone(args) end

---@class dapui.types.configurationDoneRequestListenerArgs
---@field request dapui.types.ConfigurationDoneArguments
---@field error? table

---@param listener fun(args: dapui.types.configurationDoneRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.configurationDone(listener, opts) end

--- Arguments for `continue` request.
---@class dapui.types.ContinueArguments
---@field threadId integer Specifies the active thread. If the debug adapter supports single thread execution (see `supportsSingleThreadExecutionRequests`) and the argument `singleThread` is true, only the thread with this ID is resumed.
---@field singleThread? boolean If this flag is true, execution is resumed only for the thread with given `threadId`.

---@class dapui.types.ContinueResponse
---@field allThreadsContinued? boolean The value true (or a missing property) signals to the client that all threads have been resumed. The value false indicates that not all threads were resumed.

--- The request resumes execution of all threads. If the debug adapter supports single thread execution (see capability `supportsSingleThreadExecutionRequests`), setting the `singleThread` argument to true resumes only the specified thread. If not all threads were resumed, the `allThreadsContinued` attribute of the response should be set to false.
---@async
---@param args dapui.types.ContinueArguments
---@return dapui.types.ContinueResponse
function DAPUIRequestsClient.continue_(args) end

---@class dapui.types.continue_RequestListenerArgs
---@field request dapui.types.ContinueArguments
---@field error? table
---@field response dapui.types.ContinueResponse

---@param listener fun(args: dapui.types.continue_RequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.continue_(listener, opts) end

--- Arguments for `dataBreakpointInfo` request.
---@class dapui.types.DataBreakpointInfoArguments
---@field variablesReference? integer Reference to the variable container if the data breakpoint is requested for a child of the container. The `variablesReference` must have been obtained in the current suspended state. See 'Lifetime of Object References' in the Overview section for details.
---@field name string The name of the variable's child to obtain data breakpoint information for. If `variablesReference` isn't specified, this can be an expression.
---@field frameId? integer When `name` is an expression, evaluate it in the scope of this stack frame. If not specified, the expression is evaluated in the global scope. When `variablesReference` is specified, this property has no effect.

---@class dapui.types.DataBreakpointInfoResponse
---@field dataId string An identifier for the data on which a data breakpoint can be registered with the `setDataBreakpoints` request or null if no data breakpoint is available.
---@field description string UI string that describes on what data the breakpoint is set on or why a data breakpoint is not available.
---@field accessTypes? "read"|"write"|"readWrite"[] Attribute lists the available access types for a potential data breakpoint. A UI client could surface this information.
---@field canPersist? boolean Attribute indicates that a potential data breakpoint could be persisted across sessions.

--- Obtains information on a possible data breakpoint that could be set on an expression or variable.
--- Clients should only call this request if the corresponding capability `supportsDataBreakpoints` is true.
---@async
---@param args dapui.types.DataBreakpointInfoArguments
---@return dapui.types.DataBreakpointInfoResponse
function DAPUIRequestsClient.dataBreakpointInfo(args) end

---@class dapui.types.dataBreakpointInfoRequestListenerArgs
---@field request dapui.types.DataBreakpointInfoArguments
---@field error? table
---@field response dapui.types.DataBreakpointInfoResponse

---@param listener fun(args: dapui.types.dataBreakpointInfoRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.dataBreakpointInfo(listener, opts) end

--- Arguments for `disassemble` request.
---@class dapui.types.DisassembleArguments
---@field memoryReference string Memory reference to the base location containing the instructions to disassemble.
---@field offset? integer Offset (in bytes) to be applied to the reference location before disassembling. Can be negative.
---@field instructionOffset? integer Offset (in instructions) to be applied after the byte offset (if any) before disassembling. Can be negative.
---@field instructionCount integer Number of instructions to disassemble starting at the specified location and offset. An adapter must return exactly this number of instructions - any unavailable instructions should be replaced with an implementation-defined 'invalid instruction' value.
---@field resolveSymbols? boolean If true, the adapter should attempt to resolve memory addresses and other values to symbolic names.

--- Represents a single disassembled instruction.
---@class dapui.types.DisassembledInstruction
---@field address string The address of the instruction. Treated as a hex value if prefixed with `0x`, or as a decimal value otherwise.
---@field instructionBytes? string Raw bytes representing the instruction and its operands, in an implementation-defined format.
---@field instruction string Text representing the instruction and its operands, in an implementation-defined format.
---@field symbol? string Name of the symbol that corresponds with the location of this instruction, if any.
---@field location? dapui.types.Source Source location that corresponds to this instruction, if any. Should always be set (if available) on the first instruction returned, but can be omitted afterwards if this instruction maps to the same source file as the previous instruction.
---@field line? integer The line within the source location that corresponds to this instruction, if any.
---@field column? integer The column within the line that corresponds to this instruction, if any.
---@field endLine? integer The end line of the range that corresponds to this instruction, if any.
---@field endColumn? integer The end column of the range that corresponds to this instruction, if any.

---@class dapui.types.DisassembleResponse
---@field instructions dapui.types.DisassembledInstruction[] The list of disassembled instructions.

--- Disassembles code stored at the provided location.
--- Clients should only call this request if the corresponding capability `supportsDisassembleRequest` is true.
---@async
---@param args dapui.types.DisassembleArguments
---@return dapui.types.DisassembleResponse
function DAPUIRequestsClient.disassemble(args) end

---@class dapui.types.disassembleRequestListenerArgs
---@field request dapui.types.DisassembleArguments
---@field error? table
---@field response dapui.types.DisassembleResponse

---@param listener fun(args: dapui.types.disassembleRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.disassemble(listener, opts) end

--- Arguments for `disconnect` request.
---@class dapui.types.DisconnectArguments
---@field restart? boolean A value of true indicates that this `disconnect` request is part of a restart sequence.
---@field terminateDebuggee? boolean Indicates whether the debuggee should be terminated when the debugger is disconnected. If unspecified, the debug adapter is free to do whatever it thinks is best. The attribute is only honored by a debug adapter if the corresponding capability `supportTerminateDebuggee` is true.
---@field suspendDebuggee? boolean Indicates whether the debuggee should stay suspended when the debugger is disconnected. If unspecified, the debuggee should resume execution. The attribute is only honored by a debug adapter if the corresponding capability `supportSuspendDebuggee` is true.

--- The `disconnect` request asks the debug adapter to disconnect from the debuggee (thus ending the debug session) and then to shut down itself (the debug adapter).
--- In addition, the debug adapter must terminate the debuggee if it was started with the `launch` request. If an `attach` request was used to connect to the debuggee, then the debug adapter must not terminate the debuggee.
--- This implicit behavior of when to terminate the debuggee can be overridden with the `terminateDebuggee` argument (which is only supported by a debug adapter if the corresponding capability `supportTerminateDebuggee` is true).
---@async
---@param args dapui.types.DisconnectArguments
function DAPUIRequestsClient.disconnect(args) end

---@class dapui.types.disconnectRequestListenerArgs
---@field request dapui.types.DisconnectArguments
---@field error? table

---@param listener fun(args: dapui.types.disconnectRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.disconnect(listener, opts) end

--- Provides formatting information for a value.
---@class dapui.types.ValueFormat
---@field hex? boolean Display the value in hex.

--- Arguments for `evaluate` request.
---@class dapui.types.EvaluateArguments
---@field expression string The expression to evaluate.
---@field frameId? integer Evaluate the expression in the scope of this stack frame. If not specified, the expression is evaluated in the global scope.
---@field context? string The context in which the evaluate request is used.
---@field format? dapui.types.ValueFormat Specifies details on how to format the result. The attribute is only honored by a debug adapter if the corresponding capability `supportsValueFormattingOptions` is true.

--- Properties of a variable that can be used to determine how to render the variable in the UI.
---@class dapui.types.VariablePresentationHint
---@field kind? string The kind of variable. Before introducing additional values, try to use the listed values.
---@field attributes? string[] Set of attributes represented as an array of strings. Before introducing additional values, try to use the listed values.
---@field visibility? string Visibility of variable. Before introducing additional values, try to use the listed values.
---@field lazy? boolean If true, clients can present the variable with a UI that supports a specific gesture to trigger its evaluation. This mechanism can be used for properties that require executing code when retrieving their value and where the code execution can be expensive and/or produce side-effects. A typical example are properties based on a getter function. Please note that in addition to the `lazy` flag, the variable's `variablesReference` is expected to refer to a variable that will provide the value through another `variable` request.

---@class dapui.types.EvaluateResponse
---@field result string The result of the evaluate request.
---@field type? string The type of the evaluate result. This attribute should only be returned by a debug adapter if the corresponding capability `supportsVariableType` is true.
---@field presentationHint? dapui.types.VariablePresentationHint Properties of an evaluate result that can be used to determine how to render the result in the UI.
---@field variablesReference integer If `variablesReference` is > 0, the evaluate result is structured and its children can be retrieved by passing `variablesReference` to the `variables` request as long as execution remains suspended. See 'Lifetime of Object References' in the Overview section for details.
---@field namedVariables? integer The number of named child variables. The client can use this information to present the variables in a paged UI and fetch them in chunks. The value should be less than or equal to 2147483647 (2^31-1).
---@field indexedVariables? integer The number of indexed child variables. The client can use this information to present the variables in a paged UI and fetch them in chunks. The value should be less than or equal to 2147483647 (2^31-1).
---@field memoryReference? string A memory reference to a location appropriate for this result. For pointer type eval results, this is generally a reference to the memory address contained in the pointer. This attribute should be returned by a debug adapter if corresponding capability `supportsMemoryReferences` is true.

--- Evaluates the given expression in the context of the topmost stack frame.
--- The expression has access to any variables and arguments that are in scope.
---@async
---@param args dapui.types.EvaluateArguments
---@return dapui.types.EvaluateResponse
function DAPUIRequestsClient.evaluate(args) end

---@class dapui.types.evaluateRequestListenerArgs
---@field request dapui.types.EvaluateArguments
---@field error? table
---@field response dapui.types.EvaluateResponse

---@param listener fun(args: dapui.types.evaluateRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.evaluate(listener, opts) end

--- Arguments for `exceptionInfo` request.
---@class dapui.types.ExceptionInfoArguments
---@field threadId integer Thread for which exception information should be retrieved.

--- Detailed information about an exception that has occurred.
---@class dapui.types.ExceptionDetails
---@field message? string Message contained in the exception.
---@field typeName? string Short type name of the exception object.
---@field fullTypeName? string Fully-qualified type name of the exception object.
---@field evaluateName? string An expression that can be evaluated in the current scope to obtain the exception object.
---@field stackTrace? string Stack trace at the time the exception was thrown.
---@field innerException? dapui.types.ExceptionDetails[] Details of the exception contained by this exception, if any.

---@class dapui.types.ExceptionInfoResponse
---@field exceptionId string ID of the exception that was thrown.
---@field description? string Descriptive text for the exception.
---@field breakMode "never"|"always"|"unhandled"|"userUnhandled" Mode that caused the exception notification to be raised.
---@field details? dapui.types.ExceptionDetails Detailed information about the exception.

--- Retrieves the details of the exception that caused this event to be raised.
--- Clients should only call this request if the corresponding capability `supportsExceptionInfoRequest` is true.
---@async
---@param args dapui.types.ExceptionInfoArguments
---@return dapui.types.ExceptionInfoResponse
function DAPUIRequestsClient.exceptionInfo(args) end

---@class dapui.types.exceptionInfoRequestListenerArgs
---@field request dapui.types.ExceptionInfoArguments
---@field error? table
---@field response dapui.types.ExceptionInfoResponse

---@param listener fun(args: dapui.types.exceptionInfoRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.exceptionInfo(listener, opts) end

--- Arguments for `goto` request.
---@class dapui.types.GotoArguments
---@field threadId integer Set the goto target for this thread.
---@field targetId integer The location where the debuggee will continue to run.

--- The request sets the location where the debuggee will continue to run.
--- This makes it possible to skip the execution of code or to execute code again.
--- The code between the current location and the goto target is not executed but skipped.
--- The debug adapter first sends the response and then a `stopped` event with reason `goto`.
--- Clients should only call this request if the corresponding capability `supportsGotoTargetsRequest` is true (because only then goto targets exist that can be passed as arguments).
---@async
---@param args dapui.types.GotoArguments
function DAPUIRequestsClient.goto_(args) end

---@class dapui.types.gotoRequestListenerArgs
---@field request dapui.types.GotoArguments
---@field error? table

---@param listener fun(args: dapui.types.gotoRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.goto_(listener, opts) end

--- Arguments for `gotoTargets` request.
---@class dapui.types.GotoTargetsArguments
---@field source dapui.types.Source The source location for which the goto targets are determined.
---@field line integer The line location for which the goto targets are determined.
---@field column? integer The position within `line` for which the goto targets are determined. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.

--- A `GotoTarget` describes a code location that can be used as a target in the `goto` request.
--- The possible goto targets can be determined via the `gotoTargets` request.
---@class dapui.types.GotoTarget
---@field id integer Unique identifier for a goto target. This is used in the `goto` request.
---@field label string The name of the goto target (shown in the UI).
---@field line integer The line of the goto target.
---@field column? integer The column of the goto target.
---@field endLine? integer The end line of the range covered by the goto target.
---@field endColumn? integer The end column of the range covered by the goto target.
---@field instructionPointerReference? string A memory reference for the instruction pointer value represented by this target.

---@class dapui.types.GotoTargetsResponse
---@field targets dapui.types.GotoTarget[] The possible goto targets of the specified location.

--- This request retrieves the possible goto targets for the specified source location.
--- These targets can be used in the `goto` request.
--- Clients should only call this request if the corresponding capability `supportsGotoTargetsRequest` is true.
---@async
---@param args dapui.types.GotoTargetsArguments
---@return dapui.types.GotoTargetsResponse
function DAPUIRequestsClient.gotoTargets(args) end

---@class dapui.types.gotoTargetsRequestListenerArgs
---@field request dapui.types.GotoTargetsArguments
---@field error? table
---@field response dapui.types.GotoTargetsResponse

---@param listener fun(args: dapui.types.gotoTargetsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.gotoTargets(listener, opts) end

--- Arguments for `initialize` request.
---@class dapui.types.InitializeRequestArguments
---@field clientID? string The ID of the client using this adapter.
---@field clientName? string The human-readable name of the client using this adapter.
---@field adapterID string The ID of the debug adapter.
---@field locale? string The ISO-639 locale of the client using this adapter, e.g. en-US or de-CH.
---@field linesStartAt1? boolean If true all line numbers are 1-based (default).
---@field columnsStartAt1? boolean If true all column numbers are 1-based (default).
---@field pathFormat? string Determines in what format paths are specified. The default is `path`, which is the native format.
---@field supportsVariableType? boolean Client supports the `type` attribute for variables.
---@field supportsVariablePaging? boolean Client supports the paging of variables.
---@field supportsRunInTerminalRequest? boolean Client supports the `runInTerminal` request.
---@field supportsMemoryReferences? boolean Client supports memory references.
---@field supportsProgressReporting? boolean Client supports progress reporting.
---@field supportsInvalidatedEvent? boolean Client supports the `invalidated` event.
---@field supportsMemoryEvent? boolean Client supports the `memory` event.
---@field supportsArgsCanBeInterpretedByShell? boolean Client supports the `argsCanBeInterpretedByShell` attribute on the `runInTerminal` request.
---@field supportsStartDebuggingRequest? boolean Client supports the `startDebugging` request.

--- An `ExceptionBreakpointsFilter` is shown in the UI as an filter option for configuring how exceptions are dealt with.
---@class dapui.types.ExceptionBreakpointsFilter
---@field filter string The internal ID of the filter option. This value is passed to the `setExceptionBreakpoints` request.
---@field label string The name of the filter option. This is shown in the UI.
---@field description? string A help text providing additional information about the exception filter. This string is typically shown as a hover and can be translated.
---@field default? boolean Initial value of the filter option. If not specified a value false is assumed.
---@field supportsCondition? boolean Controls whether a condition can be specified for this filter option. If false or missing, a condition can not be set.
---@field conditionDescription? string A help text providing information about the condition. This string is shown as the placeholder text for a text box and can be translated.

--- A `ColumnDescriptor` specifies what module attribute to show in a column of the modules view, how to format it,
--- and what the column's label should be.
--- It is only used if the underlying UI actually supports this level of customization.
---@class dapui.types.ColumnDescriptor
---@field attributeName string Name of the attribute rendered in this column.
---@field label string Header UI label of column.
---@field format? string Format to use for the rendered values in this column. TBD how the format strings looks like.
---@field type? "string"|"number"|"boolean"|"unixTimestampUTC" Datatype of values in this column. Defaults to `string` if not specified.
---@field width? integer Width of this column in characters (hint only).

--- Information about the capabilities of a debug adapter.
---@class dapui.types.InitializeResponse
---@field supportsConfigurationDoneRequest? boolean The debug adapter supports the `configurationDone` request.
---@field supportsFunctionBreakpoints? boolean The debug adapter supports function breakpoints.
---@field supportsConditionalBreakpoints? boolean The debug adapter supports conditional breakpoints.
---@field supportsHitConditionalBreakpoints? boolean The debug adapter supports breakpoints that break execution after a specified number of hits.
---@field supportsEvaluateForHovers? boolean The debug adapter supports a (side effect free) `evaluate` request for data hovers.
---@field exceptionBreakpointFilters? dapui.types.ExceptionBreakpointsFilter[] Available exception filter options for the `setExceptionBreakpoints` request.
---@field supportsStepBack? boolean The debug adapter supports stepping back via the `stepBack` and `reverseContinue` requests.
---@field supportsSetVariable? boolean The debug adapter supports setting a variable to a value.
---@field supportsRestartFrame? boolean The debug adapter supports restarting a frame.
---@field supportsGotoTargetsRequest? boolean The debug adapter supports the `gotoTargets` request.
---@field supportsStepInTargetsRequest? boolean The debug adapter supports the `stepInTargets` request.
---@field supportsCompletionsRequest? boolean The debug adapter supports the `completions` request.
---@field completionTriggerCharacters? string[] The set of characters that should trigger completion in a REPL. If not specified, the UI should assume the `.` character.
---@field supportsModulesRequest? boolean The debug adapter supports the `modules` request.
---@field additionalModuleColumns? dapui.types.ColumnDescriptor[] The set of additional module information exposed by the debug adapter.
---@field supportedChecksumAlgorithms? "MD5"|"SHA1"|"SHA256"|"timestamp"[] Checksum algorithms supported by the debug adapter.
---@field supportsRestartRequest? boolean The debug adapter supports the `restart` request. In this case a client should not implement `restart` by terminating and relaunching the adapter but by calling the `restart` request.
---@field supportsExceptionOptions? boolean The debug adapter supports `exceptionOptions` on the `setExceptionBreakpoints` request.
---@field supportsValueFormattingOptions? boolean The debug adapter supports a `format` attribute on the `stackTrace`, `variables`, and `evaluate` requests.
---@field supportsExceptionInfoRequest? boolean The debug adapter supports the `exceptionInfo` request.
---@field supportTerminateDebuggee? boolean The debug adapter supports the `terminateDebuggee` attribute on the `disconnect` request.
---@field supportSuspendDebuggee? boolean The debug adapter supports the `suspendDebuggee` attribute on the `disconnect` request.
---@field supportsDelayedStackTraceLoading? boolean The debug adapter supports the delayed loading of parts of the stack, which requires that both the `startFrame` and `levels` arguments and the `totalFrames` result of the `stackTrace` request are supported.
---@field supportsLoadedSourcesRequest? boolean The debug adapter supports the `loadedSources` request.
---@field supportsLogPoints? boolean The debug adapter supports log points by interpreting the `logMessage` attribute of the `SourceBreakpoint`.
---@field supportsTerminateThreadsRequest? boolean The debug adapter supports the `terminateThreads` request.
---@field supportsSetExpression? boolean The debug adapter supports the `setExpression` request.
---@field supportsTerminateRequest? boolean The debug adapter supports the `terminate` request.
---@field supportsDataBreakpoints? boolean The debug adapter supports data breakpoints.
---@field supportsReadMemoryRequest? boolean The debug adapter supports the `readMemory` request.
---@field supportsWriteMemoryRequest? boolean The debug adapter supports the `writeMemory` request.
---@field supportsDisassembleRequest? boolean The debug adapter supports the `disassemble` request.
---@field supportsCancelRequest? boolean The debug adapter supports the `cancel` request.
---@field supportsBreakpointLocationsRequest? boolean The debug adapter supports the `breakpointLocations` request.
---@field supportsClipboardContext? boolean The debug adapter supports the `clipboard` context value in the `evaluate` request.
---@field supportsSteppingGranularity? boolean The debug adapter supports stepping granularities (argument `granularity`) for the stepping requests.
---@field supportsInstructionBreakpoints? boolean The debug adapter supports adding breakpoints based on instruction references.
---@field supportsExceptionFilterOptions? boolean The debug adapter supports `filterOptions` as an argument on the `setExceptionBreakpoints` request.
---@field supportsSingleThreadExecutionRequests? boolean The debug adapter supports the `singleThread` property on the execution requests (`continue`, `next`, `stepIn`, `stepOut`, `reverseContinue`, `stepBack`).

--- The `initialize` request is sent as the first request from the client to the debug adapter in order to configure it with client capabilities and to retrieve capabilities from the debug adapter.
--- Until the debug adapter has responded with an `initialize` response, the client must not send any additional requests or events to the debug adapter.
--- In addition the debug adapter is not allowed to send any requests or events to the client until it has responded with an `initialize` response.
--- The `initialize` request may only be sent once.
---@async
---@param args dapui.types.InitializeRequestArguments
---@return dapui.types.InitializeResponse
function DAPUIRequestsClient.initialize(args) end

---@class dapui.types.initializeRequestListenerArgs
---@field request dapui.types.InitializeRequestArguments
---@field error? table
---@field response dapui.types.InitializeResponse

---@param listener fun(args: dapui.types.initializeRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.initialize(listener, opts) end

--- Arguments for `launch` request. Additional attributes are implementation specific.
---@class dapui.types.LaunchRequestArguments
---@field noDebug? boolean If true, the launch request should launch the program without enabling debugging.
---@field field__restart? any[] | boolean | integer | number | table<string,any> | string Arbitrary data from the previous, restarted session. The data is sent as the `restart` attribute of the `terminated` event. The client should leave the data intact.

--- This launch request is sent from the client to the debug adapter to start the debuggee with or without debugging (if `noDebug` is true).
--- Since launching is debugger/runtime specific, the arguments for this request are not part of this specification.
---@async
---@param args dapui.types.LaunchRequestArguments
function DAPUIRequestsClient.launch(args) end

---@class dapui.types.launchRequestListenerArgs
---@field request dapui.types.LaunchRequestArguments
---@field error? table

---@param listener fun(args: dapui.types.launchRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.launch(listener, opts) end

--- Arguments for `loadedSources` request.
---@class dapui.types.LoadedSourcesArguments

---@class dapui.types.LoadedSourcesResponse
---@field sources dapui.types.Source[] Set of loaded sources.

--- Retrieves the set of all sources currently loaded by the debugged process.
--- Clients should only call this request if the corresponding capability `supportsLoadedSourcesRequest` is true.
---@async
---@param args dapui.types.LoadedSourcesArguments
---@return dapui.types.LoadedSourcesResponse
function DAPUIRequestsClient.loadedSources(args) end

---@class dapui.types.loadedSourcesRequestListenerArgs
---@field request dapui.types.LoadedSourcesArguments
---@field error? table
---@field response dapui.types.LoadedSourcesResponse

---@param listener fun(args: dapui.types.loadedSourcesRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.loadedSources(listener, opts) end

--- Arguments for `modules` request.
---@class dapui.types.ModulesArguments
---@field startModule? integer The index of the first module to return; if omitted modules start at 0.
---@field moduleCount? integer The number of modules to return. If `moduleCount` is not specified or 0, all modules are returned.

--- A Module object represents a row in the modules view.
--- The `id` attribute identifies a module in the modules view and is used in a `module` event for identifying a module for adding, updating or deleting.
--- The `name` attribute is used to minimally render the module in the UI.
---
--- Additional attributes can be added to the module. They show up in the module view if they have a corresponding `ColumnDescriptor`.
---
--- To avoid an unnecessary proliferation of additional attributes with similar semantics but different names, we recommend to re-use attributes from the 'recommended' list below first, and only introduce new attributes if nothing appropriate could be found.
---@class dapui.types.Module
---@field id integer | string Unique identifier for the module.
---@field name string A name of the module.
---@field path? string Logical full path to the module. The exact definition is implementation defined, but usually this would be a full path to the on-disk file for the module.
---@field isOptimized? boolean True if the module is optimized.
---@field isUserCode? boolean True if the module is considered 'user code' by a debugger that supports 'Just My Code'.
---@field version? string Version of Module.
---@field symbolStatus? string User-understandable description of if symbols were found for the module (ex: 'Symbols Loaded', 'Symbols not found', etc.)
---@field symbolFilePath? string Logical full path to the symbol file. The exact definition is implementation defined.
---@field dateTimeStamp? string Module created or modified, encoded as a RFC 3339 timestamp.
---@field addressRange? string Address range covered by this module.

---@class dapui.types.ModulesResponse
---@field modules dapui.types.Module[] All modules or range of modules.
---@field totalModules? integer The total number of modules available.

--- Modules can be retrieved from the debug adapter with this request which can either return all modules or a range of modules to support paging.
--- Clients should only call this request if the corresponding capability `supportsModulesRequest` is true.
---@async
---@param args dapui.types.ModulesArguments
---@return dapui.types.ModulesResponse
function DAPUIRequestsClient.modules(args) end

---@class dapui.types.modulesRequestListenerArgs
---@field request dapui.types.ModulesArguments
---@field error? table
---@field response dapui.types.ModulesResponse

---@param listener fun(args: dapui.types.modulesRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.modules(listener, opts) end

--- Arguments for `next` request.
---@class dapui.types.NextArguments
---@field threadId integer Specifies the thread for which to resume execution for one step (of the given granularity).
---@field singleThread? boolean If this flag is true, all other suspended threads are not resumed.
---@field granularity? "statement"|"line"|"instruction" Stepping granularity. If no granularity is specified, a granularity of `statement` is assumed.

--- The request executes one step (in the given granularity) for the specified thread and allows all other threads to run freely by resuming them.
--- If the debug adapter supports single thread execution (see capability `supportsSingleThreadExecutionRequests`), setting the `singleThread` argument to true prevents other suspended threads from resuming.
--- The debug adapter first sends the response and then a `stopped` event (with reason `step`) after the step has completed.
---@async
---@param args dapui.types.NextArguments
function DAPUIRequestsClient.next(args) end

---@class dapui.types.nextRequestListenerArgs
---@field request dapui.types.NextArguments
---@field error? table

---@param listener fun(args: dapui.types.nextRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.next(listener, opts) end

--- Arguments for `pause` request.
---@class dapui.types.PauseArguments
---@field threadId integer Pause execution for this thread.

--- The request suspends the debuggee.
--- The debug adapter first sends the response and then a `stopped` event (with reason `pause`) after the thread has been paused successfully.
---@async
---@param args dapui.types.PauseArguments
function DAPUIRequestsClient.pause(args) end

---@class dapui.types.pauseRequestListenerArgs
---@field request dapui.types.PauseArguments
---@field error? table

---@param listener fun(args: dapui.types.pauseRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.pause(listener, opts) end

--- Arguments for `readMemory` request.
---@class dapui.types.ReadMemoryArguments
---@field memoryReference string Memory reference to the base location from which data should be read.
---@field offset? integer Offset (in bytes) to be applied to the reference location before reading data. Can be negative.
---@field count integer Number of bytes to read at the specified location and offset.

---@class dapui.types.ReadMemoryResponse
---@field address string The address of the first byte of data returned. Treated as a hex value if prefixed with `0x`, or as a decimal value otherwise.
---@field unreadableBytes? integer The number of unreadable bytes encountered after the last successfully read byte. This can be used to determine the number of bytes that should be skipped before a subsequent `readMemory` request succeeds.
---@field data? string The bytes read from memory, encoded using base64. If the decoded length of `data` is less than the requested `count` in the original `readMemory` request, and `unreadableBytes` is zero or omitted, then the client should assume it's reached the end of readable memory.

--- Reads bytes from memory at the provided location.
--- Clients should only call this request if the corresponding capability `supportsReadMemoryRequest` is true.
---@async
---@param args dapui.types.ReadMemoryArguments
---@return dapui.types.ReadMemoryResponse
function DAPUIRequestsClient.readMemory(args) end

---@class dapui.types.readMemoryRequestListenerArgs
---@field request dapui.types.ReadMemoryArguments
---@field error? table
---@field response dapui.types.ReadMemoryResponse

---@param listener fun(args: dapui.types.readMemoryRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.readMemory(listener, opts) end

--- Arguments for `restartFrame` request.
---@class dapui.types.RestartFrameArguments
---@field frameId integer Restart the stack frame identified by `frameId`. The `frameId` must have been obtained in the current suspended state. See 'Lifetime of Object References' in the Overview section for details.

--- The request restarts execution of the specified stack frame.
--- The debug adapter first sends the response and then a `stopped` event (with reason `restart`) after the restart has completed.
--- Clients should only call this request if the corresponding capability `supportsRestartFrame` is true.
---@async
---@param args dapui.types.RestartFrameArguments
function DAPUIRequestsClient.restartFrame(args) end

---@class dapui.types.restartFrameRequestListenerArgs
---@field request dapui.types.RestartFrameArguments
---@field error? table

---@param listener fun(args: dapui.types.restartFrameRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.restartFrame(listener, opts) end

--- Arguments for `restart` request.
---@class dapui.types.RestartArguments
---@field arguments? dapui.types.LaunchRequestArguments | dapui.types.AttachRequestArguments The latest version of the `launch` or `attach` configuration.

--- Restarts a debug session. Clients should only call this request if the corresponding capability `supportsRestartRequest` is true.
--- If the capability is missing or has the value false, a typical client emulates `restart` by terminating the debug adapter first and then launching it anew.
---@async
---@param args dapui.types.RestartArguments
function DAPUIRequestsClient.restart(args) end

---@class dapui.types.restartRequestListenerArgs
---@field request dapui.types.RestartArguments
---@field error? table

---@param listener fun(args: dapui.types.restartRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.restart(listener, opts) end

--- Arguments for `reverseContinue` request.
---@class dapui.types.ReverseContinueArguments
---@field threadId integer Specifies the active thread. If the debug adapter supports single thread execution (see `supportsSingleThreadExecutionRequests`) and the `singleThread` argument is true, only the thread with this ID is resumed.
---@field singleThread? boolean If this flag is true, backward execution is resumed only for the thread with given `threadId`.

--- The request resumes backward execution of all threads. If the debug adapter supports single thread execution (see capability `supportsSingleThreadExecutionRequests`), setting the `singleThread` argument to true resumes only the specified thread. If not all threads were resumed, the `allThreadsContinued` attribute of the response should be set to false.
--- Clients should only call this request if the corresponding capability `supportsStepBack` is true.
---@async
---@param args dapui.types.ReverseContinueArguments
function DAPUIRequestsClient.reverseContinue(args) end

---@class dapui.types.reverseContinueRequestListenerArgs
---@field request dapui.types.ReverseContinueArguments
---@field error? table

---@param listener fun(args: dapui.types.reverseContinueRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.reverseContinue(listener, opts) end

--- Arguments for `runInTerminal` request.
---@class dapui.types.RunInTerminalRequestArguments
---@field kind? "integrated"|"external" What kind of terminal to launch. Defaults to `integrated` if not specified.
---@field title? string Title of the terminal.
---@field cwd string Working directory for the command. For non-empty, valid paths this typically results in execution of a change directory command.
---@field args string[] List of arguments. The first argument is the command to run.
---@field env? table<string,string> Environment key-value pairs that are added to or removed from the default environment.
---@field argsCanBeInterpretedByShell? boolean This property should only be set if the corresponding capability `supportsArgsCanBeInterpretedByShell` is true. If the client uses an intermediary shell to launch the application, then the client must not attempt to escape characters with special meanings for the shell. The user is fully responsible for escaping as needed and that arguments using special characters may not be portable across shells.

---@class dapui.types.RunInTerminalResponse
---@field processId? integer The process ID. The value should be less than or equal to 2147483647 (2^31-1).
---@field shellProcessId? integer The process ID of the terminal shell. The value should be less than or equal to 2147483647 (2^31-1).

--- This request is sent from the debug adapter to the client to run a command in a terminal.
--- This is typically used to launch the debuggee in a terminal provided by the client.
--- This request should only be called if the corresponding client capability `supportsRunInTerminalRequest` is true.
--- Client implementations of `runInTerminal` are free to run the command however they choose including issuing the command to a command line interpreter (aka 'shell'). Argument strings passed to the `runInTerminal` request must arrive verbatim in the command to be run. As a consequence, clients which use a shell are responsible for escaping any special shell characters in the argument strings to prevent them from being interpreted (and modified) by the shell.
--- Some users may wish to take advantage of shell processing in the argument strings. For clients which implement `runInTerminal` using an intermediary shell, the `argsCanBeInterpretedByShell` property can be set to true. In this case the client is requested not to escape any special shell characters in the argument strings.
---@async
---@param args dapui.types.RunInTerminalRequestArguments
---@return dapui.types.RunInTerminalResponse
function DAPUIRequestsClient.runInTerminal(args) end

---@class dapui.types.runInTerminalRequestListenerArgs
---@field request dapui.types.RunInTerminalRequestArguments
---@field error? table
---@field response dapui.types.RunInTerminalResponse

---@param listener fun(args: dapui.types.runInTerminalRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.runInTerminal(listener, opts) end

--- Arguments for `scopes` request.
---@class dapui.types.ScopesArguments
---@field frameId integer Retrieve the scopes for the stack frame identified by `frameId`. The `frameId` must have been obtained in the current suspended state. See 'Lifetime of Object References' in the Overview section for details.

--- A `Scope` is a named container for variables. Optionally a scope can map to a source or a range within a source.
---@class dapui.types.Scope
---@field name string Name of the scope such as 'Arguments', 'Locals', or 'Registers'. This string is shown in the UI as is and can be translated.
---@field presentationHint? string A hint for how to present this scope in the UI. If this attribute is missing, the scope is shown with a generic UI.
---@field variablesReference integer The variables of this scope can be retrieved by passing the value of `variablesReference` to the `variables` request as long as execution remains suspended. See 'Lifetime of Object References' in the Overview section for details.
---@field namedVariables? integer The number of named variables in this scope. The client can use this information to present the variables in a paged UI and fetch them in chunks.
---@field indexedVariables? integer The number of indexed variables in this scope. The client can use this information to present the variables in a paged UI and fetch them in chunks.
---@field expensive boolean If true, the number of variables in this scope is large or expensive to retrieve.
---@field source? dapui.types.Source The source for this scope.
---@field line? integer The start line of the range covered by this scope.
---@field column? integer Start position of the range covered by the scope. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field endLine? integer The end line of the range covered by this scope.
---@field endColumn? integer End position of the range covered by the scope. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.

---@class dapui.types.ScopesResponse
---@field scopes dapui.types.Scope[] The scopes of the stack frame. If the array has length zero, there are no scopes available.

--- The request returns the variable scopes for a given stack frame ID.
---@async
---@param args dapui.types.ScopesArguments
---@return dapui.types.ScopesResponse
function DAPUIRequestsClient.scopes(args) end

---@class dapui.types.scopesRequestListenerArgs
---@field request dapui.types.ScopesArguments
---@field error? table
---@field response dapui.types.ScopesResponse

---@param listener fun(args: dapui.types.scopesRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.scopes(listener, opts) end

--- Properties of a breakpoint or logpoint passed to the `setBreakpoints` request.
---@class dapui.types.SourceBreakpoint
---@field line integer The source line of the breakpoint or logpoint.
---@field column? integer Start position within source line of the breakpoint or logpoint. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field condition? string The expression for conditional breakpoints. It is only honored by a debug adapter if the corresponding capability `supportsConditionalBreakpoints` is true.
---@field hitCondition? string The expression that controls how many hits of the breakpoint are ignored. The debug adapter is expected to interpret the expression as needed. The attribute is only honored by a debug adapter if the corresponding capability `supportsHitConditionalBreakpoints` is true. If both this property and `condition` are specified, `hitCondition` should be evaluated only if the `condition` is met, and the debug adapter should stop only if both conditions are met.
---@field logMessage? string If this attribute exists and is non-empty, the debug adapter must not 'break' (stop) but log the message instead. Expressions within `{}` are interpolated. The attribute is only honored by a debug adapter if the corresponding capability `supportsLogPoints` is true. If either `hitCondition` or `condition` is specified, then the message should only be logged if those conditions are met.

--- Arguments for `setBreakpoints` request.
---@class dapui.types.SetBreakpointsArguments
---@field source dapui.types.Source The source location of the breakpoints; either `source.path` or `source.sourceReference` must be specified.
---@field breakpoints? dapui.types.SourceBreakpoint[] The code locations of the breakpoints.
---@field lines? integer[] Deprecated: The code locations of the breakpoints.
---@field sourceModified? boolean A value of true indicates that the underlying source has been modified which results in new breakpoint locations.

--- Information about a breakpoint created in `setBreakpoints`, `setFunctionBreakpoints`, `setInstructionBreakpoints`, or `setDataBreakpoints` requests.
---@class dapui.types.Breakpoint
---@field id? integer The identifier for the breakpoint. It is needed if breakpoint events are used to update or remove breakpoints.
---@field verified boolean If true, the breakpoint could be set (but not necessarily at the desired location).
---@field message? string A message about the state of the breakpoint. This is shown to the user and can be used to explain why a breakpoint could not be verified.
---@field source? dapui.types.Source The source where the breakpoint is located.
---@field line? integer The start line of the actual range covered by the breakpoint.
---@field column? integer Start position of the source range covered by the breakpoint. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field endLine? integer The end line of the actual range covered by the breakpoint.
---@field endColumn? integer End position of the source range covered by the breakpoint. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based. If no end line is given, then the end column is assumed to be in the start line.
---@field instructionReference? string A memory reference to where the breakpoint is set.
---@field offset? integer The offset from the instruction reference. This can be negative.

---@class dapui.types.SetBreakpointsResponse
---@field breakpoints dapui.types.Breakpoint[] Information about the breakpoints. The array elements are in the same order as the elements of the `breakpoints` (or the deprecated `lines`) array in the arguments.

--- Sets multiple breakpoints for a single source and clears all previous breakpoints in that source.
--- To clear all breakpoint for a source, specify an empty array.
--- When a breakpoint is hit, a `stopped` event (with reason `breakpoint`) is generated.
---@async
---@param args dapui.types.SetBreakpointsArguments
---@return dapui.types.SetBreakpointsResponse
function DAPUIRequestsClient.setBreakpoints(args) end

---@class dapui.types.setBreakpointsRequestListenerArgs
---@field request dapui.types.SetBreakpointsArguments
---@field error? table
---@field response dapui.types.SetBreakpointsResponse

---@param listener fun(args: dapui.types.setBreakpointsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setBreakpoints(listener, opts) end

--- Properties of a data breakpoint passed to the `setDataBreakpoints` request.
---@class dapui.types.DataBreakpoint
---@field dataId string An id representing the data. This id is returned from the `dataBreakpointInfo` request.
---@field accessType? "read"|"write"|"readWrite" The access type of the data.
---@field condition? string An expression for conditional breakpoints.
---@field hitCondition? string An expression that controls how many hits of the breakpoint are ignored. The debug adapter is expected to interpret the expression as needed.

--- Arguments for `setDataBreakpoints` request.
---@class dapui.types.SetDataBreakpointsArguments
---@field breakpoints dapui.types.DataBreakpoint[] The contents of this array replaces all existing data breakpoints. An empty array clears all data breakpoints.

---@class dapui.types.SetDataBreakpointsResponse
---@field breakpoints dapui.types.Breakpoint[] Information about the data breakpoints. The array elements correspond to the elements of the input argument `breakpoints` array.

--- Replaces all existing data breakpoints with new data breakpoints.
--- To clear all data breakpoints, specify an empty array.
--- When a data breakpoint is hit, a `stopped` event (with reason `data breakpoint`) is generated.
--- Clients should only call this request if the corresponding capability `supportsDataBreakpoints` is true.
---@async
---@param args dapui.types.SetDataBreakpointsArguments
---@return dapui.types.SetDataBreakpointsResponse
function DAPUIRequestsClient.setDataBreakpoints(args) end

---@class dapui.types.setDataBreakpointsRequestListenerArgs
---@field request dapui.types.SetDataBreakpointsArguments
---@field error? table
---@field response dapui.types.SetDataBreakpointsResponse

---@param listener fun(args: dapui.types.setDataBreakpointsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setDataBreakpoints(listener, opts) end

--- An `ExceptionFilterOptions` is used to specify an exception filter together with a condition for the `setExceptionBreakpoints` request.
---@class dapui.types.ExceptionFilterOptions
---@field filterId string ID of an exception filter returned by the `exceptionBreakpointFilters` capability.
---@field condition? string An expression for conditional exceptions. The exception breaks into the debugger if the result of the condition is true.

--- An `ExceptionPathSegment` represents a segment in a path that is used to match leafs or nodes in a tree of exceptions.
--- If a segment consists of more than one name, it matches the names provided if `negate` is false or missing, or it matches anything except the names provided if `negate` is true.
---@class dapui.types.ExceptionPathSegment
---@field negate? boolean If false or missing this segment matches the names provided, otherwise it matches anything except the names provided.
---@field names string[] Depending on the value of `negate` the names that should match or not match.

--- An `ExceptionOptions` assigns configuration options to a set of exceptions.
---@class dapui.types.ExceptionOptions
---@field path? dapui.types.ExceptionPathSegment[] A path that selects a single or multiple exceptions in a tree. If `path` is missing, the whole tree is selected. By convention the first segment of the path is a category that is used to group exceptions in the UI.
---@field breakMode "never"|"always"|"unhandled"|"userUnhandled" Condition when a thrown exception should result in a break.

--- Arguments for `setExceptionBreakpoints` request.
---@class dapui.types.SetExceptionBreakpointsArguments
---@field filters string[] Set of exception filters specified by their ID. The set of all possible exception filters is defined by the `exceptionBreakpointFilters` capability. The `filter` and `filterOptions` sets are additive.
---@field filterOptions? dapui.types.ExceptionFilterOptions[] Set of exception filters and their options. The set of all possible exception filters is defined by the `exceptionBreakpointFilters` capability. This attribute is only honored by a debug adapter if the corresponding capability `supportsExceptionFilterOptions` is true. The `filter` and `filterOptions` sets are additive.
---@field exceptionOptions? dapui.types.ExceptionOptions[] Configuration options for selected exceptions. The attribute is only honored by a debug adapter if the corresponding capability `supportsExceptionOptions` is true.

---@class dapui.types.SetExceptionBreakpointsResponse
---@field breakpoints? dapui.types.Breakpoint[] Information about the exception breakpoints or filters. The breakpoints returned are in the same order as the elements of the `filters`, `filterOptions`, `exceptionOptions` arrays in the arguments. If both `filters` and `filterOptions` are given, the returned array must start with `filters` information first, followed by `filterOptions` information.

--- The request configures the debugger's response to thrown exceptions.
--- If an exception is configured to break, a `stopped` event is fired (with reason `exception`).
--- Clients should only call this request if the corresponding capability `exceptionBreakpointFilters` returns one or more filters.
---@async
---@param args dapui.types.SetExceptionBreakpointsArguments
---@return dapui.types.SetExceptionBreakpointsResponse
function DAPUIRequestsClient.setExceptionBreakpoints(args) end

---@class dapui.types.setExceptionBreakpointsRequestListenerArgs
---@field request dapui.types.SetExceptionBreakpointsArguments
---@field error? table
---@field response dapui.types.SetExceptionBreakpointsResponse

---@param listener fun(args: dapui.types.setExceptionBreakpointsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setExceptionBreakpoints(listener, opts) end

--- Arguments for `setExpression` request.
---@class dapui.types.SetExpressionArguments
---@field expression string The l-value expression to assign to.
---@field value string The value expression to assign to the l-value expression.
---@field frameId? integer Evaluate the expressions in the scope of this stack frame. If not specified, the expressions are evaluated in the global scope.
---@field format? dapui.types.ValueFormat Specifies how the resulting value should be formatted.

---@class dapui.types.SetExpressionResponse
---@field value string The new value of the expression.
---@field type? string The type of the value. This attribute should only be returned by a debug adapter if the corresponding capability `supportsVariableType` is true.
---@field presentationHint? dapui.types.VariablePresentationHint Properties of a value that can be used to determine how to render the result in the UI.
---@field variablesReference? integer If `variablesReference` is > 0, the evaluate result is structured and its children can be retrieved by passing `variablesReference` to the `variables` request as long as execution remains suspended. See 'Lifetime of Object References' in the Overview section for details.
---@field namedVariables? integer The number of named child variables. The client can use this information to present the variables in a paged UI and fetch them in chunks. The value should be less than or equal to 2147483647 (2^31-1).
---@field indexedVariables? integer The number of indexed child variables. The client can use this information to present the variables in a paged UI and fetch them in chunks. The value should be less than or equal to 2147483647 (2^31-1).

--- Evaluates the given `value` expression and assigns it to the `expression` which must be a modifiable l-value.
--- The expressions have access to any variables and arguments that are in scope of the specified frame.
--- Clients should only call this request if the corresponding capability `supportsSetExpression` is true.
--- If a debug adapter implements both `setExpression` and `setVariable`, a client uses `setExpression` if the variable has an `evaluateName` property.
---@async
---@param args dapui.types.SetExpressionArguments
---@return dapui.types.SetExpressionResponse
function DAPUIRequestsClient.setExpression(args) end

---@class dapui.types.setExpressionRequestListenerArgs
---@field request dapui.types.SetExpressionArguments
---@field error? table
---@field response dapui.types.SetExpressionResponse

---@param listener fun(args: dapui.types.setExpressionRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setExpression(listener, opts) end

--- Properties of a breakpoint passed to the `setFunctionBreakpoints` request.
---@class dapui.types.FunctionBreakpoint
---@field name string The name of the function.
---@field condition? string An expression for conditional breakpoints. It is only honored by a debug adapter if the corresponding capability `supportsConditionalBreakpoints` is true.
---@field hitCondition? string An expression that controls how many hits of the breakpoint are ignored. The debug adapter is expected to interpret the expression as needed. The attribute is only honored by a debug adapter if the corresponding capability `supportsHitConditionalBreakpoints` is true.

--- Arguments for `setFunctionBreakpoints` request.
---@class dapui.types.SetFunctionBreakpointsArguments
---@field breakpoints dapui.types.FunctionBreakpoint[] The function names of the breakpoints.

---@class dapui.types.SetFunctionBreakpointsResponse
---@field breakpoints dapui.types.Breakpoint[] Information about the breakpoints. The array elements correspond to the elements of the `breakpoints` array.

--- Replaces all existing function breakpoints with new function breakpoints.
--- To clear all function breakpoints, specify an empty array.
--- When a function breakpoint is hit, a `stopped` event (with reason `function breakpoint`) is generated.
--- Clients should only call this request if the corresponding capability `supportsFunctionBreakpoints` is true.
---@async
---@param args dapui.types.SetFunctionBreakpointsArguments
---@return dapui.types.SetFunctionBreakpointsResponse
function DAPUIRequestsClient.setFunctionBreakpoints(args) end

---@class dapui.types.setFunctionBreakpointsRequestListenerArgs
---@field request dapui.types.SetFunctionBreakpointsArguments
---@field error? table
---@field response dapui.types.SetFunctionBreakpointsResponse

---@param listener fun(args: dapui.types.setFunctionBreakpointsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setFunctionBreakpoints(listener, opts) end

--- Properties of a breakpoint passed to the `setInstructionBreakpoints` request
---@class dapui.types.InstructionBreakpoint
---@field instructionReference string The instruction reference of the breakpoint. This should be a memory or instruction pointer reference from an `EvaluateResponse`, `Variable`, `StackFrame`, `GotoTarget`, or `Breakpoint`.
---@field offset? integer The offset from the instruction reference. This can be negative.
---@field condition? string An expression for conditional breakpoints. It is only honored by a debug adapter if the corresponding capability `supportsConditionalBreakpoints` is true.
---@field hitCondition? string An expression that controls how many hits of the breakpoint are ignored. The debug adapter is expected to interpret the expression as needed. The attribute is only honored by a debug adapter if the corresponding capability `supportsHitConditionalBreakpoints` is true.

--- Arguments for `setInstructionBreakpoints` request
---@class dapui.types.SetInstructionBreakpointsArguments
---@field breakpoints dapui.types.InstructionBreakpoint[] The instruction references of the breakpoints

---@class dapui.types.SetInstructionBreakpointsResponse
---@field breakpoints dapui.types.Breakpoint[] Information about the breakpoints. The array elements correspond to the elements of the `breakpoints` array.

--- Replaces all existing instruction breakpoints. Typically, instruction breakpoints would be set from a disassembly window.
--- To clear all instruction breakpoints, specify an empty array.
--- When an instruction breakpoint is hit, a `stopped` event (with reason `instruction breakpoint`) is generated.
--- Clients should only call this request if the corresponding capability `supportsInstructionBreakpoints` is true.
---@async
---@param args dapui.types.SetInstructionBreakpointsArguments
---@return dapui.types.SetInstructionBreakpointsResponse
function DAPUIRequestsClient.setInstructionBreakpoints(args) end

---@class dapui.types.setInstructionBreakpointsRequestListenerArgs
---@field request dapui.types.SetInstructionBreakpointsArguments
---@field error? table
---@field response dapui.types.SetInstructionBreakpointsResponse

---@param listener fun(args: dapui.types.setInstructionBreakpointsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setInstructionBreakpoints(listener, opts) end

--- Arguments for `setVariable` request.
---@class dapui.types.SetVariableArguments
---@field variablesReference integer The reference of the variable container. The `variablesReference` must have been obtained in the current suspended state. See 'Lifetime of Object References' in the Overview section for details.
---@field name string The name of the variable in the container.
---@field value string The value of the variable.
---@field format? dapui.types.ValueFormat Specifies details on how to format the response value.

---@class dapui.types.SetVariableResponse
---@field value string The new value of the variable.
---@field type? string The type of the new value. Typically shown in the UI when hovering over the value.
---@field variablesReference? integer If `variablesReference` is > 0, the new value is structured and its children can be retrieved by passing `variablesReference` to the `variables` request as long as execution remains suspended. See 'Lifetime of Object References' in the Overview section for details.
---@field namedVariables? integer The number of named child variables. The client can use this information to present the variables in a paged UI and fetch them in chunks. The value should be less than or equal to 2147483647 (2^31-1).
---@field indexedVariables? integer The number of indexed child variables. The client can use this information to present the variables in a paged UI and fetch them in chunks. The value should be less than or equal to 2147483647 (2^31-1).

--- Set the variable with the given name in the variable container to a new value. Clients should only call this request if the corresponding capability `supportsSetVariable` is true.
--- If a debug adapter implements both `setVariable` and `setExpression`, a client will only use `setExpression` if the variable has an `evaluateName` property.
---@async
---@param args dapui.types.SetVariableArguments
---@return dapui.types.SetVariableResponse
function DAPUIRequestsClient.setVariable(args) end

---@class dapui.types.setVariableRequestListenerArgs
---@field request dapui.types.SetVariableArguments
---@field error? table
---@field response dapui.types.SetVariableResponse

---@param listener fun(args: dapui.types.setVariableRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.setVariable(listener, opts) end

--- Arguments for `source` request.
---@class dapui.types.SourceArguments
---@field source? dapui.types.Source Specifies the source content to load. Either `source.path` or `source.sourceReference` must be specified.
---@field sourceReference integer The reference to the source. This is the same as `source.sourceReference`. This is provided for backward compatibility since old clients do not understand the `source` attribute.

---@class dapui.types.SourceResponse
---@field content string Content of the source reference.
---@field mimeType? string Content type (MIME type) of the source.

--- The request retrieves the source code for a given source reference.
---@async
---@param args dapui.types.SourceArguments
---@return dapui.types.SourceResponse
function DAPUIRequestsClient.source(args) end

---@class dapui.types.sourceRequestListenerArgs
---@field request dapui.types.SourceArguments
---@field error? table
---@field response dapui.types.SourceResponse

---@param listener fun(args: dapui.types.sourceRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.source(listener, opts) end

--- Provides formatting information for a stack frame.
---@class dapui.types.StackFrameFormat
---@field hex? boolean Display the value in hex.
---@field parameters? boolean Displays parameters for the stack frame.
---@field parameterTypes? boolean Displays the types of parameters for the stack frame.
---@field parameterNames? boolean Displays the names of parameters for the stack frame.
---@field parameterValues? boolean Displays the values of parameters for the stack frame.
---@field line? boolean Displays the line number of the stack frame.
---@field module? boolean Displays the module of the stack frame.
---@field includeAll? boolean Includes all stack frames, including those the debug adapter might otherwise hide.

--- Arguments for `stackTrace` request.
---@class dapui.types.StackTraceArguments
---@field threadId integer Retrieve the stacktrace for this thread.
---@field startFrame? integer The index of the first frame to return; if omitted frames start at 0.
---@field levels? integer The maximum number of frames to return. If levels is not specified or 0, all frames are returned.
---@field format? dapui.types.StackFrameFormat Specifies details on how to format the stack frames. The attribute is only honored by a debug adapter if the corresponding capability `supportsValueFormattingOptions` is true.

--- A Stackframe contains the source location.
---@class dapui.types.StackFrame
---@field id integer An identifier for the stack frame. It must be unique across all threads. This id can be used to retrieve the scopes of the frame with the `scopes` request or to restart the execution of a stack frame.
---@field name string The name of the stack frame, typically a method name.
---@field source? dapui.types.Source The source of the frame.
---@field line integer The line within the source of the frame. If the source attribute is missing or doesn't exist, `line` is 0 and should be ignored by the client.
---@field column integer Start position of the range covered by the stack frame. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based. If attribute `source` is missing or doesn't exist, `column` is 0 and should be ignored by the client.
---@field endLine? integer The end line of the range covered by the stack frame.
---@field endColumn? integer End position of the range covered by the stack frame. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field canRestart? boolean Indicates whether this frame can be restarted with the `restart` request. Clients should only use this if the debug adapter supports the `restart` request and the corresponding capability `supportsRestartRequest` is true. If a debug adapter has this capability, then `canRestart` defaults to `true` if the property is absent.
---@field instructionPointerReference? string A memory reference for the current instruction pointer in this frame.
---@field moduleId? integer | string The module associated with this frame, if any.
---@field presentationHint? "normal"|"label"|"subtle" A hint for how to present this frame in the UI. A value of `label` can be used to indicate that the frame is an artificial frame that is used as a visual label or separator. A value of `subtle` can be used to change the appearance of a frame in a 'subtle' way.

---@class dapui.types.StackTraceResponse
---@field stackFrames dapui.types.StackFrame[] The frames of the stack frame. If the array has length zero, there are no stack frames available. This means that there is no location information available.
---@field totalFrames? integer The total number of frames available in the stack. If omitted or if `totalFrames` is larger than the available frames, a client is expected to request frames until a request returns less frames than requested (which indicates the end of the stack). Returning monotonically increasing `totalFrames` values for subsequent requests can be used to enforce paging in the client.

--- The request returns a stacktrace from the current execution state of a given thread.
--- A client can request all stack frames by omitting the startFrame and levels arguments. For performance-conscious clients and if the corresponding capability `supportsDelayedStackTraceLoading` is true, stack frames can be retrieved in a piecemeal way with the `startFrame` and `levels` arguments. The response of the `stackTrace` request may contain a `totalFrames` property that hints at the total number of frames in the stack. If a client needs this total number upfront, it can issue a request for a single (first) frame and depending on the value of `totalFrames` decide how to proceed. In any case a client should be prepared to receive fewer frames than requested, which is an indication that the end of the stack has been reached.
---@async
---@param args dapui.types.StackTraceArguments
---@return dapui.types.StackTraceResponse
function DAPUIRequestsClient.stackTrace(args) end

---@class dapui.types.stackTraceRequestListenerArgs
---@field request dapui.types.StackTraceArguments
---@field error? table
---@field response dapui.types.StackTraceResponse

---@param listener fun(args: dapui.types.stackTraceRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.stackTrace(listener, opts) end

--- Arguments for `startDebugging` request.
---@class dapui.types.StartDebuggingRequestArguments
---@field configuration table<string,any> Arguments passed to the new debug session. The arguments must only contain properties understood by the `launch` or `attach` requests of the debug adapter and they must not contain any client-specific properties (e.g. `type`) or client-specific features (e.g. substitutable 'variables').
---@field request "launch"|"attach" Indicates whether the new debug session should be started with a `launch` or `attach` request.

--- This request is sent from the debug adapter to the client to start a new debug session of the same type as the caller.
--- This request should only be sent if the corresponding client capability `supportsStartDebuggingRequest` is true.
--- A client implementation of `startDebugging` should start a new debug session (of the same type as the caller) in the same way that the caller's session was started. If the client supports hierarchical debug sessions, the newly created session can be treated as a child of the caller session.
---@async
---@param args dapui.types.StartDebuggingRequestArguments
function DAPUIRequestsClient.startDebugging(args) end

---@class dapui.types.startDebuggingRequestListenerArgs
---@field request dapui.types.StartDebuggingRequestArguments
---@field error? table

---@param listener fun(args: dapui.types.startDebuggingRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.startDebugging(listener, opts) end

--- Arguments for `stepBack` request.
---@class dapui.types.StepBackArguments
---@field threadId integer Specifies the thread for which to resume execution for one step backwards (of the given granularity).
---@field singleThread? boolean If this flag is true, all other suspended threads are not resumed.
---@field granularity? "statement"|"line"|"instruction" Stepping granularity to step. If no granularity is specified, a granularity of `statement` is assumed.

--- The request executes one backward step (in the given granularity) for the specified thread and allows all other threads to run backward freely by resuming them.
--- If the debug adapter supports single thread execution (see capability `supportsSingleThreadExecutionRequests`), setting the `singleThread` argument to true prevents other suspended threads from resuming.
--- The debug adapter first sends the response and then a `stopped` event (with reason `step`) after the step has completed.
--- Clients should only call this request if the corresponding capability `supportsStepBack` is true.
---@async
---@param args dapui.types.StepBackArguments
function DAPUIRequestsClient.stepBack(args) end

---@class dapui.types.stepBackRequestListenerArgs
---@field request dapui.types.StepBackArguments
---@field error? table

---@param listener fun(args: dapui.types.stepBackRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.stepBack(listener, opts) end

--- Arguments for `stepIn` request.
---@class dapui.types.StepInArguments
---@field threadId integer Specifies the thread for which to resume execution for one step-into (of the given granularity).
---@field singleThread? boolean If this flag is true, all other suspended threads are not resumed.
---@field targetId? integer Id of the target to step into.
---@field granularity? "statement"|"line"|"instruction" Stepping granularity. If no granularity is specified, a granularity of `statement` is assumed.

--- The request resumes the given thread to step into a function/method and allows all other threads to run freely by resuming them.
--- If the debug adapter supports single thread execution (see capability `supportsSingleThreadExecutionRequests`), setting the `singleThread` argument to true prevents other suspended threads from resuming.
--- If the request cannot step into a target, `stepIn` behaves like the `next` request.
--- The debug adapter first sends the response and then a `stopped` event (with reason `step`) after the step has completed.
--- If there are multiple function/method calls (or other targets) on the source line,
--- the argument `targetId` can be used to control into which target the `stepIn` should occur.
--- The list of possible targets for a given source line can be retrieved via the `stepInTargets` request.
---@async
---@param args dapui.types.StepInArguments
function DAPUIRequestsClient.stepIn(args) end

---@class dapui.types.stepInRequestListenerArgs
---@field request dapui.types.StepInArguments
---@field error? table

---@param listener fun(args: dapui.types.stepInRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.stepIn(listener, opts) end

--- Arguments for `stepInTargets` request.
---@class dapui.types.StepInTargetsArguments
---@field frameId integer The stack frame for which to retrieve the possible step-in targets.

--- A `StepInTarget` can be used in the `stepIn` request and determines into which single target the `stepIn` request should step.
---@class dapui.types.StepInTarget
---@field id integer Unique identifier for a step-in target.
---@field label string The name of the step-in target (shown in the UI).
---@field line? integer The line of the step-in target.
---@field column? integer Start position of the range covered by the step in target. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field endLine? integer The end line of the range covered by the step-in target.
---@field endColumn? integer End position of the range covered by the step in target. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.

---@class dapui.types.StepInTargetsResponse
---@field targets dapui.types.StepInTarget[] The possible step-in targets of the specified source location.

--- This request retrieves the possible step-in targets for the specified stack frame.
--- These targets can be used in the `stepIn` request.
--- Clients should only call this request if the corresponding capability `supportsStepInTargetsRequest` is true.
---@async
---@param args dapui.types.StepInTargetsArguments
---@return dapui.types.StepInTargetsResponse
function DAPUIRequestsClient.stepInTargets(args) end

---@class dapui.types.stepInTargetsRequestListenerArgs
---@field request dapui.types.StepInTargetsArguments
---@field error? table
---@field response dapui.types.StepInTargetsResponse

---@param listener fun(args: dapui.types.stepInTargetsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.stepInTargets(listener, opts) end

--- Arguments for `stepOut` request.
---@class dapui.types.StepOutArguments
---@field threadId integer Specifies the thread for which to resume execution for one step-out (of the given granularity).
---@field singleThread? boolean If this flag is true, all other suspended threads are not resumed.
---@field granularity? "statement"|"line"|"instruction" Stepping granularity. If no granularity is specified, a granularity of `statement` is assumed.

--- The request resumes the given thread to step out (return) from a function/method and allows all other threads to run freely by resuming them.
--- If the debug adapter supports single thread execution (see capability `supportsSingleThreadExecutionRequests`), setting the `singleThread` argument to true prevents other suspended threads from resuming.
--- The debug adapter first sends the response and then a `stopped` event (with reason `step`) after the step has completed.
---@async
---@param args dapui.types.StepOutArguments
function DAPUIRequestsClient.stepOut(args) end

---@class dapui.types.stepOutRequestListenerArgs
---@field request dapui.types.StepOutArguments
---@field error? table

---@param listener fun(args: dapui.types.stepOutRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.stepOut(listener, opts) end

--- Arguments for `terminate` request.
---@class dapui.types.TerminateArguments
---@field restart? boolean A value of true indicates that this `terminate` request is part of a restart sequence.

--- The `terminate` request is sent from the client to the debug adapter in order to shut down the debuggee gracefully. Clients should only call this request if the capability `supportsTerminateRequest` is true.
--- Typically a debug adapter implements `terminate` by sending a software signal which the debuggee intercepts in order to clean things up properly before terminating itself.
--- Please note that this request does not directly affect the state of the debug session: if the debuggee decides to veto the graceful shutdown for any reason by not terminating itself, then the debug session just continues.
--- Clients can surface the `terminate` request as an explicit command or they can integrate it into a two stage Stop command that first sends `terminate` to request a graceful shutdown, and if that fails uses `disconnect` for a forceful shutdown.
---@async
---@param args dapui.types.TerminateArguments
function DAPUIRequestsClient.terminate(args) end

---@class dapui.types.terminateRequestListenerArgs
---@field request dapui.types.TerminateArguments
---@field error? table

---@param listener fun(args: dapui.types.terminateRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.terminate(listener, opts) end

--- Arguments for `terminateThreads` request.
---@class dapui.types.TerminateThreadsArguments
---@field threadIds? integer[] Ids of threads to be terminated.

--- The request terminates the threads with the given ids.
--- Clients should only call this request if the corresponding capability `supportsTerminateThreadsRequest` is true.
---@async
---@param args dapui.types.TerminateThreadsArguments
function DAPUIRequestsClient.terminateThreads(args) end

---@class dapui.types.terminateThreadsRequestListenerArgs
---@field request dapui.types.TerminateThreadsArguments
---@field error? table

---@param listener fun(args: dapui.types.terminateThreadsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.terminateThreads(listener, opts) end

--- A Thread
---@class dapui.types.Thread
---@field id integer Unique identifier for the thread.
---@field name string The name of the thread.

---@class dapui.types.ThreadsResponse
---@field threads dapui.types.Thread[] All threads.

--- The request retrieves a list of all threads.
---@async
---@return dapui.types.ThreadsResponse
function DAPUIRequestsClient.threads() end

---@class dapui.types.threadsRequestListenerArgs
---@field error? table
---@field response dapui.types.ThreadsResponse

---@param listener fun(args: dapui.types.threadsRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.threads(listener, opts) end

--- Arguments for `variables` request.
---@class dapui.types.VariablesArguments
---@field variablesReference integer The variable for which to retrieve its children. The `variablesReference` must have been obtained in the current suspended state. See 'Lifetime of Object References' in the Overview section for details.
---@field filter? "indexed"|"named" Filter to limit the child variables to either named or indexed. If omitted, both types are fetched.
---@field start? integer The index of the first variable to return; if omitted children start at 0.
---@field count? integer The number of variables to return. If count is missing or 0, all variables are returned.
---@field format? dapui.types.ValueFormat Specifies details on how to format the Variable values. The attribute is only honored by a debug adapter if the corresponding capability `supportsValueFormattingOptions` is true.

--- A Variable is a name/value pair.
--- The `type` attribute is shown if space permits or when hovering over the variable's name.
--- The `kind` attribute is used to render additional properties of the variable, e.g. different icons can be used to indicate that a variable is public or private.
--- If the value is structured (has children), a handle is provided to retrieve the children with the `variables` request.
--- If the number of named or indexed children is large, the numbers should be returned via the `namedVariables` and `indexedVariables` attributes.
--- The client can use this information to present the children in a paged UI and fetch them in chunks.
---@class dapui.types.Variable
---@field name string The variable's name.
---@field value string The variable's value. This can be a multi-line text, e.g. for a function the body of a function. For structured variables (which do not have a simple value), it is recommended to provide a one-line representation of the structured object. This helps to identify the structured object in the collapsed state when its children are not yet visible. An empty string can be used if no value should be shown in the UI.
---@field type? string The type of the variable's value. Typically shown in the UI when hovering over the value. This attribute should only be returned by a debug adapter if the corresponding capability `supportsVariableType` is true.
---@field presentationHint? dapui.types.VariablePresentationHint Properties of a variable that can be used to determine how to render the variable in the UI.
---@field evaluateName? string The evaluatable name of this variable which can be passed to the `evaluate` request to fetch the variable's value.
---@field variablesReference integer If `variablesReference` is > 0, the variable is structured and its children can be retrieved by passing `variablesReference` to the `variables` request as long as execution remains suspended. See 'Lifetime of Object References' in the Overview section for details.
---@field namedVariables? integer The number of named child variables. The client can use this information to present the children in a paged UI and fetch them in chunks.
---@field indexedVariables? integer The number of indexed child variables. The client can use this information to present the children in a paged UI and fetch them in chunks.
---@field memoryReference? string The memory reference for the variable if the variable represents executable code, such as a function pointer. This attribute is only required if the corresponding capability `supportsMemoryReferences` is true.

---@class dapui.types.VariablesResponse
---@field variables dapui.types.Variable[] All (or a range) of variables for the given variable reference.

--- Retrieves all child variables for the given variable reference.
--- A filter can be used to limit the fetched children to either named or indexed children.
---@async
---@param args dapui.types.VariablesArguments
---@return dapui.types.VariablesResponse
function DAPUIRequestsClient.variables(args) end

---@class dapui.types.variablesRequestListenerArgs
---@field request dapui.types.VariablesArguments
---@field error? table
---@field response dapui.types.VariablesResponse

---@param listener fun(args: dapui.types.variablesRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.variables(listener, opts) end

--- Arguments for `writeMemory` request.
---@class dapui.types.WriteMemoryArguments
---@field memoryReference string Memory reference to the base location to which data should be written.
---@field offset? integer Offset (in bytes) to be applied to the reference location before writing data. Can be negative.
---@field allowPartial? boolean Property to control partial writes. If true, the debug adapter should attempt to write memory even if the entire memory region is not writable. In such a case the debug adapter should stop after hitting the first byte of memory that cannot be written and return the number of bytes written in the response via the `offset` and `bytesWritten` properties. If false or missing, a debug adapter should attempt to verify the region is writable before writing, and fail the response if it is not.
---@field data string Bytes to write, encoded using base64.

---@class dapui.types.WriteMemoryResponse
---@field offset? integer Property that should be returned when `allowPartial` is true to indicate the offset of the first byte of data successfully written. Can be negative.
---@field bytesWritten? integer Property that should be returned when `allowPartial` is true to indicate the number of bytes starting from address that were successfully written.

--- Writes bytes to memory at the provided location.
--- Clients should only call this request if the corresponding capability `supportsWriteMemoryRequest` is true.
---@async
---@param args dapui.types.WriteMemoryArguments
---@return dapui.types.WriteMemoryResponse
function DAPUIRequestsClient.writeMemory(args) end

---@class dapui.types.writeMemoryRequestListenerArgs
---@field request dapui.types.WriteMemoryArguments
---@field error? table
---@field response dapui.types.WriteMemoryResponse

---@param listener fun(args: dapui.types.writeMemoryRequestListenerArgs): boolean | nil
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.writeMemory(listener, opts) end

---@class dapui.types.BreakpointEventArgs
---@field reason string The reason for the event.
---@field breakpoint dapui.types.Breakpoint The `id` attribute is used to find the target breakpoint, the other attributes are used as the new values.

--- The event indicates that some information about a breakpoint has changed.
---@param listener fun(args: dapui.types.BreakpointEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.breakpoint(listener, opts) end

--- Information about the capabilities of a debug adapter.
---@class dapui.types.Capabilities
---@field supportsConfigurationDoneRequest? boolean The debug adapter supports the `configurationDone` request.
---@field supportsFunctionBreakpoints? boolean The debug adapter supports function breakpoints.
---@field supportsConditionalBreakpoints? boolean The debug adapter supports conditional breakpoints.
---@field supportsHitConditionalBreakpoints? boolean The debug adapter supports breakpoints that break execution after a specified number of hits.
---@field supportsEvaluateForHovers? boolean The debug adapter supports a (side effect free) `evaluate` request for data hovers.
---@field exceptionBreakpointFilters? dapui.types.ExceptionBreakpointsFilter[] Available exception filter options for the `setExceptionBreakpoints` request.
---@field supportsStepBack? boolean The debug adapter supports stepping back via the `stepBack` and `reverseContinue` requests.
---@field supportsSetVariable? boolean The debug adapter supports setting a variable to a value.
---@field supportsRestartFrame? boolean The debug adapter supports restarting a frame.
---@field supportsGotoTargetsRequest? boolean The debug adapter supports the `gotoTargets` request.
---@field supportsStepInTargetsRequest? boolean The debug adapter supports the `stepInTargets` request.
---@field supportsCompletionsRequest? boolean The debug adapter supports the `completions` request.
---@field completionTriggerCharacters? string[] The set of characters that should trigger completion in a REPL. If not specified, the UI should assume the `.` character.
---@field supportsModulesRequest? boolean The debug adapter supports the `modules` request.
---@field additionalModuleColumns? dapui.types.ColumnDescriptor[] The set of additional module information exposed by the debug adapter.
---@field supportedChecksumAlgorithms? "MD5"|"SHA1"|"SHA256"|"timestamp"[] Checksum algorithms supported by the debug adapter.
---@field supportsRestartRequest? boolean The debug adapter supports the `restart` request. In this case a client should not implement `restart` by terminating and relaunching the adapter but by calling the `restart` request.
---@field supportsExceptionOptions? boolean The debug adapter supports `exceptionOptions` on the `setExceptionBreakpoints` request.
---@field supportsValueFormattingOptions? boolean The debug adapter supports a `format` attribute on the `stackTrace`, `variables`, and `evaluate` requests.
---@field supportsExceptionInfoRequest? boolean The debug adapter supports the `exceptionInfo` request.
---@field supportTerminateDebuggee? boolean The debug adapter supports the `terminateDebuggee` attribute on the `disconnect` request.
---@field supportSuspendDebuggee? boolean The debug adapter supports the `suspendDebuggee` attribute on the `disconnect` request.
---@field supportsDelayedStackTraceLoading? boolean The debug adapter supports the delayed loading of parts of the stack, which requires that both the `startFrame` and `levels` arguments and the `totalFrames` result of the `stackTrace` request are supported.
---@field supportsLoadedSourcesRequest? boolean The debug adapter supports the `loadedSources` request.
---@field supportsLogPoints? boolean The debug adapter supports log points by interpreting the `logMessage` attribute of the `SourceBreakpoint`.
---@field supportsTerminateThreadsRequest? boolean The debug adapter supports the `terminateThreads` request.
---@field supportsSetExpression? boolean The debug adapter supports the `setExpression` request.
---@field supportsTerminateRequest? boolean The debug adapter supports the `terminate` request.
---@field supportsDataBreakpoints? boolean The debug adapter supports data breakpoints.
---@field supportsReadMemoryRequest? boolean The debug adapter supports the `readMemory` request.
---@field supportsWriteMemoryRequest? boolean The debug adapter supports the `writeMemory` request.
---@field supportsDisassembleRequest? boolean The debug adapter supports the `disassemble` request.
---@field supportsCancelRequest? boolean The debug adapter supports the `cancel` request.
---@field supportsBreakpointLocationsRequest? boolean The debug adapter supports the `breakpointLocations` request.
---@field supportsClipboardContext? boolean The debug adapter supports the `clipboard` context value in the `evaluate` request.
---@field supportsSteppingGranularity? boolean The debug adapter supports stepping granularities (argument `granularity`) for the stepping requests.
---@field supportsInstructionBreakpoints? boolean The debug adapter supports adding breakpoints based on instruction references.
---@field supportsExceptionFilterOptions? boolean The debug adapter supports `filterOptions` as an argument on the `setExceptionBreakpoints` request.
---@field supportsSingleThreadExecutionRequests? boolean The debug adapter supports the `singleThread` property on the execution requests (`continue`, `next`, `stepIn`, `stepOut`, `reverseContinue`, `stepBack`).

---@class dapui.types.CapabilitiesEventArgs
---@field capabilities dapui.types.Capabilities The set of updated capabilities.

--- The event indicates that one or more capabilities have changed.
--- Since the capabilities are dependent on the client and its UI, it might not be possible to change that at random times (or too late).
--- Consequently this event has a hint characteristic: a client can only be expected to make a 'best effort' in honoring individual capabilities but there are no guarantees.
--- Only changed capabilities need to be included, all other capabilities keep their values.
---@param listener fun(args: dapui.types.CapabilitiesEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.capabilities(listener, opts) end

---@class dapui.types.ContinuedEventArgs
---@field threadId integer The thread which was continued.
---@field allThreadsContinued? boolean If `allThreadsContinued` is true, a debug adapter can announce that all threads have continued.

--- The event indicates that the execution of the debuggee has continued.
--- Please note: a debug adapter is not expected to send this event in response to a request that implies that execution continues, e.g. `launch` or `continue`.
--- It is only necessary to send a `continued` event if there was no previous request that implied this.
---@param listener fun(args: dapui.types.ContinuedEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.continued(listener, opts) end

---@class dapui.types.ExitedEventArgs
---@field exitCode integer The exit code returned from the debuggee.

--- The event indicates that the debuggee has exited and returns its exit code.
---@param listener fun(args: dapui.types.ExitedEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.exited(listener, opts) end

--- This event indicates that the debug adapter is ready to accept configuration requests (e.g. `setBreakpoints`, `setExceptionBreakpoints`).
--- A debug adapter is expected to send this event when it is ready to accept configuration requests (but not before the `initialize` request has finished).
--- The sequence of events/requests is as follows:
--- - adapters sends `initialized` event (after the `initialize` request has returned)
--- - client sends zero or more `setBreakpoints` requests
--- - client sends one `setFunctionBreakpoints` request (if corresponding capability `supportsFunctionBreakpoints` is true)
--- - client sends a `setExceptionBreakpoints` request if one or more `exceptionBreakpointFilters` have been defined (or if `supportsConfigurationDoneRequest` is not true)
--- - client sends other future configuration requests
--- - client sends one `configurationDone` request to indicate the end of the configuration.
---@param listener fun()
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.initialized(listener, opts) end

---@class dapui.types.InvalidatedAreas
---@field __root__ string Logical areas that can be invalidated by the `invalidated` event.

---@class dapui.types.InvalidatedEventArgs
---@field areas? dapui.types.InvalidatedAreas[] Set of logical areas that got invalidated. This property has a hint characteristic: a client can only be expected to make a 'best effort' in honoring the areas but there are no guarantees. If this property is missing, empty, or if values are not understood, the client should assume a single value `all`.
---@field threadId? integer If specified, the client only needs to refetch data related to this thread.
---@field stackFrameId? integer If specified, the client only needs to refetch data related to this stack frame (and the `threadId` is ignored).

--- This event signals that some state in the debug adapter has changed and requires that the client needs to re-render the data snapshot previously requested.
--- Debug adapters do not have to emit this event for runtime changes like stopped or thread events because in that case the client refetches the new state anyway. But the event can be used for example to refresh the UI after rendering formatting has changed in the debug adapter.
--- This event should only be sent if the corresponding capability `supportsInvalidatedEvent` is true.
---@param listener fun(args: dapui.types.InvalidatedEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.invalidated(listener, opts) end

---@class dapui.types.LoadedSourceEventArgs
---@field reason "new"|"changed"|"removed" The reason for the event.
---@field source dapui.types.Source The new, changed, or removed source.

--- The event indicates that some source has been added, changed, or removed from the set of all loaded sources.
---@param listener fun(args: dapui.types.LoadedSourceEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.loadedSource(listener, opts) end

---@class dapui.types.MemoryEventArgs
---@field memoryReference string Memory reference of a memory range that has been updated.
---@field offset integer Starting offset in bytes where memory has been updated. Can be negative.
---@field count integer Number of bytes updated.

--- This event indicates that some memory range has been updated. It should only be sent if the corresponding capability `supportsMemoryEvent` is true.
--- Clients typically react to the event by re-issuing a `readMemory` request if they show the memory identified by the `memoryReference` and if the updated memory range overlaps the displayed range. Clients should not make assumptions how individual memory references relate to each other, so they should not assume that they are part of a single continuous address range and might overlap.
--- Debug adapters can use this event to indicate that the contents of a memory range has changed due to some other request like `setVariable` or `setExpression`. Debug adapters are not expected to emit this event for each and every memory change of a running program, because that information is typically not available from debuggers and it would flood clients with too many events.
---@param listener fun(args: dapui.types.MemoryEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.memory(listener, opts) end

---@class dapui.types.ModuleEventArgs
---@field reason "new"|"changed"|"removed" The reason for the event.
---@field module dapui.types.Module The new, changed, or removed module. In case of `removed` only the module id is used.

--- The event indicates that some information about a module has changed.
---@param listener fun(args: dapui.types.ModuleEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.module(listener, opts) end

---@class dapui.types.OutputEventArgs
---@field category? string The output category. If not specified or if the category is not understood by the client, `console` is assumed.
---@field output string The output to report.
---@field group? "start"|"startCollapsed"|"end" Support for keeping an output log organized by grouping related messages.
---@field variablesReference? integer If an attribute `variablesReference` exists and its value is > 0, the output contains objects which can be retrieved by passing `variablesReference` to the `variables` request as long as execution remains suspended. See 'Lifetime of Object References' in the Overview section for details.
---@field source? dapui.types.Source The source location where the output was produced.
---@field line? integer The source location's line where the output was produced.
---@field column? integer The position in `line` where the output was produced. It is measured in UTF-16 code units and the client capability `columnsStartAt1` determines whether it is 0- or 1-based.
---@field data? any[] | boolean | integer | number | table<string,any> | string Additional data to report. For the `telemetry` category the data is sent to telemetry, for the other categories the data is shown in JSON format.

--- The event indicates that the target has produced some output.
---@param listener fun(args: dapui.types.OutputEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.output(listener, opts) end

---@class dapui.types.ProcessEventArgs
---@field name string The logical name of the process. This is usually the full path to process's executable file. Example: /home/example/myproj/program.js.
---@field systemProcessId? integer The system process id of the debugged process. This property is missing for non-system processes.
---@field isLocalProcess? boolean If true, the process is running on the same computer as the debug adapter.
---@field startMethod? "launch"|"attach"|"attachForSuspendedLaunch" Describes how the debug engine started debugging this process.
---@field pointerSize? integer The size of a pointer or address for this process, in bits. This value may be used by clients when formatting addresses for display.

--- The event indicates that the debugger has begun debugging a new process. Either one that it has launched, or one that it has attached to.
---@param listener fun(args: dapui.types.ProcessEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.process(listener, opts) end

---@class dapui.types.ProgressEndEventArgs
---@field progressId string The ID that was introduced in the initial `ProgressStartEvent`.
---@field message? string More detailed progress message. If omitted, the previous message (if any) is used.

--- The event signals the end of the progress reporting with a final message.
--- This event should only be sent if the corresponding capability `supportsProgressReporting` is true.
---@param listener fun(args: dapui.types.ProgressEndEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.progressEnd(listener, opts) end

---@class dapui.types.ProgressStartEventArgs
---@field progressId string An ID that can be used in subsequent `progressUpdate` and `progressEnd` events to make them refer to the same progress reporting. IDs must be unique within a debug session.
---@field title string Short title of the progress reporting. Shown in the UI to describe the long running operation.
---@field requestId? integer The request ID that this progress report is related to. If specified a debug adapter is expected to emit progress events for the long running request until the request has been either completed or cancelled. If the request ID is omitted, the progress report is assumed to be related to some general activity of the debug adapter.
---@field cancellable? boolean If true, the request that reports progress may be cancelled with a `cancel` request. So this property basically controls whether the client should use UX that supports cancellation. Clients that don't support cancellation are allowed to ignore the setting.
---@field message? string More detailed progress message.
---@field percentage? number Progress percentage to display (value range: 0 to 100). If omitted no percentage is shown.

--- The event signals that a long running operation is about to start and provides additional information for the client to set up a corresponding progress and cancellation UI.
--- The client is free to delay the showing of the UI in order to reduce flicker.
--- This event should only be sent if the corresponding capability `supportsProgressReporting` is true.
---@param listener fun(args: dapui.types.ProgressStartEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.progressStart(listener, opts) end

---@class dapui.types.ProgressUpdateEventArgs
---@field progressId string The ID that was introduced in the initial `progressStart` event.
---@field message? string More detailed progress message. If omitted, the previous message (if any) is used.
---@field percentage? number Progress percentage to display (value range: 0 to 100). If omitted no percentage is shown.

--- The event signals that the progress reporting needs to be updated with a new message and/or percentage.
--- The client does not have to update the UI immediately, but the clients needs to keep track of the message and/or percentage values.
--- This event should only be sent if the corresponding capability `supportsProgressReporting` is true.
---@param listener fun(args: dapui.types.ProgressUpdateEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.progressUpdate(listener, opts) end

---@class dapui.types.StoppedEventArgs
---@field reason string The reason for the event. For backward compatibility this string is shown in the UI if the `description` attribute is missing (but it must not be translated).
---@field description? string The full reason for the event, e.g. 'Paused on exception'. This string is shown in the UI as is and can be translated.
---@field threadId? integer The thread which was stopped.
---@field preserveFocusHint? boolean A value of true hints to the client that this event should not change the focus.
---@field text? string Additional information. E.g. if reason is `exception`, text contains the exception name. This string is shown in the UI.
---@field allThreadsStopped? boolean If `allThreadsStopped` is true, a debug adapter can announce that all threads have stopped. - The client should use this information to enable that all threads can be expanded to access their stacktraces. - If the attribute is missing or false, only the thread with the given `threadId` can be expanded.
---@field hitBreakpointIds? integer[] Ids of the breakpoints that triggered the event. In most cases there is only a single breakpoint but here are some examples for multiple breakpoints: - Different types of breakpoints map to the same location. - Multiple source breakpoints get collapsed to the same instruction by the compiler/runtime. - Multiple function breakpoints with different function names map to the same location.

--- The event indicates that the execution of the debuggee has stopped due to some condition.
--- This can be caused by a breakpoint previously set, a stepping request has completed, by executing a debugger statement etc.
---@param listener fun(args: dapui.types.StoppedEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.stopped(listener, opts) end

---@class dapui.types.TerminatedEventArgs
---@field restart? any[] | boolean | integer | number | table<string,any> | string A debug adapter may set `restart` to true (or to an arbitrary object) to request that the client restarts the session. The value is not interpreted by the client and passed unmodified as an attribute `__restart` to the `launch` and `attach` requests.

--- The event indicates that debugging of the debuggee has terminated. This does **not** mean that the debuggee itself has exited.
---@param listener fun(args: dapui.types.TerminatedEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.terminated(listener, opts) end

---@class dapui.types.ThreadEventArgs
---@field reason string The reason for the event.
---@field threadId integer The identifier of the thread.

--- The event indicates that a thread has started or exited.
---@param listener fun(args: dapui.types.ThreadEventArgs)
---@param opts? dapui.client.ListenerOpts
function DAPUIEventListenerClient.thread(listener, opts) end

return { request = DAPUIRequestsClient, listen = DAPUIEventListenerClient }
```

## File: `lua/dapui/components/breakpoints.lua`
```
local config = require("dapui.config")
local nio = require("nio")
local util = require("dapui.util")

---@param client dapui.DAPClient
return function(client, send_ready)
  local _disabled_breakpoints = {}

  for _, event in ipairs({
    "setBreakpoints",
    "setFunctionBreakpoints",
    "setInstructionBreakpoints",
    "setDataBreakpoints",
    "breakpoint",
    "stackTrace",
    "terminated",
    "exited",
    "disconnect",
  }) do
    client.listen[event](send_ready)
  end

  ---@param bp dapui.types.DAPBreakpoint
  local function _toggle(bufnr, bp)
    client.breakpoints.toggle(bufnr, bp.line, {
      condition = bp.condition,
      hit_condition = bp.hitCondition,
      log_message = bp.logMessage,
    })

    local buffer_breakpoints = client.breakpoints.get_buf(bufnr)
    local enabled = false
    for _, buf_bp in ipairs(buffer_breakpoints) do
      if buf_bp.line == bp.line then
        enabled = true
        break
      end
    end

    if not _disabled_breakpoints[bufnr] then
      _disabled_breakpoints[bufnr] = {}
    end

    if not enabled then
      bp.enabled = false
      _disabled_breakpoints[bufnr][bp.line] = bp
    else
      _disabled_breakpoints[bufnr][bp.line] = nil
    end
    send_ready()
  end

  local function _get_breakpoints()
    ---@type table<integer, dapui.types.DAPBreakpoint[]>
    local bps = client.breakpoints.get()
    local merged_breakpoints = {}
    local buffers = {}
    for buf, _ in pairs(bps) do
      buffers[buf] = true
    end
    for bufnr, _ in pairs(_disabled_breakpoints) do
      buffers[bufnr] = true
    end
    for bufnr, _ in pairs(buffers) do
      local buf_points = bps[bufnr] or {}
      for _, bp in ipairs(buf_points) do
        bp.enabled = true
        if _disabled_breakpoints[bufnr] then
          _disabled_breakpoints[bufnr][bp.line] = nil
        end
      end
      merged_breakpoints[bufnr] = buf_points
      for _, bp in pairs(_disabled_breakpoints[bufnr] or {}) do
        table.insert(merged_breakpoints[bufnr], bp)
      end
      table.sort(merged_breakpoints[bufnr], function(a, b)
        return a.line < b.line
      end)
    end
    local sorted = {}
    for buffer, breakpoints in pairs(merged_breakpoints) do
      sorted[#sorted + 1] = {
        name = nio.api.nvim_buf_get_name(buffer),
        buffer = buffer,
        breakpoints = breakpoints,
      }
    end
    table.sort(sorted, function(a, b)
      return a.name < b.name
    end)
    return sorted
  end

  return {
    ---@param canvas dapui.Canvas
    render = function(canvas)
      local current_frame = client.session and client.session.current_frame
      local current_line = 0
      local current_file = ""
      if current_frame and current_frame.source and current_frame.source.path then
        current_file = nio.fn.bufname(current_frame.source.path)
        current_line = current_frame.line
      end
      local indent = config.render.indent
      for _, data in ipairs(_get_breakpoints()) do
        local buffer, bufname = data.buffer, data.name
        ---@type dapui.types.DAPBreakpoint[]
        local breakpoints = data.breakpoints
        local name = util.pretty_name(bufname)
        canvas:write(name, { group = "DapUIBreakpointsPath" })
        canvas:write(":\n")

        for _, bp in ipairs(breakpoints) do
          local text = vim.api.nvim_buf_get_lines(buffer, bp.line - 1, bp.line, false)
          local jump_to_bp = util.partial(
            client.lib.jump_to_frame,
            { line = bp.line, column = 0, source = { path = bufname } }
          )
          if vim.tbl_count(text) ~= 0 then
            canvas:add_mapping("open", jump_to_bp)
            canvas:add_mapping("remove", function()
              client.breakpoints.remove(buffer, bp.line)
              send_ready()
            end)
            canvas:add_mapping("toggle", function()
              _toggle(buffer, bp)
            end)
            canvas:write(string.rep(" ", indent))
            local group
            if _disabled_breakpoints[buffer] and _disabled_breakpoints[buffer][bp.line] then
              group = "DapUIBreakpointsDisabledLine"
            elseif bp.line == current_line and name == current_file then
              group = "DapUIBreakpointsCurrentLine"
            else
              group = "DapUIBreakpointsLine"
            end
            canvas:write(tostring(bp.line), { group = group })
            canvas:write(" " .. vim.trim(text[1]) .. "\n")

            local info_indent = indent + #tostring(bp.line) + 1
            local whitespace = string.rep(" ", info_indent)

            local function add_info(message, data)
              canvas:add_mapping("open", jump_to_bp)
              canvas:write(whitespace)
              canvas:write(message, { group = "DapUIBreakpointsInfo" })
              canvas:write(" " .. data .. "\n")
            end

            if bp.logMessage then
              add_info("Log Message:", bp.logMessage)
            end
            if bp.condition then
              add_info("Condition:", bp.condition)
            end
            if bp.hitCondition then
              add_info("Hit Condition:", bp.hitCondition)
            end
          end
        end
        canvas:write("\n")
      end
      if canvas:length() > 1 then
        canvas:remove_line()
        canvas:remove_line()
      else
        canvas:write("")
      end
    end,
  }
end
```

## File: `lua/dapui/components/frames.lua`
```
local config = require("dapui.config")
local util = require("dapui.util")

---@param client dapui.DAPClient
return function(client, send_ready)
  client.listen.scopes(send_ready)
  client.listen.terminated(send_ready)
  client.listen.exited(send_ready)
  client.listen.disconnect(send_ready)

  return {
    ---@async
    ---@param canvas dapui.Canvas
    render = function(canvas, thread_id, show_subtle, indent)
      if not client.session then
        return
      end

      local current_frame_id = nil

      local threads = client.session.threads

      if not threads or not threads[thread_id] then
        return
      end

      local frames = threads[thread_id].frames
      if not frames then
        local success, response = pcall(client.request.stackTrace, { threadId = thread_id })
        frames = success and response.stackFrames
      end
      if not frames then
        return
      end

      if not show_subtle then
        frames = vim.tbl_filter(function(frame)
          return frame.presentationHint ~= "subtle"
        end, frames)
      end

      if client.session then
        current_frame_id = client.session.current_frame and client.session.current_frame.id
      end

      for _, frame in ipairs(frames) do
        local is_current = frame.id == current_frame_id
        canvas:write(string.rep(" ", is_current and (indent - 1) or indent))

        if is_current then
          canvas:write(config.icons.current_frame .. " ")
        end

        canvas:write(
          frame.name,
          { group = frame.id == current_frame_id and "DapUICurrentFrameName" or "DapUIFrameName" }
        )
        canvas:write(" ")

        if frame.source ~= nil then
          local file_name = frame.source.name or frame.source.path or "<unknown>"
          local source_name = util.pretty_name(file_name)
          canvas:write(source_name, { group = "DapUISource" })
        end

        if frame.line ~= nil then
          canvas:write(":")
          canvas:write(frame.line, { group = "DapUILineNumber" })
        end
        canvas:add_mapping("open", util.partial(client.lib.jump_to_frame, frame, true))
        canvas:write("\n")
      end

      canvas:remove_line()
    end,
  }
end
```

## File: `lua/dapui/components/hover.lua`
```
local config = require("dapui.config")
local util = require("dapui.util")

---@class Hover
---@field expression string
---@field expanded boolean
---@field var_component Variables
---@field mode "set" | nil
local Hover = {}

---@param client dapui.DAPClient
return function(client, send_ready)
  ---@return Hover
  local expression
  local expr_context = "hover"
  local expanded = false
  local render_vars = require("dapui.components.variables")(client, send_ready)
  local prompt_func

  return {
    set_expression = function(new_expr, context)
      expression = new_expr
      expr_context = context or "hover"
      send_ready()
    end,
    ---@param canvas dapui.Canvas
    render = function(canvas)
      local frame = client.session and client.session.current_frame
      if not frame then
        return
      end
      if not expression then
        return
      end

      if prompt_func then
        canvas:set_prompt("> ", prompt_func, { fill = expression })
      end

      local success, hover_expr = pcall(
        client.request.evaluate,
        { expression = expression, context = expr_context, frameId = frame.id }
      )

      local var_ref = success and hover_expr.variablesReference

      local prefix
      if not success or hover_expr.variablesReference > 0 then
        prefix = config.icons[expanded and "expanded" or "collapsed"] .. " "
        canvas:write(prefix, { group = success and "DapUIDecoration" or "DapUIWatchesError" })
      end

      canvas:write(expression)

      local val_start = 0
      local value
      if not success then
        canvas:write(": ")
        val_start = canvas:line_width()
        --- Fails formatting if it isn't a DAP error
        value = util.format_error(hover_expr) or error(hover_expr)
      elseif hover_expr then
        local eval_type = util.render_type(hover_expr.type)
        if #eval_type > 0 then
          canvas:write(" ")
          canvas:write(eval_type, { group = "DapUIType" })
        end
        canvas:write(" = ")
        val_start = canvas:line_width()
        value = hover_expr.result
      else
        return
      end
      for _, line in ipairs(util.format_value(val_start, value)) do
        canvas:write(line, { group = "DapUIValue" })
        if success then
          canvas:add_mapping("expand", function()
            expanded = not expanded
            send_ready()
          end)
          canvas:add_mapping("repl", util.partial(util.send_to_repl, expression))
        end
        canvas:add_mapping("edit", function()
          prompt_func = function(new_expr)
            expression = new_expr
            prompt_func = prompt_func
            send_ready()
          end
          send_ready()
        end)
        canvas:write("\n")
      end

      if expanded and var_ref then
        render_vars.render(canvas, expression, var_ref, config.render.indent)
      end
      canvas:remove_line()
    end,
  }
end
```

## File: `lua/dapui/components/scopes.lua`
```
local config = require("dapui.config")
---@param client dapui.DAPClient
return function(client, send_ready)
  local render_vars = require("dapui.components.variables")(client, send_ready)
  local closed_scopes = {}

  ---@param scope dapui.types.Scope
  local function scope_prefix(scope)
    if scope.indexedVariables == 0 then
      return " "
    end
    return config.icons[closed_scopes[scope.name] and "collapsed" or "expanded"]
  end

  ---@type dapui.types.Scope[] | nil
  local _scopes
  client.listen.scopes(function(args)
    if args.response then
      _scopes = args.response.scopes
      -- when new scopes are parsed, automatically disable the scopes that are too expensive to render
      for _, scope in ipairs(_scopes) do
        if scope.expensive then
          closed_scopes[scope.name] = true
        end
      end
    end
    send_ready()
  end)
  local on_exit = function()
    _scopes = nil
    send_ready()
  end
  client.listen.terminated(on_exit)
  client.listen.exited(on_exit)
  client.listen.disconnect(on_exit)

  return {
    ---@param canvas dapui.Canvas
    render = function(canvas)
      -- In case scopes are wiped during render
      local scopes = _scopes
      if not scopes then
        return
      end
      for i, scope in pairs(scopes) do
        canvas:add_mapping("expand", function()
          closed_scopes[scope.name] = not closed_scopes[scope.name]
          send_ready()
        end)

        canvas:write({
          { scope_prefix(scope), group = "DapUIDecoration" },
          " ",
          { scope.name, group = "DapUIScope" },
          { ":\n" },
        })

        -- only render expanded scopes to save resources
        if not closed_scopes[scope.name] then
          render_vars.render(canvas, scope.name, scope.variablesReference, config.render.indent)
        end

        if i < #scopes then
          canvas:write("\n")
        end
      end

      canvas:remove_line()
    end,
  }
end
```

## File: `lua/dapui/components/threads.lua`
```
local config = require("dapui.config")
local frame_renderer = require("dapui.components.frames")

---@param client dapui.DAPClient
---@param send_ready function
return function(client, send_ready)
  ---@type dapui.types.Thread[] | nil
  local _threads = nil

  client.listen.threads(function(args)
    _threads = args.response.threads
  end)
  client.listen.scopes(function()
    send_ready()
  end)

  local on_exit = function()
    _threads = nil
    send_ready()
  end
  client.listen.terminated(on_exit)
  client.listen.exited(on_exit)
  client.listen.disconnect(on_exit)

  local render_frames = frame_renderer(client, send_ready)
  local subtle_threads = {}
  return {
    ---@param canvas dapui.Canvas
    render = function(canvas, indent)
      -- In case threads are wiped during render
      local threads = _threads
      local session = client.session
      if not threads or not session then
        return
      end

      indent = indent or 0

      ---@param thread dapui.types.Thread
      local function render_thread(thread, match_group)
        local first_line = canvas:length()

        canvas:write({ { thread.name, group = match_group }, ":\n" })

        render_frames.render(
          canvas,
          thread.id,
          subtle_threads[thread.id] or false,
          indent + config.render.indent
        )

        local last_line = canvas:length()

        for line = first_line, last_line, 1 do
          canvas:add_mapping("toggle", function()
            subtle_threads[thread.id] = not subtle_threads[thread.id]
            send_ready()
          end, { line = line })
        end

        canvas:write("\n\n")
      end

      local stopped_thread_id = session.stopped_thread_id

      for _, thread in pairs(threads) do
        if thread.id == stopped_thread_id then
          render_thread(thread, "DapUIStoppedThread")
        end
      end
      for _, thread in pairs(threads) do
        if thread.id ~= stopped_thread_id then
          render_thread(thread, "DapUIThread")
        end
      end

      -- canvas:remove_line()
      -- canvas:remove_line()
    end,
  }
end
```

## File: `lua/dapui/components/variables.lua`
```
local config = require("dapui.config")
local util = require("dapui.util")
local partial = util.partial
local nio = require("nio")

---@class Variables
---@field frame_expanded_children table
---@field child_components table<number, Variables>
---@field var_to_set table | nil
---@field mode "set" | nil
---@field rendered_step integer | nil
---@field rendered_vars table[] | nil
local Variables = {}

---@param client dapui.DAPClient
---@param send_ready function
return function(client, send_ready)
  local expanded_children = {}

  ---@type fun(value: string) | nil
  local prompt_func
  ---@type string | nil
  local prompt_fill
  ---@type table<string, string>
  local rendered_vars = {}

  local function reference_prefix(path, variable)
    if variable.variablesReference == 0 then
      return " "
    end
    return config.icons[expanded_children[path] and "expanded" or "collapsed"]
  end

  ---@param path string
  local function path_changed(path, value)
    return rendered_vars[path] and rendered_vars[path] ~= value
  end

  ---@param canvas dapui.Canvas
  ---@param parent_path string
  ---@param parent_ref integer
  ---@param indent integer
  local function render(canvas, parent_path, parent_ref, indent)
    if not canvas.prompt and prompt_func then
      canvas:set_prompt("> ", prompt_func, { fill = prompt_fill })
    end
    indent = indent or 0
    local success, var_data = pcall(client.request.variables, { variablesReference = parent_ref })
    local variables = success and var_data.variables or {}
    if config.render.sort_variables then
      table.sort(variables, config.render.sort_variables)
    end
    for _, variable in pairs(variables) do
      local var_path = parent_path .. "." .. variable.name

      canvas:write({
        string.rep(" ", indent),
        { reference_prefix(var_path, variable), group = "DapUIDecoration" },
        " ",
        { variable.name, group = "DapUIVariable" },
      })

      local var_type = util.render_type(variable.type)
      if #var_type > 0 then
        canvas:write({ " ", { var_type, group = "DapUIType" } })
      end

      local var_group
      if path_changed(var_path, variable.value) then
        var_group = "DapUIModifiedValue"
      else
        var_group = "DapUIValue"
      end
      rendered_vars[var_path] = variable.value
      local function add_var_line(line)
        if variable.variablesReference > 0 then
          canvas:add_mapping("expand", function()
            expanded_children[var_path] = not expanded_children[var_path]
            send_ready()
          end)
          if variable.evaluateName then
            canvas:add_mapping("repl", partial(util.send_to_repl, variable.evaluateName))
          end
        end
        canvas:add_mapping("edit", function()
          prompt_func = function(new_value)
            nio.run(function()
              prompt_func = nil
              prompt_fill = nil
              client.lib.set_variable(parent_ref, variable, new_value)
              send_ready()
            end)
          end
          prompt_fill = variable.value
          send_ready()
        end)
        canvas:write(line .. "\n", { group = var_group })
      end

      if #(variable.value or "") > 0 then
        canvas:write(" = ")
        local value_start = #canvas.lines[canvas:length()]
        local value = variable.value

        for _, line in ipairs(util.format_value(value_start, value)) do
          add_var_line(line)
        end
      else
        add_var_line(variable.value)
      end

      if expanded_children[var_path] and variable.variablesReference ~= 0 then
        render(canvas, var_path, variable.variablesReference, indent + config.render.indent)
      end
    end
  end

  return {
    render = render,
  }
end
```

## File: `lua/dapui/components/watches.lua`
```
local config = require("dapui.config")
local util = require("dapui.util")

local partial = util.partial

---@class dapui.watches.Watch
---@field expression string
---@field expanded boolean

---@param client dapui.DAPClient
return function(client, send_ready)
  local running = false
  client.listen.scopes(function()
    running = true
    send_ready()
  end)
  local on_exit = function()
    running = false
    send_ready()
  end

  client.listen.terminated(on_exit)
  client.listen.exited(on_exit)
  client.listen.disconnect(on_exit)

  ---@type dapui.watches.Watch[]
  local watches = {}
  local edit_index = nil
  local rendered_exprs = {}
  local rendered_step = client.lib.step_number()
  local render_vars = require("dapui.components.variables")(client, send_ready)

  local function add_watch(value)
    if #value > 0 then
      watches[#watches + 1] = {
        expression = value,
        expanded = false,
      }
      send_ready()
    end
  end

  local function edit_expr(new_value, index)
    index = index or edit_index
    edit_index = nil
    if #new_value > 0 then
      watches[index].expression = new_value
    end
    send_ready()
  end

  local function remove_expr(expr_i)
    table.remove(watches, expr_i)
    send_ready()
  end

  local function toggle_expression(expr_i)
    watches[expr_i].expanded = not watches[expr_i].expanded
    send_ready()
  end

  return {
    add = add_watch,
    edit = edit_expr,
    remove = remove_expr,
    get = function()
      return vim.deepcopy(watches)
    end,
    expand = toggle_expression,
    ---@param canvas dapui.Canvas
    render = function(canvas)
      if not edit_index then
        canvas:set_prompt("> ", add_watch)
      else
        canvas:set_prompt("> ", edit_expr, { fill = watches[edit_index].expression })
      end

      if vim.tbl_count(watches) == 0 then
        canvas:write("No Expressions\n", { group = "DapUIWatchesEmpty" })
        return
      end
      local frame_id = client.session
        and client.session.current_frame
        and client.session.current_frame.id
      local step = client.lib.step_number()
      for i, watch in pairs(watches) do
        local success, evaluated
        if running then
          success, evaluated = pcall(
            client.request.evaluate,
            { context = "watch", expression = watch.expression, frameId = frame_id }
          )
        else
          success, evaluated = false, { message = "No active session" }
        end
        local prefix = config.icons[watch.expanded and "expanded" or "collapsed"]

        canvas:write({
          { prefix, group = success and "DapUIWatchesValue" or "DapUIWatchesError" },
          " " .. watch.expression,
        })

        local value = ""
        if not success then
          watch.expanded = false
          canvas:write(": ")
          value = util.format_error(evaluated)
        else
          local eval_type = util.render_type(evaluated.type)
          if #eval_type > 0 then
            canvas:write({ " ", { eval_type, group = "DapUIType" } })
          end
          canvas:write(" = ")
          value = evaluated.result
        end
        local val_start = canvas:line_width()
        local var_group

        if not success or rendered_exprs[i] == evaluated.result then
          var_group = "DapUIValue"
        else
          var_group = "DapUIModifiedValue"
        end

        for _, line in ipairs(util.format_value(val_start, value)) do
          canvas:write(line, { group = var_group })
          canvas:add_mapping("remove", partial(remove_expr, i))
          canvas:add_mapping("edit", function()
            edit_index = i
            send_ready()
          end)
          if success then
            canvas:add_mapping("expand", partial(toggle_expression, i))
            canvas:add_mapping("repl", partial(util.send_to_repl, watch.expression))
          end
          canvas:write("\n")
        end

        local var_ref = success and evaluated.variablesReference or 0
        if watch.expanded and var_ref > 0 then
          render_vars.render(canvas, watch.expression, var_ref, config.render.indent)
        end
        if rendered_step ~= step then
          rendered_exprs[i] = evaluated.result
        end
      end
      if rendered_step ~= step then
        rendered_step = step
      end
    end,
  }
end
```

## File: `lua/dapui/config/highlights.lua`
```
local M = {}

local control_hl_groups = {
  "DapUINormal",
  "DapUIPlayPause",
  "DapUIRestart",
  "DapUIStop",
  "DapUIUnavailable",
  "DapUIStepOver",
  "DapUIStepInto",
  "DapUIStepBack",
  "DapUIStepOut",
}

function M.setup()
  vim.cmd([[
  hi default link DapUINormal                  Normal
  hi default link DapUIVariable                Normal
  hi default link DapUIScope                   Identifier
  hi default link DapUIType                    Type
  hi default link DapUIValue                   Normal
  hi default link DapUIModifiedValue           Function
  hi default link DapUIDecoration              Identifier
  hi default link DapUIThread                  Identifier
  hi default link DapUIStoppedThread           Function
  hi default link DapUIFrameName               Normal
  hi default link DapUISource                  Define
  hi default link DapUILineNumber              LineNr
  hi default link DapUIFloatNormal             NormalFloat
  hi default link DapUIFloatBorder             Identifier
  hi default link DapUIWatchesEmpty            PreProc
  hi default link DapUIWatchesValue            Statement
  hi default link DapUIWatchesError            PreProc
  hi default link DapUIBreakpointsPath         Identifier
  hi default link DapUIBreakpointsInfo         Statement
  hi default link DapUIBreakpointsCurrentLine  CursorLineNr
  hi default link DapUIBreakpointsLine         DapUILineNumber
  hi default link DapUIBreakpointsDisabledLine Comment
  hi default link DapUICurrentFrameName        DapUIBreakpointsCurrentLine
  hi default link DapUIStepOver                Label
  hi default link DapUIStepInto                Label
  hi default link DapUIStepBack                Label
  hi default link DapUIStepOut                 Label
  hi default link DapUIStop                    PreProc
  hi default link DapUIPlayPause               Repeat
  hi default link DapUIRestart                 Repeat
  hi default link DapUIUnavailable             Comment
  hi default link DapUIWinSelect               Special
  hi default link DapUIEndofBuffer             EndofBuffer
  ]])

  ---gets the argument highlight group information, using the newer `nvim_get_hl` if available
  ---@param highlight string highlight group
  ---@return table hl highlight information
  local function get_highlight(highlight)
    local ok, hl
    if vim.fn.has("nvim-0.9") == 1 then
      ok, hl = pcall(vim.api.nvim_get_hl, 0, { name = highlight })
      if not ok then -- highlight group is invalid
        return vim.empty_dict()
      end
    else
      ok, hl = pcall(vim.api.nvim_get_hl_by_name, highlight, true)
      if not ok or hl[true] then -- highlight group is invalid or cleared
        return vim.empty_dict()
      end
      -- change `nvim_get_hl_by_name` output into `nvim_get_hl` output format
      hl.bg = hl.background
      hl.fg = hl.foreground
    end
    return hl
  end

  -- Generate *NC variants of the control highlight groups
  if vim.fn.has("nvim-0.8") == 1 then
    local bg = get_highlight("WinBar").bg
    local bgNC = get_highlight("WinBarNC").bg

    for _, hl_group in pairs(control_hl_groups) do
      local gui = get_highlight(hl_group)
      -- if highlight group is cleared or invalid, skip
      if not vim.tbl_isempty(gui) then
        gui.default = true
        if gui.bg ~= bg then
          gui.bg = bg
          vim.api.nvim_set_hl(0, hl_group, gui)
        end
        gui.bg = bgNC
        vim.api.nvim_set_hl(0, hl_group .. "NC", gui)
      end
    end
  else
    for _, hl_group in pairs(control_hl_groups) do
      vim.cmd(string.format("hi default link %sNC %s", hl_group, hl_group))
    end
  end
end

vim.cmd([[
  augroup DAPUIRefreshHighlights
    autocmd!
    autocmd ColorScheme * lua require('dapui.config.highlights').setup()
  augroup END
]])

return M
```

## File: `lua/dapui/config/init.lua`
```
local dapui = {}

---@tag dapui.config
---@toc_entry Configuration Options

---@class dapui.Config
---@field wrap boolean Whether or not to wrap UI text
---@field icons dapui.Config.icons
---@field mappings table<dapui.Action, string|string[]> Keys to trigger actions in elements
---@field element_mappings table<string, table<dapui.Action, string|string[]>> Per-element overrides of global mappings
---@field expand_lines boolean Expand current line to hover window if larger
--- than window size
---@field force_buffers boolean Prevents other buffers being loaded into
--- nvim-dap-ui windows
---@field layouts dapui.Config.layout[] Layouts to display elements within.
--- Layouts are opened in the order defined
---@field floating dapui.Config.floating Floating window specific options
---@field controls dapui.Config.controls Controls configuration
---@field render dapui.Config.render Rendering options which can be updated
--- after initial setup
---@field select_window? fun(): integer A function which returns a window to be
--- used for opening buffers such as a stack frame location.

---@class dapui.Config.icons
---@field expanded string
---@field collapsed string
---@field current_frame string

---@class dapui.Config.layout
---@field elements string[]|dapui.Config.layout.element[] Elements to display
--- in this layout
---@field size number Size of the layout in lines/columns
---@field position "left"|"right"|"top"|"bottom" Which side of editor to open
--- layout on

---@class dapui.Config.layout.element
---@field id string Element ID
---@field size number Size of the element in lines/columns or as proportion of
--- total editor size (0-1)

---@class dapui.Config.floating
---@field max_height? number Maximum height of floating window (integer or float
--- between 0 and 1)
---@field max_width? number Maximum width of floating window (integer or float
--- between 0 and 1)
---@field border string|string[] Border argument supplied to `nvim_open_win`
---@field mappings table<dapui.FloatingAction, string|string[]> Keys to trigger
--- actions in elements

---@class dapui.Config.controls
---@field enabled boolean Show controls on an element (requires winbar feature)
---@field element string Element to show controls on
---@field icons dapui.Config.controls.icons

---@class dapui.Config.controls.icons
---@field pause string
---@field play string
---@field step_into string
---@field step_over string
---@field step_out string
---@field step_back string
---@field run_last string
---@field terminate string

---@class dapui.Config.render
---@field indent integer Default indentation size
---@field max_type_length? integer Maximum number of characters to allow a type
--- name to fill before trimming
---@field max_value_lines? integer Maximum number of lines to allow a value to
--- fill before trimming
---@field sort_variables? fun(a: dapui.types.Variable, b: dapui.types.Variable):boolean Sorting function to determine
--- render order of variables.

---@alias dapui.Action "expand"|"open"|"remove"|"edit"|"repl"|"toggle"

---@alias dapui.FloatingAction "close"

---@type dapui.Config
---@nodoc
local default_config = {
  wrap = false,
  icons = { expanded = "", collapsed = "", current_frame = "" },
  mappings = {
    -- Use a table to apply multiple mappings
    expand = { "<CR>", "<2-LeftMouse>" },
    open = "o",
    remove = "d",
    edit = "e",
    repl = "r",
    toggle = "t",
  },
  element_mappings = {},
  expand_lines = vim.fn.has("nvim-0.7") == 1,
  force_buffers = true,
  layouts = {
    {
      -- You can change the order of elements in the sidebar
      elements = {
        -- Provide IDs as strings or tables with "id" and "size" keys
        {
          id = "scopes",
          size = 0.25, -- Can be float or integer > 1
        },
        { id = "breakpoints", size = 0.25 },
        { id = "stacks", size = 0.25 },
        { id = "watches", size = 0.25 },
      },
      size = 40,
      position = "left", -- Can be "left" or "right"
    },
    {
      elements = {
        "repl",
        "console",
      },
      size = 10,
      position = "bottom", -- Can be "bottom" or "top"
    },
  },
  floating = {
    max_height = nil,
    max_width = nil,
    border = "single",
    mappings = {
      ["close"] = { "q", "<Esc>" },
    },
  },
  controls = {
    enabled = vim.fn.exists("+winbar") == 1,
    element = "repl",
    icons = {
      pause = "",
      play = "",
      step_into = "",
      step_over = "",
      step_out = "",
      step_back = "",
      run_last = "",
      terminate = "",
      disconnect = "",
    },
  },
  render = {
    max_type_length = nil, -- Can be integer or nil.
    max_value_lines = 100, -- Can be integer or nil.
    indent = 1,
  },
}

local user_config = default_config

local function fill_elements(area)
  area = vim.deepcopy(area)
  local filled = {}
  if vim.fn.has("nvim-0.11") == 1 then
    vim.validate("size", area.size, "number")
    vim.validate("elements", area.elements, "table")
    vim.validate("position", area.position, "string")
  else
    vim.validate({
      size = { area.size, "number" },
      elements = { area.elements, "table" },
      position = { area.position, "string" },
    })
  end
  for i, element in ipairs(area.elements) do
    if type(element) == "string" then
      filled[i] = { id = element, size = 1 / #area.elements }
    else
      filled[i] = element
    end
  end
  area.elements = filled
  return area
end

local function fill_mappings(mappings)
  local filled = {}
  for action, keys in pairs(mappings) do
    filled[action] = type(keys) == "table" and keys or { keys }
  end
  return filled
end

---@class dapui.config : dapui.Config
---@nodoc
dapui.config = {}

function dapui.config.setup(config)
  config = config or {}
  local filled = vim.tbl_deep_extend("keep", config, default_config)

  if config.layouts then
    filled.layouts = config.layouts
  end
  filled.mappings = fill_mappings(filled.mappings)

  local element_mappings = {}
  for elem, mappings in pairs(filled.element_mappings) do
    element_mappings[elem] = fill_mappings(mappings)
  end

  filled.element_mappings = element_mappings
  filled.floating.mappings = fill_mappings(filled.floating.mappings)
  for i, layout in ipairs(filled.layouts) do
    filled.layouts[i] = fill_elements(layout)
  end

  user_config = filled
  require("dapui.config.highlights").setup()
end

function dapui.config._format_default()
  local lines = { "Default values:", ">lua" }
  for line in vim.gsplit(vim.inspect(default_config), "\n", true) do
    table.insert(lines, "  " .. line)
  end
  table.insert(lines, "<")
  return lines
end

---@param update dapui.Config.render
---@nodoc
function dapui.config.update_render(update)
  user_config.render = vim.tbl_deep_extend("keep", update, user_config.render)
end

function dapui.config.element_mapping(element)
  return vim.tbl_extend("keep", user_config.element_mappings[element] or {}, user_config.mappings)
end

setmetatable(dapui.config, {
  __index = function(_, key)
    return user_config[key]
  end,
})

dapui.config.setup()

return dapui.config
```

## File: `lua/dapui/elements/breakpoints.lua`
```
local config = require("dapui.config")
local Canvas = require("dapui.render.canvas")
local util = require("dapui.util")

---@param client dapui.DAPClient
---@nodoc
return function(client)
  local dapui = { elements = {} }

  ---@class dapui.elements.breakpoints
  ---@toc_entry Breakpoints
  ---@text
  --- Lists all breakpoints currently set.
  ---
  --- Mappings:
  --- - `open`: Jump to the location the breakpoint is set
  --- - `toggle`: Enable/disable the selected breakpoint
  dapui.elements.breakpoints = {
    allow_without_session = true,
  }

  local send_ready = util.create_render_loop(function()
    dapui.elements.breakpoints.render()
  end)

  local breakpoints = require("dapui.components.breakpoints")(client, send_ready)

  ---@nodoc
  function dapui.elements.breakpoints.render()
    local canvas = Canvas.new()
    breakpoints.render(canvas)
    canvas:render_buffer(dapui.elements.breakpoints.buffer(), config.element_mapping("breakpoints"))
  end

  ---@nodoc
  dapui.elements.breakpoints.buffer = util.create_buffer("DAP Breakpoints", {
    filetype = "dapui_breakpoints",
  })

  return dapui.elements.breakpoints
end
```

## File: `lua/dapui/elements/console.lua`
```
local nio = require("nio")
local dap = require("dap")
local util = require("dapui.util")

return function()
  local dapui = { elements = {} }

  ---@class dapui.elements.console
  ---@toc_entry Console
  ---@text
  --- The console window used by nvim-dap for the integrated terminal.
  dapui.elements.console = {}

  local console_buf = -1
  local autoscroll = true
  ---@nodoc
  local function get_buf()
    if nio.api.nvim_buf_is_valid(console_buf) then
      return console_buf
    end
    console_buf = util.create_buffer("DAP Console", { filetype = "dapui_console" })()
    if vim.fn.has("nvim-0.7") == 1 then
      vim.keymap.set("n", "G", function()
        autoscroll = true
        vim.cmd("normal! G")
      end, { silent = true, buffer = console_buf })
      nio.api.nvim_create_autocmd({ "InsertEnter", "CursorMoved" }, {
        group = nio.api.nvim_create_augroup("dap-repl-au", { clear = true }),
        buffer = console_buf,
        callback = function()
          local active_buf = nio.api.nvim_win_get_buf(0)
          if active_buf == console_buf then
            local lnum = nio.api.nvim_win_get_cursor(0)[1]
            autoscroll = lnum == nio.api.nvim_buf_line_count(console_buf)
          end
        end,
      })
      nio.api.nvim_buf_attach(console_buf, false, {
        on_lines = function(_, _, _, _, _, _)
          local active_buf = nio.api.nvim_win_get_buf(0)

          if autoscroll and vim.fn.mode() == "n" and active_buf == console_buf then
            vim.cmd("normal! G")
          end
        end,
      })
    end
    return console_buf
  end

  dap.defaults.fallback.terminal_win_cmd = get_buf

  function dapui.elements.console.render() end

  function dapui.elements.console.buffer()
    return get_buf()
  end

  function dapui.elements.console.float_defaults()
    return { width = 80, height = 20, enter = true }
  end

  return dapui.elements.console
end
```

## File: `lua/dapui/elements/hover.lua`
```
local config = require("dapui.config")
local util = require("dapui.util")
local Canvas = require("dapui.render.canvas")

return function(client)
  local dapui = { elements = {} }

  ---@class dapui.elements.hover
  dapui.elements.hover = {}

  local send_ready = util.create_render_loop(function()
    dapui.elements.hover.render()
  end)

  local hover = require("dapui.components.hover")(client, send_ready)

  ---@nodoc
  function dapui.elements.hover.render()
    local canvas = Canvas.new()
    hover.render(canvas)
    canvas:render_buffer(dapui.elements.hover.buffer(), config.element_mapping("hover"))
  end

  ---@nodoc
  dapui.elements.hover.buffer = util.create_buffer("DAP Hover", {
    filetype = "dapui_hover",
  })

  ---Set the expression for the hover window
  ---@param expression string
  function dapui.elements.hover.set_expression(expression, context)
    hover.set_expression(expression, context)
  end

  return dapui.elements.hover
end
```

## File: `lua/dapui/elements/repl.lua`
```
local nio = require("nio")
local dap = require("dap")

return function()
  local dapui = { elements = {} }

  ---@class dapui.elements.repl
  ---@toc_entry REPL
  ---@text
  --- The REPL provided by nvim-dap.
  dapui.elements.repl = {}

  ---@nodoc
  local function get_buffer()
    -- TODO: All of this is a hack because of an error with indentline when buffer
    -- is opened in a window so have to manually find the window that was opened.
    local all_wins = nio.api.nvim_list_wins()
    local open_wins = {}
    for _, win in pairs(all_wins) do
      open_wins[win] = true
    end
    pcall(dap.repl.open, {})

    local buf = nio.fn.bufnr("dap-repl")

    for _, win in ipairs(nio.api.nvim_list_wins()) do
      if not open_wins[win] then
        pcall(nio.api.nvim_win_close, win, true)
        break
      end
    end
    return buf
  end

  local buf
  ---@nodoc
  function dapui.elements.repl.render() end

  ---@nodoc
  function dapui.elements.repl.buffer()
    if not nio.api.nvim_buf_is_valid(buf or -1) then
      buf = get_buffer()
    end
    return buf
  end

  ---@nodoc
  function dapui.elements.repl.float_defaults()
    return { width = 80, height = 20, enter = true }
  end

  return dapui.elements.repl
end
```

## File: `lua/dapui/elements/scopes.lua`
```
local config = require("dapui.config")
local util = require("dapui.util")
local Canvas = require("dapui.render.canvas")

return function(client)
  local dapui = { elements = {} }

  ---@class dapui.elements.scopes
  ---@toc_entry Variable Scopes
  ---@text
  --- Displays the available scopes and variables within them.
  ---
  --- Mappings:
  --- - `edit`: Edit the value of a variable
  --- - `expand`: Toggle showing any children of variable.
  --- - `repl`: Send variable to REPL
  dapui.elements.scopes = {}

  local send_ready = util.create_render_loop(function()
    dapui.elements.scopes.render()
  end)

  local scopes = require("dapui.components.scopes")(client, send_ready)

  ---@nodoc
  function dapui.elements.scopes.render()
    local canvas = Canvas.new()
    scopes.render(canvas)
    canvas:render_buffer(dapui.elements.scopes.buffer(), config.element_mapping("scopes"))
  end

  ---@nodoc
  dapui.elements.scopes.buffer = util.create_buffer("DAP Scopes", {
    filetype = "dapui_scopes",
  })

  return dapui.elements.scopes
end
```

## File: `lua/dapui/elements/stacks.lua`
```
local config = require("dapui.config")
local Canvas = require("dapui.render.canvas")
local util = require("dapui.util")

return function(client)
  local dapui = { elements = {} }

  ---@class dapui.elements.stacks
  ---@toc_entry Threads and Stack Frames
  ---@text
  --- Displays the running threads and their stack frames.
  ---
  --- Mappings:
  --- - `open`: Jump to a place within the stack frame.
  --- - `toggle`: Toggle displaying subtle frames
  dapui.elements.stacks = {}

  local send_ready = util.create_render_loop(function()
    dapui.elements.stacks.render()
  end)

  local threads = require("dapui.components.threads")(client, send_ready)

  ---@nodoc
  function dapui.elements.stacks.render()
    local canvas = Canvas.new()
    threads.render(canvas)
    canvas:render_buffer(dapui.elements.stacks.buffer(), config.element_mapping("stacks"))
  end

  ---@nodoc
  dapui.elements.stacks.buffer = util.create_buffer("DAP Stacks", {
    filetype = "dapui_stacks",
  })

  return dapui.elements.stacks
end
```

## File: `lua/dapui/elements/watches.lua`
```
local util = require("dapui.util")
local config = require("dapui.config")
local Canvas = require("dapui.render.canvas")

return function(client)
  local dapui = { elements = {} }

  ---@class dapui.elements.watches
  ---@toc_entry Watch Expressions
  ---@text
  --- Allows creation of expressions to watch the value of in the context of the
  --- current frame.
  --- This uses a prompt buffer for input. To enter a new expression, just enter
  --- insert mode and you will see a prompt appear. Press enter to submit
  ---
  --- Mappings:
  ---
  --- - `expand`: Toggle showing the children of an expression.
  --- - `remove`: Remove the watched expression.
  --- - `edit`: Edit an expression or set the value of a child variable.
  --- - `repl`: Send expression to REPL
  dapui.elements.watches = {
    allow_without_session = true,
  }

  local send_ready = util.create_render_loop(function()
    dapui.elements.watches.render()
  end)

  local watches = require("dapui.components.watches")(client, send_ready)

  --- Add a new watch expression
  ---@param expr? string
  function dapui.elements.watches.add(expr)
    if not expr then
      expr = util.get_current_expr()
    end
    watches.add(expr)
  end

  --- Change the chosen watch expression
  ---@param index integer
  ---@param new_expr string
  function dapui.elements.watches.edit(index, new_expr)
    watches.edit(new_expr, index)
  end

  --- Remove the chosen watch expression
  function dapui.elements.watches.remove(index)
    watches.remove(index)
  end

  --- Get the current list of watched expressions
  ---@return dapui.elements.watches.Watch[]
  function dapui.elements.watches.get()
    return watches.get()
  end

  ---@class dapui.elements.watches.Watch
  ---@field expression string
  ---@field expanded boolean

  --- Toggle the expanded state of the chosen watch expression
  ---@param index integer
  function dapui.elements.watches.toggle_expand(index)
    watches.expand(index)
  end

  ---@nodoc
  function dapui.elements.watches.render()
    local canvas = Canvas.new()
    watches.render(canvas)
    canvas:render_buffer(dapui.elements.watches.buffer(), config.element_mapping("watches"))
  end

  ---@nodoc
  dapui.elements.watches.buffer = util.create_buffer("DAP Watches", {
    filetype = "dapui_watches",
    omnifunc = "v:lua.require'dap'.omnifunc",
  })

  return dapui.elements.watches
end
```

## File: `lua/dapui/render/canvas.lua`
```
local M = {}

local api = vim.api

local util = require("dapui.util")
local config = require("dapui.config")
M.namespace = api.nvim_create_namespace("dapui")

---@class dapui.Canvas
---@field lines table
---@field matches table
---@field mappings table
---@field prompt table
---@field valid boolean
---@field expand_lines boolean
local Canvas = {}

---@type dapui.Action[]
local all_actions = { "expand", "open", "remove", "edit", "repl", "toggle" }

---@return dapui.Canvas
function Canvas:new()
  local mappings = {}
  for _, action in pairs(all_actions) do
    mappings[action] = {}
  end
  local canvas = {
    lines = { "" },
    matches = {},
    mappings = mappings,
    prompt = nil,
    valid = true,
    expand_lines = config.expand_lines,
  }
  setmetatable(canvas, self)
  self.__index = self
  return canvas
end

function Canvas:write(text, opts)
  if type(text) == "table" then
    for _, line in pairs(text) do
      if type(line) == "table" then
        self:write(line[1], line)
      else
        self:write(line)
      end
    end
    return
  end

  if type(text) ~= "string" then
    text = tostring(text)
  end
  opts = opts or {}
  local lines = vim.split(text, "[\r]?\n", { plain = false, trimempty = false })
  if #self.lines == 0 then
    self.lines = { "" }
  end
  for i, line in ipairs(lines) do
    local cur_line = self.lines[#self.lines]
    self.lines[#self.lines] = cur_line .. line
    if opts.group and #line > 0 then
      self.matches[#self.matches + 1] = { opts.group, { #self.lines, #cur_line + 1, #line } }
    end
    if i < #lines then
      table.insert(self.lines, "")
    end
  end
end

function Canvas:line_width(line)
  line = line or self:length()
  return #(self.lines[line] or "")
end

--- Remove the last line from state
function Canvas:remove_line()
  self.lines[#self.lines] = nil
end

function Canvas:reset()
  self.lines = {}
  self.matches = {}
  for _, action in pairs(vim.tbl_keys(self.mappings)) do
    self.mappings[action] = {}
  end
end

---Add a mapping for a specific line
---@param action dapui.Action
---@param callback function Callback for when mapping is used
---@param opts? table Optional extra arguments
-- Extra arguments currently accepts:
--   `line` Line to map to, defaults to last in state
function Canvas:add_mapping(action, callback, opts)
  opts = opts or {}
  local line = opts.line or self:length()
  if line == 0 then
    line = 1
  end
  self.mappings[action][line] = self.mappings[action][line] or {}
  self.mappings[action][line][#self.mappings[action][line] + 1] = callback
end

function Canvas:set_prompt(text, callback, opts)
  opts = opts or {}
  self.prompt = { text = text, callback = callback, fill = opts.fill, enter = opts.enter or false }
end

---Get the number of lines in state
function Canvas:length()
  return #self.lines
end

---Get the length of the longest line in state
function Canvas:width()
  local width = 0
  for _, line in pairs(self.lines) do
    width = width < #line and #line or width
  end
  return width
end

function Canvas:set_expand_lines(value)
  self.expand_lines = value
end

---Apply a render.canvas to a buffer
---@param buffer number
function Canvas:render_buffer(buffer, action_keys)
  local success, _ = pcall(api.nvim_buf_set_option, buffer, "modifiable", true)
  if not success then
    return false
  end

  for action, line_callbacks in pairs(self.mappings) do
    util.apply_mapping(action_keys[action], function(line)
      line = line or vim.fn.line(".")
      local callbacks = line_callbacks[line]
      if not callbacks then
        util.notify("No " .. action .. " action for current line", vim.log.levels.INFO)
        return
      end
      for _, callback in pairs(callbacks) do
        callback()
      end
    end, buffer, action)
  end

  local lines = self.lines
  local matches = self.matches
  api.nvim_buf_clear_namespace(buffer, M.namespace, 0, -1)
  api.nvim_buf_set_lines(buffer, 0, #lines, false, lines)
  local last_line = vim.fn.getbufinfo(buffer)[1].linecount
  if last_line > #lines then
    api.nvim_buf_set_lines(buffer, #lines, last_line, false, {})
  end
  for _, match in pairs(matches) do
    local pos = match[2]
    pcall(
      api.nvim_buf_set_extmark,
      buffer,
      M.namespace,
      pos[1] - 1,
      (pos[2] or 1) - 1,
      { end_col = pos[3] and (pos[2] + pos[3] - 1), hl_group = match[1] }
    )
  end
  if self.expand_lines then
    local group = api.nvim_create_augroup(
      "DAPUIExpandLongLinesFor" .. vim.fn.bufname(buffer):gsub("DAP ", ""),
      { clear = true }
    )
    api.nvim_create_autocmd({ "CursorMoved", "WinScrolled" }, {
      buffer = buffer,
      group = group,
      callback = function()
        vim.schedule(require("dapui.render.line_hover").show)
      end,
    })
  end
  if self.prompt then
    api.nvim_buf_set_option(buffer, "buftype", "prompt")
    vim.fn.prompt_setprompt(buffer, self.prompt.text)
    vim.fn.prompt_setcallback(buffer, function(value)
      vim.cmd("stopinsert")
      self.prompt.callback(value)
    end)
    if self.prompt.fill then
      api.nvim_buf_set_lines(buffer, -1, -1, true, { "> " .. self.prompt.fill })
      if api.nvim_get_current_buf() == buffer then
        api.nvim_input("A")
      end
    end
    api.nvim_buf_set_option(buffer, "modified", false)
    local group = api.nvim_create_augroup("DAPUIPromptSetUnmodified" .. buffer, {})
    api.nvim_create_autocmd({ "ExitPre" }, {
      buffer = buffer,
      group = group,
      callback = function()
        api.nvim_buf_set_option(buffer, "modified", false)
      end,
    })
  else
    api.nvim_buf_set_option(buffer, "modifiable", false)
    api.nvim_buf_set_option(buffer, "buftype", "nofile")
  end
  return true
end

--- @return dapui.Canvas
function M.new()
  return Canvas:new()
end

return M
```

## File: `lua/dapui/render/init.lua`
```
local M = {}

local canvas = require("dapui.render.canvas")

M.new_canvas = canvas.new

return M
```

## File: `lua/dapui/render/line_hover.lua`
```
local M = {}

local api = vim.api
local namespace = api.nvim_create_namespace("dapui")

local buf_wins = {}

local function create_buffer(content)
  local buf_nr = api.nvim_create_buf(false, true)
  vim.fn.setbufline(buf_nr, 1, content)
  api.nvim_buf_set_option(buf_nr, "bufhidden", "wipe")
  api.nvim_buf_set_option(buf_nr, "modified", false)

  return buf_nr
end

local function auto_close(win_id, buf_id, orig_line, orig_text)
  if not api.nvim_win_is_valid(win_id) then
    return
  end
  local group = api.nvim_create_augroup("DAPUILongLineExpand" .. buf_id, { clear = true })
  api.nvim_create_autocmd({ "WinEnter", "TabClosed", "CursorMoved", "WinScrolled" }, {
    callback = function()
      if not api.nvim_win_is_valid(win_id) then
        return
      end
      local cur_line = vim.fn.line(".")
      if
        api.nvim_get_current_buf() == buf_id
        and orig_line == cur_line
        and vim.api.nvim_buf_get_lines(buf_id, cur_line - 1, cur_line, false)[1] == orig_text
      then
        auto_close(win_id, buf_id, orig_line)
        return
      end
      buf_wins[vim.api.nvim_get_current_buf()] = nil
      local ok, error = pcall(api.nvim_win_close, win_id, true)
      if not ok then
        require("dapui.util").notify(error, vim.log.levels.DEBUG)
      end
    end,
    once = true,
    group = group,
  })
end

function M.show()
  local buffer = api.nvim_get_current_buf()
  if api.nvim_win_get_config(0).relative ~= "" then
    return
  end

  local orig_line, orig_col = unpack(api.nvim_win_get_cursor(0))
  orig_line = orig_line - 1

  local line_content = vim.fn.getline("."):sub(orig_col + 1)
  local content_width = vim.str_utfindex(line_content)

  if vim.fn.screencol() + content_width > vim.opt.columns:get() then
    orig_col = 0
    line_content = vim.fn.getline(".")
    content_width = vim.str_utfindex(line_content)
  end

  if
    content_width <= 0
    or content_width
      < vim.fn.winwidth(0) - vim.fn.getwininfo(vim.api.nvim_get_current_win())[1].textoff - orig_col - 1
  then
    return
  end

  if content_width <= 0 then
    return
  end

  local extmarks = api.nvim_buf_get_extmarks(
    buffer,
    namespace,
    { orig_line, 0 },
    { orig_line, -1 },
    { details = true }
  )

  local win_opts = {
    relative = "cursor",
    width = content_width,
    height = 1,
    style = "minimal",
    border = "none",
    row = 0,
    col = 0,
  }

  local window_id = buf_wins[buffer]
  local hover_buf
  if window_id and not api.nvim_win_is_valid(window_id) then
    buf_wins[buffer] = nil
    window_id = nil
  end
  -- Use existing window to prevent flickering
  if window_id then
    window_id = buf_wins[buffer]
    hover_buf = api.nvim_win_get_buf(window_id)
    api.nvim_win_set_config(window_id, win_opts)
    api.nvim_buf_set_lines(hover_buf, 0, -1, false, { line_content })
  else
    hover_buf = create_buffer(line_content)
    win_opts.noautocmd = true
    window_id = api.nvim_open_win(hover_buf, false, win_opts)
    buf_wins[buffer] = window_id

    api.nvim_win_call(window_id, function()
      vim.opt.winhighlight:append({ NormalFloat = "Normal" })
    end)
  end

  for _, mark in ipairs(extmarks) do
    local _, _, col, details = unpack(mark)
    if not details.end_col or details.end_col > orig_col then
      details.end_row = 0
      details.ns_id = nil
      details.end_col = details.end_col and (details.end_col - orig_col)
      col = math.max(col, orig_col)
      local ok, error =
        pcall(api.nvim_buf_set_extmark, hover_buf, namespace, 0, col - orig_col, details)
      if not ok then
        require("dapui.util").notify(error, vim.log.levels.DEBUG)
      end
    end
  end

  auto_close(
    window_id,
    buffer,
    orig_line,
    api.nvim_buf_get_lines(buffer, orig_line - 1, orig_line, false)[1]
  )
end

return M
```

## File: `lua/dapui/tests/init.lua`
```
local M = {}

M.mocks = require("dapui.tests.mocks")

M.namespace = require("dapui.render.canvas").namespace

M.bootstrap = function()
  assert:add_formatter(vim.inspect)

  A = function(...)
    local obj = select("#", ...) == 1 and select(1, ...) or { ... }
    local s = type(obj) == "string" and obj or vim.inspect(obj)
    if vim.in_fast_event() then
      vim.schedule(function()
        print(s)
      end)
    else
      print(s)
    end
  end
end

M.util = require("dapui.tests.util")

return M
```

## File: `lua/dapui/tests/mocks.lua`
```
local dap = require("dap")
local Client = require("dapui.client")

local M = {}

---@class dapui.tests.mocks.ScopesArgs
---@field scopes table<integer, dapui.types.Scope[]>

---@param args dapui.tests.mocks.ScopesArgs
function M.scopes(args)
  ---@param request_args dapui.types.ScopesArguments
  ---@return dapui.types.ScopesResponse
  return function(request_args)
    local scopes = args.scopes[request_args.frameId]
    assert(scopes, "No scopes found for frameId " .. request_args.frameId)
    return {
      scopes = scopes,
    }
  end
end

---@class dapui.tests.mocks.EvaluateArgs
---@field expressions table<string, string|dapui.types.EvaluateResponse>
function M.evaluate(args)
  ---@param request_args dapui.types.EvaluateArguments
  ---@return dapui.types.EvaluateResponse
  return function(request_args)
    local result = args.expressions[request_args.expression]
    assert(result, "No expression found for " .. request_args.expression)
    if type(result) == "string" then
      return {
        result = result,
        variablesReference = 0,
      }
    end
    result.variablesReference = result.variablesReference or 0
    return result
  end
end

---@class dapui.tests.mocks.VariablesArgs
---@field variables table<integer, dapui.types.Variable[]>

---@param args dapui.tests.mocks.VariablesArgs
function M.variables(args)
  ---@param request_args dapui.types.VariablesArguments
  ---@return dapui.types.VariablesResponse
  return function(request_args)
    local variables = args.variables[request_args.variablesReference]
    assert(variables, "No variables for variablesReference: " .. request_args.variablesReference)
    return {
      variables = variables,
    }
  end
end

---@class dapui.tests.mocks.ThreadsArgs
---@field threads dapui.types.Thread[]

---@param args dapui.tests.mocks.ThreadsArgs
function M.threads(args)
  ---@return dapui.types.ThreadsResponse
  return function()
    return {
      threads = args.threads,
    }
  end
end

---@class dapui.tests.mocks.StackTracesArgs
---@field stack_traces table<integer, dapui.types.StackFrame[]>

---@param args dapui.tests.mocks.StackTracesArgs
function M.stack_traces(args)
  ---@param request_args dapui.types.StackTraceArguments
  ---@return dapui.types.StackTraceResponse
  return function(request_args)
    local stack_frames = args.stack_traces[request_args.threadId]
    assert(stack_frames, "No stack frames for threadId: " .. request_args.threadId)
    return {
      stackFrames = stack_frames,
    }
  end
end

---@class dapui.tests.mocks.ClientArgs
---@field requests dapui.DAPRequestsClient
---@field current_frame? dapui.types.StackFrame
---@field stopped_thread_id? integer

---@param args? dapui.tests.mocks.ClientArgs
---@return dapui.DAPClient
function M.client(args)
  args = args or { requests = {} }
  local session
  session = {
    seq = 0,
    stopped_thread_id = args.stopped_thread_id,
    current_frame = args.current_frame,
    set_breakpoints = function() end,

    request = function(_, command, request_args, callback)
      session.seq = session.seq + 1
      if not args.requests[command] then
        error("No request handler for " .. command)
      end
      local response = args.requests[command](request_args)
      for _, c in pairs(dap.listeners.before[command]) do
        c(session, nil, response, request_args)
      end
      callback(nil, response, session.seq)
      for _, c in pairs(dap.listeners.after[command]) do
        c(session, nil, response, request_args)
      end
    end,
  }

  ---@type table<integer, dapui.types.DAPBreakpoint[]>
  local breakpoints = {}

  return Client(function()
    return session
  end, {
    get = function(bufnr)
      if bufnr then
        return breakpoints[bufnr]
      end
      return breakpoints
    end,
    ---@param bp_args dapui.client.BreakpointArgs
    toggle = function(bp_args, bufnr, line)
      local buf_bps = breakpoints[bufnr] or {}
      for i, bp in ipairs(buf_bps) do
        if bp.line == line then
          table.remove(buf_bps, i)
          return
        end
      end

      ---@type dapui.types.DAPBreakpoint
      buf_bps[#buf_bps + 1] = {
        condition = bp_args.condition,
        hitCondition = bp_args.hit_condition,
        line = line,
        logMessage = bp_args.log_message,
      }
      breakpoints[bufnr] = buf_bps
    end,
  })
end

return M
```

## File: `lua/dapui/tests/util.lua`
```
local nio = require("nio")
local namespace = require("dapui.render.canvas").namespace

local M = {}

function M.get_highlights(bufnr)
  local formatted = {}
  local extmarks = nio.api.nvim_buf_get_extmarks(bufnr, namespace, 0, -1, { details = true })
  for _, extmark in ipairs(extmarks) do
    local _, start_row, start_col, details = unpack(extmark)
    table.insert(formatted, {
      details.hl_group,
      start_row,
      start_col,
      details.end_row,
      details.end_col,
    })
  end
  return formatted
end

---@class dapui.tests.util.Mapping
---@field buffer integer
---@field callback? function
---@field expr integer
---@field lhs string
---@field lhsraw string
---@field lnum integer
---@field mode string
---@field noremap integer
---@field nowait integer
---@field script integer
---@field sid integer
---@field silent integer

---@param buf integer
---@return table<string, function> Per-key mappings in the buffer
function M.get_mappings(buf)
  ---@type dapui.tests.util.Mapping[]
  local raw_mappings = vim.api.nvim_buf_get_keymap(buf, "n")
  local mappings = {}
  for _, mapping in ipairs(raw_mappings) do
    mappings[mapping.lhs] = mapping.callback
  end
  return mappings
end

return M
```

## File: `lua/dapui/windows/float.lua`
```
local M = {}
local api = vim.api
local config = require("dapui.config")

local Float = { win_id = nil, listeners = { close = {} }, position = {} }

local function create_opts(content_width, content_height, position, title)
  local line_no = position.line
  local col_no = position.col

  local vert_anchor = "N"
  local hor_anchor = "W"

  local max_height = config.floating.max_height or vim.o.lines
  local max_width = config.floating.max_width or vim.o.columns
  local border = config.floating.border
  if 0 < max_height and max_height < 1 then
    max_height = math.floor(vim.o.lines * max_height)
  end
  if 0 < max_width and max_width < 1 then
    max_width = math.floor(vim.o.columns * max_width)
  end
  local height = math.min(content_height, max_height - 2)
  local width = math.min(content_width, max_width - 2)

  local row = line_no + math.min(0, vim.o.lines - (height + line_no + 3))
  local col = col_no + math.min(0, vim.o.columns - (width + col_no + 3))

  return {
    relative = "editor",
    row = row,
    col = col,
    anchor = vert_anchor .. hor_anchor,
    width = width,
    height = height,
    style = "minimal",
    border = border,
    title = title,
    title_pos = title and "center",
  }
end

function Float:new(win_id, position)
  local win = {}
  setmetatable(win, self)
  self.__index = self
  win.win_id = win_id
  win.position = position
  return win
end

function Float:listen(event, callback)
  self.listeners[event][#self.listeners[event] + 1] = callback
end

function Float:resize(width, height, position)
  if position == nil then
    position = self.position
  end
  local opts = create_opts(width, height, position)
  api.nvim_win_set_config(self.win_id, opts)
end

function Float:get_buf()
  local pass, win = pcall(api.nvim_win_get_buf, self.win_id)
  if not pass then
    return -1
  end
  return win
end

function Float:jump_to()
  if vim.fn.mode(true) ~= "n" then
    vim.cmd([[call feedkeys("\<C-\>\<C-N>", "n")]])
  end
  api.nvim_set_current_win(self.win_id)
end

function Float:close(force)
  if not force and api.nvim_get_current_win() == self.win_id then
    return false
  end
  local buf = self:get_buf()
  pcall(api.nvim_win_close, self.win_id, true)
  for _, listener in pairs(self.listeners.close) do
    listener({ buffer = buf })
  end
  return true
end

-- settings:
--   Required:
--     height
--     width
--   Optional:
--     buffer
--     position
--     title
function M.open_float(settings)
  local line_no = vim.fn.screenrow()
  local col_no = vim.fn.screencol()
  local position = settings.position or { line = line_no, col = col_no }
  local opts = create_opts(settings.width, settings.height, position, settings.title)
  local content_buffer = settings.buffer or api.nvim_create_buf(false, true)
  local content_window = api.nvim_open_win(content_buffer, false, opts)

  local output_win_id = api.nvim_win_get_number(content_window)
  vim.fn.setwinvar(output_win_id, "&winhl", "Normal:DapUIFloatNormal,FloatBorder:DapUIFloatBorder")
  vim.api.nvim_win_set_option(content_window, "wrap", false)

  return Float:new(content_window, position)
end

return M
```

## File: `lua/dapui/windows/init.lua`
```
local M = {}

local nio = require("nio")
local api = vim.api
local util = require("dapui.util")
local config = require("dapui.config")
local WindowLayout = require("dapui.windows.layout")

local float_windows = {}

---@type dapui.WindowLayout[]
M.layouts = {}

local registered_elements = {}

local function horizontal_layout(height, position, win_configs, buffers)
  local open_cmd = position == "top" and "topleft" or "botright"

  local function open_tray_win(index)
    vim.cmd(index == 1 and open_cmd .. " " .. " split" or "vsplit")
    return buffers[index]
  end

  local win_states = {}
  for _, conf in ipairs(win_configs) do
    win_states[#win_states + 1] = vim.tbl_extend("force", conf, { init_size = conf.size })
  end

  return WindowLayout({
    layout_type = "horizontal",
    area_state = { size = height, init_size = height },
    win_states = win_states,
    get_win_size = api.nvim_win_get_width,
    get_area_size = api.nvim_win_get_height,
    set_win_size = api.nvim_win_set_width,
    set_area_size = api.nvim_win_set_height,
    open_index = open_tray_win,
  })
end

local function vertical_layout(width, position, win_configs, buffers)
  local open_cmd = position == "left" and "topleft" or "botright"
  local function open_side_win(index)
    vim.cmd(index == 1 and open_cmd .. " " .. "vsplit" or "split")
    return buffers[index]
  end

  local win_states = {}
  for _, conf in ipairs(win_configs) do
    win_states[#win_states + 1] = vim.tbl_extend("force", conf, { init_size = conf.size })
  end

  return WindowLayout({
    layout_type = "vertical",
    area_state = { size = width, init_size = width },
    win_states = win_states,
    get_win_size = api.nvim_win_get_height,
    get_area_size = api.nvim_win_get_width,
    set_area_size = api.nvim_win_set_width,
    set_win_size = api.nvim_win_set_height,
    open_index = open_side_win,
  })
end

function M.area_layout(size, position, win_configs, buffers)
  local win_states = vim.deepcopy(win_configs)
  local layout_func
  if position == "top" or position == "bottom" then
    layout_func = horizontal_layout
  else
    layout_func = vertical_layout
  end
  return layout_func(size, position, win_states, buffers)
end

local function force_buffers(keep_current)
  for _, layout in ipairs(M.layouts) do
    layout:force_buffers(keep_current)
  end
end

---@param element_buffers table<string, integer>
function M.setup(element_buffers)
  local dummy_buf = util.create_buffer("", {})
  for _, layout in ipairs(M.layouts) do
    layout:close()
  end
  local layout_configs = config.layouts
  M.layouts = {}
  for i, layout in ipairs(layout_configs) do
    local buffers = {}
    for index, win_config in ipairs(layout.elements) do
      buffers[index] = element_buffers[win_config.id]
        or function()
          local elem = registered_elements[win_config.id]
          if not elem then
            return dummy_buf()
          end
          return elem.buffer()
        end
    end
    M.layouts[i] = M.area_layout(layout.size, layout.position, layout.elements, buffers)
  end
  if config.force_buffers then
    local group = api.nvim_create_augroup("DapuiWindowsSetup", {})
    api.nvim_create_autocmd({ "BufWinEnter", "BufWinLeave" }, {
      callback = function()
        force_buffers(false)
      end,
      group = group,
    })
  end
end

function M.register_element(name, elem)
  registered_elements[name] = elem
  force_buffers(false)
end

---@param element dapui.Element
function M.open_float(name, element, position, settings)
  if float_windows[name] then
    float_windows[name]:jump_to()
    return float_windows[name]
  end
  local buf = element.buffer()
  if type(settings) == "function" then
    settings = settings()
  end
  local float_win = require("dapui.windows.float").open_float({
    height = settings.height or 1,
    width = settings.width or 1,
    position = position,
    buffer = buf,
    title = settings.title,
  })

  local resize = function()
    local width = settings.width
    local height = settings.height

    if not width or not height then
      local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
      if not width then
        width = 0
        for _, line in ipairs(lines) do
          width = math.max(width, vim.str_utfindex(line))
        end
      end

      if not height then
        height = #lines
      end
    end

    if settings.position == "center" then
      local screen_w = vim.opt.columns:get()
      local screen_h = vim.opt.lines:get() - vim.opt.cmdheight:get()
      position.line = (screen_h - height) / 2
      position.col = (screen_w - width) / 2
    end

    if width <= 0 or height <= 0 then
      return
    end
    float_win:resize(width, height, position)
  end

  nio.api.nvim_buf_attach(buf, true, {
    on_lines = function()
      if not vim.api.nvim_win_is_valid(float_win.win_id) then
        return true
      end
      resize()
    end,
  })
  -- In case render doesn't trigger on_lines
  resize()

  util.apply_mapping(config.floating.mappings["close"], "<Cmd>q<CR>", buf)
  local close_cmd = "lua require('dapui.windows').close_float('" .. name .. "')"
  vim.cmd("au WinEnter,CursorMoved * ++once " .. close_cmd)
  vim.cmd("au WinClosed " .. float_win.win_id .. " ++once " .. close_cmd)
  float_windows[name] = float_win
  if settings.enter then
    float_win:jump_to()
  end
  return float_win
end

function M.close_float(element_name)
  if float_windows[element_name] == nil then
    return
  end
  local win = float_windows[element_name]
  local closed = win:close(false)
  if not closed then
    local close_cmd = "lua require('dapui.windows').close_float('" .. element_name .. "')"
    vim.cmd("au WinEnter * ++once " .. close_cmd)
    vim.cmd("au WinClosed " .. win.win_id .. " ++once " .. close_cmd)
  else
    float_windows[element_name] = nil
  end
end

return M
```

## File: `lua/dapui/windows/layout.lua`
```
local api = vim.api
local util = require("dapui.util")

---@class dapui.WinState
---@field id string
---@field size number
---@field init_size number

---@class dapui.AreaState
---@field init_size number
---@field size number

---@class dapui.WindowLayout
---@field opened_wins integer[]
---@field win_bufs table<integer, fun(): integer>
---@field win_states table<integer,dapui.WinState>
---@field area_state dapui.AreaState
---@field layout_type "horizontal" | "vertical"
--
---@field open_index fun(index: number): fun(): integer
---@field get_win_size fun(win_id: integer): integer
---@field get_area_size fun(win_id: integer): integer
---@field set_win_size fun(win_id: integer, size: integer)
---@field set_area_size fun(win_id: integer, size: integer)
local WindowLayout = {}

function WindowLayout:open()
  if self:is_open() then
    return
  end
  local cur_win = api.nvim_get_current_win()
  for i, _ in pairs(self.win_states) do
    local get_buffer = self.open_index(i)
    local win_id = api.nvim_get_current_win()
    api.nvim_set_current_buf(get_buffer())
    self.opened_wins[i] = win_id
    self:_init_win_settings(win_id)
    self.win_bufs[win_id] = get_buffer
  end
  self:resize()
  -- Fails if cur win was floating that closed
  pcall(api.nvim_set_current_win, cur_win)
end

function WindowLayout:force_buffers(keep_current)
  local curwin = api.nvim_get_current_win()
  for win, get_buffer in pairs(self.win_bufs) do
    local bufnr = get_buffer()
    local valid, curbuf = pcall(api.nvim_win_get_buf, win)
    if valid and curbuf ~= bufnr then
      if api.nvim_buf_is_loaded(bufnr) and api.nvim_buf_is_valid(bufnr) then
        -- pcall necessary to avoid erroring with `mark not set` although no mark are set
        -- this avoid other issues
        pcall(api.nvim_win_set_buf, win, bufnr)
      end
      if keep_current and curwin == win then
        util.open_buf(curbuf)
      end
    end
  end
end

function WindowLayout:_total_size()
  local total_size = 0
  for _, open_win in ipairs(self.opened_wins) do
    local success, win_size = pcall(self.get_win_size, open_win)
    total_size = total_size + (success and win_size or 0)
  end
  return total_size
end

function WindowLayout:_area_size()
  for _, win in ipairs(self.opened_wins) do
    local success, area_size = pcall(self.get_area_size, win)
    if success then
      return area_size
    end
  end
  return 0
end

function WindowLayout:resize(opts)
  opts = opts or {}
  if opts.reset then
    self.area_state.size = self.area_state.init_size
  end
  if not self:is_open() then
    return
  end

  -- Detecting whether self.area_state.size is a float or int
  if self.area_state.size < 1 then
    if self.layout_type == "vertical" then
      local left = 1
      local right = vim.opt.columns:get()
      self.area_state.size = math.floor((right - left) * self.area_state.size)
    elseif self.layout_type == "horizontal" then
      local top = vim.opt.tabline:get() == "" and 0 or 1
      local bottom = vim.opt.lines:get() - (vim.opt.laststatus:get() > 0 and 2 or 1)
      self.area_state.size = math.floor((bottom - top) * self.area_state.size)
    else
      error("Unknown layout type")
    end
  end

  self.set_area_size(self.opened_wins[1], self.area_state.size)
  local total_size = self:_total_size()
  for i, win_state in pairs(self.win_states) do
    local win_size = opts.reset and win_state.init_size or win_state.size or 1
    win_size = util.round(win_size * total_size)
    if win_size == 0 then
      win_size = 1
    end
    self.set_win_size(self.opened_wins[i], win_size)
  end
end

function WindowLayout:update_sizes()
  if not self:is_open() then
    return
  end
  local area_size = self:_area_size()
  if area_size == 0 then
    return
  end
  self.area_state.size = area_size
  local total_size = self:_total_size()
  for i, win_state in ipairs(self.win_states) do
    local win = self.opened_wins[i]
    local win_exists, _ = pcall(api.nvim_win_get_buf, win)
    if win_exists then
      local success, current_size = pcall(self.get_win_size, self.opened_wins[i])
      if success then
        win_state.size = current_size / total_size
      end
    end
  end
end

function WindowLayout:close()
  local current_win = api.nvim_get_current_win()
  for _, win in pairs(self.opened_wins) do
    local win_exists = api.nvim_win_is_valid(win)

    if win_exists then
      if win == current_win then
        vim.cmd("stopinsert") -- Prompt buffers act poorly when closed in insert mode, see #33
      end
      pcall(api.nvim_win_close, win, true)
    end
  end
  self.opened_wins = {}
end

---@return boolean
function WindowLayout:is_open()
  for _, win in ipairs(self.opened_wins) do
    if pcall(vim.api.nvim_win_get_number, win) then
      return true
    end
  end
  return false
end

function WindowLayout:toggle()
  if self:is_open() then
    self:close()
  else
    self:open()
  end
end

function WindowLayout:_init_win_settings(win)
  local config = require("dapui.config")
  local win_settings = {
    list = false,
    relativenumber = false,
    number = false,
    winfixwidth = true,
    winfixheight = true,
    wrap = config.wrap,
    signcolumn = "auto",
    spell = false,
  }
  for key, val in pairs(win_settings) do
    api.nvim_win_set_option(win, key, val)
  end
  api.nvim_win_call(win, function()
    vim.opt.winhighlight:append({ Normal = "DapUINormal", EndOfBuffer = "DapUIEndOfBuffer" })
  end)
end

function WindowLayout:new(layout)
  layout.opened_wins = {}
  layout.win_bufs = {}
  setmetatable(layout, self)
  self.__index = self
  return layout
end

---@return dapui.WindowLayout
return function(layout)
  return WindowLayout:new(layout)
end
```

## File: `scripts/docgen`
```
#!/bin/bash

nvim --headless -c "luafile ./scripts/gendocs.lua" -c 'qa'
```

## File: `scripts/gendocs.lua`
```
-- TODO: A lot of this is private code from minidoc, which could be removed if made public

local util = require("dapui.util")
local minidoc = require("mini.doc")

local H = {}
--stylua: ignore start
H.pattern_sets = {
  -- Patterns for working with afterlines. At the moment deliberately crafted
  -- to work only on first line without indent.

  -- Determine if line is a function definition. Captures function name and
  -- arguments. For reference see '2.5.9 – Function Definitions' in Lua manual.
  afterline_fundef = {
    "%s*function%s+(%S-)(%b())",           -- Regular definition
    "^local%s+function%s+(%S-)(%b())",     -- Local definition
    "^(%S+)%s*=%s*function(%b())",         -- Regular assignment
    "^local%s+(%S+)%s*=%s*function(%b())", -- Local assignment
  },

  -- Determine if line is a general assignment
  afterline_assign = {
    "^(%S-)%s*=",         -- General assignment
    "^local%s+(%S-)%s*=", -- Local assignment
  },

  -- Patterns to work with type descriptions
  -- (see https://github.com/sumneko/lua-language-server/wiki/EmmyLua-Annotations#types-and-type)
  types = {
    "table%b<>",
    "fun%b(): %S+", "fun%b()", "async fun%b(): %S+", "async fun%b()",
    "nil", "any", "boolean", "string", "number", "integer", "function", "table", "thread", "userdata", "lightuserdata",
    "%.%.%.",
    "%S+",

  },
}


H.apply_config = function(config)
  MiniDoc.config = config
end

H.is_disabled = function()
  return vim.g.minidoc_disable == true or vim.b.minidoc_disable == true
end

H.get_config = function(config)
  return vim.tbl_deep_extend("force", MiniDoc.config, vim.b.minidoc_config or {}, config or {})
end

-- Work with project specific script ==========================================
H.execute_project_script = function(input, output, config)
  -- Don't process script if there are more than one active `generate` calls
  if H.generate_is_active then
    return
  end

  -- Don't process script if at least one argument is not default
  if not (input == nil and output == nil and config == nil) then
    return
  end

  -- Store information
  local global_config_cache = vim.deepcopy(MiniDoc.config)
  local local_config_cache = vim.b.minidoc_config

  -- Pass information to a possible `generate()` call inside script
  H.generate_is_active = true
  H.generate_recent_output = nil

  -- Execute script
  local success = pcall(vim.cmd, "luafile " .. H.get_config(config).script_path)

  -- Restore information
  MiniDoc.config = global_config_cache
  vim.b.minidoc_config = local_config_cache
  H.generate_is_active = nil

  return success
end

-- Default documentation targets ----------------------------------------------
H.default_input = function()
  -- Search in current and recursively in other directories for files with
  -- 'lua' extension
  local res = {}
  for _, dir_glob in ipairs({ ".", "lua/**", "after/**", "colors/**" }) do
    local files = vim.fn.globpath(dir_glob, "*.lua", false, true)

    -- Use full paths
    files = vim.tbl_map(function(x)
      return vim.fn.fnamemodify(x, ":p")
    end, files)

    -- Put 'init.lua' first among files from same directory
    table.sort(files, function(a, b)
      if vim.fn.fnamemodify(a, ":h") == vim.fn.fnamemodify(b, ":h") then
        if vim.fn.fnamemodify(a, ":t") == "init.lua" then
          return true
        end
        if vim.fn.fnamemodify(b, ":t") == "init.lua" then
          return false
        end
      end

      return a < b
    end)
    table.insert(res, files)
  end

  return util.tbl_flatten(res)
end

H.default_output = function()
  local cur_dir = vim.fn.fnamemodify(vim.loop.cwd(), ":t:r")
  return ("doc/%s.txt"):format(cur_dir)
end

-- Parsing --------------------------------------------------------------------
H.lines_to_block_arr = function(lines, config)
  local matched_prev, matched_cur

  local res = {}
  local block_raw = { annotation = {}, section_id = {}, afterlines = {}, line_begin = 1 }

  for i, l in ipairs(lines) do
    local from, to, section_id = config.annotation_extractor(l)
    matched_prev, matched_cur = matched_cur, from ~= nil

    if matched_cur then
      if not matched_prev then
        -- Finish current block
        block_raw.line_end = i - 1
        table.insert(res, H.raw_block_to_block(block_raw, config))

        -- Start new block
        block_raw = { annotation = {}, section_id = {}, afterlines = {}, line_begin = i }
      end

      -- Add annotation line without matched annotation pattern
      table.insert(block_raw.annotation, ("%s%s"):format(l:sub(0, from - 1), l:sub(to + 1)))

      -- Add section id (it is empty string in case of no section id capture)
      table.insert(block_raw.section_id, section_id or "")
    else
      -- Add afterline
      table.insert(block_raw.afterlines, l)
    end
  end
  block_raw.line_end = #lines
  table.insert(res, H.raw_block_to_block(block_raw, config))

  return res
end

-- Raw block structure is an intermediate step added for convenience. It is
-- a table with the following keys:
-- - `annotation` - lines (after removing matched annotation pattern) that were
--   parsed as annotation.
-- - `section_id` - array with length equal to `annotation` length with strings
--   captured as section id. Empty string of no section id was captured.
-- - Everything else is used as block info (like `afterlines`, etc.).
H.raw_block_to_block = function(block_raw, config)
  if #block_raw.annotation == 0 and #block_raw.afterlines == 0 then
    return nil
  end

  local block = H.new_struct("block", {
    afterlines = block_raw.afterlines,
    line_begin = block_raw.line_begin,
    line_end = block_raw.line_end,
  })
  local block_begin = block.info.line_begin

  -- Parse raw block annotation lines from top to bottom. New section starts
  -- when section id is detected in that line.
  local section_cur = H.new_struct(
    "section",
    { id = config.default_section_id, line_begin = block_begin }
  )

  for i, annotation_line in ipairs(block_raw.annotation) do
    local id = block_raw.section_id[i]
    if id ~= "" then
      -- Finish current section
      if #section_cur > 0 then
        section_cur.info.line_end = block_begin + i - 2
        block:insert(section_cur)
      end

      -- Start new section
      section_cur = H.new_struct("section", { id = id, line_begin = block_begin + i - 1 })
    end

    section_cur:insert(annotation_line)
  end

  if #section_cur > 0 then
    section_cur.info.line_end = block_begin + #block_raw.annotation - 1
    block:insert(section_cur)
  end

  return block
end

-- Hooks ----------------------------------------------------------------------
H.apply_structure_hooks = function(doc, hooks)
  for _, file in ipairs(doc) do
    for _, block in ipairs(file) do
      hooks.block_pre(block)

      for _, section in ipairs(block) do
        hooks.section_pre(section)

        local hook = hooks.sections[section.info.id]
        if hook ~= nil then
          hook(section)
        end

        hooks.section_post(section)
      end

      hooks.block_post(block)
    end

    hooks.file(file)
  end

  hooks.doc(doc)
end

H.alias_register = function(s)
  if #s == 0 then
    return
  end

  -- Remove first word (with bits of surrounding whitespace) while capturing it
  local alias_name
  s[1] = s[1]:gsub("%s*(%S+) ?", function(x)
    alias_name = x
    return ""
  end, 1)
  if alias_name == nil then
    return
  end

  MiniDoc.current.aliases = MiniDoc.current.aliases or {}
  MiniDoc.current.aliases[alias_name] = table.concat(s, "\n")
end

H.alias_replace = function(s)
  if MiniDoc.current.aliases == nil then
    return
  end

  for i, _ in ipairs(s) do
    for alias_name, alias_desc in pairs(MiniDoc.current.aliases) do
      -- Escape special characters. This is done here and not while registering
      -- alias to allow user to refer to aliases by its original name.
      -- Store escaped words in separate variables because `vim.pesc()` returns
      -- two values which might conflict if outputs are used as arguments.
      local name_escaped = vim.pesc(alias_name)
      local desc_escaped = vim.pesc(alias_desc)
      s[i] = s[i]:gsub(name_escaped, desc_escaped)
    end
  end
end

H.toc_register = function(s)
  MiniDoc.current.toc = MiniDoc.current.toc or {}
  table.insert(MiniDoc.current.toc, s)
end

H.toc_insert = function(s)
  if MiniDoc.current.toc == nil then
    return
  end

  -- Render table of contents
  local toc_lines = {}
  for _, toc_entry in ipairs(MiniDoc.current.toc) do
    local _, tag_section = toc_entry.parent:has_descendant(function(x)
      return type(x) == "table" and x.type == "section" and x.info.id == "@tag"
    end)
    tag_section = tag_section or {}

    local lines = {}
    for i = 1, math.max(#toc_entry, #tag_section) do
      local left = toc_entry[i] or ""
      -- Use tag refernce instead of tag enclosure
      local right = string.match(tag_section[i], "%*.*%*"):gsub("%*", "|")
      -- local right = vim.trim((tag_section[i] or ""):gsub("%*", "|"))
      -- Add visual line only at first entry (while not adding trailing space)
      local filler = i == 1 and "." or (right == "" and "" or " ")
      -- Make padding of 2 spaces at both left and right
      local n_filler = math.max(74 - H.visual_text_width(left) - H.visual_text_width(right), 3)
      table.insert(lines, ("  %s%s%s"):format(left, filler:rep(n_filler), right))
    end

    table.insert(toc_lines, lines)

    -- Don't show `toc_entry` lines in output
    toc_entry:clear_lines()
  end

  for _, l in ipairs(util.tbl_flatten(toc_lines)) do
    s:insert(l)
  end
end

H.add_section_heading = function(s, heading)
  if #s == 0 or s.type ~= "section" then
    return
  end

  -- Add heading
  s:insert(1, ("%s~"):format(heading))
end

H.enclose_var_name = function(s)
  if #s == 0 or s.type ~= "section" then
    return
  end

  s[1] = s[1]:gsub("(%S+)", "{%1}", 1)
end

---@param init number Start of searching for first "type-like" string. It is
---   needed to not detect type early. Like in `@param a_function function`.
---@private
H.enclose_type = function(s, enclosure, init)
  if #s == 0 or s.type ~= "section" then
    return
  end
  enclosure = enclosure or "`%(%1%)`"
  init = init or 1

  local cur_type = H.match_first_pattern(s[1], H.pattern_sets["types"], init)
  if #cur_type == 0 then
    return
  end

  -- Add `%S*` to front and back of found pattern to support their combination
  -- with `|`. Also allows using `[]` and `?` prefixes.
  local type_pattern = ("(%%S*%s%%S*)"):format(vim.pesc(cur_type[1]))

  -- Avoid replacing possible match before `init`
  local l_start = s[1]:sub(1, init - 1)
  local l_end = s[1]:sub(init):gsub(type_pattern, enclosure, 1)
  s[1] = ("%s%s"):format(l_start, l_end)
end

-- Infer data from afterlines -------------------------------------------------
H.infer_header = function(b)
  local has_signature = b:has_descendant(function(x)
    return type(x) == "table" and x.type == "section" and x.info.id == "@signature"
  end)
  local has_tag = b:has_descendant(function(x)
    return type(x) == "table" and x.type == "section" and x.info.id == "@tag"
  end)

  if has_signature and has_tag then
    return
  end

  local l_all = table.concat(b.info.afterlines, " ")
  local tag, signature

  -- Try function definition
  local fun_capture = H.match_first_pattern(l_all, H.pattern_sets["afterline_fundef"])
  if #fun_capture > 0 then
    tag = tag or ("%s()"):format(fun_capture[1])
    signature = signature or ("%s%s"):format(fun_capture[1], fun_capture[2])
  end

  -- Try general assignment
  local assign_capture = H.match_first_pattern(l_all, H.pattern_sets["afterline_assign"])
  if #assign_capture > 0 then
    tag = tag or assign_capture[1]
    signature = signature or assign_capture[1]
  end

  if tag ~= nil then
    -- First insert signature (so that it will appear after tag section)
    if not has_signature then
      b:insert(1, H.as_struct({ signature }, "section", { id = "@signature" }))
    end

    -- Insert tag
    if not has_tag then
      b:insert(1, H.as_struct({ tag }, "section", { id = "@tag" }))
    end
  end
end

function H.is_module(name)
  if string.find(name, "%(") then
    return false
  end
  if string.find(name, "[A-Z]") then
    return false
  end
  return true
end

H.format_signature = function(line)
  -- Try capture function signature
  local name, args = line:match("(%S-)(%b())")


  -- Otherwise pick first word
  name = name or line:match("(%S+)")
  if not args and H.is_module(name) then
    return ""
  end
  local name_elems = vim.split(name, ".", { plain = true })
  name = name_elems[#name_elems]

  if not name then
    return ""
  end

  -- Tidy arguments
  if args and args ~= "()" then
    local arg_parts = vim.split(args:sub(2, -2), ",")
    local arg_list = {}
    for _, a in ipairs(arg_parts) do
      -- Enclose argument in `{}` while controlling whitespace
      table.insert(arg_list, ("{%s}"):format(vim.trim(a)))
    end
    args = ("(%s)"):format(table.concat(arg_list, ", "))
  end

  return ("`%s`%s"):format(name, args or "")
end

-- Work with structures -------------------------------------------------------
-- Constructor
H.new_struct = function(struct_type, info)
  local output = {
    info = info or {},
    type = struct_type,
  }

  output.insert = function(self, index, child)
    -- Allow both `x:insert(child)` and `x:insert(1, child)`
    if child == nil then
      child, index = index, #self + 1
    end

    if type(child) == "table" then
      child.parent = self
      child.parent_index = index
    end

    table.insert(self, index, child)

    H.sync_parent_index(self)
  end

  output.remove = function(self, index)
    index = index or #self
    table.remove(self, index)

    H.sync_parent_index(self)
  end

  output.has_descendant = function(self, predicate)
    local bool_res, descendant = false, nil
    H.apply_recursively(function(x)
      if not bool_res and predicate(x) then
        bool_res = true
        descendant = x
      end
    end, self)
    return bool_res, descendant
  end

  output.has_lines = function(self)
    return self:has_descendant(function(x)
      return type(x) == "string"
    end)
  end

  output.clear_lines = function(self)
    for i, x in ipairs(self) do
      if type(x) == "string" then
        self[i] = nil
      else
        x:clear_lines()
      end
    end
  end

  return output
end

H.sync_parent_index = function(x)
  for i, _ in ipairs(x) do
    if type(x[i]) == "table" then
      x[i].parent_index = i
    end
  end
  return x
end

-- Converter (this ensures that children have proper parent-related data)
H.as_struct = function(array, struct_type, info)
  -- Make default info `info` for cases when structure is created manually
  local default_info = ({
    section = { id = "@text", line_begin = -1, line_end = -1 },
    block = { afterlines = {}, line_begin = -1, line_end = -1 },
    file = { path = "" },
    doc = { input = {}, output = "", config = H.get_config() },
  })[struct_type]
  info = vim.tbl_deep_extend("force", default_info, info or {})

  local res = H.new_struct(struct_type, info)
  for _, x in ipairs(array) do
    res:insert(x)
  end
  return res
end

-- Work with text -------------------------------------------------------------
H.ensure_indent = function(text, n_indent_target)
  local lines = vim.split(text, "\n")
  local n_indent, n_indent_cur = math.huge, math.huge

  -- Find number of characters in indent
  for _, l in ipairs(lines) do
    -- Update lines indent: minimum of all indents except empty lines
    if n_indent > 0 then
      _, n_indent_cur = l:find("^%s*")
      -- Condition "current n-indent equals line length" detects empty line
      if (n_indent_cur < n_indent) and (n_indent_cur < l:len()) then
        n_indent = n_indent_cur
      end
    end
  end

  -- Ensure indent
  local indent = string.rep(" ", n_indent_target)
  for i, l in ipairs(lines) do
    if l ~= "" then
      lines[i] = indent .. l:sub(n_indent + 1)
    end
  end

  return table.concat(lines, "\n")
end

H.align_text = function(text, width, direction)
  if type(text) ~= "string" then
    return
  end
  text = vim.trim(text)
  width = width or 78
  direction = direction or "left"

  -- Don't do anything if aligning left or line is a whitespace
  if direction == "left" or text:find("^%s*$") then
    return text
  end

  local n_left = math.max(0, 78 - H.visual_text_width(text))
  if direction == "center" then
    n_left = math.floor(0.5 * n_left)
  end

  return (" "):rep(n_left) .. text
end

H.visual_text_width = function(text)
  -- Ignore concealed characters (usually "invisible" in 'help' filetype)
  local _, n_concealed_chars = text:gsub("([*|`])", "%1")
  return vim.fn.strdisplaywidth(text) - n_concealed_chars
end

--- Return earliest match among many patterns
---
--- Logic here is to test among several patterns. If several got a match,
--- return one with earliest match.
---
---@private
H.match_first_pattern = function(text, pattern_set, init)
  local start_tbl = vim.tbl_map(function(pattern)
    return text:find(pattern, init) or math.huge
  end, pattern_set)

  local min_start, min_id = math.huge, nil
  for id, st in ipairs(start_tbl) do
    if st < min_start then
      min_start, min_id = st, id
    end
  end

  if min_id == nil then
    return {}
  end
  return { text:match(pattern_set[min_id], init) }
end

-- Utilities ------------------------------------------------------------------
H.apply_recursively = function(f, x, used)
  used = used or {}
  if used[x] then
    return
  end
  f(x)
  used[x] = true

  if type(x) == "table" then
    for _, t in ipairs(x) do
      H.apply_recursively(f, t, used)
    end
  end
end

H.collect_strings = function(x)
  local res = {}
  H.apply_recursively(function(y)
    if type(y) == "string" then
      -- Allow `\n` in strings
      table.insert(res, vim.split(y, "\n"))
    end
  end, x)
  -- Flatten to only have strings and not table of strings (from `vim.split`)
  return util.tbl_flatten(res)
end

H.file_read = function(path)
  local file = assert(io.open(path))
  local contents = file:read("*all")
  file:close()

  return vim.split(contents, "\n")
end

H.file_write = function(path, lines)
  -- Ensure target directory exists
  local dir = vim.fn.fnamemodify(path, ":h")
  vim.fn.mkdir(dir, "p")

  -- Write to file
  vim.fn.writefile(lines, path, "b")
end

H.full_path = function(path)
  return vim.fn.resolve(vim.fn.fnamemodify(path, ":p"))
end

H.message = function(msg)
  vim.cmd("echomsg " .. vim.inspect("(mini.doc) " .. msg))
end

minidoc.setup({})
minidoc.generate(
  {
    "./lua/dapui/init.lua",
    "./lua/dapui/config/init.lua",
    "./lua/dapui/elements/scopes.lua",
    "./lua/dapui/elements/stacks.lua",
    "./lua/dapui/elements/repl.lua",
    "./lua/dapui/elements/watches.lua",
    "./lua/dapui/elements/breakpoints.lua",
    "./lua/dapui/elements/console.lua",
  },
  nil,
  {
    annotation_extractor = function(l) return string.find(l, "%s*%-%-%-(%S*) ?") end,

    hooks = vim.tbl_extend("force", minidoc.default_hooks, {
      block_pre = function(b)
        -- Infer metadata based on afterlines
        if b:has_lines() and #b.info.afterlines > 0 then H.infer_header(b) end
      end,

      block_post = function(b)
        if not b:has_lines() then return end

        local found_param, found_field = false, false
        local n_tag_sections = 0
        H.apply_recursively(function(x)
          if not (type(x) == "table" and x.type == "section") then return end

          -- Add headings before first occurence of a section which type usually
          -- appear several times
          if not found_param and x.info.id == "@param" then
            H.add_section_heading(x, "Parameters")
            found_param = true
          end
          if not found_field and x.info.id == "@field" then
            H.add_section_heading(x, "Fields")
            found_field = true
          end

          if x.info.id == "@tag" then
            local text = x[1]
            local tag = string.match(text, "%*.*%*")
            local prefix = (string.sub(tag, 2, #tag - 1))
            if not H.is_module(prefix) then
              prefix = ""
            end
            local n_filler = math.max(78 - H.visual_text_width(prefix) - H.visual_text_width(tag), 3)
            local line = ("%s%s%s"):format(prefix, (" "):rep(n_filler), tag)
            x:remove(1)
            x:insert(1, line)
            x.parent:remove(x.parent_index)
            n_tag_sections = n_tag_sections + 1
            x.parent:insert(n_tag_sections, x)
          end
        end, b)

        -- b:insert(1, H.as_struct({ string.rep('=', 78) }, 'section'))
        b:insert(H.as_struct({ "" }, "section"))
      end,


      doc = function(d)
        -- Render table of contents
        H.apply_recursively(function(x)
          if not (type(x) == "table" and x.type == "section" and x.info.id == "@toc") then return end
          H.toc_insert(x)
        end, d)

        -- Insert modeline
        d:insert(
          H.as_struct(
            { H.as_struct({ H.as_struct({ " vim:tw=78:ts=8:noet:ft=help:norl:" }, "section") }, "block") },
            "file"
          )
        )
      end,
      section_post = function(section)
        for i, line in ipairs(section) do
          if type(line) == "string" then
            if string.find(line, "^```") then
              string.gsub(line, "```(.*)", function(lang)
                section[i] = lang == "" and "<" or (">%s"):format(lang)
              end)
            end
          end
        end
      end,
      sections = {
        ["@generic"] = function(s)
          s:remove(1)
        end,
        ["@field"] = function(s)
          -- H.mark_optional(s)
          if string.find(s[1], "^private ") then
            s:remove(1)
            return
          end
          H.enclose_var_name(s)
          H.enclose_type(s, "`%(%1%)`", s[1]:find("%s"))
        end,
        ["@alias"] = function(s)
          local name = s[1]:match("%s*(%S*)")
          local alias = s[1]:match("%s(.*)$")
          s[1] = ("`%s` → `%s`"):format(name, alias)
          H.add_section_heading(s, "Alias")
          s:insert(1, H.as_struct({ ("*%s*"):format(name) }, "section", { id = "@tag" }))
        end,

        ["@param"] = function(s)
          H.enclose_var_name(s)
          H.enclose_type(s, "`%(%1%)`", s[1]:find("%s"))
        end,
        ["@return"] = function(s)
          H.enclose_type(s, "`%(%1%)`", 1)
          H.add_section_heading(s, "Return")
        end,
        ["@nodoc"] = function(s) s.parent:clear_lines() end,
        ["@class"] = function(s)
          H.enclose_var_name(s)
          -- Add heading
          local line = s[1]
          s:remove(1)
          local class_name = string.match(line, "%{(.*)%}")
          local inherits = string.match(line, ": (.*)")
          if inherits then
            s:insert(1, ("Inherits: `%s`"):format(inherits))
            s:insert(2, "")
          end
          s:insert(1, H.as_struct({ ("*%s*"):format(class_name) }, "section", { id = "@tag" }))
        end,

        ["@signature"] = function(s)
          s[1] = H.format_signature(s[1])
          if s[1] ~= "" then
            table.insert(s, "")
          end
        end,

      },

      file = function(f)
        if not f:has_lines() then
          return
        end

        if f.info.path ~= "./lua/dapui/init.lua" then
          f:insert(1, H.as_struct({ H.as_struct({ string.rep("=", 78) }, "section") }, "block"))
          f:insert(H.as_struct({ H.as_struct({ "" }, "section") }, "block"))
        else
          f:insert(
            1,
            H.as_struct(
              {
                H.as_struct(
                  { "nvim-dap-ui.txt*	A UI for nvim-dap." },
                  "section"
                ),
              },
              "block"
            )
          )
          f:insert(2, H.as_struct({ H.as_struct({ "" }, "section") }, "block"))
          f:insert(3, H.as_struct({ H.as_struct({ string.rep("=", 78) }, "section") }, "block"))
          f:insert(H.as_struct({ H.as_struct({ "" }, "section") }, "block"))
        end
      end,
    }),
  }
)
```

## File: `scripts/generate_types`
```
#!/usr/bin/env python3.10

import importlib.machinery
import importlib.util
import inspect as i
import json
import logging
import re
import tempfile as tf
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Union, get_args, get_origin

import datamodel_code_generator as d
import requests
from pydantic import BaseModel, Field, create_model
from pydantic.fields import ModelField

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

# Name conversion patterns
pat1 = re.compile("(.)([A-Z][a-z]+)")
pat2 = re.compile("([a-z0-9])([A-Z])")


def camel_to_snake(name):
    name = pat1.sub(r"\1_\2", name)
    return pat2.sub(r"\1_\2", name).lower()


class FieldSummary(BaseModel):
    type_name: str
    type: type[BaseModel]


class ModelSummary(BaseModel):
    type: type[BaseModel]
    type_name: str
    fields: dict[str, FieldSummary]
    description: str | None


class DAPTypesGenerator:
    def __init__(self) -> None:
        self.known_types = set()
        self.create_module()

    def create_module(self):
        protocol_path = Path("/tmp/dap-protocol.json")
        if not protocol_path.exists():
            logger.info("Downloading protocol")
            protocol_path.write_bytes(
                requests.get(
                    "https://raw.githubusercontent.com/microsoft/debug-adapter-protocol/gh-pages/debugAdapterProtocol.json"
                ).content
            )

        self.schema = json.loads(protocol_path.read_bytes().decode())
        _, output_path = tf.mkstemp()
        output_path = Path(output_path)

        d.generate(
            input_=protocol_path, output=output_path, use_schema_description=True
        )
        with open(output_path) as f:
            data = f.readlines()
        # Remove the update_forward_refs calls which cause errors
        while "update_forward_refs" in data[-1]:
            data.pop()

        with open(output_path, "w") as f:
            f.writelines(data)
        with open("model.py", "w") as f:
            f.writelines(data)

        # Import mymodule
        loader = importlib.machinery.SourceFileLoader("models", str(output_path))
        spec = importlib.util.spec_from_loader("models", loader)
        models_module = importlib.util.module_from_spec(spec)
        loader.exec_module(models_module)
        self.models = models_module

    def is_model(self, t) -> bool:
        return i.isclass(t) and issubclass(t, BaseModel)

    def extract_summary(
        self,
        model_cls: type[BaseModel],
    ) -> ModelSummary:
        fields = {}
        for field_name, field in model_cls.__fields__.items():
            if field and self.is_model(field.outer_type_):
                fields[field_name] = FieldSummary(
                    type=field.type_,
                    type_name=self.type_name(field.type_),
                )
        return ModelSummary(
            type=model_cls,
            type_name=self.type_name(model_cls),
            fields=fields,
            description=self.class_doc(model_cls),
        )

    def type_name(self, t) -> str:
        if self.is_model(t):
            return f"dapui.types.{t.__name__}"
        if t is int:
            return "integer"
        if t is float:
            return "number"
        if t is str:
            return "string"
        if t is bool:
            return "boolean"
        if i.isclass(t) and issubclass(t, Enum):
            return "|".join(f'"{member.value}"' for member in t.__members__.values())
        if get_origin(t) is Union:
            # Account for Optional with ? on field
            return " | ".join(
                self.type_name(a) for a in get_args(t) if a is not type(None)
            )
        if get_origin(t) is list:
            return f"{self.type_name(get_args(t)[0])}[]"
        if t is list:
            return f"any[]"
        if get_origin(t) is dict:
            return f"table<{self.type_name(get_args(t)[0])},{self.type_name(get_args(t)[1])}>"
        if t is dict:
            return f"table"
        if t is Any:
            return "any"
        if t is type(None):
            return "nil"
        raise Exception(f"Unknown type {t}")

    def safe_name(self, name: str) -> str:
        if name == "goto":
            return "goto_"
        return name

    def prepare_doc(self, doc: str, multiline: bool):
        lines = doc.strip().splitlines()
        if len(lines) == 1:
            return lines[0]
        if multiline:
            return f"{lines[0]}\n" + "\n".join(
                f"--- {line.strip()}" for line in lines[1:]
            )
        return " ".join(line.strip() for line in lines)

    def field_annotation(self, field: ModelField) -> str:
        description = field.field_info.description and self.prepare_doc(
            field.field_info.description, multiline=False
        )
        return f"---@field {field.name}{'?' if not field.required else ''} {self.type_name(field.outer_type_)} {description or ''}"

    def class_doc(self, model_cls: type[BaseModel]) -> str | None:
        if model_cls.__doc__:
            return model_cls.__doc__
        cls_schema = self.schema["definitions"].get(model_cls.__name__)
        if not cls_schema:
            return
        if sub_types := cls_schema.get("allOf"):
            for definition in sub_types:
                if sub_desc := definition.get("description"):
                    return sub_desc

    def create_class(self, t, class_name: str | None = None) -> list[str]:
        sub_classes = []
        lines = []
        t_name = class_name or self.type_name(t)
        if self.is_model(t) and t_name not in self.known_types:
            self.known_types.add(t_name)
            for field in t.__fields__.values():
                if field_sub_classes := self.create_class(field.outer_type_):
                    sub_classes += field_sub_classes
                    sub_classes.append("")
                lines.append(self.field_annotation(field))
            class_doc = self.class_doc(t)
            class_prefix = (
                [f"--- {self.prepare_doc(class_doc, multiline=True)}"]
                if class_doc
                else []
            )
            class_prefix.append(f"---@class {t_name}")
            lines = [
                *class_prefix,
                *lines,
            ]
        else:
            try:
                sub_classes = [
                    line
                    for sub_type in get_args(t)
                    for line in self.create_class(sub_type)
                ]
            except TypeError:
                ...
        return [
            *sub_classes,
            *lines,
        ]

    def create_request(
        self, request_cls: type[BaseModel], response_cls: type[BaseModel]
    ) -> list[str]:
        (command,) = list(request_cls.__fields__["command"].outer_type_.__members__)

        request_summary = self.extract_summary(request_cls)
        types = []
        signature = []
        if request_summary.description:
            signature.append(
                f"--- {self.prepare_doc(request_summary.description, multiline=True)}"
            )
        signature.append("---@async")
        if arg_summary := request_summary.fields.get("arguments"):
            types = self.create_class(arg_summary.type)
            signature += [
                f"---@param args {arg_summary.type_name}",
                f"function DAPUIRequestsClient.{self.safe_name(command)}(args) end",
            ]
        else:
            signature += [
                f"function DAPUIRequestsClient.{self.safe_name(command)}() end",
            ]

        response_summary = self.extract_summary(response_cls)
        if body_summary := response_summary.fields.get("body"):
            types.append("")
            types += self.create_class(body_summary.type, response_summary.type_name)
            signature.insert(-1, f"---@return {response_summary.type_name}")

        x = [
            *types,
            "",
            *signature,
            "",
            "",
        ]
        return x

    def create_event_listener(self, event_cls: type[BaseModel]) -> list[str]:
        (event,) = list(event_cls.__fields__["event"].outer_type_.__members__)
        event_summary = self.extract_summary(event_cls)
        types = []
        signature = []
        if event_summary.description:
            signature.append(
                f"--- {self.prepare_doc(event_summary.description, multiline=True)}"
            )
        if body_summary := event_summary.fields.get("body"):
            body_class_name = f"{event_summary.type_name}Args"
            types = self.create_class(body_summary.type, body_class_name)
            signature.append(f"---@param listener fun(args: {body_class_name})")
        else:
            signature.append(f"---@param listener fun()")

        signature.append(f"---@param opts? dapui.client.ListenerOpts")
        x = [
            *types,
            "",
            *signature,
            f"function DAPUIEventListenerClient.{self.safe_name(event)}(listener, opts) end",
            "",
            "",
        ]
        return x

    def create_request_listener(
        self, request_cls: type[BaseModel], response_cls: type[BaseModel]
    ) -> list[str]:
        (command,) = list(request_cls.__fields__["command"].outer_type_.__members__)

        request_summary = self.extract_summary(request_cls)
        response_summary = self.extract_summary(response_cls)

        listener_args = {}
        if args := request_summary.fields.get("arguments"):
            listener_args["request"] = args.type
        listener_args["error"] = dict | None
        if args := response_summary.fields.get("body"):
            listener_args["response"] = create_model(
                response_cls.__name__, __base__=args.type
            )

        args_summary = self.extract_summary(
            create_model(
                f"{command}RequestListenerArgs",
                **{name: (t, Field()) for name, t in listener_args.items()},
            )
        )
        types = self.create_class(args_summary.type)
        return [
            *types,
            "",
            f"---@param listener fun(args: {args_summary.type_name}): boolean | nil",
            f"---@param opts? dapui.client.ListenerOpts",
            f"function DAPUIEventListenerClient.{self.safe_name(command)}(listener, opts) end",
            "",
            "",
        ]

    PREFIX = """
---@class dapui.DAPRequestsClient
local DAPUIRequestsClient = {}

---@class dapui.DAPEventListenerClient
local DAPUIEventListenerClient = {}

---@class dapui.client.ListenerOpts
---@field before boolean Run before event/request is processed by nvim-dap
"""

    def generate_types(self) -> str:
        output = f"--- Generated on {datetime.utcnow()}\n"
        output += self.PREFIX

        member_names = dict(i.getmembers(self.models))
        for _, member in i.getmembers(self.models, self.is_model):
            member.update_forward_refs(**member_names)
        for name, request in i.getmembers(
            self.models,
            lambda x: x is not self.models.Request
            and i.isclass(x)
            and issubclass(x, self.models.Request),
        ):
            try:
                output += "\n".join(
                    self.create_request(
                        request,
                        getattr(self.models, name.replace("Request", "Response")),
                    )
                )
                output += "\n".join(
                    self.create_request_listener(
                        request,
                        getattr(self.models, name.replace("Request", "Response")),
                    )
                )
            except Exception as e:
                logger.exception(f"Failed to create {name}: {e}")

        for name, event in i.getmembers(
            self.models,
            lambda x: x is not self.models.Event
            and i.isclass(x)
            and issubclass(x, self.models.Event),
        ):
            try:
                output += "\n".join(self.create_event_listener(event))
            except Exception as e:
                logger.exception(f"Failed to create {name}: {e}")
        output += "\nreturn { request = DAPUIRequestsClient, listen = DAPUIEventListenerClient }"
        return output


generator = DAPTypesGenerator()
logger.info("Generating types")

types = generator.generate_types()

logger.info("Outputting types")
print(types)
```

## File: `scripts/style`
```
#!/bin/bash

stylua lua tests
```

## File: `scripts/test`
```
#!/bin/bash
tempfile=".test_output.tmp"

if [[ -n $1 ]]; then
	nvim --headless --noplugin -u tests/init.vim -c "PlenaryBustedFile $1" | tee "${tempfile}"
else
	nvim --headless --noplugin -u tests/init.vim -c "PlenaryBustedDirectory tests/ {minimal_init = 'tests/init.vim'}" | tee "${tempfile}"
fi

# Plenary doesn't emit exit code 1 when tests have errors during setup
errors=$(sed 's/\x1b\[[0-9;]*m//g' "${tempfile}" | awk '/(Errors|Failed) :/ {print $3}' | grep -v '0')

rm "${tempfile}"

if [[ -n $errors ]]; then
  echo "Tests failed"
  exit 1
fi

exit 0
```

## File: `tests/init.vim`
```
set rtp+=.
set rtp+=../plenary.nvim
set rtp+=../nvim-dap
set rtp+=../nvim-nio
runtime! plugin/plenary.vim
```

## File: `tests/minimal_init.lua`
```
local lazypath = vim.fn.stdpath("data") .. "/lazy"
vim.notify = print
vim.opt.rtp:append(".")
vim.opt.rtp:append(lazypath .. "/nvim-dap")
vim.opt.rtp:append(lazypath .. "/nvim-nio")

local home = os.getenv("HOME")
vim.opt.rtp:append(home .. "/Dev/nvim-nio")

vim.opt.swapfile = false
vim.cmd("runtime! plugin/plenary.vim")
A = function(...)
  print(vim.inspect(...))
end
```

## File: `tests/unit/util_spec.lua`
```
local util = require("dapui.util")

describe("checking is_uri", function()
  it("returns true on uri", function()
    assert(util.is_uri("file://myfile"))
  end)

  it("returns false on non-uri", function()
    assert(not util.is_uri("/myfile"))
  end)
end)

describe("checking pretty name", function()
  it("converts a path", function()
    local uri = "/home/file.py"
    local result = util.pretty_name(uri)
    assert.equals(result, "file.py")
  end)

  it("converts a uri", function()
    local uri = "file:///home/file.py"
    local result = util.pretty_name(uri)
    assert.equals(result, "file.py")
  end)
end)

describe("checking format_error", function()
  it("formats variables", function()
    local error = {
      body = {
        error = {
          format = 'Unable to eval expression: "{e}"',
          variables = { e = "could not find symbol value for a" },
        },
      },
    }
    local expected = 'Unable to eval expression: "could not find symbol value for a"'
    local result = util.format_error(error)
    assert.equals(expected, result)
  end)
  it("returns message", function()
    local error = { message = "Couldn't evaluate expression 'a'" }
    local expected = "Couldn't evaluate expression 'a'"
    local result = util.format_error(error)
    assert.equals(expected, result)
  end)
  it("returns message within body", function()
    local error = { body = { message = "Couldn't evaluate expression 'a'" } }
    local expected = "Couldn't evaluate expression 'a'"
    local result = util.format_error(error)
    assert.equals(expected, result)
  end)
end)

describe("checking partial", function()
  it("supplies preloaded args", function()
    local f = function(a, b)
      assert.equals(a, 1)
      assert.equals(b, 2)
    end
    local g = util.partial(f, 1, 2)
    g()
  end)

  it("supplies new args", function()
    local f = function(a, b)
      assert.equals(a, 1)
      assert.equals(b, 2)
    end
    local g = util.partial(f, 1)
    g(2)
  end)
end)

describe("checking round", function()
  it("rounds down", function()
    assert.equal(0, util.round(0.1))
  end)
  it("rounds up", function()
    assert.equal(1, util.round(0.5))
  end)
end)
```

## File: `tests/unit/config/init_spec.lua`
```
local config = require("dapui.config")

describe("checking setup function", function()
  it("allows nil config", function()
    config.setup()
    assert.equal(config.icons.expanded, "")
  end)

  it("allows empty config", function()
    config.setup({})
    assert.equal(config.icons.expanded, "")
  end)

  it("allows overriding values", function()
    config.setup({ icons = { expanded = "X" } })
    assert.equal(config.icons.expanded, "X")
  end)

  it("fills mappings", function()
    config.setup({ mappings = { edit = "e" } })
    assert.same({ "e" }, config.mappings.edit)
  end)

  it("fills elements", function()
    config.setup({ layouts = { { size = 10, position = "left", elements = { "scopes" } } } })
    assert.same({ { id = "scopes", size = 1 } }, config.layouts[1].elements)
  end)

  it("fills elements with proportional size", function()
    config.setup({
      layouts = { { size = 10, position = "left", elements = { "scopes", "stacks" } } },
    })
    assert.same(
      { { id = "scopes", size = 0.5 }, { id = "stacks", size = 0.5 } },
      config.layouts[1].elements
    )
  end)
end)
```

## File: `tests/unit/elements/breakpoints_spec.lua`
```
local nio = require("nio")
local Breakpoints = require("dapui.elements.breakpoints")
local a = nio.tests
local tests = require("dapui.tests")
tests.bootstrap()
local mocks = tests.mocks

describe("breakpoints element", function()
  local client, breakpoints, buf
  local init_bps = {
    test_a = {
      lines = {
        "line_a_1",
        "line_a_2",
        "line_a_3",
      },
      bps = {
        [1] = {},
        [3] = { condition = "a + 3 == 3" },
      },
    },
    test_b = {
      lines = {
        "line_b_1",
        "line_b_2",
        "line_b_3",
      },
      bps = {
        [2] = { log_message = "here" },
      },
    },
  }
  a.before_each(function()
    client = mocks.client({
      current_frame = {
        id = 1,
        line = 1,
        source = {
          path = "test_a",
        },
      },
    })
    for path, data in pairs(init_bps) do
      local path_buf = vim.api.nvim_create_buf(true, true)
      nio.api.nvim_buf_set_name(path_buf, path)
      nio.api.nvim_buf_set_lines(path_buf, 0, -1, false, data.lines)
      for line, bp in pairs(data.bps) do
        client.breakpoints.toggle(path_buf, line, bp)
      end
    end
    breakpoints = Breakpoints(client)
    breakpoints.render()
    buf = breakpoints.buffer()
  end)

  after_each(function()
    pcall(vim.api.nvim_buf_delete, buf, { force = true })
    for path, _ in pairs(init_bps) do
      local path_buf = vim.fn.bufnr(path)
      pcall(vim.api.nvim_buf_delete, path_buf, { force = true })
    end
    breakpoints = nil
  end)

  a.it("renders lines", function()
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same({
      "test_a:",
      " 1 line_a_1",
      " 3 line_a_3",
      "   Condition: a + 3 == 3",
      "",
      "test_b:",
      " 2 line_b_2",
      "   Log Message: here",
    }, lines)
  end)

  a.it("renders highlights", function()
    local highlights = tests.util.get_highlights(buf)
    assert.same({
      { "DapUIBreakpointsPath", 0, 0, 0, 6 },
      { "DapUIBreakpointsCurrentLine", 1, 1, 1, 2 },
      { "DapUIBreakpointsLine", 2, 1, 2, 2 },
      { "DapUIBreakpointsInfo", 3, 3, 3, 13 },
      { "DapUIBreakpointsPath", 5, 0, 5, 6 },
      { "DapUIBreakpointsLine", 6, 1, 6, 2 },
      { "DapUIBreakpointsInfo", 7, 3, 7, 15 },
    }, highlights)
  end)

  a.it("renders highlights with toggled breakpoint", function()
    local keymaps = tests.util.get_mappings(buf)
    keymaps.t(3)
    local highlights = tests.util.get_highlights(buf)
    assert.same({
      { "DapUIBreakpointsPath", 0, 0, 0, 6 },
      { "DapUIBreakpointsCurrentLine", 1, 1, 1, 2 },
      { "DapUIBreakpointsDisabledLine", 2, 1, 2, 2 },
      { "DapUIBreakpointsInfo", 3, 3, 3, 13 },
      { "DapUIBreakpointsPath", 5, 0, 5, 6 },
      { "DapUIBreakpointsLine", 6, 1, 6, 2 },
      { "DapUIBreakpointsInfo", 7, 3, 7, 15 },
    }, highlights)
  end)
end)
```

## File: `tests/unit/elements/hover_spec.lua`
```
local nio = require("nio")
local a = nio.tests
local Hover = require("dapui.elements.hover")
local tests = require("dapui.tests")
tests.bootstrap()
local mocks = tests.mocks

describe("hover element", function()
  ---@type dapui.elements.hover
  local hover
  local client, buf
  a.before_each(function()
    client = mocks.client({
      current_frame = {
        id = 1,
      },
      requests = {
        evaluate = mocks.evaluate({
          expressions = {
            a = "'a value'",
            ["b - 1"] = { result = "1", type = "number" },
            c = { result = "{ d = 1 }", type = "table", variablesReference = 1 },
          },
        }),
        variables = mocks.variables({
          variables = {
            [1] = {
              {
                name = "d",
                value = "1",
                type = "number",
                variablesReference = 0,
              },
            },
          },
        }),
      },
    })
    hover = Hover(client)
    buf = hover.buffer()
  end)
  after_each(function()
    pcall(vim.api.nvim_buf_delete, buf, { force = true })
    hover = nil
  end)
  a.it("renders lines", function()
    hover.set_expression("a")
    nio.sleep(10)
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same({ "a = 'a value'" }, lines)
  end)
  a.it("renders lines after expression update", function()
    hover.set_expression("a")
    hover.set_expression("b - 1")
    nio.sleep(10)
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same({ "b - 1 number = 1" }, lines)
  end)

  a.it("renders lines with expandable expression", function()
    hover.set_expression("c")
    nio.sleep(10)
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same({ " c table = { d = 1 }" }, lines)
  end)

  a.it("renders highlights with expandable expression", function()
    hover.set_expression("c")
    nio.sleep(10)
    local formatted = tests.util.get_highlights(buf)
    assert.same({
      { "DapUIDecoration", 0, 0, 0, 4 },
      { "DapUIType", 0, 6, 0, 11 },
      { "DapUIValue", 0, 14, 0, 23 },
    }, formatted)
  end)

  describe("with expanded variables", function()
    a.it("renders expanded lines", function()
      hover.set_expression("c")
      nio.sleep(10)
      local keymaps = tests.util.get_mappings(hover.buffer())
      keymaps["<CR>"](1)
      nio.sleep(10)

      local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
      assert.same({ " c table = { d = 1 }", "   d number = 1" }, lines)
    end)
    a.it("renders expanded highlights", function()
      hover.set_expression("c")
      nio.sleep(10)
      local keymaps = tests.util.get_mappings(hover.buffer())
      keymaps["<CR>"](1)
      nio.sleep(10)

      local formatted = tests.util.get_highlights(buf)
      assert.same({
        { "DapUIDecoration", 0, 0, 0, 4 },
        { "DapUIType", 0, 6, 0, 11 },
        { "DapUIValue", 0, 14, 0, 23 },
        { "DapUIDecoration", 1, 1, 1, 2 },
        { "DapUIVariable", 1, 3, 1, 4 },
        { "DapUIType", 1, 5, 1, 11 },
        { "DapUIValue", 1, 14, 1, 15 },
      }, formatted)
    end)
  end)
end)
```

## File: `tests/unit/elements/scopes_spec.lua`
```
local nio = require("nio")
local a = nio.tests
local Scopes = require("dapui.elements.scopes")
local tests = require("dapui.tests")
tests.bootstrap()
local mocks = tests.mocks

describe("scopes element", function()
  ---@type dapui.DAPClient
  local client
  local scopes, buf
  a.before_each(function()
    client = mocks.client({
      current_frame = {
        id = 1,
      },
      requests = {
        scopes = mocks.scopes({
          scopes = {
            [1] = {
              {
                name = "Locals",
                variablesReference = 1,
              },
              {
                name = "Globals",
                variablesReference = 2,
              },
            },
          },
        }),
        variables = mocks.variables({
          variables = {
            [1] = {
              {
                name = "a",
                value = "1",
                type = "number",
                variablesReference = 0,
              },
              {
                name = "b",
                value = "2",
                type = "number",
                variablesReference = 3,
              },
            },
            [2] = {
              {
                name = "CONST_A",
                value = "true",
                type = "boolean",
                variablesReference = 0,
              },
            },
            [3] = {
              {
                name = "c",
                value = "'3'",
                type = "string",
                variablesReference = 0,
              },
            },
          },
        }),
      },
    })
    scopes = Scopes(client)
    buf = scopes.buffer()
    client.request.scopes({ frameId = 1 })
  end)
  after_each(function()
    pcall(vim.api.nvim_buf_delete, buf, { force = true })
    scopes = nil
  end)
  a.it("renders initial lines", function()
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same({
      " Locals:",
      "   a number = 1",
      "  b number = 2",
      "",
      " Globals:",
      "   CONST_A boolean = true",
    }, lines)
  end)

  a.it("renders initial highlights", function()
    local formatted = tests.util.get_highlights(buf)
    assert.same({
      { "DapUIDecoration", 0, 0, 0, 3 },
      { "DapUIScope", 0, 4, 0, 10 },
      { "DapUIDecoration", 1, 1, 1, 2 },
      { "DapUIVariable", 1, 3, 1, 4 },
      { "DapUIType", 1, 5, 1, 11 },
      { "DapUIValue", 1, 14, 1, 15 },
      { "DapUIDecoration", 2, 1, 2, 4 },
      { "DapUIVariable", 2, 5, 2, 6 },
      { "DapUIType", 2, 7, 2, 13 },
      { "DapUIValue", 2, 16, 2, 17 },
      { "DapUIDecoration", 4, 0, 4, 3 },
      { "DapUIScope", 4, 4, 4, 11 },
      { "DapUIDecoration", 5, 1, 5, 2 },
      { "DapUIVariable", 5, 3, 5, 10 },
      { "DapUIType", 5, 11, 5, 18 },
      { "DapUIValue", 5, 21, 5, 25 },
    }, formatted)
  end)

  describe("with expanded variables", function()
    a.it("renders expanded lines", function()
      local keymaps = tests.util.get_mappings(scopes.buffer())
      keymaps["<CR>"](3)
      nio.sleep(10)
      local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
      assert.same({
        " Locals:",
        "   a number = 1",
        "  b number = 2",
        "    c string = '3'",
        "",
        " Globals:",
        "   CONST_A boolean = true",
      }, lines)
    end)
    a.it("renders expanded highlights", function()
      local keymaps = tests.util.get_mappings(scopes.buffer())
      keymaps["<CR>"](3)
      nio.sleep(10)
      local formatted = tests.util.get_highlights(buf)
      assert.same({
        { "DapUIDecoration", 0, 0, 0, 3 },
        { "DapUIScope", 0, 4, 0, 10 },
        { "DapUIDecoration", 1, 1, 1, 2 },
        { "DapUIVariable", 1, 3, 1, 4 },
        { "DapUIType", 1, 5, 1, 11 },
        { "DapUIValue", 1, 14, 1, 15 },
        { "DapUIDecoration", 2, 1, 2, 4 },
        { "DapUIVariable", 2, 5, 2, 6 },
        { "DapUIType", 2, 7, 2, 13 },
        { "DapUIValue", 2, 16, 2, 17 },
        { "DapUIDecoration", 3, 2, 3, 3 },
        { "DapUIVariable", 3, 4, 3, 5 },
        { "DapUIType", 3, 6, 3, 12 },
        { "DapUIValue", 3, 15, 3, 18 },
        { "DapUIDecoration", 5, 0, 5, 3 },
        { "DapUIScope", 5, 4, 5, 11 },
        { "DapUIDecoration", 6, 1, 6, 2 },
        { "DapUIVariable", 6, 3, 6, 10 },
        { "DapUIType", 6, 11, 6, 18 },
        { "DapUIValue", 6, 21, 6, 25 },
      }, formatted)
    end)
  end)
end)
```

## File: `tests/unit/elements/stacks_spec.lua`
```
local nio = require("nio")
local a = nio.tests
local Stacks = require("dapui.elements.stacks")
local tests = require("dapui.tests")
tests.bootstrap()
local mocks = tests.mocks

describe("stacks element", function()
  local client, stacks, buf
  a.before_each(function()
    client = mocks.client({
      current_frame = {
        id = 1,
      },
      requests = {
        scopes = mocks.scopes({
          scopes = {
            [1] = {
              {
                name = "Locals",
                variablesReference = 1,
              },
              {
                name = "Globals",
                variablesReference = 2,
              },
            },
          },
        }),
        threads = mocks.threads({
          threads = {
            {
              id = 1,
              name = "Thread 1",
            },
            {
              id = 2,
              name = "Thread 2",
            },
          },
        }),
        stackTrace = mocks.stack_traces({
          stack_traces = {
            [1] = {
              {
                id = 1,
                name = "stack_frame_1",
                source = {
                  name = "file_1",
                },
                line = 1,
              },
              {
                id = 2,
                name = "stack_frame_2",
                source = {
                  name = "file_2",
                },
                line = 2,
                presentationHint = "subtle",
              },
            },
            [2] = {
              {
                id = 3,
                name = "stack_frame_3",
                source = {
                  name = "file_3",
                },
                line = 3,
              },
              {
                id = 4,
                name = "stack_frame_4",
                source = {
                  name = "file_4",
                },
                line = 4,
              },
            },
          },
        }),
      },
    })
    stacks = Stacks(client)
    client.request.threads()
    client.request.scopes({ frameId = 1 })
    buf = stacks.buffer()
    nio.sleep(10)
  end)
  after_each(function()
    pcall(vim.api.nvim_buf_delete, buf, { force = true })
    stacks = nil
    client.shutdown()
  end)
  a.it("renders initial lines", function()
    stacks.render()
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same({
      "Thread 1:",
      " stack_frame_1 file_1:1",
      "",
      "Thread 2:",
      " stack_frame_3 file_3:3",
      " stack_frame_4 file_4:4",
      "",
      "",
    }, lines)
  end)

  a.it("renders initial highlights", function()
    stacks.render()
    local formatted = tests.util.get_highlights(buf)
    assert.same({
      { "DapUIThread", 0, 0, 0, 8 },
      { "DapUICurrentFrameName", 1, 4, 1, 17 },
      { "DapUISource", 1, 18, 1, 24 },
      { "DapUILineNumber", 1, 25, 1, 26 },
      { "DapUIThread", 3, 0, 3, 8 },
      { "DapUIFrameName", 4, 1, 4, 14 },
      { "DapUISource", 4, 15, 4, 21 },
      { "DapUILineNumber", 4, 22, 4, 23 },
      { "DapUIFrameName", 5, 1, 5, 14 },
      { "DapUISource", 5, 15, 5, 21 },
      { "DapUILineNumber", 5, 22, 5, 23 },
    }, formatted)
  end)

  describe("with subtle frames shown", function()
    a.it("renders expanded lines", function()
      stacks.render()
      local keymaps = tests.util.get_mappings(stacks.buffer())
      keymaps["t"](1)
      nio.sleep(10)
      local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
      assert.same({
        "Thread 1:",
        " stack_frame_1 file_1:1",
        " stack_frame_2 file_2:2",
        "",
        "Thread 2:",
        " stack_frame_3 file_3:3",
        " stack_frame_4 file_4:4",
        "",
        "",
      }, lines)
    end)
    a.it("renders expanded highlights", function()
      stacks.render()
      local keymaps = tests.util.get_mappings(stacks.buffer())
      keymaps["t"](1)
      stacks.render()
      local formatted = tests.util.get_highlights(buf)
      assert.same({
        { "DapUIThread", 0, 0, 0, 8 },
        { "DapUICurrentFrameName", 1, 4, 1, 17 },
        { "DapUISource", 1, 18, 1, 24 },
        { "DapUILineNumber", 1, 25, 1, 26 },
        { "DapUIFrameName", 2, 1, 2, 14 },
        { "DapUISource", 2, 15, 2, 21 },
        { "DapUILineNumber", 2, 22, 2, 23 },
        { "DapUIThread", 4, 0, 4, 8 },
        { "DapUIFrameName", 5, 1, 5, 14 },
        { "DapUISource", 5, 15, 5, 21 },
        { "DapUILineNumber", 5, 22, 5, 23 },
        { "DapUIFrameName", 6, 1, 6, 14 },
        { "DapUISource", 6, 15, 6, 21 },
        { "DapUILineNumber", 6, 22, 6, 23 },
      }, formatted)
    end)
  end)
end)
```

## File: `tests/unit/elements/watches_spec.lua`
```
local nio = require("nio")
local a = nio.tests
local Watches = require("dapui.elements.watches")
local tests = require("dapui.tests")
tests.bootstrap()
local mocks = tests.mocks

describe("watches element", function()
  ---@type dapui.elements.watches
  local watches
  local client, buf
  a.before_each(function()
    client = mocks.client({
      current_frame = {
        id = 1,
      },
      requests = {
        scopes = mocks.scopes({
          scopes = { [1] = {} },
        }),
        evaluate = mocks.evaluate({
          expressions = {
            a = "'a value'",
            ["b - 1"] = { result = "1", type = "number" },
            c = { result = "{ d = 1 }", type = "table", variablesReference = 1 },
          },
        }),
        variables = mocks.variables({
          variables = {
            [1] = {
              {
                name = "d",
                value = "1",
                type = "number",
                variablesReference = 0,
              },
            },
          },
        }),
      },
    })
    client.request.scopes({ frameId = 1 })
    watches = Watches(client)
    buf = watches.buffer()
    watches.render()
  end)
  after_each(function()
    pcall(vim.api.nvim_buf_delete, buf, { force = true })
    watches = nil
  end)
  describe("with no expressions", function()
    a.it("renders no expressions lines", function()
      local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
      assert.same({ "No Expressions", "" }, lines)
    end)
    a.it("renders lines after expression update", function()
      local highlights = tests.util.get_highlights(buf)
      assert.same({ { "DapUIWatchesEmpty", 0, 0, 0, 14 } }, highlights)
    end)
  end)

  a.it("renders lines with expressions", function()
    watches.add("a")
    watches.add("b - 1")
    watches.add("c")
    nio.sleep(10)
    local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
    assert.same(
      { " a = 'a value'", " b - 1 number = 1", " c table = { d = 1 }", "" },
      lines
    )
  end)

  a.it("renders highlights with expressions", function()
    watches.add("a")
    watches.add("b - 1")
    watches.add("c")
    nio.sleep(10)
    local highlights = tests.util.get_highlights(buf)
    assert.same({
      { "DapUIWatchesValue", 0, 0, 0, 3 },
      { "DapUIModifiedValue", 0, 8, 0, 17 },
      { "DapUIWatchesValue", 1, 0, 1, 3 },
      { "DapUIType", 1, 10, 1, 16 },
      { "DapUIModifiedValue", 1, 19, 1, 20 },
      { "DapUIWatchesValue", 2, 0, 2, 3 },
      { "DapUIType", 2, 6, 2, 11 },
      { "DapUIModifiedValue", 2, 14, 2, 23 },
    }, highlights)
  end)

  describe("with expanded variables", function()
    a.it("renders expanded lines", function()
      watches.add("c")
      watches.toggle_expand(1)
      nio.sleep(10)

      local lines = nio.api.nvim_buf_get_lines(buf, 0, -1, false)
      assert.same({ " c table = { d = 1 }", "   d number = 1", "" }, lines)
    end)
    a.it("renders expanded highlights", function()
      watches.add("c")
      watches.toggle_expand(1)
      nio.sleep(10)

      local highlights = tests.util.get_highlights(buf)
      assert.same({
        { "DapUIWatchesValue", 0, 0, 0, 3 },
        { "DapUIType", 0, 6, 0, 11 },
        { "DapUIModifiedValue", 0, 14, 0, 23 },
        { "DapUIDecoration", 1, 1, 1, 2 },
        { "DapUIVariable", 1, 3, 1, 4 },
        { "DapUIType", 1, 5, 1, 11 },
        { "DapUIValue", 1, 14, 1, 15 },
      }, highlights)
    end)
  end)
end)
```

## File: `tests/unit/windows/layout_spec.lua`
```
local api = vim.api
local util = require("dapui.util")
local windows = require("dapui.windows")

describe("checking window layout", function()
  local layout
  local win_configs = {
    { id = "a", size = 0.6 },
    { id = "b", size = 0.2 },
    { id = "c", size = 0.2 },
  }
  local buffers

  before_each(function()
    buffers = {}
    for index, win_conf in ipairs(win_configs) do
      local buf = api.nvim_create_buf(true, true)
      api.nvim_buf_set_name(buf, win_conf.id)
      buffers[index] = function()
        return buf
      end
    end

    layout = windows.area_layout(10, "right", win_configs, buffers)
    layout:open()
  end)

  after_each(function()
    for _, get_buf in ipairs(buffers) do
      vim.api.nvim_buf_delete(get_buf(), { force = true })
    end
    layout:close()
  end)

  it("opens all windows", function()
    for _, win_config in pairs(win_configs) do
      assert.Not.equal(-1, vim.fn.bufwinnr(win_config.id))
    end
  end)

  it("sizes area correctly", function()
    assert.equal(10, api.nvim_win_get_width(vim.fn.bufwinid(win_configs[1].id)))
  end)

  it("sizes windows correctly", function()
    local total_size = 0
    local heights = {}
    for _, win_config in pairs(win_configs) do
      local win = vim.fn.bufwinid(win_config.id)
      heights[win_config.id] = api.nvim_win_get_height(win)
      total_size = total_size + heights[win_config.id]
    end

    for i, win_config in ipairs(win_configs) do
      assert.equal(util.round(total_size * win_configs[i].size), heights[win_config.id])
    end
  end)

  it("closes all windows", function()
    layout:close()
    for _, win_config in pairs(win_configs) do
      assert.equal(-1, vim.fn.bufwinid(win_config.id))
    end
  end)

  it("retains sizes on close", function()
    local total_size = 0
    local heights = {}
    vim.api.nvim_win_set_height(vim.fn.bufwinid(win_configs[1].id), 1)
    vim.api.nvim_win_set_width(vim.fn.bufwinid(win_configs[1].id), 20)
    for _, win_config in pairs(win_configs) do
      local win = vim.fn.bufwinid(win_config.id)
      heights[win_config.id] = api.nvim_win_get_height(win)
      total_size = total_size + heights[win_config.id]
    end
    layout:update_sizes()
    layout:close()
    layout:open()
    assert.equal(20, api.nvim_win_get_width(vim.fn.bufwinid(win_configs[1].id)))
    for _, win_config in pairs(win_configs) do
      local win = vim.fn.bufwinid(win_config.id)
      assert.equal(heights[win_config.id], api.nvim_win_get_height(win))
    end
  end)
end)
```

