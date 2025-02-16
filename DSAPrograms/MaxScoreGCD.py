import sys
import heapq
import math

def max_gcd_score(A):
    N = len(A)
    A.sort(reverse=True)  # Sort A in descending order to pick the largest element first
    B = []  # Initialize empty list B
    score = 0

    # Pick the first element from A and add it to B
    B.append(A[0])
    A = A[1:]  # Remove first element from A

    # Max Heap to store potential elements with their best GCD values
    max_heap = []
    
    # Process remaining elements
    while A:
        best_gcd = 0
        best_index = -1
        
        # Find the best element to move to B
        for i in range(len(A)):
            for b in B:
                current_gcd = math.gcd(A[i], b)
                if current_gcd > best_gcd:
                    best_gcd = current_gcd
                    best_index = i
        
        # Add the best GCD value to score
        score += best_gcd
        
        # Move the best element to B
        B.append(A[best_index])
        A.pop(best_index)
    
    return score

# Read input
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

# Compute and print result
print(max_gcd_score(A))
