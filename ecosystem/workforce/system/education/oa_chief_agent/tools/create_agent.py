#!/usr/bin/env python3
"""
create_agent.py "” OmniClaw Corp V3.1 Agent Scaffolding Tool
Path: system/ops/scripts/create_agent.py

Tá»± Ä‘á»™ng táº¡o Ä‘á»§ files cho 1 agent má»›i theo agent-auto-create.md checklist.

Usage:
  python system/ops/scripts/create_agent.py --id frontend-agent --dept engineering --tier 3
  python system/ops/scripts/create_agent.py --id data-agent --dept analytics --tier 3 --head
  python system/ops/scripts/create_agent.py --list           # [Removed legacy comment]
  python system/ops/scripts/create_agent.py --check <id>    # [Removed legacy comment]
  python system/ops/scripts/create_agent.py --check-all     # [Removed legacy comment]
"""

import json
import sys
import shutil
import yaml
import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent  # system/ops/scripts -> system/ops -> system -> OmniClaw root
TEMPLATE_DIR = ROOT / "ecosystem" / "workforce" / "agents" / "_template"
AGENTS_DIR   = ROOT / "ecosystem" / "workforce" / "agents"
WORKFORCE    = ROOT / "ecosystem" / "workforce" / "agents"
ORG_CHART    = ROOT / "brain" / "corp" / "org_chart.yaml"
AGENTS_MD    = ROOT / "brain" / "shared-context" / "AGENTS.md"
REGISTRY     = ROOT / "brain" / "shared-context" / "SKILL_REGISTRY.json"
LIBRARY_GRAPH = ROOT / "brain" / "knowledge" / "LIBRARY_GRAPH.json"
MEMORY_DIR   = ROOT / "brain" / "corp" / "memory" / "agents"
DEPT_DIR     = ROOT / "ecosystem" / "workforce" / "departments"
RECEIPT_DIR  = ROOT / "system" / "telemetry" / "receipts" / "agent_onboard"

# Colors
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
C = "\033[96m"
B = "\033[1m"
X = "\033[0m"

def now():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()

def today():
    return datetime.date.today().isoformat()

# [System log: Legacy non-English comment removed]
def required_files(agent_id: str, is_head: bool = False):
    files = [
        AGENTS_DIR / agent_id / "AGENT.md",
        MEMORY_DIR / f"{agent_id}.md",
        RECEIPT_DIR / f"{agent_id}.json",
    ]
    if is_head:
        dept = agent_id.replace("-agent","").replace("_agent","")
        files += [
            DEPT_DIR / dept / "MANAGER_PROMPT.md",
            DEPT_DIR / dept / "WORKER_PROMPT.md",
            DEPT_DIR / dept / "rules.md",
        ]
    return files

def check_agent_profile(agent_id: str) -> dict:
    """Check if agent has all required files. Returns status report."""
    agent_dir  = AGENTS_DIR / agent_id
    brain_md   = agent_dir / "AGENT.md"
    mem_file   = MEMORY_DIR / f"{agent_id}.md"
    receipt    = RECEIPT_DIR / f"{agent_id}.json"
    workforce_dir = WORKFORCE / agent_id

    results = {
        "agent_id": agent_id,
        "ecosystem/workforce/agents/AGENT.md":    brain_md.exists(),
        "memory file":               mem_file.exists(),
        "onboard receipt":           receipt.exists(),
        "workforce folder":          workforce_dir.exists(),
        "in AGENTS.md":             False,
        "in org_chart":             False,
    }

    # Check AGENTS.md
    if AGENTS_MD.exists():
        content = AGENTS_MD.read_text(encoding="utf-8", errors="ignore")
        results["in AGENTS.md"] = agent_id in content

    # Check org_chart
    if ORG_CHART.exists():
        content = ORG_CHART.read_text(encoding="utf-8", errors="ignore")
        results["in org_chart"] = agent_id in content

    total = sum(1 for v in results.values() if isinstance(v, bool) and v)
    possible = sum(1 for v in results.values() if isinstance(v, bool))
    results["score"] = f"{total}/{possible}"
    results["complete"] = total == possible

    return results

