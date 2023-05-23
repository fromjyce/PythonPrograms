'''
Write a python program to print the prime factors of an integer number
'''

def prime_fac(num):
    factors = []
    divisor = 2
    while divisor<=num:
        if num%divisor==0:
            factors.append(divisor)
            num = num//divisor
        else:
            divisor+=1
    return factors

num = int(input("Enter a number: "))
factors = prime_fac(num)
print("Factors of ", num, " is ", factors)
