---
id: moneyprinter
type: knowledge
owner: OA_Triage
---
# moneyprinter
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# MoneyPrinter 💸

Sponsored by Post Bridge

<a href="https://www.post-bridge.com/?ref=moneyprinter">
  <img src="docs/repo/PostBridgeBanner.png" alt="Post Bridge integration banner" width="720" />
</a>

---

> 𝕏 Also, follow me on X: [@DevBySami](https://x.com/DevBySami).

Automate the creation of YouTube Shorts by providing a video topic.

MoneyPrinter is Ollama-first: script generation and metadata are fully powered by local Ollama models.

MoneyPrinter now uses a DB-backed generation queue (API + worker + Postgres in Docker) for reliable, restart-safe processing.

<a href="https://trendshift.io/repositories/7545" target="_blank"><img src="https://trendshift.io/api/badge/repositories/7545" alt="FujiwaraChoki%2FMoneyPrinter | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

> **Important** Please make sure you look through existing/closed issues before opening your own. If it's just a question, please join our [discord](https://dsc.gg/fuji-community) and ask there.

> **🎥** Watch the video on [YouTube](https://youtu.be/mkZsaDA2JnA?si=pNne3MnluRVkWQbE).

## Documentation

Docs are centralized in [`docs/`](docs/README.md):

- [Interactive Setup Script](setup.sh)
- [Quickstart](docs/quickstart.md)
- [Configuration](docs/configuration.md)
- [Architecture](docs/architecture.md)
- [Docker](docs/docker.md)
- [Testing](docs/testing.md)
- [Troubleshooting](docs/troubleshooting.md)

## FAQ 🤔

### Which AI provider does MoneyPrinter use?

MoneyPrinter is fully Ollama-based. Start Ollama, pull a model, and select the model in the UI.

```bash
ollama serve
ollama pull llama3.1:8b
```

### How do I get the TikTok session ID?

You can obtain your TikTok session ID by logging into TikTok in your browser and copying the value of the `sessionid` cookie.

### My ImageMagick binary is not being detected

MoneyPrinter auto-detects ImageMagick from your `PATH` on Linux, macOS, and Windows. If auto-detection fails, set the executable path manually in `.env`, for example:

```env
IMAGEMAGICK_BINARY="C:\\Program Files\\ImageMagick-7.1.0-Q16\\magick.exe"
```

Don't forget to use double backslashes (`\\`) in the path, instead of one.

### I can't install `playsound`: Wheel failed to build

If you're having trouble installing `playsound`, you can try installing it using the following command:

```bash
uv pip install -U wheel
uv pip install -U playsound
```

If you were not able to find your solution, check [Troubleshooting](docs/troubleshooting.md), ask in Discord, or create an issue.

## Donate 🎁

If you like and enjoy `MoneyPrinter`, and would like to donate, you can do that by clicking on the button on the right hand side of the repository. ❤️
You will have your name (and/or logo) added to this repository as a supporter as a sign of appreciation.

## Contributing 🤝

Pull Requests will not be accepted for the time-being.

## Star History 🌟

[![Star History Chart](https://api.star-history.com/svg?repos=FujiwaraChoki/MoneyPrinter&type=Date)](https://star-history.com/#FujiwaraChoki/MoneyPrinter&Date)

## License 📝

See [`LICENSE`](LICENSE) file for more information.

```

### File: Backend\main.py
```py
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import and_, case, select

from db import SessionLocal, init_db
from gpt import list_ollama_models
from logstream import log
from repository import create_job, get_job, list_job_events, request_cancel
from utils import ENV_FILE, SONGS_DIR, check_env_vars, clean_dir


load_dotenv(ENV_FILE)
check_env_vars()
init_db()

app = Flask(__name__)
CORS(app)

HOST = "0.0.0.0"
PORT = 8080


@app.route("/api/models", methods=["GET"])
def models():
    try:
        available_models, default_model = list_ollama_models()
        return jsonify(
            {
                "status": "success",
                "models": available_models,
                "default": default_model,
            }
        )
    except Exception as err:
        log(f"[-] Error fetching Ollama models: {str(err)}", "error")
        return jsonify(
            {
                "status": "error",
                "message": "Could not fetch Ollama models. Is Ollama running?",
                "models": [os.getenv("OLLAMA_MODEL", "llama3.1:8b")],
                "default": os.getenv("OLLAMA_MODEL", "llama3.1:8b"),
            }
        )


@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}
    if not data.get("videoSubject"):
        return jsonify({"status": "error", "message": "videoSubject is required."}), 400

    with SessionLocal() as session:
        job = create_job(session, payload=data)

    return jsonify(
        {
            "status": "success",
            "message": "Video generation queued.",
            "jobId": job.id,
        }
    )


@app.route("/api/jobs/<job_id>", methods=["GET"])
def get_job_status(job_id: str):
    with SessionLocal() as session:
        job = get_job(session, job_id)
        if not job:
            return jsonify({"status": "error", "message": "Job not found."}), 404

        return jsonify(
            {
                "status": "success",
                "job": {
                    "id": job.id,
                    "state": job.status,
                    "cancelRequested": job.cancel_requested,
                    "resultPath": job.result_path,
                    "errorMessage": job.error_message,
                    "createdAt": job.created_at.isoformat() if job.created_at else None,
                    "startedAt": job.started_at.isoformat() if job.started_at else None,
                    "completedAt": job.completed_at.isoformat()
                    if job.completed_at
                    else None,
                },
            }
        )


@app.route("/api/jobs/<job_id>/events", methods=["GET"])
def get_events(job_id: str):
    after_id = request.args.get("after", default=0, type=int)

    with SessionLocal() as session:
        job = get_job(session, job_id)
        if not job:
            return jsonify({"status": "error", "message": "Job not found."}), 404

        events = list_job_events(session, job_id, after_id=after_id)
        return jsonify(
            {
                "status": "success",
                "events": [
                    {
                        "id": event.id,
                        "type": event.event_type,
                        "level": event.level,
                        "message": event.message,
                        "payload": event.payload,
                        "timestamp": event.created_at.timestamp()
                        if event.created_at
                        else None,
                    }
                    for event in events
                ],
            }
        )


@app.route("/api/jobs/<job_id>/cancel", methods=["POST"])
def cancel_job(job_id: str):
    with SessionLocal() as session:
        cancelled = request_cancel(session, job_id)
        if not cancelled:
            return jsonify({"status": "error", "message": "Job not found."}), 404

    return jsonify({"status": "success", "message": "Cancellation requested."})


@app.route("/api/upload-songs", methods=["POST"])
def upload_songs():
    try:
        files = request.files.getlist("songs")
        if not files:
            return jsonify({"status": "error", "message": "No files uploaded."}), 400

        clean_dir(str(SONGS_DIR))
        saved = 0
        for file_item in files:
            if file_item.filename and file_item.filename.lower().endswith(".mp3"):
                safe_name = os.path.basename(file_item.filename)
                file_item.save(str(SONGS_DIR / safe_name))
                saved += 1

        if saved == 0:
            return jsonify({"status": "error", "message": "No MP3 files found."}), 400

        log(f"[+] Uploaded {saved} song(s) to {SONGS_DIR}", "success")
        return jsonify({"status": "success", "message": f"Uploaded {saved} song(s)."})
    except Exception as err:
        log(f"[-] Error uploading songs: {str(err)}", "error")
        return jsonify({"status": "error", "message": str(err)}), 500


@app.route("/api/cancel", methods=["POST"])
def cancel_latest_running_job():
    with SessionLocal() as session:
        from models import GenerationJob

        stmt = (
            select(GenerationJob)
            .where(and_(GenerationJob.status.in_(["queued", "running"])))
            .order_by(
                case((GenerationJob.status == "running", 0), else_=1),
                GenerationJob.created_at.desc(),
            )
            .limit(1)
        )
        latest_job = session.scalars(stmt).first()
        if not latest_job:
            return jsonify({"status": "error", "message": "No active job found."}), 404

        request_cancel(session, latest_job.id)

    return jsonify(
        {
            "status": "success",
            "message": "Cancellation requested.",
            "jobId": latest_job.id,
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT, threaded=True)

```

### File: docs\README.md
```md
# MoneyPrinter Docs

This folder is the single source of truth for setup, configuration, and troubleshooting.

## Start Here

- [Interactive Setup Script](../setup.sh)
- [Quickstart](quickstart.md)
- [Configuration](configuration.md)
- [Architecture](architecture.md)
- [Docker](docker.md)
- [Testing](testing.md)
- [Troubleshooting](troubleshooting.md)

## Recommended Reading Order

1. Quickstart
2. Configuration
3. Docker (if you use containers)
4. Testing
5. Troubleshooting (when something breaks)

```

### File: AGENTS.md
```md
# AGENTS Guide for MoneyPrinter

This file is the operating manual for coding agents working in this repository.
Follow it before making changes.

## 1) Repository Layout

- `Backend/`: Flask API, DB-backed job queue, and video generation pipeline.
- `Frontend/`: static HTML/JS client served by `python -m http.server`.
- `docs/`: source-of-truth setup and runtime docs.
- `fonts/`, `Songs/`, `subtitles/`, `temp/`: runtime assets/output folders.
- Root output artifact: `output.mp4`.

## 2) Source of Truth and Existing Rules

- No `.cursor/rules/` directory found.
- No `.cursorrules` file found.
- No `.github/copilot-instructions.md` file found.
- If any of the above appear later, treat them as higher-priority constraints and update this file.

## 3) Environment and Setup Commands

- Python version: `>=3.11` (from `pyproject.toml`).
- Dependency manager used in docs: `uv`.
- Create local env file: `cp .env.example .env`.
- Install dependencies: `uv sync`.
- Run backend: `uv run python Backend/main.py`.
- Run worker (new terminal): `uv run python Backend/worker.py`.
- Run frontend (new terminal): `python3 -m http.server 3000 --directory Frontend`.
- Docker workflow: `docker compose up --build`.

## 4) Build, Lint, and Test Commands

This project has a baseline `pytest` setup for backend repository tests.
Use the commands below as the expected agent workflow.

### 4.1 Build / Runtime Verification

- Backend syntax check: `uv run python -m compileall Backend`.
- Frontend syntax sanity (lightweight): open `Frontend/index.html` in browser and run generation flow.
- API smoke check after backend start: `curl http://localhost:8080/api/models`.
- Queue smoke check: `curl -X POST http://localhost:8080/api/generate -H "Content-Type: application/json" -d '{"videoSubject":"test","voice":"en_us_001","paragraphNumber":1,"customPrompt":""}'`.
- Full local run: backend + worker + frontend servers, then generate a short sample video.

### 4.2 Lint / Formatting (Recommended)

- There is no enforced formatter in-repo today.
- Follow existing style and keep diffs minimal.
- If linting is requested, prefer adding tooling in a separate PR.
- Suggested ad-hoc checks when available locally:
  - `uv run python -m py_compile Backend/*.py`
  - `uv run python -m compileall Backend`

### 4.3 Test Commands (Current and Future)

- Run all tests: `uv run pytest`
- Run one file: `uv run pytest tests/test_file.py`
- Run a single test: `uv run pytest tests/test_file.py::test_name`
- Run a single class test: `uv run pytest tests/test_file.py::TestClass::test_name`
- Current suite location: `tests/`.

## 5) High-Confidence Conventions from Existing Code

These conventions are inferred from current source and should guide new changes.

### 5.1 Python Imports

- Prefer standard library imports first, then third-party, then local modules.
- Use one import per line for readability in long modules.
- Avoid wildcard imports in new code (`from module import *`), even if legacy files use them.
- Prefer explicit local imports, e.g. `from utils import ENV_FILE, TEMP_DIR`.

### 5.2 Formatting and Structure

- Use 4-space indentation in Python.
- Keep line length readable; split long calls across multiple lines.
- Favor small helper functions for distinct pipeline stages.
- Keep side-effectful startup logic near application boot (`load_dotenv`, env checks).

### 5.3 Typing and Signatures

- Add type hints to all new/modified function signatures.
- Reuse `Optional`, `List`, `Tuple`, `dict` typing already used in backend.
- Prefer explicit return types (`-> str`, `-> None`, `-> Tuple[...]`).
- Use `Path` for filesystem paths where practical.

### 5.4 Naming Conventions

- Python functions/variables: `snake_case`.
- Constants/env keys: `UPPER_SNAKE_CASE`.
- JS variables/functions in frontend: `camelCase`.
- Keep API route names simple and verb-oriented (`/api/generate`, `/api/cancel`).

### 5.5 Error Handling and Logging

- Fail fast on missing critical env vars (current code exits early in startup checks).
- Catch exceptions at boundary layers (HTTP handlers, external API calls, file IO).
- Return user-safe JSON error messages from Flask endpoints.
- Log actionable context with existing logger/log-stream helpers.
- Do not swallow exceptions silently; at minimum emit error logs.

### 5.6 Filesystem and Path Safety

- Prefer `pathlib.Path` operations.
- Ensure directories exist before writing (`mkdir(parents=True, exist_ok=True)`).
- Sanitize uploaded filenames (`os.path.basename`) before save.
- Avoid hardcoded OS-specific paths; rely on env vars and `Path.resolve()`.

### 5.7 Backend API Patterns

- Keep endpoint payloads consistent with `{"status": "success|error", ...}`.
- Use appropriate HTTP status codes for conflict/client errors (e.g., `409`, `400`).
- Long-running work should run in worker process from DB queue, not on request thread.
- Preserve cancellation semantics using per-job cancellation and persisted job events.

### 5.8 Frontend Patterns

- Use centralized API helper (`apiRequest`) for backend calls.
- Validate required fields before firing requests.
- Keep user feedback explicit via toasts and status area toggles.
- Preserve localStorage key patterns (`<fieldId>Value`).

## 6) Change Scope Rules for Agents

- Make minimal, targeted edits.
- Do not rename files/modules unless required by task.
- Do not introduce new frameworks/toolchains without request.
- Keep backward compatibility for existing API payload shape when possible.
- Update docs in `docs/` when setup, env vars, or runtime behavior changes.

## 7) Validation Checklist Before Finishing

- Ran relevant command(s) from section 4.
- Confirmed backend still starts (`uv run python Backend/main.py`).
- Confirmed worker still starts (`uv run python Backend/worker.py`).
- Confirmed frontend still loads (`python3 -m http.server 3000 --directory Frontend`).
- Verified changed endpoints still return JSON and preserve `status` field.
- Checked no secrets were added to tracked files.

## 8) Notes for Future Tooling PRs

- Keep tests standardized on `pytest` and document exact paths/selectors here.
- If adding linting, prefer `ruff` for lint + format and commit config files.
- If adding type checks, document command and strictness level (`mypy` or equivalent).
- Keep this file updated whenever workflow commands change.

## 9) Agent Workflow Expectations

- Prefer minimal diffs and preserve current behavior unless the task requires changes.
- Keep API responses machine-parseable and consistent for frontend consumers.
- Avoid checking in generated media/output artifacts unless explicitly requested.
- Before returning work, include what was validated and what was not validated.
- When adding commands or tooling, update this file and `docs/` together.

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MoneyPrinter automates YouTube Shorts creation from text topics. It uses Ollama for script generation, TikTok TTS for voiceover, Pexels for stock footage, and moviepy/ImageMagick for video composition. Output: a 9:16 vertical video (`output.mp4`).

## Commands

### Setup
```bash
cp .env.example .env        # then fill in API keys
uv sync                     # install dependencies
ollama serve                # start Ollama (separate terminal)
ollama pull llama3.1:8b     # pull default model
```

### Run (local)
```bash
uv run python Backend/main.py                              # API on :8080
uv run python Backend/worker.py                            # queue worker
python3 -m http.server 3000 --directory Frontend           # frontend on :3000
```

### Run (Docker)
```bash
docker compose up --build   # frontend :8001, backend :8080, postgres :5432
```

### Verify
```bash
uv run python -m compileall Backend          # syntax check
curl http://localhost:8080/api/models         # API smoke test
```

### Tests
No test suite exists yet. If added, use pytest:
```bash
uv run pytest -q                                           # all tests
uv run pytest tests/test_file.py::test_name -q             # single test
```

## Architecture

### Video Generation Pipeline (end-to-end flow)

```
User input (Frontend) → POST /api/generate → generation_jobs (Postgres queue)
  → worker.py claims queued job
  → gpt.py: generate_script() via Ollama
  → gpt.py: get_search_terms() → JSON keywords
  → search.py: Pexels API → download stock clips to temp/
  → tiktokvoice.py: TTS per sentence → MP3 chunks (threaded)
  → video.py: generate_subtitles() → .srt (AssemblyAI or local timestamps)
  → video.py: combine_videos() → concatenate/crop to 9:16
  → video.py: generate_video() → burn subtitles via ImageMagick, merge audio
  → (optional) mix background music from Songs/ at 10% volume
  → (optional) youtube.py: OAuth2 upload
  → output.mp4
```

### Frontend ↔ Backend Communication
- **REST**: JSON payloads to Flask endpoints (`/api/generate`, `/api/jobs/:id`, `/api/jobs/:id/events`, `/api/jobs/:id/cancel`, `/api/models`, `/api/upload-songs`)
- **Polling**: frontend polls job status and persisted generation events.

### Key Backend Modules
| File | Responsibility |
|------|---------------|
| `main.py` | Flask app and queue/job endpoints |
| `worker.py` | Job consumer that executes generation pipeline |
| `db.py`/`models.py`/`repository.py` | DB engine, schema, queue/event persistence |
| `gpt.py` | Ollama client: script generation, search terms, YouTube metadata |
| `video.py` | Video processing: combine clips, burn subtitles, merge audio |
| `search.py` | Pexels stock video search and download |
| `tiktokvoice.py` | TikTok TTS API (60+ voices, 300-char chunking, threaded) |
| `youtube.py` | YouTube upload via Google API with OAuth2 |
| `utils.py` | Path constants, env validation, ImageMagick detection |
| `pipeline.py` | Reusable generation pipeline used by worker |

### Frontend
- `index.html`: UI with inline CSS, form fields, live log viewer
- `app.js`: API client (`apiRequest()`), job polling UI, localStorage persistence

### Runtime Directories
- `temp/`: intermediate video/audio files (cleared each generation)
- `subtitles/`: generated .srt files (cleared each generation)
- `Songs/`: user-uploaded background music MP3s
- `fonts/`: subtitle font (`bold_font.ttf`)

## Required Environment Variables

- `TIKTOK_SESSION_ID` — TikTok cookie for TTS
- `PEXELS_API_KEY` — stock video API
- `IMAGEMAGICK_BINARY` — leave empty to auto-detect from PATH

Optional: `OLLAMA_BASE_URL`, `OLLAMA_MODEL`, `ASSEMBLY_AI_API_KEY`, `DATABASE_URL`

## Conventions

- **Python**: 4-space indent, `snake_case`, type hints on all new/modified signatures, `pathlib.Path` for filesystem ops
- **JS**: `camelCase`, centralized API calls via `apiRequest()`
- **API responses**: `{"status": "success|error", ...}` with proper HTTP codes
- **Long-running work**: database-backed queue and separate worker process
- **Concurrency**: multiple jobs can be queued; worker processes them safely via DB locking
- Update `docs/` when setup, env vars, or runtime behavior changes

```

### File: setup.sh
```sh
#!/usr/bin/env bash

set -u

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"

if ! cd "$PROJECT_ROOT"; then
  printf 'Failed to enter project directory: %s\n' "$PROJECT_ROOT"
  exit 1
fi

if [ -t 1 ] && command -v tput >/dev/null 2>&1; then
  COLOR_COUNT="$(tput colors 2>/dev/null || printf '0')"
else
  COLOR_COUNT="0"
fi

if [ "$COLOR_COUNT" -ge 8 ]; then
  BOLD="$(tput bold)"
  RESET="$(tput sgr0)"
  RED="$(tput setaf 1)"
  GREEN="$(tput setaf 2)"
  YELLOW="$(tput setaf 3)"
  BLUE="$(tput setaf 4)"
  MAGENTA="$(tput setaf 5)"
  CYAN="$(tput setaf 6)"
else
  BOLD=''
  RESET=''
  RED=''
  GREEN=''
  YELLOW=''
  BLUE=''
  MAGENTA=''
  CYAN=''
fi

print_banner() {
  printf '\n'
  printf '%s%sMoneyPrinter Interactive Setup%s\n' "$BOLD" "$MAGENTA" "$RESET"
  printf '%s--------------------------------%s\n' "$MAGENTA" "$RESET"
  printf '%sThis script helps you prepare your local environment.%s\n\n' "$CYAN" "$RESET"
}

info() {
  printf '%s[INFO]%s %s\n' "$BLUE" "$RESET" "$1"
}

ok() {
  printf '%s[OK]%s   %s\n' "$GREEN" "$RESET" "$1"
}

warn() {
  printf '%s[WARN]%s %s\n' "$YELLOW" "$RESET" "$1"
}

error() {
  printf '%s[ERR]%s  %s\n' "$RED" "$RESET" "$1"
}

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

ask_yes_no() {
  prompt="$1"
  default="$2"

  while true; do
    if [ "$default" = "y" ]; then
      printf '%s [Y/n]: ' "$prompt"
    else
      printf '%s [y/N]: ' "$prompt"
    fi

    read -r reply
    case "$reply" in
      [Yy]|[Yy][Ee][Ss])
        return 0
        ;;
      [Nn]|[Nn][Oo])
        return 1
        ;;
      '')
        if [ "$default" = "y" ]; then
          return 0
        fi
        return 1
        ;;
      *)
        warn 'Please answer y or n.'
        ;;
    esac
  done
}

