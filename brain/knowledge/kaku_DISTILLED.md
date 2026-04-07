---
id: Kaku
type: knowledge
owner: OA_Triage
---
# Kaku
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <h1>Kaku</h1>
  <p><em>A fast, out-of-the-box terminal built for AI coding.</em></p>
</div>

<p align="center">
  <a href="https://github.com/tw93/Kaku/stargazers"><img src="https://img.shields.io/github/stars/tw93/Kaku?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/tw93/Kaku/releases"><img src="https://img.shields.io/github/v/tag/tw93/Kaku?label=version&style=flat-square" alt="Version"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/tw93/Kaku/commits"><img src="https://img.shields.io/github/commit-activity/m/tw93/Kaku?style=flat-square" alt="Commits"></a>
  <a href="https://twitter.com/HiTw93"><img src="https://img.shields.io/badge/follow-Tw93-red?style=flat-square&logo=Twitter" alt="Twitter"></a>
</p>

<p align="center">
  <img src="assets/kaku.jpeg" alt="Kaku Screenshot" width="1000" />
  <br/>
  Kaku is a deeply customized fork of <a href="https://github.com/wez/wezterm">WezTerm</a>, designed for an out-of-the-box experience.
</p>

## Features

- **Zero Config**: Defaults with JetBrains Mono, macOS font rendering, and low-res font sizing.
- **Theme-Aware Experience**: Auto-switches between dark and light modes with macOS, with tuned selection colors, font weight, and practical color overrides support.
- **Curated Shell Suite**: Built-in zsh plugins with optional CLI tools for prompt, diff, and navigation workflows.
- **Fast & Lightweight**: 40% smaller binary, instant startup, lazy loading, stripped-down GPU-accelerated core.
- **WezTerm-Compatible Config**: Use WezTerm's Lua config directly with full API compatibility and no migration.
- **Polished Defaults**: Copy on select, clickable file paths, history peek from full-screen apps, pane input broadcast, and visual bell on background tab completion.

## Quick Start

