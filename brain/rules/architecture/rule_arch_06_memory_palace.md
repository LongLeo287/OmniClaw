---
id: RULE-ARCH-06
name: -MemPalace 3-Layer Memory Architecture-
tags: [core, architecture, filesystem, topology, mempalace]
owner: OMA
type: system_rule
registered: true
---

# RULE-ARCH-06: MEMPALACE 3-LAYER SPATIAL ARCHITECTURE

> [!IMPORTANT]
> **Authority:** OMA (OmniClaw Master Architect)
> **Purpose:** Defines the exact Spatial Topology of OmniClaw->s Memory subsystem.

Starting in OmniClaw V5.0, the Memory Layer no longer operates as a flat file dump. It utilizes the **Drawers & Closets Paradigm**, meticulously managed by OMA and populated dynamically via the Omnibus Assimilation Pipeline (OAP). 

Any Agent attempting to store or retrieve data MUST traverse this 3-Layer architecture.

---

## 🧠 THE 3 COGNITIVE LAYERS

### Layer 1: RAW Drawers (Baseline Verbatim Data)
* **Storage Artifacts:** `.md`, `.py`, `.json` (e.g., `_DISTILLED.md`).
* **Attributes:** Primitive, uncompressed, explicitly holding 100% -Ground Truth-.
* **Purpose:** These files are strictly required for syntax-heavy logic, exact API specs, and source code. No LLM summarization loss is permitted at this layer.
* **Governed by:** OIW (Intake) and OER (Registrar).

### Layer 2: AAAK Closets (Context Summaries)
* **Storage Artifacts:** `.aaak` (`_CLOSET.aaak`).
* **Attributes:** Highly compressed using the **Lossy Abbreviation Dialect**.
* **Purpose:** For heavy conversational data, meeting logs, or long timelines. Instead of bloated tokens, OAP triggers the `mempalace_agent` to extract structural summaries (Entity Codes, Topics, and Emotions). This radically slashes LLM context window cost.
* **Governed by:** OAP (Pipeline) and executed by `mempalace_agent`.

### Layer 3: Graph Navigation (Cognitive Mapping)
* **Storage Artifacts:** `FAST_KNOWLEDGE_INDEX.json` and Memory Maps.
* **Attributes:** The topological map of **Wings** (Macro Projects / Domains) and **Rooms** (Micro Sub-topics).
* **Purpose:** This overarching logic structures EXACTLY where Agents should be reading to emulate human logic routing, rather than dumping all text into RAG blind.
* **Governed by:** **OMA (Master Architect)**. No other entity is allowed to redraw the Graph Map.

---

> [!CAUTION]
> **Agent Directive:** When an Agent is queried for information, the Agent MUST NOT fetch `_DISTILLED.md` verbatim if it is a 10,000-line Chat log. The Agent MUST ask OMA for the Graph path, head to the Wing/Room, and selectively read the `_CLOSET.aaak` to preserve Token Quota. Full `_DISTILLED.md` access is reserved exclusively for coding and spec validation.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
