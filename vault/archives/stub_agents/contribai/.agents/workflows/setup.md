---
description: New developer onboarding – environment setup, project orientation, and first contribution
---

# Setup Workflow (Onboarding)

## Steps

1. **Clone the repository**
```bash
git clone https://github.com/tang-vu/ContribAI.git
cd ContribAI
```

2. **Verify Rust toolchain**
// turbo
```bash
rustup --version
cargo --version
```
Requires Rust 2021 edition (stable toolchain). Install via https://rustup.rs if absent:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

3. **Build the project**
```bash
cargo build --manifest-path crates/contribai-rs/Cargo.toml
```

4. **Build release binary**
```bash
cargo build --manifest-path crates/contribai-rs/Cargo.toml --release
```

5. **Add binary to PATH (optional)**
```bash
# Add to shell profile, or run directly via:
export PATH="$PATH:$(pwd)/crates/contribai-rs/target/release"
```

6. **Verify installation**
// turbo
```bash
./crates/contribai-rs/target/release/contribai --help
```

7. **Set up configuration**
```bash
cp config.example.yaml config.yaml
```
Edit `config.yaml` and add:
- GitHub Personal Access Token (with `repo`, `read:org` scopes)
- Gemini API key (from https://aistudio.google.com/app/apikey)

8. **Verify configuration**
// turbo
```bash
./crates/contribai-rs/target/release/contribai config
```

9. **Run tests to verify setup**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml
```
Expect 323 tests to pass.

10. **Read the project docs**
Key files to read:
- `README.md` – Project overview
- `CONTRIBUTING.md` – How to contribute
- `.agents/agents/` – Team roles and responsibilities
- `.agents/workflows/` – Development workflows

11. **Explore the codebase**
// turbo
```bash
find crates/contribai-rs/src -name "*.rs" | sort | while read f; do
  lines=$(wc -l < "$f")
  printf "  %-60s %4d lines\n" "$f" "$lines"
done
```

12. **Try a dry run**
```bash
./crates/contribai-rs/target/release/contribai analyze https://github.com/some-small-public-repo
```

13. **Make your first contribution**
Follow the `/dev` workflow to make a small improvement.