1. [Download Kaku DMG](https://github.com/tw93/Kaku/releases/latest) & Drag to Applications
2. Or install with Homebrew: `brew install tw93/tap/kakuku`
3. Open Kaku. The app is notarized by Apple, so it opens without security warnings
4. On first launch, Kaku will automatically set up your shell environment

## Usage Guide

Kaku comes with intuitive macOS-native shortcuts:

| Action | Shortcut |
| :--- | :--- |
| Toggle Global Window | `Cmd + Opt + Ctrl + K` |
| New Tab | `Cmd + T` |
| New Window | `Cmd + N` |
| Close Tab/Pane | `Cmd + W` |
| Navigate Tabs | `Cmd + Shift + [`, `Cmd + Shift + ]` or `Cmd + 1-9` |
| Navigate Panes | `Cmd + Opt + Arrows` |
| Split Pane Vertical | `Cmd + D` |
| Split Pane Horizontal | `Cmd + Shift + D` |
| Toggle Split Direction | `Cmd + Shift + S` |
| Zoom/Unzoom Pane | `Cmd + Shift + Enter` |
| Resize Pane | `Cmd + Ctrl + Arrows` |
| Open Settings Panel | `Cmd + ,` |
| Reopen Closed Tab | `Cmd + Shift + T` |
| Rename Tab | Double-click on tab title |
| Clear Screen | `Cmd + K` |
| Doctor Panel | `Ctrl + Shift + L` |
| AI Panel | `Cmd + Shift + A` |
| Kaku Assistant Apply Suggestion | `Cmd + Shift + E` |
| Open Lazygit | `Cmd + Shift + G` |
| Yazi File Manager | `Cmd + Shift + Y` or `y` |
| Font Size | `Cmd + +`, `Cmd + -`, `Cmd + 0` |
| Smart Jump | `z <dir>` |
| Smart Select | `z -l <dir>` |
| Recent Dirs | `z -t` |

## Configuration

Kaku comes with a carefully curated shell stack for immediate productivity, so you can focus on AI coding without opening vscode:

Built-in shell stack defaults are:

- **z**: A smarter cd command that learns your most used directories for instant navigation.
- **zsh-completions**: Extended command and subcommand completion definitions.
- **Syntax Highlighting**: Real-time command validation and coloring.
- **Autosuggestions**: Intelligent, history-based completions similar to Fish shell.
- **Fish-friendly integration**: `kaku init` now can provision `~/.config/kaku/fish/kaku.fish` for fish users, and `kaku doctor` verifies both zsh/fish integration paths.

Optional CLI tools installed via Homebrew during `kaku init`:

- **Starship**: A fast, customizable prompt showing the current directory, git branch, and package versions.
- **Delta**: A syntax-highlighting pager for git, diff, and grep output.
- **Lazygit**: A terminal UI for fast, visual Git workflows without leaving the shell.
- **Yazi**: A terminal file manager. Use `y` to launch it and sync the shell directory on exit.

Kaku uses `~/.config/kaku/kaku.lua` for configuration, fully compatible with WezTerm's Lua API, with built-in defaults at `Kaku.app/Contents/Resources/kaku.lua` as fallback.

Run `kaku config` or press `Cmd + ,` to open the Settings TUI and edit common options (font, theme, opacity, bells, scrollbars, Kaku Assistant) without manually editing config files. The settings panel uses grouped sections with a pinned footer showing contextual key hints.

To enable rounded scrollbars, open `kaku config` and toggle the scrollbar style option.

If you already use your own Zsh completion workflow such as `fzf-tab`, Kaku's Smart Tab only applies inside Kaku sessions by default. You can also disable it explicitly before loading Kaku shell integration:

```zsh
export KAKU_SMART_TAB_DISABLE=1
[[ ":$PATH:" != *":$HOME/.config/kaku/zsh/bin:"* ]] && export PATH="$HOME/.config/kaku/zsh/bin:$PATH"
[[ -f "$HOME/.config/kaku/zsh/kaku.zsh" ]] && source "$HOME/.config/kaku/zsh/kaku.zsh"
```

```fish
set -gx KAKU_SMART_TAB_DISABLE 1
if not contains -- "$HOME/.config/kaku/fish/bin" $PATH
  set -gx PATH "$HOME/.config/kaku/fish/bin" $PATH
end
if test -f "$HOME/.config/kaku/fish/kaku.fish"
  source "$HOME/.config/kaku/fish/kaku.fish"
fi
```

You can also remap true-color output from specific apps to keep theme consistency:

```lua
config.color_overrides = {
  ['#6E6E6E'] = '#3A3942',
}
```

Run `kaku` in your terminal to see all available commands such as `kaku ai`, `kaku config`, `kaku doctor`, `kaku update`, and `kaku reset`.

## Kaku AI

Kaku includes a built-in assistant for command-line error recovery and a single AI settings page for coding tools.

- **Kaku Assistant**: Automatically analyzes failed commands and prepares a safe command suggestion. Enable or disable it from `kaku config`.
- **AI Tools Config**: Manage settings for tools like Claude Code, Codex, Gemini CLI, Copilot CLI, Kimi Code, Factory Droid, and OpenClaw.

Open AI settings with `kaku ai` to configure your external AI tools and edit **Kaku Assistant** details after it is enabled.
For enterprise gateway/proxy headers, edit `~/.config/kaku/assistant.toml` and set `custom_headers` there.

Tip: DeepSeek-V3.2 is a great low-cost option to start with for everyday AI coding tasks.

When Kaku Assistant has a suggestion ready after a command error, press `Cmd + Shift + E` to apply it.

## Why Kaku?

I heavily rely on the CLI for both work and personal projects. Tools I've built, like [Mole](https://github.com/tw93/mole) and [Pake](https://github.com/tw93/pake), reflect this.

I used Alacritty for years and learned to value speed and simplicity. As my workflow shifted toward AI-assisted coding, I wanted stronger tab and pane ergonomics. I also explored Kitty, Ghostty, Warp, and iTerm2. Each is strong in different areas, but I still wanted a setup that matched my own balance of performance, defaults, and control.

WezTerm is robust and highly hackable, and I am grateful for its engine and ecosystem. Kaku builds on that foundation with practical defaults for day one use, while keeping full Lua-based customization and a fast, lightweight feel.

So I built Kaku to be that environment: fast, polished, and ready to work.

### Performance

| Metric | Upstream | Kaku | Methodology |
| :--- | :--- | :--- | :--- |
| **Executable Size** | ~67 MB | ~40 MB | Aggressive symbol stripping & feature pruning |
| **Resources Volume** | ~100 MB | ~80 MB | Asset optimization & lazy-loaded assets |
| **Launch Latency** | Standard | Instant | Just-in-time initialization |
| **Shell Bootstrap** | ~200ms | ~100ms | Optimized environment provisioning |

Achieved through aggressive stripping of unused features, lazy loading of color schemes, and shell optimizations.

## FAQ

1. **Is there a Windows or Linux version?**

   Not at the moment. Kaku is currently macOS-only while we focus on polishing the macOS experience. Windows and Linux versions may come later once the macOS version is mature.

2. **Can Kaku use transparent windows on macOS?**

   Yes. You can set `window_background_opacity` and optionally `macos_window_background_blur` in `~/.config/kaku/kaku.lua`. Transparent mode now keeps top/right/bottom padding regions visually consistent to avoid transparent gaps.

3. **How do I turn off copy on select?**

   Kaku enables copy on select by default; to disable automatic clipboard copy and copy toast after selection, add `config.copy_on_select = false` to `~/.config/kaku/kaku.lua`.

4. **Can I control working directory inheritance separately for new window, tab, and split?**

   Yes. Use these options in `~/.config/kaku/kaku.lua`:
   `config.window_inherit_working_directory`
   `config.tab_inherit_working_directory`
   `config.split_pane_inherit_working_directory`
   All are enabled by default.

5. **The `kaku` command is missing. How can I recover it and troubleshoot with Kaku Doctor?**

   Open Kaku Doctor from the Shell menu first. This diagnostic path can still run when your shell command entry is missing and will tell you what to repair.

   Then run this command in a terminal to restore the shell entry:

   ```bash
   /Applications/Kaku.app/Contents/MacOS/kaku init --update-only
   exec zsh -l
   ```

   Finally run `kaku doctor` in your terminal to verify everything is healthy.

6. **How can I use Kaku's CLI capabilities (like `split-pane`) from other scripts or tools?**

   Kaku exposes a powerful CLI for interacting with its multiplexer. For example, to split the current pane, run:

   ```bash
   kaku cli split-pane
   ```

   To split it and run a specific command instead of your default shell:

   ```bash
   kaku cli split-pane -- bash -c "echo Hello"
   ```

   You can explore all available CLI commands by running `kaku cli --help` or specifically `kaku cli split-pane --help`. This is very useful when integrating Kaku with workflows or AI tools.

## Contributors

Big thanks to all contributors who helped build Kaku. Go follow them! ❤️

<a href="https://github.com/tw93/Kaku/graphs/contributors">
  <img src="./CONTRIBUTORS.svg?v=2" width="1000" />
</a>

## Support

- If Kaku helped you, star the repo or [share it](https://twitter.com/intent/tweet?url=https://github.com/tw93/Kaku&text=Kaku%20-%20A%20fast%20terminal%20built%20for%20AI%20coding.) with friends.
- Got ideas or found bugs? Open an issue/PR or check [CONTRIBUTING.md](CONTRIBUTING.md) for details.
- Like Kaku? <a href="https://miaoyan.app/cats.html?name=Kaku" target="_blank">Buy Tw93 a Coke</a> to support the project! 🥤 Supporters below.

<a href="https://miaoyan.app/cats.html?name=Kaku"><img src="https://miaoyan.app/assets/sponsors.svg" width="1000" loading="lazy" /></a>

## License

MIT License, feel free to enjoy and participate in open source.

```

### File: CONTRIBUTING.md
```md
# Contributing to Kaku

## Setup

```bash
# Clone the repository
git clone https://github.com/tw93/Kaku.git
cd Kaku

# Install Rust if it isn't already available (Homebrew keeps rustup keg-only)
brew install rustup
echo "export PATH=\"$(brew --prefix rustup)/bin:\$HOME/.cargo/bin:\$PATH\"" >> ~/.zprofile
exec zsh -l
rustup toolchain install 1.93.0

# Install required tools (cargo-nextest, cargo-watch, nightly rustfmt)
make install-tools

# Install pre-commit hook (format + test before each commit)
make install-hooks
```

## Development

| Command | Purpose |
|---------|---------|
| `make fmt` | Auto-format code (requires nightly) |
| `make fmt-check` | Check formatting without modifying files |
| `make check` | Compile check, catch type/syntax errors |
| `make test` | Run unit tests |
| `make dev` | Fast local debug: build `kaku-gui` and run from `target/debug` |
| `make build` | Compile binaries (no app bundle) |
| `make app` | Build debug app bundle → `dist/Kaku.app` |

**Recommended workflow:**

```bash
make fmt        # format first
make check      # verify it compiles
make test       # run tests
make dev        # fast local run without packaging
```

You can override log level for `make dev`:

```bash
RUST_LOG=debug make dev
```

## Build Release

```bash
# Build application and DMG (release, universal binary)
./scripts/build.sh
# Outputs: dist/Kaku.app and dist/Kaku.dmg

# Build for current architecture only (faster, for local testing)
./scripts/build.sh --native-arch

# Build app bundle only (skip DMG creation)
./scripts/build.sh --native-arch --app-only

# Build and open the app automatically
./scripts/build.sh --native-arch --open
```

## Pull Requests

1. Fork and create a branch from `main`
2. Make changes
3. Run `make fmt && make check && make test`
4. Commit and push
5. Open PR targeting `main`

CI runs format check → unit tests → cargo check → universal build validation in order.

```

### File: LICENSE.md
```md
MIT License

Copyright (c) 2024-Present Tw93
Copyright (c) 2018-Present Wez Furlong (original WezTerm code)

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

---

**Attribution & Bundled Assets**

Kaku is a customized fork of [WezTerm](https://github.com/wez/wezterm), created by Wez Furlong.
Deep gratitude to Wez for building such a powerful terminal engine.

WezTerm bundles `JetBrains Mono`, `Noto Color Emoji` and `Roboto` fonts.
Those are distributed under the terms of the OFL 1.1, the text of which
can be found in the assets/fonts directory.

WezTerm bundles `Symbols Nerd Font Mono`, built from only those icon sets
available from https://github.com/ryanoasis/nerd-fonts which are clearly
distributed under the terms of the OFL 1.1.
Note that WezTerm excludes the Pomicons icon set from this collection.

```

### File: .github\RELEASE_NOTES.md
```md
# V0.8.0 Fish 🐟

<div align="center">
  <img src="https://raw.githubusercontent.com/tw93/Kaku/main/assets/logo.png" alt="Kaku Logo" width="120" height="120" />
  <h1 style="margin: 12px 0 6px;">Kaku V0.8.0</h1>
  <p><em>A fast, out-of-the-box terminal built for AI coding.</em></p>
</div>

### Changelog

1. **Fish Shell Support**: Full fish shell integration via `kaku init`, including Starship prompt, Yazi launcher, theme sync, and conf.d entrypoint.
2. **Bell Tab Indicator**: Background tabs show a bell prefix when tasks finish, with optional Dock badge and toggleable tab prefix.
3. **Remember Last Directory**: Kaku restores the last working directory when opening new tabs or windows. Can be disabled via `kaku config`.
4. **Update & Doctor in Tabs**: `kaku update` and `kaku doctor` now open in a dedicated tab instead of blocking the current session.
5. **Basename-only Tab Titles**: New `tab_title_basename_only` option to show just the directory name instead of the full path.
6. **Scrollback Fix**: Fixed viewport jumping to top during rapid output, snapping to bottom after scrolling up, and viewport jumping when using Claude Code.
7. **Bug Fixes & Close Shortcuts**: Fixed window hide, Cmd+Click links, clipboard paste, emoji width, and SSH alias conflicts. Close dialogs now support Enter to confirm and Esc to cancel.

### 更新日志

1. **Fish Shell 完整支持**：`kaku init` 现支持 fish shell 完整引导，含 Starship 提示符、Yazi 启动器、主题同步及 conf.d 入口。
2. **铃声标签指示器**：后台标签任务完成时显示铃声前缀，支持可选 Dock badge 和标签前缀开关。
3. **记住上次目录**：新标签和新窗口打开时自动恢复上次工作目录，可通过 `kaku config` 关闭。
4. **Update/Doctor 在标签中运行**：`kaku update` 和 `kaku doctor` 在独立标签中打开，不阻塞当前会话。
5. **仅显示目录名标签**：新增 `tab_title_basename_only` 选项，只显示目录名而非完整路径。
6. **滚动修复**：修复快速输出时 viewport 跳到顶部、往上滚动后自动跳回底部，以及 Claude Code 使用时 viewport 异常跳动的问题。
7. **Bug 修复**：修复窗口隐藏、Cmd+Click 链接、剪贴板粘贴、emoji 宽度、SSH alias 冲突。关闭确认弹窗现支持回车确认、Esc 取消。

Special thanks to @mystersu, @ddotz, @rookie-ricardo, @s010s, @anzksdk, @cynosurech, and @XinCao for their contributions to this release.

> https://github.com/tw93/Kaku

```

### File: scripts\bench_startup.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

# Cold-start benchmark: "open app" -> "first window exists"
# Results are printed directly in terminal (no file output).

RUNS="${RUNS:-10}"
WARMUP="${WARMUP:-5}"
WAIT_TIMEOUT_SEC="${WAIT_TIMEOUT_SEC:-15}"

if ! command -v hyperfine >/dev/null 2>&1; then
	printf 'Error: hyperfine is required. Install with: brew install hyperfine\n' >&2
	exit 1
fi

# Format: DisplayName:AppNameForOpen:ProcessNameForPgrep
declare -a TERMINALS=(
	"Kaku:Kaku:kaku-gui"
	"Ghostty:Ghostty:ghostty"
	"Alacritty:Alacritty:alacritty"
)

quit_app() {
	local proc="$1"
	pkill -9 -x "$proc" >/dev/null 2>&1 || true
	for _ in {1..200}; do
		if ! pgrep -x "$proc" >/dev/null 2>&1; then
			return 0
		fi
		sleep 0.05
	done
	return 0
}


wait_first_window() {
	local ui_name="$1"
	local timeout_sec="$2"

	# Avoid infinite wait: keep polling until timeout
	osascript <<OSA
set timeoutSeconds to ${timeout_sec}
set startAt to (current date)
tell application "System Events"
  repeat
    if exists process "${ui_name}" then
      tell process "${ui_name}"
        if (count of windows) > 0 then
          return
        end if
      end tell
    end if
    if ((current date) - startAt) > timeoutSeconds then
      error "timeout waiting first window for ${ui_name}" number 124
    end if
    delay 0.01
  end repeat
end tell
OSA
}

cold_start_once() {
	local app_name="$1"
	local proc_name="$2"

	quit_app "$proc_name"
	sleep 1.0
	sync

	open -na "$app_name"
	wait_first_window "$app_name" "$WAIT_TIMEOUT_SEC"
	quit_app "$proc_name"
}

export WAIT_TIMEOUT_SEC
export -f quit_app wait_first_window cold_start_once

printf 'Cleaning running terminals...\n'
pkill -9 kaku-gui 2>/dev/null || true
pkill -9 ghostty 2>/dev/null || true
pkill -9 alacritty 2>/dev/null || true
sleep 1

declare -a INSTALLED=()
declare -a HYPERFINE_ARGS=()

printf 'Checking installed apps...\n'
for term in "${TERMINALS[@]}"; do
	IFS=':' read -r display_name app_name proc_name <<<"$term"

	if [[ -d "/Applications/${app_name}.app" || -d "$HOME/Applications/${app_name}.app" ]]; then
		printf '  [+] %s\n' "$display_name"
		INSTALLED+=("$term")
		HYPERFINE_ARGS+=(--command-name "$display_name" "bash -c 'cold_start_once \"$app_name\" \"$proc_name\"'")
	else
		printf '  [-] %s (not found)\n' "$display_name"
	fi
done

if [[ ${#INSTALLED[@]} -lt 2 ]]; then
	printf 'Error: need at least 2 installed terminals to compare.\n' >&2
	exit 1
fi

printf '\nBenchmark config: runs=%s warmup=%s timeout=%ss\n\n' "$RUNS" "$WARMUP" "$WAIT_TIMEOUT_SEC"

hyperfine \
	--warmup "$WARMUP" \
	--runs "$RUNS" \
	--style full \
	--sort mean-time \
	"${HYPERFINE_ARGS[@]}"

```

### File: scripts\build.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

if [[ "${OSTYPE:-}" != darwin* ]]; then
	echo "This script is macOS-only." >&2
	exit 1
fi

# Keep vendored native deps on the same minimum macOS target as Rust.
export MACOSX_DEPLOYMENT_TARGET="${MACOSX_DEPLOYMENT_TARGET:-11.0}"
export CMAKE_OSX_DEPLOYMENT_TARGET="${CMAKE_OSX_DEPLOYMENT_TARGET:-11.0}"

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

APP_NAME="Kaku"
TARGET_DIR="${TARGET_DIR:-target}"
PROFILE="${PROFILE:-release}"
OUT_DIR="${OUT_DIR:-dist}"
OPEN_APP="${OPEN_APP:-0}"
APP_ONLY="${APP_ONLY:-0}"
BUILD_ARCH="${BUILD_ARCH:-}"
KAKU_REQUIRE_SIGNED_RELEASE="${KAKU_REQUIRE_SIGNED_RELEASE:-0}"

if [[ -z "$BUILD_ARCH" ]]; then
	if [[ "$PROFILE" == "release" || "$PROFILE" == "release-opt" ]]; then
		BUILD_ARCH="universal"
	else
		BUILD_ARCH="native"
	fi
fi

resolve_native_target() {
	case "$(uname -m)" in
	arm64 | aarch64)
		echo "aarch64-apple-darwin"
		;;
	x86_64)
		echo "x86_64-apple-darwin"
		;;
	*)
		echo "Unsupported macOS architecture: $(uname -m)" >&2
		exit 1
		;;
	esac
}

