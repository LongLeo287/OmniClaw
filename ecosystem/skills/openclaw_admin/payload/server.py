#!/usr/bin/env python3
"""OpenClaw Admin Panel - Backend Server v2"""

import json, os, re, shutil, subprocess
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

OPENCLAW_DIR = Path.home() / ".openclaw"
CONFIG_FILE = OPENCLAW_DIR / "openclaw.json"
MEMORY_DIR = OPENCLAW_DIR / "workspace" / "memory"
CRON_FILE = OPENCLAW_DIR / "cron" / "jobs.json"
PROFILE_FILES = ["USER.md", "SOUL.md", "AGENTS.md", "MEMORY.md", "TOOLS.md", "HEARTBEAT.md", "IDENTITY.md"]
CRON_RUNS_DIR = OPENCLAW_DIR / "cron" / "runs"
SESSIONS_FILE = OPENCLAW_DIR / "agents" / "main" / "sessions" / "sessions.json"
SESSIONS_DIR = OPENCLAW_DIR / "agents" / "main" / "sessions"
SKILLS_DIR = OPENCLAW_DIR / "workspace" / "skills"
WORKSPACE_DIR = OPENCLAW_DIR / "workspace"
LOGS_DIR = OPENCLAW_DIR / "logs"
PORT = 8765

def read_config():
    try:
        return json.loads(CONFIG_FILE.read_text())
    except Exception as e:
        return {"error": str(e)}

def write_config(data):
    try:
        shutil.copy2(CONFIG_FILE, str(CONFIG_FILE) + ".admin-bak")
        CONFIG_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}

def get_memory_files():
    files = []
    if MEMORY_DIR.exists():
        for f in sorted(MEMORY_DIR.iterdir()):
            if f.suffix == ".md":
                stat = f.stat()
                try: content = f.read_text(encoding="utf-8")
                except: content = ""
                files.append({
                    "name": f.name, "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M"),
                    "lines": len(content.splitlines()),
                    "preview": content[:200], "content": content
                })
    return files

def get_memory_file(filename):
    fp = MEMORY_DIR / Path(filename).name
    if fp.exists() and fp.suffix == ".md":
        return {"content": fp.read_text(encoding="utf-8"), "name": fp.name}
    return {"error": "Không tìm thấy file"}

def save_memory_file(filename, content):
    fp = MEMORY_DIR / Path(filename).name
    if not fp.name.endswith(".md"): return {"error": "Chỉ hỗ trợ file .md"}
    try: fp.write_text(content, encoding="utf-8"); return {"success": True}
    except Exception as e: return {"error": str(e)}

def delete_memory_file(filename):
    fp = MEMORY_DIR / Path(filename).name
    if fp.exists() and fp.suffix == ".md":
        shutil.copy2(fp, str(fp) + ".deleted")
        fp.unlink(); return {"success": True}
    return {"error": "Không tìm thấy file"}

def get_cron_jobs():
    try:
        data = json.loads(CRON_FILE.read_text())
        jobs = data.get("jobs", [])
        for j in jobs:
            s = j.get("state", {})
            for key in ["lastRunAtMs", "nextRunAtMs", "createdAtMs", "updatedAtMs"]:
                ts = s.get(key) or j.get(key)
                fkey = key.replace("Ms", "Fmt")
                if ts:
                    s[fkey] = datetime.fromtimestamp(ts/1000).strftime("%d/%m/%Y %H:%M")
        return jobs
    except Exception as e:
        return []

def toggle_cron_job(job_id, enabled):
    try:
        data = json.loads(CRON_FILE.read_text())
        for j in data["jobs"]:
            if j["id"] == job_id:
                j["enabled"] = enabled
                j["updatedAtMs"] = int(datetime.now().timestamp() * 1000)
        shutil.copy2(CRON_FILE, str(CRON_FILE) + ".admin-bak")
        CRON_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}

