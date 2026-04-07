---
id: textual
type: knowledge
owner: OA_Triage
---
# textual
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md


[![Discord](https://img.shields.io/discord/1026214085173461072)](https://discord.gg/Enf6Z3qhVr)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/textual)](https://pypi.org/project/textual/)
[![PyPI version](https://badge.fury.io/py/textual.svg?)](https://badge.fury.io/py/textual)
![OS support](https://img.shields.io/badge/OS-macOS%20Linux%20Windows-red)



![textual-splash](https://github.com/user-attachments/assets/4caeb77e-48c0-4cf7-b14d-c53ded855ffd)

# Textual

<img align="right" width="250" alt="clock" src="https://github.com/user-attachments/assets/63e839c3-5b8e-478d-b78e-cf7647eb85e8" />

Build cross-platform user interfaces with a simple Python API. Run your apps in the terminal *or* a web browser.

Textual's API combines modern Python with the best of developments from the web world, for a lean app development experience.
De-coupled components and an advanced [testing](https://textual.textualize.io/guide/testing/) framework ensure you can maintain your app for the long-term.

Want some more examples? See the [examples](https://github.com/Textualize/textual/tree/main/examples) directory.

```python
"""
An App to show the current time.
"""

from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits


class ClockApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield Digits("")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")


if __name__ == "__main__":
    app = ClockApp()
    app.run()
```

> [!TIP]
> Textual is an asynchronous framework under the hood. Which means you can integrate your apps with async libraries &mdash; if you want to.
> If you don't want or need to use async, Textual won't force it on you. 



<img src="https://img.spacergif.org/spacer.gif" width="1" height="64"/>

## Widgets

Textual's library of [widgets](https://textual.textualize.io/widget_gallery/) covers everything from buttons, tree controls, data tables, inputs, text areas, and more…
Combined with a flexible [layout](https://textual.textualize.io/how-to/design-a-layout/) system, you can realize any User Interface you need.

Predefined themes ensure your apps will look good out of the box. 


<table>

<tr>

  <td>
    
  ![buttons](https://github.com/user-attachments/assets/2ac26387-aaa3-41ed-bc00-7d488600343c)
    
  </td>

  <td>
    
![tree](https://github.com/user-attachments/assets/61ccd6e9-97ea-4918-8eda-3ee0f0d3770e)
    
  </td>
  
</tr>


<tr>

  <td>
    
  ![datatables](https://github.com/user-attachments/assets/3e1f9f7a-f965-4901-a114-3c188bd17695)
    
  </td>

  <td>
    
![inputs](https://github.com/user-attachments/assets/b02aa203-7c37-42da-a1bb-2cb244b7d0d3)
    
  </td>
  
</tr>
<tr>

<td>

![listview](https://github.com/user-attachments/assets/963603bc-aa07-4688-bd24-379962ece871)

</td>

<td>

![textarea](https://github.com/user-attachments/assets/cd4ba787-5519-40e2-8d86-8224e1b7e506)
  
</td>

  
</tr>

</table>


<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Installing

Install Textual via pip:

```
pip install textual textual-dev
```

See [getting started](https://textual.textualize.io/getting_started/) for details.


<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Demo


Run the following command to see a little of what Textual can do:

```
python -m textual
```

Or try the [textual demo](https://github.com/textualize/textual-demo) *without* installing (requires [uv](https://docs.astral.sh/uv/)):

```bash
uvx --python 3.12 textual-demo
```

<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Dev Console

<img align="right" width="40%" alt="devtools" src="https://github.com/user-attachments/assets/12c60d65-e342-4b2f-9372-bae0459a7552" />


How do you debug an app in the terminal that is also running in the terminal?

The `textual-dev` package supplies a dev console that connects to your application from another terminal.
In addition to system messages and events, your logged messages and print statements will appear in the dev console.

See [the guide](https://textual.textualize.io/guide/devtools/) for other helpful tools provided by the `textual-dev` package.

<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

## Command Palette


Textual apps have a *fuzzy search* command palette.
Hit `ctrl+p` to open the command palette.

It is easy to extend the command palette with [custom commands](https://textual.textualize.io/guide/command_palette/) for your application.


![Command Palette](https://github.com/user-attachments/assets/94d8ec5d-b668-4033-a5cb-bf820e1b8d60)

<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>

# Textual ❤️ Web

<img align="right" width="40%" alt="textual-serve" src="https://github.com/user-attachments/assets/a25820fb-87ae-433a-858b-ac3940169242">


Textual apps are equally at home in the browser as they are the terminal. Any Textual app may be served with `textual serve` &mdash; so you can share your creations on the web.
Here's how to serve the demo app:

```
textual serve "python -m textual"
```

In addition to serving your apps locally, you can serve apps with [Textual Web](https://github.com/Textualize/textual-web).

Textual Web's firewall-busting technology can serve an unlimited number of applications.

Since Textual apps have low system requirements, you can install them anywhere Python also runs. Turning any device into a connected device.
No desktop required!


<img src="https://img.spacergif.org/spacer.gif" width="1" height="32"/>


## Join us on Discord

Join the Textual developers and community on our [Discord Server](https://discord.gg/Enf6Z3qhVr).

```

### File: examples\README.md
```md
# Textual Examples

This directory contains example Textual applications.

To run them, navigate to the examples directory and enter `python` followed by the name of the Python file.

```
cd textual/examples
python pride.py
```

```

### File: notes\README.md
```md
# Developer notes

These are notes made by the developer, and _not_ to be considered documentation.

```

### File: questions\README.md
```md

# Questions

Your questions should go in this directory.

Question files should be named with the extension ".question.md".

To build the FAQ, install [faqtory](https://github.com/willmcgugan/faqtory) if you haven't already.
Faqtory is best installed via [pipx](https://github.com/pypa/pipx) to avoid any dependency conflicts:

```
pipx install faqtory
```

Then run the following from the top of the repository:

```
faqtory build
```

```

### File: reference\README.md
```md
Contains private docs, mainly for the developers reference

```

### File: docs\examples\styles\README.md
```md
These are the examples from the documentation, used to generate screenshots.

You can run them with the textual CLI.

For example:

```
textual run text_style.py
```

```

### File: .pre-commit-config.yaml
```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: check-ast  # simply checks whether the files parse as valid python
      - id: check-builtin-literals  # requires literal syntax when initializing empty or zero python builtin types
      - id: check-case-conflict  # checks for files that would conflict in case-insensitive filesystems
      - id: check-merge-conflict  # checks for files that contain merge conflict strings
      - id: check-json  # checks json files for parseable syntax
      - id: check-toml  # checks toml files for parseable syntax
      - id: check-yaml  # checks yaml files for parseable syntax
        args: [ '--unsafe' ]  # Instead of loading the files, simply parse them for syntax.
      - id: check-shebang-scripts-are-executable  # ensures that (non-binary) files with a shebang are executable
      - id: check-vcs-permalinks  # ensures that links to vcs websites are permalinks
      - id: end-of-file-fixer  # ensures that a file is either empty, or ends with one newline
      - id: mixed-line-ending  # replaces or checks mixed line ending
  - repo: https://github.com/pycqa/isort
    rev: '5.13.2'
    hooks:
      - id: isort
        name: isort (python)
        language_version: '3.11'
        args: ['--profile', 'black', '--filter-files']
  - repo: https://github.com/psf/black
    rev: '24.1.1'
    hooks:
      - id: black
  - repo: https://github.com/hadialqattan/pycln  # removes unused imports
    rev: v2.5.0
    hooks:
      - id: pycln
        language_version: '3.11'
        args: [--all]
  - repo: https://github.com/MarcoGorelli/absolufy-imports
    rev: v0.3.1
    hooks:
      - id: absolufy-imports
exclude: ^tests/snapshot_tests

```

### File: AI_POLICY.md
```md
This project accepts AI generated Pull Requests, as long as the following guidelines are met.

- The Pull Request must fill in the repository's pull request template.
- The Pull Request must identify itself as AI generated, including the name of the agent used.
- The Pull Request must link to a issue or discussion where a solution has been approved by a maintainer (@willmcgugan).

The maintainer reserves the right to close PRs without comment if the above are not met.

```

### File: CHANGELOG.md
```md
# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [8.2.2] - 2026-04-03

### Fixed

- Fixed Pointless style updates when resizing https://github.com/Textualize/textual/pull/6464

## [8.2.1] - 2026-03-29

### Fixed

- Fix crash when a widget disapears between selections https://github.com/Textualize/textual/pull/6455

## [8.2.0] - 2026-03-27

### Added 

- Auto-scrolling on select https://github.com/Textualize/textual/pull/6440
- Selecting over containers https://github.com/Textualize/textual/pull/6440
- Added `App.ENABLE_SELECT_AUTO_SCROLL`, `App.SELECT_AUTO_SCROLL_LINES`, `App.SELECT_AUTO_SCROLL_SPEED` to tweak auto scrolling behavior https://github.com/Textualize/textual/pull/6440

## [8.1.1] - 2026-03-10

### Fixed

- Hotfix for animation on complete https://github.com/Textualize/textual/pull/6412

## [8.1.0] - 2026-03-10

### Changed

- Replace circuar references in DOM with weak references to improve GC times https://github.com/Textualize/textual/pull/6410
- When animating an attribute a second time, the original `on_complete` is now called https://github.com/Textualize/textual/pull/6410

### Added

- Added experimental `App.PAUSE_GC_ON_SCROLL_` boolean (disabled by default) https://github.com/Textualize/textual/pull/6410

## [8.0.2] - 2026-03-03

### Changed

- Themes are now in alphabetical order in command palette https://github.com/Textualize/textual/pull/6405

### Fixed

- Fixed issues with Directory Tree https://github.com/Textualize/textual/pull/6405

## [8.0.1] - 2026-03-01

### Fixed

- `DirectoryTree` runs more operations in a thread to avoid micro-freezes 

### Changes

- Some tweaks to garbage collection to reduce gc time https://github.com/Textualize/textual/pull/6402

## [8.0.0] - 2026-02-16

### Added

- Added `mode` argument to `push_screen` and `push_screen_wait` to enable pushing a screen to a non-active mode https://github.com/Textualize/textual/pull/6362
- Added `App.mode_change_signal` and `App.screen_change_signal` https://github.com/Textualize/textual/pull/6362
- Added `Tabs.get_tab` https://github.com/Textualize/textual/pull/6362
- Added Catppuccin Frappe and Macchiato themes https://github.com/Textualize/textual/pull/6335

### Changed

- It is no longer a NOOP and warning to dismiss a non-active screen. The dismiss will still work, but the screen may not update if the current mode is not active. https://github.com/Textualize/textual/pull/6362
- Added 50ms delay when switching screens to allow state to udpate and prevent janky flash of old content https://github.com/Textualize/textual/pull/6362
- Breaking change: Changed `Select.BLANK` to `Select.NULL` to avoid clash with newer `Widget.BLANK` Classvar https://github.com/Textualize/textual/pull/6374
  
## [7.5.0] - 2026-01-30

### Changed

- The DataTable row cursor will extend to the full width if there is excess space https://github.com/Textualize/textual/pull/6345
- The DataTable will send a selected event on click, only if the cell / row / column is currently highlighted https://github.com/Textualize/textual/pull/6345

## [7.4.0] - 2026-01-25

### Added

- Added `pointer` rule https://github.com/Textualize/textual/pull/6339

## [7.3.0] - 2026-01-15

### Fixed

- Fixed triple click on command palette raising an exception https://github.com/Textualize/textual/pull/6329

### Added

- Added `DOM.query_one_optional`
- Added `default` parameter to `get_component_rich_style` get_component_rich_style

### Changed

- Added super+c (command on mac) alternative bindings for copy, for terminals that support it (Ghostty does)
- Allow `Sparkline` to be of any height, not just 1 https://github.com/Textualize/textual/pull/6171

## [7.2.0] - 2026-01-11

### Changed

- The help panel will look at ancestor widgets for a `HELP` attribute if there isn't one on the focused widget https://github.com/Textualize/textual/pull/6320

## [7.1.0] - 2026-01-10

### Fixed

- Fixed issue with missing refresh

### Added

- Added Widget.BLANK which can optimize rendering of large widgets (typically containers that scroll)

## [7.0.3] - 2026-01-09

### Fixed

- Fixed performance issue with large scrollable containers https://github.com/Textualize/textual/pull/6317

## [7.0.2] - 2026-01-09

### Fixed

- Removed superfluous style udpates when setting `display` attribute. https://github.com/Textualize/textual/pull/6316

## [7.0.1] - 2026-01-07

### Added

- Added a `refresh_styles` boolean to the `ScreenResult` message which reduces style updates when popping screens

## [7.0.0] - 2026-01-03

### Changed

- `Node.update_node_styles` has grown a `animate` parameter

### Added

- Added atom-one-dark and atom-one-light themes @NSPC911 https://github.com/Textualize/textual/pull/6301

## [6.12.0] - 2026-01-02

### Fixed

- Fixed unnecessary style update when popping screens, which may have caused noticable pauses changing screens (with a lot of widgets) https://github.com/Textualize/textual/pull/6304

### Changed

- Promoted private `_update_styes` to `update_node_styles` https://github.com/Textualize/textual/pull/6304

## [6.11.0] - 2025-12-18

### Added

- Added a `TextSelected` event. https://github.com/Textualize/textual/pull/6290

## [6.10.0] - 2025-12-16

### Fixed

- Fixed broken themes https://github.com/Textualize/textual/pull/6286
- Updated toggle button style for consistency https://github.com/Textualize/textual/pull/6286

## [6.9.0] - 2025-12-14

### Added

- Added Solarized Dark theme https://github.com/Textualize/textual/pull/6278
- Added Rosé Pine themes https://github.com/Textualize/textual/pull/6277

### Fixed

- Fixed fuzzy matcher displaying wrong matched characters with simple substring match https://github.com/Textualize/textual/pull/6282

## [6.8.0] - 2025-12-07

### Added

- Added `Content.blank` https://github.com/Textualize/textual/pull/6264

### Fixed

- Fixed `Input` cursor color display in ANSI mode (`ansi_color=True`) https://github.com/Textualize/textual/issues/6234
- Fixed alt modifier on systems without extended Key Protocol https://github.com/Textualize/textual/pull/6267
- Fixed an issue where alpha keys with modifiers weren't lower cased. If you have bound to something like `ctrl+A`, then change to `ctrl+shift+a` https://github.com/Textualize/textual/pull/6267
- Fixed exception when setting `loading` attribute before mount https://github.com/Textualize/textual/pull/6268
- Fixed issue with dim filter not using background (may cause snapshot failures) https://github.com/Textualize/textual/pull/6269

## [6.7.1] - 2025-12-1

### Fixed

- Fixed `Content.fold` https://github.com/Textualize/textual/pull/6256

## [6.7.0] - 2025-11-29

### Added

- Added `GridLayout.max_column_width` https://github.com/Textualize/textual/pull/6228
- Added `Content.fold` https://github.com/Textualize/textual/pull/6238
- Added `strip_control_codes` to Content constructors https://github.com/Textualize/textual/pull/6238

### Changed 

- Added `Screen.get_loading_widget` which deferes to `App.get_loading_widget` https://github.com/Textualize/textual/pull/6228

### Fixed 

- Fixed `anchor` with `ScrollView` widgets https://github.com/Textualize/textual/pull/6228

## [6.6.0] - 2025-11-10

### Fixed

- Fixed `TextArea` cursor display on wrapped lines https://github.com/Textualize/textual/pull/6196
- Fixed `remove_children` not refreshing layout https://github.com/Textualize/textual/pull/6206
- Fixed flicker with :hover pseudo class https://github.com/Textualize/textual/pull/6214
- Fixed scrollbar not updating after textarea paste https://github.com/Textualize/textual/pull/6219

### Added

- Added `grid_size` property to `GridLayout` https://github.com/Textualize/textual/pull/6210
- Exposed `NoSelection` and `BLANK` via `textual.widgets.select` https://github.com/Textualize/textual/pull/6214
- Added `Widget.FOCUS_ON_CLICK` classvar amd `Widget.focus_on_click` method https://github.com/Textualize/textual/pull/6216
- Added support for the kitty keyboard protocol on Windows https://github.com/Textualize/textual/pull/6207
- Added `Widget.mount_compose` https://github.com/Textualize/textual/pull/6216

### Changed

- Change highlight style of Select to only highlight the border, not the label https://github.com/Textualize/textual/pull/6214

## [6.5.0] - 2025-10-31

### Added

- Added `DOMNode.trap_focus` https://github.com/Textualize/textual/pull/6202

### Fixed

- Fixed issue with focus + scroll https://github.com/Textualize/textual/pull/6203

## [6.4.0] - 2025-10-22

### Fixed

- Fixed type hint aliasing for App under TYPE_CHECKING https://github.com/Textualize/textual/pull/6152
- Fixed circular dependency effecting `bazel` users https://github.com/Textualize/textual/pull/6163
- Fixed for text selection with double width characters https://github.com/Textualize/textual/pull/6186

### Changed

- Simplified system commands (command palette) to a single word https://github.com/Textualize/textual/pull/6183

## [6.3.0] - 2025-10-11

### Added

- Added scrollbar-visibility rule https://github.com/Textualize/textual/pull/6156

### Fixed

- Fixed highlight not auto-detecting lexer https://github.com/Textualize/textual/pull/6167

### Changed

- Dropped support for Python3.8 https://github.com/Textualize/textual/pull/6121/
- Added support for Python3.14 https://github.com/Textualize/textual/pull/6121/

## [6.2.1] - 2025-10-01

- Fix inability to copy text outside of an input/textarea when it was focused https://github.com/Textualize/textual/pull/6148
- Fix issue when copying text after a double click https://github.com/Textualize/textual/pull/6148

## [6.2.0] - 2025-09-30

### Changed

- Eager tasks are now enabled On Python3.12 and above https://github.com/Textualize/textual/pull/6102
- `Widget._arrange` is now public (as `Widget.arrange`) https://github.com/Textualize/textual/pull/6108
- Reduced number of layout operations required to update the screen https://github.com/Textualize/textual/pull/6108
- The :hover pseudo-class no applies to the first widget under the mouse with a hover style set https://github.com/Textualize/textual/pull/6132
- The footer key hover background is more visible https://github.com/Textualize/textual/pull/6132
- Made `App.delay_update` public https://github.com/Textualize/textual/pull/6137
- Pilot.click will return True if the initial mouse down is on the specified target https://github.com/Textualize/textual/pull/6139

### Added

- Added `DOMNode.displayed_and_visible_children` https://github.com/Textualize/textual/pull/6102
- Added `Widget.process_layout` https://github.com/Textualize/textual/pull/6105
- Added `App.viewport_size` https://github.com/Textualize/textual/pull/6105
- Added `Screen.size` https://github.com/Textualize/textual/pull/6105
- Added `compact` to Binding.Group https://github.com/Textualize/textual/pull/6132
- Added `Screen.get_hover_widgets_at` https://github.com/Textualize/textual/pull/6132
- Added `Content.wrap` https://github.com/Textualize/textual/pull/6138
- Added support to allow support for manual keys in add_columns as well. https://github.com/Textualize/textual/pull/5923

### Fixed

- Fixed issue where Segments with a style of `None` aren't rendered https://github.com/Textualize/textual/pull/6109
- Fixed visual glitches and crash when changing `DataTable.header_height` https://github.com/Textualize/textual/pull/6128
- Fixed TextArea.placeholder not handling multi-lines https://github.com/Textualize/textual/pull/6138
- Fixed issue with RichLog when App.theme is set early https://github.com/Textualize/textual/pull/6141
- Fixed children of collapsible not being focusable after collapsible is expanded https://github.com/Textualize/textual/pull/6143

## [6.1.0] - 2025-08-01

### Added

- Added `Button.flat` boolean to enable flat button style https://github.com/Textualize/textual/pull/6094
- Added `namespaces` parameter to `run_action` https://github.com/Textualize/textual/pull/6094
- Added "block" border style https://github.com/Textualize/textual/pull/6094

## [6.0.0] - 2025-08-31

### Fixed

- Fix type hint for SelectType: only hashable types are allowed. https://github.com/Textualize/textual/pull/6034
- Fixed `Content.expand_tabs` https://github.com/Textualize/textual/pull/6038
- Fixed return value for `Pilot.double_click` and `Pilot.triple_click` https://github.com/Textualize/textual/pull/6035
- Fixed sizing issue with `Pretty` widget https://github.com/Textualize/textual/pull/6040 https://github.com/Textualize/textual/pull/6041
- Fixed garbled inline app output when `inline_no_clear=True` https://github.com/Textualize/textual/pull/6080

### Added

- Added `BAR_RENDERABLE` to `ProgressBar` widget https://github.com/Textualize/textual/pull/5963
- Added `OptionList.set_options` https://github.com/Textualize/textual/pull/6048
- Added `TextArea.suggestion` https://github.com/Textualize/textual/pull/6048
- Added `TextArea.placeholder` https://github.com/Textualize/textual/pull/6048
- Added `Header.format_title` and `App.format_title` for easier customization of title in the Header https://github.com/Textualize/textual/pull/6051
- Added `Widget.get_line_filters` and `App.get_line_filters` https://github.com/Textualize/textual/pull/6057
- Added `Binding.Group` https://github.com/Textualize/textual/pull/6070
- Added `DOMNode.displayed_children` https://github.com/Textualize/textual/pull/6070
- Added `TextArea.hide_suggestion_on_blur` boolean https://github.com/Textualize/textual/pull/6070
- Added `OptionList.highlighted_option` property https://github.com/Textualize/textual/pull/6090
- Added `TextArea.update_suggestion` method https://github.com/Textualize/textual/pull/6090
- Added `textual.getters.app` https://github.com/Textualize/textual/pull/6089

### Changed

- Breaking change: The `renderable` property on the `Static` widget has been changed to `content`. https://github.com/Textualize/textual/pull/6041
- Breaking change: `HeaderTitle` widget is now a static, with no `text` and `sub_text` reactives https://github.com/Textualize/textual/pull/6051
- Breaking change: Renamed `Label` constructor argument `renderable` to `content` for consistency https://github.com/Textualize/textual/pull/6045
- Breaking change: Optimization to line API to avoid applying background styles to widget content. In practice this means that you can no longer rely on blank Segments automatically getting the background color.

## [5.3.0] - 2025-08-07

### Added

- Added `Content.simplify` https://github.com/Textualize/textual/pull/6023
- Added `textual.reactive.Initialize` https://github.com/Textualize/textual/pull/6023

### Fixed

- Fixed issue with IDs in markdown https://github.com/Textualize/textual/pull/6019 https://github.com/Textualize/textual/pull/6023

## [5.2.0] - 2025-08-01

### Added

- Added a 'stream' layout, which is a lot like vertical but with fewer supported rules (wh
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[will@textualize.io](mailto:will@textualize.io).
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
```

### File: CONTRIBUTING.md
```md
# Contributing to Textual

First of all, thanks for taking the time to contribute to Textual!

## How can I contribute?

You can contribute to Textual in many ways:

 1. [Report a bug](https://github.com/textualize/textual/issues/new?title=%5BBUG%5D%20short%20bug%20description&template=bug_report.md)
 2. Add a new feature
 3. Fix a bug
 4. Improve the documentation


## Setup

To make a code or documentation contribution you will need to set up Textual locally.
You can follow these steps:

 1. Make sure you have Poetry installed ([see instructions here](https://python-poetry.org))
 2. Clone the Textual repository
 3. Run `poetry shell` to create a virtual environment for the dependencies
 4. Run `make setup` to install all dependencies
 5. Make sure the latest version of Textual was installed by running the command `textual --version`
 6. Install the pre-commit hooks with the command `pre-commit install`

([Read this](#makefile-commands) if the command `make` doesn't work for you.)

## Demo

Once you have Textual installed, run the Textual demo to get an impression of what Textual can do and to double check that everything was installed correctly:

```bash
python -m textual
```

## Guidelines

- Read any issue instructions carefully. Feel free to ask for clarification if any details are missing.

- Add docstrings to all of your code (functions, methods, classes, ...). The codebase should have enough examples for you to copy from.

- Write tests for your code.
  - If you are fixing a bug, make sure to add regression tests that link to the original issue.
  - If you are implementing a visual element, make sure to add _snapshot tests_. [See below](#snapshot-testing) for more details.

## Before opening a PR

Before you open your PR, please go through this checklist and make sure you've checked all the items that apply:

 - [ ] Update the `CHANGELOG.md`
 - [ ] Format your code with black (`make format`)
 - [ ] All your code has docstrings in the style of the rest of the codebase
 - [ ] Your code passes all tests (`make test`)

([Read this](#makefile-commands) if the command `make` doesn't work for you.)

## Updating and building the documentation

If you change the documentation, you will want to build the documentation to make sure everything looks like it should.
The command `make docs-serve-offline` should start a server that will let you preview the documentation locally and that should reload whenever you save changes to the documentation or the code files.

([Read this](#makefile-commands) if the command `make` doesn't work for you.)

We strive to write our documentation in a clear and accessible way so, if you find any issues with the documentation, we encourage you to open an issue where you can enumerate the things you think should be changed or added.

Opening an issue or a discussion is typically better than opening a PR directly.
That's because there are many subjective considerations that go into writing documentation and we cannot expect you, a well-intentioned external contributor, to be aware of those subjective considerations that we take into account when writing our documentation.

Of course, this does not apply to objective/technical issues with the documentation like bugs or broken links.

## After opening a PR

When you open a PR, your code will be reviewed by one of the Textual maintainers.
In that review process,

- We will take a look at all of the changes you are making
- We might ask for clarifications (why did you do X or Y?)
- We might ask for more tests/more documentation
- We might ask for some code changes

The sole purpose of those interactions is to make sure that, in the long run, everyone has the best experience possible with Textual and with the feature you are implementing/fixing.

Don't be discouraged if a reviewer asks for code changes.
If you go through our history of pull requests, you will see that every single one of the maintainers has had to make changes following a review.

## Snapshot testing

Snapshot tests ensure that visual things (like widgets) look like they are supposed to.
PR [#1969](https://github.com/Textualize/textual/pull/1969) is a good example of what adding snapshot tests looks like: it amounts to a change in the file `tests/snapshot_tests/test_snapshots.py` that should run an app that you write and compare it against a historic snapshot of what that app should look like.

When you create a new snapshot test, run it with `pytest -vv tests/snapshot_tests/test_snapshots.py`.
Because you just created this snapshot test, there is no history to compare against and the test will fail.
After running the snapshot tests, you should see a link that opens an interface in your browser.
This interface should show all failing snapshot tests and a side-by-side diff between what the app looked like when the test ran versus the historic snapshot.

Make sure your snapshot app looks like it is supposed to and that you didn't break any other snapshot tests.
If everything looks fine, you can run `make test-snapshot-update` to update the snapshot history with your new snapshot.
This will write a new SVG file to the `tests/snapshot_tests/__snapshots__/` directory.
You should NOT modify these files by hand.
If a pre-existing snapshot tests fails, you should carefully inspect the diff and decide if the new snapshot is correct or if the pre-existing one is.
If the new snapshot is correct, you should update the snapshot history with your new snapshot using `make test-snapshot-update`.
If the pre-existing snapshot is correct, your change has likely introduced a bug, and you should try to fix it.
After fixing it, and checking the output of `make test-snapshot` now looks correct, you should run `make test-snapshot-update` to update the snapshot history with your new snapshot.


([Read this](#makefile-commands) if the command `make` doesn't work for you.)

## Join the community

Seems a little overwhelming?
Join our community on [Discord](https://discord.gg/Enf6Z3qhVr) to get help!

## Makefile commands

Textual has a `Makefile` file that contains the most common commands used when developing Textual.
([Read about Make and makefiles on Wikipedia.](https://en.wikipedia.org/wiki/Make_(software)))
If you don't have Make and you're on Windows, you may want to [install Make](https://stackoverflow.com/q/32127524/2828287).

```

### File: docs.md
```md
# Documentation Workflow

* Ensure you're inside a *Python 3.10+* virtual environment
* Run the live-reload server using `mkdocs serve` from the project root
* Create new pages by adding new directories and Markdown files inside `docs/*`

## Commands

- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

```

### File: .faq\FAQ.md
```md
---
hide:
  - navigation
---

<!-- Auto-generated by FAQtory -->
<!-- Do not edit by hand! -->

# Frequently Asked Questions


Welcome to the Textual FAQ.
Here we try and answer any question that comes up frequently.
If you can't find what you are looking for here, see our other [help](./help.md) channels.

{%- for question in questions %}

<a name="{{ question.slug }}"></a>
## {{ question.title }}

{{ question.body }}

---

{%- endfor %}

Generated by [FAQtory](https://github.com/willmcgugan/faqtory)

```

### File: .faq\suggest.md
```md
{%- if questions -%}
{% if questions|length == 1 %}
We found the following entry in the [FAQ]({{ faq_url }}) which you may find helpful:
{%- else %}
We found the following entries in the [FAQ]({{ faq_url }}) which you may find helpful:
{%- endif %}

{% for question in questions %}
- [{{ question.title }}]({{ faq_url }}#{{ question.slug }})
{%- endfor %}

Feel free to close this issue if you found an answer in the FAQ. Otherwise, please give us a little time to review.

{%- else -%}
Thank you for your issue. Give us a little time to review it.

PS. You might want to check the [FAQ]({{ faq_url }}) if you haven't done so already.
{%- endif %}

This project is developed and maintained by Will McGugan. Consider [sponsoring Will's work on this project](https://github.com/sponsors/willmcgugan) (and others).

This is an automated reply, generated by [FAQtory](https://github.com/willmcgugan/faqtory)

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
Thank you for contributing!

This project requires all PRs to link to an issue or discussion. Ideally signed off by @willmcgugan

**Link to issue or discussion**

<!-- paste link here -->

```

### File: docs\FAQ.md
```md
---
hide:
  - navigation
---

<!-- Auto-generated by FAQtory -->
<!-- Do not edit by hand! -->

# Frequently Asked Questions


Welcome to the Textual FAQ.
Here we try and answer any question that comes up frequently.
If you can't find what you are looking for here, see our other [help](./help.md) channels.

<a name="does-textual-support-images"></a>
## Does Textual support images?

Textual doesn't have built-in support for images yet, but it is on the [Roadmap](https://textual.textualize.io/roadmap/).

See also the [rich-pixels](https://github.com/darrenburns/rich-pixels) project for a Rich renderable for images that works with Textual.

---

<a name="how-can-i-fix-importerror-cannot-import-name-composeresult-from-textualapp-"></a>
## How can I fix ImportError cannot import name ComposeResult from textual.app ?

You likely have an older version of Textual. You can install the latest version by adding the `-U` switch which will force pip to upgrade.

The following should do it:

```
pip install textual-dev -U
```

---

<a name="how-can-i-select-and-copy-text-in-a-textual-app"></a>
## How can I select and copy text in a Textual app?

Textual supports text selection for most widgets, via click and drag. Press ctrl+c to copy.

For widgets that don't yet support text selection, you can try and use your terminal's builtin support.
Most terminal emulators offer a modifier key which you can hold while you click and drag to restore the behavior you
may expect from the command line. The exact modifier key depends on the terminal and platform you are running on.

- **iTerm** Hold the OPTION key.
- **Gnome Terminal** Hold the SHIFT key.
- **Windows Terminal** Hold the SHIFT key.

Refer to the documentation for your terminal emulator, if it is not listed above.

---

<a name="how-can-i-set-a-translucent-app-background"></a>
## How can I set a translucent app background?

Some terminal emulators have a translucent background feature which allows the desktop underneath to be partially visible.

This feature is unlikely to work with Textual, as the translucency effect requires the use of ANSI background colors, which Textual doesn't use.
Textual uses 16.7 million colors where available which enables consistent colors across all platforms and additional effects which aren't possible with ANSI colors.

For more information on ANSI colors in Textual, see [Why no ANSI Themes?](#why-doesnt-textual-support-ansi-themes).

---

<a name="how-do-i-center-a-widget-in-a-screen"></a>
## How do I center a widget in a screen?

!!! tip

    See [*How To Center Things*](https://textual.textualize.io/how-to/center-things/) in the
    Textual documentation for a more comprehensive answer to this question.

To center a widget within a container use
[`align`](https://textual.textualize.io/styles/align/). But remember that
`align` works on the *children* of a container, it isn't something you use
on the child you want centered.

For example, here's an app that shows a `Button` in the middle of a
`Screen`:

```python
from textual.app import App, ComposeResult
from textual.widgets import Button

class ButtonApp(App):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("PUSH ME!")

if __name__ == "__main__":
    ButtonApp().run()
```

If you use the above on multiple widgets, you'll find they appear to
"left-align" in the center of the screen, like this:

```
+-----+
|     |
+-----+

+---------+
|         |
+---------+

+---------------+
|               |
+---------------+
```

If you want them more like this:

```
     +-----+
     |     |
     +-----+

   +---------+
   |         |
   +---------+

+---------------+
|               |
+---------------+
```

The best approach is to wrap each widget in a [`Center`
container](https://textual.textualize.io/api/containers/#textual.containers.Center)
that individually centers it. For example:

```python
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button

class ButtonApp(App):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Center(Button("PUSH ME!"))
        yield Center(Button("AND ME!"))
        yield Center(Button("ALSO PLEASE PUSH ME!"))
        yield Center(Button("HEY ME ALSO!!"))

if __name__ == "__main__":
    ButtonApp().run()
```

---

<a name="how-do-i-fix-workerdeclarationerror"></a>
## How do I fix WorkerDeclarationError?

Textual version 0.31.0 requires that you set `thread=True` on the `@work` decorator if you want to run a threaded worker.

If you want a threaded worker, you would declare it in the following way:

```python
@work(thread=True)
def run_in_background():
    ...
```

If you *don't* want a threaded worker, you should make your work function `async`:

```python
@work()
async def run_in_background():
    ...
```

This change was made because it was too easy to accidentally create a threaded worker, which may produce unexpected results.

---

<a name="how-do-i-pass-arguments-to-an-app"></a>
## How do I pass arguments to an app?

When creating your `App` class, override `__init__` as you would when
inheriting normally. For example:

```python
from textual.app import App, ComposeResult
from textual.widgets import Static

class Greetings(App[None]):

    def __init__(self, greeting: str="Hello", to_greet: str="World") -> None:
        self.greeting = greeting
        self.to_greet = to_greet
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(f"{self.greeting}, {self.to_greet}")
```

Then the app can be run, passing in various arguments; for example:

```python
# Running with default arguments.
Greetings().run()

# Running with a keyword argument.
Greetings(to_greet="davep").run()

# Running with both positional arguments.
Greetings("Well hello", "there").run()
```

---

<a name="why-do-some-key-combinations-never-make-it-to-my-app"></a>
## Why do some key combinations never make it to my app?

Textual can only ever support key combinations that are passed on by your
terminal application. Which keys get passed on can differ from terminal to
terminal, and from operating system to operating system.

Because of this it's best to stick to key combinations that are known to be
universally-supported; these include the likes of:

- Letters
- Numbers
- Numbered function keys (especially F1 through F10)
- Space
- Return
- Arrow, home, end and page keys
- Control
- Shift

When [creating bindings for your
application](https://textual.textualize.io/guide/input/#bindings) we
recommend picking keys and key combinations from the above.

Keys that aren't normally passed through by terminals include Cmd and Option
on macOS, and the Windows key on Windows.

If you need to test what [key
combinations](https://textual.textualize.io/guide/input/#keyboard-input)
work in different environments you can try them out with `textual keys`.

---

<a name="why-doesnt-textual-look-good-on-macos"></a>
## Why doesn't Textual look good on macOS?

You may find that the default macOS Terminal.app doesn't render Textual apps (and likely other TUIs) very well, particularly when it comes to box characters.
For instance, you may find it displays misaligned blocks and lines like this:

<img width="1042" alt="Screenshot 2023-06-19 at 10 43 02" src="https://github.com/Textualize/textual/assets/554369/e61f3876-3dd1-4ac8-b380-22922c89c7d6">

You can (mostly) fix this by opening settings -> profiles > Text tab, and changing the font settings.
We have found that Menlo Regular font, with a character spacing of 1 and line spacing of 0.805 produces reasonable results.
If you want to use another font, you may have to tweak the line spacing until you get good results.

<img width="737" alt="Screenshot 2023-06-19 at 10 44 00" src="https://github.com/Textualize/textual/assets/554369/0a052a93-b1fd-4327-9d33-d954b51a9ad2">

With these changes, Textual apps render more as intended:

<img width="1042" alt="Screenshot 2023-06-19 at 10 43 23" src="https://github.com/Textualize/textual/assets/554369/a0c4aa05-c509-4ac1-b0b8-e68ce4433f70">

Even with this *fix*, Terminal.app has a few limitations.
It is limited to 256 colors, and can be a little slow compared to more modern alternatives.
Fortunately there are a number of free terminal emulators for macOS which produces high quality results.

We recommend any of the following terminals:

- [iTerm2](https://iterm2.com/)
- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [WezTerm](https://wezfurlong.org/wezterm/)

### Terminal.app colors

<img width="762" alt="Screenshot 2023-06-19 at 11 00 12" src="https://github.com/Textualize/textual/assets/554369/e0555d23-e141-4069-b318-f3965c880208">

### iTerm2 colors

<img width="1002" alt="Screenshot 2023-06-19 at 11 00 25" src="https://github.com/Textualize/textual/assets/554369/9a8cde57-5121-49a7-a2e0-5f6fc871b7a6">

---

<a name="why-doesnt-textual-support-ansi-themes"></a>
## Why doesn't Textual support ANSI themes?

Textual will not generate escape sequences for the 16 themeable *ANSI* colors.

This is an intentional design decision we took for the following reasons:

- Not everyone has a carefully chosen ANSI color theme. Color combinations which may look fine on your system, may be unreadable on another machine. There is very little an app author or Textual can do to resolve this. Asking users to simply pick a better theme is not a good solution, since not all users will know how.
- ANSI colors can't be manipulated in the way Textual can do with other colors. Textual can blend colors and produce light and dark shades from an original color, which is used to create more readable text and user interfaces. Color blending will also be used to power future accessibility features.

Textual has a design system which guarantees apps will be readable on all platforms and terminals, and produces better results than ANSI colors.

There is currently a light and dark version of the design system, but more are planned. It will also be possible for users to customize the source colors on a per-app or per-system basis. This means that in the future you will be able to modify the core colors to blend in with your chosen terminal theme.

!!! tip "Changed in version 0.80.0"

    Textual added an `ansi_color` boolean to App. If you set this to `True`, then Textual will not attempt to convert ANSI colors. Note that you will lose transparency effects if you enable this setting.

---

Generated by [FAQtory](https://github.com/willmcgugan/faqtory)

```

### File: docs\getting_started.md
```md

All you need to get started building Textual apps.

## Requirements

Textual requires Python 3.9 or later (if you have a choice, pick the most recent Python). Textual runs on Linux, macOS, Windows and probably any OS where Python also runs. 

!!! info "Your platform"

    ### :fontawesome-brands-linux: Linux (all distros)

    All Linux distros come with a terminal emulator that can run Textual apps.

    If you are using the Linux console (rather than a desktop environment), see [Linux console]](./linux-console.md) for details. 

    ### :material-apple: macOS

    The default terminal app is limited to 256 colors. We recommend installing a newer terminal such as [iterm2](https://iterm2.com/), [Ghostty](https://ghostty.org/), [Kitty](https://sw.kovidgoyal.net/kitty/), or [WezTerm](https://wezfurlong.org/wezterm/).

    ### :material-microsoft-windows: Windows

    The new [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-gb&gl=GB) runs Textual apps beautifully.


## Installation

Here's how to install Textual.

### From PyPI

You can install Textual via PyPI, with the following command:

```
pip install textual
```

If you plan on developing Textual apps, you should also install textual developer tools:

```
pip install textual-dev
```

If you would like to enable syntax highlighting in the [TextArea](./widgets/text_area.md) widget, you should specify the "syntax" extras when you install Textual:

```
pip install "textual[syntax]"
```

### From conda-forge

Textual is also available on [conda-forge](https://conda-forge.org/). The preferred package manager for conda-forge is currently [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html):

```
micromamba install -c conda-forge textual
```

And for the textual developer tools:

```
micromamba install -c conda-forge textual-dev
```

### Textual CLI

If you installed the developer tools you should have access to the `textual` command. There are a number of sub-commands available which will aid you in building Textual apps. Run the following for a list of the available commands:

```bash
textual --help
```

See [devtools](guide/devtools.md) for more about the `textual` command.

## Demo

Once you have Textual installed, run the following to get an impression of what it can do:

```bash
python -m textual
```

## Examples


The Textual repository comes with a number of example apps. To try out the examples, first clone the Textual repository:

=== "HTTPS"

    ```bash
    git clone https://github.com/Textualize/textual.git
    ```

=== "SSH"

    ```bash
    git clone git@github.com:Textualize/textual.git
    ```

=== "GitHub CLI"

    ```bash
    gh repo clone Textualize/textual
    ```


With the repository cloned, navigate to the `/examples/` directory where you will find a number of Python files you can run from the command line:

```bash
cd textual/examples/
python code_browser.py ../
```

### Widget examples

In addition to the example apps, you can also find the code listings used to generate the screenshots in these docs in the `docs/examples` directory.

## Need help?

See the [help](./help.md) page for how to get help with Textual, or to report bugs.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
