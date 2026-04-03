#!/usr/bin/env python3
"""
OMNICLAW CORE DAEMONS  TRUST MATRIX v2.0
==========================================
Single Source of Truth for all Paths, Roles, and Pipeline
of 5 Core Daemons. Every Daemon imports this module.

Constitution: RULE-ARCH-01-DAEMONS.md + RULE-ARCH-02-FILESYSTEM.md
"""
import os

AIOS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

# [System log: Legacy non-English comment removed]
# STANDARD LOCATION MAP (CORRECTED BY OMA)
# [System log: Legacy non-English comment removed]
class PATHS:
    # VAULT/TMP - Volatility zone
    SANDBOX         = "vault/tmp/sandbox_env"
    OA_WORKSHOP     = "vault/tmp/sandbox_env/OA_workshop"
    QUARANTINE      = "vault/tmp/quarantine"
    RAW_DUMPS       = "vault/tmp/raw_knowledge_dumps"
    OHD_CLINIC      = "vault/tmp/ohd_clinic"

    # STATE QUEUES - Mailboxes transferred between Daemons
    OIW_INBOX       = "vault/tmp/state_queues/OIW_INBOX"
    OHD_TRIGGER     = "vault/tmp/state_queues/OHD_TRIGGER"
    OER_INBOX       = "vault/tmp/state_queues/OER_INBOX"
    OA_FINAL_CHECK  = "vault/tmp/state_queues/OA_FINAL_CHECK"
    OA_DISPATCH     = "vault/tmp/state_queues/OA_DISPATCH_QUEUE"

    # VAULT ASSETS
    ASSETS_MEDIA    = "vault/assets/media"
    ASSETS_DATA     = "vault/assets/data"
    ASSETS_DB       = "vault/assets/databases"
    ARCHIVES        = "vault/archives"
    DEAD_LETTERS    = "vault/archives/dead_letters"
    STUB_AGENTS     = "vault/archives/stub_agents"
    MODELS          = "vault/models"

    # BRAIN - Region of Knowledge
    KNOWLEDGE       = "brain/knowledge"
    RULES           = "brain/rules"
    REGISTRY        = "brain/registry"
    MEMORY          = "brain/memory"
    SYSTEM_MAP      = "brain/registry/OMA_SYSTEM_MAP.json"
    FAST_INDEX      = "brain/registry/FAST_INDEX.json"
    SKILL_REGISTRY  = "brain/registry/SKILL_REGISTRY.json"   # Maintained by oer_register.py
    HANDOFF_LOG     = "brain/registry/handoff_tasks.log"
    CLI_LOG         = "brain/registry/cli_run.log"

    # SHARED CONTEXT - blackboard / AGENTS / activation
    BLACKBOARD      = "brain/shared-context/blackboard.json"
    AGENTS_ROSTER   = "brain/shared-context/AGENTS.md"
    ACTIVATION      = "brain/agents/activation_status.json"

    # ECOSYSTEM - Skill Area
    SKILLS          = "ecosystem/skills"
    PLUGINS         = "ecosystem/plugins"
    WORKFLOWS       = "ecosystem/workflows"
    WORKFORCE       = "ecosystem/workforce"
    TOOLS           = "ecosystem/tools"

    # [System log: Legacy non-English comment removed]
    STAMP_OHD       = ".OHD_CLEAN"
    STAMP_OA        = ".OA_APPROVED"

    # TELEMETRY
    RECEIPTS        = "core/telemetry/receipts"
    QA_RECEIPTS     = "core/telemetry/qa_receipts"

