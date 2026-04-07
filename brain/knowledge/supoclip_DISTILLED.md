---
id: supoclip
type: knowledge
owner: OA_Triage
---
# supoclip
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Fuck OpusClip.

... because good video clips shouldn't cost a fortune or come with ugly watermarks.

<p align="center">
  <a href="https://www.supoclip.com">
    <img src="assets/banner.png" alt="SupoClip Banner" width="100%" />
  </a>
</p>

OpusClip charges $15-29/month and slaps watermarks on every free video. SupoClip gives you the same AI-powered video clipping capabilities - completely free, completely open source, and completely watermark-free, while still providing you with a hosted version, that doesn't cost the same amount as your mortgage.

> For the hosted version, sign up for the waitlist here: [SupoClip Hosted](https://www.supoclip.com)

## Why SupoClip Exists

### The OpusClip Problem

OpusClip is undeniably powerful. It's an AI video clipping tool that can turn long-form content into viral short clips with features like:

- AI-powered clip generation from long videos
- Automated captions with 97%+ accuracy
- Virality scoring to predict viral potential
- Multi-language support (20+ languages)
- Brand templates and customization

**But here's the catch:**

- **Free plan limitations**: Only 60 minutes of processing per month
- **Watermarks everywhere**: Every free video gets branded with OpusClip's watermark
- **Expensive pricing**: $15/month for Starter, $29/month for Pro
- **Processing limits**: Even paid plans have strict minute limits
- **Vendor lock-in**: Your content and workflows are tied to their platform

### The SupoClip Solution

SupoClip provides the same core functionality without the financial burden:

→ ✅ **Completely Free** - No monthly fees, no processing limits

→ ✅ **No Watermarks** - Your content stays yours

→ ✅ **Open Source** - Full transparency, community-driven development

→ ✅ **Self-Hosted** - Complete control over your data and processing

→ ✅ **Unlimited Usage** - Process as many videos as your hardware can handle

→ ✅ **Customizable** - Modify and extend the codebase to fit your needs

## Quick Start

### Prerequisites

- Docker and Docker Compose
- An AssemblyAI API key (for transcription) - [Get one here](https://www.assemblyai.com/)
- An LLM provider for AI analysis - OpenAI, Google, Anthropic, or Ollama

### 1. Clone and Configure

```bash
git clone https://github.com/your-username/supoclip.git
cd supoclip
```

Create a `.env` file in the root directory:

```env
# Required: Video transcription
ASSEMBLY_AI_API_KEY=your_assemblyai_api_key

# Required: Choose ONE LLM provider and set its API key
# Option A: Google Gemini (recommended - fast & cost-effective)
LLM=google-gla:gemini-3-flash-preview
GOOGLE_API_KEY=your_google_api_key

# Option B: OpenAI GPT-5.2 (best reasoning)
# LLM=openai:gpt-5.2
# OPENAI_API_KEY=your_openai_api_key

# Option C: Anthropic Claude
# LLM=anthropic:claude-4-sonnet
# ANTHROPIC_API_KEY=your_anthropic_api_key

# Option D: Ollama (local/self-hosted)
# LLM=ollama:gpt-oss:20b
# OLLAMA_BASE_URL=http://localhost:11434/v1
# OLLAMA_API_KEY=your_ollama_api_key  # Optional (Ollama Cloud)

# Optional: Auth secret (change in production)
BETTER_AUTH_SECRET=change_this_in_production

# Optional: DataFast analytics
# Track your deployed domain in DataFast
# NEXT_PUBLIC_DATAFAST_WEBSITE_ID=dfid_xxxxx
# NEXT_PUBLIC_DATAFAST_DOMAIN=your-domain.com
# NEXT_PUBLIC_DATAFAST_ALLOW_LOCALHOST=false

# Optional: Resend for waitlist confirmation emails
# RESEND_API_KEY=your_resend_api_key

# Optional: YouTube metadata provider
# `yt_dlp` preserves the existing metadata behavior
# `youtube_data_api` uses the official API first, then falls back to yt-dlp
# YOUTUBE_METADATA_PROVIDER=yt_dlp
# YOUTUBE_DATA_API_KEY=your_youtube_data_api_key
```

### 2. Start the Services

```bash
docker-compose up -d
```

This starts:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000 (docs at /docs)
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

### 3. Wait for Initialization

First-time startup takes a few minutes. Check progress with:

```bash
docker-compose logs -f
```

Wait until you see health checks passing for all services.

### 4. Access the App

Open http://localhost:3000 in your browser, create an account, and start clipping!

If you enable DataFast, also verify that:
- `/js/script.js` loads from your own app domain
- `/api/events` requests are proxied through your app domain
- custom goals appear after successful sign-up, sign-in, task creation, billing, feedback, or waitlist actions

### Troubleshooting

**Backend fails to start with API key error:**
- Make sure you've set the correct LLM provider AND its corresponding API key in `.env`
- Default is `google-gla:gemini-3-flash-preview` which requires `GOOGLE_API_KEY`
- If using `openai:gpt-5.2`, you MUST set `OPENAI_API_KEY`
- If using `ollama:*`, run Ollama and (optionally) set `OLLAMA_BASE_URL`
- Rebuild after changing `.env`: `docker-compose up -d --build`

**Videos stay queued / never process:**
- Check worker logs: `docker-compose logs -f worker`
- Ensure Redis is healthy: `docker-compose logs redis`
- Verify API keys are correct

**YouTube titles or duration lookup is failing:**
- `YOUTUBE_METADATA_PROVIDER=yt_dlp` keeps the old metadata path
- `YOUTUBE_METADATA_PROVIDER=youtube_data_api` requires YouTube Data API v3 enabled in Google Cloud
- Prefer `YOUTUBE_DATA_API_KEY`; if it is unset, the backend will try `GOOGLE_API_KEY`
- The backend will automatically fall back to the other metadata provider if the primary one fails
- `videos.list` costs 1 quota unit per request

**Performance tuning (default is fast mode):**
- `DEFAULT_PROCESSING_MODE=fast|balanced|quality`
- `FAST_MODE_MAX_CLIPS=4` to cap clip count in fast mode
- `FAST_MODE_TRANSCRIPT_MODEL=nano` for fastest transcript model
- View aggregate metrics: `GET /tasks/metrics/performance`

**Prisma errors on Windows:**
- Run `docker-compose down -v` to clear volumes
- Run `docker-compose up -d --build` to rebuild

**Frontend shows database errors:**
- Wait for PostgreSQL to fully initialize (check logs)
- The database is automatically created on first run

**Font picker is empty / cannot select or upload fonts:**
- Add fonts to `backend/fonts/` – see [backend/fonts/README.md](backend/fonts/README.md) for TikTok Sans and custom fonts
- Ensure `BACKEND_AUTH_SECRET` is set in `.env` when using the hosted/monetized setup
- Font upload is Pro-only when monetization is enabled; self-hosted users can upload freely

**Subscription emails are not sending:**
- Set `RESEND_API_KEY` and `RESEND_FROM_EMAIL` in `.env`
- `RESEND_FROM_EMAIL` must be a verified sender/domain in your Resend account
- The backend sends the “thank you for subscribing” email on `checkout.session.completed`
- The backend sends the “sorry to see you go” email on `customer.subscription.deleted`

## Testing

SupoClip now has a layered automated test setup:

- `pytest` for backend unit and integration tests
- `Vitest` and Testing Library for frontend route and component coverage
- `Playwright` for a small seeded browser smoke suite

Repo-level entrypoints:

```bash
make test
make test-backend
make test-frontend
make test-e2e
make test-ci
```

App-level entrypoints:

```bash
cd backend && uv sync --all-groups && .venv/bin/pytest
cd frontend && npm install && npm run test:coverage
cd frontend && npm run test:e2e
```

Local test runs expect PostgreSQL and Redis to be available. The easiest path is to start the stack with `docker-compose up -d`, then run the commands above. CI runs the same layers in GitHub Actions with Postgres and Redis service containers.

## Documentation

Detailed documentation now lives in [`docs/`](docs/README.md).

Start with:

- [`docs/setup.md`](docs/setup.md)
- [`docs/configuration.md`](docs/configuration.md)
- [`docs/app-guide.md`](docs/app-guide.md)
- [`docs/architecture.md`](docs/architecture.md)
- [`docs/api-reference.md`](docs/api-reference.md)
- [`docs/development.md`](docs/development.md)
- [`docs/troubleshooting.md`](docs/troubleshooting.md)

## Hosted Billing Emails

When you run SupoClip with monetization enabled (`SELF_HOST=false`), subscription lifecycle emails are sent through Resend by the backend:

- `checkout.session.completed` sends the thank-you-for-subscribing email
- `customer.subscription.deleted` sends the sorry-to-see-you-go email

Required env vars for this flow:

- `RESEND_API_KEY`
- `RESEND_FROM_EMAIL`
- `BACKEND_AUTH_SECRET`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `STRIPE_PRICE_ID`

### Local Development (Without Docker)

See [CLAUDE.md](CLAUDE.md) for detailed development instructions.

## License

SupoClip is released under the AGPL-3.0 License. See [LICENSE](LICENSE) for details.

```

### File: backend\README.md
```md
# Backend Docs

## Requirements

Ensure you have `ffmpeg` installed.

```
# MacOS
brew install ffmpeg

# Linux (Ubuntu)
sudo apt update -y && sudo apt install install ffmpeg -y

# Windows (Chocolatey https://chocolatey.org/)
choco install ffmpeg
```

You must also have `uv` package manager installed.

1. Create a virtual environment

```
uv venv .venv
source .venv/bin/activate
```

## Running Tests

The backend test suite uses `pytest` and is organized into:

- `tests/unit` for fast unit coverage around helpers and services
- `tests/integration` for FastAPI, database, and queue-backed API checks
- legacy `unittest`-style tests, which still run under `pytest`

Install dependencies:

```bash
uv sync --all-groups
```

Run the backend suite:

```bash
DATABASE_URL=postgresql+asyncpg://localhost:5432/supoclip \
TEST_DATABASE_URL=postgresql+asyncpg://localhost:5432/supoclip \
REDIS_HOST=127.0.0.1 \
REDIS_PORT=6379 \
.venv/bin/pytest
```

Notes:

- `TEST_DATABASE_URL` should point at a disposable local test database.
- Redis is only required for the integration paths that validate queue and health behavior.
- Coverage thresholds are enforced in `pyproject.toml` during the test run.
- For repo-level entrypoints, use `make test-backend` or `make test-ci` from the repository root.

## Email Configuration

The backend now sends subscription lifecycle emails through Resend.

Set these env vars when using hosted billing:

```
RESEND_API_KEY=your_resend_api_key
RESEND_FROM_EMAIL="SupoClip <onboarding@your-domain.com>"
```

Notes:

- `RESEND_FROM_EMAIL` must be a verified sender/domain in Resend.
- The thank-you email is triggered after a successful Stripe checkout.
- The cancellation email is triggered after Stripe subscription deletion.

## YouTube Metadata Provider

YouTube downloads still use the existing Apify-first flow with `yt-dlp` fallback. Metadata lookup is now configurable separately.

Set these env vars to use the official YouTube Data API v3 for title, duration, channel, thumbnail, and view-count preflight:

```env
YOUTUBE_METADATA_PROVIDER=youtube_data_api
YOUTUBE_DATA_API_KEY=your_youtube_data_api_key
```

Notes:

- `YOUTUBE_METADATA_PROVIDER=yt_dlp` preserves the previous metadata behavior.
- If `YOUTUBE_DATA_API_KEY` is not set, the backend will try `GOOGLE_API_KEY` for YouTube metadata requests.
- The selected metadata provider is the primary path only; the backend automatically falls back to the other provider if the first one fails.
- `videos.list` costs 1 quota unit per request in the YouTube Data API.
- The public API does not expose some `yt-dlp`-specific metadata fields like `format_id`, `resolution`, `fps`, or file size.
- Enable the YouTube Data API v3 for your Google Cloud project before using this mode.

```

### File: docs\README.md
```md
# SupoClip Documentation

This directory is the canonical documentation hub for SupoClip.

If you are new to the project, start here:

1. Read [Setup](./setup.md) to get the app running.
2. Review [Configuration](./configuration.md) to understand environment variables and operating modes.
3. Use [App Guide](./app-guide.md) to learn the user-facing parts of the product.
4. Use [Architecture](./architecture.md) to understand how the system works end to end.
5. Use [Troubleshooting](./troubleshooting.md) when something goes wrong.

## Documentation Map

- [Setup](./setup.md)
  - Docker-first installation
  - Local development commands
  - First-run checklist
  - Production-minded setup notes
- [Configuration](./configuration.md)
  - Required API keys
  - DataFast analytics settings
  - Processing modes
  - Auth and monetization settings
  - YouTube auth rotation settings
  - Feedback and email configuration
- [App Guide](./app-guide.md)
  - Main screens and routes
  - Core user workflows
  - Admin features
  - Hosted versus self-host differences
- [Architecture](./architecture.md)
  - Frontend, backend, worker, Redis, PostgreSQL
  - Queue and SSE progress flow
  - Video processing pipeline
  - Database model overview
- [API Reference](./api-reference.md)
  - Frontend proxy routes
  - Backend endpoints
  - Admin and billing endpoints
  - Notes on auth and streaming
- [Development](./development.md)
  - Repository layout
  - Commands for each app
  - Common workflows
  - Where to modify major features
- [Troubleshooting](./troubleshooting.md)
  - Startup failures
  - Stuck tasks
  - Auth, fonts, billing, and YouTube issues
  - Performance and recovery guidance

## What SupoClip Is

SupoClip is an open-source AI video clipping application. It takes long-form videos, transcribes them, uses an LLM to select the most promising short segments, and renders vertical or source-aspect clips with subtitles and optional effects.

The current repository snapshot includes:

- `frontend/`: the main Next.js application
- `backend/`: the FastAPI API and ARQ worker code
- Root-level infrastructure files such as `docker-compose.yml`, `init.sql`, `.env.example`, and `start.sh`

Repository guidance still mentions a separate `waitlist/` app, but that directory is not present in this checkout. The documentation in this folder reflects the repository as it exists now.

## Recommended Reading Paths

For operators:

1. [Setup](./setup.md)
2. [Configuration](./configuration.md)
3. [Troubleshooting](./troubleshooting.md)

For developers:

1. [Development](./development.md)
2. [Architecture](./architecture.md)
3. [API Reference](./api-reference.md)

For product and support:

1. [App Guide](./app-guide.md)
2. [Troubleshooting](./troubleshooting.md)

## Existing Documentation Outside `docs/`

This new docs tree replaces the need to hunt across several markdown files, but these older documents still contain useful context:

- [`README.md`](../README.md)
- [`QUICKSTART.md`](../QUICKSTART.md)
- [`CLAUDE.md`](../CLAUDE.md)
- [`REFACTORING_COMPLETE.md`](../REFACTORING_COMPLETE.md)
- [`backend/REFACTORING_GUIDE.md`](../backend/REFACTORING_GUIDE.md)

```

### File: frontend\package.json
```json
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "prisma generate && next build",
    "start": "next start",
    "lint": "next lint",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "test:e2e": "prisma migrate deploy && playwright test",
    "test:e2e:headed": "prisma migrate deploy && playwright test --headed",
    "postinstall": "prisma generate"
  },
  "dependencies": {
    "@prisma/client": "^6.19.2",
    "@radix-ui/react-alert-dialog": "^1.1.15",
    "@radix-ui/react-avatar": "^1.1.11",
    "@radix-ui/react-label": "^2.1.8",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-progress": "^1.1.8",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-separator": "^1.1.8",
    "@radix-ui/react-slider": "^1.3.6",
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-switch": "^1.2.6",
    "better-auth": "^1.5.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.532.0",
    "mediabunny": "^1.35.1",
    "next": "15.4.8",
    "next-themes": "^0.4.6",
    "prisma": "^6.19.2",
    "radix-ui": "^1.4.3",
    "react": "19.1.0",
    "react-dom": "19.1.0",
    "resend": "^6.9.3",
    "sonner": "^2.0.7",
    "stripe": "^20.4.0",
    "tailwind-merge": "^3.5.0",
    "tw-shimmer": "^0.4.9"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3.3.4",
    "@playwright/test": "^1.55.0",
    "@tailwindcss/postcss": "^4.2.1",
    "@testing-library/jest-dom": "^6.8.0",
    "@testing-library/react": "^16.3.0",
    "@testing-library/user-event": "^14.6.1",
    "@types/node": "^20.19.35",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.0.4",
    "@vitest/coverage-v8": "^3.2.4",
    "eslint": "^9.39.3",
    "eslint-config-next": "15.4.4",
    "jsdom": "^27.0.0",
    "msw": "^2.11.2",
    "tailwindcss": "^4.2.1",
    "tw-animate-css": "^1.4.0",
    "typescript": "^5.9.3",
    "vite-tsconfig-paths": "^5.1.4",
    "vitest": "^3.2.4",
    "wait-on": "^8.0.3"
  }
}

