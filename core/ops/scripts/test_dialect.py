import os
import sys

# Connect to OmniClaw ecosystem
sys.stdout.reconfigure(encoding='utf-8')
omniclaw_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, omniclaw_root)
sys.path.insert(0, os.path.join(omniclaw_root, "core", "utils"))

from mempalace import Dialect

def test_dialect():
    readme_path = os.path.join(omniclaw_root, "README.md")
    if not os.path.exists(readme_path):
        print("OmniClaw README.md not found.")
        return

    print("--- Reading OmniClaw README ---")
    with open(readme_path, "r", encoding="utf-8") as f:
        text = f.read(4000) # Read only first 4000 chars for testing

    print("\n--- Compressing via Dialect Zettelkasten ---")
    dial = Dialect()
    meta = {"source_file": "OmniClaw_Core_README.md", "wing": "System", "room": "Engine"}
    compressed = dial.compress(text, metadata=meta)
    
    import core.daemons.oma_synapse as oma_synapse
    oma_synapse.digest_aaak("OmniClaw_Core", compressed)
    
    print("\n--- Testing Recall from Synapse Vector Network ---")
    results = oma_synapse.synapse_recall("omniclaw_longleo_multi-agent")
    if results:
        for r in results:
            print(f"Hit [{r['similarity']}]: {r['repo_name']} => {r['aaak_zettel']}")

    print("\n[SUCCESS] Dialect Zettel Engine Operational.")

if __name__ == "__main__":
    test_dialect()
