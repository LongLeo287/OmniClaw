---
id: github.com-innobead-huber-3bf7ac0c-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:09.193656
---

# KNOWLEDGE EXTRACT: github.com_innobead_huber_3bf7ac0c
> **Extracted on:** 2026-04-01 09:21:00
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520145/github.com_innobead_huber_3bf7ac0c

---

## File: `.dockerignore`
```
.github
target
Dockerfile.*
```

## File: `.gitignore`
```
target/
.output/
.idea/
.target/
docs/book/
docs/theme/

*.iml
```

## File: `Cargo.toml`
```
[workspace]
members = ["huber", "huber-generator", "huber-procmacro"]
default-members = ["huber", "huber-procmacro"]
exclude = ["huber-generator"]
resolver = "2"

[profile.release]
strip = true
opt-level = "z"
lto = true
codegen-units = 1

[workspace.package]
version = "1.0.11"
description = "Huber, simplify GitHub package management"
authors = ["David Ko <innobead@gmail.com>"]
edition = "2021"
keywords = ["github", "package-management", "cli"]
categories = ["command-line-interface", "command-line-utilities", "development-tools"]
homepage = "https://github.com/innobead/huber"
repository = "https://github.com/innobead/huber"
readme = "README.md"
license-file = "LICENSE"

[workspace.dependencies]
huber-procmacro = { path = "huber-procmacro", version = "1.0.11" }
libcli-rs = "0.1.4"
clap = { version = "4.5.21", features = ["env", "derive"] }
log = "0.4"
env_logger = "0.11.5"
lazy_static = "1.4.0"
anyhow = "1.0"
dirs = "5.0.0"
semver = "1.0.14"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
serde_yaml = "0.9.19"
reqwest = { version = "0.12.9", default-features = false, features = ["json", "native-tls-vendored"] }
tokio = { version = "1.27", features = ["full"] }
regex = "1.4.1"
futures = "0.3"
async-trait = "0.1.64"
git2 = { version = "0.20.0", features = ["vendored-libgit2", "vendored-openssl"] }
chrono = "0.4"
symlink = "0.1.0"
is_executable = "1.0.1"
urlencoding = "2.1.2"
url = "2"
fs_extra = "1.1"
maplit = "1.0"
rayon = "1.6"
simpledi-rs = "0.1.0"
quote = "1.0"
octocrab = "0.42.1"
syn = "2.0.90"
fs2 = "0.4.3"
clap_complete = "4.5.40"
thiserror = "2.0.9"
scopeguard = "1.1.0"
better-panic = "0.3.0"
filepath = "0.2.0"
tar = "0.4.43"
xz2 = "0.1.0"
flate2 = "1.0.19"
zip = { version = "2.2.2", default-features = false, features = ["deflate-zlib-ng"] }
```

## File: `Dockerfile.build`
```
FROM rust:latest as build

WORKDIR /workspace

ARG TARGETPLATFORM
ARG BUILDPLATFORM
ARG BUILD_TARGET=debug
ARG JUST_TARGET=build

COPY . /workspace

RUN suffix=$(echo ${TARGETPLATFORM} | sed "s/\//-/g") && \
    apt update && \
    apt install -y sudo && \
    ./hack/setup-dev.sh && \
    just ${JUST_TARGET} && \
    cp target/${BUILD_TARGET}/huber target/${BUILD_TARGET}/huber-${suffix}

FROM scratch
ARG BUILD_TARGET=debug
COPY --from=build /workspace/target/${BUILD_TARGET}/huber-* /target/
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
<div align="center" style="text-align: center;">
<img src="https://raw.githubusercontent.com/innobead/huber/HEAD/docs/src/images/huber_logo.png" alt="huber" style="width:300px;"/>
</div>

<div align="center">

[![crates.io](https://img.shields.io/crates/v/huber.svg)](https://crates.io/crates/huber)
[![Releases](https://img.shields.io/github/release/innobead/huber/all.svg)](https://github.com/innobead/huber/releases)
[![GitHub](https://img.shields.io/github/license/innobead/huber)](https://github.com/innobead/huber/blob/master/LICENSE)
[![Docs](https://img.shields.io/badge/docs-latest-green.svg)](https://innobead.github.io/huber/)

</div>

**Huber** is a command-line interface tool for managing packages released from GitHub repositories. It allows you to install, update, and manage packages from GitHub repository releases in a simple and efficient way.

What features does Huber provide?

- Manage (install, update, uninstall, show, current) multiple version packages from GitHub repository releases
- Search popular GitHub repositories that Huber manages in a [curated list](docs/src/contributing/huber-managed-packages.md)
- Manage your own repositories to install packages you need
- Lock and unlock installed package versions
- Save and restore package versions
- and more..., please check the documentation for more details

> [!NOTE]  
> This documentation is for the version starting from 1.0.0. If you are using older versions, suggest upgrading to the latest version.

# Installation

Huber is supported on Linux, macOS, and Windows platforms.

- Linux (x86_64/amd64, aarch64/arm64, arm)
- MacOS (x86_64/amd64, aarch64/arm64)
- Windows (x86_64/amd64)

You can install Huber via the following methods:

**Cargo:**

```shell
cargo install huber
```

**Shell script:**

```shell
curl -sfSL https://raw.githubusercontent.com/innobead/huber/main/hack/install.sh | sh -
```

**PowerShell:**

```powershell
. { iwr -useb https://raw.githubusercontent.com/innobead/huber/main/hack/windows/install.ps1 } | iex; install
```

**Precompiled binaries:**

Download Huber executables from [GitHub releases](https://github.com/innobead/huber/releases)

# Getting Started

After installing Huber, you can start using it by running the `huber` command.

```console
$ huber --help
Huber, simplify GitHub package management

Usage: huber [OPTIONS] <COMMAND>

Commands:
  config       Manage Huber configurations
  current      Update the current package versions
  completions  Show command completions for the specified shell
  flush        Remove outdated installed artifacts
  info         Show package information
  install      Install packages
  repo         Manage repositories
  reset        Reset Huber
  search       Search package
  self-update  Update huber
  show         Show installed packages
  uninstall    Uninstall packages
  update       Updates the installed packages
  save         Save the installed package list to a file
  load         Load installed packages from a file generated by save command
  lock         Lock packages or Show locked packages
  unlock       Unlock packages
  help         Print this message or the help of the given subcommand(s)

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
  -V, --version
          Print version
```

Search and install a package:

```console
$ huber search k9s
 Name  Description                                          Source 
 k9s   🐶 Kubernetes CLI To Manage Your Clusters In Style!  https://github.com/derailed/k9s 
 
$ huber install k9s
[INFO ] k9s version not specified, getting the latest version (v0.32.7)
[INFO ] Installing package k9s@latest/v0.32.7
[INFO ] Downloading https://github.com/derailed/k9s/releases/download/v0.32.7/k9s_Linux_amd64.tar.gz
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@latest/v0.32.7 installed

$ k9s version
 ____  __.________       
|    |/ _/   __   \______
|      < \____    /  ___/
|    |  \   /    /\___ \ 
|____|__ \ /____//____  >
        \/            \/ 

Version:    v0.32.7
Commit:     6b5d24f5741a1789fb97ba3e11f0ee868d93459d
Date:       2024-11-16T20:22:28Z
```

For frequently used and advanced commands, please check the detailed documentation [here](https://innobead.github.io/huber/).

# License

The Huber source and documentation are released under the Apache License v2.0.
```

## File: `justfile`
```
prj_dir := justfile_directory()
build_dir := prj_dir / '.target'
huber_pkg_root_dir := prj_dir / 'generated-v1'
huber_exec := prj_dir / 'target/debug/huber'
cargo_opts := env('CARGO_OPTS', '')
github_token := env('GITHUB_TOKEN', '')
github_key := env('GITHUB_KEY', '')

# Install Rust componetns and tooling dependencies
build-deps:
    rustup component add rustfmt clippy
    cargo install cross
    cargo install default-target
    cargo install --git https://github.com/DevinR528/cargo-sort.git --tag v1.1.0 cargo-sort
    cargo install cargo-udeps
    cargo install mdbook mdbook-linkcheck mdbook-alerts mdbook-theme

# Build binaries
build target='' cmd_opts='':
    @rustup target add {{ if target != "" { target } else { shell("default-target") } }}
    @cargo {{ cargo_opts }} build {{ cmd_opts }} {{ if target != "" { "--target " + target } else { "" } }}

# Build binaries via Cross
build-cross target="" cmd_opts='':
    @cross {{ cargo_opts }} build {{ cmd_opts }} --target {{ if target != "" { target } else { shell("default-target") } }}

# Run tests
test:
    @cargo {{ cargo_opts }} test

# Format & Fix codes
ffix:
    @cargo-sort --workspace
    @cargo {{ cargo_opts }} +nightly fmt --all
    @cargo clippy --fix --no-deps --allow-dirty --allow-staged
    @cargo {{ cargo_opts }} fix --allow-dirty --allow-staged

# Find unused dependencies
udeps:
    @cargo +nightly udeps --all-targets

# Release binaries
release:
    @just build '' '--release'

# Clean build caches
clean:
    @cargo clean
    @rm -rf {{ build_dir }}

# Publish Huber to crates.io
publish:
    @cargo publish {{ cargo_opts }} --manifest-path={{ prj_dir }}/crates/common/Cargo.toml || true
    @sleep 10 && cargo publish {{ cargo_opts }} --manifest-path={{ prj_dir }}/crates/procmacro/Cargo.toml || true
    @sleep 10 && cargo publish {{ cargo_opts }} --manifest-path={{ prj_dir }}/crates/app/Cargo.toml || true

# (local dev) Setup development environment
setup-dev:
    @{{ prj_dir }}/hack/setup-dev.sh

# (local dev) Generate managed package list
generate force='true':
    @echo "! Must have GITHUB_TOKEN to automatically generate package description"
    @GITHUB_TOKEN={{ github_token }} FORCE={{ force }} cargo build {{ cargo_opts }} -vv --package=huber-generator
    @GITHUB_KEY={{ github_key }} just build && (HUBER_PKG_ROOT_DIR={{ huber_pkg_root_dir }} {{ huber_exec }} search | xargs -0 {{ prj_dir }}/hack/generate-huber-packages.sh)

# (local dev) Install binaries
install:
    @cargo install {{ cargo_opts }} --path {{ prj_dir }}/crates/app/ --bins
    @mkdir -p ~/.huber/bin && cp ~/.cargo/bin/huber ~/.huber/bin && {{ prj_dir }}/hack/add-huber-bin-to-env.sh

# (local dev) Run commands using the built Huber with the local package generated folder
run huber_cmd pkg_dir=huber_pkg_root_dir:
    HUBER_PKG_ROOT_DIR={{ pkg_dir }} {{ huber_exec }} {{ huber_cmd }}

# (local dev) Run commands using the installed Huber with the local package generated folder
run-installed huber_cmd pkg_dir=huber_pkg_root_dir:
    HUBER_PKG_ROOT_DIR={{ pkg_dir }} `which huber` {{ huber_cmd }}

doc:
    @mdbook build docs
```

## File: `rustfmt.toml`
```
# Set the maximum width of a line
max_width = 100

# Use spaces instead of tabs for indentation
hard_tabs = false

# Number of spaces per indentation level
tab_spaces = 4

# Control the style of braces
brace_style = "SameLineWhere"

# Reorder imports automatically
reorder_imports = true

# Group imports by standard, external, and local crates
group_imports = "StdExternalCrate"

# Enable unstable features if needed (requires nightly)
unstable_features = true
```

## File: `docs/book.toml`
```
[book]
description = "Install, upgrade and manage GitHub release packages with ease"
authors = ["David Ko"]
language = "en"

[rust]
edition = "2021"

[preprocessor.alerts]

[output.html]
default-theme = "Navy"
git-repository-url = "https://github.com/innobead/huber"

[output.linkcheck]

[output.html.search]
limit-results = 20
```

## File: `docs/src/README.md`
```markdown
<div style="text-align: center;">
<img src="images/huber_logo.png" alt="huber" style="width:300px;"/>
</div>

**Huber** is a command-line interface tool for managing packages from GitHub repositories. It allows you to install, update, and manage packages from GitHub repository releases in a simple and efficient
way.

What features does Huber provide?

- Manage (install, update, uninstall, show, current) multiple version packages from GitHub repository releases
- Search popular GitHub repositories that Huber manages in a curated list
- Lock and unlock installed package versions
- Save and restore package versions
- and more..., please check the documentation for more details

> [!NOTE]  
> This documentation is for the version starting from 1.0.0. If you are using older versions, suggest upgrading to the latest version.

# Installation

Huber is supported on Linux, macOS, and Windows platforms.

- Linux (x86_64/amd64, aarch64/arm64, arm)
- MacOS (x86_64/amd64, aarch64/arm64)
- Windows (x86_64/amd64)

You can install Huber via the following methods:

**Cargo:**

```console
cargo install huber
```

**Shell script:**

```console
curl -sfSL https://raw.githubusercontent.com/innobead/huber/main/hack/install.sh | sh -
```

**PowerShell:**

```powershell
. { iwr -useb https://raw.githubusercontent.com/innobead/huber/main/hack/windows/install.ps1 } | iex; install
```

**Precompiled binaries:**

Download Huber executables from [GitHub releases](https://github.com/innobead/huber/releases)

# Getting Started

After installing Huber, you can start using it by running the `huber` command.

```console
$ huber --help
Huber, simplify GitHub package management

Usage: huber [OPTIONS] <COMMAND>

Commands:
  config       Manage Huber configurations
  current      Update the current package versions
  completions  Show command completions for the specified shell
  flush        Remove outdated installed artifacts
  info         Show package information
  install      Install packages
  repo         Manage repositories
  reset        Reset Huber
  search       Search package
  self-update  Update huber
  show         Show installed packages
  uninstall    Uninstall packages
  update       Updates the installed packages
  save         Save the installed package list to a file
  load         Load installed packages from a file generated by save command
  lock         Lock packages or Show locked packages
  unlock       Unlock packages
  help         Print this message or the help of the given subcommand(s)

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
  -V, --version
          Print version
```

Search and install a package:

```console
$ huber search k9s
 Name  Description                                          Source 
 k9s   🐶 Kubernetes CLI To Manage Your Clusters In Style!  https://github.com/derailed/k9s 
 
$ huber install k9s
[INFO ] k9s version not specified, getting the latest version (v0.32.7)
[INFO ] Installing package k9s@latest/v0.32.7
[INFO ] Downloading https://github.com/derailed/k9s/releases/download/v0.32.7/k9s_Linux_amd64.tar.gz
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@latest/v0.32.7 installed

$ k9s version
 ____  __.________       
|    |/ _/   __   \______
|      < \____    /  ___/
|    |  \   /    /\___ \ 
|____|__ \ /____//____  >
        \/            \/ 

Version:    v0.32.7
Commit:     6b5d24f5741a1789fb97ba3e11f0ee868d93459d
Date:       2024-11-16T20:22:28Z
```

For frequently used and advanced commands, please check the corresponding sections.

# License

The Huber source and documentation are released under the Apache License v2.0.
```

## File: `docs/src/SUMMARY.md`
```markdown
# Summary

[Introduction](./README.md)

# Frequently Used Commands

- [install](../../../core/security/QUARANTINE/vetted/repos/codex/docs/install.md)
- [info](../../../vault/archives/archive_legacy/openapi-generator/samples/client/echo_api/java/okhttp-gson-user-defined-templates/info.md)
- [search](search.md)
- [show](./cmd/show.md)
- [uninstall](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/cli/uninstall.md)
- [update](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/cli/update.md)

# Advanced Commands

- [config](config.md)
- [current](./cmd/current.md)
- [completions](./cmd/completions.md)
- [flush](./cmd/flush.md)
- [repo](../../../core/security/QUARANTINE/incoming/repos/AutoGPT/docs/integrations/block_integrations/github/repo.md)
- [reset](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/cli/reset.md)
- [self-update](./cmd/self-update.md)
- [save](./cmd/save.md)
- [load](load.md)
- [lock](../../../vault/archives/archive_legacy/milvus/docs/agent_guides/streaming-system/wal/lock.md)
- [unlock](./cmd/unlock.md)

# Contributing

- [Huber Managed Packages](./contributing/huber-managed-packages.md)
- [Add a New Package](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/commands/project-management/add-package.md)
```

## File: `docs/src/cmd/completions.md`
```markdown
# The `completions` Command

The `completions` command shows command completions for the specified shell. It is useful for setting up command completions for Huber.

```console
$ huber completions --help
Show command completions for the specified shell

Usage: huber completions [OPTIONS] <SHELL>

Arguments:
  <SHELL>  Shell name [possible values: bash, elvish, fish, powershell, zsh]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```
```

## File: `docs/src/cmd/config.md`
```markdown
# The `config` Command

The `config` command manages Huber configurations including log level, GitHub token, GitHub SSH key, Huber directory, and GitHub base URI. If you want to use Huber behind a proxy, you can set the proxy server to serve the GitHub base URI.

```console
$ huber config --help
Manages huber configurations

Usage: huber config [OPTIONS] <COMMAND>

Commands:
  show  Show Huber configurations
  save  Save Huber configurations via global options
  help  Print this message or the help of the given subcommand(s)

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

# The `config show` Command

The `config show` command shows Huber configurations.

```console
$ huber config show --help
Show Huber configurations

Usage: huber config show [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

# The `config save` Command

The `config save` command saves Huber configurations via global options.

```console
$ huber config save --help
Save Huber configurations via global options

Usage: huber config save [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```
```

## File: `docs/src/cmd/current.md`
```markdown
# The `current` Command

The `current` command updates the current package versions if there are multiple versions of the same package installed.

```console
$ huber current --help
Update the current package versions

Usage: huber current [OPTIONS] <NAME_VERSION>...

Arguments:
  <NAME_VERSION>...  Package name with version (e.g. 'package-name@version')

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Update the current package version

```console
$ huber show --all
 Name     Version  Current  Kind 
 k9s      v0.32.7  true    Release 
 k9s      v0.32.5  false     Release 

$ huber current k9s@v0.32.5
[INFO ] Updating the current version of k9s to v0.32.5
[INFO ] k9s@v0.32.5 is now the current version

$ huber show --all
 Name     Version  Current  Kind 
 k9s      v0.32.7  false    Release 
 k9s      v0.32.5  true     Release 
```

```

## File: `docs/src/cmd/flush.md`
```markdown
# The `flush` Command

The `flush` command removes outdated installed artifacts to free up disk space.

```console
Remove outdated installed artifacts

Usage: huber flush [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Flush outdated installed (non-current) artifacts

```console
$ huber show --all
 Name     Version  Current  Kind 
 k9s      v0.32.7  false    Release 
 k9s      v0.32.5  true     Release 

$ huber flush
[INFO ] Removing k9s (version: v0.32.7, source: github)
[INFO ] k9s (version: v0.32.7, source: github) removed

$ huber show --all
 Name     Version  Current  Kind 
 k9s      v0.32.5  true     Release 
```
```

## File: `docs/src/cmd/info.md`
```markdown
# The `info` Command

The `info` command shows package information.

```console
$ huber info --help
Shows package information

Usage: huber info [OPTIONS] <NAME>

Arguments:
  <NAME>  Package name

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Show package information

```console
$ huber info k9s
 Name  Version  Source             Targets 
 k9s   v0.32.7  Github:            - LinuxAmd64: 
                  owner: derailed      artifact_templates: 
                  repo: k9s            - k9s_Linux_amd64.tar.gz 
                                   - LinuxArm64: 
                                       artifact_templates: 
                                       - k9s_Linux_arm64.tar.gz 
                                   - MacOSAmd64: 
                                       artifact_templates: 
                                       - k9s_Darwin_amd64.tar.gz 
                                   - MacOSArm64: 
                                       artifact_templates: 
                                       - k9s_Darwin_arm64.tar.gz 
                                   - WindowsAmd64: 
                                       artifact_templates: 
                                       - k9s_Windows_amd64.zip 
```
```

## File: `docs/src/cmd/install.md`
```markdown
# The `install` Command

The `install` command installs packages. You can specify the package name and version to install, install multiple packages at once, install the latest version of a package without specifying the
version, and install packages from a file generated by the [load](./load.md) command.

```console
$ huber install --help
Install packages

Usage: huber install [OPTIONS] <NAME_VERSION>...

Arguments:
  <NAME_VERSION>...  Package name (e.g. 'package-name', 'package-name@version')g. 'owner/repo', 'owner/repo@version') for unmanaged packages by repositories

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --prefer-stdlib <PREFER_STDLIB>
          Prefer standard library (only for Linux or Windows) [default: gnu] [possible values: gnu, musl]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Install a package

```console
$ huber install k9s
[INFO ] k9s version not specified, getting the latest version (v0.32.7)
[INFO ] Installing package k9s@latest/v0.32.7
[INFO ] Downloading https://github.com/derailed/k9s/releases/download/v0.32.7/k9s_Linux_amd64.tar.gz
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@latest/v0.32.7 installed

$ huber install k9s@v0.32.5
[INFO ] Installing package k9s@v0.32.5
[INFO ] Downloading https://github.com/derailed/k9s/releases/download/v0.32.5/k9s_Linux_amd64.tar.gz
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@v0.32.5 installed

$ huber show
 Name     Version  Current  Kind 
 k9s      v0.32.5  true     Release 

$ huber show --all
 Name     Version  Current  Kind 
 k9s      v0.32.7  false    Release 
 k9s      v0.32.5  true     Release 
```

### Install multiple packages

```console
$ huber install k9s kubectl
[INFO ] kubectl version not specified, getting the latest version (v1.32.1)
[INFO ] Installing package kubectl@latest/v1.32.1
[INFO ] k9s version not specified, getting the latest version (v0.32.7)
[INFO ] Installing package k9s@latest/v0.32.7
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@latest/v0.32.7 installed
[INFO ] Installed executables of kubectl:
    [
        "/home/davidko/.huber/bin/kubectl",
    ]
[INFO ] kubectl@latest/v1.32.1 installed
```

### Install an unmanaged package directly from a repository

```console
$ huber install rancher/rke
[INFO ] rancher/rke version not specified, getting the latest version (v1.7.2)
[INFO ] Installing package rancher/rke@latest/v1.7.2
[INFO ] Prefer downloading assets belonging to the specified stdlib: gnu
[INFO ] Downloading https://github.com/rancher/rke/releases/download/v1.7.2/rke_linux-amd64
[INFO ] Installed executables of rancher/rke:
    [
        "/home/davidko/.huber/bin/rke",
    ]
[INFO ] rancher/rke@latest/v1.7.2 installed

$ huber show
 Name         Version  Current  Kind 
 rancher/rke  v1.7.2   true     Release 
```

### Install a tag-only package which has no release

> [!NOTE]  
> This kind of package is not supported by the `update` command.
> To install a different version, you need to specify the version to install the package.

```console
$ huber install go
[WARN ] Failed to get the latest release version of go: GitHub
[INFO ] go version not specified, getting the latest version ()
[ERROR] Failed to get the latest release version of go to install; Use debug log to get more detailed error info

$ huber install go@go1.24.0
[WARN ] Failed to get the latest release version of go: GitHub
[INFO ] Installing package go@go1.24.0
[INFO ] Prefer downloading assets belonging to the specified stdlib: gnu
[INFO ] Downloading https://golang.org/dl/go1.24.0.linux-amd64.tar.gz
[INFO ] Installed executables of go:
    [
        "/home/davidko/.huber/bin/gofmt",
        "/home/davidko/.huber/bin/go",
    ]
[INFO ] go@go1.24.0 installed

$ huber show
 Name  Version   Current  Kind 
 go    go1.24.0  true     
```
```

## File: `docs/src/cmd/load.md`
```markdown
# The `load` Command

The `load` command reads the package list from a file generated by the [save](./save.md) command and installs the packages.

```console
$ huber load --help
Load installed packages from a file generated by save command

Usage: huber load [OPTIONS]

Options:
      --file <FILE>
          Load a package list to install [default: huber-packages.txt]
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Load installed packages from a file

```console
$ huber load --file output.txt
[INFO ] Loading packages from output.txt
[INFO ] Loaded packages: total 1: [
        "k9s@v0.32.7",
    ]
[INFO ] Installing packages: total 1
[INFO ] Installing package k9s@v0.32.7
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@v0.32.7 installed
[INFO ] Installed packages: total 1
```

```

## File: `docs/src/cmd/lock.md`
```markdown
# The `lock` Command

The `lock` command allows you to lock packages or display locked packages. When a package is locked, it will not be updated by the `huber update` command if its version is equal to or lower than the locked version requirement.

The package locking uses Cargo's version requirement format.

```console
the locked version.

```console
$ huber lock --help
Lock packages or Show locked packages

Usage: huber lock [OPTIONS] [NAME_VERSION]... [COMMAND]

Commands:
  show  Show locked versions
  help  Print this message or the help of the given subcommand(s)

Arguments:
  [NAME_VERSION]...  Package name (e.g. 'package-name', 'package-name@semver' or 'package-name@<semver-requirement>' using Cargo's dependency version requirement format)

Options:
      --all
          Lock all installed `current` packages
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --caret-required
          Treat version requirement as a caret requirement if no version requirement is specified
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --tilde-required
          Treat version requirement as a tilde requirement if no version requirement is specified
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

# The `lock show` Command

The `lock show` command shows locked packages and their locked version requirements.

```console
$ huber lock show --help
Usage: huber lock show [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

Lock a package:

```console
$ huber install k9s@v0.32.5
[INFO ] Installing package k9s@v0.32.5
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@v0.32.5 installed

$ huber lock k9s@=0.32.5
[INFO ] Locking packages
[INFO ] Locking package k9s@=0.32.5
[INFO ] Packages locked successfully: {
        "k9s": "=0.32.5",
    }

$ huber lock show
 Name  Version 
 k9s   =0.32.5 
 
$ huber update k9s
[INFO ] Checking for updates for k9s. The latest installed version is v0.32.5
[INFO ] Found the latest version of k9s: v0.32.7
[WARN ] Package k9s is locked to version =0.32.5. Skipping update to v0.32.7

$ huber install k9s@v0.32.7
[WARN ] Package k9s is locked to version =0.32.5. Skipping installing v0.32.7

```
```

## File: `docs/src/cmd/repo.md`
```markdown
# The `repo` Command

The `repo` command allows you to manage repositories. Huber includes two types of repositories:

- Huber managed repository, which provides a curated list of packages
- Local repository, which supports installing packages directly from remote GitHub repositories

In addition to these built-in repositories, you can also add your own repositories to install packages from them.

```console
$ huber repo --help
Manage repositories

Usage: huber repo [OPTIONS] <COMMAND>

Commands:
  add     Add a new repo
  remove  Remove a repo
  show    Show all repos
  help    Print this message or the help of the given subcommand(s)

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

# The `repo add` Command

The `repo add` command adds a new repository using the URL or file path of the Huber package index file.

```console
$ huber repo add --help
Add a new repository

Usage: huber repo add [OPTIONS] --url <URL> --file <FILE> <NAME>

Arguments:
  <NAME>  Repo name

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --url <URL>
          URL of the Huber package index file
      --file <FILE>
          File path of the Huber package index file
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

The index file is a YAML file that contains the list of packages as the below example:

```yaml
- name: aichat
  description: All-in-one LLM CLI tool featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents, with access to OpenAI, Claude, Gemini, Ollama, Groq, and more.
  source: !Github
    owner: sigoden
    repo: aichat
  targets:
  - !LinuxAmd64
    artifact_templates:
    - 'aichat-v{version}-x86_64-unknown-linux-musl.tar.gz'

```

# The `repo remove` Command

The `repo remove` command removes a repository.

```console
Remove a repository

Usage: huber repo remove [OPTIONS] [NAME]...

Arguments:
  [NAME]...  Repo names

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

# The `repo show` Command

The `repo show` command shows all repositories.

```console
$ huber repo show --help
Show all repositories

Usage: huber repo show [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Add a new repository via a file

```console
$ huber repo add --url https://raw.githubusercontent.com/innobead/huber/refs/heads/main/docs/src/cmd/repo/huber.yaml self-hosted
[INFO ] Adding repo self-hosted
[INFO ] Repo self-hosted added

$ huber repo show
 Name         Url                                                                                            File 
 local                                                                                                        
 self-hosted  https://raw.githubusercontent.com/innobead/huber/refs/heads/main/docs/src/cmd/repo/huber.yaml   
 
$ huber search aichat --repo self-hosted
 Name    Description                                                                                              Source 
 aichat  All-in-one LLM CLI tool featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents, with access to...  https://github.com/sigoden/aichat 
```

### Add a package to the local repository if the package is not available in the Huber managed repository

```console
$ huber search --repo local
[INFO ] No packages found

$ huber search rancher/rke
[INFO ] No packages found

$ huber install rancher/rke
[INFO ] rancher/rke version not specified, getting the latest version (v1.7.2)
[INFO ] Installing package rancher/rke@latest/v1.7.2
[INFO ] Prefer downloading assets belonging to the specified stdlib: gnu
[INFO ] Downloading https://github.com/rancher/rke/releases/download/v1.7.2/rke_linux-amd64
[INFO ] Installed executables of rancher/rke:
    [
        "/home/davidko/.huber/bin/rke",
    ]
[INFO ] rancher/rke@latest/v1.7.2 installed

$ huber search --repo local
 Name         Description  Source 
 rancher/rke               https://github.com/rancher/rke 
```
```

## File: `docs/src/cmd/reset.md`
```markdown
# The `reset` Command

The `reset` command resets Huber to its initial state.

```console
$ huber reset --help
Reset Huber

Usage: huber reset [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Reset Huber

```console
$ huber install k9s
[INFO ] k9s version not specified, getting the latest version (v0.32.7)
[INFO ] Installing package k9s@latest/v0.32.7
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@latest/v0.32.7 installed
 
$ huber reset
[INFO ] Resetting Huber by removing created caches, downloaded files and installed packages
[INFO ] Huber reset

$ huber show
[INFO ] No packages installed
```
```

## File: `docs/src/cmd/save.md`
```markdown
# The `save` Command

The `save` command saves the installed package list to a file which can be used by the [load](./load.md) command.

```console
$ huber save --help
Save the installed package list to a file

Usage: huber save [OPTIONS]

Options:
      --file <FILE>
          File path to save the installed package list [default: huber-packages.txt]
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Save the installed package list

```console
$ huber save --file output.txt
[INFO ] Collecting installed current packages
[INFO ] Saving the package list to output.txt
[INFO ] Saved the package list to /home/davidko/github/innobead/huber/output.txt

$ cat output.txt
k9s@v0.32.7
```
```

## File: `docs/src/cmd/search.md`
```markdown
# The `search` Command

The `search` command searches for a package by name or regex pattern.

```console
$ huber search --help
Search package

Usage: huber search [OPTIONS] [NAME]

Arguments:
  [NAME]  Package name or regex search with --pattern

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --pattern
          Regex search
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --owner <OWNER>
          Package owner
      --all
          Show all the released versions
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --repo <REPO>
          Search in a specific repository
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Search packages by pattern

```console
$ huber search --pattern wasm
 Name         Description                                                                                              Source 
 rustwasmc    Tool for building Rust functions for Node.js. Combine the performance of Rust, safety and portabilit...  https://github.com/second-state/rustwasmc 
 wasm-to-oci  Use OCI registries to distribute Wasm modules                                                            https://github.com/engineerd/wasm-to-oci 
 wasme        Web Assembly tools and SDKs for extending cloud-native infrastructure                                    https://github.com/solo-io/wasm 
 wasmer       🚀 Fast, secure, lightweight containers based on WebAssembly                                             https://github.com/wasmerio/wasmer 
 wasmtime     A lightweight WebAssembly runtime that is fast, secure, and standards-compliant                          https://github.com/bytecodealliance/wasmtime 
```

### Search a package by name. Using the `--all` flag to show all the released versions.

```console
$ huber search wasmtime
 Name      Description                                                                      Source 
 wasmtime  A lightweight WebAssembly runtime that is fast, secure, and standards-compliant  https://github.com/bytecodealliance/wasmtime 
```

```console
$ huber search wasmtime --all
 Version  Kind 
 dev      PreRelease 
 v29.0.1  Release 
 v29.0.0  Release 
 v28.0.1  Release 
 v28.0.0  Release 
 v27.0.0  Release 
 v26.0.1  Release 
 v26.0.0  Release 
 v25.0.3  Release 
 v25.0.2  Release 
 v25.0.1  Release 
 v25.0.0  Release 
 v24.0.2  Release 
 v24.0.1  Release 
 v24.0.0  Release 
 ...
```
```

## File: `docs/src/cmd/self-update.md`
```markdown
# The `self-update` Command

The `self-update` command updates Huber if a new version is available.

```console
$ huber self-update --help
Update huber

Usage: huber self-update [OPTIONS]

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --prefer-stdlib <PREFER_STDLIB>
          Prefer standard library (only for Linux or Windows) [possible values: gnu, musl, msvc]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Update Huber

```console
$ huber -V
huber v1.0.8-dirty

$ huber self-update
[INFO ] Updating Huber v1.0.9
[INFO ] Prefer downloading assets belonging to the specified stdlib: gnu
[INFO ] Installed executables of huber:
    [
        "/home/davidko/.huber/bin/huber",
    ]
[INFO ] Huber updated to v1.0.9

$ huber --version
huber v1.0.9-dirty Commit: e14f0cb-20250209181740
```
```

## File: `docs/src/cmd/show.md`
```markdown
# The `show` Command

The `show` command shows installed packages.

```console
$ huber show --help
Show installed packages

Usage: huber show [OPTIONS] [NAME]

Arguments:
  [NAME]  Package name

Options:
      --all
          Show all the installed versions
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --detail
          Show the detailed artifact info
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Show installed packages

```console
```console
$ huber show --all
 Name     Version  Current  Kind 
 k9s      v0.32.7  true     Release 
 k9s      v0.32.5  false    Release 
```
```

## File: `docs/src/cmd/uninstall.md`
```markdown
# The `uninstall` Command

The `uninstall` command uninstalls packages.

```console
$ huber uninstall --help
Uninstall packages

Usage: huber uninstall [OPTIONS] [NAME]...

Arguments:
  [NAME]...  Package name

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help 
```

## Examples

### Uninstall multiple packages

```console
$ huber uninstall k9s kubectl
[INFO ] Uninstalling k9s
[INFO ] Uninstalled k9s
[INFO ] Uninstalling kubectl
[INFO ] Uninstalled kubectl
```

### Uninstall an unmanaged package directly from a repository

```console
$ huber uninstall rancher/rke
[INFO ] Uninstalling rancher/rke
[INFO ] Uninstalled rancher/rke
```
```

## File: `docs/src/cmd/unlock.md`
```markdown
# The `unlock` Command

The `unlock` command unlocks packages.

```console
$ huber unlock --help
Unlock packages

Usage: huber unlock [OPTIONS] <NAME>...

Arguments:
  <NAME>...  Package name

Options:
      --all
          Unlock all the locked packages
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Unlock all the locked packages

```console
$huber lock k9s
[INFO ] Locking packages
[INFO ] Locking package k9s@=0.32.5
[INFO ] Packages locked successfully: {
        "k9s": "0.32.5",
    }

$ huber unlock --all
[INFO ] Unlocking packages
[INFO ] Unlocking all packages
[INFO ] Unlocked packages

$ huber lock show
[INFO ] No packages locked
```
```

## File: `docs/src/cmd/update.md`
```markdown
# The `update` Command

The `update` command updates the installed packages.

```console
$ huber update --help
Updates the installed packages

Usage: huber update [OPTIONS] [NAME]...

Arguments:
  [NAME]...  Package name

Options:
  -l, --log-level <LOG_LEVEL>
          Log level [default: OFF]
      --prefer-stdlib <PREFER_STDLIB>
          Prefer standard library (only for Linux or Windows) [possible values: gnu, musl, msvc]
      --dryrun
          Dry run to show available updates
      --github-token <GITHUB_TOKEN>
          GitHub token; Optional until reaching the rate limit of GitHub API [env: GITHUB_TOKEN=]
      --github-key <GITHUB_KEY>
          Github SSH key path; Optional, if you want to use SSH to clone the Huber repository [env: GITHUB_KEY=]
      --huber-dir <HUBER_DIR>
          Huber directory [default: /home/davidko/.huber]
      --github-base-uri <GITHUB_BASE_URI>
          GitHub base URI [env: GITHUB_BASE_URI=] [default: https://api.github.com]
  -h, --help
          Print help
```

## Examples

### Update the installed packages

```console
$ huber install k9s@v0.32.5 kubectl@v1.31.0
[INFO ] Installing package k9s@v0.32.5
[INFO ] Installing package kubectl@v1.31.0
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] k9s@v0.32.5 installed
[INFO ] Installed executables of kubectl:
    [
        "/home/davidko/.huber/bin/kubectl",
    ]
[INFO ] kubectl@v1.31.0 installed

$ huber update
[INFO ] Checking for updates for k9s. The latest installed version is v0.32.5
[INFO ] Checking for updates for kubectl. The latest installed version is v1.31.0
[INFO ] Found the latest version of kubectl: v1.32.1
[INFO ] Updating package kubectl from v1.31.0 to v1.32.1
[INFO ] Updating kubectl (version: v1.31.0, source: github) to kubectl (version: v1.32.1, source: github)
[INFO ] Found the latest version of k9s: v0.32.7
[INFO ] Updating package k9s from v0.32.5 to v0.32.7
[INFO ] Updating k9s (version: v0.32.5, source: github) to k9s (version: v0.32.7, source: github)
[INFO ] Installed executables of kubectl:
    [
        "/home/davidko/.huber/bin/kubectl",
    ]
[INFO ] Package kubectl updated to v1.32.1 successfully
[INFO ] Installed executables of k9s:
    [
        "/home/davidko/.huber/bin/k9s",
    ]
[INFO ] Package k9s updated to v0.32.7 successfully

```

### Update an unmanaged package directly from a repository

```console
$ huber install rancher/rke@v1.7.0
[INFO ] Installing package rancher/rke@v1.7.0
[INFO ] Prefer downloading assets belonging to the specified stdlib: gnu
[INFO ] Downloading https://github.com/rancher/rke/releases/download/v1.7.0/rke_linux-amd64
[INFO ] Installed executables of rancher/rke:
    [
        "/home/davidko/.huber/bin/rke",
    ]
[INFO ] rancher/rke@v1.7.0 installed

$ huber update rancher/rke
[INFO ] Checking for updates for rancher/rke. The latest installed version is v1.7.0
[INFO ] Found the latest version of rancher/rke: v1.7.2
[INFO ] Updating package rancher/rke from v1.7.0 to v1.7.2
[INFO ] Updating rancher/rke (version: v1.7.0, source: github) to rancher/rke (version: v1.7.2, source: github)
[INFO ] Prefer downloading assets belonging to the specified stdlib: gnu
[INFO ] Downloading https://github.com/rancher/rke/releases/download/v1.7.2/rke_linux-amd64
[INFO ] Installed executables of rancher/rke:
    [
        "/home/davidko/.huber/bin/rke",
    ]
[INFO ] Package rancher/rke updated to v1.7.2 successfully
```
```

## File: `docs/src/cmd/repo/huber.yaml`
```yaml
- name: aichat
  description: All-in-one LLM CLI tool featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents, with access to OpenAI, Claude, Gemini, Ollama, Groq, and more.
  source: !Github
    owner: sigoden
    repo: aichat
  targets:
  - !LinuxAmd64
    artifact_templates:
    - 'aichat-v{version}-x86_64-unknown-linux-musl.tar.gz'
```

## File: `docs/src/contributing/add-package.md`
```markdown
# Add a New Package

We use `ollam` as an example to show how to add a new package to the generator.

## Step 1: Create a new package module in `./huber-generator/src/pkg`

You can specify the exact artifact name template or use the default automatic artifact name recognition.

```rust
#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ollama".to_string(),
        source: PackageSource::Github {
            owner: "ollama".to_string(),
            repo: "ollama".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["ollama-linux-amd64.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["ollama-linux-arm64.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["ollama-darwin".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["ollama-windows-amd64.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

If the artifact name includes [`env::consts::OS`](https://doc.rust-lang.org/std/env/consts/constant.OS.html), [`env::consts::ARCH`](https://doc.rust-lang.org/std/env/consts/constant.ARCH.html), values
defined in [GOOS/GOARCH](https://pkg.go.dev/internal/platform) and release [semantic versions](https://semver.org/), you can use the default automatic artifact name recognition below instead of
specifying the artifact name template.

Besides downloading executables, Huber also supports downloading compressed files to extract executables from them. If the artifact name ends with `.tar.gz`, `.tar.xz`, `.zip`, `.tar`, `.tgz`, or
`.gz`, Huber will automatically decompress the file after downloading.

The following table shows some automatic artifact name recognition for different operating systems and architectures:

| OS            | ARCH               | Asset name                  | Renamed asset name |
|---------------|--------------------|-----------------------------|--------------------|
| linux         | amd64, x86_64, ..  | `ollama-linux-amd64`        | `ollam`            |
| linux         | aarch64, arm64, .. | `ollama-linux-arm64.tar.gz` | `ollam.tar.gz`     |
| macos, darwin | aarch64, arm64, .. | `ollama-darwin-arm64`       | `ollam`            |
| windows       | amd64, X86_64, ..  | `ollama-windows-amd64.zip`  | `ollam.zip`        |

```rust
#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ollama".to_string(),
        source: PackageSource::Github {
            owner: "ollama".to_string(),
            repo: "ollama".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## Step 2: Declare the package module in `./huber-generator/src/pkg/mod.rs`

```rust
pub mod ollama;
```

## Step 3: Export the package to the release function in `./huber-generator/src/build.rs`

```rust

fn releases() -> Vec<Package> {
    vec![
        // ... existing packages
        // Add the new package here
        ollama::release(),
    ]
}
```

## Step 4: Run the generator

After running the following command, the generator will automatically generate the package information to the `./generated-v1` directory and update the
`./docs/src/contributing/huber-managed-packages.md` file.

```console
just generate
```

Finally, please create a pull request to merge the changes into the main branch. Thank you for contributing to Huber!
```

## File: `docs/src/contributing/huber-managed-packages.md`
```markdown
# Huber Managed Packages

This package list is generated by `huber search` using the default Huber package repository.
To add a new package, please follow the instructions in [Add a New Package](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/commands/project-management/add-package.md).

```console
 Name             Description                                                                                              Source 
 ali              Generate HTTP load and plot the results in real-time                                                     https://github.com/nakabonne/ali 
 argocd           Declarative Continuous Deployment for Kubernetes                                                         https://github.com/argoproj/argo-cd 
 arkade           Open Source Marketplace For Developer Tools                                                              https://github.com/alexellis/arkade 
 asdf             Extendable version manager with support for Ruby, Node.js, Elixir, Erlang {value} more                         https://github.com/asdf-vm/asdf 
 axelard          Axelar: A Decentralized Blockchain Interoperability Network                                              https://github.com/axelarnetwork/axelar-core 
 bat              A cat(1) clone with wings.                                                                               https://github.com/sharkdp/bat 
 bottom           Yet another cross-platform graphical process/system monitor.                                             https://github.com/ClementTsang/bottom 
 buf              The best way of working with Protocol Buffers.                                                           https://github.com/bufbuild/buf 
 bun              Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one               https://github.com/oven-sh/bun 
 camel-k          Apache Camel K is a lightweight integration platform, born on Kubernetes, with serverless superpower...  https://github.com/apache/camel-k 
 chisel           A fast TCP/UDP tunnel over HTTP                                                                          https://github.com/jpillora/chisel 
 choose           A human-friendly and fast alternative to cut and (sometimes) awk                                         https://github.com/theryangeary/choose 
 cloak            A censorship circumvention tool to evade detection by authoritarian state adversaries                    https://github.com/cbeuw/Cloak 
 cni-plugins      Some reference and example networking plugins, maintained by the CNI team.                               https://github.com/containernetworking/plugins 
 codeql           Binaries for the CodeQL CLI                                                                              https://github.com/github/codeql-cli-binaries 
 compose          Define and run multi-container applications with Docker                                                  https://github.com/docker/compose 
 conftest         Write tests against structured configuration data using the Open Policy Agent Rego query language        https://github.com/open-policy-agent/conftest 
 consul           Consul is a distributed, highly available, and data center aware solution to connect and configure a...  https://github.com/hashicorp/consul 
 containerd       An open and reliable container runtime                                                                   https://github.com/containerd/containerd 
 copilot-cli      The AWS Copilot CLI is a tool for developers to build, release and operate production ready containe...  https://github.com/aws/copilot-cli 
 coreutils        Cross-platform Rust rewrite of the GNU coreutils                                                         https://github.com/uutils/coreutils 
 cosign           Code signing and transparency for containers and binaries                                                https://github.com/sigstore/cosign 
 croc             Easily and securely send things from one computer to another :crocodile: :package:                       https://github.com/schollz/croc 
 ctlptl           Making local Kubernetes clusters fun and easy to set up                                                  https://github.com/tilt-dev/ctlptl 
 czkawka          Multi functional app to find duplicates, empty folders, similar images etc.                              https://github.com/qarmin/czkawka 
 dasel            Select, put and delete data from JSON, TOML, YAML, XML and CSV files with a single tool. Supports co...  https://github.com/TomWright/dasel 
 delta            A syntax-highlighting pager for git, diff, grep, and blame output                                        https://github.com/dandavison/delta 
 deno             A modern runtime for JavaScript and TypeScript.                                                          https://github.com/denoland/deno 
 direnv           unclutter your .profile                                                                                  https://github.com/direnv/direnv 
 dive             A tool for exploring each layer in a docker image                                                        https://github.com/wagoodman/dive 
 doctl            The official command line interface for the DigitalOcean API.                                            https://github.com/digitalocean/doctl 
 dog              A command-line DNS client.                                                                               https://github.com/ogham/dog 
 dolt             Dolt – Git for Data                                                                                      https://github.com/dolthub/dolt 
 dua-cli          View disk space usage and delete unwanted data, fast.                                                    https://github.com/Byron/dua-cli 
 dust             A more intuitive version of du in rust                                                                   https://github.com/bootandy/dust 
 eksctl           The official CLI for Amazon EKS                                                                          https://github.com/eksctl-io/eksctl 
 exa              A modern replacement for ‘ls’.                                                                           https://github.com/ogham/exa 
 fd               A simple, fast and user-friendly alternative to 'find'                                                   https://github.com/sharkdp/fd 
 firecracker      Secure and fast microVMs for serverless computing.                                                       https://github.com/firecracker-microvm/firecracker 
 fission          Fast and Simple Serverless Functions for Kubernetes                                                      https://github.com/fission/fission 
 fleet            Deploy workloads from Git to large fleets of Kubernetes clusters                                         https://github.com/rancher/fleet 
 flux2            Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.              https://github.com/fluxcd/flux2 
 fnm              🚀 Fast and simple Node.js version manager, built in Rust                                                https://github.com/Schniz/fnm 
 fortio           Fortio load testing library, command line tool, advanced echo server and web UI in go (golang). Allo...  https://github.com/fortio/fortio 
 foundry          Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written...  https://github.com/foundry-rs/foundry 
 frum             A little bit fast and modern Ruby version manager written in Rust                                        https://github.com/TaKO8Ki/frum 
 gh               GitHub’s official command line tool                                                                      https://github.com/cli/cli 
 gitleaks         Find secrets with Gitleaks 🔑                                                                            https://github.com/gitleaks/gitleaks 
 gitui            Blazing 💥 fast terminal-ui for git written in rust 🦀                                                   https://github.com/extrawurst/gitui 
 go               The Go programming language                                                                              https://github.com/golang/go 
 go-http-tunnel   Fast and secure tunnels over HTTP/2                                                                      https://github.com/mmatczuk/go-http-tunnel 
 goose            A database migration tool. Supports SQL migrations and Go functions.                                     https://github.com/pressly/goose 
 gping            Ping, but with a graph                                                                                   https://github.com/orf/gping 
 gradle           Adaptable, fast automation for all                                                                       https://github.com/gradle/gradle 
 grex             A command-line tool and Rust library with Python bindings for generating regular expressions from us...  https://github.com/pemistahl/grex 
 grpcurl          Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers                             https://github.com/fullstorydev/grpcurl 
 helm             The Kubernetes Package Manager                                                                           https://github.com/helm/helm 
 helmfile         Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases. Gene...  https://github.com/helmfile/helmfile 
 hetty            An HTTP toolkit for security research.                                                                   https://github.com/dstotijn/hetty 
 hexyl            A command-line hex viewer                                                                                https://github.com/sharkdp/hexyl 
 httptap          View HTTP/HTTPS requests made by any Linux program                                                       https://github.com/monasticacademy/httptap 
 huber            Huber: simplify GitHub package management                                                                https://github.com/innobead/huber 
 hugo             The world’s fastest framework for building websites.                                                     https://github.com/gohugoio/hugo 
 hyperfine        A command-line benchmarking tool                                                                         https://github.com/sharkdp/hyperfine 
 img              Standalone, daemon-less, unprivileged Dockerfile and OCI compatible container image builder.             https://github.com/genuinetools/img 
 istio            Connect, secure, control, and observe services.                                                          https://github.com/istio/istio 
 jiq              jid on jq - interactive JSON query tool using jq expressions                                             https://github.com/fiatjaf/jiq 
 jless            jless is a command-line JSON viewer designed for reading, exploring, and searching through JSON data...  https://github.com/PaulJuliusMartinez/jless 
 jq               Command-line JSON processor                                                                              https://github.com/jqlang/jq 
 just             🤖 Just a command runner                                                                                 https://github.com/casey/just 
 jwt-cli          A super fast CLI tool to decode and encode JWTs built in Rust                                            https://github.com/mike-engel/jwt-cli 
 k0s              k0s - The Zero Friction Kubernetes                                                                       https://github.com/k0sproject/k0s 
 k3d              Little helper to run CNCF's k3s in Docker                                                                https://github.com/k3d-io/k3d 
 k3s              Lightweight Kubernetes                                                                                   https://github.com/k3s-io/k3s 
 k3sup            bootstrap K3s over SSH in < 60s 🚀                                                                       https://github.com/alexellis/k3sup 
 k6               A modern load testing tool, using Go and JavaScript - https://k6.io                                      https://github.com/grafana/k6 
 k9s              🐶 Kubernetes CLI To Manage Your Clusters In Style!                                                      https://github.com/derailed/k9s 
 kind             Kubernetes IN Docker - local clusters for testing Kubernetes                                             https://github.com/kubernetes-sigs/kind 
 ko               Build and deploy Go applications                                                                         https://github.com/ko-build/ko 
 kompose          Convert Compose to Kubernetes                                                                            https://github.com/kubernetes/kompose 
 kotlin           The Kotlin Programming Language.                                                                         https://github.com/JetBrains/kotlin 
 kpt              Automate Kubernetes Configuration Editing                                                                https://github.com/GoogleContainerTools/kpt 
 krew             📦 Find and install kubectl plugins                                                                      https://github.com/kubernetes-sigs/krew 
 kube-bench       Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kub...  https://github.com/aquasecurity/kube-bench 
 kube-linter      KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the...  https://github.com/stackrox/kube-linter 
 kubectl          Production-Grade Container Scheduling and Management                                                     https://github.com/kubernetes/kubernetes 
 kubefire         KubeFire 🔥, creates and manages Kubernetes Clusters using Firecracker microVMs                          https://github.com/innobead/kubefire 
 kubestr                                                                                                                   https://github.com/kastenhq/kubestr 
 kubevirt         Kubernetes Virtualization API and runtime in order to define and manage virtual machines.                https://github.com/kubevirt/kubevirt 
 kustomize        Customization of kubernetes YAML configurations                                                          https://github.com/kubernetes-sigs/kustomize 
 kuttl            KUbernetes Test TooL (kuttl)                                                                             https://github.com/kudobuilder/kuttl 
 linkerd2-edge    Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x.                       https://github.com/linkerd/linkerd2 
 linkerd2-stable  Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x.                       https://github.com/linkerd/linkerd2 
 loc              Count lines of code quickly.                                                                             https://github.com/cgag/loc 
 local-ai         :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first....  https://github.com/mudler/LocalAI 
 lsd              The next gen ls command                                                                                  https://github.com/lsd-rs/lsd 
 minikube         Run Kubernetes locally                                                                                   https://github.com/kubernetes/minikube 
 mkcert           A simple zero-config tool to make locally trusted development certificates with any names you'd like...  https://github.com/FiloSottile/mkcert 
 nat              `ls` alternative with useful info and a splash of color 🎨                                               https://github.com/willdoescode/nat 
 natscli          The NATS Command Line Interface                                                                          https://github.com/nats-io/natscli 
 navi             An interactive cheatsheet tool for the command-line                                                      https://github.com/denisidoro/navi 
 nerdctl          contaiNERD CTL - Docker-compatible CLI for containerd, with support for Compose, Rootless, eStargz, ...  https://github.com/containerd/nerdctl 
 node             Node.js JavaScript runtime ✨🐢🚀✨                                                                      https://github.com/nodejs/node 
 norouter         NoRouter: IP-over-Stdio. The easiest multi-host {value} multi-cloud networking ever. No root privilege is ...  https://github.com/norouter/norouter 
 nushell          A new type of shell                                                                                      https://github.com/nushell/nushell 
 octant           Highly extensible platform for developers to better understand the complexity of Kubernetes clusters...  https://github.com/vmware-tanzu/octant 
 okteto           Develop your applications directly in your Kubernetes Cluster                                            https://github.com/okteto/okteto 
 ollama           Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 2, and other large language models.         https://github.com/ollama/ollama 
 onefetch         Command-line Git information tool                                                                        https://github.com/o2sh/onefetch 
 opa              Open Policy Agent (OPA) is an open source, general-purpose policy engine.                                https://github.com/open-policy-agent/opa 
 opentofu         OpenTofu lets you declaratively manage your cloud infrastructure.                                        https://github.com/opentofu/opentofu 
 oras             OCI registry client - managing content like artifacts, images, packages                                  https://github.com/oras-project/oras 
 pack             CLI for building apps using Cloud Native Buildpacks                                                      https://github.com/buildpacks/pack 
 packer           Packer is a tool for creating identical machine images for multiple platforms from a single source c...  https://github.com/hashicorp/packer 
 podman           Podman: A tool for managing OCI containers and pods.                                                     https://github.com/containers/podman 
 powershell       PowerShell for every system!                                                                             https://github.com/PowerShell/PowerShell 
 procs            A modern replacement for ps written in Rust                                                              https://github.com/dalance/procs 
 protoc           Protocol Buffers - Google's data interchange format                                                      https://github.com/protocolbuffers/protobuf 
 pueue            :stars: Manage your shell commands.                                                                      https://github.com/Nukesor/pueue 
 pulumi           Pulumi - Infrastructure as Code in any programming language 🚀                                           https://github.com/pulumi/pulumi 
 rclone           "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi...  https://github.com/rclone/rclone 
 regclient        Docker and OCI Registry Client in Go and tooling using those libraries.                                  https://github.com/regclient/regclient 
 ripgrep          ripgrep recursively searches directories for a regex pattern while respecting your gitignore             https://github.com/BurntSushi/ripgrep 
 rke2                                                                                                                      https://github.com/rancher/rke2 
 sad              CLI search and replace | Space Age seD                                                                   https://github.com/ms-jpq/sad 
 saml2aws         CLI tool which enables you to login and retrieve AWS temporary credentials using a SAML IDP              https://github.com/Versent/saml2aws 
 sd               Intuitive find {value} replace CLI (sed alternative)                                                           https://github.com/chmln/sd 
 shadowsocks      A Rust port of shadowsocks                                                                               https://github.com/shadowsocks/shadowsocks-rust 
 skaffold         Easy and Repeatable Kubernetes Development                                                               https://github.com/GoogleContainerTools/skaffold 
 skim             Fuzzy Finder in rust!                                                                                    https://github.com/skim-rs/skim 
 solidity         Solidity, the Smart Contract Programming Language                                                        https://github.com/ethereum/solidity 
 sonobuoy         Sonobuoy is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster b...  https://github.com/vmware-tanzu/sonobuoy 
 starship         ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell!                        https://github.com/starship/starship 
 stern            ⎈ Multi pod and container log tailing for Kubernetes -- Friendly fork of https://github.com/wercke...    https://github.com/stern/stern 
 syncthing        Open Source Continuous File Synchronization                                                              https://github.com/syncthing/syncthing 
 tealdeer         A very fast implementation of tldr in Rust.                                                              https://github.com/tealdeer-rs/tealdeer 
 termshark        A terminal UI for tshark, inspired by Wireshark                                                          https://github.com/gcla/termshark 
 terraform        Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a ...  https://github.com/hashicorp/terraform 
 terrascan        Detect compliance and security violations across Infrastructure as Code to mitigate risk before prov...  https://github.com/tenable/terrascan 
 tilt             Define your dev environment as code. For microservice apps on Kubernetes.                                https://github.com/tilt-dev/tilt 
 tokei            Count your code, quickly.                                                                                https://github.com/XAMPPRocky/tokei 
 tracee           Linux Runtime Security and Forensics using eBPF                                                          https://github.com/aquasecurity/tracee 
 traefik          The Cloud Native Application Proxy                                                                       https://github.com/traefik/traefik 
 trivy            Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories,...  https://github.com/aquasecurity/trivy 
 typescript       TypeScript is a superset of JavaScript that compiles to clean JavaScript output.                         https://github.com/microsoft/TypeScript 
 typos            Source code spell checker                                                                                https://github.com/crate-ci/typos 
 vegeta           HTTP load testing tool and library. It's over 9000!                                                      https://github.com/tsenart/vegeta 
 velero           Backup and migrate Kubernetes applications and their persistent volumes                                  https://github.com/vmware-tanzu/velero 
 viddy            👀 A modern watch command. Time machine and pager etc.                                                   https://github.com/sachaos/viddy 
 volta            Volta: JS Toolchains as Code. ⚡                                                                         https://github.com/volta-cli/volta 
 wabt             The WebAssembly Binary Toolkit                                                                           https://github.com/WebAssembly/wabt 
 wasmer           🚀 Fast, secure, lightweight containers based on WebAssembly                                             https://github.com/wasmerio/wasmer 
 wasmtime         A lightweight WebAssembly runtime that is fast, secure, and standards-compliant                          https://github.com/bytecodealliance/wasmtime 
 wstunnel         Tunnel all your traffic over Websocket or HTTP2 - Bypass firewalls/DPI - Static binary available         https://github.com/erebe/wstunnel 
 xh               Friendly and fast tool for sending HTTP requests                                                         https://github.com/ducaale/xh 
 yq               yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties processor                       https://github.com/mikefarah/yq 
 zellij           A terminal workspace with batteries included                                                             https://github.com/zellij-org/zellij 
 zola             A fast static site generator in a single binary with everything built-in. https://www.getzola.org        https://github.com/getzola/zola 
 zoxide           A smarter cd command. Supports all major shells.                                                         https://github.com/ajeetdsouza/zoxide 

```
```

## File: `generated/DEPRECATED`
```
This is for backwards compatibility with the old v0 release. It will be removed in the future.

Please use the new v1 release instead and notice it is incompatible with the old v0 release.
```

## File: `generated/index.yaml`
```yaml
# This is generated. Don't modify.
- name: ali
  owner: nakabonne
  source: github
- name: argocd
  owner: argoproj
  source: github
- name: arkade
  owner: alexellis
  source: github
- name: axelard
  owner: axelarnetwork
  source: github
- name: bat
  owner: sharkdp
  source: github
- name: bottom
  owner: ClementTsang
  source: github
- name: buf
  owner: bufbuild
  source: github
- name: camel-k
  owner: apache
  source: github
- name: chisel
  owner: jpillora
  source: github
- name: choose
  owner: theryangeary
  source: github
- name: cloak
  owner: evansmurithi
  source: github
- name: codeql
  owner: github
  source: github
- name: conftest
  owner: open-policy-agent
  source: github
- name: consul
  owner: hashicorp
  source: github
- name: containerd
  owner: containerd
  source: github
- name: copilot-cli
  owner: aws
  source: github
- name: coreutils
  owner: uutils
  source: github
- name: cosign
  owner: sigstore
  source: github
- name: croc
  owner: schollz
  source: github
- name: ctlptl
  owner: tilt-dev
  source: github
- name: czkawka
  owner: qarmin
  source: github
- name: dasel
  owner: TomWright
  source: github
- name: delta
  owner: dandavison
  source: github
- name: deno
  owner: denoland
  source: github
- name: direnv
  owner: direnv
  source: github
- name: dive
  owner: wagoodman
  source: github
- name: doctl
  owner: digitalocean
  source: github
- name: dog
  owner: ogham
  source: github
- name: dolt
  owner: dolthub
  source: github
- name: drone-cli
  owner: drone
  source: github
- name: dua-cli
  owner: Byron
  source: github
- name: dust
  owner: bootandy
  source: github
- name: eksctl
  owner: weaveworks
  source: github
- name: epinio
  owner: epinio
  source: github
- name: exa
  owner: ogham
  source: github
- name: faas-cli
  owner: openfaas
  source: github
- name: fd
  owner: sharkdp
  source: github
- name: firecracker
  owner: firecracker-microvm
  source: github
- name: fission
  owner: fission
  source: github
- name: fleet
  owner: rancher
  source: github
- name: flux2
  owner: fluxcd
  source: github
- name: fnm
  owner: Schniz
  source: github
- name: fortio
  owner: fortio
  source: github
- name: frum
  owner: TaKO8Ki
  source: github
- name: gh
  owner: cli
  source: github
- name: gitui
  owner: extrawurst
  source: github
- name: go-http-tunnel
  owner: mmatczuk
  source: github
- name: gping
  owner: orf
  source: github
- name: gradle
  owner: gradle
  source: github
- name: grex
  owner: pemistahl
  source: github
- name: grpcurl
  owner: fullstorydev
  source: github
- name: helm
  owner: helm
  source: github
- name: helmfile
  owner: roboll
  source: github
- name: hetty
  owner: dstotijn
  source: github
- name: hexyl
  owner: sharkdp
  source: github
- name: hub
  owner: github
  source: github
- name: huber
  owner: innobead
  source: github
- name: hugo
  owner: gohugoio
  source: github
- name: hyperfine
  owner: sharkdp
  source: github
- name: hypper
  owner: rancher-sandbox
  source: github
- name: ignite
  owner: weaveworks
  source: github
- name: img
  owner: genuinetools
  source: github
- name: istio
  owner: istio
  source: github
- name: jiq
  owner: fiatjaf
  source: github
- name: jless
  owner: PaulJuliusMartinez
  source: github
- name: jq
  owner: stedolan
  source: github
- name: just
  owner: casey
  source: github
- name: jwt-cli
  owner: mike-engel
  source: github
- name: k0s
  owner: k0sproject
  source: github
- name: k3ai
  owner: kf5i
  source: github
- name: k3d
  owner: rancher
  source: github
- name: k3s
  owner: rancher
  source: github
- name: k3sup
  owner: alexellis
  source: github
- name: k6
  owner: k6io
  source: github
- name: k9s
  owner: derailed
  source: github
- name: keptn
  owner: keptn
  source: github
- name: ketch
  owner: shipa-corp
  source: github
- name: kind
  owner: kubernetes-sigs
  source: github
- name: ko
  owner: google
  source: github
- name: kompose
  owner: kubernetes
  source: github
- name: kotlin
  owner: JetBrains
  source: github
- name: kpt
  owner: GoogleContainerTools
  source: github
- name: krew
  owner: kubernetes-sigs
  source: github
- name: krustlet
  owner: deislabs
  source: github
- name: kube-bench
  owner: aquasecurity
  source: github
- name: kube-linter
  owner: stackrox
  source: github
- name: kubectl
  owner: kubernetes
  source: github
- name: kubefire
  owner: innobead
  source: github
- name: kubestr
  owner: kastenhq
  source: github
- name: kubevirt
  owner: kubevirt
  source: github
- name: kudo
  owner: kudobuilder
  source: github
- name: kustomize
  owner: kubernetes-sigs
  source: github
- name: kuttl
  owner: kudobuilder
  source: github
- name: kwctl
  owner: kubewarden
  source: github
- name: lens
  owner: lensapp
  source: github
- name: linkerd2-edge
  owner: linkerd
  source: github
- name: linkerd2-stable
  owner: linkerd
  source: github
- name: loc
  owner: cgag
  source: github
- name: lsd
  owner: lsd-rs
  source: github
- name: minikube
  owner: kubernetes
  source: github
- name: mkcert
  owner: FiloSottile
  source: github
- name: nat
  owner: willdoescode
  source: github
- name: natscli
  owner: nats-io
  source: github
- name: navi
  owner: denisidoro
  source: github
- name: nerdctl
  owner: containerd
  source: github
- name: node
  owner: nodejs
  source: github
- name: nomad
  owner: hashicorp
  source: github
- name: norouter
  owner: norouter
  source: github
- name: nushell
  owner: nushell
  source: github
- name: octant
  owner: vmware-tanzu
  source: github
- name: okteto
  owner: okteto
  source: github
- name: onefetch
  owner: o2sh
  source: github
- name: opa
  owner: open-policy-agent
  source: github
- name: opni
  owner: rancher
  source: github
- name: oras
  owner: deislabs
  source: github
- name: pack
  owner: buildpacks
  source: github
- name: packer
  owner: hashicorp
  source: github
- name: podman
  owner: containers
  source: github
- name: powershell
  owner: PowerShell
  source: github
- name: procs
  owner: dalance
  source: github
- name: protoc
  owner: protocolbuffers
  source: github
- name: pueue
  owner: Nukesor
  source: github
- name: pulumi
  owner: pulumi
  source: github
- name: rancher
  owner: rancher
  source: github
- name: rancher-cli
  owner: rancher
  source: github
- name: renote
  owner: ecatlabs
  source: github
- name: rio
  owner: rancher
  source: github
- name: ripgrep
  owner: BurntSushi
  source: github
- name: rke
  owner: rancher
  source: github
- name: rke2
  owner: rancher
  source: github
- name: rustwasmc
  owner: second-state
  source: github
- name: sad
  owner: ms-jpq
  source: github
- name: saml2aws
  owner: Versent
  source: github
- name: sd
  owner: chmln
  source: github
- name: shadowsocks
  owner: shadowsocks
  source: github
- name: shisho
  owner: flatt-security
  source: github
- name: skaffold
  owner: GoogleContainerTools
  source: github
- name: skim
  owner: lotabout
  source: github
- name: solidity
  owner: ethereum
  source: github
- name: sonobuoy
  owner: vmware-tanzu
  source: github
- name: ssvm
  owner: second-state
  source: github
- name: starship
  owner: starship
  source: github
- name: stern
  owner: stern
  source: github
- name: submariner
  owner: submariner-io
  source: github
- name: syncthing
  owner: syncthing
  source: github
- name: tealdeer
  owner: dbrgn
  source: github
- name: tecli
  owner: awslabs
  source: github
- name: termshark
  owner: gcla
  source: github
- name: terraform
  owner: hashicorp
  source: github
- name: terrascan
  owner: tenable
  source: github
- name: tilt
  owner: tilt-dev
  source: github
- name: tokei
  owner: XAMPPRocky
  source: github
- name: tracee
  owner: aquasecurity
  source: github
- name: trivy
  owner: aquasecurity
  source: github
- name: typescript
  owner: microsoft
  source: github
- name: typos
  owner: crate-ci
  source: github
- name: vegeta
  owner: tsenart
  source: github
- name: velero
  owner: vmware-tanzu
  source: github
- name: viddy
  owner: sachaos
  source: github
- name: volta
  owner: volta-cli
  source: github
- name: wabt
  owner: WebAssembly
  source: github
- name: wasm-to-oci
  owner: engineerd
  source: github
- name: wasme
  owner: solo-io
  source: github
- name: wasmer
  owner: wasmerio
  source: github
- name: wasmtime
  owner: bytecodealliance
  source: github
- name: waypoint
  owner: hashicorp
  source: github
- name: wstunnel
  owner: erebe
  source: github
- name: xh
  owner: ducaale
  source: github
- name: yq
  owner: mikefarah
  source: github
- name: zellij
  owner: zellij-org
  source: github
- name: zola
  owner: getzola
  source: github
- name: zoxide
  owner: ajeetdsouza
  source: github
```

## File: `generated/packages/ali.yaml`
```yaml
# This is generated. Don't modify.
name: ali
description: Generate HTTP load and plot the results in real-time
source:
  Github:
    owner: nakabonne
    repo: ali
targets:
- LinuxAmd64:
    artifact_templates:
    - ali_{version}_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - ali_{version}_linux_arm64.tar.gz
- LinuxArm32:
    artifact_templates:
    - ali_{version}_linux_armv7.tar.gz
- MacOS:
    artifact_templates:
    - ali_{version}_darwin_amd64.tar.gz
- Windows:
    artifact_templates:
    - ali_{version}_windows_amd64.tar.gz
detail: null
```

## File: `generated/packages/argocd.yaml`
```yaml
# This is generated. Don't modify.
name: argocd
description: Declarative Continuous Deployment for Kubernetes
source:
  Github:
    owner: argoproj
    repo: argo-cd
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/argocd-linux-amd64'
- MacOS:
    artifact_templates:
    - '{version}/argocd-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/argocd-windows-amd64.exe'
detail: null
```

## File: `generated/packages/arkade.yaml`
```yaml
# This is generated. Don't modify.
name: arkade
description: Open Source Marketplace For Developer Tools
source:
  Github:
    owner: alexellis
    repo: arkade
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/arkade'
- LinuxArm64:
    artifact_templates:
    - '{version}/arkade-arm64'
- MacOS:
    artifact_templates:
    - '{version}/arkade-darwin'
- MacOSArm64:
    artifact_templates:
    - '{version}/arkade-darwin-arm64'
- Windows:
    artifact_templates:
    - '{version}/arkade.exe'
detail: null
```

## File: `generated/packages/axelard.yaml`
```yaml
# This is generated. Don't modify.
name: axelard
description: 'Axelar : A Decentralized Blockchain Interoperability Network'
source:
  Github:
    owner: axelarnetwork
    repo: axelar-core
targets:
- LinuxAmd64:
    artifact_templates:
    - axelard-linux-amd64-v{version}
- LinuxArm64:
    artifact_templates:
    - axelard-linux-arm64-v{version}
- LinuxArm32:
    artifact_templates:
    - axelard-linux-amd-v{version}
- MacOS:
    artifact_templates:
    - axelard-darwin-amd64-v{version}
- MacOSArm64:
    artifact_templates:
    - axelard-darwin-arm64-v{version}
- Windows:
    artifact_templates:
    - ali_{version}_windows_amd64.tar.gz
detail: null
```

## File: `generated/packages/bat.yaml`
```yaml
# This is generated. Don't modify.
name: bat
description: A cat(1) clone with wings.
source:
  Github:
    owner: sharkdp
    repo: bat
targets:
- LinuxAmd64:
    artifact_templates:
    - bat-v{version}-x86_64-unknown-linux-gnu.tar.gz
- MacOS:
    artifact_templates:
    - bat-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - bat-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/bottom.yaml`
```yaml
# This is generated. Don't modify.
name: bottom
description: Yet another cross-platform graphical process/system monitor.
source:
  Github:
    owner: ClementTsang
    repo: bottom
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/bottom_x86_64-unknown-linux-musl.tar.gzz'
- LinuxArm64:
    artifact_templates:
    - '{version}/bottom_aarch64-unknown-linux-gnu.tar.gz'
- LinuxArm32:
    artifact_templates:
    - '{version}/bottom_armv7-unknown-linux-gnueabihf.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/bottom_x86_64-apple-darwin.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/bottom_x86_64-pc-windows-msvc.zip'
detail: null
```

## File: `generated/packages/buf.yaml`
```yaml
# This is generated. Don't modify.
name: buf
description: A new way of working with Protocol Buffers.
source:
  Github:
    owner: bufbuild
    repo: buf
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/buf-Linux-x86_64'
    - '{version}/protoc-gen-buf-breaking-Linux-x86_64'
- LinuxArm64:
    artifact_templates:
    - '{version}/buf-Linux-aarch64'
    - '{version}/protoc-gen-buf-breaking-Linux-aarch64'
- MacOS:
    artifact_templates:
    - '{version}/buf-Darwin-x86_64'
    - '{version}/protoc-gen-buf-breaking-Darwin-x86_64'
- MacOSArm64:
    artifact_templates:
    - '{version}/buf-Darwin-arm64'
    - '{version}/protoc-gen-buf-breaking-Darwin-arm64'
- Windows:
    artifact_templates:
    - '{version}/buf-Windows-x86_64'
    - '{version}/protoc-gen-buf-breaking-Windows-x86_64'
- WindowsArm64:
    artifact_templates:
    - '{version}/buf-Windows-arm64'
    - '{version}/protoc-gen-buf-breaking-Windows-arm64'
detail: null
```

## File: `generated/packages/camel-k.yaml`
```yaml
# This is generated. Don't modify.
name: camel-k
description: Apache Camel K is a lightweight integration platform, born on Kubernetes, with serverless superpowers
source:
  Github:
    owner: apache
    repo: camel-k
targets:
- LinuxAmd64:
    artifact_templates:
    - camel-k-client-{version}-linux-64bit.tar.gz
- MacOS:
    artifact_templates:
    - camel-k-client-{version}-mac-64bit.tar.gz
- Windows:
    artifact_templates:
    - camel-k-client-{version}-windows-64bit.tar.gz
detail: null
```

## File: `generated/packages/chisel.yaml`
```yaml
# This is generated. Don't modify.
name: chisel
description: A fast TCP/UDP tunnel over HTTP
source:
  Github:
    owner: jpillora
    repo: chisel
targets:
- LinuxAmd64:
    artifact_templates:
    - chisel_{version}_linux_amd64.gz
- LinuxArm64:
    artifact_templates:
    - chisel_{version}_linux_arm64.gz
- MacOS:
    artifact_templates:
    - chisel_{version}_darwin_amd64.gz
- Windows:
    artifact_templates:
    - chisel_{version}_windows_amd64.gz
detail: null
```

## File: `generated/packages/choose.yaml`
```yaml
# This is generated. Don't modify.
name: choose
description: A human-friendly and fast alternative to cut and (sometimes) awk
source:
  Github:
    owner: theryangeary
    repo: choose
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/choose'
detail: null
```

## File: `generated/packages/cloak.yaml`
```yaml
# This is generated. Don't modify.
name: cloak
description: A Command Line OTP Authenticator application.
source:
  Github:
    owner: evansmurithi
    repo: cloak
targets:
- LinuxAmd64:
    artifact_templates:
    - cloak-v{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - cloak-v{version}-aarch64-unknown-linux-gnu.tar.gz
- MacOS:
    artifact_templates:
    - cloak-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - cloak-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/codeql.yaml`
```yaml
# This is generated. Don't modify.
name: codeql
description: Binaries for the CodeQL CLI
source:
  Github:
    owner: github
    repo: codeql-cli-binaries
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/codeql-linux64.zip'
- MacOS:
    artifact_templates:
    - '{version}/codeql-osx64.zip'
- Windows:
    artifact_templates:
    - '{version}/codeql-win64.zip'
detail: null
```

## File: `generated/packages/conftest.yaml`
```yaml
# This is generated. Don't modify.
name: conftest
description: Write tests against structured configuration data using the Open Policy Agent Rego query language
source:
  Github:
    owner: open-policy-agent
    repo: conftest
targets:
- LinuxAmd64:
    artifact_templates:
    - conftest_{version}_Linux_x86_64.tar.gz
- LinuxArm64:
    artifact_templates:
    - conftest_{version}_Linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - conftest_{version}_Darwin_x86_64.tar.gz
- Windows:
    artifact_templates:
    - conftest_{version}_Windows_x86_64.zip
detail: null
```

## File: `generated/packages/consul.yaml`
```yaml
# This is generated. Don't modify.
name: consul
description: Consul is a distributed, highly available, and data center aware solution to connect and configure applications across dynamic, distributed infrastructure.
source:
  Github:
    owner: hashicorp
    repo: consul
targets:
- LinuxAmd64:
    artifact_templates:
    - https://releases.hashicorp.com/consul/{version}/consul_{version}_linux_amd64.zip
- LinuxArm64:
    artifact_templates:
    - https://releases.hashicorp.com/consul/{version}/consul_{version}_linux_arm64.zip
- MacOS:
    artifact_templates:
    - https://releases.hashicorp.com/consul/{version}/consul_{version}_darwin_amd64.zip
- Windows:
    artifact_templates:
    - https://releases.hashicorp.com/consul/{version}/consul_{version}_windows_amd64.zip
detail: null
```

## File: `generated/packages/containerd.yaml`
```yaml
# This is generated. Don't modify.
name: containerd
description: An open and reliable container runtime
source:
  Github:
    owner: containerd
    repo: containerd
targets:
- LinuxAmd64:
    artifact_templates:
    - containerd-{version}-linux-amd64.tar.gz
    - cri-containerd-cni-{version}-linux-amd64.tar.gz
- Windows:
    artifact_templates:
    - containerd-{version}-windows-amd64.tar.gz
    - cri-containerd-cni-{version}-windows-amd64.tar.gz
detail: null
```

## File: `generated/packages/copilot-cli.yaml`
```yaml
# This is generated. Don't modify.
name: copilot-cli
description: 'The AWS Copilot CLI is a tool for developers to build, release and operate production ready containerized applications on AWS App Runner or Amazon ECS on AWS Fargate. '
source:
  Github:
    owner: aws
    repo: copilot-cli
targets:
- LinuxAmd64:
    artifact_templates:
    - copilot-linux-amd64-v{version}
- LinuxArm64:
    artifact_templates:
    - copilot-linux-arm64-v{version}
- MacOS:
    artifact_templates:
    - copilot-darwin-v{version}
- MacOS:
    artifact_templates:
    - copilot-windows-v{version}.exe
detail: null
```

## File: `generated/packages/coreutils.yaml`
```yaml
# This is generated. Don't modify.
name: coreutils
description: Cross-platform Rust rewrite of the GNU coreutils
source:
  Github:
    owner: uutils
    repo: coreutils
targets:
- LinuxAmd64:
    artifact_templates:
    - coreutils-{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - coreutils-{version}-aarch64-unknown-linux-gnu.tar.gz
- LinuxArm32:
    artifact_templates:
    - coreutils-{version}-arm-unknown-linux-gnueabihf.tar.gz
- MacOS:
    artifact_templates:
    - coreutils-{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - coreutils-{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/cosign.yaml`
```yaml
# This is generated. Don't modify.
name: cosign
description: Container Signing
source:
  Github:
    owner: sigstore
    repo: cosign
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/cosign-linux-amd64'
    - '{version}/cosigned-linux-amd64'
    - '{version}/sget-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/cosign-linux-arm64'
    - '{version}/cosigned-linux-arm64'
    - '{version}/sget-linux-arm64'
- LinuxArm32:
    artifact_templates:
    - '{version}/cosign-linux-arm'
    - '{version}/cosigned-linux-arm'
    - '{version}/sget-linux-arm'
- MacOS:
    artifact_templates:
    - '{version}/cosign-darwin-amd64'
    - '{version}/sget-darwin-amd64'
- MacOSArm64:
    artifact_templates:
    - '{version}/cosign-darwin-arm64'
    - '{version}/sget-darwin-arm64'
- Windows:
    artifact_templates:
    - '{version}/cosign-windows-amd64.exe'
    - '{version}/sget-windows-amd64.exe'
detail: null
```

## File: `generated/packages/croc.yaml`
```yaml
# This is generated. Don't modify.
name: croc
description: 'Easily and securely send things from one computer to another :crocodile: :package:'
source:
  Github:
    owner: schollz
    repo: croc
targets:
- LinuxAmd64:
    artifact_templates:
    - croc_{version}_Linux-64bit.tar.gz
    executable_templates:
    - croc
- LinuxArm64:
    artifact_templates:
    - croc_{version}_Linux-ARM64.tar.gz
    executable_templates:
    - croc
- MacOS:
    artifact_templates:
    - croc_{version}_macOS-64bit.tar.gz
    executable_templates:
    - croc
- Windows:
    artifact_templates:
    - croc_{version}_Windows-64bit.zip
    executable_templates:
    - croc.exe
detail: null
```

## File: `generated/packages/ctlptl.yaml`
```yaml
# This is generated. Don't modify.
name: ctlptl
description: Making local Kubernetes clusters fun and easy to set up
source:
  Github:
    owner: tilt-dev
    repo: ctlptl
targets:
- LinuxAmd64:
    artifact_templates:
    - ctlptl.{version}.linux.x86_64.tar.gz
- MacOS:
    artifact_templates:
    - ctlptl.{version}.mac.x86_64.tar.gz
- Windows:
    artifact_templates:
    - ctlptl.{version}.windows.x86_64.tar.gz
detail: null
```

## File: `generated/packages/czkawka.yaml`
```yaml
# This is generated. Don't modify.
name: czkawka
description: Multi functional app to find duplicates, empty folders, similar images etc.
source:
  Github:
    owner: qarmin
    repo: czkawka
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/linux_czkawka_cli'
    - '{version}/linux_czkawka_gui'
    - '{version}/linux_czkawka_gui.AppImage'
- MacOS:
    artifact_templates:
    - '{version}/mac_czkawka_cli'
- Windows:
    artifact_templates:
    - '{version}/windows_czkawka_cli.exe'
detail: null
```

## File: `generated/packages/dasel.yaml`
```yaml
# This is generated. Don't modify.
name: dasel
description: Select, put and delete data from JSON, TOML, YAML, XML and CSV files with a single tool. Supports conversion between formats and can be used as a Go package.
source:
  Github:
    owner: TomWright
    repo: dasel
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/dasel_linux_amd64'
- MacOS:
    artifact_templates:
    - '{version}/dasel_macos_amd64'
- Windows:
    artifact_templates:
    - '{version}/dasel_windows_amd64.exe'
detail: null
```

## File: `generated/packages/delta.yaml`
```yaml
# This is generated. Don't modify.
name: delta
description: A syntax-highlighting pager for git, diff, and grep output
source:
  Github:
    owner: dandavison
    repo: delta
targets:
- LinuxAmd64:
    artifact_templates:
    - delta-{version}-x86_64-unknown-linux-gnu.tar.gz
- LinuxArm64:
    artifact_templates:
    - delta-{version}-aarch64-unknown-linux-gnu.tar.gz
- LinuxArm32:
    artifact_templates:
    - delta-{version}-arm-unknown-linux-gnueabihf.tar.gz
- MacOS:
    artifact_templates:
    - delta-{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - delta-{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/deno.yaml`
```yaml
# This is generated. Don't modify.
name: deno
description: A modern runtime for JavaScript and TypeScript.
source:
  Github:
    owner: denoland
    repo: deno
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/deno-x86_64-unknown-linux-gnu.zip'
- MacOS:
    artifact_templates:
    - '{version}/deno-x86_64-apple-darwin.zip'
- MacOSArm64:
    artifact_templates:
    - '{version}/deno-aarch64-apple-darwin.zip'
- Windows:
    artifact_templates:
    - '{version}/deno-x86_64-pc-windows-msvc.zip'
detail: null
```

## File: `generated/packages/direnv.yaml`
```yaml
# This is generated. Don't modify.
name: direnv
description: unclutter your .profile
source:
  Github:
    owner: direnv
    repo: direnv
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/direnv.linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/direnv.linux-arm'
- MacOS:
    artifact_templates:
    - '{version}/direnv.darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/direnv.windows-amd64.exe'
detail: null
```

## File: `generated/packages/dive.yaml`
```yaml
# This is generated. Don't modify.
name: dive
description: A tool for exploring each layer in a docker image
source:
  Github:
    owner: wagoodman
    repo: dive
targets:
- LinuxAmd64:
    artifact_templates:
    - dive_{version}_linux_amd64.tar.gz
- MacOS:
    artifact_templates:
    - dive_{version}_darwin_amd64.tar.gz
- Windows:
    artifact_templates:
    - dive_{version}_windows_amd64.zip
detail: null
```

## File: `generated/packages/doctl.yaml`
```yaml
# This is generated. Don't modify.
name: doctl
description: The official command line interface for the DigitalOcean API.
source:
  Github:
    owner: digitalocean
    repo: doctl
targets:
- LinuxAmd64:
    artifact_templates:
    - doctl-{version}-linux-amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - doctl-{version}-linux-arm64.tar.gz
- MacOS:
    artifact_templates:
    - doctl-{version}-darwin-amd64.tar.gz
- Windows:
    artifact_templates:
    - doctl-{version}-windows-amd64.zip
detail: null
```

## File: `generated/packages/dog.yaml`
```yaml
# This is generated. Don't modify.
name: dog
description: A command-line DNS client.
source:
  Github:
    owner: ogham
    repo: dog
targets:
- LinuxAmd64:
    artifact_templates:
    - dog-v{version}-x86_64-unknown-linux-gnu.zip
- MacOS:
    artifact_templates:
    - dog-v{version}-x86_64-apple-darwin.zip
- Windows:
    artifact_templates:
    - dog-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/dolt.yaml`
```yaml
# This is generated. Don't modify.
name: dolt
description: Dolt – Git for Data
source:
  Github:
    owner: dolthub
    repo: dolt
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/dolt-linux-amd64.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/dolt-darwin-amd64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/dolt-windows-amd64.zip'
detail: null
```

## File: `generated/packages/drone-cli.yaml`
```yaml
# This is generated. Don't modify.
name: drone-cli
description: 'Command Line Tools for Drone CI '
source:
  Github:
    owner: drone
    repo: drone-cli
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/drone_linux_amd64.tar.gz'
- LinuxArm64:
    artifact_templates:
    - '{version}/drone_linux_arm64.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/drone_darwin_amd64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/drone_windows_amd64.tar.gz'
detail: null
```

## File: `generated/packages/dua-cli.yaml`
```yaml
# This is generated. Don't modify.
name: dua-cli
description: View disk space usage and delete unwanted data, fast.
source:
  Github:
    owner: Byron
    repo: dua-cli
targets:
- LinuxAmd64:
    artifact_templates:
    - dua-v{version}-x86_64-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - dua-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - dua-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/dust.yaml`
```yaml
# This is generated. Don't modify.
name: dust
description: A more intuitive version of du in rust
source:
  Github:
    owner: bootandy
    repo: dust
targets:
- LinuxAmd64:
    artifact_templates:
    - dust-v{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - dust-v{version}-arm-unknown-linux-gnueabihf.tar.gz
- MacOS:
    artifact_templates:
    - dust-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - dust-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/eksctl.yaml`
```yaml
# This is generated. Don't modify.
name: eksctl
description: The official CLI for Amazon EKS
source:
  Github:
    owner: weaveworks
    repo: eksctl
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/eksctl_Linux_amd64.tar.gz'
- LinuxArm64:
    artifact_templates:
    - '{version}/eksctl_Linux_arm64.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/eksctl_Darwin_amd64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/eksctl_Windows_amd64.zip'
detail: null
```

## File: `generated/packages/epinio.yaml`
```yaml
# This is generated. Don't modify.
name: epinio
description: Opinionated platform that runs on Kubernetes, that takes you from App to URL in one step.
source:
  Github:
    owner: epinio
    repo: epinio
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/epinio-linux-amd64'
- LinuxArm32:
    artifact_templates:
    - '{version}/epinio-linux-arm32'
- LinuxArm64:
    artifact_templates:
    - '{version}/epinio-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/epinio-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/epinio-windows-amd64'
detail: null
```

## File: `generated/packages/exa.yaml`
```yaml
# This is generated. Don't modify.
name: exa
description: A modern replacement for ‘ls’.
source:
  Github:
    owner: ogham
    repo: exa
targets:
- LinuxAmd64:
    artifact_templates:
    - exa-linux-x86_64-{version}.zip
- LinuxArm32:
    artifact_templates:
    - exa-linux-armv7-{version}.zip
- MacOS:
    artifact_templates:
    - exa-macos-x86_64-{version}.zip
detail: null
```

## File: `generated/packages/faas-cli.yaml`
```yaml
# This is generated. Don't modify.
name: faas-cli
description: Official CLI for OpenFaaS
source:
  Github:
    owner: openfaas
    repo: faas-cli
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/faas-cli'
    executable_mappings:
      faas-cli: faas
- LinuxArm64:
    artifact_templates:
    - '{version}/faas-cli-arm64'
    executable_mappings:
      faas-cli: faas
- MacOS:
    artifact_templates:
    - '{version}/faas-cli-darwin'
    executable_mappings:
      faas-cli: faas
- Windows:
    artifact_templates:
    - '{version}/faas-cli.exe'
    executable_mappings:
      faas-cli: faas
detail: null
```

## File: `generated/packages/fd.yaml`
```yaml
# This is generated. Don't modify.
name: fd
description: A simple, fast and user-friendly alternative to 'find'
source:
  Github:
    owner: sharkdp
    repo: fd
targets:
- LinuxAmd64:
    artifact_templates:
    - fd-v{version}-x86_64-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - fd-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - fd-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/firecracker.yaml`
```yaml
# This is generated. Don't modify.
name: firecracker
description: Secure and fast microVMs for serverless computing.
source:
  Github:
    owner: firecracker-microvm
    repo: firecracker
targets:
- LinuxAmd64:
    artifact_templates:
    - Firecracker-v{version}-x86_64.tgz
    - firecracker-v{version}-x86_64.tgz
    scan_dirs:
    - release-v{version}
- LinuxArm64:
    artifact_templates:
    - Firecracker-v{version}-aarch64.tgz
    - firecracker-v{version}-aarch64.tgz
    scan_dirs:
    - release-v{version}
detail: null
```

## File: `generated/packages/fission.yaml`
```yaml
# This is generated. Don't modify.
name: fission
description: Fast and Simple Serverless Functions for Kubernetes
source:
  Github:
    owner: fission
    repo: fission
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/fission-cli-linux'
    - fission-all-{version}.tgz
    executable_mappings:
      fission-cli-linux: fission
- MacOS:
    artifact_templates:
    - '{version}/fission-cli-osx'
    - fission-all-{version}.tgz
    executable_mappings:
      fission-cli-osx: fission
- Windows:
    artifact_templates:
    - '{version}/fission-cli-windows.exe'
    - fission-all-{version}.tgz
    executable_mappings:
      fission-cli-windows.exe: fission.exe
detail: null
```

## File: `generated/packages/fleet.yaml`
```yaml
# This is generated. Don't modify.
name: fleet
description: Deploy workloads from Git to large fleets of Kubernetes clusters
source:
  Github:
    owner: rancher
    repo: fleet
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/fleet-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/fleet-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/fleet-darwin-arm64'
detail: null
```

## File: `generated/packages/flux2.yaml`
```yaml
# This is generated. Don't modify.
name: flux2
description: Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.
source:
  Github:
    owner: fluxcd
    repo: flux2
targets:
- LinuxAmd64:
    artifact_templates:
    - flux_0.3.0_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - flux_0.3.0_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - flux_0.3.0_darwin_amd64.tar.gz
- Windows:
    artifact_templates:
    - flux_0.3.0_windows_amd64.zip
detail: null
```

## File: `generated/packages/fnm.yaml`
```yaml
# This is generated. Don't modify.
name: fnm
description: 🚀 Fast and simple Node.js version manager, built in Rust
source:
  Github:
    owner: Schniz
    repo: fnm
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/fnm-linux.zip'
- LinuxArm64:
    artifact_templates:
    - '{version}/fnm-arm64.zip'
- LinuxArm32:
    artifact_templates:
    - '{version}/fnm-arm64.zip'
- MacOS:
    artifact_templates:
    - '{version}/fnm-macos.zip'
- Windows:
    artifact_templates:
    - '{version}/fnm-windows.zip'
detail: null
```

## File: `generated/packages/fortio.yaml`
```yaml
# This is generated. Don't modify.
name: fortio
description: Fortio load testing library, command line tool, advanced echo server and web UI in go (golang). Allows to specify a set query-per-second load and record latency histograms and other useful stats.
source:
  Github:
    owner: fortio
    repo: fortio
targets:
- LinuxAmd64:
    artifact_templates:
    - fortio-linux_x64-{version}.tgz
- MacOS:
    artifact_templates:
    - fortio-linux_x64-{version}.tgz
- Windows:
    artifact_templates:
    - fortio_win_{version}.zip
detail: null
```

## File: `generated/packages/frum.yaml`
```yaml
# This is generated. Don't modify.
name: frum
description: A little bit fast and modern Ruby version manager written in Rust
source:
  Github:
    owner: TaKO8Ki
    repo: frum
targets:
- LinuxAmd64:
    artifact_templates:
    - frum-v{version}-x86_64-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - frum-v{version}-x86_64-apple-darwin.tar.gz
detail: null
```

## File: `generated/packages/gh.yaml`
```yaml
# This is generated. Don't modify.
name: gh
description: GitHub’s official command line tool
source:
  Github:
    owner: cli
    repo: cli
targets:
- LinuxAmd64:
    artifact_templates:
    - gh_{version}_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - gh_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - gh_{version}_macOS_amd64.tar.gz
detail: null
```

## File: `generated/packages/gitui.yaml`
```yaml
# This is generated. Don't modify.
name: gitui
description: Blazing 💥 fast terminal-ui for git written in rust 🦀
source:
  Github:
    owner: extrawurst
    repo: gitui
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/gitui-linux-musl.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/gitui-mac.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/gitui-win.tar.gz'
detail: null
```

## File: `generated/packages/go-http-tunnel.yaml`
```yaml
# This is generated. Don't modify.
name: go-http-tunnel
description: Fast and secure tunnels over HTTP/2
source:
  Github:
    owner: mmatczuk
    repo: go-http-tunnel
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/tunnel_linux_amd64.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/tunnel_darwin_amd64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/tunnel_windows_amd64.tar.gz'
detail: null
```

## File: `generated/packages/gping.yaml`
```yaml
# This is generated. Don't modify.
name: gping
description: Ping, but with a graph
source:
  Github:
    owner: orf
    repo: gping
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/gping-Linux-x86_64.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/gping-Darwin-x86_64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/gping-Windows-x86_64.tar.gz'
detail: null
```

## File: `generated/packages/gradle.yaml`
```yaml
# This is generated. Don't modify.
name: gradle
description: Adaptable, fast automation for all
source:
  Github:
    owner: gradle
    repo: gradle
targets:
- LinuxAmd64:
    artifact_templates:
    - https://services.gradle.org/distributions/gradle-{version}-bin.zip
- MacOS:
    artifact_templates:
    - https://services.gradle.org/distributions/gradle-{version}-bin.zip
- Windows:
    artifact_templates:
    - https://services.gradle.org/distributions/gradle-{version}-bin.zip
detail: null
```

## File: `generated/packages/grex.yaml`
```yaml
# This is generated. Don't modify.
name: grex
description: A command-line tool and Rust library with Python bindings for generating regular expressions from user-provided test cases
source:
  Github:
    owner: pemistahl
    repo: grex
targets:
- LinuxAmd64:
    artifact_templates:
    - grex-v{version}-x86_64-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - grex-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - grex-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/grpcurl.yaml`
```yaml
# This is generated. Don't modify.
name: grpcurl
description: 'Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers'
source:
  Github:
    owner: fullstorydev
    repo: grpcurl
targets:
- LinuxAmd64:
    artifact_templates:
    - grpcurl_{version}_linux_x86_64.tar.gz
- LinuxArm64:
    artifact_templates:
    - grpcurl_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - grpcurl_{version}_osx_x86_64.tar.gz
- MacOSArm64:
    artifact_templates:
    - grpcurl_{version}_osx_arm64.tar.gz
- Windows:
    artifact_templates:
    - grpcurl_{version}_windows_x86_64.zip
detail: null
```

## File: `generated/packages/helm.yaml`
```yaml
# This is generated. Don't modify.
name: helm
description: The Kubernetes Package Manager
source:
  Github:
    owner: helm
    repo: helm
targets:
- LinuxAmd64:
    artifact_templates:
    - https://get.helm.sh/helm-v{version}-linux-amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - https://get.helm.sh/helm-v{version}-linux-arm64.tar.gz
- MacOS:
    artifact_templates:
    - https://get.helm.sh/helm-v{version}-darwin-amd64.tar.gz
- Windows:
    artifact_templates:
    - https://get.helm.sh/helm-v{version}-windows-amd64.zip
detail: null
```

## File: `generated/packages/helmfile.yaml`
```yaml
# This is generated. Don't modify.
name: helmfile
description: Deploy Kubernetes Helm Charts
source:
  Github:
    owner: roboll
    repo: helmfile
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/helmfile_linux_amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/helmfile_linux_arm64'
- MacOS:
    artifact_templates:
    - '{version}/helmfile_darwin_amd64'
- Windows:
    artifact_templates:
    - '{version}/helmfile_windows_amd64.exe'
detail: null
```

## File: `generated/packages/hetty.yaml`
```yaml
# This is generated. Don't modify.
name: hetty
description: An HTTP toolkit for security research.
source:
  Github:
    owner: dstotijn
    repo: hetty
targets:
- LinuxAmd64:
    artifact_templates:
    - hetty_{version}_Linux_x86_64.tar.gz
- MacOS:
    artifact_templates:
    - hetty_{version}_macOS_x86_64.tar.gz
- Windows:
    artifact_templates:
    - hetty_{version}_Windows_x86_64.zip
detail: null
```

## File: `generated/packages/hexyl.yaml`
```yaml
# This is generated. Don't modify.
name: hexyl
description: A command-line hex viewer
source:
  Github:
    owner: sharkdp
    repo: hexyl
targets:
- LinuxAmd64:
    artifact_templates:
    - hexyl-v{version}-x86_64-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - hexyl-v{version}-x86_64-apple-darwin.tar.gz
detail: null
```

## File: `generated/packages/hub.yaml`
```yaml
# This is generated. Don't modify.
name: hub
description: A command-line tool that makes git easier to use with GitHub.
source:
  Github:
    owner: github
    repo: hub
targets:
- LinuxAmd64:
    artifact_templates:
    - hub-linux-amd64-{version}.tgz
    executable_mappings:
      install: hub-install
- LinuxArm64:
    artifact_templates:
    - hub-linux-arm64-{version}.tgz
- MacOS:
    artifact_templates:
    - hub-darwin-amd64-{version}.tgz
- Windows:
    artifact_templates:
    - hub-windows-amd64-{version}.zip
detail: null
```

## File: `generated/packages/huber.yaml`
```yaml
# This is generated. Don't modify.
name: huber
description: Huber 📦, Package Install Manager for GitHub repos
source:
  Github:
    owner: innobead
    repo: huber
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/huber-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/huber-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/huber-darwin-amd64'
detail: null
```

## File: `generated/packages/hugo.yaml`
```yaml
# This is generated. Don't modify.
name: hugo
description: The world’s fastest framework for building websites.
source:
  Github:
    owner: gohugoio
    repo: hugo
targets:
- LinuxAmd64:
    artifact_templates:
    - hugo_{version}_Linux-64bit.tar.gz
    - hugo_extended_{version}_Linux-64bit.tar.gz
- MacOS:
    artifact_templates:
    - hugo_{version}_macOS-64bit.tar.gz
    - hugo_extended_{version}_macOS-64bit.tar.gz
- Windows:
    artifact_templates:
    - hugo_{version}_Windows-64bit.zip
    - hugo_extended_{version}_Windows-64bit.zip
detail: null
```

## File: `generated/packages/hyperfine.yaml`
```yaml
# This is generated. Don't modify.
name: hyperfine
description: A command-line benchmarking tool
source:
  Github:
    owner: sharkdp
    repo: hyperfine
targets:
- LinuxAmd64:
    artifact_templates:
    - hyperfine-v{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - hyperfine-v{version}-arm-unknown-linux-musleabihf.tar.gz
- MacOS:
    artifact_templates:
    - hyperfine-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - hyperfine-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/hypper.yaml`
```yaml
# This is generated. Don't modify.
name: hypper
description: null
source:
  Github:
    owner: rancher-sandbox
    repo: hypper
targets:
- LinuxAmd64:
    artifact_templates:
    - hypper-v0.2.0-Linux-x86_64.tar.gz
- LinuxArm64:
    artifact_templates:
    - hypper-v0.2.0-Linux-arm64.tar.gz
- LinuxArm32:
    artifact_templates:
    - hypper-v0.2.0-Linux-armv6.tar.gz
- MacOS:
    artifact_templates:
    - hypper-v0.2.0-Darwin-x86_64.tar.gz
- Windows:
    artifact_templates:
    - hypper-v0.2.0-Windows-x86_64.tar.gz
detail: null
```

## File: `generated/packages/ignite.yaml`
```yaml
# This is generated. Don't modify.
name: ignite
description: Ignite a Firecracker microVM
source:
  Github:
    owner: weaveworks
    repo: ignite
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/ignite-amd64'
    - '{version}/ignited-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/ignite-arm64'
    - '{version}/ignited-arm64'
detail: null
```

## File: `generated/packages/img.yaml`
```yaml
# This is generated. Don't modify.
name: img
description: Standalone, daemon-less, unprivileged Dockerfile and OCI compatible container image builder.
source:
  Github:
    owner: genuinetools
    repo: img
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/img-linux-amd64'
detail: null
```

## File: `generated/packages/istio.yaml`
```yaml
# This is generated. Don't modify.
name: istio
description: Connect, secure, control, and observe services.
source:
  Github:
    owner: istio
    repo: istio
targets:
- LinuxAmd64:
    artifact_templates:
    - istio-{version}-linux-amd64.tar.gz
    - istioctl-{version}-linux-amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - istio-{version}-linux-arm64.tar.gz
    - istioctl-{version}-linux-arm64.tar.gz
- MacOS:
    artifact_templates:
    - istio-{version}-osx.tar.gz
    - istioctl-{version}-osx.tar.gz
- Windows:
    artifact_templates:
    - istio-{version}-win.zip
    - istioctl-{version}-win.zip
detail: null
```

## File: `generated/packages/jiq.yaml`
```yaml
# This is generated. Don't modify.
name: jiq
description: jid on jq - interactive JSON query tool using jq expressions
source:
  Github:
    owner: fiatjaf
    repo: jiq
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/jiq_linux_amd64'
- LinuxArm32:
    artifact_templates:
    - '{version}/jiq_linux_arm'
- MacOS:
    artifact_templates:
    - '{version}/jiq_darwin_amd64'
- Windows:
    artifact_templates:
    - '{version}/jiq_windows_amd64.exe'
detail: null
```

## File: `generated/packages/jless.yaml`
```yaml
# This is generated. Don't modify.
name: jless
description: jless is a command-line JSON viewer designed for reading, exploring, and searching through JSON data.
source:
  Github:
    owner: PaulJuliusMartinez
    repo: jless
targets:
- LinuxAmd64:
    artifact_templates:
    - jless-v{version}-x86_64-unknown-linux-gnu.zip
- MacOS:
    artifact_templates:
    - jless-v{version}-x86_64-apple-darwin.zip
detail: null
```

## File: `generated/packages/jq.yaml`
```yaml
# This is generated. Don't modify.
name: jq
description: Command-line JSON processor
source:
  Github:
    owner: stedolan
    repo: jq
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/jq-linux64'
    executable_mappings:
      jq-linux64: jq
- MacOS:
    artifact_templates:
    - '{version}/jq-osx-amd64'
    executable_mappings:
      jq-osx-amd64: jq
- Windows:
    artifact_templates:
    - '{version}/jq-win64.exe'
    executable_mappings:
      jq-win64.exe: jq.exe
detail: null
```

## File: `generated/packages/just.yaml`
```yaml
# This is generated. Don't modify.
name: just
description: 🤖 Just a command runner
source:
  Github:
    owner: casey
    repo: just
targets:
- LinuxAmd64:
    artifact_templates:
    - just-{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - just-{version}-aarch64-unknown-linux-musl.tar.gz
- LinuxArm32:
    artifact_templates:
    - just-{version}-armv7-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - just-{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - just-{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/jwt-cli.yaml`
```yaml
# This is generated. Don't modify.
name: jwt-cli
description: A super fast CLI tool to decode and encode JWTs built in Rust
source:
  Github:
    owner: mike-engel
    repo: jwt-cli
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/jwt-linux.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/jwt-macOS.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/jwt-windows.tar.gz'
detail: null
```

## File: `generated/packages/k0s.yaml`
```yaml
# This is generated. Don't modify.
name: k0s
description: k0s - The Zero Friction Kubernetes
source:
  Github:
    owner: k0sproject
    repo: k0s
targets:
- LinuxAmd64:
    artifact_templates:
    - k0s-v{version}-amd64
- LinuxArm64:
    artifact_templates:
    - k0s-v{version}-arm64
- Windows:
    artifact_templates:
    - k0s-v{version}-amd64.exe
detail: null
```

## File: `generated/packages/k3ai.yaml`
```yaml
# This is generated. Don't modify.
name: k3ai
description: K3ai is a lightweight, fully automated, AI infrastructure-in-a-box solution that allows anyone to experiment quickly with Kubeflow pipelines. K3ai  is perfect for anything from Edge to laptops.
source:
  Github:
    owner: kf5i
    repo: k3ai
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/install'
    executable_mappings:
      install: k3ai-install
detail: null
```

## File: `generated/packages/k3d.yaml`
```yaml
# This is generated. Don't modify.
name: k3d
description: Little helper to run CNCF's k3s in Docker
source:
  Github:
    owner: rancher
    repo: k3d
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/k3d-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/k3d-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/k3d-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/k3d-windows-amd64.exe'
detail: null
```

## File: `generated/packages/k3s.yaml`
```yaml
# This is generated. Don't modify.
name: k3s
description: Lightweight Kubernetes
source:
  Github:
    owner: rancher
    repo: k3s
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/k3s'
- LinuxArm64:
    artifact_templates:
    - '{version}/k3s-arm64'
- LinuxArm32:
    artifact_templates:
    - '{version}/k3s-armhf'
detail: null
```

## File: `generated/packages/k3sup.yaml`
```yaml
# This is generated. Don't modify.
name: k3sup
description: bootstrap K3s over SSH in < 60s 🚀
source:
  Github:
    owner: alexellis
    repo: k3sup
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/k3sup'
- LinuxArm64:
    artifact_templates:
    - '{version}/k3sup-arm64'
- MacOS:
    artifact_templates:
    - '{version}/k3sup-darwin'
- Windows:
    artifact_templates:
    - '{version}/k3sup.exe'
detail: null
```

## File: `generated/packages/k6.yaml`
```yaml
# This is generated. Don't modify.
name: k6
description: A modern load testing tool, using Go and JavaScript - https://k6.io
source:
  Github:
    owner: k6io
    repo: k6
targets:
- LinuxAmd64:
    artifact_templates:
    - k6-v{version}-linux-amd64.tar.gz
    - k6-v{version}-linux64.tar.gz
- LinuxArm64:
    artifact_templates:
    - k6-v{version}-linux-arm64.tar.gz
- MacOS:
    artifact_templates:
    - k6-v{version}-macos-amd64.zip
    - k6-v{version}-mac.zip
- Windows:
    artifact_templates:
    - k6-v{version}-windows-amd64.zip
    - k6-v{version}-win64.zip
detail: null
```

## File: `generated/packages/k9s.yaml`
```yaml
# This is generated. Don't modify.
name: k9s
description: 🐶 Kubernetes CLI To Manage Your Clusters In Style!
source:
  Github:
    owner: derailed
    repo: k9s
targets:
- LinuxAmd64:
    artifact_templates:
    - k9s_Linux_amd64.tar.gz
    - k9s_v{version}_Linux_x86_64.tar.gz
    - '{version}/k9s_Linux_x86_64.tar.gz'
- LinuxArm64:
    artifact_templates:
    - k9s_Linux_arm64.tar.gz
    - k9s_v{version}_Linux_arm64.tar.gz
    - '{version}/k9s_Linux_arm64.tar.gz'
- LinuxArm32:
    artifact_templates:
    - k9s_Linux_arm.tar.gz
- MacOS:
    artifact_templates:
    - k9s_Darwin_amd64.tar.gz
    - k9s_v{version}_Darwin_x86_64.tar.gz
    - '{version}/k9s_Darwin_x86_64.tar.gz'
- MacOSArm64:
    artifact_templates:
    - k9s_Darwin_arm64.tar.gz
- Windows:
    artifact_templates:
    - k9s_Windows_amd64.tar.gz
    - k9s_v{version}_Windows_x86_64.tar.gz
    - '{version}/k9s_Windows_x86_64.tar.gz'
- WindowsArm:
    artifact_templates:
    - k9s_Windows_arm.tar.gz
    - k9s_v{version}_Windows_x86_64.tar.gz
    - '{version}/k9s_Windows_x86_64.tar.gz'
detail: null
```

## File: `generated/packages/keptn.yaml`
```yaml
# This is generated. Don't modify.
name: keptn
description: Cloud-native application life-cycle orchestration. Keptn automates your SLO-driven multi-stage delivery and operations & remediation of your applications.
source:
  Github:
    owner: keptn
    repo: keptn
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}_keptn-linux.tar'
- MacOS:
    artifact_templates:
    - '{version}_keptn-macOS.tar'
- Windows:
    artifact_templates:
    - '{version}_keptn-windows.tar'
detail: null
```

## File: `generated/packages/ketch.yaml`
```yaml
# This is generated. Don't modify.
name: ketch
description: Ketch is an application delivery framework that facilitates the deployment and management of applications on Kubernetes using a simple command line interface
source:
  Github:
    owner: shipa-corp
    repo: ketch
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/ketch-linux-amd64'
- MacOS:
    artifact_templates:
    - '{version}/ketch-darwin-amd64'
detail: null
```

## File: `generated/packages/kind.yaml`
```yaml
# This is generated. Don't modify.
name: kind
description: Kubernetes IN Docker - local clusters for testing Kubernetes
source:
  Github:
    owner: kubernetes-sigs
    repo: kind
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/kind-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/kind-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/kind-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/kind-windows-amd64'
detail: null
```

## File: `generated/packages/ko.yaml`
```yaml
# This is generated. Don't modify.
name: ko
description: Build and deploy Go applications
source:
  Github:
    owner: google
    repo: ko
targets:
- LinuxAmd64:
    artifact_templates:
    - ko_{version}_Linux_x86_64.tar.gz
- MacOS:
    artifact_templates:
    - ko_{version}_Darwin_x86_64.tar.gz
detail: null
```

## File: `generated/packages/kompose.yaml`
```yaml
# This is generated. Don't modify.
name: kompose
description: Convert Compose to Kubernetes
source:
  Github:
    owner: kubernetes
    repo: kompose
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/kompose-linux-arm64'
- LinuxArm64:
    artifact_templates:
    - '{version}/kompose-linux-amd64'
- MacOS:
    artifact_templates:
    - '{version}/kompose-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/kompose-windows-amd64.exe'
detail: null
```

## File: `generated/packages/kotlin.yaml`
```yaml
# This is generated. Don't modify.
name: kotlin
description: 'The Kotlin Programming Language. '
source:
  Github:
    owner: JetBrains
    repo: kotlin
targets:
- LinuxAmd64:
    artifact_templates:
    - kotlin-compiler-{version}.zip
- MacOS:
    artifact_templates:
    - kotlin-compiler-{version}.zip
- Windows:
    artifact_templates:
    - kotlin-compiler-{version}.zip
detail: null
```

## File: `generated/packages/kpt.yaml`
```yaml
# This is generated. Don't modify.
name: kpt
description: Automate Kubernetes Configuration Editing
source:
  Github:
    owner: GoogleContainerTools
    repo: kpt
targets:
- LinuxAmd64:
    artifact_templates:
    - kpt_linux_amd64-{version}.tar.gz
- MacOS:
    artifact_templates:
    - kpt_darwin_amd64-{version}.tar.gz
- Windows:
    artifact_templates:
    - kpt_windows_amd64-{version}.tar.gz
detail: null
```

## File: `generated/packages/krew.yaml`
```yaml
# This is generated. Don't modify.
name: krew
description: 📦 Find and install kubectl plugins
source:
  Github:
    owner: kubernetes-sigs
    repo: krew
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/krew-linux_amd64.tar.gz'
- LinuxArm64:
    artifact_templates:
    - '{version}/krew-linux_arm64.tar.gz'
- LinuxArm32:
    artifact_templates:
    - '{version}/krew-linux_arm.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/krew-darwin_amd64.tar.gz'
- MacOSArm64:
    artifact_templates:
    - '{version}/krew-darwin_arm64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/krew-windows_amd64.tar.gz'
detail: null
```

## File: `generated/packages/krustlet.yaml`
```yaml
# This is generated. Don't modify.
name: krustlet
description: Kubernetes Rust Kubelet
source:
  Github:
    owner: deislabs
    repo: krustlet
targets:
- LinuxAmd64:
    artifact_templates:
    - https://krustlet.blob.core.windows.net/releases/krustlet-v{version}-linux-amd64.tar.gz
- MacOS:
    artifact_templates:
    - https://krustlet.blob.core.windows.net/releases/krustlet-v{version}-macos-amd64.tar.gz
- Windows:
    artifact_templates:
    - https://krustlet.blob.core.windows.net/releases/krustlet-v{version}-windows-amd64.tar.gz
detail: null
```

## File: `generated/packages/kube-bench.yaml`
```yaml
# This is generated. Don't modify.
name: kube-bench
description: Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
source:
  Github:
    owner: aquasecurity
    repo: kube-bench
targets:
- LinuxAmd64:
    artifact_templates:
    - kube-bench_{version}_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - kube-bench_{version}_linux_arm64.tar.gz
detail: null
```

## File: `generated/packages/kube-linter.yaml`
```yaml
# This is generated. Don't modify.
name: kube-linter
description: KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
source:
  Github:
    owner: stackrox
    repo: kube-linter
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/kube-linter-linux.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/kube-linter-darwin.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/kube-linter-windows.tar.gz'
detail: null
```

## File: `generated/packages/kubectl.yaml`
```yaml
# This is generated. Don't modify.
name: kubectl
description: Production-Grade Container Scheduling and Management
source:
  Github:
    owner: kubernetes
    repo: kubernetes
targets:
- LinuxAmd64:
    artifact_templates:
    - https://storage.googleapis.com/kubernetes-release/release/v{version}/bin/linux/amd64/kubectl
- LinuxArm64:
    artifact_templates:
    - https://storage.googleapis.com/kubernetes-release/release/v{version}/bin/linux/arm64/kubectl
- MacOS:
    artifact_templates:
    - https://storage.googleapis.com/kubernetes-release/release/v{version}/bin/darwin/amd64/kubectl2
- MacOSArm64:
    artifact_templates:
    - https://storage.googleapis.com/kubernetes-release/release/v{version}/bin/darwin/arm64/kubectl
- Windows:
    artifact_templates:
    - https://storage.googleapis.com/kubernetes-release/release/v{version}/bin/windows/amd64/kubectl.exe
detail: null
```

## File: `generated/packages/kubefire.yaml`
```yaml
# This is generated. Don't modify.
name: kubefire
description: KubeFire 🔥, creates and manages Kubernetes Clusters using Firecracker microVMs
source:
  Github:
    owner: innobead
    repo: kubefire
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/kubefire-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/kubefire-linux-arm64'
detail: null
```

## File: `generated/packages/kubestr.yaml`
```yaml
# This is generated. Don't modify.
name: kubestr
description: null
source:
  Github:
    owner: kastenhq
    repo: kubestr
targets:
- LinuxAmd64:
    artifact_templates:
    - kubestr-v{version}-linux-amd64.tar.gz
- MacOS:
    artifact_templates:
    - kubestr-v{version}-darwin-amd64.tar.gz
- Windows:
    artifact_templates:
    - kubestr-v{version}-windows-amd64.zip
detail: null
```

## File: `generated/packages/kubevirt.yaml`
```yaml
# This is generated. Don't modify.
name: kubevirt
description: Kubernetes Virtualization API and runtime in order to define and manage virtual machines.
source:
  Github:
    owner: kubevirt
    repo: kubevirt
targets:
- LinuxAmd64:
    artifact_templates:
    - virtctl-v{version}-linux-amd64
- MacOS:
    artifact_templates:
    - virtctl-v{version}-darwin-amd64
- Windows:
    artifact_templates:
    - virtctl-v{version}-windows-amd64.exe
detail: null
```

## File: `generated/packages/kudo.yaml`
```yaml
# This is generated. Don't modify.
name: kudo
description: Kubernetes Universal Declarative Operator (KUDO)
source:
  Github:
    owner: kudobuilder
    repo: kudo
targets:
- LinuxAmd64:
    artifact_templates:
    - kudo_{version}_linux_x86_64.tar.gz
- LinuxArm64:
    artifact_templates:
    - kudo_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - kudo_{version}_darwin_x86_64.tar.gz
detail: null
```

## File: `generated/packages/kustomize.yaml`
```yaml
# This is generated. Don't modify.
name: kustomize
description: Customization of kubernetes YAML configurations
source:
  Github:
    owner: kubernetes-sigs
    repo: kustomize
targets:
- LinuxAmd64:
    artifact_templates:
    - kustomize_v{version}_linux_amd64.tar.gz
    tag_version_regex_template: ^kustomize/(v\d+.\d+.\d+)$
- LinuxArm64:
    artifact_templates:
    - kustomize_v{version}_linux_arm64.tar.gz
    tag_version_regex_template: ^kustomize/(v\d+.\d+.\d+)$
- MacOS:
    artifact_templates:
    - kustomize_v{version}_darwin_amd64.tar.gz
    tag_version_regex_template: ^kustomize/(v\d+.\d+.\d+)$
- Windows:
    artifact_templates:
    - kustomize_v{version}_windows_amd64.tar.gz
    tag_version_regex_template: ^kustomize/(v\d+.\d+.\d+)$
detail: null
```

## File: `generated/packages/kuttl.yaml`
```yaml
# This is generated. Don't modify.
name: kuttl
description: KUbernetes Test TooL (kuttl)
source:
  Github:
    owner: kudobuilder
    repo: kuttl
targets:
- LinuxAmd64:
    artifact_templates:
    - kuttl_{version}_linux_x86_64.tar.gz
- LinuxArm64:
    artifact_templates:
    - kuttl_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - kuttl_{version}_darwin_x86_64.tar.gz
detail: null
```

## File: `generated/packages/kwctl.yaml`
```yaml
# This is generated. Don't modify.
name: kwctl
description: Go-to CLI tool for Kubewarden users
source:
  Github:
    owner: kubewarden
    repo: kwctl
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/kwctl-linux-amd64.zip'
detail: null
```

## File: `generated/packages/lens.yaml`
```yaml
# This is generated. Don't modify.
name: lens
description: Lens - The way the world runs Kubernetes
source:
  Github:
    owner: lensapp
    repo: lens
targets:
- LinuxAmd64:
    artifact_templates:
    - Lens-{version}.AppImage
- MacOS:
    artifact_templates:
    - Lens-{version}.dmg
- Windows:
    artifact_templates:
    - Lens-Setup-{version}.exe
detail: null
```

## File: `generated/packages/linkerd2-edge.yaml`
```yaml
# This is generated. Don't modify.
name: linkerd2-edge
description: Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x.
source:
  Github:
    owner: linkerd
    repo: linkerd2
targets:
- LinuxAmd64:
    artifact_templates:
    - linkerd2-cli-edge-{version}-linux-amd64
    executable_mappings:
      linkerd2-cli-edge-{version}-linux-amd64: linkerd2-edge
    tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
- LinuxArm64:
    artifact_templates:
    - linkerd2-cli-edge-{version}-linux-arm64
    executable_mappings:
      linkerd2-cli-edge-{version}-linux-arm64: linkerd2-edge
    tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
- MacOS:
    artifact_templates:
    - linkerd2-cli-edge-{version}-darwin
    executable_mappings:
      linkerd2-cli-edge-{version}-darwin: linkerd2-edge
    tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
- Windows:
    artifact_templates:
    - linkerd2-cli-edge-{version}-windows.exe
    executable_mappings:
      linkerd2-cli-edge-{version}-windows.exe: linkerd2-edge.exe
    tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
detail: null
```

## File: `generated/packages/linkerd2-stable.yaml`
```yaml
# This is generated. Don't modify.
name: linkerd2-stable
description: Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x.
source:
  Github:
    owner: linkerd
    repo: linkerd2
targets:
- LinuxAmd64:
    artifact_templates:
    - linkerd2-cli-stable-{version}-linux-amd64
    executable_mappings:
      linkerd2-cli-stable-{version}-linux-amd64: linkerd2-stable
    tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
- LinuxArm64:
    artifact_templates:
    - linkerd2-cli-stable-{version}-linux-arm64
    executable_mappings:
      linkerd2-cli-stable-{version}-linux-arm64: linkerd2-stable
    tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
- MacOS:
    artifact_templates:
    - linkerd2-cli-stable-{version}-darwin
    executable_mappings:
      linkerd2-cli-stable-{version}-darwin: linkerd2-stable
    tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
- Windows:
    artifact_templates:
    - linkerd2-cli-stable-{version}-windows.exe
    executable_mappings:
      linkerd2-cli-stable-{version}-windows.exe: linkerd2-stable.exe
    tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
detail: null
```

## File: `generated/packages/loc.yaml`
```yaml
# This is generated. Don't modify.
name: loc
description: Count lines of code quickly.
source:
  Github:
    owner: cgag
    repo: loc
targets:
- LinuxAmd64:
    artifact_templates:
    - trust-v{version}-x86_64-unknown-linux-gnu.tar.gz
- LinuxArm64:
    artifact_templates:
    - trust-v{version}-aarch64-unknown-linux-gnu.tar.gz
- LinuxArm32:
    artifact_templates:
    - trust-v{version}-armv7-unknown-linux-gnueabihf.tar.gz
- MacOS:
    artifact_templates:
    - trust-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - trust-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/lsd.yaml`
```yaml
# This is generated. Don't modify.
name: lsd
description: The next gen ls command
source:
  Github:
    owner: lsd-rs
    repo: lsd
targets:
- LinuxAmd64:
    artifact_templates:
    - lsd-v{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - lsd-v{version}-aarch64-unknown-linux-musl.tar.gz
- LinuxArm32:
    artifact_templates:
    - lsd-v{version}-arm-unknown-linux-gnueabihf.tar.gz
- MacOS:
    artifact_templates:
    - lsd-v{version}-x86_64-apple-darwin.tar.gz
- MacOSArm64:
    artifact_templates:
    - lsd-v{version}-aarch64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - lsd-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/minikube.yaml`
```yaml
# This is generated. Don't modify.
name: minikube
description: Run Kubernetes locally
source:
  Github:
    owner: kubernetes
    repo: minikube
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/minikube-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/minikube-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/minikube-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/minikube-windows-amd64'
detail: null
```

## File: `generated/packages/mkcert.yaml`
```yaml
# This is generated. Don't modify.
name: mkcert
description: A simple zero-config tool to make locally trusted development certificates with any names you'd like.
source:
  Github:
    owner: FiloSottile
    repo: mkcert
targets:
- LinuxAmd64:
    artifact_templates:
    - mkcert-v{version}-linux-amd64
- LinuxArm64:
    artifact_templates:
    - mkcert-v{version}-linux-arm64
- MacOS:
    artifact_templates:
    - mkcert-v{version}-darwin-amd64
- Windows:
    artifact_templates:
    - mkcert-v{version}-windows-amd64.exe
detail: null
```

## File: `generated/packages/nat.yaml`
```yaml
# This is generated. Don't modify.
name: nat
description: '`ls` alternative with useful info and a splash of color 🎨'
source:
  Github:
    owner: willdoescode
    repo: nat
targets:
- MacOS:
    artifact_templates:
    - '{version}/natls_osx_binary'
detail: null
```

## File: `generated/packages/natscli.yaml`
```yaml
# This is generated. Don't modify.
name: natscli
description: The NATS Command Line Interface
source:
  Github:
    owner: nats-io
    repo: natscli
targets:
- LinuxAmd64:
    artifact_templates:
    - nats-{version}-linux-amd64.zip
- LinuxAmd64:
    artifact_templates:
    - nats-{version}-linux-arm64.zip
- LinuxArm32:
    artifact_templates:
    - nats-{version}-linux-arm7.zip
- MacOS:
    artifact_templates:
    - nats-{version}-darwin-amd64.zip
- Windows:
    artifact_templates:
    - nats-{version}-windows-amd64.zip
detail: null
```

## File: `generated/packages/navi.yaml`
```yaml
# This is generated. Don't modify.
name: navi
description: An interactive cheatsheet tool for the command-line
source:
  Github:
    owner: denisidoro
    repo: navi
targets:
- LinuxAmd64:
    artifact_templates:
    - navi-v{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxAmd64:
    artifact_templates:
    - navi-v{version}-aarch64-linux-android.tar.gz
- LinuxArm32:
    artifact_templates:
    - navi-v{version}-armv7-unknown-linux-musleabihf.tar.gz
- MacOS:
    artifact_templates:
    - navi-v{version}-x86_64-apple-darwin.tar.gz
- MacOSArm64:
    artifact_templates:
    - navi-v{version}-aarch64-apple-ios.tar.gz
- Windows:
    artifact_templates:
    - navi-v{version}-x86_64-pc-windows-gnu.zip
detail: null
```

## File: `generated/packages/nerdctl.yaml`
```yaml
# This is generated. Don't modify.
name: nerdctl
description: contaiNERD CTL - Docker-compatible CLI for containerd, with support for Compose, Rootless, eStargz, OCIcrypt, IPFS, ...
source:
  Github:
    owner: containerd
    repo: nerdctl
targets:
- LinuxAmd64:
    artifact_templates:
    - nerdctl-{version}-linux-amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - nerdctl-{version}-linux-arm64.tar.gz
- LinuxArm32:
    artifact_templates:
    - nerdctl-{version}-linux-arm-v7.tar.gz
detail: null
```

## File: `generated/packages/node.yaml`
```yaml
# This is generated. Don't modify.
name: node
description: Node.js JavaScript runtime ✨🐢🚀✨
source:
  Github:
    owner: nodejs
    repo: node
targets:
- LinuxAmd64:
    artifact_templates:
    - https://nodejs.org/dist/v{version}/node-v{version}-linux-x64.tar.xz
- LinuxArm64:
    artifact_templates:
    - https://nodejs.org/dist/v{version}/node-v{version}-linux-arm64.tar.xz
- LinuxArm32:
    artifact_templates:
    - https://nodejs.org/dist/v{version}/node-v{version}-linux-armv7l.tar.xz
- MacOS:
    artifact_templates:
    - https://nodejs.org/dist/v{version}/node-v{version}-darwin-x64.tar.gz
- MacOSArm64:
    artifact_templates:
    - https://nodejs.org/dist/v{version}/node-v{version}-darwin-arm64.tar.gz
- Windows:
    artifact_templates:
    - https://nodejs.org/dist/v{version}/node-v{version}-win-x64.zip
detail: null
```

## File: `generated/packages/nomad.yaml`
```yaml
# This is generated. Don't modify.
name: nomad
description: Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations.
source:
  Github:
    owner: hashicorp
    repo: nomad
targets:
- LinuxAmd64:
    artifact_templates:
    - https://releases.hashicorp.com/nomad/{version}/nomad_{version}_linux_amd64.zip
- LinuxArm64:
    artifact_templates:
    - https://releases.hashicorp.com/packer/{version}/nomad_{version}_linux_arm64.zip
- MacOS:
    artifact_templates:
    - https://releases.hashicorp.com/nomad/{version}/nomad_{version}_darwin_amd64.zip
- Windows:
    artifact_templates:
    - https://releases.hashicorp.com/nomad/{version}/nomad_{version}_windows_amd64.zip
detail: null
```

## File: `generated/packages/norouter.yaml`
```yaml
# This is generated. Don't modify.
name: norouter
description: 'NoRouter: IP-over-Stdio. The easiest multi-host & multi-cloud networking ever. No root privilege is required. '
source:
  Github:
    owner: norouter
    repo: norouter
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/norouter-Linux-x86_64.tgz'
- LinuxArm64:
    artifact_templates:
    - '{version}/norouter-Linux-aarch64.tgz'
- MacOS:
    artifact_templates:
    - '{version}/norouter-Darwin-x86_64.tgz'
- Windows:
    artifact_templates:
    - '{version}/norouter-Windows-x64.zip'
detail: null
```

## File: `generated/packages/nushell.yaml`
```yaml
# This is generated. Don't modify.
name: nushell
description: A new type of shell
source:
  Github:
    owner: nushell
    repo: nushell
targets:
- LinuxAmd64:
    artifact_templates:
    - nu_{version:_}_linux.tar.gz
    scan_dirs:
    - nushell-{version}
- MacOS:
    artifact_templates:
    - nu_{version:_}_macOS.zip
    scan_dirs:
    - nushell-{version}
- Windows:
    artifact_templates:
    - nu_{version:_}_windows.zip
    scan_dirs:
    - nushell-{version}
detail: null
```

## File: `generated/packages/octant.yaml`
```yaml
# This is generated. Don't modify.
name: octant
description: Highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
source:
  Github:
    owner: vmware-tanzu
    repo: octant
targets:
- LinuxAmd64:
    artifact_templates:
    - octant_{version}_Linux-64bit.tar.gz
- LinuxArm64:
    artifact_templates:
    - octant_{version}_Linux-arm64.tar.gz
- MacOS:
    artifact_templates:
    - octant_{version}_macOS-64bit.tar.gz
- Windows:
    artifact_templates:
    - octant_{version}_Windows-64bit.tar.gz
detail: null
```

## File: `generated/packages/okteto.yaml`
```yaml
# This is generated. Don't modify.
name: okteto
description: Develop your applications directly in your Kubernetes Cluster
source:
  Github:
    owner: okteto
    repo: okteto
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/okteto-Linux-x86_64'
- LinuxArm64:
    artifact_templates:
    - '{version}/okteto-Linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/okteto-Darwin-x86_64'
- Windows:
    artifact_templates:
    - '{version}/okteto.exe'
detail: null
```

## File: `generated/packages/onefetch.yaml`
```yaml
# This is generated. Don't modify.
name: onefetch
description: Command-line Git information tool
source:
  Github:
    owner: o2sh
    repo: onefetch
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/onefetch-linux.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/onefetch-mac.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/onefetch-win.tar.gz'
detail: null
```

## File: `generated/packages/opa.yaml`
```yaml
# This is generated. Don't modify.
name: opa
description: Open Policy Agent (OPA) is an open source, general-purpose policy engine.
source:
  Github:
    owner: open-policy-agent
    repo: opa
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/opa_linux_amd64'
- MacOS:
    artifact_templates:
    - '{version}/opa_darwin_amd64'
- Windows:
    artifact_templates:
    - '{version}/opa_windows_amd64.exe'
detail: null
```

## File: `generated/packages/opni.yaml`
```yaml
# This is generated. Don't modify.
name: opni
description: Multi Cluster Observability with AIOps
source:
  Github:
    owner: rancher
    repo: opni
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/opnictl'
- MacOS:
    artifact_templates:
    - '{version}/opnictl-darwin'
- Windows:
    artifact_templates:
    - '{version}/opnictl-windows'
detail: null
```

## File: `generated/packages/oras.yaml`
```yaml
# This is generated. Don't modify.
name: oras
description: OCI registry client - managing content like artifacts, images, packages
source:
  Github:
    owner: deislabs
    repo: oras
targets:
- LinuxAmd64:
    artifact_templates:
    - oras_{version}_linux_amd64.tar.gz
- MacOS:
    artifact_templates:
    - oras_{version}_darwin_amd64.tar.gz
- Windows:
    artifact_templates:
    - oras_{version}_windows_amd64.tar.gz
detail: null
```

## File: `generated/packages/pack.yaml`
```yaml
# This is generated. Don't modify.
name: pack
description: CLI for building apps using Cloud Native Buildpacks
source:
  Github:
    owner: buildpacks
    repo: pack
targets:
- LinuxAmd64:
    artifact_templates:
    - pack-v{version}-linux.tgz
- MacOS:
    artifact_templates:
    - pack-v{version}-macos.tgz
- Windows:
    artifact_templates:
    - pack-v{version}-windows.zip
detail: null
```

## File: `generated/packages/packer.yaml`
```yaml
# This is generated. Don't modify.
name: packer
description: Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
source:
  Github:
    owner: hashicorp
    repo: packer
targets:
- LinuxAmd64:
    artifact_templates:
    - https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_amd64.zip
- LinuxArm64:
    artifact_templates:
    - https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_arm64.zip
- MacOS:
    artifact_templates:
    - https://releases.hashicorp.com/packer/{version}/packer_{version}_darwin_amd64.zip
- Windows:
    artifact_templates:
    - https://releases.hashicorp.com/packer/{version}/packer_{version}_windows_amd64.zip
detail: null
```

## File: `generated/packages/podman.yaml`
```yaml
# This is generated. Don't modify.
name: podman
description: 'Podman: A tool for managing OCI containers and pods.'
source:
  Github:
    owner: containers
    repo: podman
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/podman-remote-static.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/podman-remote-release-darwin.zip'
- Windows:
    artifact_templates:
    - '{version}/podman-remote-release-windows.zip'
detail: null
```

## File: `generated/packages/powershell.yaml`
```yaml
# This is generated. Don't modify.
name: powershell
description: PowerShell for every system!
source:
  Github:
    owner: PowerShell
    repo: PowerShell
targets:
- LinuxAmd64:
    artifact_templates:
    - powershell-{version}-linux-x64.tar.gz
- MacOS:
    artifact_templates:
    - powershell-{version}-osx-x64.tar.gz
detail: null
```

## File: `generated/packages/procs.yaml`
```yaml
# This is generated. Don't modify.
name: procs
description: A modern replacement for ps written in Rust
source:
  Github:
    owner: dalance
    repo: procs
targets:
- LinuxAmd64:
    artifact_templates:
    - procs-v{version}-x86_64-lnx.zip
- MacOS:
    artifact_templates:
    - procs-v{version}-x86_64-mac.zip
- Windows:
    artifact_templates:
    - procs-v{version}-x86_64-win.zip
detail: null
```

## File: `generated/packages/protoc.yaml`
```yaml
# This is generated. Don't modify.
name: protoc
description: Protocol Buffers - Google's data interchange format
source:
  Github:
    owner: protocolbuffers
    repo: protobuf
targets:
- LinuxAmd64:
    artifact_templates:
    - protoc-{version}-linux-x86_64.zip
- LinuxArm64:
    artifact_templates:
    - protoc-{version}-linux-aarch_64.zip
- MacOS:
    artifact_templates:
    - protoc-{version}-osx-x86_64.zip
- Windows:
    artifact_templates:
    - protoc-{version}-win64.zip
detail: null
```

## File: `generated/packages/pueue.yaml`
```yaml
# This is generated. Don't modify.
name: pueue
description: ':stars: Manage your shell commands.'
source:
  Github:
    owner: Nukesor
    repo: pueue
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/pueue-linux-x86_64'
    - '{version}/pueued-linux-x86_64'
- LinuxArm64:
    artifact_templates:
    - '{version}/pueue-linux-aarch64'
    - '{version}/pueued-linux-aarch64'
- LinuxArm32:
    artifact_templates:
    - '{version}/pueue-linux-armv7'
    - '{version}/pueued-linux-armv7'
- MacOS:
    artifact_templates:
    - '{version}/pueue-macos-x86_64'
    - '{version}/pueued-macos-x86_64'
- Windows:
    artifact_templates:
    - '{version}/pueue-windows-x86_64.exe'
    - '{version}/pueued-windows-x86_64.exe'
detail: null
```

## File: `generated/packages/pulumi.yaml`
```yaml
# This is generated. Don't modify.
name: pulumi
description: Pulumi - Infrastructure as Code in any programming language. Build infrastructure intuitively on any cloud using familiar languages 🚀
source:
  Github:
    owner: pulumi
    repo: pulumi
targets:
- LinuxAmd64:
    artifact_templates:
    - https://get.pulumi.com/releases/sdk/pulumi-v{version}-linux-x64.tar.gz
- MacOS:
    artifact_templates:
    - https://get.pulumi.com/releases/sdk/pulumi-v{version}-darwin-x64.tar.gz
- Windows:
    artifact_templates:
    - https://get.pulumi.com/releases/sdk/pulumi-v{version}-windows-x64.zip
detail: null
```

## File: `generated/packages/rancher-cli.yaml`
```yaml
# This is generated. Don't modify.
name: rancher-cli
description: Rancher CLI
source:
  Github:
    owner: rancher
    repo: cli
targets:
- LinuxAmd64:
    artifact_templates:
    - rancher-linux-amd64-v{version}.tar.gz
- MacOS:
    artifact_templates:
    - rancher-darwin-amd64-v{version}.tar.gz
- Windows:
    artifact_templates:
    - rancher-windows-amd64-v{version}.zip
detail: null
```

## File: `generated/packages/rancher.yaml`
```yaml
# This is generated. Don't modify.
name: rancher
description: Complete container management platform
source:
  Github:
    owner: rancher
    repo: rancher
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/rancherd-amd64.tar.gz'
detail: null
```

## File: `generated/packages/renote.yaml`
```yaml
# This is generated. Don't modify.
name: renote
description: Renote is to extend GitHub operation experience, which is a complementary tool to use with gh
source:
  Github:
    owner: ecatlabs
    repo: renote
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/renote-linux-amd64'
- MacOS:
    artifact_templates:
    - '{version}/renote-darwin-amd64'
detail: null
```

## File: `generated/packages/rio.yaml`
```yaml
# This is generated. Don't modify.
name: rio
description: Application Deployment Engine for Kubernetes
source:
  Github:
    owner: rancher
    repo: rio
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/rio-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/rio-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/rio-darwin-amd64'
detail: null
```

## File: `generated/packages/ripgrep.yaml`
```yaml
# This is generated. Don't modify.
name: ripgrep
description: ripgrep recursively searches directories for a regex pattern while respecting your gitignore
source:
  Github:
    owner: BurntSushi
    repo: ripgrep
targets:
- LinuxAmd64:
    artifact_templates:
    - ripgrep-{version}-x86_64-unknown-linux-musl.tar.gz
- MacOS:
    artifact_templates:
    - ripgrep-{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - ripgrep-{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/rke.yaml`
```yaml
# This is generated. Don't modify.
name: rke
description: Rancher Kubernetes Engine (RKE), an extremely simple, lightning fast Kubernetes distribution that runs entirely within containers.
source:
  Github:
    owner: rancher
    repo: rke
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/rke_linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/rke_linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/rke_darwin-amd64'
detail: null
```

## File: `generated/packages/rke2.yaml`
```yaml
# This is generated. Don't modify.
name: rke2
description: null
source:
  Github:
    owner: rancher
    repo: rke2
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/rke2.linux-amd64'
detail: null
```

## File: `generated/packages/rustwasmc.yaml`
```yaml
# This is generated. Don't modify.
name: rustwasmc
description: Tool for building Rust functions for Node.js. Combine the performance of Rust, safety and portability of WebAssembly, and ease of use of JavaScript.
source:
  Github:
    owner: second-state
    repo: rustwasmc
targets:
- LinuxAmd64:
    artifact_templates:
    - rustwasmc-v{version}-x86_64-unknown-linux-gnu.tar.gz
    - ssvmup-v{version}-x86_64-unknown-linux-gnu.tar.gz
- LinuxArm64:
    artifact_templates:
    - rustwasmc-v{version}-aarch64-unknown-linux-gnu.tar.gz
    - ssvmup-v{version}-aarch64-unknown-linux-gnu.tar.gz
- MacOS:
    artifact_templates:
    - rustwasmc-v{version}-x86_64-apple-darwin.tar.gz
    - ssvmup-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - rustwasmc-v{version}-x86_64-pc-windows-msvc.tar.gz
    - ssvmup-v{version}-x86_64-pc-windows-msvc.tar.gz
detail: null
```

## File: `generated/packages/sad.yaml`
```yaml
# This is generated. Don't modify.
name: sad
description: CLI search and replace | Space Age seD
source:
  Github:
    owner: ms-jpq
    repo: sad
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/x86_64-unknown-linux-gnu.zip'
- MacOS:
    artifact_templates:
    - '{version}/x86_64-apple-darwin.zip'
detail: null
```

## File: `generated/packages/saml2aws.yaml`
```yaml
# This is generated. Don't modify.
name: saml2aws
description: CLI tool which enables you to login and retrieve AWS temporary credentials using a SAML IDP
source:
  Github:
    owner: Versent
    repo: saml2aws
targets:
- LinuxAmd64:
    artifact_templates:
    - saml2aws_{version}_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - saml2aws_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - saml2aws_{version}_darwin_amd64.tar.gz
- MacOSArm64:
    artifact_templates:
    - saml2aws_{version}_darwin_arm64.tar.gz
- Windows:
    artifact_templates:
    - saml2aws_{version}_windows_amd64.zip
- WindowsArm64:
    artifact_templates:
    - saml2aws_{version}_windows_arm64.zip
detail: null
```

## File: `generated/packages/sd.yaml`
```yaml
# This is generated. Don't modify.
name: sd
description: Intuitive find & replace CLI (sed alternative)
source:
  Github:
    owner: chmln
    repo: sd
targets:
- LinuxAmd64:
    artifact_templates:
    - sd-v{version}-x86_64-unknown-linux-musl
- MacOS:
    artifact_templates:
    - sd-v{version}-x86_64-apple-darwin
detail: null
```

## File: `generated/packages/shadowsocks.yaml`
```yaml
# This is generated. Don't modify.
name: shadowsocks
description: A Rust port of shadowsocks
source:
  Github:
    owner: shadowsocks
    repo: shadowsocks-rust
targets:
- LinuxAmd64:
    artifact_templates:
    - shadowsocks-v{version}.x86_64-unknown-linux-musl.tar.xz
- LinuxArm64:
    artifact_templates:
    - shadowsocks-v{version}.aarch64-unknown-linux-gnu.tar.xz
- MacOS:
    artifact_templates:
    - shadowsocks-v{version}.x86_64-apple-darwin.tar.xz
- Windows:
    artifact_templates:
    - shadowsocks-v{version}.x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/shisho.yaml`
```yaml
# This is generated. Don't modify.
name: shisho
description: Lightweight static analyzer for several programming languages
source:
  Github:
    owner: flatt-security
    repo: shisho
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/build-x86_64-unknown-linux-gnu.zip'
- MacOS:
    artifact_templates:
    - '{version}/build-x86_64-apple-darwin.zip'
- Windows:
    artifact_templates:
    - '{version}/build-x86_64-pc-windows.zip'
detail: null
```

## File: `generated/packages/skaffold.yaml`
```yaml
# This is generated. Don't modify.
name: skaffold
description: Easy and Repeatable Kubernetes Development
source:
  Github:
    owner: GoogleContainerTools
    repo: skaffold
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/skaffold-linux-amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/skaffold-linux-arm64'
- MacOS:
    artifact_templates:
    - '{version}/skaffold-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/skaffold-windows-amd64.exe'
detail: null
```

## File: `generated/packages/skim.yaml`
```yaml
# This is generated. Don't modify.
name: skim
description: Fuzzy Finder in rust!
source:
  Github:
    owner: lotabout
    repo: skim
targets:
- LinuxAmd64:
    artifact_templates:
    - skim-v{version}-x86_64-unknown-linux-musl.tar.gz
- LinuxArm64:
    artifact_templates:
    - skim-v{version}-armv7-unknown-linux-gnueabihf.tar.gz
- LinuxArm32:
    artifact_templates:
    - skim-v{version}-arm-unknown-linux-gnueabihf.tar.gz
- MacOS:
    artifact_templates:
    - skim-v{version}-x86_64-apple-darwin.tar.gz
detail: null
```

## File: `generated/packages/solidity.yaml`
```yaml
# This is generated. Don't modify.
name: solidity
description: Solidity, the Smart Contract Programming Language
source:
  Github:
    owner: ethereum
    repo: solidity
targets:
- LinuxAmd64:
    artifact_templates:
    - v{version}/solc-static-linux
- MacOS:
    artifact_templates:
    - v{version}/solc-macos
- Windows:
    artifact_templates:
    - v{version}/solc-windows.exe
detail: null
```

## File: `generated/packages/sonobuoy.yaml`
```yaml
# This is generated. Don't modify.
name: sonobuoy
description: Sonobuoy is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster by running a set of Kubernetes conformance tests and other plugins in an accessible and non-destructive manner.
source:
  Github:
    owner: vmware-tanzu
    repo: sonobuoy
targets:
- LinuxAmd64:
    artifact_templates:
    - sonobuoy_{version}_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - sonobuoy_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - sonobuoy_{version}_darwin_amd64.tar.gz
- Windows:
    artifact_templates:
    - sonobuoy_{version}_windows_amd64.tar.gz
detail: null
```

## File: `generated/packages/ssvm.yaml`
```yaml
# This is generated. Don't modify.
name: ssvm
description: WasmEdge is a lightweight, high-performance, and extensible WebAssembly runtime for cloud native, edge, and decentralized applications. It powers serverless apps, embedded functions, microservices, smart contracts, and IoT devices.
source:
  Github:
    owner: second-state
    repo: SSVM
targets:
- LinuxAmd64:
    artifact_templates:
    - ssvm-{version}-linux-x64.tar.gz
detail: null
```

## File: `generated/packages/starship.yaml`
```yaml
# This is generated. Don't modify.
name: starship
description: ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell!
source:
  Github:
    owner: starship
    repo: starship
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/starship-x86_64-unknown-linux-musl.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/starship-x86_64-apple-darwin.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/starship-x86_64-pc-windows-msvc.zip'
detail: null
```

## File: `generated/packages/stern.yaml`
```yaml
# This is generated. Don't modify.
name: stern
description: ⎈ Multi pod and container log tailing for Kubernetes -- Friendly fork of https://github.com/wercker/stern
source:
  Github:
    owner: stern
    repo: stern
targets:
- LinuxAmd64:
    artifact_templates:
    - stern_{version}_linux_amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - stern_{version}_linux_arm64.tar.gz
- LinuxArm32:
    artifact_templates:
    - stern_{version}_linux_arm.tar.gz
- MacOS:
    artifact_templates:
    - stern_{version}_darwin_amd64.tar.gz
- MacOS:
    artifact_templates:
    - stern_{version}_darwin_arm64.tar.gz
- Windows:
    artifact_templates:
    - stern_{version}_windows_amd64.tar.gz
- WindowsArm64:
    artifact_templates:
    - stern_{version}_windows_arm64.tar.gz
- WindowsArm:
    artifact_templates:
    - stern_{version}_windows_arm.tar.gz
detail: null
```

## File: `generated/packages/submariner.yaml`
```yaml
# This is generated. Don't modify.
name: submariner
description: Operator that deploys the various Submariner components.
source:
  Github:
    owner: submariner-io
    repo: submariner-operator
targets:
- LinuxAmd64:
    artifact_templates:
    - subctl-v{version}-linux-amd64.tar.xz
- LinuxArm64:
    artifact_templates:
    - subctl-v{version}-linux-arm64.tar.xz
- MacOS:
    artifact_templates:
    - subctl-v{version}-darwin-amd64.tar.xz
- Windows:
    artifact_templates:
    - subctl-v{version}-windows-amd64.exe.tar.xz
detail: null
```

## File: `generated/packages/syncthing.yaml`
```yaml
# This is generated. Don't modify.
name: syncthing
description: Open Source Continuous File Synchronization
source:
  Github:
    owner: syncthing
    repo: syncthing
targets:
- LinuxAmd64:
    artifact_templates:
    - syncthing-linux-amd64-v{version}.tar.gz
- LinuxArm64:
    artifact_templates:
    - syncthing-linux-arm64-v{version}.tar.gz
- MacOS:
    artifact_templates:
    - syncthing-macos-amd64-v{version}.zip
- Windows:
    artifact_templates:
    - syncthing-windows-amd64-v{version}.zip
detail: null
```

## File: `generated/packages/tealdeer.yaml`
```yaml
# This is generated. Don't modify.
name: tealdeer
description: A very fast implementation of tldr in Rust.
source:
  Github:
    owner: dbrgn
    repo: tealdeer
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/tealdeer-linux-x86_64-musl'
    - '{version}/tldr-linux-x86_64-musl'
- MacOS:
    artifact_templates:
    - '{version}/tealdeer-macos-x86_64'
- Windows:
    artifact_templates:
    - '{version}/tealdeer-windows-x86_64-msvc.exe'
detail: null
```

## File: `generated/packages/tecli.yaml`
```yaml
# This is generated. Don't modify.
name: tecli
description: In a world where everything is Terraform, teams use Terraform Cloud API to manage their workloads. TECLI increases teams productivity by facilitating such interaction and by providing easy commands that can be executed on a terminal or on CI/CD systems.
source:
  Github:
    owner: awslabs
    repo: tecli
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/tecli-linux-amd64'
- LinuxArm32:
    artifact_templates:
    - '{version}/tecli-linux-arm'
- MacOS:
    artifact_templates:
    - '{version}/tecli-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/tecli-windows-amd64.exe'
detail: null
```

## File: `generated/packages/termshark.yaml`
```yaml
# This is generated. Don't modify.
name: termshark
description: A terminal UI for tshark, inspired by Wireshark
source:
  Github:
    owner: gcla
    repo: termshark
targets:
- LinuxAmd64:
    artifact_templates:
    - termshark_{version}_linux_x64.tar.gz
- LinuxArm64:
    artifact_templates:
    - termshark_{version}_linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - termshark_{version}_macOS_x64.tar.gz
- Windows:
    artifact_templates:
    - termshark_{version}_windows_x64.zip
detail: null
```

## File: `generated/packages/terraform.yaml`
```yaml
# This is generated. Don't modify.
name: terraform
description: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.
source:
  Github:
    owner: hashicorp
    repo: terraform
targets:
- LinuxAmd64:
    artifact_templates:
    - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip
- LinuxArm64:
    artifact_templates:
    - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_arm64.zip
- MacOS:
    artifact_templates:
    - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_darwin_amd64.zip
- MacOSArm64:
    artifact_templates:
    - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_darwin_arm64.zip
- Windows:
    artifact_templates:
    - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_windows_amd64.zip
detail: null
```

## File: `generated/packages/terrascan.yaml`
```yaml
# This is generated. Don't modify.
name: terrascan
description: Detect compliance and security violations across Infrastructure as Code to mitigate risk before provisioning cloud native infrastructure.
source:
  Github:
    owner: tenable
    repo: terrascan
targets:
- LinuxAmd64:
    artifact_templates:
    - terrascan_{version}_Linux_x86_64.tar.gz
- LinuxArm64:
    artifact_templates:
    - terrascan_{version}_Linux_arm64.tar.gz
- MacOS:
    artifact_templates:
    - terrascan_{version}_Darwin_x86_64.tar.gz
- Windows:
    artifact_templates:
    - terrascan_{version}_Windows_x86_64.tar.gz
detail: null
```

## File: `generated/packages/tilt.yaml`
```yaml
# This is generated. Don't modify.
name: tilt
description: Define your dev environment as code. For microservice apps on Kubernetes.
source:
  Github:
    owner: tilt-dev
    repo: tilt
targets:
- LinuxAmd64:
    artifact_templates:
    - tilt.{version}.linux.x86_64.tar.gz
- MacOS:
    artifact_templates:
    - tilt.{version}.mac.x86_64.tar.gz
- Windows:
    artifact_templates:
    - tilt.{version}.windows.x86_64.zip
detail: null
```

## File: `generated/packages/tokei.yaml`
```yaml
# This is generated. Don't modify.
name: tokei
description: Count your code, quickly.
source:
  Github:
    owner: XAMPPRocky
    repo: tokei
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/tokei-x86_64-unknown-linux-gnu.tar.gz'
- LinuxArm64:
    artifact_templates:
    - '{version}/tokei-aarch64-unknown-linux-gnu.tar.gz'
- LinuxArm32:
    artifact_templates:
    - '{version}/tokei-armv7-unknown-linux-gnueabihf.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/tokei-x86_64-apple-darwin.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/tokei-x86_64-pc-windows-msvc.exe'
detail: null
```

## File: `generated/packages/tracee.yaml`
```yaml
# This is generated. Don't modify.
name: tracee
description: Linux Runtime Security and Forensics using eBPF
source:
  Github:
    owner: aquasecurity
    repo: tracee
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/tracee.tar.gz'
    scan_dirs:
    - dist
detail: null
```

## File: `generated/packages/trivy.yaml`
```yaml
# This is generated. Don't modify.
name: trivy
description: Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more
source:
  Github:
    owner: aquasecurity
    repo: trivy
targets:
- LinuxAmd64:
    artifact_templates:
    - trivy_{version}_Linux-64bit.tar.gz
- LinuxArm64:
    artifact_templates:
    - trivy_{version}_Linux-ARM64.tar.gz
- MacOS:
    artifact_templates:
    - trivy_{version}_macOS-64bit.tar.gz
detail: null
```

## File: `generated/packages/typescript.yaml`
```yaml
# This is generated. Don't modify.
name: typescript
description: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.
source:
  Github:
    owner: microsoft
    repo: TypeScript
targets:
- LinuxAmd64:
    artifact_templates:
    - typescript-{version}.tgz
detail: null
```

## File: `generated/packages/typos.yaml`
```yaml
# This is generated. Don't modify.
name: typos
description: Source code spell checker
source:
  Github:
    owner: crate-ci
    repo: typos
targets:
- LinuxAmd64:
    artifact_templates:
    - typos-v{version}-x86_64-unknown-linux-gnu.tar.gz
- MacOS:
    artifact_templates:
    - typos-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - typos-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/vegeta.yaml`
```yaml
# This is generated. Don't modify.
name: vegeta
description: HTTP load testing tool and library. It's over 9000!
source:
  Github:
    owner: tsenart
    repo: vegeta
targets:
- LinuxAmd64:
    artifact_templates:
    - vegeta_{version}_linux_amd64.tar.gz
- MacOS:
    artifact_templates:
    - vegeta_{version}_darwin_amd64.tar.gz
detail: null
```

## File: `generated/packages/velero.yaml`
```yaml
# This is generated. Don't modify.
name: velero
description: Backup and migrate Kubernetes applications and their persistent volumes
source:
  Github:
    owner: vmware-tanzu
    repo: velero
targets:
- LinuxAmd64:
    artifact_templates:
    - velero-v{version}-linux-amd64.tar.gz
- LinuxArm64:
    artifact_templates:
    - velero-v{version}-linux-arm64.tar.gz
- MacOS:
    artifact_templates:
    - velero-v{version}-darwin-amd64.tar.gz
detail: null
```

## File: `generated/packages/viddy.yaml`
```yaml
# This is generated. Don't modify.
name: viddy
description: 👀 A modern watch command. Time machine and pager etc.
source:
  Github:
    owner: sachaos
    repo: viddy
targets:
- LinuxAmd64:
    artifact_templates:
    - viddy_{version}_Linux_x86_64.tar.gz
- MacOS:
    artifact_templates:
    - viddy_{version}_Darwin_x86_64.tar.gz
- Windows:
    artifact_templates:
    - viddy_{version}_Windows_x86_64.tar.gz
detail: null
```

## File: `generated/packages/volta.yaml`
```yaml
# This is generated. Don't modify.
name: volta
description: 'Volta: JS Toolchains as Code. ⚡'
source:
  Github:
    owner: volta-cli
    repo: volta
targets:
- LinuxAmd64:
    artifact_templates:
    - volta-{version}-linux-openssl-1.1.tar.gz
- MacOS:
    artifact_templates:
    - volta-{version}-macos.tar.gz
- Windows:
    artifact_templates:
    - volta-{version}-windows.zip
detail: null
```

## File: `generated/packages/wabt.yaml`
```yaml
# This is generated. Don't modify.
name: wabt
description: The WebAssembly Binary Toolkit
source:
  Github:
    owner: WebAssembly
    repo: wabt
targets:
- LinuxAmd64:
    artifact_templates:
    - wabt-{version}-ubuntu.tar.gz
- MacOS:
    artifact_templates:
    - wabt-{version}-macos.tar.gz
- Windows:
    artifact_templates:
    - wabt-{version}-windows.tar.gz
detail: null
```

## File: `generated/packages/wasm-to-oci.yaml`
```yaml
# This is generated. Don't modify.
name: wasm-to-oci
description: Use OCI registries to distribute Wasm modules
source:
  Github:
    owner: engineerd
    repo: wasm-to-oci
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/linux-amd64-wasm-to-oci'
- MacOS:
    artifact_templates:
    - '{version}/darwin-amd64-wasm-to-oci'
- Windows:
    artifact_templates:
    - '{version}/windows-amd64-wasm-to-oci.exe'
detail: null
```

## File: `generated/packages/wasme.yaml`
```yaml
# This is generated. Don't modify.
name: wasme
description: Web Assembly tools and SDKs for extending cloud-native infrastructure
source:
  Github:
    owner: solo-io
    repo: wasm
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/wasme-linux-amd64'
- MacOS:
    artifact_templates:
    - '{version}/wasme-darwin-amd64'
- Windows:
    artifact_templates:
    - '{version}/wasme-windows-adm64.exe'
detail: null
```

## File: `generated/packages/wasmer.yaml`
```yaml
# This is generated. Don't modify.
name: wasmer
description: 🚀 The leading WebAssembly Runtime supporting WASIX, WASI and Emscripten
source:
  Github:
    owner: wasmerio
    repo: wasmer
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/wasmer-linux-amd64.tar.gz'
- LinuxArm64:
    artifact_templates:
    - '{version}/wasmer-linux-aarch64.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/wasmer-darwin-amd64.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/wasmer-windows.exe'
detail: null
```

## File: `generated/packages/wasmtime.yaml`
```yaml
# This is generated. Don't modify.
name: wasmtime
description: A fast and secure runtime for WebAssembly
source:
  Github:
    owner: bytecodealliance
    repo: wasmtime
targets:
- Windows:
    artifact_templates:
    - wasmtime-v{version}-x86_64-windows.zip
- Default:
    artifact_templates:
    - wasmtime-v{version}-{arch}-{os}.tar.xz
detail: null
```

## File: `generated/packages/waypoint.yaml`
```yaml
# This is generated. Don't modify.
name: waypoint
description: A tool to build, deploy, and release any application on any platform.
source:
  Github:
    owner: hashicorp
    repo: waypoint
targets:
- LinuxAmd64:
    artifact_templates:
    - https://releases.hashicorp.com/waypoint/{version}/waypoint_{version}_linux_amd64.zip
- MacOS:
    artifact_templates:
    - https://releases.hashicorp.com/waypoint/{version}/waypoint_{version}_windows_amd64.zip
- Windows:
    artifact_templates:
    - https://releases.hashicorp.com/waypoint/{version}/waypoint_{version}_darwin_amd64.zip
detail: null
```

## File: `generated/packages/wstunnel.yaml`
```yaml
# This is generated. Don't modify.
name: wstunnel
description: 'Tunneling over websocket protocol - Static binary available '
source:
  Github:
    owner: erebe
    repo: wstunnel
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/wstunnel-x64-linux.zip'
- LinuxArm64:
    artifact_templates:
    - '{version}/wstunnel-aarch64-ubuntu18.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/wstunnel-x64-macos.zip'
- Windows:
    artifact_templates:
    - '{version}/wstunnel-x64-windows.exe.zip'
detail: null
```

## File: `generated/packages/xh.yaml`
```yaml
# This is generated. Don't modify.
name: xh
description: Friendly and fast tool for sending HTTP requests
source:
  Github:
    owner: ducaale
    repo: xh
targets:
- LinuxAmd64:
    artifact_templates:
    - xh-v{version}-x86_64-unknown-linux-musl.tar.gz
    executable_mappings:
      xh: xh xhs
- LinuxArm32:
    artifact_templates:
    - xh-v{version}-arm-unknown-linux-gnueabihf.tar.gz
    executable_mappings:
      xh: xh xhs
- MacOS:
    artifact_templates:
    - xh-v{version}-x86_64-apple-darwin.tar.gz
    executable_mappings:
      xh: xh xhs
- Windows:
    artifact_templates:
    - xh-v{version}-x86_64-pc-windows-msvc.zip
    executable_mappings:
      xh: xh xhs
detail: null
```

## File: `generated/packages/yq.yaml`
```yaml
# This is generated. Don't modify.
name: yq
description: yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties processor
source:
  Github:
    owner: mikefarah
    repo: yq
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/yq_linux_amd64'
- LinuxArm64:
    artifact_templates:
    - '{version}/yq_linux_arm64'
- MacOS:
    artifact_templates:
    - '{version}/yq_darwin_amd64'
- Windows:
    artifact_templates:
    - '{version}/yq_windows_amd64.exe'
detail: null
```

## File: `generated/packages/zellij.yaml`
```yaml
# This is generated. Don't modify.
name: zellij
description: A terminal workspace with batteries included
source:
  Github:
    owner: zellij-org
    repo: zellij
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/zellij-x86_64-unknown-linux-musl.tar.gz'
- LinuxArm64:
    artifact_templates:
    - '{version}/zellij-aarch64-unknown-linux-musl.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/zellij-aarch64-apple-darwin.tar.gz'
- MacOSArm64:
    artifact_templates:
    - '{version}/zellij-aarch64-apple-darwin.tar.gz'
detail: null
```

## File: `generated/packages/zola.yaml`
```yaml
# This is generated. Don't modify.
name: zola
description: A fast static site generator in a single binary with everything built-in. https://www.getzola.org
source:
  Github:
    owner: getzola
    repo: zola
targets:
- LinuxAmd64:
    artifact_templates:
    - zola-v{version}-x86_64-unknown-linux-gnu.tar.gz
- MacOS:
    artifact_templates:
    - zola-v{version}-x86_64-apple-darwin.tar.gz
- Windows:
    artifact_templates:
    - zola-v{version}-x86_64-pc-windows-msvc.zip
detail: null
```

## File: `generated/packages/zoxide.yaml`
```yaml
# This is generated. Don't modify.
name: zoxide
description: A smarter cd command. Supports all major shells.
source:
  Github:
    owner: ajeetdsouza
    repo: zoxide
targets:
- LinuxAmd64:
    artifact_templates:
    - '{version}/zoxide-x86_64-unknown-linux-musl.tar.gz'
- LinuxArm32:
    artifact_templates:
    - '{version}/zoxide-armv7-unknown-linux-musleabihf.tar.gz'
- MacOS:
    artifact_templates:
    - '{version}/zoxide-x86_64-apple-darwin.tar.gz'
- Windows:
    artifact_templates:
    - '{version}/zoxide-x86_64-pc-windows-msvc.zip'
detail: null
```

## File: `generated-v1/index.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
- name: ali
  owner: nakabonne
  source: github
- name: argocd
  owner: argoproj
  source: github
- name: arkade
  owner: alexellis
  source: github
- name: asdf
  owner: asdf-vm
  source: github
- name: axelard
  owner: axelarnetwork
  source: github
- name: bat
  owner: sharkdp
  source: github
- name: bottom
  owner: ClementTsang
  source: github
- name: buf
  owner: bufbuild
  source: github
- name: bun
  owner: oven-sh
  source: github
- name: camel-k
  owner: apache
  source: github
- name: chisel
  owner: jpillora
  source: github
- name: choose
  owner: theryangeary
  source: github
- name: cloak
  owner: cbeuw
  source: github
- name: cni-plugins
  owner: containernetworking
  source: github
- name: codeql
  owner: github
  source: github
- name: compose
  owner: docker
  source: github
- name: conftest
  owner: open-policy-agent
  source: github
- name: consul
  owner: hashicorp
  source: github
- name: containerd
  owner: containerd
  source: github
- name: copilot-cli
  owner: aws
  source: github
- name: coreutils
  owner: uutils
  source: github
- name: cosign
  owner: sigstore
  source: github
- name: croc
  owner: schollz
  source: github
- name: ctlptl
  owner: tilt-dev
  source: github
- name: czkawka
  owner: qarmin
  source: github
- name: dasel
  owner: TomWright
  source: github
- name: delta
  owner: dandavison
  source: github
- name: deno
  owner: denoland
  source: github
- name: direnv
  owner: direnv
  source: github
- name: dive
  owner: wagoodman
  source: github
- name: doctl
  owner: digitalocean
  source: github
- name: dog
  owner: ogham
  source: github
- name: dolt
  owner: dolthub
  source: github
- name: dua-cli
  owner: Byron
  source: github
- name: dust
  owner: bootandy
  source: github
- name: eksctl
  owner: eksctl-io
  source: github
- name: exa
  owner: ogham
  source: github
- name: fd
  owner: sharkdp
  source: github
- name: firecracker
  owner: firecracker-microvm
  source: github
- name: fission
  owner: fission
  source: github
- name: fleet
  owner: rancher
  source: github
- name: flux2
  owner: fluxcd
  source: github
- name: fnm
  owner: Schniz
  source: github
- name: fortio
  owner: fortio
  source: github
- name: foundry
  owner: foundry-rs
  source: github
- name: frum
  owner: TaKO8Ki
  source: github
- name: gh
  owner: cli
  source: github
- name: gitleaks
  owner: gitleaks
  source: github
- name: gitui
  owner: extrawurst
  source: github
- name: go
  owner: golang
  source: github
- name: go-http-tunnel
  owner: mmatczuk
  source: github
- name: goose
  owner: pressly
  source: github
- name: gping
  owner: orf
  source: github
- name: gradle
  owner: gradle
  source: github
- name: grex
  owner: pemistahl
  source: github
- name: grpcurl
  owner: fullstorydev
  source: github
- name: helm
  owner: helm
  source: github
- name: helmfile
  owner: helmfile
  source: github
- name: hetty
  owner: dstotijn
  source: github
- name: hexyl
  owner: sharkdp
  source: github
- name: httptap
  owner: monasticacademy
  source: github
- name: huber
  owner: innobead
  source: github
- name: hugo
  owner: gohugoio
  source: github
- name: hyperfine
  owner: sharkdp
  source: github
- name: img
  owner: genuinetools
  source: github
- name: istio
  owner: istio
  source: github
- name: jiq
  owner: fiatjaf
  source: github
- name: jless
  owner: PaulJuliusMartinez
  source: github
- name: jq
  owner: jqlang
  source: github
- name: just
  owner: casey
  source: github
- name: jwt-cli
  owner: mike-engel
  source: github
- name: k0s
  owner: k0sproject
  source: github
- name: k3d
  owner: k3d-io
  source: github
- name: k3s
  owner: k3s-io
  source: github
- name: k3sup
  owner: alexellis
  source: github
- name: k6
  owner: grafana
  source: github
- name: k9s
  owner: derailed
  source: github
- name: kind
  owner: kubernetes-sigs
  source: github
- name: ko
  owner: ko-build
  source: github
- name: kompose
  owner: kubernetes
  source: github
- name: kotlin
  owner: JetBrains
  source: github
- name: kpt
  owner: GoogleContainerTools
  source: github
- name: krew
  owner: kubernetes-sigs
  source: github
- name: kube-bench
  owner: aquasecurity
  source: github
- name: kube-linter
  owner: stackrox
  source: github
- name: kubectl
  owner: kubernetes
  source: github
- name: kubefire
  owner: innobead
  source: github
- name: kubestr
  owner: kastenhq
  source: github
- name: kubevirt
  owner: kubevirt
  source: github
- name: kustomize
  owner: kubernetes-sigs
  source: github
- name: kuttl
  owner: kudobuilder
  source: github
- name: linkerd2-edge
  owner: linkerd
  source: github
- name: linkerd2-stable
  owner: linkerd
  source: github
- name: loc
  owner: cgag
  source: github
- name: local-ai
  owner: mudler
  source: github
- name: lsd
  owner: lsd-rs
  source: github
- name: minikube
  owner: kubernetes
  source: github
- name: mkcert
  owner: FiloSottile
  source: github
- name: nat
  owner: willdoescode
  source: github
- name: natscli
  owner: nats-io
  source: github
- name: navi
  owner: denisidoro
  source: github
- name: nerdctl
  owner: containerd
  source: github
- name: node
  owner: nodejs
  source: github
- name: norouter
  owner: norouter
  source: github
- name: nushell
  owner: nushell
  source: github
- name: octant
  owner: vmware-tanzu
  source: github
- name: okteto
  owner: okteto
  source: github
- name: ollama
  owner: ollama
  source: github
- name: onefetch
  owner: o2sh
  source: github
- name: opa
  owner: open-policy-agent
  source: github
- name: opentofu
  owner: opentofu
  source: github
- name: oras
  owner: oras-project
  source: github
- name: pack
  owner: buildpacks
  source: github
- name: packer
  owner: hashicorp
  source: github
- name: podman
  owner: containers
  source: github
- name: powershell
  owner: PowerShell
  source: github
- name: procs
  owner: dalance
  source: github
- name: protoc
  owner: protocolbuffers
  source: github
- name: pueue
  owner: Nukesor
  source: github
- name: pulumi
  owner: pulumi
  source: github
- name: rclone
  owner: rclone
  source: github
- name: regclient
  owner: regclient
  source: github
- name: ripgrep
  owner: BurntSushi
  source: github
- name: rke2
  owner: rancher
  source: github
- name: sad
  owner: ms-jpq
  source: github
- name: saml2aws
  owner: Versent
  source: github
- name: sd
  owner: chmln
  source: github
- name: shadowsocks
  owner: shadowsocks
  source: github
- name: skaffold
  owner: GoogleContainerTools
  source: github
- name: skim
  owner: skim-rs
  source: github
- name: solidity
  owner: ethereum
  source: github
- name: sonobuoy
  owner: vmware-tanzu
  source: github
- name: starship
  owner: starship
  source: github
- name: stern
  owner: stern
  source: github
- name: syncthing
  owner: syncthing
  source: github
- name: tealdeer
  owner: tealdeer-rs
  source: github
- name: termshark
  owner: gcla
  source: github
- name: terraform
  owner: hashicorp
  source: github
- name: terrascan
  owner: tenable
  source: github
- name: tilt
  owner: tilt-dev
  source: github
- name: tokei
  owner: XAMPPRocky
  source: github
- name: tracee
  owner: aquasecurity
  source: github
- name: traefik
  owner: traefik
  source: github
- name: trivy
  owner: aquasecurity
  source: github
- name: typescript
  owner: microsoft
  source: github
- name: typos
  owner: crate-ci
  source: github
- name: vegeta
  owner: tsenart
  source: github
- name: velero
  owner: vmware-tanzu
  source: github
- name: viddy
  owner: sachaos
  source: github
- name: volta
  owner: volta-cli
  source: github
- name: wabt
  owner: WebAssembly
  source: github
- name: wasmer
  owner: wasmerio
  source: github
- name: wasmtime
  owner: bytecodealliance
  source: github
- name: wstunnel
  owner: erebe
  source: github
- name: xh
  owner: ducaale
  source: github
- name: yq
  owner: mikefarah
  source: github
- name: zellij
  owner: zellij-org
  source: github
- name: zola
  owner: getzola
  source: github
- name: zoxide
  owner: ajeetdsouza
  source: github
```

## File: `generated-v1/packages/ali.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: ali
description: Generate HTTP load and plot the results in real-time
source: !Github
  owner: nakabonne
  repo: ali
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/argocd.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: argocd
description: Declarative Continuous Deployment for Kubernetes
source: !Github
  owner: argoproj
  repo: argo-cd
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/arkade.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: arkade
description: Open Source Marketplace For Developer Tools
source: !Github
  owner: alexellis
  repo: arkade
targets:
- !LinuxAmd64
  artifact_templates:
  - arkade
- !LinuxArm64
  artifact_templates:
  - arkade-arm64
- !LinuxArm
  artifact_templates:
  - arkade-armhf
- !MacOSAmd64
  artifact_templates:
  - arkade-darwin
- !MacOSArm64
  artifact_templates:
  - arkade-darwin-arm64
- !WindowsAmd64
  artifact_templates:
  - arkade.exe
```

## File: `generated-v1/packages/asdf.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: asdf
description: Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more
source: !Github
  owner: asdf-vm
  repo: asdf
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/axelard.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: axelard
description: 'Axelar: A Decentralized Blockchain Interoperability Network'
source: !Github
  owner: axelarnetwork
  repo: axelar-core
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/bat.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: bat
description: A cat(1) clone with wings.
source: !Github
  owner: sharkdp
  repo: bat
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/bottom.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: bottom
description: Yet another cross-platform graphical process/system monitor.
source: !Github
  owner: ClementTsang
  repo: bottom
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/buf.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: buf
description: The best way of working with Protocol Buffers.
source: !Github
  owner: bufbuild
  repo: buf
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/bun.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: bun
description: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
source: !Github
  owner: oven-sh
  repo: bun
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/camel-k.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: camel-k
description: Apache Camel K is a lightweight integration platform, born on Kubernetes, with serverless superpowers
source: !Github
  owner: apache
  repo: camel-k
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/chisel.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: chisel
description: A fast TCP/UDP tunnel over HTTP
source: !Github
  owner: jpillora
  repo: chisel
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/choose.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: choose
description: A human-friendly and fast alternative to cut and (sometimes) awk
source: !Github
  owner: theryangeary
  repo: choose
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/cloak.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: cloak
description: A censorship circumvention tool to evade detection by authoritarian state adversaries
source: !Github
  owner: cbeuw
  repo: Cloak
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/cni-plugins.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: cni-plugins
description: Some reference and example networking plugins, maintained by the CNI team.
source: !Github
  owner: containernetworking
  repo: plugins
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/codeql.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: codeql
description: Binaries for the CodeQL CLI
source: !Github
  owner: github
  repo: codeql-cli-binaries
targets:
- !LinuxAmd64
  artifact_templates:
  - codeql-linux64.zip
- !MacOSAmd64
  artifact_templates:
  - codeql-osx64.zip
- !WindowsAmd64
  artifact_templates:
  - codeql-win64.zip
```

## File: `generated-v1/packages/compose.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: compose
description: Define and run multi-container applications with Docker
source: !Github
  owner: docker
  repo: compose
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/conftest.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: conftest
description: Write tests against structured configuration data using the Open Policy Agent Rego query language
source: !Github
  owner: open-policy-agent
  repo: conftest
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/consul.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: consul
description: Consul is a distributed, highly available, and data center aware solution to connect and configure applications across dynamic, distributed infrastructure.
source: !Github
  owner: hashicorp
  repo: consul
targets:
- !LinuxAmd64
  artifact_templates:
  - https://releases.hashicorp.com/consul/{version}/consul_{version}_linux_amd64.zip
- !LinuxArm64
  artifact_templates:
  - https://releases.hashicorp.com/consul/{version}/consul_{version}_linux_arm64.zip
- !MacOSAmd64
  artifact_templates:
  - https://releases.hashicorp.com/consul/{version}/consul_{version}_darwin_amd64.zip
- !WindowsAmd64
  artifact_templates:
  - https://releases.hashicorp.com/consul/{version}/consul_{version}_windows_amd64.zip
```

## File: `generated-v1/packages/containerd.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: containerd
description: An open and reliable container runtime
source: !Github
  owner: containerd
  repo: containerd
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/copilot-cli.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: copilot-cli
description: 'The AWS Copilot CLI is a tool for developers to build, release and operate production ready containerized applications on AWS App Runner or Amazon ECS on AWS Fargate. '
source: !Github
  owner: aws
  repo: copilot-cli
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/coreutils.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: coreutils
description: Cross-platform Rust rewrite of the GNU coreutils
source: !Github
  owner: uutils
  repo: coreutils
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/cosign.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: cosign
description: Code signing and transparency for containers and binaries
source: !Github
  owner: sigstore
  repo: cosign
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/croc.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: croc
description: 'Easily and securely send things from one computer to another :crocodile: :package:'
source: !Github
  owner: schollz
  repo: croc
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/ctlptl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: ctlptl
description: Making local Kubernetes clusters fun and easy to set up
source: !Github
  owner: tilt-dev
  repo: ctlptl
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/czkawka.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: czkawka
description: Multi functional app to find duplicates, empty folders, similar images etc.
source: !Github
  owner: qarmin
  repo: czkawka
targets:
- !LinuxAmd64
  artifact_templates:
  - linux_czkawka_cli
  - linux_czkawka_gui
- !MacOSAmd64
  artifact_templates:
  - mac_czkawka_cli
  - mac_czkawka_gui
  - mac_krokiet_gui
- !WindowsAmd64
  artifact_templates:
  - windows_czkawka_cli.exe
  - windows_krokiet_gui_linversion.exe
  - windows_krokiet_gui_linversion_console.exe
  - windows_krokiet_gui_winversion.exe
```

## File: `generated-v1/packages/dasel.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: dasel
description: Select, put and delete data from JSON, TOML, YAML, XML and CSV files with a single tool. Supports conversion between formats and can be used as a Go package.
source: !Github
  owner: TomWright
  repo: dasel
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/delta.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: delta
description: A syntax-highlighting pager for git, diff, grep, and blame output
source: !Github
  owner: dandavison
  repo: delta
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/deno.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: deno
description: A modern runtime for JavaScript and TypeScript.
source: !Github
  owner: denoland
  repo: deno
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/direnv.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: direnv
description: unclutter your .profile
source: !Github
  owner: direnv
  repo: direnv
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/dive.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: dive
description: A tool for exploring each layer in a docker image
source: !Github
  owner: wagoodman
  repo: dive
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/doctl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: doctl
description: The official command line interface for the DigitalOcean API.
source: !Github
  owner: digitalocean
  repo: doctl
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/dog.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: dog
description: A command-line DNS client.
source: !Github
  owner: ogham
  repo: dog
targets:
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/dolt.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: dolt
description: Dolt – Git for Data
source: !Github
  owner: dolthub
  repo: dolt
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/dua-cli.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: dua-cli
description: View disk space usage and delete unwanted data, fast.
source: !Github
  owner: Byron
  repo: dua-cli
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/dust.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: dust
description: A more intuitive version of du in rust
source: !Github
  owner: bootandy
  repo: dust
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/eksctl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: eksctl
description: The official CLI for Amazon EKS
source: !Github
  owner: eksctl-io
  repo: eksctl
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/exa.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: exa
description: A modern replacement for ‘ls’.
source: !Github
  owner: ogham
  repo: exa
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/fd.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: fd
description: A simple, fast and user-friendly alternative to 'find'
source: !Github
  owner: sharkdp
  repo: fd
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/firecracker.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: firecracker
description: Secure and fast microVMs for serverless computing.
source: !Github
  owner: firecracker-microvm
  repo: firecracker
targets:
- !LinuxAmd64
  artifact_templates:
  - firecracker-v{version}-x86_64.tgz
  scan_dirs:
  - release-v{version}-{arch}
- !LinuxArm64
  artifact_templates:
  - firecracker-v{version}-aarch64.tgz
  scan_dirs:
  - release-v{version}-{arch}
```

## File: `generated-v1/packages/fission.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: fission
description: Fast and Simple Serverless Functions for Kubernetes
source: !Github
  owner: fission
  repo: fission
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/fleet.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: fleet
description: Deploy workloads from Git to large fleets of Kubernetes clusters
source: !Github
  owner: rancher
  repo: fleet
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/flux2.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: flux2
description: Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.
source: !Github
  owner: fluxcd
  repo: flux2
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/fnm.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: fnm
description: 🚀 Fast and simple Node.js version manager, built in Rust
source: !Github
  owner: Schniz
  repo: fnm
targets:
- !LinuxAmd64
  artifact_templates:
  - fnm-linux.zip
- !LinuxArm64
  artifact_templates:
  - fnm-arm64.zip
- !MacOSAmd64
  artifact_templates:
  - fnm-macos.zip
- !WindowsAmd64
  artifact_templates:
  - fnm-windows.zip
```

## File: `generated-v1/packages/fortio.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: fortio
description: Fortio load testing library, command line tool, advanced echo server and web UI in go (golang). Allows to specify a set query-per-second load and record latency histograms and other useful stats.
source: !Github
  owner: fortio
  repo: fortio
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates:
  - fortio_win_{version}.zip
```

## File: `generated-v1/packages/foundry.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: foundry
description: Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust.
source: !Github
  owner: foundry-rs
  repo: foundry
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/frum.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: frum
description: A little bit fast and modern Ruby version manager written in Rust
source: !Github
  owner: TaKO8Ki
  repo: frum
targets:
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/gh.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: gh
description: GitHub’s official command line tool
source: !Github
  owner: cli
  repo: cli
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/gitleaks.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: gitleaks
description: Find secrets with Gitleaks 🔑
source: !Github
  owner: gitleaks
  repo: gitleaks
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/gitui.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: gitui
description: Blazing 💥 fast terminal-ui for git written in rust 🦀
source: !Github
  owner: extrawurst
  repo: gitui
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates:
  - gitui-mac.tar.gz
- !WindowsAmd64
  artifact_templates:
  - gitui-win.tar.gz
```

## File: `generated-v1/packages/go-http-tunnel.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: go-http-tunnel
description: Fast and secure tunnels over HTTP/2
source: !Github
  owner: mmatczuk
  repo: go-http-tunnel
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/go.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: go
description: The Go programming language
source: !Github
  owner: golang
  repo: go
targets:
- !LinuxAmd64
  artifact_templates:
  - https://golang.org/dl/{version}.linux-amd64.tar.gz
- !LinuxArm64
  artifact_templates:
  - https://golang.org/dl/{version}.linux-arm64.tar.gz
- !MacOSAmd64
  artifact_templates:
  - https://golang.org/dl/{version}.darwin-amd64.tar.gz
- !MacOSArm64
  artifact_templates:
  - https://golang.org/dl/go{version}.darwin-arm64.tar.gz
- !WindowsAmd64
  artifact_templates:
  - https://golang.org/dl/go{version}.windows-amd64.zip
```

## File: `generated-v1/packages/goose.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: goose
description: 'A database migration tool. Supports SQL migrations and Go functions. '
source: !Github
  owner: pressly
  repo: goose
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/gping.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: gping
description: Ping, but with a graph
source: !Github
  owner: orf
  repo: gping
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates:
  - gping-Windows-msvc-x86_64.zip
```

## File: `generated-v1/packages/gradle.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: gradle
description: Adaptable, fast automation for all
source: !Github
  owner: gradle
  repo: gradle
targets:
- !LinuxAmd64
  artifact_templates:
  - https://services.gradle.org/distributions/gradle-{version}-bin.zip
- !MacOSAmd64
  artifact_templates:
  - https://services.gradle.org/distributions/gradle-{version}-bin.zip
- !WindowsAmd64
  artifact_templates:
  - https://services.gradle.org/distributions/gradle-{version}-bin.zip
```

## File: `generated-v1/packages/grex.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: grex
description: A command-line tool and Rust library with Python bindings for generating regular expressions from user-provided test cases
source: !Github
  owner: pemistahl
  repo: grex
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/grpcurl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: grpcurl
description: 'Like cURL, but for gRPC: Command-line tool for interacting with gRPC servers'
source: !Github
  owner: fullstorydev
  repo: grpcurl
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/helm.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: helm
description: The Kubernetes Package Manager
source: !Github
  owner: helm
  repo: helm
targets:
- !LinuxAmd64
  artifact_templates:
  - https://get.helm.sh/helm-v{version}-linux-amd64.tar.gz
- !LinuxArm64
  artifact_templates:
  - https://get.helm.sh/helm-v{version}-linux-arm64.tar.gz
- !LinuxArm
  artifact_templates:
  - https://get.helm.sh/helm-v{version}-linux-arm.tar.gz
- !MacOSAmd64
  artifact_templates:
  - https://get.helm.sh/helm-v{version}-darwin-amd64.tar.gz
- !MacOSArm64
  artifact_templates:
  - https://get.helm.sh/helm-v{version}-darwin-arm64.tar.gz
- !WindowsAmd64
  artifact_templates:
  - https://get.helm.sh/helm-v{version}-windows-amd64.zip
```

## File: `generated-v1/packages/helmfile.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: helmfile
description: Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases. Generate all-in-one manifests for use with ArgoCD.
source: !Github
  owner: helmfile
  repo: helmfile
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/hetty.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: hetty
description: An HTTP toolkit for security research.
source: !Github
  owner: dstotijn
  repo: hetty
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/hexyl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: hexyl
description: A command-line hex viewer
source: !Github
  owner: sharkdp
  repo: hexyl
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/httptap.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: httptap
description: View HTTP/HTTPS requests made by any Linux program
source: !Github
  owner: monasticacademy
  repo: httptap
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
```

## File: `generated-v1/packages/huber.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: huber
description: 'Huber: simplify GitHub package management'
source: !Github
  owner: innobead
  repo: huber
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/hugo.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: hugo
description: The world’s fastest framework for building websites.
source: !Github
  owner: gohugoio
  repo: hugo
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates:
  - hugo_{version}_darwin-universal.tar.gz
  - hugo_extended_{version}_darwin-universal.tar.gz
  - hugo_extended_withdeploy_{version}_darwin-universal.tar.gz
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/hyperfine.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: hyperfine
description: A command-line benchmarking tool
source: !Github
  owner: sharkdp
  repo: hyperfine
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/img.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: img
description: Standalone, daemon-less, unprivileged Dockerfile and OCI compatible container image builder.
source: !Github
  owner: genuinetools
  repo: img
targets:
- !LinuxAmd64
  artifact_templates:
  - img-linux-amd64
```

## File: `generated-v1/packages/istio.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: istio
description: Connect, secure, control, and observe services.
source: !Github
  owner: istio
  repo: istio
targets:
- !LinuxAmd64
  artifact_templates:
  - istio-{version}-linux-amd64.tar.gz
  - istioctl-{version}-linux-amd64.tar.gz
- !LinuxArm64
  artifact_templates:
  - istio-{version}-linux-arm64.tar.gz
  - istioctl-{version}-linux-arm64.tar.gz
- !MacOSAmd64
  artifact_templates:
  - istio-{version}-osx.tar.gz
  - istioctl-{version}-osx.tar.gz
- !WindowsAmd64
  artifact_templates:
  - istio-{version}-win.zip
  - istioctl-{version}-win.zip
```

## File: `generated-v1/packages/jiq.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: jiq
description: jid on jq - interactive JSON query tool using jq expressions
source: !Github
  owner: fiatjaf
  repo: jiq
targets:
- !LinuxAmd64
  artifact_templates:
  - jiq_linux_amd64
- !MacOSAmd64
  artifact_templates:
  - jiq_darwin_amd64
- !WindowsAmd64
  artifact_templates:
  - jiq_windows_amd64.exe
```

## File: `generated-v1/packages/jless.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: jless
description: jless is a command-line JSON viewer designed for reading, exploring, and searching through JSON data.
source: !Github
  owner: PaulJuliusMartinez
  repo: jless
targets:
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/jq.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: jq
description: Command-line JSON processor
source: !Github
  owner: jqlang
  repo: jq
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/just.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: just
description: 🤖 Just a command runner
source: !Github
  owner: casey
  repo: just
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/jwt-cli.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: jwt-cli
description: A super fast CLI tool to decode and encode JWTs built in Rust
source: !Github
  owner: mike-engel
  repo: jwt-cli
targets:
- !LinuxAmd64
  artifact_templates:
  - jwt-linux.tar.gz
- !LinuxArm64
  artifact_templates:
  - jwt-linux-arm64.tar.gz
- !MacOSAmd64
  artifact_templates:
  - jwt-macOS.tar.gz
- !WindowsAmd64
  artifact_templates:
  - jwt-windows.tar.gz
```

## File: `generated-v1/packages/k0s.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: k0s
description: k0s - The Zero Friction Kubernetes
source: !Github
  owner: k0sproject
  repo: k0s
targets:
- !LinuxAmd64
  artifact_templates:
  - k0s-v{version}+k0s.0-amd64
- !LinuxArm
  artifact_templates:
  - k0s-v{version}+k0s.0-arm
- !LinuxArm64
  artifact_templates:
  - k0s-v{version}+k0s.0-arm64
```

## File: `generated-v1/packages/k3d.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: k3d
description: Little helper to run CNCF's k3s in Docker
source: !Github
  owner: k3d-io
  repo: k3d
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/k3s.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: k3s
description: Lightweight Kubernetes
source: !Github
  owner: k3s-io
  repo: k3s
targets:
- !LinuxAmd64
  artifact_templates:
  - k3s
- !LinuxArm64
  artifact_templates:
  - k3s-arm64
- !LinuxArm
  artifact_templates:
  - k3s-armhf
```

## File: `generated-v1/packages/k3sup.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: k3sup
description: bootstrap K3s over SSH in < 60s 🚀
source: !Github
  owner: alexellis
  repo: k3sup
targets:
- !LinuxAmd64
  artifact_templates:
  - k3sup
- !LinuxArm64
  artifact_templates:
  - k3sup-arm64
- !LinuxArm
  artifact_templates:
  - k3sup-armhf
- !MacOSAmd64
  artifact_templates:
  - k3sup-darwin
- !MacOSArm64
  artifact_templates:
  - k3sup-darwin-arm64
- !WindowsAmd64
  artifact_templates:
  - k3sup.exe
```

## File: `generated-v1/packages/k6.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: k6
description: A modern load testing tool, using Go and JavaScript - https://k6.io
source: !Github
  owner: grafana
  repo: k6
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/k9s.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: k9s
description: 🐶 Kubernetes CLI To Manage Your Clusters In Style!
source: !Github
  owner: derailed
  repo: k9s
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kind.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kind
description: Kubernetes IN Docker - local clusters for testing Kubernetes
source: !Github
  owner: kubernetes-sigs
  repo: kind
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/ko.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: ko
description: Build and deploy Go applications
source: !Github
  owner: ko-build
  repo: ko
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kompose.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kompose
description: Convert Compose to Kubernetes
source: !Github
  owner: kubernetes
  repo: kompose
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kotlin.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kotlin
description: 'The Kotlin Programming Language. '
source: !Github
  owner: JetBrains
  repo: kotlin
targets:
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kpt.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kpt
description: Automate Kubernetes Configuration Editing
source: !Github
  owner: GoogleContainerTools
  repo: kpt
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/krew.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: krew
description: 📦 Find and install kubectl plugins
source: !Github
  owner: kubernetes-sigs
  repo: krew
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kube-bench.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kube-bench
description: Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
source: !Github
  owner: aquasecurity
  repo: kube-bench
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/kube-linter.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kube-linter
description: KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.
source: !Github
  owner: stackrox
  repo: kube-linter
targets:
- !LinuxAmd64
  artifact_templates:
  - kube-linter-linux.tar.gz
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates:
  - kube-linter-darwin.tar.gz
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/kubectl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kubectl
description: Production-Grade Container Scheduling and Management
source: !Github
  owner: kubernetes
  repo: kubernetes
targets:
- !LinuxAmd64
  artifact_templates:
  - https://dl.k8s.io/release/v{version}/bin/linux/amd64/kubectl
- !LinuxArm64
  artifact_templates:
  - https://dl.k8s.io/release/v{version}/bin/linux/arm64/kubectl
- !LinuxArm64
  artifact_templates:
  - https://dl.k8s.io/release/v{version}/bin/linux/arm/kubectl
- !MacOSAmd64
  artifact_templates:
  - https://dl.k8s.io/release/v{version}/bin/darwin/amd64/kubectl
- !MacOSArm64
  artifact_templates:
  - https://dl.k8s.io/release/v{version}/bin/darwin/arm64/kubectl
- !WindowsAmd64
  artifact_templates:
  - https://dl.k8s.io/release/v{version}/bin/windows/amd64/kubectl.exe
```

## File: `generated-v1/packages/kubefire.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kubefire
description: KubeFire 🔥, creates and manages Kubernetes Clusters using Firecracker microVMs
source: !Github
  owner: innobead
  repo: kubefire
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
```

## File: `generated-v1/packages/kubestr.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kubestr
source: !Github
  owner: kastenhq
  repo: kubestr
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kubevirt.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kubevirt
description: Kubernetes Virtualization API and runtime in order to define and manage virtual machines.
source: !Github
  owner: kubevirt
  repo: kubevirt
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kustomize.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kustomize
description: Customization of kubernetes YAML configurations
source: !Github
  owner: kubernetes-sigs
  repo: kustomize
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/kuttl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: kuttl
description: KUbernetes Test TooL (kuttl)
source: !Github
  owner: kudobuilder
  repo: kuttl
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates:
  - kubectl-kuttl_{version}_linux_armv6
  - |
    kuttl_{version}_linux_armv6.tar.gz
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/linkerd2-edge.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: linkerd2-edge
description: Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x.
source: !Github
  owner: linkerd
  repo: linkerd2
targets:
- !LinuxAmd64
  artifact_templates:
  - linkerd2-cli-edge-{version}-linux-amd64
  executable_mappings:
    linkerd2-cli-edge-{version}-linux-amd64: linkerd2-edge
  tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
- !LinuxArm64
  artifact_templates:
  - linkerd2-cli-edge-{version}-linux-arm64
  executable_mappings:
    linkerd2-cli-edge-{version}-linux-arm64: linkerd2-edge
  tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
- !MacOSAmd64
  artifact_templates:
  - linkerd2-cli-edge-{version}-darwin
  executable_mappings:
    linkerd2-cli-edge-{version}-darwin: linkerd2-edge
  tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
- !WindowsAmd64
  artifact_templates:
  - linkerd2-cli-edge-{version}-windows.exe
  executable_mappings:
    linkerd2-cli-edge-{version}-windows.exe: linkerd2-edge.exe
  tag_version_regex_template: ^edge-(\d+.\d+.\d+)$
```

## File: `generated-v1/packages/linkerd2-stable.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: linkerd2-stable
description: Ultralight, security-first service mesh for Kubernetes. Main repo for Linkerd 2.x.
source: !Github
  owner: linkerd
  repo: linkerd2
targets:
- !LinuxAmd64
  artifact_templates:
  - linkerd2-cli-stable-{version}-linux-amd64
  executable_mappings:
    linkerd2-cli-stable-{version}-linux-amd64: linkerd2-stable
  tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
- !LinuxArm64
  artifact_templates:
  - linkerd2-cli-stable-{version}-linux-arm64
  executable_mappings:
    linkerd2-cli-stable-{version}-linux-arm64: linkerd2-stable
  tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
- !MacOSAmd64
  artifact_templates:
  - linkerd2-cli-stable-{version}-darwin
  executable_mappings:
    linkerd2-cli-stable-{version}-darwin: linkerd2-stable
  tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
- !WindowsAmd64
  artifact_templates:
  - linkerd2-cli-stable-{version}-windows.exe
  executable_mappings:
    linkerd2-cli-stable-{version}-windows.exe: linkerd2-stable.exe
  tag_version_regex_template: ^stable-(\d+.\d+.\d+)$
```

## File: `generated-v1/packages/loc.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: loc
description: Count lines of code quickly.
source: !Github
  owner: cgag
  repo: loc
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/local-ai.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: local-ai
description: ':robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more models architectures. Features: Generate Text, Audio, Video, Images, Voice Cloning, Distributed, P2P inference'
source: !Github
  owner: mudler
  repo: LocalAI
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/lsd.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: lsd
description: The next gen ls command
source: !Github
  owner: lsd-rs
  repo: lsd
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/minikube.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: minikube
description: Run Kubernetes locally
source: !Github
  owner: kubernetes
  repo: minikube
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/mkcert.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: mkcert
description: A simple zero-config tool to make locally trusted development certificates with any names you'd like.
source: !Github
  owner: FiloSottile
  repo: mkcert
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/nat.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: nat
description: '`ls` alternative with useful info and a splash of color 🎨'
source: !Github
  owner: willdoescode
  repo: nat
targets:
- !MacOSAmd64
  artifact_templates:
  - natls_osx_binary
```

## File: `generated-v1/packages/natscli.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: natscli
description: The NATS Command Line Interface
source: !Github
  owner: nats-io
  repo: natscli
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/navi.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: navi
description: An interactive cheatsheet tool for the command-line
source: !Github
  owner: denisidoro
  repo: navi
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates:
  - navi-v{version}-aarch64-unknown-linux-gnu.tar.gz
- !LinuxArm
  artifact_templates:
  - navi-v{version}-armv7-unknown-linux-musleabihf.tar.gz
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/nerdctl.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: nerdctl
description: contaiNERD CTL - Docker-compatible CLI for containerd, with support for Compose, Rootless, eStargz, OCIcrypt, IPFS, ...
source: !Github
  owner: containerd
  repo: nerdctl
targets:
- !LinuxAmd64
  artifact_templates:
  - nerdctl-{version}-linux-amd64.tar.gz
- !LinuxArm64
  artifact_templates:
  - nerdctl-{version}-linux-arm64.tar.gz
- !LinuxArm
  artifact_templates:
  - nerdctl-{version}-linux-arm-v7.tar.gz
```

## File: `generated-v1/packages/node.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: node
description: Node.js JavaScript runtime ✨🐢🚀✨
source: !Github
  owner: nodejs
  repo: node
targets:
- !LinuxAmd64
  artifact_templates:
  - https://nodejs.org/dist/v{version}/node-v{version}-linux-x64.tar.xz
- !LinuxArm64
  artifact_templates:
  - https://nodejs.org/dist/v{version}/node-v{version}-linux-arm64.tar.xz
- !MacOSAmd64
  artifact_templates:
  - https://nodejs.org/dist/v{version}/node-v{version}-darwin-x64.tar.gz
- !MacOSArm64
  artifact_templates:
  - https://nodejs.org/dist/v{version}/node-v{version}-darwin-arm64.tar.gz
- !WindowsAmd64
  artifact_templates:
  - https://nodejs.org/dist/v{version}/node-v{version}-win-x64.zip
```

## File: `generated-v1/packages/norouter.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: norouter
description: 'NoRouter: IP-over-Stdio. The easiest multi-host & multi-cloud networking ever. No root privilege is required. '
source: !Github
  owner: norouter
  repo: norouter
targets:
- !LinuxAmd64
  artifact_templates:
  - norouter-Linux-x86_64.tgz
- !LinuxArm64
  artifact_templates:
  - norouter-Linux-aarch64.tgz
- !MacOSAmd64
  artifact_templates:
  - norouter-Darwin-x86_64.tgz
- !WindowsAmd64
  artifact_templates:
  - norouter-Windows-x64.zip
```

## File: `generated-v1/packages/nushell.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: nushell
description: A new type of shell
source: !Github
  owner: nushell
  repo: nushell
targets:
- !LinuxAmd64
  artifact_templates:
  - nu-{version}-x86_64-unknown-linux-gnu.tar.gz
  - nu-{version}-x86_64-unknown-linux-musl.tar.gz
- !LinuxArm64
  artifact_templates:
  - nu-{version}-aarch64-unknown-linux-gnu.tar.gz
  - nu-{version}-aarch64-unknown-linux-musl.tar.gz
- !MacOSAmd64
  artifact_templates:
  - nu-{version}-x86_64-apple-darwin.tar.gz
- !MacOSArm64
  artifact_templates:
  - nu-{version}-aarch64-apple-darwin.tar.gz
- !WindowsAmd64
  artifact_templates:
  - nu-{version}-x86_64-pc-windows-msvc.zip
```

## File: `generated-v1/packages/octant.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: octant
description: Highly extensible platform for developers to better understand the complexity of Kubernetes clusters.
source: !Github
  owner: vmware-tanzu
  repo: octant
targets:
- !LinuxAmd64
  artifact_templates:
  - octant_{version}_Linux-64bit.tar.gz
- !LinuxArm64
  artifact_templates:
  - octant_{version}_Linux-arm64.tar.gz
- !MacOSAmd64
  artifact_templates:
  - octant_{version}_macOS-64bit.tar.gz
- !WindowsAmd64
  artifact_templates:
  - octant_{version}_Windows-64bit.tar.gz
```

## File: `generated-v1/packages/okteto.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: okteto
description: Develop your applications directly in your Kubernetes Cluster
source: !Github
  owner: okteto
  repo: okteto
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates:
  - okteto.exe
```

## File: `generated-v1/packages/ollama.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: ollama
description: Get up and running with Llama 3.3, DeepSeek-R1, Phi-4, Gemma 2, and other large language models.
source: !Github
  owner: ollama
  repo: ollama
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/onefetch.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: onefetch
description: Command-line Git information tool
source: !Github
  owner: o2sh
  repo: onefetch
targets:
- !LinuxAmd64
  artifact_templates:
  - onefetch-linux.tar.gz
- !MacOSAmd64
  artifact_templates:
  - onefetch-mac.tar.gz
- !WindowsAmd64
  artifact_templates:
  - onefetch-win.tar.gz
```

## File: `generated-v1/packages/opa.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: opa
description: Open Policy Agent (OPA) is an open source, general-purpose policy engine.
source: !Github
  owner: open-policy-agent
  repo: opa
targets:
- !LinuxAmd64
  artifact_templates:
  - opa_linux_amd64
- !MacOSAmd64
  artifact_templates:
  - opa_darwin_amd64
- !WindowsAmd64
  artifact_templates:
  - opa_windows_amd64.exe
```

## File: `generated-v1/packages/opentofu.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: opentofu
description: OpenTofu lets you declaratively manage your cloud infrastructure.
source: !Github
  owner: opentofu
  repo: opentofu
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/oras.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: oras
description: OCI registry client - managing content like artifacts, images, packages
source: !Github
  owner: oras-project
  repo: oras
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/pack.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: pack
description: CLI for building apps using Cloud Native Buildpacks
source: !Github
  owner: buildpacks
  repo: pack
targets:
- !LinuxAmd64
  artifact_templates:
  - pack-v{version}-linux.tgz
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates:
  - pack-v{version}-macos.tgz
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates:
  - pack-v{version}-windows.zip
```

## File: `generated-v1/packages/packer.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: packer
description: Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
source: !Github
  owner: hashicorp
  repo: packer
targets:
- !LinuxAmd64
  artifact_templates:
  - https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_amd64.zip
- !LinuxArm64
  artifact_templates:
  - https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_arm64.zip
- !MacOSAmd64
  artifact_templates:
  - https://releases.hashicorp.com/packer/{version}/packer_{version}_darwin_amd64.zip
- !WindowsAmd64
  artifact_templates:
  - https://releases.hashicorp.com/packer/{version}/packer_{version}_windows_amd64.zip
```

## File: `generated-v1/packages/podman.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: podman
description: 'Podman: A tool for managing OCI containers and pods.'
source: !Github
  owner: containers
  repo: podman
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/powershell.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: powershell
description: PowerShell for every system!
source: !Github
  owner: PowerShell
  repo: PowerShell
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/procs.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: procs
description: A modern replacement for ps written in Rust
source: !Github
  owner: dalance
  repo: procs
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/protoc.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: protoc
description: Protocol Buffers - Google's data interchange format
source: !Github
  owner: protocolbuffers
  repo: protobuf
targets:
- !LinuxAmd64
  artifact_templates:
  - protoc-{version}-linux-x86_64.zip
- !LinuxArm64
  artifact_templates:
  - protoc-{version}-linux-aarch_64.zip
- !MacOSAmd64
  artifact_templates:
  - protoc-{version}-osx-x86_64.zip
- !MacOSArm64
  artifact_templates:
  - protoc-{version}-osx-universal_binary.zip
- !WindowsAmd64
  artifact_templates:
  - protoc-{version}-win64.zip
```

## File: `generated-v1/packages/pueue.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: pueue
description: ':stars: Manage your shell commands.'
source: !Github
  owner: Nukesor
  repo: pueue
targets:
- !LinuxAmd64
  artifact_templates:
  - pueue-linux-x86_64
  - pueued-linux-x86_64
- !LinuxArm64
  artifact_templates:
  - pueue-linux-aarch64
  - pueued-linux-aarch64
- !MacOSAmd64
  artifact_templates:
  - pueue-macos-x86_64
  - pueued-macos-x86_64
- !WindowsAmd64
  artifact_templates:
  - pueue-windows-x86_64.exe
  - pueued-windows-x86_64.exe
```

## File: `generated-v1/packages/pulumi.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: pulumi
description: Pulumi - Infrastructure as Code in any programming language 🚀
source: !Github
  owner: pulumi
  repo: pulumi
targets:
- !LinuxAmd64
  artifact_templates:
  - https://get.pulumi.com/releases/sdk/pulumi-v{version}-linux-x64.tar.gz
- !MacOSAmd64
  artifact_templates:
  - https://get.pulumi.com/releases/sdk/pulumi-v{version}-darwin-x64.tar.gz
- !WindowsAmd64
  artifact_templates:
  - https://get.pulumi.com/releases/sdk/pulumi-v{version}-windows-x64.zip
```

## File: `generated-v1/packages/rclone.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: rclone
description: '"rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files'
source: !Github
  owner: rclone
  repo: rclone
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/regclient.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: regclient
description: Docker and OCI Registry Client in Go and tooling using those libraries.
source: !Github
  owner: regclient
  repo: regclient
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/ripgrep.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: ripgrep
description: ripgrep recursively searches directories for a regex pattern while respecting your gitignore
source: !Github
  owner: BurntSushi
  repo: ripgrep
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/rke2.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: rke2
source: !Github
  owner: rancher
  repo: rke2
targets:
- !LinuxAmd64
  artifact_templates:
  - rke2.linux-amd64.tar.gz
- !LinuxArm64
  artifact_templates:
  - rke2.linux-arm64.tar.gz
- !WindowsAmd64
  artifact_templates:
  - rke2.windows-amd64.tar.gz
```

## File: `generated-v1/packages/sad.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: sad
description: CLI search and replace | Space Age seD
source: !Github
  owner: ms-jpq
  repo: sad
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/saml2aws.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: saml2aws
description: CLI tool which enables you to login and retrieve AWS temporary credentials using a SAML IDP
source: !Github
  owner: Versent
  repo: saml2aws
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/sd.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: sd
description: Intuitive find & replace CLI (sed alternative)
source: !Github
  owner: chmln
  repo: sd
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/shadowsocks.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: shadowsocks
description: A Rust port of shadowsocks
source: !Github
  owner: shadowsocks
  repo: shadowsocks-rust
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/skaffold.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: skaffold
description: Easy and Repeatable Kubernetes Development
source: !Github
  owner: GoogleContainerTools
  repo: skaffold
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/skim.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: skim
description: Fuzzy Finder in rust!
source: !Github
  owner: skim-rs
  repo: skim
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/solidity.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: solidity
description: Solidity, the Smart Contract Programming Language
source: !Github
  owner: ethereum
  repo: solidity
targets:
- !LinuxAmd64
  artifact_templates:
  - solc-static-linux
- !MacOSAmd64
  artifact_templates:
  - solc-macos
- !WindowsAmd64
  artifact_templates:
  - solc-windows.exe
```

## File: `generated-v1/packages/sonobuoy.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: sonobuoy
description: Sonobuoy is a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster by running a set of Kubernetes conformance tests and other plugins in an accessible and non-destructive manner.
source: !Github
  owner: vmware-tanzu
  repo: sonobuoy
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/starship.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: starship
description: ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell!
source: !Github
  owner: starship
  repo: starship
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/stern.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: stern
description: ⎈ Multi pod and container log tailing for Kubernetes -- Friendly fork of https://github.com/wercker/stern
source: !Github
  owner: stern
  repo: stern
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/syncthing.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: syncthing
description: Open Source Continuous File Synchronization
source: !Github
  owner: syncthing
  repo: syncthing
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/tealdeer.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: tealdeer
description: A very fast implementation of tldr in Rust.
source: !Github
  owner: tealdeer-rs
  repo: tealdeer
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/termshark.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: termshark
description: A terminal UI for tshark, inspired by Wireshark
source: !Github
  owner: gcla
  repo: termshark
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/terraform.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: terraform
description: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.
source: !Github
  owner: hashicorp
  repo: terraform
targets:
- !LinuxAmd64
  artifact_templates:
  - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip
- !LinuxArm64
  artifact_templates:
  - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_arm64.zip
- !MacOSAmd64
  artifact_templates:
  - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_darwin_amd64.zip
- !MacOSArm64
  artifact_templates:
  - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_darwin_arm64.zip
- !WindowsAmd64
  artifact_templates:
  - https://releases.hashicorp.com/terraform/{version}/terraform_{version}_windows_amd64.zip
```

## File: `generated-v1/packages/terrascan.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: terrascan
description: Detect compliance and security violations across Infrastructure as Code to mitigate risk before provisioning cloud native infrastructure.
source: !Github
  owner: tenable
  repo: terrascan
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/tilt.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: tilt
description: Define your dev environment as code. For microservice apps on Kubernetes.
source: !Github
  owner: tilt-dev
  repo: tilt
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/tokei.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: tokei
description: Count your code, quickly.
source: !Github
  owner: XAMPPRocky
  repo: tokei
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/tracee.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: tracee
description: Linux Runtime Security and Forensics using eBPF
source: !Github
  owner: aquasecurity
  repo: tracee
targets:
- !LinuxAmd64
  artifact_templates:
  - tracee-x86_64.v{version}.tar.gz
  scan_dirs:
  - dist
- !LinuxArm64
  artifact_templates:
  - tracee-aarch64.v{version}.tar.gz
  scan_dirs:
  - dist
```

## File: `generated-v1/packages/traefik.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: traefik
description: The Cloud Native Application Proxy
source: !Github
  owner: traefik
  repo: traefik
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/trivy.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: trivy
description: Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more
source: !Github
  owner: aquasecurity
  repo: trivy
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/typescript.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: typescript
description: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.
source: !Github
  owner: microsoft
  repo: TypeScript
targets:
- !LinuxAmd64
  artifact_templates:
  - typescript-{version}.tgz
```

## File: `generated-v1/packages/typos.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: typos
description: Source code spell checker
source: !Github
  owner: crate-ci
  repo: typos
targets:
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/vegeta.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: vegeta
description: HTTP load testing tool and library. It's over 9000!
source: !Github
  owner: tsenart
  repo: vegeta
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/velero.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: velero
description: Backup and migrate Kubernetes applications and their persistent volumes
source: !Github
  owner: vmware-tanzu
  repo: velero
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/viddy.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: viddy
description: 👀 A modern watch command. Time machine and pager etc.
source: !Github
  owner: sachaos
  repo: viddy
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/volta.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: volta
description: 'Volta: JS Toolchains as Code. ⚡'
source: !Github
  owner: volta-cli
  repo: volta
targets:
- !LinuxAmd64
  artifact_templates:
  - volta-{version}-linux.tar.gz
- !MacOSAmd64
  artifact_templates:
  - volta-{version}-macos.tar.gz
- !WindowsAmd64
  artifact_templates:
  - volta-{version}-windows.zip
```

## File: `generated-v1/packages/wabt.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: wabt
description: The WebAssembly Binary Toolkit
source: !Github
  owner: WebAssembly
  repo: wabt
targets:
- !LinuxAmd64
  artifact_templates:
  - wabt-{version}-ubuntu.tar.gz
- !MacOSAmd64
  artifact_templates:
  - wabt-{version}-macos-12.tar.gz
- !MacOSArm64
  artifact_templates:
  - wabt-{version}-macos-14.tar.gz
- !WindowsAmd64
  artifact_templates:
  - wabt-{version}-windows.tar.gz
```

## File: `generated-v1/packages/wasmer.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: wasmer
description: 🚀 Fast, secure, lightweight containers based on WebAssembly
source: !Github
  owner: wasmerio
  repo: wasmer
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/wasmtime.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: wasmtime
description: A lightweight WebAssembly runtime that is fast, secure, and standards-compliant
source: !Github
  owner: bytecodealliance
  repo: wasmtime
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/wstunnel.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: wstunnel
description: 'Tunnel all your traffic over Websocket or HTTP2 - Bypass firewalls/DPI - Static binary available '
source: !Github
  owner: erebe
  repo: wstunnel
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/xh.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: xh
description: Friendly and fast tool for sending HTTP requests
source: !Github
  owner: ducaale
  repo: xh
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/yq.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: yq
description: yq is a portable command-line YAML, JSON, XML, CSV, TOML  and properties processor
source: !Github
  owner: mikefarah
  repo: yq
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/zellij.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: zellij
description: A terminal workspace with batteries included
source: !Github
  owner: zellij-org
  repo: zellij
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
```

## File: `generated-v1/packages/zola.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: zola
description: A fast static site generator in a single binary with everything built-in. https://www.getzola.org
source: !Github
  owner: getzola
  repo: zola
targets:
- !LinuxAmd64
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `generated-v1/packages/zoxide.yaml`
```yaml
# THIS IS GENERATED BY huber-generator.
name: zoxide
description: A smarter cd command. Supports all major shells.
source: !Github
  owner: ajeetdsouza
  repo: zoxide
targets:
- !LinuxAmd64
  artifact_templates: []
- !LinuxArm64
  artifact_templates: []
- !LinuxArm
  artifact_templates: []
- !MacOSAmd64
  artifact_templates: []
- !MacOSArm64
  artifact_templates: []
- !WindowsAmd64
  artifact_templates: []
```

## File: `hack/add-huber-bin-to-env.sh`
```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

export_statement="export PATH=\$HOME/.huber/bin:\$PATH"

shells=(bashrc zshrc)
for s in "${shells[@]}"; do
  if [ -f "$HOME"/."$s" ] && ! grep -Fxq "$export_statement" "$HOME"/."$s"; then
    echo "$export_statement" >>"$HOME"/."$s"
  fi
done
```

## File: `hack/generate-huber-packages.sh`
```bash
#!/usr/bin/env bash

set -o errexit
set -o pipefail
#set -o nounset
#set -o xtrace

readlink=readlink
if command -v greadlink &>/dev/null; then
  readlink=greadlink
fi

PROJECT_DIR=$($readlink -f "$(dirname "${BASH_SOURCE[0]}")/..")
PKG_INDEXES_MD="${PROJECT_DIR}"/docs/src/contributing/huber-managed-packages.md
PKG_INDEXES_CONTENT=${1:-}

if [ -z "$PKG_INDEXES_CONTENT" ]; then
  echo "No generated package lists from \`huber search\`, so it was unable to generate ${PKG_INDEXES_MD}" >>/dev/stderr
  exit 1
fi

content=$(
  cat <<'EOF'
# Huber Managed Packages

This package list is generated by `huber search` using the default Huber package repository.
To add a new package, please follow the instructions in [Add a New Package](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/commands/project-management/add-package.md).

```console
{value}
```
EOF
)

content=${content/\{value\}/$PKG_INDEXES_CONTENT}
echo "$content" >"$PKG_INDEXES_MD"
```

## File: `hack/install.sh`
```bash
#!/usr/bin/env sh

set -o errexit
set -o nounset
set -o xtrace

HUBER_VERSION=${HUBER_VERSION:-latest}

get_latest_release() {
  curl -sfSL "https://api.github.com/repos/innobead/huber/releases/$HUBER_VERSION" |
    grep '"tag_name":' |
    sed -E 's/.*"([^"]+)".*/\1/'
}

os=$(uname)
arch=$(uname -m)
filename="huber-linux-amd64"

case $os in
"Linux")
  case $arch in
  "aarch64")
    if [ -e "/lib/ld-musl-x86_64.so.1" ]; then
      filename="huber-aarch64-unknown-linux-musl"
    else
      filename="huber-aarch64-unknown-linux-gnu"
    fi
    ;;
  "armv7l" | "arm")
    if [ -e "/lib/ld-musl-x86_64.so.1" ]; then
      filename="huber-arm-unknown-linux-musleabihf"
    else
      filename="huber-arm-unknown-linux-gnueabihf"
    fi
    ;;
  "x86_64" | "amd64")
    if [ -e "/lib/ld-musl-x86_64.so.1" ]; then
      filename="huber-x86_64-unknown-linux-musl"
    else
      filename="huber-x86_64-unknown-linux-gnu"
    fi
    ;;
  *)
    echo "$os:$arch is not supported" >/dev/stderr
    exit 1
    ;;
  esac
  ;;
"Darwin")
  case $arch in
  "arm64")
    filename="huber-aarch64-apple-darwin"
    ;;
  "x86_64")
    filename="huber-x86_64-apple-darwin"
    ;;
  *)
    echo "$os:$arch is not supported" >/dev/stderr
    exit 1
    ;;
  esac
  ;;
*)
  echo "$os:$arch is not supported" >/dev/stderr
  exit 1
  ;;
esac

# shellcheck disable=SC2046
curl -sfSLO "https://github.com/innobead/huber/releases/download/$(get_latest_release)/$filename" &&
  chmod +x $filename &&
  mkdir -p ~/.huber/bin &&
  mv $filename ~/.huber/bin/huber

export_statement="export PATH=\$HOME/.huber/bin:\$PATH"
if ! grep -Fxq "$export_statement" ~/.bashrc; then
  echo "$export_statement" >>~/.bashrc
fi

cat <<EOF
The installation script has updated the \$PATH environment variable in $HOME/.bashrc.
Please restart the shell or source again to make it take effect.

If you use other shell, please update the \$PATH environment variable accordingly.
EOF
```

## File: `hack/setup-dev.sh`
```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

install_linux_deps() {
  if [[ $(command -v zypper) ]]; then
    sudo zypper install -y cross-aarch64-gcc14 cross-arm-linux-gnueabi-gcc
  elif [[ $(command -v apt) ]]; then
    sudo apt update
    sudo DEBIAN_FRONTEND=noninteractive apt install -y gcc-aarch64-linux-gnu gcc-arm-linux-gnueabihf
  else
    echo "Only openSUSE, Ubuntu supported" >/dev/stderr
    exit 1
  fi

  if [[ -z $(command -v just 2>/dev/null) ]]; then
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
  fi
}

install_rust_deps() {
  if [[ -z $(command -v cargo 2>/dev/null) ]]; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    rustup toolchain install nightly
    source "$HOME"/.cargo/env
    cargo version
  fi

  export_statement="export PATH=\$HOME/.cargo/bin:\$PATH"
  if ! grep -Fxq "$export_statement" ~/.bashrc; then
    echo "$export_statement" >>"$HOME"/.bashrc
  fi

  if [[ -f "$HOME"/.cargo/env ]]; then
    source "$HOME"/.cargo/env
  fi
}

if [ "$(uname)" == "Linux" ]; then
  install_linux_deps
fi
install_rust_deps
```

## File: `hack/windows/install.ps1`
```powershell
$tag = (Invoke-WebRequest "https://api.github.com/repos/innobead/huber/releases/latest" | ConvertFrom-Json).tag_name
$url = "https://github.com/innobead/huber/releases/download/$tag/huber-x86_64-pc-windows-gnu.exe"

Write-Host "Downloading the latest huber release: $tag from $url"

New-Item ~/.huber/bin -ItemType directory
Invoke-WebRequest -Uri $url -OutFile ~/.huber/bin/huber.exe
$path = (Resolve-Path ~/.huber/bin/huber.exe)

Write-Host "huber installed in $path!"
```

## File: `hack/windows/setup-dev.ps1`
```powershell
function install_rust_dependencies {
  vcpkg integrate install

  if (!(Get-Command "cargo.exe" -ErrorAction SilentlyContinue))
  {
    Invoke-WebRequest -Uri "https://win.rustup.rs/" -OutFile "rustup-init.exe"
    .\rustup-init.exe
    cargo version
  }
}

install_rust_dependencies
```

## File: `huber/Cargo.toml`
```
[package]
name = "huber"
version.workspace = true
description.workspace = true
authors.workspace = true
edition.workspace = true
keywords.workspace = true
categories.workspace = true
homepage.workspace = true
repository.workspace = true
readme.workspace = true
license-file.workspace = true
publish = true

[[bin]]
name = "huber"
path = "src/bin/huber.rs"

[build-dependencies]
chrono.workspace = true

[dev-dependencies]
assert_cmd = "2.0.16"
sequential-test = "0.2.4"
tempfile = "3.15.0"

[dependencies]
anyhow.workspace = true
async-trait.workspace = true
better-panic.workspace = true
chrono.workspace = true
clap.workspace = true
clap_complete.workspace = true
dirs.workspace = true
env_logger.workspace = true
filepath.workspace = true
flate2.workspace = true
fs2.workspace = true
fs_extra.workspace = true
futures.workspace = true
git2.workspace = true
huber-procmacro.workspace = true
is_executable.workspace = true
lazy_static.workspace = true
libcli-rs.workspace = true
log.workspace = true
maplit.workspace = true
octocrab.workspace = true
rayon.workspace = true
regex.workspace = true
reqwest.workspace = true
scopeguard.workspace = true
semver.workspace = true
serde.workspace = true
serde_yaml.workspace = true
simpledi-rs.workspace = true
symlink.workspace = true
tar.workspace = true
thiserror.workspace = true
tokio.workspace = true
url.workspace = true
urlencoding.workspace = true
xz2.workspace = true
zip.workspace = true
```

## File: `huber/build.rs`
```rust
use std::process::Command;

use chrono::prelude::*;

fn main() {
    let short_version = command("git", vec!["describe", "--tags", "--dirty"])
        .unwrap_or_else(|| format!("v{}", env!("CARGO_PKG_VERSION")));

    let commit = command("git", vec!["rev-parse", "--short", "HEAD"]).unwrap_or_default();
    let timestamp = Utc::now().format("%Y%m%d%H%M%S").to_string();
    let version = format!("{} Commit: {}-{}", short_version, commit, timestamp);

    println!("cargo:rustc-env=HUBER_VERSION={}", short_version);
    println!("cargo:rustc-env=HUBER_LONG_VERSION={}", version);
}

fn command(cmd: &str, args: impl IntoIterator<Item = &'static str>) -> Option<String> {
    Command::new(cmd)
        .args(args)
        .output()
        .ok()
        .and_then(|output| {
            if output.status.success() {
                return Some(output.stdout);
            }
            None
        })
        .and_then(|bytes| String::from_utf8(bytes).ok())
        .map(|it| it.trim().to_string())
}
```

## File: `huber/src/compress.rs`
```rust
use std::fs::File;
use std::io;
use std::io::BufReader;
use std::path::Path;

use flate2::read::GzDecoder;
use tar::Archive;
use xz2::read::XzDecoder;
use zip::ZipArchive;

use crate::fs::set_executable_permission;

pub fn uncompress_archive(file: &Path, extract_dir: &Path, ext: &str) -> anyhow::Result<()> {
    match ext {
        "zip" => {
            unzip(file, extract_dir)?;
        }
        "tar" => {
            untar(file, extract_dir)?;
        }
        "tar.gz" | "tgz" => {
            untar_gz(file, extract_dir)?;
        }
        "tar.xz" => {
            untar_xz(file, extract_dir)?;
        }
        "gz" => {
            ungz(file, extract_dir)?;
        }
        _ => {
            return Err(anyhow::anyhow!("Unsupported archive format: {}", ext));
        }
    }

    Ok(())
}

fn untar_xz(file: &Path, extract_dir: &Path) -> anyhow::Result<()> {
    let tar_xz = File::open(file)?;
    let tar = XzDecoder::new(BufReader::new(tar_xz));
    let mut archive = Archive::new(tar);

    Ok(archive.unpack(extract_dir)?)
}

fn untar_gz(file: &Path, extract_dir: &Path) -> anyhow::Result<()> {
    let tar_gz = File::open(file)?;
    let tar = GzDecoder::new(BufReader::new(tar_gz));
    let mut archive = Archive::new(tar);

    Ok(archive.unpack(extract_dir)?)
}

fn untar(file: &Path, extract_dir: &Path) -> anyhow::Result<()> {
    let tar_file = File::open(file)?;
    let tar = BufReader::new(tar_file);
    let mut archive = Archive::new(tar);

    Ok(archive.unpack(extract_dir)?)
}

fn unzip(file: &Path, extract_dir: &Path) -> anyhow::Result<()> {
    let file = File::open(file)?;

    let mut reader = ZipArchive::new(BufReader::new(file))?;
    reader.extract(extract_dir)?;

    Ok(())
}

fn ungz(file: &Path, extract_dir: &Path) -> anyhow::Result<()> {
    let gz = File::open(file)?;
    let mut gz = GzDecoder::new(BufReader::new(gz));

    let outfile_path = extract_dir.join(
        file.file_name()
            .unwrap_or_default()
            .to_string_lossy()
            .replace(".gz", ""),
    );
    let mut out_file = File::create(&outfile_path)?;
    io::copy(&mut gz, &mut out_file)?;
    set_executable_permission(&outfile_path)?;

    Ok(())
}
```

## File: `huber/src/error.rs`
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum HuberError {
    #[error("Config not found: {0:?}")]
    ConfigNotFound(String),

    #[error("Package not found: {0:?}")]
    PackageNotFound(String),

    #[error("Package not installed: {0:?}")]
    PackageNotInstalled(String),

    #[error("Repository already exists: {0:?}")]
    RepoAlreadyExist(String),

    #[error("Repository not found: {0:?}")]
    RepoNotFound(String),

    #[error("Package unable to update")]
    PackageUnableToUpdate(#[source] anyhow::Error),
}
```

## File: `huber/src/fs.rs`
```rust
use std::fs;
use std::path::{Path, PathBuf};

use log::debug;
use regex::Regex;

pub fn dir(dir: PathBuf) -> anyhow::Result<PathBuf> {
    if !dir.exists() {
        let _ = fs::remove_dir_all(dir.as_path());
        fs::create_dir_all(dir.as_path())?;
    }

    Ok(dir)
}

#[cfg(not(target_os = "windows"))]
pub fn set_executable_permission(path: &Path) -> anyhow::Result<()> {
    debug!("Making {:?} as executable", path);

    use std::os::unix::fs::PermissionsExt;
    fs::set_permissions(path, fs::Permissions::from_mode(0o755))?;
    Ok(())
}

#[cfg(target_os = "windows")]
pub fn set_executable_permission(path: &Path) -> anyhow::Result<()> {
    debug!("Unsupported making {:?} as executable on Windows", path);
    Ok(())
}

pub fn is_empty_dir<P: AsRef<Path>>(path: P) -> bool {
    path.as_ref()
        .read_dir()
        .map(|mut it| it.next().is_none())
        .unwrap_or(false)
}

pub fn has_suffix(s: &str) -> bool {
    if cfg!(target_os = "windows") && s.ends_with(".exe") {
        return false;
    }

    Regex::new(r".*\.\S+$").unwrap().is_match(s)
}

#[cfg(test)]
mod test {
    use crate::fs::{has_suffix, is_empty_dir};

    #[test]
    fn test_is_empty_dir() {
        let dir = tempfile::tempdir().unwrap();
        assert!(is_empty_dir(dir.path()));
        assert!(!is_empty_dir("/tmp"));
    }

    #[test]
    fn test_has_suffix() {
        assert!(has_suffix("file.txt"));
        if cfg!(target_os = "windows") {
            assert!(!has_suffix("file.exe"));
        } else {
            assert!(has_suffix("file.exe"));
        }
        assert!(!has_suffix("file"));
    }
}
```

## File: `huber/src/gh.rs`
```rust
use std::fs::remove_dir_all;
use std::path::{Path, PathBuf};

use anyhow::anyhow;
use async_trait::async_trait;
use git2::{Cred, ErrorCode, FetchOptions, RemoteCallbacks, Repository};
use log::debug;
use octocrab::auth::Auth;
use octocrab::{Octocrab, OctocrabBuilder};

use crate::fs::is_empty_dir;
use crate::model::package::Package;
use crate::model::release::Release;

#[async_trait]
pub trait GithubClientTrait {
    async fn get_latest_release(
        &self,
        owner: &str,
        repo: &str,
        pkg: &Package,
    ) -> anyhow::Result<Release>;
    async fn get_release(
        &self,
        owner: &str,
        repo: &str,
        tag: &str,
        pkg: &Package,
    ) -> anyhow::Result<Release>;
    async fn get_releases(
        &self,
        owner: &str,
        repo: &str,
        pkg: &Package,
    ) -> anyhow::Result<Vec<Release>>;
    async fn clone<P: AsRef<Path> + Send + Sync>(
        &self,
        owner: &str,
        repo: &str,
        dir: P,
    ) -> anyhow::Result<()>;
}

pub struct GithubClient {
    octocrab: Octocrab,
    ssh_key: Option<PathBuf>,
}

unsafe impl Send for GithubClient {}

unsafe impl Sync for GithubClient {}

impl GithubClient {
    pub fn new(auth: Auth, ssh_key: Option<PathBuf>) -> Self {
        Self {
            octocrab: {
                let builder = OctocrabBuilder::default();
                match auth {
                    Auth::PersonalToken(token) => builder.personal_token(token),
                    Auth::UserAccessToken(token) => builder.user_access_token(token),
                    _ => {
                        debug!("Use github client with no auth");
                        builder
                    }
                }
                .build()
                .expect("Failed to build GitHub client")
            },
            ssh_key,
        }
    }

    fn clone_fresh<P: AsRef<Path> + Send>(&self, url: &str, dir: P) -> anyhow::Result<Repository> {
        let clone_repo_by_key = |key: &PathBuf| -> anyhow::Result<Repository> {
            if key.exists() {
                debug!("Cloning huber repo via SSH");

                // Prepare builder.
                let fetch_options = self.create_git_fetch_options(key.clone())?;
                let mut builder = git2::build::RepoBuilder::new();
                builder.fetch_options(fetch_options);

                return Ok(builder.clone(url, dir.as_ref())?);
            }

            Err(anyhow!("The configured github key not found, {:?}", key))
        };

        if let Some(key) = self.ssh_key.as_ref() {
            return clone_repo_by_key(key);
        }

        debug!("Cloning huber repo via https");
        //Note: if encountering authentication required, probably hit this issue https://github.com/rust-lang/git2-rs/issues/463
        match Repository::clone(url, &dir) {
            Err(err) => {
                if err.code() == ErrorCode::GenericError
                    && err
                        .message()
                        .contains("authentication required but no callback set")
                {
                    debug!("Failed to clone huber repo due to the SSH key required as per the user git config");
                    debug!("Using the default user key path to try cloning huber repo again");

                    let p = dirs::home_dir().unwrap().join(".ssh").join("id_rsa");
                    clone_repo_by_key(&p)
                } else {
                    Err(anyhow!(err))
                }
            }

            Ok(repo) => Ok(repo),
        }
    }

    fn fetch_merge_repo<P: AsRef<Path>>(&self, dir: P) -> anyhow::Result<()> {
        debug!("Merging huber repo update");

        let mut fetch_options = if let Some(key) = self.ssh_key.as_ref() {
            if key.exists() {
                debug!("Fetching huber repo via SSH");
                Some(self.create_git_fetch_options(key.clone())?)
            } else {
                None
            }
        } else {
            None
        };

        let repo = Repository::open(&dir)?;

        // fetch the origin
        let mut remote = repo.find_remote("origin")?;
        remote.fetch(&["main"], fetch_options.as_mut(), None)?;
        let fetch_head = repo.find_reference("FETCH_HEAD")?;
        let commit = repo.reference_to_annotated_commit(&fetch_head)?;

        // merge local, and checkout
        let reference_name = format!("refs/heads/{}", "main");
        let mut reference = repo.find_reference(&reference_name)?;
        let name = reference.name().expect("");
        repo.set_head(name)?;
        reference.set_target(commit.id(), "")?;

        Ok(repo.checkout_head(Some(git2::build::CheckoutBuilder::default().force()))?)
    }

    fn create_git_fetch_options<T: AsRef<Path> + 'static>(
        &self,
        key: T,
    ) -> anyhow::Result<FetchOptions> {
        let mut callbacks = RemoteCallbacks::new();
        callbacks.credentials(move |_url, username_from_url, _allowed_types| {
            Cred::ssh_key(username_from_url.unwrap(), None, key.as_ref(), None)
        });

        // Prepare fetch options.
        let mut fo = git2::FetchOptions::new();
        fo.remote_callbacks(callbacks);

        Ok(fo)
    }
}

#[async_trait]
impl GithubClientTrait for GithubClient {
    async fn get_latest_release(
        &self,
        owner: &str,
        repo: &str,
        pkg: &Package,
    ) -> anyhow::Result<Release> {
        debug!("Getting the latest release of package {}", &pkg);

        let release = if pkg.target()?.tag_version_regex_template.is_none() {
            self.octocrab
                .repos(owner, repo)
                .releases()
                .get_latest()
                .await?
        } else {
            self.octocrab.repos(owner, repo).releases().list().send().await?.into_iter().find(|it| {
                pkg.parse_version_from_tag_name(&it.tag_name).is_ok()
            }).ok_or(anyhow!("Failed to find the matched latest version based on tag_version_regex_template {:?}", pkg))?
        };

        let mut release = Release::from(release);

        release.name = pkg.name.clone();
        release.package.name = pkg.name.clone();
        release.package.source = pkg.source.clone();
        release.package.targets = pkg.targets.clone();
        release.package.version = Some(release.version.clone());

        Ok(release)
    }

    async fn get_release(
        &self,
        owner: &str,
        repo: &str,
        tag: &str,
        pkg: &Package,
    ) -> anyhow::Result<Release> {
        debug!("Getting the specific release of package {}/{}", &pkg, tag);

        let release = self
            .octocrab
            .repos(owner, repo)
            .releases()
            .get_by_tag(tag)
            .await?;
        let mut release = Release::from(release);

        release.name = pkg.name.clone();
        release.package.name = pkg.name.clone();
        release.package.source = pkg.source.clone();
        release.package.targets = pkg.targets.clone();
        release.package.version = Some(release.version.clone());

        Ok(release)
    }

    async fn get_releases(
        &self,
        owner: &str,
        repo: &str,
        pkg: &Package,
    ) -> anyhow::Result<Vec<Release>> {
        debug!("Getting all releases of package {}", &pkg);

        let releases = self
            .octocrab
            .repos(owner, repo)
            .releases()
            .list()
            .send()
            .await?;
        let releases = releases
            .into_iter()
            .map(|it| {
                let mut release = Release::from(it);

                release.name = pkg.name.clone();
                release.package.name = pkg.name.clone();
                release.package.source = pkg.source.clone();
                release.package.targets = pkg.targets.clone();
                release.package.release_kind = release.kind;

                release
            })
            .collect();

        Ok(releases)
    }

    async fn clone<P: AsRef<Path> + Send + Sync>(
        &self,
        owner: &str,
        repo: &str,
        dir: P,
    ) -> anyhow::Result<()> {
        debug!("Cloning huber github repo");

        let url = format!("https://github.com/{}/{}", owner, repo);

        if is_empty_dir(&dir) {
            self.clone_fresh(&url, &dir)?;
            return Ok(());
        }

        if let Err(e) = self.fetch_merge_repo(&dir) {
            debug!("Failed to fetch huber github repo, {:?}", e);

            let _ = remove_dir_all(&dir);
            self.clone_fresh(&url, &dir)?;
        }

        Ok(())
    }
}
```

## File: `huber/src/lib.rs`
```rust
pub mod cmd;
mod compress;
pub mod error;
pub mod fs;
mod gh;
pub mod log;
pub mod model;
mod os;
pub mod parse;
mod semver;
pub mod service;
```

## File: `huber/src/log.rs`
```rust
use std::str::FromStr;

use log::LevelFilter;

use crate::model::config::Config;

pub struct Logger;

impl Logger {
    pub fn init(config: &Config) -> anyhow::Result<()> {
        match LevelFilter::from_str(&config.log_level.to_uppercase())? {
            LevelFilter::Off => {
                env_logger::builder()
                    .filter_level(LevelFilter::Info)
                    .default_format()
                    .format_target(false)
                    .format_timestamp(None)
                    .try_init()?;
            }
            value => {
                env_logger::builder()
                    .filter_level(value)
                    .default_format()
                    .try_init()?;
            }
        }

        Ok(())
    }
}
```

## File: `huber/src/os.rs`
```rust
use std::cmp::Ordering;

use regex::Regex;

// https://github.com/golang/go/blob/master/src/go/build/syslist.go
const GO_OS_LIST: &str = "aix android darwin dragonfly freebsd hurd illumos ios js linux nacl \
netbsd openbsd plan9 solaris windows win zos macos osx";

const GO_ARCH_LIST: &str = "386 amd64 amd64p32 arm armbe arm64 arm64be ppc64 ppc64le mips \
mipsle mips64 mips64le mips64p32 mips64p32le ppc riscv riscv64 s390 s390x sparc sparc64 \
wasm x86_64 x64 aarch64 64bit";

const LIB_PATTERN_LIST: &str = r"unknown|latest|stable|gnu|musl|msvc|uclibc|gnueabihf|gnueabi|hardfloat|softfloat|thumb|thumbv6";

pub fn trim_os_arch_version(str: &str) -> String {
    let revert_sort = |x: &&str, y: &&str| -> Ordering { y.len().cmp(&x.len()) };

    let mut os_pattern: Vec<_> = GO_OS_LIST.split(" ").collect();
    os_pattern.sort_by(revert_sort);
    let os_pattern = os_pattern.join("|");

    let mut arch_pattern: Vec<_> = GO_ARCH_LIST.split(" ").collect();
    arch_pattern.sort_by(revert_sort);
    let arch_pattern = arch_pattern.join("|");

    let patterns = [
        Regex::new(r"(?i)[-_]*v?\d+.\d+.\d+[-_]*").unwrap(),
        Regex::new(&format!(r"(?i)[-_.]*({})[-_]*", os_pattern)).unwrap(),
        Regex::new(&format!(r"(?i)[-_.]*({})[-_]*", arch_pattern)).unwrap(),
        Regex::new(&format!(r"(?i)[-_.]*({})[-_]*", LIB_PATTERN_LIST)).unwrap(),
    ];

    let mut str = str.to_string();
    for pat in &patterns {
        if pat.is_match(&str) {
            str = pat.replace_all(&str, "").to_string();
        }
    }

    if cfg!(target_os = "windows") && !str.ends_with(".exe") {
        str += ".exe";
    }

    str
}

pub fn is_os_arch_match(os: &str, arch: &str, asset_url: &str) -> bool {
    let os = os.to_lowercase();
    let arch = arch.to_lowercase();
    let asset_url = asset_url.to_lowercase();

    let os_pattern = if os == "macos" {
        r"([-_.]|\b)(macos|darwin|apple|osx|mac)([-_.]?|\b)"
    } else if os == "windows" {
        r"([-_.]|\b)(windows|win)([-_.]?|\b)"
    } else {
        &format!(r"([-_.]?|\b){}([-_.]?|\b)", os)
    };
    if !Regex::new(os_pattern).unwrap().is_match(&asset_url) {
        return false;
    }

    let arch_pattern = match arch.as_str() {
        "x86_64" => r"([-_.]|\b)(x86_64|x64|amd64|64bit)([-_.]?|\b)",
        "arm" => r"\b(arm|arm32|armhf|armv7)\b",
        "aarch64" => r"([-_.]|\b)(aarch64|arm64)([-_.]?|\b)",
        _ => return false,
    };

    Regex::new(arch_pattern).unwrap().is_match(&asset_url)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_trim_os_arch_version() {
        let data = vec![
            ("name-linux-amd64", "name"),
            ("name-Linux-aarch64", "name"),
            ("name-linux-Arm64", "name"),
            ("name_Linux-64bit", "name"),
            ("name.Linux-64bit", "name"),
            ("name_macOS-64bit", "name"),
            ("name-v1.0.0_macOS-64bit", "name"),
            ("name-1.0.0_macOS-64bit", "name"),
            ("name_v1.0.0_macOS-64bit", "name"),
            ("name_macOS-64bit-v1.0.0", "name"),
            ("name_v1.0.0_macOS-64bit", "name"),
            ("name-v1.0.0-x86_64", "name"),
            ("name-x86_64", "name"),
            ("name-x86_64.exe", "name.exe"),
            ("name-darwin-arm64-v2.10.0", "name"),
        ];

        for x in data {
            if cfg!(target_os = "windows") {
                assert_eq!(trim_os_arch_version(x.0), "name.exe");
            } else {
                assert_eq!(trim_os_arch_version(x.0), x.1);
            }
        }
    }

    #[test]
    fn test_is_os_arch_match() {
        let data = vec![
            ("linux", "x86_64", "name-linux-amd64", true),
            ("linux", "x86_64", "name-linux-x86_64", true),
            ("linux", "x86_64", "name-linux-arm64", false),
            (
                "linux",
                "x86_64",
                "conftest_0.56.0_linux_x86_64.tar.gz",
                true,
            ),
            ("linux", "aarch64", "name-linux-aarch64", true),
            ("linux", "aarch64", "name-linux-arm64", true),
            ("linux", "aarch64", "name-linux-amd64", false),
            ("linux", "arm", "name-linux-armv7", true),
            ("linux", "arm", "name-linux-arm", true),
            ("linux", "arm", "name-linux-arm64", false),
            ("linux", "arm", "name-Linux-arm64", false),
            ("linux", "arm", "name-Linux-arm64.tar.gz", false),
            ("linux", "arm", "name-Linux-arm.tar.gz", true),
            ("windows", "x86_64", "name-windows-x86_64", true),
            ("windows", "x86_64", "name-windows-x86_64.exe", true),
            ("windows", "x86_64", "name-windows-amd64", true),
            ("windows", "x86_64", "name-win-amd64", true),
            ("windows", "x86_64", "name-windows-arm64", false),
            ("macos", "x86_64", "name-macos-amd64", true),
            ("macos", "x86_64", "name-darwin-amd64", true),
            ("macos", "x86_64", "name-macos-x86_64", true),
            ("macos", "x86_64", "name-darwin-x86_64", true),
            ("macos", "x86_64", "name-osx-x86_64", true),
            ("macos", "x86_64", "name-mac-x86_64", true),
            ("macos", "x86_64", "name-macos-arm64", false),
            ("macos", "aarch64", "name-macos-aarch64", true),
            ("macos", "aarch64", "name-darwin-aarch64", true),
            ("macos", "aarch64", "name-macos-arm64", true),
            ("macos", "aarch64", "name-darwin-arm64", true),
            ("macos", "aarch64", "name-macos-amd64", false),
        ];

        for (os, arch, url, expected) in data {
            assert_eq!(is_os_arch_match(os, arch, url), expected);
        }
    }
}
```

## File: `huber/src/parse.rs`
```rust
use anyhow::anyhow;
use log::warn;
use semver::{Version, VersionReq};

/// Parse package name and version
///
/// # Examples
///
/// ```
/// use huber::parse::parse_pkg_name_optional_semver;
/// let (name, version) = parse_pkg_name_optional_semver("package-name@1.2.3").unwrap();
/// assert_eq!(name, "package-name");
/// assert_eq!(version, "1.2.3");
/// ```
pub fn parse_pkg_name_optional_semver(name_version: &str) -> anyhow::Result<(String, String)> {
    let result: Vec<_> = name_version.splitn(2, '@').collect();

    if result.len() != 2 {
        return Ok((result[0].to_string(), "".to_string()));
    }

    let (name, version) = (result[0].to_string(), result[1].to_string());
    if let Err(e) = Version::parse(version.trim_start_matches('v')) {
        warn!("Failed to parse semantic version ({}): {}", version, e);
    }

    Ok((name, version))
}

/// Parse package name and version requirement
///
/// # Examples
///
/// ```
/// use huber::parse::parse_pkg_name_semver_req;
/// let (name, version) = parse_pkg_name_semver_req("package-name@~1.2.3").unwrap();
/// assert_eq!(name, "package-name");
/// assert_eq!(version, "~1.2.3");
///
/// let (name, version) = parse_pkg_name_semver_req("package-name@1.2.3").unwrap();
/// assert_eq!(name, "package-name");
/// assert_eq!(version, "1.2.3");
///
/// let (name, version) = parse_pkg_name_semver_req("package-name").unwrap();
/// assert_eq!(name, "package-name");
/// assert_eq!(version, "");
/// ```
pub fn parse_pkg_name_semver_req(name_version: &str) -> anyhow::Result<(String, String)> {
    let result: Vec<_> = name_version.splitn(2, '@').collect();

    if result.len() > 2 {
        return Err(anyhow!(
            "Failed to parse package name version due to invalid format"
        ));
    }

    let (name, version) = (
        result[0].to_string(),
        result.get(1).map_or("".to_string(), |v| v.to_string()),
    );
    if version.is_empty() || Version::parse(&version).is_ok() {
        return Ok((name, version));
    }

    VersionReq::parse(&version)?;
    Ok((name, version))
}
```

## File: `huber/src/semver.rs`
```rust
use std::cmp::Ordering;
use std::str::FromStr;

use regex::Regex;
use semver::Version;

pub trait VersionCompareTrait {
    fn cmp_version(&self, version: &str) -> Option<Ordering>;
}

impl VersionCompareTrait for String {
    fn cmp_version(&self, version: &str) -> Option<Ordering> {
        let regex = Regex::new(r"^v").unwrap();

        let self_version = Version::from_str(&regex.replace(self, ""));
        let comparing_version = Version::from_str(&regex.replace(version, ""));

        if self_version.is_err() || comparing_version.is_err() {
            return Some(Ordering::Equal);
        }

        self_version
            .unwrap()
            .partial_cmp(&comparing_version.unwrap())
    }
}
```

## File: `huber/src/cmd/config.rs`
```rust
use std::io::stdout;

use async_trait::async_trait;
use clap::{Args, Subcommand};
use libcli_rs::output;
use libcli_rs::output::{OutputFactory, OutputTrait};
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::service::config::{ConfigService, ConfigTrait};

#[derive(Subcommand)]
pub enum ConfigCommands {
    #[command(about = "Show Huber configurations", bin_name = "show")]
    Show(ConfigShowArgs),

    #[command(
        about = "Save Huber configurations via global options",
        bin_name = "save"
    )]
    Save(ConfigSaveArgs),
}

#[derive(Args)]
pub struct ConfigShowArgs {}

#[async_trait]
impl CommandTrait for ConfigShowArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let config_service = container.get::<ConfigService>().unwrap();
        let saved_config = config_service.get()?;

        output!(
            config.output_format,
            .display(
                stdout(),
                &saved_config,
                None,
                None,
            )
        )
    }
}

#[derive(Args)]
pub struct ConfigSaveArgs {}

#[async_trait]
impl CommandTrait for ConfigSaveArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let config_service = container.get::<ConfigService>().unwrap();
        let config_path = config.config_file()?;
        info!("Saving config to {:?}: {:#?}", config_path, config);
        config_service.update(config)?;
        info!("Config saved");

        Ok(())
    }
}

#[derive(Args)]
pub struct ConfigArgs {
    #[command(subcommand)]
    pub command: ConfigCommands,
}
```

## File: `huber/src/cmd/current.rs`
```rust
use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, ValueHint};
use log::info;
use semver::Version;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::{get_updated_package_version, CommandTrait};
use crate::error::HuberError::PackageNotInstalled;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::parse::parse_pkg_name_optional_semver;
use crate::service::package::PackageService;
use crate::service::release::{ReleaseAsyncTrait, ReleaseService};
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait};

#[derive(Args)]
pub struct CurrentArgs {
    #[arg(
        help = "Package name with version (e.g. 'package-name@version')",
        num_args = 1,
        value_hint = ValueHint::Unknown,
        value_parser = parse_pkg_name_optional_semver,
        required = true,
    )]
    name_version: Vec<(String, String)>,
}

#[async_trait]
impl CommandTrait for CurrentArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let release_service = container.get::<ReleaseService>().unwrap();
        let pkg_service = container.get::<PackageService>().unwrap();

        for (name, version) in self.name_version.iter() {
            if !pkg_service.has(name)? {
                return Err(anyhow!(PackageNotInstalled(name.clone())));
            }

            let pkg = pkg_service.get(name)?;
            let releases = release_service.find(&pkg).await?;

            if Version::parse(version.trim_start_matches('v')).is_err() {
                if let Some(mut r) = releases.clone().into_iter().find(|r| r.version.eq(version)) {
                    info!("Updating the current version of {} to {}", name, version);
                    release_service.set_current(&mut r).await?;
                    info!("{}@{} is now the current version", name, version);

                    return Ok(());
                } else {
                    anyhow::bail!("No installed version '{}' found for {}", version, name);
                }
            }

            let mut latest_release = release_service.get_latest(&pkg).await?;
            let version = get_updated_package_version(version, &latest_release.version);

            if let Some(mut r) = releases.into_iter().find(|r| r.version == version) {
                info!("Updating the current version of {} to {}", name, version);
                release_service.set_current(&mut r).await?;
                info!("{}@{} is now the current version", name, version);
            } else if !version.is_empty() {
                anyhow::bail!("No installed version {} found for {}", version, name);
            } else {
                info!(
                    "No version provided, trying to find the latest version of {}",
                    name
                );
                release_service.set_current(&mut latest_release).await?;
                info!(
                    "{}@{} is now the current version",
                    latest_release.package.name, latest_release.version
                );
            }
        }

        Ok(())
    }
}
```

## File: `huber/src/cmd/flush.rs`
```rust
use async_trait::async_trait;
use clap::Args;
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::model::release::{Release, SortModelTrait};
use crate::service::release::{ReleaseService, ReleaseTrait};
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait};

#[derive(Args)]
pub struct FlushArgs {}

#[async_trait]
impl CommandTrait for FlushArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let release_service = container.get::<ReleaseService>().unwrap();

        let current_releases = release_service.list()?;
        let mut flushed_releases: Vec<Release> = vec![];

        for cr in current_releases.iter() {
            let mut releases = release_service.find(&cr.package).await?;
            if releases.len() == 1 {
                continue;
            }

            releases.sort_by_version();
            for r in releases {
                if !r.current {
                    info!("Removing {}", r);
                    release_service.delete_release(&r)?;
                    info!("{} removed", r);

                    flushed_releases.push(r);
                }
            }
        }

        if flushed_releases.is_empty() {
            info!("Nothing to flush");
        }

        Ok(())
    }
}
```

## File: `huber/src/cmd/info.rs`
```rust
use std::io::stdout;

use async_trait::async_trait;
use clap::{Args, ValueHint};
use libcli_rs::output;
use libcli_rs::output::{OutputFactory, OutputTrait};
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::model::config::Config;
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;
use crate::service::ItemOperationTrait;

#[derive(Args)]
pub struct InfoArgs {
    #[arg(help = "Package name", num_args = 1, value_hint = ValueHint::Unknown)]
    name: String,
}

#[async_trait]
impl CommandTrait for InfoArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let pkg_service = container.get::<PackageService>().unwrap();
        let release_service = container.get::<ReleaseService>().unwrap();

        let pkg = pkg_service.get(&self.name)?;
        let release = release_service.get_latest(&pkg).await?;

        output!(
            config.output_format,
            .display(
                stdout(),
                &release.package,
                None,
                Some(vec!["detail"]),
            )
        )
    }
}
```

## File: `huber/src/cmd/install.rs`
```rust
use std::sync::Arc;

use async_trait::async_trait;
use clap::{Args, ValueHint};
use log::{debug, info, warn};
use simpledi_rs::di::{DIContainer, DIContainerTrait};
use tokio::task::JoinHandle;

use crate::cmd::get_default_stdlib;
use crate::cmd::update::is_pkg_locked_for_release;
use crate::cmd::{get_updated_package_version, CommandTrait, PlatformStdLib};
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::model::package::{default_targets, Package, PackageSource};
use crate::model::release::Release;
use crate::model::repo::LOCAL_REPO;
use crate::parse::parse_pkg_name_optional_semver;
use crate::service::cache::{CacheAsyncTrait, CacheService};
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;
use crate::service::repo::{RepoAsyncTrait, RepoService};
use crate::service::{ItemOperationTrait, ItemSearchTrait};

#[derive(Args)]
pub struct InstallArgs {
    #[arg(
        help = "Package name (e.g. 'package-name', 'package-name@version')g. 'owner/repo', 'owner/repo@version') for unmanaged packages by repositories",
        num_args = 1,
        required = true,
        value_parser = parse_pkg_name_optional_semver,
        value_hint = ValueHint::Unknown,
    )]
    name_version: Vec<(String, String)>,

    #[cfg(any(target_os = "linux", target_os = "windows"))]
    #[arg(
        help = "Prefer standard library (only for Linux or Windows)",
        long,
        num_args = 1,
        default_value_t = get_default_stdlib(),
        value_enum
    )]
    prefer_stdlib: PlatformStdLib,

    #[cfg(target_os = "macos")]
    #[arg(
        help = "Prefer standard library (only for Linux or Windows)",
        long,
        hide = true,
        num_args = 1,
        default_value_t = get_default_stdlib(),
        value_enum
    )]
    prefer_stdlib: PlatformStdLib,
}

#[async_trait]
impl CommandTrait for InstallArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let release_service = Arc::new(container.get::<ReleaseService>().unwrap().clone());
        let pkg_service = Arc::new(container.get::<PackageService>().unwrap().clone());
        let repo_service = Arc::new(container.get::<RepoService>().unwrap().clone());
        let config = Arc::new(config.clone());

        let cache_service = container.get::<CacheService>().unwrap();
        cache_service.update_repositories().await?;

        add_packages_to_local_repo(release_service.clone(), repo_service, &self.name_version)
            .await?;

        install_packages(
            config,
            release_service,
            pkg_service,
            &self.name_version,
            self.prefer_stdlib,
        )
        .await?;

        Ok(())
    }
}

async fn add_packages_to_local_repo(
    release_service: Arc<ReleaseService>,
    repo_service: Arc<RepoService>,
    name_versions: &[(String, String)],
) -> anyhow::Result<()> {
    let mut pkgs: Vec<Package> = vec![];

    for (name, _) in name_versions.iter() {
        let tokens: Vec<_> = name.splitn(2, '/').collect();
        if tokens.len() != 2 {
            continue;
        }

        let owner = tokens.first().unwrap();
        let repo = tokens.last().unwrap();

        let pkg = Package {
            name: name.clone(),
            source: PackageSource::Github {
                owner: owner.to_string(),
                repo: repo.to_string(),
            },
            targets: default_targets(),
            ..Default::default()
        };
        if let Err(err) = release_service.get_latest(&pkg).await {
            warn!("Skipped adding package {} to local repo: {}", name, err);
            continue;
        };

        pkgs.push(pkg);
    }

    repo_service.add_pkgs_to_repo(LOCAL_REPO, &pkgs).await?;
    Ok(())
}

pub fn parse_package_name_versions(name_versions: &[String]) -> Vec<(String, String)> {
    name_versions
        .iter()
        .map(|name_version| {
            let mut split = name_version.splitn(2, '@');
            let name = split.next().unwrap();
            let version = split.next().unwrap_or_default();

            (name.to_string(), version.to_string())
        })
        .collect()
}

pub async fn install_packages(
    config: Arc<Config>,
    release_service: Arc<ReleaseService>,
    pkg_service: Arc<PackageService>,
    pkg_versions: &[(String, String)],
    prefer_stdlib: PlatformStdLib,
) -> anyhow::Result<()> {
    let mut join_handles: Vec<JoinHandle<anyhow::Result<()>>> = vec![];

    #[allow(clippy::unnecessary_to_owned)]
    for (pkg, version) in pkg_versions.iter().cloned() {
        let pkg_service = pkg_service.clone();
        let release_service = release_service.clone();
        let config = config.clone();

        let handle: JoinHandle<anyhow::Result<()>> = tokio::spawn(async move {
            if !pkg_service.has(&pkg)? {
                warn!("Skipped installing package, as {} not found", pkg);
                return Ok(());
            }

            let mut pkg = pkg_service.get(&pkg)?;
            let latest_version = release_service
                .get_latest(&pkg)
                .await
                .map(|r| r.version)
                .or_else(|err| {
                    warn!(
                        "Failed to get the latest release version of {}: {}",
                        pkg.name, err
                    );
                    anyhow::Ok("".to_string())
                })?;
            let release_check = !latest_version.is_empty();
            let (version, is_latest) = get_version_to_install(&version, &pkg, &latest_version)?;

            if is_pkg_locked_for_release(&config, &pkg, &version) {
                warn!(
                    "Package {} is locked to version {}. Skipping installing {}",
                    pkg.name,
                    config.lock_pkg_versions.get(&pkg.name).unwrap(),
                    version
                );
                return Ok(());
            }

            let releases: Vec<Release> =
                release_service.search(Some(&pkg.name), None, None, None)?;
            if releases.iter().any(|r| r.version == version) {
                warn!("{}@{} already installed", pkg.name, version);
                return Ok(());
            }

            let msg = if is_latest {
                format!("{}@latest/{}", pkg.name, version)
            } else {
                format!("{}@{}", pkg.name, version)
            };

            info!("Installing package {}", msg);
            pkg.version = Some(version.clone());
            release_service
                .update(&pkg, &prefer_stdlib, release_check)
                .await?;
            info!("{} installed", msg);

            Ok(())
        });

        join_handles.push(handle);
    }

    for handle in join_handles.into_iter() {
        handle.await??;
    }

    Ok(())
}

fn get_version_to_install(
    version: &str,
    pkg: &Package,
    latest_version: &str,
) -> anyhow::Result<(String, bool)> {
    let (version, is_latest) = if version.is_empty() {
        info!(
            "{} version not specified, getting the latest version ({})",
            pkg.name, latest_version
        );

        if latest_version.is_empty() {
            anyhow::bail!(
                "Failed to get the latest release version of {} to install",
                pkg.name
            );
        }

        (latest_version.to_string(), true)
    } else {
        (get_updated_package_version(version, latest_version), false)
    };

    Ok((version, is_latest))
}
```

## File: `huber/src/cmd/load.rs`
```rust
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::sync::Arc;

use async_trait::async_trait;
use clap::{Args, ValueHint};
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::install::{install_packages, parse_package_name_versions};
use crate::cmd::{CommandTrait, PlatformStdLib};
use crate::model::config::Config;
use crate::service::cache::{CacheAsyncTrait, CacheService};
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;

#[derive(Args)]
pub struct LoadArgs {
    #[arg(
        help = "Load a package list to install",
        long,
        num_args = 1,
        default_value = "huber-packages.txt",
        value_hint = ValueHint::Unknown
    )]
    file: String,
}

#[async_trait]
impl CommandTrait for LoadArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let release_service = Arc::new(container.get::<ReleaseService>().unwrap().clone());
        let pkg_service = Arc::new(container.get::<PackageService>().unwrap().clone());
        let config = Arc::new(config.clone());

        let cache_service = container.get::<CacheService>().unwrap();
        cache_service.update_repositories().await?;

        info!("Loading packages from {}", self.file);

        let file = File::open(&self.file)?;
        let reader = BufReader::new(file);
        let versions: Vec<_> = reader.lines().map_while(Result::ok).collect();
        let count = versions.len();

        info!("Loaded packages: total {}: {:#?}", count, versions);
        info!("Installing packages: total {}", count);

        let versions: Vec<_> = parse_package_name_versions(&versions);
        install_packages(
            config,
            release_service,
            pkg_service,
            &versions,
            PlatformStdLib::None,
        )
        .await?;

        info!("Installed packages: total {}", count);

        Ok(())
    }
}
```

## File: `huber/src/cmd/lock.rs`
```rust
use std::io::stdout;

use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, Subcommand, ValueHint};
use libcli_rs::output;
use libcli_rs::output::{OutputFactory, OutputTrait};
use log::{info, warn};
use serde::{Deserialize, Serialize};
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::parse::parse_pkg_name_semver_req;
use crate::service::config::{ConfigService, ConfigTrait};
use crate::service::package::PackageService;
use crate::service::release::{ReleaseService, ReleaseTrait};
use crate::service::{check_pkg_installed, ItemOperationTrait};

#[derive(Args)]
pub struct LockArgs {
    #[arg(
        help = "Package name (e.g. 'package-name@semver' or package-name@<semver-requirement>' \
        using Cargo's dependency version requirement format)",
        num_args = 1,
        group = "lock",
        value_hint = ValueHint::Unknown,
        value_parser = parse_pkg_name_semver_req,
    )]
    pub name_version: Vec<(String, String)>,

    #[arg(
        help = "Lock all installed `current` packages",
        long,
        group = "lock",
        conflicts_with = "name_version",
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    pub all: bool,

    #[arg(
        help = "Treat version requirement as a caret requirement if \
        no version requirement is specified",
        long,
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    pub caret_required: bool,

    #[arg(
        help = "Treat version requirement as a tilde requirement if \
        no version requirement is specified",
        long,
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    pub tilde_required: bool,

    #[command(subcommand)]
    pub command: Option<LockCommands>,
}

#[derive(Subcommand)]
pub enum LockCommands {
    #[command(about = "Show locked package versions", bin_name = "show")]
    Show(LockShowArgs),
}

#[derive(Args)]
pub struct LockShowArgs {}

#[async_trait]
impl CommandTrait for LockShowArgs {
    async fn run(&self, config: &Config, _: &DIContainer) -> anyhow::Result<()> {
        display_locked_pkgs(config)
    }
}

#[async_trait]
impl CommandTrait for LockArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let pkg_service = container.get::<PackageService>().unwrap();
        let release_service = container.get::<ReleaseService>().unwrap();
        let config_service = container.get::<ConfigService>().unwrap();

        info!("Locking packages");

        let old_config = config.clone();
        let mut config = config.clone();

        if self.all {
            lock_installed_current_pkgs(
                &mut config,
                release_service,
                self.caret_required,
                self.tilde_required,
            )?;
        } else {
            if self.name_version.is_empty() {
                warn!("No packages specified to lock");
                return Ok(());
            }

            lock_pkgs(
                &mut config,
                pkg_service,
                release_service,
                &self.name_version,
                self.caret_required,
                self.tilde_required,
            )?;
        }

        if old_config.lock_pkg_versions != config.lock_pkg_versions {
            config_service.update(&config)?;
            info!(
                "Packages locked successfully: {:#?}",
                config.lock_pkg_versions
            );
            return Ok(());
        }

        Ok(())
    }
}

fn lock_pkgs(
    config: &mut Config,
    pkg_service: &PackageService,
    release_service: &ReleaseService,
    name_versions: &Vec<(String, String)>,
    caret_required: bool,
    tilde_required: bool,
) -> anyhow::Result<()> {
    for (pkg, version) in name_versions {
        if let Err(e) = check_pkg_installed(pkg_service, release_service, pkg) {
            let msg = if version.is_empty() {
                format!("Skipped locking package {}: {}", pkg, e)
            } else {
                format!("Skipped locking package {}@{}: {}", pkg, version, e)
            };

            warn!("{}", msg);
            continue;
        }

        let version = if version.is_empty() {
            release_service
                .current(&pkg_service.get(pkg)?)?
                .version
                .clone()
        } else {
            version.clone()
        };

        let version = get_version_requirement(caret_required, tilde_required, &version);
        info!("Locking package {}@{}", pkg, version);

        let versions = &mut config.lock_pkg_versions;
        versions.insert(pkg.clone(), version);
    }

    Ok(())
}

fn get_version_requirement(caret_required: bool, tilde_required: bool, version: &str) -> String {
    let version = version.trim_start_matches("v");
    if caret_required {
        format!("^{}", version)
    } else if tilde_required {
        format!("~{}", version)
    } else {
        version.to_string()
    }
}

fn lock_installed_current_pkgs(
    config: &mut Config,
    release_service: &ReleaseService,
    caret_required: bool,
    tilde_required: bool,
) -> anyhow::Result<()> {
    let releases = release_service.list()?;
    if releases.is_empty() {
        info!("No packages installed. Nothing to lock");
        return Ok(());
    }

    for ref r in releases {
        if !r.current {
            continue;
        }

        let version = get_version_requirement(caret_required, tilde_required, &r.version);
        info!("Locking package: {}@{}", r.name, version);
        let versions = &mut config.lock_pkg_versions;
        versions.insert(r.name.clone(), version);
    }

    Ok(())
}

fn display_locked_pkgs(config: &Config) -> anyhow::Result<()> {
    #[derive(Debug, Clone, Serialize, Deserialize)]
    struct PkgVersionInfo {
        name: String,
        version: String,
    }

    let pkg_version_infos: Vec<_> = config
        .lock_pkg_versions
        .iter()
        .map(|(name, version)| PkgVersionInfo {
            name: name.clone(),
            version: version.clone(),
        })
        .collect();

    if pkg_version_infos.is_empty() {
        warn!("No packages locked");
        return Ok(());
    }

    output!(
        config.output_format,
        .display(stdout(), &pkg_version_infos, None, None)
    )
}
```

## File: `huber/src/cmd/mod.rs`
```rust
use std::fmt::{Display, Formatter};
use std::str::FromStr;

use async_trait::async_trait;
use clap::builder::PossibleValue;
use clap::{Subcommand, ValueEnum};
use clap_complete::Shell;
use config::ConfigArgs;
use current::CurrentArgs;
use flush::FlushArgs;
use info::InfoArgs;
use install::InstallArgs;
use repo::RepoArgs;
use reset::ResetArgs;
use search::SearchArgs;
use self_update::SelfUpdateArgs;
use show::ShowArgs;
use simpledi_rs::di::DIContainer;
use uninstall::UninstallArgs;
use update::UpdateArgs;

use crate::cmd::load::LoadArgs;
use crate::cmd::lock::LockArgs;
use crate::cmd::save::SaveArgs;
use crate::cmd::unlock::UnlockArgs;
use crate::model::config::Config;

pub mod config;
mod current;
mod flush;
mod info;
mod install;
mod load;
pub mod lock;
pub mod repo;
mod reset;
mod save;
mod search;
mod self_update;
mod show;
mod uninstall;
mod unlock;
mod update;

#[async_trait]
pub trait CommandTrait {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()>;
}

#[derive(Subcommand)]
pub enum Commands {
    #[command(about = "Manage Huber configurations", bin_name = "config")]
    Config(ConfigArgs),

    #[command(about = "Update the current package versions", bin_name = "current")]
    Current(CurrentArgs),

    #[command(
        about = "Show command completions for the specified shell",
        bin_name = "completions"
    )]
    Completions {
        #[arg(help = "Shell name", num_args = 1, value_enum)]
        shell: Shell,
    },

    #[command(about = "Remove outdated installed artifacts", bin_name = "flush")]
    Flush(FlushArgs),

    #[command(about = "Show package information", bin_name = "info")]
    Info(InfoArgs),

    #[command(about = "Install packages", bin_name = "install")]
    Install(InstallArgs),

    #[command(about = "Manage repositories", bin_name = "repo")]
    Repo(RepoArgs),

    #[command(about = "Reset Huber", bin_name = "reset")]
    Reset(ResetArgs),

    #[command(about = "Search package", bin_name = "search")]
    Search(SearchArgs),

    #[command(about = "Update Huber", bin_name = "self-update")]
    SelfUpdate(SelfUpdateArgs),

    #[command(about = "Show installed packages", bin_name = "show")]
    Show(ShowArgs),

    #[command(about = "Uninstall packages", bin_name = "uninstall")]
    Uninstall(UninstallArgs),

    #[command(
        about = "Update installed packages to their latest released versions",
        bin_name = "update"
    )]
    Update(UpdateArgs),

    #[command(about = "Save the installed package list to a file", bin_name = "save")]
    Save(SaveArgs),

    #[command(
        about = "Load installed packages from a file generated by save command",
        bin_name = "load"
    )]
    Load(LoadArgs),

    #[command(about = "Lock packages or Show locked packages", bin_name = "lock")]
    Lock(LockArgs),

    #[command(about = "Unlock packages", bin_name = "unlock", bin_name = "unlock")]
    Unlock(UnlockArgs),
}
#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
pub enum PlatformStdLib {
    #[cfg(any(target_os = "linux", target_os = "windows"))]
    Gnu,
    #[cfg(target_os = "linux")]
    Musl,
    #[cfg(target_os = "windows")]
    Msvc,
    None,
}

impl Display for PlatformStdLib {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        self.to_possible_value()
            .expect("no values are skipped")
            .get_name()
            .fmt(f)
    }
}

impl FromStr for PlatformStdLib {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        for variant in Self::value_variants() {
            if variant.to_possible_value().unwrap().matches(s, false) {
                return Ok(*variant);
            }
        }
        Err(format!("invalid variant: {s}"))
    }
}

impl ValueEnum for PlatformStdLib {
    #[cfg(target_os = "linux")]
    fn value_variants<'a>() -> &'a [Self] {
        &[PlatformStdLib::Gnu, PlatformStdLib::Musl]
    }

    #[cfg(target_os = "macos")]
    fn value_variants<'a>() -> &'a [Self] {
        &[]
    }

    #[cfg(target_os = "windows")]
    fn value_variants<'a>() -> &'a [Self] {
        &[PlatformStdLib::Gnu, PlatformStdLib::Msvc]
    }

    #[cfg(target_os = "linux")]
    fn to_possible_value(&self) -> Option<PossibleValue> {
        Some(if let PlatformStdLib::Gnu = self {
            PossibleValue::new("gnu")
        } else {
            PossibleValue::new("musl")
        })
    }

    #[cfg(target_os = "windows")]
    fn to_possible_value(&self) -> Option<PossibleValue> {
        Some(if let PlatformStdLib::Gnu = self {
            PossibleValue::new("gnu")
        } else {
            PossibleValue::new("msvc")
        })
    }

    #[cfg(target_os = "macos")]
    fn to_possible_value(&self) -> Option<PossibleValue> {
        None
    }
}

#[macro_export]
macro_rules! lock_huber_ops {
    ($config:ident) => {
        use huber_procmacro::process_lock;
        use $crate::model::config::ConfigPath;

        #[cfg(not(target_os = "windows"))]
        {
            let lock_file = $config.lock_file()?;
            process_lock!(lock_file);
        }
    };
}

pub fn get_updated_package_version(version: &str, latest_version: &str) -> String {
    if latest_version.starts_with("v") && !version.starts_with("v") {
        format!("v{}", version)
    } else {
        version.to_string()
    }
}

pub fn get_default_stdlib() -> PlatformStdLib {
    #[cfg(target_os = "linux")]
    {
        PlatformStdLib::Gnu
    }
    #[cfg(target_os = "windows")]
    {
        PlatformStdLib::Msvc
    }
    #[cfg(not(any(target_os = "linux", target_os = "windows")))]
    {
        PlatformStdLib::None
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_get_updated_package_version() {
        let version = "1.0.0";
        let latest_version = "v1.0.1";
        assert_eq!(
            get_updated_package_version(version, latest_version),
            "v1.0.0"
        );

        let version = "v1.0.0";
        let latest_version = "1.0.1";
        assert_eq!(
            get_updated_package_version(version, latest_version),
            "v1.0.0"
        );

        let version = "v1.0.0";
        let latest_version = "v1.0.1";
        assert_eq!(
            get_updated_package_version(version, latest_version),
            "v1.0.0"
        );

        let version = "1.0.0";
        let latest_version = "1.0.1";
        assert_eq!(
            get_updated_package_version(version, latest_version),
            "1.0.0"
        );
    }
}
```

## File: `huber/src/cmd/repo.rs`
```rust
use std::io::stdout;
use std::path::PathBuf;

use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, Subcommand, ValueHint};
use libcli_rs::output;
use libcli_rs::output::{OutputFactory, OutputTrait};
use log::{info, warn};
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::error::HuberError::{RepoAlreadyExist, RepoNotFound};
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::model::repo::{Repository, LOCAL_REPO};
use crate::service::repo::RepoService;
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait};

#[derive(Args)]
pub struct RepoArgs {
    #[command(subcommand)]
    pub command: RepoCommands,
}

#[derive(Subcommand)]
pub enum RepoCommands {
    #[command(about = "Add a new repository", bin_name = "add")]
    Add(RepoAddArgs),

    #[command(about = "Remove a repository", bin_name = "remove")]
    Remove(RepoRemoveArgs),

    #[command(about = "Show all repositories", bin_name = "list")]
    Show(RepoShowArgs),
}

#[derive(Args)]
pub struct RepoAddArgs {
    #[arg(help = "Repo name", num_args = 1, value_hint = ValueHint::Unknown)]
    name: String,

    #[arg(
        help = "URL of the Huber package index file",
        long,
        num_args = 1,
        group = "repo",
        required_unless_present_any = &["file"],
        value_hint = ValueHint::Url
    )]
    url: Option<String>,

    #[arg(
        help = "File path of the Huber package index file",
        long,
        num_args = 1,
        group = "repo",
        required_unless_present_any = &["url"],
        value_hint = ValueHint::FilePath
    )]
    file: Option<String>,
}

#[async_trait]
impl CommandTrait for RepoAddArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let repo_service = container.get::<RepoService>().unwrap();

        if repo_service.has(&self.name)? {
            return Err(anyhow!(RepoAlreadyExist(self.name.clone())));
        }

        let repo = Repository {
            name: self.name.clone(),
            url: self.url.clone(),
            file: self.file.clone().map(PathBuf::from),
        };
        info!("Adding repo {}", repo.name);
        if let Err(err) = repo_service.create(repo.clone()).await {
            return Err(anyhow!("Failed to add repo {}: {}", repo.name, err));
        };
        info!("Repo {} added", repo.name);

        Ok(())
    }
}

#[derive(Args)]
pub struct RepoRemoveArgs {
    #[arg(help = "Repo names", num_args = 1, value_hint = ValueHint::Unknown)]
    name: Vec<String>,
}

#[async_trait]
impl CommandTrait for RepoRemoveArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let repo_service = container.get::<RepoService>().unwrap();

        for repo in &self.name {
            if repo == LOCAL_REPO {
                warn!("Cannot remove builtin local repo");
                continue;
            }

            if !repo_service.has(repo)? {
                return Err(anyhow!(RepoNotFound(repo.clone())));
            }

            info!("Removing repo {}", repo);
            repo_service.delete(repo)?;
            info!("Repo {} removed", repo);
        }

        Ok(())
    }
}

#[derive(Args)]
pub struct RepoShowArgs {}

#[async_trait]
impl CommandTrait for RepoShowArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let repo_service = container.get::<RepoService>().unwrap();

        let repos = repo_service.list()?;
        if repos.is_empty() {
            info!("No repositories added");
            return Ok(());
        }

        output!(
            config.output_format,
            .display(
                stdout(),
                &repos,
                None,
                None,
            )
        )
    }
}
```

## File: `huber/src/cmd/reset.rs`
```rust
use async_trait::async_trait;
use clap::Args;
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::service::update::{HuberUpdateService, UpdateTrait};

#[derive(Args)]
pub struct ResetArgs {}

#[async_trait]
impl CommandTrait for ResetArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let update_service = container.get::<HuberUpdateService>().unwrap();

        info!(
            "Resetting Huber by removing created caches, downloaded files and installed packages"
        );
        update_service.reset()?;
        info!("Huber reset");

        Ok(())
    }
}
```

## File: `huber/src/cmd/save.rs`
```rust
use std::fs::File;
use std::io::Write;

use async_trait::async_trait;
use clap::{Args, ValueHint};
use filepath::FilePath;
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::model::config::Config;
use crate::service::release::ReleaseService;
use crate::service::ItemOperationTrait;

#[derive(Args)]
pub struct SaveArgs {
    #[arg(
        help = "File path to save the installed package list",
        long,
        num_args = 1,
        default_value = "huber-packages.txt",
        value_hint = ValueHint::FilePath
    )]
    file: String,
}

#[async_trait]
impl CommandTrait for SaveArgs {
    async fn run(&self, _: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let release_service = container.get::<ReleaseService>().unwrap();

        info!("Collecting installed current packages");
        let versions: Vec<_> = release_service
            .list()?
            .iter()
            .filter(|r| r.current)
            .map(|r| format!("{}@{}", r.package.name, r.version))
            .collect();

        if versions.is_empty() {
            info!("No packages installed");
            return Ok(());
        }

        info!("Saving the package list to {}", self.file);
        let mut file = File::create(&self.file)?;
        file.write_all(versions.join("\n").as_bytes())?;
        info!(
            "Saved the package list to {}",
            file.path()?.canonicalize()?.to_string_lossy().to_string()
        );

        Ok(())
    }
}
```

## File: `huber/src/cmd/search.rs`
```rust
use std::io::stdout;

use async_trait::async_trait;
use clap::{Args, ValueHint};
use libcli_rs::output;
use libcli_rs::output::{OutputFactory, OutputTrait};
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::model::config::Config;
use crate::model::package::PackageSummary;
use crate::service::cache::{CacheAsyncTrait, CacheService};
use crate::service::package::PackageService;
use crate::service::ItemSearchTrait;

#[derive(Args)]
pub struct SearchArgs {
    #[arg(
        help = "Package name or regex search with --pattern",
        num_args = 1,
        value_hint = ValueHint::Unknown
    )]
    name: Option<String>,

    #[arg(
        help = "Regex search",
        long,
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    pattern: bool,

    #[arg(help = "Package owner", long,  num_args = 1, value_hint = ValueHint::Unknown)]
    owner: Option<String>,

    #[arg(
        help = "Show all the released versions",
        long,
        requires = "name",
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    all: bool,

    #[arg(
        help = "Search in a specific repository",
        long,
        num_args = 1,
        value_hint = ValueHint::Unknown
    )]
    repo: Option<String>,
}

#[async_trait]
impl CommandTrait for SearchArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let pkg_service = container.get::<PackageService>().unwrap();
        let cache_service = container.get::<CacheService>().unwrap();

        let _ = cache_service.update_repositories().await?;

        if self.all {
            let pkgs = pkg_service
                .find_summary(&self.name.clone().unwrap(), false)
                .await?;

            if pkgs.is_empty() {
                info!("No releases found");
                return Ok(());
            }

            return output!(
                config.output_format,
                .display(
                    stdout(),
                    &pkgs,
                    None,
                    Some(vec!["name", "description", "source"]),
                )
            );
        }

        let pkgs: Vec<PackageSummary> = pkg_service
            .search(
                self.name.as_deref(),
                if self.pattern {
                    self.name.as_deref()
                } else {
                    None
                },
                self.owner.as_deref(),
                self.repo.as_deref(),
            )?
            .into_iter()
            .map(PackageSummary::from)
            .collect();

        if pkgs.is_empty() {
            info!("No packages found");
            return Ok(());
        }

        output!(
            config.output_format,
            .display(
                stdout(),
                &pkgs,
                None,
                Some(vec!["version", "kind"]),
            )
        )
    }
}
```

## File: `huber/src/cmd/self_update.rs`
```rust
use async_trait::async_trait;
use clap::Args;
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::get_default_stdlib;
use crate::cmd::{CommandTrait, PlatformStdLib};
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::service::cache::{CacheAsyncTrait, CacheService};
use crate::service::update::{HuberUpdateService, UpdateAsyncTrait};

#[derive(Args)]
pub struct SelfUpdateArgs {
    #[cfg(any(target_os = "linux", target_os = "windows"))]
    #[arg(
        help = "Prefer standard library (only for Linux or Windows)",
        long,
        num_args = 1,
        default_value_t = get_default_stdlib(),
        value_enum
    )]
    prefer_stdlib: PlatformStdLib,

    #[cfg(target_os = "macos")]
    #[arg(
        help = "Prefer standard library (only for Linux or Windows)",
        long,
        hide = true,
        num_args = 1,
        default_value_t = get_default_stdlib(),
        value_enum
    )]
    prefer_stdlib: PlatformStdLib,
}

#[async_trait]
impl CommandTrait for SelfUpdateArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let cache_service = container.get::<CacheService>().unwrap();
        let _ = cache_service.update_repositories().await?;

        let update_service = container.get::<HuberUpdateService>().unwrap();
        let (has_update, version) = update_service.has_update().await?;

        if has_update {
            info!("Updating Huber {}", version);
            update_service.update(&self.prefer_stdlib).await?;
            info!("Huber updated to {}", version);
        } else {
            info!(
                "No update available. The latest version {:?} already installed.",
                env!("HUBER_VERSION")
            );
        }

        Ok(())
    }
}
```

## File: `huber/src/cmd/show.rs`
```rust
use std::io::stdout;

use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, ValueHint};
use libcli_rs::output;
use libcli_rs::output::{OutputFactory, OutputTrait};
use log::info;
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::error::HuberError::PackageNotFound;
use crate::model::config::Config;
use crate::model::release::SortModelTrait;
use crate::service::package::PackageService;
use crate::service::release::{ReleaseService, ReleaseTrait};
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait};

#[derive(Args)]
pub struct ShowArgs {
    #[arg(help = "Package name", num_args = 1, value_hint = ValueHint::Unknown)]
    name: Option<String>,

    #[arg(
        help = "Show all the installed versions",
        long,
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    all: bool,

    #[arg(
        help = "Show the detailed artifact info",
        long,
        num_args = 0,
        requires = "name",
        value_hint = ValueHint::Unknown
    )]
    detail: bool,
}

#[async_trait]
impl CommandTrait for ShowArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        let pkg_service = container.get::<PackageService>().unwrap();
        let release_service = container.get::<ReleaseService>().unwrap();

        let mut exc_keys = vec![];
        if !self.detail {
            exc_keys = vec!["package"];
        }

        if let Some(name) = self.name.as_deref() {
            return self
                .show_package(name, &exc_keys, config, pkg_service, release_service)
                .await;
        }

        let mut current_releases = release_service.list()?;
        current_releases.sort_by_name();
        exc_keys.push("executables");

        let releases = if self.all {
            let mut releases = vec![];
            for rel in current_releases.iter() {
                let mut rels = release_service.find(&rel.package).await?;
                rels.sort_by_version();
                releases.append(&mut rels);
            }

            releases
        } else {
            current_releases
        };

        if releases.is_empty() {
            info!("No packages installed");
            return Ok(());
        }

        output!(config.output_format, .display(
            stdout(),
            &releases,
            None,
            Some(exc_keys),
        ))
    }
}

impl ShowArgs {
    async fn show_package(
        &self,
        name: &str,
        exc_keys: &[&str],
        config: &Config,
        pkg_service: &PackageService,
        release_service: &ReleaseService,
    ) -> anyhow::Result<()> {
        if !release_service.has(name)? {
            return Err(anyhow!(PackageNotFound(name.to_string())));
        }

        let pkg = pkg_service.get(name)?;
        let release = release_service.current(&pkg)?;

        if self.all {
            let mut releases = release_service.find(&pkg).await?;
            releases.sort_by_version();
            releases.iter_mut().for_each(|it| {
                if it.current {
                    *it = release_service.current(&it.package).unwrap()
                }
            });

            return output!(
                config.output_format,
                .display(
                    stdout(),
                    &releases,
                    None,
                    Some(exc_keys.into()),
                )
            );
        }

        output!(
            config.output_format,
            .display(
                stdout(),
                &release,
                None,
                Some(exc_keys.into()),
            )
        )
    }
}
```

## File: `huber/src/cmd/uninstall.rs`
```rust
use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, ValueHint};
use log::{info, warn};
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;
use crate::service::{check_pkg_installed, ItemOperationTrait};

#[derive(Args)]
pub struct UninstallArgs {
    #[arg(help = "Package name", num_args = 1, value_hint = ValueHint::Unknown)]
    name: Vec<String>,
}

#[async_trait]
impl CommandTrait for UninstallArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let pkg_service = container.get::<PackageService>().unwrap();
        let release_service = container.get::<ReleaseService>().unwrap();

        for name in self.name.iter() {
            if let Err(e) = check_pkg_installed(pkg_service, release_service, name) {
                warn!("Skipped uninstalling package {}: {}", name, e);
                continue;
            }

            info!("Uninstalling {}", name);
            release_service.delete(name)?;
            info!("Uninstalled {}", name);
        }

        Ok(())
    }
}
```

## File: `huber/src/cmd/unlock.rs`
```rust
use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, ValueHint};
use log::{info, warn};
use simpledi_rs::di::{DIContainer, DIContainerTrait};

use crate::cmd::CommandTrait;
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::service::check_pkg_installed;
use crate::service::config::{ConfigService, ConfigTrait};
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;

#[derive(Args)]
pub struct UnlockArgs {
    #[arg(
        help = "Package name",
        num_args = 1,
        group = "lock",
        required = true,
        value_hint = ValueHint::Unknown
    )]
    name: Vec<String>,

    #[arg(
        help = "Unlock all the locked packages",
        long,
        group = "lock",
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    all: bool,
}

#[async_trait]
impl CommandTrait for UnlockArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let pkg_service = container.get::<PackageService>().unwrap();
        let release_service = container.get::<ReleaseService>().unwrap();
        let config_service = container.get::<ConfigService>().unwrap();
        let mut config = config.clone();

        info!("Unlocking packages");

        if self.all {
            info!("Unlocking all packages");
            config.lock_pkg_versions.clear();
        } else {
            unlock_pkgs(&mut config, pkg_service, release_service, &self.name)?;
        }

        config_service.update(&config)?;
        info!("Unlocked packages");

        Ok(())
    }
}

fn unlock_pkgs(
    config: &mut Config,
    pkg_service: &PackageService,
    release_service: &ReleaseService,
    pkgs: &Vec<String>,
) -> anyhow::Result<()> {
    for pkg in pkgs {
        if let Err(e) = check_pkg_installed(pkg_service, release_service, pkg) {
            warn!("Skipped unlocking package {}: {}", pkg, e);
            continue;
        }

        info!("Unlocking package {}", pkg);
        config.lock_pkg_versions.remove(pkg);
    }

    Ok(())
}
```

## File: `huber/src/cmd/update.rs`
```rust
use std::cmp::Ordering;
use std::collections::HashMap;
use std::sync::Arc;

use anyhow::anyhow;
use async_trait::async_trait;
use clap::{Args, ValueHint};
use log::{info, warn};
use maplit::hashmap;
use semver::{Version, VersionReq};
use simpledi_rs::di::{DIContainer, DIContainerTrait};
use tokio::task::JoinHandle;

use crate::cmd::get_default_stdlib;
use crate::cmd::{CommandTrait, PlatformStdLib};
use crate::error::HuberError::{PackageNotInstalled, PackageUnableToUpdate};
use crate::lock_huber_ops;
use crate::model::config::Config;
use crate::model::package::Package;
use crate::model::release::Release;
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;
use crate::service::ItemOperationTrait;

#[derive(Args)]
pub struct UpdateArgs {
    #[arg(help = "Package name", num_args = 1, value_hint = ValueHint::Unknown)]
    name: Vec<String>,

    #[cfg(any(target_os = "linux", target_os = "windows"))]
    #[arg(
        help = "Prefer standard library (only for Linux or Windows)",
        long,
        num_args = 1,
        default_value_t = get_default_stdlib(),
        value_enum
    )]
    prefer_stdlib: PlatformStdLib,

    #[cfg(target_os = "macos")]
    #[arg(
        help = "Prefer standard library (only for Linux or Windows)",
        long,
        hide = true,
        num_args = 1,
        default_value_t = get_default_stdlib(),
        value_enum
    )]
    prefer_stdlib: PlatformStdLib,

    #[arg(
        help = "Dry run to show available updates",
        long,
        num_args = 0,
        value_hint = ValueHint::Unknown
    )]
    dryrun: bool,
}

#[async_trait]
impl CommandTrait for UpdateArgs {
    async fn run(&self, config: &Config, container: &DIContainer) -> anyhow::Result<()> {
        lock_huber_ops!(config);

        let release_service = Arc::new(container.get::<ReleaseService>().unwrap().clone());
        let pkg_service = Arc::new(container.get::<PackageService>().unwrap().clone());
        let config = Arc::new(config.clone());

        for name in self.name.iter() {
            if !release_service.has(name)? {
                return Err(anyhow!(PackageUnableToUpdate(anyhow!(
                    PackageNotInstalled(name.clone())
                ))));
            }
        }

        let installed_latest_pkg_releases = if self.name.is_empty() {
            get_installed_latest_pkg_releases(&release_service)?
        } else {
            get_installed_latest_pkg_releases(&release_service)?
                .into_iter()
                .filter(|(name, _)| self.name.contains(name))
                .collect()
        };

        let mut join_handles: Vec<JoinHandle<anyhow::Result<()>>> = vec![];

        for (name, installed_release) in installed_latest_pkg_releases {
            let release_service = release_service.clone();
            let pkg_service = pkg_service.clone();
            let config = config.clone();
            let dryrun = self.dryrun;
            let prefer_stdlib = self.prefer_stdlib;

            let handle: JoinHandle<_> = tokio::spawn(async move {
                info!(
                    "Checking updates for {}. The latest installed version is {}",
                    name, installed_release.version
                );

                let pkg = pkg_service.get(&name)?;
                let new_release = release_service.get_latest(&pkg).await.map_err(|err| {
                    anyhow!(
                        "Failed to get the latest release of package {}: {}",
                        name,
                        err
                    )
                })?;

                info!(
                    "Found the latest version of {}: {}",
                    name, new_release.version
                );
                if is_pkg_locked_for_release(&config, &pkg, &new_release.version) {
                    warn!(
                        "Package {} is locked to version {}. Skipping updating to {}",
                        pkg.name,
                        config.lock_pkg_versions.get(&pkg.name).unwrap(),
                        new_release.version
                    );
                    return Ok(());
                }

                if new_release.compare(&installed_release)? == Ordering::Greater {
                    info!(
                        "Updating package {} from {} to {}",
                        name, installed_release.version, new_release.version
                    );
                    update(
                        release_service,
                        dryrun,
                        &new_release,
                        &installed_release,
                        &prefer_stdlib,
                    )
                    .await?;
                    info!("{} updated to {} successfully", name, new_release.version);
                } else {
                    info!(
                        "{} is already installed and up to date. Installed: {}, Latest: {}",
                        name, installed_release.version, new_release.version
                    );
                }

                Ok(())
            });
            join_handles.push(handle);
        }

        for handle in join_handles.into_iter() {
            handle.await??;
        }

        Ok(())
    }
}

fn get_installed_latest_pkg_releases(
    release_service: &ReleaseService,
) -> anyhow::Result<HashMap<String, Release>> {
    let mut installed_latest_pkg_releases: HashMap<String, Release> = hashmap! {};

    for release in release_service.list()? {
        if let Some(existing_release) = installed_latest_pkg_releases.get(&release.name) {
            if release.compare(existing_release)? == Ordering::Greater {
                installed_latest_pkg_releases.insert(release.name.clone(), release);
            }
        } else {
            installed_latest_pkg_releases.insert(release.name.clone(), release);
        }
    }
    Ok(installed_latest_pkg_releases)
}

pub fn is_pkg_locked_for_release(
    config: &Config,
    pkg: &Package,
    new_release_version: &str,
) -> bool {
    if let Some(lock_version) = config.lock_pkg_versions.get(&pkg.name) {
        let lock_version = lock_version.trim_start_matches("v");
        let lock_version = VersionReq::parse(lock_version).unwrap();

        let r = Version::parse(new_release_version.trim_start_matches("v"));
        if r.is_err() {
            warn!(
                "Failed to parse the new release version {}. Skip locking check",
                new_release_version
            );
            return false;
        }

        return !lock_version.matches(&r.unwrap());
    }

    false
}

async fn update(
    release_service: Arc<ReleaseService>,
    dryrun: bool,
    new_release: &Release,
    installed_release: &Release,
    prefer_stdlib: &PlatformStdLib,
) -> anyhow::Result<()> {
    if dryrun {
        info!("Available update {} to {}", installed_release, new_release);
    } else {
        info!("Updating {} to {}", installed_release, new_release);
        release_service
            .update(&new_release.package, prefer_stdlib, true)
            .await?;
    }

    Ok(())
}
```

## File: `huber/src/model/config.rs`
```rust
use std::collections::HashMap;
use std::env;
use std::fs::File;
use std::path::{Path, PathBuf};

use libcli_rs::output::OutputFormat;
use log::LevelFilter;
use octocrab::auth::Auth;
use serde::{Deserialize, Serialize};

use crate::fs::dir;
use crate::model::package::Package;

pub const HUBER_PKG_ROOT_DIR: &str = "HUBER_PKG_ROOT_DIR"; // generated directory
pub const GENERATED_DIR_NAME: &str = "generated-v1";

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct Config {
    pub log_level: String,
    pub output_format: OutputFormat,
    pub huber_dir: PathBuf,
    pub github_token: Option<String>,
    pub github_key: Option<String>,
    pub github_base_uri: Option<String>,
    pub lock_pkg_versions: HashMap<String, String>,
}

impl Config {
    #[allow(clippy::field_reassign_with_default)]
    pub fn new(
        log_level: String,
        output_format: OutputFormat,
        huber_dir: PathBuf,
        github_token: Option<String>,
        github_key: Option<String>,
        github_base_uri: Option<String>,
        lock_pkg_versions: HashMap<String, String>,
    ) -> Self {
        let mut config = Config::default();

        config.log_level = log_level;
        config.output_format = output_format;
        config.huber_dir = huber_dir;
        if let Some(token) = github_token {
            config.github_token = Some(token);
        }
        if let Some(key) = github_key {
            config.github_key = Some(key);
        }
        if let Some(uri) = github_base_uri {
            config.github_base_uri = Some(uri);
        }
        if !lock_pkg_versions.is_empty() {
            config.lock_pkg_versions = lock_pkg_versions;
        }

        config
    }
}

pub trait ConfigPath {
    fn lock_file(&self) -> anyhow::Result<PathBuf>;
    fn config_file(&self) -> anyhow::Result<PathBuf>;

    fn bin_dir(&self) -> anyhow::Result<PathBuf>;
    fn temp_dir(&self) -> anyhow::Result<PathBuf>;
    fn repo_root_dir(&self) -> anyhow::Result<PathBuf>;
    fn huber_repo_dir(&self) -> anyhow::Result<PathBuf>;

    fn external_repo_dir(&self, name: &str) -> anyhow::Result<PathBuf>;
    fn external_repo_file(&self, name: &str) -> anyhow::Result<PathBuf>;
    fn external_repo_pkgs_file(&self, name: &str) -> anyhow::Result<PathBuf>;

    fn huber_pkg_root_dir(&self) -> anyhow::Result<PathBuf>;
    fn pkg_manifest_file(&self, name: &str) -> anyhow::Result<PathBuf>;
    fn pkg_index_file(&self) -> anyhow::Result<PathBuf>;

    fn installed_pkg_root_dir(&self) -> anyhow::Result<PathBuf>;
    fn installed_pkg_base_dir(&self, pkg: &Package) -> anyhow::Result<PathBuf>;
    fn installed_pkg_dir(&self, pkg: &Package, version: &str) -> anyhow::Result<PathBuf>;
    fn installed_pkg_bin_dir(&self, pkg: &Package, version: &str) -> anyhow::Result<PathBuf>;
    fn installed_pkg_manifest_file(&self, pkg: &Package, version: &str) -> anyhow::Result<PathBuf>;

    fn current_pkg_dir(&self, pkg: &Package) -> anyhow::Result<PathBuf>;
    fn current_pkg_bin_dir(&self, pkg: &Package) -> anyhow::Result<PathBuf>;
    fn current_pkg_manifest_file(&self, pkg: &Package) -> anyhow::Result<PathBuf>;
    fn current_index_file(&self) -> anyhow::Result<PathBuf>;
}

impl Default for Config {
    fn default() -> Self {
        let default_config = Self {
            log_level: LevelFilter::Off.to_string(),
            output_format: OutputFormat::Console,
            huber_dir: dirs::home_dir().unwrap().join(".huber"),
            github_token: None,
            github_key: None,
            github_base_uri: Some("https://api.github.com".to_string()),
            lock_pkg_versions: Default::default(),
        };

        let config_path = default_config.config_file().unwrap();
        if config_path.exists() {
            Config::from(config_path)
        } else {
            default_config
        }
    }
}

impl From<PathBuf> for Config {
    fn from(p: PathBuf) -> Self {
        let f = File::open(&p).unwrap();
        serde_yaml::from_reader(f).unwrap()
    }
}

pub trait ConfigFieldConvertTrait {
    fn to_github_credentials(&self) -> Auth;
    fn to_github_key_path(&self) -> Option<PathBuf>;
}

impl ConfigFieldConvertTrait for Config {
    fn to_github_credentials(&self) -> Auth {
        if let Some(token) = self.github_token.clone() {
            Auth::PersonalToken(token.into())
        } else {
            Auth::None
        }
    }

    fn to_github_key_path(&self) -> Option<PathBuf> {
        self.github_key.clone().map(PathBuf::from)
    }
}

impl ConfigPath for Config {
    fn lock_file(&self) -> anyhow::Result<PathBuf> {
        let f = self.huber_dir.join("lock");
        if !f.exists() {
            File::create(f.as_path())?;
        }
        Ok(self.huber_dir.join("lock"))
    }

    fn config_file(&self) -> anyhow::Result<PathBuf> {
        Ok(self.huber_dir.join("config.yaml"))
    }

    fn bin_dir(&self) -> anyhow::Result<PathBuf> {
        dir(self.huber_dir.join("bin"))
    }

    fn temp_dir(&self) -> anyhow::Result<PathBuf> {
        dir(env::temp_dir().join("huber"))
    }

    fn repo_root_dir(&self) -> anyhow::Result<PathBuf> {
        dir(self.huber_dir.join("repos"))
    }

    fn huber_repo_dir(&self) -> anyhow::Result<PathBuf> {
        dir(self.repo_root_dir()?.join("huber"))
    }

    fn external_repo_dir(&self, name: &str) -> anyhow::Result<PathBuf> {
        dir(self.repo_root_dir()?.join(name))
    }

    fn external_repo_file(&self, name: &str) -> anyhow::Result<PathBuf> {
        Ok(self.external_repo_dir(name)?.join("repo.yaml"))
    }

    fn external_repo_pkgs_file(&self, name: &str) -> anyhow::Result<PathBuf> {
        Ok(self.external_repo_dir(name)?.join("huber.yaml"))
    }

    fn huber_pkg_root_dir(&self) -> anyhow::Result<PathBuf> {
        let path = env::var(HUBER_PKG_ROOT_DIR).unwrap_or_default();
        if Path::new(&path).is_dir() {
            dir(PathBuf::from(path))
        } else {
            dir(self.huber_repo_dir()?.join(GENERATED_DIR_NAME))
        }
    }

    fn pkg_manifest_file(&self, name: &str) -> anyhow::Result<PathBuf> {
        Ok(self
            .huber_pkg_root_dir()?
            .join("packages")
            .join(name)
            .with_extension("yaml"))
    }

    fn pkg_index_file(&self) -> anyhow::Result<PathBuf> {
        Ok(self
            .huber_pkg_root_dir()?
            .join("index")
            .with_extension("yaml"))
    }

    fn installed_pkg_root_dir(&self) -> anyhow::Result<PathBuf> {
        dir(self.huber_dir.join("packages"))
    }

    fn installed_pkg_base_dir(&self, pkg: &Package) -> anyhow::Result<PathBuf> {
        dir(self
            .installed_pkg_root_dir()?
            .join(pkg.source.to_string())
            .join(format!("{}_{}", pkg.source.owner(), pkg.name)))
    }

    fn installed_pkg_dir(&self, pkg: &Package, version: &str) -> anyhow::Result<PathBuf> {
        let version = pkg.parse_version_from_tag_name(&version.to_string())?;
        dir(self.installed_pkg_base_dir(pkg)?.join(version))
    }

    fn installed_pkg_bin_dir(&self, pkg: &Package, version: &str) -> anyhow::Result<PathBuf> {
        let version = pkg.parse_version_from_tag_name(&version.to_string())?;
        dir(self.installed_pkg_dir(pkg, &version)?.join("bin"))
    }

    fn installed_pkg_manifest_file(&self, pkg: &Package, version: &str) -> anyhow::Result<PathBuf> {
        let version = pkg.parse_version_from_tag_name(&version.to_string())?;

        Ok(self
            .installed_pkg_dir(pkg, &version)?
            .join(pkg.name.replace("/", "_"))
            .with_extension("yaml"))
    }

    fn current_pkg_dir(&self, pkg: &Package) -> anyhow::Result<PathBuf> {
        Ok(self.installed_pkg_base_dir(pkg)?.join("current"))
    }

    fn current_pkg_bin_dir(&self, pkg: &Package) -> anyhow::Result<PathBuf> {
        Ok(self.current_pkg_dir(pkg)?.join("bin"))
    }

    fn current_pkg_manifest_file(&self, pkg: &Package) -> anyhow::Result<PathBuf> {
        Ok(self
            .current_pkg_dir(pkg)?
            .join(pkg.name.replace("/", "_"))
            .with_extension("yaml"))
    }

    fn current_index_file(&self) -> anyhow::Result<PathBuf> {
        Ok(self
            .installed_pkg_root_dir()?
            .join("index")
            .with_extension("yaml"))
    }
}
```

## File: `huber/src/model/mod.rs`
```rust
pub mod config;
pub mod package;
pub mod release;
pub mod repo;
```

## File: `huber/src/model/package.rs`
```rust
use std::cmp::Ordering;
use std::collections::HashMap;
use std::fmt::{Display, Formatter};
use std::path::{Path, PathBuf};
use std::str::FromStr;
use std::{env, fmt};

use anyhow::anyhow;
use regex::Regex;
use semver::Version;
use serde::{Deserialize, Serialize};

use crate::model::release::{ReleaseKind, SortModelTrait};
use crate::semver::VersionCompareTrait;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Package {
    pub name: String,

    #[serde(default)]
    #[serde(skip_serializing_if = "Option::is_none")]
    pub version: Option<String>,

    #[serde(default)]
    #[serde(skip_serializing_if = "Option::is_none")]
    pub description: Option<String>,

    pub source: PackageSource,

    #[serde(default)]
    pub targets: Vec<PackageTargetType>,

    #[serde(skip)]
    #[serde(with = "serde_yaml::with::singleton_map")]
    pub detail: Option<PackageDetailType>,

    #[serde(skip)]
    #[serde(with = "serde_yaml::with::singleton_map")]
    pub release_kind: Option<ReleaseKind>,
}

impl Default for Package {
    fn default() -> Self {
        Self {
            name: "".to_string(),
            version: None,
            description: None,
            source: PackageSource::Github {
                owner: "".to_string(),
                repo: "".to_string(),
            },
            targets: default_targets(),
            detail: None,
            release_kind: None,
        }
    }
}

unsafe impl Send for Package {}

unsafe impl Sync for Package {}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PackageSummary {
    pub name: String,
    pub description: Option<String>,
    pub source: Option<String>,
    pub version: Option<String>,
    pub kind: Option<ReleaseKind>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum PackageSource {
    Github { owner: String, repo: String },
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum PackageDetailType {
    Github { package: GithubPackage },
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum PackageTargetType {
    LinuxAmd64(PackageManagement),
    LinuxArm64(PackageManagement),
    LinuxArm(PackageManagement),
    MacOSAmd64(PackageManagement),
    MacOSArm64(PackageManagement),
    WindowsAmd64(PackageManagement),
    Default(PackageManagement),
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct PackageManagement {
    // {version}, {os}, {arch} can be used in each. Also, an external URL is acceptable
    pub artifact_templates: Vec<String>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub executable_mappings: Option<HashMap<String, String>>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub tag_version_regex_template: Option<String>,

    // only keep the {version} part
    #[serde(skip_serializing_if = "Option::is_none")]
    pub scan_dirs: Option<Vec<String>>,
}

#[derive(Default, Debug, Clone, Serialize, Deserialize)]
pub struct GithubPackage {
    pub url: String,
    pub html_url: String,
    pub assets_url: String,
    pub upload_url: String,
    pub tarball_url: String,
    pub zipball_url: String,
    pub id: u64,
    pub tag_name: String,
    pub target_commitish: String,
    pub name: String,

    #[serde(skip_deserializing)]
    #[serde(skip_serializing)]
    pub body: String,

    pub draft: bool,
    pub prerelease: bool,
    pub created_at: String,
    pub published_at: String,
    pub assets: Vec<GithubAsset>,
}

#[derive(Default, Debug, Clone, Serialize, Deserialize)]
pub struct GithubAsset {
    pub url: String,
    pub browser_download_url: String,
    pub id: u64,
    pub name: String,
    pub label: Option<String>,
    pub state: String,
    pub content_type: String,
    pub size: u64,
    pub download_count: u64,
    pub created_at: String,
    pub updated_at: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PackageIndex {
    pub name: String,
    pub owner: String,
    pub source: String,
}

impl PackageSource {
    pub fn url(&self) -> String {
        match self {
            PackageSource::Github { owner, repo } => {
                format!("https://github.com/{}/{}", owner, repo)
            }
        }
    }

    pub fn owner(&self) -> String {
        match self {
            PackageSource::Github { owner, repo: _ } => owner.to_string(),
        }
    }
}

impl Package {
    pub fn target(&self) -> anyhow::Result<PackageManagement> {
        let os = env::consts::OS;
        let arch = env::consts::ARCH;

        let default_pkg_mgmt: Option<_> = self.targets.iter().find_map(|it| match it {
            PackageTargetType::Default(m) => Some(m.clone()),
            _ => None,
        });

        self.get_package_management(os, arch, default_pkg_mgmt)
            .ok_or(anyhow!("Unsupported OS {} or ARCH {}", os, arch))
    }

    fn get_package_management(
        &self,
        os: &str,
        arch: &str,
        default_pkg_mgmt: Option<PackageManagement>,
    ) -> Option<PackageManagement> {
        match os {
            "linux" => match arch {
                "x86_64" => self.targets.iter().find_map(|it| match it {
                    PackageTargetType::LinuxAmd64(m) => Some(m.clone()),
                    _ => default_pkg_mgmt.clone(),
                }),
                "aarch64" => self.targets.iter().find_map(|it| match it {
                    PackageTargetType::LinuxArm64(m) => Some(m.clone()),
                    _ => default_pkg_mgmt.clone(),
                }),
                _ => None,
            },
            "macos" => match arch {
                "x86_64" => self.targets.iter().find_map(|it| match it {
                    PackageTargetType::MacOSAmd64(m) => Some(m.clone()),
                    _ => default_pkg_mgmt.clone(),
                }),
                "aarch64" => self.targets.iter().find_map(|it| match it {
                    PackageTargetType::MacOSArm64(m) => Some(m.clone()),
                    _ => default_pkg_mgmt.clone(),
                }),
                _ => None,
            },
            "windows" => match arch {
                "x86_64" => self.targets.iter().find_map(|it| match it {
                    PackageTargetType::WindowsAmd64(m) => Some(m.clone()),
                    _ => default_pkg_mgmt.clone(),
                }),
                _ => None,
            },
            _ => None,
        }
    }

    pub fn parse_version_from_tag_name(&self, tag_name: &String) -> anyhow::Result<String> {
        let mut version = tag_name.clone();

        if let Some(ref template) = self.target()?.tag_version_regex_template {
            let regex = Regex::new(&template.to_string())?;

            if let Some(capture) = regex.captures(tag_name) {
                if let Some(m) = capture.get(1) {
                    version = m.as_str().to_string();
                } else {
                    return Err(anyhow!(
                        "Failed to capture the version from {} via tag_version_regex_template {}",
                        tag_name,
                        template
                    ));
                }
            }

            if Version::parse(version.trim_start_matches("v")).is_err() {
                return Err(anyhow!(
                    "Failed to parse the version {} from tag_name {}",
                    version,
                    tag_name
                ));
            }
        }

        Ok(version)
    }

    pub fn get_scan_dirs(&self, pkg_dir: &Path) -> anyhow::Result<Vec<PathBuf>> {
        let mut scan_dirs = vec![];

        if let Some(extra_scan_dirs) = self.target()?.scan_dirs {
            let mut extra_scan_dirs: Vec<PathBuf> = extra_scan_dirs
                .into_iter()
                .map(|x| {
                    pkg_dir.join(x.replace(
                        "{version}",
                        self.version.as_ref().unwrap().trim_start_matches("v"),
                    ))
                })
                .collect();
            scan_dirs.append(&mut extra_scan_dirs);
        }

        Ok(scan_dirs)
    }
}

impl From<octocrab::models::repos::Release> for GithubPackage {
    fn from(r: octocrab::models::repos::Release) -> Self {
        Self {
            url: r.url.into(),
            html_url: r.html_url.into(),
            assets_url: r.assets_url.into(),
            upload_url: r.upload_url,
            tarball_url: r.tarball_url.map_or("".into(), |x| x.into()),
            zipball_url: r.zipball_url.map_or("".into(), |x| x.into()),
            id: *r.id,
            tag_name: r.tag_name,
            target_commitish: r.target_commitish,
            name: r.name.unwrap_or("".into()),
            body: r.body.unwrap_or("".into()),
            draft: r.draft,
            prerelease: r.prerelease,
            created_at: r.created_at.map_or("".into(), |x| x.to_string()),
            published_at: r.published_at.map_or("".into(), |x| x.to_string()),
            assets: r.assets.into_iter().map(GithubAsset::from).collect(),
        }
    }
}

impl From<octocrab::models::repos::Asset> for GithubAsset {
    fn from(a: octocrab::models::repos::Asset) -> Self {
        GithubAsset {
            url: a.url.to_string(),
            browser_download_url: a.browser_download_url.to_string(),
            id: *a.id,
            name: a.name,
            label: a.label,
            state: a.state,
            content_type: a.content_type,
            size: a.size as u64,
            download_count: a.download_count as u64,
            created_at: a.created_at.to_string(),
            updated_at: a.updated_at.to_string(),
        }
    }
}

impl Display for Package {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "{}", &self.name)
    }
}

impl Display for PackageSource {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match self {
            PackageSource::Github { .. } => write!(f, "github"),
        }
    }
}

impl PackageSummary {
    pub fn compare(&self, pkg: &PackageSummary) -> anyhow::Result<Ordering> {
        let v1 = Version::from_str(self.version.clone().unwrap().trim_start_matches("v"))?;
        let v2 = Version::from_str(pkg.version.clone().unwrap().trim_start_matches("v"))?;

        Ok(v1.cmp(&v2))
    }
}

impl From<Package> for PackageSummary {
    fn from(p: Package) -> Self {
        PackageSummary {
            name: p.name.clone(),
            description: p.description.clone(),
            source: Some(p.source.url()),
            version: p.version.clone(),
            kind: p.release_kind,
        }
    }
}

impl SortModelTrait for Vec<PackageSummary> {
    fn sort_by_version(&mut self) {
        self.sort_by(|x, y| {
            y.version
                .as_ref()
                .unwrap()
                .cmp_version(x.version.as_ref().unwrap())
                .unwrap()
        });
    }

    fn sort_by_name(&mut self) {
        self.sort_by(|x, y| x.name.cmp(&y.name))
    }
}

pub fn default_targets() -> Vec<PackageTargetType> {
    vec![
        PackageTargetType::LinuxAmd64(Default::default()),
        PackageTargetType::LinuxArm64(Default::default()),
        PackageTargetType::LinuxArm(Default::default()),
        PackageTargetType::MacOSAmd64(Default::default()),
        PackageTargetType::MacOSArm64(Default::default()),
        PackageTargetType::WindowsAmd64(Default::default()),
    ]
}

pub fn default_targets_no_arm() -> Vec<PackageTargetType> {
    vec![
        PackageTargetType::LinuxAmd64(Default::default()),
        PackageTargetType::LinuxArm64(Default::default()),
        PackageTargetType::MacOSAmd64(Default::default()),
        PackageTargetType::MacOSArm64(Default::default()),
        PackageTargetType::WindowsAmd64(Default::default()),
    ]
}

pub fn default_targets_no_arm_windows() -> Vec<PackageTargetType> {
    vec![
        PackageTargetType::LinuxAmd64(Default::default()),
        PackageTargetType::LinuxArm64(Default::default()),
        PackageTargetType::MacOSAmd64(Default::default()),
        PackageTargetType::MacOSArm64(Default::default()),
    ]
}

pub fn default_targets_no_windows() -> Vec<PackageTargetType> {
    vec![
        PackageTargetType::LinuxAmd64(Default::default()),
        PackageTargetType::LinuxArm64(Default::default()),
        PackageTargetType::LinuxArm(Default::default()),
        PackageTargetType::MacOSAmd64(Default::default()),
        PackageTargetType::MacOSArm64(Default::default()),
    ]
}

pub fn default_targets_no_arm64_arm() -> Vec<PackageTargetType> {
    vec![
        PackageTargetType::LinuxAmd64(Default::default()),
        PackageTargetType::MacOSAmd64(Default::default()),
        PackageTargetType::MacOSArm64(Default::default()),
        PackageTargetType::WindowsAmd64(Default::default()),
    ]
}
```

## File: `huber/src/model/release.rs`
```rust
use std::cmp::Ordering;
use std::fmt;
use std::fmt::{Display, Formatter};
use std::str::FromStr;

use semver::Version;
use serde::{Deserialize, Serialize};

use crate::model::package::{
    GithubAsset, GithubPackage, Package, PackageDetailType, PackageSource,
};
use crate::semver::VersionCompareTrait;

pub trait SortModelTrait {
    fn sort_by_version(&mut self);
    fn sort_by_name(&mut self);
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReleaseIndex {
    pub name: String,
    pub version: String,
    pub owner: String,
    pub source: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Release {
    pub name: String,
    pub version: String,
    pub current: bool,
    pub package: Package,
    pub executables: Option<Vec<String>>,
    pub kind: Option<ReleaseKind>,
}

unsafe impl Send for Release {}

unsafe impl Sync for Release {}

#[derive(Debug, Copy, Clone, Serialize, Deserialize, Eq, PartialEq)]
pub enum ReleaseKind {
    Draft,
    PreRelease,
    Release,
}

impl Release {
    pub fn compare(&self, pkg: &Release) -> anyhow::Result<Ordering> {
        if Version::parse(&self.version).is_ok() {
            let v1 = Version::from_str(self.version.trim_start_matches("v"))?;
            let v2 = Version::from_str(pkg.version.trim_start_matches("v"))?;

            Ok(v1.cmp(&v2))
        } else {
            Ok(self.version.cmp(&pkg.version))
        }
    }
}

impl Display for Release {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{} (version: {}, source: {})",
            self.name, self.version, self.package.source
        )
    }
}

impl From<octocrab::models::repos::Release> for Release {
    fn from(r: octocrab::models::repos::Release) -> Self {
        let release_kind = if r.draft {
            ReleaseKind::Draft
        } else if r.prerelease {
            ReleaseKind::PreRelease
        } else {
            ReleaseKind::Release
        };

        Release {
            name: "".to_string(),
            version: r.tag_name.clone(),
            current: false,
            package: Package {
                name: "".to_string(),
                source: PackageSource::Github {
                    owner: "".to_string(),
                    repo: "".to_string(),
                },
                targets: vec![],
                detail: Some(PackageDetailType::Github {
                    package: GithubPackage {
                        url: r.url.into(),
                        html_url: r.html_url.into(),
                        assets_url: r.assets_url.into(),
                        upload_url: r.upload_url,
                        tarball_url: r.tarball_url.map_or("".to_string(), |s| s.to_string()),
                        zipball_url: r.zipball_url.map_or("".to_string(), |s| s.to_string()),
                        id: *r.id,
                        tag_name: r.tag_name.clone(),
                        target_commitish: r.target_commitish,
                        name: r.name.unwrap_or_default(),
                        body: r.body.unwrap_or_default(),
                        draft: r.draft,
                        prerelease: r.prerelease,
                        created_at: r.created_at.map_or("".to_string(), |s| s.to_string()),
                        published_at: r.published_at.map_or("".to_string(), |s| s.to_string()),
                        assets: r.assets.into_iter().map(GithubAsset::from).collect(),
                    },
                }),
                version: Some(r.tag_name.clone()),
                description: None,
                release_kind: Some(release_kind),
            },
            executables: None,
            kind: Some(release_kind),
        }
    }
}

impl SortModelTrait for Vec<Release> {
    fn sort_by_version(&mut self) {
        self.sort_by(|x, y| y.version.cmp_version(&x.version).unwrap());
    }

    fn sort_by_name(&mut self) {
        self.sort_by(|x, y| x.name.cmp(&y.name));
    }
}
```

## File: `huber/src/model/repo.rs`
```rust
use std::fmt;
use std::fmt::{Display, Formatter};
use std::path::PathBuf;

use serde::{Deserialize, Serialize};

pub const LOCAL_REPO: &str = "local";

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct Repository {
    pub name: String,
    #[serde(default)]
    pub url: Option<String>,
    #[serde(default)]
    pub file: Option<PathBuf>,
}

impl Display for Repository {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}", self)
    }
}
```

## File: `huber/src/service/cache.rs`
```rust
use std::env;
use std::fs::File;
use std::path::Path;
use std::sync::{Arc, RwLock};
use std::time::SystemTime;

use anyhow::anyhow;
use async_trait::async_trait;
use lazy_static::lazy_static;
use log::debug;
use rayon::prelude::*;
use regex::Regex;
use simpledi_rs::di::{DIContainer, DIContainerExtTrait, DependencyInjectTrait};

use crate::error::HuberError::PackageNotFound;
use crate::gh::{GithubClient, GithubClientTrait};
use crate::model::config::{Config, ConfigFieldConvertTrait, ConfigPath, HUBER_PKG_ROOT_DIR};
use crate::model::package::{Package, PackageIndex};
use crate::model::repo::{Repository, LOCAL_REPO};
use crate::service::repo::{RepoAsyncTrait, RepoService, RepoTrait};
use crate::service::{ItemOperationTrait, ServiceTrait};

lazy_static! {
    static ref managed_repo_modified_time: RwLock<Option<SystemTime>> = Default::default();
    static ref managed_pkg_indexes: RwLock<Vec<PackageIndex>> = Default::default();
}

pub trait CacheTrait {
    fn get_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<Package>;
    fn get_external_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<Package>;
    fn list_packages(
        &self,
        pattern: &str,
        owner: &str,
        repo: Option<&str>,
    ) -> anyhow::Result<Vec<Package>>;
    fn list_external_packages(&self, repo: Option<&str>) -> anyhow::Result<Vec<Package>>;
    fn has_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<bool>;
    fn has_external_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<bool>;
    fn get_package_indexes(&self) -> anyhow::Result<Vec<PackageIndex>>;

    fn refresh_package_indexes(&self) -> anyhow::Result<()>;
}

#[async_trait]
pub trait CacheAsyncTrait {
    async fn update_repositories(&self) -> anyhow::Result<()>;
}

#[derive(Debug)]
pub struct CacheService {
    pub container: Option<Arc<DIContainer>>,
}

unsafe impl Send for CacheService {}

unsafe impl Sync for CacheService {}

impl ServiceTrait for CacheService {}

impl DependencyInjectTrait for CacheService {
    fn inject(&mut self, container: Arc<DIContainer>) {
        self.container = Some(container);
    }
}

impl Default for CacheService {
    fn default() -> Self {
        Self::new()
    }
}

impl CacheService {
    pub fn new() -> Self {
        Self { container: None }
    }
}

impl CacheTrait for CacheService {
    fn get_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<Package> {
        if !self.has_package(name, repo)? {
            return Err(anyhow!(PackageNotFound(name.into())));
        }

        let config = self.container.get::<Config>().unwrap();
        let pkg_file = config.pkg_manifest_file(name)?;

        if pkg_file.exists() {
            Ok(serde_yaml::from_reader::<File, Package>(File::open(
                pkg_file,
            )?)?)
        } else {
            self.get_external_package(name, repo)
        }
    }

    fn get_external_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<Package> {
        match self
            .list_external_packages(repo)?
            .into_iter()
            .find(|it| it.name == name)
        {
            None => Err(anyhow!(PackageNotFound(name.into()))),
            Some(pkg) => Ok(pkg),
        }
    }

    fn list_packages(
        &self,
        pattern: &str,
        owner: &str,
        repo: Option<&str>,
    ) -> anyhow::Result<Vec<Package>> {
        let mut pkgs: Vec<Package> = vec![];

        // managed packages
        if repo.is_none() {
            pkgs = match pattern {
                "" => {
                    let indexes: Vec<_> = self.get_package_indexes()?.into_par_iter().collect();
                    indexes
                        .into_iter()
                        .filter_map(|it| {
                            if owner.is_empty() || it.owner == owner {
                                self.get_package(&it.name, repo)
                                    .map_err(|err| {
                                        debug!("{}", err);
                                        err
                                    })
                                    .ok()
                            } else {
                                None
                            }
                        })
                        .collect()
                }

                _ => {
                    let regex = Regex::new(pattern)?;
                    let indexes: Vec<_> = self.get_package_indexes()?.into_par_iter().collect();
                    indexes
                        .into_iter()
                        .filter_map(|it| {
                            if regex.is_match(&it.name) {
                                self.get_package(&it.name, repo)
                                    .map_err(|err| {
                                        debug!("{}", err);
                                        err
                                    })
                                    .ok()
                            } else {
                                None
                            }
                        })
                        .collect()
                }
            };
        }

        // external packages
        pkgs.append(&mut self.list_external_packages(repo)?);
        pkgs.sort_by(|p1, p2| p1.name.cmp(&p2.name));

        Ok(pkgs)
    }

    fn list_external_packages(&self, repo: Option<&str>) -> anyhow::Result<Vec<Package>> {
        let repo_service = self.container.get::<RepoService>().unwrap();

        if let Some(repo) = repo {
            let pkgs = repo_service.get_packages_by_repo(repo)?;
            return Ok(pkgs);
        }

        let repos = repo_service.list()?;
        let pkgs: Vec<Package> = repos
            .par_iter()
            .filter_map(|it: &Repository| {
                if let Ok(p) = repo_service.get_packages_by_repo(&it.name) {
                    Some(p)
                } else {
                    None
                }
            })
            .flat_map(|it| it)
            .collect();

        Ok(pkgs)
    }

    fn has_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<bool> {
        if repo.is_none() && self.get_package_indexes()?.iter().any(|it| it.name == name) {
            return Ok(true);
        }

        // external
        self.has_external_package(name, repo)
    }

    fn has_external_package(&self, name: &str, repo: Option<&str>) -> anyhow::Result<bool> {
        Ok(self
            .list_external_packages(repo)?
            .iter()
            .any(|it| it.name == name))
    }

    fn get_package_indexes(&self) -> anyhow::Result<Vec<PackageIndex>> {
        self.refresh_package_indexes()?;

        Ok(managed_pkg_indexes
            .read()
            .map_err(|e| anyhow!("{}", e))?
            .clone())
    }

    fn refresh_package_indexes(&self) -> anyhow::Result<()> {
        debug!("Refreshing package indexes");

        let config = self.container.get::<Config>().unwrap();
        let index_file = config.pkg_index_file()?;

        if index_file.exists() {
            let time = File::open(&index_file)?.metadata()?.modified()?;
            let modified_time = *managed_repo_modified_time
                .read()
                .map_err(|e| anyhow!("{}", e))?;
            if modified_time.is_some() && modified_time.unwrap() == time {
                return Ok(());
            }

            managed_repo_modified_time
                .write()
                .map_err(|e| anyhow!("{}", e))?
                .replace(time);
            *managed_pkg_indexes.write().map_err(|e| anyhow!("{}", e))? =
                serde_yaml::from_reader::<File, Vec<PackageIndex>>(File::open(index_file)?)?;
        }

        Ok(())
    }
}

#[async_trait]
impl CacheAsyncTrait for CacheService {
    async fn update_repositories(&self) -> anyhow::Result<()> {
        let config = self.container.get::<Config>().unwrap();

        let path = env::var(HUBER_PKG_ROOT_DIR).unwrap_or_default();
        if Path::new(&path).is_dir() {
            debug!(
                "Bypassed updating repositories, because {} is set to {}",
                HUBER_PKG_ROOT_DIR, path
            );
        } else {
            debug!("Updating huber repo");
            let dir = config.huber_repo_dir()?;

            debug!("Updating {:?}", dir);
            let client =
                GithubClient::new(config.to_github_credentials(), config.to_github_key_path());
            client.clone("innobead", "huber", dir).await?;
        }

        debug!("Updating external repos");
        let repo_service = self.container.get::<RepoService>().unwrap();
        for repo in repo_service.list()? {
            if let Some(url) = repo.url {
                debug!("Updating {:?}", config.external_repo_dir(&repo.name)?);
                repo_service
                    .download_save_pkgs_file_from_remote_github(&repo.name, &url)
                    .await?;
            } else if let Some(file) = repo.file {
                debug!("Updating {:?}", config.external_repo_dir(&repo.name)?);
                repo_service
                    .download_save_pkgs_file_from_local(&repo.name, &file)
                    .await?;
            } else if repo.name == LOCAL_REPO {
                debug!("Skip updating local repo");
            } else {
                debug!(
                    "Failed to update external repos due to empty url and file: {:?}",
                    &repo
                );
            }
        }

        Ok(())
    }
}
```

## File: `huber/src/service/config.rs`
```rust
use std::fs::{remove_file, File};
use std::sync::Arc;

use anyhow::anyhow;
use lazy_static::lazy_static;
use log::debug;
use simpledi_rs::di::{DIContainer, DIContainerExtTrait, DependencyInjectTrait};

use crate::error::HuberError;
use crate::model::config::{Config, ConfigPath};
use crate::service::ServiceTrait;

lazy_static! {
    pub static ref DEFAULT_CONFIG: Config = Default::default();
}

#[derive(Debug)]
pub struct ConfigService {
    pub container: Option<Arc<DIContainer>>,
}

unsafe impl Send for ConfigService {}

unsafe impl Sync for ConfigService {}

pub trait ConfigTrait {
    fn get(&self) -> anyhow::Result<Config>;
    fn update(&self, config: &Config) -> anyhow::Result<()>;
}

impl Default for ConfigService {
    fn default() -> Self {
        Self::new()
    }
}

impl ConfigService {
    pub fn new() -> Self {
        Self { container: None }
    }
}

impl ServiceTrait for ConfigService {}

impl DependencyInjectTrait for ConfigService {
    fn inject(&mut self, container: Arc<DIContainer>) {
        self.container = Some(container);
    }
}

impl ConfigTrait for ConfigService {
    fn get(&self) -> anyhow::Result<Config> {
        let config = self
            .container
            .get::<Config>()
            .expect("Failed to find config");
        let config_path = config.config_file()?;

        if config_path.exists() {
            debug!("Getting the config from {:?}", config_path);

            let f = File::open(&config_path)?;
            return Ok(serde_yaml::from_reader::<File, Config>(f)?);
        }

        Err(anyhow!(HuberError::ConfigNotFound(
            config_path.to_string_lossy().to_string()
        )))
    }

    fn update(&self, config: &Config) -> anyhow::Result<()> {
        let path = config.config_file()?;

        debug!("Updating the config {:?}: {:?}", path, config);
        if path.exists() {
            let _ = remove_file(&path);
        }
        let f = File::create(&path)?;
        serde_yaml::to_writer(f, &config)?;

        Ok(())
    }
}
```

## File: `huber/src/service/mod.rs`
```rust
use std::sync::Arc;

use anyhow::anyhow;
use async_trait::async_trait;
use simpledi_rs::di::{DIContainer, DIContainerTrait, DependencyInjectTrait};
use simpledi_rs::{create_dep, inject_dep};

use crate::model::config::Config;
use crate::model::repo::{Repository, LOCAL_REPO};
use crate::service::cache::{CacheService, CacheTrait};
use crate::service::config::ConfigService;
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;
use crate::service::repo::RepoService;
use crate::service::update::HuberUpdateService;

pub mod cache;
pub mod config;
pub mod package;
pub mod release;
pub mod repo;
pub mod update;

pub trait ServiceTrait: DependencyInjectTrait {}

pub trait ItemOperationTrait: ItemSearchTrait + ItemOperationAsyncTrait {
    type Item;
    type ItemInstance;
    type Condition;

    fn delete(&self, name: &str) -> anyhow::Result<()>;
    fn list(&self) -> anyhow::Result<Vec<Self::ItemInstance>>;
    fn get(&self, name: &str) -> anyhow::Result<Self::ItemInstance>;
    fn has(&self, name: &str) -> anyhow::Result<bool> {
        Ok(!self.search(Some(name), None, None, None)?.is_empty())
    }
}

#[async_trait]
pub trait ItemOperationAsyncTrait {
    type Item_;
    type ItemInstance_;
    type Condition_;

    async fn create(&self, obj: Self::Item_) -> anyhow::Result<Self::ItemInstance_>;
    async fn update(&self, obj: &Self::Item_) -> anyhow::Result<Self::ItemInstance_>;
    async fn find(&self, condition: &Self::Condition_) -> anyhow::Result<Vec<Self::ItemInstance_>>;
}

pub trait ItemSearchTrait {
    type SearchItem;

    fn search(
        &self,
        name: Option<&str>,
        pattern: Option<&str>,
        owner: Option<&str>,
        repo: Option<&str>,
    ) -> anyhow::Result<Vec<Self::SearchItem>>;
}

pub async fn init_services(config: &Config) -> Arc<DIContainer> {
    let mut container = DIContainer::new();

    create_dep!(CacheService::new(), container);
    create_dep!(config.clone(), container);
    create_dep!(ConfigService::new(), container);
    create_dep!(PackageService::new(), container);
    create_dep!(ReleaseService::new(), container);
    create_dep!(RepoService::new(), container);
    create_dep!(HuberUpdateService::new(), container);

    let container = container.init().unwrap();

    inject_dep!(PackageService, container.clone());
    inject_dep!(ReleaseService, container.clone());
    inject_dep!(CacheService, container.clone());
    inject_dep!(HuberUpdateService, container.clone());
    inject_dep!(RepoService, container.clone());
    inject_dep!(ConfigService, container.clone());

    let cache_service = container
        .get::<CacheService>()
        .expect("Failed to get cache service");

    cache_service
        .refresh_package_indexes()
        .expect("Failed to refresh package indexes");

    let repo_service = container
        .get::<RepoService>()
        .expect("Failed to get repo service");

    repo_service
        .create(Repository {
            name: LOCAL_REPO.to_string(),
            url: None,
            file: None,
        })
        .await
        .expect("Failed to create local repo");

    container
}

pub fn check_pkg_installed(
    pkg_service: &PackageService,
    release_service: &ReleaseService,
    pkg: &String,
) -> anyhow::Result<()> {
    if !pkg_service.has(pkg)? {
        return Err(anyhow!("Package {} not found", pkg));
    }

    if !release_service.has(pkg)? {
        return Err(anyhow!("Package {} not installed", pkg));
    }

    Ok(())
}
```

## File: `huber/src/service/package.rs`
```rust
use std::sync::Arc;

use anyhow::anyhow;
use async_trait::async_trait;
use log::debug;
use simpledi_rs::di::{DIContainer, DIContainerExtTrait, DependencyInjectTrait};

use crate::error::HuberError::PackageNotFound;
use crate::gh::{GithubClient, GithubClientTrait};
use crate::model::config::{Config, ConfigFieldConvertTrait};
use crate::model::package::{Package, PackageSource, PackageSummary};
use crate::model::release::{ReleaseKind, SortModelTrait};
use crate::service::cache::{CacheService, CacheTrait};
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait, ItemSearchTrait, ServiceTrait};

#[derive(Debug, Clone)]
pub struct PackageService {
    pub container: Option<Arc<DIContainer>>,
}

unsafe impl Send for PackageService {}

unsafe impl Sync for PackageService {}

impl Default for PackageService {
    fn default() -> Self {
        Self::new()
    }
}

impl PackageService {
    pub fn new() -> Self {
        Self { container: None }
    }

    pub async fn find_summary(
        &self,
        pkg_name: &str,
        release_build_only: bool,
    ) -> anyhow::Result<Vec<PackageSummary>> {
        let mut pkgs: Vec<PackageSummary> = self
            .find(&pkg_name.to_string())
            .await?
            .into_iter()
            .filter(|it| {
                if release_build_only {
                    return matches!(
                        it.release_kind.unwrap_or(ReleaseKind::PreRelease),
                        ReleaseKind::Release
                    );
                }
                true
            })
            .map(PackageSummary::from)
            .collect();

        pkgs.sort_by_version();
        Ok(pkgs)
    }
}

impl ServiceTrait for PackageService {}

impl DependencyInjectTrait for PackageService {
    fn inject(&mut self, container: Arc<DIContainer>) {
        self.container = Some(container)
    }
}

impl ItemOperationTrait for PackageService {
    type Item = Package;
    type ItemInstance = Package;
    type Condition = String;

    fn delete(&self, _name: &str) -> anyhow::Result<()> {
        unimplemented!()
    }

    fn list(&self) -> anyhow::Result<Vec<Self::ItemInstance>> {
        debug!("Getting all packages");

        self.search(None, None, None, None)
    }

    fn get(&self, name: &str) -> anyhow::Result<Self::ItemInstance> {
        debug!("Getting package: {}", name);

        let results = self.search(Some(name), None, None, None)?;
        if !results.is_empty() {
            Ok(results.first().unwrap().to_owned())
        } else {
            Err(anyhow!(PackageNotFound(name.into())))
        }
    }
}

#[async_trait]
impl ItemOperationAsyncTrait for PackageService {
    type Item_ = Package;
    type ItemInstance_ = Package;
    type Condition_ = String;

    async fn create(&self, _obj: Self::Item_) -> anyhow::Result<Self::ItemInstance_> {
        unimplemented!()
    }

    async fn update(&self, _obj: &Self::Item_) -> anyhow::Result<Self::ItemInstance_> {
        unimplemented!()
    }

    async fn find(&self, pkg_name: &Self::Condition_) -> anyhow::Result<Vec<Self::ItemInstance_>> {
        debug!("Finding packages: {}", pkg_name);

        let config = self.container.get::<Config>().unwrap();
        let client = GithubClient::new(config.to_github_credentials(), config.to_github_key_path());
        let pkg = self.get(pkg_name)?;

        match &pkg.source {
            PackageSource::Github { owner, repo } => {
                let releases = client.get_releases(owner, repo, &pkg).await?;
                Ok(releases
                    .into_iter()
                    .map(|it| {
                        let mut pkg = it.package;
                        pkg.version = Some(it.version);
                        pkg.release_kind = it.kind;

                        pkg
                    })
                    .collect())
            }
        }
    }
}

impl ItemSearchTrait for PackageService {
    type SearchItem = Package;

    fn search(
        &self,
        name: Option<&str>,
        pattern: Option<&str>,
        owner: Option<&str>,
        repo: Option<&str>,
    ) -> anyhow::Result<Vec<Self::SearchItem>> {
        let cache_service = self.container.get::<CacheService>().unwrap();

        let owner = owner.unwrap_or("");
        let mut found_items: Vec<Self::SearchItem> = vec![];

        if let Some(pattern) = pattern {
            debug!("Searching package by pattern: {}", pattern);

            let mut found_pkgs = cache_service.list_packages(pattern, owner, repo)?;
            found_items.append(&mut found_pkgs);

            return Ok(found_items);
        }

        if let Some(name) = name {
            debug!("Searching package by name: {}", name);

            match cache_service.get_package(name, repo) {
                Ok(pkg) => found_items.push(pkg),
                Err(err) => debug!("{}", err),
            }

            return Ok(found_items);
        }

        debug!("Searching all packages");
        let mut all_pkgs = cache_service.list_packages("", owner, repo)?;
        found_items.append(&mut all_pkgs);

        Ok(found_items)
    }
}
```

## File: `huber/src/service/release.rs`
```rust
use std::collections::HashMap;
use std::fs::{read_dir, read_link, remove_dir_all, remove_file, File};
use std::io::Write;
use std::path::PathBuf;
use std::sync::Arc;
use std::{env, fs};

use anyhow::anyhow;
use async_trait::async_trait;
use filepath::FilePath;
use fs_extra::move_items;
use is_executable::IsExecutable;
use log::{debug, error, info};
use maplit::hashmap;
use regex::Regex;
use simpledi_rs::di::{DIContainer, DIContainerExtTrait, DependencyInjectTrait};
use symlink::{remove_symlink_dir, remove_symlink_file, symlink_dir, symlink_file};
use url::Url;
use urlencoding::decode;

use crate::cmd::PlatformStdLib;
use crate::compress::uncompress_archive;
use crate::fs::has_suffix;
use crate::fs::set_executable_permission;
use crate::gh::{GithubClient, GithubClientTrait};
use crate::model::config::{Config, ConfigFieldConvertTrait, ConfigPath};
use crate::model::package::{GithubPackage, Package, PackageDetailType, PackageSource};
use crate::model::release::{Release, ReleaseIndex};
use crate::os::{is_os_arch_match, trim_os_arch_version};
use crate::service::package::PackageService;
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait, ItemSearchTrait, ServiceTrait};

const SUPPORTED_ARCHIVE_TYPES: [&str; 6] = ["tar.gz", "tar.xz", "zip", "tar", "tgz", "gz"];

pub trait ReleaseTrait {
    fn current(&self, pkg: &Package) -> anyhow::Result<Release>;
    fn clean_current(&self, release: &Release) -> anyhow::Result<()>;
    fn reset_current(&self, pkg: &Package) -> anyhow::Result<()>;

    fn unlink_executables_for_current(&self, pkg: &Package) -> anyhow::Result<()>;

    fn get_executables_for_current(
        &self,
        pkg: &Package,
        symlink: bool,
    ) -> anyhow::Result<Vec<String>>;
    fn delete_release(&self, release: &Release) -> anyhow::Result<()>;
}

#[async_trait]
pub trait ReleaseAsyncTrait {
    async fn download_install_github_package(
        &self,
        package: &Package,
        package_github: &GithubPackage,
        prefer_stdlib: &PlatformStdLib,
    ) -> anyhow::Result<()>;

    async fn set_current(&self, release: &mut Release) -> anyhow::Result<Vec<String>>;
}

#[derive(Debug, Clone)]
pub struct ReleaseService {
    pub container: Option<Arc<DIContainer>>,
}

unsafe impl Send for ReleaseService {}

unsafe impl Sync for ReleaseService {}

impl ServiceTrait for ReleaseService {}

impl DependencyInjectTrait for ReleaseService {
    fn inject(&mut self, container: Arc<DIContainer>) {
        self.container = Some(container)
    }
}

impl Default for ReleaseService {
    fn default() -> Self {
        Self::new()
    }
}

impl ReleaseService {
    pub fn new() -> Self {
        Self { container: None }
    }

    pub async fn get_latest(&self, pkg: &Package) -> anyhow::Result<Release> {
        debug!("Getting the latest release: {}", pkg);

        let config = self.container.get::<Config>().unwrap();
        let client = GithubClient::new(config.to_github_credentials(), config.to_github_key_path());

        match &pkg.source {
            PackageSource::Github { owner, repo } => {
                client.get_latest_release(owner, repo, pkg).await
            }
        }
    }

    pub async fn update(
        &self,
        obj: &Package,
        prefer_stdlib: &PlatformStdLib,
        release_check: bool,
    ) -> anyhow::Result<Release> {
        debug!("Updating release from package: {:#?}", &obj);

        let config = self.container.get::<Config>().unwrap();
        let client = GithubClient::new(config.to_github_credentials(), config.to_github_key_path());

        // Get the release from GitHub
        let mut release = if release_check {
            match obj.source {
                PackageSource::Github {
                    ref owner,
                    ref repo,
                } => match obj.version {
                    Some(ref v) => {
                        debug!("Getting {} of package release {}", &v, &obj);
                        client.get_release(owner, repo, v, obj).await?
                    }
                    None => {
                        debug!("Getting the latest release of package {}", &obj);

                        if let Ok(r) = client.get_latest_release(owner, repo, obj).await {
                            r
                        } else {
                            debug!("Getting the latest pre-release of package {}", &obj);
                            client
                                .get_releases(owner, repo, obj)
                                .await?
                                .first()
                                .expect("Failed to find the first release")
                                .to_owned()
                        }
                    }
                },
            }
        } else {
            Release {
                package: obj.clone(),
                version: obj.version.clone().unwrap_or_default(),
                current: false,
                executables: None,
                name: "".to_string(),
                kind: None,
            }
        };

        let release_detail = release.package.detail.clone().or_else(|| {
            Some(PackageDetailType::Github {
                package: GithubPackage {
                    tag_name: obj.version.clone().unwrap_or_default(),
                    ..Default::default()
                },
            })
        });
        if release_detail.is_none() {
            return Err(anyhow!("No matched release detail found: {}", release));
        }

        match release_detail.unwrap() {
            PackageDetailType::Github { package: p } => {
                debug!(
                    "Downloading package artifacts from github {:?}",
                    obj.source.url()
                );
                self.download_install_github_package(obj, &p, prefer_stdlib)
                    .await?;

                debug!("Setting {} as the current package", release);
                let executables = self.set_current(&mut release).await?;
                info!(
                    "Installed executables of {}:\n{:#?}",
                    obj.name, &executables
                );
                release.executables = Some(executables);

                Ok(release)
            }
        }
    }

    fn get_assets(package: &Package, version: &str) -> anyhow::Result<Vec<String>> {
        let asset_names: Vec<String> = package
            .target()?
            .artifact_templates
            .iter()
            .map(|it| {
                it.replace("{version}", version.trim_start_matches("v"))
                    .replace("{os}", env::consts::OS)
                    .replace("{arch}", env::consts::ARCH)
            })
            .filter(|it| {
                let file_name = if let Ok(url) = Url::parse(it) {
                    url.path_segments().unwrap().last().unwrap().to_string()
                } else {
                    it.clone()
                };

                if file_name.contains('.') && !file_name.ends_with(".exe") {
                    SUPPORTED_ARCHIVE_TYPES
                        .iter()
                        .any(|ext| file_name.ends_with(ext))
                } else {
                    true
                }
            })
            .collect();

        Ok(asset_names)
    }

    async fn download_assets(
        &self,
        package: &Package,
        config: &Config,
        version: &str,
        download_urls: &mut Vec<String>,
    ) -> anyhow::Result<()> {
        let mut tasks = vec![];

        'download: for download_url in download_urls {
            let pkg_dir = config.installed_pkg_dir(package, version)?;
            let filename = download_url.split("/").last().unwrap().to_string();
            let download_file_path = config.temp_dir()?.join(&filename);

            let mut ext = "";
            let trimmed_filename = trim_os_arch_version(&filename);

            for (i, &archive_type) in SUPPORTED_ARCHIVE_TYPES.iter().enumerate() {
                if trimmed_filename.ends_with(archive_type) {
                    ext = archive_type;
                    break;
                }
                if !has_suffix(&trimmed_filename) {
                    break;
                }
                if i == SUPPORTED_ARCHIVE_TYPES.len() - 1 {
                    debug!("Ignored to download {} due to unsupported archive type. Supported types: {:?}",&download_url, SUPPORTED_ARCHIVE_TYPES);
                    continue 'download;
                }
            }

            let task = async move {
                info!("Downloading {}", &download_url);
                debug!("Downloading {} to {:?}", &download_url, &download_file_path);

                let _ = remove_file(&download_file_path);
                let _ = remove_dir_all(&download_file_path);

                let response = reqwest::get(download_url.to_string()).await?;
                match response.error_for_status() {
                    Err(e) => return Err(anyhow!("{:?}", e)),

                    Ok(response) => {
                        let mut dest_f = File::create(&download_file_path)?;
                        let bytes = response.bytes().await?;
                        dest_f.write_all(&bytes)?;
                    }
                }

                // downloaded asset seems an executable instead of an archive, move it to the package directory
                if ext.is_empty() {
                    let dest_f = pkg_dir.join(&filename);

                    debug!(
                        "Moving {:?} to {:?}, because it's not an archive, regarded as an executable",
                        &download_file_path, &dest_f
                    );
                    set_executable_permission(&download_file_path)?;

                    let option = fs_extra::file::CopyOptions {
                        overwrite: false,
                        skip_exist: true,
                        buffer_size: 0,
                    };
                    fs_extra::file::move_file(&download_file_path, &dest_f, &option)?;

                    return Ok(());
                }

                Self::decompress_asset(&pkg_dir, &filename, &download_file_path, ext)?;

                Ok(())
            };

            tasks.push(task);
        }

        let downloaded = futures::future::join_all(tasks)
            .await
            .iter()
            .map(|r| {
                if let Err(e) = r {
                    error!("Failed to download asset: {}", e);
                }
                r.as_ref()
            })
            .all(|r| r.is_ok());

        if !downloaded {
            return Err(anyhow!("Failed to download assets"));
        }

        Ok(())
    }

    fn decompress_asset(
        pkg_dir: &PathBuf,
        filename: &str,
        download_file_path: &PathBuf,
        ext: &str,
    ) -> anyhow::Result<()> {
        debug!("Decompressing {} which has extension {:?}", filename, ext);

        let extract_dir = download_file_path.parent().unwrap().join("extract");
        let download_file = File::open(download_file_path)?;

        debug!("Decompressing {:?} to {:?}", &download_file, &extract_dir);

        fs::create_dir_all(&extract_dir)?;
        uncompress_archive(&download_file.path()?, &extract_dir, ext)?;

        let dir = read_dir(&extract_dir)?;
        let mut extract_content_dir = extract_dir.clone();
        if dir.count() == 1 {
            let dir = read_dir(&extract_dir)?;
            let entry = dir.into_iter().next().unwrap()?;
            extract_content_dir = entry.path();
        }

        let mut symbolic_links: HashMap<PathBuf, PathBuf> = hashmap! {};
        let items_to_copy: Vec<PathBuf> = if extract_content_dir.is_dir() {
            debug!("Moving {:?}/* to {:?}", &extract_content_dir, &pkg_dir);
            extract_content_dir
                .read_dir()?
                .filter_map(|it| {
                    let p = it.unwrap().path();

                    match read_link(&p) {
                        Ok(src_link) => {
                            let dest_link = pkg_dir.join(p.file_name().unwrap().to_str().unwrap());
                            symbolic_links.insert(dest_link, src_link.clone());

                            None
                        }

                        Err(_) => Some(p),
                    }
                })
                .collect()
        } else {
            debug!("Moving {:?} to {:?}", &extract_content_dir, &pkg_dir);
            vec![extract_content_dir]
        };

        let mut option = fs_extra::dir::CopyOptions::new();
        option.overwrite = true;
        move_items(&items_to_copy, pkg_dir, &option)?;

        for (dest_link, src_link) in symbolic_links {
            debug!("Add extra linked files {:?} to {:?}", src_link, dest_link);
            symlink_file(src_link, dest_link)?
        }

        debug!(
            "Removing temp files {:?}, {:?}",
            download_file_path, extract_dir
        );

        let _ = remove_file(download_file_path);
        let _ = remove_dir_all(download_file_path);
        let _ = remove_dir_all(&extract_dir);
        Ok(())
    }
}

impl ReleaseTrait for ReleaseService {
    fn current(&self, pkg: &Package) -> anyhow::Result<Release> {
        debug!("Getting the current release: {}", &pkg);

        let config = self.container.get::<Config>().unwrap();
        let f = config.current_pkg_manifest_file(pkg)?;
        let f = File::open(f)?;

        // add linked executables in the release
        let mut release: Release = serde_yaml::from_reader(f)?;
        let executables = self.get_executables_for_current(&release.package, false)?;
        release.executables = Some(executables);

        Ok(release)
    }

    fn clean_current(&self, release: &Release) -> anyhow::Result<()> {
        debug!("Cleaning the current release: {}", &release);

        let config = self.container.get::<Config>().unwrap();

        let p = config.installed_pkg_manifest_file(&release.package, &release.version)?;
        let f = File::open(&p)?;
        let mut r: Release = serde_yaml::from_reader(&f)?;
        r.current = false;
        remove_file(&p)?;

        let f = File::create(&p)?;
        Ok(serde_yaml::to_writer(f, &r)?)
    }

    fn reset_current(&self, pkg: &Package) -> anyhow::Result<()> {
        debug!("Cleaning {} from the current manifests", &pkg);

        let config = self.container.get::<Config>().unwrap();

        // remove old symlink bin, current
        debug!("Removing the current package symbolic links: {}", &pkg);

        let current_pkg_dir = config.current_pkg_dir(pkg)?;
        if current_pkg_dir.exists() {
            self.unlink_executables_for_current(pkg)?;

            debug!("Removing link {:?}", &current_pkg_dir);
            remove_symlink_dir(&current_pkg_dir)?;
        }

        // remove it from index
        debug!("Removing {} from the current index", &pkg);

        let index_f = config.current_index_file()?;
        let indexes = if index_f.exists() {
            let f = File::open(&index_f)?;
            let indexes: Vec<ReleaseIndex> = serde_yaml::from_reader(&f)?;

            indexes
                .into_iter()
                .filter(|it| it.name != pkg.name)
                .collect()
        } else {
            vec![]
        };

        let _ = remove_file(&index_f);

        if !indexes.is_empty() {
            let index_f = File::create(&index_f)?;
            serde_yaml::to_writer(index_f, &indexes)?;
        }

        Ok(())
    }

    fn unlink_executables_for_current(&self, pkg: &Package) -> anyhow::Result<()> {
        let exec_paths = self.get_executables_for_current(pkg, false)?;
        for ref exec_path in exec_paths {
            debug!("Removing link {:?}", exec_path);
            remove_symlink_file(exec_path)?;
        }

        Ok(())
    }

    //noinspection ALL
    fn get_executables_for_current(
        &self,
        pkg: &Package,
        symlink: bool,
    ) -> anyhow::Result<Vec<String>> {
        let config = self.container.get::<Config>().unwrap();
        let mut results: Vec<String> = vec![];

        let pkg_dir = config.current_pkg_dir(pkg)?;
        let pkg_bin_dir = config.current_pkg_bin_dir(pkg)?;
        let exec_mappings: HashMap<_, _> = pkg.target()?.executable_mappings.unwrap_or_default();

        let semver_regex = Regex::new(
            r"v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?",
        )?;

        for dir in &[pkg_dir, pkg_bin_dir] {
            debug!("Scanning executables in {:?}", dir);

            if !dir.exists() {
                debug!("Ignored scanning {:?}, because it does not exist", dir);
                continue;
            }

            for entry in read_dir(dir)? {
                let exec_path = entry?.path();
                if !exec_path.is_executable() {
                    debug!("Ignored non-executable {:?}", exec_path);
                    continue;
                } else if has_suffix(&trim_os_arch_version(
                    &exec_path.file_name().unwrap().to_string_lossy(),
                )) {
                    debug!("Ignored executable {:?} due to suffix", exec_path);
                    continue;
                }

                let mut exec_name = exec_path.file_name().unwrap().to_string_lossy().to_string();
                exec_name = semver_regex.replace(&exec_name, "").to_string();
                exec_name = exec_mappings
                    .get(&exec_name)
                    .unwrap_or(&exec_name)
                    .to_string();

                let exec_link = config.bin_dir()?.join(trim_os_arch_version(&exec_name));
                if symlink {
                    let _ = remove_file(&exec_link);
                    symlink_file(&exec_path, &exec_link)?;
                }
                if exec_link.exists() {
                    results.push(exec_link.to_string_lossy().to_string());
                }
            }
        }

        Ok(results)
    }

    fn delete_release(&self, release: &Release) -> anyhow::Result<()> {
        debug!("Removing release: {}", &release);

        let cr = self.current(&release.package)?;
        if cr.version == release.version {
            return Err(anyhow!(
                "{} is the current release, unable to remove",
                release
            ));
        }

        let config = self.container.get::<Config>().unwrap();
        let p = config.installed_pkg_dir(&release.package, &release.version)?;

        Ok(remove_dir_all(p)?)
    }
}

#[async_trait]
impl ReleaseAsyncTrait for ReleaseService {
    async fn download_install_github_package(
        &self,
        package: &Package,
        package_github: &GithubPackage,
        prefer_stdlib: &PlatformStdLib,
    ) -> anyhow::Result<()> {
        debug!("Downloading github package artifacts {}", &package);

        let config = self.container.get::<Config>().unwrap();
        let version = package.parse_version_from_tag_name(&package_github.tag_name)?;

        let mut asset_names = Self::get_assets(package, &version)?;

        let mut ext_asset_urls: Vec<String> = asset_names // external assets not on github
            .iter()
            .filter(|it| Url::parse(it).is_ok() && it.starts_with("https"))
            .cloned()
            .collect();
        let mut asset_download_urls: Vec<String> = vec![];
        asset_download_urls.append(&mut ext_asset_urls);

        if !ext_asset_urls.is_empty() {
            asset_names.retain(|it| !ext_asset_urls.contains(it));
        }

        for asset in package_github.assets.iter() {
            let asset_url = decode(&asset.browser_download_url)?.to_string();

            if asset_names.is_empty() {
                debug!(
                    "Checking {} if it's in the expected os/arch type: {}, since there are no expected artifact names defined",
                    asset.name, asset_url
                );
                if !is_os_arch_match(
                    env::consts::OS,
                    env::consts::ARCH,
                    &asset_url.to_lowercase(),
                ) {
                    continue;
                }
            } else {
                debug!(
                    "Checking {} if it's in the expected artifact names: {:?}",
                    asset.name, asset_names
                );
                if !asset_names.contains(&asset.name)
                    && !asset_names.iter().any(|it| asset_url.ends_with(it))
                {
                    debug!(
                    "Ignored {}, not mentioned or not right arch type defined in the package artifact config",
                    asset.name
                );
                    continue;
                }
            }

            debug!("Found asset: {}", asset_url);
            asset_download_urls.push(asset_url.to_string());
        }

        if !package_github.assets.is_empty() && asset_download_urls.is_empty() {
            return Err(anyhow!(
                "No available artifacts for {} to download. Expected artifact names: {:?}",
                package.name,
                asset_names
            ));
        }

        if prefer_stdlib != &PlatformStdLib::None {
            info!(
                "Prefer downloading assets for {} belonging to the specified stdlib: {}",
                package.name,
                prefer_stdlib
            );

            let stdlib_regex = Regex::new(&format!(
                r"\b{}\b?",
                prefer_stdlib.to_string().to_lowercase()
            ))?;
            let results: Vec<_> = asset_download_urls
                .clone()
                .into_iter()
                .filter(|it| {
                    let filename = Url::parse(it)
                        .unwrap()
                        .path_segments()
                        .and_then(|segments| segments.last())
                        .unwrap_or_default()
                        .to_string();
                    stdlib_regex.is_match(&filename)
                })
                .collect();
            if !results.is_empty() {
                asset_download_urls = results;
            }
        }

        self.download_assets(package, config, &version, &mut asset_download_urls)
            .await?;

        Ok(())
    }

    async fn set_current(&self, release: &mut Release) -> anyhow::Result<Vec<String>> {
        debug!("Setting the current release: {}", &release);

        release.current = true;
        release.name = release.package.name.clone();

        debug!(
            "Removing the old current release symbolic links: {}",
            &release.package
        );
        self.reset_current(&release.package)?;

        debug!("Updating the current release symbolic links: {}", &release);

        let config = self.container.get::<Config>().unwrap();
        let current_pkg_dir = config.current_pkg_dir(&release.package)?;
        let source = config.installed_pkg_dir(&release.package, &release.version)?;

        symlink_dir(&source, &current_pkg_dir)?;

        let linked_exe_files = self.get_executables_for_current(&release.package, true)?;
        if linked_exe_files.is_empty() {
            return Err(anyhow!("No executables found when installing {}", &release));
        }

        // update old current release manifest
        let index_f = config.current_index_file()?;
        let mut indexes: Vec<ReleaseIndex> = vec![];

        debug!("Updating the current index manifest: {:?}", &index_f);

        if index_f.exists() {
            let f = File::open(&index_f)?;
            indexes = serde_yaml::from_reader(&f)?;

            if let Some(found) = indexes.iter().find(|it| it.name == release.package.name) {
                let old_pkg_manifest_path =
                    config.installed_pkg_manifest_file(&release.package, &found.version)?;
                let f = File::open(&old_pkg_manifest_path)?;

                let mut r: Release = serde_yaml::from_reader(f)?;
                r.current = false;

                let _ = remove_file(&old_pkg_manifest_path);
                let f = File::create(&old_pkg_manifest_path)?;
                serde_yaml::to_writer(f, &r)?;
            }

            indexes.retain(|it| it.name != release.package.name);
        }

        indexes.push(ReleaseIndex {
            name: release.package.name.clone(),
            version: release.version.clone(),
            owner: release.package.source.owner().to_string(),
            source: release.package.source.to_string(),
        });

        // update current release index file
        let _ = remove_file(&index_f);
        let index_f = File::create(&index_f)?;
        serde_yaml::to_writer(index_f, &indexes)?;

        let release_f = config.installed_pkg_manifest_file(&release.package, &release.version)?;
        let _ = remove_file(&release_f);
        let release_f = File::create(release_f)?;
        serde_yaml::to_writer(release_f, &release)?;

        // clean other installed releases as non-current
        let releases = self.find(&release.package).await?;
        let inactive_releases: Vec<&Release> = releases
            .iter()
            .filter(|it| it.version != release.version)
            .collect();

        for r in inactive_releases {
            self.clean_current(r)?;
        }

        Ok(linked_exe_files)
    }
}

impl ItemOperationTrait for ReleaseService {
    type Item = Package;
    type ItemInstance = Release;
    type Condition = Package;

    fn delete(&self, name: &str) -> anyhow::Result<()> {
        debug!("Deleting releases of package {}", name);

        let config = self.container.get::<Config>().unwrap();
        let pkg_service = self.container.get::<PackageService>().unwrap();
        let release_service = self.container.get::<ReleaseService>().unwrap();

        let pkg = pkg_service.get(name)?;
        let release = release_service.current(&pkg)?;

        self.reset_current(&release.package)?;

        let dir = config.installed_pkg_base_dir(&pkg)?;
        Ok(remove_dir_all(dir)?)
    }

    fn list(&self) -> anyhow::Result<Vec<Self::ItemInstance>> {
        debug!("Getting all current releases");

        let config = self.container.get::<Config>().unwrap();
        let mut releases: Vec<Release> = vec![];

        let index_f = config.current_index_file()?;
        if !index_f.exists() {
            return Ok(releases);
        }
        let index_f = File::open(index_f)?;

        let pkg_service = self.container.get::<PackageService>().unwrap();
        let indexes: Vec<ReleaseIndex> = serde_yaml::from_reader(index_f)?;

        for ri in indexes {
            match pkg_service.get(&ri.name) {
                Ok(pkg) => {
                    let p = config.installed_pkg_manifest_file(&pkg, &ri.version)?;

                    debug!("Reading {:?}", p);
                    match File::open(&p) {
                        Ok(f) => {
                            releases.push(serde_yaml::from_reader(f)?);
                        }
                        Err(e) => debug!(
                            "Failed to read {:?} and ignored from the installed release list: {}",
                            p, e
                        ),
                    }
                }
                Err(e) => {
                    return Err(anyhow!(
                        "Failed to get the installed {} package: {}",
                        &ri.name,
                        e
                    ));
                }
            }
        }

        Ok(releases)
    }

    fn get(&self, _name: &str) -> anyhow::Result<Self::ItemInstance> {
        unimplemented!()
    }
}

#[async_trait]
impl ItemOperationAsyncTrait for ReleaseService {
    type Item_ = Package;
    type ItemInstance_ = Release;
    type Condition_ = Package;

    async fn create(&self, obj: Self::Item_) -> anyhow::Result<Self::ItemInstance_> {
        debug!("Creating release from package: {}", &obj);

        if self.has(&obj.name)? {
            return Err(anyhow!("{} already installed", &obj.name));
        }

        self.update(&obj, &PlatformStdLib::None, true).await
    }

    async fn update(&self, _obj: &Self::Item_) -> anyhow::Result<Self::ItemInstance_> {
        unimplemented!()
    }

    async fn find(&self, pkg: &Self::Condition_) -> anyhow::Result<Vec<Self::ItemInstance_>> {
        debug!("Finding releases by condition: {}", &pkg);

        let config = self.container.get::<Config>().unwrap();

        let mut releases: Vec<Release> = vec![];

        let pkg_base_dir = config.installed_pkg_base_dir(pkg)?;
        for entry in read_dir(&pkg_base_dir)? {
            let entry = entry?;
            let filename = entry.file_name().to_string_lossy().to_string();

            if filename == "current" {
                continue;
            }

            if entry.path().is_dir() {
                let p = config.installed_pkg_manifest_file(pkg, &filename)?;
                if !p.exists() {
                    debug!("Ignored {:?}, because the manifest file does not exist", p);
                    continue;
                }

                let f = File::open(p)?;
                let r: Release = serde_yaml::from_reader(f)?;
                releases.push(r);
            }
        }

        Ok(releases)
    }
}

impl ItemSearchTrait for ReleaseService {
    type SearchItem = Release;

    fn search(
        &self,
        name: Option<&str>,
        _pattern: Option<&str>,
        _owner: Option<&str>,
        _repo: Option<&str>,
    ) -> anyhow::Result<Vec<Self::SearchItem>> {
        debug!("Searching releases");

        let mut found_items: Vec<Self::SearchItem> = vec![];
        let releases = self.list()?;

        for r in releases.iter() {
            if name.is_some() && r.package.name != name.unwrap() {
                continue;
            }

            let mut updated_r = r.clone();

            if releases.iter().any(|it| it.version == r.version) {
                updated_r.current = true;
            }

            found_items.push(updated_r);
        }

        Ok(found_items)
    }
}
```

## File: `huber/src/service/repo.rs`
```rust
use std::fs::{read_dir, remove_dir_all, remove_file, File};
use std::io::Write;
use std::path::Path;
use std::sync::Arc;

use anyhow::anyhow;
use async_trait::async_trait;
use log::debug;
use simpledi_rs::di::{DIContainer, DIContainerExtTrait, DependencyInjectTrait};

use crate::model::config::{Config, ConfigPath};
use crate::model::package::Package;
use crate::model::repo::{Repository, LOCAL_REPO};
use crate::service::{ItemOperationAsyncTrait, ItemOperationTrait, ItemSearchTrait, ServiceTrait};

pub trait RepoTrait {
    fn get_packages_by_repo(&self, name: &str) -> anyhow::Result<Vec<Package>>;
}

#[async_trait]
pub trait RepoAsyncTrait {
    async fn download_save_pkgs_file_from_remote_github(
        &self,
        name: &str,
        url: &str,
    ) -> anyhow::Result<()>;
    async fn download_save_pkgs_file_from_local<P: AsRef<Path> + Send>(
        &self,
        name: &str,
        url: P,
    ) -> anyhow::Result<()>;
    async fn create_local_repo(&self) -> anyhow::Result<()>;
    async fn add_pkgs_to_repo(&self, name: &str, pkgs: &[Package]) -> anyhow::Result<()>;
}

#[derive(Debug, Clone)]
pub struct RepoService {
    pub container: Option<Arc<DIContainer>>,
}

unsafe impl Send for RepoService {}

unsafe impl Sync for RepoService {}

impl ServiceTrait for RepoService {}

impl DependencyInjectTrait for RepoService {
    fn inject(&mut self, container: Arc<DIContainer>) {
        self.container = Some(container);
    }
}

impl Default for RepoService {
    fn default() -> Self {
        Self::new()
    }
}

impl RepoService {
    pub fn new() -> Self {
        Self { container: None }
    }
}

impl ItemSearchTrait for RepoService {
    type SearchItem = Repository;

    fn search(
        &self,
        name: Option<&str>,
        _pattern: Option<&str>,
        _owner: Option<&str>,
        _repo: Option<&str>,
    ) -> anyhow::Result<Vec<Self::SearchItem>> {
        let repo = self.list()?.into_iter().find(|it| it.name == name.unwrap());
        if repo.is_some() {
            return Ok(vec![repo.unwrap()]);
        }

        Ok(vec![])
    }
}

impl ItemOperationTrait for RepoService {
    type Item = Repository;
    type ItemInstance = Repository;
    type Condition = String;

    fn delete(&self, name: &str) -> anyhow::Result<()> {
        let config = self.container.get::<Config>().unwrap();

        let path = config.external_repo_dir(name)?;
        if path.exists() {
            debug!("{:?} removed", path);
            let _ = remove_dir_all(path);
        }

        Ok(())
    }

    // FIXME enhance performance
    fn list(&self) -> anyhow::Result<Vec<Self::ItemInstance>> {
        let config = self.container.get::<Config>().unwrap();

        let mut repos: Vec<Repository> = vec![];
        let path = config.repo_root_dir()?;

        for entry in read_dir(&path)? {
            let entry = entry?;
            let path = entry.path();

            if path.is_dir() {
                let dir_name = path.file_name().unwrap().to_str().unwrap();
                // not include managed repo
                if dir_name == "huber" {
                    continue;
                }

                let repo_f = config.external_repo_file(dir_name)?;
                if repo_f.exists() {
                    let f = File::open(&repo_f)?;
                    let result: Repository = serde_yaml::from_reader(f)?;
                    repos.push(result);
                }
            }
        }

        Ok(repos)
    }

    fn get(&self, _name: &str) -> anyhow::Result<Self::ItemInstance> {
        unimplemented!()
    }
}

#[async_trait]
impl ItemOperationAsyncTrait for RepoService {
    type Item_ = Repository;
    type ItemInstance_ = Repository;
    type Condition_ = String;

    async fn create(&self, obj: Self::Item_) -> anyhow::Result<Self::ItemInstance_> {
        let config = self.container.get::<Config>().unwrap();

        debug!("Creating external repo: {:?}", &obj);
        match &obj {
            _ if obj.url.is_some() => {
                self.download_save_pkgs_file_from_remote_github(
                    &obj.name,
                    obj.url.as_ref().unwrap(),
                )
                .await?
            }

            _ if obj.file.is_some() => {
                self.download_save_pkgs_file_from_local(&obj.name, obj.file.as_ref().unwrap())
                    .await?
            }

            _ => {
                if obj.name == LOCAL_REPO {
                    self.create_local_repo().await?;
                } else {
                    return Err(anyhow!("Repo file or url not provided: {:?}", &obj));
                }
            }
        }

        let path = config.external_repo_file(&obj.name)?;
        let file = File::create(&path)?;
        serde_yaml::to_writer(file, &obj)?;

        Ok(obj)
    }

    async fn update(&self, _obj: &Self::Item_) -> anyhow::Result<Self::ItemInstance_> {
        unimplemented!()
    }

    async fn find(
        &self,
        _condition: &Self::Condition_,
    ) -> anyhow::Result<Vec<Self::ItemInstance_>> {
        unimplemented!()
    }
}

impl RepoTrait for RepoService {
    fn get_packages_by_repo(&self, name: &str) -> anyhow::Result<Vec<Package>> {
        let config = self.container.get::<Config>().unwrap();
        let f = config.external_repo_pkgs_file(name)?;
        let f = File::open(&f)?;

        Ok(serde_yaml::from_reader(f)?)
    }
}

#[async_trait]
impl RepoAsyncTrait for RepoService {
    async fn download_save_pkgs_file_from_remote_github(
        &self,
        name: &str,
        url: &str,
    ) -> anyhow::Result<()> {
        let config = self.container.get::<Config>().unwrap();

        let path = config.external_repo_pkgs_file(name)?;
        if path.exists() {
            let _ = remove_file(&path);
        }

        let mut url = url.to_string();
        debug!("Saving {} to {:?}", &url, &path);

        let from_github = url.contains("raw.githubusercontent.com");
        if from_github {
            if let Some(token) = config.github_token.clone() {
                let re = regex::Regex::new(r"(http|https)://")?;
                url = re
                    .replace(&url, format!("$1://{}@", token).as_str())
                    .to_string()
            }
        }

        let response = reqwest::get(&url.to_string()).await?;
        match response.error_for_status() {
            Err(e) => Err(anyhow!("{:?}", e)),
            Ok(response) => {
                let mut f = File::create(&path)?;
                let bytes = response.bytes().await?;
                f.write_all(&bytes)?;

                Ok(())
            }
        }
    }

    async fn download_save_pkgs_file_from_local<P: AsRef<Path> + Send>(
        &self,
        name: &str,
        url: P,
    ) -> anyhow::Result<()> {
        let f = File::open(&url)?;
        let pkgs: Vec<Package> = get_packages_from_file(f)?;

        let config = self.container.get::<Config>().unwrap();
        let path = config.external_repo_pkgs_file(name)?;
        if path.exists() {
            let _ = remove_file(&path);
        }

        debug!("Saving {:?} to {:?}", url.as_ref(), &path);

        let f = File::create(&path)?;
        serde_yaml::to_writer(&f, &pkgs)?;

        Ok(())
    }

    async fn create_local_repo(&self) -> anyhow::Result<()> {
        let config = self.container.get::<Config>().unwrap();
        let path = config.external_repo_pkgs_file(LOCAL_REPO)?;
        if !path.exists() {
            debug!("Creating local repo {:?}", &path);
            let f = File::create(&path)?;
            serde_yaml::to_writer::<&_, Vec<Package>>(&f, &vec![])?;
        }

        Ok(())
    }

    async fn add_pkgs_to_repo(&self, name: &str, pkgs: &[Package]) -> anyhow::Result<()> {
        let mut pkgs_to_update = self.get_packages_by_repo(name)?;
        let mut update_required = false;

        for p in pkgs {
            if pkgs_to_update.iter().any(|it| it.name == p.name) {
                continue;
            }
            pkgs_to_update.push(p.clone());
            update_required = true;
        }

        if update_required {
            let config = self.container.get::<Config>().unwrap();
            let path = config.external_repo_pkgs_file(name)?;
            let f = File::create(&path)?;
            serde_yaml::to_writer(&f, &pkgs_to_update)?;
        }

        Ok(())
    }
}

fn get_packages_from_file(f: File) -> anyhow::Result<Vec<Package>> {
    Ok(serde_yaml::from_reader(&f)?)
}
```

## File: `huber/src/service/update.rs`
```rust
use std::fs::{read_dir, remove_dir_all, remove_file};
use std::sync::Arc;

use anyhow::anyhow;
use async_trait::async_trait;
use log::debug;
use semver::Version;
use simpledi_rs::di::{DIContainer, DIContainerExtTrait, DependencyInjectTrait};

use crate::cmd::PlatformStdLib;
use crate::model::config::{Config, ConfigPath};
use crate::service::package::PackageService;
use crate::service::release::ReleaseService;
use crate::service::{ItemOperationTrait, ServiceTrait};

pub trait UpdateTrait {
    fn reset(&self) -> anyhow::Result<()>;
}

#[async_trait]
pub trait UpdateAsyncTrait {
    async fn has_update(&self) -> anyhow::Result<(bool, String)>;
    async fn update(&self, prefer_stdlib: &PlatformStdLib) -> anyhow::Result<()>;
}

#[derive(Debug)]
pub struct HuberUpdateService {
    pub container: Option<Arc<DIContainer>>,
}

unsafe impl Send for HuberUpdateService {}

unsafe impl Sync for HuberUpdateService {}

impl ServiceTrait for HuberUpdateService {}

impl DependencyInjectTrait for HuberUpdateService {
    fn inject(&mut self, container: Arc<DIContainer>) {
        self.container = Some(container);
    }
}

impl Default for HuberUpdateService {
    fn default() -> Self {
        Self::new()
    }
}

impl HuberUpdateService {
    pub fn new() -> Self {
        Self { container: None }
    }
}

impl UpdateTrait for HuberUpdateService {
    fn reset(&self) -> anyhow::Result<()> {
        let config = self.container.get::<Config>().unwrap();

        let bin_dir_path = config.bin_dir()?;
        if bin_dir_path.exists() {
            for entry in read_dir(bin_dir_path)? {
                let path = entry?.path();

                if path.file_name().unwrap().to_str().unwrap() == "huber" {
                    debug!("Keeping huber executable");

                    let option = fs_extra::file::CopyOptions::new();
                    let temp_path = path.parent().unwrap().join("huber_temp");

                    debug!("Coping {:?} to {:?}", &path, &temp_path);
                    let _ = remove_file(&temp_path);
                    fs_extra::file::copy(&path, &temp_path, &option)?;

                    debug!("Moving {:?} to {:?}", &temp_path, &path);
                    let _ = remove_file(&path);
                    fs_extra::file::move_file(&temp_path, &path, &option)?;

                    continue;
                }

                let _ = remove_dir_all(path);
            }
        }

        let _ = remove_dir_all(config.installed_pkg_root_dir()?);
        let _ = remove_dir_all(config.temp_dir()?);
        let _ = remove_dir_all(config.repo_root_dir()?);
        let _ = remove_file(config.lock_file()?);
        let _ = remove_file(config.config_file()?);

        Ok(())
    }
}

#[async_trait]
impl UpdateAsyncTrait for HuberUpdateService {
    async fn has_update(&self) -> anyhow::Result<(bool, String)> {
        let pkg_service = self.container.get::<PackageService>().unwrap();
        let release_service = self.container.get::<ReleaseService>().unwrap();

        let current_version =
            Version::parse(env!("HUBER_VERSION").trim_start_matches("v")).unwrap();
        let pkg = pkg_service.get("huber")?;

        match release_service.get_latest(&pkg).await {
            Err(e) => Err(anyhow!("No update available: {:?}", e)),
            Ok(r) => {
                let result = Version::parse(r.version.trim_start_matches("v"))
                    .map(|ver| ver > current_version);

                match result {
                    Ok(update_needed) => Ok((update_needed, r.version)),
                    Err(e) => Err(anyhow!(
                        "A update available, but failed to continue: {:?}",
                        e
                    )),
                }
            }
        }
    }

    async fn update(&self, prefer_stdlib: &PlatformStdLib) -> anyhow::Result<()> {
        let pkg_service = self.container.get::<PackageService>().unwrap();
        let release_service = self.container.get::<ReleaseService>().unwrap();

        let mut pkg = pkg_service.get("huber")?;
        let release = release_service.get_latest(&pkg).await?;
        pkg.version = Some(release.version);

        release_service.update(&pkg, prefer_stdlib, true).await?;
        Ok(())
    }
}
```

## File: `huber/tests/completions.rs`
```rust
#[macro_use]
mod common;

#[test]
fn test_completions() {
    huber_cmd!(arg("completions").arg("zsh").assert().success());
}
```

## File: `huber/tests/config.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;
use tempfile::tempdir;

#[macro_use]
mod common;

use crate::common::reset_huber;

#[test]
fn test_config_not_found() {
    defer! {
        reset_huber();
    }

    huber_cmd!(arg("config").arg("show").assert().failure());
}

#[test]
#[sequential]
fn test_config_save_and_found() {
    defer! {
        reset_huber();
    }

    let github_token = "token";
    let github_base_uri = "uri";
    let github_key = "key";
    let log_level = "trace";
    let huber_dir = tempdir().unwrap();

    huber_cmd!(arg("config")
        .arg("save")
        .arg("--github-token")
        .arg(github_token)
        .arg("--github-key")
        .arg(github_key)
        .arg("--github-base-uri")
        .arg(github_base_uri)
        .arg("--log-level")
        .arg(log_level)
        .arg("--huber-dir")
        .arg(huber_dir.path())
        .arg("--output-format")
        .arg("yaml")
        .assert()
        .success());

    huber_cmd!(arg("config")
        .arg("show")
        .arg("--huber-dir")
        .arg(huber_dir.path())
        .assert()
        .success());
}
```

## File: `huber/tests/current.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, INVALID_PKG, INVALID_PKG_VERSION, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_current() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);

    let assert = huber_cmd!(arg("current").arg(PKG_VERSION_1).assert().success());
    assert_eq_last_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{} is now the current version"#, PKG_VERSION_1)
    );
}

#[test]
#[sequential]
fn test_current_fail() {
    defer! {
        reset_huber();
    }

    let assert = huber_cmd!(arg("current").arg(INVALID_PKG_VERSION).assert().failure());
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"Package not installed: "{}""#, INVALID_PKG)
    );
}
```

## File: `huber/tests/flush.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, PKG_VERSION_1, PKG_VERSION_2};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_flush_nothing() {
    defer! {
        reset_huber();
    }

    let assert = huber_cmd!(arg("flush").assert().success());
    assert_contain_line_regex!(assert.get_output().stderr, "Nothing to flush");
}

#[test]
#[sequential]
fn test_flush() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);
    install_pkgs(&[PKG_VERSION_2]);

    let assert = huber_cmd!(arg("flush").assert().success());
    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let pkg = tokens[0];
    let version = tokens[1];

    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(
            r#"{} \(version: {}, source: github\) removed"#,
            pkg, version
        )
    );
}
```

## File: `huber/tests/info.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, INVALID_PKG, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_info() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);
    let pkg = PKG_VERSION_1.splitn(2, '@').collect::<Vec<_>>()[0];

    huber_cmd!(arg("info").arg(pkg).assert().success());
}

#[test]
#[sequential]
fn test_info_fail() {
    defer! {
        reset_huber();
    }

    let assert = huber_cmd!(arg("info").arg(INVALID_PKG).assert().failure());
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"Package not found: "{}""#, INVALID_PKG)
    );
}
```

## File: `huber/tests/install.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, INVALID_PKG_VERSION, PKG_VERSION_1, PKG_VERSION_2};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_install() {
    defer! {
        reset_huber();
    }

    let pkg = PKG_VERSION_1.splitn(2, '@').collect::<Vec<_>>()[0];
    let assert = install_pkgs(&[pkg]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{}@latest/\S+ installed"#, pkg)
    );
}

#[test]
#[sequential]
fn test_install_version() {
    defer! {
        reset_huber();
    }

    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let pkg = tokens[0];
    let version = tokens[1];

    let assert = install_pkgs(&[&format!("{}@{}", pkg, version)]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r"{}@{} installed", pkg, version)
    );

    let tokens: Vec<_> = PKG_VERSION_2.splitn(2, '@').collect();
    let pkg = tokens[0];
    let version = tokens[1].trim_start_matches('v');

    let assert = install_pkgs(&[&format!("{}@{}", pkg, version)]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r"{}@{} installed", pkg, tokens[1])
    );
}

#[test]
#[sequential]
fn test_install_compression() {
    defer! {
        reset_huber();
    }

    let assert = install_pkgs(&["just"]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{}@latest/\S+ installed"#, "just")
    );
}

#[test]
#[sequential]
fn test_install_multiple_packages() {
    defer! {
        reset_huber();
    }

    let assert = install_pkgs(&["argocd", "kubectl"]);

    // Skip tests if encountering `Sending warning alert CloseNotify` error.
    // This error would happen when running tests in GitHub workflow CI.
    if String::from_utf8(assert.get_output().stderr.clone())
        .unwrap()
        .contains("Sending warning alert CloseNotify")
    {
        assert!(
            true,
            "Skipped tests, because encountering `Sending warning alert CloseNotify` error"
        );
        return;
    }

    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{}@latest/\S+ installed"#, "argocd")
    );
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{}@latest/\S+ installed"#, "kubectl")
    );
}

#[cfg(not(target_os = "windows"))]
#[test]
#[sequential]
fn test_install_no_artifact_templates() {
    defer! {
        reset_huber();
    }

    let assert = install_pkgs(&["bat"]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{}@latest/\S+ installed"#, "bat")
    );

    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(
            r#"Decompressing {}-\S+.tar.gz which has extension "tar.gz""#,
            "bat"
        )
    );
}

#[cfg(target_os = "linux")]
#[test]
#[sequential]
fn test_install_stdlib() {
    defer! {
        reset_huber();
    }

    let assert = install_pkgs(&["bat", "--prefer-stdlib", "gnu"]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(
            r#"Decompressing {}-\S+linux-gnu.tar.gz which has extension "tar.gz""#,
            "bat"
        )
    );

    assert_not_contain_line_regex!(
        assert.get_output().stderr,
        &format!(
            r#"Decompressing {}-\S+linux-musl.tar.gz which has extension "tar.gz""#,
            "bat"
        )
    );
}

#[cfg(target_os = "linux")]
#[test]
#[sequential]
fn test_install_unmanaged_package() {
    defer! {
        reset_huber();
    }

    let assert = install_pkgs(&["innobead/huber"]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"{}@latest/\S+ installed"#, format!("innobead/huber"))
    );
}

#[test]
#[sequential]
fn test_install_tag_only_package() {
    defer! {
        reset_huber();
    }

    let assert = install_pkgs(&["go@go1.24.0"]);
    assert_contain_line_regex!(assert.get_output().stderr, "go@go1.24.0 installed");
}

#[test]
#[sequential]
fn test_install_fail() {
    defer! {
        reset_huber();
    }

    let pkg = INVALID_PKG_VERSION.splitn(2, '@').collect::<Vec<_>>()[0];
    let assert = huber_cmd!(arg("install").arg(INVALID_PKG_VERSION).assert().success());

    assert_contain_line_regex!(assert.get_output().stderr, &format!(r#"{} not found"#, pkg));
}
```

## File: `huber/tests/load.rs`
```rust
use std::fs::remove_file;

use filepath::FilePath;
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, save_pkg_list, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_load() {
    defer! {
        reset_huber();
    }

    let file = tempfile::tempfile().unwrap();
    let path = file.path().unwrap().to_string_lossy().to_string();
    defer!(remove_file(&path).unwrap());
    drop(file);

    install_pkgs(&[PKG_VERSION_1]);
    save_pkg_list(&path);

    let assert = huber_cmd!(arg("load").arg("--file").arg(&path).assert().success());
    assert_contain_line_regex!(assert.get_output().stderr, r#"Installed packages: total 1"#);
}
```

## File: `huber/tests/lock.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, update_pkg, PKG_VERSION_1, PKG_VERSION_2};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_lock_update() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);
    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let pkg = tokens[0];
    let version = tokens[1].trim_start_matches('v');
    let pkg_version = format!("{}@={}", pkg, version);

    let assert = huber_cmd!(arg("lock").arg(pkg_version).assert().success());
    assert_contain_line_regex!(
        assert.get_output().stderr,
        r#"Packages locked successfully"#
    );

    huber_cmd!(arg("lock").arg("show").assert().success());

    let assert = update_pkg("k9s");
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(
            r#"Package {} is locked to version {}. Skipping updating to \S+"#,
            pkg,
            format!("={}", version)
        )
    );
}

#[test]
#[sequential]
fn test_lock_install() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);
    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let pkg = tokens[0];
    let version = tokens[1].trim_start_matches('v');
    let pkg_version = format!("{}@={}", pkg, version);

    let assert = huber_cmd!(arg("lock").arg(pkg_version).assert().success());
    assert_contain_line_regex!(
        assert.get_output().stderr,
        r#"Packages locked successfully"#
    );

    huber_cmd!(arg("lock").arg("show").assert().success());

    let assert = install_pkgs(&[PKG_VERSION_2]);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(
            r#"Package {} is locked to version {}. Skipping installing \S+"#,
            pkg,
            format!("={}", version)
        )
    );
}

#[test]
#[sequential]
fn test_lock_fail() {
    defer! {
        reset_huber();
    }

    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let version = tokens[1].trim_start_matches('v');
    let pkg = tokens[0];
    let pkg_version = format!("{}@{}", pkg, version);

    let assert = huber_cmd!(arg("lock").arg(pkg_version).assert().success());

    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"Skipped locking package {}@"#, pkg)
    );
}

#[test]
#[sequential]
fn test_lock_semver_req() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);

    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let pkg = tokens[0];
    let version = tokens[1].trim_start_matches('v');

    let assert = huber_cmd!(arg("lock")
        .arg(format!("{}@~{}", pkg, version))
        .assert()
        .success());

    assert_contain_line_regex!(
        assert.get_output().stderr,
        r#"Packages locked successfully"#
    );

    let assert = update_pkg(pkg);
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"Package {} updated to \S+ successfully"#, pkg)
    );
}
```

## File: `huber/tests/repo.rs`
```rust
use std::env;
use std::path::Path;

use scopeguard::defer;

use crate::common::reset_huber;

#[macro_use]
mod common;

#[test]
// #[sequential]
fn test_repo_add_show_remove() {
    defer! {
        reset_huber();
    }

    let huber_config = Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("docs")
        .join("src")
        .join("cmd")
        .join("repo")
        .join("huber.yaml");
    let repo = "external";

    let assert = huber_cmd!(arg("repo")
        .arg("add")
        .arg(repo)
        .arg("--file")
        .arg(huber_config.to_string_lossy().to_string())
        .assert()
        .success());
    assert_contain_line_regex!(assert.get_output().stderr, &format!("Repo {} added", repo));

    huber_cmd!(arg("repo").arg("show").assert().success());

    let assert = huber_cmd!(arg("repo").arg("remove").arg(repo).assert().success());
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!("Repo {} removed", repo)
    );
}
```

## File: `huber/tests/reset.rs`
```rust
use sequential_test::sequential;

use crate::common::reset_huber;

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_reset() {
    let assert = reset_huber();
    assert_contain_line_regex!(assert.get_output().stderr, "Huber reset");
}
```

## File: `huber/tests/save.rs`
```rust
use std::fs;

use filepath::FilePath;
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, save_pkg_list, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_save() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);

    let file = tempfile::tempfile().unwrap();
    let path = file.path().unwrap();
    defer! {
        let  _ = fs::remove_file(&path);
    };
    drop(file);

    let assert = save_pkg_list(path.to_string_lossy().to_string().as_ref());
    //FIXME: should check the file path
    assert_contain_line_regex!(assert.get_output().stderr, "Saved the package list to");
    assert!(fs::exists(&path).unwrap());
}
```

## File: `huber/tests/uninstall.rs`
```rust
use common::{install_pkgs, uninstall_pkg};
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{reset_huber, INVALID_PKG, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_uninstall() {
    defer! {
        reset_huber();
    }

    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, '@').collect();
    let pkg = tokens[0];
    install_pkgs(&[pkg]);

    let assert = uninstall_pkg(pkg);
    assert_contain_line_regex!(assert.get_output().stderr, &format!("Uninstalled {}", pkg));
}

#[test]
#[sequential]
fn test_uninstall_fail() {
    defer! {
        reset_huber();
    }

    let assert = huber_cmd!(arg("uninstall").arg(INVALID_PKG).assert().success());
    assert_contain_line_regex!(
        assert.get_output().stderr,
        &format!(r#"Package {} not found"#, INVALID_PKG)
    );
}
```

## File: `huber/tests/unlock.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, lock_pkg, reset_huber, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_unlock() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);

    let tokens = PKG_VERSION_1.splitn(2, '@').collect::<Vec<_>>();
    let pkg = tokens[0];
    let version = tokens[1].trim_start_matches('v');
    let pkg_version = format!("{}@{}", pkg, version);

    lock_pkg(&pkg_version);

    huber_cmd!(arg("unlock").arg(pkg).assert().success());
}
```

## File: `huber/tests/update.rs`
```rust
use scopeguard::defer;
use sequential_test::sequential;

use crate::common::{install_pkgs, reset_huber, PKG_VERSION_1};

#[macro_use]
mod common;

#[test]
#[sequential]
fn test_update() {
    defer! {
        reset_huber();
    }

    install_pkgs(&[PKG_VERSION_1]);
    let tokens: Vec<_> = PKG_VERSION_1.splitn(2, "@").collect();

    huber_cmd!(arg("update").arg(tokens[0]).assert().success());
}
```

## File: `huber/tests/common/mod.rs`
```rust
#![allow(dead_code)]
#![allow(unused_macros)]

use assert_cmd::assert::Assert;

pub const HUBER_EXEC: &str = env!("CARGO_BIN_EXE_huber");
pub const INVALID_PKG: &str = "pkg_notfound";
pub const INVALID_PKG_VERSION: &str = "pkg_notfound@1.2.3";
pub const PKG_VERSION_1: &str = "k9s@v0.32.5";
pub const PKG_VERSION_2: &str = "k9s@v0.32.7";

macro_rules! huber_cmd {
    ($($body:tt)*) => {
        assert_cmd::Command::new(crate::common::HUBER_EXEC)
            .env(
                "HUBER_PKG_ROOT_DIR",
                std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
                    .parent()
                    .unwrap()
                    .join("generated-v1"),
            )
            .arg("-l")
            .arg("debug")
            .$($body)*
    };
}

macro_rules! assert_contain_line_regex {
    ($value:expr, $expect:expr) => {
        let line = String::from_utf8($value.clone()).unwrap();
        println!("Value: \n{}", line);
        println!("Expected: \n{}", $expect);
        assert!(regex::Regex::new($expect).unwrap().is_match(&line))
    };
}

macro_rules! assert_not_contain_line_regex {
    ($value:expr, $expect:expr) => {
        let line = String::from_utf8($value.clone()).unwrap();
        println!("Value: \n{}", line);
        println!("Unexpected: \n{}", $expect);
        assert!(!regex::Regex::new($expect).unwrap().is_match(&line))
    };
}

macro_rules! assert_eq_last_line_regex {
    ($value:expr, $expect:expr) => {
        let line = String::from_utf8($value.clone())
            .unwrap()
            .lines()
            .last()
            .unwrap()
            .to_string();
        println!("Value: \n{}", line);
        println!("Expected: \n{}", $expect);
        assert!(regex::Regex::new($expect).unwrap().is_match(&line))
    };
}

macro_rules! assert_eq_last_line {
    ($value:expr, $expect:expr) => {
        let line = String::from_utf8($value.clone())
            .unwrap()
            .lines()
            .last()
            .unwrap()
            .to_string();
        println!("Value: \n{}", line);
        println!("Expected: \n{}", $expect);
        assert_eq!(line, $expect)
    };
}

pub fn install_pkgs(args: &[&str]) -> Assert {
    huber_cmd!(arg("install").args(args).assert().success())
}

pub fn uninstall_pkg(name: &str) -> Assert {
    huber_cmd!(arg("uninstall").arg(name).assert().success())
}

pub fn lock_pkg(name_version: &str) -> Assert {
    huber_cmd!(arg("lock").arg(name_version).assert().success())
}

pub fn update_pkg(name: &str) -> Assert {
    huber_cmd!(arg("update").arg(name).assert().success())
}

pub fn save_pkg_list(file: &str) -> Assert {
    huber_cmd!(arg("save").arg("--file").arg(file).assert().success())
}

pub fn reset_huber() -> Assert {
    huber_cmd!(arg("reset").assert().success())
}
```

## File: `huber-generator/Cargo.toml`
```
[package]
name = "huber-generator"
description = "Internal package used by Huber"
version.workspace = true
authors.workspace = true
edition.workspace = true
keywords.workspace = true
categories.workspace = true
homepage.workspace = true
repository.workspace = true
publish = false
license-file.workspace = true
build = "src/build.rs"

[build-dependencies]
anyhow.workspace = true
huber = { path = "../huber", version = "1.0.11" }
maplit.workspace = true
octocrab.workspace = true
serde.workspace = true
serde_yaml.workspace = true
tokio.workspace = true

[dependencies]
anyhow.workspace = true
huber = { path = "../huber", version = "1.0.11" }
maplit.workspace = true
octocrab.workspace = true
```

## File: `huber-generator/src/build.rs`
```rust
use std::env;
use std::path::Path;
use std::process::Command;

use ::huber::model::config::GENERATED_DIR_NAME;
use ::huber::model::package::{Package, PackageIndex, PackageSource};
use tokio::fs::{create_dir_all, remove_dir_all, remove_file, File};
use tokio::io::AsyncWriteExt;
use tokio::task::JoinHandle;

use crate::pkg::*;

mod pkg;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let pkg_dir = env!("CARGO_MANIFEST_DIR");

    let generated_dir = Path::new(&pkg_dir)
        .parent()
        .unwrap()
        .join(GENERATED_DIR_NAME)
        .join("packages");

    let force_generated: bool = env::var("FORCE")
        .unwrap_or_else(|_| {
            if generated_dir.exists() {
                "false"
            } else {
                "true"
            }
            .to_string()
        })
        .parse()?;

    if force_generated {
        println!("Forcefully regenerate packages in {:?}", generated_dir);
        remove_dir_all(&generated_dir).await?;
    } else {
        println!("Only generate the impacted packages in {:?}", generated_dir);
    }

    create_dir_all(&generated_dir).await?;

    // generate release manifests, index file
    let index_file = Path::new(&generated_dir)
        .parent()
        .unwrap()
        .join("index.yaml");
    let _ = remove_file(&index_file).await;
    let mut index_file = File::create(index_file).await?;

    index_file
        .write_all("# THIS IS GENERATED BY huber-generator.\n".as_bytes())
        .await?;

    let mut pkg_indexes: Vec<PackageIndex> = vec![];
    let mut handles: Vec<JoinHandle<anyhow::Result<()>>> = vec![];

    for mut pkg in releases().into_iter() {
        pkg_indexes.push(PackageIndex {
            name: pkg.name.clone(),
            owner: pkg.source.owner(),
            source: pkg.source.to_string(),
        });

        let pkg_file = Path::new(&generated_dir)
            .join(pkg.name.clone())
            .with_extension("yaml");

        let handle = tokio::spawn(async move {
            if !force_generated {
                let pkg_rs_file = Path::new(&pkg_dir)
                    .join("src")
                    .join("pkg")
                    .join(format!("{}.rs", pkg.name));

                // This is the best effort to check for any local changes,
                // except that the change has been pushed to the remote origin.
                let pkg_rs_file_changed = [
                    "diff --exit-code --quiet",
                    "diff --exit-code --quiet --cached",
                ]
                .iter()
                .any(|&args| {
                    let mut args: Vec<_> = args.split(' ').collect();
                    args.append(&mut vec!["--", pkg_rs_file.to_str().unwrap()]);

                    Command::new("git")
                        .args(&args)
                        .output()
                        .map(|output| output.status.code().unwrap() != 0)
                        .unwrap()
                });

                if !pkg_rs_file_changed {
                    return Ok(());
                }

                println!("{:?} changed", pkg_rs_file)
            }

            update_description(&mut pkg).await?;

            let str = format!(
                "# THIS IS GENERATED BY huber-generator.\n{}",
                serde_yaml::to_string(&pkg)?
            );

            File::create(pkg_file)
                .await?
                .write_all(str.as_bytes())
                .await?;

            Ok(())
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.await??;
    }

    pkg_indexes.sort_by(|x, y| x.name.partial_cmp(&y.name).unwrap());
    index_file
        .write_all(serde_yaml::to_string(&pkg_indexes).unwrap().as_bytes())
        .await?;

    Ok(())
}

fn releases() -> Vec<Package> {
    vec![
        jiq::release(),
        jless::release(),
        onefetch::release(),
        gh::release(),
        dasel::release(),
        bat::release(),
        terraform::release(),
        opentofu::release(),
        packer::release(),
        syncthing::release(),
        powershell::release(),
        mkcert::release(),
        huber::release(),
        ali::release(),
        gping::release(),
        gitui::release(),
        ripgrep::release(),
        starship::release(),
        tokei::release(),
        exa::release(),
        fd::release(),
        procs::release(),
        k6::release(),
        fortio::release(),
        jwt_cli::release(),
        direnv::release(),
        tracee::release(),
        vegeta::release(),
        yq::release(),
        stern::release(),
        img::release(),
        dive::release(),
        hyperfine::release(),
        hetty::release(),
        czkawka::release(),
        cloak::release(),
        jq::release(),
        termshark::release(),
        volta::release(),
        just::release(),
        croc::release(),
        terrascan::release(),
        nerdctl::release(),
        zoxide::release(),
        dust::release(),
        pueue::release(),
        coreutils::release(),
        hugo::release(),
        typos::release(),
        zellij::release(),
        xh::release(),
        loc::release(),
        choose::release(),
        delta::release(),
        dog::release(),
        dua_cli::release(),
        skim::release(),
        hexyl::release(),
        lsd::release(),
        fnm::release(),
        frum::release(),
        nat::release(),
        sad::release(),
        sd::release(),
        navi::release(),
        tealdeer::release(),
        bottom::release(),
        grex::release(),
        codeql::release(),
        viddy::release(),
        cosign::release(),
        saml2aws::release(),
        grpcurl::release(),
        buf::release(),
        httptap::release(),
        asdf::release(),
        rclone::release(),
        gitleaks::release(),
        goose::release(),
        pulumi::release(),
        chisel::release(),
        go_http_tunnel::release(),
        shadowsocks::release(),
        norouter::release(),
        wstunnel::release(),
        doctl::release(),
        zola::release(),
        nushell::release(),
        dolt::release(),
        okteto::release(),
        skaffold::release(),
        kpt::release(),
        oras::release(),
        tilt::release(),
        ko::release(),
        protoc::release(),
        copilot_cli::release(),
        compose::release(),
        velero::release(),
        helm::release(),
        helmfile::release(),
        kubefire::release(),
        kubectl::release(),
        kustomize::release(),
        k3s::release(),
        k3sup::release(),
        k3d::release(),
        rke2::release(),
        istio::release(),
        fleet::release(),
        kube_bench::release(),
        trivy::release(),
        octant::release(),
        pack::release(),
        opa::release(),
        conftest::release(),
        kind::release(),
        krew::release(),
        minikube::release(),
        sonobuoy::release(),
        consul::release(),
        ctlptl::release(),
        arkade::release(),
        fission::release(),
        k9s::release(),
        k0s::release(),
        kuttl::release(),
        flux2::release(),
        argocd::release(),
        kompose::release(),
        eksctl::release(),
        linkerd2_edge::release(),
        linkerd2_stable::release(),
        camel_k::release(),
        kubevirt::release(),
        kubestr::release(),
        kube_linter::release(),
        natscli::release(),
        traefik::release(),
        containerd::release(),
        firecracker::release(),
        podman::release(),
        wasmtime::release(),
        wasmer::release(),
        wabt::release(),
        deno::release(),
        bun::release(),
        typescript::release(),
        node::release(),
        kotlin::release(),
        gradle::release(),
        go::release(),
        solidity::release(),
        axelard::release(),
        foundry::release(),
        ollama::release(),
        localai::release(),
        cni_plugins::release(),
        regclient::release(),
    ]
}

async fn update_description(pkg: &mut Package) -> anyhow::Result<()> {
    println!("Updating the description of package: {}", pkg);

    let octocrab = octocrab::OctocrabBuilder::default()
        .personal_token(env::var("GITHUB_TOKEN")?)
        .build()?;

    let PackageSource::Github { owner, repo } = &pkg.source;
    let repo = octocrab.repos(owner, repo).get().await?;
    pkg.description = repo.description;

    Ok(())
}
```

## File: `huber-generator/src/lib.rs`
```rust
mod pkg;
```

## File: `huber-generator/src/pkg/ali.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ali".to_string(),
        source: PackageSource::Github {
            owner: "nakabonne".to_string(),
            repo: "ali".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/argocd.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "argocd".to_string(),
        source: PackageSource::Github {
            owner: "argoproj".to_string(),
            repo: "argo-cd".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/arkade.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "arkade".to_string(),
        source: PackageSource::Github {
            owner: "alexellis".to_string(),
            repo: "arkade".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["arkade".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["arkade-arm64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec!["arkade-armhf".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["arkade-darwin".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec!["arkade-darwin-arm64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["arkade.exe".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/asdf.rs`
```rust
use huber::model::package::{default_targets_no_arm_windows, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "asdf".to_string(),
        source: PackageSource::Github {
            owner: "asdf-vm".to_string(),
            repo: "asdf".to_string(),
        },
        targets: default_targets_no_arm_windows(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/axelard.rs`
```rust
use huber::model::package::default_targets_no_arm_windows;
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "axelard".to_string(),
        source: PackageSource::Github {
            owner: "axelarnetwork".to_string(),
            repo: "axelar-core".to_string(),
        },
        targets: default_targets_no_arm_windows(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/bat.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "bat".to_string(),
        source: PackageSource::Github {
            owner: "sharkdp".to_string(),
            repo: "bat".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/bottom.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "bottom".to_string(),
        source: PackageSource::Github {
            owner: "ClementTsang".to_string(),
            repo: "bottom".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/buf.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "buf".to_string(),
        source: PackageSource::Github {
            owner: "bufbuild".to_string(),
            repo: "buf".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/bun.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "bun".to_string(),
        source: PackageSource::Github {
            owner: "oven-sh".to_string(),
            repo: "bun".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/camel_k.rs`
```rust
use huber::model::package::default_targets_no_arm;
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "camel-k".to_string(),
        source: PackageSource::Github {
            owner: "apache".to_string(),
            repo: "camel-k".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/chisel.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "chisel".to_string(),
        source: PackageSource::Github {
            owner: "jpillora".to_string(),
            repo: "chisel".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/choose.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "choose".to_string(),
        source: PackageSource::Github {
            owner: "theryangeary".to_string(),
            repo: "choose".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/cloak.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "cloak".to_string(),
        source: PackageSource::Github {
            owner: "cbeuw".to_string(),
            repo: "Cloak".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/cni_plugins.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "cni-plugins".to_string(),
        source: PackageSource::Github {
            owner: "containernetworking".to_string(),
            repo: "plugins".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::LinuxArm(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/codeql.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "codeql".to_string(),
        source: PackageSource::Github {
            owner: "github".to_string(),
            repo: "codeql-cli-binaries".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["codeql-linux64.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["codeql-osx64.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["codeql-win64.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/compose.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "compose".to_string(),
        source: PackageSource::Github {
            owner: "docker".to_string(),
            repo: "compose".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/conftest.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "conftest".to_string(),
        source: PackageSource::Github {
            owner: "open-policy-agent".to_string(),
            repo: "conftest".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/consul.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "consul".to_string(),
        source: PackageSource::Github {
            owner: "hashicorp".to_string(),
            repo: "consul".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/consul/{version}/consul_{version}_linux_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/consul/{version}/consul_{version}_linux_arm64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/consul/{version}/consul_{version}_darwin_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/consul/{version}/consul_{version}_windows_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/containerd.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "containerd".to_string(),
        source: PackageSource::Github {
            owner: "containerd".to_string(),
            repo: "containerd".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/copilot_cli.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "copilot-cli".to_string(),
        source: PackageSource::Github {
            owner: "aws".to_string(),
            repo: "copilot-cli".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/coreutils.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "coreutils".to_string(),
        source: PackageSource::Github {
            owner: "uutils".to_string(),
            repo: "coreutils".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/cosign.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "cosign".to_string(),
        source: PackageSource::Github {
            owner: "sigstore".to_string(),
            repo: "cosign".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/croc.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "croc".to_string(),
        source: PackageSource::Github {
            owner: "schollz".to_string(),
            repo: "croc".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/ctlptl.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ctlptl".to_string(),
        source: PackageSource::Github {
            owner: "tilt-dev".to_string(),
            repo: "ctlptl".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/czkawka.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "czkawka".to_string(),
        source: PackageSource::Github {
            owner: "qarmin".to_string(),
            repo: "czkawka".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "linux_czkawka_cli".to_string(),
                    "linux_czkawka_gui".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "mac_czkawka_cli".to_string(),
                    "mac_czkawka_gui".to_string(),
                    "mac_krokiet_gui".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "windows_czkawka_cli.exe".to_string(),
                    "windows_krokiet_gui_linversion.exe".to_string(),
                    "windows_krokiet_gui_linversion_console.exe".to_string(),
                    "windows_krokiet_gui_winversion.exe".to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/dasel.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "dasel".to_string(),
        source: PackageSource::Github {
            owner: "TomWright".to_string(),
            repo: "dasel".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/delta.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "delta".to_string(),
        source: PackageSource::Github {
            owner: "dandavison".to_string(),
            repo: "delta".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/deno.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "deno".to_string(),
        source: PackageSource::Github {
            owner: "denoland".to_string(),
            repo: "deno".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/direnv.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "direnv".to_string(),
        source: PackageSource::Github {
            owner: "direnv".to_string(),
            repo: "direnv".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/dive.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "dive".to_string(),
        source: PackageSource::Github {
            owner: "wagoodman".to_string(),
            repo: "dive".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/doctl.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "doctl".to_string(),
        source: PackageSource::Github {
            owner: "digitalocean".to_string(),
            repo: "doctl".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/dog.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "dog".to_string(),
        source: PackageSource::Github {
            owner: "ogham".to_string(),
            repo: "dog".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/dolt.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "dolt".to_string(),
        source: PackageSource::Github {
            owner: "dolthub".to_string(),
            repo: "dolt".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/dua_cli.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "dua-cli".to_string(),
        source: PackageSource::Github {
            owner: "Byron".to_string(),
            repo: "dua-cli".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/dust.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "dust".to_string(),
        source: PackageSource::Github {
            owner: "bootandy".to_string(),
            repo: "dust".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/eksctl.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "eksctl".to_string(),
        source: PackageSource::Github {
            owner: "eksctl-io".to_string(),
            repo: "eksctl".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/exa.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "exa".to_string(),
        source: PackageSource::Github {
            owner: "ogham".to_string(),
            repo: "exa".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/fd.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "fd".to_string(),
        source: PackageSource::Github {
            owner: "sharkdp".to_string(),
            repo: "fd".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/firecracker.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "firecracker".to_string(),
        source: PackageSource::Github {
            owner: "firecracker-microvm".to_string(),
            repo: "firecracker".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["firecracker-v{version}-x86_64.tgz".to_string()],
                executable_mappings: None,
                tag_version_regex_template: None,
                scan_dirs: Some(vec!["release-v{version}-{arch}".to_string()]),
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["firecracker-v{version}-aarch64.tgz".to_string()],
                executable_mappings: None,
                tag_version_regex_template: None,
                scan_dirs: Some(vec!["release-v{version}-{arch}".to_string()]),
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/fission.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "fission".to_string(),
        source: PackageSource::Github {
            owner: "fission".to_string(),
            repo: "fission".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/fleet.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "fleet".to_string(),
        source: PackageSource::Github {
            owner: "rancher".to_string(),
            repo: "fleet".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/flux2.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "flux2".to_string(),
        source: PackageSource::Github {
            owner: "fluxcd".to_string(),
            repo: "flux2".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/fnm.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "fnm".to_string(),
        source: PackageSource::Github {
            owner: "Schniz".to_string(),
            repo: "fnm".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["fnm-linux.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["fnm-arm64.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["fnm-macos.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["fnm-windows.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/fortio.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "fortio".to_string(),
        source: PackageSource::Github {
            owner: "fortio".to_string(),
            repo: "fortio".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["fortio_win_{version}.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/foundry.rs`
```rust
use huber::model::package::{default_targets_no_arm_windows, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "foundry".to_string(),
        source: PackageSource::Github {
            owner: "foundry-rs".to_string(),
            repo: "foundry".to_string(),
        },
        targets: default_targets_no_arm_windows(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/frum.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "frum".to_string(),
        source: PackageSource::Github {
            owner: "TaKO8Ki".to_string(),
            repo: "frum".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/gh.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "gh".to_string(),
        source: PackageSource::Github {
            owner: "cli".to_string(),
            repo: "cli".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/gitleaks.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "gitleaks".to_string(),
        source: PackageSource::Github {
            owner: "gitleaks".to_string(),
            repo: "gitleaks".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/gitui.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "gitui".to_string(),
        source: PackageSource::Github {
            owner: "extrawurst".to_string(),
            repo: "gitui".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["gitui-mac.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["gitui-win.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/go.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "go".to_string(),
        source: PackageSource::Github {
            owner: "golang".to_string(),
            repo: "go".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://golang.org/dl/{version}.linux-amd64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://golang.org/dl/{version}.linux-arm64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://golang.org/dl/{version}.darwin-amd64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec![
                    "https://golang.org/dl/go{version}.darwin-arm64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://golang.org/dl/go{version}.windows-amd64.zip".to_string()
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/go_http_tunnel.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "go-http-tunnel".to_string(),
        source: PackageSource::Github {
            owner: "mmatczuk".to_string(),
            repo: "go-http-tunnel".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/goose.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "goose".to_string(),
        source: PackageSource::Github {
            owner: "pressly".to_string(),
            repo: "goose".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/gping.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "gping".to_string(),
        source: PackageSource::Github {
            owner: "orf".to_string(),
            repo: "gping".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::LinuxArm(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["gping-Windows-msvc-x86_64.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/gradle.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "gradle".to_string(),
        source: PackageSource::Github {
            owner: "gradle".to_string(),
            repo: "gradle".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://services.gradle.org/distributions/gradle-{version}-bin.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://services.gradle.org/distributions/gradle-{version}-bin.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://services.gradle.org/distributions/gradle-{version}-bin.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/grex.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "grex".to_string(),
        source: PackageSource::Github {
            owner: "pemistahl".to_string(),
            repo: "grex".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/grpcurl.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "grpcurl".to_string(),
        source: PackageSource::Github {
            owner: "fullstorydev".to_string(),
            repo: "grpcurl".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/helm.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "helm".to_string(),
        source: PackageSource::Github {
            owner: "helm".to_string(),
            repo: "helm".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://get.helm.sh/helm-v{version}-linux-amd64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://get.helm.sh/helm-v{version}-linux-arm64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec![
                    "https://get.helm.sh/helm-v{version}-linux-arm.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://get.helm.sh/helm-v{version}-darwin-amd64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec![
                    "https://get.helm.sh/helm-v{version}-darwin-arm64.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://get.helm.sh/helm-v{version}-windows-amd64.zip".to_string()
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/helmfile.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "helmfile".to_string(),
        source: PackageSource::Github {
            owner: "helmfile".to_string(),
            repo: "helmfile".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/hetty.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "hetty".to_string(),
        source: PackageSource::Github {
            owner: "dstotijn".to_string(),
            repo: "hetty".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/hexyl.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "hexyl".to_string(),
        source: PackageSource::Github {
            owner: "sharkdp".to_string(),
            repo: "hexyl".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/httptap.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "httptap".to_string(),
        source: PackageSource::Github {
            owner: "monasticacademy".to_string(),
            repo: "httptap".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/huber.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "huber".to_string(),
        source: PackageSource::Github {
            owner: "innobead".to_string(),
            repo: "huber".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/hugo.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "hugo".to_string(),
        source: PackageSource::Github {
            owner: "gohugoio".to_string(),
            repo: "hugo".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "hugo_{version}_darwin-universal.tar.gz".to_string(),
                    "hugo_extended_{version}_darwin-universal.tar.gz".to_string(),
                    "hugo_extended_withdeploy_{version}_darwin-universal.tar.gz".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/hyperfine.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "hyperfine".to_string(),
        source: PackageSource::Github {
            owner: "sharkdp".to_string(),
            repo: "hyperfine".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/img.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "img".to_string(),
        source: PackageSource::Github {
            owner: "genuinetools".to_string(),
            repo: "img".to_string(),
        },
        targets: vec![PackageTargetType::LinuxAmd64(PackageManagement {
            artifact_templates: vec!["img-linux-amd64".to_string()],
            ..Default::default()
        })],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/istio.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "istio".to_string(),
        source: PackageSource::Github {
            owner: "istio".to_string(),
            repo: "istio".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "istio-{version}-linux-amd64.tar.gz".to_string(),
                    "istioctl-{version}-linux-amd64.tar.gz".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "istio-{version}-linux-arm64.tar.gz".to_string(),
                    "istioctl-{version}-linux-arm64.tar.gz".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "istio-{version}-osx.tar.gz".to_string(),
                    "istioctl-{version}-osx.tar.gz".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "istio-{version}-win.zip".to_string(),
                    "istioctl-{version}-win.zip".to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/jiq.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "jiq".to_string(),
        source: PackageSource::Github {
            owner: "fiatjaf".to_string(),
            repo: "jiq".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["jiq_linux_amd64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["jiq_darwin_amd64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["jiq_windows_amd64.exe".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/jless.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "jless".to_string(),
        source: PackageSource::Github {
            owner: "PaulJuliusMartinez".to_string(),
            repo: "jless".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/jq.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "jq".to_string(),
        source: PackageSource::Github {
            owner: "jqlang".to_string(),
            repo: "jq".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/just.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "just".to_string(),
        source: PackageSource::Github {
            owner: "casey".to_string(),
            repo: "just".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/jwt_cli.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "jwt-cli".to_string(),
        source: PackageSource::Github {
            owner: "mike-engel".to_string(),
            repo: "jwt-cli".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["jwt-linux.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["jwt-linux-arm64.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["jwt-macOS.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["jwt-windows.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/k0s.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "k0s".to_string(),
        source: PackageSource::Github {
            owner: "k0sproject".to_string(),
            repo: "k0s".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["k0s-v{version}+k0s.0-amd64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec!["k0s-v{version}+k0s.0-arm".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["k0s-v{version}+k0s.0-arm64".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/k3d.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "k3d".to_string(),
        source: PackageSource::Github {
            owner: "k3d-io".to_string(),
            repo: "k3d".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/k3s.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "k3s".to_string(),
        source: PackageSource::Github {
            owner: "k3s-io".to_string(),
            repo: "k3s".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["k3s".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["k3s-arm64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec!["k3s-armhf".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/k3sup.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "k3sup".to_string(),
        source: PackageSource::Github {
            owner: "alexellis".to_string(),
            repo: "k3sup".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["k3sup".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["k3sup-arm64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec!["k3sup-armhf".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["k3sup-darwin".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec!["k3sup-darwin-arm64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["k3sup.exe".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/k6.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "k6".to_string(),
        source: PackageSource::Github {
            owner: "grafana".to_string(),
            repo: "k6".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/k9s.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "k9s".to_string(),
        source: PackageSource::Github {
            owner: "derailed".to_string(),
            repo: "k9s".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kind.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kind".to_string(),
        source: PackageSource::Github {
            owner: "kubernetes-sigs".to_string(),
            repo: "kind".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/ko.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ko".to_string(),
        source: PackageSource::Github {
            owner: "ko-build".to_string(),
            repo: "ko".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kompose.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kompose".to_string(),
        source: PackageSource::Github {
            owner: "kubernetes".to_string(),
            repo: "kompose".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kotlin.rs`
```rust
use huber::model::package::{default_targets_no_arm64_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kotlin".to_string(),
        source: PackageSource::Github {
            owner: "JetBrains".to_string(),
            repo: "kotlin".to_string(),
        },
        targets: default_targets_no_arm64_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kpt.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kpt".to_string(),
        source: PackageSource::Github {
            owner: "GoogleContainerTools".to_string(),
            repo: "kpt".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/krew.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "krew".to_string(),
        source: PackageSource::Github {
            owner: "kubernetes-sigs".to_string(),
            repo: "krew".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kube_bench.rs`
```rust
use huber::model::package::{default_targets_no_windows, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kube-bench".to_string(),
        source: PackageSource::Github {
            owner: "aquasecurity".to_string(),
            repo: "kube-bench".to_string(),
        },
        targets: default_targets_no_windows(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kube_linter.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kube-linter".to_string(),
        source: PackageSource::Github {
            owner: "stackrox".to_string(),
            repo: "kube-linter".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["kube-linter-linux.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["kube-linter-darwin.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kubectl.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kubectl".to_string(),
        source: PackageSource::Github {
            owner: "kubernetes".to_string(),
            repo: "kubernetes".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://dl.k8s.io/release/v{version}/bin/linux/amd64/kubectl".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://dl.k8s.io/release/v{version}/bin/linux/arm64/kubectl".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://dl.k8s.io/release/v{version}/bin/linux/arm/kubectl".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://dl.k8s.io/release/v{version}/bin/darwin/amd64/kubectl".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec![
                    "https://dl.k8s.io/release/v{version}/bin/darwin/arm64/kubectl".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://dl.k8s.io/release/v{version}/bin/windows/amd64/kubectl.exe"
                        .to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kubefire.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kubefire".to_string(),
        source: PackageSource::Github {
            owner: "innobead".to_string(),
            repo: "kubefire".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kubestr.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kubestr".to_string(),
        source: PackageSource::Github {
            owner: "kastenhq".to_string(),
            repo: "kubestr".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kubevirt.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kubevirt".to_string(),
        source: PackageSource::Github {
            owner: "kubevirt".to_string(),
            repo: "kubevirt".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kustomize.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kustomize".to_string(),
        source: PackageSource::Github {
            owner: "kubernetes-sigs".to_string(),
            repo: "kustomize".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/kuttl.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "kuttl".to_string(),
        source: PackageSource::Github {
            owner: "kudobuilder".to_string(),
            repo: "kuttl".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec![
                    "kubectl-kuttl_{version}_linux_armv6".to_string(),
                    "kuttl_{version}_linux_armv6.tar.gz
"
                    .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/linkerd2_edge.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};
use maplit::hashmap;

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "linkerd2-edge".to_string(),
        source: PackageSource::Github {
            owner: "linkerd".to_string(),
            repo: "linkerd2".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-edge-{version}-linux-amd64".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-edge-{version}-linux-amd64".to_string() => "linkerd2-edge".to_string()
                }),
                tag_version_regex_template: Some(r"^edge-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-edge-{version}-linux-arm64".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-edge-{version}-linux-arm64".to_string() => "linkerd2-edge".to_string()
                }),
                tag_version_regex_template: Some(r"^edge-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-edge-{version}-darwin".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-edge-{version}-darwin".to_string() => "linkerd2-edge".to_string()
                }),
                tag_version_regex_template: Some(r"^edge-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-edge-{version}-windows.exe".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-edge-{version}-windows.exe".to_string() => "linkerd2-edge.exe".to_string()
                }),
                tag_version_regex_template: Some(r"^edge-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/linkerd2_stable.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};
use maplit::hashmap;

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "linkerd2-stable".to_string(),
        source: PackageSource::Github {
            owner: "linkerd".to_string(),
            repo: "linkerd2".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-stable-{version}-linux-amd64".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-stable-{version}-linux-amd64".to_string() => "linkerd2-stable".to_string()
                }),
                tag_version_regex_template: Some(r"^stable-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-stable-{version}-linux-arm64".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-stable-{version}-linux-arm64".to_string() => "linkerd2-stable".to_string()
                }),
                tag_version_regex_template: Some(r"^stable-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-stable-{version}-darwin".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-stable-{version}-darwin".to_string() => "linkerd2-stable".to_string()
                }),
                tag_version_regex_template: Some(r"^stable-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["linkerd2-cli-stable-{version}-windows.exe".to_string()],
                executable_mappings: Some(hashmap! {
                    "linkerd2-cli-stable-{version}-windows.exe".to_string() => "linkerd2-stable.exe".to_string()
                }),
                tag_version_regex_template: Some(r"^stable-(\d+.\d+.\d+)$".to_string()),
                scan_dirs: None,
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/loc.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "loc".to_string(),
        source: PackageSource::Github {
            owner: "cgag".to_string(),
            repo: "loc".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/localai.rs`
```rust
use huber::model::package::{Package, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "local-ai".to_string(),
        source: PackageSource::Github {
            owner: "mudler".to_string(),
            repo: "LocalAI".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/lsd.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "lsd".to_string(),
        source: PackageSource::Github {
            owner: "lsd-rs".to_string(),
            repo: "lsd".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/minikube.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "minikube".to_string(),
        source: PackageSource::Github {
            owner: "kubernetes".to_string(),
            repo: "minikube".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/mkcert.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "mkcert".to_string(),
        source: PackageSource::Github {
            owner: "FiloSottile".to_string(),
            repo: "mkcert".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/mod.rs`
```rust
pub mod ali;
pub mod argocd;
pub mod arkade;
pub mod axelard;
pub mod bat;
pub mod bottom;
pub mod buf;
pub mod bun;
pub mod camel_k;
pub mod chisel;
pub mod choose;
pub mod cloak;
pub mod codeql;
pub mod conftest;
pub mod consul;
pub mod containerd;
pub mod copilot_cli;
pub mod coreutils;
pub mod cosign;
pub mod croc;
pub mod ctlptl;
pub mod czkawka;
pub mod dasel;
pub mod delta;
pub mod deno;
pub mod direnv;
pub mod dive;
pub mod doctl;
pub mod dog;
pub mod dolt;
pub mod dua_cli;
pub mod dust;
pub mod eksctl;
pub mod exa;
pub mod fd;
pub mod firecracker;
pub mod fission;
pub mod fleet;
pub mod flux2;
pub mod fnm;
pub mod fortio;
pub mod frum;
pub mod gh;
pub mod gitui;
pub mod go;
pub mod go_http_tunnel;
pub mod gping;
pub mod gradle;
pub mod grex;
pub mod grpcurl;
pub mod helm;
pub mod helmfile;
pub mod hetty;
pub mod hexyl;
pub mod huber;
pub mod hugo;
pub mod hyperfine;
pub mod img;
pub mod istio;
pub mod jiq;
pub mod jless;
pub mod jq;
pub mod just;
pub mod jwt_cli;
pub mod k0s;
pub mod k3d;
pub mod k3s;
pub mod k3sup;
pub mod k6;
pub mod k9s;
pub mod kind;
pub mod ko;
pub mod kompose;
pub mod kotlin;
pub mod kpt;
pub mod krew;
pub mod kube_bench;
pub mod kube_linter;
pub mod kubectl;
pub mod kubefire;
pub mod kubestr;
pub mod kubevirt;
pub mod kustomize;
pub mod kuttl;
pub mod linkerd2_edge;
pub mod linkerd2_stable;
pub mod loc;
pub mod localai;
pub mod lsd;
pub mod minikube;
pub mod mkcert;
pub mod nat;
pub mod natscli;
pub mod navi;
pub mod nerdctl;
pub mod node;
pub mod norouter;
pub mod nushell;
pub mod octant;
pub mod okteto;
pub mod ollama;
pub mod onefetch;
pub mod opa;
pub mod opentofu;
pub mod oras;
pub mod pack;
pub mod packer;
pub mod podman;
pub mod powershell;
pub mod procs;
pub mod protoc;
pub mod pueue;
pub mod pulumi;
pub mod ripgrep;
pub mod rke2;
pub mod sad;
pub mod saml2aws;
pub mod sd;
pub mod shadowsocks;
pub mod skaffold;
pub mod skim;
pub mod solidity;
pub mod sonobuoy;
pub mod starship;
pub mod stern;

pub mod syncthing;
pub mod tealdeer;

pub mod asdf;
pub mod cni_plugins;
pub mod compose;
pub mod foundry;
pub mod gitleaks;
pub mod goose;
pub mod httptap;
pub mod rclone;
pub mod termshark;
pub mod terraform;
pub mod terrascan;
pub mod tilt;
pub mod tokei;
pub mod tracee;
pub mod traefik;
pub mod trivy;
pub mod typescript;
pub mod typos;
pub mod vegeta;
pub mod velero;
pub mod viddy;
pub mod volta;
pub mod wabt;
pub mod wasmer;
pub mod wasmtime;
pub mod wstunnel;
pub mod xh;
pub mod yq;
pub mod zellij;
pub mod zola;
pub mod zoxide;
pub mod regclient;
```

## File: `huber-generator/src/pkg/nat.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "nat".to_string(),
        source: PackageSource::Github {
            owner: "willdoescode".to_string(),
            repo: "nat".to_string(),
        },

        targets: vec![PackageTargetType::MacOSAmd64(PackageManagement {
            artifact_templates: vec!["natls_osx_binary".to_string()],
            ..Default::default()
        })],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/natscli.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "natscli".to_string(),
        source: PackageSource::Github {
            owner: "nats-io".to_string(),
            repo: "natscli".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/navi.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "navi".to_string(),
        source: PackageSource::Github {
            owner: "denisidoro".to_string(),
            repo: "navi".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "navi-v{version}-aarch64-unknown-linux-gnu.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec![
                    "navi-v{version}-armv7-unknown-linux-musleabihf.tar.gz".to_string()
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
            PackageTargetType::WindowsAmd64(Default::default()),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/nerdctl.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "nerdctl".to_string(),
        source: PackageSource::Github {
            owner: "containerd".to_string(),
            repo: "nerdctl".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["nerdctl-{version}-linux-amd64.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["nerdctl-{version}-linux-arm64.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm(PackageManagement {
                artifact_templates: vec!["nerdctl-{version}-linux-arm-v7.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/node.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "node".to_string(),
        source: PackageSource::Github {
            owner: "nodejs".to_string(),
            repo: "node".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://nodejs.org/dist/v{version}/node-v{version}-linux-x64.tar.xz"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://nodejs.org/dist/v{version}/node-v{version}-linux-arm64.tar.xz"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://nodejs.org/dist/v{version}/node-v{version}-darwin-x64.tar.gz"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec![
                    "https://nodejs.org/dist/v{version}/node-v{version}-darwin-arm64.tar.gz"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://nodejs.org/dist/v{version}/node-v{version}-win-x64.zip".to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/norouter.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "norouter".to_string(),
        source: PackageSource::Github {
            owner: "norouter".to_string(),
            repo: "norouter".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["norouter-Linux-x86_64.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["norouter-Linux-aarch64.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["norouter-Darwin-x86_64.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["norouter-Windows-x64.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/nushell.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "nushell".to_string(),
        source: PackageSource::Github {
            owner: "nushell".to_string(),
            repo: "nushell".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "nu-{version}-x86_64-unknown-linux-gnu.tar.gz".to_string(),
                    "nu-{version}-x86_64-unknown-linux-musl.tar.gz".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "nu-{version}-aarch64-unknown-linux-gnu.tar.gz".to_string(),
                    "nu-{version}-aarch64-unknown-linux-musl.tar.gz".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["nu-{version}-x86_64-apple-darwin.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec!["nu-{version}-aarch64-apple-darwin.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["nu-{version}-x86_64-pc-windows-msvc.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/octant.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "octant".to_string(),
        source: PackageSource::Github {
            owner: "vmware-tanzu".to_string(),
            repo: "octant".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["octant_{version}_Linux-64bit.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["octant_{version}_Linux-arm64.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["octant_{version}_macOS-64bit.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["octant_{version}_Windows-64bit.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/okteto.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "okteto".to_string(),
        source: PackageSource::Github {
            owner: "okteto".to_string(),
            repo: "okteto".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::LinuxArm64(Default::default()),
            PackageTargetType::MacOSAmd64(Default::default()),
            PackageTargetType::MacOSArm64(Default::default()),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["okteto.exe".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/ollama.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ollama".to_string(),
        source: PackageSource::Github {
            owner: "ollama".to_string(),
            repo: "ollama".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/onefetch.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "onefetch".to_string(),
        source: PackageSource::Github {
            owner: "o2sh".to_string(),
            repo: "onefetch".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["onefetch-linux.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["onefetch-mac.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["onefetch-win.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/opa.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "opa".to_string(),
        source: PackageSource::Github {
            owner: "open-policy-agent".to_string(),
            repo: "opa".to_string(),
        },

        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["opa_linux_amd64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["opa_darwin_amd64".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["opa_windows_amd64.exe".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/opentofu.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "opentofu".to_string(),
        source: PackageSource::Github {
            owner: "opentofu".to_string(),
            repo: "opentofu".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/oras.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "oras".to_string(),
        source: PackageSource::Github {
            owner: "oras-project".to_string(),
            repo: "oras".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/pack.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "pack".to_string(),
        source: PackageSource::Github {
            owner: "buildpacks".to_string(),
            repo: "pack".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["pack-v{version}-linux.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxAmd64(Default::default()),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["pack-v{version}-macos.tgz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(Default::default()),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["pack-v{version}-windows.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/packer.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "packer".to_string(),
        source: PackageSource::Github {
            owner: "hashicorp".to_string(),
            repo: "packer".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/packer/{version}/packer_{version}_linux_arm64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/packer/{version}/packer_{version}_darwin_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/packer/{version}/packer_{version}_windows_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/podman.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "podman".to_string(),
        source: PackageSource::Github {
            owner: "containers".to_string(),
            repo: "podman".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/powershell.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "powershell".to_string(),
        source: PackageSource::Github {
            owner: "PowerShell".to_string(),
            repo: "PowerShell".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/procs.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "procs".to_string(),
        source: PackageSource::Github {
            owner: "dalance".to_string(),
            repo: "procs".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/protoc.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "protoc".to_string(),
        source: PackageSource::Github {
            owner: "protocolbuffers".to_string(),
            repo: "protobuf".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["protoc-{version}-linux-x86_64.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["protoc-{version}-linux-aarch_64.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["protoc-{version}-osx-x86_64.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec!["protoc-{version}-osx-universal_binary.zip".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["protoc-{version}-win64.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/pueue.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "pueue".to_string(),
        source: PackageSource::Github {
            owner: "Nukesor".to_string(),
            repo: "pueue".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "pueue-linux-x86_64".to_string(),
                    "pueued-linux-x86_64".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "pueue-linux-aarch64".to_string(),
                    "pueued-linux-aarch64".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "pueue-macos-x86_64".to_string(),
                    "pueued-macos-x86_64".to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "pueue-windows-x86_64.exe".to_string(),
                    "pueued-windows-x86_64.exe".to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/pulumi.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "pulumi".to_string(),
        source: PackageSource::Github {
            owner: "pulumi".to_string(),
            repo: "pulumi".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://get.pulumi.com/releases/sdk/pulumi-v{version}-linux-x64.tar.gz"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://get.pulumi.com/releases/sdk/pulumi-v{version}-darwin-x64.tar.gz"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://get.pulumi.com/releases/sdk/pulumi-v{version}-windows-x64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/rclone.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "rclone".to_string(),
        source: PackageSource::Github {
            owner: "rclone".to_string(),
            repo: "rclone".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/regclient.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "regclient".to_string(),
        source: PackageSource::Github {
            owner: "regclient".to_string(),
            repo: "regclient".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/ripgrep.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "ripgrep".to_string(),
        source: PackageSource::Github {
            owner: "BurntSushi".to_string(),
            repo: "ripgrep".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/rke2.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "rke2".to_string(),
        source: PackageSource::Github {
            owner: "rancher".to_string(),
            repo: "rke2".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["rke2.linux-amd64.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["rke2.linux-arm64.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["rke2.windows-amd64.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/sad.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "sad".to_string(),
        source: PackageSource::Github {
            owner: "ms-jpq".to_string(),
            repo: "sad".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/saml2aws.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "saml2aws".to_string(),
        source: PackageSource::Github {
            owner: "Versent".to_string(),
            repo: "saml2aws".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/sd.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "sd".to_string(),
        source: PackageSource::Github {
            owner: "chmln".to_string(),
            repo: "sd".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/shadowsocks.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "shadowsocks".to_string(),
        source: PackageSource::Github {
            owner: "shadowsocks".to_string(),
            repo: "shadowsocks-rust".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/skaffold.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "skaffold".to_string(),
        source: PackageSource::Github {
            owner: "GoogleContainerTools".to_string(),
            repo: "skaffold".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/skim.rs`
```rust
use huber::model::package::{default_targets_no_windows, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "skim".to_string(),
        source: PackageSource::Github {
            owner: "skim-rs".to_string(),
            repo: "skim".to_string(),
        },
        targets: default_targets_no_windows(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/solidity.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "solidity".to_string(),
        source: PackageSource::Github {
            owner: "ethereum".to_string(),
            repo: "solidity".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["solc-static-linux".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["solc-macos".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["solc-windows.exe".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/sonobuoy.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "sonobuoy".to_string(),
        source: PackageSource::Github {
            owner: "vmware-tanzu".to_string(),
            repo: "sonobuoy".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/starship.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "starship".to_string(),
        source: PackageSource::Github {
            owner: "starship".to_string(),
            repo: "starship".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/stern.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "stern".to_string(),
        source: PackageSource::Github {
            owner: "stern".to_string(),
            repo: "stern".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/syncthing.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "syncthing".to_string(),
        source: PackageSource::Github {
            owner: "syncthing".to_string(),
            repo: "syncthing".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/tealdeer.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "tealdeer".to_string(),
        source: PackageSource::Github {
            owner: "tealdeer-rs".to_string(),
            repo: "tealdeer".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/termshark.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "termshark".to_string(),
        source: PackageSource::Github {
            owner: "gcla".to_string(),
            repo: "termshark".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/terraform.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "terraform".to_string(),
        source: PackageSource::Github {
            owner: "hashicorp".to_string(),
            repo: "terraform".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/terraform/{version}/terraform_{version}_linux_arm64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/terraform/{version}/terraform_{version}_darwin_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/terraform/{version}/terraform_{version}_darwin_arm64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec![
                    "https://releases.hashicorp.com/terraform/{version}/terraform_{version}_windows_amd64.zip"
                        .to_string(),
                ],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/terrascan.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "terrascan".to_string(),
        source: PackageSource::Github {
            owner: "tenable".to_string(),
            repo: "terrascan".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/tilt.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "tilt".to_string(),
        source: PackageSource::Github {
            owner: "tilt-dev".to_string(),
            repo: "tilt".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/tokei.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "tokei".to_string(),
        source: PackageSource::Github {
            owner: "XAMPPRocky".to_string(),
            repo: "tokei".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/tracee.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "tracee".to_string(),
        source: PackageSource::Github {
            owner: "aquasecurity".to_string(),
            repo: "tracee".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["tracee-x86_64.v{version}.tar.gz".to_string()],
                scan_dirs: Some(vec!["dist".to_string()]),
                ..Default::default()
            }),
            PackageTargetType::LinuxArm64(PackageManagement {
                artifact_templates: vec!["tracee-aarch64.v{version}.tar.gz".to_string()],
                scan_dirs: Some(vec!["dist".to_string()]),
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/traefik.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "traefik".to_string(),
        source: PackageSource::Github {
            owner: "traefik".to_string(),
            repo: "traefik".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/trivy.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "trivy".to_string(),
        source: PackageSource::Github {
            owner: "aquasecurity".to_string(),
            repo: "trivy".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/typescript.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "typescript".to_string(),
        source: PackageSource::Github {
            owner: "microsoft".to_string(),
            repo: "TypeScript".to_string(),
        },
        targets: vec![PackageTargetType::LinuxAmd64(PackageManagement {
            artifact_templates: vec!["typescript-{version}.tgz".to_string()],
            ..Default::default()
        })],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/typos.rs`
```rust
use huber::model::package::{default_targets_no_arm64_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "typos".to_string(),
        source: PackageSource::Github {
            owner: "crate-ci".to_string(),
            repo: "typos".to_string(),
        },
        targets: default_targets_no_arm64_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/vegeta.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "vegeta".to_string(),
        source: PackageSource::Github {
            owner: "tsenart".to_string(),
            repo: "vegeta".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/velero.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "velero".to_string(),
        source: PackageSource::Github {
            owner: "vmware-tanzu".to_string(),
            repo: "velero".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/viddy.rs`
```rust
use huber::model::package::{default_targets_no_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "viddy".to_string(),
        source: PackageSource::Github {
            owner: "sachaos".to_string(),
            repo: "viddy".to_string(),
        },
        targets: default_targets_no_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/volta.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "volta".to_string(),
        source: PackageSource::Github {
            owner: "volta-cli".to_string(),
            repo: "volta".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["volta-{version}-linux.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["volta-{version}-macos.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["volta-{version}-windows.zip".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/wabt.rs`
```rust
use huber::model::package::{Package, PackageManagement, PackageSource, PackageTargetType};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "wabt".to_string(),
        source: PackageSource::Github {
            owner: "WebAssembly".to_string(),
            repo: "wabt".to_string(),
        },
        targets: vec![
            PackageTargetType::LinuxAmd64(PackageManagement {
                artifact_templates: vec!["wabt-{version}-ubuntu.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSAmd64(PackageManagement {
                artifact_templates: vec!["wabt-{version}-macos-12.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::MacOSArm64(PackageManagement {
                artifact_templates: vec!["wabt-{version}-macos-14.tar.gz".to_string()],
                ..Default::default()
            }),
            PackageTargetType::WindowsAmd64(PackageManagement {
                artifact_templates: vec!["wabt-{version}-windows.tar.gz".to_string()],
                ..Default::default()
            }),
        ],
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/wasmer.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "wasmer".to_string(),
        source: PackageSource::Github {
            owner: "wasmerio".to_string(),
            repo: "wasmer".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/wasmtime.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "wasmtime".to_string(),
        source: PackageSource::Github {
            owner: "bytecodealliance".to_string(),
            repo: "wasmtime".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/wstunnel.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "wstunnel".to_string(),
        source: PackageSource::Github {
            owner: "erebe".to_string(),
            repo: "wstunnel".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/xh.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "xh".to_string(),
        source: PackageSource::Github {
            owner: "ducaale".to_string(),
            repo: "xh".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/yq.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "yq".to_string(),
        source: PackageSource::Github {
            owner: "mikefarah".to_string(),
            repo: "yq".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/zellij.rs`
```rust
use huber::model::package::{default_targets_no_arm_windows, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "zellij".to_string(),
        source: PackageSource::Github {
            owner: "zellij-org".to_string(),
            repo: "zellij".to_string(),
        },
        targets: default_targets_no_arm_windows(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/zola.rs`
```rust
use huber::model::package::{default_targets_no_arm64_arm, Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "zola".to_string(),
        source: PackageSource::Github {
            owner: "getzola".to_string(),
            repo: "zola".to_string(),
        },
        targets: default_targets_no_arm64_arm(),
        ..Default::default()
    }
}
```

## File: `huber-generator/src/pkg/zoxide.rs`
```rust
use huber::model::package::{Package, PackageSource};

#[allow(dead_code)]
pub fn release() -> Package {
    Package {
        name: "zoxide".to_string(),
        source: PackageSource::Github {
            owner: "ajeetdsouza".to_string(),
            repo: "zoxide".to_string(),
        },
        ..Default::default()
    }
}
```

## File: `huber-procmacro/Cargo.toml`
```
[package]
name = "huber-procmacro"
description = "Internal package used by Huber"
version.workspace = true
authors.workspace = true
edition.workspace = true
keywords.workspace = true
categories.workspace = true
homepage.workspace = true
repository.workspace = true
publish = true
license-file.workspace = true

[lib]
proc-macro = true

[dependencies]
quote.workspace = true
syn.workspace = true
```

## File: `huber-procmacro/src/lib.rs`
```rust
extern crate proc_macro;

use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, Expr};

#[proc_macro]
pub fn process_lock(input: TokenStream) -> TokenStream {
    let lock_file_pathbuf_expr = parse_macro_input!(input as Expr);

    let result = quote! {
        use crate::model::config::Config;
        use std::fs::File;
        use fs2::FileExt;
        use log::debug;
        use anyhow::anyhow;

        let lock_path = #lock_file_pathbuf_expr;
        let f = if !lock_path.exists() {
            File::create(&lock_path)
        } else {
            File::open(&lock_path)
        }.unwrap();

        let r = f.try_lock_exclusive();
        match r {
            Ok(_) => {
                debug!("{}: {:?}", "Locking the operation", lock_path);
            },

            Err(e) => {
                debug!("{:?}: {:?}", lock_path, e);
                return Err(anyhow!("huber is already running by another process for the exclusion operation. Please try after the operation finished. {:?}", e))
            }
        }
    };

    result.into()
}
```

