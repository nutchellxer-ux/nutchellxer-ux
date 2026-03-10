import os
import subprocess

def build_termuxer11():
    print("\033[96m[*] Creating termuxer11 Environment...\033[0m")
    
    # Create the folder structure
    folders = ["termuxer11/main", "termuxer11/runs"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f" [+] Folder created: {folder}")

def sync_from_root():
    # Base URL pointing to your root/main branch
    base_url = "https://raw.githubusercontent.com/nutchellxer-ux/nutchellxer-ux/main/"
    
    # Map of files to their local paths
    files = {
        "main.py": "termuxer11/main.py",
        "main/fetch.py": "termuxer11/main/fetch.py",
        "main/recreate.py": "termuxer11/main/recreate.py",
        "main/execute.py": "termuxer11/main/execute.py"
    }

    print("\033[92m[*] Syncing core assets to termuxer11/...\033[0m")
    for repo_path, local_path in files.items():
        subprocess.run(["curl", "-sL", f"{base_url}{repo_path}", "-o", local_path])
        print(f"  -> Synced: {local_path}")

if __name__ == "__main__":
    build_termuxer11()
    sync_from_root()
    print("\033[95m\n[!] Setup Complete. System is live in termuxer11/\033[0m")
