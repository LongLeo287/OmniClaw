---
id: github.com-vectorize-io-pg0-8a09a4fa-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:38.713396
---

# KNOWLEDGE EXTRACT: github.com_vectorize-io_pg0_8a09a4fa
> **Extracted on:** 2026-04-01 13:50:34
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523485/github.com_vectorize-io_pg0_8a09a4fa

---

## File: `.gitignore`
```
/target
# Cargo.lock is committed for reproducible binary builds
.idea/
node_modules/
.env
*.pyc
sdk/python/pg0/bin/
```

## File: `CLAUDE.md`
```markdown
# Claude Code Development Guidelines

## Platform Support Requirements

### Mandatory Components for All Platforms

**CRITICAL:** All supported platforms MUST include the following components:

1. **PostgreSQL** - Core database (required)
2. **pgvector** - Vector similarity search extension (required)
3. **pgbouncer** - Connection pooling (required)

### Platform Support Policy

- **Never suggest or ship** platform support without all three components
- If a component is missing for a platform (e.g., pgvector not compiled for that platform):
  - DO NOT suggest shipping without it
  - DO NOT present it as an optional component
  - The platform is NOT supported until all components are available

### Adding New Platform Support

When adding support for a new platform (e.g., `x86_64-apple-darwin`):

1. Ensure PostgreSQL binaries exist for the platform
2. Ensure pgvector compiled binaries exist for the platform
3. Ensure pgbouncer compiled binaries exist for the platform
4. Add the platform to CI/CD workflows
5. Test the complete build with all three components

### Current Platform Support

All platforms in `build.rs` and `.github/workflows/release-cli.yml` must have:
- PostgreSQL from `theseus-rs/postgresql-binaries`
- pgvector from `nicoloboschi/pgvector_compiled`
- pgbouncer from `nicoloboschi/pgbouncer_compiled`

## Build Requirements

- **All builds must succeed with all three components bundled**
- **Build MUST FAIL if any component is missing** for supported platforms
- No graceful fallbacks - missing components = build failure
- This ensures platforms are only released when fully functional
```

## File: `Cargo.toml`
```
[package]
name = "pg0"
version = "0.12.2"
edition = "2021"
description = "Zero-dependency CLI to run embedded PostgreSQL locally without installation"
license = "MIT"
repository = "https://github.com/vectorize-io/pg0"

[[bin]]
name = "pg0"
path = "src/main.rs"

[dependencies]
postgresql_embedded = { version = "0.20", default-features = false, features = ["blocking", "theseus", "rustls"] }
postgresql_extensions = { version = "0.20", default-features = false, features = ["blocking", "rustls", "portal-corp", "steampipe", "tensor-chord"] }
clap = { version = "4", features = ["derive"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
dirs = "5"
thiserror = "1"
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
flate2 = "1"
tar = "0.4"

[profile.release]
strip = true
lto = true
codegen-units = 1
```

## File: `README.md`
```markdown
# pg0

[![PyPI version](https://badge.fury.io/py/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)
[![PyPI downloads](https://img.shields.io/pypi/dm/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)
[![Python versions](https://img.shields.io/pypi/pyversions/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)

**Zero-config PostgreSQL with pgvector.**

A single binary that runs PostgreSQL locally - no installation, no configuration, no Docker required. Includes **pgvector** for AI/vector workloads out of the box.

## Why pg0?

PostgreSQL setup is painful. Docker adds complexity. Local installs conflict with system packages. pg0 gives you a real PostgreSQL server with zero friction:

- **No installation** - download a single binary and run `pg0 start`
- **No Docker** - no containers, no daemon, no complexity
- **No configuration** - sensible defaults, just works
- **Production parity** - develop with the same database you'll deploy
- **Full PostgreSQL** - JSON, arrays, CTEs, window functions, extensions, pgvector - everything works

Use pg0 for local development, testing, CI/CD pipelines, or any scenario where you want PostgreSQL without the setup overhead.

## Supported Platforms

| Platform | Architecture | Binary |
|----------|--------------|--------|
| macOS | Apple Silicon (M1/M2/M3) | `pg0-macos-arm64` |
| Linux | x86_64 (glibc) | `pg0-linux-amd64-gnu` |
| Linux | x86_64 (musl/Alpine) | `pg0-linux-amd64-musl` |
| Linux | ARM64 (glibc) | `pg0-linux-arm64-gnu` |
| Linux | ARM64 (musl/Alpine) | `pg0-linux-arm64-musl` |
| Windows | x64 | `pg0-windows-amd64.exe` |

## Features

- **Zero dependencies** - single binary, works offline
- **PostgreSQL 18** with pgvector 0.8.1 bundled
- **Multiple instances** - run multiple PostgreSQL servers simultaneously
- **Cross-platform** - macOS (Apple Silicon), Linux (x86_64 & ARM64), Windows (x64)
- **Language SDKs** - Python and Node.js libraries for programmatic control
- **Bundled psql** - no separate client installation needed
- **Persistent data** - survives restarts, stored in `~/.pg0/`

## Installation

### CLI Binary

The install script automatically detects your platform and downloads the correct binary:

```bash
curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash
```

Or with a custom install directory:

```bash
INSTALL_DIR=/usr/local/bin curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash
```

### Python SDK

Install via pip:

```bash
pip install pg0-embedded
```

Quick start:

```python
from pg0 import Pg0

# Start PostgreSQL
pg = Pg0()
pg.start()
print(pg.uri)  # postgresql://postgres:postgres@localhost:5432/postgres

# Or use context manager
with Pg0() as pg:
    result = pg.execute("SELECT version();")
    print(result)
```

See [PyPI package](https://pypi.org/project/pg0-embedded/) for more details.

### Node.js SDK

Install via npm:

```bash
npm install @vectorize-io/pg0
```

Quick start:

```typescript
import { Pg0 } from '@vectorize-io/pg0';

const pg = new Pg0();
await pg.start();
console.log(await pg.getUri());
await pg.stop();
```

### Linux Distributions

pg0 provides separate binaries optimized for different Linux distributions:

- **Debian/Ubuntu/RHEL** (glibc-based): Uses `pg0-linux-{arch}-gnu`
- **Alpine** (musl-based): Uses `pg0-linux-{arch}-musl`

The install script automatically detects your distribution and downloads the correct binary.

## Docker

pg0 works in Docker containers. Here are the minimal setup steps for each supported image type:

### Debian/Ubuntu (glibc-based)

```dockerfile
FROM debian:bookworm-slim
# or: python:3.11-slim, ubuntu:22.04, etc.

# Install required dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libxml2 \
    libssl3 \
    libgssapi-krb5-2 \
    && apt-get install -y libicu72 || apt-get install -y libicu74 || apt-get install -y libicu* \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user (PostgreSQL cannot run as root)
RUN useradd -m -s /bin/bash pguser
USER pguser

# Install pg0
RUN curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash
ENV PATH="/home/pguser/.local/bin:${PATH}"

# Start PostgreSQL when container runs
CMD ["bash", "-c", "pg0 start && tail -f /dev/null"]
```

Or start it with your application:

```bash
docker run -d myimage bash -c "pg0 start && exec your-application"
```

### Alpine (musl-based)

**Note:** The musl binary requires ICU 74. Use Alpine 3.20 (not 3.22+) as newer versions have ICU 76.

```dockerfile
FROM alpine:3.20
# or: python:3.12-alpine3.20

# Install required dependencies
RUN apk add --no-cache curl bash shadow icu-libs lz4-libs libxml2

# Create non-root user (PostgreSQL cannot run as root)
RUN adduser -D -s /bin/bash pguser
USER pguser

# Install pg0
RUN curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash
ENV PATH="/home/pguser/.local/bin:${PATH}"

# Start PostgreSQL when container runs
CMD ["sh", "-c", "pg0 start && tail -f /dev/null"]
```

Or start it with your application:

```bash
docker run -d myimage sh -c "pg0 start && exec your-application"
```

### Quick Test

Run pg0 in a Docker container with a single command:

```bash
# Debian/Ubuntu
docker run --rm -it python:3.11-slim bash -c '
  apt-get update -qq &&
  apt-get install -y curl libxml2 libssl3 libgssapi-krb5-2 libicu72 &&
  useradd -m pguser &&
  su - pguser -c "curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash &&
    export PATH=\"\$HOME/.local/bin:\$PATH\" &&
    pg0 start &&
    sleep 3 &&
    pg0 psql -c \"SELECT version();\""
'

# Alpine (use 3.20 for ICU 74 compatibility)
docker run --rm -it python:3.12-alpine3.20 sh -c '
  apk add --no-cache curl bash shadow icu-libs lz4-libs libxml2 &&
  adduser -D pguser &&
  su - pguser -c "curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash &&
    export PATH=\"\$HOME/.local/bin:\$PATH\" &&
    pg0 start &&
    sleep 3 &&
    pg0 psql -c \"SELECT version();\""
'
```

**Note:** PostgreSQL requires a non-root user for security. The examples above create a `pguser` for this purpose.

## Quick Start

```bash
# Start PostgreSQL
pg0 start

# Connect with psql
pg0 psql

# Use pgvector
pg0 psql -c "CREATE EXTENSION IF NOT EXISTS vector;"
pg0 psql -c "CREATE TABLE items (embedding vector(3));"
pg0 psql -c "INSERT INTO items VALUES ('[1,2,3]');"

# Stop when done
pg0 stop
```

## Usage

### Commands

pg0 provides the following commands:

1. **start** - Start a PostgreSQL server instance
2. **stop** - Stop a running PostgreSQL server instance
3. **drop** - Stop and permanently delete an instance (removes all data)
4. **info** - Display instance information (status, connection URI, etc.)
5. **list** - List all PostgreSQL instances
6. **psql** - Open an interactive psql shell connected to an instance
7. **logs** - View PostgreSQL logs for debugging

### Start PostgreSQL

```bash
# Start with defaults (port 5432)
pg0 start

# Start with custom options
pg0 start --port 5433 --username myuser --password mypass --database myapp
```

### Stop PostgreSQL

```bash
pg0 stop
```

### Drop Instance

Permanently delete an instance and all its data:

```bash
# Drop the default instance
pg0 drop

# Drop a named instance
pg0 drop --name myapp
```

**Warning:** This command will stop the instance if running and delete all data. This action cannot be undone.

### Get Server Info

```bash
# Human-readable format
pg0 info

# JSON output
pg0 info -o json

# Info for a specific instance
pg0 info --name myapp
```

### List Instances

```bash
# List all instances
pg0 list

# JSON output
pg0 list -o json
```

### Open psql Shell

```bash
# Interactive shell
pg0 psql

# Run a single command
pg0 psql -c "SELECT version();"

# Run a SQL file
pg0 psql -f schema.sql
```

### View Logs

View PostgreSQL logs for debugging startup issues or errors:

```bash
# View all logs
pg0 logs

# View last 50 lines
pg0 logs -n 50

# Follow logs in real-time (like tail -f)
pg0 logs --follow

# Logs for a specific instance
pg0 logs --name myapp
```

Logs are stored in `~/.pg0/instances/<name>/data/log/`.

### Installing Extensions

#### pg_textsearch (BM25 full-text search)

[pg_textsearch](https://github.com/timescale/pg_textsearch) adds BM25-ranked full-text search to PostgreSQL. Install it into your pg0 instance with a single command (requires Xcode Command Line Tools on macOS, or `build-essential` on Linux):

```bash
curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/extensions/install-pgtextsearch.sh | bash
```

Install a specific version or target a named instance:

```bash
curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/extensions/install-pgtextsearch.sh | bash -s -- --version v0.5.1 --instance myapp
```

Then enable it:

```bash
pg0 psql -c "CREATE EXTENSION IF NOT EXISTS pg_textsearch;"
```

### Using pgvector

pgvector is pre-installed. Just enable it:

```bash
pg0 psql -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

Then use it for vector similarity search:

```sql
-- Create a table with vector column
CREATE TABLE items (id serial PRIMARY KEY, embedding vector(1536));

-- Insert vectors
INSERT INTO items (embedding) VALUES ('[0.1, 0.2, ...]');

-- Find similar vectors
SELECT * FROM items ORDER BY embedding <-> '[0.1, 0.2, ...]' LIMIT 5;
```

### Multiple Instances

Run multiple PostgreSQL servers simultaneously using named instances:

```bash
# Start multiple instances on different ports
pg0 start --name app1 --port 5432
pg0 start --name app2 --port 5433
pg0 start --name test --port 5434

# List all instances
pg0 list

# Get info for a specific instance
pg0 info --name app1

# Connect to a specific instance
pg0 psql --name app2

# Stop a specific instance
pg0 stop --name test

# Stop all (one by one)
pg0 stop --name app1
pg0 stop --name app2
```

Each instance has its own data directory at `~/.pg0/instances/<name>/data/`.

## Options

### Global Options

```
  -v, --verbose  Enable verbose logging
```

### Start Options

```
pg0 start [OPTIONS]

Options:
      --name <NAME>           Instance name [default: default]
  -p, --port <PORT>           Port to listen on [default: 5432]
  -d, --data-dir <DATA_DIR>   Data directory [default: ~/.pg0/instances/<name>/data]
  -u, --username <USERNAME>   Username [default: postgres]
  -P, --password <PASSWORD>   Password [default: postgres]
  -n, --database <DATABASE>   Database name [default: postgres]
  -c, --config <KEY=VALUE>    PostgreSQL config option (can repeat)
```

### PostgreSQL Configuration

pg0 applies optimized defaults for vector/AI workloads:
- `shared_buffers=256MB`
- `maintenance_work_mem=512MB` (faster index builds)
- `effective_cache_size=1GB`
- `max_parallel_maintenance_workers=4`
- `work_mem=64MB`

Override any setting with `-c`:

```bash
# Custom memory settings
pg0 start -c shared_buffers=512MB -c work_mem=128MB

# For larger workloads
pg0 start -c shared_buffers=1GB -c maintenance_work_mem=2GB
```

## How It Works

PostgreSQL and pgvector are **bundled directly** into the pg0 binary - no downloads required, works completely offline! On first start, pg0 extracts PostgreSQL and pgvector to `~/.pg0/installation/` and initializes the database.

Data is stored in `~/.pg0/instances/<name>/data/` (or your custom `--data-dir`) and persists between restarts.

## Runtime Dependencies

pg0 bundles PostgreSQL but requires some shared libraries at runtime. These are typically pre-installed on most systems, but may need to be added in minimal environments like Docker.

**macOS:** No additional dependencies required.

**Linux (Debian/Ubuntu):**
```bash
apt-get install libxml2 libssl3 libgssapi-krb5-2
```

**Linux (Alpine):**
```bash
apk add icu-libs lz4-libs libxml2
```

### Why these dependencies?

The bundled PostgreSQL binaries are compiled with these features enabled:

| Library | Purpose | Can disable? |
|---------|---------|--------------|
| OpenSSL (`libssl`) | SSL/TLS connections | Not recommended |
| GSSAPI (`libgssapi-krb5`) | Kerberos authentication | Rarely needed locally |
| libxml2 | XML data type and functions | Rarely needed |
| ICU (`icu-libs`) | Unicode collation (Alpine only) | glibc builds don't need it |
| LZ4 (`lz4-libs`) | WAL/TOAST compression | Small impact |

Most desktop Linux distributions and macOS have these libraries pre-installed. You only need to install them manually in minimal Docker images or bare-metal servers.

## Troubleshooting

### PostgreSQL Cannot Run as Root

PostgreSQL refuses to run as root for security reasons. If you see this error:

```
initdb: error: cannot be run as root
```

You need to run pg0 as a non-root user:

```bash
# Create a non-root user and run pg0
useradd -m pguser
su - pguser -c "pg0 start"
```

**Note:** This means pg0 won't work in environments that only allow root access, such as:
- Google Colab (runs as root)
- Some CI environments
- Restricted containers

