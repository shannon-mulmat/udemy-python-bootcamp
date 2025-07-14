"""
Project description:
1. Create a Flask app where the home route displays an <h1> that says "Guess a number between 0 and 9" and display a counting gif of your choice.
2. Generate a random number between 0 and 9 or any range of numbers of your choice.
3. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number.
   If the number is too low, tell the user it's too low, same with too high or if they found the correct number. Make the <h1> text a different color for each page.

Completed: 7/14/2025
"""
from flask import Flask
from random import randint

random_number = randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
           "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnVzeDRrZGZ1dG80bXJjNTA1bjVramJuYzBmZjhyMGltbm96NzFpOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oS6UmylMXZJEN8H2mx/giphy.gif'>"

@app.route("/<int:guess>")
def guessed_number(guess):
    if guess < random_number:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > random_number:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
