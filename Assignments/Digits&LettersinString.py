# Program that uses conditional statements and loops that accepts a string and calculates the number of digits and letters
string = input("Enter the string: ")
d = 0
l = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in string:
	if i.isalpha():
		l+=1
	else:
		pass
for i in string:		
	if i in digits:
		d+=1
	else:
		pass
print("The Number of Digits in the given string is", str(d))
print("The Number of Letters in the given string is", str(l))

