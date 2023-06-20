# Function to get sum of digits 
def getSum(n:int)->int:
    return sum(list(map(int, n.strip())))

def power_of_two(n: int)->int:
    return 2**n
   
n = int(input("Enter Exponent: "))
print(getSum(str(power_of_two(n))))
