---
id: flash-rag-retrieval
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.210054
---

<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

---
description: How retrieval-master executes High-Speed RAG queries
---
# Storm Workflow: FlashRAG Retrieval (Dept 18)

## The Prompt
- Any Agent needing to look up data from `PROCESSED_LIBRARY.md` or other long documents must send the Input to `retrieval-master`.
- Example: `[Context_Request]: Configuration: Where is Redis in the original KI file?`

## Stage 1: Dual Indexing
- `retrieval-master` breaks down the Prompt into 2 pieces: Semantics and Keywords.
- Activates the Vectorizing algorithm. If the Database is not yet embedded, it activates Semantic Search using `grep_search` combined with Pattern Recognition.

## Stage 2: Parallel Sweep
- **Path A (For Logic / Reasoning):** Runs a Regex command to grab files with `##` or `---` related to "Redis".
- **Path B (For Direct Hits):** Reads the adjacent Context lines. Does not load files over 500 lines.

## Stage 3: Truncated Answer
- Extracts only a single piece of Text (about 300 words) that directly contains the original Command or Logic.
- Sends back to the calling Node: "I'm not sending a file. I'm sending an information pellet!".

> [!NOTE] FlashRAG Concept
> Optimize API Calls by reducing the thickness of the Prompt. All redundant Text chunks are trimmed before being sent to the Reasoner.
