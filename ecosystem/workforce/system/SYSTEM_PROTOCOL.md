# OmniClaw System Quadrant Protocol

> [!CAUTION]
> The `ecosystem/workforce/system/` quadrant is **STRICTLY DECLARATIVE**. 

**1. No Code Execution**
This directory must not house any `.py`, `.bat`, `.ps1` executed tools or logic. All runtime tools must be pushed up to the `core/ops/` or `core/daemons/` layer.

**2. No Autonomous Agents**
Autonomous Agent clusters (`AGENT.md`, `agent.yaml`) MUST reside in `ecosystem/workforce/agents/`. This quadrant is strictly for static system configurations, global system text assets, or intake static mapping (e.g. `corp_prompts`).

**3. OA Academy Rules**
The central OA loop does NOT track this directory in its continuous 60-second array to conserve computational load. OA operations over this area are conducted strictly via **BYPASS Execution** requested directly by the Administrator.

*End of Protocol.*
