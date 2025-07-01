from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# user_input=input("enter one of the coffee (latte/espresso/cappuccino):  ")
is_on=True
money_machine=MoneyMachine()
menu=Menu()
coffeemaker=CoffeeMaker()


while is_on:
    option=menu.get_items()
    choice=(f"what would you like: ({option}) :-")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink=menu.get_items(choice)
        if coffeemaker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)

    