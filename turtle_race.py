from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet ", "Which turtle will win the race? Enter a color "
                                              "red/orange/yellow/green/blue/purple: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["ryan", "matt", "hej", "elealeh", "mariane", "ventex"]
coordinate = [-60, -30, 0, 30, 60, 90]
number = 0

if user_bet:
    is_race_on = True
    while number < len(colors):
        turtles[number] = Turtle(shape="turtle")
        turtles[number].color(colors[number])
        turtles[number].penup()
        turtles[number].goto(-210, coordinate[number])
        number += 1


while is_race_on:
    for turtle_player in turtles:
        if turtle_player.xcor() > 230:

            is_race_on = False
            winning_color = turtle_player.pencolor()

            if winning_color == user_bet:

                print(f"You've won!  The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost :(  The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle_player.forward(random_distance)


screen.exitonclick()
