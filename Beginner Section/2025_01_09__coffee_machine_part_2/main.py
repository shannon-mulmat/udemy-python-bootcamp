"""
Project Description:
1. Recreate the coffee machine program using the provided files which contain classes created by the teacher for running the coffee machine.

Completed: 1/7/2025
"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    drink_options = menu.get_items()
    choice = input(f"Welcome to the coffee machine! What would you like? ({drink_options}): ").lower()

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("Machine is shutting down...")
        machine_on = False
    else:
        drink_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_choice) and money_machine.make_payment(drink_choice.cost):
            coffee_maker.make_coffee(drink_choice)
