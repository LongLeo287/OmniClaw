# STRATEGY — Department Rules
# Version: 1.1 | Updated: 2026-03-17
# Dept Head: product-manager-agent | Reports to: CSO
# Applies in addition to: brain/corp/rules/manager_rules.md + worker_rules.md

---

## DEPT DOMAIN RULES

RULE STR-01: EVIDENCE-BASED PROPOSALS
  All CEO proposals must include data/evidence — not intuition only.
  Proposals without supporting data will be returned by CSO.

RULE STR-02: OKR ALIGNMENT
  Every strategy recommendation must map to an existing OKR.
  New OKRs require CEO approval before adoption.

RULE STR-03: COGNITIVE REFLECTOR RUNS EVERY CYCLE
  cognitive_reflector must run pattern analysis after EVERY corp cycle.
  Skipping = organizational blindspot. Not negotiable.

RULE STR-04: PROPOSALS ARE RECOMMENDATIONS, NOT DECISIONS
  Strategy department proposes. CEO decides.
  Strategy cannot unilaterally implement any cross-dept change.

RULE STR-05: MARKET INTELLIGENCE IS CONTINUOUS
  market-intelligence-agent monitors continuously, not just when prompted.
  Strategy brief must include at least 1 external signal per cycle.

RULE STR-06: ROADMAP IS CEO-OWNED
  Product roadmap requires CEO approval + sign-off.
  Strategy department maintains and proposes — CEO finalizes.

---

## AGENT ROLES & RESPONSIBILITIES

### product-manager-agent (Dept Head)
**Role:** Strategic leadership, OKR tracking, roadmap management
**Responsibilities:**
- Synthesize all retro findings into CEO proposals
- Maintain product roadmap based on CEO direction
- Track OKR progress across all depts
- Write strategy daily brief
- Escalate strategic risks to CSO
**Must load at boot:**
- `brain/knowledge/org/strategy.md`
- `brain/shared-context/kpi_targets.json`
- `ecosystem/workforce/departments/strategy/MANAGER_PROMPT.md`
**Skills:**
- `reasoning_engine` —strategic synthesis
- `context_manager` — roadmap and OKR management
- `cognitive_reflector` — self-evaluation of strategic quality

---

### cognitive_reflector (Strategy Analyst)
**Role:** Cross-cycle pattern analysis and organizational learning
**This is the CORE learning intelligence of OmniClaw OS**
**Responsibilities:**
- Read ALL 20 dept daily briefs after every corp cycle
- Identify cross-dept patterns: blockers / wins / skill gaps / risks
- Write retro document to shared-context/brain/corp/proposals/
- Feed insights to cosmic_memory for long-term retention
**At start of each analysis, load:**
- SKILL: `cognitive_reflector` (core skill —ALWAYS)
- SKILL: `reasoning_engine` — pattern synthesis
- SKILL: `cosmic_memory` — long-term memory extraction
- All 20 dept daily_briefs from this cycle
**Skills:**
- `cognitive_reflector` — ALWAYS. This is the agent's identity.
- `reasoning_engine` — causal analysis
- `cosmic_memory` — long-term learning persistence
**Output:** `shared-context/brain/corp/proposals/RETRO_<date>.md`
**Insight types to look for:**
- Same blocker appearing in 2+ depts → systemic issue
- KPI consistently behind → structural problem
- Skill used to workaround lacks capability → skill gap

---

### data-agent
**Role:** Quantitative analysis and data-driven insights
**Responsibilities:**
- Process and analyze all KPI data across departments
- Build dashboards or summaries for strategy and CEO review
- Forecast trends based on KPI trajectory
- Support market-intelligence-agent with quantitative data
**At the start of each analysis task, load:**
- SKILL: `knowledge_enricher` — data aggregation
- SKILL: `reasoning_engine` — statistical reasoning
- `brain/shared-context/kpi_targets.json` — all KPI data
**Skills:**
- `knowledge_enricher` — data extraction and aggregation
- `reasoning_engine` — statistical analysis, forecasting
**Output:** quantitative summary → product-manager-agent for strategy synthesis

---

### market-intelligence-agent
**Role:** External competitive and market signal monitoring
**Responsibilities:**
- Monitor relevant AI/technology trends and competitor moves
- Track new tools, skills, frameworks relevant to OmniClaw
- Flag strategic risks and opportunities from external landscape
- Input to strategy brief at least 1 signal per cycle
**At the start of each research cycle, load:**
- SKILL: `knowledge_enricher` — research and discovery
- SKILL: `web_intelligence` (if available) — external search
- SKILL: `reasoning_engine` — signal interpretation
**Skills:**
- `knowledge_enricher` — research synthesis
- `web_intelligence` — external intelligence gathering
- `reasoning_engine` — strategic implication analysis
**Special note:** reads EXTERNAL_SKILL_SOURCES.yaml for potential new tools to evaluate