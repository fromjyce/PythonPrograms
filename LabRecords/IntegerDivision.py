#Program to implement Integer Division
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
q = 0
r = 0
while dividend >= divisor:
  dividend -= divisor
  q+=1
r = dividend
print("Quotient is: " + str(q) + "\nRemainder is: " + str(r))
