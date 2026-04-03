---
id: github.com-harehare-mq-conv-7db8b62d-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.586760
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq-conv_7db8b62d
> **Extracted on:** 2026-04-01 15:51:48
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524811/github.com_harehare_mq-conv_7db8b62d

---

## File: `.gitignore`
```
/target
settings.local.json
out
.DS_Store
```

## File: `Cargo.toml`
```
[package]
authors = ["Takahiro Sato <harehare1110@gmail.com>"]
categories = ["command-line-utilities", "text-processing"]
description = "A CLI tool for converting various file formats to Markdown"
edition = "2024"
homepage = "https://mqlang.org/"
keywords = ["markdown", "converter", "cli"]
license = "MIT"
name = "mq-conv"
readme = "README.md"
repository = "https://github.com/harehare/mq-conv"
version = "0.1.3"

[[bin]]
name = "mq-conv"
path = "src/main.rs"

[lib]
name = "mq_conv"
path = "src/lib.rs"

[features]
audio = ["dep:lofty"]
csv = ["dep:csv"]
default = [
  "excel",
  "pdf",
  "powerpoint",
  "word",
  "image",
  "zip",
  "epub",
  "audio",
  "csv",
  "html",
  "json",
  "yaml",
  "toml_conv",
  "xml",
  "sqlite",
  "tar",
  "video",
  "markdown_docx",
]
epub = ["dep:zip", "dep:quick-xml", "dep:mq-markdown"]
excel = ["dep:calamine"]
html = ["dep:mq-markdown"]
image = ["dep:image", "dep:kamadak-exif"]
json = ["dep:serde_json"]
markdown_docx = ["dep:docx-rs", "dep:mq-markdown"]
ocr = ["dep:leptess"]
pdf = ["dep:pdf-extract", "dep:lopdf"]
powerpoint = ["dep:zip", "dep:quick-xml"]
sqlite = ["dep:rusqlite"]
tar = ["dep:tar", "dep:flate2"]
toml_conv = ["dep:toml"]
video = ["dep:lofty"]
word = ["dep:zip", "dep:quick-xml"]
xml = ["dep:quick-xml"]
yaml = ["dep:serde_yaml"]
zip = ["dep:zip"]

[dependencies]
clap = {version = "4.6", features = ["derive"]}
miette = {version = "7", features = ["fancy"]}
thiserror = "2"

calamine = {version = "0.34", optional = true}
csv = {version = "1", optional = true}
docx-rs = {version = "0.4", optional = true}
flate2 = {version = "1", optional = true}
image = {version = "0.25", optional = true, default-features = false, features = ["png", "jpeg", "gif", "webp", "bmp", "tiff"]}
kamadak-exif = {version = "0.6", optional = true}
leptess = {version = "0.14", optional = true}
lofty = {version = "0.23", optional = true}
lopdf = {version = "0.38", optional = true}
mq-markdown = {version = "0.5.24", optional = true, features = ["html-to-markdown"]}
pdf-extract = {version = "0.10", optional = true}
quick-xml = {version = "0.39", optional = true}
rusqlite = {version = "0.39", optional = true, features = ["bundled"]}
serde_json = {version = "1", optional = true, features = ["preserve_order"]}
serde_yaml = {version = "0.9", optional = true}
tar = {version = "0.4", optional = true}
toml = {version = "1.1", optional = true}
zip = {version = "8.4", optional = true, default-features = false, features = ["deflate"]}

[dev-dependencies]
pretty_assertions = "1"
rstest = "0.26"

[profile.release]
codegen-units = 1
lto = "fat"
opt-level = "z"
panic = "abort"
strip = true
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Takahiro Sato

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
<h1 align="center">mq-conv</h1>

[![ci](https://github.com/harehare/mq-conv/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq-conv/actions/workflows/ci.yml)
[![mq language](https://img.shields.io/badge/mq-language-orange.svg)](https://github.com/harehare/mq)

A CLI tool for converting various file formats to Markdown

## Overview

`mq-conv` is a command-line tool that converts various file formats to Markdown. It supports 16+ formats including documents, spreadsheets, data formats, media files, and archives. Designed to work seamlessly with [mq](https://github.com/harehare/mq) and other Markdown processing tools.

### Key Features

- **Automatic Format Detection** - Detects file formats by extension and magic bytes
- **18+ Supported Formats** - Documents, data, media, and archives
- **Image OCR** - Extract text from images using Tesseract OCR
- **Markdown to Word** - Convert Markdown documents to `.docx` format
- **Stdin Support** - Pipe data directly from other commands
- **Modular Architecture** - Enable only the formats you need via feature flags

## Installation

### Using the Installation Script (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/harehare/mq-conv/main/bin/install.sh | bash
```

The installer will:
- Download the latest release for your platform
- Verify the binary with SHA256 checksum
- Install to `~/.mq-conv/bin/`
- Update your shell profile (bash, zsh, or fish)

After installation, restart your terminal or run:

```bash
source ~/.bashrc  # or ~/.zshrc, or ~/.config/fish/config.fish
```

### Cargo

```bash
# Install from crates.io
cargo install mq-conv
# Install using binstall
cargo binstall mq-conv@0.1.0
```

### From Source

```bash
git clone https://github.com/harehare/mq-conv.git
cd mq-conv
cargo build --release
# Binary will be at target/release/mq-conv
```

## Usage

### Basic Usage

```bash
# Convert a file to Markdown
mq-conv input.pdf

# Force a specific format
mq-conv input.bin --format json

# Pipe from stdin
cat input.json | mq-conv --format json
```

### Combine with mq

```bash
# Convert a PDF and query headings
mq conv document.pdf | mq '.h'

# Convert Excel and filter content
mq conv data.xlsx | mq '.table'
```

## Supported Formats

### Documents

| Format          | Extensions         |
| --------------- | ------------------ |
| Word            | `.docx`            |
| PowerPoint      | `.pptx`            |
| PDF             | `.pdf`             |
| EPUB            | `.epub`            |
| HTML            | `.html`            |
| Markdown → Word | `.md`, `.markdown` |

### Spreadsheets

| Format | Extensions                       |
| ------ | -------------------------------- |
| Excel  | `.xlsx`, `.xls`, `.xlsb`, `.ods` |
| CSV    | `.csv`, `.tsv`                   |

### Data Formats

| Format | Extensions                   |
| ------ | ---------------------------- |
| JSON   | `.json`                      |
| YAML   | `.yaml`, `.yml`              |
| TOML   | `.toml`                      |
| XML    | `.xml`                       |
| SQLite | `.sqlite`, `.sqlite3`, `.db` |

### Media

| Format | Extensions                                                        |
| ------ | ----------------------------------------------------------------- |
| Image  | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`, `.bmp`, `.tiff` |
| OCR    | any image (use `--format ocr`)                                    |
| Audio  | `.mp3`, `.wav`, `.flac`, `.ogg`, `.m4a`, `.aac`, `.wma`           |
| Video  | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, `.m4v`, `.wmv`, `.flv`   |

### Archives

| Format | Extensions     |
| ------ | -------------- |
| ZIP    | `.zip`         |
| TAR    | `.tar`, `.tgz` |

## Command-Line Options

```
Usage: mq-conv [OPTIONS] [FILE]

Arguments:
  [FILE]  Input file path (reads from stdin if omitted)

Options:
  -f, --format <FORMAT>  Force a specific format instead of auto-detecting
  -h, --help             Print help
  -V, --version          Print version
```

### Available Format Values

`excel`, `pdf`, `powerpoint`, `word`, `image`, `zip`, `epub`, `audio`, `csv`, `html`, `json`, `yaml`, `toml`, `xml`, `sqlite`, `tar`, `video`, `ocr`, `markdown-docx`

### OCR Requirements

The `ocr` feature requires Tesseract to be installed on your system:

```bash
# macOS
brew install tesseract

# Ubuntu/Debian
sudo apt install tesseract-ocr

# Arch Linux
sudo pacman -S tesseract
```

Usage:

```bash
# OCR an image to Markdown
mq-conv photo.png --format ocr

# Convert Markdown to Word docx
mq-conv document.md
mq-conv document.md --output-dir ./out  # creates document.docx
```

## Related Projects

- [mq](https://github.com/harehare/mq) - The underlying Markdown query processor
- [mq-tui](https://github.com/harehare/mq-tui) - Interactive terminal interface for mq
- [mqlang.org](https://mqlang.org) - Documentation and language reference

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT
```

## File: `deny.toml`
```
[graph]
all-features = false
no-default-features = false
targets = []

[output]
feature-depth = 1

[advisories]
ignore = []

[licenses]
allow = [
  "Apache-2.0 WITH LLVM-exception",
  "Apache-2.0",
  "BSD-3-Clause",
  "BSL-1.0",
  "CDLA-Permissive-2.0",
  "ISC",
  "MIT",
  "MPL-2.0",
  "NCSA",
  "Unicode-3.0",
  "Zlib",
  "MIT-0",
  "OpenSSL",
]
confidence-threshold = 0.8
exceptions = []

[licenses.private]
ignore = false
registries = []

[bans]
allow = []
deny = []
external-default-features = "allow"
highlight = "all"
multiple-versions = "warn"
skip = []
skip-tree = []
wildcards = "allow"
workspace-default-features = "allow"

[sources]
allow-git = []
allow-registry = ["https://github.com/rust-lang/crates.io-index"]
unknown-git = "warn"
unknown-registry = "warn"

[sources.allow-org]
bitbucket = []
github = []
gitlab = []
```

## File: `src/converter.rs`
```rust
use crate::error::Result;
use std::io::Write;

pub trait Converter {
    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()>;
    fn format_name(&self) -> &'static str;
    fn output_extension(&self) -> &'static str {
        "md"
    }
}
```

## File: `src/detect.rs`
```rust
use std::path::Path;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Format {
    Excel,
    Pdf,
    PowerPoint,
    Word,
    Image,
    Zip,
    Epub,
    Audio,
    Csv,
    Html,
    Json,
    Yaml,
    Toml,
    Xml,
    Sqlite,
    Tar,
    Video,
    Ocr,
    MarkdownDocx,
}

impl Format {
    pub fn detect(filename: Option<&str>, bytes: &[u8]) -> Option<Self> {
        if let Some(name) = filename
            && let Some(fmt) = Self::from_extension(name) {
                return Some(fmt);
            }
        Self::from_magic_bytes(bytes)
    }

    fn from_extension(filename: &str) -> Option<Self> {
        let ext = Path::new(filename)
            .extension()
            .and_then(|e| e.to_str())
            .map(|e| e.to_ascii_lowercase())?;

        match ext.as_str() {
            "xlsx" | "xls" | "xlsb" | "ods" => Some(Self::Excel),
            "pdf" => Some(Self::Pdf),
            "pptx" => Some(Self::PowerPoint),
            "docx" => Some(Self::Word),
            "png" | "jpg" | "jpeg" | "gif" | "webp" | "svg" | "bmp" | "tiff" | "tif" => {
                Some(Self::Image)
            }
            "zip" => Some(Self::Zip),
            "epub" => Some(Self::Epub),
            "mp3" | "wav" | "flac" | "ogg" | "m4a" | "aac" | "wma" => Some(Self::Audio),
            "csv" | "tsv" => Some(Self::Csv),
            "html" | "htm" => Some(Self::Html),
            "json" => Some(Self::Json),
            "yaml" | "yml" => Some(Self::Yaml),
            "toml" => Some(Self::Toml),
            "xml" => Some(Self::Xml),
            "sqlite" | "sqlite3" | "db" => Some(Self::Sqlite),
            "tar" => Some(Self::Tar),
            "tgz" => Some(Self::Tar),
            "mp4" | "mkv" | "avi" | "mov" | "webm" | "m4v" | "wmv" | "flv" => {
                Some(Self::Video)
            }
            "md" | "markdown" => Some(Self::MarkdownDocx),
            _ => None,
        }
    }

    fn from_magic_bytes(bytes: &[u8]) -> Option<Self> {
        if bytes.len() < 4 {
            return None;
        }

        // PDF: %PDF
        if bytes.starts_with(b"%PDF") {
            return Some(Self::Pdf);
        }

        // PNG: \x89PNG
        if bytes.starts_with(&[0x89, 0x50, 0x4E, 0x47]) {
            return Some(Self::Image);
        }

        // JPEG: \xFF\xD8\xFF
        if bytes.starts_with(&[0xFF, 0xD8, 0xFF]) {
            return Some(Self::Image);
        }

        // GIF: GIF87a or GIF89a
        if bytes.starts_with(b"GIF87a") || bytes.starts_with(b"GIF89a") {
            return Some(Self::Image);
        }

        // RIFF....WAVE (WAV)
        if bytes.len() >= 12 && bytes.starts_with(b"RIFF") && &bytes[8..12] == b"WAVE" {
            return Some(Self::Audio);
        }

        // FLAC
        if bytes.starts_with(b"fLaC") {
            return Some(Self::Audio);
        }

        // OGG
        if bytes.starts_with(b"OggS") {
            return Some(Self::Audio);
        }

        // MP3: ID3 tag or sync bytes
        if bytes.starts_with(b"ID3")
            || bytes.starts_with(&[0xFF, 0xFB])
            || bytes.starts_with(&[0xFF, 0xF3])
            || bytes.starts_with(&[0xFF, 0xF2])
        {
            return Some(Self::Audio);
        }

        // BMP
        if bytes.starts_with(b"BM") {
            return Some(Self::Image);
        }

        // TIFF
        if bytes.starts_with(&[0x49, 0x49, 0x2A, 0x00])
            || bytes.starts_with(&[0x4D, 0x4D, 0x00, 0x2A])
        {
            return Some(Self::Image);
        }

        // WEBP: RIFF....WEBP
        if bytes.len() >= 12 && bytes.starts_with(b"RIFF") && &bytes[8..12] == b"WEBP" {
            return Some(Self::Image);
        }

        // SQLite: "SQLite format 3\0"
        if bytes.len() >= 16 && bytes.starts_with(b"SQLite format 3\0") {
            return Some(Self::Sqlite);
        }

        // Gzip (tar.gz): \x1F\x8B
        if bytes.starts_with(&[0x1F, 0x8B]) {
            return Some(Self::Tar);
        }

        // ZIP-based formats: PK\x03\x04
        if bytes.starts_with(&[0x50, 0x4B, 0x03, 0x04]) {
            #[cfg(any(
                feature = "zip",
                feature = "word",
                feature = "powerpoint",
                feature = "excel",
                feature = "epub"
            ))]
            return Self::detect_zip_content(bytes);
            #[cfg(not(any(
                feature = "zip",
                feature = "word",
                feature = "powerpoint",
                feature = "excel",
                feature = "epub"
            )))]
            return Some(Self::Zip);
        }

        None
    }

    #[cfg(any(
        feature = "zip",
        feature = "word",
        feature = "powerpoint",
        feature = "excel",
        feature = "epub"
    ))]
    fn detect_zip_content(bytes: &[u8]) -> Option<Self> {
        let cursor = std::io::Cursor::new(bytes);
        let mut archive = zip::ZipArchive::new(cursor).ok()?;

        for i in 0..archive.len() {
            let entry = archive.by_index(i).ok()?;
            let name = entry.name().to_string();

            if name.starts_with("word/") {
                return Some(Self::Word);
            }
            if name.starts_with("ppt/") {
                return Some(Self::PowerPoint);
            }
            if name.starts_with("xl/") {
                return Some(Self::Excel);
            }
            if name == "mimetype" || name == "META-INF/container.xml" {
                return Some(Self::Epub);
            }
        }

        Some(Self::Zip)
    }
}

impl std::fmt::Display for Format {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Excel => write!(f, "excel"),
            Self::Pdf => write!(f, "pdf"),
            Self::PowerPoint => write!(f, "powerpoint"),
            Self::Word => write!(f, "word"),
            Self::Image => write!(f, "image"),
            Self::Zip => write!(f, "zip"),
            Self::Epub => write!(f, "epub"),
            Self::Audio => write!(f, "audio"),
            Self::Csv => write!(f, "csv"),
            Self::Html => write!(f, "html"),
            Self::Json => write!(f, "json"),
            Self::Yaml => write!(f, "yaml"),
            Self::Toml => write!(f, "toml"),
            Self::Xml => write!(f, "xml"),
            Self::Sqlite => write!(f, "sqlite"),
            Self::Tar => write!(f, "tar"),
            Self::Video => write!(f, "video"),
            Self::Ocr => write!(f, "ocr"),
            Self::MarkdownDocx => write!(f, "markdown-docx"),
        }
    }
}
```

## File: `src/error.rs`
```rust
use thiserror::Error;

pub type Result<T> = std::result::Result<T, Error>;

#[derive(Error, Debug)]
pub enum Error {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Unsupported format: {0}")]
    UnsupportedFormat(String),

    #[error("Format detection failed: could not determine file type")]
    DetectionFailed,

    #[error("Conversion error ({format}): {message}")]
    Conversion {
        format: &'static str,
        message: String,
    },

    #[error("Feature not enabled: {0}. Recompile with --features {0}")]
    FeatureDisabled(String),
}
```

## File: `src/formats.rs`
```rust
#[cfg(any(feature = "json", feature = "toml_conv", feature = "yaml"))]
pub mod structured;

#[cfg(feature = "audio")]
pub mod audio;
#[cfg(feature = "csv")]
pub mod csv;
#[cfg(feature = "epub")]
pub mod epub;
#[cfg(feature = "excel")]
pub mod excel;
#[cfg(feature = "html")]
pub mod html;
#[cfg(feature = "image")]
pub mod image;
#[cfg(feature = "json")]
pub mod json;
#[cfg(feature = "markdown_docx")]
pub mod markdown_docx;
#[cfg(feature = "ocr")]
pub mod ocr;
#[cfg(feature = "pdf")]
pub mod pdf;
#[cfg(feature = "powerpoint")]
pub mod powerpoint;
#[cfg(feature = "sqlite")]
pub mod sqlite;
#[cfg(feature = "tar")]
pub mod tar;
#[cfg(feature = "toml_conv")]
pub mod toml_conv;
#[cfg(feature = "video")]
pub mod video;
#[cfg(feature = "word")]
pub mod word;
#[cfg(feature = "xml")]
pub mod xml;
#[cfg(feature = "yaml")]
pub mod yaml;
#[cfg(feature = "zip")]
pub mod zip;

use crate::converter::Converter;
use crate::detect::Format;

pub fn get_converter(format: Format) -> crate::error::Result<Box<dyn Converter>> {
    match format {
        #[cfg(feature = "excel")]
        Format::Excel => Ok(Box::new(excel::ExcelConverter)),
        #[cfg(not(feature = "excel"))]
        Format::Excel => Err(crate::error::Error::FeatureDisabled("excel".into())),

        #[cfg(feature = "pdf")]
        Format::Pdf => Ok(Box::new(pdf::PdfConverter)),
        #[cfg(not(feature = "pdf"))]
        Format::Pdf => Err(crate::error::Error::FeatureDisabled("pdf".into())),

        #[cfg(feature = "powerpoint")]
        Format::PowerPoint => Ok(Box::new(powerpoint::PowerPointConverter)),
        #[cfg(not(feature = "powerpoint"))]
        Format::PowerPoint => Err(crate::error::Error::FeatureDisabled("powerpoint".into())),

        #[cfg(feature = "word")]
        Format::Word => Ok(Box::new(word::WordConverter)),
        #[cfg(not(feature = "word"))]
        Format::Word => Err(crate::error::Error::FeatureDisabled("word".into())),

        #[cfg(feature = "image")]
        Format::Image => Ok(Box::new(image::ImageConverter)),
        #[cfg(not(feature = "image"))]
        Format::Image => Err(crate::error::Error::FeatureDisabled("image".into())),

        #[cfg(feature = "zip")]
        Format::Zip => Ok(Box::new(zip::ZipConverter)),
        #[cfg(not(feature = "zip"))]
        Format::Zip => Err(crate::error::Error::FeatureDisabled("zip".into())),

        #[cfg(feature = "epub")]
        Format::Epub => Ok(Box::new(epub::EpubConverter)),
        #[cfg(not(feature = "epub"))]
        Format::Epub => Err(crate::error::Error::FeatureDisabled("epub".into())),

        #[cfg(feature = "audio")]
        Format::Audio => Ok(Box::new(audio::AudioConverter)),
        #[cfg(not(feature = "audio"))]
        Format::Audio => Err(crate::error::Error::FeatureDisabled("audio".into())),

        #[cfg(feature = "csv")]
        Format::Csv => Ok(Box::new(csv::CsvConverter)),
        #[cfg(not(feature = "csv"))]
        Format::Csv => Err(crate::error::Error::FeatureDisabled("csv".into())),

        #[cfg(feature = "html")]
        Format::Html => Ok(Box::new(html::HtmlConverter)),
        #[cfg(not(feature = "html"))]
        Format::Html => Err(crate::error::Error::FeatureDisabled("html".into())),

        #[cfg(feature = "json")]
        Format::Json => Ok(Box::new(json::JsonConverter)),
        #[cfg(not(feature = "json"))]
        Format::Json => Err(crate::error::Error::FeatureDisabled("json".into())),

        #[cfg(feature = "yaml")]
        Format::Yaml => Ok(Box::new(yaml::YamlConverter)),
        #[cfg(not(feature = "yaml"))]
        Format::Yaml => Err(crate::error::Error::FeatureDisabled("yaml".into())),

        #[cfg(feature = "toml_conv")]
        Format::Toml => Ok(Box::new(toml_conv::TomlConverter)),
        #[cfg(not(feature = "toml_conv"))]
        Format::Toml => Err(crate::error::Error::FeatureDisabled("toml".into())),

        #[cfg(feature = "xml")]
        Format::Xml => Ok(Box::new(xml::XmlConverter)),
        #[cfg(not(feature = "xml"))]
        Format::Xml => Err(crate::error::Error::FeatureDisabled("xml".into())),

        #[cfg(feature = "sqlite")]
        Format::Sqlite => Ok(Box::new(sqlite::SqliteConverter)),
        #[cfg(not(feature = "sqlite"))]
        Format::Sqlite => Err(crate::error::Error::FeatureDisabled("sqlite".into())),

        #[cfg(feature = "tar")]
        Format::Tar => Ok(Box::new(tar::TarConverter)),
        #[cfg(not(feature = "tar"))]
        Format::Tar => Err(crate::error::Error::FeatureDisabled("tar".into())),

        #[cfg(feature = "video")]
        Format::Video => Ok(Box::new(video::VideoConverter)),
        #[cfg(not(feature = "video"))]
        Format::Video => Err(crate::error::Error::FeatureDisabled("video".into())),

        #[cfg(feature = "ocr")]
        Format::Ocr => Ok(Box::new(ocr::OcrConverter)),
        #[cfg(not(feature = "ocr"))]
        Format::Ocr => Err(crate::error::Error::FeatureDisabled("ocr".into())),

        #[cfg(feature = "markdown_docx")]
        Format::MarkdownDocx => Ok(Box::new(markdown_docx::MarkdownDocxConverter)),
        #[cfg(not(feature = "markdown_docx"))]
        Format::MarkdownDocx => Err(crate::error::Error::FeatureDisabled("markdown-docx".into())),
    }
}
```

