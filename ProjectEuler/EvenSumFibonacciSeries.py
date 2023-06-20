#To print the fibonacci sequence of a number and the even sum of it
def print_fibonacci(n: int)->int:
    if n<=1:
        return n
    else:
        return print_fibonacci(n-1) + print_fibonacci(n-2)
    
nterms = int(input("Enter the number of terms: "))
sum_fibo = 0
for i in range(nterms):
    fibo = print_fibonacci(i)
    print(fibo)
    sum_fibo += fibo if fibo%2==0 else 0
        
print(sum_fibo)
