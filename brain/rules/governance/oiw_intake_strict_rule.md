---
id: oiw_intake_strict_rule
type: system_rule
registered: true
---

# OIW STRICT INTAKE & LIBRARY RULES

> [!CAUTION]
> **Authority:** OA (Academy Daemon)
> **Targets:** OmniClaw Intake Workflow (OIW)
> **Severity:** FATAL (CRITICAL SYSTEM INTEGRITY)

This document contains the absolute mandates for handling external code intake via the OIW Pipeline.

---

## 🛑 MANDATES FOR OMNICLAW INTAKE WORKFLOW (OIW)

1. **Blind Harvester:** OIW is strictly a data harvester. It is BANNED from independently executing `git clone` straight into the production zones.
2. **The Quarantine Drop:** OIW MUST dump all parsed raw data, scraped HTML, and cloned repositories into `$OMNICLAW_ROOT/vault/tmp/`. It is not allowed to place any file directly into `brain/` or `ecosystem/`.
3. **Loss of Registration Rights:** As of v5.0, OIW does not have the power to index skills. It must hand over the relay baton to OAP and OER for processing.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
