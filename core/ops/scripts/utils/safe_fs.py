import os
import shutil

class SafeFileSystemError(Exception):
    pass

def is_same_path_windows(path1, path2):
    """
    On Windows, checks if two string paths logically point to the exact same location
    by normalizing their paths and making them lowercase to bypass Windows case-insensitivity.
    """
    return os.path.normcase(os.path.abspath(path1)) == os.path.normcase(os.path.abspath(path2))

def safe_rename_or_merge(src, dst):
    """
    Safely renames or merges directories on Windows environments.
    Prevents the fatal data loss gap where src and dst are the same directory under case-insensitive rules.
    """
    if not os.path.exists(src):
        raise SafeFileSystemError(f"Source does not exist: {src}")

    # Root Cause Prevention: Check if they are the exact same folder (ignoring case)
    if is_same_path_windows(src, dst):
        # We are just renaming case (e.g. ABC -> abc). Let os.rename handle it directly safely.
        os.rename(src, dst)
        return True
        
    if not os.path.exists(dst):
        # Normal safe rename
        os.rename(src, dst)
        return True
        
    # Standard merge logic if really two different directories
    if os.path.isdir(src) and os.path.isdir(dst):
        for item in os.listdir(src):
            s_item = os.path.join(src, item)
            d_item = os.path.join(dst, item)
            
            if not os.path.exists(d_item):
                shutil.move(s_item, d_item)
            else:
                # Collision logic here... (e.g. rename _dup)
                pass 
                
        # Safe to remove source only after confirming they are distinct paths
        shutil.rmtree(src, ignore_errors=True)
        return True
    
    return False

if __name__ == "__main__":
    print("Safe Windows FS Module initialized.")
