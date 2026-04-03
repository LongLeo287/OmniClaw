---
id: dscharrer-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.970337
---

# KNOWLEDGE EXTRACT: dscharrer
> **Extracted on:** 2026-03-30 17:36:10
> **Source:** dscharrer

---

## File: `innoextract.md`
```markdown
# 📦 dscharrer/innoextract [🔖 PENDING/APPROVE]
🔗 https://github.com/dscharrer/innoextract
🌐 https://constexpr.org/innoextract/

## Meta
- **Stars:** ⭐ 1273 | **Forks:** 🍴 168
- **Language:** C++ | **License:** NOASSERTION
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A tool to unpack installers created by Inno Setup

## README (trích đầu)
```

# innoextract - A tool to unpack installers created by Inno Setup

[Inno Setup](https://jrsoftware.org/isinfo.php) is a tool to create installers for Microsoft Windows applications. innoextract allows to extract such installers under non-Windows systems without running the actual installer using wine. innoextract currently supports installers created by Inno Setup 1.2.10 to 6.3.3.

In addition to standard Inno Setup installers, innoextract also supports some modified Inno Setup variants including Martijn Laan's My Inno Setup Extensions 1.3.10 to 3.0.6.1 as well as GOG.com's Inno Setup-based game installers. innoextract is able to unpack Wadjet Eye Games installers (to play with AGS), Arx Fatalis patches (for use with Arx Libertatis) as well as various other Inno Setup executables.

innoextract is available under the ZLIB license - see the LICENSE file.

See the website for [Linux packages](https://constexpr.org/innoextract/#packages).

## Contact

[Website](https://constexpr.org/innoextract/)

Author: [Daniel Scharrer](https://constexpr.org/)

## Dependencies

* **[Boost](https://www.boost.org/) 1.37** or newer
* **liblzma** from [xz-utils](https://tukaani.org/xz/) *(optional)*
* **iconv** (*optional*, either as part of the system libc, as is the case with [glibc](https://www.gnu.org/software/libc/) and [uClibc](https://uclibc.org/), or as a separate [libiconv](https://www.gnu.org/software/libiconv/))

For Boost you will need the headers as well as the `iostreams`, `filesystem`, `date_time`, `system` and `program_options` libraries. Older Boost version may work but are not actively supported. The boost `iostreams` library needs to be build with zlib and bzip2 support.

While innoextract can be built without liblzma by manually setting `-DUSE_LZMA=OFF`, it is highly recommended and you won't be able to extract most installers created by newer Inno Setup versions without it.

To build innoextract you will also need **[CMake](https://cmake.org/) 2.8** and a working C++ compiler, as well as the development headers for liblzma and boost.

See the Website for [operating system-specific instructions](https://constexpr.org/innoextract/install).

## Compile and install

To compile innoextract, run:

    $ mkdir -p build && cd build
    $ cmake ..
    $ make

To install the binaries system-wide, run as root:

    # make install

The default build settings are tuned for users - if you plan to make changes to Arx Libertatis you should append the `-DDEVELOPER=1` option to the `cmake` command to enable debug output and fast incremental builds.

### Build options:

| Option                    | Default   | Description |
|:------------------------- |:---------:|:----------- |
| `BUILD_DECRYPTION`        | `ON`      | Build decryption support.
| `USE_LZMA`                | `ON`      | Use `liblzma`.
| `WITH_CONV`               | *not set* | The charset conversion library to use. Valid values are `iconv`, `win32` and `builtin`¹. If not set, a library appropriate 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

