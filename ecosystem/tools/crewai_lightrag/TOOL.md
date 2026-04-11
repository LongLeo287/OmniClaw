---
id: crewai_lightrag
name: CrewAI LightRAG Tool
status: active
integration_type: python_script
accessible_by:
  - Orchestrator
  - CrewAI Agents
tags: [rag, graph-database, crewai]
---

# LightRAG Knowledge Indexing Tool

## Overview
This native Python script functions as a `BaseTool` for CrewAI or direct orchestrator calls. It pipes text data into the centralized Knowledge Graph leveraging the LightRAG proxy. 

## Instructions
Invoke the tool by passing the raw string text that you want indexed into the Graph. The tool will parse the text and append it to the active Qdrant nodes mapped to LightRAG.
