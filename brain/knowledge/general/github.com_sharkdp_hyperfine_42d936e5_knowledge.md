---
id: github.com-sharkdp-hyperfine-42d936e5-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:21.805556
---

# KNOWLEDGE EXTRACT: github.com_sharkdp_hyperfine_42d936e5
> **Extracted on:** 2026-04-01 11:38:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521415/github.com_sharkdp_hyperfine_42d936e5

---

## File: `.gitignore`
```

/target/
**/*.rs.bk
```

## File: `CHANGELOG.md`
```markdown
# v1.20.0

## Features

- Add `--reference-name` option to give a meaningful name to the reference command, see #808 (@niklasdewally)
- The `--ignore-failure` option now supports a comma-separated list of exit codes to ignore (e.g., `--ignore-failure=1,2`), see #836 (@sharkdp)
- Python scripts: Add `--time-unit` option to `advanced_statistics.py` (@sharkdp)
- Python scripts: Add new `plot_benchmarks.py` script for plotting collections of benchmarks, see #806 (@marxin)

## Bugfixes

- Fix bug where naming individual commands with parameter scan was not working correctly, see #794 (@teofr)

## Other

- Restrict `cat` tests to Unix environments, see #776 and #777 (@ritvikos)

# v1.19.0

## Features

- Add a new `--reference <cmd>` option to specify a reference command for the relative speed comparison, see #579, #577 and #744 (@sharkdp)
- Add `--conclude` argument (analog to `--prepare`), see #565 and #719 (@jackoconnordev)
- Allow `--output=…` to appear once for each command, enabling use cases like `hyperfine --output=null my-cmd --output=./file.log my-cmd`, see #529 and #775 (@sharkdp)
- The environment variable `$HYPERFINE_ITERATION` will now contain the current iteration number for each benchmarked command, see #775 (@sharkdp)
- Add iteration information to failure error message, see #771 and #772 (@sharkdp)
- Python scripts: 
  - legend modification parameters and output DPI, see #758 (@Spreadcat)
  - Nicer whiskers plot, see #727 (@serpent7776)

## Bugfixes

- ETA not clearly visible on terminals with a block cursor, see #698 and #699 (@overclockworked64)
- Fix zsh completions, see #717 (@xzfc)

## Other

- Build binaries for aarch64-apple-darwin, see #728 (@Phault)
- Various cleanups (@hamirmahal, @one230six)

# v1.18.0

## Features

- Add support for microseconds via `--time-unit microsecond`, see #684 (@sharkdp)

## Bugfixes

- Proper argument quoting on Windows CMD, see #296 and #678 (@PedroWitzel)


# v1.17.0

## Features

- Add new `--sort` option to control the order in the rel. speed comparison and in markup export formats, see #601, #614, #655 (@sharkdp)
- Parameters which are unused in the command line are now displayed in parentheses, see #600 and #644 (@sharkdp).
- Added `--log-count` option for histogram plots, see `scripts/plot_histogram.py` (@sharkdp)

## Changes

- Updated hyperfine to use `windows-sys` instead of the unmaintained `winapi`, see #624, #639, #636, #641 (@clemenswasser)
- Silenced deprecation warning in Python scripts, see #633 (@nicovank)
- Major update of the man page, see 0ce6578, #647 (@sharkdp)

## Bugfixes

- Do not export intermediate results to stdout when using `-` as a file name, see #640 and #643 (@sharkdp)
- Markup exporting does not fail if benchmark results are zero, see #642 (@sharkdp)


# v1.16.1

## Bugfixes

- Fix line-wrapping of `--help` text (@sharkdp)
- Fix `--input=null` (@sharkdp)


# v1.16.0

## Features

- Added new `--input` option, see #541 and #563 (@snease)
- Added possibility to specify `-` as the filename in the
  `--export-*` options, see #615 and #623 (@humblepenguinn)

## Changes

- Improve hints for outlier warnings if `--warmup` or `--prepare` are in use already,
  see #570 (@sharkdp)

## Bugfixes

- Fix uncolored output on Windows if `TERM` is not set, see #583 (@nabijaczleweli)
- On Windows, only run `cmd.exe` with the `/C` option. Use `-c` for all other shells.
  See #568 and #582 (@FilipAndersson245)

## Other

- Thanks to @berombau for working on dependency upgrades, see #584
- Fixed installationm on Windows, see #595 and #596 (@AntoniosBarotsis)


# v1.15.0

## Features

- Disable colorized output in case of `TERM=dumb` or `NO_COLOR=1`, see #542 and #555 (@nabijaczleweli)
- Add new (experimental) `--min-benchmarking-time <secs>` option, see #527 (@sharkdp)

## Bugfixes

- Fix user and kernel times on Windows, see #368 and #538 (@clemenswasser)

## Other

- Improve `--help` texts of `--export-*` options, see #506 and #522 (@Engineer-of-Efficiency)


# v1.14.0

## Features

- Add a new `--output={null,pipe,inherit,<FILE>}` option to control
  where the output of the benchmarked program is redirected (if at all),
  see #377 and #509 (@tavianator, originally suggested by @BurntSushi)
- Add Emacs org-mode as a new export format, see #491 (@ppaulweber)


# v1.13.0

## Features

- Added a new `--shell=none`/`-N` option to disable the intermediate
  shell for executing the benchmarked commands. Hyperfine normally
  measures and subtracts the shell spawning time, but the intermediate
  shell always introduces a certain level of measurement noise. Using
  `--shell=none`/`-N` allows users to benchmark very fast commands
  (with a runtime on the order of a few milliseconds). See #336, #429,
  and #487 (@cipriancraciun and @sharkdp)
- Added `--setup`/`-s` option that can be used to run `make all` or
  similar. It runs once per set of tests, like `--cleanup`/`-c` (@avar)
- Added new `plot_progression.py` script to debug background interference
  effects.

## Changes

- Breaking change: the `-s` short option for `--style` is now used for
  the new `--setup` option.
- The environment offset randomization is now also available on Windows,
  see #484

## Other

- Improved documentation and test coverage, cleaned up code base for
  future improvements.


# v1.12.0

## Features

- `--command-name` can now take parameter names from `--parameter-*` options, see #351 and #391 (@silathdiir)
- Exit codes (or signals) are now printed in cases of command failures, see #342 (@KaindlJulian)
- Exit codes are now part of the JSON output, see #371 (@JordiChauzi)
- Colorized output should now be enabled on Windows by default, see #427

## Changes

- When `--export-*` commands are used, result files are created before benchmark execution
  to fail early in case of, e.g., wrong permissions. See #306 (@s1ck).
- When `--export-*` options are used, result files are written after each individual
  benchmark command instead of writing after all benchmarks have finished. See #306 (@s1ck).
- Reduce number of shell startup time measurements from 200 to 50, generally speeding up benchmarks. See #378
- User and system time are now in consistent time units, see #408 and #409 (@film42)



# v1.11.0

## Features

- The `-L`/`--parameter-list` option can now be specified multiple times to
  evaluate all possible combinations of the listed parameters:

  ``` bash
  hyperfine -L number 1,2 -L letter a,b,c \
      "echo {number}{letter}" \
      "printf '%s\n' {number}{letter}"
  # runs 12 benchmarks: 2 commands (echo and printf) times 6 combinations of
  # the "letter" and "number" parameters
  ```

  See: #253, #318 (@wchargin)

- Add CLI option to identify a command with a custom name, see #326 (@scampi)

## Changes

- When parameters are used with `--parameter-list` or `--parameter-scan`, the JSON export format
  now contains a dictionary `parameters` instead of a single key `parameter`. See #253, #318.
- The `plot_parametrized.py` script now infers the parameter name, and its `--parameter-name`
  argument has been deprecated. See #253, #318.

## Bugfixes

- Fix a bug in the outlier detection which would only detect "slow outliers" but not the fast
  ones (runs that are much faster than the rest of the benchmarking runs), see #329
- Better error messages for very fast commands that would lead to inf/nan results in the relative
  speed comparison, see #319
- Show error message if `--warmup` or `--*runs` arguments can not be parsed, see #337
- Keep output colorized when the output is not interactive and `--style=full` or `--style=color` is used.


# v1.10.0

## Features

- Hyperfine now comes with shell completion files for Bash, Zsh, Fish
  and PowerShell, see #290 (@four0000four).
- Hyperfine now comes with a basic man page, see #257 (@cadeef)
- During execution of benchmarks, hyperfine will now set a `HYPERFINE_RANDOMIZED_ENVIRONMENT_OFFSET` environment variable in order to randomize the memory layout. See #235 and #241 for references and details.
- A few enhancements for the histogram plotting scripts and the
  advanced statistics script
- Updates for the `plot_whisker.py` script, see #275 (@ghaiklor)

## Bugfixes

- Fix Spin Icon on Windows, see #229
- A few typos have been fixed, see #292 (@McMartin)

## Packaging

- `hyperfine` is now available on MacPorts for macOS, see #281 (@herbygillot)
- `hyperfine` is now available on OpenBSD, see #289 (@minusf)

Package authors: note that Hyperfine now comes with a set of shell completion files and a man page (see above)

# v1.9.0

## Features

- The new `--parameter-list <VAR> <VALUES>` option can be used to run
  a parametrized benchmark on a user-specified list of values.
  This is similar to `--parameter-scan <VAR> <MIN> <MAX>`, but doesn't
  necessarily required numeric arguments.

  ``` bash
  hyperfine --parameter-list compiler "gcc,clang" \
      "{compiler} -O2 main.cpp"
  ```

  See: #227, #234 (@JuanPotato)

- Added `none` as a possible choice for the `--style` option to
  run `hyperfine` without any output, see #193 (@knidarkness)

- Added a few new scripts for plotting various types of benchmark
  results (https://github.com/sharkdp/hyperfine/tree/master/scripts)

## Changes

- The `--prepare` command is now also run during the warmup
  phase, see #182 (@sseemayer)

- Better estimation of the remaining benchmark time due to an update
  of the `indicatif` crate.

## Other

- `hyperfine` is now available on NixOS, see #240 (@tuxinaut)

# v1.8.0

## Features

- The `--prepare <CMD>` option can now be specified multiple times to
  run specific preparation commands for each of the benchmarked programs:

  ``` bash
  hyperfine --prepare "make clean; git checkout master"  "make" \
            --prepare "make clean; git checkout feature" "make"
  ```

  See: #216, #218 (@iamsauravsharma)

- Added a new [`welch_ttest.py`](https://github.com/sharkdp/hyperfine/blob/master/scripts/welch_ttest.py) script to test whether or not the two benchmark
  results are the same, see #222 (@uetchy)

- The Markdown export has been improved. The relative speed is now exported
  with a higher precision (see #208) and includes the standard deviation
  (see #225).

## Other

- Improved documentation for [`scripts`](https://github.com/sharkdp/hyperfine/tree/master/scripts) folder (@matthieusb)

# v1.7.0

## Features

- Added a new `-D`,`--parameter-step-size` option that can be used to control
  the step size for `--parameter-scan` benchmarks. In addition, decimal numbers
  are now allowed for parameter scans. For example, the following command runs
  `sleep 0.3`, `sleep 0.5` and `sleep 0.7`:
  ``` bash
  hyperfine --parameter-scan delay 0.3 0.7 -D 0.2 'sleep {delay}'
  ```
  For more details, see #184 (@piyushrungta25)

## Other

- hyperfine is now in the official Alpine repositories, see #177 (@maxice8, @5paceToast)
- hyperfine is now in the official Fedora repositories, see #196 (@ignatenkobrain)
- hyperfine is now in the official Arch Linux repositories
- hyperfine can be installed on FreeBSD, see #204 (@0mp)
- Enabled LTO for slightly smaller binary sizes, see #179 (@Calinou)
- Various small improvements all over the code base, see #194 (@phimuemue)

# v1.6.0

## Features

- Added a `-c, --cleanup <CMD>` option to execute `CMD` after the completion of all benchmarking runs for a given command. This is useful if the commands to be benchmarked produce artifacts that need to be cleaned up. See #91 (@RalfJung and @colinwahl)
- Add parameter values (for `--parameter-scan` benchmarks) to exported CSV and JSON files. See #131 (@bbannier)
- Added AsciiDoc export option, see #137 (@5paceToast)
- The relative speed is now part of the Markdown export, see #127 (@mathiasrw and @sharkdp).
- The *median* run time is now exported via CSV and JSON, see #171 (@hosewiejacke and @sharkdp).

## Other

- Hyperfine has been updated to Rust 2018 (@AnderEnder). The minimum supported Rust version is now 1.31.

# v1.5.0

## Features

- Show the number of runs in `hyperfine`s output (@tcmal)
- Added two Python scripts to post-process exported benchmark results (see [`scripts/`](https://github.com/sharkdp/hyperfine/tree/master/scripts) folder)

## Other

- Refined `--help` text for the `--export-*` flags (@psteinb)
- Added Snapcraft file (@popey)
- Small improvements in the progress bar "experience".

# v1.4.0

## Features

- Added `-S`/`--shell` option to override the default shell, see #61 (@mqudsi and @jasonpeacock)
- Added `-u`/`--time-unit` option to change the unit of time (`second` or `millisecond`), see #80 (@jasonpeacock)
- Markdown export auto-selects time unit, see #71 (@jasonpeacock)

# v1.3.0

## Feature

- Compute and print standard deviation of the speed ratio, see #83 (@Shnatsel)
- More compact output format, see #70  (@jasonpeacock)
- Added `--style=color`, see #70 (@jasonpeacock)
- Added options to specify the max/exact numbers of runs, see #77 (@orium)

## Bugfixes

- Change Windows `cmd` interpreter to `cmd.exe` to prevent accidentally calling other programs, see #74 (@tathanhdinh)

## Other

- Binary releases for Windows are now available, see #87

# v1.2.0

- Support parameters in preparation commands, see #68 (@siiptuo)
- Updated dependencies, see #69. The minimum required Rust version is now 1.24.

# v1.1.0

* Added `--show-output` option (@chrisduerr and @sevagh)
* Refactoring work (@stevepentland)

# v1.0.0

## Features

* Support for various export-formats like CSV, JSON and Markdown - see #38, #44, #49, #42 (@stevepentland)
* Summary output that compares the different benchmarks, see #6 (@stevepentland)
* Parameterized benchmarks via `-P`, `--parameter-scan <VAR> <MIN> <MAX>`, see #19

## Thanks

I'd like to say a big THANK YOU to @stevepentland for implementing new features,
for reviewing pull requests and for giving very valuable feedback.

# v0.5.0

* Proper Windows support (@stevepentland)
* Added `--style auto/basic/nocolor/full` option (@stevepentland)
* Correctly estimate the full execution time, see #27 (@rleungx)
* Added Void Linux install instructions (@wpbirney)

# v0.4.0

- New `--style` option to disable output coloring and interactive CLI features, see #24 (@stevepentland)
- Statistical outlier detection, see #23 #18

# v0.3.0

## Features

- In addition to 'real' (wall clock) time, Hyperfine can now also measure 'user' and 'system' time (see #5).
- Added `--prepare` option that can be used to clear up disk caches before timing runs, for example (see #8).

## Other

- [Arch Linux package](https://aur.archlinux.org/packages/hyperfine) for Hyperfine (@jD91mZM2).
- Ubuntu/Debian packages are now are available.

# v0.2.0

Initial public release
```

## File: `CITATION.cff`
```
cff-version: 1.2.0
title: hyperfine
message: >-
  If you use this software in scientific
  publications, please consider citing it using the
  metadata from this file.
type: software
authors:
  - given-names: David
    family-names: Peter
    email: mail@david-peter.de
    orcid: 'https://orcid.org/0000-0001-7950-9915'
repository-code: 'https://github.com/sharkdp/hyperfine'
abstract: A command-line benchmarking tool.
license: MIT
version: 1.16.1
date-released: '2023-03-21'
```

