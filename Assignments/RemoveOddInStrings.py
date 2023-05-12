'''
Write a Python program to remove characters that have odd index values in a given string.
'''

word = input("Enter a string: ")
new_word = " "
for i in range(len(word)):
    if i % 2 ==0:
        new_word +=word[i]

print(new_word)