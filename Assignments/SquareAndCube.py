'''
Write a Python program to square and cube every number in a given list of integers using Lambda.
'''

num = int(input("Enter the size of the list: "))
lst = []
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)

square = lambda x: x**2
cube = lambda y: y**3
print("Squared Numbers in input list: ", [square(x) for x in lst])
print("Cubed Numbers in input list: ", [cube(y) for y in lst])