#Program that counts number of even numbers and odd numbers in series of numbers
n = int(input("Enter the size of the series: "))
a = []
for i in range(0,n):
	a.append(int(input("Element " + str(i+1) + ": ")))
evecount=0
oddcount=0
for x in a:
	if x%2==0:
		evecount+=1
	else:
		oddcount+=1
print("No. of Even Numbers: " + str(evecount))
print ("No. of Odd Numbers: " + str(oddcount))

