import os
import shutil
import json
from datetime import datetime

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RAW_DUMPS = os.path.join(ROOT, "vault", "tmp", "raw_knowledge_dumps")
OER_INBOX = os.path.join(ROOT, "vault", "tmp", "state_queues", "OER_INBOX")
os.makedirs(OER_INBOX, exist_ok=True)

VIP_REPOS = {
    "recall_experimental_fetched_gh_supabase_agent_skills": {
        "new_name": "repo_supabase_agent_skills",
        "type": "skill",
        "tags": ["supabase", "agent", "database", "sql"],
        "desc": "A set of skills enabling Agents to autonomously query, mutate, and manage Supabase Postgres databases.",
        "architecture": "Contains SQL generation layers, RLS (Row Level Security) compliance modules, and API handlers. Allows OmniClaw to interact directly with cloud databases."
    },
    "nutrient_agent_skill": {
        "new_name": "repo_nutrient_agent_skill",
        "type": "skill",
        "tags": ["nutrient", "api", "specialized"],
        "desc": "A specialized skill integration package that fetches domain-specific nutrient and dietetic data.",
        "architecture": "Operates using API wrappers and JSON schema parsers tailored for the Nutrient database. Easily pluggable into OmniClaw tool registry."
    },
    "office_ui_fabric_core": {
        "new_name": "repo_office_ui_fabric_core",
        "type": "plugin",
        "tags": ["ui", "css", "microsoft", "fluent"],
        "desc": "The core CSS routing and styling framework used by Microsoft Fluent UI (Office UI Fabric).",
        "architecture": "SASS/CSS based architecture with utility tokens, grid layouts, and color palettes. Recommended for building OmniClaw's enterprise-grade UI Dashboard."
    },
    "qwen2_5_omni": {
        "new_name": "repo_qwen2_5_omni",
        "type": "knowledge",
        "tags": ["omni", "multimodal", "qwen", "alibaba"],
        "desc": "Next-generation multimodal model architecture codebase capable of processing vision and audio natively.",
        "architecture": "Transformer-based late-fusion multimodal layers. Audio codecs and Vision encoders integrated into the reasoning engine. Study this to give OmniClaw sensory capabilities."
    },
    "qwen_agent": {
        "new_name": "repo_qwen_agent",
        "type": "agent",
        "tags": ["agent", "framework", "qwen"],
        "desc": "Alibaba's official framework for building instruction-driven agent applications with Qwen models.",
        "architecture": "Modular agent graph design. Supports multi-turn memory, tool dispatching (function calling), and code execution (Code Interpreter)."
    }
}

def inject():
    print("\033[94m[INFO]\033[0m Commencing VIP Injection Pipeline...")
    count = 0
    for target, info in VIP_REPOS.items():
        # Searching for the folder (it might have FETCHED_ prefix in its name or exactly target)
        src_dir = None
        for cand in os.listdir(RAW_DUMPS):
            if cand.endswith(target) or target in cand or cand.startswith(target):
                src_dir = os.path.join(RAW_DUMPS, cand)
                break
        
        if not src_dir or not os.path.isdir(src_dir):
            print(f"\033[93m[WARN]\033[0m Could not find '{target}' in RAW_DUMPS")
            continue
            
        print(f"-> Processing VIP: {info['new_name']}")
        
        # 1. Draft DEEP_KNOWLEDGE.md
        dk_path = os.path.join(src_dir, "DEEP_KNOWLEDGE.md")
        dk_content = f"# Deep Matrix Profile: {info['new_name']}\n\n> [!NOTE]\n> Drafted manually by Senior Architect Core (VIP Batch 06 Fast-Track).\n\n## Capability Profile\n{info['desc']}\n\n## Architectural Topology\n{info['architecture']}\n"
        with open(dk_path, "w", encoding="utf-8") as f:
            f.write(dk_content)
            
        # 2. Draft _DIR_IDENTITY.md
        id_path = os.path.join(src_dir, "_DIR_IDENTITY.md")
        ts = datetime.now().isoformat()
        tags = info['tags'] + ["vip-batch-06", "system-approved"]
        id_content = f"---\nid: {info['new_name']}\ntype: {info['type']}\nowner: OA\nregistered_at: {ts}\ntags: {json.dumps(tags)}\n---\n\n# {info['new_name']}\n\n## Assimilation Report\n{info['desc']}\n\n## Application for OmniClaw\n{info['architecture']}\n"
        with open(id_path, "w", encoding="utf-8") as f:
            f.write(id_content)
            
        # 3. Rename and move to OER_INBOX
        dest_dir = os.path.join(OER_INBOX, info['new_name'])
        try:
            shutil.move(src_dir, dest_dir)
            print(f"   \033[92m[QUEUED]\033[0m Successfully moved to OER_INBOX as {info['new_name']}")
            count += 1
        except Exception as e:
            print(f"   \033[91m[ERR]\033[0m Failed to dispatch {info['new_name']}: {e}")

    print(f"\033[92m[DONE]\033[0m VIP Pipeline executed ({count}/{len(VIP_REPOS)}). OER Registry should pick them up immediately.")

if __name__ == "__main__":
    inject()
