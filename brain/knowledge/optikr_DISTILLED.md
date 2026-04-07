---
id: optikr
type: knowledge
owner: OA_Triage
---
# optikr
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: readme.md
```md
# OptikR - Real-Time Screen Translation System (Vibecoded)

<div align="center">

**Translate anything on your screen in real-time**

Version preview-1.0.0 


</div>

---

## Project Motivation

This is a **proof of concept** and a **one-person community project**.

**Built by someone with minimal coding experience** — I can understand code but can't write it from scratch. This project proves that with the right tools, determination, and community support, anyone can create something meaningful.

**Why I Built This:**
- Make translation accessible to everyone
- No paywalls, no subscriptions, no limits
- Community-driven development
- Learn by doing (and sharing what I learned)
- Give back to the community that helped me

**What This Means:**
- This is a proof of concept — expect rough edges
- Bugs exist but will be fixed
- Extensive documentation to help you understand and improve it
- Community contributions are welcome and encouraged
- It works, and it works well for what it does

---

## What is OptikR?

### A Modular Framework

OptikR is not just a screen translator — it's a **modular framework built on extensibility and plugins**. This is a proof of concept demonstrating what's possible when you combine:

- **Stage-Based Pipeline Architecture** — Every processing stage (Capture, OCR, Translation, Overlay) is plugin-based
- **Universal Plugin System** — Everything can be enhanced, replaced, or extended
- **Built-In Plugin Generator** — CLI tool creates correctly structured plugins for any type
- **Zero Limits Philosophy** — The only limit is your hardware, not the software

### Built for Everyone

**Accessibility First:**
- **Custom UI Languages** — Import your own language translations via Sidebar > Language Packs
- **Highly Customizable** — Every setting is user-configurable
- **No Artificial Limits** — You control everything
- **Community-Driven** — Share plugins, dictionaries, and translations

### Everything is a Plugin

**You Can Add:**
- New OCR engines (Mokuro, Windows OCR, custom models)
- New capture methods (DirectX, Screenshot, custom implementations)
- New translation engines (local AI, cloud APIs, custom models)
- New optimizer plugins (frame skip, caching, preprocessing)
- New text processors (spell check, regex filters)

### DEMO Video

https://www.youtube.com/watch?v=7JkA0uPoAnE

**Plugin Generator Helps You:**

```bash
python run.py --create-plugin
```

Interactive CLI that generates the correct folder structure, `plugin.json`, entry script with template code, and a README for any plugin type. See [Plugins and Engines](docs/PLUGINS_AND_ENGINES.md) for full details.

### Real-Time Translation

OptikR provides a powerful real-time screen translation and OCR system. Whether you're reading manga, playing games, watching videos, or browsing the web, OptikR provides seamless translation with minimal performance impact.

### Key Features

- **Real-Time Translation** — High FPS with low latency
- **Multiple AI Engines** — EasyOCR, PaddleOCR, Tesseract, Mokuro, Surya, and more
- **Offline Capable** — Works without internet using local AI models (MarianMT, NLLB-200)
- **GPU Accelerated** — 3-6x faster with NVIDIA CUDA support
- **Smart Dictionary** — Personal translation database that learns over time
- **Context-Aware** — Presets for manga, games, videos, formal text, and more
- **100+ Languages** — Supports all major language pairs
- **50+ Plugins** — Highly extensible with optimizers, processors, and engines

---

## Quick Start

### Prerequisites

1. **Python 3.10 - 3-12** — Download from https://www.python.org/downloads/release/python-31210/
   - During installation, check **"Add Python to PATH"**
2. **CUDA Toolkit (optional, recommended for NVIDIA GPUs)** — Download from https://developer.nvidia.com/cuda-downloads
   - Install CUDA 12.x, then **restart your computer**
   - See [How To Run — CUDA section](docs/HOW_TO_RUN.md#cuda-toolkit--what-it-is-and-why-you-should-install-it) for details
3. **Visual C++ Redistributable (Windows)** — Download from https://aka.ms/vs/17/release/vc_redist.x64.exe

### Install and Run

```bash
cd OptikR
python run.py
```

That's it. On first launch, OptikR automatically:
1. Installs all dependencies from `requirements.txt`
2. Detects your GPU and installs the correct PyTorch build (CUDA or CPU)
3. Restarts itself once setup is complete

No manual `pip install` is required under normal conditions. If auto-install fails (network issues, permissions), see [How To Run](docs/HOW_TO_RUN.md) for manual installation steps.

Use the provided launcher scripts — they create an isolated virtual environment (`.venv`) and install all dependencies automatically on first run.

**Windows:**

```
start.bat
```

**Linux / macOS:**

```
chmod +x start.sh   # first time only
./start.sh
```

The launcher will:
1. Verify your Python version is 3.10–3.12.
2. Create a `.venv` virtual environment if one doesn't exist yet.
3. Run the application inside that environment (dependencies and PyTorch are installed automatically by the bootstrap process on first launch).
   - Linux launcher installs `requirements-linux.txt` when present.

### Why not `python run.py` directly?

Running `python run.py` uses your **system** Python interpreter and installs packages into your **global** site-packages. The launcher scripts ensure everything stays inside `.venv`, keeping your system Python clean.

If you prefer to manage the environment yourself, activate `.venv` first:

```
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

python run.py
```

## Removing Dependencies

Delete the `.venv` folder — that removes all installed packages. Run the launcher again to recreate a fresh environment.

## GPU Support

By default the bootstrap detects your GPU and installs the appropriate PyTorch build (CUDA or CPU-only). To manually install GPU dependencies:

```
pip install -r requirements-gpu.txt
```

For CPU-only:

```
pip install -r requirements-cpu.txt
```

### First Launch Setup

1. **Consent Dialog** — Accept the terms on first run
2. **Setup Wizard** — Guides you through initial configuration:
   - Select source and target languages
   - Choose OCR engine (EasyOCR recommended)
   - Choose translation engine (MarianMT for offline)
   - Download required AI models
3. **Start Translating**
   - Click "Select Region" to choose the area to translate
   - Click "Start" to begin real-time translation
   - Translations appear as overlays on your screen

### Troubleshooting Installation

| Problem | Solution |
|---------|----------|
| "Python not found" | Reinstall Python with "Add to PATH" checked |
| "CUDA not found" (NVIDIA GPU) | Restart computer after CUDA install |
| "DLL load failed" | Install Visual C++ Redistributable, restart |
| `pip install` fails | Run `python -m pip install --upgrade pip`, retry |

---

## Smart Dictionary

The Smart Dictionary is one of OptikR's most powerful features — a personal translation database that learns, grows, and can be shared.

### How It Works

```
First Time:
  OCR detects "Hello" → AI translates to "Hallo" → Dictionary saves it

