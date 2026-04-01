import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi, login

def first_time_dump():
    AI_OS_ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
    SECRETS_FILE = AI_OS_ROOT / "system/ops/secrets/MASTER.env"
    DATASET_REPO = "OmniClaw_Admin/OmniClaw-Data-Vault"

    print("[OmniClaw System Event]")
    
    if SECRETS_FILE.exists():
        load_dotenv(SECRETS_FILE)
    login(token=os.getenv("HF_TOKEN"))
    api = HfApi()

    # DUMP 1: SQLite Databases at Root
    for db_file in AI_OS_ROOT.glob("*.db"):
        print("[OmniClaw System Event]")
        api.upload_file(path_or_fileobj=str(db_file), path_in_repo=db_file.name, repo_id=DATASET_REPO, repo_type="dataset")
    for db_file in AI_OS_ROOT.glob("*.sqlite*"):
        print("[OmniClaw System Event]")
        api.upload_file(path_or_fileobj=str(db_file), path_in_repo=db_file.name, repo_id=DATASET_REPO, repo_type="dataset")

    # [System log: Legacy non-English comment removed]
    brain_dir = AI_OS_ROOT / "brain"
    if brain_dir.exists():
        print("[OmniClaw System Event]")...")
        api.upload_folder(folder_path=str(brain_dir), path_in_repo="brain", repo_id=DATASET_REPO, repo_type="dataset")
        print("[OmniClaw System Event]")

    # [System log: Legacy non-English comment removed]
    storage_dir = AI_OS_ROOT / "storage"
    if storage_dir.exists():
        print("[OmniClaw System Event]")...")
        api.upload_folder(folder_path=str(storage_dir), path_in_repo="storage", repo_id=DATASET_REPO, repo_type="dataset", ignore_patterns=["*node_modules*", "*.git*"])
        print("[OmniClaw System Event]")

    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")

if __name__ == '__main__':
    first_time_dump()