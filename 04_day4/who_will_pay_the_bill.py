name1=input("enter the name of the person:\n ")
name2=input("enter the name of the person:\n ")
name3=input("enter the name of the person:\n ")
name4=input("enter the name of the person:\n ")

import random

ra=random.randint(1,4)

if ra==1:
    print(name1 ,"will pay the bill")


elif ra==2:
    print(name2 ,"will pay the bill")

elif ra==3:
    print(name3 ,"will pay the bill")

elif ra==4:
    print(name4 ,"will pay the bill")