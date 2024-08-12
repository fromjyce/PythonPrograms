low = int(input())
high = int(input())

primes = []

for num in range(low, high+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

print(primes)

res = []

for p in range(len(primes)):
    for r in range(len(primes)):
        if (primes[p] - primes[r]) == 6:
            res.append((primes[p], primes[r]) )

print(len(res))
