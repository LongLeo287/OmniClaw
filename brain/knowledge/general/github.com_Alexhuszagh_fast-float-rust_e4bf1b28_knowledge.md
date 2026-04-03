---
id: github.com-alexhuszagh-fast-float-rust-e4bf1b28-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:29.713591
---

# KNOWLEDGE EXTRACT: github.com_Alexhuszagh_fast-float-rust_e4bf1b28
> **Extracted on:** 2026-04-01 10:53:46
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521075/github.com_Alexhuszagh_fast-float-rust_e4bf1b28

---

## File: `.gitignore`
```
/target
**/target/
Cargo.lock
scratch/
.idea/
.DS_Store
corpus/
```

## File: `.gitmodules`
```
[submodule "extras/data-tests/ext"]
    path = extras/data-tests/ext
    url = https://github.com/lemire/fast_float_supplemental_tests.git

[submodule "extras/simple-bench/ext"]
    path = extras/simple-bench/ext
    url = https://github.com/lemire/simple_fastfloat_benchmark.git
```

## File: `CHANGELOG.md`
```markdown
## 0.2.2

- Fix `no_std` support.
- Remove most uses of unsafe.
- Remove non-local safety invariants to prevent unsoundness.

## 0.2.1

- Fix undefined behavior in checking the buffer length.

## 0.2.0

- Fixed an edge case where long decimals with trailing zeros were truncated.
- Minor micro-optimization fixes in the fast path parser.
- Remove the use of unsafe when querying power-of-10 tables.
- Added float64 roundtrip fuzz target.
- Added tests for the power-of-5 table using num-bigint.
- Improvements and new options in the bench tool.
- Updated benchmark timings, added Apple M1 and AMD Rome timings.

## 0.1.0

Initial release, fully tested and benchmarked.
```

## File: `Cargo.toml`
```
[package]
name = "fast-float2"
version = "0.2.3"
authors = ["Ivan Smirnov <i.s.smirnov@gmail.com>", "Alex Huszagh <ahuszagh@gmail.com>"]
repository = "https://github.com/Alexhuszagh/fast-float-rust"
documentation = "https://docs.rs/fast-float2"
description = "Fast floating-point number parser."
keywords = ["parser", "parsing", "parse", "float", "no-std"]
categories = ["parser-implementations", "parsing", "text-processing", "algorithms", "no-std"]
readme = "README.md"
license = "MIT OR Apache-2.0"
autobenches = false
edition = "2018"
exclude = [
    "benches/*",
    "extras/*",
    "clippy.toml",
    "rustfmt.toml",
    "SECURITY.md",
    ".git*",
]
# FIXME: rust-version is not supported until 1.56.0.
rust-version = "1.37"

[features]
default = ["std"]
std = []

[dev-dependencies]
lexical-core = "1.0.2"
hexf-parse = "0.2.1"
ryu = "1.0"
fastrand = "2.1.1"
num-bigint = "0.4.6"

[profile.release]
lto = "fat"
codegen-units = 1

[package.metadata.docs.rs]
features = ["std"]
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

Copyright 2021 Ivan Smirnov

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
Permission is hereby granted, free of charge, to any
person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the
Software without restriction, including without
limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
# fast-float2

[![Build](https://github.com/Alexhuszagh/fast-float-rust/workflows/CI/badge.svg)](https://github.com/Alexhuszagh/fast-float-rust/actions?query=branch%3Amaster)
[![Latest Version](https://img.shields.io/crates/v/fast-float2.svg)](https://crates.io/crates/fast-float2)
[![Documentation](https://docs.rs/fast-float2/badge.svg)](https://docs.rs/fast-float2)
[![Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Rustc 1.37+](https://img.shields.io/badge/rustc-1.37+-lightgray.svg)](https://blog.rust-lang.org/2019/08/15/Rust-1.37.0.html)

This crate provides a super-fast decimal number parser from strings into floats.

```toml
[dependencies]
fast-float2 = "0.2.3"
```

There are no dependencies and the crate can be used in a no_std context by disabling the "std" feature.

*Compiler support: rustc 1.37+.*

This crate is in maintenance mode for bug fixes (especially security patches): minimal feature enhancements will be accepted. This implementation has been adopted by the Rust standard library: if you do not need parsing directly from bytes and/or partial parsers, you should use [FromStr](https://doc.rust-lang.org/std/str/trait.FromStr.html) for [f32](https://doc.rust-lang.org/std/primitive.f32.html) or [f64](https://doc.rust-lang.org/std/primitive.f64.html) instead.

## Usage

There's two top-level functions provided:
[`parse()`](https://docs.rs/fast-float/latest/fast_float/fn.parse.html) and
[`parse_partial()`](https://docs.rs/fast-float/latest/fast_float/fn.parse_partial.html), both taking
either a string or a bytes slice and parsing the input into either `f32` or `f64`:

- `parse()` treats the whole string as a decimal number and returns an error if there are
  invalid characters or if the string is empty.
- `parse_partial()` tries to find the longest substring at the beginning of the given input
  string that can be parsed as a decimal number and, in the case of success, returns the parsed
  value along the number of characters processed; an error is returned if the string doesn't
  start with a decimal number or if it is empty. This function is most useful as a building
  block when constructing more complex parsers, or when parsing streams of data.

Example:

```rust
// Parse the entire string as a decimal number.
let s = "1.23e-02";
let x: f32 = fast_float2::parse(s).unwrap();
assert_eq!(x, 0.0123);

// Parse as many characters as possible as a decimal number.
let s = "1.23e-02foo";
let (x, n) = fast_float2::parse_partial::<f32, _>(s).unwrap();
assert_eq!(x, 0.0123);
assert_eq!(n, 8);
assert_eq!(&s[n..], "foo");
```

## Details

This crate is a direct port of Daniel Lemire's [`fast_float`](https://github.com/fastfloat/fast_float)
C++ library (valuable discussions with Daniel while porting it helped shape the crate and get it to
the performance level it's at now), with some Rust-specific tweaks. Please see the original
repository for many useful details regarding the algorithm and the implementation.

The parser is locale-independent. The resulting value is the closest floating-point values (using either
`f32` or `f64`), using the "round to even" convention for values that would otherwise fall right in-between
two values. That is, we provide exact parsing according to the IEEE standard.

Infinity and NaN values can be parsed, along with scientific notation.

Both little-endian and big-endian platforms are equally supported, with extra optimizations enabled
on little-endian architectures.

Since [fast-float-rust](https://github.com/aldanor/fast-float-rust) is unmaintained, this is a fork
containing the patches and security updates.

## Testing

There are a few ways this crate is tested:

- A suite of explicit tests (taken from the original library) covering lots of edge cases.
- A file-based test suite (taken from the original library; credits to Nigel Tao), ~5M tests.
- All 4B float32 numbers are exhaustively roundtripped via ryu formatter.
- Roundtripping a large quantity of random float64 numbers via ryu formatter.
- Roundtripping float64 numbers and fuzzing random input strings via cargo-fuzz.
- All explicit test suites run on CI; roundtripping and fuzzing are run manually.

## Performance

The presented parser seems to beat all of the existing C/C++/Rust float parsers known to us at the
moment by a large margin, in all of the datasets we tested it on so far – see detailed benchmarks
below (the only exception being the original fast_float C++ library, of course – performance of
which is within noise bounds of this crate). On modern machines like Apple M1, parsing throughput
can reach up to 1.5 GB/s.

While various details regarding the algorithm can be found in the repository for the original
C++ library, here are few brief notes:

- The parser is specialized to work lightning-fast on inputs with at most 19 significant digits
  (which constitutes the so called "fast-path"). We believe that most real-life inputs should
  fall under this category, and we treat longer inputs as "degenerate" edge cases since it
  inevitable causes overflows and loss of precision.
- If the significand happens to be longer than 19 digits, the parser falls back to the "slow path",
  in which case its performance roughly matches that of the top Rust/C++ libraries (and still
  beats them most of the time, although not by a lot).
- On little-endian systems, there's additional optimizations for numbers with more than 8 digits
  after the decimal point.

## Benchmarks

Below are tables of best timings in nanoseconds for parsing a single number into a 64-bit float (using the median score, lower is better).

<!--

Not all C++ benchmarks report ns/float, which we use for our benches.
You can convert from MFloat/s to ns/float with:

```python
mfloat_to_ns = lambda x: 1e9 / x / 1e6
```

-->

### Intel i7-14700K

- CPU: Intel i7-14700K 3.40GHz
- OS: Ubuntu 24.04 (WSL2)
- Rust: 1.81
- C++: GCC 13.2.0

|                        | `canada` | `mesh`   | `uniform` | `bi`   | `iei`  | `rec32` |
| ---------------------- | -------- | -------- | --------- | ------ | ------ | ------- |
| fast-float2            | 9.98     | 5.56     | 10.08     | 56.19  | 14.52  | 15.09   |
| fast-float             | 9.77     | 5.04     | 9.05      | 57.52  | 14.40  | 14.23   |
| lexical                | 10.62    | 4.93     | 9.92      | 26.40  | 12.43  | 14.40   |
| from_str               | 11.59    | 5.92     | 11.23     | 35.92  | 14.75  | 16.76   |
| fast_float (C++)       | 12.58    | 6.35     | 11.86     | 31.55  | 12.22  | 11.97   |
| abseil (C++)           | 25.32    | 15.70    | 25.88     | 43.42  | 23.54  | 26.75   |
| netlib (C)             | 35.10    | 10.22    | 37.72     | 68.63  | 23.07  | 38.23   |
| strtod (C)             | 52.63    | 26.47    | 46.51     | 88.11  | 33.37  | 53.36   |
| doubleconversion (C++) | 32.50    | 14.69    | 47.80     | 70.01  | 205.72 | 45.66   |

### AMD EPYC 7763 64-Core Processor (Linux)

- CPU: AMD EPYC 7763 64-Core Processor 3.20GHz
- OS: Ubuntu 24.04.1
- Rust: 1.83
- C++: GCC 13.2.0
- Environment: Github Actions (2.321.0)

|                        | `canada` | `mesh`   | `uniform` | `bi`   | `iei`  | `rec32` |
| ---------------------- | -------- | -------- | --------- | ------ | ------ | ------- |
| fast-float2            | 19.83    | 10.42    | 18.64     | 80.03  | 26.12  | 27.70   |
| fast-float             | 19.17    | 9.89     | 17.34     | 82.37  | 25.26  | 27.22   |
| lexical                | 18.89    | 8.41     | 16.83     | 47.66  | 22.08  | 26.99   |
| from_str               | 22.90    | 12.72    | 22.10     | 62.20  | 27.51  | 30.80   |
| fast_float (C++)       | 20.71    | 10.72    | 24.63     | 82.85  | 24.24  | 19.60   |
| abseil (C++)           | 31.03    | 23.78    | 32.82     | 76.05  | 28.41  | 35.03   |
| netlib (C)             | 54.22    | 20.12    | 68.68     | 82.64  | 32.81  | 69.43   |
| strtod (C)             | 100.10   | 52.08    | 85.32     | 192.31 | 75.08  | 97.85   |
| doubleconversion (C++) | 75.13    | 31.98    | 87.64     | 170.06 | 124.69 | 87.26   |

### AMD EPYC 7763 64-Core Processor (Windows)

- CPU: AMD EPYC 7763 64-Core Processor 3.20GHz
- OS: Windows Server 2022 (10.0.20348)
- Rust: 1.83
- C++: MSVC 19.42.34435.0
- Environment: Github Actions (2.321.0)

|                        | `canada` | `mesh`   | `uniform` | `bi`   | `iei`  | `rec32` |
| ---------------------- | -------- | -------- | --------- | ------ | ------ | ------- |
| fast-float2            | 20.92    | 10.02    | 19.34     | 94.37  | 27.09  | 30.84   |
| fast-float             | 19.72    | 9.65     | 18.46     | 86.85  | 25.75  | 30.05   |
| lexical                | 19.15    | 8.80     | 17.92     | 51.14  | 22.16  | 28.34   |
| from_str               | 25.93    | 13.49    | 23.36     | 78.82  | 27.80  | 35.58   |
| fast_float (C++)       | 64.89    | 47.46    | 64.40     | 104.36 | 55.44  | 69.29   |
| abseil (C++)           | 37.77    | 33.10    | 41.24     | 136.86 | 37.11  | 47.32   |
| netlib (C)             | 53.76    | 28.78    | 60.96     | 76.35  | 44.33  | 62.96   |
| strtod (C)             | 181.47   | 85.95    | 192.35    | 262.81 | 125.37 | 204.94  |
| doubleconversion (C++) | 119.02   | 28.78    | 128.16    | 232.35 | 110.97 | 129.63  |

### Apple M1 (macOS)

- CPU: AMD EPYC 7763 64-Core Processor 3.20GHz
- OS: macOS (14.7.1)
- Rust: 1.83
- C++: Clang (Apple) 15.0.0.15000309
- Environment: Github Actions

|                        | `canada` | `mesh`   | `uniform` | `bi`   | `iei`  | `rec32` |
| ---------------------- | -------- | -------- | --------- | ------ | ------ | ------- |
| fast-float2            | 15.47    | 6.54     | 11.62     | 94.35  | 20.55  | 17.78   |
| fast-float             | 14.56    | 6.40     | 11.09     | 92.89  | 21.19  | 17.06   |
| lexical                | 14.13    | 6.55     | 11.96     | 35.99  | 15.93  | 18.91   |
| from_str               | 17.67    | 7.93     | 13.88     | 58.60  | 19.68  | 19.92   |
| fast_float (C++)       | 17.42    | 10.40    | 15.14     | 87.33  | 21.82  | 14.53   |
| abseil (C++)           | 20.94    | 17.31    | 22.50     | 63.86  | 24.69  | 25.19   |
| netlib (C)             | 45.05    | 13.79    | 52.38     | 156.25 | 36.10  | 51.36   |
| strtod (C)             | 25.88    | 14.25    | 27.08     | 85.32  | 23.03  | 26.86   |
| doubleconversion (C++) | 53.39    | 21.50    | 73.15     | 120.63 | 52.88  | 70.47   |

Note that the random number generation seems to differ between C/C++ and Rust, since the Rust implementations are slightly faster for pre-determined datasets like `canada` and `mesh`, but equivalent random number generators are slightly slower. Any performance penalty with `fast-float2` occurred due to fixing the UB in [check_len](https://github.com/aldanor/fast-float-rust/issues/28). The massive performance differences between `fast-float` (Rust) and `fast_float` (C++) are expected due to a faster fallback algorithms ([#96](https://github.com/fastfloat/fast_float/pull/96) and [#104](https://github.com/fastfloat/fast_float/pull/104)) used in these cases.

#### Parsers

- `fast-float2` - this very crate
- `fast-float` - the pre-ported variant
- `lexical` – `lexical_core`, v1.0.05
- `from_str` – Rust standard library, `FromStr` trait
- `fast_float (C++)` – original C++ implementation of 'fast-float' method
- `abseil (C++)` – Abseil C++ Common Libraries
- `netlib (C++)` – C++ Network Library
- `strtod (C)` – C standard library

#### Datasets

- `canada` – numbers in `canada.txt` file
- `mesh` – numbers in `mesh.txt` file
- `uniform` – uniform random numbers from 0 to 1
- `bi` – large, integer-only floats <!-- `big_ints` -- >
- `int_e_int` – random numbers of format `%de%d` <!-- `int_e_int` -->
- `rec32` – reciprocals of random 32-bit integers <!-- `one_over_rand32` -->

#### Notes

- The two test files referred above can be found in
[this](https://github.com/lemire/simple_fastfloat_benchmark) repository.
- The Rust part of the table (along with a few other benchmarks) can be generated via
  the benchmark tool that can be found under `extras/simple-bench` of this repo.
- The C/C++ part of the table (along with a few other benchmarks and parsers) can be
  generated via a C++ utility that can be found in
  [this](https://github.com/lemire/simple_fastfloat_benchmark) repository.

<br>

#### References

- Daniel Lemire, [Number Parsing at a Gigabyte per Second](https://arxiv.org/abs/2101.11408), Software: Practice and Experience 51 (8), 2021.

#### License

<sup>
Licensed under either of <a href="LICENSE-APACHE">Apache License, Version
2.0</a> or <a href="LICENSE-MIT">MIT license</a> at your option.
</sup>

<br>

<sub>
Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in this crate by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.
</sub>
```

## File: `SECURITY.md`
```markdown
# Security Policy

This crate is in maintenance mode, so only the latest version is supported and will be receiving bug fixes. If you have a security vulnerability, please reach out to me privately at [ahuszagh@gmail.com](mailto:ahuszagh@gmail.com). Other forms of communication may not reach me.
```

## File: `clippy.toml`
```
avoid-breaking-exported-api = false
disallowed-macros = [
    # Can also use an inline table with a `path` key.
    { path = "std::print", reason = "no IO allowed" },
    { path = "std::println", reason = "no IO allowed" },
    { path = "std::format", reason = "no string allocation allowed" },
    { path = "std::debug", reason = "debugging macros should not be present in any release" },
    # NOTE: unimplemented is fine because this can be for intentionally disabled methods
    { path = "std::todo", reason = "should never have TODO macros in releases" },
]
disallowed-methods = [
    { path = "std::io::stdout", reason = "no IO allowed" },
    { path = "std::io::stdin", reason = "no IO allowed" },
    { path = "std::io::stderr", reason = "no IO allowed" },
]
disallowed-types = [
    { path = "std::io::File", reason = "no IO allowed" },
    { path = "std::io::BufReader", reason = "need our own abstractions for reading/writing" },
    { path = "std::io::BufWriter", reason = "need our own abstractions for reading/writing" },
]
```

## File: `rustfmt.toml`
```
# Requires nightly to do proper formatting.
use_small_heuristics = "Off"
use_field_init_shorthand = true
trailing_semicolon = true
newline_style = "Unix"
match_block_trailing_comma = true
empty_item_single_line = false
enum_discrim_align_threshold = 40
fn_params_layout = "Tall"
fn_single_line = false
format_macro_matchers = true
format_macro_bodies = true
imports_indent = "Block"
imports_layout = "HorizontalVertical"
indent_style = "Block"
match_arm_blocks = true
overflow_delimited_expr = true
group_imports = "StdExternalCrate"
wrap_comments = true
```

## File: `extras/data-tests/Cargo.toml`
```
[package]
name = "fast-float-data-tests"
version = "0.1.0"
authors = ["Ivan Smirnov <i.s.smirnov@gmail.com>"]
edition = "2018"
readme = "README.md"
license = "MIT OR Apache-2.0"
publish = false

[dependencies]
fast-float2 = { path = "../.." }
```

## File: `extras/data-tests/README.md`
```markdown
This crate allows running the test based on files with test cases stored in the
standardized format (credit to Daniel Lemire and Nigel Tao for the test cases).
The test data is sourced from [this](https://github.com/lemire/fast_float_supplemental_tests) 
repository which is used for the original fast_float C++ library tests.

Test data files can be found under `ext/data`.

To run the tests:

```sh
cargo run --release
```
```

## File: `extras/data-tests/src/main.rs`
```rust
use std::fs::{read_dir, File};
use std::io::{BufRead, BufReader};
use std::mem::transmute;
use std::path::{Path, PathBuf};

#[derive(Clone, Debug)]
struct TestCase {
    float32: f32,
    float64: f64,
    string: String,
}

impl TestCase {
    pub fn parse(string: String) -> Self {
        let float32 = unsafe { transmute(u32::from_str_radix(&string[5..13], 16).unwrap()) };
        let float64 = unsafe { transmute(u64::from_str_radix(&string[14..30], 16).unwrap()) };
        let string = string[31..].to_string();
        Self {
            float32,
            float64,
            string,
        }
    }

    fn execute_one<F: fast_float2::FastFloat>(&self, expected: F) {
        let r = F::parse_float_partial(&self.string);
        if !r.is_ok() {
            dbg!(self);
            eprintln!("Failed to parse as f32: {:?}", self.string);
        }
        let (value, len) = r.unwrap();
        if len != self.string.len() || value != expected {
            if len != self.string.len() {
                eprintln!("Expected empty string remainder, got: {:?}", self.string.len() - len);
            }
            if value != expected {
                eprintln!("Expected output {}, got {}", expected, value);
            }
            panic!("Test case failed: {:?}", self);
        }
    }

    pub fn execute(&self) {
        self.execute_one::<f32>(self.float32);
        self.execute_one::<f64>(self.float64);
    }
}

fn parse_test_file(filename: impl AsRef<Path>) -> impl Iterator<Item = TestCase> {
    let file = File::open(filename).unwrap();
    BufReader::new(file).lines().map(Result::unwrap).map(TestCase::parse)
}

fn run_test_cases(filename: impl AsRef<Path>) -> usize {
    parse_test_file(filename).map(|test| test.execute()).count()
}

fn test_file_paths() -> Vec<PathBuf> {
    let test_data_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("ext/data");
    let mut paths = read_dir(&test_data_dir)
        .unwrap()
        .map(|d| d.unwrap().path())
        .filter(|p| {
            p.is_file()
                && p.extension().map(|e| e.to_str()) == Some(Some("txt"))
                && p.file_name().map(|f| f.to_str()) != Some(Some("CMakeLists.txt"))
        })
        .collect::<Vec<_>>();
    paths.sort();
    paths
}

fn main() {
    for path in &test_file_paths() {
        eprint!("Running test cases in {:?}... ", path.file_name().unwrap());
        let count = run_test_cases(path);
        eprintln!("{} tests passed.", count);
    }
}
```

