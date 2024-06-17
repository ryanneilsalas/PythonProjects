import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
quiz_response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
quiz_response.raise_for_status()

data = quiz_response.json()
question_data = data["results"]

# question_data = ({"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                   "question": "HTML stands for Hypertext Markup Language.", "correct_answer": "True",
#                   "incorrect_answers": ["False"]},
#                  {"type": "boolean", "difficulty": "easy",
#                   "category": "Science: Computers",
#                   "question": "The programming language Python is based "
#                               "off a modified version of JavaScript.",
#                   "correct_answer": "False", "incorrect_answers": ["True"]}, {
#                      "type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                      "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
#                      "incorrect_answers": ["True"]},
#                  {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                   "question": "In most programming languages, the operator ++ is equivalent to the "
#                               "statement += 1.",
#                   "correct_answer": "True", "incorrect_answers": ["False"]},
#                  {"type": "boolean",
#                   "difficulty": "easy",
#                   "category": "Science"
#                               ": "
#                               "Computers",
#                   "question": "The "
#                               "Windows "
#                               "ME "
#                               "operating system was released in the year 2000.",
#                   "correct_answer": "True",
#                   "incorrect_answers": [
#                       "False"]}, {
#                      "type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                      "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen "
#                                  "resolution.",
#                      "correct_answer": "False", "incorrect_answers": ["True"]},
#                  {"type": "boolean", "difficulty": "easy",
#                   "category": "Science: Computers",
#                   "question": "The Windows 7 operating system has six "
#                               "main editions.",
#                   "correct_answer": "True",
#                   "incorrect_answers": ["False"]},
#                  {"type": "boolean",
#                   "difficulty": "easy",
#                   "category": "Science: Computers",
#                   "question": "The "
#                               "Python "
#                               "programming language gets its name from the British comedy group Monty Python.",
#                   "correct_answer": "True",
#                   "incorrect_answers": [
#                       "False"]}, {
#                      "type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                      "question": "Ada Lovelace is often considered the first computer programmer.",
#                      "correct_answer": "True",
#                      "incorrect_answers": ["False"]},
#                  {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#                   "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
#                   "incorrect_answers": ["True"]})
