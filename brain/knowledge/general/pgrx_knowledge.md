---
id: pgrx-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:20.545802
---

# OmniClaw Knowledge Report: pgrx

## Tech Stack
Unknown

## File Statistics
```json
{
  "": 48,
  ".yml": 1,
  ".lock": 2,
  ".toml": 48,
  ".log": 1,
  ".sh": 7,
  ".md": 62,
  ".png": 2,
  ".svg": 3,
  ".rs": 390,
  ".sql": 9,
  ".control": 32,
  ".out": 5,
  ".c": 2,
  ".h": 6,
  ".tmTheme": 1,
  ".stderr": 26,
  ".ignored": 1
}
```

## README Snippet
```markdown
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
   + More in the 
```

**Processed by OmniClaw Automated Intake**