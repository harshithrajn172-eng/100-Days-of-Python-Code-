from art import logo
import random
print(logo)
def blackjack():

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    def compare(u_score, c_score):
        if u_score == c_score:
            return "its a tie"
        elif  c_score==0:
            return "you loose, computer has the blackjack"
        elif u_score==0:
            return "you win, you have the blackjack"
        elif u_score>21:
            return "computer wins"
        elif c_score>21:
            return "you win , computer score was higher than 21!"
        else:
            if u_score>c_score:
                return "you wins, Your score was higher than computer!"
            else:
                return "you lost Computer score was higher"

    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over = False
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    def calculate_score(hand):
        score=sum(hand)
        for card in hand:
            if card == 11 and card==10:
                return 0
            if  card==11:
                hand.remove(card)
                hand.append(1)

        return score

    while not is_game_over:

        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"User card: {user_card}\nUser score:{calculate_score(user_card)}")
        print(f"computer card: {computer_card[0]}")
        if calculate_score(user_card)==0 or calculate_score(user_card)>21:
            is_game_over=True
        else:
            choice = input("do you want to draw another card? Type 'y' or 'n':").lower()
            if choice=="y":
                user_card.append(deal_card())
                calculated_score=calculate_score(user_card)
                print(f"User card: {user_card}\nUser score:{calculated_score}")
                print(f"computer card: {computer_card[0]}")
            else:
                is_game_over=True

    while computer_score!=0 and sum(computer_card)<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(compare(user_score,computer_score))

start=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
if start=="y":
    blackjack()
else:
    print("Thank you for playing")
again=input("Do you want to play again? Type 'y' or 'n':").lower()
cont=True
while cont==True:
    if again=="y":
        blackjack()
        again=input("Do you want to play again? Type 'y' or 'n':").lower()
    else:
        cont=False



















