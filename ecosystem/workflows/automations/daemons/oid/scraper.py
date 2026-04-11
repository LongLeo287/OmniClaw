"""
oid/scraper.py — OID Multi-Fallback Scraper
Owner: intake-chief-agent (Dept: Intake & Registry)
Role: Fetch raw content from multiple source types (URL, GitHub repo, local file).
      Uses progressive fallback strategies for 'hard to scrape' sources.

STRICT RULE: 100% English only. No other language in code, comments, or output.
"""

import os
import subprocess
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple

OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[4])
QUARANTINE_DIR = Path(OMNICLAW_ROOT) / "system" / "security" / "QUARANTINE"

# Git binary — resolved from PATH automatically
GIT_CMD = shutil.which("git") or "git"


def _log(msg: str):
    ts = datetime.now().strftime('%H:%M:%S')
    print(f"[{ts}] [intake-chief] {msg}")


def _safe_name(source: str) -> str:
    """Convert any source string into a safe filesystem-friendly name."""
    digest = hashlib.md5(source.encode()).hexdigest()[:8]
    slug = source.replace("https://", "").replace("http://", "")
    slug = "".join(c if c.isalnum() or c in "-_." else "_" for c in slug)[:60]
    return f"{slug}_{digest}"


# ── Strategy 1: git clone (shallow) ──────────────────────────────────────────

def _clone_shallow(url: str, dest: Path) -> bool:
    """Fast shallow clone. Works for most public repos."""
    try:
        result = subprocess.run(
            [GIT_CMD, "clone", "--depth=1", "--single-branch", url, str(dest)],
            capture_output=True, text=True, timeout=120
        )
        return result.returncode == 0
    except Exception as e:
        _log(f"[clone_shallow] Failed: {e}")
        return False


# ── Strategy 2: git clone (full — fallback if shallow fails) ─────────────────

def _clone_full(url: str, dest: Path) -> bool:
    """Full clone for repos that block shallow clones (large mono-repos)."""
    try:
        result = subprocess.run(
            [GIT_CMD, "clone", url, str(dest)],
            capture_output=True, text=True, timeout=300
        )
        return result.returncode == 0
    except Exception as e:
        _log(f"[clone_full] Failed: {e}")
        return False


# ── Strategy 3: GitHub Zip Fallback (Heavy Duty) ─────────────────────────────

