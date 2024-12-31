"""
Write a blind auction program
We use the dictionary concepts in this program
"""

import os

#os.system("cls") -- to clear the screen

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print("\n")

print("Welcome to the secret auction program\n")

bid = {}
bidding_finished = False # This is known as flags in python if forgot google about it,flags control the flow of the condtional statements

#This is the most challenging part where we have to loop through dictionary and find the highest value
#this is the function to evaluate the highet bid
def highest_bidd(bidding_record): #we somehow need to loop through the dictionary to find the largest bid and name 
    highest_bid  = 0 # to keep track of the highest bid i.e the value of price
    winner = "" # to keep track of the winner of the bid i.e the name of the highest bidder
    for bidder in bidding_record: #when we use for loops in dictionaries it loops through the keys in the dictionary  {"Angela": 123 , "James": 542} here angela and james are keys
        bid_amount = bidding_record[bidder] #this will gives us the values in the dictionary
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid_amount} ")


#This is the looop for checking whether more bidder are there or not
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("what is your bid? : $"))  # here we must convert the type to int which is string by default
    bid[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if should_continue=="no":
        bidding_finished = True
        highest_bidd(bid)
    elif should_continue =="yes":
        os.system("cls")






