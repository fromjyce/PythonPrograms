#Write a Python function to get a string made of n copies of the last k characters of a specified string (length must be at least 5)
s = input("Enter a string: ")
if len(s)>=5:
	k = int(input("How many characters (from last) of the input string do you want to repeat? \nEnter your choice: "))
	n = int(input("How many copies of the last " + str(k) + " characters of the input string do you need? \nEnter your choice: "))
	print(s[~k+1:]*n)
else:
  print("Enter a string whose length must be atleast 5")