```

### File: frontend\README.md
```md
# Frontend

Built with Next.js 15 + ShadCN + TailwindCSS.

```

### File: backend\fonts\README.md
```md
# Fonts

This directory contains subtitle fonts that SupoClip can expose in the UI and use during clip rendering.

## How it works

- The backend scans this directory for supported font files.
- The frontend fetches the list through the fonts API.
- Selected fonts are applied to subtitles during rendering and editing flows.

## Supported formats

- `.ttf`
- `.otf`

## Adding a font

1. Copy the font file into this directory.
2. Restart the stack if the new file does not appear immediately.
3. Confirm the font is available through the app or `GET /fonts`.

## Notes

- Keep file names stable if they are already referenced by saved tasks or user defaults.
- Large font collections can make the picker harder to use, so prefer a curated set.
- Source and licensing notes for bundled fonts should go in [`SOURCES.md`](./SOURCES.md).


```

### File: backend\src\main.py
```py
from .youtube_utils import *
from .video_utils import *
from .ai import *
from .config import Config
from .caption_templates import get_template_info, get_template_names
from datetime import datetime
from contextlib import asynccontextmanager
from pathlib import Path
import logging
import json
import asyncio
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("logs/backend.log")],
)

logger = logging.getLogger(__name__)
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy import text

