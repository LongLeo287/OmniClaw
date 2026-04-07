---
id: quickcheck
type: knowledge
owner: OA_Triage
---
# quickcheck
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# quickcheck

QuickCheck is a way to do property based testing using randomly generated
input. This crate comes with the ability to randomly generate and shrink
integers, floats, tuples, booleans, lists, strings, options and results.
All QuickCheck needs is a property function—it will then randomly generate
inputs to that function and call the property for each set of inputs. If the
property fails (whether by a runtime error like index out-of-bounds or by not
satisfying your property), the inputs are "shrunk" to find a smaller
counter-example.

The shrinking strategies for lists and numbers use a binary search to cover
the input space quickly. (It should be the same strategy used in
[Koen Claessen's QuickCheck for
Haskell](https://hackage.haskell.org/package/QuickCheck).)

[![Build status](https://github.com/BurntSushi/quickcheck/workflows/ci/badge.svg)](https://github.com/BurntSushi/quickcheck/actions)
[![crates.io](https://img.shields.io/crates/v/quickcheck.svg)](https://crates.io/crates/quickcheck)

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org/).

## Documentation

The API is fully documented:
[https://docs.rs/quickcheck](https://docs.rs/quickcheck).

## Simple example

Here's an example that tests a function that reverses a vector:

```rust
fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for x in xs.iter() {
        rev.insert(0, x.clone())
    }
    rev
}

#[cfg(test)]
mod tests {
    use quickcheck::quickcheck;
    use super::reverse;

    quickcheck! {
        fn prop(xs: Vec<u32>) -> bool {
            xs == reverse(&reverse(&xs))
        }
  }
}
```

This example uses the `quickcheck!` macro, which is backwards compatible with
old versions of Rust.

## The `#[quickcheck]` attribute

To make it easier to write QuickCheck tests, the `#[quickcheck]` attribute
will convert a property function into a `#[test]` function.

To use the `#[quickcheck]` attribute, you must import the `quickcheck` macro
from the `quickcheck_macros` crate:

```rust
fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for x in xs {
        rev.insert(0, x.clone())
    }
    rev
}

#[cfg(test)]
mod tests {
    use quickcheck_macros::quickcheck;
    use super::reverse;

    #[quickcheck]
    fn double_reversal_is_identity(xs: Vec<isize>) -> bool {
        xs == reverse(&reverse(&xs))
    }
}
```

## Installation

`quickcheck` is on `crates.io`, so you can include it in your project like so:

```toml
[dependencies]
quickcheck = "1"
```

If you're only using `quickcheck` in your test code, then you can add it as a
development dependency instead:

```toml
[dev-dependencies]
quickcheck = "1"
```

If you want to use the `#[quickcheck]` attribute, then add `quickcheck_macros`

```toml
[dev-dependencies]
quickcheck = "1"
quickcheck_macros = "1"
```

N.B. When using `quickcheck` (either directly or via the attributes),
`RUST_LOG=quickcheck` enables `info!` so that it shows useful output
(like the number of tests passed). This is **not** needed to show
witnesses for failures.

Crate features:

- `"use_logging"`: (Enabled by default.) Enables the log messages governed
  `RUST_LOG`.
- `"regex"`: (Enabled by default.) Enables the use of regexes with
  `env_logger`.

## Minimum Rust version policy

This crate's minimum supported `rustc` version is `1.85.0`.

The current policy is that the minimum Rust version required to use this crate
can be increased in minor version updates. For example, if `crate 1.0` requires
Rust 1.20.0, then `crate 1.0.z` for all values of `z` will also require Rust
1.20.0 or newer. However, `crate 1.y` for `y > 0` may require a newer minimum
version of Rust.

In general, this crate will be conservative with respect to the minimum
supported version of Rust.

With all of that said, currently, `rand` is a public dependency of
`quickcheck`. Therefore, the MSRV policy above only applies when it is more
aggressive than `rand`'s MSRV policy. Otherwise, `quickcheck` will defer to
`rand`'s MSRV policy.

## Compatibility

In general, this crate considers the `Arbitrary` implementations provided as
implementation details. Strategies may or may not change over time, which may
cause new test failures, presumably due to the discovery of new bugs due to a
new kind of witness being generated. These sorts of changes may happen in
semver compatible releases.

## Alternative Rust crates for property testing

The [`proptest`](https://docs.rs/proptest) crate is inspired by the
[Hypothesis](https://hypothesis.works/) framework for Python.
You can read a comparison between `proptest` and `quickcheck`
[here](https://github.com/proptest-rs/proptest/blob/main/proptest/README.md#differences-between-quickcheck-and-proptest)
and
[here](https://github.com/proptest-rs/proptest/issues/15#issuecomment-348382287).
In particular, `proptest` improves on the concept of shrinking. So if you've
ever had problems/frustration with shrinking in `quickcheck`, then `proptest`
might be worth a try!

## Alternatives for fuzzing

Please see the
[Rust Fuzz Book](https://rust-fuzz.github.io/book/introduction.html)
and the
[`arbitrary`](https://crates.io/crates/arbitrary) crate.

## Discarding test results (or, properties are polymorphic!)

Sometimes you want to test a property that only holds for a *subset* of the
possible inputs, so that when your property is given an input that is outside
of that subset, you'd discard it. In particular, the property should *neither*
pass nor fail on inputs outside of the subset you want to test. But properties
return boolean values—which either indicate pass or fail.

To fix this, we need to take a step back and look at the type of the
`quickcheck` function:

```rust
pub fn quickcheck<A: Testable>(f: A) {
    // elided
}
```

So `quickcheck` can test any value with a type that satisfies the `Testable`
trait. Great, so what is this `Testable` business?

```rust
pub trait Testable {
    fn result(&self, &mut Gen) -> TestResult;
}
```

This trait states that a type is testable if it can produce a `TestResult`
given a source of randomness. (A `TestResult` stores information about the
results of a test, like whether it passed, failed or has been discarded.)

Sure enough, `bool` satisfies the `Testable` trait:

```rust
impl Testable for bool {
    fn result(&self, _: &mut Gen) -> TestResult {
        TestResult::from_bool(*self)
    }
}
```

But in the example, we gave a *function* to `quickcheck`. Yes, functions can
satisfy `Testable` too!

```rust
impl<A: Arbitrary + Debug, B: Testable> Testable for fn(A) -> B {
    fn result(&self, g: &mut Gen) -> TestResult {
        // elided
    }
}
```

Which says that a function satisfies `Testable` if and only if it has a single
parameter type (whose values can be randomly generated and shrunk) and returns
any type (that also satisfies `Testable`). So a function with type `fn(usize)
-> bool` satisfies `Testable` since `usize` satisfies `Arbitrary` and `bool`
satisfies `Testable`.

So to discard a test, we need to return something other than `bool`. What if we
just returned a `TestResult` directly? That should work, but we'll need to
make sure `TestResult` satisfies `Testable`:

```rust
impl Testable for TestResult {
    fn result(&self, _: &mut Gen) -> TestResult { self.clone() }
}
```

Now we can test functions that return a `TestResult` directly.

As an example, let's test our reverse function to make sure that the reverse of
a vector of length 1 is equal to the vector itself.

```rust
fn prop(xs: Vec<isize>) -> TestResult {
    if xs.len() != 1 {
        return TestResult::discard()
    }
    TestResult::from_bool(xs == reverse(&xs))
}
quickcheck(prop as fn(Vec<isize>) -> TestResult);
```

(A full working program for this example is in
[`examples/reverse_single.rs`](https://github.com/BurntSushi/quickcheck/blob/master/examples/reverse_single.rs).)

So now our property returns a `TestResult`, which allows us to encode a bit
more information. There are a few more
[convenience functions defined for the `TestResult`
type](https://docs.rs/quickcheck/*/quickcheck/struct.TestResult.html).
For example, we can't just return a `bool`, so we convert a `bool` value to a
`TestResult`.

(The ability to discard tests allows you to get similar functionality as
Haskell's `==>` combinator.)

N.B. Since discarding a test means it neither passes nor fails, `quickcheck`
will try to replace the discarded test with a fresh one. However, if your
condition is seldom met, it's possible that `quickcheck` will have to settle
for running fewer tests than usual. By default, if `quickcheck` can't find
`100` valid tests after trying `10,000` times, then it will give up.
These parameters may be changed using
[`QuickCheck::tests`](https://docs.rs/quickcheck/*/quickcheck/struct.QuickCheck.html#method.tests)
and [`QuickCheck::max_tests`](https://docs.rs/quickcheck/*/quickcheck/struct.QuickCheck.html#method.max_tests),
or by setting the `QUICKCHECK_TESTS` and `QUICKCHECK_MAX_TESTS`
environment variables.
There is also `QUICKCHECK_MIN_TESTS_PASSED` which sets the minimum number of
valid tests that need pass (defaults to `0`) in order for it to be considered a
success.

## Shrinking

Shrinking is a crucial part of QuickCheck that simplifies counter-examples for
your properties automatically. For example, if you erroneously defined a
function for reversing vectors as: (my apologies for the contrived example)

```rust
fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for i in 1..xs.len() {
        rev.insert(0, xs[i].clone())
    }
    rev
}
```

And a property to test that `xs == reverse(reverse(xs))`:

```rust
fn prop(xs: Vec<isize>) -> bool {
    xs == reverse(&reverse(&xs))
}
quickcheck(prop as fn(Vec<isize>) -> bool);
```

Then without shrinking, you might get a counter-example like:

```text
[quickcheck] TEST FAILED. Arguments: ([-17, 13, -12, 17, -8, -10, 15, -19,
-19, -9, 11, -5, 1, 19, -16, 6])
```

Which is pretty mysterious. But with shrinking enabled, you're nearly
guaranteed to get this counter-example every time:

```text
[quickcheck] TEST FAILED. Arguments: ([0])
```

Which is going to be much easier to debug.

## More Thorough Checking

Quickcheck uses random input to test, so it won't
always find bugs that could be uncovered with a particular
property. You can improve your odds of finding these latent
bugs by spending more CPU cycles asking quickcheck to find
them for you. There are a few different ways to do this, and
which one you choose is mostly a matter of taste.

If you are finding yourself doing this sort of thing a
lot, you might also be interested in trying out
[`cargo fuzz`](https://github.com/rust-fuzz/cargo-fuzz),
which runs in a loop by default.

### Running in a Loop

One approach is to run your quickcheck properties in a loop that
just keeps going until you tell it to stop or it finds a bug.
For example, you could use a bash script such as the following
one.

```bash
#!/usr/bin/bash

while true
do
    cargo test qc_
    if [[ x$? != x0 ]] ; then
        exit $?
    fi
done
```

One thing to note is that this script passes the `qc_` filter to
`cargo test`. This assumes that you've prefixed all your quickcheck
properties with `qc_`. You could leave off the filter, but then
you would be running all your deterministic tests as well, which
would take time away from quickcheck!

Checking the return code and exiting is also important. Without that
test, you won't ever notice when a failure happens.

### Cranking the Number of Tests

Another approach is to just ask quickcheck to run properties more
times. You can do this either via the
[tests()](https://docs.rs/quickcheck/*/quickcheck/struct.QuickCheck.html#method.tests)
method, or via the `QUICKCHECK_TESTS` environment variable.
This will cause quickcheck to run for a much longer time. Unlike,
the loop approach this will take a bounded amount of time, which
makes it more suitable for something like a release cycle that
wants to really hammer your software.

### Making Arbitrary Smarter

This approach entails spending more time generating interesting
inputs in your implementations of Arbitrary. The idea is to
focus on the corner cases. This approach can be tricky because
programmers are not usually great at intuiting corner cases,
and the whole idea of property checking is to take that burden
off the programmer. Despite the theoretical discomfort, this
approach can turn out to be practical.

## Generating Structs

It is very simple to generate structs in QuickCheck. Consider the following
example, where the struct `Point` is defined:

```rust
struct Point {
    x: i32,
    y: i32,
}
```

In order to generate a random `Point` instance, you need to implement
the trait `Arbitrary` for the struct `Point`:

```rust
use quickcheck::{Arbitrary, Gen};

impl Arbitrary for Point {
    fn arbitrary(g: &mut Gen) -> Point {
        Point {
            x: i32::arbitrary(g),
            y: i32::arbitrary(g),
        }
    }
}
```

## Case study: The Sieve of Eratosthenes

The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
is a simple and elegant way to find all primes less than or equal to `N`.
Briefly, the algorithm works by allocating an array with `N` slots containing
booleans. Slots marked with `false` correspond to prime numbers (or numbers
not known to be prime while building the sieve) and slots marked with `true`
are known to not be prime. For each `n`, all of its multiples in this array
are marked as true. When all `n` have been checked, the numbers marked `false`
are returned as the primes.

As you might imagine, there's a lot of potential for off-by-one errors, which
makes it ideal for randomized testing. So let's take a look at my
implementation and see if we can spot the bug:

```rust
fn sieve(n: usize) -> Vec<usize> {
    if n <= 1 {
        return vec![];
    }

    let mut marked = vec![false; n+1];
    marked[0] = true;
    marked[1] = true;
    marked[2] = true;
    for p in 2..n {
        for i in (2*p..n).filter(|&n| n % p == 0) {
            marked[i] = true;
        }
    }
    marked.iter()
          .enumerate()
          .filter_map(|(i, &m)| if m { None } else { Some(i) })
          .collect()
}
```

Let's try it on a few inputs by hand:

```text
sieve(3) => [2, 3]
sieve(5) => [2, 3, 5]
sieve(8) => [2, 3, 5, 7, 8] # !!!
```

Something has gone wrong! But where? The bug is rather subtle, but it's an
easy one to make. It's OK if you can't spot it, because we're going to use
QuickCheck to help us track it down.

Even before looking at some example outputs, it's good to try and come up with
some *properties* that are always satisfiable by the output of the function. An
obvious one for the prime number sieve is to check if all numbers returned are
prime. For that, we'll need an `is_prime` function:

```rust
fn is_prime(n: usize) -> bool {
    n != 0 && n != 1 && (2..).take_while(|i| i*i <= n).all(|i| n % i != 0)
}
```

All this is doing is c
... [TRUNCATED]
```

### File: examples\btree_set_range.rs
```rs
use std::collections::BTreeSet;
use std::ops::Bound::{self, *};

use quickcheck::{quickcheck, TestResult};

/// Covers every `std::ops::Range*` plus variants with exclusive start.
type RangeAny<T> = (Bound<T>, Bound<T>);

/// Mimic `RangeBounds::contains`, stabilized in Rust 1.35.
trait RangeBounds<T> {
    fn contains(&self, _: &T) -> bool;
}

impl<T: PartialOrd> RangeBounds<T> for RangeAny<T> {
    fn contains(&self, item: &T) -> bool {
        (match &self.0 {
            Included(start) => start <= item,
            Excluded(start) => start < item,
            Unbounded => true,
        }) && (match &self.1 {
            Included(end) => item <= end,
            Excluded(end) => item < end,
            Unbounded => true,
        })
    }
}

/// Checks conditions where `BTreeSet::range` panics:
/// - Panics if range start > end.
/// - Panics if range start == end and both bounds are Excluded.
fn panics<T: PartialOrd>(range: RangeAny<T>) -> bool {
    match (&range.0, &range.1) {
        (Excluded(start), Excluded(end)) => start >= end,
        (Included(start), Excluded(end) | Included(end))
        | (Excluded(start), Included(end)) => start > end,
        (Unbounded, _) | (_, Unbounded) => false,
    }
}

/// Checks that `BTreeSet::range` returns all items contained in the given
/// `range`.
fn check_range(set: BTreeSet<i32>, range: RangeAny<i32>) -> TestResult {
    if panics(range) {
        TestResult::discard()
    } else {
        let xs: BTreeSet<_> = set.range(range).copied().collect();
        TestResult::from_bool(
            set.iter().all(|x| range.contains(x) == xs.contains(x)),
        )
    }
}

fn main() {
    quickcheck(check_range as fn(_, _) -> TestResult);
}

```

### File: examples\out_of_bounds.rs
```rs
use quickcheck::{quickcheck, TestResult};

fn main() {
    fn prop(length: usize, index: usize) -> TestResult {
        let v: Vec<_> = (0..length).collect();
        if index < length {
            TestResult::discard()
        } else {
            TestResult::must_fail(move || v[index])
        }
    }
    quickcheck(prop as fn(usize, usize) -> TestResult);
}

```

### File: examples\reverse.rs
```rs
use quickcheck::quickcheck;

fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for x in xs {
        rev.insert(0, x.clone());
    }
    rev
}

fn main() {
    fn equality_after_applying_twice(xs: Vec<isize>) -> bool {
        xs == reverse(&reverse(&xs))
    }
    quickcheck(equality_after_applying_twice as fn(Vec<isize>) -> bool);
}

```

### File: examples\reverse_single.rs
```rs
use quickcheck::{quickcheck, TestResult};

fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
    let mut rev = vec![];
    for x in xs {
        rev.insert(0, x.clone());
    }
    rev
}

fn main() {
    fn prop(xs: Vec<isize>) -> TestResult {
        if xs.len() != 1 {
            return TestResult::discard();
        }
        TestResult::from_bool(xs == reverse(&xs))
    }
    quickcheck(prop as fn(Vec<isize>) -> TestResult);
}

```

### File: examples\sieve.rs
```rs
use quickcheck::quickcheck;

fn sieve(n: usize) -> Vec<usize> {
    if n <= 1 {
        return vec![];
    }

    let mut marked = vec![false; n + 1];
    marked[0] = true;
    marked[1] = true;
    marked[2] = true;
    for p in 2..n {
        for i in (2 * p..n).filter(|&n| n % p == 0) {
            marked[i] = true;
        }
    }
    marked
        .iter()
        .enumerate()
        .filter_map(|(i, &m)| if m { None } else { Some(i) })
        .collect()
}

fn is_prime(n: usize) -> bool {
    n != 0 && n != 1 && (2..).take_while(|i| i * i <= n).all(|i| n % i != 0)
}

fn main() {
    fn prop_all_prime(n: usize) -> bool {
        sieve(n).into_iter().all(is_prime)
    }

    fn prop_prime_iff_in_the_sieve(n: usize) -> bool {
        sieve(n) == (0..=n).filter(|&i| is_prime(i)).collect::<Vec<_>>()
    }

    quickcheck(prop_all_prime as fn(usize) -> bool);
    quickcheck(prop_prime_iff_in_the_sieve as fn(usize) -> bool);
}

```

### File: examples\sort.rs
```rs
// This is a buggy quick sort implementation, QuickCheck will find the bug for
// you.

use quickcheck::quickcheck;

fn smaller_than<T: Clone + Ord>(xs: &[T], pivot: &T) -> Vec<T> {
    xs.iter().filter(|&x| *x < *pivot).cloned().collect()
}

fn larger_than<T: Clone + Ord>(xs: &[T], pivot: &T) -> Vec<T> {
    xs.iter().filter(|&x| *x > *pivot).cloned().collect()
}

fn sortk<T: Clone + Ord>(x: &T, xs: &[T]) -> Vec<T> {
    let mut result: Vec<T> = sort(&smaller_than(xs, x));
    let last_part = sort(&larger_than(xs, x));
    result.push(x.clone());
    result.extend(last_part.iter().cloned());
    result
}

fn sort<T: Clone + Ord>(list: &[T]) -> Vec<T> {
    if list.is_empty() {
        vec![]
    } else {
        sortk(&list[0], &list[1..])
    }
}

fn main() {
    fn is_sorted(xs: Vec<isize>) -> bool {
        for win in sort(&xs).windows(2) {
            if win[0] > win[1] {
                return false;
            }
        }
        true
    }

    fn keeps_length(xs: Vec<isize>) -> bool {
        xs.len() == sort(&xs).len()
    }
    quickcheck(keeps_length as fn(Vec<isize>) -> bool);

    quickcheck(is_sorted as fn(Vec<isize>) -> bool);
}

```

### File: src\arbitrary.rs
```rs
use std::char;
use std::collections::{
    BTreeMap, BTreeSet, BinaryHeap, HashMap, HashSet, LinkedList, VecDeque,
};
use std::env;
use std::ffi::{CString, OsString};
use std::hash::{BuildHasher, Hash};
use std::iter::{empty, once, successors};
use std::net::{
    IpAddr, Ipv4Addr, Ipv6Addr, SocketAddr, SocketAddrV4, SocketAddrV6,
};
use std::num::Wrapping;
use std::num::{
    NonZeroU128, NonZeroU16, NonZeroU32, NonZeroU64, NonZeroU8, NonZeroUsize,
};
use std::ops::{
    Bound, Range, RangeFrom, RangeFull, RangeInclusive, RangeTo,
    RangeToInclusive,
};
use std::path::PathBuf;
use std::sync::Arc;
use std::time::{Duration, SystemTime, UNIX_EPOCH};

use rand::prelude::*;

/// `Gen` represents a PRNG.
///
/// It is the source of randomness from which QuickCheck will generate values.
/// An instance of `Gen` is passed to every invocation of
/// `Arbitrary::arbitrary`, which permits callers to use lower level RNG
/// routines to generate values.
///
/// It is unspecified whether this is a secure RNG or not. Therefore, callers
/// should assume it is insecure.
pub struct Gen {
    rng: rand::rngs::SmallRng,
    size: usize,
}

impl Gen {
    /// Returns a `Gen` with a random seed and the given size configuration.
    ///
    /// The `size` parameter controls the size of random values generated.
    /// For example, it specifies the maximum length of a randomly generated
    /// vector, but is and should not be used to control the range of a
    /// randomly generated number. (Unless that number is used to control the
    /// size of a data structure.)
    pub fn new(size: usize) -> Gen {
        Gen { rng: rand::make_rng(), size: size }
    }

    /// Returns a `Gen` with the given seed and a default size configuration.
    ///
    /// Two `Gen`s created with the same seed will generate the same values.
    /// Though the values may vary between QuickCheck releases.
    ///
    /// The `size` parameter controls the size of random values generated.
    /// For example, it specifies the maximum length of a randomly generated
    /// vector, but is and should not be used to control the range of a
    /// randomly generated number. (Unless that number is used to control the
    /// size of a data structure.)
    pub fn from_size_and_seed(size: usize, seed: u64) -> Gen {
        Gen { rng: rand::rngs::SmallRng::seed_from_u64(seed), size }
    }

    /// Returns the size configured with this generator.
    pub fn size(&self) -> usize {
        self.size
    }

    /// Choose among the possible alternatives in the slice given. If the slice
    /// is empty, then `None` is returned. Otherwise, a non-`None` value is
    /// guaranteed to be returned.
    pub fn choose<'a, T>(&mut self, slice: &'a [T]) -> Option<&'a T> {
        slice.choose(&mut self.rng)
    }

    fn random<T>(&mut self) -> T
    where
        rand::distr::StandardUniform: rand::distr::Distribution<T>,
    {
        self.rng.random()
    }

    fn random_range<T, R>(&mut self, range: R) -> T
    where
        T: rand::distr::uniform::SampleUniform,
        R: rand::distr::uniform::SampleRange<T>,
    {
        self.rng.random_range(range)
    }
}

/// Creates a shrinker with zero elements.
pub fn empty_shrinker<A: 'static>() -> Box<dyn Iterator<Item = A>> {
    Box::new(empty())
}

/// Creates a shrinker with a single element.
pub fn single_shrinker<A: 'static>(value: A) -> Box<dyn Iterator<Item = A>> {
    Box::new(once(value))
}

/// `Arbitrary` describes types whose values can be randomly generated and
/// shrunk.
///
/// Aside from shrinking, `Arbitrary` is different from typical RNGs in that it
/// respects `Gen::size()` for controlling how much memory a particular value
/// uses, for practical purposes. For example, `Vec::arbitrary()` respects
/// `Gen::size()` to decide the maximum `len()` of the vector. This behavior is
/// necessary due to practical speed and size limitations. Conversely,
/// `i32::arbitrary()` ignores `size()` since all `i32` values require `O(1)`
/// memory and operations between `i32`s require `O(1)` time (with the
/// exception of exponentiation).
///
/// Additionally, all types that implement `Arbitrary` must also implement
/// `Clone`.
pub trait Arbitrary: Clone + 'static {
    /// Return an arbitrary value.
    ///
    /// Implementations should respect `Gen::size()` when decisions about how
    /// big a particular value should be. Implementations should generally
    /// defer to other `Arbitrary` implementations to generate other random
    /// values when necessary. The `Gen` type also offers a few RNG helper
    /// routines.
    fn arbitrary(g: &mut Gen) -> Self;

    /// Return an iterator of values that are smaller than itself.
    ///
    /// The way in which a value is "smaller" is implementation defined. In
    /// some cases, the interpretation is obvious: shrinking an integer should
    /// produce integers smaller than itself. Others are more complex, for
    /// example, shrinking a `Vec` should both shrink its size and shrink its
    /// component values.
    ///
    /// The iterator returned should be bounded to some reasonable size.
    ///
    /// It is always correct to return an empty iterator, and indeed, this
    /// is the default implementation. The downside of this approach is that
    /// witnesses to failures in properties will be more inscrutable.
    fn shrink(&self) -> Box<dyn Iterator<Item = Self>> {
        empty_shrinker()
    }
}

impl Arbitrary for () {
    fn arbitrary(_: &mut Gen) {}
}

impl Arbitrary for bool {
    fn arbitrary(g: &mut Gen) -> bool {
        g.random()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = bool>> {
        if *self {
            single_shrinker(false)
        } else {
            empty_shrinker()
        }
    }
}

impl<A: Arbitrary> Arbitrary for Option<A> {
    fn arbitrary(g: &mut Gen) -> Option<A> {
        if g.random() {
            None
        } else {
            Some(Arbitrary::arbitrary(g))
        }
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = Option<A>>> {
        match *self {
            None => empty_shrinker(),
            Some(ref x) => {
                let chain = single_shrinker(None).chain(x.shrink().map(Some));
                Box::new(chain)
            }
        }
    }
}

impl<A: Arbitrary, B: Arbitrary> Arbitrary for Result<A, B> {
    fn arbitrary(g: &mut Gen) -> Result<A, B> {
        if g.random() {
            Ok(Arbitrary::arbitrary(g))
        } else {
            Err(Arbitrary::arbitrary(g))
        }
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = Result<A, B>>> {
        match *self {
            Ok(ref x) => {
                let xs = x.shrink();
                let tagged = xs.map(Ok);
                Box::new(tagged)
            }
            Err(ref x) => {
                let xs = x.shrink();
                let tagged = xs.map(Err);
                Box::new(tagged)
            }
        }
    }
}

macro_rules! impl_arb_for_single_tuple {
    ($(($type_param:ident, $tuple_index:tt),)*) => {
        impl<$($type_param),*> Arbitrary for ($($type_param,)*)
            where $($type_param: Arbitrary,)*
        {
            fn arbitrary(g: &mut Gen) -> ($($type_param,)*) {
                (
                    $(
                        $type_param::arbitrary(g),
                    )*
                )
            }

            fn shrink(&self) -> Box<dyn Iterator<Item=($($type_param,)*)>> {
                let iter = ::std::iter::empty();
                $(
                    let cloned = self.clone();
                    let iter = iter.chain(
                        self.$tuple_index.shrink().map(move |shr_value| {
                            let mut result = cloned.clone();
                            result.$tuple_index = shr_value;
                            result
                        })
                    );
                )*
                Box::new(iter)
            }
        }
    };
}

macro_rules! impl_arb_for_tuples {
    (@internal [$($acc:tt,)*]) => { };
    (@internal [$($acc:tt,)*] ($type_param:ident, $tuple_index:tt), $($rest:tt,)*) => {
        impl_arb_for_single_tuple!($($acc,)* ($type_param, $tuple_index),);
        impl_arb_for_tuples!(@internal [$($acc,)* ($type_param, $tuple_index),] $($rest,)*);
    };
    ($(($type_param:ident, $tuple_index:tt),)*) => {
        impl_arb_for_tuples!(@internal [] $(($type_param, $tuple_index),)*);
    };
}

impl_arb_for_tuples! {
    (A, 0),
    (B, 1),
    (C, 2),
    (D, 3),
    (E, 4),
    (F, 5),
    (G, 6),
    (H, 7),
}

impl<const N: usize, A: Arbitrary> Arbitrary for [A; N] {
    fn arbitrary(g: &mut Gen) -> Self {
        std::array::from_fn(|_ix| A::arbitrary(g))
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = [A; N]>> {
        let cloned = self.clone();
        let iter = (0..N).flat_map(move |n| {
            let cloned = cloned.clone();
            cloned[n].shrink().map(move |shr_value| {
                let mut result = cloned.clone();
                result[n] = shr_value;
                result
            })
        });

        Box::new(iter)
    }
}

impl<A: Arbitrary> Arbitrary for Vec<A> {
    fn arbitrary(g: &mut Gen) -> Vec<A> {
        let size = {
            let s = g.size();
            g.random_range(0..s)
        };
        (0..size).map(|_| A::arbitrary(g)).collect()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = Vec<A>>> {
        VecShrinker::new(self.clone())
    }
}

///Iterator which returns successive attempts to shrink the vector `seed`
struct VecShrinker<A> {
    seed: Vec<A>,
    /// How much which is removed when trying with smaller vectors
    size: usize,
    /// The end of the removed elements
    offset: usize,
    /// The shrinker for the element at `offset` once shrinking of individual
    /// elements are attempted
    element_shrinker: Box<dyn Iterator<Item = A>>,
}

impl<A: Arbitrary> VecShrinker<A> {
    #[allow(clippy::new_ret_no_self)]
    fn new(seed: Vec<A>) -> Box<dyn Iterator<Item = Vec<A>>> {
        let es = match seed.first() {
            Some(e) => e.shrink(),
            None => return empty_shrinker(),
        };
        let size = seed.len();
        Box::new(VecShrinker {
            seed,
            size,
            offset: size,
            element_shrinker: es,
        })
    }

    /// Returns the next shrunk element if any, `offset` points to the index
    /// after the returned element after the function returns
    fn next_element(&mut self) -> Option<A> {
        loop {
            match self.element_shrinker.next() {
                Some(e) => return Some(e),
                None => match self.seed.get(self.offset) {
                    Some(e) => {
                        self.element_shrinker = e.shrink();
                        self.offset += 1;
                    }
                    None => return None,
                },
            }
        }
    }
}

impl<A> Iterator for VecShrinker<A>
where
    A: Arbitrary,
{
    type Item = Vec<A>;
    fn next(&mut self) -> Option<Vec<A>> {
        // Try with an empty vector first
        if self.size == self.seed.len() {
            self.size /= 2;
            self.offset = self.size;
            return Some(vec![]);
        }
        if self.size != 0 {
            // Generate a smaller vector by removing the elements between
            // (offset - size) and offset
            let xs1 = self.seed[..(self.offset - self.size)]
                .iter()
                .chain(&self.seed[self.offset..])
                .cloned()
                .collect();
            self.offset += self.size;
            // Try to reduce the amount removed from the vector once all
            // previous sizes tried
            if self.offset > self.seed.len() {
                self.size /= 2;
                self.offset = self.size;
            }
            Some(xs1)
        } else {
            // A smaller vector did not work so try to shrink each element of
            // the vector instead Reuse `offset` as the index determining which
            // element to shrink

            // The first element shrinker is already created so skip the first
            // offset (self.offset == 0 only on first entry to this part of the
            // iterator)
            if self.offset == 0 {
                self.offset = 1;
            }

            match self.next_element() {
                Some(e) => Some(
                    self.seed[..self.offset - 1]
                        .iter()
                        .cloned()
                        .chain(Some(e))
                        .chain(self.seed[self.offset..].iter().cloned())
                        .collect(),
                ),
                None => None,
            }
        }
    }
}

impl<K: Arbitrary + Ord, V: Arbitrary> Arbitrary for BTreeMap<K, V> {
    fn arbitrary(g: &mut Gen) -> BTreeMap<K, V> {
        let vec: Vec<(K, V)> = Arbitrary::arbitrary(g);
        vec.into_iter().collect()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = BTreeMap<K, V>>> {
        let vec: Vec<(K, V)> = self.clone().into_iter().collect();
        Box::new(
            vec.shrink().map(|v| v.into_iter().collect::<BTreeMap<K, V>>()),
        )
    }
}

impl<
        K: Arbitrary + Eq + Hash,
        V: Arbitrary,
        S: BuildHasher + Default + Clone + 'static,
    > Arbitrary for HashMap<K, V, S>
{
    fn arbitrary(g: &mut Gen) -> Self {
        let vec: Vec<(K, V)> = Arbitrary::arbitrary(g);
        vec.into_iter().collect()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = Self>> {
        let vec: Vec<(K, V)> = self.clone().into_iter().collect();
        Box::new(vec.shrink().map(|v| v.into_iter().collect::<Self>()))
    }
}

impl<T: Arbitrary + Ord> Arbitrary for BTreeSet<T> {
    fn arbitrary(g: &mut Gen) -> BTreeSet<T> {
        let vec: Vec<T> = Arbitrary::arbitrary(g);
        vec.into_iter().collect()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = BTreeSet<T>>> {
        let vec: Vec<T> = self.clone().into_iter().collect();
        Box::new(vec.shrink().map(|v| v.into_iter().collect::<BTreeSet<T>>()))
    }
}

impl<T: Arbitrary + Ord> Arbitrary for BinaryHeap<T> {
    fn arbitrary(g: &mut Gen) -> BinaryHeap<T> {
        let vec: Vec<T> = Arbitrary::arbitrary(g);
        vec.into_iter().collect()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = BinaryHeap<T>>> {
        let vec: Vec<T> = self.clone().into_iter().collect();
        Box::new(
            vec.shrink().map(|v| v.into_iter().collect::<BinaryHeap<T>>()),
        )
    }
}

impl<T: Arbitrary + Eq + Hash, S: BuildHasher + Default + Clone + 'static>
    Arbitrary for HashSet<T, S>
{
    fn arbitrary(g: &mut Gen) -> Self {
        let vec: Vec<T> = Arbitrary::arbitrary(g);
        vec.into_iter().collect()
    }

    fn shrink(&self) -> Box<dyn Iterator<Item = Self>> {
        let vec: Vec<T> = self.clone().into_iter().collect();
        Box::new(vec.shrink().map(|v| v.i
... [TRUNCATED]
```

### File: src\lib.rs
```rs
/*!
This crate is a port of
[Haskell's QuickCheck](https://hackage.haskell.org/package/QuickCheck).

QuickCheck is a library for random testing of program properties. The
programmer provides a specification of the program, in the form of properties
which functions should satisfy, and QuickCheck then tests that the properties
hold in a large number of randomly generated cases.

For detailed examples, please see the
[README](https://github.com/BurntSushi/quickcheck).

# Compatibility

In general, this crate considers the `Arbitrary` implementations provided as
implementation details. Strategies may or may not change over time, which may
cause new test failures, presumably due to the discovery of new bugs due to a
new kind of witness being generated. These sorts of changes may happen in
semver compatible releases.
*/

pub use crate::arbitrary::{
    empty_shrinker, single_shrinker, Arbitrary, Gen, NoShrink,
};
pub use crate::tester::{quickcheck, QuickCheck, TestResult, Testable};

/// A macro for writing quickcheck tests.
///
/// This macro takes as input one or more property functions to test, and
/// produces a proper `#[test]` function for each property. If the property
/// fails, the behavior is as if `quickcheck` were called on the property
/// (i.e., it panics and fails the test).
///
/// Note that this macro doesn't support `mut` or patterns in parameters.
///
/// # Example
///
/// ```rust
/// # #[macro_use] extern crate quickcheck; fn main() {
/// quickcheck! {
///     fn prop_reverse_reverse(xs: Vec<usize>) -> bool {
///         let rev: Vec<_> = xs.clone().into_iter().rev().collect();
///         let revrev: Vec<_> = rev.into_iter().rev().collect();
///         xs == revrev
///     }
/// };
/// # }
/// ```
#[macro_export]
macro_rules! quickcheck {
    (@as_items $($i:item)*) => ($($i)*);
    {
        $(
            $(#[$m:meta])*
            fn $fn_name:ident($($arg_name:ident : $arg_ty:ty),*) -> $ret:ty {
                $($code:tt)*
            }
        )*
    } => (
        $crate::quickcheck! {
            @as_items
            $(
                #[test]
                $(#[$m])*
                fn $fn_name() {
                    fn prop($($arg_name: $arg_ty),*) -> $ret {
                        $($code)*
                    }
                    $crate::quickcheck(prop as fn($($arg_ty),*) -> $ret);
                }
            )*
        }
    )
}

#[cfg(feature = "use_logging")]
fn env_logger_init() -> Result<(), log::SetLoggerError> {
    env_logger::try_init()
}
#[cfg(feature = "use_logging")]
macro_rules! info {
    ($($tt:tt)*) => {
        log::info!($($tt)*)
    };
}

#[cfg(not(feature = "use_logging"))]
fn env_logger_init() {}
#[cfg(not(feature = "use_logging"))]
macro_rules! info {
    ($($_ignore:tt)*) => {
        ()
    };
}

mod arbitrary;
mod tester;

#[cfg(test)]
mod tests;

```

### File: src\tester.rs
```rs
use std::cmp;
use std::env;
use std::fmt::Debug;
use std::panic;

use crate::{
    tester::Status::{Discard, Fail, Pass},
    Arbitrary, Gen,
};

/// The main `QuickCheck` type for setting configuration and running
/// `QuickCheck`.
pub struct QuickCheck {
    tests: u64,
    max_tests: u64,
    min_tests_passed: u64,
    rng: Gen,
}

fn qc_tests() -> u64 {
    let default = 100;
    match env::var("QUICKCHECK_TESTS") {
        Ok(val) => val.parse().unwrap_or(default),
        Err(_) => default,
    }
}

fn qc_max_tests() -> u64 {
    let default = 10_000;
    match env::var("QUICKCHECK_MAX_TESTS") {
        Ok(val) => val.parse().unwrap_or(default),
        Err(_) => default,
    }
}

fn qc_gen_size() -> usize {
    let default = 100;
    match env::var("QUICKCHECK_GENERATOR_SIZE") {
        Ok(val) => val.parse().unwrap_or(default),
        Err(_) => default,
    }
}

fn qc_min_tests_passed() -> u64 {
    let default = 0;
    match env::var("QUICKCHECK_MIN_TESTS_PASSED") {
        Ok(val) => val.parse().unwrap_or(default),
        Err(_) => default,
    }
}

impl Default for QuickCheck {
    fn default() -> Self {
        Self::new()
    }
}

impl QuickCheck {
    /// Creates a new `QuickCheck` value.
    ///
    /// This can be used to run `QuickCheck` on things that implement
    /// `Testable`. You may also adjust the configuration, such as the
    /// number of tests to run.
    ///
    /// By default, the maximum number of passed tests is set to `100`, the max
    /// number of overall tests is set to `10000` and the generator is created
    /// with a size of `100`.
    pub fn new() -> QuickCheck {
        let rng = Gen::new(qc_gen_size());
        let tests = qc_tests();
        let max_tests = cmp::max(tests, qc_max_tests());
        let min_tests_passed = qc_min_tests_passed();

        QuickCheck { tests, max_tests, min_tests_passed, rng }
    }

    /// Set the random number generator to be used by `QuickCheck`.
    pub fn rng(self, rng: Gen) -> QuickCheck {
        QuickCheck { rng, ..self }
    }

    /// Set the random number generator to be used by `QuickCheck`.
    ///
    /// This is **DEPRECATED**. Using this method on Rust 2024 or newer
    /// requires the raw identifier syntax because `gen` is now a keyword.
    /// Instead, prefer the [`QuickCheck::rng`] method.
    #[deprecated(since = "1.1.0", note = "use `rng` instead")]
    pub fn r#gen(self, rng: Gen) -> QuickCheck {
        self.rng(rng)
    }

    /// Set the number of tests to run.
    ///
    /// This actually refers to the maximum number of *passed* tests that
    /// can occur. Namely, if a test causes a failure, future testing on that
    /// property stops. Additionally, if tests are discarded, there may be
    /// fewer than `tests` passed.
    pub fn tests(mut self, tests: u64) -> QuickCheck {
        self.tests = tests;
        self
    }

    /// Set the maximum number of tests to run.
    ///
    /// The number of invocations of a property will never exceed this number.
    /// This is necessary to cap the number of tests because `QuickCheck`
    /// properties can discard tests.
    pub fn max_tests(mut self, max_tests: u64) -> QuickCheck {
        self.max_tests = max_tests;
        self
    }

    /// Set the minimum number of tests that needs to pass.
    ///
    /// This actually refers to the minimum number of *valid* *passed* tests
    /// that needs to pass for the property to be considered successful.
    pub fn min_tests_passed(mut self, min_tests_passed: u64) -> QuickCheck {
        self.min_tests_passed = min_tests_passed;
        self
    }

    /// Tests a property and returns the result.
    ///
    /// The result returned is either the number of tests passed or a witness
    /// of failure.
    ///
    /// (If you're using Rust's unit testing infrastructure, then you'll
    /// want to use the `quickcheck` method, which will `panic!` on failure.)
    pub fn quicktest<A>(&mut self, f: A) -> Result<u64, TestResult>
    where
        A: Testable,
    {
        let mut n_tests_passed = 0;
        for _ in 0..self.max_tests {
            if n_tests_passed >= self.tests {
                break;
            }
            match f.result(&mut self.rng) {
                TestResult { status: Pass, .. } => n_tests_passed += 1,
                TestResult { status: Discard, .. } => continue,
                r @ TestResult { status: Fail, .. } => return Err(r),
            }
        }
        Ok(n_tests_passed)
    }

    /// Tests a property and calls `panic!` on failure.
    ///
    /// The `panic!` message will include a (hopefully) minimal witness of
    /// failure.
    ///
    /// It is appropriate to use this method with Rust's unit testing
    /// infrastructure.
    ///
    /// Note that if the environment variable `RUST_LOG` is set to enable
    /// `info` level log messages for the `quickcheck` crate, then this will
    /// include output on how many `QuickCheck` tests were passed.
    ///
    /// # Example
    ///
    /// ```rust
    /// use quickcheck::QuickCheck;
    ///
    /// fn prop_reverse_reverse() {
    ///     fn revrev(xs: Vec<usize>) -> bool {
    ///         let rev: Vec<_> = xs.clone().into_iter().rev().collect();
    ///         let revrev: Vec<_> = rev.into_iter().rev().collect();
    ///         xs == revrev
    ///     }
    ///     QuickCheck::new().quickcheck(revrev as fn(Vec<usize>) -> bool);
    /// }
    /// ```
    pub fn quickcheck<A>(&mut self, f: A)
    where
        A: Testable,
    {
        // Ignore log init failures, implying it has already been done.
        let _ = crate::env_logger_init();

        let n_tests_passed = match self.quicktest(f) {
            Ok(n_tests_passed) => n_tests_passed,
            Err(result) => panic!("{}", result.failed_msg()),
        };

        if n_tests_passed >= self.min_tests_passed {
            info!("(Passed {} QuickCheck tests.)", n_tests_passed);
        } else {
            panic!(
                "(Unable to generate enough tests, {} not discarded.)",
                n_tests_passed
            );
        }
    }
}

/// Convenience function for running `QuickCheck`.
///
/// This is an alias for `QuickCheck::new().quickcheck(f)`.
pub fn quickcheck<A: Testable>(f: A) {
    QuickCheck::new().quickcheck(f)
}

/// Describes the status of a single instance of a test.
///
/// All testable things must be capable of producing a `TestResult`.
#[derive(Clone, Debug)]
pub struct TestResult {
    status: Status,
    arguments: Option<Vec<String>>,
    err: Option<String>,
}

/// Whether a test has passed, failed or been discarded.
#[derive(Clone, Debug)]
enum Status {
    Pass,
    Fail,
    Discard,
}

impl TestResult {
    /// Produces a test result that indicates the current test has passed.
    pub fn passed() -> TestResult {
        TestResult::from_bool(true)
    }

    /// Produces a test result that indicates the current test has failed.
    pub fn failed() -> TestResult {
        TestResult::from_bool(false)
    }

    /// Produces a test result that indicates failure from a runtime error.
    pub fn error<S: Into<String>>(msg: S) -> TestResult {
        let mut r = TestResult::from_bool(false);
        r.err = Some(msg.into());
        r
    }

    /// Produces a test result that instructs `quickcheck` to ignore it.
    /// This is useful for restricting the domain of your properties.
    /// When a test is discarded, `quickcheck` will replace it with a
    /// fresh one (up to a certain limit).
    pub fn discard() -> TestResult {
        TestResult { status: Discard, arguments: None, err: None }
    }

    /// Converts a `bool` to a `TestResult`. A `true` value indicates that
    /// the test has passed and a `false` value indicates that the test
    /// has failed.
    pub fn from_bool(b: bool) -> TestResult {
        TestResult {
            status: if b { Pass } else { Fail },
            arguments: None,
            err: None,
        }
    }

    /// Tests if a "procedure" fails when executed. The test passes only if
    /// `f` generates a task failure during its execution.
    pub fn must_fail<T, F>(f: F) -> TestResult
    where
        F: FnOnce() -> T,
        F: 'static,
        T: 'static,
    {
        let f = panic::AssertUnwindSafe(f);
        TestResult::from_bool(panic::catch_unwind(f).is_err())
    }

    /// Returns `true` if and only if this test result describes a failing
    /// test.
    pub fn is_failure(&self) -> bool {
        match self.status {
            Fail => true,
            Pass | Discard => false,
        }
    }

    /// Returns `true` if and only if this test result describes a failing
    /// test as a result of a run time error.
    pub fn is_error(&self) -> bool {
        self.is_failure() && self.err.is_some()
    }

    fn failed_msg(&self) -> String {
        let arguments_msg = match self.arguments {
            None => "No Arguments Provided".to_owned(),
            Some(ref args) => format!("Arguments: ({})", args.join(", ")),
        };
        match self.err {
            None => format!("[quickcheck] TEST FAILED. {arguments_msg}"),
            Some(ref err) => format!(
                "[quickcheck] TEST FAILED (runtime error). {arguments_msg}\nError: {err}"
            ),
        }
    }
}

/// A shorter way of producing a `TestResult` from a `bool`.
///
/// # Example
///
/// ```rust
/// use quickcheck::TestResult;
///
/// let result: TestResult = (2 > 1).into();
/// assert!(!result.is_failure());
/// ```
impl From<bool> for TestResult {
    fn from(b: bool) -> TestResult {
        TestResult::from_bool(b)
    }
}

/// `Testable` describes types (e.g., a function) whose values can be
/// tested.
///
/// Anything that can be tested must be capable of producing a `TestResult`
/// given a random number generator. This is trivial for types like `bool`,
/// which are just converted to either a passing or failing test result.
///
/// For functions, an implementation must generate random arguments
/// and potentially shrink those arguments if they produce a failure.
///
/// It's unlikely that you'll have to implement this trait yourself.
pub trait Testable: 'static {
    fn result(&self, _: &mut Gen) -> TestResult;
}

impl Testable for bool {
    fn result(&self, _: &mut Gen) -> TestResult {
        TestResult::from_bool(*self)
    }
}

impl Testable for () {
    fn result(&self, _: &mut Gen) -> TestResult {
        TestResult::passed()
    }
}

impl Testable for TestResult {
    fn result(&self, _: &mut Gen) -> TestResult {
        self.clone()
    }
}

impl<A, E> Testable for Result<A, E>
where
    A: Testable,
    E: Debug + 'static,
{
    fn result(&self, g: &mut Gen) -> TestResult {
        match *self {
            Ok(ref r) => r.result(g),
            Err(ref err) => TestResult::error(format!("{err:?}")),
        }
    }
}

/// Return a vector of the debug formatting of each item in `args`
fn debug_reprs(args: &[&dyn Debug]) -> Vec<String> {
    args.iter().map(|x| format!("{x:?}")).collect()
}

macro_rules! testable_fn {
    ($($name: ident),*) => {

impl<T: Testable,
     $($name: Arbitrary + Debug),*> Testable for fn($($name),*) -> T {
    #[allow(non_snake_case)]
    fn result(&self, g: &mut Gen) -> TestResult {
        let self_ = *self;
        let a: ($($name,)*) = Arbitrary::arbitrary(g);
        let ( $($name,)* ) = a.clone();
        let mut r = safe(move || {self_($($name),*)}).result(g);

        if r.is_failure() {
            let mut a = a.shrink();
            while let Some(t) = a.next() {
                let ($($name,)*) = t.clone();
                let mut r_new = safe(move || {self_($($name),*)}).result(g);
                if r_new.is_failure() {
                    {
                        let ($(ref $name,)*) : ($($name,)*) = t;
                        r_new.arguments = Some(debug_reprs(&[$($name),*]));
                    }

                    // The shrunk value *does* witness a failure, so remember
                    // it for now
                    r = r_new;

                    // ... and switch over to that value, i.e. try to shrink
                    // it further.
                    a = t.shrink()
                }
            }
        }

        r
    }
}}}

testable_fn!();
testable_fn!(A);
testable_fn!(A, B);
testable_fn!(A, B, C);
testable_fn!(A, B, C, D);
testable_fn!(A, B, C, D, E);
testable_fn!(A, B, C, D, E, F);
testable_fn!(A, B, C, D, E, F, G);
testable_fn!(A, B, C, D, E, F, G, H);

fn safe<T, F>(fun: F) -> Result<T, String>
where
    F: FnOnce() -> T,
    F: 'static,
    T: 'static,
{
    panic::catch_unwind(panic::AssertUnwindSafe(fun)).map_err(|any_err| {
        // Extract common types of panic payload:
        // panic and assert produce &str or String
        if let Some(&s) = any_err.downcast_ref::<&str>() {
            s.to_owned()
        } else if let Some(s) = any_err.downcast_ref::<String>() {
            s.to_owned()
        } else {
            "UNABLE TO SHOW RESULT OF PANIC.".to_owned()
        }
    })
}

#[cfg(test)]
mod test {
    use crate::{Gen, QuickCheck};

    #[test]
    fn shrinking_regression_issue_126() {
        fn thetest(vals: Vec<bool>) -> bool {
            vals.iter().filter(|&v| *v).count() < 2
        }
        let failing_case = QuickCheck::new()
            .quicktest(thetest as fn(vals: Vec<bool>) -> bool)
            .unwrap_err();
        let expected_argument = format!("{:?}", [true, true]);
        assert_eq!(failing_case.arguments, Some(vec![expected_argument]));
    }

    #[test]
    fn size_for_small_types_issue_143() {
        fn t(_: i8) -> bool {
            true
        }
        QuickCheck::new().rng(Gen::new(129)).quickcheck(t as fn(i8) -> bool);
    }

    #[test]
    fn regression_signed_shrinker_panic() {
        fn foo_can_shrink(v: i8) -> bool {
            let _ = crate::Arbitrary::shrink(&v).take(100).count();
            true
        }
        crate::quickcheck(foo_can_shrink as fn(i8) -> bool);
    }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
