# def my_function():
#     print("Hello")
#     print("Bye")

# my_function()
# number=6
# while number > 0:
#     print(number)
#     number -= 1



import random
from hangman_words import word_list
from hangman_art import stages,logo
# word_list = ["aardvark", "baboon", "camel", "rhino", "crocodile"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# print(chosen_word)
life = len(stages)
display= []
print(logo+"\n")
for add_display in range(word_length):
    display += "_"
    
end_of_game = False

while not  end_of_game  :
    guess = input("Guess a letter: "+"\n").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
       
    if guess not in display:
        
        if life <=1 :
           
            print (stages[0])
            print("You Lose!")
            end_of_game = True  
            print(f"The Correct answer was {chosen_word}")
        else:   
            life = life -1 
            
            print (f"Sorry letter {guess} is not in the word")
            print (stages[life])
             
 
      
    print (display)        
    if "_" not in display:
        
        print("You Win!!!\n"+"You Win!!!\n"+"You Win!!!\n")
        end_of_game = True  
   
   

   
    
