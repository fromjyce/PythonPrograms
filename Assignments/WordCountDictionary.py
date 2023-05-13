'''
Create a word count dictionary using a string as shown below:
i/p S = ‘the quick brown fox jumps on the lazy dog’
o/p: {'t': 2, 'h': 2, 'e': 2, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 1, 'o': 4, 'w': 1, 'n': 2, 'f': 1, 
'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
'''
def createdic(lst):
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    print(element_count)


string = input("Enter a sentence: ")
formatted_string = string.replace(" ","")
lst = []
for i in formatted_string:
    lst.append(i)
createdic(lst)
