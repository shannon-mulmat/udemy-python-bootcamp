from turtle import Turtle, Screen
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def draw_center_line(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.width(5)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for i in range(20):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    def update_scoreboard(self):
        self.draw_center_line()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
