"""
Topics covered:
- Flask
- Python decorator functions

Completed: 7/7/2025
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye'

if __name__ == '__main__':
    app.run()

"""
# Python decorator function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before function
        function()
        function()
        # do something after function
    return wrapper_function

@delay_decorator
def say_hello():
    print('Hello')

@delay_decorator
def say_bye():
    print('Bye')

def say_greeting():
    print('How are you?')

say_hello()
say_bye()
say_greeting()
"""

"""
# Coding exercise:  Create your own decorator function to measure the amount of seconds that a function takes to execute.
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
  def wrapper():
      start_time = time.time()
      result = func()
      end_time = time.time()
      print(f'{func.__name__} run speed: {end_time - start_time}s')
      return result
  return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
fast_function()
slow_function()
"""
