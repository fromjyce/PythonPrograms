'''
Write a program to strip unwanted characters from strings based on specified conditions. 
The characters removed can be either from the beginning, end or both. These conditions are 
coded into individual functions as follows:
strip() method can be used to remove characters from the beginning and end of a string. If no 
arguments are provided, then the function removes whitespace, otherwise it removes the 
specified character as an argument. 
lstrip() method removes whitespace or a specified character from the beginning of the string. 
rstrip() method removes whitespace or a specified character from the end of the string.
'''


def stringstrip(word,character):
    formatted_string = word.strip(character)
    print(formatted_string)

def stringleftstrip(word,character):
    formatted_string = word.lstrip(character)
    print(formatted_string)

def stringrightstrip(word,character):
    formatted_string = word.rstrip(character)
    print(formatted_string)


word = str(input("Enter a string: "))
print(word)
choice = int(input("Do you want \n1. Strip \n2. Left Strip \n3. Right Strip \nEnter Your Choice: "))
if choice == 1:
    sliced = input("Enter the character that has to be removed: ")
    stringstrip(word,sliced)
elif choice == 2:
    sliced = input("Enter the character that has to be removed: ")
    stringleftstrip(word,sliced)
elif choice == 3:
    sliced = input("Enter the character that has to be removed: " )
    stringrightstrip(word,sliced)
else:
    print("ENTER A VALID CHOICE!!!")