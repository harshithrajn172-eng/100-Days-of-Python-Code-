from art import logo

print(logo)

bid = {}


def first_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


continuing = True

while continuing:
    user_name = input("Enter your name: ")
    user_bid = int(input("Enter your bid: $"))

    bid[user_name] = user_bid

    question = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if question == "no":
        continuing = False
        first_highest_bidder(bid)
    elif question == "yes":
        print("\n" * 20)











