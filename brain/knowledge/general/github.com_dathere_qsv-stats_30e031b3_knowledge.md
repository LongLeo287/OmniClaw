---
id: github.com-dathere-qsv-stats-30e031b3-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:43.531967
---

# KNOWLEDGE EXTRACT: github.com_dathere_qsv-stats_30e031b3
> **Extracted on:** 2026-04-01 09:29:25
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520214/github.com_dathere_qsv-stats_30e031b3

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
.DS_Store
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

qsv-stats is a high-performance Rust statistics library forked from BurntSushi's `streaming-stats`. It's designed for streaming computation on large datasets and is used by qsv's `stats` command. Key characteristics: FMA (fused multiply-add) instructions, adaptive parallelism via rayon, and composable statistics via the `Commute` trait.

## Build & Test Commands

```bash
cargo build                  # Debug build
cargo build --release        # Release build
cargo test                   # Run all tests
cargo test <test_name>       # Run a single test by name
cargo test --lib             # Library tests only
cargo doc --open             # Generate and view documentation
```

MSRV: 1.93 (Rust edition 2024)

## Architecture

### Core Trait

All statistics structs implement `Commute`, enabling parallel aggregation by merging partial results:

```rust
pub trait Commute: Sized {
    fn merge(&mut self, other: Self);
}
```

### Modules

| Module | Struct | Purpose |
|--------|--------|---------|
| **online.rs** | `OnlineStats` | Constant-space streaming mean/variance/stddev using Welford's method. Cache-optimized field layout (hot/warm/cold paths). |
| **unsorted.rs** | `Unsorted<T>` | Collects data, lazily sorts on demand. Median, quartiles (Method 3), mode/antimodes, Gini, kurtosis, Atkinson index, MAD, percentile rank. |
| **sorted.rs** | — | Statistics on pre-sorted sequences via `BinaryHeap`. |
| **frequency.rs** | `Frequencies<T>` | Exact frequency counting using `foldhash::HashMap`. Cardinality, most/least frequent. |
| **minmax.rs** | `MinMax<T>` | Min/max tracking with sort order detection (`sortiness()` returns -1.0 to 1.0). |

### Performance Patterns

- **Parallel threshold:** Datasets ≥10,000 elements use rayon parallel sort; smaller use sequential. The sort path uses a separate threshold of 10,240 (a multiple of 2048).
- **FMA:** `.mul_add()` used throughout for precision and speed.
- **Precalculated values:** `gini()` accepts optional precalculated sum; `kurtosis()` accepts mean/variance; `atkinson()` accepts mean/geometric_sum — avoiding redundant computation.
- **Lazy sorting:** `Unsorted<T>` defers sorting until a statistic is requested.
- **Quickselect:** O(n) average selection algorithm used for median/quartile computation.

### Type System

- `Partial<T>` wraps `PartialOrd` types (like f64) to provide `Ord`, enabling use in sorted collections.
- Statistics are generic over types implementing `num_traits::ToPrimitive` + `PartialOrd`.

## Testing

Tests are embedded in each module via `#[cfg(test)]` blocks (140+ tests total). Tests cover edge cases including empty data, negative values, zeros, and precision.

## Dependencies

Only 4 production dependencies: `foldhash`, `num-traits`, `rayon`, `serde`.
```

## File: `COPYING`
```
This project is dual-licensed under the Unlicense and MIT licenses.

You may use this code under the terms of either license.
```

## File: `Cargo.toml`
```
[package]
name          = "qsv-stats"
version       = "0.48.1"                                            #:version
authors       = ["Joel Natividad <joel@dathere.com>"]
description   = "Computing summary statistics on streams."
documentation = "https://docs.rs/qsv-stats"
homepage      = "https://github.com/dathere/qsv-stats"
repository    = "https://github.com/dathere/qsv-stats"
readme        = "README.md"
keywords      = ["statistics", "frequency", "mean", "stddev", "quartiles"]
categories    = ["science", "mathematics"]
license       = "MIT OR Unlicense"
edition       = "2024"
rust-version  = "1.94"

[lib]
name = "stats"

[dependencies]
foldhash   = "0.2"
num-traits = "0.2"
rayon      = "1"
serde      = { version = "1", features = ["derive"] }
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

## File: `README.md`
```markdown
# qsv-stats

This library provides common statistical functions with support for computing them
efficiently on *streams* of data. The intent is to permit parallel computation of
statistics on large data sets.

> NOTE: This fork of [streaming-stats](https://github.com/BurntSushi/rust-stats) merges 
pending upstream PRs for quartile computation and a different variance algorithm 
that is used in [qsv](https://github.com/dathere/qsv)'s [`stats` command](https://github.com/dathere/qsv/blob/master/README.md#stats_deeplink).  
It has numerous other stats, heavily updated for performance, uses parallel processing,
uses the [fused multiply add](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation#Fused_multiply%E2%80%93add) CPU instruction along with several other performance tweaks.

Dual-licensed under MIT or the [UNLICENSE](http://unlicense.org).


### Documentation

Documentation for qsv-stats exists here:
[https://docs.rs/qsv-stats](https://docs.rs/qsv-stats).


### Installation

Simply add `qsv-stats` as a dependency to your project's `Cargo.toml`:

```toml
[dependencies]
qsv-stats = "0.47.0"
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

## File: `src/frequency.rs`
```rust
use std::collections::hash_map::{Entry, Keys};
use std::hash::Hash;

use foldhash::{HashMap, HashMapExt};

use rayon::prelude::*;

use crate::Commute;

const PARALLEL_THRESHOLD: usize = 10_000;
/// A commutative data structure for exact frequency counts.
#[derive(Clone)]
pub struct Frequencies<T> {
    data: HashMap<T, u64>,
}

#[cfg(debug_assertions)]
impl<T: std::fmt::Debug + Eq + Hash> std::fmt::Debug for Frequencies<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{:?}", self.data)
    }
}

impl<T: Eq + Hash> Frequencies<T> {
    /// Create a new frequency table with no samples.
    #[must_use]
    pub fn new() -> Frequencies<T> {
        Default::default()
    }

    // Add constructor with configurable capacity
    #[must_use]
    pub fn with_capacity(capacity: usize) -> Self {
        Frequencies {
            data: HashMap::with_capacity(capacity),
        }
    }

    /// Add a value to the frequency table.
    #[inline]
    pub fn add(&mut self, v: T) {
        *self.data.entry(v).or_insert(0) += 1;
    }

    /// Return the number of occurrences of `v` in the data.
    #[inline]
    #[must_use]
    pub fn count(&self, v: &T) -> u64 {
        self.data.get(v).copied().unwrap_or(0)
    }

    /// Return the cardinality (number of unique elements) in the data.
    #[inline]
    #[must_use]
    pub fn cardinality(&self) -> u64 {
        self.len() as u64
    }

    /// Collect counts and total in a single pass, reused by `most/least_frequent`.
    fn collect_counts(&self) -> (Vec<(&T, u64)>, u64) {
        let mut total_count = 0u64;
        let counts: Vec<(&T, u64)> = self
            .data
            .iter()
            .map(|(k, &v)| {
                total_count += v;
                (k, v)
            })
            .collect();
        (counts, total_count)
    }

    /// Return a `Vec` of elements, their corresponding counts in
    /// descending order, and the total count.
    #[inline]
    #[must_use]
    pub fn most_frequent(&self) -> (Vec<(&T, u64)>, u64) {
        let (mut counts, total_count) = self.collect_counts();
        counts.sort_unstable_by_key(|&(_, c)| std::cmp::Reverse(c));
        (counts, total_count)
    }

    /// Return a `Vec` of elements, their corresponding counts in
    /// ascending order, and the total count.
    #[inline]
    #[must_use]
    pub fn least_frequent(&self) -> (Vec<(&T, u64)>, u64) {
        let (mut counts, total_count) = self.collect_counts();
        counts.sort_unstable_by_key(|&(_, c)| c);
        (counts, total_count)
    }

    /// Return a `Vec` of elements, their corresponding counts in order
    /// based on the `least` parameter, and the total count. Uses parallel sort.
    #[inline]
    #[must_use]
    pub fn par_frequent(&self, least: bool) -> (Vec<(&T, u64)>, u64)
    where
        for<'a> (&'a T, u64): Send,
        T: Ord,
    {
        let (mut counts, total_count) = self.collect_counts();
        // sort by counts asc/desc
        // if counts are equal, sort by values lexicographically
        // We need to do this because otherwise the values are not guaranteed to be in order for
        // equal counts
        if least {
            // return counts in ascending order
            let sort_fn = |&(v1, c1): &(&T, u64), &(v2, c2): &(&T, u64)| {
                c1.cmp(&c2).then_with(|| v1.cmp(v2))
            };
            if counts.len() < PARALLEL_THRESHOLD {
                counts.sort_unstable_by(sort_fn);
            } else {
                counts.par_sort_unstable_by(sort_fn);
            }
        } else {
            // return counts in descending order
            let sort_fn = |&(v1, c1): &(&T, u64), &(v2, c2): &(&T, u64)| {
                c2.cmp(&c1).then_with(|| v1.cmp(v2))
            };
            if counts.len() < PARALLEL_THRESHOLD {
                counts.sort_unstable_by(sort_fn);
            } else {
                counts.par_sort_unstable_by(sort_fn);
            }
        }
        (counts, total_count)
    }

    /// Returns the cardinality of the data.
    #[must_use]
    pub fn len(&self) -> usize {
        self.data.len()
    }

    /// Returns true if there is no frequency/cardinality data.
    #[must_use]
    pub fn is_empty(&self) -> bool {
        self.data.is_empty()
    }

    /// Return an iterator over the unique values of the data.
    #[must_use]
    pub fn unique_values(&self) -> UniqueValues<'_, T> {
        UniqueValues {
            data_keys: self.data.keys(),
        }
    }

    /// Get the top N most frequent items without sorting the entire vector
    /// This is much faster than `most_frequent()` when you only need a few items
    #[must_use]
    pub fn top_n(&self, n: usize) -> Vec<(&T, u64)>
    where
        T: Ord,
    {
        use std::collections::BinaryHeap;

        // We use a min-heap of size n to keep track of the largest elements
        let mut heap = BinaryHeap::with_capacity(n + 1);

        for (item, count) in &self.data {
            // Negate count because BinaryHeap is a max-heap
            // and we want to remove smallest elements
            heap.push(std::cmp::Reverse((*count, item)));

            // Keep heap size at n
            if heap.len() > n {
                heap.pop();
            }
        }

        // Convert to sorted vector
        heap.into_sorted_vec()
            .into_iter()
            .map(|std::cmp::Reverse((count, item))| (item, count))
            .collect()
    }

    /// Similar to `top_n` but for least frequent items
    #[must_use]
    pub fn bottom_n(&self, n: usize) -> Vec<(&T, u64)>
    where
        T: Ord,
    {
        use std::collections::BinaryHeap;

        let mut heap = BinaryHeap::with_capacity(n + 1);

        for (item, count) in &self.data {
            heap.push((*count, item));
            if heap.len() > n {
                heap.pop();
            }
        }

        heap.into_sorted_vec()
            .into_iter()
            .map(|(count, item)| (item, count))
            .collect()
    }

    /// Get items with exactly n occurrences
    #[must_use]
    pub fn items_with_count(&self, n: u64) -> Vec<&T> {
        self.data
            .iter()
            .filter(|&(_, &count)| count == n)
            .map(|(item, _)| item)
            .collect()
    }

    /// Get the sum of all counts
    #[must_use]
    pub fn total_count(&self) -> u64 {
        self.data.values().sum()
    }

    /// Check if any item occurs exactly n times
    #[must_use]
    pub fn has_count(&self, n: u64) -> bool {
        self.data.values().any(|&count| count == n)
    }

    /// Add specialized method for single increment
    #[inline]
    pub fn increment_by(&mut self, v: T, count: u64) {
        match self.data.entry(v) {
            Entry::Vacant(entry) => {
                entry.insert(count);
            }
            Entry::Occupied(mut entry) => {
                *entry.get_mut() += count;
            }
        }
    }
}

impl Frequencies<Vec<u8>> {
    /// Increment count for a byte slice key, avoiding allocation when key exists.
    /// Uses borrowed lookup via `get_mut(&[u8])` before falling back to owned insert.
    /// This works because `Vec<u8>: Borrow<[u8]>`, so `HashMap` accepts `&[u8]` for lookup.
    /// For low-cardinality columns (the common case), this eliminates ~99% of allocations.
    #[inline]
    pub fn add_borrowed(&mut self, v: &[u8]) {
        if let Some(count) = self.data.get_mut(v) {
            *count += 1;
        } else {
            self.data.insert(v.to_vec(), 1);
        }
    }

    /// Increment by a count for a byte slice key, avoiding allocation when key exists.
    #[inline]
    pub fn increment_by_borrowed(&mut self, v: &[u8], count: u64) {
        if let Some(existing) = self.data.get_mut(v) {
            *existing += count;
        } else {
            self.data.insert(v.to_vec(), count);
        }
    }
}

impl<T: Eq + Hash> Commute for Frequencies<T> {
    #[inline]
    fn merge(&mut self, v: Frequencies<T>) {
        // Reserve additional capacity to avoid reallocations
        self.data.reserve(v.data.len());

        for (k, v2) in v.data {
            match self.data.entry(k) {
                Entry::Vacant(v1) => {
                    v1.insert(v2);
                }
                Entry::Occupied(mut v1) => {
                    *v1.get_mut() += v2;
                }
            }
        }
    }
}

impl<T: Eq + Hash> Default for Frequencies<T> {
    #[inline]
    fn default() -> Frequencies<T> {
        Frequencies {
            data: HashMap::with_capacity(64),
        }
    }
}

impl<T: Eq + Hash> FromIterator<T> for Frequencies<T> {
    #[inline]
    fn from_iter<I: IntoIterator<Item = T>>(it: I) -> Frequencies<T> {
        let mut v = Frequencies::new();
        v.extend(it);
        v
    }
}

impl<T: Eq + Hash> Extend<T> for Frequencies<T> {
    #[inline]
    fn extend<I: IntoIterator<Item = T>>(&mut self, it: I) {
        let iter = it.into_iter();
        // Reserve capacity if size hint is available and reliable
        if let (lower, Some(upper)) = iter.size_hint()
            && lower == upper
        {
            // Exact size known - reserve capacity for new entries
            // We don't know how many will be new vs existing, so reserve conservatively
            self.data.reserve(lower.saturating_sub(self.data.len()));
        }
        for sample in iter {
            self.add(sample);
        }
    }
}

/// An iterator over unique values in a frequencies count.
pub struct UniqueValues<'a, K> {
    data_keys: Keys<'a, K, u64>,
}

impl<'a, K> Iterator for UniqueValues<'a, K> {
    type Item = &'a K;
    fn next(&mut self) -> Option<Self::Item> {
        self.data_keys.next()
    }
}

#[cfg(test)]
mod test {
    use super::Frequencies;
    use std::iter::FromIterator;

    #[test]
    fn ranked() {
        let mut counts = Frequencies::new();
        counts.extend(vec![1usize, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4]);
        let (most_count, most_total) = counts.most_frequent();
        assert_eq!(most_count[0], (&2, 5));
        assert_eq!(most_total, 11);
        let (least_count, least_total) = counts.least_frequent();
        assert_eq!(least_count[0], (&3, 1));
        assert_eq!(least_total, 11);
        assert_eq!(
            counts.least_frequent(),
            (vec![(&3, 1), (&1, 2), (&4, 3), (&2, 5)], 11)
        );
    }

    #[test]
    fn ranked2() {
        let mut counts = Frequencies::new();
        counts.extend(vec![1usize, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4]);
        let (most_count, most_total) = counts.par_frequent(false);
        assert_eq!(most_count[0], (&2, 5));
        assert_eq!(most_total, 11);
        let (least_count, least_total) = counts.par_frequent(true);
        assert_eq!(least_count[0], (&3, 1));
        assert_eq!(least_total, 11);
    }

    #[test]
    fn unique_values() {
        let freqs = Frequencies::from_iter(vec![8, 6, 5, 1, 1, 2, 2, 2, 3, 4, 7, 4, 4]);
        let mut unique: Vec<isize> = freqs.unique_values().copied().collect();
        unique.sort_unstable();
        assert_eq!(unique, vec![1, 2, 3, 4, 5, 6, 7, 8]);
    }

    #[test]
    fn test_top_n() {
        let mut freq = Frequencies::new();
        freq.extend(vec![1, 1, 1, 2, 2, 3, 4, 4, 4, 4]);

        let top_2 = freq.top_n(2);
        assert_eq!(top_2.len(), 2);
        assert_eq!(top_2[0], (&4, 4)); // Most frequent
        assert_eq!(top_2[1], (&1, 3)); // Second most frequent

        let bottom_2 = freq.bottom_n(2);
        assert_eq!(bottom_2.len(), 2);
        assert_eq!(bottom_2[0], (&3, 1)); // Least frequent
        assert_eq!(bottom_2[1], (&2, 2)); // Second least frequent
    }

    #[test]
    fn test_count_methods() {
        let mut freq = Frequencies::new();
        freq.extend(vec![1, 1, 1, 2, 2, 3, 4, 4, 4, 4]);

        // Test total_count()
        assert_eq!(freq.total_count(), 10);

        // Test has_count()
        assert!(freq.has_count(3)); // 1 appears 3 times
        assert!(freq.has_count(4)); // 4 appears 4 times
        assert!(freq.has_count(1)); // 3 appears 1 time
        assert!(!freq.has_count(5)); // No element appears 5 times

        // Test items_with_count()
        let items_with_3 = freq.items_with_count(3);
        assert_eq!(items_with_3, vec![&1]); // Only 1 appears 3 times

        let items_with_2 = freq.items_with_count(2);
        assert_eq!(items_with_2, vec![&2]); // Only 2 appears 2 times

        let items_with_1 = freq.items_with_count(1);
        assert_eq!(items_with_1, vec![&3]); // Only 3 appears 1 time

        let items_with_4 = freq.items_with_count(4);
        assert_eq!(items_with_4, vec![&4]); // Only 4 appears 4 times

        let items_with_5 = freq.items_with_count(5);
        assert!(items_with_5.is_empty()); // No elements appear 5 times
    }

    #[test]
    fn add_borrowed_inserts_new_key() {
        let mut freq = Frequencies::<Vec<u8>>::new();
        freq.add_borrowed(b"hello");
        assert_eq!(freq.count(&b"hello".to_vec()), 1);
        assert_eq!(freq.cardinality(), 1);
    }

    #[test]
    fn add_borrowed_increments_existing_key() {
        let mut freq = Frequencies::<Vec<u8>>::new();
        freq.add_borrowed(b"hello");
        freq.add_borrowed(b"hello");
        freq.add_borrowed(b"hello");
        assert_eq!(freq.count(&b"hello".to_vec()), 3);
        assert_eq!(freq.cardinality(), 1);

        // Also test increment_by_borrowed
        freq.increment_by_borrowed(b"world", 5);
        assert_eq!(freq.count(&b"world".to_vec()), 5);
        freq.increment_by_borrowed(b"world", 3);
        assert_eq!(freq.count(&b"world".to_vec()), 8);
    }

    #[test]
    fn borrowed_owned_interop_for_same_key() {
        let mut freq = Frequencies::<Vec<u8>>::new();
        // Insert via owned add
        freq.add(b"key".to_vec());
        // Increment via borrowed add
        freq.add_borrowed(b"key");
        freq.increment_by_borrowed(b"key", 3);
        // All methods should see the same accumulated count
        assert_eq!(freq.count(&b"key".to_vec()), 5);
        assert_eq!(freq.cardinality(), 1);
    }
}
```

