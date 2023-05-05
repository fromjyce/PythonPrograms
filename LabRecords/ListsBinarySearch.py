def CheckSearch(lst,n,search):
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == search:
            return mid
        elif lst[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return None
        

n = int(input("Enter the size of the lists: "))
lst = []
for i in range(0,n):
    a = int(input("Enter the element " + str(i+1) + " : "))
    lst.append(a)
lst.sort()
print(lst)
search = int(input("Enter the element that you want to search: "))
val = CheckSearch(lst,n,search)
if val is None:
    print(str(search) + " is not present in the list")
else:
    print(str(search) + " is present in the list")
