---
description: Build and deploy workflow – build binary, run in containers, deploy
---

# Deploy Workflow

## Steps

### Local Development
1. **Build the binary**
```bash
cargo build --manifest-path crates/contribai-rs/Cargo.toml --release
```

2. **Run CLI directly**
```bash
./crates/contribai-rs/target/release/contribai run --dry-run
```

### Docker

3. **Build Docker image**
```bash
docker build -t contribai:latest .
```
The Dockerfile uses a multi-stage build: `rust:slim` builder → `debian:bookworm-slim` runtime.
The final image contains only the static binary — no Rust toolchain.

4. **Run in container**
```bash
docker run --rm \
  -v $(pwd)/config.yaml:/app/config.yaml:ro \
  -v ~/.contribai:/root/.contribai \
  contribai:latest run --dry-run
```

5. **Run with docker-compose**
```bash
docker-compose up
```

### Binary Build

6. **Build release binary**
// turbo
```bash
cargo build --manifest-path crates/contribai-rs/Cargo.toml --release
```

7. **Verify binary**
// turbo
```bash
./crates/contribai-rs/target/release/contribai --version
```

8. **Strip binary for smaller size (Linux)**
```bash
strip crates/contribai-rs/target/release/contribai
```

### Production Deployment

9. **Set environment variables (alternative to config.yaml)**
```bash
export CONTRIBAI_GITHUB_TOKEN=ghp_xxx
export CONTRIBAI_LLM_API_KEY=xxx
export CONTRIBAI_LLM_PROVIDER=gemini
```

10. **Run as a scheduled job (cron)**
```bash
# Run every 6 hours
0 */6 * * * cd /path/to/contribai && ./contribai run >> /var/log/contribai.log 2>&1
```

11. **Monitor logs**
// turbo
```bash
# Check memory DB
DB=~/.contribai/memory.db
ls -lh "$DB" && echo "DB size: $(du -sh $DB | cut -f1)"
```
