import os
import shutil
from datetime import datetime

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
# According to earlier processing, solid deduplicated repos are inside RAW_DUMPS
RAW_DUMPS = os.path.join(ROOT, 'vault', 'tmp', 'raw_knowledge_dumps')
SKILLS_DIR = os.path.join(ROOT, 'ecosystem', 'skills')
PLUGINS_DIR = os.path.join(ROOT, 'ecosystem', 'plugins')
KNOWLEDGE_REPOS = os.path.join(ROOT, 'brain', 'knowledge', 'repos')

# Targets for Batch 04
TARGETS = [
    {
        'id': 'superagi_toolkit',
        'folder_match': 'superagi',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: SuperAGI Toolkit
description: Autonomous Framework Execution Pipeline Toolkit
tier: 1
category: autonomous-agent
department: engineering
status: active
source: Batch 04 (Vetting)
tags: [agent, framework, execution, superagi]
ingested: {date}
---

# SuperAGI Toolkit

> Empower OmniClaw with the advanced execution loops and tool scheduling borrowed from SuperAGI.

## OmniClaw Usage
Use this toolkit as a reference model whenever creating autonomous task-scheduling pipelines.

## Capabilities
- Tool Provisioning Mechanism
- Resource Scheduling
- Concurrent Agent Tasking
"""
    },
    {
        'id': 'agentops_telemetry',
        'folder_match': 'agentops',
        'type': 'skill',
        'dir': SKILLS_DIR,
        'yaml': """---
name: AgentOps Telemetry
description: AI Observability and Telemetry integration
tier: 2
category: monitoring
department: infra
status: active
source: Batch 04 (Vetting)
tags: [observability, metrics, log, tracking]
ingested: {date}
---

# AgentOps Telemetry

> Observability framework to monitor cost, latency, and hallucinations across all agents.

## OmniClaw Usage
Use these patterns to wrap all LLM calls inside `AgentOpsTracker` for comprehensive billing and token monitoring.
"""
    },
    {
        'id': 'git_mcp',
        'folder_match': 'git_mcp',
        'type': 'plugin',
        'dir': PLUGINS_DIR,
        'yaml': """---
name: Git MCP Server
description: Standard Model Context Protocol Server for Git/Github integration
tier: 2
category: mcp-server
department: engineering
status: active
source: Batch 04 (Vetting)
tags: [mcp, git, github, source-control]
ingested: {date}
---

# Git MCP Server

> Direct interface for OmniClaw Agents to execute git clone, commit, push, and PRs autonomously.

## OmniClaw Usage
This plugin provides direct functional MCP bridges. 
Register via `mcp_registry` to expose these endpoints to the LLM context.
"""
    },
    {
        'id': 'notebooklm_mcp',
        'folder_match': 'notebooklm',
        'type': 'plugin',
        'dir': PLUGINS_DIR,
        'yaml': """---
name: NotebookLM MCP
description: Localized RAG and Notebook injection via MCP
tier: 3
category: mcp-server
department: rd
status: active
source: Batch 04 (Vetting)
tags: [mcp, notebooklm, local-rag, data-injection]
ingested: {date}
---

# NotebookLM MCP

> Expose targeted local document clusters directly to the LLM agent via MCP endpoints.

## OmniClaw Usage
Useful for quickly analyzing specific PDF/MD bundles without loading them into the global LightRAG cache.
"""
    },
    {
        'id': 'n8n_atom_nodes',
        'folder_match': 'n8n',
        'type': 'knowledge',
        'dir': KNOWLEDGE_REPOS,
        'yaml': """---
name: N8N Atom Workflow
description: Custom nodes and automation references for enterprise workflows
tier: 2
category: workflow
department: operations
status: active
source: Batch 04 (Vetting)
tags: [n8n, workflow, automation, trigger]
ingested: {date}
---

# N8N Atom Workflow Concepts

> Extensive library of workflow patterns to automate triggers.

## OmniClaw Usage
Reference these nodes when configuring internal CI/CD or Agent event-driven triggers.
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
    
    # Ensure dest folders exist
    os.makedirs(SKILLS_DIR, exist_ok=True)
    os.makedirs(PLUGINS_DIR, exist_ok=True)
    os.makedirs(KNOWLEDGE_REPOS, exist_ok=True)
    
    # Map matched folders
    matched = {}
    if os.path.exists(RAW_DUMPS):
        for d in os.listdir(RAW_DUMPS):
            fp = os.path.join(RAW_DUMPS, d)
            if not os.path.isdir(fp): continue
            dl = d.lower()
            for t in TARGETS:
                if t['folder_match'] in dl:
                    if t['id'] not in matched:
                        matched[t['id']] = fp

    # Also check CIV in case they are still there
    civ_dir = os.path.join(ROOT, 'brain', 'knowledge', 'CIV')
    if os.path.exists(civ_dir):
         for d in os.listdir(civ_dir):
            fp = os.path.join(civ_dir, d)
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
        
        # Write SKILL/README
        doc_name = 'SKILL.md' if t['type'] != 'knowledge' else 'README.md'
        file_path = os.path.join(target_dir, doc_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(t['yaml'].replace('{date}', date_str))
            
        # Add Identity
        ident_path = os.path.join(target_dir, '_DIR_IDENTITY.md')
        with open(ident_path, 'w', encoding='utf-8') as f:
            f.write(f"---\nid: {t['id']}\ntype: {t['type']}\nregistered_by: OER\n---\n")

        print(f"✅ Extracted {t['id']} -> {target_dir}")
        
        # Trigger sweep on source
        if t['id'] in matched:
            apply_ghost_sweep(matched[t['id']])
            # If it's knowledge, we should move the remaining docs there
            if t['type'] == 'knowledge':
                pass # Already handled by keeping it in RAW_DUMPS which can be migrated later

if __name__ == '__main__':
    print("--- BATCH 04 INGESTION COMPONENT ---")
    run()