def delete_cron_job(job_id):
    try:
        data = json.loads(CRON_FILE.read_text())
        data["jobs"] = [j for j in data["jobs"] if j["id"] != job_id]
        shutil.copy2(CRON_FILE, str(CRON_FILE) + ".admin-bak")
        CRON_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}

def get_sessions():
    try:
        data = json.loads(SESSIONS_FILE.read_text())
        sessions = []
        for key, val in data.items():
            updated = val.get("updatedAt", 0)
            sessions.append({
                "key": key,
                "sessionId": val.get("sessionId", ""),
                "channel": val.get("lastChannel") or val.get("origin", {}).get("provider", "unknown"),
                "chatType": val.get("chatType", "direct"),
                "updatedAt": datetime.fromtimestamp(updated/1000).strftime("%d/%m/%Y %H:%M") if updated else "N/A",
                "updatedAtMs": updated,
                "label": val.get("origin", {}).get("label", ""),
                "from": val.get("origin", {}).get("from", key.split(":")[-1]),
            })
        sessions.sort(key=lambda x: x["updatedAtMs"], reverse=True)
        return sessions
    except Exception as e:
        return []

def get_skills():
    skills = []
    cfg = read_config()
    enabled_skills = cfg.get("skills", {}).get("entries", {})
    if SKILLS_DIR.exists():
        for d in sorted(SKILLS_DIR.iterdir()):
            if d.is_dir():
                skill_md = d / "SKILL.md"
                desc = ""
                if skill_md.exists():
                    try:
                        lines = skill_md.read_text(encoding="utf-8").splitlines()
                        for line in lines:
                            if line.startswith("description:"):
                                desc = line.replace("description:", "").strip().strip('"')
                                break
                    except: pass
                skills.append({
                    "name": d.name,
                    "description": desc or d.name,
                    "enabled": enabled_skills.get(d.name, {}).get("enabled", False),
                    "hasSkillMd": skill_md.exists()
                })
    return skills

def toggle_skill(name, enabled):
    try:
        cfg = read_config()
        if "skills" not in cfg: cfg["skills"] = {}
        if "entries" not in cfg["skills"]: cfg["skills"]["entries"] = {}
        if name not in cfg["skills"]["entries"]: cfg["skills"]["entries"][name] = {}
        cfg["skills"]["entries"][name]["enabled"] = enabled
        return write_config(cfg)
    except Exception as e:
        return {"error": str(e)}

def get_chat_sessions():
    """Lấy danh sách sessions có tin nhắn"""
    try:
        data = json.loads(SESSIONS_FILE.read_text())
        result = []
        for key, val in data.items():
            sid = val.get("sessionId", "")
            if not sid:
                continue
            # Đếm messages từ jsonl
            jsonl = SESSIONS_DIR / f"{sid}.jsonl"
            msg_count = 0
            file_size = 0
            if jsonl.exists():
                file_size = jsonl.stat().st_size
                try:
                    with open(jsonl) as f:
                        for line in f:
                            try:
                                d = json.loads(line)
                                if d.get("type") == "message":
                                    msg_count += 1
                            except: pass
                except: pass
            updated = val.get("updatedAt", 0)
            result.append({
                "key": key,
                "sessionId": sid,
                "channel": val.get("lastChannel") or val.get("origin", {}).get("provider", "unknown"),
                "label": val.get("origin", {}).get("label", ""),
                "from": val.get("origin", {}).get("from", key.split(":")[-1]),
                "updatedAt": datetime.fromtimestamp(updated/1000).strftime("%d/%m/%Y %H:%M") if updated else "N/A",
                "updatedAtMs": updated,
                "msgCount": msg_count,
                "fileSizeKb": round(file_size / 1024, 1),
                "hasFile": jsonl.exists()
            })
        result.sort(key=lambda x: x["updatedAtMs"], reverse=True)
        return result
    except Exception as e:
        return []


