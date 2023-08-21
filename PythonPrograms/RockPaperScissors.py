# My Project Idea
import random


def computer_guess(lst) -> str:
    return lst[random.randint(0, 2)]


def main():
    result = {"R": "S", "P": "R", "S": "P"}  
    human_count = 0
    computer_count = 0
    count = 0
    while count != 5:
        comp_guess = computer_guess(list(result.values()))
        print(comp_guess)  # erase
        human_guess = str(
            input("Enter your gesture (Rock(R),Scissors(S),Paper(P)) : ")
        ).upper()
        while human_guess not in list(result.values()):
            print("Invalid input. Please try again.")
            human_guess = input(
                "Enter your gesture (Rock(R), Scissors(S), Paper(P)): "
            ).upper()
        count += 1
        if human_guess == comp_guess:
            pass
        elif comp_guess == result[human_guess]:
            human_count += 1
        else:
            computer_count += 1
        print(
            "Your Score: {} \nComputer's Score: {}".format(human_count, computer_count)
        )


main()
