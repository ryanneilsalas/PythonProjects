from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
from ui import QuizInterface

question_bank = []

for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