check_python_version() {
  if ! command_exists python3; then
    error 'python3 not found (required: 3.11+).'
    return 1
  fi

  PYTHON_VERSION="$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null || printf '0.0.0')"
  MAJOR="$(printf '%s' "$PYTHON_VERSION" | cut -d. -f1)"
  MINOR="$(printf '%s' "$PYTHON_VERSION" | cut -d. -f2)"

  if [ "$MAJOR" -gt 3 ] || { [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 11 ]; }; then
    ok "python3 found ($PYTHON_VERSION)"
    return 0
  fi

  error "python3 version is $PYTHON_VERSION (need 3.11+)"
  return 1
}

check_prereqs() {
  info 'Checking prerequisites...'

  missing_critical=0

  if ! check_python_version; then
    missing_critical=1
  fi

  if command_exists uv; then
    ok 'uv found'
  else
    error 'uv not found (install: https://docs.astral.sh/uv/getting-started/installation/)'
    missing_critical=1
  fi

  if command_exists ffmpeg; then
    ok 'ffmpeg found'
  else
    warn 'ffmpeg not found (required for video generation).'
  fi

  if command_exists magick || command_exists convert; then
    ok 'ImageMagick found'
  else
    warn 'ImageMagick not found (some text rendering features may fail).'
  fi

  if command_exists ollama; then
    ok 'ollama found'
  else
    warn 'ollama not found (required for script generation).'
  fi

  if [ "$missing_critical" -eq 1 ]; then
    error 'Missing critical dependencies. Please install them, then rerun setup.'
    return 1
  fi

  return 0
}

