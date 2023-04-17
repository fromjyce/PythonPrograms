#Program to find factorial
def factorial(no):
		if no==0:
			return 1
		else:
			return no*factorial(no-1)
no = int(input("Enter the number: "))
print("The Factorial of " + str(no) + " is", factorial(no))
