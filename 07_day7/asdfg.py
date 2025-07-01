import random
lives =6
# Here i am creating  list of words and randomly choosing one in random word
word_list = ["apple", "banana", "peach", "mango", "papaya"]
random_word = random.choice(word_list)
print(random_word)

# Here i am printing a placeholder as the same length of word chosen above
place_holder = ""
for underscore in random_word:
    place_holder += "_ "
print(place_holder)

# List for storing already existing words
new_final_list = []

# Loop to start the game until game is not over
game_over = False

while not game_over:
    # storing the word in this variable (str)
    final_letter = ""

    # Taking user input (letters)
    user_input = input("enter a letter: \n")

    # Loop to check if the letter is in the word or not
    for letters in random_word:
        if letters == user_input:
            final_letter += user_input
            new_final_list.append(user_input)
        elif letters in new_final_list:
            final_letter += letters
        else:
            final_letter += " _ "
    if user_input not in random_word:
        lives-=1
        if lives==0:

            game_over=True
            print("you lose")
        # print(final_letter)

    if final_letter == random_word:
        game_over = True
        print("you win")

    print(f"you have written {final_letter}")
    print(stages[lives])