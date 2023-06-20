
#Find the sum of all the primes below N.
def print_primes(n):
    sum = 0
    for i in range(2, n+1):
        k = 0
        for j in range(2, i//2+1):
            if i % j == 0:
                k = k + 1
        if k <= 0:
            #print(i, end=" ")
            sum+=i
    print("\nSum of all primes below {}: ".format(n), sum)

num = int(input("Enter the number: "))
print_primes(num)


