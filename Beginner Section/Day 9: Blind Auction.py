
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