from .models import User, Task, Source, GeneratedClip
from .database import init_db, close_db, get_db, AsyncSessionLocal
from .auth_headers import get_signed_user_id, USER_ID_HEADER
from .api.routes.tasks import router as tasks_router
from .api.routes.feedback import router as feedback_router
from .api.routes.billing import router as billing_router
from .services.video_service import VideoService, UPLOAD_URL_PREFIX

config = Config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()
        yield
    finally:
        await close_db()


app = FastAPI(
    title="SupoClip API",
    description="Python-based backend for SupoClip",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[
        "Content-Type",
        "Authorization",
        "x-supoclip-user-id",
        "x-supoclip-ts",
        "x-supoclip-signature",
        "user_id",
    ],
)

# Include API routers
app.include_router(tasks_router)
app.include_router(feedback_router)
app.include_router(billing_router)

# Mount static files for serving clips
clips_dir = Path(config.temp_dir) / "clips"
clips_dir.mkdir(parents=True, exist_ok=True)
app.mount("/clips", StaticFiles(directory=str(clips_dir)), name="clips")


def _get_authenticated_user_id(request: Request) -> str:
    if config.monetization_enabled:
        return get_signed_user_id(request, config)

    user_id = request.headers.get("user_id") or request.headers.get(USER_ID_HEADER)
    if not user_id:
        raise HTTPException(status_code=401, detail="User authentication required")
    return user_id


