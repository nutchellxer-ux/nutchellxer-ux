import subprocess
import os

def fetch_pkg(pkg_name):
    # Points to your GitHub root/main branch
    base_url = f"https://raw.githubusercontent.com/nutchellxer-ux/nutchellxer-ux/main/{pkg_name}.py"
    # Downloads the file to the parent (termuxer11/) directory
    target_path = f"../{pkg_name}.py"
    
    print(f"\033[94m[*] Fetching {pkg_name}...\033[0m")
    result = subprocess.run(["curl", "-fL", base_url, "-o", target_path])
    
    if result.returncode == 0:
        print(f"\033[92m[+] {pkg_name} is now installed in termuxer11/\033[0m")
    else:
        print(f"\033[91m[!] Failed to find {pkg_name} in repository.\033[0m") 
