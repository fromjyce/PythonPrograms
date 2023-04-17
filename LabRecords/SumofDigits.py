#Program to calculate the sum of digits in a number
def dsum(n):
  s = 0
  for d in str(n):
    s+=int(d)
   return s
num = int(input("Enter a number: "))
sumn = dsum(num)
print("The sum of the digits in " + str(num) + " is " + str(sumn))
