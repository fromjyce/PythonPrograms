#Program to generate Sine and Cosine Series
import math
def cosine(x,n):
		cosx = 1
		sign = -1
		for i in range(2, n, 2):
			pi=22/7
			y=x*(pi/180)
			cosx = cosx + (sign*(y**i))/math.factorial(i)
			sign = -sign
		return cosx
def sine(x,n):
		sine = 0
		for i in range(n):
			sign = (-1)**i
			pi=22/7
			y=x*(pi/180)
			sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
		return sine
x=int(input("Enter the value of x in degrees: "))
n=int(input("Enter the number of terms: "))
print("The Sum of the Cosine series is ", round(cosine(x,n),2))
print("The Sum of the Sine Series is ", round(sine(x,n),2))
