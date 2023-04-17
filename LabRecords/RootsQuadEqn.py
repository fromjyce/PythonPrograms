#Find the roots of an Quadratic Equation
import math
a = int(input("Enter the value of coefficient of x^2 (with sign): "))
b = int(input("Enter the value of coefficient of x (with sign): "))
c = int(input("Enter the value of the constant (with sign): "))
d = b*b-4*a*c
if d > 0 :
    print ("Quadratic Equation has two real roots of different values")
    r1 = (-b+math.sqrt(d))/(2*a)
    r2 = (-b-math.sqrt(d))/(2*a)
    print ("The roots are: \nFirst Root: " + str(r1) + "\nSecond Root: " + str(r2))
elif d == 0 :
    print ("Quadratic Equation has one real root")
    r = (-1*b)/(2*a)
    print ("The Real Root is " + str(r))
else:
    print ("Quadratic Equation has no real roots")
