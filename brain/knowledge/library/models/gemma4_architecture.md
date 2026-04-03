---
id: gemma4-architecture
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.350222
---

﻿---
model_family: Gemma 4
provider: Google DeepMind / Ollama
variants:
  - id: gemma4:e4b
    context: 128K
    parameters: 4B
    type: Dense
  - id: gemma4:26b
    context: 256K
    parameters: 26B (4B active)
    type: MoE
status: INTEGRATED
---

# Gemma 4 Architecture Protocol

This model is configured as a primary Agentic and Multimodal LLM for the OmniClaw Ecosystem.

## Capabilities
- **Reasoning**: Native <|think|> block support for internal thought generation.
- **Context**: Massive 128K/256K token windows for entire codebases.
- **Multimodal**: Accepts Image and Text. (Images MUST precede text in prompts).

## Recommended Standard Parameters
- 	emperature: 1.0
- 	op_p: 0.95
- 	op_k: 64

## Execution
Gemma 4 binaries are stored securely in ault/models/ollama/.
Daemons and Agents must use the local Ollama API (localhost:11434) to interface with this brain.
