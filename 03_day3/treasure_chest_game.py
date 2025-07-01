chest = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''









print(chest)
print("welcome to the survival island where even one wrong breath is capable of killing you.")
start=input("you have two options ,choose the direction you want to go .You can either go left or right")
if start=='left':
    print("you barely survived\n walk straight and you will arrive a new path\n 'hearing sounds of Walking'\n you have arivd at the riverside")
    cs1=input("you have two otions ,will you wait or will you swim")
    if cs1=='wait':
        print("congratulations,you have survived another day")
        cs2 =input("you have to choose between two options ,type boat to use a boat or dont use anyhing.")

        if cs2=='boat':
            print("congratiolations ,your boat couldnt survive the waves and you died")

        elif cs2=='dont':
            print("you have survived again,the ship saw you and you were saved")

            print ("thanks for plying")

        else:
            print("you hve entered the wrong input.")

    
    elif cs1=="swim":
        print("you were eaten by sharks .\nGAME OVER")
    else:
        print("you have entered the wrong input")




elif start=='right':
    print("game over ,you have died .")

else:
     print("you have entered the wrong input")