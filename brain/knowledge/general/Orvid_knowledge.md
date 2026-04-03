---
id: orvid-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:18.301140
---

# KNOWLEDGE EXTRACT: Orvid
> **Extracted on:** 2026-03-30 17:50:34
> **Source:** Orvid

---

## File: `Champollion.md`
```markdown
# 📦 Orvid/Champollion [🔖 PENDING/APPROVE]
🔗 https://github.com/Orvid/Champollion


## Meta
- **Stars:** ⭐ 135 | **Forks:** 🍴 27
- **Language:** C++ | **License:** LGPL-3.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A PEX to Papyrus Decompiler for Skyrim, Fallout 4 and Starfield

## README (trích đầu)
```
# Champollion

Champollion is a decompiler for the Papyrus script language used in Skyrim, Fallout 4, Fallout 76, and Starfield. It aims to produce a Papyrus Script file (.psc) from a .pex binary file. The decompiled script should recompile to a functionally equivalent PEX binary.

## Usage

Champollion is a CLI-only program.

### Parameters

`Champollion <files or directories> [-p <output directory>] [-a [<assembly directory>]] [-c] [-t]`

| Short                     | Long                         | Description                                                  |
| ------------------------- | ---------------------------- | ------------------------------------------------------------ |
| -p *output directory*     | --psc *output directory*     | Set the output directory, where Champollion will write the decompiled files |
| -a [*assembly directory*] | --asm [*assembly directory*] | Champollion will write an assembly version of the PEX file in the given directory, if one. The assembly file is an human readable version of the content of the PEX file |
| -c                        | --comment                    | The decompiled file will be annotated with the assembly instruction corresponding to the decompiled code lines. |
| -t                        | --threaded                   | Champollion will parallelize the decompilation. It is useful when decompiling a directory containing many PEX files. |
| -r                        | --recursive                  | Recursively scan specified directory(s) for pex files to decompile|
| -s                        | --recreate-subdirs           | Recreates directory structure for script in root of output directory (Fallout 4 only, default false) |
| -e                        | --header                     | Write header to decompiled psc file                          |
| -g                        | --trace                      | Trace the decompilation and output results to rebuild log    |
|                           | --no-dump-tree               | Do not dump tree for each node during decompilation tracing (requires --trace) |
|                           | --debug-funcs                | Decompile inoperative debug and compiler-generated functions (default false) |
|                           | --no-debug-line              | Do not comment with debug info line numbers on script lines (default false) |
| -i                        | --print-info                 | Print header info from the specified PEX file(s) and exit    |
|                           | --print-compile-time         | Print the compile time of the script in format of {filename}: {time_integer} and exit |
| -v                        | --verbose                    | Verbose output                                               |
| -V                        | --version                    | Output version number                                        |
| -h                        | --help                       | Print help message                   
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

