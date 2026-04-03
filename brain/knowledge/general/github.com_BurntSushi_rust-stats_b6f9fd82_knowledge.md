---
id: github.com-burntsushi-rust-stats-b6f9fd82-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:36.184854
---

# KNOWLEDGE EXTRACT: github.com_BurntSushi_rust-stats_b6f9fd82
> **Extracted on:** 2026-04-01 16:41:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525235/github.com_BurntSushi_rust-stats_b6f9fd82

---

## File: `.gitignore`
```
.*.swp
doc
tags
examples/data/ss10pusa.csv
build
target
Cargo.lock
scratch*
```

## File: `.travis.yml`
```yaml
language: rust
```

## File: `COPYING`
```
This project is dual-licensed under the Unlicense and MIT licenses.

You may use this code under the terms of either license.
```

## File: `Cargo.toml`
```
[package]
name = "streaming-stats"
version = "0.2.3"  #:version
authors = ["Andrew Gallant <jamslam@gmail.com>"]
description = "Experimental crate for computing basic statistics on streams."
documentation = "https://docs.rs/streaming-stats"
homepage = "https://github.com/BurntSushi/rust-stats"
repository = "https://github.com/BurntSushi/rust-stats"
readme = "README.md"
keywords = ["statistics", "stats", "median", "mean", "stddev"]
license = "Unlicense/MIT"

[lib]
name = "stats"

[dependencies]
num-traits = "0.2"
```

## File: `LICENSE-MIT`
```
The MIT License (MIT)

Copyright (c) 2015 Andrew Gallant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `Makefile`
```
ctags:
	ctags --recurse --options=ctags.rust --languages=Rust

