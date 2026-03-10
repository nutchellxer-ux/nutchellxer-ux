import sys
import os

# Link to the internal engine folder
sys.path.append(os.path.join(os.getcwd(), "main"))

try:
    import fetch
    import execute
    import recreate
except ImportError:
    print("\033[91m[!] Error: Core engines (fetch, execute, recreate) missing in main/\033[0m")
    sys.exit(1)

def cli():
    if len(sys.argv) < 3:
        print("\033[93mUsage: nutchx [install|run|rebuild] [package]\033[0m")
        return

    cmd = sys.argv[1].lower()
    pkg = sys.argv[2]

    if cmd == "install":
        fetch.fetch_pkg(pkg)
    elif cmd == "run":
        execute.run_pkg(pkg)
    elif cmd == "rebuild":
        recreate.rebuild(pkg)
    else:
        print(f"[!] Unknown command: {cmd}")

if __name__ == "__main__":
    cli()
