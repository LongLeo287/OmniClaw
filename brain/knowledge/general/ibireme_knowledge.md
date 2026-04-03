---
id: ibireme-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.012202
---

# KNOWLEDGE EXTRACT: ibireme
> **Extracted on:** 2026-03-30 17:38:09
> **Source:** ibireme

---

## File: `yyjson.md`
```markdown
# 📦 ibireme/yyjson [🔖 PENDING/APPROVE]
🔗 https://github.com/ibireme/yyjson
🌐 https://ibireme.github.io/yyjson/doc/doxygen/html/

## Meta
- **Stars:** ⭐ 3673 | **Forks:** 🍴 307
- **Language:** C | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The fastest JSON library in C

## README (trích đầu)
```

# Introduction

[![Build](https://img.shields.io/github/actions/workflow/status/ibireme/yyjson/checks.yml?branch=master&style=flat-square)](https://github.com/ibireme/yyjson/actions/workflows/checks.yml)
[![Codecov](https://img.shields.io/codecov/c/github/ibireme/yyjson/master?style=flat-square)](https://codecov.io/gh/ibireme/yyjson)
[![License](https://img.shields.io/github/license/ibireme/yyjson?color=blue&style=flat-square)](https://github.com/ibireme/yyjson/blob/master/LICENSE)
[![Version](https://img.shields.io/github/v/release/ibireme/yyjson?color=orange&style=flat-square)](https://github.com/ibireme/yyjson/releases)
[![Packaging status](https://img.shields.io/repology/repositories/yyjson.svg?style=flat-square)](https://repology.org/project/yyjson/versions)

A high performance JSON library written in ANSI C.

# Features
- **Fast**: can read or write gigabytes of JSON data per second on modern CPUs.
- **Portable**: complies with ANSI C (C89), no explicit SIMD.
- **Strict**: complies with [RFC 8259](https://datatracker.ietf.org/doc/html/rfc8259) JSON standard, ensuring strict number formats and UTF-8 validation.
- **Extendable**: offers options to enable individual [JSON5](https://json5.org) features and custom allocator.
- **Accuracy**: can accurately read and write `int64`, `uint64`, and `double` numbers.
- **Flexible**: supports unlimited JSON nesting levels, `\u0000` characters, and non-null-terminated strings.
- **Manipulation**: supports querying and modifying with [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901), [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902), and [JSON Merge Patch](https://datatracker.ietf.org/doc/html/rfc7386).
- **Developer-Friendly**: easy integration with just one `.h` and one `.c` file.

# Limitations
- An array or object is stored as a [data structure](https://ibireme.github.io/yyjson/doc/doxygen/html/data-structures.html) such as linked list, which makes accessing elements by index or key slower than using an iterator.
- Duplicate keys are allowed in an object, and the order of the keys is preserved.
- JSON parsing result is immutable, requiring a `mutable copy` for modification.

# Performance
Benchmark project and dataset: [yyjson_benchmark](https://github.com/ibireme/yyjson_benchmark)

The simdjson's new `On Demand` API is faster if most JSON fields are known at compile-time.
This benchmark project only checks the DOM API, a new benchmark will be added later.

#### AWS EC2 (AMD EPYC 7R32, gcc 9.3)
![ec2_chart](doc/images/perf_reader_ec2.svg)

|twitter.json|parse (GB/s)|stringify (GB/s)|
|---|---|---|
|yyjson(insitu)|1.80|1.51|
|yyjson|1.72|1.42|
|simdjson|1.52|0.61|
|sajson|1.16|   |
|rapidjson(insitu)|0.77|   |
|rapidjson(utf8)|0.26|0.39|
|cjson|0.32|0.17|
|jansson|0.05|0.11|


#### iPhone (Apple A14, clang 12)
![a14_chart](doc/images/perf_reader_a14.svg)

|twitter.json|parse (GB/s)|stringify (GB/s)|
|---|---|---|
|yyjson(insitu)|3.51|2.41|
|yyjson|2.39|2.01|
|simdjson|2.19|0.80|

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

