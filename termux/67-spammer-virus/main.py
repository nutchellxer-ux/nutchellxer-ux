import time
import sys

def start_pta():
    print("--- PTA Sequence Initialized ---")
    
    try:
        # Ask the user for the number of repetitions
        count = int(input("Enter how many times to display '67': "))
        
        # Ask for the speed (delay in seconds)
        delay = float(input("Enter delay between outputs (e.g., 0.1 for fast, 0.5 for slow): "))

        print(f"\nStarting sequence for '67' ({count} iterations)...\n")
        time.sleep(1)

        for i in range(1, count + 1):
            # Printing '67' with the current iteration number
            sys.stdout.write(f"[{i}] 67\n")
            sys.stdout.flush()
            time.sleep(delay)

        print("\n--- PTA Sequence Complete ---")

    except ValueError:
        print("Error: Please enter numbers only.")
    except KeyboardInterrupt:
        print("\nProcess stopped by user.")

if __name__ == "__main__":
    start_pta()
