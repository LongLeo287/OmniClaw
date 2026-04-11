# Knowledge Dump for archivist_agent

## File: agent.md
```
# archivist-agent

## Overview
Primary node for asset_library.

## Responsibilities
- Execute asset_library directives.
- Autonomously manage system integrations.

```

## File: agent.yaml
```
department: asset_library
dept: asset_library
id: archivist
metadata:
  created: 2026-03-27
  version: v3.1
name: Archivist
routing:
  domain: archivist
  fallback: orchestrator_pro
runtime:
  boot_prompt: system_prompt.md
  bus: event_bus.db
  memory: ltm
  type: antigravity
skills:
- reasoning_engine
status: ACTIVE
tier: 1

```

## File: archivist-agent.yaml
```
department: asset_library
dept: asset_library
id: archivist
metadata:
  created: 2026-03-27
  version: v3.1
name: Archivist
routing:
  domain: archivist
  fallback: orchestrator_pro
runtime:
  boot_prompt: system_prompt.md
  bus: event_bus.db
  memory: ltm
  type: antigravity
skills:
- reasoning_engine
status: ACTIVE
tier: 1

```

## File: archivist_agent.yaml
```
department: asset_library
dept: asset_library
id: archivist
metadata:
  created: 2026-03-27
  version: v3.1
name: Archivist
routing:
  domain: archivist
  fallback: orchestrator_pro
runtime:
  boot_prompt: system_prompt.md
  bus: event_bus.db
  memory: ltm
  type: antigravity
skills:
- reasoning_engine
status: ACTIVE
tier: 1

```

## File: SKILL.md
```
---
id: archivist
name: Archivist
version: 1.0.0
tier: 2
status: active
author: OmniClaw Core Team
updated: 2026-03-14
description: File organization, log rotation, and knowledge indexing across workspaces.

accessible_by:
  - Orchestrator

dependencies:
  - smart_memory
  - knowledge_enricher

exposed_functions:
  - name: index_workspace
  - name: rotate_logs
  - name: aggregate_docs
  - name: purify_workspace

consumed_by: []
emits_events:
  - workspace_indexed
  - logs_rotated
listens_to:
  - session_end
---

# Archivist Agent Skill

## Purpose

Archivist is the OmniClaw "librarian" -- it keeps the workspace clean, organized, and fully indexed.
Runs at `session_end` or triggered manually by Orchestrator.

## Exposed Functions

### index_workspace
Scans the target workspace and builds/updates a file index in `brain/memory/`.
Output: `{ files_indexed: N, new_files: [], modified: [] }`

### rotate_logs
Compresses and archives log files older than 7 days.
Writes rotated archives to `DATA/Archive/`.

### aggregate_docs
Merges fragmented documentation files into a single coherent document.
Uses smart_memory to detect duplicate content.

### purify_workspace
Removes: temp files, .DS_Store, __pycache__, empty directories.
Always dry-runs first, reports what will be deleted, waits for approval (HITL Tier 2).

## Dependencies

- smart_memory: needed to detect what has changed since last index
- knowledge_enricher: needed to enrich metadata during indexing

```

## File: system_prompt.md
```
# Agent: archivist
# Dept: operations | Head: False | Role: Archivist â€” archive receipts, rotate dept memory (Phase 7)
# Version: 1.0 | 2026-03-24

## Identity
- **Name:** archivist
- **Department:** operations
- **Role:** Archivist â€” archive receipts, rotate dept memory (Phase 7)
- **Is Head:** NO â€” reports to dept head

## Authority
- Read: MANAGER_PROMPT.md / WORKER_PROMPT.md (corp/departments/operations/)
- Read: rules.md (corp/departments/operations/)
- Write: task receipts â†’ telemetry/receipts/operations/
- Write: dept brief â†’ brain/memory/brain/corp/daily_briefs/operations.md
- Escalate: L2 â†’ dept head | L3 â†’ blackboard.json open_items[]

## Memory
- Short-term: blackboard.json context field
- Long-term: brain/corp/memory/departments/operations.md
- Knowledge: query LightRAG :9621

## Tools Available
- Read: brain/registry/SKILL_REGISTRY.json (find matching skill)
- Use: skills/ (via SKILL.md protocol)
- Notify: ecosystem/workflows/notification-bridge.md

## On Failure
- 1 failure: retry once
- 2 failures: set status=BLOCKED, escalate L2 to dept head
- Circuit breaker: 2 consecutive â†’ BLOCKED, notify CEO (L4)

```