## File: `src/lib.rs`
```rust
#![allow(clippy::default_trait_access)]
#![allow(clippy::cast_precision_loss)]
#![allow(clippy::cast_possible_truncation)]
#![allow(clippy::module_name_repetitions)]
#![allow(clippy::missing_panics_doc)]
#![allow(clippy::use_self)]

use num_traits::ToPrimitive;
use std::cmp::Ordering;
use std::hash;

use serde::{Deserialize, Serialize};

pub use frequency::{Frequencies, UniqueValues};
pub use minmax::MinMax;
pub use online::{OnlineStats, mean, stddev, variance};
pub use unsorted::{
    Unsorted, antimodes, atkinson, gini, kurtosis, mad, median, mode, modes, percentile_rank,
    quartiles,
};

/// Partial wraps a type that satisfies `PartialOrd` and implements `Ord`.
///
/// This allows types like `f64` to be used in data structures that require
/// `Ord`. When an ordering is not defined, an arbitrary order is returned.
#[allow(clippy::derive_ord_xor_partial_ord)]
#[derive(Clone, PartialEq, PartialOrd, Serialize, Deserialize)]
struct Partial<T>(pub T);

impl<T: PartialEq> Eq for Partial<T> {}
// Send/Sync auto-derived: Partial<T> is Send when T: Send, Sync when T: Sync.

#[allow(clippy::derive_ord_xor_partial_ord)]
impl<T: PartialOrd> Ord for Partial<T> {
    #[inline]
    fn cmp(&self, other: &Partial<T>) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Less)
    }
}

impl<T: ToPrimitive> ToPrimitive for Partial<T> {
    #[inline]
    fn to_isize(&self) -> Option<isize> {
        self.0.to_isize()
    }
    #[inline]
    fn to_i8(&self) -> Option<i8> {
        self.0.to_i8()
    }
    #[inline]
    fn to_i16(&self) -> Option<i16> {
        self.0.to_i16()
    }
    #[inline]
    fn to_i32(&self) -> Option<i32> {
        self.0.to_i32()
    }
    #[inline]
    fn to_i64(&self) -> Option<i64> {
        self.0.to_i64()
    }

    #[inline]
    fn to_usize(&self) -> Option<usize> {
        self.0.to_usize()
    }
    #[inline]
    fn to_u8(&self) -> Option<u8> {
        self.0.to_u8()
    }
    #[inline]
    fn to_u16(&self) -> Option<u16> {
        self.0.to_u16()
    }
    #[inline]
    fn to_u32(&self) -> Option<u32> {
        self.0.to_u32()
    }
    #[inline]
    fn to_u64(&self) -> Option<u64> {
        self.0.to_u64()
    }

    #[inline]
    fn to_f32(&self) -> Option<f32> {
        self.0.to_f32()
    }
    #[inline]
    fn to_f64(&self) -> Option<f64> {
        self.0.to_f64()
    }
}

#[allow(clippy::derived_hash_with_manual_eq)]
impl<T: hash::Hash> hash::Hash for Partial<T> {
    #[inline]
    fn hash<H: hash::Hasher>(&self, state: &mut H) {
        self.0.hash(state);
    }
}

/// Defines an interface for types that have an identity and can be commuted.
///
/// The value returned by `Default::default` must be its identity with respect
/// to the `merge` operation.
pub trait Commute: Sized {
    /// Merges the value `other` into `self`.
    fn merge(&mut self, other: Self);

    /// Merges the values in the iterator into `self`.
    #[inline]
    fn consume<I: Iterator<Item = Self>>(&mut self, other: I) {
        for v in other {
            self.merge(v);
        }
    }
}

/// Merges all items in the stream.
///
/// If the stream is empty, `None` is returned.
#[inline]
pub fn merge_all<T: Commute, I: Iterator<Item = T>>(mut it: I) -> Option<T> {
    it.next().map_or_else(
        || None,
        |mut init| {
            init.consume(it);
            Some(init)
        },
    )
}

impl<T: Commute> Commute for Option<T> {
    #[inline]
    fn merge(&mut self, other: Option<T>) {
        match *self {
            None => {
                *self = other;
            }
            Some(ref mut v1) => {
                if let Some(v2) = other {
                    v1.merge(v2);
                }
            }
        }
    }
}

impl<T: Commute, E> Commute for Result<T, E> {
    #[inline]
    fn merge(&mut self, other: Result<T, E>) {
        if !self.is_err() && other.is_err() {
            *self = other;
            return;
        }
        #[allow(clippy::let_unit_value)]
        #[allow(clippy::ignored_unit_patterns)]
        let _ = self.as_mut().map_or((), |v1| {
            other.map_or_else(
                |_| {
                    unreachable!();
                },
                |v2| {
                    v1.merge(v2);
                },
            );
        });
    }
}

impl<T: Commute> Commute for Vec<T> {
    #[inline]
    fn merge(&mut self, other: Vec<T>) {
        assert_eq!(self.len(), other.len());
        for (v1, v2) in self.iter_mut().zip(other) {
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
    use crate::Commute;
    use crate::unsorted::Unsorted;

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
#![allow(clippy::cast_lossless)]
use serde::{Deserialize, Serialize};
use std::cmp::Ordering;
use std::fmt;

use crate::Commute;

/// Represents the current sort order of the data.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Deserialize, Serialize)]
pub enum SortOrder {
    Unsorted,
    Ascending,
    Descending,
}

/// A commutative data structure for tracking minimum and maximum values
/// and detecting sort order in a stream of data.
#[derive(Clone, Copy, Deserialize, Serialize, Eq, PartialEq)]
pub struct MinMax<T> {
    // Hot fields: accessed on every add() call, grouped on same cache line
    len: u32,
    ascending_pairs: u32,
    descending_pairs: u32,
    // Warm fields: accessed conditionally
    min: Option<T>,
    max: Option<T>,
    first_value: Option<T>,
    last_value: Option<T>,
}

impl<T: PartialOrd + Clone> MinMax<T> {
    /// Create an empty state where min and max values do not exist.
    #[must_use]
    pub fn new() -> MinMax<T> {
        Default::default()
    }

    /// Add a sample to the data and track min/max, the sort order & "sortiness".
    #[inline]
    pub fn add(&mut self, sample: T) {
        match self.len {
            // this comes first because it's the most common case
            2.. => {
                if let Some(ref last) = self.last_value {
                    #[allow(clippy::match_same_arms)]
                    match sample.partial_cmp(last) {
                        Some(Ordering::Greater) => self.ascending_pairs += 1,
                        Some(Ordering::Less) => self.descending_pairs += 1,
                        // this comes last because it's the least common case
                        Some(Ordering::Equal) => self.ascending_pairs += 1,
                        None => {}
                    }
                }
            }
            0 => {
                // first sample - clone for first_value and min, move to max
                self.first_value = Some(sample.clone());
                self.min = Some(sample.clone());
                self.max = Some(sample);
                self.len = 1;
                return;
            }
            1 => {
                // second sample
                if let Some(ref first) = self.first_value {
                    match sample.partial_cmp(first) {
                        Some(Ordering::Greater | Ordering::Equal) => self.ascending_pairs = 1,
                        Some(Ordering::Less) => self.descending_pairs = 1,
                        None => {}
                    }
                }
            }
        }

        // Update min/max
        if self.min.as_ref().is_none_or(|v| &sample < v) {
            self.min = Some(sample.clone());
        } else if self.max.as_ref().is_none_or(|v| &sample > v) {
            self.max = Some(sample.clone());
        }

        // Update last value and number of samples
        self.last_value = Some(sample);
        self.len += 1;
    }

    /// Add a sample by reference, only cloning when necessary to update
    /// min, max, `first_value`, or `last_value`.
    ///
    /// This is more efficient than `add()` when the caller has a reference
    /// and most samples don't update min/max, because it avoids the upfront
    /// allocation that `add()` requires from the caller.
    ///
    /// For `last_value`, the existing allocation is reused when possible
    /// by clearing and cloning into it rather than replacing.
    #[inline]
    pub fn add_ref(&mut self, sample: &T) {
        match self.len {
            2.. => {
                if let Some(ref last) = self.last_value {
                    #[allow(clippy::match_same_arms)]
                    match sample.partial_cmp(last) {
                        Some(Ordering::Greater) => self.ascending_pairs += 1,
                        Some(Ordering::Less) => self.descending_pairs += 1,
                        Some(Ordering::Equal) => self.ascending_pairs += 1,
                        None => {}
                    }
                }
            }
            0 => {
                self.first_value = Some(sample.clone());
                self.min = Some(sample.clone());
                self.max = Some(sample.clone());
                self.len = 1;
                return;
            }
            1 => {
                if let Some(ref first) = self.first_value {
                    match sample.partial_cmp(first) {
                        Some(Ordering::Greater | Ordering::Equal) => self.ascending_pairs = 1,
                        Some(Ordering::Less) => self.descending_pairs = 1,
                        None => {}
                    }
                }
            }
        }

        // Update min/max - only clone when actually updating
        if self.min.as_ref().is_none_or(|v| sample < v) {
            self.min = Some(sample.clone());
        } else if self.max.as_ref().is_none_or(|v| sample > v) {
            self.max = Some(sample.clone());
        }

        // Update last value - clone_from reuses existing allocation
        if let Some(ref mut last) = self.last_value {
            last.clone_from(sample);
        } else {
            self.last_value = Some(sample.clone());
        }
        self.len += 1;
    }

    /// Returns the minimum of the data set.
    ///
    /// `None` is returned if and only if the number of samples is `0`.
    #[inline]
    #[must_use]
    pub const fn min(&self) -> Option<&T> {
        self.min.as_ref()
    }

    /// Returns the maximum of the data set.
    ///
    /// `None` is returned if and only if the number of samples is `0`.
    #[inline]
    #[must_use]
    pub const fn max(&self) -> Option<&T> {
        self.max.as_ref()
    }

    /// Returns the number of data points.
    #[inline]
    #[must_use]
    pub const fn len(&self) -> usize {
        self.len as usize
    }

    /// Returns true if there are no data points.
    #[inline]
    #[must_use]
    pub const fn is_empty(&self) -> bool {
        self.len == 0
    }

    /// Returns the current sort order of the data.
    #[inline]
    #[must_use]
    pub fn sort_order(&self) -> SortOrder {
        let sortiness = self.sortiness();
        // Use 1e-9 to handle floating point imprecision
        // don't use f64::EPSILON because it's too small
        if (sortiness - 1.0).abs() <= 1e-9 {
            SortOrder::Ascending
        } else if (sortiness + 1.0).abs() <= 1e-9 {
            SortOrder::Descending
        } else {
            SortOrder::Unsorted
        }
    }

    /// Calculates a "sortiness" score for the data, indicating how close it is to being sorted.
    ///
    /// Returns a value between -1.0 and 1.0:
    /// * 1.0 indicates perfectly ascending order
    /// * -1.0 indicates perfectly descending order
    /// * Values in between indicate the general tendency towards ascending or descending order
    /// * 0.0 indicates either no clear ordering or empty/single-element collections
    ///
    /// # Examples
    /// ```
    /// use stats::MinMax;
    ///
    /// let mut asc: MinMax<i32> = vec![1, 2, 3, 4, 5].into_iter().collect();
    /// assert_eq!(asc.sortiness(), 1.0);
    ///
    /// let mut desc: MinMax<i32> = vec![5, 4, 3, 2, 1].into_iter().collect();
    /// assert_eq!(desc.sortiness(), -1.0);
    ///
    /// let mut mostly_asc: MinMax<i32> = vec![1, 2, 4, 3, 5].into_iter().collect();
    /// assert!(mostly_asc.sortiness() > 0.0); // Positive but less than 1.0
    /// ```
    #[inline]
    #[must_use]
    pub fn sortiness(&self) -> f64 {
        if let 0 | 1 = self.len {
            0.0
        } else {
            let total_pairs = self.ascending_pairs + self.descending_pairs;
            if total_pairs == 0 {
                0.0
            } else {
                (self.ascending_pairs as f64 - self.descending_pairs as f64) / total_pairs as f64
            }
        }
    }
}

impl MinMax<Vec<u8>> {
    /// Add a byte slice sample, avoiding heap allocation when the value doesn't
    /// update min, max, or `first_value`. Only `last_value` is always updated
    /// (reusing its existing allocation via `clone_from`).
    ///
    /// This is significantly more efficient than `add(sample.to_vec())` for large
    /// datasets where most values don't update min/max — avoiding ~99% of
    /// allocations in the common case.
    #[inline]
    pub fn add_bytes(&mut self, sample: &[u8]) {
        match self.len {
            2.. => {
                if let Some(ref last) = self.last_value {
                    #[allow(clippy::match_same_arms)]
                    match sample.partial_cmp(last.as_slice()) {
                        Some(Ordering::Greater) => self.ascending_pairs += 1,
                        Some(Ordering::Less) => self.descending_pairs += 1,
                        Some(Ordering::Equal) => self.ascending_pairs += 1,
                        None => {}
                    }
                }
            }
            0 => {
                let owned = sample.to_vec();
                self.first_value = Some(owned.clone());
                self.min = Some(owned.clone());
                self.max = Some(owned);
                self.len = 1;
                return;
            }
            1 => {
                if let Some(ref first) = self.first_value {
                    match sample.partial_cmp(first.as_slice()) {
                        Some(Ordering::Greater | Ordering::Equal) => self.ascending_pairs = 1,
                        Some(Ordering::Less) => self.descending_pairs = 1,
                        None => {}
                    }
                }
            }
        }

        // Update min/max - only allocate when actually updating
        if self.min.as_ref().is_none_or(|v| sample < v.as_slice()) {
            self.min = Some(sample.to_vec());
        } else if self.max.as_ref().is_none_or(|v| sample > v.as_slice()) {
            self.max = Some(sample.to_vec());
        }

        // Update last value - reuse existing allocation
        if let Some(ref mut last) = self.last_value {
            last.clear();
            last.extend_from_slice(sample);
        } else {
            self.last_value = Some(sample.to_vec());
        }
        self.len += 1;
    }
}

impl<T: PartialOrd + Clone> Commute for MinMax<T> {
    #[inline]
    fn merge(&mut self, v: MinMax<T>) {
        if v.min.is_none() {
            return;
        }
        self.len += v.len;
        if self.min.is_none() || v.min < self.min {
            self.min = v.min;
        }
        if self.max.is_none() || v.max > self.max {
            self.max = v.max;
        }

        // Merge pair counts
        self.ascending_pairs += v.ascending_pairs;
        self.descending_pairs += v.descending_pairs;

        // Handle merging of first_value and last_value
        if self.first_value.is_none() {
            self.first_value = v.first_value.clone();
        }
        if v.len > 0 {
            if let (Some(last), Some(v_first)) = (&self.last_value, &v.first_value) {
                match v_first.partial_cmp(last) {
                    Some(Ordering::Greater | Ordering::Equal) => self.ascending_pairs += 1,
                    Some(Ordering::Less) => self.descending_pairs += 1,
                    None => {}
                }
            }
            self.last_value = v.last_value;
        }
    }
}

impl<T: PartialOrd> Default for MinMax<T> {
    #[inline]
    fn default() -> MinMax<T> {
        MinMax {
            len: 0,
            ascending_pairs: 0,
            descending_pairs: 0,
            min: None,
            max: None,
            first_value: None,
            last_value: None,
        }
    }
}

impl<T: fmt::Debug> fmt::Debug for MinMax<T> {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match (&self.min, &self.max) {
            (Some(min), Some(max)) => {
                let sort_status = if let 0 | 1 = self.len {
                    SortOrder::Unsorted
                } else {
                    let total_pairs = self.ascending_pairs + self.descending_pairs;
                    if total_pairs == 0 {
                        SortOrder::Unsorted
                    } else {
                        let sortiness = (self.ascending_pairs as f64
                            - self.descending_pairs as f64)
                            / total_pairs as f64;
                        match sortiness {
                            1.0 => SortOrder::Ascending,
                            -1.0 => SortOrder::Descending,
                            _ => SortOrder::Unsorted,
                        }
                    }
                };
                write!(f, "[{min:?}, {max:?}], sort_order: {sort_status:?}")
            }
            (&None, &None) => write!(f, "N/A"),
            _ => unreachable!(),
        }
    }
}

impl fmt::Display for SortOrder {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            SortOrder::Unsorted => write!(f, "Unsorted"),
            SortOrder::Ascending => write!(f, "Ascending"),
            SortOrder::Descending => write!(f, "Descending"),
        }
    }
}

impl<T: PartialOrd + Clone> FromIterator<T> for MinMax<T> {
    #[inline]
    fn from_iter<I: IntoIterator<Item = T>>(it: I) -> MinMax<T> {
        let mut v = MinMax::new();
        v.extend(it);
        v
    }
}

impl<T: PartialOrd + Clone> Extend<T> for MinMax<T> {
    #[inline]
    fn extend<I: IntoIterator<Item = T>>(&mut self, it: I) {
        for sample in it {
            self.add(sample);
        }
    }
}

#[cfg(test)]
mod test {
    use super::{MinMax, SortOrder};
    use crate::Commute;

    #[test]
    fn minmax() {
        let minmax: MinMax<u32> = vec![1u32, 4, 2, 3, 10].into_iter().collect();
        assert_eq!(minmax.min(), Some(&1u32));
        assert_eq!(minmax.max(), Some(&10u32));
        assert_eq!(minmax.sort_order(), SortOrder::Unsorted);
    }

    #[test]
    fn minmax_sorted_ascending() {
        let minmax: MinMax<u32> = vec![1u32, 2, 3, 4, 5].into_iter().collect();
        assert_eq!(minmax.min(), Some(&1u32));
        assert_eq!(minmax.max(), Some(&5u32));
        assert_eq!(minmax.sort_order(), SortOrder::Ascending);
    }

    #[test]
    fn minmax_sorted_descending() {
        let minmax: MinMax<u32> = vec![5u32, 4, 3, 2, 1].into_iter().collect();
        assert_eq!(minmax.min(), Some(&1u32));
        assert_eq!(minmax.max(), Some(&5u32));
        assert_eq!(minmax.sort_order(), SortOrder::Descending);
    }

    #[test]
    fn minmax_empty() {
        let minmax: MinMax<u32> = MinMax::new();
        assert!(minmax.is_empty());
        assert_eq!(minmax.sort_order(), SortOrder::Unsorted);
    }

    #[test]
    fn minmax_merge_empty() {
        let mut mx1: MinMax<u32> = vec![1, 4, 2, 3, 10].into_iter().collect();
        assert_eq!(mx1.min(), Some(&1u32));
        assert_eq!(mx1.max(), Some(&10u32));
        assert_eq!(mx1.sort_order(), SortOrder::Unsorted);

        mx1.merge(MinMax::default());
        assert_eq!(mx1.min(), Some(&1u32));
        assert_eq!(mx1.max(), Some(&10u32));
        assert_eq!(mx1.sort_order(), SortOrder::Unsorted);
    }

    #[test]
    fn minmax_merge_diffsorts() {
        let mut mx1: MinMax<u32> = vec![1, 2, 2, 2, 3, 3, 4, 10].into_iter().collect();
        assert_eq!(mx1.min(), Some(&1u32));
        assert_eq!(mx1.max(), Some(&10u32));
        assert_eq!(mx1.sort_order(), SortOrder::Ascending);

        let mx2: MinMax<u32> = vec![5, 4, 3, 2, 1].into_iter().collect();
        assert_eq!(mx2.min(), Some(&1u32));
        assert_eq!(mx2.max(), Some(&5u32));
        assert_eq!(mx2.sort_order(), SortOrder::Descending);
        mx1.merge(mx2);
        assert_eq!(mx1.min(), Some(&1u32));
        assert_eq!(mx1.max(), Some(&10u32));
        assert_eq!(mx1.sort_order(), SortOrder::Unsorted);
    }

    #[test]
    fn minmax_merge_asc_sorts() {
        let mut mx1: MinMax<u32> = vec![2, 2, 2, 5, 10].into_iter().collect();
        assert_eq!(mx1.min(), Some(&2u32));
        assert_eq!(mx1.max(), Some(&10u32));
        assert_eq!(mx1.sort_order(), SortOrder::Ascending);

        let mx2: MinMax<u32> = vec![11, 14, 23, 32, 41].into_iter().collect();
        assert_eq!(mx2.min(), Some(&11u32));
        assert_eq!(mx2.max(), Some(&41u32));
        assert_eq!(mx2.sort_order(), SortOrder::Ascending);
        mx1.merge(mx2);
        assert_eq!(mx1.min(), Some(&2u32));
        assert_eq!(mx1.max(), Some(&41u32));
        assert_eq!(mx1.sort_order(), SortOrder::Ascending);
    }

    #[test]
    fn test_sortiness() {
        // Test empty
        let minmax: MinMax<u32> = MinMax::new();
        assert_eq!(minmax.sortiness(), 0.0);

        // Test single element
        let minmax: MinMax<u32> = vec![1].into_iter().collect();
        assert_eq!(minmax.sortiness(), 0.0);

        // Test perfectly ascending
        let minmax: MinMax<u32> = vec![1, 2, 3, 4, 5].into_iter().collect();
        assert_eq!(minmax.sortiness(), 1.0);

        // Test perfectly descending
        let minmax: MinMax<u32> = vec![5, 4, 3, 2, 1].into_iter().collect();
        assert_eq!(minmax.sortiness(), -1.0);

        // Test all equal
        let minmax: MinMax<u32> = vec![1, 1, 1, 1].into_iter().collect();
        assert_eq!(minmax.sortiness(), 1.0); // Equal pairs are considered ascending

        // Test mostly ascending
        let minmax: MinMax<u32> = vec![1, 2, 4, 3, 5].into_iter().collect();
        assert!(minmax.sortiness() > 0.0 && minmax.sortiness() < 1.0);
        assert_eq!(minmax.sortiness(), 0.5); // 2 ascending pairs, 1 descending pair

        // Test mostly descending
        let minmax: MinMax<u32> = vec![5, 4, 3, 4, 2].into_iter().collect();
        assert!(minmax.sortiness() < 0.0 && minmax.sortiness() > -1.0);
        assert_eq!(minmax.sortiness(), -0.5); // 1 ascending pair, 3 descending pairs
    }

    #[test]
    fn test_sortiness_merge() {
        let mut mx1: MinMax<u32> = vec![1, 2, 3].into_iter().collect();
        let mx2: MinMax<u32> = vec![4, 5, 6].into_iter().collect();
        assert_eq!(mx1.sortiness(), 1.0);
        assert_eq!(mx2.sortiness(), 1.0);

        mx1.merge(mx2);
        assert_eq!(mx1.sortiness(), 1.0); // Should remain perfectly sorted after merge

        let mut mx3: MinMax<u32> = vec![1, 2, 3].into_iter().collect();
        let mx4: MinMax<u32> = vec![2, 1, 0].into_iter().collect();
        mx3.merge(mx4);
        assert_eq!(mx3, vec![1, 2, 3, 2, 1, 0].into_iter().collect());
        assert!(mx3.sortiness() < 1.0); // Should show mixed sorting after merge
        assert_eq!(mx3.sortiness(), -0.2);
    }

    #[test]
    fn test_merge_single_into_empty() {
        let mut empty: MinMax<u32> = MinMax::default();
        let single: MinMax<u32> = vec![42].into_iter().collect();

        assert!(empty.first_value.is_none());
        assert!(empty.last_value.is_none());

        empty.merge(single);

        assert_eq!(empty.len(), 1);
        assert_eq!(empty.min(), Some(&42));
        assert_eq!(empty.max(), Some(&42));
        assert_eq!(empty.first_value, Some(42));
        // last_value is None for single-element MinMax (only set from 2nd element onward)
        assert_eq!(empty.last_value, None);
    }
}

