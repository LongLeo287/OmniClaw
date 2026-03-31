"""
pull_remaining_repos.py — Trích xuất Knowledge cho các repo còn thiếu.
QUAD-STREAM fallback chain:
  Stream 1: git clone --depth=1          (nhanh, đầy đủ)
  Stream 2: GitHub ZIP API               (fallback, không hang)
  Stream 3: GitHub Contents API          (file-by-file, cho repo xịn nhiều sao)
  Stream 4: GitHub GraphQL               (metadata + README, last resort)

Chạy: python system/ops/scripts/pull_remaining_repos.py
"""
import os, sys, re, json, base64, zipfile, urllib.request, urllib.error
import subprocess, shutil, time
from pathlib import Path
from datetime import datetime

# ── Paths ─────────────────────────────────────────────────────────────────────
AOS_ROOT      = Path(os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[3]))
PENDING_FILE  = AOS_ROOT / "storage" / "vault" / "DATA" / "PENDING_REPOS.md"
ARCHIVE_DIR   = AOS_ROOT / "storage" / "vault" / "ARCHIVE"
REPOS_DIR     = AOS_ROOT / "brain" / "knowledge" / "repos"
EXTRACTOR     = AOS_ROOT / "system" / "ops" / "scripts" / "knowledge_extractor.py"
PROCESSED_DIR = AOS_ROOT / "brain" / "knowledge" / "processed_repos"
PROGRESS_FILE = AOS_ROOT / "storage" / "vault" / "DATA" / ".pull_progress.json"
ENV_FILE      = AOS_ROOT / "system" / "ops" / "secrets" / "MASTER.env"

CLONE_TIMEOUT    = 600  # git clone timeout -> taskkill -> fallback
DOWNLOAD_TIMEOUT = 300  # urllib ZIP / Contents API socket timeout
EXTRACT_TIMEOUT  = 600  # knowledge_extractor.py timeout
CHUNK_SIZE       = 65536
CONTENTS_MAX_FILES = 500            # giới hạn file download qua Contents API
CONTENTS_MAX_SIZE  = 500_000        # bỏ blob > 500KB
BINARY_EXTS = {
    ".png",".jpg",".jpeg",".gif",".ico",".svg",".webp",".mp4",".webm",
    ".mp3",".wav",".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",
    ".zip",".tar",".gz",".rar",".7z",".exe",".dll",".so",".dylib",
    ".class",".jar",".pyc",".pyo",".pyd",".whl",".o",".a",".lib",
}

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

# ── GitHub helpers ─────────────────────────────────────────────────────────────
def load_token() -> str:
    if not ENV_FILE.exists():
        return ""
    for line in ENV_FILE.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.strip().startswith("GITHUB_TOKEN="):
            return line.strip().split("=", 1)[1].strip()
    return ""

GITHUB_TOKEN = load_token()

def _gh_request(url: str, method: str = "GET", data: bytes = None) -> dict | None:
    """Gọi GitHub API với token nếu có. Trả về dict hoặc None nếu lỗi."""
    req = urllib.request.Request(url, data=data, method=method)
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"{'bearer' if method == 'POST' else 'token'} {GITHUB_TOKEN}")
    req.add_header("User-Agent", "AI-OS-Corp/2.0")
    req.add_header("Accept", "application/vnd.github.v3+json")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        log(f"    [API] HTTP {e.code}: {e.reason}")
        return None
    except Exception as e:
        log(f"    [API] {type(e).__name__}: {e}")
        return None

# ── Progress ───────────────────────────────────────────────────────────────────
def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"done": [], "failed": []}

def save_progress(state: dict):
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

# ── Parse PENDING_REPOS.md ─────────────────────────────────────────────────────
def parse_pending_repos() -> list[tuple[str, str, str, int]]:
    """Trả về list (owner, repo, url, stars)."""
    if not PENDING_FILE.exists():
        log(f"[ERROR] Không tìm thấy: {PENDING_FILE}")
        return []
    unique, seen = [], set()
    for line in PENDING_FILE.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = re.search(r'https://github\.com/([\w\-\.]+)/([\w\-\.]+)', line)
        if not m:
            continue
        owner, repo = m.group(1), m.group(2)
        if repo.endswith(".git"):
            repo = repo[:-4]
        url = f"https://github.com/{owner}/{repo}"
        if url in seen:
            continue
        seen.add(url)
        stars_m = re.search(r'⭐\s*(\d[\d,]*)', line)
        stars = int((stars_m.group(1) if stars_m else "0").replace(",", ""))
        unique.append((owner, repo, url, stars))
    return unique

