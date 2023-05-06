def SelectionSort(tup):
    n = len(tup)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if tup[j] < tup[min_idx]:
                min_idx = j
        if min_idx != i:
            tup_lst = list(tup)
            tup_lst[i], tup_lst[min_idx] = tup_lst[min_idx], tup_lst[i]
            tup = tuple(tup_lst)
    print("Elements after the selection sort: ")
    print(tup)

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
print("Elements before Selection Sort: ", tup_x)
SelectionSort(tup_x)