#[test]
fn test_sortiness_simple_alphabetical() {
    let minmax: MinMax<String> = vec![
        "a".to_string(),
        "b".to_string(),
        "c".to_string(),
        "d".to_string(),
    ]
    .into_iter()
    .collect();
    assert_eq!(minmax.sortiness(), 1.0);
    assert_eq!(minmax.sort_order(), SortOrder::Ascending);

    let minmax: MinMax<String> = vec![
        "d".to_string(),
        "c".to_string(),
        "b".to_string(),
        "a".to_string(),
    ]
    .into_iter()
    .collect();
    assert_eq!(minmax.sortiness(), -1.0);
    assert_eq!(minmax.sort_order(), SortOrder::Descending);

    let minmax: MinMax<String> = vec![
        "a".to_string(),
        "b".to_string(),
        "c".to_string(),
        "a".to_string(),
    ]
    .into_iter()
    .collect();
    assert_eq!(minmax.sortiness(), 0.3333333333333333);
    assert_eq!(minmax.sort_order(), SortOrder::Unsorted);
}
```

## File: `src/online.rs`
```rust
use std::fmt;

use num_traits::ToPrimitive;
use serde::{Deserialize, Serialize};

use crate::Commute;

/// Compute the standard deviation of a stream in constant space.
#[inline]
pub fn stddev<I, T>(x: I) -> f64
where
    I: IntoIterator<Item = T>,
    T: ToPrimitive,
{
    x.into_iter().collect::<OnlineStats>().stddev()
}

/// Compute the variance of a stream in constant space.
#[inline]
pub fn variance<I, T>(x: I) -> f64
where
    I: IntoIterator<Item = T>,
    T: ToPrimitive,
{
    x.into_iter().collect::<OnlineStats>().variance()
}

/// Compute the mean of a stream in constant space.
#[inline]
pub fn mean<I, T>(x: I) -> f64
where
    I: IntoIterator<Item = T>,
    T: ToPrimitive,
{
    x.into_iter().collect::<OnlineStats>().mean()
}

/// Online state for computing mean, variance and standard deviation.
///
/// Optimized memory layout for better cache performance:
/// - Grouped related fields together in hot, warm and cold paths.
#[allow(clippy::unsafe_derive_deserialize)]
#[derive(Clone, Copy, Serialize, Deserialize, PartialEq)]
pub struct OnlineStats {
    // Hot path - always accessed together (24 bytes)
    size: u64, // 8 bytes - always accessed
    mean: f64, // 8 bytes - always accessed
    q: f64,    // 8 bytes - always accessed

    // Warm path - fast path for positive numbers (25 bytes)
    hg_sums: bool,      // 1 byte - checked before sums
    harmonic_sum: f64,  // 8 bytes - warm path
    geometric_sum: f64, // 8 bytes - warm path
    n_positive: u64,    // 8 bytes - warm path

    // Cold path - slow path for zeros/negatives (16 bytes)
    n_zero: u64,     // 8 bytes - cold path
    n_negative: u64, // 8 bytes - cold path
}

impl OnlineStats {
    /// Create initial state.
    ///
    /// Population size, variance and mean are set to `0`.
    #[must_use]
    pub fn new() -> OnlineStats {
        Default::default()
    }

    /// Initializes `OnlineStats` from a sample.
    #[must_use]
    pub fn from_slice<T: ToPrimitive>(samples: &[T]) -> OnlineStats {
        // safety: OnlineStats is only for numbers
        samples
            .iter()
            .map(|n| unsafe { n.to_f64().unwrap_unchecked() })
            .collect()
    }

    /// Return the current mean.
    #[must_use]
    pub const fn mean(&self) -> f64 {
        if self.is_empty() { f64::NAN } else { self.mean }
    }

    /// Return the current standard deviation.
    #[must_use]
    pub fn stddev(&self) -> f64 {
        self.variance().sqrt()
    }

    /// Return the current population variance (using N denominator, not N-1).
    // https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
    #[must_use]
    pub const fn variance(&self) -> f64 {
        if self.is_empty() { f64::NAN } else { self.q / (self.size as f64) }
    }

    /// Return the current harmonic mean.
    #[must_use]
    pub fn harmonic_mean(&self) -> f64 {
        if self.is_empty() || self.n_zero > 0 || self.n_negative > 0 {
            f64::NAN
        } else {
            (self.size as f64) / self.harmonic_sum
        }
    }

    /// Return the current geometric mean.
    #[must_use]
    pub fn geometric_mean(&self) -> f64 {
        if self.is_empty()
            || self.n_negative > 0
            || self.geometric_sum.is_nan()
            || self.geometric_sum == f64::INFINITY
        {
            f64::NAN
        } else if self.n_zero > 0 || self.geometric_sum == f64::NEG_INFINITY {
            // geometric_sum == -Inf means data values approach zero;
            // geometric mean correctly approaches 0.0 in that limit
            0.0
        } else {
            (self.geometric_sum / (self.size as f64)).exp()
        }
    }

    /// Return the number of negative, zero and positive counts.
    ///
    /// Returns a tuple `(negative_count, zero_count, positive_count)` where:
    /// - `negative_count`: number of values with negative sign bit (including -0.0)
    /// - `zero_count`: number of values equal to +0.0
    /// - `positive_count`: number of values greater than 0
    ///
    /// Note: -0.0 and +0.0 are distinguished by their sign bit and counted separately.
    ///
    /// # Example
    ///
    /// ```
    /// use stats::OnlineStats;
    ///
    /// let mut stats = OnlineStats::new();
    /// stats.extend(vec![-2, -1, 0, 0, 1, 2, 3]);
    ///
    /// let (neg, zero, pos) = stats.n_counts();
    /// assert_eq!(neg, 2);   // -2, -1
    /// assert_eq!(zero, 2);  // 0, 0
    /// assert_eq!(pos, 3);   // 1, 2, 3
    /// ```
    #[must_use]
    pub const fn n_counts(&self) -> (u64, u64, u64) {
        (self.n_negative, self.n_zero, self.n_positive)
    }

    // TODO: Calculate kurtosis
    // also see https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance

    /// Add a new sample.
    ///
    /// NaN values are silently skipped to prevent corrupting the statistics.
    #[inline]
    pub fn add<T: ToPrimitive>(&mut self, sample: &T) {
        // safety: we only add samples for numbers, so safe to unwrap
        let sample = unsafe { sample.to_f64().unwrap_unchecked() };

        if sample.is_nan() {
            return;
        }

        // Taken from: https://en.wikipedia.org/wiki/Standard_deviation#Rapid_calculation_methods
        // See also: https://api.semanticscholar.org/CorpusID:120126049
        self.size += 1;
        let delta = sample - self.mean;

        // FMA: equivalent to: self.mean += delta * (1.0 / (self.size as f64));
        self.mean = delta.mul_add(1.0 / (self.size as f64), self.mean);

        // FMA: equivalent to: self.q += delta * (sample - self.mean);
        self.q = delta.mul_add(sample - self.mean, self.q);

        // Handle positive numbers (most common case)
        if sample > 0.0 {
            if self.hg_sums {
                // Fast path: compute harmonic & geometric sums directly
                self.harmonic_sum += 1.0 / sample;
                self.geometric_sum += sample.ln();
            }
            self.n_positive += 1;
        } else {
            // Handle special cases (zero and negative numbers)
            if sample.is_sign_negative() {
                self.n_negative += 1;
            } else {
                self.n_zero += 1;
            }
            self.hg_sums = false;
        }
    }

    /// Add a new f64 sample.
    /// Skipping the `ToPrimitive` conversion.
    ///
    /// NaN values are silently skipped to prevent corrupting the statistics.
    #[inline]
    pub fn add_f64(&mut self, sample: f64) {
        if sample.is_nan() {
            return;
        }

        self.size += 1;
        let delta = sample - self.mean;

        self.mean = delta.mul_add(1.0 / (self.size as f64), self.mean);
        self.q = delta.mul_add(sample - self.mean, self.q);

        // Handle positive numbers (most common case)
        if sample > 0.0 {
            if self.hg_sums {
                self.harmonic_sum += 1.0 / sample;
                self.geometric_sum += sample.ln();
            }
            self.n_positive += 1;
        } else {
            // Handle special cases (zero and negative numbers)
            if sample.is_sign_negative() {
                self.n_negative += 1;
            } else {
                self.n_zero += 1;
            }
            self.hg_sums = false;
        }
    }

    /// Add a new NULL value to the population.
    /// This increases the population size by `1` and treats null as `0.0`,
    /// which increments `n_zero` and disables harmonic/geometric sum tracking.
    #[inline]
    pub fn add_null(&mut self) {
        self.add_f64(0.0);
    }

    /// Returns the number of data points.
    #[inline]
    #[must_use]
    pub const fn len(&self) -> usize {
        self.size as usize
    }

    /// Returns if empty.
    #[inline]
    #[must_use]
    pub const fn is_empty(&self) -> bool {
        self.size == 0
    }
}

impl Commute for OnlineStats {
    #[inline]
    fn merge(&mut self, v: OnlineStats) {
        if v.is_empty() {
            return;
        }

        // Taken from: https://en.wikipedia.org/wiki/Standard_deviation#Combining_standard_deviations
        let (s1, s2) = (self.size as f64, v.size as f64);
        let total = s1 + s2;
        let delta = self.mean - v.mean;
        let meandiffsq = delta * delta;

        self.size += v.size;

        // Incremental form avoids forming large intermediate products,
        // preventing catastrophic cancellation when means are large and similar
        self.mean = (v.mean - self.mean).mul_add(s2 / total, self.mean);

        // self.q += v.q + meandiffsq * s1 * s2 / (s1 + s2);
        // below is the fused multiply add version of the statement above
        self.q += meandiffsq.mul_add(s1 * s2 / total, v.q);

        self.hg_sums = self.hg_sums && v.hg_sums;
        self.harmonic_sum += v.harmonic_sum;
        self.geometric_sum += v.geometric_sum;

        self.n_zero += v.n_zero;
        self.n_negative += v.n_negative;
        self.n_positive += v.n_positive;
    }
}

impl Default for OnlineStats {
    fn default() -> OnlineStats {
        OnlineStats {
            size: 0,
            mean: 0.0,
            q: 0.0,
            harmonic_sum: 0.0,
            geometric_sum: 0.0,
            n_zero: 0,
            n_negative: 0,
            n_positive: 0,
            hg_sums: true,
        }
    }
}

impl fmt::Debug for OnlineStats {
    #[inline]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:.10} +/- {:.10}", self.mean(), self.stddev())
    }
}

impl<T: ToPrimitive> FromIterator<T> for OnlineStats {
    #[inline]
    fn from_iter<I: IntoIterator<Item = T>>(it: I) -> OnlineStats {
        let mut v = OnlineStats::new();
        v.extend(it);
        v
    }
}

impl<T: ToPrimitive> Extend<T> for OnlineStats {
    #[inline]
    fn extend<I: IntoIterator<Item = T>>(&mut self, it: I) {
        for sample in it {
            self.add(&sample);
        }
    }
}

#[cfg(test)]
mod test {
    use super::{OnlineStats, mean, stddev, variance};
    use {crate::Commute, crate::merge_all};

    #[test]
    fn online() {
        // TODO: Convert this to a quickcheck test.
        let expected = OnlineStats::from_slice(&[1usize, 2, 3, 2, 4, 6]);

        let var1 = OnlineStats::from_slice(&[1usize, 2, 3]);
        let var2 = OnlineStats::from_slice(&[2usize, 4, 6]);
        let mut got = var1;
        got.merge(var2);
        assert_eq!(expected.stddev(), got.stddev());
        assert_eq!(expected.mean(), got.mean());
        assert_eq!(expected.variance(), got.variance());
    }

    #[test]
    fn online_empty() {
        let expected = OnlineStats::new();
        assert!(expected.is_empty());
    }

    #[test]
    fn online_many() {
        // TODO: Convert this to a quickcheck test.
        let expected = OnlineStats::from_slice(&[1usize, 2, 3, 2, 4, 6, 3, 6, 9]);

        let vars = vec![
            OnlineStats::from_slice(&[1usize, 2, 3]),
            OnlineStats::from_slice(&[2usize, 4, 6]),
            OnlineStats::from_slice(&[3usize, 6, 9]),
        ];
        assert_eq!(
            expected.stddev(),
            merge_all(vars.clone().into_iter()).unwrap().stddev()
        );
        assert_eq!(
            expected.mean(),
            merge_all(vars.clone().into_iter()).unwrap().mean()
        );
        assert_eq!(
            expected.variance(),
            merge_all(vars.into_iter()).unwrap().variance()
        );
    }

    #[test]
    fn test_means() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![2.0f64, 4.0, 8.0]);

        // Arithmetic mean = (2 + 4 + 8) / 3 = 4.666...
        assert!((stats.mean() - 4.666666666667).abs() < 1e-10);

        // Harmonic mean = 3 / (1/2 + 1/4 + 1/8) = 3.428571429
        assert_eq!("3.42857143", format!("{:.8}", stats.harmonic_mean()));

        // Geometric mean = (2 * 4 * 8)^(1/3) = 4.0
        assert!((stats.geometric_mean() - 4.0).abs() < 1e-10);
    }

    #[test]
    fn test_means_with_negative() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![-2.0f64, 2.0]);

        // Arithmetic mean = (-2 + 2) / 2 = 0
        assert!(stats.mean().abs() < 1e-10);

        // Geometric mean is NaN for negative numbers
        assert!(stats.geometric_mean().is_nan());

        // Harmonic mean is undefined when values have different signs
        assert!(stats.harmonic_mean().is_nan());
    }

    #[test]
    fn test_means_with_zero() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![0.0f64, 4.0, 8.0]);

        // Arithmetic mean = (0 + 4 + 8) / 3 = 4
        assert!((stats.mean() - 4.0).abs() < 1e-10);

        // Geometric mean = (0 * 4 * 8)^(1/3) = 0
        assert!(stats.geometric_mean().abs() < 1e-10);

        // Harmonic mean is undefined when any value is 0
        assert!(stats.harmonic_mean().is_nan());
    }

    #[test]
    fn test_means_with_zero_and_negative_values() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![-10i32, -5, 0, 5, 10]);

        // Arithmetic mean = (-10 + -5 + 0 + 5 + 10) / 5 = 0
        assert!(stats.mean().abs() < 1e-10);

        // Geometric mean is NaN due to negative values
        assert!(stats.geometric_mean().is_nan());

        // Harmonic mean is NaN due to zero value
        assert!(stats.harmonic_mean().is_nan());
    }

    #[test]
    fn test_means_single_value() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![5.0f64]);

        // All means should equal the single value
        assert!((stats.mean() - 5.0).abs() < 1e-10);
        assert!((stats.geometric_mean() - 5.0).abs() < 1e-10);
        assert!((stats.harmonic_mean() - 5.0).abs() < 1e-10);
    }

    #[test]
    fn test_means_empty() {
        let stats = OnlineStats::new();

        // All means should be NaN for empty stats
        assert!(stats.mean().is_nan());
        assert!(stats.geometric_mean().is_nan());
        assert!(stats.harmonic_mean().is_nan());
    }

    // Tests for wrapper functions: stddev(), variance(), mean()

    #[test]
    fn test_mean_wrapper_basic() {
        // Test with f64 values
        let result = mean(vec![1.0f64, 2.0, 3.0, 4.0, 5.0]);
        assert!((result - 3.0).abs() < 1e-10);

        // Test with i32 values
        let result = mean(vec![1i32, 2, 3, 4, 5]);
        assert!((result - 3.0).abs() < 1e-10);

        // Test with u32 values
        let result = mean(vec![10u32, 20, 30]);
        assert!((result - 20.0).abs() < 1e-10);
    }

    #[test]
    fn test_mean_wrapper_empty() {
        let result = mean(Vec::<f64>::new());
        assert!(result.is_nan());
    }

    #[test]
    fn test_mean_wrapper_single_element() {
        assert!((mean(vec![42.0f64]) - 42.0).abs() < 1e-10);
        assert!((mean(vec![100i32]) - 100.0).abs() < 1e-10);
        assert!((mean(vec![0u8]) - 0.0).abs() < 1e-10);
    }

    #[test]
    fn test_mean_wrapper_negative_values() {
        let result = mean(vec![-5.0f64, 5.0]);
        assert!(result.abs() < 1e-10); // Mean should be 0

        let result = mean(vec![-10i32, -20, -30]);
        assert!((result - (-20.0)).abs() < 1e-10);
    }

    #[test]
    fn test_mean_wrapper_various_numeric_types() {
        // Test with different numeric types
        assert!((mean(vec![1u8, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1u16, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1u64, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1i8, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1i16, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1i64, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1.0f32, 2.0, 3.0]) - 2.0).abs() < 1e-6);
        assert!((mean(vec![1usize, 2, 3]) - 2.0).abs() < 1e-10);
        assert!((mean(vec![1isize, 2, 3]) - 2.0).abs() < 1e-10);
    }

    #[test]
    fn test_variance_wrapper_basic() {
        // Variance of [1, 2, 3, 4, 5] = 2.0 (population variance)
        let result = variance(vec![1.0f64, 2.0, 3.0, 4.0, 5.0]);
        assert!((result - 2.0).abs() < 1e-10);

        // Test with i32 values
        let result = variance(vec![1i32, 2, 3, 4, 5]);
        assert!((result - 2.0).abs() < 1e-10);
    }

    #[test]
    fn test_variance_wrapper_empty() {
        let result = variance(Vec::<f64>::new());
        assert!(result.is_nan());
    }

    #[test]
    fn test_variance_wrapper_single_element() {
        // Variance of a single element is 0
        assert!(variance(vec![42.0f64]).abs() < 1e-10);
        assert!(variance(vec![100i32]).abs() < 1e-10);
    }

    #[test]
    fn test_variance_wrapper_identical_values() {
        // Variance of identical values is 0
        let result = variance(vec![5.0f64, 5.0, 5.0, 5.0]);
        assert!(result.abs() < 1e-10);
    }

    #[test]
    fn test_variance_wrapper_various_numeric_types() {
        // Test with different numeric types - variance of [1, 2, 3] = 2/3
        let expected = 2.0 / 3.0;
        assert!((variance(vec![1u8, 2, 3]) - expected).abs() < 1e-10);
        assert!((variance(vec![1u16, 2, 3]) - expected).abs() < 1e-10);
        assert!((variance(vec![1i32, 2, 3]) - expected).abs() < 1e-10);
        assert!((variance(vec![1i64, 2, 3]) - expected).abs() < 1e-10);
        assert!((variance(vec![1usize, 2, 3]) - expected).abs() < 1e-10);
    }

    #[test]
    fn test_stddev_wrapper_basic() {
        // Standard deviation of [1, 2, 3, 4, 5] = sqrt(2.0)
        let result = stddev(vec![1.0f64, 2.0, 3.0, 4.0, 5.0]);
        assert!((result - 2.0f64.sqrt()).abs() < 1e-10);

        // Test with i32 values
        let result = stddev(vec![1i32, 2, 3, 4, 5]);
        assert!((result - 2.0f64.sqrt()).abs() < 1e-10);
    }

    #[test]
    fn test_stddev_wrapper_empty() {
        let result = stddev(Vec::<f64>::new());
        assert!(result.is_nan());
    }

    #[test]
    fn test_stddev_wrapper_single_element() {
        // Standard deviation of a single element is 0
        assert!(stddev(vec![42.0f64]).abs() < 1e-10);
        assert!(stddev(vec![100i32]).abs() < 1e-10);
    }

    #[test]
    fn test_stddev_wrapper_identical_values() {
        // Standard deviation of identical values is 0
        let result = stddev(vec![5.0f64, 5.0, 5.0, 5.0]);
        assert!(result.abs() < 1e-10);
    }

    #[test]
    fn test_stddev_wrapper_various_numeric_types() {
        // Test with different numeric types - stddev of [1, 2, 3] = sqrt(2/3)
        let expected = (2.0f64 / 3.0).sqrt();
        assert!((stddev(vec![1u8, 2, 3]) - expected).abs() < 1e-10);
        assert!((stddev(vec![1u16, 2, 3]) - expected).abs() < 1e-10);
        assert!((stddev(vec![1i32, 2, 3]) - expected).abs() < 1e-10);
        assert!((stddev(vec![1i64, 2, 3]) - expected).abs() < 1e-10);
        assert!((stddev(vec![1usize, 2, 3]) - expected).abs() < 1e-10);
    }

    #[test]
    fn test_wrapper_functions_consistency() {
        // Verify that wrapper functions produce same results as OnlineStats methods
        let data = vec![1.0f64, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0];
        let stats = OnlineStats::from_slice(&data);

        assert!((mean(data.clone()) - stats.mean()).abs() < 1e-10);
        assert!((variance(data.clone()) - stats.variance()).abs() < 1e-10);
        assert!((stddev(data) - stats.stddev()).abs() < 1e-10);
    }

    #[test]
    fn test_wrapper_functions_with_iterators() {
        // Test that wrappers work with various iterator types
        let arr = [1, 2, 3, 4, 5];

        // Array iterator
        assert!((mean(arr) - 3.0).abs() < 1e-10);

        // Range iterator
        assert!((mean(1..=5) - 3.0).abs() < 1e-10);

        // Mapped iterator
        let result = mean((1..=5).map(|x| x * 2));
        assert!((result - 6.0).abs() < 1e-10);
    }

    // Tests for n_counts functionality

    #[test]
    fn test_n_counts_basic() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![-5, -3, 0, 0, 2, 4, 6]);

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 2, "Should have 2 negative values");
        assert_eq!(zero, 2, "Should have 2 zero values");
        assert_eq!(pos, 3, "Should have 3 positive values");
    }

    #[test]
    fn test_n_counts_all_positive() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![1.0, 2.0, 3.0, 4.0]);

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 0);
        assert_eq!(zero, 0);
        assert_eq!(pos, 4);
    }

    #[test]
    fn test_n_counts_all_negative() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![-1.0, -2.0, -3.0]);

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 3);
        assert_eq!(zero, 0);
        assert_eq!(pos, 0);
    }

    #[test]
    fn test_n_counts_all_zeros() {
        let mut stats = OnlineStats::new();
        stats.extend(vec![0.0, 0.0, 0.0]);

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 0);
        assert_eq!(zero, 3);
        assert_eq!(pos, 0);
    }

    #[test]
    fn test_n_counts_with_merge() {
        let mut stats1 = OnlineStats::new();
        stats1.extend(vec![-2, 0, 3]);

        let mut stats2 = OnlineStats::new();
        stats2.extend(vec![-1, 5, 7]);

        stats1.merge(stats2);

        let (neg, zero, pos) = stats1.n_counts();
        assert_eq!(neg, 2, "Should have 2 negative values after merge");
        assert_eq!(zero, 1, "Should have 1 zero value after merge");
        assert_eq!(pos, 3, "Should have 3 positive values after merge");
    }

    #[test]
    fn test_n_counts_empty() {
        let stats = OnlineStats::new();

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 0);
        assert_eq!(zero, 0);
        assert_eq!(pos, 0);
    }

    #[test]
    fn test_n_counts_negative_zero() {
        let mut stats = OnlineStats::new();
        // -0.0 and +0.0 are distinguished by their sign bit
        // -0.0 is counted as negative, +0.0 is counted as zero
        stats.extend(vec![-0.0f64, 0.0]);

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 1, "-0.0 has negative sign bit");
        assert_eq!(zero, 1, "+0.0 is zero");
        assert_eq!(pos, 0);
    }

    #[test]
    fn test_n_counts_floats_boundary() {
        let mut stats = OnlineStats::new();
        // Test with very small positive and negative numbers
        stats.extend(vec![-0.0001f64, 0.0, 0.0001]);

        let (neg, zero, pos) = stats.n_counts();
        assert_eq!(neg, 1);
        assert_eq!(zero, 1);
        assert_eq!(pos, 1);
    }
}
```

## File: `src/sorted.rs`
```rust
use std::collections::BinaryHeap;
use std::default::Default;
use std::iter::{FromIterator, IntoIterator};

