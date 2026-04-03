---
id: mmalecot-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.134694
---

# KNOWLEDGE EXTRACT: mmalecot
> **Extracted on:** 2026-03-30 17:43:01
> **Source:** mmalecot

---

## File: `file-format.md`
```markdown
# 📦 mmalecot/file-format [🔖 PENDING/APPROVE]
🔗 https://github.com/mmalecot/file-format


## Meta
- **Stars:** ⭐ 130 | **Forks:** 🍴 22
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Crate for determining the file format of a given file or stream

## README (trích đầu)
```
# file-format

![Build](https://img.shields.io/github/actions/workflow/status/mmalecot/file-format/ci.yml?branch=main&style=flat-square&logo=github)
[![Crates.io](https://img.shields.io/crates/v/file-format.svg?style=flat-square)](https://crates.io/crates/file-format)
[![Docs](https://img.shields.io/docsrs/file-format?style=flat-square&logo=docs.rs)](https://docs.rs/file-format)
![Rust](https://img.shields.io/badge/rust-1.85+-blueviolet.svg?logo=rust&style=flat-square)
![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue.svg?style=flat-square)

Crate for determining the file format of a given file or stream.

It provides a variety of functions for identifying a wide range of file formats, including ZIP,
Compound File Binary (CFB), Extensible Markup Language (XML) and more.

It checks the signature of the file to determine its format and intelligently employs specific
readers when available for accurate identification. If the signature is not recognized, the crate
falls back to the default file format, which is Arbitrary Binary Data (BIN).

## Examples

Determines from a file:

```rust
use file_format::{FileFormat, Kind};

let fmt = FileFormat::from_file("fixtures/document/sample.pdf")?;
assert_eq!(fmt, FileFormat::PortableDocumentFormat);
assert_eq!(fmt.name(), "Portable Document Format");
assert_eq!(fmt.short_name(), Some("PDF"));
assert_eq!(fmt.media_type(), "application/pdf");
assert_eq!(fmt.extension(), "pdf");
assert_eq!(fmt.kind(), Kind::Document);
```

Determines from bytes:

```rust
use file_format::{FileFormat, Kind};

let fmt = FileFormat::from_bytes(&[0xFF, 0xD8, 0xFF]);
assert_eq!(fmt, FileFormat::JointPhotographicExpertsGroup);
assert_eq!(fmt.name(), "Joint Photographic Experts Group");
assert_eq!(fmt.short_name(), Some("JPEG"));
assert_eq!(fmt.media_type(), "image/jpeg");
assert_eq!(fmt.extension(), "jpg");
assert_eq!(fmt.kind(), Kind::Image);
```

## Usage

Add this to your `Cargo.toml`:

```toml
[dependencies]
file-format = "0.28"
```

## Crate features

All features below are disabled by default.

### Reader features

These features enable the detection of file formats that require a specific reader for
identification.

- `reader` - Enables all reader features.
- `reader-asf` - Enables Advanced Systems Format (ASF) based file formats detection.
- `reader-cfb` - Enables Compound File Binary (CFB) based file formats detection.
- `reader-ebml` - Enables Extensible Binary Meta Language (EBML) based file formats detection.
- `reader-exe` - Enables MS-DOS Executable (EXE) based file formats detection.
- `reader-id3v2` - Enables ID3v2 (ID3) based file formats detection.
- `reader-mp4` - Enables MPEG-4 Part 14 (MP4) based file formats detection.
- `reader-pdf` - Enables Portable Document Format (PDF) based file formats detection.
- `reader-rm` - Enables RealMedia (RM) based file formats detection.
- `reader-sqlite3` - Enables SQLite 3 based file formats detection.
- `reader-txt` - Enables Plain Text (TXT) file format de
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

