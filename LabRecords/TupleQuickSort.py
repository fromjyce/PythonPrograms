def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

tup_x = ()
while True:
    tup_val = input('Enter a value (enter exit to stop!): ')
    if tup_val == 'exit':
        break
    else:
        tup_x += (int(tup_val),)
print("Elements before Quick Sort: ", tup_x)
sorted_tup_x = tuple(QuickSort(tup_x))
print("Elements after Quick Sort: ", sorted_tup_x)
