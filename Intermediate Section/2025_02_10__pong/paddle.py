from turtle import Turtle
Y_POSITION = 0
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.left(90)
        self.goto(x_position, Y_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)
