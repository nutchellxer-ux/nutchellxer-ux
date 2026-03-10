import curses
import random
import time
import subprocess
import os
import shutil

def install_dependencies():
    # Check if 'play' (part of sox) is installed
    if shutil.which("play") is None:
        print("--- Dependencies missing. Installing Sox... ---")
        # Runs the Termux package manager command
        subprocess.run(["pkg", "install", "sox", "-y"])
        print("--- Installation Complete. Launching PTA... ---")
        time.sleep(1)

def play_krush():
    # Rapid-fire frequency shifts for that 'Alert' feel
    freq = random.randint(1000, 3000)
    # Using 'square' wave for a harsher, distorted sound
    subprocess.Popen(["play", "-q", "-n", "synth", "0.03", "square", str(freq), "vol", "0.5"], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    
    # Setup high-contrast colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED) # Flashing effect

    LARGE_67 = [
        "  ██████   ███████  ",
        " ██        ╚════██  ",
        " ███████       ██   ",
        " ██    ██     ██    ",
        " ╚██████     ██     "
    ]

    while True:
        rows, cols = stdscr.getmaxyx()
        color_idx = random.randint(1, 4)
        color = curses.color_pair(color_idx)
        
        # Spawn logic
        if random.random() > 0.85:
            # Large 67s "Force Spawning"
            y = random.randint(0, max(0, rows - 6))
            x = random.randint(0, max(0, cols - 25))
            for i, line in enumerate(LARGE_67):
                try: stdscr.addstr(y + i, x, line, color | curses.A_BOLD)
                except: pass
            play_krush()
        else:
            # Small 67s flooding the background
            y = random.randint(0, rows - 1)
            x = random.randint(0, cols - 3)
            try: stdscr.addstr(y, x, "67", color)
            except: pass
            
        stdscr.refresh()
        time.sleep(0.01) # Ultra-fast chaos

        if stdscr.getch() != -1:
            break

if __name__ == "__main__":
    # Run the installer before starting the visual/audio loop
    install_dependencies()
    curses.wrapper(main)
