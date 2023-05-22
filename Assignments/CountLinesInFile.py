'''
Write a program to count the number of lines in a text file.
'''


def CountLines(file):
    count=0
    with open(file,"r") as file:
       contents =  file.readlines()
       for i in contents:
           count+=1
    print(count)
    

CountLines("Sample.txt")