MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10,
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




resources ={
    "water":300 ,
    "milk" :200 ,
    "coffee":100,
}
def pay(t_cost):
    total=0


    end_payment=False
    while not end_payment:
        if total==t_cost:
            return total
        ui2=input("ENTER IN WHICH FORMAT DO YOU WANT TO PAY: ").lower()
        if ui2=="penny":
            ui3=input("enter how many penny's does user want to pay: ")*0.01
            total+=ui3
        elif ui2=="nickel":
            ui3=input("enter how many nickel's does user want to pay: ")*0.05
            total+=ui3
        elif ui2=="dime":
            ui3=input("enter how many dime's does user want to pay: ")*0.10
            total+=ui3
        elif ui2=="quarter":
            ui3=input("enter how many quarter's does user want to pay: ")*0.25
            total+=ui3
        elif ui2=="half dollar" or ui2=="half_dollar" or ui2=="hd" or ui2=="halfdollar":
            ui3=float(input("enter how many half dollar's does user want to pay: "))*0.50
            total+=ui3
        elif ui2=="dollar coin" or ui2=="dollar_coin" or ui2=="dc" or ui2=="dollarcoin":
            ui3=float(input("enter how many dollar coin's does user want to pay: "))*1.00
            total+=ui3
        else:
            print("you have entered the wrong input.")
        
def add_ingredient():
        ui0=input("tell me what ingredient do you want to add:  ")

        ui=int(input("enter in how much quantity do you want to add:  "))

        resources[ui0]=ui



def latte():
    a=0
    if MENU["latte"]["ingredients"]["water"] <= resources["water"]:
        # print("water has been used to make latte coffee.")
        amount_required=MENU["latte"]["ingredients"]["water"]
        amount_available=resources["water"]
        subtract=amount_available-amount_required
        resources["water"]=subtract
        a+=1
        # print(resources)
    else:
        print("you dont have enough water.")


    if MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
        # print("milk has been used to make latte coffee")
        amount_required=MENU["latte"]["ingredients"]["milk"]
        amount_available=resources["milk"]
        subtract=amount_available-amount_required
        resources["milk"]=subtract
        a+=1
        # print(resources)
    else:
        print("you dont have enough milk.")

        
    if MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"] and a==2:
        # print("coffee has been used to make latte coffee.")
        amount_required=MENU["latte"]["ingredients"]["coffee"]
        amount_available=resources["coffee"]
        subtract=amount_available-amount_required
        resources["coffee"]=subtract
        a+=1
        
    else:
        print("you dont have enough coffee.")
    cost=MENU["latte"]["cost"]
    if a==3:
        print("WATER , MILK AND COFFEE has been used to make latte coffee.")
        print(f"Your cost is {cost}.")
        payment=pay(cost)
        print(f"The amount you  have paid is: {payment}")


def cappuccino():
    a=0
    if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"]:
        # print("water has been used to make coffee")
        amount_required=MENU["cappuccino"]["ingredients"]["water"]
        amount_available=resources["water"]
        subtract=amount_available-amount_required
        resources["water"]=subtract
        a+=1
        # print(resources)
    else:
        print("you dont have enough water.")


    if MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
        # print("milk has been used to make coffee")
        amount_required=MENU["cappuccino"]["ingredients"]["milk"]
        amount_available=resources["milk"]
        subtract=amount_available-amount_required
        resources["milk"]=subtract
        a+=1
        # print(resources)
    else:
        print("you dont have enough milk.")

        
    if MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"] and a==2:
        # print("coffee has been used to make coffee")
        amount_required=MENU["cappuccino"]["ingredients"]["coffee"]
        amount_available=resources["coffee"]
        subtract=amount_available-amount_required
        resources["coffee"]=subtract
        a+=1
    else:
        print("you dont have enough coffee.")
    cost=MENU["cappuccino"]["cost"]
    if a==3:
        print("WATER , MILK AND COFFEE has been used to make latte coffee.")
        print(f"Your cost is {cost}.")
        payment=pay()
        print(f"The amount you  have paid is: {payment}")

def espresso():
    a=0
    if MENU["espresso"]["ingredients"]["water"] <= resources["water"]:
        # print("water has been used to make coffee")
        amount_required=MENU["espresso"]["ingredients"]["water"]
        amount_available=resources["water"]
        subtract=amount_available-amount_required
        resources["water"]=subtract
        a+=1
        # print(resources)
    else:
        print("you dont have enough water.")


    # if MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
    #     print("milk has been used to make coffee")
    #     amount_required=MENU["latte"]["ingredients"]["milk"]
    #     amount_available=resources["milk"]
    #     subtract=amount_available-amount_required
    #     resources["milk"]=subtract
    #     # print(resources)
    # else:
    #     print("you dont have enough milk.")

        
    if MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"] and a==1:
        # print("coffee has been used to make coffee")
        amount_required=MENU["espresso"]["ingredients"]["coffee"]
        amount_available=resources["coffee"]
        subtract=amount_available-amount_required
        resources["coffee"]=subtract
        a+=2
        
    else:
        print("you dont have enough coffee.")
    cost=MENU["espresso"]["cost"]
    if a==3:
        print("WATER AND COFFEE has been used to make latte coffee.")
        print(f"Your cost is {cost}.")
        payment=pay()
        print(f"The amount you  have paid is: {payment}")
coffee_working=True

while coffee_working:
    user_input1=input("WHAT ACTION WOULD YOU LIKE TO TAKE (REPORT/ADD INGREDIENT/ORDER/EXIT):   ").lower()
    if user_input1=="off":
            coffee_working=False


    elif user_input1=="report":
            for item in resources:
                print(f"{item}:{resources[item]}")


    elif user_input1=="add ingredients" or user_input1=="add_ingredient" or user_input1=="add_ingredients" or user_input1=="add ingredient" or user_input1=="ai":
            # ui0=input("tell me what ingredient do you want to add:  ")
            ingredient_added=True
            while ingredient_added:
                add_ingredient()

                ui10 = input("Do you want to add more ingredtians:").lower()

                if ui10 == "no":
                    ingredient_added = False


    elif user_input1=="order":

        user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
        
        
        if user_input=="latte":
            latte()
        elif user_input=="cappuccino":
            cappuccino()
        elif user_input=="espresso":
            espresso()
        