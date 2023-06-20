# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
def generate_binary(num):
    return bin(num)[2:]


def palindrome_checker(num):
    sum_n = 0
    for i in range(10, num + 1):
        if str(i) == str(i)[::-1] and generate_binary(i) == generate_binary(i)[::-1]:
            print(i)
            sum_n += i
    return sum_n


print(palindrome_checker(600))
