#Program to check whether input letter is vowel or consonant
vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
letter = input("Enter an alphabet: ")
if letter.isalpha():
		if letter in vowel:
			print(letter + " is a vowel")
		else:
			print(letter + " is not a vowel. It is a consonant")
else:
		print("Enter a valid alphabet!!!!")
