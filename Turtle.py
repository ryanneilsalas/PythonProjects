# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle")


# for square in range(0, 4):
#     tim.forward(100)
#     tim.left(90)
# for square in range(0, 15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# for times in range(3, 10):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     tim.pencolor(r, g, b)
#     for shape in range(0, times):
#
#         turn = 360/times
#         tim.right(turn)
#         tim.forward(100)

# def random_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     picked_color = (r, g, b)
#     return picked_color
#
#
# # tim.width(15)
# tim.speed("fastest")
#
#
# #
# # directions = [0, 90, 180, 270]
# # for _ in range(200):
# #     tim.pencolor(random_color())
# #     tim.forward(30)
# #     tim.setheading(random.choice(directions))
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