def _download_github_zip(url: str, dest: Path) -> bool:
    """Fallback to downloading repo as a ZIP file via GitHub API if git clones fail."""
    import urllib.request
    import zipfile
    import io
    
    # Parse https://github.com/user/repo
    parts = url.rstrip('/').split('/')
    if len(parts) < 2 or "github.com" not in url:
        return False
    user, repo = parts[-2], parts[-1]
    if repo.endswith(".git"):
        repo = repo[:-4]
        
    zip_url = f"https://api.github.com/repos/{user}/{repo}/zipball/HEAD"
    try:
        req = urllib.request.Request(zip_url, headers={"User-Agent": "OmniClaw-OID/2.0"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            with zipfile.ZipFile(io.BytesIO(resp.read())) as z:
                z.extractall(path=dest)
        # Zipball extracts into a sub-folder (e.g. user-repo-abc1234), move contents UP
        extracted_dirs = [d for d in dest.iterdir() if d.is_dir()]
        if extracted_dirs:
            inner_dir = extracted_dirs[0]
            for item in inner_dir.iterdir():
                shutil.move(str(item), str(dest / item.name))
            inner_dir.rmdir()
        return True
    except Exception as e:
        _log(f"[github_zip_fallback] Failed: {e}")
        return False


# ── Strategy 4: Scrape via firecrawl_adapter (URL/web page) ─────────────────

def _scrape_url_firecrawl(url: str) -> Optional[str]:
    """
    Scrape a URL via the OmniClaw firecrawl adapter (MCP-registered scraper).
    Falls back gracefully if firecrawl is unavailable.
    """
    try:
        # Dynamic import — only load if plugin is installed
        sys.path.insert(0, str(Path(OMNICLAW_ROOT) / "ecosystem"))
        from plugins.firecrawl.firecrawl_adapter import get_firecrawl  # type: ignore
        fc = get_firecrawl()
        content = fc.research_url(url)
        return content if content else None
    except Exception as e:
        _log(f"[firecrawl] Unavailable or failed: {e}")
        return None


# ── Strategy 4: urllib fallback ──────────────────────────────────────────────

def _scrape_url_urllib(url: str) -> Optional[str]:
    """Raw HTTP fallback when firecrawl is not available."""
    try:
        import urllib.request
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "OmniClaw-OID/2.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        _log(f"[urllib_fallback] Failed: {e}")
        return None


# ── Public API ────────────────────────────────────────────────────────────────

def fetch_repo(url: str, ticket_id: str) -> Optional[Path]:
    """
    Clone a GitHub/GitLab repository into a dedicated Quarantine directory.
    Tries shallow clone first, falls back to full clone if that fails.

    Returns:
        Path to the cloned repo inside QUARANTINE, or None on failure.
    """
    safe = _safe_name(url)
    dest = QUARANTINE_DIR / ticket_id / safe
    dest.parent.mkdir(parents=True, exist_ok=True)

    _log(f"[fetch_repo] Attempting shallow clone: {url}")
    if _clone_shallow(url, dest):
        _log(f"[fetch_repo] Shallow clone OK -> {dest}")
        return dest

    _log(f"[fetch_repo] Shallow failed. Trying full clone...")
    if _clone_full(url, dest):
        _log(f"[fetch_repo] Full clone OK -> {dest}")
        return dest

    _log(f"[fetch_repo] Git clones blocked. Engaging Heavy-Duty ZIP Fallback...")
    if _download_github_zip(url, dest):
        _log(f"[fetch_repo] Heavy-Duty ZIP OK -> {dest}")
        return dest

    _log(f"[fetch_repo] All clone and download strategies exhausted for: {url}")
    return None


def fetch_url(url: str, ticket_id: str) -> Optional[str]:
    """
    Fetch text content from a URL (webpage, post, documentation, etc.).
    Uses firecrawl_adapter first, falls back to urllib.

    Returns:
        Extracted text content, or None on complete failure.
    """
    import sys  # needed for dynamic import in firecrawl
    _log(f"[fetch_url] Fetching: {url}")

    content = _scrape_url_firecrawl(url)
    if content:
        _log(f"[fetch_url] Firecrawl OK ({len(content)} chars)")
        return content

    _log(f"[fetch_url] Falling back to urllib...")
    content = _scrape_url_urllib(url)
    if content:
        _log(f"[fetch_url] urllib OK ({len(content)} chars)")
        return content

    _log(f"[fetch_url] All fetch strategies exhausted for: {url}")
    return None


def fetch_local_file(path: str) -> Optional[str]:
    """
    Read a local file (PDF handled via text extraction, others as raw text).
    Returns extracted text content.
    """
    fpath = Path(path)
    if not fpath.exists():
        _log(f"[fetch_local] File not found: {path}")
        return None

    if fpath.suffix.lower() == ".pdf":
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(str(fpath))
            text = "\n".join(
                page.extract_text() or "" for page in reader.pages
            )
            _log(f"[fetch_local] PDF extracted: {fpath.name} ({len(text)} chars)")
            return text
        except Exception as e:
            _log(f"[fetch_local] PDF extraction failed: {e}")
            return None

    try:
        content = fpath.read_text(encoding="utf-8", errors="replace")
        _log(f"[fetch_local] File read: {fpath.name} ({len(content)} chars)")
        return content
    except Exception as e:
        _log(f"[fetch_local] Read failed: {e}")
        return None
