import subprocess
import sys
import os

def run_pkg(pkg_name):
    # Look for the file in the parent directory
    target_path = f"../{pkg_name}.py"
    
    if os.path.exists(target_path):
        print(f"[*] Executing {pkg_name}...")
        subprocess.run([sys.executable, target_path])
    else:
        print(f"[!] Error: {pkg_name}.py is not installed in the root.") 
