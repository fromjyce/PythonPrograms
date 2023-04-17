#Program to check whether given number is prime number or not
num = int(input("Enter a number: "))
if num == 1:
  print(str(num) + " is neither a prime number nor a composite 	number")
elif num>1:
  for i in range(2,num):
    if (num%i) == 0:
      print(str(num) + " is not a prime number")
      break;
    else:
      print(str(num) + " is a prime number")
else:
  print(str(num) + " is not prime number")
