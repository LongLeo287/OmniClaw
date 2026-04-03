---
id: zsh-autosuggestions-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.943400
---

# KNOWLEDGE EXTRACT: zsh-autosuggestions
> **Extracted on:** 2026-03-30 18:01:28
> **Source:** zsh-autosuggestions

---

## File: `.editorconfig`
```
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = tab
indent_size = 4

[*.md]
indent_style = space

[*.rb]
indent_style = space
indent_size = 2

[*.yml]
indent_style = space
indent_size = 2
```

## File: `.gitignore`
```
# zsh word code files
*.zwc
```

## File: `.rspec`
```
--color
--require spec_helper
--format documentation
```

## File: `.rubocop.yml`
```yaml
# Rails:
#   Enabled: true

AllCops:
  TargetRubyVersion: 2.3
  Include:
    - '**/Rakefile'
    - '**/config.ru'
    - '**/Gemfile'

Metrics/LineLength:
  Max: 120

Style/Documentation:
  Enabled: false

Style/DotPosition:
  EnforcedStyle: trailing

Style/FrozenStringLiteralComment:
  Enabled: false

Style/Lambda:
  Enabled: false

Style/MultilineMethodCallIndentation:
  EnforcedStyle: indented

Style/TrailingUnderscoreVariable:
  Enabled: false
```

## File: `.ruby-version`
```
2.5.3
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## v0.7.1
- Clear POSTDISPLAY instead of unsetting (#634)
- Always reset async file descriptor after consuming it (#630)
- Always use builtin `exec` (#628)
- Add `history-beginning-search-*-end` widgets to clear widget list (#619)
- Switch CI from Circle CI to GitHub Actions

## v0.7.0
- Enable asynchronous mode by default (#498)
- No longer wrap user widgets starting with `autosuggest-` prefix (#496)
- Fix a bug wrapping widgets that modify the buffer (#541)


## v0.6.4
- Fix `vi-forward-char` triggering a bell when using it to accept a suggestion (#488)
- New configuration option to skip completion suggestions when buffer matches a pattern (#487)
- New configuration option to ignore history entries matching a pattern (#456)

## v0.6.3
- Fixed bug moving cursor to end of buffer after accepting suggestion (#453)

## v0.6.2
- Fixed bug deleting the last character in the buffer in vi mode (#450)
- Degrade gracefully when user doesn't have `zsh/system` module installed (#447)

## v0.6.1
- Fixed bug occurring when `_complete` had been aliased (#443)

## v0.6.0
- Added `completion` suggestion strategy powered by completion system (#111)
- Allow setting `ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE` to an empty string (#422)
- Don't fetch suggestions after copy-earlier-word (#439)
- Allow users to unignore zle-\* widgets (e.g. zle-line-init) (#432)


## v0.5.2
- Allow disabling automatic widget re-binding for better performance (#418)
- Fix async suggestions when `SH_WORD_SPLIT` is set
- Refactor async mode to use process substitution instead of zpty (#417)

## v0.5.1
- Speed up widget rebinding (#413)
- Clean up global variable creations (#403)
- Respect user's set options when running original widget (#402)

## v0.5.0
- Don't overwrite config with default values (#335)
- Support fallback strategies by supplying array to suggestion config var
- Rename "default" suggestion strategy to "history" to name it based on what it actually does
- Reset opts in some functions affected by `GLOB_SUBST` (#334)
- Support widgets starting with dashes (ex: `-a-widget`) (#337)
- Skip async tests in zsh versions less than 5.0.8 because of reliability issues
- Fix handling of newline + carriage return in async pty (#333)


## v0.4.3
- Avoid bell when accepting suggestions with `autosuggest-accept` (#228)
- Don't fetch suggestions after [up,down]-line-or-beginning-search (#227, #241)
- We are now running CI against new 5.5.1 version
- Fix partial-accept in vi mode (#188)
- Fix suggestion disappearing on fast movement after switching to `vicmd` mode (#290)
- Fix issue rotating through kill ring with `yank-pop` (#301)
- Fix issue creating new pty for async mode when previous pty is not properly cleaned up (#249)

## v0.4.2
- Fix bug in zsh versions older than 5.0.8 (#296)
- Officially support back to zsh v4.3.11

## v0.4.1
- Switch to [[ and (( conditionals instead of [ (#257)
- Avoid warnnestedvar warnings with `typeset -g` (#275)
- Replace tabs with spaces in yaml (#268)
- Clean up and fix escaping of special characters (#267)
- Add `emacs-forward-word` to default list of partial accept widgets (#246)

## v0.4.0
- High-level integration tests using RSpec and tmux
- Add continuous integration with Circle CI
- Experimental support for asynchronous suggestions (#170)
- Fix problems with multi-line suggestions (#225)
- Optimize case where manually typing in suggestion
- Avoid wrapping any zle-\* widgets (#206)
- Remove support for deprecated options from v0.0.x
- Handle history entries that begin with dashes
- Gracefully handle being sourced multiple times (#126)
- Add enable/disable/toggle widgets to disable/enable suggestions (#219)


## v0.3.3
- Switch from $history array to fc builtin for better performance with large HISTFILEs (#164)
- Fix tilde handling when extended_glob is set (#168)
- Add config option for maximum buffer length to fetch suggestions for (#178)
- Add config option for list of widgets to ignore (#184)
- Don't fetch a new suggestion unless a modification widget actually modifies the buffer (#183)

## v0.3.2
- Test runner now supports running specific tests and choosing zsh binary
- Return code from original widget is now correctly passed through (#135)
- Add `vi-add-eol` to list of accept widgets (#143)
- Escapes widget names within evals to fix problems with irregular widget names (#152)
- Plugin now clears suggestion while within a completion menu (#149)
- .plugin file no longer relies on symbolic link support, fixing issues on Windows (#156)

## v0.3.1

- Fixes issue with `vi-next-char` not accepting suggestion (#137).
- Fixes global variable warning when WARN_CREATE_GLOBAL option enabled (#133).
- Split out a separate test file for each widget.

## v0.3.0

- Adds `autosuggest-execute` widget (PR #124).
- Adds concept of suggestion "strategies" for different ways of fetching suggestions.
- Adds "match_prev_cmd" strategy (PR #131).
- Uses git submodules for testing dependencies.
- Lots of test cleanup.
- Various bug fixes for zsh 5.0.x and `sh_word_split` option.


## v0.2.17

Start of changelog.
```

## File: `DESCRIPTION`
```
Fish-like fast/unobtrusive autosuggestions for zsh.
```

## File: `Dockerfile`
```
FROM ruby:2.5.3-alpine

ARG TEST_ZSH_VERSION
RUN : "${TEST_ZSH_VERSION:?}"

RUN apk add --no-cache autoconf
RUN apk add --no-cache libtool
RUN apk add --no-cache libcap-dev
RUN apk add --no-cache pcre-dev
RUN apk add --no-cache curl
RUN apk add --no-cache build-base
RUN apk add --no-cache ncurses-dev
RUN apk add --no-cache tmux

WORKDIR /zsh-autosuggestions

ADD install_test_zsh.sh ./
RUN ./install_test_zsh.sh

ADD Gemfile Gemfile.lock ./
RUN bundle install
```

## File: `Gemfile`
```
source 'https://rubygems.org'

gem 'rspec'
gem 'rspec-wait'
gem 'pry-byebug'
```

## File: `Gemfile.lock`
```
GEM
  remote: https://rubygems.org/
  specs:
    byebug (9.0.5)
    coderay (1.1.1)
    diff-lcs (1.3)
    method_source (0.8.2)
    pry (0.10.4)
      coderay (~> 1.1.0)
      method_source (~> 0.8.1)
      slop (~> 3.4)
    pry-byebug (3.4.0)
      byebug (~> 9.0)
      pry (~> 0.10)
    rspec (3.5.0)
      rspec-core (~> 3.5.0)
      rspec-expectations (~> 3.5.0)
      rspec-mocks (~> 3.5.0)
    rspec-core (3.5.4)
      rspec-support (~> 3.5.0)
    rspec-expectations (3.5.0)
      diff-lcs (>= 1.2.0, < 2.0)
      rspec-support (~> 3.5.0)
    rspec-mocks (3.5.0)
      diff-lcs (>= 1.2.0, < 2.0)
      rspec-support (~> 3.5.0)
    rspec-support (3.5.0)
    rspec-wait (0.0.9)
      rspec (>= 3, < 4)
    slop (3.6.0)

PLATFORMS
  ruby

DEPENDENCIES
  pry-byebug
  rspec
  rspec-wait

BUNDLED WITH
   1.13.6
```

## File: `INSTALL.md`
```markdown
# Installation

* [Packages](#packages)
* [Antigen](#antigen)
* [Oh My Zsh](#oh-my-zsh)
* [HomeBrew](#homebrew)
* [Manual](#manual-git-clone)

## Packages

| System  | Package |
| ------------- | ------------- |
| Alpine Linux | [zsh-autosuggestions](https://pkgs.alpinelinux.org/packages?name=zsh-autosuggestions) |
| Debian / Ubuntu | [zsh-autosuggestions OBS repository](https://software.opensuse.org/download.html?project=shells%3Azsh-users%3Azsh-autosuggestions&package=zsh-autosuggestions) |
| Fedora / CentOS / RHEL / Scientific Linux | [zsh-autosuggestions OBS repository](https://software.opensuse.org/download.html?project=shells%3Azsh-users%3Azsh-autosuggestions&package=zsh-autosuggestions) |
| OpenSUSE / SLE | [zsh-autosuggestions OBS repository](https://software.opensuse.org/download.html?project=shells%3Azsh-users%3Azsh-autosuggestions&package=zsh-autosuggestions) |
| Arch Linux / Manjaro / Antergos / Hyperbola | [zsh-autosuggestions](https://www.archlinux.org/packages/zsh-autosuggestions), [zsh-autosuggestions-git](https://aur.archlinux.org/packages/zsh-autosuggestions-git) |
| NixOS | [zsh-autosuggestions](https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/zs/zsh-autosuggestions/package.nix) |
| Void Linux | [zsh-autosuggestions](https://github.com/void-linux/void-packages/blob/master/srcpkgs/zsh-autosuggestions/template) |
| Mac OS | [homebrew](https://formulae.brew.sh/formula/zsh-autosuggestions)  |
| NetBSD | [pkgsrc](http://ftp.netbsd.org/pub/pkgsrc/current/pkgsrc/shells/zsh-autosuggestions/README.html)  |
| FreeBSD | [pkg](https://cgit.freebsd.org/ports/tree/shells/zsh-autosuggestions) |

## Antigen

1. Add the following to your `.zshrc`:

    ```sh
    antigen bundle zsh-users/zsh-autosuggestions
    ```

2. Start a new terminal session.

## Oh My Zsh

1. Clone this repository into `$ZSH_CUSTOM/plugins` (by default `~/.oh-my-zsh/custom/plugins`)

    ```sh
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```

2. Add the plugin to the list of plugins for Oh My Zsh to load (inside `~/.zshrc`):

    ```sh
    plugins=( 
        # other plugins...
        zsh-autosuggestions
    )
    ```

3. Start a new terminal session.

## Homebrew

1. Install command: 
    ```sh
    brew install zsh-autosuggestions
    ```

2. To activate the autosuggestions, add the following at the end of your .zshrc: 
    
    ```sh
    source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
    ```

3. Start a new terminal session.

## Manual (Git Clone)

1. Clone this repository somewhere on your machine. This guide will assume `~/.zsh/zsh-autosuggestions`.

    ```sh
    git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
    ```

2. Add the following to your `.zshrc`:

    ```sh
    source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
    ```

3. Start a new terminal session.
```

## File: `install_test_zsh.sh`
```bash
#!/bin/sh

set -ex

mkdir zsh-build
cd zsh-build

curl -L https://api.github.com/repos/zsh-users/zsh/tarball/zsh-$TEST_ZSH_VERSION | tar xz --strip=1

./Util/preconfig
./configure --enable-pcre \
            --enable-cap \
            --enable-multibyte \
            --with-term-lib='ncursesw tinfo' \
            --with-tcsetpgrp

make install.bin
make install.modules
make install.fns

cd ..

rm -rf zsh-build
```

## File: `LICENSE`
```
Copyright (c) 2013 Thiago de Arruda
Copyright (c) 2016-2021 Eric Freese

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```

## File: `Makefile`
```
SRC_DIR := ./src

SRC_FILES := \
	$(SRC_DIR)/config.zsh \
	$(SRC_DIR)/util.zsh \
	$(SRC_DIR)/bind.zsh \
	$(SRC_DIR)/highlight.zsh \
	$(SRC_DIR)/widgets.zsh \
	$(SRC_DIR)/strategies/*.zsh \
	$(SRC_DIR)/fetch.zsh \
	$(SRC_DIR)/async.zsh \
	$(SRC_DIR)/start.zsh

HEADER_FILES := \
	DESCRIPTION \
	URL \
	VERSION \
	LICENSE

PLUGIN_TARGET := zsh-autosuggestions.zsh

all: $(PLUGIN_TARGET)

$(PLUGIN_TARGET): $(HEADER_FILES) $(SRC_FILES)
	cat $(HEADER_FILES) | sed -e 's/^/# /g' > $@
	cat $(SRC_FILES) >> $@

.PHONY: clean
clean:
	rm $(PLUGIN_TARGET)

.PHONY: test
test: all
	@test -n "$$TEST_ZSH_BIN" && echo "Testing zsh binary: $(TEST_ZSH_BIN)" || true
	bundle exec rspec $(TESTS)
```

