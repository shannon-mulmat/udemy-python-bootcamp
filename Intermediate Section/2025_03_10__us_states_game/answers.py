from turtle import Turtle
STATE_FONT = ("Courier", 12, "normal")
WIN_FONT = ("Courier", 60, "normal")

class Answers(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_answer(self, x_coor, y_coor, correct_answer):
        self.goto(x_coor, y_coor)
        self.write(correct_answer, align="center", font=STATE_FONT)

    def win_game(self):
        self.goto(0,0)
        self.color("red")
        self.write("YOU WIN!", align="center", font=WIN_FONT)
