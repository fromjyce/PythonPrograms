#Program that accepts a word from the user and reverses it
word = input("Enter a word: ")
str = " "
for i in word:
		str = i+str
print("The reversed string of " + word + " is " + str)