## File: `README.md`
```markdown
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

`ZSH_AUTOSUGGEST_STRATEGY` is an array that specifies how suggestions should be generated. The strategies in the array are tried successively until a suggestion is found. There are currently three built-in strategies to choose from:

- `history`: Chooses the most recent match from history.
- `completion`: Chooses a suggestion based on what tab-completion would suggest. (requires `zpty` module, which is included with zsh since 4.0.1)
- `match_prev_cmd`: Like `history`, but chooses the most recent match whose preceding history item matches the most recently executed command ([more info](src/strategies/match_prev_cmd.zsh)). Note that this strategy won't work as expected with ZSH options that don't preserve the history order such as `HIST_IGNORE_ALL_DUPS` or `HIST_EXPIRE_DUPS_FIRST`.

For example, setting `ZSH_AUTOSUGGEST_STRATEGY=(history completion)` will first try to find a suggestion from your history, but, if it can't find a match, will find a suggestion from the completion engine.


### Widget Mapping

This plugin works by triggering custom behavior when certain [zle widgets](http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html#Zle-Widgets) are invoked. You can add and remove widgets from these arrays to change the behavior of this plugin:

- `ZSH_AUTOSUGGEST_CLEAR_WIDGETS`: Widgets in this array will clear the suggestion when invoked.
- `ZSH_AUTOSUGGEST_ACCEPT_WIDGETS`: Widgets in this array will accept the suggestion when invoked.
- `ZSH_AUTOSUGGEST_EXECUTE_WIDGETS`: Widgets in this array will execute the suggestion when invoked.
- `ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS`: Widgets in this array will partially accept the suggestion when invoked.
- `ZSH_AUTOSUGGEST_IGNORE_WIDGETS`: Widgets in this array will not trigger any custom behavior.

Widgets that modify the buffer and are not found in any of these arrays will fetch a new suggestion after they are invoked.

**Note:** A widget shouldn't belong to more than one of the above arrays.


### Disabling suggestion for large buffers

Set `ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE` to an integer value to disable autosuggestion for large buffers. The default is unset, which means that autosuggestion will be tried for any buffer size. Recommended value is 20.
This can be useful when pasting large amount of text in the terminal, to avoid triggering autosuggestion for strings that are too long.

### Asynchronous Mode

Suggestions are fetched asynchronously by default in zsh versions 5.0.8 and greater. To disable asynchronous suggestions and fetch them synchronously instead, `unset ZSH_AUTOSUGGEST_USE_ASYNC` after sourcing the plugin.

Alternatively, if you are using a version of zsh older than 5.0.8 and want to enable asynchronous mode, set the `ZSH_AUTOSUGGEST_USE_ASYNC` variable after sourcing the plugin (it can be set to anything). Note that there is [a bug](https://github.com/zsh-users/zsh-autosuggestions/issues/364#issuecomment-481423232) in versions of zsh older than 5.0.8 where <kbd>ctrl</kbd> + <kbd>c</kbd> will fail to reset the prompt immediately after fetching a suggestion asynchronously.

### Disabling automatic widget re-binding

Set `ZSH_AUTOSUGGEST_MANUAL_REBIND` (it can be set to anything) to disable automatic widget re-binding on each precmd. This can be a big boost to performance, but you'll need to handle re-binding yourself if any of the widget lists change or if you or another plugin wrap any of the autosuggest widgets. To re-bind widgets, run `_zsh_autosuggest_bind_widgets`.

### Ignoring history suggestions that match a pattern

Set `ZSH_AUTOSUGGEST_HISTORY_IGNORE` to a [glob pattern](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Glob-Operators) to prevent offering suggestions for history entries that match the pattern. For example, set it to `"cd *"` to never suggest any `cd` commands from history. Or set to `"?(#c50,)"` to never suggest anything 50 characters or longer.

**Note:** This only affects the `history` and `match_prev_cmd` suggestion strategies.

### Skipping completion suggestions for certain cases

Set `ZSH_AUTOSUGGEST_COMPLETION_IGNORE` to a [glob pattern](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Glob-Operators) to prevent offering completion suggestions when the buffer matches that pattern. For example, set it to `"git *"` to disable completion suggestions for git subcommands.

**Note:** This only affects the `completion` suggestion strategy.


### Key Bindings

This plugin provides a few widgets that you can use with `bindkey`:

1. `autosuggest-accept`: Accepts the current suggestion.
2. `autosuggest-execute`: Accepts and executes the current suggestion.
3. `autosuggest-clear`: Clears the current suggestion.
4. `autosuggest-fetch`: Fetches a suggestion (works even when suggestions are disabled).
5. `autosuggest-disable`: Disables suggestions.
6. `autosuggest-enable`: Re-enables suggestions.
7. `autosuggest-toggle`: Toggles between enabled/disabled suggestions.

For example, this would bind <kbd>ctrl</kbd> + <kbd>space</kbd> to accept the current suggestion.

```sh
bindkey '^ ' autosuggest-accept
```


## Troubleshooting

If you have a problem, please search through [the list of issues on GitHub](https://github.com/zsh-users/zsh-autosuggestions/issues?q=) to see if someone else has already reported it.

### Reporting an Issue

Before reporting an issue, please try temporarily disabling sections of your configuration and other plugins that may be conflicting with this plugin to isolate the problem.

When reporting an issue, please include:

- The smallest, simplest `.zshrc` configuration that will reproduce the problem. See [this comment](https://github.com/zsh-users/zsh-autosuggestions/issues/102#issuecomment-180944764) for a good example of what this means.
- The version of zsh you're using (`zsh --version`)
- Which operating system you're running


## Uninstallation

1. Remove the code referencing this plugin from `~/.zshrc`.

2. Remove the git repository from your hard drive

    ```sh
    rm -rf ~/.zsh/zsh-autosuggestions # Or wherever you installed
    ```


## Development

### Build Process

Edit the source files in `src/`. Run `make` to build `zsh-autosuggestions.zsh` from those source files.


### Pull Requests

Pull requests are welcome! If you send a pull request, please:

- Request to merge into the `develop` branch (*NOT* `master`)
- Match the existing coding conventions.
- Include helpful comments to keep the barrier-to-entry low for people new to the project.
- Write tests that cover your code as much as possible.


### Testing

Tests are written in ruby using the [`rspec`](http://rspec.info/) framework. They use [`tmux`](https://tmux.github.io/) to drive a pseudoterminal, sending simulated keystrokes and making assertions on the terminal content.

Test files live in `spec/`. To run the tests, run `make test`. To run a specific test, run `TESTS=spec/some_spec.rb make test`. You can also specify a `zsh` binary to use by setting the `TEST_ZSH_BIN` environment variable (ex: `TEST_ZSH_BIN=/bin/zsh make test`).

It's possible to run the tests for any supported version of zsh in a Docker image by building an image from the provided Dockerfile. To build the docker image for a specific version of zsh (where `<version>` below is substituted with the contents of a line from the [`ZSH_VERSIONS`](ZSH_VERSIONS) file), run:

```sh
docker build --build-arg TEST_ZSH_VERSION=<version> -t zsh-autosuggestions-test .
```

After building the image, run the tests via:

```sh
docker run -it -v $PWD:/zsh-autosuggestions zsh-autosuggestions-test make test
```


## License

This project is licensed under [MIT license](http://opensource.org/licenses/MIT).
For the full text of the license, see the [LICENSE](LICENSE) file.
```

## File: `URL`
```
https://github.com/zsh-users/zsh-autosuggestions
```

## File: `VERSION`
```
v0.7.1
```

## File: `zsh-autosuggestions.plugin.zsh`
```
source ${0:A:h}/zsh-autosuggestions.zsh
```

