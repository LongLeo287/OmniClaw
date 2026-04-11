import os
from pathlib import Path
import re

ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))

RENAMES = [
    # (old_subpath, new_name)
    ("brain/shared-context/OMNICLAW_BOT_POLICY.md", "OMNICLAW_BOT_POLICY.md"),
    ("brain/shared-context/OMNICLAW_IDENTITY.md", "OMNICLAW_IDENTITY.md"),
    ("brain/shared-context/corp/proposals/PROP_2026-03-22_AOS_CLI.md", "PROP_2026-03-22_OMNICLAW_CLI.md"),
    ("ecosystem/workflows/omniclaw-orchestrator.md", "omniclaw-orchestrator.md"),
    ("ecosystem/workflows/omniclaw-startup.md", "omniclaw-startup.md"),
    ("core/automations/daemons/auto_sync_omniclaw.ps1", "auto_sync_omniclaw.ps1"),
    ("core/infra/cli/omniclaw.ps1", "omniclaw.ps1"),
    ("core/infra/mcp/servers/omniclaw-workspace", "omniclaw-workspace"),
    ("core/ops/omniclaw_orchestrator.py", "omniclaw_orchestrator.py"),
    ("core/ops/omniclaw_startup.py", "omniclaw_startup.py"),
    ("core/ops/scripts/omniclaw_code_polisher.py", "omniclaw_code_polisher.py"),
    ("core/ops/scripts/omniclaw_context_injector.py", "omniclaw_context_injector.py"),
    ("core/ops/scripts/omniclaw_deep_cleaner.py", "omniclaw_deep_cleaner.py"),
    ("core/ops/scripts/omniclaw_path_fixer.py", "omniclaw_path_fixer.py"),
    ("core/ops/scripts/omniclaw.py", "omniclaw.py"),
    ("core/ops/scripts/omniclaw_integrate.py", "omniclaw_integrate.py"),
    ("core/ops/scripts/omniclaw_start.py", "omniclaw_start.py"),
    ("core/ops/scripts/audit_omniclaw.py", "audit_omniclaw.py"),
    ("core/ops/tools/omniclaw.js", "omniclaw.js"),
    ("core/telemetry/logs/mcp-omniclaw-workspace.log", "mcp-omniclaw-workspace.log"),
]

# For directories that need renaming, rename the dir itself (after its contents if any exist inside)
# Wait, omniclaw_bot dir has a YAML inside it
DIR_RENAMES = [
    ("ecosystem/workforce/agents/omniclaw_bot/omniclaw_bot-agent.yaml", "omniclaw_bot-agent.yaml"),
    ("ecosystem/workforce/agents/omniclaw_bot", "omniclaw_bot"),
]

for p, new_name in RENAMES + DIR_RENAMES:
    target = ROOT / p
    if target.exists():
        target.rename(target.parent / new_name)

# Now, go through the code globally to fix any occurrence of these old names in text
TEXT_REPLACEMENTS = {
    "OMNICLAW_BOT_POLICY": "OMNICLAW_BOT_POLICY",
    "OMNICLAW_IDENTITY": "OMNICLAW_IDENTITY",
    "omniclaw-orchestrator": "omniclaw-orchestrator",
    "omniclaw-startup": "omniclaw-startup",
    "omniclaw_bot": "omniclaw_bot",
    "auto_sync_omniclaw": "auto_sync_omniclaw",
    "omniclaw.ps1": "omniclaw.ps1",
    "omniclaw-workspace": "omniclaw-workspace",
    "omniclaw_orchestrator": "omniclaw_orchestrator",
    "omniclaw_startup": "omniclaw_startup",
    "omniclaw_code_polisher": "omniclaw_code_polisher",
    "omniclaw_context_injector": "omniclaw_context_injector",
    "omniclaw_deep_cleaner": "omniclaw_deep_cleaner",
    "omniclaw_path_fixer": "omniclaw_path_fixer",
    "omniclaw.py": "omniclaw.py",
    "omniclaw_integrate": "omniclaw_integrate",
    "omniclaw_start": "omniclaw_start",
    "audit_omniclaw": "audit_omniclaw",
    "omniclaw.js": "omniclaw.js"
}

def replace_in_file(filepath):
    try:
        content = filepath.read_text(encoding='utf-8')
        new_content = content
        for k, v in TEXT_REPLACEMENTS.items():
            new_content = new_content.replace(k, v)
        if new_content != content:
            filepath.write_text(new_content, encoding='utf-8')
    except Exception:
        # Ignore binary or read errors
        pass

for root, dirs, files in os.walk(ROOT):
    if '.git' in root or '__pycache__' in root or '.venv' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.py', '.md', '.ps1', '.json', '.yaml', '.yml', '.js', '.bat', '.txt', '.env')):
            replace_in_file(Path(root) / f)

print("Renaming and text replacement successful!")