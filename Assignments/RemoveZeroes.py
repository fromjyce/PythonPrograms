'''
Assume a list containing several 0s. Push all the zeroes to the end of the list.
Eg: [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
o/p: [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

num = int(input("Enter the size of the list: "))
lst=[]
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)
print(lst)

for i in lst:
    if i == 0:
        lst.remove(i)
        lst.append(i)

print(lst)