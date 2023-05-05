def InsertionSort(lst, n):
    for i in range(1,n):
        k = lst[i]
        j = i-1
        while j>=0 and k<=lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = k
    print("Elements of the list after the Insertion Sort: ")
    print(lst)

n = int(input("Enter the size of the elements: "))
lst = []
for i in range(n):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)
print("Elements of the list before the Insertion Sort: ")
print(lst)
InsertionSort(lst,n)