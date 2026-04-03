---
id: approval_gates
type: corp_document
registered: true
---

# APPROVAL_GATES.md — Gate Checklists for All 4 Corp Gates
# Version: 1.0 | Created: 2026-03-22
# Referenced by: corp-gate-flow.md, corp-daily-cycle.md (Phase 5)
# Authority: Tier 2 (Operations) — overridden only by Tier 0-1

---

## GATE_QA — Engineering Output Checklist

**Operated by:** qa_testing dept (test-manager-agent)
**Blocks:** All code/system changes before deployment

### Checklist (ALL must pass for PASS verdict):

```
[ ] Q1  — All automated tests pass (unit + integration)
[ ] Q2  — Test coverage ≥ 70% for new code
[ ] Q3  — No hardcoded secrets, credentials, or API keys
[ ] Q4  — No obvious linting/type errors
[ ] Q5  — RULE-DYNAMIC-01 satisfied (no absolute paths in code)
[ ] Q6  — Error handling present for external calls
[ ] Q7  — No breaking changes to existing API contracts (or documented)
[ ] Q8  — Receipt written to telemetry/receipts/<dept>/<T-ID>.json
[ ] Q9  — Split-Encoding Policy satisfied: System logic uses pure ASCII/UTF-8; human Vietnamese text is strictly isolated to `*-vn.md` files encoded with UTF-8-SIG (BOM).
```

**Scoring:**
- All 9 PASS → **GATE_QA: PASS**
- Q1–Q4 fail → **GATE_QA: FAIL** (blocking — must fix before re-submit)
- Q5–Q9 fail → **GATE_QA: CONDITIONAL** (must fix within 1 cycle)

**Receipts:** `telemetry/qa_receipts/gate_qa/<T-ID>.json`

---

## GATE_CONTENT — Content Output Checklist

**Operated by:** content_review dept (editor-agent)
**Blocks:** All public-facing content before publish

### Checklist (ALL must pass for PASS verdict):

```
[ ] C1  — No spelling/grammar errors (editor-agent review)
[ ] C2  — Factual claims verified (fact-checker review)
[ ] C3  — Brand voice consistent with SOUL.md tone
[ ] C4  — No trademark/IP violations (brand-guardian review)
[ ] C5  — CTA present and correct (where applicable)
[ ] C6  — Content policy compliant — no harmful/misleading content
[ ] C7  — Target channel format correct (tweet ≠ blog ≠ email)
[ ] C8  — CEO-sensitive topics flagged for CEO review (optional publish)
```

**Team:** editor-agent (C1,C7) | fact-checker (C2) | content-moderator (C6) | brand-guardian (C3,C4,C8)
All 4 must sign off before final PASS.

**Receipts:** `telemetry/qa_receipts/gate_content/<T-ID>.json`

---

## GATE_SECURITY — Security Scan Checklist

**Operated by:** security_grc dept (strix-agent — autonomous)
**Blocks:** New plugins, skills, external repos, data egress

### SkillSentry 9-Layer Scan (automated):

```
[ ] S1  — License check: OSI-approved or compatible license
[ ] S2  — Dependency audit: no known CVEs in direct deps
[ ] S3  — No hardcoded credentials or secrets in code
[ ] S4  — No suspicious outbound network calls
[ ] S5  — No eval/exec with untrusted input (code injection vectors)
[ ] S6  — File access limited to declared scope (no unauthorized paths)
[ ] S7  — No data exfiltration patterns (unusual data sends)
[ ] S8  — Supply chain: author/repo reputation check
[ ] S9  — SOUL.md alignment: no contradictions to core values
```

**Score:** Each layer = 0 (FAIL) or 1 (PASS). Total = 0–9.

**Verdict:**
- Score 8–9 → **PASS** (≥ 60% threshold met)
- Score 5–7 → **CONDITIONAL** — quarantine watch 7 days, monitoring enabled
- Score < 5 → **BLOCK** — CEO override required to unblock
- Any S4/S7 FAIL with confirmed threat → **CRITICAL L3 escalation regardless of total score**

**Receipts:** `telemetry/qa_receipts/gate_security/<item-id>.json`

**Critical path:** strix-agent → DIRECT L3 to `shared-context/brain/corp/escalations.md` (skip L1/L2)

---

## GATE_LEGAL — Legal Review Checklist

**Operated by:** legal dept (legal-agent)
**Blocks:** Contracts, partnerships, data sharing agreements

### Checklist:

```
[ ] L1  — Contract structure complete (parties, scope, term, termination)
[ ] L2  — No clauses that override CEO authority or agent governance rules
[ ] L3  — IP ownership clauses: all OmniClaw output remains OmniClaw property
[ ] L4  — Data privacy: GDPR/local law compliant (gdpr-agent review)
[ ] L5  — No unlimited liability clauses
[ ] L6  — Dispute resolution jurisdiction acceptable
[ ] L7  — License grants are limited, revocable, non-exclusive (where applicable)
[ ] L8  — Financial terms match CFO-approved budget
```

**Team:** contract-agent (L1,L2,L5,L6) | ip-agent (L3,L7) | gdpr-agent (L4) | legal-agent (L8)

**Verdict:**
- All pass → **CLEAR TO SIGN** — STILL requires CEO final approval before signing
- Any fail → **REVISIONS NEEDED** — specific clauses flagged
- L2 or L5 fail → **DO NOT SIGN** — L3 escalation with full analysis

**Receipts:** `telemetry/qa_receipts/gate_legal/<T-ID>.json`

---

## Gate Escalation Matrix

| Gate | 1st FAIL | 2nd FAIL | 3rd FAIL | CRITICAL |
|------|----------|----------|----------|---------|
| GATE_QA | Worker fixes, re-submit | Worker + Manager review | L2 to CTO | n/a |
| GATE_CONTENT | Author revises | Author + CMO review | L2 to CMO | n/a |
| GATE_SECURITY | CONDITIONAL watch | BLOCK + L2 to CTO/COO | CEO override required | Direct L3 — work pauses |
| GATE_LEGAL | Revisions needed | Legal chief review | DO NOT SIGN + L3 | Direct L3 — CEO required |

---

*"A gate is not an obstacle. It is proof that quality was checked."*

