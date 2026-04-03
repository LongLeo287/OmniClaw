---
id: github.com-sharkdp-fd-9a9a1d07-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:21.781839
---

# KNOWLEDGE EXTRACT: github.com_sharkdp_fd_9a9a1d07
> **Extracted on:** 2026-04-01 12:39:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521934/github.com_sharkdp_fd_9a9a1d07

---

## File: `.gitignore`
```
target/
/autocomplete/
**/*.rs.bk
```

## File: `CHANGELOG.md`
```markdown
# Unreleased

## Bugfixes
- Handle invalid working directories gracefully when using `--full-path`, see #1900 (@Xavrir).

# 10.4.2

## Bugfixes
- Fixed performance regression due to `--ignore-contain`; see #1913 and #1914

# 10.4.1

This is just a re-release of 10.4.0 due to an issue with the 10.4.0 release.

# 10.4.0

## Features
- Add `--ignore-contain` option to ignore directories containing a named entry (e.g. to ignore [`CACHEDIR.TAG`](https://bford.info/cachedir/)); see #1727 (@fischman).

## Bugfixes

- Fix Windows hyperlink generation for paths with spaces. (#1872)

- `--print0` combined with `--exec` will now print a `\0` between the output of each entry. Note that if there are multiple instances
  of `--exec`, the `\0` will be between each _set_ of commands, _not_ between each individual command run. Fixes #1797.

- Several bugs were fixed by an update to the `ignore` library used for handling ignore rules
    - #1506
    - #1667
    - #1813

## Changes

- Minimum required rust version has been increased to 1.90.0. Notably, this means dropping fully support for intel Mac and Windows 7.
- Statically link the CRT for MSVC builds via Cargo config to avoid runtime DLL dependencies, see #1874 (@FidelSch)

# 10.3.0

## Features

- Add a hidden `--mindepth` alias for `--min-depth`. (#1617)


## Bugfixes


## Changes

- Replace `humantime` crate and `chrono` crate with `jiff` crate, see #1690 (@sorairolake). This has some small changes to the
  way dates given to options such `--changed-within` and `--changed-before` including:
  - 'M' no longer means "month", as that could be confusing with minutes. Use "mo", "mos", "month" or "months" instead.
  - month and year now account for variability in the calander rather than being a hard-coded number of seconds. That is probably
    what you would expect, but it is a slight change in behavior.
- aarch64 Windows was added to CI and release artifacts
- Many dependencies were updated
- Better support building on Illumos (there is no automated testing, but some known issues were fixed)

## Other

This will be the last release that has been tested on x86_64 Mac OS, since GitHub is
dropping support for runners with that hardware.

It may also be the last release to use a version of Rust with tier-1 support for
x86_64/intel Macs and Windows 7.


# 10.2.0

## Features

- Add --hyperlink option to add OSC 8 hyperlinks to output


## Bugfixes


## Changes

- Build windows releases with rust 1.77 so windows 7 is still supported
- Deb packages now include symlink for fdfind to be more consistent with official packages


## Other

# 10.1.0

## Features

- Allow passing an optional argument to `--strip-cwd-prefix` of "always", "never", or "auto". to force whether the cwd prefix is stripped or not.
- Add a `--format` option which allows using a format template for direct ouput similar to the template used for `--exec`. (#1043)

## Bugfixes
- Fix aarch64 page size again. This time it should actually work. (#1085, #1549) (@tavianator)


## Other

- aarch64-apple-darwin target added to builds on the release page. Note that this is a tier 2 rust target.

# v10.0.0

## Features

- Add `dir` as an alias to `directory` when using `-t` \ `--type`, see #1460 and #1464 (@Ato2207).
- Add support for @%s date format in time filters similar to GNU date (seconds since Unix epoch for --older/--newer), see #1493 (@nabellows)
- Breaking: No longer automatically ignore `.git` when using `--hidden` with vcs ignore enabled. This reverts the change in v9.0.0. While this feature
  was often useful, it also broke some existing workflows, and there wasn't a good way to opt out of it. And there isn't really a good way for us to add
  a way to opt out of it. And you can easily get similar behavior by adding `.git/` to your global fdignore file.
    See #1457.

## Bugfixes

- Respect NO_COLOR environment variable with `--list-details` option. (#1455)
- Fix bug that would cause hidden files to be included despite gitignore rules
  if search path is "." (#1461, BurntSushi/ripgrep#2711).
- aarch64 builds now use 64k page sizes with jemalloc. This fixes issues on some systems, such as ARM Macs that
  have a larger system page size than the system that the binary was built on. (#1547)
- Address [CVE-2024-24576](https://blog.rust-lang.org/2024/04/09/cve-2024-24576.html), by increasing minimum rust version.


## Changes
- Minimum supported rust version is now 1.77.2


# v9.0.0

## Performance

- Performance has been *significantly improved*, both due to optimizations in the underlying `ignore`
  crate (#1429), and in `fd` itself (#1422, #1408, #1362) - @tavianator.
  [Benchmarks results](https://gist.github.com/tavianator/32edbe052f33ef60570cf5456b59de81) show gains
  of 6-8x for full traversals of smaller directories (100k files) and up to 13x for larger directories (1M files).

- The default number of threads is now constrained to be at most 64. This should improve startup time on
  systems with many CPU cores. (#1203, #1410, #1412, #1431) - @tmccombs and @tavianator

- New flushing behavior when writing output to stdout, providing better performance for TTY and non-TTY
  use cases, see #1452 and #1313 (@tavianator).

## Features

- Support character and block device file types, see #1213 and #1336 (@cgzones)
- Breaking: `.git/` is now ignored by default when using `--hidden` / `-H`, use `--no-ignore` / `-I` or
  `--no-ignore-vcs` to override, see #1387 and #1396 (@skoriop)

## Bugfixes

- Fix `NO_COLOR` support, see #1421 (@acuteenvy)

## Other

- Fixed documentation typos, see #1409 (@marcospb19)

## Thanks

Special thanks to @tavianator for his incredible work on performance in the `ignore` crate and `fd` itself.



# v8.7.1

## Bugfixes

- `-1` properly conflicts with the exec family of options.
- `--max-results` overrides `-1`
- `--quiet` properly conflicts with the exec family of options. This used to be the case, but broke during the switch to clap-derive
- `--changed-within` now accepts a space as well as a "T" as the separator between date and time (due to update of chrono dependency)

## Other
- Many dependencies were updated
- Some documentation was updated and fixed

# v8.7.0

## Features

- Add flag --no-require-git to always respect gitignore files, see #1216 (@vegerot)

## Bugfixes

- Fix logic for when to use global ignore file. There was a bug where the only case where the
  global ignore file wasn't processed was if `--no-ignore` was passed, but neither `--unrestricted`
  nor `--no-global-ignore-file` is passed. See #1209

# v8.6.0

## Features

- New `--and <pattern>` option to add additional patterns that must also be matched. See #315
  and #1139 (@Uthar)
- Added `--changed-after` as alias for `--changed-within`, to have a name consistent with `--changed-before`.


## Changes

- Breaking: On Unix-like systems, `--type executable` now additionally checks if
  the file is executable by the current user, see #1106 and #1169 (@ptipiak)


## Bugfixes

- Use fd instead of fd.exe for Powershell completions (when completions are generated on windows)


## Other


# v8.5.3

## Bugfixes

- Fix completion generation to not include full path of fd command
- Fix build error if completions feature is disabled

# v8.5.2

## Bugfixes

- Fix --owner option value parsing, see #1163 and #1164 (@tmccombs)


# v8.5.1

## Bugfixes

- Fix --threads/-j option value parsing, see #1160 and #1162 (@sharkdp)


# v8.5.0

## Features

- `--type executable`/`-t` now works on Windows, see #1051 and #1061 (@tavianator)

## Bugfixes

- Fixed differences between piped / non-piped output. This changes `fd`s behavior back to what we
  had before 8.3.0, i.e. there will be no leading `./` prefixes, unless `--exec`/`-x`,
  `--exec-batch`/`-X`, or `--print0`/`-0` are used. `--strip-cwd-prefix` can be used to strip that
  prefix in those cases. See #1046, #1115, and #1121 (@tavianator)
- `fd` could previously crash with a panic due to a race condition in Rusts standard library
  (see https://github.com/rust-lang/rust/issues/39364). This has been fixed by switching to a different
  message passing implementation, see #1060 and #1146 (@tavianator)
- `fd`s memory usage will not grow unboundedly on huge directory trees, see #1146 (@tavianator)
- fd returns an error when current working directory does not exist while a search path is
  specified, see #1072 (@vijfhoek)
- Improved "command not found" error message, see #1083 and #1109 (@themkat)
- Preserve command exit codes when using `--exec-batch`, see #1136 and #1137 (@amesgen)

## Changes

- No leading `./` prefix for non-interactive results, see above.
- fd now colorizes paths in parallel, significantly improving performance, see #1148 (@tavianator)
- fd can now avoid `stat` syscalls even when colorizing paths, as long as the color scheme doesn't
  require metadata, see #1148 (@tavianator)
- The statically linked `musl` versions of `fd` now use `jmalloc`, leading to a significant performance
  improvement, see #1062 (@tavianator)

## Other

- Added link back to GitHub in man page and `--help` text, see #1086 (@scottchiefbaker)
- Major update in how `fd` handles command line options internally, see #1067 (@tmccombs)

# v8.4.0

## Features

- Support multiple `--exec <cmd>` instances, see #406 and #960 (@tmccombs)

## Bugfixes

- "Argument list too long" errors can not appear anymore when using `--exec-batch`/`-X`, as the command invocations are automatically batched at the maximum possible size, even if `--batch-size` is not given. See #410 and #1020 (@tavianator)

## Changes

- Directories are now printed with an additional path separator at the end: `foo/bar/`, see #436 and #812 (@yyogo)
- The `-u` flag was changed to be equivalent to `-HI` (previously, a single `-u` was only equivalent to `-I`). Additional `-u` flags are still allowed, but ignored. See #840 and #986 (@jacksontheel)

## Other

- Added installation instructions for RHEL8, see #989 (@ethsol)


# v8.3.2

## Bugfixes

- Invalid absolute path on windows when searching from the drive root, see #931 and #936 (@gbarta)


# v8.3.1

## Bugfixes

- Stop implying `--no-ignore-parent` when `--no-vcs-ignore` is supplied, see #907, #901, #908 (@tmccombs)
- fd no longer waits for the whole traversal if the only matches arrive within max_buffer_time, see #868 and #895 (@tavianator)
- `--max-results=1` now immediately quits after the first result, see #867
- `fd -h` does not panic anymore when stdout is closed, see #897

## Changes

- Disable jemalloc on FreeBSD, see #896 (@xanderio)
- Updated man page, see #912 (@rlue)
- Updated zsh completions, see #932 (@tmccombs)


# v8.3.0

## Performance improvements

- Colorized output is now significantly faster, see #720 and #853 (@tavianator)
- Writing to stdout is now buffered if the output does not go to a TTY. This increases performance
  when the output of `fd` is piped to another program or to a file, see #885 (@tmccombs, original
  implementation by @sourlemon207)
- File metadata is now cached between the different filters that require it (e.g. `--owner`,
  `--size`), reducing the number of `stat` syscalls when multiple filters are used; see #863
  (@tavianator, original implementation by @alexmaco)

## Features

- Don't buffer command output from `--exec` when using a single thread. See #522
- Add new `-q, --quiet` flag, see #303 (@Asha20)
- Add new `--no-ignore-parent` flag, see #787 (@will459)
- Add new `--batch-size` flag, see #410 (@devonhollowood)
- Add opposing command-line options, see #595 (@Asha20)
- Add support for more filesystem indicators in `LS_COLORS`, see
  https://github.com/sharkdp/lscolors/pull/35 (@tavianator)

## Bugfixes

- Always show the `./` prefix for search results unless the output is a TTY or `--strip-cwd-prefix` is set, see #760 and #861 (@jcaplan)
- Set default path separator to `/` in MSYS, see #537 and #730 (@aswild)
- fd cannot search files under a RAM disk, see #752
- fd doesn't show substituted drive on Windows, see #365
- Properly handle write errors to devices that are full, see #737
- Use local time zone for time functions (`--change-newer-than`, `--change-older-than`), see #631 (@jacobmischka)
- Support `--list-details` on more platforms (like BusyBox), see #783
- The filters `--owner`, `--size`, and `--changed-{within,before}` now apply to symbolic links
  themselves, rather than the link target, except when `--follow` is specified; see #863
- Change time comparisons to be exclusive, see #794 (@jacobmischka)

## Changes

- Apply custom `--path-separator` to commands run with `--exec(-batch)` and `--list-details`, see #697 (@aswild)

## Other

- Many documentation updates


# v8.2.1

No functional changes with respect to v8.2.0. Bugfix in the release process.

# v8.2.0

## Features

- Add new `--prune` flag, see #535 (@reima)
- Improved the usability of the time-based options, see #624 and #645 (@gorogoroumaru)
- Add support for exact file sizes in the `--size` filter, see #669 and #696 (@Rogach)
- `fd` now prints an error message if the search pattern requires a leading dot but
  `--hidden` is not enabled (Unix only), see #615

## Bugfixes

- Avoid panic when performing limited searches in directories with restricted permissions, see #678
- Invalid numeric command-line arguments are silently ignored, see #675
- Disable jemalloc on Android, see #662
- The `--help` text will be colorless if `NO_COLOR` has been set, see #600 (@xanonid)

## Changes

- If `LS_COLORS` is not set (e.g. on Windows), we now provide a more comprehensive default which
  includes much more filetypes, see #604 and #682 (mjsir911).

## Other

- Added `zsh` completion files, see #654 and #189 (@smancill)

# v8.1.1

## Bugfixes

- Support colored output on older Windows versions if either (1) `--color=always` is set or (2) the `TERM` environment variable is set. See #469

# v8.1.0

## Features

- Add new `--owner [user][:group]` filter. See #307 (pull #581) (@alexmaco)
- Add support for a global ignore file (`~/.config/fd/ignore` on Unix), see #575 (@soedirgo)
- Do not exit immediately if one of the search paths is missing, see #587 (@DJRHails)

## Bugfixes

- Reverted a change from fd 8.0 that enabled colors on all Windows terminals (see below) in order to support older Windows versions again, see #577. Unfortunately, this re-opens #469
- Fix segfault caused by jemalloc on macOS Catalina, see #498
- Fix `--glob` behavior with empty pattern, see #579 (@SeamusConnor)
- Fix `--list-details` on FreeBSD, DragonFly BSD, OpenBSD and NetBSD. See #573 (@t6)

## Changes

- Updated documentation for `--size`, see #584

# v8.0.0

## Features

- Add a new `-l`/`--list-details` option to show more details about the search results. This is
  basically an alias for `--exec-batch ls -l` with some additional `ls` options.
  This can be used in order to:
    * see metadata like permissions, owner, file size, modification times (#491)
    * see symlink targets (#482)
    * achieve a deterministic output order (#324, #196, #159)
- Add a new `--max-results=<count>` option to limit the number of search results, see #472, #476 and #555
  This can be useful to speed up searches in cases where you know that there are only N results.
  Using this option is also (slightly) faster than piping to `head -n <count>` where `fd` can only
  exit when it finds the search results `<count> + 1`.
- Add the alias `-1` for `--max-results=1`, see #561. (@SimplyDanny).
- Add new `--type socket` and `--type pipe` filters, see #511.
- Add new `--min-depth <depth>` and `--exact-depth <depth>` options in addition to the existing option
  to limit the maximum depth. See #404.
- Support additional ANSI font styles in `LS_COLORS`: faint, slow blink, rapid blink, dimmed, hidden and strikethrough.

## Bugfixes

- Preserve non-UTF8 filenames: invalid UTF-8 filenames are now properly passed to child-processes
  when using `--exec`, `--exec-batch` or `--list-details`. In `fd`'s output, we replace non-UTF-8
  sequences with the "�" character. However, if the output of `fd` goes to another process, we
  print the actual bytes of the filename. For more details, see #558 and #295.
- `LS_COLORS` entries with unsupported font styles are not completely ignored, see #552

## Changes

- Colored output will now be enabled by default on older Windows versions.
  This allows the use of colored output if the terminal supports it (e.g.
  MinTTY, Git Bash). On the other hand, this will be a regression for users
  on older Windows versions with terminals that do not support ANSI escape
  sequences. Affected users can use an alias `fd="fd --color=never"` to
  continue using `fd` without colors. There is no change of behavior for
  Windows 10. See #469.
- When using `--glob` in combination with `--full-path`, a `*` character does not match a path
  separation character (`/` or `\\`) anymore. You can use `**` for that. This allows things like
  `fd -p -g '/some/base/path/*/*/*.txt'` which would previously match to arbitrary depths (instead
  of exactly two folders below `/some/base/path`. See #404.
- "Legacy" support to use `fd -exec` (with a single dash) has been removed. Use `fd -x` or
  `fd --exec` instead.
- Overall improved error handling and error messages.


## Other

- Korean translation of the README, see: [한국어](https://github.com/spearkkk/fd-kor) (@spearkkk)


# v7.5.0

## Features

- Added `--one-file-system` (aliases: `--mount`, `--xdev`) to not cross file system boundaries on Unix and Windows, see #507 (@FallenWarrior2k).
- Added `--base-directory` to change the working directory in which `fd` is run, see #509 and #475 (@hajdamak).
- `fd` will not use colored output if the `NO_COLOR` environment variable is set, see #550 and #551 (@metadave).
- `fd --exec` will return exit code 1 if one of the executed commands fails, see #526 and #531 (@fusillicode and @Giuffre)

## Bug Fixes

- Fixed 'command not found' error when using zsh completion, see #487 (@barskern).
- `fd -L` should include broken symlinks, see #357 and #497 (@tommilligan, @neersighted and @sharkdp)
- Display directories even if we don't have permission to enter, see #437 (@sharkdp)

## Changes

- A flag can now be passed multiple times without producing an error, see #488 and #496 (@rootbid).
- Search results are sorted when using the `-X` option to match the behaviour of piping to `xargs`, see #441 and #524 (@Marcoleni @crash-g).


# v7.4.0

## Performance improvements

- Reduce number of `stat` syscalls, improving the performance for searches where file metadata is
  required (`--type`, `--size`, `--changed-within`, …), see #434 (@tavianator)
- Use jemalloc by default, improving the performance for almost all searches, see #481. Note that
  Windows and `*musl*` builds do not profit from this.

## Features

- Added a new `-g`/`--glob` option to switch to glob-based searches (instead of regular expression
  based searches). This is accompanied by a new `--regex` option that can be used to switch back,
  if users want to `alias fd="fd --glob"`. See #284
- Added a new `--path-separator <sep>` option which can be useful for Windows users who
  want/need `fd` to use `/` instead of `\`, see #428 and #153 (@mookid)
- Added support for hidden files on Windows, see #379
- When `fd` is run with the `--exec-batch`/`-X` option, it now exposes the exit status of the
  command that was run, see #333.
- Exit immediately when Ctrl-C has been pressed twice, see #423

## Bugfixes

- Make `--changed-within`/`--changed-before` work for directories, see #470

## Other

- Pre-built `fd` binaries should now be available for `armhf` targets, see #457 (@detly)
- `fd` is now available on Alpine Linux, see #451 (@5paceToast)
- `fd` is now in the officla FreeBSD repositories, see #412 (@t6)
- Added OpenBSD install instructions, see #421 (@evitalis)
- Added metadata to the Debian package, see #416 (@cathalgarvey)
- `fd` can be installed via npm, see #438 (@pablopunk)


# v7.3.0

## Features

- New `--exec-batch <cmd>`/`-X <cmd>` option for batch execution of commands, see #360 (@kimsnj).
  This allows you to do things like:
  ``` bash
  fd … -X vim  # open all search results in vim (or any other editor)
  fd … -X ls -l  # view detailed stats about the search results with 'ls'
  fd -e svg -X inkscape  # open all SVG files in Inkscape
  ```
- Support for 24-bit color codes (when specified via `LS_COLORS`) as well as
  different font styles (bold, italic, underline).

## Changes

- A few performance improvements, in particular when printing lots of colorized
  results to the console, see #370
- The `LS_COLORS` handling has been "outsourced" to a separate crate (https://github.com/sharkdp/lscolors) that is now being used by other tools as well: [fselect](https://github.com/jhspetersson/fselect), [lsd](https://github.com/Peltoche/lsd/pull/84). For details, see #363.

## Other

- `fd` will be available in Ubuntu Disco DIngo (19.04), see #373 (@sylvestre)
- This release should come with a static ARM binary (`arm-unknown-linux-musleabihf`), see #320 (@duncanfinney)
- Various documentation improvements, see #389

## Thanks

Special thanks to @alexmaco for his awesome work on refactoring and code improvements! (see #401, #398, and #383)

# v7.2.0

## Features

* Added support for filtering by file modification time by adding two new options `--changed-before <date|duration>` and `--changed-within <..>`. For more details, see the `--help` text, the man page, the relevant issue #165 and the PR #339 (@kimsnj)
* Added `--show-errors` option to enable the display of filesystem error messages such as "permission denied", see #311 (@psinghal20 and @majecty)
* Added `--maxdepth` as a (hidden) alias for `--max-depth`, see #323 (@mqudsi)
* Added `--search-path` option which can be supplied to replace the positional `path` argument at any position.

## Changes

* Loosen strict handling of missing `--ignore-file`, see #280 (@psinghal20)
* Re-enabled `.ignore` files, see #156.

## Bugfixes

* `fd` could previously get stuck when run from the root directory in the
  presence of zombie processes. This curious bug has been fixed in Rust 1.29 and higher. For more details, see #288, [rust-lang/rust#50619](https://github.com/rust-lang/rust/issues/50619) and [the fix](https://github.com/rust-lang/rust/pull/50630)

## Other

* `fd` has officially landed in Debian! See #345 for details. Thanks goes to @sylvestre, @paride and possibly others I don't know about.
* Added Chinese translation of README (@chinanf-boy)

## Thanks

A special thanks goes to @joshleeb for his amazing improvements throughout
the code base (new tests, refactoring work and various other things)!


# v7.1.0

## Features

* Added `--size` filter option, see #276 (@stevepentland, @JonathanxD and @alexmaco)
* Added `--type empty` (or `-t e`) to search for empty files and/or directories, see #273

## Changes

* With the new version, `.gitignore` files will only be respected in Git repositories, not outside.
* A few performance improvements for `--type` searches, see 641976cf7ad311ba741571ca8b7f02b2654b6955 and 50a2bab5cd52d26d4a3bc786885a2c270ed3b227

## Other

* Starting with this release, we will offer pre-built ARM binaries, see #244
* Added instructions on how to use `fd` with `emacs`, see #282 (@redguardtoo)
* `fd` is now in the official openSUSE repositories, see #275 (@avindra)
* `fd` is now available via MacPorts, see #291 (@raimue)


# v7.0.0

## Features

* Added `--type executable` (or `-t x`) to search for executable files only, see #246 (@PramodBisht)
* Added support for `.fdignore` files, see #156 and #241.
* Added `--ignore-file` option to add custom ignore files, see #156.
* Suggest `--fixed-strings` on invalid regular expressions, see #234 (@PramodBisht)
* Detect when user supplied path instead of pattern, see #235.

## Changes

* `.ignore` and `.rgignore` files are not parsed anymore. Use `.fdignore` files
  or add custom files via `--ignore-file` instead.
* Updated to `regex-syntax` 0.5 (@cuviper)

## Bugfixes

* Properly normalize absolute paths, see #268
* Invalid utf8 filenames displayed when `-e` is used, see #250
* If `--type` is used, fifos/sockets/etc. are always shown, see #260

## Other

* Packaging:
    * The Arch Linux package is now simply called `fd`.
    * There is now a `fd` ebuild for Gentoo Linux.
    * There is a `scoop` package for `fd` (Windows).
    * There is a `Chocolatey` package for `fd` (Windows).
    * There is a Fedora `copr` package for `fd`.


# v6.3.0

## Features

* Files with multiple extensions can now be found via `--extension`/`-e`, see #214 (@althonos)
  ``` bash
  > fd -e tar.gz
  ```

* Added new `-F`/`--fixed-strings`/`--literal` option that treats the pattern as a literal string instead of a regular expression, see #157

  ``` bash
  > fd -F 'file(1).txt'
  ```

* Allow `-exec` to work as `--exec`, see #226 (@stevepentland)

## Bugfixes

* Fixed `Ctrl-C` handling when using `--exec`, see #224 (@Doxterpepper)

* Fixed wrong file owner for files in deb package, see #213

## Other

* Replaced old gif by a fancy new SVG screencast (@marionebl)
* Updated [benchmark results](https://github.com/sharkdp/fd#benchmark) (fd has become faster in the meantime!). There is a new repository that hosts several benchmarking scripts for fd: https://github.com/sharkdp/fd-benchmarks


# v6.2.0

## Features

* Support for filtering by multiple file extensions and multiple file types, see #199 and #177
  (@tkadur).

  For example, it's possible to search for C++ source or header files:
  ``` bash
  > fd -e cpp -e c -e cxx -e h pattern
  ```

## Changes

* The size of the output buffer (for sorting search results) is now limited to 1000 entries. This
  improves the search speed significantly if there are a lot of results, see #191 (@sharkdp).

## Bugfixes

* Fix a bug where long-running searches could not be killed via Ctrl-C, see #210 (@Doxterpepper)
* fd's exit codes are now in accordance with Unix standards, see #201 (@Doxterpepper)

## Other

* Bash, zsh and fish completion should now work with the Ubuntu `.deb` packages, see #195 and #209
  (@tmccombs and @sharkdp)
* There is a new section on how to set up `fzf` to use `fd` in the
  [README](https://github.com/sharkdp/fd#using-fd-with-fzf), see #168.


# v6.1.0

## Features

* Support for multiple search paths, see #166 (@Doxterpepper)
* Added `--no-ignore-vcs` option to disable `.gitignore` and other VCS ignore files,
  without disabling `.ignore` files - see #156 (@ptzz).

## Bugfixes

* Handle terminal signals, see #128 (@Doxterpepper)
* Fixed hang on `--exec` when user input was required, see #178 and #193 (@reima)

## Other

* Debian packages are now created via Travis CI and should be available for this and all
  future releases (@tmccombs).
* fd is now available on Void Linux (@maxice8)
* The minimum required Rust version is now 1.20

## Thanks

@Doxterpepper deserves a special mention for his great work that is included in this release and
for the support in ticket discussions and concerning Travis CI fixes. Thank you very much!

Thanks also go out to @tmccombs for the work on Debian packages and for reviewing a lot of pull requests!

# v6.0.0

## Changes

- The `--exec`/`-x` option does not spawn an intermediate shell anymore. This improves the
  performance of parallel command execution and fixes a whole class of (present and potentially
  future) problems with shell escaping. The drawback is that shell commands cannot directly be
  called with `--exec`. See #155 for the full discussion. These changes have been implemented by
  @reima (Thanks!).

## Bugfixes

- `--exec` does not escape cmd.exe metacharacters on Windows (see #155, as above).

## Other

* *fd* is now available in the FreeBSD ports (@andoriyu)
* The minimal `rustc` version is now checked when building with `cargo`, see #164 (@matematikaadit)
* The output directory for the shell completion files is created if it does not exist (@andoriyu)


# v5.0.0

## Features

* Added new `--exec`, `-x` option for parallel command execution (@mmstick, see #84 and #116). See the corresponding [README section](https://github.com/sharkdp/fd#parallel-command-execution) for an introduction.
* Auto-disable color output on unsupported Windows shells like `cmd.exe` (@iology, see #129)
* Added the `--exclude`, `-X` option to suppress certain files/directories in the search results
  (see #89).
* Added ripgrep aliases `-u` and `-uu` for `--no-ignore` and `--no-ignore --hidden`, respectively
  (@unsignedint, see #92)
* Added `-i`, `--ignore-case` (@iology, see #95)
* Made smart case really smart (@reima, see #103)
* Added RedoxOS support (@goyox86, see #131)

## Changes

* The dot `.` can now match newlines in file names (@iology, see #111)
* The short `--type` argument for symlinks has been changed from `s` to `l` (@jcpetkovich, see #83)

## Bugfixes

* Various improvements in root-path and symlink handling (@iology, see #82, #107, and #113)
* Fixed absolute path handling on Windows (@reima, #93)
* Fixed: current directory not included when using relative path (see #81)
* Fixed `--type` behavior for unknown file types (@iology, see #150)
* Some fixes around `--exec` (@iology, see #142)

## Other

* Major updates and bugfixes to our continuous integration and deployment tooling on Travis
  (@matematikaadit, see #149, #145, #133)
* Code style improvements & automatic style checking via `rustfmt` on Travis (@Detegr, see #99)
* Added a man page (@pickfire, see #77)
* *fd* has been relicensed under the dual license MIT/Apache-2.0 (@Detegr, see #105)
* Major refactorings and code improvements (Big thanks to @gsquire, @reima, @iology)
* First version of [`CONTRIBUTING`](https://github.com/sharkdp/fd/blob/master/CONTRIBUTING.md) guidelines
* There is now a Nix package (@mehandes)
* *fd* is now in the official Arch Linux repos (@cassava)
* Improved tooling around shell completion files (@ImbaKnugel, see #124)
* Updated tutorial in the [`README`](https://github.com/sharkdp/fd/blob/master/README.md)
* The minimum required version of Rust has been bumped to 1.19.

## Thanks

A *lot* of things have happened since the last release and I'd like to thank all contributors for their great support. I'd also like to thank those that have contributed by reporting bugs and by posting feature requests.

I'd also like to take this chance to say a special Thank You to a few people that have stood out in one way or another: To @iology, for contributing a multitude of bugfixes, improvements and new features. To @reima and @Detegr for their continuing great support. To @mmstick, for implementing the most advanced new feature of *fd*. And to @matematikaadit for the CI/tooling upgrades.


# v4.0.0

## Features

* Added filtering by file extension, for example `fd -e txt`, see #56 (@reima)
* Add option to force colored output: `--color always`, see #49 (@Detegr)
* Generate Shell completions for Bash, ZSH, Fish and Powershell, see #64 (@ImbaKnugel)
* Better & extended `--help` text (@abaez and @Detegr)
* Proper Windows support, see #70

## Changes

* The integration tests have been re-written in Rust :sparkles:, making them platform-independent and easily callable via `cargo test` - see #65  (many thanks to @reima!)
* New tutorial in the README (@deg4uss3r)
* Reduced number of `stat` syscalls for each result from 3 to 1, see #36.
* Enabled Appveyor CI

# v3.1.0

## Features
- Added file type filtering, e.g. `find --type directory` or `find -t f` (@exitium)

# v3.0.0

## Features
- Directories are now traversed in parallel, leading to significant performance improvements (see [benchmarks](https://github.com/sharkdp/fd#benchmark))
- Added `--print0` option (@michaelmior)
- Added AUR packages (@wezm)

## Changes
- Changed short flag for `--follow` from `-f` to `-L` (consistency with `ripgrep`)

# v2.0.0

* Changed `--sensitive` to `--case-sensitive`
* Changed `--absolute` to `--absolute-path`
* Throw an error if root directory is not existent, see #39
* Use absolute paths if the root dir is an absolute path, see #40
* Handle invalid UTF-8, see #34 #38
* Support `-V`, `--version` by switching from `getopts` to `clap`.

Misc:
* It's now possible to install `fd` via homebrew on macOS: `brew install fd`.

# v1.1.0

- Windows compatibility (@sebasv), see #29 #35
- Safely exit on broken output pipes (e.g.: usage with `head`, `tail`, ..), see #24
- Backport for rust 1.16, see #23

# v1.0.0

* Respect `.(git)ignore` files
* Use `LS_COLORS` environment variable directly, instead of `~/.dir_colors` file.
* Added unit and integration tests
* Added optional second argument (search path)

# v0.3.0

-  Parse dircolors files, closes #20
-  Colorize each path component, closes #19
-  Add short command line option for --hidden, see #18

# v0.2.0

-  Option to follow symlinks, disable colors, closes #16, closes #17
- `--filename` instead of `--full-path`
-  Option to search hidden directories, closes #12
-  Configurable search depth, closes #13
-  Detect interactive terminal, closes #11

# v0.1.0

Initial release
```

## File: `CONTRIBUTING.md`
```markdown
## Contributing to *fd*

**Thank you very much for considering contributing to this project!**

We welcome any form of contribution:

  * New issues (feature requests, bug reports, questions, ideas, ...)
  * Pull requests (documentation improvements, code improvements, new features, ...)

**Note**: Before you take the time to open a pull request, please open a ticket first. This will
give us the chance to discuss any potential changes first.

## Add an entry to the changelog

If your contribution changes the behavior of `fd` (as opposed to a typo-fix
in the documentation), please update the [`CHANGELOG.md`](CHANGELOG.md#upcoming-release) file
and describe your changes. This makes the release process much easier and
therefore helps to get your changes into a new `fd` release faster.

The top of the `CHANGELOG` contains an *"Upcoming release"* section with a few
subsections (Features, Bugfixes, …). Please add your entry to the subsection
that best describes your change.

Entries follow this format:
```
- Short description of what has been changed, see #123 (@user)
```
Here, `#123` is the number of the original issue and/or your pull request.
Please replace `@user` by your GitHub username.

## Important links

  * [Open issues](https://github.com/sharkdp/fd/issues)
  * [Open pull requests](https://github.com/sharkdp/fd/pulls)
  * [Development section in the README](https://github.com/sharkdp/fd#development)
  * [fd on crates.io](https://crates.io/crates/fd-find)
  * [LICENSE-APACHE](https://github.com/sharkdp/fd/blob/master/LICENSE-APACHE) and [LICENSE-MIT](https://github.com/sharkdp/fd/blob/master/LICENSE-MIT)
```

## File: `Cargo.toml`
```
[package]
authors = ["David Peter <mail@david-peter.de>"]
categories = ["command-line-utilities"]
description = "fd is a simple, fast and user-friendly alternative to find."
exclude = ["/benchmarks/*"]
homepage = "https://github.com/sharkdp/fd"
documentation = "https://docs.rs/fd-find"
keywords = [
    "search",
    "find",
    "file",
    "filesystem",
    "tool",
]
license = "MIT OR Apache-2.0"
name = "fd-find"
readme = "README.md"
repository = "https://github.com/sharkdp/fd"
version = "10.4.2"
edition= "2024"
rust-version = "1.90.0"

[badges.appveyor]
repository = "sharkdp/fd"

[badges.travis-ci]
repository = "sharkdp/fd"

[[bin]]
name = "fd"
path = "src/main.rs"

[dependencies]
aho-corasick = "1.1"
nu-ansi-term = "0.50"
argmax = "0.4.0"
ignore = "0.4.25"
regex = "1.12.2"
regex-syntax = "0.8"
ctrlc = "3.5"
globset = "0.4"
anyhow = "1.0"
etcetera = "0.11"
normpath = "1.1.1"
crossbeam-channel = "0.5.15"
clap_complete = {version = "4.5.62", optional = true}
faccess = "0.2.4"
jiff = "0.2.18"

[dependencies.clap]
version = "4.5.54"
features = ["suggestions", "color", "wrap_help", "cargo", "derive"]

[dependencies.lscolors]
version = "0.21"
default-features = false
features = ["nu-ansi-term"]

[target.'cfg(unix)'.dependencies]
nix = { version = "0.31.1", default-features = false, features = ["signal", "user", "hostname"] }

[target.'cfg(all(unix, not(target_os = "redox")))'.dependencies]
libc = "0.2"

# FIXME: Re-enable jemalloc on macOS
# jemalloc is currently disabled on macOS due to a bug in jemalloc in combination with macOS
# Catalina. See https://github.com/sharkdp/fd/issues/498 for details.
# This has to be kept in sync with src/main.rs where the allocator for
# the program is set.
[target.'cfg(all(not(windows), not(target_os = "android"), not(target_os = "macos"), not(target_os = "freebsd"), not(target_os = "openbsd"), not(target_os = "illumos"), not(all(target_env = "musl", target_pointer_width = "32")), not(target_arch = "riscv64")))'.dependencies]
tikv-jemallocator = {version = "0.6.0", optional = true}

[dev-dependencies]
diff = "0.1"
tempfile = "3.24"
filetime = "0.2"
test-case = "3.3"

[profile.dev]
debug = "line-tables-only"

[profile.dev.package."*"]
debug = false

[profile.debugging]
inherits = "dev"
debug = true

[profile.release]
lto = true
strip = true
codegen-units = 1

[features]
use-jemalloc = ["tikv-jemallocator"]
completions = ["clap_complete"]
base = ["use-jemalloc"]
default = ["use-jemalloc", "completions"]

[package.metadata.binstall]
pkg-url = "{ repo }/releases/download/v{ version }/{ name }-v{ version }-{ target }.{ archive-format }"
bin-dir = "{ bin }-v{ version }-{ target }/{ bin }{ binary-ext }"
pkg-fmt = "tgz"

[package.metadata.binstall.overrides.x86_64-pc-windows-msvc]
pkg-fmt = "zip"

[package.metadata.binstall.overrides.x86_64-pc-windows-gnu]
pkg-fmt = "zip"

[package.metadata.binstall.overrides.i686-pc-windows-msvc]
pkg-fmt = "zip"

[package.metadata.binstall.overrides.aarch64-pc-windows-msvc]
pkg-fmt = "zip"
```

## File: `Cross.toml`
```
# https://github.com/sharkdp/fd/issues/1085
[target.aarch64-unknown-linux-gnu.env]
passthrough = ["JEMALLOC_SYS_WITH_LG_PAGE=16"]

[target.aarch64-unknown-linux-musl.env]
passthrough = ["JEMALLOC_SYS_WITH_LG_PAGE=16"]
```

## File: `LICENSE-APACHE`
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

Copyright 2017-2020 fd developers

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

## File: `LICENSE-MIT`
```
MIT License

Copyright (c) 2017-present The fd developers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `Makefile`
```
PROFILE=release
EXE=target/$(PROFILE)/fd
prefix=/usr/local
bindir=$(prefix)/bin
datadir=$(prefix)/share
exe_name=fd

$(EXE): Cargo.toml src/**/*.rs
	cargo build --profile $(PROFILE) --locked

.PHONY: completions
completions: autocomplete/fd.bash autocomplete/fd.fish autocomplete/_fd.ps1 autocomplete/_fd

comp_dir=@mkdir -p autocomplete

autocomplete/fd.bash: $(EXE)
	$(comp_dir)
	$(EXE) --gen-completions bash > $@

autocomplete/fd.fish: $(EXE)
	$(comp_dir)
	$(EXE) --gen-completions fish > $@

autocomplete/_fd.ps1: $(EXE)
	$(comp_dir)
	$(EXE) --gen-completions powershell > $@

autocomplete/_fd: contrib/completion/_fd
	$(comp_dir)
	cp $< $@

install: $(EXE) completions
	install -Dm755 $(EXE) $(DESTDIR)$(bindir)/fd
	install -Dm644 autocomplete/fd.bash $(DESTDIR)/$(datadir)/bash-completion/completions/$(exe_name)
	install -Dm644 autocomplete/fd.fish $(DESTDIR)/$(datadir)/fish/vendor_completions.d/$(exe_name).fish
	install -Dm644 autocomplete/_fd $(DESTDIR)/$(datadir)/zsh/site-functions/_$(exe_name)
	install -Dm644 doc/fd.1 $(DESTDIR)/$(datadir)/man/man1/$(exe_name).1
```

## File: `README.md`
```markdown
# fd

[![CICD](https://github.com/sharkdp/fd/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/fd/actions/workflows/CICD.yml)
[![Version info](https://img.shields.io/crates/v/fd-find.svg)](https://crates.io/crates/fd-find)
[[中文](https://github.com/cha0ran/fd-zh)]
[[한국어](https://github.com/spearkkk/fd-kor)]

`fd` is a program to find entries in your filesystem.
It is a simple, fast and user-friendly alternative to [`find`](https://www.gnu.org/software/findutils/).
While it does not aim to support all of `find`'s powerful functionality, it provides sensible
(opinionated) defaults for a majority of use cases.

[Installation](#installation) • [How to use](#how-to-use) • [Troubleshooting](#troubleshooting)

## Features

* Intuitive syntax: `fd PATTERN` instead of `find -iname '*PATTERN*'`.
* Regular expression (default) and glob-based patterns.
* [Very fast](#benchmark) due to parallelized directory traversal.
* Uses colors to highlight different file types (same as `ls`).
* Supports [parallel command execution](#command-execution)
* Smart case: the search is case-insensitive by default. It switches to
  case-sensitive if the pattern contains an uppercase
  character[\*](http://vimdoc.sourceforge.net/htmldoc/options.html#'smartcase').
* Ignores hidden directories and files, by default.
* Ignores patterns from your `.gitignore`, by default.
* The command name is *50%* shorter[\*](https://github.com/ggreer/the_silver_searcher) than
  `find` :-).

## Demo

![Demo](doc/screencast.svg)

## How to use

First, to get an overview of all available command line options, you can either run
[`fd -h`](#command-line-options) for a concise help message or `fd --help` for a more detailed
version.

### Simple search

*fd* is designed to find entries in your filesystem. The most basic search you can perform is to
run *fd* with a single argument: the search pattern. For example, assume that you want to find an
old script of yours (the name included `netflix`):
``` bash
> fd netfl
Software/python/imdb-ratings/netflix-details.py
```
If called with just a single argument like this, *fd* searches the current directory recursively
for any entries that *contain* the pattern `netfl`.

### Regular expression search

The search pattern is treated as a regular expression. Here, we search for entries that start
with `x` and end with `rc`:
``` bash
> cd /etc
> fd '^x.*rc$'
X11/xinit/xinitrc
X11/xinit/xserverrc
```

The regular expression syntax used by `fd` is [documented here](https://docs.rs/regex/latest/regex/#syntax).

### Specifying the root directory

If we want to search a specific directory, it can be given as a second argument to *fd*:
``` bash
> fd passwd /etc
/etc/default/passwd
/etc/pam.d/passwd
/etc/passwd
```

### List all files, recursively

*fd* can be called with no arguments. This is very useful to get a quick overview of all entries
in the current directory, recursively (similar to `ls -R`):
``` bash
> cd fd/tests
> fd
testenv
testenv/mod.rs
tests.rs
```

If you want to use this functionality to list all files in a given directory, you have to use
a catch-all pattern such as `.` or `^`:
``` bash
> fd . fd/tests/
testenv
testenv/mod.rs
tests.rs
```

### Searching for a particular file extension

Often, we are interested in all files of a particular type. This can be done with the `-e` (or
`--extension`) option. Here, we search for all Markdown files in the fd repository:
``` bash
> cd fd
> fd -e md
CONTRIBUTING.md
README.md
```

The `-e` option can be used in combination with a search pattern:
``` bash
> fd -e rs mod
src/fshelper/mod.rs
src/lscolors/mod.rs
tests/testenv/mod.rs
```

### Searching for a particular file name

 To find files with exactly the provided search pattern, use the `-g` (or `--glob`) option:
``` bash
> fd -g libc.so /usr
/usr/lib32/libc.so
/usr/lib/libc.so
```

### Hidden and ignored files
By default, *fd* does not search hidden directories and does not show hidden files in the
search results. To disable this behavior, we can use the `-H` (or `--hidden`) option:
``` bash
> fd pre-commit
> fd -H pre-commit
.git/hooks/pre-commit.sample
```

If we work in a directory that is a Git repository (or includes Git repositories), *fd* does not
search folders (and does not show files) that match one of the `.gitignore` patterns. To disable
this behavior, we can use the `-I` (or `--no-ignore`) option:
``` bash
> fd num_cpu
> fd -I num_cpu
target/debug/deps/libnum_cpus-f5ce7ef99006aa05.rlib
```

To really search *all* files and directories, simply combine the hidden and ignore features to show
everything (`-HI`) or use `-u`/`--unrestricted`.

### Matching the full path
By default, *fd* only matches the filename of each file. However, using the `--full-path` or `-p` option,
you can match against the full path.

```bash
> fd -p -g '**/.git/config'
> fd -p '.*/lesson-\d+/[a-z]+.(jpg|png)'
```

### Command execution

Instead of just showing the search results, you often want to *do something* with them. `fd`
provides two ways to execute external commands for each of your search results:

* The `-x`/`--exec` option runs an external command *for each of the search results* (in parallel).
* The `-X`/`--exec-batch` option launches the external command once, with *all search results as arguments*.

#### Examples

Recursively find all zip archives and unpack them:
``` bash
fd -e zip -x unzip
```
If there are two such files, `file1.zip` and `backup/file2.zip`, this would execute
`unzip file1.zip` and `unzip backup/file2.zip`. The two `unzip` processes run in parallel
(if the files are found fast enough).

Find all `*.h` and `*.cpp` files and auto-format them inplace with `clang-format -i`:
``` bash
fd -e h -e cpp -x clang-format -i
```
Note how the `-i` option to `clang-format` can be passed as a separate argument. This is why
we put the `-x` option last.

Any positional arguments after `-x` belong to the command template, not to `fd` itself. If you
also want to pass a pattern or search path, put `-x` last:
``` bash
fd pattern path -x echo
```

Find all `test_*.py` files and open them in your favorite editor:
``` bash
fd -g 'test_*.py' -X vim
```
Note that we use capital `-X` here to open a single `vim` instance. If there are two such files,
`test_basic.py` and `lib/test_advanced.py`, this will run `vim test_basic.py lib/test_advanced.py`.

To see details like file permissions, owners, file sizes etc., you can tell `fd` to show them
by running `ls` for each result:
``` bash
fd … -X ls -lhd --color=always
```
This pattern is so useful that `fd` provides a shortcut. You can use the `-l`/`--list-details`
option to execute `ls` in this way: `fd … -l`.

The `-X` option is also useful when combining `fd` with [ripgrep](https://github.com/BurntSushi/ripgrep/) (`rg`) in order to search within a certain class of files, like all C++ source files:
```bash
fd -e cpp -e cxx -e h -e hpp -X rg 'std::cout'
```

Convert all `*.jpg` files to `*.png` files:
``` bash
fd -e jpg -x convert {} {.}.png
```
Here, `{}` is a placeholder for the search result. `{.}` is the same, without the file extension.
See below for more details on the placeholder syntax.

The terminal output of commands run from parallel threads using `-x` will not be interlaced or garbled,
so `fd -x` can be used to rudimentarily parallelize a task run over many files.
An example of this is calculating the checksum of each individual file within a directory.
```
fd -tf -x md5sum > file_checksums.txt
```

#### Placeholder syntax

The `-x` and `-X` options take a *command template* as a series of arguments (instead of a single string).
If you want to add additional options to `fd` after the command template, you can terminate it with a `\;`.

For example, `fd -x echo \; pattern path` treats `pattern path` as `fd` arguments instead of
passing them to `echo`. In practice, it is often clearer to write `fd pattern path -x echo`.

The syntax for generating commands is similar to that of [GNU Parallel](https://www.gnu.org/software/parallel/):

- `{}`: A placeholder token that will be replaced with the path of the search result
  (`documents/images/party.jpg`).
- `{.}`: Like `{}`, but without the file extension (`documents/images/party`).
- `{/}`: A placeholder that will be replaced by the basename of the search result (`party.jpg`).
- `{//}`: The parent of the discovered path (`documents/images`).
- `{/.}`: The basename, with the extension removed (`party`).

If you do not include a placeholder, *fd* automatically adds a `{}` at the end.

#### Parallel vs. serial execution

For `-x`/`--exec`, you can control the number of parallel jobs by using the `-j`/`--threads` option.
Use `--threads=1` for serial execution.

### Excluding specific files or directories

Sometimes we want to ignore search results from a specific subdirectory. For example, we might
want to search all hidden files and directories (`-H`) but exclude all matches from `.git`
directories. We can use the `-E` (or `--exclude`) option for this. It takes an arbitrary glob
pattern as an argument:
``` bash
> fd -H -E .git …
```

We can also use this to skip mounted directories:
``` bash
> fd -E /mnt/external-drive …
```

.. or to skip certain file types:
``` bash
> fd -E '*.bak' …
```

To make exclude-patterns like these permanent, you can create a `.fdignore` file. They work like
`.gitignore` files, but are specific to `fd`. For example:
``` bash
> cat ~/.fdignore
/mnt/external-drive
*.bak
```

> [!NOTE]
> `fd` also supports `.ignore` files that are used by other programs such as `rg` or `ag`.

If you want `fd` to ignore these patterns globally, you can put them in `fd`'s global ignore file.
This is usually located in `~/.config/fd/ignore` in macOS or Linux, and `%APPDATA%\fd\ignore` in
Windows.

You may wish to include `.git/` in your `fd/ignore` file so that `.git` directories, and their contents
are not included in output if you use the `--hidden` option.

### Deleting files

You can use `fd` to remove all files and directories that are matched by your search pattern.
If you only want to remove files, you can use the `--exec-batch`/`-X` option to call `rm`. For
example, to recursively remove all `.DS_Store` files, run:
``` bash
> fd -H '^\.DS_Store$' -tf -X rm
```
If you are unsure, always call `fd` without `-X rm` first. Alternatively, use `rm`s "interactive"
option:
``` bash
> fd -H '^\.DS_Store$' -tf -X rm -i
```

If you also want to remove a certain class of directories, you can use the same technique. You will
have to use `rm`s `--recursive`/`-r` flag to remove directories.

> [!NOTE]
> There are scenarios where using `fd … -X rm -r` can cause race conditions: if you have a
path like `…/foo/bar/foo/…` and want to remove all directories named `foo`, you can end up in a
situation where the outer `foo` directory is removed first, leading to (harmless) *"'foo/bar/foo':
No such file or directory"* errors in the `rm` call.

### Command-line options

This is the output of `fd -h`. To see the full set of command-line options, use `fd --help` which
also includes a much more detailed help text.

```
Usage: fd [OPTIONS] [pattern [path]...]

Arguments:
  [pattern]  the search pattern (a regular expression, unless '--glob' is used; optional)
  [path]...  the root directories for the filesystem search (optional)

Options:
  -H, --hidden                     Search hidden files and directories
  -I, --no-ignore                  Do not respect .(git|fd)ignore files
  -s, --case-sensitive             Case-sensitive search (default: smart case)
  -i, --ignore-case                Case-insensitive search (default: smart case)
  -g, --glob                       Glob-based search (default: regular expression)
  -a, --absolute-path              Show absolute instead of relative paths
  -l, --list-details               Use a long listing format with file metadata
  -L, --follow                     Follow symbolic links
  -p, --full-path                  Search full abs. path (default: filename only)
  -d, --max-depth <depth>          Set maximum search depth (default: none)
  -E, --exclude <glob>             Exclude entries that match the given glob pattern
  -t, --type <filetype>            Filter by type: file (f), directory (d/dir), symlink (l),
                                   executable (x), empty (e), socket (s), pipe (p), char-device
                                   (c), block-device (b)
  -e, --extension <ext>            Filter by file extension
  -S, --size <size>                Limit results based on the size of files
      --changed-within <date|dur>  Filter by file modification time (newer than)
      --changed-before <date|dur>  Filter by file modification time (older than)
  -o, --owner <user:group>         Filter by owning user and/or group
      --format <fmt>               Print results according to template
  -x, --exec <cmd>...              Execute a command for each search result
  -X, --exec-batch <cmd>...        Execute a command with all search results at once
  -c, --color <when>               When to use colors [default: auto] [possible values: auto,
                                   always, never]
      --hyperlink[=<when>]         Add hyperlinks to output paths [default: never] [possible
                                   values: auto, always, never]
      --ignore-contain <name>      Ignore directories containing the named entry
  -h, --help                       Print help (see more with '--help')
  -V, --version                    Print version
```

Note that options can be given after the pattern and/or path as well.

## Benchmark

Let's search my home folder for files that end in `[0-9].jpg`. It contains ~750.000
subdirectories and about a 4 million files. For averaging and statistical analysis, I'm using
[hyperfine](https://github.com/sharkdp/hyperfine). The following benchmarks are performed
with a "warm"/pre-filled disk-cache (results for a "cold" disk-cache show the same trends).

Let's start with `find`:
```
Benchmark 1: find ~ -iregex '.*[0-9]\.jpg$'
  Time (mean ± σ):     19.922 s ±  0.109 s
  Range (min … max):   19.765 s … 20.065 s
```

`find` is much faster if it does not need to perform a regular-expression search:
```
Benchmark 2: find ~ -iname '*[0-9].jpg'
  Time (mean ± σ):     11.226 s ±  0.104 s
  Range (min … max):   11.119 s … 11.466 s
```

Now let's try the same for `fd`. Note that `fd` performs a regular expression
search by default. The options `-u`/`--unrestricted` option is needed here for
a fair comparison. Otherwise `fd` does not have to traverse hidden folders and
ignored paths (see below):
```
Benchmark 3: fd -u '[0-9]\.jpg$' ~
  Time (mean ± σ):     854.8 ms ±  10.0 ms
  Range (min … max):   839.2 ms … 868.9 ms
```
For this particular example, `fd` is approximately **23 times faster** than `find -iregex`
and about **13 times faster** than `find -iname`. By the way, both tools found the exact
same 546 files :smile:.

**Note**: This is *one particular* benchmark on *one particular* machine. While we have
performed a lot of different tests (and found consistent results), things might
be different for you! We encourage everyone to try it out on their own. See
[this repository](https://github.com/sharkdp/fd-benchmarks) for all necessary scripts.

Concerning *fd*'s speed, a lot of credit goes to the `regex` and `ignore` crates that are
also used in [ripgrep](https://github.com/BurntSushi/ripgrep) (check it out!).

## Troubleshooting

### `fd` does not find my file!

Remember that `fd` ignores hidden directories and files by default. It also ignores patterns
from `.gitignore` files. If you want to make sure to find absolutely every possible file, always
use the options `-u`/`--unrestricted` option (or `-HI` to enable hidden and ignored files):
``` bash
> fd -u …
```

Also remember that by default, `fd` only searches based on the filename and
doesn't compare the pattern to the full path. If you want to search based on the
full path (similar to the `-path` option of `find`) you need to use the `--full-path`
(or `-p`) option.

### Colorized output

`fd` can colorize files by extension, just like `ls`. In order for this to work, the environment
variable [`LS_COLORS`](https://linux.die.net/man/5/dir_colors) has to be set. Typically, the value
of this variable is set by the `dircolors` command which provides a convenient configuration format
to define colors for different file formats.
On most distributions, `LS_COLORS` should be set already. If you are on Windows or if you are looking
for alternative, more complete (or more colorful) variants, see [here](https://github.com/sharkdp/vivid),
[here](https://github.com/seebi/dircolors-solarized) or
[here](https://github.com/trapd00r/LS_COLORS).

`fd` also honors the [`NO_COLOR`](https://no-color.org/) environment variable.

### `fd` doesn't seem to interpret my regex pattern correctly

A lot of special regex characters (like `[]`, `^`, `$`, ..) are also special characters in your
shell. If in doubt, always make sure to put single quotes around the regex pattern:

``` bash
> fd '^[A-Z][0-9]+$'
```

If your pattern starts with a dash, you have to add `--` to signal the end of command line
options. Otherwise, the pattern will be interpreted as a command-line option. Alternatively,
use a character class with a single hyphen character:

``` bash
> fd -- '-pattern'
> fd '[-]pattern'
```

### "Command not found" for `alias`es or shell functions

Shell `alias`es and shell functions can not be used for command execution via `fd -x` or
`fd -X`. In `zsh`, you can make the alias global via `alias -g myalias="…"`. In `bash`,
you can use `export -f my_function` to make available to child processes. You would still
need to call `fd -x bash -c 'my_function "$1"' bash`. For other use cases or shells, use
a (temporary) shell script.

## Integration with other programs

### Using fd with `fzf`

You can use *fd* to generate input for the command-line fuzzy finder [fzf](https://github.com/junegunn/fzf):
``` bash
export FZF_DEFAULT_COMMAND='fd --type file'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
```

Then, you can type `vim <Ctrl-T>` on your terminal to open fzf and search through the fd-results.

Alternatively, you might like to follow symbolic links and include hidden files (but exclude `.git` folders):
``` bash
export FZF_DEFAULT_COMMAND='fd --type file --follow --hidden --exclude .git'
```

You can even use fd's colored output inside fzf by setting:
``` bash
export FZF_DEFAULT_COMMAND="fd --type file --color=always"
export FZF_DEFAULT_OPTS="--ansi"
```

For more details, see the [Tips section](https://github.com/junegunn/fzf#tips) of the fzf README.

### Using fd with `rofi`

[*rofi*](https://github.com/davatorium/rofi) is a graphical launch menu application that is able to create menus by reading from *stdin*. Piping `fd` output into `rofi`s `-dmenu` mode creates fuzzy-searchable lists of files and directories.

#### Example

Create a case-insensitive searchable multi-select list of *PDF* files under your `$HOME` directory and open the selection with your configured PDF viewer. To list all file types, drop the `-e pdf` argument.

``` bash
fd --type f -e pdf . $HOME | rofi -keep-right -dmenu -i -p FILES -multi-select | xargs -I {} xdg-open {}
```

To modify the list that is presented by rofi, add arguments to the `fd` command. To modify the search behaviour of rofi, add arguments to the `rofi` command.

### Using fd with `emacs`

The emacs package [find-file-in-project](https://github.com/technomancy/find-file-in-project) can
use *fd* to find files.

After installing `find-file-in-project`, add the line `(setq ffip-use-rust-fd t)` to your
`~/.emacs` or `~/.emacs.d/init.el` file.

In emacs, run `M-x find-file-in-project-by-selected` to find matching files. Alternatively, run
`M-x find-file-in-project` to list all available files in the project.

### Printing the output as a tree

To format the output of `fd` as a file-tree you can use the `tree` command with
`--fromfile`:
```bash
❯ fd | tree --fromfile
```

This can be more useful than running `tree` by itself because `tree` does not
ignore any files by default, nor does it support as rich a set of options as
`fd` does to control what to print:
```bash
❯ fd --extension rs | tree --fromfile
.
├── build.rs
└── src
    ├── app.rs
    └── error.rs
```

On bash and similar you can simply create an alias:
```bash
❯ alias as-tree='tree --fromfile'
```

### Using fd with `xargs` or `parallel`

Note that `fd` has a builtin feature for [command execution](#command-execution) with
its `-x`/`--exec` and `-X`/`--exec-batch` options. If you prefer, you can still use
it in combination with `xargs`:
``` bash
> fd -0 -e rs | xargs -0 wc -l
```
Here, the `-0` option tells *fd* to separate search results by the NULL character (instead of
newlines). In the same way, the `-0` option of `xargs` tells it to read the input in this way.

## Installation

[![Packaging status](https://repology.org/badge/vertical-allrepos/fd-find.svg)](https://repology.org/project/fd-find/versions)

### On Ubuntu
*... and other Debian-based Linux distributions.*

If you run Ubuntu 19.04 (Disco Dingo) or newer, you can install the
[officially maintained package](https://packages.ubuntu.com/fd-find):
```
apt install fd-find
```
Note that the binary is called `fdfind` as the binary name `fd` is already used by another package.
It is recommended that after installation, you add a link to `fd` by executing command
`ln -s $(which fdfind) ~/.local/bin/fd`, in order to use `fd` in the same way as in this documentation.
Make sure that `$HOME/.local/bin` is in your `$PATH`.

If you use an older version of Ubuntu, you can download the latest `.deb` package from the
[release page](https://github.com/sharkdp/fd/releases) and install it via:
``` bash
dpkg -i fd_9.0.0_amd64.deb # adapt version number and architecture
```

Note that the .deb packages on the release page for this project still name the executable `fd`.

### On Debian

If you run Debian Buster or newer, you can install the
[officially maintained Debian package](https://tracker.debian.org/pkg/rust-fd-find):
```
apt-get install fd-find
```
Note that the binary is called `fdfind` as the binary name `fd` is already used by another package.
It is recommended that after installation, you add a link to `fd` by executing command
`ln -s $(which fdfind) ~/.local/bin/fd`, in order to use `fd` in the same way as in this documentation.
Make sure that `$HOME/.local/bin` is in your `$PATH`.

Note that the .deb packages on the release page for this project still name the executable `fd`.

### On Fedora

Starting with Fedora 28, you can install `fd` from the official package sources:
``` bash
dnf install fd-find
```

### On Alpine Linux

You can install [the fd package](https://pkgs.alpinelinux.org/packages?name=fd)
from the official sources, provided you have the appropriate repository enabled:
```
apk add fd
```

### On Arch Linux

You can install [the fd package](https://www.archlinux.org/packages/extra/x86_64/fd/) from the official repos:
```
pacman -S fd
```
You can also install fd [from the AUR](https://aur.archlinux.org/packages/fd-git).

### On Gentoo Linux

You can use [the fd ebuild](https://packages.gentoo.org/packages/sys-apps/fd) from the official repo:
```
emerge -av fd
```

### On openSUSE Linux

You can install [the fd package](https://software.opensuse.org/package/fd) from the official repo:
```
zypper in fd
```

### On Void Linux

You can install `fd` via xbps-install:
```
xbps-install -S fd
```

### On ALT Linux

You can install [the fd package](https://packages.altlinux.org/en/sisyphus/srpms/fd/) from the official repo:
```
apt-get install fd
```

### On Solus

You can install [the fd package](https://github.com/getsolus/packages/tree/main/packages/f/fd) from the official repo:
```
eopkg install fd
```

### On RedHat Enterprise Linux (RHEL) 8/9/10, Almalinux 8/9/10, EuroLinux 8/9 or Rocky Linux 8/9/10

You can install [the `fd` package](https://copr.fedorainfracloud.org/coprs/tkbcopr/fd/) from Fedora Copr.

```bash
dnf copr enable tkbcopr/fd
dnf install fd
```

A different version using the [slower](https://github.com/sharkdp/fd/pull/481#issuecomment-534494592) malloc [instead of jemalloc](https://bugzilla.redhat.com/show_bug.cgi?id=2216193#c1) is also available from the EPEL8/9 repo as the package `fd-find`.

### On macOS

You can install `fd` with [Homebrew](https://formulae.brew.sh/formula/fd):
```
brew install fd
```

… or with MacPorts:
```
port install fd
```

### On Windows

You can download pre-built binaries from the [release page](https://github.com/sharkdp/fd/releases).

Alternatively, you can install `fd` via [Scoop](http://scoop.sh):
```
scoop install fd
```

Or via [Chocolatey](https://chocolatey.org):
```
choco install fd
```

Or via [Winget](https://learn.microsoft.com/en-us/windows/package-manager/):
```
winget install sharkdp.fd
```

### On GuixOS

You can install [the fd package](https://guix.gnu.org/en/packages/fd-8.1.1/) from the official repo:
```
guix install fd
```

### On Mise

You can use [mise](https://github.com/jdx/mise) to install `fd` with a command like this:
```
mise use -g fd@latest
```

### On NixOS / via Nix

You can use the [Nix package manager](https://nixos.org/nix/) to install `fd`:
```
nix-env -i fd
```

### Via Flox

You can use [Flox](https://flox.dev) to install `fd` into a Flox environment:
```
flox install fd
```

### On FreeBSD

You can install [the fd-find package](https://www.freshports.org/sysutils/fd) from the official repo:
```
pkg install fd-find
```

### From npm

On Linux and macOS, you can install the [fd-find](https://npm.im/fd-find) package:

```
npm install -g fd-find
```

### From source

With Rust's package manager [cargo](https://github.com/rust-lang/cargo), you can install *fd* via:
```
cargo install fd-find
```
Note that rust version *1.77.2* or later is required.

`make` is also needed for the build.

### From binaries

The [release page](https://github.com/sharkdp/fd/releases) includes precompiled binaries for Linux, macOS and Windows. Statically-linked binaries are also available: look for archives with `musl` in the file name.

## Development
```bash
git clone https://github.com/sharkdp/fd

# Build
cd fd
cargo build

# Run unit tests and integration tests
cargo test

# Install
cargo install --path .
```

### Completions

#### From Release Archives

Pre-built completion files are included in the release archives (`.tar.gz`/`.zip`) on the
[Releases page](https://github.com/sharkdp/fd/releases), in the `autocomplete` directory.
To use these completions:

- **bash**: Source the `fd.bash` file in your `~/.bashrc`, or place it in a directory that gets sourced automatically.
- **zsh**: Move `_fd` to a directory in your `fpath` (e.g., `~/.zfunc`).
- **fish**: Copy `fd.fish` to `~/.config/fish/completions/`.
- **powershell**: Source `_fd.ps1` from one of your [profile scripts](https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/creating-profiles?view=powershell-7.5).

#### Generate from fd

You can also generate completions directly using `fd --gen-completions <shell>`:

```bash
# Bash
fd --gen-completions bash > ~/.local/share/bash-completion/completions/fd

# Zsh (ensure ~/.zfunc is in your fpath)
fd --gen-completions zsh > ~/.zfunc/_fd

# Fish
fd --gen-completions fish > ~/.config/fish/completions/fd.fish

# PowerShell
fd --gen-completions powershell >> $PROFILE
```

## Maintainers

- [sharkdp](https://github.com/sharkdp)
- [tmccombs](https://github.com/tmccombs)
- [tavianator](https://github.com/tavianator)

## License

`fd` is distributed under the terms of both the MIT License and the Apache License 2.0.

See the [LICENSE-APACHE](LICENSE-APACHE) and [LICENSE-MIT](LICENSE-MIT) files for license details.
```

## File: `SECURITY.md`
```markdown
# Security Reporting

If you wish to report a security vulnerability privately, we appreciate your diligence. Please follow the guidelines below to submit your report.

## Reporting

To report a security vulnerability, please provide the following information:

1. **PROJECT**
   - Include the URL of the project repository - Example: <https://github.com/sharkdp/fd>

2. **PUBLIC**
   - Indicate whether this vulnerability has already been publicly discussed or disclosed.
   - If so, provide relevant links.

3. **DESCRIPTION**
   - Provide a detailed description of the security vulnerability.
   - Include as much information as possible to help us understand and address the issue.

Send this information, along with any additional relevant details, to our [vulnerability reporting form](https://github.com/sharkdp/fd/security/advisories/new).

## Confidentiality

We kindly ask you to keep the report confidential until a public announcement is made.

## Notes

- Vulnerabilities will be handled on a best-effort basis.
- You may request an advance copy of the patched release, but we cannot guarantee early access before the public release.
- You will be notified via email simultaneously with the public announcement.
- We will respond within a few weeks to confirm whether your report has been accepted or rejected.

Thank you for helping to improve the security of our project!
```

## File: `rustfmt.toml`
```
# Defaults are used
```

## File: `contrib/completion/_fd`
```
#compdef fd

##
# zsh completion function for fd
#
# Based on ripgrep completion function.
# Originally based on code from the zsh-users project — see copyright notice
# below.

autoload -U is-at-least

_fd() {
  local curcontext="$curcontext" no='!' ret=1
  local -a context line state state_descr _arguments_options fd_types fd_args
  local -A opt_args

  if is-at-least 5.2; then
    _arguments_options=( -s -S )
  else
    _arguments_options=( -s )
  fi

  fd_types=(
    {f,file}'\:"regular files"'
    {d,directory}'\:"directories"'
    {l,symlink}'\:"symbolic links"'
    {e,empty}'\:"empty files or directories"'
    {x,executable}'\:"executable (files)"'
    {b,block-device}'\:"block devices"'
    {c,char-device}'\:"character devices"'
    {s,socket}'\:"sockets"'
    {p,pipe}'\:"named pipes (FIFOs)"'
  )

  # Do not complete rare options unless either the current prefix
  # matches one of those options or the user has the `complete-all`
  # style set. Note that this prefix check has to be updated manually to account
  # for all of the potential negation options listed below!
  if
    # (--[bpsu]* => match all options marked with '$no')
    [[ $PREFIX$SUFFIX == --[bopsun]* ]] ||
    zstyle -t ":complete:$curcontext:*" complete-all
  then
    no=
  fi

  # We make heavy use of argument groups here to prevent the option specs from
  # growing unwieldy. These aren't supported in zsh <5.4, though, so we'll strip
  # them out below if necessary. This makes the exclusions inaccurate on those
  # older versions, but oh well — it's not that big a deal
  fd_args=(
    + '(hidden)' # hidden files
    {-H,--hidden}'[search hidden files/directories]'

    + '(no-ignore-full)' # all ignore files
    '(no-ignore-partial)'{-I,--no-ignore}"[don't respect .(git|fd)ignore and global ignore files]"
    $no'(no-ignore-partial)*'{-u,--unrestricted}'[alias for --no-ignore, when repeated also alias for --hidden]'

    + no-ignore-partial # some ignore files
    "(no-ignore-full --no-ignore-vcs)--no-ignore-vcs[don't respect .gitignore files]"
    "!(no-ignore-full --no-global-ignore-file)--no-global-ignore-file[don't respect the global ignore file]"
    $no'(no-ignore-full --no-ignore-parent)--no-ignore-parent[]'

    + '(case)' # case-sensitivity
    {-s,--case-sensitive}'[perform a case-sensitive search]'
    {-i,--ignore-case}'[perform a case-insensitive search]'

    + '(regex-pattern)' # regex-based search pattern
    '(no-regex-pattern)--regex[perform a regex-based search (default)]'

    + '(no-regex-pattern)' # non-regex-based search pattern
    {-g,--glob}'[perform a glob-based search]'
    {-F,--fixed-strings}'[treat pattern as literal string instead of a regex]'

    + '(no-require-git)'
    "$no(no-ignore-full --no-ignore-vcs --no-require-git)--no-require-git[don't require git repo to respect gitignores]"

    + '(match-full)' # match against full path
    {-p,--full-path}'[match the pattern against the full path instead of the basename]'

    + '(follow)' # follow symlinks
    {-L,--follow}'[follow symbolic links to directories]'

    + '(abs-path)' # show absolute paths
    '(long-listing)'{-a,--absolute-path}'[show absolute paths instead of relative paths]'

    + '(null-sep)' # use null separator for output
    '(long-listing)'{-0,--print0}'[separate search results by the null character]'

    + '(long-listing)' # long-listing output
    '(abs-path null-sep max-results exec-cmds)'{-l,--list-details}'[use a long listing format with file metadata]'

    + '(max-results)' # max number of results
    '(long-listing exec-cmds)--max-results=[limit number of search results to given count and quit]:count'
    '(long-listing exec-cmds)-1[limit to a single search result and quit]'

    + '(fs-errors)' # file-system errors
    $no'--show-errors[enable the display of filesystem errors]'

    + '(fs-traversal)' # file-system traversal
    $no"--one-file-system[don't descend into directories on other file systems]"
    '!--mount'
    '!--xdev'

    + dir-depth # directory depth
    '(--exact-depth -d --max-depth)'{-d+,--max-depth=}'[set max directory depth to descend when searching]:depth'
    '!(--exact-depth -d --max-depth)--maxdepth:depth'
    '(--exact-depth --min-depth)--min-depth=[set directory depth to descend before start searching]:depth'
    '(--exact-depth -d --max-depth --maxdepth --min-depth)--exact-depth=[only search at the exact given directory depth]:depth'

    + prune # pruning
    "--prune[don't traverse into matching directories]"

    + filter-misc # filter search
    '*'{-t+,--type=}"[filter search by type]:type:(($fd_types))"
    '*'{-e+,--extension=}'[filter search by file extension]:extension'
    '*'{-E+,--exclude=}'[exclude files/directories that match the given glob pattern]:glob pattern'
    '*'{-S+,--size=}'[limit search by file size]:size limit:->size'
    '(-o --owner)'{-o+,--owner=}'[filter by owning user and/or group]:owner and/or group:->owner'

    + ignore-file # extra ignore files
    '*--ignore-file=[add a custom, low-precedence ignore-file with .gitignore format]: :_files'

    + '(filter-mtime-newer)' # filter by files modified after than
    '--changed-within=[limit search to files/directories modified within the given date/duration]:date or duration'
    '--changed-after=[alias for --changed-within]:date/duration'
    '!--change-newer-than=:date/duration'
    '!--newer=:date/duration'

    + '(filter-mtime-older)' # filter by files modified before than
    '--changed-before=[limit search to files/directories modified before the given date/duration]:date or duration'
    '!--change-older-than=:date/duration'
    '!--older=:date/duration'

    + '(color)' # colorize output
    {-c+,--color=}'[declare when to colorize search results]:when to colorize:((
      auto\:"show colors if the output goes to an interactive console (default)"
      never\:"do not use colorized output"
      always\:"always use colorized output"
    ))'

    '--hyperlink=-[add hyperlinks to output paths]::when:(auto never always)'

    + '(threads)'
    {-j+,--threads=}'[set the number of threads for searching and executing]:number of threads'

    + '(exec-cmds)' # execute command
    '(long-listing max-results)'{-x+,--exec=}'[execute command for each search result]:command: _command_names -e:*\;::program arguments: _normal'
    '(long-listing max-results)'{-X+,--exec-batch=}'[execute command for all search results at once]:command: _command_names -e:*\;::program arguments: _normal'
    '(long-listing max-results)--batch-size=[max number of args for each -X call]:size'

    + other
    '!(--max-buffer-time)--max-buffer-time=[set amount of time to buffer before showing output]:time (ms)'

    + '(about)' # about flags
    '(: * -)'{-h,--help}'[display help message]'
    '(: * -)'{-V,--version}'[display version information]'

    + path-sep # set path separator for output
    $no'(--path-separator)--path-separator=[set the path separator to use when printing file paths]:path separator'

    + search-path
    $no'(--base-directory)--base-directory=[change the current working directory to the given path]:directory:_files -/'
    $no'(*)*--search-path=[set search path (instead of positional <path> arguments)]:directory:_files -/'

    + strip-cwd-prefix
    $no'(strip-cwd-prefix exec-cmds)--strip-cwd-prefix=-[When to strip ./]::when:(always never auto)'

    + and
    '--and=[additional required search path]:pattern'


    + args # positional arguments
    '1: :_guard "^-*" pattern'
    '(--search-path)*:directory:_files -/'
  )

  # Strip out argument groups where unsupported (see above)
  is-at-least 5.4 ||
  fd_args=( ${(@)args:#(#i)(+|[a-z0-9][a-z0-9_-]#|\([a-z0-9][a-z0-9_-]#\))} )

  _arguments $_arguments_options : $fd_args && ret=0

  case ${state} in
    owner)
      compset -P '(\\|)\!'
      if compset -P '*:'; then
        _groups && ret=0
      else
        if
          compset -S ':*' ||
          # Do not add the colon suffix when completing "!user<TAB>
          # (with a starting double-quote) otherwise pressing tab again
          # after the inserted colon "!user:<TAB> will complete history modifiers
          [[ $IPREFIX == (\\|\!)*  && ($QIPREFIX == \"* && -z $QISUFFIX) ]]
        then
          _users && ret=0
        else
          local q
          # Since quotes are needed when using the negation prefix !,
          # automatically remove the colon suffix also when closing the quote
          if [[ $QIPREFIX == [\'\"]* ]]; then
            q=${QIPREFIX:0:1}
          fi
          _users -r ": \t\n\-$q" -S : && ret=0
        fi
      fi
      ;;

    size)
      if compset -P '[-+][0-9]##'; then
        local -a suff=(
          'B:bytes'
          'K:kilobytes  (10^3  = 1000   bytes)'
          'M:megabytes  (10^6  = 1000^2 bytes)'
          'G:gigabytes  (10^9  = 1000^3 bytes)'
          'T:terabytes  (10^12 = 1000^4 bytes)'
          'Ki:kibibytes  ( 2^10 = 1024   bytes)'
          'Mi:mebibytes  ( 2^20 = 1024^2 bytes)'
          'Gi:gigibytes  ( 2^30 = 1024^3 bytes)'
          'Ti:tebibytes  ( 2^40 = 1024^4 bytes)'
        )
        _describe -t units 'size limit units' suff -V 'units'
      elif compset -P '[-+]'; then
        _message -e 'size limit number (full format: <+-><number><unit>)'
      else
        _values 'size limit prefix (full format: <prefix><number><unit>)' \
          '\+[file size must be greater or equal to]'\
          '-[file size must be less than or equal to]' && ret=0
      fi
      ;;
  esac

  return ret
}

_fd "$@"

# ------------------------------------------------------------------------------
# Copyright (c) 2011 GitHub zsh-users - http://github.com/zsh-users
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the zsh-users nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL ZSH-USERS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ------------------------------------------------------------------------------
# Description
# -----------
#
#  Completion script for fd
#
# ------------------------------------------------------------------------------
# Authors
# -------
#
#  * smancill (https://github.com/smancill)
#
# ------------------------------------------------------------------------------

# Local Variables:
# mode: shell-script
# coding: utf-8-unix
# indent-tabs-mode: nil
# sh-indentation: 2
# sh-basic-offset: 2
# End:
# vim: ft=zsh sw=2 ts=2 et
```

## File: `doc/.gitattributes`
```
* linguist-vendored
```

## File: `doc/fd.1`
```
.TH FD 1
.SH NAME
fd \- find entries in the filesystem
.SH SYNOPSIS
.B fd
.RB [ \-HIEsiaLp0hV ]
.RB [ \-d
.IR depth ]
.RB [ \-t
.IR filetype ]
.RB [ \-e
.IR ext ]
.RB [ \-E
.IR exclude ]
.RB [ \-c
.IR when ]
.RB [ \-j
.IR num ]
.RB [ \-x
.IR cmd ]
.RI [ pattern
.RI [ path... ]]
.SH DESCRIPTION
.B fd
is a simple, fast and user-friendly alternative to
.BR find (1).
.P
By default
.B fd
uses regular expressions for the pattern. However, this can be changed to use simple glob patterns
with the '\-\-glob' option.
.P
By default
.B fd
will exclude hidden files and directories, as well as any files that match gitignore rules
or ignore rules in .ignore or .fdignore files.
.P
If you wish to search all files in a specific directory, you can use '' or . as the search pattern,
to match all files. Or you can use the '\-\-search\-path' option to specify the path(s) instead of
the positional parameter.
.P
Options may be given anywhere on the command line.
.SH OPTIONS
.TP
.B \-H, \-\-hidden
Include hidden files and directories in the search results
(default: hidden files and directories are skipped). The flag can be overridden with '--no-hidden'.
.IP
Ignored files are still excluded unless \-\-no\-ignore or \-\-no\-ignore\-vcs
is also used.
.TP
.B \-I, \-\-no\-ignore
Show search results from files and directories that would otherwise be ignored by
.RS
.IP \[bu] 2
.I .gitignore
.IP \[bu]
.I .git/info/exclude
.IP \[bu]
The global gitignore configuration (by default
.IR $HOME/.config/git/ignore )
.IP \[bu]
.I .ignore
.IP \[bu]
.I .fdignore
.IP \[bu]
The global fd ignore file (usually
.I $HOME/.config/fd/ignore
)
.RE
.IP
The flag can be overridden with '--ignore'.
.TP
.B \-u, \-\-unrestricted
Perform an unrestricted search, including ignored and hidden files. This is an alias for '--hidden --no-ignore'.
.TP
.B \-\-no\-ignore\-vcs
Show search results from files and directories that would otherwise be ignored by gitignore files
including
.IR  .gitignore ,
.IR  .git/info/exclude ,
and the global gitignore configuration
.RI ( core.excludesFile
git setting, which defaults to
.IR $HOME/.config/git/ignore ).
The flag can be overridden with '--ignore-vcs'.
.TP
.B \-\-no\-require\-git
Do not require a git repository to respect gitignores. By default, fd will only
respect global gitignore rules, .gitignore rules and local exclude rules if fd
detects that you are searching inside a git repository. This flag allows you to
relax this restriction such that fd will respect all git related ignore rules
regardless of whether you’re searching in a git repository or not. The flag can
be overridden with '--require-git'.
.TP
.B \-\-no\-ignore\-parent
Show search results from files and directories that would otherwise be ignored by gitignore files in
parent directories.
.TP
.B \-s, \-\-case\-sensitive
Perform a case-sensitive search. By default, fd uses case-insensitive searches, unless the
pattern contains an uppercase character (smart case).
.TP
.B \-i, \-\-ignore\-case
Perform a case-insensitive search. By default, fd uses case-insensitive searches, unless the
pattern contains an uppercase character (smart case).
.TP
.B \-g, \-\-glob
Perform a glob-based search instead of a regular expression search.
If combined with the '\-\-full-path' option, '**' can be used to match multiple path components.
.TP
.B \-\-regex
Perform a regular-expression based search (default). This can be used to override --glob.
.TP
.B \-F, \-\-fixed\-strings
Treat the pattern as a literal string instead of a regular expression. Note that this also
performs substring comparison. If you want to match on an exact filename, consider using '\-\-glob'.
.TP
.BI "\-\-and " pattern
Add additional required search patterns, all of which must be matched. Multiple additional
patterns can be specified. The patterns are regular expressions, unless '\-\-glob'
or '\-\-fixed\-strings' is used.
.TP
.B \-a, \-\-absolute\-path
Shows the full path starting from the root as opposed to relative paths.
The flag can be overridden with '--relative-path'.
.TP
.B \-l, \-\-list\-details
Use a detailed listing format like 'ls -l'. This is basically an alias
for '--exec-batch ls -l' with some additional 'ls' options. This can be used
to see more metadata, to show symlink targets and to achieve a deterministic
sort order.
.TP
.B \-L, \-\-follow
By default, fd does not descend into symlinked directories. Using this flag, symbolic links are
also traversed. The flag can be overridden with '--no-follow'.
.TP
.B \-p, \-\-full\-path
By default, the search pattern is only matched against the filename (or directory name). Using
this flag, the
.I pattern
is matched against the full path.
.TP
.B \-0, \-\-print0
Separate search results by the null character (instead of newlines). Useful for piping results to
.IR xargs .
.TP
.B \-\-max\-results count
Limit the number of search results to 'count' and quit immediately.
.TP
.B \-1
Limit the search to a single result and quit immediately. This is an alias for '--max-results=1'.
.TP
.B \-q, \-\-quiet
When the flag is present, the program does not print anything and will instead exit with a code of 0 if there is at least one search result.
Otherwise, the exit code will be 1.
This is mainly for usage in scripts and can be faster than checking for output because the search can be stopped early after the first match.
.B \-\-has\-results
can be used as an alias.
.TP
.B \-\-show-errors
Enable the display of filesystem errors for situations such as insufficient
permissions or dead symlinks.
.TP
.B \-\-strip-cwd-prefix [when]
By default, relative paths are prefixed with './' when -x/--exec,
-X/--exec-batch, or -0/--print0 are given, to reduce the risk of a
path starting with '-' being treated as a command line option. Use
this flag to change this behavior. If this flag is used without a value,
it is equivalent to passing "always". Possible values are:
.RS
.IP never
Never strip the ./ at the beginning of paths
.IP always
Always strip the ./ at the beginning of paths
.IP auto
Only strip if used with --exec, --exec-batch, or --print0. That is, it resets to the default behavior.
.RE
.TP
.B \-\-one\-file\-system, \-\-mount, \-\-xdev
By default, fd will traverse the file system tree as far as other options dictate. With this flag, fd ensures that it does not descend into a different file system than the one it started in. Comparable to the -mount or -xdev filters of find(1).
.TP
.B \-h, \-\-help
Print help information.
.TP
.B \-V, \-\-version
Print version information.
.TP
.BI "\-d, \-\-max\-depth " d
Limit directory traversal to at most
.I d
levels of depth. By default, there is no limit on the search depth.
.TP
.BI "\-\-min\-depth " d
Only show search results starting at the given depth. See also: '--max-depth' and '--exact-depth'.
.TP
.BI "\-\-exact\-depth " d
Only show search results at the exact given depth. This is an alias for '--min-depth <depth> --max-depth <depth>'.
.TP
.B \-\-prune
Do not traverse into matching directories.
.TP
.BI "\-t, \-\-type " filetype
Filter search by type:
.RS
.IP "f, file"
regular files
.IP "d, dir, directory"
directories
.IP "l, symlink"
symbolic links
.IP "b, block-device"
block devices
.IP "c, char-device"
character devices
.IP "s, socket"
sockets
.IP "p, pipe"
named pipes (FIFOs)
.IP "x, executable"
executable (files)
.IP "e, empty"
empty files or directories
.RE

.RS
This option can be specified more than once to include multiple file types.
Searching for '--type file --type symlink' will show both regular files as well as
symlinks. Note that the 'executable' and 'empty' filters work differently: '--type
executable' implies '--type file' by default. And '--type empty' searches for
empty files and directories, unless either '--type file' or '--type directory' is
specified in addition.

Examples:
  - Only search for files:
      fd --type file …
      fd -tf …
  - Find both files and symlinks
      fd --type file --type symlink …
      fd -tf -tl …
  - Find executable files:
      fd --type executable
      fd -tx
  - Find empty files:
      fd --type empty --type file
      fd -te -tf
  - Find empty directories:
      fd --type empty --type directory
      fd -te -td
.RE
.TP
.BI "\-e, \-\-extension " ext
Filter search results by file extension
.IR ext .
This option can be used repeatedly to allow for multiple possible file extensions.

If you want to search for files without extension, you can use the regex '^[^.]+$'
as a normal search pattern.
.TP
.BI "\-E, \-\-exclude " glob
Exclude files/directories that match the given glob pattern.
This overrides any other ignore logic.
Multiple exclude patterns can be specified.
Examples:
  \-\-exclude '*.pyc'
  \-\-exclude node_modules
.TP
.BI "\-\-ignore-contain " name
Exclude directories that (directly) contain the given name.
This option can be specified multiple times.
.TP
.BI "\-\-ignore-file " path
Add a custom ignore-file in '.gitignore' format.
These files have a low precedence.
.TP
.BI "\-c, \-\-color " when
Declare
.I when
to colorize search results:
.RS
.IP auto
Colorize output when standard output is connected to terminal (default).
.IP never
Do not colorize output.
.IP always
Always colorize output.
.RE
.TP
.B "\-\-hyperlink
Specify whether the output should use terminal escape codes to indicate a hyperlink to a
file url pointing to the path.

The value can be auto, always, or never.

Currently, the default is "never", and if the option is used without an argument "auto" is
used. In the future this may be changed to "auto" and "always".
.RS
.IP auto
Only output hyperlinks if color is also enabled, as a proxy for whether terminal escape
codes are acceptable.
.IP never
Never output hyperlink escapes.
.IP always
Always output hyperlink escapes, regardless of color settings.
.RE
.TP
.BI "\-j, \-\-threads " num
Set number of threads to use for searching & executing (default: number of available CPU cores).
.TP
.BI "\-S, \-\-size " size
Limit results based on the size of files using the format
.I <+-><NUM><UNIT>
.RS
.IP '+'
file size must be greater than or equal to this
.IP '-'
file size must be less than or equal to this
.P
If neither '+' nor '-' is specified, file size must be exactly equal to this.
.IP 'NUM'
The numeric size (e.g. 500)
.IP 'UNIT'
The units for NUM. They are not case-sensitive.
Allowed unit values:
.RS
.IP 'b'
bytes
.IP 'k'
kilobytes (base ten, 10^3 = 1000 bytes)
.IP 'm'
megabytes
.IP 'g'
gigabytes
.IP 't'
terabytes
.IP 'ki'
kibibytes (base two, 2^10 = 1024 bytes)
.IP 'mi'
mebibytes
.IP 'gi'
gibibytes
.IP 'ti'
tebibytes
.RE
.RE
.TP
.BI "\-\-changed-within " date|duration
Filter results based on the file modification time.
Files with modification timestamps greater than the argument will be returned.
The argument can be provided as a duration (\fI10h, 1d, 35min\fR) or as a specific point
in time as full RFC3339 format with time zone, as a date or datetime in the
local time zone (\fIYYYY-MM-DD\fR or \fIYYYY-MM-DD HH:MM:SS\fR), or as the prefix '@'
followed by the number of seconds since the Unix epoch (@[0-9]+).
\fB\-\-change-newer-than\fR,
.B --newer
or
.B --changed-after
can be used as aliases.

Examples:
  \-\-changed-within 2weeks
  \-\-change-newer-than "2018-10-27 10:00:00"
  \-\-newer 2018-10-27
  \-\-changed-after @1704067200
.TP
.BI "\-\-changed-before " date|duration
Filter results based on the file modification time.
Files with modification timestamps less than the argument will be returned.
The argument can be provided as a duration (\fI10h, 1d, 35min\fR) or as a specific point
in time as full RFC3339 format with time zone, as a date or datetime in the
local time zone (\fIYYYY-MM-DD\fR or \fIYYYY-MM-DD HH:MM:SS\fR), or as the prefix '@'
followed by the number of seconds since the Unix epoch (@[0-9]+).
.B --change-older-than
or
.B --older
can be used as aliases.

Examples:
  \-\-changed-before "2018-10-27 10:00:00"
  \-\-change-older-than 2weeks
  \-\-older @1704067200
.TP
.BI "-o, \-\-owner " [user][:group]
Filter files by their user and/or group. Format: [(user|uid)][:(group|gid)]. Either side
is optional. Precede either side with a '!' to exclude files instead.

Examples:
  \-\-owner john
  \-\-owner :students
  \-\-owner "!john:students"
.TP
.BI "-C, \-\-base\-directory " path
Change the current working directory of fd to the provided path. This means that search results will
be shown with respect to the given base path. Note that relative paths which are passed to fd via the
positional \fIpath\fR argument or the \fB\-\-search\-path\fR option will also be resolved relative to
this directory.
.TP
.BI "\-\-path\-separator " separator
Set the path separator to use when printing file paths. The default is the OS-specific separator
('/' on Unix, '\\' on Windows).
.TP
.BI "\-\-search\-path " search\-path
Provide paths to search as an alternative to the positional \fIpath\fR argument. Changes the usage to
\'fd [FLAGS/OPTIONS] \-\-search\-path PATH \-\-search\-path PATH2 [PATTERN]\'
.TP
.BI "\-\-format " fmt
Specify a template string that is used for printing a line for each file found.

The following placeholders are substituted into the string for each file before printing:
.RS
.IP {}
path (of the current search result)
.IP {/}
basename
.IP {//}
parent directory
.IP {.}
path without file extension
.IP {/.}
basename without file extension
.IP {{
literal '{' (an escape sequence)
.IP }}
literal '}' (an escape sequence)
.P
Notice that you can use "{{" and "}}" to escape "{" and "}" respectively, which is especially
useful if you need to include the literal text of one of the above placeholders.
.RE
.TP
.BI "\-x, \-\-exec " command
.RS
Execute
.I command
for each search result in parallel (use --threads=1 for sequential command execution).

Note that all subsequent positional arguments are considered to be arguments to the
.I command
- not to fd.
It is therefore recommended to place the \-x/\-\-exec option last. Alternatively, you can supply
a ';' argument to end the argument list and continue with more fd options.
Most shells require ';' to be escaped: '\\;'.
This option can be specified multiple times, in which case all commands are run for each
file found, in the order they are provided. In that case, you must supply a ';' argument for
all but the last commands.

If parallelism is enabled, the order commands will be executed in is non-deterministic. And even with
--threads=1, the order is determined by the operating system and may not be what you expect. Thus, it is
recommended that you don't rely on any ordering of the results.

Before executing the command, any placeholder patterns in the command are replaced with the
corresponding values for the current file. The same placeholders are used as in the "\-\-format"
option.

If no placeholder is present, an implicit "{}" at the end is assumed.

If --print0 is also given, then a null character (\\0) will be printed between the output for each found entry.
This allows another program to easily distinguish the output for each file if the command(s) produce multiple lines.

Examples:

  - find all *.zip files and unzip them:

        fd -e zip -x unzip

  - find *.h and *.cpp files and run "clang-format -i .." for each of them:

        fd -e h -e cpp -x clang-format -i

  - Convert all *.jpg files to *.png files:

        fd -e jpg -x convert {} {.}.png

  - Run stat for each *.txt file, separated by null characters

        fd -0 -e txt -x stat
.RE
.TP
.BI "\-X, \-\-exec-batch " command
.RS
Execute
.I command
once, with all search results as arguments.

The order of the arguments is non-deterministic and should not be relied upon.

This uses the same placeholders as "\-\-format" and "\-\-exec", but instead of expanding
once per command invocation each argument containing a placeholder is expanding for every
file in a batch and passed as separate arguments.

If no placeholder is present, an implicit "{}" at the end is assumed.

Like \-\-exec, subsequent arguments are assumed to be part of
.I command
until either the end of command arguments or a ';' argument. See above.

Like \-\-exec, this can be used multiple times, in which case each command will be run in
the order given.

Examples:

  - Find all test_*.py files and open them in your favorite editor:

        fd -g 'test_*.py' -X vim

    Note that this executes a single "vim" process with all search results as arguments.

  - Find all *.rs files and count the lines with "wc -l ...":

        fd -e rs -X wc -l
.RE
.TP
.BI "\-\-batch-size " size
Maximum number of arguments to pass to the command given with -X. If the number of results is
greater than the given size, the command given with -X is run again with remaining arguments. A
batch size of zero means there is no limit (default), but note that batching might still happen
due to OS restrictions on the maximum length of command lines.
.SH PATTERN SYNTAX
The regular expression syntax used by fd is documented here:

    https://docs.rs/regex/1.0.0/regex/#syntax

The glob syntax is documented here:

    https://docs.rs/globset/#syntax
.SH ENVIRONMENT
.TP
.B LS_COLORS
Determines how to colorize search results, see
.BR dircolors (1) .
.TP
.B NO_COLOR
Disables colorized output.
.TP
.B XDG_CONFIG_HOME, HOME
Used to locate the global ignore file. If
.B XDG_CONFIG_HOME
is set, use
.IR $XDG_CONFIG_HOME/fd/ignore .
Otherwise, use
.IR $HOME/.config/fd/ignore .
.SH FILES
.TP
.B .fdignore
This file works similarly to a .gitignore file anywhere in the searched tree and specifies patterns
that should be excluded from the search. However, this file is specific to fd, and will be used even
if the --no-ignore-vcs option is used.
.TP
.B $XDG_CONFIG_HOME/fd/ignore
Global ignore file. Unless ignore mode is turned off (such as with --no-ignore)
ignore entries in this file will be ignored, as if it was an .fdignore file in the
current directory.
.SH EXAMPLES
.TP
.RI "Find files and directories that match the pattern '" needle "':"
$ fd needle
.TP
.RI "Start a search in a given directory (" /var/log "):"
$ fd nginx /var/log
.TP
.RI "Find all Python files (all files with the extension " .py ") in the current directory:"
$ fd -e py
.TP
.RI "Open all search results with vim:"
$ fd pattern -X vim
.SH Tips and Tricks
.IP \[bu]
If you add ".git/" to your global ignore file ($XDG_CONFIG_HOME/fd/ignore), then
".git" folders will be ignored by default, even when the --hidden option is used.
.IP \[bu]
You can use a shell alias or a wrapper script in order to pass desired flags to fd
by default. For example if you do not like the default behavior of respecting gitignore,
you can use
`alias fd="/usr/bin/fd --no-ignore-vcs"`
in your .bashrc to create an alias for fd that doesn't ignore git files by default.
.SH BUGS
Bugs can be reported on GitHub: https://github.com/sharkdp/fd/issues
.SH SEE ALSO
.BR find (1)
```

## File: `doc/release-checklist.md`
```markdown
# Release checklist

This file can be used as-is, or copied into the GitHub PR description which includes
necessary changes for the upcoming release.

## Version bump

- [ ] Create a new branch for the required changes for this release.
- [ ] Update version in `Cargo.toml`. Run `cargo build` to update `Cargo.lock`.
      Make sure to `git add` the `Cargo.lock` changes as well.
- [ ] Find the current min. supported Rust version by running
      `grep rust-version Cargo.toml`.
- [ ] Update the `fd` version and the min. supported Rust version in `README.md`.
- [ ] Update `CHANGELOG.md`. Change the heading of the *"Upcoming release"* section
      to the version of this release.

## Pre-release checks and updates

- [ ] Install the latest version (`cargo install --locked -f --path .`) and make
      sure that it is available on the `PATH` (`fd --version` should show the
      new version).
- [ ] Review `-h`, `--help`, and the `man` page.
- [ ] Run `fd -h` and copy the output to the *"Command-line options"* section in
      the README
- [ ] Push all changes and wait for CI to succeed (before continuing with the
      next section).
- [ ] Optional: manually test the new features and command-line options described
      in the `CHANGELOG.md`.
- [ ] Run `cargo publish --dry-run` to make sure that it will succeed later
      (after creating the GitHub release).

## Release

- [ ] Merge your release branch (should be a fast-forward merge).
- [ ] Create a tag and push it: `git tag vX.Y.Z; git push origin tag vX.Y.Z`.
      This will trigger the deployment via GitHub Actions.
      REMINDER: If your `origin` is a fork, don't forget to push to e.g. `upstream`
      instead.
- [ ] Go to https://github.com/sharkdp/fd/releases/new to create the new
      release. Select the new tag and also use it as the release title. For the
      release notes, copy the corresponding section from `CHANGELOG.md` and
      possibly add additional remarks for package maintainers.
      Publish the release.
- [ ] Check if the binary deployment works (archives and Debian packages should
      appear when the CI run *for the Git tag* has finished).
- [ ] Publish to crates.io by running `cargo publish` in a *clean* repository.
      One way to do this is to clone a fresh copy.

## Post-release

- [ ] Prepare a new *"Upcoming release"* section at the top of `CHANGELOG.md`.
      Put this at the top:

      # Upcoming release

      ## Features


      ## Bugfixes


      ## Changes


      ## Other

```

## File: `doc/screencast.sh`
```bash
#!/bin/bash
# Designed to be executed via svg-term from the fd root directory:
# svg-term --command="bash doc/screencast.sh" --out doc/screencast.svg --padding=10
# Then run this (workaround for #1003):
# sed -i '' 's/<text/<text font-size="1.67"/g' doc/screencast.svg
set -e
set -u

PROMPT="▶"

enter() {
    INPUT=$1
    DELAY=1

    prompt
    sleep "$DELAY"
    type "$INPUT"
    sleep 0.5
    printf '%b' "\\n"
    eval "$INPUT"
    type "\\n"
}

prompt() {
    printf '%b ' "$PROMPT" | pv -q
}

type() {
    printf '%b' "$1" | pv -qL $((10+(-2 + RANDOM%5)))
}

main() {
    IFS='%'

    enter "fd"

    enter "fd app"

    enter "fd fi"

    enter "fd fi --type f"

    enter "fd --type d"

    enter "fd -e md"

    enter "fd -e md --exec wc -l"

    enter "fd '^[A-Z]'"

    enter "fd --exclude src"

    enter "fd --hidden sample"

    prompt

    sleep 3

    echo ""

    unset IFS
}

main
```

## File: `doc/sponsors.md`
```markdown
## Sponsors

`fd` development is sponsored by many individuals and companies. Thank you very much!

Please note, that being sponsored does not affect the individuality of the `fd`
project or affect the maintainers' actions in any way.
We remain impartial and continue to assess pull requests solely on merit - the
features added, bugs solved, and effect on the overall complexity of the code.
No issue will have a different priority based on sponsorship status of the
reporter.

Contributions from anybody are most welcomed, please see our [`CONTRIBUTING.md`](../bmad_repo/CONTRIBUTING.md) guide.
```

## File: `scripts/create-deb.sh`
```bash
#!/bin/bash
COPYRIGHT_YEARS="2018 - "$(date "+%Y")
MAINTAINER="David Peter <mail@david-peter.de>"
REPO="https://github.com/sharkdp/fd"
DPKG_STAGING="${CICD_INTERMEDIATES_DIR:-.}/debian-package"
DPKG_DIR="${DPKG_STAGING}/dpkg"
mkdir -p "${DPKG_DIR}"

if [[ -z "$TARGET" ]]; then
  TARGET="$(rustc -vV | sed -n 's|host: \(.*\)|\1|p')"
fi

case "$TARGET" in
  *-musl*)
    DPKG_BASENAME=fd-musl
    DPKG_CONFLICTS="fd, fd-find"
    ;;
  *)
    DPKG_BASENAME=fd
    DPKG_CONFLICTS="fd-musl, fd-find"
    ;;
esac

if [[ -z "$DPKG_VERSION" ]]; then
  DPKG_VERSION=$(cargo metadata --no-deps --format-version 1 | jq -r .packages[0].version)
fi

unset DPKG_ARCH
case "${TARGET}" in
  aarch64-*-linux-*) DPKG_ARCH=arm64 ;;
  arm-*-linux-*hf) DPKG_ARCH=armhf ;;
  i686-*-linux-*) DPKG_ARCH=i686 ;;
  x86_64-*-linux-*) DPKG_ARCH=amd64 ;;
  *) DPKG_ARCH=notset ;;
esac;

DPKG_NAME="${DPKG_BASENAME}_${DPKG_VERSION}_${DPKG_ARCH}.deb"

BIN_PATH=${BIN_PATH:-target/${TARGET}/release/fd}

# Binary
install -Dm755 "${BIN_PATH}" "${DPKG_DIR}/usr/bin/fd"

# Man page
install -Dm644 'doc/fd.1' "${DPKG_DIR}/usr/share/man/man1/fd.1"
gzip -n --best "${DPKG_DIR}/usr/share/man/man1/fd.1"

# Autocompletion files
install -Dm644 'autocomplete/fd.bash' "${DPKG_DIR}/usr/share/bash-completion/completions/fd"
install -Dm644 'autocomplete/fd.fish' "${DPKG_DIR}/usr/share/fish/vendor_completions.d/fd.fish"
install -Dm644 'autocomplete/_fd' "${DPKG_DIR}/usr/share/zsh/vendor-completions/_fd"

# README and LICENSE
install -Dm644 "README.md" "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/README.md"
install -Dm644 "LICENSE-MIT" "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/LICENSE-MIT"
install -Dm644 "LICENSE-APACHE" "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/LICENSE-APACHE"
install -Dm644 "CHANGELOG.md" "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/changelog"
gzip -n --best "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/changelog"

# Create symlinks so fdfind can be used as well:
ln -s "/usr/bin/fd" "${DPKG_DIR}/usr/bin/fdfind"
ln -s  './fd.bash' "${DPKG_DIR}/usr/share/bash-completion/completions/fdfind"
ln -s  './fd.fish' "${DPKG_DIR}/usr/share/fish/vendor_completions.d/fdfind.fish"
ln -s  './_fd' "${DPKG_DIR}/usr/share/zsh/vendor-completions/_fdfind"

cat > "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/copyright" <<EOF
Format: http://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: fd
Source: ${REPO}

Files: *
Copyright: ${MAINTAINER}
Copyright: $COPYRIGHT_YEARS ${MAINTAINER}
License: Apache-2.0 or MIT

License: Apache-2.0
  On Debian systems, the complete text of the Apache-2.0 can be found in the
  file /usr/share/common-licenses/Apache-2.0.

License: MIT
  Permission is hereby granted, free of charge, to any
  person obtaining a copy of this software and associated
  documentation files (the "Software"), to deal in the
  Software without restriction, including without
  limitation the rights to use, copy, modify, merge,
  publish, distribute, sublicense, and/or sell copies of
  the Software, and to permit persons to whom the Software
  is furnished to do so, subject to the following
  conditions:
  .
  The above copyright notice and this permission notice
  shall be included in all copies or substantial portions
  of the Software.
  .
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
  ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
  TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
  SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
  IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
  DEALINGS IN THE SOFTWARE.
EOF
  chmod 644 "${DPKG_DIR}/usr/share/doc/${DPKG_BASENAME}/copyright"

  # control file
  mkdir -p "${DPKG_DIR}/DEBIAN"
  cat > "${DPKG_DIR}/DEBIAN/control" <<EOF
Package: ${DPKG_BASENAME}
Version: ${DPKG_VERSION}
Section: utils
Priority: optional
Maintainer: ${MAINTAINER}
Homepage: ${REPO}
Architecture: ${DPKG_ARCH}
Provides: fd
Conflicts: ${DPKG_CONFLICTS}
Description: simple, fast and user-friendly alternative to find
  fd is a program to find entries in your filesystem.
  It is a simple, fast and user-friendly alternative to find.
  While it does not aim to support all of finds powerful functionality, it provides
  sensible (opinionated) defaults for a majority of use cases.
EOF

DPKG_PATH="${DPKG_STAGING}/${DPKG_NAME}"

if [[ -n $GITHUB_OUTPUT ]]; then
  echo "DPKG_NAME=${DPKG_NAME}" >> "$GITHUB_OUTPUT"
  echo "DPKG_PATH=${DPKG_PATH}" >> "$GITHUB_OUTPUT"
fi

# build dpkg
fakeroot dpkg-deb --build "${DPKG_DIR}" "${DPKG_PATH}"
```

## File: `scripts/version-bump.sh`
```bash
#!/usr/bin/bash

set -eu

# This script automates the "Version bump" section

version="$1"

if [[ -z $version ]]; then
  echo "Usage: must supply version as first argument" >&2
  exit 1
fi

git switch -C "release-$version"
sed -i -e "0,/^\[badges/{s/^version =.*/version = \"$version\"/}" Cargo.toml

msrv="$(grep -F rust-version Cargo.toml | sed -e 's/^rust-version= "\(.*\)"/\1/')"

sed -i -e "s/Note that rust version \*[0-9.]+\* or later/Note that rust version *$msrv* or later/" README.md

sed -i -e "s/^# Upcoming release/# $version/" CHANGELOG.md

```

## File: `src/cli.rs`
```rust
use std::num::NonZeroUsize;
use std::path::{Path, PathBuf};
use std::time::Duration;

use anyhow::anyhow;
use clap::{
    Arg, ArgAction, ArgGroup, ArgMatches, Command, Parser, ValueEnum, error::ErrorKind,
    value_parser,
};
#[cfg(feature = "completions")]
use clap_complete::Shell;
use normpath::PathExt;

use crate::error::print_error;
use crate::exec::CommandSet;
use crate::filesystem;
#[cfg(unix)]
use crate::filter::OwnerFilter;
use crate::filter::SizeFilter;

#[derive(Parser)]
#[command(
    name = "fd",
    version,
    about = "A program to find entries in your filesystem",
    after_long_help = "Bugs can be reported on GitHub: https://github.com/sharkdp/fd/issues",
    max_term_width = 98,
    args_override_self = true,
    group(ArgGroup::new("execs").args(&["exec", "exec_batch", "list_details"]).conflicts_with_all(&[
            "max_results", "quiet", "max_one_result"])),
)]
pub struct Opts {
    /// Include hidden directories and files in the search results (default:
    /// hidden files and directories are skipped). Files and directories are
    /// considered to be hidden if their name starts with a `.` sign (dot).
    /// Any files or directories that are ignored due to the rules described by
    /// --no-ignore are still ignored unless otherwise specified.
    /// The flag can be overridden with --no-hidden.
    #[arg(
        long,
        short = 'H',
        help = "Search hidden files and directories",
        long_help
    )]
    pub hidden: bool,

    /// Overrides --hidden
    #[arg(long, overrides_with = "hidden", hide = true, action = ArgAction::SetTrue)]
    no_hidden: (),

    /// Show search results from files and directories that would otherwise be
    /// ignored by '.gitignore', '.ignore', '.fdignore', or the global ignore file,
    /// The flag can be overridden with --ignore.
    #[arg(
        long,
        short = 'I',
        help = "Do not respect .(git|fd)ignore files",
        long_help
    )]
    pub no_ignore: bool,

    /// Overrides --no-ignore
    #[arg(long, overrides_with = "no_ignore", hide = true, action = ArgAction::SetTrue)]
    ignore: (),

    ///Show search results from files and directories that
    ///would otherwise be ignored by '.gitignore' files.
    ///The flag can be overridden with --ignore-vcs.
    #[arg(
        long,
        hide_short_help = true,
        help = "Do not respect .gitignore files",
        long_help
    )]
    pub no_ignore_vcs: bool,

    /// Overrides --no-ignore-vcs
    #[arg(long, overrides_with = "no_ignore_vcs", hide = true, action = ArgAction::SetTrue)]
    ignore_vcs: (),

    /// Do not require a git repository to respect gitignores.
    /// By default, fd will only respect global gitignore rules, .gitignore rules,
    /// and local exclude rules if fd detects that you are searching inside a
    /// git repository. This flag allows you to relax this restriction such that
    /// fd will respect all git related ignore rules regardless of whether you're
    /// searching in a git repository or not.
    ///
    ///
    /// This flag can be disabled with --require-git.
    #[arg(
        long,
        overrides_with = "require_git",
        hide_short_help = true,
        // same description as ripgrep's flag: ripgrep/crates/core/app.rs
        long_help
    )]
    pub no_require_git: bool,

    /// Overrides --no-require-git
    #[arg(long, overrides_with = "no_require_git", hide = true, action = ArgAction::SetTrue)]
    require_git: (),

    /// Show search results from files and directories that would otherwise be
    /// ignored by '.gitignore', '.ignore', or '.fdignore' files in parent directories.
    #[arg(
        long,
        hide_short_help = true,
        help = "Do not respect .(git|fd)ignore files in parent directories",
        long_help
    )]
    pub no_ignore_parent: bool,

    /// Do not respect the global ignore file
    #[arg(long, hide = true)]
    pub no_global_ignore_file: bool,

    /// Perform an unrestricted search, including ignored and hidden files. This is
    /// an alias for '--no-ignore --hidden'.
    #[arg(long = "unrestricted", short = 'u', overrides_with_all(&["ignore", "no_hidden"]), action(ArgAction::Count), hide_short_help = true,
    help = "Unrestricted search, alias for '--no-ignore --hidden'",
        long_help,
        )]
    rg_alias_hidden_ignore: u8,

    /// Case-sensitive search (default: smart case)
    #[arg(
        long,
        short = 's',
        overrides_with("ignore_case"),
        long_help = "Perform a case-sensitive search. By default, fd uses case-insensitive \
                     searches, unless the pattern contains an uppercase character (smart \
                     case)."
    )]
    pub case_sensitive: bool,

    /// Perform a case-insensitive search. By default, fd uses case-insensitive
    /// searches, unless the pattern contains an uppercase character (smart
    /// case).
    #[arg(
        long,
        short = 'i',
        overrides_with("case_sensitive"),
        help = "Case-insensitive search (default: smart case)",
        long_help
    )]
    pub ignore_case: bool,

    /// Perform a glob-based search instead of a regular expression search.
    #[arg(
        long,
        short = 'g',
        conflicts_with("fixed_strings"),
        help = "Glob-based search (default: regular expression)",
        long_help
    )]
    pub glob: bool,

    /// Perform a regular-expression based search (default). This can be used to
    /// override --glob.
    #[arg(
        long,
        overrides_with("glob"),
        hide_short_help = true,
        help = "Regular-expression based search (default)",
        long_help
    )]
    pub regex: bool,

    /// Treat the pattern as a literal string instead of a regular expression. Note
    /// that this also performs substring comparison. If you want to match on an
    /// exact filename, consider using '--glob'.
    #[arg(
        long,
        short = 'F',
        alias = "literal",
        hide_short_help = true,
        help = "Treat pattern as literal string stead of regex",
        long_help
    )]
    pub fixed_strings: bool,

    /// Add additional required search patterns, all of which must be matched. Multiple
    /// additional patterns can be specified. The patterns are regular
    /// expressions, unless '--glob' or '--fixed-strings' is used.
    #[arg(
        long = "and",
        value_name = "pattern",
        help = "Additional search patterns that need to be matched",
        long_help,
        hide_short_help = true,
        allow_hyphen_values = true
    )]
    pub exprs: Option<Vec<String>>,

    /// Shows the full path starting from the root as opposed to relative paths.
    /// The flag can be overridden with --relative-path.
    #[arg(
        long,
        short = 'a',
        help = "Show absolute instead of relative paths",
        long_help
    )]
    pub absolute_path: bool,

    /// Overrides --absolute-path
    #[arg(long, overrides_with = "absolute_path", hide = true, action = ArgAction::SetTrue)]
    relative_path: (),

    /// Use a detailed listing format like 'ls -l'. This is basically an alias
    /// for '--exec-batch ls -l' with some additional 'ls' options. This can be
    /// used to see more metadata, to show symlink targets and to achieve a
    /// deterministic sort order.
    #[arg(
        long,
        short = 'l',
        conflicts_with("absolute_path"),
        help = "Use a long listing format with file metadata",
        long_help
    )]
    pub list_details: bool,

    /// Follow symbolic links
    #[arg(
        long,
        short = 'L',
        alias = "dereference",
        long_help = "By default, fd does not descend into symlinked directories. Using this \
                     flag, symbolic links are also traversed. \
                     Flag can be overridden with --no-follow."
    )]
    pub follow: bool,

    /// Overrides --follow
    #[arg(long, overrides_with = "follow", hide = true, action = ArgAction::SetTrue)]
    no_follow: (),

    /// By default, the search pattern is only matched against the filename (or directory name). Using this flag, the pattern is matched against the full (absolute) path. Example:
    ///   fd --glob -p '**/.git/config'
    #[arg(
        long,
        short = 'p',
        help = "Search full abs. path (default: filename only)",
        long_help,
        verbatim_doc_comment
    )]
    pub full_path: bool,

    /// Separate search results by the null character (instead of newlines).
    /// Useful for piping results to 'xargs'.
    #[arg(
        long = "print0",
        short = '0',
        conflicts_with("list_details"),
        hide_short_help = true,
        help = "Separate search results by the null character",
        long_help
    )]
    pub null_separator: bool,

    /// Limit the directory traversal to a given depth. By default, there is no
    /// limit on the search depth.
    #[arg(
        long,
        short = 'd',
        value_name = "depth",
        alias("maxdepth"),
        help = "Set maximum search depth (default: none)",
        long_help
    )]
    max_depth: Option<usize>,

    /// Only show search results starting at the given depth.
    /// See also: '--max-depth' and '--exact-depth'
    #[arg(
        long,
        value_name = "depth",
        hide_short_help = true,
        alias("mindepth"),
        help = "Only show search results starting at the given depth.",
        long_help
    )]
    min_depth: Option<usize>,

    /// Only show search results at the exact given depth. This is an alias for
    /// '--min-depth <depth> --max-depth <depth>'.
    #[arg(long, value_name = "depth", hide_short_help = true, conflicts_with_all(&["max_depth", "min_depth"]),
    help = "Only show search results at the exact given depth",
        long_help,
        )]
    exact_depth: Option<usize>,

    /// Exclude files/directories that match the given glob pattern. This
    /// overrides any other ignore logic. Multiple exclude patterns can be
    /// specified.
    ///
    /// Examples:
    /// {n}  --exclude '*.pyc'
    /// {n}  --exclude node_modules
    #[arg(
        long,
        short = 'E',
        value_name = "glob",
        help = "Exclude entries that match the given glob pattern",
        long_help
    )]
    pub exclude: Vec<String>,

    /// Do not traverse into directories that match the search criteria. If
    /// you want to exclude specific directories, use the '--exclude=…' option.
    #[arg(long, hide_short_help = true, conflicts_with_all(&["size", "exact_depth"]),
        long_help,
        )]
    pub prune: bool,

    /// Filter the search by type:
    /// {n}  'f' or 'file':         regular files
    /// {n}  'd' or 'dir' or 'directory':    directories
    /// {n}  'l' or 'symlink':      symbolic links
    /// {n}  's' or 'socket':       socket
    /// {n}  'p' or 'pipe':         named pipe (FIFO)
    /// {n}  'b' or 'block-device': block device
    /// {n}  'c' or 'char-device':  character device
    /// {n}{n}  'x' or 'executable':   executables
    /// {n}  'e' or 'empty':        empty files or directories
    ///
    /// This option can be specified more than once to include multiple file types.
    /// Searching for '--type file --type symlink' will show both regular files as
    /// well as symlinks. Note that the 'executable' and 'empty' filters work differently:
    /// '--type executable' implies '--type file' by default. And '--type empty' searches
    /// for empty files and directories, unless either '--type file' or '--type directory'
    /// is specified in addition.
    ///
    /// Examples:
    /// {n}  - Only search for files:
    /// {n}      fd --type file …
    /// {n}      fd -tf …
    /// {n}  - Find both files and symlinks
    /// {n}      fd --type file --type symlink …
    /// {n}      fd -tf -tl …
    /// {n}  - Find executable files:
    /// {n}      fd --type executable
    /// {n}      fd -tx
    /// {n}  - Find empty files:
    /// {n}      fd --type empty --type file
    /// {n}      fd -te -tf
    /// {n}  - Find empty directories:
    /// {n}      fd --type empty --type directory
    /// {n}      fd -te -td
    #[arg(
        long = "type",
        short = 't',
        value_name = "filetype",
        hide_possible_values = true,
        value_enum,
        help = "Filter by type: file (f), directory (d/dir), symlink (l), \
                executable (x), empty (e), socket (s), pipe (p), \
                char-device (c), block-device (b)",
        long_help
    )]
    pub filetype: Option<Vec<FileType>>,

    /// (Additionally) filter search results by their file extension. Multiple
    /// allowable file extensions can be specified.
    ///
    /// If you want to search for files without extension,
    /// you can use the regex '^[^.]+$' as a normal search pattern.
    #[arg(
        long = "extension",
        short = 'e',
        value_name = "ext",
        help = "Filter by file extension",
        long_help
    )]
    pub extensions: Option<Vec<String>>,

    /// Limit results based on the size of files using the format <+-><NUM><UNIT>.
    ///    '+': file size must be greater than or equal to this
    ///    '-': file size must be less than or equal to this
    ///
    /// If neither '+' nor '-' is specified, file size must be exactly equal to this.
    ///    'NUM':  The numeric size (e.g. 500)
    ///    'UNIT': The units for NUM. They are not case-sensitive.
    /// Allowed unit values:
    ///     'b':  bytes
    ///     'k':  kilobytes (base ten, 10^3 = 1000 bytes)
    ///     'm':  megabytes
    ///     'g':  gigabytes
    ///     't':  terabytes
    ///     'ki': kibibytes (base two, 2^10 = 1024 bytes)
    ///     'mi': mebibytes
    ///     'gi': gibibytes
    ///     'ti': tebibytes
    #[arg(long, short = 'S', value_parser = SizeFilter::from_string, allow_hyphen_values = true, verbatim_doc_comment, value_name = "size",
        help = "Limit results based on the size of files",
        long_help,
        verbatim_doc_comment,
        )]
    pub size: Vec<SizeFilter>,

    /// Filter results based on the file modification time. Files with modification times
    /// greater than the argument are returned. The argument can be provided
    /// as a specific point in time (YYYY-MM-DD HH:MM:SS or @timestamp) or as a duration (10h, 1d, 35min).
    /// If the time is not specified, it defaults to 00:00:00.
    /// '--change-newer-than', '--newer', or '--changed-after' can be used as aliases.
    ///
    /// Examples:
    /// {n}    --changed-within 2weeks
    /// {n}    --change-newer-than '2018-10-27 10:00:00'
    /// {n}    --newer 2018-10-27
    /// {n}    --changed-after 1day
    #[arg(
        long,
        alias("change-newer-than"),
        alias("newer"),
        alias("changed-after"),
        value_name = "date|dur",
        help = "Filter by file modification time (newer than)",
        long_help
    )]
    pub changed_within: Option<String>,

    /// Filter results based on the file modification time. Files with modification times
    /// less than the argument are returned. The argument can be provided
    /// as a specific point in time (YYYY-MM-DD HH:MM:SS or @timestamp) or as a duration (10h, 1d, 35min).
    /// '--change-older-than' or '--older' can be used as aliases.
    ///
    /// Examples:
    /// {n}    --changed-before '2018-10-27 10:00:00'
    /// {n}    --change-older-than 2weeks
    /// {n}    --older 2018-10-27
    #[arg(
        long,
        alias("change-older-than"),
        alias("older"),
        value_name = "date|dur",
        help = "Filter by file modification time (older than)",
        long_help
    )]
    pub changed_before: Option<String>,

    /// Filter files by their user and/or group.
    /// Format: [(user|uid)][:(group|gid)]. Either side is optional.
    /// Precede either side with a '!' to exclude files instead.
    ///
    /// Examples:
    /// {n}    --owner john
    /// {n}    --owner :students
    /// {n}    --owner '!john:students'
    #[cfg(unix)]
    #[arg(long, short = 'o', value_parser = OwnerFilter::from_string, value_name = "user:group",
        help = "Filter by owning user and/or group",
        long_help,
        )]
    pub owner: Option<OwnerFilter>,

    /// Instead of printing the file normally, print the format string with the following placeholders replaced:
    ///   '{}': path (of the current search result)
    ///   '{/}': basename
    ///   '{//}': parent directory
    ///   '{.}': path without file extension
    ///   '{/.}': basename without file extension
    #[arg(
        long,
        value_name = "fmt",
        help = "Print results according to template",
        conflicts_with = "list_details"
    )]
    pub format: Option<String>,

    #[command(flatten)]
    pub exec: Exec,

    /// Maximum number of arguments to pass to the command given with -X.
    /// If the number of results is greater than the given size,
    /// the command given with -X is run again with remaining arguments.
    /// A batch size of zero means there is no limit (default), but note
    /// that batching might still happen due to OS restrictions on the
    /// maximum length of command lines.
    #[arg(
        long,
        value_name = "size",
        hide_short_help = true,
        requires("exec_batch"),
        value_parser = value_parser!(usize),
        default_value_t,
        help = "Max number of arguments to run as a batch size with -X",
        long_help,
    )]
    pub batch_size: usize,

    /// Add a custom ignore-file in '.gitignore' format. These files have a low precedence.
    #[arg(
        long,
        value_name = "path",
        hide_short_help = true,
        help = "Add a custom ignore-file in '.gitignore' format",
        long_help
    )]
    pub ignore_file: Vec<PathBuf>,

    /// Declare when to use color for the pattern match output
    #[arg(
        long,
        short = 'c',
        value_enum,
        default_value_t = ColorWhen::Auto,
        value_name = "when",
        help = "When to use colors",
        long_help,
    )]
    pub color: ColorWhen,

    /// Add a terminal hyperlink to a file:// url for each path in the output.
    ///
    /// Auto mode  is used if no argument is given to this option.
    ///
    /// This doesn't do anything for --exec and --exec-batch.
    #[arg(
        long,
        alias = "hyper",
        value_name = "when",
        require_equals = true,
        value_enum,
        default_value_t = HyperlinkWhen::Never,
        default_missing_value = "auto",
        num_args = 0..=1,
        help = "Add hyperlinks to output paths"
    )]
    pub hyperlink: HyperlinkWhen,

    /// Ignore directories containing the named entry.
    #[arg(long, value_name = "name")]
    pub ignore_contain: Vec<String>,

    /// Set number of threads to use for searching & executing (default: number
    /// of available CPU cores)
    #[arg(long, short = 'j', value_name = "num", hide_short_help = true, value_parser = str::parse::<NonZeroUsize>)]
    pub threads: Option<NonZeroUsize>,

    /// Milliseconds to buffer before streaming search results to console
    ///
    /// Amount of time in milliseconds to buffer, before streaming the search
    /// results to the console.
    #[arg(long, hide = true, value_parser = parse_millis)]
    pub max_buffer_time: Option<Duration>,

    ///Limit the number of search results to 'count' and quit immediately.
    #[arg(
        long,
        value_name = "count",
        hide_short_help = true,
        overrides_with("max_one_result"),
        help = "Limit the number of search results",
        long_help
    )]
    max_results: Option<usize>,

    /// Limit the search to a single result and quit immediately.
    /// This is an alias for '--max-results=1'.
    #[arg(
        short = '1',
        hide_short_help = true,
        overrides_with("max_results"),
        help = "Limit search to a single result",
        long_help
    )]
    max_one_result: bool,

    /// When the flag is present, the program does not print anything and will
    /// return with an exit code of 0 if there is at least one match. Otherwise, the
    /// exit code will be 1.
    /// '--has-results' can be used as an alias.
    #[arg(
        long,
        short = 'q',
        alias = "has-results",
        hide_short_help = true,
        conflicts_with("max_results"),
        help = "Print nothing, exit code 0 if match found, 1 otherwise",
        long_help
    )]
    pub quiet: bool,

    /// Enable the display of filesystem errors for situations such as
    /// insufficient permissions or dead symlinks.
    #[arg(
        long,
        hide_short_help = true,
        help = "Show filesystem errors",
        long_help
    )]
    pub show_errors: bool,

    /// Change the current working directory of fd to the provided path. This
    /// means that search results will be shown with respect to the given base
    /// path. Note that relative paths which are passed to fd via the positional
    /// <path> argument or the '--search-path' option will also be resolved
    /// relative to this directory.
    #[arg(
        long,
        short = 'C',
        value_name = "path",
        hide_short_help = true,
        help = "Change current working directory",
        long_help
    )]
    pub base_directory: Option<PathBuf>,

    /// the search pattern which is either a regular expression (default) or a glob
    /// pattern (if --glob is used). If no pattern has been specified, every entry
    /// is considered a match. If your pattern starts with a dash (-), make sure to
    /// pass '--' first, or it will be considered as a flag (fd -- '-foo').
    #[arg(
        default_value = "",
        hide_default_value = true,
        value_name = "pattern",
        help = "the search pattern (a regular expression, unless '--glob' is used; optional)",
        long_help
    )]
    pub pattern: String,

    /// Set the path separator to use when printing file paths. The default is
    /// the OS-specific separator ('/' on Unix, '\' on Windows).
    #[arg(
        long,
        value_name = "separator",
        hide_short_help = true,
        help = "Set path separator when printing file paths",
        long_help
    )]
    pub path_separator: Option<String>,

    /// The directory where the filesystem search is rooted (optional). If
    /// omitted, search the current working directory.
    #[arg(action = ArgAction::Append,
        value_name = "path",
        help = "the root directories for the filesystem search (optional)",
        long_help,
        )]
    path: Vec<PathBuf>,

    /// Provide paths to search as an alternative to the positional <path>
    /// argument. Changes the usage to `fd [OPTIONS] --search-path <path>
    /// --search-path <path2> [<pattern>]`
    #[arg(
        long,
        conflicts_with("path"),
        value_name = "search-path",
        hide_short_help = true,
        help = "Provides paths to search as an alternative to the positional <path> argument",
        long_help
    )]
    search_path: Vec<PathBuf>,

    /// By default, relative paths are prefixed with './' when -x/--exec,
    /// -X/--exec-batch, or -0/--print0 are given, to reduce the risk of a
    /// path starting with '-' being treated as a command line option. Use
    /// this flag to change this behavior. If this flag is used without a value,
    /// it is equivalent to passing "always".
    #[arg(long, conflicts_with_all(&["path", "search_path"]), value_name = "when", hide_short_help = true, require_equals = true, long_help)]
    strip_cwd_prefix: Option<Option<StripCwdWhen>>,

    /// By default, fd will traverse the file system tree as far as other options
    /// dictate. With this flag, fd ensures that it does not descend into a
    /// different file system than the one it started in. Comparable to the -mount
    /// or -xdev filters of find(1).
    #[cfg(any(unix, windows))]
    #[arg(long, aliases(&["mount", "xdev"]), hide_short_help = true, long_help)]
    pub one_file_system: bool,

    #[cfg(feature = "completions")]
    #[arg(long, hide = true, exclusive = true)]
    gen_completions: Option<Option<Shell>>,
}

impl Opts {
    pub fn search_paths(&self) -> anyhow::Result<Vec<PathBuf>> {
        // would it make sense to concatenate these?
        let paths = if !self.path.is_empty() {
            &self.path
        } else if !self.search_path.is_empty() {
            &self.search_path
        } else {
            let current_directory = Path::new("./");
            ensure_current_directory_exists(current_directory)?;
            return Ok(vec![self.normalize_path(current_directory)]);
        };
        Ok(paths
            .iter()
            .filter_map(|path| {
                if filesystem::is_existing_directory(path) {
                    Some(self.normalize_path(path))
                } else {
                    print_error(format!(
                        "Search path '{}' is not a directory.",
                        path.to_string_lossy()
                    ));
                    None
                }
            })
            .collect())
    }

    fn normalize_path(&self, path: &Path) -> PathBuf {
        if self.absolute_path {
            filesystem::absolute_path(path.normalize().unwrap().as_path()).unwrap()
        } else if path == Path::new(".") {
            // Change "." to "./" as a workaround for https://github.com/BurntSushi/ripgrep/pull/2711
            PathBuf::from("./")
        } else {
            path.to_path_buf()
        }
    }

    pub fn no_search_paths(&self) -> bool {
        self.path.is_empty() && self.search_path.is_empty()
    }

    #[inline]
    pub fn rg_alias_ignore(&self) -> bool {
        self.rg_alias_hidden_ignore > 0
    }

    pub fn max_depth(&self) -> Option<usize> {
        self.max_depth.or(self.exact_depth)
    }

    pub fn min_depth(&self) -> Option<usize> {
        self.min_depth.or(self.exact_depth)
    }

    pub fn threads(&self) -> NonZeroUsize {
        self.threads.unwrap_or_else(default_num_threads)
    }

    pub fn max_results(&self) -> Option<usize> {
        self.max_results
            .filter(|&m| m > 0)
            .or_else(|| self.max_one_result.then_some(1))
    }

    pub fn strip_cwd_prefix<P: FnOnce() -> bool>(&self, auto_pred: P) -> bool {
        use self::StripCwdWhen::*;
        self.no_search_paths()
            && match self.strip_cwd_prefix.map_or(Auto, |o| o.unwrap_or(Always)) {
                Auto => auto_pred(),
                Always => true,
                Never => false,
            }
    }

    #[cfg(feature = "completions")]
    pub fn gen_completions(&self) -> anyhow::Result<Option<Shell>> {
        self.gen_completions
            .map(|maybe_shell| match maybe_shell {
                Some(sh) => Ok(sh),
                None => {
                    Shell::from_env().ok_or_else(|| anyhow!("Unable to get shell from environment"))
                }
            })
            .transpose()
    }
}

/// Get the default number of threads to use, if not explicitly specified.
fn default_num_threads() -> NonZeroUsize {
    // If we can't get the amount of parallelism for some reason, then
    // default to a single thread, because that is safe.
    let fallback = NonZeroUsize::MIN;
    // To limit startup overhead on massively parallel machines, don't use more
    // than 64 threads.
    let limit = NonZeroUsize::new(64).unwrap();

    std::thread::available_parallelism()
        .unwrap_or(fallback)
        .min(limit)
}

#[derive(Copy, Clone, PartialEq, Eq, ValueEnum)]
pub enum FileType {
    #[value(alias = "f")]
    File,
    #[value(alias = "d", alias = "dir")]
    Directory,
    #[value(alias = "l")]
    Symlink,
    #[value(alias = "b")]
    BlockDevice,
    #[value(alias = "c")]
    CharDevice,
    /// A file which is executable by the current effective user
    #[value(alias = "x")]
    Executable,
    #[value(alias = "e")]
    Empty,
    #[value(alias = "s")]
    Socket,
    #[value(alias = "p")]
    Pipe,
}

#[derive(Copy, Clone, PartialEq, Eq, Debug, ValueEnum)]
pub enum ColorWhen {
    /// show colors if the output goes to an interactive console (default)
    Auto,
    /// always use colorized output
    Always,
    /// do not use colorized output
    Never,
}

#[derive(Copy, Clone, PartialEq, Eq, Debug, ValueEnum)]
pub enum StripCwdWhen {
    /// Use the default behavior
    Auto,
    /// Always strip the ./ at the beginning of paths
    Always,
    /// Never strip the ./
    Never,
}

#[derive(Copy, Clone, PartialEq, Eq, Debug, ValueEnum)]
pub enum HyperlinkWhen {
    /// Use hyperlinks only if color is enabled
    Auto,
    /// Always use hyperlinks when printing file paths
    Always,
    /// Never use hyperlinks
    Never,
}

// there isn't a derive api for getting grouped values yet,
// so we have to use hand-rolled parsing for exec and exec-batch
pub struct Exec {
    pub command: Option<CommandSet>,
}

impl clap::FromArgMatches for Exec {
    fn from_arg_matches(matches: &ArgMatches) -> clap::error::Result<Self> {
        let command = matches
            .get_occurrences::<String>("exec")
            .map(CommandSet::new)
            .or_else(|| {
                matches
                    .get_occurrences::<String>("exec_batch")
                    .map(CommandSet::new_batch)
            })
            .transpose()
            .map_err(|e| clap::Error::raw(ErrorKind::InvalidValue, e))?;
        Ok(Exec { command })
    }

    fn update_from_arg_matches(&mut self, matches: &ArgMatches) -> clap::error::Result<()> {
        *self = Self::from_arg_matches(matches)?;
        Ok(())
    }
}

impl clap::Args for Exec {
    fn augment_args(cmd: Command) -> Command {
        cmd.arg(Arg::new("exec")
            .action(ArgAction::Append)
            .long("exec")
            .short('x')
            .num_args(1..)
                .allow_hyphen_values(true)
                .value_terminator(";")
                .value_name("cmd")
                .conflicts_with("list_details")
                .help("Execute a command for each search result")
                .long_help(
                    "Execute a command for each search result in parallel (use --threads=1 for sequential command execution). \
                     There is no guarantee of the order commands are executed in, and the order should not be depended upon. \
                     All positional arguments following --exec are considered to be arguments to the command - not to fd. \
                     It is therefore recommended to place the '-x'/'--exec' option last. \
                     Use '\\;' to terminate the command template if you need to continue passing fd arguments afterwards.\n\
                     The following placeholders are substituted before the command is executed:\n  \
                       '{}':   path (of the current search result)\n  \
                       '{/}':  basename\n  \
                       '{//}': parent directory\n  \
                       '{.}':  path without file extension\n  \
                       '{/.}': basename without file extension\n  \
                       '{{':   literal '{' (for escaping)\n  \
                       '}}':   literal '}' (for escaping)\n\n\
                     If no placeholder is present, an implicit \"{}\" at the end is assumed.\n\n\
                     Examples:\n\n  \
                       - find all *.zip files and unzip them:\n\n      \
                           fd -e zip -x unzip\n\n  \
                       - find *.h and *.cpp files and run \"clang-format -i ..\" for each of them:\n\n      \
                           fd -e h -e cpp -x clang-format -i\n\n  \
                       - search within `src/` and echo each match (place `-x` last):\n\n      \
                           fd . src -x echo\n\n  \
                       - Convert all *.jpg files to *.png files:\n\n      \
                           fd -e jpg -x convert {} {.}.png\
                    ",
                ),
        )
        .arg(
            Arg::new("exec_batch")
                .action(ArgAction::Append)
                .long("exec-batch")
                .short('X')
                .num_args(1..)
                .allow_hyphen_values(true)
                .value_terminator(";")
                .value_name("cmd")
                .conflicts_with_all(["exec", "list_details"])
                .help("Execute a command with all search results at once")
                .long_help(
                    "Execute the given command once, with all search results as arguments.\n\
                     The order of the arguments is non-deterministic, and should not be relied upon.\n\
                     One of the following placeholders is substituted before the command is executed:\n  \
                       '{}':   path (of all search results)\n  \
                       '{/}':  basename\n  \
                       '{//}': parent directory\n  \
                       '{.}':  path without file extension\n  \
                       '{/.}': basename without file extension\n  \
                       '{{':   literal '{' (for escaping)\n  \
                       '}}':   literal '}' (for escaping)\n\n\
                     If no placeholder is present, an implicit \"{}\" at the end is assumed.\n\n\
                     Examples:\n\n  \
                       - Find all test_*.py files and open them in your favorite editor:\n\n      \
                           fd -g 'test_*.py' -X vim\n\n  \
                       - Find all *.rs files and count the lines with \"wc -l ...\":\n\n      \
                           fd -e rs -X wc -l\
                     "
                ),
        )
    }

    fn augment_args_for_update(cmd: Command) -> Command {
        Self::augment_args(cmd)
    }
}

fn parse_millis(arg: &str) -> Result<Duration, std::num::ParseIntError> {
    Ok(Duration::from_millis(arg.parse()?))
}

fn ensure_current_directory_exists(current_directory: &Path) -> anyhow::Result<()> {
    if filesystem::is_existing_directory(current_directory) {
        Ok(())
    } else {
        Err(anyhow!(
            "Could not retrieve current directory (has it been deleted?)."
        ))
    }
}
```

## File: `src/config.rs`
```rust
use std::{path::PathBuf, sync::Arc, time::Duration};

use lscolors::LsColors;
use regex::bytes::RegexSet;

use crate::exec::CommandSet;
use crate::filetypes::FileTypes;
#[cfg(unix)]
use crate::filter::OwnerFilter;
use crate::filter::{SizeFilter, TimeFilter};
use crate::fmt::FormatTemplate;

/// Configuration options for *fd*.
pub struct Config {
    /// Whether the search is case-sensitive or case-insensitive.
    pub case_sensitive: bool,

    /// Cached current working directory for absolute path construction.
    /// Populated when `--full-path` is set; `None` means search by filename only.
    pub full_path_base: Option<PathBuf>,

    /// Whether to ignore hidden files and directories (or not).
    pub ignore_hidden: bool,

    /// Whether to respect `.fdignore` files or not.
    pub read_fdignore: bool,

    /// Whether to respect ignore files in parent directories or not.
    pub read_parent_ignore: bool,

    /// Whether to respect VCS ignore files (`.gitignore`, ..) or not.
    pub read_vcsignore: bool,

    /// Whether to require a `.git` directory to respect gitignore files.
    pub require_git_to_read_vcsignore: bool,

    /// Whether to respect the global ignore file or not.
    pub read_global_ignore: bool,

    /// Whether to follow symlinks or not.
    pub follow_links: bool,

    /// Whether to limit the search to starting file system or not.
    pub one_file_system: bool,

    /// Whether elements of output should be separated by a null character
    pub null_separator: bool,

    /// The maximum search depth, or `None` if no maximum search depth should be set.
    ///
    /// A depth of `1` includes all files under the current directory, a depth of `2` also includes
    /// all files under subdirectories of the current directory, etc.
    pub max_depth: Option<usize>,

    /// The minimum depth for reported entries, or `None`.
    pub min_depth: Option<usize>,

    /// Whether to stop traversing into matching directories.
    pub prune: bool,

    /// The number of threads to use.
    pub threads: usize,

    /// If true, the program doesn't print anything and will instead return an exit code of 0
    /// if there's at least one match. Otherwise, the exit code will be 1.
    pub quiet: bool,

    /// Time to buffer results internally before streaming to the console. This is useful to
    /// provide a sorted output, in case the total execution time is shorter than
    /// `max_buffer_time`.
    pub max_buffer_time: Option<Duration>,

    /// `None` if the output should not be colorized. Otherwise, a `LsColors` instance that defines
    /// how to style different filetypes.
    pub ls_colors: Option<LsColors>,

    /// Whether or not we are writing to an interactive terminal
    #[cfg_attr(not(unix), allow(unused))]
    pub interactive_terminal: bool,

    /// The type of file to search for. If set to `None`, all file types are displayed. If
    /// set to `Some(..)`, only the types that are specified are shown.
    pub file_types: Option<FileTypes>,

    /// The extension to search for. Only entries matching the extension will be included.
    ///
    /// The value (if present) will be a lowercase string without leading dots.
    pub extensions: Option<RegexSet>,

    /// A format string to use to format results, similarly to exec
    pub format: Option<FormatTemplate>,

    /// If a value is supplied, each item found will be used to generate and execute commands.
    pub command: Option<Arc<CommandSet>>,

    /// Maximum number of search results to pass to each `command`. If zero, the number is
    /// unlimited.
    pub batch_size: usize,

    /// A list of glob patterns that should be excluded from the search.
    pub exclude_patterns: Vec<String>,

    /// A list of custom ignore files.
    pub ignore_files: Vec<PathBuf>,

    /// The given constraints on the size of returned files
    pub size_constraints: Vec<SizeFilter>,

    /// Constraints on last modification time of files
    pub time_constraints: Vec<TimeFilter>,

    #[cfg(unix)]
    /// User/group ownership constraint
    pub owner_constraint: Option<OwnerFilter>,

    /// Whether or not to display filesystem errors
    pub show_filesystem_errors: bool,

    /// The separator used to print file paths.
    pub path_separator: Option<String>,

    /// The actual separator, either the system default separator or `path_separator`
    pub actual_path_separator: String,

    /// The maximum number of search results
    pub max_results: Option<usize>,

    /// Whether or not to strip the './' prefix for search results
    pub strip_cwd_prefix: bool,

    /// Whether or not to use hyperlinks on paths
    pub hyperlink: bool,

    /// Names that should stop traversal down their parent. (e.g. https://bford.info/cachedir/).
    pub ignore_contain: Vec<String>,
}

impl Config {
    /// Check whether results are being printed.
    pub fn is_printing(&self) -> bool {
        self.command.is_none()
    }
}
```

## File: `src/dir_entry.rs`
```rust
use std::cell::OnceCell;
use std::ffi::OsString;
use std::fs::{FileType, Metadata};
use std::path::{Path, PathBuf};

use lscolors::{Colorable, LsColors, Style};

use crate::config::Config;
use crate::filesystem::strip_current_dir;

#[derive(Debug)]
enum DirEntryInner {
    Normal(ignore::DirEntry),
    BrokenSymlink(PathBuf),
}

#[derive(Debug)]
pub struct DirEntry {
    inner: DirEntryInner,
    metadata: OnceCell<Option<Metadata>>,
    style: OnceCell<Option<Style>>,
}

impl DirEntry {
    #[inline]
    pub fn normal(e: ignore::DirEntry) -> Self {
        Self {
            inner: DirEntryInner::Normal(e),
            metadata: OnceCell::new(),
            style: OnceCell::new(),
        }
    }

    pub fn broken_symlink(path: PathBuf) -> Self {
        Self {
            inner: DirEntryInner::BrokenSymlink(path),
            metadata: OnceCell::new(),
            style: OnceCell::new(),
        }
    }

    pub fn path(&self) -> &Path {
        match &self.inner {
            DirEntryInner::Normal(e) => e.path(),
            DirEntryInner::BrokenSymlink(pathbuf) => pathbuf.as_path(),
        }
    }

    pub fn into_path(self) -> PathBuf {
        match self.inner {
            DirEntryInner::Normal(e) => e.into_path(),
            DirEntryInner::BrokenSymlink(p) => p,
        }
    }

    /// Returns the path as it should be presented to the user.
    pub fn stripped_path(&self, config: &Config) -> &Path {
        if config.strip_cwd_prefix {
            strip_current_dir(self.path())
        } else {
            self.path()
        }
    }

    /// Returns the path as it should be presented to the user.
    pub fn into_stripped_path(self, config: &Config) -> PathBuf {
        if config.strip_cwd_prefix {
            self.stripped_path(config).to_path_buf()
        } else {
            self.into_path()
        }
    }

    pub fn file_type(&self) -> Option<FileType> {
        match &self.inner {
            DirEntryInner::Normal(e) => e.file_type(),
            DirEntryInner::BrokenSymlink(_) => self.metadata().map(|m| m.file_type()),
        }
    }

    pub fn metadata(&self) -> Option<&Metadata> {
        self.metadata
            .get_or_init(|| match &self.inner {
                DirEntryInner::Normal(e) => e.metadata().ok(),
                DirEntryInner::BrokenSymlink(path) => path.symlink_metadata().ok(),
            })
            .as_ref()
    }

    pub fn depth(&self) -> Option<usize> {
        match &self.inner {
            DirEntryInner::Normal(e) => Some(e.depth()),
            DirEntryInner::BrokenSymlink(_) => None,
        }
    }

    pub fn style(&self, ls_colors: &LsColors) -> Option<&Style> {
        self.style
            .get_or_init(|| ls_colors.style_for(self).cloned())
            .as_ref()
    }
}

impl PartialEq for DirEntry {
    #[inline]
    fn eq(&self, other: &Self) -> bool {
        self.path() == other.path()
    }
}

impl Eq for DirEntry {}

impl PartialOrd for DirEntry {
    #[inline]
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for DirEntry {
    #[inline]
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.path().cmp(other.path())
    }
}

impl Colorable for DirEntry {
    fn path(&self) -> PathBuf {
        self.path().to_owned()
    }

    fn file_name(&self) -> OsString {
        let name = match &self.inner {
            DirEntryInner::Normal(e) => e.file_name(),
            DirEntryInner::BrokenSymlink(path) => {
                // Path::file_name() only works if the last component is Normal,
                // but we want it for all component types, so we open code it.
                // Copied from LsColors::style_for_path_with_metadata().
                path.components()
                    .next_back()
                    .map(|c| c.as_os_str())
                    .unwrap_or_else(|| path.as_os_str())
            }
        };
        name.to_owned()
    }

    fn file_type(&self) -> Option<FileType> {
        self.file_type()
    }

    fn metadata(&self) -> Option<Metadata> {
        self.metadata().cloned()
    }
}
```

## File: `src/error.rs`
```rust
pub fn print_error(msg: impl Into<String>) {
    eprintln!("[fd error]: {}", msg.into());
}
```

## File: `src/exit_codes.rs`
```rust
use std::process;

#[cfg(unix)]
use nix::sys::signal::{SigHandler, Signal, raise, signal};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ExitCode {
    Success,
    HasResults(bool),
    GeneralError,
    KilledBySigint,
}

impl From<ExitCode> for i32 {
    fn from(code: ExitCode) -> Self {
        match code {
            ExitCode::Success => 0,
            ExitCode::HasResults(has_results) => !has_results as i32,
            ExitCode::GeneralError => 1,
            ExitCode::KilledBySigint => 130,
        }
    }
}

impl ExitCode {
    fn is_error(self) -> bool {
        i32::from(self) != 0
    }

    /// Exit the process with the appropriate code.
    pub fn exit(self) -> ! {
        #[cfg(unix)]
        if self == ExitCode::KilledBySigint {
            // Get rid of the SIGINT handler, if present, and raise SIGINT
            unsafe {
                if signal(Signal::SIGINT, SigHandler::SigDfl).is_ok() {
                    let _ = raise(Signal::SIGINT);
                }
            }
        }

        process::exit(self.into())
    }
}

pub fn merge_exitcodes(results: impl IntoIterator<Item = ExitCode>) -> ExitCode {
    if results.into_iter().any(ExitCode::is_error) {
        return ExitCode::GeneralError;
    }
    ExitCode::Success
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn success_when_no_results() {
        assert_eq!(merge_exitcodes([]), ExitCode::Success);
    }

    #[test]
    fn general_error_if_at_least_one_error() {
        assert_eq!(
            merge_exitcodes([ExitCode::GeneralError]),
            ExitCode::GeneralError
        );
        assert_eq!(
            merge_exitcodes([ExitCode::KilledBySigint]),
            ExitCode::GeneralError
        );
        assert_eq!(
            merge_exitcodes([ExitCode::KilledBySigint, ExitCode::Success]),
            ExitCode::GeneralError
        );
        assert_eq!(
            merge_exitcodes([ExitCode::Success, ExitCode::GeneralError]),
            ExitCode::GeneralError
        );
        assert_eq!(
            merge_exitcodes([ExitCode::GeneralError, ExitCode::KilledBySigint]),
            ExitCode::GeneralError
        );
    }

    #[test]
    fn success_if_no_error() {
        assert_eq!(merge_exitcodes([ExitCode::Success]), ExitCode::Success);
        assert_eq!(
            merge_exitcodes([ExitCode::Success, ExitCode::Success]),
            ExitCode::Success
        );
    }
}
```

## File: `src/filesystem.rs`
```rust
use std::borrow::Cow;
use std::env;
use std::ffi::OsStr;
use std::fs;
use std::io;
#[cfg(any(unix, target_os = "redox"))]
use std::os::unix::fs::FileTypeExt;
use std::path::{Path, PathBuf};

use normpath::PathExt;

use crate::dir_entry;

pub fn path_absolute_form(path: &Path) -> io::Result<PathBuf> {
    if path.is_absolute() {
        return Ok(path.to_path_buf());
    }

    let path = path.strip_prefix(".").unwrap_or(path);
    env::current_dir().map(|path_buf| path_buf.join(path))
}

pub fn absolute_path(path: &Path) -> io::Result<PathBuf> {
    let path_buf = path_absolute_form(path)?;

    #[cfg(windows)]
    let path_buf = Path::new(
        path_buf
            .as_path()
            .to_string_lossy()
            .trim_start_matches(r"\\?\"),
    )
    .to_path_buf();

    Ok(path_buf)
}

pub fn is_existing_directory(path: &Path) -> bool {
    // Note: we do not use `.exists()` here, as `.` always exists, even if
    // the CWD has been deleted.
    path.is_dir() && (path.file_name().is_some() || path.normalize().is_ok())
}

pub fn is_empty(entry: &dir_entry::DirEntry) -> bool {
    if let Some(file_type) = entry.file_type() {
        if file_type.is_dir() {
            if let Ok(mut entries) = fs::read_dir(entry.path()) {
                entries.next().is_none()
            } else {
                false
            }
        } else if file_type.is_file() {
            entry.metadata().map(|m| m.len() == 0).unwrap_or(false)
        } else {
            false
        }
    } else {
        false
    }
}

#[cfg(any(unix, target_os = "redox"))]
pub fn is_block_device(ft: fs::FileType) -> bool {
    ft.is_block_device()
}

#[cfg(windows)]
pub fn is_block_device(_: fs::FileType) -> bool {
    false
}

#[cfg(any(unix, target_os = "redox"))]
pub fn is_char_device(ft: fs::FileType) -> bool {
    ft.is_char_device()
}

#[cfg(windows)]
pub fn is_char_device(_: fs::FileType) -> bool {
    false
}

#[cfg(any(unix, target_os = "redox"))]
pub fn is_socket(ft: fs::FileType) -> bool {
    ft.is_socket()
}

#[cfg(windows)]
pub fn is_socket(_: fs::FileType) -> bool {
    false
}

#[cfg(any(unix, target_os = "redox"))]
pub fn is_pipe(ft: fs::FileType) -> bool {
    ft.is_fifo()
}

#[cfg(windows)]
pub fn is_pipe(_: fs::FileType) -> bool {
    false
}

#[cfg(any(unix, target_os = "redox"))]
pub fn osstr_to_bytes(input: &OsStr) -> Cow<'_, [u8]> {
    use std::os::unix::ffi::OsStrExt;
    Cow::Borrowed(input.as_bytes())
}

#[cfg(windows)]
pub fn osstr_to_bytes(input: &OsStr) -> Cow<'_, [u8]> {
    let string = input.to_string_lossy();

    match string {
        Cow::Owned(string) => Cow::Owned(string.into_bytes()),
        Cow::Borrowed(string) => Cow::Borrowed(string.as_bytes()),
    }
}

/// Remove the `./` prefix from a path.
pub fn strip_current_dir(path: &Path) -> &Path {
    path.strip_prefix(".").unwrap_or(path)
}

/// Default value for the path_separator, mainly for MSYS/MSYS2, which set the MSYSTEM
/// environment variable, and we set fd's path separator to '/' rather than Rust's default of '\'.
///
/// Returns Some to use a nonstandard path separator, or None to use rust's default on the target
/// platform.
pub fn default_path_separator() -> Option<String> {
    if cfg!(windows) {
        let msystem = env::var("MSYSTEM").ok()?;
        if !msystem.is_empty() {
            return Some("/".to_owned());
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::strip_current_dir;
    use std::path::Path;

    #[test]
    fn strip_current_dir_basic() {
        assert_eq!(strip_current_dir(Path::new("./foo")), Path::new("foo"));
        assert_eq!(strip_current_dir(Path::new("foo")), Path::new("foo"));
        assert_eq!(
            strip_current_dir(Path::new("./foo/bar/baz")),
            Path::new("foo/bar/baz")
        );
        assert_eq!(
            strip_current_dir(Path::new("foo/bar/baz")),
            Path::new("foo/bar/baz")
        );
    }
}
```

## File: `src/filetypes.rs`
```rust
use crate::dir_entry;
use crate::filesystem;

use faccess::PathExt;

/// Whether or not to show
#[derive(Default)]
pub struct FileTypes {
    pub files: bool,
    pub directories: bool,
    pub symlinks: bool,
    pub block_devices: bool,
    pub char_devices: bool,
    pub sockets: bool,
    pub pipes: bool,
    pub executables_only: bool,
    pub empty_only: bool,
}

impl FileTypes {
    pub fn should_ignore(&self, entry: &dir_entry::DirEntry) -> bool {
        if let Some(ref entry_type) = entry.file_type() {
            (!self.files && entry_type.is_file())
                || (!self.directories && entry_type.is_dir())
                || (!self.symlinks && entry_type.is_symlink())
                || (!self.block_devices && filesystem::is_block_device(*entry_type))
                || (!self.char_devices && filesystem::is_char_device(*entry_type))
                || (!self.sockets && filesystem::is_socket(*entry_type))
                || (!self.pipes && filesystem::is_pipe(*entry_type))
                || (self.executables_only && !entry.path().executable())
                || (self.empty_only && !filesystem::is_empty(entry))
                || !(entry_type.is_file()
                    || entry_type.is_dir()
                    || entry_type.is_symlink()
                    || filesystem::is_block_device(*entry_type)
                    || filesystem::is_char_device(*entry_type)
                    || filesystem::is_socket(*entry_type)
                    || filesystem::is_pipe(*entry_type))
        } else {
            true
        }
    }
}
```

## File: `src/hyperlink.rs`
```rust
use crate::filesystem::absolute_path;
use std::fmt::{self, Formatter, Write};
use std::path::{Path, PathBuf};

pub(crate) struct PathUrl(PathBuf);

impl PathUrl {
    pub(crate) fn new(path: &Path) -> Option<PathUrl> {
        Some(PathUrl(absolute_path(path).ok()?))
    }
}

impl fmt::Display for PathUrl {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "file://{}", host())?;
        let bytes = self.0.as_os_str().as_encoded_bytes();
        for &byte in bytes.iter() {
            encode(f, byte)?;
        }
        Ok(())
    }
}

fn encode(f: &mut Formatter, byte: u8) -> fmt::Result {
    // NOTE:
    // Most terminals can handle non-ascii unicode characters in a file url fine. But on some OSes (notably
    // windows), the encoded bytes of the path may not be valid UTF-8. Since we don't know if a
    // byte >= 128 is part of a valid UTF-8 encoding or not, we just percent encode any non-ascii
    // byte.
    // Percent encoding these bytes is probably safer anyway.
    match byte {
        b'0'..=b'9' | b'A'..=b'Z' | b'a'..=b'z' | b'/' | b':' | b'-' | b'.' | b'_' | b'~' => {
            f.write_char(byte.into())
        }
        #[cfg(windows)]
        b'\\' => f.write_char('/'),
        _ => {
            write!(f, "%{byte:02X}")
        }
    }
}

#[cfg(unix)]
fn host() -> &'static str {
    use std::sync::OnceLock;

    static HOSTNAME: OnceLock<String> = OnceLock::new();

    HOSTNAME
        .get_or_init(|| {
            nix::unistd::gethostname()
                .ok()
                .and_then(|h| h.into_string().ok())
                .unwrap_or_default()
        })
        .as_ref()
}

#[cfg(not(unix))]
const fn host() -> &'static str {
    "/"
}

#[cfg(test)]
mod test {
    use super::*;

    // This allows us to test the encoding without having to worry about the host, or absolute path
    struct Encoded(&'static str);

    impl fmt::Display for Encoded {
        fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
            for byte in self.0.bytes() {
                encode(f, byte)?;
            }
            Ok(())
        }
    }

    #[test]
    fn test_unicode_encoding() {
        assert_eq!(
            Encoded("$*\x1bßé/∫😃\x07").to_string(),
            "%24%2A%1B%C3%9F%C3%A9/%E2%88%AB%F0%9F%98%83%07",
        );
    }
}
```

## File: `src/main.rs`
```rust
mod cli;
mod config;
mod dir_entry;
mod error;
mod exec;
mod exit_codes;
mod filesystem;
mod filetypes;
mod filter;
mod fmt;
mod hyperlink;
mod output;
mod regex_helper;
mod walk;

use std::env;
use std::io::IsTerminal;
use std::path::Path;
use std::sync::Arc;

use anyhow::{Context, Result, anyhow, bail};
use clap::{CommandFactory, Parser};
use globset::GlobBuilder;
use lscolors::LsColors;
use regex::bytes::{Regex, RegexBuilder, RegexSetBuilder};

use crate::cli::{ColorWhen, HyperlinkWhen, Opts};
use crate::config::Config;
use crate::exec::CommandSet;
use crate::exit_codes::ExitCode;
use crate::filetypes::FileTypes;
#[cfg(unix)]
use crate::filter::OwnerFilter;
use crate::filter::TimeFilter;
use crate::regex_helper::{pattern_has_uppercase_char, pattern_matches_strings_with_leading_dot};

// We use jemalloc for performance reasons, see https://github.com/sharkdp/fd/pull/481
// FIXME: re-enable jemalloc on macOS, see comment in Cargo.toml file for more infos
// This has to be kept in sync with the Cargo.toml file section that declares a
// dependency on tikv-jemallocator.
#[cfg(all(
    not(windows),
    not(target_os = "android"),
    not(target_os = "macos"),
    not(target_os = "freebsd"),
    not(target_os = "openbsd"),
    not(target_os = "illumos"),
    not(all(target_env = "musl", target_pointer_width = "32")),
    not(target_arch = "riscv64"),
    feature = "use-jemalloc"
))]
#[global_allocator]
static ALLOC: tikv_jemallocator::Jemalloc = tikv_jemallocator::Jemalloc;

// vivid --color-mode 8-bit generate molokai
const DEFAULT_LS_COLORS: &str = "
ow=0:or=0;38;5;16;48;5;203:no=0:ex=1;38;5;203:cd=0;38;5;203;48;5;236:mi=0;38;5;16;48;5;203:*~=0;38;5;243:st=0:pi=0;38;5;16;48;5;81:fi=0:di=0;38;5;81:so=0;38;5;16;48;5;203:bd=0;38;5;81;48;5;236:tw=0:ln=0;38;5;203:*.m=0;38;5;48:*.o=0;38;5;243:*.z=4;38;5;203:*.a=1;38;5;203:*.r=0;38;5;48:*.c=0;38;5;48:*.d=0;38;5;48:*.t=0;38;5;48:*.h=0;38;5;48:*.p=0;38;5;48:*.cc=0;38;5;48:*.ll=0;38;5;48:*.jl=0;38;5;48:*css=0;38;5;48:*.md=0;38;5;185:*.gz=4;38;5;203:*.nb=0;38;5;48:*.mn=0;38;5;48:*.go=0;38;5;48:*.xz=4;38;5;203:*.so=1;38;5;203:*.rb=0;38;5;48:*.pm=0;38;5;48:*.bc=0;38;5;243:*.py=0;38;5;48:*.as=0;38;5;48:*.pl=0;38;5;48:*.rs=0;38;5;48:*.sh=0;38;5;48:*.7z=4;38;5;203:*.ps=0;38;5;186:*.cs=0;38;5;48:*.el=0;38;5;48:*.rm=0;38;5;208:*.hs=0;38;5;48:*.td=0;38;5;48:*.ui=0;38;5;149:*.ex=0;38;5;48:*.js=0;38;5;48:*.cp=0;38;5;48:*.cr=0;38;5;48:*.la=0;38;5;243:*.kt=0;38;5;48:*.ml=0;38;5;48:*.vb=0;38;5;48:*.gv=0;38;5;48:*.lo=0;38;5;243:*.hi=0;38;5;243:*.ts=0;38;5;48:*.ko=1;38;5;203:*.hh=0;38;5;48:*.pp=0;38;5;48:*.di=0;38;5;48:*.bz=4;38;5;203:*.fs=0;38;5;48:*.png=0;38;5;208:*.zsh=0;38;5;48:*.mpg=0;38;5;208:*.pid=0;38;5;243:*.xmp=0;38;5;149:*.iso=4;38;5;203:*.m4v=0;38;5;208:*.dot=0;38;5;48:*.ods=0;38;5;186:*.inc=0;38;5;48:*.sxw=0;38;5;186:*.aif=0;38;5;208:*.git=0;38;5;243:*.gvy=0;38;5;48:*.tbz=4;38;5;203:*.log=0;38;5;243:*.txt=0;38;5;185:*.ico=0;38;5;208:*.csx=0;38;5;48:*.vob=0;38;5;208:*.pgm=0;38;5;208:*.pps=0;38;5;186:*.ics=0;38;5;186:*.img=4;38;5;203:*.fon=0;38;5;208:*.hpp=0;38;5;48:*.bsh=0;38;5;48:*.sql=0;38;5;48:*TODO=1:*.php=0;38;5;48:*.pkg=4;38;5;203:*.ps1=0;38;5;48:*.csv=0;38;5;185:*.ilg=0;38;5;243:*.ini=0;38;5;149:*.pyc=0;38;5;243:*.psd=0;38;5;208:*.htc=0;38;5;48:*.swp=0;38;5;243:*.mli=0;38;5;48:*hgrc=0;38;5;149:*.bst=0;38;5;149:*.ipp=0;38;5;48:*.fsi=0;38;5;48:*.tcl=0;38;5;48:*.exs=0;38;5;48:*.out=0;38;5;243:*.jar=4;38;5;203:*.xls=0;38;5;186:*.ppm=0;38;5;208:*.apk=4;38;5;203:*.aux=0;38;5;243:*.rpm=4;38;5;203:*.dll=1;38;5;203:*.eps=0;38;5;208:*.exe=1;38;5;203:*.doc=0;38;5;186:*.wma=0;38;5;208:*.deb=4;38;5;203:*.pod=0;38;5;48:*.ind=0;38;5;243:*.nix=0;38;5;149:*.lua=0;38;5;48:*.epp=0;38;5;48:*.dpr=0;38;5;48:*.htm=0;38;5;185:*.ogg=0;38;5;208:*.bin=4;38;5;203:*.otf=0;38;5;208:*.yml=0;38;5;149:*.pro=0;38;5;149:*.cxx=0;38;5;48:*.tex=0;38;5;48:*.fnt=0;38;5;208:*.erl=0;38;5;48:*.sty=0;38;5;243:*.bag=4;38;5;203:*.rst=0;38;5;185:*.pdf=0;38;5;186:*.pbm=0;38;5;208:*.xcf=0;38;5;208:*.clj=0;38;5;48:*.gif=0;38;5;208:*.rar=4;38;5;203:*.elm=0;38;5;48:*.bib=0;38;5;149:*.tsx=0;38;5;48:*.dmg=4;38;5;203:*.tmp=0;38;5;243:*.bcf=0;38;5;243:*.mkv=0;38;5;208:*.svg=0;38;5;208:*.cpp=0;38;5;48:*.vim=0;38;5;48:*.bmp=0;38;5;208:*.ltx=0;38;5;48:*.fls=0;38;5;243:*.flv=0;38;5;208:*.wav=0;38;5;208:*.m4a=0;38;5;208:*.mid=0;38;5;208:*.hxx=0;38;5;48:*.pas=0;38;5;48:*.wmv=0;38;5;208:*.tif=0;38;5;208:*.kex=0;38;5;186:*.mp4=0;38;5;208:*.bak=0;38;5;243:*.xlr=0;38;5;186:*.dox=0;38;5;149:*.swf=0;38;5;208:*.tar=4;38;5;203:*.tgz=4;38;5;203:*.cfg=0;38;5;149:*.xml=0;
38;5;185:*.jpg=0;38;5;208:*.mir=0;38;5;48:*.sxi=0;38;5;186:*.bz2=4;38;5;203:*.odt=0;38;5;186:*.mov=0;38;5;208:*.toc=0;38;5;243:*.bat=1;38;5;203:*.asa=0;38;5;48:*.awk=0;38;5;48:*.sbt=0;38;5;48:*.vcd=4;38;5;203:*.kts=0;38;5;48:*.arj=4;38;5;203:*.blg=0;38;5;243:*.c++=0;38;5;48:*.odp=0;38;5;186:*.bbl=0;38;5;243:*.idx=0;38;5;243:*.com=1;38;5;203:*.mp3=0;38;5;208:*.avi=0;38;5;208:*.def=0;38;5;48:*.cgi=0;38;5;48:*.zip=4;38;5;203:*.ttf=0;38;5;208:*.ppt=0;38;5;186:*.tml=0;38;5;149:*.fsx=0;38;5;48:*.h++=0;38;5;48:*.rtf=0;38;5;186:*.inl=0;38;5;48:*.yaml=0;38;5;149:*.html=0;38;5;185:*.mpeg=0;38;5;208:*.java=0;38;5;48:*.hgrc=0;38;5;149:*.orig=0;38;5;243:*.conf=0;38;5;149:*.dart=0;38;5;48:*.psm1=0;38;5;48:*.rlib=0;38;5;243:*.fish=0;38;5;48:*.bash=0;38;5;48:*.make=0;38;5;149:*.docx=0;38;5;186:*.json=0;38;5;149:*.psd1=0;38;5;48:*.lisp=0;38;5;48:*.tbz2=4;38;5;203:*.diff=0;38;5;48:*.epub=0;38;5;186:*.xlsx=0;38;5;186:*.pptx=0;38;5;186:*.toml=0;38;5;149:*.h264=0;38;5;208:*.purs=0;38;5;48:*.flac=0;38;5;208:*.tiff=0;38;5;208:*.jpeg=0;38;5;208:*.lock=0;38;5;243:*.less=0;38;5;48:*.dyn_o=0;38;5;243:*.scala=0;38;5;48:*.mdown=0;38;5;185:*.shtml=0;38;5;185:*.class=0;38;5;243:*.cache=0;38;5;243:*.cmake=0;38;5;149:*passwd=0;38;5;149:*.swift=0;38;5;48:*shadow=0;38;5;149:*.xhtml=0;38;5;185:*.patch=0;38;5;48:*.cabal=0;38;5;48:*README=0;38;5;16;48;5;186:*.toast=4;38;5;203:*.ipynb=0;38;5;48:*COPYING=0;38;5;249:*.gradle=0;38;5;48:*.matlab=0;38;5;48:*.config=0;38;5;149:*LICENSE=0;38;5;249:*.dyn_hi=0;38;5;243:*.flake8=0;38;5;149:*.groovy=0;38;5;48:*INSTALL=0;38;5;16;48;5;186:*TODO.md=1:*.ignore=0;38;5;149:*Doxyfile=0;38;5;149:*TODO.txt=1:*setup.py=0;38;5;149:*Makefile=0;38;5;149:*.gemspec=0;38;5;149:*.desktop=0;38;5;149:*.rgignore=0;38;5;149:*.markdown=0;38;5;185:*COPYRIGHT=0;38;5;249:*configure=0;38;5;149:*.DS_Store=0;38;5;243:*.kdevelop=0;38;5;149:*.fdignore=0;38;5;149:*README.md=0;38;5;16;48;5;186:*.cmake.in=0;38;5;149:*SConscript=0;38;5;149:*CODEOWNERS=0;38;5;149:*.localized=0;38;5;243:*.gitignore=0;38;5;149:*Dockerfile=0;38;5;149:*.gitconfig=0;38;5;149:*INSTALL.md=0;38;5;16;48;5;186:*README.txt=0;38;5;16;48;5;186:*SConstruct=0;38;5;149:*.scons_opt=0;38;5;243:*.travis.yml=0;38;5;186:*.gitmodules=0;38;5;149:*.synctex.gz=0;38;5;243:*LICENSE-MIT=0;38;5;249:*MANIFEST.in=0;38;5;149:*Makefile.in=0;38;5;243:*Makefile.am=0;38;5;149:*INSTALL.txt=0;38;5;16;48;5;186:*configure.ac=0;38;5;149:*.applescript=0;38;5;48:*appveyor.yml=0;38;5;186:*.fdb_latexmk=0;38;5;243:*CONTRIBUTORS=0;38;5;16;48;5;186:*.clang-format=0;38;5;149:*LICENSE-APACHE=0;38;5;249:*CMakeLists.txt=0;38;5;149:*CMakeCache.txt=0;38;5;243:*.gitattributes=0;38;5;149:*CONTRIBUTORS.md=0;38;5;16;48;5;186:*.sconsign.dblite=0;38;5;243:*requirements.txt=0;38;5;149:*CONTRIBUTORS.txt=0;38;5;16;48;5;186:*package-lock.json=0;38;5;243:*.CFUserTextEncoding=0;38;5;243
";

fn main() {
    let result = run();
    match result {
        Ok(exit_code) => {
            exit_code.exit();
        }
        Err(err) => {
            eprintln!("[fd error]: {err:#}");
            ExitCode::GeneralError.exit();
        }
    }
}

fn run() -> Result<ExitCode> {
    let opts = Opts::parse();

    #[cfg(feature = "completions")]
    if let Some(shell) = opts.gen_completions()? {
        return print_completions(shell);
    }

    set_working_dir(&opts)?;
    let search_paths = opts.search_paths()?;
    if search_paths.is_empty() {
        bail!("No valid search paths given.");
    }

    ensure_search_pattern_is_not_a_path(&opts)?;
    let pattern = &opts.pattern;
    let exprs = &opts.exprs;
    let empty = Vec::new();

    let pattern_regexps = exprs
        .as_ref()
        .unwrap_or(&empty)
        .iter()
        .chain([pattern])
        .map(|pat| build_pattern_regex(pat, &opts))
        .collect::<Result<Vec<String>>>()?;

    let config = construct_config(opts, &pattern_regexps)?;

    ensure_use_hidden_option_for_leading_dot_pattern(&config, &pattern_regexps)?;

    let regexps = pattern_regexps
        .into_iter()
        .map(|pat| build_regex(pat, &config))
        .collect::<Result<Vec<Regex>>>()?;

    walk::scan(&search_paths, regexps, config)
}

#[cfg(feature = "completions")]
#[cold]
fn print_completions(shell: clap_complete::Shell) -> Result<ExitCode> {
    // The program name is the first argument.
    let first_arg = env::args().next();
    let program_name = first_arg
        .as_ref()
        .map(Path::new)
        .and_then(|path| path.file_stem())
        .and_then(|file| file.to_str())
        .unwrap_or("fd");
    let mut cmd = Opts::command();
    cmd.build();
    clap_complete::generate(shell, &mut cmd, program_name, &mut std::io::stdout());
    Ok(ExitCode::Success)
}

fn set_working_dir(opts: &Opts) -> Result<()> {
    if let Some(ref base_directory) = opts.base_directory {
        if !filesystem::is_existing_directory(base_directory) {
            return Err(anyhow!(
                "The '--base-directory' path '{}' is not a directory.",
                base_directory.to_string_lossy()
            ));
        }
        env::set_current_dir(base_directory).with_context(|| {
            format!(
                "Could not set '{}' as the current working directory",
                base_directory.to_string_lossy()
            )
        })?;
    }
    Ok(())
}

/// Detect if the user accidentally supplied a path instead of a search pattern
fn ensure_search_pattern_is_not_a_path(opts: &Opts) -> Result<()> {
    if !opts.full_path
        && opts.pattern.contains(std::path::MAIN_SEPARATOR)
        && Path::new(&opts.pattern).is_dir()
    {
        Err(anyhow!(
            "The search pattern '{pattern}' contains a path-separation character ('{sep}') \
             and will not lead to any search results.\n\n\
             If you want to search for all files inside the '{pattern}' directory, use a match-all pattern:\n\n  \
             fd . '{pattern}'\n\n\
             Instead, if you want your pattern to match the full file path, use:\n\n  \
             fd --full-path '{pattern}'",
            pattern = &opts.pattern,
            sep = std::path::MAIN_SEPARATOR,
        ))
    } else {
        Ok(())
    }
}

fn build_pattern_regex(pattern: &str, opts: &Opts) -> Result<String> {
    Ok(if opts.glob && !pattern.is_empty() {
        let glob = GlobBuilder::new(pattern).literal_separator(true).build()?;
        glob.regex().to_owned()
    } else if opts.fixed_strings {
        // Treat pattern as literal string if '--fixed-strings' is used
        regex::escape(pattern)
    } else {
        String::from(pattern)
    })
}

fn check_path_separator_length(path_separator: Option<&str>) -> Result<()> {
    match (cfg!(windows), path_separator) {
        (true, Some(sep)) if sep.len() > 1 => Err(anyhow!(
            "A path separator must be exactly one byte, but \
                 the given separator is {} bytes: '{}'.\n\
                 In some shells on Windows, '/' is automatically \
                 expanded. Try to use '//' instead.",
            sep.len(),
            sep
        )),
        _ => Ok(()),
    }
}

fn construct_config(mut opts: Opts, pattern_regexps: &[String]) -> Result<Config> {
    // The search will be case-sensitive if the command line flag is set or
    // if any of the patterns has an uppercase character (smart case).
    let case_sensitive = !opts.ignore_case
        && (opts.case_sensitive
            || pattern_regexps
                .iter()
                .any(|pat| pattern_has_uppercase_char(pat)));

    let path_separator = opts
        .path_separator
        .take()
        .or_else(filesystem::default_path_separator);
    let actual_path_separator = path_separator
        .clone()
        .unwrap_or_else(|| std::path::MAIN_SEPARATOR.to_string());
    check_path_separator_length(path_separator.as_deref())?;

    let size_limits = std::mem::take(&mut opts.size);
    let time_constraints = extract_time_constraints(&opts)?;
    #[cfg(unix)]
    let owner_constraint: Option<OwnerFilter> = opts.owner.and_then(OwnerFilter::filter_ignore);

    #[cfg(windows)]
    let ansi_colors_support =
        nu_ansi_term::enable_ansi_support().is_ok() || std::env::var_os("TERM").is_some();
    #[cfg(not(windows))]
    let ansi_colors_support = true;

    let interactive_terminal = std::io::stdout().is_terminal();

    let colored_output = match opts.color {
        ColorWhen::Always => true,
        ColorWhen::Never => false,
        ColorWhen::Auto => {
            let no_color = env::var_os("NO_COLOR").is_some_and(|x| !x.is_empty());
            ansi_colors_support && !no_color && interactive_terminal
        }
    };

    let ls_colors = if colored_output {
        Some(LsColors::from_env().unwrap_or_else(|| LsColors::from_string(DEFAULT_LS_COLORS)))
    } else {
        None
    };
    let hyperlink = match opts.hyperlink {
        HyperlinkWhen::Always => true,
        HyperlinkWhen::Never => false,
        HyperlinkWhen::Auto => colored_output,
    };
    let command = extract_command(&mut opts, colored_output)?;
    let has_command = command.is_some();

    let full_path_base = if opts.full_path {
        Some(env::current_dir().context(
            "Could not determine current directory. \
             This is required for --full-path.",
        )?)
    } else {
        None
    };

    Ok(Config {
        case_sensitive,
        full_path_base,
        ignore_hidden: !(opts.hidden || opts.rg_alias_ignore()),
        read_fdignore: !(opts.no_ignore || opts.rg_alias_ignore()),
        read_vcsignore: !(opts.no_ignore || opts.rg_alias_ignore() || opts.no_ignore_vcs),
        require_git_to_read_vcsignore: !opts.no_require_git,
        read_parent_ignore: !opts.no_ignore_parent,
        read_global_ignore: !(opts.no_ignore
            || opts.rg_alias_ignore()
            || opts.no_global_ignore_file),
        follow_links: opts.follow,
        one_file_system: opts.one_file_system,
        null_separator: opts.null_separator,
        quiet: opts.quiet,
        max_depth: opts.max_depth(),
        min_depth: opts.min_depth(),
        prune: opts.prune,
        threads: opts.threads().get(),
        max_buffer_time: opts.max_buffer_time,
        ls_colors,
        hyperlink,
        interactive_terminal,
        file_types: opts.filetype.as_ref().map(|values| {
            use crate::cli::FileType::*;
            let mut file_types = FileTypes::default();
            for value in values {
                match value {
                    File => file_types.files = true,
                    Directory => file_types.directories = true,
                    Symlink => file_types.symlinks = true,
                    Executable => {
                        file_types.executables_only = true;
                        file_types.files = true;
                    }
                    Empty => file_types.empty_only = true,
                    BlockDevice => file_types.block_devices = true,
                    CharDevice => file_types.char_devices = true,
                    Socket => file_types.sockets = true,
                    Pipe => file_types.pipes = true,
                }
            }

            // If only 'empty' was specified, search for both files and directories:
            if file_types.empty_only && !(file_types.files || file_types.directories) {
                file_types.files = true;
                file_types.directories = true;
            }

            file_types
        }),
        extensions: opts
            .extensions
            .as_ref()
            .map(|exts| {
                let patterns = exts
                    .iter()
                    .map(|e| e.trim_start_matches('.'))
                    .map(|e| format!(r".\.{}$", regex::escape(e)));
                RegexSetBuilder::new(patterns)
                    .case_insensitive(true)
                    .build()
            })
            .transpose()?,
        format: opts
            .format
            .as_deref()
            .map(crate::fmt::FormatTemplate::parse),
        command: command.map(Arc::new),
        batch_size: opts.batch_size,
        exclude_patterns: opts.exclude.iter().map(|p| String::from("!") + p).collect(),
        ignore_files: std::mem::take(&mut opts.ignore_file),
        size_constraints: size_limits,
        time_constraints,
        #[cfg(unix)]
        owner_constraint,
        show_filesystem_errors: opts.show_errors,
        path_separator,
        actual_path_separator,
        max_results: opts.max_results(),
        strip_cwd_prefix: opts.strip_cwd_prefix(|| !(opts.null_separator || has_command)),
        ignore_contain: opts.ignore_contain,
    })
}

fn extract_command(opts: &mut Opts, colored_output: bool) -> Result<Option<CommandSet>> {
    opts.exec
        .command
        .take()
        .map(Ok)
        .or_else(|| {
            if !opts.list_details {
                return None;
            }

            let res = determine_ls_command(colored_output)
                .map(|cmd| CommandSet::new_batch([cmd]).unwrap());
            Some(res)
        })
        .transpose()
}

fn determine_ls_command(colored_output: bool) -> Result<Vec<&'static str>> {
    #[allow(unused)]
    let gnu_ls = |command_name| {
        let color_arg = if colored_output {
            "--color=always"
        } else {
            "--color=never"
        };
        // Note: we use short options here (instead of --long-options) to support more
        // platforms (like BusyBox).
        vec![
            command_name,
            "-l", // long listing format
            "-h", // human readable file sizes
            "-d", // list directories themselves, not their contents
            color_arg,
        ]
    };
    let cmd: Vec<&str> = if cfg!(unix) {
        if !cfg!(any(
            target_os = "macos",
            target_os = "dragonfly",
            target_os = "freebsd",
            target_os = "netbsd",
            target_os = "openbsd"
        )) {
            // Assume ls is GNU ls
            gnu_ls("ls")
        } else {
            // MacOS, DragonFlyBSD, FreeBSD
            use std::process::{Command, Stdio};

            // Use GNU ls, if available (support for --color=auto, better LS_COLORS support)
            let gnu_ls_exists = Command::new("gls")
                .arg("--version")
                .stdout(Stdio::null())
                .stderr(Stdio::null())
                .status()
                .is_ok();

            if gnu_ls_exists {
                gnu_ls("gls")
            } else {
                let mut cmd = vec![
                    "ls", // BSD version of ls
                    "-l", // long listing format
                    "-h", // '--human-readable' is not available, '-h' is
                    "-d", // '--directory' is not available, but '-d' is
                ];

                if !cfg!(any(target_os = "netbsd", target_os = "openbsd")) && colored_output {
                    // -G is not available in NetBSD's and OpenBSD's ls
                    cmd.push("-G");
                }

                cmd
            }
        }
    } else if cfg!(windows) {
        use std::process::{Command, Stdio};

        // Use GNU ls, if available
        let gnu_ls_exists = Command::new("ls")
            .arg("--version")
            .stdout(Stdio::null())
            .stderr(Stdio::null())
            .status()
            .is_ok();

        if gnu_ls_exists {
            gnu_ls("ls")
        } else {
            return Err(anyhow!(
                "'fd --list-details' is not supported on Windows unless GNU 'ls' is installed."
            ));
        }
    } else {
        return Err(anyhow!(
            "'fd --list-details' is not supported on this platform."
        ));
    };
    Ok(cmd)
}

fn extract_time_constraints(opts: &Opts) -> Result<Vec<TimeFilter>> {
    let mut time_constraints: Vec<TimeFilter> = Vec::new();
    if let Some(ref t) = opts.changed_within {
        if let Some(f) = TimeFilter::after(t) {
            time_constraints.push(f);
        } else {
            return Err(anyhow!(
                "'{}' is not a valid date or duration. See 'fd --help'.",
                t
            ));
        }
    }
    if let Some(ref t) = opts.changed_before {
        if let Some(f) = TimeFilter::before(t) {
            time_constraints.push(f);
        } else {
            return Err(anyhow!(
                "'{}' is not a valid date or duration. See 'fd --help'.",
                t
            ));
        }
    }
    Ok(time_constraints)
}

fn ensure_use_hidden_option_for_leading_dot_pattern(
    config: &Config,
    pattern_regexps: &[String],
) -> Result<()> {
    if cfg!(unix)
        && config.ignore_hidden
        && pattern_regexps
            .iter()
            .any(|pat| pattern_matches_strings_with_leading_dot(pat))
    {
        Err(anyhow!(
            "The pattern(s) seems to only match files with a leading dot, but hidden files are \
            filtered by default. Consider adding -H/--hidden to search hidden files as well \
            or adjust your search pattern(s)."
        ))
    } else {
        Ok(())
    }
}

fn build_regex(pattern_regex: String, config: &Config) -> Result<regex::bytes::Regex> {
    RegexBuilder::new(&pattern_regex)
        .case_insensitive(!config.case_sensitive)
        .dot_matches_new_line(true)
        .build()
        .map_err(|e| {
            anyhow!(
                "{}\n\nNote: You can use the '--fixed-strings' option to search for a \
                 literal string instead of a regular expression. Alternatively, you can \
                 also use the '--glob' option to match on a glob pattern.",
                e
            )
        })
}
```

## File: `src/output.rs`
```rust
use std::borrow::Cow;
use std::io::{self, Write};

use lscolors::{Indicator, LsColors, Style};

use crate::config::Config;
use crate::dir_entry::DirEntry;
use crate::fmt::FormatTemplate;
use crate::hyperlink::PathUrl;

fn replace_path_separator(path: &str, new_path_separator: &str) -> String {
    path.replace(std::path::MAIN_SEPARATOR, new_path_separator)
}

// TODO: this function is performance critical and can probably be optimized
pub fn print_entry<W: Write>(stdout: &mut W, entry: &DirEntry, config: &Config) -> io::Result<()> {
    let mut has_hyperlink = false;
    if config.hyperlink
        && let Some(url) = PathUrl::new(entry.path())
    {
        write!(stdout, "\x1B]8;;{url}\x1B\\")?;
        has_hyperlink = true;
    }

    if let Some(ref format) = config.format {
        print_entry_format(stdout, entry, config, format)?;
    } else if let Some(ref ls_colors) = config.ls_colors {
        print_entry_colorized(stdout, entry, config, ls_colors)?;
    } else {
        print_entry_uncolorized(stdout, entry, config)?;
    };

    if has_hyperlink {
        write!(stdout, "\x1B]8;;\x1B\\")?;
    }

    if config.null_separator {
        write!(stdout, "\0")
    } else {
        writeln!(stdout)
    }
}

// Display a trailing slash if the path is a directory and the config option is enabled.
// If the path_separator option is set, display that instead.
// The trailing slash will not be colored.
#[inline]
fn print_trailing_slash<W: Write>(
    stdout: &mut W,
    entry: &DirEntry,
    config: &Config,
    style: Option<&Style>,
) -> io::Result<()> {
    if entry.file_type().is_some_and(|ft| ft.is_dir()) {
        write!(
            stdout,
            "{}",
            style
                .map(Style::to_nu_ansi_term_style)
                .unwrap_or_default()
                .paint(&config.actual_path_separator)
        )?;
    }
    Ok(())
}

// TODO: this function is performance critical and can probably be optimized
fn print_entry_format<W: Write>(
    stdout: &mut W,
    entry: &DirEntry,
    config: &Config,
    format: &FormatTemplate,
) -> io::Result<()> {
    let output = format.generate(
        entry.stripped_path(config),
        config.path_separator.as_deref(),
    );
    // TODO: support writing raw bytes on unix?
    write!(stdout, "{}", output.to_string_lossy())
}

// TODO: this function is performance critical and can probably be optimized
fn print_entry_colorized<W: Write>(
    stdout: &mut W,
    entry: &DirEntry,
    config: &Config,
    ls_colors: &LsColors,
) -> io::Result<()> {
    // Split the path between the parent and the last component
    let mut offset = 0;
    let path = entry.stripped_path(config);
    let path_str = path.to_string_lossy();

    if let Some(parent) = path.parent() {
        offset = parent.to_string_lossy().len();
        for c in path_str[offset..].chars() {
            if std::path::is_separator(c) {
                offset += c.len_utf8();
            } else {
                break;
            }
        }
    }

    if offset > 0 {
        let mut parent_str = Cow::from(&path_str[..offset]);
        if let Some(ref separator) = config.path_separator {
            *parent_str.to_mut() = replace_path_separator(&parent_str, separator);
        }

        let style = ls_colors
            .style_for_indicator(Indicator::Directory)
            .map(Style::to_nu_ansi_term_style)
            .unwrap_or_default();
        write!(stdout, "{}", style.paint(parent_str))?;
    }

    let style = entry
        .style(ls_colors)
        .map(Style::to_nu_ansi_term_style)
        .unwrap_or_default();
    write!(stdout, "{}", style.paint(&path_str[offset..]))?;

    print_trailing_slash(
        stdout,
        entry,
        config,
        ls_colors.style_for_indicator(Indicator::Directory),
    )?;

    Ok(())
}

// TODO: this function is performance critical and can probably be optimized
fn print_entry_uncolorized_base<W: Write>(
    stdout: &mut W,
    entry: &DirEntry,
    config: &Config,
) -> io::Result<()> {
    let path = entry.stripped_path(config);

    let mut path_string = path.to_string_lossy();
    if let Some(ref separator) = config.path_separator {
        *path_string.to_mut() = replace_path_separator(&path_string, separator);
    }
    write!(stdout, "{path_string}")?;
    print_trailing_slash(stdout, entry, config, None)
}

#[cfg(not(unix))]
fn print_entry_uncolorized<W: Write>(
    stdout: &mut W,
    entry: &DirEntry,
    config: &Config,
) -> io::Result<()> {
    print_entry_uncolorized_base(stdout, entry, config)
}

#[cfg(unix)]
fn print_entry_uncolorized<W: Write>(
    stdout: &mut W,
    entry: &DirEntry,
    config: &Config,
) -> io::Result<()> {
    use std::os::unix::ffi::OsStrExt;

    if config.interactive_terminal || config.path_separator.is_some() {
        // Fall back to the base implementation
        print_entry_uncolorized_base(stdout, entry, config)
    } else {
        // Print path as raw bytes, allowing invalid UTF-8 filenames to be passed to other processes
        stdout.write_all(entry.stripped_path(config).as_os_str().as_bytes())?;
        print_trailing_slash(stdout, entry, config, None)
    }
}
```

## File: `src/regex_helper.rs`
```rust
use regex_syntax::ParserBuilder;
use regex_syntax::hir::Hir;

/// Determine if a regex pattern contains a literal uppercase character.
pub fn pattern_has_uppercase_char(pattern: &str) -> bool {
    let mut parser = ParserBuilder::new().utf8(false).build();

    parser
        .parse(pattern)
        .map(|hir| hir_has_uppercase_char(&hir))
        .unwrap_or(false)
}

/// Determine if a regex expression contains a literal uppercase character.
fn hir_has_uppercase_char(hir: &Hir) -> bool {
    use regex_syntax::hir::*;

    match hir.kind() {
        HirKind::Literal(Literal(bytes)) => match std::str::from_utf8(bytes) {
            Ok(s) => s.chars().any(|c| c.is_uppercase()),
            Err(_) => bytes.iter().any(|b| char::from(*b).is_uppercase()),
        },
        HirKind::Class(Class::Unicode(ranges)) => ranges
            .iter()
            .any(|r| r.start().is_uppercase() || r.end().is_uppercase()),
        HirKind::Class(Class::Bytes(ranges)) => ranges
            .iter()
            .any(|r| char::from(r.start()).is_uppercase() || char::from(r.end()).is_uppercase()),
        HirKind::Capture(Capture { sub, .. }) | HirKind::Repetition(Repetition { sub, .. }) => {
            hir_has_uppercase_char(sub)
        }
        HirKind::Concat(hirs) | HirKind::Alternation(hirs) => {
            hirs.iter().any(hir_has_uppercase_char)
        }
        _ => false,
    }
}

/// Determine if a regex pattern only matches strings starting with a literal dot (hidden files)
pub fn pattern_matches_strings_with_leading_dot(pattern: &str) -> bool {
    let mut parser = ParserBuilder::new().utf8(false).build();

    parser
        .parse(pattern)
        .map(|hir| hir_matches_strings_with_leading_dot(&hir))
        .unwrap_or(false)
}

/// See above.
fn hir_matches_strings_with_leading_dot(hir: &Hir) -> bool {
    use regex_syntax::hir::*;

    // Note: this only really detects the simplest case where a regex starts with
    // "^\\.", i.e. a start text anchor and a literal dot character. There are a lot
    // of other patterns that ONLY match hidden files, e.g. ^(\\.foo|\\.bar) which are
    // not (yet) detected by this algorithm.
    match hir.kind() {
        HirKind::Concat(hirs) => {
            let mut hirs = hirs.iter();
            if let Some(hir) = hirs.next() {
                if hir.kind() != &HirKind::Look(Look::Start) {
                    return false;
                }
            } else {
                return false;
            }

            if let Some(hir) = hirs.next() {
                match hir.kind() {
                    HirKind::Literal(Literal(bytes)) => bytes.starts_with(b"."),
                    _ => false,
                }
            } else {
                false
            }
        }
        _ => false,
    }
}

#[test]
fn pattern_has_uppercase_char_simple() {
    assert!(pattern_has_uppercase_char("A"));
    assert!(pattern_has_uppercase_char("foo.EXE"));

    assert!(!pattern_has_uppercase_char("a"));
    assert!(!pattern_has_uppercase_char("foo.exe123"));
}

#[test]
fn pattern_has_uppercase_char_advanced() {
    assert!(pattern_has_uppercase_char("foo.[a-zA-Z]"));

    assert!(!pattern_has_uppercase_char(r"\Acargo"));
    assert!(!pattern_has_uppercase_char(r"carg\x6F"));
}

#[test]
fn matches_strings_with_leading_dot_simple() {
    assert!(pattern_matches_strings_with_leading_dot("^\\.gitignore"));

    assert!(!pattern_matches_strings_with_leading_dot("^.gitignore"));
    assert!(!pattern_matches_strings_with_leading_dot("\\.gitignore"));
    assert!(!pattern_matches_strings_with_leading_dot("^gitignore"));
}
```

## File: `src/walk.rs`
```rust
use std::borrow::Cow;
use std::ffi::OsStr;
use std::io::{self, Write};
use std::mem;
use std::path::PathBuf;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{Arc, Mutex, MutexGuard};
use std::thread;
use std::time::{Duration, Instant};

use anyhow::{Result, anyhow};
use crossbeam_channel::{Receiver, RecvTimeoutError, SendError, Sender, bounded};
use etcetera::BaseStrategy;
use ignore::overrides::{Override, OverrideBuilder};
use ignore::{WalkBuilder, WalkParallel, WalkState};
use regex::bytes::Regex;

use crate::config::Config;
use crate::dir_entry::DirEntry;
use crate::error::print_error;
use crate::exec;
use crate::exit_codes::{ExitCode, merge_exitcodes};
use crate::filesystem;
use crate::output;

/// The receiver thread can either be buffering results or directly streaming to the console.
#[derive(PartialEq)]
enum ReceiverMode {
    /// Receiver is still buffering in order to sort the results, if the search finishes fast
    /// enough.
    Buffering,

    /// Receiver is directly printing results to the output.
    Streaming,
}

/// The Worker threads can result in a valid entry having PathBuf or an error.
#[allow(clippy::large_enum_variant)]
#[derive(Debug)]
pub enum WorkerResult {
    // Errors should be rare, so it's probably better to allow large_enum_variant than
    // to box the Entry variant
    Entry(DirEntry),
    Error(ignore::Error),
}

/// A batch of WorkerResults to send over a channel.
#[derive(Clone)]
struct Batch {
    items: Arc<Mutex<Option<Vec<WorkerResult>>>>,
}

impl Batch {
    fn new() -> Self {
        Self {
            items: Arc::new(Mutex::new(Some(vec![]))),
        }
    }

    fn lock(&self) -> MutexGuard<'_, Option<Vec<WorkerResult>>> {
        self.items.lock().unwrap()
    }
}

impl IntoIterator for Batch {
    type Item = WorkerResult;
    type IntoIter = std::vec::IntoIter<WorkerResult>;

    fn into_iter(self) -> Self::IntoIter {
        self.lock().take().unwrap().into_iter()
    }
}

/// Wrapper that sends batches of items at once over a channel.
struct BatchSender {
    batch: Batch,
    tx: Sender<Batch>,
    limit: usize,
}

impl BatchSender {
    fn new(tx: Sender<Batch>, limit: usize) -> Self {
        Self {
            batch: Batch::new(),
            tx,
            limit,
        }
    }

    /// Check if we need to flush a batch.
    fn needs_flush(&self, batch: Option<&Vec<WorkerResult>>) -> bool {
        match batch {
            // Limit the batch size to provide some backpressure
            Some(vec) => vec.len() >= self.limit,
            // Batch was already taken by the receiver, so make a new one
            None => true,
        }
    }

    /// Add an item to a batch.
    fn send(&mut self, item: WorkerResult) -> Result<(), SendError<()>> {
        let mut batch = self.batch.lock();

        if self.needs_flush(batch.as_ref()) {
            drop(batch);
            self.batch = Batch::new();
            batch = self.batch.lock();
        }

        let items = batch.as_mut().unwrap();
        items.push(item);

        if items.len() == 1 {
            // New batch, send it over the channel
            self.tx
                .send(self.batch.clone())
                .map_err(|_| SendError(()))?;
        }

        Ok(())
    }
}

/// Maximum size of the output buffer before flushing results to the console
const MAX_BUFFER_LENGTH: usize = 1000;
/// Default duration until output buffering switches to streaming.
const DEFAULT_MAX_BUFFER_TIME: Duration = Duration::from_millis(100);

/// Wrapper for the receiver thread's buffering behavior.
struct ReceiverBuffer<'a, W> {
    /// The configuration.
    config: &'a Config,
    /// For shutting down the senders.
    quit_flag: &'a AtomicBool,
    /// The ^C notifier.
    interrupt_flag: &'a AtomicBool,
    /// Receiver for worker results.
    rx: Receiver<Batch>,
    /// Standard output.
    stdout: W,
    /// The current buffer mode.
    mode: ReceiverMode,
    /// The deadline to switch to streaming mode.
    deadline: Instant,
    /// The buffer of quickly received paths.
    buffer: Vec<DirEntry>,
    /// Result count.
    num_results: usize,
}

impl<'a, W: Write> ReceiverBuffer<'a, W> {
    /// Create a new receiver buffer.
    fn new(state: &'a WorkerState, rx: Receiver<Batch>, stdout: W) -> Self {
        let config = &state.config;
        let quit_flag = state.quit_flag.as_ref();
        let interrupt_flag = state.interrupt_flag.as_ref();
        let max_buffer_time = config.max_buffer_time.unwrap_or(DEFAULT_MAX_BUFFER_TIME);
        let deadline = Instant::now() + max_buffer_time;

        Self {
            config,
            quit_flag,
            interrupt_flag,
            rx,
            stdout,
            mode: ReceiverMode::Buffering,
            deadline,
            buffer: Vec::with_capacity(MAX_BUFFER_LENGTH),
            num_results: 0,
        }
    }

    /// Process results until finished.
    fn process(&mut self) -> ExitCode {
        loop {
            if let Err(ec) = self.poll() {
                self.quit_flag.store(true, Ordering::Relaxed);
                return ec;
            }
        }
    }

    /// Receive the next worker result.
    fn recv(&self) -> Result<Batch, RecvTimeoutError> {
        match self.mode {
            ReceiverMode::Buffering => {
                // Wait at most until we should switch to streaming
                self.rx.recv_deadline(self.deadline)
            }
            ReceiverMode::Streaming => {
                // Wait however long it takes for a result
                Ok(self.rx.recv()?)
            }
        }
    }

    /// Wait for a result or state change.
    fn poll(&mut self) -> Result<(), ExitCode> {
        match self.recv() {
            Ok(batch) => {
                for result in batch {
                    match result {
                        WorkerResult::Entry(dir_entry) => {
                            if self.config.quiet {
                                return Err(ExitCode::HasResults(true));
                            }

                            match self.mode {
                                ReceiverMode::Buffering => {
                                    self.buffer.push(dir_entry);
                                    if self.buffer.len() > MAX_BUFFER_LENGTH {
                                        self.stream()?;
                                    }
                                }
                                ReceiverMode::Streaming => {
                                    self.print(&dir_entry)?;
                                }
                            }

                            self.num_results += 1;
                            if let Some(max_results) = self.config.max_results
                                && self.num_results >= max_results
                            {
                                return self.stop();
                            }
                        }
                        WorkerResult::Error(err) => {
                            if self.config.show_filesystem_errors {
                                print_error(err.to_string());
                            }
                        }
                    }
                }

                // If we don't have another batch ready, flush before waiting
                if self.mode == ReceiverMode::Streaming && self.rx.is_empty() {
                    self.flush()?;
                }
            }
            Err(RecvTimeoutError::Timeout) => {
                self.stream()?;
            }
            Err(RecvTimeoutError::Disconnected) => {
                return self.stop();
            }
        }

        Ok(())
    }

    /// Output a path.
    fn print(&mut self, entry: &DirEntry) -> Result<(), ExitCode> {
        if let Err(e) = output::print_entry(&mut self.stdout, entry, self.config)
            && e.kind() != ::std::io::ErrorKind::BrokenPipe
        {
            print_error(format!("Could not write to output: {e}"));
            return Err(ExitCode::GeneralError);
        }

        if self.interrupt_flag.load(Ordering::Relaxed) {
            // Ignore any errors on flush, because we're about to exit anyway
            let _ = self.flush();
            return Err(ExitCode::KilledBySigint);
        }

        Ok(())
    }

    /// Switch ourselves into streaming mode.
    fn stream(&mut self) -> Result<(), ExitCode> {
        self.mode = ReceiverMode::Streaming;

        let buffer = mem::take(&mut self.buffer);
        for path in buffer {
            self.print(&path)?;
        }

        self.flush()
    }

    /// Stop looping.
    fn stop(&mut self) -> Result<(), ExitCode> {
        if self.mode == ReceiverMode::Buffering {
            self.buffer.sort();
            self.stream()?;
        }

        if self.config.quiet {
            Err(ExitCode::HasResults(self.num_results > 0))
        } else {
            Err(ExitCode::Success)
        }
    }

    /// Flush stdout if necessary.
    fn flush(&mut self) -> Result<(), ExitCode> {
        if self.stdout.flush().is_err() {
            // Probably a broken pipe. Exit gracefully.
            return Err(ExitCode::GeneralError);
        }
        Ok(())
    }
}

/// State shared by the sender and receiver threads.
struct WorkerState {
    /// The search patterns.
    patterns: Vec<Regex>,
    /// The command line configuration.
    config: Config,
    /// Flag for cleanly shutting down the parallel walk
    quit_flag: Arc<AtomicBool>,
    /// Flag specifically for quitting due to ^C
    interrupt_flag: Arc<AtomicBool>,
}

impl WorkerState {
    fn new(patterns: Vec<Regex>, config: Config) -> Self {
        let quit_flag = Arc::new(AtomicBool::new(false));
        let interrupt_flag = Arc::new(AtomicBool::new(false));

        Self {
            patterns,
            config,
            quit_flag,
            interrupt_flag,
        }
    }

    fn build_overrides(&self, paths: &[PathBuf]) -> Result<Override> {
        let first_path = &paths[0];
        let config = &self.config;

        let mut builder = OverrideBuilder::new(first_path);

        for pattern in &config.exclude_patterns {
            builder
                .add(pattern)
                .map_err(|e| anyhow!("Malformed exclude pattern: {}", e))?;
        }

        builder
            .build()
            .map_err(|_| anyhow!("Mismatch in exclude patterns"))
    }

    fn build_walker(&self, paths: &[PathBuf]) -> Result<WalkParallel> {
        let first_path = &paths[0];
        let config = &self.config;
        let overrides = self.build_overrides(paths)?;

        let mut builder = WalkBuilder::new(first_path);
        builder
            .hidden(config.ignore_hidden)
            .ignore(config.read_fdignore)
            .parents(config.read_parent_ignore && (config.read_fdignore || config.read_vcsignore))
            .git_ignore(config.read_vcsignore)
            .git_global(config.read_vcsignore)
            .git_exclude(config.read_vcsignore)
            .require_git(config.require_git_to_read_vcsignore)
            .overrides(overrides)
            .follow_links(config.follow_links)
            // No need to check for supported platforms, option is unavailable on unsupported ones
            .same_file_system(config.one_file_system)
            .max_depth(config.max_depth);

        if config.read_fdignore {
            builder.add_custom_ignore_filename(".fdignore");
        }

        if config.read_global_ignore
            && let Ok(basedirs) = etcetera::choose_base_strategy()
        {
            let global_ignore_file = basedirs.config_dir().join("fd").join("ignore");
            if global_ignore_file.is_file() {
                let result = builder.add_ignore(global_ignore_file);
                match result {
                    Some(ignore::Error::Partial(_)) => (),
                    Some(err) => {
                        print_error(format!("Malformed pattern in global ignore file. {err}."));
                    }
                    None => (),
                }
            }
        }

        for ignore_file in &config.ignore_files {
            let result = builder.add_ignore(ignore_file);
            match result {
                Some(ignore::Error::Partial(_)) => (),
                Some(err) => {
                    print_error(format!("Malformed pattern in custom ignore file. {err}."));
                }
                None => (),
            }
        }

        for path in &paths[1..] {
            builder.add(path);
        }

        let walker = builder.threads(config.threads).build_parallel();
        Ok(walker)
    }

    /// Run the receiver work, either on this thread or a pool of background
    /// threads (for --exec).
    fn receive(&self, rx: Receiver<Batch>) -> ExitCode {
        let config = &self.config;

        // This will be set to `Some` if the `--exec` argument was supplied.
        if let Some(ref cmd) = config.command {
            if cmd.in_batch_mode() {
                exec::batch(rx.into_iter().flatten(), cmd, config)
            } else {
                thread::scope(|scope| {
                    // Each spawned job will store its thread handle in here.
                    let threads = config.threads;
                    let mut handles = Vec::with_capacity(threads);
                    for _ in 0..threads {
                        let rx = rx.clone();

                        // Spawn a job thread that will listen for and execute inputs.
                        let handle =
                            scope.spawn(|| exec::job(rx.into_iter().flatten(), cmd, config));

                        // Push the handle of the spawned thread into the vector for later joining.
                        handles.push(handle);
                    }
                    let exit_codes = handles.into_iter().map(|handle| handle.join().unwrap());
                    merge_exitcodes(exit_codes)
                })
            }
        } else {
            let stdout = io::stdout().lock();
            let stdout = io::BufWriter::new(stdout);

            ReceiverBuffer::new(self, rx, stdout).process()
        }
    }

    /// Spawn the sender threads.
    fn spawn_senders(&self, walker: WalkParallel, tx: Sender<Batch>) {
        walker.run(|| {
            let patterns = &self.patterns;
            let config = &self.config;
            let quit_flag = self.quit_flag.as_ref();

            let mut limit = 0x100;
            if let Some(cmd) = &config.command
                && !cmd.in_batch_mode()
                && config.threads > 1
            {
                // Evenly distribute work between multiple receivers
                limit = 1;
            }
            let mut tx = BatchSender::new(tx.clone(), limit);

            Box::new(move |entry| {
                if quit_flag.load(Ordering::Relaxed) {
                    return WalkState::Quit;
                }

                if let Ok(e) = &entry {
                    // If the entry is a directory that contains a
                    // "ignore contain" file", we want to skip this
                    // directory.
                    // Check the filetype first to avoid unnecessary
                    // syscalls.
                    if e.file_type().is_some_and(|t| t.is_dir()) {
                        let entry_path = e.path();
                        if config
                            .ignore_contain
                            .iter()
                            .any(|ic| entry_path.join(ic).exists())
                        {
                            return WalkState::Skip;
                        }
                    }
                    if e.depth() == 0 {
                        // Skip the root directory entry.
                        return WalkState::Continue;
                    }
                }
                let entry = match entry {
                    Ok(e) => DirEntry::normal(e),
                    Err(ignore::Error::WithPath {
                        path,
                        err: inner_err,
                    }) => match inner_err.as_ref() {
                        ignore::Error::Io(io_error)
                            if io_error.kind() == io::ErrorKind::NotFound
                                && path
                                    .symlink_metadata()
                                    .ok()
                                    .is_some_and(|m| m.file_type().is_symlink()) =>
                        {
                            DirEntry::broken_symlink(path)
                        }
                        _ => {
                            return match tx.send(WorkerResult::Error(ignore::Error::WithPath {
                                path,
                                err: inner_err,
                            })) {
                                Ok(_) => WalkState::Continue,
                                Err(_) => WalkState::Quit,
                            };
                        }
                    },
                    Err(err) => {
                        return match tx.send(WorkerResult::Error(err)) {
                            Ok(_) => WalkState::Continue,
                            Err(_) => WalkState::Quit,
                        };
                    }
                };

                if let Some(min_depth) = config.min_depth
                    && entry.depth().is_none_or(|d| d < min_depth)
                {
                    return WalkState::Continue;
                }

                // Check the name first, since it doesn't require metadata
                let entry_path = entry.path();

                let search_str = search_str_for_entry(entry_path, config.full_path_base.as_deref());

                if !patterns
                    .iter()
                    .all(|pat| pat.is_match(&filesystem::osstr_to_bytes(search_str.as_ref())))
                {
                    return WalkState::Continue;
                }

                // Filter out unwanted extensions.
                if let Some(ref exts_regex) = config.extensions {
                    if let Some(path_str) = entry_path.file_name() {
                        if !exts_regex.is_match(&filesystem::osstr_to_bytes(path_str)) {
                            return WalkState::Continue;
                        }
                    } else {
                        return WalkState::Continue;
                    }
                }

                // Filter out unwanted file types.
                if let Some(ref file_types) = config.file_types
                    && file_types.should_ignore(&entry)
                {
                    return WalkState::Continue;
                }

                #[cfg(unix)]
                {
                    if let Some(ref owner_constraint) = config.owner_constraint {
                        if let Some(metadata) = entry.metadata() {
                            if !owner_constraint.matches(metadata) {
                                return WalkState::Continue;
                            }
                        } else {
                            return WalkState::Continue;
                        }
                    }
                }

                // Filter out unwanted sizes if it is a file and we have been given size constraints.
                if !config.size_constraints.is_empty() {
                    if entry_path.is_file() {
                        if let Some(metadata) = entry.metadata() {
                            let file_size = metadata.len();
                            if config
                                .size_constraints
                                .iter()
                                .any(|sc| !sc.is_within(file_size))
                            {
                                return WalkState::Continue;
                            }
                        } else {
                            return WalkState::Continue;
                        }
                    } else {
                        return WalkState::Continue;
                    }
                }

                // Filter out unwanted modification times
                if !config.time_constraints.is_empty() {
                    let mut matched = false;
                    if let Some(metadata) = entry.metadata()
                        && let Ok(modified) = metadata.modified()
                    {
                        matched = config
                            .time_constraints
                            .iter()
                            .all(|tf| tf.applies_to(&modified));
                    }
                    if !matched {
                        return WalkState::Continue;
                    }
                }

                if config.is_printing()
                    && let Some(ls_colors) = &config.ls_colors
                {
                    // Compute colors in parallel
                    entry.style(ls_colors);
                }

                let send_result = tx.send(WorkerResult::Entry(entry));

                if send_result.is_err() {
                    return WalkState::Quit;
                }

                // Apply pruning.
                if config.prune {
                    return WalkState::Skip;
                }

                WalkState::Continue
            })
        });
    }

    /// Perform the recursive scan.
    fn scan(&self, paths: &[PathBuf]) -> Result<ExitCode> {
        let config = &self.config;
        let walker = self.build_walker(paths)?;

        if config.ls_colors.is_some() && config.is_printing() {
            let quit_flag = Arc::clone(&self.quit_flag);
            let interrupt_flag = Arc::clone(&self.interrupt_flag);

            ctrlc::set_handler(move || {
                quit_flag.store(true, Ordering::Relaxed);

                if interrupt_flag.fetch_or(true, Ordering::Relaxed) {
                    // Ctrl-C has been pressed twice, exit NOW
                    ExitCode::KilledBySigint.exit();
                }
            })
            .unwrap();
        }

        let (tx, rx) = bounded(2 * config.threads);

        let exit_code = thread::scope(|scope| {
            // Spawn the receiver thread(s)
            let receiver = scope.spawn(|| self.receive(rx));

            // Spawn the sender threads.
            self.spawn_senders(walker, tx);

            receiver.join().unwrap()
        });

        if self.interrupt_flag.load(Ordering::Relaxed) {
            Ok(ExitCode::KilledBySigint)
        } else {
            Ok(exit_code)
        }
    }
}

fn search_str_for_entry<'a>(
    entry_path: &'a std::path::Path,
    full_path_base: Option<&std::path::Path>,
) -> Cow<'a, OsStr> {
    if let Some(cwd) = full_path_base {
        // If full_path_base is some, that means that we need to return
        // the absolute path
        if entry_path.is_absolute() {
            return Cow::Borrowed(entry_path.as_os_str());
        }
        let path = entry_path.strip_prefix(".").unwrap_or(entry_path);
        Cow::Owned(cwd.join(path).into())
    } else {
        match entry_path.file_name() {
            Some(filename) => Cow::Borrowed(filename),
            None => unreachable!(
                "Encountered file system entry without a file name. This should only \
                 happen for paths like 'foo/bar/..' or '/' which are not supposed to \
                 appear in a file system traversal."
            ),
        }
    }
}

/// Recursively scan the given search path for files / pathnames matching the patterns.
///
/// If the `--exec` argument was supplied, this will create a thread pool for executing
/// jobs in parallel from a given command line and the discovered paths. Otherwise, each
/// path will simply be written to standard output.
pub fn scan(paths: &[PathBuf], patterns: Vec<Regex>, config: Config) -> Result<ExitCode> {
    WorkerState::new(patterns, config).scan(paths)
}

#[cfg(test)]
mod tests {
    use super::search_str_for_entry;
    use std::path::{Path, PathBuf};

    #[test]
    fn search_str_for_entry_with_relative_path() {
        let full_path_base = Some(Path::new("/home/user"));
        assert_eq!(
            search_str_for_entry(Path::new("foo/bar"), full_path_base),
            PathBuf::from("/home/user/foo/bar")
        );
    }

    #[test]
    fn search_str_for_entry_strips_dot_prefix() {
        let full_path_base = Some(Path::new("/home/user"));
        assert_eq!(
            search_str_for_entry(Path::new("./foo/bar"), full_path_base),
            PathBuf::from("/home/user/foo/bar")
        );
    }

    #[test]
    fn search_str_for_entry_with_absolute_path() {
        let full_path_base = Some(Path::new("/home/user"));
        assert_eq!(
            search_str_for_entry(Path::new("/absolute/path"), full_path_base),
            PathBuf::from("/absolute/path")
        );
    }

    #[test]
    fn search_str_no_base_dir() {
        assert_eq!(
            search_str_for_entry(Path::new("./foo/bar"), None),
            PathBuf::from("bar")
        );
    }
}
```

## File: `src/exec/command.rs`
```rust
use std::io;
use std::io::Write;

use argmax::Command;

use crate::error::print_error;
use crate::exit_codes::ExitCode;

struct Outputs {
    stdout: Vec<u8>,
    stderr: Vec<u8>,
}
pub struct OutputBuffer {
    null_separator: bool,
    outputs: Vec<Outputs>,
}

impl OutputBuffer {
    pub fn new(null_separator: bool) -> Self {
        Self {
            null_separator,
            outputs: Vec::new(),
        }
    }

    fn push(&mut self, stdout: Vec<u8>, stderr: Vec<u8>) {
        self.outputs.push(Outputs { stdout, stderr });
    }

    fn write(self) {
        // Avoid taking the lock if there is nothing to do.
        // If null_separator is true, then we still need to write the
        // null separator, because the output may have been written directly
        // to stdout
        if self.outputs.is_empty() && !self.null_separator {
            return;
        }

        let stdout = io::stdout();
        let stderr = io::stderr();

        // While we hold these locks, only this thread will be able
        // to write its outputs.
        let mut stdout = stdout.lock();
        let mut stderr = stderr.lock();

        for output in self.outputs.iter() {
            let _ = stdout.write_all(&output.stdout);
            let _ = stderr.write_all(&output.stderr);
        }
        if self.null_separator {
            // If null_separator is enabled, then we should write a \0 at the end
            // of the output for this entry
            let _ = stdout.write_all(b"\0");
        }
    }
}

/// Executes a command.
pub fn execute_commands<I: Iterator<Item = io::Result<Command>>>(
    cmds: I,
    mut output_buffer: OutputBuffer,
    enable_output_buffering: bool,
) -> ExitCode {
    for result in cmds {
        let mut cmd = match result {
            Ok(cmd) => cmd,
            Err(e) => return handle_cmd_error(None, e),
        };

        // Spawn the supplied command.
        let output = if enable_output_buffering {
            cmd.output()
        } else {
            // If running on only one thread, don't buffer output
            // Allows for viewing and interacting with intermediate command output
            cmd.spawn().and_then(|c| c.wait_with_output())
        };

        // Then wait for the command to exit, if it was spawned.
        match output {
            Ok(output) => {
                if enable_output_buffering {
                    output_buffer.push(output.stdout, output.stderr);
                }
                if output.status.code() != Some(0) {
                    output_buffer.write();
                    return ExitCode::GeneralError;
                }
            }
            Err(why) => {
                output_buffer.write();
                return handle_cmd_error(Some(&cmd), why);
            }
        }
    }
    output_buffer.write();
    ExitCode::Success
}

pub fn handle_cmd_error(cmd: Option<&Command>, err: io::Error) -> ExitCode {
    match (cmd, err) {
        (Some(cmd), err) if err.kind() == io::ErrorKind::NotFound => {
            print_error(format!(
                "Command not found: {}",
                cmd.get_program().to_string_lossy()
            ));
            ExitCode::GeneralError
        }
        (_, err) => {
            print_error(format!("Problem while executing command: {err}"));
            ExitCode::GeneralError
        }
    }
}
```

## File: `src/exec/job.rs`
```rust
use crate::config::Config;
use crate::error::print_error;
use crate::exit_codes::{ExitCode, merge_exitcodes};
use crate::walk::WorkerResult;

use super::CommandSet;

/// An event loop that listens for inputs from the `rx` receiver. Each received input will
/// generate a command with the supplied command template. The generated command will then
/// be executed, and this process will continue until the receiver's sender has closed.
pub fn job(
    results: impl IntoIterator<Item = WorkerResult>,
    cmd: &CommandSet,
    config: &Config,
) -> ExitCode {
    // Output should be buffered when only running a single thread
    let buffer_output: bool = config.threads > 1;

    let mut ret = ExitCode::Success;
    for result in results {
        // Obtain the next result from the receiver, else if the channel
        // has closed, exit from the loop
        let dir_entry = match result {
            WorkerResult::Entry(dir_entry) => dir_entry,
            WorkerResult::Error(err) => {
                if config.show_filesystem_errors {
                    print_error(err.to_string());
                }
                continue;
            }
        };

        // Generate a command, execute it and store its exit code.
        let code = cmd.execute(
            dir_entry.stripped_path(config),
            config.path_separator.as_deref(),
            config.null_separator,
            buffer_output,
        );
        ret = merge_exitcodes([ret, code]);
    }
    // Returns error in case of any error.
    ret
}

pub fn batch(
    results: impl IntoIterator<Item = WorkerResult>,
    cmd: &CommandSet,
    config: &Config,
) -> ExitCode {
    let paths = results
        .into_iter()
        .filter_map(|worker_result| match worker_result {
            WorkerResult::Entry(dir_entry) => Some(dir_entry.into_stripped_path(config)),
            WorkerResult::Error(err) => {
                if config.show_filesystem_errors {
                    print_error(err.to_string());
                }
                None
            }
        });

    cmd.execute_batch(paths, config.batch_size, config.path_separator.as_deref())
}
```

## File: `src/exec/mod.rs`
```rust
mod command;
mod job;

use std::ffi::OsString;
use std::io;
use std::iter;
use std::path::{Path, PathBuf};
use std::process::Stdio;

use anyhow::{Result, bail};
use argmax::Command;

use crate::exec::command::OutputBuffer;
use crate::exit_codes::{ExitCode, merge_exitcodes};
use crate::fmt::{FormatTemplate, Token};

use self::command::{execute_commands, handle_cmd_error};
pub use self::job::{batch, job};

/// Execution mode of the command
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ExecutionMode {
    /// Command is executed for each search result
    OneByOne,
    /// Command is run for a batch of results at once
    Batch,
}

#[derive(Debug, Clone, PartialEq)]
pub struct CommandSet {
    mode: ExecutionMode,
    commands: Vec<CommandTemplate>,
}

impl CommandSet {
    pub fn new<I, T, S>(input: I) -> Result<CommandSet>
    where
        I: IntoIterator<Item = T>,
        T: IntoIterator<Item = S>,
        S: AsRef<str>,
    {
        Ok(CommandSet {
            mode: ExecutionMode::OneByOne,
            commands: input
                .into_iter()
                .map(CommandTemplate::new)
                .collect::<Result<_>>()?,
        })
    }

    pub fn new_batch<I, T, S>(input: I) -> Result<CommandSet>
    where
        I: IntoIterator<Item = T>,
        T: IntoIterator<Item = S>,
        S: AsRef<str>,
    {
        Ok(CommandSet {
            mode: ExecutionMode::Batch,
            commands: input
                .into_iter()
                .map(|args| {
                    let cmd = CommandTemplate::new(args)?;
                    if cmd.number_of_tokens() > 1 {
                        bail!("Only one placeholder allowed for batch commands");
                    }
                    if cmd.args[0].has_tokens() {
                        bail!("First argument of exec-batch is expected to be a fixed executable");
                    }
                    Ok(cmd)
                })
                .collect::<Result<Vec<_>>>()?,
        })
    }

    pub fn in_batch_mode(&self) -> bool {
        self.mode == ExecutionMode::Batch
    }

    pub fn execute(
        &self,
        input: &Path,
        path_separator: Option<&str>,
        null_separator: bool,
        buffer_output: bool,
    ) -> ExitCode {
        let commands = self
            .commands
            .iter()
            .map(|c| c.generate(input, path_separator));
        execute_commands(commands, OutputBuffer::new(null_separator), buffer_output)
    }

    pub fn execute_batch<I>(&self, paths: I, limit: usize, path_separator: Option<&str>) -> ExitCode
    where
        I: Iterator<Item = PathBuf>,
    {
        let builders: io::Result<Vec<_>> = self
            .commands
            .iter()
            .map(|c| CommandBuilder::new(c, limit))
            .collect();

        match builders {
            Ok(mut builders) => {
                for path in paths {
                    for builder in &mut builders {
                        if let Err(e) = builder.push(&path, path_separator) {
                            return handle_cmd_error(Some(&builder.cmd), e);
                        }
                    }
                }

                for builder in &mut builders {
                    if let Err(e) = builder.finish() {
                        return handle_cmd_error(Some(&builder.cmd), e);
                    }
                }

                merge_exitcodes(builders.iter().map(|b| b.exit_code()))
            }
            Err(e) => handle_cmd_error(None, e),
        }
    }
}

/// Represents a multi-exec command as it is built.
#[derive(Debug)]
struct CommandBuilder {
    pre_args: Vec<OsString>,
    path_arg: FormatTemplate,
    post_args: Vec<OsString>,
    cmd: Command,
    count: usize,
    limit: usize,
    exit_code: ExitCode,
}

impl CommandBuilder {
    fn new(template: &CommandTemplate, limit: usize) -> io::Result<Self> {
        let mut pre_args = vec![];
        let mut path_arg = None;
        let mut post_args = vec![];

        for arg in &template.args {
            if arg.has_tokens() {
                path_arg = Some(arg.clone());
            } else if path_arg.is_none() {
                pre_args.push(arg.generate("", None));
            } else {
                post_args.push(arg.generate("", None));
            }
        }

        let cmd = Self::new_command(&pre_args)?;

        Ok(Self {
            pre_args,
            path_arg: path_arg.unwrap(),
            post_args,
            cmd,
            count: 0,
            limit,
            exit_code: ExitCode::Success,
        })
    }

    fn new_command(pre_args: &[OsString]) -> io::Result<Command> {
        let mut cmd = Command::new(&pre_args[0]);
        cmd.stdin(Stdio::inherit());
        cmd.stdout(Stdio::inherit());
        cmd.stderr(Stdio::inherit());
        cmd.try_args(&pre_args[1..])?;
        Ok(cmd)
    }

    fn push(&mut self, path: &Path, separator: Option<&str>) -> io::Result<()> {
        if self.limit > 0 && self.count >= self.limit {
            self.finish()?;
        }

        let arg = self.path_arg.generate(path, separator);
        if !self
            .cmd
            .args_would_fit(iter::once(&arg).chain(&self.post_args))
        {
            self.finish()?;
        }

        self.cmd.try_arg(arg)?;
        self.count += 1;
        Ok(())
    }

    fn finish(&mut self) -> io::Result<()> {
        if self.count > 0 {
            self.cmd.try_args(&self.post_args)?;
            if !self.cmd.status()?.success() {
                self.exit_code = ExitCode::GeneralError;
            }

            self.cmd = Self::new_command(&self.pre_args)?;
            self.count = 0;
        }

        Ok(())
    }

    fn exit_code(&self) -> ExitCode {
        self.exit_code
    }
}

/// Represents a template that is utilized to generate command strings.
///
/// The template is meant to be coupled with an input in order to generate a command. The
/// `generate_and_execute()` method will be used to generate a command and execute it.
#[derive(Debug, Clone, PartialEq)]
struct CommandTemplate {
    args: Vec<FormatTemplate>,
}

impl CommandTemplate {
    fn new<I, S>(input: I) -> Result<CommandTemplate>
    where
        I: IntoIterator<Item = S>,
        S: AsRef<str>,
    {
        let mut args = Vec::new();
        let mut has_placeholder = false;

        for arg in input {
            let arg = arg.as_ref();

            let tmpl = FormatTemplate::parse(arg);
            has_placeholder |= tmpl.has_tokens();
            args.push(tmpl);
        }

        // We need to check that we have at least one argument, because if not
        // it will try to execute each file and directory it finds.
        //
        // Sadly, clap can't currently handle this for us, see
        // https://github.com/clap-rs/clap/issues/3542
        if args.is_empty() {
            bail!("No executable provided for --exec or --exec-batch");
        }

        // If a placeholder token was not supplied, append one at the end of the command.
        if !has_placeholder {
            args.push(FormatTemplate::Tokens(vec![Token::Placeholder]));
        }

        Ok(CommandTemplate { args })
    }

    fn number_of_tokens(&self) -> usize {
        self.args.iter().filter(|arg| arg.has_tokens()).count()
    }

    /// Generates and executes a command.
    ///
    /// Using the internal `args` field, and a supplied `input` variable, a `Command` will be
    /// build.
    fn generate(&self, input: &Path, path_separator: Option<&str>) -> io::Result<Command> {
        let mut cmd = Command::new(self.args[0].generate(input, path_separator));
        for arg in &self.args[1..] {
            cmd.try_arg(arg.generate(input, path_separator))?;
        }
        Ok(cmd)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn generate_str(template: &CommandTemplate, input: &str) -> Vec<String> {
        template
            .args
            .iter()
            .map(|arg| arg.generate(input, None).into_string().unwrap())
            .collect()
    }

    #[test]
    fn tokens_with_placeholder() {
        assert_eq!(
            CommandSet::new(vec![vec![&"echo", &"${SHELL}:"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("echo".into()),
                        FormatTemplate::Text("${SHELL}:".into()),
                        FormatTemplate::Tokens(vec![Token::Placeholder]),
                    ]
                }],
                mode: ExecutionMode::OneByOne,
            }
        );
    }

    #[test]
    fn tokens_with_no_extension() {
        assert_eq!(
            CommandSet::new(vec![vec!["echo", "{.}"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("echo".into()),
                        FormatTemplate::Tokens(vec![Token::NoExt]),
                    ],
                }],
                mode: ExecutionMode::OneByOne,
            }
        );
    }

    #[test]
    fn tokens_with_basename() {
        assert_eq!(
            CommandSet::new(vec![vec!["echo", "{/}"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("echo".into()),
                        FormatTemplate::Tokens(vec![Token::Basename]),
                    ],
                }],
                mode: ExecutionMode::OneByOne,
            }
        );
    }

    #[test]
    fn tokens_with_parent() {
        assert_eq!(
            CommandSet::new(vec![vec!["echo", "{//}"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("echo".into()),
                        FormatTemplate::Tokens(vec![Token::Parent]),
                    ],
                }],
                mode: ExecutionMode::OneByOne,
            }
        );
    }

    #[test]
    fn tokens_with_basename_no_extension() {
        assert_eq!(
            CommandSet::new(vec![vec!["echo", "{/.}"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("echo".into()),
                        FormatTemplate::Tokens(vec![Token::BasenameNoExt]),
                    ],
                }],
                mode: ExecutionMode::OneByOne,
            }
        );
    }

    #[test]
    fn tokens_with_literal_braces() {
        let template = CommandTemplate::new(vec!["{{}}", "{{", "{.}}"]).unwrap();
        assert_eq!(
            generate_str(&template, "foo"),
            vec!["{}", "{", "{.}", "foo"]
        );
    }

    #[test]
    fn tokens_with_literal_braces_and_placeholder() {
        let template = CommandTemplate::new(vec!["{{{},end}"]).unwrap();
        assert_eq!(generate_str(&template, "foo"), vec!["{foo,end}"]);
    }

    #[test]
    fn tokens_multiple() {
        assert_eq!(
            CommandSet::new(vec![vec!["cp", "{}", "{/.}.ext"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("cp".into()),
                        FormatTemplate::Tokens(vec![Token::Placeholder]),
                        FormatTemplate::Tokens(vec![
                            Token::BasenameNoExt,
                            Token::Text(".ext".into())
                        ]),
                    ],
                }],
                mode: ExecutionMode::OneByOne,
            }
        );
    }

    #[test]
    fn tokens_single_batch() {
        assert_eq!(
            CommandSet::new_batch(vec![vec!["echo", "{.}"]]).unwrap(),
            CommandSet {
                commands: vec![CommandTemplate {
                    args: vec![
                        FormatTemplate::Text("echo".into()),
                        FormatTemplate::Tokens(vec![Token::NoExt]),
                    ],
                }],
                mode: ExecutionMode::Batch,
            }
        );
    }

    #[test]
    fn tokens_multiple_batch() {
        assert!(CommandSet::new_batch(vec![vec!["echo", "{.}", "{}"]]).is_err());
    }

    #[test]
    fn template_no_args() {
        assert!(CommandTemplate::new::<Vec<_>, &'static str>(vec![]).is_err());
    }

    #[test]
    fn command_set_no_args() {
        assert!(CommandSet::new(vec![vec!["echo"], vec![]]).is_err());
    }

    #[test]
    fn generate_custom_path_separator() {
        let arg = FormatTemplate::Tokens(vec![Token::Placeholder]);
        macro_rules! check {
            ($input:expr, $expected:expr) => {
                assert_eq!(arg.generate($input, Some("#")), OsString::from($expected));
            };
        }

        check!("foo", "foo");
        check!("foo/bar", "foo#bar");
        check!("/foo/bar/baz", "#foo#bar#baz");
    }

    #[cfg(windows)]
    #[test]
    fn generate_custom_path_separator_windows() {
        let arg = FormatTemplate::Tokens(vec![Token::Placeholder]);
        macro_rules! check {
            ($input:expr, $expected:expr) => {
                assert_eq!(arg.generate($input, Some("#")), OsString::from($expected));
            };
        }

        // path starting with a drive letter
        check!(r"C:\foo\bar", "C:#foo#bar");
        // UNC path
        check!(r"\\server\share\path", "##server#share#path");
        // Drive Relative path - no separator after the colon omits the RootDir path component.
        // This is uncommon, but valid
        check!(r"C:foo\bar", "C:foo#bar");

        // forward slashes should get normalized and interpreted as separators
        check!("C:/foo/bar", "C:#foo#bar");
        check!("C:foo/bar", "C:foo#bar");

        // Rust does not interpret "//server/share" as a UNC path, but rather as a normal
        // absolute path that begins with RootDir, and the two slashes get combined together as
        // a single path separator during normalization.
        //check!("//server/share/path", "##server#share#path");
    }
}
```

## File: `src/filter/mod.rs`
```rust
pub use self::size::SizeFilter;
pub use self::time::TimeFilter;

#[cfg(unix)]
pub use self::owner::OwnerFilter;

mod size;
mod time;

#[cfg(unix)]
mod owner;
```

## File: `src/filter/owner.rs`
```rust
use anyhow::{Result, anyhow};
use nix::unistd::{Group, User};
use std::fs;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct OwnerFilter {
    uid: Check<u32>,
    gid: Check<u32>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Check<T> {
    Equal(T),
    NotEq(T),
    Ignore,
}

impl OwnerFilter {
    const IGNORE: Self = OwnerFilter {
        uid: Check::Ignore,
        gid: Check::Ignore,
    };

    /// Parses an owner constraint
    /// Returns an error if the string is invalid
    /// Returns Ok(None) when string is acceptable but a noop (such as "" or ":")
    pub fn from_string(input: &str) -> Result<Self> {
        let mut it = input.split(':');
        let (fst, snd) = (it.next(), it.next());

        if it.next().is_some() {
            return Err(anyhow!(
                "more than one ':' present in owner string '{}'. See 'fd --help'.",
                input
            ));
        }

        let uid = Check::parse(fst, |s| {
            if let Ok(uid) = s.parse() {
                Ok(uid)
            } else {
                User::from_name(s)?
                    .map(|user| user.uid.as_raw())
                    .ok_or_else(|| anyhow!("'{}' is not a recognized user name", s))
            }
        })?;
        let gid = Check::parse(snd, |s| {
            if let Ok(gid) = s.parse() {
                Ok(gid)
            } else {
                Group::from_name(s)?
                    .map(|group| group.gid.as_raw())
                    .ok_or_else(|| anyhow!("'{}' is not a recognized group name", s))
            }
        })?;

        Ok(OwnerFilter { uid, gid })
    }

    /// If self is a no-op (ignore both uid and gid) then return `None`, otherwise wrap in a `Some`
    pub fn filter_ignore(self) -> Option<Self> {
        if self == Self::IGNORE {
            None
        } else {
            Some(self)
        }
    }

    pub fn matches(&self, md: &fs::Metadata) -> bool {
        use std::os::unix::fs::MetadataExt;

        self.uid.check(md.uid()) && self.gid.check(md.gid())
    }
}

impl<T: PartialEq> Check<T> {
    fn check(&self, v: T) -> bool {
        match self {
            Check::Equal(x) => v == *x,
            Check::NotEq(x) => v != *x,
            Check::Ignore => true,
        }
    }

    fn parse<F>(s: Option<&str>, f: F) -> Result<Self>
    where
        F: Fn(&str) -> Result<T>,
    {
        let (s, equality) = match s {
            Some("") | None => return Ok(Check::Ignore),
            Some(s) if s.starts_with('!') => (&s[1..], false),
            Some(s) => (s, true),
        };

        f(s).map(|x| {
            if equality {
                Check::Equal(x)
            } else {
                Check::NotEq(x)
            }
        })
    }
}

#[cfg(test)]
mod owner_parsing {
    use super::OwnerFilter;

    macro_rules! owner_tests {
        ($($name:ident: $value:expr => $result:pat,)*) => {
            $(
                #[test]
                fn $name() {
                    let o = OwnerFilter::from_string($value);
                    match o {
                        $result => {},
                        _ => panic!("{:?} does not match {}", o, stringify!($result)),
                    }
                }
            )*
        };
    }

    use super::Check::*;
    owner_tests! {
        empty:      ""      => Ok(OwnerFilter::IGNORE),
        uid_only:   "5"     => Ok(OwnerFilter { uid: Equal(5), gid: Ignore     }),
        uid_gid:    "9:3"   => Ok(OwnerFilter { uid: Equal(9), gid: Equal(3)   }),
        gid_only:   ":8"    => Ok(OwnerFilter { uid: Ignore,   gid: Equal(8)   }),
        colon_only: ":"     => Ok(OwnerFilter::IGNORE),
        trailing:   "5:"    => Ok(OwnerFilter { uid: Equal(5), gid: Ignore     }),

        uid_negate: "!5"    => Ok(OwnerFilter { uid: NotEq(5), gid: Ignore     }),
        both_negate:"!4:!3" => Ok(OwnerFilter { uid: NotEq(4), gid: NotEq(3)   }),
        uid_not_gid:"6:!8"  => Ok(OwnerFilter { uid: Equal(6), gid: NotEq(8)   }),

        more_colons:"3:5:"  => Err(_),
        only_colons:"::"    => Err(_),
    }
}
```

## File: `src/filter/size.rs`
```rust
use std::sync::OnceLock;

use anyhow::anyhow;
use regex::Regex;

static SIZE_CAPTURES: OnceLock<Regex> = OnceLock::new();

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum SizeFilter {
    Max(u64),
    Min(u64),
    Equals(u64),
}

// SI prefixes (powers of 10)
const KILO: u64 = 1000;
const MEGA: u64 = KILO * 1000;
const GIGA: u64 = MEGA * 1000;
const TERA: u64 = GIGA * 1000;

// Binary prefixes (powers of 2)
const KIBI: u64 = 1024;
const MEBI: u64 = KIBI * 1024;
const GIBI: u64 = MEBI * 1024;
const TEBI: u64 = GIBI * 1024;

impl SizeFilter {
    pub fn from_string(s: &str) -> anyhow::Result<Self> {
        SizeFilter::parse_opt(s)
            .ok_or_else(|| anyhow!("'{}' is not a valid size constraint. See 'fd --help'.", s))
    }

    fn parse_opt(s: &str) -> Option<Self> {
        let pattern =
            SIZE_CAPTURES.get_or_init(|| Regex::new(r"(?i)^([+-]?)(\d+)(b|[kmgt]i?b?)$").unwrap());
        if !pattern.is_match(s) {
            return None;
        }

        let captures = pattern.captures(s)?;
        let limit_kind = captures.get(1).map_or("+", |m| m.as_str());
        let quantity = captures
            .get(2)
            .and_then(|v| v.as_str().parse::<u64>().ok())?;

        let multiplier = match &captures.get(3).map_or("b", |m| m.as_str()).to_lowercase()[..] {
            v if v.starts_with("ki") => KIBI,
            v if v.starts_with('k') => KILO,
            v if v.starts_with("mi") => MEBI,
            v if v.starts_with('m') => MEGA,
            v if v.starts_with("gi") => GIBI,
            v if v.starts_with('g') => GIGA,
            v if v.starts_with("ti") => TEBI,
            v if v.starts_with('t') => TERA,
            "b" => 1,
            _ => return None,
        };

        let size = quantity * multiplier;
        match limit_kind {
            "+" => Some(SizeFilter::Min(size)),
            "-" => Some(SizeFilter::Max(size)),
            "" => Some(SizeFilter::Equals(size)),
            _ => None,
        }
    }

    pub fn is_within(&self, size: u64) -> bool {
        match *self {
            SizeFilter::Max(limit) => size <= limit,
            SizeFilter::Min(limit) => size >= limit,
            SizeFilter::Equals(limit) => size == limit,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    macro_rules! gen_size_filter_parse_test {
        ($($name: ident: $val: expr,)*) => {
            $(
                #[test]
                fn $name() {
                    let (txt, expected) = $val;
                    let actual = SizeFilter::from_string(txt).unwrap();
                    assert_eq!(actual, expected);
                }
            )*
        };
    }

    // Parsing and size conversion tests data. Ensure that each type gets properly interpreted.
    // Call with higher base values to ensure expected multiplication (only need a couple)
    gen_size_filter_parse_test! {
        byte_plus:                ("+1b",     SizeFilter::Min(1)),
        byte_plus_multiplier:     ("+10b",    SizeFilter::Min(10)),
        byte_minus:               ("-1b",     SizeFilter::Max(1)),
        kilo_plus:                ("+1k",     SizeFilter::Min(1000)),
        kilo_plus_suffix:         ("+1kb",    SizeFilter::Min(1000)),
        kilo_minus:               ("-1k",     SizeFilter::Max(1000)),
        kilo_minus_multiplier:    ("-100k",   SizeFilter::Max(100_000)),
        kilo_minus_suffix:        ("-1kb",    SizeFilter::Max(1000)),
        kilo_plus_upper:          ("+1K",     SizeFilter::Min(1000)),
        kilo_plus_suffix_upper:   ("+1KB",    SizeFilter::Min(1000)),
        kilo_minus_upper:         ("-1K",     SizeFilter::Max(1000)),
        kilo_minus_suffix_upper:  ("-1Kb",    SizeFilter::Max(1000)),
        kibi_plus:                ("+1ki",    SizeFilter::Min(1024)),
        kibi_plus_multiplier:     ("+10ki",   SizeFilter::Min(10_240)),
        kibi_plus_suffix:         ("+1kib",   SizeFilter::Min(1024)),
        kibi_minus:               ("-1ki",    SizeFilter::Max(1024)),
        kibi_minus_multiplier:    ("-100ki",  SizeFilter::Max(102_400)),
        kibi_minus_suffix:        ("-1kib",   SizeFilter::Max(1024)),
        kibi_plus_upper:          ("+1KI",    SizeFilter::Min(1024)),
        kibi_plus_suffix_upper:   ("+1KiB",   SizeFilter::Min(1024)),
        kibi_minus_upper:         ("-1Ki",    SizeFilter::Max(1024)),
        kibi_minus_suffix_upper:  ("-1KIB",   SizeFilter::Max(1024)),
        mega_plus:                ("+1m",     SizeFilter::Min(1_000_000)),
        mega_plus_suffix:         ("+1mb",    SizeFilter::Min(1_000_000)),
        mega_minus:               ("-1m",     SizeFilter::Max(1_000_000)),
        mega_minus_suffix:        ("-1mb",    SizeFilter::Max(1_000_000)),
        mega_plus_upper:          ("+1M",     SizeFilter::Min(1_000_000)),
        mega_plus_suffix_upper:   ("+1MB",    SizeFilter::Min(1_000_000)),
        mega_minus_upper:         ("-1M",     SizeFilter::Max(1_000_000)),
        mega_minus_suffix_upper:  ("-1Mb",    SizeFilter::Max(1_000_000)),
        mebi_plus:                ("+1mi",    SizeFilter::Min(1_048_576)),
        mebi_plus_suffix:         ("+1mib",   SizeFilter::Min(1_048_576)),
        mebi_minus:               ("-1mi",    SizeFilter::Max(1_048_576)),
        mebi_minus_suffix:        ("-1mib",   SizeFilter::Max(1_048_576)),
        mebi_plus_upper:          ("+1MI",    SizeFilter::Min(1_048_576)),
        mebi_plus_suffix_upper:   ("+1MiB",   SizeFilter::Min(1_048_576)),
        mebi_minus_upper:         ("-1Mi",    SizeFilter::Max(1_048_576)),
        mebi_minus_suffix_upper:  ("-1MIB",   SizeFilter::Max(1_048_576)),
        giga_plus:                ("+1g",     SizeFilter::Min(1_000_000_000)),
        giga_plus_suffix:         ("+1gb",    SizeFilter::Min(1_000_000_000)),
        giga_minus:               ("-1g",     SizeFilter::Max(1_000_000_000)),
        giga_minus_suffix:        ("-1gb",    SizeFilter::Max(1_000_000_000)),
        giga_plus_upper:          ("+1G",     SizeFilter::Min(1_000_000_000)),
        giga_plus_suffix_upper:   ("+1GB",    SizeFilter::Min(1_000_000_000)),
        giga_minus_upper:         ("-1G",     SizeFilter::Max(1_000_000_000)),
        giga_minus_suffix_upper:  ("-1Gb",    SizeFilter::Max(1_000_000_000)),
        gibi_plus:                ("+1gi",    SizeFilter::Min(1_073_741_824)),
        gibi_plus_suffix:         ("+1gib",   SizeFilter::Min(1_073_741_824)),
        gibi_minus:               ("-1gi",    SizeFilter::Max(1_073_741_824)),
        gibi_minus_suffix:        ("-1gib",   SizeFilter::Max(1_073_741_824)),
        gibi_plus_upper:          ("+1GI",    SizeFilter::Min(1_073_741_824)),
        gibi_plus_suffix_upper:   ("+1GiB",   SizeFilter::Min(1_073_741_824)),
        gibi_minus_upper:         ("-1Gi",    SizeFilter::Max(1_073_741_824)),
        gibi_minus_suffix_upper:  ("-1GIB",   SizeFilter::Max(1_073_741_824)),
        tera_plus:                ("+1t",     SizeFilter::Min(1_000_000_000_000)),
        tera_plus_suffix:         ("+1tb",    SizeFilter::Min(1_000_000_000_000)),
        tera_minus:               ("-1t",     SizeFilter::Max(1_000_000_000_000)),
        tera_minus_suffix:        ("-1tb",    SizeFilter::Max(1_000_000_000_000)),
        tera_plus_upper:          ("+1T",     SizeFilter::Min(1_000_000_000_000)),
        tera_plus_suffix_upper:   ("+1TB",    SizeFilter::Min(1_000_000_000_000)),
        tera_minus_upper:         ("-1T",     SizeFilter::Max(1_000_000_000_000)),
        tera_minus_suffix_upper:  ("-1Tb",    SizeFilter::Max(1_000_000_000_000)),
        tebi_plus:                ("+1ti",    SizeFilter::Min(1_099_511_627_776)),
        tebi_plus_suffix:         ("+1tib",   SizeFilter::Min(1_099_511_627_776)),
        tebi_minus:               ("-1ti",    SizeFilter::Max(1_099_511_627_776)),
        tebi_minus_suffix:        ("-1tib",   SizeFilter::Max(1_099_511_627_776)),
        tebi_plus_upper:          ("+1TI",    SizeFilter::Min(1_099_511_627_776)),
        tebi_plus_suffix_upper:   ("+1TiB",   SizeFilter::Min(1_099_511_627_776)),
        tebi_minus_upper:         ("-1Ti",    SizeFilter::Max(1_099_511_627_776)),
        tebi_minus_suffix_upper:  ("-1TIB",   SizeFilter::Max(1_099_511_627_776)),
    }

    /// Invalid parse testing
    macro_rules! gen_size_filter_failure {
        ($($name:ident: $value:expr,)*) => {
            $(
                #[test]
                fn $name() {
                    let i = SizeFilter::from_string($value);
                    assert!(i.is_err());
                }
            )*
        };
    }

    // Invalid parse data
    gen_size_filter_failure! {
        ensure_missing_number_returns_none: "+g",
        ensure_missing_unit_returns_none: "+18",
        ensure_bad_format_returns_none_1: "$10M",
        ensure_bad_format_returns_none_2: "badval",
        ensure_bad_format_returns_none_3: "9999",
        ensure_invalid_unit_returns_none_1: "+50a",
        ensure_invalid_unit_returns_none_2: "-10v",
        ensure_invalid_unit_returns_none_3: "+1Mv",
        ensure_bib_format_returns_none: "+1bib",
        ensure_bb_format_returns_none: "+1bb",
    }

    #[test]
    fn is_within_less_than() {
        let f = SizeFilter::from_string("-1k").unwrap();
        assert!(f.is_within(999));
    }

    #[test]
    fn is_within_less_than_equal() {
        let f = SizeFilter::from_string("-1k").unwrap();
        assert!(f.is_within(1000));
    }

    #[test]
    fn is_within_greater_than() {
        let f = SizeFilter::from_string("+1k").unwrap();
        assert!(f.is_within(1001));
    }

    #[test]
    fn is_within_greater_than_equal() {
        let f = SizeFilter::from_string("+1K").unwrap();
        assert!(f.is_within(1000));
    }
}
```

## File: `src/filter/time.rs`
```rust
use jiff::{Span, Timestamp, Zoned, civil::DateTime, tz::TimeZone};

use std::time::{Duration, SystemTime, UNIX_EPOCH};

/// Filter based on time ranges.
#[derive(Debug, PartialEq, Eq)]
pub enum TimeFilter {
    Before(SystemTime),
    After(SystemTime),
}

#[cfg(not(test))]
fn now() -> Zoned {
    Zoned::now()
}

#[cfg(test)]
thread_local! {
    static TESTTIME: std::cell::RefCell<Option<Zoned>> = None.into();
}

/// This allows us to set a specific time when running tests
#[cfg(test)]
fn now() -> Zoned {
    TESTTIME.with_borrow(|reftime| reftime.as_ref().cloned().unwrap_or_else(Zoned::now))
}

impl TimeFilter {
    fn from_str(s: &str) -> Option<SystemTime> {
        if let Ok(span) = s.parse::<Span>() {
            let datetime = now().checked_sub(span).ok()?;
            Some(datetime.into())
        } else if let Ok(timestamp) = s.parse::<Timestamp>() {
            Some(timestamp.into())
        } else if let Ok(datetime) = s.parse::<DateTime>() {
            Some(
                TimeZone::system()
                    .to_ambiguous_zoned(datetime)
                    .later()
                    .ok()?
                    .into(),
            )
        } else {
            let timestamp_secs: u64 = s.strip_prefix('@')?.parse().ok()?;
            Some(UNIX_EPOCH + Duration::from_secs(timestamp_secs))
        }
    }

    pub fn before(s: &str) -> Option<TimeFilter> {
        TimeFilter::from_str(s).map(TimeFilter::Before)
    }

    pub fn after(s: &str) -> Option<TimeFilter> {
        TimeFilter::from_str(s).map(TimeFilter::After)
    }

    pub fn applies_to(&self, t: &SystemTime) -> bool {
        match self {
            TimeFilter::Before(limit) => t < limit,
            TimeFilter::After(limit) => t > limit,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::time::Duration;

    struct TestTime(SystemTime);

    impl TestTime {
        fn new(time: Zoned) -> Self {
            TESTTIME.with_borrow_mut(|t| *t = Some(time.clone()));
            TestTime(time.into())
        }

        fn set(&mut self, time: Zoned) {
            TESTTIME.with_borrow_mut(|t| *t = Some(time.clone()));
            self.0 = time.into();
        }

        fn timestamp(&self) -> SystemTime {
            self.0
        }
    }

    impl Drop for TestTime {
        fn drop(&mut self) {
            // Stop using manually set times
            TESTTIME.with_borrow_mut(|t| *t = None);
        }
    }

    #[test]
    fn is_time_filter_applicable() {
        let local_tz = TimeZone::system();
        let mut test_time = TestTime::new(
            local_tz
                .to_ambiguous_zoned("2010-10-10 10:10:10".parse::<DateTime>().unwrap())
                .later()
                .unwrap(),
        );
        let mut ref_time = test_time.timestamp();

        assert!(TimeFilter::after("1min").unwrap().applies_to(&ref_time));
        assert!(!TimeFilter::before("1min").unwrap().applies_to(&ref_time));

        let t1m_ago = ref_time - Duration::from_secs(60);
        assert!(!TimeFilter::after("30sec").unwrap().applies_to(&t1m_ago));
        assert!(TimeFilter::after("2min").unwrap().applies_to(&t1m_ago));

        assert!(TimeFilter::before("30sec").unwrap().applies_to(&t1m_ago));
        assert!(!TimeFilter::before("2min").unwrap().applies_to(&t1m_ago));

        let t10s_before = "2010-10-10 10:10:00";
        assert!(
            !TimeFilter::before(t10s_before)
                .unwrap()
                .applies_to(&ref_time)
        );
        assert!(
            TimeFilter::before(t10s_before)
                .unwrap()
                .applies_to(&t1m_ago)
        );

        assert!(
            TimeFilter::after(t10s_before)
                .unwrap()
                .applies_to(&ref_time)
        );
        assert!(!TimeFilter::after(t10s_before).unwrap().applies_to(&t1m_ago));

        let same_day = "2010-10-10";
        assert!(!TimeFilter::before(same_day).unwrap().applies_to(&ref_time));
        assert!(!TimeFilter::before(same_day).unwrap().applies_to(&t1m_ago));

        assert!(TimeFilter::after(same_day).unwrap().applies_to(&ref_time));
        assert!(TimeFilter::after(same_day).unwrap().applies_to(&t1m_ago));

        test_time.set(
            "2010-10-10T10:10:10+00:00"
                .parse::<Timestamp>()
                .unwrap()
                .to_zoned(local_tz.clone()),
        );
        ref_time = test_time.timestamp();
        let t1m_ago = ref_time - Duration::from_secs(60);
        let t10s_before = "2010-10-10T10:10:00+00:00";
        assert!(
            !TimeFilter::before(t10s_before)
                .unwrap()
                .applies_to(&ref_time)
        );
        assert!(
            TimeFilter::before(t10s_before)
                .unwrap()
                .applies_to(&t1m_ago)
        );

        assert!(
            TimeFilter::after(t10s_before)
                .unwrap()
                .applies_to(&ref_time)
        );
        assert!(!TimeFilter::after(t10s_before).unwrap().applies_to(&t1m_ago));

        let ref_timestamp = 1707723412u64; // Mon Feb 12 07:36:52 UTC 2024
        test_time.set(
            "2024-02-12T07:36:52+00:00"
                .parse::<Timestamp>()
                .unwrap()
                .to_zoned(local_tz),
        );
        ref_time = test_time.timestamp();
        let t1m_ago = ref_time - Duration::from_secs(60);
        let t1s_later = ref_time + Duration::from_secs(1);
        // Timestamp only supported via '@' prefix
        assert!(TimeFilter::before(&ref_timestamp.to_string()).is_none());
        assert!(
            TimeFilter::before(&format!("@{ref_timestamp}"))
                .unwrap()
                .applies_to(&t1m_ago)
        );
        assert!(
            !TimeFilter::before(&format!("@{ref_timestamp}"))
                .unwrap()
                .applies_to(&t1s_later)
        );
        assert!(
            !TimeFilter::after(&format!("@{ref_timestamp}"))
                .unwrap()
                .applies_to(&t1m_ago)
        );
        assert!(
            TimeFilter::after(&format!("@{ref_timestamp}"))
                .unwrap()
                .applies_to(&t1s_later)
        );
    }
}
```

## File: `src/fmt/input.rs`
```rust
use std::ffi::{OsStr, OsString};
use std::path::{Path, PathBuf};

use crate::filesystem::strip_current_dir;

/// Removes the parent component of the path
pub fn basename(path: &Path) -> &OsStr {
    path.file_name().unwrap_or(path.as_os_str())
}

/// Removes the extension from the path
pub fn remove_extension(path: &Path) -> OsString {
    let dirname = dirname(path);
    let stem = path.file_stem().unwrap_or(path.as_os_str());

    let path = PathBuf::from(dirname).join(stem);

    strip_current_dir(&path).to_owned().into_os_string()
}

/// Removes the basename from the path.
pub fn dirname(path: &Path) -> OsString {
    path.parent()
        .map(|p| {
            if p == OsStr::new("") {
                OsString::from(".")
            } else {
                p.as_os_str().to_owned()
            }
        })
        .unwrap_or_else(|| path.as_os_str().to_owned())
}

#[cfg(test)]
mod path_tests {
    use super::*;
    use std::path::MAIN_SEPARATOR_STR;

    fn correct(input: &str) -> String {
        input.replace('/', MAIN_SEPARATOR_STR)
    }

    macro_rules! func_tests {
        ($($name:ident: $func:ident for $input:expr => $output:expr)+) => {
            $(
                #[test]
                fn $name() {
                    let input_path = PathBuf::from(&correct($input));
                    let output_string = OsString::from(correct($output));
                    assert_eq!($func(&input_path), output_string);
                }
            )+
        }
    }

    func_tests! {
        remove_ext_simple:  remove_extension  for  "foo.txt"      =>  "foo"
        remove_ext_dir:     remove_extension  for  "dir/foo.txt"  =>  "dir/foo"
        hidden:             remove_extension  for  ".foo"         =>  ".foo"
        remove_ext_utf8:    remove_extension  for  "💖.txt"       =>  "💖"
        remove_ext_empty:   remove_extension  for  ""             =>  ""

        basename_simple:  basename  for  "foo.txt"      =>  "foo.txt"
        basename_dir:     basename  for  "dir/foo.txt"  =>  "foo.txt"
        basename_empty:   basename  for  ""             =>  ""
        basename_utf8_0:  basename  for  "💖/foo.txt"   =>  "foo.txt"
        basename_utf8_1:  basename  for  "dir/💖.txt"   =>  "💖.txt"

        dirname_simple:  dirname  for  "foo.txt"      =>  "."
        dirname_dir:     dirname  for  "dir/foo.txt"  =>  "dir"
        dirname_utf8_0:  dirname  for  "💖/foo.txt"   =>  "💖"
        dirname_utf8_1:  dirname  for  "dir/💖.txt"   =>  "dir"
    }

    #[test]
    #[cfg(windows)]
    fn dirname_root() {
        assert_eq!(dirname(&PathBuf::from("C:")), OsString::from("C:"));
        assert_eq!(dirname(&PathBuf::from("\\")), OsString::from("\\"));
    }

    #[test]
    #[cfg(not(windows))]
    fn dirname_root() {
        assert_eq!(dirname(&PathBuf::from("/")), OsString::from("/"));
    }
}
```

## File: `src/fmt/mod.rs`
```rust
mod input;

use std::borrow::Cow;
use std::ffi::{OsStr, OsString};
use std::fmt::{self, Display, Formatter};
use std::path::{Component, Path, Prefix};
use std::sync::OnceLock;

use aho_corasick::AhoCorasick;

use self::input::{basename, dirname, remove_extension};

/// Designates what should be written to a buffer
///
/// Each `Token` contains either text, or a placeholder variant, which will be used to generate
/// commands after all tokens for a given command template have been collected.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Token {
    Placeholder,
    Basename,
    Parent,
    NoExt,
    BasenameNoExt,
    Text(String),
}

impl Display for Token {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        match *self {
            Token::Placeholder => f.write_str("{}")?,
            Token::Basename => f.write_str("{/}")?,
            Token::Parent => f.write_str("{//}")?,
            Token::NoExt => f.write_str("{.}")?,
            Token::BasenameNoExt => f.write_str("{/.}")?,
            Token::Text(ref string) => f.write_str(string)?,
        }
        Ok(())
    }
}

/// A parsed format string
///
/// This is either a collection of `Token`s including at least one placeholder variant,
/// or a fixed text.
#[derive(Clone, Debug, PartialEq)]
pub enum FormatTemplate {
    Tokens(Vec<Token>),
    Text(String),
}

static PLACEHOLDERS: OnceLock<AhoCorasick> = OnceLock::new();

impl FormatTemplate {
    pub fn has_tokens(&self) -> bool {
        matches!(self, FormatTemplate::Tokens(_))
    }

    pub fn parse(fmt: &str) -> Self {
        // NOTE: we assume that { and } have the same length
        const BRACE_LEN: usize = '{'.len_utf8();
        let mut tokens = Vec::new();
        let mut remaining = fmt;
        let mut buf = String::new();
        let placeholders = PLACEHOLDERS.get_or_init(|| {
            AhoCorasick::new(["{{", "}}", "{}", "{/}", "{//}", "{.}", "{/.}"]).unwrap()
        });
        while let Some(m) = placeholders.find(remaining) {
            match m.pattern().as_u32() {
                0 | 1 => {
                    // we found an escaped {{ or }}, so add
                    // everything up to the first char to the buffer
                    // then skip the second one.
                    buf += &remaining[..m.start() + BRACE_LEN];
                    remaining = &remaining[m.end()..];
                }
                id if !remaining[m.end()..].starts_with('}') => {
                    buf += &remaining[..m.start()];
                    if !buf.is_empty() {
                        tokens.push(Token::Text(std::mem::take(&mut buf)));
                    }
                    tokens.push(token_from_pattern_id(id));
                    remaining = &remaining[m.end()..];
                }
                _ => {
                    // We got a normal pattern, but the final "}"
                    // is escaped, so add up to that to the buffer, then
                    // skip the final }
                    buf += &remaining[..m.end()];
                    remaining = &remaining[m.end() + BRACE_LEN..];
                }
            }
        }
        // Add the rest of the string to the buffer, and add the final buffer to the tokens
        if !remaining.is_empty() {
            buf += remaining;
        }
        if tokens.is_empty() {
            // No placeholders were found, so just return the text
            return FormatTemplate::Text(buf);
        }
        // Add final text segment
        if !buf.is_empty() {
            tokens.push(Token::Text(buf));
        }
        debug_assert!(!tokens.is_empty());
        FormatTemplate::Tokens(tokens)
    }

    /// Generate a result string from this template. If path_separator is Some, then it will replace
    /// the path separator in all placeholder tokens. Fixed text and tokens are not affected by
    /// path separator substitution.
    pub fn generate(&self, path: impl AsRef<Path>, path_separator: Option<&str>) -> OsString {
        use Token::*;
        let path = path.as_ref();

        match *self {
            Self::Tokens(ref tokens) => {
                let mut s = OsString::new();
                for token in tokens {
                    match token {
                        Basename => s.push(Self::replace_separator(basename(path), path_separator)),
                        BasenameNoExt => s.push(Self::replace_separator(
                            &remove_extension(basename(path).as_ref()),
                            path_separator,
                        )),
                        NoExt => s.push(Self::replace_separator(
                            &remove_extension(path),
                            path_separator,
                        )),
                        Parent => s.push(Self::replace_separator(&dirname(path), path_separator)),
                        Placeholder => {
                            s.push(Self::replace_separator(path.as_ref(), path_separator))
                        }
                        Text(string) => s.push(string),
                    }
                }
                s
            }
            Self::Text(ref text) => OsString::from(text),
        }
    }

    /// Replace the path separator in the input with the custom separator string. If path_separator
    /// is None, simply return a borrowed Cow<OsStr> of the input. Otherwise, the input is
    /// interpreted as a Path and its components are iterated through and re-joined into a new
    /// OsString.
    fn replace_separator<'a>(path: &'a OsStr, path_separator: Option<&str>) -> Cow<'a, OsStr> {
        // fast-path - no replacement necessary
        if path_separator.is_none() {
            return Cow::Borrowed(path);
        }

        let path_separator = path_separator.unwrap();
        let mut out = OsString::with_capacity(path.len());
        let mut components = Path::new(path).components().peekable();

        while let Some(comp) = components.next() {
            match comp {
                // Absolute paths on Windows are tricky.  A Prefix component is usually a drive
                // letter or UNC path, and is usually followed by RootDir. There are also
                // "verbatim" prefixes beginning with "\\?\" that skip normalization. We choose to
                // ignore verbatim path prefixes here because they're very rare, might be
                // impossible to reach here, and there's no good way to deal with them. If users
                // are doing something advanced involving verbatim windows paths, they can do their
                // own output filtering with a tool like sed.
                Component::Prefix(prefix) => {
                    if let Prefix::UNC(server, share) = prefix.kind() {
                        // Prefix::UNC is a parsed version of '\\server\share'
                        out.push(path_separator);
                        out.push(path_separator);
                        out.push(server);
                        out.push(path_separator);
                        out.push(share);
                    } else {
                        // All other Windows prefix types are rendered as-is. This results in e.g. "C:" for
                        // drive letters. DeviceNS and Verbatim* prefixes won't have backslashes converted,
                        // but they're not returned by directories fd can search anyway so we don't worry
                        // about them.
                        out.push(comp.as_os_str());
                    }
                }

                // Root directory is always replaced with the custom separator.
                Component::RootDir => out.push(path_separator),

                // Everything else is joined normally, with a trailing separator if we're not last
                _ => {
                    out.push(comp.as_os_str());
                    if components.peek().is_some() {
                        out.push(path_separator);
                    }
                }
            }
        }
        Cow::Owned(out)
    }
}

// Convert the id from an aho-corasick match to the
// appropriate token
fn token_from_pattern_id(id: u32) -> Token {
    use Token::*;
    match id {
        2 => Placeholder,
        3 => Basename,
        4 => Parent,
        5 => NoExt,
        6 => BasenameNoExt,
        _ => unreachable!(),
    }
}

#[cfg(test)]
mod fmt_tests {
    use super::*;
    use std::path::PathBuf;

    #[test]
    fn parse_no_placeholders() {
        let templ = FormatTemplate::parse("This string has no placeholders");
        assert_eq!(
            templ,
            FormatTemplate::Text("This string has no placeholders".into())
        );
    }

    #[test]
    fn parse_only_brace_escapes() {
        let templ = FormatTemplate::parse("This string only has escapes like {{ and }}");
        assert_eq!(
            templ,
            FormatTemplate::Text("This string only has escapes like { and }".into())
        );
    }

    #[test]
    fn all_placeholders() {
        use Token::*;

        let templ = FormatTemplate::parse(
            "{{path={} \
            basename={/} \
            parent={//} \
            noExt={.} \
            basenameNoExt={/.} \
            }}",
        );
        assert_eq!(
            templ,
            FormatTemplate::Tokens(vec![
                Text("{path=".into()),
                Placeholder,
                Text(" basename=".into()),
                Basename,
                Text(" parent=".into()),
                Parent,
                Text(" noExt=".into()),
                NoExt,
                Text(" basenameNoExt=".into()),
                BasenameNoExt,
                Text(" }".into()),
            ])
        );

        let mut path = PathBuf::new();
        path.push("a");
        path.push("folder");
        path.push("file.txt");

        let expanded = templ.generate(&path, Some("/")).into_string().unwrap();

        assert_eq!(
            expanded,
            "{path=a/folder/file.txt \
            basename=file.txt \
            parent=a/folder \
            noExt=a/folder/file \
            basenameNoExt=file }"
        );
    }
}
```

## File: `tests/tests.rs`
```rust
mod testenv;

#[cfg(unix)]
use nix::unistd::{Gid, Group, Uid, User};
use std::fs;
use std::io::Write;
use std::path::Path;
use std::time::{Duration, SystemTime};
use test_case::test_case;

use jiff::Timestamp;
use normpath::PathExt;
use regex::escape;

use crate::testenv::TestEnv;

static DEFAULT_DIRS: &[&str] = &["one/two/three", "one/two/three/directory_foo"];

static DEFAULT_FILES: &[&str] = &[
    "a.foo",
    "one/b.foo",
    "one/two/c.foo",
    "one/two/C.Foo2",
    "one/two/three/d.foo",
    "fdignored.foo",
    "gitignored.foo",
    ".hidden.foo",
    "e1 e2",
];

#[allow(clippy::let_and_return)]
fn get_absolute_root_path(env: &TestEnv) -> String {
    let path = env
        .test_root()
        .normalize()
        .expect("absolute path")
        .as_path()
        .to_str()
        .expect("string")
        .to_string();

    #[cfg(windows)]
    let path = path.trim_start_matches(r"\\?\").to_string();

    path
}

#[cfg(test)]
fn get_test_env_with_abs_path(dirs: &[&'static str], files: &[&'static str]) -> (TestEnv, String) {
    let env = TestEnv::new(dirs, files);
    let root_path = get_absolute_root_path(&env);
    (env, root_path)
}

#[cfg(test)]
fn create_file_with_size<P: AsRef<Path>>(path: P, size_in_bytes: usize) {
    let content = "#".repeat(size_in_bytes);
    let mut f = fs::File::create::<P>(path).unwrap();
    f.write_all(content.as_bytes()).unwrap();
}

/// Simple test
#[test]
fn test_simple() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(&["a.foo"], "a.foo");
    te.assert_output(&["b.foo"], "one/b.foo");
    te.assert_output(&["d.foo"], "one/two/three/d.foo");

    te.assert_output(
        &["foo"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

static AND_EXTRA_FILES: &[&str] = &[
    "a.foo",
    "one/b.foo",
    "one/two/c.foo",
    "one/two/C.Foo2",
    "one/two/three/baz-quux",
    "one/two/three/Baz-Quux2",
    "one/two/three/d.foo",
    "fdignored.foo",
    "gitignored.foo",
    ".hidden.foo",
    "A-B.jpg",
    "A-C.png",
    "B-A.png",
    "B-C.png",
    "C-A.jpg",
    "C-B.png",
    "e1 e2",
];

/// AND test
#[test]
fn test_and_basic() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &["foo", "--and", "c"],
        "one/two/C.Foo2
        one/two/c.foo
        one/two/three/directory_foo/",
    );

    te.assert_output(
        &["f", "--and", "[ad]", "--and", "[_]"],
        "one/two/three/directory_foo/",
    );

    te.assert_output(
        &["f", "--and", "[ad]", "--and", "[.]"],
        "a.foo
        one/two/three/d.foo",
    );

    te.assert_output(&["Foo", "--and", "C"], "one/two/C.Foo2");

    te.assert_output(&["foo", "--and", "asdasdasdsadasd"], "");
}

#[test]
fn test_and_empty_pattern() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);
    te.assert_output(&["Foo", "--and", "2", "--and", ""], "one/two/C.Foo2");
}

#[test]
fn test_and_bad_pattern() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_failure(&["Foo", "--and", "2", "--and", "[", "--and", "C"]);
    te.assert_failure(&["Foo", "--and", "[", "--and", "2", "--and", "C"]);
    te.assert_failure(&["Foo", "--and", "2", "--and", "C", "--and", "["]);
    te.assert_failure(&["[", "--and", "2", "--and", "C", "--and", "Foo"]);
}

#[test]
fn test_and_pattern_starts_with_dash() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &["baz", "--and", "quux"],
        "one/two/three/Baz-Quux2
        one/two/three/baz-quux",
    );
    te.assert_output(
        &["baz", "--and", "-"],
        "one/two/three/Baz-Quux2
        one/two/three/baz-quux",
    );
    te.assert_output(
        &["Quu", "--and", "x", "--and", "-"],
        "one/two/three/Baz-Quux2",
    );
}

#[test]
fn test_and_plus_extension() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &[
            "A",
            "--and",
            "B",
            "--extension",
            "jpg",
            "--extension",
            "png",
        ],
        "A-B.jpg
        B-A.png",
    );

    te.assert_output(
        &[
            "A",
            "--extension",
            "jpg",
            "--and",
            "B",
            "--extension",
            "png",
        ],
        "A-B.jpg
        B-A.png",
    );
}

#[test]
fn test_and_plus_type() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &["c", "--type", "d", "--and", "foo"],
        "one/two/three/directory_foo/",
    );

    te.assert_output(
        &["c", "--type", "f", "--and", "foo"],
        "one/two/C.Foo2
        one/two/c.foo",
    );
}

#[test]
fn test_and_plus_glob() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(&["*foo", "--glob", "--and", "c*"], "one/two/c.foo");
}

#[test]
fn test_and_plus_fixed_strings() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &["foo", "--fixed-strings", "--and", "c", "--and", "."],
        "one/two/c.foo
        one/two/C.Foo2",
    );

    te.assert_output(
        &["foo", "--fixed-strings", "--and", "[c]", "--and", "."],
        "",
    );

    te.assert_output(
        &["Foo", "--fixed-strings", "--and", "C", "--and", "."],
        "one/two/C.Foo2",
    );
}

#[test]
fn test_and_plus_ignore_case() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &["Foo", "--ignore-case", "--and", "C", "--and", "[.]"],
        "one/two/C.Foo2
        one/two/c.foo",
    );
}

#[test]
fn test_and_plus_case_sensitive() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &["foo", "--case-sensitive", "--and", "c", "--and", "[.]"],
        "one/two/c.foo",
    );
}

#[test]
fn test_and_plus_full_path() {
    let te = TestEnv::new(DEFAULT_DIRS, AND_EXTRA_FILES);

    te.assert_output(
        &[
            "three",
            "--full-path",
            "--and",
            "_foo",
            "--and",
            r"[/\\]dir",
        ],
        "one/two/three/directory_foo/",
    );

    te.assert_output(
        &[
            "three",
            "--full-path",
            "--and",
            r"[/\\]two",
            "--and",
            r"[/\\]dir",
        ],
        "one/two/three/directory_foo/",
    );
}

/// Test each pattern type with an empty pattern.
#[test]
fn test_empty_pattern() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    let expected = "a.foo
    e1 e2
    one/
    one/b.foo
    one/two/
    one/two/c.foo
    one/two/C.Foo2
    one/two/three/
    one/two/three/d.foo
    one/two/three/directory_foo/
    symlink";

    te.assert_output(&["--regex"], expected);
    te.assert_output(&["--fixed-strings"], expected);
    te.assert_output(&["--glob"], expected);
}

/// Test multiple directory searches
#[test]
fn test_multi_file() {
    let dirs = &["test1", "test2"];
    let files = &["test1/a.foo", "test1/b.foo", "test2/a.foo"];
    let te = TestEnv::new(dirs, files);
    te.assert_output(
        &["a.foo", "test1", "test2"],
        "test1/a.foo
        test2/a.foo",
    );

    te.assert_output(
        &["", "test1", "test2"],
        "test1/a.foo
        test2/a.foo
        test1/b.foo",
    );

    te.assert_output(&["a.foo", "test1"], "test1/a.foo");

    te.assert_output(&["b.foo", "test1", "test2"], "test1/b.foo");
}

/// Test search over multiple directory with missing
#[test]
fn test_multi_file_with_missing() {
    let dirs = &["real"];
    let files = &["real/a.foo", "real/b.foo"];
    let te = TestEnv::new(dirs, files);
    te.assert_output(&["a.foo", "real", "fake"], "real/a.foo");

    te.assert_error(
        &["a.foo", "real", "fake"],
        "[fd error]: Search path 'fake' is not a directory.",
    );

    te.assert_output(
        &["", "real", "fake"],
        "real/a.foo
        real/b.foo",
    );

    te.assert_output(
        &["", "real", "fake1", "fake2"],
        "real/a.foo
        real/b.foo",
    );

    te.assert_error(
        &["", "real", "fake1", "fake2"],
        "[fd error]: Search path 'fake1' is not a directory.
        [fd error]: Search path 'fake2' is not a directory.",
    );

    te.assert_failure_with_error(
        &["", "fake1", "fake2"],
        "[fd error]: Search path 'fake1' is not a directory.
        [fd error]: Search path 'fake2' is not a directory.
        [fd error]: No valid search paths given.",
    );
}

/// Explicit root path
#[test]
fn test_explicit_root_path() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["foo", "one"],
        "one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    te.assert_output(
        &["foo", "one/two/three"],
        "one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    te.assert_output_subdirectory(
        "one/two/",
        &["foo", "../../"],
        "../../a.foo
        ../../one/b.foo
        ../../one/two/c.foo
        ../../one/two/C.Foo2
        ../../one/two/three/d.foo
        ../../one/two/three/directory_foo/",
    );

    te.assert_output_subdirectory(
        "one/two/three",
        &["", ".."],
        "../c.foo
        ../C.Foo2
        ../three/
        ../three/d.foo
        ../three/directory_foo/",
    );
}

/// Regex searches
#[test]
fn test_regex_searches() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["[a-c].foo"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2",
    );

    te.assert_output(
        &["--case-sensitive", "[a-c].foo"],
        "a.foo
        one/b.foo
        one/two/c.foo",
    );
}

/// Smart case
#[test]
fn test_smart_case() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["c.foo"],
        "one/two/c.foo
        one/two/C.Foo2",
    );

    te.assert_output(&["C.Foo"], "one/two/C.Foo2");

    te.assert_output(&["Foo"], "one/two/C.Foo2");

    // Only literal uppercase chars should trigger case sensitivity.
    te.assert_output(
        &["\\Ac"],
        "one/two/c.foo
        one/two/C.Foo2",
    );
    te.assert_output(&["\\AC"], "one/two/C.Foo2");
}

/// Case sensitivity (--case-sensitive)
#[test]
fn test_case_sensitive() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(&["--case-sensitive", "c.foo"], "one/two/c.foo");

    te.assert_output(&["--case-sensitive", "C.Foo"], "one/two/C.Foo2");

    te.assert_output(
        &["--ignore-case", "--case-sensitive", "C.Foo"],
        "one/two/C.Foo2",
    );
}

/// Case insensitivity (--ignore-case)
#[test]
fn test_case_insensitive() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--ignore-case", "C.Foo"],
        "one/two/c.foo
        one/two/C.Foo2",
    );

    te.assert_output(
        &["--case-sensitive", "--ignore-case", "C.Foo"],
        "one/two/c.foo
        one/two/C.Foo2",
    );
}

/// Glob-based searches (--glob)
#[test]
fn test_glob_searches() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--glob", "*.foo"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/three/d.foo",
    );

    te.assert_output(
        &["--glob", "[a-c].foo"],
        "a.foo
        one/b.foo
        one/two/c.foo",
    );

    te.assert_output(
        &["--glob", "[a-c].foo*"],
        "a.foo
        one/b.foo
        one/two/C.Foo2
        one/two/c.foo",
    );
}

/// Glob-based searches (--glob) in combination with full path searches (--full-path)
#[cfg(not(windows))] // TODO: make this work on Windows
#[test]
fn test_full_path_glob_searches() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--glob", "--full-path", "**/one/**/*.foo"],
        "one/b.foo
        one/two/c.foo
        one/two/three/d.foo",
    );

    te.assert_output(
        &["--glob", "--full-path", "**/one/*/*.foo"],
        " one/two/c.foo",
    );

    te.assert_output(
        &["--glob", "--full-path", "**/one/*/*/*.foo"],
        " one/two/three/d.foo",
    );
}

#[test]
fn test_smart_case_glob_searches() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--glob", "c.foo*"],
        "one/two/C.Foo2
        one/two/c.foo",
    );

    te.assert_output(&["--glob", "C.Foo*"], "one/two/C.Foo2");
}

/// Glob-based searches (--glob) in combination with --case-sensitive
#[test]
fn test_case_sensitive_glob_searches() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(&["--glob", "--case-sensitive", "c.foo*"], "one/two/c.foo");
}

/// Glob-based searches (--glob) in combination with --extension
#[test]
fn test_glob_searches_with_extension() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--glob", "--extension", "foo2", "[a-z].*"],
        "one/two/C.Foo2",
    );
}

/// Make sure that --regex overrides --glob
#[test]
fn test_regex_overrides_glob() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(&["--glob", "--regex", "Foo2$"], "one/two/C.Foo2");
}

/// Full path search (--full-path)
#[test]
fn test_full_path() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    let root = te.system_root();
    let prefix = escape(&root.to_string_lossy());

    te.assert_output(
        &["--full-path", &format!("^{prefix}.*three.*foo$")],
        "one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

/// Hidden files (--hidden)
#[test]
fn test_hidden() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--hidden", "foo"],
        ".hidden.foo
        a.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

/// Hidden file attribute on Windows
#[cfg(windows)]
#[test]
fn test_hidden_file_attribute() {
    use std::os::windows::fs::OpenOptionsExt;

    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    // https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileattributesa
    const FILE_ATTRIBUTE_HIDDEN: u32 = 2;

    fs::OpenOptions::new()
        .create(true)
        .write(true)
        .attributes(FILE_ATTRIBUTE_HIDDEN)
        .open(te.test_root().join("hidden-file.txt"))
        .unwrap();

    te.assert_output(&["--hidden", "hidden-file.txt"], "hidden-file.txt");
    te.assert_output(&["hidden-file.txt"], "");
}

/// Ignored files (--no-ignore)
#[test]
fn test_no_ignore() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--no-ignore", "foo"],
        "a.foo
        fdignored.foo
        gitignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    te.assert_output(
        &["--hidden", "--no-ignore", "foo"],
        ".hidden.foo
        a.foo
        fdignored.foo
        gitignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

/// .gitignore and .fdignore
#[test]
fn test_gitignore_and_fdignore() {
    let files = &[
        "ignored-by-nothing",
        "ignored-by-fdignore",
        "ignored-by-gitignore",
        "ignored-by-both",
    ];
    let te = TestEnv::new(&[], files);

    fs::File::create(te.test_root().join(".fdignore"))
        .unwrap()
        .write_all(b"ignored-by-fdignore\nignored-by-both")
        .unwrap();

    fs::File::create(te.test_root().join(".gitignore"))
        .unwrap()
        .write_all(b"ignored-by-gitignore\nignored-by-both")
        .unwrap();

    te.assert_output(&["ignored"], "ignored-by-nothing");

    te.assert_output(
        &["--no-ignore-vcs", "ignored"],
        "ignored-by-nothing
        ignored-by-gitignore",
    );

    te.assert_output(
        &["--no-ignore", "ignored"],
        "ignored-by-nothing
        ignored-by-fdignore
        ignored-by-gitignore
        ignored-by-both",
    );
}

/// Ignore parent ignore files (--no-ignore-parent)
#[test]
fn test_no_ignore_parent() {
    let dirs = &["inner"];
    let files = &[
        "inner/parent-ignored",
        "inner/child-ignored",
        "inner/not-ignored",
    ];
    let te = TestEnv::new(dirs, files);

    // Ignore 'parent-ignored' in root
    fs::File::create(te.test_root().join(".gitignore"))
        .unwrap()
        .write_all(b"parent-ignored")
        .unwrap();
    // Ignore 'child-ignored' in inner
    fs::File::create(te.test_root().join("inner/.gitignore"))
        .unwrap()
        .write_all(b"child-ignored")
        .unwrap();

    te.assert_output_subdirectory("inner", &[], "not-ignored");

    te.assert_output_subdirectory(
        "inner",
        &["--no-ignore-parent"],
        "parent-ignored
        not-ignored",
    );
}

/// Ignore parent ignore files (--no-ignore-parent) with an inner git repo
#[test]
fn test_no_ignore_parent_inner_git() {
    let dirs = &["inner"];
    let files = &[
        "inner/parent-ignored",
        "inner/child-ignored",
        "inner/not-ignored",
    ];
    let te = TestEnv::new(dirs, files);

    // Make the inner folder also appear as a git repo
    fs::create_dir_all(te.test_root().join("inner/.git")).unwrap();

    // Ignore 'parent-ignored' in root
    fs::File::create(te.test_root().join(".gitignore"))
        .unwrap()
        .write_all(b"parent-ignored")
        .unwrap();
    // Ignore 'child-ignored' in inner
    fs::File::create(te.test_root().join("inner/.gitignore"))
        .unwrap()
        .write_all(b"child-ignored")
        .unwrap();

    te.assert_output_subdirectory(
        "inner",
        &[],
        "not-ignored
        parent-ignored",
    );

    te.assert_output_subdirectory(
        "inner",
        &["--no-ignore-parent"],
        "not-ignored
        parent-ignored",
    );
}

/// Precedence of .fdignore files
#[test]
fn test_custom_ignore_precedence() {
    let dirs = &["inner"];
    let files = &["inner/foo"];
    let te = TestEnv::new(dirs, files);

    // Ignore 'foo' via .gitignore
    fs::File::create(te.test_root().join("inner/.gitignore"))
        .unwrap()
        .write_all(b"foo")
        .unwrap();

    // Whitelist 'foo' via .fdignore
    fs::File::create(te.test_root().join(".fdignore"))
        .unwrap()
        .write_all(b"!foo")
        .unwrap();

    te.assert_output(&["foo"], "inner/foo");

    te.assert_output(&["--no-ignore-vcs", "foo"], "inner/foo");

    te.assert_output(&["--no-ignore", "foo"], "inner/foo");
}

/// Don't require git to respect gitignore (--no-require-git)
#[test]
fn test_respect_ignore_files() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    // Not in a git repo anymore
    fs::remove_dir(te.test_root().join(".git")).unwrap();

    // don't respect gitignore because we're not in a git repo
    te.assert_output(
        &["foo"],
        "a.foo
        gitignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    // respect gitignore because we set `--no-require-git`
    te.assert_output(
        &["--no-require-git", "foo"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    // make sure overriding works
    te.assert_output(
        &["--no-require-git", "--require-git", "foo"],
        "a.foo
        gitignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    te.assert_output(
        &["--no-require-git", "--no-ignore", "foo"],
        "a.foo
        gitignored.foo
        fdignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

/// VCS ignored files (--no-ignore-vcs)
#[test]
fn test_no_ignore_vcs() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--no-ignore-vcs", "foo"],
        "a.foo
        gitignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

/// Test that --no-ignore-vcs still respects .fdignored in parent directory
#[test]
fn test_no_ignore_vcs_child_dir() {
    let te = TestEnv::new(
        &["inner"],
        &["inner/fdignored.foo", "inner/foo", "inner/gitignored.foo"],
    );

    te.assert_output_subdirectory(
        "inner",
        &["--no-ignore-vcs", "foo"],
        "foo
        gitignored.foo",
    );
}

/// Custom ignore files (--ignore-file)
#[test]
fn test_custom_ignore_files() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    // Ignore 'C.Foo2' and everything in 'three'.
    fs::File::create(te.test_root().join("custom.ignore"))
        .unwrap()
        .write_all(b"C.Foo2\nthree")
        .unwrap();

    te.assert_output(
        &["--ignore-file", "custom.ignore", "foo"],
        "a.foo
        one/b.foo
        one/two/c.foo",
    );
}

/// Ignored files with ripgrep aliases (-u / -uu)
#[test]
fn test_no_ignore_aliases() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["-u", "foo"],
        ".hidden.foo
        a.foo
        fdignored.foo
        gitignored.foo
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

#[cfg(not(windows))]
#[test]
fn test_global_ignore() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES).global_ignore_file("one");
    te.assert_output(
        &[],
        "a.foo
    e1 e2
    symlink",
    );
}

#[cfg(not(windows))]
#[test_case("--unrestricted", ".hidden.foo
a.foo
fdignored.foo
gitignored.foo
one/b.foo
one/two/c.foo
one/two/C.Foo2
one/two/three/d.foo
one/two/three/directory_foo/"; "unrestricted")]
#[test_case("--no-ignore", "a.foo
fdignored.foo
gitignored.foo
one/b.foo
one/two/c.foo
one/two/C.Foo2
one/two/three/d.foo
one/two/three/directory_foo/"; "no-ignore")]
#[test_case("--no-global-ignore-file", "a.foo
one/b.foo
one/two/c.foo
one/two/C.Foo2
one/two/three/d.foo
one/two/three/directory_foo/"; "no-global-ignore-file")]
fn test_no_global_ignore(flag: &str, expected_output: &str) {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES).global_ignore_file("one");
    te.assert_output(&[flag, "foo"], expected_output);
}

/// Symlinks (--follow)
#[test]
fn test_follow() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--follow", "c.foo"],
        "one/two/c.foo
        one/two/C.Foo2
        symlink/c.foo
        symlink/C.Foo2",
    );
}

// File system boundaries (--one-file-system)
// Limited to Unix because, to the best of my knowledge, there is no easy way to test a use case
// file systems mounted into the tree on Windows.
// Not limiting depth causes massive delay under Darwin, see BurntSushi/ripgrep#1429
#[test]
#[cfg(unix)]
fn test_file_system_boundaries() {
    // Helper function to get the device ID for a given path
    // Inspired by https://github.com/BurntSushi/ripgrep/blob/8892bf648cfec111e6e7ddd9f30e932b0371db68/ignore/src/walk.rs#L1693
    fn device_num(path: impl AsRef<Path>) -> u64 {
        use std::os::unix::fs::MetadataExt;

        path.as_ref().metadata().map(|md| md.dev()).unwrap()
    }

    // Can't simulate file system boundaries
    let te = TestEnv::new(&[], &[]);

    let dev_null = Path::new("/dev/null");

    // /dev/null should exist in all sane Unixes. Skip if it doesn't exist for some reason.
    // Also skip should it be on the same device as the root partition for some reason.
    if !dev_null.is_file() || device_num(dev_null) == device_num("/") {
        return;
    }

    te.assert_output(
        &["--full-path", "--max-depth", "2", "^/dev/null$", "/"],
        "/dev/null",
    );
    te.assert_output(
        &[
            "--one-file-system",
            "--full-path",
            "--max-depth",
            "2",
            "^/dev/null$",
            "/",
        ],
        "",
    );
}

#[test]
fn test_follow_broken_symlink() {
    let mut te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    te.create_broken_symlink("broken_symlink")
        .expect("Failed to create broken symlink.");

    te.assert_output(
        &["symlink"],
        "broken_symlink
        symlink",
    );
    te.assert_output(
        &["--type", "symlink", "symlink"],
        "broken_symlink
        symlink",
    );

    te.assert_output(&["--type", "file", "symlink"], "");

    te.assert_output(
        &["--follow", "--type", "symlink", "symlink"],
        "broken_symlink",
    );
    te.assert_output(&["--follow", "--type", "file", "symlink"], "");
}

/// Null separator (--print0)
#[test]
fn test_print0() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--print0", "foo"],
        "./a.fooNULL
        ./one/b.fooNULL
        ./one/two/C.Foo2NULL
        ./one/two/c.fooNULL
        ./one/two/three/d.fooNULL
        ./one/two/three/directory_foo/NULL",
    );
}

/// Maximum depth (--max-depth)
#[test]
fn test_max_depth() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--max-depth", "3"],
        "a.foo
        e1 e2
        one/
        one/b.foo
        one/two/
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/
        symlink",
    );

    te.assert_output(
        &["--max-depth", "2"],
        "a.foo
        e1 e2
        one/
        one/b.foo
        one/two/
        symlink",
    );

    te.assert_output(
        &["--max-depth", "1"],
        "a.foo
        e1 e2
        one/
        symlink",
    );
}

/// Minimum depth (--min-depth)
#[test]
fn test_min_depth() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--min-depth", "3"],
        "one/two/c.foo
        one/two/C.Foo2
        one/two/three/
        one/two/three/d.foo
        one/two/three/directory_foo/",
    );

    te.assert_output(
        &["--min-depth", "4"],
        "one/two/three/d.foo
        one/two/three/directory_foo/",
    );
}

/// Exact depth (--exact-depth)
#[test]
fn test_exact_depth() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--exact-depth", "3"],
        "one/two/c.foo
        one/two/C.Foo2
        one/two/three/",
    );
}

/// Pruning (--prune)
#[test]
fn test_prune() {
    let dirs = &["foo/bar", "bar/foo", "baz"];
    let files = &[
        "foo/foo.file",
        "foo/bar/foo.file",
        "bar/foo.file",
        "bar/foo/foo.file",
        "baz/foo.file",
    ];

    let te = TestEnv::new(dirs, files);

    te.assert_output(
        &["foo"],
        "foo/
        foo/foo.file
        foo/bar/foo.file
        bar/foo.file
        bar/foo/
        bar/foo/foo.file
        baz/foo.file",
    );

    te.assert_output(
        &["--prune", "foo"],
        "foo/
        bar/foo/
        bar/foo.file
        baz/foo.file",
    );
}

/// Absolute paths (--absolute-path)
#[test]
fn test_absolute_path() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--absolute-path"],
        &format!(
            "{abs_path}/a.foo
            {abs_path}/e1 e2
            {abs_path}/one/
            {abs_path}/one/b.foo
            {abs_path}/one/two/
            {abs_path}/one/two/c.foo
            {abs_path}/one/two/C.Foo2
            {abs_path}/one/two/three/
            {abs_path}/one/two/three/d.foo
            {abs_path}/one/two/three/directory_foo/
            {abs_path}/symlink",
            abs_path = &abs_path
        ),
    );

    te.assert_output(
        &["--absolute-path", "foo"],
        &format!(
            "{abs_path}/a.foo
            {abs_path}/one/b.foo
            {abs_path}/one/two/c.foo
            {abs_path}/one/two/C.Foo2
            {abs_path}/one/two/three/d.foo
            {abs_path}/one/two/three/directory_foo/",
            abs_path = &abs_path
        ),
    );
}

/// Show absolute paths if the path argument is absolute
#[test]
fn test_implicit_absolute_path() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["foo", &abs_path],
        &format!(
            "{abs_path}/a.foo
            {abs_path}/one/b.foo
            {abs_path}/one/two/c.foo
            {abs_path}/one/two/C.Foo2
            {abs_path}/one/two/three/d.foo
            {abs_path}/one/two/three/directory_foo/",
            abs_path = &abs_path
        ),
    );
}

/// Absolute paths should be normalized
#[test]
fn test_normalized_absolute_path() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output_subdirectory(
        "one",
        &["--absolute-path", "foo", ".."],
        &format!(
            "{abs_path}/a.foo
            {abs_path}/one/b.foo
            {abs_path}/one/two/c.foo
            {abs_path}/one/two/C.Foo2
            {abs_path}/one/two/three/d.foo
            {abs_path}/one/two/three/directory_foo/",
            abs_path = &abs_path
        ),
    );
}

/// File type filter (--type)
#[test]
fn test_type() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--type", "f"],
        "a.foo
        e1 e2
        one/b.foo
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/d.foo",
    );

    te.assert_output(&["--type", "f", "e1"], "e1 e2");

    te.assert_output(
        &["--type", "d"],
        "one/
        one/two/
        one/two/three/
        one/two/three/directory_foo/",
    );

    te.assert_output(
        &["--type", "d", "--type", "l"],
        "one/
        one/two/
        one/two/three/
        one/two/three/directory_foo/
        symlink",
    );

    te.assert_output(&["--type", "l"], "symlink");
}

/// Test `--type executable`
#[cfg(unix)]
#[test]
fn test_type_executable() {
    use std::os::unix::fs::OpenOptionsExt;

    // This test assumes the current user isn't root
    // (otherwise if the executable bit is set for any level, it is executable for the current
    // user)
    if Uid::current().is_root() {
        return;
    }

    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    fs::OpenOptions::new()
        .create_new(true)
        .truncate(true)
        .write(true)
        .mode(0o777)
        .open(te.test_root().join("executable-file.sh"))
        .unwrap();

    fs::OpenOptions::new()
        .create(true)
        .truncate(true)
        .write(true)
        .mode(0o645)
        .open(te.test_root().join("not-user-executable-file.sh"))
        .unwrap();

    te.assert_output(&["--type", "executable"], "executable-file.sh");

    te.assert_output(
        &["--type", "executable", "--type", "directory"],
        "executable-file.sh
        one/
        one/two/
        one/two/three/
        one/two/three/directory_foo/",
    );
}

/// Test `--type empty`
#[test]
fn test_type_empty() {
    let te = TestEnv::new(&["dir_empty", "dir_nonempty"], &[]);

    create_file_with_size(te.test_root().join("0_bytes.foo"), 0);
    create_file_with_size(te.test_root().join("5_bytes.foo"), 5);

    create_file_with_size(te.test_root().join("dir_nonempty").join("2_bytes.foo"), 2);

    te.assert_output(
        &["--type", "empty"],
        "0_bytes.foo
        dir_empty/",
    );

    te.assert_output(
        &["--type", "empty", "--type", "file", "--type", "directory"],
        "0_bytes.foo
        dir_empty/",
    );

    te.assert_output(&["--type", "empty", "--type", "file"], "0_bytes.foo");

    te.assert_output(&["--type", "empty", "--type", "directory"], "dir_empty/");
}

/// File extension (--extension)
#[test]
fn test_extension() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--extension", "foo"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/three/d.foo",
    );

    te.assert_output(
        &["--extension", ".foo"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/three/d.foo",
    );

    te.assert_output(
        &["--extension", ".foo", "--extension", "foo2"],
        "a.foo
        one/b.foo
        one/two/c.foo
        one/two/three/d.foo
        one/two/C.Foo2",
    );

    te.assert_output(&["--extension", ".foo", "a"], "a.foo");

    te.assert_output(&["--extension", "foo2"], "one/two/C.Foo2");

    let te2 = TestEnv::new(&[], &["spam.bar.baz", "egg.bar.baz", "yolk.bar.baz.sig"]);

    te2.assert_output(
        &["--extension", ".bar.baz"],
        "spam.bar.baz
        egg.bar.baz",
    );

    te2.assert_output(&["--extension", "sig"], "yolk.bar.baz.sig");

    te2.assert_output(&["--extension", "bar.baz.sig"], "yolk.bar.baz.sig");

    let te3 = TestEnv::new(&[], &["latin1.e\u{301}xt", "smiley.☻"]);

    te3.assert_output(&["--extension", "☻"], "smiley.☻");

    te3.assert_output(&["--extension", ".e\u{301}xt"], "latin1.e\u{301}xt");

    let te4 = TestEnv::new(&[], &[".hidden", "test.hidden"]);

    te4.assert_output(&["--hidden", "--extension", ".hidden"], "test.hidden");
}

/// No file extension (test for the pattern provided in the --help text)
#[test]
fn test_no_extension() {
    let te = TestEnv::new(
        DEFAULT_DIRS,
        &["a.foo", "aa", "one/b.foo", "one/bb", "one/two/three/d"],
    );

    te.assert_output(
        &["^[^.]+$"],
        "aa
        one/
        one/bb
        one/two/
        one/two/three/
        one/two/three/d
        one/two/three/directory_foo/
        symlink",
    );

    te.assert_output(
        &["^[^.]+$", "--type", "file"],
        "aa
        one/bb
        one/two/three/d",
    );
}

/// Symlink as search directory
#[test]
fn test_symlink_as_root() {
    let mut te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    te.create_broken_symlink("broken_symlink")
        .expect("Failed to create broken symlink.");

    // From: http://pubs.opengroup.org/onlinepubs/9699919799/functions/getcwd.html
    // The getcwd() function shall place an absolute pathname of the current working directory in
    // the array pointed to by buf, and return buf. The pathname shall contain no components that
    // are dot or dot-dot, or are symbolic links.
    //
    // Key points:
    // 1. The path of the current working directory of a Unix process cannot contain symlinks.
    // 2. The path of the current working directory of a Windows process can contain symlinks.
    //
    // More:
    // 1. On Windows, symlinks are resolved after the ".." component.
    // 2. On Unix, symlinks are resolved immediately as encountered.

    let parent_parent = if cfg!(windows) { ".." } else { "../.." };
    te.assert_output_subdirectory(
        "symlink",
        &["", parent_parent],
        &format!(
            "{dir}/a.foo
            {dir}/broken_symlink
            {dir}/e1 e2
            {dir}/one/
            {dir}/one/b.foo
            {dir}/one/two/
            {dir}/one/two/c.foo
            {dir}/one/two/C.Foo2
            {dir}/one/two/three/
            {dir}/one/two/three/d.foo
            {dir}/one/two/three/directory_foo/
            {dir}/symlink",
            dir = &parent_parent
        ),
    );
}

#[test]
fn test_symlink_and_absolute_path() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);

    let expected_path = if cfg!(windows) { "symlink" } else { "one/two" };

    te.assert_output_subdirectory(
        "symlink",
        &["--absolute-path"],
        &format!(
            "{abs_path}/{expected_path}/c.foo
            {abs_path}/{expected_path}/C.Foo2
            {abs_path}/{expected_path}/three/
            {abs_path}/{expected_path}/three/d.foo
            {abs_path}/{expected_path}/three/directory_foo/",
            abs_path = &abs_path,
            expected_path = expected_path
        ),
    );
}

#[test]
fn test_symlink_as_absolute_root() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["", &format!("{abs_path}/symlink")],
        &format!(
            "{abs_path}/symlink/c.foo
            {abs_path}/symlink/C.Foo2
            {abs_path}/symlink/three/
            {abs_path}/symlink/three/d.foo
            {abs_path}/symlink/three/directory_foo/",
            abs_path = &abs_path
        ),
    );
}

#[test]
fn test_symlink_and_full_path() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);
    let root = te.system_root();
    let prefix = escape(&root.to_string_lossy());

    let expected_path = if cfg!(windows) { "symlink" } else { "one/two" };

    te.assert_output_subdirectory(
        "symlink",
        &[
            "--absolute-path",
            "--full-path",
            &format!("^{prefix}.*three"),
        ],
        &format!(
            "{abs_path}/{expected_path}/three/
            {abs_path}/{expected_path}/three/d.foo
            {abs_path}/{expected_path}/three/directory_foo/",
            abs_path = &abs_path,
            expected_path = expected_path
        ),
    );
}

#[test]
fn test_symlink_and_full_path_abs_path() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);
    let root = te.system_root();
    let prefix = escape(&root.to_string_lossy());
    te.assert_output(
        &[
            "--full-path",
            &format!("^{prefix}.*symlink.*three"),
            &format!("{abs_path}/symlink"),
        ],
        &format!(
            "{abs_path}/symlink/three/
            {abs_path}/symlink/three/d.foo
            {abs_path}/symlink/three/directory_foo/",
            abs_path = &abs_path
        ),
    );
}
/// Exclude patterns (--exclude)
#[test]
fn test_excludes() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--exclude", "*.foo"],
        "one/
        one/two/
        one/two/C.Foo2
        one/two/three/
        one/two/three/directory_foo/
        e1 e2
        symlink",
    );

    te.assert_output(
        &["--exclude", "*.foo", "--exclude", "*.Foo2"],
        "one/
        one/two/
        one/two/three/
        one/two/three/directory_foo/
        e1 e2
        symlink",
    );

    te.assert_output(
        &["--exclude", "*.foo", "--exclude", "*.Foo2", "foo"],
        "one/two/three/directory_foo/",
    );

    te.assert_output(
        &["--exclude", "one/two/", "foo"],
        "a.foo
        one/b.foo",
    );

    te.assert_output(
        &["--exclude", "one/**/*.foo"],
        "a.foo
        e1 e2
        one/
        one/two/
        one/two/C.Foo2
        one/two/three/
        one/two/three/directory_foo/
        symlink",
    );
}

#[test]
fn format() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--format", "path={}", "--path-separator=/"],
        "path=a.foo
        path=e1 e2
        path=one
        path=one/b.foo
        path=one/two
        path=one/two/C.Foo2
        path=one/two/c.foo
        path=one/two/three
        path=one/two/three/d.foo
        path=one/two/three/directory_foo
        path=symlink",
    );

    te.assert_output(
        &["foo", "--format", "noExt={.}", "--path-separator=/"],
        "noExt=a
        noExt=one/b
        noExt=one/two/C
        noExt=one/two/c
        noExt=one/two/three/d
        noExt=one/two/three/directory_foo",
    );

    te.assert_output(
        &["foo", "--format", "basename={/}", "--path-separator=/"],
        "basename=a.foo
        basename=b.foo
        basename=C.Foo2
        basename=c.foo
        basename=d.foo
        basename=directory_foo",
    );

    te.assert_output(
        &["foo", "--format", "name={/.}", "--path-separator=/"],
        "name=a
        name=b
        name=C
        name=c
        name=d
        name=directory_foo",
    );

    te.assert_output(
        &["foo", "--format", "parent={//}", "--path-separator=/"],
        "parent=.
        parent=one
        parent=one/two
        parent=one/two
        parent=one/two/three
        parent=one/two/three",
    );
}

/// Shell script execution (--exec)
#[test]
fn test_exec() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);
    // TODO Windows tests: D:file.txt \file.txt \\server\share\file.txt ...
    if !cfg!(windows) {
        te.assert_output(
            &["--absolute-path", "foo", "--exec", "echo"],
            &format!(
                "{abs_path}/a.foo
                {abs_path}/one/b.foo
                {abs_path}/one/two/C.Foo2
                {abs_path}/one/two/c.foo
                {abs_path}/one/two/three/d.foo
                {abs_path}/one/two/three/directory_foo",
                abs_path = &abs_path
            ),
        );

        te.assert_output(
            &["foo", "--exec", "echo", "{}"],
            "./a.foo
            ./one/b.foo
            ./one/two/C.Foo2
            ./one/two/c.foo
            ./one/two/three/d.foo
            ./one/two/three/directory_foo",
        );

        te.assert_output(
            &["foo", "--strip-cwd-prefix", "--exec", "echo", "{}"],
            "a.foo
            one/b.foo
            one/two/C.Foo2
            one/two/c.foo
            one/two/three/d.foo
            one/two/three/directory_foo",
        );

        te.assert_output(
            &["foo", "--exec", "echo", "{.}"],
            "a
            one/b
            one/two/C
            one/two/c
            one/two/three/d
            one/two/three/directory_foo",
        );

        te.assert_output(
            &["foo", "--exec", "echo", "{/}"],
            "a.foo
            b.foo
            C.Foo2
            c.foo
            d.foo
            directory_foo",
        );

        te.assert_output(
            &["foo", "--exec", "echo", "{/.}"],
            "a
            b
            C
            c
            d
            directory_foo",
        );

        te.assert_output(
            &["foo", "--exec", "echo", "{//}"],
            ".
            ./one
            ./one/two
            ./one/two
            ./one/two/three
            ./one/two/three",
        );

        te.assert_output(&["e1", "--exec", "printf", "%s.%s\n"], "./e1 e2.");
    }
}

// TODO test for windows
#[cfg(not(windows))]
#[test]
fn test_exec_multi() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &[
            "--absolute-path",
            "foo",
            "--exec",
            "echo",
            ";",
            "--exec",
            "echo",
            "test",
            "{/}",
        ],
        &format!(
            "{abs_path}/a.foo
                {abs_path}/one/b.foo
                {abs_path}/one/two/C.Foo2
                {abs_path}/one/two/c.foo
                {abs_path}/one/two/three/d.foo
                {abs_path}/one/two/three/directory_foo
                test a.foo
                test b.foo
                test C.Foo2
                test c.foo
                test d.foo
                test directory_foo",
            abs_path = &abs_path
        ),
    );

    te.assert_output(
        &[
            "e1", "--exec", "echo", "{.}", ";", "--exec", "echo", "{/}", ";", "--exec", "echo",
            "{//}", ";", "--exec", "echo", "{/.}",
        ],
        "e1 e2
        e1 e2
        .
        e1 e2",
    );

    // We use printf here because we need to suppress a newline and
    // echo -n is not POSIX-compliant.
    te.assert_output(
        &[
            "foo", "--exec", "printf", "%s", "{/}: ", ";", "--exec", "printf", "%s\\n", "{//}",
        ],
        "a.foo: .
        b.foo: ./one
        C.Foo2: ./one/two
        c.foo: ./one/two
        d.foo: ./one/two/three
        directory_foo: ./one/two/three",
    );
}

#[cfg(not(windows))]
#[test]
fn test_exec_nulls() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    te.assert_output(
        &["foo", "--print0", "--exec", "printf", "p=%s"],
        "p=./a.fooNULL
        p=./one/b.fooNULL
        p=./one/two/C.Foo2NULL
        p=./one/two/c.fooNULL
        p=./one/two/three/d.fooNULL
        p=./one/two/three/directory_fooNULL",
    );
}

#[test]
fn test_exec_batch() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);
    let te = te.normalize_line(true);

    // TODO Test for windows
    if !cfg!(windows) {
        te.assert_output(
            &["--absolute-path", "foo", "--exec-batch", "echo"],
            &format!(
                "{abs_path}/a.foo {abs_path}/one/b.foo {abs_path}/one/two/C.Foo2 {abs_path}/one/two/c.foo {abs_path}/one/two/three/d.foo {abs_path}/one/two/three/directory_foo",
                abs_path = &abs_path
            ),
        );

        te.assert_output(
            &["foo", "--exec-batch", "echo", "{}"],
            "./a.foo ./one/b.foo ./one/two/C.Foo2 ./one/two/c.foo ./one/two/three/d.foo ./one/two/three/directory_foo",
        );

        te.assert_output(
            &["foo", "--strip-cwd-prefix", "--exec-batch", "echo", "{}"],
            "a.foo one/b.foo one/two/C.Foo2 one/two/c.foo one/two/three/d.foo one/two/three/directory_foo",
        );

        te.assert_output(
            &["foo", "--exec-batch", "echo", "{/}"],
            "a.foo b.foo C.Foo2 c.foo d.foo directory_foo",
        );

        te.assert_output(
            &["no_match", "--exec-batch", "echo", "Matched: ", "{/}"],
            "",
        );

        te.assert_failure_with_error(
            &["foo", "--exec-batch", "echo", "{}", "{}"],
            "error: Only one placeholder allowed for batch commands\n\
            \n\
            Usage: fd [OPTIONS] [pattern] [path]...\n\
            \n\
            For more information, try '--help'.\n\
            ",
        );

        te.assert_failure_with_error(
            &["foo", "--exec-batch", "echo", "{/}", ";", "-x", "echo"],
            "error: the argument '--exec-batch <cmd>...' cannot be used with '--exec <cmd>...'\n\
            \n\
            Usage: fd --exec-batch <cmd>... <pattern> [path]...\n\
            \n\
            For more information, try '--help'.\n\
            ",
        );

        te.assert_failure_with_error(
            &["foo", "--exec-batch"],
            "error: a value is required for '--exec-batch <cmd>...' but none was supplied\n\
            \n\
            For more information, try '--help'.\n\
            ",
        );

        te.assert_failure_with_error(
            &["foo", "--exec-batch", "echo {}"],
            "error: First argument of exec-batch is expected to be a fixed executable\n\
            \n\
            Usage: fd [OPTIONS] [pattern] [path]...\n\
            \n\
            For more information, try '--help'.\n\
            ",
        );

        te.assert_failure_with_error(&["a.foo", "--exec-batch", "bash", "-c", "exit 1"], "");
    }
}

#[test]
fn test_exec_batch_multi() {
    // TODO test for windows
    if cfg!(windows) {
        return;
    }
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    let output = te.assert_success_and_get_output(
        ".",
        &[
            "foo",
            "--exec-batch",
            "echo",
            "{}",
            ";",
            "--exec-batch",
            "echo",
            "{/}",
        ],
    );
    let stdout = std::str::from_utf8(&output.stdout).unwrap();
    let lines: Vec<_> = stdout
        .lines()
        .map(|l| {
            let mut words: Vec<_> = l.split_whitespace().collect();
            words.sort_unstable();
            words
        })
        .collect();

    assert_eq!(
        lines,
        &[
            [
                "./a.foo",
                "./one/b.foo",
                "./one/two/C.Foo2",
                "./one/two/c.foo",
                "./one/two/three/d.foo",
                "./one/two/three/directory_foo"
            ],
            [
                "C.Foo2",
                "a.foo",
                "b.foo",
                "c.foo",
                "d.foo",
                "directory_foo"
            ],
        ]
    );

    te.assert_failure_with_error(
        &[
            "a.foo",
            "--exec-batch",
            "echo",
            ";",
            "--exec-batch",
            "bash",
            "-c",
            "exit 1",
        ],
        "",
    );
}

#[test]
fn test_exec_batch_with_limit() {
    // TODO Test for windows
    if cfg!(windows) {
        return;
    }

    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    let output = te.assert_success_and_get_output(
        ".",
        &["foo", "--batch-size=2", "--exec-batch", "echo", "{}"],
    );
    let stdout = String::from_utf8_lossy(&output.stdout);

    for line in stdout.lines() {
        assert_eq!(2, line.split_whitespace().count());
    }

    let mut paths: Vec<_> = stdout
        .lines()
        .flat_map(|line| line.split_whitespace())
        .collect();
    paths.sort_unstable();
    assert_eq!(
        &paths,
        &[
            "./a.foo",
            "./one/b.foo",
            "./one/two/C.Foo2",
            "./one/two/c.foo",
            "./one/two/three/d.foo",
            "./one/two/three/directory_foo"
        ],
    );
}

/// Shell script execution (--exec) with a custom --path-separator
#[test]
fn test_exec_with_separator() {
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);
    te.assert_output(
        &[
            "--path-separator=#",
            "--absolute-path",
            "foo",
            "--exec",
            "echo",
        ],
        &format!(
            "{abs_path}#a.foo
                {abs_path}#one#b.foo
                {abs_path}#one#two#C.Foo2
                {abs_path}#one#two#c.foo
                {abs_path}#one#two#three#d.foo
                {abs_path}#one#two#three#directory_foo",
            abs_path = abs_path.replace(std::path::MAIN_SEPARATOR, "#"),
        ),
    );

    te.assert_output(
        &["--path-separator=#", "foo", "--exec", "echo", "{}"],
        ".#a.foo
            .#one#b.foo
            .#one#two#C.Foo2
            .#one#two#c.foo
            .#one#two#three#d.foo
            .#one#two#three#directory_foo",
    );

    te.assert_output(
        &["--path-separator=#", "foo", "--exec", "echo", "{.}"],
        "a
            one#b
            one#two#C
            one#two#c
            one#two#three#d
            one#two#three#directory_foo",
    );

    te.assert_output(
        &["--path-separator=#", "foo", "--exec", "echo", "{/}"],
        "a.foo
            b.foo
            C.Foo2
            c.foo
            d.foo
            directory_foo",
    );

    te.assert_output(
        &["--path-separator=#", "foo", "--exec", "echo", "{/.}"],
        "a
            b
            C
            c
            d
            directory_foo",
    );

    te.assert_output(
        &["--path-separator=#", "foo", "--exec", "echo", "{//}"],
        ".
            .#one
            .#one#two
            .#one#two
            .#one#two#three
            .#one#two#three",
    );

    te.assert_output(
        &["--path-separator=#", "e1", "--exec", "printf", "%s.%s\n"],
        ".#e1 e2.",
    );
}

/// Non-zero exit code (--quiet)
#[test]
fn test_quiet() {
    let dirs = &[];
    let files = &["a.foo", "b.foo"];
    let te = TestEnv::new(dirs, files);

    te.assert_output(&["-q"], "");
    te.assert_output(&["--quiet"], "");
    te.assert_output(&["--has-results"], "");
    te.assert_failure_with_error(&["--quiet", "c.foo"], "")
}

/// Literal search (--fixed-strings)
#[test]
fn test_fixed_strings() {
    let dirs = &["test1", "test2"];
    let files = &["test1/a.foo", "test1/a_foo", "test2/Download (1).tar.gz"];
    let te = TestEnv::new(dirs, files);

    // Regex search, dot is treated as "any character"
    te.assert_output(
        &["a.foo"],
        "test1/a.foo
         test1/a_foo",
    );

    // Literal search, dot is treated as character
    te.assert_output(&["--fixed-strings", "a.foo"], "test1/a.foo");

    // Regex search, parens are treated as group
    te.assert_output(&["download (1)"], "");

    // Literal search, parens are treated as characters
    te.assert_output(
        &["--fixed-strings", "download (1)"],
        "test2/Download (1).tar.gz",
    );

    // Combine with --case-sensitive
    te.assert_output(&["--fixed-strings", "--case-sensitive", "download (1)"], "");
}

/// Filenames with invalid UTF-8 sequences
#[cfg(target_os = "linux")]
#[test]
fn test_invalid_utf8() {
    use std::ffi::OsStr;
    use std::os::unix::ffi::OsStrExt;

    let dirs = &["test1"];
    let files = &[];
    let te = TestEnv::new(dirs, files);

    fs::File::create(
        te.test_root()
            .join(OsStr::from_bytes(b"test1/test_\xFEinvalid.txt")),
    )
    .unwrap();

    te.assert_output(&["", "test1/"], "test1/test_�invalid.txt");

    te.assert_output(&["invalid", "test1/"], "test1/test_�invalid.txt");

    // Should not be found under a different extension
    te.assert_output(&["-e", "zip", "", "test1/"], "");
}

/// Filtering for file size (--size)
#[test]
fn test_size() {
    let te = TestEnv::new(&[], &[]);

    create_file_with_size(te.test_root().join("0_bytes.foo"), 0);
    create_file_with_size(te.test_root().join("11_bytes.foo"), 11);
    create_file_with_size(te.test_root().join("30_bytes.foo"), 30);
    create_file_with_size(te.test_root().join("3_kilobytes.foo"), 3 * 1000);
    create_file_with_size(te.test_root().join("4_kibibytes.foo"), 4 * 1024);

    // Zero and non-zero sized files.
    te.assert_output(
        &["", "--size", "+0B"],
        "0_bytes.foo
        11_bytes.foo
        30_bytes.foo
        3_kilobytes.foo
        4_kibibytes.foo",
    );

    // Zero sized files.
    te.assert_output(&["", "--size", "-0B"], "0_bytes.foo");
    te.assert_output(&["", "--size", "0B"], "0_bytes.foo");
    te.assert_output(&["", "--size=0B"], "0_bytes.foo");
    te.assert_output(&["", "-S", "0B"], "0_bytes.foo");

    // Files with 2 bytes or more.
    te.assert_output(
        &["", "--size", "+2B"],
        "11_bytes.foo
        30_bytes.foo
        3_kilobytes.foo
        4_kibibytes.foo",
    );

    // Files with 2 bytes or less.
    te.assert_output(&["", "--size", "-2B"], "0_bytes.foo");

    // Files with size between 1 byte and 11 bytes.
    te.assert_output(&["", "--size", "+1B", "--size", "-11B"], "11_bytes.foo");

    // Files with size equal 11 bytes.
    te.assert_output(&["", "--size", "11B"], "11_bytes.foo");

    // Files with size between 1 byte and 30 bytes.
    te.assert_output(
        &["", "--size", "+1B", "--size", "-30B"],
        "11_bytes.foo
        30_bytes.foo",
    );

    // Combine with a search pattern
    te.assert_output(&["^11_", "--size", "+1B", "--size", "-30B"], "11_bytes.foo");

    // Files with size between 12 and 30 bytes.
    te.assert_output(&["", "--size", "+12B", "--size", "-30B"], "30_bytes.foo");

    // Files with size between 31 and 100 bytes.
    te.assert_output(&["", "--size", "+31B", "--size", "-100B"], "");

    // Files with size between 3 kibibytes and 5 kibibytes.
    te.assert_output(&["", "--size", "+3ki", "--size", "-5ki"], "4_kibibytes.foo");

    // Files with size between 3 kilobytes and 5 kilobytes.
    te.assert_output(
        &["", "--size", "+3k", "--size", "-5k"],
        "3_kilobytes.foo
        4_kibibytes.foo",
    );

    // Files with size greater than 3 kilobytes and less than 3 kibibytes.
    te.assert_output(&["", "--size", "+3k", "--size", "-3ki"], "3_kilobytes.foo");

    // Files with size equal 4 kibibytes.
    te.assert_output(&["", "--size", "+4ki", "--size", "-4ki"], "4_kibibytes.foo");
    te.assert_output(&["", "--size", "4ki"], "4_kibibytes.foo");
}

#[cfg(test)]
fn create_file_with_modified<P: AsRef<Path>>(path: P, duration_in_secs: u64) {
    let st = SystemTime::now() - Duration::from_secs(duration_in_secs);
    let ft = filetime::FileTime::from_system_time(st);
    fs::File::create(&path).expect("creation failed");
    filetime::set_file_times(&path, ft, ft).expect("time modification failed");
}

#[cfg(test)]
fn remove_symlink<P: AsRef<Path>>(path: P) {
    #[cfg(unix)]
    fs::remove_file(path).expect("remove symlink");

    // On Windows, symlinks remember whether they point to files or directories, so try both
    #[cfg(windows)]
    fs::remove_file(path.as_ref())
        .or_else(|_| fs::remove_dir(path.as_ref()))
        .expect("remove symlink");
}

#[test]
fn test_modified_relative() {
    let te = TestEnv::new(&[], &[]);
    remove_symlink(te.test_root().join("symlink"));
    create_file_with_modified(te.test_root().join("foo_0_now"), 0);
    create_file_with_modified(te.test_root().join("bar_1_min"), 60);
    create_file_with_modified(te.test_root().join("foo_10_min"), 600);
    create_file_with_modified(te.test_root().join("bar_1_h"), 60 * 60);
    create_file_with_modified(te.test_root().join("foo_2_h"), 2 * 60 * 60);
    create_file_with_modified(te.test_root().join("bar_1_day"), 24 * 60 * 60);

    te.assert_output(
        &["", "--changed-within", "15min"],
        "foo_0_now
        bar_1_min
        foo_10_min",
    );

    te.assert_output(
        &["", "--change-older-than", "15min"],
        "bar_1_h
        foo_2_h
        bar_1_day",
    );

    te.assert_output(
        &["foo", "--changed-within", "12h"],
        "foo_0_now
        foo_10_min
        foo_2_h",
    );
}

#[cfg(test)]
fn change_file_modified<P: AsRef<Path>>(path: P, iso_date: &str) {
    let st = iso_date
        .parse::<Timestamp>()
        .map(SystemTime::from)
        .expect("invalid date");
    let ft = filetime::FileTime::from_system_time(st);
    filetime::set_file_times(path, ft, ft).expect("time modification failde");
}

#[test]
fn test_modified_absolute() {
    let te = TestEnv::new(&[], &["15mar2018", "30dec2017"]);
    remove_symlink(te.test_root().join("symlink"));
    change_file_modified(te.test_root().join("15mar2018"), "2018-03-15T12:00:00Z");
    change_file_modified(te.test_root().join("30dec2017"), "2017-12-30T23:59:00Z");

    te.assert_output(
        &["", "--change-newer-than", "2018-01-01 00:00:00"],
        "15mar2018",
    );
    te.assert_output(
        &["", "--changed-before", "2018-01-01 00:00:00"],
        "30dec2017",
    );
}

#[cfg(unix)]
#[test]
fn test_owner_ignore_all() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    te.assert_output(&["--owner", ":", "a.foo"], "a.foo");
    te.assert_output(&["--owner", "", "a.foo"], "a.foo");
}

#[cfg(unix)]
#[test]
fn test_owner_current_user() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    let uid = Uid::current();
    te.assert_output(&["--owner", &uid.to_string(), "a.foo"], "a.foo");
    if let Ok(Some(user)) = User::from_uid(uid) {
        te.assert_output(&["--owner", &user.name, "a.foo"], "a.foo");
    }
}

#[cfg(unix)]
#[test]
fn test_owner_current_group() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    let gid = Gid::current();
    te.assert_output(&["--owner", &format!(":{gid}"), "a.foo"], "a.foo");
    if let Ok(Some(group)) = Group::from_gid(gid) {
        te.assert_output(&["--owner", &format!(":{}", group.name), "a.foo"], "a.foo");
    }
}

#[cfg(target_os = "linux")]
#[test]
fn test_owner_root() {
    // This test assumes the current user isn't root
    if Uid::current().is_root() || Gid::current() == Gid::from_raw(0) {
        return;
    }
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);
    te.assert_output(&["--owner", "root", "a.foo"], "");
    te.assert_output(&["--owner", "0", "a.foo"], "");
    te.assert_output(&["--owner", ":root", "a.foo"], "");
    te.assert_output(&["--owner", ":0", "a.foo"], "");
}

#[test]
fn test_custom_path_separator() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["foo", "one", "--path-separator", "="],
        "one=b.foo
        one=two=c.foo
        one=two=C.Foo2
        one=two=three=d.foo
        one=two=three=directory_foo=",
    );
}

#[test]
fn test_base_directory() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--base-directory", "one"],
        "b.foo
        two/
        two/c.foo
        two/C.Foo2
        two/three/
        two/three/d.foo
        two/three/directory_foo/",
    );

    te.assert_output(
        &["--base-directory", "one/two/", "foo"],
        "c.foo
        C.Foo2
        three/d.foo
        three/directory_foo/",
    );

    // Explicit root path
    te.assert_output(
        &["--base-directory", "one", "foo", "two"],
        "two/c.foo
        two/C.Foo2
        two/three/d.foo
        two/three/directory_foo/",
    );

    // Ignore base directory when absolute path is used
    let (te, abs_path) = get_test_env_with_abs_path(DEFAULT_DIRS, DEFAULT_FILES);
    let abs_base_dir = &format!("{abs_path}/one/two/", abs_path = &abs_path);
    te.assert_output(
        &["--base-directory", abs_base_dir, "foo", &abs_path],
        &format!(
            "{abs_path}/a.foo
            {abs_path}/one/b.foo
            {abs_path}/one/two/c.foo
            {abs_path}/one/two/C.Foo2
            {abs_path}/one/two/three/d.foo
            {abs_path}/one/two/three/directory_foo/",
            abs_path = &abs_path
        ),
    );
}

#[test]
fn test_max_results() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    // Unrestricted
    te.assert_output(
        &["--max-results=0", "c.foo"],
        "one/two/C.Foo2
         one/two/c.foo",
    );

    // Limited to two results
    te.assert_output(
        &["--max-results=2", "c.foo"],
        "one/two/C.Foo2
         one/two/c.foo",
    );

    // Limited to one result. We could find either C.Foo2 or c.foo
    let assert_just_one_result_with_option = |option| {
        let output = te.assert_success_and_get_output(".", &[option, "c.foo"]);
        let stdout = String::from_utf8_lossy(&output.stdout)
            .trim()
            .replace(&std::path::MAIN_SEPARATOR.to_string(), "/");
        assert!(stdout == "one/two/C.Foo2" || stdout == "one/two/c.foo");
    };
    assert_just_one_result_with_option("--max-results=1");
    assert_just_one_result_with_option("-1");

    // check that --max-results & -1 conflict with --exec
    te.assert_failure(&["thing", "--max-results=0", "--exec=cat"]);
    te.assert_failure(&["thing", "-1", "--exec=cat"]);
    te.assert_failure(&["thing", "--max-results=1", "-1", "--exec=cat"]);
}

/// Filenames with non-utf8 paths are passed to the executed program unchanged
///
/// Note:
/// - the test is disabled on Darwin/OSX, since it coerces file names to UTF-8,
///   even when the requested file name is not valid UTF-8.
/// - the test is currently disabled on Windows because I'm not sure how to create
///   invalid UTF-8 files on Windows
#[cfg(all(unix, not(target_os = "macos")))]
#[test]
fn test_exec_invalid_utf8() {
    use std::ffi::OsStr;
    use std::os::unix::ffi::OsStrExt;

    let dirs = &["test1"];
    let files = &[];
    let te = TestEnv::new(dirs, files);

    fs::File::create(
        te.test_root()
            .join(OsStr::from_bytes(b"test1/test_\xFEinvalid.txt")),
    )
    .unwrap();

    te.assert_output_raw(
        &["", "test1/", "--exec", "echo", "{}"],
        b"test1/test_\xFEinvalid.txt\n",
    );

    te.assert_output_raw(
        &["", "test1/", "--exec", "echo", "{/}"],
        b"test_\xFEinvalid.txt\n",
    );

    te.assert_output_raw(&["", "test1/", "--exec", "echo", "{//}"], b"test1\n");

    te.assert_output_raw(
        &["", "test1/", "--exec", "echo", "{.}"],
        b"test1/test_\xFEinvalid\n",
    );

    te.assert_output_raw(
        &["", "test1/", "--exec", "echo", "{/.}"],
        b"test_\xFEinvalid\n",
    );
}

#[test]
fn test_list_details() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    // Make sure we can execute 'fd --list-details' without any errors.
    te.assert_success_and_get_output(".", &["--list-details"]);
}

#[test]
fn test_single_and_multithreaded_execution() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(&["--threads=1", "a.foo"], "a.foo");
    te.assert_output(&["--threads=16", "a.foo"], "a.foo");
}

/// Make sure that fd fails if numeric arguments can not be parsed
#[test]
fn test_number_parsing_errors() {
    let te = TestEnv::new(&[], &[]);

    te.assert_failure(&["--threads=a"]);
    te.assert_failure(&["-j", ""]);
    te.assert_failure(&["--threads=0"]);

    te.assert_failure(&["--min-depth=a"]);
    te.assert_failure(&["--mindepth=a"]);
    te.assert_failure(&["--max-depth=a"]);
    te.assert_failure(&["--maxdepth=a"]);
    te.assert_failure(&["--exact-depth=a"]);

    te.assert_failure(&["--max-buffer-time=a"]);

    te.assert_failure(&["--max-results=a"]);
}

#[test_case("--hidden", &["--no-hidden"] ; "hidden")]
#[test_case("--no-ignore", &["--ignore"] ; "no-ignore")]
#[test_case("--no-ignore-vcs", &["--ignore-vcs"] ; "no-ignore-vcs")]
#[test_case("--no-require-git", &["--require-git"] ; "no-require-git")]
#[test_case("--follow", &["--no-follow"] ; "follow")]
#[test_case("--absolute-path", &["--relative-path"] ; "absolute-path")]
#[test_case("-u", &["--ignore", "--no-hidden"] ; "u")]
#[test_case("-uu", &["--ignore", "--no-hidden"] ; "uu")]
fn test_opposing(flag: &str, opposing_flags: &[&str]) {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    let mut flags = vec![flag];
    flags.extend_from_slice(opposing_flags);
    let out_no_flags = te.assert_success_and_get_normalized_output(".", &[]);
    let out_opposing_flags = te.assert_success_and_get_normalized_output(".", &flags);

    assert_eq!(
        out_no_flags,
        out_opposing_flags,
        "{} should override {}",
        opposing_flags.join(" "),
        flag
    );
}

/// Print error if search pattern starts with a dot and --hidden is not set
/// (Unix only, hidden files on Windows work differently)
#[test]
#[cfg(unix)]
fn test_error_if_hidden_not_set_and_pattern_starts_with_dot() {
    let te = TestEnv::new(&[], &[".gitignore", ".whatever", "non-hidden"]);

    te.assert_failure(&["^\\.gitignore"]);
    te.assert_failure(&["--glob", ".gitignore"]);

    te.assert_output(&["--hidden", "^\\.gitignore"], ".gitignore");
    te.assert_output(&["--hidden", "--glob", ".gitignore"], ".gitignore");
    te.assert_output(&[".gitignore"], "");
}

#[test]
fn test_strip_cwd_prefix() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    te.assert_output(
        &["--strip-cwd-prefix", "."],
        "a.foo
        e1 e2
        one/
        one/b.foo
        one/two/
        one/two/c.foo
        one/two/C.Foo2
        one/two/three/
        one/two/three/d.foo
        one/two/three/directory_foo/
        symlink",
    );
}

/// When fd is ran from a non-existent working directory, but an existent
/// directory is passed in the arguments, it should still run fine
#[test]
#[cfg(all(not(windows), not(target_os = "illumos")))]
fn test_invalid_cwd() {
    let te = TestEnv::new(&[], &[]);

    let root = te.test_root().join("foo");
    fs::create_dir(&root).unwrap();
    std::env::set_current_dir(&root).unwrap();
    fs::remove_dir(&root).unwrap();

    let output = std::process::Command::new(te.test_exe())
        .arg("query")
        .arg(te.test_root())
        .output()
        .unwrap();

    if !output.status.success() {
        panic!("{output:?}");
    }
}

/// Test behavior of .git directory with various flags
#[test]
fn test_git_dir() {
    let te = TestEnv::new(
        &[".git/one", "other_dir/.git", "nested/dir/.git"],
        &[
            ".git/one/foo.a",
            ".git/.foo",
            ".git/a.foo",
            "other_dir/.git/foo1",
            "nested/dir/.git/foo2",
        ],
    );

    te.assert_output(
        &["--hidden", "foo"],
        ".git/one/foo.a
        .git/.foo
        .git/a.foo
        other_dir/.git/foo1
        nested/dir/.git/foo2",
    );
    te.assert_output(&["--no-ignore", "foo"], "");
    te.assert_output(
        &["--hidden", "--no-ignore", "foo"],
        ".git/one/foo.a
         .git/.foo
         .git/a.foo
         other_dir/.git/foo1
         nested/dir/.git/foo2",
    );
    te.assert_output(
        &["--hidden", "--no-ignore-vcs", "foo"],
        ".git/one/foo.a
         .git/.foo
         .git/a.foo
         other_dir/.git/foo1
         nested/dir/.git/foo2",
    );
}

#[test]
fn test_gitignore_parent() {
    let te = TestEnv::new(&["sub"], &[".abc", "sub/.abc"]);

    fs::File::create(te.test_root().join(".gitignore"))
        .unwrap()
        .write_all(b".abc\n")
        .unwrap();

    te.assert_output_subdirectory("sub", &["--hidden"], "");
    te.assert_output_subdirectory("sub", &["--hidden", "--search-path", "."], "");
}

#[test]
fn test_hyperlink() {
    let te = TestEnv::new(DEFAULT_DIRS, DEFAULT_FILES);

    #[cfg(unix)]
    let hostname = nix::unistd::gethostname().unwrap().into_string().unwrap();
    #[cfg(not(unix))]
    let hostname = "/";

    let expected = format!(
        "\x1b]8;;file://{}{}/a.foo\x1b\\a.foo\x1b]8;;\x1b\\",
        hostname,
        get_absolute_root_path(&te),
    );

    te.assert_output(&["--hyperlink=always", "a.foo"], &expected);
}

#[test]
fn test_ignore_contain() {
    let te = TestEnv::new(
        &["include", "exclude", "exclude/sub", "other"],
        &[
            "top",
            "include/foo",
            "exclude/CACHEDIR.TAG",
            "exclude/sub/nope",
            "other/ignoremyparent",
        ],
    );
    let expected = "include/
    include/foo
    symlink
    top";
    te.assert_output(
        &[
            "--ignore-contain=CACHEDIR.TAG",
            "--ignore-contain=ignoremyparent",
            ".",
        ],
        expected,
    );
}

#[test]
fn test_ignore_contain_precedence_over_depth_check() {
    let te = TestEnv::new(
        &["include", "exclude", "exclude/sub"],
        &[
            "top",
            "include/foo",
            "exclude/CACHEDIR.TAG",
            "exclude/sub/nope",
        ],
    );
    let expected = "include/foo";
    te.assert_output(
        &["--ignore-contain=CACHEDIR.TAG", "--min-depth=2", "."],
        expected,
    );
}

#[test]
fn test_ignore_contain_precedence_over_root_check() {
    let te = TestEnv::new(&["include"], &["CACHEDIR.TAG", "top", "include/foo"]);
    let expected = "";
    te.assert_output(&["--ignore-contain=CACHEDIR.TAG", "."], expected);
}
```

## File: `tests/testenv/mod.rs`
```rust
use std::env;
use std::fs;
use std::io::{self, Write};
#[cfg(unix)]
use std::os::unix;
#[cfg(windows)]
use std::os::windows;
use std::path::{Path, PathBuf};
use std::process;

use tempfile::TempDir;

/// Environment for the integration tests.
pub struct TestEnv {
    /// Temporary working directory.
    temp_dir: TempDir,

    /// Path to the *fd* executable.
    fd_exe: PathBuf,

    /// Normalize each line by sorting the whitespace-separated words
    normalize_line: bool,

    /// Temporary directory for storing test config (global ignore file)
    config_dir: Option<TempDir>,
}

/// Create the working directory and the test files.
fn create_working_directory(
    directories: &[&'static str],
    files: &[&'static str],
) -> Result<TempDir, io::Error> {
    let temp_dir = tempfile::Builder::new().prefix("fd-tests").tempdir()?;

    {
        let root = temp_dir.path();

        // Pretend that this is a Git repository in order for `.gitignore` files to be respected
        fs::create_dir_all(root.join(".git"))?;

        for directory in directories {
            fs::create_dir_all(root.join(directory))?;
        }

        for file in files {
            fs::File::create(root.join(file))?;
        }

        #[cfg(unix)]
        unix::fs::symlink(root.join("one/two"), root.join("symlink"))?;

        // Note: creating symlinks on Windows requires the `SeCreateSymbolicLinkPrivilege` which
        // is by default only granted for administrators.
        #[cfg(windows)]
        windows::fs::symlink_dir(root.join("one/two"), root.join("symlink"))?;

        fs::File::create(root.join(".fdignore"))?.write_all(b"fdignored.foo")?;

        fs::File::create(root.join(".gitignore"))?.write_all(b"gitignored.foo")?;
    }

    Ok(temp_dir)
}

fn create_config_directory_with_global_ignore(ignore_file_content: &str) -> io::Result<TempDir> {
    let config_dir = tempfile::Builder::new().prefix("fd-config").tempdir()?;
    let fd_dir = config_dir.path().join("fd");
    fs::create_dir(&fd_dir)?;
    let mut ignore_file = fs::File::create(fd_dir.join("ignore"))?;
    ignore_file.write_all(ignore_file_content.as_bytes())?;

    Ok(config_dir)
}

/// Find the *fd* executable.
fn find_fd_exe() -> PathBuf {
    // Read the location of the fd executable from the environment
    PathBuf::from(env::var("CARGO_BIN_EXE_fd").unwrap_or(env!("CARGO_BIN_EXE_fd").to_string()))
}

/// Format an error message for when *fd* did not exit successfully.
fn format_exit_error(args: &[&str], output: &process::Output) -> String {
    format!(
        "`fd {}` did not exit successfully.\nstdout:\n---\n{}---\nstderr:\n---\n{}---",
        args.join(" "),
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    )
}

/// Format an error message for when the output of *fd* did not match the expected output.
fn format_output_error(args: &[&str], expected: &str, actual: &str) -> String {
    // Generate diff text.
    let diff_text = diff::lines(expected, actual)
        .into_iter()
        .map(|diff| match diff {
            diff::Result::Left(l) => format!("-{l}"),
            diff::Result::Both(l, _) => format!(" {l}"),
            diff::Result::Right(r) => format!("+{r}"),
        })
        .collect::<Vec<_>>()
        .join("\n");

    format!(
        concat!(
            "`fd {}` did not produce the expected output.\n",
            "Showing diff between expected and actual:\n{}\n"
        ),
        args.join(" "),
        diff_text
    )
}

/// Normalize the output for comparison.
fn normalize_output(s: &str, trim_start: bool, normalize_line: bool) -> String {
    // Split into lines and normalize separators.
    let mut lines = s
        .replace('\0', "NULL\n")
        .lines()
        .map(|line| {
            let line = if trim_start { line.trim_start() } else { line };
            let line = line.replace('/', std::path::MAIN_SEPARATOR_STR);
            if normalize_line {
                let mut words: Vec<_> = line.split_whitespace().collect();
                words.sort_unstable();
                return words.join(" ");
            }
            line
        })
        .collect::<Vec<_>>();

    lines.sort();
    lines.join("\n")
}

/// Trim whitespace from the beginning of each line.
fn trim_lines(s: &str) -> String {
    s.lines()
        .map(|line| line.trim_start())
        .fold(String::new(), |mut str, line| {
            str.push_str(line);
            str.push('\n');
            str
        })
}

impl TestEnv {
    pub fn new(directories: &[&'static str], files: &[&'static str]) -> TestEnv {
        let temp_dir = create_working_directory(directories, files).expect("working directory");
        let fd_exe = find_fd_exe();

        TestEnv {
            temp_dir,
            fd_exe,
            normalize_line: false,
            config_dir: None,
        }
    }

    pub fn normalize_line(self, normalize: bool) -> TestEnv {
        TestEnv {
            temp_dir: self.temp_dir,
            fd_exe: self.fd_exe,
            normalize_line: normalize,
            config_dir: self.config_dir,
        }
    }

    pub fn global_ignore_file(self, content: &str) -> TestEnv {
        let config_dir =
            create_config_directory_with_global_ignore(content).expect("config directory");
        TestEnv {
            config_dir: Some(config_dir),
            ..self
        }
    }

    /// Create a broken symlink at the given path in the temp_dir.
    pub fn create_broken_symlink<P: AsRef<Path>>(
        &mut self,
        link_path: P,
    ) -> Result<PathBuf, io::Error> {
        let root = self.test_root();
        let broken_symlink_link = root.join(link_path);
        {
            let temp_target_dir = tempfile::Builder::new()
                .prefix("fd-tests-broken-symlink")
                .tempdir()?;
            let broken_symlink_target = temp_target_dir.path().join("broken_symlink_target");
            fs::File::create(&broken_symlink_target)?;
            #[cfg(unix)]
            unix::fs::symlink(&broken_symlink_target, &broken_symlink_link)?;
            #[cfg(windows)]
            windows::fs::symlink_file(&broken_symlink_target, &broken_symlink_link)?;
        }
        Ok(broken_symlink_link)
    }

    /// Get the root directory for the tests.
    pub fn test_root(&self) -> PathBuf {
        self.temp_dir.path().to_path_buf()
    }

    /// Get the path of the fd executable.
    #[cfg_attr(windows, allow(unused))]
    pub fn test_exe(&self) -> &PathBuf {
        &self.fd_exe
    }

    /// Get the root directory of the file system.
    pub fn system_root(&self) -> PathBuf {
        let mut components = self.temp_dir.path().components();
        PathBuf::from(components.next().expect("root directory").as_os_str())
    }

    /// Assert that calling *fd* in the specified path under the root working directory,
    /// and with the specified arguments produces the expected output.
    pub fn assert_success_and_get_output<P: AsRef<Path>>(
        &self,
        path: P,
        args: &[&str],
    ) -> process::Output {
        // Run *fd*.
        let output = self.run_command(path.as_ref(), args);

        // Check for exit status.
        if !output.status.success() {
            panic!("{}", format_exit_error(args, &output));
        }

        output
    }

    pub fn assert_success_and_get_normalized_output<P: AsRef<Path>>(
        &self,
        path: P,
        args: &[&str],
    ) -> String {
        let output = self.assert_success_and_get_output(path, args);
        normalize_output(
            &String::from_utf8_lossy(&output.stdout),
            false,
            self.normalize_line,
        )
    }

    /// Assert that calling *fd* with the specified arguments produces the expected output.
    pub fn assert_output(&self, args: &[&str], expected: &str) {
        self.assert_output_subdirectory(".", args, expected)
    }

    /// Similar to assert_output, but able to handle non-utf8 output
    #[cfg(all(unix, not(target_os = "macos")))]
    pub fn assert_output_raw(&self, args: &[&str], expected: &[u8]) {
        let output = self.assert_success_and_get_output(".", args);

        assert_eq!(expected, &output.stdout[..]);
    }

    /// Assert that calling *fd* in the specified path under the root working directory,
    /// and with the specified arguments produces the expected output.
    pub fn assert_output_subdirectory<P: AsRef<Path>>(
        &self,
        path: P,
        args: &[&str],
        expected: &str,
    ) {
        // Normalize both expected and actual output.
        let expected = normalize_output(expected, true, self.normalize_line);
        let actual = self.assert_success_and_get_normalized_output(path, args);

        // Compare actual output to expected output.
        if expected != actual {
            panic!("{}", format_output_error(args, &expected, &actual));
        }
    }

    /// Assert that calling *fd* with the specified arguments produces the expected error,
    /// and does not succeed.
    pub fn assert_failure_with_error(&self, args: &[&str], expected: &str) {
        let status = self.assert_error_subdirectory(".", args, Some(expected));
        if status.success() {
            panic!("error '{expected}' did not occur.");
        }
    }

    /// Assert that calling *fd* with the specified arguments does not succeed.
    pub fn assert_failure(&self, args: &[&str]) {
        let status = self.assert_error_subdirectory(".", args, None);
        if status.success() {
            panic!("Failure did not occur as expected.");
        }
    }

    /// Assert that calling *fd* with the specified arguments produces the expected error.
    pub fn assert_error(&self, args: &[&str], expected: &str) -> process::ExitStatus {
        self.assert_error_subdirectory(".", args, Some(expected))
    }

    fn run_command(&self, path: &Path, args: &[&str]) -> process::Output {
        // Setup *fd* command.
        let mut cmd = process::Command::new(&self.fd_exe);
        cmd.current_dir(self.temp_dir.path().join(path));
        if let Some(config_dir) = &self.config_dir {
            cmd.env("XDG_CONFIG_HOME", config_dir.path());
        } else {
            cmd.arg("--no-global-ignore-file");
        }
        // Make sure LS_COLORS is unset to ensure consistent
        // color output
        cmd.env("LS_COLORS", "");
        cmd.args(args);

        // Run *fd*.
        cmd.output().expect("fd output")
    }

    /// Assert that calling *fd* in the specified path under the root working directory,
    /// and with the specified arguments produces an error with the expected message.
    fn assert_error_subdirectory<P: AsRef<Path>>(
        &self,
        path: P,
        args: &[&str],
        expected: Option<&str>,
    ) -> process::ExitStatus {
        let output = self.run_command(path.as_ref(), args);

        if let Some(expected) = expected {
            // Normalize both expected and actual output.
            let expected_error = trim_lines(expected);
            let actual_err = trim_lines(&String::from_utf8_lossy(&output.stderr));

            // Compare actual output to expected output.
            if !actual_err.trim_start().starts_with(&expected_error) {
                panic!(
                    "{}",
                    format_output_error(args, &expected_error, &actual_err)
                );
            }
        }

        output.status
    }
}
```

