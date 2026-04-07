---
id: fastfetch
type: knowledge
owner: OA_Triage
---
# fastfetch
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Fastfetch

[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/fastfetch-cli/fastfetch/ci.yml)](https://github.com/fastfetch-cli/fastfetch/actions)
[![GitHub license](https://img.shields.io/github/license/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/blob/dev/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/graphs/contributors)
[![GitHub top language](https://img.shields.io/github/languages/top/fastfetch-cli/fastfetch?logo=c&label=)](https://github.com/fastfetch-cli/fastfetch/blob/dev/CMakeLists.txt#L5)
[![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/commits)  
[![homebrew downloads](https://img.shields.io/homebrew/installs/dm/fastfetch?logo=homebrew)](https://formulae.brew.sh/formula/fastfetch#default)
[![GitHub all releases](https://img.shields.io/github/downloads/fastfetch-cli/fastfetch/total?logo=github)](https://github.com/fastfetch-cli/fastfetch/releases)  
[![GitHub release (with filter)](https://img.shields.io/github/v/release/fastfetch-cli/fastfetch?logo=github)](https://github.com/fastfetch-cli/fastfetch/releases)
[![latest packaged version(s)](https://repology.org/badge/latest-versions/fastfetch.svg)](https://repology.org/project/fastfetch/versions)
[![Packaging status](https://repology.org/badge/tiny-repos/fastfetch.svg)](https://repology.org/project/fastfetch/versions)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/fastfetch-cli/fastfetch)
[![中文README](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-README-red)](README-cn.md)

Fastfetch is a [neofetch](https://github.com/dylanaraps/neofetch)-like tool for fetching system information and displaying it in a visually appealing way. It is written mainly in C, with a focus on performance and customizability. Currently, it supports Linux, macOS, Windows 8.1+, Android, FreeBSD, OpenBSD, NetBSD, DragonFly, Haiku and SunOS (illumos, Solaris).

> Note: Fastfetch is only actively tested on x86-64 and aarch64 platforms. It may work on other platforms but is not guaranteed to do so.

<img src="screenshots/example1.png" width="49%" align="left" />
<img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Square_Tiles_Texture.png" width="49%" height="16px" align="left" />
<img src="screenshots/example4.png" width="49%" align="left" />
<img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Square_Tiles_Texture.png" width="49%" height="16px" align="left" />
<img src="screenshots/example2.png" width="48%" align="top" />
<img src="screenshots/example3.png" width="48%" align="top" />
<img src="screenshots/example5.png" height="15%" align="top" />

According configuration files for examples are located [here](https://github.com/fastfetch-cli/fastfetch/tree/dev/presets/examples).

There are [screenshots on different platforms](https://github.com/fastfetch-cli/fastfetch/wiki).

## Installation

### Linux

Some distributions package outdated versions of fastfetch. Older versions receive no support, so please always try to use the latest version.

<a href="https://repology.org/project/fastfetch/versions">
    <img src="https://repology.org/badge/vertical-allrepos/fastfetch.svg?columns=2" alt="Packaging status" align="right">
</a>

* Ubuntu: [`ppa:zhangsongcui3371/fastfetch`](https://launchpad.net/~zhangsongcui3371/+archive/ubuntu/fastfetch) (Ubuntu 22.04 or newer; latest version)
* Debian / Ubuntu: `apt install fastfetch` (Debian 13 or newer; Ubuntu 25.04 or newer)
* Debian / Ubuntu: Download `fastfetch-linux-<proper architecture>.deb` from [Github release page](https://github.com/fastfetch-cli/fastfetch/releases/latest) and double-click it (for Ubuntu 20.04 or newer and Debian 11 or newer).
* Arch Linux: `pacman -S fastfetch`
* Fedora: `dnf install fastfetch`
* Gentoo: `emerge --ask app-misc/fastfetch`
* Alpine: `apk add --upgrade fastfetch`
* NixOS: `nix-shell -p fastfetch`
* openSUSE: `zypper install fastfetch`
* ALT Linux: `apt-get install fastfetch`
* Exherbo: `cave resolve --execute app-misc/fastfetch`
* Solus: `eopkg install fastfetch`
* Slackware: `sbopkg -i fastfetch`
* Void Linux: `xbps-install fastfetch`
* Venom Linux: `scratch install fastfetch`

You may need `sudo`, `doas`, or `sup` to run these commands.

If fastfetch is not packaged for your distribution or an outdated version is packaged, [linuxbrew](https://brew.sh/) is a good alternative: `brew install fastfetch`

### macOS

* [Homebrew](https://formulae.brew.sh/formula/fastfetch#default): `brew install fastfetch`
* [MacPorts](https://ports.macports.org/port/fastfetch/): `sudo port install fastfetch`

### Windows

* [scoop](https://scoop.sh/#/apps?q=fastfetch): `scoop install fastfetch`
* [Chocolatey](https://community.chocolatey.org/packages/fastfetch): `choco install fastfetch`
* [winget](https://github.com/microsoft/winget-pkgs/tree/master/manifests/f/Fastfetch-cli/Fastfetch): `winget install fastfetch`
* [MSYS2 MinGW](https://packages.msys2.org/base/mingw-w64-fastfetch): `pacman -S mingw-w64-<subsystem>-<arch>-fastfetch`

You may also download the program directly from [the GitHub releases page](https://github.com/fastfetch-cli/fastfetch/releases/latest) in the form of an archive file.

### BSD systems

* FreeBSD: `pkg install fastfetch`
* NetBSD: `pkgin in fastfetch`
* OpenBSD: `pkg_add fastfetch` (Snapshots only)
* DragonFly BSD: `pkg install fastfetch` (Snapshots only)

### Android (Termux)

* `pkg install fastfetch`

### Nightly

<https://nightly.link/fastfetch-cli/fastfetch/workflows/ci/dev?preview>

## Build from source

See the Wiki: https://github.com/fastfetch-cli/fastfetch/wiki/Building

## Usage

* Run with default configuration: `fastfetch`
* Run with [all supported modules](https://github.com/fastfetch-cli/fastfetch/wiki/Support+Status#available-modules) to find what interests you: `fastfetch -c all.jsonc`
* View all data that fastfetch detects: `fastfetch -s <module1>[:<module2>][:<module3>] --format json`
* Display help messages: `fastfetch --help`
* Generate a minimal config file: `fastfetch [-s <module1>[:<module2>]] --gen-config [</path/to/config.jsonc>]`
    * Use: `--gen-config-full` to generate a full config file with all optional options

## Customization

Fastfetch uses JSONC (JSON with comments) for configuration. [See the Wiki for details](https://github.com/fastfetch-cli/fastfetch/wiki/Configuration). There are some premade config files in the [`presets`](presets) directory, including those used for the screenshots above. You can load them using `-c <filename>`. These files can serve as examples of the configuration syntax.

Logos can also be heavily customized; see the [logo documentation](https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options) for more information.

### WARNING

Fastfetch supports a `Command` module that can run arbitrary shell commands. If you copy-paste a config file from an untrusted source, it may contain malicious commands that can harm your system or compromise your privacy. Please always review the config file before using it.

## FAQ

### Q: Neofetch is good enough. Why do I need fastfetch?

1. Fastfetch is actively maintained.
2. Fastfetch is faster, as the name suggests.
3. Fastfetch has a greater number of features, though by default it only has a few modules enabled; use `fastfetch -c all` to discover what you want.
4. Fastfetch is more configurable. You can find more information in the Wiki: <https://github.com/fastfetch-cli/fastfetch/wiki/Configuration>.
5. Fastfetch is more polished. For example, neofetch prints `555 MiB` in the Memory module and `23 G` in the Disk module, whereas fastfetch prints `555.00 MiB` and `22.97 GiB` respectively.
6. Fastfetch is more accurate. For example, [neofetch never actually supports the Wayland protocol](https://github.com/dylanaraps/neofetch/pull/2395).

### Q: Fastfetch shows my local IP address. Does it leak my privacy?

A local IP address (10.x.x.x, 172.x.x.x, 192.168.x.x) has nothing to do with privacy. It only has meaning if you are on the same network, for example, if you connect to the same Wi-Fi network.

Actually, the `Local IP` module is the most useful module for me personally. I (@CarterLi) have several VMs installed to test fastfetch and often need to SSH into them. With fastfetch running on shell startup, I never need to type `ip addr` manually.

If you really don't like it, you can disable the `Local IP` module in `config.jsonc`.

### Q: Where is the config file? I can't find it.

Fastfetch does not generate a config file automatically. You can use `fastfetch --gen-config` to generate one. The config file will be saved in `~/.config/fastfetch/config.jsonc` by default. See the [Wiki for details](https://github.com/fastfetch-cli/fastfetch/wiki/Configuration).

### Q: The configuration is so complex. Where is the documentation?

Fastfetch uses JSON (with comments) for configuration. I suggest using an IDE with JSON schema support (like VSCode) to edit it.

Alternatively, you can refer to the presets in the [`presets` directory](https://github.com/fastfetch-cli/fastfetch/tree/dev/presets).

The **correct** way to edit the configuration:

This is an example that [changes size prefix from MiB / GiB to MB / GB](https://github.com/fastfetch-cli/fastfetch/discussions/1014). Editor used: [helix](https://github.com/helix-editor/helix)

[![asciicast](https://asciinema.org/a/1uF6sTPGKrHKI1MVaFcikINSQ.svg)](https://asciinema.org/a/1uF6sTPGKrHKI1MVaFcikINSQ)

### Q: I WANT THE DOCUMENTATION!

[Here is the documentation](https://github.com/fastfetch-cli/fastfetch/wiki/Json-Schema). It is generated from the [JSON schema](https://github.com/fastfetch-cli/fastfetch/blob/dev/doc/json_schema.json), but you might not find it very user-friendly.

### Q: How can I customize the module output?

Fastfetch uses `format` to generate output. For example, to make the `GPU` module show only the GPU name (leaving other information undisplayed), you can use:

```jsonc
{
    "modules": [
        {
            "type": "gpu",
            "format": "{name}" // See `fastfetch -h gpu-format` for details
        }
    ]
}
```

...which is equivalent to `fastfetch -s gpu --gpu-format '{name}'`

See `fastfetch -h format` for information on basic usage. For module-specific formatting, see `fastfetch -h <module>-format`

### Q: I have my own ASCII art / image file. How can I show it with fastfetch?

Try `fastfetch -l /path/to/logo`. See the [logo documentation](https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options) for details.

If you just want to display the distro name in [FIGlet text](https://github.com/pwaller/pyfiglet):

```bash
# install pyfiglet and jq first
pyfiglet -s -f small_slant $(fastfetch -s os --format json | jq -r '.[0].result.name') && fastfetch -l none
```

![image](https://github.com/fastfetch-cli/fastfetch/assets/6134068/6466524e-ab8c-484f-848d-eec7ddeb7df2)

### Q: My image logo behaves strangely. How can I fix it?

See the troubleshooting section: <https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options#troubleshooting>

### Q: Fastfetch runs in black and white on shell startup. Why?

This issue usually occurs when using fastfetch with `p10k`. There are known incompatibilities between fastfetch and p10k instant prompt.
The p10k documentation clearly states that you should NOT print anything to stdout after `p10k-instant-prompt` is initialized. You should put `fastfetch` before the initialization of `p10k-instant-prompt` (recommended).

You can always use `fastfetch --pipe false` to force fastfetch to run in colorful mode.

### Q: Why do fastfetch and neofetch show different memory usage results?

See [#1096](https://github.com/fastfetch-cli/fastfetch/issues/1096).

### Q: Fastfetch shows fewer dpkg packages than neofetch. Is it a bug?

Neofetch incorrectly counts `rc` packages (packages that have been removed but still have configuration files remaining). See bug: https://github.com/dylanaraps/neofetch/issues/2278

### Q: I use Debian / Ubuntu / Debian-derived distro. My GPU is detected as `XXXX Device XXXX (VGA compatible)`. Is this a bug?

Try upgrading `pci.ids`: Download <https://pci-ids.ucw.cz/v2.2/pci.ids> and overwrite the file `/usr/share/hwdata/pci.ids`. For AMD GPUs, you should also upgrade `amdgpu.ids`: Download <https://gitlab.freedesktop.org/mesa/drm/-/raw/main/data/amdgpu.ids> and overwrite the file `/usr/share/libdrm/amdgpu.ids`

Alternatively, you may try using `fastfetch --gpu-driver-specific`, which will make fastfetch attempt to ask the driver for the GPU name if supported.

### Q: I get the error `Authorization required, but no authorization protocol specified` when running fastfetch as root

Try `export XAUTHORITY=$HOME/.Xauthority`

### Q: Fastfetch cannot detect my awesome 3rd-party macOS window manager!

Try `fastfetch --wm-detect-plugin`. See also [#984](https://github.com/fastfetch-cli/fastfetch/issues/984)

### Q: How can I change the colors of my ASCII logo?

Try `fastfetch --logo-color-[1-9] <color>`, where `[1-9]` is the index of color placeholders.

For example: `fastfetch --logo-color-1 red --logo-color-2 green`.

In JSONC, you can use:

```jsonc
{
    "logo": {
        "color": {
            "1": "red",
            "2": "green"
        }
    }
}
```

### Q: How do I hide a key?

Set the key to a white space.

```jsonc
{
    "key": " "
}
```

### Q: How can I display images on Windows?

As of April 2025:

#### mintty and Wezterm

mintty (used by Bash on Windows and MSYS2) and Wezterm (nightly build only) support the iTerm image protocol on Windows.

In `config.jsonc`:  
```json
{
  "logo": {
    "type": "iterm",
    "source": "C:/path/to/image.png",
    "width": <num-in-chars>
  }
}
```

#### Windows Terminal

Windows Terminal supports the sixel image protocol only.

* If you installed fastfetch through MSYS2:
    1. Install imagemagick: `pacman -S mingw-w64-<subsystem>-x86_64-imagemagick`
    2. In `config.jsonc`:  
```jsonc
{
  "logo": {
    "type": "sixel", // DO NOT USE "auto"
    "source": "C:/path/to/image.png", // Do NOT use `~` as fastfetch is a native Windows program and doesn't apply cygwin path conversion
    "width": <image-width-in-chars>, // Optional
    "height": <image-height-in-chars> // Optional
  }
}
```
* If you installed fastfetch via scoop or downloaded the binary directly from the GitHub Releases page:
    1. Convert your image manually to sixel format using [any online image conversion service](https://www.google.com/search?q=convert+image+to+sixel)
    2. In `config.jsonc`:  
```jsonc
{
  "logo": {
    "type": "raw", // DO NOT USE "auto"
    "source": "C:/path/to/image.sixel",
    "width": <image-width-in-chars>, // Required
    "height": <image-height-in-chars> // Required
  }
}
```

### Q: I want feature A / B / C. W
... [TRUNCATED]
```

### File: CHANGELOG.md
```md
# 2.61.0

Changes:
* Support for Windows 7 and 8 has been removed.
    * Windows 8.1 is now the oldest version supported by fastfetch.
* The GPU module on WSL no longer relies on `DXCore`.
    * The `directx-headers` dependency is no longer required.
    * Fastfetch on Linux is now pure C; a C++ compiler is no longer required.
    * GPU type detection is now slightly less accurate, but detection speed should be slightly faster.
* The GPU module on Windows now uses `DXCore` for more accurate GPU type detection (requires Windows 10 or later).
    * This feature is built only when `DXCore` headers are available, which requires installing `mingw-w64-<msystem>-x86_64-directx-headers` on MSYS2.

Features:
* Adds a `brightness` option for color display configuration (#2238, Colors)
* Adds support for detecting Bluetooth keyboards on Linux (#2220, Keyboard)
* Adds support for detecting GlazeWM (WM, macOS)
* Adds a `showEmptySlots` option to display empty memory slots on Linux (#2222, PhysicalMemory)
* Adds marketing product name detection on Asahi Linux (Host, Linux)
* Adds support for new M5 Mac models (Host, macOS)
* Improves SMBIOS robustness by validating malformed data and improving error handling
* Improves reliability when terminating child processes (Processing, Windows)
* Improves Intel Mac support by querying SMBIOS data directly (Global, macOS)
* Includes numerous internal cleanups and optimizations

Bugfixes:
* Fixes missing memory devices on some machines (PhysicalMemory)
* Fixes CPUCache deduplication for shared caches (#2228, CPUCache, Linux)
* Fixes WM version reporting for niri (#2218, WM, Linux)
* Fixes SSID decoding issues from `iw` output (Wifi, Linux)
* Fixes the CMD code page being changed after running fastfetch on Windows (#2245, Windows)

# 2.60.0

Changes:
* The CMake option `ENABLE_WIN7_COMPAT:BOOLEAN` now defaults to `OFF` and will be removed in v2.61.0, effectively dropping support for Windows 7 in the next release.
    * This follows the Windows 7 deprecation notice introduced in v2.57.0.
* `wm.detectPlugin` now defaults to `true` (WM)

Features:
* Adds `{cwd}` for custom title formatting, which displays the current working directory (Title)
* Adds support for detecting the Zed version (#2200, Editor)
* Adds support for detecting `moss` packages (Packages, Linux)
* Adds support for detecting komorebi, FancyWM, and GlazeWM (WM, Windows)
* Adds support for WM plugin version detection on macOS (WM, macOS)
* Adds support for retrieving the executable path on OpenBSD (#2195, OpenBSD)

Bugfixes:
* Fixes a potential segmentation fault caused by dereferencing a negative index (#2198)
* Fixes `tempSensor` parsing so that it accepts only string values (#2202, CPU)
* Fixes an issue that unexpectedly caused fewer devices to be reported (Keyboard, Linux)
* Improves WM detection on LXQt by querying WM settings only when no WM has already been detected (#2199, WM, Linux)
* Fixes memory leaks in DBus connection handling and in the OpenGL EGL context lifecycle
* Fixes niri version detection on Fedora (WM, Linux)
* Includes various internal cleanups and optimizations

Logos:
* Adds `RengeOS` (#2170)
* Adds `Emmabuntüs` (#2207)
* Updates Artix Linux (#2157)
* Updates Linux Mint (#2186)
* Renames `Refracted Devuan` to `Refracta`
* Renames `ExodiaPredator` to `ExodiaOS`

# 2.59.0

Changes:
* Fastfetch no longer relies on the unreliable environment variables `$USER` or `%USERPROFILE%` to determine the current username (Title)
    * People who set `$USER` to customize the Fastfetch title should use `{ "type": "title", "format": "your-custom-user-name" }` to achieve the same result.
* Fastfetch no longer tries to probe inaccessible remote disk drives on Windows (Disk, Windows)
    * People who have remote drives may use `{ "type": "disk", "hideFolders": "X:\\" }` to ignore problematic ones.
    * This change removes some ugly hacks from the codebase and matches the behavior on `*nix`.

Features:
* Adds Oracle Solaris support (#2176, SunOS)
* Adds UID / SID detection (Title)
    * In custom format: `{user-id}`
* Switches to native GPU detection on GNU/Hurd and removes the `libpciaccess` dependency (GPU, Hurd)
* Improves memory size detection on macOS (Memory, macOS)
    * Avoids relying on `hw.memsize_usable` by default, which may not be available on older macOS versions
* Improves Windows disk detection accuracy and performance (Disk, Windows)
* Adds more ARM CPU parts and removes duplicated cases (CPU, ARM)

Logos:
* Adds 6-color support to the NixOS logo (including the small variant) (#2180)

# 2.58.0

An early release to fix compatibility issues with KDE Plasma 6.6.

Breaking changes:
* The `de.slowVersionDetection` option has been removed. Slow version detection is now always enabled, as required on non-FHS-compliant distros (e.g., NixOS). (#2149, DE, Linux)

Features:
* Adds the `--structure-disabled <modules...>` command-line flag to temporarily disable module structure printing.
    * For example: `fastfetch --structure-disabled colors` removes the color blocks from the default output.
* Supports chassis type detection on Linux ARM devices when reported via the device tree (Chassis, Linux)
* Supports Bedrock Linux version detection (#2155, OS, Linux)
* Honors the `DBPath` and `RootDir` settings in `pacman.conf` when detecting Pacman packages (#2154, Packages, Linux)

Bugfixes:
* Fixes a crash issue on KDE Plasma 6.6 (Display, Linux)
* Fixes the Command module not working with `--dynamic-interval` (#2152, Command)
* Fixes Quartz Compositor version detection. It now correctly reports the version of `WindowServer` (`SkyLight`) instead of `WindowManager`. (WM, macOS)

Logos:
* Adds Kiss2

# 2.57.1

Features:
* Tiny performance improvements (Windows)
* Improves the reliability of hostname retrieval (Title, Windows)

Bugfixes:
* Fixes potential compilation issues on Linux (#2142, Linux)
* Fixes compilation errors on macOS when building with older SDKs (#2140, macOS)
* Fixes compilation issues when building with `-DENABLE_SYSTEM_YYJSON=ON` (#2143)

Logos:
* Updates PrismLinux and adds a small variant

# 2.57.0

Deprecation notice:
* Support for Windows 7 (and 8.x) is deprecated and will be removed in a future release. Extended support for Windows 7 (and 8.1) ended on January 10, 2023. These versions do not officially support ANSI escape codes (running fastfetch on them requires a third-party terminal such as ConEmu). In addition, Windows 7 lacks some APIs used by fastfetch. Fastfetch currently loads these APIs dynamically at runtime to maintain compatibility, but this adds complexity to the codebase and increases the maintenance burden.
    * A CMake flag `ENABLE_WIN7_COMPAT:BOOLEAN` has been introduced (defaults to `ON` for now). If set to `OFF`, Windows 7 compatibility code is excluded, and the resulting binaries will support only Windows 10 (version 1607 and later) and Windows 11.
    * The main prebuilt Windows binaries on the Release page (`fastfetch-windows-amd64.*`) are built with `ENABLE_WIN7_COMPAT=OFF`. These are the binaries used by `scoop` and `winget`. Users who need Windows 7 (or 8.x) support can download the `-win7` variant instead.
    * ~~The `ENABLE_WIN7_COMPAT` CMake option and the `-win7` variant binaries are planned to be removed in 2.60.0~~.

Features:
* Supports COSMIC DE version detection (DE, Linux)
* Supports niri version detection (#2121, WM, Linux)
* Supports cosmic-term version and terminal font detection (Terminal / TerminalFont, Linux)
* Supports urxvt font detection (TerminalFont, Linux) (#2105)
* Improves xterm font detection by checking `xterm.vt100.faceName` (TerminalFont, Linux)
* Supports Secure Boot detection (Bootmgr, macOS)
* Supports DPI scale factor detection on Windows 7 (Display, Windows)
* Supports xterm 256-color codes in color configuration
    * In `display.color`: "`@<color-index>`" (e.g., "`@34`" for color index `34`)
    * In `*.format` strings: "`#@<color-index>`" (e.g., "`#@34`" for color index `34`)
* Improves uptime accuracy on Windows 10+ (Uptime, Windows)
* Adds a new module `Logo` to query built-in logo raw data in JSON output (Logo)
    * Usage: `fastfetch -s logo -l <logo-name> -j # Supported in JSON format only`
* Supports shell version detection even if the binary has been deleted (#2136, Shell, Linux)
* Overall code refinements and optimizations

Bugfixes:
* Skips local / loopback routes when detecting network interfaces (LocalIP, Linux) (#2127)
* Fixes CPU speed detection on s390x (CPU, Linux) (#2129)
* Fixes GPU detection error handling and supports case-insensitive PCI ID parsing (GPU, Windows)
* Fixes some networking issues and memory leaks (Networking)
* Fixes `exePath` reporting relative paths on macOS (Shell, macOS)

Logos:
* Adds openSUSE Tumbleweed braille logo
* Adds Xinux
* Renames HydraPWK to NetHydra
* Fixes colors of deepin and UOS
* Fixes colors of macOS and variants

# 2.56.1

Features:
* Improves compatibility with KDE Plasma 6.5 (#2093, Display)
* Adds a `tempSensor` option to specify the sensor name used for CPU temperature detection (CPU)
    * Example: `{ "type": "cpu", "tempSensor": "hwmon0" /* Use /sys/class/hwmon/hwmon0 for temperature detection */ }`
* Refines Memory usage detection on macOS to match Activity Monitor more closely (Memory, macOS)
* Minor optimizations

Bugfixes:
* Fixes cache line size detection (CPU, macOS)

Logos:
* Removes Opak
* Updates GXDE

# 2.56.0

Features:
* Enhances config file loading. `--config` and `-c` with relative path now also searches paths defined in `fastfetch --list-config-paths` (typically `~/.config/fastfetch/`)
    * This allows users to use `fastfetch -c my-config` without needing to specify the full path.
* Adds NUMA node count detection (CPU)
    * Exposed via `{numa-nodes}` in custom format
    * Supported on Linux, FreeBSD and Windows
* Supports the newest Alacritty config format (#2070, TerminalFont)
* Detects driver specific info for Zhaoxin GPUs (GPU, Linux)
* Detects Android OEM UI for certain OSes (DE, Android)
* Improves users detection on Linux (#2064, Users, Linux)
    * Adds systemd fallback when utmp is unavailable
    * Fixes resource leaks
    * Always reports the newest session info
* Adds kiss package manager support (#2072, Packages, Linux)
* Reports `sshd` if `$SSH_TTY` is not available (Terminal)
* Zpool module rewrite (#2051, Zpool)
    * Adds new Zpool properties: allocated, guid, readOnly
    * Zpool module now uses runtime lookup for properties to ensure portability
    * Adds NetBSD (requires `sudo`) and macOS support
* Adds `splitLines` option for Command module, which splits the output into sub modules, each containing one line of the output (Command)
```
* Command output:
Line 1
Line 2
Line 3

* Old behavior:
Command: Line 1
Line 2
Line 3

* With `"splitLines": true`:
Command 1: Line 1
Command 2: Line 2
Command 3: Line 3
```

Bugfixes:
* Fixes {m,o}ksh version detection on Linux (Shell)
* Fixes Alacritty config parsing for TOML format (#2070, TerminalFont)
* Improves builtin logo printing for piping and buffering (#2065, Logo)
* Uses absolute path when detecting shell and terminal version if available (#2067, TerminalShell)

Logos:
* Updates Codex Linux logo (#2071)
* Adds OS/2 Warp logo (#2062)
* Adds Amiga logo (#2061)

# 2.55.1

Bugfixes:
* Fix parallel command execution breaks randomly (#2056 / #2058, Command)
    * Regression from v2.55.0
* Fix `dylib` searching path on macOS (macOS)
    * Regression from v2.55.0
* Fix an uninitialized field (#2057, Display)

# 2.55.0

Changes:
* Commands are now executed in parallel by default to improve performance (#2045, Command)
    * This behavior can be disabled in the config file with `"parallel": false` if it causes problems with certain scripts
* Folder/filesystem hiding is moved to the detection stage; hidden entries are no longer probed, improving performance (#2043, Disk)

Features:
* Adds `command.parallel` and `command.useStdErr` config options (Command)
    * `parallel`: set to `false` to disable parallel execution (see Changes above)
    * `useStdErr`: set to `true` to use stderr output instead of stdout
* Adds the command-line flag `--dynamic-interval <interval-in-ms>` to enable dynamic output auto-refresh (#2041)
    * Due to internal limitations, some modules do not support dynamic updates (notably Display and Media)
* Adds support for using the current playing media's cover art as a logo source (Media / Logo)
    * Usage: `"logo": { "type": "<image-protocol>", "source": "media-cover" }` in JSON config; or `--<image-protocol> media-cover` in command line
    * Supports local sources only
* Adds native GPU detection support on OpenBSD and NetBSD (instead of depending on `libpciaccess`) (GPU)
    * No functional changes
    * Root privileges are required to access PCI config space on OpenBSD (as always)
* Adds GPU detection support on GNU/Hurd (GPU)
    * Requires building with `libpciaccess`
* Shows Debian point release on Raspberry Pi OS (#2032, OS, Linux)
* Adds `Brush` shell version detection (Shell)
* Improves Mac family detection via prefix matching (Host)

Bugfixes:
* Ignores `run-parts` during terminal/shell detection (#2048, Terminal / Shell, Linux)
* Fixes fish version detection when `LC_ALL` is set (#2014, Shell, Linux)
* Hides the module when no desktop icons are found (#2023, Icons, Windows)
* Skips auxiliary display controllers to prevent the module from reporting duplicate entries (#2034, GPU, Linux)
* Refines Apple rpath handling; fixes building for the Homebrew version on macOS (#1998, CMake)

Logos:
* Adds Vincent OS and MacaroniOS

# 2.54.0

Windows binaries in Release page are now signed by SignPath.

Changes:
* Moves macOS and Windows design language detection from the DE module to the Theme module

Features:
* Adds `--json` and `-j` command line flags as a shortcut for `--format json`
* Various improvements to the OS module (OS)
    * Displays point releases for Debian
    * Displays code names for Ubuntu
    * Displays build ID for macOS
    * Displays code names for Windows (previously shown in the Kernel module)
* Adds basic support for Wine (Windows)
* Adds basic support for hppa and sh architectures (CPU, Linux)
* Improves T-Head SoC name detection from the device tree (#1997, CPU, Linux)
* Supports glob patterns in `Disk.hideFolders` (Disk)
    * For example, `/boot/*` will match both `/boot/efi` and `/boot/firmware`
* Adds brightness-level detection for external monitor support on Intel macOS (Brightness, macOS)
* Adds configurable spacing between icon and text in keys
    * `display.key.type: "both-N"` where N is `0-4`
    * Useful for non-monospaced Nerd Fonts
* Adds detection support for modern Samsung Exynos SoCs (CPU, Android)
* Adds a new CMake option `-DENABLE_WORDEXP=<ON|OFF>` to enable or disable using `wordexp(3)` for acquiring logo file paths (`logo.source`)
    * Enabled by default for compatibility
    * Disabling this option reverts to using `glob(3)`, which 
... [TRUNCATED]
```

### File: CMakeLists.txt
```txt
cmake_minimum_required(VERSION 3.12.0) # target_link_libraries with OBJECT libs & project homepage url

project(fastfetch
    VERSION 2.61.0
    LANGUAGES C
    DESCRIPTION "Fast neofetch-like system information tool"
    HOMEPAGE_URL "https://github.com/fastfetch-cli/fastfetch"
)

set(PROJECT_LICENSE "MIT license")

if(DEFINED CMAKE_SYSTEM_PROCESSOR_OVERRIDE) # Used by github actions for i686 build
    set(CMAKE_SYSTEM_PROCESSOR ${CMAKE_SYSTEM_PROCESSOR_OVERRIDE} CACHE INTERNAL "")
endif()
string(TOLOWER "${CMAKE_SYSTEM_PROCESSOR}" CMAKE_SYSTEM_PROCESSOR)
if(CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set(CMAKE_SYSTEM_PROCESSOR "amd64")
elseif(CMAKE_SYSTEM_PROCESSOR STREQUAL "arm64")
    set(CMAKE_SYSTEM_PROCESSOR "aarch64")
endif()
message(STATUS "Build for system processor: ${CMAKE_SYSTEM_PROCESSOR}")

###################
# Target Platform #
###################
if(ANDROID)
    set(LINUX FALSE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "Linux")
    set(LINUX TRUE CACHE BOOL "..." FORCE) # LINUX means GNU/Linux, not just the kernel
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "FreeBSD")
    set(FreeBSD TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "OpenBSD")
    set(OpenBSD TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "MidnightBSD")
    set(FreeBSD TRUE CACHE BOOL "..." FORCE)
    set(MidnightBSD TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "NetBSD")
    set(NetBSD TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "DragonFly")
    set(FreeBSD TRUE CACHE BOOL "..." FORCE)
    set(DragonFly TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "SunOS")
    set(SunOS TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "Haiku")
    set(Haiku TRUE CACHE BOOL "..." FORCE)
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "GNU")
    set(GNU TRUE CACHE BOOL "..." FORCE)
elseif(NOT APPLE AND NOT WIN32)
    message(FATAL_ERROR "Unsupported platform: ${CMAKE_SYSTEM_NAME}")
endif()

#############################
# Compile time dependencies #
#############################

set(THREADS_PREFER_PTHREAD_FLAG NOT WIN32)
find_package(Threads)

find_package(PkgConfig)
if(NOT PKG_CONFIG_FOUND)
    message(WARNING "pkg-config not found, library detection might be limited")
endif()

include(CheckIncludeFile)

#####################
# Configure options #
#####################

include(CMakeDependentOption)

cmake_dependent_option(ENABLE_VULKAN "Enable vulkan" ON "LINUX OR APPLE OR FreeBSD OR OpenBSD OR NetBSD OR WIN32 OR ANDROID OR SunOS OR Haiku OR GNU" OFF)
cmake_dependent_option(ENABLE_WAYLAND "Enable wayland-client" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR GNU" OFF)
cmake_dependent_option(ENABLE_XCB_RANDR "Enable xcb-randr" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_XRANDR "Enable xrandr" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_DRM "Enable libdrm" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_DRM_AMDGPU "Enable libdrm_amdgpu" ON "LINUX OR FreeBSD OR GNU" OFF)
cmake_dependent_option(ENABLE_GIO "Enable gio-2.0" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_DCONF "Enable dconf" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_DBUS "Enable dbus-1" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR SunOS OR Haiku OR GNU" OFF)
cmake_dependent_option(ENABLE_SQLITE3 "Enable sqlite3" ON "LINUX OR FreeBSD OR APPLE OR OpenBSD OR NetBSD OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_RPM "Enable rpm" ON "LINUX OR GNU" OFF)
cmake_dependent_option(ENABLE_IMAGEMAGICK7 "Enable imagemagick 7" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR APPLE OR ANDROID OR WIN32 OR SunOS OR Haiku OR GNU" OFF)
cmake_dependent_option(ENABLE_IMAGEMAGICK6 "Enable imagemagick 6" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR APPLE OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_CHAFA "Enable chafa" ON "ENABLE_IMAGEMAGICK6 OR ENABLE_IMAGEMAGICK7" OFF)
cmake_dependent_option(ENABLE_EGL "Enable egl" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR WIN32 OR SunOS OR Haiku OR GNU" OFF)
cmake_dependent_option(ENABLE_GLX "Enable glx" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR ANDROID OR SunOS OR GNU" OFF)
cmake_dependent_option(ENABLE_OPENCL "Enable opencl" ON "LINUX OR FreeBSD OR OpenBSD OR NetBSD OR WIN32 OR ANDROID OR SunOS OR Haiku OR GNU" OFF)
cmake_dependent_option(ENABLE_FREETYPE "Enable freetype" ON "ANDROID" OFF)
cmake_dependent_option(ENABLE_PULSE "Enable pulse" ON "LINUX OR ANDROID OR GNU" OFF)
cmake_dependent_option(ENABLE_DDCUTIL "Enable ddcutil" ON "LINUX" OFF)
cmake_dependent_option(ENABLE_ELF "Enable libelf" ON "LINUX OR ANDROID OR DragonFly OR Haiku OR GNU" OFF)
cmake_dependent_option(ENABLE_THREADS "Enable multithreading" ON "Threads_FOUND" OFF)

option(ENABLE_ZLIB "Enable zlib" ON)
option(ENABLE_SYSTEM_YYJSON "Use system provided (instead of fastfetch embedded) yyjson library" OFF)
option(ENABLE_ASAN "Build fastfetch with ASAN (address sanitizer)" OFF)
option(ENABLE_LTO "Enable link-time optimization in release mode if supported" ON)
option(BUILD_FLASHFETCH "Build flashfetch" ON) # Also build the flashfetch binary
option(BUILD_TESTS "Build tests" OFF) # Also create test executables
option(SET_TWEAK "Add tweak to project version" ON) # This is set to off by github actions for release builds
option(IS_MUSL "Build with musl libc" OFF) # Used by Github Actions
option(INSTALL_LICENSE "Install license into /usr/share/licenses" ON)
option(ENABLE_EMBEDDED_PCIIDS "Embed pci.ids into fastfetch, requires `python`" OFF)
option(ENABLE_EMBEDDED_AMDGPUIDS "Embed amdgpu.ids into fastfetch, requires `python`" OFF)
option(ENABLE_WORDEXP "Enable using of wordexp(3) if available, instead of glob(3)" ON)
option(ENABLE_LIBZFS "Enable libzfs" ON)
if(WIN32 AND NOT CMAKE_SYSTEM_PROCESSOR STREQUAL "aarch64")
    option(ENABLE_WIN81_COMPAT "Enable legacy Windows compatibility (Windows 8.1 and later; Windows 7 unsupported)" ON)
endif()
if(APPLE)
    option(ENABLE_APPLE_MEMSIZE_USABLE "Use usable memory size as total memory size in Memory module, to match other systems" OFF)
endif()

set(BINARY_LINK_TYPE_OPTIONS dlopen dynamic static)
set(BINARY_LINK_TYPE dlopen CACHE STRING "How to link fastfetch")
set_property(CACHE BINARY_LINK_TYPE PROPERTY STRINGS ${BINARY_LINK_TYPE_OPTIONS})
if(NOT BINARY_LINK_TYPE IN_LIST BINARY_LINK_TYPE_OPTIONS)
    message(FATAL_ERROR "BINARY_LINK_TYPE must be one of ${BINARY_LINK_TYPE_OPTIONS}")
endif()

set(PACKAGE_MANAGERS AM APK BREW CHOCO DPKG EMERGE EOPKG FLATPAK GUIX LINGLONG LPKG LPKGBUILD MACPORTS NIX OPKG PACMAN PACSTALL PALUDIS PISI PKG PKGTOOL RPM SCOOP SNAP SOAR SORCERY WINGET XBPS)
foreach(package_manager ${PACKAGE_MANAGERS})
    if(package_manager STREQUAL "WINGET")
        option(PACKAGES_DISABLE_${package_manager} "Disable ${package_manager} package manager detection by default" ON)
    else()
        option(PACKAGES_DISABLE_${package_manager} "Disable ${package_manager} package manager detection by default" OFF)
    endif()
endforeach()

if (LINUX)
    set(CUSTOM_PCI_IDS_PATH "" CACHE STRING "Custom path to file pci.ids, defaults to `/usr/share/hwdata/pci.ids`")
    set(CUSTOM_AMDGPU_IDS_PATH "" CACHE STRING "Custom path to file amdgpu.ids, defaults to `/usr/share/libdrm/amdgpu.ids`")
    set(CUSTOM_OS_RELEASE_PATH "" CACHE STRING "Custom path to file os-release, defaults to `/etc/os-release`")
endif()

####################
# Compiler options #
####################

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE RelWithDebInfo)
endif()

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
if(ENABLE_THREADS)
    if(CMAKE_USE_WIN32_THREADS_INIT)
        message(STATUS "Threads type: Win32 thread")
    elseif(CMAKE_USE_PTHREADS_INIT)
        message(STATUS "Threads type: pthread")
    endif()
else()
    message(STATUS "Threads type: disabled")
endif()

set(WARNING_FLAGS "-Wall -Wextra -Wconversion -Werror=uninitialized -Werror=return-type -Werror=vla")

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${WARNING_FLAGS} -Werror=incompatible-pointer-types -Werror=implicit-function-declaration -Werror=int-conversion")

if(WIN32 OR Haiku)
    enable_language(CXX)
    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${WARNING_FLAGS}")
endif()

if(WIN32)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--tsaware -Wl,--build-id")

    if(ENABLE_WIN81_COMPAT)
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--subsystem,console,--major-os-version,6,--minor-os-version,3")
    else()
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--subsystem,console,--major-os-version,10,--minor-os-version,0")
    endif()
elseif(APPLE AND CMAKE_C_COMPILER_ID MATCHES "Clang")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fobjc-arc")
endif()

set(FASTFETCH_FLAGS_DEBUG "-fno-omit-frame-pointer")
if(ENABLE_ASAN)
    message(STATUS "Address sanitizer enabled (DEBUG only)")
    set(FASTFETCH_FLAGS_DEBUG "${FASTFETCH_FLAGS_DEBUG} -fsanitize=address")
endif()
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} ${FASTFETCH_FLAGS_DEBUG}")
set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} ${FASTFETCH_FLAGS_DEBUG} -fstack-protector-all -fno-delete-null-pointer-checks")
if(NOT WIN32)
    set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} -rdynamic")
endif()

if(ENABLE_LTO AND NOT CMAKE_BUILD_TYPE STREQUAL "Debug")
    message(STATUS "Enabling LTO")
    include(CheckIPOSupported)
    check_ipo_supported(RESULT IPO_SUPPORTED)
    if(IPO_SUPPORTED)
        set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
    endif()
endif()

#######################
# Target FS structure #
#######################

if(NOT TARGET_DIR_ROOT)
    if(NOT ANDROID)
        set(TARGET_DIR_ROOT "")
    else()
        set(TARGET_DIR_ROOT "/data/data/com.termux/files/usr")
    endif()
endif()

if(NOT TARGET_DIR_USR)
    if(NOT ANDROID)
        set(TARGET_DIR_USR "${TARGET_DIR_ROOT}/usr")
    else()
        set(TARGET_DIR_USR "${TARGET_DIR_ROOT}")
    endif()
endif()

if(NOT TARGET_DIR_HOME)
    if(APPLE)
        set(TARGET_DIR_HOME "${TARGET_DIR_ROOT}/Users")
    elseif(ANDROID)
        set(TARGET_DIR_HOME "/data/data/com.termux/files/home")
    else()
        set(TARGET_DIR_HOME "${TARGET_DIR_ROOT}/home")
    endif()
endif()

if(NOT TARGET_DIR_ETC)
    set(TARGET_DIR_ETC "${TARGET_DIR_ROOT}/etc")
endif()

message(STATUS "Target dirs: ROOT=\"${TARGET_DIR_ROOT}\" USR=\"${TARGET_DIR_USR}\" HOME=\"${TARGET_DIR_HOME}\" ETC=\"${TARGET_DIR_ETC}\"")

#https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT.html
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX "${TARGET_DIR_USR}" CACHE PATH "..." FORCE)
endif()

if(NOT CMAKE_INSTALL_SYSCONFDIR)
    set(CMAKE_INSTALL_SYSCONFDIR "${TARGET_DIR_ETC}" CACHE PATH "..." FORCE)
endif()

#################
# Tweak version #
#################

if (SET_TWEAK AND EXISTS "${CMAKE_SOURCE_DIR}/.git")
    execute_process(
        COMMAND git describe --tags
        WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
        OUTPUT_VARIABLE PROJECT_VERSION_GIT
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    string(REGEX MATCH "-[0-9]+" PROJECT_VERSION_TWEAK "${PROJECT_VERSION_GIT}")
endif()
if(PROJECT_VERSION_TWEAK)
    string(REGEX MATCH "[0-9]+" PROJECT_VERSION_TWEAK_NUM "${PROJECT_VERSION_TWEAK}")
else()
    set(PROJECT_VERSION_TWEAK_NUM 0)
endif()

#############
# Text data #
#############

function(fastfetch_encode_c_string STR OUTVAR)
    string(REGEX REPLACE "\n$" "" TEMP "${STR}")  # Remove trailing newline
    string(REPLACE "\\" "\\\\" TEMP "${TEMP}")    # Escape backslashes
    string(REPLACE "\n" "\\n" TEMP "${TEMP}")     # Replace newlines with \n
    string(REPLACE "\"" "\\\"" TEMP "${TEMP}")    # Replace quotes with \"
    set(${OUTVAR} "\"${TEMP}\"" PARENT_SCOPE)
endfunction(fastfetch_encode_c_string)

function(fastfetch_load_text FILENAME OUTVAR)
    file(READ "${FILENAME}" TEMP)
    fastfetch_encode_c_string("${TEMP}" TEMP)
    set(${OUTVAR} "${TEMP}" PARENT_SCOPE)
endfunction(fastfetch_load_text)

find_package(Python)
if(Python_FOUND)
    message(STATUS "Minifying 'help.json'")
    execute_process(COMMAND ${Python_EXECUTABLE} -c "import json,sys;json.dump(json.load(sys.stdin),sys.stdout,separators=(',',':'))"
                    INPUT_FILE "${CMAKE_CURRENT_SOURCE_DIR}/src/data/help.json"
                    OUTPUT_VARIABLE DATATEXT_JSON_HELP)
    if(DATATEXT_JSON_HELP STREQUAL "")
        message(ERROR "DATATEXT_JSON_HELP is empty, which should not happen!")
    endif()
else()
    message(WARNING "Python3 is not found, 'help.json' will not be minified")
    file(READ "src/data/help.json" DATATEXT_JSON_HELP)
endif()

if(ENABLE_EMBEDDED_PCIIDS AND NOT EXISTS "${PROJECT_BINARY_DIR}/fastfetch_pciids.c.inc")
    if(Python_FOUND)
        if(NOT EXISTS "${PROJECT_BINARY_DIR}/pci.ids")
            message(STATUS "'${PROJECT_BINARY_DIR}/pci.ids' is missing, downloading...")
            file(DOWNLOAD "https://pci-ids.ucw.cz/v2.2/pci.ids" "${PROJECT_BINARY_DIR}/pci.ids")
        endif()
        message(STATUS "Generating 'fastfetch_pciids.c.inc'")
        execute_process(COMMAND ${Python_EXECUTABLE} "${CMAKE_CURRENT_SOURCE_DIR}/scripts/gen-pciids.py" "${PROJECT_BINARY_DIR}/pci.ids"
                        OUTPUT_FILE "${PROJECT_BINARY_DIR}/fastfetch_pciids.c.inc"
                        RESULT_VARIABLE PYTHON_PCIIDS_RETCODE)
        if(NOT PYTHON_PCIIDS_RETCODE EQUAL 0)
            file(REMOVE "${PROJECT_BINARY_DIR}/fastfetch_pciids.c.inc")
            message(WARNING "Failed to generate 'fastfetch_pciids.c.inc'")
            set(ENABLE_EMBEDDED_PCIIDS OFF)
        endif()
    else()
        message(WARNING "Python3 is not found, 'fastfetch_pciids.c.inc' will not be generated")
        set(ENABLE_EMBEDDED_PCIIDS OFF)
    endif()
endif()

if(ENABLE_EMBEDDED_AMDGPUIDS AND NOT EXISTS "${PROJECT_BINARY_DIR}/fastfetch_amdgpuids.c.inc")
    if(Python_FOUND)
        if(NOT EXISTS "${PROJECT_BINARY_DIR}/amdgpu.ids")
            message(STATUS "'${PROJECT_BINARY_DIR}/amdgpu.ids' is missing, downloading...")
            file(DOWNLOAD "https://gitlab.freedesktop.org/mesa/drm/-/raw/main/data/amdgpu.ids" "${PROJECT_BINARY_DIR}/amdgpu.ids")
        endif()
        message(STATUS "Generating 'fastfetch_amdgpuids.c.inc'")
        execute_process(COMMAND ${Python_EXECUTABLE} "${CMAKE_CURRENT_SOURCE_DIR}/scripts/gen-amdgpuids.py" "${PROJECT_BINARY_DIR}/amdgpu.ids"
                        OUTPUT_FILE "${PROJECT_BINARY_DIR}/fastfetch_amdgpuids.c.inc"
                        RESULT_VARIABLE PYTHON_AMDGPUIDS_RETCODE)
        if(NOT PYTHON_AMDGPUIDS_RETCODE EQUAL 0)
            file(REMOVE "${PROJECT_BINARY_DIR}/fastfetch_amdgpuids.c.inc")
            mes
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
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

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
* Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of
  any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address,
  without their explicit permission
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
Examples of representing our community include using an official email address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[INSERT CONTACT METHOD].
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

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

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
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
