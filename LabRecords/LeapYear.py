#Checking whether the input year is leap year or not
year = int(input("Enter a year: "))
	if year%4==0:
		print(str(year) + " is a leap year")
	else:
		print(str(year) + " is not a leap year")
