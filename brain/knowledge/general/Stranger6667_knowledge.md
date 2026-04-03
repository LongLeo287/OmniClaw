---
id: stranger6667-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:18.710786
---

# KNOWLEDGE EXTRACT: Stranger6667
> **Extracted on:** 2026-03-30 17:54:06
> **Source:** Stranger6667

---

## File: `jsonschema.md`
```markdown
# 📦 Stranger6667/jsonschema [🔖 PENDING/APPROVE]
🔗 https://github.com/Stranger6667/jsonschema
🌐 https://docs.rs/jsonschema

## Meta
- **Stars:** ⭐ 761 | **Forks:** 🍴 121
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A high-performance JSON Schema validator for Rust

## README (trích đầu)
```
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
- 🔗 Bindings for [Python](https://github.com/Stranger6667/jsonschema/tree/master/crates/jsonschema-py) and [Rub
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

