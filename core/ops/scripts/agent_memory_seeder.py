import os
import re
from datetime import datetime

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ROADMAP_PATH = os.path.join(ROOT, "brain", "memory", "ROADMAP.md")
AGENT_MEMORY_DIR = os.path.join(ROOT, "brain", "memory", "corp_memory", "agents")

AGENT_TEMPLATE = """---
id: {agent_slug}_memory
type: corp_document
registered: true
---

# Agent Task Memory (Long-term System B)

## [{date}] — Task: System Initialization
**Context:** Bootstrapped by OA Seeding Routine during Phase 1 Hardening.
**Outcome:** SUCCESS 
**Key lesson:** Memory frameworks are successfully mapped via OMA.
**Next time:** Await dispatch commands via Neural Bus and OHD.
**Current blockers:** None
"""

def sluggify(text):
    return re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')

def run_seeder():
    if not os.path.exists(ROADMAP_PATH):
        print("ROADMAP.md not found!")
        return

    print("[OA SEEDER] Harvesting Agents from ROADMAP.md...")
    with open(ROADMAP_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|')
    matches = pattern.findall(content)

    today = datetime.now().strftime("%Y-%m-%d")
    count = 0

    os.makedirs(AGENT_MEMORY_DIR, exist_ok=True)

    for match in matches:
        dept, agent, workers, status = [m.strip() for m in match]
        if "Dept" in dept or set(dept) == {'-'}: continue

        num_workers = int(workers)
        
        # 1. Create Head Agent Memory
        head_slug = sluggify(agent)
        path_head = os.path.join(AGENT_MEMORY_DIR, f"{head_slug}.md")
        with open(path_head, "w", encoding="utf-8") as f:
            f.write(AGENT_TEMPLATE.format(agent_slug=head_slug, date=today))
        count += 1
        
        # 2. Create Sub-Worker Agent Memories
        dept_slug = sluggify(dept).replace('-', '_')
        for i in range(1, num_workers):
            worker_slug = f"{dept_slug}_worker_{i}"
            path_worker = os.path.join(AGENT_MEMORY_DIR, f"{worker_slug}.md")
            with open(path_worker, "w", encoding="utf-8") as f:
                f.write(AGENT_TEMPLATE.format(agent_slug=worker_slug, date=today))
            count += 1
            
        print(f" -> Generated 1 Head Agent and {num_workers-1} generic workers for {dept}")

    print(f"\n[SUCCESS] OA Seeder populated {count} distinct Agent Memories!")

if __name__ == "__main__":
    run_seeder()