## File: `Cargo.toml`
```
[package]
authors = ["David Peter <mail@david-peter.de>"]
categories = ["command-line-utilities"]
description = "A command-line benchmarking tool"
homepage = "https://github.com/sharkdp/hyperfine"
license = "MIT OR Apache-2.0"
name = "hyperfine"
readme = "README.md"
repository = "https://github.com/sharkdp/hyperfine"
version = "1.20.0"
edition = "2018"
build = "build.rs"
rust-version = "1.88.0"

[features]
# Use the nightly feature windows_process_extensions_main_thread_handle
windows_process_extensions_main_thread_handle = []

[dependencies]
colored = "2.1"
indicatif = "=0.17.4"
statistical = "1.0"
csv = "1.3"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
rust_decimal = "1.36"
rand = "0.8"
shell-words = "1.0"
thiserror = "2.0"
anyhow = "1.0"

[target.'cfg(not(windows))'.dependencies]
libc = "0.2"

[target.'cfg(windows)'.dependencies]
windows-sys = { version = "0.59", features = [
    "Win32_Foundation",
    "Win32_Security",
    "Win32_System_JobObjects",
    "Win32_System_LibraryLoader",
    "Win32_System_Threading",
] }

[target.'cfg(all(windows, not(windows_process_extensions_main_thread_handle)))'.dependencies]
once_cell = "1.19"

[target.'cfg(target_os="linux")'.dependencies]
nix = { version = "0.29", features = ["zerocopy"] }

[dependencies.clap]
version = "4"
default-features = false
features = [
    "suggestions",
    "color",
    "wrap_help",
    "cargo",
    "help",
    "usage",
    "error-context",
]

[dev-dependencies]
approx = "0.5"
assert_cmd = "2.0"
insta = { version = "1.41.1", features = ["yaml"] }
predicates = "3.1"
tempfile = "3.23"

[profile.dev.package]
insta.opt-level = 3
similar.opt-level = 3

[build-dependencies]
clap = "4.5.48"
clap_complete = "4.2.1"

[profile.release]
lto = true
strip = true
codegen-units = 1
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

   Copyright [yyyy] [name of copyright owner]

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

Copyright (c) 2018-2022 David Peter, and all hyperfine contributors

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

## File: `README.md`
```markdown
# hyperfine
[![CICD](https://github.com/sharkdp/hyperfine/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/hyperfine/actions/workflows/CICD.yml)
[![Version info](https://img.shields.io/crates/v/hyperfine.svg)](https://crates.io/crates/hyperfine)
[中文](https://github.com/chinanf-boy/hyperfine-zh)

A command-line benchmarking tool.

**Demo**: Benchmarking [`fd`](https://github.com/sharkdp/fd) and
[`find`](https://www.gnu.org/software/findutils/):

![hyperfine](https://i.imgur.com/z19OYxE.gif)

### Sponsors

A special *thank you* goes to our biggest <a href="doc/sponsors.md">sponsor</a>:<br>

<a href="https://www.warp.dev/hyperfine">
  <img src="doc/sponsors/warp-logo.png" width="200" alt="Warp">
  <br>
  <strong>Warp, the intelligent terminal</strong>
  <br>
  <sub>Available on MacOS, Linux, Windows</sub>
</a>

## Features

* Statistical analysis across multiple runs.
* Support for arbitrary shell commands.
* Constant feedback about the benchmark progress and current estimates.
* Warmup runs can be executed before the actual benchmark.
* Cache-clearing commands can be set up before each timing run.
* Statistical outlier detection to detect interference from other programs and caching effects.
* Export results to various formats: CSV, JSON, Markdown, AsciiDoc.
* Parameterized benchmarks (e.g. vary the number of threads).
* Cross-platform

## Usage

### Basic benchmarks

To run a benchmark, you can simply call `hyperfine <command>...`. The argument(s) can be any
shell command. For example:
```sh
hyperfine 'sleep 0.3'
```

Hyperfine will automatically determine the number of runs to perform for each command. By default,
it will perform *at least* 10 benchmarking runs and measure for at least 3 seconds. To change this,
you can use the `-r`/`--runs` option:
```sh
hyperfine --runs 5 'sleep 0.3'
```

If you want to compare the runtimes of different programs, you can pass multiple commands:
```sh
hyperfine 'hexdump file' 'xxd file'
```

### Warmup runs and preparation commands

For programs that perform a lot of disk I/O, the benchmarking results can be heavily influenced
by disk caches and whether they are cold or warm.

If you want to run the benchmark on a warm cache, you can use the `-w`/`--warmup` option to
perform a certain number of program executions before the actual benchmark:
```sh
hyperfine --warmup 3 'grep -R TODO *'
```

Conversely, if you want to run the benchmark for a cold cache, you can use the `-p`/`--prepare`
option to run a special command before *each* timing run. For example, to clear harddisk caches
on Linux, you can run
```sh
sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
```
To use this specific command with hyperfine, call `sudo -v` to temporarily gain sudo permissions
and then call:
```sh
hyperfine --prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' 'grep -R TODO *'
```

### Parameterized benchmarks

If you want to run a series of benchmarks where a single parameter is varied (say, the number of
threads), you can use the `-P`/`--parameter-scan` option and call:
```sh
hyperfine --prepare 'make clean' --parameter-scan num_threads 1 12 'make -j {num_threads}'
```
This also works with decimal numbers. The `-D`/`--parameter-step-size` option can be used
to control the step size:
```sh
hyperfine --parameter-scan delay 0.3 0.7 -D 0.2 'sleep {delay}'
```
This runs `sleep 0.3`, `sleep 0.5` and `sleep 0.7`.

For non-numeric parameters, you can also supply a list of values with the `-L`/`--parameter-list`
option:
```
hyperfine -L compiler gcc,clang '{compiler} -O2 main.cpp'
```

### Intermediate shell

By default, commands are executed using a predefined shell (`/bin/sh` on Unix, `cmd.exe` on Windows).
If you want to use a different shell, you can use the `-S, --shell <SHELL>` option:
```sh
hyperfine --shell zsh 'for i in {1..10000}; do echo test; done'
```

Note that hyperfine always *corrects for the shell spawning time*. To do this, it performs a calibration
procedure where it runs the shell with an empty command (multiple times), to measure the startup time
of the shell. It will then subtract this time from the total to show the actual time used by the command
in question.

If you want to run a benchmark *without an intermediate shell*, you can use the `-N` or `--shell=none`
option. This is helpful for very fast commands (< 5 ms) where the shell startup overhead correction would
produce a significant amount of noise. Note that you cannot use shell syntax like `*` or `~` in this case.
```
hyperfine -N 'grep TODO /home/user'
```


### Shell functions and aliases

If you are using bash, you can export shell functions to directly benchmark them with hyperfine:

```bash
my_function() { sleep 1; }
export -f my_function
hyperfine --shell=bash my_function
```

Otherwise, inline them into or source them from the benchmarked program:

```sh
hyperfine 'my_function() { sleep 1; }; my_function'

echo 'alias my_alias="sleep 1"' > /tmp/my_alias.sh
hyperfine '. /tmp/my_alias.sh; my_alias'
```

### Exporting results

Hyperfine has multiple options for exporting benchmark results to CSV, JSON, Markdown and other
formats (see `--help` text for details).

#### Markdown

You can use the `--export-markdown <file>` option to create tables like the following:

| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `find . -iregex '.*[0-9]\.jpg$'` | 2.275 ± 0.046 | 2.243 | 2.397 | 9.79 ± 0.22 |
| `find . -iname '*[0-9].jpg'` | 1.427 ± 0.026 | 1.405 | 1.468 | 6.14 ± 0.13 |
| `fd -HI '.*[0-9]\.jpg$'` | 0.232 ± 0.002 | 0.230 | 0.236 | 1.00 |

#### JSON

The JSON output is useful if you want to analyze the benchmark results in more detail. The
[`scripts/`](https://github.com/sharkdp/hyperfine/tree/master/scripts) folder includes a lot
of helpful Python programs to further analyze benchmark results and create helpful
visualizations, like a histogram of runtimes or a whisker plot to compare
multiple benchmarks:

| ![](doc/histogram.png) | ![](doc/whisker.png) |
|---:|---:|


### Detailed benchmark flowchart

The following chart explains the execution order of various timing runs when using options
like `--warmup`, `--prepare <cmd>`, `--setup <cmd>` or `--cleanup <cmd>`:

![](doc/execution-order.png)

## Installation

[![Packaging status](https://repology.org/badge/vertical-allrepos/hyperfine.svg?columns=3&exclude_unsupported=1)](https://repology.org/project/hyperfine/versions)

### On Ubuntu

On Ubuntu, hyperfine can be installed [from the official repositories](https://launchpad.net/ubuntu/+source/rust-hyperfine):
```
apt install hyperfine
```

Alternatively, for the latest version, you can download the appropriate `.deb` package from the [Release page](https://github.com/sharkdp/hyperfine/releases) and install it via `dpkg`:
```
wget https://github.com/sharkdp/hyperfine/releases/download/v1.20.0/hyperfine_1.20.0_amd64.deb
sudo dpkg -i hyperfine_1.20.0_amd64.deb
```

### On Fedora

On Fedora, hyperfine can be installed from the official repositories:

```sh
dnf install hyperfine
```

### On Alpine Linux

On Alpine Linux, hyperfine can be installed [from the official repositories](https://pkgs.alpinelinux.org/packages?name=hyperfine):
```
apk add hyperfine
```

### On Arch Linux

On Arch Linux, hyperfine can be installed [from the official repositories](https://archlinux.org/packages/extra/x86_64/hyperfine/):
```
pacman -S hyperfine
```

### On Debian Linux

On Debian Linux, hyperfine can be installed [from the official repositories](https://packages.debian.org/hyperfine):
```
apt install hyperfine
```

### On Exherbo Linux

On Exherbo Linux, hyperfine can be installed [from the rust repositories](https://gitlab.exherbo.org/exherbo/rust/-/tree/master/packages/sys-apps/hyperfine):
```
cave resolve -x repository/rust
cave resolve -x hyperfine
```

### On Funtoo Linux

On Funtoo Linux, hyperfine can be installed [from core-kit](https://github.com/funtoo/core-kit/tree/1.4-release/app-benchmarks/hyperfine):
```
emerge app-benchmarks/hyperfine
```

### On NixOS

On NixOS, hyperfine can be installed [from the official repositories](https://nixos.org/nixos/packages.html?query=hyperfine):
```
nix-env -i hyperfine
```

### On Flox

On Flox, hyperfine can be installed as follows.
```
flox install hyperfine
```
Hyperfine's version in Flox follows that of Nix.

### On openSUSE

On openSUSE, hyperfine can be installed [from the official repositories](https://software.opensuse.org/package/hyperfine):
```
zypper install hyperfine
```

### On Void Linux

Hyperfine can be installed via xbps

```
xbps-install -S hyperfine
```

### On macOS

Hyperfine can be installed via [Homebrew](https://brew.sh):
```
brew install hyperfine
```

Or you can install using [MacPorts](https://www.macports.org):
```
sudo port selfupdate
sudo port install hyperfine
```

### On FreeBSD

Hyperfine can be installed via pkg:
```
pkg install hyperfine
```

### On OpenBSD

```
doas pkg_add hyperfine
```

### On Windows

Hyperfine can be installed via [Chocolatey](https://community.chocolatey.org/packages/hyperfine), [Scoop](https://scoop.sh/#/apps?q=hyperfine&s=0&d=1&o=true&id=8f7c10f75ecf5f9e42a862c615257328e2f70f61), or [Winget](https://github.com/microsoft/winget-pkgs/tree/master/manifests/s/sharkdp/hyperfine):
```
choco install hyperfine
```
```
scoop install hyperfine
```
```
winget install hyperfine
```

### With conda

Hyperfine can be installed via [`conda`](https://conda.io/en/latest/) from the [`conda-forge`](https://anaconda.org/conda-forge/hyperfine) channel:
```
conda install -c conda-forge hyperfine
```

### With cargo (Linux, macOS, Windows)

Hyperfine can be installed from source via [cargo](https://doc.rust-lang.org/cargo/):
```
cargo install --locked hyperfine
```

Make sure that you use Rust 1.76 or newer.

### From binaries (Linux, macOS, Windows)

Download the corresponding archive from the [Release page](https://github.com/sharkdp/hyperfine/releases).

## Alternative tools

Hyperfine is inspired by [bench](https://github.com/Gabriella439/bench).

## Integration with other tools

[Chronologer](https://github.com/dandavison/chronologer) is a tool that uses `hyperfine` to
visualize changes in benchmark timings across your Git history.

[Bencher](https://github.com/bencherdev/bencher) is a continuous benchmarking tool that supports `hyperfine` to
track benchmarks and catch performance regressions in CI.

Drop hyperfine JSON outputs onto the [Venz](https://try.venz.dev) chart to visualize the results,
and manage hyperfine configurations.

Make sure to check out the [`scripts` folder](https://github.com/sharkdp/hyperfine/tree/master/scripts)
in this repository for a set of tools to work with `hyperfine` benchmark results.

## Origin of the name

The name *hyperfine* was chosen in reference to the hyperfine levels of caesium 133 which play a crucial role in the
[definition of our base unit of time](https://en.wikipedia.org/wiki/Second#History_of_definition)
— the second.

## Citing hyperfine

Thank you for considering to cite hyperfine in your research work. Please see the information
in the sidebar on how to properly cite hyperfine.

## License

`hyperfine` is dual-licensed under the terms of the MIT License and the Apache License 2.0.

See the [LICENSE-APACHE](LICENSE-APACHE) and [LICENSE-MIT](LICENSE-MIT) files for details.
```

## File: `build.rs`
```rust
use std::fs;

use clap_complete::{generate_to, Shell};

include!("src/cli.rs");

fn main() {
    let var = std::env::var_os("SHELL_COMPLETIONS_DIR").or_else(|| std::env::var_os("OUT_DIR"));
    let outdir = match var {
        None => return,
        Some(outdir) => outdir,
    };
    fs::create_dir_all(&outdir).unwrap();

    let mut command = build_command();
    for shell in [
        Shell::Bash,
        Shell::Fish,
        Shell::Zsh,
        Shell::PowerShell,
        Shell::Elvish,
    ] {
        generate_to(shell, &mut command, "hyperfine", &outdir).unwrap();
    }
}
```

## File: `doc/hyperfine.1`
```
.TH HYPERFINE 1
.SH NAME
hyperfine \- command\-line benchmarking tool
.SH SYNOPSIS
.B hyperfine
.RB [ \-ihVN ]
.RB [ \-\-warmup
.IR NUM ]
.RB [ \-\-min\-runs
.IR NUM ]
.RB [ \-\-max\-runs
.IR NUM ]
.RB [ \-\-runs
.IR NUM ]
.RB [ \-\-setup
.IR CMD ]
.RB [ \-\-prepare
.IR CMD ]
.RB [ \-\-conclude
.IR CMD ]
.RB [ \-\-cleanup
.IR CMD ]
.RB [ \-\-parameter\-scan
.IR VAR
.IR MIN
.IR MAX ]
.RB [ \-\-parameter\-step\-size
.IR DELTA ]
.RB [ \-\-parameter\-list
.IR VAR
.IR VALUES ]
.RB [ \-\-shell
.IR SHELL ]
.RB [ \-\-style
.IR TYPE ]
.RB [ \-\-sort
.IR METHOD ]
.RB [ \-\-time-unit
.IR UNIT ]
.RB [ \-\-export\-asciidoc
.IR FILE ]
.RB [ \-\-export\-csv
.IR FILE ]
.RB [ \-\-export\-json
.IR FILE ]
.RB [ \-\-export\-markdown
.IR FILE ]
.RB [ \-\-export\-orgmode
.IR FILE ]
.RB [ \-\-output
.IR WHERE ]
.RB [ \-\-input
.IR WHERE ]
.RB [ \-\-command\-name
.IR NAME ]
.RI [ COMMAND... ]
.SH DESCRIPTION
A command\-line benchmarking tool which includes:
.LP
.RS
* Statistical analysis across multiple runs
.RE
.RS
* Support for arbitrary shell commands
.RE
.RS
* Constant feedback about the benchmark progress and current estimates
.RE
.RS
* Warmup runs can be executed before the actual benchmark
.RE
.RS
* Cache-clearing commands can be set up before each timing run
.RE
.RS
* Statistical outlier detection to detect interference from other programs and caching effects
.RE
.RS
* Export results to various formats: CSV, JSON, Markdown, AsciiDoc
.RE
.RS
* Parameterized benchmarks (e.g. vary the number of threads)
.RE
.SH OPTIONS
.HP
\fB\-w\fR, \fB\-\-warmup\fR \fINUM\fP
.IP
Perform \fINUM\fP warmup runs before the actual benchmark. This can be used
to fill (disk) caches for I/O\-heavy programs.
.HP
\fB\-m\fR, \fB\-\-min\-runs\fR \fINUM\fP
.IP
Perform at least \fINUM\fP runs for each command. Default: 10.
.HP
\fB\-M\fR, \fB\-\-max\-runs\fR \fINUM\fP
.IP
Perform at most \fINUM\fP runs for each command. By default, there is no
limit.
.HP
\fB\-r\fR, \fB\-\-runs\fR \fINUM\fP
.IP
Perform exactly \fINUM\fP runs for each command. If this option is not specified,
\fBhyperfine\fR automatically determines the number of runs.
.HP
\fB\-s\fR, \fB\-\-setup\fR \fICMD...\fP
.IP
Execute \fICMD\fP once before each set of timing runs. This is useful
for compiling your software or with the provided parameters, or to do any
other work that should happen once before a series of benchmark runs,
not every time as would happen with the \fB\-\-prepare\fR option.
.HP
\fB\-p\fR, \fB\-\-prepare\fR \fICMD...\fP
.IP
Execute \fICMD\fP before each timing run. This is useful for clearing disk caches,
for example.
The \fB\-\-prepare\fR option can be specified once for all commands or multiple times,
once for each command. In the latter case, each preparation command will be
run prior to the corresponding benchmark command.
.HP
\fB\-\-conclude\fR \fICMD...\fP
.IP
Execute \fICMD\fP after each timing run. This is useful for clearing disk caches,
for example.
The \fB\-\-conclude\fR option can be specified once for all commands or multiple times,
once for each command. In the latter case, each conclusion command will be
run after the corresponding benchmark command.
.HP
\fB\-c\fR, \fB\-\-cleanup\fR \fICMD...\fP
.IP
Execute \fICMD\fP after the completion of all benchmarking runs for each individual
command to be benchmarked. This is useful if the commands to be benchmarked
produce artifacts that need to be cleaned up. It only runs once a series of
benchmark runs, as opposed to \fB\-\-conclude\fR option which runs after
every run.
.HP
\fB\-P\fR, \fB\-\-parameter\-scan\fR \fIVAR\fP \fIMIN\fP \fIMAX\fP
.IP
Perform benchmark runs for each value in the range \fIMIN..MAX\fP. Replaces the
string '{\fIVAR\fP}' in each command by the current parameter value.
.IP
.RS
Example:
.RS
\fBhyperfine\fR \fB\-P\fR threads 1 8 'make \-j {threads}'
.RE
.RE
.IP
This performs benchmarks for 'make \-j 1', 'make \-j 2', ..., 'make \-j 8'.
.IP
To have the value increase following different patterns, use shell
arithmetics.
.IP
.RS
Example:
.RS
\fBhyperfine\fR \fB\-P\fR size 0 3 'sleep $((2**{size}))'
.RE
.RE
.IP
This performs benchmarks with power of 2 increases: 'sleep 1', 'sleep
2', 'sleep 4', ...
.IP
The exact syntax may vary depending on your shell and OS.
.HP
\fB\-D\fR, \fB\-\-parameter\-step\-size\fR \fIDELTA\fP
.IP
This argument requires \fB\-\-parameter\-scan\fR to be specified as well. Traverse the
range \fIMIN..MAX\fP in steps of \fIDELTA\fP.
.IP
.RS
Example:
.RS
\fBhyperfine\fR \fB\-P\fR delay 0.3 0.7 \fB\-D\fR 0.2 'sleep {delay}'
.RE
.RE
.IP
This performs benchmarks for 'sleep 0.3', 'sleep 0.5' and 'sleep 0.7'.
.HP
\fB\-L\fR, \fB\-\-parameter\-list\fR \fIVAR\fP \fIVALUES\fP
.IP
Perform benchmark runs for each value in the comma\-separated list of \fIVALUES\fP.
Replaces the string '{\fIVAR\fP}' in each command by the current parameter value.
.IP
.RS
Example:
.RS
\fBhyperfine\fR \fB\-L\fR compiler gcc,clang '{compiler} \-O2 main.cpp'
.RE
.RE
.IP
This performs benchmarks for 'gcc \-O2 main.cpp' and 'clang \-O2 main.cpp'.
.IP
The option can be specified multiple times to run benchmarks for all
possible parameter combinations.
.HP
\fB\-S\fR, \fB\-\-shell\fR \fISHELL\fP
.IP
Set the shell to use for executing benchmarked commands. This can be
the name or the path to the shell executable, or a full command line
like "bash \fB\-\-norc\fR". It can also be set to "default" to explicitly
select the default shell on this platform. Finally, this can also be
set to "none" to disable the shell. In this case, commands will be
executed directly. They can still have arguments, but more complex
things like "sleep 0.1; sleep 0.2" are not possible without a shell.
.HP
\fB\-N\fR
.IP
An alias for '\-\-shell=none'.
.HP
\fB\-i\fR, \fB\-\-ignore\-failure\fR
.IP
Ignore non\-zero exit codes of the benchmarked programs.
.HP
\fB\-\-style\fR \fITYPE\fP
.IP
Set output style \fITYPE\fP (default: auto). Set this to 'basic' to disable output
coloring and interactive elements. Set it to 'full' to enable all effects even
if no interactive terminal was detected. Set this to 'nocolor' to keep the
interactive output without any colors. Set this to 'color' to keep the colors
without any interactive output. Set this to 'none' to disable all the output
of the tool.
.HP
\fB\-\-sort\fR \fIMETHOD\fP
.IP
Specify the sort order of the speed comparison summary and the
exported tables for markup formats (Markdown, AsciiDoc, org\-mode):
.RS
.IP "auto (default)"
the speed comparison will be ordered by time and
the markup tables will be ordered by command (input order).
.IP "command"
order benchmarks in the way they were specified
.IP "mean\-time"
order benchmarks by mean runtime
.RE
.HP
\fB\-u\fR, \fB\-\-time\-unit\fR \fIUNIT\fP
.IP
Set the time unit to be used. Possible values: microsecond, millisecond, second. If
the option is not given, the time unit is determined automatically.
This option affects the standard output as well as all export formats
except for CSV and JSON.
.HP
\fB\-\-export\-asciidoc\fR \fIFILE\fP 
.IP
Export the timing summary statistics as an AsciiDoc table to the given \fIFILE\fP.
The output time unit can be changed using the \fB\-\-time\-unit\fR option.
.HP
\fB\-\-export\-csv\fR \fIFILE\fP
.IP
Export the timing summary statistics as CSV to the given \fIFILE\fP. If you need the
timing results for each individual run, use the JSON export format.
The output time unit is always seconds.
.HP
\fB\-\-export\-json\fR \fIFILE\fP
.IP
Export the timing summary statistics and timings of individual runs as JSON to
the given \fIFILE\fP. The output time unit is always seconds.
.HP
\fB\-\-export\-markdown\fR \fIFILE\fP
.IP
Export the timing summary statistics as a Markdown table to the given \fIFILE\fP.
The output time unit can be changed using the \fB\-\-time\-unit\fR option.
.HP
\fB\-\-export\-orgmode\fR \fIFILE\fP
.IP
Export the timing summary statistics as an Emacs org\-mode table to the
given \fIFILE\fP. The output time unit can be changed using the \fB\-\-time\-unit\fR option.
.HP
\fB\-\-show\-output\fR
.IP
Print the stdout and stderr of the benchmark instead of suppressing it. This
will increase the time it takes for benchmarks to run, so it should only be
used for debugging purposes or when trying to benchmark output speed.
.HP
\fB\-\-output\fR \fIWHERE\fP
.IP
Control where the output of the benchmark is redirected. Note that
some programs like 'grep' detect when standard output is \fI\,/dev/null\/\fP and
apply certain optimizations. To avoid that, consider using
\-\-output=pipe.
.IP
\fIWHERE\fP can be:
.RS
.IP null
Redirect output to \fI\,/dev/null\/\fP (the default).
.IP pipe
Feed the output through a pipe before discarding it.
.IP inherit
Don't redirect the output at all (same as \&'\-\-show\-output').
.IP "<FILE>"
Write the output to the given file.
.RE
.IP
This option can be specified once for all commands or multiple times,
once for each command. Note: If you want to log the output of each and
every iteration, you can use a shell redirection and the $HYPERFINE_ITERATION
environment variable: 'my-command > output-${HYPERFINE_ITERATION}.log'
.HP
\fB\-\-input\fR \fIWHERE\fP
.IP
Control where the input of the benchmark comes from.
.IP
\fIWHERE\fP can be:
.RS
.IP null
Read from \fI\,/dev/null\/\fP (the default).
.IP "<FILE>"
Read the input from the given file.
.RE
.HP
\fB\-n\fR, \fB\-\-command\-name\fR \fiNAME\fP
.IP
Give a meaningful \fiNAME\fP to a command. This can be specified multiple times
if several commands are benchmarked.
.HP
\fB\-h\fR, \fB\-\-help\fR
.IP
Print help
.HP
\fB\-V\fR, \fB\-\-version\fR
.IP
Print version
.SH EXAMPLES
.LP
Basic benchmark of 'find . -name todo.txt':
.RS
.nf
\fBhyperfine\fR 'find . -name todo.txt'
.fi
.RE
.LP
Perform benchmarks for 'sleep 0.2' and 'sleep 3.2' with a minimum 5 runs each:
.RS
.nf
\fBhyperfine\fR \fB\-\-min\-runs\fR 5 'sleep 0.2' 'sleep 3.2'
.fi
.RE
.LP
Perform a benchmark of 'grep' with a warm disk cache by executing 3 runs up front that are not part
of the measurement: 
.RS
.nf
\fBhyperfine\fR \fB\-\-warmup\fR 3 'grep -R TODO *'
.fi
.RE
.LP
Export the results of a parameter scan benchmark to a markdown table: 
.RS
.nf
\fBhyperfine\fR \fB\-\-export\-markdown\fR output.md \fB\-\-parameter-scan\fR time 1 5 'sleep {time}'
.fi
.RE
.LP
Demonstrate when each of \fB\-\-setup\fR, \fB\-\-prepare\fR, \fB\-\-conclude\fR, \fIcmd\fP and \fB\-\-cleanup\fR will run:
.RS
.nf
\fBhyperfine\fR \fB\-L\fR n 1,2 \fB\-r\fR 2 \fB\-\-show-output\fR \\
	\fB\-\-setup\fR 'echo setup n={n}' \\
	\fB\-\-prepare\fR 'echo prepare={n}' \\
	\fB\-\-conclude\fR 'echo conclude={n}' \\
	\fB\-\-cleanup\fR 'echo cleanup n={n}' \\
	'echo command n={n}'
.fi
.RE
.RE
.SH AUTHOR
.LP
David Peter <mail@david-peter.de>
.LP
Source, bug tracker, and additional information can be found on GitHub:
.I https://github.com/sharkdp/hyperfine
```

## File: `doc/sponsors.md`
```markdown
## Sponsors

`hyperfine` development is sponsored by many individuals and companies. Thank you very much!

Please note, that being sponsored does not affect the individuality of the `hyperfine`
project or affect the maintainers' actions in any way.
We remain impartial and continue to assess pull requests solely on merit - the
features added, bugs solved, and effect on the overall complexity of the code.
No issue will have a different priority based on sponsorship status of the
reporter.

Contributions from anybody are most welcomed.

If you want to see our biggest sponsors, check the top of [`README.md`](../../../README.md#sponsors).
```

## File: `scripts/README.md`
```markdown
This folder contains scripts that can be used in combination with hyperfines `--export-json` option.

### Example:

```bash
hyperfine 'sleep 0.020' 'sleep 0.021' 'sleep 0.022' --export-json sleep.json
./plot_whisker.py sleep.json
```

### Pre-requisites

To make these scripts work, you will need `numpy`, `matplotlib` and `scipy`.

If you have a Python package manager that understands [PEP-723](https://peps.python.org/pep-0723/)
inline script requirements like [`uv`](https://github.com/astral-sh/uv) or [`pipx`](https://github.com/pypa/pipx),
you can directly run the scripts using

```bash
uv run plot_whisker.py sleep.json
```

Otherwise, install the dependencies via your system package manager or using `pip`:

```bash
pip install numpy matplotlib scipy  # pip3, if you are using python3
```
```

## File: `scripts/advanced_statistics.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
# ]
# ///

import argparse
import json
from enum import Enum

import numpy as np


class Unit(Enum):
    SECOND = 1
    MILLISECOND = 2

    def factor(self):
        match self:
            case Unit.SECOND:
                return 1
            case Unit.MILLISECOND:
                return 1e3

    def __str__(self):
        match self:
            case Unit.SECOND:
                return "s"
            case Unit.MILLISECOND:
                return "ms"


parser = argparse.ArgumentParser()
parser.add_argument("file", help="JSON file with benchmark results")
parser.add_argument(
    "--time-unit",
    help="The unit of time.",
    default="second",
    action="store",
    choices=["second", "millisecond"],
    dest="unit",
)
args = parser.parse_args()

unit = Unit.MILLISECOND if args.unit == "millisecond" else Unit.SECOND
unit_str = str(unit)

with open(args.file) as f:
    results = json.load(f)["results"]

commands = [b["command"] for b in results]
times = [b["times"] for b in results]

for command, ts in zip(commands, times):
    ts = [t * unit.factor() for t in ts]

    p05 = np.percentile(ts, 5)
    p25 = np.percentile(ts, 25)
    p75 = np.percentile(ts, 75)
    p95 = np.percentile(ts, 95)

    iqr = p75 - p25

    print(f"Command '{command}'")
    print(f"  runs:   {len(ts):8d}")
    print(f"  mean:   {np.mean(ts):8.3f} {unit_str}")
    print(f"  stddev: {np.std(ts, ddof=1):8.3f} {unit_str}")
    print(f"  median: {np.median(ts):8.3f} {unit_str}")
    print(f"  min:    {np.min(ts):8.3f} {unit_str}")
    print(f"  max:    {np.max(ts):8.3f} {unit_str}")
    print()
    print("  percentiles:")
    print(f"     P_05 .. P_95:    {p05:.3f} {unit_str} .. {p95:.3f} {unit_str}")
    print(
        f"     P_25 .. P_75:    {p25:.3f} {unit_str} .. {p75:.3f} {unit_str}  (IQR = {iqr:.3f} {unit_str})"
    )
    print()
```

## File: `scripts/plot_benchmark_comparison.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
#     "pyqt6",
#     "numpy",
# ]
# ///

"""
This script shows `hyperfine` benchmark results as a bar plot grouped by command.
Note all the input files must contain results for all commands.
"""

import argparse
import json
import pathlib

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "files", nargs="+", type=pathlib.Path, help="JSON files with benchmark results"
)
parser.add_argument("--title", help="Plot Title")
parser.add_argument(
    "--benchmark-names", nargs="+", help="Names of the benchmark groups"
)
parser.add_argument("-o", "--output", help="Save image to the given filename")

args = parser.parse_args()

commands = None
data = []
inputs = []

if args.benchmark_names:
    assert len(args.files) == len(
        args.benchmark_names
    ), "Number of benchmark names must match the number of input files."

for i, filename in enumerate(args.files):
    with open(filename) as f:
        results = json.load(f)["results"]
    benchmark_commands = [b["command"] for b in results]
    if commands is None:
        commands = benchmark_commands
    else:
        assert (
            commands == benchmark_commands
        ), f"Unexpected commands in {filename}: {benchmark_commands}, expected: {commands}"
    data.append([round(b["mean"], 2) for b in results])
    if args.benchmark_names:
        inputs.append(args.benchmark_names[i])
    else:
        inputs.append(filename.stem)

data = np.transpose(data)
x = np.arange(len(inputs))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(layout="constrained")
fig.set_figheight(5)
fig.set_figwidth(10)
for i, command in enumerate(commands):
    offset = width * (i + 1)
    rects = ax.bar(x + offset, data[i], width, label=command)

ax.set_xticks(x + 0.5, inputs)
ax.grid(visible=True, axis="y")

if args.title:
    plt.title(args.title)
plt.xlabel("Benchmark")
plt.ylabel("Time [s]")
plt.legend(title="Command")

if args.output:
    plt.savefig(args.output)
else:
    plt.show()
```

## File: `scripts/plot_histogram.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
#     "pyqt6",
#     "numpy",
# ]
# ///

"""This program shows `hyperfine` benchmark results as a histogram."""

import argparse
import json

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results")
parser.add_argument("--title", help="Plot title")
parser.add_argument(
    "--labels", help="Comma-separated list of entries for the plot legend"
)
parser.add_argument("--bins", help="Number of bins (default: auto)")
parser.add_argument(
    "--legend-location",
    help="Location of the legend on plot (default: upper center)",
    choices=[
        "upper center",
        "lower center",
        "right",
        "left",
        "best",
        "upper left",
        "upper right",
        "lower left",
        "lower right",
        "center left",
        "center right",
        "center",
    ],
    default="upper center",
)
parser.add_argument(
    "--type", help="Type of histogram (*bar*, barstacked, step, stepfilled)"
)
parser.add_argument("-o", "--output", help="Save image to the given filename.")
parser.add_argument(
    "--t-min", metavar="T", help="Minimum time to be displayed (seconds)"
)
parser.add_argument(
    "--t-max", metavar="T", help="Maximum time to be displayed (seconds)"
)
parser.add_argument(
    "--log-count",
    help="Use a logarithmic y-axis for the event count",
    action="store_true",
)

args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

if args.labels:
    labels = args.labels.split(",")
else:
    labels = [b["command"] for b in results]
all_times = [b["times"] for b in results]

t_min = float(args.t_min) if args.t_min else np.min(list(map(np.min, all_times)))
t_max = float(args.t_max) if args.t_max else np.max(list(map(np.max, all_times)))

bins = int(args.bins) if args.bins else "auto"
histtype = args.type if args.type else "bar"

plt.figure(figsize=(10, 5))
plt.hist(
    all_times,
    label=labels,
    bins=bins,
    histtype=histtype,
    range=(t_min, t_max),
)
plt.legend(
    loc=args.legend_location,
    fancybox=True,
    shadow=True,
    prop={"size": 10, "family": ["Source Code Pro", "Fira Mono", "Courier New"]},
)

plt.xlabel("Time [s]")
if args.title:
    plt.title(args.title)

if args.log_count:
    plt.yscale("log")
else:
    plt.ylim(0, None)

if args.output:
    plt.savefig(args.output, dpi=600)
else:
    plt.show()
```

## File: `scripts/plot_parametrized.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
#     "pyqt6",
# ]
# ///

"""This program shows parametrized `hyperfine` benchmark results as an
errorbar plot."""

import argparse
import json
import sys

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results", nargs="+")
parser.add_argument(
    "--parameter-name",
    metavar="name",
    type=str,
    help="Deprecated; parameter names are now inferred from benchmark files",
)
parser.add_argument(
    "--log-x", help="Use a logarithmic x (parameter) axis", action="store_true"
)
parser.add_argument(
    "--log-time", help="Use a logarithmic time axis", action="store_true"
)
parser.add_argument(
    "--titles", help="Comma-separated list of titles for the plot legend"
)
parser.add_argument("-o", "--output", help="Save image to the given filename.")

args = parser.parse_args()
if args.parameter_name is not None:
    sys.stderr.write(
        "warning: --parameter-name is deprecated; names are inferred from "
        "benchmark results\n"
    )


def die(msg):
    sys.stderr.write(f"fatal: {msg}\n")
    sys.exit(1)


def extract_parameters(results):
    """Return `(parameter_name: str, parameter_values: List[float])`."""
    if not results:
        die("no benchmark data to plot")
    (names, values) = zip(*(unique_parameter(b) for b in results))
    names = frozenset(names)
    if len(names) != 1:
        die(
            f"benchmarks must all have the same parameter name, but found: {sorted(names)}"
        )
    return (next(iter(names)), list(values))


def unique_parameter(benchmark):
    """Return the unique parameter `(name: str, value: float)`, or die."""
    params_dict = benchmark.get("parameters", {})
    if not params_dict:
        die("benchmarks must have exactly one parameter, but found none")
    if len(params_dict) > 1:
        die(
            f"benchmarks must have exactly one parameter, but found multiple: {sorted(params_dict)}"
        )
    [(name, value)] = params_dict.items()
    return (name, float(value))


parameter_name = None

for filename in args.file:
    with open(filename) as f:
        results = json.load(f)["results"]

    (this_parameter_name, parameter_values) = extract_parameters(results)
    if parameter_name is not None and this_parameter_name != parameter_name:
        die(
            f"files must all have the same parameter name, but found {parameter_name!r} vs. {this_parameter_name!r}"
        )
    parameter_name = this_parameter_name

    times_mean = [b["mean"] for b in results]
    times_stddev = [b["stddev"] for b in results]

    plt.errorbar(x=parameter_values, y=times_mean, yerr=times_stddev, capsize=2)

plt.xlabel(parameter_name)
plt.ylabel("Time [s]")

if args.log_time:
    plt.yscale("log")
else:
    plt.ylim(0, None)

if args.log_x:
    plt.xscale("log")

if args.titles:
    plt.legend(args.titles.split(","))

if args.output:
    plt.savefig(args.output)
else:
    plt.show()
```

## File: `scripts/plot_progression.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyqt6",
#     "matplotlib",
#     "numpy",
# ]
# ///

"""This program shows `hyperfine` benchmark results in a sequential way
in order to debug possible background interference, caching effects,
thermal throttling and similar effects.
"""

import argparse
import json

import matplotlib.pyplot as plt
import numpy as np


def moving_average(times, num_runs):
    times_padded = np.pad(
        times, (num_runs // 2, num_runs - 1 - num_runs // 2), mode="edge"
    )
    kernel = np.ones(num_runs) / num_runs
    return np.convolve(times_padded, kernel, mode="valid")


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results")
parser.add_argument("--title", help="Plot Title")
parser.add_argument("-o", "--output", help="Save image to the given filename.")
parser.add_argument(
    "-w",
    "--moving-average-width",
    type=int,
    metavar="num_runs",
    help="Width of the moving-average window (default: N/5)",
)
parser.add_argument(
    "--no-moving-average",
    action="store_true",
    help="Do not show moving average curve",
)


args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

for result in results:
    label = result["command"]
    times = result["times"]
    num = len(times)
    nums = range(num)

    plt.scatter(x=nums, y=times, marker=".")
    plt.ylim([0, None])
    plt.xlim([-1, num])

    if not args.no_moving_average:
        moving_average_width = (
            num // 5 if args.moving_average_width is None else args.moving_average_width
        )

        average = moving_average(times, moving_average_width)
        plt.plot(nums, average, "-")

if args.title:
    plt.title(args.title)

legend = []
for result in results:
    legend.append(result["command"])
    if not args.no_moving_average:
        legend.append("moving average")
plt.legend(legend)

plt.ylabel("Time [s]")

if args.output:
    plt.savefig(args.output)
else:
    plt.show()
```

## File: `scripts/plot_whisker.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
#     "pyqt6",
# ]
# ///

"""This program shows `hyperfine` benchmark results as a box and whisker plot.

Quoting from the matplotlib documentation:
    The box extends from the lower to upper quartile values of the data, with
    a line at the median. The whiskers extend from the box to show the range
    of the data. Flier points are those past the end of the whiskers.
"""

import argparse
import json

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results")
parser.add_argument("--title", help="Plot Title")
parser.add_argument("--sort-by", choices=["median"], help="Sort method")
parser.add_argument(
    "--labels", help="Comma-separated list of entries for the plot legend"
)
parser.add_argument("-o", "--output", help="Save image to the given filename.")

args = parser.parse_args()

with open(args.file, encoding="utf-8") as f:
    results = json.load(f)["results"]

if args.labels:
    labels = args.labels.split(",")
else:
    labels = [b["command"] for b in results]
times = [b["times"] for b in results]

if args.sort_by == "median":
    medians = [b["median"] for b in results]
    indices = sorted(range(len(labels)), key=lambda k: medians[k])
    labels = [labels[i] for i in indices]
    times = [times[i] for i in indices]

plt.figure(figsize=(10, 6), constrained_layout=True)
boxplot = plt.boxplot(times, vert=True, patch_artist=True)
cmap = plt.get_cmap("rainbow")
colors = [cmap(val / len(times)) for val in range(len(times))]

for patch, color in zip(boxplot["boxes"], colors):
    patch.set_facecolor(color)

if args.title:
    plt.title(args.title)
plt.legend(handles=boxplot["boxes"], labels=labels, loc="best", fontsize="medium")
plt.ylabel("Time [s]")
plt.ylim(0, None)
plt.xticks(list(range(1, len(labels) + 1)), labels, rotation=45)
if args.output:
    plt.savefig(args.output)
else:
    plt.show()
```

## File: `scripts/ruff.toml`
```
target-version = "py310"

[lint]
extend-select = ["I", "UP", "RUF"]
```

## File: `scripts/welch_ttest.py`
```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "scipy",
# ]
# ///

"""This script performs Welch's t-test on a JSON export file with two
benchmark results to test whether or not the two distributions are
the same."""

import argparse
import json
import sys

from scipy import stats

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with two benchmark results")
args = parser.parse_args()

with open(args.file) as f:
    results = json.load(f)["results"]

if len(results) != 2:
    print("The input file has to contain exactly two benchmarks")
    sys.exit(1)

a, b = (x["command"] for x in results[:2])
X, Y = (x["times"] for x in results[:2])

print(f"Command 1: {a}")
print(f"Command 2: {b}\n")

t, p = stats.ttest_ind(X, Y, equal_var=False)
th = 0.05
dispose = p < th
print(f"t = {t:.3}, p = {p:.3}")
print()

if dispose:
    print(f"There is a difference between the two benchmarks (p < {th}).")
else:
    print(f"The two benchmarks are almost the same (p >= {th}).")
```

## File: `src/cli.rs`
```rust
use std::ffi::OsString;

use clap::{
    builder::NonEmptyStringValueParser, crate_version, Arg, ArgAction, ArgMatches, Command,
    ValueHint,
};

pub fn get_cli_arguments<'a, I, T>(args: I) -> ArgMatches
where
    I: IntoIterator<Item = T>,
    T: Into<OsString> + Clone + 'a,
{
    let command = build_command();
    command.get_matches_from(args)
}

/// Build the clap command for parsing command line arguments
fn build_command() -> Command {
    Command::new("hyperfine")
        .version(crate_version!())
        .next_line_help(true)
        .hide_possible_values(true)
        .about("A command-line benchmarking tool.")
        .help_expected(true)
        .max_term_width(80)
        .arg(
            Arg::new("command")
                .help("The command to benchmark. This can be the name of an executable, a command \
                       line like \"grep -i todo\" or a shell command like \"sleep 0.5 && echo test\". \
                       The latter is only available if the shell is not explicitly disabled via \
                       '--shell=none'. If multiple commands are given, hyperfine will show a \
                       comparison of the respective runtimes.")
                .required(true)
                .action(ArgAction::Append)
                .value_hint(ValueHint::CommandString)
                .value_parser(NonEmptyStringValueParser::new()),
        )
        .arg(
            Arg::new("warmup")
                .long("warmup")
                .short('w')
                .value_name("NUM")
                .action(ArgAction::Set)
                .help(
                    "Perform NUM warmup runs before the actual benchmark. This can be used \
                     to fill (disk) caches for I/O-heavy programs.",
                ),
        )
        .arg(
            Arg::new("min-runs")
                .long("min-runs")
                .short('m')
                .action(ArgAction::Set)
                .value_name("NUM")
                .help("Perform at least NUM runs for each command (default: 10)."),
        )
        .arg(
            Arg::new("max-runs")
                .long("max-runs")
                .short('M')
                .action(ArgAction::Set)
                .value_name("NUM")
                .help("Perform at most NUM runs for each command. By default, there is no limit."),
        )
        .arg(
            Arg::new("runs")
                .long("runs")
                .conflicts_with_all(["max-runs", "min-runs"])
                .short('r')
                .action(ArgAction::Set)
                .value_name("NUM")
                .help("Perform exactly NUM runs for each command. If this option is not specified, \
                       hyperfine automatically determines the number of runs."),
        )
        .arg(
            Arg::new("setup")
                .long("setup")
                .short('s')
                .action(ArgAction::Set)
                .value_name("CMD")
                .value_hint(ValueHint::CommandString)
                .help(
                    "Execute CMD before each set of timing runs. This is useful for \
                     compiling your software with the provided parameters, or to do any \
                     other work that should happen once before a series of benchmark runs, \
                     not every time as would happen with the --prepare option."
                ),
        )
        .arg(
            Arg::new("reference")
                .long("reference")
                .action(ArgAction::Set)
                .value_name("CMD")
                .help(
                    "The reference command for the relative comparison of results. \
                    If this is unset, results are compared with the fastest command as reference."
                )
        )
        .arg(
            Arg::new("reference-name")
                .long("reference-name")
                .action(ArgAction::Set)
                .value_name("CMD")
                .help("Give a meaningful name to the reference command.")
                .requires("reference")
        )
        .arg(
            Arg::new("prepare")
                .long("prepare")
                .short('p')
                .action(ArgAction::Append)
                .num_args(1)
                .value_name("CMD")
                .value_hint(ValueHint::CommandString)
                .help(
                    "Execute CMD before each timing run. This is useful for \
                     clearing disk caches, for example.\nThe --prepare option can \
                     be specified once for all commands or multiple times, once for \
                     each command. In the latter case, each preparation command will \
                     be run prior to the corresponding benchmark command.",
                ),
        )
        .arg(
            Arg::new("conclude")
                .long("conclude")
                .short('C')
                .action(ArgAction::Append)
                .num_args(1)
                .value_name("CMD")
                .value_hint(ValueHint::CommandString)
                .help(
                    "Execute CMD after each timing run. This is useful for killing \
                     long-running processes started (e.g. a web server started in --prepare), \
                     for example.\nThe --conclude option can be specified once for all \
                     commands or multiple times, once for each command. In the latter case, \
                     each conclude command will be run after the corresponding benchmark \
                     command.",
                ),
        )
        .arg(
            Arg::new("cleanup")
                .long("cleanup")
                .short('c')
                .action(ArgAction::Set)
                .value_name("CMD")
                .value_hint(ValueHint::CommandString)
                .help(
                    "Execute CMD after the completion of all benchmarking \
                     runs for each individual command to be benchmarked. \
                     This is useful if the commands to be benchmarked produce \
                     artifacts that need to be cleaned up."
                ),
        )
        .arg(
            Arg::new("parameter-scan")
                .long("parameter-scan")
                .short('P')
                .action(ArgAction::Set)
                .allow_hyphen_values(true)
                .value_names(["VAR", "MIN", "MAX"])
                .help(
                    "Perform benchmark runs for each value in the range MIN..MAX. Replaces the \
                     string '{VAR}' in each command by the current parameter value.\n\n  \
                     Example:  hyperfine -P threads 1 8 'make -j {threads}'\n\n\
                     This performs benchmarks for 'make -j 1', 'make -j 2', …, 'make -j 8'.\n\n\
                     To have the value increase following different patterns, use shell arithmetics.\n\n  \
                     Example: hyperfine -P size 0 3 'sleep $((2**{size}))'\n\n\
                     This performs benchmarks with power of 2 increases: 'sleep 1', 'sleep 2', 'sleep 4', …\n\
                     The exact syntax may vary depending on your shell and OS."
                ),
        )
        .arg(
            Arg::new("parameter-step-size")
                .long("parameter-step-size")
                .short('D')
                .action(ArgAction::Set)
                .value_names(["DELTA"])
                .requires("parameter-scan")
                .help(
                    "This argument requires --parameter-scan to be specified as well. \
                     Traverse the range MIN..MAX in steps of DELTA.\n\n  \
                     Example:  hyperfine -P delay 0.3 0.7 -D 0.2 'sleep {delay}'\n\n\
                     This performs benchmarks for 'sleep 0.3', 'sleep 0.5' and 'sleep 0.7'.",
                ),
        )
        .arg(
            Arg::new("parameter-list")
                .long("parameter-list")
                .short('L')
                .action(ArgAction::Append)
                .allow_hyphen_values(true)
                .value_names(["VAR", "VALUES"])
                .conflicts_with_all(["parameter-scan", "parameter-step-size"])
                .help(
                    "Perform benchmark runs for each value in the comma-separated list VALUES. \
                     Replaces the string '{VAR}' in each command by the current parameter value\
                     .\n\nExample:  hyperfine -L compiler gcc,clang '{compiler} -O2 main.cpp'\n\n\
                     This performs benchmarks for 'gcc -O2 main.cpp' and 'clang -O2 main.cpp'.\n\n\
                     The option can be specified multiple times to run benchmarks for all \
                     possible parameter combinations.\n"
                ),
        )
        .arg(
            Arg::new("shell")
                .long("shell")
                .short('S')
                .action(ArgAction::Set)
                .value_name("SHELL")
                .overrides_with("shell")
                .value_hint(ValueHint::CommandString)
                .help("Set the shell to use for executing benchmarked commands. This can be the \
                       name or the path to the shell executable, or a full command line \
                       like \"bash --norc\". It can also be set to \"default\" to explicitly select \
                       the default shell on this platform. Finally, this can also be set to \
                       \"none\" to disable the shell. In this case, commands will be executed \
                       directly. They can still have arguments, but more complex things like \
                       \"sleep 0.1; sleep 0.2\" are not possible without a shell.")
        )
        .arg(
            Arg::new("no-shell")
                .short('N')
                .action(ArgAction::SetTrue)
                .conflicts_with_all(["shell", "debug-mode"])
                .help("An alias for '--shell=none'.")
        )
        .arg(
            Arg::new("ignore-failure")
                .long("ignore-failure")
                .action(ArgAction::Set)
                .value_name("MODE")
                .num_args(0..=1)
                .default_missing_value("all-non-zero")
                .require_equals(true)
                .short('i')
                .help("Ignore failures of the benchmarked programs. Without a value or with \
                       'all-non-zero', all non-zero exit codes are ignored. You can also provide \
                       a comma-separated list of exit codes to ignore (e.g., --ignore-failure=1,2)."),
        )
        .arg(
            Arg::new("style")
                .long("style")
                .action(ArgAction::Set)
                .value_name("TYPE")
                .value_parser(["auto", "basic", "full", "nocolor", "color", "none"])
                .help(
                    "Set output style type (default: auto). Set this to 'basic' to disable output \
                     coloring and interactive elements. Set it to 'full' to enable all effects \
                     even if no interactive terminal was detected. Set this to 'nocolor' to \
                     keep the interactive output without any colors. Set this to 'color' to keep \
                     the colors without any interactive output. Set this to 'none' to disable all \
                     the output of the tool.",
                ),
        )
        .arg(
            Arg::new("sort")
            .long("sort")
            .action(ArgAction::Set)
            .value_name("METHOD")
            .value_parser(["auto", "command", "mean-time"])
            .default_value("auto")
            .hide_default_value(true)
            .help(
                "Specify the sort order of the speed comparison summary and the exported tables for \
                 markup formats (Markdown, AsciiDoc, org-mode):\n  \
                   * 'auto' (default): the speed comparison will be ordered by time and\n    \
                     the markup tables will be ordered by command (input order).\n  \
                   * 'command': order benchmarks in the way they were specified\n  \
                   * 'mean-time': order benchmarks by mean runtime\n"
            ),
        )
        .arg(
            Arg::new("time-unit")
                .long("time-unit")
                .short('u')
                .action(ArgAction::Set)
                .value_name("UNIT")
                .value_parser(["microsecond", "millisecond", "second"])
                .help("Set the time unit to be used. Possible values: microsecond, millisecond, second. \
                       If the option is not given, the time unit is determined automatically. \
                       This option affects the standard output as well as all export formats except for CSV and JSON."),
        )
        .arg(
            Arg::new("export-asciidoc")
                .long("export-asciidoc")
                .action(ArgAction::Set)
                .value_name("FILE")
                .value_hint(ValueHint::FilePath)
                .help("Export the timing summary statistics as an AsciiDoc table to the given FILE. \
                       The output time unit can be changed using the --time-unit option."),
        )
        .arg(
            Arg::new("export-csv")
                .long("export-csv")
                .action(ArgAction::Set)
                .value_name("FILE")
                .value_hint(ValueHint::FilePath)
                .help("Export the timing summary statistics as CSV to the given FILE. If you need \
                       the timing results for each individual run, use the JSON export format. \
                       The output time unit is always seconds."),
        )
        .arg(
            Arg::new("export-json")
                .long("export-json")
                .action(ArgAction::Set)
                .value_name("FILE")
                .value_hint(ValueHint::FilePath)
                .help("Export the timing summary statistics and timings of individual runs as JSON to the given FILE. \
                       The output time unit is always seconds"),
        )
        .arg(
            Arg::new("export-markdown")
                .long("export-markdown")
                .action(ArgAction::Set)
                .value_name("FILE")
                .value_hint(ValueHint::FilePath)
                .help("Export the timing summary statistics as a Markdown table to the given FILE. \
                       The output time unit can be changed using the --time-unit option."),
        )
        .arg(
            Arg::new("export-orgmode")
                .long("export-orgmode")
                .action(ArgAction::Set)
                .value_name("FILE")
                .value_hint(ValueHint::FilePath)
                .help("Export the timing summary statistics as an Emacs org-mode table to the given FILE. \
                       The output time unit can be changed using the --time-unit option."),
        )
        .arg(
            Arg::new("show-output")
                .long("show-output")
                .action(ArgAction::SetTrue)
                .conflicts_with("style")
                .help(
                    "Print the stdout and stderr of the benchmark instead of suppressing it. \
                     This will increase the time it takes for benchmarks to run, \
                     so it should only be used for debugging purposes or \
                     when trying to benchmark output speed.",
                ),
        )
        .arg(
            Arg::new("output")
                .long("output")
                .conflicts_with("show-output")
                .action(ArgAction::Append)
                .value_name("WHERE")
                .help(
                    "Control where the output of the benchmark is redirected. Note \
                     that some programs like 'grep' detect when standard output is \
                     /dev/null and apply certain optimizations. To avoid that, consider \
                     using '--output=pipe'.\n\
                     \n\
                     <WHERE> can be:\n\
                     \n  \
                       null:     Redirect output to /dev/null (the default).\n\
                     \n  \
                       pipe:     Feed the output through a pipe before discarding it.\n\
                     \n  \
                       inherit:  Don't redirect the output at all (same as '--show-output').\n\
                     \n  \
                       <FILE>:   Write the output to the given file.\n\n\
                    This option can be specified once for all commands or multiple times, once for \
                    each command. Note: If you want to log the output of each and every iteration, \
                    you can use a shell redirection and the '$HYPERFINE_ITERATION' environment variable:\n    \
                    hyperfine 'my-command > output-${HYPERFINE_ITERATION}.log'\n\n",
                ),
        )
        .arg(
            Arg::new("input")
                .long("input")
                .action(ArgAction::Set)
                .num_args(1)
                .value_name("WHERE")
                .help("Control where the input of the benchmark comes from.\n\
                       \n\
                       <WHERE> can be:\n\
                       \n  \
                         null:     Read from /dev/null (the default).\n\
                       \n  \
                         <FILE>:   Read the input from the given file."),
        )
        .arg(
            Arg::new("command-name")
                .long("command-name")
                .short('n')
                .action(ArgAction::Append)
                .num_args(1)
                .value_name("NAME")
                .help("Give a meaningful name to a command. This can be specified multiple times \
                       if several commands are benchmarked."),
        )
        // This option is hidden for now, as it is not yet clear yet if we want to 'stabilize' this,
        // see discussion in https://github.com/sharkdp/hyperfine/issues/527
        .arg(
            Arg::new("min-benchmarking-time")
            .long("min-benchmarking-time")
            .action(ArgAction::Set)
            .hide(true)
            .help("Set the minimum time (in seconds) to run benchmarks. Note that the number of \
                   benchmark runs is additionally influenced by the `--min-runs`, `--max-runs`, and \
                   `--runs` option.")
        )
        .arg(
            Arg::new("debug-mode")
            .long("debug-mode")
            .action(ArgAction::SetTrue)
            .hide(true)
            .help("Enable debug mode which does not actually run commands, but returns fake times when the command is 'sleep <time>'.")
        )
}

#[test]
fn verify_app() {
    build_command().debug_assert();
}
```

## File: `src/command.rs`
```rust
use std::collections::BTreeMap;
use std::fmt;
use std::str::FromStr;

use crate::parameter::tokenize::tokenize;
use crate::parameter::ParameterValue;
use crate::{
    error::{OptionsError, ParameterScanError},
    parameter::{
        range_step::{Numeric, RangeStep},
        ParameterNameAndValue,
    },
};

use clap::{parser::ValuesRef, ArgMatches};

use anyhow::{bail, Context, Result};
use rust_decimal::Decimal;

/// A command that should be benchmarked.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Command<'a> {
    /// The command name (without parameter substitution)
    name: Option<&'a str>,

    /// The command that should be executed (without parameter substitution)
    expression: &'a str,

    /// Zero or more parameter values.
    parameters: Vec<ParameterNameAndValue<'a>>,
}

impl<'a> Command<'a> {
    pub fn new(name: Option<&'a str>, expression: &'a str) -> Command<'a> {
        Command {
            name,
            expression,
            parameters: Vec::new(),
        }
    }

    pub fn new_parametrized(
        name: Option<&'a str>,
        expression: &'a str,
        parameters: impl IntoIterator<Item = ParameterNameAndValue<'a>>,
    ) -> Command<'a> {
        Command {
            name,
            expression,
            parameters: parameters.into_iter().collect(),
        }
    }

    pub fn get_name(&self) -> String {
        self.name.map_or_else(
            || self.get_command_line(),
            |name| self.replace_parameters_in(name),
        )
    }

    pub fn get_name_with_unused_parameters(&self) -> String {
        let parameters = self
            .get_unused_parameters()
            .fold(String::new(), |output, (parameter, value)| {
                output + &format!("{parameter} = {value}, ")
            });
        let parameters = parameters.trim_end_matches(", ");
        let parameters = if parameters.is_empty() {
            "".into()
        } else {
            format!(" ({parameters})")
        };

        format!("{}{}", self.get_name(), parameters)
    }

    pub fn get_command_line(&self) -> String {
        self.replace_parameters_in(self.expression)
    }

    pub fn get_command(&self) -> Result<std::process::Command> {
        let command_line = self.get_command_line();
        let mut tokens = shell_words::split(&command_line)
            .with_context(|| format!("Failed to parse command '{command_line}'"))?
            .into_iter();

        if let Some(program_name) = tokens.next() {
            let mut command_builder = std::process::Command::new(program_name);
            command_builder.args(tokens);
            Ok(command_builder)
        } else {
            bail!("Can not execute empty command")
        }
    }

    pub fn get_parameters(&self) -> &[(&'a str, ParameterValue)] {
        &self.parameters
    }

    pub fn get_unused_parameters(&self) -> impl Iterator<Item = &(&'a str, ParameterValue)> {
        self.parameters
            .iter()
            .filter(move |(parameter, _)| !self.expression.contains(&format!("{{{parameter}}}")))
    }

    fn replace_parameters_in(&self, original: &str) -> String {
        let mut result = String::new();
        let mut replacements = BTreeMap::<String, String>::new();
        for (param_name, param_value) in &self.parameters {
            replacements.insert(format!("{{{param_name}}}"), param_value.to_string());
        }
        let mut remaining = original;
        // Manually replace consecutive occurrences to avoid double-replacing: e.g.,
        //
        //     hyperfine -L foo 'a,{bar}' -L bar 'baz,quux' 'echo {foo} {bar}'
        //
        // should not ever run 'echo baz baz'. See `test_get_command_line_nonoverlapping`.
        'outer: while let Some(head) = remaining.chars().next() {
            for (k, v) in &replacements {
                if remaining.starts_with(k.as_str()) {
                    result.push_str(v);
                    remaining = &remaining[k.len()..];
                    continue 'outer;
                }
            }
            result.push(head);
            remaining = &remaining[head.len_utf8()..];
        }
        result
    }
}

/// A collection of commands that should be benchmarked
pub struct Commands<'a>(Vec<Command<'a>>);

impl<'a> Commands<'a> {
    pub fn from_cli_arguments(matches: &'a ArgMatches) -> Result<Commands<'a>> {
        let command_names = matches.get_many::<String>("command-name");
        let command_strings = matches
            .get_many::<String>("command")
            .unwrap_or_default()
            .map(|v| v.as_str())
            .collect::<Vec<_>>();

        if let Some(args) = matches.get_many::<String>("parameter-scan") {
            let step_size = matches
                .get_one::<String>("parameter-step-size")
                .map(|s| s.as_str());
            Ok(Self(Self::get_parameter_scan_commands(
                command_names,
                command_strings,
                args,
                step_size,
            )?))
        } else if let Some(args) = matches.get_many::<String>("parameter-list") {
            let command_names = command_names.map_or(vec![], |names| {
                names.map(|v| v.as_str()).collect::<Vec<_>>()
            });
            let args: Vec<_> = args.map(|v| v.as_str()).collect::<Vec<_>>();
            let param_names_and_values: Vec<(&str, Vec<String>)> = args
                .chunks_exact(2)
                .map(|pair| {
                    let name = pair[0];
                    let list_str = pair[1];
                    (name, tokenize(list_str))
                })
                .collect();
            {
                let duplicates =
                    Self::find_duplicates(param_names_and_values.iter().map(|(name, _)| *name));
                if !duplicates.is_empty() {
                    bail!("Duplicate parameter names: {}", &duplicates.join(", "));
                }
            }

            let dimensions: Vec<usize> = std::iter::once(command_strings.len())
                .chain(
                    param_names_and_values
                        .iter()
                        .map(|(_, values)| values.len()),
                )
                .collect();
            let param_space_size = dimensions.iter().product();
            if param_space_size == 0 {
                return Ok(Self(Vec::new()));
            }

            // `--command-name` should appear exactly once or exactly B times,
            // where B is the total number of benchmarks.
            let command_name_count = command_names.len();
            if command_name_count > 1 && command_name_count != param_space_size {
                return Err(OptionsError::UnexpectedCommandNameCount(
                    command_name_count,
                    param_space_size,
                )
                .into());
            }

            let mut i = 0;
            let mut commands = Vec::with_capacity(param_space_size);
            let mut index = vec![0usize; dimensions.len()];
            'outer: loop {
                let name = command_names
                    .get(i)
                    .or_else(|| command_names.first())
                    .copied();
                i += 1;

                let (command_index, params_indices) = index.split_first().unwrap();
                let parameters: Vec<_> = param_names_and_values
                    .iter()
                    .zip(params_indices)
                    .map(|((name, values), i)| (*name, ParameterValue::Text(values[*i].clone())))
                    .collect();
                commands.push(Command::new_parametrized(
                    name,
                    command_strings[*command_index],
                    parameters,
                ));

                // Increment index, exiting loop on overflow.
                for (i, n) in index.iter_mut().zip(dimensions.iter()) {
                    *i += 1;
                    if *i < *n {
                        continue 'outer;
                    } else {
                        *i = 0;
                    }
                }
                break 'outer;
            }

            Ok(Self(commands))
        } else {
            let command_names = command_names.map_or(vec![], |names| {
                names.map(|v| v.as_str()).collect::<Vec<_>>()
            });
            if command_names.len() > command_strings.len() {
                return Err(OptionsError::TooManyCommandNames(command_strings.len()).into());
            }

            let mut commands = Vec::with_capacity(command_strings.len());
            for (i, s) in command_strings.iter().enumerate() {
                commands.push(Command::new(command_names.get(i).copied(), s));
            }
            Ok(Self(commands))
        }
    }

    pub fn iter(&self) -> impl Iterator<Item = &Command<'a>> {
        self.0.iter()
    }

    pub fn num_commands(&self, has_reference_command: bool) -> usize {
        self.0.len() + if has_reference_command { 1 } else { 0 }
    }

    /// Finds all the strings that appear multiple times in the input iterator, returning them in
    /// sorted order. If no string appears more than once, the result is an empty vector.
    fn find_duplicates<'b, I: IntoIterator<Item = &'b str>>(i: I) -> Vec<&'b str> {
        let mut counts = BTreeMap::<&'b str, usize>::new();
        for s in i {
            *counts.entry(s).or_default() += 1;
        }
        counts
            .into_iter()
            .filter_map(|(k, n)| if n > 1 { Some(k) } else { None })
            .collect()
    }

    fn build_parameter_scan_commands<'b, T: Numeric>(
        param_name: &'b str,
        param_min: T,
        param_max: T,
        step: T,
        command_names: Vec<&'b str>,
        command_strings: Vec<&'b str>,
    ) -> Result<Vec<Command<'b>>, ParameterScanError> {
        let param_range = RangeStep::new(param_min, param_max, step)?;
        let command_name_count = command_names.len();

        let mut i = 0;
        let mut commands = vec![];
        for value in param_range {
            for cmd in &command_strings {
                let name = command_names
                    .get(i)
                    .or_else(|| command_names.first())
                    .copied();
                commands.push(Command::new_parametrized(
                    name,
                    cmd,
                    vec![(param_name, ParameterValue::Numeric(value.into()))],
                ));
                i += 1;
            }
        }

        // `--command-name` should appear exactly once or exactly B times,
        // where B is the total number of benchmarks.
        let command_count = commands.len();
        if command_name_count > 1 && command_name_count != command_count {
            return Err(ParameterScanError::UnexpectedCommandNameCount(
                command_name_count,
                command_count,
            ));
        }

        Ok(commands)
    }

    fn get_parameter_scan_commands<'b>(
        command_names: Option<ValuesRef<'b, String>>,
        command_strings: Vec<&'b str>,
        mut vals: ValuesRef<'b, String>,
        step: Option<&str>,
    ) -> Result<Vec<Command<'b>>, ParameterScanError> {
        let command_names = command_names.map_or(vec![], |names| {
            names.map(|v| v.as_str()).collect::<Vec<_>>()
        });
        let param_name = vals.next().unwrap().as_str();
        let param_min = vals.next().unwrap().as_str();
        let param_max = vals.next().unwrap().as_str();

        // attempt to parse as integers
        if let (Ok(param_min), Ok(param_max), Ok(step)) = (
            param_min.parse::<i32>(),
            param_max.parse::<i32>(),
            step.unwrap_or("1").parse::<i32>(),
        ) {
            return Self::build_parameter_scan_commands(
                param_name,
                param_min,
                param_max,
                step,
                command_names,
                command_strings,
            );
        }

        // try parsing them as decimals
        let param_min = Decimal::from_str(param_min)?;
        let param_max = Decimal::from_str(param_max)?;

        if step.is_none() {
            return Err(ParameterScanError::StepRequired);
        }

        let step = Decimal::from_str(step.unwrap())?;
        Self::build_parameter_scan_commands(
            param_name,
            param_min,
            param_max,
            step,
            command_names,
            command_strings,
        )
    }
}

#[test]
fn test_get_command_line_nonoverlapping() {
    let cmd = Command::new_parametrized(
        None,
        "echo {foo} {bar}",
        vec![
            ("foo", ParameterValue::Text("{bar} baz".into())),
            ("bar", ParameterValue::Text("quux".into())),
        ],
    );
    assert_eq!(cmd.get_command_line(), "echo {bar} baz quux");
}

#[test]
fn test_get_parameterized_command_name() {
    let cmd = Command::new_parametrized(
        Some("name-{bar}-{foo}"),
        "echo {foo} {bar}",
        vec![
            ("foo", ParameterValue::Text("baz".into())),
            ("bar", ParameterValue::Text("quux".into())),
        ],
    );
    assert_eq!(cmd.get_name(), "name-quux-baz");
}

impl fmt::Display for Command<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.get_command_line())
    }
}

#[test]
fn test_build_commands_cross_product() {
    use crate::cli::get_cli_arguments;

    let matches = get_cli_arguments(vec![
        "hyperfine",
        "-L",
        "par1",
        "a,b",
        "-L",
        "par2",
        "z,y",
        "echo {par1} {par2}",
        "printf '%s\n' {par1} {par2}",
    ]);
    let result = Commands::from_cli_arguments(&matches).unwrap().0;

    // Iteration order: command list first, then parameters in listed order (here, "par1" before
    // "par2", which is distinct from their sorted order), with parameter values in listed order.
    let pv = |s: &str| ParameterValue::Text(s.to_string());
    let cmd = |cmd: usize, par1: &str, par2: &str| {
        let expression = ["echo {par1} {par2}", "printf '%s\n' {par1} {par2}"][cmd];
        let params = vec![("par1", pv(par1)), ("par2", pv(par2))];
        Command::new_parametrized(None, expression, params)
    };
    let expected = vec![
        cmd(0, "a", "z"),
        cmd(1, "a", "z"),
        cmd(0, "b", "z"),
        cmd(1, "b", "z"),
        cmd(0, "a", "y"),
        cmd(1, "a", "y"),
        cmd(0, "b", "y"),
        cmd(1, "b", "y"),
    ];
    assert_eq!(result, expected);
}

#[test]
fn test_build_parameter_list_commands() {
    use crate::cli::get_cli_arguments;

    let matches = get_cli_arguments(vec![
        "hyperfine",
        "echo {foo}",
        "--parameter-list",
        "foo",
        "1,2",
        "--command-name",
        "name-{foo}",
    ]);
    let commands = Commands::from_cli_arguments(&matches).unwrap().0;
    assert_eq!(commands.len(), 2);
    assert_eq!(commands[0].get_name(), "name-1");
    assert_eq!(commands[1].get_name(), "name-2");
    assert_eq!(commands[0].get_command_line(), "echo 1");
    assert_eq!(commands[1].get_command_line(), "echo 2");
}

#[test]
fn test_build_parameter_scan_commands() {
    use crate::cli::get_cli_arguments;
    let matches = get_cli_arguments(vec![
        "hyperfine",
        "echo {val}",
        "--parameter-scan",
        "val",
        "1",
        "2",
        "--parameter-step-size",
        "1",
        "--command-name",
        "name-{val}",
    ]);
    let commands = Commands::from_cli_arguments(&matches).unwrap().0;
    assert_eq!(commands.len(), 2);
    assert_eq!(commands[0].get_name(), "name-1");
    assert_eq!(commands[1].get_name(), "name-2");
    assert_eq!(commands[0].get_command_line(), "echo 1");
    assert_eq!(commands[1].get_command_line(), "echo 2");
}

#[test]
fn test_build_parameter_scan_commands_named() {
    use crate::cli::get_cli_arguments;
    let matches = get_cli_arguments(vec![
        "hyperfine",
        "echo {val}",
        "sleep {val}",
        "--parameter-scan",
        "val",
        "1",
        "2",
        "--parameter-step-size",
        "1",
        "--command-name",
        "echo-1",
        "--command-name",
        "sleep-1",
        "--command-name",
        "echo-2",
        "--command-name",
        "sleep-2",
    ]);
    let commands = Commands::from_cli_arguments(&matches).unwrap().0;
    assert_eq!(commands.len(), 4);
    assert_eq!(commands[0].get_name(), "echo-1");
    assert_eq!(commands[0].get_command_line(), "echo 1");
    assert_eq!(commands[1].get_name(), "sleep-1");
    assert_eq!(commands[1].get_command_line(), "sleep 1");
    assert_eq!(commands[2].get_name(), "echo-2");
    assert_eq!(commands[2].get_command_line(), "echo 2");
    assert_eq!(commands[3].get_name(), "sleep-2");
    assert_eq!(commands[3].get_command_line(), "sleep 2");
}

#[test]
fn test_parameter_scan_commands_int() {
    let commands = Commands::build_parameter_scan_commands(
        "val",
        1i32,
        7i32,
        3i32,
        vec![],
        vec!["echo {val}"],
    )
    .unwrap();
    assert_eq!(commands.len(), 3);
    assert_eq!(commands[2].get_name(), "echo 7");
    assert_eq!(commands[2].get_command_line(), "echo 7");
}

#[test]
fn test_parameter_scan_commands_decimal() {
    let param_min = Decimal::from_str("0").unwrap();
    let param_max = Decimal::from_str("1").unwrap();
    let step = Decimal::from_str("0.33").unwrap();

    let commands = Commands::build_parameter_scan_commands(
        "val",
        param_min,
        param_max,
        step,
        vec![],
        vec!["echo {val}"],
    )
    .unwrap();
    assert_eq!(commands.len(), 4);
    assert_eq!(commands[3].get_name(), "echo 0.99");
    assert_eq!(commands[3].get_command_line(), "echo 0.99");
}

#[test]
fn test_parameter_scan_commands_names() {
    let commands = Commands::build_parameter_scan_commands(
        "val",
        1i32,
        3i32,
        1i32,
        vec!["name-{val}"],
        vec!["echo {val}"],
    )
    .unwrap();
    assert_eq!(commands.len(), 3);
    let command_names = commands
        .iter()
        .map(|c| c.get_name())
        .collect::<Vec<String>>();
    assert_eq!(command_names, vec!["name-1", "name-2", "name-3"]);
}

#[test]
fn test_get_specified_command_names() {
    let commands = Commands::build_parameter_scan_commands(
        "val",
        1i32,
        3i32,
        1i32,
        vec!["name-a", "name-b", "name-c"],
        vec!["echo {val}"],
    )
    .unwrap();
    assert_eq!(commands.len(), 3);
    let command_names = commands
        .iter()
        .map(|c| c.get_name())
        .collect::<Vec<String>>();
    assert_eq!(command_names, vec!["name-a", "name-b", "name-c"]);
}

#[test]
fn test_different_command_name_count_with_parameters() {
    let result = Commands::build_parameter_scan_commands(
        "val",
        1i32,
        3i32,
        1i32,
        vec!["name-1", "name-2"],
        vec!["echo {val}"],
    );
    assert!(matches!(
        result.unwrap_err(),
        ParameterScanError::UnexpectedCommandNameCount(2, 3)
    ));
}
```

## File: `src/error.rs`
```rust
use std::num::{self, ParseFloatError, ParseIntError};

use rust_decimal::Error as DecimalError;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum ParameterScanError {
    #[error("Error while parsing parameter scan arguments ({0})")]
    ParseIntError(num::ParseIntError),
    #[error("Error while parsing parameter scan arguments ({0})")]
    ParseDecimalError(DecimalError),
    #[error("Empty parameter range")]
    EmptyRange,
    #[error("Parameter range is too large")]
    TooLarge,
    #[error("Zero is not a valid parameter step")]
    ZeroStep,
    #[error("A step size is required when the range bounds are floating point numbers. The step size can be specified with the '-D/--parameter-step-size <DELTA>' parameter")]
    StepRequired,
    #[error("'--command-name' has been specified {0} times. It has to appear exactly once, or exactly {1} times (number of benchmarks)")]
    UnexpectedCommandNameCount(usize, usize),
}

impl From<num::ParseIntError> for ParameterScanError {
    fn from(e: num::ParseIntError) -> ParameterScanError {
        ParameterScanError::ParseIntError(e)
    }
}

impl From<DecimalError> for ParameterScanError {
    fn from(e: DecimalError) -> ParameterScanError {
        ParameterScanError::ParseDecimalError(e)
    }
}

#[derive(Debug, Error)]
pub enum OptionsError<'a> {
    #[error(
        "Conflicting requirements for the number of runs (empty range, min is larger than max)"
    )]
    EmptyRunsRange,
    #[error("Too many --command-name options: Expected {0} at most")]
    TooManyCommandNames(usize),
    #[error("'--command-name' has been specified {0} times. It has to appear exactly once, or exactly {1} times (number of benchmarks)")]
    UnexpectedCommandNameCount(usize, usize),
    #[error("Could not read numeric integer argument to '--{0}': {1}")]
    IntParsingError(&'a str, ParseIntError),
    #[error("Could not read numeric floating point argument to '--{0}': {1}")]
    FloatParsingError(&'a str, ParseFloatError),
    #[error("An empty command has been specified for the '--shell <command>' option")]
    EmptyShell,
    #[error("Failed to parse '--shell <command>' expression as command line: {0}")]
    ShellParseError(shell_words::ParseError),
    #[error("Unknown output policy '{0}'. Use './{0}' to output to a file named '{0}'.")]
    UnknownOutputPolicy(String),
    #[error("The file '{0}' specified as '--input' does not exist")]
    StdinDataFileDoesNotExist(String),
}
```

## File: `src/main.rs`
```rust
#![cfg_attr(
    all(windows, feature = "windows_process_extensions_main_thread_handle"),
    feature(windows_process_extensions_main_thread_handle)
)]

use std::env;

use benchmark::scheduler::Scheduler;
use cli::get_cli_arguments;
use command::Commands;
use export::ExportManager;
use options::Options;

use anyhow::Result;
use colored::*;

pub mod benchmark;
pub mod cli;
pub mod command;
pub mod error;
pub mod export;
pub mod options;
pub mod outlier_detection;
pub mod output;
pub mod parameter;
pub mod timer;
pub mod util;

fn run() -> Result<()> {
    // Enabled ANSI colors on Windows 10
    #[cfg(windows)]
    colored::control::set_virtual_terminal(true).unwrap();

    let cli_arguments = get_cli_arguments(env::args_os());
    let mut options = Options::from_cli_arguments(&cli_arguments)?;
    let commands = Commands::from_cli_arguments(&cli_arguments)?;
    let export_manager = ExportManager::from_cli_arguments(
        &cli_arguments,
        options.time_unit,
        options.sort_order_exports,
    )?;

    options.validate_against_command_list(&commands)?;

    let mut scheduler = Scheduler::new(&commands, &options, &export_manager);
    scheduler.run_benchmarks()?;
    scheduler.print_relative_speed_comparison();
    scheduler.final_export()?;

    Ok(())
}

fn main() {
    match run() {
        Ok(_) => {}
        Err(e) => {
            eprintln!("{} {:#}", "Error:".red(), e);
            std::process::exit(1);
        }
    }
}
```

## File: `src/options.rs`
```rust
use std::fs::File;
use std::io::IsTerminal;
use std::path::PathBuf;
use std::process::{Command, Stdio};
use std::{cmp, env, fmt, io};

use anyhow::ensure;
use clap::ArgMatches;

use crate::command::Commands;
use crate::error::OptionsError;
use crate::util::units::{Second, Unit};

use anyhow::Result;

#[cfg(not(windows))]
pub const DEFAULT_SHELL: &str = "sh";

#[cfg(windows)]
pub const DEFAULT_SHELL: &str = "cmd.exe";

/// Shell to use for executing benchmarked commands
#[derive(Debug, PartialEq)]
pub enum Shell {
    /// Default shell command
    Default(&'static str),

    /// Custom shell command specified via --shell
    Custom(Vec<String>),
}

impl Default for Shell {
    fn default() -> Self {
        Shell::Default(DEFAULT_SHELL)
    }
}

impl fmt::Display for Shell {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Shell::Default(cmd) => write!(f, "{cmd}"),
            Shell::Custom(cmdline) => write!(f, "{}", shell_words::join(cmdline)),
        }
    }
}

impl Shell {
    /// Parse given string as shell command line
    pub fn parse_from_str<'a>(s: &str) -> Result<Self, OptionsError<'a>> {
        let v = shell_words::split(s).map_err(OptionsError::ShellParseError)?;
        if v.is_empty() || v[0].is_empty() {
            return Err(OptionsError::EmptyShell);
        }
        Ok(Shell::Custom(v))
    }

    pub fn command(&self) -> Command {
        match self {
            Shell::Default(cmd) => Command::new(cmd),
            Shell::Custom(cmdline) => {
                let mut c = Command::new(&cmdline[0]);
                c.args(&cmdline[1..]);
                c
            }
        }
    }
}

/// Action to take when an executed command fails.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum CmdFailureAction {
    /// Exit with an error message
    RaiseError,

    /// Ignore all non-zero exit codes
    IgnoreAllFailures,

    /// Ignore specific exit codes
    IgnoreSpecificFailures(Vec<i32>),
}

/// Output style type option
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OutputStyleOption {
    /// Do not output with colors or any special formatting
    Basic,

    /// Output with full color and formatting
    Full,

    /// Keep elements such as progress bar, but use no coloring
    NoColor,

    /// Keep coloring, but use no progress bar
    Color,

    /// Disable all the output
    Disabled,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SortOrder {
    Command,
    MeanTime,
}

/// Bounds for the number of benchmark runs
pub struct RunBounds {
    /// Minimum number of benchmark runs
    pub min: u64,

    /// Maximum number of benchmark runs
    pub max: Option<u64>,
}

impl Default for RunBounds {
    fn default() -> Self {
        RunBounds { min: 10, max: None }
    }
}

#[derive(Debug, Default, Clone, PartialEq)]
pub enum CommandInputPolicy {
    /// Read from the null device
    #[default]
    Null,

    /// Read input from a file
    File(PathBuf),
}

impl CommandInputPolicy {
    pub fn get_stdin(&self) -> io::Result<Stdio> {
        let stream: Stdio = match self {
            CommandInputPolicy::Null => Stdio::null(),

            CommandInputPolicy::File(path) => {
                let file: File = File::open(path)?;
                Stdio::from(file)
            }
        };

        Ok(stream)
    }
}

/// How to handle the output of benchmarked commands
#[derive(Debug, Clone, PartialEq, Eq, Default)]
pub enum CommandOutputPolicy {
    /// Redirect output to the null device
    #[default]
    Null,

    /// Feed output through a pipe before discarding it
    Pipe,

    /// Redirect output to a file
    File(PathBuf),

    /// Show command output on the terminal
    Inherit,
}

impl CommandOutputPolicy {
    pub fn get_stdout_stderr(&self) -> io::Result<(Stdio, Stdio)> {
        let streams = match self {
            CommandOutputPolicy::Null => (Stdio::null(), Stdio::null()),

            // Typically only stdout is performance-relevant, so just pipe that
            CommandOutputPolicy::Pipe => (Stdio::piped(), Stdio::null()),

            CommandOutputPolicy::File(path) => {
                let file = File::create(path)?;
                (file.into(), Stdio::null())
            }

            CommandOutputPolicy::Inherit => (Stdio::inherit(), Stdio::inherit()),
        };

        Ok(streams)
    }
}

#[derive(Debug, PartialEq)]
pub enum ExecutorKind {
    Raw,
    Shell(Shell),
    Mock(Option<String>),
}

impl Default for ExecutorKind {
    fn default() -> Self {
        ExecutorKind::Shell(Shell::default())
    }
}

/// The main settings for a hyperfine benchmark session
pub struct Options {
    /// Upper and lower bound for the number of benchmark runs
    pub run_bounds: RunBounds,

    /// Number of warmup runs
    pub warmup_count: u64,

    /// Minimum benchmarking time
    pub min_benchmarking_time: Second,

    /// Whether or not to ignore non-zero exit codes
    pub command_failure_action: CmdFailureAction,

    // Command to use as a reference for relative speed comparison
    pub reference_command: Option<String>,

    // Name of the reference command
    pub reference_name: Option<String>,

    /// Command(s) to run before each timing run
    pub preparation_command: Option<Vec<String>>,

    /// Command(s) to run after each timing run
    pub conclusion_command: Option<Vec<String>>,

    /// Command to run before each *batch* of timing runs, i.e. before each individual benchmark
    pub setup_command: Option<String>,

    /// Command to run after each *batch* of timing runs, i.e. after each individual benchmark
    pub cleanup_command: Option<String>,

    /// What color mode to use for the terminal output
    pub output_style: OutputStyleOption,

    /// How to order benchmarks in the relative speed comparison
    pub sort_order_speed_comparison: SortOrder,

    /// How to order benchmarks in the markup format exports
    pub sort_order_exports: SortOrder,

    /// Determines how we run commands
    pub executor_kind: ExecutorKind,

    /// Where input to the benchmarked command comes from
    pub command_input_policy: CommandInputPolicy,

    /// What to do with the output of the benchmarked commands
    pub command_output_policies: Vec<CommandOutputPolicy>,

    /// Which time unit to use when displaying results
    pub time_unit: Option<Unit>,
}

impl Default for Options {
    fn default() -> Options {
        Options {
            run_bounds: RunBounds::default(),
            warmup_count: 0,
            min_benchmarking_time: 3.0,
            command_failure_action: CmdFailureAction::RaiseError,
            reference_command: None,
            reference_name: None,
            preparation_command: None,
            conclusion_command: None,
            setup_command: None,
            cleanup_command: None,
            output_style: OutputStyleOption::Full,
            sort_order_speed_comparison: SortOrder::MeanTime,
            sort_order_exports: SortOrder::Command,
            executor_kind: ExecutorKind::default(),
            command_output_policies: vec![CommandOutputPolicy::Null],
            time_unit: None,
            command_input_policy: CommandInputPolicy::Null,
        }
    }
}

impl Options {
    pub fn from_cli_arguments<'a>(matches: &ArgMatches) -> Result<Self, OptionsError<'a>> {
        let mut options = Self::default();
        let param_to_u64 = |param| {
            matches
                .get_one::<String>(param)
                .map(|n| {
                    n.parse::<u64>()
                        .map_err(|e| OptionsError::IntParsingError(param, e))
                })
                .transpose()
        };

        options.warmup_count = param_to_u64("warmup")?.unwrap_or(options.warmup_count);

        let mut min_runs = param_to_u64("min-runs")?;
        let mut max_runs = param_to_u64("max-runs")?;

        if let Some(runs) = param_to_u64("runs")? {
            min_runs = Some(runs);
            max_runs = Some(runs);
        }

        match (min_runs, max_runs) {
            (Some(min), None) => {
                options.run_bounds.min = min;
            }
            (None, Some(max)) => {
                // Since the minimum was not explicit we lower it if max is below the default min.
                options.run_bounds.min = cmp::min(options.run_bounds.min, max);
                options.run_bounds.max = Some(max);
            }
            (Some(min), Some(max)) if min > max => {
                return Err(OptionsError::EmptyRunsRange);
            }
            (Some(min), Some(max)) => {
                options.run_bounds.min = min;
                options.run_bounds.max = Some(max);
            }
            (None, None) => {}
        };

        options.setup_command = matches.get_one::<String>("setup").map(String::from);

        options.reference_command = matches.get_one::<String>("reference").map(String::from);
        options.reference_name = matches
            .get_one::<String>("reference-name")
            .map(String::from);

        options.preparation_command = matches
            .get_many::<String>("prepare")
            .map(|values| values.map(String::from).collect::<Vec<String>>());

        options.conclusion_command = matches
            .get_many::<String>("conclude")
            .map(|values| values.map(String::from).collect::<Vec<String>>());

        options.cleanup_command = matches.get_one::<String>("cleanup").map(String::from);

        options.command_output_policies = if matches.get_flag("show-output") {
            vec![CommandOutputPolicy::Inherit]
        } else if let Some(output_values) = matches.get_many::<String>("output") {
            let mut policies = vec![];
            for value in output_values {
                let policy = match value.as_str() {
                    "null" => CommandOutputPolicy::Null,
                    "pipe" => CommandOutputPolicy::Pipe,
                    "inherit" => CommandOutputPolicy::Inherit,
                    arg => {
                        let path = PathBuf::from(arg);
                        if path.components().count() <= 1 {
                            return Err(OptionsError::UnknownOutputPolicy(arg.to_string()));
                        }
                        CommandOutputPolicy::File(path)
                    }
                };
                policies.push(policy);
            }
            policies
        } else {
            vec![CommandOutputPolicy::Null]
        };

        options.output_style = match matches.get_one::<String>("style").map(|s| s.as_str()) {
            Some("full") => OutputStyleOption::Full,
            Some("basic") => OutputStyleOption::Basic,
            Some("nocolor") => OutputStyleOption::NoColor,
            Some("color") => OutputStyleOption::Color,
            Some("none") => OutputStyleOption::Disabled,
            _ => {
                if options
                    .command_output_policies
                    .contains(&CommandOutputPolicy::Inherit)
                    || !io::stdout().is_terminal()
                {
                    OutputStyleOption::Basic
                } else if env::var_os("TERM")
                    .map(|t| t == "unknown" || t == "dumb")
                    .unwrap_or(!cfg!(target_os = "windows"))
                    || env::var_os("NO_COLOR")
                        .map(|t| !t.is_empty())
                        .unwrap_or(false)
                {
                    OutputStyleOption::NoColor
                } else {
                    OutputStyleOption::Full
                }
            }
        };

        match options.output_style {
            OutputStyleOption::Basic | OutputStyleOption::NoColor => {
                colored::control::set_override(false)
            }
            OutputStyleOption::Full | OutputStyleOption::Color => {
                colored::control::set_override(true)
            }
            OutputStyleOption::Disabled => {}
        };

        (
            options.sort_order_speed_comparison,
            options.sort_order_exports,
        ) = match matches.get_one::<String>("sort").map(|s| s.as_str()) {
            None | Some("auto") => (SortOrder::MeanTime, SortOrder::Command),
            Some("command") => (SortOrder::Command, SortOrder::Command),
            Some("mean-time") => (SortOrder::MeanTime, SortOrder::MeanTime),
            Some(_) => unreachable!("Unknown sort order"),
        };

        options.executor_kind = if matches.get_flag("no-shell") {
            ExecutorKind::Raw
        } else {
            match (
                matches.get_flag("debug-mode"),
                matches.get_one::<String>("shell"),
            ) {
                (false, Some(shell)) if shell == "default" => ExecutorKind::Shell(Shell::default()),
                (false, Some(shell)) if shell == "none" => ExecutorKind::Raw,
                (false, Some(shell)) => ExecutorKind::Shell(Shell::parse_from_str(shell)?),
                (false, None) => ExecutorKind::Shell(Shell::default()),
                (true, Some(shell)) => ExecutorKind::Mock(Some(shell.into())),
                (true, None) => ExecutorKind::Mock(None),
            }
        };

        if let Some(mode) = matches.get_one::<String>("ignore-failure") {
            options.command_failure_action = match mode.as_str() {
                "all-non-zero" | "" => CmdFailureAction::IgnoreAllFailures,
                codes => {
                    let exit_codes: Result<Vec<i32>, _> = codes
                        .split(',')
                        .map(|s| {
                            s.trim()
                                .parse::<i32>()
                                .map_err(|e| OptionsError::IntParsingError("ignore-failure", e))
                        })
                        .collect();
                    CmdFailureAction::IgnoreSpecificFailures(exit_codes?)
                }
            };
        }

        options.time_unit = match matches.get_one::<String>("time-unit").map(|s| s.as_str()) {
            Some("microsecond") => Some(Unit::MicroSecond),
            Some("millisecond") => Some(Unit::MilliSecond),
            Some("second") => Some(Unit::Second),
            _ => None,
        };

        if let Some(time) = matches.get_one::<String>("min-benchmarking-time") {
            options.min_benchmarking_time = time
                .parse::<f64>()
                .map_err(|e| OptionsError::FloatParsingError("min-benchmarking-time", e))?;
        }

        options.command_input_policy = if let Some(path_str) = matches.get_one::<String>("input") {
            if path_str == "null" {
                CommandInputPolicy::Null
            } else {
                let path = PathBuf::from(path_str);
                if !path.exists() {
                    return Err(OptionsError::StdinDataFileDoesNotExist(
                        path_str.to_string(),
                    ));
                }
                CommandInputPolicy::File(path)
            }
        } else {
            CommandInputPolicy::Null
        };

        Ok(options)
    }

    pub fn validate_against_command_list(&mut self, commands: &Commands) -> Result<()> {
        let has_reference_command = self.reference_command.is_some();
        let num_commands = commands.num_commands(has_reference_command);

        if let Some(preparation_command) = &self.preparation_command {
            ensure!(
                preparation_command.len() <= 1 || num_commands == preparation_command.len(),
                "The '--prepare' option has to be provided just once or N times, where N={num_commands} is the \
                 number of benchmark commands (including a potential reference)."
            );
        }

        if let Some(conclusion_command) = &self.conclusion_command {
            ensure!(
                conclusion_command.len() <= 1 || num_commands == conclusion_command.len(),
                "The '--conclude' option has to be provided just once or N times, where N={num_commands} is the \
                 number of benchmark commands (including a potential reference)."
            );
        }

        if self.command_output_policies.len() == 1 {
            self.command_output_policies =
                vec![self.command_output_policies[0].clone(); num_commands];
        } else {
            ensure!(
                self.command_output_policies.len() == num_commands,
                "The '--output' option has to be provided just once or N times, where N={num_commands} is the \
                 number of benchmark commands (including a potential reference)."
            );
        }

        Ok(())
    }
}

#[test]
fn test_default_shell() {
    let shell = Shell::default();

    let s = format!("{shell}");
    assert_eq!(&s, DEFAULT_SHELL);

    let cmd = shell.command();
    assert_eq!(cmd.get_program(), DEFAULT_SHELL);
}

#[test]
fn test_can_parse_shell_command_line_from_str() {
    let shell = Shell::parse_from_str("shell -x 'aaa bbb'").unwrap();

    let s = format!("{shell}");
    assert_eq!(&s, "shell -x 'aaa bbb'");

    let cmd = shell.command();
    assert_eq!(cmd.get_program().to_string_lossy(), "shell");
    assert_eq!(
        cmd.get_args()
            .map(|a| a.to_string_lossy())
            .collect::<Vec<_>>(),
        vec!["-x", "aaa bbb"]
    );

    // Error cases
    assert!(matches!(
        Shell::parse_from_str("shell 'foo").unwrap_err(),
        OptionsError::ShellParseError(_)
    ));

    assert!(matches!(
        Shell::parse_from_str("").unwrap_err(),
        OptionsError::EmptyShell
    ));

    assert!(matches!(
        Shell::parse_from_str("''").unwrap_err(),
        OptionsError::EmptyShell
    ));
}
```

## File: `src/outlier_detection.rs`
```rust
//! A module for statistical outlier detection.
//!
//! References:
//! - Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and Handle Outliers",
//!   The ASQC Basic References in Quality Control: Statistical Techniques, Edward F. Mykytka,
//!   Ph.D., Editor.

use statistical::median;

/// Minimum modified Z-score for a datapoint to be an outlier. Here, 1.4826 is a factor that
/// converts the MAD to an estimator for the standard deviation. The second factor is the number
/// of standard deviations.
pub const OUTLIER_THRESHOLD: f64 = 1.4826 * 10.0;

/// Compute modifized Z-scores for a given sample. A (unmodified) Z-score is defined by
/// `(x_i - x_mean)/x_stddev` whereas the modified Z-score is defined by `(x_i - x_median)/MAD`
/// where MAD is the median absolute deviation.
///
/// References:
/// - <https://en.wikipedia.org/wiki/Median_absolute_deviation>
pub fn modified_zscores(xs: &[f64]) -> Vec<f64> {
    assert!(!xs.is_empty());

    // Compute sample median:
    let x_median = median(xs);

    // Compute the absolute deviations from the median:
    let deviations: Vec<f64> = xs.iter().map(|x| (x - x_median).abs()).collect();

    // Compute median absolute deviation:
    let mad = median(&deviations);

    // Handle MAD == 0 case
    let mad = if mad > 0.0 { mad } else { f64::EPSILON };

    // Compute modified Z-scores (x_i - x_median) / MAD
    xs.iter().map(|&x| (x - x_median) / mad).collect()
}

/// Return the number of outliers in a given sample. Outliers are defined as data points with a
/// modified Z-score that is larger than `OUTLIER_THRESHOLD`.
#[cfg(test)]
pub fn num_outliers(xs: &[f64]) -> usize {
    if xs.is_empty() {
        return 0;
    }

    let scores = modified_zscores(xs);
    scores
        .iter()
        .filter(|&&s| s.abs() > OUTLIER_THRESHOLD)
        .count()
}

#[test]
fn test_detect_outliers() {
    // Should not detect outliers in small samples
    assert_eq!(0, num_outliers(&[]));
    assert_eq!(0, num_outliers(&[50.0]));
    assert_eq!(0, num_outliers(&[1000.0, 0.0]));

    // Should not detect outliers in low-variance samples
    let xs = [-0.2, 0.0, 0.2];
    assert_eq!(0, num_outliers(&xs));

    // Should detect a single outlier
    let xs = [-0.2, 0.0, 0.2, 4.0];
    assert_eq!(1, num_outliers(&xs));

    // Should detect a single outlier
    let xs = [0.5, 0.30, 0.29, 0.31, 0.30];
    assert_eq!(1, num_outliers(&xs));

    // Should detect no outliers in sample drawn from normal distribution
    let xs = [
        2.33269488,
        1.42195907,
        -0.57527698,
        -0.31293437,
        2.2948158,
        0.75813273,
        -1.0712388,
        -0.96394741,
        -1.15897446,
        1.10976285,
    ];
    assert_eq!(0, num_outliers(&xs));

    // Should detect two outliers that were manually added
    let xs = [
        2.33269488,
        1.42195907,
        -0.57527698,
        -0.31293437,
        2.2948158,
        0.75813273,
        -1.0712388,
        -0.96394741,
        -1.15897446,
        1.10976285,
        20.0,
        -500.0,
    ];
    assert_eq!(2, num_outliers(&xs));
}

#[test]
fn test_detect_outliers_if_mad_becomes_0() {
    // See https://stats.stackexchange.com/q/339932
    let xs = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 100.0];
    assert_eq!(1, num_outliers(&xs));

    let xs = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 100.0, 100.0];
    assert_eq!(2, num_outliers(&xs));
}
```

## File: `src/benchmark/benchmark_result.rs`
```rust
use std::collections::BTreeMap;

use serde::Serialize;

use crate::util::units::Second;

/// Set of values that will be exported.
// NOTE: `serde` is used for JSON serialization, but not for CSV serialization due to the
// `parameters` map. Update `src/hyperfine/export/csv.rs` with new fields, as appropriate.
#[derive(Debug, Default, Clone, Serialize, PartialEq)]
pub struct BenchmarkResult {
    /// The full command line of the program that is being benchmarked
    pub command: String,

    /// The full command line of the program that is being benchmarked, possibly including a list of
    /// parameters that were not used in the command line template.
    #[serde(skip_serializing)]
    pub command_with_unused_parameters: String,

    /// The average run time
    pub mean: Second,

    /// The standard deviation of all run times. Not available if only one run has been performed
    pub stddev: Option<Second>,

    /// The median run time
    pub median: Second,

    /// Time spent in user mode
    pub user: Second,

    /// Time spent in kernel mode
    pub system: Second,

    /// Minimum of all measured times
    pub min: Second,

    /// Maximum of all measured times
    pub max: Second,

    /// All run time measurements
    #[serde(skip_serializing_if = "Option::is_none")]
    pub times: Option<Vec<Second>>,

    /// Maximum memory usage of the process, in bytes
    #[serde(skip_serializing_if = "Option::is_none")]
    pub memory_usage_byte: Option<Vec<u64>>,

    /// Exit codes of all command invocations
    pub exit_codes: Vec<Option<i32>>,

    /// Parameter values for this benchmark
    #[serde(skip_serializing_if = "BTreeMap::is_empty")]
    pub parameters: BTreeMap<String, String>,
}
```

## File: `src/benchmark/executor.rs`
```rust
#[cfg(windows)]
use std::os::windows::process::CommandExt;
use std::process::ExitStatus;

use crate::command::Command;
use crate::options::{
    CmdFailureAction, CommandInputPolicy, CommandOutputPolicy, Options, OutputStyleOption, Shell,
};
use crate::output::progress_bar::get_progress_bar;
use crate::timer::{execute_and_measure, TimerResult};
use crate::util::randomized_environment_offset;
use crate::util::units::Second;

use super::timing_result::TimingResult;

use anyhow::{bail, Context, Result};
use statistical::mean;

pub enum BenchmarkIteration {
    NonBenchmarkRun,
    Warmup(u64),
    Benchmark(u64),
}

impl BenchmarkIteration {
    pub fn to_env_var_value(&self) -> Option<String> {
        match self {
            BenchmarkIteration::NonBenchmarkRun => None,
            BenchmarkIteration::Warmup(i) => Some(format!("warmup-{}", i)),
            BenchmarkIteration::Benchmark(i) => Some(format!("{}", i)),
        }
    }
}

pub trait Executor {
    /// Run the given command and measure the execution time
    fn run_command_and_measure(
        &self,
        command: &Command<'_>,
        iteration: BenchmarkIteration,
        command_failure_action: Option<CmdFailureAction>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<(TimingResult, ExitStatus)>;

    /// Perform a calibration of this executor. For example,
    /// when running commands through a shell, we need to
    /// measure the shell spawning time separately in order
    /// to subtract it from the full runtime later.
    fn calibrate(&mut self) -> Result<()>;

    /// Return the time overhead for this executor when
    /// performing a measurement. This should return the time
    /// that is being used in addition to the actual runtime
    /// of the command.
    fn time_overhead(&self) -> Second;
}

fn run_command_and_measure_common(
    mut command: std::process::Command,
    iteration: BenchmarkIteration,
    command_failure_action: CmdFailureAction,
    command_input_policy: &CommandInputPolicy,
    command_output_policy: &CommandOutputPolicy,
    command_name: &str,
) -> Result<TimerResult> {
    let stdin = command_input_policy.get_stdin()?;
    let (stdout, stderr) = command_output_policy.get_stdout_stderr()?;
    command.stdin(stdin).stdout(stdout).stderr(stderr);

    command.env(
        "HYPERFINE_RANDOMIZED_ENVIRONMENT_OFFSET",
        randomized_environment_offset::value(),
    );

    if let Some(value) = iteration.to_env_var_value() {
        command.env("HYPERFINE_ITERATION", value);
    }

    let result = execute_and_measure(command)
        .with_context(|| format!("Failed to run command '{command_name}'"))?;

    if !result.status.success() {
        use crate::util::exit_code::extract_exit_code;

        let should_fail = match command_failure_action {
            CmdFailureAction::RaiseError => true,
            CmdFailureAction::IgnoreAllFailures => false,
            CmdFailureAction::IgnoreSpecificFailures(ref codes) => {
                // Only fail if the exit code is not in the list of codes to ignore
                if let Some(exit_code) = extract_exit_code(result.status) {
                    !codes.contains(&exit_code)
                } else {
                    // If we can't extract an exit code, treat it as a failure
                    true
                }
            }
        };

        if should_fail {
            let when = match iteration {
                BenchmarkIteration::NonBenchmarkRun => "a non-benchmark run".to_string(),
                BenchmarkIteration::Warmup(0) => "the first warmup run".to_string(),
                BenchmarkIteration::Warmup(i) => format!("warmup iteration {i}"),
                BenchmarkIteration::Benchmark(0) => "the first benchmark run".to_string(),
                BenchmarkIteration::Benchmark(i) => format!("benchmark iteration {i}"),
            };
            bail!(
                "{cause} in {when}. Use the '-i'/'--ignore-failure' option if you want to ignore this. \
                Alternatively, use the '--show-output' option to debug what went wrong.",
                cause=result.status.code().map_or(
                    "The process has been terminated by a signal".into(),
                    |c| format!("Command terminated with non-zero exit code {c}")

                ),
            );
        }
    }

    Ok(result)
}

pub struct RawExecutor<'a> {
    options: &'a Options,
}

impl<'a> RawExecutor<'a> {
    pub fn new(options: &'a Options) -> Self {
        RawExecutor { options }
    }
}

impl Executor for RawExecutor<'_> {
    fn run_command_and_measure(
        &self,
        command: &Command<'_>,
        iteration: BenchmarkIteration,
        command_failure_action: Option<CmdFailureAction>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<(TimingResult, ExitStatus)> {
        let result = run_command_and_measure_common(
            command.get_command()?,
            iteration,
            command_failure_action.unwrap_or_else(|| self.options.command_failure_action.clone()),
            &self.options.command_input_policy,
            output_policy,
            &command.get_command_line(),
        )?;

        Ok((
            TimingResult {
                time_real: result.time_real,
                time_user: result.time_user,
                time_system: result.time_system,
                memory_usage_byte: result.memory_usage_byte,
            },
            result.status,
        ))
    }

    fn calibrate(&mut self) -> Result<()> {
        Ok(())
    }

    fn time_overhead(&self) -> Second {
        0.0
    }
}

pub struct ShellExecutor<'a> {
    options: &'a Options,
    shell: &'a Shell,
    shell_spawning_time: Option<TimingResult>,
}

impl<'a> ShellExecutor<'a> {
    pub fn new(shell: &'a Shell, options: &'a Options) -> Self {
        ShellExecutor {
            shell,
            options,
            shell_spawning_time: None,
        }
    }
}

impl Executor for ShellExecutor<'_> {
    fn run_command_and_measure(
        &self,
        command: &Command<'_>,
        iteration: BenchmarkIteration,
        command_failure_action: Option<CmdFailureAction>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<(TimingResult, ExitStatus)> {
        let on_windows_cmd = cfg!(windows) && *self.shell == Shell::Default("cmd.exe");
        let mut command_builder = self.shell.command();
        command_builder.arg(if on_windows_cmd { "/C" } else { "-c" });

        // Windows needs special treatment for its behavior on parsing cmd arguments
        if on_windows_cmd {
            #[cfg(windows)]
            command_builder.raw_arg(command.get_command_line());
        } else {
            command_builder.arg(command.get_command_line());
        }

        let mut result = run_command_and_measure_common(
            command_builder,
            iteration,
            command_failure_action.unwrap_or_else(|| self.options.command_failure_action.clone()),
            &self.options.command_input_policy,
            output_policy,
            &command.get_command_line(),
        )?;

        // Subtract shell spawning time
        if let Some(spawning_time) = self.shell_spawning_time {
            result.time_real = (result.time_real - spawning_time.time_real).max(0.0);
            result.time_user = (result.time_user - spawning_time.time_user).max(0.0);
            result.time_system = (result.time_system - spawning_time.time_system).max(0.0);
        }

        Ok((
            TimingResult {
                time_real: result.time_real,
                time_user: result.time_user,
                time_system: result.time_system,
                memory_usage_byte: result.memory_usage_byte,
            },
            result.status,
        ))
    }

    /// Measure the average shell spawning time
    fn calibrate(&mut self) -> Result<()> {
        const COUNT: u64 = 50;
        let progress_bar = if self.options.output_style != OutputStyleOption::Disabled {
            Some(get_progress_bar(
                COUNT,
                "Measuring shell spawning time",
                self.options.output_style,
            ))
        } else {
            None
        };

        let mut times_real: Vec<Second> = vec![];
        let mut times_user: Vec<Second> = vec![];
        let mut times_system: Vec<Second> = vec![];

        for _ in 0..COUNT {
            // Just run the shell without any command
            let res = self.run_command_and_measure(
                &Command::new(None, ""),
                BenchmarkIteration::NonBenchmarkRun,
                None,
                &CommandOutputPolicy::Null,
            );

            match res {
                Err(_) => {
                    let shell_cmd = if cfg!(windows) {
                        format!("{} /C \"\"", self.shell)
                    } else {
                        format!("{} -c \"\"", self.shell)
                    };

                    bail!(
                        "Could not measure shell execution time. Make sure you can run '{}'.",
                        shell_cmd
                    );
                }
                Ok((r, _)) => {
                    times_real.push(r.time_real);
                    times_user.push(r.time_user);
                    times_system.push(r.time_system);
                }
            }

            if let Some(bar) = progress_bar.as_ref() {
                bar.inc(1)
            }
        }

        if let Some(bar) = progress_bar.as_ref() {
            bar.finish_and_clear()
        }

        self.shell_spawning_time = Some(TimingResult {
            time_real: mean(&times_real),
            time_user: mean(&times_user),
            time_system: mean(&times_system),
            memory_usage_byte: 0,
        });

        Ok(())
    }

    fn time_overhead(&self) -> Second {
        self.shell_spawning_time.unwrap().time_real
    }
}

#[derive(Clone)]
pub struct MockExecutor {
    shell: Option<String>,
}

impl MockExecutor {
    pub fn new(shell: Option<String>) -> Self {
        MockExecutor { shell }
    }

    fn extract_time<S: AsRef<str>>(sleep_command: S) -> Second {
        assert!(sleep_command.as_ref().starts_with("sleep "));
        sleep_command
            .as_ref()
            .trim_start_matches("sleep ")
            .parse::<Second>()
            .unwrap()
    }
}

impl Executor for MockExecutor {
    fn run_command_and_measure(
        &self,
        command: &Command<'_>,
        _iteration: BenchmarkIteration,
        _command_failure_action: Option<CmdFailureAction>,
        _output_policy: &CommandOutputPolicy,
    ) -> Result<(TimingResult, ExitStatus)> {
        #[cfg(unix)]
        let status = {
            use std::os::unix::process::ExitStatusExt;
            ExitStatus::from_raw(0)
        };

        #[cfg(windows)]
        let status = {
            use std::os::windows::process::ExitStatusExt;
            ExitStatus::from_raw(0)
        };

        Ok((
            TimingResult {
                time_real: Self::extract_time(command.get_command_line()),
                time_user: 0.0,
                time_system: 0.0,
                memory_usage_byte: 0,
            },
            status,
        ))
    }

    fn calibrate(&mut self) -> Result<()> {
        Ok(())
    }

    fn time_overhead(&self) -> Second {
        match &self.shell {
            None => 0.0,
            Some(shell) => Self::extract_time(shell),
        }
    }
}

#[test]
fn test_mock_executor_extract_time() {
    assert_eq!(MockExecutor::extract_time("sleep 0.1"), 0.1);
}
```

## File: `src/benchmark/mod.rs`
```rust
pub mod benchmark_result;
pub mod executor;
pub mod relative_speed;
pub mod scheduler;
pub mod timing_result;

use std::cmp;

use crate::benchmark::executor::BenchmarkIteration;
use crate::command::Command;
use crate::options::{
    CmdFailureAction, CommandOutputPolicy, ExecutorKind, Options, OutputStyleOption,
};
use crate::outlier_detection::{modified_zscores, OUTLIER_THRESHOLD};
use crate::output::format::{format_duration, format_duration_unit};
use crate::output::progress_bar::get_progress_bar;
use crate::output::warnings::{OutlierWarningOptions, Warnings};
use crate::parameter::ParameterNameAndValue;
use crate::util::exit_code::extract_exit_code;
use crate::util::min_max::{max, min};
use crate::util::units::Second;
use benchmark_result::BenchmarkResult;
use timing_result::TimingResult;

use anyhow::{anyhow, Result};
use colored::*;
use statistical::{mean, median, standard_deviation};

use self::executor::Executor;

/// Threshold for warning about fast execution time
pub const MIN_EXECUTION_TIME: Second = 5e-3;

pub struct Benchmark<'a> {
    number: usize,
    command: &'a Command<'a>,
    options: &'a Options,
    executor: &'a dyn Executor,
}

impl<'a> Benchmark<'a> {
    pub fn new(
        number: usize,
        command: &'a Command<'a>,
        options: &'a Options,
        executor: &'a dyn Executor,
    ) -> Self {
        Benchmark {
            number,
            command,
            options,
            executor,
        }
    }

    /// Run setup, cleanup, or preparation commands
    fn run_intermediate_command(
        &self,
        command: &Command<'_>,
        error_output: &'static str,
        output_policy: &CommandOutputPolicy,
    ) -> Result<TimingResult> {
        self.executor
            .run_command_and_measure(
                command,
                executor::BenchmarkIteration::NonBenchmarkRun,
                Some(CmdFailureAction::RaiseError),
                output_policy,
            )
            .map(|r| r.0)
            .map_err(|_| anyhow!(error_output))
    }

    /// Run the command specified by `--setup`.
    fn run_setup_command(
        &self,
        parameters: impl IntoIterator<Item = ParameterNameAndValue<'a>>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<TimingResult> {
        let command = self
            .options
            .setup_command
            .as_ref()
            .map(|setup_command| Command::new_parametrized(None, setup_command, parameters));

        let error_output = "The setup command terminated with a non-zero exit code. \
                            Append ' || true' to the command if you are sure that this can be ignored.";

        Ok(command
            .map(|cmd| self.run_intermediate_command(&cmd, error_output, output_policy))
            .transpose()?
            .unwrap_or_default())
    }

    /// Run the command specified by `--cleanup`.
    fn run_cleanup_command(
        &self,
        parameters: impl IntoIterator<Item = ParameterNameAndValue<'a>>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<TimingResult> {
        let command = self
            .options
            .cleanup_command
            .as_ref()
            .map(|cleanup_command| Command::new_parametrized(None, cleanup_command, parameters));

        let error_output = "The cleanup command terminated with a non-zero exit code. \
                            Append ' || true' to the command if you are sure that this can be ignored.";

        Ok(command
            .map(|cmd| self.run_intermediate_command(&cmd, error_output, output_policy))
            .transpose()?
            .unwrap_or_default())
    }

    /// Run the command specified by `--prepare`.
    fn run_preparation_command(
        &self,
        command: &Command<'_>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<TimingResult> {
        let error_output = "The preparation command terminated with a non-zero exit code. \
                            Append ' || true' to the command if you are sure that this can be ignored.";

        self.run_intermediate_command(command, error_output, output_policy)
    }

    /// Run the command specified by `--conclude`.
    fn run_conclusion_command(
        &self,
        command: &Command<'_>,
        output_policy: &CommandOutputPolicy,
    ) -> Result<TimingResult> {
        let error_output = "The conclusion command terminated with a non-zero exit code. \
                            Append ' || true' to the command if you are sure that this can be ignored.";

        self.run_intermediate_command(command, error_output, output_policy)
    }

    /// Run the benchmark for a single command
    pub fn run(&self) -> Result<BenchmarkResult> {
        if self.options.output_style != OutputStyleOption::Disabled {
            println!(
                "{}{}: {}",
                "Benchmark ".bold(),
                (self.number + 1).to_string().bold(),
                self.command.get_name_with_unused_parameters(),
            );
        }

        let mut times_real: Vec<Second> = vec![];
        let mut times_user: Vec<Second> = vec![];
        let mut times_system: Vec<Second> = vec![];
        let mut memory_usage_byte: Vec<u64> = vec![];
        let mut exit_codes: Vec<Option<i32>> = vec![];
        let mut all_succeeded = true;

        let output_policy = &self.options.command_output_policies[self.number];

        let preparation_command = self.options.preparation_command.as_ref().map(|values| {
            let preparation_command = if values.len() == 1 {
                &values[0]
            } else {
                &values[self.number]
            };
            Command::new_parametrized(
                None,
                preparation_command,
                self.command.get_parameters().iter().cloned(),
            )
        });

        let run_preparation_command = || {
            preparation_command
                .as_ref()
                .map(|cmd| self.run_preparation_command(cmd, output_policy))
                .transpose()
        };

        let conclusion_command = self.options.conclusion_command.as_ref().map(|values| {
            let conclusion_command = if values.len() == 1 {
                &values[0]
            } else {
                &values[self.number]
            };
            Command::new_parametrized(
                None,
                conclusion_command,
                self.command.get_parameters().iter().cloned(),
            )
        });
        let run_conclusion_command = || {
            conclusion_command
                .as_ref()
                .map(|cmd| self.run_conclusion_command(cmd, output_policy))
                .transpose()
        };

        self.run_setup_command(self.command.get_parameters().iter().cloned(), output_policy)?;

        // Warmup phase
        if self.options.warmup_count > 0 {
            let progress_bar = if self.options.output_style != OutputStyleOption::Disabled {
                Some(get_progress_bar(
                    self.options.warmup_count,
                    "Performing warmup runs",
                    self.options.output_style,
                ))
            } else {
                None
            };

            for i in 0..self.options.warmup_count {
                let _ = run_preparation_command()?;
                let _ = self.executor.run_command_and_measure(
                    self.command,
                    BenchmarkIteration::Warmup(i),
                    None,
                    output_policy,
                )?;
                let _ = run_conclusion_command()?;
                if let Some(bar) = progress_bar.as_ref() {
                    bar.inc(1)
                }
            }
            if let Some(bar) = progress_bar.as_ref() {
                bar.finish_and_clear()
            }
        }

        // Set up progress bar (and spinner for initial measurement)
        let progress_bar = if self.options.output_style != OutputStyleOption::Disabled {
            Some(get_progress_bar(
                self.options.run_bounds.min,
                "Initial time measurement",
                self.options.output_style,
            ))
        } else {
            None
        };

        let preparation_result = run_preparation_command()?;
        let preparation_overhead =
            preparation_result.map_or(0.0, |res| res.time_real + self.executor.time_overhead());

        // Initial timing run
        let (res, status) = self.executor.run_command_and_measure(
            self.command,
            BenchmarkIteration::Benchmark(0),
            None,
            output_policy,
        )?;
        let success = status.success();

        let conclusion_result = run_conclusion_command()?;
        let conclusion_overhead =
            conclusion_result.map_or(0.0, |res| res.time_real + self.executor.time_overhead());

        // Determine number of benchmark runs
        let runs_in_min_time = (self.options.min_benchmarking_time
            / (res.time_real
                + self.executor.time_overhead()
                + preparation_overhead
                + conclusion_overhead)) as u64;

        let count = {
            let min = cmp::max(runs_in_min_time, self.options.run_bounds.min);

            self.options
                .run_bounds
                .max
                .as_ref()
                .map(|max| cmp::min(min, *max))
                .unwrap_or(min)
        };

        let count_remaining = count - 1;

        // Save the first result
        times_real.push(res.time_real);
        times_user.push(res.time_user);
        times_system.push(res.time_system);
        memory_usage_byte.push(res.memory_usage_byte);
        exit_codes.push(extract_exit_code(status));

        all_succeeded = all_succeeded && success;

        // Re-configure the progress bar
        if let Some(bar) = progress_bar.as_ref() {
            bar.set_length(count)
        }
        if let Some(bar) = progress_bar.as_ref() {
            bar.inc(1)
        }

        // Gather statistics (perform the actual benchmark)
        for i in 0..count_remaining {
            run_preparation_command()?;

            let msg = {
                let mean = format_duration(mean(&times_real), self.options.time_unit);
                format!("Current estimate: {}", mean.to_string().green())
            };

            if let Some(bar) = progress_bar.as_ref() {
                bar.set_message(msg.to_owned())
            }

            let (res, status) = self.executor.run_command_and_measure(
                self.command,
                BenchmarkIteration::Benchmark(i + 1),
                None,
                output_policy,
            )?;
            let success = status.success();

            times_real.push(res.time_real);
            times_user.push(res.time_user);
            times_system.push(res.time_system);
            memory_usage_byte.push(res.memory_usage_byte);
            exit_codes.push(extract_exit_code(status));

            all_succeeded = all_succeeded && success;

            if let Some(bar) = progress_bar.as_ref() {
                bar.inc(1)
            }

            run_conclusion_command()?;
        }

        if let Some(bar) = progress_bar.as_ref() {
            bar.finish_and_clear()
        }

        // Compute statistical quantities
        let t_num = times_real.len();
        let t_mean = mean(&times_real);
        let t_stddev = if times_real.len() > 1 {
            Some(standard_deviation(&times_real, Some(t_mean)))
        } else {
            None
        };
        let t_median = median(&times_real);
        let t_min = min(&times_real);
        let t_max = max(&times_real);

        let user_mean = mean(&times_user);
        let system_mean = mean(&times_system);

        // Formatting and console output
        let (mean_str, time_unit) = format_duration_unit(t_mean, self.options.time_unit);
        let min_str = format_duration(t_min, Some(time_unit));
        let max_str = format_duration(t_max, Some(time_unit));
        let num_str = format!("{t_num} runs");

        let user_str = format_duration(user_mean, Some(time_unit));
        let system_str = format_duration(system_mean, Some(time_unit));

        if self.options.output_style != OutputStyleOption::Disabled {
            if times_real.len() == 1 {
                println!(
                    "  Time ({} ≡):        {:>8}  {:>8}     [User: {}, System: {}]",
                    "abs".green().bold(),
                    mean_str.green().bold(),
                    "        ", // alignment
                    user_str.blue(),
                    system_str.blue()
                );
            } else {
                let stddev_str = format_duration(t_stddev.unwrap(), Some(time_unit));

                println!(
                    "  Time ({} ± {}):     {:>8} ± {:>8}    [User: {}, System: {}]",
                    "mean".green().bold(),
                    "σ".green(),
                    mean_str.green().bold(),
                    stddev_str.green(),
                    user_str.blue(),
                    system_str.blue()
                );

                println!(
                    "  Range ({} … {}):   {:>8} … {:>8}    {}",
                    "min".cyan(),
                    "max".purple(),
                    min_str.cyan(),
                    max_str.purple(),
                    num_str.dimmed()
                );
            }
        }

        // Warnings
        let mut warnings = vec![];

        // Check execution time
        if matches!(self.options.executor_kind, ExecutorKind::Shell(_))
            && times_real.iter().any(|&t| t < MIN_EXECUTION_TIME)
        {
            warnings.push(Warnings::FastExecutionTime);
        }

        // Check program exit codes
        if !all_succeeded {
            warnings.push(Warnings::NonZeroExitCode);
        }

        // Run outlier detection
        let scores = modified_zscores(&times_real);

        let outlier_warning_options = OutlierWarningOptions {
            warmup_in_use: self.options.warmup_count > 0,
            prepare_in_use: self
                .options
                .preparation_command
                .as_ref()
                .map(|v| v.len())
                .unwrap_or(0)
                > 0,
        };

        if scores[0] > OUTLIER_THRESHOLD {
            warnings.push(Warnings::SlowInitialRun(
                times_real[0],
                outlier_warning_options,
            ));
        } else if scores.iter().any(|&s| s.abs() > OUTLIER_THRESHOLD) {
            warnings.push(Warnings::OutliersDetected(outlier_warning_options));
        }

        if !warnings.is_empty() {
            eprintln!(" ");

            for warning in &warnings {
                eprintln!("  {}: {}", "Warning".yellow(), warning);
            }
        }

        if self.options.output_style != OutputStyleOption::Disabled {
            println!(" ");
        }

        self.run_cleanup_command(self.command.get_parameters().iter().cloned(), output_policy)?;

        Ok(BenchmarkResult {
            command: self.command.get_name(),
            command_with_unused_parameters: self.command.get_name_with_unused_parameters(),
            mean: t_mean,
            stddev: t_stddev,
            median: t_median,
            user: user_mean,
            system: system_mean,
            min: t_min,
            max: t_max,
            times: Some(times_real),
            memory_usage_byte: Some(memory_usage_byte),
            exit_codes,
            parameters: self
                .command
                .get_parameters()
                .iter()
                .map(|(name, value)| (name.to_string(), value.to_string()))
                .collect(),
        })
    }
}
```

## File: `src/benchmark/relative_speed.rs`
```rust
use std::cmp::Ordering;

use super::benchmark_result::BenchmarkResult;
use crate::{options::SortOrder, util::units::Scalar};

#[derive(Debug)]
pub struct BenchmarkResultWithRelativeSpeed<'a> {
    pub result: &'a BenchmarkResult,
    pub relative_speed: Scalar,
    pub relative_speed_stddev: Option<Scalar>,
    pub is_reference: bool,
    // Less means faster
    pub relative_ordering: Ordering,
}

pub fn compare_mean_time(l: &BenchmarkResult, r: &BenchmarkResult) -> Ordering {
    l.mean.partial_cmp(&r.mean).unwrap_or(Ordering::Equal)
}

pub fn fastest_of(results: &[BenchmarkResult]) -> &BenchmarkResult {
    results
        .iter()
        .min_by(|&l, &r| compare_mean_time(l, r))
        .expect("at least one benchmark result")
}

fn compute_relative_speeds<'a>(
    results: &'a [BenchmarkResult],
    reference: &'a BenchmarkResult,
    sort_order: SortOrder,
) -> Vec<BenchmarkResultWithRelativeSpeed<'a>> {
    let mut results: Vec<_> = results
        .iter()
        .map(|result| {
            let is_reference = result == reference;
            let relative_ordering = compare_mean_time(result, reference);

            if result.mean == 0.0 {
                return BenchmarkResultWithRelativeSpeed {
                    result,
                    relative_speed: if is_reference { 1.0 } else { f64::INFINITY },
                    relative_speed_stddev: None,
                    is_reference,
                    relative_ordering,
                };
            }

            let ratio = match relative_ordering {
                Ordering::Less => reference.mean / result.mean,
                Ordering::Equal => 1.0,
                Ordering::Greater => result.mean / reference.mean,
            };

            // https://en.wikipedia.org/wiki/Propagation_of_uncertainty#Example_formulas
            // Covariance asssumed to be 0, i.e. variables are assumed to be independent
            let ratio_stddev = match (result.stddev, reference.stddev) {
                (Some(result_stddev), Some(fastest_stddev)) => Some(
                    ratio
                        * ((result_stddev / result.mean).powi(2)
                            + (fastest_stddev / reference.mean).powi(2))
                        .sqrt(),
                ),
                _ => None,
            };

            BenchmarkResultWithRelativeSpeed {
                result,
                relative_speed: ratio,
                relative_speed_stddev: ratio_stddev,
                is_reference,
                relative_ordering,
            }
        })
        .collect();

    match sort_order {
        SortOrder::Command => {}
        SortOrder::MeanTime => {
            results.sort_unstable_by(|r1, r2| compare_mean_time(r1.result, r2.result));
        }
    }

    results
}

pub fn compute_with_check_from_reference<'a>(
    results: &'a [BenchmarkResult],
    reference: &'a BenchmarkResult,
    sort_order: SortOrder,
) -> Option<Vec<BenchmarkResultWithRelativeSpeed<'a>>> {
    if fastest_of(results).mean == 0.0 || reference.mean == 0.0 {
        return None;
    }

    Some(compute_relative_speeds(results, reference, sort_order))
}

pub fn compute_with_check(
    results: &[BenchmarkResult],
    sort_order: SortOrder,
) -> Option<Vec<BenchmarkResultWithRelativeSpeed<'_>>> {
    let fastest = fastest_of(results);

    if fastest.mean == 0.0 {
        return None;
    }

    Some(compute_relative_speeds(results, fastest, sort_order))
}

/// Same as compute_with_check, potentially resulting in relative speeds of infinity
pub fn compute(
    results: &[BenchmarkResult],
    sort_order: SortOrder,
) -> Vec<BenchmarkResultWithRelativeSpeed<'_>> {
    let fastest = fastest_of(results);

    compute_relative_speeds(results, fastest, sort_order)
}

#[cfg(test)]
fn create_result(name: &str, mean: Scalar) -> BenchmarkResult {
    use std::collections::BTreeMap;

    BenchmarkResult {
        command: name.into(),
        command_with_unused_parameters: name.into(),
        mean,
        stddev: Some(1.0),
        median: mean,
        user: mean,
        system: 0.0,
        min: mean,
        max: mean,
        times: None,
        memory_usage_byte: None,
        exit_codes: Vec::new(),
        parameters: BTreeMap::new(),
    }
}

#[test]
fn test_compute_relative_speed() {
    use approx::assert_relative_eq;

    let results = vec![
        create_result("cmd1", 3.0),
        create_result("cmd2", 2.0),
        create_result("cmd3", 5.0),
    ];

    let annotated_results = compute_with_check(&results, SortOrder::Command).unwrap();

    assert_relative_eq!(1.5, annotated_results[0].relative_speed);
    assert_relative_eq!(1.0, annotated_results[1].relative_speed);
    assert_relative_eq!(2.5, annotated_results[2].relative_speed);
}

#[test]
fn test_compute_relative_speed_with_reference() {
    use approx::assert_relative_eq;

    let results = vec![create_result("cmd2", 2.0), create_result("cmd3", 5.0)];
    let reference = create_result("cmd2", 4.0);

    let annotated_results =
        compute_with_check_from_reference(&results, &reference, SortOrder::Command).unwrap();

    assert_relative_eq!(2.0, annotated_results[0].relative_speed);
    assert_relative_eq!(1.25, annotated_results[1].relative_speed);
}

#[test]
fn test_compute_relative_speed_for_zero_times() {
    let results = vec![create_result("cmd1", 1.0), create_result("cmd2", 0.0)];

    let annotated_results = compute_with_check(&results, SortOrder::Command);

    assert!(annotated_results.is_none());
}
```

## File: `src/benchmark/scheduler.rs`
```rust
use super::benchmark_result::BenchmarkResult;
use super::executor::{Executor, MockExecutor, RawExecutor, ShellExecutor};
use super::{relative_speed, Benchmark};
use colored::*;
use std::cmp::Ordering;

use crate::command::{Command, Commands};
use crate::export::ExportManager;
use crate::options::{ExecutorKind, Options, OutputStyleOption, SortOrder};

use anyhow::Result;

pub struct Scheduler<'a> {
    commands: &'a Commands<'a>,
    options: &'a Options,
    export_manager: &'a ExportManager,
    results: Vec<BenchmarkResult>,
}

impl<'a> Scheduler<'a> {
    pub fn new(
        commands: &'a Commands,
        options: &'a Options,
        export_manager: &'a ExportManager,
    ) -> Self {
        Self {
            commands,
            options,
            export_manager,
            results: vec![],
        }
    }

    pub fn run_benchmarks(&mut self) -> Result<()> {
        let mut executor: Box<dyn Executor> = match self.options.executor_kind {
            ExecutorKind::Raw => Box::new(RawExecutor::new(self.options)),
            ExecutorKind::Mock(ref shell) => Box::new(MockExecutor::new(shell.clone())),
            ExecutorKind::Shell(ref shell) => Box::new(ShellExecutor::new(shell, self.options)),
        };

        let reference = self
            .options
            .reference_command
            .as_ref()
            .map(|cmd| Command::new(self.options.reference_name.as_deref(), cmd));

        executor.calibrate()?;

        for (number, cmd) in reference.iter().chain(self.commands.iter()).enumerate() {
            self.results
                .push(Benchmark::new(number, cmd, self.options, &*executor).run()?);

            // We export results after each individual benchmark, because
            // we would risk losing them if a later benchmark fails.
            self.export_manager.write_results(&self.results, true)?;
        }

        Ok(())
    }

    pub fn print_relative_speed_comparison(&self) {
        if self.options.output_style == OutputStyleOption::Disabled {
            return;
        }

        if self.results.len() < 2 {
            return;
        }

        let reference = self
            .options
            .reference_command
            .as_ref()
            .map(|_| &self.results[0])
            .unwrap_or_else(|| relative_speed::fastest_of(&self.results));

        if let Some(annotated_results) = relative_speed::compute_with_check_from_reference(
            &self.results,
            reference,
            self.options.sort_order_speed_comparison,
        ) {
            match self.options.sort_order_speed_comparison {
                SortOrder::MeanTime => {
                    println!("{}", "Summary".bold());

                    let reference = annotated_results.iter().find(|r| r.is_reference).unwrap();
                    let others = annotated_results.iter().filter(|r| !r.is_reference);

                    println!(
                        "  {} ran",
                        reference.result.command_with_unused_parameters.cyan()
                    );

                    for item in others {
                        let stddev = if let Some(stddev) = item.relative_speed_stddev {
                            format!(" ± {}", format!("{:.2}", stddev).green())
                        } else {
                            "".into()
                        };
                        let comparator = match item.relative_ordering {
                            Ordering::Less => format!(
                                "{}{} times slower than",
                                format!("{:8.2}", item.relative_speed).bold().green(),
                                stddev
                            ),
                            Ordering::Greater => format!(
                                "{}{} times faster than",
                                format!("{:8.2}", item.relative_speed).bold().green(),
                                stddev
                            ),
                            Ordering::Equal => format!(
                                "    As fast ({}{}) as",
                                format!("{:.2}", item.relative_speed).bold().green(),
                                stddev
                            ),
                        };
                        println!(
                            "{} {}",
                            comparator,
                            &item.result.command_with_unused_parameters.magenta()
                        );
                    }
                }
                SortOrder::Command => {
                    println!("{}", "Relative speed comparison".bold());

                    for item in annotated_results {
                        println!(
                            "  {}{}  {}",
                            format!("{:10.2}", item.relative_speed).bold().green(),
                            if item.is_reference {
                                "        ".into()
                            } else if let Some(stddev) = item.relative_speed_stddev {
                                format!(" ± {}", format!("{stddev:5.2}").green())
                            } else {
                                "        ".into()
                            },
                            &item.result.command_with_unused_parameters,
                        );
                    }
                }
            }
        } else {
            eprintln!(
                "{}: The benchmark comparison could not be computed as some benchmark times are zero. \
                 This could be caused by background interference during the initial calibration phase \
                 of hyperfine, in combination with very fast commands (faster than a few milliseconds). \
                 Try to re-run the benchmark on a quiet system. If you did not do so already, try the \
                 --shell=none/-N option. If it does not help either, you command is most likely too fast \
                 to be accurately benchmarked by hyperfine.",
                 "Note".bold().red()
            );
        }
    }

    pub fn final_export(&self) -> Result<()> {
        self.export_manager.write_results(&self.results, false)
    }
}

#[cfg(test)]
fn generate_results(args: &[&'static str]) -> Result<Vec<BenchmarkResult>> {
    use crate::cli::get_cli_arguments;

    let args = ["hyperfine", "--debug-mode", "--style=none"]
        .iter()
        .chain(args);
    let cli_arguments = get_cli_arguments(args);
    let mut options = Options::from_cli_arguments(&cli_arguments)?;

    assert_eq!(options.executor_kind, ExecutorKind::Mock(None));

    let commands = Commands::from_cli_arguments(&cli_arguments)?;
    let export_manager = ExportManager::from_cli_arguments(
        &cli_arguments,
        options.time_unit,
        options.sort_order_exports,
    )?;

    options.validate_against_command_list(&commands)?;

    let mut scheduler = Scheduler::new(&commands, &options, &export_manager);

    scheduler.run_benchmarks()?;
    Ok(scheduler.results)
}

#[test]
fn scheduler_basic() -> Result<()> {
    insta::assert_yaml_snapshot!(generate_results(&["--runs=2", "sleep 0.123", "sleep 0.456"])?, @r#"
    - command: sleep 0.123
      mean: 0.123
      stddev: 0
      median: 0.123
      user: 0
      system: 0
      min: 0.123
      max: 0.123
      times:
        - 0.123
        - 0.123
      memory_usage_byte:
        - 0
        - 0
      exit_codes:
        - 0
        - 0
    - command: sleep 0.456
      mean: 0.456
      stddev: 0
      median: 0.456
      user: 0
      system: 0
      min: 0.456
      max: 0.456
      times:
        - 0.456
        - 0.456
      memory_usage_byte:
        - 0
        - 0
      exit_codes:
        - 0
        - 0
    "#);

    Ok(())
}
```

## File: `src/benchmark/timing_result.rs`
```rust
use crate::util::units::Second;

/// Results from timing a single command
#[derive(Debug, Default, Copy, Clone)]
pub struct TimingResult {
    /// Wall clock time
    pub time_real: Second,

    /// Time spent in user mode
    pub time_user: Second,

    /// Time spent in kernel mode
    pub time_system: Second,

    /// Maximum amount of memory used, in bytes
    pub memory_usage_byte: u64,
}
```

## File: `src/export/asciidoc.rs`
```rust
use super::markup::Alignment;
use crate::export::markup::MarkupExporter;

#[derive(Default)]
pub struct AsciidocExporter {}

impl MarkupExporter for AsciidocExporter {
    fn table_header(&self, cell_aligmnents: &[Alignment]) -> String {
        format!(
            "[cols=\"{}\"]\n|===",
            cell_aligmnents
                .iter()
                .map(|a| match a {
                    Alignment::Left => "<",
                    Alignment::Right => ">",
                })
                .collect::<Vec<&str>>()
                .join(",")
        )
    }

    fn table_footer(&self, _cell_aligmnents: &[Alignment]) -> String {
        "|===\n".to_string()
    }

    fn table_row(&self, cells: &[&str]) -> String {
        format!("\n| {} \n", cells.join(" \n| "))
    }

    fn table_divider(&self, _cell_aligmnents: &[Alignment]) -> String {
        "".to_string()
    }

    fn command(&self, cmd: &str) -> String {
        format!("`{cmd}`")
    }
}

/// Check Asciidoc-based data row formatting
#[test]
fn test_asciidoc_exporter_table_data() {
    let exporter = AsciidocExporter::default();
    let data = vec!["a", "b", "c"];

    let actual = exporter.table_row(&data);
    let expect = "\n| a \n| b \n| c \n";

    assert_eq!(expect, actual);
}

/// Check Asciidoc-based table header formatting
#[test]
fn test_asciidoc_exporter_table_header() {
    let exporter = AsciidocExporter::default();
    let cells_alignment = [
        Alignment::Left,
        Alignment::Right,
        Alignment::Right,
        Alignment::Right,
        Alignment::Right,
    ];

    let actual = exporter.table_header(&cells_alignment);
    let expect = "[cols=\"<,>,>,>,>\"]\n|===";

    assert_eq!(expect, actual);
}
```

## File: `src/export/csv.rs`
```rust
use std::borrow::Cow;

use csv::WriterBuilder;

use super::Exporter;
use crate::benchmark::benchmark_result::BenchmarkResult;
use crate::options::SortOrder;
use crate::util::units::Unit;

use anyhow::Result;

#[derive(Default)]
pub struct CsvExporter {}

impl Exporter for CsvExporter {
    fn serialize(
        &self,
        results: &[BenchmarkResult],
        _unit: Option<Unit>,
        _sort_order: SortOrder,
    ) -> Result<Vec<u8>> {
        let mut writer = WriterBuilder::new().from_writer(vec![]);

        {
            let mut headers: Vec<Cow<[u8]>> = [
                // The list of times and exit codes cannot be exported to the CSV file - omit them.
                "command", "mean", "stddev", "median", "user", "system", "min", "max",
            ]
            .iter()
            .map(|x| Cow::Borrowed(x.as_bytes()))
            .collect();
            if let Some(res) = results.first() {
                for param_name in res.parameters.keys() {
                    headers.push(Cow::Owned(format!("parameter_{param_name}").into_bytes()));
                }
            }
            writer.write_record(headers)?;
        }

        for res in results {
            let mut fields = vec![Cow::Borrowed(res.command.as_bytes())];
            for f in &[
                res.mean,
                res.stddev.unwrap_or(0.0),
                res.median,
                res.user,
                res.system,
                res.min,
                res.max,
            ] {
                fields.push(Cow::Owned(f.to_string().into_bytes()))
            }
            for v in res.parameters.values() {
                fields.push(Cow::Borrowed(v.as_bytes()))
            }
            writer.write_record(fields)?;
        }

        Ok(writer.into_inner()?)
    }
}

#[test]
fn test_csv() {
    use std::collections::BTreeMap;
    let exporter = CsvExporter::default();

    let results = vec![
        BenchmarkResult {
            command: String::from("command_a"),
            command_with_unused_parameters: String::from("command_a"),
            mean: 1.0,
            stddev: Some(2.0),
            median: 1.0,
            user: 3.0,
            system: 4.0,
            min: 5.0,
            max: 6.0,
            times: Some(vec![7.0, 8.0, 9.0]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: {
                let mut params = BTreeMap::new();
                params.insert("foo".into(), "one".into());
                params.insert("bar".into(), "two".into());
                params
            },
        },
        BenchmarkResult {
            command: String::from("command_b"),
            command_with_unused_parameters: String::from("command_b"),
            mean: 11.0,
            stddev: Some(12.0),
            median: 11.0,
            user: 13.0,
            system: 14.0,
            min: 15.0,
            max: 16.5,
            times: Some(vec![17.0, 18.0, 19.0]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: {
                let mut params = BTreeMap::new();
                params.insert("foo".into(), "one".into());
                params.insert("bar".into(), "seven".into());
                params
            },
        },
    ];

    let actual = String::from_utf8(
        exporter
            .serialize(&results, Some(Unit::Second), SortOrder::Command)
            .unwrap(),
    )
    .unwrap();

    insta::assert_snapshot!(actual, @r#"
    command,mean,stddev,median,user,system,min,max,parameter_bar,parameter_foo
    command_a,1,2,1,3,4,5,6,two,one
    command_b,11,12,11,13,14,15,16.5,seven,one
    "#);
}
```

## File: `src/export/json.rs`
```rust
use serde::*;
use serde_json::to_vec_pretty;

use super::Exporter;
use crate::benchmark::benchmark_result::BenchmarkResult;
use crate::options::SortOrder;
use crate::util::units::Unit;

use anyhow::Result;

#[derive(Serialize, Debug)]
struct HyperfineSummary<'a> {
    results: &'a [BenchmarkResult],
}

#[derive(Default)]
pub struct JsonExporter {}

impl Exporter for JsonExporter {
    fn serialize(
        &self,
        results: &[BenchmarkResult],
        _unit: Option<Unit>,
        _sort_order: SortOrder,
    ) -> Result<Vec<u8>> {
        let mut output = to_vec_pretty(&HyperfineSummary { results });
        if let Ok(ref mut content) = output {
            content.push(b'\n');
        }

        Ok(output?)
    }
}
```

## File: `src/export/markdown.rs`
```rust
use crate::export::markup::MarkupExporter;

use super::markup::Alignment;

#[derive(Default)]
pub struct MarkdownExporter {}

impl MarkupExporter for MarkdownExporter {
    fn table_row(&self, cells: &[&str]) -> String {
        format!("| {} |\n", cells.join(" | "))
    }

    fn table_divider(&self, cell_aligmnents: &[Alignment]) -> String {
        format!(
            "|{}\n",
            cell_aligmnents
                .iter()
                .map(|a| match a {
                    Alignment::Left => ":---|",
                    Alignment::Right => "---:|",
                })
                .collect::<String>()
        )
    }

    fn command(&self, cmd: &str) -> String {
        format!("`{cmd}`")
    }
}

/// Check Markdown-based data row formatting
#[test]
fn test_markdown_formatter_table_data() {
    let formatter = MarkdownExporter::default();

    assert_eq!(formatter.table_row(&["a", "b", "c"]), "| a | b | c |\n");
}

/// Check Markdown-based horizontal line formatting
#[test]
fn test_markdown_formatter_table_divider() {
    let formatter = MarkdownExporter::default();

    let divider = formatter.table_divider(&[Alignment::Left, Alignment::Right, Alignment::Left]);
    assert_eq!(divider, "|:---|---:|:---|\n");
}
```

## File: `src/export/markup.rs`
```rust
use crate::benchmark::relative_speed::BenchmarkResultWithRelativeSpeed;
use crate::benchmark::{benchmark_result::BenchmarkResult, relative_speed};
use crate::options::SortOrder;
use crate::output::format::format_duration_value;
use crate::util::units::Unit;

use super::Exporter;
use anyhow::Result;

pub enum Alignment {
    Left,
    Right,
}

pub trait MarkupExporter {
    fn table_results(&self, entries: &[BenchmarkResultWithRelativeSpeed], unit: Unit) -> String {
        // prepare table header strings
        let notation = format!("[{}]", unit.short_name());

        // prepare table cells alignment
        let cells_alignment = [
            Alignment::Left,
            Alignment::Right,
            Alignment::Right,
            Alignment::Right,
            Alignment::Right,
        ];

        // emit table header format
        let mut table = self.table_header(&cells_alignment);

        // emit table header data
        table.push_str(&self.table_row(&[
            "Command",
            &format!("Mean {notation}"),
            &format!("Min {notation}"),
            &format!("Max {notation}"),
            "Relative",
        ]));

        // emit horizontal line
        table.push_str(&self.table_divider(&cells_alignment));

        for entry in entries {
            let measurement = &entry.result;
            // prepare data row strings
            let cmd_str = measurement
                .command_with_unused_parameters
                .replace('|', "\\|");
            let mean_str = format_duration_value(measurement.mean, Some(unit)).0;
            let stddev_str = if let Some(stddev) = measurement.stddev {
                format!(" ± {}", format_duration_value(stddev, Some(unit)).0)
            } else {
                "".into()
            };
            let min_str = format_duration_value(measurement.min, Some(unit)).0;
            let max_str = format_duration_value(measurement.max, Some(unit)).0;
            let rel_str = format!("{:.2}", entry.relative_speed);
            let rel_stddev_str = if entry.is_reference {
                "".into()
            } else if let Some(stddev) = entry.relative_speed_stddev {
                format!(" ± {stddev:.2}")
            } else {
                "".into()
            };

            // prepare table row entries
            table.push_str(&self.table_row(&[
                &self.command(&cmd_str),
                &format!("{mean_str}{stddev_str}"),
                &min_str,
                &max_str,
                &format!("{rel_str}{rel_stddev_str}"),
            ]))
        }

        // emit table footer format
        table.push_str(&self.table_footer(&cells_alignment));

        table
    }

    fn table_row(&self, cells: &[&str]) -> String;

    fn table_divider(&self, cell_aligmnents: &[Alignment]) -> String;

    fn table_header(&self, _cell_aligmnents: &[Alignment]) -> String {
        "".to_string()
    }

    fn table_footer(&self, _cell_aligmnents: &[Alignment]) -> String {
        "".to_string()
    }

    fn command(&self, size: &str) -> String;
}

fn determine_unit_from_results(results: &[BenchmarkResult]) -> Unit {
    if let Some(first_result) = results.first() {
        // Use the first BenchmarkResult entry to determine the unit for all entries.
        format_duration_value(first_result.mean, None).1
    } else {
        // Default to `Second`.
        Unit::Second
    }
}

impl<T: MarkupExporter> Exporter for T {
    fn serialize(
        &self,
        results: &[BenchmarkResult],
        unit: Option<Unit>,
        sort_order: SortOrder,
    ) -> Result<Vec<u8>> {
        let unit = unit.unwrap_or_else(|| determine_unit_from_results(results));
        let entries = relative_speed::compute(results, sort_order);

        let table = self.table_results(&entries, unit);
        Ok(table.as_bytes().to_vec())
    }
}
```

## File: `src/export/mod.rs`
```rust
use std::fs::{File, OpenOptions};
use std::io::Write;

mod asciidoc;
mod csv;
mod json;
mod markdown;
mod markup;
mod orgmode;
#[cfg(test)]
mod tests;

use self::asciidoc::AsciidocExporter;
use self::csv::CsvExporter;
use self::json::JsonExporter;
use self::markdown::MarkdownExporter;
use self::orgmode::OrgmodeExporter;

use crate::benchmark::benchmark_result::BenchmarkResult;
use crate::options::SortOrder;
use crate::util::units::Unit;

use anyhow::{Context, Result};
use clap::ArgMatches;

/// The desired form of exporter to use for a given file.
#[derive(Clone)]
pub enum ExportType {
    /// Asciidoc Table
    Asciidoc,

    /// CSV (comma separated values) format
    Csv,

    /// JSON format
    Json,

    /// Markdown table
    Markdown,

    /// Emacs org-mode tables
    Orgmode,
}

/// Interface for different exporters.
trait Exporter {
    /// Export the given entries in the serialized form.
    fn serialize(
        &self,
        results: &[BenchmarkResult],
        unit: Option<Unit>,
        sort_order: SortOrder,
    ) -> Result<Vec<u8>>;
}

pub enum ExportTarget {
    File(String),
    Stdout,
}

struct ExporterWithTarget {
    exporter: Box<dyn Exporter>,
    target: ExportTarget,
}

/// Handles the management of multiple file exporters.
pub struct ExportManager {
    exporters: Vec<ExporterWithTarget>,
    time_unit: Option<Unit>,
    sort_order: SortOrder,
}

impl ExportManager {
    /// Build the ExportManager that will export the results specified
    /// in the given ArgMatches
    pub fn from_cli_arguments(
        matches: &ArgMatches,
        time_unit: Option<Unit>,
        sort_order: SortOrder,
    ) -> Result<Self> {
        let mut export_manager = Self {
            exporters: vec![],
            time_unit,
            sort_order,
        };
        {
            let mut add_exporter = |flag, exporttype| -> Result<()> {
                if let Some(filename) = matches.get_one::<String>(flag) {
                    export_manager.add_exporter(exporttype, filename)?;
                }
                Ok(())
            };
            add_exporter("export-asciidoc", ExportType::Asciidoc)?;
            add_exporter("export-json", ExportType::Json)?;
            add_exporter("export-csv", ExportType::Csv)?;
            add_exporter("export-markdown", ExportType::Markdown)?;
            add_exporter("export-orgmode", ExportType::Orgmode)?;
        }
        Ok(export_manager)
    }

    /// Add an additional exporter to the ExportManager
    pub fn add_exporter(&mut self, export_type: ExportType, filename: &str) -> Result<()> {
        let exporter: Box<dyn Exporter> = match export_type {
            ExportType::Asciidoc => Box::<AsciidocExporter>::default(),
            ExportType::Csv => Box::<CsvExporter>::default(),
            ExportType::Json => Box::<JsonExporter>::default(),
            ExportType::Markdown => Box::<MarkdownExporter>::default(),
            ExportType::Orgmode => Box::<OrgmodeExporter>::default(),
        };

        self.exporters.push(ExporterWithTarget {
            exporter,
            target: if filename == "-" {
                ExportTarget::Stdout
            } else {
                let _ = File::create(filename)
                    .with_context(|| format!("Could not create export file '{filename}'"))?;
                ExportTarget::File(filename.to_string())
            },
        });

        Ok(())
    }

    /// Write the given results to all Exporters. The 'intermediate' flag specifies
    /// whether this is being called while still performing benchmarks, or if this
    /// is the final call after all benchmarks have been finished. In the former case,
    /// results are written to all file targets (to always have them up to date, even
    /// if a benchmark fails). In the latter case, we only print to stdout targets (in
    /// order not to clutter the output of hyperfine with intermediate results).
    pub fn write_results(&self, results: &[BenchmarkResult], intermediate: bool) -> Result<()> {
        for e in &self.exporters {
            let content = || {
                e.exporter
                    .serialize(results, self.time_unit, self.sort_order)
            };

            match e.target {
                ExportTarget::File(ref filename) => {
                    if intermediate {
                        write_to_file(filename, &content()?)?
                    }
                }
                ExportTarget::Stdout => {
                    if !intermediate {
                        println!();
                        println!("{}", String::from_utf8(content()?).unwrap());
                    }
                }
            }
        }
        Ok(())
    }
}

/// Write the given content to a file with the specified name
fn write_to_file(filename: &str, content: &[u8]) -> Result<()> {
    let mut file = OpenOptions::new().write(true).open(filename)?;
    file.write_all(content)
        .with_context(|| format!("Failed to export results to '{filename}'"))
}
```

## File: `src/export/orgmode.rs`
```rust
use super::markup::Alignment;
use crate::export::markup::MarkupExporter;

#[derive(Default)]
pub struct OrgmodeExporter {}

impl MarkupExporter for OrgmodeExporter {
    fn table_row(&self, cells: &[&str]) -> String {
        format!(
            "| {}  |  {} |\n",
            cells.first().unwrap(),
            &cells[1..].join(" |  ")
        )
    }

    fn table_divider(&self, cell_aligmnents: &[Alignment]) -> String {
        format!("|{}--|\n", "--+".repeat(cell_aligmnents.len() - 1))
    }

    fn command(&self, cmd: &str) -> String {
        format!("={cmd}=")
    }
}

/// Check Emacs org-mode data row formatting
#[test]
fn test_orgmode_formatter_table_data() {
    let exporter = OrgmodeExporter::default();

    let actual = exporter.table_row(&["a", "b", "c"]);
    let expect = "| a  |  b |  c |\n";

    assert_eq!(expect, actual);
}

/// Check Emacs org-mode horizontal line formatting
#[test]
fn test_orgmode_formatter_table_line() {
    let exporter = OrgmodeExporter::default();

    let actual = exporter.table_divider(&[
        Alignment::Left,
        Alignment::Left,
        Alignment::Left,
        Alignment::Left,
        Alignment::Left,
    ]);
    let expect = "|--+--+--+--+--|\n";

    assert_eq!(expect, actual);
}
```

## File: `src/export/tests.rs`
```rust
use super::Exporter;
use crate::benchmark::benchmark_result::BenchmarkResult;
use crate::export::asciidoc::AsciidocExporter;
use crate::export::orgmode::OrgmodeExporter;
use crate::util::units::Unit;
use crate::{export::markdown::MarkdownExporter, options::SortOrder};
use std::collections::BTreeMap;

fn get_output<E: Exporter + Default>(
    results: &[BenchmarkResult],
    unit: Option<Unit>,
    sort_order: SortOrder,
) -> String {
    let exporter = E::default();
    String::from_utf8(exporter.serialize(results, unit, sort_order).unwrap()).unwrap()
}

/// Ensure the makrup output includes the table header and the multiple
/// benchmark results as a table. The list of actual times is not included
/// in the output.
///
/// This also demonstrates that the first entry's units (ms) are used to set
/// the units for all entries when the time unit is not specified.
#[test]
fn test_markup_export_auto_ms() {
    let results = [
        BenchmarkResult {
            command: String::from("sleep 0.1"),
            command_with_unused_parameters: String::from("sleep 0.1"),
            mean: 0.1057,
            stddev: Some(0.0016),
            median: 0.1057,
            user: 0.0009,
            system: 0.0011,
            min: 0.1023,
            max: 0.1080,
            times: Some(vec![0.1, 0.1, 0.1]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
        BenchmarkResult {
            command: String::from("sleep 2"),
            command_with_unused_parameters: String::from("sleep 2"),
            mean: 2.0050,
            stddev: Some(0.0020),
            median: 2.0050,
            user: 0.0009,
            system: 0.0012,
            min: 2.0020,
            max: 2.0080,
            times: Some(vec![2.0, 2.0, 2.0]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
    ];

    insta::assert_snapshot!(get_output::<MarkdownExporter>(&results, None, SortOrder::Command), @r#"
    | Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
    |:---|---:|---:|---:|---:|
    | `sleep 0.1` | 105.7 ± 1.6 | 102.3 | 108.0 | 1.00 |
    | `sleep 2` | 2005.0 ± 2.0 | 2002.0 | 2008.0 | 18.97 ± 0.29 |
    "#);

    insta::assert_snapshot!(get_output::<AsciidocExporter>(&results, None, SortOrder::Command), @r#"
    [cols="<,>,>,>,>"]
    |===
    | Command 
    | Mean [ms] 
    | Min [ms] 
    | Max [ms] 
    | Relative 

    | `sleep 0.1` 
    | 105.7 ± 1.6 
    | 102.3 
    | 108.0 
    | 1.00 

    | `sleep 2` 
    | 2005.0 ± 2.0 
    | 2002.0 
    | 2008.0 
    | 18.97 ± 0.29 
    |===
    "#);

    insta::assert_snapshot!(get_output::<OrgmodeExporter>(&results, None, SortOrder::Command), @r#"
    | Command  |  Mean [ms] |  Min [ms] |  Max [ms] |  Relative |
    |--+--+--+--+--|
    | =sleep 0.1=  |  105.7 ± 1.6 |  102.3 |  108.0 |  1.00 |
    | =sleep 2=  |  2005.0 ± 2.0 |  2002.0 |  2008.0 |  18.97 ± 0.29 |
    "#);
}

/// This (again) demonstrates that the first entry's units (s) are used to set
/// the units for all entries when the time unit is not given.
#[test]
fn test_markup_export_auto_s() {
    let results = [
        BenchmarkResult {
            command: String::from("sleep 2"),
            command_with_unused_parameters: String::from("sleep 2"),
            mean: 2.0050,
            stddev: Some(0.0020),
            median: 2.0050,
            user: 0.0009,
            system: 0.0012,
            min: 2.0020,
            max: 2.0080,
            times: Some(vec![2.0, 2.0, 2.0]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
        BenchmarkResult {
            command: String::from("sleep 0.1"),
            command_with_unused_parameters: String::from("sleep 0.1"),
            mean: 0.1057,
            stddev: Some(0.0016),
            median: 0.1057,
            user: 0.0009,
            system: 0.0011,
            min: 0.1023,
            max: 0.1080,
            times: Some(vec![0.1, 0.1, 0.1]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
    ];

    insta::assert_snapshot!(get_output::<MarkdownExporter>(&results, None, SortOrder::Command), @r#"
    | Command | Mean [s] | Min [s] | Max [s] | Relative |
    |:---|---:|---:|---:|---:|
    | `sleep 2` | 2.005 ± 0.002 | 2.002 | 2.008 | 18.97 ± 0.29 |
    | `sleep 0.1` | 0.106 ± 0.002 | 0.102 | 0.108 | 1.00 |
    "#);

    insta::assert_snapshot!(get_output::<AsciidocExporter>(&results, None, SortOrder::Command), @r#"
    [cols="<,>,>,>,>"]
    |===
    | Command 
    | Mean [s] 
    | Min [s] 
    | Max [s] 
    | Relative 

    | `sleep 2` 
    | 2.005 ± 0.002 
    | 2.002 
    | 2.008 
    | 18.97 ± 0.29 

    | `sleep 0.1` 
    | 0.106 ± 0.002 
    | 0.102 
    | 0.108 
    | 1.00 
    |===
    "#);

    insta::assert_snapshot!(get_output::<OrgmodeExporter>(&results, None, SortOrder::Command), @r#"
    | Command  |  Mean [s] |  Min [s] |  Max [s] |  Relative |
    |--+--+--+--+--|
    | =sleep 2=  |  2.005 ± 0.002 |  2.002 |  2.008 |  18.97 ± 0.29 |
    | =sleep 0.1=  |  0.106 ± 0.002 |  0.102 |  0.108 |  1.00 |
    "#);
}

/// This (again) demonstrates that the given time unit (ms) is used to set
/// the units for all entries.
#[test]
fn test_markup_export_manual_ms() {
    let timing_results = [
        BenchmarkResult {
            command: String::from("sleep 2"),
            command_with_unused_parameters: String::from("sleep 2"),
            mean: 2.0050,
            stddev: Some(0.0020),
            median: 2.0050,
            user: 0.0009,
            system: 0.0012,
            min: 2.0020,
            max: 2.0080,
            times: Some(vec![2.0, 2.0, 2.0]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
        BenchmarkResult {
            command: String::from("sleep 0.1"),
            command_with_unused_parameters: String::from("sleep 0.1"),
            mean: 0.1057,
            stddev: Some(0.0016),
            median: 0.1057,
            user: 0.0009,
            system: 0.0011,
            min: 0.1023,
            max: 0.1080,
            times: Some(vec![0.1, 0.1, 0.1]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
    ];

    insta::assert_snapshot!(get_output::<MarkdownExporter>(&timing_results, Some(Unit::MilliSecond), SortOrder::Command), @r#"
    | Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
    |:---|---:|---:|---:|---:|
    | `sleep 2` | 2005.0 ± 2.0 | 2002.0 | 2008.0 | 18.97 ± 0.29 |
    | `sleep 0.1` | 105.7 ± 1.6 | 102.3 | 108.0 | 1.00 |
    "#);

    insta::assert_snapshot!(get_output::<AsciidocExporter>(&timing_results, Some(Unit::MilliSecond), SortOrder::Command), @r#"
    [cols="<,>,>,>,>"]
    |===
    | Command 
    | Mean [ms] 
    | Min [ms] 
    | Max [ms] 
    | Relative 

    | `sleep 2` 
    | 2005.0 ± 2.0 
    | 2002.0 
    | 2008.0 
    | 18.97 ± 0.29 

    | `sleep 0.1` 
    | 105.7 ± 1.6 
    | 102.3 
    | 108.0 
    | 1.00 
    |===
    "#);

    insta::assert_snapshot!(get_output::<OrgmodeExporter>(&timing_results, Some(Unit::MilliSecond), SortOrder::Command), @r#"
    | Command  |  Mean [ms] |  Min [ms] |  Max [ms] |  Relative |
    |--+--+--+--+--|
    | =sleep 2=  |  2005.0 ± 2.0 |  2002.0 |  2008.0 |  18.97 ± 0.29 |
    | =sleep 0.1=  |  105.7 ± 1.6 |  102.3 |  108.0 |  1.00 |
    "#);
}

/// The given time unit (s) is used to set the units for all entries.
#[test]
fn test_markup_export_manual_s() {
    let results = [
        BenchmarkResult {
            command: String::from("sleep 2"),
            command_with_unused_parameters: String::from("sleep 2"),
            mean: 2.0050,
            stddev: Some(0.0020),
            median: 2.0050,
            user: 0.0009,
            system: 0.0012,
            min: 2.0020,
            max: 2.0080,
            times: Some(vec![2.0, 2.0, 2.0]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
        BenchmarkResult {
            command: String::from("sleep 0.1"),
            command_with_unused_parameters: String::from("sleep 0.1"),
            mean: 0.1057,
            stddev: Some(0.0016),
            median: 0.1057,
            user: 0.0009,
            system: 0.0011,
            min: 0.1023,
            max: 0.1080,
            times: Some(vec![0.1, 0.1, 0.1]),
            memory_usage_byte: None,
            exit_codes: vec![Some(0), Some(0), Some(0)],
            parameters: BTreeMap::new(),
        },
    ];

    insta::assert_snapshot!(get_output::<MarkdownExporter>(&results, Some(Unit::Second), SortOrder::Command), @r#"
        | Command | Mean [s] | Min [s] | Max [s] | Relative |
        |:---|---:|---:|---:|---:|
        | `sleep 2` | 2.005 ± 0.002 | 2.002 | 2.008 | 18.97 ± 0.29 |
        | `sleep 0.1` | 0.106 ± 0.002 | 0.102 | 0.108 | 1.00 |
        "#);

    insta::assert_snapshot!(get_output::<MarkdownExporter>(&results, Some(Unit::Second), SortOrder::MeanTime), @r#"
        | Command | Mean [s] | Min [s] | Max [s] | Relative |
        |:---|---:|---:|---:|---:|
        | `sleep 0.1` | 0.106 ± 0.002 | 0.102 | 0.108 | 1.00 |
        | `sleep 2` | 2.005 ± 0.002 | 2.002 | 2.008 | 18.97 ± 0.29 |
        "#);

    insta::assert_snapshot!(get_output::<AsciidocExporter>(&results, Some(Unit::Second), SortOrder::Command), @r#"
    [cols="<,>,>,>,>"]
    |===
    | Command 
    | Mean [s] 
    | Min [s] 
    | Max [s] 
    | Relative 

    | `sleep 2` 
    | 2.005 ± 0.002 
    | 2.002 
    | 2.008 
    | 18.97 ± 0.29 

    | `sleep 0.1` 
    | 0.106 ± 0.002 
    | 0.102 
    | 0.108 
    | 1.00 
    |===
    "#);
}
```

## File: `src/output/format.rs`
```rust
use crate::util::units::{Second, Unit};

/// Format the given duration as a string. The output-unit can be enforced by setting `unit` to
/// `Some(target_unit)`. If `unit` is `None`, it will be determined automatically.
pub fn format_duration(duration: Second, unit: Option<Unit>) -> String {
    let (duration_fmt, _) = format_duration_unit(duration, unit);
    duration_fmt
}

/// Like `format_duration`, but returns the target unit as well.
pub fn format_duration_unit(duration: Second, unit: Option<Unit>) -> (String, Unit) {
    let (out_str, out_unit) = format_duration_value(duration, unit);

    (format!("{} {}", out_str, out_unit.short_name()), out_unit)
}

/// Like `format_duration`, but returns the target unit as well.
pub fn format_duration_value(duration: Second, unit: Option<Unit>) -> (String, Unit) {
    if (duration < 0.001 && unit.is_none()) || unit == Some(Unit::MicroSecond) {
        (Unit::MicroSecond.format(duration), Unit::MicroSecond)
    } else if (duration < 1.0 && unit.is_none()) || unit == Some(Unit::MilliSecond) {
        (Unit::MilliSecond.format(duration), Unit::MilliSecond)
    } else {
        (Unit::Second.format(duration), Unit::Second)
    }
}

#[test]
fn test_format_duration_unit_basic() {
    let (out_str, out_unit) = format_duration_unit(1.3, None);

    assert_eq!("1.300 s", out_str);
    assert_eq!(Unit::Second, out_unit);

    let (out_str, out_unit) = format_duration_unit(1.0, None);

    assert_eq!("1.000 s", out_str);
    assert_eq!(Unit::Second, out_unit);

    let (out_str, out_unit) = format_duration_unit(0.999, None);

    assert_eq!("999.0 ms", out_str);
    assert_eq!(Unit::MilliSecond, out_unit);

    let (out_str, out_unit) = format_duration_unit(0.0005, None);

    assert_eq!("500.0 µs", out_str);
    assert_eq!(Unit::MicroSecond, out_unit);

    let (out_str, out_unit) = format_duration_unit(0.0, None);

    assert_eq!("0.0 µs", out_str);
    assert_eq!(Unit::MicroSecond, out_unit);

    let (out_str, out_unit) = format_duration_unit(1000.0, None);

    assert_eq!("1000.000 s", out_str);
    assert_eq!(Unit::Second, out_unit);
}

#[test]
fn test_format_duration_unit_with_unit() {
    let (out_str, out_unit) = format_duration_unit(1.3, Some(Unit::Second));

    assert_eq!("1.300 s", out_str);
    assert_eq!(Unit::Second, out_unit);

    let (out_str, out_unit) = format_duration_unit(1.3, Some(Unit::MilliSecond));

    assert_eq!("1300.0 ms", out_str);
    assert_eq!(Unit::MilliSecond, out_unit);

    let (out_str, out_unit) = format_duration_unit(1.3, Some(Unit::MicroSecond));

    assert_eq!("1300000.0 µs", out_str);
    assert_eq!(Unit::MicroSecond, out_unit);
}
```

## File: `src/output/mod.rs`
```rust
pub mod format;
pub mod progress_bar;
pub mod warnings;
```

## File: `src/output/progress_bar.rs`
```rust
use indicatif::{ProgressBar, ProgressStyle};
use std::time::Duration;

use crate::options::OutputStyleOption;

#[cfg(not(windows))]
const TICK_SETTINGS: (&str, u64) = ("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏ ", 80);

#[cfg(windows)]
const TICK_SETTINGS: (&str, u64) = (r"+-x| ", 200);

/// Return a pre-configured progress bar
pub fn get_progress_bar(length: u64, msg: &str, option: OutputStyleOption) -> ProgressBar {
    let progressbar_style = match option {
        OutputStyleOption::Basic | OutputStyleOption::Color => ProgressStyle::default_bar(),
        _ => ProgressStyle::default_spinner()
            .tick_chars(TICK_SETTINGS.0)
            .template(" {spinner} {msg:<30} {wide_bar} ETA {eta_precise} ")
            .expect("no template error"),
    };

    let progress_bar = match option {
        OutputStyleOption::Basic | OutputStyleOption::Color => ProgressBar::hidden(),
        _ => ProgressBar::new(length),
    };
    progress_bar.set_style(progressbar_style);
    progress_bar.enable_steady_tick(Duration::from_millis(TICK_SETTINGS.1));
    progress_bar.set_message(msg.to_owned());

    progress_bar
}
```

## File: `src/output/warnings.rs`
```rust
use std::fmt;

use crate::benchmark::MIN_EXECUTION_TIME;
use crate::output::format::format_duration;
use crate::util::units::Second;

pub struct OutlierWarningOptions {
    pub warmup_in_use: bool,
    pub prepare_in_use: bool,
}

/// A list of all possible warnings
pub enum Warnings {
    FastExecutionTime,
    NonZeroExitCode,
    SlowInitialRun(Second, OutlierWarningOptions),
    OutliersDetected(OutlierWarningOptions),
}

impl fmt::Display for Warnings {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            Warnings::FastExecutionTime => write!(
                f,
                "Command took less than {:.0} ms to complete. Note that the results might be \
                inaccurate because hyperfine can not calibrate the shell startup time much \
                more precise than this limit. You can try to use the `-N`/`--shell=none` \
                option to disable the shell completely.",
                MIN_EXECUTION_TIME * 1e3
            ),
            Warnings::NonZeroExitCode => write!(f, "Ignoring non-zero exit code."),
            Warnings::SlowInitialRun(time_first_run, ref options) => write!(
                f,
                "The first benchmarking run for this command was significantly slower than the \
                 rest ({time}). This could be caused by (filesystem) caches that were not filled until \
                 after the first run. {hints}",
                time=format_duration(time_first_run, None),
                hints=match (options.warmup_in_use, options.prepare_in_use) {
                    (true, true) => "You are already using both the '--warmup' option as well \
                    as the '--prepare' option. Consider re-running the benchmark on a quiet system. \
                    Maybe it was a random outlier. Alternatively, consider increasing the warmup \
                    count.",
                    (true, false) => "You are already using the '--warmup' option which helps \
                    to fill these caches before the actual benchmark. You can either try to \
                    increase the warmup count further or re-run this benchmark on a quiet system \
                    in case it was a random outlier. Alternatively, consider using the '--prepare' \
                    option to clear the caches before each timing run.",
                    (false, true) => "You are already using the '--prepare' option which can \
                    be used to clear caches. If you did not use a cache-clearing command with \
                    '--prepare', you can either try that or consider using the '--warmup' option \
                    to fill those caches before the actual benchmark.",
                    (false, false) => "You should consider using the '--warmup' option to fill \
                    those caches before the actual benchmark. Alternatively, use the '--prepare' \
                    option to clear the caches before each timing run."
                }
            ),
            Warnings::OutliersDetected(ref options) => write!(
                f,
                "Statistical outliers were detected. Consider re-running this benchmark on a quiet \
                 system without any interferences from other programs.{hint}",
                hint=if options.warmup_in_use && options.prepare_in_use {
                    ""
                } else {
                    " It might help to use the '--warmup' or '--prepare' options."
                }
            ),
        }
    }
}
```

## File: `src/parameter/mod.rs`
```rust
use crate::util::number::Number;
use std::fmt::Display;

pub mod range_step;
pub mod tokenize;

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum ParameterValue {
    Text(String),
    Numeric(Number),
}

impl Display for ParameterValue {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let str = match self {
            ParameterValue::Text(ref value) => value.clone(),
            ParameterValue::Numeric(value) => value.to_string(),
        };
        write!(f, "{str}")
    }
}

pub type ParameterNameAndValue<'a> = (&'a str, ParameterValue);
```

## File: `src/parameter/range_step.rs`
```rust
use std::convert::TryInto;
use std::ops::{Add, AddAssign, Div, Sub};

use crate::error::ParameterScanError;
use crate::util::number::Number;

pub trait Numeric:
    Add<Output = Self>
    + Sub<Output = Self>
    + Div<Output = Self>
    + AddAssign
    + PartialOrd
    + Copy
    + Clone
    + From<i32>
    + Into<Number>
{
}
impl<
        T: Add<Output = Self>
            + Sub<Output = Self>
            + Div<Output = Self>
            + AddAssign
            + PartialOrd
            + Copy
            + Clone
            + From<i32>
            + Into<Number>,
    > Numeric for T
{
}

#[derive(Debug)]
pub struct RangeStep<T> {
    state: T,
    end: T,
    step: T,
}

impl<T: Numeric> RangeStep<T> {
    pub fn new(start: T, end: T, step: T) -> Result<Self, ParameterScanError> {
        if end < start {
            return Err(ParameterScanError::EmptyRange);
        }

        if step == T::from(0) {
            return Err(ParameterScanError::ZeroStep);
        }

        const MAX_PARAMETERS: usize = 100_000;
        match range_step_size_hint(start, end, step) {
            (_, Some(size)) if size <= MAX_PARAMETERS => Ok(Self {
                state: start,
                end,
                step,
            }),
            _ => Err(ParameterScanError::TooLarge),
        }
    }
}

impl<T: Numeric> Iterator for RangeStep<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        if self.state > self.end {
            return None;
        }
        let return_val = self.state;
        self.state += self.step;

        Some(return_val)
    }

    fn size_hint(&self) -> (usize, Option<usize>) {
        range_step_size_hint(self.state, self.end, self.step)
    }
}

fn range_step_size_hint<T: Numeric>(start: T, end: T, step: T) -> (usize, Option<usize>) {
    if step == T::from(0) {
        return (usize::MAX, None);
    }

    let steps = (end - start + T::from(1)) / step;
    steps
        .into()
        .try_into()
        .map_or((usize::MAX, None), |u| (u, Some(u)))
}

#[cfg(test)]
mod tests {
    use super::*;

    use rust_decimal::Decimal;
    use std::str::FromStr;

    #[test]
    fn test_integer_range() {
        let param_range: Vec<i32> = RangeStep::new(0, 10, 3).unwrap().collect();

        assert_eq!(param_range.len(), 4);
        assert_eq!(param_range[0], 0);
        assert_eq!(param_range[3], 9);
    }

    #[test]
    fn test_decimal_range() {
        let param_min = Decimal::from(0);
        let param_max = Decimal::from(1);
        let step = Decimal::from_str("0.1").unwrap();

        let param_range: Vec<Decimal> = RangeStep::new(param_min, param_max, step)
            .unwrap()
            .collect();

        assert_eq!(param_range.len(), 11);
        assert_eq!(param_range[0], Decimal::from(0));
        assert_eq!(param_range[10], Decimal::from(1));
    }

    #[test]
    fn test_range_step_validate() {
        let result = RangeStep::new(0, 10, 3);
        assert!(result.is_ok());

        let result = RangeStep::new(
            Decimal::from(0),
            Decimal::from(1),
            Decimal::from_str("0.1").unwrap(),
        );
        assert!(result.is_ok());

        let result = RangeStep::new(11, 10, 1);
        assert_eq!(format!("{}", result.unwrap_err()), "Empty parameter range");

        let result = RangeStep::new(0, 10, 0);
        assert_eq!(
            format!("{}", result.unwrap_err()),
            "Zero is not a valid parameter step"
        );

        let result = RangeStep::new(0, 100_001, 1);
        assert_eq!(
            format!("{}", result.unwrap_err()),
            "Parameter range is too large"
        );
    }
}
```

## File: `src/parameter/tokenize.rs`
```rust
pub fn tokenize(values: &str) -> Vec<String> {
    let mut tokens = vec![];
    let mut buf = String::new();

    let mut iter = values.chars();
    while let Some(c) = iter.next() {
        match c {
            '\\' => match iter.next() {
                Some(c2 @ ',') | Some(c2 @ '\\') => {
                    buf.push(c2);
                }
                Some(c2) => {
                    buf.push('\\');
                    buf.push(c2);
                }
                None => buf.push('\\'),
            },
            ',' => {
                tokens.push(buf);
                buf = String::new();
            }
            _ => {
                buf.push(c);
            }
        };
    }

    tokens.push(buf);

    tokens
}

#[test]
fn test_tokenize_single_value() {
    assert_eq!(tokenize(r""), vec![""]);
    assert_eq!(tokenize(r"foo"), vec!["foo"]);
    assert_eq!(tokenize(r" "), vec![" "]);
    assert_eq!(tokenize(r"hello\, world!"), vec!["hello, world!"]);
    assert_eq!(tokenize(r"\,"), vec![","]);
    assert_eq!(tokenize(r"\,\,\,"), vec![",,,"]);
    assert_eq!(tokenize(r"\n"), vec![r"\n"]);
    assert_eq!(tokenize(r"\\"), vec![r"\"]);
    assert_eq!(tokenize(r"\\\,"), vec![r"\,"]);
}

#[test]
fn test_tokenize_multiple_values() {
    assert_eq!(tokenize(r"foo,bar,baz"), vec!["foo", "bar", "baz"]);
    assert_eq!(tokenize(r"hello world,foo"), vec!["hello world", "foo"]);

    assert_eq!(tokenize(r"hello\,world!,baz"), vec!["hello,world!", "baz"]);
}

#[test]
fn test_tokenize_empty_values() {
    assert_eq!(tokenize(r"foo,,bar"), vec!["foo", "", "bar"]);
    assert_eq!(tokenize(r",bar"), vec!["", "bar"]);
    assert_eq!(tokenize(r"bar,"), vec!["bar", ""]);
    assert_eq!(tokenize(r",,"), vec!["", "", ""]);
}
```

## File: `src/timer/mod.rs`
```rust
mod wall_clock_timer;

#[cfg(windows)]
mod windows_timer;

#[cfg(not(windows))]
mod unix_timer;

#[cfg(target_os = "linux")]
use nix::fcntl::{splice, SpliceFFlags};
#[cfg(target_os = "linux")]
use std::fs::File;
#[cfg(target_os = "linux")]
use std::os::fd::AsFd;

#[cfg(target_os = "windows")]
use windows_sys::Win32::System::Threading::CREATE_SUSPENDED;

use crate::util::units::Second;
use wall_clock_timer::WallClockTimer;

use std::io::Read;
use std::process::{ChildStdout, Command, ExitStatus};

use anyhow::Result;

#[cfg(not(windows))]
#[derive(Debug, Copy, Clone)]
struct CPUTimes {
    /// Total amount of time spent executing in user mode
    pub user_usec: i64,

    /// Total amount of time spent executing in kernel mode
    pub system_usec: i64,

    /// Maximum amount of memory used by the process, in bytes
    pub memory_usage_byte: u64,
}

/// Used to indicate the result of running a command
#[derive(Debug, Copy, Clone)]
pub struct TimerResult {
    pub time_real: Second,
    pub time_user: Second,
    pub time_system: Second,
    pub memory_usage_byte: u64,
    /// The exit status of the process
    pub status: ExitStatus,
}

/// Discard the output of a child process.
fn discard(output: ChildStdout) {
    const CHUNK_SIZE: usize = 64 << 10;

    #[cfg(target_os = "linux")]
    {
        if let Ok(file) = File::create("/dev/null") {
            while let Ok(bytes) = splice(
                output.as_fd(),
                None,
                file.as_fd(),
                None,
                CHUNK_SIZE,
                SpliceFFlags::empty(),
            ) {
                if bytes == 0 {
                    break;
                }
            }
        }
    }

    let mut output = output;
    let mut buf = [0; CHUNK_SIZE];
    while let Ok(bytes) = output.read(&mut buf) {
        if bytes == 0 {
            break;
        }
    }
}

/// Execute the given command and return a timing summary
pub fn execute_and_measure(mut command: Command) -> Result<TimerResult> {
    #[cfg(not(windows))]
    let cpu_timer = self::unix_timer::CPUTimer::start();

    #[cfg(windows)]
    {
        use std::os::windows::process::CommandExt;

        // Create the process in a suspended state so that we don't miss any cpu time between process creation and `CPUTimer` start.
        command.creation_flags(CREATE_SUSPENDED);
    }

    let wallclock_timer = WallClockTimer::start();
    let mut child = command.spawn()?;

    #[cfg(windows)]
    let cpu_timer = {
        // SAFETY: We created a suspended process
        unsafe { self::windows_timer::CPUTimer::start_suspended_process(&child) }
    };

    if let Some(output) = child.stdout.take() {
        // Handle CommandOutputPolicy::Pipe
        discard(output);
    }

    let status = child.wait()?;

    let time_real = wallclock_timer.stop();
    let (time_user, time_system, memory_usage_byte) = cpu_timer.stop();

    Ok(TimerResult {
        time_real,
        time_user,
        time_system,
        memory_usage_byte,
        status,
    })
}
```

## File: `src/timer/unix_timer.rs`
```rust
#![cfg(not(windows))]

use std::convert::TryFrom;
use std::mem;

use crate::timer::CPUTimes;
use crate::util::units::Second;

#[derive(Debug, Copy, Clone)]
pub struct CPUInterval {
    /// Total amount of time spent executing in user mode
    pub user: Second,

    /// Total amount of time spent executing in kernel mode
    pub system: Second,
}

pub struct CPUTimer {
    start_cpu: CPUTimes,
}

impl CPUTimer {
    pub fn start() -> Self {
        CPUTimer {
            start_cpu: get_cpu_times(),
        }
    }

    pub fn stop(&self) -> (Second, Second, u64) {
        let end_cpu = get_cpu_times();
        let cpu_interval = cpu_time_interval(&self.start_cpu, &end_cpu);
        (
            cpu_interval.user,
            cpu_interval.system,
            end_cpu.memory_usage_byte,
        )
    }
}

/// Read CPU execution times ('user' and 'system')
fn get_cpu_times() -> CPUTimes {
    use libc::{getrusage, rusage, RUSAGE_CHILDREN};

    let result: rusage = unsafe {
        let mut buf = mem::zeroed();
        let success = getrusage(RUSAGE_CHILDREN, &mut buf);
        assert_eq!(0, success);
        buf
    };

    const MICROSEC_PER_SEC: i64 = 1000 * 1000;

    // Linux and *BSD return the value in KibiBytes, Darwin flavors in bytes
    let max_rss_byte = if cfg!(target_os = "macos") || cfg!(target_os = "ios") {
        result.ru_maxrss
    } else {
        result.ru_maxrss * 1024
    };

    #[allow(clippy::useless_conversion)]
    CPUTimes {
        user_usec: i64::from(result.ru_utime.tv_sec) * MICROSEC_PER_SEC
            + i64::from(result.ru_utime.tv_usec),
        system_usec: i64::from(result.ru_stime.tv_sec) * MICROSEC_PER_SEC
            + i64::from(result.ru_stime.tv_usec),
        memory_usage_byte: u64::try_from(max_rss_byte).unwrap_or(0),
    }
}

/// Compute the time intervals in between two `CPUTimes` snapshots
fn cpu_time_interval(start: &CPUTimes, end: &CPUTimes) -> CPUInterval {
    CPUInterval {
        user: ((end.user_usec - start.user_usec) as f64) * 1e-6,
        system: ((end.system_usec - start.system_usec) as f64) * 1e-6,
    }
}

#[cfg(test)]
use approx::assert_relative_eq;

#[test]
fn test_cpu_time_interval() {
    let t_a = CPUTimes {
        user_usec: 12345,
        system_usec: 54321,
        memory_usage_byte: 0,
    };

    let t_b = CPUTimes {
        user_usec: 20000,
        system_usec: 70000,
        memory_usage_byte: 0,
    };

    let t_zero = cpu_time_interval(&t_a, &t_a);
    assert!(t_zero.user.abs() < f64::EPSILON);
    assert!(t_zero.system.abs() < f64::EPSILON);

    let t_ab = cpu_time_interval(&t_a, &t_b);
    assert_relative_eq!(0.007655, t_ab.user);
    assert_relative_eq!(0.015679, t_ab.system);

    let t_ba = cpu_time_interval(&t_b, &t_a);
    assert_relative_eq!(-0.007655, t_ba.user);
    assert_relative_eq!(-0.015679, t_ba.system);
}
```

## File: `src/timer/wall_clock_timer.rs`
```rust
use std::time::Instant;

use crate::util::units::Second;

pub struct WallClockTimer {
    start: Instant,
}

impl WallClockTimer {
    pub fn start() -> WallClockTimer {
        WallClockTimer {
            start: Instant::now(),
        }
    }

    pub fn stop(&self) -> Second {
        let duration = self.start.elapsed();
        duration.as_secs() as f64 + f64::from(duration.subsec_nanos()) * 1e-9
    }
}
```

## File: `src/timer/windows_timer.rs`
```rust
#![cfg(windows)]
#![warn(unsafe_op_in_unsafe_fn)]

use std::{mem, os::windows::io::AsRawHandle, process, ptr};

use windows_sys::Win32::{
    Foundation::{CloseHandle, HANDLE},
    System::JobObjects::{
        AssignProcessToJobObject, CreateJobObjectW, JobObjectBasicAccountingInformation,
        QueryInformationJobObject, JOBOBJECT_BASIC_ACCOUNTING_INFORMATION,
    },
};

#[cfg(feature = "windows_process_extensions_main_thread_handle")]
use std::os::windows::process::ChildExt;
#[cfg(feature = "windows_process_extensions_main_thread_handle")]
use windows_sys::Win32::System::Threading::ResumeThread;

#[cfg(not(feature = "windows_process_extensions_main_thread_handle"))]
use once_cell::sync::Lazy;
#[cfg(not(feature = "windows_process_extensions_main_thread_handle"))]
use windows_sys::{
    s, w,
    Win32::{
        Foundation::{NTSTATUS, STATUS_SUCCESS},
        System::LibraryLoader::{GetModuleHandleW, GetProcAddress},
    },
};

use crate::util::units::Second;

const HUNDRED_NS_PER_MS: i64 = 10;

#[cfg(not(feature = "windows_process_extensions_main_thread_handle"))]
#[allow(non_upper_case_globals)]
static NtResumeProcess: Lazy<unsafe extern "system" fn(ProcessHandle: HANDLE) -> NTSTATUS> =
    Lazy::new(|| {
        // SAFETY: Getting the module handle for ntdll.dll is safe
        let ntdll = unsafe { GetModuleHandleW(w!("ntdll.dll")) };
        assert!(ntdll != std::ptr::null_mut(), "GetModuleHandleW failed");

        // SAFETY: The ntdll handle is valid
        let nt_resume_process = unsafe { GetProcAddress(ntdll, s!("NtResumeProcess")) };

        // SAFETY: We transmute to the correct function signature
        unsafe { mem::transmute(nt_resume_process.unwrap()) }
    });

pub struct CPUTimer {
    job_object: HANDLE,
}

impl CPUTimer {
    pub unsafe fn start_suspended_process(child: &process::Child) -> Self {
        let child_handle = child.as_raw_handle() as HANDLE;

        // SAFETY: Creating a new job object is safe
        let job_object = unsafe { CreateJobObjectW(ptr::null_mut(), ptr::null_mut()) };
        assert!(
            job_object != std::ptr::null_mut(),
            "CreateJobObjectW failed"
        );

        // SAFETY: The job object handle is valid
        let ret = unsafe { AssignProcessToJobObject(job_object, child_handle) };
        assert!(ret != 0, "AssignProcessToJobObject failed");

        #[cfg(feature = "windows_process_extensions_main_thread_handle")]
        {
            // SAFETY: The main thread handle is valid
            let ret = unsafe { ResumeThread(child.main_thread_handle().as_raw_handle() as HANDLE) };
            assert!(ret != u32::MAX, "ResumeThread failed");
        }

        #[cfg(not(feature = "windows_process_extensions_main_thread_handle"))]
        {
            // Since we can't get the main thread handle on stable rust, we use
            // the undocumented but widely known `NtResumeProcess` function to
            // resume a process by it's handle.

            // SAFETY: The process handle is valid
            let ret = unsafe { NtResumeProcess(child_handle) };
            assert!(ret == STATUS_SUCCESS, "NtResumeProcess failed");
        }

        Self { job_object }
    }

    pub fn stop(&self) -> (Second, Second, u64) {
        let mut job_object_info =
            mem::MaybeUninit::<JOBOBJECT_BASIC_ACCOUNTING_INFORMATION>::uninit();

        // SAFETY: A valid job object got created in `start_suspended_process`
        let res = unsafe {
            QueryInformationJobObject(
                self.job_object,
                JobObjectBasicAccountingInformation,
                job_object_info.as_mut_ptr().cast(),
                mem::size_of::<JOBOBJECT_BASIC_ACCOUNTING_INFORMATION>() as u32,
                ptr::null_mut(),
            )
        };

        if res != 0 {
            // SAFETY: The job object info got correctly initialized
            let job_object_info = unsafe { job_object_info.assume_init() };

            // The `TotalUserTime` is "The total amount of user-mode execution time for
            // all active processes associated with the job, as well as all terminated processes no
            // longer associated with the job, in 100-nanosecond ticks."
            let user: i64 = job_object_info.TotalUserTime / HUNDRED_NS_PER_MS;

            // The `TotalKernelTime` is "The total amount of kernel-mode execution time
            // for all active processes associated with the job, as well as all terminated
            // processes no longer associated with the job, in 100-nanosecond ticks."
            let kernel: i64 = job_object_info.TotalKernelTime / HUNDRED_NS_PER_MS;
            (user as f64 * 1e-6, kernel as f64 * 1e-6, 0)
        } else {
            (0.0, 0.0, 0)
        }
    }
}

impl Drop for CPUTimer {
    fn drop(&mut self) {
        // SAFETY: A valid job object got created in `start_suspended_process`
        unsafe { CloseHandle(self.job_object) };
    }
}
```

## File: `src/util/exit_code.rs`
```rust
use std::process::ExitStatus;

#[cfg(unix)]
pub fn extract_exit_code(status: ExitStatus) -> Option<i32> {
    use std::os::unix::process::ExitStatusExt;

    // From the ExitStatus::code documentation:
    //
    //   "On Unix, this will return None if the process was terminated by a signal."
    //
    // In that case, ExitStatusExt::signal should never return None.
    //
    // To differentiate between "normal" exit codes and signals, we are using a technique
    // similar to bash (https://tldp.org/LDP/abs/html/exitcodes.html) and add 128 to the
    // signal value.
    status.code().or_else(|| status.signal().map(|s| s + 128))
}

#[cfg(not(unix))]
pub fn extract_exit_code(status: ExitStatus) -> Option<i32> {
    status.code()
}
```

## File: `src/util/min_max.rs`
```rust
/// A max function for f64's without NaNs
pub fn max(vals: &[f64]) -> f64 {
    *vals
        .iter()
        .max_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap()
}

/// A min function for f64's without NaNs
pub fn min(vals: &[f64]) -> f64 {
    *vals
        .iter()
        .min_by(|a, b| a.partial_cmp(b).unwrap())
        .unwrap()
}

#[test]
fn test_max() {
    let assert_float_eq = |a: f64, b: f64| {
        assert!((a - b).abs() < f64::EPSILON);
    };

    assert_float_eq(1.0, max(&[1.0]));
    assert_float_eq(-1.0, max(&[-1.0]));
    assert_float_eq(-1.0, max(&[-2.0, -1.0]));
    assert_float_eq(1.0, max(&[-1.0, 1.0]));
    assert_float_eq(1.0, max(&[-1.0, 1.0, 0.0]));
}
```

## File: `src/util/mod.rs`
```rust
pub mod exit_code;
pub mod min_max;
pub mod number;
pub mod randomized_environment_offset;
pub mod units;
```

## File: `src/util/number.rs`
```rust
use std::convert::TryFrom;
use std::fmt;

use rust_decimal::prelude::ToPrimitive;
use rust_decimal::Decimal;
use serde::Serialize;

#[derive(Debug, Clone, Serialize, Copy, PartialEq, Eq)]
#[serde(untagged)]
pub enum Number {
    Int(i32),
    Decimal(Decimal),
}

impl fmt::Display for Number {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            Number::Int(i) => fmt::Display::fmt(&i, f),
            Number::Decimal(i) => fmt::Display::fmt(&i, f),
        }
    }
}

impl From<i32> for Number {
    fn from(x: i32) -> Number {
        Number::Int(x)
    }
}

impl From<Decimal> for Number {
    fn from(x: Decimal) -> Number {
        Number::Decimal(x)
    }
}

impl TryFrom<Number> for usize {
    type Error = ();

    fn try_from(numeric: Number) -> Result<Self, Self::Error> {
        match numeric {
            Number::Int(i) => usize::try_from(i).map_err(|_| ()),
            Number::Decimal(d) => match d.to_u64() {
                Some(u) => usize::try_from(u).map_err(|_| ()),
                None => Err(()),
            },
        }
    }
}
```

## File: `src/util/randomized_environment_offset.rs`
```rust
/// Returns a string with a random length. This value will be set as an environment
/// variable to account for offset effects. See [1] for more details.
///
/// [1] Mytkowicz, 2009. Producing Wrong Data Without Doing Anything Obviously Wrong!.
///     Sigplan Notices - SIGPLAN. 44. 265-276. 10.1145/1508284.1508275.
pub fn value() -> String {
    "X".repeat(rand::random::<usize>() % 4096usize)
}
```

## File: `src/util/units.rs`
```rust
//! This module contains common units.

pub type Scalar = f64;

/// Type alias for unit of time
pub type Second = Scalar;

/// Supported time units
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Unit {
    Second,
    MilliSecond,
    MicroSecond,
}

impl Unit {
    /// The abbreviation of the Unit.
    pub fn short_name(self) -> String {
        match self {
            Unit::Second => String::from("s"),
            Unit::MilliSecond => String::from("ms"),
            Unit::MicroSecond => String::from("µs"),
        }
    }

    /// Returns the Second value formatted for the Unit.
    pub fn format(self, value: Second) -> String {
        match self {
            Unit::Second => format!("{value:.3}"),
            Unit::MilliSecond => format!("{:.1}", value * 1e3),
            Unit::MicroSecond => format!("{:.1}", value * 1e6),
        }
    }
}

#[test]
fn test_unit_short_name() {
    assert_eq!("s", Unit::Second.short_name());
    assert_eq!("ms", Unit::MilliSecond.short_name());
    assert_eq!("µs", Unit::MicroSecond.short_name());
}

// Note - the values are rounded when formatted.
#[test]
fn test_unit_format() {
    let value: Second = 123.456789;
    assert_eq!("123.457", Unit::Second.format(value));
    assert_eq!("123456.8", Unit::MilliSecond.format(value));

    assert_eq!("1234.6", Unit::MicroSecond.format(0.00123456));
}
```

## File: `tests/common.rs`
```rust
use std::process::Command;

use assert_cmd::cargo::CommandCargoExt;

pub fn hyperfine_raw_command() -> Command {
    let mut cmd = Command::cargo_bin("hyperfine").unwrap();
    cmd.current_dir("tests/");
    cmd
}

pub fn hyperfine() -> assert_cmd::Command {
    assert_cmd::Command::from_std(hyperfine_raw_command())
}
```

## File: `tests/example_input_file.txt`
```
This text is part of a file
```

## File: `tests/execution_order_tests.rs`
```rust
use std::{fs::File, io::Read, path::PathBuf};

use tempfile::{tempdir, TempDir};

mod common;
use common::hyperfine;

struct ExecutionOrderTest {
    cmd: assert_cmd::Command,
    expected_content: String,
    logfile_path: PathBuf,
    #[allow(dead_code)]
    tempdir: TempDir,
}

impl ExecutionOrderTest {
    fn new() -> Self {
        let tempdir = tempdir().unwrap();
        let logfile_path = tempdir.path().join("output.log");

        ExecutionOrderTest {
            cmd: hyperfine(),
            expected_content: String::new(),
            logfile_path,
            tempdir,
        }
    }

    fn arg<S: AsRef<str>>(&mut self, arg: S) -> &mut Self {
        self.cmd.arg(arg.as_ref());
        self
    }

    fn get_command(&self, output: &str) -> String {
        format!(
            "echo {output} >> {path}",
            output = output,
            path = self.logfile_path.to_string_lossy()
        )
    }

    fn command(&mut self, output: &str) -> &mut Self {
        self.arg(self.get_command(output));
        self
    }

    fn setup(&mut self, output: &str) -> &mut Self {
        self.arg("--setup");
        self.command(output)
    }

    fn prepare(&mut self, output: &str) -> &mut Self {
        self.arg("--prepare");
        self.command(output)
    }

    fn reference(&mut self, output: &str) -> &mut Self {
        self.arg("--reference");
        self.command(output)
    }

    fn conclude(&mut self, output: &str) -> &mut Self {
        self.arg("--conclude");
        self.command(output)
    }

    fn cleanup(&mut self, output: &str) -> &mut Self {
        self.arg("--cleanup");
        self.command(output)
    }

    fn expect_output(&mut self, output: &str) -> &mut Self {
        self.expected_content.push_str(output);

        #[cfg(windows)]
        {
            self.expected_content.push_str(" \r");
        }

        self.expected_content.push('\n');
        self
    }

    fn run(&mut self) {
        self.cmd.assert().success();

        let mut f = File::open(&self.logfile_path).unwrap();
        let mut content = String::new();
        f.read_to_string(&mut content).unwrap();

        assert_eq!(content, self.expected_content);
    }
}

impl Default for ExecutionOrderTest {
    fn default() -> Self {
        Self::new()
    }
}

#[test]
fn benchmarks_are_executed_sequentially_one() {
    ExecutionOrderTest::new()
        .arg("--runs=1")
        .command("command 1")
        .command("command 2")
        .expect_output("command 1")
        .expect_output("command 2")
        .run();
}

#[test]
fn benchmarks_are_executed_sequentially() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .command("command 1")
        .command("command 2")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 2")
        .expect_output("command 2")
        .run();
}

#[test]
fn warmup_runs_are_executed_before_benchmarking_runs() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .arg("--warmup=3")
        .command("command 1")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 1")
        .run();
}

#[test]
fn setup_commands_are_executed_before_each_series_of_timing_runs() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .setup("setup")
        .command("command 1")
        .command("command 2")
        .expect_output("setup")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("setup")
        .expect_output("command 2")
        .expect_output("command 2")
        .run();
}

#[test]
fn prepare_commands_are_executed_before_each_timing_run() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .prepare("prepare")
        .command("command 1")
        .command("command 2")
        .expect_output("prepare")
        .expect_output("command 1")
        .expect_output("prepare")
        .expect_output("command 1")
        .expect_output("prepare")
        .expect_output("command 2")
        .expect_output("prepare")
        .expect_output("command 2")
        .run();
}

#[test]
fn conclude_commands_are_executed_after_each_timing_run() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .conclude("conclude")
        .command("command 1")
        .command("command 2")
        .expect_output("command 1")
        .expect_output("conclude")
        .expect_output("command 1")
        .expect_output("conclude")
        .expect_output("command 2")
        .expect_output("conclude")
        .expect_output("command 2")
        .expect_output("conclude")
        .run();
}

#[test]
fn prepare_commands_are_executed_before_each_warmup() {
    ExecutionOrderTest::new()
        .arg("--warmup=2")
        .arg("--runs=1")
        .prepare("prepare")
        .command("command 1")
        .command("command 2")
        // warmup 1
        .expect_output("prepare")
        .expect_output("command 1")
        .expect_output("prepare")
        .expect_output("command 1")
        // benchmark 1
        .expect_output("prepare")
        .expect_output("command 1")
        // warmup 2
        .expect_output("prepare")
        .expect_output("command 2")
        .expect_output("prepare")
        .expect_output("command 2")
        // benchmark 2
        .expect_output("prepare")
        .expect_output("command 2")
        .run();
}

#[test]
fn conclude_commands_are_executed_after_each_warmup() {
    ExecutionOrderTest::new()
        .arg("--warmup=2")
        .arg("--runs=1")
        .conclude("conclude")
        .command("command 1")
        .command("command 2")
        // warmup 1
        .expect_output("command 1")
        .expect_output("conclude")
        .expect_output("command 1")
        .expect_output("conclude")
        // benchmark 1
        .expect_output("command 1")
        .expect_output("conclude")
        // warmup 2
        .expect_output("command 2")
        .expect_output("conclude")
        .expect_output("command 2")
        .expect_output("conclude")
        // benchmark 2
        .expect_output("command 2")
        .expect_output("conclude")
        .run();
}

#[test]
fn cleanup_commands_are_executed_once_after_each_benchmark() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .cleanup("cleanup")
        .command("command 1")
        .command("command 2")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("cleanup")
        .expect_output("command 2")
        .expect_output("command 2")
        .expect_output("cleanup")
        .run();
}

#[test]
fn setup_prepare_cleanup_combined() {
    ExecutionOrderTest::new()
        .arg("--warmup=1")
        .arg("--runs=2")
        .setup("setup")
        .prepare("prepare")
        .command("command1")
        .command("command2")
        .cleanup("cleanup")
        // 1
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("cleanup")
        // 2
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("cleanup")
        .run();
}

#[test]
fn setup_prepare_conclude_cleanup_combined() {
    ExecutionOrderTest::new()
        .arg("--warmup=1")
        .arg("--runs=2")
        .setup("setup")
        .prepare("prepare")
        .command("command1")
        .command("command2")
        .conclude("conclude")
        .cleanup("cleanup")
        // 1
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("conclude")
        .expect_output("cleanup")
        // 2
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("conclude")
        .expect_output("cleanup")
        .run();
}

#[test]
fn single_parameter_value() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .arg("--parameter-list")
        .arg("number")
        .arg("1,2,3")
        .command("command {number}")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 2")
        .expect_output("command 2")
        .expect_output("command 3")
        .expect_output("command 3")
        .run();
}

#[test]
fn multiple_parameter_values() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .arg("--parameter-list")
        .arg("number")
        .arg("1,2,3")
        .arg("--parameter-list")
        .arg("letter")
        .arg("a,b")
        .command("command {number} {letter}")
        .expect_output("command 1 a")
        .expect_output("command 1 a")
        .expect_output("command 2 a")
        .expect_output("command 2 a")
        .expect_output("command 3 a")
        .expect_output("command 3 a")
        .expect_output("command 1 b")
        .expect_output("command 1 b")
        .expect_output("command 2 b")
        .expect_output("command 2 b")
        .expect_output("command 3 b")
        .expect_output("command 3 b")
        .run();
}

#[test]
fn reference_is_executed_first() {
    ExecutionOrderTest::new()
        .arg("--runs=1")
        .reference("reference")
        .command("command 1")
        .command("command 2")
        .expect_output("reference")
        .expect_output("command 1")
        .expect_output("command 2")
        .run();
}

#[test]
fn reference_is_executed_first_parameter_value() {
    ExecutionOrderTest::new()
        .arg("--runs=2")
        .reference("reference")
        .arg("--parameter-list")
        .arg("number")
        .arg("1,2,3")
        .command("command {number}")
        .expect_output("reference")
        .expect_output("reference")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 2")
        .expect_output("command 2")
        .expect_output("command 3")
        .expect_output("command 3")
        .run();
}

#[test]
fn reference_is_executed_separately_from_commands() {
    ExecutionOrderTest::new()
        .arg("--runs=1")
        .reference("command 1")
        .command("command 1")
        .command("command 2")
        .expect_output("command 1")
        .expect_output("command 1")
        .expect_output("command 2")
        .run();
}

#[test]
fn setup_prepare_reference_conclude_cleanup_combined() {
    ExecutionOrderTest::new()
        .arg("--warmup=1")
        .arg("--runs=2")
        .setup("setup")
        .prepare("prepare")
        .reference("reference")
        .command("command1")
        .command("command2")
        .conclude("conclude")
        .cleanup("cleanup")
        // reference
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("reference")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("reference")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("reference")
        .expect_output("conclude")
        .expect_output("cleanup")
        // 1
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command1")
        .expect_output("conclude")
        .expect_output("cleanup")
        // 2
        .expect_output("setup")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("conclude")
        .expect_output("prepare")
        .expect_output("command2")
        .expect_output("conclude")
        .expect_output("cleanup")
        .run();
}

#[test]
fn setup_separate_prepare_separate_conclude_cleanup_combined() {
    ExecutionOrderTest::new()
        .arg("--warmup=1")
        .arg("--runs=2")
        .setup("setup")
        .cleanup("cleanup")
        .prepare("prepare1")
        .command("command1")
        .conclude("conclude1")
        .prepare("prepare2")
        .command("command2")
        .conclude("conclude2")
        // 1
        .expect_output("setup")
        .expect_output("prepare1")
        .expect_output("command1")
        .expect_output("conclude1")
        .expect_output("prepare1")
        .expect_output("command1")
        .expect_output("conclude1")
        .expect_output("prepare1")
        .expect_output("command1")
        .expect_output("conclude1")
        .expect_output("cleanup")
        // 2
        .expect_output("setup")
        .expect_output("prepare2")
        .expect_output("command2")
        .expect_output("conclude2")
        .expect_output("prepare2")
        .expect_output("command2")
        .expect_output("conclude2")
        .expect_output("prepare2")
        .expect_output("command2")
        .expect_output("conclude2")
        .expect_output("cleanup")
        .run();
}

#[test]
fn setup_separate_prepare_reference_separate_conclude_cleanup_combined() {
    ExecutionOrderTest::new()
        .arg("--warmup=1")
        .arg("--runs=2")
        .setup("setup")
        .cleanup("cleanup")
        .prepare("prepareref")
        .reference("reference")
        .conclude("concluderef")
        .prepare("prepare1")
        .command("command1")
        .conclude("conclude1")
        .prepare("prepare2")
        .command("command2")
        .conclude("conclude2")
        // reference
        .expect_output("setup")
        .expect_output("prepareref")
        .expect_output("reference")
        .expect_output("concluderef")
        .expect_output("prepareref")
        .expect_output("reference")
        .expect_output("concluderef")
        .expect_output("prepareref")
        .expect_output("reference")
        .expect_output("concluderef")
        .expect_output("cleanup")
        // 1
        .expect_output("setup")
        .expect_output("prepare1")
        .expect_output("command1")
        .expect_output("conclude1")
        .expect_output("prepare1")
        .expect_output("command1")
        .expect_output("conclude1")
        .expect_output("prepare1")
        .expect_output("command1")
        .expect_output("conclude1")
        .expect_output("cleanup")
        // 2
        .expect_output("setup")
        .expect_output("prepare2")
        .expect_output("command2")
        .expect_output("conclude2")
        .expect_output("prepare2")
        .expect_output("command2")
        .expect_output("conclude2")
        .expect_output("prepare2")
        .expect_output("command2")
        .expect_output("conclude2")
        .expect_output("cleanup")
        .run();
}
```

## File: `tests/integration_tests.rs`
```rust
mod common;
use common::hyperfine;

use predicates::prelude::*;

/// Platform-specific I/O utility.
/// - On Unix-like systems, defaults to `cat`.
/// - On Windows, uses `findstr` as an alternative.
///   See: <https://superuser.com/questions/853580/real-windows-equivalent-to-cat-stdin>
const STDIN_READ_COMMAND: &str = if cfg!(windows) { "findstr x*" } else { "cat" };

pub fn hyperfine_debug() -> assert_cmd::Command {
    let mut cmd = hyperfine();
    cmd.arg("--debug-mode");
    cmd
}

#[test]
fn runs_successfully() {
    hyperfine()
        .arg("--runs=2")
        .arg("echo dummy benchmark")
        .assert()
        .success();
}

#[test]
fn one_run_is_supported() {
    hyperfine()
        .arg("--runs=1")
        .arg("echo dummy benchmark")
        .assert()
        .success();
}

#[test]
fn can_run_commands_without_a_shell() {
    hyperfine()
        .arg("--runs=1")
        .arg("--show-output")
        .arg("--shell=none")
        .arg("echo 'hello world' argument2")
        .assert()
        .success()
        .stdout(predicate::str::contains("hello world argument2"));
}

#[test]
fn fails_with_wrong_number_of_command_name_arguments() {
    hyperfine()
        .arg("--command-name=a")
        .arg("--command-name=b")
        .arg("echo a")
        .assert()
        .failure()
        .stderr(predicate::str::contains("Too many --command-name options"));
}

#[test]
fn fails_with_wrong_number_of_prepare_options() {
    hyperfine()
        .arg("--runs=1")
        .arg("--prepare=echo a")
        .arg("--prepare=echo b")
        .arg("echo a")
        .arg("echo b")
        .assert()
        .success();

    hyperfine()
        .arg("--runs=1")
        .arg("--prepare=echo ref")
        .arg("--prepare=echo a")
        .arg("--prepare=echo b")
        .arg("--reference=echo ref")
        .arg("echo a")
        .arg("echo b")
        .assert()
        .success();

    hyperfine()
        .arg("--runs=1")
        .arg("--prepare=echo a")
        .arg("--prepare=echo b")
        .arg("echo a")
        .arg("echo b")
        .arg("echo c")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The '--prepare' option has to be provided",
        ));

    hyperfine()
        .arg("--runs=1")
        .arg("--prepare=echo a")
        .arg("--prepare=echo b")
        .arg("--reference=echo ref")
        .arg("echo a")
        .arg("echo b")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The '--prepare' option has to be provided",
        ));
}

#[test]
fn fails_with_wrong_number_of_conclude_options() {
    hyperfine()
        .arg("--runs=1")
        .arg("--conclude=echo a")
        .arg("--conclude=echo b")
        .arg("echo a")
        .arg("echo b")
        .assert()
        .success();

    hyperfine()
        .arg("--runs=1")
        .arg("--conclude=echo ref")
        .arg("--conclude=echo a")
        .arg("--conclude=echo b")
        .arg("--reference=echo ref")
        .arg("echo a")
        .arg("echo b")
        .assert()
        .success();

    hyperfine()
        .arg("--runs=1")
        .arg("--conclude=echo a")
        .arg("--conclude=echo b")
        .arg("echo a")
        .arg("echo b")
        .arg("echo c")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The '--conclude' option has to be provided",
        ));

    hyperfine()
        .arg("--runs=1")
        .arg("--conclude=echo a")
        .arg("--conclude=echo b")
        .arg("--reference=echo ref")
        .arg("echo a")
        .arg("echo b")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The '--conclude' option has to be provided",
        ));
}

#[test]
fn fails_with_duplicate_parameter_names() {
    hyperfine()
        .arg("--parameter-list")
        .arg("x")
        .arg("1,2,3")
        .arg("--parameter-list")
        .arg("x")
        .arg("a,b,c")
        .arg("echo test")
        .assert()
        .failure()
        .stderr(predicate::str::contains("Duplicate parameter names: x"));
}

#[test]
fn fails_for_unknown_command() {
    hyperfine()
        .arg("--runs=1")
        .arg("some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "Command terminated with non-zero exit code",
        ));
}

#[test]
fn fails_for_unknown_command_without_shell() {
    hyperfine()
        .arg("--shell=none")
        .arg("--runs=1")
        .arg("some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "Failed to run command 'some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577'",
        ));
}

#[cfg(unix)]
#[test]
fn fails_for_failing_command_without_shell() {
    hyperfine()
        .arg("--shell=none")
        .arg("--runs=1")
        .arg("false")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "Command terminated with non-zero exit code",
        ));
}

#[test]
fn fails_for_unknown_setup_command() {
    hyperfine()
        .arg("--runs=1")
        .arg("--setup=some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577")
        .arg("echo test")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The setup command terminated with a non-zero exit code.",
        ));
}

#[test]
fn fails_for_unknown_cleanup_command() {
    hyperfine()
        .arg("--runs=1")
        .arg("--cleanup=some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577")
        .arg("echo test")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The cleanup command terminated with a non-zero exit code.",
        ));
}

#[test]
fn fails_for_unknown_prepare_command() {
    hyperfine()
        .arg("--prepare=some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577")
        .arg("echo test")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The preparation command terminated with a non-zero exit code.",
        ));
}

#[test]
fn fails_for_unknown_conclude_command() {
    hyperfine()
        .arg("--conclude=some-nonexisting-program-b5d9574198b7e4b12a71fa4747c0a577")
        .arg("echo test")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The conclusion command terminated with a non-zero exit code.",
        ));
}

#[cfg(unix)]
#[test]
fn can_run_failing_commands_with_ignore_failure_option() {
    hyperfine()
        .arg("false")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "Command terminated with non-zero exit code",
        ));

    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure")
        .arg("false")
        .assert()
        .success();
}