## File: `zsh-autosuggestions.zsh`
```
# Fish-like fast/unobtrusive autosuggestions for zsh.
# https://github.com/zsh-users/zsh-autosuggestions
# v0.7.1
# Copyright (c) 2013 Thiago de Arruda
# Copyright (c) 2016-2021 Eric Freese
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

#--------------------------------------------------------------------#
# Global Configuration Variables                                     #
#--------------------------------------------------------------------#

# Color to use when highlighting suggestion
# Uses format of `region_highlight`
# More info: http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html#Zle-Widgets
(( ! ${+ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE} )) &&
typeset -g ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'

# Prefix to use when saving original versions of bound widgets
(( ! ${+ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX} )) &&
typeset -g ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX=autosuggest-orig-

# Strategies to use to fetch a suggestion
# Will try each strategy in order until a suggestion is returned
(( ! ${+ZSH_AUTOSUGGEST_STRATEGY} )) && {
	typeset -ga ZSH_AUTOSUGGEST_STRATEGY
	ZSH_AUTOSUGGEST_STRATEGY=(history)
}

# Widgets that clear the suggestion
(( ! ${+ZSH_AUTOSUGGEST_CLEAR_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_CLEAR_WIDGETS
	ZSH_AUTOSUGGEST_CLEAR_WIDGETS=(
		history-search-forward
		history-search-backward
		history-beginning-search-forward
		history-beginning-search-backward
		history-beginning-search-forward-end
		history-beginning-search-backward-end
		history-substring-search-up
		history-substring-search-down
		up-line-or-beginning-search
		down-line-or-beginning-search
		up-line-or-history
		down-line-or-history
		accept-line
		copy-earlier-word
	)
}

# Widgets that accept the entire suggestion
(( ! ${+ZSH_AUTOSUGGEST_ACCEPT_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_ACCEPT_WIDGETS
	ZSH_AUTOSUGGEST_ACCEPT_WIDGETS=(
		forward-char
		end-of-line
		vi-forward-char
		vi-end-of-line
		vi-add-eol
	)
}

# Widgets that accept the entire suggestion and execute it
(( ! ${+ZSH_AUTOSUGGEST_EXECUTE_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_EXECUTE_WIDGETS
	ZSH_AUTOSUGGEST_EXECUTE_WIDGETS=(
	)
}

# Widgets that accept the suggestion as far as the cursor moves
(( ! ${+ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS
	ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS=(
		forward-word
		emacs-forward-word
		vi-forward-word
		vi-forward-word-end
		vi-forward-blank-word
		vi-forward-blank-word-end
		vi-find-next-char
		vi-find-next-char-skip
	)
}

# Widgets that should be ignored (globbing supported but must be escaped)
(( ! ${+ZSH_AUTOSUGGEST_IGNORE_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_IGNORE_WIDGETS
	ZSH_AUTOSUGGEST_IGNORE_WIDGETS=(
		orig-\*
		beep
		run-help
		set-local-history
		which-command
		yank
		yank-pop
		zle-\*
	)
}

# Pty name for capturing completions for completion suggestion strategy
(( ! ${+ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME} )) &&
typeset -g ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME=zsh_autosuggest_completion_pty

#--------------------------------------------------------------------#
# Utility Functions                                                  #
#--------------------------------------------------------------------#

_zsh_autosuggest_escape_command() {
	setopt localoptions EXTENDED_GLOB

	# Escape special chars in the string (requires EXTENDED_GLOB)
	echo -E "${1//(#m)[\"\'\\()\[\]|*?~]/\\$MATCH}"
}

#--------------------------------------------------------------------#
# Widget Helpers                                                     #
#--------------------------------------------------------------------#

_zsh_autosuggest_incr_bind_count() {
	typeset -gi bind_count=$((_ZSH_AUTOSUGGEST_BIND_COUNTS[$1]+1))
	_ZSH_AUTOSUGGEST_BIND_COUNTS[$1]=$bind_count
}

# Bind a single widget to an autosuggest widget, saving a reference to the original widget
_zsh_autosuggest_bind_widget() {
	typeset -gA _ZSH_AUTOSUGGEST_BIND_COUNTS

	local widget=$1
	local autosuggest_action=$2
	local prefix=$ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX

	local -i bind_count

	# Save a reference to the original widget
	case $widgets[$widget] in
		# Already bound
		user:_zsh_autosuggest_(bound|orig)_*)
			bind_count=$((_ZSH_AUTOSUGGEST_BIND_COUNTS[$widget]))
			;;

		# User-defined widget
		user:*)
			_zsh_autosuggest_incr_bind_count $widget
			zle -N $prefix$bind_count-$widget ${widgets[$widget]#*:}
			;;

		# Built-in widget
		builtin)
			_zsh_autosuggest_incr_bind_count $widget
			eval "_zsh_autosuggest_orig_${(q)widget}() { zle .${(q)widget} }"
			zle -N $prefix$bind_count-$widget _zsh_autosuggest_orig_$widget
			;;

		# Completion widget
		completion:*)
			_zsh_autosuggest_incr_bind_count $widget
			eval "zle -C $prefix$bind_count-${(q)widget} ${${(s.:.)widgets[$widget]}[2,3]}"
			;;
	esac

	# Pass the original widget's name explicitly into the autosuggest
	# function. Use this passed in widget name to call the original
	# widget instead of relying on the $WIDGET variable being set
	# correctly. $WIDGET cannot be trusted because other plugins call
	# zle without the `-w` flag (e.g. `zle self-insert` instead of
	# `zle self-insert -w`).
	eval "_zsh_autosuggest_bound_${bind_count}_${(q)widget}() {
		_zsh_autosuggest_widget_$autosuggest_action $prefix$bind_count-${(q)widget} \$@
	}"

	# Create the bound widget
	zle -N -- $widget _zsh_autosuggest_bound_${bind_count}_$widget
}

# Map all configured widgets to the right autosuggest widgets
_zsh_autosuggest_bind_widgets() {
	emulate -L zsh

 	local widget
	local ignore_widgets

	ignore_widgets=(
		.\*
		_\*
		${_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS/#/autosuggest-}
		$ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX\*
		$ZSH_AUTOSUGGEST_IGNORE_WIDGETS
	)

	# Find every widget we might want to bind and bind it appropriately
	for widget in ${${(f)"$(builtin zle -la)"}:#${(j:|:)~ignore_widgets}}; do
		if [[ -n ${ZSH_AUTOSUGGEST_CLEAR_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget clear
		elif [[ -n ${ZSH_AUTOSUGGEST_ACCEPT_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget accept
		elif [[ -n ${ZSH_AUTOSUGGEST_EXECUTE_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget execute
		elif [[ -n ${ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget partial_accept
		else
			# Assume any unspecified widget might modify the buffer
			_zsh_autosuggest_bind_widget $widget modify
		fi
	done
}

# Given the name of an original widget and args, invoke it, if it exists
_zsh_autosuggest_invoke_original_widget() {
	# Do nothing unless called with at least one arg
	(( $# )) || return 0

	local original_widget_name="$1"

	shift

	if (( ${+widgets[$original_widget_name]} )); then
		zle $original_widget_name -- $@
	fi
}

#--------------------------------------------------------------------#
# Highlighting                                                       #
#--------------------------------------------------------------------#

# If there was a highlight, remove it
_zsh_autosuggest_highlight_reset() {
	typeset -g _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT

	if [[ -n "$_ZSH_AUTOSUGGEST_LAST_HIGHLIGHT" ]]; then
		region_highlight=("${(@)region_highlight:#$_ZSH_AUTOSUGGEST_LAST_HIGHLIGHT}")
		unset _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT
	fi
}

# If there's a suggestion, highlight it
_zsh_autosuggest_highlight_apply() {
	typeset -g _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT

	if (( $#POSTDISPLAY )); then
		typeset -g _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT="$#BUFFER $(($#BUFFER + $#POSTDISPLAY)) $ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE"
		region_highlight+=("$_ZSH_AUTOSUGGEST_LAST_HIGHLIGHT")
	else
		unset _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT
	fi
}

#--------------------------------------------------------------------#
# Autosuggest Widget Implementations                                 #
#--------------------------------------------------------------------#

# Disable suggestions
_zsh_autosuggest_disable() {
	typeset -g _ZSH_AUTOSUGGEST_DISABLED
	_zsh_autosuggest_clear
}

# Enable suggestions
_zsh_autosuggest_enable() {
	unset _ZSH_AUTOSUGGEST_DISABLED

	if (( $#BUFFER )); then
		_zsh_autosuggest_fetch
	fi
}

# Toggle suggestions (enable/disable)
_zsh_autosuggest_toggle() {
	if (( ${+_ZSH_AUTOSUGGEST_DISABLED} )); then
		_zsh_autosuggest_enable
	else
		_zsh_autosuggest_disable
	fi
}

# Clear the suggestion
_zsh_autosuggest_clear() {
	# Remove the suggestion
	POSTDISPLAY=

	_zsh_autosuggest_invoke_original_widget $@
}

# Modify the buffer and get a new suggestion
_zsh_autosuggest_modify() {
	local -i retval

	# Only available in zsh >= 5.4
	local -i KEYS_QUEUED_COUNT

	# Save the contents of the buffer/postdisplay
	local orig_buffer="$BUFFER"
	local orig_postdisplay="$POSTDISPLAY"

	# Clear suggestion while waiting for next one
	POSTDISPLAY=

	# Original widget may modify the buffer
	_zsh_autosuggest_invoke_original_widget $@
	retval=$?

	emulate -L zsh

	# Don't fetch a new suggestion if there's more input to be read immediately
	if (( $PENDING > 0 || $KEYS_QUEUED_COUNT > 0 )); then
		POSTDISPLAY="$orig_postdisplay"
		return $retval
	fi

	# Optimize if manually typing in the suggestion or if buffer hasn't changed
	if [[ "$BUFFER" = "$orig_buffer"* && "$orig_postdisplay" = "${BUFFER:$#orig_buffer}"* ]]; then
		POSTDISPLAY="${orig_postdisplay:$(($#BUFFER - $#orig_buffer))}"
		return $retval
	fi

	# Bail out if suggestions are disabled
	if (( ${+_ZSH_AUTOSUGGEST_DISABLED} )); then
		return $?
	fi

	# Get a new suggestion if the buffer is not empty after modification
	if (( $#BUFFER > 0 )); then
		if [[ -z "$ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE" ]] || (( $#BUFFER <= $ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE )); then
			_zsh_autosuggest_fetch
		fi
	fi

	return $retval
}

# Fetch a new suggestion based on what's currently in the buffer
_zsh_autosuggest_fetch() {
	if (( ${+ZSH_AUTOSUGGEST_USE_ASYNC} )); then
		_zsh_autosuggest_async_request "$BUFFER"
	else
		local suggestion
		_zsh_autosuggest_fetch_suggestion "$BUFFER"
		_zsh_autosuggest_suggest "$suggestion"
	fi
}

# Offer a suggestion
_zsh_autosuggest_suggest() {
	emulate -L zsh

	local suggestion="$1"

	if [[ -n "$suggestion" ]] && (( $#BUFFER )); then
		POSTDISPLAY="${suggestion#$BUFFER}"
	else
		POSTDISPLAY=
	fi
}

# Accept the entire suggestion
_zsh_autosuggest_accept() {
	local -i retval max_cursor_pos=$#BUFFER

	# When vicmd keymap is active, the cursor can't move all the way
	# to the end of the buffer
	if [[ "$KEYMAP" = "vicmd" ]]; then
		max_cursor_pos=$((max_cursor_pos - 1))
	fi

	# If we're not in a valid state to accept a suggestion, just run the
	# original widget and bail out
	if (( $CURSOR != $max_cursor_pos || !$#POSTDISPLAY )); then
		_zsh_autosuggest_invoke_original_widget $@
		return
	fi

	# Only accept if the cursor is at the end of the buffer
	# Add the suggestion to the buffer
	BUFFER="$BUFFER$POSTDISPLAY"

	# Remove the suggestion
	POSTDISPLAY=

	# Run the original widget before manually moving the cursor so that the
	# cursor movement doesn't make the widget do something unexpected
	_zsh_autosuggest_invoke_original_widget $@
	retval=$?

	# Move the cursor to the end of the buffer
	if [[ "$KEYMAP" = "vicmd" ]]; then
		CURSOR=$(($#BUFFER - 1))
	else
		CURSOR=$#BUFFER
	fi

	return $retval
}

# Accept the entire suggestion and execute it
_zsh_autosuggest_execute() {
	# Add the suggestion to the buffer
	BUFFER="$BUFFER$POSTDISPLAY"

	# Remove the suggestion
	POSTDISPLAY=

	# Call the original `accept-line` to handle syntax highlighting or
	# other potential custom behavior
	_zsh_autosuggest_invoke_original_widget "accept-line"
}

# Partially accept the suggestion
_zsh_autosuggest_partial_accept() {
	local -i retval cursor_loc

	# Save the contents of the buffer so we can restore later if needed
	local original_buffer="$BUFFER"

	# Temporarily accept the suggestion.
	BUFFER="$BUFFER$POSTDISPLAY"

	# Original widget moves the cursor
	_zsh_autosuggest_invoke_original_widget $@
	retval=$?

	# Normalize cursor location across vi/emacs modes
	cursor_loc=$CURSOR
	if [[ "$KEYMAP" = "vicmd" ]]; then
		cursor_loc=$((cursor_loc + 1))
	fi

	# If we've moved past the end of the original buffer
	if (( $cursor_loc > $#original_buffer )); then
		# Set POSTDISPLAY to text right of the cursor
		POSTDISPLAY="${BUFFER[$(($cursor_loc + 1)),$#BUFFER]}"

		# Clip the buffer at the cursor
		BUFFER="${BUFFER[1,$cursor_loc]}"
	else
		# Restore the original buffer
		BUFFER="$original_buffer"
	fi

	return $retval
}

() {
	typeset -ga _ZSH_AUTOSUGGEST_BUILTIN_ACTIONS

	_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS=(
		clear
		fetch
		suggest
		accept
		execute
		enable
		disable
		toggle
	)

	local action
	for action in $_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS modify partial_accept; do
		eval "_zsh_autosuggest_widget_$action() {
			local -i retval

			_zsh_autosuggest_highlight_reset

			_zsh_autosuggest_$action \$@
			retval=\$?

			_zsh_autosuggest_highlight_apply

			zle -R

			return \$retval
		}"
	done

	for action in $_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS; do
		zle -N autosuggest-$action _zsh_autosuggest_widget_$action
	done
}

#--------------------------------------------------------------------#
# Completion Suggestion Strategy                                     #
#--------------------------------------------------------------------#
# Fetches a suggestion from the completion engine
#

_zsh_autosuggest_capture_postcompletion() {
	# Always insert the first completion into the buffer
	compstate[insert]=1

	# Don't list completions
	unset 'compstate[list]'
}

_zsh_autosuggest_capture_completion_widget() {
	# Add a post-completion hook to be called after all completions have been
	# gathered. The hook can modify compstate to affect what is done with the
	# gathered completions.
	local -a +h comppostfuncs
	comppostfuncs=(_zsh_autosuggest_capture_postcompletion)

	# Only capture completions at the end of the buffer
	CURSOR=$#BUFFER

	# Run the original widget wrapping `.complete-word` so we don't
	# recursively try to fetch suggestions, since our pty is forked
	# after autosuggestions is initialized.
	zle -- ${(k)widgets[(r)completion:.complete-word:_main_complete]}

	if is-at-least 5.0.3; then
		# Don't do any cr/lf transformations. We need to do this immediately before
		# output because if we do it in setup, onlcr will be re-enabled when we enter
		# vared in the async code path. There is a bug in zpty module in older versions
		# where the tty is not properly attached to the pty slave, resulting in stty
		# getting stopped with a SIGTTOU. See zsh-workers thread 31660 and upstream
		# commit f75904a38
		stty -onlcr -ocrnl -F /dev/tty
	fi

	# The completion has been added, print the buffer as the suggestion
	echo -nE - $'\0'$BUFFER$'\0'
}

zle -N autosuggest-capture-completion _zsh_autosuggest_capture_completion_widget

_zsh_autosuggest_capture_setup() {
	# There is a bug in zpty module in older zsh versions by which a
	# zpty that exits will kill all zpty processes that were forked
	# before it. Here we set up a zsh exit hook to SIGKILL the zpty
	# process immediately, before it has a chance to kill any other
	# zpty processes.
	if ! is-at-least 5.4; then
		zshexit() {
			# The zsh builtin `kill` fails sometimes in older versions
			# https://unix.stackexchange.com/a/477647/156673
			kill -KILL $$ 2>&- || command kill -KILL $$

			# Block for long enough for the signal to come through
			sleep 1
		}
	fi

	# Try to avoid any suggestions that wouldn't match the prefix
	zstyle ':completion:*' matcher-list ''
	zstyle ':completion:*' path-completion false
	zstyle ':completion:*' max-errors 0 not-numeric

	bindkey '^I' autosuggest-capture-completion
}

_zsh_autosuggest_capture_completion_sync() {
	_zsh_autosuggest_capture_setup

	zle autosuggest-capture-completion
}

_zsh_autosuggest_capture_completion_async() {
	_zsh_autosuggest_capture_setup

	zmodload zsh/parameter 2>/dev/null || return # For `$functions`

	# Make vared completion work as if for a normal command line
	# https://stackoverflow.com/a/7057118/154703
	autoload +X _complete
	functions[_original_complete]=$functions[_complete]
	function _complete() {
		unset 'compstate[vared]'
		_original_complete "$@"
	}

	# Open zle with buffer set so we can capture completions for it
	vared 1
}

_zsh_autosuggest_strategy_completion() {
	# Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable extended glob for completion ignore pattern
	setopt EXTENDED_GLOB

	typeset -g suggestion
	local line REPLY

	# Exit if we don't have completions
	whence compdef >/dev/null || return

	# Exit if we don't have zpty
	zmodload zsh/zpty 2>/dev/null || return

	# Exit if our search string matches the ignore pattern
	[[ -n "$ZSH_AUTOSUGGEST_COMPLETION_IGNORE" ]] && [[ "$1" == $~ZSH_AUTOSUGGEST_COMPLETION_IGNORE ]] && return

	# Zle will be inactive if we are in async mode
	if zle; then
		zpty $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME _zsh_autosuggest_capture_completion_sync
	else
		zpty $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME _zsh_autosuggest_capture_completion_async "\$1"
		zpty -w $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME $'\t'
	fi

	{
		# The completion result is surrounded by null bytes, so read the
		# content between the first two null bytes.
		zpty -r $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME line '*'$'\0''*'$'\0'

		# Extract the suggestion from between the null bytes.  On older
		# versions of zsh (older than 5.3), we sometimes get extra bytes after
		# the second null byte, so trim those off the end.
		# See http://www.zsh.org/mla/workers/2015/msg03290.html
		suggestion="${${(@0)line}[2]}"
	} always {
		# Destroy the pty
		zpty -d $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME
	}
}

#--------------------------------------------------------------------#
# History Suggestion Strategy                                        #
#--------------------------------------------------------------------#
# Suggests the most recent history item that matches the given
# prefix.
#

_zsh_autosuggest_strategy_history() {
	# Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable globbing flags so that we can use (#m) and (x~y) glob operator
	setopt EXTENDED_GLOB

	# Escape backslashes and all of the glob operators so we can use
	# this string as a pattern to search the $history associative array.
	# - (#m) globbing flag enables setting references for match data
	# TODO: Use (b) flag when we can drop support for zsh older than v5.0.8
	local prefix="${1//(#m)[\\*?[\]<>()|^~#]/\\$MATCH}"

	# Get the history items that match the prefix, excluding those that match
	# the ignore pattern
	local pattern="$prefix*"
	if [[ -n $ZSH_AUTOSUGGEST_HISTORY_IGNORE ]]; then
		pattern="($pattern)~($ZSH_AUTOSUGGEST_HISTORY_IGNORE)"
	fi

	# Give the first history item matching the pattern as the suggestion
	# - (r) subscript flag makes the pattern match on values
	typeset -g suggestion="${history[(r)$pattern]}"
}

#--------------------------------------------------------------------#
# Match Previous Command Suggestion Strategy                         #
#--------------------------------------------------------------------#
# Suggests the most recent history item that matches the given
# prefix and whose preceding history item also matches the most
# recently executed command.
#
# For example, suppose your history has the following entries:
#   - pwd
#   - ls foo
#   - ls bar
#   - pwd
#
# Given the history list above, when you type 'ls', the suggestion
# will be 'ls foo' rather than 'ls bar' because your most recently
# executed command (pwd) was previously followed by 'ls foo'.
#
# Note that this strategy won't work as expected with ZSH options that don't
# preserve the history order such as `HIST_IGNORE_ALL_DUPS` or
# `HIST_EXPIRE_DUPS_FIRST`.

_zsh_autosuggest_strategy_match_prev_cmd() {
	# Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable globbing flags so that we can use (#m) and (x~y) glob operator
	setopt EXTENDED_GLOB

	# TODO: Use (b) flag when we can drop support for zsh older than v5.0.8
	local prefix="${1//(#m)[\\*?[\]<>()|^~#]/\\$MATCH}"

	# Get the history items that match the prefix, excluding those that match
	# the ignore pattern
	local pattern="$prefix*"
	if [[ -n $ZSH_AUTOSUGGEST_HISTORY_IGNORE ]]; then
		pattern="($pattern)~($ZSH_AUTOSUGGEST_HISTORY_IGNORE)"
	fi

	# Get all history event numbers that correspond to history
	# entries that match the pattern
	local history_match_keys
	history_match_keys=(${(k)history[(R)$~pattern]})

	# By default we use the first history number (most recent history entry)
	local histkey="${history_match_keys[1]}"

	# Get the previously executed command
	local prev_cmd="$(_zsh_autosuggest_escape_command "${history[$((HISTCMD-1))]}")"

	# Iterate up to the first 200 history event numbers that match $prefix
	for key in "${(@)history_match_keys[1,200]}"; do
		# Stop if we ran out of history
		[[ $key -gt 1 ]] || break

		# See if the history entry preceding the suggestion matches the
		# previous command, and use it if it does
		if [[ "${history[$((key - 1))]}" == "$prev_cmd" ]]; then
			histkey="$key"
			break
		fi
	done

	# Give back the matched history entry
	typeset -g suggestion="$history[$histkey]"
}

#--------------------------------------------------------------------#
# Fetch Suggestion                                                   #
#--------------------------------------------------------------------#
# Loops through all specified strategies and returns a suggestion
# from the first strategy to provide one.
#

_zsh_autosuggest_fetch_suggestion() {
	typeset -g suggestion
	local -a strategies
	local strategy

	# Ensure we are working with an array
	strategies=(${=ZSH_AUTOSUGGEST_STRATEGY})

	for strategy in $strategies; do
		# Try to get a suggestion from this strategy
		_zsh_autosuggest_strategy_$strategy "$1"

		# Ensure the suggestion matches the prefix
		[[ "$suggestion" != "$1"* ]] && unset suggestion

		# Break once we've found a valid suggestion
		[[ -n "$suggestion" ]] && break
	done
}

#--------------------------------------------------------------------#
# Async                                                              #
#--------------------------------------------------------------------#

_zsh_autosuggest_async_request() {
	zmodload zsh/system 2>/dev/null # For `$sysparams`

	typeset -g _ZSH_AUTOSUGGEST_ASYNC_FD _ZSH_AUTOSUGGEST_CHILD_PID

	# If we've got a pending request, cancel it
	if [[ -n "$_ZSH_AUTOSUGGEST_ASYNC_FD" ]] && { true <&$_ZSH_AUTOSUGGEST_ASYNC_FD } 2>/dev/null; then
		# Close the file descriptor and remove the handler
		builtin exec {_ZSH_AUTOSUGGEST_ASYNC_FD}<&-
		zle -F $_ZSH_AUTOSUGGEST_ASYNC_FD

		# We won't know the pid unless the user has zsh/system module installed
		if [[ -n "$_ZSH_AUTOSUGGEST_CHILD_PID" ]]; then
			# Zsh will make a new process group for the child process only if job
			# control is enabled (MONITOR option)
			if [[ -o MONITOR ]]; then
				# Send the signal to the process group to kill any processes that may
				# have been forked by the suggestion strategy
				kill -TERM -$_ZSH_AUTOSUGGEST_CHILD_PID 2>/dev/null
			else
				# Kill just the child process since it wasn't placed in a new process
				# group. If the suggestion strategy forked any child processes they may
				# be orphaned and left behind.
				kill -TERM $_ZSH_AUTOSUGGEST_CHILD_PID 2>/dev/null
			fi
		fi
	fi

	# Fork a process to fetch a suggestion and open a pipe to read from it
	builtin exec {_ZSH_AUTOSUGGEST_ASYNC_FD}< <(
		# Tell parent process our pid
		echo $sysparams[pid]

		# Fetch and print the suggestion
		local suggestion
		_zsh_autosuggest_fetch_suggestion "$1"
		echo -nE "$suggestion"
	)

	# There's a weird bug here where ^C stops working unless we force a fork
	# See https://github.com/zsh-users/zsh-autosuggestions/issues/364
	autoload -Uz is-at-least
	is-at-least 5.8 || command true

	# Read the pid from the child process
	read _ZSH_AUTOSUGGEST_CHILD_PID <&$_ZSH_AUTOSUGGEST_ASYNC_FD

	# When the fd is readable, call the response handler
	zle -F "$_ZSH_AUTOSUGGEST_ASYNC_FD" _zsh_autosuggest_async_response
}

# Called when new data is ready to be read from the pipe
# First arg will be fd ready for reading
# Second arg will be passed in case of error
_zsh_autosuggest_async_response() {
	emulate -L zsh

	local suggestion

	if [[ -z "$2" || "$2" == "hup" ]]; then
		# Read everything from the fd and give it as a suggestion
		IFS='' read -rd '' -u $1 suggestion
		zle autosuggest-suggest -- "$suggestion"

		# Close the fd
		builtin exec {1}<&-
	fi

	# Always remove the handler
	zle -F "$1"
	_ZSH_AUTOSUGGEST_ASYNC_FD=
}

#--------------------------------------------------------------------#
# Start                                                              #
#--------------------------------------------------------------------#

# Start the autosuggestion widgets
_zsh_autosuggest_start() {
	# By default we re-bind widgets on every precmd to ensure we wrap other
	# wrappers. Specifically, highlighting breaks if our widgets are wrapped by
	# zsh-syntax-highlighting widgets. This also allows modifications to the
	# widget list variables to take effect on the next precmd. However this has
	# a decent performance hit, so users can set ZSH_AUTOSUGGEST_MANUAL_REBIND
	# to disable the automatic re-binding.
	if (( ${+ZSH_AUTOSUGGEST_MANUAL_REBIND} )); then
		add-zsh-hook -d precmd _zsh_autosuggest_start
	fi

	_zsh_autosuggest_bind_widgets
}

# Mark for auto-loading the functions that we use
autoload -Uz add-zsh-hook is-at-least

# Automatically enable asynchronous mode in newer versions of zsh. Disable for
# older versions because there is a bug when using async mode where ^C does not
# work immediately after fetching a suggestion.
# See https://github.com/zsh-users/zsh-autosuggestions/issues/364
if is-at-least 5.0.8; then
	typeset -g ZSH_AUTOSUGGEST_USE_ASYNC=
fi

# Start the autosuggestion widgets on the next precmd
add-zsh-hook precmd _zsh_autosuggest_start
```

