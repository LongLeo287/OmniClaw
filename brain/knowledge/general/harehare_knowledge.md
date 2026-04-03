---
id: harehare-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:50.787544
---

# KNOWLEDGE EXTRACT: harehare
> **Extracted on:** 2026-03-30 17:38:04
> **Source:** harehare

---

## File: `mq-conv.md`
```markdown
# 📦 harehare/mq-conv [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-conv
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 1 | **Forks:** 🍴 0
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A CLI tool for converting various file formats to Markdown

## README (trích đầu)
```
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
| TOML   | `.toml`    
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-docs.md`
```markdown
# 📦 harehare/mq-docs [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-docs
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A documentation generator for mq functions, macros, and selectors. 

## README (trích đầu)
```
<h1 align="center">mq-docs</h1>

A documentation generator for [mq](https://github.com/harehare/mq) functions, macros, and selectors. Generates reference documentation from built-in definitions or custom `.mq` files in multiple output formats.

![mq-docs](./assets/mq-docs.jpg)

## Features

- Generates documentation for functions, macros, and selectors
- Multiple output formats: Markdown, plain text, and HTML
- HTML output includes interactive sidebar navigation, search/filter, and responsive design
- Supports built-in modules, custom files, and loadable modules (e.g., `csv`, `json`)
- Available as both a CLI tool and a library

## Installation

### Using the Installation Script (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/harehare/mq-docs/main/bin/install.sh | bash
```

The installer will:
- Download the latest release for your platform
- Verify the binary with SHA256 checksum
- Install to `~/.mq-check/bin/`
- Update your shell profile (bash, zsh, or fish)

After installation, restart your terminal or run:
```bash
source ~/.bashrc  # or ~/.zshrc, or ~/.config/fish/config.fish
```

### Cargo

```bash
# Install from crates.io
cargo install mq-docs
# Install using binstall
cargo binstall mq-docs@0.1.0
```

### From Source

```bash
git clone https://github.com/harehare/mq-docs.git
cd mq-docs
cargo build --release
# Binary will be at target/release/mq-docs
```

## Usage

### CLI

```bash
# Generate documentation for built-in functions (default: Markdown)
mq-docs

# Generate from custom files
mq-docs file1.mq file2.mq

# Load specific modules
mq-docs -M csv -M json

# Include built-in functions alongside custom modules/files
mq-docs -B -M json file.mq

# Specify output format
mq-docs -F html > docs.html
mq-docs -F markdown > docs.md
mq-docs -F text
```

#### Options

| Option                      | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| `[FILES]`                   | Input `.mq` files to generate documentation from                   |
| `-M, --module-names <NAME>` | Module names to load (repeatable)                                  |
| `-F, --format <FORMAT>`     | Output format: `markdown`, `text`, or `html` (default: `markdown`) |
| `-B, --include-builtin`     | Include built-in functions alongside modules/files                 |

### Library

```rust
use mq_docs::{generate_docs, DocFormat};

fn main() -> miette::Result<()> {
    // Generate Markdown documentation for built-in functions
    let docs = generate_docs(&None, &None, &DocFormat::Markdown, false)?;
    println!("{docs}");
    Ok(())
}
```

## Output Formats

- **Markdown** - Tables suitable for rendering in documentation sites or GitHub
- **Text** - Plain text output for terminal viewing
- **HTML** - Self-contained single-page HTML with dark theme, sidebar navigation, search filtering, and mobile support

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-edit.md`
```markdown
# 📦 harehare/mq-edit [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-edit
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-18
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A terminal-based Markdown and code editor with WYSIWYG rendering and LSP support.

## README (trích đầu)
```
<h1 align="center">mq-edit</h1>

A terminal-based Markdown and code editor with WYSIWYG rendering and LSP support.

![demo](assets/demo.gif)

## Overview

`mq-edit` is a Rust-based TUI (Text User Interface) editor that provides:
- **Markdown WYSIWYG**: The line under the cursor displays source, other lines show rich formatted text
- **LSP Integration**: Full Language Server Protocol support for code intelligence
- **Multi-language support**: Rust, Python, MQ (Markdown Query Language), and more

Built on top of the `mq-markdown` parser with full LSP capabilities.

### Using the Installation Script (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/harehare/mq-edit/main/bin/install.sh | bash
```

