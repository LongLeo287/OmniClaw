---
id: llmfit
type: knowledge
owner: OA_Triage
---
# llmfit
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# llmfit

<p align="center">
  <img src="assets/icon.svg" alt="llmfit icon" width="128" height="128">
</p>

<p align="center">
  <b>English</b> ·
  <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <a href="https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml"><img src="https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://crates.io/crates/llmfit"><img src="https://img.shields.io/crates/v/llmfit.svg" alt="Crates.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
</p>

**Hundreds of models & providers. One command to find what runs on your hardware.**

A terminal tool that right-sizes LLM models to your system's RAM, CPU, and GPU. Detects your hardware, scores each model across quality, speed, fit, and context dimensions, and tells you which ones will actually run well on your machine.

Ships with an interactive TUI (default) and a classic CLI mode. Supports multi-GPU setups, MoE architectures, dynamic quantization selection, speed estimation, and local runtime providers (Ollama, llama.cpp, MLX, Docker Model Runner, LM Studio).

> **Sister projects:**
> - [sympozium](https://github.com/sympozium-ai/sympozium/) — managing agents in Kubernetes.
> - [llmserve](https://github.com/AlexsJones/llmserve) — a simple TUI for serving local LLM models. Pick a model, pick a backend, serve it.

![demo](demo.gif)

---

## Install

### Windows
```sh
scoop install llmfit
```

If Scoop is not installed, follow the [Scoop installation guide](https://scoop.sh/).

### macOS / Linux

#### Homebrew
```sh
brew install llmfit
```

#### Quick install
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```

Downloads the latest release binary from GitHub and installs it to `/usr/local/bin` (or `~/.local/bin` if no sudo).

**Install to `~/.local/bin` without sudo:**
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh -s -- --local
```

### Docker / Podman
```sh
docker run ghcr.io/alexsjones/llmfit
```
This prints JSON from `llmfit recommend` command. The JSON could be further queried with `jq`.
```
podman run ghcr.io/alexsjones/llmfit recommend --use-case coding | jq '.models[].name'
```

### From source
```sh
git clone https://github.com/AlexsJones/llmfit.git
cd llmfit
cargo build --release
# binary is at target/release/llmfit
```

---

## Usage

### TUI (default)

```sh
llmfit
```

Launches the interactive terminal UI. Your system specs (CPU, RAM, GPU name, VRAM, backend) are shown at the top. Models are listed in a scrollable table sorted by composite score. Each row shows the model's score, estimated tok/s, best quantization for your hardware, run mode, memory usage, and use-case category.

| Key                        | Action                                                                |
|----------------------------|-----------------------------------------------------------------------|
| `Up` / `Down` or `j` / `k` | Navigate models                                                       |
| `/`                        | Enter search mode (partial match on name, provider, params, use case) |
| `Esc` or `Enter`           | Exit search mode                                                      |
| `Ctrl-U`                   | Clear search                                                          |
| `f`                        | Cycle fit filter: All, Runnable, Perfect, Good, Marginal              |
| `a`                        | Cycle availability filter: All, GGUF Avail, Installed                 |
| `s`                        | Cycle sort column: Score, Params, Mem%, Ctx, Date, Use Case           |
| `v`                        | Enter Visual mode (select multiple models)                            |
| `V`                        | Enter Select mode (column-based filtering)                            |
| `t`                        | Cycle color theme (saved automatically)                               |
| `p`                        | Open Plan mode for selected model (hardware planning)                 |
| `P`                        | Open provider filter popup                                            |
| `U`                        | Open use-case filter popup                                            |
| `C`                        | Open capability filter popup                                          |
| `m`                        | Mark selected model for compare                                       |
| `c`                        | Open compare view (marked vs selected)                                |
| `x`                        | Clear compare mark                                                    |
| `i`                        | Toggle installed-first sorting (any detected runtime provider)        |
| `d`                        | Download selected model (provider picker when multiple are available) |
| `r`                        | Refresh installed models from runtime providers                       |
| `Enter`                    | Toggle detail view for selected model                                 |
| `PgUp` / `PgDn`            | Scroll by 10                                                          |
| `g` / `G`                  | Jump to top / bottom                                                  |
| `q`                        | Quit                                                                  |

### Vim-like modes

The TUI uses Vim-inspired modes shown in the bottom-left status bar. The current mode determines which keys are active.

#### Normal mode

The default mode. Navigate, search, filter, and open views. All keys in the table above apply here.

#### Visual mode (`v`)

Select a contiguous range of models for bulk comparison. Press `v` to anchor at the current row, then navigate with `j`/`k` or arrow keys to extend the selection. Selected rows are highlighted.

| Key                 | Action                                                 |
|---------------------|--------------------------------------------------------|
| `j` / `k` or arrows | Extend selection up/down                               |
| `c`                 | Compare all selected models (opens multi-compare view) |
| `m`                 | Mark current model for two-model compare               |
| `Esc` or `v`        | Exit Visual mode                                       |

The multi-compare view displays a table where rows are attributes (Score, tok/s, Fit, Mem%, Params, Mode, Context, Quant, etc.) and columns are models. Best values are highlighted. Use `h`/`l` or arrow keys to scroll horizontally if more models are selected than fit on screen.

#### Select mode (`V`)

Column-based filtering. Press `V` (shift-v) to enter Select mode, then use `h`/`l` or arrow keys to move between column headers. The active column is visually highlighted. Press `Enter` or `Space` to activate the appropriate filter for that column:

| Column                        | Filter action                                                             |
|-------------------------------|---------------------------------------------------------------------------|
| Inst                          | Cycle availability filter                                                 |
| Model                         | Enter search mode                                                         |
| Provider                      | Open provider popup                                                       |
| Params                        | Open parameter-size bucket popup (<3B, 3-7B, 7-14B, 14-30B, 30-70B, 70B+) |
| Score, tok/s, Mem%, Ctx, Date | Sort by that column                                                       |
| Quant                         | Open quantization popup                                                   |
| Mode                          | Open run-mode popup (GPU, MoE, CPU+GPU, CPU)                              |
| Fit                           | Cycle fit filter                                                          |
| Use Case                      | Open use-case popup                                                       |

Row navigation (`j`/`k`) still works in Select mode so you can see the effect of filters as you apply them. Press `Esc` to return to Normal mode.

### TUI Plan mode (`p`)

Plan mode inverts normal fit analysis: instead of asking "what fits my hardware?", it estimates "what hardware is needed for this model config?".

Use `p` on a selected row, then:

| Key                    | Action                                                    |
|------------------------|-----------------------------------------------------------|
| `Tab` / `j` / `k`      | Move between editable fields (Context, Quant, Target TPS) |
| `Left` / `Right`       | Move cursor in current field                              |
| Type                   | Edit current field                                        |
| `Backspace` / `Delete` | Remove characters                                         |
| `Ctrl-U`               | Clear current field                                       |
| `Esc` or `q`           | Exit Plan mode                                            |

Plan mode shows estimates for:
- minimum and recommended VRAM/RAM/CPU cores
- feasible run paths (GPU, CPU offload, CPU-only)
- upgrade deltas to reach better fit targets

### Themes

Press `t` to cycle through 10 built-in color themes. Your selection is saved automatically to `~/.config/llmfit/theme` and restored on next launch.

| Theme                    | Description                                       |
|--------------------------|---------------------------------------------------|
| **Default**              | Original llmfit colors                            |
| **Dracula**              | Dark purple background with pastel accents        |
| **Solarized**            | Ethan Schoonover's Solarized Dark palette         |
| **Nord**                 | Arctic, cool blue-gray tones                      |
| **Monokai**              | Monokai Pro warm syntax colors                    |
| **Gruvbox**              | Retro groove palette with warm earth tones        |
| **Catppuccin Latte**     | 🌻 Light theme — harmonious pastel inversion      |
| **Catppuccin Frappé**    | 🪴 Low-contrast dark — muted, subdued aesthetic   |
| **Catppuccin Macchiato** | 🌺 Medium-contrast dark — gentle, soothing tones  |
| **Catppuccin Mocha**     | 🌿 Darkest variant — cozy with color-rich accents |

### Web dashboard

When you run `llmfit` in non-JSON mode, it automatically starts a background web dashboard on `0.0.0.0:8787`. Open it in any browser on the same network:

```
http://<your-machine-ip>:8787
```

Override the host or port with environment variables:

```sh
LLMFIT_DASHBOARD_HOST=0.0.0.0 LLMFIT_DASHBOARD_PORT=9000 llmfit
```

| Variable | Default | Description |
|---|---|---|
| `LLMFIT_DASHBOARD_HOST` | `0.0.0.0` | Interface to bind the dashboard server |
| `LLMFIT_DASHBOARD_PORT` | `8787` | Port to bind the dashboard server |

To disable the auto-started dashboard, pass `--no-dashboard`:

```sh
llmfit --no-dashboard
```

### CLI mode

Use `--cli` or any subcommand to get classic table output:

```sh
# Table of all models ranked by fit
llmfit --cli

# Only perfectly fitting models, top 5
llmfit fit --perfect -n 5

# Show detected system specs
llmfit system

# List all models in the database
llmfit list

# Search by name, provider, or size
llmfit search "llama 8b"

# Detailed view of a single model
llmfit info "Mistral-7B"

# Top 5 recommendations (JSON, for agent/script consumption)
llmfit recommend --json --limit 5

# Recommendations filtered by use case
llmfit recommend --json --use-case coding --limit 3

# Force a specific runtime (bypass automatic MLX selection on Apple Silicon)
llmfit recommend --force-runtime llamacpp
llmfit recommend --force-runtime llamacpp --use-case coding --limit 3

# Plan required hardware for a specific model configuration
llmfit plan "Qwen/Qwen3-4B-MLX-4bit" --context 8192
llmfit plan "Qwen/Qwen3-4B-MLX-4bit" --context 8192 --quant mlx-4bit
llmfit plan "Qwen/Qwen3-4B-MLX-4bit" --context 8192 --target-tps 25 --json

# Run as a node-level REST API (for cluster schedulers / aggregators)
llmfit serve --host 0.0.0.0 --port 8787
```

### REST API (`llmfit serve`)

`llmfit serve` starts an HTTP API that exposes the same fit/scoring data used by TUI/CLI, including filtering and top-model selection for a node.

```sh
# Liveness
curl http://localhost:8787/health

# Node hardware info
curl http://localhost:8787/api/v1/system

# Full fit list with filters
curl "http://localhost:8787/api/v1/models?min_fit=marginal&runtime=llamacpp&sort=score&limit=20"

# Key scheduling endpoint: top runnable models for this node
curl "http://localhost:8787/api/v1/models/top?limit=5&min_fit=good&use_case=coding"

# Search by model name/provider text
curl "http://localhost:8787/api/v1/models/Mistral?runtime=any"
```

Supported query params for `models`/`models/top`:

- `limit` (or `n`): max number of rows returned
- `perfect`: `true|false` (forces perfect-only when `true`)
- `min_fit`: `perfect|good|marginal|too_tight`
- `runtime`: `any|mlx|llamacpp`
- `use_case`: `general|coding|reasoning|chat|multimodal|embedding`
- `provider`: provider text filter (substring)
- `search`: free-text filter across name/provider/size/use-case
- `sort`: `score|tps|params|mem|ctx|date|use_case`
- `include_too_tight`: include non-runnable rows (default `false` on `/top`, `true` on `/models`)
- `max_context`: per-request context cap for memory estimation
- `force_runtime`: `mlx|llamacpp|vllm` — override automatic runtime selection during analysis

Validate API behavior locally:

```sh
# spawn server automatically and run endpoint/schema/filter assertions
python3 scripts/test_api.py --spawn

# or test an already-running server
python3 scripts/test_api.py --base-url http://127.0.0.1:8787
```

### GPU memory override

GPU VRAM autodetection can fail on some systems (e.g. broken `nvidia-smi`, VMs, passthrough setups). Use `--memory` to manually specify your GPU's VRAM:

```sh
# Override with 32 GB VRAM
llmfit --memory=32G

# Megabytes also work (32000 MB ≈ 31.25 GB)
llmfit --memory=32000M

# Works with all modes: TUI, CLI, and subcommands
llmfit --memory=24G --cli
llmfit --memory=24G fit --perfect -n 5
llmfit --memory=24G system
llmfit --memory=24G info "Llama-3.1-70B"
llmfit --memory=24G recommend --json
```

Accepted suffixes: `G`/`GB`/`GiB` (gigabytes), `M`/`MB`/`MiB` (megabytes), `T`/`TB`/`TiB` (terabytes). Case-insensitive. If no GPU was detected, the override creates a synthetic GPU entry so models are scored for GPU inference.

### Context-length cap for estimation

Use `--max-context` to cap context length used for memory estimation (without changing each model's advertised maximum context):

```sh
# Estimate memory fit at 4K context
llmfit --max-context 4096 --cli

# Works with subcommands
llmfit --max-conte
... [TRUNCATED]
```

### File: .release_please_manifest.json
```json
{
  ".": "0.3.7"
}

```

### File: AGENTS.md
```md
# AGENTS.md

Instructions for AI agents contributing to this codebase.

---

## Project overview

`llmfit` is a Rust CLI/TUI tool that matches LLM models against local system hardware (RAM, CPU, GPU). It detects system specs, loads a model database from embedded JSON, scores each model's fit, and presents results in an interactive terminal UI or classic table output.

## Language and toolchain

- Rust, edition 2024.
- Build with `cargo build`. Run with `cargo run`.
- No nightly features required. Stable toolchain only.
- Minimum supported Rust version: whatever edition 2024 requires (1.85+).

## Architecture

```
main.rs          Entrypoint. Parses CLI args via clap. Launches TUI by default,
                 falls back to CLI subcommands (system, list, fit, search, info)
                 or --cli flag for classic table output.

hardware.rs      SystemSpecs::detect() reads RAM/CPU via sysinfo crate.
                 detect_gpu() shells out to nvidia-smi / rocm-smi, and
                 detects Apple Silicon via system_profiler.
                 On unified memory (Apple Silicon), VRAM = system RAM.
                 No async. No unsafe.

models.rs        LlmModel struct. ModelDatabase loads from data/hf_models.json
                 embedded via include_str!() at compile time. No runtime file I/O.

fit.rs           FitLevel enum (Perfect, Good, Marginal, TooTight).
                 RunMode enum (Gpu, CpuOffload, CpuOnly).
                 ModelFit::analyze() compares a model against SystemSpecs,
                 selecting the best available execution path (GPU > CPU offload > CPU).
                 rank_models_by_fit() sorts by fit level, then run mode, then utilization.

display.rs       CLI-mode table rendering using the tabled crate.
                 Only used when --cli flag or subcommands are invoked.

tui_app.rs       TUI application state. Holds all models, filters (search text,
                 provider toggles, fit filter), selection index.
                 All filtering logic is here -- apply_filters() recomputes
                 filtered_fits indices whenever inputs change.

tui_ui.rs        Rendering with ratatui. Four layout regions: system bar,
                 search/filter bar, model table (or detail pane), status bar.
                 Stateless rendering -- reads from App, writes to Frame.

tui_events.rs    Keyboard event handling with crossterm. Two modes: Normal
                 (navigation, filter toggling, quit) and Search (text input).
```

## Data flow

1. `App::new()` calls `SystemSpecs::detect()` and `ModelDatabase::new()`.
2. Every model is analyzed into a `ModelFit` via `ModelFit::analyze()`.
3. Results are sorted by `rank_models_by_fit()`.
4. `apply_filters()` produces `filtered_fits: Vec<usize>` (indices into `all_fits`).
5. The TUI render loop reads `App` state and draws via `tui_ui::draw()`.
6. `tui_events::handle_events()` mutates `App` state, triggering re-render.

## Model database

- Source: `data/hf_models.json` (33 models).
- Generated by `scripts/scrape_hf_models.py` (Python, stdlib only, no pip deps).
- Embedded at compile time via `include_str!("../data/hf_models.json")`.
- Schema per entry: name, provider, parameter_count, min_ram_gb, recommended_ram_gb, min_vram_gb, quantization, context_length, use_case.
- `min_vram_gb` is VRAM needed for GPU inference. `min_ram_gb` is system RAM needed for CPU inference. Both are derived from the same parameter count.
- RAM formula: `params * 0.5 bytes (Q4_K_M) / 1024^3 * 1.2 overhead`.
- VRAM formula: `params * 0.5 bytes (Q4_K_M) / 1024^3 * 1.1 activation overhead`.
- Recommended RAM: `model_size * 2.0`.

Do not manually edit `hf_models.json`. Regenerate it by running the scraper:

```sh
python3 scripts/scrape_hf_models.py
```

The scraper has hardcoded fallback entries for gated models that require authentication.

## Conventions

- No `unsafe` code.
- No `.unwrap()` on user-facing paths. Use proper error handling or `expect()` with a descriptive message for internal invariants only.
- Fit levels are ordered: Perfect > Good > Marginal > TooTight. Do not add levels without updating `rank_models_by_fit()` sort logic.
- Fit is VRAM-first. GPU inference with sufficient VRAM is the ideal path. CPU inference via system RAM is a fallback. The `RunMode` enum tracks which memory pool is being used (Gpu, CpuOffload, CpuOnly).
- `min_vram_gb` is the VRAM needed to load model weights on GPU. `min_ram_gb` is the system RAM needed for CPU-only inference (same weights, loaded into RAM instead). They represent the same workload on different hardware paths.
- On Apple Silicon (unified memory), VRAM = system RAM. The `CpuOffload` path is skipped because there is no separate RAM pool to spill to. `SystemSpecs::unified_memory` tracks this.
- TUI rendering is stateless. `tui_ui::draw()` must not mutate `App`. Pass `&mut App` only for `TableState` widget requirements -- do not use it to change application state.
- Event handling in `tui_events.rs` is the sole place that mutates `App` in the TUI loop.
- Keep `display.rs` and `tui_*.rs` independent. The CLI path must work without initializing any TUI state.

## Adding a new model to the database

1. Add the model's HuggingFace repo ID to `TARGET_MODELS` in `scripts/scrape_hf_models.py`.
2. If the model is gated (requires HF auth), add a fallback entry to the `FALLBACK` dict in the same script.
3. Run `python3 scripts/scrape_hf_models.py`.
4. Verify the output in `data/hf_models.json`.
5. Run `cargo build` to verify compilation.

## Adding a new filter

1. Add the filter state to `App` in `tui_app.rs`.
2. Add filtering logic inside `apply_filters()`.
3. Add the keybinding in `tui_events.rs` (Normal mode handler).
4. Add the UI widget in `tui_ui.rs` (`draw_search_and_filters()` function).
5. Update the status bar help text in `draw_status_bar()`.

## Adding a new CLI subcommand

1. Add a variant to the `Commands` enum in `main.rs`.
2. Add the match arm in the `main()` function's command dispatch.
3. Use `display.rs` functions for output, or add new ones as needed.

## Testing

There are no tests yet. When adding tests:

- Unit tests for `fit.rs` logic (given known SystemSpecs and LlmModel values, assert correct FitLevel).
- Unit tests for `models.rs` (verify JSON parsing, search matching).
- Integration tests for CLI subcommands via `assert_cmd` crate.
- TUI is difficult to unit test. Keep rendering stateless and test the state mutations in `tui_app.rs` directly.

## Dependencies policy

- Prefer crates that are well-maintained and have minimal transitive dependencies.
- `sysinfo` is the system detection crate. Do not replace it with raw platform calls.
- `ratatui` + `crossterm` is the TUI stack. Do not mix in `termion` or `ncurses`.
- `clap` with derive feature for CLI parsing. Do not use manual arg parsing.
- The Python scraper uses only stdlib (`urllib`, `json`). Do not add pip dependencies.

## Common tasks

```sh
# Build
cargo build

# Run TUI
cargo run

# Run CLI mode
cargo run -- --cli

# Run specific subcommand
cargo run -- system
cargo run -- fit --perfect -n 5
cargo run -- search "llama"

# Refresh model database
python3 scripts/scrape_hf_models.py && cargo build

# Check for compilation issues
cargo check

# Format code
cargo fmt

# Lint
cargo clippy
```

## Platform notes

- GPU detection shells out to `nvidia-smi` (NVIDIA) and `rocm-smi` (AMD). These are best-effort and fail silently if unavailable.
- Apple Silicon detection uses `system_profiler SPDisplaysDataType`. On unified memory Macs, VRAM is reported as available system RAM (same pool).
- `sysinfo` handles cross-platform RAM/CPU. No conditional compilation needed.
- The TUI uses crossterm which works on Linux, macOS, and Windows terminals.

```

### File: API.md
```md
# llmfit REST API Guide

This document is for agent/client builders integrating with `llmfit serve`.

## Purpose

`llmfit serve` exposes node-local model fit analysis (same core data used by TUI/CLI) over HTTP and serves a local web dashboard.

Primary use case:
- Query each node in a cluster for top runnable models.
- Aggregate externally (scheduler/controller/UI) for placement decisions.

## Start the server

```sh
llmfit serve --port 8787
```

Global flags still apply:

```sh
llmfit --memory 24G --max-context 8192 serve --port 8787
```

## Base URL

Default local base URL:

```text
http://127.0.0.1:8787
```

To expose outside localhost, pass `--host 0.0.0.0`.

If you are building from source and want the dashboard embedded in `llmfit`, build web assets first:

```sh
cd llmfit-web && npm ci && npm run build
```

## Endpoints

### `GET /`
Web dashboard entrypoint (same-origin UI for fit exploration).

### `GET /health`
Liveness probe.

Example response:

```json
{
  "status": "ok",
  "node": {
    "name": "worker-1",
    "os": "linux"
  }
}
```

---

### `GET /api/v1/system`
Returns node identity + detected hardware.

Example response shape:

```json
{
  "node": {
    "name": "worker-1",
    "os": "linux"
  },
  "system": {
    "total_ram_gb": 62.23,
    "available_ram_gb": 41.08,
    "cpu_cores": 14,
    "cpu_name": "Intel(R) Core(TM) Ultra 7 165U",
    "has_gpu": false,
    "gpu_vram_gb": null,
    "gpu_name": null,
    "gpu_count": 0,
    "unified_memory": false,
    "backend": "CPU (x86)",
    "gpus": []
  }
}
```

---

### `GET /api/v1/models`
Returns filtered/sorted model-fit rows for this node.

Envelope shape:

```json
{
  "node": { "name": "worker-1", "os": "linux" },
  "system": { "...": "..." },
  "total_models": 23,
  "returned_models": 10,
  "filters": { "...": "echo of query state" },
  "models": [
    {
      "name": "Qwen/Qwen2.5-Coder-7B-Instruct",
      "provider": "Qwen",
      "parameter_count": "7B",
      "params_b": 7.0,
      "context_length": 32768,
      "use_case": "Coding",
      "category": "Coding",
      "release_date": "2025-03-14",
      "is_moe": false,
      "fit_level": "good",
      "fit_label": "Good",
      "run_mode": "gpu",
      "run_mode_label": "GPU",
      "score": 86.5,
      "score_components": {
        "quality": 87.0,
        "speed": 81.2,
        "fit": 90.1,
        "context": 88.0
      },
      "estimated_tps": 42.5,
      "runtime": "llamacpp",
      "runtime_label": "llama.cpp",
      "best_quant": "Q5_K_M",
      "memory_required_gb": 5.8,
      "memory_available_gb": 12.0,
      "utilization_pct": 48.3,
      "notes": [],
      "gguf_sources": []
    }
  ]
}
```

---

### `GET /api/v1/models/top`
Key scheduling endpoint. Same schema as `/api/v1/models`, but defaults to top 5 runnable entries.

Important behavior:
- Defaults `limit=5`.
- Excludes `too_tight` rows unless explicitly overridden (and top endpoint still keeps runnable semantics).

---

### `GET /api/v1/models/{name}`
Path-constrained search. Equivalent to a text search scoped by `{name}`.

Useful for:
- Client-side drilldown after selecting a model family.

## Query parameters

Supported on `/api/v1/models` and `/api/v1/models/top` (also `/api/v1/models/{name}`):

- `limit` (or alias `n`): max rows returned.
- `perfect`: `true|false` (when `true`, only perfect fits).
- `min_fit`: `perfect|good|marginal|too_tight`.
- `runtime`: `any|mlx|llamacpp`.
- `use_case`: `general|coding|reasoning|chat|multimodal|embedding`.
- `provider`: provider substring filter.
- `search`: free-text filter (name/provider/params/use-case/category).
- `sort`: `score|tps|params|mem|ctx|date|use_case`.
- `include_too_tight`: include unrunnable rows (defaults true for `/models`, false for `/models/top`).
- `max_context`: per-request context cap used by memory estimation.
- `force_runtime`: `mlx|llamacpp|vllm` — override automatic runtime selection during analysis (e.g. get llama.cpp recommendations on Apple Silicon instead of MLX).

## Error handling

Invalid filter values return HTTP 400:

```json
{
  "error": "invalid min_fit value: use perfect|good|marginal|too_tight"
}
```

Server errors return HTTP 500 with `{"error": "..."}`.

## Client integration recommendations

### 1) Polling pattern for schedulers
For each node agent:
1. Call `/health`.
2. Call `/api/v1/system`.
3. Call `/api/v1/models/top?limit=K&min_fit=good`.
4. Attach node metadata and forward to your central scheduler.

### 2) Conservative placement defaults
For production placement, prefer:

```text
min_fit=good
include_too_tight=false
sort=score
limit=5..20
```

### 3) Per-workload targeting
Examples:
- Coding workloads: `use_case=coding`
- Embedding workloads: `use_case=embedding`
- Runtime constrained to llama.cpp fleet: `runtime=llamacpp`

### 4) Stable parsing
Treat unknown fields as forward-compatible additions:
- Parse required fields you depend on.
- Ignore unknown fields.

## Curl examples

```sh
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/api/v1/system
curl "http://127.0.0.1:8787/api/v1/models?limit=20&min_fit=marginal&sort=score"
curl "http://127.0.0.1:8787/api/v1/models/top?limit=5&min_fit=good&use_case=coding"
curl "http://127.0.0.1:8787/api/v1/models/Mistral?runtime=any"
```

## Versioning notes

Current API prefix is `v1`.

If you build long-lived clients, pin to `/api/v1/...` and validate behavior with the local test script in `scripts/test_api.py`.

```

### File: CHANGELOG.md
```md
# Changelog

## [0.3.7](https://github.com/AlexsJones/llmfit/compare/v0.3.6...v0.3.7) (2026-02-21)


### Features

* add --memory flag to override GPU VRAM autodetection ([9a02f6e](https://github.com/AlexsJones/llmfit/commit/9a02f6e1616f59783ccff5b007c25213854f63b9))
* add --memory flag to override GPU VRAM autodetection ([39c5486](https://github.com/AlexsJones/llmfit/commit/39c5486aa3d94f9b9ef36e29642b64d848d0d2b0))
* add 15 popular models from HuggingFace ([128a020](https://github.com/AlexsJones/llmfit/commit/128a020323897a67ed5d12dd397bcf4924a6bf51))
* Add 15 popular models from HuggingFace (33→48 models) ([c45606b](https://github.com/AlexsJones/llmfit/commit/c45606bdb235b6bfe616bb616b1364a97e76f0c1))
* add homebrew tap support and update release workflow ([db09473](https://github.com/AlexsJones/llmfit/commit/db094734288d17a49d9c3c5c99859fe0d7dc976d))
* added arc support ([b5892fc](https://github.com/AlexsJones/llmfit/commit/b5892fc2ff313e71f57b7d793c7444d2aaadc0bd))
* added logo ([c21d416](https://github.com/AlexsJones/llmfit/commit/c21d4168f2bcd6da878848f9a6f97179d558606b))
* added moe ([ac7ffe4](https://github.com/AlexsJones/llmfit/commit/ac7ffe4ed79eb22ec43cf7bc20e8cd8d102d16a9))
* adding release please ([f2bfc7f](https://github.com/AlexsJones/llmfit/commit/f2bfc7fcf2587b74e05d8ad9d1041be6de456e69))
* append (WSL) to RAM label in tui when running under WSL ([e0397cf](https://github.com/AlexsJones/llmfit/commit/e0397cf51025b393b0d4024c4ae67200ee206390))
* caught some unavailable models on ollama ([b9f38da](https://github.com/AlexsJones/llmfit/commit/b9f38da9579040a7c2bada55838c5541474883ca))
* caught some unavailable models on ollama ([c0f7c20](https://github.com/AlexsJones/llmfit/commit/c0f7c20f61cdd9ae692de6ca66344befba2fafa9))
* detect installed Ollama models and support pulling from TUI ([4159aaf](https://github.com/AlexsJones/llmfit/commit/4159aaf304b3b421679f8231cf574465783d5b41))
* first pass ([855ad3d](https://github.com/AlexsJones/llmfit/commit/855ad3d34160cce6200c0ff128c34bcdcb0b922b))
* fixed up skill ([fcb712a](https://github.com/AlexsJones/llmfit/commit/fcb712a98ac785ad83ad689d5300f17cb80a3f1c))
* fixed up skill ([1f7d1de](https://github.com/AlexsJones/llmfit/commit/1f7d1de547a31202b9d34dd62bf543f5a22b2de7))
* fixing vram on apple bug ([5e08754](https://github.com/AlexsJones/llmfit/commit/5e087549c7c1523f4d5df72bd8a915330498a795))
* fixing vram on apple bug ([b3deca1](https://github.com/AlexsJones/llmfit/commit/b3deca1d9eac16283d0e9269c68a1af1dfc871ab))
* fixing vram on apple bug ([92ddb0e](https://github.com/AlexsJones/llmfit/commit/92ddb0e82579c6018d1acb4e3dfbe1df7d582605))
* fixing vram on apple bug ([42b2081](https://github.com/AlexsJones/llmfit/commit/42b2081577bed23176c0f87d1ad0b142cce23872))
* improvements based on [#12](https://github.com/AlexsJones/llmfit/issues/12) ([5428ef8](https://github.com/AlexsJones/llmfit/commit/5428ef8cdd42e88bced1459b55b480aab767637c))
* increased model count ([156b29d](https://github.com/AlexsJones/llmfit/commit/156b29deb077a1d66948254b370597a118fd5daf))
* increment version ([283bebb](https://github.com/AlexsJones/llmfit/commit/283bebb8eca5da2fc7124b665ae773fda48aed93))
* overall to the scoring system ([f475938](https://github.com/AlexsJones/llmfit/commit/f4759381d23b834e0a42a4699d23fb3f858fe677))
* overall to the scoring system ([b0696cf](https://github.com/AlexsJones/llmfit/commit/b0696cf297f1cb11247493355406d8b9c56510db))
* overall to the scoring system ([37e2e10](https://github.com/AlexsJones/llmfit/commit/37e2e10076f450f79165d92541baf04957ec2fe9))
* plumbing 2 ([1c615bb](https://github.com/AlexsJones/llmfit/commit/1c615bb57b7395f9be888245f8157dec2bab8bb4))
* plumbing 2 ([dd6a3ec](https://github.com/AlexsJones/llmfit/commit/dd6a3ec20e09ae72eada1fada73a6392c9673221))
* pull functionality ([923e7e7](https://github.com/AlexsJones/llmfit/commit/923e7e7463dd2bd53b6438ad3c8f2eb1f7a45af4))
* release plumbing ([7d21719](https://github.com/AlexsJones/llmfit/commit/7d217192bc1638f7ff69a22c2467d7d86da96641))
* release plumbing ([3accbb4](https://github.com/AlexsJones/llmfit/commit/3accbb42c99321fb6f8ade9d2f07af0fee93ed9e))
* reworked available models for download ([9adc84f](https://github.com/AlexsJones/llmfit/commit/9adc84f3041dca14fdcdc4437409b2b81eaca5a3))
* support for windows vulkan ([cc0fd61](https://github.com/AlexsJones/llmfit/commit/cc0fd619fa31e01c398c3c23f45aa915005670c8))
* supporting 94 models ([a652be3](https://github.com/AlexsJones/llmfit/commit/a652be31dd0cbe36f89572de7022e2a145fb3788))
* updated build actions ([1e65fdd](https://github.com/AlexsJones/llmfit/commit/1e65fddecb5f183870ddf1aa865dcaddba47523a))
* updated images ([9141109](https://github.com/AlexsJones/llmfit/commit/9141109f753ef38eb2b2eb5c604edb6ee0d7e371))
* updated models ([2d6c1d6](https://github.com/AlexsJones/llmfit/commit/2d6c1d66708186c0a21cb2f082a5b4e2fb03db90))
* updated tui to support multiple providers better and also multiple GPU support ([a3ca0bd](https://github.com/AlexsJones/llmfit/commit/a3ca0bd64647fa958c15bb7038a9e02df175fe67))
* updated urls ([f75ec27](https://github.com/AlexsJones/llmfit/commit/f75ec2750f325ff73725e5b8b194ba854c8579e9))
* updated version ([2cfc73e](https://github.com/AlexsJones/llmfit/commit/2cfc73ebdb6214f801e32880ff6451b2809bbb45))


### Bug Fixes

* correctly estimate VRAM for APU integrated GPUs ([72c8cb0](https://github.com/AlexsJones/llmfit/commit/72c8cb0e7873e0a8bcf4a10aee877bc38555299c))
* correctly estimate VRAM for APU integrated GPUs (Radeon Graphics) ([8da5c2a](https://github.com/AlexsJones/llmfit/commit/8da5c2a0443b73a3ac78ac087b0f08acdba6aaa9)), closes [#25](https://github.com/AlexsJones/llmfit/issues/25)
* update OpenClaw skill to match actual CLI output ([f38a0e5](https://github.com/AlexsJones/llmfit/commit/f38a0e56ef332bde8f3b03f8b06b5982fe90c1cc))
* update OpenClaw skill to match actual CLI output ([e1adbfd](https://github.com/AlexsJones/llmfit/commit/e1adbfd0abd786bc7a99496f20a7f81070bc8fe3))

## [0.3.6](https://github.com/AlexsJones/llmfit/compare/llmfit-v0.3.5...llmfit-v0.3.6) (2026-02-21)


### Features

* release plumbing ([7d21719](https://github.com/AlexsJones/llmfit/commit/7d217192bc1638f7ff69a22c2467d7d86da96641))
* release plumbing ([3accbb4](https://github.com/AlexsJones/llmfit/commit/3accbb42c99321fb6f8ade9d2f07af0fee93ed9e))

## [0.3.5](https://github.com/AlexsJones/llmfit/compare/llmfit-v0.3.4...llmfit-v0.3.5) (2026-02-21)


### Features

* add --memory flag to override GPU VRAM autodetection ([9a02f6e](https://github.com/AlexsJones/llmfit/commit/9a02f6e1616f59783ccff5b007c25213854f63b9))
* add --memory flag to override GPU VRAM autodetection ([39c5486](https://github.com/AlexsJones/llmfit/commit/39c5486aa3d94f9b9ef36e29642b64d848d0d2b0))
* add 15 popular models from HuggingFace ([128a020](https://github.com/AlexsJones/llmfit/commit/128a020323897a67ed5d12dd397bcf4924a6bf51))
* Add 15 popular models from HuggingFace (33→48 models) ([c45606b](https://github.com/AlexsJones/llmfit/commit/c45606bdb235b6bfe616bb616b1364a97e76f0c1))
* add homebrew tap support and update release workflow ([db09473](https://github.com/AlexsJones/llmfit/commit/db094734288d17a49d9c3c5c99859fe0d7dc976d))
* added arc support ([b5892fc](https://github.com/AlexsJones/llmfit/commit/b5892fc2ff313e71f57b7d793c7444d2aaadc0bd))
* added logo ([c21d416](https://github.com/AlexsJones/llmfit/commit/c21d4168f2bcd6da878848f9a6f97179d558606b))
* added moe ([ac7ffe4](https://github.com/AlexsJones/llmfit/commit/ac7ffe4ed79eb22ec43cf7bc20e8cd8d102d16a9))
* adding release please ([f2bfc7f](https://github.com/AlexsJones/llmfit/commit/f2bfc7fcf2587b74e05d8ad9d1041be6de456e69))
* append (WSL) to RAM label in tui when running under WSL ([e0397cf](https://github.com/AlexsJones/llmfit/commit/e0397cf51025b393b0d4024c4ae67200ee206390))
* caught some unavailable models on ollama ([b9f38da](https://github.com/AlexsJones/llmfit/commit/b9f38da9579040a7c2bada55838c5541474883ca))
* caught some unavailable models on ollama ([c0f7c20](https://github.com/AlexsJones/llmfit/commit/c0f7c20f61cdd9ae692de6ca66344befba2fafa9))
* detect installed Ollama models and support pulling from TUI ([4159aaf](https://github.com/AlexsJones/llmfit/commit/4159aaf304b3b421679f8231cf574465783d5b41))
* first pass ([855ad3d](https://github.com/AlexsJones/llmfit/commit/855ad3d34160cce6200c0ff128c34bcdcb0b922b))
* fixed up skill ([fcb712a](https://github.com/AlexsJones/llmfit/commit/fcb712a98ac785ad83ad689d5300f17cb80a3f1c))
* fixed up skill ([1f7d1de](https://github.com/AlexsJones/llmfit/commit/1f7d1de547a31202b9d34dd62bf543f5a22b2de7))
* fixing vram on apple bug ([5e08754](https://github.com/AlexsJones/llmfit/commit/5e087549c7c1523f4d5df72bd8a915330498a795))
* fixing vram on apple bug ([b3deca1](https://github.com/AlexsJones/llmfit/commit/b3deca1d9eac16283d0e9269c68a1af1dfc871ab))
* fixing vram on apple bug ([92ddb0e](https://github.com/AlexsJones/llmfit/commit/92ddb0e82579c6018d1acb4e3dfbe1df7d582605))
* fixing vram on apple bug ([42b2081](https://github.com/AlexsJones/llmfit/commit/42b2081577bed23176c0f87d1ad0b142cce23872))
* improvements based on [#12](https://github.com/AlexsJones/llmfit/issues/12) ([5428ef8](https://github.com/AlexsJones/llmfit/commit/5428ef8cdd42e88bced1459b55b480aab767637c))
* increased model count ([156b29d](https://github.com/AlexsJones/llmfit/commit/156b29deb077a1d66948254b370597a118fd5daf))
* increment version ([283bebb](https://github.com/AlexsJones/llmfit/commit/283bebb8eca5da2fc7124b665ae773fda48aed93))
* overall to the scoring system ([f475938](https://github.com/AlexsJones/llmfit/commit/f4759381d23b834e0a42a4699d23fb3f858fe677))
* overall to the scoring system ([b0696cf](https://github.com/AlexsJones/llmfit/commit/b0696cf297f1cb11247493355406d8b9c56510db))
* overall to the scoring system ([37e2e10](https://github.com/AlexsJones/llmfit/commit/37e2e10076f450f79165d92541baf04957ec2fe9))
* pull functionality ([923e7e7](https://github.com/AlexsJones/llmfit/commit/923e7e7463dd2bd53b6438ad3c8f2eb1f7a45af4))
* reworked available models for download ([9adc84f](https://github.com/AlexsJones/llmfit/commit/9adc84f3041dca14fdcdc4437409b2b81eaca5a3))
* support for windows vulkan ([cc0fd61](https://github.com/AlexsJones/llmfit/commit/cc0fd619fa31e01c398c3c23f45aa915005670c8))
* supporting 94 models ([a652be3](https://github.com/AlexsJones/llmfit/commit/a652be31dd0cbe36f89572de7022e2a145fb3788))
* updated build actions ([1e65fdd](https://github.com/AlexsJones/llmfit/commit/1e65fddecb5f183870ddf1aa865dcaddba47523a))
* updated images ([9141109](https://github.com/AlexsJones/llmfit/commit/9141109f753ef38eb2b2eb5c604edb6ee0d7e371))
* updated models ([2d6c1d6](https://github.com/AlexsJones/llmfit/commit/2d6c1d66708186c0a21cb2f082a5b4e2fb03db90))
* updated tui to support multiple providers better and also multiple GPU support ([a3ca0bd](https://github.com/AlexsJones/llmfit/commit/a3ca0bd64647fa958c15bb7038a9e02df175fe67))
* updated urls ([f75ec27](https://github.com/AlexsJones/llmfit/commit/f75ec2750f325ff73725e5b8b194ba854c8579e9))
* updated version ([2cfc73e](https://github.com/AlexsJones/llmfit/commit/2cfc73ebdb6214f801e32880ff6451b2809bbb45))


### Bug Fixes

* correctly estimate VRAM for APU integrated GPUs ([72c8cb0](https://github.com/AlexsJones/llmfit/commit/72c8cb0e7873e0a8bcf4a10aee877bc38555299c))
* correctly estimate VRAM for APU integrated GPUs (Radeon Graphics) ([8da5c2a](https://github.com/AlexsJones/llmfit/commit/8da5c2a0443b73a3ac78ac087b0f08acdba6aaa9)), closes [#25](https://github.com/AlexsJones/llmfit/issues/25)
* update OpenClaw skill to match actual CLI output ([f38a0e5](https://github.com/AlexsJones/llmfit/commit/f38a0e56ef332bde8f3b03f8b06b5982fe90c1cc))
* update OpenClaw skill to match actual CLI output ([e1adbfd](https://github.com/AlexsJones/llmfit/commit/e1adbfd0abd786bc7a99496f20a7f81070bc8fe3))

```

### File: index.html
```html
<html>
<head>
  <meta charset="utf-8">
  <title>llmfit</title>
</head>
<body>
  <h1>llmfit</h1>
  <p>Match LLM models to your hardware.</p>
  <pre>curl -fsSL https://llmfit.axjns.dev/install.sh | sh</pre>
  <p><a href="https://github.com/AlexsJones/llmfit">GitHub</a></p>
</body>
</html>

```

### File: install.sh
```sh
#!/bin/sh
# llmfit installer
# Usage: curl -fsSL https://raw.githubusercontent.com/AlexsJones/llmfit/main/install.sh | sh
#        curl -fsSL ... | sh -s -- --local   # Install to ~/.local/bin (no sudo)
#
# Downloads the latest llmfit release from GitHub and installs
# the binary to /usr/local/bin (or ~/.local/bin with --local or if no sudo).
# Supports piped execution: sudo prompts read from /dev/tty when stdin is a pipe.

set -e

REPO="AlexsJones/llmfit"
BINARY="llmfit"
LOCAL_INSTALL=""

# --- helpers ---

info() { printf '  \033[1;34m>\033[0m %s\n' "$*"; }
warn() { printf '  \033[1;33m>\033[0m %s\n' "$*"; }
err()  { printf '  \033[1;31m!\033[0m %s\n' "$*" >&2; exit 1; }

need() {
    command -v "$1" >/dev/null 2>&1 || err "Required tool '$1' not found. Please install it and try again."
}

# --- parse arguments ---

parse_args() {
    while [ $# -gt 0 ]; do
        case "$1" in
            --local|-l)
                LOCAL_INSTALL="1"
                ;;
            --help|-h)
                echo "Usage: install.sh [OPTIONS]"
                echo ""
                echo "Options:"
                echo "  --local, -l    Install to ~/.local/bin (no sudo required)"
                echo "  --help, -h     Show this help message"
                exit 0
                ;;
            *)
                warn "Unknown option: $1"
                ;;
        esac
        shift
    done
}

# --- detect platform ---

detect_platform() {
    OS="$(uname -s)"
    ARCH="$(uname -m)"

    case "$OS" in
        Linux)  OS="unknown-linux-musl" ;;
        Darwin) OS="apple-darwin" ;;
        *)      err "Unsupported OS: $OS" ;;
    esac

    case "$ARCH" in
        x86_64|amd64)   ARCH="x86_64" ;;
        aarch64|arm64)  ARCH="aarch64" ;;
        *)              err "Unsupported architecture: $ARCH" ;;
    esac

    PLATFORM="${ARCH}-${OS}"
}

# --- fetch latest release ---

fetch_latest_tag() {
    need curl
    need tar

    # Use the releases redirect instead of the API to avoid GitHub's
    # 60-request/hour rate limit on unauthenticated API calls (403).
    TAG="$(curl -fsSI "https://github.com/${REPO}/releases/latest" 2>/dev/null \
        | grep -i '^location:' \
        | head -1 \
        | sed 's|.*/tag/||' \
        | tr -d '\r\n')"

    [ -n "$TAG" ] || err "Could not determine latest release. Check https://github.com/${REPO}/releases"
}

# --- checksum verification ---

verify_checksum() {
    CHECKSUM_FILE="${TMPDIR}/${ASSET}.sha256"

    # Attempt to download the checksum file (-f exits non-zero on HTTP 4xx/5xx)
    if ! curl -fsSL --max-time 10 "${URL}.sha256" -o "$CHECKSUM_FILE" 2>/dev/null; then
        warn "No checksum file found for this release — skipping integrity check"
        return
    fi

    info "Verifying checksum..."
    if command -v sha256sum >/dev/null 2>&1; then
        (cd "$TMPDIR" && sha256sum -c "${ASSET}.sha256" --quiet) \
            || err "Checksum verification failed. The download may be corrupted or tampered with."
    elif command -v shasum >/dev/null 2>&1; then
        (cd "$TMPDIR" && shasum -a 256 -q -c "${ASSET}.sha256") \
            || err "Checksum verification failed. The download may be corrupted or tampered with."
    else
        warn "Neither sha256sum nor shasum available — skipping integrity check"
    fi
}

# --- download and install ---

install() {
    ASSET="${BINARY}-${TAG}-${PLATFORM}.tar.gz"
    URL="https://github.com/${REPO}/releases/download/${TAG}/${ASSET}"

    TMPDIR="$(mktemp -d)"
    trap 'rm -rf "$TMPDIR"' EXIT

    info "Downloading ${BINARY} ${TAG} for ${PLATFORM}..."
    curl -fsSL "$URL" -o "${TMPDIR}/${ASSET}" \
        || err "Download failed. Asset '${ASSET}' may not exist for your platform.\n  Check: https://github.com/${REPO}/releases/tag/${TAG}"

    verify_checksum

    info "Extracting..."
    tar -xzf "${TMPDIR}/${ASSET}" -C "$TMPDIR"

    # Find the binary in the extracted contents
    BIN="$(find "$TMPDIR" -name "$BINARY" -type f | head -1)"
    [ -n "$BIN" ] || err "Binary not found in archive. Release asset may have an unexpected layout."
    chmod +x "$BIN"

    # Determine install directory
    if [ -n "$LOCAL_INSTALL" ]; then
        # User explicitly requested local install
        INSTALL_DIR="${HOME}/.local/bin"
        mkdir -p "$INSTALL_DIR"
        info "Installing to ${INSTALL_DIR} (--local mode)..."
    elif [ -w /usr/local/bin ]; then
        # /usr/local/bin is writable without sudo
        INSTALL_DIR="/usr/local/bin"
    elif command -v sudo >/dev/null 2>&1; then
        # sudo is available — use /dev/tty for password prompt when stdin is a pipe
        info "Installing to /usr/local/bin (requires sudo)..."
        if [ -t 0 ]; then
            SUDO_ASKPASS="" sudo mv "$BIN" "/usr/local/bin/${BINARY}"
        elif [ -e /dev/tty ]; then
            SUDO_ASKPASS="" sudo mv "$BIN" "/usr/local/bin/${BINARY}" </dev/tty
        else
            false
        fi
        if [ $? -eq 0 ]; then
            info "Installed ${BINARY} to /usr/local/bin/${BINARY}"
            return
        else
            warn "sudo failed, falling back to ~/.local/bin"
            INSTALL_DIR="${HOME}/.local/bin"
            mkdir -p "$INSTALL_DIR"
        fi
    else
        # No write access and no interactive sudo, use local install
        INSTALL_DIR="${HOME}/.local/bin"
        mkdir -p "$INSTALL_DIR"
        info "Installing to ${INSTALL_DIR} (no sudo available)..."
    fi

    mv "$BIN" "${INSTALL_DIR}/${BINARY}"
    info "Installed ${BINARY} to ${INSTALL_DIR}/${BINARY}"

    # Check if install dir is in PATH
    case ":$PATH:" in
        *":${INSTALL_DIR}:"*) ;;
        *)
            warn "Add ${INSTALL_DIR} to your PATH to use '${BINARY}' directly:"
            echo ""
            echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
            echo ""
            ;;
    esac
}

# --- main ---

main() {
    parse_args "$@"
    info "llmfit installer"
    detect_platform
    fetch_latest_tag
    install
    info "Done. Run '${BINARY}' to get started."
}

main "$@"

```

### File: MODELS.md
```md
# Supported Models

llmfit ships with a curated database of 106 LLM models from HuggingFace. All memory estimates assume Q4_K_M quantization (0.5 bytes per parameter) unless noted otherwise.

### 01.ai

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [01-ai/Yi-6B-Chat](https://huggingface.co/01-ai/Yi-6B-Chat) | 6.1B | Q4_K_M | 4k | Instruction following, chat |
| [01-ai/Yi-34B-Chat](https://huggingface.co/01-ai/Yi-34B-Chat) | 34.4B | Q4_K_M | 4k | Instruction following, chat |

### Alibaba

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 600M | Q4_K_M | 40k | Lightweight, edge deployment |
| [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | 873M | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3.5-0.8B-Base](https://huggingface.co/Qwen/Qwen3.5-0.8B-Base) | 873M | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) | 1.5B | Q4_K_M | 32k | Code generation and completion |
| [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 1.7B | Q4_K_M | 40k | Lightweight, edge deployment |
| [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | 2.3B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3.5-2B-Base](https://huggingface.co/Qwen/Qwen3.5-2B-Base) | 2.3B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) | 3.8B | Q4_K_M | 32k | Multimodal, vision and text |
| [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) | 4.0B | Q4_K_M | 40k | General purpose text generation |
| [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) | 4.7B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3.5-4B-Base](https://huggingface.co/Qwen/Qwen3.5-4B-Base) | 4.7B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) | 7.6B | Q4_K_M | 32k | Instruction following, chat |
| [Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | 7.6B | Q4_K_M | 32k | Code generation and completion |
| [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 8.2B | Q4_K_M | 40k | General purpose text generation |
| [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) | 8.3B | Q4_K_M | 32k | Multimodal, vision and text |
| [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) | 9.7B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3.5-9B-Base](https://huggingface.co/Qwen/Qwen3.5-9B-Base) | 9.7B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | 14.8B | Q4_K_M | 128k | Instruction following, chat |
| [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | 14.8B | Q4_K_M | 128k | General purpose text generation |
| [Qwen/Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | 14.8B | Q4_K_M | 32k | Code generation and completion |
| [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) | 27.8B | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) | 30.5B (MoE) | Q4_K_M | 40k | Efficient MoE, general purpose |
| [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | 36.0B (MoE) | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) | 32.5B | Q4_K_M | 128k | Instruction following, chat |
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 32.8B | Q4_K_M | 40k | General purpose text generation |
| [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | 32.8B | Q4_K_M | 32k | Code generation and completion |
| [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) | 72.7B | Q4_K_M | 32k | Instruction following, chat |
| [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | 125.1B (MoE) | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | 235B (MoE) | Q4_K_M | 40k | State-of-the-art, MoE architecture |
| [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | 403.4B (MoE) | Q4_K_M | 256k | Multimodal, vision and text |
| [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | 480B (MoE) | Q4_K_M | 256k | Code generation and completion |

### Allen Institute

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [allenai/OLMo-2-0325-32B-Instruct](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct) | 32B | Q4_K_M | 4k | Fully open-source, instruction following |

### Ant Group

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [inclusionAI/Ling-lite](https://huggingface.co/inclusionAI/Ling-lite) | 16.8B (MoE) | Q4_K_M | 128k | Efficient MoE, general purpose |

### BAAI

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) | 335M | Q4_K_M | 512 | Text embeddings for RAG |

### Baidu

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [baidu/ERNIE-4.5-300B-A47B-Paddle](https://huggingface.co/baidu/ERNIE-4.5-300B-A47B-Paddle) | 300B (MoE) | Q4_K_M | 128k | Multilingual, reasoning |

### BigCode

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [bigcode/starcoder2-7b](https://huggingface.co/bigcode/starcoder2-7b) | 7.2B | Q4_K_M | 16k | Code generation and completion |
| [bigcode/starcoder2-15b](https://huggingface.co/bigcode/starcoder2-15b) | 15.7B | Q4_K_M | 16k | Code generation and completion |

### BigScience

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [bigscience/bloom](https://huggingface.co/bigscience/bloom) | 176B | Q4_K_M | 2k | Multilingual text generation |

### Cohere

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [CohereForAI/c4ai-command-r-v01](https://huggingface.co/CohereForAI/c4ai-command-r-v01) | 35B | Q4_K_M | 128k | RAG, tool use, agents |

### Community

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) | 1.1B | Q4_K_M | 2k | Instruction following, chat |

### DeepSeek

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) | 7.6B | Q4_K_M | 128k | Advanced reasoning, chain-of-thought |
| [deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) | 16B (MoE) | Q4_K_M | 128k | Code generation and completion |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | 32.8B | Q4_K_M | 128k | Advanced reasoning, chain-of-thought |
| [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | 671B (MoE) | Q4_K_M | 128k | Advanced reasoning, chain-of-thought |
| [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 685B (MoE) | Q4_K_M | 128k | State-of-the-art, MoE architecture |

### Google

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) | 1B | Q4_K_M | 32k | Lightweight, edge deployment |
| [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it) | 2.6B | Q4_K_M | 4k | General purpose text generation |
| [google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) | 4B | Q4_K_M | 128k | Lightweight, general purpose |
| [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) | 9.2B | Q4_K_M | 4k | General purpose text generation |
| [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 12B | Q4_K_M | 128k | Multimodal, vision and text |
| [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 27B | Q4_K_M | 128k | General purpose text generation |
| [google/gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it) | 27.2B | Q4_K_M | 4k | General purpose text generation |

### HuggingFace

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) | 7.2B | Q4_K_M | 32k | General purpose text generation |

### IBM

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [ibm-granite/granite-4.0-h-micro](https://huggingface.co/ibm-granite/granite-4.0-h-micro) | 3B | Q4_K_M | 128k | Enterprise, hybrid Mamba/transformer |
| [ibm-granite/granite-4.0-h-tiny](https://huggingface.co/ibm-granite/granite-4.0-h-tiny) | 7B (MoE) | Q4_K_M | 128k | Enterprise, hybrid Mamba/transformer |
| [ibm-granite/granite-3.1-8b-instruct](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct) | 8.1B | Q4_K_M | 128k | Enterprise, instruction following |
| [ibm-granite/granite-4.0-h-small](https://huggingface.co/ibm-granite/granite-4.0-h-small) | 32B (MoE) | Q4_K_M | 128k | Enterprise, hybrid Mamba/transformer |

### LMSYS

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [lmsys/vicuna-7b-v1.5](https://huggingface.co/lmsys/vicuna-7b-v1.5) | 7.0B | Q4_K_M | 4k | Instruction following, chat |
| [lmsys/vicuna-13b-v1.5](https://huggingface.co/lmsys/vicuna-13b-v1.5) | 13.0B | Q4_K_M | 4k | Instruction following, chat |

### Meituan

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [meituan/LongCat-Flash](https://huggingface.co/meituan/LongCat-Flash) | 560B (MoE) | Q4_K_M | 512k | Long context MoE |

### Meta

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) | 1.2B | Q4_K_M | 4k | General purpose text generation |
| [meta-llama/Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B) | 3.2B | Q4_K_M | 4k | General purpose text generation |
| [meta-llama/CodeLlama-7b-Instruct-hf](https://huggingface.co/meta-llama/CodeLlama-7b-Instruct-hf) | 6.7B | Q4_K_M | 4k | Code generation and completion |
| [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) | 8.0B | Q4_K_M | 4k | General purpose text generation |
| [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | 8.0B | Q4_K_M | 4k | Instruction following, chat |
| [meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) | 10.7B | Q4_K_M | 4k | Instruction following, chat |
| [meta-llama/CodeLlama-13b-Instruct-hf](https://huggingface.co/meta-llama/CodeLlama-13b-Instruct-hf) | 13.0B | Q4_K_M | 4k | Code generation and completion |
| [meta-llama/CodeLlama-34b-Instruct-hf](https://huggingface.co/meta-llama/CodeLlama-34b-Instruct-hf) | 33.7B | Q4_K_M | 4k | Code generation and completion |
| [meta-llama/Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) | 70.6B | Q4_K_M | 4k | Instruction following, chat |
| [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | 70.6B | Q4_K_M | 128k | Instruction following, chat |
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 109B (MoE) | Q4_K_M | 128k | Multimodal, vision and text |
| [meta-llama/Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 400B (MoE) | Q4_K_M | 128k | Multimodal, vision and text |
| [meta-llama/Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) | 405.9B | Q4_K_M | 4k | Instruction following, chat |

### Microsoft

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [microsoft/phi-3-mini-4k-instruct](https://huggingface.co/microsoft/phi-3-mini-4k-instruct) | 3.8B | Q4_K_M | 4k | Lightweight, edge deployment |
| [microsoft/Phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct) | 3.8B | Q4_K_M | 128k | Lightweight, long context |
| [microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) | 3.8B | Q4_K_M | 128k | Lightweight, edge deployment |
| [microsoft/Orca-2-7b](https://huggingface.co/microsoft/Orca-2-7b) | 7.0B | Q4_K_M | 4k | Reasoning, step-by-step solutions |
| [microsoft/Orca-2-13b](https://huggingface.co/microsoft/Orca-2-13b) | 13.0B | Q4_K_M | 4k | Reasoning, step-by-step solutions |
| [microsoft/phi-4](https://huggingface.co/microsoft/phi-4) | 14B | Q4_K_M | 16k | Reasoning, STEM, code generation |
| [microsoft/Phi-3-medium-14b-instruct](https://huggingface.co/microsoft/Phi-3-medium-14b-instruct) | 14B | Q4_K_M | 4k | Balanced performance and size |

### Mistral AI

| Model | Parameters | Quantization | Context | Use Case |
|-------|-----------|--------------|---------|----------|
| [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | 7.2B | Q4_K_M | 32k | Instruction following, chat |
| [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) | 8.0B | Q4_K_M | 32k | Instruction following, chat |
| [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | 12.2B | Q4_K_M | 128k | Instruction following, chat |
| [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | 24B | Q4_K_M | 32k | Instruction following, chat |
| [mistralai/Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | 24B | Q4_K_M | 128k | Multimodal, vision and text |
| [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) | 46.7B (MoE) | Q4_K_M | 32k | Instruction following, chat |
| [mistralai/Mistral-Large-Instruct
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
