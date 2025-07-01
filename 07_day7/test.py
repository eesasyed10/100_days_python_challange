import random

secret = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input("Guess a number 1–10: "))
    attempts += 1
    if guess == secret:
        print("You got it!")
        break
    else:
        print("Try again!")
else:
    print("Out of attempts! The number was", secret)
