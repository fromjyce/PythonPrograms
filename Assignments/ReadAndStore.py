'''
Write a python program to read contents from a list and store it in a file
'''


file = open("Sample.txt","r")
file1 = open("SampleRS.txt", "x")
for i in file:
    file1.write(i)

file.close()
file1.close()
file1 = open("SampleRS.txt", "r")
for line in file1:
    print(line)
file1.close()