Next Time:
  OCR detects "Hello" → Dictionary: "Hallo" (instant, no AI needed)
```

### Key Capabilities

- **Instant Lookup** — Skips AI translation entirely for known text
- **Per Language Pair** — Separate dictionary files (e.g., `en_de.json.gz`, `ja_en.json.gz`)
- **Full Control** — Browse, edit, delete entries in the Dictionary Editor
- **Import/Export** — Share dictionaries with the community (JSON format)
- **Word Extraction** — Optionally breaks sentences into individual words on stop
- **Statistics** — Track entries, lookups, hit rate, and most-used translations
- **Cleaning Tools** — Remove OCR errors and low-confidence entries

### Real Performance Impact

| Scenario | Without Dictionary | With Dictionary (after learning) |
|----------|-------------------|----------------------------------|
| Manga reading | AI processing every frame | 60-80% hit rate, instant lookups |
| Game UI | AI processing every frame | 70-90% hit rate (UI is repetitive) |
| Video subtitles | AI processing every frame | 50-70% hit rate |

### Community Sharing

Export your dictionary from the Smart Dictionary tab and share the JSON file. Others can import it to get instant access to thousands of pre-translated terms. Great for manga communities, game localization groups, and language learners.

---

## Settings Overview

### General
- Interface language (English, German, French, Italian, Japanese)
- Source and target languages
- Runtime mode (Auto, GPU, CPU)
- Startup options

### Capture
- Capture method (DirectX, Screenshot, Auto-detect)
- Frame rate (5–120 FPS)
- Capture quality (Low, Medium, High, Ultra)
- Multi-monitor and multi-region support
- Adaptive capture, fallback mode, small text enhancement

### OCR
- Engine selection (EasyOCR, PaddleOCR, Tesseract, Mokuro, and more)
- Language packs
- Confidence threshold
- Intelligent preprocessing (two-pass OCR)

### Translation
- Local engines: MarianMT, NLLB-200, Qwen3
- Cloud engines: Google Translate, DeepL, Azure, LibreTranslate
- Quality settings, fallback translation, batch processing

### Overlay
- Font family and size
- Text/background/border colors
- Transparency and positioning strategy (Simple, Smart, Flow-Based)
- Animation (Fade, Slide, Scale, None)
- Seamless background mode (auto-matches overlay to original background)

### Pipeline Management
- Pipeline status and statistics
- Active plugin toggles
- Context presets (Manga, Game UI, Subtitles, Novel, Technical, Wikipedia)
- Sequential vs Async pipeline mode
- Plugin-by-stage browser

### Storage
- Translation cache management
- Learning dictionary management
- Export options (translations, screenshots, logs)

### Advanced
- Log level and output
- Thread pool size and process priority
- Developer/debug options

---

## Context Plugin

The Context Plugin adapts OCR, text validation, and translation behavior based on your content type. Provides 10-30% accuracy improvement.

### Available Presets

| Preset | OCR Behavior | Translation Style |
|--------|-------------|-------------------|
| Wikipedia/Formal | High confidence, proper caps | Formal, precise |
| Manga/Comics | ALL CAPS aware, speech bubbles | Casual, emotion-preserving |
| Game UI | Short phrases, buttons | Concise, action-oriented |
| Subtitles/Video | Line break aware | Natural speech |
| Novel/Book | Paragraph-aware | Literary, descriptive |
| Technical Doc | Code/term aware | Precise, technical |

Custom tags can further refine context: `action`, `comedy`, `sci-fi`, `dialogue-heavy`, `technical`.

---

## Pipeline Architecture

### Sequential Pipeline (Default)

Each stage completes before the next starts. Simple, stable, low memory.

```
Frame 1: CAPTURE → OCR → TRANSLATE → POSITION → OVERLAY
Then Frame 2 starts...
```

**Best for:** Most users, lower-end systems, debugging.

### Async Pipeline (Advanced)

Stages run in parallel on different frames simultaneously. Higher throughput.

```
Time 0ms:   Frame 1: CAPTURE
Time 8ms:   Frame 1: OCR        | Frame 2: CAPTURE
Time 16ms:  Frame 1: OCR        | Frame 2: OCR       | Frame 3: CAPTURE
Time 58ms:  Frame 1: TRANSLATE  | Frame 2: OCR       | Frame 3: OCR
Time 88ms:  Frame 1: OVERLAY ✓  | Frame 2: TRANSLATE | Frame 3: OCR
```

**Best for:** Quad-core+ CPUs, 8 GB+ RAM, users who need 30+ FPS.

### Comparison

| Metric | Sequential | Async |
|--------|-----------|-------|
| Throughput | ~10 FPS | ~50 FPS |
| CPU Usage | Medium | High |
| Memory | ~2 GB | ~3-4 GB |
| Stability | Very High | High |
| Recommended | Most users | Power users |

Switch in Pipeline Management > Overview > "Async Pipeline" toggle.

---

## Performance Optimization

### Essential Plugins (Always Active)

| Plugin | Benefit |
|--------|---------|
| Frame Skip | 50-70% CPU reduction — skips unchanged frames |
| Translation Cache | Instant lookup for repeated text |
| Smart Dictionary | Learns translations permanently |
| Text Validator | Filters garbage text, 30-50% noise reduction |
| Text Block Merger | Merges fragmented OCR text |

### Optional Plugins

| Plugin | Benefit |
|--------|---------|
| Async Pipeline | 50-80% throughput boost |
| Batch Processing | 30-50% faster processing |
| Parallel OCR/Capture | 2-3x faster for multi-region |
| Priority Queue | Better interactive responsiveness |
| Work-Stealing Pool | Load balancing across threads |
| Motion Tracker | Skips OCR during scrolling |
| Spell Corrector | Fixes OCR errors |

### Performance Metrics

| Configuration | Frame Time | FPS | CPU Usage |
|--------------|-----------|-----|-----------|
| No optimizations | ~94ms | ~10 | High |
| Essential plugins | ~30-40ms | ~25-33 | Medium |
| All optimizations | ~10-20ms | ~50-100 | Low |

---

## Application Structure

```
OptikR/
├── run.py                     # Entry point
├── bootstrap.py               # Auto-setup (dependencies, PyTorch, config)
├── requirements.txt           # Core dependencies
├── requirements-cpu.txt       # PyTorch CPU variant
├── requirements-gpu.txt       # PyTorch CUDA variant
├── app/                       # Application logic
│   ├── core/                  # Config, main window, model catalog
│   ├── ocr/                   # OCR plugin management
│   ├── text_translation/      # Translation layer
│   ├── workflow/              # Pipeline, plugin manager, plugin generator
│   ├── benchmark/             # Benchmark runner
│   ├── localization/          # UI translations (en, de, fr, it, ja)
│   ├── styles/                # QSS stylesheets (dark/light)
│   └── utils/                 # Path utils, PyTorch manager, CUDA utils
├── ui/                        # User interface (PyQt6)
│   ├── settings/              # Settings tabs
│   ├── dialogs/               # Dialogs (first-run wizard, benchmark, help)
│   ├── overlays/              # Translation overlay rendering
│   └── layout/                # Sidebar, toolbar
├── plugins/                   # Plugin system
│   ├── stages/                # Core pipeline stages
│   │   ├── capture/           # Screen capture plugins
│   │   ├── ocr/               # OCR engine plugins
│   │   ├── translation/       # Translation engine plugins
│   │   ├── vision/            # Vision-language model plugins
│   │   └── llm/               # LLM plugins
│   └── enhancers/             # Pipeline enhancers
│       ├── optimizers/        # Performance optimizer plugins
│       ├── text_processors/   # Text processing plugins
│       └── audio_translation/ # Audio translation plugin
├── user_data/                 # User-owned runtime data
│   ├── config/                # user_config.json
│   ├── learned/translations/  # Smart Dictionary files
│   ├── exports/               # Exported translations, screenshots, logs
│   ├── custom_plugins/        # User-installed plugins
│   └── backups/               # Config backups
└── system_data/               # System-managed runtime data
    
