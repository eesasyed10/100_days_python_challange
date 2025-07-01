print("welcome to the tip calculator")
bill =int(input("write the total bill:\n  "))
tip= int(input("how much tip you would like to give? 10% , 15$ , 20%\n  "))
split=int(input("how many people will split the bill?\n"))

calc = (bill*tip/ 100 + bill)/split

print("the amount of money each person has to pay is :  " , float(calc) )