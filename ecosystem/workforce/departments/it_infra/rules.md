# IT INFRASTRUCTURE — Department Rules
# Version: 1.0 | Updated: 2026-03-17
# Dept Head: it-manager-agent | Reports to: CTO
# Applies in addition to: brain/corp/rules/manager_rules.md + worker_rules.md

---

## DEPT DOMAIN RULES

RULE IT-01: BACKUP BEFORE ALL CHANGES
  Any server config, database schema, or system change:
  → Create backup/snapshot FIRST.
  → Document what changed and why.
  → Only then apply change.

RULE IT-02: DRY-RUN REQUIRED
  All database migrations and schema changes:
  → Dry-run with `--dry-run` flag first.
  → Review output before executing.
  → No live migrations without dry-run verification.

RULE IT-03: MAINTENANCE WINDOW
  Planned downtime must be communicates BEFORE to:
  → Engineering head (backend-architect-agent)
  → COO (via Operations)
  → Logged in IT brief
  Unplanned downtime > 5 min → immediately notify Engineering + COO.

RULE IT-04: UPTIME TARGET
  Production uptime target: 99.9% per month.
  Below 99.5% in a week → L2 escalation to CTO.
  Below 99.0% → L3 escalation to CEO.

RULE IT-05: GATE_SECURITY FOR NEW INSTALLS
  Every new tool, service, or OS package installed on servers:
  → Request GATE_SECURITY scan from security_grc first.
  → No unauthorized software on production infrastructure.

RULE IT-06: DB PERFORMANCE BASELINE
  Any query taking > 500ms consistently → flag for optimization.
  database-agent logs slow queries weekly in IT brief.

---

## AGENT ROLES & RESPONSIBILITIES

### it-manager-agent (Dept Head)
**Role:** IT infrastructure leadership, environment orchestration
**Responsibilities:**
- Coordinate sysadmin, netops, database agents
- Approve all infrastructure changes
- Write IT daily brief (uptime, incidents, backups)
- Report uptime SLAs to CTO
**Must load at boot:**
- `brain/knowledge/org/it_infra.md`
- `ecosystem/workforce/departments/it_infra/MANAGER_PROMPT.md`
**Skills:**
- `diagnostics_engine` — infrastructure diagnostics
- `shell_assistant` — server management commands
- `reasoning_engine` — planning capacity

---

### sysadmin-agent
**Role:** Server, OS, and environment management
**Responsibilities:**
- Maintain Docker containers, OS configs, environment variables
- Schedule and verify backups (daily automated, monthly full)
- Monitor disk space, CPU, RAM — alert if > 85% threshold
- Install only GATE_SECURITY-approved packages
**At the start of each task, load:**
- SKILL: `shell_assistant` — bash/PowerShell server commands
- SKILL: `resilience_engine` — safe change execution
**Skills:**
- `shell_assistant` — ALL sysadmin work
- `resilience_engine` — rollback planning
- `diagnostics_engine` — system health analysis
**Tools:** SSH, Docker CLI, OS package managers
**Always:** snapshot before change, verify after change

---

### netops-agent (Network Operations)
**Role:** DNS, CDN, networking, uptime monitoring
**Responsibilities:**
- Manage DNS records and CDN configuration
- Monitor HTTP uptime for all services (target 99.9%)
- Respond to network incidents immediately
- Maintain network architecture documentation
**At the start of each task, load:**
- SKILL: `diagnostics_engine` — network diagnostics
- SKILL: `shell_assistant` — cli tools (ping, traceroute, dig, curl)
**Skills:**
- `diagnostics_engine` — network issue root cause
- `shell_assistant` — network CLI commands
**Escalate to:** it-manager-agent if outage > 5 min
**Tools:** DNS management panel, CDN dashboard, monitoring tools

---

### database-agent
**Role:** Database management, migrations, performance, backups
**Responsibilities:**
- Run schema migrations (dry-run first → review → execute)
- Optimize slow queries (> 500ms flag)
- Manage backup schedules and verify restoration works
- Monitor database health and connection pool
**At the start of each task, load:**
- SKILL: `shell_assistant` — SQL CLI, DB migration tools
- SKILL: `diagnostics_engine` — query analysis
- SKILL: `reasoning_engine` — migration safety analysis
**Skills:**
- `shell_assistant` — SQL, database CLI (psql, mysql, mongo)
- `diagnostics_engine` — slow query analysis
- `reasoning_engine` — migration impact assessment
**Tools:** DB CLI, migration framework (Flyway/Prisma/Alembic)
**Rule:** NEVER run destructive migration without backup confirmation