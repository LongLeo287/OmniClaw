---
id: github.com-open-telemetry-opentelemetry-proto-e503
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:08.147563
---

# KNOWLEDGE EXTRACT: github.com_open-telemetry_opentelemetry-proto_e5039b5f
> **Extracted on:** 2026-04-01 14:12:14
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523762/github.com_open-telemetry_opentelemetry-proto_e5039b5f

---

## File: `.gitattributes`
```
* text=auto eol=lf
```

## File: `.gitignore`
```
# IntelliJ IDEA
.idea
*.iml

# VS Code
.vscode
.classpath
.project
.settings/

# OS X
.DS_Store

# Emacs
*~
\#*\#

# Vim
.swp

# Generated code
/gen/

node_modules
```

## File: `.lychee.toml`
```
include_fragments = true

exclude = [
    # excluding links to pull requests and issues is done for performance
    "^https://github.com/open-telemetry/opentelemetry-proto/(pull|issue)/\\d+$"
]

# better to be safe and avoid failures
max_retries = 6
```

## File: `.markdownlint.yaml`
```yaml
# See https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md
# and https://github.com/DavidAnson/markdownlint/blob/main/README.md

# Default state for all rules
default: true

ul-style: false
line-length: false
no-duplicate-header:
  siblings_only: true
ol-prefix:
  style: ordered
no-inline-html: false
fenced-code-language: false
MD024: false
MD059: false
```

