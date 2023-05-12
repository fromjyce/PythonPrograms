'''
Create a user-defined function that accepts a string as its input and perform the following: add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Return the updated string.
'''

word = input("Enter a string/word: ")
if len(word)>=3:
    if word[-3:] != "ing":
        print(word+"ing")
    else:
        print(word+"ly")
else:
    print("ERROR! The length of the word should be more thatn 3")