... [TRUNCATED]
```

### File: requirements.txt
```txt
# OptikR Requirements
# Install: pip install -r requirements.txt
# Python 3.10+ compatible

# ============================================================================
# GUI Framework
# ============================================================================
PyQt6>=6.5.0
PyQt6-Qt6>=6.5.0
PyQt6-sip>=13.5.0

# ============================================================================
# Deep Learning & AI
# ============================================================================
# NOTE: PyTorch is installed separately based on your hardware
# For manual installation:
# - CPU only: pip install -r requirements-cpu.txt
# - GPU (CUDA 12.4): pip install -r requirements-gpu.txt

# ============================================================================
# OCR Engines
# ============================================================================
easyocr>=1.7.0
paddleocr>=2.7.0
manga-ocr>=0.1.11
pytesseract>=0.3.10
rapidocr-onnxruntime>=1.3.0  # Optional: Lightweight PaddleOCR via ONNX Runtime
python-doctr[torch]>=0.8.0  # Optional: Transformer-based OCR (Mindee DocTR)
surya-ocr>=0.4.0,<=0.13.1  # Optional: Vision-transformer OCR (90+ languages) — pinned: 0.14+ requires torch>=2.7 (no CUDA 12.4 wheels)
# mokuro — installed automatically by the plugin system with --no-deps
# to avoid overwriting CUDA torch.  Manual install:
#   pip install mokuro --no-deps
#   pip install fire loguru natsort pyclipper shapely torchsummary yattag
# mokuro>=0.2.1

# ============================================================================
# Vision Mode (Qwen3-VL)
# ============================================================================
# qwen-vl-utils — installed with --no-deps to avoid pulling in packages
# that could overwrite CUDA torch.  Manual install:
#   pip install qwen-vl-utils --no-deps
#   pip install av
# qwen-vl-utils>=0.0.14

# ============================================================================
# Translation
# ============================================================================
transformers>=4.57.0,<5.0.0
sentencepiece>=0.1.99  # Required by transformers/MarianMT
huggingface-hub>=0.23.0  # Required by transformers
# accelerate — installed automatically by the plugin system with --no-deps
# to avoid overwriting CUDA torch.  Manual install:
#   pip install accelerate --no-deps
#   pip install pyyaml safetensors
# accelerate>=0.26.0

# ============================================================================
# Image Processing
# ============================================================================
opencv-python>=4.8.0
Pillow>=10.0.0
numpy>=1.24.0
scipy>=1.11.0
scikit-image>=0.21.0

# ============================================================================
# Screen Capture
# ============================================================================
mss>=9.0.1

# ============================================================================
# Package Management
# ============================================================================
packaging>=21.0

# ============================================================================
# System Utilities
# ============================================================================
psutil>=5.9.0
pystray>=0.19.0
py-cpuinfo>=9.0.0

# ============================================================================
# Networking
# ============================================================================
requests>=2.31.0
urllib3>=2.0.0  # Required by requests

# ============================================================================
# Security
# ============================================================================
cryptography>=42.0.0

# ============================================================================
# Translation Services
# ============================================================================
deep-translator>=1.11.0
deepl>=1.16.0
google-cloud-translate>=3.12.0  # Optional: Google Cloud Translation API (premium)

# ============================================================================
# Text Processing
# ============================================================================
textdistance>=4.5.0
pyspellchecker>=0.7.2  # Optional: Used by spell checker plugin

# ============================================================================
# Performance Monitoring
# ============================================================================
nvidia-ml-py>=12.0.0  # Optional: NVIDIA GPU monitoring

# ============================================================================
# GPU Acceleration (Optional - Uncomment if needed)
# ============================================================================
# cupy>=12.0.0  # CUDA-accelerated NumPy
# pyopencl>=2023.1  # OpenCL support
# numba>=0.57.0  # JIT compiler