configure_local_database_url() {
  if [ ! -f .env ]; then
    return 0
  fi

  db_result="$(python3 - <<'PY'
from pathlib import Path

env_path = Path('.env')
text = env_path.read_text(encoding='utf-8')
has_trailing_newline = text.endswith('\n')
lines = text.splitlines()
target = 'DATABASE_URL="sqlite:///moneyprinter.db"'

for index, line in enumerate(lines):
    if not line.startswith('DATABASE_URL='):
        continue

    value = line.split('=', 1)[1].strip().strip('"').strip("'")
    if value == '' or value.startswith('postgresql+psycopg://'):
        lines[index] = target
        env_path.write_text(
            '\n'.join(lines) + ('\n' if has_trailing_newline else ''),
            encoding='utf-8',
        )
        print('updated')
    else:
        print('kept')
    break
else:
    lines.append(target)
    env_path.write_text(
        '\n'.join(lines) + ('\n' if has_trailing_newline or lines else ''),
        encoding='utf-8',
    )
    print('added')
PY
)"

  case "$db_result" in
    updated)
      info 'Set DATABASE_URL to local SQLite default in .env'
      ;;
    added)
      info 'Added DATABASE_URL local SQLite default to .env'
      ;;
    *)
      info 'Keeping existing DATABASE_URL in .env'
      ;;
  esac
}

