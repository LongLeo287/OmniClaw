# Deep Matrix Profile: mempalace

# Deep Knowledge Report for MemPalace

## Overview

Mempalace is an advanced memory management system designed to handle various types of chat data, project files, and provide semantic search capabilities. It leverages a hierarchical structure with layers (L0-L3) to manage and retrieve memories efficiently.

## Architectural Patterns

### Layered Memory Management
- **Layer 0 (Identity):** Always loaded, containing essential identity information.
- **Layer 1 (Essential Story):** Always loaded, holding key moments from the user's history.
- **Layer 2 (On-Demand):** Loaded based on specific topics or wings, providing detailed context when needed.
- **Layer 3 (Deep Search):** Full semantic search capabilities across all data.

### Command Line Interface (CLI)
Mempalace provides a CLI for various operations:
- `init`: Detects rooms from folder structure.
- `split`: Splits concatenated files into per-session files.
- `mine`: Mines project and conversation files.
- `search`: Searches through the memory palace.
- `wake-up`: Shows L0 + L1 wake-up context.
- `status`: Displays current state.

### Configuration System
Configurations are managed via a configuration file (`~/.mempalace/config.json`) with fallbacks to environment variables and default values. The system supports:
- **Palace Path:** Directory where memory is stored.
- **Collection Name:** ChromaDB collection name for storing memories.
- **Topic Wings:** Predefined topics used in semantic search.

### Entity Detection
Entities such as people and projects are auto-detected from file content using a two-pass approach:
1. **Pass 1:** Scans files, extracts entity candidates with signal counts.
2. **Pass 2:** Scores and classifies each candidate.

### Knowledge Graph
A temporal knowledge graph is implemented to manage relationships between entities over time:
- **Entity Nodes:** People, projects, tools, concepts.
- **Relationship Edges:** Typed (e.g., `child_of`, `does`).
- **Temporal Validity:** Tracks when facts are true.
- **Closet References:** Links back to verbatim memories.

### Semantic Search
Uses ChromaDB for full-text and semantic search capabilities:
- **Indexing:** Files are indexed based on content, metadata, and relationships.
- **Querying:** Supports complex queries with time filtering.

## Core Algorithms

### Entity Detection Algorithm
1. **Signal Extraction:**
   - **Person Signals:** Verbs, pronouns, dialogue markers.
   - **Project Signals:** Verbs related to projects, file names, imports.
2. **Candidate Classification:**
   - **Interactive Review:** Users confirm or modify detected entities.

### Knowledge Graph Construction
- **Triple Addition:** Adds relationships between entities with temporal validity.
- **Querying:** Entity-first traversal with time filtering.

### Semantic Search Algorithm
1. **Indexing:** Files are indexed using ChromaDB.
2. **Query Processing:**
   - **Exact Matches:** Full-text search for exact words.
   - **Semantic Queries:** Uses semantic embeddings to find relevant memories.

## Primary Mechanisms

### Entity Registry
- **Onboarding:** User explicitly defines entities.
- **Learned:** Inferences from session history with high confidence.
- **Research:** Lookups via Wikipedia for unknown terms.

### Wake-Up Context
- **L0 + L1:** Provides a quick overview of key moments and identity information.
- **Wing-Specific:** Customizable context based on project or topic.

### File Mining
- **Project Files:** Mines code, documentation, notes from projects.
- **Conversation Files:** Extracts conversations from various chat platforms (Claude, ChatGPT, Slack).

## Conclusion

Mempalace is a sophisticated memory management system that integrates entity detection, knowledge graph construction, and semantic search to provide a comprehensive solution for managing and retrieving memories. Its layered architecture ensures efficient retrieval of relevant information while maintaining user privacy.

---

This report provides an in-depth look at the architectural patterns, core algorithms, and primary mechanisms used in MemPalace.