from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is a paragraph.</p>'\
           '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTExZnl1cXcyaXp4OTAzamdueDdwNnBkdGlyOG84eXNvc3NiNjRpOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yFQ0ywscgobJK/giphy.gif">'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_italics(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_italics
@make_underlined
def say_bye():
    return "Bye!"

# Create variable paths and converting the path to a specific data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello there, {name}, you are number {number}!'

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)


"""
# Advanced Python decorator with *args and **kwargs

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Shannon")
new_user.is_logged_in = True
create_blog_post(new_user)
"""