docs:
	cargo doc
	# WTF is rustdoc doing?
	in-dir ./target/doc fix-perms
	rscp ./target/doc/* gopher:~/www/burntsushi.net/rustdoc/

push:
	git push origin master
	git push github master

```

## File: `README.md`
```markdown
An experimental library that provides some common statistical functions with
some support for computing them efficiently on *streams* of data. The intent
is to permit parallel computation of statistics on large data sets.

[![Build status](https://api.travis-ci.org/BurntSushi/rust-stats.png)](https://travis-ci.org/BurntSushi/rust-stats)
[![](http://meritbadge.herokuapp.com/streaming-stats)](https://crates.io/crates/streaming-stats)

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

Some documentation exists here:
[https://docs.rs/streaming-stats](https://docs.rs/streaming-stats).


### Installation

Simply add `streaming-stats` as a dependency to your project's `Cargo.toml`:

```toml
[dependencies]
streaming-stats = "0.2"
```
```

## File: `UNLICENSE`
```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```

## File: `ctags.rust`
```
--langdef=Rust
--langmap=Rust:.rs
--regex-Rust=/^[ \t]*(#\[[^\]]\][ \t]*)*(pub[ \t]+)?(extern[ \t]+)?("[^"]+"[ \t]+)?(unsafe[ \t]+)?fn[ \t]+([a-zA-Z0-9_]+)/\6/f,functions,function definitions/
--regex-Rust=/^[ \t]*(pub[ \t]+)?type[ \t]+([a-zA-Z0-9_]+)/\2/T,types,type definitions/
--regex-Rust=/^[ \t]*(pub[ \t]+)?enum[ \t]+([a-zA-Z0-9_]+)/\2/g,enum,enumeration names/
--regex-Rust=/^[ \t]*(pub[ \t]+)?struct[ \t]+([a-zA-Z0-9_]+)/\2/s,structure names/
--regex-Rust=/^[ \t]*(pub[ \t]+)?mod[ \t]+([a-zA-Z0-9_]+)/\2/m,modules,module names/
--regex-Rust=/^[ \t]*(pub[ \t]+)?static[ \t]+([a-zA-Z0-9_]+)/\2/c,consts,static constants/
--regex-Rust=/^[ \t]*(pub[ \t]+)?trait[ \t]+([a-zA-Z0-9_]+)/\2/t,traits,traits/
--regex-Rust=/^[ \t]*(pub[ \t]+)?impl([ \t\n]+<.*>)?[ \t]+([a-zA-Z0-9_]+)/\3/i,impls,trait implementations/
--regex-Rust=/^[ \t]*macro_rules![ \t]+([a-zA-Z0-9_]+)/\1/d,macros,macro definitions/
```

## File: `session.vim`
```
au BufWritePost *.rs silent!make ctags > /dev/null 2>&1
```

## File: `src/frequency.rs`
```rust
use std::collections::hash_map::{HashMap, Entry};
use std::fmt;
use std::hash::Hash;
use std::iter::{FromIterator, IntoIterator};
use std::default::Default;

use Commute;

/// A commutative data structure for exact frequency counts.
#[derive(Clone)]
pub struct Frequencies<T> {
    data: HashMap<T, u64>,
}

impl<T: fmt::Debug + Eq + Hash> fmt::Debug for Frequencies<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.data)
    }
}

impl<T: Eq + Hash> Frequencies<T> {
    /// Create a new frequency table with no samples.
    pub fn new() -> Frequencies<T> {
        Default::default()
    }

    /// Add a sample to the frequency table.
    pub fn add(&mut self, v: T) {
        match self.data.entry(v) {
            Entry::Vacant(count) => { count.insert(1); },
            Entry::Occupied(mut count) => { *count.get_mut() += 1; },
        }
    }

    /// Return the number of occurrences of `v` in the data.
    pub fn count(&self, v: &T) -> u64 {
        self.data.get(v).map(|&v| v).unwrap_or(0)
    }

    /// Return the cardinality (number of unique elements) in the data.
    pub fn cardinality(&self) -> u64 {
        self.len() as u64
    }

    /// Returns the mode if one exists.
    pub fn mode(&self) -> Option<&T> {
        let counts = self.most_frequent();
        if counts.is_empty() {
            None
        } else if counts.len() >= 2 && counts[0].1 == counts[1].1 {
            None
        } else {
            Some(counts[0].0)
        }
    }

    /// Return a `Vec` of elements and their corresponding counts in
    /// descending order.
    pub fn most_frequent(&self) -> Vec<(&T, u64)> {
        let mut counts: Vec<_> = self.data.iter()
                                          .map(|(k, &v)| (k, v))
                                          .collect();
        counts.sort_by(|&(_, c1), &(_, c2)| c2.cmp(&c1));
        counts
    }

    /// Return a `Vec` of elements and their corresponding counts in
    /// ascending order.
    pub fn least_frequent(&self) -> Vec<(&T, u64)> {
        let mut counts: Vec<_> = self.data.iter()
                                          .map(|(k, &v)| (k, v))
                                          .collect();
        counts.sort_by(|&(_, c1), &(_, c2)| c1.cmp(&c2));
        counts
    }

    /// Returns the cardinality of the data.
    pub fn len(&self) -> usize {
        self.data.len()
    }
}

impl<T: Eq + Hash> Commute for Frequencies<T> {
    fn merge(&mut self, v: Frequencies<T>) {
        for (k, v2) in v.data.into_iter() {
            match self.data.entry(k) {
                Entry::Vacant(v1) => { v1.insert(v2); }
                Entry::Occupied(mut v1) => { *v1.get_mut() += v2; }
            }
        }
    }
}

impl<T: Eq + Hash> Default for Frequencies<T> {
    fn default() -> Frequencies<T> {
        Frequencies { data: HashMap::with_capacity(100000) }
    }
}

impl<T: Eq + Hash> FromIterator<T> for Frequencies<T> {
    fn from_iter<I: IntoIterator<Item=T>>(it: I) -> Frequencies<T> {
        let mut v = Frequencies::new();
        v.extend(it);
        v
    }
}

impl<T: Eq + Hash> Extend<T> for Frequencies<T> {
    fn extend<I: IntoIterator<Item=T>>(&mut self, it: I) {
        for sample in it {
            self.add(sample);
        }
    }
}

#[cfg(test)]
mod test {
    use super::Frequencies;

    #[test]
    fn ranked() {
        let mut counts = Frequencies::new();
        counts.extend(vec![1usize, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4].into_iter());
        assert_eq!(counts.most_frequent()[0], (&2, 5));
        assert_eq!(counts.least_frequent()[0], (&3, 1));
    }
}
```

## File: `src/lib.rs`
```rust
extern crate num_traits;

use std::cmp::Ordering;
use std::hash;
use num_traits::ToPrimitive;

pub use frequency::Frequencies;
pub use minmax::MinMax;
pub use online::{OnlineStats, stddev, variance, mean};
pub use unsorted::{Unsorted, median, mode, modes};

/// Partial wraps a type that satisfies `PartialOrd` and implements `Ord`.
///
/// This allows types like `f64` to be used in data structures that require
/// `Ord`. When an ordering is not defined, an arbitrary order is returned.
#[derive(Clone, PartialEq, PartialOrd)]
struct Partial<T>(pub T);

impl<T: PartialEq> Eq for Partial<T> {}

impl<T: PartialOrd> Ord for Partial<T> {
    fn cmp(&self, other: &Partial<T>) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Less)
    }
}

impl<T: ToPrimitive> ToPrimitive for Partial<T> {
    fn to_isize(&self) -> Option<isize> { self.0.to_isize() }
    fn to_i8(&self) -> Option<i8> { self.0.to_i8() }
    fn to_i16(&self) -> Option<i16> { self.0.to_i16() }
    fn to_i32(&self) -> Option<i32> { self.0.to_i32() }
    fn to_i64(&self) -> Option<i64> { self.0.to_i64() }

    fn to_usize(&self) -> Option<usize> { self.0.to_usize() }
    fn to_u8(&self) -> Option<u8> { self.0.to_u8() }
    fn to_u16(&self) -> Option<u16> { self.0.to_u16() }
    fn to_u32(&self) -> Option<u32> { self.0.to_u32() }
    fn to_u64(&self) -> Option<u64> { self.0.to_u64() }

    fn to_f32(&self) -> Option<f32> { self.0.to_f32() }
    fn to_f64(&self) -> Option<f64> { self.0.to_f64() }
}

impl<T: hash::Hash> hash::Hash for Partial<T> {
    fn hash<H: hash::Hasher>(&self, state: &mut H) { self.0.hash(state); }
}

/// Defines an interface for types that have an identity and can be commuted.
///
/// The value returned by `Default::default` must be its identity with respect
/// to the `merge` operation.
pub trait Commute : Sized {
    /// Merges the value `other` into `self`.
    fn merge(&mut self, other: Self);

    /// Merges the values in the iterator into `self`.
    fn consume<I: Iterator<Item=Self>>(&mut self, other: I) {
        for v in other {
            self.merge(v);
        }
    }
}

/// Merges all items in the stream.
///
/// If the stream is empty, `None` is returned.
pub fn merge_all<T: Commute, I: Iterator<Item=T>>(mut it: I) -> Option<T> {
    match it.next() {
        None => None,
        Some(mut init) => { init.consume(it); Some(init) }
    }
}

impl<T: Commute> Commute for Option<T> {
    fn merge(&mut self, other: Option<T>) {
        match *self {
            None => { *self = other; }
            Some(ref mut v1) => { other.map(|v2| v1.merge(v2)); }
        }
    }
}

impl<T: Commute, E> Commute for Result<T, E> {
    fn merge(&mut self, other: Result<T, E>) {
        // Can't figure out how to work around the borrow checker to make
        // this code less awkward.
        if !self.is_err() && other.is_err() {
            *self = other;
            return;
        }
        match *self {
            Err(_) => {},
            Ok(ref mut v1) => {
                match other {
                    Ok(v2) => { v1.merge(v2); }
                    // This is the awkward part. We can't assign to `*self`
                    // because of the `ref mut v1` borrow. So we catch this
                    // case above and declare that this cannot be reached.
                    Err(_) => { unreachable!(); }
                }
            }
        }
    }
}

impl<T: Commute> Commute for Vec<T> {
    fn merge(&mut self, other: Vec<T>) {
        assert_eq!(self.len(), other.len());
        for (v1, v2) in self.iter_mut().zip(other.into_iter()) {
            v1.merge(v2);
        }
    }
}

mod frequency;
mod minmax;
mod online;
mod unsorted;

#[cfg(test)]
mod test {
    use Commute;
    use unsorted::Unsorted;

    #[test]
    fn options() {
        let v1: Unsorted<usize> = vec![2, 1, 3, 2].into_iter().collect();
        let v2: Unsorted<usize> = vec![5, 6, 5, 5].into_iter().collect();
        let mut merged = Some(v1);
        merged.merge(Some(v2));
        assert_eq!(merged.unwrap().mode(), Some(5));
    }
}
```

## File: `src/minmax.rs`
```rust
use std::default::Default;
use std::fmt;
use std::iter::{FromIterator, IntoIterator};

use Commute;

/// A commutative data structure for tracking minimum and maximum values.
///
/// This also stores the number of samples.
#[derive(Clone)]
pub struct MinMax<T> {
    len: u64,
    min: Option<T>,
    max: Option<T>,
}

impl<T: PartialOrd + Clone> MinMax<T> {
    /// Create an empty state where min and max values do not exist.
    pub fn new() -> MinMax<T> {
        Default::default()
    }

    /// Add a sample to the data.
    pub fn add(&mut self, sample: T) {
        self.len += 1;
        if self.min.as_ref().map(|v| &sample < v).unwrap_or(true) {
            self.min = Some(sample.clone());
        }
        if self.max.as_ref().map(|v| &sample > v).unwrap_or(true) {
            self.max = Some(sample);
        }
    }

    /// Returns the minimum of the data set.
    ///
    /// `None` is returned if and only if the number of samples is `0`.
    pub fn min(&self) -> Option<&T> {
        self.min.as_ref()
    }

    /// Returns the maximum of the data set.
    ///
    /// `None` is returned if and only if the number of samples is `0`.
    pub fn max(&self) -> Option<&T> {
        self.max.as_ref()
    }

    /// Returns the number of data point.
    pub fn len(&self) -> usize {
        self.len as usize
    }
}

impl<T: PartialOrd> Commute for MinMax<T> {
    fn merge(&mut self, v: MinMax<T>) {
        self.len += v.len;
        if self.min.is_none() || (!v.min.is_none() && v.min < self.min) {
            self.min = v.min;
        }
        if self.max.is_none() || (!v.max.is_none() && v.max > self.max) {
            self.max = v.max;
        }
    }
}

impl<T: PartialOrd> Default for MinMax<T> {
    fn default() -> MinMax<T> {
        MinMax {
            len: 0,
            min: None,
            max: None,
        }
    }
}

impl<T: fmt::Debug> fmt::Debug for MinMax<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match (&self.min, &self.max) {
            (&Some(ref min), &Some(ref max)) => {
                write!(f, "[{:?}, {:?}]", min, max)
            }
            (&None, &None) => write!(f, "N/A"),
            _ => unreachable!(),
        }
    }
}

impl<T: PartialOrd + Clone> FromIterator<T> for MinMax<T> {
    fn from_iter<I: IntoIterator<Item=T>>(it: I) -> MinMax<T> {
        let mut v = MinMax::new();
        v.extend(it);
        v
    }
}

impl<T: PartialOrd + Clone> Extend<T> for MinMax<T> {
    fn extend<I: IntoIterator<Item=T>>(&mut self, it: I) {
        for sample in it {
            self.add(sample);
        }
    }
}

#[cfg(test)]
mod test {
    use super::MinMax;
    use Commute;

    #[test]
    fn minmax() {
        let minmax: MinMax<u32> =
            vec![1u32, 4, 2, 3, 10].into_iter().collect();
        assert_eq!(minmax.min(), Some(&1u32));
        assert_eq!(minmax.max(), Some(&10u32));
    }

    #[test]
    fn minmax_merge_empty() {
        let mut mx1: MinMax<u32> = vec![1, 4, 2, 3, 10].into_iter().collect();
        assert_eq!(mx1.min(), Some(&1u32));
        assert_eq!(mx1.max(), Some(&10u32));

        mx1.merge(MinMax::default());
        assert_eq!(mx1.min(), Some(&1u32));
        assert_eq!(mx1.max(), Some(&10u32));
    }
}
```

## File: `src/online.rs`
```rust
use std::default::Default;
use std::fmt;
use std::iter::{FromIterator, IntoIterator};

use num_traits::ToPrimitive;

use Commute;

/// Compute the standard deviation of a stream in constant space.
pub fn stddev<I>(it: I) -> f64
        where I: Iterator, <I as Iterator>::Item: ToPrimitive {
    it.collect::<OnlineStats>().stddev()
}

/// Compute the variance of a stream in constant space.
pub fn variance<I>(it: I) -> f64
        where I: Iterator, <I as Iterator>::Item: ToPrimitive {
    it.collect::<OnlineStats>().variance()
}

/// Compute the mean of a stream in constant space.
pub fn mean<I>(it: I) -> f64
        where I: Iterator, <I as Iterator>::Item: ToPrimitive {
    it.collect::<OnlineStats>().mean()
}

/// Online state for computing mean, variance and standard deviation.
#[derive(Clone, Copy)]
pub struct OnlineStats {
    size: u64,
    mean: f64,
    variance: f64,
}

impl OnlineStats {
    /// Create initial state.
    ///
    /// Population size, variance and mean are set to `0`.
    pub fn new() -> OnlineStats {
        Default::default()
    }

    /// Initializes variance from a sample.
    pub fn from_slice<T: ToPrimitive>(samples: &[T]) -> OnlineStats {
        samples.iter().map(|n| n.to_f64().unwrap()).collect()
    }

    /// Return the current mean.
    pub fn mean(&self) -> f64 {
        self.mean
    }

    /// Return the current standard deviation.
    pub fn stddev(&self) -> f64 {
        self.variance.sqrt()
    }

    /// Return the current variance.
    pub fn variance(&self) -> f64 {
        self.variance
    }

    /// Add a new sample.
    pub fn add<T: ToPrimitive>(&mut self, sample: T) {
        let sample = sample.to_f64().unwrap();
        // Taken from: http://goo.gl/JKeqvj
        // See also: http://goo.gl/qTtI3V
        let oldmean = self.mean;
        let prevq = self.variance * (self.size as f64);

        self.size += 1;
        self.mean += (sample - oldmean) / (self.size as f64);
        self.variance = (prevq + (sample - oldmean) * (sample - self.mean))
                        / (self.size as f64);
    }

    /// Add a new NULL value to the population.
    ///
    /// This increases the population size by `1`.
    pub fn add_null(&mut self) {
        self.add(0usize);
    }

    /// Returns the number of data points.
    pub fn len(&self) -> usize {
        self.size as usize
    }
}

impl Commute for OnlineStats {
    fn merge(&mut self, v: OnlineStats) {
        // Taken from: http://goo.gl/iODi28
        let (s1, s2) = (self.size as f64, v.size as f64);
        let meandiffsq = (self.mean - v.mean) * (self.mean - v.mean);
        let mean = ((s1 * self.mean) + (s2 * v.mean)) / (s1 + s2);
        let var = (((s1 * self.variance) + (s2 * v.variance))
                   / (s1 + s2))
                  +
                  ((s1 * s2 * meandiffsq) / ((s1 + s2) * (s1 + s2)));
        self.size += v.size;
        self.mean = mean;
        self.variance = var;
    }
}

impl Default for OnlineStats {
    fn default() -> OnlineStats {
        OnlineStats {
            size: 0,
            mean: 0.0,
            variance: 0.0,
        }
    }
}

impl fmt::Debug for OnlineStats {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:.10} +/- {:.10}", self.mean(), self.stddev())
    }
}

impl<T: ToPrimitive> FromIterator<T> for OnlineStats {
    fn from_iter<I: IntoIterator<Item=T>>(it: I) -> OnlineStats {
        let mut v = OnlineStats::new();
        v.extend(it);
        v
    }
}

impl<T: ToPrimitive> Extend<T> for OnlineStats {
    fn extend<I: IntoIterator<Item=T>>(&mut self, it: I) {
        for sample in it {
            self.add(sample)
        }
    }
}

#[cfg(test)]
mod test {
    use {Commute, merge_all};
    use super::OnlineStats;

    #[test]
    fn stddev() {
        // TODO: Convert this to a quickcheck test.
        let expected = OnlineStats::from_slice(&[1usize, 2, 3, 2, 4, 6]);

        let var1 = OnlineStats::from_slice(&[1usize, 2, 3]);
        let var2 = OnlineStats::from_slice(&[2usize, 4, 6]);
        let mut got = var1;
        got.merge(var2);
        assert_eq!(expected.stddev(), got.stddev());
    }

    #[test]
    fn stddev_many() {
        // TODO: Convert this to a quickcheck test.
        let expected = OnlineStats::from_slice(
            &[1usize, 2, 3, 2, 4, 6, 3, 6, 9]);

        let vars = vec![
            OnlineStats::from_slice(&[1usize, 2, 3]),
            OnlineStats::from_slice(&[2usize, 4, 6]),
            OnlineStats::from_slice(&[3usize, 6, 9]),
        ];
        assert_eq!(expected.stddev(),
                   merge_all(vars.into_iter()).unwrap().stddev());
    }
}
```

## File: `src/sorted.rs`
```rust
use std::collections::BinaryHeap;
use std::default::Default;
use std::iter::{FromIterator, IntoIterator};

use num_traits::ToPrimitive;

use {Commute, Partial};

pub fn median_on_sorted<T>(data: &[T]) -> Option<f64>
        where T: PartialOrd + ToPrimitive {
    Some(match data.len() {
        0 => return None,
        1 => data[0].to_f64().unwrap(),
        len if len % 2 == 0 => {
            let v1 = data[(len / 2) - 1].to_f64().unwrap();
            let v2 = data[len / 2].to_f64().unwrap();
            (v1 + v2) / 2.0
        }
        len => {
            data[len / 2].to_f64().unwrap()
        }
    })
}

pub fn mode_on_sorted<T, I>(it: I) -> Option<T>
        where T: PartialOrd, I: Iterator<Item=T> {
    // This approach to computing the mode works very nicely when the
    // number of samples is large and is close to its cardinality.
    // In other cases, a hashmap would be much better.
    // But really, how can we know this when given an arbitrary stream?
    // Might just switch to a hashmap to track frequencies. That would also
    // be generally useful for discovering the cardinality of a sample.
    let (mut mode, mut next) = (None, None);
    let (mut mode_count, mut next_count) = (0usize, 0usize);
    for x in it {
        if mode.as_ref().map(|y| y == &x).unwrap_or(false) {
            mode_count += 1;
        } else if next.as_ref().map(|y| y == &x).unwrap_or(false) {
            next_count += 1;
        } else {
            next = Some(x);
            next_count = 0;
        }

        if next_count > mode_count {
            mode = next;
            mode_count = next_count;
            next = None;
            next_count = 0;
        } else if next_count == mode_count {
            mode = None;
            mode_count = 0usize;
        }
    }
    mode
}

/// A commutative data structure for sorted sequences of data.
///
/// Note that this works on types that do not define a total ordering like
/// `f32` and `f64`. Then an ordering is not defined, an arbitrary order
/// is returned.
#[derive(Clone)]
pub struct Sorted<T> {
    data: BinaryHeap<Partial<T>>,
}

impl<T: PartialOrd> Sorted<T> {
    /// Create initial empty state.
    pub fn new() -> Sorted<T> {
        Default::default()
    }

    /// Add a new element to the set.
    pub fn add(&mut self, v: T) {
        self.data.push(Partial(v))
    }

    /// Returns the number of data points.
    pub fn len(&self) -> usize {
        self.data.len()
    }
}

impl<T: PartialOrd + Clone> Sorted<T> {
    /// Returns the mode of the data.
    pub fn mode(&self) -> Option<T> {
        let p = mode_on_sorted(self.data.clone().into_sorted_vec().into_iter());
        p.map(|p| p.0)
    }
}

impl<T: PartialOrd + ToPrimitive + Clone> Sorted<T> {
    /// Returns the median of the data.
    pub fn median(&self) -> Option<f64> {
        // Grr. The only way to avoid the alloc here is to take `self` by
        // value. Could return `(f64, Sorted<T>)`, but that seems a bit weird.
        //
        // NOTE: Can `std::mem::swap` help us here?
        let data = self.data.clone().into_sorted_vec();
        median_on_sorted(&*data)
    }
}

impl<T: PartialOrd> Commute for Sorted<T> {
    fn merge(&mut self, v: Sorted<T>) {
        // should this be `into_sorted_vec`?
        self.data.extend(v.data.into_vec().into_iter());
    }
}

impl<T: PartialOrd> Default for Sorted<T> {
    fn default() -> Sorted<T> { Sorted { data: BinaryHeap::new() } }
}

impl<T: PartialOrd> FromIterator<T> for Sorted<T> {
    fn from_iter<I: IntoIterator<Item=T>>(it: I) -> Sorted<T> {
        let mut v = Sorted::new();
        v.extend(it);
        v
    }
}

impl<T: PartialOrd> Extend<T> for Sorted<T> {
    fn extend<I: IntoIterator<Item=T>>(&mut self, it: I) {
        self.data.extend(it.into_iter().map(Partial))
    }
}

#[cfg(test)]
mod test {
    use num::ToPrimitive;
    use super::Sorted;

    fn median<T, I>(it: I) -> Option<f64>
       where T: PartialOrd + ToPrimitive + Clone, I: Iterator<Item=T> {
        it.collect::<Sorted<T>>().median()
    }

    fn mode<T, I>(it: I) -> Option<T>
       where T: PartialOrd + Clone, I: Iterator<Item=T> {
        it.collect::<Sorted<T>>().mode()
    }

    #[test]
    fn median_stream() {
        assert_eq!(median(vec![3usize, 5, 7, 9].into_iter()), Some(6.0));
        assert_eq!(median(vec![3usize, 5, 7].into_iter()), Some(5.0));
    }

    #[test]
    fn mode_stream() {
        assert_eq!(mode(vec![3usize, 5, 7, 9].into_iter()), None);
        assert_eq!(mode(vec![3usize, 3, 3, 3].into_iter()), Some(3));
        assert_eq!(mode(vec![3usize, 3, 3, 4].into_iter()), Some(3));
        assert_eq!(mode(vec![4usize, 3, 3, 3].into_iter()), Some(3));
        assert_eq!(mode(vec![1usize, 1, 2, 3, 3].into_iter()), None);
    }

    #[test]
    fn median_floats() {
        assert_eq!(median(vec![3.0f64, 5.0, 7.0, 9.0].into_iter()), Some(6.0));
        assert_eq!(median(vec![3.0f64, 5.0, 7.0].into_iter()), Some(5.0));
    }

    #[test]
    fn mode_floats() {
        assert_eq!(mode(vec![3.0f64, 5.0, 7.0, 9.0].into_iter()), None);
        assert_eq!(mode(vec![3.0f64, 3.0, 3.0, 3.0].into_iter()), Some(3.0));
        assert_eq!(mode(vec![3.0f64, 3.0, 3.0, 4.0].into_iter()), Some(3.0));
        assert_eq!(mode(vec![4.0f64, 3.0, 3.0, 3.0].into_iter()), Some(3.0));
        assert_eq!(mode(vec![1.0f64, 1.0, 2.0, 3.0, 3.0].into_iter()), None);
    }
}
```

## File: `src/unsorted.rs`
```rust
use std::default::Default;
use std::iter::{FromIterator, IntoIterator};
use num_traits::ToPrimitive;

use {Commute, Partial};

/// Compute the exact median on a stream of data.
///
/// (This has time complexity `O(nlogn)` and space complexity `O(n)`.)
pub fn median<I>(it: I) -> Option<f64>
        where I: Iterator, <I as Iterator>::Item: PartialOrd + ToPrimitive {
    it.collect::<Unsorted<_>>().median()
}

/// Compute the exact mode on a stream of data.
///
/// (This has time complexity `O(nlogn)` and space complexity `O(n)`.)
///
/// If the data does not have a mode, then `None` is returned.
pub fn mode<T, I>(it: I) -> Option<T>
       where T: PartialOrd + Clone, I: Iterator<Item=T> {
    it.collect::<Unsorted<T>>().mode()
}

/// Compute the modes on a stream of data.
/// 
/// If there is a single mode, then only that value is returned in the `Vec`
/// however, if there multiple values tied for occuring the most amount of times
/// those values are returned.
/// 
/// ## Example
/// ```
/// use stats;
/// 
/// let vals = vec![1, 1, 2, 2, 3];
/// 
/// assert_eq!(stats::modes(vals.into_iter()), vec![1, 2]);
/// ```
/// This has time complexity `O(n)`
///
/// If the data does not have a mode, then an empty `Vec` is returned.
pub fn modes<T, I>(it: I) -> Vec<T>
       where T: PartialOrd + Clone, I: Iterator<Item=T> {
    it.collect::<Unsorted<T>>().modes()
}

fn median_on_sorted<T>(data: &[T]) -> Option<f64>
        where T: PartialOrd + ToPrimitive {
    Some(match data.len() {
        0 => return None,
        1 => data[0].to_f64().unwrap(),
        len if len % 2 == 0 => {
            let v1 = data[(len / 2) - 1].to_f64().unwrap();
            let v2 = data[len / 2].to_f64().unwrap();
            (v1 + v2) / 2.0
        }
        len => {
            data[len / 2].to_f64().unwrap()
        }
    })
}

fn mode_on_sorted<T, I>(it: I) -> Option<T>
        where T: PartialOrd, I: Iterator<Item=T> {
    // This approach to computing the mode works very nicely when the
    // number of samples is large and is close to its cardinality.
    // In other cases, a hashmap would be much better.
    // But really, how can we know this when given an arbitrary stream?
    // Might just switch to a hashmap to track frequencies. That would also
    // be generally useful for discovering the cardinality of a sample.
    let (mut mode, mut next) = (None, None);
    let (mut mode_count, mut next_count) = (0usize, 0usize);
    for x in it {
        if mode.as_ref().map(|y| y == &x).unwrap_or(false) {
            mode_count += 1;
        } else if next.as_ref().map(|y| y == &x).unwrap_or(false) {
            next_count += 1;
        } else {
            next = Some(x);
            next_count = 0;
        }

        if next_count > mode_count {
            mode = next;
            mode_count = next_count;
            next = None;
            next_count = 0;
        } else if next_count == mode_count {
            mode = None;
            mode_count = 0usize;
        }
    }
    mode
}

fn modes_on_sorted<T, I>(it: I) -> Vec<T>
        where T: PartialOrd, I: Iterator<Item=T> {

    let mut highest_mode = 1_u32;
    let mut modes: Vec<u32> = vec![];
    let mut values = vec![];
    let mut count = 0;
    for x in it {
        if values.len() == 0 {
            values.push(x);
            modes.push(1);
            continue
        }
        if x == values[count] {
            modes[count] += 1;
            if highest_mode < modes[count] {
                highest_mode = modes[count];
            }
        } else {
            values.push(x);
            modes.push(1);
            count += 1;
        }
    }
    modes.into_iter()
        .zip(values)
        .filter(|(cnt, _val)| *cnt == highest_mode && highest_mode > 1)
        .map(|(_, val)| val)
        .collect()
}

/// A commutative data structure for lazily sorted sequences of data.
///
/// The sort does not occur until statistics need to be computed.
///
/// Note that this works on types that do not define a total ordering like
/// `f32` and `f64`. When an ordering is not defined, an arbitrary order
/// is returned.
#[derive(Clone)]
pub struct Unsorted<T> {
    data: Vec<Partial<T>>,
    sorted: bool,
}

impl<T: PartialOrd> Unsorted<T> {
    /// Create initial empty state.
    pub fn new() -> Unsorted<T> {
        Default::default()
    }

    /// Add a new element to the set.
    pub fn add(&mut self, v: T) {
        self.dirtied();
        self.data.push(Partial(v))
    }

    /// Return the number of data points.
    pub fn len(&self) -> usize {
        self.data.len()
    }

    fn sort(&mut self) {
        if !self.sorted {
            self.data.sort();
        }
    }

    fn dirtied(&mut self) {
        self.sorted = false;
    }
}

impl<T: PartialOrd + Eq + Clone> Unsorted<T> {
    pub fn cardinality(&mut self) -> usize {
        self.sort();
        let mut set = self.data.clone();
        set.dedup();
        set.len()
    }
}

impl<T: PartialOrd + Clone> Unsorted<T> {
    /// Returns the mode of the data.
    pub fn mode(&mut self) -> Option<T> {
        self.sort();
        mode_on_sorted(self.data.iter()).map(|p| p.0.clone())
    }

    /// Returns the modes of the data.
    pub fn modes(&mut self) -> Vec<T> {
        self.sort();
        modes_on_sorted(self.data.iter())
            .into_iter()
            .map(|p| p.0.clone())
            .collect()
    }
}

impl<T: PartialOrd + ToPrimitive> Unsorted<T> {
    /// Returns the median of the data.
    pub fn median(&mut self) -> Option<f64> {
        self.sort();
        median_on_sorted(&*self.data)
    }
}

impl<T: PartialOrd> Commute for Unsorted<T> {
    fn merge(&mut self, v: Unsorted<T>) {
        self.dirtied();
        self.data.extend(v.data.into_iter());
    }
}

impl<T: PartialOrd> Default for Unsorted<T> {
    fn default() -> Unsorted<T> {
        Unsorted {
            data: Vec::with_capacity(1000),
            sorted: true,
        }
    }
}

impl<T: PartialOrd> FromIterator<T> for Unsorted<T> {
    fn from_iter<I: IntoIterator<Item=T>>(it: I) -> Unsorted<T> {
        let mut v = Unsorted::new();
        v.extend(it);
        v
    }
}

impl<T: PartialOrd> Extend<T> for Unsorted<T> {
    fn extend<I: IntoIterator<Item=T>>(&mut self, it: I) {
        self.dirtied();
        self.data.extend(it.into_iter().map(Partial))
    }
}

#[cfg(test)]
mod test {
    use super::{median, mode, modes};

    #[test]
    fn median_stream() {
        assert_eq!(median(vec![3usize, 5, 7, 9].into_iter()), Some(6.0));
        assert_eq!(median(vec![3usize, 5, 7].into_iter()), Some(5.0));
    }

    #[test]
    fn mode_stream() {
        assert_eq!(mode(vec![3usize, 5, 7, 9].into_iter()), None);
        assert_eq!(mode(vec![3usize, 3, 3, 3].into_iter()), Some(3));
        assert_eq!(mode(vec![3usize, 3, 3, 4].into_iter()), Some(3));
        assert_eq!(mode(vec![4usize, 3, 3, 3].into_iter()), Some(3));
        assert_eq!(mode(vec![1usize, 1, 2, 3, 3].into_iter()), None);
    }

    #[test]
    fn median_floats() {
        assert_eq!(median(vec![3.0f64, 5.0, 7.0, 9.0].into_iter()), Some(6.0));
        assert_eq!(median(vec![3.0f64, 5.0, 7.0].into_iter()), Some(5.0));
        assert_eq!(median(vec![1.0f64, 2.5, 3.0].into_iter()), Some(2.5));
    }

    #[test]
    fn mode_floats() {
        assert_eq!(mode(vec![3.0f64, 5.0, 7.0, 9.0].into_iter()), None);
        assert_eq!(mode(vec![3.0f64, 3.0, 3.0, 3.0].into_iter()), Some(3.0));
        assert_eq!(mode(vec![3.0f64, 3.0, 3.0, 4.0].into_iter()), Some(3.0));
        assert_eq!(mode(vec![4.0f64, 3.0, 3.0, 3.0].into_iter()), Some(3.0));
        assert_eq!(mode(vec![1.0f64, 1.0, 2.0, 3.0, 3.0].into_iter()), None);
    }

    #[test]
    fn modes_stream() {
        assert_eq!(modes(vec![3usize, 5, 7, 9].into_iter()), vec![]);
        assert_eq!(modes(vec![3usize, 3, 3, 3].into_iter()), vec![3]);
        assert_eq!(modes(vec![3usize, 3, 4, 4].into_iter()), vec![3, 4]);
        assert_eq!(modes(vec![4usize, 3, 3, 3].into_iter()), vec![3]);
        assert_eq!(modes(vec![1usize, 1, 2, 2].into_iter()), vec![1, 2]);
        let vec: Vec<u32> = vec![];
        assert_eq!(modes(vec.into_iter()), vec![]);
    }

    #[test]
    fn modes_floats() {
        assert_eq!(modes(vec![3_f64, 5.0, 7.0, 9.0].into_iter()), vec![]);
        assert_eq!(modes(vec![3_f64, 3.0, 3.0, 3.0].into_iter()), vec![3.0]);
        assert_eq!(modes(vec![3_f64, 3.0, 4.0, 4.0].into_iter()), vec![3.0, 4.0]);
        assert_eq!(modes(vec![1_f64, 1.0, 2.0, 3.0, 3.0].into_iter()), vec![1.0, 3.0]);
    }
}
```