#[cfg(unix)]
#[test]
fn can_ignore_specific_exit_codes() {
    // Test that specifying exit code 1 ignores it
    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=1")
        .arg("exit 1")
        .assert()
        .success();

    // Test that other exit codes still fail
    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=1")
        .arg("exit 2")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "Command terminated with non-zero exit code 2",
        ));
}

#[cfg(unix)]
#[test]
fn can_ignore_multiple_exit_codes() {
    // Test that all specified exit codes are ignored
    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=1,2,3")
        .arg("exit 1")
        .assert()
        .success();

    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=1,2,3")
        .arg("exit 2")
        .assert()
        .success();

    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=1,2,3")
        .arg("exit 3")
        .assert()
        .success();

    // Test that other exit codes still fail
    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=1,2,3")
        .arg("exit 4")
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "Command terminated with non-zero exit code 4",
        ));
}

#[cfg(unix)]
#[test]
fn ignore_failure_with_all_non_zero() {
    // Test explicit "all-non-zero" mode
    hyperfine()
        .arg("--runs=1")
        .arg("--ignore-failure=all-non-zero")
        .arg("exit 5")
        .assert()
        .success();
}

#[test]
fn shows_output_of_benchmarked_command() {
    hyperfine()
        .arg("--runs=2")
        .arg("--command-name=dummy")
        .arg("--show-output")
        .arg("echo 4fd47015")
        .assert()
        .success()
        .stdout(predicate::str::contains("4fd47015").count(2));
}

