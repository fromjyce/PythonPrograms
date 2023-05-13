'''
Write a Python function "listdiff(l1,l2)" that takes two lists l1 and l2 as input and 
prints all values that are either in l1 or in l2 but not in both lists. 
You may assume that each input list is sorted in ascending order and has distinct values (i.e., 
no duplicates). You may also assume that the two lists have elements of the same type. 
Your output should also be in ascending order. Do *not* sort the output --- you should 
generate the output values in ascending order
'''

def difflist(lst1,lst2):
    lst1.extend(lst2)
    element_count = {}
    for element in lst1:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    new_list = [element for element in lst1 if element_count[element] == 1]
    print(new_list)


num1 = int(input("Enter the size of the LIST ONE: "))
lst1 = []
lst2 = []
dicst_count = {}
for i in range(num1):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst1.append(a)
print("LIST ONE: ", lst1)
num2 = int(input("Enter the size of the LIST TWO: "))
for i in range(num2):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst2.append(a)
print("LIST TWO: ", lst2)
difflist(lst1,lst2)

