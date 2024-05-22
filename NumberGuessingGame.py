import random

print ("Welcome to  the Number Guessing Game")
print("I'm thinking ofa number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

the_number = random.randint(1,100)


def guess (attempts):
  is_game_over = False
  while not is_game_over :
    guess = int(input("Make a guess: "))
    if guess == the_number:
      print(f"You guess the number! , the number was {the_number}")
      is_game_over = True
    elif guess != the_number:
      attempts -= 1
      if attempts < 1:
        print("You Lose! :P")
        is_game_over = True
      else:
        print(f"You have {attempts} attempts remaining to guess the number!")
        if guess > the_number:
         print("Too High")
        elif guess < the_number:
         print("Too Low")
        
      
if difficulty == "easy":
  print("You have 10 attempts remaining to guess the number")
  attempts = 10
  guess(attempts)
 
   
elif difficulty == "hard" :
  print("You have 5 attempts remaining to guess the number")
  attempts = 5
  guess(attempts)
 
else :
  print("Please choose a viable option. ")

#  ============= UDEMY CODE =====================
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()