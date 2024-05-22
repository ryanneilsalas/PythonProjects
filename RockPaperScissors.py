# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random ()
# print(random_float)

# fruits = ["apple","bananas","carrots"]

# # fruits [1] =  "pear"
# fruits.append("pear")
# fruits.extend(["jackfruit","guava"])
# print(fruits)
# fruits = ["Strawberries","Nectarines"]
# vegetables= ["potato","celery"]
# dirty_dozen= [fruits, vegetables]

# Treasure map
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position [0].lower()
# abc = ["a","b","c"]
# letter_index = abc.index(letter)
# print (letter_index)
# number_index = int(position [1]) -1
# map[number_index][letter_index] = "X"

# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock, paper, scissors]
urchoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
int_urchoice = int(urchoice)

if int_urchoice >= 3 or int_urchoice < 0 :
    print("Invalid Number, You lose")
else :
    print(game_images[int_urchoice])

    comps_choice = random.randint(0,2)

    print("Computer Chose:")

    print(game_images[comps_choice])


    if int_urchoice == 0 and comps_choice == 2 :
     print("You win!")
    elif comps_choice == 2 and int_urchoice == 0 :
        print("You lose")
    elif comps_choice > int_urchoice :
     print("You lose")
    elif int_urchoice > comps_choice :
        print("You win!")
    elif int_urchoice == comps_choice :
        print("Draw")

