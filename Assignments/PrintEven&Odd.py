# Write a Python program to print even numbers in a list using ‘for’ loop.

no = int(input("Enter the size of the list: "))
lst = []
for i in range(no):
    a = int(input("Enter Element: " + str(i+1) + " : "))
    lst.append(a)

print("Even numbers in the input list: ")
for i in lst:
    if i % 2 == 0:
        print(i )

print("Odd numbers present in the list: ")
for i in lst:
    if i % 2 != 0:
        print(i )