import time
import random

def waiting_game():
    target = random.randint(2,4)
    print(f"\nYour Target time is {target} seconds")
    input(' ---PRESS ENTER TO BEGIN--- ')
    start = time.perf_counter()
    input(f"\nPRESS ENTER AGAIN AFTER {target} seconds")
    elapsed = time.perf_counter()-start
    print(f"Elapsed Time: {elapsed :.3f} seconds")
    if elapsed==target:
        print("Unbelievable! Perfect Timing!!")
    elif elapsed<target:
        print(f"{target-elapsed :.3f} seconds too fast")
    else:
        print(f"{elapsed-target :.3f} seconds too slow")

waiting_game()
    