def _resolve_uploaded_video_path(url: str) -> Path:
    return VideoService.resolve_local_video_path(url)


@app.get("/")
def read_root():
    return {
        "message": "This is the SupoClip FastAPI-based API. Visit /docs for the API documentation."
    }


@app.get("/health/db")
async def check_database_health(db: AsyncSession = Depends(get_db)):
    """Check database connectivity"""
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}


@app.post("/start")
async def start_task(request: Request):
    """Start a new task for authenticated users"""
    if config.monetization_enabled:
        raise HTTPException(status_code=404, detail="Not found")

    logger.info("🚀 Starting new task request")

    data = await request.json()

    raw_source = data.get("source")
    user_id = _get_authenticated_user_id(request)

    # Get font customization options from request
    font_options = data.get("font_options", {})
    font_family = font_options.get("font_family", "TikTokSans-Regular")
    font_size = font_options.get("font_size", 24)
    font_color = font_options.get("font_color", "#FFFFFF")

    # Get caption template and B-roll options
    caption_template = data.get("caption_template", "default")
    include_broll = data.get("include_broll", False)

    logger.info(
        f"📝 Request data - URL: {raw_source.get('url') if raw_source else 'None'}, User ID: {user_id}"
    )

    if not raw_source or not raw_source.get("url"):
        logger.error("❌ Source URL is missing")
        raise HTTPException(status_code=400, detail="Source URL is required")

    if not user_id:
        logger.error("❌ User ID is missing")
        raise HTTPException(status_code=401, detail="User authentication required")

    # Validate user_id is a valid string and user exists
    if not user_id or len(user_id.strip()) == 0:
        logger.error(f"❌ Invalid user ID format: {user_id}")
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    logger.info(f"🔍 Checking if user {user_id} exists in database")
    # Check if user exists in database
    async with AsyncSessionLocal() as db:
        user_exists = await db.execute(
            text("SELECT 1 FROM users WHERE id = :user_id"), {"user_id": user_id}
        )
        if not user_exists.fetchone():
            logger.error(f"❌ User {user_id} not found in database")
            raise HTTPException(status_code=404, detail="User not found")

        logger.info(f"✅ User {user_id} found in database")

        source = Source()
        source.type = source.decide_source_type(raw_source["url"])
        logger.info(f"📺 Source type detected: {source.type}")

        if source.type == "youtube":
            logger.info("🎬 Getting YouTube video title")
            source.title = get_youtube_video_title(raw_source["url"])
            if not source.title:
                logger.warning("⚠️ Could not get YouTube title, using default")
                source.title = "YouTube Video"
            logger.info(f"📝 Video title: {source.title}")
        else:
            source.title = raw_source.get("title", "Uploaded Video")
            logger.info(f"📝 Custom title: {source.title}")

        relevant_segments_json = []
        clips_info = []
        relevant_parts = None

        logger.info("💾 Saving source and creating task in database")
        async with AsyncSessionLocal() as db:
            db.add(source)
            await db.flush()
            logger.info(f"✅ Source saved with ID: {source.id}")

            task = Task(
                user_id=user_id,
                source_id=source.id,
                generated_clips_ids=None,
                font_family=font_family,
                font_size=font_size,
                font_color=font_color,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )

            db.add(task)
            await db.commit()
            logger.info(f"✅ Task created with ID: {task.id}")

            # Determine video path based on source type
            video_path = None
            if source.type == "youtube":
                logger.info("⬇️ Starting YouTube video download")
                video_path = download_youtube_video(raw_source["url"])
                if not video_path:
                    logger.error("❌ Failed to download video")
                    raise HTTPException(
                        status_code=500, detail="Failed to download video"
                    )
                logger.info(f"✅ Video downloaded to: {video_path}")
            else:
                video_path = _resolve_uploaded_video_path(raw_source["url"])
                logger.info(f"📁 Using uploaded video at: {video_path}")

                # Verify the uploaded file exists
                if not Path(video_path).exists():
                    logger.error(f"❌ Uploaded video file not found: {video_path}")
                    raise HTTPException(
                        status_code=404, detail="Uploaded video file not found"
                    )

            # Process video (same for both YouTube and uploaded videos)
            if video_path:
                logger.info(
                    "🎤 Starting transcript generation with AssemblyAI + SRT equalization"
                )
                transcript = get_video_transcript(video_path)
                logger.info(
                    f"✅ AssemblyAI transcript generated with 10-char line equalization (length: {len(transcript)} characters)"
                )

                logger.info(
                    "🤖 Starting AI analysis for relevant segments with virality scoring"
                )
                relevant_parts = await get_most_relevant_parts_by_transcript(
                    transcript, include_broll=include_broll
                )
                logger.info(
                    f"✅ AI analysis complete - found {len(relevant_parts.most_relevant_segments)} segments"
                )

                # Convert to JSON format for response with virality data
                logger.info(
                    "📊 Converting AI results to JSON format with virality scores"
                )
                relevant_segments_json = []
                for segment in relevant_parts.most_relevant_segments:
                    segment_data = {
                        "start_time": segment.start_time,
                        "end_time": segment.end_time,
                        "text": segment.text,
                        "relevance_score": segment.relevance_score,
                        "reasoning": segment.reasoning,
                    }
                    # Add virality data if available
                    if segment.virality:
                        segment_data.update(
                            {
                                "virality_score": segment.virality.total_score,
                                "hook_score": segment.virality.hook_score,
                                "engagement_score": segment.virality.engagement_score,
                                "value_score": segment.virality.value_score,
                                "shareability_score": segment.virality.shareability_score,
                                "hook_type": segment.virality.hook_type,
                                "virality_reasoning": segment.virality.virality_reasoning,
                            }
                        )
                    relevant_segments_json.append(segment_data)
                logger.info(f"✅ Created {len(relevant_segments_json)} segment records")

                # Create standalone clips from relevant segments and custom fonts
                logger.info("🎬 Starting standalone clip generation")
                clips_output_dir = Path(config.temp_dir) / "clips"
                logger.info(f"📁 Output directory: {clips_output_dir}")
                logger.info(
                    f"🎨 Font settings - Family: {font_family}, Size: {font_size}, Color: {font_color}, Template: {caption_template}"
                )
                clips_info = create_clips_with_transitions(
                    video_path,
                    relevant_segments_json,
                    clips_output_dir,
                    font_family,
                    font_size,
                    font_color,
                    caption_template,
                )
                logger.info(
                    f"✅ Generated {len(clips_info)} standalone video clips"
                )

                # Save clips to database
                logger.info("💾 Saving clips to database")
                async with AsyncSessionLocal() as db:
                    clip_ids = []
                    for i, clip_info in enumerate(clips_info):
                        logger.info(
                            f"💾 Saving clip {i + 1}/{len(clips_info)}: {clip_info['filename']}"
                        )
                        clip_record = GeneratedClip(
                            task_id=task.id,
                            filename=clip_info["filename"],
                            file_path=clip_info["path"],
                            start_time=clip_info["start_time"],
                            end_time=clip_info["end_time"],
                            duration=clip_info["duration"],
                            text=clip_info["text"],
                            relevance_score=clip_info["relevance_score"],
                            reasoning=clip_info["reasoning"],
                            clip_order=i + 1,
                            # Virality scores
                            virality_score=clip_info.get("virality_score", 0),
                            hook_score=clip_info.get("hook_score", 0),
                            engagement_score=clip_info.get("engagement_score", 0),
                            value_score=clip_info.get("value_score", 0),
                            shareability_score=clip_info.get("shareability_score", 0),
                            hook_type=clip_info.get("hook_type"),
                        )
                        db.add(clip_record)
                        await db.flush()
                        clip_ids.append(clip_record.id)
                        logger.info(f"✅ Clip {i + 1} saved with ID: {clip_record.id}")

                    # Update task with clip IDs
                    logger.info(f"🔗 Updating task with {len(clip_ids)} clip IDs")
                    task_update = await db.execute(
                        text(
                            "UPDATE tasks SET generated_clips_ids = :clip_ids WHERE id = :task_id"
                        ),
                        {"clip_ids": clip_ids, "task_id": task.id},
                    )
                    await db.commit()
                    logger.info("✅ Task updated with clip IDs")
            else:
                logger.error("❌ No video path available for processing")
                raise HTTPException(
                    status_code=500, detail="No video available for processing"
                )

            logger.info(f"🎉 Task completed successfully! Task ID: {task.id}")
        logger.info(
            f"📊 Final results - Segments: {len(relevant_segments_json)}, Clips: {len(clips_info)}"
        )

        return {
            "message": "Task started successfully",
            "task_id": task.id,
            "relevant_segments": relevant_segments_json,
            "clips": clips_info,
            "summary": relevant_parts.summary if relevant_parts else None,
            "key_topics": relevant_parts.key_topics if relevant_parts else None,
        }


