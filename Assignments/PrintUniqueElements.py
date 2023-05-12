'''
Accept a list of values from the user and print only the unique elements from the list.
'''
num = int(input("Enter the size of the list: "))
lst = []
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)

unq_values = list(set(lst))
print("Unique Values in the Input List: ", unq_values)