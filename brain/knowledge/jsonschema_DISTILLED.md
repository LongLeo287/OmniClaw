---
id: jsonschema
type: knowledge
owner: OA_Triage
---
# jsonschema
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# jsonschema

[<img alt="crates.io" src="https://img.shields.io/crates/v/jsonschema.svg?style=flat-square&color=fc8d62&logo=rust" height="20">](https://crates.io/crates/jsonschema)
[<img alt="docs.rs" src="https://img.shields.io/badge/docs.rs-jsonschema-66c2a5?style=flat-square&labelColor=555555&logo=docs.rs" height="20">](https://docs.rs/jsonschema)
[<img alt="build status" src="https://img.shields.io/github/actions/workflow/status/Stranger6667/jsonschema/ci.yml?branch=master&style=flat-square" height="20">](https://github.com/Stranger6667/jsonschema/actions?query=branch%3Amaster)
[<img alt="codecov.io" src="https://img.shields.io/codecov/c/gh/Stranger6667/jsonschema?logo=codecov&style=flat-square&token=B1EnafGlRL" height="20">](https://app.codecov.io/github/Stranger6667/jsonschema)
[<img alt="Supported Dialects" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fbowtie.report%2Fbadges%2Frust-jsonschema%2Fsupported_versions.json&style=flat-square">](https://bowtie.report/#/implementations/rust-jsonschema)

A high-performance JSON Schema validator for Rust.

```rust
use serde_json::json;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let schema = json!({"maxLength": 5});
    let instance = json!("foo");

    // One-off validation
    assert!(jsonschema::is_valid(&schema, &instance));
    assert!(jsonschema::validate(&schema, &instance).is_ok());

    // Build & reuse (faster)
    let validator = jsonschema::validator_for(&schema)?;

    // Fail on first error
    assert!(validator.validate(&instance).is_ok());

    // Iterate over errors
    for error in validator.iter_errors(&instance) {
        eprintln!("Error: {error}");
        eprintln!("Location: {}", error.instance_path());
    }

    // Boolean result
    assert!(validator.is_valid(&instance));

    // Structured output (JSON Schema Output v1)
    let evaluation = validator.evaluate(&instance);
    for annotation in evaluation.iter_annotations() {
        eprintln!(
            "Annotation at {}: {:?}",
            annotation.schema_location,
            annotation.annotations.value()
        );
    }

    Ok(())
}
```

You also can use it from the command line via the [jsonschema-cli](https://github.com/Stranger6667/jsonschema/tree/master/crates/jsonschema-cli) crate.

```console
$ jsonschema-cli schema.json -i instance.json
```

See more usage examples in the [documentation](https://docs.rs/jsonschema).

> ⚠️ **Upgrading from older versions?** Check our [Migration Guide](https://github.com/Stranger6667/jsonschema/blob/master/MIGRATION.md) for key changes.

## Highlights

- 📚 Full support for popular JSON Schema drafts
- 🔧 Custom keywords and format validators
- 🌐 Blocking & non-blocking remote reference fetching (network/file)
- 🎨 Structured Output v1 reports (flag/list/hierarchical)
- ✨ Meta-schema validation for schema documents, including custom metaschemas
- 🔗 Bindings for [Python](https://github.com/Stranger6667/jsonschema/tree/master/crates/jsonschema-py) and [Ruby](https://github.com/Stranger6667/jsonschema/tree/master/crates/jsonschema-rb)
- 🚀 WebAssembly support
- 💻 Command Line Interface

### Supported drafts

The following drafts are supported:

- [![Draft 2020-12](https://img.shields.io/endpoint?url=https%3A%2F%2Fbowtie.report%2Fbadges%2Frust-jsonschema%2Fcompliance%2Fdraft2020-12.json)](https://bowtie.report/#/implementations/rust-jsonschema)
- [![Draft 2019-09](https://img.shields.io/endpoint?url=https%3A%2F%2Fbowtie.report%2Fbadges%2Frust-jsonschema%2Fcompliance%2Fdraft2019-09.json)](https://bowtie.report/#/implementations/rust-jsonschema)
- [![Draft 7](https://img.shields.io/endpoint?url=https%3A%2F%2Fbowtie.report%2Fbadges%2Frust-jsonschema%2Fcompliance%2Fdraft7.json)](https://bowtie.report/#/implementations/rust-jsonschema)
- [![Draft 6](https://img.shields.io/endpoint?url=https%3A%2F%2Fbowtie.report%2Fbadges%2Frust-jsonschema%2Fcompliance%2Fdraft6.json)](https://bowtie.report/#/implementations/rust-jsonschema)
- [![Draft 4](https://img.shields.io/endpoint?url=https%3A%2F%2Fbowtie.report%2Fbadges%2Frust-jsonschema%2Fcompliance%2Fdraft4.json)](https://bowtie.report/#/implementations/rust-jsonschema)

You can check the current status on the [Bowtie Report](https://bowtie.report/#/implementations/rust-jsonschema).

## Notable Users

- Tauri: [Config validation](https://github.com/tauri-apps/tauri/blob/c901d9fdf932bf7c3c77e9d3097fabb1fe0712af/crates/tauri-cli/src/helpers/config.rs#L173)
- Apollo Router: [Config file validation](https://github.com/apollographql/router/blob/855cf6cc0757ca6176970ddf3ae8c98c87c632d1/apollo-router/src/configuration/schema.rs#L120)
- qsv: [CSV record validation with custom keyword & format validator](https://github.com/jqnatividad/qsv/blob/6b6985065a1270f767d881b13aa2a27fae1958fb/src/cmd/validate.rs#L630)

## Performance

`jsonschema` outperforms other Rust JSON Schema validators in most scenarios:

- Up to **75-645x** faster than `valico` and `jsonschema_valid` for complex schemas
- Generally **2-52x** faster than `boon`, and **>5000x** faster for recursive schemas

For detailed benchmarks, see our [full performance comparison](https://github.com/Stranger6667/jsonschema/tree/master/crates/benchmark-suite).

## Minimum Supported Rust Version (MSRV)

This crate requires Rust 1.83.0 or later.

## TLS Configuration

By default, `jsonschema` uses `aws-lc-rs` as the TLS cryptography provider, which is the default one in `reqwest`.

### Using Ring Instead

You can opt into using `ring` as the TLS provider:

```toml
[dependencies]
jsonschema = {
    version = "0.42",
    default-features = false,
    features = ["resolve-http", "resolve-file", "tls-ring"]
}
```

**NOTE:** If both `tls-aws-lc-rs` and `tls-ring` features are enabled, `aws-lc-rs` takes precedence.

## Acknowledgements

This library draws API design inspiration from the Python [`jsonschema`](https://github.com/python-jsonschema/jsonschema) package. We're grateful to the Python `jsonschema` maintainers and contributors for their pioneering work in JSON Schema validation.

## Support

If you have questions, need help, or want to suggest improvements, please use [GitHub Discussions](https://github.com/Stranger6667/jsonschema/discussions).

## Sponsorship

If you find `jsonschema` useful, please consider [sponsoring its development](https://github.com/sponsors/Stranger6667).

## Contributing

We welcome contributions! Here's how you can help:

- Share your use cases
- Implement missing keywords
- Fix failing test cases from the [JSON Schema test suite](https://bowtie.report/#/implementations/rust-jsonschema)

See [CONTRIBUTING.md](https://github.com/Stranger6667/jsonschema/blob/master/CONTRIBUTING.md) for more details.

## License

Licensed under [MIT License](https://github.com/Stranger6667/jsonschema/blob/master/LICENSE).

```

### File: CHANGELOG.md
```md
# Changelog

## [Unreleased]

### Fixed

- Incorrect handling of `duration` format when hours and seconds appear without minutes, or years and days without months.

## [0.45.0] - 2026-03-08

### Added

- `bundle(schema)` / `async_bundle(schema)` / `ValidationOptions::bundle`: produce a Compound Schema Document with external `$ref` targets embedded in a draft-appropriate container (`definitions` for Draft 4/6/7, `$defs` for Draft 2019-09/2020-12) while preserving `$ref` values. [#791](https://github.com/Stranger6667/jsonschema/issues/791).
- **CLI**: `jsonschema validate` and `jsonschema bundle` subcommands. Flat invocation (`jsonschema schema.json -i …`) is deprecated — use `jsonschema validate` instead. [#791](https://github.com/Stranger6667/jsonschema/issues/791).
- `ValidationError::absolute_keyword_location()` to get the absolute keyword location URI of the schema node that produced the error. [#737](https://github.com/Stranger6667/jsonschema/issues/737).

### Changed

- `ValidationError::into_parts()` now returns `ValidationErrorParts` instead of a tuple.

## [0.44.1] - 2026-03-03

### Fixed

- `hostname` format now applies legacy RFC 1034 semantics in Draft 4/6 and keeps IDNA A-label validation in Draft 7+.

## [0.44.0] - 2026-03-02

### Added

- `canonical::json::to_string(value)` for canonical JSON serialization (stable key ordering and numeric normalization), useful for deduplicating equivalent JSON Schemas.

### Fixed

- Do not produce annotations for non-string instances from `contentMediaType`, `contentEncoding`, and `contentSchema` keywords.

## [0.43.0] - 2026-02-28

### Performance

- Optimize `pattern` and `patternProperties` for `^(a|b|c)$` alternations via linear array scan.
- Optimize `^\S*$` patterns by replacing regex with a direct ECMA-262 whitespace check.

### Fixed

- `anyOf`, `format`, `unevaluatedProperties`, and `unevaluatedItems` now correctly collect annotations per spec.

## [0.42.2] - 2026-02-26

### Fixed

- SWAR digit parser accepted bytes `:`–`?` (0x3A–0x3F) as valid digits during `date`, `time`, and `date-time` format validation, potentially allowing malformed values to pass.

### Performance

- Extend `pattern` prefix optimization to handle escaped slashes (`^\/`) and exact-match patterns (`^\$ref$`).
- Specialize `enum` for cases when all variants are strings.

## [0.42.1] - 2026-02-17

### Performance

- Reduce dynamic dispatch overhead for non-recursive `$ref` resolution.
- Cache ECMA regex transformations during `format: "regex"` validation.

## [0.42.0] - 2026-02-14

### Added

- `JsonType::as_str` method for zero-allocation type name access.
- `ValidationErrorKind::keyword` is now public.
- `tls-ring` feature flag to opt into using `ring` as the TLS crypto provider instead of the default `aws-lc-rs`. [#997](https://github.com/Stranger6667/jsonschema/pull/997)
- **CLI**: Support YAML (`.yaml`/`.yml`) instance files in text output mode. [#988](https://github.com/Stranger6667/jsonschema/pull/988)

### Changed

- **BREAKING**: Default TLS crypto provider switched back to `aws-lc-rs`. Users who need `ring` can opt in via the `tls-ring` feature flag. This resolves potential conflicts with other libraries using `aws-lc-rs`. [#997](https://github.com/Stranger6667/jsonschema/pull/997)

### Fixed

- Panic when validating `$ref` targets that resolve to boolean schemas.

### Performance

- Cache formatted schema locations with `OnceLock` to avoid repeated formatting during `evaluate()`.

## [0.41.0] - 2026-02-04

### Performance

- Replace regex-based `uri-template` format validation with a hand-rolled RFC 6570 parser.
- Specialize `items` keyword for simple type schemas (`{"type": "string"}`, `{"type": "number"}`, etc.) to eliminate dynamic dispatch overhead.
- Precompute regex matches on known properties.
- Faster `unevaluatedProperties` validation via O(1) property lookup and short-circuit `oneOf` evaluation.
- Use HashMap for large set of properties.
- Lower HashMap threshold from 40 to 15 properties for faster property lookups.

## [0.40.2] - 2026-01-30

### Changed

- Exclude internal `tracker` field from `ValidationError` Debug output.
- Switch HTTP client TLS crypto backend from `aws-lc-rs` to `ring` to simplify building from source on some Linux distributions. [#957](https://github.com/Stranger6667/jsonschema/issues/957)

### Fixed

- `type: integer` validation in Draft 4 now correctly accepts large integers outside the i64/u64 range when `arbitrary-precision` feature is enabled.

## [0.40.1] - 2026-01-30

### Changed

- `ValidationErrorKind::Custom` now includes a `keyword` field containing the custom keyword name.

### Performance

- Faster validation via cost-based keyword ordering.
- Faster `patternProperties` for simple prefix patterns (e.g., `^x-`).

## [0.40.0] - 2026-01-18

### Added

- `HttpOptions` and `ValidationOptions::with_http_options()` for configuring HTTP client behavior (timeouts, TLS verification, custom CA certificates) when fetching external schemas.
- **CLI**: `--timeout`, `--connect-timeout`, `--insecure`, and `--cacert` flags for HTTP configuration.

## [0.39.0] - 2026-01-16

### Added

- `ValidationError::evaluation_path()` for the dynamic path including `$ref` traversals.

### Changed

- **BREAKING**: Simplified custom keyword API - `Keyword::validate` no longer receives path parameters, and `ValidationError::custom` only takes a message.

### Fixed

- `schemaLocation` in evaluation output now excludes `$ref`/`$dynamicRef`/`$recursiveRef` per JSON Schema spec.

### Performance

- `evaluate()`: 4.5-30x faster on complex schemas, 12-89% faster overall.
- Recursive schemas with `oneOf`/`anyOf`: ~4000x faster via memoization. [#930](https://github.com/Stranger6667/jsonschema/issues/930)

## [0.38.1] - 2025-12-25

### Fixed

- `multipleOf` validation for integer values between `2^53` and `i64::MAX` with `arbitrary-precision` feature.

## [0.38.0] - 2025-12-24

### Added

- `EmailOptions` for configuring `email` format validation. [#903](https://github.com/Stranger6667/jsonschema/pull/903)

### Fixed

- Use-after-free in async `$ref` resolution when multiple refs target the same external URL with different fragments. [#906](https://github.com/Stranger6667/jsonschema/issues/906)
- `multipleOf` validation for large u64 values beyond `i64::MAX` with `arbitrary-precision` feature.
- `Validator` not being `Send + Sync` on WASM targets. [#915](https://github.com/Stranger6667/jsonschema/issues/915)

## [0.37.4] - 2025-11-30

### Fixed

- Stack overflow during validation of schemas with circular `$ref` chains (e.g., `a` -> `b` -> `a`).
- Local `$ref` resolution within fragment-extracted external resources. [#892](https://github.com/Stranger6667/jsonschema/issues/892)

### Removed

- Deprecated `PrimitiveType` & `PrimitiveTypesBitMap`.

## [0.37.3] - 2025-11-28

### Fixed

- External resources not discovered within subresources of local `$ref` targets. [#892](https://github.com/Stranger6667/jsonschema/issues/892)

## [0.37.2] - 2025-11-27

### Added

- `JsonTypeSet::len()` and `JsonTypeSet::remove()` helpers for managing type sets.

### Fixed

- External resources not discovered through chained local `$ref` references. [#892](https://github.com/Stranger6667/jsonschema/issues/892)

## [0.37.1] - 2025-11-19

### Fixed

- Stack overflow on empty `$ref` value. [#886](https://github.com/Stranger6667/jsonschema/issues/886)

## [0.37.0] - 2025-11-19

### Added

- `evaluate()` top-level function for convenient access to structured validation output.
- **CLI**: Schema-only validation now also validates all referenced schemas. [#804](https://github.com/Stranger6667/jsonschema/issues/804)
- Support for additional `contentEncoding` values per RFC 4648: `base64url`, `base32`, `base32hex`, and `base16`. These encodings are now validated alongside the existing `base64` support in Draft 6 and 7. [#26](https://github.com/Stranger6667/jsonschema/issues/26)
- `validator.iter_errors(instance).into_errors()`. It returns a `ValidationErrors` type that collects validation errors and implements `std::error::Error`. [#451](https://github.com/Stranger6667/jsonschema/issues/451)

### Changed

- **BREAKING**: `ValidationError` fields are private; use `instance()`, `kind()`, `instance_path()`, and `schema_path()` instead of accessing struct fields directly.
- **BREAKING**: `ErrorIterator` is now a newtype wrapper instead of `Box<dyn ValidationErrorIterator>`.

### Performance

- `validate` and other APIs returning `Result<_, ValidationError>` are 5–10% faster in some workloads due to the smaller error handle.
- `evaluate`: Avoiding deep clones of unmatched keyword values (e.g., `title`, `description`, `examples`) on every schema node evaluation by using `Arc` internally. Can be multiple times faster for schemas with large annotations.

## [0.36.0] - 2025-11-18

### Added

- **CLI**: Structured `--output flag|list|hierarchical` modes now stream newline-delimited JSON records with schema/instance metadata plus JSON Schema Output v1 payloads (default `text` output remains human-readable).
- **CLI**: `--errors-only` flag to suppress successful validation output and only show failures.
- **CLI**: When invoked with only a schema file (no instances), validates the schema against its meta-schema. [#804](https://github.com/Stranger6667/jsonschema/issues/804)
- New `Validator::evaluate()` API exposes JSON Schema Output v1 (flag/list/hierarchical) reports along with iterator helpers for annotations and errors.
- `meta::validator_for()` function to build validators for meta-schema validation with full `Validator` API access.
- `Validator` now implements `Clone`. [#809](https://github.com/Stranger6667/jsonschema/issues/809)

### Removed

- `Validator::apply()`, `Output`, and `BasicOutput` types have been removed in favor of the richer `evaluate()` API.

## [0.35.0] - 2025-11-16

### Added

- Support for custom meta-schemas. Schemas with custom `$schema` URIs can now be used by registering their meta-schemas in the `Registry` via `jsonschema::options().with_registry()`. [#664](https://github.com/Stranger6667/jsonschema/issues/664)
- `arbitrary-precision` feature for exact numeric validation of large integers and decimals beyond standard floating-point limits. [#103](https://github.com/Stranger6667/jsonschema/issues/103)
- Support for HTTPS `$schema` URIs for drafts 04, 06, and 07 (e.g., `https://json-schema.org/draft-07/schema`). [#802](https://github.com/Stranger6667/jsonschema/issues/802)

### Changed

- **BREAKING**: `meta::is_valid` now panics for unknown `$schema` values instead of defaulting to Draft 2020-12. `meta::validate` returns an error for unknown `$schema` values. Use `meta::options().with_registry()` to validate schemas against custom meta-schemas.
- **BREAKING**: `Resource::from_contents` no longer returns `Result` and always succeeds, since draft detection no longer fails for unknown `$schema` values.

### Removed

- **BREAKING**: `meta::try_is_valid` and `meta::try_validate`. Use `meta::is_valid` and `meta::validate` instead.
- **BREAKING**: `primitive_type` module (deprecated since 0.30.0). Use `jsonschema::types` instead.

### Performance

- `required`: short-circuit when the instance object has fewer properties than required keys.

## [0.34.0] - 2025-11-14

### Changed

- **BREAKING**: `BasicOutput` and `Annotations` no longer have lifetime parameters. Update type annotations from `BasicOutput<'a>` to `BasicOutput` and `Annotations<'a>` to `Annotations`.
- `referencing`: URI caching now avoids hash collisions and reduces lock contention.
- Update `fluent-uri` to `0.4.1`.
- Bump MSRV to `1.83.0`.
- Drop the `Send + Sync` bounds from `Retrieve`/`AsyncRetrieve` on `wasm32`.
- Use the new `draftX::meta::validator()` helper so meta-schema validators lazy-init on `wasm32` while native targets keep borrowing the cached `jsonschema::meta::MetaValidator`.

### Fixed

- Hostname and IDN hostname formats now decode `xn--` labels, reject leading combining marks/uppercase prefixes, and enforce the latest JSON Schema punycode context rules.
- Restore `wasm32-unknown-unknown` support. [#785](https://github.com/Stranger6667/jsonschema/issues/785)

### Performance

- `apply` now reuses cached schema locations, URI fragments, and buffers for up to ~2.5x faster validation.
- Recursive and regular `$ref` compilation deduplicates validator nodes, which decreases the memory usage and improves performance.
- Validator compilation restores the regex cache for faster builds on regex-heavy schemas and precomputes absolute schema locations, trading a bit of compile time for faster `apply` on location-heavy workloads.
- Large schema compilation is significantly faster. [#755](https://github.com/Stranger6667/jsonschema/issues/755)
- `unevaluatedProperties` validation is 25-35% faster through optimized property marking and early-exit paths.
- `unevaluatedProperties` memory usage drastically reduced by eliminating redundant registry clones during compilation.
- `unevaluatedItems` validation is ~10% faster through early-exit optimizations and eliminating redundant validations in combinators.

### Removed

- **BREAKING**: `Validator::config` to reduce the memory footprint.
- **BREAKING**: Public `DRAFT4_META_VALIDATOR`, `DRAFT6_META_VALIDATOR`, `DRAFT7_META_VALIDATOR`, `DRAFT201909_META_VALIDATOR`, and `DRAFT202012_META_VALIDATOR` statics. Use `draftX::meta::validator()` helper functions instead (e.g., `draft7::meta::validator()`).

## [0.33.0] - 2025-08-24

### Fixed

- **BREAKING**: `instance_path` segments are now unescaped when iterating. `LocationSegment::Property` now holds `Cow<'_, str>` and `LocationSegment` is no longer `Copy`. [#788](https://github.com/Stranger6667/jsonschema/issues/788)

## [0.32.1] - 2025-08-03

### Changed

- Bump `fancy-regex` to `0.16`.

## [0.32.0] - 2025-07-29

### Added

- Added missing `context` field to `ValidationErrorKind::OneOfMultipleValid`.

### Changed

- Improved error message for `enum`.

## [0.31.0] - 2025-07-28

### Added

- **CLI**: flag `-d, --draft <4|6|7|2019|2020>` to enforce a specific JSON Schema draft.
- **CLI**: flags `--assert-format` and `--no-assert-format` to toggle validation of `format` keywords.
- Added `context` for `ValidationErrorKind::AnyOf` and `ValidationErrorKind::OneOfNotValid` which contains errors for all subschemas, each inside a separate vector with an index matching subschema ID.

### Fixed

- Improve the precision of `multipleOf` for float values.

### Changed

- Bump `fancy-regex` to `0.15`.

## [0.30.0] - 2025-04-16

### Added

- `JsonType` and `JsonTypeSet`.
- `ValidationOptions::with_base_uri` that allows for specifying a base URI for all relative references in the schema.
- Configuration options for the underlying regex engine used by `pattern` and `patternProperties` keywords.

### Changed

- Better error messages for relative `$ref` without base URI.

### Fixed

- **CLI**: Inability to load relative file `$ref`. [#725](https://gith
... [TRUNCATED]
```

### File: codecov.yaml
```yaml
github_checks:
  annotations: false

coverage:
  status:
    project: off
    patch: off

# Ignore test/benchmark infrastructure & dev-only suite helpers from coverage
ignore:
  - "crates/benchmark/"
  - "crates/benchmark-suite/"
  - "crates/jsonschema-testsuite/"
  - "crates/jsonschema-testsuite-codegen/"
  - "crates/jsonschema-testsuite-internal/"
  - "crates/jsonschema-referencing-testsuite/"
  - "crates/jsonschema-referencing-testsuite-codegen/"
  - "crates/jsonschema-referencing-testsuite-internal/"
  - "crates/testsuite-common/"

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at dmitry@dygalo.dev. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq

```

### File: CONTRIBUTING.md
```md
# Contributing to jsonschema

Thank you for your interest in contributing to jsonschema! We welcome contributions from everyone in the form of suggestions, bug reports, pull requests, and feedback. This document provides guidance if you're thinking of helping out.

## Submitting Bug Reports and Feature Requests

When reporting a bug or asking for help, please include enough details so that others can reproduce the behavior you're seeing.

To open an issue, [follow this link](https://github.com/Stranger6667/jsonschema-rs/issues/new) and fill out the appropriate template.

When making a feature request, please make it clear what problem you intend to solve with the feature and provide some ideas on how to implement it.

**NOTE**: Many commands are available via a [Justfile](https://github.com/casey/just) located in the root of the repository.

## Running the Tests

The tests in jsonschema depend on the [JSON Schema Test Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite). Before running the tests, you need to download the suite.

Initialize and update the git submodules:

   ```console
   $ git submodule init
   $ git submodule update
   ```

This will clone the JSON Schema Test Suite to `crates/jsonschema/tests/suite/`.

Then follow instructions below to run the tests either for the Rust Core or Python Bindings.

## Rust Core

### Rust Toolchain

jsonschema targets Rust 1.83.0 as its Minimum Supported Rust Version (MSRV). Please ensure your contributions are compatible with this version.

You can use [rustup](https://rustup.rs/) to manage your installed toolchains. To set up the correct version for the jsonschema project:

   ```console
   $ rustup override set 1.83.0
   ```

### Running the Tests

Run the tests with:

   ```console
   $ cargo test --all-features
   ```

Make sure all tests pass before submitting your pull request. If you've added new functionality, please include appropriate tests.

### Formatting and Linting

Format your code using:

   ```console
   $ cargo fmt --all
   ```

And lint it using:

   ```console
   $ cargo clippy --all-targets --all-features -- -D warnings
   ```

## Python Bindings

The Python bindings are located in the `crates/jsonschema-py` directory. If you're working on or testing the Python bindings, follow these steps:

### Setting Up the Python Environment

We recommend using [uv](https://github.com/astral-sh/uv) for managing the Python environment. To set up the environment:

1. Navigate to the `crates/jsonschema-py` directory:

   ```console
   $ cd crates/jsonschema-py
   ```

2. Create a virtual environment and install the package in editable mode with test dependencies:

   ```console
   $ uv venv
   $ uv pip install -e ".[tests]"
   ```

### Running Python Tests

To run the Python tests:

   ```console
   $ uv run pytest tests-py
   ```

Make sure all Python tests pass before submitting your pull request. If you've added new functionality to the Python bindings, please include appropriate Python tests as well.

### Formatting and Linting

Format your code using:

   ```console
   $ uvx ruff format benches python tests-py
   $ cargo fmt --all
   ```

And lint it using:

   ```console
   $ uvx ruff check benches python tests-py
   $ cargo clippy --all-targets --all-features -- -D warnings
   ```

### Adding New Functionality

For small changes (e.g., bug fixes), feel free to submit a PR directly.

For larger changes (e.g., new functionality or configuration options), please create an [issue](https://github.com/Stranger6667/jsonschema-rs/issues) first to discuss your proposed change.

### Improving Documentation

Contributions to documentation are always welcome. If you find any part of the documentation unclear or incomplete, please open an issue or submit a pull request.

### Implementing Missing Keywords

If you're looking to contribute code, implementing missing keywords for newer JSON Schema drafts is a great place to start. Check the [compliance badges](https://github.com/Stranger6667/jsonschema-rs#supported-drafts) to see which drafts might need work.

### Fixing Test Cases

Another way to contribute is by fixing failing test cases from the [JSON Schema Test Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite). You can check the current status on the [Bowtie Report](https://bowtie.report/#/implementations/rust-jsonschema).

## Pull Requests

1. Ensure your code passes all tests and lint checks.
2. Update the documentation as necessary.
3. Add or update tests as appropriate.
4. If you're adding new functionality, please include a description in the README.
5. If your change affects users, add an entry to the CHANGELOG.

## Getting Help

If you need help with contributing to jsonschema, you can:

1. Open a [GitHub Discussion](https://github.com/Stranger6667/jsonschema-rs/discussions).
2. Ask in the pull request or issue if you've already opened one.

Thank you for contributing to jsonschema!

```

### File: MIGRATION.md
```md
# Migration Guide

## Upgrading from 0.38.x to 0.39.0

### Custom keyword API simplified

The `Keyword::validate` signature has been simplified. Path information (`instance_path` and `schema_path`)
is now filled in automatically, so you only need to provide the error message.

**`Keyword::validate` signature:**

```rust
// Old (0.38.x)
fn validate<'i>(
    &self,
    instance: &'i Value,
    location: &LazyLocation,
) -> Result<(), ValidationError<'i>>;

// New (0.39.0)
fn validate<'i>(&self, instance: &'i Value) -> Result<(), ValidationError<'i>>;
```

**Creating errors:**

```rust
// Old (0.38.x)
ValidationError::custom(schema_path, instance_path, instance, message)

// New (0.39.0) - just the message, paths are filled in automatically
ValidationError::custom("expected a string")

// For factory errors (invalid schema values)
ValidationError::schema("expected true")
```

**Updated implementation example:**

```rust
use jsonschema::{Keyword, ValidationError};
use serde_json::Value;

struct MyValidator;

impl Keyword for MyValidator {
    fn validate<'i>(&self, instance: &'i Value) -> Result<(), ValidationError<'i>> {
        if !instance.is_string() {
            return Err(ValidationError::custom("expected a string"));
        }
        Ok(())
    }

    fn is_valid(&self, instance: &Value) -> bool {
        instance.is_string()
    }
}
```

## Upgrading from 0.37.x to 0.38.0

### WASM: `Validator` is now `Send + Sync`

The `Validator` type is now `Send + Sync` on WASM targets, restoring the expected behavior that was inadvertently broken in 0.34.0. This allows `Validator` to be used in static variables and shared across async contexts on WASM.

If you implemented custom `Keyword` or `Format` validators on WASM that rely on non-thread-safe types (like `Rc` or `RefCell`), you'll need to update them to use thread-safe alternatives (`Arc`, `Mutex`, etc.):

```rust
use std::sync::Arc;

// Old (0.37.x on WASM) - non-thread-safe types were allowed
use std::rc::Rc;
struct MyKeyword {
    data: Rc<SomeData>,
}

// New (0.38.x) - must be Send + Sync on all platforms
struct MyKeyword {
    data: Arc<SomeData>,
}
```

Note: The `Retrieve` and `AsyncRetrieve` traits still have relaxed `Send + Sync` bounds on WASM, so retrievers can continue to use non-thread-safe types.

## Upgrading from 0.36.x to 0.37.0

### `ValidationError` is now opaque

All `ValidationError` fields are private. Replace `error.instance`, `error.instance_path`, `error.schema_path`, and `error.kind` with the corresponding accessor calls:

```rust
let instance = error.instance();
let kind = error.kind();
let instance_path = error.instance_path();
let schema_path = error.schema_path();
```

### `ErrorIterator` is now a struct

`ErrorIterator` used to be a `type` alias to `Box<dyn ValidationErrorIterator<'_>>` and is now a struct wrapping that iterator.

## Upgrading from 0.35.x to 0.36.0

### Removal of `Validator::apply`, `Output`, and `BasicOutput`

The legacy `apply()` API and its `BasicOutput`/`OutputUnit` structures have been removed in favor of
the richer [`Validator::evaluate`](https://docs.rs/jsonschema/latest/jsonschema/struct.Validator.html#method.evaluate)
interface that exposes the JSON Schema Output v1 formats (flag/list/hierarchical) directly.

```rust
use serde_json::json;

// Old (0.35.x)
let output = validator.apply(&instance).basic();
match output {
    BasicOutput::Valid(units) => println!("valid: {units:?}"),
    BasicOutput::Invalid(errors) => println!("errors: {errors:?}"),
}

// New (0.36.0)
let evaluation = validator.evaluate(&instance);
if evaluation.flag().valid {
    println!("valid");
}
let list = serde_json::to_value(evaluation.list())?;
let hierarchical = serde_json::to_value(evaluation.hierarchical())?;
```

Because `evaluate()` materializes every evaluation step so it can provide the structured outputs, it
always walks the full schema tree. If you only need a boolean result, continue to prefer
[`is_valid`](https://docs.rs/jsonschema/latest/jsonschema/fn.is_valid.html) or
[`validate`](https://docs.rs/jsonschema/latest/jsonschema/fn.validate.html).

The serialized JSON now matches the [JSON Schema Output v1 specification](https://github.com/json-schema-org/json-schema-spec/blob/main/specs/output/jsonschema-validation-output-machines.md)
and its companion [schema](https://github.com/json-schema-org/json-schema-spec/blob/main/specs/output/schema.json).
For example, evaluating an array against a schema with `prefixItems` and `items` produces list output like:

```json
{
  "valid": false,
  "details": [
    {"valid": false, "evaluationPath": "", "schemaLocation": "", "instanceLocation": ""},
    {
      "valid": false,
      "evaluationPath": "/items",
      "instanceLocation": "",
      "schemaLocation": "/items",
      "droppedAnnotations": true
    },
    {
      "valid": false,
      "evaluationPath": "/items",
      "instanceLocation": "/1",
      "schemaLocation": "/items"
    },
    {
      "valid": false,
      "evaluationPath": "/items/type",
      "instanceLocation": "/1",
      "schemaLocation": "/items/type",
      "errors": {"type": "\"oops\" is not of type \"integer\""}
    },
    {
      "valid": true,
      "evaluationPath": "/prefixItems",
      "instanceLocation": "",
      "schemaLocation": "/prefixItems",
      "annotations": 0
    },
    {
      "valid": true,
      "evaluationPath": "/prefixItems/0",
      "instanceLocation": "/0",
      "schemaLocation": "/prefixItems/0"
    },
    {
      "valid": true,
      "evaluationPath": "/prefixItems/0/type",
      "instanceLocation": "/0",
      "schemaLocation": "/prefixItems/0/type"
    },
    {
      "valid": true,
      "evaluationPath": "/type",
      "instanceLocation": "",
      "schemaLocation": "/type"
    }
  ]
}
```

If you need to inspect annotations or errors programmatically without serializing to JSON, use the
new [`evaluation.iter_annotations()`](https://docs.rs/jsonschema/latest/jsonschema/struct.Evaluation.html#method.iter_annotations)
and [`evaluation.iter_errors()`](https://docs.rs/jsonschema/latest/jsonschema/struct.Evaluation.html#method.iter_errors)
helpers.

## Upgrading from 0.34.x to 0.35.0

### Custom meta-schemas require explicit registration

Schemas with custom/unknown `$schema` URIs now require their meta-schema to be registered before building validators. Custom meta-schemas automatically inherit the draft-specific behavior of their underlying draft by walking the meta-schema chain. Validators always honor an explicitly configured draft (e.g., via `ValidationOptions::with_draft`), so overriding the draft is still the highest priority and bypasses auto-detection and the registry check intentionally.

```rust
// Old (0.34.x) - would fail with unclear error
let schema = json!({
    "$schema": "http://example.com/custom",
    "type": "object"
});
let validator = jsonschema::validator_for(&schema)?;

// New (0.35.x) - explicit registration required
use jsonschema::{Registry, Resource, Draft};

let meta_schema = json!({
    "$id": "http://example.com/custom",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$vocabulary": {
        "https://json-schema.org/draft/2020-12/vocab/core": true,
        "https://json-schema.org/draft/2020-12/vocab/validation": true,
    }
});

let registry = Registry::try_from_resources(
    [("http://example.com/custom", Resource::from_contents(meta_schema))]
)?;

let validator = jsonschema::options()
    .with_registry(registry)
    .build(&schema)?;
```

**Draft Resolution:** Custom meta-schemas inherit draft-specific behavior from their underlying draft. For example, a custom meta-schema based on Draft 7 will preserve Draft 7 semantics (ignoring `$ref` siblings, validating formats by default). The validator walks the meta-schema chain to determine the appropriate draft. To override this behavior, use `.with_draft()` to explicitly set a draft version.

### Removed `meta::try_is_valid` and `meta::try_validate`

The `try_*` variants have been removed. The behavior has changed:

- **Old (0.34.x)**: `try_is_valid` and `try_validate` returned `Result<_, ReferencingError>` for unknown `$schema` values
- **New (0.35.x)**: `is_valid` **panics** for unknown `$schema` values, `validate` **returns `ValidationError`**

```rust
// Old (0.34.x)
match jsonschema::meta::try_is_valid(&schema) {
    Ok(is_valid) => println!("Valid: {}", is_valid),
    Err(e) => println!("Unknown schema: {}", e),
}

// New (0.35.x) - For known drafts only
let result = jsonschema::meta::is_valid(&schema); // Returns bool, panics on unknown $schema

// New (0.35.x) - For custom meta-schemas
let registry = Registry::try_from_resources([
    ("http://example.com/custom", Resource::from_contents(meta_schema))
])?;
let result = jsonschema::meta::options()
    .with_registry(registry)
    .is_valid(&schema); // Returns bool
```

### `Resource::from_contents` no longer returns `Result`

The method now always succeeds and returns `Resource` directly, since draft detection no longer fails for unknown `$schema` values.

```rust
// Old (0.34.x)
let resource = Resource::from_contents(schema)?;

// New (0.35.x)
let resource = Resource::from_contents(schema); // No ? needed
```

### Removed `primitive_type` module

The `primitive_type` module has been removed. Use `jsonschema::types` instead.

```rust
// Old (0.34.x)
use jsonschema::primitive_type::{PrimitiveType, PrimitiveTypesBitMap};

// New (0.35.x)
use jsonschema::types::{JsonType, JsonTypeSet};
```

## Upgrading from 0.33.x to 0.34.0

### Removed `Validator::config()`

The `Validator::config()` method has been removed to reduce memory footprint. The validator no longer stores the configuration internally.

```rust
// Old (0.33.x)
let validator = jsonschema::validator_for(&schema)?;
let config = validator.config(); // Returns Arc<ValidationOptions>

// New (0.34.x)
// No replacement - the config is not stored after compilation
// If you need config values, keep a reference to your ValidationOptions
let options = jsonschema::options().with_draft(Draft::Draft7);
let validator = options.build(&schema)?;
// Keep `options` around if you need to access configuration later
```

### Meta-validator statics replaced with functions

Public `DRAFT*_META_VALIDATOR` statics have been removed. Use the new `draftX::meta::validator()` helper functions instead. Dropping the `Send + Sync` bounds for retrievers means the old `LazyLock` statics can't store validators on `wasm32` anymore, so the new helper borrows cached validators on native platforms and builds owned copies on WebAssembly.

```rust
// Old (0.33.x)
use jsonschema::DRAFT7_META_VALIDATOR;
DRAFT7_META_VALIDATOR.is_valid(&schema);

// Also removed:
use jsonschema::DRAFT4_META_VALIDATOR;
use jsonschema::DRAFT6_META_VALIDATOR;
use jsonschema::DRAFT201909_META_VALIDATOR;
use jsonschema::DRAFT202012_META_VALIDATOR;

// New (0.34.x)
let validator = jsonschema::draft7::meta::validator();
validator.is_valid(&schema);

// Or use the module-specific helper:
jsonschema::draft7::meta::is_valid(&schema);
```

### Lifetime parameters removed from output types

`BasicOutput` and `Annotations` no longer have lifetime parameters. This simplifies the API and uses `Arc` for internal ownership.

```rust
// Old (0.33.x)
fn process_output<'a>(output: BasicOutput<'a>) -> Result<(), Error> {
    match output {
        BasicOutput::Valid(units) => {
            for unit in units {
                let annotations: &Annotations<'a> = unit.annotations();
                // ...
            }
        }
        BasicOutput::Invalid(errors) => { /* ... */ }
    }
    Ok(())
}

// New (0.34.x)
fn process_output(output: BasicOutput) -> Result<(), Error> {
    match output {
        BasicOutput::Valid(units) => {
            for unit in units {
                let annotations: &Annotations = unit.annotations();
                // ...
            }
        }
        BasicOutput::Invalid(errors) => { /* ... */ }
    }
    Ok(())
}
```

### WASM: Relaxed `Send + Sync` bounds

`Retrieve` / `AsyncRetrieve` on `wasm32` no longer require `Send + Sync`.

```rust
use jsonschema::{Retrieve, Uri};
use serde_json::Value;
use std::error::Error;

// Old (0.33.x)
use std::sync::{Arc, Mutex};
struct BrowserRetriever(Arc<Mutex<JsFetcher>>);

impl Retrieve for BrowserRetriever {
    fn retrieve(&self, uri: &Uri<String>) -> Result<Value, Box<dyn Error + Send + Sync>> {
        self.0.lock().unwrap().fetch(uri)
    }
}

// New (0.34.x)
use std::rc::Rc;
struct BrowserRetriever(Rc<JsFetcher>);

impl Retrieve for BrowserRetriever {
    fn retrieve(&self, uri: &Uri<String>) -> Result<Value, Box<dyn Error + Send + Sync>> {
        self.0.fetch(uri)
    }
}
```

Async retrievers follow the same pattern—switch `async_trait::async_trait` to `async_trait::async_trait(?Send)` on wasm so the implementation can hold non-thread-safe types.

```rust
// Old (0.33.x)
#[async_trait::async_trait]
impl AsyncRetrieve for BrowserRetriever {
    async fn retrieve(&self, uri: &Uri<String>) -> Result<Value, Box<dyn Error + Send + Sync>> {
        self.0.lock().unwrap().fetch(uri).await
    }
}

// New (0.34.x, wasm32)
#[async_trait::async_trait(?Send)]
impl AsyncRetrieve for BrowserRetriever {
    async fn retrieve(&self, uri: &Uri<String>) -> Result<Value, Box<dyn Error + Send + Sync>> {
        self.0.fetch(uri).await
    }
}
```

## Upgrading from 0.32.x to 0.33.0

In 0.33 `LocationSegment::Property` now holds a `Cow<'_, str>` and `LocationSegment` is no longer `Copy`. 

If your code matches the enum and treats the property as `&str`, update it like this.

This change was made to support proper round-trips for JSON Pointer segments (escaped vs. unescaped forms).

```rust
// Old (0.32.x)
match segment {
    LocationSegment::Property(p) => do_something(p), // p: &str
    LocationSegment::Index(i)    => ...
}

do_something_else(segment);

// New (0.33.0)
match segment {
    LocationSegment::Property(p) => do_something(&*p), // p: Cow<'_, str>
    LocationSegment::Index(i)    => ...
}

// `LocationSegment` is no longer Copy, use `.clone()` if you need ownership
do_something_else(segment.clone());
```

## Upgrading from 0.29.x to 0.30.0

`PrimitiveType` was replaced by `JsonType`, and `PrimitiveTypesBitMap` with `JsonTypeSet`.

```rust
// Old (0.29.x)
use jsonschema::primitive_types::PrimitiveType;
use jsonschema::primitive_types::PrimitiveTypesBitMap;

// New (0.30.0)
use jsonschema::JsonType;
use jsonschema::JsonTypeSet;
```

## Upgrading from 0.28.x to 0.29.0

The builder methods on `ValidationOptions` now take ownership of `self`. Change your code to use method chaining instead of reusing the options instance:

```rust
// Old (0.28.x)
let mut options = jsonschema::options();
options.with_draft(Draft::Draft202012);
options.with_format("custom", |s| s.len() > 3);
let validator = options.build(&schema)?;

// New (0.29.0)
let validator = jsonschema::options()
    .with_draft(Draft::Draft202012)
    .with_format("custom", |
... [TRUNCATED]
```