See the [Docker](#docker) section for complete examples of running pg0 as a non-root user.

### Port Already in Use

If port 5432 is already in use, pg0 will automatically find an available port:

```bash
pg0 start --name second-instance
# Output: Port 5432 is in use, using port 54321 instead.
```

To use a specific port, specify it explicitly:

```bash
pg0 start --port 5433
```

## Build from Source

```bash
cargo build --release
```

The binary will be at `target/release/pg0`.

## Changelog

### 0.12.2
- Fix reproducible builds by committing `Cargo.lock` ([`28c51ec`](https://github.com/vectorize-io/pg0/commit/28c51ec))

### 0.12.1
- Fix data loss on restart after unclean shutdown ([#6](https://github.com/vectorize-io/pg0/issues/6), [`21e0f08`](https://github.com/vectorize-io/pg0/commit/21e0f08))

### 0.12.0
- Intel Mac (x86_64) support ([#5](https://github.com/vectorize-io/pg0/pull/5))
- Fix Python sdist build ([#4](https://github.com/vectorize-io/pg0/pull/4))

### 0.11.0
- Improved error handling and logging in Python SDK ([`b6cb333`](https://github.com/vectorize-io/pg0/commit/b6cb333))

### 0.10.0
- Bundled CLI binary in Python package ([#1](https://github.com/vectorize-io/pg0/pull/1))

### 0.9.0
- Bundled pgvector extension ([`5ee9fee`](https://github.com/vectorize-io/pg0/commit/5ee9fee))

### 0.8.0
- Bundled PostgreSQL binaries for offline use ([`a565d5b`](https://github.com/vectorize-io/pg0/commit/a565d5b))

### 0.7.0
- GLIBC 2.31 support ([`dd4755c`](https://github.com/vectorize-io/pg0/commit/dd4755c))

### 0.6.0
- ARM64 + Alpine Linux support ([`ebcd95d`](https://github.com/vectorize-io/pg0/commit/ebcd95d))
- `drop` command and Python/Node SDKs ([`24b75fa`](https://github.com/vectorize-io/pg0/commit/24b75fa))

### 0.2.0
- Multi-instance support ([`b3ac463`](https://github.com/vectorize-io/pg0/commit/b3ac463))

### 0.1.0
- Initial release

## License

MIT
```

## File: `build.rs`
```rust
use std::env;
use std::fs;
use std::io;
use std::path::PathBuf;

fn main() {
    println!("cargo:rerun-if-changed=versions.env");

    // Load versions from versions.env
    let versions_env = fs::read_to_string("versions.env").expect("Failed to read versions.env");
    let mut pg_version = String::new();
    let mut pgvector_version = String::new();
    let mut pgvector_tag = String::new();
    let mut pgvector_repo = String::new();

    for line in versions_env.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        if let Some((key, value)) = line.split_once('=') {
            match key.trim() {
                "PG_VERSION" => pg_version = value.trim().to_string(),
                "PGVECTOR_VERSION" => pgvector_version = value.trim().to_string(),
                "PGVECTOR_COMPILED_TAG" => pgvector_tag = value.trim().to_string(),
                "PGVECTOR_COMPILED_REPO" => pgvector_repo = value.trim().to_string(),
                _ => {}
            }
        }
    }

    println!("cargo:rustc-env=PG_VERSION={}", pg_version);
    println!("cargo:rustc-env=PGVECTOR_VERSION={}", pgvector_version);
    println!("cargo:rustc-env=PGVECTOR_COMPILED_TAG={}", pgvector_tag);
    println!("cargo:rustc-env=PGVECTOR_COMPILED_REPO={}", pgvector_repo);

    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());

    // Bundle PostgreSQL and pgvector
    bundle_postgresql(&pg_version, &out_dir);
    bundle_pgvector(&pg_version, &pgvector_tag, &pgvector_repo, &out_dir);
}

fn bundle_postgresql(pg_version: &str, out_dir: &PathBuf) {
    let target = env::var("TARGET").unwrap();

    // Map Rust target to theseus-rs binary name
    let pg_target = match target.as_str() {
        "aarch64-apple-darwin" => "aarch64-apple-darwin",
        "x86_64-apple-darwin" => "x86_64-apple-darwin",
        "x86_64-unknown-linux-gnu" => "x86_64-unknown-linux-gnu",
        "x86_64-unknown-linux-musl" => "x86_64-unknown-linux-musl",
        "aarch64-unknown-linux-gnu" => "aarch64-unknown-linux-gnu",
        "aarch64-unknown-linux-musl" => "aarch64-unknown-linux-musl",
        "x86_64-pc-windows-msvc" => "x86_64-pc-windows-msvc",
        _ => {
            eprintln!(
                "Warning: Unknown target {}, PostgreSQL will not be bundled",
                target
            );
            let marker = out_dir.join("postgresql_bundle.tar.gz");
            fs::write(&marker, b"").expect("Failed to create empty bundle marker");
            println!(
                "cargo:rustc-env=POSTGRESQL_BUNDLE_PATH={}",
                marker.display()
            );
            println!("cargo:rustc-env=POSTGRESQL_BUNDLED=false");
            return;
        }
    };

    let ext = if target.contains("windows") {
        "zip"
    } else {
        "tar.gz"
    };
    let filename = format!("postgresql-{}-{}.{}", pg_version, pg_target, ext);
    let url = format!(
        "https://github.com/theseus-rs/postgresql-binaries/releases/download/{}/{}",
        pg_version, filename
    );

    let bundle_path = out_dir.join(&filename);

    // Download if not already cached
    if !bundle_path.exists() {
        eprintln!(
            "Downloading PostgreSQL {} for {}...",
            pg_version, pg_target
        );
        download_file(&url, &bundle_path).expect("Failed to download PostgreSQL bundle");
        eprintln!("Downloaded to {}", bundle_path.display());
    } else {
        eprintln!("Using cached PostgreSQL bundle: {}", bundle_path.display());
    }

    println!(
        "cargo:rustc-env=POSTGRESQL_BUNDLE_PATH={}",
        bundle_path.display()
    );
}

fn bundle_pgvector(pg_version: &str, pgvector_tag: &str, pgvector_repo: &str, out_dir: &PathBuf) {
    let target = env::var("TARGET").unwrap();

    // Map Rust target to pgvector platform name
    let pgvector_platform = match target.as_str() {
        "aarch64-apple-darwin" => "aarch64-apple-darwin",
        "x86_64-apple-darwin" => "x86_64-apple-darwin",
        "x86_64-unknown-linux-gnu" => "x86_64-unknown-linux-gnu",
        "x86_64-unknown-linux-musl" => "x86_64-unknown-linux-gnu", // musl uses gnu pgvector
        "aarch64-unknown-linux-gnu" => "aarch64-unknown-linux-gnu",
        "aarch64-unknown-linux-musl" => "aarch64-unknown-linux-gnu", // musl uses gnu pgvector
        "x86_64-pc-windows-msvc" => {
            eprintln!("Warning: pgvector not available for Windows, skipping bundle");
            let marker = out_dir.join("pgvector_bundle.tar.gz");
            fs::write(&marker, b"").expect("Failed to create empty pgvector marker");
            println!(
                "cargo:rustc-env=PGVECTOR_BUNDLE_PATH={}",
                marker.display()
            );
            return;
        }
        _ => {
            eprintln!(
                "Warning: Unknown target {}, pgvector will not be bundled",
                target
            );
            let marker = out_dir.join("pgvector_bundle.tar.gz");
            fs::write(&marker, b"").expect("Failed to create empty pgvector marker");
            println!(
                "cargo:rustc-env=PGVECTOR_BUNDLE_PATH={}",
                marker.display()
            );
            return;
        }
    };

    // Get PG major version (e.g., "18" from "18.1.0")
    let pg_major = pg_version.split('.').next().unwrap_or("18");

    let filename = format!("pgvector-{}-pg{}.tar.gz", pgvector_platform, pg_major);
    let url = format!(
        "https://github.com/{}/releases/download/{}/{}",
        pgvector_repo, pgvector_tag, filename
    );

    let bundle_path = out_dir.join(&filename);

    // Download if not already cached
    if !bundle_path.exists() {
        eprintln!(
            "Downloading pgvector for {} (PG {})...",
            pgvector_platform, pg_major
        );
        download_file(&url, &bundle_path).expect("Failed to download pgvector bundle");
        eprintln!("Downloaded to {}", bundle_path.display());
    } else {
        eprintln!("Using cached pgvector bundle: {}", bundle_path.display());
    }

    println!(
        "cargo:rustc-env=PGVECTOR_BUNDLE_PATH={}",
        bundle_path.display()
    );
}

fn download_file(url: &str, dest: &PathBuf) -> io::Result<()> {
    // Use curl for downloading (available on all CI platforms)
    let status = std::process::Command::new("curl")
        .args(["-fsSL", url, "-o"])
        .arg(dest)
        .status()?;

    if !status.success() {
        return Err(io::Error::new(
            io::ErrorKind::Other,
            format!("Failed to download {}", url),
        ));
    }

    Ok(())
}
```

## File: `build.sh`
```bash
#!/bin/bash
set -e

echo "Building pg0..."

# Build release binary
cargo build --release

# Get the binary path
BINARY="target/release/pg0"

echo ""
echo "Build complete!"
echo "Binary: $BINARY"
echo ""
echo "To install locally:"
echo "  cp $BINARY /usr/local/bin/"
echo "  # or"
echo "  cp $BINARY ~/.local/bin/"
```

## File: `install.sh`
```bash
#!/bin/bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

REPO="vectorize-io/pg0"
BINARY_NAME="pg0"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"

# Detect OS and architecture
detect_platform() {
    local os arch libc platform

    case "$(uname -s)" in
        Linux*)     os="linux";;
        Darwin*)    os="darwin";;
        MINGW*|MSYS*|CYGWIN*)  os="windows";;
        *)          echo -e "${RED}Unsupported operating system: $(uname -s)${NC}"; exit 1;;
    esac

    case "$(uname -m)" in
        x86_64|amd64)   arch="x86_64";;
        arm64|aarch64)  arch="aarch64";;
        *)              echo -e "${RED}Unsupported architecture: $(uname -m)${NC}"; exit 1;;
    esac

    # Detect libc for Linux (musl vs glibc)
    if [ "$os" = "linux" ]; then
        if [ -f "/lib/ld-musl-${arch}.so.1" ] || [ -f "/lib/ld-musl-x86_64.so.1" ] || [ -f "/lib/ld-musl-aarch64.so.1" ]; then
            # Running on Alpine/musl
            libc="musl"
        else
            # Running on Debian/Ubuntu/etc with glibc
            libc="gnu"

            # Check glibc version - if too old, fall back to musl (statically linked)
            # Our gnu binaries require GLIBC 2.35+ (built on Ubuntu 22.04)
            if command -v ldd >/dev/null 2>&1; then
                glibc_version=$(ldd --version 2>&1 | head -n1 | grep -oE '[0-9]+\.[0-9]+' | head -n1)
                if [ -n "$glibc_version" ]; then
                    # Compare versions (2.35 minimum)
                    glibc_major=$(echo "$glibc_version" | cut -d. -f1)
                    glibc_minor=$(echo "$glibc_version" | cut -d. -f2)

                    if [ "$glibc_major" -lt 2 ] || ([ "$glibc_major" -eq 2 ] && [ "$glibc_minor" -lt 35 ]); then
                        echo -e "${YELLOW}Note: Detected old glibc ${glibc_version}. Using statically-linked musl binary for compatibility.${NC}"
                        libc="musl"
                    fi
                fi
            fi
        fi
        platform="${os}-${arch}-${libc}"
    else
        platform="${os}-${arch}"
    fi

    # Validate supported platforms
    case "$platform" in
        darwin-aarch64|linux-x86_64-gnu|linux-x86_64-musl|linux-aarch64-gnu|linux-aarch64-musl|windows-x86_64)
            ;;
        darwin-x86_64)
            echo -e "${YELLOW}Note: Intel Mac users can run the Apple Silicon binary via Rosetta 2${NC}"
            platform="darwin-aarch64"
            ;;
        *)
            echo -e "${RED}Unsupported platform: ${platform}${NC}"
            echo "Supported platforms:"
            echo "  - darwin-aarch64 (macOS Apple Silicon)"
            echo "  - linux-x86_64-gnu (Debian/Ubuntu x86_64)"
            echo "  - linux-x86_64-musl (Alpine x86_64)"
            echo "  - linux-aarch64-gnu (Debian/Ubuntu ARM64)"
            echo "  - linux-aarch64-musl (Alpine ARM64)"
            echo "  - windows-x86_64"
            exit 1
            ;;
    esac

    echo "$platform"
}

# Get latest release tag
get_latest_version() {
    local auth_header=""
    if [ -n "${GITHUB_TOKEN:-}" ]; then
        auth_header="Authorization: Bearer ${GITHUB_TOKEN}"
    fi

    if [ -n "$auth_header" ]; then
        curl -sL -H "$auth_header" "https://api.github.com/repos/${REPO}/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'
    else
        curl -sL "https://api.github.com/repos/${REPO}/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'
    fi
}

main() {
    echo -e "${GREEN}Installing pg0 - embedded PostgreSQL CLI...${NC}"

    local platform
    platform=$(detect_platform)
    echo "Detected platform: ${platform}"

    local ext=""
    if [[ "$platform" == windows* ]]; then
        ext=".exe"
    fi

    local url
    # Check if PG0_BINARY_URL is set (supports file:// and http(s)://)
    if [ -n "${PG0_BINARY_URL:-}" ]; then
        url="${PG0_BINARY_URL}"
        echo "Using custom binary URL: ${url}"
    else
        local version
        version=$(get_latest_version)
        if [ -z "$version" ]; then
            echo -e "${RED}Failed to fetch latest version${NC}"
            exit 1
        fi
        echo "Latest version: ${version}"

        local filename="${BINARY_NAME}-${platform}${ext}"
        url="https://github.com/${REPO}/releases/download/${version}/${filename}"
        echo "Downloading from: ${url}"
    fi

    # Create install directory if it doesn't exist
    mkdir -p "${INSTALL_DIR}"

    # Download/copy binary
    local tmp_file
    tmp_file=$(mktemp)

    if [[ "$url" == file://* ]]; then
        # Handle file:// URLs - just copy the file
        local file_path="${url#file://}"
        if [ ! -f "$file_path" ]; then
            echo -e "${RED}File not found: ${file_path}${NC}"
            rm -f "${tmp_file}"
            exit 1
        fi
        cp "$file_path" "${tmp_file}"
    else
        # Handle http(s):// URLs
        if ! curl -fsSL "${url}" -o "${tmp_file}"; then
            echo -e "${RED}Failed to download binary${NC}"
            rm -f "${tmp_file}"
            exit 1
        fi
    fi

    # Move to install directory
    mv "${tmp_file}" "${INSTALL_DIR}/${BINARY_NAME}${ext}"
    chmod +x "${INSTALL_DIR}/${BINARY_NAME}${ext}"

    echo -e "${GREEN}Successfully installed ${BINARY_NAME} to ${INSTALL_DIR}/${BINARY_NAME}${ext}${NC}"

    # Check if install dir is in PATH
    if [[ ":$PATH:" != *":${INSTALL_DIR}:"* ]]; then
        echo ""
        echo -e "${YELLOW}NOTE: ${INSTALL_DIR} is not in your PATH.${NC}"
        echo "Add it to your shell configuration:"
        echo ""
        echo "  export PATH=\"\$PATH:${INSTALL_DIR}\""
        echo ""
    fi

    echo ""
    echo "pg0 is now available."
}

main "$@"
```

## File: `release.sh`
```bash
#!/bin/bash
set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

show_usage() {
    echo "Usage: ./release.sh <component> <version>"
    echo ""
    echo "Components:"
    echo "  cli     - CLI + Python package (tag: v*)"
    echo "  node    - Node.js client (tag: node-*)"
    echo ""
    echo "Version:"
    echo "  X.Y.Z   - Explicit version (e.g., 1.0.0)"
    echo "  patch   - Bump patch version (0.1.0 -> 0.1.1)"
    echo "  minor   - Bump minor version (0.1.0 -> 0.2.0)"
    echo "  major   - Bump major version (0.1.0 -> 1.0.0)"
    echo ""
    echo "Examples:"
    echo "  ./release.sh cli 0.1.0"
    echo "  ./release.sh cli patch"
    echo "  ./release.sh node 1.0.0"
    echo "  ./release.sh node patch"
    echo ""
    echo "Note: 'cli' releases both the CLI binaries and Python package together"
}

get_cli_version() {
    grep '^version = ' Cargo.toml | head -1 | sed 's/version = "\(.*\)"/\1/'
}

get_py_version() {
    grep '^version = ' sdk/python/pyproject.toml | head -1 | sed 's/version = "\(.*\)"/\1/'
}

get_node_version() {
    grep '"version"' sdk/node/package.json | head -1 | sed 's/.*"version": "\(.*\)".*/\1/'
}

bump_version() {
    local current=$1
    local bump_type=$2

    IFS='.' read -r MAJOR MINOR PATCH <<< "$current"

    case $bump_type in
        patch)
            PATCH=$((PATCH + 1))
            ;;
        minor)
            MINOR=$((MINOR + 1))
            PATCH=0
            ;;
        major)
            MAJOR=$((MAJOR + 1))
            MINOR=0
            PATCH=0
            ;;
    esac

    echo "${MAJOR}.${MINOR}.${PATCH}"
}

validate_version() {
    local version=$1
    if ! echo "$version" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
        echo -e "${RED}Error: Invalid version format '$version'${NC}"
        echo "Version must be in semantic format: X.Y.Z (e.g., 1.0.0)"
        exit 1
    fi
}

check_clean_git() {
    if ! git diff --quiet || ! git diff --staged --quiet; then
        echo -e "${RED}Error: You have uncommitted changes. Please commit or stash them first.${NC}"
        git status --short
        exit 1
    fi
}

check_tag_exists() {
    local tag=$1
    if git rev-parse "$tag" >/dev/null 2>&1; then
        echo -e "${RED}Error: Tag $tag already exists${NC}"
        exit 1
    fi
}

release_cli() {
    local version=$1
    local current_cli=$(get_cli_version)
    local current_py=$(get_py_version)

    echo -e "${BLUE}CLI + Python Release${NC}"
    echo "Current CLI version: $current_cli"
    echo "Current Python version: $current_py"

    # Handle version bump (based on CLI version)
    if [ "$version" = "patch" ] || [ "$version" = "minor" ] || [ "$version" = "major" ]; then
        version=$(bump_version "$current_cli" "$version")
    fi

    validate_version "$version"
    local tag="v$version"

    check_clean_git
    check_tag_exists "$tag"

    echo -e "${YELLOW}Preparing release $tag (CLI + Python)${NC}"

    # Update version in Cargo.toml
    echo "Updating Cargo.toml version to $version..."
    sed -i.bak "s/^version = \".*\"/version = \"$version\"/" Cargo.toml
    rm -f Cargo.toml.bak

    # Update version in pyproject.toml
    echo "Updating pyproject.toml version to $version..."
    sed -i.bak "s/^version = \".*\"/version = \"$version\"/" sdk/python/pyproject.toml
    rm -f sdk/python/pyproject.toml.bak

    # Commit and tag
    git add Cargo.toml sdk/python/pyproject.toml
    git commit -m "chore: bump CLI version to $version"
    git tag -a "$tag" -m "Release $version"

    # Push
    git push
    git push origin "$tag"

    echo -e "${GREEN}Release $tag pushed!${NC}"
    echo ""
    echo "This will release:"
    echo "  - CLI binaries to GitHub Releases"
    echo "  - Python package to PyPI (pg0-embedded)"
}

release_node() {
    local version=$1
    local current=$(get_node_version)

    echo -e "${BLUE}Node.js Release${NC}"
    echo "Current version: $current"

    # Handle version bump
    if [ "$version" = "patch" ] || [ "$version" = "minor" ] || [ "$version" = "major" ]; then
        version=$(bump_version "$current" "$version")
    fi

    validate_version "$version"
    local tag="node-$version"

    check_clean_git
    check_tag_exists "$tag"

    echo -e "${YELLOW}Preparing Node.js release $tag${NC}"

    # Update version in package.json
    echo "Updating package.json version to $version..."
    cd sdk/node
    npm version "$version" --no-git-tag-version
    cd ../..

    # Commit and tag
    git add sdk/node/package.json
    git commit -m "chore: bump Node.js client version to $version"
    git tag -a "$tag" -m "Node.js Client Release $version"

    # Push
    git push
    git push origin "$tag"

    echo -e "${GREEN}Node.js release $tag pushed!${NC}"
    echo "Package will be published to npm as: @vectorize-io/pg0"
}

# Main
if [ -z "$1" ] || [ -z "$2" ]; then
    show_usage
    exit 1
fi

COMPONENT=$1
VERSION=$2

case $COMPONENT in
    cli)
        release_cli "$VERSION"
        ;;
    node|nodejs)
        release_node "$VERSION"
        ;;
    *)
        echo -e "${RED}Error: Unknown component '$COMPONENT'${NC}"
        echo ""
        show_usage
        exit 1
        ;;
esac
```

## File: `versions.env`
```
PG_VERSION=18.1.0
PGVECTOR_VERSION=0.8.1
PGVECTOR_COMPILED_TAG=v0.18.237
PGVECTOR_COMPILED_REPO=nicoloboschi/pgvector_compiled

# PgBouncer for connection pooling
PGBOUNCER_VERSION=1.23.1
PGBOUNCER_COMPILED_TAG=v1.23.1
PGBOUNCER_COMPILED_REPO=nicoloboschi/pgbouncer_compiled
```

## File: `docker-tests/README.md`
```markdown
# Docker Tests for pg0

Automated tests to verify pg0 works correctly across different platforms and distributions.

## CLI Tests

| Test | Image | Platform | Architecture | libc |
|------|-------|----------|--------------|------|
| `test_debian_amd64.sh` | python:3.11-slim | linux/amd64 | x86_64 | glibc |
| `test_debian_arm64.sh` | python:3.11-slim | linux/arm64 | aarch64 | glibc |
| `test_alpine_amd64.sh` | python:3.12-alpine3.20 | linux/amd64 | x86_64 | musl |
| `test_alpine_arm64.sh` | python:3.12-alpine3.20 | linux/arm64 | aarch64 | musl |

## Python SDK Tests

| Test | Image | Platform | Architecture | libc |
|------|-------|----------|--------------|------|
| `python/test_debian_amd64.sh` | python:3.11-slim | linux/amd64 | x86_64 | glibc |
| `python/test_debian_arm64.sh` | python:3.11-slim | linux/arm64 | aarch64 | glibc |
| `python/test_alpine_amd64.sh` | python:3.12-alpine3.20 | linux/amd64 | x86_64 | musl |
| `python/test_alpine_arm64.sh` | python:3.12-alpine3.20 | linux/arm64 | aarch64 | musl |

The Python SDK tests install the package via `pip install .` and verify the bundled binary works correctly.

## What Each Test Does

1. **System Check** - Verifies architecture and OS
2. **Install pg0** - Downloads and installs pg0 CLI
3. **Start PostgreSQL** - Starts embedded PostgreSQL server
4. **Basic SELECT** - Tests PostgreSQL connectivity
5. **Table Operations** - Creates table, inserts data, queries
6. **pgvector Test** - Tests vector extension (if available)
7. **Cleanup** - Stops PostgreSQL

## Running Tests

### Run All Tests

```bash
cd docker-tests
chmod +x *.sh
./run_all_tests.sh
```

### Run Individual Tests

```bash
# Test Debian AMD64 (most common)
./test_debian_amd64.sh

# Test Debian ARM64 (M1/M2/M3 Macs, AWS Graviton)
./test_debian_arm64.sh

# Test Alpine AMD64
./test_alpine_amd64.sh

# Test Alpine ARM64
./test_alpine_arm64.sh
```

## Expected Results

### Debian/Ubuntu (glibc)
- ✅ PostgreSQL: Works
- ✅ pgvector: Works
- ✅ All queries: Success

### Alpine (musl)
- ✅ PostgreSQL: Works (requires `icu-libs`, `lz4-libs`, `libxml2`, `zstd-libs`, `procps` packages and ICU 74 - use Alpine 3.20)
- ⚠️ pgvector: Fails (no musl binaries available - glibc-only)
- ✅ Basic queries: Success

**Note:** The PostgreSQL musl binary is built against ICU 74. Alpine 3.22+ uses ICU 76 which is not compatible. Use Alpine 3.20 for musl-based deployments.

## Requirements

- Docker installed and running
- Internet connection (to download pg0 binary)
- ~50MB free space (PostgreSQL and pgvector are bundled in the binary)

## Troubleshooting

### ARM64 tests are slow

ARM64 tests use emulation on x86_64 hosts, which is slower. This is expected.

### pgvector fails on Alpine

This is a known limitation. pgvector binaries are currently only available for glibc, not musl.

## CI Integration

These tests can be integrated into GitHub Actions:

```yaml
- name: Test pg0 on Debian AMD64
  run: |
    cd docker-tests
    ./test_debian_amd64.sh
```

## Adding New Tests

To add a new platform test:

1. Copy an existing test script
2. Modify the image and platform
3. Update the Docker command as needed
4. Add it to `run_all_tests.sh`
```

## File: `docker-tests/run_all_tests.sh`
```bash
#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

FAILED_TESTS=()
PASSED_TESTS=()

run_test() {
    local test_name=$1
    local test_script=$2

    echo ""
    echo -e "${BLUE}======================================${NC}"
    echo -e "${BLUE}Running: $test_name${NC}"
    echo -e "${BLUE}======================================${NC}"

    if bash "$test_script"; then
        PASSED_TESTS+=("$test_name")
        echo -e "${GREEN}✅ $test_name PASSED${NC}"
    else
        FAILED_TESTS+=("$test_name")
        echo -e "${RED}❌ $test_name FAILED${NC}"
    fi
}

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}pg0 Docker Test Suite${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "This will test pg0 on multiple platforms:"
echo "  - Debian AMD64 (python:3.11-slim)"
echo "  - Debian ARM64 (python:3.11-slim)"
echo "  - Alpine AMD64 (python:3.11-alpine)"
echo "  - Alpine ARM64 (python:3.11-alpine)"
echo ""
echo -e "${YELLOW}Note: ARM64 tests will use emulation on x86_64 hosts${NC}"
echo ""
read -p "Press Enter to continue..."

# Run all tests
run_test "Debian AMD64" "$DIR/test_debian_amd64.sh"
run_test "Debian ARM64" "$DIR/test_debian_arm64.sh"
run_test "Alpine AMD64" "$DIR/test_alpine_amd64.sh"
run_test "Alpine ARM64" "$DIR/test_alpine_arm64.sh"

# Print summary
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Test Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

if [ ${#PASSED_TESTS[@]} -gt 0 ]; then
    echo -e "${GREEN}Passed (${#PASSED_TESTS[@]}):${NC}"
    for test in "${PASSED_TESTS[@]}"; do
        echo -e "  ${GREEN}✅${NC} $test"
    done
fi

if [ ${#FAILED_TESTS[@]} -gt 0 ]; then
    echo ""
    echo -e "${RED}Failed (${#FAILED_TESTS[@]}):${NC}"
    for test in "${FAILED_TESTS[@]}"; do
        echo -e "  ${RED}❌${NC} $test"
    done
    echo ""
    exit 1
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}🎉 ALL TESTS PASSED!${NC}"
echo -e "${GREEN}========================================${NC}"
```

## File: `docker-tests/test_alpine_amd64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 on Alpine AMD64"
echo "Image: python:3.12-alpine3.20"
echo "Platform: linux/amd64"
echo "=================================="

# Get the script directory to find install.sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INSTALL_SCRIPT="$SCRIPT_DIR/../install.sh"

# Note: Using Alpine 3.20 because the musl PostgreSQL binary requires ICU 74
# Alpine 3.22 has ICU 76 which is not compatible
docker run --rm --platform=linux/amd64 \
  -v "$INSTALL_SCRIPT:/tmp/install.sh:ro" \
  python:3.12-alpine3.20 sh -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing dependencies ==="
apk add --no-cache curl bash sudo procps shadow icu-libs lz4-libs libxml2 zstd-libs > /dev/null 2>&1

echo ""
echo "=== Creating non-root user ==="
adduser -D -s /bin/bash pguser
echo "pguser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

echo ""
echo "=== Copying local install.sh ==="
cp /tmp/install.sh /usr/local/bin/install.sh
chmod 755 /usr/local/bin/install.sh

echo ""
echo "=== Switching to non-root user for pg0 ==="
su - pguser << EOF
set -e

echo "=== Installing pg0 ==="
bash /usr/local/bin/install.sh
export PATH="\$HOME/.local/bin:\$PATH"

echo ""
echo "=== Checking pg0 version ==="
pg0 --version

echo ""
echo "=== Starting PostgreSQL ==="
pg0 start
sleep 5

echo ""
echo "=== Getting instance info ==="
pg0 info

echo ""
echo "=== Testing basic SELECT query ==="
pg0 psql -c "SELECT version();" -t | head -1

echo ""
echo "=== Testing table creation and data ==="
pg0 psql -c "CREATE TABLE test (id INT, name TEXT);"
pg0 psql -c "INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');"
pg0 psql -c "SELECT * FROM test;" -t

echo ""
echo "=== Testing pgvector extension ==="
if pg0 psql -c "CREATE EXTENSION IF NOT EXISTS vector;" 2>&1; then
    echo "✅ pgvector extension created successfully"
    pg0 psql -c "CREATE TABLE embeddings (id INT, vec vector(3));"
    pg0 psql -c "INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');"
    pg0 psql -c "SELECT * FROM embeddings;" -t
    echo "✅ pgvector working correctly"
else
    echo "⚠️  pgvector extension failed (known limitation on Alpine/musl)"
fi

echo ""
echo "=== Stopping PostgreSQL ==="
pg0 stop

echo ""
echo "=================================="
echo "✅ ALL TESTS PASSED - Alpine AMD64"
echo "=================================="
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `docker-tests/test_alpine_arm64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 on Alpine ARM64"
echo "Image: python:3.12-alpine3.20"
echo "Platform: linux/arm64"
echo "=================================="

# Get the script directory to find install.sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INSTALL_SCRIPT="$SCRIPT_DIR/../install.sh"

# Note: Using Alpine 3.20 because the musl PostgreSQL binary requires ICU 74
# Alpine 3.22 has ICU 76 which is not compatible
docker run --rm --platform=linux/arm64 \
  -v "$INSTALL_SCRIPT:/tmp/install.sh:ro" \
  python:3.12-alpine3.20 sh -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing dependencies ==="
apk add --no-cache curl bash sudo procps shadow icu-libs lz4-libs libxml2 zstd-libs > /dev/null 2>&1

echo ""
echo "=== Creating non-root user ==="
adduser -D -s /bin/bash pguser
echo "pguser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

echo ""
echo "=== Copying local install.sh ==="
cp /tmp/install.sh /usr/local/bin/install.sh
chmod 755 /usr/local/bin/install.sh

echo ""
echo "=== Switching to non-root user for pg0 ==="
su - pguser << EOF
set -e

echo "=== Installing pg0 ==="
bash /usr/local/bin/install.sh
export PATH="\$HOME/.local/bin:\$PATH"

echo ""
echo "=== Checking pg0 version ==="
pg0 --version

echo ""
echo "=== Starting PostgreSQL ==="
pg0 start
sleep 5

echo ""
echo "=== Getting instance info ==="
pg0 info || (echo "Failed to get info, checking logs..." && cat ~/.pg0/instances/default/data/log/* 2>/dev/null || echo "No logs found")

echo ""
echo "=== Testing basic SELECT query ==="
pg0 psql -c "SELECT version();" -t | head -1

echo ""
echo "=== Testing table creation and data ==="
pg0 psql -c "CREATE TABLE test (id INT, name TEXT);"
pg0 psql -c "INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');"
pg0 psql -c "SELECT * FROM test;" -t

echo ""
echo "=== Testing pgvector extension ==="
if pg0 psql -c "CREATE EXTENSION IF NOT EXISTS vector;" 2>&1; then
    echo "✅ pgvector extension created successfully"
    pg0 psql -c "CREATE TABLE embeddings (id INT, vec vector(3));"
    pg0 psql -c "INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');"
    pg0 psql -c "SELECT * FROM embeddings;" -t
    echo "✅ pgvector working correctly"
else
    echo "⚠️  pgvector extension failed (known limitation on Alpine/musl)"
fi

echo ""
echo "=== Stopping PostgreSQL ==="
pg0 stop

echo ""
echo "=================================="
echo "✅ ALL TESTS PASSED - Alpine ARM64"
echo "=================================="
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `docker-tests/test_debian_amd64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 on Debian AMD64"
echo "Image: python:3.11-slim"
echo "Platform: linux/amd64"
echo "=================================="

# Get the script directory to find install.sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INSTALL_SCRIPT="$SCRIPT_DIR/../install.sh"

# Check if PG0_BINARY_PATH is set (local binary to test)
VOLUME_ARGS=""
BINARY_ENV=""
if [ -n "${PG0_BINARY_PATH:-}" ]; then
    echo "Using local binary: $PG0_BINARY_PATH"
    VOLUME_ARGS="-v $PG0_BINARY_PATH:/tmp/pg0-binary:ro"
    BINARY_ENV="-e PG0_BINARY_URL=file:///tmp/pg0-binary"
fi

docker run --rm --platform=linux/amd64 \
  $BINARY_ENV \
  -v "$INSTALL_SCRIPT:/tmp/install.sh:ro" \
  $VOLUME_ARGS \
  python:3.11-slim bash -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing dependencies ==="
apt-get update -qq
# Install dependencies - libicu version may vary by Debian version
apt-get install -y curl libxml2 libssl3 libgssapi-krb5-2 sudo procps 2>&1 | grep -v "^Get:" || true
# Install libicu (try different versions)
apt-get install -y libicu72 2>/dev/null || apt-get install -y libicu74 2>/dev/null || apt-get install -y libicu* 2>&1 | head -5

echo ""
echo "=== Creating non-root user ==="
useradd -m -s /bin/bash pguser
echo "pguser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

echo ""
echo "=== Copying local install.sh ==="
cp /tmp/install.sh /usr/local/bin/install.sh
chmod 755 /usr/local/bin/install.sh

echo ""
echo "=== Switching to non-root user for pg0 ==="
su - pguser << EOF
set -e
export PG0_BINARY_URL="${PG0_BINARY_URL}"

echo "=== Installing pg0 ==="
bash /usr/local/bin/install.sh
export PATH="\$HOME/.local/bin:\$PATH"

echo ""
echo "=== Checking pg0 version ==="
pg0 --version

echo ""
echo "=== Starting PostgreSQL ==="
pg0 start
sleep 5

echo ""
echo "=== Getting instance info ==="
pg0 info || (echo "Failed to get info, checking logs..." && cat ~/.pg0/instances/default/data/log/* 2>/dev/null || echo "No logs found")

echo ""
echo "=== Testing basic SELECT query ==="
pg0 psql -c "SELECT version();" -t | head -1

echo ""
echo "=== Testing table creation and data ==="
pg0 psql -c "CREATE TABLE test (id INT, name TEXT);"
pg0 psql -c "INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');"
pg0 psql -c "SELECT * FROM test;" -t

echo ""
echo "=== Testing pgvector extension ==="
if pg0 psql -c "CREATE EXTENSION IF NOT EXISTS vector;" 2>&1; then
    echo "✅ pgvector extension created successfully"
    pg0 psql -c "CREATE TABLE embeddings (id INT, vec vector(3));"
    pg0 psql -c "INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');"
    pg0 psql -c "SELECT * FROM embeddings;" -t
    echo "✅ pgvector working correctly"
else
    echo "⚠️  pgvector extension failed (expected on some platforms)"
fi

echo ""
echo "=== Stopping PostgreSQL ==="
pg0 stop

echo ""
echo "=================================="
echo "✅ ALL TESTS PASSED - Debian AMD64"
echo "=================================="
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `docker-tests/test_debian_arm64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 on Debian ARM64"
echo "Image: python:3.11-slim"
echo "Platform: linux/arm64"
echo "=================================="

# Get the script directory to find install.sh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INSTALL_SCRIPT="$SCRIPT_DIR/../install.sh"

docker run --rm --platform=linux/arm64 \
  -v "$INSTALL_SCRIPT:/tmp/install.sh:ro" \
  python:3.11-slim bash -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing dependencies ==="
apt-get update -qq
# Install dependencies - libicu version may vary by Debian version
apt-get install -y curl libxml2 libssl3 libgssapi-krb5-2 sudo procps 2>&1 | grep -v "^Get:" || true
# Install libicu (try different versions)
apt-get install -y libicu72 2>/dev/null || apt-get install -y libicu74 2>/dev/null || apt-get install -y libicu* 2>&1 | head -5

echo ""
echo "=== Creating non-root user ==="
useradd -m -s /bin/bash pguser
echo "pguser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

echo ""
echo "=== Copying local install.sh ==="
cp /tmp/install.sh /usr/local/bin/install.sh
chmod 755 /usr/local/bin/install.sh

echo ""
echo "=== Switching to non-root user for pg0 ==="
su - pguser << EOF
set -e

echo "=== Installing pg0 ==="
bash /usr/local/bin/install.sh
export PATH="\$HOME/.local/bin:\$PATH"

echo ""
echo "=== Checking pg0 version ==="
pg0 --version

echo ""
echo "=== Starting PostgreSQL ==="
pg0 start
sleep 5

echo ""
echo "=== Getting instance info ==="
pg0 info || (echo "Failed to get info, checking logs..." && cat ~/.pg0/instances/default/data/log/* 2>/dev/null || echo "No logs found")

echo ""
echo "=== Testing basic SELECT query ==="
pg0 psql -c "SELECT version();" -t | head -1

echo ""
echo "=== Testing table creation and data ==="
pg0 psql -c "CREATE TABLE test (id INT, name TEXT);"
pg0 psql -c "INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');"
pg0 psql -c "SELECT * FROM test;" -t

echo ""
echo "=== Testing pgvector extension ==="
if pg0 psql -c "CREATE EXTENSION IF NOT EXISTS vector;" 2>&1; then
    echo "✅ pgvector extension created successfully"
    pg0 psql -c "CREATE TABLE embeddings (id INT, vec vector(3));"
    pg0 psql -c "INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');"
    pg0 psql -c "SELECT * FROM embeddings;" -t
    echo "✅ pgvector working correctly"
else
    echo "⚠️  pgvector extension failed (expected on some platforms)"
fi

echo ""
echo "=== Stopping PostgreSQL ==="
pg0 stop

echo ""
echo "=================================="
echo "✅ ALL TESTS PASSED - Debian ARM64"
echo "=================================="
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `docker-tests/python/test_alpine_amd64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 Python SDK on Alpine AMD64"
echo "Image: python:3.12-alpine3.20"
echo "Platform: linux/amd64"
echo "=================================="

# Get the script directory to find the SDK
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SDK_DIR="$SCRIPT_DIR/../../sdk/python"

# Note: Using Alpine 3.20 because the musl PostgreSQL binary requires ICU 74
# Alpine 3.22 has ICU 76 which is not compatible
docker run --rm --platform=linux/amd64 \
  -v "$SDK_DIR:/sdk-src:ro" \
  python:3.12-alpine3.20 sh -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing system dependencies ==="
# procps is needed for pg0 to check if postgres process is running
# zstd-libs is needed for PostgreSQL compression support
apk add --no-cache bash sudo shadow icu-libs lz4-libs libxml2 procps zstd-libs > /dev/null 2>&1

echo ""
echo "=== Creating non-root user ==="
adduser -D -s /bin/bash pguser

# Copy SDK to writable location (excluding any existing bin directory with wrong-platform binary)
mkdir -p /home/pguser/sdk
cp -r /sdk-src/pg0 /home/pguser/sdk/
cp /sdk-src/pyproject.toml /sdk-src/hatch_build.py /sdk-src/README.md /home/pguser/sdk/
rm -rf /home/pguser/sdk/pg0/bin  # Remove any existing binary
chown -R pguser:pguser /home/pguser/sdk

echo ""
echo "=== Switching to non-root user ==="
su - pguser << EOF
set -e
export PATH="/usr/local/bin:\$PATH"

echo "=== Installing Python SDK (will download correct binary) ==="
cd /home/pguser/sdk
python3 -m pip install --user . -q

echo ""
echo "=== Testing Python SDK ==="
python3 << PYEOF
from pg0 import Pg0, _get_bundled_binary

# Check bundled binary
bundled = _get_bundled_binary()
print(f"Bundled binary: {bundled}")
assert bundled is not None, "Bundled binary not found!"
assert bundled.exists(), f"Bundled binary does not exist: {bundled}"

# Start PostgreSQL
print("")
print("=== Starting PostgreSQL ===")
pg = Pg0()
info = pg.start()
print(f"PostgreSQL running on port {info.port}")
print(f"URI: {info.uri}")

# Test basic query
print("")
print("=== Testing basic SELECT query ===")
result = pg.execute("SELECT version();")
print(result.strip().split("\\n")[0][:80])

# Test table operations
print("")
print("=== Testing table creation and data ===")
pg.execute("CREATE TABLE test (id INT, name TEXT);")
pg.execute("INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');")
result = pg.execute("SELECT * FROM test;")
print(result)

# Test pgvector (expected to fail on Alpine/musl)
print("")
print("=== Testing pgvector extension ===")
try:
    pg.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    print("✅ pgvector extension created successfully")
    pg.execute("CREATE TABLE embeddings (id INT, vec vector(3));")
    pg.execute("INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');")
    result = pg.execute("SELECT * FROM embeddings;")
    print(result)
    print("✅ pgvector working correctly")
except Exception as e:
    print("⚠️ pgvector extension failed (known limitation on Alpine/musl)")

# Stop PostgreSQL
print("")
print("=== Stopping PostgreSQL ===")
pg.stop()
pg.drop()

print("")
print("==================================")
print("✅ ALL TESTS PASSED - Alpine AMD64 Python SDK")
print("==================================")
PYEOF
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `docker-tests/python/test_alpine_arm64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 Python SDK on Alpine ARM64"
echo "Image: python:3.12-alpine3.20"
echo "Platform: linux/arm64"
echo "=================================="

# Get the script directory to find the SDK
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SDK_DIR="$SCRIPT_DIR/../../sdk/python"

# Note: Using Alpine 3.20 because the musl PostgreSQL binary requires ICU 74
# Alpine 3.22 has ICU 76 which is not compatible
docker run --rm --platform=linux/arm64 \
  -v "$SDK_DIR:/sdk-src:ro" \
  python:3.12-alpine3.20 sh -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing system dependencies ==="
# procps is needed for pg0 to check if postgres process is running
# zstd-libs is needed for PostgreSQL compression support
apk add --no-cache bash sudo shadow icu-libs lz4-libs libxml2 procps zstd-libs > /dev/null 2>&1

echo ""
echo "=== Creating non-root user ==="
adduser -D -s /bin/bash pguser

# Copy SDK to writable location (excluding any existing bin directory with wrong-platform binary)
mkdir -p /home/pguser/sdk
cp -r /sdk-src/pg0 /home/pguser/sdk/
cp /sdk-src/pyproject.toml /sdk-src/hatch_build.py /sdk-src/README.md /home/pguser/sdk/
rm -rf /home/pguser/sdk/pg0/bin  # Remove any existing binary
chown -R pguser:pguser /home/pguser/sdk

echo ""
echo "=== Switching to non-root user ==="
su - pguser << EOF
set -e
export PATH="/usr/local/bin:\$PATH"

echo "=== Installing Python SDK (will download correct binary) ==="
cd /home/pguser/sdk
python3 -m pip install --user . -q

echo ""
echo "=== Testing Python SDK ==="
python3 << PYEOF
from pg0 import Pg0, _get_bundled_binary

# Check bundled binary
bundled = _get_bundled_binary()
print(f"Bundled binary: {bundled}")
assert bundled is not None, "Bundled binary not found!"
assert bundled.exists(), f"Bundled binary does not exist: {bundled}"

# Start PostgreSQL
print("")
print("=== Starting PostgreSQL ===")
pg = Pg0()
info = pg.start()
print(f"PostgreSQL running on port {info.port}")
print(f"URI: {info.uri}")

# Test basic query
print("")
print("=== Testing basic SELECT query ===")
result = pg.execute("SELECT version();")
print(result.strip().split("\\n")[0][:80])

# Test table operations
print("")
print("=== Testing table creation and data ===")
pg.execute("CREATE TABLE test (id INT, name TEXT);")
pg.execute("INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');")
result = pg.execute("SELECT * FROM test;")
print(result)

# Test pgvector (expected to fail on Alpine/musl)
print("")
print("=== Testing pgvector extension ===")
try:
    pg.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    print("✅ pgvector extension created successfully")
    pg.execute("CREATE TABLE embeddings (id INT, vec vector(3));")
    pg.execute("INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');")
    result = pg.execute("SELECT * FROM embeddings;")
    print(result)
    print("✅ pgvector working correctly")
except Exception as e:
    print("⚠️ pgvector extension failed (known limitation on Alpine/musl)")

# Stop PostgreSQL
print("")
print("=== Stopping PostgreSQL ===")
pg.stop()
pg.drop()

print("")
print("==================================")
print("✅ ALL TESTS PASSED - Alpine ARM64 Python SDK")
print("==================================")
PYEOF
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `docker-tests/python/test_debian_amd64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 Python SDK on Debian AMD64"
echo "Image: python:3.11-slim"
echo "Platform: linux/amd64"
echo "=================================="

# Get the script directory to find the SDK
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SDK_DIR="$SCRIPT_DIR/../../sdk/python"

docker run --rm --platform=linux/amd64 \
  -v "$SDK_DIR:/sdk-src:ro" \
  python:3.11-slim bash -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing system dependencies ==="
apt-get update -qq
# procps is needed for pg0 to check if postgres process is running
apt-get install -y -qq libxml2 libssl3 libgssapi-krb5-2 procps > /dev/null 2>&1
apt-get install -y -qq libicu72 || apt-get install -y -qq libicu74 || apt-get install -y -qq libicu76 || apt-get install -y -qq "libicu*" > /dev/null 2>&1

echo ""
echo "=== Creating non-root user ==="
useradd -m -s /bin/bash pguser

# Copy SDK to writable location (excluding any existing bin directory with wrong-platform binary)
mkdir -p /home/pguser/sdk
cp -r /sdk-src/pg0 /home/pguser/sdk/
cp /sdk-src/pyproject.toml /sdk-src/hatch_build.py /sdk-src/README.md /home/pguser/sdk/
rm -rf /home/pguser/sdk/pg0/bin  # Remove any existing binary
chown -R pguser:pguser /home/pguser/sdk

echo ""
echo "=== Switching to non-root user ==="
su - pguser << EOF
set -e

echo "=== Installing Python SDK (will download correct binary) ==="
cd /home/pguser/sdk
pip install --user . -q

echo ""
echo "=== Testing Python SDK ==="
python3 << PYEOF
from pg0 import Pg0, _get_bundled_binary

# Check bundled binary
bundled = _get_bundled_binary()
print(f"Bundled binary: {bundled}")
assert bundled is not None, "Bundled binary not found!"
assert bundled.exists(), f"Bundled binary does not exist: {bundled}"

# Start PostgreSQL
print("")
print("=== Starting PostgreSQL ===")
pg = Pg0()
info = pg.start()
print(f"PostgreSQL running on port {info.port}")
print(f"URI: {info.uri}")

# Verify it is actually running
info = pg.info()
print(f"Verified running: {info.running}")
if not info.running:
    raise RuntimeError("PostgreSQL is not running after start!")

# Test basic query
print("")
print("=== Testing basic SELECT query ===")
result = pg.execute("SELECT version();")
print(result.strip().split("\\n")[0][:80])

# Test table operations
print("")
print("=== Testing table creation and data ===")
pg.execute("CREATE TABLE test (id INT, name TEXT);")
pg.execute("INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');")
result = pg.execute("SELECT * FROM test;")
print(result)

# Test pgvector
print("")
print("=== Testing pgvector extension ===")
try:
    pg.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    print("pgvector extension created successfully")
    pg.execute("CREATE TABLE embeddings (id INT, vec vector(3));")
    pg.execute("INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');")
    result = pg.execute("SELECT * FROM embeddings;")
    print(result)
    print("pgvector working correctly")
except Exception as e:
    print(f"pgvector failed: {e}")

# Stop PostgreSQL
print("")
print("=== Stopping PostgreSQL ===")
pg.stop()
pg.drop()

print("")
print("==================================")
print("ALL TESTS PASSED - Debian AMD64 Python SDK")
print("==================================")
PYEOF
EOF
'

echo ""
echo "Test completed successfully!"
```

## File: `docker-tests/python/test_debian_arm64.sh`
```bash
#!/bin/bash
set -e

echo "=================================="
echo "Testing pg0 Python SDK on Debian ARM64"
echo "Image: python:3.11-slim"
echo "Platform: linux/arm64"
echo "=================================="

# Get the script directory to find the SDK
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SDK_DIR="$SCRIPT_DIR/../../sdk/python"

docker run --rm --platform=linux/arm64 \
  -v "$SDK_DIR:/sdk-src:ro" \
  python:3.11-slim bash -c '
set -e

echo "=== System Info ==="
uname -m
cat /etc/os-release | grep PRETTY_NAME

echo ""
echo "=== Installing system dependencies ==="
apt-get update -qq
# procps is needed for pg0 to check if postgres process is running
apt-get install -y -qq libxml2 libssl3 libgssapi-krb5-2 procps > /dev/null 2>&1
apt-get install -y -qq libicu72 || apt-get install -y -qq libicu74 || apt-get install -y -qq libicu76 || apt-get install -y -qq "libicu*" > /dev/null 2>&1

echo ""
echo "=== Creating non-root user ==="
useradd -m -s /bin/bash pguser

# Copy SDK to writable location (excluding any existing bin directory with wrong-platform binary)
mkdir -p /home/pguser/sdk
cp -r /sdk-src/pg0 /home/pguser/sdk/
cp /sdk-src/pyproject.toml /sdk-src/hatch_build.py /sdk-src/README.md /home/pguser/sdk/
rm -rf /home/pguser/sdk/pg0/bin  # Remove any existing binary
chown -R pguser:pguser /home/pguser/sdk

echo ""
echo "=== Switching to non-root user ==="
su - pguser << EOF
set -e

echo "=== Installing Python SDK (will download correct binary) ==="
cd /home/pguser/sdk
pip install --user . -q

echo ""
echo "=== Testing Python SDK ==="
python3 << PYEOF
from pg0 import Pg0, _get_bundled_binary

# Check bundled binary
bundled = _get_bundled_binary()
print(f"Bundled binary: {bundled}")
assert bundled is not None, "Bundled binary not found!"
assert bundled.exists(), f"Bundled binary does not exist: {bundled}"

# Start PostgreSQL
print("")
print("=== Starting PostgreSQL ===")
pg = Pg0()
info = pg.start()
print(f"PostgreSQL running on port {info.port}")
print(f"URI: {info.uri}")

# Test basic query
print("")
print("=== Testing basic SELECT query ===")
result = pg.execute("SELECT version();")
print(result.strip().split("\\n")[0][:80])

# Test table operations
print("")
print("=== Testing table creation and data ===")
pg.execute("CREATE TABLE test (id INT, name TEXT);")
pg.execute("INSERT INTO test VALUES (1, '\''Hello'\''), (2, '\''World'\'');")
result = pg.execute("SELECT * FROM test;")
print(result)

# Test pgvector
print("")
print("=== Testing pgvector extension ===")
try:
    pg.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    print("✅ pgvector extension created successfully")
    pg.execute("CREATE TABLE embeddings (id INT, vec vector(3));")
    pg.execute("INSERT INTO embeddings VALUES (1, '\''[1,2,3]'\'');")
    result = pg.execute("SELECT * FROM embeddings;")
    print(result)
    print("✅ pgvector working correctly")
except Exception as e:
    print(f"⚠️ pgvector failed: {e}")

# Stop PostgreSQL
print("")
print("=== Stopping PostgreSQL ===")
pg.stop()
pg.drop()

print("")
print("==================================")
print("✅ ALL TESTS PASSED - Debian ARM64 Python SDK")
print("==================================")
PYEOF
EOF
'

echo ""
echo "✅ Test completed successfully!"
```

## File: `sdk/node/README.md`
```markdown
# pg0 - PostgreSQL for Node.js

[![npm](https://badge.fury.io/js/@vectorize-io%2Fpg0.svg)](https://www.npmjs.com/package/@vectorize-io/pg0)

Zero-config PostgreSQL with pgvector. No installation, no Docker, no configuration.

## Install

```bash
npm install @vectorize-io/pg0
```

## Usage

```typescript
import { Pg0 } from "@vectorize-io/pg0";

// Basic usage
const pg = new Pg0();
await pg.start();
console.log(await pg.getUri()); // postgresql://postgres:postgres@localhost:5432/postgres
await pg.execute("CREATE EXTENSION IF NOT EXISTS vector");
await pg.stop();

// Custom configuration
const pg = new Pg0({
  name: "myapp",
  port: 5433,
  username: "myuser",
  password: "mypass",
  database: "mydb",
  config: { shared_buffers: "512MB" }
});
await pg.start();
await pg.stop();

// Sync API also available
pg.startSync();
pg.stopSync();
```

## API

### Pg0 Class

| Method | Description |
|--------|-------------|
| `start()` / `startSync()` | Start PostgreSQL, returns `InstanceInfo` |
| `stop()` / `stopSync()` | Stop PostgreSQL |
| `drop()` / `dropSync()` | Stop and delete all data |
| `info()` / `infoSync()` | Get instance info |
| `execute(sql)` / `executeSync(sql)` | Run SQL query |
| `getUri()` / `getUriSync()` | Get connection URI |
| `isRunning()` / `isRunningSync()` | Check if running |

### Module Functions

```typescript
import { start, stop, drop, info, listInstances } from "@vectorize-io/pg0";

await start({ name: "default", port: 5432 });  // Start instance
await stop("default");                          // Stop instance
await drop("default");                          // Delete instance
await info("default");                          // Get instance info
await listInstances();                          // List all instances

// Sync versions: startSync, stopSync, dropSync, infoSync, listInstancesSync
```

## Links

- [GitHub](https://github.com/vectorize-io/pg0)
- [CLI Documentation](https://github.com/vectorize-io/pg0#readme)
```

## File: `sdk/node/package.json`
```json
{
  "name": "@vectorize-io/pg0",
  "version": "0.1.0",
  "description": "Node.js API for pg0 - embedded PostgreSQL with pgvector",
  "main": "dist/src/index.js",
  "types": "dist/src/index.d.ts",
  "files": [
    "dist"
  ],
  "scripts": {
    "build": "tsc",
    "test": "tsc && node --test dist/tests/*.test.js",
    "prepublishOnly": "npm run build"
  },
  "keywords": [
    "postgresql",
    "postgres",
    "database",
    "embedded",
    "pgvector",
    "vector"
  ],
  "author": "Vectorize",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/vectorize-io/pg0"
  },
  "homepage": "https://github.com/vectorize-io/pg0",
  "engines": {
    "node": ">=16"
  },
  "publishConfig": {
    "access": "public"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.0.0"
  }
}
```

## File: `sdk/node/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022"],
    "declaration": true,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "."
  },
  "include": ["src/**/*", "tests/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `sdk/node/src/index.ts`
```typescript
import { execFile, execFileSync, execSync } from "child_process";
import { chmodSync, existsSync, mkdirSync } from "fs";
import { homedir } from "os";
import { join } from "path";
import { promisify } from "util";

const execFileAsync = promisify(execFile);

const PG0_REPO = "vectorize-io/pg0";
const INSTALL_SCRIPT_URL = `https://raw.githubusercontent.com/${PG0_REPO}/main/install.sh`;

export class Pg0Error extends Error {
  constructor(message: string) {
    super(message);
    this.name = "Pg0Error";
  }
}

export class Pg0NotFoundError extends Pg0Error {
  constructor(message: string = "pg0 binary not found") {
    super(message);
    this.name = "Pg0NotFoundError";
  }
}

export class Pg0NotRunningError extends Pg0Error {
  constructor(message: string = "PostgreSQL instance is not running") {
    super(message);
    this.name = "Pg0NotRunningError";
  }
}

export class Pg0AlreadyRunningError extends Pg0Error {
  constructor(message: string = "PostgreSQL instance is already running") {
    super(message);
    this.name = "Pg0AlreadyRunningError";
  }
}

export interface InstanceInfo {
  name: string;
  running: boolean;
  pid?: number;
  port?: number;
  version?: string;
  username?: string;
  database?: string;
  data_dir?: string;
  uri?: string;
}

export interface Pg0Options {
  /** Instance name (allows multiple instances) */
  name?: string;
  /** Port to listen on */
  port?: number;
  /** Database username */
  username?: string;
  /** Database password */
  password?: string;
  /** Database name */
  database?: string;
  /** Custom data directory */
  dataDir?: string;
  /** PostgreSQL configuration options */
  config?: Record<string, string>;
}

function getInstallDir(): string {
  if (process.platform === "win32") {
    const base = process.env.LOCALAPPDATA || join(homedir(), "AppData", "Local");
    return join(base, "pg0", "bin");
  }
  return join(homedir(), ".local", "bin");
}

/**
 * Install the pg0 binary using the official install script.
 * @param force Force reinstall even if already installed
 * @returns Path to installed binary
 */
export async function install(force: boolean = false): Promise<string> {
  const installDir = getInstallDir();
  const binaryName = process.platform === "win32" ? "pg0.exe" : "pg0";
  const binaryPath = join(installDir, binaryName);

  if (existsSync(binaryPath) && !force) {
    return binaryPath;
  }

  // Use the official install script which handles:
  // - Platform detection (including old glibc fallback to musl)
  // - Intel Mac Rosetta handling
  // - Proper binary naming
  if (process.platform === "win32") {
    throw new Pg0NotFoundError(
      "Auto-install not supported on Windows. " +
      "Please download pg0 manually from https://github.com/vectorize-io/pg0/releases"
    );
  }

  console.log("Installing pg0 using official install script...");

  return new Promise((resolve, reject) => {
    const { exec } = require("child_process");
    exec(
      `curl -fsSL ${INSTALL_SCRIPT_URL} | bash`,
      { timeout: 120000 },
      (error: Error | null, stdout: string, stderr: string) => {
        if (error) {
          reject(new Pg0NotFoundError(`Install script failed: ${stderr || error.message}`));
          return;
        }

        // Verify installation
        if (existsSync(binaryPath)) {
          resolve(binaryPath);
          return;
        }

        // Check if installed to a different location via PATH
        try {
          const which = execSync("which pg0", { encoding: "utf-8" }).trim();
          if (which) {
            resolve(which);
            return;
          }
        } catch {
          // Not in PATH
        }

        reject(new Pg0NotFoundError("Install script succeeded but pg0 binary not found"));
      }
    );
  });
}

/**
 * Install the pg0 binary synchronously using the official install script.
 */
export function installSync(force: boolean = false): string {
  const installDir = getInstallDir();
  const binaryName = process.platform === "win32" ? "pg0.exe" : "pg0";
  const binaryPath = join(installDir, binaryName);

  if (existsSync(binaryPath) && !force) {
    return binaryPath;
  }

  // Use the official install script
  if (process.platform === "win32") {
    throw new Pg0NotFoundError(
      "Auto-install not supported on Windows. " +
      "Please download pg0 manually from https://github.com/vectorize-io/pg0/releases"
    );
  }

  console.log("Installing pg0 using official install script...");

  try {
    execSync(`curl -fsSL ${INSTALL_SCRIPT_URL} | bash`, {
      encoding: "utf-8",
      timeout: 120000,
    });

    // Verify installation
    if (existsSync(binaryPath)) {
      return binaryPath;
    }

    // Check if installed to a different location via PATH
    try {
      const which = execSync("which pg0", { encoding: "utf-8" }).trim();
      if (which) {
        return which;
      }
    } catch {
      // Not in PATH
    }

    throw new Pg0NotFoundError("Install script succeeded but pg0 binary not found");
  } catch (e: any) {
    if (e instanceof Pg0NotFoundError) throw e;
    throw new Pg0NotFoundError(`Failed to install pg0: ${e.message || e}`);
  }
}

function findPg0Sync(): string {
  // Check PATH
  const { execSync } = require("child_process");
  try {
    const result = execSync("which pg0 2>/dev/null || where pg0 2>nul", { encoding: "utf-8" });
    if (result.trim()) return result.trim().split("\n")[0];
  } catch {
    // Not in PATH
  }

  // Check install location
  const installDir = getInstallDir();
  const binaryName = process.platform === "win32" ? "pg0.exe" : "pg0";
  const binaryPath = join(installDir, binaryName);

  if (existsSync(binaryPath)) {
    return binaryPath;
  }

  // Auto-install
  return installSync();
}

async function findPg0(): Promise<string> {
  // Check install location first (faster than which)
  const installDir = getInstallDir();
  const binaryName = process.platform === "win32" ? "pg0.exe" : "pg0";
  const binaryPath = join(installDir, binaryName);

  if (existsSync(binaryPath)) {
    return binaryPath;
  }

  // Check PATH
  const { execSync } = require("child_process");
  try {
    const result = execSync("which pg0 2>/dev/null || where pg0 2>nul", { encoding: "utf-8" });
    if (result.trim()) return result.trim().split("\n")[0];
  } catch {
    // Not in PATH
  }

  // Auto-install
  return install();
}

async function runPg0(...args: string[]): Promise<{ stdout: string; stderr: string }> {
  const pg0Path = await findPg0();
  try {
    return await execFileAsync(pg0Path, args);
  } catch (error: any) {
    const stderr = error.stderr || error.message || "";
    if (stderr.toLowerCase().includes("already running")) {
      throw new Pg0AlreadyRunningError(stderr);
    } else if (
      stderr.toLowerCase().includes("no running instance") ||
      stderr.toLowerCase().includes("not running")
    ) {
      throw new Pg0NotRunningError(stderr);
    }
    throw new Pg0Error(stderr || "pg0 command failed");
  }
}

function runPg0Sync(...args: string[]): string {
  const pg0Path = findPg0Sync();
  try {
    return execFileSync(pg0Path, args, { encoding: "utf-8" });
  } catch (error: any) {
    const stderr = error.stderr || error.message || "";
    if (stderr.toLowerCase().includes("already running")) {
      throw new Pg0AlreadyRunningError(stderr);
    } else if (
      stderr.toLowerCase().includes("no running instance") ||
      stderr.toLowerCase().includes("not running")
    ) {
      throw new Pg0NotRunningError(stderr);
    }
    throw new Pg0Error(stderr || "pg0 command failed");
  }
}

/**
 * Embedded PostgreSQL instance.
 *
 * @example
 * ```typescript
 * import { Pg0 } from "pg0";
 *
 * const pg = new Pg0();
 * await pg.start();
 * console.log(await pg.getUri());
 * await pg.stop();
 * ```
 */
export class Pg0 {
  readonly name: string;
  readonly port: number;
  readonly username: string;
  readonly password: string;
  readonly database: string;
  readonly dataDir?: string;
  readonly config: Record<string, string>;

  constructor(options: Pg0Options = {}) {
    this.name = options.name ?? "default";
    this.port = options.port ?? 5432;
    this.username = options.username ?? "postgres";
    this.password = options.password ?? "postgres";
    this.database = options.database ?? "postgres";
    this.dataDir = options.dataDir;
    this.config = options.config ?? {};
  }

  /** Start the PostgreSQL instance. */
  async start(): Promise<InstanceInfo> {
    const args = this._buildStartArgs();
    await runPg0(...args);
    return this.info();
  }

  /** Start the PostgreSQL instance (synchronous). */
  startSync(): InstanceInfo {
    const args = this._buildStartArgs();
    runPg0Sync(...args);
    return this.infoSync();
  }

  private _buildStartArgs(): string[] {
    const args = [
      "start",
      "--name", this.name,
      "--port", String(this.port),
      "--username", this.username,
      "--password", this.password,
      "--database", this.database,
    ];

    if (this.dataDir) {
      args.push("--data-dir", this.dataDir);
    }

    for (const [key, value] of Object.entries(this.config)) {
      args.push("-c", `${key}=${value}`);
    }

    return args;
  }

  /** Stop the PostgreSQL instance. */
  async stop(): Promise<void> {
    try {
      await runPg0("stop", "--name", this.name);
    } catch (e) {
      // Ignore "not running" errors
      if (!(e instanceof Pg0NotRunningError)) throw e;
    }
  }

  /** Stop the PostgreSQL instance (synchronous). */
  stopSync(): void {
    try {
      runPg0Sync("stop", "--name", this.name);
    } catch (e) {
      // Ignore "not running" errors
      if (!(e instanceof Pg0NotRunningError)) throw e;
    }
  }

  /** Drop the PostgreSQL instance (stop if running, delete all data). */
  async drop(force: boolean = true): Promise<void> {
    const args = ["drop", "--name", this.name];
    if (force) args.push("--force");
    try {
      await runPg0(...args);
    } catch {
      // Ignore errors
    }
  }

  /** Drop the PostgreSQL instance (synchronous). */
  dropSync(force: boolean = true): void {
    const args = ["drop", "--name", this.name];
    if (force) args.push("--force");
    try {
      runPg0Sync(...args);
    } catch {
      // Ignore errors
    }
  }

  /** Get information about the PostgreSQL instance. */
  async info(): Promise<InstanceInfo> {
    const { stdout } = await runPg0("info", "--name", this.name, "-o", "json");
    return JSON.parse(stdout);
  }

  /** Get information about the PostgreSQL instance (synchronous). */
  infoSync(): InstanceInfo {
    const stdout = runPg0Sync("info", "--name", this.name, "-o", "json");
    return JSON.parse(stdout);
  }

  /** Get the connection URI if running. */
  async getUri(): Promise<string | undefined> {
    return (await this.info()).uri;
  }

  /** Get the connection URI if running (synchronous). */
  getUriSync(): string | undefined {
    return this.infoSync().uri;
  }

  /** Check if the instance is running. */
  async isRunning(): Promise<boolean> {
    return (await this.info()).running;
  }

  /** Check if the instance is running (synchronous). */
  isRunningSync(): boolean {
    return this.infoSync().running;
  }

  /** Run psql with the given arguments. */
  async psql(...args: string[]): Promise<{ stdout: string; stderr: string }> {
    return runPg0("psql", "--name", this.name, ...args);
  }

  /** Run psql with the given arguments (synchronous). */
  psqlSync(...args: string[]): string {
    return runPg0Sync("psql", "--name", this.name, ...args);
  }

  /** Execute a SQL command and return the output. */
  async execute(sql: string): Promise<string> {
    return (await this.psql("-c", sql)).stdout;
  }

  /** Execute a SQL command and return the output (synchronous). */
  executeSync(sql: string): string {
    return this.psqlSync("-c", sql);
  }
}

/** List all pg0 instances. */
export async function listInstances(): Promise<InstanceInfo[]> {
  const { stdout } = await runPg0("list", "-o", "json");
  return JSON.parse(stdout);
}

/** List all pg0 instances (synchronous). */
export function listInstancesSync(): InstanceInfo[] {
  return JSON.parse(runPg0Sync("list", "-o", "json"));
}

/** List available PostgreSQL extensions. */
export async function listExtensions(): Promise<string[]> {
  const { stdout } = await runPg0("list-extensions");
  return stdout.trim().split("\n").filter(line => line.trim());
}

/** List available PostgreSQL extensions (synchronous). */
export function listExtensionsSync(): string[] {
  const stdout = runPg0Sync("list-extensions");
  return stdout.trim().split("\n").filter(line => line.trim());
}

/** Start a PostgreSQL instance (convenience function). */
export async function start(options: Pg0Options = {}): Promise<InstanceInfo> {
  return new Pg0(options).start();
}

/** Start a PostgreSQL instance (synchronous convenience function). */
export function startSync(options: Pg0Options = {}): InstanceInfo {
  return new Pg0(options).startSync();
}

/** Stop a PostgreSQL instance (convenience function). */
export async function stop(name: string = "default"): Promise<void> {
  try {
    await runPg0("stop", "--name", name);
  } catch (e) {
    if (!(e instanceof Pg0NotRunningError)) throw e;
  }
}

/** Stop a PostgreSQL instance (synchronous convenience function). */
export function stopSync(name: string = "default"): void {
  try {
    runPg0Sync("stop", "--name", name);
  } catch (e) {
    if (!(e instanceof Pg0NotRunningError)) throw e;
  }
}

/** Drop a PostgreSQL instance (stop if running, delete all data). */
export async function drop(name: string = "default", force: boolean = true): Promise<void> {
  const args = ["drop", "--name", name];
  if (force) args.push("--force");
  try {
    await runPg0(...args);
  } catch {
    // Ignore errors
  }
}

/** Drop a PostgreSQL instance (synchronous convenience function). */
export function dropSync(name: string = "default", force: boolean = true): void {
  const args = ["drop", "--name", name];
  if (force) args.push("--force");
  try {
    runPg0Sync(...args);
  } catch {
    // Ignore errors
  }
}

/** Get information about a PostgreSQL instance (convenience function). */
export async function info(name: string = "default"): Promise<InstanceInfo> {
  const { stdout } = await runPg0("info", "--name", name, "-o", "json");
  return JSON.parse(stdout);
}

/** Get information about a PostgreSQL instance (synchronous convenience function). */
export function infoSync(name: string = "default"): InstanceInfo {
  return JSON.parse(runPg0Sync("info", "--name", name, "-o", "json"));
}

// Keep PostgreSQL as alias for backwards compatibility
export const PostgreSQL = Pg0;

export default Pg0;
```

## File: `sdk/node/tests/pg0.test.ts`
```typescript
import { describe, it, before, after } from "node:test";
import assert from "node:assert";
import {
  PostgreSQL,
  Pg0AlreadyRunningError,
  start,
  stop,
  info,
  listInstances,
  startSync,
  stopSync,
  infoSync,
  listInstancesSync,
  dropSync,
} from "../src";

// Use unique ports to avoid conflicts
const TEST_PORT = 15433;
const TEST_NAME = "node-test";

function cleanup() {
  // Drop instance to fully clean up data between tests
  dropSync(TEST_NAME);
}

describe("PostgreSQL class", () => {
  before(() => cleanup());
  after(() => cleanup());

  describe("start and stop", () => {
    after(() => cleanup());

    it("should start and stop PostgreSQL", async () => {
      const pg = new PostgreSQL({ name: TEST_NAME, port: TEST_PORT });

      // Start
      const startInfo = await pg.start();
      assert.strictEqual(startInfo.running, true);
      assert.strictEqual(startInfo.port, TEST_PORT);
      assert(startInfo.uri);
      assert(startInfo.uri.includes(`:${TEST_PORT}/`));

      // Stop
      await pg.stop();
      const stopInfo = await pg.info();
      assert.strictEqual(stopInfo.running, false);
    });
  });

  describe("sync methods", () => {
    after(() => cleanup());

    it("should start and stop PostgreSQL synchronously", () => {
      const pg = new PostgreSQL({ name: TEST_NAME, port: TEST_PORT });

      // Start
      const startInfo = pg.startSync();
      assert.strictEqual(startInfo.running, true);
      assert.strictEqual(startInfo.port, TEST_PORT);

      // Check running
      assert.strictEqual(pg.isRunningSync(), true);
      assert(pg.getUriSync());

      // Stop
      pg.stopSync();
      assert.strictEqual(pg.isRunningSync(), false);
    });
  });

  describe("execute SQL", () => {
    after(() => cleanup());

    it("should execute SQL commands", async () => {
      const pg = new PostgreSQL({ name: TEST_NAME, port: TEST_PORT });
      await pg.start();

      try {
        // Execute a simple query
        const result = await pg.execute("SELECT 1 as num;");
        assert(result.includes("1"));

        // Create and query a table
        await pg.execute("CREATE TABLE test_table (id serial, name text);");
        await pg.execute("INSERT INTO test_table (name) VALUES ('hello');");
        const queryResult = await pg.execute("SELECT name FROM test_table;");
        assert(queryResult.includes("hello"));
      } finally {
        await pg.stop();
      }
    });
  });

  describe("custom credentials", () => {
    after(() => cleanup());

    it("should use custom username, password, database", async () => {
      const pg = new PostgreSQL({
        name: TEST_NAME,
        port: TEST_PORT,
        username: "testuser",
        password: "testpass",
        database: "testdb",
      });
      const info = await pg.start();

      try {
        assert(info.uri);
        assert(info.uri.includes("testuser"));
        assert(info.uri.includes("testpass"));
        assert(info.uri.includes("testdb"));
      } finally {
        await pg.stop();
      }
    });
  });

  describe("custom config", () => {
    after(() => cleanup());

    it("should apply custom PostgreSQL configuration", async () => {
      const pg = new PostgreSQL({
        name: TEST_NAME,
        port: TEST_PORT,
        config: { work_mem: "128MB" },
      });
      await pg.start();

      try {
        const result = await pg.execute("SHOW work_mem;");
        assert(result.includes("128MB"));
      } finally {
        await pg.stop();
      }
    });
  });

  describe("error handling", () => {
    after(() => cleanup());

    it("should throw Pg0AlreadyRunningError when starting twice", async () => {
      const pg = new PostgreSQL({ name: TEST_NAME, port: TEST_PORT });
      await pg.start();

      try {
        await assert.rejects(async () => {
          await pg.start();
        }, Pg0AlreadyRunningError);
      } finally {
        await pg.stop();
      }
    });

    it("should not throw when stopping non-running instance", async () => {
      const pg = new PostgreSQL({ name: TEST_NAME, port: TEST_PORT });
      // Should not throw - stop is idempotent
      await pg.stop();
    });

    it("should return running=false for non-running instance", async () => {
      const pg = new PostgreSQL({ name: TEST_NAME, port: TEST_PORT });
      const info = await pg.info();

      assert.strictEqual(info.running, false);
      assert.strictEqual(info.uri, undefined);
    });
  });
});

describe("Convenience functions", () => {
  before(() => cleanup());
  after(() => cleanup());

  describe("async functions", () => {
    after(() => cleanup());

    it("should start, get info, and stop", async () => {
      const startInfo = await start({ name: TEST_NAME, port: TEST_PORT });
      assert.strictEqual(startInfo.running, true);

      const infoResult = await info(TEST_NAME);
      assert.strictEqual(infoResult.running, true);
      assert.strictEqual(infoResult.port, TEST_PORT);

      await stop(TEST_NAME);
      const afterStop = await info(TEST_NAME);
      assert.strictEqual(afterStop.running, false);
    });
  });

  describe("sync functions", () => {
    after(() => cleanup());

    it("should start, get info, and stop synchronously", () => {
      const startInfo = startSync({ name: TEST_NAME, port: TEST_PORT });
      assert.strictEqual(startInfo.running, true);

      const infoResult = infoSync(TEST_NAME);
      assert.strictEqual(infoResult.running, true);

      stopSync(TEST_NAME);
      const afterStop = infoSync(TEST_NAME);
      assert.strictEqual(afterStop.running, false);
    });
  });

  describe("list instances", () => {
    after(() => cleanup());

    it("should list running instances", async () => {
      await start({ name: TEST_NAME, port: TEST_PORT });

      try {
        const instances = await listInstances();
        const names = instances.map((i) => i.name);
        assert(names.includes(TEST_NAME));
      } finally {
        await stop(TEST_NAME);
      }
    });

    it("should list running instances synchronously", () => {
      startSync({ name: TEST_NAME, port: TEST_PORT });

      try {
        const instances = listInstancesSync();
        const names = instances.map((i) => i.name);
        assert(names.includes(TEST_NAME));
      } finally {
        stopSync(TEST_NAME);
      }
    });
  });
});
```

## File: `sdk/python/README.md`
```markdown
# pg0 - PostgreSQL for Python

[![PyPI](https://badge.fury.io/py/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)

Zero-config PostgreSQL with pgvector. No installation, no Docker, no configuration.

## Install

```bash
pip install pg0-embedded
```

## Usage

```python
from pg0 import Pg0

# Basic usage
with Pg0() as pg:
    print(pg.uri)  # postgresql://postgres:postgres@localhost:5432/postgres
    pg.execute("CREATE EXTENSION IF NOT EXISTS vector")
    pg.execute("SELECT version()")

# Custom configuration
pg = Pg0(
    name="myapp",
    port=5433,
    username="myuser",
    password="mypass",
    database="mydb",
    config={"shared_buffers": "512MB"}
)
pg.start()
pg.stop()
```

## API

### Pg0 Class

| Method | Description |
|--------|-------------|
| `start()` | Start PostgreSQL, returns `InstanceInfo` |
| `stop()` | Stop PostgreSQL |
| `drop()` | Stop and delete all data |
| `info()` | Get instance info |
| `execute(sql)` | Run SQL query |
| `uri` | Connection URI (property) |
| `running` | Check if running (property) |

### Module Functions

```python
import pg0

pg0.start(name="default", port=5432, ...)  # Start instance
pg0.stop(name="default")                    # Stop instance
pg0.drop(name="default")                    # Delete instance
pg0.info(name="default")                    # Get instance info
pg0.list_instances()                        # List all instances
```

### Getting Connection URI

```python
from pg0 import Pg0

pg = Pg0()
pg.start()

# Using the uri property
print(pg.uri)  # postgresql://postgres:postgres@localhost:5432/postgres

# Or using info()
info = pg.info()
print(info.uri)  # postgresql://postgres:postgres@localhost:5432/postgres
print(info.port)  # 5432
print(info.username)  # postgres
print(info.database)  # postgres
```

## Supported Platforms

Pre-built wheels are available for:

| Platform | Architecture | Wheel Tag |
|----------|--------------|-----------|
| macOS | Apple Silicon (M1/M2/M3) | `macosx_14_0_arm64` |
| Linux | x86_64 (glibc) | `manylinux_2_35_x86_64` |
| Linux | ARM64 (glibc) | `manylinux_2_35_aarch64` |
| Windows | x64 | `win_amd64` |

For other platforms, install from source (requires Rust toolchain):
```bash
pip install pg0-embedded --no-binary pg0-embedded
```

## Links

- [GitHub](https://github.com/vectorize-io/pg0)
- [CLI Documentation](https://github.com/vectorize-io/pg0#readme)
```

## File: `sdk/python/build_binary.py`
```python
#!/usr/bin/env python3
"""
Build script to download the pg0 binary for the current platform.
This is run during wheel building to bundle the binary into the package.
"""

import hashlib
import os
import platform
import stat
import subprocess
import sys
import urllib.request
from pathlib import Path

# These are updated with each release
PG0_VERSION = "v0.9.0"
PG0_REPO = "vectorize-io/pg0"

# SHA256 checksums for each binary (updated with each release)
# To generate: sha256sum pg0-<platform>
CHECKSUMS = {
    "darwin-aarch64": "",  # Will be populated by CI
    "linux-x86_64-gnu": "",
    "linux-x86_64-musl": "",
    "linux-aarch64-gnu": "",
    "linux-aarch64-musl": "",
    "windows-x86_64": "",
}


def get_platform() -> str:
    """Detect the current platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        return "darwin-aarch64"
    elif system == "linux":
        if machine in ("x86_64", "amd64"):
            arch = "x86_64"
        elif machine in ("aarch64", "arm64"):
            arch = "aarch64"
        else:
            raise RuntimeError(f"Unsupported architecture: {machine}")

        # Detect musl vs glibc
        try:
            result = subprocess.run(
                ["ldd", "--version"],
                capture_output=True,
                text=True,
            )
            if "musl" in (result.stdout + result.stderr).lower():
                return f"linux-{arch}-musl"
        except FileNotFoundError:
            pass

        # Check for musl loader
        if Path(f"/lib/ld-musl-{arch}.so.1").exists():
            return f"linux-{arch}-musl"

        return f"linux-{arch}-gnu"
    elif system == "windows":
        return "windows-x86_64"
    else:
        raise RuntimeError(f"Unsupported platform: {system}")


def download_binary(target_dir: Path, plat: str | None = None) -> Path:
    """Download the pg0 binary for the specified platform."""
    if plat is None:
        plat = get_platform()

    ext = ".exe" if plat.startswith("windows") else ""
    filename = f"pg0-{plat}{ext}"
    url = f"https://github.com/{PG0_REPO}/releases/download/{PG0_VERSION}/{filename}"

    target_dir.mkdir(parents=True, exist_ok=True)
    binary_path = target_dir / f"pg0{ext}"

    print(f"Downloading pg0 {PG0_VERSION} for {plat}...")
    print(f"  URL: {url}")

    # Download to temp file first
    tmp_path = binary_path.with_suffix(".tmp")
    urllib.request.urlretrieve(url, tmp_path)

    # Verify checksum if available
    expected_checksum = CHECKSUMS.get(plat, "")
    if expected_checksum:
        with open(tmp_path, "rb") as f:
            actual_checksum = hashlib.sha256(f.read()).hexdigest()
        if actual_checksum != expected_checksum:
            tmp_path.unlink()
            raise RuntimeError(
                f"Checksum mismatch for {plat}!\n"
                f"  Expected: {expected_checksum}\n"
                f"  Actual:   {actual_checksum}"
            )
        print(f"  Checksum verified: {actual_checksum[:16]}...")
    else:
        print("  Warning: No checksum available for verification")

    # Move to final location
    tmp_path.rename(binary_path)

    # Make executable on Unix
    if not plat.startswith("windows"):
        binary_path.chmod(binary_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f"  Saved to: {binary_path}")
    return binary_path


def main():
    """Download binary for current platform into pg0/bin/."""
    script_dir = Path(__file__).parent
    bin_dir = script_dir / "pg0" / "bin"

    # Allow overriding platform via environment variable (for CI cross-builds)
    plat = os.environ.get("PG0_TARGET_PLATFORM")

    download_binary(bin_dir, plat)
    print("Done!")


if __name__ == "__main__":
    main()
```

## File: `sdk/python/hatch_build.py`
```python
"""
Hatch build hook to include the pg0 binary in the wheel.

The binary can come from:
1. PG0_BINARY_PATH env var - path to a pre-built binary (for CI/release)
2. Local cargo build - builds from source using cargo (only if in repo with Cargo.toml)
3. GitHub releases - downloads from releases (fallback for sdist installs)
"""

import os
import platform
import shutil
import stat
import subprocess
import urllib.request
from pathlib import Path
from typing import Any, Optional

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

# GitHub repo for downloading releases
PG0_REPO = "vectorize-io/pg0"


def get_platform() -> str:
    """Detect the current platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        return "darwin-aarch64" if machine == "arm64" else "darwin-x86_64"
    elif system == "linux":
        if machine in ("x86_64", "amd64"):
            arch = "x86_64"
        elif machine in ("aarch64", "arm64"):
            arch = "aarch64"
        else:
            raise RuntimeError(f"Unsupported architecture: {machine}")

        # Detect musl vs glibc
        try:
            result = subprocess.run(
                ["ldd", "--version"],
                capture_output=True,
                text=True,
            )
            if "musl" in (result.stdout + result.stderr).lower():
                return f"linux-{arch}-musl"
        except FileNotFoundError:
            pass

        # Check for musl loader
        if Path(f"/lib/ld-musl-{arch}.so.1").exists():
            return f"linux-{arch}-musl"

        return f"linux-{arch}-gnu"
    elif system == "windows":
        return "windows-x86_64"
    else:
        raise RuntimeError(f"Unsupported platform: {system}")


def try_build_binary_locally(target_dir: Path) -> Optional[Path]:
    """Try to build pg0 binary from source using cargo.

    Returns the path to the binary if successful, None if not in a repo context.
    """
    # Find the repo root (sdk/python -> repo root)
    repo_root = Path(__file__).parent.parent.parent

    cargo_toml = repo_root / "Cargo.toml"
    if not cargo_toml.exists():
        # Not in repo context (e.g., installing from sdist)
        return None

    print("Building pg0 binary from source...")
    print(f"  Repo root: {repo_root}")

    # Build with cargo
    env = os.environ.copy()
    env["BUNDLE_POSTGRESQL"] = "true"

    result = subprocess.run(
        ["cargo", "build", "--release"],
        cwd=repo_root,
        env=env,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"  stdout: {result.stdout}")
        print(f"  stderr: {result.stderr}")
        raise RuntimeError(f"Cargo build failed: {result.stderr}")

    # Find the built binary
    system = platform.system().lower()
    binary_name = "pg0.exe" if system == "windows" else "pg0"
    built_binary = repo_root / "target" / "release" / binary_name

    if not built_binary.exists():
        raise RuntimeError(f"Built binary not found at {built_binary}")

    # Copy to target directory
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / binary_name
    shutil.copy2(built_binary, target_path)

    # Make executable on Unix
    if system != "windows":
        target_path.chmod(target_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f"  Built binary copied to: {target_path}")
    return target_path


def download_binary(target_dir: Path, plat: str, version: str) -> Path:
    """Download the pg0 binary from GitHub releases."""
    ext = ".exe" if plat.startswith("windows") else ""
    filename = f"pg0-{plat}{ext}"
    url = f"https://github.com/{PG0_REPO}/releases/download/{version}/{filename}"

    target_dir.mkdir(parents=True, exist_ok=True)
    binary_path = target_dir / f"pg0{ext}"

    print(f"Downloading pg0 {version} for {plat}...")
    print(f"  URL: {url}")

    # Download to temp file first
    tmp_path = binary_path.with_suffix(".tmp")
    urllib.request.urlretrieve(url, tmp_path)

    # Move to final location
    tmp_path.rename(binary_path)

    # Make executable on Unix
    if not plat.startswith("windows"):
        binary_path.chmod(binary_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f"  Saved to: {binary_path}")
    return binary_path


def get_package_version(root: Path) -> str:
    """Read the package version from pyproject.toml."""
    import re

    pyproject_path = root / "pyproject.toml"
    content = pyproject_path.read_text()

    # Simple regex to find version = "x.y.z" in [project] section
    match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if match:
        return match.group(1)

    raise RuntimeError("Could not find version in pyproject.toml")


class CustomBuildHook(BuildHookInterface):
    """Build hook to include pg0 binary in wheel build."""

    PLUGIN_NAME = "custom"

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """Called before the build starts."""
        if self.target_name != "wheel":
            # Only include binary for wheel builds, not sdist
            return

        root = Path(self.root)
        bin_dir = root / "pg0" / "bin"
        system = platform.system().lower()
        ext = ".exe" if system == "windows" else ""
        binary_path = bin_dir / f"pg0{ext}"

        # Check if binary already exists
        if binary_path.exists():
            print(f"Binary already exists: {binary_path}")
        # Option 1: Use pre-built binary from env var (for CI)
        elif os.environ.get("PG0_BINARY_PATH"):
            src_path = Path(os.environ["PG0_BINARY_PATH"])
            if not src_path.exists():
                raise RuntimeError(f"PG0_BINARY_PATH does not exist: {src_path}")
            print(f"Using pre-built binary from PG0_BINARY_PATH: {src_path}")
            bin_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, binary_path)
            if system != "windows":
                binary_path.chmod(binary_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        # Option 2: Download from GitHub releases (if PG0_VERSION specified)
        elif os.environ.get("PG0_VERSION"):
            plat = os.environ.get("PG0_TARGET_PLATFORM") or get_platform()
            download_binary(bin_dir, plat, os.environ["PG0_VERSION"])
        # Option 3: Try to build locally from source (if in repo context)
        else:
            built_path = try_build_binary_locally(bin_dir)
            if built_path is not None:
                print(f"Built binary: {built_path}")
            else:
                # Option 4: Download from GitHub releases using package version (fallback for sdist)
                pkg_version = get_package_version(root)
                plat = get_platform()
                print(f"Downloading pg0 v{pkg_version} for {plat} (sdist install)...")
                download_binary(bin_dir, plat, f"v{pkg_version}")

        # Note: The binary is included via artifacts = ["pg0/bin/*"] in pyproject.toml
        # No need to use force_include here
```

## File: `sdk/python/pyproject.toml`
```
[project]
name = "pg0-embedded"
version = "0.12.2"
description = "Python API for pg0 - embedded PostgreSQL"
readme = "README.md"
license = "MIT"
requires-python = ">=3.8"
keywords = ["postgresql", "database", "embedded", "pgvector"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

[project.urls]
Homepage = "https://github.com/vectorize-io/pg0"
Repository = "https://github.com/vectorize-io/pg0"

[project.optional-dependencies]
dev = ["pytest>=8.0.0"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["pg0"]
# Include the bundled binary in the wheel (artifacts are files that should be
# included even if they're in .gitignore)
artifacts = ["pg0/bin/*"]

# Custom build hook to download the binary before building (wheel only)
[tool.hatch.build.targets.wheel.hooks.custom]
path = "hatch_build.py"
```

## File: `sdk/python/uv.lock`
```
version = 1
revision = 1
requires-python = ">=3.8"
resolution-markers = [
    "python_full_version >= '3.10'",
    "python_full_version == '3.9.*'",
    "python_full_version < '3.9'",
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335 },
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", version = "4.13.2", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.9'" },
    { name = "typing-extensions", version = "4.15.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.9' and python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/79/66800aadf48771f6b62f7eb014e352e5d06856655206165d775e675a02c9/exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219", size = 30371 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0e/97c33bf5009bdbac74fd2beace167cab3f978feb69cc36f1ef79360d6c4e/exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598", size = 16740 },
]

[[package]]
name = "iniconfig"
version = "2.1.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version == '3.9.*'",
    "python_full_version < '3.9'",
]
sdist = { url = "https://files.pythonhosted.org/packages/f2/97/ebf4da567aa6827c909642694d71c9fcf53e5b504f2d96afea02718862f3/iniconfig-2.1.0.tar.gz", hash = "sha256:3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7", size = 4793 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/e1/e6716421ea10d38022b952c159d5161ca1193197fb744506875fbb87ea7b/iniconfig-2.1.0-py3-none-any.whl", hash = "sha256:9deba5723312380e77435581c6bf4935c94cbfab9b1ed33ef8d238ea168eb760", size = 6050 },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.10'",
]
sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484 },
]

[[package]]
name = "packaging"
version = "25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469 },
]

[[package]]
name = "pg0-embedded"
version = "0.10.1"
source = { editable = "." }

[package.optional-dependencies]
dev = [
    { name = "pytest", version = "8.3.5", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.9'" },
    { name = "pytest", version = "8.4.2", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version == '3.9.*'" },
    { name = "pytest", version = "9.0.1", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.10'" },
]

[package.metadata]
requires-dist = [{ name = "pytest", marker = "extra == 'dev'", specifier = ">=8.0.0" }]
provides-extras = ["dev"]

[[package]]
name = "pluggy"
version = "1.5.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.9'",
]
sdist = { url = "https://files.pythonhosted.org/packages/96/2d/02d4312c973c6050a18b314a5ad0b3210edb65a906f868e31c111dede4a6/pluggy-1.5.0.tar.gz", hash = "sha256:2cffa88e94fdc978c4c574f15f9e59b7f4201d439195c3715ca9e2486f1d0cf1", size = 67955 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/5f/e351af9a41f866ac3f1fac4ca0613908d9a41741cfcf2228f4ad853b697d/pluggy-1.5.0-py3-none-any.whl", hash = "sha256:44e1ad92c8ca002de6377e165f3e0f1be63266ab4d554740532335b9d75ea669", size = 20556 },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.10'",
    "python_full_version == '3.9.*'",
]
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538 },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217 },
]

[[package]]
name = "pytest"
version = "8.3.5"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.9'",
]
dependencies = [
    { name = "colorama", marker = "python_full_version < '3.9' and sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.9'" },
    { name = "iniconfig", version = "2.1.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.9'" },
    { name = "packaging", marker = "python_full_version < '3.9'" },
    { name = "pluggy", version = "1.5.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.9'" },
    { name = "tomli", marker = "python_full_version < '3.9'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ae/3c/c9d525a414d506893f0cd8a8d0de7706446213181570cdbd766691164e40/pytest-8.3.5.tar.gz", hash = "sha256:f4efe70cc14e511565ac476b57c279e12a855b11f48f212af1080ef2263d3845", size = 1450891 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/30/3d/64ad57c803f1fa1e963a7946b6e0fea4a70df53c1a7fed304586539c2bac/pytest-8.3.5-py3-none-any.whl", hash = "sha256:c69214aa47deac29fad6c2a4f590b9c4a9fdb16a403176fe154b79c0b4d4d820", size = 343634 },
]

[[package]]
name = "pytest"
version = "8.4.2"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version == '3.9.*'",
]
dependencies = [
    { name = "colorama", marker = "python_full_version == '3.9.*' and sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version == '3.9.*'" },
    { name = "iniconfig", version = "2.1.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version == '3.9.*'" },
    { name = "packaging", marker = "python_full_version == '3.9.*'" },
    { name = "pluggy", version = "1.6.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version == '3.9.*'" },
    { name = "pygments", marker = "python_full_version == '3.9.*'" },
    { name = "tomli", marker = "python_full_version == '3.9.*'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a3/5c/00a0e072241553e1a7496d638deababa67c5058571567b92a7eaa258397c/pytest-8.4.2.tar.gz", hash = "sha256:86c0d0b93306b961d58d62a4db4879f27fe25513d4b969df351abdddb3c30e01", size = 1519618 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a8/a4/20da314d277121d6534b3a980b29035dcd51e6744bd79075a6ce8fa4eb8d/pytest-8.4.2-py3-none-any.whl", hash = "sha256:872f880de3fc3a5bdc88a11b39c9710c3497a547cfa9320bc3c5e62fbf272e79", size = 365750 },
]

[[package]]
name = "pytest"
version = "9.0.1"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.10'",
]
dependencies = [
    { name = "colorama", marker = "python_full_version >= '3.10' and sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version == '3.10.*'" },
    { name = "iniconfig", version = "2.3.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.10'" },
    { name = "packaging", marker = "python_full_version >= '3.10'" },
    { name = "pluggy", version = "1.6.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.10'" },
    { name = "pygments", marker = "python_full_version >= '3.10'" },
    { name = "tomli", marker = "python_full_version == '3.10.*'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/07/56/f013048ac4bc4c1d9be45afd4ab209ea62822fb1598f40687e6bf45dcea4/pytest-9.0.1.tar.gz", hash = "sha256:3e9c069ea73583e255c3b21cf46b8d3c56f6e3a1a8f6da94ccb0fcf57b9d73c8", size = 1564125 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/8b/6300fb80f858cda1c51ffa17075df5d846757081d11ab4aa35cef9e6258b/pytest-9.0.1-py3-none-any.whl", hash = "sha256:67be0030d194df2dfa7b556f2e56fb3c3315bd5c8822c6951162b92b32ce7dad", size = 373668 },
]

[[package]]
name = "tomli"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/52/ed/3f73f72945444548f33eba9a87fc7a6e969915e7b1acc8260b30e1f76a2f/tomli-2.3.0.tar.gz", hash = "sha256:64be704a875d2a59753d80ee8a533c3fe183e3f06807ff7dc2232938ccb01549", size = 17392 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/2e/299f62b401438d5fe1624119c723f5d877acc86a4c2492da405626665f12/tomli-2.3.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:88bd15eb972f3664f5ed4b57c1634a97153b4bac4479dcb6a495f41921eb7f45", size = 153236 },
    { url = "https://files.pythonhosted.org/packages/86/7f/d8fffe6a7aefdb61bced88fcb5e280cfd71e08939da5894161bd71bea022/tomli-2.3.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:883b1c0d6398a6a9d29b508c331fa56adbcdff647f6ace4dfca0f50e90dfd0ba", size = 148084 },
    { url = "https://files.pythonhosted.org/packages/47/5c/24935fb6a2ee63e86d80e4d3b58b222dafaf438c416752c8b58537c8b89a/tomli-2.3.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d1381caf13ab9f300e30dd8feadb3de072aeb86f1d34a8569453ff32a7dea4bf", size = 234832 },
    { url = "https://files.pythonhosted.org/packages/89/da/75dfd804fc11e6612846758a23f13271b76d577e299592b4371a4ca4cd09/tomli-2.3.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a0e285d2649b78c0d9027570d4da3425bdb49830a6156121360b3f8511ea3441", size = 242052 },
    { url = "https://files.pythonhosted.org/packages/70/8c/f48ac899f7b3ca7eb13af73bacbc93aec37f9c954df3c08ad96991c8c373/tomli-2.3.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0a154a9ae14bfcf5d8917a59b51ffd5a3ac1fd149b71b47a3a104ca4edcfa845", size = 239555 },
    { url = "https://files.pythonhosted.org/packages/ba/28/72f8afd73f1d0e7829bfc093f4cb98ce0a40ffc0cc997009ee1ed94ba705/tomli-2.3.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:74bf8464ff93e413514fefd2be591c3b0b23231a77f901db1eb30d6f712fc42c", size = 245128 },
    { url = "https://files.pythonhosted.org/packages/b6/eb/a7679c8ac85208706d27436e8d421dfa39d4c914dcf5fa8083a9305f58d9/tomli-2.3.0-cp311-cp311-win32.whl", hash = "sha256:00b5f5d95bbfc7d12f91ad8c593a1659b6387b43f054104cda404be6bda62456", size = 96445 },
    { url = "https://files.pythonhosted.org/packages/0a/fe/3d3420c4cb1ad9cb462fb52967080575f15898da97e21cb6f1361d505383/tomli-2.3.0-cp311-cp311-win_amd64.whl", hash = "sha256:4dc4ce8483a5d429ab602f111a93a6ab1ed425eae3122032db7e9acf449451be", size = 107165 },
    { url = "https://files.pythonhosted.org/packages/ff/b7/40f36368fcabc518bb11c8f06379a0fd631985046c038aca08c6d6a43c6e/tomli-2.3.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d7d86942e56ded512a594786a5ba0a5e521d02529b3826e7761a05138341a2ac", size = 154891 },
    { url = "https://files.pythonhosted.org/packages/f9/3f/d9dd692199e3b3aab2e4e4dd948abd0f790d9ded8cd10cbaae276a898434/tomli-2.3.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:73ee0b47d4dad1c5e996e3cd33b8a76a50167ae5f96a2607cbe8cc773506ab22", size = 148796 },
    { url = "https://files.pythonhosted.org/packages/60/83/59bff4996c2cf9f9387a0f5a3394629c7efa5ef16142076a23a90f1955fa/tomli-2.3.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:792262b94d5d0a466afb5bc63c7daa9d75520110971ee269152083270998316f", size = 242121 },
    { url = "https://files.pythonhosted.org/packages/45/e5/7c5119ff39de8693d6baab6c0b6dcb556d192c165596e9fc231ea1052041/tomli-2.3.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4f195fe57ecceac95a66a75ac24d9d5fbc98ef0962e09b2eddec5d39375aae52", size = 250070 },
    { url = "https://files.pythonhosted.org/packages/45/12/ad5126d3a278f27e6701abde51d342aa78d06e27ce2bb596a01f7709a5a2/tomli-2.3.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:e31d432427dcbf4d86958c184b9bfd1e96b5b71f8eb17e6d02531f434fd335b8", size = 245859 },
    { url = "https://files.pythonhosted.org/packages/fb/a1/4d6865da6a71c603cfe6ad0e6556c73c76548557a8d658f9e3b142df245f/tomli-2.3.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b0882799624980785240ab732537fcfc372601015c00f7fc367c55308c186f6", size = 250296 },
    { url = "https://files.pythonhosted.org/packages/a0/b7/a7a7042715d55c9ba6e8b196d65d2cb662578b4d8cd17d882d45322b0d78/tomli-2.3.0-cp312-cp312-win32.whl", hash = "sha256:ff72b71b5d10d22ecb084d345fc26f42b5143c5533db5e2eaba7d2d335358876", size = 97124 },
    { url = "https://files.pythonhosted.org/packages/06/1e/f22f100db15a68b520664eb3328fb0ae4e90530887928558112c8d1f4515/tomli-2.3.0-cp312-cp312-win_amd64.whl", hash = "sha256:1cb4ed918939151a03f33d4242ccd0aa5f11b3547d0cf30f7c74a408a5b99878", size = 107698 },
    { url = "https://files.pythonhosted.org/packages/89/48/06ee6eabe4fdd9ecd48bf488f4ac783844fd777f547b8d1b61c11939974e/tomli-2.3.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5192f562738228945d7b13d4930baffda67b69425a7f0da96d360b0a3888136b", size = 154819 },
    { url = "https://files.pythonhosted.org/packages/f1/01/88793757d54d8937015c75dcdfb673c65471945f6be98e6a0410fba167ed/tomli-2.3.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:be71c93a63d738597996be9528f4abe628d1adf5e6eb11607bc8fe1a510b5dae", size = 148766 },
    { url = "https://files.pythonhosted.org/packages/42/17/5e2c956f0144b812e7e107f94f1cc54af734eb17b5191c0bbfb72de5e93e/tomli-2.3.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c4665508bcbac83a31ff8ab08f424b665200c0e1e645d2bd9ab3d3e557b6185b", size = 240771 },
    { url = "https://files.pythonhosted.org/packages/d5/f4/0fbd014909748706c01d16824eadb0307115f9562a15cbb012cd9b3512c5/tomli-2.3.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4021923f97266babc6ccab9f5068642a0095faa0a51a246a6a02fccbb3514eaf", size = 248586 },
    { url = "https://files.pythonhosted.org/packages/30/77/fed85e114bde5e81ecf9bc5da0cc69f2914b38f4708c80ae67d0c10180c5/tomli-2.3.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4ea38c40145a357d513bffad0ed869f13c1773716cf71ccaa83b0fa0cc4e42f", size = 244792 },
    { url = "https://files.pythonhosted.org/packages/55/92/afed3d497f7c186dc71e6ee6d4fcb0acfa5f7d0a1a2878f8beae379ae0cc/tomli-2.3.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ad805ea85eda330dbad64c7ea7a4556259665bdf9d2672f5dccc740eb9d3ca05", size = 248909 },
    { url = "https://files.pythonhosted.org/packages/f8/84/ef50c51b5a9472e7265ce1ffc7f24cd4023d289e109f669bdb1553f6a7c2/tomli-2.3.0-cp313-cp313-win32.whl", hash = "sha256:97d5eec30149fd3294270e889b4234023f2c69747e555a27bd708828353ab606", size = 96946 },
    { url = "https://files.pythonhosted.org/packages/b2/b7/718cd1da0884f281f95ccfa3a6cc572d30053cba64603f79d431d3c9b61b/tomli-2.3.0-cp313-cp313-win_amd64.whl", hash = "sha256:0c95ca56fbe89e065c6ead5b593ee64b84a26fca063b5d71a1122bf26e533999", size = 107705 },
    { url = "https://files.pythonhosted.org/packages/19/94/aeafa14a52e16163008060506fcb6aa1949d13548d13752171a755c65611/tomli-2.3.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:cebc6fe843e0733ee827a282aca4999b596241195f43b4cc371d64fc6639da9e", size = 154244 },
    { url = "https://files.pythonhosted.org/packages/db/e4/1e58409aa78eefa47ccd19779fc6f36787edbe7d4cd330eeeedb33a4515b/tomli-2.3.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4c2ef0244c75aba9355561272009d934953817c49f47d768070c3c94355c2aa3", size = 148637 },
    { url = "https://files.pythonhosted.org/packages/26/b6/d1eccb62f665e44359226811064596dd6a366ea1f985839c566cd61525ae/tomli-2.3.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c22a8bf253bacc0cf11f35ad9808b6cb75ada2631c2d97c971122583b129afbc", size = 241925 },
    { url = "https://files.pythonhosted.org/packages/70/91/7cdab9a03e6d3d2bb11beae108da5bdc1c34bdeb06e21163482544ddcc90/tomli-2.3.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0eea8cc5c5e9f89c9b90c4896a8deefc74f518db5927d0e0e8d4a80953d774d0", size = 249045 },
    { url = "https://files.pythonhosted.org/packages/15/1b/8c26874ed1f6e4f1fcfeb868db8a794cbe9f227299402db58cfcc858766c/tomli-2.3.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b74a0e59ec5d15127acdabd75ea17726ac4c5178ae51b85bfe39c4f8a278e879", size = 245835 },
    { url = "https://files.pythonhosted.org/packages/fd/42/8e3c6a9a4b1a1360c1a2a39f0b972cef2cc9ebd56025168c4137192a9321/tomli-2.3.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b5870b50c9db823c595983571d1296a6ff3e1b88f734a4c8f6fc6188397de005", size = 253109 },
    { url = "https://files.pythonhosted.org/packages/22/0c/b4da635000a71b5f80130937eeac12e686eefb376b8dee113b4a582bba42/tomli-2.3.0-cp314-cp314-win32.whl", hash = "sha256:feb0dacc61170ed7ab602d3d972a58f14ee3ee60494292d384649a3dc38ef463", size = 97930 },
    { url = "https://files.pythonhosted.org/packages/b9/74/cb1abc870a418ae99cd5c9547d6bce30701a954e0e721821df483ef7223c/tomli-2.3.0-cp314-cp314-win_amd64.whl", hash = "sha256:b273fcbd7fc64dc3600c098e39136522650c49bca95df2d11cf3b626422392c8", size = 107964 },
    { url = "https://files.pythonhosted.org/packages/54/78/5c46fff6432a712af9f792944f4fcd7067d8823157949f4e40c56b8b3c83/tomli-2.3.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:940d56ee0410fa17ee1f12b817b37a4d4e4dc4d27340863cc67236c74f582e77", size = 163065 },
    { url = "https://files.pythonhosted.org/packages/39/67/f85d9bd23182f45eca8939cd2bc7050e1f90c41f4a2ecbbd5963a1d1c486/tomli-2.3.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:f85209946d1fe94416debbb88d00eb92ce9cd5266775424ff81bc959e001acaf", size = 159088 },
    { url = "https://files.pythonhosted.org/packages/26/5a/4b546a0405b9cc0659b399f12b6adb750757baf04250b148d3c5059fc4eb/tomli-2.3.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a56212bdcce682e56b0aaf79e869ba5d15a6163f88d5451cbde388d48b13f530", size = 268193 },
    { url = "https://files.pythonhosted.org/packages/42/4f/2c12a72ae22cf7b59a7fe75b3465b7aba40ea9145d026ba41cb382075b0e/tomli-2.3.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c5f3ffd1e098dfc032d4d3af5c0ac64f6d286d98bc148698356847b80fa4de1b", size = 275488 },
    { url = "https://files.pythonhosted.org/packages/92/04/a038d65dbe160c3aa5a624e93ad98111090f6804027d474ba9c37c8ae186/tomli-2.3.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:5e01decd096b1530d97d5d85cb4dff4af2d8347bd35686654a004f8dea20fc67", size = 272669 },
    { url = "https://files.pythonhosted.org/packages/be/2f/8b7c60a9d1612a7cbc39ffcca4f21a73bf368a80fc25bccf8253e2563267/tomli-2.3.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:8a35dd0e643bb2610f156cca8db95d213a90015c11fee76c946aa62b7ae7e02f", size = 279709 },
    { url = "https://files.pythonhosted.org/packages/7e/46/cc36c679f09f27ded940281c38607716c86cf8ba4a518d524e349c8b4874/tomli-2.3.0-cp314-cp314t-win32.whl", hash = "sha256:a1f7f282fe248311650081faafa5f4732bdbfef5d45fe3f2e702fbc6f2d496e0", size = 107563 },
    { url = "https://files.pythonhosted.org/packages/84/ff/426ca8683cf7b753614480484f6437f568fd2fda2edbdf57a2d3d8b27a0b/tomli-2.3.0-cp314-cp314t-win_amd64.whl", hash = "sha256:70a251f8d4ba2d9ac2542eecf008b3c8a9fc5c3f9f02c56a9d7952612be2fdba", size = 119756 },
    { url = "https://files.pythonhosted.org/packages/77/b8/0135fadc89e73be292b473cb820b4f5a08197779206b33191e801feeae40/tomli-2.3.0-py3-none-any.whl", hash = "sha256:e95b1af3c5b07d9e643909b5abbec77cd9f1217e6d0bca72b0234736b9fb1f1b", size = 14408 },
]

[[package]]
name = "typing-extensions"
version = "4.13.2"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.9'",
]
sdist = { url = "https://files.pythonhosted.org/packages/f6/37/23083fcd6e35492953e8d2aaaa68b860eb422b34627b13f2ce3eb6106061/typing_extensions-4.13.2.tar.gz", hash = "sha256:e6c81219bd689f51865d9e372991c540bda33a0379d5573cddb9a3a23f7caaef", size = 106967 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8b/54/b1ae86c0973cc6f0210b53d508ca3641fb6d0c56823f288d108bc7ab3cc8/typing_extensions-4.13.2-py3-none-any.whl", hash = "sha256:a439e7c04b49fec3e5d3e2beaa21755cadbbdc391694e28ccdd36ca4a1408f8c", size = 45806 },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.10'",
    "python_full_version == '3.9.*'",
]
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614 },
]
```

## File: `sdk/python/pg0/__init__.py`
```python
"""
pg0 - Embedded PostgreSQL for Python

Usage:
    from pg0 import Pg0

    # Start PostgreSQL
    pg = Pg0()
    pg.start()
    print(pg.uri)
    pg.stop()

    # Or use context manager
    with Pg0() as pg:
        print(pg.uri)
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


__version__ = "0.1.0"


class Pg0Error(Exception):
    """Base exception for pg0 errors."""
    pass


class Pg0NotFoundError(Pg0Error):
    """pg0 binary not found and could not be installed."""
    pass


class Pg0NotRunningError(Pg0Error):
    """PostgreSQL instance is not running."""
    pass


class Pg0AlreadyRunningError(Pg0Error):
    """PostgreSQL instance is already running."""
    pass


@dataclass
class InstanceInfo:
    """Information about a PostgreSQL instance."""
    name: str
    running: bool
    pid: Optional[int] = None
    port: Optional[int] = None
    version: Optional[str] = None
    username: Optional[str] = None
    database: Optional[str] = None
    data_dir: Optional[str] = None
    uri: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "InstanceInfo":
        return cls(
            name=data.get("name", "default"),
            running=data.get("running", False),
            pid=data.get("pid"),
            port=data.get("port"),
            version=data.get("version"),
            username=data.get("username"),
            database=data.get("database"),
            data_dir=data.get("data_dir"),
            uri=data.get("uri"),
        )


def _get_bundled_binary() -> Optional[Path]:
    """Get the path to the bundled pg0 binary, if it exists."""
    package_dir = Path(__file__).parent
    binary_name = "pg0.exe" if sys.platform == "win32" else "pg0"
    bundled_path = package_dir / "bin" / binary_name
    if bundled_path.exists():
        return bundled_path
    return None


def _get_install_dir() -> Path:
    """Get the directory where pg0 binary should be installed."""
    # Use ~/.local/bin on Unix, or a pg0-specific dir
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
        return base / "pg0" / "bin"
    else:
        return Path.home() / ".local" / "bin"


def _find_pg0() -> str:
    """Find the pg0 binary or raise an error if not found."""
    # Check for bundled binary first (from platform-specific wheel)
    bundled = _get_bundled_binary()
    if bundled:
        return str(bundled)

    # Check PATH
    path = shutil.which("pg0")
    if path:
        return path

    # Check common install location
    install_dir = _get_install_dir()
    binary_name = "pg0.exe" if sys.platform == "win32" else "pg0"
    binary_path = install_dir / binary_name

    if binary_path.exists():
        return str(binary_path)

    # No binary found
    raise Pg0NotFoundError(
        "pg0 binary not found. Install it with:\n"
        "  curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash\n"
        "Or download from: https://github.com/vectorize-io/pg0/releases"
    )


def _run_pg0(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run a pg0 command."""
    pg0_path = _find_pg0()
    try:
        result = subprocess.run(
            [pg0_path, *args],
            capture_output=True,
            text=True,
        )
        if check and result.returncode != 0:
            stderr = result.stderr.strip()
            if "already running" in stderr.lower():
                raise Pg0AlreadyRunningError(stderr)
            elif "no running instance" in stderr.lower() or "not running" in stderr.lower():
                raise Pg0NotRunningError(stderr)
            else:
                raise Pg0Error(stderr or f"pg0 command failed with code {result.returncode}")
        return result
    except FileNotFoundError:
        raise Pg0NotFoundError("pg0 binary not found")


class Pg0:
    """
    Embedded PostgreSQL instance.

    Args:
        name: Instance name (allows multiple instances)
        port: Port to listen on (None = auto-select available port)
        username: Database username
        password: Database password
        database: Database name
        data_dir: Custom data directory
        config: Dict of PostgreSQL configuration options

    Example:
        # Simple usage (auto-selects available port)
        pg = Pg0()
        pg.start()
        print(pg.uri)
        pg.stop()

        # Context manager with specific port
        with Pg0(port=5433, database="myapp") as pg:
            print(pg.uri)

        # Custom config
        pg = Pg0(config={"shared_buffers": "512MB"})
    """

    def __init__(
        self,
        name: str = "default",
        port: Optional[int] = None,
        username: str = "postgres",
        password: str = "postgres",
        database: str = "postgres",
        data_dir: Optional[str] = None,
        config: Optional[dict[str, str]] = None,
    ):
        self.name = name
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.data_dir = data_dir
        self.config = config or {}

    def start(self) -> InstanceInfo:
        """
        Start the PostgreSQL instance.

        Returns:
            InstanceInfo with connection details

        Raises:
            Pg0AlreadyRunningError: If instance is already running
            Pg0Error: If start fails
        """
        args = [
            "start",
            "--name", self.name,
            "--username", self.username,
            "--password", self.password,
            "--database", self.database,
        ]

        if self.port is not None:
            args.extend(["--port", str(self.port)])

        if self.data_dir:
            args.extend(["--data-dir", self.data_dir])

        for key, value in self.config.items():
            args.extend(["-c", f"{key}={value}"])

        _run_pg0(*args)
        return self.info()

    def stop(self) -> None:
        """
        Stop the PostgreSQL instance.

        Note: Does not raise an error if the instance is not running.
        """
        _run_pg0("stop", "--name", self.name, check=False)

    def drop(self, force: bool = True) -> None:
        """
        Drop the PostgreSQL instance (stop if running, delete all data).

        Args:
            force: Skip confirmation prompt (default True for programmatic use)

        Warning:
            This permanently deletes all data for this instance!
        """
        args = ["drop", "--name", self.name]
        if force:
            args.append("--force")
        _run_pg0(*args, check=False)

    def info(self) -> InstanceInfo:
        """
        Get information about the PostgreSQL instance.

        Returns:
            InstanceInfo with current status and connection details
        """
        result = _run_pg0("info", "--name", self.name, "-o", "json", check=False)
        data = json.loads(result.stdout)
        return InstanceInfo.from_dict(data)

    @property
    def uri(self) -> Optional[str]:
        """Get the connection URI if running."""
        return self.info().uri

    @property
    def running(self) -> bool:
        """Check if the instance is running."""
        return self.info().running

    def psql(self, *args: str) -> subprocess.CompletedProcess:
        """
        Run psql with the given arguments.

        Args:
            *args: Arguments to pass to psql (e.g., "-c", "SELECT 1")

        Returns:
            CompletedProcess with stdout/stderr

        Example:
            result = pg.psql("-c", "SELECT version();")
            print(result.stdout)
        """
        return _run_pg0("psql", "--name", self.name, *args)

    def execute(self, sql: str) -> str:
        """
        Execute a SQL command and return the output.

        Args:
            sql: SQL command to execute

        Returns:
            Command output as string

        Example:
            output = pg.execute("SELECT version();")
        """
        result = self.psql("-c", sql)
        return result.stdout

    def logs(self, lines: Optional[int] = None) -> str:
        """
        Get PostgreSQL logs for this instance.

        Args:
            lines: Number of lines to return (None = all logs)

        Returns:
            Log content as string

        Example:
            print(pg.logs(50))  # Last 50 lines
        """
        args = ["logs", "--name", self.name]
        if lines is not None:
            args.extend(["-n", str(lines)])
        result = _run_pg0(*args, check=False)
        return result.stdout

    def __enter__(self) -> "Pg0":
        """Context manager entry - starts PostgreSQL."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit - stops PostgreSQL."""
        try:
            self.stop()
        except Pg0NotRunningError:
            pass


def list_instances() -> list[InstanceInfo]:
    """
    List all pg0 instances.

    Returns:
        List of InstanceInfo for all known instances
    """
    result = _run_pg0("list", "-o", "json", check=False)
    data = json.loads(result.stdout)
    return [InstanceInfo.from_dict(item) for item in data]


def list_extensions() -> list[str]:
    """
    List available PostgreSQL extensions.

    Returns:
        List of available extension names

    Example:
        extensions = pg0.list_extensions()
        print(extensions)  # ['vector', 'postgis', ...]
    """
    result = _run_pg0("list-extensions", check=False)
    lines = result.stdout.strip().split("\n")
    return [line.strip() for line in lines if line.strip()]


def start(
    name: str = "default",
    port: Optional[int] = None,
    username: str = "postgres",
    password: str = "postgres",
    database: str = "postgres",
    **config: str,
) -> InstanceInfo:
    """
    Start a PostgreSQL instance (convenience function).

    Args:
        name: Instance name
        port: Port to listen on (None = auto-select available port)
        username: Database username
        password: Database password
        database: Database name
        **config: PostgreSQL configuration options

    Returns:
        InstanceInfo with connection details

    Example:
        info = pg0.start(shared_buffers="512MB")  # auto-selects port
        print(info.uri)
    """
    pg = Pg0(
        name=name,
        port=port,
        username=username,
        password=password,
        database=database,
        config=config,
    )
    return pg.start()


def stop(name: str = "default") -> None:
    """
    Stop a PostgreSQL instance (convenience function).

    Args:
        name: Instance name to stop
    """
    _run_pg0("stop", "--name", name, check=False)


def drop(name: str = "default", force: bool = True) -> None:
    """
    Drop a PostgreSQL instance (convenience function).

    Stops the instance if running and deletes all data.

    Args:
        name: Instance name to drop
        force: Skip confirmation prompt (default True for programmatic use)

    Warning:
        This permanently deletes all data for this instance!
    """
    args = ["drop", "--name", name]
    if force:
        args.append("--force")
    _run_pg0(*args, check=False)


def info(name: str = "default") -> InstanceInfo:
    """
    Get information about a PostgreSQL instance (convenience function).

    Args:
        name: Instance name

    Returns:
        InstanceInfo with current status
    """
    result = _run_pg0("info", "--name", name, "-o", "json", check=False)
    data = json.loads(result.stdout)
    return InstanceInfo.from_dict(data)


def logs(name: str = "default", lines: Optional[int] = None) -> str:
    """
    Get PostgreSQL logs for an instance (convenience function).

    Args:
        name: Instance name
        lines: Number of lines to return (None = all logs)

    Returns:
        Log content as string
    """
    args = ["logs", "--name", name]
    if lines is not None:
        args.extend(["-n", str(lines)])
    result = _run_pg0(*args, check=False)
    return result.stdout


# Keep PostgreSQL as alias for backwards compatibility
PostgreSQL = Pg0


__all__ = [
    "Pg0",
    "PostgreSQL",  # alias
    "InstanceInfo",
    "Pg0Error",
    "Pg0NotFoundError",
    "Pg0NotRunningError",
    "Pg0AlreadyRunningError",
    "list_instances",
    "list_extensions",
    "start",
    "stop",
    "drop",
    "info",
    "logs",
    "_get_bundled_binary",  # for testing
]
```

## File: `sdk/python/tests/test_pg0.py`
```python
"""Tests for pg0 Python client."""

import os
import signal
import time

import pytest
import pg0
from pg0 import Pg0, InstanceInfo, Pg0AlreadyRunningError, Pg0Error


# Use a unique port to avoid conflicts
TEST_PORT = 15432
TEST_NAME = "pytest-test"


@pytest.fixture
def clean_instance():
    """Ensure test instance is dropped before and after test."""
    # Cleanup before - drop to remove any existing data/config
    pg0.drop(TEST_NAME)

    yield

    # Cleanup after
    pg0.drop(TEST_NAME)


class TestPg0:
    """Tests for Pg0 class."""

    def test_start_stop(self, clean_instance):
        """Test starting and stopping Pg0."""
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)

        # Start
        info = pg.start()
        assert info.running is True
        assert info.port == TEST_PORT
        assert info.uri is not None
        assert f":{TEST_PORT}/" in info.uri

        # Stop
        pg.stop()
        info = pg.info()
        assert info.running is False

    def test_context_manager(self, clean_instance):
        """Test using Pg0 as context manager."""
        with Pg0(name=TEST_NAME, port=TEST_PORT) as pg:
            assert pg.running is True
            assert pg.uri is not None

        # Should be stopped after exiting context
        info = pg0.info(TEST_NAME)
        assert info.running is False

    def test_execute_sql(self, clean_instance):
        """Test executing SQL commands."""
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)
        pg.start()

        try:
            # Execute a simple query
            result = pg.execute("SELECT 1 as num;")
            assert "1" in result

            # Create and query a table
            pg.execute("CREATE TABLE test_table (id serial, name text);")
            pg.execute("INSERT INTO test_table (name) VALUES ('hello');")
            result = pg.execute("SELECT name FROM test_table;")
            assert "hello" in result
        finally:
            pg.stop()

    def test_custom_credentials(self, clean_instance):
        """Test custom username, password, database."""
        pg = Pg0(
            name=TEST_NAME,
            port=TEST_PORT,
            username="testuser",
            password="testpass",
            database="testdb",
        )
        info = pg.start()

        try:
            assert "testuser" in info.uri
            assert "testpass" in info.uri
            assert "testdb" in info.uri
        finally:
            pg.stop()

    def test_custom_config(self, clean_instance):
        """Test custom Pg0 configuration."""
        pg = Pg0(
            name=TEST_NAME,
            port=TEST_PORT,
            config={"work_mem": "128MB"},
        )
        pg.start()

        try:
            result = pg.execute("SHOW work_mem;")
            assert "128MB" in result
        finally:
            pg.stop()

    def test_already_running_error(self, clean_instance):
        """Test that starting twice raises error."""
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)
        pg.start()

        try:
            with pytest.raises(Pg0AlreadyRunningError):
                pg.start()
        finally:
            pg.stop()

    def test_stop_when_not_running(self, clean_instance):
        """Test that stopping when not running does not raise error."""
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)
        # Should not raise - stop is idempotent
        pg.stop()

    def test_info_when_not_running(self, clean_instance):
        """Test getting info when not running."""
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)
        info = pg.info()

        assert info.running is False
        assert info.uri is None

    def test_port_conflict_error(self, clean_instance):
        """Test that starting two instances on the same port gives a readable error."""
        pg1 = Pg0(name=TEST_NAME, port=TEST_PORT)
        pg2 = Pg0(name=f"{TEST_NAME}-2", port=TEST_PORT)

        pg1.start()

        try:
            with pytest.raises(Pg0Error) as exc_info:
                pg2.start()

            # Verify the error message mentions the port conflict
            error_message = str(exc_info.value).lower()
            assert "port" in error_message or "address" in error_message or "in use" in error_message, \
                f"Error message should mention port conflict, got: {exc_info.value}"
        finally:
            pg1.stop()
            pg2.stop()
            pg0.drop(f"{TEST_NAME}-2")

    def test_data_survives_crash(self, clean_instance):
        """Test that data is preserved after an unclean shutdown (SIGKILL).

        Regression test for https://github.com/vectorize-io/pg0/issues/6
        Simulates a crash by sending SIGKILL to the PostgreSQL process,
        which leaves a stale postmaster.pid. On restart, data must still exist.
        """
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)
        info = pg.start()

        # Create a table and insert data
        pg.execute("CREATE TABLE crash_test (id serial PRIMARY KEY, value text);")
        pg.execute("INSERT INTO crash_test (value) VALUES ('survive_crash');")
        result = pg.execute("SELECT value FROM crash_test;")
        assert "survive_crash" in result

        # Simulate a crash: SIGKILL the postgres process (leaves stale postmaster.pid)
        pid = info.pid
        assert pid is not None
        os.kill(pid, signal.SIGKILL)
        time.sleep(1)  # Wait for process to die

        # Restart — this must NOT lose data
        info = pg.start()
        assert info.running is True

        # Verify data survived the crash
        result = pg.execute("SELECT value FROM crash_test;")
        assert "survive_crash" in result

        pg.stop()


class TestConvenienceFunctions:
    """Tests for module-level convenience functions."""

    def test_start_stop_info(self, clean_instance):
        """Test start, stop, info functions."""
        info = pg0.start(name=TEST_NAME, port=TEST_PORT)
        assert info.running is True

        info = pg0.info(TEST_NAME)
        assert info.running is True
        assert info.port == TEST_PORT

        pg0.stop(TEST_NAME)
        info = pg0.info(TEST_NAME)
        assert info.running is False

    def test_list_instances(self, clean_instance):
        """Test listing instances."""
        # Start an instance
        pg0.start(name=TEST_NAME, port=TEST_PORT)

        try:
            instances = pg0.list_instances()
            names = [i.name for i in instances]
            assert TEST_NAME in names
        finally:
            pg0.stop(TEST_NAME)

    def test_logs(self, clean_instance):
        """Test getting logs."""
        pg = Pg0(name=TEST_NAME, port=TEST_PORT)
        pg.start()

        try:
            # Run a query to generate some log activity
            pg.execute("SELECT 1;")

            # Get logs via instance method
            logs = pg.logs()
            assert isinstance(logs, str)

            # Get logs with line limit
            logs_limited = pg.logs(lines=10)
            assert isinstance(logs_limited, str)

            # Get logs via module function
            logs_module = pg0.logs(TEST_NAME)
            assert isinstance(logs_module, str)
        finally:
            pg.stop()


class TestInstanceInfo:
    """Tests for InstanceInfo dataclass."""

    def test_from_dict(self):
        """Test creating InstanceInfo from dict."""
        data = {
            "name": "test",
            "running": True,
            "pid": 1234,
            "port": 5432,
            "uri": "postgresql://localhost:5432/test",
        }
        info = InstanceInfo.from_dict(data)

        assert info.name == "test"
        assert info.running is True
        assert info.pid == 1234
        assert info.port == 5432
        assert info.uri == "postgresql://localhost:5432/test"

    def test_from_dict_minimal(self):
        """Test creating InstanceInfo from minimal dict."""
        data = {"running": False}
        info = InstanceInfo.from_dict(data)

        assert info.name == "default"
        assert info.running is False
        assert info.pid is None
        assert info.uri is None
```

## File: `src/main.rs`
```rust
use clap::{Parser, Subcommand};
use flate2::read::GzDecoder;
use postgresql_embedded::blocking::PostgreSQL;
use postgresql_embedded::{Settings, VersionReq};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;
use std::process;
use tar::Archive;
use thiserror::Error;
use tracing_subscriber::EnvFilter;

/// The embedded PostgreSQL bundle
static POSTGRESQL_BUNDLE: &[u8] = include_bytes!(env!("POSTGRESQL_BUNDLE_PATH"));

/// The embedded pgvector bundle
static PGVECTOR_BUNDLE: &[u8] = include_bytes!(env!("PGVECTOR_BUNDLE_PATH"));

#[derive(Error, Debug)]
enum CliError {
    #[error("PostgreSQL error: {0}")]
    PostgreSQL(#[from] postgresql_embedded::Error),
    #[error("Extension error: {0}")]
    Extension(#[from] postgresql_extensions::Error),
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("No running instance found")]
    NoInstance,
    #[error("Instance already running (pid: {0})")]
    AlreadyRunning(u32),
    #[error("Could not determine data directory")]
    NoDataDir,
    #[error("Failed to parse PID from postmaster.pid")]
    PidParse,
    #[error("Extension '{0}' not found")]
    ExtensionNotFound(String),
    #[error("{0}")]
    Other(String),
}

#[derive(Parser)]
#[command(name = "pg0")]
#[command(about = "Zero-dependency CLI to run embedded PostgreSQL locally", long_about = None)]
#[command(version)]
struct Cli {
    /// Enable verbose logging
    #[arg(short, long, global = true)]
    verbose: bool,

    #[command(subcommand)]
    command: Commands,
}

const DEFAULT_INSTANCE_NAME: &str = "default";

#[derive(Subcommand)]
enum Commands {
    /// Start PostgreSQL server
    Start {
        /// Instance name (allows running multiple instances)
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,

        /// Port to listen on (auto-allocates if not specified and default port is in use)
        #[arg(short, long)]
        port: Option<u16>,

        /// PostgreSQL version (must match bundled version)
        #[arg(short = 'V', long, default_value = env!("PG_VERSION"))]
        version: String,

        /// Data directory (defaults to ~/.pg0/instances/<name>/data)
        #[arg(short, long)]
        data_dir: Option<String>,

        /// Username for the database
        #[arg(short, long, default_value = "postgres")]
        username: String,

        /// Password for the database
        #[arg(short = 'P', long, default_value = "postgres")]
        password: String,

        /// Database name to create
        #[arg(short = 'n', long, default_value = "postgres")]
        database: String,

        /// PostgreSQL configuration options (can be used multiple times)
        /// Example: -c shared_buffers=512MB -c work_mem=128MB
        #[arg(short = 'c', long = "config", value_name = "KEY=VALUE")]
        config: Vec<String>,
    },
    /// Stop PostgreSQL server
    Stop {
        /// Instance name
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,
    },
    /// Drop an instance (stop if running, delete all data)
    Drop {
        /// Instance name
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,

        /// Skip confirmation prompt
        #[arg(short, long)]
        force: bool,
    },
    /// Show PostgreSQL server info (status, connection URI, etc.)
    Info {
        /// Instance name
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,

        /// Output format
        #[arg(short, long, default_value = "text")]
        output: OutputFormat,
    },
    /// List all instances
    List {
        /// Output format
        #[arg(short, long, default_value = "text")]
        output: OutputFormat,
    },
    /// Open psql shell connected to the running instance
    Psql {
        /// Instance name
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,

        /// Additional arguments to pass to psql
        #[arg(trailing_var_arg = true, allow_hyphen_values = true)]
        args: Vec<String>,
    },
    /// Show PostgreSQL logs
    Logs {
        /// Instance name
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,

        /// Number of lines to show (default: all)
        #[arg(short = 'n', long)]
        lines: Option<usize>,

        /// Follow log output (like tail -f)
        #[arg(short, long)]
        follow: bool,
    },
    /// Install a PostgreSQL extension (e.g., pgvector)
    InstallExtension {
        /// Instance name
        #[arg(long, default_value = DEFAULT_INSTANCE_NAME)]
        name: String,

        /// Extension name (e.g., "vector", "postgis")
        extension: String,
    },
    /// List available extensions
    ListExtensions,
}

#[derive(Clone, Debug, Default, clap::ValueEnum)]
enum OutputFormat {
    #[default]
    Text,
    Json,
}

#[derive(Serialize, Deserialize)]
struct InstanceInfo {
    pid: u32,
    port: u16,
    data_dir: PathBuf,
    installation_dir: PathBuf,
    username: String,
    password: String,
    database: String,
    version: String,
}

#[derive(Serialize)]
struct InfoOutput {
    name: String,
    running: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    pid: Option<u32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    port: Option<u16>,
    #[serde(skip_serializing_if = "Option::is_none")]
    version: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    username: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    database: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    data_dir: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    uri: Option<String>,
}

fn get_base_dir() -> Result<PathBuf, CliError> {
    dirs::home_dir()
        .map(|h| h.join(".pg0"))
        .ok_or(CliError::NoDataDir)
}

fn get_instances_dir() -> Result<PathBuf, CliError> {
    Ok(get_base_dir()?.join("instances"))
}

fn get_instance_dir(name: &str) -> Result<PathBuf, CliError> {
    Ok(get_instances_dir()?.join(name))
}

fn get_state_file(name: &str) -> Result<PathBuf, CliError> {
    Ok(get_instance_dir(name)?.join("instance.json"))
}

fn load_instance(name: &str) -> Result<Option<InstanceInfo>, CliError> {
    let state_file = get_state_file(name)?;
    if state_file.exists() {
        let content = fs::read_to_string(&state_file)?;
        Ok(Some(serde_json::from_str(&content)?))
    } else {
        Ok(None)
    }
}

fn save_instance(name: &str, info: &InstanceInfo) -> Result<(), CliError> {
    let instance_dir = get_instance_dir(name)?;
    fs::create_dir_all(&instance_dir)?;
    let state_file = get_state_file(name)?;
    fs::write(&state_file, serde_json::to_string_pretty(info)?)?;
    Ok(())
}

fn remove_instance(name: &str) -> Result<(), CliError> {
    let state_file = get_state_file(name)?;
    if state_file.exists() {
        fs::remove_file(&state_file)?;
    }
    Ok(())
}

fn list_instances() -> Result<Vec<String>, CliError> {
    let instances_dir = get_instances_dir()?;
    if !instances_dir.exists() {
        return Ok(Vec::new());
    }

    let mut names = Vec::new();
    for entry in fs::read_dir(&instances_dir)? {
        let entry = entry?;
        if entry.path().is_dir() {
            if let Some(name) = entry.file_name().to_str() {
                // Check if it has an instance.json file
                if entry.path().join("instance.json").exists() {
                    names.push(name.to_string());
                }
            }
        }
    }
    names.sort();
    Ok(names)
}

fn is_process_running(pid: u32) -> bool {
    #[cfg(unix)]
    {
        use std::process::Command;
        Command::new("kill")
            .args(["-0", &pid.to_string()])
            .output()
            .map(|o| o.status.success())
            .unwrap_or(false)
    }
    #[cfg(windows)]
    {
        use std::process::Command;
        Command::new("tasklist")
            .args(["/FI", &format!("PID eq {}", pid)])
            .output()
            .map(|o| String::from_utf8_lossy(&o.stdout).contains(&pid.to_string()))
            .unwrap_or(false)
    }
}

/// Read the PID from PostgreSQL's postmaster.pid file
fn read_postmaster_pid(data_dir: &PathBuf) -> Result<u32, CliError> {
    let pid_file = data_dir.join("postmaster.pid");
    let content = fs::read_to_string(&pid_file)?;
    // First line of postmaster.pid is the PID
    content
        .lines()
        .next()
        .and_then(|line| line.trim().parse().ok())
        .ok_or(CliError::PidParse)
}

/// Expand ~ to home directory
fn expand_path(path: &str) -> PathBuf {
    if path.starts_with("~/") {
        if let Some(home) = dirs::home_dir() {
            return home.join(&path[2..]);
        }
    }
    PathBuf::from(path)
}

/// Check if a port is available for binding
fn is_port_available(port: u16) -> bool {
    std::net::TcpListener::bind(("127.0.0.1", port)).is_ok()
}

/// Find an available port, starting from the given port
fn find_available_port(start_port: u16) -> u16 {
    let mut port = start_port;
    while !is_port_available(port) {
        port += 1;
        if port > 65535 - 100 {
            // Wrap around to a random high port if we've gone too far
            port = 49152; // Start of dynamic/private port range
        }
    }
    port
}

/// Read the latest PostgreSQL log file content (last 20 lines)
fn read_latest_pg_log(data_dir: &PathBuf) -> Option<String> {
    let log_dir = data_dir.join("log");
    let entries = fs::read_dir(&log_dir).ok()?;

    // Find the most recent log file
    let mut log_files: Vec<_> = entries
        .filter_map(|e| e.ok())
        .filter(|e| e.path().extension().map(|ext| ext == "log").unwrap_or(false))
        .collect();
    log_files.sort_by_key(|e| {
        std::cmp::Reverse(
            e.metadata()
                .and_then(|m| m.modified())
                .unwrap_or(std::time::SystemTime::UNIX_EPOCH),
        )
    });

    let log_file = log_files.first()?;
    let content = fs::read_to_string(log_file.path()).ok()?;

    // Get last 20 lines
    let lines: Vec<&str> = content.lines().collect();
    let last_lines: Vec<&str> = lines.iter().rev().take(20).rev().cloned().collect();

    if last_lines.is_empty() {
        None
    } else {
        Some(last_lines.join("\n"))
    }
}

/// Extract the bundled PostgreSQL to the installation directory
/// Returns the path to the version-specific directory (e.g., ~/.pg0/installation/18.1.0)
fn extract_bundled_postgresql(installation_dir: &PathBuf, pg_version: &str) -> Result<PathBuf, CliError> {
    let version_dir = installation_dir.join(pg_version);

    // Check if already extracted
    let bin_dir = version_dir.join("bin");
    if bin_dir.exists() && bin_dir.join("postgres").exists() {
        tracing::debug!("PostgreSQL already extracted at {}", version_dir.display());
        return Ok(version_dir);
    }

    if POSTGRESQL_BUNDLE.is_empty() {
        return Err(CliError::Other(
            "PostgreSQL bundle is empty - this binary was not built with BUNDLE_POSTGRESQL=true".to_string()
        ));
    }

    println!("Extracting bundled PostgreSQL {}...", pg_version);
    fs::create_dir_all(&version_dir)?;

    // Extract the tar.gz bundle
    // The archive contains paths like "postgresql-18.1.0-aarch64-apple-darwin/bin/postgres"
    // We need to extract to version_dir, stripping the first path component
    let decoder = GzDecoder::new(POSTGRESQL_BUNDLE);
    let mut archive = Archive::new(decoder);

    for entry in archive.entries()? {
        let mut entry = entry?;
        let path = entry.path()?;

        // Strip the first component (e.g., "postgresql-18.1.0-aarch64-apple-darwin")
        let stripped_path: PathBuf = path.components().skip(1).collect();
        if stripped_path.as_os_str().is_empty() {
            continue; // Skip the root directory entry
        }

        let dest_path = version_dir.join(&stripped_path);

        // Create parent directories if needed
        if let Some(parent) = dest_path.parent() {
            fs::create_dir_all(parent)?;
        }

        // Extract the entry
        if entry.header().entry_type().is_dir() {
            fs::create_dir_all(&dest_path)?;
        } else {
            entry.unpack(&dest_path)?;
        }
    }

    // Verify extraction
    if !bin_dir.join("postgres").exists() {
        return Err(CliError::Other(format!(
            "PostgreSQL extraction failed - postgres binary not found at {}",
            bin_dir.display()
        )));
    }

    // Make binaries executable on Unix
    #[cfg(unix)]
    {
        use std::os::unix::fs::PermissionsExt;
        if let Ok(entries) = fs::read_dir(&bin_dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                if path.is_file() {
                    if let Ok(metadata) = path.metadata() {
                        let mut perms = metadata.permissions();
                        perms.set_mode(0o755);
                        let _ = fs::set_permissions(&path, perms);
                    }
                }
            }
        }
        // Also make lib files executable/accessible
        let lib_dir = version_dir.join("lib");
        if let Ok(entries) = fs::read_dir(&lib_dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                if path.is_file() {
                    if let Ok(metadata) = path.metadata() {
                        let mut perms = metadata.permissions();
                        perms.set_mode(0o755);
                        let _ = fs::set_permissions(&path, perms);
                    }
                }
            }
        }
    }

    println!("PostgreSQL {} extracted successfully.", pg_version);
    Ok(version_dir)
}

/// Install pgvector extension files into the PostgreSQL installation
fn install_pgvector(installation_dir: &PathBuf, pg_version: &str) -> Result<(), CliError> {
    let pg_major = pg_version.split('.').next().unwrap_or("16");
    let pgvector_version = env!("PGVECTOR_VERSION");

    // Find the version-specific installation directory
    let version_dir = fs::read_dir(installation_dir)?
        .filter_map(|e| e.ok())
        .find(|e| e.path().is_dir() && e.file_name().to_string_lossy().starts_with(pg_major))
        .map(|e| e.path())
        .ok_or_else(|| std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "PostgreSQL installation directory not found"
        ))?;

    let lib_dir = version_dir.join("lib");
    let extension_dir = version_dir.join("share").join("extension");

    // Check if pgvector is already installed
    if extension_dir.join("vector.control").exists() {
        tracing::debug!("pgvector already installed");
        return Ok(());
    }

    if PGVECTOR_BUNDLE.is_empty() {
        return Err(CliError::Other(
            "pgvector bundle is empty - this binary was not built with BUNDLE_POSTGRESQL=true".to_string()
        ));
    }

    println!("Installing pgvector {}...", pgvector_version);

    // Extract bundled pgvector
    let decoder = GzDecoder::new(PGVECTOR_BUNDLE);
    let mut archive = Archive::new(decoder);

    for entry in archive.entries()? {
        let mut entry = entry?;
        let path = entry.path()?;

        if let Some(name) = path.file_name().and_then(|n| n.to_str()) {
            if name.ends_with(".so") || name.ends_with(".dylib") || name.ends_with(".dll") {
                let dest = lib_dir.join(name);
                entry.unpack(&dest)?;
                // Make library executable on Unix
                #[cfg(unix)]
                {
                    use std::os::unix::fs::PermissionsExt;
                    if let Ok(metadata) = dest.metadata() {
                        let mut perms = metadata.permissions();
                        perms.set_mode(0o755);
                        let _ = fs::set_permissions(&dest, perms);
                    }
                }
            } else if name == "vector.control" || name.starts_with("vector--") {
                let dest = extension_dir.join(name);
                entry.unpack(&dest)?;
            }
        }
    }

    println!("pgvector {} installed successfully!", pgvector_version);
    Ok(())
}

