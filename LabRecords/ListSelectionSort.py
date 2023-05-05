def SelectionSort(lst,n):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if lst[min]>lst[j]:
                min = j
        lst[i],lst[min] = lst[min],lst[i]
    print("Elements after the selection sort: ")
    print(lst)

n = int(input("Enter the size of the list: "))
lst = []
for i in range(0,n):
    a = int(input("Enter the element " + str(i+1) + " : "))
    lst.append(a)
print("The Elements of the array before selection sort: ")
print(lst)
SelectionSort(lst,n)