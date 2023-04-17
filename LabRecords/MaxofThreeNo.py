#Find the maximum of three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a>b and a>c:
  print(str(a) + " is the maximum of  " + str(a) + ", " + str(b) + " and " + str(c))
elif b>a and b>c:
  print(str(b) + " is the maximum of  " + str(a) + ", " + str(b) + " and " + str(c))
else:
  print(str(c) + " is the maximum of  " + str(a) + ", " + str(b) + " and " + str(c))
