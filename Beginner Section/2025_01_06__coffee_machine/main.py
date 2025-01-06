from coffee_data import menu, resources
from art import logo

ESPRESSO_WATER = menu['espresso']['ingredients']['water']
ESPRESSO_COFFEE = menu['espresso']['ingredients']['coffee']
ESPRESSO_COST = menu['espresso']['cost']

LATTE_WATER = menu['latte']['ingredients']['water']
LATTE_MILK = menu['latte']['ingredients']['milk']
LATTE_COFFEE = menu['latte']['ingredients']['coffee']
LATTE_COST = menu['latte']['cost']

CAPPUCCINO_WATER = menu['cappuccino']['ingredients']['water']
CAPPUCCINO_MILK = menu['cappuccino']['ingredients']['milk']
CAPPUCCINO_COFFEE = menu['cappuccino']['ingredients']['coffee']
CAPPUCCINO_COST = menu['cappuccino']['cost']

def resource_report():
    print("Water:", resources['water'], 'mL')
    print("Milk:", resources['milk'], 'mL')
    print("Coffee:", resources['coffee'], 'mL')
    print("Money: $", resources['money'])

def make_espresso():
    resources['water'] -= ESPRESSO_WATER
    resources['coffee'] -= ESPRESSO_COFFEE
    resources['money'] += ESPRESSO_COST
    print("Here is your espresso, enjoy!")

def make_latte():
    resources['water'] -= LATTE_WATER
    resources['milk'] -= LATTE_MILK
    resources['coffee'] -= LATTE_COFFEE
    resources['money'] += LATTE_COST
    print("Here is your latte, enjoy!")

def make_cappuccino():
    resources['water'] -= CAPPUCCINO_WATER
    resources['milk'] -= CAPPUCCINO_MILK
    resources['coffee'] -= CAPPUCCINO_COFFEE
    resources['money'] += CAPPUCCINO_COST
    print("Here is your cappuccino, enjoy!")

def calculate_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarter_total = quarters * 0.25
    dime_total = dimes * 0.10
    nickle_total = nickles * 0.05
    penny_total = pennies * 0.01
    return quarter_total + dime_total + nickle_total + penny_total

def calculate_change(customer_coin_total, drink_cost):
    customer_change = round(customer_coin_total - drink_cost, 2)
    if customer_change > 0:
        print(f"Here is your change, ${customer_change}")
    else:
        return

def coffee_machine():
    print(logo, "\nWelcome to the coffee shop!")
    machine_on = True

    while machine_on:
        order = input("What can we get you today? (espresso / latte / cappuccino): ").lower()

        if order == 'report':
            resource_report()
        elif order == 'espresso':
            if resources['water'] - ESPRESSO_WATER >= 0:
                if resources['coffee'] - ESPRESSO_COFFEE >= 0:
                    customer_coin_total = calculate_coins()
                    if customer_coin_total >= ESPRESSO_COST:
                        calculate_change(customer_coin_total, ESPRESSO_COST)
                        make_espresso()
                    else:
                        print("Sorry, that is not enough money. Money refunded.")
                else:
                    print("Sorry, there is not enough coffee.")
            else:
                print("Sorry, there is not enough water.")
        elif order == 'latte':
            if resources['water'] - LATTE_WATER >= 0:
                if resources['milk'] - LATTE_MILK >= 0:
                    if resources['coffee'] - LATTE_COFFEE >= 0:
                        customer_coin_total = calculate_coins()
                        if customer_coin_total >= LATTE_COST:
                            calculate_change(customer_coin_total, LATTE_COST)
                            make_latte()
                        else:
                            print("Sorry, that is not enough money. Money refunded.")
                    else:
                        print("Sorry, there is not enough coffee.")
                else:
                    print("Sorry, there is not enough milk.")
            else:
                print("Sorry, there is not enough water.")
        elif order == 'cappuccino':
            if resources['water'] - CAPPUCCINO_WATER >= 0:
                if resources['milk'] - CAPPUCCINO_MILK >= 0:
                    if resources['coffee'] - CAPPUCCINO_COFFEE >= 0:
                        customer_coin_total = calculate_coins()
                        if customer_coin_total >= CAPPUCCINO_COST:
                            calculate_change(customer_coin_total, CAPPUCCINO_COST)
                            make_cappuccino()
                        else:
                            print("Sorry, that is not enough money. Money refunded.")
                    else:
                        print("Sorry, there is not enough coffee.")
                else:
                    print("Sorry, there is not enough milk.")
            else:
                print("Sorry, there is not enough water.")
        elif order == 'off':
            print("Coffee machine is shutting down.")
            machine_on = False
        else:
            print("Sorry, we don't make that.")

coffee_machine()