## File: `ZSH_VERSIONS`
```
# Zsh releases to run tests against
# See https://github.com/zsh-users/zsh/releases
4.3.11
5.0.2
5.0.8
5.1.1
5.2
5.3.1
5.4.2
5.5.1
5.6.2
5.7.1
5.8.1
5.9
```

## File: `spec/async_spec.rb`
```ruby
context 'with asynchronous suggestions enabled' do
  let(:options) { ["ZSH_AUTOSUGGEST_USE_ASYNC="] }

  describe '`up-line-or-beginning-search`' do
    let(:before_sourcing) do
      -> do
        session.
          run_command('autoload -U up-line-or-beginning-search').
          run_command('zle -N up-line-or-beginning-search').
          send_string('bindkey "').
          send_keys('C-v').send_keys('up').
          send_string('" up-line-or-beginning-search').
          send_keys('enter')
      end
    end

    it 'should show previous history entries' do
      with_history(
        'echo foo',
        'echo bar',
        'echo baz'
      ) do
        session.clear_screen
        3.times { session.send_keys('up') }
        wait_for { session.content }.to eq("echo foo")
      end
    end
  end

  describe '`copy-earlier-word`' do
    let(:before_sourcing) do
      -> do
        session.
          run_command('autoload -Uz copy-earlier-word').
          run_command('zle -N copy-earlier-word').
          run_command('bindkey "^N" copy-earlier-word')
      end
    end

    it 'should cycle through previous words in the buffer' do
      session.clear_screen
      session.send_string('foo bar baz')
      sleep 0.5
      session.send_keys('C-n')
      wait_for { session.content }.to eq('foo bar bazbaz')
      session.send_keys('C-n')
      wait_for { session.content }.to eq('foo bar bazbar')
      session.send_keys('C-n')
      wait_for { session.content }.to eq('foo bar bazfoo')
    end
  end

  describe 'pressing ^C after fetching a suggestion' do
    before do
      skip 'Workaround does not work below v5.0.8' if session.zsh_version < Gem::Version.new('5.0.8')
    end

    it 'terminates the prompt and begins a new one' do
      session.send_keys('e')
      sleep 0.5
      session.send_keys('C-c')
      sleep 0.5
      session.send_keys('echo')

      wait_for { session.content }.to eq("e\necho")
    end
  end
end


```

## File: `spec/kill_ring_spec.rb`
```ruby
context 'with some items in the kill ring' do
  before do
    session.
      send_string('echo foo').
      send_keys('C-u').
      send_string('echo bar').
      send_keys('C-u')
  end

  describe '`yank-pop`' do
    it 'should cycle through all items in the kill ring' do
      session.send_keys('C-y')
      wait_for { session.content }.to eq('echo bar')

      session.send_keys('escape').send_keys('y')
      wait_for { session.content }.to eq('echo foo')

      session.send_keys('escape').send_keys('y')
      wait_for { session.content }.to eq('echo bar')
    end
  end
end

```

## File: `spec/line_init_spec.rb`
```ruby
context 'with zle-line-init unignored' do
  let(:after_sourcing) do
    -> do
      session.
        run_command('setopt extendedglob').
        run_command('ZSH_AUTOSUGGEST_IGNORE_WIDGETS=(${(@)ZSH_AUTOSUGGEST_IGNORE_WIDGETS:#zle-\*} zle-\^line-init)').
        run_command('zle-line-init() { BUFFER="echo" }')
    end
  end

  it 'should fetch a suggestion on each line initialization' do
    with_history('echo foo') do
      session.run_command('zle -N zle-line-init')
      wait_for { session.content }.to end_with('echo foo')
    end
  end
end
```

## File: `spec/multi_line_spec.rb`
```ruby
describe 'a multi-line suggestion' do
  it 'should be displayed on multiple lines' do
    with_history("echo \"\n\"") do
      session.send_keys('e')
      wait_for { session.content }.to eq("echo \"\n\"")
    end
  end
end
```

## File: `spec/spec_helper.rb`
```ruby
require 'pry'
require 'rspec/wait'
require 'terminal_session'
require 'tempfile'

RSpec.shared_context 'terminal session' do
  let(:term_opts) { {} }
  let(:session) { TerminalSession.new(term_opts) }
  let(:before_sourcing) { -> {} }
  let(:after_sourcing) { -> {} }
  let(:options) { [] }

  around do |example|
    before_sourcing.call
    session.run_command(['source zsh-autosuggestions.zsh', *options].join('; '))
    after_sourcing.call
    session.clear_screen

    example.run

    session.destroy
  end

  def with_history(*commands, &block)
    Tempfile.create do |f|
      f.write(commands.map{|c| c.gsub("\n", "\\\n")}.join("\n"))
      f.flush

      session.run_command('fc -p')
      session.run_command("fc -R #{f.path}")

      session.clear_screen

      yield block

      session.send_keys('C-c')
      session.run_command('fc -P')
    end
  end
end

RSpec.configure do |config|
  config.expect_with :rspec do |expectations|
    expectations.include_chain_clauses_in_custom_matcher_descriptions = true
  end

  config.mock_with :rspec do |mocks|
    mocks.verify_partial_doubles = true
  end

  config.wait_timeout = 2

  config.include_context 'terminal session'
end
```

