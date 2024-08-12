from itertools import combinations

n = int(input())


res = []

if n % 2 != 0:
    print(1)
else:
    nums = list(range(1,n+1))
    print(nums)
    for j in range(0, n+1, 2):
        comb = combinations(nums,j)
        res.extend(comb)
    print(len(res)-2 + n)

