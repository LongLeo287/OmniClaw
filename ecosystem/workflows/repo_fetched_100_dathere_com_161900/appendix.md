---
jupytext:
    text_representation:
        extension: .md
        format_name: myst
kernelspec:
    display_name: Bash
    language: bash
    name: bash
---

# Appendix

Here you may find conceptual content related to the exercises in the book.

## qsv version

qsv has multiple versions and may differ for each system. Here we run [a command](https://github.com/dathere/qsv/blob/master/docs/PERFORMANCE.md#version-details) to show what version of qsv this book is using along with other information:

```{code-cell}
qsv --version
```

## qsv release assets

A mapping of qsv release files for an arbitrary version X.Y.Z and platforms they may run on are shown in the table below.

```{table} qsv release assets (vX.Y.Z)
:name: qsv-release-assets

| File                                      | Platform |
| ----------------------------------------- | ------------------------- |
| `qsv-X.Y.Z-x86_64-pc-windows-msvc.zip`    | 64-bit MSVC (Windows 10+)            |
| `qsv-X.Y.Z.msi`                           | Windows                   |
| `qsv-X.Y.Z-x86_64-pc-windows-gnu.zip`     | 64-bit MinGW (Windows 10+)            |
| `qsv-X.Y.Z-i686-pc-windows-msvc.zip`      | 32-bit MSVC (Windows 10+)               |
| `qsv-X.Y.Z-aarch64-apple-darwin.zip`      | ARM64 macOS (11.0+, Big Sur+)       |
| `qsv-X.Y.Z-x86_64-apple-darwin.zip`       | 64-bit macOS (10.12+, Sierra+)      |
| `qsv-X.Y.Z-aarch64-unknown-linux-gnu.zip` | ARM64 Linux (kernel 4.1, glibc 2.17+)                 |
| `qsv-X.Y.Z-x86_64-unknown-linux-gnu.zip`  | 64-bit Linux (kernel 3.2+, glibc 2.17+)              |
| `qsv-X.Y.Z-x86_64-unknown-linux-musl.zip` | 64-bit Linux with musl 1.2.3              |
| `qsv-X.Y.Z-i686-unknown-linux-gnu.zip`    | 32-bit Linux (kernel 3.2+, glibc 2.17+)                 |
```

:::{note}
The listed OS/architecture are primarily based on [information from "The rustc book"](https://doc.rust-lang.org/nightly/rustc/platform-support.html).
:::

(command-data-streams)=
## Command data streams (`stdin`, `stdout`, and `stderr`)

The terms `stdin`, `stdout`, and `stderr` may commonly be found within qsv's source code and in the lessons.

Here's a very brief explanation of what each means in the context of a command:

- `stdin` ("Standard input"): Input data
- `stdout` ("Standard out"): Output data
- `stderr` ("Standard error"): Error output

Let's consider the following pipeline as an example:

```bash
qsv clipboard | qsv stats -E
```

- There are two commands ran here, each separated by a pipe (`|`).
- The output (`stdout`) of `qsv clipboard` is used as the input (`stdin`) of `qsv stats -E`.

For further explanation you may read online articles regarding piping commands. You may view a few more examples [here](https://zerotomastery.io/cheatsheets/linux-commands-cheat-sheet/#piping-and-command-redirection).
