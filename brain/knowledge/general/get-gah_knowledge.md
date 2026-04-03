---
id: get-gah-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:26.937795
---

# KNOWLEDGE EXTRACT: get-gah
> **Extracted on:** 2026-03-30 17:37:58
> **Source:** get-gah

---

## File: `gah.md`
```markdown
# 📦 get-gah/gah [🔖 PENDING/APPROVE]
🔗 https://github.com/get-gah/gah


## Meta
- **Stars:** ⭐ 282 | **Forks:** 🍴 8
- **Language:** Shell | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
gah is an GitHub Releases app installer, that does not require sudo

## README (trích đầu)
```
![gah! logo](./_static/logo-256x128.png)


![GitHub top language](https://img.shields.io/github/languages/top/get-gah/gah?color=d8d440&style=flat-square)
![GitHub file size in bytes](https://img.shields.io/github/size/get-gah/gah/gah?color=db805a&style=flat-square)
[![GitHub Release](https://img.shields.io/github/v/release/get-gah/gah?color=db5b92&style=flat-square)](https://github.com/get-gah/gah/releases)
[![GitHub License](https://img.shields.io/github/license/get-gah/gah?color=b95fda&style=flat-square)](https://github.com/get-gah/gah/blob/master/LICENSE)
[![All Contributors](https://img.shields.io/github/all-contributors/get-gah/gah?color=b1abea&style=flat-square)](#contributors)


`gah` is an GitHub Releases app installer, that **DOES NOT REQUIRE SUDO**! It is a simple bash script that downloads the latest release of an app from GitHub and installs it in `~/.local/bin`. It is designed to be used with apps that are distributed as a single binary file.

## Motivation

Nowadays more and more command-line tools and applications are distributed via GitHub Releases. The installation process looks always the same: you go to the release page, expand assets, find the right file for your platform (which may be very frustrating, especially when there are 200+ assets and very often developers use different naming conventions - e.g. `myapp-linux-amd64`, `myapp_linux_x64`, `myapp-unknown-linux-gnu-x86_64`, etc.), download it, unpack it, move it to `~/.local/bin`, execute `chmod +x` on it and don't forget to clean up afterwards. For me, it was a hassle. Each time I needed to go thru the process again I was doing "gah! not again!". So I thought, why not automate this process? In fact, I love automation and RegExp. And so `gah` was born.

## Features

- 🏷 Downloads the latest or given release of an app from GitHub
- 🎯 Automatically selects matching binary for the current platform

  - Supported OS: Linux and MacOS
  - Supported architectures: x64 and ARM64

- 🎳 Supports multiple matching apps in a single GitHub Release
- 📤 Supports archived (`.zip`, `.tar.gz`, `.tar.bz2`, `.tar.xz`) and single binary releases
- 🗃 Has own base of predefined aliases for GitHub repositories (PRs are welcome!)
- 🔐 Verifies downloaded files using provided by `openssl` against [asset's digest value](https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#get-a-release-asset)

## Requirements

- `bash` (version 3 or higher)
- `perl` (by default installed on most unix systems, required for bash < 4)
- `jq`
- `curl` or `wget`
- `tar` (by default installed on most unix systems)
- `unzip` (by default installed on most unix systems)
- `openssl` (by default installed on most unix systems)

## Installation

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/get-gah/gah/refs/heads/master/tools/install.sh)"
```
or
```bash
bash -c "$(wget -qO- https://raw.githubusercontent.com/get-gah/gah/refs/heads/master/tools/install.sh)"
```

## Usage

![gah demo](./_static/dem
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

