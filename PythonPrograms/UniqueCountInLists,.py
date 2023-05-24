def read_file_contents(path):
    with open(path,"r") as file:
        contents = file.read()
    return contents

def count_words(file_path):
    words_freq = {}
    count = 0
    contents = read_file_contents(file_path)
    words = contents.split()
    for i in words:
        count+=1
        if i in words_freq:
            words_freq[i]+=1
        else:
            words_freq[i] = 1
    sorted_words_freq = sorted(words_freq.items(), key=lambda x:x[1], reverse=True)[:20]
    print("Total Number of Words: ",count)
    for word, freq in sorted_words_freq:
        print("'Frequency of",word,'is:',freq)

count_words("Sample.txt")