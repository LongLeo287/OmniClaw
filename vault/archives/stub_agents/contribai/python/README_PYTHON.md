# ContribAI — Python Legacy

> ⚠️ **This is the legacy Python implementation (v4.1.0).**  
> The active development is now the **Rust version** in [`crates/contribai-rs/`](../crates/contribai-rs/).

## Why archived?

ContribAI has been fully rewritten in Rust (v5.0.0+) for:
- 10–50× faster analysis and PR generation
- Single binary, no Python runtime required
- Memory safety, no GIL, true parallelism
- 335 tests, full feature parity

## Using the Python version

```bash
# From project root
pip install -e ".[dev]"
python -m contribai.cli.main --help
# or (after pip install)
contribai-py --help
```

## Structure

```
python/
├── contribai/          # Python package (importable as 'contribai')
│   ├── cli/            # Click CLI
│   ├── core/           # Config, events, profiles
│   ├── analysis/       # Analyzers
│   ├── github/         # API client
│   ├── generator/      # Code generation
│   ├── orchestrator/   # Pipeline + memory
│   └── ...
└── tests/              # 400+ pytest tests
```

## Rust version (recommended)

```bash
# From project root
cargo build --release
./target/release/contribai --help
# or
cargo install --path crates/contribai-rs
contribai --help
```
