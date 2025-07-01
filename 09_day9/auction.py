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
dictionary={}
auction_end=False
def highest_bid(bids_dict):
   highest_bidding=0
   winner=""
   for bidder in bids_dict:
      current_bidder= bidder
      current_bidding=dictionary[bidder]
      if current_bidding>highest_bidding:
         highest_bidding=current_bidding
         winner=bidder
      
   print(f"THE {winner} is the winner with {highest_bidding}")

while not auction_end==True:
    name=input("ENTER THE NAME OF THE BIDDER:\n")
    bid=int(input("ENTER THE AMOUNT OF  BID:\n"))

    dictionary[name]=bid

    continue_bidding=input("do you want to continue bidding.\nTYPE 'YES' TO CONTINUE AND 'NO' TO STOP BIDDING:\n")
    if continue_bidding=="yes":
      print('\n' * 100)
    elif continue_bidding=="no":
       highest_bid(dictionary)
       auction_end=True

       break


      
      