# ============================================================================
# Audio Translation Plugin (Optional)
# ============================================================================
# Audio deps live in a separate file to manage torch conflicts safely:
#   pip install -r requirements-audio.txt
#   pip install openai-whisper --no-deps
# See requirements-audio.txt for full instructions.

```

### File: bootstrap.py
```py
"""
OptikR — Bootstrap module.

Runs all environment setup that must happen before the application starts:
  1. EXE stdout/stderr fix
  2. Warning suppression & environment variables
  3. Logging configuration
  4. sys.path setup
  5. PyTorch auto-installation (may restart process)
  6. Application directory creation
  7. Config manager initialization
  8. Installation info / CUDA path loading

After this module is imported, the following are available:
  - bootstrap.logger          — pre-configured logger for optikr
  - bootstrap.config_manager  — SimpleConfigManager instance (ready to use)
  - bootstrap.INSTALLATION_INFO — hardware/CUDA detection dict
"""

import sys
import os
import warnings
import re
import shutil
import site
from pathlib import Path

# ============================================================================
# EXE FIX: Redirect stdout/stderr for windowed applications
# ============================================================================
# When running as a windowed EXE (console=False), sys.stdout and sys.stderr
# are None, which causes crashes when code tries to use print() or flush().
if getattr(sys, 'frozen', False):
    _devnull_handles = []
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w', encoding='utf-8', errors='ignore')
        _devnull_handles.append(sys.stdout)
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w', encoding='utf-8', errors='ignore')
        _devnull_handles.append(sys.stderr)
    if _devnull_handles:
        import atexit

        def _close_devnull():
            for h in _devnull_handles:
                try:
                    h.close()
                except Exception:
                    pass

        atexit.register(_close_devnull)
# ============================================================================

# Suppress common warnings for cleaner console output
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning, module='paddle')
warnings.filterwarnings('ignore', category=UserWarning, module='transformers')
warnings.filterwarnings('ignore', message='.*resume_download.*')
warnings.filterwarnings('ignore', message='.*torch.load.*')
warnings.filterwarnings('ignore', message='.*_pytree.*')

# Suppress paddle verbose output
os.environ['GLOG_minloglevel'] = '3'
os.environ['FLAGS_pir_apply_shape_optimization_pass'] = '0'
os.environ['PPOCR_SHOW_LOG'] = '0'
os.environ['PADDLEOCR_VERBOSE'] = '0'

# Suppress Qt DPI awareness warning on Windows (harmless — already set by another component)
os.environ.setdefault('QT_LOGGING_RULES', 'qt.qpa.window=false')

import logging

# Configure logging to suppress verbose library output
logging.getLogger('mokuro').setLevel(logging.CRITICAL)
logging.getLogger('transformers').setLevel(logging.CRITICAL)
logging.getLogger('huggingface_hub').setLevel(logging.CRITICAL)
logging.getLogger('paddleocr').setLevel(logging.CRITICAL)

# Suppress root logger warnings
logging.getLogger().setLevel(logging.ERROR)

# Logging format constants
_STANDARD_FORMAT = '[%(levelname)s] [%(asctime)s] [%(name)s] [%(threadName)s] %(message)s'
_STANDARD_DATEFMT = '%H:%M:%S'
_DEBUG_FORMAT = (
    '[%(levelname)s] [%(asctime)s.%(msecs)03d] '
    '[%(name)s:%(funcName)s:%(lineno)d] [%(threadName)s] %(message)s'
)

# Module logger — shared across bootstrap and run.py
logger = logging.getLogger('optikr')
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter(_STANDARD_FORMAT, datefmt=_STANDARD_DATEFMT))
    logger.addHandler(_handler)
    logger.propagate = False

from app.utils.credential_filter import CredentialLoggingFilter
logger.addFilter(CredentialLoggingFilter())

# Add root directory to Python path for imports
_current_dir = Path(__file__).parent
if str(_current_dir) not in sys.path:
    sys.path.insert(0, str(_current_dir))


