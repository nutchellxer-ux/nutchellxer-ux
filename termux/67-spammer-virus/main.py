import curses
import random
import time
import subprocess
import os

# The ASCII "Image" Placeholder
IMG_POPUP = [
    "┌──────────┐",
    "│  [IMG]   │",
    "│  PICTURE │",
    "└──────────┘"
]

def play_krush():
    freq = random.randint(1500, 3500)
    subprocess.Popen(["play", "-q", "-n", "synth", "0.02", "square", str(freq)], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    popups = [] # List to track active popups: [(y, x), ...]
    click_count = 0
    stage = "IMAGE_CHAOS"
    
    while True:
        rows, cols = stdscr.getmaxyx()
        
        if stage == "IMAGE_CHAOS":
            # 1. Background Chaos (67s)
            for _ in range(2):
                try: stdscr.addstr(random.randint(0, rows-1), random.randint(0, cols-3), "67", curses.color_pair(1))
                except: pass

            # 2. Randomly Spawn Image Popups
            if random.random() > 0.94 and len(popups) < 5:
                py, px = random.randint(0, rows-5), random.randint(0, cols-13)
                popups.append((py, px))
                play_krush()

            # 3. Draw Active Popups
            for py, px in popups:
                for i, line in enumerate(IMG_POPUP):
                    try: stdscr.addstr(py + i, px, line, curses.color_pair(2) | curses.A_REVERSE)
                    except: pass

            # 4. Handle Mouse/Touch Clicks
            key = stdscr.getch()
            if key == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                # Check if click hit any popup
                for p in popups[:]:
                    py, px = p
                    if py <= my < py + 4 and px <= mx < px + 12:
                        popups.remove(p)
                        click_count += 1
                        stdscr.clear() # Flash on click
            
            # Show Progress
            try: stdscr.addstr(0, 0, f"INTERCEPTED: {click_count}/50", curses.color_pair(3) | curses.A_BOLD)
            except: pass

            if click_count >= 50:
                stage = "SECRET_TYPE"
                stdscr.clear()

        elif stage == "SECRET_TYPE":
            # The previous stages follow here...
            stdscr.addstr(rows//2, (cols-25)//2, "IMAGE BREACH CONTAINED.", curses.color_pair(3))
            stdscr.addstr(rows//2 + 1, (cols-30)//2, "PROCEED WITH pkg install...", curses.color_pair(1))
            # (Insert previous logic for secret commands here)
            break 

        stdscr.refresh()
        time.sleep(0.02)

if __name__ == "__main__":
    curses.wrapper(main)
    import curses
import random
import time
import subprocess
import os

# ASCII Art for the big 67
BIG_67 = [
    "  ██████   ███████  ",
    " ██        ╚════██  ",
    " ███████       ██   ",
    " ██    ██     ██    ",
    " ╚██████     ██     "
]

def play_alert():
    try:
        f = random.randint(1200, 3000)
        subprocess.Popen(["play", "-q", "-n", "synth", "0.03", "square", str(f)], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except: pass

def main(stdscr):
    # Setup Terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.use_default_colors()
    
    # Initialize Colors (1=Red, 2=Green, 3=Yellow, 4=Blue, 5=Magenta, 6=Cyan)
    for i in range(1, 7):
        curses.init_pair(i, i, -1)
    
    stage = "DISASTER"
    input_buffer = ""

    while True:
        rows, cols = stdscr.getmaxyx()
        
        if stage == "DISASTER":
            # 1. Spawn Small 67s with Random Colors
            y, x = random.randint(0, rows-1), random.randint(0, cols-3)
            color = curses.color_pair(random.randint(1, 6))
            try: stdscr.addstr(y, x, "67", color)
            except: pass

            # 2. Spawn Big 67s occasionally
            if random.random() > 0.95:
                by, bx = random.randint(0, max(0, rows-6)), random.randint(0, max(0, cols-22))
                for i, line in enumerate(BIG_67):
                    try: stdscr.addstr(by+i, bx, line, curses.color_pair(random.randint(1,6)) | curses.A_BOLD)
                    except: pass
                play_alert()

            # Listen for Secret Command: pkg install nutchellxer
            ch = stdscr.getch()
            if ch != -1:
                input_buffer += chr(ch)
                if "pkg install nutchellxer" in input_buffer:
                    stage = "ASSETS"
                    input_buffer = ""
                    stdscr.clear()

        elif stage == "ASSETS":
            # Display "Done" and wait for: nutch install 67-virus
            stdscr.addstr(rows//2, (cols-30)//2, "NUTCHELLXER INSTALLED: DONE", curses.color_pair(2))
            stdscr.refresh()
            
            ch = stdscr.getch()
            if ch != -1:
                input_buffer += chr(ch)
                if "nutch install 67-virus" in input_buffer:
                    stage = "STOP_WAIT"
                    input_buffer = ""
                    stdscr.addstr(rows//2 + 2, (cols-25)//2, "ASSETS DOWNLOADED: DONE", curses.color_pair(2))
        
        elif stage == "STOP_WAIT":
            # Wait for: 67-virus ~stop
            ch = stdscr.getch()
            if ch != -1:
                input_buffer += chr(ch)
                if "67-virus ~stop" in input_buffer:
                    stage = "FINAL"
                    input_buffer = ""

        elif stage == "FINAL":
            stdscr.clear()
            msg = "TYPE 'STOP' AND PRESS ENTER"
            stdscr.addstr(rows//2 - 2, (cols-len(msg))//2, msg, curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(rows//2, (cols-len(input_buffer))//2, input_buffer)
            
            ch = stdscr.getch()
            if ch != -1:
                if ch in (10, 13):
                    if input_buffer.strip().upper() == "STOP": break
                    else: input_buffer = ""
                elif ch == 127: input_buffer = input_buffer[:-1]
                else: input_buffer += chr(ch)

        stdscr.refresh()
        time.sleep(0.02)

if __name__ == "__main__":
    curses.wrapper(main)
    print("--- SYSTEM RESTORED ---")
