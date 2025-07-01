import random
fruits=["apples","banana","papaya","melon","strawberry"]


fruits_outcome=random.choice(fruits)


print(fruits_outcome)


fruits_length=len(fruits_outcome)


holder_1=""


for trying in range (fruits_length):
    holder_1+= "_ "

print(holder_1)
guess_holder=""



for every_guess in fruits_outcome:
    guess=input("guess the letter: ").lower()
    if every_guess==guess:
        guess_holder+=every_guess
    else:
        guess_holder+="_ "
print(f"you have guessed{guess_holder}")
print(
    f"You guessed:  '{guess}'.\n  "
    f"The secret word has {len(fruits_outcome)} letters,\n "
    f"so it looks like: {guess_holder}\n"
    f"and the real answer is {fruits_outcome}"
)