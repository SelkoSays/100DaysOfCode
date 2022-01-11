def find_highest_bidder(bidding_rercord):
    highest_bid=0
    winner=""
    for bidder in bidding_rercord:
        bid_amount=bidding_rercord[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}")