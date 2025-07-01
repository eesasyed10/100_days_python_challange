import random
logo='''
                                                            .   oooo                                                                  .o8                              
                                                          .o8   `888                                                                 "888                              
 .oooooooo oooo  oooo   .ooooo.   .oooo.o  .oooo.o      .o888oo  888 .oo.    .ooooo.       ooo. .oo.   oooo  oooo  ooo. .oo.  .oo.    888oooo.   .ooooo.  oooo d8b     
888' `88b  `888  `888  d88' `88b d88(  "8 d88(  "8        888    888P"Y88b  d88' `88b      `888P"Y88b  `888  `888  `888P"Y88bP"Y88b   d88' `88b d88' `88b `888""8P     
888   888   888   888  888ooo888 `"Y88b.  `"Y88b.         888    888   888  888ooo888       888   888   888   888   888   888   888   888   888 888ooo888  888         
`88bod8P'   888   888  888    .o o.  )88b o.  )88b        888 .  888   888  888    .o       888   888   888   888   888   888   888   888   888 888    .o  888     .o. 
`8oooooo.   `V88V"V8P' `Y8bod8P' 8""888P' 8""888P'        "888" o888o o888o `Y8bod8P'      o888o o888o  `V88V"V8P' o888o o888o o888o  `Y8bod8P' `Y8bod8P' d888b    Y8P 
d"     YD                                                                                                                                                              
"Y88888P'    
'''

game_has_ended=False

def r_n():
   numbers = list(range(1, 101))
   random_number=random.choice(numbers)
   return random_number


def compare(num1,num2):
    if num1>num2:
      return ("TOO HIGH.")
    elif num1<num2:
      return ("TOO LOW.")
    else:
      return ("YOU HAVE ENTERED THE CORRECT NUMBER.")

def run_program():
   user_input=int(input("enter the number: "))
   com=compare(user_input,random_number)
   return com

def easy_mode():
   lives=10
   while not lives==0:
      ab=run_program()
      print(ab)
      if ab=="YOU HAVE ENTERED THE CORRECT NUMBER.":
         return True
         break
      else: 
        lives-=1
      if lives==0:
         return False

def hard_mode():
   lives=5
   
   while not lives==0:
      ab=run_program()
      print(ab)
      if ab=="YOU HAVE ENTERED THE CORRECT NUMBER.":
         game_has_ended=True
         return True 
      else: 
        lives-=1
      if lives==0:
         return False

while not game_has_ended==True:
   
   random_number = r_n()
   print(logo)
   print(random_number)

   game_mode=input("ENTER 'EASY' FOR EASY MODE AND 'HARD' FOR HARD MODE:\n")
   if game_mode=="easy":
      won=easy_mode()
      if not won :
         print(f"the correct answer was: {random_number}.")
      


   elif game_mode=="hard":
      won=hard_mode()
      if not won :
         print(f"the correct answer was: {random_number}.")

   print("THE GAME HAS ENDED , THANKS FOR PLAYING.")
   play_again=input("enter 'y' to play again and 'n' to stop playing.")
   print("\n"*30)
   if play_again=='n':
      game_has_ended=True
    



