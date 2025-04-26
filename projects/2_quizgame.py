def play_quiz():
    print("\n*****Welcome to the computer quize game.*****")
    play = input("\nAre you ready to play (yes or no?) ")
    scores = 0
    if play.lower() != "yes":
        print("Thank you for visiting our page.")
    else:
        name = input("Enter your name: ")

        print("\n1. What is the full form of CPU? ")
        print(
            "\n1. Cubical Processing Unit.\n2. Computer Power Unit.\n3. Central Processing Unit.\n"
        )
        answer = input("Choose the best answer: ")

        if answer == "3":
            print("You are correct!🎉\n")
            scores += 1
        else:
            print("You got it wrong, better luck next time.\n")

        print("\n1. What is the full form of RAM? ")
        print(
            "\n1. Random Aggressive Machine.\n2. Random Access Memory.\n3. Random Artificial Memory.\n"
        )
        answer = input("Choose the best answer: ")

        if answer == "2":
            print("You are correct!🎉\n")
            scores += 1
        else:
            print("You got it wrong, better luck next time.\n")

        print("\n1. What is the full form of SSD? ")
        print("\n1. Solid State Drive.\n2. System Saved Data.\n3. State Solid Drive.\n")
        answer = input("Choose the best answer: ")

        if answer == "1":
            print("You are correct!🎉\n")
            scores += 1
        else:
            print("You got it wrong, better luck next time.\n")

        print("\n1. What is the full form of USB? ")
        print(
            "\n1. Universal State Bytes.\n2. Universal Serial Bus.\n3. Unlimited System Behaviour.\n"
        )
        answer = input("Choose the best answer: ")

        if answer == "2":
            print("You are correct!🎉\n")
            scores += 1
        else:
            print("You got it wrong, better luck next time.\n")

        print("\n1. What is the full form of HTTP? ")
        print(
            "\n1. HiddenText Transfer Protocol.\n2. HighTime Transfer Protocol.\n3. HyperText Transfer Protocol.\n"
        )
        answer = input("Choose the best answer: ")

        if answer == "3":
            print("You are correct!🎉\n")
            scores += 1
        else:
            print("You got it wrong, better luck next time.\n")

        print(f"You got {scores} questions right, out of 5 questions.")
        print(f"You got {scores/5 * 100}%")


if __name__ == "__main__":
    play_quiz()
