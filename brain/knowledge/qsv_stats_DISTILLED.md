---
id: qsv-stats
type: knowledge
owner: OA_Triage
---
# qsv-stats
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: CLAUDE.md
```md
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

### File: .claude\settings.json
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$TOOL_INPUT\" | grep -q 'Cargo.lock' && echo 'BLOCK: Do not edit Cargo.lock — this is a library crate' && exit 1 || exit 0",
            "timeout": 5000
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "file=$(echo \"$TOOL_INPUT\" | grep -o '\"file_path\":\"[^\"]*\"' | head -1 | sed 's/\"file_path\":\"//;s/\"//'); if [ -n \"$file\" ] && echo \"$file\" | grep -q '\\.rs$'; then cargo fmt 2>/dev/null; fi",
            "timeout": 10000
          },
          {
            "type": "command",
            "command": "file=$(echo \"$TOOL_INPUT\" | grep -o '\"file_path\":\"[^\"]*\"' | head -1 | sed 's/\"file_path\":\"//;s/\"//'); if [ -n \"$file\" ] && echo \"$file\" | grep -q '\\.rs$'; then cargo test --lib 2>&1 | tail -5; fi",
            "timeout": 60000
          },
          {
            "type": "command",
            "command": "file=$(echo \"$TOOL_INPUT\" | grep -o '\"file_path\":\"[^\"]*\"' | head -1 | sed 's/\"file_path\":\"//;s/\"//'); if [ -n \"$file\" ] && echo \"$file\" | grep -q '\\.rs$'; then cargo clippy --lib 2>&1 | grep 'warning\\|error' | head -10; fi",
            "timeout": 30000
          }
        ]
      }
    ]
  }
}

```

### File: src\frequency.rs
```rs
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

### File: src\lib.rs
```rs
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

### File: src\minmax.rs
```rs
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
        assert_
... [TRUNCATED]
```

### File: src\online.rs
```rs
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

  
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