## File: `src/lib.rs`
```rust
pub mod converter;
pub mod detect;
pub mod error;
pub mod formats;
```

## File: `src/main.rs`
```rust
use std::fs;
use std::io::{self, BufWriter, IsTerminal, Read, Write};
use std::path::PathBuf;

use clap::{Parser, ValueEnum};
use miette::IntoDiagnostic;

use mq_conv::detect::Format;

#[derive(Parser, Debug)]
#[command(name = "mq-conv")]
#[command(version, about = "Convert various file formats to Markdown")]
struct Args {
    /// Input file paths (reads from stdin if not provided)
    files: Vec<PathBuf>,

    /// Force a specific format instead of auto-detecting
    #[arg(short, long)]
    format: Option<FormatArg>,

    /// Output directory for individual .md files (one per input file)
    #[arg(short, long)]
    output_dir: Option<PathBuf>,
}

#[derive(ValueEnum, Clone, Debug)]
enum FormatArg {
    Excel,
    Pdf,
    Powerpoint,
    Word,
    Image,
    Zip,
    Epub,
    Audio,
    Csv,
    Html,
    Json,
    Yaml,
    Toml,
    Xml,
    Sqlite,
    Tar,
    Video,
    Ocr,
    MarkdownDocx,
}

impl From<FormatArg> for Format {
    fn from(arg: FormatArg) -> Self {
        match arg {
            FormatArg::Excel => Format::Excel,
            FormatArg::Pdf => Format::Pdf,
            FormatArg::Powerpoint => Format::PowerPoint,
            FormatArg::Word => Format::Word,
            FormatArg::Image => Format::Image,
            FormatArg::Zip => Format::Zip,
            FormatArg::Epub => Format::Epub,
            FormatArg::Audio => Format::Audio,
            FormatArg::Csv => Format::Csv,
            FormatArg::Html => Format::Html,
            FormatArg::Json => Format::Json,
            FormatArg::Yaml => Format::Yaml,
            FormatArg::Toml => Format::Toml,
            FormatArg::Xml => Format::Xml,
            FormatArg::Sqlite => Format::Sqlite,
            FormatArg::Tar => Format::Tar,
            FormatArg::Video => Format::Video,
            FormatArg::Ocr => Format::Ocr,
            FormatArg::MarkdownDocx => Format::MarkdownDocx,
        }
    }
}

fn convert_one(
    input: &[u8],
    filename: Option<&str>,
    forced_format: Option<&FormatArg>,
    writer: &mut dyn Write,
) -> miette::Result<()> {
    let format = if let Some(f) = forced_format {
        f.clone().into()
    } else {
        Format::detect(filename, input).ok_or_else(|| {
            miette::miette!("Could not detect file format. Use --format to specify.")
        })?
    };

    let converter = mq_conv::formats::get_converter(format).map_err(|e| miette::miette!("{e}"))?;
    converter
        .convert(input, writer)
        .map_err(|e| miette::miette!("{e}"))?;
    Ok(())
}

fn main() -> miette::Result<()> {
    let args = Args::parse();

    if args.files.is_empty() {
        // stdin mode
        if io::stdin().is_terminal() {
            return Err(miette::miette!(
                "No input file specified and stdin is a terminal.\nUsage: mq-conv <FILE>... or pipe data to stdin with --format"
            ));
        }
        let mut buf = Vec::new();
        io::stdin().read_to_end(&mut buf).into_diagnostic()?;

        let stdout = io::stdout();
        let mut writer = BufWriter::new(stdout.lock());
        convert_one(&buf, None, args.format.as_ref(), &mut writer)?;
        writer.flush().into_diagnostic()?;
    } else if let Some(ref output_dir) = args.output_dir {
        // Output each file as individual output file
        fs::create_dir_all(output_dir).into_diagnostic()?;

        for path in &args.files {
            let input = fs::read(path).into_diagnostic()?;
            let filename = path.file_name().map(|n| n.to_string_lossy().into_owned());

            let stem = path
                .file_stem()
                .map(|s| s.to_string_lossy().into_owned())
                .unwrap_or_else(|| "output".to_string());

            let format = if let Some(f) = args.format.as_ref() {
                f.clone().into()
            } else {
                Format::detect(filename.as_deref(), &input).ok_or_else(|| {
                    miette::miette!("Could not detect file format. Use --format to specify.")
                })?
            };

            let converter =
                mq_conv::formats::get_converter(format).map_err(|e| miette::miette!("{e}"))?;
            let ext = converter.output_extension();
            let out_path = output_dir.join(format!("{stem}.{ext}"));

            let file = fs::File::create(&out_path).into_diagnostic()?;
            let mut writer = BufWriter::new(file);
            converter
                .convert(&input, &mut writer)
                .map_err(|e| miette::miette!("{e}"))?;
            writer.flush().into_diagnostic()?;
        }
    } else {
        // Output all to stdout
        let stdout = io::stdout();
        let mut writer = BufWriter::new(stdout.lock());

        for (i, path) in args.files.iter().enumerate() {
            if i > 0 {
                writeln!(writer, "\n---\n").into_diagnostic()?;
            }
            let input = fs::read(path).into_diagnostic()?;
            let filename = path.file_name().map(|n| n.to_string_lossy().into_owned());
            convert_one(
                &input,
                filename.as_deref(),
                args.format.as_ref(),
                &mut writer,
            )?;
        }
        writer.flush().into_diagnostic()?;
    }

    Ok(())
}
```

## File: `src/formats/audio.rs`
```rust
use std::io::{Cursor, Write};

use lofty::file::TaggedFileExt;
use lofty::prelude::*;
use lofty::probe::Probe;
use lofty::tag::ItemKey;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct AudioConverter;

impl Converter for AudioConverter {
    fn format_name(&self) -> &'static str {
        "audio"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let tagged_file =
            Probe::new(cursor)
                .guess_file_type()
                .map_err(|e| Error::Conversion {
                    format: "audio",
                    message: e.to_string(),
                })?
                .read()
                .map_err(|e| Error::Conversion {
                    format: "audio",
                    message: e.to_string(),
                })?;

        writeln!(writer, "# Audio")?;
        writeln!(writer)?;

        // File properties
        let props = tagged_file.properties();
        writeln!(writer, "## File Info")?;
        writeln!(writer)?;
        writeln!(writer, "| Property | Value |")?;
        writeln!(writer, "|----------|-------|")?;

        writeln!(
            writer,
            "| Format | {:?} |",
            tagged_file.file_type()
        )?;
        writeln!(writer, "| Size | {} |", format_size(input.len() as u64))?;

        let duration = props.duration();
        if !duration.is_zero() {
            let secs = duration.as_secs();
            let mins = secs / 60;
            let rem = secs % 60;
            writeln!(writer, "| Duration | {mins}:{rem:02} |")?;
        }

        if let Some(bitrate) = props.overall_bitrate() {
            writeln!(writer, "| Bitrate | {bitrate} kbps |")?;
        }

        if let Some(sample_rate) = props.sample_rate() {
            writeln!(writer, "| Sample Rate | {sample_rate} Hz |")?;
        }

        if let Some(channels) = props.channels() {
            let ch_label = match channels {
                1 => "Mono",
                2 => "Stereo",
                _ => "Multi-channel",
            };
            writeln!(writer, "| Channels | {channels} ({ch_label}) |")?;
        }

        writeln!(writer)?;

        // Tags
        if let Some(tag) = tagged_file.primary_tag().or(tagged_file.first_tag()) {
            let items: Vec<(&str, String)> = [
                ("Title", tag.get_string(ItemKey::TrackTitle)),
                ("Artist", tag.get_string(ItemKey::TrackArtist)),
                ("Album", tag.get_string(ItemKey::AlbumTitle)),
                ("Year", tag.get_string(ItemKey::Year)),
                ("Track", tag.get_string(ItemKey::TrackNumber)),
                ("Genre", tag.get_string(ItemKey::Genre)),
                ("Comment", tag.get_string(ItemKey::Comment)),
            ]
            .into_iter()
            .filter_map(|(k, v)| v.map(|v| (k, v.to_string())))
            .collect();

            if !items.is_empty() {
                writeln!(writer, "## Tags")?;
                writeln!(writer)?;
                writeln!(writer, "| Tag | Value |")?;
                writeln!(writer, "|-----|-------|")?;
                for (key, value) in &items {
                    writeln!(writer, "| {key} | {} |", value.replace('|', "\\|"))?;
                }
            }
        }

        Ok(())
    }
}

fn format_size(bytes: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = 1024 * KB;
    const GB: u64 = 1024 * MB;

    if bytes >= GB {
        format!("{:.1} GB", bytes as f64 / GB as f64)
    } else if bytes >= MB {
        format!("{:.1} MB", bytes as f64 / MB as f64)
    } else if bytes >= KB {
        format!("{:.1} KB", bytes as f64 / KB as f64)
    } else {
        format!("{bytes} B")
    }
}
```

## File: `src/formats/csv.rs`
```rust
use std::io::Write;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct CsvConverter;

impl Converter for CsvConverter {
    fn format_name(&self) -> &'static str {
        "csv"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let mut reader = csv::ReaderBuilder::new()
            .flexible(true)
            .from_reader(input);

        let headers = reader.headers().map_err(|e| Error::Conversion {
            format: "csv",
            message: e.to_string(),
        })?;

        let col_count = headers.len();
        if col_count == 0 {
            writeln!(writer, "*Empty CSV*")?;
            return Ok(());
        }

        // Header row
        write!(writer, "|")?;
        for field in headers.iter() {
            write!(writer, " {} |", escape_pipe(field))?;
        }
        writeln!(writer)?;

        // Separator
        write!(writer, "|")?;
        for _ in 0..col_count {
            write!(writer, "---|")?;
        }
        writeln!(writer)?;

        // Data rows
        for result in reader.records() {
            let record = result.map_err(|e| Error::Conversion {
                format: "csv",
                message: e.to_string(),
            })?;
            write!(writer, "|")?;
            for i in 0..col_count {
                let cell = record.get(i).unwrap_or("");
                write!(writer, " {} |", escape_pipe(cell))?;
            }
            writeln!(writer)?;
        }

        Ok(())
    }
}

fn escape_pipe(s: &str) -> String {
    s.replace('|', "\\|")
}
```

## File: `src/formats/epub.rs`
```rust
use std::io::{Cursor, Read, Write};

use quick_xml::Reader;
use quick_xml::events::Event;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct EpubConverter;

impl Converter for EpubConverter {
    fn format_name(&self) -> &'static str {
        "epub"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let mut archive = zip::ZipArchive::new(cursor).map_err(|e| Error::Conversion {
            format: "epub",
            message: e.to_string(),
        })?;

        // Find the OPF file path from container.xml
        let opf_path = find_opf_path(&mut archive)?;

        // Parse the OPF for metadata and spine order
        let opf_content = read_entry(&mut archive, &opf_path)?;
        let (metadata, spine_items) = parse_opf(&opf_content)?;

        // Resolve the base directory of the OPF file
        let opf_dir = if let Some(pos) = opf_path.rfind('/') {
            &opf_path[..=pos]
        } else {
            ""
        };

        // Write metadata
        if let Some(title) = &metadata.title {
            writeln!(writer, "# {title}")?;
        } else {
            writeln!(writer, "# EPUB")?;
        }
        writeln!(writer)?;

        if let Some(author) = &metadata.author {
            writeln!(writer, "**Author**: {author}")?;
        }
        if let Some(language) = &metadata.language {
            writeln!(writer, "**Language**: {language}")?;
        }
        if let Some(publisher) = &metadata.publisher {
            writeln!(writer, "**Publisher**: {publisher}")?;
        }
        if let Some(date) = &metadata.date {
            writeln!(writer, "**Date**: {date}")?;
        }
        if let Some(description) = &metadata.description {
            writeln!(writer)?;
            writeln!(writer, "> {description}")?;
        }

        writeln!(writer)?;
        writeln!(writer, "---")?;

        // Process spine items (chapters)
        let mut chapter_num = 0;
        for item_path in &spine_items {
            let full_path = if let Some(stripped) = item_path.strip_prefix('/') {
                stripped.to_string()
            } else {
                format!("{opf_dir}{item_path}")
            };

            if let Ok(html_content) = read_entry(&mut archive, &full_path) {
                let text = html_to_markdown(&html_content);
                let text = text.trim();
                if !text.is_empty() {
                    chapter_num += 1;

                    if chapter_num > 1 {
                        writeln!(writer)?;
                        writeln!(writer, "---")?;
                    }
                    writeln!(writer)?;
                    writeln!(writer, "{text}")?;
                }
            }
        }

        Ok(())
    }
}

#[derive(Default)]
struct EpubMetadata {
    title: Option<String>,
    author: Option<String>,
    language: Option<String>,
    publisher: Option<String>,
    description: Option<String>,
    date: Option<String>,
}

fn find_opf_path(archive: &mut zip::ZipArchive<Cursor<&[u8]>>) -> Result<String> {
    let container = read_entry(archive, "META-INF/container.xml")?;
    let mut reader = Reader::from_str(&container);

    loop {
        match reader.read_event() {
            Ok(Event::Empty(e)) | Ok(Event::Start(e)) if e.name().as_ref() == b"rootfile" => {
                for attr in e.attributes().flatten() {
                    if attr.key.as_ref() == b"full-path" {
                        return Ok(String::from_utf8_lossy(&attr.value).to_string());
                    }
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => {
                return Err(Error::Conversion {
                    format: "epub",
                    message: format!("Failed to parse container.xml: {e}"),
                });
            }
            _ => {}
        }
    }

    Err(Error::Conversion {
        format: "epub",
        message: "Could not find rootfile in container.xml".into(),
    })
}

fn parse_opf(content: &str) -> Result<(EpubMetadata, Vec<String>)> {
    let mut metadata = EpubMetadata::default();
    let mut manifest: Vec<(String, String)> = Vec::new(); // (id, href)
    let mut spine_ids: Vec<String> = Vec::new();

    let mut reader = Reader::from_str(content);
    let mut current_tag = String::new();
    let mut in_metadata = false;

    loop {
        match reader.read_event() {
            Ok(Event::Start(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "metadata" => in_metadata = true,
                    "title" | "creator" | "language" | "publisher" | "description" | "date"
                        if in_metadata =>
                    {
                        current_tag = local.clone();
                    }
                    "item" => {
                        let mut id = String::new();
                        let mut href = String::new();
                        for attr in e.attributes().flatten() {
                            match attr.key.as_ref() {
                                b"id" => id = String::from_utf8_lossy(&attr.value).to_string(),
                                b"href" => href = String::from_utf8_lossy(&attr.value).to_string(),
                                _ => {}
                            }
                        }
                        if !id.is_empty() && !href.is_empty() {
                            manifest.push((id, href));
                        }
                    }
                    _ => {}
                }
            }
            Ok(Event::Empty(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "item" => {
                        let mut id = String::new();
                        let mut href = String::new();
                        for attr in e.attributes().flatten() {
                            match attr.key.as_ref() {
                                b"id" => id = String::from_utf8_lossy(&attr.value).to_string(),
                                b"href" => href = String::from_utf8_lossy(&attr.value).to_string(),
                                _ => {}
                            }
                        }
                        if !id.is_empty() && !href.is_empty() {
                            manifest.push((id, href));
                        }
                    }
                    "itemref" => {
                        for attr in e.attributes().flatten() {
                            if attr.key.as_ref() == b"idref" {
                                spine_ids.push(String::from_utf8_lossy(&attr.value).to_string());
                            }
                        }
                    }
                    _ => {}
                }
            }
            Ok(Event::Text(e)) if !current_tag.is_empty() => {
                let text = e.decode().unwrap_or_default().to_string();
                match current_tag.as_str() {
                    "title" => metadata.title = Some(text),
                    "creator" => metadata.author = Some(text),
                    "language" => metadata.language = Some(text),
                    "publisher" => metadata.publisher = Some(text),
                    "description" => metadata.description = Some(text),
                    "date" => metadata.date = Some(text),
                    _ => {}
                }
            }
            Ok(Event::End(e)) => {
                let local = local_name(e.name().as_ref());
                if local == "metadata" {
                    in_metadata = false;
                }
                current_tag.clear();

                if local == "itemref" {
                    // Handle <itemref idref="..."></itemref> form
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => {
                return Err(Error::Conversion {
                    format: "epub",
                    message: format!("Failed to parse OPF: {e}"),
                });
            }
            _ => {}
        }
    }

    // Resolve spine IDs to file paths
    let spine_items: Vec<String> = spine_ids
        .iter()
        .filter_map(|id| {
            manifest
                .iter()
                .find(|(mid, _)| mid == id)
                .map(|(_, href)| href.clone())
        })
        .collect();

    Ok((metadata, spine_items))
}

fn read_entry(archive: &mut zip::ZipArchive<Cursor<&[u8]>>, name: &str) -> Result<String> {
    let mut file = archive.by_name(name).map_err(|e| Error::Conversion {
        format: "epub",
        message: format!("Entry not found: {name}: {e}"),
    })?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn html_to_markdown(html: &str) -> String {
    mq_markdown::convert_html_to_markdown(
        html,
        mq_markdown::ConversionOptions {
            extract_scripts_as_code_blocks: true,
            generate_front_matter: true,
            use_title_as_h1: true,
        },
    )
    .unwrap_or_default()
}

fn local_name(name: &[u8]) -> String {
    let s = std::str::from_utf8(name).unwrap_or("");
    if let Some(pos) = s.rfind(':') {
        s[pos + 1..].to_string()
    } else {
        s.to_string()
    }
}
```