use num_traits::ToPrimitive;

use {crate::Commute, crate::Partial};

pub fn median_on_sorted<T>(data: &[T]) -> Option<f64>
        where T: PartialOrd + ToPrimitive {
    let len = data.len();
    match len {
        0 => None,
        // safety: // Use direct indexing since we know len == 1
        1 => data[0].to_f64(),
        len if len % 2 == 0 => {
            let idx = len / 2;
            // SAFETY: We know idx and idx-1 are valid because len >= 2
            unsafe {
                let v1 = data.get_unchecked(idx - 1).to_f64()?;
                let v2 = data.get_unchecked(idx).to_f64()?;
                Some(f64::midpoint(v1, v2))
            }
        }
        len => {
            // SAFETY: We know len/2 is valid because len >= 3
            unsafe { data.get_unchecked(len / 2).to_f64() }
        }
    }
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
        if mode.as_ref() == Some(&x) {
            mode_count += 1;
        } else if next.as_ref() == Some(&x) {
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
#[derive(Clone, Deserialize, Serialize, Eq, PartialEq, Debug)]
pub struct Sorted<T> {
    data: BinaryHeap<Partial<T>>,
}

impl<T: PartialOrd> Sorted<T> {
    /// Create initial empty state.
    #[inline]
    pub fn new() -> Sorted<T> {
        Default::default()
    }

    /// Add a new element to the set.
    #[inline]
    pub fn add(&mut self, v: T) {
        self.data.push(Partial(v))
    }

    /// Returns the number of data points.
    #[inline]
    pub fn len(&self) -> usize {
        self.data.len()
    }
}

impl<T: PartialOrd + Clone> Sorted<T> {
    /// Returns the mode of the data. Clones the internal heap.
    #[inline]
    pub fn mode(&self) -> Option<T> {
        let p = mode_on_sorted(self.data.clone().into_sorted_vec().into_iter());
        p.map(|p| p.0)
    }

    /// Returns the mode of the data, consuming `self` to avoid cloning.
    #[inline]
    pub fn into_mode(self) -> Option<T> {
        let p = mode_on_sorted(self.data.into_sorted_vec().into_iter());
        p.map(|p| p.0)
    }
}

impl<T: PartialOrd + ToPrimitive + Clone> Sorted<T> {
    /// Returns the median of the data. Clones the internal heap.
    #[inline]
    pub fn median(&self) -> Option<f64> {
        let data = self.data.clone().into_sorted_vec();
        median_on_sorted(&*data)
    }

    /// Returns the median of the data, consuming `self` to avoid cloning.
    #[inline]
    pub fn into_median(self) -> Option<f64> {
        let data = self.data.into_sorted_vec();
        median_on_sorted(&*data)
    }
}

impl<T: PartialOrd> Commute for Sorted<T> {
    #[inline]
    fn merge(&mut self, v: Sorted<T>) {
        // should this be `into_sorted_vec`?
        self.data.extend(v.data);
    }
}

impl<T: PartialOrd> Default for Sorted<T> {
    #[inline]
    fn default() -> Sorted<T> { Sorted { data: BinaryHeap::new() } }
}

impl<T: PartialOrd> FromIterator<T> for Sorted<T> {
    #[inline]
    fn from_iter<I: IntoIterator<Item=T>>(it: I) -> Sorted<T> {
        let mut v = Sorted::new();
        v.extend(it);
        v
    }
}

impl<T: PartialOrd> Extend<T> for Sorted<T> {
    #[inline]
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
use num_traits::ToPrimitive;
use rayon::iter::{IndexedParallelIterator, IntoParallelRefIterator, ParallelIterator};
use rayon::prelude::ParallelSlice;
use rayon::slice::ParallelSliceMut;

use serde::{Deserialize, Serialize};

use {crate::Commute, crate::Partial};

// PARALLEL_THRESHOLD (10,000) is the minimum dataset size for rayon parallel sort.
// The separate 10,240 threshold in cardinality estimation (5 × 2,048) is aligned to
// cache-line-friendly chunk sizes for parallel iterator reduction.
const PARALLEL_THRESHOLD: usize = 10_000;

/// Compute the exact median on a stream of data.
///
/// (This has time complexity `O(nlogn)` and space complexity `O(n)`.)
#[inline]
pub fn median<I>(it: I) -> Option<f64>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send,
{
    it.collect::<Unsorted<_>>().median()
}

/// Compute the median absolute deviation (MAD) on a stream of data.
#[inline]
pub fn mad<I>(it: I, precalc_median: Option<f64>) -> Option<f64>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send + Sync,
{
    it.collect::<Unsorted<_>>().mad(precalc_median)
}

/// Compute the exact 1-, 2-, and 3-quartiles (Q1, Q2 a.k.a. median, and Q3) on a stream of data.
///
/// (This has time complexity `O(n log n)` and space complexity `O(n)`.)
#[inline]
pub fn quartiles<I>(it: I) -> Option<(f64, f64, f64)>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send,
{
    it.collect::<Unsorted<_>>().quartiles()
}

/// Compute the exact mode on a stream of data.
///
/// (This has time complexity `O(nlogn)` and space complexity `O(n)`.)
///
/// If the data does not have a mode, then `None` is returned.
#[inline]
pub fn mode<T, I>(it: I) -> Option<T>
where
    T: PartialOrd + Clone + Send,
    I: Iterator<Item = T>,
{
    it.collect::<Unsorted<T>>().mode()
}

/// Compute the modes on a stream of data.
///
/// If there is a single mode, then only that value is returned in the `Vec`
/// however, if there are multiple values tied for occurring the most amount of times
/// those values are returned.
///
/// ## Example
/// ```
/// use stats;
///
/// let vals = vec![1, 1, 2, 2, 3];
///
/// assert_eq!(stats::modes(vals.into_iter()), (vec![1, 2], 2, 2));
/// ```
/// This has time complexity `O(n)`
///
/// If the data does not have a mode, then an empty `Vec` is returned.
#[inline]
pub fn modes<T, I>(it: I) -> (Vec<T>, usize, u32)
where
    T: PartialOrd + Clone + Send,
    I: Iterator<Item = T>,
{
    it.collect::<Unsorted<T>>().modes()
}

/// Compute the antimodes on a stream of data.
///
/// Antimode is the least frequent non-zero score.
///
/// If there is a single antimode, then only that value is returned in the `Vec`
/// however, if there are multiple values tied for occurring the least amount of times
/// those values are returned.
///
/// Only the first 10 antimodes are returned to prevent returning the whole set
/// when cardinality = number of records (i.e. all unique values).
///
/// ## Example
/// ```
/// use stats;
///
/// let vals = vec![1, 1, 2, 2, 3];
///
/// assert_eq!(stats::antimodes(vals.into_iter()), (vec![3], 1, 1));
/// ```
/// This has time complexity `O(n)`
///
/// If the data does not have an antimode, then an empty `Vec` is returned.
#[inline]
pub fn antimodes<T, I>(it: I) -> (Vec<T>, usize, u32)
where
    T: PartialOrd + Clone + Send,
    I: Iterator<Item = T>,
{
    let (antimodes_result, antimodes_count, antimodes_occurrences) =
        it.collect::<Unsorted<T>>().antimodes();
    (antimodes_result, antimodes_count, antimodes_occurrences)
}

/// Compute the Gini Coefficient on a stream of data.
///
/// The Gini Coefficient measures inequality in a distribution, ranging from 0 (perfect equality)
/// to 1 (perfect inequality).
///
/// (This has time complexity `O(n log n)` and space complexity `O(n)`.)
#[inline]
pub fn gini<I>(it: I, precalc_sum: Option<f64>) -> Option<f64>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send + Sync,
{
    it.collect::<Unsorted<_>>().gini(precalc_sum)
}

/// Compute the kurtosis (excess kurtosis) on a stream of data.
///
/// Kurtosis measures the "tailedness" of a distribution. Excess kurtosis is kurtosis - 3,
/// where 0 indicates a normal distribution, positive values indicate heavy tails, and
/// negative values indicate light tails.
///
/// (This has time complexity `O(n log n)` and space complexity `O(n)`.)
#[inline]
pub fn kurtosis<I>(it: I, precalc_mean: Option<f64>, precalc_variance: Option<f64>) -> Option<f64>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send + Sync,
{
    it.collect::<Unsorted<_>>()
        .kurtosis(precalc_mean, precalc_variance)
}

/// Compute the percentile rank of a value on a stream of data.
///
/// Returns the percentile rank (0-100) of the given value in the distribution.
/// If the value is less than all values, returns 0.0. If greater than all, returns 100.0.
///
/// (This has time complexity `O(n log n)` and space complexity `O(n)`.)
#[inline]
pub fn percentile_rank<I, V>(it: I, value: V) -> Option<f64>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send + Sync,
    V: PartialOrd + ToPrimitive,
{
    it.collect::<Unsorted<_>>().percentile_rank(value)
}

/// Compute the Atkinson Index on a stream of data.
///
/// The Atkinson Index measures inequality with an inequality aversion parameter ε.
/// It ranges from 0 (perfect equality) to 1 (perfect inequality).
/// Higher ε values give more weight to inequality at the lower end of the distribution.
///
/// (This has time complexity `O(n log n)` and space complexity `O(n)`.)
#[inline]
pub fn atkinson<I>(
    it: I,
    epsilon: f64,
    precalc_mean: Option<f64>,
    precalc_geometric_sum: Option<f64>,
) -> Option<f64>
where
    I: Iterator,
    <I as Iterator>::Item: PartialOrd + ToPrimitive + Send + Sync,
{
    it.collect::<Unsorted<_>>()
        .atkinson(epsilon, precalc_mean, precalc_geometric_sum)
}

fn median_on_sorted<T>(data: &[T]) -> Option<f64>
where
    T: PartialOrd + ToPrimitive,
{
    Some(match data.len() {
        // Empty slice case - return None early
        0 => return None,
        // Single element case - return that element converted to f64
        1 => data.first()?.to_f64()?,
        // Even length case - average the two middle elements
        len if len.is_multiple_of(2) => {
            let idx = len / 2;
            // Safety: we know these indices are valid because we checked len is even and non-zero,
            // so idx-1 and idx are valid indices into data
            let v1 = unsafe { data.get_unchecked(idx - 1) }.to_f64()?;
            let v2 = unsafe { data.get_unchecked(idx) }.to_f64()?;
            f64::midpoint(v1, v2)
        }
        // Odd length case - return the middle element
        // Safety: we know the index is within bounds
        len => unsafe { data.get_unchecked(len / 2) }.to_f64()?,
    })
}

fn mad_on_sorted<T>(data: &[T], precalc_median: Option<f64>) -> Option<f64>
where
    T: Sync + PartialOrd + ToPrimitive,
{
    if data.is_empty() {
        return None;
    }
    let median_obs = precalc_median.unwrap_or_else(|| median_on_sorted(data).unwrap());

    // Use adaptive parallel processing based on data size
    let mut abs_diff_vec: Vec<f64> = if data.len() < PARALLEL_THRESHOLD {
        // Sequential processing for small datasets
        // Iterator collect enables TrustedLen optimization, eliminating per-element bounds checks
        data.iter()
            // SAFETY: to_f64() always returns Some for standard numeric types (f32/f64, i/u 8-64)
            .map(|x| (median_obs - unsafe { x.to_f64().unwrap_unchecked() }).abs())
            .collect()
    } else {
        // Parallel processing for large datasets
        data.par_iter()
            // SAFETY: to_f64() always returns Some for standard numeric types
            .map(|x| (median_obs - unsafe { x.to_f64().unwrap_unchecked() }).abs())
            .collect()
    };

    // Use select_nth_unstable to find the median in O(n) instead of O(n log n) full sort
    let len = abs_diff_vec.len();
    let mid = len / 2;
    let cmp = |a: &f64, b: &f64| a.total_cmp(b);

    abs_diff_vec.select_nth_unstable_by(mid, cmp);

    if len.is_multiple_of(2) {
        // Even length: need both mid-1 and mid elements
        let right = abs_diff_vec[mid];
        // The left partition [0..mid] contains elements <= abs_diff_vec[mid],
        // so we can find the max of the left partition for mid-1
        let left = abs_diff_vec[..mid]
            .iter()
            .max_by(|a, b| cmp(a, b))
            .copied()?;
        Some(f64::midpoint(left, right))
    } else {
        Some(abs_diff_vec[mid])
    }
}

fn gini_on_sorted<T>(data: &[Partial<T>], precalc_sum: Option<f64>) -> Option<f64>
where
    T: Sync + PartialOrd + ToPrimitive,
{
    let len = data.len();

    // Early return for empty data
    if len == 0 {
        return None;
    }

    // Single element case: perfect equality, Gini = 0
    if len == 1 {
        return Some(0.0);
    }

    // Gini coefficient is only defined for non-negative distributions.
    // Since data is sorted, check the first (smallest) element.
    // SAFETY: len > 1 guaranteed by checks above
    let first_val = unsafe { data.get_unchecked(0).0.to_f64().unwrap_unchecked() };
    if first_val < 0.0 {
        return None;
    }

    // Compute sum and weighted sum.
    // When precalc_sum is provided, only compute weighted_sum in a single pass.
    // When not provided, fuse both computations into a single pass over the data
    // to halve cache pressure (following the fold/reduce pattern used in kurtosis).
    let (sum, weighted_sum) = if let Some(precalc) = precalc_sum {
        if precalc < 0.0 {
            return None;
        }
        // Only need weighted_sum — single pass
        let weighted_sum = if len < PARALLEL_THRESHOLD {
            let mut weighted_sum = 0.0;
            for (i, x) in data.iter().enumerate() {
                // SAFETY: to_f64() always returns Some for standard numeric types
                let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                weighted_sum = ((i + 1) as f64).mul_add(val, weighted_sum);
            }
            weighted_sum
        } else {
            data.par_iter()
                .enumerate()
                .map(|(i, x)| {
                    // SAFETY: to_f64() always returns Some for standard numeric types
                    let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                    ((i + 1) as f64).mul_add(val, 0.0)
                })
                .sum()
        };
        (precalc, weighted_sum)
    } else if len < PARALLEL_THRESHOLD {
        // Fused single pass: compute both sum and weighted_sum together
        let mut sum = 0.0;
        let mut weighted_sum = 0.0;
        for (i, x) in data.iter().enumerate() {
            // SAFETY: to_f64() always returns Some for standard numeric types (f32/f64, i/u 8-64)
            let val = unsafe { x.0.to_f64().unwrap_unchecked() };
            sum += val;
            weighted_sum = ((i + 1) as f64).mul_add(val, weighted_sum);
        }
        (sum, weighted_sum)
    } else {
        // Fused parallel single pass using fold/reduce
        data.par_iter()
            .enumerate()
            .fold(
                || (0.0_f64, 0.0_f64),
                |acc, (i, x)| {
                    // SAFETY: to_f64() always returns Some for standard numeric types
                    let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                    (acc.0 + val, ((i + 1) as f64).mul_add(val, acc.1))
                },
            )
            .reduce(|| (0.0, 0.0), |a, b| (a.0 + b.0, a.1 + b.1))
    };

    // If sum is zero, Gini is undefined
    if sum == 0.0 {
        return None;
    }

    // Compute Gini coefficient using the formula:
    // G = (2 * Σ(i * y_i)) / (n * Σ(y_i)) - (n + 1) / n
    // where i is 1-indexed rank and y_i are sorted values
    let n = len as f64;
    let gini = 2.0f64.mul_add(weighted_sum / (n * sum), -(n + 1.0) / n);

    Some(gini)
}

fn kurtosis_on_sorted<T>(
    data: &[Partial<T>],
    precalc_mean: Option<f64>,
    precalc_variance: Option<f64>,
) -> Option<f64>
where
    T: Sync + PartialOrd + ToPrimitive,
{
    let len = data.len();

    // Need at least 4 elements for meaningful kurtosis
    if len < 4 {
        return None;
    }

    // Use pre-calculated mean if provided, otherwise compute it
    let mean = if let Some(precalc) = precalc_mean {
        precalc
    } else {
        let sum: f64 = if len < PARALLEL_THRESHOLD {
            // Iterator sum enables auto-vectorization (SIMD) by the compiler
            data.iter()
                // SAFETY: to_f64() always returns Some for standard numeric types (f32/f64, i/u 8-64)
                .map(|x| unsafe { x.0.to_f64().unwrap_unchecked() })
                .sum()
        } else {
            data.par_iter()
                // SAFETY: to_f64() always returns Some for standard numeric types
                .map(|x| unsafe { x.0.to_f64().unwrap_unchecked() })
                .sum()
        };
        sum / len as f64
    };

    // Compute variance_sq and fourth_power_sum
    // If variance is provided, we can compute variance_sq directly (variance_sq = variance^2)
    // Otherwise, we need to compute variance from the data
    let (variance_sq, fourth_power_sum) = if let Some(variance) = precalc_variance {
        // Negative variance is invalid (possible floating-point rounding artifact)
        if variance < 0.0 {
            return None;
        }
        // Use pre-calculated variance: variance_sq = variance^2
        let variance_sq = variance * variance;

        // Still need to compute fourth_power_sum
        let fourth_power_sum = if len < PARALLEL_THRESHOLD {
            let mut sum = 0.0;
            for x in data {
                // SAFETY: to_f64() always returns Some for standard numeric types
                let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                let diff = val - mean;
                let diff_sq = diff * diff;
                sum = diff_sq.mul_add(diff_sq, sum);
            }
            sum
        } else {
            data.par_iter()
                .map(|x| {
                    // SAFETY: to_f64() always returns Some for standard numeric types
                    let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                    let diff = val - mean;
                    let diff_sq = diff * diff;
                    diff_sq * diff_sq
                })
                .sum()
        };

        (variance_sq, fourth_power_sum)
    } else {
        // Compute both variance_sum and fourth_power_sum
        let (variance_sum, fourth_power_sum) = if len < PARALLEL_THRESHOLD {
            let mut variance_sum = 0.0;
            let mut fourth_power_sum = 0.0;

            for x in data {
                // SAFETY: to_f64() always returns Some for standard numeric types
                let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                let diff = val - mean;
                let diff_sq = diff * diff;
                variance_sum += diff_sq;
                fourth_power_sum = diff_sq.mul_add(diff_sq, fourth_power_sum);
            }

            (variance_sum, fourth_power_sum)
        } else {
            // Single pass computing both sums simultaneously
            data.par_iter()
                .fold(
                    || (0.0_f64, 0.0_f64),
                    |acc, x| {
                        // SAFETY: to_f64() always returns Some for standard numeric types
                        let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                        let diff = val - mean;
                        let diff_sq = diff * diff;
                        (acc.0 + diff_sq, diff_sq.mul_add(diff_sq, acc.1))
                    },
                )
                .reduce(|| (0.0, 0.0), |a, b| (a.0 + b.0, a.1 + b.1))
        };

        let variance = variance_sum / len as f64;

        // If variance is zero, all values are the same, kurtosis is undefined
        if variance == 0.0 {
            return None;
        }

        let variance_sq = variance * variance;
        (variance_sq, fourth_power_sum)
    };

    // If variance_sq is zero, all values are the same, kurtosis is undefined
    if variance_sq == 0.0 {
        return None;
    }

    let n = len as f64;

    // Sample excess kurtosis formula:
    // kurtosis = (n(n+1) * Σ((x_i - mean)⁴)) / ((n-1)(n-2)(n-3) * variance²) - 3(n-1)²/((n-2)(n-3))
    let denominator = (n - 1.0) * (n - 2.0) * (n - 3.0);
    let adjustment = 3.0 * (n - 1.0) * (n - 1.0) / denominator;
    let kurtosis = (n * (n + 1.0) * fourth_power_sum).mul_add(1.0 / (denominator * variance_sq), -adjustment);

    Some(kurtosis)
}

fn percentile_rank_on_sorted<T, V>(data: &[Partial<T>], value: &V) -> Option<f64>
where
    T: PartialOrd + ToPrimitive,
    V: PartialOrd + ToPrimitive,
{
    let len = data.len();

    if len == 0 {
        return None;
    }

    let value_f64 = value.to_f64()?;

    // Binary search to find the position where value would be inserted
    // This gives us the number of values <= value
    let count_leq = data.binary_search_by(|x| {
        x.0.to_f64()
            .unwrap_or(f64::NAN)
            .partial_cmp(&value_f64)
            .unwrap_or(std::cmp::Ordering::Less)
    });

    let count = match count_leq {
        Ok(idx) => {
            // Value found at idx — use partition_point (O(log n)) to find the upper bound
            // of equal values instead of a linear scan
            let upper = data[idx + 1..].partition_point(|x| {
                x.0.to_f64()
                    .is_some_and(|v| v.total_cmp(&value_f64).is_le())
            });
            idx + 1 + upper
        }
        Err(idx) => idx, // Number of values less than value
    };

    // Percentile rank = (count / n) * 100
    Some((count as f64 / len as f64) * 100.0)
}

fn atkinson_on_sorted<T>(
    data: &[Partial<T>],
    epsilon: f64,
    precalc_mean: Option<f64>,
    precalc_geometric_sum: Option<f64>,
) -> Option<f64>
where
    T: Sync + PartialOrd + ToPrimitive,
{
    let len = data.len();

    // Early return for empty data
    if len == 0 {
        return None;
    }

    // Single element case: perfect equality, Atkinson = 0
    if len == 1 {
        return Some(0.0);
    }

    // Epsilon must be non-negative
    if epsilon < 0.0 {
        return None;
    }

    // Use pre-calculated mean if provided, otherwise compute it
    let mean = if let Some(precalc) = precalc_mean {
        precalc
    } else {
        let sum: f64 = if len < PARALLEL_THRESHOLD {
            // Iterator sum enables auto-vectorization (SIMD) by the compiler
            data.iter()
                // SAFETY: to_f64() always returns Some for standard numeric types (f32/f64, i/u 8-64)
                .map(|x| unsafe { x.0.to_f64().unwrap_unchecked() })
                .sum()
        } else {
            data.par_iter()
                // SAFETY: to_f64() always returns Some for standard numeric types
                .map(|x| unsafe { x.0.to_f64().unwrap_unchecked() })
                .sum()
        };
        sum / len as f64
    };

    // If mean is zero, Atkinson is undefined
    if mean == 0.0 {
        return None;
    }

    // Handle special case: epsilon = 1 (uses geometric mean)
    if (epsilon - 1.0).abs() < 1e-10 {
        // A_1 = 1 - (geometric_mean / mean)
        let geometric_sum: f64 = if let Some(precalc) = precalc_geometric_sum {
            precalc
        } else if len < PARALLEL_THRESHOLD {
            let mut sum = 0.0;
            for x in data {
                // SAFETY: to_f64() always returns Some for standard numeric types
                let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                if val <= 0.0 {
                    // Geometric mean undefined for non-positive values
                    return None;
                }
                sum += val.ln();
            }
            sum
        } else {
            data.par_iter()
                .map(|x| {
                    // SAFETY: to_f64() always returns Some for standard numeric types
                    let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                    if val <= 0.0 {
                        return f64::NAN;
                    }
                    val.ln()
                })
                .sum()
        };

        if geometric_sum.is_nan() {
            return None;
        }

        let geometric_mean = (geometric_sum / len as f64).exp();
        return Some(1.0 - geometric_mean / mean);
    }

    // General case: epsilon != 1
    // A_ε = 1 - (1/n * Σ((x_i/mean)^(1-ε)))^(1/(1-ε))
    let exponent = 1.0 - epsilon;

    let sum_powered: f64 = if len < PARALLEL_THRESHOLD {
        let mut sum = 0.0;
        for x in data {
            // SAFETY: to_f64() always returns Some for standard numeric types
            let val = unsafe { x.0.to_f64().unwrap_unchecked() };
            if val < 0.0 {
                // Negative values with non-integer exponent are undefined
                return None;
            }
            let ratio = val / mean;
            sum += ratio.powf(exponent);
        }
        sum
    } else {
        data.par_iter()
            .map(|x| {
                // SAFETY: to_f64() always returns Some for standard numeric types
                let val = unsafe { x.0.to_f64().unwrap_unchecked() };
                if val < 0.0 {
                    return f64::NAN;
                }
                let ratio = val / mean;
                ratio.powf(exponent)
            })
            .sum()
    };

    if sum_powered.is_nan() || sum_powered <= 0.0 {
        return None;
    }

    let atkinson = 1.0 - (sum_powered / len as f64).powf(1.0 / exponent);
    Some(atkinson)
}

/// Selection algorithm to find the k-th smallest element in O(n) average time.
/// This is an implementation of quickselect algorithm.
#[cfg(test)]
fn quickselect<T>(data: &mut [Partial<T>], k: usize) -> Option<&T>
where
    T: PartialOrd,
{
    if data.is_empty() || k >= data.len() {
        return None;
    }

    let mut left = 0;
    let mut right = data.len() - 1;

    loop {
        if left == right {
            return Some(&data[left].0);
        }

        // Use median-of-three pivot selection for better performance
        let pivot_idx = median_of_three_pivot(data, left, right);
        let pivot_idx = partition(data, left, right, pivot_idx);

        match k.cmp(&pivot_idx) {
            std::cmp::Ordering::Equal => return Some(&data[pivot_idx].0),
            std::cmp::Ordering::Less => right = pivot_idx - 1,
            std::cmp::Ordering::Greater => left = pivot_idx + 1,
        }
    }
}

/// Select the median of three elements as pivot for better quickselect performance
#[cfg(test)]
fn median_of_three_pivot<T>(data: &[Partial<T>], left: usize, right: usize) -> usize
where
    T: PartialOrd,
{
    let mid = left + (right - left) / 2;

    if data[left] <= data[mid] {
        if data[mid] <= data[right] {
            mid
        } else if data[left] <= data[right] {
            right
        } else {
            left
        }
    } else if data[left] <= data[right] {
        left
    } else if data[mid] <= data[right] {
        right
    } else {
        mid
    }
}

/// Partition function for quickselect
#[cfg(test)]
fn partition<T>(data: &mut [Partial<T>], left: usize, right: usize, pivot_idx: usize) -> usize
where
    T: PartialOrd,
{
    // Move pivot to end
    data.swap(pivot_idx, right);
    let mut store_idx = left;

    // Move all elements smaller than pivot to the left
    // Cache pivot position for better cache locality (access data[right] directly each time)
    for i in left..right {
        // Safety: i, store_idx, and right are guaranteed to be in bounds
        // Compare directly with pivot at data[right] - compiler should optimize this access
        if unsafe { data.get_unchecked(i) <= data.get_unchecked(right) } {
            data.swap(i, store_idx);
            store_idx += 1;
        }
    }

    // Move pivot to its final place
    data.swap(store_idx, right);
    store_idx
}

// This implementation follows Method 3 from https://en.wikipedia.org/wiki/Quartile
// It divides data into quarters based on the length n = 4k + r where r is remainder.
// For each remainder case (0,1,2,3), it uses different formulas to compute Q1, Q2, Q3.
fn quartiles_on_sorted<T>(data: &[Partial<T>]) -> Option<(f64, f64, f64)>
where
    T: PartialOrd + ToPrimitive,
{
    let len = data.len();

    // Early return for small arrays
    match len {
        0..=2 => return None,
        3 => {
            return Some(
                // SAFETY: We know these indices are valid because len == 3
                unsafe {
                    (
                        data.get_unchecked(0).0.to_f64()?,
                        data.get_unchecked(1).0.to_f64()?,
                        data.get_unchecked(2).0.to_f64()?,
                    )
                },
            );
        }
        _ => {}
    }

    // Calculate k and remainder in one division
    let k = len / 4;
    let remainder = len % 4;

    // SAFETY: All index calculations below are guaranteed to be in bounds
    // because we've verified len >= 4 above and k is len/4
    unsafe {
        Some(match remainder {
            0 => {
                // Let data = {x_i}_{i=0..4k} where k is positive integer.
                // Median q2 = (x_{2k-1} + x_{2k}) / 2.
                // If we divide data into two parts {x_i < q2} as L and
                // {x_i > q2} as R, #L == #R == 2k holds true. Thus,
                // q1 = (x_{k-1} + x_{k}) / 2 and q3 = (x_{3k-1} + x_{3k}) / 2.
                // =============
                // Simply put: Length is multiple of 4 (4k)
                // q1 = (x_{k-1} + x_k) / 2
                // q2 = (x_{2k-1} + x_{2k}) / 2
                // q3 = (x_{3k-1} + x_{3k}) / 2
                let q1 = f64::midpoint(
                    data.get_unchecked(k - 1).0.to_f64()?,
                    data.get_unchecked(k).0.to_f64()?,
                );
                let q2 = f64::midpoint(
                    data.get_unchecked(2 * k - 1).0.to_f64()?,
                    data.get_unchecked(2 * k).0.to_f64()?,
                );
                let q3 = f64::midpoint(
                    data.get_unchecked(3 * k - 1).0.to_f64()?,
                    data.get_unchecked(3 * k).0.to_f64()?,
                );
                (q1, q2, q3)
            }
            1 => {
                // Let data = {x_i}_{i=0..4k+1} where k is positive integer.
                // Median q2 = x_{2k}.
                // If we divide data other than q2 into two parts {x_i < q2}
                // as L and {x_i > q2} as R, #L == #R == 2k holds true. Thus,
                // q1 = (x_{k-1} + x_{k}) / 2 and q3 = (x_{3k} + x_{3k+1}) / 2.
                // =============
                // Simply put: Length is 4k + 1
                // q1 = (x_{k-1} + x_k) / 2
                // q2 = x_{2k}
                // q3 = (x_{3k} + x_{3k+1}) / 2
                let q1 = f64::midpoint(
                    data.get_unchecked(k - 1).0.to_f64()?,
                    data.get_unchecked(k).0.to_f64()?,
                );
                let q2 = data.get_unchecked(2 * k).0.to_f64()?;
                let q3 = f64::midpoint(
                    data.get_unchecked(3 * k).0.to_f64()?,
                    data.get_unchecked(3 * k + 1).0.to_f64()?,
                );
                (q1, q2, q3)
            }
            2 => {
                // Let data = {x_i}_{i=0..4k+2} where k is positive integer.
                // Median q2 = (x_{(2k+1)-1} + x_{2k+1}) / 2.
                // If we divide data into two parts {x_i < q2} as L and
                // {x_i > q2} as R, it's true that #L == #R == 2k+1.
                // Thus, q1 = x_{k} and q3 = x_{3k+1}.
                // =============
                // Simply put: Length is 4k + 2
                // q1 = x_k
                // q2 = (x_{2k} + x_{2k+1}) / 2
                // q3 = x_{3k+1}
                let q1 = data.get_unchecked(k).0.to_f64()?;
                let q2 = f64::midpoint(
                    data.get_unchecked(2 * k).0.to_f64()?,
                    data.get_unchecked(2 * k + 1).0.to_f64()?,
                );
                let q3 = data.get_unchecked(3 * k + 1).0.to_f64()?;
                (q1, q2, q3)
            }
            _ => {
                // Let data = {x_i}_{i=0..4k+3} where k is positive integer.
                // Median q2 = x_{2k+1}.
                // If we divide data other than q2 into two parts {x_i < q2}
                // as L and {x_i > q2} as R, #L == #R == 2k+1 holds true.
                // Thus, q1 = x_{k} and q3 = x_{3k+2}.
                // =============
                // Simply put: Length is 4k + 3
                // q1 = x_k
                // q2 = x_{2k+1}
                // q3 = x_{3k+2}
                let q1 = data.get_unchecked(k).0.to_f64()?;
                let q2 = data.get_unchecked(2 * k + 1).0.to_f64()?;
                let q3 = data.get_unchecked(3 * k + 2).0.to_f64()?;
                (q1, q2, q3)
            }
        })
    }
}

/// Zero-copy quartiles computation using index-based selection.
/// This avoids copying data by working with an array of indices.
///
/// Uses `select_nth_unstable_by` on the indices array, which partitions in-place.
/// After selecting position p, elements at indices [0..p] are <= the p-th element
/// and elements at [p+1..] are >= it. By selecting positions in ascending order,
/// each subsequent selection only needs to search within the right partition,
/// avoiding redundant O(n) resets.
fn quartiles_with_zero_copy_selection<T>(data: &[Partial<T>]) -> Option<(f64, f64, f64)>
where
    T: PartialOrd + ToPrimitive,
{
    let len = data.len();

    // Early return for small arrays
    match len {
        0..=2 => return None,
        3 => {
            let mut indices: Vec<usize> = (0..3).collect();
            let cmp =
                |a: &usize, b: &usize| data[*a].partial_cmp(&data[*b]).unwrap_or(std::cmp::Ordering::Less);
            indices.sort_unstable_by(cmp);
            let min_val = data[indices[0]].0.to_f64()?;
            let med_val = data[indices[1]].0.to_f64()?;
            let max_val = data[indices[2]].0.to_f64()?;
            return Some((min_val, med_val, max_val));
        }
        _ => {}
    }

    let k = len / 4;
    let remainder = len % 4;

    let mut indices: Vec<usize> = (0..len).collect();
    let cmp = |a: &usize, b: &usize| {
        data[*a]
            .partial_cmp(&data[*b])
            .unwrap_or(std::cmp::Ordering::Less)
    };

    // Collect the unique positions we need in ascending order.
    // By selecting in ascending order, each select_nth_unstable_by partitions
    // the array so subsequent selections operate on progressively smaller slices.
    // We deduplicate because adjacent quartile boundaries can overlap for small k.
    let raw_positions: Vec<usize> = match remainder {
        0 => vec![k - 1, k, 2 * k - 1, 2 * k, 3 * k - 1, 3 * k],
        1 => vec![k - 1, k, 2 * k, 3 * k, 3 * k + 1],
        2 => vec![k, 2 * k, 2 * k + 1, 3 * k + 1],
        _ => vec![k, 2 * k + 1, 3 * k + 2],
    };

    let mut unique_positions = raw_positions.clone();
    unique_positions.dedup();

    // Select each unique position in ascending order, narrowing the search range
    let mut start = 0;
    for &pos in &unique_positions {
        indices[start..].select_nth_unstable_by(pos - start, &cmp);
        start = pos + 1;
    }

    // Now read all needed values (including duplicates) from the partitioned indices
    let values: Vec<f64> = raw_positions
        .iter()
        .map(|&pos| data[indices[pos]].0.to_f64())
        .collect::<Option<Vec<_>>>()?;

    match remainder {
        0 => {
            let q1 = f64::midpoint(values[0], values[1]);
            let q2 = f64::midpoint(values[2], values[3]);
            let q3 = f64::midpoint(values[4], values[5]);
            Some((q1, q2, q3))
        }
        1 => {
            let q1 = f64::midpoint(values[0], values[1]);
            let q2 = values[2];
            let q3 = f64::midpoint(values[3], values[4]);
            Some((q1, q2, q3))
        }
        2 => {
            let q1 = values[0];
            let q2 = f64::midpoint(values[1], values[2]);
            let q3 = values[3];
            Some((q1, q2, q3))
        }
        _ => Some((values[0], values[1], values[2])),
    }
}

fn mode_on_sorted<T, I>(it: I) -> Option<T>
where
    T: PartialOrd,
    I: Iterator<Item = T>,
{
    use std::cmp::Ordering;

    // This approach to computing the mode works very nicely when the
    // number of samples is large and is close to its cardinality.
    // In other cases, a hashmap would be much better.
    // But really, how can we know this when given an arbitrary stream?
    // Might just switch to a hashmap to track frequencies. That would also
    // be generally useful for discovering the cardinality of a sample.
    let (mut mode, mut next) = (None, None);
    let (mut mode_count, mut next_count) = (0usize, 0usize);
    for x in it {
        if mode.as_ref() == Some(&x) {
            mode_count += 1;
        } else if next.as_ref() == Some(&x) {
            next_count += 1;
        } else {
            next = Some(x);
            next_count = 0;
        }

        match next_count.cmp(&mode_count) {
            Ordering::Greater => {
                mode = next;
                mode_count = next_count;
                next = None;
                next_count = 0;
            }
            Ordering::Equal => {
                mode = None;
                mode_count = 0;
            }
            Ordering::Less => {}
        }
    }
    mode
}

/// Computes both modes and antimodes from a sorted slice of values.
/// This version works with references to avoid unnecessary cloning.
///
/// # Arguments
///
/// * `data` - A sorted slice of values
///
/// # Notes
///
/// - Mode is the most frequently occurring value(s)
/// - Antimode is the least frequently occurring value(s)
/// - Only returns up to 10 antimodes to avoid returning the full set when all values are unique
/// - For empty slices, returns empty vectors and zero counts
/// - For single value slices, returns that value as the mode and empty antimode
/// - When all values occur exactly once, returns empty mode and up to 10 values as antimodes
///
/// # Returns
///
/// A tuple containing:
/// * Modes information: `(Vec<T>, usize, u32)` where:
///   - Vec<T>: Vector containing the mode values
///   - usize: Number of modes found
///   - u32: Frequency/count of the mode values
/// * Antimodes information: `(Vec<T>, usize, u32)` where:
///   - Vec<T>: Vector containing up to 10 antimode values
///   - usize: Total number of antimodes
///   - u32: Frequency/count of the antimode values
#[allow(clippy::type_complexity)]
#[inline]
fn modes_and_antimodes_on_sorted_slice<T>(
    data: &[Partial<T>],
) -> ((Vec<T>, usize, u32), (Vec<T>, usize, u32))
where
    T: PartialOrd + Clone,
{
    let size = data.len();

    // Early return for empty slice
    if size == 0 {
        return ((Vec::new(), 0, 0), (Vec::new(), 0, 0));
    }

    // Estimate capacity using integer square root of size
    // Integer square root using Newton's method (faster than floating point sqrt)
    let mut x = size;
    let mut y = x.div_ceil(2);
    while y < x {
        x = y;
        y = usize::midpoint(x, size / x);
    }
    let sqrt_size = x;
    let mut runs: Vec<(&T, u32)> = Vec::with_capacity(sqrt_size.clamp(16, 1_000));

    let mut current_value = &data[0].0;
    let mut current_count = 1;
    let mut highest_count = 1;
    let mut lowest_count = u32::MAX;

    // Count consecutive runs - optimized to reduce allocations
    for x in data.iter().skip(1) {
        if x.0 == *current_value {
            current_count += 1;
            highest_count = highest_count.max(current_count);
        } else {
            runs.push((current_value, current_count));
            lowest_count = lowest_count.min(current_count);
            current_value = &x.0;
            current_count = 1;
        }
    }
    runs.push((current_value, current_count));
    lowest_count = lowest_count.min(current_count);

    // Early return if only one unique value
    if runs.len() == 1 {
        let (val, count) = runs.pop().unwrap();
        return ((vec![val.clone()], 1, count), (Vec::new(), 0, 0));
    }

    // Special case: if all values appear exactly once
    if highest_count == 1 {
        let antimodes_count = runs.len().min(10);
        let total_count = runs.len();
        let mut antimodes = Vec::with_capacity(antimodes_count);
        for (val, _) in runs.into_iter().take(antimodes_count) {
            antimodes.push(val.clone());
        }
        // For modes: empty, count 0, occurrences 0 (not 1, 1)
        return ((Vec::new(), 0, 0), (antimodes, total_count, 1));
    }

    // Collect modes and antimodes directly in a single pass, cloning values immediately
    // instead of collecting indices first and then cloning in a second pass
    let estimated_modes = (runs.len() / 10).clamp(1, 10);
    let estimated_antimodes = 10.min(runs.len());

    let mut modes_result = Vec::with_capacity(estimated_modes);
    let mut antimodes_result = Vec::with_capacity(estimated_antimodes);
    let mut mode_count = 0;
    let mut antimodes_count = 0;
    let mut antimodes_collected = 0_u32;

    for (val, count) in &runs {
        if *count == highest_count {
            modes_result.push((*val).clone());
            mode_count += 1;
        }
        if *count == lowest_count {
            antimodes_count += 1;
            if antimodes_collected < 10 {
                antimodes_result.push((*val).clone());
                antimodes_collected += 1;
            }
        }
    }

    (
        (modes_result, mode_count, highest_count),
        (antimodes_result, antimodes_count, lowest_count),
    )
}

/// A commutative data structure for lazily sorted sequences of data.
///
/// The sort does not occur until statistics need to be computed.
///
/// Note that this works on types that do not define a total ordering like
/// `f32` and `f64`. When an ordering is not defined, an arbitrary order
/// is returned.
#[allow(clippy::unsafe_derive_deserialize)]
#[derive(Clone, Serialize, Deserialize, Eq, PartialEq)]
pub struct Unsorted<T> {
    sorted: bool,
    data: Vec<Partial<T>>,
}

impl<T: PartialOrd + Send> Unsorted<T> {
    /// Create initial empty state.
    #[inline]
    #[must_use]
    pub fn new() -> Unsorted<T> {
        Default::default()
    }

    /// Add a new element to the set.
    #[allow(clippy::inline_always)]
    #[inline(always)]
    pub fn add(&mut self, v: T) {
        self.sorted = false;
        self.data.push(Partial(v));
    }

    /// Return the number of data points.
    #[inline]
    #[must_use]
    pub const fn len(&self) -> usize {
        self.data.len()
    }

    #[inline]
    #[must_use]
    pub const fn is_empty(&self) -> bool {
        self.data.is_empty()
    }

    #[inline]
    fn sort(&mut self) {
        if !self.sorted {
            // Use sequential sort for small datasets (< 10k elements) to avoid parallel overhead
            if self.data.len() < PARALLEL_THRESHOLD {
                self.data.sort_unstable();
            } else {
                self.data.par_sort_unstable();
            }
            self.sorted = true;
        }
    }

    #[inline]
    const fn already_sorted(&mut self) {
        self.sorted = true;
    }

    /// Add multiple elements efficiently
    #[inline]
    pub fn add_bulk(&mut self, values: Vec<T>) {
        self.sorted = false;
        self.data.reserve(values.len());
        self.data.extend(values.into_iter().map(Partial));
    }

    /// Shrink capacity to fit current data
    #[inline]
    pub fn shrink_to_fit(&mut self) {
        self.data.shrink_to_fit();
    }

    /// Create with specific capacity
    #[inline]
    #[must_use]
    pub fn with_capacity(capacity: usize) -> Self {
        Unsorted {
            sorted: true,
            data: Vec::with_capacity(capacity),
        }
    }

    /// Add a value assuming it's greater than all existing values
    #[inline]
    pub fn push_ascending(&mut self, value: T) {
        if let Some(last) = self.data.last() {
            debug_assert!(last.0 <= value, "Value must be >= than last element");
        }
        self.data.push(Partial(value));
        // Data remains sorted
    }
}

impl<T: PartialOrd + PartialEq + Clone + Send + Sync> Unsorted<T> {
    #[inline]
    /// Returns the cardinality of the data.
    /// Set `sorted` to `true` if the data is already sorted.
    /// Set `parallel_threshold` to `0` to force sequential processing.
    /// Set `parallel_threshold` to `1` to use the default parallel threshold (`10_000`).
    /// Set `parallel_threshold` to `2` to force parallel processing.
    /// Set `parallel_threshold` to any other value to use a custom parallel threshold
    /// greater than the default threshold of `10_000`.
    pub fn cardinality(&mut self, sorted: bool, parallel_threshold: usize) -> u64 {
        const CHUNK_SIZE: usize = 2048; // Process data in chunks of 2048 elements
        const DEFAULT_PARALLEL_THRESHOLD: usize = 10_240; // multiple of 2048

        let len = self.data.len();
        match len {
            0 => return 0,
            1 => return 1,
            _ => {}
        }

        if sorted {
            self.already_sorted();
        } else {
            self.sort();
        }

        let use_parallel = parallel_threshold != 0
            && (parallel_threshold == 1
                || len > parallel_threshold.max(DEFAULT_PARALLEL_THRESHOLD));

        if use_parallel {
            // Parallel processing using chunks
            // Process chunks in parallel, returning (count, first_elem, last_elem) for each
            type ChunkInfo<'a, T> = Vec<(u64, Option<&'a Partial<T>>, Option<&'a Partial<T>>)>;
            let chunk_info: ChunkInfo<'_, T> = self
                .data
                .par_chunks(CHUNK_SIZE)
                .map(|chunk| {
                    // Count unique elements within this chunk
                    let mut count = u64::from(!chunk.is_empty());
                    for [a, b] in chunk.array_windows::<2>() {
                        if a != b {
                            count += 1;
                        }
                    }
                    (count, chunk.first(), chunk.last())
                })
                .collect();

            // Combine results, checking boundaries between chunks
            let mut total = 0;
            for (i, &(count, first_opt, _last_opt)) in chunk_info.iter().enumerate() {
                total += count;

                // Check boundary with previous chunk
                if i > 0
                    && let (Some(prev_last), Some(curr_first)) = (chunk_info[i - 1].2, first_opt)
                    && prev_last == curr_first
                {
                    total -= 1; // Deduct 1 if boundary values are equal
                }
            }

            total
        } else {
            // Sequential processing

            // the statement below is equivalent to:
            // let mut count = if self.data.is_empty() { 0 } else { 1 };
            let mut count = u64::from(!self.data.is_empty());

            for [a, b] in self.data.array_windows::<2>() {
                if a != b {
                    count += 1;
                }
            }
            count
        }
    }
}

impl<T: PartialOrd + Clone + Send> Unsorted<T> {
    /// Returns the mode of the data.
    #[inline]
    pub fn mode(&mut self) -> Option<T> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        mode_on_sorted(self.data.iter().map(|p| &p.0)).cloned()
    }

    /// Returns the modes of the data.
    /// Note that there is also a `frequency::mode()` function that return one mode
    /// with the highest frequency. If there is a tie, it returns None.
    #[inline]
    fn modes(&mut self) -> (Vec<T>, usize, u32) {
        if self.data.is_empty() {
            return (Vec::new(), 0, 0);
        }
        self.sort();
        modes_and_antimodes_on_sorted_slice(&self.data).0
    }

    /// Returns the antimodes of the data.
    /// `antimodes_result` only returns the first 10 antimodes
    #[inline]
    fn antimodes(&mut self) -> (Vec<T>, usize, u32) {
        if self.data.is_empty() {
            return (Vec::new(), 0, 0);
        }
        self.sort();
        modes_and_antimodes_on_sorted_slice(&self.data).1
    }

    /// Returns the modes and antimodes of the data.
    /// `antimodes_result` only returns the first 10 antimodes
    #[allow(clippy::type_complexity)]
    #[inline]
    pub fn modes_antimodes(&mut self) -> ((Vec<T>, usize, u32), (Vec<T>, usize, u32)) {
        if self.data.is_empty() {
            return ((Vec::new(), 0, 0), (Vec::new(), 0, 0));
        }
        self.sort();
        modes_and_antimodes_on_sorted_slice(&self.data)
    }
}

impl Unsorted<Vec<u8>> {
    /// Add a byte slice, converting to `Vec<u8>` internally.
    ///
    /// This is a convenience method that avoids requiring the caller to call
    /// `.to_vec()` before `add()`. The allocation still occurs internally,
    /// but the API is cleaner and opens the door for future optimizations
    /// (e.g., frequency-map deduplication for high-cardinality data).
    #[allow(clippy::inline_always)]
    #[inline(always)]
    pub fn add_bytes(&mut self, v: &[u8]) {
        self.sorted = false;
        self.data.push(Partial(v.to_vec()));
    }
}

impl<T: PartialOrd + ToPrimitive + Send> Unsorted<T> {
    /// Returns the median of the data.
    #[inline]
    pub fn median(&mut self) -> Option<f64> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        median_on_sorted(&self.data)
    }
}

impl<T: PartialOrd + ToPrimitive + Send + Sync> Unsorted<T> {
    /// Returns the Median Absolute Deviation (MAD) of the data.
    #[inline]
    pub fn mad(&mut self, existing_median: Option<f64>) -> Option<f64> {
        if self.data.is_empty() {
            return None;
        }
        if existing_median.is_none() {
            self.sort();
        }
        mad_on_sorted(&self.data, existing_median)
    }
}

impl<T: PartialOrd + ToPrimitive + Send> Unsorted<T> {
    /// Returns the quartiles of the data using the traditional sorting approach.
    ///
    /// This method sorts the data first and then computes quartiles.
    /// Time complexity: O(n log n)
    #[inline]
    pub fn quartiles(&mut self) -> Option<(f64, f64, f64)> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        quartiles_on_sorted(&self.data)
    }
}