def get_session_messages(session_id, limit=200):
    """Đọc tin nhắn từ session jsonl"""
    safe_id = session_id.replace("/", "").replace("..", "")
    jsonl = SESSIONS_DIR / f"{safe_id}.jsonl"
    if not jsonl.exists():
        # Thử file reset
        for f in SESSIONS_DIR.iterdir():
            if f.name.startswith(safe_id) and f.name.endswith(".jsonl"):
                jsonl = f
                break
    if not jsonl.exists():
        return {"error": "Không tìm thấy session"}
    messages = []
    try:
        with open(jsonl, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    d = json.loads(line)
                    if d.get("type") != "message":
                        continue
                    msg = d.get("message", {})
                    role = msg.get("role", "?")
                    content = msg.get("content", [])
                    text = ""
                    if isinstance(content, str):
                        text = content
                    elif isinstance(content, list):
                        parts = []
                        for c in content:
                            if isinstance(c, dict):
                                if c.get("type") == "text":
                                    parts.append(c.get("text", ""))
                                elif c.get("type") == "tool_use":
                                    parts.append(f"[🔧 {c.get('name','tool')}]")
                                elif c.get("type") == "tool_result":
                                    r = c.get("content", "")
                                    if isinstance(r, list):
                                        r = " ".join(x.get("text","") for x in r if isinstance(x,dict))
                                    parts.append(f"[📤 Kết quả: {str(r)[:100]}]")
                        text = "\n".join(parts)
                    if text.strip():
                        messages.append({
                            "role": role,
                            "text": text,
                            "ts": d.get("timestamp", "")
                        })
                except: pass
        # Lấy limit tin cuối
        return {"messages": messages[-limit:], "total": len(messages)}
    except Exception as e:
        return {"error": str(e)}


def get_profile_files():
    """Lấy danh sách file hồ sơ"""
    files = []
    for name in PROFILE_FILES:
        fp = WORKSPACE_DIR / name
        if fp.exists():
            try:
                content = fp.read_text(encoding="utf-8")
                stat = fp.stat()
                files.append({
                    "name": name,
                    "content": content,
                    "lines": len(content.splitlines()),
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M")
                })
            except: pass
    return files


def save_profile_file(name, content):
    """Lưu file hồ sơ"""
    safe = Path(name).name
    if safe not in PROFILE_FILES:
        return {"error": "File không được phép"}
    fp = WORKSPACE_DIR / safe
    try:
        shutil.copy2(fp, str(fp) + ".admin-bak")
        fp.write_text(content, encoding="utf-8")
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}


def get_cron_run_history(job_id):
    """Lấy lịch sử chạy của 1 cron job từ file jsonl"""
    safe_id = job_id.replace("/", "").replace("..", "")
    jsonl = CRON_RUNS_DIR / f"{safe_id}.jsonl"
    if not jsonl.exists():
        return []
    runs = []
    try:
        with open(jsonl, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    d = json.loads(line)
                    run_ts = d.get("ts", 0) or d.get("runAtMs", 0)
                    next_ts = d.get("nextRunAtMs", 0)
                    runs.append({
                        "status": d.get("status", "?"),
                        "summary": d.get("summary", "")[:500],
                        "durationMs": d.get("durationMs", 0),
                        "action": d.get("action", ""),
                        "ts": datetime.fromtimestamp(run_ts/1000).strftime("%d/%m/%Y %H:%M") if run_ts else "?",
                        "nextRun": datetime.fromtimestamp(next_ts/1000).strftime("%d/%m %H:%M") if next_ts else "?",
                    })
                except: pass
    except: pass
    runs.reverse()  # mới nhất lên trước
    return runs


def get_diary_files():
    """Lấy danh sách file nhật ký hàng ngày"""
    files = []
    if MEMORY_DIR.exists():
        for f in sorted(MEMORY_DIR.iterdir(), reverse=True):
            if f.suffix == ".md" and re.match(r"\d{4}-\d{2}-\d{2}\.md", f.name):
                try:
                    content = f.read_text(encoding="utf-8")
                    stat = f.stat()
                    # Parse ngày
                    date_str = f.stem  # e.g. "2026-03-19"
                    try:
                        dt = datetime.strptime(date_str, "%Y-%m-%d")
                        weekdays_vi = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
                        weekday = weekdays_vi[dt.weekday()]
                        display_date = f"{weekday}, {dt.strftime('%d/%m/%Y')}"
                    except:
                        display_date = date_str
                    files.append({
                        "name": f.name,
                        "date": date_str,
                        "displayDate": display_date,
                        "content": content,
                        "lines": len(content.splitlines()),
                        "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%H:%M")
                    })
                except: pass
    return files[:30]  # tối đa 30 ngày


