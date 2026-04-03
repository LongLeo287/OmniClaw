---
id: quickwit-oss-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:05.383334
---

# KNOWLEDGE EXTRACT: quickwit-oss
> **Extracted on:** 2026-03-30 17:52:20
> **Source:** quickwit-oss

---

## File: `tantivy.md`
```markdown
# 📦 quickwit-oss/tantivy [🔖 PENDING/APPROVE]
🔗 https://github.com/quickwit-oss/tantivy


## Meta
- **Stars:** ⭐ 14798 | **Forks:** 🍴 880
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust

## README (trích đầu)
```
[![Docs](https://docs.rs/tantivy/badge.svg)](https://docs.rs/crate/tantivy/)
[![Build Status](https://github.com/quickwit-oss/tantivy/actions/workflows/test.yml/badge.svg)](https://github.com/quickwit-oss/tantivy/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/quickwit-oss/tantivy/branch/main/graph/badge.svg)](https://codecov.io/gh/quickwit-oss/tantivy)
[![Join the chat at https://discord.gg/MT27AG5EVE](https://shields.io/discord/908281611840282624?label=chat%20on%20discord)](https://discord.gg/MT27AG5EVE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Crates.io](https://img.shields.io/crates/v/tantivy.svg)](https://crates.io/crates/tantivy)

<img src="https://tantivy-search.github.io/logo/tantivy-logo.png" alt="Tantivy, the fastest full-text search engine library written in Rust" height="250">

## Fast full-text search engine library written in Rust

**If you are looking for an alternative to Elasticsearch or Apache Solr, check out [Quickwit](https://github.com/quickwit-oss/quickwit), our distributed search engine built on top of Tantivy.**

Tantivy is closer to [Apache Lucene](https://lucene.apache.org/) than to [Elasticsearch](https://www.elastic.co/products/elasticsearch) or [Apache Solr](https://lucene.apache.org/solr/) in the sense it is not
an off-the-shelf search engine server, but rather a crate that can be used to build such a search engine.

Tantivy is, in fact, strongly inspired by Lucene's design.

## Benchmark

The following [benchmark](https://tantivy-search.github.io/bench/) breaks down the
performance for different types of queries/collections.

Your mileage WILL vary depending on the nature of queries and their load.

Details about the benchmark can be found at this [repository](https://github.com/quickwit-oss/search-benchmark-game).

## Features

- Full-text search
- Configurable tokenizer (stemming available for 17 Latin languages) with third party support for Chinese ([tantivy-jieba](https://crates.io/crates/tantivy-jieba) and [cang-jie](https://crates.io/crates/cang-jie)), Japanese ([lindera](https://github.com/lindera-morphology/lindera-tantivy), [Vaporetto](https://crates.io/crates/vaporetto_tantivy), and [tantivy-tokenizer-tiny-segmenter](https://crates.io/crates/tantivy-tokenizer-tiny-segmenter)) and Korean ([lindera](https://github.com/lindera-morphology/lindera-tantivy) + [lindera-ko-dic-builder](https://github.com/lindera-morphology/lindera-ko-dic-builder))
- Fast (check out the :racehorse: :sparkles: [benchmark](https://tantivy-search.github.io/bench/) :sparkles: :racehorse:)
- Tiny startup time (<10ms), perfect for command-line tools
- BM25 scoring (the same as Lucene)
- Natural query language (e.g. `(michael AND jackson) OR "king of pop"`)
- Phrase queries search (e.g. `"michael jackson"`)
- Incremental indexing
- Multithreaded indexing (indexing English Wikipedia takes < 3 minutes on my desktop)
- Mmap directory
- SIMD integer compressio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

