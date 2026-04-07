---
id: just
type: knowledge
owner: OA_Triage
---
# just
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align=right>Table of Contents↗️</div>

<h1 align=center><code>just</code></h1>

<div align=center>
  <a href=https://crates.io/crates/just>
    <img src=https://img.shields.io/crates/v/just.svg alt="crates.io version">
  </a>
  <a href=https://github.com/casey/just/actions/workflows/ci.yaml>
    <img src=https://github.com/casey/just/actions/workflows/ci.yaml/badge.svg alt="build status">
  </a>
  <a href=https://github.com/casey/just/releases>
    <img src=https://img.shields.io/github/downloads/casey/just/total.svg alt=downloads>
  </a>
  <a href=https://discord.gg/ezYScXR>
    <img src=https://img.shields.io/discord/695580069837406228?logo=discord alt="chat on discord">
  </a>
  <a href=mailto:casey@rodarmor.com?subject=Thanks%20for%20Just!>
    <img src=https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg alt="say thanks">
  </a>
</div>
<br>

`just` is a handy way to save and run project-specific commands.

This readme is also available as a [book](https://just.systems/man/en/). The
book reflects the latest release, whereas the
[readme on GitHub](https://github.com/casey/just/blob/master/README.md)
reflects latest master.

(中文文档在 [这里](https://github.com/casey/just/blob/master/README.中文.md),
快看过来!)

Commands, called recipes, are stored in a file called `justfile` with syntax
inspired by `make`:

![screenshot](https://raw.githubusercontent.com/casey/just/master/etc/screenshot.png)

You can then run them with `just RECIPE`:

```console
$ just test-all
cc *.c -o main
./test --all
Yay, all your tests passed!
```

`just` has a ton of useful features, and many improvements over `make`:

- `just` is a command runner, not a build system, so it avoids much of
  [`make`'s complexity and idiosyncrasies](#what-are-the-idiosyncrasies-of-make-that-just-avoids).
  No need for `.PHONY` recipes!

- Linux, MacOS, Windows, and other reasonable unices are supported with no
  additional dependencies. (Although if your system doesn't have an `sh`,
  you'll need to [choose a different shell](#shell).)

- Errors are specific and informative, and syntax errors are reported along
  with their source context.

- Recipes can accept [command line arguments](#recipe-parameters).

- Wherever possible, errors are resolved statically. Unknown recipes and
  circular dependencies are reported before anything runs.

- `just` [loads `.env` files](#dotenv-settings), making it easy to populate
  environment variables.

- Recipes can be [listed from the command line](#listing-available-recipes).

- Command line completion scripts are
  [available for most popular shells](#shell-completion-scripts).

- Recipes can be written in
  [arbitrary languages](#shebang-recipes), like Python or NodeJS.

- `just` can be invoked from any subdirectory, not just the directory that
  contains the `justfile`.

- And [much more](https://just.systems/man/en/)!

If you need help with `just` please feel free to open an issue or ping me on
[Discord](https://discord.gg/ezYScXR). Feature requests and bug reports are
always welcome!

Installation
------------

Just can be installed using your favorite [package manager](#packages), by
downloading [pre-built binaries](#pre-built-binaries), or building from source
with `cargo install just`.

### Prerequisites

`just` should run on any system with a reasonable `sh`, including Linux, MacOS,
and the BSDs.

#### Windows

On Windows, `just` works with the `sh` provided by
[Git for Windows](https://git-scm.com),
[GitHub Desktop](https://desktop.github.com), or
[Cygwin](http://www.cygwin.com). After installation, `sh` must be available in
the `PATH` of the shell you want to invoke `just` from.

If you'd rather not install `sh`, you can use the `shell` setting to use the
shell of your choice.

Like PowerShell:

```just
# use PowerShell instead of sh:
set shell := ["powershell.exe", "-c"]

hello:
  Write-Host "Hello, world!"
```

…or `cmd.exe`:

```just
# use cmd.exe instead of sh:
set shell := ["cmd.exe", "/c"]

list:
  dir
```

You can also set the shell using command-line arguments. For example, to use
PowerShell, launch `just` with `--shell powershell.exe --shell-arg -c`.

(PowerShell is installed by default on Windows 7 SP1 and Windows Server 2008 R2
S1 and later, and `cmd.exe` is quite fiddly, so PowerShell is recommended for
most Windows users.)

### Packages

#### Cross-platform

<table>
  <thead>
    <tr>
      <th>Package Manager</th>
      <th>Package</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href=https://github.com/alexellis/arkade>arkade</a></td>
      <td>just</td>
      <td><code>arkade get just</code></td>
    </tr>
    <tr>
      <td><a href=https://asdf-vm.com>asdf</a></td>
      <td><a href=https://github.com/olofvndrhr/asdf-just>just</a></td>
      <td>
        <code>asdf plugin add just</code><br>
        <code>asdf install just &lt;version&gt;</code>
      </td>
    </tr>
    <tr>
      <td><a href=https://www.rust-lang.org>Cargo</a></td>
      <td><a href=https://crates.io/crates/just>just</a></td>
      <td><code>cargo install just</code></td>
    </tr>
    <tr>
      <td><a href=https://github.com/cargo-bins/cargo-binstall>Cargo Binstall</a></td>
      <td><a href=https://crates.io/crates/just>just</a></td>
      <td><code>cargo binstall just</code></td>
    </tr>
    <tr>
      <td><a href=https://docs.conda.io/projects/conda/en/latest/index.html>Conda</a></td>
      <td><a href=https://anaconda.org/conda-forge/just>just</a></td>
      <td><code>conda install -c conda-forge just</code></td>
    </tr>
    <tr>
      <td><a href=https://brew.sh>Homebrew</a></td>
      <td><a href=https://formulae.brew.sh/formula/just>just</a></td>
      <td><code>brew install just</code></td>
    </tr>
    <tr>
      <td><a href=https://nixos.org/nix/>Nix</a></td>
      <td><a href=https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/ju/just/package.nix>just</a></td>
      <td><code>nix-env -iA nixpkgs.just</code></td>
    </tr>
    <tr>
      <td><a href=https://www.npmjs.com/>npm</a></td>
      <td><a href=https://www.npmjs.com/package/rust-just>rust-just</a></td>
      <td><code>npm install -g rust-just</code></td>
    </tr>
    <tr>
      <td><a href=https://pipx.pypa.io/stable/>pipx</a></td>
      <td><a href=https://pypi.org/project/rust-just/>rust-just</a></td>
      <td><code>pipx install rust-just</code></td>
    </tr>
    <tr>
      <td><a href=https://snapcraft.io>Snap</a></td>
      <td><a href=https://snapcraft.io/just>just</a></td>
      <td><code>snap install --edge --classic just</code></td>
    </tr>
    <tr>
      <td><a href=https://docs.astral.sh/uv/>uv</a></td>
      <td><a href=https://pypi.org/project/rust-just/>rust-just</a></td>
      <td><code>uv tool install rust-just</code></td>
    </tr>
  </tbody>
</table>

#### BSD

<table>
  <thead>
    <tr>
      <th>Operating System</th>
      <th>Package Manager</th>
      <th>Package</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href=https://www.freebsd.org>FreeBSD</a></td>
      <td><a href=https://www.freebsd.org/doc/handbook/pkgng-intro.html>pkg</a></td>
      <td><a href=https://www.freshports.org/deskutils/just/>just</a></td>
      <td><code>pkg install just</code></td>
    </tr>
    <tr>
      <td><a href=https://www.openbsd.org>OpenBSD</a></td>
      <td><a href=https://www.openbsd.org/faq/faq15.html>pkg_*</a></td>
      <td><a href=https://cvsweb.openbsd.org/cgi-bin/cvsweb/ports/sysutils/just>just</a></td>
      <td><code>pkg_add just</code></td>
    </tr>
  </tbody>
</table>

#### Linux

<table>
  <thead>
    <tr>
      <th>Operating System</th>
      <th>Package Manager</th>
      <th>Package</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href=https://alpinelinux.org>Alpine</a></td>
      <td><a href=https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>apk-tools</a></td>
      <td><a href=https://pkgs.alpinelinux.org/package/edge/community/x86_64/just>just</a></td>
      <td><code>apk add just</code></td>
    </tr>
    <tr>
      <td><a href=https://www.archlinux.org>Arch</a></td>
      <td><a href=https://wiki.archlinux.org/title/Pacman>pacman</a></td>
      <td><a href=https://archlinux.org/packages/extra/x86_64/just/>just</a></td>
      <td><code>pacman -S just</code></td>
    </tr>
    <tr>
      <td>
        <a href=https://debian.org>Debian 13</a> and
        <a href=https://ubuntu.com>Ubuntu 24.04</a> derivatives</td>
      <td><a href=https://en.wikipedia.org/wiki/APT_(software)>apt</a></td>
      <td><a href=https://packages.debian.org/trixie/just>just</a></td>
      <td><code>apt install just</code></td>
    </tr>
    <tr>
      <td><a href=https://getfedora.org>Fedora</a></td>
      <td><a href=https://dnf.readthedocs.io/en/latest/>DNF</a></td>
      <td><a href=https://src.fedoraproject.org/rpms/rust-just>just</a></td>
      <td><code>dnf install just</code></td>
    </tr>
    <tr>
      <td><a href=https://www.gentoo.org>Gentoo</a></td>
      <td><a href=https://wiki.gentoo.org/wiki/Portage>Portage</a></td>
      <td><a href=https://packages.gentoo.org/packages/dev-build/just>dev-build/just</a></td>
      <td>
        <code>emerge -av dev-build/just</code>
      </td>
    </tr>
    <tr>
      <td><a href=https://nixos.org/nixos/>NixOS</a></td>
      <td><a href=https://nixos.org/nix/>Nix</a></td>
      <td><a href=https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/ju/just/package.nix>just</a></td>
      <td><code>nix-env -iA nixos.just</code></td>
    </tr>
    <tr>
      <td><a href=https://opensuse.org>openSUSE</a></td>
      <td><a href=https://en.opensuse.org/Portal:Zypper>Zypper</a></td>
      <td><a href=https://build.opensuse.org/package/show/Base:System/just>just</a></td>
      <td><code>zypper in just</code></td>
    </tr>
    <tr>
      <td><a href=https://getsol.us>Solus</a></td>
      <td><a href=https://getsol.us/articles/package-management/basics/en>eopkg</a></td>
      <td><a href=https://dev.getsol.us/source/just/>just</a></td>
      <td><code>eopkg install just</code></td>
    </tr>
    <tr>
      <td><a href=https://voidlinux.org>Void</a></td>
      <td><a href=https://wiki.voidlinux.org/XBPS>XBPS</a></td>
      <td><a href=https://github.com/void-linux/void-packages/blob/master/srcpkgs/just/template>just</a></td>
      <td><code>xbps-install -S just</code></td>
    </tr>
  </tbody>
</table>

#### Windows

<table>
  <thead>
    <tr>
      <th>Package Manager</th>
      <th>Package</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href=https://chocolatey.org>Chocolatey</a></td>
      <td><a href=https://github.com/michidk/just-choco>just</a></td>
      <td><code>choco install just</code></td>
    </tr>
    <tr>
      <td><a href=https://scoop.sh>Scoop</a></td>
      <td><a href=https://github.com/ScoopInstaller/Main/blob/master/bucket/just.json>just</a></td>
      <td><code>scoop install just</code></td>
    </tr>
    <tr>
      <td><a href=https://learn.microsoft.com/en-us/windows/package-manager/>Windows Package Manager</a></td>
      <td><a href=https://github.com/microsoft/winget-pkgs/tree/master/manifests/c/Casey/Just>Casey/Just</a></td>
      <td><code>winget install --id Casey.Just --exact</code></td>
    </tr>
  </tbody>
</table>

#### macOS

<table>
  <thead>
    <tr>
      <th>Package Manager</th>
      <th>Package</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href=https://www.macports.org>MacPorts</a></td>
      <td><a href=https://ports.macports.org/port/just/summary>just</a></td>
      <td><code>port install just</code></td>
    </tr>
  </tbody>
</table>

![just package version table](https://repology.org/badge/vertical-allrepos/just.svg)

### Pre-Built Binaries

Pre-built binaries for Linux, MacOS, and Windows can be found on
[the releases page](https://github.com/casey/just/releases).

You can use the following command on Linux, MacOS, or Windows to download the
latest release, just replace `DEST` with the directory where you'd like to put
`just`:

```console
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to DEST
```

For example, to install `just` to `~/bin`:

```console
# create ~/bin
mkdir -p ~/bin

# download and extract just to ~/bin/just
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/bin

# add `~/bin` to the paths that your shell searches for executables
# this line should be added to your shells initialization file,
# e.g. `~/.bashrc` or `~/.zshrc`
export PATH="$PATH:$HOME/bin"

# just should now be executable
just --help
```

Note that `install.sh` may fail on GitHub Actions, or in other environments
where many machines share IP addresses. `install.sh` calls GitHub APIs in order
to determine the latest version of `just` to install, and those API calls are
rate-limited on a per-IP basis. To make `install.sh` more reliable in such
circumstances, pass a specific tag to install with `--tag`.

Another way to avoid rate-limiting is to pass a GitHub authentication token to
`install.sh` as an environment variable named `GITHUB_TOKEN`, allowing it to
authenticate its requests.

[Releases](https://github.com/casey/just/releases) include a `SHA256SUM` file
which can be used to verify the integrity of pre-built binary archives.

To verify a release, download the pre-built binary archive along with the
`SHA256SUM` file and run:

```sh
shasum --algorithm 256 --ignore-missing --check SHA256SUMS
```

### GitHub Actions

`just` can be installed on GitHub Actions in a few ways.

Using package managers pre-installed on GitHub Actions runners on MacOS with
`brew install just`, and on Windows with `choco install just`.

With [extractions/setup-just](https://github.com/extractions/setup-just):

```yaml
- uses: extractions/setup-just@v3
  with:
    just-version: 1.5.0  # optional semver specification, otherwise latest
```

Or with [taiki-e/install-action](https://github.com/taiki-e/install-action):

```yaml
- uses: taiki-e/install-action@just
```

### Docker

`just` is available as a Docker image from
[the GitHub Container Registry](https://ghcr.io/casey/just).

To copy `just` into a Docker image, add the following line to your
`Dockerfile`:

```dockerfile
COPY --from=ghcr.io/casey/just:latest /just /usr/local/bin/
```

After copying, `just` may also be used as part of a docker build:

```dockerfile
RUN just
```

### Release RSS Feed

An [RSS feed](https://en.wikipedia.org/wiki/RSS) of `just` releases is
available [here](https://github.com/casey/just/releases.atom).

### Node.js Installation

[just-install](https://npmjs.com/package/just-install) can be used to automate
installation of `just` in Node.js applications.

`just` is a great, more robust alternative to npm scripts. If you want to
include `just` in the dependencies of a Node.js application, `just-install`
will install a local, platform-specific binary as part of the `npm install
... [TRUNCATED]
```

### File: build.rs
```rs
fn main() {
  let os = std::env::var("CARGO_CFG_TARGET_OS").unwrap();
  let env = std::env::var("CARGO_CFG_TARGET_ENV").unwrap();
  if os == "windows" {
    if env == "msvc" {
      println!("cargo::rustc-link-arg=/STACK:2097152");
    } else if env == "gnu" {
      println!("cargo::rustc-link-arg=-Wl,--stack,2097152");
    }
  }
}

```

### File: CHANGELOG.md
```md
Changelog
=========

[1.48.1](https://github.com/casey/just/releases/tag/1.48.1) - 2026-03-27
------------------------------------------------------------------------

- Fix bash completion of command lines containing `:` ([#3205](https://github.com/casey/just/pull/3205) by [casey](https://github.com/casey))
- Call zsh completion function when first auto-loaded ([#3199](https://github.com/casey/just/pull/3199) by [casey](https://github.com/casey))
- Fix `--set` missing value error message interpolation ([#3198](https://github.com/casey/just/pull/3198) by [cuiweixie](https://github.com/cuiweixie))
- Add `#compdef` to zsh completion script ([#3197](https://github.com/casey/just/pull/3197) by [casey](https://github.com/casey))
- Add instructions for alias completions in bash ([#3190](https://github.com/casey/just/pull/3190) by [casey](https://github.com/casey))
- Remove redundant clap derive attributes ([#3183](https://github.com/casey/just/pull/3183) by [casey](https://github.com/casey))
- Move files into etc/ ([#3182](https://github.com/casey/just/pull/3182) by [casey](https://github.com/casey))
- Update stable features in readme ([#3181](https://github.com/casey/just/pull/3181) by [casey](https://github.com/casey))

[1.48.0](https://github.com/casey/just/releases/tag/1.48.0) - 2026-03-23
------------------------------------------------------------------------

### Added
- Build docker images ([#3174](https://github.com/casey/just/pull/3174) by [casey](https://github.com/casey))
- Dynamically complete recipes for `--usage` ([#3172](https://github.com/casey/just/pull/3172) by [casey](https://github.com/casey))
- Dynamically complete groups ([#3171](https://github.com/casey/just/pull/3171) by [casey](https://github.com/casey))
- Dynamically complete recipes and variables ([#3169](https://github.com/casey/just/pull/3169) by [casey](https://github.com/casey))
- Complete appropriate filetypes ([#3168](https://github.com/casey/just/pull/3168) by [casey](https://github.com/casey))
- Allow overriding variables in submodules ([#3151](https://github.com/casey/just/pull/3151) by [casey](https://github.com/casey))
- Add `--json` as synonym for `--dump --dump-format json` ([#3143](https://github.com/casey/just/pull/3143) by [casey](https://github.com/casey))

### Changed
- Stabilize lazy evaluation ([#3180](https://github.com/casey/just/pull/3180) by [casey](https://github.com/casey))
- Switch to dynamic completion engine ([#3167](https://github.com/casey/just/pull/3167) by [casey](https://github.com/casey))
- Respect PATH and PATHEXT when running commands on Windows ([#3160](https://github.com/casey/just/pull/3160) by [casey](https://github.com/casey))
- Make `which()` and `require()` respect PATHEXT on Windows ([#3144](https://github.com/casey/just/pull/3144) by [casey](https://github.com/casey))

### Misc
- Add completion script installation instructions ([#3178](https://github.com/casey/just/pull/3178) by [casey](https://github.com/casey))
- Fix readme typo ([#3176](https://github.com/casey/just/pull/3176) by [Rohan5commit](https://github.com/Rohan5commit))
- Remove Vagrantfile ([#3173](https://github.com/casey/just/pull/3173) by [casey](https://github.com/casey))
- Fix signal handling typo ([#3170](https://github.com/casey/just/pull/3170) by [Rohan5commit](https://github.com/Rohan5commit))
- Add cargo-binstall installation instructions ([#3165](https://github.com/casey/just/pull/3165) by [casey](https://github.com/casey))
- Fix typos ([#3162](https://github.com/casey/just/pull/3162) by [casey](https://github.com/casey))
- Readme typo: forground ([#3161](https://github.com/casey/just/pull/3161) by [Rohan5commit](https://github.com/Rohan5commit))
- Use clap derive to parse arguments ([#3158](https://github.com/casey/just/pull/3158) by [casey](https://github.com/casey))
- Fix readme typo ([#3156](https://github.com/casey/just/pull/3156) by [teee32](https://github.com/teee32))
- Document that path_exists() returns strings ([#2946](https://github.com/casey/just/pull/2946) by [cspotcode](https://github.com/cspotcode))
- Remove version references from readme headings ([#3153](https://github.com/casey/just/pull/3153) by [casey](https://github.com/casey))
- Fix readme typo ([#3152](https://github.com/casey/just/pull/3152) by [Rohan5commit](https://github.com/Rohan5commit))
- Fix variadic parameter typo in readme ([#3150](https://github.com/casey/just/pull/3150) by [casey](https://github.com/casey))
- Fix readme typo ([#3148](https://github.com/casey/just/pull/3148) by [Rohan5commit](https://github.com/Rohan5commit))
- Avoid conditional compilation ([#3145](https://github.com/casey/just/pull/3145) by [casey](https://github.com/casey))
- Update VS Code extension in Chinese readme ([#2984](https://github.com/casey/just/pull/2984) by [A-moment096](https://github.com/A-moment096))
- Change replace wording in readme ([#3137](https://github.com/casey/just/pull/3137) by [Rohan5commit](https://github.com/Rohan5commit))
- Document recipe metadata ([#3142](https://github.com/casey/just/pull/3142) by [casey](https://github.com/casey))

[1.47.1](https://github.com/casey/just/releases/tag/1.47.1) - 2026-03-16
------------------------------------------------------------------------

### Fixed
- Block on running parallel dependencies ([#3139](https://github.com/casey/just/pull/3139) by [casey](https://github.com/casey))
- Fix setting-exported assignment visibility in child modules ([#3128](https://github.com/casey/just/pull/3128) by [casey](https://github.com/casey))

### Added
- Add `eager` keyword to force evaluation of unused assignments ([#3131](https://github.com/casey/just/pull/3131) by [casey](https://github.com/casey))

### Changed
- Only evaluate used variables in --evaluate and --command ([#3130](https://github.com/casey/just/pull/3130) by [casey](https://github.com/casey))

### Misc
- Make eager assignments unstable ([#3140](https://github.com/casey/just/pull/3140) by [casey](https://github.com/casey))
- Include path to .env file in error messages ([#3135](https://github.com/casey/just/pull/3135) by [casey](https://github.com/casey))
- Consolidate override checking ([#3127](https://github.com/casey/just/pull/3127) by [casey](https://github.com/casey))
- Update readme version references ([#3126](https://github.com/casey/just/pull/3126) by [casey](https://github.com/casey))

[1.47.0](https://github.com/casey/just/releases/tag/1.47.0) - 2026-03-14
------------------------------------------------------------------------

### Added
- Add lazy evaluation setting ([#3083](https://github.com/casey/just/pull/3083) by [casey](https://github.com/casey))
- Add guard sigil `?` ([#2547](https://github.com/casey/just/pull/2547) by [casey](https://github.com/casey))
- Add `--group` flag to filter `--list` output by group ([#3117](https://github.com/casey/just/pull/3117) by [terror](https://github.com/terror))
- Add attributes for DragonFly BSD, FreeBSD, and NetBSD ([#3115](https://github.com/casey/just/pull/3115) by [jakewilliami](https://github.com/jakewilliami))
- Add `[env(NAME, VALUE)` recipe attribute ([#2957](https://github.com/casey/just/pull/2957) by [neunenak](https://github.com/neunenak))

### Changed
- Make `--timestamp` print timestamps unconditionally ([#3114](https://github.com/casey/just/pull/3114) by [casey](https://github.com/casey))
- Print `--timestamps` with script recipes ([#3050](https://github.com/casey/just/pull/3050) by [casey](https://github.com/casey))
- `[private]` modules are excluded from `--list` output ([#2889](https://github.com/casey/just/pull/2889) by [Scott-Guest](https://github.com/Scott-Guest))

### Misc
- Fix readme typo ([#3122](https://github.com/casey/just/pull/3122) by [Rohan5commit](https://github.com/Rohan5commit))
- Move choose and run into match statement ([#3120](https://github.com/casey/just/pull/3120) by [casey](https://github.com/casey))
- Add uv install instructions to readme ([#3062](https://github.com/casey/just/pull/3062) by [npikall](https://github.com/npikall))
- Suppress error when --choose is cancelled by user ([#3098](https://github.com/casey/just/pull/3098) by [cobyfrombrooklyn-bot](https://github.com/cobyfrombrooklyn-bot))
- Test formatting justfile with undefined variable succeeds ([#3110](https://github.com/casey/just/pull/3110) by [casey](https://github.com/casey))
- Format without compiling ([#3103](https://github.com/casey/just/pull/3103) by [terror](https://github.com/terror))
- Fix Gentoo installation instructions ([#3085](https://github.com/casey/just/pull/3085) by [DarthGandalf](https://github.com/DarthGandalf))
- Deny unreachable pub ([#3080](https://github.com/casey/just/pull/3080) by [casey](https://github.com/casey))
- Fix readme typo ([#3079](https://github.com/casey/just/pull/3079) by [pvinis](https://github.com/pvinis))
- Include blank chapters in book ([#3076](https://github.com/casey/just/pull/3076) by [casey](https://github.com/casey))
- Clean up build script ([#3078](https://github.com/casey/just/pull/3078) by [casey](https://github.com/casey))
- Increase stack size on Windows ([#3077](https://github.com/casey/just/pull/3077) by [casey](https://github.com/casey))
- Fix readme typo ([#3066](https://github.com/casey/just/pull/3066) by [kenden](https://github.com/kenden))
- Remove dependency on executable-path ([#3058](https://github.com/casey/just/pull/3058) by [casey](https://github.com/casey))
- Fix typos ([#3056](https://github.com/casey/just/pull/3056) by [galenseilis](https://github.com/galenseilis))
- Avoid conditional compilation in integration tests ([#3055](https://github.com/casey/just/pull/3055) by [casey](https://github.com/casey))
- Assert exit status last in `Test` builder ([#3054](https://github.com/casey/just/pull/3054) by [casey](https://github.com/casey))
- Remove makedeb/MPR installation instructions ([#3053](https://github.com/casey/just/pull/3053) by [Chengings](https://github.com/Chengings))
- Handle errors when checking for files ([#3051](https://github.com/casey/just/pull/3051) by [casey](https://github.com/casey))

[1.46.0](https://github.com/casey/just/releases/tag/1.46.0) - 2026-01-01
------------------------------------------------------------------------

### Fixed
- Don't leak signal handler pipe into child processes ([#3035](https://github.com/casey/just/pull/3035) by [rjmac](https://github.com/rjmac))

### Added
- Allow `long` to default to parameter name ([#3041](https://github.com/casey/just/pull/3041) by [casey](https://github.com/casey))
- Allow const expressions in all settings ([#3037](https://github.com/casey/just/pull/3037) by [casey](https://github.com/casey))
- Allow const expressions in `working-directory` ([#3033](https://github.com/casey/just/pull/3033) by [casey](https://github.com/casey))
- Add --usage subcommand and argument help strings ([#3031](https://github.com/casey/just/pull/3031) by [casey](https://github.com/casey))
- Add flags without values ([#3029](https://github.com/casey/just/pull/3029) by [casey](https://github.com/casey))
- Allow passing arguments as short `-x` options ([#3028](https://github.com/casey/just/pull/3028) by [casey](https://github.com/casey))
- Allow recipes to take `--long` options ([#3026](https://github.com/casey/just/pull/3026) by [casey](https://github.com/casey))

### Misc
- Add original token to string literal ([#3042](https://github.com/casey/just/pull/3042) by [casey](https://github.com/casey))
- Remove string literal lifetime ([#3036](https://github.com/casey/just/pull/3036) by [casey](https://github.com/casey))
- Move overrides into config ([#3032](https://github.com/casey/just/pull/3032) by [casey](https://github.com/casey))
- Test that options are passed as positional arguments ([#3030](https://github.com/casey/just/pull/3030) by [casey](https://github.com/casey))
- Group arguments by parameter ([#3025](https://github.com/casey/just/pull/3025) by [casey](https://github.com/casey))
- Add OpenBSD package to readme ([#2900](https://github.com/casey/just/pull/2900) by [vext01](https://github.com/vext01))
- Re-enable mdbook-linkcheck ([#3011](https://github.com/casey/just/pull/3011) by [casey](https://github.com/casey))
- Disable dependabot ([#3010](https://github.com/casey/just/pull/3010) by [casey](https://github.com/casey))
- Fix pre-release check in pages deploy job ([#3009](https://github.com/casey/just/pull/3009) by [casey](https://github.com/casey))

[1.45.0](https://github.com/casey/just/releases/tag/1.45.0) - 2025-12-10
------------------------------------------------------------------------

### Added
- Allow requiring recipe arguments to match regular expression patterns ([#3000](https://github.com/casey/just/pull/3000) by [casey](https://github.com/casey))

### Fixed
- Allow shell-expanded strings in attributes ([#3007](https://github.com/casey/just/pull/3007) by [casey](https://github.com/casey))
- Fix arg pattern anchoring ([#3002](https://github.com/casey/just/pull/3002) by [casey](https://github.com/casey))

### Misc
- Use non-capturing group in arg pattern regex ([#3006](https://github.com/casey/just/pull/3006) by [casey](https://github.com/casey))
- Remove redundant type annotation ([#3004](https://github.com/casey/just/pull/3004) by [casey](https://github.com/casey))

[1.44.1](https://github.com/casey/just/releases/tag/1.44.1) - 2025-12-09
------------------------------------------------------------------------

### Fixed
- Properly close format string delimiter ([#2997](https://github.com/casey/just/pull/2997) by [casey](https://github.com/casey))

[1.44.0](https://github.com/casey/just/releases/tag/1.44.0) - 2025-12-06
------------------------------------------------------------------------

### Added
- Add f'{format}' strings ([#2985](https://github.com/casey/just/pull/2985) by [casey](https://github.com/casey))
- Use double braces `{{…}}` for format strings ([#2993](https://github.com/casey/just/pull/2993) by [casey](https://github.com/casey))
- Stabilize `[script]` attribute ([#2988](https://github.com/casey/just/pull/2988) by [casey](https://github.com/casey))

### Changed
- Allow newlines in interpolations and `}` to abut interpolation `}}` ([#2992](https://github.com/casey/just/pull/2992) by [casey](https://github.com/casey))

### Misc
- Test format strings with conditionals ([#2991](https://github.com/casey/just/pull/2991) by [casey](https://github.com/casey))
- Move StringState into module ([#2989](https://github.com/casey/just/pull/2989) by [casey](https://github.com/casey))
- Test undefined variable in format string error ([#2987](https://github.com/casey/just/pull/2987) by [casey](https://github.com/casey))
- Update `softprops/action-gh-release` to 2.5.0 ([#2979](https://github.com/casey/just/pull/2979) by [app/dependabot](https://github.com/app/dependabot))
- Link to `just-lsp` in readme ([#2846](https://github.com/casey/just/pull/2846) by [terror](https://github.com/terror))
- Fix `just --list` submodule example in readme ([#2973](https://github.com/casey
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
Contributing
============

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you shall be licensed as in [LICENSE](LICENSE),
without any additional terms or conditions.

See [the readme](README.md#contributing) for contribution workflow suggestions.

```

### File: GRAMMAR.md
```md
justfile grammar
================

Justfiles are processed by a mildly context-sensitive tokenizer
and a recursive descent parser. The grammar is LL(k), for an
unknown but hopefully reasonable value of k.

tokens
------

```
BACKTICK            = `[^`]*`
INDENTED_BACKTICK   = ```[^(```)]*```
COMMENT             = #([^!].*)?$
DEDENT              = emitted when indentation decreases
EOF                 = emitted at the end of the file
INDENT              = emitted when indentation increases
LINE                = emitted before a recipe line
NAME                = [a-zA-Z_][a-zA-Z0-9_-]*
NEWLINE             = \n|\r\n
RAW_STRING          = '[^']*'
INDENTED_RAW_STRING = '''[^(''')]*'''
STRING              = "[^"]*" # also processes \n \r \t \" \\ escapes
INDENTED_STRING     = """[^(""")]*""" # also processes \n \r \t \" \\ escapes
LINE_PREFIX         = @-|-@|@|-
TEXT                = recipe text, only matches in a recipe body
```

grammar syntax
--------------

```
|   alternation
()  grouping
_?  option (0 or 1 times)
_*  repetition (0 or more times)
_+  repetition (1 or more times)
```

grammar
-------

```
justfile      : item* EOF

item          : alias
              | assignment
              | eol
              | export
              | import
              | module
              | recipe
              | set

eol           : NEWLINE
              | COMMENT NEWLINE

alias         : 'alias' NAME ':=' target eol

target        : NAME ('::' NAME)*

assignment    : NAME ':=' expression eol

export        : 'export' assignment

set           : 'set' setting eol

setting       : 'allow-duplicate-recipes' boolean?
              | 'allow-duplicate-variables' boolean?
              | 'dotenv-filename' ':=' string
              | 'dotenv-load' boolean?
              | 'dotenv-path' ':=' string
              | 'dotenv-required' boolean?
              | 'export' boolean?
              | 'fallback' boolean?
              | 'ignore-comments' boolean?
              | 'positional-arguments' boolean?
              | 'script-interpreter' ':=' string_list
              | 'quiet' boolean?
              | 'shell' ':=' string_list
              | 'tempdir' ':=' string
              | 'unstable' boolean?
              | 'windows-powershell' boolean?
              | 'windows-shell' ':=' string_list
              | 'working-directory' ':=' string

boolean       : ':=' ('true' | 'false')

string_list   : '[' string (',' string)* ','? ']'

import        : 'import' '?'? string? eol

module        : 'mod' '?'? NAME string? eol

expression    : disjunct || expression
              | disjunct

disjunct      : conjunct && disjunct
              | conjunct

conjunct      : 'if' condition '{' expression '}' 'else' '{' expression '}'
              | 'assert' '(' condition ',' expression ')'
              | '/' expression
              | value '/' expression
              | value '+' expression
              | value

condition     : expression '==' expression
              | expression '!=' expression
              | expression '=~' expression

value         : NAME '(' sequence? ')'
              | BACKTICK
              | INDENTED_BACKTICK
              | NAME
              | string
              | '(' expression ')'

string        : 'x'? STRING
              | 'x'? INDENTED_STRING
              | 'x'? RAW_STRING
              | 'x'? INDENTED_RAW_STRING

sequence      : expression ',' sequence
              | expression ','?

recipe        : attributes* '@'? NAME parameter* variadic? ':' dependencies eol body?

attributes    : '[' attribute (',' attribute)* ']' eol

attribute     : NAME
              | NAME ':' string
              | NAME '(' string (',' string)* ')'

parameter     : '$'? NAME
              | '$'? NAME '=' value

variadic      : '*' parameter
              | '+' parameter

dependencies  : dependency* ('&&' dependency+)?

dependency    : target
              | '(' target expression* ')'

body          : INDENT line+ DEDENT

line          : LINE LINE_PREFIX? (TEXT | interpolation)+ NEWLINE
              | NEWLINE

interpolation : '{{' expression '}}'
```

```

### File: README.中文.md
```md
↖️ 目录

<h1 align="center"><code>just</code></h1>

<div align="center">
  <a href="https://crates.io/crates/just">
    <img src="https://img.shields.io/crates/v/just.svg" alt="crates.io version">
  </a>
  <a href="https://github.com/casey/just/actions">
    <img src="https://github.com/casey/just/actions/workflows/ci.yaml/badge.svg" alt="build status">
  </a>
  <a href="https://github.com/casey/just/releases">
    <img src="https://img.shields.io/github/downloads/casey/just/total.svg" alt="downloads">
  </a>
  <a href="https://discord.gg/ezYScXR">
    <img src="https://img.shields.io/discord/695580069837406228?logo=discord" alt="chat on discord">
  </a>
  <a href="mailto:casey@rodarmor.com?subject=Thanks%20for%20Just!">
    <img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="say thanks">
  </a>
</div>
<br>

`just` 为您提供一种保存和运行项目特有命令的便捷方式。

本指南同时也可以以 [书](https://just.systems/man/zh/) 的形式提供在线阅读。

命令，在此也称为配方，存储在一个名为 `justfile` 的文件中，其语法受 `make` 启发：

![screenshot](https://raw.githubusercontent.com/casey/just/master/etc/screenshot.png)

然后你可以用 `just RECIPE` 运行它们：

```sh
$ just test-all
cc *.c -o main
./test --all
Yay, all your tests passed!
```

`just` 有很多很棒的特性，而且相比 `make` 有很多改进：

- `just` 是一个命令运行器，而不是一个构建系统，所以它避免了许多 [`make` 的复杂性和特异性](#just-避免了-make-的哪些特异性)。不需要 `.PHONY` 配方!

- 支持 Linux、MacOS 和 Windows，而且无需额外的依赖。(尽管如果你的系统没有 `sh`，你需要 [选择一个不同的 Shell](#shell))。

- 错误具体且富有参考价值，语法错误将会与产生它们的上下文一起被报告。

- 配方可以接受 [命令行参数](#配方参数)。

- 错误会尽可能被静态地解决。未知的配方和循环依赖关系会在运行之前被报告。

- `just` 可以 [加载`.env`文件](#环境变量加载)，简化环境变量注入。

- 配方可以在 [命令行中列出](#列出可用的配方)。

- 命令行自动补全脚本 [支持大多数流行的 Shell](#shell-自动补全脚本)。

- 配方可以用 [任意语言](#用其他语言书写配方) 编写，如 Python 或 NodeJS。

- `just` 可以从任何子目录中调用，而不仅仅是包含 `justfile` 的目录。

- 不仅如此，还有 [更多](https://just.systems/man/zh/)！

如果你在使用 `just` 方面需要帮助，请随时创建一个 Issue 或在 [Discord](https://discord.gg/ezYScXR) 上与我联系。我们随时欢迎功能请求和错误报告！

安装
------------

### 预备知识

`just` 应该可以在任何有合适的 `sh` 的系统上运行，包括 Linux、MacOS 和 BSD。

在 Windows 上，`just` 可以使用 [Git for Windows](https://git-scm.com)、[GitHub Desktop](https://desktop.github.com) 或 [Cygwin](http://www.cygwin.com) 所提供的 `sh`。

如果你不愿意安装 `sh`，也可以使用 `shell` 设置来指定你要使用的 Shell。

比如 PowerShell：

```just
# 使用 PowerShell 替代 sh:
set shell := ["powershell.exe", "-c"]

hello:
  Write-Host "Hello, world!"
```

…或者 `cmd.exe`:

```just
# 使用 cmd.exe 替代 sh:
set shell := ["cmd.exe", "/c"]

list:
  dir
```

你也可以使用命令行参数来设置 Shell。例如，若要使用 PowerShell 也可以用 `--shell powershell.exe --shell-arg -c` 启动`just`。

(PowerShell 默认安装在 Windows 7 SP1 和 Windows Server 2008 R2 S1 及更高版本上，而 `cmd.exe` 相当麻烦，所以 PowerShell 被推荐给大多数 Windows 用户)

### 安装包

<table>
  <thead>
    <tr>
      <th>操作系统</th>
      <th>包管理器</th>
      <th>安装包</th>
      <th>命令</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="https://forge.rust-lang.org/release/platform-support.html">Various</a></td>
    <td><a href="https://www.rust-lang.org">Cargo</a></td>
    <td><a href="https://crates.io/crates/just">just</a></td>
    <td><code>cargo install just</code></td>
  </tr>
  <tr>
    <td><a href="https://en.wikipedia.org/wiki/Microsoft_Windows">Microsoft Windows</a></td>
    <td><a href="https://scoop.sh">Scoop</a></td>
    <td><a href="https://github.com/ScoopInstaller/Main/blob/master/bucket/just.json">just</a></td>
    <td><code>scoop install just</code></td>
  </tr>
  <tr>
    <td><a href="https://docs.brew.sh/Installation">Various</a></td>
    <td><a href="https://brew.sh">Homebrew</a></td>
    <td><a href="https://formulae.brew.sh/formula/just">just</a></td>
    <td><code>brew install just</code></td>
  </tr>
  <tr>
    <td><a href="https://en.wikipedia.org/wiki/MacOS">macOS</a></td>
    <td><a href="https://www.macports.org">MacPorts</a></td>
    <td><a href="https://ports.macports.org/port/just/summary">just</a></td>
    <td><code>port install just</code></td>
  </tr>
  <tr>
    <td><a href="https://www.archlinux.org">Arch Linux</a></td>
    <td><a href="https://wiki.archlinux.org/title/Pacman">pacman</a></td>
    <td><a href="https://archlinux.org/packages/community/x86_64/just/">just</a></td>
    <td><code>pacman -S just</code></td>
  </tr>
  <tr>
    <td><a href="https://nixos.org/download.html#download-nix">Various</a></td>
    <td><a href="https://nixos.org/nix/">Nix</a></td>
    <td><a href="https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/ju/just/package.nix">just</a></td>
    <td><code>nix-env -iA nixpkgs.just</code></td>
  </tr>
  <tr>
    <td><a href="https://nixos.org/nixos/">NixOS</a></td>
    <td><a href="https://nixos.org/nix/">Nix</a></td>
    <td><a href="https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/ju/just/package.nix">just</a></td>
    <td><code>nix-env -iA nixos.just</code></td>
  </tr>
  <tr>
    <td><a href="https://getsol.us">Solus</a></td>
    <td><a href="https://getsol.us/articles/package-management/basics/en">eopkg</a></td>
    <td><a href="https://dev.getsol.us/source/just/">just</a></td>
    <td><code>eopkg install just</code></td>
  </tr>
  <tr>
    <td><a href="https://voidlinux.org">Void Linux</a></td>
    <td><a href="https://wiki.voidlinux.org/XBPS">XBPS</a></td>
    <td><a href="https://github.com/void-linux/void-packages/blob/master/srcpkgs/just/template">just</a></td>
    <td><code>xbps-install -S just</code></td>
  </tr>
  <tr>
    <td><a href="https://www.freebsd.org">FreeBSD</a></td>
    <td><a href="https://www.freebsd.org/doc/handbook/pkgng-intro.html">pkg</a></td>
    <td><a href="https://www.freshports.org/deskutils/just/">just</a></td>
    <td><code>pkg install just</code></td>
  </tr>
  <tr>
    <td><a href="https://alpinelinux.org">Alpine Linux</a></td>
    <td><a href="https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management">apk-tools</a></td>
    <td><a href="https://pkgs.alpinelinux.org/package/edge/community/x86_64/just">just</a></td>
    <td><code>apk add just</code></td>
  </tr>
  <tr>
    <td><a href="https://getfedora.org">Fedora Linux</a></td>
    <td><a href="https://dnf.readthedocs.io/en/latest/">DNF</a></td>
    <td><a href="https://src.fedoraproject.org/rpms/rust-just">just</a></td>
    <td><code>dnf install just</code></td>
  </tr>
  <tr>
    <td><a href="https://www.gentoo.org">Gentoo Linux</a></td>
    <td><a href="https://wiki.gentoo.org/wiki/Portage">Portage</a></td>
    <td><a href="https://github.com/gentoo-mirror/guru/tree/master/sys-devel/just">guru/sys-devel/just</a></td>
    <td>
      <code>eselect repository enable guru</code><br>
      <code>emerge --sync guru</code><br>
      <code>emerge sys-devel/just</code>
    </td>
  </tr>
  <tr>
    <td><a href="https://docs.conda.io/en/latest/miniconda.html#system-requirements">Various</a></td>
    <td><a href="https://docs.conda.io/projects/conda/en/latest/index.html">Conda</a></td>
    <td><a href="https://anaconda.org/conda-forge/just">just</a></td>
    <td><code>conda install -c conda-forge just</code></td>
  </tr>
  <tr>
    <td><a href="https://en.wikipedia.org/wiki/Microsoft_Windows">Microsoft Windows</a></td>
    <td><a href="https://chocolatey.org">Chocolatey</a></td>
    <td><a href="https://github.com/michidk/just-choco">just</a></td>
    <td><code>choco install just</code></td>
  </tr>
  <tr>
    <td><a href="https://snapcraft.io/docs/installing-snapd">Various</a></td>
    <td><a href="https://snapcraft.io">Snap</a></td>
    <td><a href="https://snapcraft.io/just">just</a></td>
    <td><code>snap install --edge --classic just</code></td>
  </tr>
  <tr>
    <td><a href="https://github.com/casey/just/releases">Various</a></td>
    <td><a href="https://asdf-vm.com">asdf</a></td>
    <td><a href="https://github.com/olofvndrhr/asdf-just">just</a></td>
    <td>
      <code>asdf plugin add just</code><br>
      <code>asdf install just &lt;version&gt;</code>
    </td>
  </tr>
  <tr>
    <td><a href="https://packaging.python.org/tutorials/installing-packages">Various</a></td>
    <td><a href="https://pypi.org">PyPI</a></td>
    <td><a href="https://pypi.org/project/rust-just">rust-just</a></td>
    <td>
      <code>pipx install rust-just</code><br>
    </td>
  </tr>
  <tr>
    <td><a href="https://docs.npmjs.com/packages-and-modules/getting-packages-from-the-registry">Various</a></td>
    <td><a href="https://www.npmjs.com">npm</a></td>
    <td><a href="https://www.npmjs.com/package/rust-just">rust-just</a></td>
    <td>
      <code>npm install -g rust-just</code><br>
    </td>
  </tr>
  <tr>
    <td><a href="https://debian.org">Debian</a> and <a href="https://ubuntu.com">Ubuntu</a> derivatives</td>
    <td><a href="https://mpr.makedeb.org">MPR</a></td>
    <td><a href="https://mpr.makedeb.org/packages/just">just</a></td>
    <td>
      <code>git clone 'https://mpr.makedeb.org/just'</code><br>
      <code>cd just</code><br>
      <code>makedeb -si</code>
    </td>
  </tr>
  <tr>
    <td><a href="https://debian.org">Debian</a> and <a href="https://ubuntu.com">Ubuntu</a> derivatives</td>
    <td><a href="https://docs.makedeb.org/prebuilt-mpr">Prebuilt-MPR</a></td>
    <td><a href="https://mpr.makedeb.org/packages/just">just</a></td>
    <td>
      <sup><b>You must have the <a href="https://docs.makedeb.org/prebuilt-mpr/getting-started/#setting-up-the-repository">Prebuilt-MPR set up</a> on your system in order to run this command.</b></sup><br>
      <code>sudo apt install just</code>
    </td>
  </tr>
  </tbody>
</table>

![package version table](https://repology.org/badge/vertical-allrepos/just.svg)

### 预制二进制文件

Linux、MacOS 和 Windows 的预制二进制文件可以在 [发布页](https://github.com/casey/just/releases) 上找到。

你也可以在 Linux、MacOS 或 Windows 上使用下面的命令来下载最新的版本，只需将 `DEST` 替换为你想安装 `just` 的目录即可：

```sh
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to DEST
```

例如，安装 `just` 到 `~/bin` 目录：

```sh
# 创建 ~/bin
mkdir -p ~/bin

# 下载并解压 just 到 ~/bin/just
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/bin

# 在 Shell 搜索可执行文件的路径中添加`~/bin`
# 这一行应该被添加到你的 Shell 初始化文件中，e.g. `~/.bashrc` 或者 `~/.zshrc`：
export PATH="$PATH:$HOME/bin"

# 现在 just 应该就可以执行了
just --help
```

### GitHub Actions

使用 [extractions/setup-just](https://github.com/extractions/setup-just):

```yaml
- uses: extractions/setup-just@v1
  with:
    just-version: 0.8 # optional semver specification, otherwise latest
```

使用 [taiki-e/install-action](https://github.com/taiki-e/install-action):

```yaml
- uses: taiki-e/install-action@just
```

### 发布 RSS 订阅

`just` 的发布 [RSS 订阅](https://en.wikipedia.org/wiki/RSS) 可以在 [这里](https://github.com/casey/just/releases.atom) 找到。

### Node.js 安装

[just-install](https://npmjs.com/package/just-install) 可用于在 Node.js 应用程序中自动安装 `just`。

`just` 是一个很赞的比 npm 脚本更强大的替代品。如果你想在 Node.js 应用程序的依赖中包含 `just`，可以通过 `just-install`，它将在本机安装一个针对特定平台的二进制文件作为 `npm install` 安装结果的一部分。这样就不需要每个开发者使用上述提到的步骤独立安装 `just`。安装后，`just` 命令将在 npm 脚本或 npx 中工作。这对那些想让项目的设置过程尽可能简单的团队来说是很有用的。

想了解更多信息, 请查看 [just-install 说明文件](https://github.com/brombal/just-install#readme)。

向后兼容性
-----------------------

随着 1.0 版本的发布，`just` 突出对向后兼容性和稳定性的强烈承诺。

未来的版本将不会引入向后不兼容的变化，不会使现有的 `justfile` 停止工作，或破坏命令行界面的正常调用。

然而，这并不排除修复全面的错误，即使这样做可能会破坏依赖其行为的 `justfiles`。

永远不会有一个 `just` 2.0。任何理想的向后兼容的变化都是在每个 `justfile` 的基础上选择性加入的，所以用户可以在他们的闲暇时间进行迁移。

还没有准备好稳定化的功能将在 `--unstable` 标志后被选择性启用。由 `--unstable` 启用的功能可能会在任何时候以不兼容的方式发生变化。

编辑器支持
--------------

`justfile` 的语法与 `make` 非常接近，你可以让你的编辑器对 `just` 使用 `make` 语法高亮。

### Vim 和 Neovim

#### `vim-just`

[vim-just](https://github.com/NoahTheDuke/vim-just) 插件可以为 vim 提供 `justfile` 语法高亮显示。

你可以用你喜欢的软件包管理器安装它，如 [Plug](https://github.com/junegunn/vim-plug)：

```vim
call plug#begin()

Plug 'NoahTheDuke/vim-just'

call plug#end()
```

或者使用 Vim 的内置包支持：

```sh
mkdir -p ~/.vim/pack/vendor/start
cd ~/.vim/pack/vendor/start
git clone https://github.com/NoahTheDuke/vim-just.git
```

#### `tree-sitter-just`

[tree-sitter-just](https://github.com/IndianBoy42/tree-sitter-just) 是一个针对 Neovim 的 [Nvim Treesitter](https://github.com/nvim-treesitter/nvim-treesitter) 插件。

#### Makefile 语法高亮

Vim 内置的 makefile 语法高亮对 `justfile` 来说并不完美，但总比没有好。你可以把以下内容放在 `~/.vim/filetype.vim` 中：

```vimscript
if exists("did_load_filetypes")
  finish
endif

augroup filetypedetect
  au BufNewFile,BufRead justfile setf make
augroup END
```
或者在单个 `justfile` 中添加以下内容，以在每个文件的基础上启用 `make` 模式：

```text
# vim: set ft=make :
```

### Emacs

[just-mode](https://github.com/leon-barrett/just-mode.el) 可以为 `justfile` 提供语法高亮和自动缩进。它可以在 [MELPA](https://melpa.org/) 上通过 [just-mode](https://melpa.org/#/just-mode) 获得。

[justl](https://github.com/psibi/justl.el) 提供了执行和列出配方的命令。

你可以在一个单独的 `justfile` 中添加以下内容，以便对每个文件启用 `make` 模式：

```text
# Local Variables:
# mode: makefile
# End:
```

### Visual Studio Code

VS Code 的一个插件可以在 [这里](https://github.com/nefrob/vscode-just) 找到。

不再维护的 VS Code 插件有 [skellock/vscode-just](https://github.com/skellock/vscode-just) 和 [sclu1034/vscode-just](https://github.com/sclu1034/vscode-just)。

### JetBrains IDEs

由 [linux_china](https://github.com/linux-china) 为 JetBrains IDEs 提供的插件可 [由此获得](https://plugins.jetbrains.com/plugin/18658-just)。

### Kakoune

Kakoune 已经内置支持 `justfile` 语法高亮，这要感谢 TeddyDD。

### Sublime Text

由 [nk9](https://github.com/nk9) 提供的 [Just 包](https://github.com/nk9/just_sublime) 支持 `just` 语法高亮，同时还有其它工具，这些可以在 [PackageControl](https://packagecontrol.io/packages/Just) 上找到。

### 其它编辑器

欢迎给我发送必要的命令，以便在你选择的编辑器中实现语法高亮，这样我就可以把它们放在这里。

快速开始
-----------

参见 [安装部分](#安装) 了解如何在你的电脑上安装 `just`。试着运行 `just --version` 以确保它被正确安装。

关于语法的概述，请查看这个 [速查表](https://cheatography.com/linux-china/cheat-sheets/justfile/)。

一旦 `just` 安装完毕并开始工作，在你的项目根目录创建一个名为 `justfile` 的文件，内容如下：

```just
recipe-name:
  echo 'This is a recipe!'

# 这是一行注释
another-recipe:
  @echo 'This is another recipe.'
```

当你调用 `just` 时，它会在当前目录和父目录寻找文件 `justfile`，所以你可以从你项目的任何子目录中调用它。

搜索 `justfile` 是不分大小写的，所以任何大小写，如 `Justfile`、`JUSTFILE` 或 `JuStFiLe` 都可以工作。`just` 也会寻找名字为 `.justfile` 的文件，以便你打算隐藏一个 `justfile`。

运行 `just` 时未传参数，则运行 `justfile` 中的第一个配方：

```sh
$ just
echo 'This is a recipe!'
This is a recipe!
```

通过一个或多个参数指定要运行的配方：

```sh
$ just another-recipe
This is another recipe.
```

`just` 在运行每条命令前都会将其打印到标准错误中，这就是为什么 `echo 'This is a recipe!'` 被打印出来。对于以 `@` 开头的行，这将被抑制，这就是为什么 `echo 'This is another recipe.'` 没有被打印。

如果一个命令失败，配方就会停止运行。这里 `cargo publish` 只有在 `cargo test` 成功后才会运行：

```just
publish:
  cargo test
  # 前面的测试通过才会执行 publish!
  cargo publish
```

配方可以依赖其他配方。在这里，`test` 配方依赖于 `build` 配方，所以 `build` 将在 `test` 之前运行：

```just
build:
  cc main.c foo.c bar.c -o main

test: build
  ./test

sloc:
  @echo "`wc -l *.c` lines of code"
```

```sh
$ just test
cc main.c foo.c bar.c -o main
./test
testing… all tests passed!
```

没有依赖关系的配方将按照命令行上给出的顺序运行：

```sh
$ just build sloc
cc main.c foo.c bar.c -o main
1337 lines of code
```

依赖项总是先运行，即使它们被放在依赖它们的配方之后：

```sh
$ just test build
cc main.c foo.c bar.c -o main
./test
testing… all tests passed!
```

示例
--------

在 [Examples 目录](https://github.com/casey/just/tree/master/examples) 中可以找到各种 `justfile` 的例子。

特性介绍
--------

### 默认配方

当 `just` 被调用而没有传入任何配方时，它会运行 `justfile` 中的第一个配方。这个配方可能是项目中最常运行的命令，比如运行测试：

```just
test:
  cargo test
... [TRUNCATED]
```

### File: src\alias.rs
```rs
use super::*;

/// An alias, e.g. `alias name := target`
#[derive(Debug, PartialEq, Clone, Serialize)]
pub(crate) struct Alias<'src, T = Arc<Recipe<'src>>> {
  pub(crate) attributes: AttributeSet<'src>,
  pub(crate) name: Name<'src>,
  #[serde(
    bound(serialize = "T: Keyed<'src>"),
    serialize_with = "keyed::serialize"
  )]
  pub(crate) target: T,
}

impl<'src> Alias<'src, Namepath<'src>> {
  pub(crate) fn resolve(self, target: Arc<Recipe<'src>>) -> Alias<'src> {
    assert!(self.target.last().lexeme() == target.name());

    Alias {
      attributes: self.attributes,
      name: self.name,
      target,
    }
  }
}

impl Alias<'_> {
  pub(crate) fn is_public(&self) -> bool {
    !self.name.lexeme().starts_with('_')
      && !self.attributes.contains(AttributeDiscriminant::Private)
  }
}

impl<'src, T> Keyed<'src> for Alias<'src, T> {
  fn key(&self) -> &'src str {
    self.name.lexeme()
  }
}

impl<'src> Display for Alias<'src, Namepath<'src>> {
  fn fmt(&self, f: &mut Formatter) -> fmt::Result {
    write!(f, "alias {} := {}", self.name.lexeme(), self.target)
  }
}

impl Display for Alias<'_> {
  fn fmt(&self, f: &mut Formatter) -> fmt::Result {
    write!(
      f,
      "alias {} := {}",
      self.name.lexeme(),
      self.target.name.lexeme()
    )
  }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