#[test]
fn runs_commands_using_user_defined_shell() {
    hyperfine()
        .arg("--runs=1")
        .arg("--show-output")
        .arg("--shell")
        .arg("echo 'custom_shell' '--shell-arg'")
        .arg("echo benchmark")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("custom_shell --shell-arg -c echo benchmark").or(
                predicate::str::contains("custom_shell --shell-arg /C echo benchmark"),
            ),
        );
}

#[test]
fn can_pass_input_to_command_from_a_file() {
    hyperfine()
        .arg("--runs=1")
        .arg("--input=example_input_file.txt")
        .arg("--show-output")
        .arg(STDIN_READ_COMMAND)
        .assert()
        .success()
        .stdout(predicate::str::contains("This text is part of a file"));
}

#[test]
fn fails_if_invalid_stdin_data_file_provided() {
    hyperfine()
        .arg("--runs=1")
        .arg("--input=example_non_existent_file.txt")
        .arg("--show-output")
        .arg(STDIN_READ_COMMAND)
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "The file 'example_non_existent_file.txt' specified as '--input' does not exist",
        ));
}

#[test]
fn returns_mean_time_in_correct_unit() {
    hyperfine_debug()
        .arg("sleep 1.234")
        .assert()
        .success()
        .stdout(predicate::str::contains("Time (mean ± σ):      1.234 s ±"));

    hyperfine_debug()
        .arg("sleep 0.123")
        .assert()
        .success()
        .stdout(predicate::str::contains("Time (mean ± σ):     123.0 ms ±"));

    hyperfine_debug()
        .arg("--time-unit=millisecond")
        .arg("sleep 1.234")
        .assert()
        .success()
        .stdout(predicate::str::contains("Time (mean ± σ):     1234.0 ms ±"));

    hyperfine_debug()
        .arg("--time-unit=microsecond")
        .arg("sleep 1.234")
        .assert()
        .success()
        .stdout(predicate::str::contains(
            "Time (mean ± σ):     1234000.0 µs ±",
        ));
}

