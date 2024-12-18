"""
Topics Covered:
1. Dictionaries
2. Nested lists and dictionaries

Project Description:
1. Ask the user for their name and bid amount, add these to a dictionary with "name" as the key and "bid amount" as the value.
2. Ask if there are other bidders, if yes clear the screen and ask the next bidder for their name and bid amount, add these to the dictionary.
3. If there are no more bidders, search through the final dictionary for the highest bidder, and print out their name and their bid amount.

Completed: 12/18/2024
"""
from art import logo

print(logo)

def find_highest_bidder(bidding_dictionary):
    max_bid = max(bidding_dictionary.values())
    for key, value in bidding_dictionary.items():
        if value == max_bid:
            max_bidder = key
    return max_bidder, max_bid

bids_dict = {}
more_bids = 'yes'
while more_bids == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids_dict[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    print("\n" * 20)

max_bidder, max_bid = find_highest_bidder(bids_dict)

print(f"The winner is {max_bidder} with a bid of ${max_bid}")