setup_env_file() {
  if [ ! -f .env.example ]; then
    warn '.env.example is missing; skipping env setup.'
    return 0
  fi

  if [ -f .env ]; then
    if ask_yes_no '.env already exists. Overwrite it from .env.example?' 'n'; then
      cp .env.example .env
      ok '.env overwritten from .env.example'
    else
      info 'Keeping existing .env'
    fi
  else
    cp .env.example .env
    ok 'Created .env from .env.example'
  fi

  configure_local_database_url

  if ask_yes_no 'Open .env now to edit required keys?' 'y'; then
    if [ -n "${EDITOR:-}" ] && command_exists "$EDITOR"; then
      "$EDITOR" .env
    elif command_exists nano; then
      nano .env
    elif command_exists vi; then
      vi .env
    else
      warn "No terminal editor detected. Please edit $PROJECT_ROOT/.env manually."
    fi
  fi
}

install_dependencies() {
  if ask_yes_no 'Install Python dependencies with uv sync?' 'y'; then
    info 'Running uv sync...'
    if uv sync; then
      ok 'Dependencies installed'
    else
      error 'uv sync failed'
      return 1
    fi
  else
    warn 'Skipped dependency installation.'
  fi

  return 0
}

check_ollama_models() {
  if ! command_exists ollama; then
    return 0
  fi

  if ! ask_yes_no 'Check local Ollama models now?' 'y'; then
    return 0
  fi

  info 'Querying Ollama model list...'
  if ollama list; then
    ok 'Ollama is reachable.'
  else
    warn 'Could not query Ollama. If needed, run: ollama serve'
    return 0
  fi

  if ask_yes_no 'Pull default model llama3.1:8b now?' 'n'; then
    printf 'Model name [llama3.1:8b]: '
    read -r model_name
    model_name="${model_name:-llama3.1:8b}"

    info "Pulling model $model_name ..."
    if ollama pull "$model_name"; then
      ok "Model $model_name is ready"
    else
      warn "Failed to pull model $model_name"
    fi
  fi
}

