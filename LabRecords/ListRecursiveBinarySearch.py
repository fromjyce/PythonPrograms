def BinarySearch(lst, low, high,n):
    if low<=high:
        mid = (low+high)//2
        if lst[mid]==n:
            return mid
        elif lst[mid]>n:
            return BinarySearch(lst,low,mid-1,n)
        else:
            return BinarySearch(lst,mid+1,high,n)
    else:
        return -1

n = int(input("Enter the size of the lists: "))
lst = []
for i in range(0,n):
    a = int(input("Enter the element " + str(i+1) + " : "))
    lst.append(a)
print(lst)
search = int(input("Enter the element that you want to search: "))
val = BinarySearch(lst, 0, n-1, search)
if val == -1:
    print(str(search) + " is not present in the list")
else:
    print(str(search) + " is present in the list")
