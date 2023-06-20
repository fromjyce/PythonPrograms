#What is the Nth Prime Number?
def generateprime(N):
    primes = [2]
    num = 3 
    while len(primes) < N: 
        is_prime = True 
        for i in range(len(primes)):
            if num % primes[i] == 0:
                is_prime = False
                break 
        if is_prime:
            primes.append(num)
        num+=2
    return primes


num = int(input("Enter the Nth position: "))
primes = generateprime(num)
print("The {} Prime Number is: ".format(num), primes[num-1])
 
