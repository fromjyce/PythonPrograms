# Function to calculate the time Lucy finishes her ride for each test case
def lucy_ride_time(N, V, X):
    if V == 0:
        # If there are no VIPs, Lucy will be the first to ride
        return X
    elif N == 0:
        # If there are no people in the normal queue, Lucy rides after all VIPs
        return V * X
    else:
        pos_luc = V + 1
        x_count = N - (pos_luc * 2)
        total_n_count = N - x_count
        total_n = total_n_count * X
        total_v = V * X
        total_a = total_v + total_n
        return total_a + X


# Input reading and processing
T = int(input())
for _ in range(T):
    N, V, X = map(int, input().split())
    result = lucy_ride_time(N, V, X)
    print(result)
