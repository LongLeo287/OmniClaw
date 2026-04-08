# System Upgrade Proposal: guardrails

> [!TIP]
> This actionable proposal was automatically drafted by OA Academy because this repository scored 8/10.

## Application Vision for OmniClaw
OmniClaw can integrate NeMo Guardrails as its core 'Safety and Constraint Layer' for any new agent or workflow. Instead of simply passing the user input to an LLM, OmniClaw's Router Agent first passes the input through the Guardrails system. This system validates the intent against defined schemas (e.g., 'BookFlight' or 'CheckBalance'), ensuring the LLM only generates responses and calls functions that are explicitly permitted. This prevents prompt injection and hallucination, making OmniClaw's multi-agent interactions more reliable and auditable.

## Next Action Items
1. Review the `DEEP_KNOWLEDGE.md` to understand the architecture.
2. Isolate the target modules identified in the vision.
3. Wrap the modules into an OmniClaw Skill or Agent in `ecosystem/`.