#[test]
fn performs_ten_runs_for_slow_commands() {
    hyperfine_debug()
        .arg("sleep 0.5")
        .assert()
        .success()
        .stdout(predicate::str::contains("10 runs"));
}

#[test]
fn performs_three_seconds_of_benchmarking_for_fast_commands() {
    hyperfine_debug()
        .arg("sleep 0.01")
        .assert()
        .success()
        .stdout(predicate::str::contains("300 runs"));
}

#[test]
fn takes_shell_spawning_time_into_account_for_computing_number_of_runs() {
    hyperfine_debug()
        .arg("--shell=sleep 0.02")
        .arg("sleep 0.01")
        .assert()
        .success()
        .stdout(predicate::str::contains("100 runs"));
}

#[test]
fn takes_preparation_command_into_account_for_computing_number_of_runs() {
    hyperfine_debug()
        .arg("--prepare=sleep 0.02")
        .arg("sleep 0.01")
        .assert()
        .success()
        .stdout(predicate::str::contains("100 runs"));

    // Shell overhead needs to be added to both the prepare command and the actual command,
    // leading to a total benchmark time of (prepare + shell + cmd + shell = 0.1 s)
    hyperfine_debug()
        .arg("--shell=sleep 0.01")
        .arg("--prepare=sleep 0.03")
        .arg("sleep 0.05")
        .assert()
        .success()
        .stdout(predicate::str::contains("30 runs"));
}

