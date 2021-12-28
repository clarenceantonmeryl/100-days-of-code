from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    drink_input = input(f"What drink do you want: {menu.get_items()} ")

    if drink_input == "report":
        coffee_maker.report()
        money_machine.report()

    elif drink_input == "off":
        break

    else:
        drink = menu.find_drink(drink_input)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            continue