## File: `extras/simple-bench/Cargo.toml`
```
[package]
name = "fast-float-simple-bench"
version = "0.1.0"
authors = ["Ivan Smirnov <i.s.smirnov@gmail.com>"]
edition = "2018"
readme = "README.md"
license = "MIT OR Apache-2.0"
publish = false

[dependencies]
fast-float2 = { path = "../.." }
anyhow = "1.0"
lexical = "7.0.4"
lexical-core = "1.0.5"
fastrand = "2.1.1"
fast-float = "0.2"
clap = { version = "4.5.23", features = ["derive"] }
```

## File: `extras/simple-bench/README.md`
```markdown
This crate provides a utility for benchmarking the `fast-float2` crate against
`lexical_core` and standard library's `FromStr`.

To run a file-based test:

```sh
cargo run --release -- file ext/data/canada.txt
```

There's two files used in benchmarking of the original fast_float C++ library
(canada.txt and mesh.txt), they are sourced from
[this](https://github.com/lemire/simple_fastfloat_benchmark) repository. These
files can be found under `ext/data`.

To run a randomized test:

```sh
cargo run --release -- random uniform
```

For more details and options (choosing a different random generator, storing
randomized inputs to a file, changing the number of runs, or switching between
32-bit and 64-bit floats), refer to help:

```
cargo run --release -- --help
```
```

## File: `extras/simple-bench/src/main.rs`
```rust
mod random;

use std::fs;
use std::iter;
use std::path::{Path, PathBuf};
use std::str::FromStr;
use std::time::Instant;

use clap::Parser;
use fast_float2::FastFloat;
use fastrand::Rng;
use lexical::FromLexical;
use random::RandomGen;
//use structopt::StructOpt;

#[derive(Parser, Debug)]
#[command(name = "fast-float-simple-bench", about = "fast-float benchmark utility")]
struct Opt {
    /// Parse numbers as float32 (default is float64)
    #[arg(short, long = "32")]
    float32: bool,

    /// How many times to repeat parsing
    #[arg(short, long, default_value = "1000")]
    repeat: usize,

    /// Only run fast-float benches
    #[arg(short, long, default_value = "false")]
    only_fast_float: bool,

    #[command(subcommand)]
    command: Cmd,
}

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
enum Cmd {
    /// Read the floats from file
    File {
        /// Input file (one number per line)
        #[arg(value_parser)]
        filename: PathBuf,
    },

    /// Generate random floats in (0, 1]
    Random {
        /// Random generator to be used
        #[arg(
            value_enum,
            default_value = "uniform",
            //possible_values = RandomGen::variants()
        )]
        gen: RandomGen,

        /// Number of random floats generated
        #[arg(short = 'n', default_value = "50000")]
        count: usize,

        /// Random generator seed
        #[arg(short, default_value = "0")]
        seed: u64,

        /// Also save the generated inputs to file
        #[arg(value_parser, short = 'f')]
        filename: Option<PathBuf>,
    },

    /// Run all benchmarks for fast-float only
    All {
        /// Number of random floats generated
        #[structopt(short = 'n', default_value = "50000")]
        count: usize,

        /// Random generator seed
        #[structopt(short, default_value = "0")]
        seed: u64,
    },
}

#[derive(Debug, Clone)]
struct BenchResult {
    pub name: String,
    pub times: Vec<i64>,
    pub count: usize,
    pub bytes: usize,
}

fn black_box<T>(dummy: T) -> T {
    unsafe {
        let ret = core::ptr::read_volatile(&dummy);
        core::mem::forget(dummy);
        ret
    }
}

fn run_bench<T: FastFloat, F: Fn(&str) -> T>(
    inputs: &[String],
    repeat: usize,
    func: F,
) -> Vec<i64> {
    const WARMUP: usize = 1000;
    let mut times = Vec::with_capacity(repeat + WARMUP);
    for _ in 0..repeat + WARMUP {
        let t0 = Instant::now();
        for input in inputs {
            black_box(func(input.as_str()));
        }
        times.push(t0.elapsed().as_nanos() as _);
    }
    times.split_at(WARMUP).1.into()
}

#[derive(Debug, Copy, Clone, Eq, PartialEq)]
enum Method {
    FastFloat,
    FastFloat2,
    Lexical,
    FromStr,
}

fn type_str(float32: bool) -> &'static str {
    if float32 {
        "f32"
    } else {
        "f64"
    }
}

impl Method {
    pub fn name(&self) -> &'static str {
        match self {
            Self::FastFloat2 => "fast-float2",
            Self::FastFloat => "fast-float",
            Self::Lexical => "lexical",
            Self::FromStr => "from_str",
        }
    }

    fn run_as<T: FastFloat + fast_float::FastFloat + FromLexical + FromStr>(
        &self,
        input: &Input,
        repeat: usize,
        name: &str,
    ) -> BenchResult {
        let data = &input.data;
        let times = match self {
            Self::FastFloat2 => run_bench(data, repeat, |s: &str| {
                fast_float2::parse_partial::<T, _>(s).unwrap_or_default().0
            }),
            Self::FastFloat => run_bench(data, repeat, |s: &str| {
                fast_float::parse_partial::<T, _>(s).unwrap_or_default().0
            }),
            Self::Lexical => run_bench(data, repeat, |s: &str| {
                lexical_core::parse_partial::<T>(s.as_bytes()).unwrap_or_default().0
            }),
            Self::FromStr => run_bench(data, repeat, |s: &str| s.parse::<T>().unwrap_or_default()),
        };

        BenchResult {
            times,
            name: name.into(),
            count: input.count(),
            bytes: input.bytes(),
        }
    }

    pub fn run(&self, input: &Input, repeat: usize, name: &str, float32: bool) -> BenchResult {
        if float32 {
            self.run_as::<f32>(input, repeat, name)
        } else {
            self.run_as::<f64>(input, repeat, name)
        }
    }

    pub fn all() -> &'static [Self] {
        &[Method::FastFloat2, Method::FastFloat, Method::Lexical, Method::FromStr]
    }
}

fn print_report(results: &[BenchResult], title: &str) {
    let width = 81;
    println!("{:=<width$}", "", width = width + 4);
    println!("| {:^width$} |", title, width = width);
    println!("|{:=<width$}|", "", width = width + 2);
    print_table("ns/float", results, width, |t, n, _| t as f64 / n as f64);
    print_table("Mfloat/s", results, width, |t, n, _| 1e3 * n as f64 / t as f64);
    print_table("MB/s", results, width, |t, _, b| b as f64 * 1e9 / 1024. / 1024. / t as f64);
    println!("|{:width$}|", "", width = width + 2);
    println!("{:=<width$}", "", width = width + 4);
}

fn print_table(
    heading: &str,
    results: &[BenchResult],
    width: usize,
    transform: impl Fn(i64, usize, usize) -> f64,
) {
    let repeat = results[0].times.len();
    let columns = &[
        ("min", 0),
        ("5%", repeat / 20),
        ("25%", repeat / 4),
        ("median", repeat / 2),
        ("75%", (3 * repeat) / 4),
        ("95%", (19 * repeat) / 20),
        ("max", repeat - 1),
    ];
    let w = 9;
    let h = width - 7 * w;

    println!("|{:width$}|", "", width = width + 2);
    print!("| {:<h$}", heading, h = h);
    for (name, _) in columns {
        print!("{:>w$}", name, w = w);
    }
    println!(" |");
    println!("|{:-<width$}|", "", width = width + 2);
    for res in results {
        print!("| {:<h$}", res.name, h = h);
        let (n, b) = (res.count, res.bytes);
        let mut metrics = res.times.iter().map(|&t| transform(t, n, b)).collect::<Vec<_>>();
        metrics.sort_by(|a, b| a.partial_cmp(b).unwrap());
        for &(_, idx) in columns {
            print!("{:>w$.2}", metrics[idx], w = w);
        }
        println!(" |");
    }
}

struct Input {
    pub data: Vec<String>,
    pub name: String,
}

impl Input {
    pub fn from_file(filename: impl AsRef<Path>) -> Self {
        let filename = filename.as_ref();
        let data =
            fs::read_to_string(&filename).unwrap().trim().lines().map(String::from).collect();
        let name = filename.file_name().unwrap().to_str().unwrap().into();
        Self {
            data,
            name,
        }
    }

    pub fn from_random(gen: RandomGen, count: usize, seed: u64) -> Self {
        let mut rng = Rng::with_seed(seed);
        let data = iter::repeat_with(|| gen.gen(&mut rng)).take(count).collect();
        let name = format!("{}", gen);
        Self {
            data,
            name,
        }
    }

    pub fn count(&self) -> usize {
        self.data.len()
    }

    pub fn bytes(&self) -> usize {
        self.data.iter().map(|s| s.len()).sum()
    }

    pub fn title(&self, float32: bool) -> String {
        format!(
            "{} ({}, {:.2} MB, {})",
            self.name,
            self.count(),
            self.bytes() as f64 / 1024. / 1024.,
            type_str(float32),
        )
    }
}

fn main() {
    let opt = Opt::parse();

    let methods = if !opt.only_fast_float && !matches!(&opt.command, &Cmd::All { .. }) {
        Method::all().into()
    } else {
        vec![Method::FastFloat2]
    };

    let inputs = match opt.command {
        Cmd::File {
            filename,
        } => vec![Input::from_file(filename)],
        Cmd::Random {
            gen,
            count,
            seed,
            filename,
        } => {
            let input = Input::from_random(gen, count, seed);
            if let Some(filename) = filename {
                fs::write(filename, input.data.join("\n")).unwrap();
            }
            vec![input]
        },
        Cmd::All {
            count,
            seed,
        } => {
            let mut inputs = vec![];
            let data_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("ext/data");
            inputs.push(Input::from_file(data_dir.join("mesh.txt")));
            inputs.push(Input::from_file(data_dir.join("canada.txt")));
            for &gen in RandomGen::all() {
                inputs.push(Input::from_random(gen, count, seed))
            }
            inputs
        },
    };

    let mut results = vec![];
    for input in &inputs {
        for method in &methods {
            let name = if inputs.len() == 1 {
                method.name()
            } else {
                &input.name
            };
            results.push(method.run(input, opt.repeat.max(1), name, opt.float32));
        }
    }

    let title = if inputs.len() == 1 {
        inputs[0].title(opt.float32)
    } else {
        format!("fast-float (all, {})", type_str(opt.float32))
    };
    print_report(&results, &title);
}
```

## File: `extras/simple-bench/src/random.rs`
```rust
use std::fmt::{self, Display};
use std::str::FromStr;

use anyhow::{bail, Error, Result};
use fastrand::Rng;

#[derive(Copy, Clone, Debug, PartialEq, Eq)]
pub enum RandomGen {
    Uniform,
    OneOverRand32,
    SimpleUniform32,
    SimpleInt32,
    IntEInt,
    SimpleInt64,
    BigIntDotInt,
    BigInts,
}

impl Display for RandomGen {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Self::Uniform => write!(f, "uniform"),
            Self::OneOverRand32 => write!(f, "one_over_rand32"),
            Self::SimpleUniform32 => write!(f, "simple_uniform32"),
            Self::SimpleInt32 => write!(f, "simple_int32"),
            Self::IntEInt => write!(f, "int_e_int"),
            Self::SimpleInt64 => write!(f, "simple_int64"),
            Self::BigIntDotInt => write!(f, "bigint_int_dot_int"),
            Self::BigInts => write!(f, "big_ints"),
        }
    }
}

impl FromStr for RandomGen {
    type Err = Error;

    fn from_str(s: &str) -> Result<Self> {
        Ok(match s {
            "uniform" => Self::Uniform,
            "one_over_rand32" => Self::OneOverRand32,
            "simple_uniform32" => Self::SimpleUniform32,
            "simple_int32" => Self::SimpleInt32,
            "int_e_int" => Self::IntEInt,
            "simple_int64" => Self::SimpleInt64,
            "bigint_int_dot_int" => Self::BigIntDotInt,
            "big_ints" => Self::BigInts,
            _ => bail!("Invalid random generator: {:?}", s),
        })
    }
}

impl RandomGen {
    pub fn all() -> &'static [Self] {
        &[
            Self::Uniform,
            Self::OneOverRand32,
            Self::SimpleUniform32,
            Self::SimpleInt32,
            Self::IntEInt,
            Self::SimpleInt64,
            Self::BigIntDotInt,
            Self::BigInts,
        ]
    }

    pub fn gen(&self, rng: &mut Rng) -> String {
        match self {
            Self::Uniform
            | Self::OneOverRand32
            | Self::SimpleUniform32
            | Self::SimpleInt32
            | Self::SimpleInt64 => lexical::to_string(match self {
                Self::Uniform => rng.f64(),
                Self::OneOverRand32 => 1. / rng.u32(1..) as f64,
                Self::SimpleUniform32 => rng.u32(..) as f64 / u32::MAX as f64,
                Self::SimpleInt32 => rng.u32(..) as f64,
                Self::SimpleInt64 => rng.u64(..) as f64,
                _ => unreachable!(),
            }),
            Self::IntEInt => format!("{}e{}", rng.u32(..), rng.u32(..99)),
            Self::BigInts => format!("{}{}{}", rng.u64(..), rng.u64(..), rng.u64(..)),
            Self::BigIntDotInt => format!("{}.{}", rng.u32(..), rng.u32(..)),
        }
    }
}
```

## File: `fuzz/Cargo.toml`
```
[package]
name = "fast-float-fuzz"
version = "0.1.0"
authors = ["Ivan Smirnov <i.s.smirnov@gmail.com>"]
edition = "2018"
publish = false

[package.metadata]
cargo-fuzz = true

[workspace]
members = ["."]

[dependencies]
fast-float2 = { path = ".." }
libfuzzer-sys = "0.4.7"
ryu = "1.0"

[[bin]]
name = "fast_float"
path = "fuzz_targets/fast_float.rs"
test = false
doc = false

[[bin]]
name = "roundtrip_f64"
path = "fuzz_targets/roundtrip_f64.rs"
test = false
doc = false
```

## File: `fuzz/float.dict`
```
"0"
"1"
"2"
"3"
"4"
"5"
"6"
"7"
"8"
"9"
"."
"-"
"+"
"e"
"E"
```

## File: `fuzz/fuzz_targets/fast_float.rs`
```rust
#![no_main]

use libfuzzer_sys::fuzz_target;

fn black_box<T>(dummy: T) -> T {
    unsafe {
        let ret = core::ptr::read_volatile(&dummy);
        core::mem::forget(dummy);
        ret
    }
}

fuzz_target!(|data: &[u8]| {
    let _ = black_box(::fast_float2::parse::<f32, _>(data));
    let _ = black_box(::fast_float2::parse::<f64, _>(data));
});
```

## File: `fuzz/fuzz_targets/roundtrip_f64.rs`
```rust
#![no_main]
use libfuzzer_sys::fuzz_target;

// We only test the roundtrip of f64 with a fuzzer because f32 search space
// is small enough that we can test it exhaustively

fn check_roundtrip(float: f64, string: impl AsRef<str>) {
    let result = ::fast_float2::parse::<f64, _>(string.as_ref()).unwrap();
    if float.is_nan() {
        assert!(result.is_nan());
    } else {
        assert_eq!(float, result);
    }
}

fuzz_target!(|float: f64| {
    // we use both ryu and stdlib since ryu prefers scientific notation while stdlib
    // never uses it at all; hence more code paths will be executed
    let mut buf = ryu::Buffer::new();
    check_roundtrip(float, buf.format(float));
    check_roundtrip(float, float.to_string());
});
```

## File: `src/binary.rs`
```rust
use crate::common::AdjustedMantissa;
use crate::float::Float;
use crate::table::{LARGEST_POWER_OF_FIVE, POWER_OF_FIVE_128, SMALLEST_POWER_OF_FIVE};

#[inline]
pub fn compute_float<F: Float>(q: i64, mut w: u64) -> AdjustedMantissa {
    let am_zero = AdjustedMantissa::zero_pow2(0);
    let am_inf = AdjustedMantissa::zero_pow2(F::INFINITE_POWER);
    let am_error = AdjustedMantissa::zero_pow2(-1);

    if w == 0 || q < F::SMALLEST_POWER_OF_TEN as i64 {
        return am_zero;
    } else if q > F::LARGEST_POWER_OF_TEN as i64 {
        return am_inf;
    }
    let lz = w.leading_zeros();
    w <<= lz;
    let (lo, hi) = compute_product_approx(q, w, F::MANTISSA_EXPLICIT_BITS + 3);
    if lo == 0xFFFF_FFFF_FFFF_FFFF {
        let inside_safe_exponent = (-27..=55).contains(&q);
        if !inside_safe_exponent {
            return am_error;
        }
    }
    let upperbit = (hi >> 63) as i32;
    let mut mantissa = hi >> (upperbit + 64 - F::MANTISSA_EXPLICIT_BITS as i32 - 3);
    let mut power2 = power(q as i32) + upperbit - lz as i32 - F::MINIMUM_EXPONENT;
    if power2 <= 0 {
        if -power2 + 1 >= 64 {
            return am_zero;
        }
        mantissa >>= -power2 + 1;
        mantissa += mantissa & 1;
        mantissa >>= 1;
        power2 = (mantissa >= (1_u64 << F::MANTISSA_EXPLICIT_BITS)) as i32;
        return AdjustedMantissa {
            mantissa,
            power2,
        };
    }
    if lo <= 1
        && q >= F::MIN_EXPONENT_ROUND_TO_EVEN as i64
        && q <= F::MAX_EXPONENT_ROUND_TO_EVEN as i64
        && mantissa & 3 == 1
        && (mantissa << (upperbit + 64 - F::MANTISSA_EXPLICIT_BITS as i32 - 3)) == hi
    {
        mantissa &= !1_u64;
    }
    mantissa += mantissa & 1;
    mantissa >>= 1;
    if mantissa >= (2_u64 << F::MANTISSA_EXPLICIT_BITS) {
        mantissa = 1_u64 << F::MANTISSA_EXPLICIT_BITS;
        power2 += 1;
    }
    mantissa &= !(1_u64 << F::MANTISSA_EXPLICIT_BITS);
    if power2 >= F::INFINITE_POWER {
        return am_inf;
    }
    AdjustedMantissa {
        mantissa,
        power2,
    }
}

#[inline]
fn power(q: i32) -> i32 {
    (q.wrapping_mul(152_170 + 65536) >> 16) + 63
}

#[inline]
fn full_multiplication(a: u64, b: u64) -> (u64, u64) {
    let r = (a as u128) * (b as u128);
    (r as u64, (r >> 64) as u64)
}

// This will compute or rather approximate w * 5**q and return a pair of 64-bit
// words approximating the result, with the "high" part corresponding to the
// most significant bits and the low part corresponding to the least significant
// bits.
#[inline]
fn compute_product_approx(q: i64, w: u64, precision: usize) -> (u64, u64) {
    debug_assert!(q >= SMALLEST_POWER_OF_FIVE as i64);
    debug_assert!(q <= LARGEST_POWER_OF_FIVE as i64);
    debug_assert!(precision <= 64);

    let mask = if precision < 64 {
        0xFFFF_FFFF_FFFF_FFFF_u64 >> precision
    } else {
        0xFFFF_FFFF_FFFF_FFFF_u64
    };
    let index = (q - SMALLEST_POWER_OF_FIVE as i64) as usize;
    // NOTE: this cannot be ellided by the compiler, but the proof the index
    // must be within the bounds is non-trivial, especially because this
    // comes from a parsed result. Since this is unlikely to have any major
    // performance implications, as is determined empirically, we keep the
    // bounds check despite the performance hit.
    let (lo5, hi5) = POWER_OF_FIVE_128[index];
    let (mut first_lo, mut first_hi) = full_multiplication(w, lo5);
    if first_hi & mask == mask {
        let (_, second_hi) = full_multiplication(w, hi5);
        first_lo = first_lo.wrapping_add(second_hi);
        if second_hi > first_lo {
            first_hi += 1;
        }
    }
    (first_lo, first_hi)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_full_multiplication() {
        fn check(a: u64, b: u64, lo: u64, hi: u64) {
            assert_eq!(full_multiplication(a, b), (lo, hi));
            assert_eq!(full_multiplication(b, a), (lo, hi));
        }
        check(1 << 0, 1 << 0, 1, 0);
        check(1 << 0, 1 << 63, 1 << 63, 0);
        check(1 << 1, 1 << 63, 0, 1);
        check(1 << 63, 1 << 0, 1 << 63, 0);
        check(1 << 63, 1 << 1, 0, 1);
        check(1 << 63, 1 << 2, 0, 2);
        check(1 << 63, 1 << 63, 0, 1 << 62);
    }
}
```

