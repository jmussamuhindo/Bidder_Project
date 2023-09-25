from art import logo
import os

print(logo)

def clear_terminal():
    if os.name == 'nt':   
        os.system('cls')   

def clear_terminal():
    if os.name == 'nt':   
        os.system('cls')

bids = {}
bidding_finished = False

def find_highes_bidder(bidding_record):
    highest_bid = 0
    winner =""
    #bidding_record = {"Angel" : 123, "James" : 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print (f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highes_bidder(bids)
    elif should_continue == "yes":
        clear_terminal()
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            


