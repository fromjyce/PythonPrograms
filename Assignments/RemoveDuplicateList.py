'''
39)	Write a Python program to eliminate the duplicate values in a numeric sequence stored in a list, but preserve the order of the remaining items. 
The original list should be passed to a function named dedupe(), and the function then returns the updated list.
'''

def dedupe(lst):
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element]+=1
        else:
            element_count[element] = 1
    new_lst = list(element_count)
    print("Elemets of list after removing duplicates: ", new_lst)


num = int(input("Enter the size of the list: "))
lst = []
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)
print("Elements of list before removing duplicates: ", lst)
dedupe(lst)