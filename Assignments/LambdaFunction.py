'''
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument
'''
num = int(input("Enter any number: "))
x = lambda a: a+ 15
print(x(num))

'''
Create a lambda function that multiplies argument x with argument y and prints the result
'''
x,y = input("Enter two numbers: ").split()
func = lambda a,b: a*b
print(func(int(x),int(y)))