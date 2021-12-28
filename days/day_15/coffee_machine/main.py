from utils.clear_screen import clear_screen

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def display_report():
    print(f"Water: {resources['water']} mL \n"
          f"Milk: {resources['milk']} mL \n"
          f"Coffee: {resources['coffee']} g \n"
          f"Money: ${resources['money']}")


def make_coffee(coffee_choice):
    resources["water"] -= MENU[coffee_choice]['ingredients']['water']
    resources["milk"] -= MENU[coffee_choice]['ingredients']['milk']
    resources["coffee"] -= MENU[coffee_choice]['ingredients']['coffee']
    resources["money"] += MENU[coffee_choice]['cost']
    print("Coffee made")
    return resources


def check_water(coffee_choice):
    return resources['water'] >= MENU[coffee_choice]['ingredients']['water']


def check_milk(coffee_choice):
    return resources['milk'] >= MENU[coffee_choice]['ingredients']['milk']


def check_coffee(coffee_choice):
    return resources['water'] >= MENU[coffee_choice]['ingredients']['coffee']


def check_resources(coffee_choice):
    return check_coffee(coffee_choice) and check_milk(coffee_choice) and check_water(coffee_choice)


def process_coins():
    quarter_amount = int(input("How many quarters do you pay: "))
    dime_amount = int(input("How many dimes do you pay: "))
    nickel_amount = int(input("How many nickels do you pay: "))
    cent_amount = int(input("How many cents do you pay: "))

    total_amount = round((0.25 * quarter_amount) +
                         (0.1 * dime_amount) +
                         (0.05 * nickel_amount) +
                         (0.01 * cent_amount), 2)

    return total_amount


def transaction(coffee_choice, paid_amount):

    resources_available = check_resources(coffee_choice)

    if MENU[coffee_choice]['cost'] > paid_amount:
        print("You do not have enough money. Cannot make coffee")

    elif not resources_available:
        print("Not enough resources available. Cannot make coffee")

    else:
        if round(paid_amount - MENU[coffee_choice]['cost'], 2) > 0:
            print(f"Here is ${round(paid_amount - MENU[coffee_choice]['cost'], 2)} in change")

        global resources
        resources = make_coffee(coffee_choice)


def coffee_machine():

    coffee_choice_input = input("What coffee do you want? Espresso, latte, or cappuccino. R for report.").lower()

    if coffee_choice_input == "espresso" or coffee_choice_input == "latte" or coffee_choice_input == "cappuccino":
        money_paid = process_coins()
        transaction(coffee_choice_input, money_paid)
    elif coffee_choice_input == "r":
        display_report()
    else:
        pass


making_coffee = True

while making_coffee:

    coffee_machine_input = input("Do you want to make a coffee (y or n)?").lower()

    if coffee_machine_input == "y":
        clear_screen()
        coffee_machine()
    else:
        break
