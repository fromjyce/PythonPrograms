#Program to calculate the power of a number efficiently
def power(b, p):
   		 if p == 0:
        			return 1
    		elif p % 2 == 0:
        			return power(b, p/2) * power(b, p/2)
    		else:
        			return b * power(b, (p-1)/2) * power(b, (p-1)/2)
b = int(input("Enter the base: "))
p = int(input("Enter the power: "))
print(str(b) + " to the power of " + str(p) + " is ", power(b,p))
