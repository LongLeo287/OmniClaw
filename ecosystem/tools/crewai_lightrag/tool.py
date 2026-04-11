import sys
import os
from crewai.tools import BaseTool
from pathlib import Path

# Append root for OmniClaw relative imports
_OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[3])
sys.path.append(_OMNICLAW_ROOT)

class LightRAGTool(BaseTool):
    name: str = "LightRAG Knowledge Indexing Tool"
    description: str = "Reads report text or documents and inserts them directly into the core Knowledge Graph RAG. Input is markdown content."

    def _run(self, document_content: str) -> str:
        try:
            from plugins.LightRAG.lightrag_adapter import get_lightrag
            rag = get_lightrag()
            print(f"[{self.name}] Inserting text into graph ({len(document_content)} chars)...")
            success = rag.insert(document_content, source_hint="CrewAI Multi-Agent Pipeline")
            if success:
                return "Graph Node Insertion SUCCESS. Knowledge successfully updated into the system."
            return "Failed to insert into Graph RAG."
        except ImportError:
            return "Fallback Error: 'plugins.LightRAG' adapter not found. Verify LightRAG Docker bridge is running."
        except Exception as e:
            return f"Error indexing document: {e}"
