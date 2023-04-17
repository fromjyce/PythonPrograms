#Program to find a substring in a main string without using any in-built functions.
sentence = input("Enter a sentence: ")
find = input("Enter a substring that you want to search: ")
split_value = []
tmp = ' '
for c in sentence:
    		if c == ' ':
        			split_value.append(tmp)
        			tmp = ' '
    		else:
        			tmp += c
if tmp:
   		 split_value.append(tmp)

found = False
for word in split_value:
   		 if find in word:
        			found = True
        			break
if found:
    		print(find + " is present in " + sentence)
else:
    		print(find + " is not present in " + sentence)
