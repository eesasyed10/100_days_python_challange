from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# user_input=input("enter one of the coffee (latte/espresso/cappuccino):  ")
is_on=True
money_machine=MoneyMachine()
menu=Menu()
coffeemaker=CoffeeMaker()
# print(menu)
# menu.name()
while is_on:
    ui=input(f"enter the coffee you want ({menu.get_items()}):  ")
    if ui == "report":
        coffeemaker.report()
    elif ui == "latte" or ui == "cappuccino" or ui == "espresso":
        item = menu.find_drink(ui)
        if coffeemaker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffeemaker.make_coffee(item)
        # print(a)
    elif ui == "off":
        is_on=False

