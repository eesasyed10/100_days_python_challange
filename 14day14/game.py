import random
from dictionary import data
vs = """
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ """
logo="""  _    _ _____ _____ _    _ ______ _____  
 | |  | |_   _/ ____| |  | |  ____|  __ \ 
 | |__| | | || |  __| |__| | |__  | |__) |
 |  __  | | || | |_ |  __  |  __| |  _  / 
 | |  | |_| || |__| | |  | | |____| | \ \ 
 |_|  |_|_____\_____|_|  |_|______|_|  \_\
                 / __ \|  __ \           
                | |  | | |__) |          
                | |  | |  _  /           
                | |__| | | \ \           
  _      ____ _  \____/|_|__\_\_ _____   
 | |    / __ \ \        / /  ____|  __ \  
 | |   | |  | \ \  /\  / /| |__  | |__) | 
 | |   | |  | |\ \/  \/ / |  __| |  _  /  
 | |___| |__| | \  /\  /  | |____| | \ \  
 |______\____/   \/__\/__ |______|_|  \_\ 
   / ____|   /\   |  \/  |  ____|         
  | |  __   /  \  | \  / | |__            
  | | |_ | / /\ \ | |\/| |  __|           
  | |__| |/ ____ \| |  | | |____          
   \_____/_/    \_\_|  |_|______|   """
# format the data into presentable form 
def format_data(account):
    """takes users data and converts it into presentable format"""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_descr} , from {account_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
score =0
account_b = random.choice(data)
continue_gaming=True
while continue_gaming:
    # genarate a random data from an integer
    account_a = account_b
    account_b = random.choice(data)
    if account_a==account_b:
        account_b = random.choice(data)

    

    print(f"Compare A : {format_data(account_a)}.")
    print(vs)
    print(f"Against B : {format_data(account_b)}.")


    # ask the user to choose one option
    guess=input("Who has more followers? type 'A' or 'B' :   ").lower()
    print("\n"*30)
    print(logo)
    # check if the user is correct
    # - check by comparing the follower count
    a_follower_count= account_a["follower_count"]
    b_follower_count= account_b["follower_count"]
    # - use if statements to check if the user is correct
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    #  give the user feedback 
    if is_correct:
        score+=1
        print(f"you are right and your current score is : {score}.")
    else:
        print(f"you are wrong.  Final score: {score}")
        continue_gaming=False
# keep score of what we are doing

# make the game repeatable

# make the account on position b to replace the account on position a after we give the correct answer.