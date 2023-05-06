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

tup_val = input('Enter a value (enter exit to stop!): ')
tup_x = ()
if tup_val != 'exit':
    tup_x = tuple(tup_val)
while True:
    if tup_val != 'exit':
        tup_val = input('Enter a value (enter exit to stop!): ')
        if tup_val != 'exit':
            tup_x = tup_x + (tup_val,)
    else:
        break
print(tup_x)
search = input("Enter the element of the tuple that you want to search: ")
val = BinarySearch(tup_x,0, len(tup_x) -1, search)
if val == -1:
    print(search + " is not present in the tuple")
else:
    print(search + " is present in the tuple")
