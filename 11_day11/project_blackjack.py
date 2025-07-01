import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():

    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards1=random.choice(cards)
    return cards1
def play_game():
    print(logo)
    game_has_ended=False
    user_cards=[]

    computer_cards=[]
    def compare(u_score,c_score):
        if u_score==c_score:
            return ("its a draw")

        elif c_score==0:
            return (f"you loose ,your opponent has blackjack.")
        elif u_score==0:
            return (f"you win,you have blackjack.")
        elif u_score> 21:
            return (f"yo went over ,you loose.")
        elif c_score > 21:
            return (f"the computer went over ,you win.")
        elif u_score > c_score:
            return (f"you win.")
        else:
            return(f"you lost")


    def calculate_score(score):

        if sum(score)==21 and len(score)==2:
            return 0
        if 11 in score and sum(score)>21:
            score.remove(11)
            score.append(1)
        
        return sum(score)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_has_ended:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards are {user_cards} and your score is {user_score}")
        print(f"computer's first card is {computer_cards[0]} .")




        if user_score==0 or computer_score==0 or user_score>21 or computer_score>21:
            game_has_ended=True
        else:
            wanna_play_again=input("type 'y' if you want to play again and 'n' to end the game.")
            if wanna_play_again=="y":
                user_cards.append(deal_card())
                # computer_cards.append(deal_card)

            else:
                game_has_ended=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f"your cards are: {user_cards} and your score is : {user_score}")
    print(f"computer cards are {computer_cards} and his score is {computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play a game of blackjack ,type 'y' to play and 'n' to stop") == "y":
    print("\n"* 20)
    play_game()

