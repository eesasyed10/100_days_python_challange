import random
fruits=["apples","banana","papaya","melon","strawberry"]


fruits_outcome=random.choice(fruits)


print(fruits_outcome)


fruits_length=len(fruits_outcome)


holder_1=""


for trying in range (fruits_length):
    holder_1+= "_ "

print(holder_1)

holder_2=0
guess_holder=""
while holder_2<4:
    holder_2+=1
    guess_1=input("enter your guess: ").lower()
    for letter in fruits_outcome:
        if guess_1==letter:
            guess_holder+=guess_1
            print(guess_1)
        else:
            guess_holder+="_ "
            print("_ ")

else:
    print("you have run out of tries.")
print(guess_holder)