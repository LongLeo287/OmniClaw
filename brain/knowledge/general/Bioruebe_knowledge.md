---
id: bioruebe-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:57.847717
---

# KNOWLEDGE EXTRACT: Bioruebe
> **Extracted on:** 2026-03-30 17:30:49
> **Source:** Bioruebe

---

## File: `Bio.cs.md`
```markdown
# 📦 Bioruebe/Bio.cs [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/Bio.cs


## Meta
- **Stars:** ⭐ 4 | **Forks:** 🍴 0
- **Language:** C# | **License:** MIT
- **Last updated:** 2025-06-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Bioruebe's standard library, C# edition

## README (trích đầu)
```
# BioLib (*Bio.cs*)

A helper library used in most of my C# projects.

The main purpose of this library is speeding up the development of command line applications by providing functions for common tasks, as well as ensuring consistency in terms of UX.

## Installation

Install the package [Bioruebe.BioLib](https://www.nuget.org/packages/Bioruebe.BioLib/) with NuGet.

## Library functions

- Command line interface helpers: prompts, progress display, functions for common tasks
- File I/O:
  - Automatic overwrite prompts
  - Path validation
- Working with binary data and streams: pattern search, copy, split, dump to file
- Logging: pretty console outputs for many file types
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `cicdec.md`
```markdown
# 📦 Bioruebe/cicdec [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/cicdec


## Meta
- **Stars:** ⭐ 39 | **Forks:** 🍴 6
- **Language:** C# | **License:** BSD-3-Clause
- **Last updated:** 2026-02-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An unpacker for Clickteam Install Creator installers

## README (trích đầu)
```
# cicdec
Extract files from installers made with Clickteam Install Creator.

### Usage

`cicdec [<options>...] <installer> [<output_directory>]`

If no output directory is specified, all files are extracted to a subdirectory named after the input file.

##### Options

| Switch       | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| -v <version> | Extract as installer version <version>. Auto-detection might not always work correctly, so it is possible to explicitly set the installer version. Possible values are `20`, `24`, `30`, `35`, `40` |
| -db        | Dump blocks. Save additional installer data like registry changes, license files and the uninstaller. This is considered raw data and might not be readable or usable. |
| -dfb       | Dump file block. This is raw binary data containing all files in compressed form and only useful for debugging purposes. |
| -si          | Simulate extraction without writing files to disk. Useful for debugging. |



### Limitations

- Installers, which contain multiple product versions, are not supported
	- This includes official Clickteam products, such as the Install Creator and Patch Maker installers themselves
- Encrypted installers are not supported
- Installer versions below 2.0.0.20 are untested and might not be supported. Please open an issue if you encounter an installer, which fails to extract
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `godotdec.md`
```markdown
# 📦 Bioruebe/godotdec [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/godotdec


## Meta
- **Stars:** ⭐ 218 | **Forks:** 🍴 19
- **Language:** C# | **License:** BSD-3-Clause
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An unpacker for Godot Engine package files (.pck)

## README (trích đầu)
```
# godotdec

An unpacker for Godot Engine package files (.pck)

### Usage
`godotdec [<options>] <input_file> [<output_dir>]`

###### Options:

| Flag (short) | Flag (long) | Description                                                  |
| ------------ | ----------- | ------------------------------------------------------------ |
| -c           | --convert   | Convert certain engine-specific file types (textures, some audio streams) to standard formats. |

### Technical details

Godot Engine's package format is specified as:

| Value/Type | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| 0x43504447 | Magic number (GDPC)                                          |
| 4 x Int32  | Engine version: version, major, minor, revision              |
| 16 x Int32 | Reserved space, 0                                            |
| Int32      | Number of files in archive                                   |
|            | ----- Begin of file index, for each file the following data is stored ---- |
| Int32      | Length of path string                                        |
| String     | Path as string, e.g. res://actors/Enemy/enemy.atex           |
| Int64      | File offset                                                  |
| Int64      | File size                                                    |
| 16 bytes   | MD5                                                          |
|            | ----- Begin of file contents -----                           |

The source code of the .pck packer can be found [here](https://github.com/godotengine/godot/blob/master/core/io/pck_packer.cpp)

### Limitations

- This tool is designed to extract assets. If you are interested in the scripts of a game, check out [Godot RE Tools](https://github.com/bruvzg/gdsdecomp)
- MD5 checksum is not used to verify extracted files
- Format conversion is only supported for .png, .ogg
- Modified engine versions may use a custom package format, which godotdec does not support

### Remarks

No reverse engineering has been used to write this tool.

I released it as a helper for artists to search games for unlicensed use of their assets. It is not meant to encourage extraction with the sole purpose of using assets in your own products without permission of the copyright holder.

Remember: don't steal assets from other people's games. Respect copyrights. And don't protect your own games - it's unnecessary effort.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `rmvdec.md`
```markdown
# 📦 Bioruebe/rmvdec [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/rmvdec


## Meta
- **Stars:** ⭐ 31 | **Forks:** 🍴 3
- **Language:** C# | **License:** BSD-3-Clause
- **Last updated:** 2026-02-27
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A decrypter for RPG-Maker-MV ressource files (.rpgmvp, .rpgmvo, rpgmvm)

## README (trích đầu)
```
# rmvdec

A simple decrypter for RPG-Maker MV resource files (.rpgmvp, .rpgmvo, rpgmvm)

### Usage

`rmvdec <input_file>|<input_dir> [<output_dir>] [-r] [-rm] [-k <decryption_key>|<path_to_System.json>]`

- Rmvdec supports either a single file or a whole folder as input. In folder mode only files with one of the 3 allowed extensions is processed. Subdirectories are ignored per default.
- The encryption/decryption key is needed to extract any file.
  - It can either be specified directly or in form of the path to the games's System.json configuration file.
  - If the 'key' argument is omitted, rmvdec automatically searches up to 5 levels upwards from the input directory for a data folder containing System.json. If the game folder structure is intact, this should always work.

#### Options

| Switch | Alternative switches       | Description                                                      |
| ------ | -------------------------- | ---------------------------------------------------------------- |
| -r     | `--recursive`, `--recurse` | Include files in subdirectories                                  |
| -rm    | `--remove`                 | Delete original files after decryption                           |
| -f     | `--force`                  | Try to decrypt all files, not only those with allowed extensions |

### Technical details

RPG-Maker MV files are encrypted by simply XORing the raw bytes with an encryption key and adding a 16 byte header to the file. The key is saved in System.json, which can be found inside the `/data` folder of the game. The file extension is based on the input type:

| encrypted | original |
| --------- | -------- |
| rpgmvp¹   | png      |
| rpgmvm    | m4a      |
| rpgmvo    | ogg      |

¹ Some games use `.png_` as an extension for images instead. Rmvdec checks for this extension as well.

### Remarks

No reverse engineering has been used to write this tool, it is based on public information about the file format released by other researchers.

I released it as a helper for artists to search games for unlicensed use of their assets. It is not meant to encourage extraction with the sole purpose of using assets in your own products without permission of the copyright holder.

Remember: don't steal assets from other people's games. Respect copyrights. And don't protect your own games - it's unnecessary effort.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `spoondec.md`
```markdown
# 📦 Bioruebe/spoondec [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/spoondec


## Meta
- **Stars:** ⭐ 9 | **Forks:** 🍴 0
- **Language:** C# | **License:** BSD-3-Clause
- **Last updated:** 2025-10-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An extractor for Spoon Installers

## README (trích đầu)
```
# spoondec
Extract files from for Spoon Installers

### Usage

`spoondec <input_file> [<output_dir>]`

If no output directory is specified, all files are extracted to a subdirectory named after the input file.

### Remarks

- Old versions are currently not supported
- This tool is based on [this script](http://wwwhomes.uni-bielefeld.de/joehlschlaeger/unpSpoonInst.cmd.txt) posted on [legroom.net](http://legroom.net/node/842).
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `UniExtract2.md`
```markdown
# 📦 Bioruebe/UniExtract2 [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/UniExtract2


## Meta
- **Stars:** ⭐ 4248 | **Forks:** 🍴 374
- **Language:** AutoIt | **License:** GPL-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Universal Extractor 2 is a tool to extract files from any type of archive or installer.

## README (trích đầu)
```
# Universal Extractor 2 _(UniExtract2)_

[![Download](https://img.shields.io/badge/download-success?style=for-the-badge)](https://github.com/Bioruebe/UniExtract2#download)

Universal Extractor 2 is a tool designed to **extract files from any type of extractable file**.

Unlike most archiving programs, UniExtract is not limited to **standard archives** such as `.zip` and `.rar`. It can also deal with **application installers**, **disk images** and even **game archives** and other **multimedia files**. An overview of supported file types can be found [here](/brain/knowledge/docs_legacy/FORMATS.md)

This program is an unofficial updated and extended version of the [original UniExtract by Jared Breland](http://legroom.net/software/uniextract). As the development of the original version has stopped and no update has been published for years, many forks (modified versions, maintained by volunteers from the community) have arisen. This is the most advanced of them, featuring a very long list of enhancements.

## New features in version 2

- 500+ new supported file types
- Batch mode
- Scan only mode to detect the type of any given file
- Built-in updater
- Support for password list for common archives
- Improved context menu integration and status box
- Better and faster file analysis
- Silent mode, not showing any prompts
- Many interface improvements and redesigned dialogs
- Resource usage/speed improvements, lots of bug fixes

See the [changelog](brain/knowledge/docs_legacy/changelog.txt) for a complete log of all improvements.

## Download

Get the latest version [here](https://github.com/Bioruebe/UniExtract2/releases/download/v2.0.0-rc.3/UniExtractRC3.zip)

###### Virus alert?

Universal Extractor does not contain any malware. Some anti-virus programs occasionally misdetect files inside UniExtract's program directory. You can be sure that this is a so-called false positive, an error - if you downloaded UniExtract from the official source at `https://github.com/Bioruebe/UniExtract2`. A more detailed explanation can be found [here](/brain/knowledge/docs_legacy/ANTI-MALWARE.md). If you encounter a false positive, please report it [here](https://github.com/Bioruebe/UniExtract2/issues/78).

###### 'Windows protected your PC'?

Modern versions of Windows have a feature called *SmartScreen*, which warns about unknown files. This means software without a big company behind it and/or a huge userbase produces a warning. Don't panic! Mostly this happens after a new version of UniExtract has been released. After enough users updated their installation, the warning might vanish, because it now has reputation. If you see a *SmartScreen* warning, you can safely click 'More info', then 'Run anyway'.

###### System requirements

In short: Windows XP or newer.
However, outdated version of Windows only have limited support:

- Windows 7: sending feedback requires you to follow [this guide by Microsoft](https://support.microsoft.com/en-us/help/3140245/update-to-enable-tls-1-1-and-tls-1-2-as-default-secure-protocols-in-wi), otherwise it
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `utagedec.md`
```markdown
# 📦 Bioruebe/utagedec [🔖 PENDING/APPROVE]
🔗 https://github.com/Bioruebe/utagedec


## Meta
- **Stars:** ⭐ 4 | **Forks:** 🍴 0
- **Language:** Haxe | **License:** BSD-3-Clause
- **Last updated:** 2025-06-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A simple decrypter for utage encrypted files (.utage)

## README (trích đầu)
```
# utagedec
A simple decryptor for utage encrypted files (.utage)

### Usage
`utagedec <input_file>|<input_dir> [<output_dir>] [-k <decryption_key>]`

- Utagedec supports either a single file or a whole folder as input. In folder mode only files with one of 3 the allowed extensions is processed. Subdirectories are ++ignored++.
- The encryption/decryption key is needed to extract any file. Automatic detection is not supported yet. (I don't have enough sample games to test.) If no key is provided the engine's standard key is used to decrypt the files - this may or may not work for your game.

### Technical details

UTAGE encrypts assets using a modified XOR algorithm: if the input byte is either zero or the same as the next byte of the key, it is not touched (to prevent leaking the key in files with sequences of zero bytes). Otherwise, the byte is XOR-ed.
There are also functions to compress assets before encrypting and the possibility to overwrite the encryption code with a custom algorithm. Both are currently not supported by utagedec.

### Limitations

- UTAGE also supports compression of asset files, utagedec doesn't at the moment. So if the output is not useful, it may have been compressed (or the decryption key was wrong).
- The decryption key cannot be determined automatically yet.
- Games made with UTAGE can use a custom encryption algorithm. This may be different for each game, and is also not supported by utagedec.
- If you found a game, which is not supported, feel free to open an issue and send me a sample file.

### Remarks
This is the result of analysing the file type itself, no reverse engineering has been used to write this tool.

I released it as a helper for artists to search games for unlicensed use of their assets. It is not meant to encourage extraction with the sole purpose of using assets in your own products without permission of the copyright holder.

Remember: don't steal assets from other people's games. Respect copyrights. And don't protect your own games - it's unnecessary effort.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