## File: `src/common.rs`
```rust
use core::marker::PhantomData;
use core::ptr;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct AsciiStr<'a> {
    ptr: *const u8,
    end: *const u8,
    _marker: PhantomData<&'a [u8]>,
}

impl<'a> AsciiStr<'a> {
    #[inline]
    pub fn new(s: &'a [u8]) -> Self {
        Self {
            ptr: s.as_ptr(),
            end: unsafe { s.as_ptr().add(s.len()) },
            _marker: PhantomData,
        }
    }

    pub fn len(&self) -> isize {
        self.end as isize - self.ptr as isize
    }

    /// # Safety
    ///
    /// Safe if `n <= self.len()`
    #[inline]
    pub unsafe fn step_by(&mut self, n: usize) -> &mut Self {
        debug_assert!(
            // FIXME: remove when we drop support for < 1.43.0
            n < isize::max_value() as usize && n as isize <= self.len(),
            "buffer overflow: stepping by greater than our buffer length."
        );
        // SAFETY: Safe if `n <= self.len()`
        unsafe { self.ptr = self.ptr.add(n) };
        self
    }

    /// # Safety
    ///
    /// Safe if `!self.is_empty()`
    #[inline]
    pub unsafe fn step(&mut self) -> &mut Self {
        debug_assert!(!self.is_empty(), "buffer overflow: buffer is empty.");
        // SAFETY: Safe if the buffer is not empty, that is, `self.len() >= 1`
        unsafe { self.step_by(1) }
    }

    #[inline]
    pub fn step_if(&mut self, c: u8) -> bool {
        let stepped = self.first_is(c);
        if stepped {
            // SAFETY: safe since we have at least 1 character in the buffer
            unsafe { self.step() };
        }
        stepped
    }

    #[inline]
    pub fn is_empty(&self) -> bool {
        self.ptr == self.end
    }

    /// # Safety
    ///
    /// Safe if `!self.is_empty()`
    #[inline]
    pub unsafe fn first_unchecked(&self) -> u8 {
        debug_assert!(!self.is_empty(), "attempting to get first value of empty buffer.");
        unsafe { *self.ptr }
    }

    #[inline]
    pub fn first(&self) -> Option<u8> {
        if self.is_empty() {
            None
        } else {
            // SAFETY: safe since `!self.is_empty()`
            Some(unsafe { self.first_unchecked() })
        }
    }

    #[inline]
    pub fn first_is(&self, c: u8) -> bool {
        self.first() == Some(c)
    }

    #[inline]
    pub fn first_is2(&self, c1: u8, c2: u8) -> bool {
        self.first().map_or(false, |c| c == c1 || c == c2)
    }

    #[inline]
    pub fn first_is_digit(&self) -> bool {
        self.first().map_or(false, |c| c.is_ascii_digit())
    }

    #[inline]
    pub fn first_digit(&self) -> Option<u8> {
        self.first().and_then(|x| {
            if x.is_ascii_digit() {
                Some(x - b'0')
            } else {
                None
            }
        })
    }

    #[inline]
    pub fn try_read_digit(&mut self) -> Option<u8> {
        let digit = self.first_digit()?;
        // SAFETY: Safe since `first_digit` means the buffer is not empty
        unsafe { self.step() };
        Some(digit)
    }

    #[inline]
    pub fn parse_digits(&mut self, mut func: impl FnMut(u8)) {
        while let Some(digit) = self.try_read_digit() {
            func(digit);
        }
    }

    #[inline]
    pub fn try_read_u64(&self) -> Option<u64> {
        if self.len() >= 8 {
            Some(unsafe { self.read_u64_unchecked() })
        } else {
            None
        }
    }

    /// # Safety
    ///
    /// Safe if `self.len() >= 8`
    #[inline]
    #[allow(clippy::cast_ptr_alignment)]
    pub unsafe fn read_u64_unchecked(&self) -> u64 {
        debug_assert!(self.len() >= 8, "overflowing buffer: buffer is not 8 bytes long");
        let src = self.ptr as *const u64;
        // SAFETY: Safe if `self.len() >= 8`
        u64::from_le(unsafe { ptr::read_unaligned(src) })
    }

    #[inline]
    pub fn offset_from(&self, other: &Self) -> isize {
        isize::wrapping_sub(self.ptr as isize, other.ptr as isize) // assuming the same end
    }
}

// Most of these are inherently unsafe; we assume we know what we're calling and
// when.
pub trait ByteSlice: AsRef<[u8]> + AsMut<[u8]> {
    #[inline]
    fn check_first(&self, c: u8) -> bool {
        self.as_ref().first() == Some(&c)
    }

    #[inline]
    fn check_first2(&self, c1: u8, c2: u8) -> bool {
        if let Some(&c) = self.as_ref().first() {
            c == c1 || c == c2
        } else {
            false
        }
    }

    #[inline]
    fn eq_ignore_case(&self, u: &[u8]) -> bool {
        let s = self.as_ref();
        if s.len() < u.len() {
            return false;
        }
        let d = (0..u.len()).fold(0, |d, i| d | s[i] ^ u[i]);
        d == 0 || d == 32
    }

    #[inline]
    fn advance(&self, n: usize) -> &[u8] {
        &self.as_ref()[n..]
    }

    #[inline]
    fn skip_chars(&self, c: u8) -> &[u8] {
        let mut s = self.as_ref();
        while s.check_first(c) {
            s = s.advance(1);
        }
        s
    }

    /// # Safety
    ///
    /// Safe if `self.len() >= 8`.
    #[inline]
    #[allow(clippy::cast_ptr_alignment)]
    unsafe fn read_u64(&self) -> u64 {
        debug_assert!(self.as_ref().len() >= 8);
        let src = self.as_ref().as_ptr() as *const u64;
        // SAFETY: safe if `self.len() >= 8`.
        u64::from_le(unsafe { ptr::read_unaligned(src) })
    }

    /// # Safety
    ///
    /// Safe if `self.len() >= 8`.
    #[inline]
    #[allow(clippy::cast_ptr_alignment)]
    unsafe fn write_u64(&mut self, value: u64) {
        debug_assert!(self.as_ref().len() >= 8);
        let dst = self.as_mut().as_mut_ptr() as *mut u64;
        // SAFETY: safe if `self.len() >= 8`.
        unsafe { ptr::write_unaligned(dst, u64::to_le(value)) };
    }
}

impl ByteSlice for [u8] {
}

#[inline]
pub fn is_8digits(v: u64) -> bool {
    let a = v.wrapping_add(0x4646_4646_4646_4646);
    let b = v.wrapping_sub(0x3030_3030_3030_3030);
    (a | b) & 0x8080_8080_8080_8080 == 0
}

#[inline]
pub fn parse_digits(s: &mut &[u8], mut f: impl FnMut(u8)) {
    while let Some(&ch) = s.first() {
        let c = ch.wrapping_sub(b'0');
        if c < 10 {
            f(c);
            *s = s.advance(1);
        } else {
            break;
        }
    }
}

#[derive(Debug, Copy, Clone, PartialEq, Eq, Default)]
pub struct AdjustedMantissa {
    pub mantissa: u64,
    pub power2: i32,
}

impl AdjustedMantissa {
    #[inline]
    pub const fn zero_pow2(power2: i32) -> Self {
        Self {
            mantissa: 0,
            power2,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_read_write_u64() {
        let bytes = b"01234567";
        let string = AsciiStr::new(bytes);
        let int = string.try_read_u64();
        assert_eq!(int, Some(0x3736353433323130));

        let int = unsafe { bytes.read_u64() };
        assert_eq!(int, 0x3736353433323130);

        let mut slc = [0u8; 8];
        unsafe { slc.write_u64(0x3736353433323130) };
        assert_eq!(&slc, bytes);
    }
}
```

## File: `src/decimal.rs`
```rust
use core::fmt::{self, Debug};

use crate::common::{is_8digits, parse_digits, ByteSlice};

#[derive(Clone)]
pub struct Decimal {
    pub num_digits: usize,
    pub decimal_point: i32,
    pub negative: bool,
    pub truncated: bool,
    pub digits: [u8; Self::MAX_DIGITS],
}

impl Debug for Decimal {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.debug_struct("Decimal")
            .field("num_digits", &self.num_digits)
            .field("decimal_point", &self.decimal_point)
            .field("negative", &self.negative)
            .field("truncated", &self.truncated)
            .field("digits", &(&self.digits[..self.num_digits]))
            .finish()
    }
}

impl PartialEq for Decimal {
    fn eq(&self, other: &Self) -> bool {
        self.num_digits == other.num_digits
            && self.decimal_point == other.decimal_point
            && self.negative == other.negative
            && self.truncated == other.truncated
            && self.digits[..] == other.digits[..]
    }
}

impl Eq for Decimal {
}

impl Default for Decimal {
    fn default() -> Self {
        Self {
            num_digits: 0,
            decimal_point: 0,
            negative: false,
            truncated: false,
            digits: [0; Self::MAX_DIGITS],
        }
    }
}

impl Decimal {
    pub const MAX_DIGITS: usize = 768;
    pub const MAX_DIGITS_WITHOUT_OVERFLOW: usize = 19;
    pub const DECIMAL_POINT_RANGE: i32 = 2047;

    #[inline]
    pub fn try_add_digit(&mut self, digit: u8) {
        if self.num_digits < Self::MAX_DIGITS {
            self.digits[self.num_digits] = digit;
        }
        self.num_digits += 1;
    }

    #[inline]
    pub fn trim(&mut self) {
        while self.num_digits != 0 && self.digits[self.num_digits - 1] == 0 {
            self.num_digits -= 1;
        }
    }

    #[inline]
    pub fn round(&self) -> u64 {
        if self.num_digits == 0 || self.decimal_point < 0 {
            return 0;
        } else if self.decimal_point > 18 {
            return 0xFFFF_FFFF_FFFF_FFFF_u64;
        }
        let dp = self.decimal_point as usize;
        let mut n = 0_u64;
        for i in 0..dp {
            n *= 10;
            if i < self.num_digits {
                n += self.digits[i] as u64;
            }
        }
        let mut round_up = false;
        if dp < self.num_digits {
            round_up = self.digits[dp] >= 5;
            if self.digits[dp] == 5 && dp + 1 == self.num_digits {
                round_up = self.truncated || ((dp != 0) && (1 & self.digits[dp - 1] != 0));
            }
        }
        if round_up {
            n += 1;
        }
        n
    }

    #[inline]
    pub fn left_shift(&mut self, shift: usize) {
        if self.num_digits == 0 {
            return;
        }
        let num_new_digits = number_of_digits_decimal_left_shift(self, shift);
        let mut read_index = self.num_digits;
        let mut write_index = self.num_digits + num_new_digits;
        let mut n = 0_u64;
        while read_index != 0 {
            read_index -= 1;
            write_index -= 1;
            n += (self.digits[read_index] as u64) << shift;
            let quotient = n / 10;
            let remainder = n - (10 * quotient);
            if write_index < Self::MAX_DIGITS {
                self.digits[write_index] = remainder as u8;
            } else if remainder > 0 {
                self.truncated = true;
            }
            n = quotient;
        }
        while n > 0 {
            write_index -= 1;
            let quotient = n / 10;
            let remainder = n - (10 * quotient);
            if write_index < Self::MAX_DIGITS {
                self.digits[write_index] = remainder as u8;
            } else if remainder > 0 {
                self.truncated = true;
            }
            n = quotient;
        }
        self.num_digits += num_new_digits;
        if self.num_digits > Self::MAX_DIGITS {
            self.num_digits = Self::MAX_DIGITS;
        }
        self.decimal_point += num_new_digits as i32;
        self.trim();
    }

    #[inline]
    pub fn right_shift(&mut self, shift: usize) {
        let mut read_index = 0;
        let mut write_index = 0;
        let mut n = 0_u64;
        while (n >> shift) == 0 {
            if read_index < self.num_digits {
                n = (10 * n) + self.digits[read_index] as u64;
                read_index += 1;
            } else if n == 0 {
                return;
            } else {
                while (n >> shift) == 0 {
                    n *= 10;
                    read_index += 1;
                }
                break;
            }
        }
        self.decimal_point -= read_index as i32 - 1;
        if self.decimal_point < -Self::DECIMAL_POINT_RANGE {
            self.num_digits = 0;
            self.decimal_point = 0;
            self.negative = false;
            self.truncated = false;
            return;
        }
        let mask = (1_u64 << shift) - 1;
        while read_index < self.num_digits {
            let new_digit = (n >> shift) as u8;
            n = (10 * (n & mask)) + self.digits[read_index] as u64;
            read_index += 1;
            self.digits[write_index] = new_digit;
            write_index += 1;
        }
        while n > 0 {
            let new_digit = (n >> shift) as u8;
            n = 10 * (n & mask);
            if write_index < Self::MAX_DIGITS {
                self.digits[write_index] = new_digit;
                write_index += 1;
            } else if new_digit > 0 {
                self.truncated = true;
            }
        }
        self.num_digits = write_index;
        self.trim();
    }
}

#[inline]
pub fn parse_decimal(mut s: &[u8]) -> Decimal {
    // can't fail since it follows a call to parse_number
    assert!(!s.is_empty(), "the buffer cannot be empty since it follows a call to parse_number");
    let mut d = Decimal::default();
    let start = s;

    let c = s[0];
    d.negative = c == b'-';
    if c == b'-' || c == b'+' {
        s = s.advance(1);
    }
    s = s.skip_chars(b'0');
    parse_digits(&mut s, |digit| d.try_add_digit(digit));
    if s.check_first(b'.') {
        s = s.advance(1);
        let first = s;
        if d.num_digits == 0 {
            s = s.skip_chars(b'0');
        }
        while s.len() >= 8 && d.num_digits + 8 < Decimal::MAX_DIGITS {
            // SAFETY: Safe since `s.len() >= 8`
            let v = unsafe { s.read_u64() };
            if !is_8digits(v) {
                break;
            }
            // SAFETY: Safe since `num_digits + 8 < Decimal::MAX_DIGITS`
            unsafe { d.digits[d.num_digits..].write_u64(v - 0x3030_3030_3030_3030) };
            d.num_digits += 8;
            s = s.advance(8);
        }
        parse_digits(&mut s, |digit| d.try_add_digit(digit));
        d.decimal_point = s.len() as i32 - first.len() as i32;
    }
    if d.num_digits != 0 {
        // Ignore the trailing zeros if there are any
        let mut n_trailing_zeros = 0;
        for &c in start[..(start.len() - s.len())].iter().rev() {
            if c == b'0' {
                n_trailing_zeros += 1;
            } else if c != b'.' {
                break;
            }
        }
        d.decimal_point += n_trailing_zeros as i32;
        d.num_digits -= n_trailing_zeros;
        d.decimal_point += d.num_digits as i32;
        if d.num_digits > Decimal::MAX_DIGITS {
            d.truncated = true;
            d.num_digits = Decimal::MAX_DIGITS;
        }
    }
    if s.check_first2(b'e', b'E') {
        s = s.advance(1);
        let mut neg_exp = false;
        if s.check_first(b'-') {
            neg_exp = true;
            s = s.advance(1);
        } else if s.check_first(b'+') {
            s = s.advance(1);
        }
        let mut exp_num = 0_i32;
        parse_digits(&mut s, |digit| {
            if exp_num < 0x10000 {
                exp_num = 10 * exp_num + digit as i32;
            }
        });
        d.decimal_point += if neg_exp {
            -exp_num
        } else {
            exp_num
        };
    }
    for i in d.num_digits..Decimal::MAX_DIGITS_WITHOUT_OVERFLOW {
        d.digits[i] = 0;
    }
    d
}

#[inline]
#[allow(clippy::redundant_else)]
fn number_of_digits_decimal_left_shift(d: &Decimal, mut shift: usize) -> usize {
    const TABLE: [u16; 65] = [
        0x0000, 0x0800, 0x0801, 0x0803, 0x1006, 0x1009, 0x100D, 0x1812, 0x1817, 0x181D, 0x2024,
        0x202B, 0x2033, 0x203C, 0x2846, 0x2850, 0x285B, 0x3067, 0x3073, 0x3080, 0x388E, 0x389C,
        0x38AB, 0x38BB, 0x40CC, 0x40DD, 0x40EF, 0x4902, 0x4915, 0x4929, 0x513E, 0x5153, 0x5169,
        0x5180, 0x5998, 0x59B0, 0x59C9, 0x61E3, 0x61FD, 0x6218, 0x6A34, 0x6A50, 0x6A6D, 0x6A8B,
        0x72AA, 0x72C9, 0x72E9, 0x7B0A, 0x7B2B, 0x7B4D, 0x8370, 0x8393, 0x83B7, 0x83DC, 0x8C02,
        0x8C28, 0x8C4F, 0x9477, 0x949F, 0x94C8, 0x9CF2, 0x051C, 0x051C, 0x051C, 0x051C,
    ];
    const TABLE_POW5: [u8; 0x051C] = [
        5, 2, 5, 1, 2, 5, 6, 2, 5, 3, 1, 2, 5, 1, 5, 6, 2, 5, 7, 8, 1, 2, 5, 3, 9, 0, 6, 2, 5, 1,
        9, 5, 3, 1, 2, 5, 9, 7, 6, 5, 6, 2, 5, 4, 8, 8, 2, 8, 1, 2, 5, 2, 4, 4, 1, 4, 0, 6, 2, 5,
        1, 2, 2, 0, 7, 0, 3, 1, 2, 5, 6, 1, 0, 3, 5, 1, 5, 6, 2, 5, 3, 0, 5, 1, 7, 5, 7, 8, 1, 2,
        5, 1, 5, 2, 5, 8, 7, 8, 9, 0, 6, 2, 5, 7, 6, 2, 9, 3, 9, 4, 5, 3, 1, 2, 5, 3, 8, 1, 4, 6,
        9, 7, 2, 6, 5, 6, 2, 5, 1, 9, 0, 7, 3, 4, 8, 6, 3, 2, 8, 1, 2, 5, 9, 5, 3, 6, 7, 4, 3, 1,
        6, 4, 0, 6, 2, 5, 4, 7, 6, 8, 3, 7, 1, 5, 8, 2, 0, 3, 1, 2, 5, 2, 3, 8, 4, 1, 8, 5, 7, 9,
        1, 0, 1, 5, 6, 2, 5, 1, 1, 9, 2, 0, 9, 2, 8, 9, 5, 5, 0, 7, 8, 1, 2, 5, 5, 9, 6, 0, 4, 6,
        4, 4, 7, 7, 5, 3, 9, 0, 6, 2, 5, 2, 9, 8, 0, 2, 3, 2, 2, 3, 8, 7, 6, 9, 5, 3, 1, 2, 5, 1,
        4, 9, 0, 1, 1, 6, 1, 1, 9, 3, 8, 4, 7, 6, 5, 6, 2, 5, 7, 4, 5, 0, 5, 8, 0, 5, 9, 6, 9, 2,
        3, 8, 2, 8, 1, 2, 5, 3, 7, 2, 5, 2, 9, 0, 2, 9, 8, 4, 6, 1, 9, 1, 4, 0, 6, 2, 5, 1, 8, 6,
        2, 6, 4, 5, 1, 4, 9, 2, 3, 0, 9, 5, 7, 0, 3, 1, 2, 5, 9, 3, 1, 3, 2, 2, 5, 7, 4, 6, 1, 5,
        4, 7, 8, 5, 1, 5, 6, 2, 5, 4, 6, 5, 6, 6, 1, 2, 8, 7, 3, 0, 7, 7, 3, 9, 2, 5, 7, 8, 1, 2,
        5, 2, 3, 2, 8, 3, 0, 6, 4, 3, 6, 5, 3, 8, 6, 9, 6, 2, 8, 9, 0, 6, 2, 5, 1, 1, 6, 4, 1, 5,
        3, 2, 1, 8, 2, 6, 9, 3, 4, 8, 1, 4, 4, 5, 3, 1, 2, 5, 5, 8, 2, 0, 7, 6, 6, 0, 9, 1, 3, 4,
        6, 7, 4, 0, 7, 2, 2, 6, 5, 6, 2, 5, 2, 9, 1, 0, 3, 8, 3, 0, 4, 5, 6, 7, 3, 3, 7, 0, 3, 6,
        1, 3, 2, 8, 1, 2, 5, 1, 4, 5, 5, 1, 9, 1, 5, 2, 2, 8, 3, 6, 6, 8, 5, 1, 8, 0, 6, 6, 4, 0,
        6, 2, 5, 7, 2, 7, 5, 9, 5, 7, 6, 1, 4, 1, 8, 3, 4, 2, 5, 9, 0, 3, 3, 2, 0, 3, 1, 2, 5, 3,
        6, 3, 7, 9, 7, 8, 8, 0, 7, 0, 9, 1, 7, 1, 2, 9, 5, 1, 6, 6, 0, 1, 5, 6, 2, 5, 1, 8, 1, 8,
        9, 8, 9, 4, 0, 3, 5, 4, 5, 8, 5, 6, 4, 7, 5, 8, 3, 0, 0, 7, 8, 1, 2, 5, 9, 0, 9, 4, 9, 4,
        7, 0, 1, 7, 7, 2, 9, 2, 8, 2, 3, 7, 9, 1, 5, 0, 3, 9, 0, 6, 2, 5, 4, 5, 4, 7, 4, 7, 3, 5,
        0, 8, 8, 6, 4, 6, 4, 1, 1, 8, 9, 5, 7, 5, 1, 9, 5, 3, 1, 2, 5, 2, 2, 7, 3, 7, 3, 6, 7, 5,
        4, 4, 3, 2, 3, 2, 0, 5, 9, 4, 7, 8, 7, 5, 9, 7, 6, 5, 6, 2, 5, 1, 1, 3, 6, 8, 6, 8, 3, 7,
        7, 2, 1, 6, 1, 6, 0, 2, 9, 7, 3, 9, 3, 7, 9, 8, 8, 2, 8, 1, 2, 5, 5, 6, 8, 4, 3, 4, 1, 8,
        8, 6, 0, 8, 0, 8, 0, 1, 4, 8, 6, 9, 6, 8, 9, 9, 4, 1, 4, 0, 6, 2, 5, 2, 8, 4, 2, 1, 7, 0,
        9, 4, 3, 0, 4, 0, 4, 0, 0, 7, 4, 3, 4, 8, 4, 4, 9, 7, 0, 7, 0, 3, 1, 2, 5, 1, 4, 2, 1, 0,
        8, 5, 4, 7, 1, 5, 2, 0, 2, 0, 0, 3, 7, 1, 7, 4, 2, 2, 4, 8, 5, 3, 5, 1, 5, 6, 2, 5, 7, 1,
        0, 5, 4, 2, 7, 3, 5, 7, 6, 0, 1, 0, 0, 1, 8, 5, 8, 7, 1, 1, 2, 4, 2, 6, 7, 5, 7, 8, 1, 2,
        5, 3, 5, 5, 2, 7, 1, 3, 6, 7, 8, 8, 0, 0, 5, 0, 0, 9, 2, 9, 3, 5, 5, 6, 2, 1, 3, 3, 7, 8,
        9, 0, 6, 2, 5, 1, 7, 7, 6, 3, 5, 6, 8, 3, 9, 4, 0, 0, 2, 5, 0, 4, 6, 4, 6, 7, 7, 8, 1, 0,
        6, 6, 8, 9, 4, 5, 3, 1, 2, 5, 8, 8, 8, 1, 7, 8, 4, 1, 9, 7, 0, 0, 1, 2, 5, 2, 3, 2, 3, 3,
        8, 9, 0, 5, 3, 3, 4, 4, 7, 2, 6, 5, 6, 2, 5, 4, 4, 4, 0, 8, 9, 2, 0, 9, 8, 5, 0, 0, 6, 2,
        6, 1, 6, 1, 6, 9, 4, 5, 2, 6, 6, 7, 2, 3, 6, 3, 2, 8, 1, 2, 5, 2, 2, 2, 0, 4, 4, 6, 0, 4,
        9, 2, 5, 0, 3, 1, 3, 0, 8, 0, 8, 4, 7, 2, 6, 3, 3, 3, 6, 1, 8, 1, 6, 4, 0, 6, 2, 5, 1, 1,
        1, 0, 2, 2, 3, 0, 2, 4, 6, 2, 5, 1, 5, 6, 5, 4, 0, 4, 2, 3, 6, 3, 1, 6, 6, 8, 0, 9, 0, 8,
        2, 0, 3, 1, 2, 5, 5, 5, 5, 1, 1, 1, 5, 1, 2, 3, 1, 2, 5, 7, 8, 2, 7, 0, 2, 1, 1, 8, 1, 5,
        8, 3, 4, 0, 4, 5, 4, 1, 0, 1, 5, 6, 2, 5, 2, 7, 7, 5, 5, 5, 7, 5, 6, 1, 5, 6, 2, 8, 9, 1,
        3, 5, 1, 0, 5, 9, 0, 7, 9, 1, 7, 0, 2, 2, 7, 0, 5, 0, 7, 8, 1, 2, 5, 1, 3, 8, 7, 7, 7, 8,
        7, 8, 0, 7, 8, 1, 4, 4, 5, 6, 7, 5, 5, 2, 9, 5, 3, 9, 5, 8, 5, 1, 1, 3, 5, 2, 5, 3, 9, 0,
        6, 2, 5, 6, 9, 3, 8, 8, 9, 3, 9, 0, 3, 9, 0, 7, 2, 2, 8, 3, 7, 7, 6, 4, 7, 6, 9, 7, 9, 2,
        5, 5, 6, 7, 6, 2, 6, 9, 5, 3, 1, 2, 5, 3, 4, 6, 9, 4, 4, 6, 9, 5, 1, 9, 5, 3, 6, 1, 4, 1,
        8, 8, 8, 2, 3, 8, 4, 8, 9, 6, 2, 7, 8, 3, 8, 1, 3, 4, 7, 6, 5, 6, 2, 5, 1, 7, 3, 4, 7, 2,
        3, 4, 7, 5, 9, 7, 6, 8, 0, 7, 0, 9, 4, 4, 1, 1, 9, 2, 4, 4, 8, 1, 3, 9, 1, 9, 0, 6, 7, 3,
        8, 2, 8, 1, 2, 5, 8, 6, 7, 3, 6, 1, 7, 3, 7, 9, 8, 8, 4, 0, 3, 5, 4, 7, 2, 0, 5, 9, 6, 2,
        2, 4, 0, 6, 9, 5, 9, 5, 3, 3, 6, 9, 1, 4, 0, 6, 2, 5,
    ];

    shift &= 63;
    let x_a = TABLE[shift];
    let x_b = TABLE[shift + 1];
    let num_new_digits = (x_a >> 11) as usize;
    let pow5_a = (0x7FF & x_a) as usize;
    let pow5_b = (0x7FF & x_b) as usize;
    let pow5 = &TABLE_POW5[pow5_a..];
    for (i, &p5) in pow5.iter().enumerate().take(pow5_b - pow5_a) {
        if i >= d.num_digits {
            return num_new_digits - 1;
        } else if d.digits[i] == p5 {
            continue;
        } else if d.digits[i] < p5 {
            return num_new_digits - 1;
        } else {
            return num_new_digits;
        }
    }
    num_new_digits
}
```

