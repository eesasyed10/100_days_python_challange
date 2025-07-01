import random
word_list=["apple","banana","peach","mango","papaya"]
random_word=random.choice(word_list)
print(random_word)
placeholder=""
length=len(random_word)
for length in range(length):
    placeholder+= "_"

print(random_word)

guess=input("guess the letter: ").lower()
print(guess)
word=""
for letter in random_word:
    if guess==letter:
        word+=letter
    else :

        print("_") 