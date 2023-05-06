def BinarySearch(lst,n):
    low = 0
    high = len(lst) - 1
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if lst[mid] < n:
            low = mid + 1
        elif lst[mid] > n:
            high = mid - 1
        else:
            return mid
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
val = BinarySearch(tup_x,search)
if val == -1:
    print(search + " is not present in the tuple")
else:
    print(search + " is present in the tuple")