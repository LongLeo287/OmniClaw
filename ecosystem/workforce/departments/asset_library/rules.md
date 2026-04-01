# ⚖️ RULES (Dept 18: Asset & Knowledge Library)

> Internal Code for Asset Library.

1. **RULE 01: NO BULK READ** 🚫
   Agents (including Tier 1) absolutely CANNOT read the entire `PROCESSED_LIBRARY.md` file or raw data files larger than 500 lines. All queries must go through `retrieval-master`.

2. **RULE 02: HIGH-SPEED RAG MANDATE** ⚡
   `retrieval-master` forces the use of parallel Vector/Keyword expressions according to the FlashRAG principle. No linear scanning. Output should be limited to 200 - 300 words of highest quality.

3. **RULE 03: INDEX FIRST, RETRIEVE LATER** 🗃️
   All new source code pushed into the ARCHIVE branch must be chunk tagged by `knowledge-curator-agent` and `asset-tracker-agent` immediately before granting access.