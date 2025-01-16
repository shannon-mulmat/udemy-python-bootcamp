"""
Initial turtle commands to get ued to the class/methods/attributes

Completed: 1/15/2025
"""
import turtle
from random import choice, randint

timmy = turtle.Turtle()
timmy.shape("turtle")

# 1. Draw a square
def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.left(90)

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 2. Draw a dashed line
def draw_dashed_line():
    for i in range(20):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 3. Draw all shapes from a triangle to a decagon, have random colors for each shape
def draw_shape(number_of_sides):
    colors = ["dodger blue", "dark green", "firebrick", "tomato", "blue violet",
              "light blue", "dark cyan", "aquamarine", "bisque", "hot pink"]
    angle = 360 / number_of_sides
    timmy.color(choice(colors))
    for i in range(number_of_sides):
        timmy.forward(100)
        timmy.left(angle)

def draw_all_the_shapes():
    for i in range(3, 11):
        draw_shape(i)

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 4. Random walk with random RGB colors
def random_color():
    """
    Returns a random RGB color
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def random_walk():
    directions = [0, 90, 180, 270]
    timmy.pensize(10)
    timmy.speed(10)
    turtle.colormode(255)
    for i in range(200):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(choice(directions))

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 5. Draw a spirograph with random RGB colors
def draw_spirograph():
    turtle.colormode(255)
    timmy.speed(100)
    heading = 5
    iterations = int(360 / heading)
    for i in range(iterations):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(heading)
        heading += 5

""""""""""""""""""""""""""""""""""""""""""""""""""""""

def main():
    draw_square()
    timmy.reset()
    draw_dashed_line()
    timmy.reset()
    draw_all_the_shapes()
    timmy.reset()
    random_walk()
    timmy.reset()
    draw_spirograph()

main()
screen = turtle.Screen()
screen.exitonclick()
