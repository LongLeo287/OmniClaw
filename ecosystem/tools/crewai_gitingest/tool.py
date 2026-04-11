import sys
import os
from crewai.tools import BaseTool
from pathlib import Path

# Append root for OmniClaw relative imports
_OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[3])
sys.path.append(_OMNICLAW_ROOT)

class GitingestTool(BaseTool):
    name: str = "Gitingest Code Repo Analyzer"
    description: str = "Extracts source code and summarizes directory structure from a Github URL. Input is a valid repo URL."

    def _run(self, repo_url: str) -> str:
        try:
            # Local gitingest library or HTTP API
            from gitingest import ingest
            print(f"[{self.name}] Ingesting {repo_url}...")
            summary, tree, content = ingest(repo_url)
            # Truncate content to avoid exceeding light mode token limits
            return f"Directory Tree:\n{tree}\n\nKey Content Snippet:\n{content[:3000]}"
        except ImportError:
            # Fallback tool if gitingest python module is not installed
            return f"Fallback Error: Python module 'gitingest' not found. Please install."
        except Exception as e:
            return f"Error grabbing repo: {e}"