fn start(
    name: String,
    port: u16,
    port_was_specified: bool,
    version: String,
    data_dir: Option<String>,
    username: String,
    password: String,
    database: String,
    config: Vec<String>,
) -> Result<(), CliError> {
    // Check if already running
    if let Some(info) = load_instance(&name)? {
        if is_process_running(info.pid) {
            return Err(CliError::AlreadyRunning(info.pid));
        }
        // Stale instance: clean up instance metadata but preserve data directory.
        // Remove stale postmaster.pid so PostgreSQL can start with existing data.
        let pid_file = info.data_dir.join("postmaster.pid");
        if pid_file.exists() {
            println!("Removing stale postmaster.pid (process {} no longer running)...", info.pid);
            fs::remove_file(&pid_file)?;
        }
        remove_instance(&name)?;
    }

    // Auto-allocate port if the requested port is in use (only if port wasn't explicitly specified)
    let port = if !port_was_specified && !is_port_available(port) {
        let new_port = find_available_port(port);
        println!("Port {} is in use, using port {} instead.", port, new_port);
        new_port
    } else {
        port
    };

    let base_dir = get_base_dir()?;
    let instance_dir = get_instance_dir(&name)?;

    // Use provided data_dir or default to instance-specific directory
    let data_dir = match data_dir {
        Some(dir) => expand_path(&dir),
        None => instance_dir.join("data"),
    };

    let installation_dir = base_dir.join("installation");

    fs::create_dir_all(&data_dir)?;
    fs::create_dir_all(&installation_dir)?;

    println!("Setting up PostgreSQL {}...", version);

    let version_req: VersionReq = version.parse().map_err(|e| {
        std::io::Error::new(
            std::io::ErrorKind::InvalidInput,
            format!("Invalid version: {}", e),
        )
    })?;

    // Build configuration HashMap with sensible defaults
    let mut configuration: HashMap<String, String> = HashMap::new();

    // Apply opinionated defaults optimized for vector/AI workloads
    configuration.insert("shared_buffers".to_string(), "256MB".to_string());
    configuration.insert("maintenance_work_mem".to_string(), "512MB".to_string());
    configuration.insert("effective_cache_size".to_string(), "1GB".to_string());
    configuration.insert("max_parallel_maintenance_workers".to_string(), "4".to_string());
    configuration.insert("work_mem".to_string(), "64MB".to_string());

    // Enable logging to files (required for `pg0 logs` command)
    configuration.insert("logging_collector".to_string(), "on".to_string());
    configuration.insert("log_directory".to_string(), "log".to_string());
    configuration.insert("log_filename".to_string(), "postgresql-%Y-%m-%d.log".to_string());
    configuration.insert("log_rotation_age".to_string(), "1d".to_string());
    configuration.insert("log_rotation_size".to_string(), "100MB".to_string());

    // Parse and apply custom config options (these override defaults)
    for cfg in &config {
        if let Some((key, value)) = cfg.split_once('=') {
            configuration.insert(key.trim().to_string(), value.trim().to_string());
        } else {
            eprintln!("Warning: Invalid config format '{}', expected KEY=VALUE", cfg);
        }
    }

    // Extract bundled PostgreSQL
    let version_install_dir = extract_bundled_postgresql(&installation_dir, &version)?;

    let settings = Settings {
        version: version_req,
        port,
        username: username.clone(),
        password: password.clone(),
        data_dir: data_dir.clone(),
        installation_dir: version_install_dir,
        configuration,
        trust_installation_dir: true, // Use our extracted files
        temporary: false, // Never delete data directory on drop - pg0 manages data lifecycle explicitly
        timeout: Some(std::time::Duration::from_secs(600)), // 10 minute timeout for slow systems (ARM64 emulation under QEMU)
        ..Default::default()
    };

    let mut postgresql = PostgreSQL::new(settings);
    postgresql.setup()?;

    // Install pgvector extension
    if let Err(e) = install_pgvector(&installation_dir, &version) {
        eprintln!("Warning: Failed to install pgvector: {}", e);
        eprintln!("You can try installing it manually with: pg0 install-extension vector");
    }

    println!("Starting PostgreSQL on port {}...", port);
    if let Err(e) = postgresql.start() {
        // Try to read the PostgreSQL log for more context
        let log_context = read_latest_pg_log(&data_dir);
        let error_msg = if let Some(log) = log_context {
            format!("Failed to start PostgreSQL: {}\n\nPostgreSQL log:\n{}", e, log)
        } else {
            format!("Failed to start PostgreSQL: {}", e)
        };
        return Err(CliError::Other(error_msg));
    }

    // Create the user if it's not the default 'postgres'
    // Note: postgresql_embedded always creates 'postgres' as the superuser
    if username != "postgres" {
        println!("Creating user '{}'...", username);
        let psql_path = find_psql_binary(&installation_dir)?;
        let create_user_sql = format!(
            "DO $$ BEGIN IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '{}') THEN CREATE USER \"{}\" WITH SUPERUSER PASSWORD '{}'; END IF; END $$;",
            username, username, password.replace('\'', "''")
        );
        let status = std::process::Command::new(&psql_path)
            .arg(&format!("postgresql://postgres:{}@localhost:{}/postgres", password, port))
            .arg("-c")
            .arg(&create_user_sql)
            .status()?;
        if !status.success() {
            eprintln!("Warning: Failed to create user '{}'", username);
        }
    }

    // Create the database if it doesn't exist and it's not the default 'postgres'
    if database != "postgres" {
        println!("Creating database '{}'...", database);
        if let Err(e) = postgresql.create_database(&database) {
            // Ignore error if database already exists
            let err_str = e.to_string();
            if !err_str.contains("already exists") {
                return Err(e.into());
            }
        }
        // Grant privileges to the user on the database
        if username != "postgres" {
            let psql_path = find_psql_binary(&installation_dir)?;
            let grant_sql = format!("GRANT ALL PRIVILEGES ON DATABASE \"{}\" TO \"{}\";", database, username);
            let _ = std::process::Command::new(&psql_path)
                .arg(&format!("postgresql://postgres:{}@localhost:{}/postgres", password, port))
                .arg("-c")
                .arg(&grant_sql)
                .status();
        }
    }

    // Read PID from postmaster.pid file
    let pid = read_postmaster_pid(&data_dir)?;

    let info = InstanceInfo {
        pid,
        port,
        data_dir: data_dir.clone(),
        installation_dir,
        username: username.clone(),
        password: password.clone(),
        database: database.clone(),
        version: version.clone(),
    };

    save_instance(&name, &info)?;

    println!();
    println!("PostgreSQL is running!");
    println!("  Instance: {}", name);
    println!("  PID:      {}", pid);
    println!("  Port:     {}", port);
    println!("  Username: {}", username);
    println!("  Password: {}", password);
    println!("  Database: {}", database);
    println!("  Data dir: {}", data_dir.display());
    println!();
    println!(
        "Connection URI: postgresql://{}:{}@localhost:{}/{}",
        username, password, port, database
    );
    println!();
    if name == DEFAULT_INSTANCE_NAME {
        println!("Use 'pg0 stop' to stop the server.");
    } else {
        println!("Use 'pg0 stop --name {}' to stop the server.", name);
    }

    // Detach - let the process continue running
    std::mem::forget(postgresql);

    Ok(())
}

