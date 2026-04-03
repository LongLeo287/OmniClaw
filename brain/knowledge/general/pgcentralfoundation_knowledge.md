---
id: pgcentralfoundation-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:20.533624
---

# KNOWLEDGE EXTRACT: pgcentralfoundation
> **Extracted on:** 2026-03-30 17:51:00
> **Source:** pgcentralfoundation

---

## File: `pgrx.md`
```markdown
# 📦 pgcentralfoundation/pgrx [🔖 PENDING/APPROVE]
🔗 https://github.com/pgcentralfoundation/pgrx


## Meta
- **Stars:** ⭐ 4423 | **Forks:** 🍴 308
- **Language:** Rust | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Build Postgres Extensions with Rust!

## README (trích đầu)
```
![Logo](art/pgrx-logo-color-transparent-475x518.png)

# `pgrx`

> Build Postgres Extensions with Rust!

![GitHub Actions badge](https://github.com/pgcentralfoundation/pgrx/actions/workflows/tests.yml/badge.svg)
[![crates.io badge](https://img.shields.io/crates/v/pgrx.svg)](https://crates.io/crates/pgrx)
[![docs.rs badge](https://docs.rs/pgrx/badge.svg)](https://docs.rs/pgrx)
[![Twitter Follow](https://img.shields.io/twitter/follow/pgrx_rs.svg?style=flat)](https://twitter.com/pgrx_rs)
[![Discord Chat](https://img.shields.io/discord/710918545906597938.svg)][Discord]


`pgrx` is a framework for developing PostgreSQL extensions in Rust and strives to be as idiomatic and safe as possible.

`pgrx` supports Postgres 13 through Postgres 18.

## Want to chat with us or get a question answered?

   + **Please join our [Discord Server][Discord].**

   + **We are also in need of financial [sponsorship](https://checkout.square.site/merchant/MLHG5M9GAXQPV/checkout/2OW2SULDQBSZ2JLHSLRZQLZH).**

## Key Features

- **A fully managed development environment with [`cargo-pgrx`](../../../README.md)**
   + `cargo pgrx new`: Create new extensions quickly
   + `cargo pgrx init`: Install new (or register existing) PostgreSQL installs
   + `cargo pgrx run`: Run your extension and interactively test it in `psql` (or `pgcli`)
   + `cargo pgrx test`: Unit-test your extension across multiple PostgreSQL versions
   + `cargo pgrx package`: Create installation packages for your extension
   + More in the [`README.md`](../../../README.md)!
- **Target Multiple Postgres Versions**
   + Support from Postgres 13 to Postgres 17 from the same codebase
   + Use Rust feature gating to use version-specific APIs
   + Seamlessly test against all versions
- **Automatic Schema Generation**
   + Implement extensions entirely in Rust
   + [Automatic mapping for many Rust types into PostgreSQL](#mapping-of-postgres-types-to-rust)
   + SQL schemas generated automatically (or manually via `cargo pgrx schema`)
   + Include custom SQL with `extension_sql!` & `extension_sql_file!`
- **Safety First**
   + Translates Rust `panic!`s into Postgres `ERROR`s that abort the transaction, not the process
   + Memory Management follows Rust's drop semantics, even in the face of `panic!` and `elog(ERROR)`
   + `#[pg_guard]` procedural macro to ensure the above
   + Postgres `Datum`s are `Option<T> where T: FromDatum`
      - `NULL` Datums are safely represented as `Option::<T>::None`
- **First-class UDF support**
   + Annotate functions with `#[pg_extern]` to expose them to Postgres
   + Return `pgrx::iter::SetOfIterator<'a, T>` for `RETURNS SETOF`
   + Return `pgrx::iter::TableIterator<'a, T>` for `RETURNS TABLE (...)`
   + Create trigger functions with `#[pg_trigger]`
- **Easy Custom Types**
   + `#[derive(PostgresType)]` to use a Rust struct as a Postgres type
      - By default, represented as a CBOR-encoded object in-memory/on-disk, and JSON as human-readable
      - Supports `#[pg_binary_protocol]` t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

