"""
Vinni - The Craftsman
Problem Description
Vinni is a craftsman. He makes different types of toys using different materials and sells them in the market. One day he ran out of raw materials, so he went to the market with N rupees.

There he found M types of materials with which he can make toys. Each type of material has different costs and thus the selling price of toys of each type will also vary from one another.

Given,

N - total amount of money with Vinni (in rupees)

M - total types of materials available in the market.

quantity_available - an array denoting the available quantity of each type where ith integer denotes the available quantity of ith type material.

quantity_needed - an array denoting the quantity needed for making the toy of that type where ith integer denotes the quantity of ith material needed to make toy.

cost_of_one_unit - an array denoting the cost of one unit of material where ith integer denotes cost of one unit of ith type material.

selling_price - an array denoting the selling price of toys where ith integer denotes the price of toy made up of ith material.

Help Vinni in choosing the raw materials to avail maximum amount!

Note: Every toy he is going to make will be guaranteed to be sold in the market.

Constraints
1<= N <= 10^4

1<= M <= 10^3

1 <= quantity_available[i] <= 10^3

1 <= quantity_needed[i] <= 10^3

1 <= cost_of_one_unit [i] <= 10^3

1 <= selling_price [i] <= 10^3

It is not guaranteed that initially there will be enough raw material in the market to make a toy of a given type.

Input
First line consists of N and M separated by space.

Next four lines consists of four array viz. quantity_available, quantity_needed, cost_of_one_unit, selling_price.

Output
Print the maximum amount Vinni can earn.

Time Limit (secs)
1

Examples
Example 1

Input

21 3

11 12 13

3 4 5

2 1 2

20 15 12

Output

70

Explanation

Type

Quantity available in the shop

(in units)

Quantity needed to make one toy

(in units)

Cost of one unit of raw material

(in rupees)

Selling price of manufactured toy

(in rupees)

Total quantity selected

(in units)

Cost of selected raw materials

(in rupees)

Amount earned by Vinni by selling toys

(in rupees)

Type 1

11

3

2

20

6

2*6=12

2*20=40

Type 2

12

4

1

15

8

1*8=8

2*15=30

Type 3

13

5

2

12

0

0

0


From the above table, it is clear that Vinni can earn a maximum of 70 rupees. There is no other combination which can earn more than 70 rupees.

Example 2

Input

8 2

10 6

1 2

2 1

25 30

Output

115

Explanation

Type

Quantity available in the shop

(in units)

Quantity needed to make toy

(in units)

Cost of one unit of raw material

(in rupees)

Selling price of manufactured toy

(in rupees)

Total quantity selected

(in units)

Cost of selected raw materials

(in rupees)

Amount earned by Vinni selling toys

(in rupees)

Type 1

10

1

2

25

1

2*1=2

1*25=25

Type 2

6

2

1

30

6

1*6=6

3*30=90

From the above table, it is clear that Vinni can earn a maximum of 115 rupees. There is no other combination which can earn more than 115 rupees.
"""


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