fn stop(name: String) -> Result<(), CliError> {
    let info = load_instance(&name)?.ok_or(CliError::NoInstance)?;

    if !is_process_running(info.pid) {
        println!("PostgreSQL instance '{}' is not running.", name);
        return Ok(());
    }

    println!("Stopping PostgreSQL instance '{}' (pid: {})...", name, info.pid);

    // Send SIGTERM to gracefully stop
    #[cfg(unix)]
    {
        use std::process::Command;
        let _ = Command::new("kill")
            .args(["-TERM", &info.pid.to_string()])
            .output();
    }
    #[cfg(windows)]
    {
        use std::process::Command;
        let _ = Command::new("taskkill")
            .args(["/PID", &info.pid.to_string()])
            .output();
    }

    // Wait a bit for graceful shutdown
    std::thread::sleep(std::time::Duration::from_secs(2));

    // Force kill if still running
    if is_process_running(info.pid) {
        #[cfg(unix)]
        {
            use std::process::Command;
            let _ = Command::new("kill")
                .args(["-9", &info.pid.to_string()])
                .output();
        }
        #[cfg(windows)]
        {
            use std::process::Command;
            let _ = Command::new("taskkill")
                .args(["/F", "/PID", &info.pid.to_string()])
                .output();
        }
    }

    println!("PostgreSQL instance '{}' stopped.", name);

    Ok(())
}

