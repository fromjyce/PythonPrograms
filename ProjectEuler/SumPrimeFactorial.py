import sympy
import math

"""
def sum_factorial():
    sum = 0
    mod_sum = 0
    for num in range(5, pow(10, 8)):
        if sympy.isprime(num):
            for i in range(1, 6):
                sum += math.factorial(num - i)
                mod_sum += sum % num

    return mod_sum
"""


def sum_factorial(num):
    sum = 0
    mod_sum = 0
    if sympy.isprime(num):
        for i in range(1, 6):
            sum += math.factorial(num - i)
    mod_sum = sum % num

    return mod_sum,sum


print(sum_factorial(7))
