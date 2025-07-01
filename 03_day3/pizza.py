print("welcome to our pizza restraunt:  ")


size =input(" size pizza do you want? S, M or L:  ")




if size.lower()=='s':
    bill=100
    pepperoni= input("you want pepperoni on your pizza? Y or n ")
    if pepperoni.lower()=='y':
        bill+=20
    else:
        bill+= 0
    extra_cheese=input("you want extra cheese? Y or N: ")
    if extra_cheese.lower()=='y':
        bill+= 50
    else:
        bill+= 0 
    
    print("your total bill is ", bill)



    

elif size.lower() =='m':
    bill=150
    bill=100
    pepperoni= input("you want pepperoni on your pizza? Y or n ")
    if pepperoni.lower()=='y':
        bill+=20
    else:
        bill+= 0
    extra_cheese=input("you want extra cheese? Y or N: ")
    if extra_cheese.lower()=='y':
        bill+= 50
    else:
        bill+= 0 
    
    print("your total bill is ", bill)

elif size.lower() == 'l':
    bill=200
    bill=100
    pepperoni= input("you want pepperoni on your pizza? Y or n ")
    if pepperoni.lower()=='y':
        bill+=20
    else:
        bill+= 0
    extra_cheese=input("you want extra cheese? Y or N: ")
    if extra_cheese.lower()=='y':
        bill+= 50
    else:
        bill+= 0 
    
    print("your total bill is ", bill)


