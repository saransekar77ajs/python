import random

print("🪙 COIN FLIP GAME 🎮")

options = ["Heads", "Tails"]

while True:
    try:
        guess = int(input("Guess your toss (1 for Heads / 2 for Tails / 3 to quit)"))
        if guess == 3:
            print("👋 Goodbye!")
            break
        elif guess not in [1, 2, 3]:
            print(
                "Invalid input, please choose 1 for Heads, 2 for Tails and 3 to quit."
            )
            continue
        flip = random.choice(options)
        print(f"\n🪙 Coin shows {flip}")
        if options[guess - 1] == flip:
            print(f"You won! You guessed it correctly.🎉")
        else:
            print(f"You lost! You guessed it wrong.😭")
    except ValueError:
        print("Invalid input, please enter valid guesses.")