def is_already_done(repo: str) -> bool:
    if (PROCESSED_DIR / f"{repo}_knowledge.md").exists():
        return True
    if (ARCHIVE_DIR / repo).exists() and any((ARCHIVE_DIR / repo).iterdir()):
        return True
    return False

# ════════════════════════════════════════════════════════════════════════════════
# STREAM 1 — git clone (nhanh, đầy đủ code)
# ════════════════════════════════════════════════════════════════════════════════
def _kill_proc_tree(pid: int):
    subprocess.run(f"taskkill /F /T /PID {pid}", shell=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def stream1_git_clone(owner: str, repo: str, dest: Path) -> bool:
    if dest.exists() and any(dest.iterdir()):
        log("    [S1] EXISTS — bỏ qua clone.")
        return True

    url = f"https://github.com/{owner}/{repo}.git"
    env = os.environ.copy()
    env.update({"GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "never", "GIT_ASKPASS": "echo"})

    log(f"    [S1] git clone --depth=1 (timeout={CLONE_TIMEOUT}s) ...")
    proc = subprocess.Popen(
        ["git", "clone", "--depth=1", "--quiet", url, str(dest)],
        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL, env=env,
    )
    try:
        _, err = proc.communicate(timeout=CLONE_TIMEOUT)
        if proc.returncode == 0:
            log("    [S1] ✓ Clone thành công.")
            return True
        log(f"    [S1] Thất bại rc={proc.returncode}: {err.decode('utf-8',errors='ignore').strip()[:150]}")
    except subprocess.TimeoutExpired:
        log(f"    [S1] Timeout {CLONE_TIMEOUT}s → kill proc tree → fallback.")
        _kill_proc_tree(proc.pid)
        proc.wait()
        time.sleep(1)
    except Exception as e:
        log(f"    [S1] Exception: {e}")

    if dest.exists():
        shutil.rmtree(dest, ignore_errors=True)
    return False

# ════════════════════════════════════════════════════════════════════════════════
# STREAM 2 — GitHub ZIP API (không spawn process, không deadlock)
# ════════════════════════════════════════════════════════════════════════════════
def stream2_zip_api(owner: str, repo: str, dest: Path) -> bool:
    api_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/HEAD"
    req = urllib.request.Request(api_url)
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    req.add_header("User-Agent", "AI-OS-Corp/2.0")

    zip_path = dest.parent / f"_tmp_{repo}.zip"
    log(f"    [S2] Download ZIP từ GitHub API ...")
    try:
        with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as resp:
            with open(zip_path, "wb") as f:
                while True:
                    chunk = resp.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    f.write(chunk)

        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as zf:
            for member in zf.infolist():
                parts = member.filename.split("/", 1)
                if len(parts) < 2 or not parts[1]:
                    continue
                target = dest / parts[1]
                if member.filename.endswith("/"):
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(zf.read(member.filename))

        zip_path.unlink(missing_ok=True)
        log("    [S2] ✓ Download + Unzip thành công.")
        return True

    except urllib.error.HTTPError as e:
        log(f"    [S2] HTTP {e.code}: {e.reason}")
    except zipfile.BadZipFile:
        log("    [S2] ZIP file bị hỏng.")
    except Exception as e:
        log(f"    [S2] {type(e).__name__}: {e}")

    if zip_path.exists():
        zip_path.unlink(missing_ok=True)
    if dest.exists():
        shutil.rmtree(dest, ignore_errors=True)
    return False

# ════════════════════════════════════════════════════════════════════════════════
# STREAM 3 — GitHub Contents API (file-by-file, cho repo xịn nhiều sao)
# ════════════════════════════════════════════════════════════════════════════════
def stream3_contents_api(owner: str, repo: str, dest: Path) -> bool:
    log(f"    [S3] GitHub Contents API (file-by-file) ...")

    # 1. Lấy cây file tree đệ quy
    tree_data = _gh_request(
        f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"
    )
    if not tree_data:
        log("    [S3] Không lấy được file tree.")
        return False

    if tree_data.get("truncated"):
        log("    [S3] Tree bị truncated (repo lớn), chỉ lấy phần đầu.")

    # 2. Lọc file phù hợp
    blobs = [
        item for item in tree_data.get("tree", [])
        if item.get("type") == "blob"
        and item.get("size", 0) < CONTENTS_MAX_SIZE
        and Path(item["path"]).suffix.lower() not in BINARY_EXTS
    ][:CONTENTS_MAX_FILES]

    log(f"    [S3] Sẽ download {len(blobs)} files ...")
    dest.mkdir(parents=True, exist_ok=True)
    downloaded = 0

    for item in blobs:
        blob_data = _gh_request(
            f"https://api.github.com/repos/{owner}/{repo}/git/blobs/{item['sha']}"
        )
        if not blob_data:
            continue
        try:
            if blob_data.get("encoding") == "base64":
                raw = base64.b64decode(blob_data["content"].replace("\n", ""))
                content = raw.decode("utf-8", errors="replace")
            else:
                content = blob_data.get("content", "")

            target = dest / item["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            downloaded += 1
        except Exception:
            continue
        time.sleep(0.08)  # Tránh rate limit (~5000 req/h với token)

    if downloaded == 0:
        log("    [S3] Không tải được file nào, thất bại.")
        if dest.exists():
            shutil.rmtree(dest, ignore_errors=True)
        return False

    log(f"    [S3] ✓ Download {downloaded}/{len(blobs)} files thành công.")
    return True

# ════════════════════════════════════════════════════════════════════════════════
# PREFLIGHT & STREAM 4 (GraphQL)
# ════════════════════════════════════════════════════════════════════════════════
def get_preflight_data(owner: str, repo: str) -> dict | None:
    """Gọi GraphQL lấy metadata (size, topics, description). Trả về None nếu lỗi."""
    if not GITHUB_TOKEN:
        return None
        
    query = """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        diskUsage
        description stargazerCount forkCount updatedAt
        primaryLanguage { name }
        licenseInfo { spdxId }
        repositoryTopics(first: 10) { nodes { topic { name } } }
        readme_main: object(expression: "HEAD:README.md") { ... on Blob { text } }
        readme_alt:  object(expression: "HEAD:readme.md") { ... on Blob { text } }
        readme_rst:  object(expression: "HEAD:README.rst") { ... on Blob { text } }
      }
    }"""
    payload = json.dumps({"query": query, "variables": {"owner": owner, "name": repo}}).encode("utf-8")
    data = _gh_request("https://api.github.com/graphql", method="POST", data=payload)
    if not data:
        return None
    r = (data.get("data") or {}).get("repository")
    return r

def write_stream4_direct(owner: str, repo: str, r: dict) -> bool:
    """Stream 4: Write metadata + README directly to PROCESSED_DIR."""
    readme = (
        (r.get("readme_main") or {}).get("text")
        or (r.get("readme_alt")  or {}).get("text")
        or (r.get("readme_rst")  or {}).get("text")
        or "(Không có README)"
    )
    topics = [t["topic"]["name"] for t in (r.get("repositoryTopics") or {}).get("nodes", [])]
    lang    = (r.get("primaryLanguage") or {}).get("name", "N/A")
    license_ = (r.get("licenseInfo") or {}).get("spdxId", "Unknown")

    note = f"""# 📦 {owner}/{repo} [GRAPHQL — Stream 4]
🔗 https://github.com/{owner}/{repo}

## Meta
- **Size:** ~{r.get('diskUsage', 0) // 1024} MB | **Stars:** ⭐ {r.get('stargazerCount', 0)} | **Forks:** 🍴 {r.get('forkCount', 0)}
- **Language:** {lang} | **License:** {license_}
- **Updated:** {(r.get('updatedAt') or '')[:10]}
- **Topics:** {', '.join(topics) or '(none)'}

## Mô tả
{r.get('description') or '(No description)'}

## README (FULL)
```markdown
{readme[:15000]}
```

---
*Stream 4: GraphQL Direct Mode | Extracted: {datetime.now().strftime('%Y-%m-%d %H:%M')} | AI OS Corp*
"""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_file = PROCESSED_DIR / f"{repo}_knowledge.md"
    out_file.write_text(note, encoding="utf-8")
    log(f"    [S4] ✓ Ghi trực tiếp → {out_file.name}")
    return True

# ════════════════════════════════════════════════════════════════════════════════
# ORCHESTRATOR — SMART ROUTING
# ════════════════════════════════════════════════════════════════════════════════
def acquire_repo(owner: str, repo: str, dest: Path) -> tuple[bool, bool, str]:
    """
    Định tuyến thông minh dựa vào Rules.
    Trả về (success, needs_extract, stream_used).
    """
    meta = get_preflight_data(owner, repo)
    if meta:
        size_kb = meta.get("diskUsage") or 0
        size_mb = size_kb / 1024
        topics = [t["topic"]["name"].lower() for t in (meta.get("repositoryTopics") or {}).get("nodes", [])]
        name_desc = f"{repo} {meta.get('description') or ''}".lower()
        is_awesome = "awesome" in name_desc or any("awesome" in t for t in topics)
        
        log(f"  [PREFLIGHT] Size: {size_mb:.1f}MB | Awesome List: {is_awesome}")
        
        # Rule 1: Awesome Lists (chỉ chứa link/README)
        if is_awesome:
            log("  → [RULE 1] Repo dạng Awesome List (bản chất chỉ có README) → Đi Stream 4")
            ok = write_stream4_direct(owner, repo, meta)
            return ok, False, "S4(GraphQL)"
            
        if size_mb > 500:
             log(f"  [CẢNH BÁO] Repo khổng lồ ({size_mb:.1f}MB) - Vẫn tiếp tục tải để lấy full code!")
            
        # Rule 2: Contents API
        if 0 < size_mb <= 5:
            log("  → [RULE 2] Repo siêu nhỏ gọn (<5MB) → Đi Stream 3")
            if stream3_contents_api(owner, repo, dest):
                return True, True, "S3(ContentsAPI)"
            log("    [S3 FAIL] Fallback áp dụng Rule 4 → Stream 2 (ZIP)")
            if stream2_zip_api(owner, repo, dest):
                return True, True, "S2(ZIP-Fallback)"
            return False, False, "Failed"
            
        log("  → [RULE 3] Repo tiêu chuẩn (5-200MB) → Đi Stream 1 (Git Clone)")
    else:
         log("  [PREFLIGHT] Không có token hoặc lỗi API → Đi luồng mặc định (Stream 1)")

    # Default / Rule 3: Git Clone
    if stream1_git_clone(owner, repo, dest):
        return True, True, "S1(Git)"
        
    # Rule 4: ZIP Fallback
    log("  → [RULE 4] Stream 1 thất bại → Fallback Stream 2 (ZIP API cứu cánh) ...")
    if stream2_zip_api(owner, repo, dest):
        return True, True, "S2(ZIP-Fallback)"

    return False, False, "Failed"

# ── Extract Knowledge ──────────────────────────────────────────────────────────
def extract_knowledge(archive_path: Path) -> bool:
    """Chạy knowledge_extractor.py — truyền path ARCHIVE thật, không phải junction."""
    try:
        res = subprocess.run(
            [sys.executable, str(EXTRACTOR), "--dir", str(archive_path)],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL, timeout=EXTRACT_TIMEOUT,
        )
        if res.returncode == 0:
            log(f"  [EXTRACT] ✓ → {archive_path.name}_knowledge.md")
            return True
        err = res.stderr.decode("utf-8", errors="ignore").strip()[:300]
        log(f"  [EXTRACT ERROR] rc={res.returncode} | {err}")
        return False
    except subprocess.TimeoutExpired:
        log(f"  [EXTRACT TIMEOUT] Quá {EXTRACT_TIMEOUT}s")
        return False
    except Exception as e:
        log(f"  [EXTRACT EXCEPTION] {e}")
        return False

# ── Junction ───────────────────────────────────────────────────────────────────
def create_junction(src: Path, target: Path):
    if target.exists():
        return
    try:
        subprocess.run(
            f'cmd /c mklink /J "{target}" "{src}"',
            shell=True, check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10,
        )
        log(f"  [JUNCTION] ✓ → brain/knowledge/repos/{target.name}")
    except Exception as e:
        log(f"  [JUNCTION WARN] {e}")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print(f"\n{'='*65}")
    print("  PULL REMAINING REPOS — Quad-Stream Knowledge Extractor")
    print(f"  Root  : {AOS_ROOT}")
    tk = f"{GITHUB_TOKEN[:4]}...{GITHUB_TOKEN[-4:]}" if len(GITHUB_TOKEN) > 8 else "(không có)"
    print(f"  Token : {tk}")
    print(f"  Luồng : S1:git → S2:ZIP → S3:Contents API → S4:GraphQL")
    print(f"  Mode  : SMART ROUTING (Preflight -> Rules)")
    print(f"{'='*65}\n")

    repos = parse_pending_repos()
    if not repos:
        return

    state = load_progress()

    missing = []
    for owner, repo, url, stars in repos:
        if url in state["done"] or url in state["failed"]:
            continue
        if is_already_done(repo):
            if url not in state["done"]:
                state["done"].append(url)
            continue
        missing.append((owner, repo, url, stars))
    save_progress(state)

    log(f"Tổng: {len(repos)}  |  Done: {len(state['done'])}  |  Failed: {len(state['failed'])}  |  Cần xử lý: {len(missing)}\n")

    if not missing:
        log("✅ Tất cả repos đã được xử lý!")
        return

    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    failed  = 0

    for i, (owner, repo, url, stars) in enumerate(missing, 1):
        star_label = f"⭐{stars:,}" if stars else ""
        log(f"── [{i}/{len(missing)}] {owner}/{repo} {star_label}")

        dest_archive  = ARCHIVE_DIR / repo
        dest_junction = REPOS_DIR   / repo

        # Acquire repo content (smart routing)
        ok, needs_extract, stream_used = acquire_repo(owner, repo, dest_archive)

        if not ok:
            state["failed"].append(url)
            save_progress(state)
            failed += 1
            log(f"  ❌ TẤT CẢ LUỒNG THẤT BẠI — bỏ qua\n")
            continue

        if needs_extract:
            # Junction (optional, không ảnh hưởng nếu fail)
            create_junction(dest_archive, dest_junction)

            # Extract — dùng path archive THẬT (không phải junction)
            extract_ok = extract_knowledge(dest_archive)
            
            # THEO ĐÚNG QUY TRÌNH: Phân tích/học xong thì xoá luôn bản clone để nhẹ máy
            if dest_junction.exists():
                try: dest_junction.unlink()
                except: pass
            if dest_archive.exists():
                shutil.rmtree(dest_archive, ignore_errors=True)

            if not extract_ok:
                state["failed"].append(url)
                save_progress(state)
                failed += 1
                log(f"  ❌ EXTRACT FAILED\n")
                continue

        # Post-Processing: Đánh giá, tạo Agent hoặc nạp Data
        md_file = PROCESSED_DIR / f"{repo}_knowledge.md"
        if md_file.exists():
            log(f"  [POST] Kích hoạt quy trình xử lý sau tải cho {repo}")
            import subprocess
            subprocess.run([
                sys.executable, str(AOS_ROOT / "system" / "ops" / "scripts" / "omniclaw_post_processor.py"),
                repo, str(md_file)
            ], check=False)

        # Done
        state["done"].append(url)
        save_progress(state)
        success += 1
        log(f"  ✅ DONE ({stream_used})\n")

    print(f"\n{'='*65}")
    print(f"  KẾT QUẢ: ✅ {success} thành công  |  ❌ {failed} thất bại")
    print(f"  Progress: {PROGRESS_FILE}")
    print(f"{'='*65}")
    if failed:
        print(f"  → Chạy lại script để retry {failed} repos bị fail.\n")

if __name__ == "__main__":
    main()