## File: `src/float.rs`
```rust
use core::fmt::{Debug, Display};
use core::ops::{Add, Div, Mul, Neg};

mod private {
    pub trait Sealed {}
}

#[doc(hidden)]
pub trait Float:
    Sized
    + private::Sealed
    + Div<Output = Self>
    + Neg<Output = Self>
    + Mul<Output = Self>
    + Add<Output = Self>
    + PartialEq
    + PartialOrd
    + Default
    + Clone
    + Copy
    + Debug
    + Display
{
    const INFINITY: Self;
    const NEG_INFINITY: Self;
    const NAN: Self;
    const NEG_NAN: Self;

    const MANTISSA_EXPLICIT_BITS: usize;
    const MIN_EXPONENT_ROUND_TO_EVEN: i32;
    const MAX_EXPONENT_ROUND_TO_EVEN: i32;
    const MIN_EXPONENT_FAST_PATH: i64;
    const MAX_EXPONENT_FAST_PATH: i64;
    const MAX_EXPONENT_DISGUISED_FAST_PATH: i64;
    const MINIMUM_EXPONENT: i32;
    const INFINITE_POWER: i32;
    const SIGN_INDEX: usize;
    const SMALLEST_POWER_OF_TEN: i32;
    const LARGEST_POWER_OF_TEN: i32;

    const MAX_MANTISSA_FAST_PATH: u64 = 2_u64 << Self::MANTISSA_EXPLICIT_BITS;

    fn from_u64(v: u64) -> Self;
    fn from_u64_bits(v: u64) -> Self;
    fn pow10_fast_path(exponent: usize) -> Self;
}

impl private::Sealed for f32 {
}

impl Float for f32 {
    const INFINITY: Self = core::f32::INFINITY;
    const NEG_INFINITY: Self = core::f32::NEG_INFINITY;
    const NAN: Self = core::f32::NAN;
    const NEG_NAN: Self = -core::f32::NAN;

    const MANTISSA_EXPLICIT_BITS: usize = 23;
    const MIN_EXPONENT_ROUND_TO_EVEN: i32 = -17;
    const MAX_EXPONENT_ROUND_TO_EVEN: i32 = 10;
    const MIN_EXPONENT_FAST_PATH: i64 = -10; // assuming FLT_EVAL_METHOD = 0
    const MAX_EXPONENT_FAST_PATH: i64 = 10;
    const MAX_EXPONENT_DISGUISED_FAST_PATH: i64 = 17;
    const MINIMUM_EXPONENT: i32 = -127;
    const INFINITE_POWER: i32 = 0xFF;
    const SIGN_INDEX: usize = 31;
    const SMALLEST_POWER_OF_TEN: i32 = -65;
    const LARGEST_POWER_OF_TEN: i32 = 38;

    #[inline]
    fn from_u64(v: u64) -> Self {
        v as f32
    }

    #[inline]
    fn from_u64_bits(v: u64) -> Self {
        f32::from_bits((v & 0xFFFF_FFFF) as u32)
    }

    #[inline]
    fn pow10_fast_path(exponent: usize) -> Self {
        #[allow(clippy::use_self)]
        const TABLE: [f32; 16] =
            [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 0., 0., 0., 0., 0.];
        TABLE[exponent & 15]
    }
}

impl private::Sealed for f64 {
}

impl Float for f64 {
    const INFINITY: Self = core::f64::INFINITY;
    const NEG_INFINITY: Self = core::f64::NEG_INFINITY;
    const NAN: Self = core::f64::NAN;
    const NEG_NAN: Self = -core::f64::NAN;

    const MANTISSA_EXPLICIT_BITS: usize = 52;
    const MIN_EXPONENT_ROUND_TO_EVEN: i32 = -4;
    const MAX_EXPONENT_ROUND_TO_EVEN: i32 = 23;
    const MIN_EXPONENT_FAST_PATH: i64 = -22; // assuming FLT_EVAL_METHOD = 0
    const MAX_EXPONENT_FAST_PATH: i64 = 22;
    const MAX_EXPONENT_DISGUISED_FAST_PATH: i64 = 37;
    const MINIMUM_EXPONENT: i32 = -1023;
    const INFINITE_POWER: i32 = 0x7FF;
    const SIGN_INDEX: usize = 63;
    const SMALLEST_POWER_OF_TEN: i32 = -342;
    const LARGEST_POWER_OF_TEN: i32 = 308;

    #[inline]
    fn from_u64(v: u64) -> Self {
        v as f64
    }

    #[inline]
    fn from_u64_bits(v: u64) -> Self {
        f64::from_bits(v)
    }

    #[inline]
    fn pow10_fast_path(exponent: usize) -> Self {
        #[allow(clippy::use_self)]
        const TABLE: [f64; 32] = [
            1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14, 1e15,
            1e16, 1e17, 1e18, 1e19, 1e20, 1e21, 1e22, 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        ];
        TABLE[exponent & 31]
    }
}
```

## File: `src/lib.rs`
```rust
//! This crate provides a super-fast decimal number parser from strings into
//! floats.
//!
//! ## Usage
//!
//! There's two top-level functions provided: [`parse`](crate::parse()) and
//! [`parse_partial`](crate::parse_partial()), both taking
//! either a string or a bytes slice and parsing the input into either `f32` or
//! `f64`:
//!
//! - [`parse`](crate::parse()) treats the whole string as a decimal number and
//!   returns an error if there are invalid characters or if the string is
//!   empty.
//! - [`parse_partial`](crate::parse_partial()) tries to find the longest
//!   substring at the beginning of the given input string that can be parsed as
//!   a decimal number and, in the case of success, returns the parsed value
//!   along the number of characters processed; an error is returned if the
//!   string doesn't start with a decimal number or if it is empty. This
//!   function is most useful as a building block when constructing more complex
//!   parsers, or when parsing streams of data.
//!
//! ## Examples
//!
//! ```rust
//! // Parse the entire string as a decimal number.
//! let s = "1.23e-02";
//! let x: f32 = fast_float2::parse(s).unwrap();
//! assert_eq!(x, 0.0123);
//!
//! // Parse as many characters as possible as a decimal number.
//! let s = "1.23e-02foo";
//! let (x, n) = fast_float2::parse_partial::<f32, _>(s).unwrap();
//! assert_eq!(x, 0.0123);
//! assert_eq!(n, 8);
//! assert_eq!(&s[n..], "foo");
//! ```

#![cfg_attr(not(feature = "std"), no_std)]
#![allow(unused_unsafe)]
#![warn(unsafe_op_in_unsafe_fn)]
#![warn(clippy::all, clippy::pedantic, clippy::nursery, clippy::cargo)]
#![deny(
    clippy::doc_markdown,
    clippy::unnecessary_safety_comment,
    clippy::semicolon_if_nothing_returned,
    clippy::unwrap_used,
    clippy::as_underscore,
    clippy::doc_markdown
)]
#![allow(
    clippy::cast_possible_truncation,
    clippy::cast_possible_wrap,
    clippy::cast_sign_loss,
    clippy::cast_lossless,
    clippy::cast_precision_loss,
    clippy::missing_const_for_fn,
    clippy::use_self,
    clippy::module_name_repetitions,
    clippy::cargo_common_metadata,
    clippy::struct_field_names
)]

use core::fmt::{self, Display};

mod binary;
mod common;
mod decimal;
mod float;
mod number;
mod parse;
mod simple;
mod table;

/// Opaque error type for fast-float parsing functions.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct Error;

impl Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "error while parsing a float")
    }
}

#[cfg(feature = "std")]
impl std::error::Error for Error {
    fn description(&self) -> &'static str {
        "error while parsing a float"
    }
}

/// Result type alias for fast-float parsing functions.
pub type Result<T> = core::result::Result<T, Error>;

/// Trait for numerical float types that can be parsed from string.
pub trait FastFloat: float::Float {
    /// Parse a decimal number from string into float (full).
    ///
    /// # Errors
    ///
    /// Will return an error either if the string is not a valid decimal number.
    /// or if any characters are left remaining unparsed.
    #[inline]
    fn parse_float<S: AsRef<[u8]>>(s: S) -> Result<Self> {
        let s = s.as_ref();
        match Self::parse_float_partial(s) {
            Ok((v, n)) if n == s.len() => Ok(v),
            _ => Err(Error),
        }
    }

    /// Parse a decimal number from string into float (partial).
    ///
    /// This method parses as many characters as possible and returns the
    /// resulting number along with the number of digits processed (in case
    /// of success, this number is always positive).
    ///
    /// # Errors
    ///
    /// Will return an error either if the string doesn't start with a valid
    /// decimal number – that is, if no zero digits were processed.
    #[inline]
    fn parse_float_partial<S: AsRef<[u8]>>(s: S) -> Result<(Self, usize)> {
        parse::parse_float(s.as_ref()).ok_or(Error)
    }
}

impl FastFloat for f32 {
}
impl FastFloat for f64 {
}

/// Parse a decimal number from string into float (full).
///
/// # Errors
///
/// Will return an error either if the string is not a valid decimal number
/// or if any characters are left remaining unparsed.
#[inline]
pub fn parse<T: FastFloat, S: AsRef<[u8]>>(s: S) -> Result<T> {
    T::parse_float(s)
}

/// Parse a decimal number from string into float (partial).
///
/// This function parses as many characters as possible and returns the
/// resulting number along with the number of digits processed (in case of
/// success, this number is always positive).
///
/// # Errors
///
/// Will return an error either if the string doesn't start with a valid decimal
/// number – that is, if no zero digits were processed.
#[inline]
pub fn parse_partial<T: FastFloat, S: AsRef<[u8]>>(s: S) -> Result<(T, usize)> {
    T::parse_float_partial(s)
}
```

## File: `src/number.rs`
```rust
use crate::common::{is_8digits, AsciiStr, ByteSlice};
use crate::float::Float;

const MIN_19DIGIT_INT: u64 = 100_0000_0000_0000_0000;

#[allow(clippy::unreadable_literal)]
pub const INT_POW10: [u64; 16] = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000,
    10000000000,
    100000000000,
    1000000000000,
    10000000000000,
    100000000000000,
    1000000000000000,
];

#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct Number {
    pub exponent: i64,
    pub mantissa: u64,
    pub negative: bool,
    pub many_digits: bool,
}

impl Number {
    #[inline]
    fn is_fast_path<F: Float>(&self) -> bool {
        F::MIN_EXPONENT_FAST_PATH <= self.exponent
            && self.exponent <= F::MAX_EXPONENT_DISGUISED_FAST_PATH
            && self.mantissa <= F::MAX_MANTISSA_FAST_PATH
            && !self.many_digits
    }

    #[inline]
    pub fn try_fast_path<F: Float>(&self) -> Option<F> {
        if self.is_fast_path::<F>() {
            let mut value = if self.exponent <= F::MAX_EXPONENT_FAST_PATH {
                // normal fast path
                let value = F::from_u64(self.mantissa);
                if self.exponent < 0 {
                    value / F::pow10_fast_path((-self.exponent) as usize)
                } else {
                    value * F::pow10_fast_path(self.exponent as usize)
                }
            } else {
                // disguised fast path
                let shift = self.exponent - F::MAX_EXPONENT_FAST_PATH;
                let mantissa = self.mantissa.checked_mul(INT_POW10[shift as usize])?;
                if mantissa > F::MAX_MANTISSA_FAST_PATH {
                    return None;
                }
                F::from_u64(mantissa) * F::pow10_fast_path(F::MAX_EXPONENT_FAST_PATH as usize)
            };
            if self.negative {
                value = -value;
            }
            Some(value)
        } else {
            None
        }
    }
}

#[inline]
fn parse_8digits(mut v: u64) -> u64 {
    const MASK: u64 = 0x0000_00FF_0000_00FF;
    const MUL1: u64 = 0x000F_4240_0000_0064;
    const MUL2: u64 = 0x0000_2710_0000_0001;
    v -= 0x3030_3030_3030_3030;
    v = (v * 10) + (v >> 8); // will not overflow, fits in 63 bits
    let v1 = (v & MASK).wrapping_mul(MUL1);
    let v2 = ((v >> 16) & MASK).wrapping_mul(MUL2);
    ((v1.wrapping_add(v2) >> 32) as u32) as u64
}

#[inline]
fn try_parse_digits(s: &mut AsciiStr<'_>, x: &mut u64) {
    s.parse_digits(|digit| {
        // overflows to be handled later
        *x = x.wrapping_mul(10).wrapping_add(digit as u64);
    });
}

#[inline]
fn try_parse_19digits(s: &mut AsciiStr<'_>, x: &mut u64) {
    while *x < MIN_19DIGIT_INT {
        if let Some(digit) = s.try_read_digit() {
            *x = (*x * 10) + digit as u64; // no overflows here
        } else {
            break;
        }
    }
}

#[inline]
fn try_parse_8digits(s: &mut AsciiStr<'_>, x: &mut u64) {
    // may cause overflows, to be handled later
    if let Some(v) = s.try_read_u64() {
        if is_8digits(v) {
            *x = x.wrapping_mul(1_0000_0000).wrapping_add(parse_8digits(v));
            // SAFETY: safe since there is at least 8 bytes from `try_read_u64`.
            unsafe { s.step_by(8) };
            if let Some(v) = s.try_read_u64() {
                if is_8digits(v) {
                    *x = x.wrapping_mul(1_0000_0000).wrapping_add(parse_8digits(v));
                    // SAFETY: safe since there is at least 8 bytes from `try_read_u64`.
                    unsafe { s.step_by(8) };
                }
            }
        }
    }
}

