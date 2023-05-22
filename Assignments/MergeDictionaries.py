'''
Write a Python script to merge two Python dictionaries.
'''

dictionary1 = {}
while True:
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dictionary1[key] = value
    continue_input = input("Do you want to continue? (Y/N): ")
    if continue_input == "N" or continue_input == 'n':
        break
print(dictionary1)
dictionary2 = {}
while True:
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dictionary2[key] = value
    continue_input = input("Do you want to continue? (Y/N): ")
    if continue_input == "N" or continue_input == 'n':
        break
print(dictionary2)

dictionary1.update(dictionary2)
print(dictionary1)