## File: `CHANGELOG.md`
```markdown
# Changelog

The full list of changes can be found in the compare view for the respective release at <https://github.com/open-telemetry/opentelemetry-proto/releases>.

## Unreleased

### Added

### Changed

### Fixed

### Removed

## 1.10.0 - 2026-03-09

### Added

- profiles: introduce reference based attributes [#733](https://github.com/open-telemetry/opentelemetry-proto/pull/733)

### Changed

- docs: Add more clarity to experiments. [#771](https://github.com/open-telemetry/opentelemetry-proto/pull/771)
- profiles: clarify Sample message usage guidance docs. [#742](https://github.com/open-telemetry/opentelemetry-proto/pull/742)
- profiles: improve Sample message clarity and usage documentation. [#724](https://github.com/open-telemetry/opentelemetry-proto/pull/724)
- profiles: clarify the profile and sample timestamps relationship. [#744](https://github.com/open-telemetry/opentelemetry-proto/pull/744)
- common: rename ref suffix to strindex [#768](https://github.com/open-telemetry/opentelemetry-proto/pull/768)

### Fixed

- examples: Represent uint64 and fixed64 fields as strings in metrics.json. [#748](https://github.com/open-telemetry/opentelemetry-proto/pull/748)
- logs: `SEVERITY_NUMBER_UNSPECIFIED` can be used as the `severity_number` field is optional. [#736](https://github.com/open-telemetry/opentelemetry-proto/pull/736)

## 1.9.0 - 2025-10-31

### Added

- profiles: drop field profile.comment_strindices. [#729](https://github.com/open-telemetry/opentelemetry-proto/pull/729)
- profiles: clarify the original payload field comments. [#722](https://github.com/open-telemetry/opentelemetry-proto/pull/722)
- profiles: add a note about cardinality implications for attribute values. [#713](https://github.com/open-telemetry/opentelemetry-proto/pull/713)

### Changed

- profiles: clarify dictionary guidelines: duplicates and other restrictions. [#732](https://github.com/open-telemetry/opentelemetry-proto/pull/732)
- profiles: clarify the original payload field comments. [#722](https://github.com/open-telemetry/opentelemetry-proto/pull/722)
- profiles: rename line -> lines and sample -> samples since they are repeated fields. [#712](https://github.com/open-telemetry/opentelemetry-proto/pull/712)
- profiles: document more explicitly the dictionary zero element requirement. [#711](https://github.com/open-telemetry/opentelemetry-proto/pull/711)
- all: drop attribute values restrictions. [#707](https://github.com/open-telemetry/opentelemetry-proto/pull/707)<br>
  ⚠️ **IMPORTANT**: OTLP consumers are expected to accept attribute values that were previously considered invalid.
  All attributes can now contain:
  - empty values,
  - bytes values,
  - array values different than array of string values, bool values, int values, double values,
  - kvlist values.

### Fixed

- all: fix schema_url comments to include scope field coverage. [#727](https://github.com/open-telemetry/opentelemetry-proto/pull/727)
- all: add missing field comments. [#717](https://github.com/open-telemetry/opentelemetry-proto/pull/717)

### Removed

- profiles: drop field profile.comment_strindices. [#729](https://github.com/open-telemetry/opentelemetry-proto/pull/729)
- profiles: remove aggregation temporality enum and field. [#710](https://github.com/open-telemetry/opentelemetry-proto/pull/710)

## 1.8.0 - 2025-09-02

### Changed

- profiles: drop gzip requirement. [#661](https://github.com/open-telemetry/opentelemetry-proto/pull/661)
- profiles: avoid `optional` keyword usage. [#659](https://github.com/open-telemetry/opentelemetry-proto/pull/659)
- profiles: make `profile_id` optional. [#665](https://github.com/open-telemetry/opentelemetry-proto/pull/665)
- profiles: use single `Profile.sample_type` and clarify use of timestamps. [#649](https://github.com/open-telemetry/opentelemetry-proto/pull/649)
- all: add notes about the attribute values restrictions. [#683](https://github.com/open-telemetry/opentelemetry-proto/pull/683)<br>
  ⚠️ **IMPORTANT**: These restrictions can be dropped in a future minor release.
- profiles: clarify usage of the zero value as the first element of tables in `ProfilesDictionary`. [#688](https://github.com/open-telemetry/opentelemetry-proto/pull/688), [#698](https://github.com/open-telemetry/opentelemetry-proto/pull/698)
- profiles: unsigned `time_nanos` and `duration_nanos` in `Profile`. [#692](https://github.com/open-telemetry/opentelemetry-proto/pull/692)
- profiles: improve attribute encoding in `ProfilesDictionary`. [#672](https://github.com/open-telemetry/opentelemetry-proto/pull/672)
- profiles: simplify profile stack trace representation. [#708](https://github.com/open-telemetry/opentelemetry-proto/pull/708)

### Fixed

- examples: fix OTLP JSON Event example body. [#666](https://github.com/open-telemetry/opentelemetry-proto/pull/666)
- docs: minor specification fixes around `UNAVAILABLE` and `RetryInfo`. [#669](https://github.com/open-telemetry/opentelemetry-proto/pull/669)

### Removed

- profiles: remove `default_sample_type`. [#679](https://github.com/open-telemetry/opentelemetry-proto/pull/679)
- profiles: remove `has_*` debug info fields, they are moving to attributes. [#595](https://github.com/open-telemetry/opentelemetry-proto/pull/595)
- profiles: remove `Location.is_folded`. [#690](https://github.com/open-telemetry/opentelemetry-proto/pull/690)

## 1.7.0 - 2025-05-19

### Added

- profiles: introduce Dictionary message in ProfilesData, and move the lookup tables into it. [#650](https://github.com/open-telemetry/opentelemetry-proto/pull/650)

## 1.6.0 - 2025-04-29

### Added

- resource: Add EntityRef. [#635](https://github.com/open-telemetry/opentelemetry-proto/pull/635)

### Changed

- logs: Stabilize `event_name` field in `LogRecord` message. [#643](https://github.com/open-telemetry/opentelemetry-proto/pull/643)
- profiles: Move the lookup tables to ProfilesData. [#644](https://github.com/open-telemetry/opentelemetry-proto/pull/644)
- profiles: Move default sample_type from the string table to sample_type. [#620](https://github.com/open-telemetry/opentelemetry-proto/pull/620)

## 1.5.0 - 2024-12-12

### Added

- all: Add note about `schema_url` format (including version). [#605](https://github.com/open-telemetry/opentelemetry-proto/pull/605)
- logs: Add top-level `event_name` field to log records instead of `event.name` attribute. [#600](https://github.com/open-telemetry/opentelemetry-proto/pull/600)

### Removed

- profiles: Remove unused `Label` definition. [#602](https://github.com/open-telemetry/opentelemetry-proto/pull/602)
- profiles: drop duplicate `attributes` field in message Profile. [#606](https://github.com/open-telemetry/opentelemetry-proto/pull/606)

## 1.4.0 - 2024-11-20

### Added

* metrics: Add resource attributes and scope to metrics proto diagram. [#519](https://github.com/open-telemetry/opentelemetry-proto/pull/519)
* metrics: Added json example for exponential histogram. [#580](https://github.com/open-telemetry/opentelemetry-proto/pull/580)

### Changed

* metrics: Clarify aggregation temporality for Summary metric type. [#591](https://github.com/open-telemetry/opentelemetry-proto/pull/591)
* docs: Remove HTTP 1.1 restriction from Protocol Details [#571](https://github.com/open-telemetry/opentelemetry-proto/pull/571)
* docs: Update specification to include development profiles [#582](https://github.com/open-telemetry/opentelemetry-proto/pull/582)
* docs: update references to logging exporter [#581](https://github.com/open-telemetry/opentelemetry-proto/pull/581)
* Makefile: exclude Profiles protocol from breaking-changes [#576](https://github.com/open-telemetry/opentelemetry-proto/pull/576)
* Makefile: exclude Profiles service from breaking changes too [#586](https://github.com/open-telemetry/opentelemetry-proto/pull/586/)
* profiles: align type of index into string table [#557](https://github.com/open-telemetry/opentelemetry-proto/pull/557)
* profiles: drop Sample.stacktrace_id_index [#575](https://github.com/open-telemetry/opentelemetry-proto/pull/575)
* profiles: drop BuildIdKind [#584](https://github.com/open-telemetry/opentelemetry-proto/pull/584)
* profiles: drop Sample.label [#583](https://github.com/open-telemetry/opentelemetry-proto/pull/583)
* profiles: drop Location.type_index [#578](https://github.com/open-telemetry/opentelemetry-proto/pull/578)
* profiles: Rename profiles v1experimental to v1development [#585](https://github.com/open-telemetry/opentelemetry-proto/pull/585)
* profiles: Make mapping in Profile optional [#556](https://github.com/open-telemetry/opentelemetry-proto/pull/556)
* profiles: Fold the content of pprofextended.proto into profiles.proto, removing ProfileContainer. [#590](https://github.com/open-telemetry/opentelemetry-proto/pull/590)
* profiles: Improve lookup table pattern use in profiles. [#592](https://github.com/open-telemetry/opentelemetry-proto/pull/592)
* profiles: Renovations to experimental profiling schema. [#596](https://github.com/open-telemetry/opentelemetry-proto/pull/596)

## 1.3.2 - 2024-06-28

### Changed

* profiles: add missing java_package option to pprofextended. [#558](https://github.com/open-telemetry/opentelemetry-proto/pull/558)

## 1.3.1 - 2024-05-07

### Changed

* profiles: fix versioning in selector. [#551](https://github.com/open-telemetry/opentelemetry-proto/pull/551)

## 1.3.0 - 2024-04-24

### Added

* Add new profile signal.
  [#534](https://github.com/open-telemetry/opentelemetry-proto/pull/534)

## 1.2.0 - 2024-03-29

### Added

* Indicate if a `Span`'s parent or link is remote using 2 bit flag.
  [#484](https://github.com/open-telemetry/opentelemetry-proto/pull/484)
* Add metric.metadata for supporting additional metadata on metrics
  [#514](https://github.com/open-telemetry/opentelemetry-proto/pull/514)
* Add example of an Event [#538](https://github.com/open-telemetry/opentelemetry-proto/pull/538)

### Changed

## 1.1.0 - 2024-01-10

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v1.0.0...v1.1.0).

### Added

* Add `flags` field to `Span` and `Span/Link` for W3C-specified Trace Context flags.
  [#503](https://github.com/open-telemetry/opentelemetry-proto/pull/503)

### Changed

* Update and fix OTLP JSON examples. [#516](https://github.com/open-telemetry/opentelemetry-proto/pull/516),
  [#510](https://github.com/open-telemetry/opentelemetry-proto/pull/510),
  [#499](https://github.com/open-telemetry/opentelemetry-proto/pull/499)
* Remove irrelevant comments from metric name field. [#512](https://github.com/open-telemetry/opentelemetry-proto/pull/512)
* Add comment to explain schema_url fields. [#504](https://github.com/open-telemetry/opentelemetry-proto/pull/504)

## 1.0.0 - 2023-07-03

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.20.0...v1.0.0).

### Maturity

* Add note about the possibility to have unstable components after 1.0.0
  [#489](https://github.com/open-telemetry/opentelemetry-proto/pull/489)
* Add maturity JSON entry per package
  [#490](https://github.com/open-telemetry/opentelemetry-proto/pull/490)

## 0.20.0 - 2023-06-06

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.19.0...v0.20.0).

### Maturity

* Declare OTLP/JSON Stable.
  [#436](https://github.com/open-telemetry/opentelemetry-proto/pull/436)
  [#435](https://github.com/open-telemetry/opentelemetry-proto/pull/435)
* Provide stronger symbolic stability guarantees.
  [#432](https://github.com/open-telemetry/opentelemetry-proto/pull/432)
* Clarify how additive changes are handled.
  [#455](https://github.com/open-telemetry/opentelemetry-proto/pull/455)

### Changed

* Change the exponential histogram boundary condition.
  [#409](https://github.com/open-telemetry/opentelemetry-proto/pull/409)
* Clarify behavior for empty/not present/invalid trace_id and span_id fields.
  [#442](https://github.com/open-telemetry/opentelemetry-proto/pull/442)
* Change the collector trace endpoint to /v1/traces.
  [#449](https://github.com/open-telemetry/opentelemetry-proto/pull/449)

### Added

* Introduce `zero_threshold` field to `ExponentialHistogramDataPoint`.
  [#441](https://github.com/open-telemetry/opentelemetry-proto/pull/441)
  [#453](https://github.com/open-telemetry/opentelemetry-proto/pull/453)

### Removed

* Delete requirement to generate new trace/span id if an invalid id is received.
  [#444](https://github.com/open-telemetry/opentelemetry-proto/pull/444)

## 0.19.0 - 2022-08-03

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.18.0...v0.19.0).

### Changed

* Add `csharp_namespace` option to protos.
  ([#399](https://github.com/open-telemetry/opentelemetry-proto/pull/399))
* Fix some out-of-date urls which link to [specification](https://github.com/open-telemetry/opentelemetry-specification). ([#402](https://github.com/open-telemetry/opentelemetry-proto/pull/402))
* :stop_sign: [BREAKING] Delete deprecated InstrumentationLibrary,
  InstrumentationLibraryLogs, InstrumentationLibrarySpans and
  InstrumentationLibraryMetrics messages. Delete deprecated
  instrumentation_library_logs, instrumentation_library_spans and
  instrumentation_library_metrics fields.

### Added

* Introduce Scope Attributes. [#395](https://github.com/open-telemetry/opentelemetry-proto/pull/395)
* Introduce partial success fields in `Export<signal>ServiceResponse`.
 [#414](https://github.com/open-telemetry/opentelemetry-proto/pull/414)

## 0.18.0 - 2022-05-17

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.17.0...v0.18.0).

### Changed

* Declare logs Stable.
  [(#376)](https://github.com/open-telemetry/opentelemetry-proto/pull/376)
* Metrics ExponentialHistogramDataPoint makes the `sum` optional
  (follows the same change in HistogramDataPOint in 0.15). [#392](https://github.com/open-telemetry/opentelemetry-proto/pull/392)

## 0.17.0 - 2022-05-06

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.16.0...v0.17.0).

### Changed

* Introduce optional `min` and `max` fields to the Histogram and ExponentialHistogram data points.
  [(#279)](https://github.com/open-telemetry/opentelemetry-proto/pull/279)

## 0.16.0 - 2022-03-31

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.15.0...v0.16.0).

### Removed

* Remove deprecated LogRecord.Name field (#373).

## 0.15.0 - 2022-03-19

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.14.0...v0.15.0).

### Changed

* Rename InstrumentationLibrary to InstrumentationScope (#362)

### Added

* Use optional for `sum` field to mark presence (#366)

## 0.14.0 - 2022-03-08

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.13.0...v0.14.0).

### Removed

* Deprecate LogRecord.Name field (#357)

## 0.13.0 - 2022-02-10

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.12.0...v0.13.0).

### Changed

* `Swagger` generation updated to `openapiv2` due to the use of an updated version of protoc in `otel/build-protobuf`
* Clarify attribute key uniqueness requirement (#350)
* Fix path to Go packages (#360)

### Added

* Add ObservedTimestamp to LogRecord. (#351)
* Add native kotlin support (#337)

### Removed

* Remove unused deprecated message StringKeyValue (#358)
* Remove experimental metrics config service (#359)

## 0.12.0 - 2022-01-19

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.11.0...v0.12.0).

### Changed

* Rename logs to log_records in InstrumentationLibraryLogs. (#352)

### Removed

* Remove deprecated messages and fields from traces. (#341)
* Remove deprecated messages and fields from metrics. (#342)

## 0.11.0 - 2021-10-07

Full list of differences found in [this compare](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.10.0...v0.11.0).

### Added

* ExponentialHistogram is a base-2 exponential histogram described in [OTEP 149](https://github.com/open-telemetry/oteps/pull/149). (#322)
* Adds `TracesData`, `MetricsData`, and `LogsData` container types for common use
  in transporting multiple `ResourceSpans`, `ResourceMetrics`, and `ResourceLogs`. (#332)

## 0.10.0 - 2021-09-07

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.9.0...v0.10.0)

### Maturity

* `collector/logs/*` is now considered `Beta`. (#311)
* `logs/*` is now considered `Beta`. (#311)

### Added

* Metrics data points add a `flags` field with one bit to represent explicitly missing data. (#316)

## 0.9.0 - 2021-04-12

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.8.0...v0.9.0)

### Maturity

* `collector/metrics/*` is now considered `stable`. (#305)

### Changed: Metrics

* :stop_sign: [DATA MODEL CHANGE] Histogram/Summary sums must be monotonic counters of events (#302)
* :stop_sign: [DATA MODEL CHANGE] Clarify requirements and semantics for start time (#295)
* :stop_sign: [BREAKING] Deprecate `labels` field from NumberDataPoint, HistogramDataPoint, SummaryDataPoint and add equivalent `attributes` field (#283)
* :stop_sign: [BREAKING] Deprecate `filtered_labels` field from Exemplars and add equivalent `filtered_attributes` field (#283)

### Added

- Common - Add bytes (binary) as data type to AnyValue (#297)
- Common - Add schema_url fields as described in OTEP 0152 (#298)

### Removed

* Remove if no changes for this section before release.

## 0.8.0 - 2021-03-23

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.7.0...v0.8.0)

### Historical breaking change notice

Release 0.8 was the last in the line of releases marked as "unstable".
This release broke compatibility in more ways than were recognized and
documented at the time of its release.  In particular, #278 created
the `NumberDataPoint` type and used it in several locations in place
of the former `DoubleDataPoint`.  The new `oneof` in `NumberDataPoint`
re-used the former `DoubleDataPoint` tag number, which means that
pre-0.8 `DoubleSum` and `DoubleGauge` points would parse correctly as
a 0.8 `Sum` and `Gauge` points containing double-valued numbers.

However, by virtue of a `syntax = "proto3"` declaration, the protocol
compiler for all versions of OTLP have not included field presence,
which means 0 values are not serialized.  **The result is that valid
OTLP 0.7 `DoubleSum` and `DoubleGauge` points would not parse
correctly as OTLP 0.8 data.**  Instead, they parse as
`NumberDataPoint` with a missing value in the `oneof` field.

### Changed: Metrics

* :stop_sign: [DEPRECATION] Deprecate IntSum, IntGauge, and IntDataPoint (#278)
* :stop_sign: [DEPRECATION] Deprecate IntExemplar (#281)
* :stop_sign: [DEPRECATION] Deprecate IntHistogram (#270)
* :stop_sign: [BREAKING] Rename DoubleGauge to Gauge (#278)
* :stop_sign: [BREAKING] Rename DoubleSum to Sum (#278)
* :stop_sign: [BREAKING] Rename DoubleDataPoint to NumberDataPoint (#278)
* :stop_sign: [BREAKING] Rename DoubleSummary to Summary (#269)
* :stop_sign: [BREAKING] Rename DoubleExemplar to Exemplar (#281)
* :stop_sign: [BREAKING] Rename DoubleHistogram to Histogram (#270)
* :stop_sign: [DATA MODEL CHANGE] Make explicit bounds compatible with OM/Prometheus (#262)

## 0.7.0 - 2021-01-28

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.6.0...v0.7.0)

### Maturity

$$$Protobuf Encodings:**

* `collector/metrics/*` is now considered `Beta`. (#223)
* `collector/logs/*` is now considered `Alpha`. (#228)
* `logs/*` is now considered `Alpha`. (#228)
* `metrics/*` is now considered `Beta`. (#223)

### Changed

* Common/Logs/Metrics/Traces - Clarify empty instrumentation (#245)

### Added

* Metrics - Add SummaryDataPoint support to Metrics proto (#227)

## 0.6.0 - 2020-10-28

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.5.0...v0.6.0)

### Maturity

* Clarify maturity guarantees (#225)

### Changed

* Traces - Deprecated old Span status code and added a new status code according to specification (#224)
** Marked for removal `2021-10-22` given Stability Guarantees.
* Rename ProbabilitySampler to TraceIdRatioBased (#221)

## 0.5.0 - 2020-08-31

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.4.0...v0.5.0)

### Maturity Changes

**Protobuf Encodings:**

* `collector/trace/*` is now `Stable`.
* `common/*` is now `Stable`.
* `resource/*` is now `Stable`.
* `trace/trace.proto` is now `Stable`. (#160)

**JSON Encodings:**

* All messages are now `Alpha`.

### Changed

* :stop_sign: [BREAKING] Metrics - protocol was refactored, and lots of breaking changes.
  * Removed MetricDescriptor and embedded into Metric and the new data types.
  * Add new data types Gauge/Sum/Histogram.
  * Make use of the "AggregationTemporality" into the data types that allow that support.
* Rename enum values to follow the proto3 style guide.

### Added

* Enable build to use docker image otel/build-protobuf to be used in CI.
** Can also be used by the languages to generate protos.

### Removed

* :stop_sign: [BREAKING] Remove generated golang structs from the repository

### Errata

The following was announced in the release, but has not yet been considered stable. Please see the latest
README.md for actual status.

> This is a Release Candidate to declare Metrics part of the protocol Stable.

## 0.4.0 - 2020-06-23

Full list of differences found in [this compare.](https://github.com/open-telemetry/opentelemetry-proto/compare/v0.3.0...v0.4.0)

### Changed

* Metrics - Add temporality to MetricDescriptor (#140).

### Added

* Metrics - Add Monotonic Types (#145)
* Common/Traces - Added support for arrays and maps for attribute values (AnyValue) (#157).

### Removed

* :stop_sign: [BREAKING] Metrics - Removed common labels from MetricDescriptor (#144).

### Errata

The following was announced in the release, but this was not considered Stable until `v0.5.0`

> This is a Release Candidate to declare Traces part of the protocol Stable.

## 0.3.0 - 2020-03-23

* Initial protos for trace, metrics, resource and OTLP.
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

## Introduction

Welcome, and thank you for your interest in contributing to the OpenTelemetry Protocol (OTLP) Specification! Your contributions — big or small — are invaluable in shaping and improving this essential part of the OpenTelemetry ecosystem.

Whether you are fixing a small issue, updating documentation, or introducing a major improvement, we appreciate your efforts.
If you're new to the project, don't hesitate to ask questions and seek guidance from the community.
We are here to support you!

Before contributing, we encourage you to read the OpenTelemetry project [contributing
guide](https://github.com/open-telemetry/community/blob/main/guides/contributor/README.md)
for general information about the project.

## Prerequisites

- `Docker`

## Making changes to the .proto files

After making any changes to .proto files make sure to generate all
implementation by running `make gen-all`.

## Style-Guide

OpenTelemetry follows the [protocol buffer style guide](https://protobuf.dev/programming-guides/style/) with the following clarifications:

- All Messages and fields should be documented via comments.
- Field comments should document purpose or behavior with active verbs, or
  a simple definition noun phrase (similar to a dictionary entry).
  - valid: "Represents ..."
    valid: "Additional attributes that describe the scope."
  - not-valid: "used to represent..."
- Message and field comments may reference the field or message by name.
  - valid: "AnyValue ..."
  - valid: "The value ..."

## Further Help

If you have any questions or need assistance while contributing, feel free to reach out to the [`#otel-specification`](https://cloud-native.slack.com/archives/C01N7PP1THC) Slack channel.  
View meeting notes of previous SIG calls in this [google doc](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s/edit?gid=0#gid=0) as stated [here](https://github.com/open-telemetry/community/?tab=readme-ov-file#governing-bodies) to stay up to date.

Also see the [specification](https://github.com/open-telemetry/opentelemetry-specification?tab=readme-ov-file#questions) repo for more info. Thank you.
```

## File: `LICENSE`
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

## File: `Makefile`
```
GOPATH_DIR := $(GOPATH)/src/github.com/open-telemetry/opentelemetry-proto
GENDIR := gen
GOPATH_GENDIR := $(GOPATH_DIR)/$(GENDIR)

# Find all .proto files.
PROTO_FILES := $(wildcard opentelemetry/proto/*/*/*.proto opentelemetry/proto/*/*/*/*.proto)

# Function to execute a command. Note the empty line before endef to make sure each command
# gets executed separately instead of concatenated with previous one.
# Accepts command to execute as first parameter.
define exec-command
$(1)

endef

.PHONY: all
all: gen-all markdown-link-check markdownlint

# Generate all implementations
.PHONY: gen-all
gen-all: gen-cpp gen-csharp gen-go gen-java gen-kotlin gen-objc gen-openapi gen-php gen-python gen-ruby

DEPENDENCIES_DOCKERFILE=./dependencies.Dockerfile

OTEL_DOCKER_PROTOBUF ?= otel/build-protobuf:0.9.0
BUF_DOCKER ?= bufbuild/buf:1.7.0

PROTOC := docker run --rm -u ${shell id -u} -v${PWD}:${PWD} -w${PWD} ${OTEL_DOCKER_PROTOBUF} --proto_path=${PWD}
BUF := docker run --rm -v "${PWD}:/workspace" -w /workspace ${BUF_DOCKER}
# When checking for protobuf breaking changes, check against the latest release tag
LAST_RELEASE_TAG := $(shell git tag --sort=committerdate | tail -1)
# Options are described in https://docs.buf.build/breaking/usage#git
BUF_AGAINST ?= "https://github.com/open-telemetry/opentelemetry-proto.git\#tag=$(LAST_RELEASE_TAG)"

PROTO_GEN_CPP_DIR ?= $(GENDIR)/cpp
PROTO_GEN_CSHARP_DIR ?= $(GENDIR)/csharp
PROTO_GEN_GO_DIR ?= $(GENDIR)/go
PROTO_GEN_JAVA_DIR ?= $(GENDIR)/java
PROTO_GEN_JS_DIR ?= $(GENDIR)/js
PROTO_GEN_KOTLIN_DIR ?= $(GENDIR)/kotlin
PROTO_GEN_OBJC_DIR ?= $(GENDIR)/objc
PROTO_GEN_OPENAPI_DIR ?= $(GENDIR)/openapi
PROTO_GEN_PHP_DIR ?= $(GENDIR)/php
PROTO_GEN_PYTHON_DIR ?= $(GENDIR)/python
PROTO_GEN_RUBY_DIR ?= $(GENDIR)/ruby

# Docker pull image.
.PHONY: docker-pull
docker-pull:
	docker pull $(OTEL_DOCKER_PROTOBUF)
	docker pull $(BUF_DOCKER)

# Generate gRPC/Protobuf implementation for C++.
.PHONY: gen-cpp
gen-cpp:
	rm -rf ./$(PROTO_GEN_CPP_DIR)
	mkdir -p ./$(PROTO_GEN_CPP_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --cpp_out=./$(PROTO_GEN_CPP_DIR) $(file)))
	$(PROTOC) --cpp_out=./$(PROTO_GEN_CPP_DIR) --grpc-cpp_out=./$(PROTO_GEN_CPP_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --cpp_out=./$(PROTO_GEN_CPP_DIR) --grpc-cpp_out=./$(PROTO_GEN_CPP_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --cpp_out=./$(PROTO_GEN_CPP_DIR) --grpc-cpp_out=./$(PROTO_GEN_CPP_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --cpp_out=./$(PROTO_GEN_CPP_DIR) --grpc-cpp_out=./$(PROTO_GEN_CPP_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for C#.
.PHONY: gen-csharp
gen-csharp:
	rm -rf ./$(PROTO_GEN_CSHARP_DIR)
	mkdir -p ./$(PROTO_GEN_CSHARP_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --csharp_out=./$(PROTO_GEN_CSHARP_DIR) $(file)))
	$(PROTOC) --csharp_out=./$(PROTO_GEN_CSHARP_DIR) --grpc-csharp_out=./$(PROTO_GEN_CSHARP_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --csharp_out=./$(PROTO_GEN_CSHARP_DIR) --grpc-csharp_out=./$(PROTO_GEN_CSHARP_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --csharp_out=./$(PROTO_GEN_CSHARP_DIR) --grpc-csharp_out=./$(PROTO_GEN_CSHARP_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --csharp_out=./$(PROTO_GEN_CSHARP_DIR) --grpc-csharp_out=./$(PROTO_GEN_CSHARP_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for Go.
.PHONY: gen-go
gen-go:
	rm -rf ./$(PROTO_GEN_GO_DIR)
	mkdir -p ./$(PROTO_GEN_GO_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command,$(PROTOC) --go_out=plugins=grpc:./$(PROTO_GEN_GO_DIR) $(file)))
	$(PROTOC) --grpc-gateway_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/trace/v1/trace_service_http.yaml:./$(PROTO_GEN_GO_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --grpc-gateway_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/metrics/v1/metrics_service_http.yaml:./$(PROTO_GEN_GO_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --grpc-gateway_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/logs/v1/logs_service_http.yaml:./$(PROTO_GEN_GO_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --grpc-gateway_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/profiles/v1development/profiles_service_http.yaml:./$(PROTO_GEN_GO_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for Java.
.PHONY: gen-java
gen-java:
	rm -rf ./$(PROTO_GEN_JAVA_DIR)
	mkdir -p ./$(PROTO_GEN_JAVA_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --java_out=./$(PROTO_GEN_JAVA_DIR) $(file)))

# Generate gRPC/Protobuf implementation for Kotlin.
.PHONY: gen-kotlin
gen-kotlin: gen-java
	rm -rf ./$(PROTO_GEN_KOTLIN_DIR)
	mkdir -p ./$(PROTO_GEN_KOTLIN_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --kotlin_out=./$(PROTO_GEN_KOTLIN_DIR) $(file)))


# Generate gRPC/Protobuf implementation for JavaScript.
.PHONY: gen-js
gen-js:
	rm -rf ./$(PROTO_GEN_JS_DIR)
	mkdir -p ./$(PROTO_GEN_JS_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --js_out=import_style=commonjs:./$(PROTO_GEN_JS_DIR) $(file)))
	$(PROTOC) --js_out=import_style=commonjs:./$(PROTO_GEN_JS_DIR) --grpc-web_out=import_style=commonjs,mode=grpcweb:./$(PROTO_GEN_JS_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --js_out=import_style=commonjs:./$(PROTO_GEN_JS_DIR) --grpc-web_out=import_style=commonjs,mode=grpcweb:./$(PROTO_GEN_JS_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --js_out=import_style=commonjs:./$(PROTO_GEN_JS_DIR) --grpc-web_out=import_style=commonjs,mode=grpcweb:./$(PROTO_GEN_JS_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --js_out=import_style=commonjs:./$(PROTO_GEN_JS_DIR) --grpc-web_out=import_style=commonjs,mode=grpcweb:./$(PROTO_GEN_JS_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for Objective-C.
.PHONY: gen-objc
gen-objc:
	rm -rf ./$(PROTO_GEN_OBJC_DIR)
	mkdir -p ./$(PROTO_GEN_OBJC_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --objc_out=./$(PROTO_GEN_OBJC_DIR) $(file)))
	$(PROTOC) --objc_out=./$(PROTO_GEN_OBJC_DIR) --grpc-objc_out=./$(PROTO_GEN_OBJC_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --objc_out=./$(PROTO_GEN_OBJC_DIR) --grpc-objc_out=./$(PROTO_GEN_OBJC_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --objc_out=./$(PROTO_GEN_OBJC_DIR) --grpc-objc_out=./$(PROTO_GEN_OBJC_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --objc_out=./$(PROTO_GEN_OBJC_DIR) --grpc-objc_out=./$(PROTO_GEN_OBJC_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf for openapi v2 (swagger)
.PHONY: gen-openapi
gen-openapi:
	mkdir -p $(PROTO_GEN_OPENAPI_DIR)
	$(PROTOC) --openapiv2_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/trace/v1/trace_service_http.yaml:$(PROTO_GEN_OPENAPI_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --openapiv2_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/metrics/v1/metrics_service_http.yaml:$(PROTO_GEN_OPENAPI_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --openapiv2_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/logs/v1/logs_service_http.yaml:$(PROTO_GEN_OPENAPI_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --openapiv2_out=logtostderr=true,grpc_api_configuration=opentelemetry/proto/collector/profiles/v1development/profiles_service_http.yaml:$(PROTO_GEN_OPENAPI_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for PhP.
.PHONY: gen-php
gen-php:
	rm -rf ./$(PROTO_GEN_PHP_DIR)
	mkdir -p ./$(PROTO_GEN_PHP_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --php_out=./$(PROTO_GEN_PHP_DIR) $(file)))
	$(PROTOC) --php_out=./$(PROTO_GEN_PHP_DIR) --grpc-php_out=./$(PROTO_GEN_PHP_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --php_out=./$(PROTO_GEN_PHP_DIR) --grpc-php_out=./$(PROTO_GEN_PHP_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --php_out=./$(PROTO_GEN_PHP_DIR) --grpc-php_out=./$(PROTO_GEN_PHP_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --php_out=./$(PROTO_GEN_PHP_DIR) --grpc-php_out=./$(PROTO_GEN_PHP_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for Python.
.PHONY: gen-python
gen-python:
	rm -rf ./$(PROTO_GEN_PYTHON_DIR)
	mkdir -p ./$(PROTO_GEN_PYTHON_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --python_out=./$(PROTO_GEN_PYTHON_DIR) $(file)))
	$(PROTOC) --python_out=./$(PROTO_GEN_PYTHON_DIR) --grpc-python_out=./$(PROTO_GEN_PYTHON_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --python_out=./$(PROTO_GEN_PYTHON_DIR) --grpc-python_out=./$(PROTO_GEN_PYTHON_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --python_out=./$(PROTO_GEN_PYTHON_DIR) --grpc-python_out=./$(PROTO_GEN_PYTHON_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --python_out=./$(PROTO_GEN_PYTHON_DIR) --grpc-python_out=./$(PROTO_GEN_PYTHON_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# Generate gRPC/Protobuf implementation for Ruby.
.PHONY: gen-ruby
gen-ruby:
	rm -rf ./$(PROTO_GEN_RUBY_DIR)
	mkdir -p ./$(PROTO_GEN_RUBY_DIR)
	$(foreach file,$(PROTO_FILES),$(call exec-command, $(PROTOC) --ruby_out=./$(PROTO_GEN_RUBY_DIR) $(file)))
	$(PROTOC) --ruby_out=./$(PROTO_GEN_RUBY_DIR) --grpc-ruby_out=./$(PROTO_GEN_RUBY_DIR) opentelemetry/proto/collector/trace/v1/trace_service.proto
	$(PROTOC) --ruby_out=./$(PROTO_GEN_RUBY_DIR) --grpc-ruby_out=./$(PROTO_GEN_RUBY_DIR) opentelemetry/proto/collector/metrics/v1/metrics_service.proto
	$(PROTOC) --ruby_out=./$(PROTO_GEN_RUBY_DIR) --grpc-ruby_out=./$(PROTO_GEN_RUBY_DIR) opentelemetry/proto/collector/logs/v1/logs_service.proto
	$(PROTOC) --ruby_out=./$(PROTO_GEN_RUBY_DIR) --grpc-ruby_out=./$(PROTO_GEN_RUBY_DIR) opentelemetry/proto/collector/profiles/v1development/profiles_service.proto

# The Profiling protocol is still development. So it is excluded from the breaking-change check.
.PHONY: breaking-change
breaking-change:
	$(BUF) breaking --against $(BUF_AGAINST) --config '{"version":"v1","breaking":{"ignore":["opentelemetry/proto/profiles", "opentelemetry/proto/collector/profiles"]}}' $(BUF_FLAGS)


ALL_DOCS := $(shell find . -type f -name '*.md' -not -path './.github/*' -not -path './node_modules/*' | sort)

LYCHEEIMAGE := $(shell awk '$$4=="lychee" {print $$2}' $(DEPENDENCIES_DOCKERFILE))
.PHONY: markdown-link-check
markdown-link-check:
	docker run --rm \
		--mount 'type=bind,source=$(PWD),target=/home/repo' \
		$(LYCHEEIMAGE) \
		--config home/repo/.lychee.toml \
		--root-dir /home/repo \
		-v \
		home/repo

MARKDOWNLINTIMAGE := $(shell awk '$$4=="markdownlint" {print $$2}' $(DEPENDENCIES_DOCKERFILE))
.PHONY: markdownlint
markdownlint:
	@for f in $(ALL_DOCS); do \
		echo $$f; \
		docker run --rm \
			--mount 'type=bind,source=$(PWD),target=/workdir' \
			$(MARKDOWNLINTIMAGE) \
			--config .markdownlint.yaml $$f || exit 1; \
	done
```

## File: `README.md`
```markdown
# OpenTelemetry Protocol (OTLP) Specification

[![Build Check](https://github.com/open-telemetry/opentelemetry-proto/workflows/Build%20Check/badge.svg?branch=main)](https://github.com/open-telemetry/opentelemetry-proto/actions?query=workflow%3A%22Build+Check%22+branch%3Amain)

This repository contains the [OTLP protocol specification](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md)
and the corresponding Language Independent Interface Types ([.proto files](opentelemetry/proto)).

## Language Independent Interface Types

The proto files can be consumed as GIT submodules or copied and built directly in the consumer project.

The compiled files are published to central repositories (Maven, ...) from OpenTelemetry client libraries.

See [contribution guidelines](CONTRIBUTING.md) if you would like to make any changes.

## OTLP/JSON

See additional requirements for [OTLP/JSON wire representation here](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/otlp.md#json-protobuf-encoding).

## Generate gRPC Client Libraries

To generate the raw gRPC client libraries, use `make gen-${LANGUAGE}`. Currently supported languages are:

* cpp
* csharp
* go
* java
* objc
* openapi (swagger)
* php
* python
* ruby

## Maturity Level

1.0.0 and newer releases from this repository may contain unstable (alpha or beta)
components as indicated by the Maturity table below.

| Component | Binary Protobuf Maturity | JSON Maturity |
| --------- | --------------- | ------------- |
| common/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| resource/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| metrics/\*<br>collector/metrics/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| trace/\*<br>collector/trace/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| logs/\*<br>collector/logs/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| profiles/\*<br>collector/profiles/* | Development | [Development](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |

(See [Versioning and Stability](https://github.com/open-telemetry/opentelemetry-specification/blob/a08d1f92f62acd4aafe4dfaa04ae7bf28600d49e/specification/versioning-and-stability.md)
for definition of maturity levels).

## Stability Definition

Components marked `Stable` provide the following guarantees:

- Field types, numbers and names will not change.
- Service names and `service` package names will not change.
- Service method names will not change. [from 1.0.0]
- Service method parameter names will not change. [from 1.0.0]
- Service method parameter types and return types will not change. [from 1.0.0]
- Service method kind (unary vs streaming) will not change.
- Names of `message`s and `enum`s will not change. [from 1.0.0]
- Numbers assigned to `enum` choices will not change.
- Names of `enum` choices will not change. [from 1.0.0]
- The location of `message`s and `enum`s, i.e. whether they are declared at the top lexical
  scope or nested inside another `message` will not change. [from 1.0.0]
- Package names and directory structure will not change. [from 1.0.0]
- `optional` and `repeated` declarators of existing fields will not change. [from 1.0.0]
- No existing symbol will be deleted.  [from 1.0.0]

Note: guarantees marked [from 1.0.0] will go into effect when this repository is tagged
with version number 1.0.0.

The following additive changes are allowed:

- Adding new fields to existing `message`s.
- Adding new `message`s or `enum`s.
- Adding new choices to existing `enum`s.
- Adding new choices to existing `oneof` fields.
- Adding new `service`s.
- Adding new `method`s to existing `service`s.

All the additive changes above must be accompanied by an explanation about how
new and old senders and receivers that implement the version of the protocol
before and after the change interoperate.

## Experiments

### New Experimental Components  

Sometimes we need to experiment with new components, for example to add a
completely new signal to OpenTelemetry. When designing a new signal, we
recommend a "development" package to be used. This package will be used
throughout development until reaching release candidate, in which case the
`development` suffix is removed (e.g. `v1` instead of `v1development`),
creating a stable release package.

Such isolated experimental components are excluded from
above [stability requirements](#stability-definition).

We recommend using
`Development`, `Alpha`, `Beta`, `Release Candidate`
[levels](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/0232-maturity-of-otel.md#maturity-levels)
to communicate different grades of readiness of new components. These levels
MUST be communicated in the documentation of a message, field, etc. when the
level does not match the stability of the package. For example, if a package is
`Stable` but a field is not, the documentation MUST indicate that the field is
experimental with the appropriate level (e.g. `Alpha`, `Beta`, etc).
Conversely, individual `Status` annotations are not required if a component
is the same maturity level as the package it is defined in.

Experimental components may be removed completely at the end of the experiment,
provided that they are not referenced from any `Stable` component.

Experiments which succeed, require a review to be marked `Stable`. Once marked
`Stable` they become subject to the [stability requirements](#stability-definition).

### Experimental Additions to Stable Components

New experimental fields or messages may be added in `Development` state to `Stable`
components. The experimental fields and messages within `Stable components` are subject
to the full [stability requirements](#stability-definition).

When the stability of a *portion* of the protocol doesn't match the expectations of the
package, there MUST be a stability annotation in the docs. For example:

```protobuf
// A reference to an Entity.
// Entity represents an object of interest associated with produced telemetry: e.g spans, metrics, profiles, or logs.
//
// Status: [Development]
message EntityRef {
  // ...
}
```

If an experiment concludes and the previously added field or message is not needed
anymore, the field/message must stay, but it may be declared "deprecated". During all
phases of experimentation it must be clearly specified that the field or message may be
deprecated. Typically, deprecated fields are left empty by the senders and the recipients
that participate in experiments must expect during all experimental phases (including
*after* the experiment is concluded) that the experimental field or message has an
empty value.

Experiments which succeed, require a review before the field or the message is marked
`Stable`.

## Generated Code

No guarantees are provided whatsoever about the stability of the code that
is generated from the .proto files by any particular code generator.

## Maintainers

- [OpenTelemetry Technical Committee](https://github.com/open-telemetry/community/blob/main/community-members.md#technical-committee)

For more information about the maintainer role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#maintainer).

## Approvers

- [OpenTelemetry Specification Sponsors](https://github.com/open-telemetry/community/blob/main/community-members.md#specifications-and-proto)

For more information about the approver role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#approver).
```

## File: `RELEASING.md`
```markdown
# How to Create a Release

_Instruction for Maintainers only._

- Prepare the release by updating [CHANGELOG.md](CHANGELOG.md), see for example
[this PR](https://github.com/open-telemetry/opentelemetry-proto/pull/537).
Merge the PR. From this point on no new PRs can be merged until the release is complete.

- Go to Github [release page](https://github.com/open-telemetry/opentelemetry-proto/releases),
click `Draft a new release`.

- Click "Choose a tag" and specify the next version number. The Target branch should be "main".

- Click "Generate release notes" to get a draft release note. Remove editorial
changes from the notes and any other changes that you don't want in the release notes.
In addition, you can refer to [CHANGELOG.md](CHANGELOG.md) for a list of major changes since last release.

- Click "Publish Release".

Our tags follow the naming convention of `v1.<minor>.<patch>`. Increment `minor` by 1
and use `patch` value of 0 for new minor version releases. For patch releases keep `minor`
unchanged and increment the `patch`.
```

## File: `buf.yaml`
```yaml
version: v1

# See https://docs.buf.build/breaking/configuration
breaking:
  use:
    - WIRE
```

## File: `dependencies.Dockerfile`
```
# This is a renovate-friendly source of Docker images.
FROM davidanson/markdownlint-cli2:v0.22.0@sha256:ea33f1f6a0f062f88a3dddfc49f6d6b5621648a93a0ff49a58bf8ac5a15330b9 AS markdownlint
FROM lycheeverse/lychee:sha-3a09227-alpine@sha256:5853bd7c283663a1200dbb15924a5047f8d4c50adfa7a4c212a94f04bbac831c AS lychee
```

## File: `docs/README.md`
```markdown
# OpenTelemetry Protocol (OTLP)

This is the specification of the OpenTelemetry Protocol (OTLP).

- [Design Goals](design-goals.md)
- [Requirements](../../../core/security/QUARANTINE/vetted/repos/LobsterAI/spec/features/001_optimize_windows_startup/checklists/requirements.md)
- [Specification](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md)
- [SDK Exporter](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md)
```

## File: `docs/design-goals.md`
```markdown
# Design Goals for OpenTelemetry Wire Protocol

We want to design a telemetry data exchange protocol that has the following characteristics:

- Be suitable for use between all of the following node types: instrumented applications, telemetry backends, local agents, stand-alone collectors/forwarders.

- Have high reliability of data delivery and clear visibility when the data cannot be delivered.

- Have low CPU usage for serialization and deserialization.

- Impose minimal pressure on memory manager, including pass-through scenarios, where deserialized data is short-lived and must be serialized as-is shortly after and where such short-lived data is created and discarded at high frequency (think telemetry data forwarders).

- Support ability to efficiently modify deserialized data and serialize again to pass further. This is related but slightly different from the previous requirement.

- Ensure high throughput (within the available bandwidth) in high latency networks (e.g. scenarios where telemetry source and the backend are separated by high latency network).

- Allow backpressure signalling.

- Be load-balancer friendly (do not hinder re-balancing).
```

## File: `docs/requirements.md`
```markdown
# OpenTelemetry Protocol Requirements

This document will drive OpenTelemetry Protocol design and RFC.

## Goals

See the goals of OpenTelemetry Protocol design [here](design-goals.md).

## Vocabulary

There are 2 parties involved in telemetry data exchange. In this document the party that is the source of telemetry data is called the Client, the party that is the destination of telemetry data is called the Server.

Examples of a Client are instrumented applications or sending side of telemetry collectors, examples of Servers are telemetry backends or receiving side of telemetry collectors (so a Collector is typically both a Client and a Server depending on which side you look from).

## Known Issues with Existing Protocols

Our experience with OpenCensus and other protocols has been that many of them have one or more of the following drawbacks:

- High CPU consumption for serialization and especially deserialization of received telemetry data.
- High and frequent CPU consumption by Garbage Collector.
- Lack of delivery guarantees for certain protocols (e.g. stream-based gRPC OpenCensus protocol) which makes troubleshooting of telemetry pipelines difficult.
- Not aware / not cooperating with load balancers resulting in potentially large imbalances in horizontally scaled backends.
- Support either traces or metrics but not both.

Our goal is to avoid or mitigate these known issues in the new protocol.

## Requirements

The following are OpenTelemetry protocol requirements.

### Supported Node Types

The protocol must be suitable for use between all of the following node types: instrumented applications, telemetry backends, telemetry agents running as local daemons, stand-alone collector/forwarder services.

### Supported Data Types

The protocol must support traces and metrics as data types.

### Reliability of Delivery

The protocol must ensure reliable data delivery and clear visibility when the data cannot be delivered. This should be achieved by sending data acknowledgements from the Server to the Client.

Note that acknowledgements alone are not sufficient to guarantee that: a) no data will be lost and b) no data will be duplicated. Acknowledgements can help to guarantee a) but not b). Guaranteeing both at the same is difficult. Because it is usually preferable for telemetry data to be duplicated than to lose it, we choose to guarantee that there are no data losses while potentially allowing duplicate data.

Duplicates can typically happen in edge cases (e.g. on reconnections, network interruptions, etc) when the client has no way of knowing if last sent data was delivered. In these cases the client will usually choose to re-send the data to guarantee the delivery which in turn may result in duplicate data on the server side.

_To avoid having duplicates the client and the server could track sent and delivered items using uniquely identifying ids. The exact mechanism for tracking the ids and performing data de-duplication may be defined at the layer above the protocol layer and is outside the scope of this document._

For this reason we have slightly relaxed requirements and consider duplicate data acceptable in rare cases.

Note: this protocol is concerned with reliability of delivery between one pair of client/server nodes and aims to ensure that no data is lost in-transit between the client and the server. Many telemetry collection systems have multiple nodes that the data must travel across until reaching the final destination (e.g. application -> agent -> collector -> backend). End-to-end delivery guarantees in such systems is outside of the scope for this document. The acknowledgements described in this protocol happen between a single client/server pair and do not span multiple nodes in multi-hop delivery paths.

### Throughput

The protocol must ensure high throughput in high latency networks when the client and the server are not in the same data center.

This requirement may rule out half-duplex protocols. The throughput of half-duplex protocols is highly dependent on network roundtrip time and request size. To achieve good throughput request sizes may be too large to be practical.

### Compression

The protocol must achieve high compression ratios for telemetry data. The protocol design must consider batching of telemetry data and grouping of similar data (both can help to achieve better compression using common compression algorithms).

### Encryption

Industry standard encryption (e.g. TLS/HTTPS) must be supported.

### Backpressure Signalling and Throttling

The protocol must allow backpressure signalling.

If the server is unable to keep up with the pace of data it receives from the client then it must be able to signal that fact to the client. The client may then throttle itself to avoid overwhelming the server.

If the underlying transport is a stream that has its own flow control mechanism then the backpressure could be applied by delaying the reading of data from the server’s endpoint which could then be signalled to the client via underlying flow-control. However this approach makes it difficult for the client to distinguish server overloading from network delays (due to e.g. network losses). Such distinction is important for [observability reasons](https://github.com/open-telemetry/opentelemetry-service/pull/188). Because of this it is required for the protocol to allow to explicitly and clearly signal backpressure from the server to the client without relying on implicit signalling using underlying flow-control mechanisms.

The backpressure signal should include a hint to the client about desirable reduced rate of data.

### Serialization Performance

The protocol must have fast data serialization and deserialization characteristics.

Ideally it must also support very fast pass-through mode (when no modifications to the data are needed), fast “augmenting” or “tagging” of data and partial inspection of data (e.g. check for presence of specific tag). These requirements help to create fast Agents and Collectors.

### Memory Usage Profile

The protocol must impose minimal pressure on memory manager, including pass-through scenarios, when deserialized data is short-lived and must be serialized as-is shortly after and when such short-lived data is created and discarded at high frequency (think telemetry data forwarders).

The implementation of telemetry protocol must aim to minimize the number of memory allocations and deallocations performed during serialization and deserialization and aim to minimize the pressure on Garbage Collection (for GC languages).

### Level 7 Load Balancer Friendly

The protocol must allow Level 7 load balancers such as Envoy to re-balance the traffic for each batch of telemetry data. The traffic should not get pinned by a load balancer to one server for the entire duration of telemetry data sending, thus potentially leading to imbalanced load of servers located behind the load balancer.

### Backwards Compatibility

The protocol should be possible to evolve over time. It should be possible for nodes that implement different versions of OpenTelemetry protocol to interoperate (while possibly regressing to the lowest common denominator from functional perspective).

### General Requirements

The protocol must use well-known, mature encoding and transport mechanisms with ubiquitous availability of implementations in wide selection of languages that are supported by OpenTelemetry.
```

## File: `docs/specification.md`
```markdown
<!-- markdownlint-disable-next-line first-line-heading -->
<!--- Hugo front matter used to generate the website version of this page:
title: OTLP Specification
linkTitle: OTLP
aliases:
  - /docs/reference/specification/protocol/otlp
  - /docs/specs/otel/protocol/otlp
spelling:
  cSpell:ignore backoff backpressure errdetails nanos proto reconnections retryable
cascade:
  body_class: otel-docs-spec
  github_repo: &repo https://github.com/open-telemetry/opentelemetry-proto
  path_base_for_github_subdir: tmp/otlp
  github_project_repo: *repo
--->

# OpenTelemetry Protocol Specification

**Status**:

* [Stable](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/document-status.md) for the trace, metric and log signals.
* [Development](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/document-status.md) for the profiles signal.

The OpenTelemetry Protocol (OTLP) specification describes the encoding, transport,
and delivery mechanism of telemetry data between telemetry sources, intermediate
nodes such as collectors and telemetry backends.

<details>
<summary>Table of Contents</summary>

<!-- toc -->

- [Protocol Details](#protocol-details)
  * [OTLP/gRPC](#otlpgrpc)
    + [OTLP/gRPC Concurrent Requests](#otlpgrpc-concurrent-requests)
    + [OTLP/gRPC Response](#otlpgrpc-response)
      - [Full Success](#full-success)
      - [Partial Success](#partial-success)
      - [Failures](#failures)
    + [OTLP/gRPC Throttling](#otlpgrpc-throttling)
    + [OTLP/gRPC Service and Protobuf Definitions](#otlpgrpc-service-and-protobuf-definitions)
    + [OTLP/gRPC Default Port](#otlpgrpc-default-port)
  * [OTLP/HTTP](#otlphttp)
    + [Binary Protobuf Encoding](#binary-protobuf-encoding)
    + [JSON Protobuf Encoding](#json-protobuf-encoding)
    + [OTLP/HTTP Request](#otlphttp-request)
    + [OTLP/HTTP Response](#otlphttp-response)
      - [Full Success](#full-success-1)
      - [Partial Success](#partial-success-1)
      - [Failures](#failures-1)
      - [Bad Data](#bad-data)
      - [OTLP/HTTP Throttling](#otlphttp-throttling)
      - [All Other Responses](#all-other-responses)
    + [OTLP/HTTP Connection](#otlphttp-connection)
    + [OTLP/HTTP Concurrent Requests](#otlphttp-concurrent-requests)
    + [OTLP/HTTP Default Port](#otlphttp-default-port)
- [Implementation Recommendations](#implementation-recommendations)
  * [Multi-Destination Exporting](#multi-destination-exporting)
- [Known Limitations](#known-limitations)
  * [Request Acknowledgements](#request-acknowledgements)
    + [Duplicate Data](#duplicate-data)
- [Future Versions and Interoperability](#future-versions-and-interoperability)
- [Glossary](#glossary)
- [References](#references)

<!-- tocstop -->

</details>

OTLP is a general-purpose telemetry data delivery protocol designed in the scope
of the OpenTelemetry project.

## Protocol Details

OTLP defines the encoding of telemetry data and the protocol used to exchange
data between the client and the server.

This specification defines how OTLP is implemented over
[gRPC](https://grpc.io/) and HTTP transports and specifies
[Protocol Buffers schema](https://developers.google.com/protocol-buffers/docs/overview)
that is used for the payloads.

OTLP is a request/response style protocol: the clients send requests, and the
server replies with corresponding responses. This document defines one request
and response type: `Export`.

All server components MUST support the following transport compression options:

* No compression, denoted by `none`.
* Gzip compression, denoted by `gzip`.

### OTLP/gRPC

After establishing the underlying gRPC transport, the client starts sending
telemetry data using unary requests using
[Export*ServiceRequest](https://github.com/open-telemetry/opentelemetry-proto)
messages ([ExportLogsServiceRequest](../opentelemetry/proto/collector/logs/v1/logs_service.proto) for logs,
[ExportMetricsServiceRequest](../opentelemetry/proto/collector/metrics/v1/metrics_service.proto) for metrics,
[ExportTraceServiceRequest](../opentelemetry/proto/collector/trace/v1/trace_service.proto) for traces,
[ExportProfilesServiceRequest](../opentelemetry/proto/collector/profiles/v1development/profiles_service.proto) for profiles).
The client continuously sends a sequence of requests to the server and expects
to receive a response to each request:

![Request-Response](img/otlp-request-response.png)

_Note: this protocol is concerned with the reliability of delivery between one
pair of client/server nodes and aims to ensure that no data is lost in transit
between the client and the server. Many telemetry collection systems have
intermediary nodes that the data must travel across until reaching the final
destination (e.g. application -> agent -> collector -> backend). End-to-end
delivery guarantees in such systems is outside of the scope of OTLP. The
acknowledgements described in this protocol happen between a single
client/server pair and do not span intermediary nodes in multi-hop delivery
paths._

#### OTLP/gRPC Concurrent Requests

After sending the request the client MAY wait until the response is received
from the server. In that case there will be at most only one request in flight
that is not yet acknowledged by the server.

![Unary](img/otlp-sequential.png)

Sequential operation is recommended when simplicity of implementation is
desirable, and when the client and the server are connected via very low-latency
network, such as when the client is an instrumented application and
the server is an OpenTelemetry Collector running as a local daemon (agent).

The implementations that need to achieve high throughput SHOULD support
concurrent Unary calls to achieve higher throughput. The client SHOULD send new
requests without waiting for the response to the earlier sent requests,
essentially creating a pipeline of requests that are currently in flight that
are not acknowledged.

![Concurrent](img/otlp-concurrent.png)

The number of concurrent requests SHOULD be configurable.

The maximum achievable throughput is
`max_concurrent_requests * max_request_size / (network_latency + server_response_time)`.
For example, if the request can contain at most 100 spans, network roundtrip
latency is 200ms, and server response time is 300 ms, then the maximum achievable
throughput with one concurrent request is `100 spans / (200ms+300ms)` or 200
spans per second. It is easy to see that in high latency networks or when the
server response time is high to achieve good throughput, the requests need to be
very big or a lot concurrent requests must be done.

If the client is shutting down (e.g. when the containing process wants to exit)
the client will optionally wait until all pending acknowledgements are received
or until an implementation-specific timeout expires. This ensures the reliable
delivery of telemetry data. The client implementation SHOULD expose an option to
turn on and off the waiting during a shutdown.

If the client is unable to deliver a certain request (e.g. a timer expired while
waiting for acknowledgements) the client SHOULD record the fact that the data
was not delivered.

#### OTLP/gRPC Response

The response MUST be the appropriate message (see below for
the specific message to use in the [Full Success](#full-success),
[Partial Success](#partial-success) and [Failure](#failures) cases).

##### Full Success

The success response indicates telemetry data is successfully accepted by the
server.

If the server receives an empty request (a request that does not carry
any telemetry data) the server SHOULD respond with success.

On success, the server response MUST be a
[Export\<signal>ServiceResponse](../opentelemetry/proto/collector) message
(`ExportTraceServiceResponse` for traces, `ExportMetricsServiceResponse` for
metrics, `ExportLogsServiceResponse` for logs and
`ExportProfilesServiceResponse` for profiles).

The server MUST leave the `partial_success` field unset
in case of a successful response.

##### Partial Success

If the request is only partially accepted
(i.e. when the server accepts only parts of the data and rejects the rest), the
server response MUST be the same
[Export\<signal>ServiceResponse](../opentelemetry/proto/collector)
message as in the [Full Success](#full-success) case.

Additionally, the server MUST initialize the `partial_success` field
(`ExportTracePartialSuccess` message for traces, `ExportMetricsPartialSuccess`
message for metrics, `ExportLogsPartialSuccess` message for logs and
`ExportProfilesPartialSuccess` for profiles), and it MUST set the respective
`rejected_spans`, `rejected_data_points`, `rejected_log_records` or
`rejected_profiles` field with the number of spans/data points/log
records/profiles it rejected.

The server SHOULD populate the `error_message` field with a human-readable
error message in English. The message should explain why the
server rejected parts of the data and might offer guidance on how users
can address the issues.
The protocol does not attempt to define the structure of the error message.

Servers MAY also use the `partial_success` field to convey
warnings/suggestions to clients even when the server fully accepts the request.
In such cases, the `rejected_<signal>` field MUST have a value of `0`, and
the `error_message` field MUST be non-empty.

The client MUST NOT retry the request when it receives a partial success
response where the `partial_success` is populated.

##### Failures

When the server returns an error, it falls into 2 broad categories:
retryable and not-retryable:

- Retryable errors indicate that telemetry data processing failed, and the
  client SHOULD record the error and may retry exporting the same data.
  For example, this can happen when the server is temporarily unable to
  process the data.

- Not-retryable errors indicate that telemetry data processing failed, and the
  client MUST NOT retry sending the same telemetry data. The client MUST drop
  the telemetry data.
  For example, this can happen, when the request contains bad data
  and cannot be deserialized or processed by the server. The client
  SHOULD maintain a counter of such dropped data.

The server SHOULD indicate retryable errors using code
[Unavailable](https://godoc.org/google.golang.org/grpc/codes) and MAY supply
additional
[details via status](https://godoc.org/google.golang.org/grpc/status#Status.WithDetails)
using
[RetryInfo](https://github.com/googleapis/googleapis/blob/6a8c7914d1b79bd832b5157a09a9332e8cbd16d4/google/rpc/error_details.proto#L40).
Here is a sample Go code to illustrate:

```go
  // Do this on server side.
  st, err := status.New(codes.Unavailable, "Server is unavailable").
    WithDetails(&errdetails.RetryInfo{RetryDelay: &duration.Duration{Seconds: 5}})
  if err != nil {
    log.Fatal(err)
  }

  return st.Err()
```

To indicate not-retryable errors, the server is recommended to use code
[InvalidArgument](https://godoc.org/google.golang.org/grpc/codes) and MAY supply
additional
[details via status](https://godoc.org/google.golang.org/grpc/status#Status.WithDetails)
using
[BadRequest](https://github.com/googleapis/googleapis/blob/6a8c7914d1b79bd832b5157a09a9332e8cbd16d4/google/rpc/error_details.proto#L119).
If more appropriate, another gRPC status code may be used. Here is a
snippet of sample Go code to illustrate:

```go
  // Do this on the server side.
  st, err := status.New(codes.InvalidArgument, "Invalid Argument").
    WithDetails(&errdetails.BadRequest{})
  if err != nil {
    log.Fatal(err)
  }

  return st.Err()
```

The server MAY use other gRPC codes to indicate retryable and not-retryable
errors if those other gRPC codes are more appropriate for a particular erroneous
situation. The client SHOULD interpret gRPC status codes as retryable or
not-retryable according to the following table:

|gRPC Code|Retryable?|
|---------|----------|
|CANCELLED|Yes|
|UNKNOWN|No|
|INVALID_ARGUMENT|No|
|DEADLINE_EXCEEDED|Yes|
|NOT_FOUND|No|
|ALREADY_EXISTS|No|
|PERMISSION_DENIED|No|
|UNAUTHENTICATED|No|
|RESOURCE_EXHAUSTED|Only if the server can recover (see below)|
|FAILED_PRECONDITION|No|
|ABORTED|Yes|
|OUT_OF_RANGE|Yes|
|UNIMPLEMENTED|No|
|INTERNAL|No|
|UNAVAILABLE|Yes|
|DATA_LOSS|Yes|

When retrying, the client SHOULD implement an exponential backoff strategy. An
exception to this is the Throttling case explained below, which provides
explicit instructions about retrying interval.

The client SHOULD interpret `RESOURCE_EXHAUSTED` code as retryable only if the
server signals that the recovery from resource exhaustion is possible.
This is signaled by the server by returning
[a status](https://godoc.org/google.golang.org/grpc/status#Status.WithDetails) containing
[RetryInfo](https://github.com/googleapis/googleapis/blob/6a8c7914d1b79bd832b5157a09a9332e8cbd16d4/google/rpc/error_details.proto#L40).
In this case the behavior of the server and the client is exactly as described in
[OTLP/gRPC Throttling](#otlpgrpc-throttling) section. If no such status is returned,
then the `RESOURCE_EXHAUSTED` code SHOULD be treated as non-retryable.

#### OTLP/gRPC Throttling

OTLP allows backpressure signaling.

If the server is unable to keep up with the pace of data it receives from the
client then it SHOULD signal that fact to the client. The client MUST then
throttle itself to avoid overwhelming the server.

To signal backpressure when using gRPC transport, the server SHOULD return an
error with code [Unavailable](https://godoc.org/google.golang.org/grpc/codes)
and MAY supply additional
[details via status](https://godoc.org/google.golang.org/grpc/status#Status.WithDetails)
using
[RetryInfo](https://github.com/googleapis/googleapis/blob/6a8c7914d1b79bd832b5157a09a9332e8cbd16d4/google/rpc/error_details.proto#L40).
Here is a snippet of sample Go code to illustrate:

```go
  // Do this on the server side.
  st, err := status.New(codes.Unavailable, "Server is unavailable").
    WithDetails(&errdetails.RetryInfo{RetryDelay: &duration.Duration{Seconds: 30}})
  if err != nil {
    log.Fatal(err)
  }

  return st.Err()

  ...

  // Do this on the client side.
  st := status.Convert(err)
  for _, detail := range st.Details() {
    switch t := detail.(type) {
    case *errdetails.RetryInfo:
      if t.RetryDelay.Seconds > 0 || t.RetryDelay.Nanos > 0 {
        // Wait before retrying.
      }
    }
  }
```

When the client receives this signal, it SHOULD follow the recommendations
outlined in documentation for
[RetryInfo](https://github.com/googleapis/googleapis/blob/6a8c7914d1b79bd832b5157a09a9332e8cbd16d4/google/rpc/error_details.proto#L40):

```
// Describes when the clients can retry a failed request. Clients could ignore
// the recommendation here or retry when this information is missing from the error
// responses.
//
// It's always recommended that clients should use exponential backoff when
// retrying.
//
// Clients should wait until `retry_delay` amount of time has passed since
// receiving the error response before retrying.  If retrying requests also
// fail, clients should use an exponential backoff scheme to increase gradually
// the delay between retries based on `retry_delay` until either a maximum
// number of retries has been reached, or a maximum retry delay cap has been
// reached.
```

The value of `retry_delay` is determined by the server and is implementation
dependant. The server SHOULD choose a `retry_delay` value that is big enough to
give the server time to recover yet is not too big to cause the client to drop
data while being throttled.

#### OTLP/gRPC Service and Protobuf Definitions

gRPC service definitions [are here](../opentelemetry/proto/collector).

Protobuf definitions for requests and responses [are here](../opentelemetry/proto).

Please make sure to check the proto version and [maturity level](../../../README.md#maturity-level).
Schemas for different signals may be at different maturity level - some stable,
some in beta.

#### OTLP/gRPC Default Port

The default network port for OTLP/gRPC is 4317.

### OTLP/HTTP

OTLP/HTTP uses Protobuf payloads encoded either in
[binary format](#binary-protobuf-encoding) or in [JSON format](#json-protobuf-encoding).
Regardless of the encoding the Protobuf schema of the messages is the same for
OTLP/HTTP and OTLP/gRPC as [defined here](../opentelemetry/proto).

OTLP/HTTP uses HTTP POST requests to send telemetry data from clients to
servers. Implementations MAY use HTTP/1.1 or HTTP/2 transports. Implementations
that use HTTP/2 transport SHOULD fallback to HTTP/1.1 transport if HTTP/2
connection cannot be established.

#### Binary Protobuf Encoding

Binary Protobuf encoded payloads use proto3
[encoding standard](https://developers.google.com/protocol-buffers/docs/encoding).

The client and the server MUST set "Content-Type: application/x-protobuf"
request and response headers when sending binary Protobuf encoded payload.

#### JSON Protobuf Encoding

JSON Protobuf encoded payloads use proto3 standard defined
[JSON Mapping](https://developers.google.com/protocol-buffers/docs/proto3#json)
for mapping between Protobuf and JSON, with the following deviations from that mapping:

- The `traceId` and `spanId` byte arrays are represented as
  [case-insensitive hex-encoded strings](https://tools.ietf.org/html/rfc4648#section-8);
  they are not base64-encoded as is defined in the standard
  [Protobuf JSON Mapping](https://developers.google.com/protocol-buffers/docs/proto3#json).
  Hex encoding is used for `traceId` and `spanId` fields in all OTLP
  Protobuf messages, e.g., the `Span`, `Link`, `LogRecord`, etc. messages.
  For example, the `traceId` field in a Span can be represented like this:
  { "traceId": "5B8EFFF798038103D269B633813FC60C", ... }

- Values of enum fields MUST be encoded as integer values. Unlike the standard
  [Protobuf JSON Mapping](https://developers.google.com/protocol-buffers/docs/proto3#json),
  which allows values of enum fields to be encoded as either integer values or
  as enum name strings, only integer enum values are allowed in OTLP JSON
  Protobuf Encoding; the enum name strings MUST NOT be used. For example, the
  `kind` field with a value of SPAN_KIND_SERVER in a Span can be represented
  like this: { "kind": 2, ... }

- OTLP/JSON receivers MUST ignore message fields with unknown names and MUST
  unmarshal the message as if the unknown field was not present in the payload.
  This aligns with the behavior of the Binary Protobuf unmarshaler and ensures
  that adding new fields to OTLP messages does not break existing receivers.

- The keys of JSON objects are field names converted to lowerCamelCase. Original
  field names are not valid to use as keys for JSON objects.
  For example, this is a valid JSON representation of a Resource:
  `{ "attributes": {...}, "droppedAttributesCount": 123 }`, and this is NOT a valid
  representation:
  `{ "attributes": {...}, "dropped_attributes_count": 123 }`.

Note that according to [Protobuf specs](
https://developers.google.com/protocol-buffers/docs/proto3#json) 64-bit integer
numbers in JSON-encoded payloads are encoded as decimal strings, and either
numbers or strings are accepted when decoding.

The client and the server MUST set "Content-Type: application/json" request and
response headers when sending JSON Protobuf encoded payload.

For JSON payload examples see: [OTLP JSON request examples](../../../README.md)

#### OTLP/HTTP Request

Telemetry data is sent via HTTP POST request. The body of the POST request is a
payload either in binary-encoded Protobuf format or in JSON-encoded Protobuf
format.

The default URL path for requests that carry trace data is `/v1/traces` (for
example the full URL when connecting to "example.com" server will be
`https://example.com/v1/traces`). The request body is a Protobuf-encoded
`ExportTraceServiceRequest` message.

The default URL path for requests that carry metric data is `/v1/metrics` and
the request body is a Protobuf-encoded `ExportMetricsServiceRequest` message.

The default URL path for requests that carry log data is `/v1/logs` and the
request body is a Protobuf-encoded `ExportLogsServiceRequest` message.

The default URL path for requests that carry profiling data is
`/v1development/profiles` and the request body is a Protobuf-encoded
`ExportProfilesServiceRequest` message.

The client MAY gzip the content and in that case MUST include
"Content-Encoding: gzip" request header. The client MAY include
"Accept-Encoding: gzip" request header if it can receive gzip-encoded responses.

Non-default URL paths for requests MAY be configured on the client and server
sides.

#### OTLP/HTTP Response

The response body MUST be the appropriate serialized Protobuf message (see
below for the specific message to use in the [Full Success](#full-success-1),
[Partial Success](#partial-success-1) and [Failure](#failures-1) cases).

The server MUST set "Content-Type: application/x-protobuf" header if the
response body is binary-encoded Protobuf payload. The server MUST set
"Content-Type: application/json" if the response is JSON-encoded Protobuf
payload. The server MUST use the same "Content-Type" in the response as it
received in the request.

If the request header "Accept-Encoding: gzip" is present in the request the
server MAY gzip-encode the response and set "Content-Encoding: gzip" response
header.

##### Full Success

The success response indicates telemetry data is successfully accepted by the
server.

If the server receives an empty request (a request that does not carry
any telemetry data) the server SHOULD respond with success.

On success, the server MUST respond with `HTTP 200 OK`. The response body MUST
be a Protobuf-encoded
[Export\<signal>ServiceResponse](../opentelemetry/proto/collector) message
(`ExportTraceServiceResponse` for traces, `ExportMetricsServiceResponse` for
metrics, `ExportLogsServiceResponse` for logs and
`ExportProfilesServiceResponse` for profiles).

The server MUST leave the `partial_success` field unset
in case of a successful response.

##### Partial Success

If the request is only partially accepted
(i.e. when the server accepts only parts of the data and rejects the rest), the
server MUST respond with `HTTP 200 OK`. The response body MUST be the same
[Export\<signal>ServiceResponse](../opentelemetry/proto/collector)
message as in the [Full Success](#full-success-1) case.

Additionally, the server MUST initialize the `partial_success` field
(`ExportTracePartialSuccess` message for traces, `ExportMetricsPartialSuccess`
message for metrics, `ExportLogsPartialSuccess` message for logs and
`ExportProfilesPartialSuccess` for profiles), and it MUST set the respective
`rejected_spans`, `rejected_data_points`, `rejected_log_records` or `rejected_profiles` field with
the number of spans/data points/log records it rejected.

The server SHOULD populate the `error_message` field with a human-readable
error message in English. The message should explain why the
server rejected parts of the data and might offer guidance on how users
can address the issues.
The protocol does not attempt to define the structure of the error message.

Servers MAY also use the `partial_success` field to convey
warnings/suggestions to clients even when it fully accepts the request.
In such cases, the `rejected_<signal>` field MUST have a value of `0`, and
the `error_message` field MUST be non-empty.

The client MUST NOT retry the request when it receives a partial success
response where the `partial_success` is populated.

##### Failures

If the processing of the request fails, the server MUST respond with appropriate
`HTTP 4xx` or `HTTP 5xx` status code. See the sections below for more details about
specific failure cases and HTTP status codes that should be used.

The response body for all `HTTP 4xx` and `HTTP 5xx` responses MUST be a
Protobuf-encoded
[Status](https://godoc.org/google.golang.org/genproto/googleapis/rpc/status#Status)
message that describes the problem.

This specification does not use `Status.code` field and the server MAY omit
`Status.code` field. The clients are not expected to alter their behavior based
on `Status.code` field but MAY record it for troubleshooting purposes.

The `Status.message` field SHOULD contain a developer-facing error message as
defined in `Status` message schema.

The server MAY include `Status.details` field with additional details. Read
below about what this field can contain in each specific failure case.

The server SHOULD use HTTP response status codes to indicate
retryable and not-retryable errors for a particular erroneous situation. The
client SHOULD honour HTTP response status codes as retryable or not-retryable.

##### Retryable Response Codes

The requests that receive a response status code listed in following table SHOULD
be retried.
All other `4xx` or `5xx` response status codes MUST NOT be retried.

|HTTP response status code|
|---------|
|429 Too Many Requests|
|502 Bad Gateway|
|503 Service Unavailable|
|504 Gateway Timeout|

##### Bad Data

If the processing of the request fails because the request contains data that
cannot be decoded or is otherwise invalid and such failure is permanent, then the
server MUST respond with `HTTP 400 Bad Request`. The `Status.details` field in
the response SHOULD contain a
[BadRequest](https://github.com/googleapis/googleapis/blob/d14bf59a446c14ef16e9931ebfc8e63ab549bf07/google/rpc/error_details.proto#L166)
that describes the bad data.

The client MUST NOT retry the request when it receives `HTTP 400 Bad Request`
response.

##### OTLP/HTTP Throttling

If the server receives more requests than the client is allowed or the server is
overloaded, the server SHOULD respond with `HTTP 429 Too Many Requests` or
`HTTP 503 Service Unavailable` and MAY include
["Retry-After"](https://tools.ietf.org/html/rfc7231#section-7.1.3) header with a
recommended time interval in seconds to wait before retrying.

The client SHOULD honour the waiting interval specified in the "Retry-After"
header if it is present. If the client receives a retryable error code (see
[table above](#retryable-response-codes)) and the "Retry-After" header is
not present in the response, then the client SHOULD implement an exponential backoff
strategy between retries.

##### All Other Responses

All other HTTP responses that are not explicitly listed in this document should
be treated according to HTTP specifications.

If the server disconnects without returning a response, the client SHOULD retry
and send the same request. The client SHOULD implement an exponential backoff
strategy between retries to avoid overwhelming the server.

#### OTLP/HTTP Connection

If the client cannot connect to the server, the client SHOULD retry the
connection using an exponential backoff strategy between retries. The interval
between retries must have a random jitter.

The client SHOULD keep the connection alive between requests.

Server implementations SHOULD accept OTLP/HTTP with binary-encoded Protobuf
payload and OTLP/HTTP with JSON-encoded Protobuf payload requests on the same
port and multiplex the requests to the corresponding payload decoder based on
the "Content-Type" request header.

Server implementations MAY accept OTLP/gRPC and OTLP/HTTP requests on the same
port and multiplex the connections to the corresponding transport handler based
on the "Content-Type" request header.

#### OTLP/HTTP Concurrent Requests

To achieve higher total throughput, the client MAY send requests using several
parallel HTTP connections. In that case, the maximum number of parallel
connections SHOULD be configurable.

#### OTLP/HTTP Default Port

The default network port for OTLP/HTTP is 4318.

## Implementation Recommendations

### Multi-Destination Exporting

An additional complication must be accounted for when one client must send
telemetry data to more than one destination server. When one of the servers
acknowledges the data and the other server does not (yet), the client needs
to decide how to move forward.

In such a situation, the client SHOULD implement queuing, acknowledgment
handling, and retrying logic per destination. This ensures that servers do not
block each other. The queues SHOULD reference shared, immutable data to be sent,
thus minimizing the memory overhead caused by having multiple queues.

![Multi-Destination Exporting](img/otlp-multi-destination.png)

This ensures that all destination servers receive the data regardless of their
speed of reception (within the available limits imposed by the size of the
client-side queue).

### Empty Telemetry Envelopes

Under certain circumstances, it is possible to have a telemetry envelope with
no contents. Some examples would be a ResourceMetrics with no ScopeMetrics
inside it, a ResourceMetrics with no Metrics inside it, or the equivalents for
Logs or Spans. One way this might happen would be for filtering rules to remove
all the contained data points, though there are others.

In practice, such empty envelopes are often discarded by existing
implementations. Given that, senders SHOULD NOT create empty envelopes (OTLP
payloads that contain zero spans, zero metric points or zero log records),
receivers MAY ignore empty envelopes, and implementations that receive and send
(forward) OTLP payloads MAY drop empty envelopes.

## Known Limitations

### Request Acknowledgements

#### Duplicate Data

In edge cases (e.g. on reconnections, network interruptions, etc) the client has
no way of knowing if recently sent data was delivered if no acknowledgement was
received yet. The client will typically choose to re-send such data to guarantee
delivery, which may result in duplicate data on the server side. This is a
deliberate choice and is considered to be the right tradeoff for telemetry data.

## Future Versions and Interoperability

OTLP will evolve and change over time. Future versions of OTLP must be designed
and implemented in a way that ensures that clients and servers that implement
different versions of OTLP can interoperate and exchange telemetry data. Old
clients must be able to talk to new servers and vice versa. Suppose new versions
of OTLP introduce new functionality that cannot be understood and supported by
nodes implementing the old versions of OTLP. In that case, the protocol must
regress to the lowest common denominator from a functional perspective.

When possible, the interoperability MUST be ensured between all versions of
OTLP that are not declared obsolete.

OTLP does not use explicit protocol version numbering. OTLP's interoperability
of clients and servers of different versions is based on the following concepts:

1. OTLP (current and future versions) defines a set of capabilities, some of
   which are mandatory, while others are optional. Clients and servers must implement
   mandatory capabilities and can choose to implement only a subset of optional
   capabilities.

2. For minor changes to the protocol, future versions and extensions of OTLP are
   encouraged to use the Protobuf's ability to evolve the message schema in
   a backward-compatible manner. Newer versions of OTLP may add new fields to
   messages that will be ignored by clients and servers that do not understand
   these fields. In many cases, careful design of such schema changes and correct
   choice of default values for new fields is enough to ensure interoperability
   of different versions without nodes explicitly detecting that their peer node
   has different capabilities.

3. More significant changes must be explicitly defined as new optional
   capabilities in future OTEPs. Such capabilities SHOULD be discovered by
   client and server implementations after establishing the underlying
   transport. The exact discovery mechanism SHOULD be described in future OTEPs,
   which define the new capabilities and typically can be implemented by making
   a discovery request/response message exchange from the client to server. The
   mandatory capabilities defined by this specification are implied and do not
   require discovery. The implementation which supports a new, optional
   capability MUST adjust its behavior to match the expectation of a peer that
   does not support a particular capability.

## Glossary

There are 2 parties involved in telemetry data exchange. In this document the
party that is the source of telemetry data is called the `Client`, the party
that is the destination of telemetry data is called the `Server`.

![Client-Server](img/otlp-client-server.png)

Examples of a Client are instrumented applications or sending side of telemetry
collectors, examples of Servers are telemetry backends or receiving side of
telemetry collectors (so a Collector is typically both a Client and a Server
depending on which side you look from).

Both the Client and the Server are also a `Node`. This term is used in the
document when referring to either one.

## References

- [OTEP 0035](https://github.com/open-telemetry/oteps/blob/main/text/0035-opentelemetry-protocol.md) OpenTelemetry Protocol Specification
- [OTEP 0099](https://github.com/open-telemetry/oteps/blob/main/text/0099-otlp-http.md) OTLP/HTTP: HTTP Transport Extension for OTLP
- [OTEP 0122](https://github.com/open-telemetry/oteps/blob/main/text/0122-otlp-http-json.md) OTLP: JSON Encoding for OTLP/HTTP
```

## File: `examples/README.md`
```markdown
# OTLP JSON request examples

This folder contains a collection of example OTLP JSON files for all signals
that can be used as request payloads.

- Trace [trace.json](trace.json)
- Metrics [metrics.json](metrics.json)
- Logs [logs.json](logs.json)
  - Events [events.json](events.json)

## Trying it out

First run a OpenTelemetry collector with the following configuration:

```yaml
receivers:
  otlp:
    protocols:
      http:

exporters:
  debug:
    verbosity: detailed

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [debug]
    metrics:
      receivers: [otlp]
      exporters: [debug]
    logs:
      receivers: [otlp]
      exporters: [debug]
```

Then send a curl request to the collector (e.g. for Logs):

```shell
curl -X POST -H "Content-Type: application/json" -d @logs.json -i localhost:4318/v1/logs
```

> Remember to change the URL path when sending other signals (traces/metrics).
```

## File: `examples/events.json`
```json
{
  "resourceLogs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "my.service"
            }
          }
        ]
      },
      "scopeLogs": [
        {
          "scope": {
            "name": "my.library",
            "version": "1.0.0",
            "attributes": [
              {
                "key": "my.scope.attribute",
                "value": {
                  "stringValue": "some scope attribute"
                }
              }
            ]
          },
          "logRecords": [
            {
              "eventName": "browser.page_view",
              "timeUnixNano": "1544712660300000000",
              "observedTimeUnixNano": "1544712660300000000",
              "severityNumber": 9,
              "severityText": "test severity text",
              "attributes": [
                {
                  "key": "event.attribute",
                  "value": {
                    "stringValue": "some event attribute"
                  }
                }
              ],
              "body": {
                "kvlistValue": {
                  "values": [
                    {
                      "key": "type",
                      "value": {
                        "intValue": "0"
                      }
                    },
                    {
                      "key": "url",
                      "value": {
                        "stringValue": "https://www.guidgenerator.com/online-guid-generator.aspx"
                      }
                    },
                    {
                      "key": "referrer",
                      "value": {
                        "stringValue": "https://wwww.google.com"
                      }
                    },
                    {
                      "key": "title",
                      "value": {
                        "stringValue": "Free Online GUID Generator"
                      }
                    }
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## File: `examples/logs.json`
```json
{
  "resourceLogs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "my.service"
            }
          }
        ]
      },
      "scopeLogs": [
        {
          "scope": {
            "name": "my.library",
            "version": "1.0.0",
            "attributes": [
              {
                "key": "my.scope.attribute",
                "value": {
                  "stringValue": "some scope attribute"
                }
              }
            ]
          },
          "logRecords": [
            {
              "timeUnixNano": "1544712660300000000",
              "observedTimeUnixNano": "1544712660300000000",
              "severityNumber": 10,
              "severityText": "Information",
              "traceId": "5B8EFFF798038103D269B633813FC60C",
              "spanId": "EEE19B7EC3C1B174",
              "body": {
                "stringValue": "Example log record"
              },
              "attributes": [
                {
                  "key": "string.attribute",
                  "value": {
                    "stringValue": "some string"
                  }
                },
                {
                  "key": "boolean.attribute",
                  "value": {
                    "boolValue": true
                  }
                },
                {
                  "key": "int.attribute",
                  "value": {
                    "intValue": "10"
                  }
                },
                {
                  "key": "double.attribute",
                  "value": {
                    "doubleValue": 637.704
                  }
                },
                {
                  "key": "array.attribute",
                  "value": {
                    "arrayValue": {
                      "values": [
                        {
                          "stringValue": "many"
                        },
                        {
                          "stringValue": "values"
                        }
                      ]
                    }
                  }
                },
                {
                  "key": "map.attribute",
                  "value": {
                    "kvlistValue": {
                      "values": [
                        {
                          "key": "some.map.key",
                          "value": {
                            "stringValue": "some value"
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## File: `examples/metrics.json`
```json
{
  "resourceMetrics": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "my.service"
            }
          }
        ]
      },
      "scopeMetrics": [
        {
          "scope": {
            "name": "my.library",
            "version": "1.0.0",
            "attributes": [
              {
                "key": "my.scope.attribute",
                "value": {
                  "stringValue": "some scope attribute"
                }
              }
            ]
          },
          "metrics": [
            {
              "name": "my.counter",
              "unit": "1",
              "description": "I am a Counter",
              "sum": {
                "aggregationTemporality": 1,
                "isMonotonic": true,
                "dataPoints": [
                  {
                    "asDouble": 5,
                    "startTimeUnixNano": "1544712660300000000",
                    "timeUnixNano": "1544712660300000000",
                    "attributes": [
                      {
                        "key": "my.counter.attr",
                        "value": {
                          "stringValue": "some value"
                        }
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "my.gauge",
              "unit": "1",
              "description": "I am a Gauge",
              "gauge": {
                "dataPoints": [
                  {
                    "asDouble": 10,
                    "timeUnixNano": "1544712660300000000",
                    "attributes": [
                      {
                        "key": "my.gauge.attr",
                        "value": {
                          "stringValue": "some value"
                        }
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "my.histogram",
              "unit": "1",
              "description": "I am a Histogram",
              "histogram": {
                "aggregationTemporality": 1,
                "dataPoints": [
                  {
                    "startTimeUnixNano": "1544712660300000000",
                    "timeUnixNano": "1544712660300000000",
                    "count": "2",
                    "sum": 2,
                    "bucketCounts": ["1","1"],
                    "explicitBounds": [1],
                    "min": 0,
                    "max": 2,
                    "attributes": [
                      {
                        "key": "my.histogram.attr",
                        "value": {
                          "stringValue": "some value"
                        }
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "my.exponential.histogram",
              "unit": "1",
              "description": "I am an Exponential Histogram",
              "exponentialHistogram": {
                "aggregationTemporality": 1,
                "dataPoints": [
                  {
                    "startTimeUnixNano": "1544712660300000000",
                    "timeUnixNano": "1544712660300000000",
                    "count": "3",
                    "sum": 10,
                    "scale": 0,
                    "zeroCount": "1",
                    "positive": {
                      "offset": 1,
                      "bucketCounts": ["0","2"]
                    },
                    "min": 0,
                    "max": 5,
                    "zeroThreshold": 0,
                    "attributes": [
                      {
                        "key": "my.exponential.histogram.attr",
                        "value": {
                          "stringValue": "some value"
                        }
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## File: `examples/trace.json`
```json
{
  "resourceSpans": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "my.service"
            }
          }
        ]
      },
      "scopeSpans": [
        {
          "scope": {
            "name": "my.library",
            "version": "1.0.0",
            "attributes": [
              {
                "key": "my.scope.attribute",
                "value": {
                  "stringValue": "some scope attribute"
                }
              }
            ]
          },
          "spans": [
            {
              "traceId": "5B8EFFF798038103D269B633813FC60C",
              "spanId": "EEE19B7EC3C1B174",
              "parentSpanId": "EEE19B7EC3C1B173",
              "name": "I'm a server span",
              "startTimeUnixNano": "1544712660000000000",
              "endTimeUnixNano": "1544712661000000000",
              "kind": 2,
              "attributes": [
                {
                  "key": "my.span.attr",
                  "value": {
                    "stringValue": "some value"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## File: `opentelemetry/proto/collector/README.md`
```markdown
# OpenTelemetry Collector Proto

This package describes the OpenTelemetry collector protocol.

## Packages

1. `common` package contains the common messages shared between different services.
2. `trace` package contains the Trace Service protos.
3. `metrics` package contains the Metrics Service protos.
4. `logs` package contains the Logs Service protos.
```

## File: `opentelemetry/proto/collector/logs/v1/logs_service.proto`
```
// Copyright 2020, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.collector.logs.v1;

import "opentelemetry/proto/logs/v1/logs.proto";

option csharp_namespace = "OpenTelemetry.Proto.Collector.Logs.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.collector.logs.v1";
option java_outer_classname = "LogsServiceProto";
option go_package = "go.opentelemetry.io/proto/otlp/collector/logs/v1";

// Service that can be used to push logs between one Application instrumented with
// OpenTelemetry and an collector, or between an collector and a central collector (in this
// case logs are sent/received to/from multiple Applications).
service LogsService {
  rpc Export(ExportLogsServiceRequest) returns (ExportLogsServiceResponse) {}
}

message ExportLogsServiceRequest {
  // An array of ResourceLogs.
  // For data coming from a single resource this array will typically contain one
  // element. Intermediary nodes (such as OpenTelemetry Collector) that receive
  // data from multiple origins typically batch the data before forwarding further and
  // in that case this array will contain multiple elements.
  repeated opentelemetry.proto.logs.v1.ResourceLogs resource_logs = 1;
}

message ExportLogsServiceResponse {
  // The details of a partially successful export request.
  //
  // If the request is only partially accepted
  // (i.e. when the server accepts only parts of the data and rejects the rest)
  // the server MUST initialize the `partial_success` field and MUST
  // set the `rejected_<signal>` with the number of items it rejected.
  //
  // Servers MAY also make use of the `partial_success` field to convey
  // warnings/suggestions to senders even when the request was fully accepted.
  // In such cases, the `rejected_<signal>` MUST have a value of `0` and
  // the `error_message` MUST be non-empty.
  //
  // A `partial_success` message with an empty value (rejected_<signal> = 0 and
  // `error_message` = "") is equivalent to it not being set/present. Senders
  // SHOULD interpret it the same way as in the full success case.
  ExportLogsPartialSuccess partial_success = 1;
}

message ExportLogsPartialSuccess {
  // The number of rejected log records.
  //
  // A `rejected_<signal>` field holding a `0` value indicates that the
  // request was fully accepted.
  int64 rejected_log_records = 1;

  // A developer-facing human-readable message in English. It should be used
  // either to explain why the server rejected parts of the data during a partial
  // success or to convey warnings/suggestions during a full success. The message
  // should offer guidance on how users can address such issues.
  //
  // error_message is an optional field. An error_message with an empty value
  // is equivalent to it not being set.
  string error_message = 2;
}
```

## File: `opentelemetry/proto/collector/logs/v1/logs_service_http.yaml`
```yaml
# This is an API configuration to generate an HTTP/JSON -> gRPC gateway for the
# OpenTelemetry service using github.com/grpc-ecosystem/grpc-gateway.
type: google.api.Service
config_version: 3
http:
 rules:
 - selector: opentelemetry.proto.collector.logs.v1.LogsService.Export
   post: /v1/logs
   body: "*"
```

## File: `opentelemetry/proto/collector/metrics/v1/metrics_service.proto`
```
// Copyright 2019, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.collector.metrics.v1;

import "opentelemetry/proto/metrics/v1/metrics.proto";

option csharp_namespace = "OpenTelemetry.Proto.Collector.Metrics.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.collector.metrics.v1";
option java_outer_classname = "MetricsServiceProto";
option go_package = "go.opentelemetry.io/proto/otlp/collector/metrics/v1";

// Service that can be used to push metrics between one Application
// instrumented with OpenTelemetry and a collector, or between a collector and a
// central collector.
service MetricsService {
  rpc Export(ExportMetricsServiceRequest) returns (ExportMetricsServiceResponse) {}
}

message ExportMetricsServiceRequest {
  // An array of ResourceMetrics.
  // For data coming from a single resource this array will typically contain one
  // element. Intermediary nodes (such as OpenTelemetry Collector) that receive
  // data from multiple origins typically batch the data before forwarding further and
  // in that case this array will contain multiple elements.
  repeated opentelemetry.proto.metrics.v1.ResourceMetrics resource_metrics = 1;
}

message ExportMetricsServiceResponse {
  // The details of a partially successful export request.
  //
  // If the request is only partially accepted
  // (i.e. when the server accepts only parts of the data and rejects the rest)
  // the server MUST initialize the `partial_success` field and MUST
  // set the `rejected_<signal>` with the number of items it rejected.
  //
  // Servers MAY also make use of the `partial_success` field to convey
  // warnings/suggestions to senders even when the request was fully accepted.
  // In such cases, the `rejected_<signal>` MUST have a value of `0` and
  // the `error_message` MUST be non-empty.
  //
  // A `partial_success` message with an empty value (rejected_<signal> = 0 and
  // `error_message` = "") is equivalent to it not being set/present. Senders
  // SHOULD interpret it the same way as in the full success case.
  ExportMetricsPartialSuccess partial_success = 1;
}

message ExportMetricsPartialSuccess {
  // The number of rejected data points.
  //
  // A `rejected_<signal>` field holding a `0` value indicates that the
  // request was fully accepted.
  int64 rejected_data_points = 1;

  // A developer-facing human-readable message in English. It should be used
  // either to explain why the server rejected parts of the data during a partial
  // success or to convey warnings/suggestions during a full success. The message
  // should offer guidance on how users can address such issues.
  //
  // error_message is an optional field. An error_message with an empty value
  // is equivalent to it not being set.
  string error_message = 2;
}
```

## File: `opentelemetry/proto/collector/metrics/v1/metrics_service_http.yaml`
```yaml
# This is an API configuration to generate an HTTP/JSON -> gRPC gateway for the
# OpenTelemetry service using github.com/grpc-ecosystem/grpc-gateway.
type: google.api.Service
config_version: 3
http:
 rules:
 - selector: opentelemetry.proto.collector.metrics.v1.MetricsService.Export
   post: /v1/metrics
   body: "*"
```

## File: `opentelemetry/proto/collector/profiles/v1development/profiles_service.proto`
```
// Copyright 2023, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.collector.profiles.v1development;

import "opentelemetry/proto/profiles/v1development/profiles.proto";

option csharp_namespace = "OpenTelemetry.Proto.Collector.Profiles.V1Development";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.collector.profiles.v1development";
option java_outer_classname = "ProfilesServiceProto";
option go_package = "go.opentelemetry.io/proto/otlp/collector/profiles/v1development";

// Service that can be used to push profiles between one Application instrumented with
// OpenTelemetry and a collector, or between a collector and a central collector.
service ProfilesService {
  rpc Export(ExportProfilesServiceRequest) returns (ExportProfilesServiceResponse) {}
}

// Status: [Alpha]
message ExportProfilesServiceRequest {
  // An array of ResourceProfiles.
  // For data coming from a single resource this array will typically contain one
  // element. Intermediary nodes (such as OpenTelemetry Collector) that receive
  // data from multiple origins typically batch the data before forwarding further and
  // in that case this array will contain multiple elements.
  repeated opentelemetry.proto.profiles.v1development.ResourceProfiles resource_profiles = 1;

  // The reference table containing all data shared by profiles across the message being sent.
  opentelemetry.proto.profiles.v1development.ProfilesDictionary dictionary = 2;
}

// Status: [Alpha]
message ExportProfilesServiceResponse {
  // The details of a partially successful export request.
  //
  // If the request is only partially accepted
  // (i.e. when the server accepts only parts of the data and rejects the rest)
  // the server MUST initialize the `partial_success` field and MUST
  // set the `rejected_<signal>` with the number of items it rejected.
  //
  // Servers MAY also make use of the `partial_success` field to convey
  // warnings/suggestions to senders even when the request was fully accepted.
  // In such cases, the `rejected_<signal>` MUST have a value of `0` and
  // the `error_message` MUST be non-empty.
  //
  // A `partial_success` message with an empty value (rejected_<signal> = 0 and
  // `error_message` = "") is equivalent to it not being set/present. Senders
  // SHOULD interpret it the same way as in the full success case.
  ExportProfilesPartialSuccess partial_success = 1;
}

// Status: [Alpha]
message ExportProfilesPartialSuccess {
  // The number of rejected profiles.
  //
  // A `rejected_<signal>` field holding a `0` value indicates that the
  // request was fully accepted.
  int64 rejected_profiles = 1;

  // A developer-facing human-readable message in English. It should be used
  // either to explain why the server rejected parts of the data during a partial
  // success or to convey warnings/suggestions during a full success. The message
  // should offer guidance on how users can address such issues.
  //
  // error_message is an optional field. An error_message with an empty value
  // is equivalent to it not being set.
  string error_message = 2;
}
```

## File: `opentelemetry/proto/collector/profiles/v1development/profiles_service_http.yaml`
```yaml
# This is an API configuration to generate an HTTP/JSON -> gRPC gateway for the
# OpenTelemetry service using github.com/grpc-ecosystem/grpc-gateway.
type: google.api.Service
config_version: 3
http:
 rules:
 - selector: opentelemetry.proto.collector.profiles.v1development.ProfilesService.Export
   post: /v1development/profiles
   body: "*"
```

## File: `opentelemetry/proto/collector/trace/v1/trace_service.proto`
```
// Copyright 2019, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.collector.trace.v1;

import "opentelemetry/proto/trace/v1/trace.proto";

option csharp_namespace = "OpenTelemetry.Proto.Collector.Trace.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.collector.trace.v1";
option java_outer_classname = "TraceServiceProto";
option go_package = "go.opentelemetry.io/proto/otlp/collector/trace/v1";

// Service that can be used to push spans between one Application instrumented with
// OpenTelemetry and a collector, or between a collector and a central collector (in this
// case spans are sent/received to/from multiple Applications).
service TraceService {
  rpc Export(ExportTraceServiceRequest) returns (ExportTraceServiceResponse) {}
}

message ExportTraceServiceRequest {
  // An array of ResourceSpans.
  // For data coming from a single resource this array will typically contain one
  // element. Intermediary nodes (such as OpenTelemetry Collector) that receive
  // data from multiple origins typically batch the data before forwarding further and
  // in that case this array will contain multiple elements.
  repeated opentelemetry.proto.trace.v1.ResourceSpans resource_spans = 1;
}

message ExportTraceServiceResponse {
  // The details of a partially successful export request.
  //
  // If the request is only partially accepted
  // (i.e. when the server accepts only parts of the data and rejects the rest)
  // the server MUST initialize the `partial_success` field and MUST
  // set the `rejected_<signal>` with the number of items it rejected.
  //
  // Servers MAY also make use of the `partial_success` field to convey
  // warnings/suggestions to senders even when the request was fully accepted.
  // In such cases, the `rejected_<signal>` MUST have a value of `0` and
  // the `error_message` MUST be non-empty.
  //
  // A `partial_success` message with an empty value (rejected_<signal> = 0 and
  // `error_message` = "") is equivalent to it not being set/present. Senders
  // SHOULD interpret it the same way as in the full success case.
  ExportTracePartialSuccess partial_success = 1;
}

message ExportTracePartialSuccess {
  // The number of rejected spans.
  //
  // A `rejected_<signal>` field holding a `0` value indicates that the
  // request was fully accepted.
  int64 rejected_spans = 1;

  // A developer-facing human-readable message in English. It should be used
  // either to explain why the server rejected parts of the data during a partial
  // success or to convey warnings/suggestions during a full success. The message
  // should offer guidance on how users can address such issues.
  //
  // error_message is an optional field. An error_message with an empty value
  // is equivalent to it not being set.
  string error_message = 2;
}
```

## File: `opentelemetry/proto/collector/trace/v1/trace_service_http.yaml`
```yaml
# This is an API configuration to generate an HTTP/JSON -> gRPC gateway for the
# OpenTelemetry service using github.com/grpc-ecosystem/grpc-gateway.
type: google.api.Service
config_version: 3
http:
 rules:
 - selector: opentelemetry.proto.collector.trace.v1.TraceService.Export
   post: /v1/traces
   body: "*"
```

## File: `opentelemetry/proto/common/v1/common.proto`
```
// Copyright 2019, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.common.v1;

option csharp_namespace = "OpenTelemetry.Proto.Common.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.common.v1";
option java_outer_classname = "CommonProto";
option go_package = "go.opentelemetry.io/proto/otlp/common/v1";

// Represents any type of attribute value. AnyValue may contain a
// primitive value such as a string or integer or it may contain an arbitrary nested
// object containing arrays, key-value lists and primitives.
message AnyValue {
  // The value is one of the listed fields. It is valid for all values to be unspecified
  // in which case this AnyValue is considered to be "empty".
  oneof value {
    string string_value = 1;
    bool bool_value = 2;
    int64 int_value = 3;
    double double_value = 4;
    ArrayValue array_value = 5;
    KeyValueList kvlist_value = 6;
    bytes bytes_value = 7;
    // Reference to the string value in ProfilesDictionary.string_table.
    //
    // Note: This is currently used exclusively in the Profiling signal.
    // Implementers of OTLP receivers for signals other than Profiling should
    // treat the presence of this value as a non-fatal issue.
    // Log an error or warning indicating an unexpected field intended for the
    // Profiling signal and process the data as if this value were absent or
    // empty, ignoring its semantic content for the non-Profiling signal.
    //
    // Status: [Alpha]
    int32 string_value_strindex = 8;
  }
}

// ArrayValue is a list of AnyValue messages. We need ArrayValue as a message
// since oneof in AnyValue does not allow repeated fields.
message ArrayValue {
  // Array of values. The array may be empty (contain 0 elements).
  repeated AnyValue values = 1;
}

// KeyValueList is a list of KeyValue messages. We need KeyValueList as a message
// since `oneof` in AnyValue does not allow repeated fields. Everywhere else where we need
// a list of KeyValue messages (e.g. in Span) we use `repeated KeyValue` directly to
// avoid unnecessary extra wrapping (which slows down the protocol). The 2 approaches
// are semantically equivalent.
message KeyValueList {
  // A collection of key/value pairs of key-value pairs. The list may be empty (may
  // contain 0 elements).
  //
  // The keys MUST be unique (it is not allowed to have more than one
  // value with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated KeyValue values = 1;
}

// Represents a key-value pair that is used to store Span attributes, Link
// attributes, etc.
message KeyValue {
  // The key name of the pair.
  // key_strindex MUST NOT be set if key is used.
  string key = 1;

  // The value of the pair.
  AnyValue value = 2;

  // Reference to the string key in ProfilesDictionary.string_table.
  // key MUST NOT be set if key_strindex is used.
  //
  // Note: This is currently used exclusively in the Profiling signal.
  // Implementers of OTLP receivers for signals other than Profiling should
  // treat the presence of this key as a non-fatal issue.
  // Log an error or warning indicating an unexpected field intended for the
  // Profiling signal and process the data as if this value were absent or
  // empty, ignoring its semantic content for the non-Profiling signal.
  //
  // Status: [Alpha]
  int32 key_strindex = 3;
}

// InstrumentationScope is a message representing the instrumentation scope information
// such as the fully qualified name and version. 
message InstrumentationScope {
  // A name denoting the Instrumentation scope.
  // An empty instrumentation scope name means the name is unknown.
  string name = 1;

  // Defines the version of the instrumentation scope.
  // An empty instrumentation scope version means the version is unknown.
  string version = 2;

  // Additional attributes that describe the scope. [Optional].
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated KeyValue attributes = 3;

  // The number of attributes that were discarded. Attributes
  // can be discarded because their keys are too long or because there are too many
  // attributes. If this value is 0, then no attributes were dropped.
  uint32 dropped_attributes_count = 4;
}

// A reference to an Entity.
// Entity represents an object of interest associated with produced telemetry: e.g spans, metrics, profiles, or logs.
//
// Status: [Development]
message EntityRef {
  // The Schema URL, if known. This is the identifier of the Schema that the entity data
  // is recorded in. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  //
  // This schema_url applies to the data in this message and to the Resource attributes
  // referenced by id_keys and description_keys.
  // TODO: discuss if we are happy with this somewhat complicated definition of what
  // the schema_url applies to.
  //
  // This field obsoletes the schema_url field in ResourceMetrics/ResourceSpans/ResourceLogs.
  string schema_url = 1;

  // Defines the type of the entity. MUST not change during the lifetime of the entity.
  // For example: "service" or "host". This field is required and MUST not be empty
  // for valid entities.
  string type = 2;

  // Attribute Keys that identify the entity.
  // MUST not change during the lifetime of the entity. The Id must contain at least one attribute.
  // These keys MUST exist in the containing {message}.attributes.
  repeated string id_keys = 3;

  // Descriptive (non-identifying) attribute keys of the entity.
  // MAY change over the lifetime of the entity. MAY be empty.
  // These attribute keys are not part of entity's identity.
  // These keys MUST exist in the containing {message}.attributes.
  repeated string description_keys = 4;
}
```

## File: `opentelemetry/proto/logs/v1/logs.proto`
```
// Copyright 2020, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.logs.v1;

import "opentelemetry/proto/common/v1/common.proto";
import "opentelemetry/proto/resource/v1/resource.proto";

option csharp_namespace = "OpenTelemetry.Proto.Logs.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.logs.v1";
option java_outer_classname = "LogsProto";
option go_package = "go.opentelemetry.io/proto/otlp/logs/v1";

// LogsData represents the logs data that can be stored in a persistent storage,
// OR can be embedded by other protocols that transfer OTLP logs data but do not
// implement the OTLP protocol.
//
// The main difference between this message and collector protocol is that
// in this message there will not be any "control" or "metadata" specific to
// OTLP protocol.
//
// When new fields are added into this message, the OTLP request MUST be updated
// as well.
message LogsData {
  // An array of ResourceLogs.
  // For data coming from a single resource this array will typically contain
  // one element. Intermediary nodes that receive data from multiple origins
  // typically batch the data before forwarding further and in that case this
  // array will contain multiple elements.
  repeated ResourceLogs resource_logs = 1;
}

// A collection of ScopeLogs from a Resource.
message ResourceLogs {
  reserved 1000;

  // The resource for the logs in this message.
  // If this field is not set then resource info is unknown.
  opentelemetry.proto.resource.v1.Resource resource = 1;

  // A list of ScopeLogs that originate from a resource.
  repeated ScopeLogs scope_logs = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the resource data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "resource" field. It does not apply
  // to the data in the "scope_logs" field which have their own schema_url field.
  string schema_url = 3;
}

// A collection of Logs produced by a Scope.
message ScopeLogs {
  // The instrumentation scope information for the logs in this message.
  // Semantically when InstrumentationScope isn't set, it is equivalent with
  // an empty instrumentation scope name (unknown).
  opentelemetry.proto.common.v1.InstrumentationScope scope = 1;

  // A list of log records.
  repeated LogRecord log_records = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the log data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "scope" field and all logs in the
  // "log_records" field.
  string schema_url = 3;
}

// Possible values for LogRecord.SeverityNumber.
enum SeverityNumber {
  SEVERITY_NUMBER_UNSPECIFIED = 0;
  SEVERITY_NUMBER_TRACE  = 1;
  SEVERITY_NUMBER_TRACE2 = 2;
  SEVERITY_NUMBER_TRACE3 = 3;
  SEVERITY_NUMBER_TRACE4 = 4;
  SEVERITY_NUMBER_DEBUG  = 5;
  SEVERITY_NUMBER_DEBUG2 = 6;
  SEVERITY_NUMBER_DEBUG3 = 7;
  SEVERITY_NUMBER_DEBUG4 = 8;
  SEVERITY_NUMBER_INFO   = 9;
  SEVERITY_NUMBER_INFO2  = 10;
  SEVERITY_NUMBER_INFO3  = 11;
  SEVERITY_NUMBER_INFO4  = 12;
  SEVERITY_NUMBER_WARN   = 13;
  SEVERITY_NUMBER_WARN2  = 14;
  SEVERITY_NUMBER_WARN3  = 15;
  SEVERITY_NUMBER_WARN4  = 16;
  SEVERITY_NUMBER_ERROR  = 17;
  SEVERITY_NUMBER_ERROR2 = 18;
  SEVERITY_NUMBER_ERROR3 = 19;
  SEVERITY_NUMBER_ERROR4 = 20;
  SEVERITY_NUMBER_FATAL  = 21;
  SEVERITY_NUMBER_FATAL2 = 22;
  SEVERITY_NUMBER_FATAL3 = 23;
  SEVERITY_NUMBER_FATAL4 = 24;
}

// LogRecordFlags represents constants used to interpret the
// LogRecord.flags field, which is protobuf 'fixed32' type and is to
// be used as bit-fields. Each non-zero value defined in this enum is
// a bit-mask.  To extract the bit-field, for example, use an
// expression like:
//
//   (logRecord.flags & LOG_RECORD_FLAGS_TRACE_FLAGS_MASK)
//
enum LogRecordFlags {
  // The zero value for the enum. Should not be used for comparisons.
  // Instead use bitwise "and" with the appropriate mask as shown above.
  LOG_RECORD_FLAGS_DO_NOT_USE = 0;

  // Bits 0-7 are used for trace flags.
  LOG_RECORD_FLAGS_TRACE_FLAGS_MASK = 0x000000FF;

  // Bits 8-31 are reserved for future use.
}

// A log record according to OpenTelemetry Log Data Model:
// https://github.com/open-telemetry/oteps/blob/main/text/logs/0097-log-data-model.md
message LogRecord {
  reserved 4;

  // time_unix_nano is the time when the event occurred.
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
  // Value of 0 indicates unknown or missing timestamp.
  fixed64 time_unix_nano = 1;

  // Time when the event was observed by the collection system.
  // For events that originate in OpenTelemetry (e.g. using OpenTelemetry Logging SDK)
  // this timestamp is typically set at the generation time and is equal to Timestamp.
  // For events originating externally and collected by OpenTelemetry (e.g. using
  // Collector) this is the time when OpenTelemetry's code observed the event measured
  // by the clock of the OpenTelemetry code. This field MUST be set once the event is
  // observed by OpenTelemetry.
  //
  // For converting OpenTelemetry log data to formats that support only one timestamp or
  // when receiving OpenTelemetry log data by recipients that support only one timestamp
  // internally the following logic is recommended:
  //   - Use time_unix_nano if it is present, otherwise use observed_time_unix_nano.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
  // Value of 0 indicates unknown or missing timestamp.
  fixed64 observed_time_unix_nano = 11;

  // Numerical value of the severity, normalized to values described in Log Data Model.
  // [Optional].
  SeverityNumber severity_number = 2;

  // The severity text (also known as log level). The original string representation as
  // it is known at the source. [Optional].
  string severity_text = 3;

  // A value containing the body of the log record. Can be for example a human-readable
  // string message (including multi-line) describing the event in a free form or it can
  // be a structured data composed of arrays and maps of other values. [Optional].
  opentelemetry.proto.common.v1.AnyValue body = 5;

  // Additional attributes that describe the specific event occurrence. [Optional].
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 6;
  uint32 dropped_attributes_count = 7;

  // Flags, a bit field. 8 least significant bits are the trace flags as
  // defined in W3C Trace Context specification. 24 most significant bits are reserved
  // and must be set to 0. Readers must not assume that 24 most significant bits
  // will be zero and must correctly mask the bits when reading 8-bit trace flag (use
  // flags & LOG_RECORD_FLAGS_TRACE_FLAGS_MASK). [Optional].
  fixed32 flags = 8;

  // A unique identifier for a trace. All logs from the same trace share
  // the same `trace_id`. The ID is a 16-byte array. An ID with all zeroes OR
  // of length other than 16 bytes is considered invalid (empty string in OTLP/JSON
  // is zero-length and thus is also invalid).
  //
  // This field is optional.
  //
  // The receivers SHOULD assume that the log record is not associated with a
  // trace if any of the following is true:
  //   - the field is not present,
  //   - the field contains an invalid value.
  bytes trace_id = 9;

  // A unique identifier for a span within a trace, assigned when the span
  // is created. The ID is an 8-byte array. An ID with all zeroes OR of length
  // other than 8 bytes is considered invalid (empty string in OTLP/JSON
  // is zero-length and thus is also invalid).
  //
  // This field is optional. If the sender specifies a valid span_id then it SHOULD also
  // specify a valid trace_id.
  //
  // The receivers SHOULD assume that the log record is not associated with a
  // span if any of the following is true:
  //   - the field is not present,
  //   - the field contains an invalid value.
  bytes span_id = 10;

  // A unique identifier of event category/type.
  // All events with the same event_name are expected to conform to the same
  // schema for both their attributes and their body.
  //
  // Recommended to be fully qualified and short (no longer than 256 characters).
  //
  // Presence of event_name on the log record identifies this record
  // as an event.
  //
  // [Optional].
  string event_name = 12;
}
```

## File: `opentelemetry/proto/metrics/v1/metrics.proto`
```
// Copyright 2019, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.metrics.v1;

import "opentelemetry/proto/common/v1/common.proto";
import "opentelemetry/proto/resource/v1/resource.proto";

option csharp_namespace = "OpenTelemetry.Proto.Metrics.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.metrics.v1";
option java_outer_classname = "MetricsProto";
option go_package = "go.opentelemetry.io/proto/otlp/metrics/v1";

// MetricsData represents the metrics data that can be stored in a persistent
// storage, OR can be embedded by other protocols that transfer OTLP metrics
// data but do not implement the OTLP protocol.
//
// MetricsData
// └─── ResourceMetrics
//   ├── Resource
//   ├── SchemaURL
//   └── ScopeMetrics
//      ├── Scope
//      ├── SchemaURL
//      └── Metric
//         ├── Name
//         ├── Description
//         ├── Unit
//         └── data
//            ├── Gauge
//            ├── Sum
//            ├── Histogram
//            ├── ExponentialHistogram
//            └── Summary
//
// The main difference between this message and collector protocol is that
// in this message there will not be any "control" or "metadata" specific to
// OTLP protocol.
//
// When new fields are added into this message, the OTLP request MUST be updated
// as well.
message MetricsData {
  // An array of ResourceMetrics.
  // For data coming from a single resource this array will typically contain
  // one element. Intermediary nodes that receive data from multiple origins
  // typically batch the data before forwarding further and in that case this
  // array will contain multiple elements.
  repeated ResourceMetrics resource_metrics = 1;
}

// A collection of ScopeMetrics from a Resource.
message ResourceMetrics {
  reserved 1000;

  // The resource for the metrics in this message.
  // If this field is not set then no resource info is known.
  opentelemetry.proto.resource.v1.Resource resource = 1;

  // A list of metrics that originate from a resource.
  repeated ScopeMetrics scope_metrics = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the resource data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "resource" field. It does not apply
  // to the data in the "scope_metrics" field which have their own schema_url field.
  string schema_url = 3;
}

// A collection of Metrics produced by an Scope.
message ScopeMetrics {
  // The instrumentation scope information for the metrics in this message.
  // Semantically when InstrumentationScope isn't set, it is equivalent with
  // an empty instrumentation scope name (unknown).
  opentelemetry.proto.common.v1.InstrumentationScope scope = 1;

  // A list of metrics that originate from an instrumentation library.
  repeated Metric metrics = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the metric data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "scope" field and all metrics in the
  // "metrics" field.
  string schema_url = 3;
}

// Defines a Metric which has one or more timeseries.  The following is a
// brief summary of the Metric data model.  For more details, see:
//
//   https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/data-model.md
//
// The data model and relation between entities is shown in the
// diagram below. Here, "DataPoint" is the term used to refer to any
// one of the specific data point value types, and "points" is the term used
// to refer to any one of the lists of points contained in the Metric.
//
// - Metric is composed of a metadata and data.
// - Metadata part contains a name, description, unit.
// - Data is one of the possible types (Sum, Gauge, Histogram, Summary).
// - DataPoint contains timestamps, attributes, and one of the possible value type
//   fields.
//
//    Metric
//  +------------+
//  |name        |
//  |description |
//  |unit        |     +------------------------------------+
//  |data        |---> |Gauge, Sum, Histogram, Summary, ... |
//  +------------+     +------------------------------------+
//
//    Data [One of Gauge, Sum, Histogram, Summary, ...]
//  +-----------+
//  |...        |  // Metadata about the Data.
//  |points     |--+
//  +-----------+  |
//                 |      +---------------------------+
//                 |      |DataPoint 1                |
//                 v      |+------+------+   +------+ |
//              +-----+   ||label |label |...|label | |
//              |  1  |-->||value1|value2|...|valueN| |
//              +-----+   |+------+------+   +------+ |
//              |  .  |   |+-----+                    |
//              |  .  |   ||value|                    |
//              |  .  |   |+-----+                    |
//              |  .  |   +---------------------------+
//              |  .  |                   .
//              |  .  |                   .
//              |  .  |                   .
//              |  .  |   +---------------------------+
//              |  .  |   |DataPoint M                |
//              +-----+   |+------+------+   +------+ |
//              |  M  |-->||label |label |...|label | |
//              +-----+   ||value1|value2|...|valueN| |
//                        |+------+------+   +------+ |
//                        |+-----+                    |
//                        ||value|                    |
//                        |+-----+                    |
//                        +---------------------------+
//
// Each distinct type of DataPoint represents the output of a specific
// aggregation function, the result of applying the DataPoint's
// associated function of to one or more measurements.
//
// All DataPoint types have three common fields:
// - Attributes includes key-value pairs associated with the data point
// - TimeUnixNano is required, set to the end time of the aggregation
// - StartTimeUnixNano is optional, but strongly encouraged for DataPoints
//   having an AggregationTemporality field, as discussed below.
//
// Both TimeUnixNano and StartTimeUnixNano values are expressed as
// UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
//
// # TimeUnixNano
//
// This field is required, having consistent interpretation across
// DataPoint types.  TimeUnixNano is the moment corresponding to when
// the data point's aggregate value was captured.
//
// Data points with the 0 value for TimeUnixNano SHOULD be rejected
// by consumers.
//
// # StartTimeUnixNano
//
// StartTimeUnixNano in general allows detecting when a sequence of
// observations is unbroken.  This field indicates to consumers the
// start time for points with cumulative and delta
// AggregationTemporality, and it should be included whenever possible
// to support correct rate calculation.  Although it may be omitted
// when the start time is truly unknown, setting StartTimeUnixNano is
// strongly encouraged.
message Metric {
  reserved 4, 6, 8;

  // The name of the metric.
  string name = 1;

  // A description of the metric, which can be used in documentation.
  string description = 2;

  // The unit in which the metric value is reported. Follows the format
  // described by https://unitsofmeasure.org/ucum.html.
  string unit = 3;

  // Data determines the aggregation type (if any) of the metric, what is the
  // reported value type for the data points, as well as the relatationship to
  // the time interval over which they are reported.
  oneof data {
    Gauge gauge = 5;
    Sum sum = 7;
    Histogram histogram = 9;
    ExponentialHistogram exponential_histogram = 10;
    Summary summary = 11;
  }

  // Additional metadata attributes that describe the metric. [Optional].
  // Attributes are non-identifying.
  // Consumers SHOULD NOT need to be aware of these attributes.
  // These attributes MAY be used to encode information allowing
  // for lossless roundtrip translation to / from another data model.
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue metadata = 12;
}

// Gauge represents the type of a scalar metric that always exports the
// "current value" for every data point. It should be used for an "unknown"
// aggregation.
//
// A Gauge does not support different aggregation temporalities. Given the
// aggregation is unknown, points cannot be combined using the same
// aggregation, regardless of aggregation temporalities. Therefore,
// AggregationTemporality is not included. Consequently, this also means
// "StartTimeUnixNano" is ignored for all data points.
message Gauge {
  // The time series data points.
  // Note: Multiple time series may be included (same timestamp, different attributes).
  repeated NumberDataPoint data_points = 1;
}

// Sum represents the type of a scalar metric that is calculated as a sum of all
// reported measurements over a time interval.
message Sum {
  // The time series data points.
  // Note: Multiple time series may be included (same timestamp, different attributes).
  repeated NumberDataPoint data_points = 1;

  // aggregation_temporality describes if the aggregator reports delta changes
  // since last report time, or cumulative changes since a fixed start time.
  AggregationTemporality aggregation_temporality = 2;

  // Represents whether the sum is monotonic.
  bool is_monotonic = 3;
}

// Histogram represents the type of a metric that is calculated by aggregating
// as a Histogram of all reported measurements over a time interval.
message Histogram {
  // The time series data points.
  // Note: Multiple time series may be included (same timestamp, different attributes).
  repeated HistogramDataPoint data_points = 1;

  // aggregation_temporality describes if the aggregator reports delta changes
  // since last report time, or cumulative changes since a fixed start time.
  AggregationTemporality aggregation_temporality = 2;
}

// ExponentialHistogram represents the type of a metric that is calculated by aggregating
// as a ExponentialHistogram of all reported double measurements over a time interval.
message ExponentialHistogram {
  // The time series data points.
  // Note: Multiple time series may be included (same timestamp, different attributes).
  repeated ExponentialHistogramDataPoint data_points = 1;

  // aggregation_temporality describes if the aggregator reports delta changes
  // since last report time, or cumulative changes since a fixed start time.
  AggregationTemporality aggregation_temporality = 2;
}

// Summary metric data are used to convey quantile summaries,
// a Prometheus (see: https://prometheus.io/docs/concepts/metric_types/#summary)
// and OpenMetrics (see: https://github.com/prometheus/OpenMetrics/blob/4dbf6075567ab43296eed941037c12951faafb92/protos/prometheus.proto#L45)
// data type. These data points cannot always be merged in a meaningful way.
// While they can be useful in some applications, histogram data points are
// recommended for new applications.
// Summary metrics do not have an aggregation temporality field. This is
// because the count and sum fields of a SummaryDataPoint are assumed to be
// cumulative values.
message Summary {
  // The time series data points.
  // Note: Multiple time series may be included (same timestamp, different attributes).
  repeated SummaryDataPoint data_points = 1;
}

// AggregationTemporality defines how a metric aggregator reports aggregated
// values. It describes how those values relate to the time interval over
// which they are aggregated.
enum AggregationTemporality {
  // UNSPECIFIED is the default AggregationTemporality, it MUST not be used.
  AGGREGATION_TEMPORALITY_UNSPECIFIED = 0;

  // DELTA is an AggregationTemporality for a metric aggregator which reports
  // changes since last report time. Successive metrics contain aggregation of
  // values from continuous and non-overlapping intervals.
  //
  // The values for a DELTA metric are based only on the time interval
  // associated with one measurement cycle. There is no dependency on
  // previous measurements like is the case for CUMULATIVE metrics.
  //
  // For example, consider a system measuring the number of requests that
  // it receives and reports the sum of these requests every second as a
  // DELTA metric:
  //
  //   1. The system starts receiving at time=t_0.
  //   2. A request is received, the system measures 1 request.
  //   3. A request is received, the system measures 1 request.
  //   4. A request is received, the system measures 1 request.
  //   5. The 1 second collection cycle ends. A metric is exported for the
  //      number of requests received over the interval of time t_0 to
  //      t_0+1 with a value of 3.
  //   6. A request is received, the system measures 1 request.
  //   7. A request is received, the system measures 1 request.
  //   8. The 1 second collection cycle ends. A metric is exported for the
  //      number of requests received over the interval of time t_0+1 to
  //      t_0+2 with a value of 2.
  AGGREGATION_TEMPORALITY_DELTA = 1;

  // CUMULATIVE is an AggregationTemporality for a metric aggregator which
  // reports changes since a fixed start time. This means that current values
  // of a CUMULATIVE metric depend on all previous measurements since the
  // start time. Because of this, the sender is required to retain this state
  // in some form. If this state is lost or invalidated, the CUMULATIVE metric
  // values MUST be reset and a new fixed start time following the last
  // reported measurement time sent MUST be used.
  //
  // For example, consider a system measuring the number of requests that
  // it receives and reports the sum of these requests every second as a
  // CUMULATIVE metric:
  //
  //   1. The system starts receiving at time=t_0.
  //   2. A request is received, the system measures 1 request.
  //   3. A request is received, the system measures 1 request.
  //   4. A request is received, the system measures 1 request.
  //   5. The 1 second collection cycle ends. A metric is exported for the
  //      number of requests received over the interval of time t_0 to
  //      t_0+1 with a value of 3.
  //   6. A request is received, the system measures 1 request.
  //   7. A request is received, the system measures 1 request.
  //   8. The 1 second collection cycle ends. A metric is exported for the
  //      number of requests received over the interval of time t_0 to
  //      t_0+2 with a value of 5.
  //   9. The system experiences a fault and loses state.
  //   10. The system recovers and resumes receiving at time=t_1.
  //   11. A request is received, the system measures 1 request.
  //   12. The 1 second collection cycle ends. A metric is exported for the
  //      number of requests received over the interval of time t_1 to
  //      t_0+1 with a value of 1.
  //
  // Note: Even though, when reporting changes since last report time, using
  // CUMULATIVE is valid, it is not recommended. This may cause problems for
  // systems that do not use start_time to determine when the aggregation
  // value was reset (e.g. Prometheus).
  AGGREGATION_TEMPORALITY_CUMULATIVE = 2;
}

// DataPointFlags is defined as a protobuf 'uint32' type and is to be used as a
// bit-field representing 32 distinct boolean flags.  Each flag defined in this
// enum is a bit-mask.  To test the presence of a single flag in the flags of
// a data point, for example, use an expression like:
//
//   (point.flags & DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK) == DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK
//
enum DataPointFlags {
  // The zero value for the enum. Should not be used for comparisons.
  // Instead use bitwise "and" with the appropriate mask as shown above.
  DATA_POINT_FLAGS_DO_NOT_USE = 0;

  // This DataPoint is valid but has no recorded value.  This value
  // SHOULD be used to reflect explicitly missing data in a series, as
  // for an equivalent to the Prometheus "staleness marker".
  DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1;

  // Bits 2-31 are reserved for future use.
}

// NumberDataPoint is a single data point in a timeseries that describes the
// time-varying scalar value of a metric.
message NumberDataPoint {
  reserved 1;

  // The set of key/value pairs that uniquely identify the timeseries from
  // where this point belongs. The list may be empty (may contain 0 elements).
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 7;

  // StartTimeUnixNano is optional but strongly encouraged, see the
  // the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 start_time_unix_nano = 2;

  // TimeUnixNano is required, see the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 time_unix_nano = 3;

  // The value itself.  A point is considered invalid when one of the recognized
  // value fields is not present inside this oneof.
  oneof value {
    double as_double = 4;
    sfixed64 as_int = 6;
  }

  // (Optional) List of exemplars collected from
  // measurements that were used to form the data point
  repeated Exemplar exemplars = 5;

  // Flags that apply to this specific data point.  See DataPointFlags
  // for the available flags and their meaning.
  uint32 flags = 8;
}

// HistogramDataPoint is a single data point in a timeseries that describes the
// time-varying values of a Histogram. A Histogram contains summary statistics
// for a population of values, it may optionally contain the distribution of
// those values across a set of buckets.
//
// If the histogram contains the distribution of values, then both
// "explicit_bounds" and "bucket counts" fields must be defined.
// If the histogram does not contain the distribution of values, then both
// "explicit_bounds" and "bucket_counts" must be omitted and only "count" and
// "sum" are known.
message HistogramDataPoint {
  reserved 1;

  // The set of key/value pairs that uniquely identify the timeseries from
  // where this point belongs. The list may be empty (may contain 0 elements).
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 9;

  // StartTimeUnixNano is optional but strongly encouraged, see the
  // the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 start_time_unix_nano = 2;

  // TimeUnixNano is required, see the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 time_unix_nano = 3;

  // count is the number of values in the population. Must be non-negative. This
  // value must be equal to the sum of the "count" fields in buckets if a
  // histogram is provided.
  fixed64 count = 4;

  // sum of the values in the population. If count is zero then this field
  // must be zero.
  //
  // Note: Sum should only be filled out when measuring non-negative discrete
  // events, and is assumed to be monotonic over the values of these events.
  // Negative events *can* be recorded, but sum should not be filled out when
  // doing so.  This is specifically to enforce compatibility w/ OpenMetrics,
  // see: https://github.com/prometheus/OpenMetrics/blob/v1.0.0/specification/OpenMetrics.md#histogram
  optional double sum = 5;

  // bucket_counts is an optional field contains the count values of histogram
  // for each bucket.
  //
  // The sum of the bucket_counts must equal the value in the count field.
  //
  // The number of elements in bucket_counts array must be by one greater than
  // the number of elements in explicit_bounds array. The exception to this rule
  // is when the length of bucket_counts is 0, then the length of explicit_bounds
  // must also be 0.
  repeated fixed64 bucket_counts = 6;

  // explicit_bounds specifies buckets with explicitly defined bounds for values.
  //
  // The boundaries for bucket at index i are:
  //
  // (-infinity, explicit_bounds[i]] for i == 0
  // (explicit_bounds[i-1], explicit_bounds[i]] for 0 < i < size(explicit_bounds)
  // (explicit_bounds[i-1], +infinity) for i == size(explicit_bounds)
  //
  // The values in the explicit_bounds array must be strictly increasing.
  //
  // Histogram buckets are inclusive of their upper boundary, except the last
  // bucket where the boundary is at infinity. This format is intentionally
  // compatible with the OpenMetrics histogram definition.
  //
  // If bucket_counts length is 0 then explicit_bounds length must also be 0,
  // otherwise the data point is invalid.
  repeated double explicit_bounds = 7;

  // (Optional) List of exemplars collected from
  // measurements that were used to form the data point
  repeated Exemplar exemplars = 8;

  // Flags that apply to this specific data point.  See DataPointFlags
  // for the available flags and their meaning.
  uint32 flags = 10;

  // min is the minimum value over (start_time, end_time].
  optional double min = 11;

  // max is the maximum value over (start_time, end_time].
  optional double max = 12;
}

// ExponentialHistogramDataPoint is a single data point in a timeseries that describes the
// time-varying values of a ExponentialHistogram of double values. A ExponentialHistogram contains
// summary statistics for a population of values, it may optionally contain the
// distribution of those values across a set of buckets.
//
message ExponentialHistogramDataPoint {
  // The set of key/value pairs that uniquely identify the timeseries from
  // where this point belongs. The list may be empty (may contain 0 elements).
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 1;

  // StartTimeUnixNano is optional but strongly encouraged, see the
  // the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 start_time_unix_nano = 2;

  // TimeUnixNano is required, see the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 time_unix_nano = 3;

  // The number of values in the population. Must be
  // non-negative. This value must be equal to the sum of the "bucket_counts"
  // values in the positive and negative Buckets plus the "zero_count" field.
  fixed64 count = 4;

  // The sum of the values in the population. If count is zero then this field
  // must be zero.
  //
  // Note: Sum should only be filled out when measuring non-negative discrete
  // events, and is assumed to be monotonic over the values of these events.
  // Negative events *can* be recorded, but sum should not be filled out when
  // doing so.  This is specifically to enforce compatibility w/ OpenMetrics,
  // see: https://github.com/prometheus/OpenMetrics/blob/v1.0.0/specification/OpenMetrics.md#histogram
  optional double sum = 5;

  // scale describes the resolution of the histogram.  Boundaries are
  // located at powers of the base, where:
  //
  //   base = (2^(2^-scale))
  //
  // The histogram bucket identified by `index`, a signed integer,
  // contains values that are greater than (base^index) and
  // less than or equal to (base^(index+1)).
  //
  // The positive and negative ranges of the histogram are expressed
  // separately.  Negative values are mapped by their absolute value
  // into the negative range using the same scale as the positive range.
  //
  // scale is not restricted by the protocol, as the permissible
  // values depend on the range of the data.
  sint32 scale = 6;

  // The count of values that are either exactly zero or
  // within the region considered zero by the instrumentation at the
  // tolerated degree of precision.  This bucket stores values that
  // cannot be expressed using the standard exponential formula as
  // well as values that have been rounded to zero.
  //
  // Implementations MAY consider the zero bucket to have probability
  // mass equal to (zero_count / count).
  fixed64 zero_count = 7;

  // positive carries the positive range of exponential bucket counts.
  Buckets positive = 8;

  // negative carries the negative range of exponential bucket counts.
  Buckets negative = 9;

  // Buckets are a set of bucket counts, encoded in a contiguous array
  // of counts.
  message Buckets {
    // The bucket index of the first entry in the bucket_counts array.
    //
    // Note: This uses a varint encoding as a simple form of compression.
    sint32 offset = 1;

    // An array of count values, where bucket_counts[i] carries
    // the count of the bucket at index (offset+i). bucket_counts[i] is the count
    // of values greater than base^(offset+i) and less than or equal to
    // base^(offset+i+1).
    //
    // Note: By contrast, the explicit HistogramDataPoint uses
    // fixed64.  This field is expected to have many buckets,
    // especially zeros, so uint64 has been selected to ensure
    // varint encoding.
    repeated uint64 bucket_counts = 2;
  }

  // Flags that apply to this specific data point.  See DataPointFlags
  // for the available flags and their meaning.
  uint32 flags = 10;

  // (Optional) List of exemplars collected from
  // measurements that were used to form the data point
  repeated Exemplar exemplars = 11;

  // The minimum value over (start_time, end_time].
  optional double min = 12;

  // The maximum value over (start_time, end_time].
  optional double max = 13;

  // ZeroThreshold may be optionally set to convey the width of the zero
  // region. Where the zero region is defined as the closed interval
  // [-ZeroThreshold, ZeroThreshold].
  // When ZeroThreshold is 0, zero count bucket stores values that cannot be
  // expressed using the standard exponential formula as well as values that
  // have been rounded to zero.
  double zero_threshold = 14;
}

// SummaryDataPoint is a single data point in a timeseries that describes the
// time-varying values of a Summary metric. The count and sum fields represent
// cumulative values.
message SummaryDataPoint {
  reserved 1;

  // The set of key/value pairs that uniquely identify the timeseries from
  // where this point belongs. The list may be empty (may contain 0 elements).
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 7;

  // StartTimeUnixNano is optional but strongly encouraged, see the
  // the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 start_time_unix_nano = 2;

  // TimeUnixNano is required, see the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 time_unix_nano = 3;

  // count is the number of values in the population. Must be non-negative.
  fixed64 count = 4;

  // sum of the values in the population. If count is zero then this field
  // must be zero.
  //
  // Note: Sum should only be filled out when measuring non-negative discrete
  // events, and is assumed to be monotonic over the values of these events.
  // Negative events *can* be recorded, but sum should not be filled out when
  // doing so.  This is specifically to enforce compatibility w/ OpenMetrics,
  // see: https://github.com/prometheus/OpenMetrics/blob/v1.0.0/specification/OpenMetrics.md#summary
  double sum = 5;

  // Represents the value at a given quantile of a distribution.
  //
  // To record Min and Max values following conventions are used:
  // - The 1.0 quantile is equivalent to the maximum value observed.
  // - The 0.0 quantile is equivalent to the minimum value observed.
  //
  // See the following issue for more context:
  // https://github.com/open-telemetry/opentelemetry-proto/issues/125
  message ValueAtQuantile {
    // The quantile of a distribution. Must be in the interval
    // [0.0, 1.0].
    double quantile = 1;

    // The value at the given quantile of a distribution.
    //
    // Quantile values must NOT be negative.
    double value = 2;
  }

  // (Optional) list of values at different quantiles of the distribution calculated
  // from the current snapshot. The quantiles must be strictly increasing.
  repeated ValueAtQuantile quantile_values = 6;

  // Flags that apply to this specific data point.  See DataPointFlags
  // for the available flags and their meaning.
  uint32 flags = 8;
}

// A representation of an exemplar, which is a sample input measurement.
// Exemplars also hold information about the environment when the measurement
// was recorded, for example the span and trace ID of the active span when the
// exemplar was recorded.
message Exemplar {
  reserved 1;

  // The set of key/value pairs that were filtered out by the aggregator, but
  // recorded alongside the original measurement. Only key/value pairs that were
  // filtered out by the aggregator should be included
  repeated opentelemetry.proto.common.v1.KeyValue filtered_attributes = 7;

  // time_unix_nano is the exact time when this exemplar was recorded
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 time_unix_nano = 2;

  // The value of the measurement that was recorded. An exemplar is
  // considered invalid when one of the recognized value fields is not present
  // inside this oneof.
  oneof value {
    double as_double = 3;
    sfixed64 as_int = 6;
  }

  // (Optional) Span ID of the exemplar trace.
  // span_id may be missing if the measurement is not recorded inside a trace
  // or if the trace is not sampled.
  bytes span_id = 4;

  // (Optional) Trace ID of the exemplar trace.
  // trace_id may be missing if the measurement is not recorded inside a trace
  // or if the trace is not sampled.
  bytes trace_id = 5;
}
```

## File: `opentelemetry/proto/profiles/v1development/profiles.proto`
```
// Copyright 2023, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// This file includes work covered by the following copyright and permission notices:
//
// Copyright 2016 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.profiles.v1development;

import "opentelemetry/proto/common/v1/common.proto";
import "opentelemetry/proto/resource/v1/resource.proto";

option csharp_namespace = "OpenTelemetry.Proto.Profiles.V1Development";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.profiles.v1development";
option java_outer_classname = "ProfilesProto";
option go_package = "go.opentelemetry.io/proto/otlp/profiles/v1development";

//                Relationships Diagram
//
// ┌──────────────────┐                      LEGEND
// │   ProfilesData   │ ─────┐
// └──────────────────┘      │           ─────▶ embedded
//   │                       │
//   │ 1-n                   │           ─────▷ referenced by index
//   ▼                       ▼
// ┌──────────────────┐   ┌────────────────────┐
// │ ResourceProfiles │   │ ProfilesDictionary │
// └──────────────────┘   └────────────────────┘
//   │
//   │ 1-n
//   ▼
// ┌──────────────────┐
// │  ScopeProfiles   │
// └──────────────────┘
//   │
//   │ 1-n
//   ▼
// ┌──────────────────┐
// │      Profile     │
// └──────────────────┘
//   │                                n-1
//   │ 1-n         ┌───────────────────────────────────────┐
//   ▼             │                                       ▽
// ┌──────────────────┐   1-n   ┌─────────────────┐   ┌──────────┐
// │      Sample      │ ──────▷ │ KeyValueAndUnit │   │   Link   │
// └──────────────────┘         └─────────────────┘   └──────────┘
//   │                              △      △
//   │ n-1                          │      │ 1-n
//   ▽                              │      │
// ┌──────────────────┐             │      │
// │      Stack       │             │      │
// └──────────────────┘             │      │
//   │                     1-n      │      │
//   │ 1-n         ┌────────────────┘      │
//   ▽             │                       │
// ┌──────────────────┐   n-1   ┌─────────────┐
// │     Location     │ ──────▷ │   Mapping   │
// └──────────────────┘         └─────────────┘
//   │
//   │ 1-n
//   ▼
// ┌──────────────────┐
// │       Line       │
// └──────────────────┘
//   │
//   │ 1-1
//   ▽
// ┌──────────────────┐
// │     Function     │
// └──────────────────┘
//

// ProfilesDictionary represents the profiles data shared across the
// entire message being sent. The following applies to all fields in this
// message:
//
// - A dictionary is an array of dictionary items. Users of the dictionary
//   compactly reference the items using the index within the array.
//
// - A dictionary MUST have a zero value encoded as the first element. This
//   allows for _index fields pointing into the dictionary to use a 0 pointer
//   value to indicate 'null' / 'not set'. Unless otherwise defined, a 'zero
//   value' message value is one with all default field values, so as to
//   minimize wire encoded size.
//
// - There SHOULD NOT be dupes in a dictionary. The identity of dictionary
//   items is based on their value, recursively as needed. If a particular
//   implementation does emit duplicated items, it MUST NOT attempt to give them
//   meaning based on the index or order. A profile processor may remove
//   duplicate items and this MUST NOT have any observable effects for
//   consumers.
//
// - There SHOULD NOT be orphaned (unreferenced) items in a dictionary. A
//   profile processor may remove ("garbage-collect") orphaned items and this
//   MUST NOT have any observable effects for consumers.
//
// Status: [Alpha]
message ProfilesDictionary {
  // Mappings from address ranges to the image/binary/library mapped
  // into that address range referenced by locations via Location.mapping_index.
  //
  // mapping_table[0] must always be zero value (Mapping{}) and present.
  repeated Mapping mapping_table = 1;

  // Locations referenced by samples via Stack.location_indices.
  //
  // location_table[0] must always be zero value (Location{}) and present.
  repeated Location location_table = 2;

  // Functions referenced by locations via Line.function_index.
  //
  // function_table[0] must always be zero value (Function{}) and present.
  repeated Function function_table = 3;

  // Links referenced by samples via Sample.link_index.
  //
  // link_table[0] must always be zero value (Link{}) and present.
  repeated Link link_table = 4;

  // A common table for strings referenced by various messages.
  //
  // string_table[0] must always be "" and present.
  repeated string string_table = 5;

  // A common table for attributes referenced by the Profile, Sample, Mapping
  // and Location messages below through attribute_indices field. Each entry is
  // a key/value pair with an optional unit. Since this is a dictionary table,
  // multiple entries with the same key may be present, unlike direct attribute
  // tables like Resource.attributes. The referencing attribute_indices fields,
  // though, do maintain the key uniqueness requirement.
  //
  // It's recommended to use attributes for variables with bounded cardinality,
  // such as categorical variables
  // (https://en.wikipedia.org/wiki/Categorical_variable). Using an attribute of
  // a floating point type (e.g., CPU time) in a sample can quickly make every
  // attribute value unique, defeating the purpose of the dictionary and
  // impractically increasing the profile size.
  //
  // Examples of attributes:
  //     "/http/user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
  //     "abc.com/myattribute": true
  //     "allocation_size": 128 bytes
  //
  // attribute_table[0] must always be zero value (KeyValueAndUnit{}) and present.
  repeated KeyValueAndUnit attribute_table = 6;

  // Stacks referenced by samples via Sample.stack_index.
  //
  // stack_table[0] must always be zero value (Stack{}) and present.
  repeated Stack stack_table = 7;
}

// ProfilesData represents the profiles data that can be stored in persistent storage,
// OR can be embedded by other protocols that transfer OTLP profiles data but do not
// implement the OTLP protocol.
//
// The main difference between this message and collector protocol is that
// in this message there will not be any "control" or "metadata" specific to
// OTLP protocol.
//
// When new fields are added into this message, the OTLP request MUST be updated
// as well.
//
// Status: [Alpha]
message ProfilesData {
  // An array of ResourceProfiles.
  // For data coming from an SDK profiler, this array will typically contain one
  // element. Host-level profilers will usually create one ResourceProfile per
  // container, as well as one additional ResourceProfile grouping all samples
  // from non-containerized processes.
  // Other resource groupings are possible as well and clarified via
  // Resource.attributes and semantic conventions.
  // Tools that visualize profiles should prefer displaying
  // resources_profiles[0].scope_profiles[0].profiles[0] by default.
  repeated ResourceProfiles resource_profiles = 1;

  // One instance of ProfilesDictionary
  ProfilesDictionary dictionary = 2;
}


// A collection of ScopeProfiles from a Resource.
//
// Status: [Alpha]
message ResourceProfiles {
  reserved 1000;

  // The resource for the profiles in this message.
  // If this field is not set then no resource info is known.
  opentelemetry.proto.resource.v1.Resource resource = 1;

  // A list of ScopeProfiles that originate from a resource.
  repeated ScopeProfiles scope_profiles = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the resource data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "resource" field. It does not apply
  // to the data in the "scope_profiles" field which have their own schema_url field.
  string schema_url = 3;
}

// A collection of Profiles produced by an InstrumentationScope.
//
// Status: [Alpha]
message ScopeProfiles {
  // The instrumentation scope information for the profiles in this message.
  // Semantically when InstrumentationScope isn't set, it is equivalent with
  // an empty instrumentation scope name (unknown).
  opentelemetry.proto.common.v1.InstrumentationScope scope = 1;

  // A list of Profiles that originate from an instrumentation scope.
  repeated Profile profiles = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the profile data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "scope" field and all profiles in the
  // "profiles" field.
  string schema_url = 3;
}

// Profile is a common stacktrace profile format.
//
// Measurements represented with this format should follow the
// following conventions:
//
// - Consumers should treat unset optional fields as if they had been
//   set with their default value.
//
// - When possible, measurements should be stored in "unsampled" form
//   that is most useful to humans.  There should be enough
//   information present to determine the original sampled values.
//
// - The profile is represented as a set of samples, where each sample
//   references a stack trace which is a list of locations, each belonging
//   to a mapping.
// - There is a N->1 relationship from Stack.location_indices entries to
//   locations. For every Stack.location_indices entry there must be a
//   unique Location with that index.
// - There is an optional N->1 relationship from locations to
//   mappings. For every nonzero Location.mapping_id there must be a
//   unique Mapping with that index.

// Represents a complete profile, including sample types, samples, mappings to
// binaries, stacks, locations, functions, string table, and additional
// metadata. It modifies and annotates pprof Profile with OpenTelemetry
// specific fields.
//
// Note that whilst fields in this message retain the name and field id from pprof in most cases
// for ease of understanding data migration, it is not intended that pprof:Profile and
// OpenTelemetry:Profile encoding be wire compatible.
//
// Status: [Alpha]
message Profile {
  // The type and unit of all Sample.values in this profile.
  // For a cpu or off-cpu profile this might be:
  //   ["cpu","nanoseconds"] or ["off_cpu","nanoseconds"]
  // For a heap profile, this might be:
  //   ["allocated_objects","count"] or ["allocated_space","bytes"],
  ValueType sample_type = 1;
  // The set of samples recorded in this profile.
  repeated Sample samples = 2;

  // The following fields 3-12 are informational, do not affect
  // interpretation of results.

  // Time of collection. Value is UNIX Epoch time in nanoseconds since 00:00:00
  // UTC on 1 January 1970.
  fixed64 time_unix_nano = 3;
  // Duration of the profile. For instant profiles like live heap snapshot, the
  // duration can be zero but it may be preferable to set time_unix_nano to the
  // process start time and duration_nano to the relative time when the profile
  // was gathered. This ensures Sample.timestamps_unix_nano values such as
  // allocation timestamp fall into the profile time range.
  uint64 duration_nano = 4;
  // The kind of events between sampled occurrences.
  // e.g [ "cpu","cycles" ] or [ "heap","bytes" ]
  ValueType period_type = 5;
  // The number of events between sampled occurrences.
  int64 period = 6;

  // A globally unique identifier for a profile. The ID is a 16-byte array. An ID with
  // all zeroes is considered invalid. It may be used for deduplication and signal
  // correlation purposes. It is acceptable to treat two profiles with different values
  // in this field as not equal, even if they represented the same object at an earlier
  // time.
  // This field is optional; an ID may be assigned to an ID-less profile in a later step.
  bytes profile_id = 7;

  // The number of attributes that were discarded. Attributes
  // can be discarded because their keys are too long or because there are too many
  // attributes. If this value is 0, then no attributes were dropped.
  uint32 dropped_attributes_count = 8;

  // The original payload format. See also original_payload. Optional, but the
  // format and the bytes must be set or unset together.
  //
  // The allowed values for the format string are defined by the OpenTelemetry
  // specification. Some examples are "jfr", "pprof", "linux_perf".
  //
  // The original payload may be optionally provided when the conversion to the
  // OLTP format was done from a different format with some loss of the fidelity
  // and the receiver may want to store the original payload to allow future
  // lossless export or reinterpretation. Some examples of the original format
  // are JFR (Java Flight Recorder), pprof, Linux perf.
  //
  // Even when the original payload is in a format that is semantically close to
  // OTLP, such as pprof, a conversion may still be lossy in some cases (e.g. if
  // the pprof file contains custom extensions or conventions).
  //
  // The original payload can be large in size, so including the original
  // payload should be configurable by the profiler or collector options. The
  // default behavior should be to not include the original payload.
  string original_payload_format = 9;
  // The original payload bytes. See also original_payload_format. Optional, but
  // format and the bytes must be set or unset together.
  bytes original_payload = 10;

  // References to attributes in attribute_table. [optional]
  repeated int32 attribute_indices = 11;
}

// A pointer from a profile Sample to a trace Span.
// Connects a profile sample to a trace span, identified by unique trace and span IDs.
//
// Status: [Alpha]
message Link {
  // A unique identifier of a trace that this linked span is part of. The ID is a
  // 16-byte array.
  bytes trace_id = 1;

  // A unique identifier for the linked span. The ID is an 8-byte array.
  bytes span_id = 2;
}

// ValueType describes the type and units of a value.
//
// Status: [Alpha]
message ValueType {
  // Index into ProfilesDictionary.string_table.
  int32 type_strindex = 1;

  // Index into ProfilesDictionary.string_table.
  int32 unit_strindex = 2;
}

// Each Sample records values encountered in some program context. The program
// context is typically a stack trace, perhaps augmented with auxiliary
// information like the thread-id, some indicator of a higher level request
// being handled etc.
//
// A Sample MUST have have at least one values or timestamps_unix_nano entry. If
// both fields are populated, they MUST contain the same number of elements, and
// the elements at the same index MUST refer to the same event.
//
// For the purposes of efficiently representing aggregated data observations, a Sample is regarded
// as having a shared identity and an associated collection of per-observation data points.
// Samples having the same identity SHOULD be combined by inserting timestamps and values to the data arrays.
//
// Examples of different ways ('shapes') of representing a sample with the total value of 10:
//
// Report of a stacktrace at 10 timestamps (consumers must assume the value is 1 for each point):
//    values: []
//    timestamps_unix_nano: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
//
// Report of a stacktrace with an aggregated value without timestamps:
//   values: [10]
//    timestamps_unix_nano: []
//
// Report of a stacktrace at 4 timestamps where each point records a specific value:
//    values: [2, 2, 3, 3]
//    timestamps_unix_nano: [1, 2, 3, 4]
//
// All Samples for a Profile SHOULD have the same shape, i.e. all data observation series should consistently
// adopt the same data recording style.
//
// Status: [Alpha]
message Sample {

  // A Sample's identity (i.e. 'primary key') is the tuple of {stack_index, set_of(attribute_indices), link_index}

  // Reference to stack in ProfilesDictionary.stack_table.
  int32 stack_index = 1;
  // References to attributes in ProfilesDictionary.attribute_table. [optional]
  repeated int32 attribute_indices = 2;
  // Reference to link in ProfilesDictionary.link_table. [optional]
  // It can be unset / set to 0 if no link exists, as link_table[0] is always a 'null' default value.
  int32 link_index = 3;

  // The following fields may contain per-observation data and do not form part of the Sample's identity.

  // The type and unit of each value is defined by Profile.sample_type.
  repeated int64 values = 4;
  // Timestamps associated with Sample. Value is UNIX Epoch time in nanoseconds
  // since 00:00:00 UTC on 1 January 1970. The timestamps should fall within the
  // [Profile.time_unix_nano, Profile.time_unix_nano + Profile.duration_nano)
  // time range.
  repeated fixed64 timestamps_unix_nano = 5;
}

// Describes the mapping of a binary in memory, including its address range,
// file offset, and metadata like build ID
//
// Status: [Alpha]
message Mapping {
  // Address at which the binary (or DLL) is loaded into memory.
  uint64 memory_start = 1;
  // The limit of the address range occupied by this mapping.
  uint64 memory_limit = 2;
  // Offset in the binary that corresponds to the first mapped address.
  uint64 file_offset = 3;
  // The object this entry is loaded from.  This can be a filename on
  // disk for the main binary and shared libraries, or virtual
  // abstractions like "[vdso]".
  int32 filename_strindex = 4;  // Index into ProfilesDictionary.string_table.
  // References to attributes in ProfilesDictionary.attribute_table. [optional]
  repeated int32 attribute_indices = 5;
}

// A Stack represents a stack trace as a list of locations.
//
// Status: [Alpha]
message Stack {
  // References to locations in ProfilesDictionary.location_table.
  // The first location is the leaf frame.
  repeated int32 location_indices = 1;
}

// Describes function and line table debug information.
//
// Status: [Alpha]
message Location {
  // Reference to mapping in ProfilesDictionary.mapping_table.
  // It can be unset / set to 0 if the mapping is unknown or not applicable for
  // this profile type, as mapping_table[0] is always a 'null' default mapping.
  int32 mapping_index = 1;
  // The instruction address for this location, if available.  It
  // should be within [Mapping.memory_start...Mapping.memory_limit]
  // for the corresponding mapping. A non-leaf address may be in the
  // middle of a call instruction. It is up to display tools to find
  // the beginning of the instruction if necessary.
  uint64 address = 2;
  // Multiple line indicates this location has inlined functions,
  // where the last entry represents the caller into which the
  // preceding entries were inlined.
  //
  // E.g., if memcpy() is inlined into printf:
  //    lines[0].function_name == "memcpy"
  //    lines[1].function_name == "printf"
  repeated Line lines = 3;
  // References to attributes in ProfilesDictionary.attribute_table. [optional]
  repeated int32 attribute_indices = 4;
}

// Details a specific line in a source code, linked to a function.
//
// Status: [Alpha]
message Line {
  // Reference to function in ProfilesDictionary.function_table.
  int32 function_index = 1;
  // Line number in source code. 0 means unset.
  int64 line = 2;
  // Column number in source code. 0 means unset.
  int64 column = 3;
}

// Describes a function, including its human-readable name, system name,
// source file, and starting line number in the source.
//
// Status: [Alpha]
message Function {
  // The function name. Empty string if not available.
  int32 name_strindex = 1;
  // Function name, as identified by the system. For instance,
  // it can be a C++ mangled name. Empty string if not available.
  int32 system_name_strindex = 2;
  // Source file containing the function. Empty string if not available.
  int32 filename_strindex = 3;
  // Line number in source file. 0 means unset.
  int64 start_line = 4;
}

// A custom 'dictionary native' style of encoding attributes which is more convenient
// for profiles than opentelemetry.proto.common.v1.KeyValue
// Specifically, uses the string table for keys and allows optional unit information.
//
// Status: [Alpha]
message KeyValueAndUnit {
  // The index into the string table for the attribute's key.
  int32 key_strindex  = 1;
  // The value of the attribute.
  opentelemetry.proto.common.v1.AnyValue value = 2;
  // The index into the string table for the attribute's unit.
  // zero indicates implicit (by semconv) or non-defined unit.
  int32 unit_strindex = 3;
}
```

## File: `opentelemetry/proto/resource/v1/resource.proto`
```
// Copyright 2019, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.resource.v1;

import "opentelemetry/proto/common/v1/common.proto";

option csharp_namespace = "OpenTelemetry.Proto.Resource.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.resource.v1";
option java_outer_classname = "ResourceProto";
option go_package = "go.opentelemetry.io/proto/otlp/resource/v1";

// Resource information.
message Resource {
  // Set of attributes that describe the resource.
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 1;

  // The number of dropped attributes. If the value is 0, then
  // no attributes were dropped.
  uint32 dropped_attributes_count = 2;

  // Set of entities that participate in this Resource.
  //
  // Note: keys in the references MUST exist in attributes of this message.
  //
  // Status: [Development]
  repeated opentelemetry.proto.common.v1.EntityRef entity_refs = 3;
}
```

## File: `opentelemetry/proto/trace/v1/trace.proto`
```
// Copyright 2019, OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

syntax = "proto3";

package opentelemetry.proto.trace.v1;

import "opentelemetry/proto/common/v1/common.proto";
import "opentelemetry/proto/resource/v1/resource.proto";

option csharp_namespace = "OpenTelemetry.Proto.Trace.V1";
option java_multiple_files = true;
option java_package = "io.opentelemetry.proto.trace.v1";
option java_outer_classname = "TraceProto";
option go_package = "go.opentelemetry.io/proto/otlp/trace/v1";

// TracesData represents the traces data that can be stored in a persistent storage,
// OR can be embedded by other protocols that transfer OTLP traces data but do
// not implement the OTLP protocol.
//
// The main difference between this message and collector protocol is that
// in this message there will not be any "control" or "metadata" specific to
// OTLP protocol.
//
// When new fields are added into this message, the OTLP request MUST be updated
// as well.
message TracesData {
  // An array of ResourceSpans.
  // For data coming from a single resource this array will typically contain
  // one element. Intermediary nodes that receive data from multiple origins
  // typically batch the data before forwarding further and in that case this
  // array will contain multiple elements.
  repeated ResourceSpans resource_spans = 1;
}

// A collection of ScopeSpans from a Resource.
message ResourceSpans {
  reserved 1000;

  // The resource for the spans in this message.
  // If this field is not set then no resource info is known.
  opentelemetry.proto.resource.v1.Resource resource = 1;

  // A list of ScopeSpans that originate from a resource.
  repeated ScopeSpans scope_spans = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the resource data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "resource" field. It does not apply
  // to the data in the "scope_spans" field which have their own schema_url field.
  string schema_url = 3;
}

// A collection of Spans produced by an InstrumentationScope.
message ScopeSpans {
  // The instrumentation scope information for the spans in this message.
  // Semantically when InstrumentationScope isn't set, it is equivalent with
  // an empty instrumentation scope name (unknown).
  opentelemetry.proto.common.v1.InstrumentationScope scope = 1;

  // A list of Spans that originate from an instrumentation scope.
  repeated Span spans = 2;

  // The Schema URL, if known. This is the identifier of the Schema that the span data
  // is recorded in. Notably, the last part of the URL path is the version number of the
  // schema: http[s]://server[:port]/path/<version>. To learn more about Schema URL see
  // https://opentelemetry.io/docs/specs/otel/schemas/#schema-url
  // This schema_url applies to the data in the "scope" field and all spans and span
  // events in the "spans" field.
  string schema_url = 3;
}

// A Span represents a single operation performed by a single component of the system.
//
// The next available field id is 17.
message Span {
  // A unique identifier for a trace. All spans from the same trace share
  // the same `trace_id`. The ID is a 16-byte array. An ID with all zeroes OR
  // of length other than 16 bytes is considered invalid (empty string in OTLP/JSON
  // is zero-length and thus is also invalid).
  //
  // This field is required.
  bytes trace_id = 1;

  // A unique identifier for a span within a trace, assigned when the span
  // is created. The ID is an 8-byte array. An ID with all zeroes OR of length
  // other than 8 bytes is considered invalid (empty string in OTLP/JSON
  // is zero-length and thus is also invalid).
  //
  // This field is required.
  bytes span_id = 2;

  // trace_state conveys information about request position in multiple distributed tracing graphs.
  // It is a trace_state in w3c-trace-context format: https://www.w3.org/TR/trace-context/#tracestate-header
  // See also https://github.com/w3c/distributed-tracing for more details about this field.
  string trace_state = 3;

  // The `span_id` of this span's parent span. If this is a root span, then this
  // field must be empty. The ID is an 8-byte array.
  bytes parent_span_id = 4;

  // Flags, a bit field.
  //
  // Bits 0-7 (8 least significant bits) are the trace flags as defined in W3C Trace
  // Context specification. To read the 8-bit W3C trace flag, use
  // `flags & SPAN_FLAGS_TRACE_FLAGS_MASK`.
  //
  // See https://www.w3.org/TR/trace-context-2/#trace-flags for the flag definitions.
  //
  // Bits 8 and 9 represent the 3 states of whether a span's parent
  // is remote. The states are (unknown, is not remote, is remote).
  // To read whether the value is known, use `(flags & SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK) != 0`.
  // To read whether the span is remote, use `(flags & SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK) != 0`.
  //
  // When creating span messages, if the message is logically forwarded from another source
  // with an equivalent flags fields (i.e., usually another OTLP span message), the field SHOULD
  // be copied as-is. If creating from a source that does not have an equivalent flags field
  // (such as a runtime representation of an OpenTelemetry span), the high 22 bits MUST
  // be set to zero.
  // Readers MUST NOT assume that bits 10-31 (22 most significant bits) will be zero.
  //
  // [Optional].
  fixed32 flags = 16;

  // A description of the span's operation.
  //
  // For example, the name can be a qualified method name or a file name
  // and a line number where the operation is called. A best practice is to use
  // the same display name at the same call point in an application.
  // This makes it easier to correlate spans in different traces.
  //
  // This field is semantically required to be set to non-empty string.
  // Empty value is equivalent to an unknown span name.
  //
  // This field is required.
  string name = 5;

  // SpanKind is the type of span. Can be used to specify additional relationships between spans
  // in addition to a parent/child relationship.
  enum SpanKind {
    // Unspecified. Do NOT use as default.
    // Implementations MAY assume SpanKind to be INTERNAL when receiving UNSPECIFIED.
    SPAN_KIND_UNSPECIFIED = 0;

    // Indicates that the span represents an internal operation within an application,
    // as opposed to an operation happening at the boundaries. Default value.
    SPAN_KIND_INTERNAL = 1;

    // Indicates that the span covers server-side handling of an RPC or other
    // remote network request.
    SPAN_KIND_SERVER = 2;

    // Indicates that the span describes a request to some remote service.
    SPAN_KIND_CLIENT = 3;

    // Indicates that the span describes a producer sending a message to a broker.
    // Unlike CLIENT and SERVER, there is often no direct critical path latency relationship
    // between producer and consumer spans. A PRODUCER span ends when the message was accepted
    // by the broker while the logical processing of the message might span a much longer time.
    SPAN_KIND_PRODUCER = 4;

    // Indicates that the span describes consumer receiving a message from a broker.
    // Like the PRODUCER kind, there is often no direct critical path latency relationship
    // between producer and consumer spans.
    SPAN_KIND_CONSUMER = 5;
  }

  // Distinguishes between spans generated in a particular context. For example,
  // two spans with the same name may be distinguished using `CLIENT` (caller)
  // and `SERVER` (callee) to identify queueing latency associated with the span.
  SpanKind kind = 6;

  // The start time of the span. On the client side, this is the time
  // kept by the local machine where the span execution starts. On the server side, this
  // is the time when the server's application handler starts running.
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
  //
  // This field is semantically required and it is expected that end_time >= start_time.
  fixed64 start_time_unix_nano = 7;

  // The end time of the span. On the client side, this is the time
  // kept by the local machine where the span execution ends. On the server side, this
  // is the time when the server application handler stops running.
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
  //
  // This field is semantically required and it is expected that end_time >= start_time.
  fixed64 end_time_unix_nano = 8;

  // A collection of key/value pairs. Note, global attributes
  // like server name can be set using the resource API. Examples of attributes:
  //
  //     "/http/user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
  //     "/http/server_latency": 300
  //     "example.com/myattribute": true
  //     "example.com/score": 10.239
  //
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  // The behavior of software that receives duplicated keys can be unpredictable.
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 9;

  // The number of attributes that were discarded. Attributes
  // can be discarded because their keys are too long or because there are too many
  // attributes. If this value is 0, then no attributes were dropped.
  uint32 dropped_attributes_count = 10;

  // Event is a time-stamped annotation of the span, consisting of user-supplied
  // text description and key-value pairs.
  message Event {
    // The time the event occurred.
    fixed64 time_unix_nano = 1;

    // The name of the event.
    // This field is semantically required to be set to non-empty string.
    string name = 2;

    // A collection of attribute key/value pairs on the event.
    // Attribute keys MUST be unique (it is not allowed to have more than one
    // attribute with the same key).
    // The behavior of software that receives duplicated keys can be unpredictable.
    repeated opentelemetry.proto.common.v1.KeyValue attributes = 3;

    // The number of dropped attributes. If the value is 0,
    // then no attributes were dropped.
    uint32 dropped_attributes_count = 4;
  }

  // A collection of Event items.
  repeated Event events = 11;

  // The number of dropped events. If the value is 0, then no
  // events were dropped.
  uint32 dropped_events_count = 12;

  // A pointer from the current span to another span in the same trace or in a
  // different trace. For example, this can be used in batching operations,
  // where a single batch handler processes multiple requests from different
  // traces or when the handler receives a request from a different project.
  message Link {
    // A unique identifier of a trace that this linked span is part of. The ID is a
    // 16-byte array.
    bytes trace_id = 1;

    // A unique identifier for the linked span. The ID is an 8-byte array.
    bytes span_id = 2;

    // The trace_state associated with the link.
    string trace_state = 3;

    // A collection of attribute key/value pairs on the link.
    // Attribute keys MUST be unique (it is not allowed to have more than one
    // attribute with the same key).
    // The behavior of software that receives duplicated keys can be unpredictable.
    repeated opentelemetry.proto.common.v1.KeyValue attributes = 4;

    // The number of dropped attributes. If the value is 0,
    // then no attributes were dropped.
    uint32 dropped_attributes_count = 5;

    // Flags, a bit field.
    //
    // Bits 0-7 (8 least significant bits) are the trace flags as defined in W3C Trace
    // Context specification. To read the 8-bit W3C trace flag, use
    // `flags & SPAN_FLAGS_TRACE_FLAGS_MASK`.
    //
    // See https://www.w3.org/TR/trace-context-2/#trace-flags for the flag definitions.
    //
    // Bits 8 and 9 represent the 3 states of whether the link is remote.
    // The states are (unknown, is not remote, is remote).
    // To read whether the value is known, use `(flags & SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK) != 0`.
    // To read whether the link is remote, use `(flags & SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK) != 0`.
    //
    // Readers MUST NOT assume that bits 10-31 (22 most significant bits) will be zero.
    // When creating new spans, bits 10-31 (most-significant 22-bits) MUST be zero.
    //
    // [Optional].
    fixed32 flags = 6;
  }

  // A collection of Links, which are references from this span to a span
  // in the same or different trace.
  repeated Link links = 13;

  // The number of dropped links after the maximum size was
  // enforced. If this value is 0, then no links were dropped.
  uint32 dropped_links_count = 14;

  // An optional final status for this span. Semantically when Status isn't set, it means
  // span's status code is unset, i.e. assume STATUS_CODE_UNSET (code = 0).
  Status status = 15;
}

// The Status type defines a logical error model that is suitable for different
// programming environments, including REST APIs and RPC APIs.
message Status {
  reserved 1;

  // A developer-facing human readable error message.
  string message = 2;

  // For the semantics of status codes see
  // https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/api.md#set-status
  enum StatusCode {
    // The default status.
    STATUS_CODE_UNSET               = 0;
    // The Span has been validated by an Application developer or Operator to 
    // have completed successfully.
    STATUS_CODE_OK                  = 1;
    // The Span contains an error.
    STATUS_CODE_ERROR               = 2;
  };

  // The status code.
  StatusCode code = 3;
}

// SpanFlags represents constants used to interpret the
// Span.flags field, which is protobuf 'fixed32' type and is to
// be used as bit-fields. Each non-zero value defined in this enum is
// a bit-mask.  To extract the bit-field, for example, use an
// expression like:
//
//   (span.flags & SPAN_FLAGS_TRACE_FLAGS_MASK)
//
// See https://www.w3.org/TR/trace-context-2/#trace-flags for the flag definitions.
//
// Note that Span flags were introduced in version 1.1 of the
// OpenTelemetry protocol.  Older Span producers do not set this
// field, consequently consumers should not rely on the absence of a
// particular flag bit to indicate the presence of a particular feature.
enum SpanFlags {
  // The zero value for the enum. Should not be used for comparisons.
  // Instead use bitwise "and" with the appropriate mask as shown above.
  SPAN_FLAGS_DO_NOT_USE = 0;

  // Bits 0-7 are used for trace flags.
  SPAN_FLAGS_TRACE_FLAGS_MASK = 0x000000FF;

  // Bits 8 and 9 are used to indicate that the parent span or link span is remote.
  // Bit 8 (`HAS_IS_REMOTE`) indicates whether the value is known.
  // Bit 9 (`IS_REMOTE`) indicates whether the span or link is remote.
  SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK = 0x00000100;
  SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK = 0x00000200;

  // Bits 10-31 are reserved for future use.
}
```

