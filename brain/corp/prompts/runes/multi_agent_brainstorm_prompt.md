---
description: Multi-Agent structured design review — simulate peer review with 4 constrained agent roles before implementation
id: multi_agent_brainstorm_prompt
type: corp_document
registered: true
---
## MANDATORY DELIVERY RULE
Write output to artifact file → notify_user → NEVER paste in chat
Invoke only for high-risk, high-complexity, or high-impact designs.

---
## Multi-Agent Review Structure (Mandatory)

### 🎨 Phase 1 — Primary Designer
```
Summary of proposed design (from confirmed brainstorm):
- Key architectural decisions: [...]
- Assumptions: [...]
- Decision Log (started): [...]
```

---
### ⚔️ Phase 2A — Skeptic / Challenger
```
Internal Prompt: "Assume this design fails in production. Why?"
```
**Checklist:**
- [ ] Single-point-of-failure vulnerabilities?
- [ ] Uncontrolled external dependencies?
- [ ] Flawed assumptions that could occur?
- [ ] YAGNI violations?

**Results:** [list specific objections]

---
### 🔒 Phase 2B — Constraint Guardian
```
Focus: performance · security · reliability · maintainability · cost
```
**Checklist:**
- [ ] Can the system handle maximum load?
- [ ] Is sensitive data protected?
- [ ] Will it be maintainable in 6 months?
- [ ] Do operational costs scale reasonably?

**Results:** [pass / reject / needs revision]

---
### 👤 Phase 2C — User Advocate
```
Focus: UX · cognitive load · clarity · error messaging
```
**Checklist:**
- [ ] Will users understand it without guidance?
- [ ] Are error messages meaningful?
- [ ] Are there confusing points in the flow?

**Results:** [pass / reject / needs revision]

---
### ⚖️ Phase 3 — Arbiter / Integrator
```
Resolve all objections. Declare: APPROVED | REVISE | REJECT
```

| Objection | From | Accept? | Resolution |
|-----------|------|---------|------------|
| [objection] | Skeptic | ✅/❌ | [how it's handled] |

**Verdict:** [APPROVED / REVISE / REJECT]
**Decision Log (final):** [record all decisions]

---
*Implementation must only proceed after Arbiter declares APPROVED.*