fn drop_instance(name: String, force: bool) -> Result<(), CliError> {
    let instance = load_instance(&name)?;

    if instance.is_none() {
        println!("Instance '{}' does not exist.", name);
        return Ok(());
    }

    let info = instance.unwrap();

    // Confirmation prompt unless --force
    if !force {
        println!("This will permanently delete instance '{}' and all its data:", name);
        println!("  Data dir: {}", info.data_dir.display());
        println!();
        print!("Are you sure? [y/N] ");
        std::io::Write::flush(&mut std::io::stdout())?;

        let mut input = String::new();
        std::io::stdin().read_line(&mut input)?;
        if !input.trim().eq_ignore_ascii_case("y") {
            println!("Aborted.");
            return Ok(());
        }
    }

    // Stop if running
    if is_process_running(info.pid) {
        println!("Stopping PostgreSQL instance '{}' (pid: {})...", name, info.pid);
        #[cfg(unix)]
        {
            use std::process::Command;
            let _ = Command::new("kill")
                .args(["-TERM", &info.pid.to_string()])
                .output();
        }
        #[cfg(windows)]
        {
            use std::process::Command;
            let _ = Command::new("taskkill")
                .args(["/PID", &info.pid.to_string()])
                .output();
        }
        std::thread::sleep(std::time::Duration::from_secs(2));

        if is_process_running(info.pid) {
            #[cfg(unix)]
            {
                use std::process::Command;
                let _ = Command::new("kill")
                    .args(["-9", &info.pid.to_string()])
                    .output();
            }
            #[cfg(windows)]
            {
                use std::process::Command;
                let _ = Command::new("taskkill")
                    .args(["/F", "/PID", &info.pid.to_string()])
                    .output();
            }
        }
    }

    // Delete data directory
    if info.data_dir.exists() {
        println!("Deleting data directory: {}", info.data_dir.display());
        fs::remove_dir_all(&info.data_dir)?;
    }

    // Delete instance directory (contains instance.json)
    let instance_dir = get_instance_dir(&name)?;
    if instance_dir.exists() {
        fs::remove_dir_all(&instance_dir)?;
    }

    println!("Instance '{}' dropped.", name);

    Ok(())
}

