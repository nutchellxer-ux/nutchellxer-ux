import os
from fetch import fetch_pkg

def rebuild(pkg_name):
    target_path = f"../{pkg_name}.py"
    
    if os.path.exists(target_path):
        print(f"[*] Removing old version of {pkg_name}...")
        os.remove(target_path)
    
    print(f"[*] Recreating {pkg_name}...")
    return fetch_pkg(pkg_name) 
