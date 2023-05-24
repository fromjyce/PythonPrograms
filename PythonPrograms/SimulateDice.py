from random import randint
from collections import Counter

def roll_dice(*dice,trials=1_000_000):
    counts = Counter()
    for _ in range(trials):
        counts[sum((randint(1,sides) for sides in dice))] +=1
    print("\nOUTCOME PROBABILITY\n")
    for outcome in range(len(dice),sum(dice)+1):
       print(f"{outcome}\t{counts[outcome] * 100/trials :0.2f}%") 

roll_dice(4,6,6)