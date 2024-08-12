from itertools import permutations

word = input()

string_list = permutations(word)

for w in string_list:
    print("".join(w))