#[test]
fn takes_conclusion_command_into_account_for_computing_number_of_runs() {
    hyperfine_debug()
        .arg("--conclude=sleep 0.02")
        .arg("sleep 0.01")
        .assert()
        .success()
        .stdout(predicate::str::contains("100 runs"));

    // Shell overhead needs to be added to both the conclude command and the actual command,
    // leading to a total benchmark time of (cmd + shell + conclude + shell = 0.1 s)
    hyperfine_debug()
        .arg("--shell=sleep 0.01")
        .arg("--conclude=sleep 0.03")
        .arg("sleep 0.05")
        .assert()
        .success()
        .stdout(predicate::str::contains("30 runs"));
}

#[test]
fn takes_both_preparation_and_conclusion_command_into_account_for_computing_number_of_runs() {
    hyperfine_debug()
        .arg("--prepare=sleep 0.01")
        .arg("--conclude=sleep 0.01")
        .arg("sleep 0.01")
        .assert()
        .success()
        .stdout(predicate::str::contains("100 runs"));

    // Shell overhead needs to be added to both the prepare, conclude and the actual command,
    // leading to a total benchmark time of (prepare + shell + cmd + shell + conclude + shell = 0.1 s)
    hyperfine_debug()
        .arg("--shell=sleep 0.01")
        .arg("--prepare=sleep 0.01")
        .arg("--conclude=sleep 0.01")
        .arg("sleep 0.05")
        .assert()
        .success()
        .stdout(predicate::str::contains("30 runs"));
}

