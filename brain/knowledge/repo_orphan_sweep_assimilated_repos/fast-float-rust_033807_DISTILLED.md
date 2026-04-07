---
id: fast-float-rust
type: knowledge
owner: OA_Triage
---
# fast-float-rust
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: extras\data-tests\README.md
```md
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

### File: extras\simple-bench\README.md
```md
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

### File: CHANGELOG.md
```md
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

### File: SECURITY.md
```md
# Security Policy

This crate is in maintenance mode, so only the latest version is supported and will be receiving bug fixes. If you have a security vulnerability, please reach out to me privately at [ahuszagh@gmail.com](mailto:ahuszagh@gmail.com). Other forms of communication may not reach me.

```

### File: src\binary.rs
```rs
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

### File: src\common.rs
```rs
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

### File: src\decimal.rs
```rs
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

### File: src\float.rs
```rs
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

### File: src\lib.rs
```rs
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

### File: src\number.rs
```rs
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
