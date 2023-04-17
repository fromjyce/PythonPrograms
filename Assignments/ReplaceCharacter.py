#Read a string and check if the first character is occurring more than once in the string. If yes, replace the occurrence by ‘$’ from the second instance. 
import re
word = input("Enter a string: ")
word1 = word.lower()
n = word1.count(word1[0])
if n>=2:
    word2 = word1[0] + word1[1:].replace(word1[0],'$')
    print(word2)
else:
    print("No Repeated Occurences")