# ============================================================================
# PYTORCH AUTO-INSTALLATION
# Delegates detection/install to PyTorchManager — restart logic stays here
# because it happens before the app event loop exists.
# ============================================================================
def _check_and_install_pytorch():
    """Check if PyTorch is installed. If not, auto-install via PyTorchManager.

    On first run without PyTorch: detects GPU, installs matching variant,
    then restarts the process.

    Returns:
        tuple: (success, is_gpu, message)
    """
    from app.utils.pytorch_manager import PyTorchManager, PyTorchVersion

    mgr = PyTorchManager()
    info = mgr.get_pytorch_info()

    def _get_missing_core_deps():
        """Return missing packages required to launch the GUI."""
        import importlib.util
        required = ("PyQt6", "packaging")
        return [pkg for pkg in required if importlib.util.find_spec(pkg) is None]

    missing_core = _get_missing_core_deps()

    if info['installed'] and not missing_core:
        version = info['version']
        is_gpu = info['cuda_available']
        if is_gpu and info.get('devices'):
            gpu_name = info['devices'][0]['name']
            logger.info("PyTorch %s detected with GPU: %s", version, gpu_name)
        else:
            logger.info("PyTorch %s detected (CPU mode)", version)
        return True, is_gpu, f"PyTorch {version} ready"
    elif info['installed'] and missing_core:
        logger.warning(
            "PyTorch is installed, but core dependencies are missing: %s. "
            "Running requirements install to repair environment.",
            ", ".join(missing_core),
        )

    # PyTorch not installed — first-run auto-install
    import subprocess

    _req_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')

    cuda_info = mgr.check_cuda_toolkit()
    use_cuda = cuda_info['installed'] or cuda_info['driver_version'] is not None
    force_cpu = os.environ.get("OPTIKR_FORCE_CPU_TORCH", "").strip().lower() in {
        "1", "true", "yes", "on",
    }
    if force_cpu:
        use_cuda = False
        logger.info("OPTIKR_FORCE_CPU_TORCH is enabled — forcing CPU PyTorch install path")

    variant = "CUDA" if use_cuda else "CPU"
    logger.info("=" * 60)
    logger.info("FIRST RUN: Setting up OptikR (%s)...", variant)
    logger.info("This is a one-time setup and may take a few minutes.")
    logger.info("=" * 60)

    def _normalize_pkg_name(name):
        return re.sub(r"[-_.]+", "-", name.strip().lower())

    def _extract_req_name(req_line):
        """Parse package name from a requirements line."""
        line = req_line.strip()
        if not line or line.startswith('#'):
            return None
        if line.startswith(('-r', '--requirement', '-e', '--editable', '--index-url',
                           '--extra-index-url', '--find-links', '--trusted-host',
                           '--constraint', '-c')):
            return None
        if ' #' in line:
            line = line.split(' #', 1)[0].strip()
        # Keep only the package token before version/extras/markers.
        token = re.split(r'[<>=!~;\[\s]', line, maxsplit=1)[0].strip()
        if not token or token.startswith(('.', '/', '\\')) or '://' in token:
            return None
        return _normalize_pkg_name(token)

    def _extract_pkg_from_pip_line(pip_line):
        """Extract package name from common pip output lines."""
        text = pip_line.strip()
        if text.startswith("Collecting "):
            pkg = text[len("Collecting "):].split()[0]
            return _normalize_pkg_name(pkg)
        if text.startswith("Requirement already satisfied: "):
            pkg = text[len("Requirement already satisfied: "):].split()[0]
            return _normalize_pkg_name(pkg)
        if text.startswith("Processing "):
            pkg = Path(text[len("Processing "):].split()[0]).stem.split('-')[0]
            return _normalize_pkg_name(pkg)
        return None

    def _cleanup_stale_torch_artifacts():
        """Remove broken pip leftovers like '~orch*' in site-packages."""
        try:
            candidates = set()
            for sp in getattr(site, "getsitepackages", lambda: [])() or []:
                if sp:
                    candidates.add(Path(sp))
            user_site = getattr(site, "getusersitepackages", lambda: "")()
            if user_site:
                candidates.add(Path(user_site))

            stale_prefixes = ("~orch", "~unctorch")
            removed = 0
            for sp in candidates:
                if not sp.exists() or not sp.is_dir():
                    continue
                for entry in sp.iterdir():
                    name = entry.name.lower()
                    if not name.startswith(stale_prefixes):
                        continue
                    try:
                        if entry.is_dir():
                            shutil.rmtree(entry, ignore_errors=False)
                        else:
                            entry.unlink(missing_ok=True)
                        removed += 1
                        logger.warning("Removed stale package artifact: %s", entry)
                    except Exception as e:
                        logger.warning("Could not remove stale artifact %s: %s", entry, e)
            if removed:
                logger.info("Cleaned %d stale torch artifact(s) before install", removed)
        except Exception as e:
            logger.debug("Stale artifact cleanup skipped: %s", e)

    def _restart_current_process():
        """Restart the current script with robust Windows path handling."""
        argv = [sys.executable]
        if sys.argv:
            argv.extend(sys.argv)
        try:
            # subprocess handles quoting on Windows better than os.execv when
            # executable paths/usernames contain spaces.
            import subprocess as _subprocess
            _subprocess.Popen(argv, close_fds=True)
            os._exit(0)
        except Exception as restart_error:
            logger.error("Failed to restart automatically: %s", restart_error)
            return False

    try:
        _cleanup_stale_torch_artifacts()

        # Step 1: Install all requirements from requirements.txt
        if os.path.exists(_req_file):
            direct_reqs = []
            with open(_req_file, 'r', encoding='utf-8') as req_handle:
                for line in req_handle:
                    parsed = _extract_req_name(line)
                    if parsed:
                        direct_reqs.append(parsed)
            direct_req_set = set(direct_reqs)
            total_direct = len(direct_req_set)
            logger.info(
                "Step 1/2: Installing dependencies from requirements.txt (%d direct deps)...",
                total_direct,
            )

            req_cmd = [
                sys.executable, '-m', 'pip', 'install', '-r', _req_file,
                '--disable-pip-version-check', '--progress-bar', 'off',
            ]
            req_proc = subprocess.Popen(
                req_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )

            completed_direct = set()
            last_remaining = total_direct
            assert req_proc.stdout is not None
            for raw_line in req_proc.stdout:
                line = raw_line.rstrip()
                if not line:
                    continue
                pkg_name = _extract_pkg_from_pip_line(line)
                if pkg_name:
                    if pkg_name in direct_req_set:
                        completed_direct.add(pkg_name)
                        remaining = total_direct - len(completed_direct)
                        if remaining != last_remaining:
                            logger.info(
                                "Dependency progress: %d/%d direct deps checked (remaining: %d)",
                                len(completed_direct), total_direct, remaining,
                            )
                            last_remaining = remaining
                logger.info("[pip] %s", line)

            # Do not force a hard timeout by default: first-run installs can
            # legitimately take >10 minutes on slower machines/networks.
            # Optional override: set OPTIKR_PIP_INSTALL_TIMEOUT (seconds).
            timeout_raw = os.environ.get("OPTIKR_PIP_INSTALL_TIMEOUT", "").strip()
            timeout_seconds = int(timeout_raw) if timeout_raw.isdigit() else 0
            if timeout_seconds > 0:
                req_proc.wait(timeout=timeout_seconds)
            else:
                req_proc.wait()
            if req_proc.returncode != 0:
                logger.warning(
                    "Some dependencies may have failed (exit code %s). "
                    "Direct deps checked: %d/%d, remaining: %d",
                    req_proc.returncode,
                    len(completed_direct),
                    total_direct,
                    max(total_direct - len(completed_direct), 0),
                )
            else:
                logger.info(
                    "Dependencies installed successfully. Direct deps checked: %d/%d.",
                    len(completed_direct),
                    total_direct,
                )
        else:
            logger.warning("requirements.txt not found, skipping dependency install.")

        # Re-check PyTorch after requirements install.
        # On some systems, torch may already be pulled in as a transitive
        # dependency (e.g. easyocr). Re-installing in the same process can
        # trigger WinError 32 file-lock issues on Windows.
        post_req_info = mgr.get_pytorch_info()
        if post_req_info.get('installed'):
            post_version = post_req_info.get('version', 'unknown')
            post_cuda = bool(post_req_info.get('cuda_available'))
            if force_cpu:
                # In forced CPU mode, keep only CPU builds and do not accept
                # CUDA-tagged wheels that may have been pulled transitively.
                if "+cu" not in post_version and not post_cuda:
                    logger.info(
                        "PyTorch %s already available after Step 1 in CPU mode; "
                        "skipping Step 2 installation.",
                        post_version,
                    )
                    return True, False, f"PyTorch {post_version} ready"
                logger.warning(
                    "Force-CPU mode detected a CUDA-tagged torch build (%s). "
                    "Reinstalling CPU wheel in Step 2.",
                    post_version,
                )
            elif not use_cuda or post_cuda:
                logger.info(
                    "PyTorch %s already available after Step 1 (cuda=%s); "
                    "skipping Step 2 installation.",
                    post_version, post_cuda,
                )
                return True, post_cuda