resolve_build_targets() {
	case "$BUILD_ARCH" in
	universal)
		echo "aarch64-apple-darwin x86_64-apple-darwin"
		;;
	native)
		echo "$(resolve_native_target)"
		;;
	arm64)
		echo "aarch64-apple-darwin"
		;;
	x86_64)
		echo "x86_64-apple-darwin"
		;;
	*)
		echo "Unsupported BUILD_ARCH=$BUILD_ARCH (expected: universal, native, arm64, x86_64)" >&2
		exit 1
		;;
	esac
}

require_command() {
	if ! command -v "$1" >/dev/null 2>&1; then
		echo "Missing required command: $1" >&2
		echo "Install the Rust toolchain bootstrap first, then retry." >&2
		echo "See CONTRIBUTING.md for setup instructions." >&2
		exit 1
	fi
}

is_developer_id_application_identity() {
	[[ "$1" == Developer\ ID\ Application:* ]]
}

detect_signing_identity() {
	local identities count

	if [[ -n "${KAKU_SIGNING_IDENTITY:-}" ]]; then
		if ! is_developer_id_application_identity "$KAKU_SIGNING_IDENTITY"; then
			echo "Warning: KAKU_SIGNING_IDENTITY is not a Developer ID Application certificate: $KAKU_SIGNING_IDENTITY" >&2
			echo "Notarization requires Developer ID Application signing." >&2
			return 1
		fi
		return 0
	fi

	identities=$(security find-identity -v -p codesigning 2>/dev/null | awk -F '"' '/Developer ID Application/{print $2}' || true)
	count=$(printf '%s\n' "$identities" | grep -c '^Developer ID Application:' || true)

	if [[ "$count" -ge 1 ]]; then
		KAKU_SIGNING_IDENTITY=$(printf '%s\n' "$identities" | head -n1)
		export KAKU_SIGNING_IDENTITY
		if [[ "$count" -gt 1 ]]; then
			echo "Release build: found multiple Developer ID Application certificates, auto-selecting: $KAKU_SIGNING_IDENTITY"
		else
			echo "Release build: auto-detected signing identity: $KAKU_SIGNING_IDENTITY"
		fi
		return 0
	fi

	echo "Warning: no Developer ID Application certificate found in Keychain." >&2
	return 1
}

codesign_with_retry() {
	local max_attempts=3
	local delay_seconds=15
	local attempt=1
	local output rc

	while (( attempt <= max_attempts )); do
		if output=$(codesign "$@" 2>&1); then
			if [[ -n "$output" ]]; then
				printf '%s\n' "$output"
			fi
			return 0
		fi

		rc=$?
		printf '%s\n' "$output" >&2

		if [[ "$output" != *"timestamp service is not available"* ]]; then
			return "$rc"
		fi

		if (( attempt == max_attempts )); then
			echo "codesign failed after $max_attempts attempts because the Apple timestamp service remained unavailable." >&2
			return "$rc"
		fi

		echo "codesign timestamp service unavailable, retrying in ${delay_seconds}s (attempt ${attempt}/${max_attempts})..." >&2
		sleep "$delay_seconds"
		attempt=$((attempt + 1))
	done
}

ensure_rust_targets() {
	local installed
	local missing=()

	installed="$(rustup target list --installed)"
	for target in "$@"; do
		if ! grep -Fxq "$target" <<<"$installed"; then
			missing+=("$target")
		fi
	done

	if [[ ${#missing[@]} -gt 0 ]]; then
		echo "Installing missing Rust targets: ${missing[*]}"
		rustup target add "${missing[@]}"
	fi
}

for arg in "$@"; do
	case "$arg" in
	--open) OPEN_APP=1 ;;
	--app-only) APP_ONLY=1 ;;
	--native-arch) BUILD_ARCH="native" ;;
	esac
done

require_command cargo
require_command rustup

APP_BUNDLE_SRC="assets/macos/Kaku.app"
APP_BUNDLE_OUT="$OUT_DIR/$APP_NAME.app"

echo "[1/7] Building binaries ($PROFILE, $BUILD_ARCH)..."
PROFILE_DIR="debug"
CARGO_PROFILE_ARGS=()
if [[ "$PROFILE" == "release" ]]; then
	CARGO_PROFILE_ARGS=(--release)
	PROFILE_DIR="release"
elif [[ "$PROFILE" == "release-opt" ]]; then
	CARGO_PROFILE_ARGS=(--profile release-opt)
	PROFILE_DIR="release-opt"
fi

if ! BUILD_TARGETS_STR="$(resolve_build_targets)"; then
	exit 1
fi

