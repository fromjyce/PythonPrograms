from itertools import combinations
import sys
input = sys.stdin.read

def main():
    data = input().strip().split()
    
    # Read n, m, c1, c2
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    c1 = int(data[index + 2])
    c2 = int(data[index + 3])
    index += 4
    
    players = []
    
    # Read players' data
    for _ in range(n):
        seed = int(data[index])
        scores = list(map(int, data[index + 1:index + 1 + m]))
        challenge_score = int(data[index + 1 + m])
        total_score = sum(scores) + challenge_score
        players.append((total_score, seed))
        index += 1 + m + 1
    
    # Sort players by total_score descending and by seed ascending
    players.sort(key=lambda x: (-x[0], x[1]))
    
    # Collect top c1 and next c2 players
    finalists = tuple(sorted(seed for _, seed in players[:c1]))
    wildcard = tuple(sorted(seed for _, seed in players[c1:c1 + c2]))
    
    # Use set to store unique combinations of finalists and wildcard
    unique_combinations = set()
    unique_combinations.add((finalists, wildcard))
    
    # Output the number of unique combinations
    print(len(unique_combinations))

if __name__ == "__main__":
    main()