## File: `src/formats/excel.rs`
```rust
use std::io::{Cursor, Write};

use calamine::{Data, Reader, open_workbook_auto_from_rs};

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct ExcelConverter;

impl Converter for ExcelConverter {
    fn format_name(&self) -> &'static str {
        "excel"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let mut workbook =
            open_workbook_auto_from_rs(cursor).map_err(|e| Error::Conversion {
                format: "excel",
                message: e.to_string(),
            })?;

        let sheet_names: Vec<String> = workbook.sheet_names().to_vec();

        for (idx, name) in sheet_names.iter().enumerate() {
            let range = workbook
                .worksheet_range(name)
                .map_err(|e| Error::Conversion {
                    format: "excel",
                    message: e.to_string(),
                })?;

            if idx > 0 {
                writeln!(writer)?;
            }
            writeln!(writer, "# {name}")?;

            let rows: Vec<Vec<String>> = range
                .rows()
                .map(|row| row.iter().map(format_cell).collect())
                .collect();

            if rows.is_empty() {
                writeln!(writer)?;
                writeln!(writer, "*Empty sheet*")?;
                continue;
            }

            let blocks = split_into_blocks(rows);
            if blocks.is_empty() {
                writeln!(writer)?;
                writeln!(writer, "*Empty sheet*")?;
                continue;
            }

            for block in blocks {
                writeln!(writer)?;
                match classify_block(block) {
                    Block::Table(rows) => write_table(writer, &rows)?,
                    Block::Text(lines) => write_text(writer, &lines)?,
                }
            }
        }

        Ok(())
    }
}

enum Block {
    Table(Vec<Vec<String>>),
    Text(Vec<String>),
}

fn split_into_blocks(rows: Vec<Vec<String>>) -> Vec<Vec<Vec<String>>> {
    let mut blocks = Vec::new();
    let mut current: Vec<Vec<String>> = Vec::new();

    for row in rows {
        if is_blank_row(&row) {
            if !current.is_empty() {
                blocks.push(current);
                current = Vec::new();
            }
        } else {
            current.push(row);
        }
    }

    if !current.is_empty() {
        blocks.push(current);
    }

    blocks
}

fn classify_block(block: Vec<Vec<String>>) -> Block {
    if block.len() >= 2 {
        let multi_col_rows = block
            .iter()
            .filter(|row| row.iter().filter(|c| !c.is_empty()).count() >= 2)
            .count();

        if multi_col_rows * 2 > block.len() {
            return Block::Table(block);
        }
    }

    let lines = block
        .into_iter()
        .map(|row| {
            row.into_iter()
                .filter(|c| !c.is_empty())
                .collect::<Vec<_>>()
                .join("  ")
        })
        .collect();

    Block::Text(lines)
}

fn write_table(writer: &mut dyn Write, rows: &[Vec<String>]) -> Result<()> {
    let col_count = rows.iter().map(|r| r.len()).max().unwrap_or(0);
    if col_count == 0 {
        return Ok(());
    }

    // Header row
    let header = &rows[0];
    write!(writer, "|")?;
    for i in 0..col_count {
        let cell = header.get(i).map(|s| s.as_str()).unwrap_or("");
        write!(writer, " {cell} |")?;
    }
    writeln!(writer)?;

    // Separator
    write!(writer, "|")?;
    for _ in 0..col_count {
        write!(writer, "---|")?;
    }
    writeln!(writer)?;

    // Data rows
    for row in rows.iter().skip(1) {
        write!(writer, "|")?;
        for i in 0..col_count {
            let cell = row.get(i).map(|s| s.as_str()).unwrap_or("");
            write!(writer, " {cell} |")?;
        }
        writeln!(writer)?;
    }

    Ok(())
}

fn write_text(writer: &mut dyn Write, lines: &[String]) -> Result<()> {
    let mut first = true;
    for line in lines {
        if line.is_empty() {
            continue;
        }
        if !first {
            writeln!(writer)?;
        }
        writeln!(writer, "{line}")?;
        first = false;
    }
    Ok(())
}

fn is_blank_row(row: &[String]) -> bool {
    row.iter().all(|c| c.is_empty())
}

fn format_cell(data: &Data) -> String {
    match data {
        Data::Empty => String::new(),
        Data::String(s) => escape_pipe(s),
        Data::Int(n) => n.to_string(),
        Data::Float(f) => {
            if *f == f.trunc() {
                format!("{f:.0}")
            } else {
                f.to_string()
            }
        }
        Data::Bool(b) => b.to_string(),
        Data::DateTime(dt) => escape_pipe(&dt.to_string()),
        Data::DateTimeIso(s) => escape_pipe(s),
        Data::DurationIso(s) => escape_pipe(s),
        Data::Error(e) => format!("#{e:?}"),
    }
}

fn escape_pipe(s: &str) -> String {
    s.replace('|', "\\|")
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::converter::Converter;
    use rstest::rstest;

    // ── unit tests ────────────────────────────────────────────────────────────

    #[rstest]
    #[case(vec![], true)]
    #[case(vec!["".to_string()], true)]
    #[case(vec!["".to_string(), "".to_string()], true)]
    #[case(vec!["a".to_string()], false)]
    #[case(vec!["".to_string(), "b".to_string()], false)]
    fn test_is_blank_row(#[case] row: Vec<String>, #[case] expected: bool) {
        assert_eq!(is_blank_row(&row), expected);
    }

    fn s(v: &[&str]) -> Vec<String> {
        v.iter().map(|s| s.to_string()).collect()
    }

    #[test]
    fn test_split_empty() {
        assert!(split_into_blocks(vec![]).is_empty());
    }

    #[test]
    fn test_split_no_blank_rows() {
        let rows = vec![s(&["a", "b"]), s(&["c", "d"])];
        let blocks = split_into_blocks(rows.clone());
        assert_eq!(blocks.len(), 1);
        assert_eq!(blocks[0], rows);
    }

    #[test]
    fn test_split_blank_row_separator() {
        let rows = vec![
            s(&["title"]),
            s(&[""]),
            s(&["Name", "Age"]),
            s(&["Alice", "30"]),
        ];
        let blocks = split_into_blocks(rows);
        assert_eq!(blocks.len(), 2);
        assert_eq!(blocks[0], vec![s(&["title"])]);
        assert_eq!(blocks[1], vec![s(&["Name", "Age"]), s(&["Alice", "30"])]);
    }

    #[test]
    fn test_split_multiple_blank_rows_collapsed() {
        let rows = vec![s(&["a"]), s(&[""]), s(&[""]), s(&["b"])];
        let blocks = split_into_blocks(rows);
        assert_eq!(blocks.len(), 2);
    }

    #[test]
    fn test_split_leading_trailing_blank_rows_ignored() {
        let rows = vec![s(&[""]), s(&["a", "b"]), s(&["c", "d"]), s(&[""])];
        let blocks = split_into_blocks(rows);
        assert_eq!(blocks.len(), 1);
    }

    #[test]
    fn test_classify_dense_multi_column_is_table() {
        let block = vec![
            s(&["Name", "Age", "City"]),
            s(&["Alice", "30", "Tokyo"]),
            s(&["Bob", "25", "Osaka"]),
        ];
        assert!(matches!(classify_block(block), Block::Table(_)));
    }

    #[test]
    fn test_classify_single_row_is_text() {
        let block = vec![s(&["Report Title"])];
        assert!(matches!(classify_block(block), Block::Text(_)));
    }

    #[test]
    fn test_classify_single_column_multi_row_is_text() {
        let block = vec![s(&["Line one"]), s(&["Line two"]), s(&["Line three"])];
        assert!(matches!(classify_block(block), Block::Text(_)));
    }

    #[test]
    fn test_classify_sparse_rows_is_text() {
        // Only 1 out of 3 rows has 2+ cells — does not reach majority threshold
        let block = vec![
            s(&["Label", "Value"]),
            s(&["Note"]),
            s(&["Footer"]),
        ];
        assert!(matches!(classify_block(block), Block::Text(_)));
    }

    // ── integration tests (require zip feature to build xlsx) ─────────────────

    #[cfg(feature = "zip")]
    mod xlsx_tests {
        use super::*;
        use std::io::Write;

        /// Build a minimal xlsx from a 2-D grid of strings.
        /// Empty rows in `rows` (empty slices `&[]`) become gaps in row numbering
        /// so calamine produces blank rows in the Range.
        fn make_xlsx(sheet_name: &str, rows: &[&[&str]]) -> Vec<u8> {
            fn col_letter(i: usize) -> char {
                (b'A' + i as u8) as char
            }

            let mut sheet_data = String::new();
            for (r, row) in rows.iter().enumerate() {
                if row.is_empty() {
                    continue; // gap → calamine fills with empty row
                }
                let row_num = r + 1;
                sheet_data.push_str(&format!("<row r=\"{row_num}\">"));
                for (c, cell) in row.iter().enumerate() {
                    if cell.is_empty() {
                        continue;
                    }
                    let addr = format!("{}{}", col_letter(c), row_num);
                    sheet_data.push_str(&format!(
                        "<c r=\"{addr}\" t=\"inlineStr\"><is><t>{cell}</t></is></c>"
                    ));
                }
                sheet_data.push_str("</row>");
            }

            let content_types = r#"<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>"#;

            let rels = r#"<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"#;

            let workbook = format!(
                r#"<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
          xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets><sheet name="{sheet_name}" sheetId="1" r:id="rId1"/></sheets>
</workbook>"#
            );

            let workbook_rels = r#"<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>"#;

            let worksheet = format!(
                r#"<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <sheetData>{sheet_data}</sheetData>
</worksheet>"#
            );

            let buf = Vec::new();
            let cursor = std::io::Cursor::new(buf);
            let mut zip = zip::ZipWriter::new(cursor);
            let opts = zip::write::SimpleFileOptions::default()
                .compression_method(zip::CompressionMethod::Stored);

            for (name, content) in [
                ("[Content_Types].xml", content_types.to_string()),
                ("_rels/.rels", rels.to_string()),
                ("xl/workbook.xml", workbook),
                ("xl/_rels/workbook.xml.rels", workbook_rels.to_string()),
                ("xl/worksheets/sheet1.xml", worksheet),
            ] {
                zip.start_file(name, opts).unwrap();
                zip.write_all(content.as_bytes()).unwrap();
            }

            zip.finish().unwrap().into_inner()
        }

        fn convert(data: &[u8]) -> String {
            let mut out = Vec::new();
            ExcelConverter.convert(data, &mut out).unwrap();
            String::from_utf8(out).unwrap()
        }

        #[test]
        fn test_pure_table() {
            let xlsx = make_xlsx(
                "Sales",
                &[
                    &["Name", "Age", "City"],
                    &["Alice", "30", "Tokyo"],
                    &["Bob", "25", "Osaka"],
                ],
            );
            let out = convert(&xlsx);
            assert!(out.contains("# Sales"), "sheet heading missing");
            assert!(out.contains("| Name | Age | City |"), "header row missing");
            assert!(out.contains("|---|---|---|"), "separator missing");
            assert!(out.contains("| Alice | 30 | Tokyo |"), "data row missing");
            assert!(out.contains("| Bob | 25 | Osaka |"), "data row missing");
        }

        #[test]
        fn test_text_only_single_column() {
            let xlsx = make_xlsx(
                "Notes",
                &[&["First note"], &["Second note"], &["Third note"]],
            );
            let out = convert(&xlsx);
            assert!(out.contains("First note"), "text line missing");
            assert!(out.contains("Second note"), "text line missing");
            assert!(!out.contains("|---|"), "should not be a table");
        }

        #[test]
        fn test_mixed_title_blank_table() {
            let xlsx = make_xlsx(
                "Report",
                &[
                    &["Monthly Report"],
                    &[], // blank row
                    &["Name", "Score"],
                    &["Alice", "95"],
                    &["Bob", "87"],
                ],
            );
            let out = convert(&xlsx);
            assert!(out.contains("Monthly Report"), "title missing");
            assert!(out.contains("| Name | Score |"), "table header missing");
            assert!(out.contains("| Alice | 95 |"), "table row missing");
            // title should NOT appear as a table row
            assert!(!out.contains("| Monthly Report |"), "title rendered as table row");
        }

        #[test]
        fn test_mixed_table_blank_note() {
            let xlsx = make_xlsx(
                "Sheet1",
                &[
                    &["Item", "Qty"],
                    &["Apple", "10"],
                    &[], // blank row
                    &["Note: draft only"],
                ],
            );
            let out = convert(&xlsx);
            assert!(out.contains("| Item | Qty |"), "table missing");
            assert!(out.contains("Note: draft only"), "note missing");
            assert!(!out.contains("| Note: draft only |"), "note rendered as table row");
        }

        #[test]
        fn test_pipe_escaped_in_cell() {
            let xlsx = make_xlsx("S", &[&["a|b", "c"], &["x|y", "z"]]);
            let out = convert(&xlsx);
            assert!(out.contains("a\\|b"), "pipe not escaped");
        }

        #[test]
        fn test_sheet_name_as_heading() {
            let xlsx = make_xlsx("MySheet", &[&["a", "b"], &["1", "2"]]);
            let out = convert(&xlsx);
            assert!(out.starts_with("# MySheet\n"), "sheet heading wrong");
        }
    }
}
```

## File: `src/formats/html.rs`
```rust
use std::io::Write;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct HtmlConverter;

impl Converter for HtmlConverter {
    fn format_name(&self) -> &'static str {
        "html"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let text = mq_markdown::convert_html_to_markdown(
            std::str::from_utf8(input).map_err(|e| Error::Conversion {
                format: "html",
                message: e.to_string(),
            })?,
            mq_markdown::ConversionOptions {
                extract_scripts_as_code_blocks: true,
                generate_front_matter: true,
                use_title_as_h1: true,
            },
        )
        .map_err(|e| Error::Conversion {
            format: "html",
            message: e.to_string(),
        })?;

        let trimmed = text.trim();
        if trimmed.is_empty() {
            writeln!(writer, "*Empty HTML document*")?;
        } else {
            writeln!(writer, "{trimmed}")?;
        }

        Ok(())
    }
}
```

## File: `src/formats/image.rs`
```rust
use std::io::{Cursor, Write};

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct ImageConverter;

impl Converter for ImageConverter {
    fn format_name(&self) -> &'static str {
        "image"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        if is_svg(input) {
            writeln!(writer, "# Image")?;
            writeln!(writer)?;
            writeln!(writer, "| Property | Value |")?;
            writeln!(writer, "|----------|-------|")?;
            writeln!(writer, "| Format | SVG |")?;
            writeln!(writer, "| Size | {} |", format_size(input.len() as u64))?;
            return Ok(());
        }

        let cursor = Cursor::new(input);
        let reader = image::ImageReader::new(cursor)
            .with_guessed_format()
            .map_err(|e| Error::Conversion {
                format: "image",
                message: e.to_string(),
            })?;

        let format = reader.format();
        let img = reader.decode().map_err(|e| Error::Conversion {
            format: "image",
            message: e.to_string(),
        })?;

        writeln!(writer, "# Image")?;
        writeln!(writer)?;
        writeln!(writer, "| Property | Value |")?;
        writeln!(writer, "|----------|-------|")?;

        if let Some(fmt) = format {
            writeln!(writer, "| Format | {fmt:?} |")?;
        }

        writeln!(writer, "| Size | {} |", format_size(input.len() as u64))?;
        writeln!(
            writer,
            "| Dimensions | {}x{} |",
            img.width(),
            img.height()
        )?;
        writeln!(writer, "| Color Type | {:?} |", img.color())?;

        write_exif(input, writer)?;

        Ok(())
    }
}

fn write_exif(input: &[u8], writer: &mut dyn Write) -> Result<()> {
    let exif_reader = exif::Reader::new();
    let mut cursor = Cursor::new(input);
    let exif_data: exif::Exif = match exif_reader.read_from_container(&mut cursor) {
        Ok(exif) => exif,
        Err(_) => return Ok(()),
    };

    let fields: Vec<(String, String)> = exif_data
        .fields()
        .filter_map(|f| {
            let tag_name = f.tag.to_string();
            let value = f.display_value().with_unit(&exif_data).to_string();
            if value.is_empty() || value == "unknown" {
                return None;
            }
            Some((tag_name, value))
        })
        .collect();

    if fields.is_empty() {
        return Ok(());
    }

    writeln!(writer)?;
    writeln!(writer, "## EXIF Metadata")?;
    writeln!(writer)?;
    writeln!(writer, "| Tag | Value |")?;
    writeln!(writer, "|-----|-------|")?;
    for (tag, value) in &fields {
        writeln!(writer, "| {tag} | {} |", value.replace('|', "\\|"))?;
    }

    Ok(())
}

fn is_svg(input: &[u8]) -> bool {
    let header = if input.len() > 256 { &input[..256] } else { input };
    let text = String::from_utf8_lossy(header);
    text.contains("<svg") || text.starts_with("<?xml")
}

fn format_size(bytes: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = 1024 * KB;

    if bytes >= MB {
        format!("{:.1} MB", bytes as f64 / MB as f64)
    } else if bytes >= KB {
        format!("{:.1} KB", bytes as f64 / KB as f64)
    } else {
        format!("{bytes} B")
    }
}
```

## File: `src/formats/json.rs`
```rust
use std::io::Write;

use crate::converter::Converter;
use crate::error::{Error, Result};
use crate::formats::structured;

pub struct JsonConverter;

impl Converter for JsonConverter {
    fn format_name(&self) -> &'static str {
        "json"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let value: serde_json::Value =
            serde_json::from_slice(input).map_err(|e| Error::Conversion {
                format: "json",
                message: e.to_string(),
            })?;

        let structured_value = structured::Value::from(value);
        structured::write_value_as_markdown(writer, &structured_value)?;

        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::converter::Converter;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    fn convert(input: &str) -> String {
        let converter = JsonConverter;
        let mut output = Vec::new();
        converter.convert(input.as_bytes(), &mut output).unwrap();
        String::from_utf8(output).unwrap()
    }

    #[rstest]
    #[case::primitive_string(r#""hello""#, "hello\n")]
    #[case::primitive_integer("42", "42\n")]
    #[case::primitive_bool("true", "true\n")]
    #[case::null("null", "\n")]
    fn test_primitive(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    #[case::flat_object(
        r#"{"name":"Alice","age":30}"#,
        "| Key | Value |\n|---|---|\n| name | Alice |\n| age | 30 |\n\n"
    )]
    #[case::nested_object(
        r#"{"name":"Alice","address":{"city":"Tokyo","zip":"100"}}"#,
        "| Key | Value |\n|---|---|\n| name | Alice |\n\n# address\n\n| Key | Value |\n|---|---|\n| city | Tokyo |\n| zip | 100 |\n\n"
    )]
    #[case::object_with_array_of_primitives(
        r#"{"tags":["rust","cli"]}"#,
        "# tags\n\n- rust\n- cli\n\n"
    )]
    #[case::object_with_array_of_objects(
        r#"{"users":[{"name":"Alice","role":"admin"},{"name":"Bob","role":"user"}]}"#,
        "# users\n\n| name | role |\n|---|---|\n| Alice | admin |\n| Bob | user |\n\n"
    )]
    fn test_object(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    #[case::array_of_primitives(r#"["a","b","c"]"#, "- a\n- b\n- c\n\n")]
    #[case::array_of_objects(
        r#"[{"id":1,"name":"x"},{"id":2,"name":"y"}]"#,
        "| id | name |\n|---|---|\n| 1 | x |\n| 2 | y |\n\n"
    )]
    #[case::empty_array("[]", "*empty*\n")]
    fn test_array(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    #[case::pipe_in_value(
        r#"{"cmd":"a|b"}"#,
        "| Key | Value |\n|---|---|\n| cmd | a\\|b |\n\n"
    )]
    fn test_escape(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    fn test_deep_nesting() {
        let input = r#"{"a":{"b":{"c":{"d":{"e":{"f":{"g":"deep"}}}}}}}"#;
        let output = convert(input);
        assert!(output.contains("###### f"));
        assert!(output.contains("deep"));
    }

    #[rstest]
    fn test_mixed_array() {
        let output = convert(r#"[1,{"key":"val"}]"#);
        assert!(output.contains("- 1"));
        assert!(output.contains("| Key | Value |"));
        assert!(output.contains("| key | val |"));
    }
}
```

