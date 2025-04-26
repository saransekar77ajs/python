import random


def rockpaperscissors():
    print("***** Welcome to Rock/Paper/Scissors Game! *****")
    user_wins = 0
    computer_wins = 0
    count = 0
    options = ["Rock", "Paper", "Scissors"]

    while True:
        play = input("\nDo you want to play? (yes/no): ")
        if play.lower() != "yes":
            if count == 0:
                print("\nThank you for visiting our page. Goodbye! 👋")
                break

            print("\n📊 Final Score:")
            print(f"🏆 You won {user_wins} times.")
            print(f"🤖 Computer won {computer_wins} times.")
            break

        print("\nEnter your choice:")
        print("1. Rock\n2. Paper\n3. Scissors")
        count += 1

        try:
            index = int(input("Enter your choice (1, 2 or 3): "))
            if index < 1 or index > 3:
                print("⚠️ Invalid choice. Please select 1, 2, or 3.")
                continue
            user_pick = options[index - 1]
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        computer_pick = random.choice(options)
        print(f"\nYou picked: {user_pick}")
        print(f"Computer picked: {computer_pick}")

        if user_pick == computer_pick:
            print("😊 It's a tie.")
        elif (
            (user_pick == "Rock" and computer_pick == "Scissors")
            or (user_pick == "Paper" and computer_pick == "Rock")
            or (user_pick == "Scissors" and computer_pick == "Paper")
        ):
            print("🎉 You Win!")
            user_wins += 1
        else:
            print("☹️ You lost.")
            computer_wins += 1


if __name__ == "__main__":
    rockpaperscissors()
