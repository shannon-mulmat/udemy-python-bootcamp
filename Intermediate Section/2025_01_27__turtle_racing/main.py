"""
Project Description:
- Create a racing game using the turtle module. You will make 6 turtles, each with a different color.
- Each turtle will start at the same position on the x-axis, aka the "starting line", and be separated by your choice of distanct on the y-axis.
- Each turn, they will all move forward a random distance between 0 and 10.
- Whichever turtle makes it to the "finish line" first is the winner.
- Before the race begins, the user can guess which turtle will win the race.

Completed: 1/27/2025
"""
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle do you think is going to win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coor = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_coor[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You were right! The winner was {winning_turtle}.")
            else:
                print(f"You were wrong. The winner was {winning_turtle}.")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