def get_proxy_detail():
    """Lấy chi tiết proxy và cấu hình keys"""
    try:
        r = subprocess.run(["curl","-s","--max-time","2","http://127.0.0.1:3099/status"],
            capture_output=True, text=True, timeout=3)
        cfg = read_config()
        provider = cfg.get("models",{}).get("providers",{}).get("myprovider",{})
        api_key = provider.get("apiKey","")
        if r.returncode == 0 and r.stdout:
            data = json.loads(r.stdout)
            return {
                "online": True,
                "host": data.get("host",""),
                "totalKeys": data.get("totalKeys",0),
                "nextKeyIndex": data.get("nextKeyIndex",0),
                "currentApiKeyPreview": api_key[:12]+"..." if api_key else "N/A",
                "primaryModel": cfg.get("agents",{}).get("defaults",{}).get("model",{}).get("primary","N/A")
            }
    except: pass
    return {"online": False}



def get_proxy_status():
    try:
        r = subprocess.run(["curl","-s","--max-time","2","http://127.0.0.1:3099/status"],
            capture_output=True, text=True, timeout=3)
        if r.returncode == 0 and r.stdout:
            return {"online": True, "data": json.loads(r.stdout)}
    except: pass
    return {"online": False}

def get_openclaw_status():
    cfg = read_config()
    port = cfg.get("gateway", {}).get("port", 18789)
    token = cfg.get("gateway", {}).get("auth", {}).get("token", "")
    try:
        r = subprocess.run(["curl","-s","--max-time","2","-H",f"Authorization: Bearer {token}",
            f"http://127.0.0.1:{port}/status"], capture_output=True, text=True, timeout=3)
        if r.returncode == 0:
            return {"online": True}
    except: pass
    return {"online": False}