## File: `spec/terminal_session.rb`
```ruby
require 'securerandom'

class TerminalSession
  ZSH_BIN = ENV['TEST_ZSH_BIN'] || 'zsh'

  def initialize(opts = {})
    opts = {
      width: 80,
      height: 24,
      prompt: '',
      term: 'xterm-256color',
      zsh_bin: ZSH_BIN
    }.merge(opts)

    @opts = opts

    cmd="PS1=\"#{opts[:prompt]}\" TERM=#{opts[:term]} #{ZSH_BIN} -f"
    tmux_command("new-session -d -x #{opts[:width]} -y #{opts[:height]} '#{cmd}'")
  end

  def zsh_version
    @zsh_version ||= Gem::Version.new(`#{ZSH_BIN} -c 'echo -n $ZSH_VERSION'`)
  end

  def tmux_socket_name
    @tmux_socket_name ||= SecureRandom.hex(6)
  end

  def run_command(command)
    send_string(command)
    send_keys('enter')

    self
  end

  def send_string(str)
    tmux_command("send-keys -t 0 -l -- '#{str.gsub("'", "\\'")}'")

    self
  end

  def send_keys(*keys)
    tmux_command("send-keys -t 0 #{keys.join(' ')}")

    self
  end

  def paste_string(str)
    tmux_command("set-buffer -- '#{str}'")
    tmux_command("paste-buffer -dpr -t 0")

    self
  end

  def content(esc_seqs: false)
    cmd = 'capture-pane -p -t 0'
    cmd += ' -e' if esc_seqs
    tmux_command(cmd).strip
  end

  def clear_screen
    send_keys('C-l')

    i = 0
    until content == opts[:prompt] || i > 20 do
      sleep(0.1)
      i = i + 1
    end

    self
  end

  def destroy
    tmux_command('kill-session')
  end

  def cursor
    tmux_command("display-message -t 0 -p '\#{cursor_x},\#{cursor_y}'").
      strip.
      split(',').
      map(&:to_i)
  end

  def attach!
    tmux_command('attach-session')
  end

  private

  attr_reader :opts

  def tmux_command(cmd)
    out = `tmux -u -L #{tmux_socket_name} #{cmd}`

    raise("tmux error running: '#{cmd}'") unless $?.success?

    out
  end
end
```

## File: `spec/integrations/auto_cd_spec.rb`
```ruby
describe 'with `AUTO_CD` option set' do
  let(:after_sourcing) do
    -> {
      session.run_command('setopt AUTO_CD')
      session.run_command('autoload compinit && compinit')
    }
  end

  it 'directory names are still completed' do
    session.send_string('sr')
    session.send_keys('C-i')
    wait_for { session.content }.to eq('src/')
  end
end
```

## File: `spec/integrations/bracketed_paste_magic_spec.rb`
```ruby
describe 'pasting using bracketed-paste-magic' do
  let(:before_sourcing) do
    -> do
      session.
        run_command('autoload -Uz bracketed-paste-magic').
        run_command('zle -N bracketed-paste bracketed-paste-magic')
    end
  end

  context 'with suggestions disabled while pasting' do
    before do
      session.
        run_command('bpm_init() { zle autosuggest-disable }').
        run_command('bpm_finish() { zle autosuggest-enable }').
        run_command('zstyle :bracketed-paste-magic paste-init bpm_init').
        run_command('zstyle :bracketed-paste-magic paste-finish bpm_finish')
    end

    it 'does not show an incorrect suggestion' do
      with_history('echo hello') do
        session.paste_string("echo #{'a' * 60}")
        sleep 1
        expect(session.content).to eq("echo #{'a' * 60}")
      end
    end
  end

  context 'with `bracketed-paste` added to the list of widgets that clear the suggestion' do
    let(:options) { ['ZSH_AUTOSUGGEST_CLEAR_WIDGETS+=(bracketed-paste)'] }

    it 'does not retain an old suggestion' do
      with_history ('echo foo') do
        session.send_string('echo ')
        wait_for { session.content }.to eq('echo foo')
        session.paste_string('bar')
        wait_for { session.content }.to eq('echo bar')
        session.send_keys('C-a') # Any cursor movement works
        sleep 1
        expect(session.content).to eq('echo bar')
      end
    end
  end
end
```

## File: `spec/integrations/client_zpty_spec.rb`
```ruby
describe 'a running zpty command' do
  let(:before_sourcing) { -> { session.run_command('zmodload zsh/zpty && zpty -b kitty cat') } }

  context 'when using `completion` strategy' do
    let(:options) { ["ZSH_AUTOSUGGEST_STRATEGY=completion"] }

    it 'is not affected' do
      session.send_keys('a').send_keys('C-h')
      session.run_command('zpty -t kitty; echo $?')

      wait_for { session.content }.to end_with("\n0")
    end
  end
end
```

## File: `spec/integrations/glob_subst_spec.rb`
```ruby
describe 'with `GLOB_SUBST` option set' do
  let(:after_sourcing) do
    -> {
      session.run_command('setopt GLOB_SUBST')
    }
  end

  it 'error messages are not printed' do
    session.send_string('[[')
    wait_for { session.content }.to eq('[[')
  end
end
```

## File: `spec/integrations/rebound_bracket_spec.rb`
```ruby
describe 'rebinding [' do
  context 'initialized before sourcing the plugin' do
    before do
      session.run_command("function [ { $commands[\\[] \"$@\" }")
      session.clear_screen
    end

    it 'executes the custom behavior and the built-in behavior' do
      session.send_string('asdf')
      wait_for { session.content }.to eq('asdf')
    end
  end
end
```

## File: `spec/integrations/vi_mode_spec.rb`
```ruby
describe 'when using vi mode' do
  let(:before_sourcing) do
    -> do
      session.run_command('bindkey -v')
    end
  end

  describe 'moving the cursor after exiting insert mode' do
    it 'should not clear the current suggestion' do
      with_history('foobar foo') do
        session.
          send_string('foo').
          send_keys('escape').
          send_keys('h')

        wait_for { session.content }.to eq('foobar foo')
      end
    end
  end

  describe '`vi-forward-word-end`' do
    it 'should accept through the end of the current word' do
      with_history('foobar foo') do
        session.
          send_string('foo').
          send_keys('escape').
          send_keys('e'). # vi-forward-word-end
          send_keys('a'). # vi-add-next
          send_string('baz')

        wait_for { session.content }.to eq('foobarbaz')
      end
    end
  end

  describe '`vi-forward-word`' do
    it 'should accept through the first character of the next word' do
      with_history('foobar foo') do
        session.
          send_string('foo').
          send_keys('escape').
          send_keys('w'). # vi-forward-word
          send_keys('a'). # vi-add-next
          send_string('az')

        wait_for { session.content }.to eq('foobar faz')
      end
    end
  end

  describe '`vi-find-next-char`' do
    it 'should accept through the next occurrence of the character' do
      with_history('foobar foo') do
        session.
          send_string('foo').
          send_keys('escape').
          send_keys('f'). # vi-find-next-char
          send_keys('o').
          send_keys('a'). # vi-add-next
          send_string('b')

        wait_for { session.content }.to eq('foobar fob')
      end
    end
  end

  describe '`vi-delete`' do
    it 'should be able to remove the last character in the buffer' do
      skip 'deleting last char did not work below zsh version 5.0.8' if session.zsh_version < Gem::Version.new('5.0.8')

      session.
        send_string('echo foo').
        send_keys('escape').
        send_keys('d').
        send_keys('l')

      wait_for { session.content }.to eq('echo fo')
    end
  end
end
```

## File: `spec/integrations/wrapped_widget_spec.rb`
```ruby
describe 'a wrapped widget' do
  let(:widget) { 'backward-delete-char' }

  context 'initialized before sourcing the plugin' do
    let(:before_sourcing) do
      -> do
        session.
          run_command("_orig_#{widget}() { zle .#{widget} }").
          run_command("zle -N orig-#{widget} _orig_#{widget}").
          run_command("#{widget}-magic() { zle orig-#{widget}; BUFFER+=b }").
          run_command("zle -N #{widget} #{widget}-magic")
      end
    end

    it 'executes the custom behavior and the built-in behavior' do
      with_history('foobar', 'foodar') do
        session.send_string('food').send_keys('C-h')
        wait_for { session.content }.to eq('foobar')
      end
    end
  end

  context 'initialized after sourcing the plugin' do
    before do
      session.
        run_command("zle -N orig-#{widget} ${widgets[#{widget}]#*:}").
        run_command("#{widget}-magic() { zle orig-#{widget}; BUFFER+=b }").
        run_command("zle -N #{widget} #{widget}-magic").
        clear_screen
    end

    it 'executes the custom behavior and the built-in behavior' do
      with_history('foobar', 'foodar') do
        session.send_string('food').send_keys('C-h')
        wait_for { session.content }.to eq('foobar')
      end
    end
  end