## File: `src/formats/markdown_docx.rs`
```rust
use std::io::{Cursor, Write};

use docx_rs::{
    AbstractNumbering, AlignmentType, Docx, IndentLevel, Level, LevelJc, LevelText, NumberFormat,
    Numbering, NumberingId, Paragraph, Run, Start, Table, TableRow,
};
use mq_markdown::{Markdown, Node};

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct MarkdownDocxConverter;

impl Converter for MarkdownDocxConverter {
    fn format_name(&self) -> &'static str {
        "markdown-docx"
    }

    fn output_extension(&self) -> &'static str {
        "docx"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let markdown = std::str::from_utf8(input).map_err(|e| Error::Conversion {
            format: "markdown-docx",
            message: format!("Input is not valid UTF-8: {e}"),
        })?;

        let doc = build_docx(markdown).map_err(|e| Error::Conversion {
            format: "markdown-docx",
            message: e.to_string(),
        })?;

        let mut buf = Cursor::new(Vec::new());
        doc.build().pack(&mut buf).map_err(|e| Error::Conversion {
            format: "markdown-docx",
            message: format!("Failed to generate docx: {e}"),
        })?;

        writer.write_all(buf.get_ref())?;
        Ok(())
    }
}

fn heading_style(depth: u8) -> &'static str {
    match depth {
        1 => "Heading1",
        2 => "Heading2",
        3 => "Heading3",
        4 => "Heading4",
        5 => "Heading5",
        _ => "Heading6",
    }
}

// (text, bold, italic, code)
type RunInfo = (String, bool, bool, bool);

fn collect_runs(values: &[Node], bold: bool, italic: bool) -> Vec<RunInfo> {
    let mut runs = Vec::new();
    for v in values {
        match v {
            Node::Text(t) => runs.push((t.value.clone(), bold, italic, false)),
            Node::CodeInline(c) => runs.push((c.value.to_string(), false, false, true)),
            Node::Strong(s) => runs.extend(collect_runs(&s.values, true, italic)),
            Node::Emphasis(e) => runs.extend(collect_runs(&e.values, bold, true)),
            Node::Break(_) => runs.push((" ".to_string(), false, false, false)),
            Node::Link(l) => runs.extend(collect_runs(&l.values, bold, italic)),
            Node::Delete(d) => runs.extend(collect_runs(&d.values, bold, italic)),
            _ => {}
        }
    }
    runs
}

fn extract_text(values: &[Node]) -> String {
    collect_runs(values, false, false)
        .into_iter()
        .map(|(t, _, _, _)| t)
        .collect()
}

fn build_paragraph_from_runs(runs: Vec<RunInfo>) -> Paragraph {
    let mut para = Paragraph::new();
    for (text, bold, italic, code) in runs {
        let mut run = Run::new().add_text(&text);
        if bold {
            run = run.bold();
        }
        if italic {
            run = run.italic();
        }
        if code {
            run = run.fonts(docx_rs::RunFonts::new().ascii("Courier New"));
        }
        para = para.add_run(run);
    }
    para
}

fn flush_inline_runs(doc: Docx, runs: &mut Vec<RunInfo>) -> Docx {
    if runs.is_empty() {
        return doc;
    }
    let para = build_paragraph_from_runs(std::mem::take(runs));
    doc.add_paragraph(para)
}

fn flush_table(doc: Docx, table_data: &mut Vec<(usize, usize, String)>) -> Docx {
    if table_data.is_empty() {
        return doc;
    }
    let max_row = table_data.iter().map(|(r, _, _)| *r).max().unwrap_or(0);
    let col_count = table_data.iter().map(|(_, c, _)| *c).max().unwrap_or(0) + 1;

    let mut table = Table::new(vec![]);
    for row_idx in 0..=max_row {
        let mut cells = vec![];
        for col_idx in 0..col_count {
            let text = table_data
                .iter()
                .find(|(r, c, _)| *r == row_idx && *c == col_idx)
                .map(|(_, _, t)| t.as_str())
                .unwrap_or("");
            let mut run = Run::new().add_text(text);
            if row_idx == 0 {
                run = run.bold();
            }
            let cell = docx_rs::TableCell::new()
                .add_paragraph(Paragraph::new().align(AlignmentType::Left).add_run(run));
            cells.push(cell);
        }
        table = table.add_row(TableRow::new(cells));
    }
    table_data.clear();
    doc.add_table(table)
}

fn build_docx(markdown: &str) -> std::result::Result<Docx, Box<dyn std::error::Error>> {
    let mut doc = Docx::new();

    // Add a list numbering definition for unordered lists
    let abstract_numbering = AbstractNumbering::new(0).add_level(
        Level::new(
            0,
            Start::new(1),
            NumberFormat::new("bullet"),
            LevelText::new("•"),
            LevelJc::new("left"),
        )
        .indent(
            Some(720),
            Some(docx_rs::SpecialIndentType::Hanging(360)),
            None,
            None,
        ),
    );
    doc = doc.add_abstract_numbering(abstract_numbering);
    doc = doc.add_numbering(Numbering::new(1, 0));

    let parsed = markdown.parse::<Markdown>()?;

    let mut inline_runs: Vec<RunInfo> = Vec::new();
    let mut prev_end_line: Option<usize> = None;
    let mut table_data: Vec<(usize, usize, String)> = Vec::new();
    let mut in_table = false;
    let mut ordered_item_count: u64 = 0;
    let mut in_ordered_list = false;

    for node in &parsed.nodes {
        match node {
            Node::TableCell(cell) => {
                doc = flush_inline_runs(doc, &mut inline_runs);
                prev_end_line = None;
                in_table = true;
                in_ordered_list = false;
                ordered_item_count = 0;
                let text = extract_text(&cell.values);
                table_data.push((cell.row, cell.column, text));
                continue;
            }
            Node::TableAlign(_) => {
                continue;
            }
            _ => {
                if in_table {
                    doc = flush_table(doc, &mut table_data);
                    in_table = false;
                }
            }
        }

        match node {
            Node::Heading(h) => {
                doc = flush_inline_runs(doc, &mut inline_runs);
                in_ordered_list = false;
                ordered_item_count = 0;
                let text = extract_text(&h.values);
                let para = Paragraph::new()
                    .style(heading_style(h.depth))
                    .add_run(Run::new().add_text(&text));
                doc = doc.add_paragraph(para);
                prev_end_line = h.position.as_ref().map(|p| p.end.line);
            }

            Node::Code(c) => {
                doc = flush_inline_runs(doc, &mut inline_runs);
                in_ordered_list = false;
                ordered_item_count = 0;
                for line in c.value.lines() {
                    let para = Paragraph::new().add_run(
                        Run::new()
                            .add_text(line)
                            .fonts(docx_rs::RunFonts::new().ascii("Courier New")),
                    );
                    doc = doc.add_paragraph(para);
                }
                prev_end_line = c.position.as_ref().map(|p| p.end.line);
            }

            Node::List(l) => {
                doc = flush_inline_runs(doc, &mut inline_runs);
                let text = extract_text(&l.values);
                if l.ordered {
                    if !in_ordered_list {
                        ordered_item_count = 1;
                        in_ordered_list = true;
                    } else {
                        ordered_item_count += 1;
                    }
                    let formatted = format!("{ordered_item_count}. {text}");
                    let para = Paragraph::new().add_run(Run::new().add_text(&formatted));
                    doc = doc.add_paragraph(para);
                } else {
                    in_ordered_list = false;
                    ordered_item_count = 0;
                    let para = Paragraph::new()
                        .numbering(NumberingId::new(1), IndentLevel::new(0))
                        .add_run(Run::new().add_text(&text));
                    doc = doc.add_paragraph(para);
                }
                prev_end_line = l.position.as_ref().map(|p| p.end.line);
            }

            Node::Blockquote(bq) => {
                doc = flush_inline_runs(doc, &mut inline_runs);
                in_ordered_list = false;
                ordered_item_count = 0;
                let text = extract_text(&bq.values);
                let para = Paragraph::new()
                    .style("Quote")
                    .add_run(Run::new().add_text(&text));
                doc = doc.add_paragraph(para);
                prev_end_line = bq.position.as_ref().map(|p| p.end.line);
            }

            Node::HorizontalRule(_) => {
                doc = flush_inline_runs(doc, &mut inline_runs);
                in_ordered_list = false;
                ordered_item_count = 0;
                let para = Paragraph::new().add_run(Run::new().add_text("─".repeat(40)));
                doc = doc.add_paragraph(para);
                prev_end_line = None;
            }

            // Inline nodes — group into paragraphs using position info
            Node::Text(_)
            | Node::Strong(_)
            | Node::Emphasis(_)
            | Node::CodeInline(_)
            | Node::Break(_)
            | Node::Link(_)
            | Node::Delete(_) => {
                in_ordered_list = false;
                ordered_item_count = 0;
                if let Some(pos) = node.position()
                    && let Some(end) = prev_end_line
                {
                    if pos.start.line > end + 1 {
                        doc = flush_inline_runs(doc, &mut inline_runs);
                    }
                    prev_end_line = Some(pos.end.line);
                }
                let runs = match node {
                    Node::Text(t) => vec![(t.value.clone(), false, false, false)],
                    Node::Strong(s) => collect_runs(&s.values, true, false),
                    Node::Emphasis(e) => collect_runs(&e.values, false, true),
                    Node::CodeInline(c) => vec![(c.value.to_string(), false, false, true)],
                    Node::Break(_) => vec![(" ".to_string(), false, false, false)],
                    Node::Link(l) => collect_runs(&l.values, false, false),
                    Node::Delete(d) => collect_runs(&d.values, false, false),
                    _ => vec![],
                };
                inline_runs.extend(runs);
            }

            _ => {}
        }
    }

    if in_table {
        doc = flush_table(doc, &mut table_data);
    }
    doc = flush_inline_runs(doc, &mut inline_runs);

    Ok(doc)
}
```

## File: `src/formats/ocr.rs`
```rust
use std::io::Write;

use leptess::LepTess;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct OcrConverter;

impl Converter for OcrConverter {
    fn format_name(&self) -> &'static str {
        "ocr"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let mut lt = LepTess::new(None, "eng").map_err(|e| Error::Conversion {
            format: "ocr",
            message: format!("Failed to initialize Tesseract (is tesseract installed?): {e}"),
        })?;

        lt.set_image_from_mem(input).map_err(|e| Error::Conversion {
            format: "ocr",
            message: format!("Failed to load image for OCR: {e}"),
        })?;

        let text = lt.get_utf8_text().map_err(|e| Error::Conversion {
            format: "ocr",
            message: format!("OCR extraction failed: {e}"),
        })?;

        for line in text.lines() {
            let trimmed = line.trim();
            if !trimmed.is_empty() {
                writeln!(writer, "{trimmed}")?;
            } else {
                writeln!(writer)?;
            }
        }

        Ok(())
    }
}
```

