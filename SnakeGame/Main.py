from turtle import Screen
from Snake import Snake_Brain
from Food import Food
from Scoreboard import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

coordinate = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake_Brain(coordinate, segments)
snake.create_snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        score.add_score()
        snake.extend()
        food.refresh()

    if (snake.segments[0].xcor() > 290
            or snake.segments[0].xcor() < -290
            or snake.segments[0].ycor() > 290
            or snake.segments[0].ycor() < -290):
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
