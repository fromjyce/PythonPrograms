#Program to calculate the Greatest Common Divisor
def fgcd(x,y):
		while(y):
			x,y = y, x%y
		return x
num = int(input("Enter the number of integers that will be used: "))
lst = []
for i in range (0,num):
  no = int(input("Integer " + str(i+1) + ": "))
  lst.append(no)
n1 = lst[0]
n2 = lst[1]
gcd = fgcd(n1,n2)
for i in range (2, len(lst)):
  gcd = fgcd(gcd,lst[i])
mystr = "GCD of "
print (mystr + ', '.join(str(no) for no in lst) + " is " + str(gcd)) 
