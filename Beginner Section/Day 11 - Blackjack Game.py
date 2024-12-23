"""
Capstone Project

Project Description:
1. Using the rules of Blackjack, create the game in a python file
2. This game will be simplified, assuming a limitless deck of cards instead of a 52-card deck

Completed: 12/23/2024
"""
import random
from art import logo

def play_blackjack():
    """
    Asks the user if they want to run the Blackjack program
    :return: String, user input of 'y' for 'yes' or 'n' for 'no'
    """
    return input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def deal_card():
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def print_score(player_cards, dealer_cards, continue_game):
    """
    Prints the current hand for the player and the player's total score, along
    with either the dealer's first card (if the game is still going), or the
    current hand for the dealer and the dealer's total score
    :param player_cards: List, the cards that the player possesses
    :param dealer_cards: List, the cards that the dealer possesses
    :param continue_game: Boolean, True or False if the game is continuing,
    determines which print statements are returned
    :return: String, two print statements, one for the player's whole hand
    and one for the dealer: only the dealer's first card if the game is
    still going, or their whole hand if the game is over
    """
    if continue_game:
        print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Dealer's first card: {dealer_cards[0]}")
    else:
        print(f"    Your final cards: {player_cards}, final score: {sum(player_cards)}")
        print(f"    Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

def replace_11_with_1(hand):
    """
    Replaces 11 with 1 (the ace card)
    :param hand: List, the list of cards being checked for an 11
    :return: List, the same list that was passed in, but 11 will be replaced with 1
    """
    hand.remove(11)
    hand.append(1)

play_game = play_blackjack()

while play_game == 'y':
    print("\n" * 20, logo)

    player_hand = []
    dealer_hand = []

    for num in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    continue_playing = True

    if sum(player_hand) == 21 and sum(dealer_hand) != 21:
        continue_playing = False

    if sum(player_hand) > 21 and 11 in player_hand:
        replace_11_with_1(player_hand)

    if sum(dealer_hand) > 21 and 11 in dealer_hand:
        replace_11_with_1(dealer_hand)

    while sum(player_hand) < 21 and continue_playing:
        print_score(player_hand, dealer_hand, continue_playing)

        more_cards = input("Type 'y' to get another card, type 'n' to pass: ")

        if more_cards == 'y':
            player_hand.append(deal_card())
            if sum(player_hand) > 21:
                if 11 in player_hand:
                    replace_11_with_1(player_hand)
                else:
                    continue_playing = False
        else:
            continue_playing = False

    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        if sum(dealer_hand) > 21:
            if 11 in dealer_hand:
                replace_11_with_1(dealer_hand)

    if sum(dealer_hand) == sum(player_hand) and sum(player_hand) <= 21:
        print_score(player_hand, dealer_hand, continue_playing)
        print("It's a draw!")
    elif sum(player_hand) > 21:
        print_score(player_hand, dealer_hand, continue_playing)
        print("Bust! You lose.")
    elif sum(player_hand) == 21:
        print_score(player_hand, dealer_hand, False)
        print("You win!")
    elif sum(player_hand) < 21:
        if sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21:
            print_score(player_hand, dealer_hand, continue_playing)
            print("You lose.")
        else:
            print_score(player_hand, dealer_hand, continue_playing)
            print("You win!")

    play_game = play_blackjack()
