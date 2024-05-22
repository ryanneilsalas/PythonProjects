import random
from Art import logo
print (logo)
start = input("Do you want to play a game BlackJack? Type 'y' or 'n': ")
user_cards = []
computer_cards = []
is_game_over = False

def deal_deck():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    r_card= random.choice(cards)
    return r_card
def calc_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score) :
    if user_score > 21 and computer_score > 21:
        return "You went over, You lose"
    
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You Win!"
    elif computer_score == 0 :
        return "You Lose!"
    elif user_score >  21:
        return "You went over, You Lose!"
    elif computer_score >  21:
        return "Opponent went over, You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"
    
for _ in range(2):
    user_cards.append(deal_deck())
    computer_cards.append(deal_deck())
if start == "y":  
    
    while not is_game_over :
     user_score = calc_card (user_cards)
     computer_score = calc_card (computer_cards)
     print(f" Your Cards: {user_cards}, current score: {user_score}")
     print(f" Computer's first  card: {computer_cards[0]}") 
     
     if user_score == 0 or computer_score== 0 or user_score > 21:
         is_game_over = True   
     else: 
         another_card = input("Type 'y' to get another card, type 'n' to pass : ")
         if another_card == "y" :
             user_cards.append(deal_deck())
         else:
             is_game_over = True
             
    while computer_score!= 0  and computer_score < 17:
        computer_cards.append(deal_deck())
        computer_score = calc_card(computer_cards)
    print(f" Your final hand:{user_cards}, final score:{user_score}")
    print(f" Computer's final hand: {computer_cards} final score:{computer_score}")
    print(compare(user_score,computer_score))
    
            
            
elif start == "n":
    is_game_over = True
    print("Please Play my Game :(")
else:
    is_game_over = True
    print("Please choos a valid option.")
    