def register_to_library_graph(agent_id: str, dept: str, tier: int):
    """Register the new agent as a node in the Central Library Graph."""
    if not LIBRARY_GRAPH.exists():
        print(f"  {Y}⚠️{X}  LIBRARY_GRAPH.json not found. Run library_manager indexer first.")
        return
    try:
        data = json.loads(LIBRARY_GRAPH.read_text(encoding="utf-8", errors="ignore"))
        nodes = data.get("nodes", [])
        edges = data.get("edges", [])
        
        node_id = f"AGENT-{agent_id}"
        
        for n in nodes:
            if n.get("id") == node_id:
                print(f"  {Y}⚠️{X}  Agent node '{node_id}' already in LIBRARY_GRAPH.json")
                return
                
        new_node = {
            "id": node_id,
            "type": "agent_node",
            "name": agent_id,
            "title": f"AGENT PROFILE: {agent_id}",
            "path": f"ecosystem/workforce/agents/{agent_id}/SKILL.md",
            "tags": ["agent", "workforce", f"tier{tier}"]
        }
        nodes.append(new_node)
        
        if dept:
            edges.append({
                "source": node_id,
                "target": f"DEPT-{dept}",
                "relationship": "belongs_to"
            })
            
        data["nodes"] = nodes
        data["edges"] = edges
        
        LIBRARY_GRAPH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  {G}✅{X} brain/knowledge/LIBRARY_GRAPH.json (Agent Node added)")
    except Exception as e:
        print(f"  {R}❌{X} Failed to update LIBRARY_GRAPH.json: {e}")

def cmd_check(agent_id: str):
    """Check one agent profile completeness."""
    r = check_agent_profile(agent_id)
    icon = G + "COMPLETE" + X if r["complete"] else Y + f"INCOMPLETE ({r['score']})" + X
    print(f"\n{B}Agent: {agent_id}{X} "” {icon}")
    for k, v in r.items():
        if isinstance(v, bool):
            status = G + "âœ…" + X if v else R + "âŒ" + X
            print(f"  {status} {k}")
    print()


def cmd_check_all():
    """Check all 99 agents from ecosystem/workforce/agents/ folder."""
    print(f"\n{B}Checking all agent profiles...{X}\n")
    complete, incomplete = [], []

    for p in sorted(AGENTS_DIR.iterdir()):
        if p.is_dir() and not p.name.startswith('_'):
            r = check_agent_profile(p.name)
            if r["complete"]:
                complete.append(p.name)
            else:
                incomplete.append((p.name, r["score"]))

    print("[OmniClaw System Event]")}):{X}")
    for a in complete:
        print(f"  "¢ {a}")

    print("[OmniClaw System Event]")}):{X}")
    for a, score in incomplete:
        print(f"  "¢ {a} "” {score} files")

    print(f"\n{B}Summary: {len(complete)}/{len(complete)+len(incomplete)} agents fully profiled{X}\n")


