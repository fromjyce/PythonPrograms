#Program to generate the Multiplication table of a number
num = int(input("Enter a number: "))
index = int(input("Enter the bottom limit: "))
print("The Multiplication Table of " + str(num) + " upto " + str(index) + " is: ")
for i in range (0,index):
  print (str(num) + " X " + str(i+1) + " = " + str(num*(i+1)))
