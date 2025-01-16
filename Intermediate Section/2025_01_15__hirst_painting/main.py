"""
Project Description:
1. Forge a Hirst painting using the turtle class
    - Use a real Hirst painting to generate your color palette in RGB tuples
    - Have the turtle draw a dot with a random color from the palette, go ahead 50 paces,
      then draw another dot with another random color from the palette
    - The dot should have a radius of 20
    - The painting should be 10 dots by 10 dots

Completed: 1/15/2025
"""
import colorgram
import turtle
import random

timmy = turtle.Turtle()
turtle.speed(100)
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()

def extract_colors_from_image():
    """
    Returns a list of tuples containing RBG colors.
    """
    color_list = colorgram.extract("image.jpg", 100)
    color_tuple_list = []

    for color in color_list:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r, g, b)
        color_tuple_list.append(color_tuple)

    # remove the first color as it's the background color and not a dot color
    background_color = color_tuple_list[0]
    color_tuple_list.remove(background_color)

    return color_tuple_list

def color_dot_row(painting_size):
    color_list = extract_colors_from_image()

    for i in range(painting_size):
        color_choice = random.choice(color_list)
        timmy.dot(20, color_choice)
        timmy.forward(50)

def hirst_painting(painting_size):
    x = -200
    y = -200
    timmy.setpos(x, y)
    for i in range(painting_size):
        color_dot_row(painting_size)
        y += 50
        timmy.setpos(x, y)

hirst_painting(10)

screen = turtle.Screen()
screen.exitonclick()