# [System log: Legacy non-English comment removed]
# 5-DAEMONS DISTRIBUTED MATRIX
# [System log: Legacy non-English comment removed]
TRUST_MATRIX = {

    "OMA": {
        "role": "Map Master  Chief Architect",
        "description": "Designs and maintains spatial order across the entire system. Creates _DIR_IDENTITY.md. Quarantines stray files.",
        "action_rule": "IRON RULE: Move Only  Strictly No Delete",
        "can_read":    ["*"],
        "can_write":   [PATHS.SYSTEM_MAP, PATHS.QUARANTINE, PATHS.STUB_AGENTS],
        "can_create_folders": ["*"],  # OMA is the only daemon allowed to create folders
        "can_write_identity": ["*"],  # OMA creates _DIR_IDENTITY.md for the entire system
        "strictly_denied": [],        # No read restrictions, but cannot modify file contents
        "handoff_to": ["OHD", "OA"],
        "triggers": ["scheduled_deepscan", "startup"],
    },

    "OIW": {
        "role": "Intake Workflow - The Hunter",
        "description": "Fetch remote data (Git, Web, API). Isolate/process roughly within sandbox. Place into quarantine or raw_dumps.",
        "action_rule": "Post-fetch routing to designated nodes only. Do not penetrate deeper into Brain without authorization.",
        "can_read":    [PATHS.SANDBOX, PATHS.OIW_INBOX, PATHS.SYSTEM_MAP],
        "can_write":   [PATHS.SANDBOX, PATHS.QUARANTINE, PATHS.RAW_DUMPS],
        "strictly_denied": [PATHS.KNOWLEDGE, PATHS.RULES, PATHS.REGISTRY,
                            PATHS.SKILLS, PATHS.PLUGINS, PATHS.WORKFORCE, "core"],
        "handoff_to": ["OHD"],  # Signal qua OHD_TRIGGER sau khi xong
        "triggers": [PATHS.OIW_INBOX, "manual_call"],
    },

    "OHD": {
        "role": "Health Daemon - System Medic & Patrol",
        "description": "Heal files/folders system-wide. Route stray files to correct locations based on OMA map. NO deletion authority. Auto-triggers on errors.",
        "action_rule": "DO NOT DELETE. Heal or route to correct location. Automatically intercept all unhealthy flows.",
        "can_read":    ["*"],
        "can_write":   [PATHS.QUARANTINE, PATHS.OA_FINAL_CHECK, PATHS.OA_DISPATCH, PATHS.OER_INBOX, PATHS.OHD_CLINIC],
        "can_move":    ["*"],  # Allow moving files to correct destinations based on OMA map
        "strictly_denied": ["core", PATHS.RULES],
        "handoff_to": ["OER", "OA"],
        "triggers": [PATHS.OHD_TRIGGER, "filesystem_event", "error_detected"],
        "autonomous": True,  # OHD activates autonomously without explicit calls
    },

    "OER": {
        "role": "Ecosystem Registrar - The Archivist",
        "description": "Receive clean files from OER_INBOX. Register (ID/tag/type). Distribute to brain/ecosystem. Update local _DIR_IDENTITY.md. Broadcast updates to OIW.",
        "action_rule": "Content generation strictly prohibited. Exclusively handle registry, distribution, and archival updates.",
        "can_read":    ["*"],
        "can_write":   [PATHS.OER_INBOX, PATHS.KNOWLEDGE, PATHS.SKILLS,
                        PATHS.PLUGINS, PATHS.WORKFLOWS, PATHS.WORKFORCE,
                        PATHS.FAST_INDEX, PATHS.OIW_INBOX],
        "can_update_identity": [PATHS.KNOWLEDGE, PATHS.SKILLS, PATHS.PLUGINS,
                                 PATHS.WORKFLOWS, PATHS.WORKFORCE],
        "strictly_denied": ["core"],
        "handoff_to": ["OA"],  # Complex files needing verdict
        "triggers": [PATHS.OER_INBOX],
    },

    "OA": {
        "role": "Academy Auditor - The Supreme Elder",
        "description": "Highest authority among the 5 Daemons. Extract knowledge from raw data. Create agents/skills/plugins/workflows. Provide verdicts on anomalies. Output always routes through OER registrar before entering ecosystem.",
        "action_rule": "Supreme authority bound by strict pipeline compliance. Output -> OER_INBOX first. Bypassing the registry is forbidden.",
        "can_read":    ["*"],
        "can_write":   [PATHS.OA_WORKSHOP, PATHS.OER_INBOX, PATHS.RULES,
                        PATHS.OA_DISPATCH, PATHS.HANDOFF_LOG, PATHS.QUARANTINE, PATHS.DEAD_LETTERS],
        "strictly_denied": ["core/daemons"],  # Cannot self-modify Daemon source code
        "handoff_to": ["OER"],
        "triggers": [PATHS.OA_DISPATCH, PATHS.RAW_DUMPS, "manual_call"],
        "authority_level": "SUPREME",  # Supreme verdict authority on conflicts
    },

    "OBD": {
        "role": "OmniClaw Bridge Daemon - The Harbor Master",
        "description": "Port supervisor and border patrol. Manages lifecycle of 8000 (FastAPI), 9621 (LightRAG), 5055 (Notebook), and Telegram bridges. Kills zombie processes.",
        "action_rule": "Maintain communication ports. Auto-recover closed connections. Report fatal drops to OHD_TRIGGER.",
        "can_read":    ["*"],
        "can_write":   [PATHS.OHD_TRIGGER, PATHS.RECEIPTS],
        "strictly_denied": [PATHS.RULES, "vault/models"],
        "handoff_to": ["OHD"],
        "triggers": ["startup", "port_crash_detected"],
        "autonomous": True, 
    },
}

# [System log: Legacy non-English comment removed]
# RUNTIME UTILITIES
# [System log: Legacy non-English comment removed]
def authenticate_daemon(daemon_name: str) -> dict:
    """Starts the Daemon and returns its configuration from the Trust Matrix."""
    if daemon_name not in TRUST_MATRIX:
        raise ValueError(f" UNKNOWN DAEMON: '{daemon_name}' is not in Trust Matrix!")
    cfg = TRUST_MATRIX[daemon_name]
    print(f"\033[92m[OK]\033[0m [{daemon_name}] Authenticated - Role: {cfg['role']}")
    return cfg


def assert_write_access(daemon_name: str, target_path: str) -> bool:
    """
    Check if the Daemon has Write permission for the target_path.
    Returns True if permitted, False if violated.
    """
    cfg = TRUST_MATRIX.get(daemon_name)
    if not cfg:
        print(f"\033[91m[ERR]\033[0m [TRUST-MATRIX] Unknown daemon: {daemon_name}")
        return False

    rel = os.path.relpath(target_path, AIOS_ROOT).replace("\\", "/")

    # Check the banned list first
    for denied in cfg.get("strictly_denied", []):
        if denied != "*" and rel.startswith(denied):
            print(f"\033[91m[ERR]\033[0m [TRUST-MATRIX] VIOLATION: {daemon_name} tried to write to '{rel}' - FORBIDDEN: {denied}")
            return False

    # Check the whitelist
    for allowed in cfg.get("can_write", []):
        if allowed == "*" or rel.startswith(allowed):
            return True

    print(f"\033[93m[WARN]\033[0m [TRUST-MATRIX] {daemon_name} wrote outside bounds: '{rel}'")
    return False


def get_handoff_targets(daemon_name: str) -> list:
    """Returns the list of next Daemons in the pipeline."""
    return TRUST_MATRIX.get(daemon_name, {}).get("handoff_to", [])


def abs_path(*relative_parts) -> str:
    """Create absolute path from AIOS_ROOT."""
    return os.path.join(AIOS_ROOT, *relative_parts)
