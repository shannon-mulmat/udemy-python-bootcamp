"""
Topics Covered:
1. Data types
2. Type error, checking, and data type conversion
3. Mathematical operations
4. Number manipulation

Project Description:
1. We're going to build a tip calculator.
2. If the bill was $150.00, split between 5 people, with 12% tip.
3. Each person should pay: (150.00 / 5) * 1.12 = 33.6
4. After formatting the result to 2 decimal places = 33.60

Completed: 11/18/2024
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))
cost_per_person = round(float((bill + bill * (tip/100)) / people), 2)

print(f"Each person should pay: ${cost_per_person}")