BUILD_TARGETS=()
IFS=' ' read -r -a BUILD_TARGETS <<<"$BUILD_TARGETS_STR"
if [[ ${#BUILD_TARGETS[@]} -eq 0 ]]; then
	echo "No build targets resolved for BUILD_ARCH=$BUILD_ARCH" >&2
	exit 1
fi

ensure_rust_targets "${BUILD_TARGETS[@]}"

for target in "${BUILD_TARGETS[@]}"; do
	echo "Building target: $target"
	CARGO_TERM_PROGRESS_WHEN=auto cargo build --locked ${CARGO_PROFILE_ARGS[@]+"${CARGO_PROFILE_ARGS[@]}"} --target "$target" --target-dir "$TARGET_DIR" -p kaku-gui -p kaku
done

if [[ "$BUILD_ARCH" == "universal" ]]; then
	BIN_DIR="$TARGET_DIR/universal/$PROFILE_DIR"
	mkdir -p "$BIN_DIR"
	for bin in kaku kaku-gui; do
		lipo -create \
			-output "$BIN_DIR/$bin" \
			"$TARGET_DIR/aarch64-apple-darwin/$PROFILE_DIR/$bin" \
			"$TARGET_DIR/x86_64-apple-darwin/$PROFILE_DIR/$bin"
		chmod +x "$BIN_DIR/$bin"
	done
else
	BIN_DIR="$TARGET_DIR/${BUILD_TARGETS[0]}/$PROFILE_DIR"
fi

for bin in kaku kaku-gui; do
	echo -n "Built $bin: "
	lipo -info "$BIN_DIR/$bin"
done

echo "[2/7] Preparing app bundle..."
rm -rf "$APP_BUNDLE_OUT"
mkdir -p "$OUT_DIR"
cp -R "$APP_BUNDLE_SRC" "$APP_BUNDLE_OUT"

# Move libraries from root to Frameworks (macOS requirement)
if ls "$APP_BUNDLE_OUT"/*.dylib 1>/dev/null 2>&1; then
	mkdir -p "$APP_BUNDLE_OUT/Contents/Frameworks"
	mv "$APP_BUNDLE_OUT"/*.dylib "$APP_BUNDLE_OUT/Contents/Frameworks/"
fi

mkdir -p "$APP_BUNDLE_OUT/Contents/MacOS"
mkdir -p "$APP_BUNDLE_OUT/Contents/Resources"

echo "[2.5/7] Syncing version from Cargo.toml..."
# Extract version from kaku/Cargo.toml (assuming it's the source of truth)
VERSION=$(grep '^version =' kaku/Cargo.toml | head -n 1 | cut -d '"' -f2)
if [[ -n "$VERSION" ]]; then
	echo "Stamping version $VERSION into Info.plist"
	/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString $VERSION" "$APP_BUNDLE_OUT/Contents/Info.plist"
	/usr/libexec/PlistBuddy -c "Set :CFBundleVersion $VERSION" "$APP_BUNDLE_OUT/Contents/Info.plist"
else
	echo "Warning: Could not detect version from kaku/Cargo.toml"
fi

echo "[3/7] Downloading vendor plugins..."
./scripts/download_vendor.sh

echo "[4/7] Copying resources and binaries..."
cp -R assets/shell-integration/* "$APP_BUNDLE_OUT/Contents/Resources/"
cp -R assets/shell-completion "$APP_BUNDLE_OUT/Contents/Resources/"
cp -R assets/fonts "$APP_BUNDLE_OUT/Contents/Resources/"
mkdir -p "$APP_BUNDLE_OUT/Contents/Resources/vendor"
for vendor_item in starship.toml zsh-z zsh-autosuggestions zsh-syntax-highlighting zsh-completions; do
	src_path="assets/vendor/$vendor_item"
	if [[ -e "$src_path" ]]; then
		cp -R "$src_path" "$APP_BUNDLE_OUT/Contents/Resources/vendor/"
	else
		echo "Warning: missing vendor item: $src_path"
	fi
done
cp assets/shell-integration/first_run.sh "$APP_BUNDLE_OUT/Contents/Resources/"
chmod +x "$APP_BUNDLE_OUT/Contents/Resources/first_run.sh"

# Explicitly use the logo.icns from assets if available
if [[ -f "assets/logo.icns" ]]; then
	cp "assets/logo.icns" "$APP_BUNDLE_OUT/Contents/Resources/terminal.icns"
fi

if ! tic -xe kaku -o "$APP_BUNDLE_OUT/Contents/Resources/terminfo" termwiz/data/kaku.terminfo; then
	echo "Warning: 'tic -xe' failed (some ncurses/tic variants). Falling back to full compile mode."
	tic -x -o "$APP_BUNDLE_OUT/Contents/Resources/terminfo" termwiz/data/kaku.terminfo
fi

for bin in kaku kaku-gui; do
	cp "$BIN_DIR/$bin" "$APP_BUNDLE_OUT/Contents/MacOS/$bin"
	chmod +x "$APP_BUNDLE_OUT/Contents/MacOS/$bin"
done

# Clean up xattrs to prevent icon caching issues or quarantine
xattr -cr "$APP_BUNDLE_OUT"

echo "[5/7] Signing app bundle..."
# Signing strategy:
# - Dev builds (PROFILE=dev): Always use ad-hoc signing (-) for speed
# - Release builds (PROFILE=release/release-opt): Use KAKU_SIGNING_IDENTITY or auto-detect a Developer ID Application certificate
# Usage with developer certificate:
#   KAKU_SIGNING_IDENTITY="Developer ID Application: Your Name (TEAMID)" ./scripts/build.sh
if [[ "$KAKU_REQUIRE_SIGNED_RELEASE" == "1" && ( "$PROFILE" == "dev" || "$PROFILE" == "debug" ) ]]; then
	echo "Error: signed release requires PROFILE=release or PROFILE=release-opt, got PROFILE=$PROFILE" >&2
	exit 1
fi

if [[ "$PROFILE" == "dev" || "$PROFILE" == "debug" ]]; then
	SIGNING_IDENTITY="-"
	echo "Dev build: using ad-hoc signing"
else
	if detect_signing_identity; then
		SIGNING_IDENTITY="$KAKU_SIGNING_IDENTITY"
		echo "Release build: signing with developer certificate"
	else
		if [[ "$KAKU_REQUIRE_SIGNED_RELEASE" == "1" ]]; then
			echo "Error: release build requires a Developer ID Application certificate. Set KAKU_SIGNING_IDENTITY or install one in Keychain." >&2
			exit 1
		fi
		SIGNING_IDENTITY="-"
		echo "Release build: using ad-hoc signing (set KAKU_SIGNING_IDENTITY or install a single Developer ID Application certificate for notarization)"
	fi
fi

BASE_SIGN_ARGS=(
	--force
	--sign "$SIGNING_IDENTITY"
)

RUNTIME_SIGN_ARGS=(
	"${BASE_SIGN_ARGS[@]}"
	--options runtime
	--entitlements assets/macos/Kaku.entitlements
)

if [[ "$SIGNING_IDENTITY" == "-" ]]; then
	BUNDLE_ID="$(/usr/libexec/PlistBuddy -c "Print :CFBundleIdentifier" "$APP_BUNDLE_OUT/Contents/Info.plist" 2>/dev/null || true)"
	if [[ -n "$BUNDLE_ID" ]]; then
		# Keep designated requirement stable across local ad-hoc builds so macOS TCC
		# does not treat each rebuilt app as a brand-new identity.
		echo "Ad-hoc signing with stable designated requirement: $BUNDLE_ID"
	else
		echo "Warning: CFBundleIdentifier not found. Falling back to default ad-hoc requirement."
	fi
fi

touch "$APP_BUNDLE_OUT/Contents/Resources/terminal.icns"
touch "$APP_BUNDLE_OUT/Contents/Info.plist"
touch "$APP_BUNDLE_OUT"

while IFS= read -r -d '' dylib; do
	codesign_with_retry "${BASE_SIGN_ARGS[@]}" "$dylib"
done < <(find "$APP_BUNDLE_OUT/Contents/Frameworks" -type f -name '*.dylib' -print0 | sort -z)

for bin in "$APP_BUNDLE_OUT/Contents/MacOS/kaku" "$APP_BUNDLE_OUT/Contents/MacOS/kaku-gui"; do
	codesign_with_retry "${RUNTIME_SIGN_ARGS[@]}" "$bin"
done

APP_SIGN_ARGS=("${RUNTIME_SIGN_ARGS[@]}")
if [[ "$SIGNING_IDENTITY" == "-" && -n "${BUNDLE_ID:-}" ]]; then
	APP_SIGN_ARGS+=("-r=designated => identifier \"$BUNDLE_ID\"")
fi

codesign_with_retry "${APP_SIGN_ARGS[@]}" "$APP_BUNDLE_OUT"

if [[ "$APP_ONLY" == "1" ]]; then
	echo "App bundle ready: $APP_BUNDLE_OUT"
	if [[ "$OPEN_APP" == "1" ]]; then open "$APP_BUNDLE_OUT"; fi
	exit 0
fi

UPDATE_ZIP_NAME="kaku_for_update.zip"
UPDATE_ZIP_PATH="$OUT_DIR/$UPDATE_ZIP_NAME"
UPDATE_SHA_PATH="$OUT_DIR/${UPDATE_ZIP_NAME}.sha256"

echo "[6/7] Creating auto-update archive..."
rm -f "$UPDATE_ZIP_PATH" "$UPDATE_SHA_PATH"
/usr/bin/ditto -c -k --sequesterRsrc --keepParent "$APP_BUNDLE_OUT" "$UPDATE_ZIP_PATH"
(
	cd "$OUT_DIR"
	/usr/bin/shasum -a 256 "$UPDATE_ZIP_NAME" >"$(basename "$UPDATE_SHA_PATH")"
)
echo "Update archive created: $UPDATE_ZIP_PATH"
echo "Update checksum created: $UPDATE_SHA_PATH"

echo "[7/7] Creating DMG..."
DMG_NAME="$APP_NAME.dmg"
DMG_PATH="$OUT_DIR/$DMG_NAME"
DMG_BASE_PATH="$OUT_DIR/$APP_NAME"
TEMP_DMG_PATH="$OUT_DIR/${APP_NAME}-temp.dmg"
STAGING_DIR="$OUT_DIR/dmg_staging"
BACKGROUND_IMAGE_SOURCE="assets/macos/dmg/background.png"
BACKGROUND_IMAGE_NAME="background.png"

hdiutil_cmd() {
	LC_ALL=C LANG=en_US.UTF-8 hdiutil "$@"
}

cleanup_volumes() {
	local vol_pattern="/Volumes/$APP_NAME"
	local max_attempts=15
	local attempt=1

	while [ $attempt -le $max_attempts ]; do
		if hdiutil_cmd info | grep -q "$vol_pattern"; then
			echo "Detaching existing volumes (Attempt $attempt/$max_attempts)..."
			hdiutil_cmd info | grep "$vol_pattern" | awk '{print $1}' | while read -r dev; do
				echo "Force detaching $dev..."
				hdiutil_cmd detach "$dev" -force || true
			done
			sleep 1
		else
			if [ -d "$vol_pattern" ]; then
				echo "Removing stale mount point directory $vol_pattern..."
				rmdir "$vol_pattern" || true
			fi
			return 0
		fi
		attempt=$((attempt + 1))
	done
	echo "Warning: Failed to fully detach volumes after $max_attempts attempts."
}

configure_dmg_layout() {
	local disk_name="$1"
	local app_name="$2"
	local background_name="$3"

	osascript >/dev/null <<EOF
tell application "Finder"
	tell disk "${disk_name}"
		open
		set current view of container window to icon view
		set toolbar visible of container window to false
		set statusbar visible of container window to false
		set the bounds of container window to {100, 100, 780, 520}
		set viewOptions to the icon view options of container window
		set arrangement of viewOptions to not arranged
		set icon size of viewOptions to 120
		set text size of viewOptions to 14
		try
			set background picture of viewOptions to file ".background:${background_name}"
		end try
		set position of item "${app_name}.app" of container window to {190, 245}
		set position of item "Applications" of container window to {500, 245}
		close
		open
		update without registering applications
		delay 1
	end tell
end tell
EOF
}

cleanup_volumes

/bin/sync

rm -rf "$DMG_PATH" "$TEMP_DMG_PATH" "$STAGING_DIR" "$DMG_BASE_PATH.dmg"
mkdir -p "$STAGING_DIR"

cp -R "$APP_BUNDLE_OUT" "$STAGING_DIR/"
ln -s /Applications "$STAGING_DIR/Applications"

if [[ -f "$BACKGROUND_IMAGE_SOURCE" ]]; then
	mkdir -p "$STAGING_DIR/.background"
	cp "$BACKGROUND_IMAGE_SOURCE" "$STAGING_DIR/.background/$BACKGROUND_IMAGE_NAME"
else
	echo "Warning: DMG background image not found at $BACKGROUND_IMAGE_SOURCE; using default Finder background."
fi

mdutil -i off "$STAGING_DIR" >/dev/null 2>&1 || true

echo "Creating DMG..."
MAX_RETRIES=3
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
	if ! hdiutil_cmd create -quiet -volname "$APP_NAME" \
		-srcfolder "$STAGING_DIR" \
		-ov -format UDRW \
		"$TEMP_DMG_PATH"; then
		echo "hdiutil create failed. Retrying in 2 seconds... ($((RETRY_COUNT + 1))/$MAX_RETRIES)"
		cleanup_volumes
		sleep 2
		RETRY_COUNT=$((RETRY_COUNT + 1))
		continue
	fi

	ATTACH_OUTPUT=$(hdiutil_cmd attach -readwrite -noverify -noautoopen "$TEMP_DMG_PATH" 2>/dev/null || true)
	DEVICE=$(echo "$ATTACH_OUTPUT" | awk '/\/dev\// {print $1; exit}')
	MOUNT_POINT=$(echo "$ATTACH_OUTPUT" | awk -F'\t' '/\/Volumes\// {print $NF; exit}')
	MOUNT_NAME=$(basename "$MOUNT_POINT")

	if [[ -z "$DEVICE" || -z "$MOUNT_POINT" ]]; then
		echo "Failed to attach temporary DMG. Retrying..."
		if [[ -n "${DEVICE:-}" ]]; then
			hdiutil_cmd detach "$DEVICE" -force >/dev/null 2>&1 || true
		fi
		cleanup_volumes
		sleep 2
		RETRY_COUNT=$((RETRY_COUNT + 1))
		continue
	fi

	if ! configure_dmg_layout "$MOUNT_NAME" "$APP_NAME" "$BACKGROUND_
... [TRUNCATED]
```

### File: scripts\check_config_release_readiness.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

VERSION_FILE="assets/shell-integration/config_version.txt"
HIGHLIGHTS_FILE="assets/shell-integration/config_update_highlights.tsv"
CHECK_SCRIPT="assets/shell-integration/check_config_version.sh"
FIRST_RUN_SCRIPT="assets/shell-integration/first_run.sh"
KAKU_LUA="assets/macos/Kaku.app/Contents/Resources/kaku.lua"

file_contains_literal() {
	local needle="$1"
	local file="$2"

	if command -v rg >/dev/null 2>&1; then
		rg -Fq -- "$needle" "$file"
	else
		grep -Fq -- "$needle" "$file"
	fi
}

if [[ ! -f "$VERSION_FILE" ]]; then
	echo "Missing config version file: $VERSION_FILE" >&2
	exit 1
fi

config_version="$(tr -d '[:space:]' < "$VERSION_FILE" || true)"
if [[ ! "$config_version" =~ ^[0-9]+$ ]]; then
	echo "Invalid config version in $VERSION_FILE: $config_version" >&2
	exit 1
fi

if [[ ! -f "$HIGHLIGHTS_FILE" ]]; then
	echo "Missing config highlights file: $HIGHLIGHTS_FILE" >&2
	exit 1
fi

if ! awk -F '\t' '
	BEGIN { ok = 1 }
	NF == 0 { next }
	$0 ~ /^[[:space:]]*#/ { next }
	NF < 2 || $1 !~ /^[0-9]+$/ || $2 == "" { ok = 0 }
	END { exit ok ? 0 : 1 }
' "$HIGHLIGHTS_FILE"; then
	echo "Invalid config highlights format in $HIGHLIGHTS_FILE" >&2
	exit 1
fi

for script in "$CHECK_SCRIPT" "$FIRST_RUN_SCRIPT"; do
	if ! file_contains_literal 'read_bundled_config_version "$SCRIPT_DIR"' "$script"; then
		echo "Expected $script to read config_version.txt via read_bundled_config_version" >&2
		exit 1
	fi
done

if ! file_contains_literal 'config_version.txt' "$KAKU_LUA"; then
	echo "Expected $KAKU_LUA to read config_version.txt" >&2
	exit 1
fi

echo "Config release readiness passed for version $config_version"

```

### File: scripts\check_release_config.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

VERSION_FILE="assets/shell-integration/config_version.txt"
HIGHLIGHTS_FILE="assets/shell-integration/config_update_highlights.tsv"
TAG_PATTERN='^[Vv][0-9]+\.[0-9]+\.[0-9]+$'
current_release_version=$(grep '^version =' "$REPO_ROOT/kaku/Cargo.toml" | head -n1 | cut -d'"' -f2)

echo "=== Config Version Check ==="
echo ""

current_config_version=$(cat "$VERSION_FILE" | tr -d '[:space:]')
echo "Current config version: $current_config_version"

previous_tag=$(
    git tag --sort=-version:refname \
        | grep -E "$TAG_PATTERN" \
        | grep -Eiv "^v${current_release_version}$" \
        | head -n 1
)

if [[ -z "$previous_tag" ]]; then
    echo "Warning: no previous release tag found, skipping previous release comparison"
    previous_config_version=""
else
    previous_config_version=$(git show "${previous_tag}:${VERSION_FILE}" 2>/dev/null | tr -d '[:space:]' || true)
    if [[ ! "$previous_config_version" =~ ^[0-9]+$ ]]; then
        echo "Warning: could not read config version from $previous_tag, skipping previous release comparison"
        previous_config_version=""
    else
        echo "Previous release tag: $previous_tag"
        echo "Previous release config version: $previous_config_version"
    fi
fi

if [[ -n "$previous_config_version" ]]; then
    expected_config_version=$((previous_config_version + 1))
    echo "Expected config version for this release: $expected_config_version"
    echo ""

    if [[ "$current_config_version" -ne "$expected_config_version" ]]; then
        echo "Error: config version is incorrect"
        echo "  Repository value: $current_config_version"
        echo "  Expected value:   $expected_config_version"
        exit 1
    fi
fi

new_highlights=$(grep "^$current_config_version	" "$HIGHLIGHTS_FILE" 2>/dev/null || echo "")

if [[ -z "$new_highlights" ]]; then
    echo "Warning: no highlights found for version $current_config_version"
    echo ""
    echo "If this release updates bundled config behavior, add entries to $HIGHLIGHTS_FILE:"
    echo "$current_config_version	<更新内容（英文）>"
    echo "$current_config_version	<更新内容（中文）>"
    echo ""
    echo "Versions currently present in the highlights file:"
    cut -f1 "$HIGHLIGHTS_FILE" | sort -u -n | tail -5
    exit 1
else
    echo "Found highlights for version $current_config_version:"
    echo "$new_highlights" | head -3
    echo ""

    count=$(echo "$new_highlights" | wc -l)
    echo "Total highlight entries: $count"

    if [[ $count -lt 2 ]]; then
        echo "Error: at least 2 highlight entries are required for version $current_config_version"
        echo "Add matching English and Chinese entries to $HIGHLIGHTS_FILE"
        exit 1
    fi
fi

echo ""
echo "Config version check passed"

```

### File: scripts\check_release_notes.sh
```sh
#!/usr/bin/env bash
# Check if RELEASE_NOTES.md version matches Cargo.toml version
# Usage: ./check_release_notes.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RELEASE_NOTES="$REPO_ROOT/.github/RELEASE_NOTES.md"

# Get version from Cargo.toml
cargo_version="$(grep '^version =' "$REPO_ROOT/kaku/Cargo.toml" | head -n1 | cut -d'"' -f2)"

if [[ ! -f "$RELEASE_NOTES" ]]; then
    echo "❌ RELEASE_NOTES.md not found at $RELEASE_NOTES" >&2
    exit 1
fi

# Extract version from RELEASE_NOTES.md title (format: # V0.7.0 or # 0.7.0)
notes_version=$(head -n1 "$RELEASE_NOTES" | grep -oE '[vV]?[0-9]+\.[0-9]+\.[0-9]+' | sed 's/^[vV]//' || true)

if [[ -z "$notes_version" ]]; then
    echo "❌ Could not extract version from RELEASE_NOTES.md title" >&2
    echo "   Expected format: '# V0.7.0' or '# 0.7.0'" >&2
    exit 1
fi

if [[ "$notes_version" != "$cargo_version" ]]; then
    echo "❌ Version mismatch!" >&2
    echo "   Cargo.toml:  $cargo_version" >&2
    echo "   RELEASE_NOTES: $notes_version" >&2
    exit 1
fi

echo "✓ RELEASE_NOTES.md version matches: v$cargo_version"

```

### File: scripts\download_vendor.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

# This script downloads plugin dependencies bundled into the Kaku App.
# CLI tools (starship/git-delta/lazygit) are installed via Homebrew at init time.

VENDOR_DIR="$(cd "$(dirname "$0")/../assets/vendor" && pwd)"
mkdir -p "$VENDOR_DIR"

download_pinned_repo() {
	local step="$1"
	local name="$2"
	local repo="$3"
	local ref="$4"
	local dest="$VENDOR_DIR/$name"
	local marker_file="$dest/.kaku-vendor-ref"
	local archive_url="https://codeload.github.com/$repo/tar.gz/$ref"
	local temp_dir
	local extract_dir
	local archive_path
	local source_dir

	echo "[$step/4] Syncing $name @ $ref..."
	if [[ -f "$marker_file" ]] && [[ "$(cat "$marker_file")" == "$ref" ]]; then
		echo "$name already pinned to $ref, skipping."
		return
	fi

	temp_dir="$(mktemp -d)"
	trap 'rm -rf "$temp_dir"' RETURN
	extract_dir="$temp_dir/extract"
	archive_path="$temp_dir/$name.tar.gz"
	mkdir -p "$extract_dir"

	curl --fail --location --silent --show-error --retry 3 --retry-delay 2 "$archive_url" --output "$archive_path"
	tar -xzf "$archive_path" -C "$extract_dir"
	source_dir="$(find "$extract_dir" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
	if [[ -z "$source_dir" ]]; then
		echo "Failed to unpack $name from $archive_url" >&2
		exit 1
	fi

	rm -rf "$dest"
	mv "$source_dir" "$dest"
	printf '%s\n' "$ref" > "$marker_file"
	trap - RETURN
	rm -rf "$temp_dir"
}

echo "[0/4] Cleaning legacy vendor binaries..."
rm -f "$VENDOR_DIR/starship" "$VENDOR_DIR/delta" "$VENDOR_DIR/zoxide"
rm -rf "$VENDOR_DIR/completions" "$VENDOR_DIR/man"
rm -f "$VENDOR_DIR/README.md" "$VENDOR_DIR/CHANGELOG.md" "$VENDOR_DIR/LICENSE"

# Pin external shell integrations to exact commits so app/release artifacts stay reproducible.
download_pinned_repo "1" "zsh-autosuggestions" "zsh-users/zsh-autosuggestions" "85919cd1ffa7d2d5412f6d3fe437ebdbeeec4fc5"
download_pinned_repo "2" "zsh-syntax-highlighting" "zsh-users/zsh-syntax-highlighting" "1d85c692615a25fe2293bdd44b34c217d5d2bf04"
download_pinned_repo "3" "zsh-completions" "zsh-users/zsh-completions" "84615f3d0b0e943d5b1de862c9552e572c8e70bb"
download_pinned_repo "4" "zsh-z" "agkozak/zsh-z" "cf9225feebfae55e557e103e95ce20eca5eff270"

echo "Vendor dependencies downloaded to $VENDOR_DIR"

```

### File: scripts\notarize.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

# Notarization script for Kaku macOS app
# Usage: ./scripts/notarize.sh [--staple-only]
#
# Prerequisites:
# 1. App must be signed with Developer ID
# 2. Set environment variables (or use macOS Keychain):
#    - KAKU_NOTARIZE_APPLE_ID: Your Apple ID email
#    - KAKU_NOTARIZE_TEAM_ID: Your Team ID (10 characters)
#    - KAKU_NOTARIZE_PASSWORD: App-specific password (not your Apple ID password)
#
# To generate app-specific password:
# https://appleid.apple.com/account/manage -> Sign-In and Security -> App-Specific Passwords

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

APP_NAME="Kaku"
OUT_DIR="${OUT_DIR:-dist}"
APP_BUNDLE="${OUT_DIR}/${APP_NAME}.app"
DMG_PATH="${OUT_DIR}/${APP_NAME}.dmg"
NOTARY_SUBMIT_MAX_ATTEMPTS="${NOTARY_SUBMIT_MAX_ATTEMPTS:-3}"
NOTARY_SUBMIT_RETRY_DELAY="${NOTARY_SUBMIT_RETRY_DELAY:-20}"

STAPLE_ONLY=0
for arg in "$@"; do
	case "$arg" in
	--staple-only) STAPLE_ONLY=1 ;;
	esac
done

is_valid_team_id() {
	[[ "$1" =~ ^[A-Z0-9]{10}$ ]]
}

require_developer_id_signature() {
	local metadata
	local signed_team_id

	metadata=$(codesign -dvvvv "$APP_BUNDLE" 2>&1) || {
		echo "Error: failed to inspect app signature." >&2
		return 1
	}

	if ! grep -q "^Authority=Developer ID Application:" <<<"$metadata"; then
		echo "Error: App must be signed with a Developer ID Application certificate before notarization." >&2
		echo "Rebuild with ./scripts/build.sh after installing a single Developer ID Application certificate, or set KAKU_SIGNING_IDENTITY explicitly." >&2
		echo "$metadata" | grep -E "^(Authority=|TeamIdentifier=|Signature=)" >&2 || true
		return 1
	fi

	signed_team_id=$(echo "$metadata" | awk -F= '/^TeamIdentifier=/{print $2; exit}')
	if ! is_valid_team_id "$signed_team_id"; then
		echo "Error: App signature does not contain a valid TeamIdentifier." >&2
		echo "$metadata" | grep -E "^(Authority=|TeamIdentifier=|Signature=)" >&2 || true
		return 1
	fi
}

# Check if app exists
if [[ ! -d "$APP_BUNDLE" ]]; then
	echo "Error: $APP_BUNDLE not found. Run ./scripts/build.sh first."
	exit 1
fi

# Verify signing
if ! codesign -v "$APP_BUNDLE" 2>/dev/null; then
	echo "Error: App is not signed. Re-run ./scripts/build.sh with a Developer ID Application certificate available."
	exit 1
fi

require_developer_id_signature || exit 1

echo "App: $APP_BUNDLE"
echo "DMG: $DMG_PATH"

# Get credentials from environment or Keychain
APPLE_ID="${KAKU_NOTARIZE_APPLE_ID:-}"
TEAM_ID="${KAKU_NOTARIZE_TEAM_ID:-}"
PASSWORD="${KAKU_NOTARIZE_PASSWORD:-}"

if [[ -n "$TEAM_ID" ]] && ! is_valid_team_id "$TEAM_ID"; then
	echo "Warning: ignoring invalid KAKU_NOTARIZE_TEAM_ID: $TEAM_ID"
	TEAM_ID=""
fi

# If not set via env, try to read from Keychain
if [[ -z "$APPLE_ID" ]]; then
	echo "Checking Keychain for notarization credentials..."
	APPLE_ID=$(security find-generic-password -s "kaku-notarize-apple-id" -w 2>/dev/null || true)
fi

if [[ -z "$PASSWORD" ]]; then
	PASSWORD=$(security find-generic-password -s "kaku-notarize-password" -w 2>/dev/null || true)
fi

if [[ -z "$TEAM_ID" ]]; then
	# Try to extract from signing identity
	TEAM_ID=$(codesign -dv "$APP_BUNDLE" 2>&1 | grep TeamIdentifier | head -1 | awk -F= '{print $2}')
	if [[ -n "$TEAM_ID" ]] && ! is_valid_team_id "$TEAM_ID"; then
		echo "Warning: ignoring invalid TeamIdentifier from app signature: $TEAM_ID"
		TEAM_ID=""
	fi
	if [[ -n "$TEAM_ID" ]]; then
		echo "Using Team ID from signature: $TEAM_ID"
	fi
fi

if [[ -z "$APPLE_ID" || -z "$PASSWORD" || -z "$TEAM_ID" ]]; then
	echo ""
	echo "Error: Notarization credentials not found."
	echo ""
	echo "Please set environment variables:"
	echo "  export KAKU_NOTARIZE_APPLE_ID='your-apple-id@example.com'"
	echo "  export KAKU_NOTARIZE_TEAM_ID='YOURTEAMID'"
	echo "  export KAKU_NOTARIZE_PASSWORD='xxxx-xxxx-xxxx-xxxx'"
	echo ""
	echo "Or store in Keychain:"
	echo "  security add-generic-password -s 'kaku-notarize-apple-id' -a 'kaku' -w 'your-apple-id@example.com'"
	echo "  security add-generic-password -s 'kaku-notarize-password' -a 'kaku' -w 'your-app-specific-password'"
	echo ""
	echo "To generate app-specific password: https://appleid.apple.com/account/manage"
	exit 1
fi

if [[ "$STAPLE_ONLY" == "1" ]]; then
	echo "Stapling existing notarization ticket..."

	echo "Stapling app bundle..."
	xcrun stapler staple "$APP_BUNDLE"

	if [[ -f "$DMG_PATH" ]]; then
		echo "Stapling DMG..."
		xcrun stapler staple "$DMG_PATH"
	fi

	echo "✅ Staple complete!"
	echo ""
	echo "Verifying notarization:"
	spctl -a -vv "$APP_BUNDLE" 2>&1 || true
	exit 0
fi

is_transient_notary_failure() {
	local output="$1"
	[[ "$output" == *"statusCode: Optional(500)"* ]] ||
		[[ "$output" == *"statusCode\": 500"* ]] ||
		[[ "$output" == *"code = \"UNEXPECTED_ERROR\""* ]] ||
		[[ "$output" == *"title = \"Uncaught server exception\""* ]]
}

submit_for_notarization() {
	local attempt=1
	local delay="$NOTARY_SUBMIT_RETRY_DELAY"

	while true; do
		if SUBMIT_OUTPUT=$(xcrun notarytool submit "$SUBMISSION_PATH" \
			--apple-id "$APPLE_ID" \
			--team-id "$TEAM_ID" \
			--password "$PASSWORD" \
			--wait 2>&1); then
			return 0
		fi

		if (( attempt >= NOTARY_SUBMIT_MAX_ATTEMPTS )) || ! is_transient_notary_failure "$SUBMIT_OUTPUT"; then
			return 1
		fi

		echo "Apple notarization service returned a transient 500 error (attempt ${attempt}/${NOTARY_SUBMIT_MAX_ATTEMPTS})."
		echo "Retrying in ${delay}s..."
		sleep "$delay"

		attempt=$((attempt + 1))
		delay=$((delay * 2))
	done
}

# Submit for notarization
echo "Submitting for notarization..."
echo "  Apple ID: $APPLE_ID"
echo "  Team ID: $TEAM_ID"

# Submit the DMG if it exists, otherwise submit the app
if [[ -f "$DMG_PATH" ]]; then
	SUBMISSION_PATH="$DMG_PATH"
	echo "  Submitting DMG..."
else
	SUBMISSION_PATH="$APP_BUNDLE"
	echo "  Submitting app bundle..."
fi

# Submit and capture output
echo ""
echo "Uploading to Apple notarization service (this may take a few minutes)..."
submit_for_notarization || {
	echo "Notarization submission failed:"
	echo "$SUBMIT_OUTPUT"
	exit 1
}

echo "$SUBMIT_OUTPUT"

# Check if accepted
if echo "$SUBMIT_OUTPUT" | grep -q "Accepted"; then
	echo ""
	echo "✅ Notarization accepted! Stapling ticket..."

	xcrun stapler staple "$APP_BUNDLE"

	if [[ -f "$DMG_PATH" ]]; then
		xcrun stapler staple "$DMG_PATH"
	fi

	echo ""
	echo "✅ Done! App is notarized and ready for distribution."
	echo ""
	echo "Verifying notarization:"
	spctl -a -vv "$APP_BUNDLE" 2>&1 || true
else
	echo ""
	echo "❌ Notarization failed or returned unexpected status."
	echo "Full output:"
	echo "$SUBMIT_OUTPUT"

	# Extract submission ID and fetch detailed log
	SUBMISSION_ID=$(echo "$SUBMIT_OUTPUT" | grep "id:" | head -1 | awk '{print $2}')
	if [[ -n "$SUBMISSION_ID" ]]; then
		echo ""
		echo "Fetching detailed notarization log..."
		xcrun notarytool log "$SUBMISSION_ID" \
			--apple-id "$APPLE_ID" \
			--team-id "$TEAM_ID" \
			--password "$PASSWORD" 2>&1 || true
	fi

	exit 1
fi

```

### File: scripts\release.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

# Release script for Kaku
# Usage: ./scripts/release.sh
#
# Prerequisites:
#   - Clean git working tree on main branch
#   - gh CLI authenticated (for creating releases)
#   - Apple Developer ID certificate in login Keychain (or set KAKU_SIGNING_IDENTITY)
#   - Notarization credentials in Keychain or env vars (KAKU_NOTARIZE_*)
#
# Environment variables:
#   KAKU_SIGNING_IDENTITY    - Signing identity (auto-detected from Keychain if not set)
#   KAKU_NOTARIZE_APPLE_ID   - Apple ID for notarization
#   KAKU_NOTARIZE_TEAM_ID    - Team ID for notarization
#   KAKU_NOTARIZE_PASSWORD   - App-specific password for notarization
#   HOMEBREW_TAP_TOKEN       - Optional: GitHub token for Homebrew tap (defaults to gh auth token)
#   RUN_CLIPPY               - Set to 1 to also run clippy (default: 0)
#   SKIP_TESTS               - Set to 1 to skip tests (default: 0)

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

APP_NAME="Kaku"
OUT_DIR="${OUT_DIR:-$REPO_ROOT/dist}"
PROFILE="${PROFILE:-release-opt}"
BUILD_ARCH="${BUILD_ARCH:-universal}"
RUN_CLIPPY="${RUN_CLIPPY:-0}"
SKIP_TESTS="${SKIP_TESTS:-0}"
GITHUB_REPO="${GITHUB_REPO:-tw93/Kaku}"
HOMEBREW_TAP_REPO="${HOMEBREW_TAP_REPO:-tw93/homebrew-tap}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $*"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $*"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
}

die() {
    log_error "$*"
    exit 1
}

is_valid_team_id() {
    [[ "$1" =~ ^[A-Z0-9]{10}$ ]]
}

is_developer_id_application_identity() {
    [[ "$1" == Developer\ ID\ Application:* ]]
}

# Detect version from Cargo.toml if not provided
get_cargo_version() {
    grep '^version =' "$REPO_ROOT/kaku/Cargo.toml" | head -n1 | cut -d'"' -f2
}

# Verify git is clean
check_clean_git() {
    log_info "Checking git status..."
    if [[ -n "$(git status --porcelain 2>/dev/null)" ]]; then
        git status
        die "Working tree is not clean. Commit or stash changes before releasing."
    fi

    # Check we're on main branch
    local branch
    branch=$(git rev-parse --abbrev-ref HEAD)
    if [[ "$branch" != "main" ]]; then
        die "Not on main branch (currently on: $branch). Releases must be from main."
    fi
}

# Verify version consistency across crates
check_version_consistency() {
    log_info "Checking version consistency..."
    local kaku_version kaku_gui_version
    kaku_version=$(grep '^version =' "$REPO_ROOT/kaku/Cargo.toml" | head -n1 | cut -d'"' -f2)
    kaku_gui_version=$(grep '^version =' "$REPO_ROOT/kaku-gui/Cargo.toml" | head -n1 | cut -d'"' -f2)

    if [[ "$kaku_version" != "$kaku_gui_version" ]]; then
        die "Version mismatch: kaku=$kaku_version, kaku-gui=$kaku_gui_version"
    fi

    log_info "Version: $kaku_version"
}

# Check release notes match version
check_release_notes() {
    log_info "Checking release notes..."
    if [[ -x "$REPO_ROOT/scripts/check_release_notes.sh" ]]; then
        "$REPO_ROOT/scripts/check_release_notes.sh"
    else
        log_warn "check_release_notes.sh not found or not executable"
    fi
}

# Check config release metadata is ready
check_release_config() {
    log_info "Checking config release metadata..."
    if [[ ! -x "$REPO_ROOT/scripts/check_release_config.sh" ]]; then
        die "scripts/check_release_config.sh is missing or not executable"
    fi

    "$REPO_ROOT/scripts/check_release_config.sh"
}

extract_release_title() {
    local release_notes_file="$REPO_ROOT/.github/RELEASE_NOTES.md"
    local title

    if [[ ! -f "$release_notes_file" ]]; then
        return 1
    fi

    title=$(awk '/^# / { sub(/^# /, ""); print; exit }' "$release_notes_file")
    if [[ -z "$title" ]]; then
        return 1
    fi

    printf '%s\n' "$title"
}

# Check gh CLI is authenticated
check_gh_auth() {
    log_info "Checking GitHub CLI authentication..."
    if ! command -v gh >/dev/null 2>&1; then
        die "gh CLI not found. Install from https://cli.github.com/"
    fi

    if ! gh auth status >/dev/null 2>&1; then
        die "gh CLI not authenticated. Run: gh auth login"
    fi
}

# Detect Developer ID from Keychain if not set
detect_signing_identity() {
    if [[ -n "${KAKU_SIGNING_IDENTITY:-}" ]]; then
        if ! is_developer_id_application_identity "$KAKU_SIGNING_IDENTITY"; then
            die "KAKU_SIGNING_IDENTITY must be a Developer ID Application certificate, got: $KAKU_SIGNING_IDENTITY"
        fi
        log_info "Using signing identity from environment: $KAKU_SIGNING_IDENTITY"
        return 0
    fi

    log_info "Detecting signing identity from Keychain..."

    # Find Developer ID Application certificates
    local identities
    identities=$(security find-identity -v -p codesigning 2>/dev/null | grep "Developer ID Application" | awk -F '"' '{print $2}' || true)

    local count
    count=$(echo "$identities" | grep -c "^Developer ID Application" || echo "0")

    if [[ "$count" -eq 0 ]]; then
        die "No Developer ID Application certificate found in Keychain.\n" \
            "Install your certificate or set KAKU_SIGNING_IDENTITY environment variable."
    fi

    KAKU_SIGNING_IDENTITY=$(echo "$identities" | grep "^Developer ID Application" | head -n1)
    export KAKU_SIGNING_IDENTITY
    if [[ "$count" -gt 1 ]]; then
        log_warn "Multiple Developer ID Application certificates found, auto-selecting the first match"
    fi
    log_info "Auto-detected signing identity: $KAKU_SIGNING_IDENTITY"
}

validate_release_profile() {
    case "$PROFILE" in
        release|release-opt)
            log_info "Using release build profile: $PROFILE"
            ;;
        *)
            die "Invalid PROFILE=$PROFILE for release flow. Use PROFILE=release or PROFILE=release-opt."
            ;;
    esac
}

resolve_notarization_team_id() {
    local team_id="${KAKU_NOTARIZE_TEAM_ID:-}"

    if [[ -n "$team_id" ]]; then
        if is_valid_team_id "$team_id"; then
            return 0
        fi

        log_warn "Ignoring invalid KAKU_NOTARIZE_TEAM_ID: $team_id"
    fi

    team_id=$(printf '%s\n' "${KAKU_SIGNING_IDENTITY:-}" | sed -n 's/.*(\([A-Z0-9]\{10\}\)).*/\1/p')
    if [[ -n "$team_id" ]] && is_valid_team_id "$team_id"; then
        export KAKU_NOTARIZE_TEAM_ID="$team_id"
        log_info "Derived notarization Team ID from signing identity: $team_id"
        return 0
    fi

    return 1
}

# Check notarization credentials are available
check_notarization_creds() {
    log_info "Checking notarization credentials..."

    local have_creds=0
    local have_team_id=0

    if resolve_notarization_team_id; then
        have_team_id=1
    fi

    # Check environment variables
    if [[ -n "${KAKU_NOTARIZE_APPLE_ID:-}" && -n "${KAKU_NOTARIZE_PASSWORD:-}" && "$have_team_id" -eq 1 ]]; then
        have_creds=1
        log_info "Using notarization credentials from environment variables"
    else
        # Check Keychain
        local apple_id password
        apple_id=$(security find-generic-password -s "kaku-notarize-apple-id" -w 2>/dev/null || true)
        password=$(security find-generic-password -s "kaku-notarize-password" -w 2>/dev/null || true)

        if [[ -n "$apple_id" && -n "$password" && "$have_team_id" -eq 1 ]]; then
            have_creds=1
            log_info "Found notarization credentials in Keychain and resolved Team ID"
        fi
    fi

    if [[ "$have_creds" -eq 0 ]]; then
        log_warn "Notarization credentials not found in environment or Keychain"
        log_warn "Notarization may fail. To set up credentials:"
        log_warn "  export KAKU_NOTARIZE_APPLE_ID='your-apple-id@example.com'"
        log_warn "  export KAKU_NOTARIZE_TEAM_ID='YOURTEAMID'"
        log_warn "  export KAKU_NOTARIZE_PASSWORD='xxxx-xxxx-xxxx-xxxx'"
        log_warn ""
        log_warn "Or store in Keychain:"
        log_warn "  security add-generic-password -s 'kaku-notarize-apple-id' -a 'kaku' -w 'your-apple-id@example.com'"
        log_warn "  security add-generic-password -s 'kaku-notarize-password' -a 'kaku' -w 'your-app-specific-password'"
        read -r -p "Continue anyway? [y/N] " response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
}

# Run all quality checks
run_checks() {
    log_info "Running format check..."
    make fmt-check

    log_info "Running compilation check..."
    make check

    if [[ "$RUN_CLIPPY" == "1" ]]; then
        log_info "Running clippy..."
        cargo clippy --locked --all-targets -- -D warnings
    fi

    if [[ "$SKIP_TESTS" == "0" ]]; then
        log_info "Running tests..."
        make test
    else
        log_warn "Skipping tests (SKIP_TESTS=1)"
    fi
}

# Build the release
build_release() {
    log_info "Building release (PROFILE=$PROFILE, ARCH=$BUILD_ARCH)..."

    export KAKU_SIGNING_IDENTITY
    export KAKU_REQUIRE_SIGNED_RELEASE=1
    export PROFILE
    export BUILD_ARCH
    export OUT_DIR

    ./scripts/build.sh
}

# Notarize the release
notarize_release() {
    log_info "Submitting for notarization..."
    ./scripts/notarize.sh
}

# Create and push git tag
create_tag() {
    local version="$1"
    local tag="V${version}"
    local head_sha
    local tag_sha
    local remote_tag_sha

    log_info "Creating tag $tag..."
    head_sha=$(git rev-parse HEAD)

    if git show-ref --verify --quiet "refs/tags/$tag"; then
        tag_sha=$(git rev-parse "$tag^{}")
        if [[ "$tag_sha" != "$head_sha" ]]; then
            die "Tag $tag already exists at $tag_sha, but HEAD is $head_sha."
        fi

        log_warn "Tag $tag already exists at current HEAD, reusing it."
    else
        git tag -a "$tag" -m "Release $tag"
    fi

    remote_tag_sha=$(git ls-remote --tags origin "refs/tags/${tag}^{}" | awk 'NR == 1 { print $1 }')
    if [[ -n "$remote_tag_sha" ]]; then
        if [[ "$remote_tag_sha" != "$head_sha" ]]; then
            die "Origin already has tag $tag at $remote_tag_sha, but HEAD is $head_sha."
        fi

        log_warn "Origin already has tag $tag at current HEAD, skipping push."
        return 0
    fi

    log_info "Pushing tag $tag..."
    git push origin "$tag"
}

# Create GitHub Release
create_github_release() {
    local version="$1"
    local tag="V${version}"
    local release_notes_file="$REPO_ROOT/.github/RELEASE_NOTES.md"
    local release_title="$APP_NAME $tag"
    local notes_arg=""
    local release_edit_args=()
    local release_title_from_notes=""

    # Build a cleaned notes file: strip the first heading line and remove blank
    # lines between numbered list items so GitHub doesn't render extra spacing.
    local notes_tmp
    notes_tmp=$(mktemp /tmp/kaku-release-notes.XXXXXX.md)
    # shellcheck disable=SC2064
    trap "rm -f $notes_tmp" RETURN

    if [[ -f "$release_notes_file" ]]; then
        # Skip leading "# Title" line (and following blank line), then collapse
        # blank lines that appear between numbered list items.
        awk '
            NR == 1 && /^# / { next }
            NR == 2 && /^[[:space:]]*$/ { next }
            /^[[:space:]]*$/ { blank=1; next }
            blank { if (!/^[0-9]+\./) printf "\n"; blank=0 }
            { print }
            END { if (blank) printf "\n" }
        ' "$release_notes_file" > "$notes_tmp"

        if [[ -s "$notes_tmp" ]]; then
            notes_arg="--notes-file"
        else
            notes_arg="--generate-notes"
        fi
    else
        notes_arg="--generate-notes"
    fi

    if release_title_from_notes=$(extract_release_title); then
        release_title="$release_title_from_notes"
    fi

    log_info "Creating GitHub Release for $tag..."

    if [[ "$notes_arg" == "--notes-file" ]]; then
        release_edit_args=(--title "$release_title" "$notes_arg" "$notes_tmp")
    else
        release_edit_args=(--title "$release_title")
    fi

    # Check if release already exists
    if gh release view "$tag" -R "$GITHUB_REPO" >/dev/null 2>&1; then
        log_warn "Release $tag already exists, reconciling title, notes, and assets..."
        gh release edit "$tag" \
            -R "$GITHUB_REPO" \
            "${release_edit_args[@]}"
        gh release upload "$tag" \
            -R "$GITHUB_REPO" \
            "$OUT_DIR/Kaku.dmg" \
            "$OUT_DIR/kaku_for_update.zip" \
            "$OUT_DIR/kaku_for_update.zip.sha256" \
            --clobber
    else
        if [[ "$notes_arg" == "--notes-file" ]]; then
            gh release create "$tag" \
                -R "$GITHUB_REPO" \
                "$OUT_DIR/Kaku.dmg" \
                "$OUT_DIR/kaku_for_update.zip" \
                "$OUT_DIR/kaku_for_update.zip.sha256" \
                --title "$release_title" \
                "$notes_arg" "$notes_tmp"
        else
            gh release create "$tag" \
                -R "$GITHUB_REPO" \
                "$OUT_DIR/Kaku.dmg" \
                "$OUT_DIR/kaku_for_update.zip" \
                "$OUT_DIR/kaku_for_update.zip.sha256" \
                --title "$release_title" \
                --generate-notes
        fi
    fi

    log_info "GitHub Release created: https://github.com/${GITHUB_REPO}/releases/tag/$tag"
}

# Optional: Update Homebrew tap
update_homebrew_tap() {
    local version="$1"
    local token=""
    local dmg_sha256
    local dispatch_output
    local workflow_url="https://github.com/${HOMEBREW_TAP_REPO}/actions/workflows/bump.yml"
    local latest_run_url=""

    # Try to get token: env var > gh auth token
    if [[ -n "${HOMEBREW_TAP_TOKEN:-}" ]]; then
        token="$HOMEBREW_TAP_TOKEN"
        log_info "Using HOMEBREW_TAP_TOKEN from environment"
    else
        # Try to get token from gh CLI
        token=$(gh auth token 2>/dev/null || true)
        if [[ -n "$token" ]]; then
            log_info "Using GitHub token from 'gh auth token'"
        fi
    fi

    if [[ -z "$token" ]]; then
        log_info "No GitHub token available, skipping Homebrew tap update"
        return 0
    fi

    dmg_sha256=$(shasum -a 256 "$OUT_DIR/Kaku.dmg" | awk '{print $1}')

    log_info "Dispatching Homebrew tap update..."

    # Dispatch workflow to update Homebrew tap
    if ! dispatch_output=$(
        GH_TOKEN="$token" gh api \
        --method POST \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "/repos/${HOMEBREW_TAP_REPO}/dispatches" \
        -f "event_type=kaku_release_published" \
        -f "client_payload[version]=$version" \
        -f "client_payload[sha256]=$dmg_sha256" 2>&1
    ); then
        log_warn "Failed to dispatch Homebrew tap update for ${HOMEBREW_TAP_REPO}"
        log_warn "$dispatch_output"
        log_warn "Track the workflow here: $workflow_url"
        return 0
    fi

    log_info "Homebrew tap update dispatched"
    log_info "Track the workflow here: $workflow_url"

    latest_run_url=$(gh run list \
        -R "$HOMEBREW_TAP_REPO" \
        --workflow bump.yml \
        --limit 1
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