#[inline]
fn parse_scientific(s: &mut AsciiStr<'_>) -> i64 {
    if !s.first_is2(b'e', b'E') {
        return 0;
    }

    // the first character is 'e'/'E' and scientific mode is enabled
    let start = *s;
    // SAFETY: safe since there is at least 1 character which is `e` or `E`
    unsafe { s.step() };
    let mut exp_num = 0_i64;
    let mut neg_exp = false;
    if s.first_is2(b'-', b'+') {
        neg_exp = s.first_is(b'-');
        // SAFETY: safe since there's at least 1 character in the buffer
        unsafe { s.step() };
    }
    if s.first_is_digit() {
        s.parse_digits(|digit| {
            if exp_num < 0x10000 {
                exp_num = 10 * exp_num + digit as i64; // no overflows here
            }
        });
        if neg_exp {
            -exp_num
        } else {
            exp_num
        }
    } else {
        *s = start; // ignore 'e' and return back
        0
    }
}

#[inline]
pub fn parse_number(s: &[u8]) -> Option<(Number, usize)> {
    if s.is_empty() {
        return None;
    }

    let mut s = AsciiStr::new(s);
    let start = s;

    // handle optional +/- sign
    let mut negative = false;
    if s.step_if(b'-') {
        negative = true;
        if s.is_empty() {
            return None;
        }
    } else if s.step_if(b'+') && s.is_empty() {
        return None;
    }
    debug_assert!(!s.is_empty(), "should not have empty buffer after sign checks");

    // parse initial digits before dot
    let mut mantissa = 0_u64;
    let digits_start = s;
    try_parse_digits(&mut s, &mut mantissa);
    let mut n_digits = s.offset_from(&digits_start);

    // handle dot with the following digits
    let mut n_after_dot = 0;
    let mut exponent = 0_i64;
    let int_end = s;
    if s.step_if(b'.') {
        let before = s;
        try_parse_8digits(&mut s, &mut mantissa);
        try_parse_digits(&mut s, &mut mantissa);
        n_after_dot = s.offset_from(&before);
        exponent = -n_after_dot as i64;
    }

    n_digits += n_after_dot;
    if n_digits == 0 {
        return None;
    }

    // handle scientific format
    let exp_number = parse_scientific(&mut s);
    exponent += exp_number;

    let len = s.offset_from(&start) as usize;

    // handle uncommon case with many digits
    if n_digits <= 19 {
        return Some((
            Number {
                exponent,
                mantissa,
                negative,
                many_digits: false,
            },
            len,
        ));
    }

    n_digits -= 19;
    let mut many_digits = false;
    let mut p = digits_start;
    while p.first_is2(b'0', b'.') {
        // SAFETY: safe since there's at least 1 element that is `0` or `.`.
        let byte = unsafe { p.first_unchecked() };
        // '0' = b'.' + 2
        n_digits -= byte.saturating_sub(b'0' - 1) as isize;
        // SAFETY: safe since there's at least 1 element from the `first_is2` check.
        unsafe { p.step() };
    }
    if n_digits > 0 {
        // at this point we have more than 19 significant digits, let's try again
        many_digits = true;
        mantissa = 0;
        let mut s = digits_start;
        try_parse_19digits(&mut s, &mut mantissa);
        exponent = if mantissa >= MIN_19DIGIT_INT {
            int_end.offset_from(&s) // big int
        } else {
            // SAFETY: safe since `s` is at the digits start, so we have
            // at least 1 digit from `ndigits > 0`.
            debug_assert!(s.first_is(b'.'), "first character for the fraction must be a decimal");
            unsafe { s.step() }; // fractional component, skip the '.'
            let before = s;
            try_parse_19digits(&mut s, &mut mantissa);
            -s.offset_from(&before)
        } as i64;
        exponent += exp_number; // add back the explicit part
    }

    Some((
        Number {
            exponent,
            mantissa,
            negative,
            many_digits,
        },
        len,
    ))
}

#[inline]
pub fn parse_inf_nan<F: Float>(s: &[u8]) -> Option<(F, usize)> {
    fn parse_inf_rest(s: &[u8]) -> usize {
        if s.len() >= 8 && s[3..].eq_ignore_case(b"inity") {
            8
        } else {
            3
        }
    }
    if s.len() >= 3 {
        if s.eq_ignore_case(b"nan") {
            return Some((F::NAN, 3));
        } else if s.eq_ignore_case(b"inf") {
            return Some((F::INFINITY, parse_inf_rest(s)));
        } else if s.len() >= 4 {
            if s[0] == b'+' {
                let s = s.advance(1);
                if s.eq_ignore_case(b"nan") {
                    return Some((F::NAN, 4));
                } else if s.eq_ignore_case(b"inf") {
                    return Some((F::INFINITY, 1 + parse_inf_rest(s)));
                }
            } else if s[0] == b'-' {
                let s = s.advance(1);
                if s.eq_ignore_case(b"nan") {
                    return Some((F::NEG_NAN, 4));
                } else if s.eq_ignore_case(b"inf") {
                    return Some((F::NEG_INFINITY, 1 + parse_inf_rest(s)));
                }
            }
        }
    }
    None
}
```

## File: `src/parse.rs`
```rust
use crate::binary::compute_float;
use crate::float::Float;
use crate::number::{parse_inf_nan, parse_number};
use crate::simple::parse_long_mantissa;

#[inline]
pub fn parse_float<F: Float>(s: &[u8]) -> Option<(F, usize)> {
    let (num, rest) = match parse_number(s) {
        Some(r) => r,
        None => return parse_inf_nan(s),
    };
    if let Some(value) = num.try_fast_path::<F>() {
        return Some((value, rest));
    }

    let mut am = compute_float::<F>(num.exponent, num.mantissa);
    if num.many_digits && am != compute_float::<F>(num.exponent, num.mantissa + 1) {
        am.power2 = -1;
    }
    if am.power2 < 0 {
        am = parse_long_mantissa::<F>(s);
    }

    let mut word = am.mantissa;
    word |= (am.power2 as u64) << F::MANTISSA_EXPLICIT_BITS;
    if num.negative {
        word |= 1_u64 << F::SIGN_INDEX;
    }
    Some((F::from_u64_bits(word), rest))
}
```

## File: `src/simple.rs`
```rust
use crate::common::AdjustedMantissa;
use crate::decimal::{parse_decimal, Decimal};
use crate::float::Float;

#[inline]
pub fn parse_long_mantissa<F: Float>(s: &[u8]) -> AdjustedMantissa {
    const MAX_SHIFT: usize = 60;
    const NUM_POWERS: usize = 19;
    const POWERS: [u8; 19] =
        [0, 3, 6, 9, 13, 16, 19, 23, 26, 29, 33, 36, 39, 43, 46, 49, 53, 56, 59];

    let get_shift = |n| {
        if n < NUM_POWERS {
            POWERS[n] as usize
        } else {
            MAX_SHIFT
        }
    };

    let am_zero = AdjustedMantissa::zero_pow2(0);
    let am_inf = AdjustedMantissa::zero_pow2(F::INFINITE_POWER);

    let mut d = parse_decimal(s);

    if d.num_digits == 0 || d.decimal_point < -324 {
        return am_zero;
    } else if d.decimal_point >= 310 {
        return am_inf;
    }
    let mut exp2 = 0_i32;
    while d.decimal_point > 0 {
        let n = d.decimal_point as usize;
        let shift = get_shift(n);
        d.right_shift(shift);
        if d.decimal_point < -Decimal::DECIMAL_POINT_RANGE {
            return am_zero;
        }
        exp2 += shift as i32;
    }
    while d.decimal_point <= 0 {
        let shift = if d.decimal_point == 0 {
            match d.digits[0] {
                digit if digit >= 5 => break,
                0 | 1 => 2,
                _ => 1,
            }
        } else {
            get_shift((-d.decimal_point) as usize)
        };
        d.left_shift(shift);
        if d.decimal_point > Decimal::DECIMAL_POINT_RANGE {
            return am_inf;
        }
        exp2 -= shift as i32;
    }
    exp2 -= 1;
    while (F::MINIMUM_EXPONENT + 1) > exp2 {
        let mut n = ((F::MINIMUM_EXPONENT + 1) - exp2) as usize;
        if n > MAX_SHIFT {
            n = MAX_SHIFT;
        }
        d.right_shift(n);
        exp2 += n as i32;
    }
    if (exp2 - F::MINIMUM_EXPONENT) >= F::INFINITE_POWER {
        return am_inf;
    }
    d.left_shift(F::MANTISSA_EXPLICIT_BITS + 1);
    let mut mantissa = d.round();
    if mantissa >= (1_u64 << (F::MANTISSA_EXPLICIT_BITS + 1)) {
        d.right_shift(1);
        exp2 += 1;
        mantissa = d.round();
        if (exp2 - F::MINIMUM_EXPONENT) >= F::INFINITE_POWER {
            return am_inf;
        }
    }
    let mut power2 = exp2 - F::MINIMUM_EXPONENT;
    if mantissa < (1_u64 << F::MANTISSA_EXPLICIT_BITS) {
        power2 -= 1;
    }
    mantissa &= (1_u64 << F::MANTISSA_EXPLICIT_BITS) - 1;
    AdjustedMantissa {
        mantissa,
        power2,
    }
}
```

## File: `src/table.rs`
```rust
pub const SMALLEST_POWER_OF_FIVE: i32 = -342;
pub const LARGEST_POWER_OF_FIVE: i32 = 308;
pub const N_POWERS_OF_FIVE: usize = (LARGEST_POWER_OF_FIVE - SMALLEST_POWER_OF_FIVE + 1) as usize;

#[cfg(test)]
mod tests {
    use num_bigint::BigUint;

    use super::*;

    fn compute_pow5_128(q: i32) -> (u64, u64) {
        let mut c = if q < 0 {
            let pow5 = BigUint::from(5_u8).pow((-q) as u32);
            let mut z = 0_u16;
            while (BigUint::from(1_u8) << z) < pow5 {
                z += 1;
            }
            let b = if q < -27 {
                2 * z + 128
            } else {
                z + 127
            };
            (BigUint::from(1_u8) << b) / pow5 + BigUint::from(1_u8)
        } else {
            BigUint::from(5_u8).pow(q as u32)
        };
        while c < (BigUint::from(1_u8) << 127) {
            c <<= 1;
        }
        while c >= (BigUint::from(1_u8) << 128) {
            c >>= 1;
        }
        let mut digits = c.to_u32_digits();
        while digits.len() < 4 {
            digits.push(0);
        }
        assert_eq!(digits.len(), 4);
        let lo = (digits[0] as u64) + (digits[1] as u64 * (1_u64 << 32));
        let hi = (digits[2] as u64) + (digits[3] as u64 * (1_u64 << 32));
        (hi, lo)
    }

    #[test]
    #[cfg_attr(miri, ignore)]
    fn test_pow5_table() {
        for q in SMALLEST_POWER_OF_FIVE..=LARGEST_POWER_OF_FIVE {
            let (hi, lo) = compute_pow5_128(q);
            let expected = POWER_OF_FIVE_128[(q - SMALLEST_POWER_OF_FIVE) as usize];
            assert_eq!(hi, expected.0);
            assert_eq!(lo, expected.1);
        }
    }
}