end
```

## File: `spec/integrations/zle_input_stack_spec.rb`
```ruby
describe 'using `zle -U`' do
  let(:before_sourcing) do
    -> do
      session.
        run_command('_zsh_autosuggest_strategy_test() { sleep 1; _zsh_autosuggest_strategy_history "$1" }').
        run_command('foo() { zle -U - "echo hello" }; zle -N foo; bindkey ^B foo')
    end
  end

  let(:options) { ['unset ZSH_AUTOSUGGEST_USE_ASYNC', 'ZSH_AUTOSUGGEST_STRATEGY=test'] }

  # TODO: This is only possible with the $KEYS_QUEUED_COUNT widget parameter, coming soon...
  xit 'does not fetch a suggestion for every inserted character' do
    session.send_keys('C-b')
    wait_for { session.content }.to eq('echo hello')
  end

  it 'shows a suggestion when the widget completes' do
    with_history('echo hello world') do
      session.send_keys('C-b')
      wait_for { session.content(esc_seqs: true) }.to match(/\Aecho hello\e\[[0-9]+m world/)
    end
  end
end
```

## File: `spec/options/buffer_max_size_spec.rb`
```ruby
describe 'a suggestion' do
  let(:term_opts) { { width: 200 } }
  let(:long_command) { "echo #{'a' * 100}" }

  around do |example|
    with_history(long_command) { example.run }
  end

  it 'is provided for any buffer length' do
    session.send_string(long_command[0...-1])
    wait_for { session.content }.to eq(long_command)
  end

  context 'when ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE is specified' do
    let(:buffer_max_size) { 10 }
    let(:options) { ["ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=#{buffer_max_size}"] }

    it 'is provided when the buffer is shorter than the specified length' do
      session.send_string(long_command[0...(buffer_max_size - 1)])
      wait_for { session.content }.to eq(long_command)
    end

    it 'is provided when the buffer is equal to the specified length' do
      session.send_string(long_command[0...(buffer_max_size)])
      wait_for { session.content }.to eq(long_command)
    end

    it 'is not provided when the buffer is longer than the specified length'
  end
end
```

## File: `spec/options/highlight_style_spec.rb`
```ruby
describe 'a displayed suggestion' do
  it 'is shown in the default style'

  describe 'when ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE is set to a zle_highlight string' do
    it 'is shown in the specified style'
  end
end
```

## File: `spec/options/original_widget_prefix_spec.rb`
```ruby
describe 'an original zle widget' do
  context 'is accessible with the default prefix'

  context 'when ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX is set' do
    it 'is accessible with the specified prefix'
  end
end
```

## File: `spec/options/strategy_spec.rb`
```ruby
describe 'a suggestion for a given prefix' do
  let(:history_strategy) { '_zsh_autosuggest_strategy_history() { suggestion="history" }' }
  let(:foobar_strategy) { '_zsh_autosuggest_strategy_foobar() { [[ "foobar baz" = $1* ]] && suggestion="foobar baz" }' }
  let(:foobaz_strategy) { '_zsh_autosuggest_strategy_foobaz() { [[ "foobaz bar" = $1* ]] && suggestion="foobaz bar" }' }

  let(:after_sourcing) do
    -> do
      session.run_command(history_strategy)
    end
  end

  it 'by default is determined by calling the `history` strategy function' do
    session.send_string('h')
    wait_for { session.content }.to eq('history')
  end

  context 'when ZSH_AUTOSUGGEST_STRATEGY is set to an array' do
    let(:after_sourcing) do
      -> do
        session.
          run_command(foobar_strategy).
          run_command(foobaz_strategy).
          run_command('ZSH_AUTOSUGGEST_STRATEGY=(foobar foobaz)')
      end
    end

    it 'is determined by the first strategy function to return a suggestion' do
      session.send_string('foo')
      wait_for { session.content }.to eq('foobar baz')

      session.send_string('baz')
      wait_for { session.content }.to eq('foobaz bar')
    end
  end

  context 'when ZSH_AUTOSUGGEST_STRATEGY is set to a string' do
    let(:after_sourcing) do
      -> do
        session.
          run_command(foobar_strategy).
          run_command(foobaz_strategy).
          run_command('ZSH_AUTOSUGGEST_STRATEGY="foobar foobaz"')
      end
    end

    it 'is determined by the first strategy function to return a suggestion' do
      session.send_string('foo')
      wait_for { session.content }.to eq('foobar baz')

      session.send_string('baz')
      wait_for { session.content }.to eq('foobaz bar')
    end
  end
end

```

## File: `spec/options/widget_lists_spec.rb`
```ruby
describe 'a zle widget' do
  let(:widget) { 'my-widget' }
  let(:before_sourcing) { -> { session.run_command("#{widget}() {}; zle -N #{widget}; bindkey ^B #{widget}") } }

  context 'when added to ZSH_AUTOSUGGEST_ACCEPT_WIDGETS' do
    let(:options) { ["ZSH_AUTOSUGGEST_ACCEPT_WIDGETS+=(#{widget})"] }

    it 'accepts the suggestion and moves the cursor to the end of the buffer when invoked' do
      with_history('echo hello') do
        session.send_string('e')
        wait_for { session.content }.to eq('echo hello')
        session.send_keys('C-b')
        wait_for { session.content(esc_seqs: true) }.to eq('echo hello')
        wait_for { session.cursor }.to eq([10, 0])
      end
    end
  end

  context 'when added to ZSH_AUTOSUGGEST_CLEAR_WIDGETS' do
    let(:options) { ["ZSH_AUTOSUGGEST_CLEAR_WIDGETS+=(#{widget})"] }

    it 'clears the suggestion when invoked' do
      with_history('echo hello') do
        session.send_string('e')
        wait_for { session.content }.to eq('echo hello')
        session.send_keys('C-b')
        wait_for { session.content }.to eq('e')
      end
    end
  end

  context 'when added to ZSH_AUTOSUGGEST_EXECUTE_WIDGETS' do
    let(:options) { ["ZSH_AUTOSUGGEST_EXECUTE_WIDGETS+=(#{widget})"] }

    it 'executes the suggestion when invoked' do
      with_history('echo hello') do
        session.send_string('e')
        wait_for { session.content }.to eq('echo hello')
        session.send_keys('C-b')
        wait_for { session.content }.to end_with("\nhello")
      end
    end
  end

  context 'when added to ZSH_AUTOSUGGEST_IGNORE_WIDGETS' do
    let(:options) { ["ZSH_AUTOSUGGEST_IGNORE_WIDGETS=(#{widget})"] }

    it 'should not be wrapped with an autosuggest widget' do
      session.run_command("echo $widgets[#{widget}]")
      wait_for { session.content }.to end_with("\nuser:#{widget}")
    end
  end

  context 'that moves the cursor forward' do
    before { session.run_command("#{widget}() { zle forward-char }") }

    context 'when added to ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS' do
      let(:options) { ["ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS=(#{widget})"] }

      it 'accepts the suggestion as far as the cursor is moved when invoked' do
        with_history('echo hello') do
          session.send_string('e')
          wait_for { session.content }.to start_with('echo hello')
          session.send_keys('C-b')
          wait_for { session.content(esc_seqs: true) }.to match(/\Aec\e\[[0-9]+mho hello/)
        end
      end
    end
  end

  context 'that modifies the buffer' do
    before { session.run_command("#{widget}() { BUFFER=\"foo\" }") }

    context 'when not added to any of the widget lists' do
      it 'modifies the buffer and fetches a new suggestion' do
        with_history('foobar') do
          session.send_keys('C-b')
          wait_for { session.content }.to eq('foobar')
        end
      end
    end
  end
end

describe 'a modification to the widget lists' do
  let(:widget) { 'my-widget' }
  let(:before_sourcing) { -> { session.run_command("#{widget}() {}; zle -N #{widget}; bindkey ^B #{widget}") } }
  before { session.run_command("ZSH_AUTOSUGGEST_ACCEPT_WIDGETS+=(#{widget})") }

  it 'takes effect on the next cmd line' do
    with_history('echo hello') do
      session.send_string('e')
      wait_for { session.content }.to eq('echo hello')
      session.send_keys('C-b')
      wait_for { session.content(esc_seqs: true) }.to eq('echo hello')
    end
  end

  context 'when manual rebind is enabled' do
    let(:options) { ["ZSH_AUTOSUGGEST_MANUAL_REBIND=true"] }

    it 'does not take effect until bind command is re-run' do
      with_history('echo hello') do
        session.send_string('e')
        wait_for { session.content }.to eq('echo hello')
        session.send_keys('C-b')
        sleep 1
        expect(session.content(esc_seqs: true)).not_to eq('echo hello')

        session.send_keys('C-c')
        session.run_command('_zsh_autosuggest_bind_widgets').clear_screen
        wait_for { session.content }.to eq('')

        session.send_string('e')
        wait_for { session.content }.to eq('echo hello')
        session.send_keys('C-b')
        wait_for { session.content(esc_seqs: true) }.to eq('echo hello')
      end
    end
  end
end
```

## File: `spec/strategies/completion_spec.rb`
```ruby
describe 'the `completion` suggestion strategy' do
  let(:options) { ['ZSH_AUTOSUGGEST_STRATEGY=completion'] }
  let(:before_sourcing) do
    -> do
      session.
        run_command('autoload compinit && compinit').
        run_command('_foo() { compadd bar; compadd bat }').
        run_command('_num() { compadd two; compadd three }').
        run_command('compdef _foo baz').
        run_command('compdef _num one')
    end
  end

  it 'suggests the first completion result' do
    session.send_string('baz ')
    wait_for { session.content }.to eq('baz bar')
  end

  it 'does not add extra carriage returns when prefix has a line feed' do
    skip '`stty` does not work inside zpty below zsh version 5.0.3' if session.zsh_version < Gem::Version.new('5.0.3')
    session.send_string('baz \\').send_keys('C-v', 'C-j')
    wait_for { session.content }.to eq("baz \\\nbar")
  end

  context 'when `_complete` is aliased' do
    let(:before_sourcing) do
      -> do
        session.
          run_command('autoload compinit && compinit').
          run_command('_foo() { compadd bar; compadd bat }').
          run_command('compdef _foo baz').
          run_command('alias _complete=_complete')
      end
    end

    it 'suggests the first completion result' do
      session.send_string('baz ')
      wait_for { session.content }.to eq('baz bar')
    end
  end

  context 'when ZSH_AUTOSUGGEST_COMPLETION_IGNORE is set to a pattern' do
    let(:options) { ['ZSH_AUTOSUGGEST_STRATEGY=completion', 'ZSH_AUTOSUGGEST_COMPLETION_IGNORE="one *"'] }

    it 'makes suggestions when the buffer does not match the pattern' do
      session.send_string('baz ')
      wait_for { session.content }.to eq('baz bar')
    end

    it 'does not make suggestions when the buffer matches the pattern' do
      session.send_string('one t')
      sleep 1
      expect(session.content).to eq('one t')
    end
  end

  context 'when async mode is enabled' do
    let(:options) { ['ZSH_AUTOSUGGEST_USE_ASYNC=true', 'ZSH_AUTOSUGGEST_STRATEGY=completion'] }

    it 'suggests the first completion result' do
      session.send_string('baz ')
      wait_for { session.content }.to eq('baz bar')
    end

    it 'does not add extra carriage returns when prefix has a line feed' do
      skip '`stty` does not work inside zpty below zsh version 5.0.3' if session.zsh_version < Gem::Version.new('5.0.3')
      session.send_string('baz \\').send_keys('C-v', 'C-j')
      wait_for { session.content }.to eq("baz \\\nbar")
    end
  end
end

```

## File: `spec/strategies/history_spec.rb`
```ruby
require 'strategies/special_characters_helper'

describe 'the `history` suggestion strategy' do
  it 'suggests the last matching history entry' do
    with_history('ls foo', 'ls bar', 'echo baz') do
      session.send_string('ls')
      wait_for { session.content }.to eq('ls bar')
    end
  end

  context 'when ZSH_AUTOSUGGEST_HISTORY_IGNORE is set to a pattern' do
    let(:options) { ['ZSH_AUTOSUGGEST_HISTORY_IGNORE="* bar"'] }

    it 'does not make suggestions that match the pattern' do
      with_history('ls foo', 'ls bar', 'echo baz') do
        session.send_string('ls')
        wait_for { session.content }.to eq('ls foo')
      end
    end
  end

  include_examples 'special characters'
end
```

## File: `spec/strategies/match_prev_cmd_spec.rb`
```ruby
require 'strategies/special_characters_helper'

describe 'the `match_prev_cmd` strategy' do
  let(:options) { ['ZSH_AUTOSUGGEST_STRATEGY=match_prev_cmd'] }

  let(:history) { [
    'echo what',
    'ls foo',
    'echo what',
    'ls bar',
    'ls baz',
    'echo what'
  ] }

  it 'suggests the last matching history entry after the previous command' do
    with_history(*history) do
      session.send_string('ls')
      wait_for { session.content }.to eq('ls bar')
    end
  end

  context 'when ZSH_AUTOSUGGEST_HISTORY_IGNORE is set to a pattern' do
    let(:options) { ['ZSH_AUTOSUGGEST_STRATEGY=match_prev_cmd', 'ZSH_AUTOSUGGEST_HISTORY_IGNORE="* bar"'] }

    it 'does not make suggestions that match the pattern' do
      with_history(*history) do
        session.send_string('ls')
        wait_for { session.content }.to eq('ls foo')
      end
    end
  end

  include_examples 'special characters'
end
```

## File: `spec/strategies/special_characters_helper.rb`
```ruby
shared_examples 'special characters' do
  describe 'a special character in the buffer should be treated like any other character' do
    it 'asterisk' do
      with_history('echo "hello*"', 'echo "hello."') do
        session.send_string('echo "hello*')
        wait_for { session.content }.to eq('echo "hello*"')
      end
    end

    it 'question mark' do
      with_history('echo "hello?"', 'echo "hello."') do
        session.send_string('echo "hello?')
        wait_for { session.content }.to eq('echo "hello?"')
      end
    end

    it 'backslash' do
      with_history('echo "hello\nworld"') do
        session.send_string('echo "hello\\')
        wait_for { session.content }.to eq('echo "hello\nworld"')
      end
    end

    it 'double backslash' do
      with_history('echo "\\\\"') do
        session.send_string('echo "\\\\')
        wait_for { session.content }.to eq('echo "\\\\"')
      end
    end

    it 'tilde' do
      with_history('echo ~/foo') do
        session.send_string('echo ~')
        wait_for { session.content }.to eq('echo ~/foo')
      end
    end

    it 'parentheses' do
      with_history('echo "$(ls foo)"') do
        session.send_string('echo "$(')
        wait_for { session.content }.to eq('echo "$(ls foo)"')
      end
    end

    it 'square bracket' do
      with_history('echo "$history[123]"') do
        session.send_string('echo "$history[')
        wait_for { session.content }.to eq('echo "$history[123]"')
        session.send_string('123]')
        wait_for { session.content }.to eq('echo "$history[123]"')
      end
    end

    it 'octothorpe' do
      with_history('echo "#yolo"') do
        session.send_string('echo "#')
        wait_for { session.content }.to eq('echo "#yolo"')
      end
    end

    it 'caret' do
      with_history('echo "^A"', 'echo "^B"') do
        session.send_string('echo "^A')
        wait_for { session.content }.to eq('echo "^A"')
      end
    end

    it 'dash' do
      with_history('-foo() {}') do
        session.send_string('-')
        wait_for { session.content }.to eq('-foo() {}')
      end
    end
  end
end
```

## File: `spec/widgets/disable_spec.rb`
```ruby
describe 'the `autosuggest-disable` widget' do
  before do
    session.run_command('bindkey ^B autosuggest-disable')
  end

  it 'disables suggestions and clears the suggestion' do
    with_history('echo hello') do
      session.send_string('echo')
      wait_for { session.content }.to eq('echo hello')

      session.send_keys('C-b')
      wait_for { session.content }.to eq('echo')

      session.send_string(' h')
      sleep 1
      expect(session.content).to eq('echo h')
    end
  end
end
```

## File: `spec/widgets/enable_spec.rb`
```ruby
describe 'the `autosuggest-enable` widget' do
  before do
    session.
      run_command('typeset -g _ZSH_AUTOSUGGEST_DISABLED').
      run_command('bindkey ^B autosuggest-enable')
  end

  it 'enables suggestions and fetches a suggestion' do
    with_history('echo hello') do
      session.send_string('e')
      sleep 1
      expect(session.content).to eq('e')

      session.send_keys('C-b')
      session.send_string('c')
      wait_for { session.content }.to eq('echo hello')
    end
  end

  context 'invoked on an empty buffer' do
    it 'does not fetch a suggestion' do
      with_history('echo hello') do
        session.send_keys('C-b')
        sleep 1
        expect(session.content).to eq('')
      end
    end
  end

  context 'invoked on a non-empty buffer' do
    it 'fetches a suggestion' do
      with_history('echo hello') do
        session.send_string('e')
        sleep 1
        expect(session.content).to eq('e')

        session.send_keys('C-b')
        wait_for { session.content }.to eq('echo hello')
      end
    end
  end
end
```

## File: `spec/widgets/fetch_spec.rb`
```ruby
describe 'the `autosuggest-fetch` widget' do
  context 'when suggestions are disabled' do
    before do
      session.
        run_command('bindkey ^B autosuggest-disable').
        run_command('bindkey ^F autosuggest-fetch').
        send_keys('C-b')
    end

    it 'will fetch and display a suggestion' do
      with_history('echo hello') do
        session.send_string('echo h')
        sleep 1
        expect(session.content).to eq('echo h')

        session.send_keys('C-f')
        wait_for { session.content }.to eq('echo hello')

        session.send_string('e')
        wait_for { session.content }.to eq('echo hello')
      end
    end
  end
end
```

## File: `spec/widgets/toggle_spec.rb`
```ruby
describe 'the `autosuggest-toggle` widget' do
  before do
    session.run_command('bindkey ^B autosuggest-toggle')
  end

  it 'toggles suggestions' do
    with_history('echo world', 'echo hello') do
      session.send_string('echo')
      wait_for { session.content }.to eq('echo hello')

      session.send_keys('C-b')
      wait_for { session.content }.to eq('echo')

      session.send_string(' h')
      sleep 1
      expect(session.content).to eq('echo h')

      session.send_keys('C-b')
      wait_for { session.content }.to eq('echo hello')

      session.send_keys('C-h')
      session.send_string('w')
      wait_for { session.content }.to eq('echo world')
    end
  end
end
```

## File: `src/async.zsh`
```

#--------------------------------------------------------------------#
# Async                                                              #
#--------------------------------------------------------------------#

_zsh_autosuggest_async_request() {
	zmodload zsh/system 2>/dev/null # For `$sysparams`

	typeset -g _ZSH_AUTOSUGGEST_ASYNC_FD _ZSH_AUTOSUGGEST_CHILD_PID

	# If we've got a pending request, cancel it
	if [[ -n "$_ZSH_AUTOSUGGEST_ASYNC_FD" ]] && { true <&$_ZSH_AUTOSUGGEST_ASYNC_FD } 2>/dev/null; then
		# Close the file descriptor and remove the handler
		builtin exec {_ZSH_AUTOSUGGEST_ASYNC_FD}<&-
		zle -F $_ZSH_AUTOSUGGEST_ASYNC_FD

		# We won't know the pid unless the user has zsh/system module installed
		if [[ -n "$_ZSH_AUTOSUGGEST_CHILD_PID" ]]; then
			# Zsh will make a new process group for the child process only if job
			# control is enabled (MONITOR option)
			if [[ -o MONITOR ]]; then
				# Send the signal to the process group to kill any processes that may
				# have been forked by the suggestion strategy
				kill -TERM -$_ZSH_AUTOSUGGEST_CHILD_PID 2>/dev/null
			else
				# Kill just the child process since it wasn't placed in a new process
				# group. If the suggestion strategy forked any child processes they may
				# be orphaned and left behind.
				kill -TERM $_ZSH_AUTOSUGGEST_CHILD_PID 2>/dev/null
			fi
		fi
	fi

	# Fork a process to fetch a suggestion and open a pipe to read from it
	builtin exec {_ZSH_AUTOSUGGEST_ASYNC_FD}< <(
		# Tell parent process our pid
		echo $sysparams[pid]

		# Fetch and print the suggestion
		local suggestion
		_zsh_autosuggest_fetch_suggestion "$1"
		echo -nE "$suggestion"
	)

	# There's a weird bug here where ^C stops working unless we force a fork
	# See https://github.com/zsh-users/zsh-autosuggestions/issues/364
	autoload -Uz is-at-least
	is-at-least 5.8 || command true

	# Read the pid from the child process
	read _ZSH_AUTOSUGGEST_CHILD_PID <&$_ZSH_AUTOSUGGEST_ASYNC_FD

	# When the fd is readable, call the response handler
	zle -F "$_ZSH_AUTOSUGGEST_ASYNC_FD" _zsh_autosuggest_async_response
}

# Called when new data is ready to be read from the pipe
# First arg will be fd ready for reading
# Second arg will be passed in case of error
_zsh_autosuggest_async_response() {
	emulate -L zsh

	local suggestion

	if [[ -z "$2" || "$2" == "hup" ]]; then
		# Read everything from the fd and give it as a suggestion
		IFS='' read -rd '' -u $1 suggestion
		zle autosuggest-suggest -- "$suggestion"

		# Close the fd
		builtin exec {1}<&-
	fi

	# Always remove the handler
	zle -F "$1"
	_ZSH_AUTOSUGGEST_ASYNC_FD=
}
```

## File: `src/bind.zsh`
```

#--------------------------------------------------------------------#
# Widget Helpers                                                     #
#--------------------------------------------------------------------#

_zsh_autosuggest_incr_bind_count() {
	typeset -gi bind_count=$((_ZSH_AUTOSUGGEST_BIND_COUNTS[$1]+1))
	_ZSH_AUTOSUGGEST_BIND_COUNTS[$1]=$bind_count
}

# Bind a single widget to an autosuggest widget, saving a reference to the original widget
_zsh_autosuggest_bind_widget() {
	typeset -gA _ZSH_AUTOSUGGEST_BIND_COUNTS

	local widget=$1
	local autosuggest_action=$2
	local prefix=$ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX

	local -i bind_count

	# Save a reference to the original widget
	case $widgets[$widget] in
		# Already bound
		user:_zsh_autosuggest_(bound|orig)_*)
			bind_count=$((_ZSH_AUTOSUGGEST_BIND_COUNTS[$widget]))
			;;

		# User-defined widget
		user:*)
			_zsh_autosuggest_incr_bind_count $widget
			zle -N $prefix$bind_count-$widget ${widgets[$widget]#*:}
			;;

		# Built-in widget
		builtin)
			_zsh_autosuggest_incr_bind_count $widget
			eval "_zsh_autosuggest_orig_${(q)widget}() { zle .${(q)widget} }"
			zle -N $prefix$bind_count-$widget _zsh_autosuggest_orig_$widget
			;;

		# Completion widget
		completion:*)
			_zsh_autosuggest_incr_bind_count $widget
			eval "zle -C $prefix$bind_count-${(q)widget} ${${(s.:.)widgets[$widget]}[2,3]}"
			;;
	esac

	# Pass the original widget's name explicitly into the autosuggest
	# function. Use this passed in widget name to call the original
	# widget instead of relying on the $WIDGET variable being set
	# correctly. $WIDGET cannot be trusted because other plugins call
	# zle without the `-w` flag (e.g. `zle self-insert` instead of
	# `zle self-insert -w`).
	eval "_zsh_autosuggest_bound_${bind_count}_${(q)widget}() {
		_zsh_autosuggest_widget_$autosuggest_action $prefix$bind_count-${(q)widget} \$@
	}"

	# Create the bound widget
	zle -N -- $widget _zsh_autosuggest_bound_${bind_count}_$widget
}

