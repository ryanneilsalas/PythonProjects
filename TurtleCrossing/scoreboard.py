from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)


    def level_up(self):
        self.level += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