... [TRUNCATED]
```

### File: requirements-audio.txt
```txt
# OptikR Requirements — Audio Translation
# Install: pip install -r requirements-audio.txt
#
# These are the dependencies for real-time audio translation, speech-to-text
# (Whisper), text-to-speech, push-to-talk, and game voice chat integration.
#
# ============================================================================
# IMPORTANT — Install order to protect your CUDA PyTorch build:
#
#   1. Base deps:    pip install -r requirements.txt
#   2. PyTorch:      pip install -r requirements-gpu.txt  (or requirements-cpu.txt)
#   3. Audio deps:   pip install -r requirements-audio.txt
#   4. Whisper:      pip install openai-whisper --no-deps
#   5. (Optional)    pip install coqui-tts  (torch no longer bundled since 0.27.4)
#
#   Step 4 MUST use --no-deps because openai-whisper declares torch as a
#   dependency; pip would otherwise pull a CPU-only torch wheel from PyPI and
#   silently overwrite your CUDA build.
#
#   The first-run setup wizard handles all of this automatically when you
#   enable the "Audio Translation" option.
# ============================================================================

# ============================================================================
# Audio Capture & Playback
# ============================================================================
pyaudio>=0.2.13         # Microphone input / speaker output via PortAudio
pyttsx3>=2.90           # Offline system TTS (lightweight fallback)

# ============================================================================
# Voice Activity Detection
# ============================================================================
webrtcvad>=2.0.10       # WebRTC-based voice activity detection

# ============================================================================
# Whisper Sub-Dependencies (safe — no torch dependency)
#
# These support openai-whisper which is installed separately with --no-deps.
# numpy, tqdm, and numba are omitted because they are already satisfied by
# the base requirements.txt or are already present as transitive deps.
# ============================================================================
more-itertools          # Required by openai-whisper
tiktoken>=0.3.3         # Required by openai-whisper (BPE tokenizer)
numba>=0.57.0           # Required by openai-whisper (word-level timestamps)

# ============================================================================
# Game Voice Chat / Push-to-Talk
# ============================================================================
pynput>=1.7.6           # Global hotkey listener for push-to-talk
pycaw>=20230407         # Windows Audio Session API (process enumeration, volume)
comtypes>=1.3.0         # COM interop for per-process WASAPI loopback (Windows)

# ============================================================================
# Torch-Dependent Packages — NOT installed by this file
#
# Install these AFTER PyTorch, using --no-deps for Whisper:
#
#   pip install openai-whisper --no-deps
#   pip install coqui-tts                  (optional, better-quality neural TTS)
#
# openai-whisper declares torch as a dependency so --no-deps is required.
# coqui-tts >= 0.27.4 no longer bundles torch, so it is safe to install
# normally — but verify your torch version is not overwritten afterwards.
#
# Both packages also require ffmpeg to be installed on your system:
#   Windows: winget install ffmpeg  (or download from https://ffmpeg.org)
#   Linux:   sudo apt install ffmpeg
# ============================================================================

```

### File: requirements-cpu.txt
```txt
# OptikR Requirements - CPU PyTorch Variant
# Use with core deps:
#   pip install -r requirements-cpu.txt
#   pip install -r requirements.txt
#
# Force CPU wheels from PyTorch index so Linux CPU installs do not
# download CUDA-enabled torch builds and NVIDIA runtime packages.
--index-url https://download.pytorch.org/whl/cpu
torch>=2.0.0
torchvision>=0.15.0
torchaudio>=2.0.0

```

### File: requirements-gpu.txt
```txt
# OptikR Requirements - GPU Version
# Install standalone: pip install -r requirements-gpu.txt
# Or with core deps: pip install -r requirements.txt && pip install -r requirements-gpu.txt
# Requires: NVIDIA GPU with CUDA 12.4 or compatible
# Python 3.10+ compatible

# ============================================================================
# PyTorch with CUDA support
# ============================================================================
# Using --extra-index-url so PyPI remains available for other packages
# This allows standalone installation without breaking non-PyTorch deps
--extra-index-url https://download.pytorch.org/whl/cu124
torch>=2.0.0
torchvision>=0.15.0
torchaudio>=2.0.0

```

### File: requirements-linux.txt
```txt
# Linux-specific optional dependencies for capture/runtime compatibility.
# Core dependencies remain in requirements.txt.
#
# Keep this file minimal to avoid forcing desktop-stack assumptions.
# Add packages here only when they are truly Linux-specific.

```

### File: requirements-windows.txt
```txt
# ============================================================================
# Windows-specific
# ============================================================================
pywin32>=306
winocr>=0.0.6  # Optional: Windows OCR (wraps Windows.Media.Ocr / DirectML)
bettercam>=1.0.0  # GPU-accelerated capture (AMD/NVIDIA, Desktop Duplication API)

```

### File: run.py
```py
"""
OptikR — Application entry point.

Supports both GUI mode and headless CLI mode. Qt is imported lazily so
headless commands can run without UI dependencies.
"""

import os
import sys
import atexit
import signal
import platform
import threading
import argparse
from pathlib import Path
from datetime import datetime

HEADLESS_EXAMPLES = """Examples:
  python run.py --headless-run --mode continuous --full-screen --monitor-index 0 --capture-method screenshot --ocr-engine tesseract --translation-engine google_free
  python run.py --headless-run --mode single-shot --region 0,0,1280,720 --monitor-index 0 --ocr-engine easyocr --translation-engine marianmt_gpu
  python run.py --headless-run --mode continuous --region 100,80,1600,900 --plugin-enable context_manager --plugin-disable motion_tracker
  python run.py --headless-run --dry-run --full-screen --set pipeline.mode=text --set capture.fps=15
"""


