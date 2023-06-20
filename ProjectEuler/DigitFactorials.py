# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
import math


def get_digit_factorial_sum(num):
    factorial_sum = 0
    for digit in str(num):
        factorial_sum += math.factorial(int(digit))
    return factorial_sum


def find_curious_digits():
    curious_digits = []
    for num in range(3, 50000):
        if num == get_digit_factorial_sum(num):
            curious_digits.append(num)
    return curious_digits


curious_digit_list = find_curious_digits()
count = len(curious_digit_list)

print(count, curious_digit_list)