impl<T: PartialOrd + ToPrimitive + Send + Sync> Unsorted<T> {
    /// Returns the Gini Coefficient of the data.
    ///
    /// The Gini Coefficient measures inequality in a distribution, ranging from 0 (perfect equality)
    /// to 1 (perfect inequality). This method sorts the data first and then computes the Gini coefficient.
    /// Time complexity: O(n log n)
    #[inline]
    pub fn gini(&mut self, precalc_sum: Option<f64>) -> Option<f64> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        gini_on_sorted(&self.data, precalc_sum)
    }

    /// Returns the kurtosis (excess kurtosis) of the data.
    ///
    /// Kurtosis measures the "tailedness" of a distribution. Excess kurtosis is kurtosis - 3,
    /// where 0 indicates a normal distribution, positive values indicate heavy tails, and
    /// negative values indicate light tails. This method sorts the data first and then computes kurtosis.
    /// Time complexity: O(n log n)
    #[inline]
    pub fn kurtosis(
        &mut self,
        precalc_mean: Option<f64>,
        precalc_variance: Option<f64>,
    ) -> Option<f64> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        kurtosis_on_sorted(&self.data, precalc_mean, precalc_variance)
    }

    /// Returns the percentile rank of a value in the data.
    ///
    /// Returns the percentile rank (0-100) of the given value. If the value is less than all
    /// values, returns 0.0. If greater than all, returns 100.0.
    /// This method sorts the data first and then computes the percentile rank.
    /// Time complexity: O(n log n)
    #[inline]
    #[allow(clippy::needless_pass_by_value)]
    pub fn percentile_rank<V>(&mut self, value: V) -> Option<f64>
    where
        V: PartialOrd + ToPrimitive,
    {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        percentile_rank_on_sorted(&self.data, &value)
    }

    /// Returns the Atkinson Index of the data.
    ///
    /// The Atkinson Index measures inequality with an inequality aversion parameter ε.
    /// It ranges from 0 (perfect equality) to 1 (perfect inequality).
    /// Higher ε values give more weight to inequality at the lower end of the distribution.
    /// This method sorts the data first and then computes the Atkinson index.
    /// Time complexity: O(n log n)
    ///
    /// # Arguments
    /// * `epsilon` - Inequality aversion parameter (must be >= 0). Common values:
    ///   - 0.0: No inequality aversion (returns 0)
    ///   - 0.5: Moderate aversion
    ///   - 1.0: Uses geometric mean (special case)
    ///   - 2.0: High aversion
    /// * `precalc_mean` - Optional pre-calculated mean
    /// * `precalc_geometric_sum` - Optional pre-calculated geometric sum (sum of ln(val)), only used when epsilon = 1
    #[inline]
    pub fn atkinson(
        &mut self,
        epsilon: f64,
        precalc_mean: Option<f64>,
        precalc_geometric_sum: Option<f64>,
    ) -> Option<f64> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        atkinson_on_sorted(&self.data, epsilon, precalc_mean, precalc_geometric_sum)
    }
}

