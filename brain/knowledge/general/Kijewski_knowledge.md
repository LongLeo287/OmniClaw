---
id: kijewski-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.828118
---

# KNOWLEDGE EXTRACT: Kijewski
> **Extracted on:** 2026-03-30 17:38:16
> **Source:** Kijewski

---

## File: `zipsign.md`
```markdown
# 📦 Kijewski/zipsign [🔖 PENDING/APPROVE]
🔗 https://github.com/Kijewski/zipsign


## Meta
- **Stars:** ⭐ 25 | **Forks:** 🍴 5
- **Language:** Rust | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
## zipsign

A tool to sign and verify `.zip` and `.tar.gz` files with an ed25519 signing key.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Kijewski/zipsign/ci.yml?branch=main&style=flat-square&logoColor=white)](https://github.com/Kijewski/zipsign/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/zipsign?logo=rust&style=flat-square&logoColor=white)](https://crates.io/crates/zipsign)

### Install

```text
cargo install zipsign
```

or

```text
cargo install --git https://github.com/Kijewski/zipsign
```

### Example

* .zip:

    ```sh
    # Generate key pair:
    $ zipsign gen-key priv.key pub.key

    # ZIP a file and list the content of the ZIP file:
    $ zip Cargo.lock.zip Cargo.lock
    $ unzip -l Cargo.lock.zip
    Cargo.lock

    # Sign the ZIP file:
    $ zipsign sign zip Cargo.lock.zip priv.key
    $ unzip -l Cargo.lock.zip
    Cargo.lock

    # Verify that the generated signature is valid:
    $ zipsign verify zip Cargo.lock.zip pub.key
    OK
    ```

* .tar:

    ```sh
    # Generate key pair:
    $ zipsign gen-key priv.key pub.key

    # TAR a file and list the content of the ZIP file:
    $ tar czf Cargo.lock.tgz Cargo.lock
    $ tar tzf Cargo.lock.tgz
    Cargo.lock

    # Sign the .tar.gz file:
    $ zipsign sign tar Cargo.lock.tgz priv.key
    $ tar tzf Cargo.lock.tgz
    Cargo.lock

    # Verify that the generated signature is valid:
    $ zipsign verify tar Cargo.lock.tgz pub.key
    OK
    ```

### Generate key

Usage: `zipsign gen-key <PRIVATE_KEY> <VERIFYING_KEY>`

Arguments:

* `PRIVATE_KEY`:    Private key file to create
* `VERIFYING_KEY`:  Verifying key (public key) file to create

Options:

* `-e`, `--extract`: Don't create new key pair, but extract public key from private key
* `-f`, `--force`: Overwrite output file if it exists

### Sign a .zip or .tar.gz file

Usage: `zipsign sign [zip|tar] [-o <OUTPUT>] <INPUT> <KEYS>...`

Subcommands:

* `zip`: Sign a .zip file
* `tar`: Sign a .tar.gz file

Options:

* `-o`, `--output <OUTPUT>`:   Signed file to generate (if omitted, the input is overwritten)
* `-c`, `--context <CONTEXT>`: Arbitrary string used to salt the input, defaults to file name of `<INPUT>`
* `-f`, `--force`:             Overwrite output file if it exists

Arguments:

* `<INPUT>`:   Input file to sign
* `<KEYS>...`: One or more files containing private keys

### Verify a signature

Usage: `zipsign verify [zip|tar] <INPUT>`

Subcommands:

* `zip`: Verify a signed `.zip` file
* `tar`: Verify a signed `.tar.gz` file

Options:

* `-c`, `--context <CONTEXT>`: An arbitrary string used to salt the input, defaults to file name of `<INPUT>`
* `-q`, `--quiet`:             Don't write "OK" if the verification succeeded

Arguments:

* `<INPUT>`:   Signed `.zip` or `.tar.gz` file
* `<KEYS>...`: One or more files containing verifying keys

### Remove signatures

Usage: `zipsign unsign [zip|tar] [-o <OUTPUT>] <INPUT>`

Subcommands:

* `zip`: Removed signatures from `.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