print_next_steps() {
  printf '\n%sNext steps%s\n' "$BOLD" "$RESET"
  printf '%s1.%s Start backend: %suv run python Backend/main.py%s\n' "$CYAN" "$RESET" "$BOLD" "$RESET"
  printf '%s2.%s Start worker (new terminal): %suv run python Backend/worker.py%s\n' "$CYAN" "$RESET" "$BOLD" "$RESET"
  printf '%s3.%s Start frontend (new terminal): %spython3 -m http.server 3000 --directory Frontend%s\n' "$CYAN" "$RESET" "$BOLD" "$RESET"
  printf '%s4.%s Open: %shttp://localhost:3000%s\n\n' "$CYAN" "$RESET" "$BOLD" "$RESET"
}

main() {
  print_banner

  if ! check_prereqs; then
    exit 1
  fi

  setup_env_file

  if ! install_dependencies; then
    exit 1
  fi

  check_ollama_models
  print_next_steps
  ok 'Setup complete. Happy building!'
}

main "$@"

```

### File: Backend\db.py
```py
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from dotenv import load_dotenv
from utils import ENV_FILE


load_dotenv(ENV_FILE)


class Base(DeclarativeBase):
    pass


def _database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url
    return "sqlite:///moneyprinter.db"


DATABASE_URL = _database_url()

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {},
)

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)


def init_db() -> None:
    from models import Artifact, GenerationEvent, GenerationJob, Project, Script  # noqa: F401

    Base.metadata.create_all(bind=engine)

```

### File: Backend\gpt.py
```py
import re
import os
import json
from ollama import Client, ResponseError

from dotenv import load_dotenv
from logstream import log
from typing import Tuple, List, Optional
from utils import ENV_FILE

# Load environment variables
load_dotenv(ENV_FILE)

# Set environment variables
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OLLAMA_TIMEOUT = float(os.getenv("OLLAMA_TIMEOUT", "180"))


def _ollama_client() -> Client:
    return Client(host=OLLAMA_BASE_URL, timeout=OLLAMA_TIMEOUT)


def _extract_model_name(model_obj) -> str:
    if hasattr(model_obj, "model") and getattr(model_obj, "model"):
        return str(getattr(model_obj, "model")).strip()
    if hasattr(model_obj, "name") and getattr(model_obj, "name"):
        return str(getattr(model_obj, "name")).strip()
    if isinstance(model_obj, dict):
        return str(model_obj.get("model") or model_obj.get("name") or "").strip()
    return ""


def list_ollama_models() -> Tuple[List[str], str]:
    """
    Returns available Ollama model names and configured default model.

    Returns:
        Tuple[List[str], str]: (available model names, default model)
    """
    try:
        response = _ollama_client().list()
    except Exception as err:
        raise RuntimeError(f"Failed to fetch Ollama models: {err}") from err

    models = []
    if hasattr(response, "models") and getattr(response, "models") is not None:
        models = list(getattr(response, "models"))
    elif isinstance(response, dict):
        models = response.get("models") or []

    model_names = [_extract_model_name(model) for model in models]
    model_names = [name for name in model_names if name]

    unique_names = list(dict.fromkeys(model_names))

    if OLLAMA_MODEL and OLLAMA_MODEL in unique_names:
        default_model = OLLAMA_MODEL
    elif unique_names:
        default_model = unique_names[0]
    else:
        default_model = OLLAMA_MODEL if OLLAMA_MODEL else ""

    return unique_names, default_model


def generate_response(prompt: str, ai_model: str) -> str:
    """
    Generate a script for a video, depending on the subject of the video.

    Args:
        video_subject (str): The subject of the video.
        ai_model (str): The AI model to use for generation.


    Returns:

        str: The response from the AI model.

    """

    model_name = (ai_model or "").strip() or OLLAMA_MODEL

    try:
        client = _ollama_client()
        try:
            response = client.chat(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                stream=False,
            )
        except ResponseError as err:
            if err.status_code == 404:
                try:
                    response = client.generate(
                        model=model_name, prompt=prompt, stream=False
                    )
                except ResponseError as fallback_err:
                    if (
                        fallback_err.status_code == 404
                        and "not found" in str(fallback_err).lower()
                    ):
                        available_models, _ = list_ollama_models()
                        available = (
                            ", ".join(available_models) if available_models else "none"
                        )
                        raise RuntimeError(
                            f"Ollama model '{model_name}' is not installed. Available models: {available}. "
                            f"Install it with: ollama pull {model_name}"
                        ) from fallback_err
                    raise
            else:
                raise
    except RuntimeError:
        raise
    except Exception as err:
        raise RuntimeError(f"Failed to connect to Ollama: {err}") from err

    content = ""
    if hasattr(response, "message") and getattr(response, "message") is not None:
        message = getattr(response, "message")
        if hasattr(message, "content") and getattr(message, "content"):
            content = str(getattr(message, "content")).strip()
        elif isinstance(message, dict):
            content = str(message.get("content") or "").strip()

    if not content:
        if hasattr(response, "response") and getattr(response, "response"):
            content = str(getattr(response, "response")).strip()
        elif isinstance(response, dict):
            content = (
                str(response.get("message", {}).get("content") or "")
                or str(response.get("response") or "")
            ).strip()

    if not content:
        raise RuntimeError("Ollama returned an empty response.")

    return content


