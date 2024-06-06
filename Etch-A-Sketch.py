from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_right():
    tim.right(20)


def move_left():
    tim.left(20)


def clear():
    tim.reset()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards,  "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