# Map all configured widgets to the right autosuggest widgets
_zsh_autosuggest_bind_widgets() {
	emulate -L zsh

 	local widget
	local ignore_widgets

	ignore_widgets=(
		.\*
		_\*
		${_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS/#/autosuggest-}
		$ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX\*
		$ZSH_AUTOSUGGEST_IGNORE_WIDGETS
	)

	# Find every widget we might want to bind and bind it appropriately
	for widget in ${${(f)"$(builtin zle -la)"}:#${(j:|:)~ignore_widgets}}; do
		if [[ -n ${ZSH_AUTOSUGGEST_CLEAR_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget clear
		elif [[ -n ${ZSH_AUTOSUGGEST_ACCEPT_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget accept
		elif [[ -n ${ZSH_AUTOSUGGEST_EXECUTE_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget execute
		elif [[ -n ${ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS[(r)$widget]} ]]; then
			_zsh_autosuggest_bind_widget $widget partial_accept
		else
			# Assume any unspecified widget might modify the buffer
			_zsh_autosuggest_bind_widget $widget modify
		fi
	done
}

# Given the name of an original widget and args, invoke it, if it exists
_zsh_autosuggest_invoke_original_widget() {
	# Do nothing unless called with at least one arg
	(( $# )) || return 0

	local original_widget_name="$1"

	shift

	if (( ${+widgets[$original_widget_name]} )); then
		zle $original_widget_name -- $@
	fi
}
```

## File: `src/config.zsh`
```

#--------------------------------------------------------------------#
# Global Configuration Variables                                     #
#--------------------------------------------------------------------#

# Color to use when highlighting suggestion
# Uses format of `region_highlight`
# More info: http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html#Zle-Widgets
(( ! ${+ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE} )) &&
typeset -g ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'

# Prefix to use when saving original versions of bound widgets
(( ! ${+ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX} )) &&
typeset -g ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX=autosuggest-orig-

# Strategies to use to fetch a suggestion
# Will try each strategy in order until a suggestion is returned
(( ! ${+ZSH_AUTOSUGGEST_STRATEGY} )) && {
	typeset -ga ZSH_AUTOSUGGEST_STRATEGY
	ZSH_AUTOSUGGEST_STRATEGY=(history)
}

# Widgets that clear the suggestion
(( ! ${+ZSH_AUTOSUGGEST_CLEAR_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_CLEAR_WIDGETS
	ZSH_AUTOSUGGEST_CLEAR_WIDGETS=(
		history-search-forward
		history-search-backward
		history-beginning-search-forward
		history-beginning-search-backward
		history-beginning-search-forward-end
		history-beginning-search-backward-end
		history-substring-search-up
		history-substring-search-down
		up-line-or-beginning-search
		down-line-or-beginning-search
		up-line-or-history
		down-line-or-history
		accept-line
		copy-earlier-word
	)
}

# Widgets that accept the entire suggestion
(( ! ${+ZSH_AUTOSUGGEST_ACCEPT_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_ACCEPT_WIDGETS
	ZSH_AUTOSUGGEST_ACCEPT_WIDGETS=(
		forward-char
		end-of-line
		vi-forward-char
		vi-end-of-line
		vi-add-eol
	)
}

# Widgets that accept the entire suggestion and execute it
(( ! ${+ZSH_AUTOSUGGEST_EXECUTE_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_EXECUTE_WIDGETS
	ZSH_AUTOSUGGEST_EXECUTE_WIDGETS=(
	)
}

# Widgets that accept the suggestion as far as the cursor moves
(( ! ${+ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS
	ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS=(
		forward-word
		emacs-forward-word
		vi-forward-word
		vi-forward-word-end
		vi-forward-blank-word
		vi-forward-blank-word-end
		vi-find-next-char
		vi-find-next-char-skip
	)
}

# Widgets that should be ignored (globbing supported but must be escaped)
(( ! ${+ZSH_AUTOSUGGEST_IGNORE_WIDGETS} )) && {
	typeset -ga ZSH_AUTOSUGGEST_IGNORE_WIDGETS
	ZSH_AUTOSUGGEST_IGNORE_WIDGETS=(
		orig-\*
		beep
		run-help
		set-local-history
		which-command
		yank
		yank-pop
		zle-\*
	)
}

# Pty name for capturing completions for completion suggestion strategy
(( ! ${+ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME} )) &&
typeset -g ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME=zsh_autosuggest_completion_pty
```

## File: `src/fetch.zsh`
```

#--------------------------------------------------------------------#
# Fetch Suggestion                                                   #
#--------------------------------------------------------------------#
# Loops through all specified strategies and returns a suggestion
# from the first strategy to provide one.
#

_zsh_autosuggest_fetch_suggestion() {
	typeset -g suggestion
	local -a strategies
	local strategy

	# Ensure we are working with an array
	strategies=(${=ZSH_AUTOSUGGEST_STRATEGY})

	for strategy in $strategies; do
		# Try to get a suggestion from this strategy
		_zsh_autosuggest_strategy_$strategy "$1"

		# Ensure the suggestion matches the prefix
		[[ "$suggestion" != "$1"* ]] && unset suggestion

		# Break once we've found a valid suggestion
		[[ -n "$suggestion" ]] && break
	done
}
```

## File: `src/highlight.zsh`
```

#--------------------------------------------------------------------#
# Highlighting                                                       #
#--------------------------------------------------------------------#

# If there was a highlight, remove it
_zsh_autosuggest_highlight_reset() {
	typeset -g _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT

	if [[ -n "$_ZSH_AUTOSUGGEST_LAST_HIGHLIGHT" ]]; then
		region_highlight=("${(@)region_highlight:#$_ZSH_AUTOSUGGEST_LAST_HIGHLIGHT}")
		unset _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT
	fi
}

# If there's a suggestion, highlight it
_zsh_autosuggest_highlight_apply() {
	typeset -g _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT

	if (( $#POSTDISPLAY )); then
		typeset -g _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT="$#BUFFER $(($#BUFFER + $#POSTDISPLAY)) $ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE"
		region_highlight+=("$_ZSH_AUTOSUGGEST_LAST_HIGHLIGHT")
	else
		unset _ZSH_AUTOSUGGEST_LAST_HIGHLIGHT
	fi
}
```

## File: `src/start.zsh`
```

#--------------------------------------------------------------------#
# Start                                                              #
#--------------------------------------------------------------------#

# Start the autosuggestion widgets
_zsh_autosuggest_start() {
	# By default we re-bind widgets on every precmd to ensure we wrap other
	# wrappers. Specifically, highlighting breaks if our widgets are wrapped by
	# zsh-syntax-highlighting widgets. This also allows modifications to the
	# widget list variables to take effect on the next precmd. However this has
	# a decent performance hit, so users can set ZSH_AUTOSUGGEST_MANUAL_REBIND
	# to disable the automatic re-binding.
	if (( ${+ZSH_AUTOSUGGEST_MANUAL_REBIND} )); then
		add-zsh-hook -d precmd _zsh_autosuggest_start
	fi

	_zsh_autosuggest_bind_widgets
}

# Mark for auto-loading the functions that we use
autoload -Uz add-zsh-hook is-at-least

# Automatically enable asynchronous mode in newer versions of zsh. Disable for
# older versions because there is a bug when using async mode where ^C does not
# work immediately after fetching a suggestion.
# See https://github.com/zsh-users/zsh-autosuggestions/issues/364
if is-at-least 5.0.8; then
	typeset -g ZSH_AUTOSUGGEST_USE_ASYNC=
fi

# Start the autosuggestion widgets on the next precmd
add-zsh-hook precmd _zsh_autosuggest_start
```

## File: `src/util.zsh`
```

#--------------------------------------------------------------------#
# Utility Functions                                                  #
#--------------------------------------------------------------------#

_zsh_autosuggest_escape_command() {
	setopt localoptions EXTENDED_GLOB

	# Escape special chars in the string (requires EXTENDED_GLOB)
	echo -E "${1//(#m)[\"\'\\()\[\]|*?~]/\\$MATCH}"
}
```

## File: `src/widgets.zsh`
```

#--------------------------------------------------------------------#
# Autosuggest Widget Implementations                                 #
#--------------------------------------------------------------------#

# Disable suggestions
_zsh_autosuggest_disable() {
	typeset -g _ZSH_AUTOSUGGEST_DISABLED
	_zsh_autosuggest_clear
}

# Enable suggestions
_zsh_autosuggest_enable() {
	unset _ZSH_AUTOSUGGEST_DISABLED

	if (( $#BUFFER )); then
		_zsh_autosuggest_fetch
	fi
}

# Toggle suggestions (enable/disable)
_zsh_autosuggest_toggle() {
	if (( ${+_ZSH_AUTOSUGGEST_DISABLED} )); then
		_zsh_autosuggest_enable
	else
		_zsh_autosuggest_disable
	fi
}

# Clear the suggestion
_zsh_autosuggest_clear() {
	# Remove the suggestion
	POSTDISPLAY=

	_zsh_autosuggest_invoke_original_widget $@
}

# Modify the buffer and get a new suggestion
_zsh_autosuggest_modify() {
	local -i retval

	# Only available in zsh >= 5.4
	local -i KEYS_QUEUED_COUNT

	# Save the contents of the buffer/postdisplay
	local orig_buffer="$BUFFER"
	local orig_postdisplay="$POSTDISPLAY"

	# Clear suggestion while waiting for next one
	POSTDISPLAY=

	# Original widget may modify the buffer
	_zsh_autosuggest_invoke_original_widget $@
	retval=$?

	emulate -L zsh

	# Don't fetch a new suggestion if there's more input to be read immediately
	if (( $PENDING > 0 || $KEYS_QUEUED_COUNT > 0 )); then
		POSTDISPLAY="$orig_postdisplay"
		return $retval
	fi

	# Optimize if manually typing in the suggestion or if buffer hasn't changed
	if [[ "$BUFFER" = "$orig_buffer"* && "$orig_postdisplay" = "${BUFFER:$#orig_buffer}"* ]]; then
		POSTDISPLAY="${orig_postdisplay:$(($#BUFFER - $#orig_buffer))}"
		return $retval
	fi

	# Bail out if suggestions are disabled
	if (( ${+_ZSH_AUTOSUGGEST_DISABLED} )); then
		return $?
	fi

	# Get a new suggestion if the buffer is not empty after modification
	if (( $#BUFFER > 0 )); then
		if [[ -z "$ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE" ]] || (( $#BUFFER <= $ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE )); then
			_zsh_autosuggest_fetch
		fi
	fi

	return $retval
}

# Fetch a new suggestion based on what's currently in the buffer
_zsh_autosuggest_fetch() {
	if (( ${+ZSH_AUTOSUGGEST_USE_ASYNC} )); then
		_zsh_autosuggest_async_request "$BUFFER"
	else
		local suggestion
		_zsh_autosuggest_fetch_suggestion "$BUFFER"
		_zsh_autosuggest_suggest "$suggestion"
	fi
}

# Offer a suggestion
_zsh_autosuggest_suggest() {
	emulate -L zsh

	local suggestion="$1"

	if [[ -n "$suggestion" ]] && (( $#BUFFER )); then
		POSTDISPLAY="${suggestion#$BUFFER}"
	else
		POSTDISPLAY=
	fi
}

# Accept the entire suggestion
_zsh_autosuggest_accept() {
	local -i retval max_cursor_pos=$#BUFFER

	# When vicmd keymap is active, the cursor can't move all the way
	# to the end of the buffer
	if [[ "$KEYMAP" = "vicmd" ]]; then
		max_cursor_pos=$((max_cursor_pos - 1))
	fi

	# If we're not in a valid state to accept a suggestion, just run the
	# original widget and bail out
	if (( $CURSOR != $max_cursor_pos || !$#POSTDISPLAY )); then
		_zsh_autosuggest_invoke_original_widget $@
		return
	fi

	# Only accept if the cursor is at the end of the buffer
	# Add the suggestion to the buffer
	BUFFER="$BUFFER$POSTDISPLAY"

	# Remove the suggestion
	POSTDISPLAY=

	# Run the original widget before manually moving the cursor so that the
	# cursor movement doesn't make the widget do something unexpected
	_zsh_autosuggest_invoke_original_widget $@
	retval=$?

	# Move the cursor to the end of the buffer
	if [[ "$KEYMAP" = "vicmd" ]]; then
		CURSOR=$(($#BUFFER - 1))
	else
		CURSOR=$#BUFFER
	fi

	return $retval
}

# Accept the entire suggestion and execute it
_zsh_autosuggest_execute() {
	# Add the suggestion to the buffer
	BUFFER="$BUFFER$POSTDISPLAY"

	# Remove the suggestion
	POSTDISPLAY=

	# Call the original `accept-line` to handle syntax highlighting or
	# other potential custom behavior
	_zsh_autosuggest_invoke_original_widget "accept-line"
}

# Partially accept the suggestion
_zsh_autosuggest_partial_accept() {
	local -i retval cursor_loc

	# Save the contents of the buffer so we can restore later if needed
	local original_buffer="$BUFFER"

	# Temporarily accept the suggestion.
	BUFFER="$BUFFER$POSTDISPLAY"

	# Original widget moves the cursor
	_zsh_autosuggest_invoke_original_widget $@
	retval=$?

	# Normalize cursor location across vi/emacs modes
	cursor_loc=$CURSOR
	if [[ "$KEYMAP" = "vicmd" ]]; then
		cursor_loc=$((cursor_loc + 1))
	fi

	# If we've moved past the end of the original buffer
	if (( $cursor_loc > $#original_buffer )); then
		# Set POSTDISPLAY to text right of the cursor
		POSTDISPLAY="${BUFFER[$(($cursor_loc + 1)),$#BUFFER]}"

		# Clip the buffer at the cursor
		BUFFER="${BUFFER[1,$cursor_loc]}"
	else
		# Restore the original buffer
		BUFFER="$original_buffer"
	fi

	return $retval
}

() {
	typeset -ga _ZSH_AUTOSUGGEST_BUILTIN_ACTIONS

	_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS=(
		clear
		fetch
		suggest
		accept
		execute
		enable
		disable
		toggle
	)

	local action
	for action in $_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS modify partial_accept; do
		eval "_zsh_autosuggest_widget_$action() {
			local -i retval

			_zsh_autosuggest_highlight_reset

			_zsh_autosuggest_$action \$@
			retval=\$?

			_zsh_autosuggest_highlight_apply

			zle -R

			return \$retval
		}"
	done

	for action in $_ZSH_AUTOSUGGEST_BUILTIN_ACTIONS; do
		zle -N autosuggest-$action _zsh_autosuggest_widget_$action
	done
}
```

## File: `src/strategies/completion.zsh`
```

#--------------------------------------------------------------------#
# Completion Suggestion Strategy                                     #
#--------------------------------------------------------------------#
# Fetches a suggestion from the completion engine
#

_zsh_autosuggest_capture_postcompletion() {
	# Always insert the first completion into the buffer
	compstate[insert]=1

	# Don't list completions
	unset 'compstate[list]'
}

_zsh_autosuggest_capture_completion_widget() {
	# Add a post-completion hook to be called after all completions have been
	# gathered. The hook can modify compstate to affect what is done with the
	# gathered completions.
	local -a +h comppostfuncs
	comppostfuncs=(_zsh_autosuggest_capture_postcompletion)

	# Only capture completions at the end of the buffer
	CURSOR=$#BUFFER

	# Run the original widget wrapping `.complete-word` so we don't
	# recursively try to fetch suggestions, since our pty is forked
	# after autosuggestions is initialized.
	zle -- ${(k)widgets[(r)completion:.complete-word:_main_complete]}

	if is-at-least 5.0.3; then
		# Don't do any cr/lf transformations. We need to do this immediately before
		# output because if we do it in setup, onlcr will be re-enabled when we enter
		# vared in the async code path. There is a bug in zpty module in older versions
		# where the tty is not properly attached to the pty slave, resulting in stty
		# getting stopped with a SIGTTOU. See zsh-workers thread 31660 and upstream
		# commit f75904a38
		stty -onlcr -ocrnl -F /dev/tty
	fi

	# The completion has been added, print the buffer as the suggestion
	echo -nE - $'\0'$BUFFER$'\0'
}

zle -N autosuggest-capture-completion _zsh_autosuggest_capture_completion_widget

_zsh_autosuggest_capture_setup() {
	# There is a bug in zpty module in older zsh versions by which a
	# zpty that exits will kill all zpty processes that were forked
	# before it. Here we set up a zsh exit hook to SIGKILL the zpty
	# process immediately, before it has a chance to kill any other
	# zpty processes.
	if ! is-at-least 5.4; then
		zshexit() {
			# The zsh builtin `kill` fails sometimes in older versions
			# https://unix.stackexchange.com/a/477647/156673
			kill -KILL $$ 2>&- || command kill -KILL $$

			# Block for long enough for the signal to come through
			sleep 1
		}
	fi

	# Try to avoid any suggestions that wouldn't match the prefix
	zstyle ':completion:*' matcher-list ''
	zstyle ':completion:*' path-completion false
	zstyle ':completion:*' max-errors 0 not-numeric

	bindkey '^I' autosuggest-capture-completion
}

_zsh_autosuggest_capture_completion_sync() {
	_zsh_autosuggest_capture_setup

	zle autosuggest-capture-completion
}

_zsh_autosuggest_capture_completion_async() {
	_zsh_autosuggest_capture_setup

	zmodload zsh/parameter 2>/dev/null || return # For `$functions`

	# Make vared completion work as if for a normal command line
	# https://stackoverflow.com/a/7057118/154703
	autoload +X _complete
	functions[_original_complete]=$functions[_complete]
	function _complete() {
		unset 'compstate[vared]'
		_original_complete "$@"
	}

	# Open zle with buffer set so we can capture completions for it
	vared 1
}

_zsh_autosuggest_strategy_completion() {
	# Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable extended glob for completion ignore pattern
	setopt EXTENDED_GLOB

	typeset -g suggestion
	local line REPLY

	# Exit if we don't have completions
	whence compdef >/dev/null || return

	# Exit if we don't have zpty
	zmodload zsh/zpty 2>/dev/null || return

	# Exit if our search string matches the ignore pattern
	[[ -n "$ZSH_AUTOSUGGEST_COMPLETION_IGNORE" ]] && [[ "$1" == $~ZSH_AUTOSUGGEST_COMPLETION_IGNORE ]] && return

	# Zle will be inactive if we are in async mode
	if zle; then
		zpty $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME _zsh_autosuggest_capture_completion_sync
	else
		zpty $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME _zsh_autosuggest_capture_completion_async "\$1"
		zpty -w $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME $'\t'
	fi

	{
		# The completion result is surrounded by null bytes, so read the
		# content between the first two null bytes.
		zpty -r $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME line '*'$'\0''*'$'\0'

		# Extract the suggestion from between the null bytes.  On older
		# versions of zsh (older than 5.3), we sometimes get extra bytes after
		# the second null byte, so trim those off the end.
		# See http://www.zsh.org/mla/workers/2015/msg03290.html
		suggestion="${${(@0)line}[2]}"
	} always {
		# Destroy the pty
		zpty -d $ZSH_AUTOSUGGEST_COMPLETIONS_PTY_NAME
	}
}
```

## File: `src/strategies/history.zsh`
```

#--------------------------------------------------------------------#
# History Suggestion Strategy                                        #
#--------------------------------------------------------------------#
# Suggests the most recent history item that matches the given
# prefix.
#

_zsh_autosuggest_strategy_history() {
	# Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable globbing flags so that we can use (#m) and (x~y) glob operator
	setopt EXTENDED_GLOB

	# Escape backslashes and all of the glob operators so we can use
	# this string as a pattern to search the $history associative array.
	# - (#m) globbing flag enables setting references for match data
	# TODO: Use (b) flag when we can drop support for zsh older than v5.0.8
	local prefix="${1//(#m)[\\*?[\]<>()|^~#]/\\$MATCH}"

	# Get the history items that match the prefix, excluding those that match
	# the ignore pattern
	local pattern="$prefix*"
	if [[ -n $ZSH_AUTOSUGGEST_HISTORY_IGNORE ]]; then
		pattern="($pattern)~($ZSH_AUTOSUGGEST_HISTORY_IGNORE)"
	fi

	# Give the first history item matching the pattern as the suggestion
	# - (r) subscript flag makes the pattern match on values
	typeset -g suggestion="${history[(r)$pattern]}"
}
```

## File: `src/strategies/match_prev_cmd.zsh`
```

#--------------------------------------------------------------------#
# Match Previous Command Suggestion Strategy                         #
#--------------------------------------------------------------------#
# Suggests the most recent history item that matches the given
# prefix and whose preceding history item also matches the most
# recently executed command.
#
# For example, suppose your history has the following entries:
#   - pwd
#   - ls foo
#   - ls bar
#   - pwd
#
# Given the history list above, when you type 'ls', the suggestion
# will be 'ls foo' rather than 'ls bar' because your most recently
# executed command (pwd) was previously followed by 'ls foo'.
#
# Note that this strategy won't work as expected with ZSH options that don't
# preserve the history order such as `HIST_IGNORE_ALL_DUPS` or
# `HIST_EXPIRE_DUPS_FIRST`.

_zsh_autosuggest_strategy_match_prev_cmd() {
	# Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable globbing flags so that we can use (#m) and (x~y) glob operator
	setopt EXTENDED_GLOB

	# TODO: Use (b) flag when we can drop support for zsh older than v5.0.8
	local prefix="${1//(#m)[\\*?[\]<>()|^~#]/\\$MATCH}"

	# Get the history items that match the prefix, excluding those that match
	# the ignore pattern
	local pattern="$prefix*"
	if [[ -n $ZSH_AUTOSUGGEST_HISTORY_IGNORE ]]; then
		pattern="($pattern)~($ZSH_AUTOSUGGEST_HISTORY_IGNORE)"
	fi

	# Get all history event numbers that correspond to history
	# entries that match the pattern
	local history_match_keys
	history_match_keys=(${(k)history[(R)$~pattern]})

	# By default we use the first history number (most recent history entry)
	local histkey="${history_match_keys[1]}"

	# Get the previously executed command
	local prev_cmd="$(_zsh_autosuggest_escape_command "${history[$((HISTCMD-1))]}")"

	# Iterate up to the first 200 history event numbers that match $prefix
	for key in "${(@)history_match_keys[1,200]}"; do
		# Stop if we ran out of history
		[[ $key -gt 1 ]] || break

		# See if the history entry preceding the suggestion matches the
		# previous command, and use it if it does
		if [[ "${history[$((key - 1))]}" == "$prev_cmd" ]]; then
			histkey="$key"
			break
		fi
	done

	# Give back the matched history entry
	typeset -g suggestion="$history[$histkey]"
}
```