## File: `src/formats/pdf.rs`
```rust
use std::io::Write;

use lopdf::Document;
use pdf_extract::{
    ColorSpace, MediaBox, OutputDev, OutputError, Path, PathOp, Transform, output_doc,
};

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct PdfConverter;

impl Converter for PdfConverter {
    fn format_name(&self) -> &'static str {
        "pdf"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let doc = Document::load_mem(input).map_err(|e| Error::Conversion {
            format: "pdf",
            message: e.to_string(),
        })?;

        write_metadata(&doc, writer)?;

        let mut collector = PageCollector::new();
        output_doc(&doc, &mut collector).map_err(|e| Error::Conversion {
            format: "pdf",
            message: e.to_string(),
        })?;

        if collector.pages.is_empty() {
            writeln!(
                writer,
                "*PDF contains no extractable text (may be scanned/image-based)*"
            )?;
            return Ok(());
        }

        let total_pages = collector.pages.len();
        for (i, page) in collector.pages.into_iter().enumerate() {
            writeln!(writer, "## Page {}", i + 1)?;
            writeln!(writer)?;

            if page.glyphs.is_empty() {
                writeln!(writer, "*Empty page*")?;
            } else {
                write_page_content(writer, page)?;
            }

            if i + 1 < total_pages {
                writeln!(writer)?;
                writeln!(writer, "---")?;
                writeln!(writer)?;
            }
        }

        Ok(())
    }
}

// ---------------------------------------------------------------------------
// Positional data structures
// ---------------------------------------------------------------------------

struct Glyph {
    x: f64,
    y: f64,
    advance: f64,
    ch: String,
}

struct PageData {
    glyphs: Vec<Glyph>,
    rects: Vec<(f64, f64, f64, f64)>, // (x, y, width, height)
}

struct PageCollector {
    pages: Vec<PageData>,
    current_glyphs: Vec<Glyph>,
    current_rects: Vec<(f64, f64, f64, f64)>,
}

impl PageCollector {
    fn new() -> Self {
        Self {
            pages: Vec::new(),
            current_glyphs: Vec::new(),
            current_rects: Vec::new(),
        }
    }

    fn collect_rects_from_path(&mut self, ctm: &Transform, path: &Path) {
        for op in &path.ops {
            if let PathOp::Rect(rx, ry, rw, rh) = op {
                let w = (rw * ctm.m11).abs();
                let h = (rh * ctm.m22).abs();
                // Only keep rectangles large enough to be table borders (>5pt each dimension)
                if w > 5.0 && h > 2.0 {
                    let x = ctm.m31 + rx * ctm.m11 + ry * ctm.m21;
                    let y = ctm.m32 + rx * ctm.m12 + ry * ctm.m22;
                    self.current_rects.push((x, y, w, h));
                }
            }
        }
    }
}

impl OutputDev for PageCollector {
    fn begin_page(
        &mut self,
        _page_num: u32,
        _media_box: &MediaBox,
        _art_box: Option<(f64, f64, f64, f64)>,
    ) -> std::result::Result<(), OutputError> {
        self.current_glyphs.clear();
        self.current_rects.clear();
        Ok(())
    }

    fn end_page(&mut self) -> std::result::Result<(), OutputError> {
        self.pages.push(PageData {
            glyphs: std::mem::take(&mut self.current_glyphs),
            rects: std::mem::take(&mut self.current_rects),
        });
        Ok(())
    }

    fn output_character(
        &mut self,
        trm: &Transform,
        width: f64,
        _spacing: f64,
        font_size: f64,
        char: &str,
    ) -> std::result::Result<(), OutputError> {
        let x = trm.m31;
        let y = trm.m32;
        // Approximate advance width in page units
        let scale = (trm.m11 * trm.m11 + trm.m12 * trm.m12).sqrt();
        let advance = width.abs() * font_size.abs() * scale;
        self.current_glyphs.push(Glyph {
            x,
            y,
            advance,
            ch: char.to_string(),
        });
        Ok(())
    }

    fn begin_word(&mut self) -> std::result::Result<(), OutputError> {
        Ok(())
    }
    fn end_word(&mut self) -> std::result::Result<(), OutputError> {
        Ok(())
    }
    fn end_line(&mut self) -> std::result::Result<(), OutputError> {
        Ok(())
    }

    fn stroke(
        &mut self,
        ctm: &Transform,
        _: &ColorSpace,
        _: &[f64],
        path: &Path,
    ) -> std::result::Result<(), OutputError> {
        self.collect_rects_from_path(ctm, path);
        Ok(())
    }

    fn fill(
        &mut self,
        ctm: &Transform,
        _: &ColorSpace,
        _: &[f64],
        path: &Path,
    ) -> std::result::Result<(), OutputError> {
        self.collect_rects_from_path(ctm, path);
        Ok(())
    }
}

// ---------------------------------------------------------------------------
// Word / line building
// ---------------------------------------------------------------------------

struct Word {
    x: f64,
    y: f64,
    text: String,
}

struct TextLine {
    y: f64,
    words: Vec<Word>,
}

fn build_words(mut glyphs: Vec<Glyph>) -> Vec<Word> {
    if glyphs.is_empty() {
        return Vec::new();
    }
    // Sort top-to-bottom (y descending in PDF space), then left-to-right
    glyphs.sort_by(|a, b| {
        b.y.partial_cmp(&a.y)
            .unwrap_or(std::cmp::Ordering::Equal)
            .then(a.x.partial_cmp(&b.x).unwrap_or(std::cmp::Ordering::Equal))
    });

    let mut words: Vec<Word> = Vec::new();
    let mut buf = String::new();
    let mut wx = glyphs[0].x;
    let mut wy = glyphs[0].y;
    let mut prev_x_end = glyphs[0].x + glyphs[0].advance.max(1.0);
    let mut prev_y = glyphs[0].y;

    for glyph in &glyphs {
        let y_diff = (glyph.y - prev_y).abs();
        let x_gap = glyph.x - prev_x_end;
        // New line (>3pt y diff) or significant horizontal gap = word boundary
        let new_word = y_diff > 3.0 || x_gap > 4.0;

        if new_word && !buf.trim().is_empty() {
            words.push(Word {
                x: wx,
                y: wy,
                text: buf.trim().to_string(),
            });
            buf.clear();
            wx = glyph.x;
            wy = glyph.y;
        } else if new_word {
            buf.clear();
            wx = glyph.x;
            wy = glyph.y;
        }

        if buf.is_empty() {
            wx = glyph.x;
            wy = glyph.y;
        }

        buf.push_str(&glyph.ch);
        prev_x_end = glyph.x + glyph.advance.max(1.0);
        prev_y = glyph.y;
    }

    if !buf.trim().is_empty() {
        words.push(Word {
            x: wx,
            y: wy,
            text: buf.trim().to_string(),
        });
    }

    words.retain(|w| !w.text.is_empty());
    words
}

fn build_lines(mut words: Vec<Word>) -> Vec<TextLine> {
    if words.is_empty() {
        return Vec::new();
    }
    // Sort top-to-bottom
    words.sort_by(|a, b| b.y.partial_cmp(&a.y).unwrap_or(std::cmp::Ordering::Equal));

    let mut lines: Vec<TextLine> = Vec::new();
    for word in words {
        if let Some(last) = lines.last_mut()
            && (word.y - last.y).abs() < 3.0
        {
            last.words.push(word);
            continue;
        }
        lines.push(TextLine {
            y: word.y,
            words: vec![word],
        });
    }

    for line in &mut lines {
        line.words
            .sort_by(|a, b| a.x.partial_cmp(&b.x).unwrap_or(std::cmp::Ordering::Equal));
    }

    lines
}

// ---------------------------------------------------------------------------
// Table detection
// ---------------------------------------------------------------------------

/// Cluster a list of x-positions into column boundaries (within `tol` points).
fn cluster_columns(positions: &[f64], tol: f64) -> Vec<f64> {
    let mut sorted = positions.to_vec();
    sorted.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    sorted.dedup_by(|a, b| (*a - *b).abs() < tol);
    sorted
}

/// Assign a word to the nearest column index.
fn nearest_col(x: f64, cols: &[f64]) -> usize {
    cols.iter()
        .enumerate()
        .min_by(|&(_, a), &(_, b)| {
            (x - a)
                .abs()
                .partial_cmp(&(x - b).abs())
                .unwrap_or(std::cmp::Ordering::Equal)
        })
        .map(|(i, _)| i)
        .unwrap_or(0)
}

/// Try to interpret a slice of consecutive lines as a table.
/// Returns Some(rows) if the lines look like a table, None otherwise.
fn try_as_table(lines: &[&TextLine]) -> Option<Vec<Vec<String>>> {
    if lines.len() < 2 {
        return None;
    }

    // Collect all word x-start positions
    let all_x: Vec<f64> = lines
        .iter()
        .flat_map(|l| l.words.iter().map(|w| w.x))
        .collect();

    let cols = cluster_columns(&all_x, 8.0);
    if cols.len() < 2 {
        return None;
    }

    // Count how many lines have words aligned to ≥2 distinct columns
    let aligned = lines
        .iter()
        .filter(|line| {
            let mut used_cols = std::collections::HashSet::new();
            for w in &line.words {
                used_cols.insert(nearest_col(w.x, &cols));
            }
            used_cols.len() >= 2
        })
        .count();

    // Require ≥ 2/3 of lines to be multi-column, and at least 2 such lines
    if aligned < 2 || aligned * 3 < lines.len() * 2 {
        return None;
    }

    // Build table rows: merge words that fall into the same cell
    let rows: Vec<Vec<String>> = lines
        .iter()
        .map(|line| {
            let mut cells: Vec<String> = vec![String::new(); cols.len()];
            for word in &line.words {
                let ci = nearest_col(word.x, &cols);
                if !cells[ci].is_empty() {
                    cells[ci].push(' ');
                }
                cells[ci].push_str(&word.text);
            }
            cells
        })
        .collect();

    Some(rows)
}

/// Check whether rectangles suggest a grid (table borders).
fn rects_suggest_table(rects: &[(f64, f64, f64, f64)]) -> bool {
    rects.len() >= 4
}

// ---------------------------------------------------------------------------
// Markdown rendering
// ---------------------------------------------------------------------------

fn render_table(writer: &mut dyn Write, rows: &[Vec<String>]) -> Result<()> {
    if rows.is_empty() {
        return Ok(());
    }
    let col_count = rows.iter().map(|r| r.len()).max().unwrap_or(0);
    if col_count == 0 {
        return Ok(());
    }

    for (i, row) in rows.iter().enumerate() {
        let cells: Vec<String> = (0..col_count)
            .map(|ci| {
                row.get(ci)
                    .map(|s| s.replace('|', "\\|"))
                    .unwrap_or_default()
            })
            .collect();
        writeln!(writer, "| {} |", cells.join(" | "))?;

        // Insert separator after first row (header)
        if i == 0 {
            let sep: Vec<&str> = (0..col_count).map(|_| "---").collect();
            writeln!(writer, "| {} |", sep.join(" | "))?;
        }
    }
    writeln!(writer)?;
    Ok(())
}

// ---------------------------------------------------------------------------
// Main page content renderer
// ---------------------------------------------------------------------------

/// Compute the median y-gap between consecutive lines (typical line height).
fn typical_line_spacing(lines: &[TextLine]) -> f64 {
    if lines.len() < 2 {
        return 14.0;
    }
    let mut gaps: Vec<f64> = lines
        .windows(2)
        .map(|w| (w[0].y - w[1].y).abs())
        .filter(|&g| g > 1.0)
        .collect();
    if gaps.is_empty() {
        return 14.0;
    }
    gaps.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    gaps[gaps.len() / 2]
}

fn line_to_string(line: &TextLine) -> String {
    line.words
        .iter()
        .map(|w| w.text.as_str())
        .collect::<Vec<_>>()
        .join(" ")
}

fn is_bullet_line(s: &str) -> bool {
    s.starts_with('•')
        || s.starts_with('●')
        || s.starts_with('○')
        || s.starts_with('–')
        || s.starts_with("- ")
        || s.starts_with("* ")
}

fn write_page_content(writer: &mut dyn Write, page: PageData) -> Result<()> {
    let has_table_rects = rects_suggest_table(&page.rects);
    let words = build_words(page.glyphs);
    let lines = build_lines(words);

    if lines.is_empty() {
        return Ok(());
    }

    let spacing = typical_line_spacing(&lines);
    // A gap larger than this threshold signals a paragraph break.
    // Use 1.4× median spacing; tighten to avoid joining across section breaks.
    let para_gap = spacing * 1.4;

    let mut i = 0;
    while i < lines.len() {
        // --- Table detection: try to grow a table region from i ---
        let mut table_end = i + 1;
        while table_end <= lines.len() {
            let slice: Vec<&TextLine> = lines[i..table_end].iter().collect();
            if try_as_table(&slice).is_none() && !(has_table_rects && table_end - i >= 2) {
                break;
            }
            table_end += 1;
        }
        table_end -= 1;

        if table_end > i + 1 {
            let slice: Vec<&TextLine> = lines[i..table_end].iter().collect();
            if let Some(rows) = try_as_table(&slice) {
                render_table(writer, &rows)?;
                i = table_end;
                continue;
            }
        }

        // --- Special single-line elements (bullets, numbered lists) ---
        let first_text = line_to_string(&lines[i]);
        let first_trimmed = first_text.trim();

        if is_bullet_line(first_trimmed) {
            let content = if first_trimmed.starts_with("- ") || first_trimmed.starts_with("* ") {
                first_trimmed[2..].trim()
            } else {
                first_trimmed[first_trimmed.chars().next().unwrap().len_utf8()..].trim()
            };
            writeln!(writer, "- {content}")?;
            i += 1;
            continue;
        }

        if let Some(content) = strip_numbered_prefix(first_trimmed) {
            writeln!(writer, "1. {content}")?;
            i += 1;
            continue;
        }

        // --- Paragraph grouping: accumulate lines until a break condition ---
        let mut para_lines: Vec<&TextLine> = vec![&lines[i]];
        let mut j = i + 1;

        while j < lines.len() {
            let y_gap = (lines[j - 1].y - lines[j].y).abs();

            // Large vertical gap → paragraph break
            if y_gap > para_gap {
                break;
            }

            let next_text = line_to_string(&lines[j]);
            let next_trimmed = next_text.trim();

            // Next line is a list item or starts a table → break
            if is_bullet_line(next_trimmed) || strip_numbered_prefix(next_trimmed).is_some() {
                break;
            }
            if j + 1 < lines.len() {
                let two: Vec<&TextLine> = lines[j..j + 2].iter().collect();
                if try_as_table(&two).is_some() {
                    break;
                }
            }

            para_lines.push(&lines[j]);
            j += 1;
        }

        write_paragraph(writer, &para_lines)?;
        i = j;
    }

    Ok(())
}

/// Join a group of consecutive lines into a single paragraph and write it.
fn write_paragraph(writer: &mut dyn Write, lines: &[&TextLine]) -> Result<()> {
    let mut para = String::new();

    for line in lines {
        let t = line_to_string(line);
        let t = t.trim();
        if t.is_empty() {
            continue;
        }

        // Handle hyphenated line breaks: "implemen-" + "tation" → "implementation"
        if para.ends_with('-') {
            let prev_alpha = para
                .chars()
                .rev()
                .nth(1)
                .map(|c| c.is_alphabetic())
                .unwrap_or(false);
            let next_lower = t.chars().next().map(|c| c.is_lowercase()).unwrap_or(false);
            if prev_alpha && next_lower {
                para.pop(); // remove hyphen
                para.push_str(t);
                continue;
            }
        }

        if !para.is_empty() {
            para.push(' ');
        }
        para.push_str(t);
    }

    let para = para.trim().to_string();
    if para.is_empty() {
        return Ok(());
    }

    // Single isolated line → check for heading
    if lines.len() == 1 && is_heading_candidate(&para) {
        writeln!(writer, "### {para}")?;
        writeln!(writer)?;
        return Ok(());
    }

    writeln!(writer, "{para}")?;
    writeln!(writer)?;
    Ok(())
}

// ---------------------------------------------------------------------------
// Metadata
// ---------------------------------------------------------------------------

fn write_metadata(doc: &Document, writer: &mut dyn Write) -> Result<()> {
    let info = extract_info(doc);
    if info.is_empty() {
        return Ok(());
    }

    let title = info.iter().find(|(k, _)| k == "Title").map(|(_, v)| v);
    if let Some(title) = title {
        if !title.is_empty() {
            writeln!(writer, "# {title}")?;
        } else {
            writeln!(writer, "# PDF Document")?;
        }
    } else {
        writeln!(writer, "# PDF Document")?;
    }
    writeln!(writer)?;

    let mut has_meta = false;
    for (key, value) in &info {
        if key == "Title" || value.is_empty() {
            continue;
        }
        writeln!(writer, "- **{key}**: {value}")?;
        has_meta = true;
    }

    if has_meta {
        writeln!(writer)?;
    }

    writeln!(writer, "---")?;
    writeln!(writer)?;

    Ok(())
}

fn extract_info(doc: &Document) -> Vec<(String, String)> {
    let mut info = Vec::new();

    let info_dict = doc
        .trailer
        .get(b"Info")
        .ok()
        .and_then(|obj| obj.as_reference().ok())
        .and_then(|id| doc.get_dictionary(id).ok());

    let Some(dict) = info_dict else {
        return info;
    };

    let keys = [
        (b"Title".as_slice(), "Title"),
        (b"Author", "Author"),
        (b"Subject", "Subject"),
        (b"Creator", "Creator"),
        (b"Producer", "Producer"),
        (b"CreationDate", "Created"),
        (b"ModDate", "Modified"),
    ];

    for (pdf_key, label) in keys {
        if let Ok(obj) = dict.get(pdf_key) {
            let text = pdf_object_to_string(obj);
            if !text.is_empty() {
                info.push((label.to_string(), text));
            }
        }
    }

    info
}

fn pdf_object_to_string(obj: &lopdf::Object) -> String {
    match obj {
        lopdf::Object::String(bytes, _) => {
            if bytes.len() >= 2 && bytes[0] == 0xFE && bytes[1] == 0xFF {
                let chars: Vec<u16> = bytes[2..]
                    .chunks(2)
                    .filter_map(|c| {
                        if c.len() == 2 {
                            Some(u16::from_be_bytes([c[0], c[1]]))
                        } else {
                            None
                        }
                    })
                    .collect();
                String::from_utf16_lossy(&chars)
            } else {
                String::from_utf8_lossy(bytes).to_string()
            }
        }
        _ => String::new(),
    }
}

// ---------------------------------------------------------------------------
// Text helpers (shared with structured text path)
// ---------------------------------------------------------------------------

fn is_heading_candidate(line: &str) -> bool {
    let len = line.len();
    if !(2..=80).contains(&len) {
        return false;
    }
    let last = line.chars().last().unwrap();
    if matches!(last, '.' | ',' | ';' | '!' | '?' | ')') {
        return false;
    }
    let first = line.chars().next().unwrap();
    if !first.is_uppercase() && !first.is_ascii_digit() {
        return false;
    }
    line.split_whitespace().count() <= 10
}

fn strip_numbered_prefix(line: &str) -> Option<&str> {
    let trimmed = line.trim_start();
    let rest = trimmed.trim_start_matches(|c: char| c.is_ascii_digit());
    if rest.len() < trimmed.len() {
        if let Some(rest) = rest.strip_prefix(". ") {
            return Some(rest);
        }
        if let Some(rest) = rest.strip_prefix(") ") {
            return Some(rest);
        }
    }
    None
}
```