#[test]
fn shows_benchmark_comparison_with_relative_times() {
    hyperfine_debug()
        .arg("sleep 1.0")
        .arg("sleep 2.0")
        .arg("sleep 3.0")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("2.00 ± 0.00 times faster")
                .and(predicate::str::contains("3.00 ± 0.00 times faster")),
        );
}

#[test]
fn shows_benchmark_comparison_with_same_time() {
    hyperfine_debug()
        .arg("--command-name=A")
        .arg("--command-name=B")
        .arg("sleep 1.0")
        .arg("sleep 1.0")
        .arg("sleep 2.0")
        .arg("sleep 1000.0")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("As fast (1.00 ± 0.00) as")
                .and(predicate::str::contains("2.00 ± 0.00 times faster"))
                .and(predicate::str::contains("1000.00 ± 0.00 times faster")),
        );
}

#[test]
fn shows_benchmark_comparison_relative_to_reference() {
    hyperfine_debug()
        .arg("--reference=sleep 2.0")
        .arg("sleep 1.0")
        .arg("sleep 3.0")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("2.00 ± 0.00 times slower")
                .and(predicate::str::contains("1.50 ± 0.00 times faster")),
        );
}

#[test]
fn shows_reference_name() {
    hyperfine_debug()
        .arg("--reference=sleep 2.0")
        .arg("--reference-name=refabc123")
        .arg("sleep 1.0")
        .arg("sleep 3.0")
        .assert()
        .success()
        .stdout(predicate::str::contains("Benchmark 1: refabc123"));
}

