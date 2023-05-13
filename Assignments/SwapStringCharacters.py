'''
Create a Python program that reads a string sentence and swaps the first and last character of each word in the string and displays the result
'''
word = input("Enter a string/word: ")
formatted_word = word.split(" ")
new_formatted_word = []
for string in formatted_word:
    n = len(string)
    formatted_string = string[n-1:n]+string[1:n-1]+string[0]
    new_formatted_word.append(formatted_string)
joint_format_word = " ".join(new_formatted_word)
print(joint_format_word)
