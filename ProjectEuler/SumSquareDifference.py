#Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.
def sum_of_squares(n):
    sum_of_square = 0
    for i in range(n+1):
        sum_of_square+=i**2
    
    return sum_of_square

def square_of_sum(n):
    sum = 0
    for i in range(n+1):
        sum+=i

    return sum**2

num = int(input("Enter the number: "))
print("Square of the sum: ", square_of_sum(num))
print("Sum of the squares: ", sum_of_squares(num))
print("Difference between the sum of squares of the first {num} natural numbers and the square of the sum: ", square_of_sum(num)-sum_of_squares(num))