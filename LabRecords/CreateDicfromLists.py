'''
Create a dictionary from two lists as shown below:
key = [‘a’,’b’,’c’,’d’,’e’,’f’]
value = [1,2,3,4,5,6]
D = {‘a’:1,’b’:2,’c’:3,’d’:4,’e’:5,’f’:6]
Check if the length of key and value are the same before performing the operation. If not, 
print a message mentioning the dictionary cannot be created due to length mismatch
'''

num = int(input("Enter the size of the lists: "))
lst1 = []
lst2 = []
disct = {}
print("Enter the elements of the list one: ")
for i in range(num):
    a = input("Enter Element " + str(i+1) + " : ")
    lst1.append(a)
print("List One : ", lst1)

print("Enter the elements of the list two: ")
for i in range(num):
    b = input("Enter Element " + str(i+1) + " : ")
    lst2.append(b)
print("List Two: ", lst2)

if all(len(item1) == len(item2) for item1, item2 in zip(lst1, lst2)):
    disct = dict(zip(lst1,lst2))
    print(disct)
else:
    print("ERROR!!! LENGTH OF THE ITEMS IN BOTH LISTS ARE NOT MATCHING")


