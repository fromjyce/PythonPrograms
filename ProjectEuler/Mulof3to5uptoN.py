#To print and find the sum of all multiples of 3 or 5 upto n
def printMul(num):
    count = 0
    lstnumbers = []
    for i in range(1,num):
        if i%3==0 or i%5==0:
            lstnumbers.append(i)
            count+=i
    print("Sum: ", count)
    # print("Elements: ", lstnumbers)

num = int(input("Enter the upper limit: "))
printMul(num)
    