## File: `src/formats/powerpoint.rs`
```rust
use std::io::{Cursor, Read, Write};

use quick_xml::Reader;
use quick_xml::events::Event;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct PowerPointConverter;

impl Converter for PowerPointConverter {
    fn format_name(&self) -> &'static str {
        "powerpoint"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let mut archive = zip::ZipArchive::new(cursor).map_err(|e| Error::Conversion {
            format: "powerpoint",
            message: e.to_string(),
        })?;

        let mut slide_names: Vec<String> = Vec::new();
        for i in 0..archive.len() {
            if let Ok(entry) = archive.by_index(i) {
                let name = entry.name().to_string();
                if name.starts_with("ppt/slides/slide") && name.ends_with(".xml") {
                    slide_names.push(name);
                }
            }
        }

        slide_names.sort_by_key(|name| {
            name.trim_start_matches("ppt/slides/slide")
                .trim_end_matches(".xml")
                .parse::<u32>()
                .unwrap_or(0)
        });

        for (idx, slide_name) in slide_names.iter().enumerate() {
            let xml = read_entry(&mut archive, slide_name)?;
            let content = extract_slide_content(&xml)?;

            if idx > 0 {
                writeln!(writer)?;
                writeln!(writer, "---")?;
                writeln!(writer)?;
            }

            // Use first shape as slide title if it looks like a title
            let mut title_written = false;
            if let Some(first) = content.shapes.first()
                && first.is_title {
                    let text = join_paragraphs_inline(&first.paragraphs);
                    writeln!(writer, "# {text}")?;
                    writeln!(writer)?;
                    title_written = true;
                }

            if !title_written {
                writeln!(writer, "# Slide {}", idx + 1)?;
                writeln!(writer)?;
            }

            let start = if title_written { 1 } else { 0 };
            let content_shapes: Vec<_> = content.shapes[start..]
                .iter()
                .filter(|s| !s.paragraphs.is_empty())
                .collect();

            if content_shapes.is_empty() && content.tables.is_empty() && !title_written {
                writeln!(writer, "*Empty slide*")?;
            }

            for shape in &content_shapes {
                if shape.is_subtitle {
                    let text = join_paragraphs_inline(&shape.paragraphs);
                    if !text.is_empty() {
                        writeln!(writer, "## {text}")?;
                        writeln!(writer)?;
                    }
                } else {
                    for para in &shape.paragraphs {
                        let text = render_paragraph(para);
                        let text = text.trim();
                        if text.is_empty() {
                            continue;
                        }

                        if shape.has_bullets {
                            writeln!(writer, "- {text}")?;
                        } else {
                            writeln!(writer, "{text}")?;
                            writeln!(writer)?;
                        }
                    }
                    if shape.has_bullets {
                        writeln!(writer)?;
                    }
                }
            }

            // Write tables
            for table in &content.tables {
                write_table(writer, table)?;
                writeln!(writer)?;
            }

            // Speaker notes
            let notes_name =
                slide_name.replace("ppt/slides/slide", "ppt/notesSlides/notesSlide");
            if let Ok(notes_xml) = read_entry(&mut archive, &notes_name) {
                let notes_content = extract_slide_content(&notes_xml)?;
                let notes_text: String = notes_content
                    .shapes
                    .iter()
                    .flat_map(|s| &s.paragraphs)
                    .map(render_paragraph)
                    .map(|s| s.trim().to_string())
                    .filter(|s| !s.is_empty() && !s.chars().all(|c| c.is_ascii_digit()))
                    .collect::<Vec<_>>()
                    .join("\n");
                if !notes_text.is_empty() {
                    writeln!(writer, "> **Notes**: {notes_text}")?;
                    writeln!(writer)?;
                }
            }
        }

        Ok(())
    }
}

struct SlideContent {
    shapes: Vec<SlideShape>,
    tables: Vec<Vec<Vec<String>>>,
}

struct SlideShape {
    paragraphs: Vec<Paragraph>,
    is_title: bool,
    is_subtitle: bool,
    has_bullets: bool,
}

struct Paragraph {
    runs: Vec<TextRun>,
}

struct TextRun {
    text: String,
    bold: bool,
    italic: bool,
}

fn render_paragraph(para: &Paragraph) -> String {
    para.runs
        .iter()
        .map(|run| format_run_text(&run.text, run.bold, run.italic))
        .collect::<String>()
}

fn join_paragraphs_inline(paragraphs: &[Paragraph]) -> String {
    paragraphs
        .iter()
        .map(render_paragraph)
        .collect::<Vec<_>>()
        .join(" ")
}

fn format_run_text(text: &str, bold: bool, italic: bool) -> String {
    if text.is_empty() {
        return String::new();
    }
    match (bold, italic) {
        (true, true) => format!("***{text}***"),
        (true, false) => format!("**{text}**"),
        (false, true) => format!("*{text}*"),
        (false, false) => text.to_string(),
    }
}

fn extract_slide_content(xml: &str) -> Result<SlideContent> {
    let mut shapes = Vec::new();
    let mut tables: Vec<Vec<Vec<String>>> = Vec::new();
    let mut reader = Reader::from_str(xml);

    let mut in_shape = false;
    let mut in_text_body = false;
    let mut in_paragraph = false;
    let mut in_run = false;
    let mut in_text = false;
    let mut in_ppr = false;
    let mut in_rpr = false;
    let mut in_table = false;
    let mut in_table_row = false;
    let mut in_table_cell = false;

    let mut current_run = TextRun {
        text: String::new(),
        bold: false,
        italic: false,
    };
    let mut current_paragraph = Paragraph { runs: Vec::new() };
    let mut paragraphs: Vec<Paragraph> = Vec::new();
    let mut shape_type = String::new();
    let mut has_bullets = false;

    let mut table_rows: Vec<Vec<String>> = Vec::new();
    let mut table_row: Vec<String> = Vec::new();
    let mut cell_text = String::new();

    loop {
        match reader.read_event() {
            Ok(Event::Start(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "sp" | "pic" if !in_table => {
                        in_shape = true;
                        paragraphs.clear();
                        shape_type.clear();
                        has_bullets = false;
                    }
                    "txBody" => in_text_body = true,
                    "p" if in_text_body => {
                        in_paragraph = true;
                        current_paragraph = Paragraph { runs: Vec::new() };
                    }
                    "pPr" if in_paragraph => in_ppr = true,
                    "r" if in_paragraph => {
                        in_run = true;
                        current_run = TextRun {
                            text: String::new(),
                            bold: false,
                            italic: false,
                        };
                    }
                    "rPr" if in_run => {
                        in_rpr = true;
                        // Check attributes for bold/italic
                        for attr in e.attributes().flatten() {
                            match attr.key.as_ref() {
                                b"b" => {
                                    current_run.bold =
                                        attr.value.as_ref() == b"1" || attr.value.as_ref() == b"true";
                                }
                                b"i" => {
                                    current_run.italic =
                                        attr.value.as_ref() == b"1" || attr.value.as_ref() == b"true";
                                }
                                _ => {}
                            }
                        }
                    }
                    "t" if in_run => in_text = true,
                    "tbl" => {
                        in_table = true;
                        table_rows.clear();
                    }
                    "tr" if in_table => {
                        in_table_row = true;
                        table_row.clear();
                    }
                    "tc" if in_table_row => {
                        in_table_cell = true;
                        cell_text.clear();
                    }
                    _ => {}
                }
            }
            Ok(Event::Empty(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "ph" => {
                        for attr in e.attributes().flatten() {
                            if attr.key.as_ref() == b"type" {
                                shape_type =
                                    String::from_utf8_lossy(&attr.value).to_string();
                            }
                        }
                        if shape_type.is_empty() {
                            shape_type = "body".to_string();
                        }
                    }
                    "buChar" | "buAutoNum" | "buFont" if in_ppr => {
                        has_bullets = true;
                    }
                    "rPr" if in_run => {
                        // Self-closing rPr
                        for attr in e.attributes().flatten() {
                            match attr.key.as_ref() {
                                b"b" => {
                                    current_run.bold =
                                        attr.value.as_ref() == b"1" || attr.value.as_ref() == b"true";
                                }
                                b"i" => {
                                    current_run.italic =
                                        attr.value.as_ref() == b"1" || attr.value.as_ref() == b"true";
                                }
                                _ => {}
                            }
                        }
                    }
                    _ => {}
                }
            }
            Ok(Event::Text(e)) => {
                let decoded = e.decode().unwrap_or_default().to_string();
                if in_table_cell {
                    cell_text.push_str(&decoded);
                } else if in_text {
                    current_run.text.push_str(&decoded);
                }
            }
            Ok(Event::End(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "sp" | "pic" if !in_table => {
                        if in_shape && !paragraphs.is_empty() {
                            let is_title = matches!(
                                shape_type.as_str(),
                                "title" | "ctrTitle"
                            );
                            let is_subtitle = matches!(
                                shape_type.as_str(),
                                "subTitle"
                            );
                            shapes.push(SlideShape {
                                paragraphs: std::mem::take(&mut paragraphs),
                                is_title,
                                is_subtitle,
                                has_bullets,
                            });
                        }
                        in_shape = false;
                    }
                    "txBody" => in_text_body = false,
                    "p" if in_text_body && !in_table_cell => {
                        if in_paragraph && !current_paragraph.runs.is_empty() {
                            paragraphs.push(std::mem::replace(
                                &mut current_paragraph,
                                Paragraph { runs: Vec::new() },
                            ));
                        }
                        in_paragraph = false;
                    }
                    "pPr" => in_ppr = false,
                    "r" if !in_table_cell => {
                        if in_run && !current_run.text.is_empty() {
                            current_paragraph.runs.push(std::mem::replace(
                                &mut current_run,
                                TextRun {
                                    text: String::new(),
                                    bold: false,
                                    italic: false,
                                },
                            ));
                        }
                        in_run = false;
                        in_rpr = false;
                    }
                    "rPr" => in_rpr = false,
                    "t" => in_text = false,
                    "tc" => {
                        table_row.push(cell_text.trim().to_string());
                        cell_text.clear();
                        in_table_cell = false;
                    }
                    "tr" => {
                        table_rows.push(table_row.clone());
                        table_row.clear();
                        in_table_row = false;
                    }
                    "tbl" => {
                        if !table_rows.is_empty() {
                            tables.push(table_rows.clone());
                        }
                        table_rows.clear();
                        in_table = false;
                    }
                    _ => {}
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => {
                return Err(Error::Conversion {
                    format: "powerpoint",
                    message: format!("Failed to parse slide XML: {e}"),
                });
            }
            _ => {}
        }
    }

    // Suppress unused variable warnings
    let _ = in_rpr;

    Ok(SlideContent { shapes, tables })
}

fn write_table(writer: &mut dyn Write, rows: &[Vec<String>]) -> Result<()> {
    if rows.is_empty() {
        return Ok(());
    }

    let col_count = rows.iter().map(|r| r.len()).max().unwrap_or(0);
    if col_count == 0 {
        return Ok(());
    }

    // Header
    let header = &rows[0];
    write!(writer, "|")?;
    for i in 0..col_count {
        let cell = header.get(i).map(|s| s.as_str()).unwrap_or("");
        write!(writer, " {} |", cell.replace('|', "\\|"))?;
    }
    writeln!(writer)?;

    // Separator
    write!(writer, "|")?;
    for _ in 0..col_count {
        write!(writer, "---|")?;
    }
    writeln!(writer)?;

    // Data
    for row in rows.iter().skip(1) {
        write!(writer, "|")?;
        for i in 0..col_count {
            let cell = row.get(i).map(|s| s.as_str()).unwrap_or("");
            write!(writer, " {} |", cell.replace('|', "\\|"))?;
        }
        writeln!(writer)?;
    }

    Ok(())
}

fn read_entry(archive: &mut zip::ZipArchive<Cursor<&[u8]>>, name: &str) -> Result<String> {
    let mut file = archive.by_name(name).map_err(|e| Error::Conversion {
        format: "powerpoint",
        message: format!("Entry not found: {name}: {e}"),
    })?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn local_name(name: &[u8]) -> String {
    let s = std::str::from_utf8(name).unwrap_or("");
    if let Some(pos) = s.rfind(':') {
        s[pos + 1..].to_string()
    } else {
        s.to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::converter::Converter;
    use rstest::rstest;
    use std::io::Write;

    fn make_pptx(slides: &[(&str, &str)]) -> Vec<u8> {
        let buf = Vec::new();
        let cursor = Cursor::new(buf);
        let mut zip = zip::ZipWriter::new(cursor);
        let options = zip::write::SimpleFileOptions::default()
            .compression_method(zip::CompressionMethod::Stored);
        for (name, content) in slides {
            zip.start_file(name.to_string(), options).unwrap();
            zip.write_all(content.as_bytes()).unwrap();
        }
        zip.finish().unwrap().into_inner()
    }

    fn slide_xml(body: &str) -> String {
        format!(
            r#"<?xml version="1.0" encoding="UTF-8"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
       xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <p:cSld><p:spTree>{body}</p:spTree></p:cSld>
</p:sld>"#
        )
    }

    fn title_shape(text: &str) -> String {
        format!(
            r#"<p:sp><p:nvSpPr><p:nvPr><p:ph type="title"/></p:nvPr></p:nvSpPr>
<p:txBody><a:p><a:r><a:t>{text}</a:t></a:r></a:p></p:txBody></p:sp>"#
        )
    }

    fn body_shape(text: &str) -> String {
        format!(
            r#"<p:sp><p:nvSpPr><p:nvPr><p:ph type="body"/></p:nvPr></p:nvSpPr>
<p:txBody><a:p><a:r><a:t>{text}</a:t></a:r></a:p></p:txBody></p:sp>"#
        )
    }

    fn formatted_shape(text: &str, bold: bool, italic: bool) -> String {
        let mut attrs = Vec::new();
        if bold {
            attrs.push(r#"b="1""#);
        }
        if italic {
            attrs.push(r#"i="1""#);
        }
        let rpr = if attrs.is_empty() {
            String::new()
        } else {
            format!("<a:rPr {}/>", attrs.join(" "))
        };
        format!(
            r#"<p:sp><p:nvSpPr><p:nvPr><p:ph type="body"/></p:nvPr></p:nvSpPr>
<p:txBody><a:p><a:r>{rpr}<a:t>{text}</a:t></a:r></a:p></p:txBody></p:sp>"#
        )
    }

    fn bullet_shape(items: &[&str]) -> String {
        let paras: String = items
            .iter()
            .map(|t| {
                format!(
                    r#"<a:p><a:pPr><a:buChar char="•"/></a:pPr><a:r><a:t>{t}</a:t></a:r></a:p>"#
                )
            })
            .collect();
        format!(
            r#"<p:sp><p:nvSpPr><p:nvPr><p:ph type="body"/></p:nvPr></p:nvSpPr>
<p:txBody>{paras}</p:txBody></p:sp>"#
        )
    }

    fn table_xml(rows: &[&[&str]]) -> String {
        let rows_xml: String = rows
            .iter()
            .map(|cells| {
                let cells_xml: String = cells
                    .iter()
                    .map(|c| {
                        format!(r#"<a:tc><a:txBody><a:p><a:r><a:t>{c}</a:t></a:r></a:p></a:txBody></a:tc>"#)
                    })
                    .collect();
                format!("<a:tr>{cells_xml}</a:tr>")
            })
            .collect();
        format!(
            r#"<a:graphicFrame><a:graphic><a:graphicData>
<a:tbl>{rows_xml}</a:tbl>
</a:graphicData></a:graphic></a:graphicFrame>"#
        )
    }

    fn convert(pptx_bytes: &[u8]) -> String {
        let converter = PowerPointConverter;
        let mut output = Vec::new();
        converter.convert(pptx_bytes, &mut output).unwrap();
        String::from_utf8(output).unwrap()
    }

    #[rstest]
    #[case::title("title", "# Hello")]
    #[case::plain("plain", "Some content")]
    #[case::bold("bold", "**important**")]
    #[case::italic("italic", "*emphasis*")]
    #[case::bold_italic("bold_italic", "***strong***")]
    fn test_text_formatting(#[case] kind: &str, #[case] expected: &str) {
        let shape = match kind {
            "title" => title_shape("Hello"),
            "plain" => body_shape("Some content"),
            "bold" => formatted_shape("important", true, false),
            "italic" => formatted_shape("emphasis", false, true),
            "bold_italic" => formatted_shape("strong", true, true),
            _ => unreachable!(),
        };
        let xml = slide_xml(&shape);
        let pptx = make_pptx(&[("ppt/slides/slide1.xml", &xml)]);
        let output = convert(&pptx);
        assert!(
            output.contains(expected),
            "Expected {expected:?} in:\n{output}"
        );
    }

    #[rstest]
    fn test_bullet_list() {
        let shape = bullet_shape(&["Item A", "Item B", "Item C"]);
        let xml = slide_xml(&shape);
        let pptx = make_pptx(&[("ppt/slides/slide1.xml", &xml)]);
        let output = convert(&pptx);
        assert!(output.contains("- Item A"));
        assert!(output.contains("- Item B"));
        assert!(output.contains("- Item C"));
    }

    #[rstest]
    fn test_table() {
        let tbl = table_xml(&[&["Name", "Age"], &["Alice", "30"], &["Bob", "25"]]);
        let xml = slide_xml(&tbl);
        let pptx = make_pptx(&[("ppt/slides/slide1.xml", &xml)]);
        let output = convert(&pptx);
        assert!(output.contains("| Name | Age |"), "Missing header in:\n{output}");
        assert!(output.contains("|---|"), "Missing separator in:\n{output}");
        assert!(output.contains("| Alice | 30 |"), "Missing row in:\n{output}");
        assert!(output.contains("| Bob | 25 |"), "Missing row in:\n{output}");
    }

    #[rstest]
    fn test_multiple_slides() {
        let s1 = slide_xml(&title_shape("Slide One"));
        let s2 = slide_xml(&title_shape("Slide Two"));
        let pptx = make_pptx(&[
            ("ppt/slides/slide1.xml", &s1),
            ("ppt/slides/slide2.xml", &s2),
        ]);
        let output = convert(&pptx);
        assert!(output.contains("# Slide One"));
        assert!(output.contains("---"));
        assert!(output.contains("# Slide Two"));
    }

    #[rstest]
    fn test_empty_slide() {
        let xml = slide_xml("");
        let pptx = make_pptx(&[("ppt/slides/slide1.xml", &xml)]);
        let output = convert(&pptx);
        assert!(output.contains("*Empty slide*"));
    }

    #[rstest]
    fn test_slide_ordering() {
        let s1 = slide_xml(&title_shape("First"));
        let s2 = slide_xml(&title_shape("Second"));
        let s3 = slide_xml(&title_shape("Third"));
        let pptx = make_pptx(&[
            ("ppt/slides/slide3.xml", &s3),
            ("ppt/slides/slide1.xml", &s1),
            ("ppt/slides/slide2.xml", &s2),
        ]);
        let output = convert(&pptx);
        let p1 = output.find("# First").unwrap();
        let p2 = output.find("# Second").unwrap();
        let p3 = output.find("# Third").unwrap();
        assert!(p1 < p2);
        assert!(p2 < p3);
    }

    #[rstest]
    fn test_subtitle() {
        let shapes = format!(
            "{}{}",
            title_shape("Main Title"),
            r#"<p:sp><p:nvSpPr><p:nvPr><p:ph type="subTitle"/></p:nvPr></p:nvSpPr>
<p:txBody><a:p><a:r><a:t>Sub Title</a:t></a:r></a:p></p:txBody></p:sp>"#
        );
        let xml = slide_xml(&shapes);
        let pptx = make_pptx(&[("ppt/slides/slide1.xml", &xml)]);
        let output = convert(&pptx);
        assert!(output.contains("# Main Title"));
        assert!(output.contains("## Sub Title"));
    }
}
```

## File: `src/formats/sqlite.rs`
```rust
use std::io::Write;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct SqliteConverter;

impl Converter for SqliteConverter {
    fn format_name(&self) -> &'static str {
        "sqlite"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        // Write input to a temporary file since rusqlite needs a file path
        let tmp = std::env::temp_dir().join(format!("mq-conv-{}.db", std::process::id()));
        std::fs::write(&tmp, input)?;

        let result = convert_db(&tmp, writer);

        let _ = std::fs::remove_file(&tmp);

        result
    }
}

fn convert_db(path: &std::path::Path, writer: &mut dyn Write) -> Result<()> {
    let conn = rusqlite::Connection::open_with_flags(
        path,
        rusqlite::OpenFlags::SQLITE_OPEN_READ_ONLY,
    )
    .map_err(|e| Error::Conversion {
        format: "sqlite",
        message: e.to_string(),
    })?;

    // Get all table names
    let mut stmt = conn
        .prepare("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        .map_err(|e| Error::Conversion {
            format: "sqlite",
            message: e.to_string(),
        })?;

    let tables: Vec<String> = stmt
        .query_map([], |row| row.get(0))
        .map_err(|e| Error::Conversion {
            format: "sqlite",
            message: e.to_string(),
        })?
        .filter_map(|r| r.ok())
        .collect();

    writeln!(writer, "# Database")?;
    writeln!(writer)?;
    writeln!(writer, "**Tables**: {}", tables.len())?;
    writeln!(writer)?;

    for (idx, table) in tables.iter().enumerate() {
        if idx > 0 {
            writeln!(writer)?;
        }
        writeln!(writer, "## {table}")?;
        writeln!(writer)?;

        // Get column info
        let mut col_stmt = conn
            .prepare(&format!("PRAGMA table_info(\"{}\")", table.replace('"', "\"\"")))
            .map_err(|e| Error::Conversion {
                format: "sqlite",
                message: e.to_string(),
            })?;

        let columns: Vec<(String, String, bool)> = col_stmt
            .query_map([], |row| {
                Ok((
                    row.get::<_, String>(1)?,
                    row.get::<_, String>(2)?,
                    row.get::<_, bool>(5)?,
                ))
            })
            .map_err(|e| Error::Conversion {
                format: "sqlite",
                message: e.to_string(),
            })?
            .filter_map(|r| r.ok())
            .collect();

        // Schema
        writeln!(writer, "| Column | Type | PK |")?;
        writeln!(writer, "|--------|------|----|")?;
        for (name, dtype, pk) in &columns {
            let pk_mark = if *pk { "yes" } else { "" };
            writeln!(writer, "| {name} | {dtype} | {pk_mark} |")?;
        }
        writeln!(writer)?;

        // Row count
        let count: i64 = conn
            .query_row(
                &format!("SELECT COUNT(*) FROM \"{}\"", table.replace('"', "\"\"")),
                [],
                |row| row.get(0),
            )
            .unwrap_or(0);

        writeln!(writer, "**Rows**: {count}")?;

        // Preview first 10 rows
        if count > 0 && !columns.is_empty() {
            writeln!(writer)?;

            let col_names: Vec<&str> = columns.iter().map(|(n, _, _)| n.as_str()).collect();

            // Header
            write!(writer, "|")?;
            for name in &col_names {
                write!(writer, " {name} |")?;
            }
            writeln!(writer)?;

            // Separator
            write!(writer, "|")?;
            for _ in &col_names {
                write!(writer, "---|")?;
            }
            writeln!(writer)?;

            // Data (limit to 10 rows)
            let query = format!(
                "SELECT * FROM \"{}\" LIMIT 10",
                table.replace('"', "\"\"")
            );
            let mut data_stmt = conn.prepare(&query).map_err(|e| Error::Conversion {
                format: "sqlite",
                message: e.to_string(),
            })?;

            let col_count = columns.len();
            let mut rows = data_stmt.query([]).map_err(|e| Error::Conversion {
                format: "sqlite",
                message: e.to_string(),
            })?;

            while let Some(row) = rows.next().map_err(|e| Error::Conversion {
                format: "sqlite",
                message: e.to_string(),
            })? {
                write!(writer, "|")?;
                for i in 0..col_count {
                    let val: String = row
                        .get::<_, rusqlite::types::Value>(i)
                        .map(|v| match v {
                            rusqlite::types::Value::Null => "NULL".to_string(),
                            rusqlite::types::Value::Integer(n) => n.to_string(),
                            rusqlite::types::Value::Real(f) => f.to_string(),
                            rusqlite::types::Value::Text(s) => s.replace('|', "\\|"),
                            rusqlite::types::Value::Blob(b) => format!("[BLOB {} bytes]", b.len()),
                        })
                        .unwrap_or_default();
                    write!(writer, " {val} |")?;
                }
                writeln!(writer)?;
            }

            if count > 10 {
                writeln!(writer)?;
                writeln!(writer, "*Showing 10 of {count} rows*")?;
            }
        }
    }

    Ok(())
}
```

