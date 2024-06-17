import html


class Quiz_brain:
    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        quiz_number = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(quiz_number.text)
        return f"Q.{self.question_number}:{q_text}"
        # user_answer = input(f"Q.{self.question_number}:{q_text} (True/False)")
        # self.check_answer(user_answer, quiz_number.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number-1]
        print(f"question number:{user_answer} question list:{correct_answer.answer}")
        if user_answer.lower() == correct_answer.answer.lower():
            self.score += 1
            return True

        else:
            return False