def kill_openclaw_browser():
    try:
        subprocess.run(["pkill", "-f", "Google Chrome.*openclaw/user-data"], check=False, capture_output=True)
        subprocess.run(["pkill", "-f", "openclaw-gateway"], check=False, capture_output=True)
        return {"success": True, "message": "Đã chặn hoàn toàn tiến trình OpenClaw."}
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_logs():
    entries = []
    if LOGS_DIR.exists():
        for f in sorted(LOGS_DIR.iterdir(), reverse=True):
            if f.is_file() and f.suffix in [".log", ".jsonl"]:
                try:
                    content = f.read_text(encoding="utf-8", errors="replace")
                    # Lấy 200 dòng cuối
                    lines = content.splitlines()[-200:]
                    entries.append({
                        "name": f.name,
                        "modified": datetime.fromtimestamp(f.stat().st_mtime).strftime("%d/%m/%Y %H:%M"),
                        "size": f"({f.stat().st_size // 1024} KB)",
                        "content": "\n".join(lines)
                    })
                except: pass
    return entries[:5]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, path):
        content = Path(path).read_bytes()
        ext = Path(path).suffix
        mime = {".html":"text/html",".css":"text/css",".js":"application/javascript"}.get(ext,"text/plain")
        self.send_response(200)
        self.send_header("Content-Type", f"{mime}; charset=utf-8")
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        routes = {
            "/": lambda: self.send_file(Path(__file__).parent / "index.html"),
            "/index.html": lambda: self.send_file(Path(__file__).parent / "index.html"),
            "/api/config": lambda: self.send_json(read_config()),
            "/api/memory": lambda: self.send_json(get_memory_files()),
            "/api/memory/file": lambda: self.send_json(get_memory_file(params.get("name",[""])[0])),
            "/api/cron": lambda: self.send_json(get_cron_jobs()),
            "/api/sessions": lambda: self.send_json(get_sessions()),
            "/api/skills": lambda: self.send_json(get_skills()),
            "/api/logs": lambda: self.send_json(get_logs()),
            "/api/chats": lambda: self.send_json(get_chat_sessions()),
            "/api/chats/messages": lambda: self.send_json(get_session_messages(params.get("id",[""])[0])),
            "/api/profile": lambda: self.send_json(get_profile_files()),
            "/api/cron/runs": lambda: self.send_json(get_cron_run_history(params.get("id",[""])[0])),
            "/api/diary": lambda: self.send_json(get_diary_files()),
            "/api/proxy/detail": lambda: self.send_json(get_proxy_detail()),
            "/api/status": lambda: self.send_json({
                "proxy": get_proxy_status(),
                "openclaw": get_openclaw_status(),
                "model": read_config().get("agents",{}).get("defaults",{}).get("model",{}).get("primary","N/A"),
                "config_modified": datetime.fromtimestamp(CONFIG_FILE.stat().st_mtime).strftime("%d/%m/%Y %H:%M") if CONFIG_FILE.exists() else "N/A"
            }),
        }

        if path in routes:
            routes[path]()
        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        try: data = json.loads(self.rfile.read(length)) if length else {}
        except: data = {}

        if path == "/api/config":
            self.send_json(write_config(data))
        elif path == "/api/memory/save":
            self.send_json(save_memory_file(data.get("name",""), data.get("content","")))
        elif path == "/api/memory/delete":
            self.send_json(delete_memory_file(data.get("name","")))
        elif path == "/api/cron/toggle":
            self.send_json(toggle_cron_job(data.get("id",""), data.get("enabled", True)))
        elif path == "/api/cron/delete":
            self.send_json(delete_cron_job(data.get("id","")))
        elif path == "/api/profile/save":
            self.send_json(save_profile_file(data.get("name",""), data.get("content","")))
        elif path == "/api/skills/toggle":
            self.send_json(toggle_skill(data.get("name",""), data.get("enabled", True)))
        elif path == "/api/switch":
            provider = data.get("provider")
            cfg = read_config()
            providers = cfg.get("models", {}).get("providers", {})
            if provider not in providers:
                self.send_json({"error": f"Không tìm thấy provider {provider}"}, 404); return
            
            # Tự động lấy ID của model đầu tiên trong danh sách của provider
            model_id = "claude-sonnet-4.6" # Mặc định nếu không tìm thấy
            provider_models = providers[provider].get("models", [])
            if isinstance(provider_models, list) and len(provider_models) > 0:
                model_id = provider_models[0].get("id", model_id)
                
            new_primary = f"{provider}/{model_id}"
            cfg.setdefault("agents", {}).setdefault("defaults", {}).setdefault("model", {})["primary"] = new_primary
            if write_config(cfg):
                # Trigger cập nhật status lập tức nếu cần, nhưng chỉ cần trả về success
                self.send_json({"success": True, "provider": provider})
            else:
                self.send_json({"error": "Không thể ghi file config"}, 500)
        elif path == "/api/kill-browser":
            self.send_json(kill_openclaw_browser())
        else:
            self.send_json({"error": "Không tìm thấy endpoint"}, 404)


if __name__ == "__main__":
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try: s.connect(('10.255.255.255', 1)); local_ip = s.getsockname()[0]
    except: local_ip = '127.0.0.1'
    finally: s.close()

    print("\n" + "="*50)
    print("  🦞 OpenClaw Admin Panel")
    print("="*50)
    print(f"  ✅ Đang chạy tại local: http://localhost:{PORT}")
    print(f"  📱 Truy cập từ LAN/Wifi: http://{local_ip}:{PORT}")
    print(f"  ⛔ Nhấn Ctrl+C để dừng")
    print("="*50 + "\n")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    try: server.serve_forever()
    except KeyboardInterrupt: print("\n✅ Đã dừng server.")
