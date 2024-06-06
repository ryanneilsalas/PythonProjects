from turtle import Turtle


class paddle:

    def __init__(self):
        self.number_paddle = []

        self.coordinate = [(-380, 0), (375, 0)]

        for paddl in self.coordinate:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.penup()
            new_paddle.shapesize(stretch_len=4, stretch_wid=1)
            new_paddle.setheading(90)
            new_paddle.goto(paddl)
            new_paddle.speed("fastest")
            self.number_paddle.append(new_paddle)

    def up1(self):
        if self.number_paddle[0].ycor() < 230:
            self.number_paddle[0].forward(20)

    def down1(self):
        if self.number_paddle[0].ycor() > -230:
            self.number_paddle[0].backward(20)

    def up2(self):
        if self.number_paddle[1].ycor() < 230:
            self.number_paddle[1].forward(20)

    def down2(self):
        if self.number_paddle[1].ycor() > -230:
            self.number_paddle[1].backward(20)
