def CheckSearch (lst,n,search):
    for i in lst:
        if i == search:
            return 1
    return -1
        
n = int(input("Enter the size of the lists: "))
lst = []
for i in range(0,n):
    a = int(input("Enter the element " + str(i+1) + " : "))
    lst.append(a)
print("The Elements of the List: ")
print(lst)
search = int(input("Enter the element that you want to search: "))
val = CheckSearch(lst,n,search)
if val == -1:
    print(str(search) + " is not present in the list")
else:
    print(str(search) + " is present in the list")