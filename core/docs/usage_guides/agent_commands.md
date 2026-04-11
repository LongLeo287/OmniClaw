---
id: agent-commands
type: document
owner: SYSTEM
tags: [operators, agents]
---

# 💻 Agent Commands (CLI Usage)

This protocol governs how a human operator (CEO) or Orchestrator invokes specific agents and tools within the OmniClaw framework.

[**🇻🇳 Vietnamese Translation**](agent_commands_vn.md) | [**Return to Docs Index**](../README.md) | [**📚 Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## Boot Prompt Selection

Use the boot prompt that matches the interface you are opening:

- `brain/agents/claude.md` for Claude Code style terminal sessions
- `brain/agents/gemini.md` for Gemini or Antigravity style orchestration sessions

Do not mix the two boot files in the same startup path.

## Recommended Operator Prompts

Examples:

```text
Load brain/agents/claude.md and follow the boot sequence for this repository.
Load brain/agents/gemini.md and route this task using the current system router.
Read brain/rules/_DIR_IDENTITY.md, ecosystem/_REGIONAL_MAP.md, and core/docs/README.md before planning changes.
```

## Routing References

When an agent needs more context, prefer current checked-in maps:

- `brain/agents/system_router.json`
- `brain/agents/README.md`
- `brain/rules/_DIR_IDENTITY.md`
- `ecosystem/_REGIONAL_MAP.md`
- `ecosystem/workforce/_REGIONAL_MAP.md`
- `ecosystem/skills/_REGIONAL_MAP.md`
- `ecosystem/tools/_REGIONAL_MAP.md`
- `ecosystem/bridges/_REGIONAL_MAP.md`

## Runtime Actions

Prefer explicit actions over hidden automation:

- ask for diagnostics with `omniclaw doctor`
- inspect resolved roots with `omniclaw paths`
- launch a bridge with its dedicated launcher in `ecosystem/bridges/`
- use repair mode only when provisioning is intentional

## Command Style

- Keep operator prompts explicit about scope, target files, and desired outcome.
- Prefer English for system instructions, logs, and agent-to-agent handoffs.
- Treat bridge repair, package installation, and heavy-state sync as explicit provisioning tasks, not default runtime behavior.
