import random

print(" 🔡 WORD SCRAMBLER 🔡 ")

while True:
    word = input("Enter a word to scramble (or 'q' to quit) ")

    if word.lower() == "q":
        print("👋 Good Bye!")
        break
    else:
        new_word = list(word)
        random.shuffle(new_word)
        new_word = "".join(new_word)
        print(f"Scrambled: {new_word}")
