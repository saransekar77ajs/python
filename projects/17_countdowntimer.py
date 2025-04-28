import time

print("===== ⏱️ COUNTDOWN TIMER ⏱️ =====")
print("✨ Count down from your chosen seconds!✨")

while True:
    try:
        sec = int(input("Enter seconds to countdown from: "))

        print(f"⌛Starting countdown from {sec} seconds!")

        for i in range(sec, 0, -1):
            if i == 1:
                print(f"{i} second remaining....")
                time.sleep(1)
            else:
                print(f"{i} seconds remaining....")
                time.sleep(1)
        print("\n🎉 Countdown Complete! 🎉")

    except ValueError:
        print("Please enter a valid seconds")

    count_again = input("Start another countdown? (y/n) ").lower().strip()

    if not count_again == "y":
        print("👋 Goodbye!")
        break
    else:
        continue