def generate_script(
    video_subject: str,
    paragraph_number: int,
    ai_model: str,
    voice: str,
    customPrompt: str,
) -> Optional[str]:
    """
    Generate a script for a video, depending on the subject of the video, the number of paragraphs, and the AI model.



    Args:

        video_subject (str): The subject of the video.

        paragraph_number (int): The number of paragraphs to generate.

        ai_model (str): The AI model to use for generation.



    Returns:

        str: The script for the video.

    """

    # Build prompt

    if customPrompt:
        prompt = customPrompt
    else:
        prompt = """
            Generate a script for a video, depending on the subject of the video.

            The script is to be returned as a string with the specified number of paragraphs.

            Here is an example of a string:
            "This is an example string."

            Do not under any circumstance reference this prompt in your response.

            Get straight to the point, don't start with unnecessary things like, "welcome to this video".

            Obviously, the script should be related to the subject of the video.

            YOU MUST NOT INCLUDE ANY TYPE OF MARKDOWN OR FORMATTING IN THE SCRIPT, NEVER USE A TITLE.
            YOU MUST WRITE THE SCRIPT IN THE LANGUAGE SPECIFIED IN [LANGUAGE].
            ONLY RETURN THE RAW CONTENT OF THE SCRIPT. DO NOT INCLUDE "VOICEOVER", "NARRATOR" OR SIMILAR INDICATORS OF WHAT SHOULD BE SPOKEN AT THE BEGINNING OF EACH PARAGRAPH OR LINE. YOU MUST NOT MENTION THE PROMPT, OR ANYTHING ABOUT THE SCRIPT ITSELF. ALSO, NEVER TALK ABOUT THE AMOUNT OF PARAGRAPHS OR LINES. JUST WRITE THE SCRIPT.

        """

    prompt += f"""
    
    Subject: {video_subject}
    Number of paragraphs: {paragraph_number}
    Language: {voice}

    """

    # Generate script
    response = generate_response(prompt, ai_model)

    log(response, "info")

    # Return the generated script
    if response:
        # Clean the script
        # Remove asterisks, hashes
        response = response.replace("*", "")
        response = response.replace("#", "")

        # Remove markdown syntax
        response = re.sub(r"\[.*\]", "", response)
        response = re.sub(r"\(.*\)", "", response)

        # Split the script into paragraphs
        paragraphs = response.split("\n\n")

        # Select the specified number of paragraphs
        selected_paragraphs = paragraphs[:paragraph_number]

        # Join the selected paragraphs into a single string
        final_script = "\n\n".join(selected_paragraphs)

        # Print to console the number of paragraphs used
        log(f"Number of paragraphs used: {len(selected_paragraphs)}", "success")

        return final_script
    else:
        log("[-] GPT returned an empty response.", "error")
        return None


def get_search_terms(
    video_subject: str, amount: int, script: str, ai_model: str
) -> List[str]:
    """
    Generate a JSON-Array of search terms for stock videos,
    depending on the subject of a video.

    Args:
        video_subject (str): The subject of the video.
        amount (int): The amount of search terms to generate.
        script (str): The script of the video.
        ai_model (str): The AI model to use for generation.

    Returns:
        List[str]: The search terms for the video subject.
    """

    # Build prompt
    prompt = f"""
    Generate {amount} search terms for stock videos,
    depending on the subject of a video.
    Subject: {video_subject}

    The search terms are to be returned as
    a JSON-Array of strings.

    Each search term should consist of 1-3 words,
    always add the main subject of the video.
    
    YOU MUST ONLY RETURN THE JSON-ARRAY OF STRINGS.
    YOU MUST NOT RETURN ANYTHING ELSE. 
    YOU MUST NOT RETURN THE SCRIPT.
    
    The search terms must be related to the subject of the video.
    Here is an example of a JSON-Array of strings:
    ["search term 1", "search term 2", "search term 3"]

    For context, here is the full text:
    {script}
    """

    # Generate search terms
    response = generate_response(prompt, ai_model)
    log(response, "info")

    # Parse response into a list of search terms
    search_terms = []

    try:
        search_terms = json.loads(response)
        if not isinstance(search_terms, list) or not all(
            isinstance(term, str) for term in search_terms
        ):
            raise ValueError("Response is not a list of strings.")

    except (json.JSONDecodeError, ValueError):
        log("[*] GPT returned an unformatted response. Attempting to clean...", "warning")

        # Attempt to extract JSON array first
        match = re.search(r"\[[\s\S]*\]", response)
        if match:
            try:
                search_terms = json.loads(match.group())
            except json.JSONDecodeError:
                search_terms = []

        # Last-resort fallback: collect quoted strings
        if not search_terms:
            search_terms = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', response)
            search_terms = [term.strip() for term in search_terms if term.strip()]

    # Let user know
    log(f"\nGenerated {len(search_terms)} search terms: {', '.join(search_terms)}", "info")

    # Return search terms
    return search_terms


def generate_metadata(
    video_subject: str, script: str, ai_model: str
) -> Tuple[str, str, List[str]]:
    """
    Generate metadata for a YouTube video, including the title, description, and keywords.

    Args:
        video_subject (str): The subject of the video.
        script (str): The script of the video.
        ai_model (str): The AI model to use for generation.

    Returns:
        Tuple[str, str, List[str]]: The title, description, and keywords for the video.
    """

    # Build prompt for title
    title_prompt = f"""  
    Generate a catchy and SEO-friendly title for a YouTube shorts video about {video_subject}.  
    """

    # Generate title
    title = generate_response(title_prompt, ai_model).strip()

    # Build prompt for description
    description_prompt = f"""  
    Write a brief and engaging description for a YouTube shorts video about {video_subject}.  
    The video is based on the following script:  
    {script}  
    """

    # Generate description
    description = generate_response(description_prompt, ai_model).strip()

    # Generate keywords
    keywords = get_search_terms(video_subject, 6, script, ai_model)

    return title, description, keywords

```

### File: Backend\logstream.py
```py
import json
import queue
import re
import time


