'''
THE COWS AND BULLS
Create a list with several 4 letter words (use internet as the source). Assign a word from the 
list randomly to a variable called wordle.
Obtain a 4- letter input from the user. Write a program to compare the user input and the 
wordle variable. If a character matches and if it is in the same position, increment the variable 
called “Bull”. 
If a character matches and if it is in different positions, increment the variable called “cow”. 
The game gets over when the user gets 4 bulls. Give 10 attempts to the user and if the user 
doesn’t get the word in the ten attempts, print a message saying “You have exceeded the 
limit. Please play a new game.”
'''


import random
def compare_words(word1,wordle):
    bull = cow = 0
    for i in range(len(word1)):
        if word1[i] == wordle[i]:
            bull+=1
        elif word1[i] in wordle:
            cow+=1
    return bull,cow


words = ["food", "home", "long", "need", "side", "idea", "look", "next", "some", "back", "girl", "stop", "open", "mile", "over", "hand", "grow", "know", "page", "walk"]
wordle = random.choice(words)
for i in range(10):
        word = input("Enter a random four letter word: ")
        if len(word) == 4:
            bull, cow = compare_words(word,wordle)
            if bull!=4:
                 print("Random word: ", wordle)
                 print("Bull Score: ", bull)
                 print("Cow Score: ", cow)
                 print("\nPLAY THE GAME AGAIN\n")
            else:
                 print("CONGRATS!!! YOU WON THE GAME!!! YOUR BULL SCORE IS 4")
                 break;                
        else:
            print("ERROR!!, Enter a four letter word!!!")
print("\nYou have exceeded the limit. Please play a new game.\n")