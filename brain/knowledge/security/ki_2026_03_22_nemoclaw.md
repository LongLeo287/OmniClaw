---
id: KI-2026-03-22-nemoclaw
source: https://github.com/NVIDIA/NemoClaw
type: REFERENCE
domain: security
dept: security_grc, rd
stars: 1k
compatible_ai_os: False
created: 2026-03-22T23:23:54.299876
---

# NVIDIA NemoClaw

> NVIDIA reference stack for running OpenClaw agents in sandboxed OpenShell. 4-layer protection: network egress control, filesystem isolation, process syscall blocking, inference rerouting.

**Source:** [https://github.com/NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)  
**Stars:** 1k | **Type:** REFERENCE  
**OmniClaw Compatible:** ❌ OpenClaw/NVIDIA-specific

## OmniClaw Notes
OpenClaw/OpenShell ecosystem. NOT compatible with OmniClaw Claude/Antigravity. However, the 4-layer sandbox architecture (network+filesystem+process+inference) is extremely valuable reference for OmniClaw security model. Study the Blueprint/Policy design for OmniClaw QUARANTINE process.

## Key Concepts
- 4-layer protection: Network, Filesystem, Process, Inference
- Network: blocks unauthorized outbound, hot-reloadable policy
- Filesystem: /sandbox and /tmp only, locked at creation
- Process: blocks privilege escalation + dangerous syscalls
- Inference: reroutes model API calls to controlled backends
- Blueprint lifecycle: resolve→verify digest→plan→apply
- Nemotron-3-super-120b-a12b as production model
- OpenShell: surfaces blocked requests in TUI for operator approval

---
*Ingested: 2026-03-22T23:23:54.299876 via knowledge-ingest Phase 1-3*
