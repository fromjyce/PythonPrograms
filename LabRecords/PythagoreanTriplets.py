#Programs that generate Pythagorean Triplets
import math
def pyth(up):
		c=0
		m=2
		while(c<up):
			for n in range(1,m):
				a=m*m-n*n
				b=2*m*n
				c=m*m+n*n
				if (c>up):
					break
			print(a,b,c)
      m=m+1
up=int(input("Enter the upper limit:  "))
print("The pythagorian triplets till the upper limit of " + str(up) + ": ")
print(pyth(up))

