#Number Guessing Game Objectives:
import art
import random

random_number = random.randint(1, 100)

def easy_level():
  lives = 10
  global random_number
  print("You have 10 attempts remaining to guess the number")
  while lives != 0:
    user_guessing = int(input("Make a guess : "))
    if user_guessing == random_number:
      print(f"You got it! The answer was {random_number}.")
      break
    elif user_guessing > random_number:
      print("Too high.")
      print("guess again")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number.")
    elif user_guessing < random_number:
      print("Too low")
      print("guess again.")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number.")

    if lives == 0:
      print(f"The answer is {random_number}")  


def hard_level():
  lives = 5
  global random_number
  print("You have 5 attempts remaining to guess the number.")
  while lives != 0:
    user_guessing = int(input("Make a guess : "))
    if user_guessing == random_number:
      print(f"You got it! The answer was {random_number}.")
      break
    elif user_guessing > random_number:
      print("Too high.")
      print("guess again")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number.")
    elif user_guessing < random_number:
      print("Too low")
      print("guess again.")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number.")

    if lives == 0:
      print(f"The answer is {random_number}")

def play_game():
  global random_number
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  #print(f"pssst, The answer is {random_number}")

  user_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if user_level == "easy":
    easy_level()
  else:
    hard_level()


play_game()
