# ISLAND_SANDBOX_PROTOCOL.md — The Iron Curtain 
# Version: 2.0 | Updated: 2026-04-06
# Authority: Tier 1 (Security Root) — Part of AI OS Firewall

## Purpose

OmniClaw architecture must operate as a completely hermetic container (Island Sandbox). 
This protocol guarantees that **no Script, Agent, or Daemon** may read from, write to, or spawn directories outside of the designated `$OMNICLAW_ROOT` directory.
It also outlines the strict Malware Protection and File Freezing capabilities of the OSF (OmniClaw Sandbox Firewall).

## 1. Absolute Root Constraint (Warded by `osf_warden`)

All operations must be fully relative to the dynamic detection of the OmniClaw directory.

```python
# ❌ ANTI-PATTERN: Breaking the Sandbox
import os
def load_data():
    return open("C:\\User\\Desktop\\my_data.json")

def write_cache():
    os.makedirs("D:\\tmp\\omniclaw_cache", exist_ok=True)
```

```python
# ✅ CORRECT: Island Constraint adherence
import os

OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VAULT_TMP = os.path.join(OMNICLAW_ROOT, "vault", "tmp")

def write_cache():
    target = os.path.join(VAULT_TMP, "omniclaw_cache")
    os.makedirs(target, exist_ok=True)
```

## 2. Temporary Storage Routing

To ensure self-containment, all system temp routines (`/tmp` , `%TEMP%`) MUST BE EXPLICITLY OVERRIDDEN OR REROUTED into the internal `vault/tmp` queue. 

- Never use standard `tempfile.gettempdir()` blindly in Python unless you override it to point back to OmniClaw.
- Git Clones and raw mass ingestion MUST land in `vault/quarantine` or `vault/tmp`.
- Local LLM installations (e.g. HuggingFace CLI, Ollama Pulls) must direct their cache into `OmniClaw MODELS` or `.cache` inside the OS structure. Do NOT pollute `~/.ollama` or `~/.cache` globally.

## 3. The "No Ghost" Rule

If logic requires executing an external third-party binary/tool that forces write operations to external hardcoded drives (like `C:\ProgramData`), the Operation Daemon must wrap the tool, collect the artifacts dynamically, and then forcefully cleanse the external pollution post-operation.

Nothing escapes the island. Nothing stays outside the island.

## 4. Immutable Core Defense (Warded by `osf_auditor`)

Critical system files (such as `SKILL_REGISTRY.json`, `LIBRARY_GRAPH.json`, and core python scripts) MUST be capable of being locked into **Read-Only (Immutable) Mode** via the `osf_file_locker.py` tool.
No Agent or Daemon has the authority to bypass the lock without OSF override privileges. This prevents any rogue logic from erasing or altering the operating system's brain mass.

## 5. Sterile Intake (Warded by `osf_quarantine_guard`)

Before any folder or repository can leave `vault/quarantine` and enter `OER_INBOX` for distillation, it MUST undergo a Deep Vector Scan via `osf_malware_censor.py`.
Any presence of base64 evaluators, shell execution injections (`rm -rf`), or trojan payloads will result in immediate Vaporization by the Heavy Destroyer (OHD) subsystem.
