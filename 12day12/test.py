import random

from guess_the_number import logo

print(logo)

def play_mode(secret, lives):
    while lives > 0:
        guess = int(input(f"You have {lives} lives left. Enter your guess: "))
        if guess == secret:
            print("🎉 YOU GOT IT!")
            return True
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")
        lives -= 1
    return False

def main():
    print(logo)
    while True:
        secret = random.choice(range(1, 101))
        mode = input("Choose EASY or HARD:\n").strip().lower()
        if mode == "easy":
            won = play_mode(secret, 10)
        else:
            won = play_mode(secret, 5)

        if not won:
            print(f"😢 You’ve run out of lives. The correct number was {secret}!")

        if input("Play again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break
        print("\n" * 3)

if __name__ == "__main__":
    main()