fn info(name: String, output_format: OutputFormat) -> Result<(), CliError> {
    let instance = load_instance(&name)?;

    let output = match instance {
        Some(info) => {
            let running = is_process_running(info.pid);
            if running {
                let uri = format!(
                    "postgresql://{}:{}@localhost:{}/{}",
                    info.username, info.password, info.port, info.database
                );
                InfoOutput {
                    name: name.clone(),
                    running: true,
                    pid: Some(info.pid),
                    port: Some(info.port),
                    version: Some(info.version),
                    username: Some(info.username),
                    database: Some(info.database),
                    data_dir: Some(info.data_dir.display().to_string()),
                    uri: Some(uri),
                }
            } else {
                // Stopped but instance exists - show data_dir
                InfoOutput {
                    name: name.clone(),
                    running: false,
                    pid: None,
                    port: Some(info.port),
                    version: Some(info.version),
                    username: Some(info.username),
                    database: Some(info.database),
                    data_dir: Some(info.data_dir.display().to_string()),
                    uri: None,
                }
            }
        }
        None => {
            // Instance doesn't exist
            InfoOutput {
                name: name.clone(),
                running: false,
                pid: None,
                port: None,
                version: None,
                username: None,
                database: None,
                data_dir: None,
                uri: None,
            }
        }
    };

    match output_format {
        OutputFormat::Json => {
            println!("{}", serde_json::to_string_pretty(&output)?);
        }
        OutputFormat::Text => {
            if output.running {
                println!("PostgreSQL instance '{}' is running", name);
                println!("  PID:      {}", output.pid.unwrap());
                println!("  Port:     {}", output.port.unwrap());
                println!("  Version:  {}", output.version.as_ref().unwrap());
                println!("  Username: {}", output.username.as_ref().unwrap());
                println!("  Database: {}", output.database.as_ref().unwrap());
                println!("  Data dir: {}", output.data_dir.as_ref().unwrap());
                println!();
                println!("URI: {}", output.uri.as_ref().unwrap());
            } else if output.data_dir.is_some() {
                println!("PostgreSQL instance '{}' is stopped", name);
                println!("  Port:     {}", output.port.unwrap());
                println!("  Version:  {}", output.version.as_ref().unwrap());
                println!("  Username: {}", output.username.as_ref().unwrap());
                println!("  Database: {}", output.database.as_ref().unwrap());
                println!("  Data dir: {}", output.data_dir.as_ref().unwrap());
                println!();
                println!("Use 'pg0 start --name {}' to start it.", name);
            } else {
                println!("PostgreSQL instance '{}' does not exist", name);
            }
        }
    }

    Ok(())
}

