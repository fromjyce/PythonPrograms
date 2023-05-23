'''
Write a program to count the frequency of words in a file
'''

def read_file_contents(file_name):
    with open(file_name, "r") as file:
        contents = file.read()
    return contents

def frequency_counter():
    contents = read_file_contents("Sample.txt")
    words = contents.split()

    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    for word, frequency in word_frequency.items():
        print('Frequency of', word, 'is :', frequency)

frequency_counter()

  