#[test]
fn performs_all_benchmarks_in_parameter_scan() {
    hyperfine_debug()
        .arg("--parameter-scan")
        .arg("time")
        .arg("30")
        .arg("45")
        .arg("--parameter-step-size")
        .arg("5")
        .arg("sleep {time}")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("Benchmark 1: sleep 30")
                .and(predicate::str::contains("Benchmark 2: sleep 35"))
                .and(predicate::str::contains("Benchmark 3: sleep 40"))
                .and(predicate::str::contains("Benchmark 4: sleep 45"))
                .and(predicate::str::contains("Benchmark 5: sleep 50").not()),
        );
}

#[test]
fn performs_reference_and_all_benchmarks_in_parameter_scan() {
    hyperfine_debug()
        .arg("--reference=sleep 25")
        .arg("--parameter-scan")
        .arg("time")
        .arg("30")
        .arg("45")
        .arg("--parameter-step-size")
        .arg("5")
        .arg("sleep {time}")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("Benchmark 1: sleep 25")
                .and(predicate::str::contains("Benchmark 2: sleep 30"))
                .and(predicate::str::contains("Benchmark 3: sleep 35"))
                .and(predicate::str::contains("Benchmark 4: sleep 40"))
                .and(predicate::str::contains("Benchmark 5: sleep 45"))
                .and(predicate::str::contains("Benchmark 6: sleep 50").not()),
        );
}

#[test]
fn intermediate_results_are_not_exported_to_stdout() {
    hyperfine_debug()
        .arg("--style=none") // To only see the Markdown export on stdout
        .arg("--export-markdown")
        .arg("-")
        .arg("sleep 1")
        .arg("sleep 2")
        .assert()
        .success()
        .stdout(
            (predicate::str::contains("sleep 1").count(1))
                .and(predicate::str::contains("sleep 2").count(1)),
        );
}

#[test]
#[cfg(unix)]
fn exports_intermediate_results_to_file() {
    use tempfile::tempdir;

    let tempdir = tempdir().unwrap();
    let export_path = tempdir.path().join("results.md");

    hyperfine()
        .arg("--runs=1")
        .arg("--export-markdown")
        .arg(&export_path)
        .arg("true")
        .arg("false")
        .assert()
        .failure();

    let contents = std::fs::read_to_string(export_path).unwrap();
    assert!(contents.contains("true"));
}

#[test]
fn unused_parameters_are_shown_in_benchmark_name() {
    hyperfine()
        .arg("--runs=2")
        .arg("--parameter-list")
        .arg("branch")
        .arg("master,feature")
        .arg("echo test")
        .assert()
        .success()
        .stdout(
            predicate::str::contains("echo test (branch = master)")
                .and(predicate::str::contains("echo test (branch = feature)")),
        );
}

#[test]
fn speed_comparison_sort_order() {
    for sort_order in ["auto", "mean-time"] {
        hyperfine_debug()
            .arg("sleep 2")
            .arg("sleep 1")
            .arg(format!("--sort={sort_order}"))
            .assert()
            .success()
            .stdout(predicate::str::contains(
                "sleep 1 ran\n    2.00 ± 0.00 times faster than sleep 2",
            ));
    }

    hyperfine_debug()
        .arg("sleep 2")
        .arg("sleep 1")
        .arg("--sort=command")
        .assert()
        .success()
        .stdout(predicate::str::contains(
            "2.00 ±  0.00  sleep 2\n        1.00          sleep 1",
        ));
}

#[cfg(windows)]
#[test]
fn windows_quote_args() {
    hyperfine()
        .arg("more \"example_input_file.txt\"")
        .assert()
        .success();
}

#[cfg(windows)]
#[test]
fn windows_quote_before_quote_args() {
    hyperfine()
        .arg("dir \"..\\src\\\" \"..\\tests\\\"")
        .assert()
        .success();
}
```

