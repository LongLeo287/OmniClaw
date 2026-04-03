---
id: zsh-users-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.973223
---

# KNOWLEDGE EXTRACT: zsh-users
> **Extracted on:** 2026-03-30 18:01:32
> **Source:** zsh-users

---

## File: `zsh-autosuggestions.md`
```markdown
# 📦 zsh-users/zsh-autosuggestions [🔖 PENDING/APPROVE]
🔗 https://github.com/zsh-users/zsh-autosuggestions


## Meta
- **Stars:** ⭐ 35114 | **Forks:** 🍴 1928
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Fish-like autosuggestions for zsh

## README (trích đầu)
```
# zsh-autosuggestions

_[Fish](http://fishshell.com/)-like fast/unobtrusive autosuggestions for zsh._

It suggests commands as you type based on history and completions.

Requirements: Zsh v4.3.11 or later

[![Chat on Gitter](https://img.shields.io/gitter/room/zsh-users/zsh-autosuggestions.svg)](https://gitter.im/zsh-users/zsh-autosuggestions)

<a href="https://asciinema.org/a/37390" target="_blank"><img src="https://asciinema.org/a/37390.png" width="400" /></a>


## Installation

See [INSTALL.md](INSTALL.md).


## Usage

As you type commands, you will see a completion offered after the cursor in a muted gray color. This color can be changed by setting the `ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE` variable. See [configuration](#configuration).

If you press the <kbd>→</kbd> key (`forward-char` widget) or <kbd>End</kbd> (`end-of-line` widget) with the cursor at the end of the buffer, it will accept the suggestion, replacing the contents of the command line buffer with the suggestion.

If you invoke the `forward-word` widget, it will partially accept the suggestion up to the point that the cursor moves to.


## Configuration

You may want to override the default global config variables. Default values of these variables can be found [here](src/config.zsh).

**Note:** If you are using Oh My Zsh, you can put this configuration in a file in the `$ZSH_CUSTOM` directory. See their comments on [overriding internals](https://github.com/robbyrussell/oh-my-zsh/wiki/Customization#overriding-internals).


### Suggestion Highlight Style

Set `ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE` to configure the style that the suggestion is shown with. The default is `fg=8`, which will set the foreground color to color 8 from the [256-color palette](https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg). If your terminal only supports 8 colors, you will need to use a number between 0 and 7.

Background color can also be set, and the suggestion can be styled bold, underlined, or standout. For example, this would show suggestions with bold, underlined, pink text on a cyan background:

```sh
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#ff00ff,bg=cyan,bold,underline"
```

For more info, read the Character Highlighting section of the zsh manual: `man zshzle` or [online](http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html#Character-Highlighting).

**Note:** Some iTerm2 users have reported [not being able to see the suggestions](https://github.com/zsh-users/zsh-autosuggestions/issues/416#issuecomment-486516333). If this affects you, the problem is likely caused by incorrect color settings. In order to correct this, go into iTerm2's setting, navigate to profile > colors and make sure that the colors for Basic Colors > Background and ANSI Colors > Bright Black are **different**.


### Suggestion Strategy

`ZSH_AUTOSUGGEST_STRATEGY` is an array that specifies how suggestions should be generated. The strategies in the array are tried successively until a suggestion is found. T
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `zsh-syntax-highlighting.md`
```markdown
# 📦 zsh-users/zsh-syntax-highlighting [🔖 PENDING/APPROVE]
🔗 https://github.com/zsh-users/zsh-syntax-highlighting
🌐 github.com/zsh-users/zsh-syntax-highlighting

## Meta
- **Stars:** ⭐ 22416 | **Forks:** 🍴 1368
- **Language:** Shell | **License:** BSD-3-Clause
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Fish shell like syntax highlighting for Zsh.

## README (trích đầu)
```
zsh-syntax-highlighting [![Build Status][build-status-image]][build-status]
=======================

**[Fish shell][fish]-like syntax highlighting for [Zsh][zsh].**

*Requirements: zsh 4.3.11+.*

[fish]: https://fishshell.com/
[zsh]: https://www.zsh.org/

This package provides syntax highlighting for the shell zsh.  It enables
highlighting of commands whilst they are typed at a zsh prompt into an
interactive terminal.  This helps in reviewing commands before running
them, particularly in catching syntax errors.

Some examples:

Before: [![Screenshot #1.1](images/before1-smaller.png)](images/before1.png)
<br/>
After:&nbsp; [![Screenshot #1.2](images/after1-smaller.png)](images/after1.png)

Before: [![Screenshot #2.1](images/before2-smaller.png)](images/before2.png)
<br/>
After:&nbsp; [![Screenshot #2.2](images/after2-smaller.png)](images/after2.png)

Before: [![Screenshot #3.1](images/before3-smaller.png)](images/before3.png)
<br/>
After:&nbsp; [![Screenshot #3.2](images/after3-smaller.png)](images/after3.png)

Before: [![Screenshot #4.1](images/before4-smaller.png)](images/before4-smaller.png)
<br/>
After:&nbsp; [![Screenshot #4.2](images/after4-smaller.png)](images/after4-smaller.png)



How to install
--------------

See [INSTALL.md](INSTALL.md).


FAQ
---

### Why must `zsh-syntax-highlighting.zsh` be sourced at the end of the `.zshrc` file?

zsh-syntax-highlighting works by hooking into the Zsh Line Editor (ZLE) and
computing syntax highlighting for the command-line buffer as it stands at the
time z-sy-h's hook is invoked.

In zsh 5.2 and older,
`zsh-syntax-highlighting.zsh` hooks into ZLE by wrapping ZLE widgets.  It must
be sourced after all custom widgets have been created (i.e., after all `zle -N`
calls and after running `compinit`) in order to be able to wrap all of them.
Widgets created after z-sy-h is sourced will work, but will not update the
syntax highlighting.

In zsh newer than 5.8 (not including 5.8 itself),
zsh-syntax-highlighting uses the `add-zle-hook-widget` facility to install
a `zle-line-pre-redraw` hook.  Hooks are run in order of registration,
therefore, z-sy-h must be sourced (and register its hook) after anything else
that adds hooks that modify the command-line buffer.

### Does syntax highlighting work during incremental history search?

Highlighting the command line during an incremental history search (by default bound to
to <kbd>Ctrl+R</kbd> in zsh's emacs keymap) requires zsh 5.4 or newer.

Under zsh versions older than 5.4, the zsh-default [underlining][zshzle-Character-Highlighting]
of the matched portion of the buffer remains available, but zsh-syntax-highlighting's
additional highlighting is unavailable.  (Those versions of zsh do not provide
enough information to allow computing the highlighting correctly.)

See issues [#288][i288] and [#415][i415] for details.

[zshzle-Character-Highlighting]: https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Character-Highlighting
[i288]: https://github.com/zsh-us
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

