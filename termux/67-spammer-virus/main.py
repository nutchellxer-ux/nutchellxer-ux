import sys
import time

def start_spam():
    print("PTA Active: Outputting 67. Press CTRL+C to stop.")
    time.sleep(1) # Give you a second to prepare
    
    try:
        while True:
            # sys.stdout is faster than a standard print for high-volume output
            sys.stdout.write("67\n")
            sys.stdout.flush() 
            # Small sleep to prevent Termux from freezing
            time.sleep(0.01) 
    except KeyboardInterrupt:
        print("\nPTA Stopped.")

if __name__ == "__main__":
    start_spam()