def cmd_list():
    """List all agents with profile status."""
    agents = sorted(p.name for p in AGENTS_DIR.iterdir() if p.is_dir() and not p.name.startswith('_'))
    print(f"\n{B}Brain Agents ({len(agents)} profiles){X}")
    for a in agents:
        has_agent_md = (AGENTS_DIR / a / "AGENT.md").exists()
        icon = "âœ…" if has_agent_md else "âŒ"
        print(f"  {icon} {a}")

    workforce = sorted(p.name for p in WORKFORCE.iterdir() if p.is_dir()) if WORKFORCE.exists() else []
    print(f"\n{B}Workforce Agents ({len(workforce)} folders){X}")
    for a in workforce:
        files = list((WORKFORCE / a).iterdir())
        print(f"  ðŸ“ {a} "” {len(files)} files: {[f.name for f in files]}")


def scaffold_agent(agent_id: str, dept: str, tier: int, is_head: bool = False, title: str = ""):
    """Scaffold all required files for a new agent."""
    print(f"\n{B}ðŸ¤– Scaffolding Agent: {agent_id}{X}")
    print(f"  Dept: {dept} | Tier: {tier} | Head: {is_head}\n")

    created = []

    # 1. ecosystem/workforce/agents/<agent_id>/AGENT.md from template
    agent_dir = AGENTS_DIR / agent_id
    agent_dir.mkdir(parents=True, exist_ok=True)
    agent_md_path = agent_dir / "AGENT.md"

    if not agent_md_path.exists():
        template = (TEMPLATE_DIR / "AGENT.md").read_text(encoding="utf-8", errors="ignore")
        filled = template \
            .replace("[Agent Name]", agent_id.replace("-", " ").title()) \
            .replace("[Short Role Description]", title or f"{dept.title()} specialist") \
            .replace("<DATE>", today()) \
            .replace("<Dept Name>", dept.title()) \
            .replace("<N>", str(tier)) \
            .replace("<2|3|4>", str(tier)) \
            .replace("<agent-id>", agent_id) \
            .replace("<dept_name>", dept) \
            .replace("<ISO8601>", now())

        agent_md_path.write_text(filled, encoding="utf-8")
        print("[OmniClaw System Event]")
        created.append(str(agent_md_path.relative_to(ROOT)))
    else:
        print("[OmniClaw System Event]")

    # 2. Memory file
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    mem_path = MEMORY_DIR / f"{agent_id}.md"
    if not mem_path.exists():
        mem_content = f"# Memory: {agent_id}\n\n## {today()} "” Initialization\nContext: Agent created via create_agent.py scaffold\nOutcome: SUCCESS\nKey lesson: Awaiting first task\nCurrent blockers: none\n"
        mem_path.write_text(mem_content, encoding="utf-8")
        print("[OmniClaw System Event]")
        created.append(str(mem_path.relative_to(ROOT)))
    else:
        print("[OmniClaw System Event]")

    # 3. Onboard receipt
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    receipt_path = RECEIPT_DIR / f"{agent_id}.json"
    if not receipt_path.exists():
        receipt = {
            "agent_id": agent_id,
            "created_by": "create_agent.py",
            "trigger": "manual-scaffold",
            "ceo_approved": True,
            "approved_at": now(),
            "strix_approved": False,
            "dept": dept,
            "tier": tier,
            "llm_tier": "economy",
            "autonomy": "supervised",
            "activation_date": now(),
            "version": "1.0",
            "note": "Scaffolded manually. Strix review pending."
        }
        receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding="utf-8")
        print("[OmniClaw System Event]")
        created.append(str(receipt_path.relative_to(ROOT)))
    else:
        print("[OmniClaw System Event]")

    # 4. Workforce folder + SKILL.md stub
    wf_dir = WORKFORCE / agent_id
    wf_dir.mkdir(parents=True, exist_ok=True)
    skill_path = wf_dir / "SKILL.md"
    if not skill_path.exists():
        skill_content = f"---\nname: {agent_id}\ndescription: {dept.title()} specialist agent\nagents: [{agent_id}]\ntier: tier{tier}\nstatus: active\nadded: {today()}\n---\n\n# {agent_id.replace('-',' ').title()}\n\nSee: ecosystem/workforce/agents/{agent_id}/AGENT.md\n"
        skill_path.write_text(skill_content, encoding="utf-8")
        print("[OmniClaw System Event]")
        created.append(str(skill_path.relative_to(ROOT)))

    # 5. Department files (if head agent)
    if is_head:
        dept_path = DEPT_DIR / dept
        dept_path.mkdir(parents=True, exist_ok=True)

        for fname, content in {
            "MANAGER_PROMPT.md": f"# Manager Prompt: {dept.title()}\n\n## Mission\n<Define dept mission>\n\n## Team\n- Head: {agent_id}\n\n## Workflow\n<Define workflow>\n\n## Brief Format\n<Define daily brief format>\n",
            "WORKER_PROMPT.md":  f"# Worker Prompt: {dept.title()}\n\n## Role Context\n<Define worker role>\n\n## Skill Loading\n<List skills to activate>\n\n## Task Ownership\n<Define task ownership>\n",
            "rules.md":          f"# Rules: {dept.title()}\n\n## Constraints\n1. <Rule 1>\n2. <Rule 2>\n\n## Escalation\n- L1: Agent self-solves\n- L2: Report to {agent_id}\n- L3: Stop + notify CEO\n",
        }.items():
            fpath = dept_path / fname
            if not fpath.exists():
                fpath.write_text(content, encoding="utf-8")
                print("[OmniClaw System Event]")
                created.append(str(fpath.relative_to(ROOT)))

        # Dept memory
        dept_mem = ROOT / "brain" / "corp" / "memory" / "departments"
        dept_mem.mkdir(parents=True, exist_ok=True)
        dept_mem_file = dept_mem / f"{dept}.md"
        if not dept_mem_file.exists():
            dept_mem_file.write_text(f"# Dept Memory: {dept.title()}\n\n## {today()} "” Initialized\nHead: {agent_id}\nStatus: Active\n", encoding="utf-8")
            print("[OmniClaw System Event]")

        # Daily brief channel
        briefs = ROOT / "brain" / "shared-context" / "corp" / "daily_briefs"
        briefs.mkdir(parents=True, exist_ok=True)
        brief_file = briefs / f"{dept}.md"
        if not brief_file.exists():
            brief_file.write_text(f"# Daily Brief: {dept.title()}\n\n## {today()}\nAgent {agent_id} activated — ready for tasks.\n", encoding="utf-8")
            print(f"  {G}✅{X} brain/shared-context/corp/daily_briefs/{dept}.md")

    # 6. Central Library Graph Insertion
    register_to_library_graph(agent_id, dept, tier)

    print(f"\n  {B}Created {len(created)} files.{X}")

    # Summary checklist
    print(f"\n  {B}Checklist:{X}")
    print("[OmniClaw System Event]")")
    print("[OmniClaw System Event]")")
    print("[OmniClaw System Event]")")
    print("[OmniClaw System Event]")
    if is_head:
        print("[OmniClaw System Event]")
        print("[OmniClaw System Event]")

    print(f"\n  {G}Agent '{agent_id}' scaffolded. Full activation requires CEO approval.{X}\n")


# [System log: Legacy non-English comment removed]
def main():
    args = sys.argv[1:]

    if not args or args[0] == "--help":
        print(f"""
{B}create_agent.py "” OmniClaw Corp Agent Scaffolding Tool{X}

Commands:
  --list                        List all agents with status
  --check <agent-id>            Check profile completeness for 1 agent
  --check-all                   Check all agents in ecosystem/workforce/agents/
  --id <id> --dept <dept> --tier <n>    Scaffold new agent
    --head                      Also create department files
    --title <title>             Agent title/description

Examples:
  python system/ops/scripts/create_agent.py --list
  python system/ops/scripts/create_agent.py --check frontend-agent
  python system/ops/scripts/create_agent.py --check-all
  python system/ops/scripts/create_agent.py --id crm-agent --dept sales --tier 3
  python system/ops/scripts/create_agent.py --id hr-manager-agent --dept hr --tier 3 --head
""")
        return

    if "--list" in args:
        cmd_list()
    elif "--check-all" in args:
        cmd_check_all()
    elif "--check" in args:
        idx = args.index("--check")
        agent_id = args[idx+1] if idx+1 < len(args) else ""
        if agent_id:
            cmd_check(agent_id)
        else:
            print("Usage: --check <agent-id>")
    elif "--id" in args:
        def get_arg(flag, default=""):
            try:
                i = args.index(flag)
                return args[i+1]
            except (ValueError, IndexError):
                return default

        agent_id = get_arg("--id")
        dept     = get_arg("--dept", "general")
        tier     = int(get_arg("--tier", "3"))
        title    = get_arg("--title", "")
        is_head  = "--head" in args

        if not agent_id:
            print("Error: --id is required")
            sys.exit(1)

        scaffold_agent(agent_id, dept, tier, is_head, title)
    else:
        print(f"{R}Unknown command. Use --help for usage.{X}")
        sys.exit(1)


if __name__ == "__main__":
    main()
