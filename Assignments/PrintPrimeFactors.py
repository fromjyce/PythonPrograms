#Program that print the prime factor of the input number
def primefactors(n):
    c = 2
    while (n>1):
        if (n%c==0):
            print(c)
            n = n/c
        else:
            c = c+1

n = int(input("Enter a number: "))
primefactors(n)
