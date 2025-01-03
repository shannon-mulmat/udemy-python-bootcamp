"""
Project Description:
1. Build a game that asks the user to guess who has more followers on Instagram.
2. The program randomly selects 2 accounts from a list of dictionaries and asks the user which account they think has more followers, 'A' or 'B'.
3. If the user guesses correctly they get a point, the program sets 'A' equal to 'B', and generates a new 'B' to compare with the new 'A'.
4. If the user guesses wrong, the game is over.

Completed: 1/3/2025
"""
from art import logo, vs
from game_data import data
from random import randint

def random_account_from_list():
    """
    Returns a random integer from 0 to the length of the list "data"
    """
    return randint(0, len(data))

def set_next_compare(account_b):
    """
    Takes the second random account, sets it as the first account,
    and chooses a new second random account.
    :param account_b: The second random account
    :return: The old second account as the new first account, and a new random second account.
    """
    account_a = account_b
    while account_a == account_b:
        account_b = random_account_from_list()
    return account_a, account_b

def check_answer(item_1, item_2, user_score):
    """
    Compares the follower counts from 2 different accounts.
    :param item_1:
    :param item_2:
    :param user_score:
    :return: Boolean to continue playing or not, and the user's current score
    """
    if data[item_1]['follower_count'] > data[item_2]['follower_count']:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        return True, user_score
    elif data[item_1]['follower_count'] < data[item_2]['follower_count']:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        return False, user_score
    else:
        print("They have the same number of followers!")
        return True, user_score

def format_data(account):
    """
    Takes the account data and returns it formatted in a printable way
    :param account:
    :return: Formatted string with each desired item from the account dictionary
    """
    account_name = data[account]['name']
    account_description = data[account]['description']
    account_country = data[account]['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def game():
    print(logo)
    user_score = 0
    account_a = random_account_from_list()
    account_b = random_account_from_list()

    while account_a == account_b:
        account_b = random_account_from_list()

    continue_playing = True

    while continue_playing:
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        print("\n" * 20)
        print(logo)

        if user_choice == 'A':
            continue_playing, user_score = check_answer(account_a, account_b, user_score)
            account_a, account_b = set_next_compare(account_b)
        elif user_choice == 'B':
            continue_playing, user_score = check_answer(account_b, account_a, user_score)
            account_a, account_b = set_next_compare(account_b)
        else:
            print("Invalid input. Please type 'A' or 'B'.")

game()
