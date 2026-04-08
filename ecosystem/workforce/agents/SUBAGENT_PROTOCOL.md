# SUBAGENT PROTOCOL (V3.0 - Zero Trust Edition)
# Version: 3.0 | Owner: OmniClaw OER Registry & OBD Harbor
# Purpose: OmniClaw Autonomous Pipeline rules for dynamic sub-agent spawning

## Rule 1: No Inherited Context (Strict Amnesia)
Sub-agents do NOT inherit parent context. They spawn with zero memory.
**Mandatory Args**: `task_id`, `workspace_path`, `acceptance_criteria`, `files_to_read`

## Rule 2: Least Privilege Tooling (Pillar of Security)
Sub-agents must explicitly declare the minimal tools required.
If the parent possesses shell execution but the sub-task is purely analysis, the sub-agent MUST NOT be granted shell privileges.

## Rule 3: Time-to-Live (TTL) & Token Boundaries
All dynamic instances must carry an execution limit to prevent resource starvation.
- **TTL Constraint**: Enforce `max_tokens` or `timeout_seconds`.
- **Harbor Override**: OBD Harbor will aggressively terminate any sub-agent exceeding its granted budget.

## Rule 4: Circuit Breaker & Quarantine Routing
- **Failure 1**: Attempt alternative heuristic path.
- **Failure 2**: Set blackboard status to `BLOCKED`. Immediately package all tainted workspace artifacts and route them to `vault/tmp/quarantine/`. Notify OSF Warden for sandbox clearance.

## Rule 5: OER Ephemeral Passport
Before execution, every spawned sub-agent must request an ephemeral PID from `OER Registry`. Unmapped (invisible) sub-agents will be purged by OMA Architect.

## Rule 6: Telemetry Receipt
Before death, emit a mandatory end-to-end trace.
**Path**: `telemetry/receipts/<dept>/<task_id>_<timestamp>.json`