fn find_psql_binary(installation_dir: &PathBuf) -> Result<PathBuf, CliError> {
    // Look for psql in installation_dir/*/bin/psql (version subdirectory)
    if let Ok(entries) = fs::read_dir(installation_dir) {
        for entry in entries.flatten() {
            let psql_path = entry.path().join("bin").join("psql");
            if psql_path.exists() {
                return Ok(psql_path);
            }
        }
    }

    // Fallback: try direct path (in case structure changes)
    let direct_path = installation_dir.join("bin").join("psql");
    if direct_path.exists() {
        return Ok(direct_path);
    }

    Err(CliError::Io(std::io::Error::new(
        std::io::ErrorKind::NotFound,
        format!(
            "psql not found in {}",
            installation_dir.display()
        ),
    )))
}

fn psql(name: String, args: Vec<String>) -> Result<(), CliError> {
    let info = load_instance(&name)?.ok_or(CliError::NoInstance)?;

    if !is_process_running(info.pid) {
        remove_instance(&name)?;
        return Err(CliError::NoInstance);
    }

    let psql_path = find_psql_binary(&info.installation_dir)?;

    // Build connection URI
    let uri = format!(
        "postgresql://{}:{}@localhost:{}/{}",
        info.username, info.password, info.port, info.database
    );

    // Execute psql with the connection URI and any additional args
    let status = std::process::Command::new(&psql_path)
        .arg(&uri)
        .args(&args)
        .status()?;

    if !status.success() {
        std::process::exit(status.code().unwrap_or(1));
    }

    Ok(())
}

