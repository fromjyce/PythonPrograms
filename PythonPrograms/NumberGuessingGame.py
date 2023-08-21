# INfor Aid Tech Task
"""The game should have a clean and user-friendly interface.
It should allow users to input their name and start the game.
It should generate a random number between 1 and 100.
It should allow users to guess the number within 10 attempts.
It should provide feedback to the user after each guess, letting them know if their guess was too high or too low.
It should declare the user as the winner if they guess the number correctly.
It should give the user the option to play again or quit the game."""
import random


def main():  # algorithm behind guessing game
    print("Welcome to the Number Guessing Game!!!")
    random_num = random.randint(0, 100)
    # print(random_num)
    attempts = 0
    while attempts != 10:
        guess_num = int(input("Enter your guess: "))
        if guess_num == random_num:
            print("Congrats!! You won the game")
            chc = input("Do you want to play again? \nEnter your choice: ")
            if chc == "yes" or chc == "Yes" or chc == "YES":
                main()
            break
        elif guess_num < random_num:
            print("Your guess was too low!")
        else:
            print("Your guess was too high")
        attempts += 1
    if attempts == 10:
        choice = input(
            "You Lost the Game!!\nDo you want to play again? \nEnter your choice: "
        )
        if choice == "yes" or choice == "Yes" or choice == "YES":
            main()


main()
