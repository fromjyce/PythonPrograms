'''
Write a Python program to find the binary equivalent of a number using recursion.
'''

def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')


decimal_number = int(input("Enter a decimal number: "))
print("Binary equivalent:", end=' ')
decimal_to_binary(decimal_number)
