"""
Project Description:
1. Use OOP to create a Quiz Game program that has a set list of questions and answers. The program asks the user each question in turn, and tracks when they answer correctly.

Completed: 1/14/2015
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()
