# Program that uses conditional statements and loops that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lowercase)
lines = []
while True:
	line = input("Enter Lines :")
	if line:
		lines.append(line.lower())
	else:
		break
print("\nLOWER CASE OF THE INPUT SENTENCE: ")
for sentence in lines:
	print(sentence)
