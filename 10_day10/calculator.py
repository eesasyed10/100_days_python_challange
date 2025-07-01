logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b 




dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide,


}
def calculator():
    print(logo)
    first_number=float(input("enter your first number\n"))
    continue_calculation=True
    while not continue_calculation==False:
        for dict in dictionary:
            print(dict)
        print("\n" * 1 )
        enter_sign=input("enter what operation do you want to use.")
        second_number=float(input("enter your second number."))

        answer=dictionary[enter_sign](first_number,second_number)
        print(f"{first_number} {enter_sign} {second_number} = {answer}")

        conti=input("enter'y' if you want to continue with the same number and 'n' if you dont want to continue.")
        if conti=="y":
            num1=answer
            calculator()
        
        else:
            continue_calculation=False
            print("\n" * 20)

calculator()