'''
Write a program to insert a given string before every number present in a list using
list comprehension
'''

word = input("Enter the string/word: ")
num = int(input("Enter the size of the list: "))
lst = []
new_lst = []
for i in range(num):
    a = int(input("Enter Element " + str(i+1) + " : "))
    lst.append(a)
 
for i in lst:
    string = word+str(i)
    new_lst.append(string)

print(new_lst)
