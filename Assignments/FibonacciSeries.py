num = int(input("Enter the number of elements: "))
n1, n2 = 0 , 1
count = 0
if num<=0:
    print("Please enter a positive integer")
elif num == 1:
    print("Fibonacci Sequence upto ",num," is ",n1)
else:
    print("Fibonacci Sequence: ")
    while count<num:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count+=1


