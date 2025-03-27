"""
Topics Covered:
1. HTML escape/unescape

Project Description:
1. Update the quiz game from 1/14/2025 to have a UI
2. Get the quiz questions via the trivia website's API

Completed: 3/25/2025
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
