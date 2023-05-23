'''
Write a Python function to sort the words in a string
'''
def Sorted(string):
    split_string = string.split()
    split_string = [i.lower() + i for i in split_string]
    split_string.sort()
    split_string = [w[len(w)//2:] for w in split_string]
    final_string = ' '.join(split_string)

    print("Sorted Order: ", final_string)

string = input("Enter string, separated with spaces: ")
Sorted(string)