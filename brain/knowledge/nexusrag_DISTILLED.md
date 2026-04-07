---
id: nexusrag
type: knowledge
owner: OA_Triage
---
# nexusrag
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

# NexusRAG

### Hybrid Knowledge Base with Agentic Chat, Citations & Knowledge Graph

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React_19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leducdat-profile)

**Upload documents. Ask questions. Get cited answers.**

NexusRAG combines vector search, knowledge graph, and cross-encoder reranking into one seamless RAG pipeline — powered by Gemini, local Ollama, or fully offline sentence-transformers.

[Features](#features) · [Quick Start](#quick-start) · [Model Recommendations](#multi-provider-llm) · [Tech Stack](#tech-stack)

</div>

---

## Architecture

<div align="center">

![NexusRAG Architecture](showcase/nexusrag_architecture.jpg)

</div>

## Showcase

<div align="center">
 
https://github.com/user-attachments/assets/fa845fab-dcc3-4a64-86ac-6dda2c073156

</div>

---

## Beyond Traditional RAG

Most RAG systems follow a simple pipeline: split text → embed → retrieve → generate. NexusRAG goes further at every stage:

| Aspect | Traditional RAG | NexusRAG |
|---|---|---|
| **Document Parsing** | Plain text extraction, structure lost | Docling or [Marker](https://github.com/datalab-to/marker): preserves headings, page boundaries, formulas, layout — switchable via config |
| **Images & Tables** | Ignored entirely | Extracted, captioned by vision LLM, embedded as searchable vectors |
| **Chunking** | Fixed-size splits, breaks mid-sentence | Hybrid semantic + structural chunking (respects headings, tables) |
| **Embeddings** | Single model for everything | Dual-model: BAAI/bge-m3 (1024d, search) + KG embedding (Gemini 3072d / Ollama / sentence-transformers) |
| **Retrieval** | Vector similarity only | 3-way parallel: Vector over-fetch + KG entity lookup + Cross-encoder rerank |
| **Knowledge** | No entity awareness | LightRAG graph: entity extraction, relationship mapping, multi-hop traversal |
| **Context** | Raw chunks dumped to LLM | Structured assembly: KG insights → cited chunks → related images/tables |
| **Citations** | None or manual | Auto-generated 4-char IDs with page number and heading path |
| **Page awareness** | Lost after chunking | Preserved end-to-end: chunk → citation → document viewer navigation |

---

## Features

<details>
<summary><b>Deep Document Parsing (Docling / Marker)</b></summary>

NexusRAG supports two document parsers, switchable via `NEXUSRAG_DOCUMENT_PARSER` env config:

| Feature | [Docling](https://github.com/docling-project/docling) (default) | [Marker](https://github.com/datalab-to/marker) |
|---|---|---|
| **Math/Formula** | Basic (known LaTeX issues) | Superior LaTeX via Surya |
| **GPU footprint** | ~18-20GB VRAM (formula enrichment) | ~2-4GB VRAM |
| **Formats** | PDF, DOCX, PPTX, HTML | PDF, DOCX, PPTX, XLSX, HTML, EPUB |
| **Chunking** | HybridChunker (semantic + structural) | Heading-aware + page-based |
| **Image extraction** | Via Docling pipeline | Via Marker pipeline |
| **Table extraction** | Structured export | Markdown tables |

Both parsers share the same output contract (`ParsedDocument`) — downstream pipeline (dedup, embedding, KG, retrieval) works identically regardless of parser choice.

**Common features across both parsers:**
- **Structural preservation** — Heading hierarchy, page boundaries, paragraph grouping
- **Multi-format** — PDF, DOCX, PPTX, TXT with consistent output
- **Page-aware metadata** — Every chunk carries its page number, heading path, and references to images/tables on the same page
- **LLM captioning** — Images and tables captioned by vision/text LLM for semantic search

```bash
# Switch parser in .env
NEXUSRAG_DOCUMENT_PARSER=marker   # or "docling" (default)
```

</details>

<details open>
<summary><b>Hybrid Retrieval Pipeline</b></summary>

| Stage | Technology | Details |
|---|---|---|
| **Vector Embedding** | BAAI/bge-m3 | 1024-dim multilingual bi-encoder (100+ languages) |
| **KG Embedding** | Gemini / Ollama / sentence-transformers | Configurable: Gemini (3072d), Ollama, or local sentence-transformers (e.g. bge-m3 1024d) |
| **Vector Search** | ChromaDB | Cosine similarity, over-fetch top-20 candidates |
| **Knowledge Graph** | LightRAG | Entity/relationship extraction, keyword-to-entity matching |
| **Reranking** | BAAI/bge-reranker-v2-m3 | Cross-encoder joint scoring — encodes (query, chunk) pairs together |
| **Generation** | Gemini / Ollama | Agentic streaming chat with function calling |

**Why two embedding models?** Vector search needs speed (local bge-m3, 1024-dim). Knowledge graph extraction needs semantic richness for entity recognition — choose Gemini Embedding (3072-dim, cloud), Ollama, or sentence-transformers (fully local, no API needed). Each model is optimized for its role.

**Retrieval flow:**
1. **Parallel retrieval** — Vector over-fetch (top-20) + KG entity lookup run simultaneously
2. **Cross-encoder reranking** — All 20 candidates scored jointly with the query through a transformer (far more precise than cosine similarity alone)
3. **Filtering** — Keep top-8 above relevance threshold (0.15), with fallback to top-3 if all below
4. **Media discovery** — Find images and tables on the same pages as retrieved chunks

</details>

<details>
<summary><b>Visual Document Intelligence</b></summary>

Images and tables are **embedded into chunk vectors** — not stored separately. When the parser extracts an image on page 5, its LLM-generated caption is appended to the text chunks on that page before embedding. This means searching for "revenue chart" finds chunks that contain the chart description, without needing a separate image search index.

**Image Pipeline**
1. Parser (Docling or Marker) extracts images from PDF/DOCX/PPTX (up to 50 per document)
2. Vision LLM (Gemini Vision or Ollama multimodal) generates captions: specific numbers, labels, trends
3. Captions appended to page chunks: `[Image on page 5]: Graph showing 12% revenue growth YoY`
4. Chunk is embedded → **image becomes vector-searchable** through its description
5. During retrieval, images on matched pages are surfaced as `[IMG-p4f2]` references

**Table Pipeline**
1. Parser exports tables as structured Markdown (preserving rows, columns, dimensions)
2. Text LLM summarizes each table: purpose, key columns, notable values (max 500 chars)
3. Summaries appended to page chunks: `[Table on page 5 (3x4)]: Annual sales by region`
4. Table summaries injected back into document Markdown as blockquotes for the document viewer

</details>

<details>
<summary><b>Custom Document Metadata</b></summary>

Enhance RAG accuracy and organization by attaching custom key-value metadata during document upload:

- **Metadata Filtering** — Perform hybrid search (semantic + metadata filtering) to narrow down the search space and prevent hallucinations.
- **Flexible Organization** — Tag documents with attributes like `year`, `category`, or `author` without needing separate workspaces.
- **Optimized Retrieval** — Pre-filtering in ChromaDB reduces processing time and latency during vector search.
- **Supported Endpoints** — Pass `custom_metadata` (list of key-values) in the upload API, and `metadata_filter` in query/chat APIs.

</details>

<details>
<summary><b>Citation System</b></summary>

Every answer is grounded in source documents with **4-character citation IDs** (e.g., `[a3z1]`):

- **Inline citations** — Clickable badges embedded directly in the answer text
- **Source cards** — Each citation shows filename, page number, heading path, and relevance score
- **Cross-navigation** — Click a citation to jump to the exact section in the document viewer
- **Image references** — Visual content cited separately as `[IMG-p4f2]` with page tracking
- **Strict grounding** — The LLM is instructed to only cite sources that directly support claims, max 3 per sentence

</details>

<details>
<summary><b>Knowledge Graph Visualization</b></summary>

Interactive force-directed graph built from extracted entities and relationships:

- **Entity types** — Person, Organization, Product, Location, Event, Technology, Financial Metric, Date, Regulation (configurable)
- **Force simulation** — Repulsion + spring forces + center gravity with real-time physics
- **Pan & zoom** — Mouse drag, scroll wheel (0.3x-3x), keyboard reset
- **Node interaction** — Click to select, hover to highlight connected edges, drag to reposition
- **Entity scaling** — Node radius proportional to connectivity (degree)
- **Query modes** — Naive, Local (multi-hop), Global (summary), Hybrid (default)
- **No extra services** — LightRAG uses file-based storage (NetworkX + NanoVectorDB), zero Docker overhead

</details>

<details>
<summary><b>Multi-Provider LLM</b></summary>

Switch between cloud and local models with a single environment variable:

#### Gemini (Cloud)

| Model | Best For | Thinking |
|---|---|---|
| `gemini-2.5-flash` | General chat, fast responses | Budget-based (auto) |
| `gemini-3.1-flash-lite` | High throughput, cost-effective **Recommended default**| Level-based: minimal / low / medium / high |

Extended thinking is automatically configured — Gemini 2.5 uses `thinking_budget_tokens`, Gemini 3.x uses `thinking_level`.

#### Ollama (Local / Self-hosted)

| Model | Parameters | Recommendation |
|---|---|---|
| `qwen3.5:9b` | 9B | Good multilingual support, solid tool calling **Recommended default** |
| `qwen3.5:4b` | 4B | Lightweight, works on 8GB RAM. May miss some tool calls |
| `gemma3:12b` | 12B | Best balance of quality and speed.  |

> **Tip**: For Knowledge Graph extraction, larger models (12B+) produce significantly better entity/relationship quality. Smaller models (4B) may extract zero entities on complex documents.

**Provider switching** — Comment/uncomment blocks in `.env`:

```bash
# Cloud (Gemini)
LLM_PROVIDER=gemini
GOOGLE_AI_API_KEY=your-key

# Local (Ollama) — uncomment to switch
# LLM_PROVIDER=ollama
# OLLAMA_MODEL=gemma3:12b
```

#### KG Embedding Providers

The Knowledge Graph embedding model is configured separately from the chat LLM:

| Provider | Config | API Required | Dimension |
|---|---|---|---|
| **Gemini** (default) | `KG_EMBEDDING_PROVIDER=gemini` | Google AI API key | 3072 |
| **Ollama** | `KG_EMBEDDING_PROVIDER=ollama` | Ollama server | Varies |
| **sentence-transformers** | `KG_EMBEDDING_PROVIDER=sentence_transformers` | None (fully local) | Model-dependent (e.g. 1024 for bge-m3) |

```bash
# Fully local KG embeddings — no API or external service needed
KG_EMBEDDING_PROVIDER=sentence_transformers
KG_EMBEDDING_MODEL=BAAI/bge-m3
KG_EMBEDDING_DIMENSION=1024
```

> **Tip**: `sentence_transformers` reuses the same `BAAI/bge-m3` model already downloaded for vector search — zero extra disk space, zero API costs, fully offline.

</details>

<details>
<summary><b>Agentic Streaming Chat</b></summary>

The chat system uses a semi-agentic architecture with real-time SSE streaming:

- **Agent steps** — Visual timeline: Analyzing → Retrieving → Generating → Done (with live timers)
- **Extended thinking** — Gemini/Ollama reasoning displayed in a collapsible panel
- **Function calling** — Native (Gemini) or prompt-based (Ollama) `search_documents` tool
- **Force-search mode** — Pre-retrieval before LLM generation for guaranteed grounded answers
- **Heartbeat** — 15s SSE keepalive prevents TCP timeout on slow responses
- **Fallback** — If Ollama produces empty output, auto-triggers search + retry
- **Chat history** — Persistent per workspace with message ratings (thumbs up/down)

</details>

<details>
<summary><b>UI / UX</b></summary>

**Theme & Layout**
- Dark / Light mode with smooth transition, persisted preference
- Collapsible sidebar with workspace navigation (icon-only mode at narrow width)
- Responsive grid layouts — mobile to desktop

**Chat Interface**
- Streaming token rendering with memoized paragraph blocks (only active block re-renders)
- Inline citation badges with hover tooltips (source file, page, heading path, relevance %)
- Agent step timeline with spinner animations and elapsed timers
- Thinking panel — scrollable, auto-follow, collapsible after completion
- Code blocks with syntax highlighting (Python, JS, SQL, etc.) and one-click copy

**Document Management**
- Drag-and-drop upload (PDF, DOCX, PPTX, TXT, MD — up to 50MB)
- Status badges with shimmer animation during processing
- Per-document chips: pages, chunks, images, tables, file size, processing time

**Search**
- 4 query modes: Hybrid, Vector, Local KG, Global KG
- Adjustable result count (1-20) with slider + direct input
- Document scope filtering (multi-select)
- Relevance score bars with color coding (green / amber / red)

**Analytics Dashboard**
- Stat cards: documents, indexed, chunks, images, entities, relationships
- Entity type distribution bar with animated widths
- Top entities ranked by connectivity
- Per-document chunk breakdown chart

**Micro-interactions**
- Framer Motion animations throughout (staggered entrances, layout transitions)
- Loading skeletons, toast notifications, empty state illustrations
- Keyboard shortcuts: `/` to focus search, `Enter` to send, `Escape` to cancel

</details>

<details>
<summary><b>Workspace System</b></summary>

- Multiple isolated knowledge bases, each with its own documents, ChromaDB collection, and KG
- Custom system prompt per workspace (override default Q&A behavior)
- Independent chat history with message persistence and ratings

</details>

---

## Evaluation

NexusRAG was evaluated using two complementary methods: **16 hand-crafted tests** (rule-based metrics) and **30 RAGAS synthetic tests** (LLM-as-judge). Test corpus: TechVina Annual Report 2025 (Vietnamese, 26 chunks) + DeepSeek-V3.2 Technical Paper (English, 57 chunks).

<details open>
<summary><b>Phase 1 — Hand-crafted Tests (Rule-based)</b></summary>

<div align="center">

![Phase 1 Evaluation](showcase/eval_phase1.png)

</div>

16 tests across 6 categories using 8 rule-based metrics (keyword coverage, refusal accuracy, citation format, language match, etc.) — no LLM judge involved.

| Category | Pass Rate | Avg Score |
|---|---|---|
| Fact Extraction (VI + EN) | 5/5 | 0.93 |
| Table Data | 2/3 | 0.83 |
| Cross-Document Reasoning | 2/2 | 0.89 |
| Anti-Hallucination | 3/3 | 1.00 |
| Multi-turn History | 2/2 | 0.87 |
| Citation Accuracy | 1/1 | 0.85 |
| **Overall** | **15/16** | **0.89 — EXCELLENT** |

</details>

... [TRUNCATED]
```

### File: backend\requirements.txt
```txt
# DeepRAG — Knowledge Base + RAG Backend
# ============================================

# Web framework
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
python-multipart>=0.0.6

# Database
sqlalchemy[asyncio]>=2.0.23
asyncpg>=0.29.0
alembic>=1.12.0

# Vector store
chromadb>=0.4.22

# Embeddings & reranking
sentence-transformers>=2.2.2

# Document parsing (Docling — default)
docling>=2.0.0

# Document parsing (Marker — alternative, better math/formula, lighter GPU)
# Install with: pip install marker-pdf[full]
# Activate with: NEXUSRAG_DOCUMENT_PARSER=marker
marker-pdf[full]>=1.10.0

# Text processing
langchain-text-splitters>=0.0.1

# LLM providers
google-genai>=1.0.0
ollama>=0.4.0

# Knowledge Graph (LightRAG)
lightrag-hku>=1.0.0

# Utilities
python-dotenv>=1.0.0
pydantic>=2.5.0
pydantic-settings>=2.1.0
httpx>=0.25.0
aiofiles>=23.2.1
Pillow>=10.0.0

```

### File: frontend\package.json
```json
{
  "name": "nexusrag-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "engines": {
    "node": ">=18.0.0",
    "pnpm": ">=8.0.0"
  },
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@radix-ui/react-popover": "^1.1.15",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/react-query": "^5.90.20",
    "@types/react-syntax-highlighter": "^15.5.13",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "framer-motion": "^12.33.0",
    "katex": "^0.16.33",
    "lucide-react": "^0.563.0",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-markdown": "^10.1.0",
    "react-router-dom": "^7.13.0",
    "react-syntax-highlighter": "^16.1.1",
    "rehype-katex": "^7.0.1",
    "remark-gfm": "^4.0.1",
    "remark-math": "^6.0.0",
    "sonner": "^2.0.7",
    "tailwind-merge": "^3.4.0",
    "zustand": "^5.0.11"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@tailwindcss/vite": "^4.1.18",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.0",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "eslint": "^9.39.1",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "globals": "^16.5.0",
    "tailwindcss": "^4.1.18",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.46.4",
    "vite": "^7.2.4"
  }
}

```

### File: backend\app\main.py
```py
"""
NexusRAG — standalone Knowledge Base + RAG application.
"""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import logging

from datetime import datetime, timedelta

from sqlalchemy import text, update

from app.core.config import settings
from app.core.database import engine, Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting NexusRAG API...")
    import os
    auto_create = os.environ.get("AUTO_CREATE_TABLES", "true").lower() == "true"
    if auto_create:
        async with engine.begin() as conn:
            # Check if tables already exist (e.g., alembic_version)
            result = await conn.execute(
                text("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'alembic_version');")
            )
            is_initialized = result.scalar()

            if not is_initialized:
                schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
                if os.path.exists(schema_path):
                    with open(schema_path, "r", encoding="utf-8") as f:
                        schema_sql = f.read()
                    
                    # Split and execute each statement to avoid asyncpg multi-statement issues
                    for statement in schema_sql.split(';'):
                        stmt = statement.strip()
                        if stmt:
                            await conn.execute(text(stmt))
                    logger.info("Database tables created from schema.sql")
                    
                    # Stamp the alembic version
                    await conn.execute(text("INSERT INTO public.alembic_version (version_num) VALUES ('2047460692d0') ON CONFLICT DO NOTHING;"))
                else:
                    await conn.run_sync(Base.metadata.create_all)
                    logger.info("Database tables created/verified (Base.metadata.create_all)")
            else:
                logger.info("Database is already initialized.")

        # Recover stale processing documents (stuck from previous runs)
        from app.models.document import Document, DocumentStatus
        from sqlalchemy.ext.asyncio import AsyncSession
        from sqlalchemy import select as sa_select
        async with AsyncSession(engine) as session:
            timeout = settings.NEXUSRAG_PROCESSING_TIMEOUT_MINUTES
            cutoff = datetime.utcnow() - timedelta(minutes=timeout)
            stale_statuses = [
                DocumentStatus.PROCESSING,
                DocumentStatus.PARSING,
                DocumentStatus.INDEXING,
            ]
            result = await session.execute(
                update(Document)
                .where(
                    Document.status.in_(stale_statuses),
                    Document.updated_at < cutoff,
                )
                .values(
                    status=DocumentStatus.FAILED,
                    error_message=f"Processing timeout ({timeout}min). Click Analyze to retry.",
                )
                .returning(Document.id)
            )
            stale_ids = [row[0] for row in result.fetchall()]
            if stale_ids:
                await session.commit()
                logger.warning(f"Recovered {len(stale_ids)} stale documents: {stale_ids}")
    else:
        logger.info("AUTO_CREATE_TABLES=false — skipping auto-migration")
    yield
    logger.info("Shutting down...")
    await engine.dispose()


app = FastAPI(
    title=settings.APP_NAME,
    description="NexusRAG — Knowledge Base with semantic search, knowledge graph, and LLM chat",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    redirect_slashes=False,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/ready")
async def ready():
    return {"status": "ready"}


# API routes
from app.api.router import api_router  # noqa: E402

app.include_router(api_router, prefix="/api/v1")

# Static files — document images extracted by NexusRAG (Docling)
_docling_data = Path(__file__).resolve().parent.parent / "data" / "docling"
_docling_data.mkdir(parents=True, exist_ok=True)
app.mount("/static/doc-images", StaticFiles(directory=str(_docling_data)), name="static_doc_images")

# Import models so SQLAlchemy registers them
from app.models import knowledge_base, document, chat_message  # noqa: E402, F401

```

### File: run_bk.sh
```sh
#!/bin/bash
# NexusRAG Backend — start FastAPI server (port 8080)
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/backend"

# Activate NexusRAG's own venv
if [ -d "$SCRIPT_DIR/venv" ]; then
    source "$SCRIPT_DIR/venv/bin/activate"
else
    echo "ERROR: venv not found. Create it first:"
    echo "  cd $SCRIPT_DIR && python3 -m venv venv && source venv/bin/activate && pip install -r backend/requirements.txt"
    exit 1
fi

echo "Starting NexusRAG backend on port 8080..."
uvicorn app.main:app --reload --port 8080

```

### File: run_fe.sh
```sh
#!/bin/bash
# NexusRAG Frontend — start Vite dev server
set -e

# Load nvm if available
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

cd "$(dirname "$0")/frontend"

# Install deps if needed
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    pnpm install
fi

echo "Starting NexusRAG frontend on port 5174..."
pnpm dev

```

### File: setup.sh
```sh
#!/bin/bash
# ============================================================
# NexusRAG — Local Development Setup
# ============================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "============================================"
echo "  NexusRAG — Local Development Setup"
echo "============================================"
echo ""

# -----------------------------------------------------------
# 1. Check prerequisites
# -----------------------------------------------------------
echo "[1/7] Checking prerequisites..."

# Python
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found. Install Python 3.10+ first."
    exit 1
fi
PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PY_MAJOR=$(echo "$PY_VERSION" | cut -d. -f1)
PY_MINOR=$(echo "$PY_VERSION" | cut -d. -f2)
if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
    echo "ERROR: Python 3.10+ required (found $PY_VERSION)"
    exit 1
fi
echo "  Python $PY_VERSION"

# Node
if ! command -v node &>/dev/null; then
    echo "ERROR: node not found. Install Node.js 18+ first."
    exit 1
fi
NODE_MAJOR=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$NODE_MAJOR" -lt 18 ]; then
    echo "ERROR: Node.js 18+ required (found $(node -v))"
    exit 1
fi
echo "  Node $(node -v)"

# pnpm
if ! command -v pnpm &>/dev/null; then
    echo "ERROR: pnpm not found. Install: npm install -g pnpm"
    exit 1
fi
echo "  pnpm $(pnpm -v)"

# Docker (optional)
if command -v docker &>/dev/null; then
    echo "  Docker $(docker --version | cut -d' ' -f3 | tr -d ',')"
    HAS_DOCKER=true
else
    echo "  Docker: not found (PostgreSQL + ChromaDB must be started manually)"
    HAS_DOCKER=false
fi

echo ""

# -----------------------------------------------------------
# 2. Create Python virtual environment
# -----------------------------------------------------------
echo "[2/7] Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  Created venv/"
else
    echo "  venv/ already exists"
fi
source venv/bin/activate

# -----------------------------------------------------------
# 3. Install Python dependencies
# -----------------------------------------------------------
echo "[3/7] Installing Python dependencies..."
pip install -q --upgrade pip
pip install -q -r backend/requirements.txt
echo "  Done."

# -----------------------------------------------------------
# 4. Create .env if not exists
# -----------------------------------------------------------
echo "[4/7] Checking .env configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "  Created .env from .env.example"
    echo "  >>> IMPORTANT: Edit .env and set GOOGLE_AI_API_KEY <<<"
else
    echo "  .env already exists"
fi

# -----------------------------------------------------------
# 5. Start services (Docker)
# -----------------------------------------------------------
echo "[5/7] Starting database services..."
if [ "$HAS_DOCKER" = true ]; then
    docker compose -f docker-compose.services.yml up -d
    echo "  Waiting for PostgreSQL to be ready..."
    for i in $(seq 1 30); do
        if docker exec nexusrag-postgres pg_isready -U postgres &>/dev/null; then
            echo "  PostgreSQL ready."
            break
        fi
        if [ "$i" -eq 30 ]; then
            echo "  WARNING: PostgreSQL not ready after 30s. Check docker logs."
        fi
        sleep 1
    done
else
    echo "  Skipped (no Docker). Ensure PostgreSQL (port 5433) and ChromaDB (port 8002) are running."
fi

# -----------------------------------------------------------
# 6. Download ML models (optional)
# -----------------------------------------------------------
echo ""
echo "[6/7] ML models (~2.5GB total):"
echo "  - BAAI/bge-m3 (embedding, ~1.4GB)"
echo "  - BAAI/bge-reranker-v2-m3 (reranker, ~1.1GB)"
echo ""
read -p "  Download models now? [y/N] " -n 1 -r
echo ""
if [[ $REPLY =~ ^[yY]$ ]]; then
    echo "  Downloading models (this may take a few minutes)..."
    python backend/scripts/download_models.py
else
    echo "  Skipped. Models will be downloaded on first use."
fi

# -----------------------------------------------------------
# 7. Install frontend dependencies
# -----------------------------------------------------------
echo "[7/7] Installing frontend dependencies..."
cd frontend
pnpm install
cd ..

# -----------------------------------------------------------
# Done
# -----------------------------------------------------------
echo ""
echo "============================================"
echo "  Setup Complete!"
echo "============================================"
echo ""
echo "  Start backend:   ./run_bk.sh"
echo "  Start frontend:  ./run_fe.sh"
echo "  Open:            http://localhost:5174"
echo ""
echo "  Or use Docker:   docker compose up -d"
echo ""

```

### File: frontend\index.html
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/png" href="/logo.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
    <title>NexusRAG</title>
    <script>
      // Set theme before first paint to prevent flash
      (function() {
        var theme = localStorage.getItem('theme');
        if (!theme) {
          theme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
        }
        document.documentElement.setAttribute('data-theme', theme);
      })();
    </script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: frontend\pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      '@radix-ui/react-popover':
        specifier: ^1.1.15
        version: 1.1.15(@types/react-dom@19.2.3(@types/react@19.2.14))(@types/react@19.2.14)(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      '@tailwindcss/typography':
        specifier: ^0.5.19
        version: 0.5.19(tailwindcss@4.2.1)
      '@tanstack/react-query':
        specifier: ^5.90.20
        version: 5.90.21(react@19.2.4)
      '@types/react-syntax-highlighter':
        specifier: ^15.5.13
        version: 15.5.13
      class-variance-authority:
        specifier: ^0.7.1
        version: 0.7.1
      clsx:
        specifier: ^2.1.1
        version: 2.1.1
      framer-motion:
        specifier: ^12.33.0
        version: 12.34.3(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      katex:
        specifier: ^0.16.33
        version: 0.16.33
      lucide-react:
        specifier: ^0.563.0
        version: 0.563.0(react@19.2.4)
      react:
        specifier: ^19.2.0
        version: 19.2.4
      react-dom:
        specifier: ^19.2.0
        version: 19.2.4(react@19.2.4)
      react-markdown:
        specifier: ^10.1.0
        version: 10.1.0(@types/react@19.2.14)(react@19.2.4)
      react-router-dom:
        specifier: ^7.13.0
        version: 7.13.1(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      react-syntax-highlighter:
        specifier: ^16.1.1
        version: 16.1.1(react@19.2.4)
      rehype-katex:
        specifier: ^7.0.1
        version: 7.0.1
      remark-gfm:
        specifier: ^4.0.1
        version: 4.0.1
      remark-math:
        specifier: ^6.0.0
        version: 6.0.0
      sonner:
        specifier: ^2.0.7
        version: 2.0.7(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      tailwind-merge:
        specifier: ^3.4.0
        version: 3.5.0
      zustand:
        specifier: ^5.0.11
        version: 5.0.11(@types/react@19.2.14)(react@19.2.4)
    devDependencies:
      '@eslint/js':
        specifier: ^9.39.1
        version: 9.39.3
      '@tailwindcss/vite':
        specifier: ^4.1.18
        version: 4.2.1(vite@7.3.1(@types/node@24.10.15)(jiti@2.6.1)(lightningcss@1.31.1))
      '@types/node':
        specifier: ^24.10.1
        version: 24.10.15
      '@types/react':
        specifier: ^19.2.0
        version: 19.2.14
      '@types/react-dom':
        specifier: ^19.2.3
        version: 19.2.3(@types/react@19.2.14)
      '@vitejs/plugin-react':
        specifier: ^5.1.1
        version: 5.1.4(vite@7.3.1(@types/node@24.10.15)(jiti@2.6.1)(lightningcss@1.31.1))
      eslint:
        specifier: ^9.39.1
        version: 9.39.3(jiti@2.6.1)
      eslint-plugin-react-hooks:
        specifier: ^7.0.1
        version: 7.0.1(eslint@9.39.3(jiti@2.6.1))
      eslint-plugin-react-refresh:
        specifier: ^0.4.24
        version: 0.4.26(eslint@9.39.3(jiti@2.6.1))
      globals:
        specifier: ^16.5.0
        version: 16.5.0
      tailwindcss:
        specifier: ^4.1.18
        version: 4.2.1
      typescript:
        specifier: ~5.9.3
        version: 5.9.3
      typescript-eslint:
        specifier: ^8.46.4
        version: 8.56.1(eslint@9.39.3(jiti@2.6.1))(typescript@5.9.3)
      vite:
        specifier: ^7.2.4
        version: 7.3.1(@types/node@24.10.15)(jiti@2.6.1)(lightningcss@1.31.1)

packages:

  '@babel/code-frame@7.29.0':
    resolution: {integrity: sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==}
    engines: {node: '>=6.9.0'}

  '@babel/compat-data@7.29.0':
    resolution: {integrity: sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==}
    engines: {node: '>=6.9.0'}

  '@babel/core@7.29.0':
    resolution: {integrity: sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==}
    engines: {node: '>=6.9.0'}

  '@babel/generator@7.29.1':
    resolution: {integrity: sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-compilation-targets@7.28.6':
    resolution: {integrity: sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-globals@7.28.0':
    resolution: {integrity: sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-imports@7.28.6':
    resolution: {integrity: sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-transforms@7.28.6':
    resolution: {integrity: sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-plugin-utils@7.28.6':
    resolution: {integrity: sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-string-parser@7.27.1':
    resolution: {integrity: sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.28.5':
    resolution: {integrity: sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-option@7.27.1':
    resolution: {integrity: sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==}
    engines: {node: '>=6.9.0'}

  '@babel/helpers@7.28.6':
    resolution: {integrity: sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.29.0':
    resolution: {integrity: sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/plugin-transform-react-jsx-self@7.27.1':
    resolution: {integrity: sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/plugin-transform-react-jsx-source@7.27.1':
    resolution: {integrity: sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/runtime@7.28.6':
    resolution: {integrity: sha512-05WQkdpL9COIMz4LjTxGpPNCdlpyimKppYNoJ5Di5EUObifl8t4tuLuUBBZEpoLYOmfvIWrsp9fCl0HoPRVTdA==}
    engines: {node: '>=6.9.0'}

  '@babel/template@7.28.6':
    resolution: {integrity: sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==}
    engines: {node: '>=6.9.0'}

  '@babel/traverse@7.29.0':
    resolution: {integrity: sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==}
    engines: {node: '>=6.9.0'}

  '@babel/types@7.29.0':
    resolution: {integrity: sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==}
    engines: {node: '>=6.9.0'}

  '@esbuild/aix-ppc64@0.27.3':
    resolution: {integrity: sha512-9fJMTNFTWZMh5qwrBItuziu834eOCUcEqymSH7pY+zoMVEZg3gcPuBNxH1EvfVYe9h0x/Ptw8KBzv7qxb7l8dg==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.27.3':
    resolution: {integrity: sha512-YdghPYUmj/FX2SYKJ0OZxf+iaKgMsKHVPF1MAq/P8WirnSpCStzKJFjOjzsW0QQ7oIAiccHdcqjbHmJxRb/dmg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.27.3':
    resolution: {integrity: sha512-i5D1hPY7GIQmXlXhs2w8AWHhenb00+GxjxRncS2ZM7YNVGNfaMxgzSGuO8o8SJzRc/oZwU2bcScvVERk03QhzA==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.27.3':
    resolution: {integrity: sha512-IN/0BNTkHtk8lkOM8JWAYFg4ORxBkZQf9zXiEOfERX/CzxW3Vg1ewAhU7QSWQpVIzTW+b8Xy+lGzdYXV6UZObQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.27.3':
    resolution: {integrity: sha512-Re491k7ByTVRy0t3EKWajdLIr0gz2kKKfzafkth4Q8A5n1xTHrkqZgLLjFEHVD+AXdUGgQMq+Godfq45mGpCKg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.27.3':
    resolution: {integrity: sha512-vHk/hA7/1AckjGzRqi6wbo+jaShzRowYip6rt6q7VYEDX4LEy1pZfDpdxCBnGtl+A5zq8iXDcyuxwtv3hNtHFg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.27.3':
    resolution: {integrity: sha512-ipTYM2fjt3kQAYOvo6vcxJx3nBYAzPjgTCk7QEgZG8AUO3ydUhvelmhrbOheMnGOlaSFUoHXB6un+A7q4ygY9w==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.27.3':
    resolution: {integrity: sha512-dDk0X87T7mI6U3K9VjWtHOXqwAMJBNN2r7bejDsc+j03SEjtD9HrOl8gVFByeM0aJksoUuUVU9TBaZa2rgj0oA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.27.3':
    resolution: {integrity: sha512-sZOuFz/xWnZ4KH3YfFrKCf1WyPZHakVzTiqji3WDc0BCl2kBwiJLCXpzLzUBLgmp4veFZdvN5ChW4Eq/8Fc2Fg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.27.3':
    resolution: {integrity: sha512-s6nPv2QkSupJwLYyfS+gwdirm0ukyTFNl3KTgZEAiJDd+iHZcbTPPcWCcRYH+WlNbwChgH2QkE9NSlNrMT8Gfw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.27.3':
    resolution: {integrity: sha512-yGlQYjdxtLdh0a3jHjuwOrxQjOZYD/C9PfdbgJJF3TIZWnm/tMd/RcNiLngiu4iwcBAOezdnSLAwQDPqTmtTYg==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.27.3':
    resolution: {integrity: sha512-WO60Sn8ly3gtzhyjATDgieJNet/KqsDlX5nRC5Y3oTFcS1l0KWba+SEa9Ja1GfDqSF1z6hif/SkpQJbL63cgOA==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.27.3':
    resolution: {integrity: sha512-APsymYA6sGcZ4pD6k+UxbDjOFSvPWyZhjaiPyl/f79xKxwTnrn5QUnXR5prvetuaSMsb4jgeHewIDCIWljrSxw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.27.3':
    resolution: {integrity: sha512-eizBnTeBefojtDb9nSh4vvVQ3V9Qf9Df01PfawPcRzJH4gFSgrObw+LveUyDoKU3kxi5+9RJTCWlj4FjYXVPEA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.27.3':
    resolution: {integrity: sha512-3Emwh0r5wmfm3ssTWRQSyVhbOHvqegUDRd0WhmXKX2mkHJe1SFCMJhagUleMq+Uci34wLSipf8Lagt4LlpRFWQ==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.27.3':
    resolution: {integrity: sha512-pBHUx9LzXWBc7MFIEEL0yD/ZVtNgLytvx60gES28GcWMqil8ElCYR4kvbV2BDqsHOvVDRrOxGySBM9Fcv744hw==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.27.3':
    resolution: {integrity: sha512-Czi8yzXUWIQYAtL/2y6vogER8pvcsOsk5cpwL4Gk5nJqH5UZiVByIY8Eorm5R13gq+DQKYg0+JyQoytLQas4dA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.27.3':
    resolution: {integrity: sha512-sDpk0RgmTCR/5HguIZa9n9u+HVKf40fbEUt+iTzSnCaGvY9kFP0YKBWZtJaraonFnqef5SlJ8/TiPAxzyS+UoA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.27.3':
    resolution: {integrity: sha512-P14lFKJl/DdaE00LItAukUdZO5iqNH7+PjoBm+fLQjtxfcfFE20Xf5CrLsmZdq5LFFZzb5JMZ9grUwvtVYzjiA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.27.3':
    resolution: {integrity: sha512-AIcMP77AvirGbRl/UZFTq5hjXK+2wC7qFRGoHSDrZ5v5b8DK/GYpXW3CPRL53NkvDqb9D+alBiC/dV0Fb7eJcw==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.27.3':
    resolution: {integrity: sha512-DnW2sRrBzA+YnE70LKqnM3P+z8vehfJWHXECbwBmH/CU51z6FiqTQTHFenPlHmo3a8UgpLyH3PT+87OViOh1AQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openharmony-arm64@0.27.3':
    resolution: {integrity: sha512-NinAEgr/etERPTsZJ7aEZQvvg/A6IsZG/LgZy+81wON2huV7SrK3e63dU0XhyZP4RKGyTm7aOgmQk0bGp0fy2g==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openharmony]

  '@esbuild/sunos-x64@0.27.3':
    resolution: {integrity: sha512-PanZ+nEz+eWoBJ8/f8HKxTTD172SKwdXebZ0ndd953gt1HRBbhMsaNqjTyYLGLPdoWHy4zLU7bDVJztF5f3BHA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/win32-arm64@0.27.3':
    resolution: {integrity: sha512-B2t59lWWYrbRDw/tjiWOuzSsFh1Y/E95ofKz7rIVYSQkUYBjfSgf6oeYPNWHToFRr2zx52JKApIcAS/D5TUBnA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-ia32@0.27.3':
    resolution: {integrity: sha512-QLKSFeXNS8+tHW7tZpMtjlNb7HKau0QDpwm49u0vUp9y1WOF+PEzkU84y9GqYaAVW8aH8f3GcBck26jh54cX4Q==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-x64@0.27.3':
    resolution: {integrity: sha512-4uJGhsxuptu3OcpVAzli+/gWusVGwZZHTlS63hh++ehExkVT8SgiEf7/uC/PclrPPkLhZqGgCTjd0VWLo6xMqA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [win32]

  '@eslint-community/eslint-utils@4.9.1':
    resolution: {integrity: sha512-phrYmNiYppR7znFEdqgfWHXR6NCkZEK7hwWDHZUjit/2/U0r6XvkDl0SYnoM51Hq7FhCGdLDT6zxCCOY1hexsQ==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: ^6.0.0 || ^7.0.0 || >=8.0.0

  '@eslint-community/regexpp@4.12.2':
    resolution: {integrity: sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==}
    engines: {node: ^12.0.0 || ^14.0.0 || >=16.0.0}

  '@eslint/config-array@0.21.1':
    resolution: {integrity: sha512-aw1gNayWpdI/jSYVgzN5pL0cfzU02GT3NBpeT/DXbx1/1x7ZKxFPd9bwrzygx/qiwIQiJ1sw/zD8qY/kRvlGHA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/config-helpers@0.4.2':
    resolution: {integrity: sha512-gBrxN88gOIf3R7ja5K9slwNayVcZgK6SOUORm2uBzTeIEfeVaIhOpCtTox3P6R7o2jLFwLFTLnC7kU/RGcYEgw==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/core@0.17.0':
    resolution: {integrity: sha512-yL/sLrpmtDaFEiUj1osRP4TI2MDz1AddJL+jZ7KSqvBuliN4xqYY54IfdN8qD8Toa6g1iloph1fxQNkjOxrrpQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/eslintrc@3.3.4':
    resolution: {integrity: sha512-4h4MVF8pmBsncB60r0wSJiIeUKTSD4m7FmTFThG8RHlsg9ajqckLm9OraguFGZE4vVdpiI1Q4+hFnisopmG6gQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/js@9.39.3':
    resolution: {integrity: sha512-1B1VkCq6FuUNlQvlBYb+1jDu/gV297TIs/OeiaSR9l1H27SVW55ONE1e1Vp16NqP683+xEGzxYtv4XCiDPaQiw==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/object-schema@2.1.7':
    resolution: {integrity: sha512-VtAOaymWVfZcmZbp6E2mympDIHvyjXs/12LqWYjVw6qjrfF+VK+fyG33kChz3nnK+SU5/NeHOqrTEHS8sXO3OA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@eslint/plugin-kit@0.4.1':
    resolution: {integrity: sha512-43/qtrDUokr7LJqoF2c3+RInu/t4zfrpYdoSDfYyhg52rwLV
... [TRUNCATED]
```

### File: frontend\tsconfig.app.json
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "types": ["vite/client"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,

    /* Path aliases */
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"]
}

```

### File: frontend\tsconfig.json
```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}

```

### File: frontend\tsconfig.node.json
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "ESNext",
    "types": ["node"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}

```

### File: frontend\vite.config.ts
```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5174,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
      '/static': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
})

```

### File: tasks\lessons.md
```md
# Lessons Learned
_To be updated as mistakes or clarifications arise during the task._

```

### File: tasks\todo.md
```md
# Support Postgres as Vector DB

## Goal
Add an option to use PostgreSQL (via pgvector) as a vector database instead of just ChromaDB.

## Success Criteria
1. Configuration setting `VECTOR_DB_PROVIDER` (`chroma` or `postgres`) is added and properly respected.
2. Abstract VectorStore interface or a consistent duck-typing signature is defined.
3. Existing `VectorStore` in `vector_store.py` is renamed/moved to `ChromaVectorStore`.
4. A new `PostgresVectorStore` is created.
5. `pgvector` dependency is added to `backend/requirements.txt` and DB initialized properly with `pgvector` extension.
6. The factory methods provide the correct vector store instance.
7. Postgres vector database configuration is available in `docker-compose.yml`.

## Steps
- [ ] List directory structure and examine database models/migrations to understand how to add `pgvector`.
- [ ] Create detailed Implementation Plan (pseudocode) for approval.
- [ ] Update `backend/app/core/config.py`.
- [ ] Define abstract vector store and implement `ChromaVectorStore` & `PostgresVectorStore`.
- [ ] Update database setup (migrations or init scripts) to initialize `vector` extension and table if using PG.
- [ ] Update `backend/requirements.txt`.
- [ ] Update `docker-compose.yml` and related environment variables.
- [ ] Verify functionality (testing with both providers).

```

### File: backend\app\__init__.py
```py

```

### File: backend\scripts\download_models.py
```py
"""Pre-download sentence-transformers models for offline use.

Usage:
    python backend/scripts/download_models.py

Environment variables (optional):
    NEXUSRAG_EMBEDDING_MODEL  — default: BAAI/bge-m3
    NEXUSRAG_RERANKER_MODEL   — default: BAAI/bge-reranker-v2-m3
"""
import os
import sys


def download_models():
    embedding_model = os.environ.get("NEXUSRAG_EMBEDDING_MODEL", "BAAI/bge-m3")
    reranker_model = os.environ.get("NEXUSRAG_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3")

    from sentence_transformers import SentenceTransformer, CrossEncoder

    print(f"[1/2] Downloading embedding model: {embedding_model}")
    SentenceTransformer(embedding_model)
    print(f"      Done.")

    print(f"[2/2] Downloading reranker model: {reranker_model}")
    CrossEncoder(reranker_model)
    print(f"      Done.")

    print("\nAll models downloaded successfully.")


if __name__ == "__main__":
    download_models()

```

### File: backend\scripts\eval_rag.py
```py
"""
NexusRAG Evaluation Script — Production-grade RAG quality assessment.

Uses DeepEval metrics (LLM-as-judge) + custom rule-based checks.
Supports Ollama (local) and Gemini (cloud) as judge models.

Usage:
    cd NexusRAG/backend
    source ../venv/bin/activate
    python scripts/eval_rag.py --workspace 11 [--judge ollama|gemini]
"""

import argparse
import asyncio
import json
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import requests

# ── Configuration ─────────────────────────────────────────────────────────────

BASE_URL = "http://localhost:8080/api/v1/rag"
TIMEOUT = 120  # seconds per request


# ── Data structures ───────────────────────────────────────────────────────────

@dataclass
class TestCase:
    """A single evaluation test case."""
    id: str
    category: str  # fact_extraction, table_data, cross_doc, anti_hallucination, history, citation
    question: str
    language: str  # vi, en
    history: list[dict] = field(default_factory=list)
    # Ground truth (optional — for reference-based metrics)
    expected_answer: str = ""
    expected_keywords: list[str] = field(default_factory=list)
    expected_refuse: bool = False  # Should the system refuse to answer?
    # Results (filled after evaluation)
    answer: str = ""
    retrieved_contexts: list[str] = field(default_factory=list)
    source_count: int = 0
    latency_ms: float = 0


@dataclass
class MetricResult:
    """Result of a single metric evaluation."""
    name: str
    score: float  # 0.0 - 1.0
    passed: bool
    reason: str = ""


@dataclass
class TestResult:
    """Full evaluation result for a test case."""
    test_id: str
    category: str
    question: str
    language: str
    answer_preview: str
    source_count: int
    latency_ms: float
    metrics: list[MetricResult] = field(default_factory=list)
    overall_score: float = 0.0


# ── Test Dataset ──────────────────────────────────────────────────────────────

def build_test_cases(workspace_id: int) -> list[TestCase]:
    """
    Hand-crafted test cases for KBG9 workspace (id=11).
    Documents:
      - doc 11: TechVina annual report 2025 (Vietnamese)
      - doc 12: DeepSeek-V3.2 technical paper (English)
    """
    cases = [
        # ── Fact Extraction (Vietnamese doc) ──
        TestCase(
            id="FACT-VI-01",
            category="fact_extraction",
            question="TechVina được thành lập năm nào và hoạt động ở bao nhiêu quốc gia?",
            language="vi",
            expected_keywords=["2010", "12"],
        ),
        TestCase(
            id="FACT-VI-02",
            category="fact_extraction",
            question="Doanh thu của TechVina năm 2025 là bao nhiêu và tăng trưởng bao nhiêu phần trăm?",
            language="vi",
            expected_keywords=["4.850", "4850", "23,4", "23.4"],
        ),
        TestCase(
            id="FACT-VI-03",
            category="fact_extraction",
            question="TechVina có bao nhiêu nhân sự và phân bổ theo trình độ như thế nào?",
            language="vi",
            expected_keywords=["3.200", "3200"],
        ),
        # ── Fact Extraction (English doc) ──
        TestCase(
            id="FACT-EN-01",
            category="fact_extraction",
            question="What are the key technical breakthroughs of DeepSeek-V3.2?",
            language="en",
            expected_keywords=["DSA", "Sparse Attention", "reinforcement", "RL"],
        ),
        TestCase(
            id="FACT-EN-02",
            category="fact_extraction",
            question="What competitions did DeepSeek-V3.2 achieve gold-medal performance in?",
            language="en",
            expected_keywords=["IMO", "IOI"],
        ),
        # ── Table Data Extraction ──
        TestCase(
            id="TABLE-01",
            category="table_data",
            question="Cho tôi biết doanh thu thuần và EBITDA của TechVina từ 2023-2025?",
            language="vi",
            expected_keywords=["3.180", "3180", "4.850", "4850", "890"],
        ),
        TestCase(
            id="TABLE-02",
            category="table_data",
            question="Biên lợi nhuận gộp và ROE của TechVina qua các năm 2023-2025 là bao nhiêu?",
            language="vi",
            expected_keywords=["40", "42", "44", "12,8", "15,6", "18,7"],
        ),
        TestCase(
            id="TABLE-03",
            category="table_data",
            question="DeepSeek-V3.2 đạt kết quả bao nhiêu trên AIME 2025 và HMMT Feb 2025?",
            language="vi",
            expected_keywords=["93.1", "AIME"],
        ),
        # ── Cross-Document Reasoning ──
        TestCase(
            id="CROSS-01",
            category="cross_doc",
            question="TechVina có mảng AI Platform không? Doanh thu mảng này là bao nhiêu? Và DeepSeek-V3.2 có những khả năng AI gì nổi bật?",
            language="vi",
            expected_keywords=["AI Platform", "900", "DSA"],
        ),
        TestCase(
            id="CROSS-02",
            category="cross_doc",
            question="TechVina đầu tư bao nhiêu cho R&D? DeepSeek-V3.2 có đóng góp gì cho cộng đồng open-source?",
            language="vi",
            expected_keywords=["R&D", "12"],
        ),
        # ── Anti-Hallucination (should refuse) ──
        TestCase(
            id="ANTI-01",
            category="anti_hallucination",
            question="Elon Musk sinh năm bao nhiêu?",
            language="vi",
            expected_refuse=True,
        ),
        TestCase(
            id="ANTI-02",
            category="anti_hallucination",
            question="Cách nấu phở Hà Nội ngon nhất?",
            language="vi",
            expected_refuse=True,
        ),
        TestCase(
            id="ANTI-03",
            category="anti_hallucination",
            question="Bitcoin giá bao nhiêu hôm nay?",
            language="vi",
            expected_refuse=True,
        ),
        # ── History / Follow-up ──
        TestCase(
            id="HIST-01",
            category="history",
            question="Mảng nào tăng trưởng mạnh nhất?",
            language="vi",
            history=[
                {"role": "user", "content": "TechVina có những mảng kinh doanh chính nào?"},
                {"role": "assistant", "content": "TechVina có 4 mảng kinh doanh chính:\n1. Giải pháp phần mềm: 1.890 tỷ VNĐ\n2. Dịch vụ Cloud: 1.520 tỷ VNĐ\n3. AI Platform: 900 tỷ VNĐ\n4. Tư vấn & Triển khai: 540 tỷ VNĐ"},
            ],
            expected_keywords=["AI Platform", "66", "67"],
        ),
        TestCase(
            id="HIST-02",
            category="history",
            question="Giải thích chi tiết hơn về điểm đầu tiên",
            language="vi",
            history=[
                {"role": "user", "content": "DeepSeek-V3.2 có những đặc điểm kỹ thuật nào nổi bật?"},
                {"role": "assistant", "content": "DeepSeek-V3.2 có 3 đặc điểm kỹ thuật nổi bật:\n1. DeepSeek Sparse Attention (DSA) - cơ chế attention hiệu quả\n2. Scalable RL framework - mở rộng tính toán post-training\n3. Agentic Task Synthesis - pipeline tạo dữ liệu cho agent"},
            ],
            expected_keywords=["DSA", "Sparse Attention", "lightning", "indexer"],
        ),
        # ── Citation Quality ──
        TestCase(
            id="CITE-01",
            category="citation",
            question="TechVina thực hiện thương vụ M&A nào năm 2025 và giá trị bao nhiêu?",
            language="vi",
            expected_keywords=["DataStream", "Singapore", "45"],
        ),
    ]
    return cases


# ── Rule-based metrics (no LLM needed) ────────────────────────────────────

def eval_keyword_coverage(tc: TestCase) -> MetricResult:
    """Check if expected keywords appear in the answer."""
    if not tc.expected_keywords:
        return MetricResult("keyword_coverage", 1.0, True, "No keywords to check")

    found = 0
    missing = []
    for kw in tc.expected_keywords:
        if kw.lower() in tc.answer.lower():
            found += 1
        else:
            missing.append(kw)

    score = found / len(tc.expected_keywords) if tc.expected_keywords else 1.0
    passed = score >= 0.5  # At least half the keywords
    reason = f"{found}/{len(tc.expected_keywords)} keywords found"
    if missing:
        reason += f". Missing: {missing}"
    return MetricResult("keyword_coverage", score, passed, reason)


def eval_refusal_accuracy(tc: TestCase) -> MetricResult:
    """Check if the system correctly refused (or didn't refuse) to answer.

    Distinguishes between:
    - Full refusal: entire answer is a refusal (e.g., "Tài liệu không chứa thông tin này.")
    - Partial gap noting: answer provides data but notes some gaps (acceptable)
    """
    refusal_phrases = [
        "không chứa thông tin",
        "không có thông tin",
        "tài liệu không",
        "not contain",
        "no relevant information",
    ]
    answer_lower = tc.answer.lower()

    # Count refusal phrase occurrences
    refusal_hits = sum(1 for p in refusal_phrases if p in answer_lower)

    # Check if answer is MOSTLY a refusal (short + refusal phrase)
    word_count = len(tc.answer.split())
    is_full_refusal = refusal_hits > 0 and word_count < 20
    # Partial gap: answer has substance + notes some gaps
    is_partial_gap = refusal_hits > 0 and word_count >= 20

    if tc.expected_refuse:
        if refusal_hits > 0:
            return MetricResult("refusal_accuracy", 1.0, True, "Correctly refused")
        else:
            return MetricResult("refusal_accuracy", 0.0, False,
                                "Should have refused but answered")
    else:
        if is_full_refusal:
            return MetricResult("refusal_accuracy", 0.0, False,
                                "Over-refusal: entire answer is a refusal")
        elif is_partial_gap:
            # Answer provides some data but notes gaps — this is acceptable behavior
            return MetricResult("refusal_accuracy", 0.8, True,
                                "Partial answer with noted gaps (acceptable)")
        else:
            return MetricResult("refusal_accuracy", 1.0, True, "Correctly answered")


def eval_phantom_citations(tc: TestCase) -> MetricResult:
    """Check for phantom citations when refusing to answer.

    Only flags as phantom if:
    - The answer is a FULL refusal (short, no substantive content) AND has citations
    - OR a refusal sentence itself contains citations (e.g., "Không có thông tin [1]")

    Does NOT flag if the answer provides useful data with citations + notes some gaps.
    """
    refusal_phrases = ["không chứa", "không có thông tin", "not contain", "no information"]
    answer_lower = tc.answer.lower()
    word_count = len(tc.answer.split())

    # Full refusal with citations = phantom
    is_full_refusal = any(p in answer_lower for p in refusal_phrases) and word_count < 20
    all_citations = re.findall(r'\[(?:IMG-)?\d+\]', tc.answer)

    if is_full_refusal and all_citations:
        return MetricResult("no_phantom_citations", 0.0, False,
                            f"Phantom citations on full refusal: {all_citations}")

    # Check for citations IN refusal sentences specifically
    sentences = re.split(r'[.!?\n]', tc.answer)
    phantom_in_sentence = []
    for sent in sentences:
        sent_lower = sent.lower().strip()
        if any(p in sent_lower for p in refusal_phrases):
            sent_citations = re.findall(r'\[(?:IMG-)?\d+\]', sent)
            if sent_citations:
                phantom_in_sentence.extend(sent_citations)

    if phantom_in_sentence:
        return MetricResult("no_phantom_citations", 0.3, False,
                            f"Citations in refusal sentences: {phantom_in_sentence}")

    return MetricResult("no_phantom_citations", 1.0, True, "No phantom citations")


def eval_citation_format(tc: TestCase) -> MetricResult:
    """Check citation format: [1] [2] not [1, 2] or [1][2]."""
    # Check for grouped citations (bad: [1, 2] or [1,2])
    grouped = re.findall(r'\[\d+[,\s]+\d+\]', tc.answer)
    if grouped:
        return MetricResult("citation_format", 0.0, False,
                            f"Grouped citations found: {grouped}")
    return MetricResult("citation_format", 1.0, True, "Citations properly formatted")


def eval_token_artifacts(tc: TestCase) -> MetricResult:
    """Check for Gemini token artifacts like <unusedNNN>."""
    artifacts = re.findall(r'<unused\d+>:?\s*', tc.answer)
    if artifacts:
        return MetricResult("no_token_artifacts", 0.0, False,
                            f"Token artifacts: {artifacts}")
    return MetricResult("no_token_artifacts", 1.0, True, "No token artifacts")


def eval_language_match(tc: TestCase) -> MetricResult:
    """Check if answer language matches question language."""
    # Simple heuristic: Vietnamese has many diacritical marks
    vn_chars = set("áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ")
    vn_count = sum(1 for c in tc.answer.lower() if c in vn_chars)
    total_alpha = sum(1 for c in tc.answer if c.isalpha())

    if total_alpha == 0:
        return MetricResult("language_match", 1.0, True, "No text to check")

    vn_ratio = vn_count / total_alpha

    if tc.language == "vi":
        # Vietnamese question should get Vietnamese answer
        # Allow some English (technical terms), but at least 5% VN chars
        if vn_ratio > 0.03:
            return MetricResult("language_match", 1.0, True,
                                f"Vietnamese content detected ({vn_ratio:.1%})")
        else:
            return MetricResult("language_match", 0.0, False,
                                f"Expected Vietnamese but got mostly English ({vn_ratio:.1%})")
    else:
        return MetricResult("language_match", 1.0, True, "English response OK")


def eval_answer_completeness(tc: TestCase) -> MetricResult:
    """Check if answer has substance (not just a one-liner refusal for non-refusal cases)."""
    if tc.expected_refuse:
        return MetricResult("answer_completeness", 1.0, True, "Refusal case — skip")

    word_count = len(tc.answer.split())
    if word_count < 10:
        return MetricResult("answer_completeness", 0.2, False,
                            f"Answer too short ({word_count} words)")
    elif word_count < 30:
        return MetricResult("answer_completeness", 0.6, True,
                            f"Brief answer ({word_count} words)")
    else:
        return MetricResult("answer_completeness", 1.0, True,
                            f"Detailed answer ({word_count} words)")


def eval_context_utilization(tc: TestCase) -> MetricResult:
    """Check if retrieved contexts are actually being cited in the answer."""
    if tc.expected_refuse or tc.source_count == 0:
        return MetricResult("context_utilization", 1.0, True, "Skip — refusal or no sources")

    citations = re.findall(r'\[(\d+)\]', tc.answer)
    cited_indices = set(int(c) for c in citations)
    if not 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
