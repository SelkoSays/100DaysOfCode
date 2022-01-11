from functions import *
from clear_function import clearConsole

bidders = {}

while True:
    name = input("Enter your name: ")
    bidders[name] = eval(input("Enter your bid: $"))

    
    while True:
        con = input("Are there any otehr bidders? (Y/N): ").upper()
        if con == "Y" or con == "N":
            break
        else:
            pass

    if con == "Y":
        clearConsole()
    elif con == "N":
        break
    else:
        pass

find_highest_bidder(bidders)