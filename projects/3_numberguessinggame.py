import random


def guess_number():
    print("\n***** Welcome to the Number Guessing Game! *****")

    try:
        play = input("\nAre you ready to play? (yes/no): ").strip().lower()

        if play != "yes":
            print("\nThank you for visiting our page.\n")
            return

        computer_guess = random.randint(1, 10)
        count = 0
        max_tries = 5

        while count < max_tries:
            try:
                user_guess = int(input("\nGuess the number between 1 and 10: "))
                count += 1

                if user_guess == computer_guess:
                    print(
                        f"\n🎯 You guessed {user_guess}, and the computer guessed {computer_guess}."
                    )
                    print(f"🎉 You won in {count} {'try' if count == 1 else 'tries'}!")
                    break
                elif user_guess < computer_guess:
                    print("🔻 Your guess is too low.")
                else:
                    print("🔺 Your guess is too high.")

                if count < max_tries:
                    print(f"You have {max_tries - count} tries left.")
                else:
                    print(
                        f"\n😢 You've used all your tries. The correct number was {computer_guess}. Better luck next time!"
                    )

            except ValueError:
                print("⚠️ Please enter a valid integer between 1 and 10.")

    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    guess_number()