@app.post("/start-with-progress")
async def start_task_with_progress(request: Request):
    """Start a new task and return task ID for SSE tracking"""
    if config.monetization_enabled:
        raise HTTPException(status_code=404, detail="Not found")

    data = await request.json()
    raw_source = data.get("source")
    user_id = _get_authenticated_user_id(request)

    # Get font customization options from request
    font_options = data.get("font_options", {})
    font_family = font_options.get("font_family", "TikTokSans-Regular")
    font_size = font_options.get("font_size", 24)
    font_color = font_options
... [TRUNCATED]
```

### File: AGENTS.md
```md
# Repository Guidelines

## Project Structure & Module Organization
This repository is a monorepo with three apps:
- `backend/`: FastAPI + async worker code (`src/api`, `src/services`, `src/repositories`, `src/workers`).
- `frontend/`: main Next.js app (`src/app`, `src/components`, `src/lib`, `prisma/`).
- `waitlist/`: separate Next.js marketing/waitlist app.

Infra and bootstrap files live at the root: `docker-compose.yml`, `init.sql`, `.env.example`, and `start.sh`.

## Build, Test, and Development Commands
Use Docker for full-stack development:
- `docker-compose up -d --build`: start frontend, backend, worker, Postgres, and Redis.
- `docker-compose logs -f`: stream service logs.
- `docker-compose down`: stop everything.

Local app commands:
- `cd frontend && npm run dev` (or `waitlist`): run Next.js in dev mode.
- `cd frontend && npm run build && npm run start`: production build + serve.
- `cd frontend && npm run lint` (same in `waitlist`): run ESLint.
- `cd backend && uv sync && uvicorn src.main:app --reload --host 0.0.0.0 --port 8000`: run API locally.
- `cd backend && .venv/bin/arq src.workers.tasks.WorkerSettings`: run the worker.

## Coding Style & Naming Conventions
- Python: 4-space indentation, type hints where practical, `snake_case` for functions/modules.
- TypeScript/React: 2-space indentation, `PascalCase` for component names, `camelCase` for variables/functions, route files in Next.js App Router conventions (`app/.../page.tsx`, `route.ts`).
- Linting: Next.js ESLint configs in `frontend/eslint.config.mjs` and `waitlist/eslint.config.mjs`.
- Imports: use the `@/*` alias in Next.js apps when possible.

