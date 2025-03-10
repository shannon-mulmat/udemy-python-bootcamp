"""
Topics Covered:
1. Pandas library
2. Working with CSVs
3. Data Frames

Project Description:
1. Build a game where the user guesses the 50 US states

Completed: 3/9/2025
"""
import turtle
import pandas as pd
from answers import Answers

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answers = Answers()

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()
already_guessed = []
correct_guesses = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{str(correct_guesses)}/50 States Correct", prompt="Guess a state:").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in states_list:
            if state not in already_guessed:
                states_to_learn.append(state)
        df = pd.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in already_guessed:
        already_guessed.append(answer_state)
        state_row = data[data.state == answer_state]
        answers.write_answer(state_row.x.item(), state_row.y.item(), answer_state)
        correct_guesses += 1
        if correct_guesses == 50:
            answers.win_game()

screen.exitonclick()
