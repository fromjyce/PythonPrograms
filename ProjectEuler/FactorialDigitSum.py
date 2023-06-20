#Find the sum of the digits of factorial of a number
def calculate_factorial(num):    
    if num == 0:
        return 1
    return num * calculate_factorial(num-1)
   
def calculate_digits(num):
    return sum(list(map(int, str(num).strip())))

num = int(input("Enter Number: "))
print("Sum of digits of factorial of {}: ".format(num), calculate_digits(calculate_factorial(num)))
   