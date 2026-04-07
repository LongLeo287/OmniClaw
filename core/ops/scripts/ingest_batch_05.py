import os
import shutil
from datetime import datetime

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RAW_DUMPS = os.path.join(ROOT, 'vault', 'tmp', 'raw_knowledge_dumps')
SKILLS_DIR = os.path.join(ROOT, 'ecosystem', 'skills')

TARGETS = [
    {
        'id': 'lightrag_engine',
        'folder_match': 'lightrag',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: LightRAG Engine
description: Graph-based Knowledge Retrieval Augmentation
tier: 1
category: memory
department: rd
status: active
tags: [rag, graphrag, retrieval, knowledge]
---

# LightRAG Engine
> Next-generation RAG leveraging graph relationships to preserve multi-hop narrative context. Let AI "remember" forever.
"""
    },
    {
        'id': 'guardrails_shield',
        'folder_match': 'guardrail',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: Guardrails Shield
description: LLM Output Validation & Safety Constraints
tier: 2
category: safety
department: security
status: active
tags: [guardrails, validation, safety, constraints]
---

# Guardrails Shield
> Prevents the agent from executing harmful bash sequences or spitting out malformed JSON.
"""
    },
    {
        'id': 'kore_memory',
        'folder_match': 'kore_memory',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: Kore Memory Architecture
description: Event-driven Episodic Agent Memory
tier: 2
category: memory
department: engineering
status: active
tags: [memory, episodic, agent-memory]
---

# Kore Memory Architecture
> Stores interactions in an episodic timeline context so agents can recall past conversations efficiently.
"""
    },
    {
        'id': 'claude_agentic_patterns',
        'folder_match': 'claude_code',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: Anthropic Claude Code Patterns
description: Core Prompt architectures and Agentic Workflows from Anthropic
tier: 1
category: framework
department: rd
status: active
tags: [claude, prompt, pattern, anthropic]
---

# Claude Code Patterns
> The absolute best-practice prompt scaffolding for coding agents. Drop this inside our MCP server definitions.
"""
    },
    {
        'id': 'whisper_flash_compute',
        'folder_match': 'insanely_fast_whisper',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: Insanely Fast Whisper
description: Real-time Audio transcription using Flash Attention
tier: 2
category: audio
department: rd
status: active
tags: [whisper, audio, asr, transcription]
---

# Whisper Flash Compute
> Enables ultra-fast speech-to-text, unlocking voice-control possibilities for OmniClaw.
"""
    }
]

def apply_ghost_sweep(target_path):
    import sys
    sys.path.append(os.path.join(ROOT, 'core', 'ops', 'scripts'))
    try:
        from ghost_sweep import sweep_directory
        print(f"Applying Ghost Sweep to {target_path}")
        sweep_directory(target_path)
    except Exception as e:
        print(f"Error applying ghost sweep: {e}")

def run():
    date_str = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(SKILLS_DIR, exist_ok=True)
    
    # Map matched folders
    matched = {}
    searched_dirs = [RAW_DUMPS, os.path.join(ROOT, 'brain', 'knowledge', 'CIV')]
    
    for search_dir in searched_dirs:
        if os.path.exists(search_dir):
            for d in os.listdir(search_dir):
                fp = os.path.join(search_dir, d)
                if not os.path.isdir(fp): continue
                dl = d.lower()
                for t in TARGETS:
                    if t['folder_match'] in dl:
                        if t['id'] not in matched:
                            matched[t['id']] = fp

    for t in TARGETS:
        # Create the skill/plugin
        target_dir = os.path.join(t['dir'], t['id'])
        os.makedirs(target_dir, exist_ok=True)
        
        file_path = os.path.join(target_dir, 'SKILL.md')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(t['yaml'])
            
        # Add Identity
        ident_path = os.path.join(target_dir, '_DIR_IDENTITY.md')
        with open(ident_path, 'w', encoding='utf-8') as f:
            f.write(f"---\nid: {t['id']}\ntype: {t['type']}\nregistered_by: OER\n---\n")

        print(f"✅ Extracted {t['id']} -> {target_dir}")
        
        if t['id'] in matched:
            apply_ghost_sweep(matched[t['id']])

if __name__ == '__main__':
    print("--- BATCH 05 INGESTION COMPONENT ---")
    run()
