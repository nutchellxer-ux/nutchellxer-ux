import curses
import random
import time
import subprocess
import os

def play_krush(intensity=1):
    # Intensity increases the frequency and harshness
    freq = random.randint(1500, 4000)
    wave = random.choice(["square", "sawtooth"])
    subprocess.Popen(["play", "-q", "-n", "synth", "0.02", wave, str(freq), "vol", str(0.4 * intensity)], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def draw_bar(stdscr, label, row, cols, color):
    stdscr.clear()
    stdscr.addstr(row - 2, (cols - len(label)) // 2, label, curses.A_BOLD | color)
    for i in range(31):
        bar = "█" * i + "▒" * (30 - i)
        percent = f" LOADING ASSETS: {bar} {int(i/30*100)}%"
        try: stdscr.addstr(row, (cols - len(percent)) // 2, percent, color)
        except: pass
        stdscr.refresh()
        time.sleep(0.08)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    
    # Color Schemes
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stage = "INITIAL_BREACH"
    input_buffer = ""
    start_time = time.time()

    while True:
        rows, cols = stdscr.getmaxyx()
        
        if stage == "INITIAL_BREACH":
            # Flood 67s with random sizes and flicker
            for _ in range(3):
                y, x = random.randint(0, rows-1), random.randint(0, cols-3)
                attr = curses.color_pair(1) | (curses.A_BOLD if random.random() > 0.5 else 0)
                try: stdscr.addstr(y, x, "67", attr)
                except: pass
            
            if random.random() > 0.96: play_krush(1)
            
            key = stdscr.getch()
            if key != -1:
                input_buffer += chr(key)
                if "pkg install nutchellxer" in input_buffer:
                    draw_bar(stdscr, "NUTCHELLXER KERNEL INTEGRATION", rows // 2, cols, curses.color_pair(2))
                    input_buffer = ""
                    stage = "ASSET_FLOOD"

        elif stage == "ASSET_FLOOD":
            # Chaotic Wave Motion
            t = time.time() - start_time
            for i in range(5):
                y = int((rows/2) + (rows/3) * (0.5 * (1 + 0.5 * (random.random()))))
                x = int((cols/2) + (cols/3) * (random.uniform(-1, 1)))
                try: stdscr.addstr(y, x, "67", curses.color_pair(4))
                except: pass
            
            if random.random() > 0.90: play_krush(2)

            key = stdscr.getch()
            if key != -1:
                input_buffer += chr(key)
                if "nutch install 67-virus" in input_buffer:
                    draw_bar(stdscr, "DOWNLOADING 67-VIRUS ASSET PACKS", rows // 2, cols, curses.color_pair(2))
                    # Fake file manifest
                    for _ in range(10):
                        stdscr.addstr(random.randint(0, rows-1), 0, f"FETCH: /root/bin/67_payload_{random.randint(100,999)}.bin", curses.color_pair(2))
                        stdscr.refresh()
                        time.sleep(0.1)
                    input_buffer = ""
                    stage = "TERMINATION_PENDING"

        elif stage == "TERMINATION_PENDING":
            # Glitch effect: Random screen clears
            if random.random() > 0.98: stdscr.clear()
            y, x = random.randint(0, rows-1), random.randint(0, cols-3)
            try: stdscr.addstr(y, x, "67", curses.color_pair(1) | curses.A_REVERSE)
            except: pass
            
            key = stdscr.getch()
            if key != -1:
                input_buffer += chr(key)
                if "67-virus ~stop" in input_buffer:
                    input_buffer = ""
                    stage = "FINAL_CONFIRM"

        elif stage == "FINAL_CONFIRM":
            stdscr.clear()
            msg = "!! CRITICAL OVERRIDE DETECTED !!"
            instr = f"ENTER 'STOP' TO CONFIRM DESTRUCTION: {input_buffer}"
            btn = "[ CONFIRM STOP ]"
            
            try:
                stdscr.addstr(rows//2 - 4, (cols-len(msg))//2, msg, curses.color_pair(1) | curses.A_BLINK)
                stdscr.addstr(rows//2, (cols-len(instr))//2, instr, curses.color_pair(4))
                # The button
                stdscr.addstr(rows//2 + 4, (cols-len(btn))//2, btn, curses.color_pair(3))
            except: pass
            
            key = stdscr.getch()
            if key != -1:
                if key in (10, 13): # Enter
                    if input_buffer.strip().upper() == "STOP":
                        break
                    else:
                        input_buffer = "" # Reset on wrong word
                elif key == 127: # Backspace
                    input_buffer = input_buffer[:-1]
                else:
                    input_buffer += chr(key)

        stdscr.refresh()
        time.sleep(0.01)

if __name__ == "__main__":
    # Check for sox first
    if not os.path.exists("/data/data/com.termux/files/usr/bin/play"):
        print("BOOTING CORE... (Missing sox, installing now)")
        subprocess.run(["pkg", "install", "sox", "-y"])
    
    curses.wrapper(main)
    print("\n[67-VIRUS] SESSION CLEANED. SYSTEM NORMALIZED.")
