'''
Given a list, find the frequency of each element and save it as the list of tuple 
[(number, frequency)].

'''

def frequencycount(lst):
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    listuple = [(k,v) for k,v in element_count.items()]
    print(listuple)

num = int(input("Enter the size of the list: "))
lst = []
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)
frequencycount(lst)
