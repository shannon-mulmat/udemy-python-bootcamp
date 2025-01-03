"""
Topics Covered:
1. Functions with outputs
2. Multpile return values
3. Docstrings

Project Description:
1. Program asks the user to type the first number.
2. Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
3. Program asks the user to type the second number.
4. Program works out the result based on the chosen mathematical operator.
5. Program asks if the user wants to continue working with the previous result.
   If yes, program loops to use the previous result as the first number and then repeats the calculation process.
   If no, program asks the user for the fist number again and wipes all memory of previous calculations.

Completed: 12/19/2024
"""
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    accumulate = True
    n1 = float(input("What's the first number?: "))

    while accumulate:
        for key in operations:
            print(key)

        symbol = input("Pick an operartion: ")

        n2 = float(input("What's the next number?: "))

        result = operations[symbol](n1, n2)

        print(f"{n1} {symbol} {n2} = {result}")

        calculate_more = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. ").lower()

        if calculate_more == 'y':
            n1 = result
        else:
            accumulate = False
            print('\n' * 20)
            calculator()

calculator()
