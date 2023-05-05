def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

n = int(input("Enter the size of the list: "))
lst = []
for i in range(n):
    a = int(input("Enter element " + str(i+1) + " : "))
    lst.append(a)
print("Elements of the list before the Quick Sort: ", lst)
print("Elements of the list after the Quick Sort: ", quick_sort(lst))