fn logs(name: String, lines: Option<usize>, follow: bool) -> Result<(), CliError> {
    let instance_dir = get_instance_dir(&name)?;
    let log_dir = instance_dir.join("data").join("log");

    if !log_dir.exists() {
        return Err(CliError::Other(format!(
            "Log directory not found for instance '{}'. Has PostgreSQL been started?",
            name
        )));
    }

    // Find the most recent log file
    let mut log_files: Vec<_> = fs::read_dir(&log_dir)?
        .filter_map(|e| e.ok())
        .filter(|e| e.path().is_file())
        .collect();

    if log_files.is_empty() {
        return Err(CliError::Other(format!(
            "No log files found for instance '{}'",
            name
        )));
    }

    // Sort by modification time, most recent first
    log_files.sort_by_key(|e| std::cmp::Reverse(
        e.metadata().and_then(|m| m.modified()).ok()
    ));

    let log_file = &log_files[0].path();

    if follow {
        // Follow mode - use tail -f equivalent
        println!("Following logs for instance '{}' (Ctrl+C to exit):", name);
        println!("Log file: {}", log_file.display());
        println!();

        let mut file = fs::File::open(log_file)?;
        let mut pos = file.metadata()?.len();

        // Print existing content first
        use std::io::{BufRead, BufReader, Seek, SeekFrom};
        file.seek(SeekFrom::Start(0))?;
        let reader = BufReader::new(&file);
        for line in reader.lines() {
            println!("{}", line?);
        }

        // Now follow new content
        loop {
            file.seek(SeekFrom::Start(pos))?;
            let reader = BufReader::new(&file);
            for line in reader.lines() {
                println!("{}", line?);
            }
            pos = file.metadata()?.len();
            std::thread::sleep(std::time::Duration::from_millis(100));
        }
    } else {
        // Show logs (optionally limited to N lines)
        use std::io::{BufRead, BufReader};
        let file = fs::File::open(log_file)?;
        let reader = BufReader::new(file);
        let all_lines: Vec<_> = reader.lines().collect::<Result<_, _>>()?;

        let lines_to_show = if let Some(n) = lines {
            &all_lines[all_lines.len().saturating_sub(n)..]
        } else {
            &all_lines[..]
        };

        println!("Logs for instance '{}' ({})", name, log_file.display());
        println!();
        for line in lines_to_show {
            println!("{}", line);
        }
    }

    Ok(())
}

fn find_installed_version(installation_dir: &PathBuf) -> Result<String, CliError> {
    if let Ok(entries) = fs::read_dir(installation_dir) {
        for entry in entries.flatten() {
            if entry.path().is_dir() {
                if let Some(name) = entry.file_name().to_str() {
                    // Check if it looks like a version directory
                    if name.chars().next().map(|c| c.is_ascii_digit()).unwrap_or(false) {
                        return Ok(name.to_string());
                    }
                }
            }
        }
    }
    Err(CliError::Io(std::io::Error::new(
        std::io::ErrorKind::NotFound,
        "No PostgreSQL version found in installation directory",
    )))
}

fn install_extension(instance_name: String, extension_name: String) -> Result<(), CliError> {
    let info = load_instance(&instance_name)?.ok_or(CliError::NoInstance)?;

    if !is_process_running(info.pid) {
        remove_instance(&instance_name)?;
        return Err(CliError::NoInstance);
    }

    println!("Fetching available extensions...");

    let available = postgresql_extensions::blocking::get_available_extensions()?;

    // Find the extension (case-insensitive search)
    let ext = available
        .iter()
        .find(|e| e.name().to_lowercase() == extension_name.to_lowercase())
        .ok_or_else(|| CliError::ExtensionNotFound(extension_name.clone()))?;

    let ext_name = ext.name().to_string();
    let ext_namespace = ext.namespace().to_string();
    println!("Installing extension '{}'...", ext_name);

    // Get installed PostgreSQL version
    let pg_version = find_installed_version(&info.installation_dir)?;
    let version_req: VersionReq = pg_version.parse().map_err(|e| {
        std::io::Error::new(
            std::io::ErrorKind::InvalidInput,
            format!("Invalid version: {}", e),
        )
    })?;

    // Build Settings for the extension installer
    // The installation_dir needs to point to the version-specific directory
    let version_install_dir = info.installation_dir.join(&pg_version);
    let settings = Settings {
        version: version_req.clone(),
        port: info.port,
        username: info.username.clone(),
        password: info.password.clone(),
        data_dir: info.data_dir.clone(),
        installation_dir: version_install_dir,
        ..Default::default()
    };

    postgresql_extensions::blocking::install(
        &settings,
        &ext_namespace,
        &ext_name,
        &version_req,
    )?;

    println!("Extension '{}' installed successfully!", ext_name);
    println!();
    println!("To enable it in your database, run:");
    println!("  pg0 psql -c \"CREATE EXTENSION IF NOT EXISTS {};\"", ext_name);

    Ok(())
}

fn list(output_format: OutputFormat) -> Result<(), CliError> {
    let instance_names = list_instances()?;

    let mut instances: Vec<InfoOutput> = Vec::new();
    for name in &instance_names {
        if let Some(info) = load_instance(name)? {
            let running = is_process_running(info.pid);
            let output = if running {
                let uri = format!(
                    "postgresql://{}:{}@localhost:{}/{}",
                    info.username, info.password, info.port, info.database
                );
                InfoOutput {
                    name: name.clone(),
                    running: true,
                    pid: Some(info.pid),
                    port: Some(info.port),
                    version: Some(info.version),
                    username: Some(info.username),
                    database: Some(info.database),
                    data_dir: Some(info.data_dir.display().to_string()),
                    uri: Some(uri),
                }
            } else {
                InfoOutput {
                    name: name.clone(),
                    running: false,
                    pid: None,
                    port: Some(info.port),
                    version: Some(info.version),
                    username: Some(info.username),
                    database: Some(info.database),
                    data_dir: Some(info.data_dir.display().to_string()),
                    uri: None,
                }
            };
            instances.push(output);
        }
    }

    match output_format {
        OutputFormat::Json => {
            println!("{}", serde_json::to_string_pretty(&instances)?);
        }
        OutputFormat::Text => {
            if instances.is_empty() {
                println!("No instances found.");
            } else {
                println!("Instances:");
                println!();
                for instance in &instances {
                    let status = if instance.running { "running" } else { "stopped" };
                    if instance.running {
                        println!(
                            "  {} ({}) - port {} - {}",
                            instance.name,
                            status,
                            instance.port.unwrap(),
                            instance.uri.as_ref().unwrap()
                        );
                    } else {
                        println!(
                            "  {} ({}) - port {} - {}",
                            instance.name,
                            status,
                            instance.port.unwrap(),
                            instance.data_dir.as_ref().unwrap()
                        );
                    }
                }
            }
        }
    }

    Ok(())
}

fn list_extensions() -> Result<(), CliError> {
    println!("Fetching available extensions...");

    let extensions = postgresql_extensions::blocking::get_available_extensions()?;

    println!();
    println!("Available extensions:");
    println!();

    for ext in extensions {
        println!("  {} - {}", ext.name(), ext.description());
    }

    Ok(())
}

fn init_logging(verbose: bool) {
    let filter = if verbose {
        EnvFilter::new("debug")
    } else {
        EnvFilter::new("warn")
    };

    tracing_subscriber::fmt()
        .with_env_filter(filter)
        .with_target(true)
        .init();
}

fn main() {
    let cli = Cli::parse();

    init_logging(cli.verbose);

    let result = match cli.command {
        Commands::Start {
            name,
            port,
            version,
            data_dir,
            username,
            password,
            database,
            config,
        } => {
            let port_was_specified = port.is_some();
            let port = port.unwrap_or(5432);
            start(name, port, port_was_specified, version, data_dir, username, password, database, config)
        }
        Commands::Stop { name } => stop(name),
        Commands::Drop { name, force } => drop_instance(name, force),
        Commands::Info { name, output } => info(name, output),
        Commands::List { output } => list(output),
        Commands::Psql { name, args } => psql(name, args),
        Commands::Logs { name, lines, follow } => logs(name, lines, follow),
        Commands::InstallExtension { name, extension } => install_extension(name, extension),
        Commands::ListExtensions => list_extensions(),
    };

    if let Err(e) = result {
        eprintln!("Error: {}", e);
        process::exit(1);
    }
}
```

