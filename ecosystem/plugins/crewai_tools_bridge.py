import sys
import os

from crewai.tools import BaseTool
from pydantic import Field

from pathlib import Path

# Append root for OmniClaw relative imports
_OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[2])
sys.path.append(_OMNICLAW_ROOT)

class GitingestTool(BaseTool):
    name: str = "Gitingest Code Repo Analyzer"
    description: str = "Extracts source code and summarizes directory structure from a Github URL. Input is a valid repo URL."

    def _run(self, repo_url: str) -> str:
        try:
            # Thu vien gitingest local hoac API HTTP
            from gitingest import ingest
            print(f"[{self.name}] Ingesting {repo_url}...")
            summary, tree, content = ingest(repo_url)
            # Truncate content de tranh qua gioi han token cua mode nhe
            return f"Directory Tree:\n{tree}\n\nKey Content Snippet:\n{content[:3000]}"
        except ImportError:
            # Fallback tool neu chua install gitingest module python
            return f"Fallback Error: Python module 'gitingest' not found. Please install."
        except Exception as e:
            return f"Error grabbing repo: {e}"


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
                return "Graph Node Insertion SUCCESS. Da cap nhat kien thuc vao he thong."
            return "Failed to insert into Graph RAG."
        except Exception as e:
            return f"Error indexing document: {e}"