#[allow(clippy::unreadable_literal)]
pub const POWER_OF_FIVE_128: [(u64, u64); N_POWERS_OF_FIVE] = [
    (0xeef453d6923bd65a, 0x113faa2906a13b3f),
    (0x9558b4661b6565f8, 0x4ac7ca59a424c507),
    (0xbaaee17fa23ebf76, 0x5d79bcf00d2df649),
    (0xe95a99df8ace6f53, 0xf4d82c2c107973dc),
    (0x91d8a02bb6c10594, 0x79071b9b8a4be869),
    (0xb64ec836a47146f9, 0x9748e2826cdee284),
    (0xe3e27a444d8d98b7, 0xfd1b1b2308169b25),
    (0x8e6d8c6ab0787f72, 0xfe30f0f5e50e20f7),
    (0xb208ef855c969f4f, 0xbdbd2d335e51a935),
    (0xde8b2b66b3bc4723, 0xad2c788035e61382),
    (0x8b16fb203055ac76, 0x4c3bcb5021afcc31),
    (0xaddcb9e83c6b1793, 0xdf4abe242a1bbf3d),
    (0xd953e8624b85dd78, 0xd71d6dad34a2af0d),
    (0x87d4713d6f33aa6b, 0x8672648c40e5ad68),
    (0xa9c98d8ccb009506, 0x680efdaf511f18c2),
    (0xd43bf0effdc0ba48, 0x212bd1b2566def2),
    (0x84a57695fe98746d, 0x14bb630f7604b57),
    (0xa5ced43b7e3e9188, 0x419ea3bd35385e2d),
    (0xcf42894a5dce35ea, 0x52064cac828675b9),
    (0x818995ce7aa0e1b2, 0x7343efebd1940993),
    (0xa1ebfb4219491a1f, 0x1014ebe6c5f90bf8),
    (0xca66fa129f9b60a6, 0xd41a26e077774ef6),
    (0xfd00b897478238d0, 0x8920b098955522b4),
    (0x9e20735e8cb16382, 0x55b46e5f5d5535b0),
    (0xc5a890362fddbc62, 0xeb2189f734aa831d),
    (0xf712b443bbd52b7b, 0xa5e9ec7501d523e4),
    (0x9a6bb0aa55653b2d, 0x47b233c92125366e),
    (0xc1069cd4eabe89f8, 0x999ec0bb696e840a),
    (0xf148440a256e2c76, 0xc00670ea43ca250d),
    (0x96cd2a865764dbca, 0x380406926a5e5728),
    (0xbc807527ed3e12bc, 0xc605083704f5ecf2),
    (0xeba09271e88d976b, 0xf7864a44c633682e),
    (0x93445b8731587ea3, 0x7ab3ee6afbe0211d),
    (0xb8157268fdae9e4c, 0x5960ea05bad82964),
    (0xe61acf033d1a45df, 0x6fb92487298e33bd),
    (0x8fd0c16206306bab, 0xa5d3b6d479f8e056),
    (0xb3c4f1ba87bc8696, 0x8f48a4899877186c),
    (0xe0b62e2929aba83c, 0x331acdabfe94de87),
    (0x8c71dcd9ba0b4925, 0x9ff0c08b7f1d0b14),
    (0xaf8e5410288e1b6f, 0x7ecf0ae5ee44dd9),
    (0xdb71e91432b1a24a, 0xc9e82cd9f69d6150),
    (0x892731ac9faf056e, 0xbe311c083a225cd2),
    (0xab70fe17c79ac6ca, 0x6dbd630a48aaf406),
    (0xd64d3d9db981787d, 0x92cbbccdad5b108),
    (0x85f0468293f0eb4e, 0x25bbf56008c58ea5),
    (0xa76c582338ed2621, 0xaf2af2b80af6f24e),
    (0xd1476e2c07286faa, 0x1af5af660db4aee1),
    (0x82cca4db847945ca, 0x50d98d9fc890ed4d),
    (0xa37fce126597973c, 0xe50ff107bab528a0),
    (0xcc5fc196fefd7d0c, 0x1e53ed49a96272c8),
    (0xff77b1fcbebcdc4f, 0x25e8e89c13bb0f7a),
    (0x9faacf3df73609b1, 0x77b191618c54e9ac),
    (0xc795830d75038c1d, 0xd59df5b9ef6a2417),
    (0xf97ae3d0d2446f25, 0x4b0573286b44ad1d),
    (0x9becce62836ac577, 0x4ee367f9430aec32),
    (0xc2e801fb244576d5, 0x229c41f793cda73f),
    (0xf3a20279ed56d48a, 0x6b43527578c1110f),
    (0x9845418c345644d6, 0x830a13896b78aaa9),
    (0xbe5691ef416bd60c, 0x23cc986bc656d553),
    (0xedec366b11c6cb8f, 0x2cbfbe86b7ec8aa8),
    (0x94b3a202eb1c3f39, 0x7bf7d71432f3d6a9),
    (0xb9e08a83a5e34f07, 0xdaf5ccd93fb0cc53),
    (0xe858ad248f5c22c9, 0xd1b3400f8f9cff68),
    (0x91376c36d99995be, 0x23100809b9c21fa1),
    (0xb58547448ffffb2d, 0xabd40a0c2832a78a),
    (0xe2e69915b3fff9f9, 0x16c90c8f323f516c),
    (0x8dd01fad907ffc3b, 0xae3da7d97f6792e3),
    (0xb1442798f49ffb4a, 0x99cd11cfdf41779c),
    (0xdd95317f31c7fa1d, 0x40405643d711d583),
    (0x8a7d3eef7f1cfc52, 0x482835ea666b2572),
    (0xad1c8eab5ee43b66, 0xda3243650005eecf),
    (0xd863b256369d4a40, 0x90bed43e40076a82),
    (0x873e4f75e2224e68, 0x5a7744a6e804a291),
    (0xa90de3535aaae202, 0x711515d0a205cb36),
    (0xd3515c2831559a83, 0xd5a5b44ca873e03),
    (0x8412d9991ed58091, 0xe858790afe9486c2),
    (0xa5178fff668ae0b6, 0x626e974dbe39a872),
    (0xce5d73ff402d98e3, 0xfb0a3d212dc8128f),
    (0x80fa687f881c7f8e, 0x7ce66634bc9d0b99),
    (0xa139029f6a239f72, 0x1c1fffc1ebc44e80),
    (0xc987434744ac874e, 0xa327ffb266b56220),
    (0xfbe9141915d7a922, 0x4bf1ff9f0062baa8),
    (0x9d71ac8fada6c9b5, 0x6f773fc3603db4a9),
    (0xc4ce17b399107c22, 0xcb550fb4384d21d3),
    (0xf6019da07f549b2b, 0x7e2a53a146606a48),
    (0x99c102844f94e0fb, 0x2eda7444cbfc426d),
    (0xc0314325637a1939, 0xfa911155fefb5308),
    (0xf03d93eebc589f88, 0x793555ab7eba27ca),
    (0x96267c7535b763b5, 0x4bc1558b2f3458de),
    (0xbbb01b9283253ca2, 0x9eb1aaedfb016f16),
    (0xea9c227723ee8bcb, 0x465e15a979c1cadc),
    (0x92a1958a7675175f, 0xbfacd89ec191ec9),
    (0xb749faed14125d36, 0xcef980ec671f667b),
    (0xe51c79a85916f484, 0x82b7e12780e7401a),
    (0x8f31cc0937ae58d2, 0xd1b2ecb8b0908810),
    (0xb2fe3f0b8599ef07, 0x861fa7e6dcb4aa15),
    (0xdfbdcece67006ac9, 0x67a791e093e1d49a),
    (0x8bd6a141006042bd, 0xe0c8bb2c5c6d24e0),
    (0xaecc49914078536d, 0x58fae9f773886e18),
    (0xda7f5bf590966848, 0xaf39a475506a899e),
    (0x888f99797a5e012d, 0x6d8406c952429603),
    (0xaab37fd7d8f58178, 0xc8e5087ba6d33b83),
    (0xd5605fcdcf32e1d6, 0xfb1e4a9a90880a64),
    (0x855c3be0a17fcd26, 0x5cf2eea09a55067f),
    (0xa6b34ad8c9dfc06f, 0xf42faa48c0ea481e),
    (0xd0601d8efc57b08b, 0xf13b94daf124da26),
    (0x823c12795db6ce57, 0x76c53d08d6b70858),
    (0xa2cb1717b52481ed, 0x54768c4b0c64ca6e),
    (0xcb7ddcdda26da268, 0xa9942f5dcf7dfd09),
    (0xfe5d54150b090b02, 0xd3f93b35435d7c4c),
    (0x9efa548d26e5a6e1, 0xc47bc5014a1a6daf),
    (0xc6b8e9b0709f109a, 0x359ab6419ca1091b),
    (0xf867241c8cc6d4c0, 0xc30163d203c94b62),
    (0x9b407691d7fc44f8, 0x79e0de63425dcf1d),
    (0xc21094364dfb5636, 0x985915fc12f542e4),
    (0xf294b943e17a2bc4, 0x3e6f5b7b17b2939d),
    (0x979cf3ca6cec5b5a, 0xa705992ceecf9c42),
    (0xbd8430bd08277231, 0x50c6ff782a838353),
    (0xece53cec4a314ebd, 0xa4f8bf5635246428),
    (0x940f4613ae5ed136, 0x871b7795e136be99),
    (0xb913179899f68584, 0x28e2557b59846e3f),
    (0xe757dd7ec07426e5, 0x331aeada2fe589cf),
    (0x9096ea6f3848984f, 0x3ff0d2c85def7621),
    (0xb4bca50b065abe63, 0xfed077a756b53a9),
    (0xe1ebce4dc7f16dfb, 0xd3e8495912c62894),
    (0x8d3360f09cf6e4bd, 0x64712dd7abbbd95c),
    (0xb080392cc4349dec, 0xbd8d794d96aacfb3),
    (0xdca04777f541c567, 0xecf0d7a0fc5583a0),
    (0x89e42caaf9491b60, 0xf41686c49db57244),
    (0xac5d37d5b79b6239, 0x311c2875c522ced5),
    (0xd77485cb25823ac7, 0x7d633293366b828b),
    (0x86a8d39ef77164bc, 0xae5dff9c02033197),
    (0xa8530886b54dbdeb, 0xd9f57f830283fdfc),
    (0xd267caa862a12d66, 0xd072df63c324fd7b),
    (0x8380dea93da4bc60, 0x4247cb9e59f71e6d),
    (0xa46116538d0deb78, 0x52d9be85f074e608),
    (0xcd795be870516656, 0x67902e276c921f8b),
    (0x806bd9714632dff6, 0xba1cd8a3db53b6),
    (0xa086cfcd97bf97f3, 0x80e8a40eccd228a4),
    (0xc8a883c0fdaf7df0, 0x6122cd128006b2cd),
    (0xfad2a4b13d1b5d6c, 0x796b805720085f81),
    (0x9cc3a6eec6311a63, 0xcbe3303674053bb0),
    (0xc3f490aa77bd60fc, 0xbedbfc4411068a9c),
    (0xf4f1b4d515acb93b, 0xee92fb5515482d44),
    (0x991711052d8bf3c5, 0x751bdd152d4d1c4a),
    (0xbf5cd54678eef0b6, 0xd262d45a78a0635d),
    (0xef340a98172aace4, 0x86fb897116c87c34),
    (0x9580869f0e7aac0e, 0xd45d35e6ae3d4da0),
    (0xbae0a846d2195712, 0x8974836059cca109),
    (0xe998d258869facd7, 0x2bd1a438703fc94b),
    (0x91ff83775423cc06, 0x7b6306a34627ddcf),
    (0xb67f6455292cbf08, 0x1a3bc84c17b1d542),
    (0xe41f3d6a7377eeca, 0x20caba5f1d9e4a93),
    (0x8e938662882af53e, 0x547eb47b7282ee9c),
    (0xb23867fb2a35b28d, 0xe99e619a4f23aa43),
    (0xdec681f9f4c31f31, 0x6405fa00e2ec94d4),
    (0x8b3c113c38f9f37e, 0xde83bc408dd3dd04),
    (0xae0b158b4738705e, 0x9624ab50b148d445),
    (0xd98ddaee19068c76, 0x3badd624dd9b0957),
    (0x87f8a8d4cfa417c9, 0xe54ca5d70a80e5d6),
    (0xa9f6d30a038d1dbc, 0x5e9fcf4ccd211f4c),
    (0xd47487cc8470652b, 0x7647c3200069671f),
    (0x84c8d4dfd2c63f3b, 0x29ecd9f40041e073),
    (0xa5fb0a17c777cf09, 0xf468107100525890),
    (0xcf79cc9db955c2cc, 0x7182148d4066eeb4),
    (0x81ac1fe293d599bf, 0xc6f14cd848405530),
    (0xa21727db38cb002f, 0xb8ada00e5a506a7c),
    (0xca9cf1d206fdc03b, 0xa6d90811f0e4851c),
    (0xfd442e4688bd304a, 0x908f4a166d1da663),
    (0x9e4a9cec15763e2e, 0x9a598e4e043287fe),
    (0xc5dd44271ad3cdba, 0x40eff1e1853f29fd),
    (0xf7549530e188c128, 0xd12bee59e68ef47c),
    (0x9a94dd3e8cf578b9, 0x82bb74f8301958ce),
    (0xc13a148e3032d6e7, 0xe36a52363c1faf01),
    (0xf18899b1bc3f8ca1, 0xdc44e6c3cb279ac1),
    (0x96f5600f15a7b7e5, 0x29ab103a5ef8c0b9),
    (0xbcb2b812db11a5de, 0x7415d448f6b6f0e7),
    (0xebdf661791d60f56, 0x111b495b3464ad21),
    (0x936b9fcebb25c995, 0xcab10dd900beec34),
    (0xb84687c269ef3bfb, 0x3d5d514f40eea742),
    (0xe65829b3046b0afa, 0xcb4a5a3112a5112),
    (0x8ff71a0fe2c2e6dc, 0x47f0e785eaba72ab),
    (0xb3f4e093db73a093, 0x59ed216765690f56),
    (0xe0f218b8d25088b8, 0x306869c13ec3532c),
    (0x8c974f7383725573, 0x1e414218c73a13fb),
    (0xafbd2350644eeacf, 0xe5d1929ef90898fa),
    (0xdbac6c247d62a583, 0xdf45f746b74abf39),
    (0x894bc396ce5da772, 0x6b8bba8c328eb783),
    (0xab9eb47c81f5114f, 0x66ea92f3f326564),
    (0xd686619ba27255a2, 0xc80a537b0efefebd),
    (0x8613fd0145877585, 0xbd06742ce95f5f36),
    (0xa798fc4196e952e7, 0x2c48113823b73704),
    (0xd17f3b51fca3a7a0, 0xf75a15862ca504c5),
    (0x82ef85133de648c4, 0x9a984d73dbe722fb),
    (0xa3ab66580d5fdaf5, 0xc13e60d0d2e0ebba),
    (0xcc963fee10b7d1b3, 0x318df905079926a8),
    (0xffbbcfe994e5c61f, 0xfdf17746497f7052),
    (0x9fd561f1fd0f9bd3, 0xfeb6ea8bedefa633),
    (0xc7caba6e7c5382c8, 0xfe64a52ee96b8fc0),
    (0xf9bd690a1b68637b, 0x3dfdce7aa3c673b0),
    (0x9c1661a651213e2d, 0x6bea10ca65c084e),
    (0xc31bfa0fe5698db8, 0x486e494fcff30a62),
    (0xf3e2f893dec3f126, 0x5a89dba3c3efccfa),
    (0x986ddb5c6b3a76b7, 0xf89629465a75e01c),
    (0xbe89523386091465, 0xf6bbb397f1135823),
    (0xee2ba6c0678b597f, 0x746aa07ded582e2c),
    (0x94db483840b717ef, 0xa8c2a44eb4571cdc),
    (0xba121a4650e4ddeb, 0x92f34d62616ce413),
    (0xe896a0d7e51e1566, 0x77b020baf9c81d17),
    (0x915e2486ef32cd60, 0xace1474dc1d122e),
    (0xb5b5ada8aaff80b8, 0xd819992132456ba),
    (0xe3231912d5bf60e6, 0x10e1fff697ed6c69),
    (0x8df5efabc5979c8f, 0xca8d3ffa1ef463c1),
    (0xb1736b96b6fd83b3, 0xbd308ff8a6b17cb2),
    (0xddd0467c64bce4a0, 0xac7cb3f6d05ddbde),
    (0x8aa22c0dbef60ee4, 0x6bcdf07a423aa96b),
    (0xad4ab7112eb3929d, 0x86c16c98d2c953c6),
    (0xd89d64d57a607744, 0xe871c7bf077ba8b7),
    (0x87625f056c7c4a8b, 0x11471cd764ad4972),
    (0xa93af6c6c79b5d2d, 0xd598e40d3dd89bcf),
    (0xd389b47879823479, 0x4aff1d108d4ec2c3),
    (0x843610cb4bf160cb, 0xcedf722a585139ba),
    (0xa54394fe1eedb8fe, 0xc2974eb4ee658828),
    (0xce947a3da6a9273e, 0x733d226229feea32),
    (0x811ccc668829b887, 0x806357d5a3f525f),
    (0xa163ff802a3426a8, 0xca07c2dcb0cf26f7),
    (0xc9bcff6034c13052, 0xfc89b393dd02f0b5),
    (0xfc2c3f3841f17c67, 0xbbac2078d443ace2),
    (0x9d9ba7832936edc0, 0xd54b944b84aa4c0d),
    (0xc5029163f384a931, 0xa9e795e65d4df11),
    (0xf64335bcf065d37d, 0x4d4617b5ff4a16d5),
    (0x99ea0196163fa42e, 0x504bced1bf8e4e45),
    (0xc06481fb9bcf8d39, 0xe45ec2862f71e1d6),
    (0xf07da27a82c37088, 0x5d767327bb4e5a4c),
    (0x964e858c91ba2655, 0x3a6a07f8d510f86f),
    (0xbbe226efb628afea, 0x890489f70a55368b),
    (0xeadab0aba3b2dbe5, 0x2b45ac74ccea842e),
    (0x92c8ae6b464fc96f, 0x3b0b8bc90012929d),
    (0xb77ada0617e3bbcb, 0x9ce6ebb40173744),
    (0xe55990879ddcaabd, 0xcc420a6a101d0515),
    (0x8f57fa54c2a9eab6, 0x9fa946824a12232d),
    (0xb32df8e9f3546564, 0x47939822dc96abf9),
    (0xdff9772470297ebd, 0x59787e2b93bc56f7),
    (0x8bfbea76c619ef36, 0x57eb4edb3c55b65a),
    (0xaefae51477a06b03, 0xede622920b6b23f1),
    (0xdab99e59958885c4, 0xe95fab368e45eced),
    (0x88b402f7fd75539b, 0x11dbcb0218ebb414),
    (0xaae103b5fcd2a881, 0xd652bdc29f26a119),
    (0xd59944a37c0752a2, 0x4be76d3346f0495f),
    (0x857fcae62d8493a5, 0x6f70a4400c562ddb),
    (0xa6dfbd9fb8e5b88e, 0xcb4ccd500f6bb952),
    (0xd097ad07a71f26b2, 0x7e2000a41346a7a7),
    (0x825ecc24c873782f, 0x8ed400668c0c28c8),
    (0xa2f67f2dfa90563b, 0x728900802f0f32fa),
    (0xcbb41ef979346bca, 0x4f2b40a03ad2ffb9),
    (0xfea126b7d78186bc, 0xe2f610c84987bfa8),
    (0x9f24b832e6b0f436, 0xdd9ca7d2df4d7c9),
    (0xc6ede63fa05d3143, 0x91503d1c79720dbb),
    (0xf8a95fcf88747d94, 0x75a44c6397ce912a),
    (0x9b69dbe1b548ce7c, 0xc986afbe3ee11aba),
    (0xc24452da229b021b, 0xfbe85badce996168),
    (0xf2d56790ab41c2a2, 0xfae27299423fb9c3),
    (0x97c560ba6b0919a5, 0xdccd879fc967d41a),
    (0xbdb6b8e905cb600f, 0x5400e987bbc1c920),
    (0xed246723473e3813, 0x290123e9aab23b68),
    (0x9436c0760c86e30b, 0xf9a0b6720aaf6521),
    (0xb94470938fa89bce, 0xf808e40e8d5b3e69),
    (0xe7958cb87392c2c2, 0xb60b1d1230b20e04),
    (0x90bd77f3483bb9b9, 0xb1c6f22b5e6f48c2),
    (0xb4ecd5f01a4aa828, 0x1e38aeb6360b1af3),
    (0xe2280b6c20dd5232, 0x25c6da63c38de1b0),
    (0x8d590723948a535f, 0x579c487e5a38ad0e),
    (0xb0af48ec79ace837, 0x2d835a9df0c6d851),
    (0xdcdb1b2798182244, 0xf8e431456cf88e65),
    (0x8a08f0f8bf0f156b, 0x1b8e9ecb641b58ff),
    (0xac8b2d36eed2dac5, 0xe272467e3d222f3f),
    (0xd7adf884aa879177, 0x5b0ed81dcc6abb0f),
    (0x86ccbb52ea94baea, 0x98e947129fc2b4e9),
    (0xa87fea27a539e9a5, 0x3f2398d747b36224),
    (0xd29fe4b18e88640e, 0x8eec7f0d19a03aad),
    (0x83a3eeeef9153e89, 0x1953cf68300424ac),
    (0xa48ceaaab75a8e2b, 0x5fa8c3423c052dd7),
    (0xcdb02555653131b6, 0x3792f412cb06794d),
    (0x808e17555f3ebf11, 0xe2bbd88bbee40bd0),
    (0xa0b19d2ab70e6ed6, 0x5b6aceaeae9d0ec4),
    (0xc8de047564d20a8b, 0xf245825a5a445275),
    (0xfb158592be068d2e, 0xeed6e2f0f0d56712),
    (0x9ced737bb6c4183d, 0x55464dd69685606b),
    (0xc428d05aa4751e4c, 0xaa97e14c3c26b886),
    (0xf53304714d9265df, 0xd53dd99f4b3066a8),
    (0x993fe2c6d07b7fab, 0xe546a8038efe4029),
    (0xbf8fdb78849a5f96, 0xde98520472bdd033),
    (0xef73d256a5c0f77c, 0x963e66858f6d4440),
    (0x95a8637627989aad, 0xdde7001379a44aa8),
    (0xbb127c53b17ec159, 0x5560c018580d5d52),
    (0xe9d71b689dde71af, 0xaab8f01e6e10b4a6),
    (0x9226712162ab070d, 0xcab3961304ca70e8),
    (0xb6b00d69bb55c8d1, 0x3d607b97c5fd0d22),
    (0xe45c10c42a2b3b05, 0x8cb89a7db77c506a),
    (0x8eb98a7a9a5b04e3, 0x77f3608e92adb242),
    (0xb267ed1940f1c61c, 0x55f038b237591ed3),
    (0xdf01e85f912e37a3, 0x6b6c46dec52f6688),
    (0x8b61313bbabce2c6, 0x2323ac4b3b3da015),
    (0xae397d8aa96c1b77, 0xabec975e0a0d081a),
    (0xd9c7dced53c72255, 0x96e7bd358c904a21),
    (0x881cea14545c7575, 0x7e50d64177da2e54),
    (0xaa242499697392d2, 0xdde50bd1d5d0b9e9),
    (0xd4ad2dbfc3d07787, 0x955e4ec64b44e864),
    (0x84ec3c97da624ab4, 0xbd5af13bef0b113e),
    (0xa6274bbdd0fadd61, 0xecb1ad8aeacdd58e),
    (0xcfb11ead453994ba, 0x67de18eda5814af2),
    (0x81ceb32c4b43fcf4, 0x80eacf948770ced7),
    (0xa2425ff75e14fc31, 0xa1258379a94d028d),
    (0xcad2f7f5359a3b3e, 0x96ee45813a04330),
    (0xfd87b5f28300ca0d, 0x8bca9d6e188853fc),
    (0x9e74d1b791e07e48, 0x775ea264cf55347e),
    (0xc612062576589dda, 0x95364afe032a819e),
    (0xf79687aed3eec551, 0x3a83ddbd83f52205),
    (0x9abe14cd44753b52, 0xc4926a9672793543),
    (0xc16d9a0095928a27, 0x75b7053c0f178294),
    (0xf1c90080baf72cb1, 0x5324c68b12dd6339),
    (0x971da05074da7bee, 0xd3f6fc16ebca5e04),
    (0xbce5086492111aea, 0x88f4bb1ca6bcf585),
    (0xec1e4a7db69561a5, 0x2b31e9e3d06c32e6),
    (0x9392ee8e921d5d07, 0x3aff322e62439fd0),
    (0xb877aa3236a4b449, 0x9befeb9fad487c3),
    (0xe69594bec44de15b, 0x4c2ebe687989a9b4),
    (0x901d7cf73ab0acd9, 0xf9d37014bf60a11),
    (0xb424dc35095cd80f, 0x538484c19ef38c95),
    (0xe12e13424bb40e13, 0x2865a5f206b06fba),
    (0x8cbccc096f5088cb, 0xf93f87b7442e45d4),
    (0xafebff0bcb24aafe, 0xf78f69a51539d749),
    (0xdbe6fecebdedd5be, 0xb573440e5a884d1c),
    (0x89705f4136b4a597, 0x31680a88f8953031),
    (0xabcc77118461cefc, 0xfdc20d2b36ba7c3e),
    (0xd6bf94d5e57a42bc, 0x3d32907604691b4d),
    (0x8637bd05af6c69b5, 0xa63f9a49c2c1b110),
    (0xa7c5ac471b478423, 0xfcf80dc33721d54),
    (0xd1b71758e219652b, 0xd3c36113404ea4a9),
    (0x83126e978d4fdf3b, 0x645a1cac083126ea),
    (0xa3d70a3d70a3d70a, 0x3d70a3d70a3d70a4),
    (0xcccccccccccccccc, 0xcccccccccccccccd),
    (0x8000000000000000, 0x0),
    (0xa000000000000000, 0x0),
    (0xc800000000000000, 0x0),
    (0xfa00000000000000, 0x0),
    (0x9c40000000000000, 0x0),
    (0xc350000000000000, 0x0),
    (0xf424000000000000, 0x0),
    (0x9896800000000000, 0x0),
    (0xbebc200000000000, 0x0),
    (0xee6b280000000000, 0x0),
    (0x9502f90000000000, 0x0),
    (0xba43b74000000000, 0x0),
    (0xe8d4a51000000000, 0x0),
    (0x9184e72a00000000, 0x0),
    (0xb5e620f480000000, 0x0),
    (0xe35fa931a0000000, 0x0),
    (0x8e1bc9bf04000000, 0x0),
    (0xb1a2bc2ec5000000, 0x0),
    (0xde0b6b3a76400000, 0x0),
    (0x8ac7230489e80000, 0x0),
    (0xad78ebc5ac620000, 0x0),
    (0xd8d726b7177a8000, 0x0),
    (0x878678326eac9000, 0x0),
    (0xa968163f0a57b400, 0x0),
    (0xd3c21bcecceda100, 0x0),
    (0x84595161401484a0, 0x0),
    (0xa56fa5b99019a5c8, 0x0),
    (0xcecb8f27f4200f3a, 0x0),
    (0x813f3978f8940984, 0x4000000000000000),
    (0xa18f07d736b90be5, 0x5000000000000000),
    (0xc9f2c9cd04674ede, 0xa400000000000000),
    (0xfc6f7c4045812296, 0x4d00000000000000),
    (0x9dc5ada82b70b59d, 0xf020000000000000),
    (0xc5371912364ce305, 0x6c28000000000000),
    (0xf684df56c3e01bc6, 0xc732000000000000),
    (0x9a130b963a6c115c, 0x3c7f400000000000),
    (0xc097ce7bc90715b3, 0x4b9f100000000000),
    (0xf0bdc21abb48db20, 0x1e86d40000000000),
    (0x96769950b50d88f4, 0x1314448000000000),
    (0xbc143fa4e250eb31, 0x17d955a000000000),
    (0xeb194f8e1ae525fd, 0x5dcfab0800000000),
    (0x92efd1b8d0cf37be, 0x5aa1cae500000000),
    (0xb7abc627050305ad, 0xf14a3d9e40000000),
    (0xe596b7b0c643c719, 0x6d9ccd05d0000000),
    (0x8f7e32ce7bea5c6f, 0xe4820023a2000000),
    (0xb35dbf821ae4f38b, 0xdda2802c8a800000),
    (0xe0352f62a19e306e, 0xd50b2037ad200000),
    (0x8c213d9da502de45, 0x4526f422cc340000),
    (0xaf298d050e4395d6, 0x9670b12b7f410000),
    (0xdaf3f04651d47b4c, 0x3c0cdd765f114000),
    (0x88d8762bf324cd0f, 0xa5880a69fb6ac800),
    (0xab0e93b6efee0053, 0x8eea0d047a457a00),
    (0xd5d238a4abe98068, 0x72a4904598d6d880),
    (0x85a36366eb71f041, 0x47a6da2b7f864750),
    (0xa70c3c40a64e6c51, 0x999090b65f67d924),
    (0xd0cf4b50cfe20765, 0xfff4b4e3f741cf6d),
    (0x82818f1281ed449f, 0xbff8f10e7a8921a4),
    (0xa321f2d7226895c7, 0xaff72d52192b6a0d),
    (0xcbea6f8ceb02bb39, 0x9bf4f8a69f764490),
    (0xfee50b7025c36a08, 0x2f236d04753d5b4),
    (0x9f4f2726179a2245, 0x1d762422c946590),
    (0xc722f0ef9d80aad6, 0x424d3ad2b7b97ef5),
    (0xf8ebad2b84e0d58b, 0xd2e0898765a7deb2),
    (0x9b934c3b330c8577, 0x63cc55f49f88eb2f),
    (0xc2781f49ffcfa6d5, 0x3cbf6b71c76b25fb),
    (0xf316271c7fc3908a, 0x8bef464e3945ef7a),
    (0x97edd871cfda3a56, 0x97758bf0e3cbb5ac),
    (0xbde94e8e43d0c8ec, 0x3d52eeed1cbea317),
    (0xed63a231d4c4fb27, 0x4ca7aaa863ee4bdd),
    (0x945e455f24fb1cf8, 0x8fe8caa93e74ef6a),
    (0xb975d6b6ee39e436, 0xb3e2fd538e122b44),
    (0xe7d34c64a9c85d44, 0x60dbbca87196b616),
    (0x90e40fbeea1d3a4a, 0xbc8955e946fe31cd),
    (0xb51d13aea4a488dd, 0x6babab6398bdbe41),
    (0xe264589a4dcdab14, 0xc696963c7eed2dd1),
    (0x8d7eb76070a08aec, 0xfc1e1de5cf543ca2),
    (0xb0de65388cc8ada8, 0x3b25a55f43294bcb),
    (0xdd15fe86affad912, 0x49ef0eb713f39ebe),
    (0x8a2dbf142dfcc7ab, 0x6e3569326c784337),
    (0xacb92ed9397bf996, 0x49c2c37f07965404),
    (0xd7e77a8f87daf7fb, 0xdc33745ec97be906),
    (0x86f0ac99b4e8dafd, 0x69a028bb3ded71a3),
    (0xa8acd7c0222311bc, 0xc40832ea0d68ce0c),
    (0xd2d80db02aabd62b, 0xf50a3fa490c30190),
    (0x83c7088e1aab65db, 0x792667c6da79e0fa),
    (0xa4b8cab1a1563f52, 0x577001b891185938),
    (0xcde6fd5e09abcf26, 0xed4c0226b55e6f86),
    (0x80b05e5ac60b6178, 0x544f8158315b05b4),
    (0xa0dc75f1778e39d6, 0x696361ae3db1c721),
    (0xc913936dd571c84c, 0x3bc3a19cd1e38e9),
    (0xfb5878494ace3a5f, 0x4ab48a04065c723),
    (0x9d174b2dcec0e47b, 0x62eb0d64283f9c76),
    (0xc45d1df942711d9a, 0x3ba5d0bd324f8394),
    (0xf5746577930d6500, 0xca8f44ec7ee36479),
    (0x9968bf6abbe85f20, 0x7e998b13cf4e1ecb),
    (0xbfc2ef456ae276e8, 0x9e3fedd8c321a67e),
    (0xefb3ab16c59b14a2, 0xc5cfe94ef3ea101e),
    (0x95d04aee3b80ece5, 0xbba1f1d158724a12),
    (0xbb445da9ca61281f, 0x2a8a6e45ae8edc97),
    (0xea1575143cf97226, 0xf52d09d71a3293bd),
    (0x924d692ca61be758, 0x593c2626705f9c56),
    (0xb6e0c377cfa2e12e, 0x6f8b2fb00c77836c),
    (0xe498f455c38b997a, 0xb6dfb9c0f956447),
    (0x8edf98b59a373fec, 0x4724bd4189bd5eac),
    (0xb2977ee300c50fe7, 0x58edec91ec2cb657),
    (0xdf3d5e9bc0f653e1, 0x2f2967b66737e3ed),
    (0x8b865b215899f46c, 0xbd79e0d20082ee74),
    (0xae67f1e9aec07187, 0xecd8590680a3aa11),
    (0xda01ee641a708de9, 0xe80e6f4820cc9495),
    (0x884134fe908658b2, 0x3109058d147fdcdd),
    (0xaa51823e34a7eede, 0xbd4b46f0599fd415),
    (0xd4e5e2cdc1d1ea96, 0x6c9e18ac7007c91a),
    (0x850fadc09923329e, 0x3e2cf6bc604ddb0),
    (0xa6539930bf6bff45, 0x84db8346b786151c),
    (0xcfe87f7cef46ff16, 0xe612641865679a63),
    (0x81f14fae158c5f6e, 0x4fcb7e8f3f60c07e),
    (0xa26da3999aef7749, 0xe3be5e330f38f09d),
    (0xcb090c8001ab551c, 0x5cadf5bfd3072cc5),
    (0xfdcb4fa002162a63, 0x73d9732fc7c8f7f6),
    (0x9e9f11c4014dda7e, 0x2867e7fddcdd9afa),
    (0xc646d63501a1511d, 0xb281e1fd541501b8),
    (0xf7d88bc24209a565, 0x1f225a7ca91a4226),
    (0x9ae757596946075f, 0x3375788de9b06958),
    (0xc1a12d2fc3978937, 0x52d6b1641c83ae),
    (0xf209787bb47d6b84, 0xc0678c5dbd23a49a),
    (0x9745eb4d50ce6332, 0xf840b7ba963646e0),
    (0xbd176620a501fbff, 0xb650e5a93bc3d898),
    (0xec5d3fa8ce427aff, 0xa3e51f138ab4cebe),
    (0x93ba47c980e98cdf, 0xc66f336c36b10137),
    (0xb8a8d9bbe123f017, 0xb80b0047445d4184),
    (0xe6d3102ad96cec1d, 0xa60dc059157491e5),
    (0x9043ea1ac7e41392, 0x87c89837ad68db2f),
    (0xb454e4a179dd1877, 0x29babe4598c311fb),
    (0xe16a1dc9d8545e94, 0xf4296dd6fef3d67a),
    (0x8ce2529e2734bb1d, 0x1899e4a65f58660c),
    (0xb01ae745b101e9e4, 0x5ec05dcff72e7f8f),
    (0xdc21a1171d42645d, 0x76707543f4fa1f73),
    (0x899504ae72497eba, 0x6a06494a791c53a8),
    (0xabfa45da0edbde69, 0x487db9d17636892),
    (0xd6f8d7509292d603, 0x45a9d2845d3c42b6),
    (0x865b86925b9bc5c2, 0xb8a2392ba45a9b2),
    (0xa7f26836f282b732, 0x8e6cac7768d7141e),
    (0xd1ef0244af2364ff, 0x3207d795430cd926),
    (0x8335616aed761f1f, 0x7f44e6bd49e807b8),
    (0xa402b9c5a8d3a6e7, 0x5f16206c9c6209a6),
    (0xcd036837130890a1, 0x36dba887c37a8c0f),
    (0x802221226be55a64, 0xc2494954da2c9789),
    (0xa02aa96b06deb0fd, 0xf2db9baa10b7bd6c),
    (0xc83553c5c8965d3d, 0x6f92829494e5acc7),
    (0xfa42a8b73abbf48c, 0xcb772339ba1f17f9),
    (0x9c69a97284b578d7, 0xff2a760414536efb),
    (0xc38413cf25e2d70d, 0xfef5138519684aba),
    (0xf46518c2ef5b8cd1, 0x7eb258665fc25d69),
    (0x98bf2f79d5993802, 0xef2f773ffbd97a61),
    (0xbeeefb584aff8603, 0xaafb550ffacfd8fa),
    (0xeeaaba2e5dbf6784, 0x95ba2a53f983cf38),
    (0x952ab45cfa97a0b2, 0xdd945a747bf26183),
    (0xba756174393d88df, 0x94f971119aeef9e4),
    (0xe912b9d1478ceb17, 0x7a37cd5601aab85d),
    (0x91abb422ccb812ee, 0xac62e055c10ab33a),
    (0xb616a12b7fe617aa, 0x577b986b314d6009),
    (0xe39c49765fdf9d94, 0xed5a7e85fda0b80b),
    (0x8e41ade9fbebc27d, 0x14588f13be847307),
    (0xb1d219647ae6b31c, 0x596eb2d8ae258fc8),
    (0xde469fbd99a05fe3, 0x6fca5f8ed9aef3bb),
    (0x8aec23d680043bee, 0x25de7bb9480d5854),
    (0xada72ccc20054ae9, 0xaf561aa79a10ae6a),
    (0xd910f7ff28069da4, 0x1b2ba1518094da04),
    (0x87aa9aff79042286, 0x90fb44d2f05d0842),
    (0xa99541bf57452b28, 0x353a1607ac744a53),
    (0xd3fa922f2d1675f2, 0x42889b8997915ce8),
    (0x847c9b5d7c2e09b7, 0x69956135febada11),
    (0xa59bc234db398c25, 0x43fab9837e699095),
    (0xcf02b2c21207ef2e, 0x94f967e45e03f4bb),
    (0x8161afb94b44f57d, 0x1d1be0eebac278f5),
    (0xa1ba1ba79e1632dc, 0x6462d92a69731732),
    (0xca28a291859bbf93, 0x7d7b8f7503cfdcfe),
    (0xfcb2cb35e702af78, 0x5cda735244c3d43e),
    (0x9defbf01b061adab, 0x3a0888136afa64a7),
    (0xc56baec21c7a1916, 0x88aaa1845b8fdd0),
    (0xf6c69a72a3989f5b, 0x8aad549e57273d45),
    (0x9a3c2087a63f6399, 0x36ac54e2f678864b),
    (0xc0cb28a98fcf3c7f, 0x84576a1bb416a7dd),
    (0xf0fdf2d3f3c30b9f, 0x656d44a2a11c51d5),
    (0x969eb7c47859e743, 0x9f644ae5a4b1b325),
    (0xbc4665b596706114, 0x873d5d9f0dde1fee),
    (0xeb57ff22fc0c7959, 0xa90cb506d155a7ea),
    (0x9316ff75dd87cbd8, 0x9a7f12442d588f2),
    (0xb7dcbf5354e9bece, 0xc11ed6d538aeb2f),
    (0xe5d3ef282a242e81, 0x8f1668c8a86da5fa),
    (0x8fa475791a569d10, 0xf96e017d694487bc),
    (0xb38d92d760ec4455, 0x37c981dcc395a9ac),
    (0xe070f78d3927556a, 0x85bbe253f47b1417),
    (0x8c469ab843b89562, 0x93956d7478ccec8e),
    (0xaf58416654a6babb, 0x387ac8d1970027b2),
    (0xdb2e51bfe9d0696a, 0x6997b05fcc0319e),
    (0x88fcf317f22241e2, 0x441fece3bdf81f03),
    (0xab3c2fddeeaad25a, 0xd527e81cad7626c3),
    (0xd60b3bd56a5586f1, 0x8a71e223d8d3b074),
    (0x85c7056562757456, 0xf6872d5667844e49),
    (0xa738c6bebb12d16c, 0xb428f8ac016561db),
    (0xd106f86e69d785c7, 0xe13336d701beba52),
    (0x82a45b450226b39c, 0xecc0024661173473),
    (0xa34d721642b06084, 0x27f002d7f95d0190),
    (0xcc20ce9bd35c78a5, 0x31ec038df7b441f4),
    (0xff290242c83396ce, 0x7e67047175a15271),
    (0x9f79a169bd203e41, 0xf0062c6e984d386),
    (0xc75809c42c684dd1, 0x52c07b78a3e60868),
    (0xf92e0c3537826145, 0xa7709a56ccdf8a82),
    (0x9bbcc7a142b17ccb, 0x88a66076400bb691),
    (0xc2abf989935ddbfe, 0x6acff893d00ea435),
    (0xf356f7ebf83552fe, 0x583f6b8c4124d43),
    (0x98165af37b2153de, 0xc3727a337a8b704a),
    (0xbe1bf1b059e9a8d6, 0x744f18c0592e4c5c),
    (0xeda2ee1c7064130c, 0x1162def06f79df73),
    (0x9485d4d1c63e8be7, 0x8addcb5645ac2ba8),
    (0xb9a74a0637ce2ee1, 0x6d953e2bd7173692),
    (0xe8111c87c5c1ba99, 0xc8fa8db6ccdd0437),
    (0x910ab1d4db9914a0, 0x1d9c9892400a22a2),
    (0xb54d5e4a127f59c8, 0x2503beb6d00cab4b),
    (0xe2a0b5dc971f303a, 0x2e44ae64840fd61d),
    (0x8da471a9de737e24, 0x5ceaecfed289e5d2),
    (0xb10d8e1456105dad, 0x7425a83e872c5f47),
    (0xdd50f1996b947518, 0xd12f124e28f77719),
    (0x8a5296ffe33cc92f, 0x82bd6b70d99aaa6f),
    (0xace73cbfdc0bfb7b, 0x636cc64d1001550b),
    (0xd8210befd30efa5a, 0x3c47f7e05401aa4e),
    (0x8714a775e3e95c78, 0x65acfaec34810a71),
    (0xa8d9d1535ce3b396, 0x7f1839a741a14d0d),
    (0xd31045a8341ca07c, 0x1ede48111209a050),
    (0x83ea2b892091e44d, 0x934aed0aab460432),
    (0xa4e4b66b68b65d60, 0xf81da84d5617853f),
    (0xce1de40642e3f4b9, 0x36251260ab9d668e),
    (0x80d2ae83e9ce78f3, 0xc1d72b7c6b426019),
    (0xa1075a24e4421730, 0xb24cf65b8612f81f),
    (0xc94930ae1d529cfc, 0xdee033f26797b627),
    (0xfb9b7cd9a4a7443c, 0x169840ef017da3b1),
    (0x9d412e0806e88aa5, 0x8e1f289560ee864e),
    (0xc491798a08a2ad4e, 0xf1a6f2bab92a27e2),
    (0xf5b5d7ec8acb58a2, 0xae10af696774b1db),
    (0x9991a6f3d6bf1765, 0xacca6da1e0a8ef29),
    (0xbff610b0cc6edd3f, 0x17fd090a58d32af3),
    (0xeff394dcff8a948e, 0xddfc4b4cef07f5b0),
    (0x95f83d0a1fb69cd9, 0x4abdaf101564f98e),
    (0xbb764c4ca7a4440f, 0x9d6d1ad41abe37f1),
    (0xea53df5fd18d5513, 0x84c86189216dc5ed),
    (0x92746b9be2f8552c, 0x32fd3cf5b4e49bb4),
    (0xb7118682dbb66a77, 0x3fbc8c33221dc2a1),
    (0xe4d5e82392a40515, 0xfabaf3feaa5334a),
    (0x8f05b1163ba6832d, 0x29cb4d87f2a7400e),
    (0xb2c71d5bca9023f8, 0x743e20e9ef511012),
    (0xdf78e4b2bd342cf6, 0x914da9246b255416),
    (0x8bab8eefb6409c1a, 0x1ad089b6c2f7548e),
    (0xae9672aba3d0c320, 0xa184ac2473b529b1),
    (0xda3c0f568cc4f3e8, 0xc9e5d72d90a2741e),
    (0x8865899617fb1871, 0x7e2fa67c7a658892),
    (0xaa7eebfb9df9de8d, 0xddbb901b98feeab7),
    (0xd51ea6fa85785631, 0x552a74227f3ea565),
    (0x8533285c936b35de, 0xd53a88958f87275f),
    (0xa67ff273b8460356, 0x8a892abaf368f137),
    (0xd01fef10a657842c, 0x2d2b7569b0432d85),
    (0x8213f56a67f6b29b, 0x9c3b29620e29fc73),
    (0xa298f2c501f45f42, 0x8349f3ba91b47b8f),
    (0xcb3f2f7642717713, 0x241c70a936219a73),
    (0xfe0efb53d30dd4d7, 0xed238cd383aa0110),
    (0x9ec95d1463e8a506, 0xf4363804324a40aa),
    (0xc67bb4597ce2ce48, 0xb143c6053edcd0d5),
    (0xf81aa16fdc1b81da, 0xdd94b7868e94050a),
    (0x9b10a4e5e9913128, 0xca7cf2b4191c8326),
    (0xc1d4ce1f63f57d72, 0xfd1c2f611f63a3f0),
    (0xf24a01a73cf2dccf, 0xbc633b39673c8cec),
    (0x976e41088617ca01, 0xd5be0503e085d813),
    (0xbd49d14aa79dbc82, 0x4b2d8644d8a74e18),
    (0xec9c459d51852ba2, 0xddf8e7d60ed1219e),
    (0x93e1ab8252f33b45, 0xcabb90e5c942b503),
    (0xb8da1662e7b00a17, 0x3d6a751f3b936243),
    (0xe7109bfba19c0c9d, 0xcc512670a783ad4),
    (0x906a617d450187e2, 0x27fb2b80668b24c5),
    (0xb484f9dc9641e9da, 0xb1f9f660802dedf6),
    (0xe1a63853bbd26451, 0x5e7873f8a0396973),
    (0x8d07e33455637eb2, 0xdb0b487b6423e1e8),
    (0xb049dc016abc5e5f, 0x91ce1a9a3d2cda62),
    (0xdc5c5301c56b75f7, 0x7641a140cc7810fb),
    (0x89b9b3e11b6329ba, 0xa9e904c87fcb0a9d),
    (0xac2820d9623bf429, 0x546345fa9fbdcd44),
    (0xd732290fbacaf133, 0xa97c177947ad4095),
    (0x867f59a9d4bed6c0, 0x49ed8eabcccc485d),
    (0xa81f301449ee8c70, 0x5c68f256bfff5a74),
    (0xd226fc195c6a2f8c, 0x73832eec6fff3111),
    (0x83585d8fd9c25db7, 0xc831fd53c5ff7eab),
    (0xa42e74f3d032f525, 0xba3e7ca8b77f5e55),
    (0xcd3a1230c43fb26f, 0x28ce1bd2e55f35eb),
    (0x80444b5e7aa7cf85, 0x7980d163cf5b81b3),
    (0xa0555e361951c366, 0xd7e105bcc332621f),
    (0xc86ab5c39fa63440, 0x8dd9472bf3fefaa7),
    (0xfa856334878fc150, 0xb14f98f6f0feb951),
    (0x9c935e00d4b9d8d2, 0x6ed1bf9a569f33d3),
    (0xc3b8358109e84f07, 0xa862f80ec4700c8),
    (0xf4a642e14c6262c8, 0xcd27bb612758c0fa),
    (0x98e7e9cccfbd7dbd, 0x8038d51cb897789c),
    (0xbf21e44003acdd2c, 0xe0470a63e6bd56c3),
    (0xeeea5d5004981478, 0x1858ccfce06cac74),
    (0x95527a5202df0ccb, 0xf37801e0c43ebc8),
    (0xbaa718e68396cffd, 0xd30560258f54e6ba),
    (0xe950df20247c83fd, 0x47c6b82ef32a2069),
    (0x91d28b7416cdd27e, 0x4cdc331d57fa5441),
    (0xb6472e511c81471d, 0xe0133fe4adf8e952),
    (0xe3d8f9e563a198e5, 0x58180fddd97723a6),
    (0x8e679c2f5e44ff8f, 0x570f09eaa7ea7648),
];
```

## File: `tests/test_api.rs`
```rust
use fast_float2::{parse, parse_partial, FastFloat};

