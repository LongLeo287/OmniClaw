import os
import re
from datetime import datetime

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ROADMAP_PATH = os.path.join(ROOT, "brain", "memory", "ROADMAP.md")
DEPT_MEMORY_DIR = os.path.join(ROOT, "brain", "memory", "corp_memory", "departments")

# Simplified template loader, utilizing standard System B pattern.
DEPT_TEMPLATE = """---
id: {dept_id}_memory
type: corp_document
registered: true
---

# {dept_name} Memory (Long-term System B)

## Origin Generation
**Date:** {date}
**Source:** OA Seeding Routine generated from ROADMAP.md
**Current State:** {status}
**Head Agent:** {head_agent}
**Worker Count:** {workers}

## Internal Objectives & Known Patterns:
- Ensure 24/7 cross-agent reliability.
- Execute assignments via {head_agent} and report to OmniClaw Core.

## Cross-dept dependencies:
- Connected to OIW Intake and OA Academy for training.

## Lessons learned:
- Standby mode initialized successfully.
"""

def sluggify(text):
    return re.sub(r'[^a-zA-Z0-9]+', '_', text.lower()).strip('_')

def run_seeder():
    if not os.path.exists(ROADMAP_PATH):
        print("ROADMAP.md not found!")
        return

    print("[OA SEEDER] Reading ROADMAP.md...")
    with open(ROADMAP_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the table: | Dept | Head Agent | Workers | Status |
    # Extract rows:
    pattern = re.compile(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|')
    matches = pattern.findall(content)

    today = datetime.now().strftime("%Y-%m-%d")
    count = 0

    os.makedirs(DEPT_MEMORY_DIR, exist_ok=True)

    for match in matches:
        dept, agent, workers, status = [m.strip() for m in match]
        if "Dept" in dept or set(dept) == {'-'}: continue # Skip headers

        slug = sluggify(dept)
        filepath = os.path.join(DEPT_MEMORY_DIR, f"{slug}.md")
        
        md_content = DEPT_TEMPLATE.format(
            dept_id=slug,
            dept_name=dept,
            date=today,
            head_agent=agent,
            workers=workers,
            status=status
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        count += 1
        print(f" -> Memory generated for: {dept}")

    print(f"\n[SUCCESS] OA Seeder has successfully initialized {count} Department Memory Ledgers into System B!")

if __name__ == "__main__":
    run_seeder()
