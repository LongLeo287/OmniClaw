---
id: repo-fetched-arrow-rs-124613
type: knowledge
owner: OA
registered_at: 2026-04-05T03:29:31.476795
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_arrow-rs_124613

## Assimilation Report
Auto-cloned repository: FETCHED_arrow-rs_124613

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Native Rust implementation of Apache Arrow and Apache Parquet

Welcome to the [Rust][rust] implementation of [Apache Arrow], a popular
in-memory columnar format and [Apache Parquet], a popular columnar file
format.

## Community

We welcome participation from everyone and encourage you to join us, ask
questions, help others, and get involved. All participation in the Apache Arrow
project is governed by the Apache Software Foundation's [code of
conduct](https://www.apache.org/foundation/policies/conduct.html).

We use GitHub [issues] and [pull requests] for all technical discussions, reviews,
new features, bug fixes and release coordination. This ensures that all communication
is public and archived for future reference.

The `dev@arrow.apache.org` mailing list is the communication channel for the overall Apache Arrow community.
Instructions for signing up and links to the archives can be found on the [Arrow Community](https://arrow.apache.org/community/) page.

Some community members also use the [Arrow Rust Discord Server](https://discord.gg/YAb2TdazKQ) and the official [ASF Slack](https://s.apache.org/slack-invite) server for informal discussions and coordination.
This is a great place to meet other contributors and get guidance on where to contribute.
However, all technical designs should also be recorded and formalized in GitHub issues, so that they are accessible to everyone.
In Slack, find us in the `#arrow-rust` channel and feel free to ask for an invite via Discord, GitHub issues, or other means.

There is more information in the [contributing] guide.

## Repository Structure

This repository contains the following crates:

| Crate              | Description                                                                  | Latest API Docs                                  | README                            |
| ------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------- |
| [`arrow`]          | Core functionality (memory layout, arrays, low level computations)           | [docs.rs](https://docs.rs/arrow/latest)          | [(README)][arrow-readme]          |
| [`arrow-flight`]   | Support for Arrow-Flight IPC protocol                                        | [docs.rs](https://docs.rs/arrow-flight/latest)   | [(README)][flight-readme]         |
| [`parquet`]        | Support for the [Apache Parquet] columnar file format                        | [docs.rs](https://docs.rs/parquet/latest)        | [(README)][parquet-readme]        |
| [`parquet_derive`] | A crate for deriving RecordWriter/RecordReader for arbitrary, simple structs | [docs.rs](https://docs.rs/parquet-derive/latest) | [(README)][parquet-derive-readme] |

The current development version the API documentation can be found [here](https://arrow.apache.org/rust).

Note: previously the [`object_store`] crate was also part of this repository,
but it has been moved to the [arrow-rs-object-store repository]

[apache arrow]: https://arrow.apache.org/
[apache parquet]: https://parquet.apache.org/
[`arrow`]: https://crates.io/crates/arrow
[`parquet`]: https://crates.io/crates/parquet
[`parquet_derive`]: https://crates.io/crates/parquet-derive
[`arrow-flight`]: https://crates.io/crates/arrow-flight
[arrow-rs-object-store repository]: https://github.com/apache/arrow-rs-object-store

## Release Versioning and Schedule

The Arrow Rust project releases approximately monthly and follows [Semantic
Versioning].

Due to available maintainer and testing bandwidth, [`arrow`] crates ([`arrow`],
[`arrow-flight`], etc.) are released on the same schedule with the same versions
as the [`parquet`] and [`parquet_derive`] crates.

This crate releases every month. We release new major versions (with potentially
breaking API changes) at most once a quarter, and release incremental minor
versions in the intervening months. See [ticket #5368] for more details.

To keep our maintenance burden down, we do regularly scheduled releases (major
and minor) from the `main` branch. How we handle PRs with breaking API changes
is described in the [contributing] guide.

[contributing]: CONTRIBUTING.md#breaking-changes

Planned Release Schedule

| Approximate Date | Version    | Notes                                   |
| ---------------- | ---------- | --------------------------------------- |
| March 2026       | [`58.1.0`] | Minor, NO breaking API changes          |
| April 2026       | [`58.2.0`] | Minor, NO breaking API changes          |
| May 2026         | [`59.0.0`] | Major, potentially breaking API changes |

[`58.1.0`]: https://github.com/apache/arrow-rs/issues/9108
[`58.2.0`]: https://github.com/apache/arrow-rs/issues/9109
[`59.0.0`]: https://github.com/apache/arrow-rs/issues/9110
[ticket #5368]: https://github.com/apache/arrow-rs/issues/5368
[semantic versioning]: https://semver.org/

### Rust Version Compatibility Policy

arrow-rs and parquet are built and tested with stable Rust, and will keep a rolling MSRV (minimum supported Rust version) that can only be updated in major releases on an as needed basis (e.g. project dependencies bump their MSRV or a particular Rust feature is useful for us etc.). The new MSRV if selected will be at least 6 months old. The minor releases are guaranteed to have the same MSRV.

Note: If a Rust hotfix is released for the current MSRV, the MSRV will be updated to the specific minor version that includes all applicable hotfixes preceding other policies.

### Guidelines for `panic` vs `Result`

In general, use panics for bad states that are unreachable, unrecoverable or harmful.
For those caused by invalid user input, however, we prefer to report that invalidity
gracefully as an error result instead of panicking. In general, invalid input should result
in an `Error` as soon as possible. It _is_ ok for code paths after validation to assume
validation has already occurred and panic if not. See [ticket #6737] for more nuances.

[ticket #6737]: https://github.com/apache/arrow-rs/issues/6737

### Deprecation Guidelines

Minor releases may deprecate, but not remove APIs. Deprecating APIs allows
downstream Rust programs to still compile, but generate compiler warnings. This
gives downstream crates time to migrate prior to API removal.

To deprecate an API:

- Mark the API as deprecated using `#[deprecated]` and specify the exact arrow-rs version in which it was deprecated
- Concisely describe the preferred API to help the user transition

The deprecated version is the next version which will be released (please
consult the list above). To mark the API as deprecated, use the
`#[deprecated(since = "...", note = "...")]` attribute.

For example

```rust
#[deprecated(since = "51.0.0", note = "Use `date_part` instead")]
```

In general, deprecated APIs will remain in the codebase for at least two major releases after
they were deprecated (typically between 6 - 9 months later). For example, an API
deprecated in `51.3.0` can be removed in `54.0.0` (or later). Deprecated APIs
may be removed earlier or later than these guidelines at the discretion of the
maintainers.

## Related Projects

There are several related crates in different repositories

| Crate               | Description                                                  | Documentation                      |
| ------------------- | ------------------------------------------------------------ | ---------------------------------- |
| [`object_store`]    | Object Storage (aws, azure, gcp, local, in-memory) interface | [(README)][object_store-readme]    |
| [`datafusion`]      | In-memory query engine with SQL support                      | [(README)][datafusion-readme]      |
| [`ballista`]        | Distributed query execution                                  | [(README)][ballista-readme]        |
| [`parquet_opendal`] | Use [`opendal`] for [`parquet`] Arrow IO                     | [(README)][parquet_opendal-readme] |

[`datafusion`]: https://crates.io/crates/datafusion
[`ballista`]: https://crates.io/crates/ballista
[`parquet_opendal`]: https://crates.io/crates/parquet_opendal
[parquet_opendal-readme]: https://github.com/apache/opendal/blob/main/integrations/parquet/README.md
[object_store-readme]: https://github.com/apache/arrow-rs-object-store/blob/main/README.md

Collectively, these crates support a wider array of functionality for analytic computations in Rust.

For example, you can write SQL queries or a `DataFrame` (using the
[`datafusion`] crate) to read a parquet file (using the [`parquet`] crate),
evaluate it in-memory using Arrow's columnar format (using the [`arrow`] crate),
and send to another process (using the [`arrow-flight`] crate).

Generally speaking, the [`arrow`] crate offers functionality for using Arrow
arrays, and [`datafusion`] offers most operations typically found in SQL,
including `join`s and window functions.

You can find more details about each crate in their respective READMEs.

[rust]: https://www.rust-lang.org/
[`object_store`]: https://crates.io/crates/object-store
[arrow-readme]: arrow/README.md
[contributing]: CONTRIBUTING.md
[parquet-readme]: parquet/README.md
[flight-readme]: arrow-flight/README.md
[datafusion-readme]: https://github.com/apache/datafusion/blob/main/README.md
[ballista-readme]: https://github.com/apache/datafusion-ballista/blob/main/README.md
[parquet-derive-readme]: parquet_derive/README.md
[issues]: https://github.com/apache/arrow-rs/issues
[pull requests]: https://github.com/apache/arrow-rs/pulls
[discussions]: https://github.com/apache/arrow-rs/discussions

```

### File: .github\workflows\README.md
```md
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

The CI is structured so most tests are run in specific workflows:
`arrow.yml` for `arrow`, `parquet.yml` for `parquet` and so on.

The basic idea is to run all tests on pushes to main (to ensure we
keep main green) but run only the individual workflows on PRs that
change files that could affect them.

```

### File: CHANGELOG.md
```md
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Changelog

## [58.1.0](https://github.com/apache/arrow-rs/tree/58.1.0) (2026-03-20)

[Full Changelog](https://github.com/apache/arrow-rs/compare/58.0.0...58.1.0)

**Implemented enhancements:**

- Reuse compression dict lz4\_block [\#9566](https://github.com/apache/arrow-rs/issues/9566)
- \[Variant\] Add `variant_to_arrow` `Struct` type support [\#9529](https://github.com/apache/arrow-rs/issues/9529)
- \[Variant\] Add `unshred_variant` support for `Binary` and `LargeBinary` types [\#9526](https://github.com/apache/arrow-rs/issues/9526)
- \[Variant\] Add `shred_variant` support for `LargeUtf8` and `LargeBinary` types [\#9525](https://github.com/apache/arrow-rs/issues/9525)
- \[Variant\] `variant_get` tests clean up [\#9517](https://github.com/apache/arrow-rs/issues/9517)
- parquet\_variant: Support LargeUtf8 typed value in `unshred_variant` [\#9513](https://github.com/apache/arrow-rs/issues/9513)
- parquet-variant: Support string view typed value in `unshred_variant` [\#9512](https://github.com/apache/arrow-rs/issues/9512)
- Deprecate ArrowTimestampType::make\_value in favor of from\_naive\_datetime [\#9490](https://github.com/apache/arrow-rs/issues/9490) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Followup for support \['fieldName'\] in VariantPath [\#9478](https://github.com/apache/arrow-rs/issues/9478)
- Speedup DELTA\_BINARY\_PACKED decoding when bitwidth is 0 [\#9476](https://github.com/apache/arrow-rs/issues/9476) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)]
- Support CSV files encoded with charsets other than UTF-8 [\#9465](https://github.com/apache/arrow-rs/issues/9465) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Expose Avro writer schema when building the reader [\#9460](https://github.com/apache/arrow-rs/issues/9460) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Python: avoid importing pyarrow classes ever time [\#9438](https://github.com/apache/arrow-rs/issues/9438)
- Add `append_nulls` to `MapBuilder` [\#9431](https://github.com/apache/arrow-rs/issues/9431) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Add `append_non_nulls` to `StructBuilder` [\#9429](https://github.com/apache/arrow-rs/issues/9429) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Add `append_value_n` to GenericByteBuilder [\#9425](https://github.com/apache/arrow-rs/issues/9425) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Optimize `from_bitwise_binary_op` [\#9378](https://github.com/apache/arrow-rs/issues/9378) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Configurable Arrow representation of UTC timestamps for Avro reader [\#9279](https://github.com/apache/arrow-rs/issues/9279) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]

**Fixed bugs:**

- MutableArrayData::extend does not copy child values for ListView arrays [\#9561](https://github.com/apache/arrow-rs/issues/9561) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- ListView interleave bug [\#9559](https://github.com/apache/arrow-rs/issues/9559) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Flight encoding panics with "no dict id for field" with nested dict arrays [\#9555](https://github.com/apache/arrow-rs/issues/9555) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] [[arrow-flight](https://github.com/apache/arrow-rs/labels/arrow-flight)]
- "DeltaBitPackDecoder only supports Int32Type and Int64Type" but unsigned types are supported too [\#9551](https://github.com/apache/arrow-rs/issues/9551) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)]
- Potential overflow when calling `util::bit_mask::set_bits` \(soundness issue\) [\#9543](https://github.com/apache/arrow-rs/issues/9543) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- handle Null type in try\_merge for Struct, List, LargeList, and Union [\#9523](https://github.com/apache/arrow-rs/issues/9523) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Invalid offset in sparse column chunk data for multiple predicates [\#9516](https://github.com/apache/arrow-rs/issues/9516) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)]
- debug\_assert\_eq! in BatchCoalescer panics in debug mode when batch\_size \< 4 [\#9506](https://github.com/apache/arrow-rs/issues/9506) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- Parquet Statistics::null\_count\_opt wrongly returns Some\(0\) when stats are missing [\#9451](https://github.com/apache/arrow-rs/issues/9451) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)]
- Error "Not all children array length are the same!" when decoding rows spanning across page boundaries in parquet file when using `RowSelection` [\#9370](https://github.com/apache/arrow-rs/issues/9370) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)]
- Avro schema resolution not properly supported for complex types [\#9336](https://github.com/apache/arrow-rs/issues/9336) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]

**Documentation updates:**

- Update planned release schedule in README.md [\#9466](https://github.com/apache/arrow-rs/pull/9466) ([alamb](https://github.com/alamb))

**Performance improvements:**

- Introduce `NullBuffer::try_from_unsliced` to simplify array construction [\#9385](https://github.com/apache/arrow-rs/issues/9385) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]
- perf: Coalesce page fetches when RowSelection selects all rows [\#9578](https://github.com/apache/arrow-rs/pull/9578) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([Dandandan](https://github.com/Dandandan))
- Use chunks\_exact for has\_true/has\_false to enable compiler unrolling [\#9570](https://github.com/apache/arrow-rs/pull/9570) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([adriangb](https://github.com/adriangb))
- pyarrow: Cache the imported classes to avoid importing them each time [\#9439](https://github.com/apache/arrow-rs/pull/9439) ([Tpt](https://github.com/Tpt))

**Closed issues:**

- Duplicate macro definition: `partially_shredded_variant_array_gen` [\#9492](https://github.com/apache/arrow-rs/issues/9492)
- Enable `LargeList` / `ListView` / `LargeListView` for `VariantArray::try_new` [\#9455](https://github.com/apache/arrow-rs/issues/9455)
- Support variables/expressions in record\_batch! macro [\#9245](https://github.com/apache/arrow-rs/issues/9245) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)]

**Merged pull requests:**

- \[Variant\] Add unshred\_variant support for Binary and LargeBinary types [\#9576](https://github.com/apache/arrow-rs/pull/9576) ([kunalsinghdadhwal](https://github.com/kunalsinghdadhwal))
- \[Variant\] Add `variant_to_arrow` `Struct` type support [\#9572](https://github.com/apache/arrow-rs/pull/9572) ([sdf-jkl](https://github.com/sdf-jkl))
- Make Sbbf Constructers Public [\#9569](https://github.com/apache/arrow-rs/pull/9569) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([cetra3](https://github.com/cetra3))
- fix: Used `checked_add` for bounds checks to avoid UB [\#9568](https://github.com/apache/arrow-rs/pull/9568) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([etseidl](https://github.com/etseidl))
- Add mutable operations to BooleanBuffer \(Bit\*Assign\) [\#9567](https://github.com/apache/arrow-rs/pull/9567) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([Dandandan](https://github.com/Dandandan))
- chore\(deps\): update lz4\_flex requirement from 0.12 to 0.13 [\#9565](https://github.com/apache/arrow-rs/pull/9565) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([dependabot[bot]](https://github.com/apps/dependabot))
- arrow-select: fix MutableArrayData interleave for ListView [\#9560](https://github.com/apache/arrow-rs/pull/9560) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([asubiotto](https://github.com/asubiotto))
- Move `ValueIter` into own module, and add public `record_count` function [\#9557](https://github.com/apache/arrow-rs/pull/9557) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([Rafferty97](https://github.com/Rafferty97))
- arrow-flight: generate dict\_ids for dicts nested inside complex types [\#9556](https://github.com/apache/arrow-rs/pull/9556) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] [[arrow-flight](https://github.com/apache/arrow-rs/labels/arrow-flight)] ([asubiotto](https://github.com/asubiotto))
- add `shred_variant` support for `LargeUtf8` and `LargeBinary` [\#9554](https://github.com/apache/arrow-rs/pull/9554) ([sdf-jkl](https://github.com/sdf-jkl))
- \[minor\] Download clickbench file when missing [\#9553](https://github.com/apache/arrow-rs/pull/9553) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([Dandandan](https://github.com/Dandandan))
- DeltaBitPackEncoderConversion: Fix panic message on invalid type [\#9552](https://github.com/apache/arrow-rs/pull/9552) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([progval](https://github.com/progval))
- Replace interleave overflow panic with error [\#9549](https://github.com/apache/arrow-rs/pull/9549) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([xudong963](https://github.com/xudong963))
- feat\(arrow-avro\): `HeaderInfo` to expose OCF header [\#9548](https://github.com/apache/arrow-rs/pull/9548) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([mzabaluev](https://github.com/mzabaluev))
- chore: Protect `main` branch with required reviews [\#9547](https://github.com/apache/arrow-rs/pull/9547) ([comphead](https://github.com/comphead))
- Add benchmark for `infer_json_schema` [\#9546](https://github.com/apache/arrow-rs/pull/9546) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([Rafferty97](https://github.com/Rafferty97))
- chore\(deps\): bump black from 24.3.0 to 26.3.1 in /parquet/pytest [\#9545](https://github.com/apache/arrow-rs/pull/9545) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([dependabot[bot]](https://github.com/apps/dependabot))
- Unroll interleave -25-30% [\#9542](https://github.com/apache/arrow-rs/pull/9542) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([Dandandan](https://github.com/Dandandan))
- Optimize `take_fixed_size_binary` For Predefined Value Lengths [\#9535](https://github.com/apache/arrow-rs/pull/9535) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([tobixdev](https://github.com/tobixdev))
- feat: expose arrow schema on async avro reader [\#9534](https://github.com/apache/arrow-rs/pull/9534) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([mzabaluev](https://github.com/mzabaluev))
- Make with\_file\_decryption\_properties pub instead of pub\(crate\) [\#9532](https://github.com/apache/arrow-rs/pull/9532) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([Dandandan](https://github.com/Dandandan))
- fix: handle Null type in try\_merge for Struct, List, LargeList, and Union [\#9524](https://github.com/apache/arrow-rs/pull/9524) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([zhuqi-lucas](https://github.com/zhuqi-lucas))
- chore: extend record\_batch macro to support variables and expressions [\#9522](https://github.com/apache/arrow-rs/pull/9522) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([buraksenn](https://github.com/buraksenn))
- \[Variant\] clean up `variant_get` tests [\#9518](https://github.com/apache/arrow-rs/pull/9518) ([sdf-jkl](https://github.com/sdf-jkl))
- support large string for unshred variant [\#9515](https://github.com/apache/arrow-rs/pull/9515) ([friendlymatthew](https://github.com/friendlymatthew))
- support string view unshred variant [\#9514](https://github.com/apache/arrow-rs/pull/9514) ([friendlymatthew](https://github.com/friendlymatthew))
- Add has\_true\(\) and has\_false\(\) to BooleanArray [\#9511](https://github.com/apache/arrow-rs/pull/9511) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([adriangb](https://github.com/adriangb))
- Fix Invalid offset in sparse column chunk data error for multiple predicates [\#9509](https://github.com/apache/arrow-rs/pull/9509) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([cetra3](https://github.com/cetra3))
- fix: remove incorrect debug assertion in BatchCoalescer  [\#9508](https://github.com/apache/arrow-rs/pull/9508) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([Tim-53](https://github.com/Tim-53))
- \[Json\] Add benchmarks for list json reader [\#9507](https://github.com/apache/arrow-rs/pull/9507) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([liamzwbao](https://github.com/liamzwbao))
- fix: first next\_back\(\) on new RowsIter panics [\#9505](https://github.com/apache/arrow-rs/pull/9505) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([rluvaton](https://github.com/rluvaton))
- Add some benchmarks for decoding delta encoded Parquet [\#9500](https://github.com/apache/arrow-rs/pull/9500) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([etseidl](https://github.com/etseidl))
- chore: remove duplicate macro `partially_shredded_variant_array_gen` [\#9498](https://github.com/apache/arrow-rs/pull/9498) ([codephage2020](https://github.com/codephage2020))
- Deprecate ArrowTimestampType::make\_value in favor of from\_naive\_datetime [\#9491](https://github.com/apache/arrow-rs/pull/9491) [[arrow](https://github.com/apache/arrow-rs/labels/arrow)] ([codephage2020](https://github.com/codephage2020))
- fix: Do not assume missing nullcount stat means zero nullcount [\#9481](https://github.com/apache/arrow-rs/pull/9481) [[parquet](https://github.com/apache/arrow-rs/labels/parquet)] ([scovich](https://github.com/scovich))
- \[Variant\] Enahcne bracket access for VariantPath [\#9479](https://github.com/apache/arrow-rs/pull/9479) ([klion26](https://github.com/klion26))
- Optimize delta binary decoder in the case where bitwidth=0 [\#9477](https://github.com/apache/arrow-rs/pull/9477) [[parquet](https://github.co
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

# Code of Conduct

- [Code of Conduct for The Apache Software Foundation][1]

[1]: https://www.apache.org/foundation/policies/conduct.html

```

### File: CONTRIBUTING.md
```md
<!---
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->

## Introduction

We welcome and encourage contributions of all kinds, such as:

1. Tickets with issue reports of feature requests
2. Documentation improvements
3. Code (PR or PR Review)

In addition to submitting new PRs, we have a healthy tradition of community
members helping review each other's PRs. Doing so is a great way to help the
community as well as get more familiar with Rust and the relevant codebases.

## Finding and Creating Issues to Work On

You can find a curated [good-first-issue] list to help you get started.

Arrow-rs is an open contribution project, and thus there is no particular
project imposed deadline for completing any issue or any restriction on who can
work on an issue, nor how many people can work on an issue at the same time.

Contributors drive the project forward based on their own priorities and
interests and thus you are free to work on any issue that interests you.

If someone is already working on an issue that you want or need but hasn't
been able to finish it yet, you should feel free to work on it as well. In
general it is both polite and will help avoid unnecessary duplication of work if
you leave a note on an issue when you start working on it.

If you want to work on an issue which is not already assigned to someone else
and there are no comment indicating that someone is already working on that
issue then you can assign the issue to yourself by submitting a single word
comment `take`. This will assign the issue to yourself. However, if you are
unable to make progress you should unassign the issue by using the `unassign me`
link at the top of the issue page (and ask for help if are stuck) so that
someone else can get involved in the work.

If you plan to work on a new feature that doesn't have an existing ticket, it is
a good idea to open a ticket to discuss the feature. Advanced discussion often
helps avoid wasted effort by determining early if the feature is a good fit for
Arrow-rs before too much time is invested. It also often helps to discuss your
ideas with the community to get feedback on implementation.

[good-first-issue]: https://github.com/apache/arrow-rs/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22

## Developer's guide to Arrow Rust

### Setting Up Your Build Environment

Install the Rust tool chain:

https://www.rust-lang.org/tools/install

Also, make sure your Rust tool chain is up-to-date, because we always use the latest stable version of Rust to test this project.

```bash
rustup update stable
```

### How to compile

This is a standard cargo project with workspaces. To build it, you need to have `rust` and `cargo`:

```bash
cargo build
```

You can also use rust's official docker image:

```bash
docker run --rm -v $(pwd):/arrow-rs -it rust /bin/bash -c "cd /arrow-rs && rustup component add rustfmt && cargo build"
```

The command above assumes that are in the root directory of the project.

You can also compile specific workspaces:

```bash
cd arrow && cargo build
```

### Git Submodules

Before running tests and examples, it is necessary to set up the local development environment.

The tests rely on test data that is contained in git submodules.

To pull down this data run the following:

```bash
git submodule update --init
```

This populates data in two git submodules:

- `./parquet-testing/data` (sourced from https://github.com/apache/parquet-testing.git)
- `./testing` (sourced from https://github.com/apache/arrow-testing)

By default, `cargo test` will look for these directories at their
standard location. The following environment variables can be used to override the location:

```bash
# Optionally specify a different location for test data
export PARQUET_TEST_DATA=$(cd ./parquet-testing/data; pwd)
export ARROW_TEST_DATA=$(cd ./testing/data; pwd)
```

From here on, this is a pure Rust project and `cargo` can be used to run tests, benchmarks, docs and examples as usual.

## Running the tests

Run tests using the Rust standard `cargo test` command:

```bash
# run all unit and integration tests
cargo test

# run tests for the arrow crate
cargo test -p arrow
```

For some changes, you may want to run additional tests. You can find up-to-date information on the current CI tests in [.github/workflows](https://github.com/apache/arrow-rs/tree/main/.github/workflows). Here are some examples of additional tests you may want to run:

```bash
# run tests for the parquet crate
cargo test -p parquet

# run arrow tests with all features enabled
cargo test -p arrow --all-features

# run the doc tests
cargo test --doc
```

## Code Formatting

Our CI uses `rustfmt` to check code formatting. Before submitting a
PR be sure to run the following and check for lint issues:

```bash
cargo +stable fmt --all -- --check
```

Note that currently the above will not check all source files in the parquet crate. To check all
parquet files run the following from the top-level `arrow-rs` directory:

```bash
cargo fmt -p parquet -- --check --config skip_children=true `find ./parquet -name "*.rs" \! -name format.rs`
```

## Breaking Changes

Our [release schedule] allows breaking API changes only in major releases.
This means that if your PR has a breaking API change, it should be marked as
`api-change` and it will not be merged until development opens for the next
major release. See [this ticket] for details.

[release schedule]: README.md#release-versioning-and-schedule
[this ticket]: https://github.com/apache/arrow-rs/issues/5907

## Clippy Lints

We use `clippy` for checking lints during development, and CI runs `clippy` checks.

Run the following to check for `clippy` lints:

```bash
# run clippy with default settings
cargo clippy --workspace --all-targets --all-features -- -D warnings

```

If you use Visual Studio Code with the `rust-analyzer` plugin, you can enable `clippy` to run each time you save a file. See https://users.rust-lang.org/t/how-to-use-clippy-in-vs-code-with-rust-analyzer/41881.

One of the concerns with `clippy` is that it often produces a lot of false positives, or that some recommendations may hurt readability. We do not have a policy of which lints are ignored, but if you disagree with a `clippy` lint, you may disable the lint and briefly justify it.

Search for `allow(clippy::` in the codebase to identify lints that are ignored/allowed. We currently prefer ignoring lints on the lowest unit possible.

- If you are introducing a line that returns a lint warning or error, you may disable the lint on that line.
- If you have several lints on a function or module, you may disable the lint on the function or module.
- If a lint is pervasive across multiple modules, you may disable it at the crate level.

## Running Benchmarks

Running benchmarks are a good way to test the performance of a change. As benchmarks usually take a long time to run, we recommend running targeted tests instead of the full suite.

```bash
# run all benchmarks
cargo bench

# run arrow benchmarks
cargo bench -p arrow

# run benchmark for the parse_time function within the arrow-cast crate
cargo bench -p arrow-cast --bench parse_time
```

To set the baseline for your benchmarks, use the --save-baseline flag:

```bash
git checkout main

cargo bench --bench parse_time -- --save-baseline main

git checkout feature

cargo bench --bench parse_time -- --baseline main
```

## Git Pre-Commit Hook

We can use [git pre-commit hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) to automate various kinds of git pre-commit checking/formatting.

Suppose you are in the root directory of the project.

First check if the file already exists:

```bash
ls -l .git/hooks/pre-commit
```

If the file already exists, to avoid mistakenly **overriding**, you MAY have to check
the link source or file content. Else if not exist, let's safely soft link [pre-commit.sh](pre-commit.sh) as file `.git/hooks/pre-commit`:

```bash
ln -s  ../../pre-commit.sh .git/hooks/pre-commit
```

If sometimes you want to commit without checking, just run `git commit` with `--no-verify`:

```bash
git commit --no-verify -m "... commit message ..."
```

```

### File: NOTICE.txt
```txt
Apache Arrow
Copyright 2016-2026 The Apache Software Foundation

This product includes software developed at
The Apache Software Foundation (http://www.apache.org/).

This product includes software from the SFrame project (BSD, 3-clause).
* Copyright (C) 2015 Dato, Inc.
* Copyright (c) 2009 Carnegie Mellon University.

This product includes software from the Feather project (Apache 2.0)
https://github.com/wesm/feather

This product includes software from the DyND project (BSD 2-clause)
https://github.com/libdynd

This product includes software from the LLVM project
 * distributed under the University of Illinois Open Source

This product includes software from the google-lint project
 * Copyright (c) 2009 Google Inc. All rights reserved.

This product includes software from the mman-win32 project
 * Copyright https://code.google.com/p/mman-win32/
 * Licensed under the MIT License;

This product includes software from the LevelDB project
 * Copyright (c) 2011 The LevelDB Authors. All rights reserved.
 * Use of this source code is governed by a BSD-style license that can be
 * Moved from Kudu http://github.com/cloudera/kudu

This product includes software from the CMake project
 * Copyright 2001-2009 Kitware, Inc.
 * Copyright 2012-2014 Continuum Analytics, Inc.
 * All rights reserved.

This product includes software from https://github.com/matthew-brett/multibuild (BSD 2-clause)
 * Copyright (c) 2013-2016, Matt Terry and Matthew Brett; all rights reserved.

This product includes software from the Ibis project (Apache 2.0)
 * Copyright (c) 2015 Cloudera, Inc.
 * https://github.com/cloudera/ibis

This product includes software from Dremio (Apache 2.0)
  * Copyright (C) 2017-2018 Dremio Corporation
  * https://github.com/dremio/dremio-oss

This product includes software from Google Guava (Apache 2.0)
  * Copyright (C) 2007 The Guava Authors
  * https://github.com/google/guava

This product include software from CMake (BSD 3-Clause)
  * CMake - Cross Platform Makefile Generator
  * Copyright 2000-2019 Kitware, Inc. and Contributors

The web site includes files generated by Jekyll.

--------------------------------------------------------------------------------

This product includes code from Apache Kudu, which includes the following in
its NOTICE file:

  Apache Kudu
  Copyright 2016 The Apache Software Foundation

  This product includes software developed at
  The Apache Software Foundation (http://www.apache.org/).

  Portions of this software were developed at
  Cloudera, Inc (http://www.cloudera.com/).

--------------------------------------------------------------------------------

This product includes code from Apache ORC, which includes the following in
its NOTICE file:

  Apache ORC
  Copyright 2013-2019 The Apache Software Foundation

  This product includes software developed by The Apache Software
  Foundation (http://www.apache.org/).

  This product includes software developed by Hewlett-Packard:
  (c) Copyright [2014-2015] Hewlett-Packard Development Company, L.P

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for arrow_rs
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\pull_request_template.md
```md
# Which issue does this PR close?

<!--
We generally require a GitHub issue to be filed for all bug fixes and enhancements and this helps us generate change logs for our releases. You can link an issue to this PR using the GitHub syntax.
-->

- Closes #NNN.

# Rationale for this change

<!--
Why are you proposing this change? If this is already explained clearly in the issue then this section is not needed.
Explaining clearly why changes are proposed helps reviewers understand your changes and offer better suggestions for fixes.
-->

# What changes are included in this PR?

<!--
There is no need to duplicate the description in the issue here but it is sometimes worth providing a summary of the individual changes in this PR.
-->

# Are these changes tested?

<!--
We typically require tests for all PRs in order to:
1. Prevent the code from being accidentally broken by subsequent changes
2. Serve as another way to document the expected behavior of the code

If tests are not included in your PR, please explain why (for example, are they covered by existing tests)?
-->

# Are there any user-facing changes?

<!--
If there are user-facing changes then we may require documentation to be updated before approving the PR.

If there are any breaking changes to public APIs, please call them out.
-->

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
<!--
A clear and concise description of what the bug is.
-->

**To Reproduce**
<!--
Steps to reproduce the behavior:
-->

**Expected behavior**
<!--
A clear and concise description of what you expected to happen.
-->

**Additional context**
<!--
Add any other context about the problem here.
-->
```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: ''

---

**Is your feature request related to a problem or challenge? Please describe what you are trying to do.**
<!--
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...] 
(This section helps Arrow developers understand the context and *why* for this feature, in addition to  the *what*)
-->

**Describe the solution you'd like**
<!--
A clear and concise description of what you want to happen.
-->

**Describe alternatives you've considered**
<!--
A clear and concise description of any alternative solutions or features you've considered.
-->

**Additional context**
<!--
Add any other context or screenshots about the feature request here.
-->

```

### File: .github\ISSUE_TEMPLATE\question.md
```md
---
name: Question
about: Ask question about this project
title: ''
labels: question
assignees: ''

---

**Which part is this question about**
<!--
Is it code base, library api, documentation or some other part?
-->

**Describe your question**
<!--
A clear and concise description of what the question is.
-->

**Additional context**
<!--
Add any other context about the problem here.
-->

```