## Testing Guidelines
There is no mature automated test suite yet. Treat linting plus manual verification as the current baseline:
- Run `npm run lint` in both Next.js apps.
- Smoke test core flows with `docker-compose` (create task, process clips, view task page).

When adding tests, place them near code or under `tests/` with clear names (`test_*.py`, `*.test.ts[x]`).

## Commit & Pull Request Guidelines
Recent history favors short imperative commit subjects (`Add list endpoint`, `Fix typo`, `improve UX`). Prefer:
- `type(scope): concise summary` (example: `feat(backend): add task list pagination`).
- One logical change per commit.

PRs should include:
- What changed and why.
- Any env/config or migration impact.
- Screenshots/GIFs for UI changes.
- Linked issue(s) and manual verification steps.

## Security & Configuration Tips
- Never commit real secrets; use `.env.example` as the template.
- Required runtime keys include `ASSEMBLY_AI_API_KEY` and either one hosted LLM provider key (`OPENAI_API_KEY`, `GOOGLE_API_KEY`, or `ANTHROPIC_API_KEY`) or an Ollama model configuration (`LLM=ollama:*`, optional `OLLAMA_BASE_URL`).

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SupoClip is an open-source alternative to OpusClip — an AI-powered video clipping tool that transforms long-form content into viral short clips. AGPL-3.0 licensed.

## Development Commands

### Docker (recommended)

```bash
docker-compose up -d              # Start all 5 services
docker-compose up -d --build      # Rebuild after changes
docker-compose logs -f backend    # Debug backend
docker-compose logs -f worker     # Debug video processing
docker-compose down               # Stop all services
```

Services: Frontend (:3000), Backend API (:8000, docs at /docs), Worker (ARQ), PostgreSQL (:5432), Redis (:6379)

### Backend (local)

Uses `uv` (not pip/poetry). Requires Python 3.11+, ffmpeg, running PostgreSQL and Redis.

```bash
cd backend
uv venv .venv && source .venv/bin/activate
uv sync

# API server (uses refactored entry point)
uvicorn src.main_refactored:app --reload --host 0.0.0.0 --port 8000

# Worker process (required for video processing)
arq src.workers.tasks.WorkerSettings
```

### Frontend (local)

```bash
cd frontend
npm install
npm run dev          # Dev server with Turbopack
npm run build        # Prisma generate + Next.js build
npm run lint
```

### Waitlist

```bash
cd waitlist
bun install          # Uses bun, not npm
bun run dev
```

### No tests

The project currently has no test files.

## Architecture

### System Overview

```
User → Frontend (Next.js 15) → Backend API (FastAPI) → Redis Queue → ARQ Worker
                                      ↓                                  ↓
                               PostgreSQL ←───────────────────────────────┘
```

Task creation returns immediately (<100ms). Video processing happens asynchronously in the worker. Frontend connects via SSE for real-time progress updates.

### Backend: Layered Architecture

The backend was refactored from monolithic (`main.py`, legacy) to layered (`main_refactored.py`, active):

```
api/routes/          → HTTP handlers (tasks.py, media.py)
services/            → Business logic (task_service.py, video_service.py)
repositories/        → Raw SQL via asyncpg (task_repository.py, clip_repository.py, source_repository.py)
workers/             → ARQ job queue (tasks.py, job_queue.py, progress.py)
utils/               → Thread pool helpers for blocking operations (async_helpers.py)
```

**Key patterns:**
- All DB access goes through repository classes using raw SQL (`text()` queries), not SQLAlchemy ORM
- Blocking operations (video processing, downloads, transcription) wrapped in `run_in_thread()` to avoid blocking the async event loop
- Progress tracking uses Redis pub/sub → SSE to frontend
- Task status flow: `queued → processing → completed/error/cancelled`

### Video Processing Pipeline

1. **Input** → YouTube URL (yt-dlp) or uploaded file
2. **Transcription** → AssemblyAI word-level timestamps (cached as `.transcript_cache.json`)
3. **AI Analysis** → Pydantic AI selects 3-7 viral segments (10-45s each) with virality scoring
4. **Clip Generation** → MoviePy creates 9:16 clips with:
   - Face-centered cropping: MediaPipe → OpenCV DNN → Haar cascade (fallback chain)
   - Word-synced subtitles from AssemblyAI
   - Custom fonts (TTF files in `backend/fonts/`)
   - Optional transition effects (`backend/transitions/`)
   - Optional B-roll overlays (Pexels API)
   - Caption templates with animation styles
5. **Storage** → Clips to `{TEMP_DIR}/clips/`, metadata to PostgreSQL

### Frontend Architecture

- **Next.js 15** with App Router, React 19, TailwindCSS v4
- **ShadCN UI** (New York style, stone base color, Radix primitives)
- **Better Auth** with Prisma adapter for email/password auth
- **No global state library** — React hooks only (`useState`, `useEffect`, `useSession`)
- All pages use `"use client"` — SSR is minimal
- Prisma client generated to `frontend/src/generated/prisma/` (custom output path)
- Build: `prisma generate && next build` (Prisma generate runs on both build and postinstall)

**Auth flow:** Frontend calls Better Auth → session cookie → passes `user_id` header to backend API

### Database

PostgreSQL 15. Schema in `init.sql`. Mixed naming conventions:
- `tasks`, `sources`, `generated_clips` → snake_case
- `session`, `account`, `verification`, `users` → camelCase (Better Auth)
- UUIDs stored as VARCHAR(36)
- Auto-update triggers on `updated_at`/`updatedAt` columns

## Key Backend Files

| File | Purpose |
|------|---------|
| `src/main_refactored.py` | Active FastAPI entry point (129 lines) |
| `src/main.py` | Legacy monolithic entry point (do not use for new work) |
| `src/api/routes/tasks.py` | Task CRUD, SSE progress, clip editing endpoints (711 lines) |
| `src/api/routes/media.py` | Fonts, transitions, uploads, templates |
| `src/services/task_service.py` | Task orchestration, clip editing logic (574 lines) |
| `src/services/video_service.py` | Video download, transcription, AI analysis, clip generation |
| `src/workers/tasks.py` | ARQ worker task definitions |
| `src/workers/job_queue.py` | Job queue management |
| `src/workers/progress.py` | Real-time progress via Redis |
| `src/ai.py` | Pydantic AI agents, system prompt, segment validation |
| `src/video_utils.py` | Video processing, cropping, subtitles (~820 lines) |
| `src/clip_editor.py` | Clip trim, split, merge, export presets |
| `src/broll.py` | Pexels API B-roll integration |
| `src/caption_templates.py` | Caption template system |
| `src/config.py` | Environment variable configuration |