## File: `src/formats/structured.rs`
```rust
use std::io::Write;

use crate::error::Result;

/// A format-agnostic value representation for structured data.
/// Each format converter converts its native value type into this enum,
/// then uses `write_value_as_markdown` to produce structured markdown output.
pub enum Value {
    Null,
    Bool(bool),
    Integer(i64),
    Float(f64),
    String(String),
    Array(Vec<Value>),
    /// Key-value pairs preserving insertion order.
    Object(Vec<(String, Value)>),
}

impl Value {
    fn is_primitive(&self) -> bool {
        matches!(
            self,
            Value::Null | Value::Bool(_) | Value::Integer(_) | Value::Float(_) | Value::String(_)
        )
    }

    fn display_primitive(&self) -> String {
        match self {
            Value::Null => String::new(),
            Value::Bool(b) => b.to_string(),
            Value::Integer(n) => n.to_string(),
            Value::Float(f) => f.to_string(),
            Value::String(s) => s.clone(),
            Value::Array(_) | Value::Object(_) => String::new(),
        }
    }
}

/// Write a structured value as markdown to the given writer.
pub fn write_value_as_markdown(writer: &mut dyn Write, value: &Value) -> Result<()> {
    write_value(writer, value, 1)?;
    Ok(())
}

fn write_value(writer: &mut dyn Write, value: &Value, depth: usize) -> Result<()> {
    match value {
        Value::Null => {
            writeln!(writer)?;
        }
        Value::Bool(_) | Value::Integer(_) | Value::Float(_) | Value::String(_) => {
            writeln!(writer, "{}", value.display_primitive())?;
        }
        Value::Array(items) => {
            write_array(writer, items, depth)?;
        }
        Value::Object(entries) => {
            write_object(writer, entries, depth)?;
        }
    }
    Ok(())
}

fn write_object(writer: &mut dyn Write, entries: &[(String, Value)], depth: usize) -> Result<()> {
    // Separate entries into primitive key-value pairs and complex (nested) entries.
    // Group consecutive primitives into a table.
    let mut i = 0;
    while i < entries.len() {
        if entries[i].1.is_primitive() {
            // Collect consecutive primitive entries
            let start = i;
            while i < entries.len() && entries[i].1.is_primitive() {
                i += 1;
            }
            let primitives = &entries[start..i];
            write_kv_table(writer, primitives)?;
            writeln!(writer)?;
        } else {
            let (key, val) = &entries[i];
            write_heading(writer, key, depth)?;
            write_value(writer, val, depth + 1)?;
            i += 1;
        }
    }
    Ok(())
}

fn write_array(writer: &mut dyn Write, items: &[Value], depth: usize) -> Result<()> {
    if items.is_empty() {
        writeln!(writer, "*empty*")?;
        return Ok(());
    }

    // Check if all items are objects with similar keys → render as table
    if let Some(table) = try_as_table(items) {
        write_markdown_table(writer, &table.headers, &table.rows)?;
        writeln!(writer)?;
        return Ok(());
    }

    // Check if all items are primitives → render as bullet list
    if items.iter().all(|v| v.is_primitive()) {
        for item in items {
            writeln!(writer, "- {}", item.display_primitive())?;
        }
        writeln!(writer)?;
        return Ok(());
    }

    // Mixed array: render each item
    for (idx, item) in items.iter().enumerate() {
        match item {
            v if v.is_primitive() => {
                writeln!(writer, "- {}", v.display_primitive())?;
            }
            Value::Object(entries) => {
                write_heading(writer, &format!("{}", idx + 1), depth)?;
                write_object(writer, entries, depth + 1)?;
            }
            Value::Array(inner) => {
                write_heading(writer, &format!("{}", idx + 1), depth)?;
                write_array(writer, inner, depth + 1)?;
            }
            _ => {}
        }
    }

    Ok(())
}

fn write_heading(writer: &mut dyn Write, text: &str, depth: usize) -> Result<()> {
    let level = depth.min(6);
    let hashes = "#".repeat(level);
    writeln!(writer, "{hashes} {text}")?;
    writeln!(writer)?;
    Ok(())
}

/// Write a set of primitive key-value pairs as a markdown table.
fn write_kv_table(writer: &mut dyn Write, entries: &[(String, Value)]) -> Result<()> {
    writeln!(writer, "| Key | Value |")?;
    writeln!(writer, "|---|---|")?;
    for (key, val) in entries {
        let escaped_key = escape_pipe(key);
        let escaped_val = escape_pipe(&val.display_primitive());
        writeln!(writer, "| {escaped_key} | {escaped_val} |")?;
    }
    Ok(())
}

struct TableData {
    headers: Vec<String>,
    rows: Vec<Vec<String>>,
}

/// Try to interpret an array of values as a table (array of objects with common keys).
fn try_as_table(items: &[Value]) -> Option<TableData> {
    // All items must be objects
    let objects: Vec<&Vec<(String, Value)>> = items
        .iter()
        .filter_map(|v| match v {
            Value::Object(entries) => Some(entries),
            _ => None,
        })
        .collect();

    if objects.len() != items.len() || objects.is_empty() {
        return None;
    }

    // All values in the objects must be primitives
    if !objects
        .iter()
        .all(|entries| entries.iter().all(|(_, v)| v.is_primitive()))
    {
        return None;
    }

    // Collect all unique keys preserving order from first object
    let mut headers: Vec<String> = Vec::new();
    for entries in &objects {
        for (key, _) in *entries {
            if !headers.contains(key) {
                headers.push(key.clone());
            }
        }
    }

    let rows: Vec<Vec<String>> = objects
        .iter()
        .map(|entries| {
            headers
                .iter()
                .map(|h| {
                    entries
                        .iter()
                        .find(|(k, _)| k == h)
                        .map(|(_, v)| v.display_primitive())
                        .unwrap_or_default()
                })
                .collect()
        })
        .collect();

    Some(TableData { headers, rows })
}

fn write_markdown_table(
    writer: &mut dyn Write,
    headers: &[String],
    rows: &[Vec<String>],
) -> Result<()> {
    // Header row
    write!(writer, "|")?;
    for h in headers {
        write!(writer, " {} |", escape_pipe(h))?;
    }
    writeln!(writer)?;

    // Separator row
    write!(writer, "|")?;
    for _ in headers {
        write!(writer, "---|")?;
    }
    writeln!(writer)?;

    // Data rows
    for row in rows {
        write!(writer, "|")?;
        for (i, cell) in row.iter().enumerate() {
            if i < headers.len() {
                write!(writer, " {} |", escape_pipe(cell))?;
            }
        }
        writeln!(writer)?;
    }

    Ok(())
}

fn escape_pipe(s: &str) -> String {
    s.replace('|', "\\|")
}

// --- Conversions from format-specific value types ---

#[cfg(feature = "json")]
impl From<serde_json::Value> for Value {
    fn from(v: serde_json::Value) -> Self {
        match v {
            serde_json::Value::Null => Value::Null,
            serde_json::Value::Bool(b) => Value::Bool(b),
            serde_json::Value::Number(n) => {
                if let Some(i) = n.as_i64() {
                    Value::Integer(i)
                } else {
                    Value::Float(n.as_f64().unwrap_or(0.0))
                }
            }
            serde_json::Value::String(s) => Value::String(s),
            serde_json::Value::Array(arr) => {
                Value::Array(arr.into_iter().map(Value::from).collect())
            }
            serde_json::Value::Object(map) => {
                Value::Object(map.into_iter().map(|(k, v)| (k, Value::from(v))).collect())
            }
        }
    }
}

#[cfg(feature = "toml_conv")]
impl From<toml::Value> for Value {
    fn from(v: toml::Value) -> Self {
        match v {
            toml::Value::String(s) => Value::String(s),
            toml::Value::Integer(i) => Value::Integer(i),
            toml::Value::Float(f) => Value::Float(f),
            toml::Value::Boolean(b) => Value::Bool(b),
            toml::Value::Datetime(dt) => Value::String(dt.to_string()),
            toml::Value::Array(arr) => Value::Array(arr.into_iter().map(Value::from).collect()),
            toml::Value::Table(map) => {
                Value::Object(map.into_iter().map(|(k, v)| (k, Value::from(v))).collect())
            }
        }
    }
}

#[cfg(feature = "yaml")]
impl From<serde_yaml::Value> for Value {
    fn from(v: serde_yaml::Value) -> Self {
        match v {
            serde_yaml::Value::Null => Value::Null,
            serde_yaml::Value::Bool(b) => Value::Bool(b),
            serde_yaml::Value::Number(n) => {
                if let Some(i) = n.as_i64() {
                    Value::Integer(i)
                } else {
                    Value::Float(n.as_f64().unwrap_or(0.0))
                }
            }
            serde_yaml::Value::String(s) => Value::String(s),
            serde_yaml::Value::Sequence(arr) => {
                Value::Array(arr.into_iter().map(Value::from).collect())
            }
            serde_yaml::Value::Mapping(map) => Value::Object(
                map.into_iter()
                    .map(|(k, v)| {
                        let key = match k {
                            serde_yaml::Value::String(s) => s,
                            serde_yaml::Value::Number(n) => n.to_string(),
                            serde_yaml::Value::Bool(b) => b.to_string(),
                            _ => format!("{k:?}"),
                        };
                        (key, Value::from(v))
                    })
                    .collect(),
            ),
            serde_yaml::Value::Tagged(tagged) => Value::from(tagged.value),
        }
    }
}

#[cfg(test)]
mod tests {
    use std::f64;

    use super::*;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    fn render(value: Value) -> String {
        let mut output = Vec::new();
        write_value_as_markdown(&mut output, &value).unwrap();
        String::from_utf8(output).unwrap()
    }

    #[rstest]
    #[case::null_value(Value::Null, "\n")]
    #[case::bool_true(Value::Bool(true), "true\n")]
    #[case::bool_false(Value::Bool(false), "false\n")]
    #[case::integer(Value::Integer(42), "42\n")]
    #[case::float(Value::Float(f64::consts::PI), "3.141592653589793\n")]
    #[case::string(Value::String("hello".into()), "hello\n")]
    fn test_primitive_values(#[case] value: Value, #[case] expected: &str) {
        assert_eq!(render(value), expected);
    }

    #[rstest]
    #[case::empty_array(
        Value::Array(vec![]),
        "*empty*\n"
    )]
    #[case::primitive_array(
        Value::Array(vec![
            Value::String("a".into()),
            Value::String("b".into()),
        ]),
        "- a\n- b\n\n"
    )]
    fn test_array_values(#[case] value: Value, #[case] expected: &str) {
        assert_eq!(render(value), expected);
    }

    #[rstest]
    fn test_object_with_primitives() {
        let value = Value::Object(vec![
            ("name".into(), Value::String("Alice".into())),
            ("age".into(), Value::Integer(30)),
        ]);
        let expected = "\
| Key | Value |
|---|---|
| name | Alice |
| age | 30 |

";
        assert_eq!(render(value), expected);
    }

    #[rstest]
    fn test_object_with_nested_object() {
        let value = Value::Object(vec![
            ("name".into(), Value::String("Alice".into())),
            (
                "address".into(),
                Value::Object(vec![("city".into(), Value::String("Tokyo".into()))]),
            ),
        ]);
        let output = render(value);
        assert!(output.contains("| name | Alice |"));
        assert!(output.contains("# address"));
        assert!(output.contains("| city | Tokyo |"));
    }

    #[rstest]
    fn test_array_of_objects_as_table() {
        let value = Value::Array(vec![
            Value::Object(vec![
                ("id".into(), Value::Integer(1)),
                ("name".into(), Value::String("x".into())),
            ]),
            Value::Object(vec![
                ("id".into(), Value::Integer(2)),
                ("name".into(), Value::String("y".into())),
            ]),
        ]);
        let expected = "\
| id | name |
|---|---|
| 1 | x |
| 2 | y |

";
        assert_eq!(render(value), expected);
    }

    #[rstest]
    fn test_array_of_objects_with_nested_not_table() {
        let value = Value::Array(vec![Value::Object(vec![
            ("id".into(), Value::Integer(1)),
            ("tags".into(), Value::Array(vec![Value::String("a".into())])),
        ])]);
        let output = render(value);
        assert!(!output.starts_with("| id |"));
    }

    #[rstest]
    fn test_consecutive_primitives_grouped() {
        let value = Value::Object(vec![
            ("a".into(), Value::String("1".into())),
            ("b".into(), Value::String("2".into())),
            (
                "nested".into(),
                Value::Object(vec![("x".into(), Value::String("y".into()))]),
            ),
            ("c".into(), Value::String("3".into())),
        ]);
        let output = render(value);
        assert!(output.contains("| a | 1 |"));
        assert!(output.contains("| b | 2 |"));
        assert!(output.contains("# nested"));
        assert!(output.contains("| c | 3 |"));
    }

    #[rstest]
    fn test_pipe_escape_in_keys_and_values() {
        let value = Value::Object(vec![("a|b".into(), Value::String("c|d".into()))]);
        let output = render(value);
        assert!(output.contains("a\\|b"));
        assert!(output.contains("c\\|d"));
    }

    #[rstest]
    fn test_heading_depth_caps_at_6() {
        let mut v = Value::Object(vec![("g".into(), Value::String("leaf".into()))]);
        for key in ["f", "e", "d", "c", "b", "a"] {
            v = Value::Object(vec![(key.into(), v)]);
        }
        let output = render(v);
        assert!(output.contains("###### f") || output.contains("###### g"));
        assert!(!output.contains("#######"));
    }

    #[rstest]
    fn test_mixed_array_rendering() {
        let value = Value::Array(vec![
            Value::Integer(1),
            Value::Object(vec![("key".into(), Value::String("val".into()))]),
        ]);
        let output = render(value);
        assert!(output.contains("- 1"));
        assert!(output.contains("# 2"));
        assert!(output.contains("| key | val |"));
    }
}
```

## File: `src/formats/tar.rs`
```rust
use std::io::{Cursor, Read, Write};

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct TarConverter;

impl Converter for TarConverter {
    fn format_name(&self) -> &'static str {
        "tar"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        // Try gzip first, then plain tar
        if is_gzip(input) {
            let decoder =
                flate2::read::GzDecoder::new(Cursor::new(input));
            convert_tar(decoder, writer)
        } else {
            convert_tar(Cursor::new(input), writer)
        }
    }
}

fn is_gzip(bytes: &[u8]) -> bool {
    bytes.len() >= 2 && bytes[0] == 0x1F && bytes[1] == 0x8B
}

fn convert_tar<R: Read>(reader: R, writer: &mut dyn Write) -> Result<()> {
    let mut archive = tar::Archive::new(reader);
    let entries = archive.entries().map_err(|e| Error::Conversion {
        format: "tar",
        message: e.to_string(),
    })?;

    let mut items: Vec<(String, u64, char)> = Vec::new();
    let mut total_size: u64 = 0;

    for entry in entries {
        let entry = entry.map_err(|e| Error::Conversion {
            format: "tar",
            message: e.to_string(),
        })?;

        let path = entry
            .path()
            .map(|p| p.to_string_lossy().to_string())
            .unwrap_or_else(|_| "???".to_string());

        let size = entry.size();
        let kind = match entry.header().entry_type() {
            tar::EntryType::Regular => 'f',
            tar::EntryType::Directory => 'd',
            tar::EntryType::Symlink => 'l',
            tar::EntryType::Link => 'h',
            _ => '?',
        };

        total_size += size;
        items.push((path, size, kind));
    }

    writeln!(writer, "# Archive")?;
    writeln!(writer)?;
    writeln!(writer, "**Total entries**: {}", items.len())?;
    writeln!(writer)?;

    writeln!(writer, "| # | Name | Size | Type |")?;
    writeln!(writer, "|---|------|------|------|")?;

    for (idx, (name, size, kind)) in items.iter().enumerate() {
        let type_str = match kind {
            'd' => "dir",
            'f' => "file",
            'l' => "symlink",
            'h' => "hardlink",
            _ => "other",
        };
        let size_str = if *kind == 'd' {
            "-".to_string()
        } else {
            format_size(*size)
        };
        writeln!(
            writer,
            "| {} | {name} | {size_str} | {type_str} |",
            idx + 1,
        )?;
    }

    writeln!(writer)?;
    writeln!(writer, "**Total size**: {}", format_size(total_size))?;

    Ok(())
}

fn format_size(bytes: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = 1024 * KB;
    const GB: u64 = 1024 * MB;

    if bytes >= GB {
        format!("{:.1} GB", bytes as f64 / GB as f64)
    } else if bytes >= MB {
        format!("{:.1} MB", bytes as f64 / MB as f64)
    } else if bytes >= KB {
        format!("{:.1} KB", bytes as f64 / KB as f64)
    } else {
        format!("{bytes} B")
    }
}
```

## File: `src/formats/toml_conv.rs`
```rust
use std::io::Write;

use crate::converter::Converter;
use crate::error::{Error, Result};
use crate::formats::structured;

pub struct TomlConverter;

impl Converter for TomlConverter {
    fn format_name(&self) -> &'static str {
        "toml"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let text = std::str::from_utf8(input).map_err(|e| Error::Conversion {
            format: "toml",
            message: e.to_string(),
        })?;

        let value: toml::Value = toml::from_str(text).map_err(|e| Error::Conversion {
            format: "toml",
            message: e.to_string(),
        })?;

        let structured_value = structured::Value::from(value);
        structured::write_value_as_markdown(writer, &structured_value)?;

        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::converter::Converter;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    fn convert(input: &str) -> String {
        let converter = TomlConverter;
        let mut output = Vec::new();
        converter.convert(input.as_bytes(), &mut output).unwrap();
        String::from_utf8(output).unwrap()
    }

    #[rstest]
    #[case::flat_keys(
        "name = \"test\"\nversion = \"0.1.0\"",
        "| Key | Value |\n|---|---|\n| name | test |\n| version | 0.1.0 |\n\n"
    )]
    #[case::section(
        "[package]\nname = \"app\"\nversion = \"1.0\"",
        "# package\n\n| Key | Value |\n|---|---|\n| name | app |\n| version | 1.0 |\n\n"
    )]
    #[case::nested_sections(
        "[a]\n[a.b]\nkey = \"val\"",
        "# a\n\n## b\n\n| Key | Value |\n|---|---|\n| key | val |\n\n"
    )]
    #[case::array_of_strings(
        "tags = [\"rust\", \"cli\"]",
        "# tags\n\n- rust\n- cli\n\n"
    )]
    #[case::array_of_tables(
        "[[items]]\nid = 1\nname = \"x\"\n\n[[items]]\nid = 2\nname = \"y\"",
        "# items\n\n| id | name |\n|---|---|\n| 1 | x |\n| 2 | y |\n\n"
    )]
    fn test_conversion(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    #[case::integer("val = 42")]
    #[case::float("val = 3.14")]
    #[case::boolean("val = true")]
    fn test_primitive_types(#[case] input: &str) {
        let output = convert(input);
        assert!(output.contains("| Key | Value |"));
        assert!(output.contains("| val |"));
    }

    #[rstest]
    fn test_inline_table() {
        let output = convert("dep = { version = \"1\", features = [\"full\"] }");
        assert!(output.contains("dep"));
        assert!(output.contains("version"));
    }
}
```

## File: `src/formats/video.rs`
```rust
use std::io::{Cursor, Write};

use lofty::file::TaggedFileExt;
use lofty::prelude::*;
use lofty::probe::Probe;
use lofty::tag::ItemKey;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct VideoConverter;

impl Converter for VideoConverter {
    fn format_name(&self) -> &'static str {
        "video"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let tagged_file =
            Probe::new(cursor)
                .guess_file_type()
                .map_err(|e| Error::Conversion {
                    format: "video",
                    message: e.to_string(),
                })?
                .read()
                .map_err(|e| Error::Conversion {
                    format: "video",
                    message: e.to_string(),
                })?;

        writeln!(writer, "# Video")?;
        writeln!(writer)?;

        let props = tagged_file.properties();
        writeln!(writer, "## File Info")?;
        writeln!(writer)?;
        writeln!(writer, "| Property | Value |")?;
        writeln!(writer, "|----------|-------|")?;

        writeln!(
            writer,
            "| Format | {:?} |",
            tagged_file.file_type()
        )?;
        writeln!(writer, "| Size | {} |", format_size(input.len() as u64))?;

        let duration = props.duration();
        if !duration.is_zero() {
            let total_secs = duration.as_secs();
            let hours = total_secs / 3600;
            let mins = (total_secs % 3600) / 60;
            let secs = total_secs % 60;
            if hours > 0 {
                writeln!(writer, "| Duration | {hours}:{mins:02}:{secs:02} |")?;
            } else {
                writeln!(writer, "| Duration | {mins}:{secs:02} |")?;
            }
        }

        if let Some(bitrate) = props.overall_bitrate() {
            writeln!(writer, "| Bitrate | {bitrate} kbps |")?;
        }

        if let Some(channels) = props.channels() {
            let ch_label = match channels {
                1 => "Mono",
                2 => "Stereo",
                6 => "5.1 Surround",
                8 => "7.1 Surround",
                _ => "Multi-channel",
            };
            writeln!(writer, "| Audio Channels | {channels} ({ch_label}) |")?;
        }

        if let Some(sample_rate) = props.sample_rate() {
            writeln!(writer, "| Audio Sample Rate | {sample_rate} Hz |")?;
        }

        writeln!(writer)?;

        // Tags
        if let Some(tag) = tagged_file.primary_tag().or(tagged_file.first_tag()) {
            let items: Vec<(&str, String)> = [
                ("Title", tag.get_string(ItemKey::TrackTitle)),
                ("Artist", tag.get_string(ItemKey::TrackArtist)),
                ("Album", tag.get_string(ItemKey::AlbumTitle)),
                ("Year", tag.get_string(ItemKey::Year)),
                ("Genre", tag.get_string(ItemKey::Genre)),
                ("Comment", tag.get_string(ItemKey::Comment)),
            ]
            .into_iter()
            .filter_map(|(k, v)| v.map(|v| (k, v.to_string())))
            .collect();

            if !items.is_empty() {
                writeln!(writer, "## Tags")?;
                writeln!(writer)?;
                writeln!(writer, "| Tag | Value |")?;
                writeln!(writer, "|-----|-------|")?;
                for (key, value) in &items {
                    writeln!(writer, "| {key} | {} |", value.replace('|', "\\|"))?;
                }
            }
        }

        Ok(())
    }
}

fn format_size(bytes: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = 1024 * KB;
    const GB: u64 = 1024 * MB;

    if bytes >= GB {
        format!("{:.1} GB", bytes as f64 / GB as f64)
    } else if bytes >= MB {
        format!("{:.1} MB", bytes as f64 / MB as f64)
    } else if bytes >= KB {
        format!("{:.1} KB", bytes as f64 / KB as f64)
    } else {
        format!("{bytes} B")
    }
}
```

