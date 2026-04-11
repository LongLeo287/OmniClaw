"""
oid/extractor.py — OID Knowledge Extraction Module
Owner: knowledge_enricher (Dept: Knowledge & Registry)
Role: Compress a raw cloned repository into a single structured Markdown file.
Optimized for: RAG / LLM context loading, disk efficiency, Windows MAX_PATH compliance.

Usage (as module):
    from oid.extractor import extract_knowledge
    extract_knowledge(Path("/path/to/repo"), cleanup=True)
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime

# Windows stdout encoding fix
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# ── Configuration ─────────────────────────────────────────────────────────────
MAX_FILE_SIZE_MB = 10
MAX_DEPTH = 10
OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[4])

PROCESSED_DIR = Path(OMNICLAW_ROOT) / "brain" / "knowledge" / "processed_repos"

IGNORE_DIRS = {
    ".git", ".svn", ".hg", "node_modules", "vendor", "venv", ".venv",
    "env", ".env", "__pycache__", "dist", "build", "out", "target",
    "bin", "obj", ".idea", ".vscode", "coverage", ".next", ".nuxt"
}

IGNORE_EXTS = {
    # Binary and media
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".webp",
    ".mp4", ".webm", ".mov", ".mp3", ".wav",
    # Compiled artifacts
    ".exe", ".dll", ".so", ".dylib", ".class", ".jar",
    ".pyc", ".pyo", ".pyd", ".whl",
    # Archives
    ".zip", ".tar", ".gz", ".rar", ".7z",
}

IGNORE_FILES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "poetry.lock", "Pipfile.lock", "Cargo.lock"
}

EXT_LANGUAGE_MAP = {
    ".py": "python", ".js": "javascript", ".ts": "typescript",
    ".tsx": "tsx", ".jsx": "jsx", ".html": "html", ".css": "css",
    ".scss": "scss", ".json": "json", ".md": "markdown",
    ".yml": "yaml", ".yaml": "yaml", ".sh": "bash", ".bash": "bash",
    ".ps1": "powershell", ".go": "go", ".rs": "rust", ".java": "java",
    ".c": "c", ".cpp": "cpp", ".h": "c", ".cs": "csharp",
    ".php": "php", ".rb": "ruby", ".sql": "sql", ".xml": "xml"
}


def _log(msg: str):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] [knowledge_enricher] {msg}")


def _is_readable_text(filepath: Path) -> bool:
    """Safely probe whether a file is human-readable UTF-8 text."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except Exception:
        return False


def extract_knowledge(repo_path: Path, cleanup: bool = False) -> bool:
    """
    Compress a raw repository directory into a single Markdown knowledge file.

    Args:
        repo_path: Absolute path to the cloned repository directory.
        cleanup:   If True, delete the raw repo after successful extraction.

    Returns:
        True on success, False on failure.
    """
    if not repo_path.exists() or not repo_path.is_dir():
        _log(f"[ERROR] Source directory not found: {repo_path}")
        return False

    repo_name = repo_path.name
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_file = PROCESSED_DIR / f"{repo_name}_knowledge.md"

    _log(f"[EXTRACTING] {repo_name} -> {out_file.name}")

    total_files = 0
    total_lines = 0

    with open(out_file, "w", encoding="utf-8") as out:
        out.write(f"# KNOWLEDGE EXTRACT: {repo_name}\n")
        out.write(f"> **Extracted on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write(f"> **Source:** {repo_path.as_posix()}\n\n")
        out.write("---\n\n")

        for root_dir, dirs, files in os.walk(repo_path):
            # Enforce depth limit to prevent infinite symlink loops
            current_depth = len(Path(root_dir).relative_to(repo_path).parts)
            if current_depth > MAX_DEPTH:
                dirs.clear()
                continue

            # Prune ignored directories in-place
            dirs[:] = sorted([
                d for d in dirs
                if d not in IGNORE_DIRS and not d.startswith('.')
            ])

            for file in sorted(files):
                if file in IGNORE_FILES:
                    continue

                fpath = Path(root_dir) / file

                # Security: never follow symlinks
                if fpath.is_symlink():
                    continue

                if fpath.suffix.lower() in IGNORE_EXTS:
                    continue

                # Anti Zip-Bomb: size guard
                try:
                    if fpath.stat().st_size > MAX_FILE_SIZE_MB * 1024 * 1024:
                        _log(f"[SKIP] File too large (>{MAX_FILE_SIZE_MB}MB): {fpath.name}")
                        continue
                except Exception:
                    continue

                if not _is_readable_text(fpath):
                    continue

                rel_path = fpath.relative_to(repo_path)
                lang = EXT_LANGUAGE_MAP.get(fpath.suffix.lower(), "")

                try:
                    content = fpath.read_text(encoding="utf-8", errors="replace")
                    line_count = len(content.splitlines())
                    if line_count == 0:
                        continue

                    out.write(f"## File: `{rel_path.as_posix()}`\n")
                    out.write(f"```{lang}\n")
                    out.write(content)
                    if not content.endswith('\n'):
                        out.write("\n")
                    out.write("```\n\n")

                    total_files += 1
                    total_lines += line_count

                except Exception as e:
                    _log(f"[WARN] Could not read {fpath.name}: {e}")

    _log(f"[DONE] Extracted {total_files} files / {total_lines} lines into {out_file.name}")

    if cleanup:
        _log(f"[CLEANUP] Removing raw repo: {repo_name}")
        try:
            shutil.rmtree(repo_path, ignore_errors=True)
            _log(f"[CLEANUP] Deleted: {repo_name}")
        except Exception as e:
            _log(f"[ERROR] Cleanup failed for {repo_name}: {e}")

    return True


# ── CLI entrypoint (backward compatible) ─────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="OmniClaw OID — Knowledge Extractor"
    )
    parser.add_argument("--dir", required=True,
                        help="Path to raw cloned repository directory")
    parser.add_argument("--cleanup", action="store_true",
                        help="Delete raw directory after successful extraction")
    args = parser.parse_args()

    extract_knowledge(Path(args.dir), args.cleanup)
