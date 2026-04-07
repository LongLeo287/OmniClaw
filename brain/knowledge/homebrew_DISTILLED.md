---
id: homebrew
type: knowledge
owner: OA_Triage
---
# homebrew
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Homebrew Core

Core formulae for the Homebrew package manager.

 [Homebrew/discussions (forum)](https://github.com/orgs/Homebrew/discussions)

## How do I install these formulae?

Just `brew install <formula>`. This is the default tap for Homebrew and is installed by default.

## More Documentation, Troubleshooting, Contributing, Security, Community, Donations, License and Sponsors

See these sections in [Homebrew/brew's README](https://github.com/Homebrew/brew#homebrew).

```

### File: AGENTS.md
```md
# Agent Instructions for homebrew-core

This document helps coding agents produce high-quality PRs for homebrew-core formula contributions.

## Before Any PR

1. **Check for existing PRs** for the same formula: [open PRs](https://github.com/Homebrew/homebrew-core/pulls)
2. Run `brew tap homebrew/core` if not already tapped

## Version Updates

Preferred method for version bumps:

```sh
brew bump-formula-pr --strict <formula> --url=<url> --sha256=<sha256>
# or
brew bump-formula-pr --strict <formula> --tag=<tag> --revision=<revision>
# or
brew bump-formula-pr --strict <formula> --version=<version>
```

This handles URL/checksum updates, commit message, and opens the PR automatically.

### Manual Version Updates

If manual editing is needed:

```sh
brew edit <formula>
# Update url and sha256 (or tag and revision)
# Leave `bottle do` block unchanged
```

Commit message: `foo 1.2.3`

## Formula Fixes

For bug fixes or improvements to existing formulae:

```sh
brew edit <formula>
# Make changes
# Leave `bottle do` block unchanged
```

Commit message: `foo: fix <description>` or `foo: <description>`

### When to Add a Revision

Add or increment `revision` when:
- Fix requires existing bottles to be rebuilt
- Dependencies changed in a way that affects the built package
- The installed binary/library behavior changes

Do NOT add revision for cosmetic changes (comments, style, livecheck fixes).

## New Formulae

```sh
brew create <url>
# Edit the generated formula
```

Commit message: `foo 1.2.3 (new formula)`

### Required Elements

- **Test block**: MUST verify actual functionality, not just `--version` or `--help`
  - Version check is acceptable as an additional assertion
  - For libraries: compile and link sample code
  - Use `testpath` for temporary files

- **Service block**: If the software can run as a daemon, include a `service do` block:
  ```ruby
service do
  run [opt_bin/"foo", "start"]
  keep_alive true
end
  ```

- **Livecheck**: Prefer default behavior. Only add a `livecheck` block if automatic detection fails.

- **Head support**: Include when the project has a development branch:
  ```ruby
head "https://github.com/org/repo.git", branch: "main"
  ```
  Git repositories MUST specify `branch:`.

## Required Validation (All PR Types)

All checks MUST pass locally before opening a PR:

```sh
# Build from source (required)
HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source <formula>

# Run tests
brew test <formula>

# Audit (existing formula)
brew audit --strict <formula>

# Audit (new formula only)
brew audit --new <formula>

# Style check
brew style <formula>
```

## PR Template Checklist

You MUST verify all items before submitting:

- [ ] Followed [CONTRIBUTING.md](CONTRIBUTING.md)
- [ ] Commits follow [commit style guide](https://docs.brew.sh/Formula-Cookbook#commit)
- [ ] No existing [open PRs](https://github.com/Homebrew/homebrew-core/pulls) for same change
- [ ] Built locally with `HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source`
- [ ] Tests pass with `brew test`
- [ ] Audit passes with `brew audit --strict` (or `--new` for new formulae)

## Commit Message Format

- Version update: `foo 1.2.3`
- New formula: `foo 1.2.3 (new formula)`
- Fix/change: `foo: fix <description>` or `foo: <description>`
- First line MUST be 50 characters or less
- Reference issues with `Closes #12345` in commit body if applicable

## PR Hygiene

### MUST

- One formula change per PR
- Keep diffs minimal and focused
- Provide only essential context in PR description

### MUST NOT

- Edit `bottle do` blocks (managed by BrewTestBot)
- Batch unrelated formula changes
- Include large logs or verbose output in PR body
- Add non-Homebrew usage caveats in PR body
- Include unrelated refactors or cleanups

## PR Description Template

Keep it minimal:

```
Built and tested locally on [macOS version/Linux].

[One sentence describing the change if not obvious from title.]
```

## CI Failures

- Reproduce failures locally before debugging
- Read error messages and annotations in "Files changed" tab
- Check complete build log in "Checks" tab if needed
- For Linux failures, use the [Homebrew Docker container](CONTRIBUTING.md#homebrew-docker-container)
- If stuck, comment describing what you've tried

## AI Disclosure

If AI assisted with the PR, check the AI checkbox in the PR template and briefly describe:
- How AI was used
- What manual verification was performed

## References

- [Formula Cookbook](https://docs.brew.sh/Formula-Cookbook)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [How to Open a PR](https://docs.brew.sh/How-To-Open-a-Homebrew-Pull-Request)

```

### File: CONTRIBUTING.md
```md
# Contributing to Homebrew

First time contributing to Homebrew? Read our [Code of Conduct](https://github.com/Homebrew/.github/blob/HEAD/CODE_OF_CONDUCT.md#code-of-conduct).

Ensure your commits follow the [commit style guide](https://docs.brew.sh/Formula-Cookbook#commit).

Thanks for contributing!

### To report a bug

* run `brew update` (twice)
* run and read `brew doctor`
* read [the Troubleshooting Checklist](https://docs.brew.sh/Troubleshooting)
* open an issue on the formula's repository

### To submit a version upgrade for the `foo` formula

* check if the same upgrade has been already submitted by [searching the open pull requests for `foo`](https://github.com/Homebrew/homebrew-core/pulls?utf8=✓&q=is%3Apr+is%3Aopen+foo).
* `brew tap homebrew/core`
* `brew bump-formula-pr --strict foo` with one of the following:
  * `--url=...` and `--sha256=...`
  * `--tag=...` and `--revision=...`
  * `--version=...`

### To add a new formula for `foo` version `2.3.4` from `$URL`

* read [the Formula Cookbook](https://docs.brew.sh/Formula-Cookbook) or: `brew create $URL` and make edits
* `HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source foo`
* `brew audit --new foo`
* `git commit` with message formatted `foo 2.3.4 (new formula)`
* [open a pull request](https://docs.brew.sh/How-To-Open-a-Homebrew-Pull-Request) and fix any failing tests

Once you've addressed any potential feedback and a member of the Homebrew org has approved your pull request, the [BrewTestBot](https://github.com/BrewTestBot) will automatically merge it a couple of minutes later.

### To contribute a fix to the `foo` formula

If you are already well-versed in the use of `git`, then you can work with the local
copy of the `homebrew-core` repository as you are used to. You may need to run
`brew tap homebrew/core` to clone it, if you haven't done so already; the repository
will then be located in the directory `$(brew --repository homebrew/core)`.
Modify the formula there using `brew edit foo`,
leaving the section `bottle do ... end` unchanged, and prepare a pull request
as you usually do.  Before submitting your pull request, be sure to test it
with these commands:

```
brew uninstall --force foo
HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source foo
brew test foo
brew audit --strict foo
brew style foo
```

After testing, if you think it is needed to force the corresponding bottles to be
rebuilt and redistributed, add a line of the form `revision 1` to the formula,
or add 1 to the revision number already present.

If you are not already well versed in the use of `git`, then you may learn
about it from the introduction at
https://docs.brew.sh/How-To-Open-a-Homebrew-Pull-Request and then proceed as
follows:

* run `brew tap homebrew/core --force`, if you haven't done so previously
* run `brew edit foo` and make edits
* leave the section `bottle do ... end` unchanged
* test your changes using the commands listed above
* run `git commit` with message formatted `foo <insert new version number>` or `foo: <insert details>`
* open a pull request as described in the introduction linked to above, wait for the automated test results, and fix any failing tests

Once you've addressed any potential feedback and a member of the Homebrew org has approved your pull request, the [BrewTestBot](https://github.com/BrewTestBot) will automatically merge it a couple of minutes later.

### Dealing with CI failures

Pull requests with failing CI should not be merged, so the failures will need to be fixed. Start by looking for errors in the CI log. Some errors will show up as annotations in the "Files changed" tab of your pull request. If there are no annotations, or the annotations do not contain the relevant errors, then the complete build log can be found in the "Checks" tab of your pull request.

Once you've identified the error(s), check whether you can reproduce them locally. You should be able to do this with one or more of `HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source`, `brew audit --strict --online`, and `brew test`. Don't forget to checkout your PR branch before trying this! If you can reproduce the failure(s), then it is likely that the formula needs to be fixed. Read the error messages carefully. Many errors provide hints on how to fix them. Failing that: looking up the error message is often a fruitful source of hints for what to do next.

If you can't reproduce an error, then you need to identify what makes your local environment different from the build environment in CI. It is likely that one of those differences is driving the CI failure. It may help to try to make your local environment as similar to CI as possible to try to reproduce the failure. If the CI failure occurs on Linux, you can use the Homebrew Docker container to emulate the CI environment. See the next section for a guide on how to do this.

If you're still stuck: don't fret. Leave a comment on your PR describing what you've done to try to diagnose and fix the CI failure and we'll do our best to help you resolve them.

### Homebrew Docker container

Linux CI runs on a Docker container running Ubuntu. If you have Docker installed, you can use our container with:

```
docker run --interactive --tty --rm --pull always ghcr.io/homebrew/brew:latest /bin/bash
```

If you don't have Docker installed:

```
brew install --formula docker lima
limactl start template://docker
docker context create lima --docker "host=unix://${HOME}/.lima/docker/sock/docker.sock"
docker context use lima
```

You should now be able to run the `docker` command shown above.

```

### File: disabled_new_usr_local_relocation_formulae.json
```json
[
  "colordiff",
  "cpanminus",
  "davmail",
  "luarocks",
  "meson",
  "phpmyadmin",
  "python-setuptools",
  "rabbitmq",
  "ruby-install",
  "sqlite-utils",
  "zsh-completions"
]

```

### File: formula_renames.json
```json
{
  "alloy": "alloy-analyzer",
  "amtk": "libgedit-amtk",
  "annie": "lux",
  "ark": "velero",
  "arm": "nyx",
  "asciigen": "glyph",
  "at-spi2-atk": "at-spi2-core",
  "atk": "at-spi2-core",
  "azion-cli": "azion",
  "aztfy": "aztfexport",
  "artifactory-cli-go": "jfrog-cli",
  "badtouch": "authoscope",
  "bash-completion2": "bash-completion@2",
  "beanstalk": "beanstalkd",
  "berkeley-db4": "berkeley-db@4",
  "bigdata": "blazegraph",
  "boot2docker": "docker-machine",
  "bro": "zeek",
  "cagent": "docker-agent",
  "cdiff": "ydiff",
  "chipmunk": "chipmunk-physics",
  "clawdbot-cli": "openclaw-cli",
  "cloog018": "cloog",
  "cloudflare-wrangler2": "cloudflare-wrangler",
  "commonmark": "cmark",
  "coq": "rocq",
  "cppformat": "fmt",
  "crystal-lang": "crystal",
  "cutter": "cutter-cli",
  "curl-openssl": "curl",
  "cv": "progress",
  "cyassl": "wolfssl",
  "dash": "dash-shell",
  "d-bus": "dbus",
  "docker-slim": "mintoolkit",
  "dump1090-mutability": "dump1090-fa",
  "fbida": "exiftran",
  "fcct": "butane",
  "ffmpeg28": "ffmpeg@2.8",
  "findbugs": "spotbugs",
  "genai-toolbox": "mcp-toolbox",
  "geode": "apache-geode",
  "geth": "ethereum",
  "gitlab-ci-multi-runner": "gitlab-runner",
  "giflib@5": "giflib",
  "glib-utils": "glib",
  "glibmm@2.64": "glibmm@2.66",
  "glfw3": "glfw",
  "gloo-ctl": "glooctl",
  "gnatsd": "nats-server",
  "gnome-icon-theme": "adwaita-icon-theme",
  "gnome-latex": "enter-tex",
  "gnome-themes-standard": "gnome-themes-extra",
  "gnu-cobol": "gnucobol",
  "gnupg2": "gnupg",
  "gold": "binutils",
  "goplus": "xgo",
  "google-perftools": "gperftools",
  "grakn": "typedb",
  "grpc-swift": "protoc-gen-grpc-swift",
  "grunt": "grunt-cli",
  "gst-devtools": "gstreamer",
  "gst-editing-services": "gstreamer",
  "gst-libav": "gstreamer",
  "gst-plugins-bad": "gstreamer",
  "gst-plugins-base": "gstreamer",
  "gst-plugins-good": "gstreamer",
  "gst-plugins-rs": "gstreamer",
  "gst-plugins-ugly": "gstreamer",
  "gst-python": "gstreamer",
  "gst-rtsp-server": "gstreamer",
  "gst-validate": "gstreamer",
  "gtk+4": "gtk4",
  "gtksourceview@4": "gtksourceview4",
  "gutenberg": "zola",
  "hh": "hstr",
  "hpp-fcl": "coal",
  "ht-rust": "xh",
  "htop-osx": "htop",
  "httpd24": "httpd",
  "huggingface-cli": "hf",
  "i386-elf-binutils": "x86_64-elf-binutils",
  "i386-elf-gcc": "x86_64-elf-gcc",
  "iccmax": "iccdev",
  "iceberg": "iceberg-cli",
  "interactive-rebase-tool": "git-interactive-rebase-tool",
  "ipfs": "kubo",
  "jfrog-cli-go": "jfrog-cli",
  "juju2": "juju",
  "juju@2.0": "juju",
  "jupyter": "jupyterlab",
  "kafkacat": "kcat",
  "kde-extra-cmake-modules": "extra-cmake-modules",
  "kde-karchive": "karchive",
  "kde-kdoctools": "kdoctools",
  "kde-ki18n": "ki18n",
  "kde-threadweaver": "threadweaver",
  "kertish-dfs": "kertish-dos",
  "kotlin-compiler": "kotlin",
  "ksh": "ksh93",
  "kubernetes-helm": "helm",
  "ldb": "samba",
  "letsencrypt": "certbot",
  "libcppa": "caf",
  "libcython": "cython",
  "libmongoclient": "mongo-cxx-driver",
  "libpython-tabulate": "python-tabulate",
  "libsasl2": "cyrus-sasl",
  "libtorch": "pytorch",
  "libxml++3": "libxml++@3",
  "limbo": "turso",
  "llama": "walk",
  "mat": "mat2",
  "mcp-scan": "snyk-agent-scan",
  "minizip2": "minizip-ng",
  "mist": "mist-cli",
  "mkl-dnn": "onednn",
  "moar": "moor",
  "mobile-shell": "mosh",
  "mongo-c": "mongo-c-driver",
  "mpich2": "mpich",
  "mps-youtube": "yewtube",
  "mr2": "zoro",
  "mysql-connector-c": "mysql-client",
  "nanopb-generator": "nanopb",
  "newsbeuter": "newsboat",
  "nimrod": "nim",
  "now-cli": "vercel-cli",
  "nova": "nova-fairwinds",
  "nping": "nbping",
  "objective-caml": "ocaml",
  "offline-imap": "offlineimap",
  "oil": "oils-for-unix",
  "onedrive": "onedrive-cli",
  "open-cobol": "gnucobol",
  "opencv3": "opencv",
  "osh": "etsh",
  "pangomm@2.42": "pangomm@2.46",
  "parallelstl": "onedpl",
  "pev": "readpe",
  "php-intl": "php",
  "poac": "cabin",
  "polarssl": "mbedtls",
  "pony-language-server": "ponyc",
  "prefligit": "prek",
  "prest": "prestd",
  "presto": "prestodb",
  "prestosql": "trino",
  "prql-compiler": "prqlc",
  "pydantic-core": "pydantic",
  "pyqt5": "pyqt@5",
  "python-certifi": "certifi",
  "python-chardet": "chardet",
  "python-cryptography": "cryptography",
  "qt5": "qt@5",
  "ra-multiplex": "lspmux",
  "racket": "minimal-racket",
  "rebar@3": "rebar3",
  "recipes": "gnome-recipes",
  "repopack": "repomix",
  "resin-cli": "balena-cli",
  "richmd": "rich-cli",
  "rig-r": "r-rig",
  "rio": "rio-terminal",
  "root6": "root",
  "rt-audio": "rtaudio",
  "rtx": "mise",
  "rustfmt": "rust",
  "rustup-init": "rustup",
  "screenbrightness": "brightness",
  "sdl": "sdl12-compat",
  "selenium-server-standalone": "selenium-server",
  "server-go": "openiothub-server",
  "shuttle": "shuttle-cli",
  "singularity": "apptainer",
  "sloth": "sloth-cli",
  "speedtest_cli": "speedtest-cli",
  "ssreflect": "math-comp",
  "squirrel": "squirrel-lang",
  "tachyon": "alluxio",
  "tensorflow": "libtensorflow",
  "tepl": "libgedit-tepl",
  "thors-mongo": "thors-anvil",
  "thors-serializer": "thors-anvil",
  "todoist": "todoist-cli",
  "todolist": "ultralist",
  "tomee-jax-rs": "tomee-plus",
  "tracker": "tinysparql",
  "transfig": "fig2dev",
  "transmission": "transmission-cli",
  "trust-dns": "hickory-dns",
  "twine-pypi": "twine",
  "usbmuxd": "libusbmuxd",
  "wcurl": "curl",
  "weboob": "woob",
  "wires": "geckodriver",
  "wpcli-completion": "wp-cli-completion",
  "wxmac": "wxwidgets",
  "xkeyboardconfig": "xkeyboard-config",
  "xu4": "scummvm"
}

```

### File: LICENSE.txt
```txt
BSD 2-Clause License

Copyright (c) 2009-present, Homebrew contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

### File: synced_versions_formulae.json
```json
[
  [
    "aarch64-elf-binutils",
    "arm-linux-gnueabihf-binutils",
    "arm-none-eabi-binutils",
    "binutils",
    "i686-elf-binutils",
    "m68k-elf-binutils",
    "mipsel-linux-gnu-binutils",
    "riscv64-elf-binutils",
    "x86_64-elf-binutils",
    "x86_64-linux-gnu-binutils"
  ],
  ["apache-arrow", "apache-arrow-glib"],
  ["avro-c", "avro-cpp", "avro-tools"],
  ["b3sum", "blake3"],
  ["baresip", "libre"],
  ["htslib", "samtools"],
  ["boost", "boost-bcp", "boost-build", "boost-mpi", "boost-python3"],
  ["bundler-completion", "gem-completion", "rails-completion", "rake-completion", "ruby-completion"],
  ["cmake", "cmake-docs"],
  ["dbhash", "lemon", "sqldiff", "sqlite", "sqlite-analyzer", "sqlite-rsync"],
  ["dmd", "dtools"],
  ["docker", "docker-completion"],
  ["etl", "synfig"],
  ["file-formula", "libmagic"],
  ["edencommon", "fb303", "fbthrift", "fizz", "folly", "mvfst", "proxygen", "wangle", "watchman"],
  ["extra-cmake-modules", "karchive", "kdoctools", "ki18n", "ktexttemplate", "threadweaver"],
  ["ffmpeg", "ffmpeg-full"],
  ["gcc", "libgccjit"],
  ["gdb", "aarch64-elf-gdb", "arm-none-eabi-gdb", "i386-elf-gdb", "riscv64-elf-gdb", "x86_64-elf-gdb"],
  ["git", "git-credential-libsecret", "git-gui", "git-svn"],
  ["gmic", "cimg"],
  ["gnome-online-accounts", "libgoa"],
  ["hdf5", "hdf5-mpi"],
  ["imagemagick", "imagemagick-full"],
  ["libmediainfo", "media-info"],
  ["libnetworkit", "networkit"],
  ["libnghttp2", "nghttp2"],
  ["libngspice", "ngspice"],
  ["libnice", "libnice-gstreamer"],
  ["libtorrent-rakshasa", "rtorrent"],
  ["lima", "lima-additional-guestagents"],
  ["llvm", "lld", "flang", "wasi-runtimes"],
  ["logcli", "loki"],
  ["qalculate-gtk", "qalculate-qt"],
  ["mame", "rom-tools"],
  ["mecab-unidic", "mecab-unidic-extended"],
  ["micropython", "mpremote"],
  ["moarvm", "nqp", "rakudo"],
  ["moreutils", "sponge"],
  ["mupdf", "mupdf-tools"],
  ["mysql", "mysql-client"],
  ["notmuch", "notmuch-mutt"],
  ["openssh", "ssh-copy-id"],
  ["petsc", "petsc-complex"],
  ["pipewire", "pipewire-gstreamer"],
  ["poppler", "poppler-qt5"],
  ["python-tk@3.10", "python@3.10"],
  ["python-gdbm@3.11", "python-tk@3.11", "python@3.11"],
  ["python-gdbm@3.12", "python-tk@3.12", "python@3.12"],
  ["python-gdbm@3.13", "python-tk@3.13", "python@3.13"],
  ["python-gdbm@3.14", "python-tk@3.14", "python@3.14", "python-freethreading"],
  ["python-tk@3.9", "python@3.9"],
  [
    "qt",
    "qt-libiodbc",
    "qt-mariadb",
    "qt-mysql",
    "qt-percona-server",
    "qt-postgresql",
    "qt-unixodbc",
    "qt3d",
    "qt5compat",
    "qtbase",
    "qtcanvaspainter",
    "qtcharts",
    "qtconnectivity",
    "qtdatavis3d",
    "qtdeclarative",
    "qtgraphs",
    "qtgrpc",
    "qthttpserver",
    "qtimageformats",
    "qtlanguageserver",
    "qtlocation",
    "qtlottie",
    "qtmultimedia",
    "qtnetworkauth",
    "qtpositioning",
    "qtquick3d",
    "qtquick3dphysics",
    "qtquickeffectmaker",
    "qtquicktimeline",
    "qtremoteobjects",
    "qtscxml",
    "qtsensors",
    "qtserialbus",
    "qtserialport",
    "qtshadertools",
    "qtspeech",
    "qtsvg",
    "qttasktree",
    "qttools",
    "qttranslations",
    "qtvirtualkeyboard",
    "qtwayland",
    "qtwebchannel",
    "qtwebengine",
    "qtwebsockets",
    "qtwebview"
  ],
  ["qwt", "qwt-qt5"],
  [
    "spirv-headers",
    "spirv-tools",
    "vulkan-extensionlayer",
    "vulkan-headers",
    "vulkan-loader",
    "vulkan-profiles",
    "vulkan-tools",
    "vulkan-utility-libraries",
    "vulkan-validationlayers"
  ],
  ["surelog", "uhdm"],
  ["technitium-dns", "technitium-library"],
  ["tmuxinator", "tmuxinator-completion"],
  ["tree-sitter", "tree-sitter-cli"],
  ["wp-cli", "wp-cli-completion"]
]

```

### File: tap_migrations.json
```json
{
  "android-ndk": "homebrew/cask",
  "android-platform-tools": "homebrew/cask",
  "app-engine-go-32": "homebrew/cask/google-cloud-sdk",
  "app-engine-go-64": "homebrew/cask/google-cloud-sdk",
  "avidemux": "homebrew/cask",
  "chromedriver": "homebrew/cask",
  "cockatrice": "homebrew/cask",
  "codex": "homebrew/cask",
  "consul": "homebrew/cask",
  "corelocationcli": "homebrew/cask",
  "geany": "homebrew/cask",
  "gearboy": "homebrew/cask",
  "gearsystem": "homebrew/cask",
  "gimp": "homebrew/cask",
  "grads": "homebrew/cask",
  "gtkwave": "homebrew/cask",
  "inkscape": "homebrew/cask",
  "joplin": "homebrew/cask",
  "keybase": "homebrew/cask",
  "luanti": "homebrew/cask",
  "meld": "homebrew/cask",
  "minetest": "homebrew/cask/luanti",
  "mitmproxy": "homebrew/cask",
  "openrct2": "homebrew/cask",
  "openttd": "homebrew/cask",
  "osxfuse": "homebrew/cask",
  "quassel": "homebrew/cask",
  "schismtracker": "homebrew/cask/schism-tracker",
  "transmission-remote-gtk": "homebrew/cask/transmission-remote-gui",
  "truetree": "homebrew/cask",
  "wesnoth": "homebrew/cask/the-battle-for-wesnoth"
}

```

### File: .github\actionlint.yaml
```yaml
self-hosted-runner:
  # Labels of self-hosted runner in array of strings.
  labels: []
# Configuration variables in array of strings defined in your repository or
# organization. `null` means disabling configuration variables check.
# Empty array means no configuration variable is allowed.
config-variables: []

```

### File: .github\ISSUE_TEMPLATE.md
```md
# Please fill out one of the templates on: https://github.com/Homebrew/homebrew-core/issues/new/choose or we will close it without comment.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
-----

<!-- Do not tick a checkbox if you haven’t performed its action. Honesty is indispensable for a smooth review process. -->
<!-- Use [x] to mark item done before creation, or just click the checkboxes with device pointer after creation -->
<!-- In the following questions `<formula>` is the name of the formula you're editing. -->

- [ ] Have you followed the [guidelines for contributing](https://github.com/Homebrew/homebrew-core/blob/HEAD/CONTRIBUTING.md)?
- [ ] Have you ensured that your commits follow the [commit style guide](https://docs.brew.sh/Formula-Cookbook#commit)?
- [ ] Have you checked that there aren't other open [pull requests](https://github.com/Homebrew/homebrew-core/pulls) for the same formula update/change?
- [ ] Have you built your formula locally with `HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source <formula>`?
- [ ] Is your test running fine `brew test <formula>`?
- [ ] Does your build pass `brew audit --strict <formula>` (after doing `HOMEBREW_NO_INSTALL_FROM_API=1 brew install --build-from-source <formula>`)? If this is a new formula, does it pass `brew audit --new <formula>`?

-----

- [ ] AI was used to generate or assist with generating this PR. *Please specify below how you used AI to help you, and what steps you have taken to manually verify the changes*.

-----

```

### File: .github\workflows\scripts\check-labels.js
```js
module.exports = async ({github, context, core}, formulae_detect, dependent_testing) => {
    const deps_suffix = dependent_testing ? '-deps' : ''

    const { data: { labels: labels } } = await github.rest.pulls.get({
      owner: context.repo.owner,
      repo: context.repo.repo,
      pull_number: context.issue.number
    })
    const label_names = labels.map(label => label.name)
    var syntax_only = false

    if (label_names.includes('CI-syntax-only')) {
      console.log('CI-syntax-only label found. Skipping tests job.')
      syntax_only = true
    } else if (label_names.includes('CI-published-bottle-commits')) {
      console.log('CI-published-bottle-commits label found. Skipping tests job.')
      syntax_only = true
    } else {
      console.log('No CI-syntax-only label found. Running tests job.')
    }

    core.setOutput('nodejs', !syntax_only && label_names.includes('nodejs'))

    core.setOutput('syntax-only', syntax_only)
    if (syntax_only) {
      return
    }

    var linux_runner = 'ubuntu-latest'
    if (label_names.includes(`CI-linux-self-hosted${deps_suffix}`)) {
      linux_runner = 'linux-self-hosted-1'
    } else if (label_names.includes(`CI-linux-large-runner${deps_suffix}`)) {
      linux_runner = 'homebrew-large-bottle-build'
    }
    core.setOutput('linux-runner', linux_runner)

    if (label_names.includes(`CI-no-fail-fast${deps_suffix}`)) {
      console.log(`CI-no-fail-fast${deps_suffix} label found. Continuing tests despite failing matrix builds.`)
      core.setOutput('fail-fast', false)
    } else {
      console.log(`No CI-no-fail-fast${deps_suffix} label found. Stopping tests on first failing matrix build.`)
      core.setOutput('fail-fast', true)
    }

    if (label_names.includes('CI-skip-dependents')) {
      console.log('CI-skip-dependents label found. Skipping brew test-bot --only-formulae-dependents.')
      core.setOutput('test-dependents', false)
    } else if (!formulae_detect.testing_formulae) {
      console.log('No testing formulae found. Skipping brew test-bot --only-formulae-dependents.')
      core.setOutput('test-dependents', false)
    } else {
      console.log('No CI-skip-dependents label found. Running brew test-bot --only-formulae-dependents.')
      core.setOutput('test-dependents', true)
    }

    if (dependent_testing) {
      if (label_names.includes('long dependent tests')) {
        console.log('"long dependent tests" label found. Setting long GitHub Actions timeout.')
        core.setOutput('long-timeout', true)
      } else {
        console.log('No "long dependent tests" label found. Setting short GitHub Actions timeout.')
        core.setOutput('long-timeout', false)
      }
    } else {
      if (label_names.includes('long build')) {
        console.log('"long build" label found. Setting long GitHub Actions timeout.')
        core.setOutput('long-timeout', true)
      } else {
        console.log('No "long build" label found. Setting short GitHub Actions timeout.')
        core.setOutput('long-timeout', false)
      }
    }

    const test_bot_formulae_args = ["--only-formulae", "--junit", "--only-json-tab", "--skip-dependents"]
    const test_bot_dependents_args = ["--only-formulae-dependents", "--junit"]

    if (label_names.includes(`CI-test-bot-no-concurrent-downloads`)) {
      console.log(`CI-test-bot-no-concurrent-downloads label found. Running with HOMEBREW_DOWNLOAD_CONCURRENCY=1`)
      core.setOutput('download-concurrency', '1')
    } else {
      console.log(`No CI-test-bot-no-concurrent-downloads label found. Running with HOMEBREW_DOWNLOAD_CONCURRENCY=auto`)
      core.setOutput('download-concurrency', 'auto')
    }

    if (label_names.includes(`CI-test-bot-fail-fast${deps_suffix}`)) {
      console.log(`CI-test-bot-fail-fast${deps_suffix} label found. Passing --fail-fast to brew test-bot.`)
      test_bot_formulae_args.push('--fail-fast')
      test_bot_dependents_args.push('--fail-fast')
    } else {
      console.log(`No CI-test-bot-fail-fast${deps_suffix} label found. Not passing --fail-fast to brew test-bot.`)
    }

    if (label_names.includes('CI-build-dependents-from-source')) {
      console.log('CI-build-dependents-from-source label found. Passing --build-dependents-from-source to brew test-bot.')
      test_bot_dependents_args.push('--build-dependents-from-source')
    } else {
      console.log('No CI-build-dependents-from-source label found. Not passing --build-dependents-from-source to brew test-bot.')
    }

    if (label_names.includes('CI-skip-recursive-dependents')) {
      console.log('CI-skip-recursive-dependents label found. Passing --skip-recursive-dependents to brew test-bot.')
      test_bot_dependents_args.push('--skip-recursive-dependents')
    } else {
      console.log('No CI-skip-recursive-dependents label found. Not passing --skip-recursive-dependents to brew test-bot.')
    }

    if (label_names.includes('CI-skip-livecheck')) {
      console.log('CI-skip-livecheck label found. Passing --skip-livecheck to brew test-bot.')
      test_bot_formulae_args.push('--skip-livecheck')
    } else {
      console.log('No CI-skip-livecheck label found. Not passing --skip-livecheck to brew test-bot.')
    }

    if (label_names.includes('CI-version-downgrade')) {
      console.log('CI-version-downgrade label found. Passing --skip-stable-version-audit to brew test-bot.')
      test_bot_formulae_args.push('--skip-stable-version-audit')
    } else {
      console.log('No CI-version-downgrade label found. Not passing --skip-stable-version-audit to brew test-bot.')
    }

    if (label_names.includes('CI-checksum-change-confirmed')) {
      console.log('CI-checksum-change-confirmed label found. Passing --skip-checksum-only-audit to brew test-bot.')
      test_bot_formulae_args.push('--skip-checksum-only-audit')
    } else {
      console.log('No CI-checksum-change-confirmed label found. Not passing --skip-checksum-only-audit to brew test-bot.')
    }

    if (label_names.includes('CI-skip-revision-audit')) {
      console.log('CI-skip-revision-audit label found. Passing --skip-revision-audit to brew test-bot.')
      test_bot_formulae_args.push('--skip-revision-audit')
    } else {
      console.log('No CI-skip-revision-audit label found. Not passing --skip-revision-audit to brew test-bot.')
    }

    if (label_names.includes('CI-skip-new-formulae')) {
      console.log('CI-skip-new-formulae label found. Passing --skip-new to brew test-bot.')
      test_bot_formulae_args.push('--skip-new')
    } else {
      console.log('No CI-skip-new-formulae label found. Not passing --skip-new to brew test-bot.')
    }

    if (label_names.includes('CI-skip-new-formulae-strict')) {
      console.log('CI-skip-new-formulae-strict label found. Passing --skip-new-strict to brew test-bot.')
      test_bot_formulae_args.push('--skip-new-strict')
    } else {
      console.log('No CI-skip-new-formulae-strict label found. Not passing --skip-new-strict to brew test-bot.')
    }

    if (label_names.includes('CI-skip-online-checks')) {
      console.log('CI-skip-online-checks label found. Passing --skip-online-checks to brew test-bot.')
      test_bot_formulae_args.push('--skip-online-checks')
    } else {
      console.log('No CI-skip-online-checks label found. Not passing --skip-online-checks to brew test-bot.')
    }

    core.setOutput('test-bot-formulae-args', test_bot_formulae_args.join(" "))
    core.setOutput('test-bot-dependents-args', test_bot_dependents_args.join(" "))
}

```

