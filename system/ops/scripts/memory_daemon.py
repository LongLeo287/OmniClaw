import os
import sys
import json
import warnings
warnings.filterwarnings("ignore")

ROOT = os.environ.get("AOS_ROOT", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
ENV_PATH = os.path.join(ROOT, "system", "ops", "secrets", "MASTER.env")
DB_PATH = os.path.join(ROOT, "brain", "memory", "qdrant_db")

def load_env():
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'): continue
                if '=' in line:
                    key, val = line.split('=', 1)
                    os.environ[key.strip()] = val.strip()

load_env()
gemini_key = os.environ.get('GOOGLE_AI_API_KEY', '')
if not gemini_key:
    gemini_key = os.environ.get('GEMINI_API_KEY', '')
gemini_key = gemini_key.strip('"').strip("'")
os.environ['GEMINI_API_KEY'] = gemini_key

# Import mem0 AFTER env variables are loaded
# Fallback gracefully if mem0/numpy not compatible with current Python version
_MEM0_AVAILABLE = False
try:
    from mem0 import Memory
    _MEM0_AVAILABLE = True
except Exception:
    pass


class MemoryCore:
    def __init__(self):
        os.makedirs(DB_PATH, exist_ok=True)
        if _MEM0_AVAILABLE:
            self._init_mem0()
        else:
            self._init_local()

    def _init_mem0(self):
        """Full mem0 + Qdrant mode."""
        self.config = {
            "llm": {
                "provider": "gemini",
                "config": {
                    "model": "gemini-2.5-flash",
                    "api_key": gemini_key,
                    "temperature": 0.1
                }
            },
            "embedder": {
                "provider": "ollama",
                "config": {
                    "model": "nomic-embed-text"
                }
            },
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "path": DB_PATH
                }
            }
        }
        self.m = Memory.from_config(config_dict=self.config)
        self._mode = "mem0"

    def _init_local(self):
        """Fallback: JSON-based local memory store."""
        self._local_db = os.path.join(DB_PATH, "local_memory.json")
        os.makedirs(DB_PATH, exist_ok=True)
        if not os.path.exists(self._local_db):
            with open(self._local_db, 'w', encoding='utf-8') as f:
                json.dump([], f)
        self.m = None
        self._mode = "local_json"

    def add_fact(self, text, user_id="CEO", agent_id=None):
        if self._mode == "mem0":
            meta = {}
            if agent_id: meta["agent"] = agent_id
            return self.m.add(text, user_id=user_id, metadata=meta)
        else:
            data = self.get_all(user_id)
            data.append({"text": text, "user_id": user_id, "agent_id": agent_id})
            with open(self._local_db, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return {"status": "ok", "mode": "local_json"}

    def search(self, query, user_id="CEO"):
        if self._mode == "mem0":
            return self.m.search(query, user_id=user_id)
        data = self.get_all(user_id)
        return [m for m in data if query.lower() in m.get("text", "").lower()]

    def get_all(self, user_id="CEO"):
        if self._mode == "mem0":
            return self.m.get_all(user_id=user_id)
        try:
            with open(self._local_db, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
            return [m for m in all_data if m.get("user_id") == user_id]
        except Exception:
            return []

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "search"
    text = sys.argv[2] if len(sys.argv) > 2 else "AI OS"

    print(f"[*] MemoryCore Direct Access -> Action: {action.upper()}")
    core = MemoryCore()

    if action == "add":
        res = core.add_fact(text)
        print("[+] MEMORY ADDED:", res)
    elif action == "search":
        res = core.search(text)
        print("[?] SEARCH RESULTS:")
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif action == "all":
        res = core.get_all()
        print("[*] ALL MEMORIES:")
        print(json.dumps(res, indent=2, ensure_ascii=False))
