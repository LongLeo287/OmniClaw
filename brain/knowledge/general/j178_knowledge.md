---
id: j178-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:55.763603
---

# KNOWLEDGE EXTRACT: j178
> **Extracted on:** 2026-03-30 17:38:10
> **Source:** j178

---

## File: `prek.md`
```markdown
# 📦 j178/prek [🔖 PENDING/APPROVE]
🔗 https://github.com/j178/prek
🌐 https://prek.j178.dev/

## Meta
- **Stars:** ⭐ 7053 | **Forks:** 🍴 195
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
⚡ Better `pre-commit`, re-engineered in Rust

## README (trích đầu)
```
<div align="center">

<h1>
<img width="180" alt="prek" src="https://raw.githubusercontent.com/j178/prek/master/docs/assets/logo.webp" />

prek

</h1>

[![prek](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![PyPI version](https://img.shields.io/pypi/v/prek.svg)](https://pypi.python.org/pypi/prek)
[![codecov](https://codecov.io/github/j178/prek/graph/badge.svg?token=MP6TY24F43)](https://codecov.io/github/j178/prek)
[![PyPI Downloads](https://img.shields.io/pypi/dm/prek?logo=python)](https://pepy.tech/projects/prek)
[![Discord](https://img.shields.io/discord/1403581202102878289?logo=discord)](https://discord.gg/3NRJUqJz86)

</div>

<!-- --8<-- [start: description] -->

[pre-commit](https://pre-commit.com/) is a framework to run hooks written in many languages, and it manages the
language toolchain and dependencies for running the hooks.

*prek* is a reimagined version of pre-commit, built in Rust.
It is designed to be a faster, dependency-free and drop-in alternative for it,
while also providing some additional long-requested features.

<!-- --8<-- [end: description] -->

> [!NOTE]
> Although prek is pretty new, it’s already powering real‑world projects like [CPython](https://github.com/python/cpython), [Apache Airflow](https://github.com/apache/airflow), [FastAPI](https://github.com/fastapi/fastapi), and more projects are picking it up—see [Who is using prek?](#who-is-using-prek). If you’re looking for an alternative to `pre-commit`, please give it a try—we’d love your feedback!
>
> Please note that some languages are not yet supported for full drop‑in parity with `pre-commit`. See [Language Support](https://prek.j178.dev/languages/) for current status.

<!-- --8<-- [start:features] -->

## Features

- A single binary with no dependencies, does not require Python or any other runtime.
- [Faster](https://prek.j178.dev/benchmark/) than `pre-commit` and more efficient in disk space usage.
- Fully compatible with the original pre-commit configurations and hooks.
- Built-in support for monorepos (i.e. [workspace mode](https://prek.j178.dev/workspace/)).
- Integration with [`uv`](https://github.com/astral-sh/uv) for managing Python virtual environments and dependencies.
- Improved toolchain installations for Python, Node.js, Bun, Go, Rust and Ruby, shared between hooks.
- [Built-in](https://prek.j178.dev/builtin/) Rust-native implementation of some common hooks.

<!-- --8<-- [end:features] -->

## Table of contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [Why prek?](#why-prek)
- [Who is using prek?](#who-is-using-prek)
- [Acknowledgements](#acknowledgements)

## Installation

<details>
<summary>Standalone installer</summary>

prek provides a standalone installer script to download and install the tool,

On Linux and macOS:

<!-- --8<-- [start: linux-standalone-install] -->

```bash
curl --proto '=https' --tlsv1.2 -LsSf https://git
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

