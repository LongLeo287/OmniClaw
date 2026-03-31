#!/usr/bin/env python3
"""
OmniClaw Post-Extraction Processor
Triggered per-repository after knowledge extraction to evaluate and auto-scaffold agents or index knowledge.
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

ROOT = Path(os.getenv("OMNICLAW_ROOT", "d:/LongLeo/AI OS CORP/AI OS"))
CREATE_AGENT_SCRIPT = ROOT / "system" / "ops" / "scripts" / "CREATE_AGENT.py"
INDEX_RAG_SCRIPT = ROOT / "system" / "ops" / "scripts" / "index_skills_lightrag.py"
LOG_FILE = ROOT / "system" / "telemetry" / "omniclaw_post_processing.log"

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def evaluate_and_route(repo_name: str, md_filepath: str):
    log(f"--- Bắt đầu xử lý Post-Extraction: {repo_name} ---")
    
    path = Path(md_filepath)
    if not path.exists():
        log(f"[ERROR] Không tìm thấy file {md_filepath}")
        return

    content = path.read_text(encoding="utf-8").lower()
    
    # Heuristics
    is_agent = "agent" in content or "llm" in content or "rag" in content
    is_mcp = "mcp" in content or "model context protocol" in content
    
    # Decide action
    my_env = os.environ.copy()
    my_env["PYTHONIOENCODING"] = "utf-8"

    if is_agent and ("python" in content or "framework" in content):
        log(f"[{repo_name}] Phân loại: Tương thích Agent/Department Framework. Đang scaffold...")
        agent_id = f"{repo_name.lower().replace('.', '-')}-agent"
        result = subprocess.run([
            sys.executable, str(CREATE_AGENT_SCRIPT),
            "--id", agent_id,
            "--dept", "engineering",
            "--tier", "2",
            "--title", f"Auto-Scaffolded Agent for {repo_name}"
        ], capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT), env=my_env)
        
        if result.returncode == 0:
            log(f"[{repo_name}] Scaffold thành công: {agent_id}.")
        else:
            log(f"[{repo_name}] Lỗi Scaffold: {result.stderr.strip()}")
            
    elif is_mcp:
        log(f"[{repo_name}] Phân loại: Tương thích MCP Ecosystem.")
        # We can implement auto-mcp config injection here if needed in the future
    else:
        log(f"[{repo_name}] Phân loại: Base Knowledge/Tools.")

    # Always index into LightRAG
    log(f"[{repo_name}] Đang nạp kiến thức vào LightRAG...")
    rag_result = subprocess.run([
        sys.executable, str(INDEX_RAG_SCRIPT),
        "--file", str(path)
    ], capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT), env=my_env)
    
    if rag_result.returncode == 0:
        log(f"[{repo_name}] Nạp kiến thức thành công.")
    else:
        log(f"[{repo_name}] Lỗi nạp RAG: {rag_result.stderr.strip()}")
        
    log(f"--- Hoàn tất xử lý: {repo_name} ---\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: python omniclaw_post_processor.py <repo_name> <md_filepath>")
        sys.exit(1)
        
    repo_name = sys.argv[1]
    md_filepath = sys.argv[2]
    evaluate_and_route(repo_name, md_filepath)

if __name__ == "__main__":
    main()
