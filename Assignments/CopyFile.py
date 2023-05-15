'''
Write a Python program to read a file (assume the file is filled with some contents) and copy the contents to a new file. Write appropriate comments.
'''


file = open("C:\\Users\\jaya2\\MVSC\\SNU\\Sample.txt")
file2 = open("C:\\Users\\jaya2\\MVSC\\SNU\\SampleRead.txt", "x")
for x in file:
    file2.write(x)

with open("C:\\Users\\jaya2\\MVSC\\SNU\\SampleRead.txt") as file2:
    for y in file2:
        print(y)