class LogStream:
    """Thread-safe log queue that doubles as an SSE generator."""

    def __init__(self, maxsize: int = 500):
        self._queue: queue.Queue = queue.Queue(maxsize=maxsize)

    def clear(self) -> None:
        """Drain all pending items from the queue."""
        while True:
            try:
                self._queue.get_nowait()
            except queue.Empty:
                break

    def push(self, message: str, level: str = "info") -> None:
        """Add a log entry. Drops the oldest entry if the queue is full."""
        entry = {
            "type": "log",
            "message": message,
            "level": level,
            "timestamp": time.time(),
        }
        try:
            self._queue.put_nowait(entry)
        except queue.Full:
            try:
                self._queue.get_nowait()
            except queue.Empty:
                pass
            try:
                self._queue.put_nowait(entry)
            except queue.Full:
                pass

    def push_event(self, event_type: str, data: dict | None = None) -> None:
        """Send a control event (complete, error, cancelled)."""
        entry = {
            "type": event_type,
            "timestamp": time.time(),
            **(data or {}),
        }
        try:
            self._queue.put_nowait(entry)
        except queue.Full:
            try:
                self._queue.get_nowait()
            except queue.Empty:
                pass
            try:
                self._queue.put_nowait(entry)
            except queue.Full:
                pass

    def stream(self, timeout: float = 30.0):
        """Generator yielding SSE-formatted lines. Terminates on control events."""
        while True:
            try:
                entry = self._queue.get(timeout=timeout)
                yield f"data: {json.dumps(entry)}\n\n"
                if entry.get("type") in ("complete", "error", "cancelled"):
                    return
            except queue.Empty:
                # Send keepalive comment to prevent connection timeout
                yield ": keepalive\n\n"


# Strip ANSI escape codes from terminal-colored strings
_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

# Singleton shared by all modules
log_stream = LogStream()

# Color-to-level mapping for termcolor colors
_COLOR_LEVEL = {
    "green": "success",
    "red": "error",
    "yellow": "warning",
    "blue": "info",
    "cyan": "info",
    "magenta": "info",
}


def log(message: str, level: str = "info") -> None:
    """Drop-in replacement for ``print(colored(msg, color))``.

    Prints to the terminal **and** pushes an ANSI-stripped copy to the SSE queue.
    """
    print(message)
    clean = _ANSI_RE.sub("", str(message))
    log_stream.push(clean, level)

```

### File: Backend\models.py
```py
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


class GenerationJob(Base):
    __tablename__ = "generation_jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    project_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("projects.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    cancel_requested: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    attempt_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    max_attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    result_path: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False, index=True
    )
    started_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    project: Mapped[Optional[Project]] = relationship("Project")
    events: Mapped[list["GenerationEvent"]] = relationship(
        "GenerationEvent", back_populates="job", cascade="all, delete-orphan"
    )


class GenerationEvent(Base):
    __tablename__ = "generation_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("generation_jobs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    event_type: Mapped[str] = mapped_column(String(20), nullable=False, default="log")
    level: Mapped[str] = mapped_column(String(20), nullable=False, default="info")
    message: Mapped[str] = mapped_column(Text, nullable=False)
    payload: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False, index=True
    )

    job: Mapped[GenerationJob] = relationship("GenerationJob", back_populates="events")


class Script(Base):
    __tablename__ = "scripts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("generation_jobs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    model_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


class Artifact(Base):
    __tablename__ = "artifacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("generation_jobs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    artifact_type: Mapped[str] = mapped_column(String(64), nullable=False)
    path: Mapped[str] = mapped_column(String(512), nullable=False)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

```

### File: Backend\pipeline.py
```py
import os
import shutil
import subprocess

from apiclient.errors import HttpError
from moviepy import (
    AudioFileClip,
    CompositeAudioClip,
    VideoFileClip,
    afx,
    concatenate_audioclips,
)
from uuid import uuid4

from gpt import generate_metadata, generate_script, get_search_terms
from logstream import log
from search import search_for_stock_videos
from tiktokvoice import tts
from utils import (
    BASE_DIR,
    PROJECT_ROOT,
    SONGS_DIR,
    SUBTITLES_DIR,
    TEMP_DIR,
    choose_random_song,
)
from video import combine_videos, generate_subtitles, generate_video, save_video
from youtube import upload_video


class PipelineCancelled(Exception):
    pass