# ============================================================================
# Crash logger
# ============================================================================

def _import_bootstrap():
    """Import bootstrap lazily and return (logger, config_manager)."""
    from bootstrap import logger, config_manager
    return logger, config_manager


def _install_crash_logger(logger):
    """Install a global exception hook that logs unhandled crashes to system_data/logs/."""
    from app.utils.path_utils import ensure_dir
    import traceback as _tb

    crash_log_dir = ensure_dir('logs')
    _original_hook = sys.excepthook

    def _crash_hook(exc_type, exc_value, exc_traceback):
        if exc_type is KeyboardInterrupt:
            _original_hook(exc_type, exc_value, exc_traceback)
            return
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            crash_file = crash_log_dir / f'crash_{timestamp}.log'
            with open(crash_file, 'w', encoding='utf-8') as f:
                f.write(f"OptikR Crash Report — {datetime.now().isoformat()}\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Exception: {exc_type.__name__}: {exc_value}\n\n")
                f.write("Traceback:\n")
                _tb.print_exception(exc_type, exc_value, exc_traceback, file=f)
                f.write(f"\nPython: {sys.version}\n")
                f.write(f"Platform: {platform.platform()}\n")
            logger.critical("Crash log saved to: %s", crash_file)
        except Exception:
            pass  # Last resort — don't mask the original crash
        _original_hook(exc_type, exc_value, exc_traceback)

    sys.excepthook = _crash_hook

    # Also catch unhandled thread exceptions (Python 3.10+)
    if hasattr(threading, 'excepthook'):
        _original_thread_hook = threading.excepthook

        def _thread_crash_hook(args):
            _crash_hook(args.exc_type, args.exc_value, args.exc_traceback)
            _original_thread_hook(args)

        threading.excepthook = _thread_crash_hook


# ============================================================================
# Main application
# ============================================================================

def _run_gui() -> int:
    """Launch the OptikR application."""
    logger, config_manager = _import_bootstrap()
    from PyQt6.QtWidgets import QApplication

    logger.info("")
    logger.info("=" * 60)
    logger.info("OPTIKR")
    logger.info("=" * 60)
    logger.info("Starting application...")
    logger.info("")

    _install_crash_logger(logger)

    app = QApplication(sys.argv)

    # Load UI language from config
    try:
        from app.localization import get_language_manager
        ui_lang = config_manager.get_setting('ui.language', 'en')
        language_manager = get_language_manager()
        language_manager.set_language(ui_lang)
        logger.info("UI language set to: %s", ui_lang)
    except Exception as e:
        logger.warning("Failed to load UI language: %s", e)

    # Load stylesheet (dark default, base fallback)
    stylesheet_path = Path(__file__).parent / "app" / "styles" / "dark.qss"
    if stylesheet_path.exists():
        with open(stylesheet_path, 'r', encoding='utf-8') as f:
            app.setStyleSheet(f.read())
        logger.info("Loaded dark mode stylesheet")
    else:
        stylesheet_path = Path(__file__).parent / "app" / "styles" / "base.qss"
        if stylesheet_path.exists():
            with open(stylesheet_path, 'r', encoding='utf-8') as f:
                app.setStyleSheet(f.read())
            logger.info("Loaded base stylesheet")
        else:
            logger.warning("No stylesheet found")
            return 1

    # Check for user consent
    from ui.dialogs.consent_dialog import check_user_consent, show_consent_dialog

    consent_result = None
    if not check_user_consent(config_manager):
        logger.info("FIRST TIME LAUNCH - USER CONSENT REQUIRED")
        consent_result = show_consent_dialog(parent=None, config_manager=config_manager)
        if not consent_result:
            logger.info("User declined consent. Exiting application.")
            return 0
        logger.info("User consent obtained. Continuing...")

    # Check for first-run setup
    from ui.dialogs.first_run import FirstRunWizard, show_first_run_wizard

    show_wizard = config_manager.get_setting('startup.show_setup_wizard', True)
    force_setup_wizard = isinstance(consent_result, dict) and consent_result.get('mode') == 'online'
    if force_setup_wizard or (show_wizard and not FirstRunWizard.is_setup_complete()):
        logger.info("First run detected — launching setup wizard")
        wizard_result = show_first_run_wizard(
            config_manager=config_manager,
            force=force_setup_wizard,
        )
        if not wizard_result:
            logger.warning("Setup wizard was cancelled or failed")
            logger.info("You can re-run the wizard from Settings later")
    else:
        logger.info("First-run setup already completed, skipping wizard")

    # Show loading overlay
    from ui.common.widgets.loading_overlay import LoadingOverlay
    splash = LoadingOverlay()
    splash.show()
    splash.set_progress(10, "Initializing...")
    QApplication.processEvents()

    splash.set_progress(30, "Loading configuration...")

    # Periodic cache clear (runs only when enabled in config and retention elapsed)
    try:
        from app.utils.periodic_cache_cleaner import run_periodic_clear
        run_periodic_clear(config_manager)
    except Exception as e:
        logger.warning("Periodic cache clear failed: %s", e)

    # Create main window
    from app.core.main_window import MainWindow

    splash.set_progress(50, "Building UI...")
    window = MainWindow(config_manager=config_manager)

    # Register atexit and signal handlers for cleanup fallback (Bug 1.12)
    _cleanup_called = False

    def _cleanup_handler(*args):
        nonlocal _cleanup_called
        if not _cleanup_called:
            _cleanup_called = True
            try:
                window._cleanup_on_exit()
            except Exception:
                pass

    atexit.register(_cleanup_handler)
    signal.signal(signal.SIGTERM, lambda sig, frame: (_cleanup_handler(), sys.exit(0)))
    signal.signal(signal.SIGINT, lambda sig, frame: (_cleanup_handler(), sys.exit(0)))

    splash.set_progress(80, "Loading pipeline...")
    QApplication.processEvents()

    splash.set_progress(100, "Ready!")

    window.show()
    splash.finish_with_delay(window, delay_ms=600)

    logger.info("OptikR started successfully")
    logger.info("Ready for translation")

    return app.exec()