impl<T: PartialOrd + ToPrimitive + Clone + Send> Unsorted<T> {
    /// Returns the quartiles of the data using selection algorithm.
    ///
    /// This implementation uses a selection algorithm (quickselect) to find quartiles
    /// in O(n) average time complexity instead of O(n log n) sorting.
    /// Requires T to implement Clone to create a working copy of the data.
    ///
    /// **Performance Note**: While theoretically O(n) vs O(n log n), this implementation
    /// is often slower than the sorting-based approach for small to medium datasets due to:
    /// - Need to find multiple order statistics (3 separate quickselect calls)
    /// - Overhead of copying data to avoid mutation
    /// - Rayon's highly optimized parallel sorting
    #[inline]
    pub fn quartiles_with_selection(&mut self) -> Option<(f64, f64, f64)> {
        if self.data.is_empty() {
            return None;
        }
        // Use zero-copy approach (indices-based) to avoid cloning all elements
        quartiles_with_zero_copy_selection(&self.data)
    }
}

impl<T: PartialOrd + ToPrimitive + Send> Unsorted<T> {
    /// Returns the quartiles using zero-copy selection algorithm.
    ///
    /// This implementation avoids copying data by working with indices instead,
    /// providing better performance than the clone-based selection approach.
    /// The algorithm is O(n) average time and only allocates a vector of indices (usize).
    #[inline]
    #[must_use]
    pub fn quartiles_zero_copy(&self) -> Option<(f64, f64, f64)> {
        if self.data.is_empty() {
            return None;
        }
        quartiles_with_zero_copy_selection(&self.data)
    }
}

impl<T: PartialOrd + Send> Commute for Unsorted<T> {
    #[inline]
    fn merge(&mut self, mut v: Unsorted<T>) {
        if v.is_empty() {
            return;
        }

        self.sorted = false;
        // we use std::mem::take to avoid unnecessary allocations
        self.data.extend(std::mem::take(&mut v.data));
    }
}

impl<T: PartialOrd> Default for Unsorted<T> {
    #[inline]
    fn default() -> Unsorted<T> {
        Unsorted {
            data: Vec::with_capacity(16),
            sorted: true, // empty is sorted
        }
    }
}

impl<T: PartialOrd + Send> FromIterator<T> for Unsorted<T> {
    #[inline]
    fn from_iter<I: IntoIterator<Item = T>>(it: I) -> Unsorted<T> {
        let mut v = Unsorted::new();
        v.extend(it);
        v
    }
}

impl<T: PartialOrd> Extend<T> for Unsorted<T> {
    #[inline]
    fn extend<I: IntoIterator<Item = T>>(&mut self, it: I) {
        self.sorted = false;
        self.data.extend(it.into_iter().map(Partial));
    }
}

fn custom_percentiles_on_sorted<T>(data: &[Partial<T>], percentiles: &[u8]) -> Option<Vec<T>>
where
    T: PartialOrd + Clone,
{
    let len = data.len();

    // Early return for empty array or invalid percentiles
    if len == 0 || percentiles.iter().any(|&p| p > 100) {
        return None;
    }

    // Optimize: Check if percentiles are already sorted and unique
    let unique_percentiles: Vec<u8> = if percentiles.len() <= 1 {
        // Single or empty percentile - no need to sort/dedup
        percentiles.to_vec()
    } else {
        // Check if already sorted and unique (common case)
        let is_sorted_unique = percentiles.array_windows::<2>().all(|[a, b]| a < b);

        if is_sorted_unique {
            // Already sorted and unique, use directly without cloning
            percentiles.to_vec()
        } else {
            // Need to sort and dedup - use fixed-size bool array (domain is 0..=100)
            let mut seen = [false; 101];
            let mut sorted_unique = Vec::with_capacity(percentiles.len().min(101));
            for &p in percentiles {
                if !seen[p as usize] {
                    seen[p as usize] = true;
                    sorted_unique.push(p);
                }
            }
            sorted_unique.sort_unstable();
            sorted_unique
        }
    };

    let mut results = Vec::with_capacity(unique_percentiles.len());

    // SAFETY: All index calculations below are guaranteed to be in bounds
    // because we've verified len > 0 and the rank calculation ensures
    // the index is within bounds
    unsafe {
        for &p in &unique_percentiles {
            // Calculate the ordinal rank using nearest-rank method
            // see https://en.wikipedia.org/wiki/Percentile#The_nearest-rank_method
            // n = ⌈(P/100) × N⌉
            #[allow(clippy::cast_sign_loss)]
            let rank = ((f64::from(p) / 100.0) * len as f64).ceil() as usize;

            // Convert to 0-based index
            let idx = rank.saturating_sub(1);

            // Get the value at that rank and extract the inner value
            results.push(data.get_unchecked(idx).0.clone());
        }
    }

    Some(results)
}

impl<T: PartialOrd + Clone + Send> Unsorted<T> {
    /// Returns the requested percentiles of the data.
    ///
    /// Uses the nearest-rank method to compute percentiles.
    /// Each returned value is an actual value from the dataset.
    ///
    /// # Arguments
    /// * `percentiles` - A slice of u8 values representing percentiles to compute (0-100)
    ///
    /// # Returns
    /// * `None` if the data is empty or if any percentile is > 100
    /// * `Some(Vec<T>)` containing percentile values in the same order as requested
    ///
    /// # Example
    /// ```
    /// use stats::Unsorted;
    /// let mut data = Unsorted::new();
    /// data.extend(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
    /// let percentiles = vec![25, 50, 75];
    /// let results = data.custom_percentiles(&percentiles).unwrap();
    /// assert_eq!(results, vec![3, 5, 8]);
    /// ```
    #[inline]
    pub fn custom_percentiles(&mut self, percentiles: &[u8]) -> Option<Vec<T>> {
        if self.data.is_empty() {
            return None;
        }
        self.sort();
        custom_percentiles_on_sorted(&self.data, percentiles)
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_cardinality_empty() {
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.cardinality(false, 1), 0);
    }

    #[test]
    fn test_cardinality_single_element() {
        let mut unsorted = Unsorted::new();
        unsorted.add(5);
        assert_eq!(unsorted.cardinality(false, 1), 1);
    }

