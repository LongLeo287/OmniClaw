import os
import zipfile
import argparse
from pathlib import Path
import sys

def pack_release(source_dir_str, version, project_name, output_dir_str):
    source_dir = Path(source_dir_str).resolve()
    
    if not output_dir_str:
        release_dir = source_dir / "releases"
    else:
        release_dir = Path(output_dir_str).resolve()
        
    release_dir.mkdir(parents=True, exist_ok=True)
    zip_filename = release_dir / f"{project_name}_{version}.zip"
    
    # OPTIONAL: Clean before packing
    try:
        script_dir = Path(__file__).resolve().parent
        if str(script_dir) not in sys.path:
            sys.path.append(str(script_dir))
        import omniclaw_cleanup_crew
        # Only scan specific data dirs (not root) for fast pre-pack cleanup
        cleanup_targets = ["brain/memory", "storage/vault", "ecosystem/plugins"]
        omniclaw_cleanup_crew.deploy_cleanup_crew(cleanup_targets, base_path=source_dir)
    except Exception as e:
        print(f" [WARNING] Cleanup Crew bypass: {e}")

    print(f"\n[PACKAGER] INITIALIZING ZIP RELEASE: {project_name} ({version})")
    print(f" -> Source Domain: {source_dir}")
    print(f" -> Output Binary: {zip_filename}")
    
    EXCLUDE_DIRS = {'.git', 'node_modules', '__pycache__', '.pytest_cache', 'releases', 'Trash_Before_Push', 'sandbox', 'venv', 'env'}
    
    # Heavy data directories that should only keep structure (.keep, README.md) 
    # to maintain clean architecture without the heavy weight.
    HEAVY_DATA_DIRS = {'brain/memory', 'brain/knowledge', 'storage/vault', 'ecosystem/plugins'}
    heavy_paths = [ (source_dir / d).resolve() for d in HEAVY_DATA_DIRS ]
    
    if zip_filename.exists():
        try:
            zip_filename.unlink()
        except PermissionError:
            # File is locked (e.g. open in Windows Explorer) — use timestamped filename
            import time
            ts = int(time.time())
            zip_filename = release_dir / f"{project_name}_{version}_{ts}.zip"
            print(f" [INFO] Previous ZIP is locked. Writing to new file: {zip_filename.name}")

    def is_heavy_data_file(file_path_obj):
        for hp in heavy_paths:
            if hp in file_path_obj.parents:
                return True
        return False

    added_files_count = 0
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            root_path = Path(root)
            
            for file in files:
                if file in {'.env', 'Thumbs.db'} or file.endswith(('.log', '.tmp', '.pack', '.idx')):
                    continue
                    
                file_path = root_path / file
                
                if is_heavy_data_file(file_path):
                    if file not in {'.keep', '.gitkeep', 'README.md'}:
                        continue
                        
                # Anti-Corruption trick for Windows: force POSIX paths
                arcname = file_path.relative_to(source_dir).as_posix()
                zipf.write(file_path, arcname)
                added_files_count += 1
                
    print(f"\n[SUCCESS] PACKING COMPLETE. {added_files_count} source files archived.")
    size_mb = zip_filename.stat().st_size / (1024*1024)
    print(f"--> Payload Metrics (Source Code Only): {size_mb:.2f} MB")
    print(f"--> Extracted to: {zip_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OmniClaw Production Packager")
    parser.add_argument("--source-dir", required=True, help="Path to the repository root directory")
    parser.add_argument("--project-name", required=True, help="Name of the ZIP file payload")
    parser.add_argument("--version", default="v2.0.0", help="Release version (default: v2.0.0)")
    parser.add_argument("--output-dir", default="", help="Destination directory (optional)")
    
    args = parser.parse_args()
    pack_release(args.source_dir, args.version, args.project_name, args.output_dir)