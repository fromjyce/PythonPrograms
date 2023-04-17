#Write a Python function that takes a string and an integer ‘n’. The function should return a string after removing the ‘n’th character in the string. 
str = input("Enter a string: ")
num = int(input("Enter a number: "))
word = str[:num-1] + str[num:]
print(word)   