## File: `src/formats/word.rs`
```rust
use std::io::{Cursor, Read, Write};

use quick_xml::Reader;
use quick_xml::events::Event;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct WordConverter;

impl Converter for WordConverter {
    fn format_name(&self) -> &'static str {
        "word"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let mut archive = zip::ZipArchive::new(cursor).map_err(|e| Error::Conversion {
            format: "word",
            message: e.to_string(),
        })?;

        let document_xml = read_entry(&mut archive, "word/document.xml")?;
        let paragraphs = parse_document(&document_xml)?;

        let mut first = true;
        for para in &paragraphs {
            match para {
                Paragraph::Heading(level, text) => {
                    if !first {
                        writeln!(writer)?;
                    }
                    let hashes = "#".repeat(*level as usize);
                    writeln!(writer, "{hashes} {text}")?;
                }
                Paragraph::Text(text) => {
                    if !text.is_empty() {
                        if !first {
                            writeln!(writer)?;
                        }
                        writeln!(writer, "{text}")?;
                    }
                }
                Paragraph::ListItem(text) => {
                    writeln!(writer, "- {text}")?;
                }
                Paragraph::BlockQuote(text) => {
                    if !first {
                        writeln!(writer)?;
                    }
                    writeln!(writer, "> {text}")?;
                }
                Paragraph::Table(rows) => {
                    if !first {
                        writeln!(writer)?;
                    }
                    write_table(writer, rows)?;
                }
            }
            first = false;
        }

        Ok(())
    }
}

enum Paragraph {
    Heading(u8, String),
    Text(String),
    ListItem(String),
    BlockQuote(String),
    Table(Vec<Vec<String>>),
}

fn parse_document(xml: &str) -> Result<Vec<Paragraph>> {
    let mut paragraphs = Vec::new();
    let mut reader = Reader::from_str(xml);

    let mut in_paragraph = false;
    let mut in_run = false;
    let mut in_table = false;
    let mut in_table_row = false;
    let mut in_table_cell = false;
    let mut current_text = String::new();
    let mut current_style: Option<String> = None;
    let mut is_bold = false;
    let mut is_italic = false;
    let mut is_list_item = false;
    let mut table_rows: Vec<Vec<String>> = Vec::new();
    let mut table_row: Vec<String> = Vec::new();
    let mut cell_text = String::new();

    loop {
        match reader.read_event() {
            Ok(Event::Start(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "p" => {
                        in_paragraph = true;
                        current_text.clear();
                        current_style = None;
                        is_bold = false;
                        is_italic = false;
                        is_list_item = false;
                    }
                    "r" => in_run = true,
                    "tbl" => {
                        in_table = true;
                        table_rows.clear();
                    }
                    "tr" => {
                        in_table_row = true;
                        table_row.clear();
                    }
                    "tc" => {
                        in_table_cell = true;
                        cell_text.clear();
                    }
                    _ => {}
                }
            }
            Ok(Event::Empty(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "pStyle" => {
                        for attr in e.attributes().flatten() {
                            if attr.key.as_ref() == b"w:val" || attr.key.as_ref() == b"val" {
                                current_style = Some(
                                    String::from_utf8_lossy(&attr.value).to_string(),
                                );
                            }
                        }
                    }
                    "b" => is_bold = true,
                    "i" => is_italic = true,
                    "numPr" | "ilvl" => is_list_item = true,
                    _ => {}
                }
            }
            Ok(Event::Text(e)) => {
                if in_run || in_table_cell {
                    let text = e.decode().unwrap_or_default().to_string();
                    if in_table_cell {
                        cell_text.push_str(&text);
                    } else if in_paragraph {
                        let formatted = format_run_text(&text, is_bold, is_italic);
                        current_text.push_str(&formatted);
                    }
                }
            }
            Ok(Event::End(e)) => {
                let local = local_name(e.name().as_ref());
                match local.as_str() {
                    "p" => {
                        if in_table_cell {
                            if !cell_text.is_empty() {
                                // cell text accumulated separately
                            }
                        } else if in_paragraph {
                            let para = if let Some(ref style) = current_style {
                                if let Some(level) = heading_level(style) {
                                    Paragraph::Heading(level, current_text.clone())
                                } else if is_blockquote(style) {
                                    Paragraph::BlockQuote(current_text.clone())
                                } else if is_list_item {
                                    Paragraph::ListItem(current_text.clone())
                                } else {
                                    Paragraph::Text(current_text.clone())
                                }
                            } else if is_list_item {
                                Paragraph::ListItem(current_text.clone())
                            } else {
                                Paragraph::Text(current_text.clone())
                            };
                            paragraphs.push(para);
                        }
                        in_paragraph = false;
                    }
                    "r" => {
                        in_run = false;
                        is_bold = false;
                        is_italic = false;
                    }
                    "tc" => {
                        table_row.push(cell_text.trim().to_string());
                        cell_text.clear();
                        in_table_cell = false;
                    }
                    "tr" => {
                        table_rows.push(table_row.clone());
                        table_row.clear();
                        in_table_row = false;
                    }
                    "tbl" => {
                        if !table_rows.is_empty() {
                            paragraphs.push(Paragraph::Table(table_rows.clone()));
                        }
                        table_rows.clear();
                        in_table = false;
                    }
                    _ => {}
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => {
                return Err(Error::Conversion {
                    format: "word",
                    message: format!("Failed to parse document.xml: {e}"),
                });
            }
            _ => {}
        }
    }

    // Suppress unused variable warnings
    let _ = in_table;
    let _ = in_table_row;

    Ok(paragraphs)
}

fn write_table(writer: &mut dyn Write, rows: &[Vec<String>]) -> Result<()> {
    if rows.is_empty() {
        return Ok(());
    }

    let col_count = rows.iter().map(|r| r.len()).max().unwrap_or(0);
    if col_count == 0 {
        return Ok(());
    }

    // Header
    let header = &rows[0];
    write!(writer, "|")?;
    for i in 0..col_count {
        let cell = header.get(i).map(|s| s.as_str()).unwrap_or("");
        write!(writer, " {} |", cell.replace('|', "\\|"))?;
    }
    writeln!(writer)?;

    // Separator
    write!(writer, "|")?;
    for _ in 0..col_count {
        write!(writer, "---|")?;
    }
    writeln!(writer)?;

    // Data
    for row in rows.iter().skip(1) {
        write!(writer, "|")?;
        for i in 0..col_count {
            let cell = row.get(i).map(|s| s.as_str()).unwrap_or("");
            write!(writer, " {} |", cell.replace('|', "\\|"))?;
        }
        writeln!(writer)?;
    }

    Ok(())
}

fn format_run_text(text: &str, bold: bool, italic: bool) -> String {
    if text.is_empty() {
        return String::new();
    }
    match (bold, italic) {
        (true, true) => format!("***{text}***"),
        (true, false) => format!("**{text}**"),
        (false, true) => format!("*{text}*"),
        (false, false) => text.to_string(),
    }
}

fn is_blockquote(style: &str) -> bool {
    let lower = style.to_ascii_lowercase();
    lower == "quote" || lower == "intensequote" || lower == "blockquote"
}

fn heading_level(style: &str) -> Option<u8> {
    let lower = style.to_ascii_lowercase();
    if let Some(rest) = lower.strip_prefix("heading") {
        rest.trim()
            .parse::<u8>()
            .ok()
            .filter(|&n| (1..=6).contains(&n))
    } else if let Some(rest) = lower.strip_prefix("titre") {
        rest.trim()
            .parse::<u8>()
            .ok()
            .filter(|&n| (1..=6).contains(&n))
    } else {
        None
    }
}

fn read_entry(archive: &mut zip::ZipArchive<Cursor<&[u8]>>, name: &str) -> Result<String> {
    let mut file = archive.by_name(name).map_err(|e| Error::Conversion {
        format: "word",
        message: format!("Entry not found: {name}: {e}"),
    })?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

fn local_name(name: &[u8]) -> String {
    let s = std::str::from_utf8(name).unwrap_or("");
    if let Some(pos) = s.rfind(':') {
        s[pos + 1..].to_string()
    } else {
        s.to_string()
    }
}
```

## File: `src/formats/xml.rs`
```rust
use std::io::Write;

use quick_xml::Reader;
use quick_xml::events::Event;

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct XmlConverter;

impl Converter for XmlConverter {
    fn format_name(&self) -> &'static str {
        "xml"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let text = std::str::from_utf8(input).map_err(|e| Error::Conversion {
            format: "xml",
            message: e.to_string(),
        })?;

        let root = parse_xml(text)?;
        write_element(writer, &root, 1)?;

        Ok(())
    }
}

struct XmlElement {
    name: String,
    attributes: Vec<(String, String)>,
    children: Vec<XmlNode>,
}

enum XmlNode {
    Element(XmlElement),
    Text(String),
}

fn parse_xml(text: &str) -> Result<XmlElement> {
    let mut reader = Reader::from_str(text);
    let mut stack: Vec<XmlElement> = Vec::new();
    let mut root: Option<XmlElement> = None;

    loop {
        match reader.read_event() {
            Ok(Event::Start(e)) => {
                let name = local_name(e.name().as_ref());
                let attributes: Vec<(String, String)> = e
                    .attributes()
                    .flatten()
                    .map(|a| {
                        (
                            String::from_utf8_lossy(a.key.as_ref()).to_string(),
                            String::from_utf8_lossy(&a.value).to_string(),
                        )
                    })
                    .collect();
                stack.push(XmlElement {
                    name,
                    attributes,
                    children: Vec::new(),
                });
            }
            Ok(Event::Empty(e)) => {
                let name = local_name(e.name().as_ref());
                let attributes: Vec<(String, String)> = e
                    .attributes()
                    .flatten()
                    .map(|a| {
                        (
                            String::from_utf8_lossy(a.key.as_ref()).to_string(),
                            String::from_utf8_lossy(&a.value).to_string(),
                        )
                    })
                    .collect();
                let elem = XmlElement {
                    name,
                    attributes,
                    children: Vec::new(),
                };
                if let Some(parent) = stack.last_mut() {
                    parent.children.push(XmlNode::Element(elem));
                } else {
                    root = Some(elem);
                }
            }
            Ok(Event::Text(e)) => {
                let text = e.decode().unwrap_or_default().trim().to_string();
                if !text.is_empty()
                    && let Some(parent) = stack.last_mut() {
                        parent.children.push(XmlNode::Text(text));
                    }
            }
            Ok(Event::CData(e)) => {
                let text = String::from_utf8_lossy(e.as_ref()).trim().to_string();
                if !text.is_empty()
                    && let Some(parent) = stack.last_mut() {
                        parent.children.push(XmlNode::Text(text));
                    }
            }
            Ok(Event::End(_)) => {
                if let Some(elem) = stack.pop() {
                    if let Some(parent) = stack.last_mut() {
                        parent.children.push(XmlNode::Element(elem));
                    } else {
                        root = Some(elem);
                    }
                }
            }
            Ok(Event::Eof) => break,
            Err(e) => {
                return Err(Error::Conversion {
                    format: "xml",
                    message: format!("Invalid XML: {e}"),
                });
            }
            _ => {}
        }
    }

    root.ok_or_else(|| Error::Conversion {
        format: "xml",
        message: "Empty XML document".into(),
    })
}

fn write_element(writer: &mut dyn Write, elem: &XmlElement, depth: usize) -> Result<()> {
    let level = depth.min(6);
    let hashes = "#".repeat(level);
    writeln!(writer, "{hashes} {}", elem.name)?;
    writeln!(writer)?;

    // Write attributes as a table
    if !elem.attributes.is_empty() {
        writeln!(writer, "| Attribute | Value |")?;
        writeln!(writer, "|---|---|")?;
        for (key, val) in &elem.attributes {
            writeln!(writer, "| {} | {} |", escape_pipe(key), escape_pipe(val))?;
        }
        writeln!(writer)?;
    }

    // Separate text nodes and element children
    let mut text_parts: Vec<&str> = Vec::new();
    let mut child_elements: Vec<&XmlElement> = Vec::new();

    for child in &elem.children {
        match child {
            XmlNode::Text(t) => text_parts.push(t),
            XmlNode::Element(e) => child_elements.push(e),
        }
    }

    // Write text content
    if !text_parts.is_empty() {
        for text in &text_parts {
            writeln!(writer, "{text}")?;
        }
        writeln!(writer)?;
    }

    // Try to group repeated same-name child elements into a table
    if !child_elements.is_empty() {
        let mut i = 0;
        while i < child_elements.len() {
            // Find a run of same-named elements
            let name = &child_elements[i].name;
            let mut end = i + 1;
            while end < child_elements.len() && child_elements[end].name == *name {
                end += 1;
            }

            if end - i > 1 && can_table_elements(&child_elements[i..end]) {
                write_elements_as_table(writer, &child_elements[i..end], depth)?;
                i = end;
            } else {
                // Write each element as a subsection
                while i < end {
                    write_element(writer, child_elements[i], depth + 1)?;
                    i += 1;
                }
            }
        }
    }

    Ok(())
}

/// Check if a group of same-named elements can be represented as a table.
/// They must all have only attributes and/or a single text child, no nested elements.
fn can_table_elements(elements: &[&XmlElement]) -> bool {
    elements.iter().all(|e| {
        let has_child_elements = e
            .children
            .iter()
            .any(|c| matches!(c, XmlNode::Element(_)));
        !has_child_elements
    })
}

fn write_elements_as_table(
    writer: &mut dyn Write,
    elements: &[&XmlElement],
    depth: usize,
) -> Result<()> {
    let level = (depth + 1).min(6);
    let hashes = "#".repeat(level);
    writeln!(writer, "{hashes} {}", elements[0].name)?;
    writeln!(writer)?;

    // Collect all attribute names + "text" column if any have text
    let mut headers: Vec<String> = Vec::new();
    let mut has_text = false;

    for elem in elements {
        for (key, _) in &elem.attributes {
            if !headers.contains(key) {
                headers.push(key.clone());
            }
        }
        let text: String = elem
            .children
            .iter()
            .filter_map(|c| match c {
                XmlNode::Text(t) => Some(t.as_str()),
                _ => None,
            })
            .collect::<Vec<_>>()
            .join(" ");
        if !text.is_empty() {
            has_text = true;
        }
    }

    if has_text {
        headers.push("text".to_string());
    }

    if headers.is_empty() {
        return Ok(());
    }

    // Header row
    write!(writer, "|")?;
    for h in &headers {
        write!(writer, " {} |", escape_pipe(h))?;
    }
    writeln!(writer)?;

    // Separator
    write!(writer, "|")?;
    for _ in &headers {
        write!(writer, "---|")?;
    }
    writeln!(writer)?;

    // Data rows
    for elem in elements {
        write!(writer, "|")?;
        for h in &headers {
            let val = if h == "text" {
                elem.children
                    .iter()
                    .filter_map(|c| match c {
                        XmlNode::Text(t) => Some(t.as_str()),
                        _ => None,
                    })
                    .collect::<Vec<_>>()
                    .join(" ")
            } else {
                elem.attributes
                    .iter()
                    .find(|(k, _)| k == h)
                    .map(|(_, v)| v.clone())
                    .unwrap_or_default()
            };
            write!(writer, " {} |", escape_pipe(&val))?;
        }
        writeln!(writer)?;
    }
    writeln!(writer)?;

    Ok(())
}

fn escape_pipe(s: &str) -> String {
    s.replace('|', "\\|")
}

fn local_name(name: &[u8]) -> String {
    let s = std::str::from_utf8(name).unwrap_or("");
    if let Some(pos) = s.rfind(':') {
        s[pos + 1..].to_string()
    } else {
        s.to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::converter::Converter;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    fn convert(input: &str) -> String {
        let converter = XmlConverter;
        let mut output = Vec::new();
        converter.convert(input.as_bytes(), &mut output).unwrap();
        String::from_utf8(output).unwrap()
    }

    #[rstest]
    #[case::simple_element(
        "<root>hello</root>",
        "# root\n\nhello\n\n"
    )]
    #[case::element_with_attributes(
        r#"<item id="1" name="test"/>"#,
        "# item\n\n| Attribute | Value |\n|---|---|\n| id | 1 |\n| name | test |\n\n"
    )]
    #[case::nested_elements(
        "<root><child>text</child></root>",
        "# root\n\n## child\n\ntext\n\n"
    )]
    #[case::attributes_and_text(
        r#"<book lang="en">Rust Guide</book>"#,
        "# book\n\n| Attribute | Value |\n|---|---|\n| lang | en |\n\nRust Guide\n\n"
    )]
    fn test_basic(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    #[case::repeated_elements_as_table(
        r#"<list><item id="1">A</item><item id="2">B</item></list>"#,
        "# list\n\n## item\n\n| id | text |\n|---|---|\n| 1 | A |\n| 2 | B |\n\n"
    )]
    #[case::repeated_empty_elements_as_table(
        r#"<data><row x="1" y="2"/><row x="3" y="4"/></data>"#,
        "# data\n\n## row\n\n| x | y |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n\n"
    )]
    fn test_table_grouping(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    fn test_deep_nesting() {
        let output = convert("<a><b><c><d>deep</d></c></b></a>");
        assert!(output.contains("# a"));
        assert!(output.contains("## b"));
        assert!(output.contains("### c"));
        assert!(output.contains("#### d"));
        assert!(output.contains("deep"));
    }

    #[rstest]
    fn test_pipe_escape() {
        let output = convert(r#"<item val="a|b"/>"#);
        assert!(output.contains("a\\|b"));
    }

    #[rstest]
    fn test_empty_xml_error() {
        let converter = XmlConverter;
        let mut output = Vec::new();
        let result = converter.convert(b"", &mut output);
        assert!(result.is_err());
    }

    #[rstest]
    fn test_mixed_children() {
        let output = convert(r#"<root><a>text</a><b x="1"/><b x="2"/></root>"#);
        assert!(output.contains("## a"));
        assert!(output.contains("text"));
        assert!(output.contains("## b"));
        assert!(output.contains("| x |"));
    }
}
```

## File: `src/formats/yaml.rs`
```rust
use std::io::Write;

use crate::converter::Converter;
use crate::error::{Error, Result};
use crate::formats::structured;

pub struct YamlConverter;

impl Converter for YamlConverter {
    fn format_name(&self) -> &'static str {
        "yaml"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let value: serde_yaml::Value =
            serde_yaml::from_slice(input).map_err(|e| Error::Conversion {
                format: "yaml",
                message: e.to_string(),
            })?;

        let structured_value = structured::Value::from(value);
        structured::write_value_as_markdown(writer, &structured_value)?;

        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::converter::Converter;
    use pretty_assertions::assert_eq;
    use rstest::rstest;

    fn convert(input: &str) -> String {
        let converter = YamlConverter;
        let mut output = Vec::new();
        converter.convert(input.as_bytes(), &mut output).unwrap();
        String::from_utf8(output).unwrap()
    }

    #[rstest]
    #[case::flat_mapping(
        "name: Alice\nage: 30",
        "| Key | Value |\n|---|---|\n| name | Alice |\n| age | 30 |\n\n"
    )]
    #[case::nested_mapping(
        "user:\n  name: Bob\n  city: Tokyo",
        "# user\n\n| Key | Value |\n|---|---|\n| name | Bob |\n| city | Tokyo |\n\n"
    )]
    #[case::sequence_of_scalars(
        "items:\n  - apple\n  - banana",
        "# items\n\n- apple\n- banana\n\n"
    )]
    #[case::sequence_of_mappings(
        "users:\n  - name: A\n    id: 1\n  - name: B\n    id: 2",
        "# users\n\n| name | id |\n|---|---|\n| A | 1 |\n| B | 2 |\n\n"
    )]
    fn test_conversion(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    #[case::top_level_sequence("- a\n- b\n- c", "- a\n- b\n- c\n\n")]
    #[case::scalar_string("hello", "hello\n")]
    #[case::scalar_integer("42", "42\n")]
    #[case::null_value(
        "key: null",
        "| Key | Value |\n|---|---|\n| key |  |\n\n"
    )]
    fn test_edge_cases(#[case] input: &str, #[case] expected: &str) {
        assert_eq!(convert(input), expected);
    }

    #[rstest]
    fn test_non_string_keys() {
        let output = convert("true: yes\nfalse: no");
        assert!(output.contains("true"));
        assert!(output.contains("false"));
    }
}
```

## File: `src/formats/zip.rs`
```rust
use std::io::{Cursor, Write};

use crate::converter::Converter;
use crate::error::{Error, Result};

pub struct ZipConverter;

impl Converter for ZipConverter {
    fn format_name(&self) -> &'static str {
        "zip"
    }

    fn convert(&self, input: &[u8], writer: &mut dyn Write) -> Result<()> {
        let cursor = Cursor::new(input);
        let mut archive = zip::ZipArchive::new(cursor).map_err(|e| Error::Conversion {
            format: "zip",
            message: e.to_string(),
        })?;

        let mut total_uncompressed: u64 = 0;
        let mut total_compressed: u64 = 0;
        let count = archive.len();

        writeln!(writer, "# Archive")?;
        writeln!(writer)?;
        writeln!(writer, "**Total entries**: {count}")?;
        writeln!(writer)?;

        writeln!(
            writer,
            "| # | Name | Size | Compressed | Method |"
        )?;
        writeln!(
            writer,
            "|---|------|------|------------|--------|"
        )?;

        for i in 0..count {
            let entry = archive.by_index(i).map_err(|e| Error::Conversion {
                format: "zip",
                message: e.to_string(),
            })?;

            let name = entry.name().to_string();
            let size = entry.size();
            let compressed = entry.compressed_size();
            let method = format!("{:?}", entry.compression());

            total_uncompressed += size;
            total_compressed += compressed;

            let (size_str, compressed_str) = if entry.is_dir() {
                ("-".to_string(), "-".to_string())
            } else {
                (format_size(size), format_size(compressed))
            };

            writeln!(
                writer,
                "| {idx} | {name} | {size_str} | {compressed_str} | {method} |",
                idx = i + 1,
            )?;
        }

        writeln!(writer)?;
        let ratio = if total_uncompressed > 0 {
            format!(
                "{:.1}%",
                (1.0 - total_compressed as f64 / total_uncompressed as f64) * 100.0
            )
        } else {
            "N/A".to_string()
        };
        writeln!(
            writer,
            "**Total size**: {} (compressed: {}, ratio: {ratio})",
            format_size(total_uncompressed),
            format_size(total_compressed),
        )?;

        Ok(())
    }
}

fn format_size(bytes: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = 1024 * KB;
    const GB: u64 = 1024 * MB;

    if bytes >= GB {
        format!("{:.1} GB", bytes as f64 / GB as f64)
    } else if bytes >= MB {
        format!("{:.1} MB", bytes as f64 / MB as f64)
    } else if bytes >= KB {
        format!("{:.1} KB", bytes as f64 / KB as f64)
    } else {
        format!("{bytes} B")
    }
}
```

