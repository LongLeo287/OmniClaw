---
id: agent-commands
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.668140
---

# 💻 Agent Commands (CLI Usage)

This protocol governs how a human operator (CEO) or Orchestrator invokes specific agents and tools within the OmniClaw framework.

[**🇻🇳 Xem Bản Tiếng Việt**](agent_commands-vn.md) | [**Return to Docs Index**](../README.md) | [**📚 Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## Direct Invocation via Terminal

If you want to skip Orchestrators and talk directly to an agent, you load their specific `_rules.md` file found in `brain/rules` and supply the initial task.

**Example: Activating Strix Security (Dept 10)**

Whenever you're reviewing a cloned repo or a community plugin:

```bash
> Hey Assistant, load brain/rules/10_strix_security_rules.md and review this payload.
```

## Built-In Commands & Skills

Agents inherently understand the skills provided by the registry. Instead of writing shell scripts, simply tell the agent to invoke the tool.

- **`search_web`**: Tell the Research Agent (Dept 13) to look up a topic on Google/Perplexity.
- **`run_tests`**: Tell the QA agent (Dept 02) to verify a new PR branch using local pytest.
- **`civ_intake`**: Trigger the Content Intake Pipeline to ingest a PDF or Github Repository.

### Custom Workflows
If an agent is failing to accomplish a multi-step task, build them a workflow inside `system/ops/workflows/` and tell them to read it first before executing.
