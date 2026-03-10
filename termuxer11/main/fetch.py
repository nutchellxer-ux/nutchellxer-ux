import subprocess
import os

def fetch_pkg(pkg_name):
    # Points to your GitHub root
    base_url = f"https://raw.githubusercontent.com/nutchellxer-ux/nutchellxer-ux/main/{pkg_name}.py"
    # Target is the parent directory (termuxer11/)
    target_path = f"../{pkg_name}.py"
    
    print(f"[*] Fetching {pkg_name} from repository...")
    result = subprocess.run(["curl", "-fL", base_url, "-o", target_path])
    
    if result.returncode == 0:
        print(f"[+] {pkg_name} installed in termuxer11/")
        return True
    else:
        print(f"[!] Error: Package {pkg_name} not found.")
        return False 
