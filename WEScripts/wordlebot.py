import random


def select(word, criteria):
    return all([any([(char not in word) for i, char in criteria['b']]), all([(char in word) and (char != word[i]) for i, char in criteria['y']]), all([ char == word[i] for i, char in criteria['g']])])

def unique_letter_words(lst_words: list[str]) -> list[str]:
    unq_lst = []
    for word in lst_words:
        if len(word)==len(set(word)):
            unq_lst.append(word)
    return unq_lst

def load_words(fname: str) -> list[str]:
	return [line.strip() for line in open(fname)]

def get_first_word()->str:
     return random.choice(unique_letter_words(load_words("five_word.txt")))

def transform_into_criteria(word: str, response: str,criteria :dict) -> dict:
    info = list(zip(response, enumerate(word)))
    for colour, char in info:
        criteria[colour].append(char)
    return criteria

def trial(word_list: list[str]):
    return random.choice(word_list)

def reduce_list(word_list: list[str], criteria) -> list:
    return [x for x in word_list if select(x, criteria)]

def game(trials = 6):
    word_list = load_words("five_word.txt")
    criteria = {"b": [], "g": [], "y": []}
    word = get_first_word()
    for i in range(trials - 1):
        print(word, end = '')
        response = input("\t")
        criteria = transform_into_criteria(word, response, criteria)
        word_list = reduce_list(word_list, criteria)
        word = trial(word_list)
        if 'ggggg' == response:
            break
game()
