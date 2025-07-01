

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

put=int(input("enter 1 for 'rock',  2 for 'paper', 3 for'scissors':\n"))


if put==1:
    print("you have chosen ",rock," and")

elif put==2:
    print("you have chosen ",paper," and")

elif put==3:
    print("you have chosen ",scissors," and")


import random

ra=random.randint(1,3)
if ra==1:
    print("the computer has chosen ",rock)
    



elif ra==2:
    print("the computer has chosen",paper)


elif ra==3:
    print("the computer has chosen",scissors)


else:
    ("you have entered the wong input")



if put> ra:
    print("you won")

elif put== ra:
    print("its a draw")

elif put==1 and ra==3:
    print("you win")

elif put==3 and ra==1:
    print("computer wins")

else:
    print("computer wins")

