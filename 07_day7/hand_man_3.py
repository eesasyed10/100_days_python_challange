import random
word_list=["apple","banana","peach","mango","papaya"]
random_word=random.choice(word_list)
print(random_word)


placeholder=""
for underscore in random_word:
    placeholder+="_ "
print(placeholder)

game_over=False

new_list=[]


while not game_over:
    final_result=""
    user_guess=input("enter the letter you want to guess: \n")
    
    for letter in random_word:
        if letter == user_guess:
            final_result+=user_guess
            new_list.append(user_guess)

        elif letter in new_list:
            final_result += letter

        elif letter != user_guess:
            final_result+= " _ "


    if final_result==random_word:
        game_over=True
    print(f"your final result is\n{final_result} :")
