def InsertionSort(tup):
    sorted_lst = [tup[0]]
    for elem in tup[1:]:
        i = 0
        while i < len(sorted_lst) and elem >= sorted_lst[i]:
            i += 1
        sorted_lst.insert(i, elem)
    print("Elements after Insertion Sort: ", tuple(sorted_lst))

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
print("Elements before Insertion sort: ", tup_x)
InsertionSort(tup_x)
