import random 

four_letter_words = [line.strip() for line in open("four_words.txt")]
five_letter_words = [line.strip() for line in open("five_words.txt")]
six_letter_words = [line.strip() for line in open("six_words.txt")]

def unique_letter_words(lst_words: list[str]) -> list[str]:
    unq_lst = []
    for word in lst_words:
        if len(word) == len(set(word)):
            unq_lst.append(word)
    return unq_lst

def load_words(hardness: str) -> list[str]:
    if hardness == "easy":
        return unique_letter_words(four_letter_words)
    elif hardness == "medium":
        return unique_letter_words(five_letter_words)
    else:
        return unique_letter_words(six_letter_words)

def get_user_guess()->str:
    while True:
        guess = input("Enter your guess: ")
        if guess.isalpha() and (len(guess) == 4 or len(guess) == 5 or len(guess) == 6):
            return guess
        else:
            print("Invalid guess. Please enter a 4-letter word.")

def remove_words(word_list:list[str], blacklist:list[str]) -> list[str]:
    return [word for word in word_list if not any(black_letter in word for black_letter in blacklist)]

def count_common(guess: str, target: str) -> str:
    count = 0
    for i in guess:
        if i in target:
            count += 1
    return count

def play_game():
    hardness = input("easy(4) or medium(5) or hard(6)? ")
    word_list = load_words(hardness)
    computer_words = load_words(hardness)
    computer_word = random.choice(computer_words)
    print(computer_word)
    game_over = False  # Variable to track game status

    while not game_over:
        computer_guess = random.choice(word_list)
        print(f"Computer's guess: {computer_guess}")

        common = int(input("Enter the number of cows (-1 for correct): "))

        if common == -1:
            print("You LOST\nComputer Won")
            game_over = True
            break

        while common > 6 or common < 0:
            print("Invalid input! Please enter valid numbers.")
            common = int(input("Enter the number of cows (-1 for correct): "))

        user_guess = get_user_guess()

        common_c = count_common(user_guess, computer_word)
        print(f"Common Word: {common_c}")

        if user_guess == computer_word:
            print("You WON\nComputer LOST")
            game_over = True
            break

        if common == 0:
            word_list = remove_words(word_list, list(computer_guess))

        if len(word_list) == 0:
            print("Oops! The computer has run out of words to guess. You win!")
            game_over = True
            break

play_game()

