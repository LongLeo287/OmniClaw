---
id: schollz-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.876718
---

# KNOWLEDGE EXTRACT: schollz
> **Extracted on:** 2026-03-30 17:53:04
> **Source:** schollz

---

## File: `croc.md`
```markdown
# 📦 schollz/croc [🔖 PENDING/APPROVE]
🔗 https://github.com/schollz/croc
🌐 https://schollz.com/software/croc6

## Meta
- **Stars:** ⭐ 34481 | **Forks:** 🍴 1355
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Easily and securely send things from one computer to another :crocodile: :package:

## README (trích đầu)
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/6550035/46709024-9b23ad00-cbf6-11e8-9fb2-ca8b20b7dbec.jpg" width="408px" border="0" alt="croc">
  <br>
  <a href="https://github.com/schollz/croc/releases/latest"><img src="https://img.shields.io/github/v/release/schollz/croc" alt="Version"></a>
  <a href="https://github.com/schollz/croc/actions/workflows/ci.yml"><img src="https://github.com/schollz/croc/actions/workflows/ci.yml/badge.svg" alt="Build Status"></a>
  <a href="https://github.com/sponsors/schollz"><img alt="GitHub Sponsors" src="https://img.shields.io/github/sponsors/schollz"></a>
</p>
<p align="center">
  <strong>This project’s future depends on community support. <a href="https://github.com/sponsors/schollz">Become a sponsor today</a>.</strong>
</p>

## About

`croc` is a tool that allows any two computers to simply and securely transfer files and folders. AFAIK, *croc* is the only CLI file-transfer tool that does **all** of the following:

- Allows **any two computers** to transfer data (using a relay)
- Provides **end-to-end encryption** (using PAKE)
- Enables easy **cross-platform** transfers (Windows, Linux, Mac)
- Allows **multiple file** transfers
- Allows **resuming transfers** that are interrupted
- No need for local server or port-forwarding
- **IPv6-first** with IPv4 fallback
- Can **use a proxy**, like Tor

For more information about `croc`, see [my blog post](https://schollz.com/tinker/croc6/) or read a [recent interview I did](https://console.substack.com/p/console-91).

![Example](src/install/customization.gif)

## Install

You can download [the latest release for your system](https://github.com/schollz/croc/releases/latest), or install a release from the command-line:

```bash
curl https://getcroc.schollz.com | bash
```

### On macOS

Using [Homebrew](https://brew.sh/):

```bash
brew install croc
```

Using [MacPorts](https://www.macports.org/):

```bash
sudo port selfupdate
sudo port install croc
```

### On Windows

You can install the latest release with [Scoop](https://scoop.sh/), [Chocolatey](https://chocolatey.org/), or [Winget](https://learn.microsoft.com/windows/package-manager/):

```bash
scoop install croc
```

```bash
choco install croc
```

```bash
winget install schollz.croc
```

### Using nix-env

You can install the latest release with [Nix](https://nixos.org/):

```bash
nix-env -i croc
```

### On NixOS

You can add this to your [configuration.nix](https://nixos.org/manual/nixos/stable/#ch-configuration):

```nix
environment.systemPackages = [
  pkgs.croc
];
```

### On Alpine Linux

First, install dependencies:

```bash
apk add bash coreutils
wget -qO- https://getcroc.schollz.com | bash
```

### On Arch Linux

Install with `pacman`:

```bash
pacman -S croc
```

### On Fedora

Install with `dnf`:

```bash
dnf install croc
```

### On Gentoo

Install with `portage`:

```bash
emerge net-misc/croc
```

### On Termux

Install with `pkg`:

```bash
pkg install croc
```

### On FreeBSD

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