def run_generation_pipeline(
    data: dict,
    is_cancelled,
    on_log,
    amount_of_stock_videos: int = 5,
) -> str:
    def emit(message: str, level: str = "info") -> None:
        log(message, level)
        if on_log:
            on_log(message, level)

    def guard_cancelled() -> None:
        if is_cancelled and is_cancelled():
            raise PipelineCancelled("Video generation was cancelled.")

    paragraph_number = int(data.get("paragraphNumber", 1))
    ai_model = data.get("aiModel")
    n_threads = data.get("threads")
    subtitles_position = data.get("subtitlesPosition")
    text_color = data.get("color")
    use_music = data.get("useMusic", False)
    automate_youtube_upload = data.get("automateYoutubeUpload", False)

    emit("[Video to be generated]", "info")
    emit("   Subject: " + data["videoSubject"], "info")
    emit("   AI Model: " + str(ai_model), "info")
    emit("   Custom Prompt: " + data["customPrompt"], "info")

    guard_cancelled()

    voice = data.get("voice", "")
    voice_prefix = voice[:2]

    if not voice:
        emit('[!] No voice was selected. Defaulting to "en_us_001"', "warning")
        voice = "en_us_001"
        voice_prefix = voice[:2]

    script = generate_script(
        data["videoSubject"],
        paragraph_number,
        ai_model,
        voice,
        data["customPrompt"],
    )

    if not script:
        raise RuntimeError(
            "Could not generate a script. Try a different model or prompt."
        )

    search_terms = get_search_terms(
        data["videoSubject"], amount_of_stock_videos, script, ai_model
    )

    video_urls = []
    it = 15
    min_dur = 10

    for search_term in search_terms:
        guard_cancelled()
        found_urls = search_for_stock_videos(
            search_term, os.getenv("PEXELS_API_KEY"), it, min_dur
        )
        for url in found_urls:
            if url not in video_urls:
                video_urls.append(url)
                break

    if not video_urls:
        raise RuntimeError("No videos found to download.")

    video_paths = []
    emit(f"[+] Downloading {len(video_urls)} videos...", "info")

    for video_url in video_urls:
        guard_cancelled()
        try:
            saved_video_path = save_video(video_url)
            video_paths.append(saved_video_path)
        except Exception:
            emit(f"[-] Could not download video: {video_url}", "error")

    emit("[+] Videos downloaded!", "success")
    emit("[+] Script generated!", "success")

    guard_cancelled()

    sentences = script.split(". ")
    sentences = list(filter(lambda x: x != "", sentences))
    paths = []

    for sentence in sentences:
        guard_cancelled()
        current_tts_path = str(TEMP_DIR / f"{uuid4()}.mp3")
        tts(sentence, voice, filename=current_tts_path)
        audio_clip = AudioFileClip(current_tts_path)
        paths.append(audio_clip)

    final_audio = concatenate_audioclips(paths)
    tts_path = str(TEMP_DIR / f"{uuid4()}.mp3")
    try:
        final_audio.write_audiofile(tts_path)
    finally:
        final_audio.close()
        for audio_clip in paths:
            audio_clip.close()

    try:
        subtitles_path = generate_subtitles(
            audio_path=tts_path,
            sentences=sentences,
            audio_clips=paths,
            voice=voice_prefix,
        )
    except Exception as err:
        emit(f"[-] Error generating subtitles: {err}", "error")
        subtitles_path = None

    if not subtitles_path:
        raise RuntimeError(
            "Could not generate subtitles. Check AssemblyAI key or local subtitle settings."
        )

    temp_audio = AudioFileClip(tts_path)
    try:
        combined_video_path = combine_videos(
            video_paths, temp_audio.duration, 5, n_threads or 2
        )
    finally:
        temp_audio.close()

    try:
        final_video_path = generate_video(
            combined_video_path,
            tts_path,
            subtitles_path,
            n_threads or 2,
            subtitles_position,
            text_color or "#FFFF00",
        )
    except Exception as err:
        raise RuntimeError(
            f"Could not render final video. Check subtitle/font/ImageMagick setup. ({err})"
        ) from err

    title, description, keywords = generate_metadata(
        data["videoSubject"], script, ai_model
    )

    emit("[-] Metadata for YouTube upload:", "info")
    emit("   Title:", "info")
    emit(f"   {title}", "info")
    emit("   Description:", "info")
    emit(f"   {description}", "info")
    emit("   Keywords:", "info")
    emit(f"  {', '.join(keywords)}", "info")

    if automate_youtube_upload:
        client_secrets_file = str((BASE_DIR / "client_secret.json").resolve())
        skip_yt_upload = False
        if not os.path.exists(client_secrets_file):
            skip_yt_upload = True
            emit(
                "[-] Client secrets file missing. YouTube upload will be skipped.",
                "warning",
            )
            emit(
                "[-] Please download the client_secret.json from Google Cloud Platform and store this inside the /Backend directory.",
                "error",
            )

        if not skip_yt_upload:
            video_category_id = "28"
            privacy_status = "private"
            video_metadata = {
                "video_path": str((TEMP_DIR / final_video_path).resolve()),
                "title": title,
                "description": description,
                "category": video_category_id,
                "keywords": ",".join(keywords),
                "privacyStatus": privacy_status,
            }

            try:
                video_response = upload_video(
                    video_path=video_metadata["video_path"],
                    title=video_metadata["title"],
                    description=video_metadata["description"],
                    category=video_metadata["category"],
                    keywords=video_metadata["keywords"],
                    privacy_status=video_metadata["privacyStatus"],
                )
                emit(f"Uploaded video ID: {video_response.get('id')}", "success")
            except HttpError as err:
                emit(
                    f"An HTTP error {err.resp.status} occurred:\n{err.content}", "error"
                )

    final_output_path = str(PROJECT_ROOT / final_video_path)
    rendered_video_path = str(TEMP_DIR / final_video_path)
    render_threads = n_threads or (os.cpu_count() or 2)

    guard_cancelled()

    if use_music:
        song_path = choose_random_song()

        if not song_path:
            emit(
                "[-] Could not find songs in Songs/. Continuing without background music.",
                "warning",
            )
            use_music = False

        if use_music:
            video_clip = VideoFileClip(rendered_video_path)
            song_clip = None
            mixed_audio = None
            mixed_audio_path = str(TEMP_DIR / f"{uuid4()}_mixed_audio.m4a")
            try:
                original_duration = video_clip.duration
                original_audio = video_clip.audio
                song_clip = AudioFileClip(song_path).with_fps(44100)
                song_clip = song_clip.with_effects(
                    [afx.AudioLoop(duration=original_duration)]
                )
                song_clip = song_clip.with_volume_scaled(0.1).with_fps(44100)

                mixed_audio = CompositeAudioClip(
                    [original_audio, song_clip]
                ).with_duration(original_duration)
                mixed_audio.write_audiofile(
                    mixed_audio_path,
                    fps=44100,
                    codec="aac",
                    bitrate="192k",
                )
            finally:
                video_clip.close()
                if mixed_audio is not None:
                    mixed_audio.close()
                if song_clip is not None:
                    song_clip.close()

            try:
                subprocess.run(
                    [
                        "ffmpeg",
                        "-y",
                        "-i",
                        rendered_video_path,
                        "-i",
                        mixed_audio_path,
                        "-map",
                        "0:v:0",
                        "-map",
                        "1:a:0",
                        "-c:v",
                        "copy",
                        "-c:a",
                        "aac",
                        "-b:a",
                        "192k",
                        "-shortest",
                        final_output_path,
                    ],
                    check=True,
                    capture_output=True,
                    text=True,
                )
            except Exception:
                emit(
                    "[!] ffmpeg remux failed. Falling back to MoviePy render for music mix.",
                    "warning",
                )
                video_clip = VideoFileClip(rendered_video_path)
                song_clip = None
                try:
                    original_duration = video_clip.duration
                    original_audio = video_clip.audio
                    song_clip = AudioFileClip(song_path).with_fps(44100)
                    song_clip = song_clip.with_effects(
                        [afx.AudioLoop(duration=original_duration)]
                    )
                    song_clip = song_clip.with_volume_scaled(0.1).with_fps(44100)
                    comp_audio = CompositeAudioClip(
                        [original_audio, song_clip]
                    ).with_duration(original_duration)
                    video_clip = (
                        video_clip.with_audio(comp_audio)
                        .with_fps(30)
                        .with_duration(original_duration)
                    )
                    video_clip.write_videofile(
                        final_output_path,
                        threads=render_threads,
                        fps=30,
                        codec="libx264",
                        audio_codec="aac",
                        preset="medium",
                    )
                finally:
                    video_clip.close()
                    if song_clip is not None:
                        song_clip.close()
            finally:
                if os.path.exists(mixed_audio_path):
                    os.remove(mixed_audio_path)

    if not use_music:
        shutil.copy2(rendered_video_path, final_output_path)

    emit(f"[+] Video generated: {final_video_path}!", "success")

    if os.name == "nt":
        subprocess.run(
            ["taskkill", "/f", "/im", "ffmpeg.exe"],
            check=False,
            capture_output=True,
            text=True,
        )
    elif shutil.which("pkill"):
        subprocess.run(
            ["pkill", "-f", "ffmpeg"],
            check=False,
            capture_output=True,
            text=True,
        )

    return final_video_path

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
