"""
Topics Covered:
1. Local and global scope
2. Block scope
3. Global variables
4. Global constants

Project Description:
1. The computer chooses a random number between 1 and 100
2. The user chooses a difficulty level, easy for 10 guess attempts and hard for 5 guesse attempts.
3. The user guesses what the computer's number is:
    If the user guesses too high or too low, the program tells them "too high" or "too low", deducts a guess attempt, and if the user still has guess attempts it prompts them to guess again.
    If the user guesses correctly before they run out of guess attempts, they win.
    If the user runs out of guess attempts, they lose.

Completed: 1/2/2025
"""
import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, answer, attempts):
    """
    Checks answer against user's guess
    :return: The number of attempts remaining
    """
    if user_guess > answer:
        print("Too high.")
        return attempts - 1
    elif user_guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The number was {answer}.")

def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def play_game():
    print(logo, "\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    answer = random.randint(1,100)
    user_guess = 0

    while user_guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        attempts = check_answer(user_guess, answer, attempts)

        if attempts == 0:
            print(f"You've run out of guesses! The number was {answer}.")
            return
        elif user_guess != answer:
            print("Guess again.")

play_game()