The installer will:
- Download the latest release for your platform
- Verify the binary with SHA256 checksum
- Install to `~/.mq-edit/bin/`
- Update your shell profile (bash, zsh, or fish)

After installation, restart your terminal or run:

```bash
source ~/.bashrc  # or ~/.zshrc, or ~/.config/fish/config.fish
```

### Cargo

```bash
# Install from crates.io
cargo install mq-edit
# Install using binstall
cargo binstall mq-edit@0.1.0
```

### From Source

```bash
git clone https://github.com/harehare/mq-edit.git
cd mq-edit
cargo build --release
# Binary will be at target/release/mq-edit
```

## Usage

```bash
# Open a Markdown file
mq-edit README.md

# Open a Rust file (with LSP support)
mq-edit src/main.rs

# Open an MQ file (Markdown Query Language)
mq-edit query.mq

# Create a new file (empty buffer)
mq-edit

# Initialize default configuration file
mq-edit --init-config

# Show help
mq-edit --help
```

### Keyboard Shortcuts

| Key              | Action                                      |
| ---------------- | ------------------------------------------- |
| `Ctrl+S`         | Save file (opens save dialog for new files) |
| `Ctrl+Q` / `Esc` | Quit                                        |
| `Alt+B` / `F2`   | Toggle file browser                         |
| `Ctrl+Space`     | Code completion (LSP)                       |
| `Ctrl+D`         | Go to definition (LSP)                      |
| `Ctrl+B`         | Navigate back                               |
| `Ctrl+F`         | Navigate forward                            |
| `Ctrl+G`         | Go to line                                  |
| `Ctrl+E`         | Execute mq query                            |
| `F3`             | Search                                      |
| `F4`             | Find and replace                            |
| `Up/Down`        | Move cursor / Select completion             |
| `Enter`          | Apply completion                            |

## Pipe Mode

