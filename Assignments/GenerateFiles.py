'''
Write a program to generate 10 text files in a directory named as “1.txt”, “2.txt”,.. 
“10.txt
'''

import os
def GenerateFile(n):
    for i in range(n):
       fd = os.open("{}.txt".format(i+1), os.O_CREAT | os.O_WRONLY)

GenerateFile(10)