macro_rules! check_ok {
    ($s:expr, $x:expr) => {
        let s = $s;
        check_ok!(s, $x, f32);
        check_ok!(s.as_bytes(), $x, f32);
        check_ok!(s, $x, f64);
        check_ok!(s.as_bytes(), $x, f64);
    };
    ($s:expr, $x:expr, $ty:ty) => {
        assert_eq!(<$ty>::parse_float($s).unwrap(), $x);
        assert_eq!(<$ty>::parse_float_partial($s).unwrap(), ($x, $s.len()));
        assert_eq!(parse::<$ty, _>($s).unwrap(), $x);
        assert_eq!(parse_partial::<$ty, _>($s).unwrap(), ($x, $s.len()));
    };
}

macro_rules! check_ok_partial {
    ($s:expr, $x:expr, $n:expr) => {
        let s = $s;
        check_ok_partial!(s, $x, $n, f32);
        check_ok_partial!(s.as_bytes(), $x, $n, f32);
        check_ok_partial!(s, $x, $n, f64);
        check_ok_partial!(s.as_bytes(), $x, $n, f64);
    };
    ($s:expr, $x:expr, $n:expr, $ty:ty) => {
        assert!(<$ty>::parse_float($s).is_err());
        assert_eq!(<$ty>::parse_float_partial($s).unwrap(), ($x, $n));
        assert!(parse::<$ty, _>($s).is_err());
        assert_eq!(parse_partial::<$ty, _>($s).unwrap(), ($x, $n));
    };
}

macro_rules! check_err {
    ($s:expr) => {
        let s = $s;
        check_err!(s, f32);
        check_err!(s.as_bytes(), f32);
        check_err!(s, f64);
        check_err!(s.as_bytes(), f64);
    };
    ($s:expr, $ty:ty) => {
        assert!(<$ty>::parse_float($s).is_err());
        assert!(<$ty>::parse_float_partial($s).is_err());
        assert!(parse::<$ty, _>($s).is_err());
        assert!(parse_partial::<$ty, _>($s).is_err());
    };
}