## API Endpoints (routes in `api/routes/`)

**Task lifecycle:**
- `POST /start-with-progress` — Create task, enqueue to worker (returns task_id)
- `GET /tasks/` — List user tasks
- `GET /tasks/{id}` — Get task with clips
- `GET /tasks/{id}/progress` — SSE real-time progress stream
- `POST /tasks/{id}/cancel` — Cancel processing
- `POST /tasks/{id}/resume` — Resume cancelled/errored task
- `DELETE /tasks/{id}` — Delete task

**Clip editing:**
- `PATCH /tasks/{id}/clips/{clip_id}` — Trim clip
- `POST /tasks/{id}/clips/{clip_id}/split` — Split at timestamp
- `POST /tasks/{id}/clips/merge` — Merge selected clips
- `PATCH /tasks/{id}/clips/{clip_id}/captions` — Update captions
- `GET /tasks/{id}/clips/{clip_id}/export?preset=tiktok` — Export with platform preset

**Media:**
- `GET /fonts`, `GET /transitions`, `GET /caption-templates`, `GET /broll/status`
- `POST /upload` — Upload video file
- `GET /clips/{filename}` — Serve generated clips

## Environment Variables

Required in `.env` (root) or `backend/.env`:

```bash
ASSEMBLY_AI_API_KEY=...              # Required: video transcription
LLM=google-gla:gemini-3-flash-preview # Format: provider:model-name
GOOGLE_API_KEY=...                   # Or OPENAI_API_KEY / ANTHROPIC_API_KEY
OLLAMA_BASE_URL=http://localhost:11434/v1  # Optional for ollama:* models
OLLAMA_API_KEY=...                   # Optional; required for Ollama Cloud

# Optional
PEXELS_API_KEY=...                   # B-roll stock footage
REDIS_HOST=localhost                 # Default: localhost
REDIS_PORT=6379                      # Default: 6379
QUEUED_TASK_TIMEOUT_SECONDS=180      # Fail-safe for stuck tasks
TEMP_DIR=/tmp                        # Temp file storage
DATABASE_URL=postgresql+asyncpg://...
BETTER_AUTH_SECRET=...               # Frontend auth secret
```

## Common Workflows

### Adding fonts/transitions

Drop `.ttf` files into `backend/fonts/` or `.mp4` files into `backend/transitions/`. They auto-appear via their respective `GET` endpoints.

### Modifying AI clip selection

Edit `backend/src/ai.py`: `simplified_system_prompt` controls selection criteria, `TranscriptSegment` defines the output model, `get_most_relevant_parts_by_transcript()` runs analysis with validation.

### Video processing constraints

- Output: 9:16 vertical format, H.264, even pixel dimensions (`round_to_even()`)
- Subtitles positioned at 75% down the frame
- Virality scoring: `hook_score`, `engagement_score`, `value_score`, `shareability_score` (0-25 each, summed to `virality_score` 0-100)

```

### File: install_cron.sh
```sh
#!/usr/bin/env bash

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CRON_DIR="$REPO_DIR/.cron"
UPDATER_SCRIPT="$CRON_DIR/update_and_restart.sh"
LOG_FILE="$REPO_DIR/cron_update.log"
LOCK_FILE="/tmp/supoclip_auto_update.lock"

CRON_TAG_START="# supoclip-auto-update-start"
CRON_TAG_END="# supoclip-auto-update-end"
CRON_SCHEDULE="0 */3 * * *"

mkdir -p "$CRON_DIR"

cat > "$UPDATER_SCRIPT" <<EOF
#!/usr/bin/env bash

set -euo pipefail

REPO_DIR="$REPO_DIR"
LOG_FILE="$LOG_FILE"
LOCK_FILE="$LOCK_FILE"

exec >> "\$LOG_FILE" 2>&1

echo "[\$(date '+%Y-%m-%d %H:%M:%S')] Starting auto-update check"

if ! command -v flock >/dev/null 2>&1; then
  echo "flock command not found; aborting"
  exit 1
fi

exec 9>"\$LOCK_FILE"
if ! flock -n 9; then
  echo "Another update process is running; exiting"
  exit 0
fi

cd "\$REPO_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repository: \$REPO_DIR"
  exit 1
fi

if [ -n "\$(git status --porcelain)" ]; then
  echo "Repository has local changes; skipping update"
  exit 0
fi

git fetch --quiet

LOCAL_COMMIT="\$(git rev-parse HEAD)"
REMOTE_COMMIT="\$(git rev-parse @{u})"

if [ "\$LOCAL_COMMIT" = "\$REMOTE_COMMIT" ]; then
  echo "No updates found (\$LOCAL_COMMIT)"
  exit 0
fi

echo "Update detected: \$LOCAL_COMMIT -> \$REMOTE_COMMIT"
git pull --ff-only --quiet

if docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD="docker-compose"
else
  echo "Neither 'docker compose' nor 'docker-compose' is available"
  exit 1
fi

echo "Restarting Docker services"
\$COMPOSE_CMD down
\$COMPOSE_CMD up -d --build

echo "Update complete"
EOF

chmod +x "$UPDATER_SCRIPT"

EXISTING_CRON="$(crontab -l 2>/dev/null || true)"

UPDATED_CRON="$(printf '%s\n' "$EXISTING_CRON" | awk -v start="$CRON_TAG_START" -v end="$CRON_TAG_END" '
  $0 == start { skip = 1; next }
  $0 == end { skip = 0; next }
  !skip { print }
')"

CRON_LINE="$CRON_SCHEDULE $UPDATER_SCRIPT"

{
  printf '%s\n' "$UPDATED_CRON"
  printf '%s\n' "$CRON_TAG_START"
  printf '%s\n' "$CRON_LINE"
  printf '%s\n' "$CRON_TAG_END"
} | crontab -

echo "Installed cron job: $CRON_LINE"
echo "Logs will be written to: $LOG_FILE"

