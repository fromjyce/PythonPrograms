'''
Write a Python program to remove duplicates from a list
'''

num = int(input("Enter the size of the list: "))
lst = []
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)

print(list(set(lst)))

