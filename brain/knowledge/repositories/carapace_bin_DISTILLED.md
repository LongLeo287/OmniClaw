---
id: repo-fetched-carapace-bin-151736
type: knowledge
owner: OA
registered_at: 2026-04-05T04:05:52.727786
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_carapace-bin_151736

## Assimilation Report
Auto-cloned repository: FETCHED_carapace-bin_151736

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# carapace-bin

[![PkgGoDev](https://pkg.go.dev/badge/github.com/carapace-sh/carapace-bin/pkg/actions)](https://pkg.go.dev/github.com/carapace-sh/carapace-bin/pkg/actions)
[![GoReportCard](https://goreportcard.com/badge/github.com/carapace-sh/carapace-bin)](https://goreportcard.com/report/github.com/carapace-sh/carapace-bin)
[![documentation](https://img.shields.io/badge/&zwnj;-documentation-blue?logo=gitbook)](https://carapace-sh.github.io/carapace-bin/)
[![Completers](https://carapace-sh.github.io/carapace-bin/badge.svg)](https://carapace-sh.github.io/carapace-bin/completers.html)
[![Macros](https://carapace-sh.github.io/carapace-bin/macros-badge.svg)](https://carapace-sh.github.io/carapace-bin/spec/macros.html)
[![Packaging status](https://repology.org/badge/tiny-repos/carapace.svg)](https://repology.org/project/carapace/versions)
[![faq](https://img.shields.io/badge/discussions-faq-white)](https://github.com/orgs/carapace-sh/discussions?discussions_q=label%3Afaq)

Carapace-bin provides argument completion for multiple CLI commands ([full list](https://carapace-sh.github.io/carapace-bin/completers.html)), and works across multiple POSIX and non-POSIX shells.

![](./docs/src/opengraph-elvish.png)

Supported shells:
- [Bash](https://www.gnu.org/software/bash/)
- [Cmd](https://en.wikipedia.org/wiki/Cmd.exe) ([experimental](https://github.com/carapace-sh/carapace/issues/1107))
- [Elvish](https://elv.sh/)
- [Fish](https://fishshell.com/)
- [Ion](https://doc.redox-os.org/ion-manual/) ([experimental](https://github.com/carapace-sh/carapace/issues/88))
- [Nushell](https://www.nushell.sh/)
- [Oil](http://oils.pub/)
- [Powershell](https://microsoft.com/powershell)
- [Tcsh](https://www.tcsh.org/) ([experimental](https://github.com/carapace-sh/carapace/issues/331))
- [Xonsh](https://xon.sh/)
- [Zsh](https://www.zsh.org/)

## Getting Started

[Read], [Install] and [Setup].

[Read]:https://pixi.carapace.sh
[Install]:https://carapace-sh.github.io/carapace-bin/install.html
[Setup]:https://carapace-sh.github.io/carapace-bin/setup.html

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for carapace_bin
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\src\carapace-bin.md
```md
# carapace-bin

[carapace-bin](https://github.com/carapace-sh/carapace-bin) is a multi-shell multi-command argument completer based on [carapace-sh/carapace](https://github.com/carapace-sh/carapace).

![](./opengraph-elvish.png)

Supported shells:
- [Bash](https://www.gnu.org/software/bash/)
- [Elvish](https://elv.sh/)
- [Fish](https://fishshell.com/)
- [Ion](https://doc.redox-os.org/ion-manual/) ([experimental](https://github.com/carapace-sh/carapace/issues/88))
- [Nushell](https://www.nushell.sh/)
- [Oil](http://oils.pub/)
- [Powershell](https://microsoft.com/powershell)
- [Tcsh](https://www.tcsh.org/) ([experimental](https://github.com/carapace-sh/carapace/issues/331))
- [Xonsh](https://xon.sh/)
- [Zsh](https://www.zsh.org/)

```

### File: docs\src\choices.md
```md
# Choices

The **default priority** of completers can be **overridden** with `carapace --choice {name}[/{variant}][@{group}]`.

![](./choices/choices.cast)

> Choices are stored as simple text files in your [config directory](setup/userConfigDir.html).
> ```sh
> carapace
> └── choices
>     ├── sed  # sed@bsd
>     └── tldr # tldr/tldr-python-client
> ```

## Bridges

[Bridges](https://github.com/carapace-sh/carapace-bridge) are a special form of choices as they can be added as **additional completers** otherwise unknown.

![](./choices/bridges.cast)

> With [CARAPACE_BRIDGES](setup/environment.html#carapace_bridges) completers from `zsh`, `fish`, `bash`, and `inshellisense` can largely determined and act as implicit fallback.
> But frameworks like [cobra](setup/environment.html#carapace_bridges) need to be set explicitly.


Currently available bridges:
- [argcomplete](https://github.com/kislyuk/argcomplete)
- [argcomplete_v1](https://github.com/kislyuk/argcomplete) (legacy)
- [aws](https://github.com/aws/aws-cli)
- [bash](https://www.gnu.org/software/bash/)
- [carapace](https://github.com/carapace-sh/carapace)
- [clap](https://github.com/clap-rs/clap) (experimental - needs [clap-rs/clap#3166](https://github.com/clap-rs/clap/issues/3166))
- [click](https://github.com/pallets/click)
- [cobra](https://github.com/spf13/cobra)
- [complete](https://github.com/posener/complete)
- [fish](https://fishshell.com/)
- [inshellisense](https://github.com/microsoft/inshellisense)
- [jj](https://www.jj-vcs.dev)
- [kingpin](https://github.com/alecthomas/kingpin)
- [kitten](https://github.com/kovidgoyal/kitty)
- [powershell](https://microsoft.com/powershell)
- [urfavecli](https://github.com/urfave/cli)
- [urfavecli_v1](https://github.com/urfave/cli) (legacy)
- [yargs](https://github.com/yargs/yargs)
- [zsh](https://www.zsh.org/)

> Bridging frameworks should be preferred to shells (e.g. `zsh`) as these generally work better and have less overhead.

```

### File: docs\src\completers.md
```md
# Completers

_filled automatically_

```

### File: docs\src\development.md
```md
# Development

```

### File: docs\src\groups.md
```md
# Groups

Completers are organized into **groups**.

- `android` termux completers
- `bridge` bridged completers
- `bsd` bsd-like completers
- `common` common completers
- `darwin` macos completers
- `linux` linux completers
- `unix` unix-like completers
- `user` user specs
- `system` system specs
- `windows` windows completers

You can **list** available completers of a **group** with `carapace --list @{group}`.

![](./groups/group.cast)

> Binaries only contain **relevant groups** unless built with the [build tag](https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags) `force_all`.

## Priority

Multiple **groups** providing a completer for a command are ordered by **priority**.

- darwin
  1. `user`
  1. `system`
  1. `darwin`
  1. `bsd`
  1. `unix`
  1. `common`
  1. `bridge`

- linux
  1. `user`
  1. `system`
  1. `linux`
  1. `unix`
  1. `common`
  1. `bridge`

- termux
  1. `user`
  1. `system`
  1. `android`
  1. `linux`
  1. `unix`
  1. `common`
  1. `bridge`

- windows
  1. `user`
  1. `system`
  1. `windows`
  1. `common`
  1. `bridge`


You can **list** available completers of a **command** with `carapace --list {command}`.

![](./groups/priority.cast)

```

### File: docs\src\install.md
```md
# Install

## Manually

Download from [releases](https://github.com/carapace-sh/carapace-bin/releases) and add `carapace` to [PATH](https://en.wikipedia.org/wiki/PATH_(variable)).

## AUR

Install [carapace-bin](https://aur.archlinux.org/packages/carapace-bin/) from [AUR](https://aur.archlinux.org/).

```sh
# e.g. with pamac
pamac install carapace-bin
```

## DEB

Install from [fury.io](https://rsteube.fury.site/)

```toml
# /etc/apt/sources.list.d/fury.list
deb [trusted=yes] https://apt.fury.io/rsteube/ /
```

```sh
apt-get update && apt-get install carapace-bin
```

## Homebrew

Install from [homebrew-core](https://formulae.brew.sh/formula/carapace)

```sh
brew install carapace
```

---

Install from [rsteube/homebrew-tap](https://github.com/rsteube/homebrew-tap)

```sh
brew tap rsteube/homebrew-tap
brew install rsteube/tap/carapace
```

## Mise [mise](https://github.com/jdx/mise)

```sh
mise use -g carapace@latest
```

## Nix

Install from [nixpkgs](https://search.nixos.org/packages?show=carapace)

```sh
nix-shell -p carapace
```

## PKGX

Install from [pkgx.dev](https://pkgx.dev/pkgs/carapace.sh/)

```sh
pkgx install carapace
```

## RPM

Install from [fury.io](https://rsteube.fury.site/)

### Yum

```toml
# /etc/yum.repos.d/fury.repo
[fury]
name=Gemfury Private Repo
baseurl=https://yum.fury.io/rsteube/
enabled=1
gpgcheck=0
```

```sh
yum install carapace-bin
```

### Zypper

```sh
zypper ar --gpgcheck-allow-unsigned -f https://yum.fury.io/rsteube/ carapace
zypper install carapace-bin
```

## Scoop

Install from [ScoopInstaller/Extras](https://github.com/ScoopInstaller/Extras) (**recommended**)

```sh
scoop bucket add extras
scoop install extras/carapace-bin
```

---

Install from [rsteube/scoop-bucket](https://github.com/rsteube/scoop-bucket)

```sh
scoop bucket add rsteube https://github.com/rsteube/scoop-bucket.git
scoop install carapace-bin
```

## Termux

Install from [termux/termux-packages](https://github.com/termux/termux-packages)

```sh
pkg install carapace
```

---

Install from [carapace-sh/termux](https://github.com/carapace-sh/termux) (gh_pages)
> **WIP**: repo currently manually created

### Manually

```sh
# $PREFIX/etc/apt/sources.list.d
deb [trusted=yes] https://termux.carapace.sh termux extras  
```

```sh
apt update && apt install carapace-bin
```

### Script
```sh
curl termux.carapace.sh | sh
```

## Winget

Install from [winget-pkgs](https://github.com/microsoft/winget-pkgs)

```sh
winget install -e --id rsteube.Carapace
```

## X-CMD

Install from [x-cmd.com](https://www.x-cmd.com/pkg/carapace-bin)

```sh
x env use carapace-bin
```

```

### File: docs\src\overlay.md
```md
# Overlay

Overlays are essentially [Spec] files placed in [`${UserConfigDir}/carapace/overlays`] that provide additional completions.
These are merged with the existing completion and provide a workaround for issues that have yet to be fixed in upstream.

> Overlays implicitly set `CARAPACE_LENIENT` to allow unknown flags.

## Flag

```yaml
# ${UserConfigDir}/carapace/overlays/doctl.yaml
name: doctl
persistentflags:
  --output=: Desired output format [text|json]
completion:
  flag:
    output: [text, json]
commands:
  - name: compute
    description: Display commands that manage infrastructure
    commands:
      - name: region
        description: Display commands to list datacenter regions
        commands:
          - name: list
            description: List datacenter regions
            flags:
              --format=: Columns for output in a comma-separated list
            completion:
              flag:
                format: ["$uniquelist(,)", Slug, Name, Available]
```

![](./overlay-flag.cast)

## Command

```yaml
# ${UserConfigDir}/carapace/overlays/doctl.yaml
name: doctl
commands:
  - name: auth
    description: Display commands for authenticating doctl with an account
    group: management

  - name: compute
    description: Display commands that manage infrastructure
    group: core

  - name: custom
    description: custom command
    group: custom
    flags:
      -h, --help: show help
    completion:
      positional:
        - [one, two, three]
```

![](./overlay-command.cast)

[Spec]:./spec.md
[`${UserConfigDir}/carapace/overlays`]:https://pkg.go.dev/os#UserConfigDir

```

### File: docs\src\release_notes.md
```md
# Release Notes

Release notes contain _noteworthy_ changes between **minor** (`1.x`) releases.

> These aren't strictly pinned to **tags**.
> So a feature announced as `1.n` might already be present in a previous (`1.{n-1}.x`) or added in a later (`1.n.x`) **patch** release.
>
> See [releases](https://github.com/carapace-sh/carapace-bin/releases) for an exact changelog.

```

### File: docs\src\setup.md
```md
# Setup

> This registers all the available [completers](./completers.md).
> It is also possible to load a single one by replacing `_carapace` with the completer name (e.g. `carapace chmod`).

> **See [UserConfigDir](./setup/userConfigDir.md) for details.**

## Bash

```sh
# ~/.bashrc
export CARAPACE_BRIDGES='zsh,fish,bash,inshellisense' # optional
source <(carapace _carapace)
```

![](./setup-bash.png)

## Cmd

```lua
# ~/AppData/Local/clink/carapace.lua
load(io.popen('carapace _carapace cmd-clink'):read("*a"))()
```

![](./setup-cmd.png)

> Needs [clink](https://chrisant996.github.io/clink/).

## Elvish

```sh
# ${UserConfigDir}/elvish/rc.elv
set-env CARAPACE_BRIDGES 'zsh,fish,bash,inshellisense' # optional
eval (carapace _carapace|slurp)
```

![](./setup-elvish.png)

## Fish

```sh
# ${UserConfigDir}/fish/config.fish
set -Ux CARAPACE_BRIDGES 'zsh,fish,bash,inshellisense' # optional
carapace _carapace | source
```

![](./setup-fish.png)

## Nushell

```sh
## ${UserConfigDir}/nushell/env.nu
$env.CARAPACE_BRIDGES = 'zsh,fish,bash,inshellisense' # optional
mkdir $"($nu.cache-dir)"
carapace _carapace nushell | save --force $"($nu.cache-dir)/carapace.nu"

# ${UserConfigDir}/nushell/config.nu
source $"($nu.cache-dir)/carapace.nu"
```

![](./setup-nushell.png)

## Oil

```sh
# ${UserConfigDir}/oil/oshrc
export CARAPACE_BRIDGES='zsh,fish,bash,inshellisense' # optional
source <(carapace _carapace)
```

![](./setup-oil.png)

## Powershell

```sh
# ${UserConfigDir}/powershell/Microsoft.PowerShell_profile.ps1
$env:CARAPACE_BRIDGES = 'zsh,fish,bash,inshellisense' # optional
Set-PSReadLineOption -Colors @{ "Selection" = "`e[7m" }
Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete
carapace _carapace | Out-String | Invoke-Expression
```

> **Note:** The `Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete` line is **required**.
> The default `Complete` function (used by PSReadLine's `Emacs` edit mode) will display raw ANSI escape codes
> (e.g. `^[[21;22;23;24;25;29m^[[39;49m`) in the prompt instead of styled completions.
>
> If you use `Set-PSReadLineOption -EditMode Emacs`, make sure it is placed **before** the
> `Set-PSReadlineKeyHandler` line above, as it resets key bindings and would override the `Tab` binding
> back to `Complete`.

![](./setup-powershell.png)

## Tcsh
```sh
# ~/.tcshrc
setenv CARAPACE_BRIDGES 'zsh,fish,bash,inshellisense' # optional
set autolist
eval `carapace _carapace`
```

![](./setup-tcsh.png)

## Xonsh
```sh
# ${UserConfigDir}/xonsh/rc.xsh
$CARAPACE_BRIDGES='zsh,fish,bash,inshellisense' # optional
$COMPLETIONS_CONFIRM=True
exec($(carapace _carapace))
```

![](./setup-xonsh.png)

## Zsh

```sh
# ${UserConfigDir}/zsh/.zshrc
autoload -U compinit && compinit
export CARAPACE_BRIDGES='zsh,fish,bash,inshellisense' # optional
zstyle ':completion:*' format $'\e[2;37mCompleting %d\e[m'
source <(carapace _carapace)
```

Order of groups can be configured with the zstyle [group-order](https://zsh.sourceforge.io/Guide/zshguide06.html).
```sh
zstyle ':completion:*:git:*' group-order 'main commands' 'alias commands' 'external commands'
```

![](./setup-zsh.png)

```

### File: docs\src\spec.md
```md
# Spec

Custom completions can be defined using yaml files.

> see [carapace-spec] for more documentation

```yaml
# yaml-language-server: $schema=https://carapace.sh/schemas/command.json
name: mycmd
description: my command
flags:
  --optarg?: optarg flag
  -r, --repeatable*: repeatable flag
  -v=: flag with value
persistentflags:
  --help: bool flag
completion:
  flag:
    optarg: ["one", "two\twith description", "three\twith style\tblue"]
    v: ["$files"]
commands:
- name: sub
  description: subcommand
  completion:
    positional:
      - ["$list(,)", "1", "2", "3"]
      - ["$directories"]
```

![](./spec.cast)

## Custom Macros

Carapace provides a range of [custom macros](./spec/macros.md):

```sh
carapace --macro                       # list macros
carapace --macro color.HexColors       # show macro details
carapace --macro color.HexColors <TAB> # test macro
```

![](./spec-macros.cast)


[carapace-spec]:https://carapace-sh.github.io/carapace-spec

```

### File: docs\src\style.md
```md
# Style

[Transformations](#transformations) can be applied to files and specific values.
 
> This is only supported in [elvish], [nushell], [powershell], [xonsh] and [zsh].

## File

Files can be styled with the `LS_COLORS` environment variable (e.g. using [vivid]):

```sh
# elvish
set-env LS_COLORS (vivid generate dracula)

# powershell
$env:LS_COLORS = (vivid generate dracula)

# zsh
export LS_COLORS=$(vivid generate dracula)
```

![](./style-filename.cast)

## Value

Values can be styled with a comma separated list of [transformations](#transformations):

```sh
# set
carapace --style 'carapace.Value=bold,magenta'

# clear
carapace --style 'carapace.Description='
```

![](./style-value.cast)

> Generic configuration like default value and description style can be found under `carapace.{key}`

## Scheme

How the default colors look depends on your [terminal color scheme](https://github.com/rsteube/vincent).

> It is recommended to choose one with a high contrast so that every color is [well readable](https://gogh-co.github.io/Gogh/).

![](./style-scheme.cast)


## Transformations

Transformations are adopted from [elvish](https://elv.sh/ref/builtin.html#styled):

> Each `$style-transformer` can be one of the following:
> - A boolean attribute name:
>   - One of `bold`, `dim`, `italic`, `underlined`, `blink` and `inverse` for
>     setting the corresponding attribute.
>   - An attribute name prefixed by `no-` for unsetting the attribute.
>   - An attribute name prefixed by `toggle-` for toggling the attribute
>     between set and unset.
> - A color name for setting the text color, which may be one of the
>   following:
>   - One of the 8 basic ANSI colors: `black`, `red`, `green`, `yellow`,
>     `blue`, `magenta`, `cyan` and `white`.
>   - The bright variant of the 8 basic ANSI colors, with a `bright-` prefix.
>   - Any color from the xterm 256-color palette, as `colorX` (such as
>     `color12`).
>   - A 24-bit RGB color written as `#RRGGBB` (such as `'#778899'`).
>     **Note**: You need to quote such values, since an unquoted `#` introduces
>     a comment (e.g. use `'bg-#778899'` instead of `bg-#778899`).
> - A color name prefixed by `fg-` to set the foreground color. This has
>   the same effect as specifying the color name without the `fg-` prefix.
> - A color name prefixed by `bg-` to set the background color.


[Elvish]:https://elv.sh/
[Nushell]:https://nushell.sh/
[Powershell]:https://microsoft.com/powershell
[vivid]:https://github.com/sharkdp/vivid
[Xonsh]:https://xon.sh/
[Zsh]:https://www.zsh.org/

```

### File: docs\src\SUMMARY.md
```md
# Summary

- [carapace-bin](./carapace-bin.md)
  - [Install](./install.md)
    - [Selfupdate](./install/selfupdate.md)
  - [Setup](./setup.md)
    - [Environment](./setup/environment.md)
    - [UserConfigDir](./setup/userConfigDir.md)
  - [Groups](./groups.md)
  - [Variants](./variants.md)
  - [Choices](./choices.md)
  - [Completers](./completers.md)
  - [Style](./style.md)
  - [Spec](./spec.md)
    - [User](./spec/user.md)
    - [Bridge](./spec/bridge.md)
    - [Embed](./spec/embed.md)
    - [Run](./spec/run.md)
    - [Shim](./spec/shim.md)
    - [Scrape](./spec/scrape.md)
    - [Codegen](./spec/codegen.md)
    - [Examples](./spec/examples.md)
    - [Macros](./spec/macros.md)
  - [Overlay](./overlay.md)
  - [Variable](./variable.md)
    - [Conditions](./variable/conditions.md)
  - [Development](./development.md)
    - [Project Layout](./development/projectLayout.md)
    - [Build](./development/build.md)
    - [Docker](./development/docker.md)
    - [Creating Completers](./development/creatingCompleters.md)
      - [Manually](./development/creatingCompleters/manually.md)
      - [Parsing](./development/creatingCompleters/parsing.md)
      - [Scraping](./development/creatingCompleters/scraping.md)
      - [Examples](./development/creatingCompleters/examples.md)
    - [Updating Completers](./development/updatingCompleters.md)
    - [Best Practices](./development/bestPractices.md)
      - [Coupled Actions](./development/bestPractices/coupledActions.md)
    - [Tools](./development/tools.md)
      - [carapace-fmt](./development/tools/carapace-fmt.md)
      - [carapace-lint](./development/tools/carapace-lint.md)
      - [carapace-parse](./development/tools/carapace-parse.md)
      - [carapace-generate](./development/tools/carapace-generate.md)
  - [Release Notes](./release_notes.md)
    - [v1.x](./release_notes/v1.x.md)
    - [v1.6](./release_notes/v1.6.md)
    - [v1.5](./release_notes/v1.5.md)
    - [v1.4](./release_notes/v1.4.md)
    - [v1.3](./release_notes/v1.3.md)
    - [v1.2](./release_notes/v1.2.md)
    - [v1.1](./release_notes/v1.1.md)
    - [v1.0](./release_notes/v1.0.md)
    - [v0.30](./release_notes/v0.30.md)
    - [v0.29](./release_notes/v0.29.md)
    - [v0.28](./release_notes/v0.28.md)
    - [v0.27](./release_notes/v0.27.md)
    - [v0.26](./release_notes/v0.26.md)
    - [v0.25](./release_notes/v0.25.md)
    - [v0.24](./release_notes/v0.24.md)
    - [v0.23](./release_notes/v0.23.md)
    - [v0.22](./release_notes/v0.22.md)
    - [v0.21](./release_notes/v0.21.md)
    - [v0.20](./release_notes/v0.20.md)
    - [v0.19](./release_notes/v0.19.md)
    - [v0.18](./release_notes/v0.18.md)
    - [v0.17](./release_notes/v0.17.md)
    - [v0.16](./release_notes/v0.16.md)
    - [v0.15](./release_notes/v0.15.md)
    - [v0.14](./release_notes/v0.14.md)
    - [v0.13](./release_notes/v0.13.md)
    - [v0.12](./release_notes/v0.12.md)
    - [v0.11](./release_notes/v0.11.md)

```

### File: docs\src\variable.md
```md
# Variable

Complex environment variable completion is provided with `get-env`, `set-env` and `unset-env`.

In `elvish` the completion is simply overridden.
For other shells custom functions are added.

> Setting `CARAPACE_ENV=0` before sourcing `carapace _carapace` disables this behaviour.

![](./variable.cast)

## Custom variables

Custom variables can be defined in `${UserConfigDir}/carapace/variables/{group}.yaml`

```yaml
variables:
  CUSTOM_EXAMPLE: example environment variable
  CUSTOM_MACRO: macro example
  HTTPS_PROXY: override existing variable
completion:
  variable:
    CUSTOM_EXAMPLE: ["0\tdisabled\tred", "1\tenabled\tgreen"]
    CUSTOM_MACRO: ["$carapace.tools.gh.Labels({owner: rsteube, name: carapace}) ||| $uniquelist(,)"]
    HTTPS_PROXY: ["https://localhost:8443\tdevelopment", "https://proxy.company:443\tproduction"]
```

![](./variable-custom.cast)

It is also possible to define conditions.

```yaml
condition: ["$Parent([.git])"]
variables:
  CUSTOM_CONDITION: condition example
completion:
  variable:
    CUSTOM_CONDITION: ["within", "git", "repo"]
```

![](./variable-condition.cast)

```

### File: docs\src\variants.md
```md
# Variants

[Groups](./groups.md) can contain multiple completers for the same command.


You can **list** available **variants** for a command with `carapace --list {name}[/{variant}][@{group}]`.

![](./variants/variants.cast)

## Priority

Multiple **variants** within the same group are ordered by **name**.

- tldr
  1. `tealdeer`
  1. `tldr-python-client`

```

