---
id: clone_security_protocol
type: system_rule
registered: true
---

# Clone Security Protocol (CSP)
**Version:** 2.0  
**Authority:** OSF (OmniClaw Sandbox Firewall Daemon)
**Enforcement Level:** MANDATORY — No exceptions.

---

## DIRECTIVE
Before cloning ANY external repository into `$OMNICLAW_ROOT`:
1. **Intake Queue:** ALL repos MUST be cloned by OIW into `$OMNICLAW_ROOT/vault/tmp/<repo-name>` FIRST.
2. **OSF Scan:** The OSF Daemon must inspect the repository for API key leaks, known IOCs (from `global_blacklist.md`), and embedded binaries.
3. **Release:** Only after a PASS result from OSF may the OAP daemon move the content into the `brain/knowledge` or `ecosystem/` working instances.

---

## Step-by-Step Pre-Clone Vetting

### STAGE 1: Visual Metric Analysis (By Agent)

Before invoking OIW to `git clone`, the instructed Agent must inspect the repo visually:

| Check | Pass Condition | Red Flag |
|-------|---------------|----------|
| Stars | > 50 preferred | < 10 stars + no known author = suspicious |
| Last Commit | Active (< 1 year) | Abandoned repo with sudden new commit |

### STAGE 2: The OSF Execution Sandbox

Any execution of `npm install`, `pip install`, or `make` inside a newly cloned repository MUST be executed via a sandboxed worker, never strictly in the core `$OMNICLAW_ROOT/core/` daemon space. 
If an Agent tries to execute an unfamiliar Makefile or script outside of `vault/tmp/`, OSF will forcibly block the execution.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