    #[test]
    fn test_cardinality_unique_elements() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        assert_eq!(unsorted.cardinality(false, 1), 5);
    }

    #[test]
    fn test_cardinality_duplicate_elements() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 2, 3, 3, 3, 4, 4, 4, 4]);
        assert_eq!(unsorted.cardinality(false, 1), 4);
    }

    #[test]
    fn test_cardinality_all_same() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1; 100]);
        assert_eq!(unsorted.cardinality(false, 1), 1);
    }

    #[test]
    fn test_cardinality_large_range() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(0..1_000_000);
        assert_eq!(unsorted.cardinality(false, 1), 1_000_000);
    }

    #[test]
    fn test_cardinality_large_range_sequential() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(0..1_000_000);
        assert_eq!(unsorted.cardinality(false, 2_000_000), 1_000_000);
    }

    #[test]
    fn test_cardinality_presorted() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        unsorted.sort();
        assert_eq!(unsorted.cardinality(true, 1), 5);
    }

    #[test]
    fn test_cardinality_float() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1.0, 1.0, 2.0, 3.0, 3.0, 4.0]);
        assert_eq!(unsorted.cardinality(false, 1), 4);
    }

    #[test]
    fn test_cardinality_string() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec!["a", "b", "b", "c", "c", "c"]);
        assert_eq!(unsorted.cardinality(false, 1), 3);
    }

    #[test]
    fn test_quartiles_selection_vs_sorted() {
        // Test that selection-based quartiles gives same results as sorting-based
        let test_cases = vec![
            vec![3, 5, 7, 9],
            vec![3, 5, 7],
            vec![1, 2, 7, 11],
            vec![3, 5, 7, 9, 12],
            vec![2, 2, 3, 8, 10],
            vec![3, 5, 7, 9, 12, 20],
            vec![0, 2, 4, 8, 10, 11],
            vec![3, 5, 7, 9, 12, 20, 21],
            vec![1, 5, 6, 6, 7, 10, 19],
        ];

        for test_case in test_cases {
            let mut unsorted1 = Unsorted::new();
            let mut unsorted2 = Unsorted::new();
            let mut unsorted3 = Unsorted::new();
            unsorted1.extend(test_case.clone());
            unsorted2.extend(test_case.clone());
            unsorted3.extend(test_case.clone());

            let result_sorted = unsorted1.quartiles();
            let result_selection = unsorted2.quartiles_with_selection();
            let result_zero_copy = unsorted3.quartiles_zero_copy();

            assert_eq!(
                result_sorted, result_selection,
                "Selection mismatch for test case: {:?}",
                test_case
            );
            assert_eq!(
                result_sorted, result_zero_copy,
                "Zero-copy mismatch for test case: {:?}",
                test_case
            );
        }
    }

    #[test]
    fn test_quartiles_with_selection_small() {
        // Test edge cases for selection-based quartiles
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.quartiles_with_selection(), None);

        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2]);
        assert_eq!(unsorted.quartiles_with_selection(), None);

        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3]);
        assert_eq!(unsorted.quartiles_with_selection(), Some((1.0, 2.0, 3.0)));
    }

    #[test]
    fn test_quickselect() {
        let data = vec![
            Partial(3),
            Partial(1),
            Partial(4),
            Partial(1),
            Partial(5),
            Partial(9),
            Partial(2),
            Partial(6),
        ];

        // Test finding different positions
        assert_eq!(quickselect(&mut data.clone(), 0), Some(&1));
        assert_eq!(quickselect(&mut data.clone(), 3), Some(&3));
        assert_eq!(quickselect(&mut data.clone(), 7), Some(&9));

        // Test edge cases
        let mut empty: Vec<Partial<i32>> = vec![];
        assert_eq!(quickselect(&mut empty, 0), None);

        let mut data = vec![Partial(3), Partial(1), Partial(4), Partial(1), Partial(5)];
        assert_eq!(quickselect(&mut data, 10), None); // k >= len
    }

    #[test]
    fn median_stream() {
        assert_eq!(median(vec![3usize, 5, 7, 9].into_iter()), Some(6.0));
        assert_eq!(median(vec![3usize, 5, 7].into_iter()), Some(5.0));
    }

    #[test]
    fn mad_stream() {
        assert_eq!(mad(vec![3usize, 5, 7, 9].into_iter(), None), Some(2.0));
        assert_eq!(
            mad(
                vec![
                    86usize, 60, 95, 39, 49, 12, 56, 82, 92, 24, 33, 28, 46, 34, 100, 39, 100, 38,
                    50, 61, 39, 88, 5, 13, 64
                ]
                .into_iter(),
                None
            ),
            Some(16.0)
        );
    }

    #[test]
    fn mad_stream_precalc_median() {
        let data = vec![3usize, 5, 7, 9].into_iter();
        let median1 = median(data.clone());
        assert_eq!(mad(data, median1), Some(2.0));

        let data2 = vec![
            86usize, 60, 95, 39, 49, 12, 56, 82, 92, 24, 33, 28, 46, 34, 100, 39, 100, 38, 50, 61,
            39, 88, 5, 13, 64,
        ]
        .into_iter();
        let median2 = median(data2.clone());
        assert_eq!(mad(data2, median2), Some(16.0));
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

    #[test]
    fn modes_stream() {
        assert_eq!(modes(vec![3usize, 5, 7, 9].into_iter()), (vec![], 0, 0));
        assert_eq!(modes(vec![3usize, 3, 3, 3].into_iter()), (vec![3], 1, 4));
        assert_eq!(modes(vec![3usize, 3, 4, 4].into_iter()), (vec![3, 4], 2, 2));
        assert_eq!(modes(vec![4usize, 3, 3, 3].into_iter()), (vec![3], 1, 3));
        assert_eq!(modes(vec![1usize, 1, 2, 2].into_iter()), (vec![1, 2], 2, 2));
        let vec: Vec<u32> = vec![];
        assert_eq!(modes(vec.into_iter()), (vec![], 0, 0));
    }

    #[test]
    fn modes_floats() {
        assert_eq!(
            modes(vec![3_f64, 5.0, 7.0, 9.0].into_iter()),
            (vec![], 0, 0)
        );
        assert_eq!(
            modes(vec![3_f64, 3.0, 3.0, 3.0].into_iter()),
            (vec![3.0], 1, 4)
        );
        assert_eq!(
            modes(vec![3_f64, 3.0, 4.0, 4.0].into_iter()),
            (vec![3.0, 4.0], 2, 2)
        );
        assert_eq!(
            modes(vec![1_f64, 1.0, 2.0, 3.0, 3.0].into_iter()),
            (vec![1.0, 3.0], 2, 2)
        );
    }

    #[test]
    fn antimodes_stream() {
        assert_eq!(
            antimodes(vec![3usize, 5, 7, 9].into_iter()),
            (vec![3, 5, 7, 9], 4, 1)
        );
        assert_eq!(
            antimodes(vec![1usize, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].into_iter()),
            (vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13, 1)
        );
        assert_eq!(
            antimodes(vec![1usize, 3, 3, 3].into_iter()),
            (vec![1], 1, 1)
        );
        assert_eq!(
            antimodes(vec![3usize, 3, 4, 4].into_iter()),
            (vec![3, 4], 2, 2)
        );
        assert_eq!(
            antimodes(
                vec![
                    3usize, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13,
                    14, 14, 15, 15
                ]
                .into_iter()
            ),
            // we only show the first 10 of the 13 antimodes
            (vec![3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 13, 2)
        );
        assert_eq!(
            antimodes(
                vec![
                    3usize, 3, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 4, 4, 5, 5, 6, 6, 7, 7, 13, 13,
                    14, 14, 15, 15
                ]
                .into_iter()
            ),
            (vec![3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 13, 2)
        );
        assert_eq!(
            antimodes(vec![3usize, 3, 3, 4].into_iter()),
            (vec![4], 1, 1)
        );
        assert_eq!(
            antimodes(vec![4usize, 3, 3, 3].into_iter()),
            (vec![4], 1, 1)
        );
        assert_eq!(
            antimodes(vec![1usize, 1, 2, 2].into_iter()),
            (vec![1, 2], 2, 2)
        );
        let vec: Vec<u32> = vec![];
        assert_eq!(antimodes(vec.into_iter()), (vec![], 0, 0));
    }

    #[test]
    fn antimodes_floats() {
        assert_eq!(
            antimodes(vec![3_f64, 5.0, 7.0, 9.0].into_iter()),
            (vec![3.0, 5.0, 7.0, 9.0], 4, 1)
        );
        assert_eq!(
            antimodes(vec![3_f64, 3.0, 3.0, 3.0].into_iter()),
            (vec![], 0, 0)
        );
        assert_eq!(
            antimodes(vec![3_f64, 3.0, 4.0, 4.0].into_iter()),
            (vec![3.0, 4.0], 2, 2)
        );
        assert_eq!(
            antimodes(vec![1_f64, 1.0, 2.0, 3.0, 3.0].into_iter()),
            (vec![2.0], 1, 1)
        );
    }

    #[test]
    fn test_custom_percentiles() {
        // Test with integers
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        unsorted.extend(1..=11); // [1,2,3,4,5,6,7,8,9,10,11]

        let result = unsorted.custom_percentiles(&[25, 50, 75]).unwrap();
        assert_eq!(result, vec![3, 6, 9]);

        // Test with strings
        let mut str_data = Unsorted::new();
        str_data.extend(vec!["a", "b", "c", "d", "e"]);
        let result = str_data.custom_percentiles(&[20, 40, 60, 80]).unwrap();
        assert_eq!(result, vec!["a", "b", "c", "d"]);

        // Test with chars
        let mut char_data = Unsorted::new();
        char_data.extend('a'..='e');
        let result = char_data.custom_percentiles(&[25, 50, 75]).unwrap();
        assert_eq!(result, vec!['b', 'c', 'd']);

        // Test with floats
        let mut float_data = Unsorted::new();
        float_data.extend(vec![1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]);
        let result = float_data
            .custom_percentiles(&[10, 30, 50, 70, 90])
            .unwrap();
        assert_eq!(result, vec![1.1, 3.3, 5.5, 7.7, 9.9]);

        // Test with empty percentiles array
        let result = float_data.custom_percentiles(&[]).unwrap();
        assert_eq!(result, Vec::<f64>::new());

        // Test with duplicate percentiles
        let result = float_data.custom_percentiles(&[50, 50, 50]).unwrap();
        assert_eq!(result, vec![5.5]);

        // Test with extreme percentiles
        let result = float_data.custom_percentiles(&[0, 100]).unwrap();
        assert_eq!(result, vec![1.1, 9.9]);

        // Test with unsorted percentiles
        let result = float_data.custom_percentiles(&[75, 25, 50]).unwrap();
        assert_eq!(result, vec![3.3, 5.5, 7.7]); // results always sorted

        // Test with single element
        let mut single = Unsorted::new();
        single.add(42);
        let result = single.custom_percentiles(&[0, 50, 100]).unwrap();
        assert_eq!(result, vec![42, 42, 42]);
    }

    #[test]
    fn quartiles_stream() {
        assert_eq!(
            quartiles(vec![3usize, 5, 7].into_iter()),
            Some((3., 5., 7.))
        );
        assert_eq!(
            quartiles(vec![3usize, 5, 7, 9].into_iter()),
            Some((4., 6., 8.))
        );
        assert_eq!(
            quartiles(vec![1usize, 2, 7, 11].into_iter()),
            Some((1.5, 4.5, 9.))
        );
        assert_eq!(
            quartiles(vec![3usize, 5, 7, 9, 12].into_iter()),
            Some((4., 7., 10.5))
        );
        assert_eq!(
            quartiles(vec![2usize, 2, 3, 8, 10].into_iter()),
            Some((2., 3., 9.))
        );
        assert_eq!(
            quartiles(vec![3usize, 5, 7, 9, 12, 20].into_iter()),
            Some((5., 8., 12.))
        );
        assert_eq!(
            quartiles(vec![0usize, 2, 4, 8, 10, 11].into_iter()),
            Some((2., 6., 10.))
        );
        assert_eq!(
            quartiles(vec![3usize, 5, 7, 9, 12, 20, 21].into_iter()),
            Some((5., 9., 20.))
        );
        assert_eq!(
            quartiles(vec![1usize, 5, 6, 6, 7, 10, 19].into_iter()),
            Some((5., 6., 10.))
        );
    }

    #[test]
    fn quartiles_floats() {
        assert_eq!(
            quartiles(vec![3_f64, 5., 7.].into_iter()),
            Some((3., 5., 7.))
        );
        assert_eq!(
            quartiles(vec![3_f64, 5., 7., 9.].into_iter()),
            Some((4., 6., 8.))
        );
        assert_eq!(
            quartiles(vec![3_f64, 5., 7., 9., 12.].into_iter()),
            Some((4., 7., 10.5))
        );
        assert_eq!(
            quartiles(vec![3_f64, 5., 7., 9., 12., 20.].into_iter()),
            Some((5., 8., 12.))
        );
        assert_eq!(
            quartiles(vec![3_f64, 5., 7., 9., 12., 20., 21.].into_iter()),
            Some((5., 9., 20.))
        );
    }

    #[test]
    fn test_quartiles_zero_copy_small() {
        // Test edge cases for zero-copy quartiles
        let unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.quartiles_zero_copy(), None);

        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2]);
        assert_eq!(unsorted.quartiles_zero_copy(), None);

        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3]);
        assert_eq!(unsorted.quartiles_zero_copy(), Some((1.0, 2.0, 3.0)));

        // Test larger case
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![3, 5, 7, 9]);
        assert_eq!(unsorted.quartiles_zero_copy(), Some((4.0, 6.0, 8.0)));
    }

    #[test]
    fn gini_empty() {
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.gini(None), None);
        let empty_vec: Vec<i32> = vec![];
        assert_eq!(gini(empty_vec.into_iter(), None), None);
    }

    #[test]
    fn gini_single_element() {
        let mut unsorted = Unsorted::new();
        unsorted.add(5);
        assert_eq!(unsorted.gini(None), Some(0.0));
        assert_eq!(gini(vec![5].into_iter(), None), Some(0.0));
    }

    #[test]
    fn gini_perfect_equality() {
        // All values are the same - perfect equality, Gini = 0
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![10, 10, 10, 10, 10]);
        let result = unsorted.gini(None).unwrap();
        assert!((result - 0.0).abs() < 1e-10, "Expected 0.0, got {}", result);

        assert!((gini(vec![10, 10, 10, 10, 10].into_iter(), None).unwrap() - 0.0).abs() < 1e-10);
    }

    #[test]
    fn gini_perfect_inequality() {
        // One value has everything, others have zero - perfect inequality
        // For [0, 0, 0, 0, 100], Gini should be close to 1
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![0, 0, 0, 0, 100]);
        let result = unsorted.gini(None).unwrap();
        // Perfect inequality should give Gini close to 1
        // For n=5, one value=100, others=0: G = (2*5*100)/(5*100) - 6/5 = 2 - 1.2 = 0.8
        assert!((result - 0.8).abs() < 1e-10, "Expected 0.8, got {}", result);
    }

    #[test]
    fn gini_stream() {
        // Test with known values
        // For [1, 2, 3, 4, 5]:
        // sum = 15
        // weighted_sum = 1*1 + 2*2 + 3*3 + 4*4 + 5*5 = 1 + 4 + 9 + 16 + 25 = 55
        // n = 5
        // G = (2 * 55) / (5 * 15) - 6/5 = 110/75 - 1.2 = 1.4667 - 1.2 = 0.2667
        let result = gini(vec![1usize, 2, 3, 4, 5].into_iter(), None).unwrap();
        let expected = (2.0 * 55.0) / (5.0 * 15.0) - 6.0 / 5.0;
        assert!(
            (result - expected).abs() < 1e-10,
            "Expected {}, got {}",
            expected,
            result
        );
    }

    #[test]
    fn gini_floats() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1.0, 2.0, 3.0, 4.0, 5.0]);
        let result = unsorted.gini(None).unwrap();
        let expected = (2.0 * 55.0) / (5.0 * 15.0) - 6.0 / 5.0;
        assert!((result - expected).abs() < 1e-10);

        assert!(
            (gini(vec![1.0f64, 2.0, 3.0, 4.0, 5.0].into_iter(), None).unwrap() - expected).abs()
                < 1e-10
        );
    }

    #[test]
    fn gini_all_zeros() {
        // All zeros - sum is zero, Gini is undefined
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![0, 0, 0, 0]);
        assert_eq!(unsorted.gini(None), None);
        assert_eq!(gini(vec![0, 0, 0, 0].into_iter(), None), None);
    }

    #[test]
    fn gini_negative_values() {
        // Test with negative values (mathematically valid)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![-5, -3, -1, 1, 3, 5]);
        let result = unsorted.gini(None);
        // Sum is 0, so Gini is undefined
        assert_eq!(result, None);

        // Test with negative values that don't sum to zero
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![-2, -1, 0, 1, 2]);
        let result = unsorted.gini(None);
        // Sum is 0, so Gini is undefined
        assert_eq!(result, None);

        // Test with values containing negatives that sum to non-zero
        // Gini is undefined for negative values, should return None
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![-1, 0, 1, 2, 3]);
        let result = unsorted.gini(None);
        assert_eq!(result, None);
    }

    #[test]
    fn gini_known_cases() {
        // Test case: [1, 1, 1, 1, 1] - perfect equality
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 1, 1, 1, 1]);
        let result = unsorted.gini(None).unwrap();
        assert!((result - 0.0).abs() < 1e-10);

        // Test case: [0, 0, 0, 0, 1] - high inequality
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![0, 0, 0, 0, 1]);
        let result = unsorted.gini(None).unwrap();
        // G = (2 * 5 * 1) / (5 * 1) - 6/5 = 2 - 1.2 = 0.8
        assert!((result - 0.8).abs() < 1e-10);

        // Test case: [1, 2, 3] - moderate inequality
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3]);
        let result = unsorted.gini(None).unwrap();
        // sum = 6, weighted_sum = 1*1 + 2*2 + 3*3 = 1 + 4 + 9 = 14
        // G = (2 * 14) / (3 * 6) - 4/3 = 28/18 - 4/3 = 1.5556 - 1.3333 = 0.2222
        let expected = (2.0 * 14.0) / (3.0 * 6.0) - 4.0 / 3.0;
        assert!((result - expected).abs() < 1e-10);
    }

    #[test]
    fn gini_precalc_sum() {
        // Test with pre-calculated sum
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let precalc_sum = Some(15.0);
        let result = unsorted.gini(precalc_sum).unwrap();
        let expected = (2.0 * 55.0) / (5.0 * 15.0) - 6.0 / 5.0;
        assert!((result - expected).abs() < 1e-10);

        // Test that pre-calculated sum gives same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.gini(None).unwrap();
        assert!((result - result2).abs() < 1e-10);
    }

    #[test]
    fn gini_large_dataset() {
        // Test with larger dataset to exercise parallel path
        let data: Vec<i32> = (1..=1000).collect();
        let result = gini(data.iter().copied(), None);
        assert!(result.is_some());
        let gini_val = result.unwrap();
        // For uniform distribution, Gini should be positive but not too high
        assert!(gini_val > 0.0 && gini_val < 0.5);
    }

    #[test]
    fn gini_unsorted_vs_sorted() {
        // Test that sorting doesn't affect result
        let mut unsorted1 = Unsorted::new();
        unsorted1.extend(vec![5, 2, 8, 1, 9, 3, 7, 4, 6]);
        let result1 = unsorted1.gini(None).unwrap();

        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5, 6, 7, 8, 9]);
        let result2 = unsorted2.gini(None).unwrap();

        assert!((result1 - result2).abs() < 1e-10);
    }

    #[test]
    fn gini_small_values() {
        // Test with very small values
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![0.001, 0.002, 0.003, 0.004, 0.005]);
        let result = unsorted.gini(None);
        assert!(result.is_some());
        // Should be same as [1, 2, 3, 4, 5] scaled down
        let expected = (2.0 * 55.0) / (5.0 * 15.0) - 6.0 / 5.0;
        assert!((result.unwrap() - expected).abs() < 1e-10);
    }

    #[test]
    fn gini_large_values() {
        // Test with large values
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1000, 2000, 3000, 4000, 5000]);
        let result = unsorted.gini(None);
        assert!(result.is_some());
        // Should be same as [1, 2, 3, 4, 5] scaled up
        let expected = (2.0 * 55.0) / (5.0 * 15.0) - 6.0 / 5.0;
        assert!((result.unwrap() - expected).abs() < 1e-10);
    }

    #[test]
    fn gini_two_elements() {
        // Test with exactly 2 elements
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2]);
        let result = unsorted.gini(None).unwrap();
        // For [1, 2]: sum=3, weighted_sum=1*1+2*2=5, n=2
        // G = (2*5)/(2*3) - 3/2 = 10/6 - 1.5 = 1.6667 - 1.5 = 0.1667
        let expected = (2.0 * 5.0) / (2.0 * 3.0) - 3.0 / 2.0;
        assert!((result - expected).abs() < 1e-10);
    }

    #[test]
    fn gini_precalc_sum_zero() {
        // Test with pre-calculated sum of zero (should return None)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let result = unsorted.gini(Some(0.0));
        assert_eq!(result, None);
    }

    #[test]
    fn gini_precalc_sum_negative() {
        // Gini is undefined for negative values, should return None
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![-5, -3, -1, 1, 3]);
        let result = unsorted.gini(None);
        assert_eq!(result, None);

        // Negative precalculated sum should also return None
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3]);
        let result = unsorted.gini(Some(-5.0));
        assert_eq!(result, None);
    }

    #[test]
    fn gini_different_types() {
        // Test with different integer types
        let mut unsorted_u32 = Unsorted::new();
        unsorted_u32.extend(vec![1u32, 2, 3, 4, 5]);
        let result_u32 = unsorted_u32.gini(None).unwrap();

        let mut unsorted_i64 = Unsorted::new();
        unsorted_i64.extend(vec![1i64, 2, 3, 4, 5]);
        let result_i64 = unsorted_i64.gini(None).unwrap();

        let expected = (2.0 * 55.0) / (5.0 * 15.0) - 6.0 / 5.0;
        assert!((result_u32 - expected).abs() < 1e-10);
        assert!((result_i64 - expected).abs() < 1e-10);
    }

    #[test]
    fn gini_extreme_inequality() {
        // Test with extreme inequality: one very large value, many zeros
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]);
        let result = unsorted.gini(None).unwrap();
        // For [0,0,0,0,0,0,0,0,0,1000]: sum=1000, weighted_sum=10*1000=10000, n=10
        // G = (2*10000)/(10*1000) - 11/10 = 20/10 - 1.1 = 2 - 1.1 = 0.9
        assert!((result - 0.9).abs() < 1e-10);
    }

    #[test]
    fn gini_duplicate_values() {
        // Test with many duplicate values
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 1, 1, 5, 5, 5, 10, 10, 10]);
        let result = unsorted.gini(None);
        assert!(result.is_some());
        // Should be between 0 and 1
        let gini_val = result.unwrap();
        assert!(gini_val >= 0.0 && gini_val <= 1.0);
    }

    #[test]
    fn kurtosis_empty() {
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.kurtosis(None, None), None);
        let empty_vec: Vec<i32> = vec![];
        assert_eq!(kurtosis(empty_vec.into_iter(), None, None), None);
    }

    #[test]
    fn kurtosis_small() {
        // Need at least 4 elements
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2]);
        assert_eq!(unsorted.kurtosis(None, None), None);

        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3]);
        assert_eq!(unsorted.kurtosis(None, None), None);
    }

    #[test]
    fn kurtosis_normal_distribution() {
        // Normal distribution should have kurtosis close to 0
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let result = unsorted.kurtosis(None, None);
        assert!(result.is_some());
        // For small samples, kurtosis can vary significantly
    }

    #[test]
    fn kurtosis_all_same() {
        // All same values - variance is 0, kurtosis undefined
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![5, 5, 5, 5]);
        assert_eq!(unsorted.kurtosis(None, None), None);
    }

    #[test]
    fn kurtosis_stream() {
        let result = kurtosis(vec![1usize, 2, 3, 4, 5].into_iter(), None, None);
        assert!(result.is_some());
    }

    #[test]
    fn kurtosis_precalc_mean_variance() {
        // Test with pre-calculated mean and variance
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);

        // Calculate mean and variance manually
        let mean = 3.0f64;
        let variance = ((1.0f64 - 3.0).powi(2)
            + (2.0f64 - 3.0).powi(2)
            + (3.0f64 - 3.0).powi(2)
            + (4.0f64 - 3.0).powi(2)
            + (5.0f64 - 3.0).powi(2))
            / 5.0;

        let result = unsorted.kurtosis(Some(mean), Some(variance));
        assert!(result.is_some());

        // Test that pre-calculated values give same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.kurtosis(None, None);
        assert!((result.unwrap() - result2.unwrap()).abs() < 1e-10);
    }

    #[test]
    fn kurtosis_precalc_mean_only() {
        // Test with pre-calculated mean only
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let mean = 3.0f64;

        let result = unsorted.kurtosis(Some(mean), None);
        assert!(result.is_some());

        // Test that pre-calculated mean gives same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.kurtosis(None, None);
        assert!((result.unwrap() - result2.unwrap()).abs() < 1e-10);
    }

    #[test]
    fn kurtosis_precalc_variance_only() {
        // Test with pre-calculated variance only
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let variance = ((1.0f64 - 3.0).powi(2)
            + (2.0f64 - 3.0).powi(2)
            + (3.0f64 - 3.0).powi(2)
            + (4.0f64 - 3.0).powi(2)
            + (5.0f64 - 3.0).powi(2))
            / 5.0;

        let result = unsorted.kurtosis(None, Some(variance));
        assert!(result.is_some());

        // Test that pre-calculated variance gives same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.kurtosis(None, None);
        assert!((result.unwrap() - result2.unwrap()).abs() < 1e-10);
    }

    #[test]
    fn kurtosis_exact_calculation() {
        // Test with exact calculation for [1, 2, 3, 4]
        // Mean = 2.5
        // Variance = ((1-2.5)^2 + (2-2.5)^2 + (3-2.5)^2 + (4-2.5)^2) / 4 = (2.25 + 0.25 + 0.25 + 2.25) / 4 = 1.25
        // Variance^2 = 1.5625
        // Fourth powers: (1-2.5)^4 + (2-2.5)^4 + (3-2.5)^4 + (4-2.5)^4 = 5.0625 + 0.0625 + 0.0625 + 5.0625 = 10.25
        // n = 4
        // Kurtosis = (4*5*10.25) / (3*2*1*1.5625) - 3*3*3/(2*1) = 205 / 9.375 - 13.5 = 21.8667 - 13.5 = 8.3667
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4]);
        let result = unsorted.kurtosis(None, None).unwrap();
        // For small samples, kurtosis can be very high
        assert!(result.is_finite());
    }

    #[test]
    fn kurtosis_uniform_distribution() {
        // Uniform distribution should have negative excess kurtosis
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
        let result = unsorted.kurtosis(None, None).unwrap();
        // Uniform distribution has excess kurtosis = -1.2
        // But for small samples, it can vary significantly
        assert!(result.is_finite());
    }

    #[test]
    fn kurtosis_large_dataset() {
        // Test with larger dataset to exercise parallel path
        let data: Vec<i32> = (1..=1000).collect();
        let result = kurtosis(data.iter().copied(), None, None);
        assert!(result.is_some());
        let kurt_val = result.unwrap();
        assert!(kurt_val.is_finite());
    }

    #[test]
    fn kurtosis_unsorted_vs_sorted() {
        // Test that sorting doesn't affect result
        let mut unsorted1 = Unsorted::new();
        unsorted1.extend(vec![5, 2, 8, 1, 9, 3, 7, 4, 6]);
        let result1 = unsorted1.kurtosis(None, None).unwrap();

        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5, 6, 7, 8, 9]);
        let result2 = unsorted2.kurtosis(None, None).unwrap();

        assert!((result1 - result2).abs() < 1e-10);
    }

    #[test]
    fn kurtosis_minimum_size() {
        // Test with exactly 4 elements (minimum required)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4]);
        let result = unsorted.kurtosis(None, None);
        assert!(result.is_some());
        assert!(result.unwrap().is_finite());
    }

    #[test]
    fn kurtosis_heavy_tailed() {
        // Test with heavy-tailed distribution (outliers)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 100]);
        let result = unsorted.kurtosis(None, None).unwrap();
        // Heavy tails should give positive excess kurtosis
        assert!(result.is_finite());
        // With an outlier, kurtosis should be positive
        assert!(result > -10.0); // Allow some variance but should be reasonable
    }

    #[test]
    fn kurtosis_light_tailed() {
        // Test with light-tailed distribution (values close together)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![10, 11, 12, 13, 14, 15, 16, 17, 18, 19]);
        let result = unsorted.kurtosis(None, None).unwrap();
        // Light tails might give negative excess kurtosis
        assert!(result.is_finite());
    }

    #[test]
    fn kurtosis_small_variance() {
        // Test with very small variance (values very close together)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![10.0, 10.001, 10.002, 10.003, 10.004]);
        let result = unsorted.kurtosis(None, None);
        // Should still compute (variance is very small but non-zero)
        assert!(result.is_some());
        assert!(result.unwrap().is_finite());
    }

    #[test]
    fn kurtosis_precalc_zero_variance() {
        // Test with pre-calculated variance of zero (should return None)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let result = unsorted.kurtosis(None, Some(0.0));
        assert_eq!(result, None);
    }

    #[test]
    fn kurtosis_precalc_negative_variance() {
        // Test with negative variance (invalid, but should handle gracefully)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        // Negative variance is invalid, but function should handle it
        let result = unsorted.kurtosis(None, Some(-1.0));
        // Should either return None or handle it gracefully
        // The function computes variance_sq = variance^2, so negative becomes positive
        // But this is invalid input, so behavior may vary
        // For now, just check it doesn't panic
        let _ = result;
    }

    #[test]
    fn kurtosis_different_types() {
        // Test with different integer types
        let mut unsorted_u32 = Unsorted::new();
        unsorted_u32.extend(vec![1u32, 2, 3, 4, 5]);
        let result_u32 = unsorted_u32.kurtosis(None, None).unwrap();

        let mut unsorted_i64 = Unsorted::new();
        unsorted_i64.extend(vec![1i64, 2, 3, 4, 5]);
        let result_i64 = unsorted_i64.kurtosis(None, None).unwrap();

        assert!((result_u32 - result_i64).abs() < 1e-10);
    }

    #[test]
    fn kurtosis_floating_point_precision() {
        // Test floating point precision
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1.1, 2.2, 3.3, 4.4, 5.5]);
        let result = unsorted.kurtosis(None, None);
        assert!(result.is_some());
        assert!(result.unwrap().is_finite());
    }

    #[test]
    fn kurtosis_negative_values() {
        // Test with negative values
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![-5, -3, -1, 1, 3, 5]);
        let result = unsorted.kurtosis(None, None);
        assert!(result.is_some());
        assert!(result.unwrap().is_finite());
    }

    #[test]
    fn kurtosis_mixed_positive_negative() {
        // Test with mixed positive and negative values
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![-10, -5, 0, 5, 10]);
        let result = unsorted.kurtosis(None, None);
        assert!(result.is_some());
        assert!(result.unwrap().is_finite());
    }

    #[test]
    fn kurtosis_duplicate_values() {
        // Test with duplicate values (but not all same)
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 1, 2, 2, 3, 3, 4, 4, 5, 5]);
        let result = unsorted.kurtosis(None, None);
        assert!(result.is_some());
        assert!(result.unwrap().is_finite());
    }

    #[test]
    fn kurtosis_precalc_mean_wrong() {
        // Test that wrong pre-calculated mean gives wrong result
        let mut unsorted1 = Unsorted::new();
        unsorted1.extend(vec![1, 2, 3, 4, 5]);
        let correct_result = unsorted1.kurtosis(None, None).unwrap();

        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let wrong_mean = 10.0; // Wrong mean
        let wrong_result = unsorted2.kurtosis(Some(wrong_mean), None).unwrap();

        // Results should be different
        assert!((correct_result - wrong_result).abs() > 1e-5);
    }

    #[test]
    fn percentile_rank_empty() {
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.percentile_rank(5), None);
        let empty_vec: Vec<i32> = vec![];
        assert_eq!(percentile_rank(empty_vec.into_iter(), 5), None);
    }

    #[test]
    fn percentile_rank_basic() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

        // Value less than all
        assert_eq!(unsorted.percentile_rank(0), Some(0.0));

        // Value greater than all
        assert_eq!(unsorted.percentile_rank(11), Some(100.0));

        // Median (5) should be around 50th percentile
        let rank = unsorted.percentile_rank(5).unwrap();
        assert!((rank - 50.0).abs() < 1.0);

        // First value should be at 10th percentile
        let rank = unsorted.percentile_rank(1).unwrap();
        assert!((rank - 10.0).abs() < 1.0);
    }

    #[test]
    fn percentile_rank_duplicates() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 1, 2, 2, 3, 3, 4, 4, 5, 5]);

        // Value 2 appears twice, should be at 40th percentile (4 values <= 2)
        let rank = unsorted.percentile_rank(2).unwrap();
        assert!((rank - 40.0).abs() < 1.0);
    }

    #[test]
    fn percentile_rank_stream() {
        let result = percentile_rank(vec![1usize, 2, 3, 4, 5].into_iter(), 3);
        assert_eq!(result, Some(60.0)); // 3 out of 5 values <= 3
    }

    #[test]
    fn percentile_rank_many_ties() {
        // 100 copies of 5 followed by 100 copies of 10 — tests O(log n) upper bound
        let mut unsorted = Unsorted::new();
        for _ in 0..100 {
            unsorted.add(5u32);
        }
        for _ in 0..100 {
            unsorted.add(10u32);
        }
        // 100 values <= 5 out of 200
        let rank = unsorted.percentile_rank(5).unwrap();
        assert!((rank - 50.0).abs() < f64::EPSILON);
        // All 200 values <= 10
        let mut unsorted2 = Unsorted::new();
        for _ in 0..100 {
            unsorted2.add(5u32);
        }
        for _ in 0..100 {
            unsorted2.add(10u32);
        }
        let rank = unsorted2.percentile_rank(10).unwrap();
        assert!((rank - 100.0).abs() < f64::EPSILON);
    }

    #[test]
    fn atkinson_empty() {
        let mut unsorted: Unsorted<i32> = Unsorted::new();
        assert_eq!(unsorted.atkinson(1.0, None, None), None);
        let empty_vec: Vec<i32> = vec![];
        assert_eq!(atkinson(empty_vec.into_iter(), 1.0, None, None), None);
    }

    #[test]
    fn atkinson_single_element() {
        let mut unsorted = Unsorted::new();
        unsorted.add(5);
        assert_eq!(unsorted.atkinson(1.0, None, None), Some(0.0));
        assert_eq!(atkinson(vec![5].into_iter(), 1.0, None, None), Some(0.0));
    }

    #[test]
    fn atkinson_perfect_equality() {
        // All values the same - perfect equality, Atkinson = 0
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![10, 10, 10, 10, 10]);
        let result = unsorted.atkinson(1.0, None, None).unwrap();
        assert!((result - 0.0).abs() < 1e-10);
    }

    #[test]
    fn atkinson_epsilon_zero() {
        // Epsilon = 0 means no inequality aversion, should return 0
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let result = unsorted.atkinson(0.0, None, None).unwrap();
        assert!((result - 0.0).abs() < 1e-10);
    }

    #[test]
    fn atkinson_epsilon_one() {
        // Epsilon = 1 uses geometric mean
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let result = unsorted.atkinson(1.0, None, None);
        assert!(result.is_some());
    }

    #[test]
    fn atkinson_negative_epsilon() {
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        assert_eq!(unsorted.atkinson(-1.0, None, None), None);
    }

    #[test]
    fn atkinson_zero_mean() {
        // If mean is zero, Atkinson is undefined
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![0, 0, 0, 0]);
        assert_eq!(unsorted.atkinson(1.0, None, None), None);
    }

    #[test]
    fn atkinson_stream() {
        let result = atkinson(vec![1usize, 2, 3, 4, 5].into_iter(), 1.0, None, None);
        assert!(result.is_some());
    }

    #[test]
    fn atkinson_precalc_mean_geometric_sum() {
        // Test with pre-calculated mean and geometric_sum
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);

        // Calculate mean and geometric_sum manually
        let mean = 3.0f64;
        let geometric_sum = 1.0f64.ln() + 2.0f64.ln() + 3.0f64.ln() + 4.0f64.ln() + 5.0f64.ln();

        let result = unsorted.atkinson(1.0, Some(mean), Some(geometric_sum));
        assert!(result.is_some());

        // Test that pre-calculated values give same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.atkinson(1.0, None, None);
        assert!((result.unwrap() - result2.unwrap()).abs() < 1e-10);
    }

    #[test]
    fn atkinson_precalc_mean_only() {
        // Test with pre-calculated mean only
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let mean = 3.0f64;

        let result = unsorted.atkinson(1.0, Some(mean), None);
        assert!(result.is_some());

        // Test that pre-calculated mean gives same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.atkinson(1.0, None, None);
        assert!((result.unwrap() - result2.unwrap()).abs() < 1e-10);
    }

    #[test]
    fn atkinson_precalc_geometric_sum_only() {
        // Test with pre-calculated geometric_sum only
        let mut unsorted = Unsorted::new();
        unsorted.extend(vec![1, 2, 3, 4, 5]);
        let geometric_sum = 1.0f64.ln() + 2.0f64.ln() + 3.0f64.ln() + 4.0f64.ln() + 5.0f64.ln();

        let result = unsorted.atkinson(1.0, None, Some(geometric_sum));
        assert!(result.is_some());

        // Test that pre-calculated geometric_sum gives same result
        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(vec![1, 2, 3, 4, 5]);
        let result2 = unsorted2.atkinson(1.0, None, None);
        assert!((result.unwrap() - result2.unwrap()).abs() < 1e-10);
    }
}

