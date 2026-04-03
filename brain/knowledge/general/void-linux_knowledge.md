---
id: void-linux-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:41.947896
---

# KNOWLEDGE EXTRACT: void-linux
> **Extracted on:** 2026-03-30 17:58:59
> **Source:** void-linux

---

## File: `void-packages.md`
```markdown
# 📦 void-linux/void-packages [🔖 PENDING/APPROVE]
🔗 https://github.com/void-linux/void-packages
🌐 https://voidlinux.org

## Meta
- **Stars:** ⭐ 3096 | **Forks:** 🍴 2562
- **Language:** Shell | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The Void source packages collection

## README (trích đầu)
```
## The XBPS source packages collection

This repository contains the XBPS source packages collection to build binary packages
for the Void Linux distribution.

The included `xbps-src` script will fetch and compile the sources, and install its
files into a `fake destdir` to generate XBPS binary packages that can be installed
or queried through the `xbps-install(1)` and `xbps-query(1)` utilities, respectively.

See [Contributing](./CONTRIBUTING.md) for a general overview of how to contribute and the
[Manual](./Manual.md) for details of how to create source packages.

### Table of Contents

- [Requirements](#requirements)
- [Quick start](#quick-start)
- [chroot methods](#chroot-methods)
- [Install the bootstrap packages](#install-bootstrap)
- [Configuration](#configuration)
- [Directory hierarchy](#directory-hierarchy)
- [Building packages](#building-packages)
- [Package build options](#build-options)
- [Sharing and signing your local repositories](#sharing-and-signing)
- [Rebuilding and overwriting existing local packages](#rebuilding)
- [Enabling distcc for distributed compilation](#distcc)
- [Distfiles mirrors](#distfiles-mirrors)
- [Cross compiling packages for a target architecture](#cross-compiling)
- [Using xbps-src in a foreign Linux distribution](#foreign)
- [Remaking the masterdir](#remaking-masterdir)
- [Keeping your masterdir uptodate](#updating-masterdir)
- [Building 32bit packages on x86_64](#building-32bit)
- [Building packages natively for the musl C library](#building-for-musl)
- [Building void base-system from scratch](#building-base-system)

### Requirements

- GNU bash
- xbps >= 0.56
- git(1) - unless configured to not, see etc/defaults.conf
- common POSIX utilities included by default in almost all UNIX systems
- curl(1) - required by `xbps-src update-check`

For bootstrapping from source additionally:
- flock(1) - util-linux
- bsdtar or GNU tar (in that order of preference)
- install(1) - GNU coreutils
- objcopy(1), objdump(1), strip(1): binutils

`xbps-src` requires [a utility to chroot](#chroot-methods) and bind mount existing directories
into a `masterdir` that is used as its main `chroot` directory. `xbps-src` supports
multiple utilities to accomplish this task.

> NOTE: `xbps-src` does not allow building as root anymore. Use one of the chroot
methods.

<a name="quick-start"></a>
### Quick start

Clone the `void-packages` git repository:

```
$ git clone https://github.com/void-linux/void-packages.git
$ cd void-packages
```

Bootstrapping from binary packages will be done automatically when first building
a package, but it can be done manually with:

```
$ ./xbps-src binary-bootstrap
```

Build a package by specifying the `pkg` target and the package name:

```
$ ./xbps-src pkg <package_name>
```

Use `./xbps-src -h` to list all available targets and options.

To build packages marked as 'restricted', modify `etc/conf`:

```
$ echo XBPS_ALLOW_RESTRICTED=yes >> etc/conf
```

Once built, the package will be available in `host
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

