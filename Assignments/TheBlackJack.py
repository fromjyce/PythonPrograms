import random
def generate_random_cards():
  cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  return random.sample(cards, 2)

def calculate_total(cards):
  total = 0
  for card in cards:
    if card == 'A':
      total += 11
    elif card in ['J', 'Q', 'K']:
      total += 10
    else:
      total += int(card)
  return total

def print_options():
  print("What do you want to do? ")
  print("1. Deal")
  print("2. Stand")

while True:
  print_options()

  inpcho = input("Enter your choice: ")

  if inpcho == "1":
    cards = generate_random_cards()
    total = calculate_total(cards)
    print("Your Score is " + str(total) + " Try Again")
  elif inpcho == "2":
    print("Stand")
    break
  else:
    break

if total <= 21:
  print("You Win!")
else:
  print("You Lose!")