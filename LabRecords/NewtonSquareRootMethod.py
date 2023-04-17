#Program to Calculate the Square Root of a number using Newton's Method
def squareroot(n , it = 100):
  a = float(n)
  for i in range(it):
    n = 0.5*(n+a/n)
  return n
num = int(input("Enter the number: "))
root = squareroot(num)
print("The Square Root of " + str(num) + " using Newton's Method is " + str(root))
