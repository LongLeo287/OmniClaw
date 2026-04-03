---
id: orf-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:18.278912
---

# KNOWLEDGE EXTRACT: orf
> **Extracted on:** 2026-03-30 17:50:34
> **Source:** orf

---

## File: `gping.md`
```markdown
# 📦 orf/gping [🔖 PENDING/APPROVE]
🔗 https://github.com/orf/gping


## Meta
- **Stars:** ⭐ 12399 | **Forks:** 🍴 362
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Ping, but with a graph

## README (trích đầu)
```
# gping 🚀

[![Crates.io](https://img.shields.io/crates/v/gping.svg)](https://crates.io/crates/gping)
[![Actions Status](https://github.com/orf/gping/workflows/CI/badge.svg)](https://github.com/orf/gping/actions)

Ping, but with a graph.

![](./images/readme-example.gif)

Comes with the following super-powers:
* Graph the ping time for multiple hosts
* Graph the _execution time_ for commands via the `--cmd` flag
* Custom colours
* Windows, Mac and Linux support

Table of Contents
=================

   * [Install :cd:](#install-cd)
   * [Usage :saxophone:](#usage-saxophone)

<a href="https://repology.org/project/gping/versions">
    <img src="https://repology.org/badge/vertical-allrepos/gping.svg" alt="Packaging status" align="right">
</a>

# Install :cd:

* macOS
  * [Homebrew](https://formulae.brew.sh/formula/gping#default): `brew install gping`
  * [MacPorts](https://ports.macports.org/port/gping/): `sudo port install gping`
* Linux (Homebrew): `brew install gping`
* CentOS (and other distributions with an old glibc): Download the MUSL build from the latest release
* Windows/ARM:
  * Scoop: `scoop install gping`
  * Chocolatey: `choco install gping`
  * Download the latest release from [the github releases page](https://github.com/orf/gping/releases)
* Fedora ([COPR](https://copr.fedorainfracloud.org/coprs/atim/gping/)): `sudo dnf copr enable atim/gping -y && sudo dnf install gping`
* Cargo (**This requires `rustc` version 1.67.0 or greater**): `cargo install gping`
* Arch Linux: `pacman -S gping`
* Alpine linux: `apk add gping`
* Ubuntu >23.10/Debian >13: `apt install gping`
* Ubuntu/Debian ([Azlux's repo](https://packages.azlux.fr/)):
  ```bash
  echo 'deb [signed-by=/usr/share/keyrings/azlux.gpg] https://packages.azlux.fr/debian/ bookworm main' | sudo tee /etc/apt/sources.list.d/azlux.list
  sudo apt install gpg
  curl -s https://azlux.fr/repo.gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/azlux.gpg > /dev/null
  sudo apt update
  sudo apt install gping
  ```
* Gentoo ([dm9pZCAq overlay](https://github.com/gentoo-mirror/dm9pZCAq)):
  ```sh
  sudo eselect repository enable dm9pZCAq
  sudo emerge --sync dm9pZCAq
  sudo emerge net-misc/gping::dm9pZCAq
  ```
* FreeBSD:
  * [pkg](https://www.freshports.org/net-mgmt/gping/): `pkg install gping`
  * [ports](https://cgit.freebsd.org/ports/tree/net-mgmt/gping) `cd /usr/ports/net-mgmt/gping; make install clean`
* Docker:
  ```sh
  # Check all options
  docker run --rm -ti --network host ghcr.io/orf/gping:gping-v1.15.1 --help
  # Ping google.com
  docker run --rm -ti --network host ghcr.io/orf/gping:gping-v1.15.1 google.com
  ```
* Flox:
  ```sh
  # Inside of a Flox environment
  flox install gping
  ```
* [gah](https://github.com/marverix/gah):
  ```sh
  gah install gping
  ```

# Usage :saxophone:

Just run `gping [host]`. `host` can be a command like `curl google.com` if the `--cmd` flag is used. You can also use
shorthands like `aws:eu-west-1` or `aws:ca-central-1` to ping specific cloud reg
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