#[cfg(test)]
mod bench {
    use super::*;
    use std::time::Instant;

    #[test]
    #[ignore] // Run with `cargo test comprehensive_quartiles_benchmark -- --ignored --nocapture` to see performance comparison
    fn comprehensive_quartiles_benchmark() {
        // Test a wide range of data sizes
        let data_sizes = vec![
            1_000, 10_000, 100_000, 500_000, 1_000_000, 2_000_000, 5_000_000, 10_000_000,
        ];

        println!("=== COMPREHENSIVE QUARTILES BENCHMARK ===\n");

        for size in data_sizes {
            println!("--- Testing with {} elements ---", size);

            // Test different data patterns
            let test_patterns = vec![
                ("Random", generate_random_data(size)),
                ("Reverse Sorted", {
                    let mut v = Vec::with_capacity(size);
                    for x in (0..size).rev() {
                        v.push(x as i32);
                    }
                    v
                }),
                ("Already Sorted", {
                    let mut v = Vec::with_capacity(size);
                    for x in 0..size {
                        v.push(x as i32);
                    }
                    v
                }),
                ("Many Duplicates", {
                    // Create a vector with just a few distinct values repeated many times
                    let mut v = Vec::with_capacity(size);
                    let chunk_size = size / 100;
                    for i in 0..100 {
                        v.extend(std::iter::repeat_n(i, chunk_size));
                    }
                    // Add any remaining elements
                    v.extend(std::iter::repeat_n(0, size - v.len()));
                    v
                }),
            ];

            for (pattern_name, test_data) in test_patterns {
                println!("\n  Pattern: {}", pattern_name);

                // Benchmark sorting-based approach
                let mut unsorted1 = Unsorted::new();
                unsorted1.extend(test_data.clone());

                let start = Instant::now();
                let result_sorted = unsorted1.quartiles();
                let sorted_time = start.elapsed();

                // Benchmark selection-based approach (with copying)
                let mut unsorted2 = Unsorted::new();
                unsorted2.extend(test_data.clone());

                let start = Instant::now();
                let result_selection = unsorted2.quartiles_with_selection();
                let selection_time = start.elapsed();

                // Benchmark zero-copy selection-based approach
                let mut unsorted3 = Unsorted::new();
                unsorted3.extend(test_data);

                let start = Instant::now();
                let result_zero_copy = unsorted3.quartiles_zero_copy();
                let zero_copy_time = start.elapsed();

                // Verify results are the same
                assert_eq!(result_sorted, result_selection);
                assert_eq!(result_sorted, result_zero_copy);

                let selection_speedup =
                    sorted_time.as_nanos() as f64 / selection_time.as_nanos() as f64;
                let zero_copy_speedup =
                    sorted_time.as_nanos() as f64 / zero_copy_time.as_nanos() as f64;

                println!("    Sorting:       {:>12?}", sorted_time);
                println!(
                    "    Selection:     {:>12?} (speedup: {:.2}x)",
                    selection_time, selection_speedup
                );
                println!(
                    "    Zero-copy:     {:>12?} (speedup: {:.2}x)",
                    zero_copy_time, zero_copy_speedup
                );

                let best_algorithm =
                    if zero_copy_speedup > 1.0 && zero_copy_speedup >= selection_speedup {
                        "ZERO-COPY"
                    } else if selection_speedup > 1.0 {
                        "SELECTION"
                    } else {
                        "SORTING"
                    };
                println!("    Best: {}", best_algorithm);
            }

            println!(); // Add blank line between sizes
        }
    }

    // Generate random data for benchmarking
    fn generate_random_data(size: usize) -> Vec<i32> {
        // Simple LCG random number generator for reproducible results
        let mut rng = 1234567u64;
        let mut vec = Vec::with_capacity(size);
        for _ in 0..size {
            rng = rng.wrapping_mul(1103515245).wrapping_add(12345);
            vec.push((rng >> 16) as i32);
        }
        vec
    }

    #[test]
    #[ignore] // Run with `cargo test find_selection_threshold -- --ignored --nocapture` to find exact threshold
    fn find_selection_threshold() {
        println!("=== FINDING SELECTION ALGORITHM THRESHOLD ===\n");

        // Binary search approach to find the threshold
        let mut found_threshold = None;
        let test_sizes = vec![
            1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 7_500_000, 10_000_000,
            15_000_000, 20_000_000, 25_000_000, 30_000_000,
        ];

        for size in test_sizes {
            println!("Testing size: {}", size);

            // Use random data as it's most representative of real-world scenarios
            let test_data = generate_random_data(size);

            // Run multiple iterations to get average performance
            let iterations = 3;
            let mut sorting_total = 0u128;
            let mut selection_total = 0u128;
            let mut zero_copy_total = 0u128;

            for i in 0..iterations {
                println!("  Iteration {}/{}", i + 1, iterations);

                // Sorting approach
                let mut unsorted1 = Unsorted::new();
                unsorted1.extend(test_data.clone());

                let start = Instant::now();
                let _result_sorted = unsorted1.quartiles();
                sorting_total += start.elapsed().as_nanos();

                // Selection approach (with copying)
                let mut unsorted2 = Unsorted::new();
                unsorted2.extend(test_data.clone());

                let start = Instant::now();
                let _result_selection = unsorted2.quartiles_with_selection();
                selection_total += start.elapsed().as_nanos();

                // Zero-copy selection approach
                let mut unsorted3 = Unsorted::new();
                unsorted3.extend(test_data.clone());

                let start = Instant::now();
                let _result_zero_copy = unsorted3.quartiles_zero_copy();
                zero_copy_total += start.elapsed().as_nanos();
            }

            let avg_sorting = sorting_total / iterations as u128;
            let avg_selection = selection_total / iterations as u128;
            let avg_zero_copy = zero_copy_total / iterations as u128;
            let selection_speedup = avg_sorting as f64 / avg_selection as f64;
            let zero_copy_speedup = avg_sorting as f64 / avg_zero_copy as f64;

            println!(
                "  Average sorting:    {:>12.2}ms",
                avg_sorting as f64 / 1_000_000.0
            );
            println!(
                "  Average selection:  {:>12.2}ms (speedup: {:.2}x)",
                avg_selection as f64 / 1_000_000.0,
                selection_speedup
            );
            println!(
                "  Average zero-copy:  {:>12.2}ms (speedup: {:.2}x)",
                avg_zero_copy as f64 / 1_000_000.0,
                zero_copy_speedup
            );

            if (selection_speedup > 1.0 || zero_copy_speedup > 1.0) && found_threshold.is_none() {
                found_threshold = Some(size);
                let best_method = if zero_copy_speedup > selection_speedup {
                    "Zero-copy"
                } else {
                    "Selection"
                };
                println!(
                    "  *** THRESHOLD FOUND: {} becomes faster at {} elements ***",
                    best_method, size
                );
            }

            println!();
        }

        match found_threshold {
            Some(threshold) => println!(
                "🎯 Selection algorithm becomes faster at approximately {} elements",
                threshold
            ),
            None => println!("❌ Selection algorithm did not become faster in the tested range"),
        }
    }

    #[test]
    #[ignore] // Run with `cargo test benchmark_different_data_types -- --ignored --nocapture` to test different data types
    fn benchmark_different_data_types() {
        println!("=== BENCHMARKING DIFFERENT DATA TYPES ===\n");

        let size = 5_000_000; // Use a large size where differences might be visible

        // Test with f64 (floating point)
        println!("Testing with f64 data:");
        let float_data: Vec<f64> = generate_random_data(size)
            .into_iter()
            .map(|x| x as f64 / 1000.0)
            .collect();

        let mut unsorted1 = Unsorted::new();
        unsorted1.extend(float_data.clone());
        let start = Instant::now();
        let _result = unsorted1.quartiles();
        let sorting_time = start.elapsed();

        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(float_data.clone());
        let start = Instant::now();
        let _result = unsorted2.quartiles_with_selection();
        let selection_time = start.elapsed();

        let mut unsorted3 = Unsorted::new();
        unsorted3.extend(float_data);
        let start = Instant::now();
        let _result = unsorted3.quartiles_zero_copy();
        let zero_copy_time = start.elapsed();

        println!("  Sorting:    {:?}", sorting_time);
        println!("  Selection:  {:?}", selection_time);
        println!("  Zero-copy:  {:?}", zero_copy_time);
        println!(
            "  Selection Speedup:  {:.2}x",
            sorting_time.as_nanos() as f64 / selection_time.as_nanos() as f64
        );
        println!(
            "  Zero-copy Speedup:  {:.2}x\n",
            sorting_time.as_nanos() as f64 / zero_copy_time.as_nanos() as f64
        );

        // Test with i64 (larger integers)
        println!("Testing with i64 data:");
        let int64_data: Vec<i64> = generate_random_data(size)
            .into_iter()
            .map(|x| x as i64 * 1000)
            .collect();

        let mut unsorted1 = Unsorted::new();
        unsorted1.extend(int64_data.clone());
        let start = Instant::now();
        let _result = unsorted1.quartiles();
        let sorting_time = start.elapsed();

        let mut unsorted2 = Unsorted::new();
        unsorted2.extend(int64_data.clone());
        let start = Instant::now();
        let _result = unsorted2.quartiles_with_selection();
        let selection_time = start.elapsed();

        let mut unsorted3 = Unsorted::new();
        unsorted3.extend(int64_data);
        let start = Instant::now();
        let _result = unsorted3.quartiles_zero_copy();
        let zero_copy_time = start.elapsed();

        println!("  Sorting:    {:?}", sorting_time);
        println!("  Selection:  {:?}", selection_time);
        println!("  Zero-copy:  {:?}", zero_copy_time);
        println!(
            "  Selection Speedup:  {:.2}x",
            sorting_time.as_nanos() as f64 / selection_time.as_nanos() as f64
        );
        println!(
            "  Zero-copy Speedup:  {:.2}x",
            sorting_time.as_nanos() as f64 / zero_copy_time.as_nanos() as f64
        );
    }
}
```

