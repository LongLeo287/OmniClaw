import os
import sys
import hashlib
from datetime import datetime

try:
    import chromadb
except ImportError:
    print("\033[91m[ERR]\033[0m [Synapse] 'chromadb' not installed. Please pip install chromadb.")
    sys.exit(1)

DAEMON_NAME = "OMA_SYNAPSE"
OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CHROMA_DB_PATH = os.path.join(OMNICLAW_ROOT, "brain", "chroma_db")

def _get_collection():
    os.makedirs(CHROMA_DB_PATH, exist_ok=True)
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    try:
        return client.get_collection("synapse_nodes")
    except Exception:
        return client.create_collection("synapse_nodes")

def digest_aaak(repo_name: str, aaak_content: str):
    """
    Ingests an AAAK dialect crystal directly into the Synapse Network (ChromaDB).
    This acts as the Event-driven trigger called by OA.
    """
    collection = _get_collection()
    node_id = f"node_{repo_name}_{hashlib.md5(repo_name.encode()).hexdigest()[:8]}"
    
    print(f"\033[96m[OMA-SYNAPSE]\033[0m Absorbing Dialect Crystal into Vector Network for: {repo_name}")
    
    # Store the entire dense AAAK footprint as a mathematical node
    try:
        # Check if exists, overwrite if needed.
        collection.upsert(
            documents=[aaak_content],
            ids=[node_id],
            metadatas=[{
                "repo_name": repo_name,
                "ingested_at": datetime.now().isoformat(),
                "node_type": "aaak_memory"
            }]
        )
        print(f"    \033[92m[OK]\033[0m Synapse Link Established. ID: {node_id}")
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m [OMA-SYNAPSE] Failed to absorb memory node: {str(e)}")

def synapse_recall(query: str, n_results: int = 3):
    """
    Semantic retrieval over the global Synapse Network.
    Returns highly relevant AAAK zettels in <500ms.
    """
    collection = _get_collection()
    
    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m [OMA-SYNAPSE] Query failed: {str(e)}")
        return []

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    dists = results.get("distances", [[]])[0]
    
    hits = []
    for doc, meta, dist in zip(docs, metas, dists):
        similarity = round(1 - dist, 3)
        hits.append({
            "repo_name": meta.get("repo_name", "Unknown"),
            "similarity": similarity,
            "aaak_zettel": doc
        })
        
    return hits

if __name__ == "__main__":
    # Test execution
    print("Testing Synapse Recall...")
    import time
    t0 = time.time()
    results = synapse_recall("technical architecture")
    t1 = time.time()
    
    print(f"\nCompleted in {round((t1-t0)*1000, 2)} ms.")
    if not results:
        print("No memories stored yet.")
    else:
        for i, hit in enumerate(results, 1):
            print(f"\n--- [HIT {i}] SIMILARITY: {hit['similarity']} | REPO: {hit['repo_name']} ---")
            print(hit['aaak_zettel'])
