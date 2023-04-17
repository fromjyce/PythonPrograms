#Program to calculate the Sum of Series in a Number
a = []
s = 0
num = int(input("Enter the size of the series: "))
for i in range(0,num):
  no = int(input("Element " + str(i+1) + ": "))
  a.append(no)
  s+=no
mystr = "The Sum of "
print (mystr + ', '.join(str(no) for no in a) + " is " + str(s))
