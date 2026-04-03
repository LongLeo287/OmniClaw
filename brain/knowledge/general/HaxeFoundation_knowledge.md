---
id: haxefoundation-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:50.855887
---

# KNOWLEDGE EXTRACT: HaxeFoundation
> **Extracted on:** 2026-03-30 17:38:04
> **Source:** HaxeFoundation

---

## File: `neko.md`
```markdown
# 📦 HaxeFoundation/neko [🔖 PENDING/APPROVE]
🔗 https://github.com/HaxeFoundation/neko
🌐 https://nekovm.org

## Meta
- **Stars:** ⭐ 578 | **Forks:** 🍴 112
- **Language:** C | **License:** NOASSERTION
- **Last updated:** 2026-03-19
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The Neko Virtual Machine

## README (trích đầu)
```
![NekoVM](https://cloud.githubusercontent.com/assets/576184/14234981/10528a0e-f9f1-11e5-8922-894569b2feea.png)

[![CI](https://github.com/HaxeFoundation/neko/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/HaxeFoundation/neko/actions/workflows/main.yml)

# Deprecated as of 2021-09-09

**Neko is not actively maintained anymore.**

We keep it compatible with existing Haxe standard library and Haxe language features. But don't expect any new features in Neko itself and don't expect implementation of any new Haxe standard library API.

# Neko Virtual Machine

See https://nekovm.org/

## Snapshot Builds

Compiled binaries can be found in the "artifacts" section in the summary of each [Github Actions build](https://github.com/HaxeFoundation/neko/actions?query=branch%3Amaster+is%3Asuccess).

For macOS, Neko snapshot of the latest master branch can be built using [homebrew](https://brew.sh/) in a single command: `brew install neko --HEAD`. It will install required dependencies, build, and install Neko to the system. The binaries can be found at `brew --prefix neko`. Use `brew reinstall neko --HEAD` to upgrade in the future.

## Build instruction

Neko can be built using CMake (version 3.x is recommended) and one of the C compilers listed as follows:

 * Windows: Visual Studio 2010 / 2013 / 2015 / 2017
 * Mac: XCode (with its "Command line tools")
 * Linux: gcc (can be obtained by installing the "build-essential" Debian/Ubuntu package)

Neko needs to link with various third-party libraries, which are summarized as follows:

| library / tool                          | OS          | Debian/Ubuntu package                                     |
|-----------------------------------------|-------------|-----------------------------------------------------------|
| Boehm GC                                | all         | libgc-dev                                                 |
| OpenSSL                                 | all         | libssl-dev                                                |
| pcre2                                   | all         | libpcre2-dev                                              |
| zlib                                    | all         | zlib1g-dev                                                |
| Apache 2.2 / 2.4, with apr and apr-util | all         | apache2-dev                                               |
| MariaDB / MySQL (Connector/C)           | all         | libmariadb-client-lgpl-dev-compat (or libmysqlclient-dev) |
| SQLite                                  | all         | libsqlite3-dev                                            |
| mbed TLS                                | all         | libmbedtls-dev                                            |
| GTK+3                                   | Linux       | libgtk-3-dev                                              |

On Windows, CMake will automatically download and build the libraries in the build folder during the build process. However, you need to
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