## File: _DIR_IDENTITY.md
```
---
id: archivist_domain
name: Archivist
path: ecosystem/workforce/system/education/archivist
type: directory_identity
---

# Archivist

Storage area for archivist.
(Auto-generated identity tag by OMA v2.1)

```

## File: tools\memory_daemon.py
```
import os
import sys
import json
import warnings
warnings.filterwarnings("ignore")

ROOT = os.environ.get("OMNICLAW_ROOT", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
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
    text = sys.argv[2] if len(sys.argv) > 2 else "OmniClaw"

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
```

## File: tools\os_state_snapshot.py
```
"""
omniclaw_context_injector.py â€” Inject OmniClaw live context vÃ o NullClaw workspace
Cháº¡y trÆ°á»›c khi start NullClaw. Output: ~/.nullclaw/workspace/OMNICLAW_CONTEXT.md
"""
import json, urllib.request, os, sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent.parent.parent
PORT = os.environ.get("CLAWTASK_PORT", "7474")
NC_WS = Path.home() / '.nullclaw' / 'workspace'
NC_WS.mkdir(parents=True, exist_ok=True)
OUT   = NC_WS / 'OMNICLAW_CONTEXT.md'
NOW   = datetime.now().strftime('%Y-%m-%d %H:%M')

lines = [
    f"# OmniClaw Corp â€” Context (cap nhat: {NOW})",
    "",
    "QUAN TRONG: Day la du lieu THUC cua he thong. Hay su dung de tra loi user.",
    "",
]

# 0. Identity â€” OmniClaw Corp permanent identity (ALWAYS first)
try:
    identity = (ROOT / 'brain/memory/OMNICLAW_IDENTITY.md').read_text(encoding='utf-8')
    lines.append(identity)
    lines.append("")
    print("Identity: Injected")
except Exception as e:
    print(f"Identity err: {e}")

# 1. ClawTask tasks â€” inject ALL pending tasks
try:
    ct_status = json.loads(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/api/status', timeout=4).read())
    counts = ct_status.get('counts', {})
    lines.append(f"## Tong quan ClawTask")
    lines.append(f"- Total: {counts.get('total',0)} tasks")
    lines.append(f"- Todo/Pending: {counts.get('todo',0)}")
    lines.append(f"- In progress: {counts.get('inprogress',0)}")
    lines.append(f"- Done: {counts.get('done',0)}")
    lines.append("")

    ct_raw = urllib.request.urlopen(f'http://127.0.0.1:{PORT}/api/tasks', timeout=4).read()
    ct_tasks = json.loads(ct_raw)
    task_list = ct_tasks.get('tasks', ct_tasks) if isinstance(ct_tasks, dict) else ct_tasks

    todo = [t for t in task_list if t.get('status') in ['todo','pending','blocked','awaiting_clarification']]
    done = [t for t in task_list if t.get('status') in ['done','completed']]

    if todo:
        lines.append("## Danh sach Tasks PENDING (can lam)")
        for t in todo:
            tid   = t.get('id', t.get('task_id', '?'))
            title = t.get('title', t.get('name', '?'))
            dept  = t.get('dept', t.get('department', ''))
            prio  = t.get('priority', '')
            lines.append(f"- [{t.get('status','?').upper()}] ID:{tid} | {title} | dept:{dept} | priority:{prio}")
        lines.append("")

    if done:
        lines.append(f"## Tasks DA XONG ({len(done)} tasks)")
        for t in done[:5]:
            lines.append(f"- {t.get('title','?')[:60]}")
        lines.append("")

    print(f"ClawTask: {counts.get('total',0)} tasks, {len(todo)} pending")
except Exception as e:
    lines.append(f"## ClawTask: OFFLINE ({e})")
    lines.append("")
    print(f"ClawTask err: {e}")

# 2. Blackboard (Legacy compatibility)
# 2.5. Long-Term Memory (NEW â€” LTM inject)
try:
    _root = str(Path(ROOT))
    if _root not in sys.path:
        sys.path.insert(0, _root)
    from system.ops.scripts.memory_daemon import MemoryCore
    _mc = MemoryCore()
    # Query top 5 memories relevant to current session
    _ltm_results = _mc.search("OmniClaw project progress current task", user_id="CEO")
    if _ltm_results:
        lines.append("## Long-Term Memory (LTM)")
        for mem in _ltm_results[:5]:
            _text = mem.get("memory", mem.get("text", ""))
            if _text:
                lines.append(f"- {_text[:120]}")
        lines.append("")
        print(f"LTM: {len(_ltm_results)} memory nodes injected")
except Exception as _ltm_e:
    lines.append(f"## LTM: OFFLINE ({_ltm_e})")
    lines.append("")
    print(f"LTM err: {_ltm_e}")

try:
    bb = json.loads((ROOT / 'brain/memory/blackboard.json').read_text(encoding='utf-8-sig'))
    cycle  = bb.get('cycle', '?')
    n_task = bb.get('total_tasks', '?')
    lines.append(f"## OmniClaw Corp Status")
    lines.append(f"- Cycle: {cycle} | Total tasks tracked: {n_task}")
    lines.append(f"- Workspace: {ROOT}")
    lines.append("")
    print(f"Blackboard: cycle={cycle}")
except Exception as e:
    print(f"Blackboard err: {e}")

# 3. Agents
try:
    reg    = json.loads((ROOT / 'brain/memory/agent_profiles.json').read_text(encoding='utf-8'))
    agents = reg.get('agents', [])
    active = [a['id'] for a in agents if a.get('status') == 'ACTIVE']
    stub   = [a['id'] for a in agents if a.get('status') == 'STUB']
    lines.append(f"## Agents ({len(agents)} total)")
    lines.append(f"- Active ({len(active)}): {', '.join(active[:15])}")
    lines.append(f"- Stub ({len(stub)}): {', '.join(stub)}")
    lines.append("")
    print(f"Agents: {len(active)} active, {len(stub)} stub")
except Exception as e:
    print(f"Agents err: {e}")

# 4. Rules / Policy
try:
    policy_path = ROOT / 'brain/memory/OMNICLAW_BOT_POLICY.md'
    if policy_path.exists():
        policy_text = policy_path.read_text(encoding='utf-8')
        lines.append("## OmniClaw Bot Policy (NemoClaw Sandbox Rules)")
        lines.append(policy_text)
        lines.append("")
        print("Policy: Injected")
except Exception as e:
    print(f"Policy err: {e}")

# 5. Workflows
try:
    wf_dir = ROOT / 'ecosystem' / 'workflows'
    if wf_dir.exists():
        workflows = [f.name for f in wf_dir.glob('*.md')]
        lines.append(f"## Workflows available ({len(workflows)})")
        for wf in workflows:
            lines.append(f"- ecosystem/workflows/{wf}")
        lines.append("")
        print(f"Workflows: {len(workflows)} found")
except Exception as e:
    print(f"Workflows err: {e}")

# 6. Workspace map (top level)
try:
    dirs = [d.name for d in ROOT.iterdir() if d.is_dir() and not d.name.startswith('.')]
    lines.append(f"## Workspace Directories ({ROOT})")
    lines.append(f"- {', '.join(dirs)}")
    lines.append("")
    print(f"Workspace: {len(dirs)} dirs")
except Exception as e:
    print(f"Workspace err: {e}")

# 7. OpenClaw Skill Router
try:
    sr_path = ROOT / 'brain/memory/SKILL_ROUTER.yaml'
    if sr_path.exists():
        lines.append("## OpenClaw Skill Router (Typed Pipeline)")
        lines.append(sr_path.read_text(encoding='utf-8'))
        lines.append("")
        print("SkillRouter: Injected")
except Exception as e:
    print(f"SkillRouter err: {e}")

OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f"OK: {OUT} ({OUT.stat().st_size} bytes)")
```