```

### File: QUICKSTART.md
```md
# SupoClip Quick Start Guide

Run SupoClip with Docker in just one command!

## Prerequisites

1. **Docker Desktop** installed and running
2. **API Keys** (get these from the providers):
   - [AssemblyAI API Key](https://www.assemblyai.com/) (required for transcription)
   - At least one AI provider:
      - [OpenAI API Key](https://platform.openai.com/api-keys) (recommended)
      - [Google AI API Key](https://makersuite.google.com/app/apikey)
      - [Anthropic API Key](https://console.anthropic.com/)
      - [Ollama](https://ollama.com/) (local/self-hosted, no API key required for local)

## Quick Start (Single Command)

```bash
./start.sh
```

That's it! The script will:
- Check prerequisites
- Build Docker images
- Start all services
- Show you where to access the app

## First Time Setup

### 1. Configure Environment Variables

Edit the `.env` file in the project root and add your API keys:

```bash
# Required for video transcription
ASSEMBLY_AI_API_KEY=your_assemblyai_key_here

# Choose one AI provider for clip selection
OPENAI_API_KEY=your_openai_key_here

# Configure which AI model to use
LLM=openai:gpt-4

# OR use Ollama locally
# LLM=ollama:gpt-oss:20b
# OLLAMA_BASE_URL=http://localhost:11434/v1

# Optional: Resend for waitlist + subscription lifecycle emails
# Required if you want hosted billing emails when SELF_HOST=false
# RESEND_API_KEY=your_resend_api_key_here
# RESEND_FROM_EMAIL="SupoClip <onboarding@your-domain.com>"
```

### 2. Start SupoClip

```bash
./start.sh
```

### 3. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Manual Docker Commands

If you prefer to use Docker commands directly:

```bash
# Start all services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild after code changes
docker-compose up -d --build
```

## Environment Configuration

### Required Variables

| Variable | Description | Where to Get |
|----------|-------------|--------------|
| `ASSEMBLY_AI_API_KEY` | Speech-to-text transcription | https://www.assemblyai.com/ |
| `LLM` | AI model identifier | e.g., `openai:gpt-5.2` or `ollama:gpt-oss:20b` |

### Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WHISPER_MODEL_SIZE` | `medium` | Whisper model size (tiny/base/small/medium/large) |
| `BETTER_AUTH_SECRET` | dev secret | Auth secret (change in production!) |
| `GOOGLE_API_KEY` | - | For Google Gemini models |
| `ANTHROPIC_API_KEY` | - | For Claude models |
| `OLLAMA_BASE_URL` | `http://localhost:11434/v1` | For local/self-hosted Ollama endpoint |
| `OLLAMA_API_KEY` | - | Optional, required for Ollama Cloud |
| `RESEND_API_KEY` | - | Optional in self-host mode, required for hosted billing/waitlist emails |
| `RESEND_FROM_EMAIL` | `SupoClip <onboarding@resend.dev>` | Verified sender for backend subscription emails |

### Hosted Billing Email Setup

If you enable hosted monetization with `SELF_HOST=false`, set these as well:

| Variable | Description |
|----------|-------------|
| `BACKEND_AUTH_SECRET` | Shared secret used by frontend API routes to call the backend |
| `STRIPE_SECRET_KEY` | Stripe server-side API key |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signing secret |
| `STRIPE_PRICE_ID` | Stripe price ID for the Pro subscription |
| `RESEND_API_KEY` | Resend API key used to send subscription emails |
| `RESEND_FROM_EMAIL` | Verified sender address used for subscription emails |

The billing flow sends:

- A thank-you email after `checkout.session.completed`
- A cancellation email after `customer.subscription.deleted`

## Supported AI Models

### OpenAI (Recommended)
```bash
LLM=openai:gpt-4
LLM=openai:gpt-4-turbo
LLM=openai:gpt-3.5-turbo
```

### Anthropic
```bash
LLM=anthropic:claude-3-5-sonnet-20241022
LLM=anthropic:claude-3-opus
LLM=anthropic:claude-3-haiku
```

### Google
```bash
LLM=google-gla:gemini-3-flash-preview
LLM=google-gla:gemini-3-pro-preview
```

### Ollama
```bash
LLM=ollama:gpt-oss:20b
OLLAMA_BASE_URL=http://localhost:11434/v1
```

## Troubleshooting

### Services not starting?

1. **Check Docker is running**:
   ```bash
   docker info
   ```

2. **View service logs**:
   ```bash
   docker-compose logs -f
   ```

3. **Check service health**:
   ```bash
   docker-compose ps
   ```

### API Keys not working?

1. Verify keys are set in `.env` file
2. Ensure no extra spaces around the `=` sign
3. Restart services after changing `.env`:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

### Database issues?

Reset the database:
```bash
docker-compose down -v  # WARNING: This deletes all data!
docker-compose up -d
```

## Architecture

SupoClip runs 4 Docker containers:

1. **Frontend** (Next.js 15) - Port 3000
2. **Backend** (FastAPI + Python) - Port 8000
3. **PostgreSQL** - Port 5432
4. **Redis** - Port 6379

All services are connected via a Docker network and start automatically with proper health checks.

## What Happens When You Run `./start.sh`?

1. Checks if `.env` file exists with required API keys
2. Verifies Docker is running
3. Builds Docker images (first time: ~5-10 minutes)
4. Starts PostgreSQL and waits for it to be healthy
5. Starts Redis cache
6. Starts backend API server
7. Starts frontend web server
8. Displays URLs for accessing the application

## Production Deployment

For production use:

1. Change `BETTER_AUTH_SECRET` to a secure random string
2. Use strong database passwords
3. Enable HTTPS with a reverse proxy (nginx/Caddy)
4. Set up persistent volumes for data
5. Configure backup strategies

## Next Steps

- Read the full documentation in `CLAUDE.md`
- Check out the API docs at http://localhost:8000/docs
- View example clips in the frontend
- Customize fonts by adding TTF files to `backend/fonts/`
- Add transition effects by adding MP4 files to `backend/transitions/`

## Getting Help

- Check logs: `docker-compose logs -f`
- View API documentation: http://localhost:8000/docs
- Report issues: Create a GitHub issue with logs and error messages

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
