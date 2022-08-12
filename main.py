#clear funtion from replit
from replit import clear

import art

print(art.logo)
print("Welcome to the Silent auction")
bid = {}

next_participant = True 


def bid_fun(bid_val):
    highest_val = 0
    winner = ""
    for bid_entry in bid_val:
        bid_amount = bid_val[bid_entry]
        if bid_amount > highest_val:
            highest_val = bid_amount
            winner = bid_entry
    print(f"The winner is {winner}, highest_value is ${highest_val}")


while next_participant:

    name = input("Enter the name of participant: ")
    amount = int(input("Enter the bid: $"))
    bid[name] = amount

    parti = input("Do you want to add participant name?(yes/no): ")
    if parti == "yes":
        clear() #clear function
    elif parti == "no":
        next_participant = False
        bid_fun(bid)
