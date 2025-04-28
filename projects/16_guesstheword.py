import random

print("\n🔡GUESS THE WORD!🔡")
print("✨Unscramble the letters to find the word!✨")

words = ["Python", "JavaScript", "Coding", "Computer", "Learning", "Practice"]

while True:
    original_word = random.choice(words)

    shuffled_word = list(original_word)
    random.shuffle(shuffled_word)
    shuffled_word = "".join(shuffled_word)

    print(f"Scrambled word: {shuffled_word}")
    user_guess = input(f"What is the word? ").lower().strip()

    if user_guess == original_word.lower():
        print("🎉 Correct! You win!🏆")
    else:
        print(f"Sorry, the word was {original_word.capitalize()}.")
    if not input("Do you want to play again? (y/n) ").lower().startswith("y"):
        print("👋 Thanks for playing, Goodbye!")
        break
    else:
        continue