## File: tools\save_session_memory.py
```
"""
save_session_memory.py â€” Auto-save session summary to LTM (Long-Term Memory)
Gá»i cuá»‘i má»—i phiên lÃ m viá»‡c Ä‘á»ƒ lÆ°u ký á»©c vÄ©nh viá»…n vÃ o MemoryCore.
Usage:
  python save_session_memory.py "Tóm táº¯t phiên: hoÃ n thÃ nh X, Y, Z"
  python save_session_memory.py --from-blackboard  (auto-read from blackboard.json)
"""
import os
import sys
import json
import warnings
warnings.filterwarnings("ignore")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
BB_PATH = os.path.join(ROOT, "brain", "memory", "blackboard.json")

sys.path.insert(0, ROOT)
from core.ops.scripts.memory_daemon import MemoryCore

def save_text(text, user_id="CEO", agent_id="antigravity"):
    core = MemoryCore()
    result = core.add_fact(text, user_id=user_id, agent_id=agent_id)
    print(f"[âœ“] LTM saved: {text[:80]}...")
    return result

def save_from_blackboard():
    try:
        with open(BB_PATH, 'r', encoding='utf-8-sig', errors='replace') as f:
            bb = json.load(f)

        facts = []

        # Extract active_campaign
        campaign = bb.get("active_campaign")
        if campaign:
            facts.append(f"OmniClaw Ä‘ang á»Ÿ campaign: {campaign}")

        # Extract last_session summary
        last_session = bb.get("last_session", {})
        if last_session:
            ts = last_session.get("timestamp", "unknown")
            summary = last_session.get("summary", "")
            if summary:
                facts.append(f"Phiên lÃ m viá»‡c {ts}: {summary}")

        # Extract open_items
        open_items = bb.get("open_items", [])
        if open_items:
            titles = []
            for item in open_items[:5]:
                if isinstance(item, dict):
                    titles.append(item.get("title", str(item)[:50]))
                else:
                    titles.append(str(item)[:50])
            facts.append(f"Viá»‡c tá»“n Ä‘á»ng: {'; '.join(titles)}")

        # Extract corp status
        status = bb.get("system_status", "")
        cycle = bb.get("active_campaign", "")
        if status:
            facts.append(f"System status: {status} | Campaign: {cycle}")

        if facts:
            core = MemoryCore()
            for fact in facts:
                core.add_fact(fact, user_id="CEO", agent_id="postprocess")
                print(f"  [+] {fact[:80]}")
            print(f"[âœ“] Saved {len(facts)} memory nodes from blackboard")
        else:
            print("[~] No facts to extract from blackboard")

    except Exception as e:
        print(f"[!] Failed to read blackboard: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: save_session_memory.py <text> | --from-blackboard")
        sys.exit(1)

    if sys.argv[1] == "--from-blackboard":
        save_from_blackboard()
    else:
        text = " ".join(sys.argv[1:])
        save_text(text)
```

## File: tools\_DIR_IDENTITY.md
```
---
id: tools_domain
name: Tools
path: ecosystem/workforce/system/education/archivist/tools
type: directory_identity
---

# Tools

Storage area for tools.
(Auto-generated identity tag by OMA v2.1)

```


