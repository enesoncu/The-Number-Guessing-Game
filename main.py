from art import logo
from random import randint

easy_attempts = 10
hard_attempts = 5

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_attempts
    else:
        return hard_attempts

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("In this game, I'll be thinking of a number between 1 and 100. You'll try to guess!")
    answer = randint(1, 100)
  
    turns = game_difficulty()
    guess = 0
  
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
  
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The answer was {answer}")
            return
        elif guess != answer:
            print("Guess again.")

while True:
    play_game()
    if input("Do you want to play again? Type 'yes' or 'no': ").lower() != "yes":
        print("Thanks for playing!")
        break
