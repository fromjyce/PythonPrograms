#Program of Simple Calculator
import math
print("Operations are: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Root of the number \n6. Power \n7. Sine of an angle \n8. Cosine of an angle \n9. Tangent of an angle \n10. Logarithm of a number \n11. Factorial of a number")
c = int(input("Enter your choice: "))
if c==1:
		sum=0
		op=int(input("Enter the number of operands: "))
		for i in range (0,op):
			a = int(input("Operand " + str(i+1) + ": "))
			sum+=a
		print("Sum: " + str(sum))
elif c==2:
		a = int(input("Enter the Minuend: "))
		b = int(input("Enter the Subtrahend: "))
		diff = a-b
		print("Difference: " + str(diff))
elif c==3:
		prod=1
		lst = []
		ops = int(input("Enter the number of operands: "))
		for i in range (0,ops):
			o = int(input("Operand " + str(i+1) + ": "))
			lst.append(o)
		for i in lst:
			prod = prod * i
		print("Product: " + str(prod))
elif c==4:
		divd = int(input("Enter the dividend: "))
		divs = int(input("Enter the divisor: "))
		rem = divd%divs
		quo = divd/divs
		print("Quotient: " + str(quo) +"\nRemainder: " + str(rem))
elif c==5:
		nu = int(input("Enter the radicand: "))
		ind = int(input("Enter the index: "))
		in1 = 1/ind
		st = pow(nu,in1)
		print("Root of " + str(nu) + " to " + str(ind) + " is " + str(st))
elif c==6:
		x = int(input("Enter the base: "))
		y = int(input("Enter the exponent: "))
		p = pow(x,y)
		print("The value of " + str(x) + " to the power of " + str(y) + " is "  + str(p))
elif c==7:
		x = int(input("Enter the value of the angle: "))
		x1 = math.radians(x)
		si = math.sin(x1)
		print ("Sine of " + str(x) + " is " + str(si))
		cc = input("Do you want to find the cosecant of " + str(x) + " [Yes/No]: ")
		if cc == 'Yes' or cc == 'yes' or cc == 'Y' or cc == 'y':
			cosec=1/si
			print("Cosecant of " + str(x) + " is " + str(cosec))
		else:
			exit()
elif c==8:
		x = int(input("Enter the value of the angle: "))
		x1 = math.radians(x)
		cos = math.cos(x1)
		print ("Cosine of " + str(x) + " is " + str(cos))
		cc = input("Do you want to find the secant of " + str(x) + " [Yes/No]: ")
		if cc == 'Yes' or cc == 'yes' or cc == 'Y' or cc == 'y':
			sec=1/cos
			print("Secant of " + str(x) + " is " + str(sec))
		else:
			exit()
elif c==9:
		x = int(input("Enter the value of the angle: "))
		x1 = math.radians(x)
		tan = math.tan(x1)
		print ("Tangent of " + str(x) + " is " + str(tan))
		cc = input("Do you want to find the cotangent of " + str(x) + " [Yes/No]: ")
		if cc == 'Yes' or cc == 'yes' or cc == 'Y' or cc == 'y':
			cot=1/tan
			print("Cotangent of " + str(x) + " is " + str(cot))
		else:
			exit()
elif c==10:
		x = int(input("Enter the number: "))	
		cc = int(input("Do you want to find: \n1. Natural Logarithm of the Number \n2. Base-10 Logarithm of the Number \n3. Base-2 Logarithm of the Number \nEnter your choice: "))
		if cc == 1:
			nl = math.log(x)
			print ("Natural Logarithm of " + str(x) + " is " + str(nl))
		elif cc == 2:
			bt = math.log10(x)
			print ("Base-10 Logarithm of " + str(x) + " is " + str(bt))
		elif cc == 3:
			btw = math.log2(x)
			print("Base-2 Logarithm of " + str(x) + " is " + str(btw))
		else:
			print("Error!! Enter a number between 1 to 3")
elif c==11:
		x = int(input("Enter the number: "))
		fact = math.factorial(x)
		print ("Factorial of " + str(x) + " is " + str(fact))
else:
		print("Error!!! Enter a number between 1 to 11")
