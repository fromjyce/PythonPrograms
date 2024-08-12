def getMaxProfit(indicators, profit, k):
    n = len(indicators)
    dp = [-float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        current_or = 0
        current_profit = 0
        for j in range(n):
            if mask & (1 << j):
                current_or |= indicators[j]
                current_profit += profit[j]
        
        if current_or <= k:
            dp[mask] = max(dp[mask], current_profit)
    
    return max(dp)

# Example usage:
indicators = [2, 3, 1, 5, 9]
profit = [1, 2, 6, 1, 5]
k = 31

print(getMaxProfit(indicators, profit, k))  # Output: 9