def _handle_plugin_generator_path(plugin_generator_path: str) -> int:
    """Generate plugin using the CLI plugin generator path."""
    from app.workflow.universal_plugin_generator import PluginGenerator

    plugin_path = Path(plugin_generator_path)
    if not plugin_path.exists():
        print(f"[ERROR] Plugin path does not exist: {plugin_path}")
        return 1

    print(f"[INFO] Generating plugin from: {plugin_path}")
    generator = PluginGenerator(output_dir="plugins")
    generator.run_interactive()
    return 0


def _handle_auto_generate_missing() -> int:
    """Auto-generate missing plugins by probing plugin managers."""
    from app.ocr.ocr_plugin_manager import OCRPluginManager
    from app.capture.capture_plugin_manager import CapturePluginManager
    from app.text_processors.text_processor_plugin_manager import TextProcessorPluginManager

    print("\n" + "=" * 60)
    print("AUTO-GENERATING MISSING PLUGINS")
    print("=" * 60)
    print("\nScanning for installed packages and generating plugins...\n")

    success_count = 0
    total_count = 0

    print("[1/3] Checking OCR plugins...")
    try:
        ocr_plugins = OCRPluginManager().discover_plugins()
        print(f"  ✓ Discovered {len(ocr_plugins)} OCR plugins")
        success_count += 1
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    total_count += 1

    print("[2/3] Checking Capture plugins...")
    try:
        capture_plugins = CapturePluginManager().discover_plugins()
        print(f"  ✓ Discovered {len(capture_plugins)} Capture plugins")
        success_count += 1
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    total_count += 1

    print("[3/3] Checking Text Processor plugins...")
    try:
        text_proc_plugins = TextProcessorPluginManager().discover_plugins()
        print(f"  ✓ Discovered {len(text_proc_plugins)} Text Processor plugins")
        success_count += 1
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    total_count += 1

    print("\n" + "=" * 60)
    print(f"COMPLETE: {success_count}/{total_count} plugin types processed")
    print("=" * 60 + "\n")

    return 0 if success_count == total_count else 1


def _handle_create_plugin() -> int:
    """Launch interactive plugin generator."""
    from app.workflow.universal_plugin_generator import PluginGenerator

    generator = PluginGenerator(output_dir="plugins")
    generator.run_interactive()
    return 0


def _handle_health_check() -> int:
    """Run comprehensive health checks in headless mode."""
    _, config_manager = _import_bootstrap()
    from app.utils.health_check import HealthCheck

    print("\n" + "=" * 60)
    print("SYSTEM HEALTH CHECK")
    print("=" * 60)
    print("\nRunning comprehensive system health check...\n")

    health_check = HealthCheck(config_manager)
    try:
        system_health = health_check.run_all_checks()

        print("=" * 60)
        print("HEALTH CHECK RESULTS")
        print("=" * 60)
        print()

        if system_health.is_healthy:
            print("✅ Overall Status: HEALTHY")
            print("All system components are functioning correctly.\n")
        else:
            print("⚠️  Overall Status: ISSUES DETECTED")
            print("Some components have issues that need attention.\n")

        print("Component Status:")
        print("-" * 60)

        for component_name, result in system_health.components.items():
            status_icon = "✅" if result.passed else "❌"
            print(f"{status_icon} {component_name.upper()}")
            print(f"   Status: {result.message}")
            if result.details:
                print(f"   Details: {result.details}")
            if not result.passed and result.remediation:
                print(f"   Remediation: {result.remediation}")
            print()

        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)

        failed_components = system_health.get_failed_components()
        if failed_components:
            print(f"Failed Components: {', '.join(failed_components)}")
        else:
            print("No issues detected. System is ready to use.")

        print("=" * 60 + "\n")
        return 0 if system_health.is_healthy else 1

    except Exception as e:
        print(f"\n[ERROR] Health check failed with exception: {e}")
        import traceback
        traceback.print_exc()
        return 1


def _print_examples() -> int:
    print(HEADLESS_EXAMPLES.rstrip())
    return 0


def _handle_headless_run(args: argparse.Namespace) -> int:
    logger, config_manager = _import_bootstrap()
    from app.core.headless_runner import run_headless

    result = run_headless(args=args, logger=logger, default_config_manager=config_manager)
    if result.exit_code == 0:
        logger.info(result.message)
    else:
        logger.error("%s", result.message)
    return result.exit_code


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='OptikR - OCR and Translation Tool',
        epilog=HEADLESS_EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--create-plugin', action='store_true',
                        help='Launch plugin generator (no UI)')
    parser.add_argument('--plugin-type', type=str,
                        choices=['capture', 'ocr', 'translation', 'optimizer', 'text_processor'],
                        help='Plugin type to generate')
    parser.add_argument('--plugin-generator', type=str, metavar='PATH',
                        help='Generate plugin from template at specified path (no UI)')
    parser.add_argument('--auto-generate-missing', action='store_true',
                        help='Auto-generate missing essential plugins (no UI)')
    parser.add_argument('--health-check', action='store_true',
                        help='Run system health check and display results')
    parser.add_argument('--examples', action='store_true',
                        help='Print headless examples and exit')
    parser.add_argument('--headless-run', action='store_true',
                        help='Run full translation pipeline in headless mode')
    parser.add_argument('--mode', choices=['continuous', 'single-shot'],
                        default='continuous',
                        help='Headless runtime mode (default: continuous)')
    parser.add_argument('--full-screen', action='store_true',
                        help='Use full-screen capture for the selected monitor')
    parser.add_argument('--region', type=str, metavar='X,Y,W,H',
                        help='Custom capture region (e.g. 0,0,1280,720)')
    parser.add_argument('--monitor-index', type=int, default=0,
                        help='Monitor index for full-screen or custom region (default: 0)')
    parser.add_argument('--capture-method', type=str,
                        help='Override capture.method for this run')
    parser.add_argument('--ocr-engine', type=str,
                        help='Override OCR engine for this run')
    parser.add_argument('--translation-engine', type=str,
                        help='Override translation engine for this run')
    parser.add_argument('--plugin-enable', action='append', default=[],
                        help='Enable plugin key (or key=value), repeatable')
    parser.add_argument('--plugin-disable', action
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
