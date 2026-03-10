import subprocess
import sys
import os

def run_pkg(pkg_name):
    # Look for the package in the parent directory
    target_path = f"../{pkg_name}.py"
    
    if os.path.exists(target_path):
        print(f"\033[92m[*] Launching {pkg_name}...\033[0m")
        subprocess.run([sys.executable, target_path])
    else:
        print(f"\033[91m[!] Error: {pkg_name}.py is not installed.\033[0m")