#[test]
fn test_api() {
    check_ok!("1.23", 1.23);
    check_ok!("0.", 0.);
    check_ok!("-0", 0.);
    check_ok!("+00", 0.);
    check_ok!("-0001e-02", -0.01);
    check_ok!("345", 345.);

    check_ok_partial!("1a", 1., 1);
    check_ok_partial!("-2e-1x", -0.2, 5);
    check_ok_partial!("2e2.", 200., 3);
    check_ok_partial!("2ea", 2., 1);

    check_err!("");
    check_err!(" ");
    check_err!(".");
    check_err!(".e1");
    check_err!("+");
    check_err!("-");
    check_err!("x");
    check_err!("a123");
}
```

## File: `tests/test_basic.rs`
```rust
use std::str::FromStr;

use hexf_parse::{parse_hexf32, parse_hexf64};

fn hexf32(s: &str) -> f32 {
    parse_hexf32(s, false).unwrap()
}

fn hexf64(s: &str) -> f64 {
    parse_hexf64(s, false).unwrap()
}

macro_rules! check {
    ($ty:ident, $s:expr) => {{
        check!($ty, stringify!($s), $s)
    }};
    ($ty:ident, $s:expr,inf) => {{
        check!($ty, $s, core::$ty::INFINITY)
    }};
    ($ty:ident, $s:expr,neg_inf) => {{
        check!($ty, $s, core::$ty::NEG_INFINITY)
    }};
    ($ty:ident, $s:expr, $e:expr) => {{
        let string = String::from($s);
        let s = string.as_bytes();
        let expected: $ty = $e;
        let result = fast_float2::parse::<$ty, _>(s).unwrap();
        assert_eq!(result, expected);
        let lex = lexical_core::parse::<$ty>(s).unwrap();
        assert_eq!(result, lex);
        let std = <$ty>::from_str(string.as_str());
        if let Ok(std) = std {
            // stdlib can't parse all weird floats
            if std.is_finite() && result.is_finite() {
                // some weird edge cases stdlib parses as inf, e.g. 0e999999999999999
                assert_eq!(result, std);
            }
        }
    }};
}
macro_rules! check_lex {
    ($ty:ident, $s:expr) => {{
        let v = lexical_core::parse::<$ty>($s.as_bytes()).unwrap();
        check!($ty, $s, v);
    }};
}
macro_rules! check_f32 {
    ($($tt:tt)+) => {
        check!(f32, $($tt)+)
    }
}
macro_rules! check_f64 {
    ($($tt:tt)+) => {
        check!(f64, $($tt)+)
    }
}
macro_rules! check_f32_lex {
    ($s:expr) => {
        check_lex!(f32, $s)
    };
}
macro_rules! check_f64_lex {
    ($s:expr) => {
        check_lex!(f64, $s)
    };
}
macro_rules! check_f32_inf {
    ($s:expr) => {
        check!(f32, $s, inf)
    };
}
macro_rules! check_f32_neg_inf {
    ($s:expr) => {
        check!(f32, $s, neg_inf)
    };
}
macro_rules! check_f64_inf {
    ($s:expr) => {
        check!(f64, $s, inf)
    };
}
macro_rules! check_f64_neg_inf {
    ($s:expr) => {
        check!(f64, $s, neg_inf)
    };
}

fn append_zeros(s: impl AsRef<str>, n: usize) -> String {
    let mut s = String::from(s.as_ref());
    for _ in 0..n {
        s.push('0');
    }
    s
}

#[test]
fn test_f64_inf() {
    check_f64_inf!("INF");
    check_f64_inf!("INFINITY");
    check_f64_inf!("infinity");
    check_f64_inf!("inf");
    check_f64_inf!("1234456789012345678901234567890e9999999999999999999999999999");
    check_f64_inf!("1.832312213213213232132132143451234453123412321321312e308");
    check_f64_inf!("2e30000000000000000");
    check_f64_inf!("2e3000");
    check_f64_inf!("1.8e308");
    check_f64_inf!("1.9e308");

    check_f64_neg_inf!("-INF");
    check_f64_neg_inf!("-INFINITY");
    check_f64_neg_inf!("-infinity");
    check_f64_neg_inf!("-inf");
    check_f64_neg_inf!("-2139879401095466344511101915470454744.9813888656856943E+272");
}

#[test]
fn test_f64_long() {
    check_f64!(
        "\
         9355950000000000000.000000000000000000000000000000000018446744073709551616000001\
         84467440737095516161844674407370955161407370955161618446744073709551616000184467\
         44073709551616600000184467440737095516161844674407370955161407370955161618446744\
         07370955161600018446744073709551616018446744073709556744516161844674407370955161\
         40737095516161844674407370955161600018446744073709551616018446744073709551611616\
         00018446744073709500184467440737095516160018446744073709551616001844674407370955\
         11681644674407370955161600018440737095516160184467440737095516161844674407370955\
         16160001844674407536910751601611616000184467440737095001844674407370955161600184\
         46744073709551616001844674407370955161618446744073709551616000184495516161844674\
         4073709551616000184467440753691075160018446744073709",
        hexf64("0x1.03ae05e8fca1cp+63")
    );
    check_f64!(
        "\
         2.225073858507202124188701479202220329072405282794390378143031338374351073192441\
         94686754406432563881851382188218502438069999947733013005649884107791928741341929\
         29720097048195199306799329096904278406473168204156592672863293363047467012331685\
         29834221527445172608358596545663192828352447877877998943107797838336991592885945\
         55213714181128458251145584319223079897504395086859412457230891738946169368372321\
         19137365897797772328669884035639025104444303545739673370658398105542045669382465\
         84137476071559811765738776267476659123871999319040063173347090030127901881752034\
         47190250028061277777916798391090578584006464715943810511489154282775041174682194\
         13395246668250343130618158782937900420539237507208336669324158000275839111885418\
         8641513168478436313080237596295773983001708984375e-308",
        hexf64("0x1.0000000000002p-1022")
    );
    check_f64_inf!(
        "\
         14384566631413902735261182076422355811832278452463312311626366537903681520913941\
         96930365828634687637948157940776599182791387527135353034738357134110310609455693\
         90082419354977279201654318268051974058035436546798544018359870131225762454556233\
         13970183299286131961255902741877200739148180625308303165331580986249841188892982\
         81371812288789537310599037529113415438738954894752124724983067241108764488346454\
         37669901867307840475112141480493722424080599312381693232622368309077056159757045\
         77939329858261626042558845291341263962822021265262533893834218067279545885255961\
         14379801269094096329805054803089299736996870951258573010877404407451953846698609\
         19821392688269207855703322826525930548119852605981316446918758669325733577952202\
         04076454986842633399219052275566166981299674128912822316855046606712779271982900\
         09824680186319750978665734576683784255802269708917361719466043175201158849097881\
         37047711185017157986905601606166617302905958843377601564443970505037755427769614\
         39282780934537928038462527159660167332226464423828921239400524413468224297215938\
         84378212558701004356924243030059517489346646577724622498919752597382095222500311\
         12418182351225107135618176937657765139002829779615620881537508915912839494571051\
         58613344862671017974971111259092725051947928708896171797587034426080161433432621\
         59998149700606597792535574457560429226974273443630323818747730771316763398572110\
         87495998192373246307688452867739265415001026982223940199342748237651323138921235\
         35835735663769155726509168665536123661873789595549835667127670933729060301889762\
         20169058025354973622211666504549316958271880975697143546564469806791358707318873\
         07570838334500409015197406832583817753126695417740666139222980134999469594150993\
         5655355652985723782153570084089560139142231.738475042362596875449154552392299548\
         94713816208169416867534067784380761312978044932336375902701297246698737092181681\
         31626587547265451210905455072402670004565947865409496052607224619378706306348749\
         91729398208026467698131898691830012167897399682179601734569071423681e-733"
    );
    check_f64_lex!(
        "\
         0.000000000000000000000000000000000000000000000000000000000000000000000000000000\
         00000000000000000000000000000000000000000000000000000000000000000000000000000000\
         00000000000000000000000000000000000000000000000000000000000000000000000000000000\
         00000000000000000000000000000000000000000000000000000000000000000000044501477170\
         14402272114819593418263951869639092703291296046852219449644444042153891033059047\
         81627017582829831782607924221374017287738918929105531441481564124348675997628212\
         65346585071045737627442980259622449029037796981144446145705102663115100318287949\
         52795966823603998647925096578034214163701381261333311989876551545144031526125381\
         32666529513060001849177663286607555958373922409899478075565940981010216121988146\
         05258742579179000071675999344145086087205681577915435923018910334964869420614052\
         18289243144579760516365090360651414037721744226256159024466852576737244643007551\
         33324500796506867194913776884780053099639677097589658441378944337966219939673169\
         36280457084866613206797017728916080020698679408551343728867675409720757232455434\
         770912461317493580281734466552734375"
    );
    check_f64_lex!(
        "\
         0.000000000000000000000000000000000000000000000000000000000000000000000000000000\
         00000000000000000000000000000000000000000000000000000000000000000000000000000000\
         00000000000000000000000000000000000000000000000000000000000000000000000000000000\
         00000000000000000000000000000000000000000000000000000000000000000000022250738585\
         07200889024586876085859887650423112240959465493524802562440009228235695178775888\
         80375915526423097809504343120858773871583572918219930202943792242235598198275012\
         42041788969571311791082261043971979604000454897391938079198936081525613113376149\
         84204327175103362739154978273159414382813627511383860409424946494228631669542910\
         50802018159266421349966065178030950759130587198464239060686371020051087232827846\
         78843631944515866135041223479014792369585208321597621066375401613736583044193603\
         71477835530668283453563400507407304013560296804637591858316312422452159926254649\
         43008368518617194224176464551371354201322170313704965832101546540680353974179060\
         22589503023501937519773030945763173210852507299305089761582519159720757232455434\
         770912461317493580281734466552734375"
    );
}

#[test]
fn test_f64_general() {
    check_f64!("9007199254740993.0", hexf64("0x1.p+53"));
    check_f64!(append_zeros("9007199254740993.0", 1000), hexf64("0x1.p+53"));
    check_f64!("10000000000000000000", hexf64("0x1.158e460913dp+63"));
    check_f64!("10000000000000000000000000000001000000000000", hexf64("0x1.cb2d6f618c879p+142"));
    check_f64!("10000000000000000000000000000000000000000001", hexf64("0x1.cb2d6f618c879p+142"));
    check_f64!(1.1920928955078125e-07);
    check_f64!("-0", -0.0);
    check_f64!("1.0000000000000006661338147750939242541790008544921875", 1.0000000000000007);
    check_f64!("1090544144181609348835077142190", hexf64("0x1.b8779f2474dfbp+99"));
    check_f64!(2.2250738585072013e-308);
    check_f64!(-92666518056446206563E3);
    check_f64!(-92666518056446206563E3);
    check_f64!(-42823146028335318693e-128);
    check_f64!(90054602635948575728E72);
    check_f64_lex!(
        "\
         1.000000000000001885589208702234638701745660206917535153946435506630705583683732\
         21972569761144603605635692374830246134201063722058e-309"
    );
    check_f64!("0e9999999999999999999999999999", 0.0);
    check_f64!(-2402844368454405395.2);
    check_f64!(2402844368454405395.2);
    check_f64!(7.0420557077594588669468784357561207962098443483187940792729600000e+59);
    check_f64!(7.0420557077594588669468784357561207962098443483187940792729600000e+59);
    check_f64!(-1.7339253062092163730578609458683877051596800000000000000000000000e+42);
    check_f64!(-2.0972622234386619214559824785284023792871122537545728000000000000e+52);
    check_f64!(-1.0001803374372191849407179462120053338028379051879898808320000000e+57);
    check_f64!(-1.8607245283054342363818436991534856973992070520151142825984000000e+58);
    check_f64!(-1.9189205311132686907264385602245237137907390376574976000000000000e+52);
    check_f64!(-2.8184483231688951563253238886553506793085187889855201280000000000e+54);
    check_f64!(-1.7664960224650106892054063261344555646357024359107788800000000000e+53);
    check_f64!(-2.1470977154320536489471030463761883783915110400000000000000000000e+45);
    check_f64!(-4.4900312744003159009338275160799498340862630046359789166919680000e+61);
    check_f64!("+1", 1.0);
    check_f64!("1.797693134862315700000000000000001e308", 1.7976931348623157e308);
    check_f64!("3e-324", hexf64("0x0.0000000000001p-1022"));
    check_f64!("1.00000006e+09", hexf64("0x1.dcd651ep+29"));
    check_f64!("4.9406564584124653e-324", hexf64("0x0.0000000000001p-1022"));
    check_f64!("4.9406564584124654e-324", hexf64("0x0.0000000000001p-1022"));
    check_f64!("2.2250738585072009e-308", hexf64("0x0.fffffffffffffp-1022"));
    check_f64!("2.2250738585072014e-308", hexf64("0x1.p-1022"));
    check_f64!("1.7976931348623157e308", hexf64("0x1.fffffffffffffp+1023"));
    check_f64!("1.7976931348623158e308", hexf64("0x1.fffffffffffffp+1023"));
    check_f64!(4503599627370496.5);
    check_f64!(4503599627475352.5);
    check_f64!(4503599627475353.5);
    check_f64!(2251799813685248.25);
    check_f64!(1125899906842624.125);
    check_f64!(1125899906842901.875);
    check_f64!(2251799813685803.75);
    check_f64!(4503599627370497.5);
    check_f64!(45035996.273704995);
    check_f64!(45035996.273704985);
    check_f64!(1.2345e30);
}

#[test]
fn test_f32_inf() {
    check_f32_inf!("INF");
    check_f32_inf!("INFINITY");
    check_f32_inf!("infinity");
    check_f32_inf!("inf");
    check_f32_inf!("1234456789012345678901234567890e9999999999999999999999999999");
    check_f32_inf!("2e3000");
    check_f32_inf!("3.5028234666e38");

    check_f32_neg_inf!("-INF");
    check_f32_neg_inf!("-INFINITY");
    check_f32_neg_inf!("-infinity");
    check_f32_neg_inf!("-inf");
}

#[test]
fn test_f32_basic() {
    let f1 = "\
        1.175494140627517859246175898662808184331245864732796240031385942718174675986064\
        7699724722770042717456817626953125";
    check_f32!(f1, hexf32("0x1.2ced3p+0"));
    check_f32!(format!("{}e-38", f1), hexf32("0x1.fffff8p-127"));
    check_f32!(format!("{}e-38", append_zeros(f1, 655)), hexf32("0x1.fffff8p-127"));
    check_f32!(format!("{}e-38", append_zeros(f1, 656)), hexf32("0x1.fffff8p-127"));
    check_f32!(format!("{}e-38", append_zeros(f1, 1000)), hexf32("0x1.fffff8p-127"));
    check_f32!(1.00000006e+09);
    check_f32!(1.4012984643e-45);
    check_f32!(1.1754942107e-38);
    check_f32!(1.1754943508e-45);
    check_f32!("-0", -0.0);
    check_f32!("1090544144181609348835077142190", hexf32("0x1.b877ap+99"));
    check_f32!(1.1754943508e-38);
    check_f32!(30219.0830078125);
    check_f32!(16252921.5);
    check_f32!(5322519.25);
    check_f32!(3900245.875);
    check_f32!(1510988.3125);
    check_f32!(782262.28125);
    check_f32!(328381.484375);
    check_f32!(156782.0703125);
    check_f32!(85003.24609375);
    check_f32!(43827.048828125);
    check_f32!(17419.6494140625);
    check_f32!(15498.36376953125);
    check_f32!(6318.580322265625);
    check_f32!(2525.2840576171875);
    check_f32!(1370.9265747070312);
    check_f32!(936.3702087402344);
    check_f32!(411.88682556152344);
    check_f32!(206.50310516357422);
    check_f32!(124.16878890991211);
    check_f32!(50.811574935913086);
    check_f32!(17.486443519592285);
    check_f32!(13.91745138168335);
    check_f32!("7.5464513301849365", hexf32("0x1.e2f90ep+2"));
    check_f32!(2.687217116355896);
    check_f32!("1.1877630352973938", hexf32("0x1.30113ep+0"));
    check_f32!(0.7622503340244293);
    check_f32!("0.30531780421733856", hexf32("0x1.38a53ap-2"));
    check_f32!("0.21791061013936996", hexf32("0x1.be47eap-3"));
    check_f32!("0.09289376810193062", hexf32("0x1.7c7e2ep-4"));
    check_f32!(0.03706067614257336);
    check_f32!(0.028068351559340954);
    check_f32!("0.012114629615098238", hexf32("0x1.8cf8e2p-7"));
    check_f32!("0.004221370676532388", hexf32("0x1.14a6dap-8"));
    check_f32!(0.002153817447833717);
    check_f32!("0.0015924838953651488", hexf32("0x1.a175cap-10"));
    check_f32!(0.0008602388261351734);
    check_f32!("0.00036393293703440577", hexf32("0x1.7d9c82p-12"));
    check_f32!(0.00013746770127909258);
    check_f32!(16407.9462890625);
    check_f32!("1.1754947011469036e-38", hexf32("0x1.000006p-126"));
    check_f32!("7.0064923216240854e-46", hexf32("0x1.p-149"));
    check_f32!(8388614.5);
    check_f32!("0e9999999999999999999999999999", 0.);
    check_f32!(
        "4.7019774032891500318749461488889827112746622270883500860350068251e-38",
        4.7019774032891500318749461488889827112746622270883500860350068251e-38
    );
    check_f32_lex!(
        "\
         3.141592653589793238462643383279502884197169399375105820974944592307816406286208\
         9986280348253421170679"
    );
    check_f32!(
        "2.3509887016445750159374730744444913556373311135441750430175034126e-38",
        2.3509887016445750159374730744444913556373311135441750430175034126e-38
    );
    check_f32!("+1", 1.);
    check_f32!("7.0060e-46", 0.);
    check_f32!("3.4028234664e38", hexf32("0x1.fffffep+127"));
    check_f32!("3.4028234665e38", hexf32("0x1.fffffep+127"));
    check_f32!("3.4028234666e38", hexf32("0x1.fffffep+127"));
    check_f32_lex!(
        "\
         0.000000000000000000000000000000000000011754943508222875079687365372222456778186\
         655567720875215087517062784172594547271728515625"
    );
    check_f32_lex!(
        "\
         0.000000000000000000000000000000000000000000001401298464324817070923729583289916\
         13128026194187651577175706828388979108268586060148663818836212158203125"
    );
    check_f32_lex!(
        "\
         0.000000000000000000000000000000000000023509885615147285834557659820715330266457\
         17985517980855365926236850006129930346077117064851336181163787841796875"
    );
    check_f32_lex!(
        "\
         0.000000000000000000000000000000000000011754942106924410754870294448492873488270\
         52428745893333857174530571588870475618904265502351336181163787841796875"
    );
    check_f32!(1.2345e15);
}

#[test]
fn test_f64_pow10() {
    for i in -308..=308 {
        let s = format!("1e{}", i);
        let v = f64::from_str(&s).unwrap();
        assert_eq!(fast_float2::parse::<f64, _>(s).unwrap(), v);
    }
}

#[test]
fn test_f32_pow10() {
    for i in -38..=38 {
        let s = format!("1e{}", i);
        let v = f32::from_str(&s).unwrap();
        assert_eq!(fast_float2::parse::<f32, _>(s).unwrap(), v);
    }
}
```

## File: `tests/test_exhaustive.rs`
```rust
#[test]
#[ignore]
fn test_f32_exhaustive_ryu() {
    let mut buf = ryu::Buffer::new();
    for i in 0..0xFFFF_FFFF_u32 {
        let a: f32 = unsafe { core::mem::transmute(i) };
        let s = buf.format(a);
        let b: f32 = fast_float2::parse(s).unwrap();
        assert!(a == b || (a.is_nan() && b.is_nan()));
    }
}
```

## File: `tests/test_random.rs`
```rust
#[test]
#[ignore]
fn test_f64_random_from_u64() {
    const N_ITER: u64 = 1 << 32;

    let mut rng = fastrand::Rng::with_seed(0);
    let mut buf = ryu::Buffer::new();
    for _ in 0..N_ITER {
        let i: u64 = rng.u64(0..0xFFFF_FFFF_FFFF_FFFF);
        let a: f64 = unsafe { core::mem::transmute(i) };
        let s = buf.format(a);
        let b: f64 = fast_float2::parse(s).unwrap();
        assert!(a == b || (a.is_nan() && b.is_nan()));
    }
}
```

