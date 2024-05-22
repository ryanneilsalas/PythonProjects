from art import logo
from game_data import data
import random


def pick_account():
    random_acc = random.choice(data)
    return (random_acc)

def convert(account):
    name = account["name"]
    description = account["description"]
    country = account['country']
    
    return f"{name}, a {description}, from {country}"

def compare(guess,a_followers,b_followers) :
    if a_followers > b_followers :
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_over = False
    account_a = pick_account()
    account_b = pick_account()
    while not game_over:
        if account_a != account_b:
            print(f"Compare A: {convert(account_a)}")
            print("VS")
            print(f"Compare B: {convert(account_b)}")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            name_a = account_a ["name"]
            name_b = account_b ["name"]
            a_followers_count = account_a ["follower_count"] 
            b_followers_count = account_b ["follower_count"] 
            is_correct = compare(guess,a_followers_count,b_followers_count)
            
            if is_correct:
                score +=1
                print(f"\nYou're Right {name_a} has {a_followers_count} followers while {name_b} has {b_followers_count}")
                print(f"Current Score:  {score}\n")
            else:
                print(f"\nSorry, that's wrong, Final score: {score}")
                game_over = True
        else:
            account_a = account_b
            account_b = pick_account()
            
game()