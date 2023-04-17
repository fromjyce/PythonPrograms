#Program that converts a decimal to its binary equivalent
import math
num = int(input("Enter the number: "))
print("The Binary Equivalent is " + str(num) + " is " + str(bin(num).replace("0b"," ")))
