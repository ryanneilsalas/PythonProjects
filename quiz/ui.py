from tkinter import *
from quiz_brain import Quiz_brain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
LABEL_FONT = ("Arial", 20, "bold")
GREEN = "#39e75f"
RED = "#f01e2c"


class QuizInterface:

    def __init__(self, quiz_brain: Quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Insert Question Here",
                                                     font=FONT,
                                                     width=280)
        self.lbl_score = Label(text="Score: 0", font=LABEL_FONT, bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(column=1, row=0)
        self.btn_true = Button(text="True", bg=GREEN, fg="white",
                               font=LABEL_FONT, pady=20, padx=20, command=self.tap_true)
        self.btn_true.grid(column=0, row=2)
        self.btn_false = Button(text="False", bg=RED, fg="white",
                                font=LABEL_FONT, pady=20, padx=20, command=self.tap_false)
        self.btn_false.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.btn_true.config(state="normal")
            self.btn_false.config(state="normal")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the Quiz :)")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def tap_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def tap_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.btn_true.config(state="disabled")
        self.btn_false.config(state="disabled")
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(2000, self.get_next_question)
