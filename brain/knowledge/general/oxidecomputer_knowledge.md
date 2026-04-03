---
id: oxidecomputer-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:18.506454
---

# KNOWLEDGE EXTRACT: oxidecomputer
> **Extracted on:** 2026-03-30 17:50:35
> **Source:** oxidecomputer

---

## File: `progenitor.md`
```markdown
# 📦 oxidecomputer/progenitor [🔖 PENDING/APPROVE]
🔗 https://github.com/oxidecomputer/progenitor


## Meta
- **Stars:** ⭐ 880 | **Forks:** 🍴 123
- **Language:** Rust | **License:** MPL-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An OpenAPI client generator

## README (trích đầu)
```
# Progenitor

Progenitor is a Rust crate for generating opinionated clients from API
descriptions in the OpenAPI 3.0.x specification. It makes use of Rust
futures for `async` API calls and `Streams` for paginated interfaces.

It generates a type called `Client` with methods that correspond to the
operations specified in the OpenAPI document.

Progenitor can also generate a CLI to interact with an OpenAPI service
instance, and [`httpmock`](https://crates.io/crates/httpmock) helpers to
create a strongly typed mock of the OpenAPI service.

The primary target is OpenAPI documents emitted by
[Dropshot](https://github.com/oxidecomputer/dropshot)-generated APIs, but it
can be used for many OpenAPI documents. As OpenAPI covers a wide range of APIs,
Progenitor may fail for some OpenAPI documents. If you encounter a problem, you
can help the project by filing an issue that includes the OpenAPI document that
produced the problem.

## Using Progenitor

There are three different ways of using the `progenitor` crate. The one you
choose will depend on your use case and preferences.

### Macro

The simplest way to use Progenitor is via its `generate_api!` macro.

In a source file (often `main.rs`, `lib.rs`, or `mod.rs`) simply invoke the
macro:

```rust
generate_api!("path/to/openapi_document.json");
```

You'll need to add the following to `Cargo.toml`:

```toml
[dependencies]
futures = "0.3"
progenitor = { git = "https://github.com/oxidecomputer/progenitor" }
reqwest = { version = "0.13", features = ["json", "query", "stream"] }
serde = { version = "1.0", features = ["derive"] }
```

In addition, if the OpenAPI document contains string types with the `format`
field set to `date` or `date-time`, include

```toml
[dependencies]
chrono = { version = "0.4", features = ["serde"] }
```

Similarly, if there is a `format` field set to `uuid`:

```toml
[dependencies]
uuid = { version = "1.0.0", features = ["serde", "v4"] }
```

And if there are any websocket channel endpoints:

```toml
[dependencies]
base64 = "0.21"
rand = "0.8"
```

If types include regular expression validation:

```toml
[dependencies]
regress = "0.4.1"
```

The macro has some additional fancy options to control the generated code:

```rust
generate_api!(
    spec = "path/to/openapi_document.json",      // The OpenAPI document
    interface = Builder,                         // Choose positional (default) or builder style
    tags = Separate,                             // Tags may be Merged or Separate (default)
    inner_type = my_client::InnerType,           // Client inner type available to pre and post hooks
    pre_hook = closure::or::path::to::function,  // Hook invoked before issuing the HTTP request
    post_hook = closure::or::path::to::function, // Hook invoked prior to receiving the HTTP response
    derives = [ schemars::JsonSchema ],          // Additional derive macros applied to generated types
);
```

Note that the macro will be re-evaluated when the `spec` OpenAPI document
changes (
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

