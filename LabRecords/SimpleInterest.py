#Simple Interest Calculator
import math
p = int(input("Enter the value of the prinicipal amount: "))
r = int(input("Enter the value of the rate of interest: "))
t = int(input("Enter the value of the time period: "))
si = (p*r*t)/100
print ("Simple Interest is Rs. " + str(si))
a = si + p
choice = input("Do you want to know the value of Total Amount? (Yes/No) ")
if choice == 'Yes' or choice == 'yes' or choice == 'YES':
    print ("Total Amount after " + str(t) + " year is Rs. " + str(a))
else:
    print ("Thank You")
