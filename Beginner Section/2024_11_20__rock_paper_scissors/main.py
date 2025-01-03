"""
Topics Covered:
1. Random Module
2. Lists
3. Length of list
4. Index error
5. Nested lists

Project Description:
1. You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

Completed: 11/20/2024
"""
import random
from art import rock, paper, scissors

game_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
computer_choice = random.randint(0, 2)

print(f"You chose:\n{game_list[user_choice]}")

print(f"Computer chose:\n{game_list[computer_choice]}")

if user_choice == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("You win")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("Draw")
    else:
        print("You lose")
else:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    else:
        print("Draw")
