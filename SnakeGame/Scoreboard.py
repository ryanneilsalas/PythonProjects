from turtle import Turtle

FONT = ("Courier", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            get_highscore = file.read()
        self.highscore = int(get_highscore)
        self.score_number = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write_score()

    def add_score(self):
        self.score_number += 1
        self.write_score()

    def reset(self):
        if self.score_number > self.highscore:
            self.highscore = self.score_number
            with open ("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score_number = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score_number}  High Score: {self.highscore}", False, "center", FONT)
