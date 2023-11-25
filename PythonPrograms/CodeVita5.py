def max_earnings(
    N, M, quantity_available, quantity_needed, cost_of_one_unit, selling_price
):
    # Initialize a 2D array to store maximum earnings for each material and quantity
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    # Fill the dp array using dynamic programming
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # If there is enough quantity of material i to make a toy
            if (
                quantity_needed[i - 1] <= quantity_available[i - 1]
                and j >= cost_of_one_unit[i - 1]
            ):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - cost_of_one_unit[i - 1]] + selling_price[i - 1],
                )

    return dp[M][N]


# Input reading
N, M = map(int, input().split())
quantity_available = list(map(int, input().split()))
quantity_needed = list(map(int, input().split()))
cost_of_one_unit = list(map(int, input().split()))
selling_price = list(map(int, input().split()))

# Output the maximum amount Vinni can earn
result = max_earnings(
    N, M, quantity_available, quantity_needed, cost_of_one_unit, selling_price
)
print(result)
