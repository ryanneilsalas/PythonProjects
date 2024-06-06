from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score_l()
        self.show_score_r()

    def l_scores(self):
        self.clear()
        self.l_score += 1
        self.show_score_l()
        self.show_score_r()

    def r_scores(self):
        self.clear()
        self.r_score += 1
        self.show_score_l()
        self.show_score_r()

    def show_score_l(self):
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))

    def show_score_r(self):
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))
