#Program to check whether the input string is palindrome or not
string = input("Enter a string: ")
rev_string = string[::-1]
if rev_string == string:
   		 print(string + " is a palindrome")
else:
 		 print(string + " is not a palindrome")