`mq-edit` supports pipe mode, allowing you to read from stdin and write to stdout. This is useful for combining with [mq](https://github.com/harehare/mq) and other command-line tools. In pipe mode, pressing `Esc` exits immediately without a save confirmation dialog — the edited content is written to stdout on exit.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-go.md`
```markdown
# 📦 harehare/mq-go [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-go


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-14
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Go bindings for mq — a jq-like query language for Markdown processing.

## README (trích đầu)
```
<h1 align="center">mq-go</h1>

Go bindings for [mq](https://github.com/harehare/mq) — a jq-like query language for Markdown processing.

This package wraps the `mq-ffi` C library using cgo, providing a safe, idiomatic Go API for querying and transforming Markdown, MDX, HTML, and plain text content.

## Requirements

- Go 1.21+
- `mq-ffi` C library installed on your system

## Installation

```bash
go get github.com/harehare/mq-go
```

## Usage

### Basic query

```go
engine, err := mq.New()
if err != nil {
    log.Fatal(err)
}
defer engine.Close()

result, err := engine.Run(".h1", "# Hello World\n\nSome text")
if err != nil {
    log.Fatal(err)
}
fmt.Println(result.Text()) // "# Hello World"
```

### Query with specific input format

```go
// Plain text (split by lines)
result, err := engine.RunWithFormat(`select(contains("foo"))`, "foo\nbar\nbaz", mq.FormatText)

// MDX content
result, err := engine.RunWithFormat("select(is_mdx())", "# Title\n\n<Component />", mq.FormatMDX)

// HTML content (auto-converted to Markdown)
result, err := engine.RunWithFormat(`select(contains("Hello"))`, "<h1>Hello</h1>", mq.FormatHTML)
```

### HTML to Markdown conversion

```go
markdown, err := mq.HTMLToMarkdown("<h1>Hello</h1><p>World</p>")

// With options
markdown, err := mq.HTMLToMarkdownWithOptions(html, mq.ConversionOptions{
    UseTitleAsH1:               true,
    GenerateFrontMatter:        true,
    ExtractScriptsAsCodeBlocks: true,
})
```

### Working with results

```go
result, err := engine.Run(".h2", content)

result.Text()         // all values joined by newline
result.Values()       // []string of non-empty values
result.Len()          // total number of values
result.Get(0)         // value at index
```

## Input Formats

| Constant | Description |
|---|---|
| `FormatMarkdown` | Standard Markdown (CommonMark/GFM) — default |
| `FormatMDX` | Markdown with JSX support |
| `FormatText` | Plain text, split by lines |
| `FormatHTML` | HTML, auto-converted to Markdown |

## Query Examples

```
.h1                          # extract H1 headings
.h2                          # extract H2 headings
.code                        # extract code blocks
.[]                          # iterate over all nodes
.h2 | select(contains("x"))  # filter by content
```

## License

[MIT](LICENSE)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-java.md`
```markdown
# 📦 harehare/mq-java [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-java
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Java | **License:** MIT
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Java bindings for mq — a jq-like command-line tool for Markdown processing.

## README (trích đầu)
```
<h1 align="center">mq-java</h1>

Java bindings for [mq](https://github.com/harehare/mq) — a jq-like command-line tool for Markdown processing.

## Requirements

- Java 11+
- Maven
- Rust toolchain (for building the native library)

## Setup

Clone and build the native library, then compile the Java bindings:

```bash
make build
```

Or step by step:

```bash
make setup       # Clone the mq repository
make build-rust  # Build the mq-ffi native library
mvn compile      # Compile the Java sources
```

## Running Tests

```bash
make test
```

## Usage

### Basic Query

```java
try (Mq mq = new Mq()) {
    MqResult result = mq.run(".h1", "# Hello World\n\nSome text");
    System.out.println(result.text()); // "# Hello World"
}
```

### Input Formats

```java
try (Mq mq = new Mq()) {
    // Markdown (default)
    MqResult md = mq.run(".h2", content, InputFormat.MARKDOWN);

    // MDX
    MqResult mdx = mq.run("select(is_mdx())", content, InputFormat.MDX);

    // HTML (auto-converted to Markdown)
    MqResult html = mq.run(".h1", "<h1>Title</h1>", InputFormat.HTML);

    // Plain text (split by lines)
    MqResult text = mq.run("select(contains(\"foo\"))", content, InputFormat.TEXT);
}
```

### HTML to Markdown Conversion

```java
String markdown = Mq.htmlToMarkdown("<h1>Hello</h1><p>World</p>");
```

With options:

```java
ConversionOptions options = new ConversionOptions();
options.useTitleAsH1 = true;
options.generateFrontMatter = true;
options.extractScriptsAsCodeBlocks = true;

String markdown = Mq.htmlToMarkdown(html, options);
```

### Working with Results

```java
MqResult result = mq.run(".h2", content);

// Get all values joined by newline
String text = result.text();

// Get as a list
List<String> values = result.values();

// Access by index
String first = result.get(0);

// Iterate
for (String value : result) {
    System.out.println(value);
}
```

## API

### `Mq`

| Method | Description |
|---|---|
| `run(String code, String content)` | Run a query on Markdown content |
| `run(String code, String content, InputFormat format)` | Run a query with a specified input format |
| `static htmlToMarkdown(String html)` | Convert HTML to Markdown |
| `static htmlToMarkdown(String html, ConversionOptions options)` | Convert HTML to Markdown with options |
| `close()` | Release native resources (`AutoCloseable`) |

### `InputFormat`

| Value | Description |
|---|---|
| `MARKDOWN` | CommonMark / GFM (default) |
| `MDX` | Markdown with JSX |
| `HTML` | HTML (auto-converted to Markdown) |
| `TEXT` | Plain text, split by lines |
| `RAW` | Raw input, no parsing |

### `ConversionOptions`

| Field | Type | Description |
|---|---|---|
| `extractScriptsAsCodeBlocks` | `boolean` | Extract `<script>` tags as code blocks |
| `generateFrontMatter` | `boolean` | Generate front matter from HTML `<head>` metadata |
| `useTitleAsH1` | `boolean` | Use `<title>` as an H1 heading |

## License

[MIT](LICENSE)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-mcp.md`
```markdown
# 📦 harehare/mq-mcp [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-mcp
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 0
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Model Context Protocol (MCP) server implementation for mq. 

## README (trích đầu)
```
<h1 align="center">mq-mcp</h1>

[![ci](https://github.com/harehare/mq-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq-mcp/actions/workflows/ci.yml)
[![mq language](https://img.shields.io/badge/mq-language-orange.svg)](https://github.com/harehare/mq)


Model Context Protocol (MCP) server implementation for [mq](https://github.com/harehare/mq). This crate provides an MCP server that allows AI assistants to process Markdown and HTML content using mq's query language.

## Installation

You can install mq-mcp using the installation script:

```bash
curl -fsSL https://raw.githubusercontent.com/harehare/mq-mcp/main/bin/install.sh | bash
```

Or clone this repository and run the install script:

```bash
git clone https://github.com/harehare/mq-mcp.git
cd mq-mcp
./bin/install.sh
```

The script will:
- Install the `mq` binary to `~/.mq/bin`
- Add `~/.mq/bin` to your PATH (if not already present)
- Support macOS, Linux, and Windows
- Verify checksums for security

After installation, restart your terminal or run:

```bash
source ~/.zshrc  # or ~/.bashrc for bash users
```

## Implementation

The server implements four MCP tools:

- `html_to_markdown`: Converts HTML to Markdown and executes mq queries
- `extract_markdown`: Executes mq queries on Markdown content
- `available_functions`: Returns available functions for mq queries
- `available_selectors`: Returns available selectors for mq queries

### Tool Parameters

#### html_to_markdown

- `html` (string): HTML content to process
- `query` (optional string): mq query to execute

#### extract_markdown

- `markdown` (string): Markdown content to process
- `query` (string): mq query to execute

#### available_functions

No parameters. Returns JSON with function names, descriptions, parameters, and example queries.

#### available_selectors

No parameters. Returns JSON with selector names, descriptions, and parameters.

## Configuration

### Claude Desktop

#### Using mq-mcp binary directly

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "/Users/YOUR_USERNAME/.mq/bin/mq-mcp",
      "args": []
    }
  }
}
```

Or simply use `mq-mcp` if `~/.mq/bin` is in your PATH:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "mq-mcp",
      "args": []
    }
  }
}
```

#### Using mq command

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "/Users/YOUR_USERNAME/.mq/bin/mq",
      "args": ["mcp"]
    }
  }
}
```

Or simply use `mq` if `~/.mq/bin` is in your PATH:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "mq",
      "args": ["mcp"]
    }
  }
}
```

### VS Code with MCP Extension

#### Using mq-mcp binary directly

Add to `.vscode/settings.json`:

```json
{
  "mcp": {
    "servers": {
      "mq-mcp": {
        "type": "stdio",
        "command": "mq-mcp",
        "args": []
      }
    }
  }
}
```
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-python.md`
```markdown
# 📦 harehare/mq-python [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-python
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 1 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Python bindings for mq, a jq-like command-line tool for processing Markdown.

## README (trích đầu)
```
<h1 align="center">mq-python</h1>

[![PyPI](https://img.shields.io/pypi/v/markdown-query.svg)](https://pypi.org/project/markdown-query/)

Python bindings for the mq Markdown processor.

## Installation

```bash
pip install markdown-query
```

## Usage

### Basic Usage

Use the `run` function to process Markdown with mq queries:

```python
import mq

# Extract all level 1 headings
result = mq.run(".h1", "# Hello World\n\n## Heading2\n\nText")
print(result.values)  # ['# Hello World']

# Extract all level 2 headings
result = mq.run(".h2", "# Main Title\n\n## Section A\n\n## Section B")
print(result.values)  # ['## Section A', '## Section B']

# Get all results as a single string
print(result.text)  # '## Section A\n## Section B'
```

### Filtering and Transforming

Use mq query syntax to filter and transform Markdown:

```python
import mq

markdown = """
# Product

## Features
Great features here.

## Installation
Install instructions.
"""

# Filter headings containing specific text
result = mq.run('.h2 | select(contains("Feature"))', markdown)
print(result.values)  # ['## Features']

# Extract list items
result = mq.run(".[]", "# List\n\n- Item 1\n- Item 2\n- Item 3")
print(result.values)  # ['- Item 1', '- Item 2', '- Item 3']

# Extract code blocks
result = mq.run(".code", "# Code\n\n```python\nprint('Hello')\n```")
print(result.values)  # ["```python\nprint('Hello')\n```"]
```

### Input Formats

mq supports multiple input formats:

```python
import mq

# Markdown (default)
options = mq.Options()
options.input_format = mq.InputFormat.MARKDOWN
result = mq.run(".h1", "# Heading", options)

# MDX (Markdown with JSX)
options = mq.Options()
options.input_format = mq.InputFormat.MDX
result = mq.run("select(is_mdx())", "# MDX\n\n<Component />", options)
print(result.values)  # ['<Component />']

# HTML
options = mq.Options()
options.input_format = mq.InputFormat.HTML
result = mq.run('select(contains("Hello"))', "<h1>Hello</h1><p>World</p>", options)
print(result.values)  # ['# Hello']

# Plain text
options = mq.Options()
options.input_format = mq.InputFormat.TEXT
result = mq.run('select(contains("2"))', "Line 1\nLine 2\nLine 3", options)
print(result.values)  # ['Line 2']
```

Available input formats:
- `InputFormat.MARKDOWN` - Standard Markdown (default)
- `InputFormat.MDX` - Markdown with JSX
- `InputFormat.HTML` - HTML content
- `InputFormat.TEXT` - Plain text
- `InputFormat.RAW` - Raw string input
- `InputFormat.NULL` - Null input

### Rendering Options

Customize the output rendering:

```python
import mq

options = mq.Options()
options.input_format = mq.InputFormat.MARKDOWN
options.list_style = mq.ListStyle.PLUS        # Use '+' for list items
options.link_title_style = mq.TitleSurroundStyle.SINGLE  # Use single quotes for link titles
options.link_url_style = mq.UrlSurroundStyle.ANGLE       # Use angle brackets for URLs

result = mq.run(".", markdown, options)
```

Available options:
- `ListStyle`: `DASH` (default), `PLUS`, `STAR`
- `TitleSurrou
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-ruby.md`
```markdown
# 📦 harehare/mq-ruby [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-ruby
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Ruby bindings for mq, a jq-like command-line tool for processing Markdown.

## README (trích đầu)
```
<h1 align="center">mq-ruby</h1>

[![Gem Version](https://badge.fury.io/rb/mq-ruby.svg)](https://badge.fury.io/rb/mq-ruby)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ruby bindings for [mq](https://mqlang.org/), a jq-like command-line tool for processing Markdown.

## Ruby API

Once complete, the Ruby API will look like this:

```ruby
require 'mq'

# Basic usage
markdown = <<~MD
  # Main Title
  ## Section 1
  Some content here.
  ## Section 2
  More content.
MD

result = MQ.run('.h2', markdown)
result.values.each do |heading|
  puts heading
end
# => ## Section 1
# => ## Section 2

# With options
options = MQ::Options.new
options.input_format = MQ::InputFormat::HTML

result = MQ.run('.h1', '<h1>Hello</h1><p>World</p>', options)
puts result.text  # => # Hello

# HTML to Markdown conversion
html = '<h1>Title</h1><p>Paragraph</p>'
markdown = MQ.html_to_markdown(html)
puts markdown  # => # Title\n\nParagraph
```

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Links

- [mq Website](https://mqlang.org/)
- [GitHub Repository](https://github.com/harehare/mq)
- [Command-line Tool](https://github.com/harehare/mq#installation)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-task.md`
```markdown
# 📦 harehare/mq-task [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-task
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 2
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
mq-task is a task runner that executes code blocks in Markdown files based on section titles. 

## README (trích đầu)
```
<h1 align="center">mq-task</h1>

[![ci](https://github.com/harehare/mq-task/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq-task/actions/workflows/ci.yml)

`mq-task` is a task runner that executes code blocks in Markdown files based on section titles.
It is implemented using [mq](https://github.com/harehare/mq), a jq-like command-line tool for Markdown processing, to parse and extract sections from Markdown documents.

![demo](assets/demo.gif)

> [!WARNING]
> `mq-task` is currently under active development.

## Features

- Execute code blocks from specific sections in Markdown files
- Configurable runtimes for different programming languages
- Support for custom heading levels
- TOML-based configuration
- Built on top of the mq query language

## Installation

### Quick Install

```bash
curl -sSL https://raw.githubusercontent.com/harehare/mq-task/refs/heads/main/bin/install.sh | bash
```

The installer will:
- Download the latest mq binary for your platform
- Install it to `~/.mq/bin/`
- Update your shell profile to add mq to your PATH

### Cargo

```sh
$ cargo install --git https://github.com/harehare/mq-task.git
```

## Usage

### Run a task (shorthand)

```bash
# Run from README.md (default)
mq-task "Task Name"

# Run from a specific file
mq-task -f tasks.md "Task Name"
```

### Run a task (explicit)

```bash
mq-task run "Task Name"
mq-task run --file tasks.md "Task Name"
```

### Pass arguments to a task

You can pass arguments to your task using `--` separator:

```bash
# Pass arguments to a task
mq-task "Task Name" -- arg1 arg2 arg3

# With explicit run command
mq-task run "Task Name" -- arg1 arg2 arg3

# From a specific file
mq-task -f tasks.md "Task Name" -- arg1 arg2
```

Arguments are accessible via environment variables:
- `MX_ARGS`: All arguments joined by space (e.g., "arg1 arg2 arg3")
- `MX_ARG_0`, `MX_ARG_1`, ...: Individual arguments

Example in a Markdown task:

````markdown
## My Task

```bash
echo "All args: $MX_ARGS"
echo "First arg: $MX_ARG_0"
echo "Second arg: $MX_ARG_1"
```
````

### List available tasks

```bash
# List tasks from README.md (default)
mq-task

# List tasks from a specific file
mq-task -f tasks.md
mq-task list --file tasks.md
```

### Initialize configuration

```bash
mq-task init
```

This creates an `mq-task.toml` file with default runtime settings.

## Configuration

Create an `mq-task.toml` file to customize runtime behavior:

```toml
# Runtimes configuration
# Simple format: language = "command"
# The execution mode defaults to "stdin"
[runtimes]
bash = "bash"
sh = "sh"
python = "python3"
ruby = "ruby"
node = "node"
javascript = "node"
js = "node"
php = "php"
perl = "perl"
jq = "jq"

# Detailed format with execution mode
# Execution modes: "stdin" (default), "file", or "arg"
# - stdin: Pass code via standard input
# - file: Write code to a temporary file and pass it as an argument
# - arg: Pass code as a command-line argument

[runtimes.go]
command = "go run"
execution_mode = "file"  
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-update.md`
```markdown
# 📦 harehare/mq-update [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-update
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
mq-update is a utility to update the mq binary to the latest version from GitHub releases. 

## README (trích đầu)
```
<h1 align="center"><code>mq-update</code></h1>

Updater for `mq` and `mq` subcommands (`mq-check`, `mq-conv`, etc.).

![demo](assets/demo.gif)

## Overview

`mq-update` is a utility to update the `mq` binary and its subcommands (e.g., `mq-check`, `mq-conv`, `mq-docs`) to the latest version from GitHub releases.

## Installation

### Using the install script (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/harehare/mq-update/main/scripts/install.sh | bash
```

### From source with Cargo

```bash
cargo install --git https://github.com/harehare/mq-update.git
```

## Usage

### Update mq to the latest version

```bash
mq-update
```

### Update a subcommand

```bash
# Update mq-check to the latest version
mq-update check

# Update mq-conv to the latest version
mq-update conv
```

### Update to a specific version

```bash
mq-update --target v0.5.12
# or
mq-update --target 0.5.12

# Subcommand with a specific version
mq-update check --target v0.1.0
```

### Show current version

```bash
mq-update --current

# Subcommand version
mq-update check --current
```

### Force reinstall

```bash
mq-update --force
```

## Options

- `[SUBCOMMAND]`: Subcommand name to update (e.g., `check` for `mq-check`)
- `-t, --target <VERSION>`: Target version to install (defaults to latest)
- `-f, --force`: Force reinstall even if already up-to-date
- `--current`: Show current version
- `-h, --help`: Print help
- `-V, --version`: Print version

## How it works

1. Locates the binary (`mq` or `mq-{subcommand}`) via `which`
2. Checks the current version
3. Fetches the latest release information from GitHub (`harehare/mq` or `harehare/mq-{subcommand}`)
4. Downloads the appropriate binary for your platform
5. Creates a backup of the existing binary
6. Replaces the existing binary with the new one

## Supported Platforms

- **Linux** (glibc)
  - x86_64
  - aarch64
- **Linux** (musl) - Alpine Linux, etc.
  - x86_64
  - aarch64
- **macOS**
  - x86_64 (Intel)
  - aarch64 (Apple Silicon)
- **Windows**
  - x86_64

## License

MIT License - see [LICENSE](LICENSE) for details.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq-view.md`
```markdown
# 📦 harehare/mq-view [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq-view
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 3 | **Forks:** 🍴 0
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A library and CLI tool for rendering Markdown documents with syntax highlighting and rich text formatting.

## README (trích đầu)
```
<h1 align="center">mq-view</h1>

[![ci](https://github.com/harehare/mq-view/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq-view/actions/workflows/ci.yml)

A library and CLI tool for rendering Markdown documents with syntax highlighting and rich text formatting.
Built with [mq](https://github.com/harehare/mq) - jq-like command-line tool for markdown processing.

![demo](assets/demo.gif)

## Features

- 🎨 **Syntax Highlighting**: Tree-sitter powered syntax highlighting for 13+ programming languages
- 📝 **Rich Markdown Rendering**: Support for headers, lists, code blocks, links, images, and more
- 🔔 **GitHub-style Callouts**: NOTE, TIP, IMPORTANT, WARNING, CAUTION
- 🔗 **Clickable Links**: Terminal hyperlinks using OSC 8

## Installation

### Quick Install

```bash
curl -sSL https://raw.githubusercontent.com/harehare/mq-view/refs/heads/main/bin/install.sh | bash
```

The installer will:
- Download the latest mq-view binary for your platform
- Install it to `~/.mq/bin/`
- Update your shell profile to add mq-view to your PATH

### Cargo

From crates.io (stable):

```sh
cargo install mq-view
```

From git (latest):

```sh
cargo install --git https://github.com/harehare/mq-view.git
```

## Supported Languages

- Rust, JavaScript, TypeScript (+ TSX)
- Python, Go, Java
- C, C++
- HTML, CSS, JSON
- Bash/Shell

## Usage

### As a CLI Tool

View a markdown file:

```bash
mq-view README.md
```

Pipe markdown content:

```bash
echo "# Hello\n\n\`\`\`rust\nfn main() {}\n\`\`\`" | mq-view
```

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq.md`
```markdown
# 📦 harehare/mq [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 369 | **Forks:** 🍴 7
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A jq-like Markdown query language for command-line processing

## README (trích đầu)
```
<div align="center">
  <img src="assets/logo.svg" style="width: 128px; height: 128px;"/>
</div>

<div align="center">
  <a href="https://mqlang.org">Visit the site 🌐</a>
  &mdash;
  <a href="https://mqlang.org/book">Read the book 📖</a>
  &mdash;
  <a href="https://mqlang.org/playground">Playground 🎮</a>
</div>

<h1 align="center">mq</h1>

[![ci](https://github.com/harehare/mq/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/harehare/mq/graph/badge.svg?token=E4UD7Q9NC3)](https://codecov.io/gh/harehare/mq)
[![CodSpeed Badge](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json?style=for-the-badge)](https://codspeed.io/harehare/mq)
[![audit](https://github.com/harehare/mq/actions/workflows/audit.yml/badge.svg)](https://github.com/harehare/mq/actions/workflows/audit.yml)
[![GitHub Release](https://img.shields.io/github/v/release/harehare/mq)](https://github.com/harehare/mq/releases)
[![Crates.io](https://img.shields.io/crates/v/mq-lang)](https://crates.io/crates/mq-lang)
[![npm](https://img.shields.io/npm/v/mq-web)](https://www.npmjs.com/package/mq-web)

mq is a command-line tool that processes Markdown using a syntax similar to jq.
It's written in Rust, allowing you to easily slice, filter, map, and transform structured data.

![demo](assets/demo.gif)

> [!IMPORTANT]
> This project is under active development.

## Why mq?

mq makes working with Markdown files as easy as jq makes working with JSON. It's especially useful for:

- **LLM Workflows**: Efficiently manipulate and process Markdown used in LLM prompts and outputs
- **LLM Input Generation**: Generate structured Markdown content optimized for LLM consumption, since Markdown serves as the primary input format for most language models
- **Documentation Management**: Extract, transform, and organize content across multiple documentation files
- **Content Analysis**: Quickly extract specific sections or patterns from Markdown documents
- **Batch Processing**: Apply consistent transformations across multiple Markdown files

Since LLM inputs are primarily in Markdown format, mq provides efficient tools for generating and processing the structured Markdown content that LLMs require.

## Features

- **Slice and Filter**: Extract specific parts of your Markdown documents with ease.
- **Map and Transform**: Apply transformations to your Markdown content.
- **Command-line Interface**: Simple and intuitive CLI for quick operations.
- **Extensibility**: Easily extendable with custom functions.
- **Built-in support**: Filter and transform content with many built-in functions and selectors.
- **REPL Support**: Interactive command-line REPL for testing and experimenting.
- **IDE Support**: VSCode Extension and Language Server **Protocol** (LSP) support for custom function development.
- **Debugger**: Includes an experimental debugger (`mq-dbg`) for inspecting and stepping through mq queries interactively.
- **External
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mq_elixir.md`
```markdown
# 📦 harehare/mq_elixir [🔖 PENDING/APPROVE]
🔗 https://github.com/harehare/mq_elixir
🌐 https://mqlang.org

## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Elixir | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Elixir bindings for mq, a jq-like command-line tool for processing Markdown.

## README (trích đầu)
```
# mq_elixir

Elixir bindings for [mq](https://mqlang.org/), a jq-like command-line tool for Markdown processing.

## Features

- Process markdown, MDX, HTML, and plain text
- Full mq query language support
- Multiple input and output format options
- Configurable rendering options
- Fast Rust-powered NIF implementation

## Installation

Add `mq` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:mq_elixir, "~> 0.1.0"}
  ]
end
```


## Usage

### Basic Query

```elixir
# Extract all H1 headings
{:ok, result} = Mq.run(".h1", "# Hello\n## World")
IO.inspect(result.values)  # ["# Hello"]
```

### Working with Results

```elixir
{:ok, result} = Mq.run(".h", "# H1\n## H2\n### H3")

# Access values
result.values  # ["# H1", "## H2", "### H3"]
result.text    # "# H1\n## H2\n### H3"

# Enumerate
Enum.each(result, fn heading -> IO.puts(heading) end)
```

## Documentation

Full documentation is available on [HexDocs](https://hexdocs.pm/mq_elixir).

For mq query language syntax, see the [official mq documentation](https://mqlang.org/).

## License

MIT License

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

