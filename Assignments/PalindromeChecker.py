#Program to check whether a number is palindrome or not
num = int(input("Enter a number: "))
no = num
revnum = 0
while no!=0:
    digit = no%10
    revnum = revnum*10+digit
    no //= 10
if (revnum == num):
    print(str(num) + " is a palindrome number")
else:
    print(str(num) + " is not a palindome number")
